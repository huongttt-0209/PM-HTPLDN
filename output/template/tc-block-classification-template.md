# TC Block Classification — Template (cross-project)

> Dùng trong MỌI round QA của project HTPLDN. QA mới hoặc QA khác dùng folder này áp dụng template này khi tổng hợp TC chưa chạy / đang block.
>
> **Trigger áp dụng:** sau MỖI round (R{N}) chạy functional / workflow / smoke / permission / regression — khi cần báo cáo "TC nào chạy được, TC nào chưa, vì sao, ai unblock". BẮT BUỘC kèm bảng phân loại trong báo cáo + sync với tester / dev / BA / Infra để có owner unblock.

## 1. Mục tiêu

Khi 1 round QA kết thúc, BẮT BUỘC trả lời 3 câu:
1. **TC nào chưa PASS?** (✅ Đạt = OK; phần còn lại cần phân loại)
2. **Vì sao chưa PASS?** (chia 6 nhóm chuẩn dưới đây — không "tự nghĩ ra nhóm mới")
3. **Cần làm gì + ai làm để chạy được?** (action cụ thể + role owner)

Output: 2 bảng — Bảng tổng (44 TC × Status) + Bảng chi tiết non-PASS (× nhóm × phương án × ai). Đặt ngay sau Verdict trong functional/workflow report (xem CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC").

## 2. 6 nhóm nguyên nhân chuẩn

QA chỉ được pick 1 nhóm cho mỗi TC non-PASS. Nếu TC có 2 nguyên nhân, pick **nguyên nhân chặn TRƯỚC** (root blocker), nhóm còn lại note "+ phụ thuộc Y" trong cột "Cần làm gì".

### Nhóm A — **Thiếu seed data**

**Triệu chứng:** Endpoint UI/API phản hồi đúng spec nhưng list/result rỗng vì DB chưa có record cần thiết. Tester KHÔNG thấy bug logic — chỉ thiếu data tiền điều kiện.

**Trigger phân loại:**
- Empty state "Chưa có dữ liệu" + spec yêu cầu N record → cần seed N record
- Dropdown empty + entity-map cho biết upstream module có "Tạo tại" → cần seed upstream
- Permission test fail vì account thiếu role mà role tồn tại trong CSV → cần advance state account

**Phương án xử lý chuẩn:**
- (a) Walk workflow UI tạo record (BẮT BUỘC theo `feedback_test_method_ui_only` — không bulk POST)
- (b) Nếu workflow upstream chưa test → dependency upstream (chuyển sang Nhóm E)
- (c) Nếu seed task tồn tại trong todo nhưng chưa chạy → split ra task seed riêng

**Ai làm:** QA seed (chính) hoặc Dev BE nếu seeder cần fixture.

**KHÔNG dùng nhóm này khi:** test method sai (vd test BN scope mà chỉ có TW data → chuyển nhóm khác hoặc accept negative case).

### Nhóm B — **Chờ dev fix bug**

**Triệu chứng:** TC fail vì BE/FE bug đã được log thành bug-report ID. Bug có SRS reference rõ. Re-test cùng kịch bản sau khi dev fix sẽ pass.

**Trigger phân loại:**
- TC đã probe đầy đủ + có BUG-{module}-{ID} log
- Bug status = Open hoặc PARTIAL trong bug-report
- Không phải data drift account (data drift = nhóm con của B vẫn được, ghi rõ)

**Phương án xử lý chuẩn:**
- (a) Ghi rõ bug ID + severity trong cột "Vì sao"
- (b) Cột "Cần làm gì" nêu fix cụ thể nếu QA biết (vd "wire event handler X"), ngược lại "Dev BE fix BUG-XXX rồi re-test"
- (c) Sau khi dev claim fix → quy trình re-test có capture screenshot + verify SRS line

**Ai làm:** Dev BE / Dev FE tùy bug. Tester re-verify.

**KHÔNG dùng nhóm này khi:** chưa log bug — phải log bug TRƯỚC, mới mark TC nhóm B.

### Nhóm C — **Chờ BA confirm spec**

**Triệu chứng:** UI/API hoạt động khác spec NHƯNG hành vi có thể đúng (BR thay đổi gần đây, spec ambiguous, 2 spec khác nhau). Tester không thể quyết định Đạt/Lỗi cho đến khi BA xác nhận.

**Trigger phân loại:**
- 2 nguồn spec mâu thuẫn (vd FR-XX-01 vs §3.4.3.YY)
- SRS line ambiguous + dev claim "implement đúng theo BA verbal"
- Spec mới đề cập nhưng AC chưa có

**Phương án xử lý chuẩn:**
- (a) BẮT BUỘC quote nguyên văn 2 spec line vào cột "Vì sao"
- (b) BẮT BUỘC verify NotebookLM (project HTPLDN id `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) + grep SRS local (xem memory `feedback_bug_verify_notebooklm_local`)
- (c) Cột "Cần làm gì" = "BA confirm: spec X hay spec Y?"
- (d) NẾU BA chưa phản hồi sau 1 round → escalate user lead, KHÔNG defer im lặng

**Ai làm:** BA (chính) + QA + Dev cùng họp nếu phức tạp.

**KHÔNG dùng nhóm này khi:** spec rõ + dev claim "khác spec" mà không có verbal BA. Đó là Nhóm B (bug FE/BE).

### Nhóm D — **Lỗi env / chờ infra**

**Triệu chứng:** TC không chạy được vì môi trường thiếu component (sandbox, mock server, mTLS cert, API key, batch trigger, DB config). Code dev có thể đã đúng nhưng tester không kết nối được tới hạ tầng cần test.

**Trigger phân loại:**
- mTLS guard chặn outbound/inbound → cần Cổng PLQG sandbox
- Batch job chỉ chạy theo cron → cần dev expose trigger manual
- DB config (timeout days, feature flag) → cần dev đổi config dev env
- API key Cổng PLQG, MailHog OTP, webhook outbound → infra setup
- Test sandbox stub fail/race → dev BE tạo stub

**Phương án xử lý chuẩn:**
- (a) Liệt kê CHÍNH XÁC component thiếu trong cột "Vì sao"
- (b) Cột "Cần làm gì" = action infra/dev cụ thể (set config X / expose endpoint Y / cấp API key Z)
- (c) Tester có thể tự setup nếu thuộc QA scope (vd Postman); ngược lại escalate Infra
- (d) NẾU infra deploy lâu (>1 sprint) → coordinate workaround: dev BE expose CMS proxy nội bộ thay sandbox bên ngoài (pattern R12 TVN-022/029/038)

**Ai làm:** Dev BE / Infra / QA API tùy component.

**KHÔNG dùng nhóm này khi:** code dev chưa write — đó là Nhóm B/F.

### Nhóm E — **Dependency upstream chưa xong**

**Triệu chứng:** TC phụ thuộc kết quả của TC/task khác chưa hoàn thành. Khi upstream PASS, TC này sẽ chạy được.

**Trigger phân loại:**
- TC test cross-module mà module upstream chưa seed/test
- TC negative test cần state mismatch mà workflow chính chưa walk
- TC đánh giá / cập nhật metric mà entity gốc chưa có

**Phương án xử lý chuẩn:**
- (a) Cột "Vì sao" nêu RÕ task/TC upstream + state cần thiết (theo memory `feedback_dependency_chain_state_explicit`: `[need: ≥N entity state X]` không phải `[need: task ID ✅]`)
- (b) Cột "Cần làm gì" = "Run TC/task upstream Z trước"
- (c) Khi upstream xong → re-evaluate TC này, không tự động flip status
- (d) Theo dõi `tasks/state-snapshot.md` để biết khi nào dep thoả

**Ai làm:** Tester upstream → tester downstream verify.

**KHÔNG dùng nhóm này khi:** upstream đã PASS rồi nhưng tester chưa chạy → đó là Nhóm F (lý do khác — defer).

### Nhóm F — **Lý do khác (defer / out-of-scope)**

**Triệu chứng:** TC không thuộc 5 nhóm A-E. Có thể là:
- DB-level only (cần DBA query EXPLAIN, không có UI/API equivalent)
- Out-of-scope round (theo §4.1 phân nhóm B/C/D)
- Yêu cầu tool đặc biệt (Postman/Bruno cho outbound API mà QA chưa setup)
- Rủi ro thấp + cost cao (vd test 30 ngày timeout cần đợi thật)

**Phương án xử lý chuẩn:**
- (a) Cột "Vì sao" nêu RÕ lý do defer (DB-level / out-of-scope / cost cao)
- (b) Cột "Cần làm gì" = "Defer round X — chạy khi: [điều kiện cụ thể]"
- (c) Defer KHÔNG phải "không bao giờ chạy" — phải có round target cụ thể
- (d) NẾU defer >2 round → escalate user lead, đề xuất priority bump hoặc accept defer permanent

**Ai làm:** Tùy lý do — QA + lead cùng quyết.

**KHÔNG dùng nhóm này khi:** TC có nhóm A-E phù hợp. Nhóm F là last resort.

## 3. Format bảng output (bắt buộc)

Mỗi report (functional/workflow/smoke) BẮT BUỘC có 2 bảng. Đặt **ngay sau Verdict + Accounts** (LATEST round), TRƯỚC narrative deep-dive.

### Bảng 1 — Snapshot toàn bộ TC (mọi round, status mới nhất)

```markdown
## Bảng trạng thái TC (snapshot R{N} — LATEST YYYY-MM-DD HH:MM:SS)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| ... | ... | ✅/⚠️/❌/🚫/⏭/🤷 | R{N} | ... |
| **Tổng** | **N TC** | ✅X · ⚠️Y · ❌Z · 🚫W · ⏭V · 🤷U | | |
```

Status icon (terminology Việt — xem memory `feedback_qa_language_style`):
- ✅ Đạt (PASS clean)
- ⚠️ Sai spec (PASS but deviates SRS, Minor)
- ❌ Lỗi (FAIL — bug confirmed)
- 🚫 Không test được (BLOCKED — thiếu data/permission/env)
- ⏭ Hoãn (DEFER — out-of-scope round này)
- 🤷 Không xác định (CẤM kết luận — phải retry method)

### Bảng 2 — TC chưa chạy được × phân loại × phương án × owner

```markdown
## Bảng TC chưa chạy được (R{N}) — phân loại 6 nhóm

Hiện tại còn N TC chưa PASS — chia M nhóm: X chờ dev fix · Y chờ seed · Z out-of-scope · ...

| # | TC ID | Status | Nhóm nguyên nhân | Phương án xử lý | Ai làm |
|---|---|:-:|---|---|:-:|
| 1 | XXX-001 | ⏭ Hoãn | **Chờ dev fix bug** (BUG-XXX) | Dev BE wire event Y → re-test | Dev BE |
| ... | ... | ... | ... | ... | ... |
```

Cột "Nhóm nguyên nhân" BẮT BUỘC dùng tên A-F của template này (in đậm). Cột "Phương án xử lý" ≤25 từ. Cột "Ai làm" chọn 1: `Dev BE` / `Dev FE` / `QA seed` / `QA API` / `BA` / `Infra` / `DBA`.

## 4. Anti-patterns (CẤM)

- ❌ "Defer / TBD / Skip" mà không nêu lý do cụ thể trong nhóm A-F.
- ❌ Đặt 2 bảng ở cuối file thay vì sau Verdict.
- ❌ Dùng nhóm "Khác / Other" khi A-E phù hợp — phải pick 1 nhóm cụ thể.
- ❌ Ghi cột "Ai làm" = "QA team" / "Dev team" — phải role cụ thể (Dev BE vs Dev FE; QA seed vs QA API).
- ❌ Mark "🤷 Không xác định" — phải retry method (reload fresh, curl, isolatedContext) trước khi kết luận.
- ❌ Phân loại nhóm B mà chưa log bug — log bug ID trước, mark nhóm B sau.
- ❌ Defer >2 round mà không escalate user lead.
- ❌ Cột "Vì sao chưa chạy được" >25 từ — đẩy chi tiết vào bug-report hoặc footnote.

## 5. Workflow re-test sau dev unblock

Khi dev claim fix bug → quy trình re-test cho TC nhóm B/D:

1. **Capture state pre-test:** `take_screenshot` + `list_network_requests` baseline
2. **Re-run kịch bản gốc** TRƯỚC mọi modification — verify dev fix thực
3. **Verify SRS line khớp:** quote nguyên văn SRS local + query NotebookLM (memory `feedback_bug_verify_notebooklm_local`)
4. **Update bug-report:** Status Open→Closed + dòng `> **Re-test:** YYYY-MM-DD R{N} HH:MM:SS — ✅ PASS (Closed-verified). ...`
5. **Update todo.md:** dòng `**Bug:**` X/Y → (X+1)/Y; flip task icon nếu phù hợp (xem CLAUDE.md "State marker workflow")
6. **Update Bảng 1 + Bảng 2 trong functional report:** TC flip status ⏭/🚫/❌ → ✅, xoá khỏi Bảng 2

## 6. Reference

- CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp" (terminology + format)
- Memory `feedback_test_report_required_tables` (rule + reasoning)
- Memory `feedback_dependency_chain_state_explicit` (Nhóm E format)
- Memory `feedback_test_method_ui_only` (Nhóm A workflow)
- Memory `feedback_qa_block_must_seed_data` (anti-pattern Nhóm A defer)
- Memory `feedback_deep_review_before_ba_defer` (Nhóm C verify chuẩn)
- Memory `feedback_block_unlock_analysis` (Nhóm E workflow loop)
- `output/template/bug-report-template.md` (Nhóm B log bug đúng format)
- `tasks/state-snapshot.md` (Nhóm A + E verify state thực)
