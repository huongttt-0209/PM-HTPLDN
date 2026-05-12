# Review — FR-05 Vụ việc test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:44:52

## Gaps

- **State count drift (12 vs 9 vs 10):** Phần 1.1 ghi "12 trạng thái" và `srs-update-2026-5-5/srs-fr-05-vu-viec.md:45,2052` cũng 12 enum, nhưng task brief gọi "9-state SM". Test-plan §2.5 phân bảng đủ 12 row OK; nhưng §1.1 line 22 lại ghi "12 trạng thái, 18+ transition (gồm 2 self-loop)" trong khi §2.5 đếm 21 transition + 3 self-loop. Sửa §1.1 → "12 trạng thái, 21 transition + 3 self-loop" để khớp §2.5 và tránh contradiction.

- **Thiếu TC bảng đếm cho cross-cutting (TC-AUTH/PERM/SLA/SEARCH/AUDIT/DATA/EXPORT/PAGE/NOTIF/EVAL/CONFLICT/LOCK/DELETE/NEW02/YCBS/CK):** §2.1 cite các TC-ID cross-cutting (TC-AUTH-01..05, TC-PERM-01..12, TC-SLA-01..06, TC-NOTIF-01..06, TC-AUDIT-01..04, TC-DELETE-01..02, TC-EXPORT-01..02, TC-PAGE-01, TC-DATA-01..02, TC-CONFLICT-01, TC-CK-01..05, TC-YCBS-01..03, TC-EVAL-04, TC-LOCK-01, TC-NEW02-04, TC-SEARCH-01..02, TC-KT-01..03, TC-PC-01..05) — tổng ~62 TC — nhưng §3 file structure CHỈ list 23 file (`01-TC-list-filter.md` đến `25-TC-data-migration.md`). Bảng §4 cho thấy mỗi file 3-10 TC, tổng 130. Vấn đề: §2.1 TC-IDs không map 1:1 vào file nào trong §3. Phải ánh xạ mỗi cross-cutting TC-ID → file cụ thể (vd `TC-AUTH-01 → 22-TC-perm-cross-unit.md`), nếu không tester sẽ không biết phải viết TC này ở đâu.

- **Hard-delete cross-cutting C1 chưa cite SRS update FR-05:** §1.1 line 35 + §2.1 BR-DATA-01 row đều nhắc "hard-delete bỏ DA_XOA" cite `01-tong-quan-nghiep-vu.md §6.3 (1)`. Tuy nhiên `srs-update-2026-5-5/srs-fr-05-vu-viec.md:2052` enum trạng thái CHỈ có 12 state đã liệt kê (không có `DA_XOA`) — cite chỉ là negative absence. Cần cite line cụ thể trong `01-tong-quan-nghiep-vu.md` ở format chuẩn `01-tong-quan-nghiep-vu.md:229` (test plan ghi vague "§6.3 (1) line 229" KHÔNG có path prefix theo rule `feedback_bug_srs_ref_path`). TC25 data migration sẽ verify ra sao? Test plan thiếu acceptance criteria cho hard-delete (phải verify `DELETE` thật xóa row, không soft-delete `is_deleted=1`).

- **Mâu thuẫn BR-DATA-01 vs C1 hard-delete:** §2.1 BR-DATA-01 row ghi "Soft delete" với ngoại lệ "C1 cross-cutting v3.5: hard-delete bỏ DA_XOA" — đây là **mâu thuẫn** trực tiếp với SRS line 2397-2401 ("Mọi thao tác xóa đều là soft delete"). 2 nguồn (SRS FR-05 vs cross-cutting `01-tong-quan`) đang nói khác nhau cho cùng entity VU_VIEC. Test plan chưa flag SPEC-CLARIFY ticket — phải tạo task hỏi BA quy định nào áp dụng cho VU_VIEC trước khi viết TC, không thì TC25 sẽ defer hoặc cho kết quả sai.

- **BR-AUTH-10 lọc kép nguồn không thuộc SRS FR-05:** §2.1 row BR-AUTH-10 cite `input/quy-trinh-nghiep-vu/01-tong-quan-nghiep-vu.md:194-197` — chính xác có dòng đó (đã verify), nhưng `srs-update-2026-5-5/srs-fr-05-vu-viec.md` KHÔNG nhắc BR-AUTH-10 lần nào và CHANGELOG dòng 17 ghi rõ "Thay đổi 10 (đổi tên FR-V.I-15 + BR-AUTH-10) OUT". Vậy BR-AUTH-10 áp dụng cho FR-05 dựa vào source nào ngoài tong-quan? Phải cite cụ thể `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` line N (nếu BR-AUTH-10 owned bởi FR-04) hoặc `srs-v3.md` Phụ lục B; hiện cite chỉ tong-quan nghiệp vụ (không phải SRS chính).

- **FR-V.I-NEW-02 cross-ref tới FR-06 (Chi trả) bị thiếu hoàn toàn:** Task brief đề cập "DN bổ sung HSCT (FR-V.II-14 cross-ref to FR-06)". Test plan §1.2 row 19 (`19-TC-dn-bo-sung.md`) CHỈ nói "DN bổ sung HS (YEU_CAU_BO_SUNG → DANG_KIEM_TRA)" — thuần SM transition T10. Không có TC nào cover edge case DN bổ sung *HSCT* (Hồ sơ chi trả) cross-module sang FR-06. Theo brief, cần defer rõ ràng hoặc add TC marker "out-of-scope, defer FR-06 plan". Hiện test plan im lặng.

- **TC25 data migration `nguoi_ho_tro_id` chỉ 3 TC, nhưng risk schema cao:** §1.1 line 32 ghi rõ 3 cột phân công mới + bỏ `nguoi_ho_tro_id`; _DELTA-MAP-FR05 §3 ghi "schema migration risk cao". Bảng §4 cho `25-TC-data-migration.md` chỉ 0 Happy + 1 Negative + 2 Edge = 3 TC. Open issues §6 trong _DELTA-MAP nói "Migration data cũ — SRS không cover", nghĩa là cần ≥5 TC: (a) VV cũ có `nguoi_ho_tro_id` hiển thị thế nào ở SCR-V.I-03 Accordion 5, (b) migration script đặt `loai_doi_tuong_xu_ly='CA_NHAN'` + `nguoi_xu_ly_id = nguoi_ho_tro_id`?, (c) báo cáo FR-11 đọc trường cũ break ra sao, (d) audit log LICH_SU cho migration event, (e) edge `nguoi_ho_tro_id NULL` (VV chưa phân công cũ). 3 TC không đủ.

- **TC-CK (công khai) thiếu test BR-PUBLIC-04 outbound payload verification:** §1.2 row 20 + §4 ghi 10 TC. §2.1 BR-PUBLIC-04 ghi "TC-CK-02..03 verify API payload outbound chỉ 9 fields". Tuy nhiên test plan KHÔNG ghi rõ phương pháp verify — env QA có mock server Cổng PLQG không? Nếu không, BR-EC-20 (KHÔNG set `cong_khai=1` trước API OK) làm sao trigger được? Phải add note: "Cần mock Cổng PLQG endpoint hoặc intercept request qua MCP `list_network_requests`. Defer nếu chưa có mock — nhóm D Lỗi env".

- **Thiếu TC cho 3 placeholder transition không có FR formal (T15 auto-return, T21 mở lại, T12 auto 3 lần):** §2.5 bảng row T15 + T21 ghi "(placeholder dev impl UI v3)" + _DELTA-MAP §3 Findings critical #7 confirm "3 transition không có FR formal" do Thay đổi 5/6/7 OUT. Test plan §1.2 KHÔNG có file TC riêng cho 3 transition này; chỉ TC09/06 cover happy path forward. Cần explicit TC-PLACEHOLDER-01..03 với acceptance "expected behavior follow v3 UI rules + BR-EC-15/16; nếu UI render khác → defer, không log bug".

- **UC67 PRE-03 `Role ∈ {CB_NV, DN}` vs §2.3 Permission Matrix row `DANH_GIA_VU_VIEC chấm UC67`:** §2.3 matrix row UC67 ghi "QTHT ❌, CB_NV ✅ scope, CB_PD ❌ (CSV UC67 exclude), DN ✅ own DN, NHT ❌, TVV ❌, CG ❌". SRS line 1177 nói rõ `Role ∈ {CB_NV, DN}`. Vấn đề: matrix row KHÔNG ghi rõ QTHT cũng exclude (chỉ ghi ❌ nhưng KHÔNG cite). Phải thêm note "QTHT ❌ vì không nằm trong CSV UC67 enum CB_NV/DN" để tester P0 không nhầm QTHT có quyền chấm.

- **BR-AUTH-08 exception cite chỉ 1 chiều:** §2.1 BR-AUTH-08 row ngoại lệ ghi "'QTHT và Cán bộ Trung ương' — line 2393". SRS line 2393 đúng có exception, nhưng test plan §2.3 matrix row "VU_VIEC danh sách (R)" ghi QTHT="All" và CB_NV_TW="TW scope". "All" vs "TW scope" là 2 phạm vi khác nhau — QTHT thấy toàn quốc KHÔNG filter `don_vi_id`, CB TW thấy toàn quốc nhưng vẫn có thể filter. Test plan chưa làm rõ khác biệt → TC-PERM dễ FAIL false negative khi QTHT thấy được data bị CB TW lọc.

- **Test method UI BẮT BUỘC qua MCP nhưng test plan KHÔNG nhắc:** Rule project (CLAUDE.md "Tool routing — BẮT BUỘC từ 2026-05-05") + memory `feedback_test_method_ui_only` (2026-05-07) yêu cầu MỌI test phải UI click chain qua Chrome DevTools MCP, không API direct. Test plan §3-§5 chỉ ghi file structure + bảng đếm, KHÔNG note test method. Phải thêm §4.x "Test method: MCP Chrome DevTools mặc định; API verify chỉ qua `list_network_requests` supporting evidence theo CLAUDE.md".

- **Thiếu Bảng 1 + Bảng 2 cho execution report:** CLAUDE.md "Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC sau mỗi round (enforced 2026-05-10)" yêu cầu mọi functional report có Bảng 1 (snapshot toàn bộ TC × status) + Bảng 2 (TC non-PASS × nguyên nhân × phương án). Test plan §5 "Tiêu chí đạt/không đạt" chưa link template `output/template/test-case-execution-report-template.md` và chưa nhắc 2 bảng này. Add cross-ref để tester R1 không quên format.

- **SLA 15 ngày — chưa cite NĐ69/2024 + NĐ55 Đ.8 K.1 status verify:** §6 Pháp lý row "NĐ 69/2024 — SSO VNeID — chưa web-verify, defer" — OK. Nhưng NĐ55 Đ.8 K.1 (SLA 15 ngày) — _DELTA-MAP §6 Open issues confirm "Cite NĐ 55 Đ.8 K.1 chưa web-verify, defer khi test". Test plan §2.1 BR-SLA-01 không flag warning này. Tester R1 dễ log BUG-FALSE khi BE deploy theo SLA cũ 10 ngày. Phải add note "BR-SLA-01: cite NĐ55 Đ.8 K.1 chưa web-verify — verify qua BA trước khi log bug nếu BE trả deadline = 10 ngày LV".

- **UC106 checklist 6 hạng mục covered nhưng KHÔNG có TC verify config UC106 nguồn từ đâu:** §2.1 BR-LEGAL-02 row cite SRS line 516-523 (6 hạng mục). Test plan §1.2 row 6 (`06-TC-kiem-tra.md`) 7 TC. SRS line 530 step 3 "Tải checklist từ cấu hình UC106" — checklist là **configurable** (UC106 thuộc FR-10 QTHT). TC plan thiếu edge case: QTHT thay đổi UC106 thì VV đang DANG_KIEM_TRA xài checklist cũ hay mới? Versioning giống FR-V.I-NEW-01 không? Đây là cross-module dep upstream FR-10 chưa cite.

## Suggestions

- **Bổ sung mapping table TC-ID ↔ file:** Thêm bảng cuối §2 mapping mỗi cross-cutting TC-ID (TC-AUTH-01..05, TC-PERM-01..12, TC-CK-01..05, ...) → 1 file `XX-TC-*.md` cụ thể. Hiện tester không biết viết TC-AUTH-03 vào file nào (22 hay 23?).

- **Tách `06-TC-kiem-tra.md` thành 06a (kiểm tra happy) + 06b (BR-EC-15 3-lần auto TU_CHOI):** Hiện 7 TC trong 1 file, mix happy + edge case BR-EC-15 (counter 1/2/3 + auto TU_CHOI lần 4). BR-EC-15 là rule v3.5 critical, deserve file riêng để dễ trace bug và rerun isolated.

- **Add §2.7 "TC defer policy" cho 3 placeholder + cross-module dep:** List rõ TC nào defer (vd T15 auto-return placeholder, FR-V.II-14 DN bổ sung HSCT cross FR-06, NĐ69/2024 cite) với rationale + verification trigger.

- **Add seed pre-check vào §2.6:** Hiện §2.6 nói "verify per query downstream" + cite memory `feedback_seed_acceptance_strict_split`. Bổ sung concrete verify commands: `MCP list_network_requests` filter URL `/api/v1/tu-van-vien?loai_tvv=TVV&trang_thai=HOAT_DONG` để đếm count realtime, mỗi LV ≥1. Verification command pattern theo `tasks/state-snapshot.md` enforced 2026-05-07.

- **Thay tất cả "≥3 TVV/cấp ĐP" bằng "≥1 record per filter":** Test plan §1.3 line "Lưu ý seed TVV" ghi "≥3 TVV/cấp ĐP + ≥1 CG/TW + ≥1 TC TV". Convention project (CLAUDE.md "Quy tắc seed task — A5 R7 fail") yêu cầu acceptance theo **filter coverage**, KHÔNG theo count tổng. "3 TVV/ĐP" nếu cả 3 trùng LV thì vẫn thiếu — phải reword "≥1 TVV per LV cần test × cấp ĐP test, verify qua `?loai_tvv=TVV&linh_vuc=X&don_vi_id=Y`".

- **Add explicit TC cho BR-FLOW-03 + QTHT force-edit:** §2.1 BR-FLOW-03 cite "QTHT có thể force-edit (audit đặc biệt)". TC-LOCK-01 chỉ verify "VV đã duyệt KHÔNG sửa được" — thiếu TC verify QTHT vẫn override được + audit log đặc biệt (`BR-FLOW-03` exception). Thêm TC-LOCK-02 QTHT force-edit happy path + TC-LOCK-03 audit log có flag `is_force_edit=true`.

- **Renumber file TC để fill gap row 8:** §3 thiếu `08-TC-*.md`. FR-V.I-08 (UC58 search) gộp vào `01-TC-list-filter.md`. Để tránh nhầm lẫn, hoặc rename file thành `01-TC-list-search-filter.md`, hoặc giữ `08-TC-search-only.md` riêng (P1, 2-3 TC for SQL/XSS injection BR-EC-13).

- **Thêm section §7 "Test method + tool routing":** Note rõ "Mặc định Chrome DevTools MCP cho mọi UI test; isolated context per role per CLAUDE.md memory `qa_htpldn_round5_t01`; OTP bypass `666666`; auth pattern `Template login MCP`". Cấm gstack `$B` ngoài fallback. Cấm API direct cho seed test. Tester mới onboard sẽ rõ tool ngay.

- **Add ghi chú DN account convention:** §1.3 ghi DN dùng `9999999990` (HN), `9999999991` (BG). Đây là MST DN, không phải username VNeID Tier 2 thật. Trên app QA hiện không có VNeID sandbox — DN test sẽ login thế nào? Phải add note "DN bypass auth qua mock cookie / role overlay theo memory `qa_htpldn_round5_t01`; nếu BE đã wire VNeID sandbox NĐ69/2024, dùng tài khoản test mock".

- **Đổi "TC sẵn 130" thành range 125-140:** Bảng §4 đếm chính xác 130 nhưng các file TC chưa được tạo. Khi viết detail TC có thể phát sinh edge mới (vd EC-V.I-05-01..13 đã có 13 edge UC55 inbound — `srs-update-2026-5-5:469-481`). Để con số chính xác sau khi viết detail, ghi range "~130 TC (±10%)".

- **Add cross-module dep section:** Brief task #3 yêu cầu "Cross-module out (FR-06/14/08) noted". Test plan §2.6 cite "Đọc tại FR-06/FR-08/FR-11/FR-14" rời rạc. Tạo bảng riêng "Cross-module downstream impact" liệt kê: FR-06 (Chi trả) đọc `vu_viec_id`, FR-08 (Đánh giá tổng hợp) đọc DANH_GIA_VU_VIEC, FR-11 (Báo cáo) đọc cong_khai filter, FR-14 (Thông báo) đọc THONG_BAO. Mỗi cross-ref → TC verify smoke 1 màn hình downstream sau khi FR-05 PASS.

- **Verify cite path consistency:** Test plan trộn 2 style cite: `srs-update-2026-5-5/srs-fr-05-vu-viec.md:2074` (full path) và `:1652-1693` (short). Memory `feedback_bug_srs_ref_path` 2026-05-06 yêu cầu path PREFIX bắt buộc. Replace all short refs (vd `:1664` ở §2.4) bằng full `srs-update-2026-5-5/srs-fr-05-vu-viec.md:1664`.

## Verdict

**REVISE** — Coverage 21 FR + 12 state SM + 130 TC tổng thể đầy đủ và cite SRS đúng line trong phần lớn case, nhưng còn 4 blocker phải fix trước R1 thực thi: (1) mâu thuẫn BR-DATA-01 soft-delete vs C1 hard-delete chưa flag SPEC-CLARIFY; (2) BR-AUTH-10 cite nguồn không thuộc SRS FR-05; (3) TC25 schema migration chỉ 3 TC trên rủi ro cao; (4) cross-cutting TC-ID (~62 TC) không map vào file structure §3 nên tester không biết viết ở đâu. Sau khi fix 4 blocker + apply ≥6 suggestion (mapping table, test method note, defer policy, seed verify command) plan có thể APPROVE.
