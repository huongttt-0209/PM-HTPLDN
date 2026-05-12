# Review — FR-07 Doanh nghiệp test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:05:00
**Source:** docs/todo-test/fr-07-doanh-nghiep/test-plan.md (293 lines)

## Gaps

- **Đếm trường DN không nhất quán nội tại** — §1.1 line 19 nói `DOANH_NGHIEP (28 trường)`, §2.4 line 124 cũng nói "form 28 trường", nhưng count thực tế bảng entity SRS (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:438-462`) chỉ 22 attribute (+ 7 common fields = 29). Đồng thời SCR-V.III-02 line 323-354 list 28 component (component ≠ field — gồm cả label/Mã DN readonly/file upload). User prompt nói "21 trường" → mismatch 3 chiều (21 / 22 / 28). TC `DN-002` claim "tab Thông tin cơ bản 28 trường" sẽ FAIL nếu app render khác.
- **Quy mô switch → impact chi trả FR-06 chưa cover** — User prompt yêu cầu "quy mô switch impact chi trả % ở FR-06". Test plan chỉ có `DN-004/005` test auto-suggest + warning `WRN-DN-01`, KHÔNG có TC verify đổi `quy_mo` của DN → chi trả % cho VV liên quan có recompute hay không. Cross-module dependency này không nằm trong `03-TC-cross-module-dropdown.md` (chỉ test dropdown visibility).
- **Filter logic `linh_vuc_ids[]` claim AND không có SRS quote** — `DN-017` line 211 nói "AND logic" nhưng SRS line 231 chỉ nói "Kết hợp tất cả điều kiện lọc có giá trị (AND)" — đây là AND giữa các filter khác nhau (quy_mo AND tinh_thanh), không phải AND giữa các option multi-select trong cùng `linh_vuc_ids`. Multi-select cùng field thông thường là OR (in clause). Cần SPEC-CLARIFY trước khi đóng test.
- **BR-AUTH-EMAIL-01 ID không có trong SRS local** — Test plan line 72 cite `srs-fr-07:449` cho BR-AUTH-EMAIL-01. Đọc line 449 thật → chỉ nói "KHÔNG UNIQUE ... BR-AUTH-EMAIL-01, không cần OTP". BR này không có row riêng trong §6 Business Rules (line 515-528). Đây là BR module-specific tự đặt — phải mark là cross-module BR từ FR-VIII-22 hoặc giữ làm SPEC-CLARIFY.
- **BR-DATA-06 (Export Excel) inference không có quote ngoại lệ** — SCR-V.III-01 line 284 có nút "Xuất Excel" → BR-DATA-06 áp dụng. NHƯNG Lịch sử thay đổi line 17 nói: "Quyết định CĐT/BA — BỎ chức năng Xuất Excel khỏi FR-V.III-01 (Thay đổi 5 cũ trong delta — đã OUT, không apply vào v3.5)". Contradiction nội tại SRS — Lịch sử nói BỎ nhưng bảng component vẫn còn nút. Test plan claim BR-DATA-06 áp dụng có thể sai. TC `DN-022/023` rủi ro FAIL hoặc dead spec.
- **5 trường công khai CR-01 (SPEC-CLARIFY-FR07-01) — kết luận sai chiều** — Test plan §2.4 cuối line 142 nói "Inputs prompt nói có nhưng grep SRS local không tìm thấy". User prompt review yêu cầu "5 trường công khai CR-01 v3.5 áp dụng?". Grep `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` không có mention `cong_khai`/`anh_dai_dien`/`thoi_gian_dang_tai` → kết luận đúng KHÔNG áp dụng cho DN entity, nhưng test plan giữ SPEC-CLARIFY làm "ambiguous" thay vì kết luận dứt khoát.
- **Permission row NHT mơ hồ** — Line 105 "tab 1+2" cho NHT Read detail — không có ref SRS. NHT đọc tab Thông tin cơ bản DN dựa trên permission gì? SPEC-CLARIFY-FR07-03 line 273 đã raise nhưng vẫn để row trong bảng → cần move row sang "pending clarify" hoặc xóa khỏi matrix.
- **TC create flow self-reg cross-link mỏng** — Line 36 nói "KHÔNG cover luồng tạo DN — DN tạo qua self-reg FR-VIII-22 → cover ở test plan FR-10". Đúng scope, nhưng tiền điều kiện line 167 `≥6 DN self-reg HOAT_DONG` requires FR-10 self-reg đã chạy xong. Không có dependency note `[need: ...]` format state-explicit theo CLAUDE.md "State marker workflow".
- **CHECK constraint chưa cover `tong_nguon_von`** — SRS line 469 có `CHECK (tong_nguon_von >= 0)`. TC `DN-036/037/038` test `so_lao_dong`, `so_lao_dong_nu`, `tinh_thanh_id` nhưng MISS test `tong_nguon_von < 0` reject. SRS line 469 explicit nên gap rõ ràng.
- **TC tổng = 40 nhưng phân bổ Negative chỉ 12.5% (5 TC)** — Industry baseline negative ≥25%. Một số gap: không test `email` format invalid (Inputs #15 line 111 yêu cầu "Format email hợp lệ"), không test `nguoi_dai_dien` blank (Y bắt buộc — line 109).
- **Audit log AUDIT_LOG verify method chưa rõ** — `DN-003` claim "verify AUDIT_LOG ghi giá trị cũ → mới". App có UI Audit log không? Phải DB query? Method này chưa nêu — risk BLOCKED nếu không có endpoint admin xem audit.

## Suggestions

- **Lock số trường thực tế ở 22 attribute SRS + 7 common = 29**, hoặc đếm theo UI component (28 row SCR). Note rõ trong TC `DN-002`: "verify đúng số input visible khớp SCR-V.III-02 bảng line 323-354".
- **Thêm TC `DN-041` cross-module: đổi `quy_mo` DN từ NHO → VUA → verify chi trả % VV cũ recompute** theo `srs-fr-06-chi-tra.md` công thức (nếu BR-CALC tồn tại). Hoặc move sang FR-06 test plan với ref ngược.
- **SPEC-CLARIFY-FR07-04 mới**: AND vs OR cho `linh_vuc_ids[]` multi-select — verify BA + dev BE intent trước test.
- **Xóa hoặc giữ Xuất Excel — escalate BA ngay**: contradiction Lịch sử thay đổi vs SCR-V.III-01 line 284. Nếu BỎ → bỏ TC `DN-022/023` + `DN-032` không cần verify dead button (vì button không có sẵn).
- **Thêm TC negative `email` format invalid + `nguoi_dai_dien` blank** để đẩy negative ratio lên 20-25%.
- **Thêm TC `tong_nguon_von` < 0 reject** (line 469 SRS).
- **Format `[need: ...]` state-explicit** trong §2.6 Tiền điều kiện theo CLAUDE.md "State marker workflow". Vd: `[need: ≥6 DOANH_NGHIEP trạng_thái=HOAT_DONG (verify GET /doanh-nghiep?trang_thai=HOAT_DONG count≥6)]`.
- **Verify method AUDIT_LOG**: nêu cụ thể MCP `list_network_requests` capture API call hoặc curl GET `/audit-logs?entity=DOANH_NGHIEP` (nếu exposed). Nếu không có → flip TC `DN-003` xuống P1 và mark dependency.
- **Move SPEC-CLARIFY-FR07-03 NHT permission ra khỏi bảng main matrix** — đặt vào "pending" subsection để tránh tester test row mơ hồ thành false negative.
- **Sibling-check chưa làm** (line 293 footer) — chạy đối chiếu §2.1 BR với FR-05/FR-12 trước BA sign-off như test plan tự nhận.

## Verdict

**REVISE** — Test plan có cấu trúc tốt và cite SRS chặt, nhưng có 3 lỗi correctness phải fix trước: contradiction số trường (21/22/28), contradiction Xuất Excel (Lịch sử vs SCR), và MISS cross-module impact quy mô → chi trả FR-06 (đây là yêu cầu chính prompt).
