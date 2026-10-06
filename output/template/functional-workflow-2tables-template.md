# Template — 2 bảng tổng hợp BẮT BUỘC cho Functional/Workflow report

> Trích chi tiết từ CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp". **Policy tóm tắt (vị trí đặt + Cấm + 6 nhóm A-F) vẫn ở CLAUDE.md**; file này giữ markdown mẫu đầy đủ + column rules + ví dụ để copy.

**Áp dụng cho mọi tester (hiện tại + tương lai) làm việc trong folder `output/qa-reports/`.** Mọi file `functional-test-report-*.md` và `workflow-test-report-*.md` BẮT BUỘC chứa 2 bảng dưới — đặt **ngay sau Verdict + Accounts** (LATEST round), TRƯỚC narrative deep-dive Phase 1/2/3.

## Bảng 1 — Trạng thái toàn bộ TC (snapshot LATEST)

Aggregate **toàn bộ TC** trong test plan của module × cột Status mới nhất × Note 1-line. Update sau MỖI round (R{N} mới nhất ghi vào ô cuối). Không xóa TC cũ — TC thay đổi status flip icon + ghi round phát hiện.

```markdown
## Bảng trạng thái TC (snapshot R{N} — LATEST YYYY-MM-DD HH:MM:SS)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TV-001 | Tạo VV | ✅ PASS | R8 | OK clean |
| TV-022 | Auto-save 30s | ❌ FAIL | R16-P2 | Endpoint /trao-doi missing — BUG-BE-R16-003 |
| TV-053 | NHT phân công CG | 🚫 BLOCKED | R16-P2 | Cascade R7.3.14 NHT TVV seed |
| ... | ... | ... | ... | ... |
| **Tổng** | **N TC** | ✅X · ⚠️Y · ❌Z · 🚫W · ⏭V · 🤷U | | |
```

**Status icon convention** (terminology Việt):
- ✅ Đạt (PASS clean)
- ⚠️ Sai spec (PASS but deviates SRS, log Minor)
- ❌ Lỗi (FAIL — bug confirmed)
- 🚫 Không test được (BLOCKED — thiếu data/permission/env)
- ⏭ Hoãn (SKIP — out-of-scope round này, defer)
- 🤷 Không xác định (cần re-test, ambiguous evidence) — CẤM kết luận, phải retry method

## Bảng 2 — TC chưa chạy được + cần làm gì để chạy

Aggregate CHỈ TC non-PASS (⚠️/❌/🚫/⏭/🤷). Format **đơn giản, ngôn ngữ tự nhiên, ngắn gọn**. Mục đích: tester/dev/BA nhìn 1 cái biết ngay TC nào kẹt vì gì, cần làm gì để chạy được, ai làm.

```markdown
## Bảng TC chưa chạy được — cần làm gì để chạy (R{N})

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TV-022 | Endpoint auto-save 30s chưa có (BUG-BE-R16-003) | BE expose endpoint `/trao-doi-nhap` theo SRS §1496 | Dev BE |
| TV-053 | NHT chưa có TVV record để phân công | Seed R7.3.14 — walk workflow tạo NHT có TVV | QA seed |
| TV-040 | TVV stats counter không có trong spec | BA confirm có yêu cầu không | BA |
```

**Cột "Vì sao chưa chạy được"** — 1 câu ≤20 từ, ngôn ngữ tự nhiên (không ERR code, không endpoint path đầy đủ — đẩy chi tiết vào bug-report).

**Cột "Cần làm gì để chạy"** — action cụ thể, ≤25 từ. Không "Defer" / "TBD" — phải nói rõ task nào / ai cần làm trước.

**Cột "Ai làm"** — chọn 1: `Dev BE` / `Dev FE` / `QA seed` / `QA API` / `BA` / `Infra`.

**Trước Bảng 2 BẮT BUỘC có 1 dòng tóm tắt** "Hiện tại còn N TC chưa chạy được — chia M nhóm: X chờ dev fix · Y chờ seed · Z out-of-scope...". Mục đích: user/QA mới đọc 1 dòng biết tổng thể.

**Cấm:**
- Đặt 2 bảng ở cuối file — phải ngay sau Verdict.
- Để Bảng 2 trống mà Bảng 1 có TC non-PASS — phải đối chiếu 1:1.
- Cột "Vì sao" / "Cần làm gì" >25 từ — đẩy chi tiết ra bug-report.
- Quên update sau round — round mới overwrite TC vừa retest.
- Dùng English jargon (BLOCKED/PENDING/DEFERRED) trong cột mô tả.

**Lý do bảng này quan trọng:** user / QA handoff cross-tester / dev / BA cần đọc 1 lần biết ngay "TC nào chạy được, TC nào kẹt vì gì, ai cần unblock". Không có bảng này → tester sau phải đọc full narrative Phase 1/2/3 nhiều round → tốn thời gian + miss status.

## Phân loại 6 nhóm nguyên nhân cho cột "Vì sao chưa chạy được" — BẮT BUỘC (enforced 2026-05-10 22:30:00)

Cột "Vì sao chưa chạy được" trong Bảng 2 KHÔNG được tự nghĩ ra label — phải pick **1 trong 6 nhóm chuẩn** A-F:

| Nhóm | Tên | Trigger phân loại |
|:-:|---|---|
| **A** | Thiếu seed data | DB chưa có record / variant / state cần — tester không thấy bug logic, chỉ thiếu data tiền điều kiện |
| **B** | Chờ dev fix bug | Đã log BUG-{module}-{ID} với SRS ref, status Open hoặc PARTIAL |
| **C** | Chờ BA confirm spec | 2 spec mâu thuẫn / SRS ambiguous / dev claim verbal BA |
| **D** | Lỗi env / chờ infra | mTLS sandbox / Cổng PLQG / API key / batch trigger / DB config / mock server |
| **E** | Dependency upstream chưa xong | TC/task khác chưa PASS, theo format `[need: ≥N entity state X]` |
| **F** | Lý do khác | DB-level only (DBA query) / out-of-scope round / cost cao (vd timeout 30 ngày) |

Chi tiết trigger phân loại + phương án chuẩn + workflow re-test + anti-patterns: **[`tc-block-classification-template.md`](tc-block-classification-template.md)** — áp dụng cho **MỌI round QA + MỌI tester** (hiện tại + tương lai).

**Cấm:**
- Tự nghĩ ra nhóm 7+ ngoài A-F.
- Ghi "Defer" / "TBD" / "Skip" trong cột "Vì sao" mà không pick nhóm A-F.
- Mark nhóm B mà chưa log bug — phải log BUG-{ID} TRƯỚC, mark nhóm B SAU.
- Mark "🤷 Không xác định" mà không retry method (reload fresh, curl, isolatedContext) trước (xem memory `feedback_deep_review_before_ba_defer`).
- Defer >2 round nhóm F mà không escalate user lead.
- Cột "Ai làm" ghi "QA team" / "Dev team" — phải role cụ thể: `Dev BE` / `Dev FE` / `QA seed` / `QA API` / `BA` / `Infra` / `DBA`.
