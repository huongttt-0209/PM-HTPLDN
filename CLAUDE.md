# CLAUDE.md — QA Project: PM HTPLDN

Project này chứa tài liệu QA cho Phần mềm Hỗ trợ Pháp lý Doanh nghiệp (PM HTPLDN).

## 🔴 Skill routing preference — BẮT BUỘC hỏi trước

**Không tự động dùng skill chỉ vì yêu cầu của user khớp mô tả skill.**

- Chỉ dùng skill khi user gọi rõ bằng tên skill, slash command, hoặc yêu cầu trực tiếp "dùng skill X".
- Nếu agent nhận thấy một skill có thể cho kết quả tốt hơn, phải hỏi user xác nhận trước khi áp dụng.
- Nếu user không xác nhận hoặc không nhắc skill, xử lý thủ công theo context repo và các file liên quan.
- Quy tắc này áp dụng cho mọi session làm việc trong repo này.

## 🔴 Tool routing — BẮT BUỘC (enforced từ 2026-05-05)

**Mọi QA test / browse / smoke / functional / workflow / regression trên project này PHẢI dùng Chrome DevTools MCP làm tool MẶC ĐỊNH.**

| Trigger từ user | Tool dùng | Cấm dùng |
|---|---|---|
| `/qa`, `/qa-only`, `/gstack-qa-only`, `/gstack-qa`, `/browse`, `/investigate` | **Chrome DevTools MCP** (`mcp__chrome-devtools__*`) | gstack `$B` / browse-server / Playwright direct |
| "test [module/page]", "QA [feature]", "kiểm thử...", "chạy smoke...", "verify..." | **Chrome DevTools MCP** | gstack `$B` |
| Auth flow (login + OTP) | MCP-Template login (xem section "Chrome DevTools MCP — PATTERNS BẮT BUỘC" §Template login) | gstack atomic chain |

**Lý do:** Smoke test 2026-04-21 chứng minh MCP 3/3 PASS, gstack crash rate 50%→20% chỉ sau 3 fix R3.1. MCP có `list_network_requests` + `list_console_messages` native, gstack không có. 1 lần login/session vs gstack re-login mỗi bash do `$PPID` reset.

**Khi nào fallback gstack `$B`:**
1. MCP server crash thật + restart không recover (hiếm).
2. User explicit yêu cầu `--use-gstack` hoặc "dùng gstack" / "dùng `$B`".
3. CSS-selector-exact-match cần Playwright low-level (vd verify class custom). Vẫn ưu tiên `evaluate_script` của MCP trước.

**Khi skill template (vd `/gstack-qa-only`) yêu cầu `$B`:** ADAPT — giữ workflow Phase 1-6, thay command theo bảng map ở section "MCP-Rule 6: Phân loại lỗi" trong file này. Output report theo template project ([output/template/](output/template/)), KHÔNG dùng `.gstack/qa-reports/`.

**Khi nào hỏi user trước khi chạy:**
- Skill workflow generic conflict với task cụ thể trong [tasks/todo.md](tasks/todo.md) → confirm scope task ID.
- User chưa nói rõ module/account → hỏi 1 lần rồi chạy.

## Quick reference

- **App URL:** http://103.172.236.130:3000/
- **MailHog (OTP inbox):** http://103.172.236.130:8025
- **Test strategy:** [output/test-strategy.md](output/test-strategy.md)
- **Permission matrix:** [output/permission-matrix.md](output/permission-matrix.md) (49 entity × 11 role)
- **Test accounts:** [input/users.csv](input/users.csv) · **Permission test usage guide:** [input/test-accounts-isolation.csv](input/test-accounts-isolation.csv)
- **🔴 SRS — nguồn do PROMPT chỉ định thắng.** Prompt session không nói nguồn → mặc định [Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/](Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/) (bản chốt 2026-07-25) cho mọi verify / log bug / quote số dòng.
  - Bản cũ [input/srs-update-2026-5-5/](input/srs-update-2026-5-5/) là bản BA trích khi viết phiếu UAT — **CHỈ tham chiếu**, KHÔNG quote số dòng. Hai bản lệch ~+5..+14 dòng và lệch cả NỘI DUNG ở vài chỗ (vd mục "Tải file Excel mô tả kèm" đã gỡ khỏi SCR-VII-03; `ERR-DG-BC-01` → `ERR-DG-TR-01`). Quote nhầm bản → bug invalid.
  - [v3 legacy](input/srs-v3/) · [CHANGELOG v3→v3.5](input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md)
- **Báo cáo QA:** [output/qa-reports/](output/qa-reports/)
- **🔴 QA SOP (8 quy trình chính):** [output/qa-sop.md](output/qa-sop.md) — đọc TRƯỚC khi bắt đầu round mới
- **State machines v3.5 ref card:** [input/data/state-machines-v3.5.md](input/data/state-machines-v3.5.md) — bảng tra cứu state machine 14 module
- **SRS contradictions tracker:** [tasks/srs-contradictions.md](tasks/srs-contradictions.md) — mâu thuẫn spec cần BA chốt

### Seed data references (new 2026-04-23)
- **Flow + hub tier + troubleshooting:** [input/flow-module.md](input/flow-module.md) — state machine 14 module + Hub Tier + Seed Presets (Phụ lục 2) + Troubleshooting (Phụ lục 3)
- **Cross-module map:** [input/data/entity-map.md](input/data/entity-map.md) — 18 entity × "Tạo tại / Đọc tại" ma trận
- **Seed fixture (giá trị nhập):** [input/data/seed-fixture.yaml](input/data/seed-fixture.yaml) — 6 variants/entity theo tier Y
- **Công thức seed:** YAML cho giá trị + flow-module.md cho state machine + account switch. Không cần file riêng cho step-by-step.

## Quy tắc seed task — BẮT BUỘC tránh gãy như A5 (2026-04-29)

**Mỗi seed task entity có ≥2 chiều combinatorial (entity × state × loại × LV × cấp):**

1. **Acceptance theo filter, KHÔNG theo số lượng tổng.**
   - ❌ Sai: "Seed 12 variant"
   - ✅ Đúng: "Seed ≥3 record cho mỗi filter downstream (loại × state × LV)"

2. **Verify per-filter trước khi đóng task.**
   - ❌ Sai: `total = 12 → ✅ pass`
   - ✅ Đúng: `?loaiTvv=CG → ≥1, ?loaiTvv=NHT → ≥1, ?loaiTvv=TVV → ≥1 → ✅ pass`

3. **Mở `entity-map.md` cột "Đọc tại" trước khi viết acceptance.** List downstream → quote SRS filter → fill section "Downstream consumer × filter" trong [seed-checklist-template.md](output/template/seed-checklist-template.md).

4. **Nếu thiếu filter → split sub-task ngay** (vd T1.B3b/B3c). Không dồn vào task gốc.

**Pattern đã gãy:** A5 R5/R6/R7 vì T1.B3 acceptance "12 variant TVV" gộp loại → 0 CG / 12 TVV → block 4 round.

**Reference đầy đủ:** [`tasks/lessons-learned.md`](tasks/lessons-learned.md) entry "2026-04-28 → 2026-04-29 — A5 TVCS FAIL".

## State marker workflow — auto re-eval downstream task (enforced 2026-05-07)

**Vấn đề cũ:** Dep `[need: R7.4.D3 ⚠️ ≥1 record]` gate downstream theo task icon thay vì state thực. Task ⚠️ partial → downstream ⏳ false-block dù data đủ. Task ✅ → downstream 🟢 dù data đã reset.

**Format dep `[need: ...]` chuẩn:**
```
[need: <state predicate> (✓ N) | (✗ N|reason); <optional spec/account note>]
```
- `(✓ N)` = state thoả, count thực = N
- `(✗ N|reason)` = state KHÔNG thoả
- KHÔNG nhắc icon task upstream trong bracket — task icon đổi liên tục, marker phản ánh state thực

**Single source state count:** [tasks/state-snapshot.md](tasks/state-snapshot.md) — entity × state distribution + verify command (MCP/curl).

**Workflow sau MỌI task ✅ thay đổi state entity X (BẮT BUỘC, không hỏi user):**

1. Re-run verify command (MCP `list_network_requests` / curl) cho entity X.
2. Update [tasks/state-snapshot.md](tasks/state-snapshot.md) count + timestamp.
3. Grep todo.md `[need: ... <X> ...]` → list task có dep entity X.
4. Đổi marker từng task: `(✗ N)` ↔ `(✓ N)` theo state mới.
5. Edit todo.md → hook `auto-rescan-todo.py` tự flip ⏳→🟢 nếu mọi marker `(✓ ...)`. (Hook contract: xem bảng §Hook contracts phía dưới.)

**Workflow sau khi đóng bug ở bug-report-*.md (BẮT BUỘC, từ 2026-05-08; bổ sung step 6 từ 2026-05-10):**

1. Update Bug Summary Table trong file bug-report: Status `Open → Closed` + thêm dòng `> **Re-test:** YYYY-MM-DD R{N} — ✅ PASS ...` sau heading bug.
2. Mở [tasks/todo.md](tasks/todo.md) tìm task gốc tham chiếu bug-report đó.
3. Cập nhật dòng `**Bug:**` trong todo: tăng số đóng (`X/Y → (X+1)/Y`).
4. Save todo.md → hook `check-todo-stale-bug-closure.py` warn nếu icon ⚠️/🚫 + bug đã N/N đóng.
5. Tester verify Kết quả task (PASS/FAIL/Sai spec) → quyết flip icon:
   - ⚠️ → ✅: Kết quả PASS clean (chỉ còn Minor defer OK).
   - ⚠️ giữ nguyên: còn Open Major / Sai spec component khác / cần re-test.
   - 🚫 → ⏳/🟢: nếu block chính đã giải, dep upstream ready.
6. **Rename `bug-report-<slug>.md` → `Pass-bug-report-<slug>.md` khi MỌI bug trong file đã Closed.** Quy tắc đầy đủ (trigger + 2 bước action + anti-pattern) ở §"Bug-report folder discipline" §1 phía dưới — KHÔNG lặp lại ở đây để tránh drift.

**Hook contracts (todo + bug status)** — cả 4 hook đều PostToolUse Edit/Write/MultiEdit; KHÔNG tự flip icon task (tester quyết):

| Hook | Trigger / INPUT | OUTPUT | KHÔNG tự làm / BLOCK |
|---|---|---|---|
| `auto-rescan-todo.py` | todo.md sau Edit | flip ⏳→🟢 task dep thoả; recount bảng Tiến độ | flip 🟢→✅/⚠️/🚫. BLOCK khi bracket có `(✗`, icon ⚠️/🚫/⏳, keyword phi-task ("BA confirm"/"endpoint deploy"/"VNeID Tier"/"spec contradiction") |
| `check-todo-stale-bug-closure.py` | todo.md | stderr warn task ⚠️/🚫 có `**Bug:** X/X đóng` (all closed) — gợi ý flip | auto-flip (Minor defer = ✅ subjective). Skip khi total=0, X<Y, không có dòng Bug |
| `auto-rename-pass-prefix.py` | `**/bug-reports/**/bug-report-*.md` (skip nếu đã `Pass-`) | stderr remind rename `Pass-<orig>.md` + grep reference link. Detect: Bug Summary mọi row Closed, không Open/Reopen | auto-rename (phá link cross-file → tester dùng MultiEdit batch) |
| `auto-sync-todo-bug-status.py` | `tasks/todo*.md` hoặc `**/bug-report*.md` | tự sửa drift `todo-*.md`: link cũ→`Pass-` khi file cũ mất + file Pass tồn tại; `**Bug:** X/Y đóng` khi đúng 1 link + count chắc; mirror `tasks/tmp/todo-*.md` | sửa dòng nhiều link/subset count (chỉ warn ambiguous). Manual: `... --check` / `--write` |

**Ví dụ:**
```
OLD: [need: R7.4.D3 ⚠️ ≥1 record DA_DUYET]
NEW: [need: ≥1 Kho QA DA_DUYET mỗi LV (✗ 5/6 — thiếu KDTM + Hành chính)]
```

Chi tiết workflow + anti-pattern: memory `feedback_todo_update_after_run` §E.

---

## Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC sau mỗi round (enforced 2026-05-10)

**Áp dụng mọi tester trong `output/qa-reports/`.** Mọi `functional-test-report-*.md` + `workflow-test-report-*.md` BẮT BUỘC có 2 bảng, đặt **ngay sau Verdict + Accounts (LATEST round), TRƯỚC narrative Phase 1/2/3**:

- **Bảng 1 — Trạng thái toàn bộ TC** (snapshot LATEST): mọi TC × Status × Round phát hiện × Note ≤15 từ + dòng Tổng. Không xóa TC cũ, flip icon khi đổi status.
- **Bảng 2 — TC chưa chạy được**: chỉ TC non-PASS × "Vì sao" (≤20 từ) × "Cần làm gì" (≤25 từ) × "Ai làm". Trước bảng có 1 dòng tóm tắt tổng thể ("còn N TC kẹt — X chờ dev · Y chờ seed...").

**Status icon:** ✅ Đạt · ⚠️ Sai spec (log Minor) · ❌ Lỗi (bug) · 🚫 Không test được · ⏭ Hoãn · 🤷 Không xác định (CẤM kết luận, phải retry method).

**Cột "Vì sao" pick 1 trong 6 nhóm chuẩn A-F:** A thiếu seed · B chờ dev fix bug (đã log BUG-{ID}) · C chờ BA confirm spec · D lỗi env/infra · E dep upstream (`[need: ≥N entity state X]`) · F khác (DB-level/out-of-scope/cost cao). **Cột "Ai làm"** role cụ thể: `Dev BE`/`Dev FE`/`QA seed`/`QA API`/`BA`/`Infra`/`DBA`.

> **Markdown mẫu 2 bảng đầy đủ + column rules + ví dụ: [output/template/functional-workflow-2tables-template.md](output/template/functional-workflow-2tables-template.md).** Chi tiết trigger 6 nhóm + phương án + re-test workflow: [output/template/tc-block-classification-template.md](output/template/tc-block-classification-template.md).

**Cấm:** 2 bảng ở cuối file (phải ngay sau Verdict) · Bảng 2 trống khi Bảng 1 có non-PASS · cột mô tả >25 từ (đẩy ra bug-report) · quên update sau round · English jargon (BLOCKED/PENDING/DEFERRED) trong cột mô tả · tự nghĩ nhóm ngoài A-F · "Defer/TBD/Skip" không pick nhóm · mark nhóm B chưa log bug · "Ai làm" ghi "QA team"/"Dev team".

---

## Quy tắc viết todo.md (enforced bằng hook `.claude/hooks/check-todo-concise.py`)

**Template cứng cho mỗi task:**

```
- <icon> **<ID>** <Tên task ngắn>
  - **Kết quả:** <PASS N/N | FAIL | ⚠️ N/M | 🚫 block do X> — <≤15 từ>. [report-link]
  - **Bug:** [bug-report-link] — <closed>/<total> đóng     ← chỉ khi có bug
  - **Cần có sẵn:** <ref task ✅/❌>                        ← chỉ khi task ⏳/🚫
  - **Output:** [report-link]                                ← optional
```

**Hook chặn:** dòng `**Kết quả:**` >25 từ → block Edit/Write. Hook trigger trên mọi file kết thúc `/todo.md`.

**Cấm trong todo.md** (chuyển sang bug-report / workflow-report):
- Pool count, endpoint path, enum value, network response, dev claim, thao tác đối chiếu nguồn
- Multi-round narrative ("R6 sau dev claim fix...", "identical R3 28/4...")
- Cascade impact reasoning (đặt ở section "Module bị block")

**DO (≤15 từ, đúng template):**
```
- ✅ **A1** Workflow TVV — luồng nhập tay
  - **Kết quả:** PASS 12/12 bước. R6 advance thêm 9 record. [workflow-test-report-TVV.md]
  - **Bug:** [bug-report-flow-TVV.md] — 3/4 đóng
```

**DON'T (35+ từ, nhồi chi tiết):**
```
- **Kết quả R7 29/4 09:36:** FAIL — modal Phân công CG TVCS-0001 dropdown Trống.
  Pool thực có 8 CG DANG_HOAT_DONG cover 6 LV; Doanh nghiệp có 2 CG khớp
  (TVV-0019 + TVV-0021). FE truyền trangThai=HOAT_DONG cho endpoint TU_VAN_VIEN
  → mismatch enum, BE trả 0. Đã đối chiếu SRS + ERD khớp.
```

**Note nhật ký** (`> Note 2026-04-29 ...`) tách riêng đầu file, không phải dòng Kết quả — vẫn được phép dài để daily handoff.

---

## Khi viết test plan mới cho module

- Theo quy trình [output/scaling-test-strategy.md §4.1 Bước 3](output/scaling-test-strategy.md): grep BR từ SRS Phụ lục B + sibling-check ≥2 module + BA sign-off trước Bước 4
- Copy template: [output/template/test-plan-overview-template.md](output/template/test-plan-overview-template.md)
- BR có "Áp dụng: Toàn bộ..." trong SRS = default áp dụng. Ngoại lệ phải QUOTE line SRS, không tự suy luận.

## Khi log bug — BẮT BUỘC

1. **Read [output/template/bug-report-template.md](output/template/bug-report-template.md) trước khi Write/Edit bug entry.** Bug entry chỉ có 6 sections: Mô tả / Bước tái hiện / KQ mong đợi / KQ thực tế / Bằng chứng / So sánh (optional permission). KHÔNG thêm Tác động / Đề xuất fix / SRS verification / Phân biệt module.
   - **Ngoại lệ duy nhất — mục thứ 7 `Cách verify sau khi fix`:** BẮT BUỘC và CHỈ dùng cho bug **Reopen** (bug chuyển lại dev sau vòng re-verify). Bug Pass / không phải lỗi / chờ BA → không có mục này. Đây là quy trình re-test (Precondition · các bước · ✅ PASS khi · ❌ FAIL nếu · ⚠️ bẫy), không phải phần phân tích như 4 mục bị cấm ở trên. Ghi giống hệt từng chữ với ô note trên bảng theo dõi.
2. **Nguồn chuẩn = ĐÚNG file/thư mục SRS mà prompt của session chỉ định — không mặc định nguồn nào khác.**
   Mọi lần log / đóng / đổi severity đều phải **mở chính file đó** và quote số dòng **thực đọc được**, không
   quote từ trí nhớ. Thư trả lời BA, ô phản hồi DEV/TKM trên bảng, ảnh đối tác, báo cáo đợt cũ, và SRS ở
   đường dẫn khác **chỉ là ngữ cảnh / manh mối để biết tra chỗ nào** — cấm dùng làm căn cứ verdict, cấm suy
   ra yêu cầu ngoài những gì SRS prompt cấp ghi rõ. Prompt không chỉ định nguồn → hỏi user, đừng tự chọn.
   **Riêng FLOW 04:** SRS prompt cấp khác expected đối tác → bắt buộc BA confirm, kể cả dev đang đúng SRS;
   không được tự Pass/Không phải lỗi.
3. **Workaround = bug candidate.** Gặp 4xx/5xx → log, không skip vì "tự fix được". **Riêng FLOW 04:** chỉ
   áp dụng khi 4xx/5xx tự lộ trong bước bắt buộc của vế đang verify; nếu nó chỉ xuất hiện sau khi đổi màn,
   role, filter, seed hoặc field ngoài bug thì ghi candidate, cấm mở rộng case để điều tra.

### 3-Step Verify TRƯỚC khi log bug (enforced 2026-05-13 — chi tiết: [output/qa-sop.md §4.4](output/qa-sop.md))

Sau khi deep-verify R20 phát hiện 5/9 bug Open có vấn đề (3 false bug + 2 wrong wording quote sai mã/state), enforce 3 step:

1. **Kiểm tra SRS version.** **Prompt của session chỉ định nguồn nào thì dùng đúng nguồn đó.** Prompt không nói → fallback `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (xem Quick reference). **CẤM mở `input/srs-update-2026-5-5/` để lấy số dòng.** Nếu module chưa cover trong v3.5 → đọc [CHANGELOG-v3-to-v3.5.md](input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) xem có deprecate → fallback v3 + ghi rõ trong bug entry. **Quote sai bản = bug invalid.** Riêng **FLOW 04** không tự fallback: dùng đúng SRS prompt cấp; thiếu coverage thì ghi SRS im lặng và xử theo flow.
2. **Quote nguyên văn SRS line số.** Mở file SRS, tìm line cụ thể, format `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-NN-X.md:LINE` + nội dung. KHÔNG dùng số dòng từ trí nhớ — luôn mở file verify. **Số dòng ghi trong phiếu UAT / thư trả lời BA là của bản `input/` (lệch ~+5..+14) — phải tự mở bản chốt xác minh lại, không bê nguyên.**
3. **Verify lại bằng method khác.** UI fail → curl API direct cùng action so sánh. API fail → reload UI fresh re-test. Mâu thuẫn UI vs API → ghi cả 2 trong bug entry, đề xuất BA confirm.

### Wording rule — describe requirement, NOT prescribe implementation

- ❌ Sai (prescribe): "Phải hiện button **Đồng ý/Hủy**", "Phải gọi `POST /api/v1/X` trả 200", "Phải có mã `ERR-PC-06`"
- ✅ Đúng (describe): "Theo SRS line N, khi role X bấm duyệt không hợp lệ, hệ thống phải hiển thị thông báo từ chối + giữ state cũ"

**Lý do:** Dev có nhiều cách implement. Bug describe yêu cầu nghiệp vụ, dev tự chọn implementation. Prescribe → talk past 8+ round (BUG-PC-INACTIVE pattern).

### Pre-log: tra SRS contradictions tracker

Trước log bug, search [tasks/srs-contradictions.md](tasks/srs-contradictions.md). Nếu module/topic đã có entry Open → không log như spec normal, ghi note "depends on SRS-C-NNN BA decision" trong bug entry. **Riêng FLOW 04:** tracker chỉ dùng chống trùng sau khi đã đối chiếu đúng SRS prompt cấp; tracker không được đổi relation `MATCH/DIFF/GAP` hoặc verdict.

## Re-test discipline — OVERWRITE 1 dòng latest, KHÔNG append history (enforced 2026-05-12)

**Áp dụng cho mọi QA / tester làm việc trong folder `output/qa-reports/`.** Mỗi bug trong file `bug-report-*.md` chỉ giữ **DUY NHẤT 1 dòng** blockquote Re-test latest ngay sau heading bug. Mỗi lần retest mới → **OVERWRITE** dòng cũ, KHÔNG append blockquote list / Re-verify #N tích lũy.

**Vì sao:**
- Field `**Ngày**` ở header phải sync với timestamp dòng Re-test mới — nếu append history, Ngày stale dần (vd HDTV file: header `2026-05-12 02:50:00` vs body latest `2026-05-12 15:55:00` lệch 13h).
- Multi-line history `Re-verify #6 / #7 / #8` tích lũy hàng trăm dòng/file sau 8-19 round → dev đọc noise + dễ stale.
- Lịch sử retest cũ đã có ở Bug Summary Table cột Status — KHÔNG cần lặp ở blockquote.

**Format đúng (chỉ 1 dòng):**
```markdown
## ~~BUG-XXX-NNN~~ [CLOSED] — {tiêu đề}

> **Re-test:** 2026-05-12 15:55:00 R19 — ✅ PASS (Closed-verified). {1-2 câu why fixed}.
```

**KHÔNG được:**
- ❌ Append blockquote list: `> - 2026-04-28 R3 ...` + `> - 2026-04-29 R4 ...`
- ❌ Append `> **Re-verify #6` + `> **Re-verify #7` + `> **Re-verify #8` cho cùng bug
- ❌ Để field `**Ngày**` ở header lệch với max timestamp trong body
- ❌ **Section `## Tổng hợp` đầu file dồn round-narrative blockquote** `> **R{N} retest ...` / `> **R{N} run ...` — section này SNAPSHOT LATEST, OVERWRITE 1 đoạn ngắn (≤5 dòng) tóm tắt round mới nhất + breakdown Open/Closed. Round history cũ đã có ở cột Status Bug Summary Table + Re-test bug-level → KHÔNG lặp. Hook `check-retest-no-duplicate.py` BLOCK khi edit introduce >2 round-narrative blockquote mới trong section Tổng hợp; legacy file >2 → stderr INFO warn migration manual (collapse về 1 snapshot LATEST).

**Tooling (committed, portable cho mọi QA clone repo):**

| Tool | Vai trò | Lệnh |
|---|---|---|
| `.claude/scripts/collapse-retest-history.py` | Migration 1 lần — collapse retest history cũ, giữ latest theo max timestamp | `python3 .claude/scripts/collapse-retest-history.py --dry-run <file>` → review → `--write` (tạo `.bak` backup) |
| `.claude/hooks/check-retest-no-duplicate.py` | PreToolUse — block edit introduce >1 retest block/bug | Auto-trigger Edit/Write/MultiEdit |
| `.claude/hooks/auto-bump-bug-report-date.py` | PostToolUse — auto-bump header.Ngày = max body timestamp | Auto-trigger Edit/Write/MultiEdit |

**Evidence ảnh từ retest cũ:** Hook + script KHÔNG tự append ảnh vào latest line (ảnh thuộc state cũ, append sai context). Migration script in stderr list ảnh ref bị mất → tester quyết migrate manual nếu cần.

## Bug-report folder discipline — Pass- prefix + image co-locate (enforced 2026-05-10)

**Layout chuẩn `output/qa-reports/round{N}-*/bug-reports/`:**
```
bug-reports/
└── <module>/                          ← chỉ chứa *.md + image/ subfolder
    ├── bug-report-<X>.md              ← file còn ≥1 bug Open
    ├── Pass-bug-report-<Y>.md         ← file 100% bug Closed (tester rename manual khi hook warn)
    └── image/
        └── *.png / *.jpg / *.jpeg / *.b64.txt
```

**3 rule cứng (mỗi khi update file bug-report):**

1. **Pass- prefix khi 100% bug Closed** (home đầy đủ của quy tắc — §State marker workflow step 6 chỉ trỏ về đây).
   - **Trigger:** Bug Summary Table KHÔNG còn row Status `Open`/`Reopen` (tất cả `Closed` / strikethrough `~~`) **VÀ** task gốc todo.md đã flip ✅ Kết quả PASS clean.
   - **Action — 2 bước, KHÔNG skip bước 2:**
     1. `git mv .../bug-report-<slug>.md .../Pass-bug-report-<slug>.md` (giữ git history). Chưa track: rename filesystem rồi `git add` mới + `git rm` cũ.
     2. **Update MỌI reference link** `bug-report-<slug>.md` → `Pass-bug-report-<slug>.md` (dùng MultiEdit batch). Grep: `tasks/todo.md` + `tasks/todo-<module>.md` dòng `**Bug:**`; `output/qa-reports/round{N}/{workflow,functional,seed}/` reports; `README.md` + master-index*.md.
     - **Cấm:** rename mà không update link → 404 cascade cross-file → master-index regen lỗi.
   - **Anti-pattern — KHÔNG rename khi:** file một-bug Closed nhưng task todo còn ⚠️/🚫 (bug khác chưa log); còn risk re-open (FE fix chưa deploy stable, dev claim chưa user verify); Status có `Reopen`.
   - **Hook `auto-rename-pass-prefix.py` là WARN-ONLY** — stderr nhắc rename khi đủ điều kiện, **KHÔNG auto-rename** vì rename phá link cross-file → tester quyết.

2. **Ảnh phải nằm trong `<module>/image/`.** CẤM:
   - Ảnh rời cùng cấp với MD (vd `<module>/screenshot.png`).
   - Subfolder lạ kiểu `<module>/img/`, `<module>/screenshots/`, `<module>/evidence-rN/`, `<module>/evidence-<task>/` — gộp hết về `image/`.
   - Top-level `bug-reports/image/` chứa ảnh mixed nhiều module — phải distribute về owner.
   - **Soft-enforced by hook** [`check-bug-report-image-discipline.py`](.claude/hooks/check-bug-report-image-discipline.py) — warn-only stderr, không block (vì cleanup cần move + ref update).

3. **Khi save screenshot mới qua MCP `take_screenshot({filePath})`:** path BẮT BUỘC = `output/qa-reports/round{N}-*/bug-reports/<module>/image/<filename>`. Không save vào parent module folder, không tạo subfolder mới.

**Workflow khi phát hiện drift (loose images / odd subfolders):**

1. Move loose images: `mv <module>/*.png <module>/image/` (lọc các file rời).
2. Gộp subfolder lạ: `mv <module>/img/* <module>/image/ && rmdir <module>/img` (lặp cho mỗi subfolder lạ).
3. Distribute top-level image/: grep MD ref `grep -rl <fname>` tìm owner module → move vào module đó. File không có ref → suy luận từ tên file prefix (vd `r7-X-Y` → task ID → module).
4. Update MD ref: `](../image/X)` / `](screenshots/X)` / `](evidence-*/X)` / `](img/X)` / bare `](X.png)` → đổi hết thành `](image/X)`.
5. Verify: hook `check-bug-report-image-discipline.py` không còn warn + grep MD không còn broken ref.

**Anti-pattern:**
- ❌ Save screenshot vào root module folder vì "tiện".
- ❌ Tạo `evidence-r{N}/` mỗi round — gộp vào `image/`.
- ❌ Manual rename `bug-report-*` → `Pass-*` mà quên update inbound link → todo.md broken.
- ❌ Đổi nội dung MD khi rename Pass- (vd thêm dòng "## All closed") — chỉ rename, không edit content.

## Chrome DevTools MCP — PATTERNS BẮT BUỘC (primary tool từ 2026-04-21)

**Lý do MCP > gstack:** 0% crash qua smoke (vs 20-50% gstack), 1 lần login/session (vs re-login mỗi bash do `$PPID` reset), native `list_network_requests` + `list_console_messages` inspection.

**Config:** `~/.claude.json` → `mcpServers.chrome-devtools` với `npx -y chrome-devtools-mcp@latest --isolated --viewport 1440x900`. Chrome window hiện (headless=false mặc định). Tool prefix: `mcp__chrome-devtools__*`.

**Expected: 2 tab khi launch (do `--isolated` mode):**
- Tab 1 `about:blank`: launcher tab tự sinh khi Chromium khởi với isolated profile. **Không cần đóng** — không tốn RAM đáng kể, không block tool, không ảnh hưởng correctness.
- Tab 2: tab MCP `new_page()` mở để test thực tế.

**KHÔNG bỏ flag `--isolated`** — flag này bắt buộc cho QA multi-role isolation (xem memory `qa_htpldn_round5_t01`). Bỏ flag = BE httpOnly cookie + localStorage sticky cross-session = role test contaminated = false positive permission. Tab `about:blank` là trade-off cosmetic chấp nhận được.

**Banner "Chrome đang được phần mềm kiểm tra tự động kiểm soát":** notification chuẩn của Chrome khi có CDP client connect. Luôn xuất hiện mỗi MCP session, không phải bug.

### MCP-Rule 1→8 + Template login — tóm tắt

> **Chi tiết đầy đủ + JS mẫu + step list: [docs/htpldn-mcp-patterns.md](docs/htpldn-mcp-patterns.md).** Mở file đó khi cần copy snippet.

- **Rule 1 — `wait_for(text[])` trước mọi `fill`/`click`.** Array text match label/placeholder/heading (robust hơn CSS). App render chậm → timeout ≥10000ms.
- **Rule 2 — `take_snapshot` lấy `uid` FRESH sau mỗi navigate/modal/render.** `uid` chỉ valid tại snapshot đó. a11y tree ẩn element `display:none`/0×0 → dùng `evaluate_script` inspect DOM khi nghi ngờ.
- **Rule 3 — `click` sidebar, KHÔNG `navigate_page` sau login.** Auth ở `localStorage` key `auth-store` + HttpOnly refresh cookie; `navigate_page` = full reload → kick `/login`. Logout đủ: `fetch('/api/v1/auth/logout',{method:'POST',credentials:'include'})` + clear localStorage/sessionStorage rồi navigate `/login`.
- **Rule 4 — Expand sidebar (click "Thu gọn menu") trước submenu lần đầu session.** Sidebar collapsed 64px → submenu render `display:none`.
- **Rule 5 — KHÔNG áp dụng cleanup/retry/atomic-chain/session-reset của gstack.** MCP single process, `sessionStorage` persist cross-call. Crash thật (hiếm) → restart Claude Code, MCP tự reconnect.
- **Rule 6 — Phân loại lỗi (Rule 9) TRƯỚC khi react.** Tool map gstack→MCP: URL=`evaluate_script(()=>location.href)` · screenshot=`take_screenshot` · console=`list_console_messages` · network=`list_network_requests` · DOM=`evaluate_script`.
- **Rule 7 — CSS selector qua `evaluate_script`** (count / click-ẩn / check-class). Selector library ở §Rule 11.
- **Rule 8 — Verify UI ephemeral (toast <5s) qua `MutationObserver`, KHÔNG poll DOM.** Install observer trên `document.body` BEFORE click → capture `addedNodes` 2-5s → filter text/class regex. Poll → false negative "silent fail" (BUG-BM-005 sai 4 round). KHÔNG dùng cho element persistent (table/form/sidebar).
- **Template login** (`qtht_01` / `Secret@123`, OTP `666666`): new_page `/login` → wait_for → snapshot → fill_form → click → wait OTP → type_text → wait dashboard → snapshot → expand sidebar → click submenu. Role CB_TW landing `/403` = PASS; dùng `wait_for(["Quản trị hệ thống"])` làm signal.

---

## Shared rules — áp dụng cả MCP và gstack

### Rule 7 (Account lock fallback) — tóm tắt

> **Step-by-step đầy đủ (capture evidence + fallback procedure + log format): [docs/htpldn-shared-rules-detail.md](docs/htpldn-shared-rules-detail.md) §Rule 7.**

Login fail (toast `Tài khoản tạm khóa` / `Invalid credentials` / HTTP 401 `POST /api/v1/auth/login` / stuck `/login`):
1. **Capture evidence NGAY** — screenshot + console errors + toast DOM (`.ant-message, .ant-notification, [role="alert"], .ant-form-item-explain-error`) + curl `error.code`.
2. **Auto-fallback 1 lượt trong SAME `vai_tro` + `don_vi_ma`** (suffix `_02` → `_03`). **BẮT BUỘC log account thực dùng** trong report.
3. **Constraint cứng:** CHỈ fallback SAME role+cấp. TUYỆT ĐỐI KHÔNG đổi role/cấp (vd TW→ĐP → data scope khác → invalid). BN/DP phải giữ cùng đơn vị.
4. **Hết siblings → STOP, mark BLOCKED, báo user** theo format:

```
🚫 BLOCKED — Toàn bộ account role "<vai trò>" cấp "<cấp>" đều lock
Tried: <primary>, <sibling_1>, ...
Symptom: <toast / HTTP / error code>
Evidence: <screenshot path>
Options: (a) unlock + retry  (b) account khác role/cấp (ảnh hưởng scope)  (c) abort
Bạn chọn (a/b/c)?
```

**Ngoại lệ KHÔNG fallback (STOP ngay):** `admin` (root, không sibling); test yêu cầu đúng username cụ thể (authorization theo user).
**KHÔNG được:** chờ unlock để retry cùng account · retry cùng account ≥3 lần (thêm lock) · fallback qua role/cấp khác mà không hỏi user.

### Rule 9 (Phân loại lỗi diagnostic)

> **Step 1/2/3 + anti-pattern + ví dụ đầy đủ: [docs/htpldn-shared-rules-detail.md](docs/htpldn-shared-rules-detail.md) §Rule 9.** Áp dụng trước Rule 6/7/8 gstack ([docs/legacy/gstack-fallback-rules.md](docs/legacy/gstack-fallback-rules.md)).

Fail (wait timeout / URL lạ / toast lỗi) → **Step 1: capture diagnostic BẮT BUỘC** (screenshot + console + network + DOM) TRƯỚC khi quyết action. **Step 2: phân loại theo bảng. Step 3: escalate kèm phân loại rõ ràng.**

| Dấu hiệu quan sát | Phân loại | Action |
|---|---|---|
| URL `about:blank` giữa 2 bash (gstack, `[browse] Starting server...` lặp) | HARNESS session reset (gstack) | Fix Rule 8. **KHÔNG** cleanup/retry |
| `about:blank` giữa 2 step trong 1 chain / `Target...closed` | REAL CRASH | Cleanup+retry 1 lần (gstack) / restart MCP |
| `wait` timeout + DOM có element class khác | SELECTOR OUTDATED | Update selector, re-run. **KHÔNG** retry selector cũ |
| `wait` timeout + console sạch + network pending >10s | APP/BE BUG | **STOP**, escalate BE. **KHÔNG** retry |
| `wait` timeout + console TypeError/500 toast | APP/FE BUG | **STOP**, log console+screenshot, escalate FE |
| `timed out` sau chain >15 step | CHAIN QUÁ DÀI (gstack) | Split chain, bridge cookies |
| Toast `Tài khoản tạm khóa`/`Invalid credentials` | ACCOUNT ISSUE | STOP theo Rule 7, đổi account |
| curl pre-flight ≠ 200 / auth timeout | ENV DOWN | STOP, escalate infra |

**Anti-pattern:** tăng timeout+retry khi chưa phân loại · mark BLOCKED ngay lần timeout đầu (chưa diagnostic) · cleanup+retry mù khi thấy `about:blank` · bỏ Step 1 capture.

### Rule 11 (Selector library + App-side quirks)

**Selector library — 6 selector hay dùng nhất (bảng đầy đủ 26 selector: [docs/htpldn-selector-library.md](docs/htpldn-selector-library.md)):**

| Mục đích | Selector |
|----------|----------|
| Login / Password input | `input[placeholder="Nhập tên đăng nhập"]` · `input[placeholder="Nhập mật khẩu"]` |
| OTP input (6 ô) | `input[inputmode="numeric"][maxlength="1"]` (KHÔNG dùng `.ant-otp`) |
| Table row | `.ant-table-tbody tr.ant-table-row` |
| Row action Sửa/Xóa | `tr.ant-table-row:has-text("<ma>") a:has-text("Sửa")` ← **`<a>` chứ không phải `<button>`** |
| Drawer form submit | `button:has-text("Đồng ý")` ← **NOT [Lưu] như spec** |
| Toast wrapper (AntD v5) | `.ant-message-notice-wrapper` ← **NOT `.ant-message-notice`** (AntD v5 đổi tên class) |

**App-side quirks cần biết:**
- UI thực tế dùng **Drawer** (right panel) cho form CRUD, KHÔNG phải Modal dialog (spec nói modal)
- Button submit label **[Đồng ý]** thay vì **[Lưu]** theo spec
- Row action **Sửa/Xóa là `<a>` tag** chứ không phải `<button>`
- Trạng thái trong form là **radio button** ("Kích hoạt"/"Vô hiệu hóa") thay vì toggle ("Hoạt động"/"Không hoạt động") theo spec
- Navigation giữa categories: click `li.tab-item` trong `ul.side-tabs`, HOẶC goto URL `/quan-tri/danh-muc/{LOAI_DM}` (goto có thể mất auth nếu cross chain — gstack Rule 8)

> **⚠️ App-side bug — VẪN áp dụng với MCP:** Pattern "4th sidebar click destabilize page" (click `Quản trị hệ thống` → `Danh mục dùng chung` → `Tài khoản & phân quyền` → `Cấu hình hệ thống` thường crash). Workaround: cap 3 navigation/session, reload `/login` làm fresh start nếu cần. Long-term: escalate dev (memory leak / event listener accumulation trong React component sidebar).

---

## Gstack browse (`$B`) — LEGACY / FALLBACK (archived 2026-04-21)

**Status:** Gstack giữ làm fallback khi MCP unavailable hoặc cần CSS-selector-exact-match. **Chi tiết patterns + bảng compat "Rule N" cũ → location:** [docs/legacy/gstack-fallback-rules.md](docs/legacy/gstack-fallback-rules.md) (§Reference compatibility ở cuối file). Rule 7 (Account lock) + Rule 9 (Phân loại lỗi) là SHARED — xem §Shared rules ở trên.

## Known app bugs

| ID | Severity | Title |
|----|----------|-------|
| BUG-UI-01 | Minor | Login trang render 2-3s loading spinner trước khi form hiện |
| BUG-ENV-01 | Minor | Form login persist username/password giữa các lần navigate (dù không check "Ghi nhớ đăng nhập") |

## Quy trình phân loại tab trống / empty state khi QA

Khi thấy tab/màn hình rỗng hoặc placeholder, phân loại TRƯỚC khi log bug hoặc seed data (tránh log sai loại + tránh seed data khi thực chất là bug dev):

| Dấu hiệu quan sát | Phân loại | Xử lý |
|---|---|---|
| Text **"Chức năng đang phát triển"** + image "Trống" / placeholder SVG | **BUG — UI chưa build** (miss feature, vi phạm spec + AC) | Log Critical/Major, screenshot, cite SRS line + AC line. **KHÔNG** seed data — seed xong vẫn rỗng. |
| Text chuẩn: `"Chưa có dữ liệu"`, `"Không tìm thấy..."`, `"Chưa có vụ việc hỗ trợ"`, `.ant-empty` | **Empty state hợp lệ** — thiếu seed data | Seed đúng preset trong [`input/flow-module.md` §Phụ lục 2](input/flow-module.md) + fixture [`input/data/seed-fixture.yaml`](input/data/seed-fixture.yaml) → retest. |
| Table có data nhưng KPI=0, count sai, record mong đợi không hiện | **FE filter bug** hoặc **BE missing join** | MCP `list_network_requests` verify response payload. API trả data=[] → BE bug / wrong scope filter. API trả data nhưng UI không render → FE bug. |
| Text lạ / English leak / `null` / `undefined` / JSON dump | **BUG UI copy hoặc serialization** | Log Minor/Medium, screenshot. |
| Dropdown/list rỗng dù network 200 có bytes | **API double-wrap** (xem memory `qa_htpldn_api_wrap_bug`) | curl verify response shape, check BE envelope wrap 2 lần. |

**Iron rules:**
- KHÔNG log "empty state" thành bug khi chưa seed đủ upstream data theo preset ([Entity Map](input/data/entity-map.md) để trace).
- KHÔNG kết luận BE bug khi chưa check `list_network_requests` response payload.
- "Chức năng đang phát triển" = bug, không phải data gap — log ngay, đừng phí thời gian seed.

## Testing approach

- **Functional tests:** [output/funtion/](output/funtion/) — test cases per module (`7.X-<module>.md`)
- **Smoke specs:** [output/smoke-specs/](output/smoke-specs/) — smoke test 4 bước self-contained (`6.X-smoke-<module>.md`, số khớp funtion/)
- **State Machine specs:** [output/smoke/](output/smoke/) — states + test paths + BR (`6.X-sm-<module>.md`)
- **Template bug/report:** [output/template/](output/template/)
- **QA skills to use:** `/qa-only` (report-only), `/qa` (test + fix), `/browse` (manual exploration)

## Fetch OTP helper

```bash
curl -s "http://103.172.236.130:8025/api/v2/messages?limit=1" | python3 -c "
import sys, json, re
d = json.loads(sys.stdin.read())
msg = d['items'][0]
print('To:', msg['To'][0]['Mailbox'] + '@' + msg['To'][0]['Domain'])
print('OTP:', re.search(r'\b(\d{6})\b', msg['Content']['Body']).group(1))
"
```
