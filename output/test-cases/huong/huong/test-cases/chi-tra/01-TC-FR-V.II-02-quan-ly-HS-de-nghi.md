# TC — FR-V.II-02 + FR-V.II-06: Quản lý DS HS Chi trả + Tiếp nhận + DN rút HS

> **UC ref**: UC69 + UC73 (gộp DS HS đề nghị + DS HS đề nghị TT) | **Screen**: SCR-V.II-01 | **SRS**: srs-fr-06:143-231 + 434-465 + 894-952
> **Roles**: CB_NV (TW/BN/DP) primary, CB_PD (TW/BN/DP) read-only, DN (rút HS qua chuyên trang/DVC)
> **Mục tiêu**: Verify DS 5 tab + filter (trạng thái/quy mô/range ngày) + phân trang + action context-sensitive theo trạng thái + transition CHO_TIEP_NHAN → DANG_KIEM_TRA (Tiếp nhận) + CHO_TIEP_NHAN → HUY (DN rút).

## Preconditions

- Hệ thống có ≥ 5 HS Chi trả ở mỗi state (CHO_TIEP_NHAN, DANG_KIEM_TRA, YEU_CAU_BO_SUNG, DANG_DANH_GIA, DANG_THAM_DINH, CHO_PHE_DUYET, DA_DUYET, DA_THANH_TOAN, TU_CHOI, HUY) — env hiện có ~70 HSCT 8 state (memory `fr06_chi_tra_r7e3_finding.md`)
- DN đã có HS CHO_TIEP_NHAN qua DVC để test rút HS
- Đăng nhập role `cb_nv_tw_01` (mặc định scope toàn quốc) hoặc `cb_nv_dp_01` (scope AG) tùy TC

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-LIST-001 | Login `cb_nv_tw_01` | 1. Vào /chi-tra/danh-sach 2. Verify 5 tab + count 3. Verify 9 cột | DS hiện đầy đủ 5 tab "Tất cả / Chờ xử lý (CHO_TIEP_NHAN+DANG_KIEM_TRA+YEU_CAU_BO_SUNG) / Đang đánh giá (DANG_DANH_GIA+DANG_THAM_DINH) / Chờ PD (CHO_PHE_DUYET) / Đã xử lý (DA_DUYET+DA_THANH_TOAN+TU_CHOI+HUY)". 9 cột (Mã HS / Tên DN / Quy mô / Số tiền đề nghị / Số tiền duyệt / Trạng thái / SLA / Ngày nộp / Hành động). Mặc định 20 dòng/trang | AC#1, BR-DATA-07 | P0 |
| TC-CT-LIST-002 | Login `cb_nv_tw_01` | 1. Click tab "Chờ xử lý" 2. Verify count tab vs số dòng | Tab filter đúng 3 trạng thái CHO_TIEP_NHAN+DANG_KIEM_TRA+YEU_CAU_BO_SUNG. Số đếm tab = số dòng | AC#1 | P0 |
| TC-CT-LIST-003 | Login `cb_nv_tw_01` | 1. Filter "Quy mô DN" = "Siêu nhỏ" 2. Filter "Trạng thái" = "Đang kiểm tra" 3. Range ngày 01/01/2026 - 31/12/2026 4. Click "Tìm kiếm" | DS lọc AND logic — chỉ HS quy mô SIEU_NHO + trạng thái DANG_KIEM_TRA + ngày nộp trong range. Combobox quy mô hiển thị nhãn Việt "Siêu nhỏ/Nhỏ/Vừa" (giá trị nội bộ SIEU_NHO/NHO/VUA — srs-fr-06:916) | AC#3 | P1 |
| TC-CT-LIST-004 | Login `cb_nv_tw_01` | 1. Nhập keyword "test_DN" trong ô tìm kiếm 2. Click Tìm kiếm | DS filter theo tên DN OR mã HS chứa keyword | AC#3 | P1 |
| TC-CT-LIST-005 | Login `cb_nv_tw_01` + > 21 HS | 1. Vào DS 2. Verify pagination 3. Click trang 2 | 20 dòng/trang. Pagination hiển thị 20 default. Click trang 2 → lấy dòng 21+ | BR-DATA-07 | P1 |
| TC-CT-LIST-006 | Login `cb_nv_dp_01` (AG) | 1. Vào /chi-tra/danh-sach | DS chỉ hiện HS thuộc đơn vị AG (BR-AUTH-08 multi-tenant scoping). KHÔNG thấy HS BG/BNI. cb_nv_tw_01 thấy toàn quốc | BR-AUTH-08, AC#1 | P0 |
| TC-CT-LIST-007 | Login `cb_nv_tw_01` + HS X ở CHO_TIEP_NHAN | 1. Click hàng HS X 2. Verify nút Hành động hiện | Cột Hành động hiện nút "Tiếp nhận" cho HS CHO_TIEP_NHAN. Click → mở SCR-V.II-02 chi tiết tại section tương ứng | AC#1, srs-fr-06:928 | P0 |
| TC-CT-TIEP-NHAN-001 | Login `cb_nv_tw_01` + HS X CHO_TIEP_NHAN cùng đơn vị TW | 1. Vào /chi-tra/:id của X 2. Click "Tiếp nhận" | HS X chuyển CHO_TIEP_NHAN → DANG_KIEM_TRA. Field `ngay_tiep_nhan = NOW()`, `nguoi_tiep_nhan_id = cb_nv_tw_01.id`. AUDIT_LOG ghi hành động='TIEP_NHAN'. Stepper bước [Tiếp nhận] highlight done. Toast success. | SM-CHITRA, BR-DATA-05, srs-fr-06:196-204 | P0 |
| TC-CT-TIEP-NHAN-002 | Login `cb_nv_tw_01` + HS X DANG_KIEM_TRA (đã tiếp nhận) | 1. Vào /chi-tra/:id của X 2. Tìm nút Tiếp nhận | Nút Tiếp nhận KHÔNG hiện (state guard). Nếu force gọi API → ERR-CT-TN-01 "Hồ sơ không ở trạng thái chờ tiếp nhận" | ERR-CT-TN-01, srs-fr-06:221 | P0 |
| TC-CT-TIEP-NHAN-003 | Login `cb_nv_dp_01` (AG) + HS Y CHO_TIEP_NHAN của BG | 1. Force vào /chi-tra/:id của Y | 403 Forbidden hoặc 404 Not Found (BR-AUTH-08 scope). KHÔNG cho phép tiếp nhận xuyên đơn vị | BR-AUTH-08 | P0 |
| TC-CT-RUT-001 | Login `dn_01` (DN AG) qua chuyên trang + HS Z CHO_TIEP_NHAN của dn_01 | 1. Vào trang HS của tôi 2. Click HS Z 3. Click "Rút hồ sơ" 4. Confirm modal | HS Z chuyển CHO_TIEP_NHAN → HUY. Field `ly_do_huy = "DN_RUT_HO_SO"`. CB NV (nếu đã gán) nhận TB "Doanh nghiệp đã rút hồ sơ". AUDIT_LOG ghi hành động='RUT_HO_SO'. | SM-CHITRA, BR-NOTIF-01, srs-fr-06:206-214 | P0 |
| TC-CT-RUT-002 | Login `dn_01` + HS Z DANG_KIEM_TRA (đã tiếp nhận) | 1. Vào HS của tôi 2. Tìm nút Rút hồ sơ | Nút "Rút hồ sơ" KHÔNG hiện. Nếu force API → ERR-CT-RUT-01 "Chỉ được rút hồ sơ khi chưa tiếp nhận" | ERR-CT-RUT-01, srs-fr-06:222 | P0 |
| TC-CT-RUT-003 | Login `dn_01` + HS W CHO_TIEP_NHAN của dn_02 | 1. Force GET /chi-tra/:id của W | 403/404. dn_01 KHÔNG xem hoặc rút HS dn_02 (scope DN) | BR-AUTH-08 | P0 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-LIST-008 | Login `cb_nv_tw_01` | 1. Filter `tu_ngay = 31/12/2026`, `den_ngay = 01/01/2026` (đảo ngược) | Validation error "Từ ngày phải ≤ Đến ngày" — KHÔNG submit. Hoặc trả về empty với cảnh báo | AC#3 (range guard) | P1 |
| TC-CT-LIST-009 | Login `cb_nv_tw_01` + > 100 HS | 1. Vào DS 2. Click cột "Số tiền đề nghị" sort DESC 3. Chuyển trang 2 | DS sort theo `so_tien_de_nghi` DESC. Pagination giữ sort khi chuyển trang. Nếu cap mặc định 20/trang → đảm bảo trang 2 lấy đúng 20 dòng kế (offset=20) | BR-DATA-07 | P1 |
| TC-CT-LIST-010 | 2 CB NV cùng cấp đăng nhập (cb_nv_tw_01 + cb_nv_tw_02) cùng HS X CHO_TIEP_NHAN | 1. Cả hai vào /chi-tra/:id 2. Cả hai click "Tiếp nhận" gần đồng thời | Một thắng (HS → DANG_KIEM_TRA, `nguoi_tiep_nhan_id` của user đầu tiên). User thứ 2 nhận ERR-CT-TN-01 + toast "Hồ sơ đã được tiếp nhận" — race condition handled (optimistic lock hoặc state check backend) | ERR-CT-TN-01, BR-EC-01 (Optimistic Locking) | P1 |
| TC-CT-LIST-011 | Login `cb_nv_tw_01` | 1. Click "Xuất Excel" toolbar | File .xlsx download. Nội dung khớp DS đang filter (cùng filter trạng thái/quy mô/range ngày) | srs-fr-06:912 | P1 |
| TC-CT-RUT-004 | Login `dn_01`, HS Z CHO_TIEP_NHAN | 1. Click "Rút hồ sơ" 2. Modal confirm 3. Click "Hủy" (cancel modal) | Modal đóng. HS Z giữ nguyên CHO_TIEP_NHAN. KHÔNG có audit log của hành động RUT_HO_SO | srs-fr-06:211 (xác nhận lại) | P1 |
| TC-CT-LIST-012 (A6 fill GAP-A5-01) | Login `cb_nv_tw_01` | 1. Vào /chi-tra/danh-sach 2. Nhập keyword "không-tồn-tại-zzzzz" 3. Click "Tìm kiếm" | DS empty với INF-CT-01 "Không tìm thấy hồ sơ phù hợp" hiển thị placeholder. KHÔNG crash | INF-CT-01, srs-fr-06:220 | P1 |

## Tổng số TC: 19 (A4 +5 edge, A6 +1 fill GAP-A5-01)

**P0: 10** | P1: 9

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-01)
