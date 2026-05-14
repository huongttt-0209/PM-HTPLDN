# Lessons Learned — Round 5 PM HTPLDN

File ghi lại vấn đề thực tế gặp khi chạy QA + bài học áp dụng cho task sau. Không phải rule cứng — chỉ note để tránh lặp.

---

## 2026-05-11 — Tách workflow QA sau dev fix: re-verify bug ≠ audit full module

**Vấn đề:**
- Khi user cần "verify bug dev đã fix" và "kiểm tra module đã full luồng chưa", ban đầu tôi gom cả hai vào một skill/workflow `qa-bugfix-reverify-audit`.
- Cách gom này gây lệch trọng tâm:
  - Re-verify bug cần trả lời: bug dev claim fixed đã thật sự `Closed-verified` chưa, bug nào vẫn `Open/Partial`, TC/path nào được unblock để chạy tiếp.
  - Audit trạng thái module cần trả lời: toàn bộ module/chức năng đã full workflow chưa, coverage hiện tại là bao nhiêu, bug open/closed, blocker còn lại là gì, roadmap nào để hoàn tất full.
- Nếu không tách, report dễ vừa thiếu "TC có thể chạy tiếp sau bug fix", vừa thiếu "phương án tổng để full module".

**Quyết định xử lý:**
- Tách thành 2 skill trong project:
  - `.agents/skills/qa-bugfix-reverify-audit/` — dùng sau khi dev claim fixed bug.
  - `.agents/skills/qa-module-status-audit/` — dùng để review trạng thái tổng module/full luồng.
- Flow chuẩn:
  1. Dev claim fixed bug.
  2. Chạy `qa-bugfix-reverify-audit` để re-test bug, cập nhật bug `Open/Closed/Partial`, xác định TC/path được unblock.
  3. Chạy tất cả TC/path có thể chạy ngay hoặc có thể chạy sau QA-side setup.
  4. Chạy `qa-module-status-audit` để kết luận module đã full luồng chưa và còn blocker gì.

**Bài học áp dụng:**
1. **Không dùng một report để trả lời hai câu hỏi khác nhau.**
   - Re-verify bug là report tác nghiệp sau dev fix.
   - Module status là report quản trị/trạng thái tổng.
   - Nếu user hỏi "bug đã fix chưa" → dùng bugfix workflow. Nếu user hỏi "module đã full chưa" → dùng module status workflow.

2. **Sau re-verify bug phải có "testability sweep", không chỉ liệt kê TC unlock do bug fix.**
   - Rà tất cả TC/path `BLOCKED`, `DEFER`, `SKIP`, `Not run`, `Partial` liên quan.
   - Phân loại:
     - `chạy ngay`
     - `chạy sau QA setup`
     - `vẫn block bởi external owner`
   - Output bắt buộc: `Testability Sweep Sau Dev Fix` + `Setup Cần Chuẩn Bị Để Chạy TC Tiếp`.

3. **Không quy mọi defer/block thành "thiếu seed data".**
   - Taxonomy blocker cần đủ rộng:
     - thiếu seed data
     - thiếu state/data setup
     - thiếu account/role/permission
     - thiếu file/upload artifact
     - thiếu email/notification setup
     - chờ dev fix bug
     - chờ BA confirm spec
     - lỗi env/tooling
     - dependency upstream chưa xong
     - thiếu backdated/time-travel data
     - rate limit/session/JWT/OTP issue
     - data drift/cleanup làm mất pool
     - integration/API endpoint chưa deploy
     - cần DBA/API direct hỗ trợ setup
     - cần mock/stub lỗi external service
     - chưa đủ evidence/report cũ
     - lý do khác

4. **Case "chờ BA confirm spec" không được đẩy BA ngay.**
   - Bắt buộc search SRS local trước bằng TC ID / FR ID / rule ID / screen ID / field / enum / error code / label.
   - Ưu tiên nguồn: `input/srs-update-*` → `input/quy-trinh-nghiep-vu` → derived docs `output/funtion`, smoke specs, permission matrix, BA question docs.
   - Nếu có NotebookLM context/access thì cross-check sau SRS local.
   - Nếu SRS đã trả lời được → không gọi là BA-block nữa; đổi sang nguyên nhân thật: dev bug, setup/data gap, upstream, env/tooling.
   - Nếu SRS im lặng/mâu thuẫn → mới giữ `chờ BA confirm spec`, kèm câu hỏi BA cụ thể + evidence/gap.
   - Không bịa expected behavior để đóng câu hỏi; câu trả lời spec phải cite file local + line/section.

5. **Bug summary phải luôn có số Open/Closed.**
   - Report đầu bảng phải có `Bug Open` và `Bug Closed`.
   - Chi tiết phải có `Bug Summary` với `Open`, `Partial/Open`, `Closed`, `Closed-verified`, `New bug`.
   - Nếu todo và bug report lệch số → cite cả hai, ưu tiên timestamp mới hơn.

6. **Audit module status phải kết thúc bằng roadmap full luồng.**
   - Output bắt buộc: `Phương Án Để Hoàn Thành Full Luồng Chức Năng`.
   - Bảng cần trả lời:
     - mục tiêu hoàn tất
     - việc cần làm tiếp
     - loại blocker
     - owner
     - điều kiện xác nhận xong
     - TC/luồng được unblock
   - Đây là phần người quản lý cần nhất để biết "muốn full-pass thì làm gì tiếp".

**Anti-pattern phải tránh:**
- ❌ Re-verify bug xong kết luận luôn module `Ready/Not ready` khi chưa chạy follow-up TC.
- ❌ Chỉ chạy TC unlock do bug fix, bỏ qua TC defer có thể chạy sau setup nhỏ như account/file/mock/backdate.
- ❌ Ghi "chờ BA" mà chưa search SRS local/NotebookLM.
- ❌ Ghi "thiếu data" chung chung mà không nói cần record trạng thái nào, field nào, account nào, file nào, mock nào.
- ❌ Báo module chưa full nhưng không có roadmap để full.

**Áp dụng cho dự án sau:**
- Khi dev fix bug: gọi `qa-bugfix-reverify-audit`.
- Sau khi chạy hết follow-up TC có thể chạy: gọi `qa-module-status-audit`.
- Nếu report phát hiện blocker QA-side có thể chuẩn bị, ưu tiên setup và chạy ngay trước khi chốt module status cuối.

---

## 2026-05-09 — BA chốt QTHT KHÔNG có quyền tạo NHT (đóng 2 bug Invalid)

**Vấn đề trước:**
- R7.7.4.5 NHT functional log 2 bug Major (BUG-NHT-001 "QTHT thiếu CRUD UI" + BUG-NHT-002 "Modal thiếu field Đơn vị tự do cho QTHT") dựa vào SRS srs-fr-04 §SCR-IV-NHT-01/02 (line 1737-1738, 1781-1782) ghi rõ "QTHT thêm/sửa/xóa NHT toàn hệ thống".
- QA giả định spec đúng → log bug "permission inversion" Major P0.

**BA chốt 2026-05-09:**
- QTHT KHÔNG có quyền thêm/sửa/xóa NHT. Chỉ Read.
- CRUD NHT thuộc CB Nghiệp vụ (cùng đơn vị, BR-AUTH-08 lock).
- UI ẩn buttons Add/Edit/Delete/Swap với QTHT là **design đúng**.

**Tác động xử lý:**
- BUG-NHT-001 + BUG-NHT-002 đóng INVALID (re-classify, giữ lịch sử).
- BUG-NHT-003 (mail link broken) + BUG-NHT-004 (thiếu tab Bồi dưỡng) + BUG-NHT-005 (toast lỗi duplicate) giữ Open — không liên quan permission.
- functional-test-report-r7-7-4-5: NHT-001 QTHT path + NHT-007 sửa đơn vị → N/A. Pass rate 17% → 33% (3/9 active).
- permission-matrix.md QTHT/NGUOI_HO_TRO row đổi từ ✅ CRUD → 👁️ R + flag CHANGED.
- todo-nht.md cập nhật Kết quả + Bug closed count 0/5 → 2/5.

**Bài học áp dụng:**
1. **Spec ambiguous (UI ẩn nút trái spec) → hỏi BA trước khi log bug permission**, đặc biệt khi UI behavior không chỉ là "thiếu nút" mà còn align với BR-AUTH-08 / một role khác có CRUD.
2. SRS srs-fr-04 lines 1737-1738 + 1781-1782 + 2403-2409 là **outdated** — chờ BA update SRS để tránh QA cycle sau lại dựa vào spec cũ.
3. Phân biệt: "UI thiếu nút" (có thể là design đúng theo permission) vs "API trả 403/500" (rõ ràng bug). Test permission UI bằng đúng role có quyền theo SCR — đã có rule trong CLAUDE.md, lần này QA test bằng cb_nv_tw_03 ra đầy đủ button (đúng role) → OK; nhưng kết luận "QTHT thiếu UI = bug" sai vì giả định QTHT là root.

---

## 2026-05-08 — Probe TK creation timing (FR-VIII-15) + qtht_02 OTP bypass anomaly

**Probe TC1 R7.4.A1.6 — TK creation timing đúng spec FR-VIII-15:**
- Query `qtht_01` → `/quan-tri/tai-khoan` total=59 TK toàn hệ thống.
- Cross-check 3 cohort:
  - 6 CG batch 2 MOI_DANG_KY (CG-0023..0028) → **0 TK** (đúng — không tạo pre-mature)
  - 6 TVV batch 2 MOI_DANG_KY (TVV-0017..0022) → **0 TK** (đúng)
  - TVV-0013 CHO_KICH_HOAT (R7.4.A1) → **1 TK CHO_KICH_HOAT** (đúng — auto-tạo TK qua FR-VIII-15 step 6 khi state = CKH)
  - 6 CG batch 1 HOAT_DONG (CG-0001..0006) → **6 TK HOAT_DONG** (đúng — TK active sau set MK)
- **Kết luận:** BE timing đúng spec. KHÔNG phải bug. Khắc phục concern trước đó "có pre-mature tạo TK ở MDK không".

**Anomaly qtht_02 OTP bypass:**
- Login `qtht_02` + password `Secret@123` PASS, nhận OTP screen, fill OTP `666666` → BE trả 400 Bad Request.
- Login `qtht_01` + same flow → OTP `666666` work bình thường.
- Workaround: dùng `qtht_01` cho query TK admin scope.
- **Cần raise:** OTP bypass có specific allowlist account hay rate-limit per account? Log riêng nếu repeat ở task sau.

**ly_13 (CG-0001) login UI E2E ✅ — unlock CG flow:**
- TK đã set MK qua API thuần ở R7.2.9 vẫn login UI MCP `Secret@123` + OTP `666666` → dashboard.
- Sidebar 2 menu (Đào tạo + Tư vấn), KHÔNG có QTHT/Mạng lưới/Hỏi đáp/Vụ việc/Chi trả → permission đúng role CG.
- TVCS module render data scope đúng (1 record CG mình tham gia).
- URL force `/quan-tri/danh-muc` → FE redirect `/dashboard`.
- **Kết luận:** API path R7.2.9 không phải fake pass — TK 9/9 functional cho login UI + permission FE. Phần thiếu (click mail link UI + form set MK qua UI) dồn task R7.2.9b.

**Bài học:**
1. **Probe trước khi log bug timing** — concern "có pre-mature tạo TK ko?" nếu skip probe → có thể log bug ảo. 1 query qtht_01 = unlock toàn bộ concern, ROI cao.
2. **API path PASS không loại trừ UI E2E test** — phải verify thêm "TK functional cho login UI + permission đúng role + URL force protect" mới đủ E2E. R7.2.9b cover gap UI click mail + UI form set MK.
3. **OTP bypass anomaly** — không assume `666666` work cho mọi account QTHT. Fallback `qtht_01` nếu `qtht_02` fail. Memory `feedback_prefer_account_02_runs` giữ nguyên (default _02), chỉ note exception cho QTHT OTP path.

---

## 2026-05-08 — 7 task R7 vi phạm rule UI-only — flip ⚠️ retroactive defer R8 re-test

**Vấn đề:**
- Rule [`feedback_test_method_ui_only`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_test_method_ui_only.md) ban hành 2026-05-07: mọi seed/workflow/permission test phải UI MCP click chain. CẤM bulk POST API.
- Audit batch R7 (2026-05-06 chạy, trước rule 1 ngày): 7 task dùng API thuần / dominant.
- User chốt **retroactive enforce** + **flip ⚠️ truth in labeling** (KHÔNG grandfather), defer re-test R8.

**Task vi phạm flip ⚠️:**

| Task | File | Method observed |
|---|---|---|
| R7.2.2 | todo-tc-tv | API thuần `POST /api/v1/to-chuc-tu-vans` |
| R7.2.3 | todo-tc-tv | API dominant (1/5 record qua UI, 4/5 API) |
| R7.2.9 | todo-qtht | API thuần `/auth/first-login-password` + `/auth/reset-password` curl |
| R7.3.1 | todo-hoi-dap | API thuần `POST /api/v1/hoi-daps` |
| R7.3.2 | todo-vu-viec | API thuần `POST /api/v1/vu-viecs/manual` |
| R7.3.3 | todo-tvcs | API thuần `POST /api/v1/noi-dung-tu-van-cs` |
| R7.4.A5 | todo-tvcs | Đã ⚠️ + thêm UI gap note (3/11 step UI, 7 step API direct) |

**Task đã 🚫 KHÔNG cần flip:**
- R7.4.A4 (Hỏi đáp workflow) — đã 🚫 do BUG-HD-A4-001/002/003. Re-run buộc UI.

**Defer có justification (KHÔNG flip):**
- R7.1.5 ngày lễ — UI tab chưa deploy (DEPLOY-004 logged). Workaround API hợp lý đến khi UI deploy.

**Re-classify từ heuristic count sang COMPLIANT (audit subagent confirm):**
- R7.2.5 TVV TW, R7.2.6 CG TW, R7.2.7 NHT, R7.3.4 HSPL DN — UI dominant với screenshot evidence. Heuristic api/ui count nhầm.
- R7.4.A1 + R7.4.A1-CG (TVV workflow) — UI compliant; KHÔNG cần re-run vì UI compliance (chỉ re-run nếu BE fix bug và muốn verify).

**Phương án xử lý chốt:**
1. Flip ✅ → ⚠️ với coverage tag chuẩn `[~X% UI — reason, re-test UI per rule 2026-05-07]`.
2. Hook `auto-rescan-todo.py` cascade dep marker xuống downstream task.
3. Pool seed cũ (records API) **giữ nguyên** — KHÔNG xóa. Re-test sẽ ADD records mới UI bên cạnh, tránh cascade FK orphan vào R7.4.A1/A1-CG.
4. Acceptance R7.4.A6 (Workflow SM-TCTV mới) walk SM tạo 1 TC TV qua UI = 1 evidence record cho R7.2.2/2.3 partial UI cover.
5. Re-test full batch ~3.5-5h theo dep order: R7.2.2 → R7.2.3 → R7.3.1 → R7.3.2 → R7.3.3 → R7.2.9 → R7.4.A4 (sau khi BE fix bug).

**Bài học (META — về phản biện trước khi action):**
1. **User pick option không đồng nghĩa option đúng** — phải phản biện trước khi action, đặc biệt khi quyết định cascade nhiều task. Tôi đã chiều theo user 2 lần (split task R7.4.A6 + flip ⚠️ retroactive) — user phải nhắc "ko phản biện chiều theo ý mình à". Sửa: 3 câu phản biện claim/scope/recommend rank trước MỌI action.
2. **Heuristic count api/ui không chính xác** — `grep -c "POST"` đếm cả API verify (compliant) lẫn API direct (vi phạm). Phải read file content để classify thực sự. Audit subagent (general-purpose) làm việc này hiệu quả ~15p.
3. **Khi flip ⚠️ batch, dùng coverage tag state-explicit** — `[~X% UI — reason]` thay vì `[need: <task-ID>]`. Hook enforce.
4. **Cascade FK orphan risk** — pool cũ KHÔNG xóa khi re-test. ADD records mới UI bên cạnh. Workflow re-run dùng records mới hoặc records cũ tùy quyết định riêng.

---

## 2026-05-07 — FR-02 v3.5 typo SRS sao chép nhầm template state `DA_PHAN_CONG` từ FR-V.I-09 VU_VIEC sang HOI_DAP (KHÔNG phải mâu thuẫn nội bộ)

**Vấn đề:**
- Khi rà soát SRS [`srs-update-2026-5-5/srs-fr-02-hoi-dap.md`](../input/srs-update-2026-5-5/srs-fr-02-hoi-dap.md) v3.5, phát hiện state `DA_PHAN_CONG` xuất hiện 7 vị trí trong FR-II-04/05/06: filter cứng (line 317/385/400/404), Preconditions (line 448), Processing/Output/Postcondition/AC (line 474/498/502/509/511).
- Nhưng **CHECK constraint** entity HOI_DAP (line 1341) + **SM-HOIDAP diagram** (line 1488-1500) + **transition table** (line 1521) đều canonical 9 state KHÔNG có DA_PHAN_CONG.
- **Lỗi ban đầu của tôi (turn trước):** Tôi log như "mâu thuẫn nội bộ SRS v3.5 — chờ BA chốt giữ/bỏ" và đặt vào `srs-conflicts-need-ba.md` với 2 option (a) bổ sung DA_PHAN_CONG + (b) xóa khỏi 7 vị trí. Đặt làm gate block test plan FR-02.
- **User push back:** "deep review kỹ tài liệu cũng không có câu trả lời hả, bạn review kỹ lại". Re-verify với 4 nguồn ngoài srs-fr-02 → phát hiện root cause thực.

**Root cause (deep review 4 nguồn — verify kỹ thay vì 2):**
- Master [`srs-v3.md`](../input/srs-update-2026-5-5/srs-v3.md) line **1367** CHECK constraint: `DA_PHAN_CONG` thuộc entity **VU_VIEC** (12 state) — KHÔNG phải HOI_DAP.
- Master [`srs-v3.md:4985-5011`](../input/srs-update-2026-5-5/srs-v3.md) SM-VUVIEC: transition `DANG_KIEM_TRA → DA_PHAN_CONG → DANG_XU_LY/DA_TIEP_NHAN` cho FR-V.I-09/10 phân công NHT/TVV vụ việc.
- [`02-thu-tu-module.md:421/426/427/487`](../input/quy-trinh-nghiep-vu/02-thu-tu-module.md): bảng SM-VUVIEC dùng DA_PHAN_CONG. Đặc biệt line 487 đã có cảnh báo từ trước: *"Master SRS §C.1 enum có 9 state nhưng KHÔNG có DA_PHAN_CONG; tuy nhiên srs-fr-02 UC15 (FR-II-06) lại set trang_thai='DA_PHAN_CONG'. Đây là conflict trong SRS — cần CĐT thống nhất. Bảng dưới bám Master."* → người viết 02-thu-tu-module.md đã spot từ trước và quyết định bám Master.
- [`flow-module.md:184`](../input/quy-trinh-nghiep-vu/flow-module.md): SM-VUVIEC 12 state có DA_PHAN_CONG (cho VU_VIEC, không HOI_DAP).

**→ Đây là TYPO cherry-pick template:** BA copy template Processing từ FR-V.I-09 (Phân công VU_VIEC) sang FR-II-06 (Phân công HOI_DAP) v3.5 nhưng quên đổi state name. Cùng pattern "Phân công" nên 2 FR có template gần giống nhau. Master truth canonical đã có (HOI_DAP 9 state, không có DA_PHAN_CONG). Không phải feature ambiguous chờ BA chốt.

**Bài học (META — về cách verify SRS conflict trước khi log BA pending):**
1. **Khi spot inconsistency state machine, BẮT BUỘC verify 4+ nguồn ngoài file FR đang đọc** — không dừng ở "FR section dùng X nhưng CHECK constraint trong cùng file không có X". Phải mở Master `srs-v3.md` + `02-thu-tu-module.md` + `flow-module.md` xem state đó có thuộc entity khác không. Memory rule cross-project [`feedback_test_plan_check_sm_table.md`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_test_plan_check_sm_table.md) đã yêu cầu mở `02-thu-tu-module.md` trước khi viết test plan — nhưng tôi đã không apply lúc deep review conflict.
2. **Khi 02-thu-tu-module.md đã có cảnh báo từ trước** (vd line 487 "bám Master"), đó là đáp án của project — không cần tạo BA question mới, chỉ cần cite cảnh báo có sẵn + update test plan theo Master.
3. **"Mâu thuẫn nội bộ trong file FR" có 2 loại:** (a) feature ambiguous thực sự cần BA chốt, (b) typo cherry-pick template từ FR khác. Phân biệt bằng cách grep state name xuyên dự án — nếu state đó là canonical của module khác → typo, không phải (a).
4. **User push back là tín hiệu sớm.** Memory rule [`feedback_dev_pushback_critical_thinking`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_dev_pushback_critical_thinking.md) áp với dev push back. Logic tương tự với user push back trên review kết quả: phải verify lại 2 lần thay vì confirm rule cũ.

**Áp dụng (UNIVERSAL — mọi SRS state machine inconsistency):**
- **Step 1:** Spot state X dùng trong FR section nhưng không trong CHECK constraint cùng file → KHÔNG vội log BA pending.
- **Step 2:** Grep state X trong Master `srs-v3.md` (file root cùng folder v3.5) — nếu thuộc entity khác → typo template, log dưới dạng "BA fix typo SRS, không block test".
- **Step 3:** Grep state X trong `02-thu-tu-module.md` + `flow-module.md` — verify đó có phải canonical state của module khác không + có cảnh báo từ trước không.
- **Step 4:** Nếu Master + 2 file canonical đều cho state X thuộc module khác → kết luận TYPO. Test plan bám Master truth. Báo BA fix typo cosmetic.
- **Step 5:** Nếu Master + 2 file đều không có state X → đó là feature mới chưa chốt → log BA question với 2 option giữ/bỏ.

**Anti-pattern phải tránh:**
- ❌ Spot inconsistency trong 1 file → log BA pending → đặt làm gate block test mà không verify Master + 02-thu-tu-module.md trước.
- ❌ Cho rằng "BA cherry-pick chưa hoàn thiện" → assume feature mới → tạo gate block. Đa số trường hợp là typo template.
- ❌ Skip cảnh báo có sẵn trong 02-thu-tu-module.md (như line 487 đã spot từ trước "bám Master") → tự log lại như issue mới.

**Cost:** ~15 phút verify SRS lần đầu (chỉ check srs-fr-02) → log sai gate → 30 phút deep review cross-check 4 nguồn sau user push back → 20 phút sửa lại srs-conflicts-need-ba.md + todo.md + plan.md + lessons-learned.md. **Tổng cost lỗi: ~50 phút** vs ~10 phút nếu deep review từ đầu. Lesson: verify Master trước khi log BA pending là ROI cao nhất.

---

## 2026-05-06 — FR-02 v3.5 spec internal contradiction `DA_PHAN_CONG` (LEGACY — đã refine ở entry 2026-05-07)

> Entry này log lần đầu khi nhầm là "mâu thuẫn nội bộ chờ BA chốt". Sau push back của user, deep review xác định là typo template (xem entry 2026-05-07 trên). Giữ entry này làm reference về quá trình học.

**Vấn đề (đã refine):** State `DA_PHAN_CONG` ở 7 vị trí FR-II-04/05/06 nhưng không trong CHECK constraint HOI_DAP + SM diagram. Tôi nhầm là "BA pending giữ/bỏ" — thực ra là typo cherry-pick từ FR-V.I-09 VU_VIEC sang FR-II-06 HOI_DAP. Master `srs-v3.md` line 1367 + 4985-5011 + 02-thu-tu-module.md line 487 + flow-module.md line 184 đều canonical = DA_PHAN_CONG thuộc VU_VIEC, HOI_DAP 9 state KHÔNG có.

**Root cause refine:** Tôi không apply rule "mở 02-thu-tu-module.md + flow-module.md trước khi log conflict" — chỉ check 1 file srs-fr-02 nội bộ.

---

## 2026-05-06 — SRS v3.5 partial release: 12/16 file FR slice + master fallback cho 4 file thiếu

**Vấn đề:**
- BA phát hành SRS v3.5 ngày 2026-05-06 (CHANGELOG-v3-to-v3.5.md). Folder `input/srs-update-2026-5-5/` chỉ có **12/16 file FR slice**: fr-01 đến fr-10 + fr-12 + fr-13. Thiếu **fr-11 (Báo cáo) / fr-14 (HĐ TV) / fr-15 (CT HTPLDN) / fr-16 (API)**.
- Đã verify qua NotebookLM (notebook `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) — kết quả khẳng định: "phần chi tiết FR của Nhóm IX, X.3, XI, XII thuộc các file `srs-fr-11/14/15/16` không xuất hiện trong phạm vi tài liệu hiện tại". Đây là **chủ ý của BA**, không phải drift bug — 4 file này còn đợi Pha 3 reconcile.
- **Hệ quả:** mọi reference owner FR-14 / FR-16 trong các file v3.5 (vd FR-09 §4 stub redirect HOP_DONG_TU_VAN → `srs-fr-14-hop-dong-tv.md`) đang trỏ về file **không tồn tại** trong v3.5 folder.
- Master `srs-v3.md` v3.5 (cùng folder) vẫn giữ entity HOP_DONG_TU_VAN block đầy đủ (line 1853) với `Tham chiếu FR: FR-X.3-01` — đây là **source-of-truth tạm** cho FR-14 đến khi có file riêng.
- Tương tự, FR-16 changes (rename `la_cong_khai` → `cong_khai` trong API filter) chỉ ghi trong CHANGELOG, không có file slice riêng để verify.

**Root cause:**
1. **Cherry-pick không đồng đều.** BA cherry-pick từ v4 sang v3.5 nhưng dừng ở 12 file đã review xong. 4 file còn lại để Pha 3.
2. **Naming convention mâu thuẫn.** File slice trong v3.5 ghi ngày apply 2026-05-06 ở header → tester nhầm tưởng "tất cả file đã apply". Thực tế chỉ 12 file.
3. **Cross-reference broken.** Stub redirect trong fr-09 trỏ về fr-14 → tester click không thấy file → nghi vấn drift bug.

**Bài học:**
1. **Trước khi viết test plan/task cho 1 module, verify file slice TỒN TẠI trong v3.5 folder.** Nếu thiếu → đọc spec từ master `srs-v3.md` (search §3.4.3 cho entity, §3.2 cho FR, Phụ lục B cho BR, Phụ lục C cho SM).
2. **Cross-reference NotebookLM khi nghi ngờ drift.** Notebook `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` (project HTPLDN v3.5) có metadata 16 file FR — query để xác nhận file nào real, file nào pending.
3. **Slice drift trong file reference (chỉ "referenced" không "owned") KHÔNG phải bug nghiệp vụ.** Vd `srs-fr-13-tv-nhanh.md` line 750 còn `la_cong_khai` cho HOI_DAP — owner FR-02 đã rename đúng `cong_khai`. Đây là drift slice, source-of-truth FR-02 đúng → flag minor không block.

**Áp dụng (UNIVERSAL — mọi SRS update batch có file slice + master file):**
- **Step 1:** Mở `ls input/srs-update-*/` đếm số file FR slice. Compare với mục lục §3.2.1 trong master.
- **Step 2:** Với module có file slice → đọc slice. Với module thiếu file slice → đọc master section §3.2.<X> + §3.4.3.<Y> + Phụ lục B/C.
- **Step 3:** Với entity owned bởi module thiếu file slice (vd HOP_DONG_TU_VAN owned bởi FR-14) → master là source-of-truth. Tag rõ trong test plan: `_(spec từ srs-v3.md line N — file slice fr-XX chưa release)_`.
- **Step 4:** CHANGELOG-v3-to-v3.5.md có changes của FR-XX nhưng không có file slice → ghi rõ "Pha 3 pending" trong todo. Không tạo task QA chạy cho phần này cho đến khi file slice release.

**Anti-pattern phải tránh:**
- ❌ Cho rằng "v3.5 folder = tất cả module v3.5 ready" → tạo task R8 cho FR-14/16 dựa trên CHANGELOG → khi chạy thấy file slice không có → block phải hỏi BA.
- ❌ Log bug "stub redirect trỏ file không tồn tại" → đây là pattern intentional của partial release.
- ❌ Update test artifact 7.14 / 7.16 dựa trên CHANGELOG (high-level summary) thay vì master srs-v3.md (low-level spec).

**Cost:** 30 phút deep verify 3 ambiguity (master HOP_DONG_TU_VAN refs / v3.5 thiếu file / fr-13 line 750 drift) — nếu bỏ qua sẽ tốn ~1 round QA chạy bằng spec sai.

---

## 2026-05-06 R7.0.2 — False positive 2/8 bug deploy gap do verify bằng QTHT (sai role)

**Vấn đề:**
- Plan-r7-trigger.md ngày 2026-05-06 list 8 bug deploy gap (DEPLOY-001..008). Trong đó:
  - DEPLOY-002 "Sub-menu UI 'Người hỗ trợ pháp lý' chưa thêm vào sidebar Mạng lưới TVV"
  - DEPLOY-003 "Sub-menu UI 'Tổ chức tư vấn' chưa thêm (BE đã có endpoint)"
- User push back "mình vào web vẫn thấy Tổ chức tư vấn mà". Retest qua MCP với `qtht_01` → confirm chỉ thấy 1 sub-menu "Tư vấn viên / Chuyên gia". User push back tiếp "QTHT có quyền không?".
- Login lại bằng `cb_nv_tw_01` (CB Nghiệp vụ TW) → sub-menu "Mạng lưới Tư vấn viên" hiện đầy đủ 3 sub-menu: Tư vấn viên / Chuyên gia + **Tổ chức tư vấn** + **Người hỗ trợ pháp lý**.
- SCR-IV-01 SRS line 1474-1477 spec "Quyền truy cập" chỉ Cán bộ Nghiệp vụ + Cán bộ Phê duyệt + TVV/CG — KHÔNG có QTHT. Đây là feature đúng spec, không phải bug.

**Root cause:**
1. **Default mental model "QTHT all-access".** QA verify deploy mặc định login qtht_01 vì là role admin — assume QTHT thấy mọi UI element. Sai cho menu/submenu/tab có gating per-permission.
2. **Plan-r7-trigger không ghi rõ test bằng role nào.** Khi verify "sidebar Mạng lưới TVV chỉ 1 sub-menu" — không note login bằng account nào → reproducer thiếu, dễ miss.
3. **Bug bị rơi vào confirmation bias.** Verify deploy chạy tuần tự `qtht_01` → kết luận "thiếu" cho tất cả menu/submenu — không retest với role khác trước khi log.

**Bài học:**
1. **Verify "UI element thiếu" BẮT BUỘC test bằng role có permission per SCR.** Memory cross-project: [`feedback_verify_ui_gap_role_permission.md`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_verify_ui_gap_role_permission.md).
2. **Pre-test UI surface audit** cần task riêng với checklist `[Spec ref / UI element / Required role / Verify status / Bug ID nếu thiếu]` extract từ SRS update.
3. **Bug report "missing UI element" phải quote line SRS role permission + role đã test.** Nếu thiếu, dev/PM đọc bug không reproduce được.

**Findings phụ kèm verify lại 8 bug:**
- DEPLOY-001 (NHT BE 404) + DEPLOY-004 (HOC_VIEN BE 404): vẫn cần curl re-verify hôm nay
- DEPLOY-002 + DEPLOY-003: ❌ FALSE POSITIVE — drop khỏi list
- DEPLOY-005 (4 sub-menu Đào tạo): ✅ CONFIRMED với cb_nv_tw_01 — chỉ thấy 5 sub-menu cũ
- DEPLOY-006 (Tab Ngày lễ Cấu hình HT): ✅ CONFIRMED với qtht_01 — Cấu hình HT 4 tab cố định + Danh mục dùng chung 14 mục đều không có Ngày lễ
- DEPLOY-007 (Filter Địa bàn): ⚠️ SAI MÔ TẢ — SRS không bỏ filter, chỉ rename label "Địa bàn" → "Đơn vị quản lý". Bug đúng = label sai (Minor UI copy)
- DEPLOY-008 (Tab Chờ kích hoạt): ⚠️ SAI TÊN TAB — web có 6 tab, SRS quy định 7 tab. Tab thiếu thực sự = "Chờ thẩm định" (CHO_THAM_DINH state), KHÔNG phải "Chờ kích hoạt"

**Áp dụng:**
- Trước khi log "UI element missing" → grep section "Quyền truy cập" SCR + login đúng role.
- Mỗi SRS update batch → tạo pre-test UI surface audit task với checklist per-role.
- Bug report "missing UI" entry phải quote role permission line + role tested.

---

## 2026-05-02 R11 — A5 TVCS BLOCK lần 4 (Round 11) do seed actor không advance state + bug template vi phạm cũ chưa cleanup

**Vấn đề:**
- R6.4.A5 todo gốc đánh giá `[full 100% — R6.3.3 ✅ + CG account ✅ + FK link ✅. KHÔNG cần A1.5]` → flip 🟢 sai. Khi chạy thực tế: dropdown FR-12 phân công CG trống vì 5 CG seed R6.2.5 stuck `MOI_DANG_KY/YEU_CAU_BO_SUNG`, dropdown filter `trangThai=DANG_HOAT_DONG ∧ loaiTvv=CG` trả 0 record.
- 6 active TVV (state DANG_HOAT_DONG) đều `loaiTvv=TVV` → không match filter `loaiTvv=CG`.
- R6.4.A1 (TVV) ngẫu nhiên advance 6 TVV state → tester/planner nhầm tưởng "advance state là phần test workflow" áp dụng luôn cho CG → R6.2.5 dừng ở "saved 6/6", không advance.
- Bug report flow-tvcs.md mới + flow-hoidap.md mới có section "Tác động" / "Đề xuất fix" — vi phạm rule có sẵn từ 2026-04-23 (CLAUDE.md line 73). User đã nhắc lần 2.
- TVV-0008 missing trong UI (R6.2.5 claim 6 CG, UI thấy 5 = 0007 + 0009-0012). Acceptance "PASS 6/6" không cross-check UI count.

**Root cause (3 lớp):**
1. **Plan acceptance dừng ở "đã tạo" — không đến "consumer dùng được".** R6.2.5 acceptance theo count + LV coverage, không có verify query downstream.
2. **Không phân biệt 2 loại state machine cùng entity.** TVV/CG có profile state (`MOI_DANG_KY → DANG_HOAT_DONG`) khác workflow state (`MOI → TIEP_NHAN → ...`). Workflow test ngẫu nhiên advance profile state → tạo cảm giác "advance state là phụ" → R6.2.5 (CG) lặp lại sai lầm.
3. **Rule có sẵn không enforce bằng hook.** Memory `feedback_seed_acceptance_strict_split` (2026-04-29) đã ghi rule, CLAUDE.md đã quote, nhưng chỉ enforce todo line ngắn + count sync, không enforce semantic dependency chain.

**Bài học (3 rule mới — saved cross-project memory):**
1. **Mỗi entity actor (TVV/CG/NHT/GV/CB/học viên) BẮT BUỘC 2 task tách:** `seed-create` (state default) + `advance-state` (state đáp ứng filter consumer). Không gộp. Memory: [`feedback_seed_actor_state_gap.md`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_seed_actor_state_gap.md).
2. **Dependency tag `[need: ...]` phải nêu STATE + verify query, KHÔNG nêu chỉ task ID.** ❌ `[need: R6.3.3 ✅ + CG account ✅]` ✅ `[need: ≥1 CG mỗi LV ở DANG_HOAT_DONG (verify GET /tu-van-viens?trangThai=DANG_HOAT_DONG&loaiTvv=CG&linhVucIds=<id>)]`. Memory: [`feedback_dependency_chain_state_explicit.md`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_dependency_chain_state_explicit.md).
3. **Bug detail strict 6 sections.** Cấm Tác động/Đề xuất fix/SRS verification/Phân biệt module. Hook enforce. Memory: [`feedback_bug_report_template_strict.md`](../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_bug_report_template_strict.md).

**Áp dụng (UNIVERSAL — mọi entity actor có downstream consumer khác module):**
- Trigger: entity có dropdown ở module khác + có state machine (profile state).
- Step 1: trước khi viết task seed entity actor, mở `input/data/entity-map.md` (cột "Đọc tại") + grep SRS filter từng consumer.
- Step 2: nếu filter consumer yêu cầu state ≠ default → tách task `<entity>-advance-state` riêng. Acceptance `[need: ≥N record state X (verify <query>)]`.
- Step 3: task `seed-create` đóng ✅ chỉ khi verify query downstream PASS, không chỉ "saved N/N".
- Step 4: dependency chain phải nêu state + verify query, không nêu task ID.
- Step 5: bug report mới — strict 6 sections; cleanup bug report cũ trước khi viết mới (tránh copy pattern cũ).

**Anti-pattern (toàn project):**
- Acceptance "PASS N/N saved" — chỉ chứng minh seeder, không downstream.
- Dependency `[need: <task-id> ✅]` hoặc `[full 100%]` không có state verify.
- Gộp "advance state" vào "test workflow" — workflow test có thể không cover hết entity.
- Trust icon ✅ task upstream — task icon là intent, state là reality. Verify reality.

**Cost của lesson này:**
- 1 round QA test wasted (R6.4.A5 R11) ~30 phút setup + 20 phút discover root cause.
- 30 phút plan re-baseline (thêm task R6.4.A1-CG, update todo bảng tổng).
- Pattern lặp lại từ R5/R6/R7 (memory `feedback_seed_acceptance_strict_split` 2026-04-29) — thực tế 4 lần fail liên tiếp cùng pattern. Lesson này phải khóa cứng bằng hook + template, không bằng memory đơn thuần.

**Liên quan:** R6.3.10 GV (giảng viên) sẽ gặp pattern tương tự — entity GV cũng có profile state + dropdown consumer khác module (FR-III). Khi BA confirm SRS contradiction (chi tiết: [`tasks/decisions/giangvien-srs-contradiction-2026-04-27.md`](decisions/giangvien-srs-contradiction-2026-04-27.md)), apply ngay 3 rule mới cho R6.3.10.

---

## 2026-04-28 → 2026-04-29 — A5 TVCS FAIL do seed acceptance gộp scope (R5/R6/R7)

**Vấn đề:**
- Acceptance T1.B3 viết "12 variant TVV" — không split `loai_tvv` (TVV/CG/NHT).
- Acceptance A5 viết "6 CG/TVV ACTIVE" — gộp CG+TVV trong khi SRS strict "Chỉ CG".
- Kết quả R5: seed 12 TVV / 0 CG vẫn pass gate. R6/R7: split T1.B3b (6 CG) + T1.B3c (3 NHT) lấp gap, nhưng FE TVCS bug enum lệch nên dropdown vẫn empty (BUG-FLOW-TVCS-003).

**Bài học:**
1. Acceptance seed entity nhiều loại phải **split combinatorial**: entity × state × flag × lĩnh vực × downstream consumer. Không gộp.
2. **Pass acceptance theo số lượng ≠ đủ data downstream.** "Seed 12 record" pass nhưng filter `loaiTvv=CG ∧ DANG_HOAT_DONG ∧ la_cong_khai=true` có thể trả 0. Phải verify bằng query thực tế cho từng filter downstream.
3. Sau khi seed actor mới (TVV/CG/NHT), kiểm tra Phân công mặc định (QTHT) có cần row mapping không — dropdown có data nhưng gợi ý vẫn rỗng nếu thiếu mapping (xem A2b R7).
4. **Entity-map phải có TRƯỚC khi viết acceptance seed**, không phải sau. Đảo lại thứ tự: entity-map → đọc downstream consumer → split acceptance.
5. Khi FE bug + seed gap đồng thời, không gộp 2 vấn đề. R4 từng nhầm root cause "BE filter strict đơn vị" → phí 1 round. R5 mới ra root cause FE enum lệch.

**Áp dụng (UNIVERSAL — mọi seed task entity có ≥2 chiều combinatorial trong toàn dự án, không chỉ TVV):**
- Trigger: entity có CHECK constraint enum / loại / cấp / flag / lĩnh vực ≥2 chiều (TU_VAN_VIEN, DOANH_NGHIEP, HO_SO_PHAP_LY, BIEU_MAU, MAU_PHAN_HOI, TAI_KHOAN, KHOA_HOC, DANH_MUC, NHCH, ĐKT, CTDT, BAI_GIANG, ...).
- Step 1: mở [`input/data/entity-map.md`](../input/data/entity-map.md) đọc cột "Đọc tại" → liệt kê tất cả downstream task.
- Step 2: cho mỗi downstream, quote nguyên văn SRS filter (`srs-fr-X line N` + `02-thu-tu-module §`).
- Step 3: acceptance split combinatorial: entity × state × flag × LV × cấp × downstream. Không gộp 2 chiều.
- Step 4: pass acceptance bằng verify query thực tế per filter downstream (không chỉ đếm tổng).
- Step 5: section "Downstream consumer × filter" trong [`output/template/seed-checklist-template.md`](../output/template/seed-checklist-template.md) là blocker — mọi seed task mới phải fill section này trước khi seed.
- Step 6 (sibling-check): per memory `feedback_test_plan_check_sm_table`, mở SM table 02-thu-tu-module + check ≥2 module sibling đọc entity này trước khi viết acceptance.
- Pair task seed actor + task QTHT phân công khi cần (vd A2 cho TVV → A2b cho CG/NHT).

**Anti-pattern phải tránh (toàn project):**
- "Seed N variant" mà không split chiều.
- Pass acceptance theo COUNT(record) thay vì verify per-filter query.
- Viết acceptance khi chưa đọc entity-map.
- Gộp 2 loại entity (CG+TVV, TW+ĐP, siêu nhỏ+nhỏ) trong 1 acceptance.

**Liên quan:** R4 cũng từng có pattern tương tự với GIANG_VIEN (SRS contradiction §Inputs vs §3.4.3.x).

---

## 2026-04-28 — LGSP / Cổng PLQG sync hay lỗi

**Vấn đề:** 2 bug Critical cùng pattern phát hiện cross-module:
- BUG-FLOW-BIEUMAU-001 (R5 trụ C1): "Lỗi đồng bộ" Cổng PLQG khi advance Biểu mẫu CONG_KHAI.
- BUG-FLOW-CTHTPLDN-001 (R5 P3.3 pilot TW): `POST /publish` → HTTP 502 khi công bố CT.

**Bài học:**
- Module có sync ra Cổng PLQG: BIEU_MAU · CT_HTPLDN · TVV (Công khai) · HOI_DAP (Công khai) · KHOA_HOC (DA_CONG_KHAI).
- Khi test các module này → expect LGSP có thể down. Workaround: dùng path alt skip công bố nếu SM cho phép (vd CT HTPLDN: `DA_DUYET → DANG_THUC_HIEN` skip `DA_CONG_BO`).
- Bug log nhóm theo pattern, link nhau cross-reference.
- Escalate dev/infra config LGSP credentials + retry + graceful fallback.

---

## 2026-04-28 — UI auto-chain nhiều transition vào 1 click

**Vấn đề:** 2 case UI gộp 3 transition thành 1 click:
- TVV: "Gửi KQ" tab Thẩm định → auto-chain `MOI_DANG_KY → CHO_THAM_DINH → DANG_THAM_DINH → YEU_CAU_BO_SUNG` (3 transition). UI thiếu nút [Tiếp nhận] + [Bắt đầu thẩm định].
- CT HTPLDN: stepper auto-tick "Công bố" dù skip path #7a (DA_DUYET → DANG_THUC_HIEN bỏ qua DA_CONG_BO).

**Bài học:**
- Khi UI advance state nhanh hơn SM define → log finding "UI auto-chain", pending BA confirm:
  (a) Design choice OK → SRS update simplify
  (b) UI thiếu nút intermediate → build thêm
  (c) Verify BE audit log có ghi từng transition không
- Stepper UI có thể tick step không thực sự đi qua → cosmetic finding, không block test nhưng note.

---


## 2026-05-10 — BE flag conditional theo creation method (UI form vs API direct) — false-positive 4 round trên BUG-MAIL-FL-001

**Vấn đề:** BUG-MAIL-FL-001 (Email promise force-change MK lần đầu nhưng implementation không enforce) bị flag Open across 4 round R7.1-R7.3 do tester dùng path API direct tạo TK (`POST /api/v1/tai-khoan` + `PATCH /trang-thai {hanhDong:KICH_HOAT}`) thay vì UI form click chain. R7.4 retest qua UI form → ✅ PASS clean.

**Root cause:** BE chỉ set flag `mustChangePassword: true` cho TK tạo qua UI form. Direct API skip logic đó → login response không có flag → FE không render modal "Đặt mật khẩu mới" → tester kết luận FAIL nhầm. Implementation thực ra đã đúng từ đầu, dev fix correct.

**Bài học:**

1. **Mọi bug auth/first-login/notification/onboarding flow phải UI chain verify, KHÔNG shortcut qua API.** BE có thể có flag conditional theo creation method (vd: `created_via_ui` metadata, request header, trigger logic in FE controller). API direct = bypass logic = false negative.

2. **Trigger force UI verify** (cho R8+ và sau):
   - Bug liên quan first-login / change-password / activate flow.
   - Bug liên quan email content vs implementation behavior.
   - Bug liên quan FE modal blocking / route guard.
   - Bug có user-facing message ("hệ thống sẽ yêu cầu...").

3. **API chỉ dùng để inspect (network tab) hoặc verify BE chấp nhận khi UI broken** (vd RESET MK R7.7.8c — UI thiếu form `/auth/forgot-password` nên fallback API là correct, đã ghi rõ trong bug). KHÔNG dùng API để TẠO TK rồi test login flow.

4. **Discipline check trước retest:** tự hỏi 3 câu trước khi mark FAIL:
   - "Tôi tạo TK/dữ liệu qua đúng flow user thực sẽ dùng không?"
   - "BE có thể đặt flag/metadata phụ thuộc creation context không?"
   - "Manual test trên UI có cho kết quả khác API test không?"

5. **Anti-pattern điển hình tôi đã làm:**
   - Lý do: API nhanh hơn UI form click chain (~3s vs ~30s), test scale hơn.
   - Hậu quả: 4 round false-positive, dev mistakenly tin bug còn open, user đã phải nhắc "manual on system thấy okie rồi".

6. **Bug-report disclosure khi phát hiện tester error:** thêm section `## ⚠️ Tester Error Disclosure` đầu bug-report ghi rõ round nào INVALID + nguyên nhân + lessons-learned link. KHÔNG ẩn / KHÔNG xóa retest cũ — giữ lại để minh bạch process.

**Reference:**
- Memory rule cũ: `feedback_test_method_ui_only` (2026-05-07) — tôi vi phạm khi retest BUG-MAIL-FL-001 R7.1-R7.3.
- Bug case: [`Pass-bug-report-mail-first-login-promise-not-enforced.md`](../output/qa-reports/round7-2026-05-06/bug-reports/qtht-tai-khoan/Pass-bug-report-mail-first-login-promise-not-enforced.md).
- Audit kết quả 2026-05-10: scan 22 bug-report R7 → CHỈ BUG-MAIL-FL-001 có pattern này. Các bug API-direct khác (RESET MK, NHT, JWT revoke, TVCS, chi-tra) đều correct context (UI broken / data verification / BE behavior bug).

---

## 2026-05-13 — R20 deep-verify finding: 5/9 bug Open có vấn đề do dùng SRS cũ + quote sai mã

**Vấn đề:**
Sau R20 reverify 9 bug Open, deep-verify SRS v3.5 + NotebookLM phát hiện **5/9 bug có vấn đề** (~56%):

| Bug | Vấn đề | Verdict |
|---|---|---|
| BUG-FUNC-DG-016 | Dùng state machine v3 cũ (6 states gồm `DA_DANH_GIA`). v3.5 đã đổi 8 states không có state này. | INVALID — đóng |
| BUG-VV-FN-PC-CROSS-CAP-01 | Hiểu sai ERR-PC-05 = chặn user khác đơn vị, không chặn cross-cấp TVV. NĐ 77/2008 cho TVV toàn quốc. | INVALID — đóng |
| BUG-BC-KYBAOCAO-NOT-VALIDATED | Giả định BE phải groupBy theo enum theoKy. SRS chỉ định là filter range. | WONT-FIX — đóng |
| BUG-VV-FN-PC-INACTIVE-01 | Đúng concept BE phải chặn inactive, NHƯNG expect mã `ERR-PC-06` (sai). Đúng là `ERR-PC-02`. | Rewrite mã ERR |
| BUG-VV-PC-WRN-01 | Prescribe button text "[Tìm thủ công]". SRS chỉ yêu cầu mechanism (có thể button / toggle / clear filter). | Rewrite mechanism |

Talk-past-each-other 8+ round vì:
- QA log bug expect 1 thứ
- Dev hiểu khác hoặc fix theo cách ad-hoc (vd dùng mã `ERR-VAL-VI-PC-09` thay vì `ERR-PC-02`)
- Re-test fail → log lại → cycle lặp.

**Root cause 5 pattern:**

1. **QA dùng SRS v3 cũ thay vì v3.5** — DG-016 (state machine), một phần BC-KYBAOCAO.
2. **QA quote sai mã ERR** — VV-PC-INACTIVE (expect PC-06 → đúng PC-02), BC-DATA-SCOPE-LEAK (ref FR-XIII → đúng FR-IX).
3. **QA hiểu sai context spec** — VV-PC-CROSS-CAP (hiểu ERR-PC-05 là cross-cấp, đúng là khác đơn vị).
4. **Bug viết prescriptive** — VV-PC-WRN-01 (button) thay vì describe requirement (mechanism).
5. **SRS tự mâu thuẫn** — E2E-S4-011 (FR-05 dùng `LOAI_HINH_HT` vs FR-10 dùng `LOAI_HINH_HO_TRO`).

**Quyết định xử lý — 6 hành động cứng (đã viết vào dev-fix-list.md):**

1. **Quy trình 3-step verify TRƯỚC khi log bug:**
   - Step A: Check SRS version. Cấm reference `srs-v3/` nếu module có `srs-update-2026-5-5/`.
   - Step B: Grep nguyên văn mã ERR / FR ID / state / enum. Quote `<file_path>:<line>` vào bug.
   - Step C: NotebookLM cross-check 1 query cho mã ERR / state machine có nguy cơ hiểu sai.

2. **Bug template strict thêm field "Theo SRS quote nguyên văn":**
   ```
   Theo SRS `<file_path>:<line>`:
   > "<text>"
   ```
   Thiếu file:line + quote → bug không hợp lệ.

3. **State machine + enum reference card** — tạo `input/data/state-machines-v3.5.md` với 14 module × state v3.5 + bảng chuyển đổi v3→v3.5.

4. **SRS contradiction tracking** — tạo `tasks/srs-contradictions.md`, mỗi tuần escalate BA chốt.

5. **Bug wording rule** — describe requirement, KHÔNG prescribe implementation.
   - ❌ "FE thiếu button [Tìm thủ công]"
   - ✅ "FE thiếu mechanism cho phép tìm/override LV"

6. **Hook enforcement (deferred)** — `check-bug-srs-version.py`, `check-bug-err-code-quoted.py`, `check-bug-state-machine-quoted.py`. Sau khi rule stabilize 2-3 round.

**Bài học áp dụng:**

1. **Mỗi round QA đầu tiên: list spec v3.5 hiện có.** Update CLAUDE.md note nếu module nào chỉ còn v3.
2. **Khi log bug: BẮT BUỘC grep `<mã ERR / state / enum>` SRS v3.5 + quote.** Không có quote = bug entry không hợp lệ.
3. **Khi spec ambiguous / contradict: STOP log bug, escalate BA trước.** Đừng force interpretation.
4. **Re-test bug lần 2+: BẮT BUỘC deep-review SRS lại.** Có thể bug viết sai từ đầu, không phải dev không fix.
5. **Bug viết theo "describe what's broken (per spec)" — KHÔNG "prescribe implementation"**. Implementation là việc dev quyết.

**Reference:**
- Verdict R20 deep-verify: [`output/qa-reports/round7-2026-05-06/reverify-2026-05-12/dev-fix-list.md`](../output/qa-reports/round7-2026-05-06/reverify-2026-05-12/dev-fix-list.md) — section "Phương án xử lý triệt để".
- Memory rule liên quan: `feedback_deep_review_before_ba_defer.md` (2026-05-07) — extend rule này: trigger deep-review không chỉ cho "BA defer" mà cho **mọi bug Open >2 round + bug có mã ERR/state machine specific**.

---
