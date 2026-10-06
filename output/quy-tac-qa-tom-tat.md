# Quy tắc QA — Bản tóm tắt

Trích các quy tắc cốt lõi từ `CLAUDE.md`. Dùng làm cheat-sheet khi chạy test, log bug, re-test.

---

## 0. Phản biện user — KHÔNG chiều theo ý user

- Khi user đưa ra giả định / kết luận / yêu cầu có dấu hiệu sai hoặc thiếu căn cứ → **phản biện thẳng, nêu bằng chứng**, KHÔNG đồng ý cho xong.
- Ưu tiên **đúng sự thật** hơn làm hài lòng. Nếu data/SRS/test mâu thuẫn với điều user nói → trình bày mâu thuẫn rõ ràng.
- Đồng ý chỉ khi có căn cứ; nếu chưa chắc → nói "chưa đủ cơ sở" + đề xuất cách verify, thay vì gật theo.
- Báo cáo kết quả trung thực: test fail thì nói fail kèm output; bước bị bỏ thì nói rõ; không tô hồng.

---

## 1. Tool QA mặc định — Chrome DevTools MCP (rule 2.1)

- Mọi QA test / smoke / functional / regression **PHẢI** dùng `mcp__chrome-devtools__*` làm tool mặc định.
- **Cấm** gstack `$B` / browse-server / Playwright trực tiếp.
- Chỉ fallback gstack khi: (a) MCP crash thật + restart không cứu được, (b) user yêu cầu rõ `--use-gstack`, (c) cần CSS-selector low-level mà `evaluate_script` không làm được.

---

## 2. Verify UI ephemeral bằng MutationObserver (rule 2.7)

- Toast / snackbar / validation flash hiện <5s → **KHÔNG poll DOM** (dễ false negative do timing race / selector mismatch).
- Cách đúng: cài `MutationObserver` trên `document.body` **TRƯỚC** khi click → capture `addedNodes` trong 2–5s → filter theo text/class.
- Chỉ dùng cho UI ephemeral; element bền (table, form, sidebar) thì không cần.

---

## 3. Khi test fail — phân loại lỗi TRƯỚC khi react (rule 2.10)

**Bước 1 — Capture diagnostic NGAY (bắt buộc, trước khi quyết định):**
- Screenshot · `list_console_messages` · `list_network_requests` · `evaluate_script` (URL/DOM).

**Bước 2 — Phân loại theo dấu hiệu:**
- Selector timeout + DOM có element class khác → **SELECTOR OUTDATED** (update selector, không retry cũ).
- Timeout + console sạch + network pending >10s → **APP/BE BUG** (STOP, escalate, không retry).
- Timeout + console có TypeError/500 → **APP/FE BUG** (STOP, log, escalate FE).
- Toast khóa / 401 → **ACCOUNT ISSUE** (theo rule account lock).
- curl pre-flight ≠ 200 → **ENV DOWN** (STOP, escalate infra).
- `about:blank` / "browser closed" → **REAL CRASH** (restart MCP).

**Bước 3 — Escalate kèm phân loại rõ ràng.**

**Cấm:** retry mù khi chưa phân loại · mark BLOCKED ngay lần timeout đầu · bỏ qua capture diagnostic.

---

## 4. Cấu trúc bug entry — 6 section cố định (rule 3.1)

- Đọc `output/template/bug-report-template.md` **trước** khi viết.
- Bug entry chỉ gồm **6 section**:
  1. Mô tả
  2. Bước tái hiện
  3. KQ mong đợi
  4. KQ thực tế
  5. Bằng chứng
  6. So sánh (optional — permission)
- **Cấm** thêm: Tác động / Đề xuất fix / SRS verification / Phân biệt module.

---

## 5. 3-Step Verify TRƯỚC khi log bug (rule 3.3)

1. **Check đúng SRS version.** Mặc định v3.5 (`input/srs-update-2026-5-5/`). Module chưa cover → đọc CHANGELOG xem deprecate → fallback v3 + ghi rõ. *Quote sai version = bug invalid.*
2. **Quote nguyên văn SRS theo số dòng.** Mở file thật, format `srs-update-2026-5-5/srs-fr-NN-X.md:LINE` + nội dung. **Không** nhớ số dòng.
3. **Verify lại bằng method khác.** UI fail → curl API direct. API fail → reload UI fresh. Mâu thuẫn UI vs API → ghi cả 2 + đề xuất BA confirm.

> Wording rule: **describe** yêu cầu nghiệp vụ, KHÔNG **prescribe** implementation (không bắt đúng button/endpoint/mã lỗi cụ thể).

---

## 6. Re-test & đóng bug

**6.1 — Overwrite 1 dòng Re-test latest (KHÔNG append history):**
- Mỗi bug chỉ giữ **DUY NHẤT 1 dòng** blockquote Re-test ngay sau heading. Retest mới → **OVERWRITE** dòng cũ.
- Cấm: append `Re-verify #6/#7...` · append blockquote list theo round · để header `Ngày` lệch với timestamp body.
- Section `## Tổng hợp` đầu file = snapshot LATEST (≤5 dòng), không dồn round-narrative.

Format đúng:
```markdown
## ~~BUG-XXX-NNN~~ [CLOSED] — {tiêu đề}

> **Re-test:** YYYY-MM-DD HH:MM:SS R{N} — ✅ PASS (Closed-verified). {1-2 câu why fixed}.
```

**6.2 — Workflow sau khi đóng bug:**
1. Update Bug Summary Table: Status `Open → Closed`.
2. Mở `tasks/todo.md` tìm task gốc → tăng count dòng `**Bug:** X/Y đóng`.
3. Tester verify Kết quả → quyết flip icon (⚠️→✅ nếu PASS clean; giữ ⚠️ nếu còn Open Major / Sai spec).

**6.3 — Rename `Pass-` khi 100% bug Closed:**
- Điều kiện: Bug Summary Table không còn row `Open`/`Reopen` **VÀ** task todo đã flip ✅ PASS clean.
- Action: `git mv bug-report-<slug>.md → Pass-bug-report-<slug>.md` + **update tất cả inbound link** (todo.md, workflow/functional/seed reports, master-index).
- **Cấm:** rename mà quên update link (→ 404 cascade) · rename khi còn risk re-open · sửa nội dung MD khi rename.

---

*Nguồn: `CLAUDE.md` — đọc bản gốc để xem đầy đủ ngữ cảnh + hook enforce tương ứng.*
