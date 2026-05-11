# Functional test report — R7.7.2 CG/TVV 31 TC

**Ngày chạy:** 2026-05-07 R7
**Account:** `cb_nv_tw_02` (Secret@123, OTP 666666)
**Spec:** [funtion/7.4-chuyen-gia-tvv.md](../../../../funtion/7.4-chuyen-gia-tvv.md) — UC39..50 (28 TC ID, kèm 5 sub TC = 33 TC)
**SRS ref:** `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` (FR-IV-01..16)
**Scope:** functional behavior + UI structure + validation + cross-cut với R7.4.A1/A1-CG/A2 walks

## Verdict

⚠️ **PASS ~97% (R30 LATEST 2026-05-11 02:58:00)** — 32 ✅ Đạt · 0 ❌ Lỗi · 1 ⚠️ Sai spec (BUG-RETRY-005 STILL OPEN — R30 NHT cùng đơn vị + CB role đều fail với 2 permission rule BE sai khác nhau; TVV TU_CHOI `taiKhoanId=null` → rule "chủ hồ sơ" deadlock) · 0 🚫 Không test được · 0 ⏰ Hoãn (= 33 TC). **R30 UI verify cho RETRY-005:** seed mới `nht_btp_tw_audit_r30` (NHT BTP-TW cùng đơn vị TVV-BTP-TW-0011) → probe `/nop-lai` 2 role khác nhau (NHT 403 ERR-PERM-SYS-00-01; CB 403 ERR-PERM-IV-NL-02). **Cần BE rework + BA fix SRS** (xem [bug-report RETRY-005](../../bug-reports/tu-van-vien-cg/bug-report-functional-r7-7-2-tvv-retry.md)).

> **R7.7.2 R30 UI verify RETRY-005 (2026-05-11 02:58:00):** lấp data gap R28 bằng seed mới `nht_btp_tw_audit_r30` (NHT BTP-TW cùng đơn vị TVV-BTP-TW-0011, `donViId=00000000-0000-4000-8000-000000000001`) qua UI MCP click chain (cb_nv_tw_02 → Thêm mới NHT → mail kích hoạt → Quên mật khẩu → set Secret@123 → login OTP 666666).
> - **NHT cùng đơn vị (nht_btp_tw_audit_r30):** `POST /api/v1/tu-van-viens/720eda6c-.../nop-lai` body `{version:5, hoTen, cccd, ghiChu}` → **403 ERR-PERM-SYS-00-01** "Forbidden" (generic, BE chặn role NHT toàn bộ). GET TVV-BTP-TW-0011 → 200 OK (NHT có quyền đọc).
> - **CB_NV_TW BTP-TW (cb_nv_tw_02, permission `bo-sung_tu_van_vien`):** cùng endpoint cùng body → **403 ERR-PERM-IV-NL-02** "Chỉ chủ hồ sơ mới được nộp lại".
> - **UI flow R30:** login `nht_btp_tw_audit_r30` → /chuyen-gia-tvv/{id}/chinh-sua → form load đầy đủ → click Lưu → FE block validation "File thẻ hành nghề bắt buộc" (giống R28). Evidence: [r30-retry005-nht-cung-donvi-403.png](../../bug-reports/tu-van-vien-cg/img/r30-retry005-nht-cung-donvi-403.png).
> - **Phát hiện mới R30:** TVV TU_CHOI có `taiKhoanId=null` (FR-IV-03 line 348 "TVV chưa có tài khoản khi chưa kích hoạt") → BE permission rule "chủ hồ sơ" = **deadlock không actor nào pass được**. Bug không chỉ "sai rule" mà còn "rule không thể thực hiện được" cho mọi TVV TU_CHOI.
> - **TVV-023** giữ ⚠️ Sai spec — yêu cầu cho dev không đổi: (1) đổi perm `/nop-lai` sang "NHT cùng đơn vị" (BR-AUTH-08 + SCR-IV-02:1462); (2) bỏ endpoint riêng → save-trigger PATCH (line 1571 + 2308); (3) BA fix SRS line 2314 mâu thuẫn line 1462 + 366.

> **R7.7.2 R28 UI verify RETRY-005 (2026-05-10 19:55:00):** chạy lại UI MCP cho RETRY-005 theo rule `feedback_test_method_ui_only` (R27 chỉ API direct). Test 2 actor:
> - **NHT cross-don_vi** (nht_01 STP-AG → TVV BTP-TW-0011 TU_CHOI): GET /tu-van-viens/{id} → **403** (cross-don_vi check working) → form rỗng → click Lưu không fire request. Evidence: [r28-retry005-nht-cross-donvi-403.png](../../bug-reports/tu-van-vien-cg/img/r28-retry005-nht-cross-donvi-403.png)
> - **CB_NV_TW BTP-TW** (cb_nv_tw_02, full perm, đại diện thử actor "có quyền"): UI navigate /chuyen-gia-tvv/{id}/chinh-sua → form load đầy đủ Lê Văn Chuyên Gia → click Lưu → **FE block validation** "File thẻ hành nghề là bắt buộc đối với Tư vấn viên" (TU_CHOI cũ thiếu file). Upload file dummy via POST /api/v1/files/upload → **403 ERR-PERM-FILE-01**. Evidence: [r28-retry005-cb-luu-noresult.png](../../bug-reports/tu-van-vien-cg/img/r28-retry005-cb-luu-noresult.png)
> - **TVV-023** giữ ⚠️ Sai spec (đổi từ Partial → Open): BUG-CG-77-RETRY-005 STILL OPEN — UI verify confirm BE design sai 2 chỗ. (1) Permission rule "chủ hồ sơ" thay vì "NHT cùng đơn vị" per SCR-IV-02 line 1462. (2) Endpoint `/nop-lai` riêng thay vì PATCH save-trigger pattern per FR-IV-04 line 1571. SRS line 2314 SM-TVV mâu thuẫn line 1462 + line 366 — cần BA fix.
> - **Note data gap (không phải method block):** "NHT cùng don_vi" lý tưởng cần seed mới (5 TVV TU_CHOI hiện đều donViId BTP-TW; NHT seed chỉ STP-AG/STP-DN). Defer khi BE rework xong.

> **R7.7.2 R27 re-verify dev fix wave 4 (2026-05-10 18:35:00):** dev wave 4 sau R26 push fix lại 3 bug Open. Verify qua API browser MCP (cb_nv_tw_02 + isolatedContext qa_r27_verify; nht_01 + qa_r27_nht).
> - **TVV-022 nhánh có VV** đổi ⚠️ → ✅ Đạt: BUG-RETRY-004 Closed — DELETE TVV-BTP-TW-0004 (Trương Văn Mười Sáu, gắn VV-BTP-TW-20260507-002 phan-cong CHO_XAC_NHAN) → **HTTP 409 ERR-TVV-05** "Không thể xóa: TVV còn vụ việc đang xử lý". State sau = HOAT_DONG (record không hard-delete). BR-LEGAL-04 enforced sau 4 lần verify R23-R26. [r27-retry004-tvv0004-409-fixed.png](../../bug-reports/tu-van-vien-cg/img/r27-retry004-tvv0004-409-fixed.png)
> - **TVV-015** đổi ❌ → ✅ Đạt: BUG-RETRY-007 Closed — endpoint `GET/POST /tu-van-viens/{id}/danh-gia` + alias `POST /vu-viecs/{vvId}/danh-gia-tvv` đã build. Insert 2 record DANH_GIA_SAU_VU_VIEC → meta avgChuyenMon=4.5, avgThaiDo=5, avgDungHan=4, diemTb=4.5, tongSoDanhGia=2. TVV detail `diemDanhGiaTb=4.5 + soLuongDanhGia=2` — BR-CALC-06 trigger working. FR-IV-09 step 5+6 satisfied. [r27-retry007-danh-gia-endpoint-fixed.png](../../bug-reports/tu-van-vien-cg/img/r27-retry007-danh-gia-endpoint-fixed.png)
> - **TVV-023** giữ ⚠️ Partial: BUG-RETRY-005 — endpoint `POST /tu-van-viens/{id}/nop-lai` đã build (R26 trả 404 → R27 trả 422 validate version + 403 ERR-PERM-IV-NL-02 "Chỉ chủ hồ sơ mới được nộp lại"). Vướng: TVV TU_CHOI có taiKhoanId=null per FR-IV-03 line 348, không thể login làm "chủ hồ sơ". Cần BA clarify actor: (a) public portal anonymous + CCCD validation; (b) NHT proxy; (c) auto-issue account khi TU_CHOI. [r27-retry005-nop-lai-endpoint-built.png](../../bug-reports/tu-van-vien-cg/img/r27-retry005-nop-lai-endpoint-built.png)
> - **Sample regression PASS:** TVV-001 (10 tab list + 8 record HOAT_DONG + pagination 20/trang) — không regression sau dev wave 4. [r27-tvv001-regression-pass.png](evidence-r7-7-2/r27-tvv001-regression-pass.png)

> **R7.7.2 R26 re-verify dev fix wave 3 (2026-05-10 12:25:00):** dev báo đã fix RETRY-004/005/007 sau R25; verify lại qua API browser (cb_nv_tw_02 + isolatedContext qa_r25_verify) + sample UI regression cho 2 TC closed.
> - **TVV-022 nhánh có VV** giữ ⚠️ Sai spec: BUG-RETRY-004 lặp pattern lần 4 — DELETE TVV-0001 (Lý Thị Mười Ba, gắn VV-...20260509-006 DA_PHAN_CONG + phan-cong CHO_XAC_NHAN) → 204, hard-delete bypass BR-LEGAL-04. Dev claim fix 3 lần (R24/R25/R26) đều fail.
> - **TVV-023** giữ ❌ Lỗi: BUG-RETRY-005 — 9 POST endpoint biến thể (`/dang-ky-lai`, `/gui-lai`, `/resubmit`, `/cho-tham-dinh`, `/nop-lai`, `/submit`, `/state-transitions`, `/transitions`, `/state`) đều 404; PATCH trangThai 200 nhưng no-op (state vẫn TU_CHOI).
> - **TVV-015** giữ ❌ Lỗi: BUG-RETRY-007 — 14 GET + 1 POST = 15 path biến thể danh-gia-sau-vu-viec đều 404 (đã thử thêm `/feedback`, `/ratings`, `/danh-gia-sau-vu-viec/list`).
> - **Sample regression PASS:** TVV-001 (10 tab list + pagination) + TVV-007 (chi tiết TVV-0002 5 tab) — không regression sau dev wave 3.

> **R7.7.2 R25 re-verify dev fix wave 2 (2026-05-10 12:05:00):** dev báo đã fix toàn bộ 4 bug Open; verify lại qua UI + API browser, isolatedContext `qa_r25_verify`, account `cb_nv_tw_02` / Secret@123 / OTP 666666.
> - **TVV-007** đổi ⚠️ → ✅ Đạt: BUG-RETRY-006 Closed — chi tiết TVV-BTP-TW-0001 hiện 5 tab (Hồ sơ/Thẩm định disabled/Năng lực/Lịch sử hỗ trợ/Đánh giá), khớp SRS strict 4-5 tab. Tab "HĐ tư vấn" đã remove. [r25-retry006-tvv-detail-5tabs-fixed.png](../../bug-reports/tu-van-vien-cg/img/r25-retry006-tvv-detail-5tabs-fixed.png)
> - **TVV-022 nhánh có VV** giữ ❌ Lỗi: BUG-RETRY-004 STILL OPEN — DELETE TVV-0033 (gắn VV-...20260510-001 + phan-cong CHO_XAC_NHAN) → 204 thay vì 409. Pattern lặp 3 lần liên tiếp R23/R24/R25.
> - **TVV-023** giữ ❌ Lỗi: BUG-RETRY-005 STILL OPEN — probe 6 endpoint biến thể TU_CHOI → CHO_THAM_DINH đều 404; PATCH trangThai 200 nhưng no-op (state vẫn TU_CHOI).
> - **TVV-015** giữ ❌ Lỗi: BUG-RETRY-007 STILL OPEN — probe 9 path biến thể `/danh-gia-sau-vu-viec` đều 404. BE chưa expose endpoint entity DANH_GIA_SAU_VU_VIEC.

> **R7.7.2 R23 re-verify (2026-05-10 09:00:00):** retest toàn bộ sau dev fix wave R23. Qua UI browser MCP (login huongcg + nht_04_ui + 9999999990 + cb_nv_tw_02 + cb_pd_tw_02), không API direct làm primary.
> - **TVV-006** đổi 🚫 → ✅: BUG-CG-A1-003 Closed (R7.4.A1) + BUG-TVV-A2-002 Closed (R23) — NHT cập nhật năng lực TVV-0017 → state YCBS→DTD auto-transition (FR-IV-04 step 7).
> - **TVV-010** đổi 🚫 → ✅: cùng cơ chế TVV-006 — state transition YCBS→DTD verified.
> - **TVV-011** đổi ❌ → ✅: BUG-CG-A1-001/002 Closed (R7.4.A1 R11 walk TVV-0032 fresh MDK→HOAT_DONG full lifecycle).
> - **TVV-012** đổi ❌ → ✅: BUG-CG-77-RETRY-002 Closed (R23) — toolbar Chờ phê duyệt có `Phê duyệt hàng loạt` + `Từ chối hàng loạt` + `Bỏ chọn tất cả`.
> - **TVV-012a** đổi ❌ → ✅: BUG-CG-A1-002+003+005 Closed (R8→R22) — mail link kích hoạt port `:3000` OK + state CHO_KICH_HOAT→HOAT_DONG verified.
> - **TVV-017** đổi 🚫 → ✅: NHT chỉnh sửa hồ sơ TVV-0030 (huongcg) — PATCH `/tu-van-viens/{id}` 200, version 5→6, `dienThoai=0987654321` + `diaChi="Hà Nội R23 NHT contact update"` persisted (FR-IV-11 NHT actor — KHÔNG phải TVV/CG self per SRS line 887). [r23-tvv017-nht-contact-update-saved.png](evidence-r7-7-2/r23-tvv017-nht-contact-update-saved.png)
> - **TVV-021** đổi ❌ → ✅: BUG-CG-A1-004 Closed (R8) — Guard VO_HIEU_HOA enforce ERR-TT-02 khi TVV còn VV DANG_XU_LY.
> - **TVV-022 nhánh không VV** đổi ❌ → ✅: BUG-CG-77-RETRY-001 Closed (R23) — DELETE TVV-0008 trả 204 + record gone.
> - **TVV-022 nhánh có VV** giữ ⚠️: BUG-CG-77-RETRY-004 Partial — defect đổi 500→204 (BE bypass BR-LEGAL-04, hard-delete TVV còn VV gắn không enforce ERR-TVV-05).
> - **TVV-023** đổi 🚫 → ❌: NEW BUG-CG-77-RETRY-005 — FE Lưu form Sửa TVV state `TU_CHOI` cố call 5 endpoints transition (`/nop-lai`, `/re-submit`, `/dang-ky-lai`, `/cho-tham-dinh`, `/submit`) đều **404**. BE thiếu endpoint cho transition `TU_CHOI → CHO_THAM_DINH` (cooldown đã bỏ BA chốt 2026-05-03, workflow chưa build). [r23-tvv023-tu-choi-resubmit-404.png](evidence-r7-7-2/r23-tvv023-tu-choi-resubmit-404.png)
> - **TVV-025** đổi 🚫 → ✅: huongcg login → user-menu → "Hồ sơ cá nhân" → /profile render 2 tab (Thông tin cá nhân + Bảo mật) chỉ-đọc Tài khoản. AC FR-IV-04+11 "TVV/CG đăng nhập chuyên trang xem hồ sơ → không có nút sửa TVV record" met. [r23-tvv025-cg-profile-readonly.png](evidence-r7-7-2/r23-tvv025-cg-profile-readonly.png)
> - **TVV-028** đổi 🚫 → ✅: DN-01 (9999999990) sidebar không có menu Mạng lưới TVV. GET `/api/v1/tu-van-viens*` → 403 ERR-PERM-SYS-00-01. DN permissions list KHÔNG có `read_tu_van_vien`. [r23-tvv028-dn-403-tu-van-viens.png](evidence-r7-7-2/r23-tvv028-dn-403-tu-van-viens.png)
> - **TVV-015** giữ 🚫: DN-01 portal `/vu-viec/danh-sach` 0 record. Cần seed VV E2E (DN tạo HSVV → CB tiếp nhận → phân công TVV → TVV xử lý → DN nghiệm thu HOÀN THÀNH) → defer R8 sau khi seed pool VV HOAN_THANH có TVV gắn.
>
> **R7.7.2 R10 re-verify (2026-05-10):** qua UI browser, không API direct. TVV-016 đổi ❌ → ✅; BUG-CG-77-RETRY-003 Closed. BUG-CG-77-RETRY-002 partial fix nhưng vẫn Open vì thiếu `Từ chối hàng loạt`; BUG-CG-77-RETRY-001/004 vẫn Open.
>
> **R7.7.2 R9 re-verify (2026-05-10):** qua UI browser, không verify bằng API. TVV-001 + TVV-014 đổi ❌ → ✅; BUG-CG-77-001 + BUG-CG-77-002 Closed. Overall vẫn FAIL do các bug retry còn Open và bug cũ R7.4 vẫn ảnh hưởng một số TC.

> **R7.7.2 verify pass 4 (2026-05-08 10:10):** retry TVV-022 nhánh có VV (sau verify VV pool có 2 TVV gắn VV: TVV-0003 Ngô Thị Mười Lăm + TVV-0004 Trương Văn Mười Sáu).
> - **TVV-022 nhánh có VV** đổi 🚫 → ❌ Lỗi: click Xóa row TVV-0003 (gắn VV-BTP-TW-20260507-001 Lao động) → modal Xác nhận → click Xóa → modal đóng silent, **không toast**. Network DELETE `/api/v1/tu-van-viens/<id>` trả **HTTP 500** (không phải 409 ERR-TVV-05 theo spec BR-LEGAL-04). API GET sau action: TVV-0003 vẫn HOAT_DONG version=6 (record không bị xóa — BE đã reject thực sự nhưng wrong status code + UI silent). → **BUG-CG-77-RETRY-004 Major** (BE wrong status + FE silent — pattern cùng RETRY-001).
>
> **R7.7.2 verify pass 3 (2026-05-08 00:30):** retry 5 case ⏰ Hoãn qua UI browse only (không API direct), seed walk thẩm định → CHO_PHE_DUYET, switch session sang CB_PD_TW. Bug phát hiện log file riêng, không tự ý workaround.
> - **TVV-012** đổi ⏰ → ❌ Lỗi: tab Chờ phê duyệt cho CB_PD_TW thiếu UI batch select (no checkbox + no toolbar). Single Phê duyệt detail page hoạt động. → **BUG-CG-77-RETRY-002 Major**.
> - **TVV-014a** đổi ⏰ → ✅: batch Hủy công khai 8 record OK (toolbar appear after multi-select).
> - **TVV-014b** đổi ⏰ → ✅: batch Công khai 8 record OK happy path. Sub-case "partial fail" không simulate được (cần API mock mid-batch fail) → giữ note tách out.
> - **TVV-016** đổi ⏰ → ❌ Lỗi: empty state tab Lịch sử hỗ trợ wording sai spec ("Chưa có lịch sử hỗ trợ" thay "Tư vấn viên chưa tham gia hỗ trợ vụ việc nào"). → **BUG-CG-77-RETRY-003 Minor**.
> - **TVV-022 nhánh không VV** đổi ⏰ → ❌ Lỗi: click Xóa + confirm "Xóa" trên TVV-0008 (nhánh không VV) → no toast, sau reload record vẫn tồn tại. Functional regression UC50. → **BUG-CG-77-RETRY-001 Major**.

> **R7.7.2 verify pass 2 (2026-05-07 23:30):** retry 2 case `🤷 Không xác định` + `⚠️ Sai spec` qua NotebookLM HTPLDN + SRS local + UI fresh form.
> - **TVV-005** đổi 🤷 → ✅ Đạt: form mới hoàn toàn, để Lĩnh vực trống, click Lưu → FE chặn submit + báo "Phải chọn ít nhất 1 lĩnh vực" (2 lần). Test method cũ bị cache state nên kết luận sai.
> - **TVV-007** giữ ⚠️ Sai spec với note rõ: NotebookLM + grep SRS xác nhận SCR-IV-03 spec chi tiết chỉ define 5 tab (Hồ sơ/Thẩm định/Năng lực/Lịch sử hỗ trợ/Đánh giá), không có tab HĐ tư vấn. NHƯNG mục lục SRS v3 line 14 nói "HĐ tư vấn — KHÔNG có menu riêng — Truy cập qua tab VV/TVV" → đây là **SRS doc gap** (intent có nhưng SCR-IV-03 spec quên). UI làm đúng intent. Escalate BA bổ sung row tab HĐ TV vào SCR-IV-03.

**Bug mới R7.7.2:** BUG-CG-77-001/002 Closed R9 trong [Pass-bug-report-functional-r7-7-2-tvv.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-functional-r7-7-2-tvv.md); trong [bug-report-functional-r7-7-2-tvv-retry.md](../../bug-reports/tu-van-vien-cg/bug-report-functional-r7-7-2-tvv-retry.md): RETRY-003 Closed R10, RETRY-002 Partial/Open, RETRY-001/004 Open. **Bug cũ vẫn Open ở R7.4:** BUG-CG-A1-001/002/003/004.

## Ý nghĩa cột Status

| Ký hiệu | Nghĩa |
|---|---|
| ✅ Đạt | Test xong, kết quả khớp spec |
| ❌ Lỗi | Test xong, kết quả sai spec → có bug |
| ⚠️ Sai spec | UI/BE làm khác spec nhưng chưa rõ là bug hay spec sai → defer chờ BA |
| 🤷 Không xác định | Test không kết luận được (vd: chưa nhập đủ data, công cụ test bị giới hạn) |
| 🚫 Không test được | Có thể chạy nhưng thiếu điều kiện đầu vào (account/data/UI), nên không test được lúc này |
| ⏰ Hoãn | Test sau, cần chuẩn bị thêm bước (vd: cần thêm CB PD account, cần seed data, cần task khác xong trước) |

## Test Case Matrix

| TC | UC | Mô tả | P | Status | Lý do / Evidence |
|---|---|---|:-:|:-:|---|
| **TVV-001** | UC39 | Danh sách 6 tab + phân trang 20/trang | P0 | ✅ Đạt | **Re-verify R9 2026-05-10:** master list hiện đủ 10 tab, gồm `Từ chối` + `Vô hiệu hóa`; phân trang 20/trang ✅. **BUG-CG-77-001 Closed.** [r9 evidence](../../bug-reports/tu-van-vien-cg/evidence-r7-7-2/r9-verify-2026-05-10-cg-77-001-tabs-fixed.png) |
| **TVV-002** | UC40 | Tìm kiếm Họ tên/Mã/CCCD + filter | P0 | ✅ Đạt | Search "Mười Ba" trả 2 kết quả (BE match từng từ rời). [TVV-002-search-mui-ba.png](evidence-r7-7-2/TVV-002-search-mui-ba.png) |
| **TVV-003** | UC41 | NHT submit hồ sơ TVV → state `MOI_DANG_KY` | P0 | ✅ Đạt | Form `Thêm TVV` submit OK → tạo TVV id=83d390c7, state `MOI_DANG_KY, version: 1`. |
| **TVV-004** | UC41 | CCCD trùng → ERR-TVV-02 | P0 | ✅ Đạt | Submit CCCD trùng → FE báo "CCCD đã tồn tại trong hệ thống". [TVV-004-cccd-duplicate-error.png](evidence-r7-7-2/TVV-004-cccd-duplicate-error.png) |
| **TVV-005** | UC41 | Thiếu Lĩnh vực PL → báo lỗi | P1 | ✅ Đạt | **Verify pass 2 2026-05-07:** form `/chuyen-gia-tvv/tao-moi` mới hoàn toàn, fill 8 required field (trừ Lĩnh vực), click Lưu → FE chặn submit + render error "Phải chọn ít nhất 1 lĩnh vực" 2 lần. URL stuck `/tao-moi` không navigate. [TVV-005-retest-fresh-form-validate-ok.png](evidence-r7-7-2/TVV-005-retest-fresh-form-validate-ok.png) |
| **TVV-006** | UC42 | NHT cập nhật năng lực TVV (FR-IV-04 — actor NHT, KHÔNG phải TVV/CG) | P1 | ✅ Đạt | **R23 2026-05-10:** BUG-CG-A1-003 Closed (R8) + BUG-TVV-A2-002 Closed (R23) — NHT cập nhật năng lực TVV YEU_CAU_BO_SUNG → state tự transition DANG_THAM_DINH (FR-IV-04 step 7). Walk verified [workflow-test-report-r7-4-a2.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a2.md) A2.2. SRS line 408 actor = NHT (test plan TC title cũ "TVV/CG cập nhật" miscategorized — đã sửa actor). |
| **TVV-007** | UC43 | Chi tiết 5 tab | P0 | ✅ Đạt | **R25 2026-05-10 12:05:00:** BUG-CG-77-RETRY-006 Closed — UI giảm 6 → 5 tab (Hồ sơ/Thẩm định disabled/Năng lực/Lịch sử hỗ trợ/Đánh giá), khớp SCR-IV-03 component spec strict 5 tab cho CB NV. Tab "HĐ tư vấn" đã remove. [r25-retry006-tvv-detail-5tabs-fixed.png](../../bug-reports/tu-van-vien-cg/img/r25-retry006-tvv-detail-5tabs-fixed.png) |
| **TVV-008** | UC44 | Thẩm định 4 nhóm tiêu chí | P0 | ✅ Đạt | Đã test ở R7.4.A1-CG TC-CG-A1-02. POST `/tham-dinh` body 4 nhóm BE accept. |
| **TVV-008b** | UC44 | Thẩm định KHÔNG ĐẠT → TU_CHOI | P1 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.B (TVV-0011/0012 → TU_CHOI). |
| **TVV-009** | UC44 | Thẩm định → YEU_CAU_BO_SUNG | P0 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.C (TVV-0010 → YEU_CAU_BO_SUNG). |
| **TVV-010** | UC44 | Bổ sung xong → quay lại thẩm định | P1 | ✅ Đạt | **R23 2026-05-10:** BUG-TVV-A2-002 Closed (R23) — NHT cập nhật năng lực FR-IV-04 step 7 trigger auto-transition `YEU_CAU_BO_SUNG → DANG_THAM_DINH`. Walk verified [workflow-test-report-r7-4-a2.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a2.md) A2.2 R23. |
| **TVV-011** | UC45 | Phê duyệt → CHO_KICH_HOAT | P0 | ✅ Đạt | **R23 2026-05-10:** BUG-CG-A1-001+002 Closed (R8/R11) — R7.4.A1 R11 walk fresh TVV-0032 lifecycle MDK→HOAT_DONG full PASS, state đúng `CHO_KICH_HOAT` sau phê duyệt + auto-issue tài khoản + mail fire OK. Walk: [workflow-test-report-r7-4-a1.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a1.md). |
| **TVV-012** | UC45 | Phê duyệt hàng loạt | P1 | ✅ Đạt | **R23 2026-05-10:** BUG-CG-77-RETRY-002 Closed — tab Chờ phê duyệt của `cb_pd_tw_02` chọn 1 record TVV-0046 hiện đủ 3 nút toolbar `Phê duyệt hàng loạt` + `Từ chối hàng loạt` + `Bỏ chọn tất cả`. [r23-retry002-batch-toolbar-tu-choi-fixed.png](../../bug-reports/tu-van-vien-cg/img/r23-retry002-batch-toolbar-tu-choi-fixed.png) |
| **TVV-012a** | UC45 | Bấm link mail kích hoạt → HOAT_DONG | P0 | ✅ Đạt | **R23 2026-05-10:** BUG-CG-A1-002+003+005 Closed (R8/R11/R22) — R11 walk TVV-0032 + R22 walk TVV-0036 đều PASS. Mail body chứa link `http://103.172.236.130:3000/auth/first-login-password?token=...` reachable, TVV đặt MK lần đầu → state `HOAT_DONG` verified. Walk: [workflow-test-report-r7-4-a1.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a1.md). |
| **TVV-013** | UC45 | Từ chối → bắt buộc lý do ≥10 ký tự | P0 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.B. |
| **TVV-014** | UC46 | Modal Công khai 5 fields | P1 | ✅ Đạt | **Re-verify R9 2026-05-10:** modal có `Mô tả công khai` bắt buộc, counter `0 / 5000`, upload tệp tùy chọn, giới hạn 10 tệp và 20MB/tệp. **BUG-CG-77-002 Closed.** [r9 evidence](../../bug-reports/tu-van-vien-cg/evidence-r7-7-2/r9-verify-2026-05-10-cg-77-002-modal-fixed.png) |
| **TVV-014a** | UC46 | Hủy công khai | P1 | ✅ Đạt | **Verify pass 3 2026-05-08:** tab Đang hoạt động → Select all 8 TVV → toolbar appear → click "Hủy công khai" → batch OK, toast Success, 8 record state "Chưa công khai". **R9 2026-05-10:** form MD-CONG-KHAI đã build, BUG-CG-77-002 Closed. [TVV-014a-batch-huy-cong-khai-success.png](evidence-r7-7-2/TVV-014a-batch-huy-cong-khai-success.png) |
| **TVV-014b** | UC46 | Công khai hàng loạt — happy path | P2 | ✅ Đạt | **Verify pass 3 2026-05-08:** tab Đang hoạt động → Select all 8 TVV → toolbar "Công khai lên Cổng PLQG" → batch OK, 8 record state "Đã công khai". Sub-case "partial fail mid-batch" không simulate được qua UI (cần API mock) → tách defer test infrastructure. [TVV-014b-batch-cong-khai-success.png](evidence-r7-7-2/TVV-014b-batch-cong-khai-success.png) |
| **TVV-015** | UC47 | DN đánh giá TVV sau VV (thang 1.0-5.0) | P1 | ✅ Đạt | **R27 2026-05-10 18:35:00:** BUG-CG-77-RETRY-007 Closed — endpoint `GET/POST /tu-van-viens/{id}/danh-gia` + alias `POST /vu-viecs/{vvId}/danh-gia-tvv` build R27. Insert 2 record DANH_GIA_SAU_VU_VIEC → meta avgChuyenMon=4.5, avgThaiDo=5, avgDungHan=4, diemTb=4.5, tongSoDanhGia=2. TVV detail `diemDanhGiaTb=4.5, soLuongDanhGia=2` — BR-CALC-06 trigger working. [r27-retry007-danh-gia-endpoint-fixed.png](../../bug-reports/tu-van-vien-cg/img/r27-retry007-danh-gia-endpoint-fixed.png) |
| **TVV-016** | UC48 | Xem lịch sử hỗ trợ TVV | P2 | ✅ Đạt | **Re-verify R10 2026-05-10:** detail TVV-0008 tab Lịch sử hỗ trợ hiện đúng wording `Tư vấn viên chưa tham gia hỗ trợ vụ việc nào`; **BUG-CG-77-RETRY-003 Closed**. [r10 evidence](../../bug-reports/tu-van-vien-cg/evidence-r7-7-2/r10-verify-2026-05-10-cg-77-retry-003-current.png) |
| **TVV-017** | UC49 | NHT cập nhật contact info TVV (FR-IV-11 — actor NHT, KHÔNG phải TVV/CG) | P1 | ✅ Đạt | **R23 2026-05-10:** SRS line 887 actor = NHT. `nht_04_ui` mở /chuyen-gia-tvv/{id}/chinh-sua TVV-0030 huongcg → cập nhật `dienThoai="0987654321"` + `diaChi="Hà Nội R23 NHT contact update"` → click Lưu → PATCH `/api/v1/tu-van-viens/{id}` reqid=219 trả 200, version 5→6 verified GET. CG huongcg tự /profile chỉ có 2 tab readonly TAI_KHOAN, không có nút sửa TVV record (AC met). [r23-tvv017-nht-contact-update-saved.png](evidence-r7-7-2/r23-tvv017-nht-contact-update-saved.png) |
| **TVV-018** | UC50 | Tạm dừng HOAT_DONG → TAM_DUNG | P1 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.D. |
| **TVV-019** | UC50 | Kích hoạt lại TAM_DUNG → HOAT_DONG | P1 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.D. |
| **TVV-019b** | UC50 | Khôi phục VO_HIEU_HOA → HOAT_DONG | P2 | ✅ Đạt | TVV-0003 (Ngô Thị Mười Lăm) sau khi vô hiệu hóa, click `Cập nhật trạng thái` → drawer chỉ option "Đang hoạt động". Submit lý do ≥10 ký tự → state `HOAT_DONG, version: 6` ✅. (Nhãn UI "Đang hoạt động" thay vì "Hoạt động" — liên quan BUG-CG-A1-001.) [TVV-019b-vo-hieu-hoa-khoi-phuc.png](evidence-r7-7-2/TVV-019b-vo-hieu-hoa-khoi-phuc.png) |
| **TVV-020** | UC50 | Vô hiệu hóa khi không có VV | P0 | ✅ Đạt | Đã test ở R7.4.A1 walk A1.D. |
| **TVV-021** | UC50 | Vô hiệu hóa khi có VV → phải bị chặn | P0 | ✅ Đạt | **R23 2026-05-10:** BUG-CG-A1-004 Closed (R8) — Guard VO_HIEU_HOA enforce ERR-TT-02. Walk verified [workflow-test-report-r7-4-a1.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a1.md) A1.D. |
| **TVV-022** | UC50 | Xóa cứng TVV (chỉ khi không có VV) | P1 | ✅ Đạt | **R27 2026-05-10 18:35:00:** **Nhánh không VV** ✅ — BUG-CG-77-RETRY-001 Closed (R23). **Nhánh có VV** ✅ — BUG-CG-77-RETRY-004 Closed: DELETE TVV-BTP-TW-0004 (gắn VV-...20260507-002 phan-cong CHO_XAC_NHAN) → **409 ERR-TVV-05** "Không thể xóa: TVV còn vụ việc đang xử lý"; state sau = HOAT_DONG (không hard-delete). BR-LEGAL-04 enforced sau 4 lần verify R23-R26. [r27-retry004-tvv0004-409-fixed.png](../../bug-reports/tu-van-vien-cg/img/r27-retry004-tvv0004-409-fixed.png) |
| **TVV-023** | — | Nộp lại sau TU_CHOI (KHÔNG cooldown) | P2 | ⚠️ Sai spec | **R30 2026-05-11 02:58:00:** BUG-CG-77-RETRY-005 **STILL OPEN — BE 2 permission rule sai khác nhau cho 2 role** (lấp data gap R28). Seed mới `nht_btp_tw_audit_r30` (NHT BTP-TW cùng đơn vị TVV-BTP-TW-0011) → POST `/nop-lai`: NHT → 403 ERR-PERM-SYS-00-01 generic; CB_NV_TW → 403 ERR-PERM-IV-NL-02 "Chỉ chủ hồ sơ". Phát hiện mới: TVV TU_CHOI có `taiKhoanId=null` (FR-IV-03:348) → rule "chủ hồ sơ" deadlock không actor nào pass được. Cần BE rework + BA fix SRS. [r30-retry005-nht-cung-donvi-403.png](../../bug-reports/tu-van-vien-cg/img/r30-retry005-nht-cung-donvi-403.png) + [r28-retry005-nht-cross-donvi-403.png](../../bug-reports/tu-van-vien-cg/img/r28-retry005-nht-cross-donvi-403.png) + [r28-retry005-cb-luu-noresult.png](../../bug-reports/tu-van-vien-cg/img/r28-retry005-cb-luu-noresult.png) |
| **TVV-024** | — | QTHT chỉ xem, KHÔNG sửa/xóa TVV | P1 | ✅ Đạt | Đã test ở R7.4.A1 + memory `qa_htpldn_qtht_permission_bypass` — bypass đã closed R6. |
| **TVV-025** | — | TVV/CG xem hồ sơ của mình | P0 | ✅ Đạt | **R23 2026-05-10:** `huongcg` (CG) login OK → user-menu → "Hồ sơ cá nhân" → /profile render 2 tab (Thông tin cá nhân + Bảo mật). Form chỉ-đọc TAI_KHOAN với readOnly Tên đăng nhập + Email + Vai trò; KHÔNG có nút "Sửa TVV record". GET `/api/v1/tu-van-viens/me` 403 (CG read own TVV chỉ qua /profile UI). AC FR-IV-04+11 "TVV/CG đăng nhập chuyên trang xem hồ sơ → không có nút sửa" met. [r23-tvv025-cg-profile-readonly.png](evidence-r7-7-2/r23-tvv025-cg-profile-readonly.png) |
| **TVV-026** | — | CB NV TW thấy toàn quốc; ĐP chỉ thấy đơn vị mình | P0 | ✅ Đạt | Đã test ở R7.4.A1-CG TC-11 — `cb_nv_dp_02` GET TVV TW → 403. |
| **TVV-027** | — | CB PD chỉ phê duyệt cùng cấp | P0 | ✅ Đạt | Đã test ở R7.4.A1-CG TC-10 — `cb_pd_dp_02` POST `/phe-duyet` TVV TW → 403. |
| **TVV-028** | — | DN không thấy TU_VAN_VIEN backend | P1 | ✅ Đạt | **R23 2026-05-10:** DN-01 `9999999990` login OK → /dashboard. Sidebar 5 nhóm (Tổng quan + Quản lý đào tạo + Quản lý vụ việc + Quản lý chi trả + Quản lý DN), KHÔNG có "Mạng lưới TVV"/"Tư vấn viên". GET `/api/v1/tu-van-viens?page=0&size=10` → 403 ERR-PERM-SYS-00-01; GET `/api/v1/tu-van-viens/{id}` → 403; GET `/api/v1/tu-van-viens` → 403. DN.permissions list không có `read_tu_van_vien`. [r23-tvv028-dn-403-tu-van-viens.png](evidence-r7-7-2/r23-tvv028-dn-403-tu-van-viens.png) |

## Bugs phát hiện ở R7.7.2

9 bug — trạng thái sau R30:
- [Pass-bug-report-functional-r7-7-2-tvv.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-functional-r7-7-2-tvv.md): BUG-CG-77-001 + BUG-CG-77-002 — ✅ Closed R9.
- [bug-report-functional-r7-7-2-tvv-retry.md](../../bug-reports/tu-van-vien-cg/bug-report-functional-r7-7-2-tvv-retry.md): BUG-CG-77-RETRY-001 ✅ Closed R23; BUG-CG-77-RETRY-002 ✅ Closed R23; BUG-CG-77-RETRY-003 ✅ Closed R10; **BUG-CG-77-RETRY-004 ✅ Closed R27** (DELETE → 409 ERR-TVV-05); **BUG-CG-77-RETRY-005 🔴 Open R30** (R30 NHT cùng đơn vị + CB role đều fail với 2 permission rule sai khác nhau; TVV TU_CHOI `taiKhoanId=null` → rule "chủ hồ sơ" deadlock); BUG-CG-77-RETRY-006 ✅ Closed R25; **BUG-CG-77-RETRY-007 ✅ Closed R27** (endpoint danh-gia + BR-CALC-06 trigger working). 8/9 đóng, 1 Open cần BE rework + BA fix SRS.

5 bug R7.4 đã Closed: [Pass-bug-report-flow-r7-4-a1-tvv.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a1-tvv.md) (5/5 Closed R8→R22) + [Pass-bug-report-flow-r7-4-a1-cg-state.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a1-cg-state.md) (1/1 Closed R8b) + [Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md](../../bug-reports/tu-van-vien-cg/Pass-bug-report-flow-r7-4-a2-nht-permission-gap.md) (3/3 Closed R23).

## Tóm tắt R28: case còn ⚠️ vì sao?

Nhóm theo nguyên nhân để dev/BA dễ unblock:

| Nguyên nhân | Số TC | TC list | Cần làm gì để test? |
|---|:-:|---|---|
| **BE design sai 2 chỗ + SRS contradiction** (BUG-RETRY-005 Open R28) | 1 | TVV-023 | (1) Dev BE đổi permission rule `/nop-lai` từ "chủ hồ sơ" sang "NHT cùng đơn vị" per SCR-IV-02 line 1462 + BR-AUTH-08; (2) Dev BE bỏ endpoint `/nop-lai` riêng → dùng PATCH `/api/v1/tu-van-viens/{id}` save-trigger pattern (giống `YEU_CAU_BO_SUNG → DANG_THAM_DINH` line 1571 + 2308); (3) BA fix SRS line 2314 SM-TVV mâu thuẫn line 1462 SCR-IV-02 + line 366 FR-IV-04 (chọn 1 actor đúng). Sau 3 fix QA seed NHT BTP-TW + verify e2e UI walk. |
| **TVV-014b sub-case partial fail** | 1 | TVV-014b sub-case | Cần API mock simulate fail giữa batch để test rollback per-item — defer test infrastructure. |

## Out of scope (defer)

- **TVV-014b partial fail simulation** → đợi test infrastructure (API mock mid-batch fail).

## Files / Evidence

- 6 screenshot ở `evidence-r7-7-2/`
- API responses captured live
- Reference reports: [workflow-test-report-r7-4-a1.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a1.md), [workflow-test-report-r7-4-a1-cg.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a1-cg.md), [workflow-test-report-r7-4-a2.md](../../workflow/tu-van-vien-cg/workflow-test-report-r7-4-a2.md)
