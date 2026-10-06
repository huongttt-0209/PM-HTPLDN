# Test Cases — UC51 + UC58: Quản lý DS Hồ sơ Vụ việc + Tìm kiếm (FR-V.I-01 + FR-V.I-08)

> **SRS Ref**: FR-V.I-01 (srs-fr-05:80-148), FR-V.I-08 (srs-fr-05:627-689), SCR-V.I-01 (srs-fr-05:1652-1692)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06 · **Codex review 2026-05-09**: +4 TC (107/206/308/310) cover gap tab filter + UC58 empty + batch delete + sort cột khác
> **Tài khoản chính**: `cb_nv_tw_01` (toàn quốc TW), `cb_nv_tw_02` (CB NV TW khác — multi-user concurrent)
> **A7 note**: TC list gốc 18 → giữ 16 sau A7 (loại 2 TC verify DB query thuần — chuyển sang verify network).

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DS-UI-01 | FR-V.I-01 / SCR-V.I-01 | Verify layout SCR-V.I-01: 6 tab + filter-bar 7 control + table 11 cột + batch action-bar + pagination | `cb_nv_tw_01`. Login → vào "Quản lý Vụ việc". | — | 1. Quan sát breadcrumb. 2. Quan sát toolbar 4 nút. 3. Quan sát 6 tab. 4. Quan sát filter-bar 7 control. 5. Quan sát table header. 6. Click 1 checkbox dòng. 7. Quan sát action-bar. 8. Quan sát pagination. | **UI**: (1) Breadcrumb "Trang chủ > Vụ việc > Danh sách hồ sơ" (srs-fr-05:1662). (2) Toolbar: tiêu đề "Quản lý Vụ việc HTPL" + 4 nút [+ Thêm mới] [+ Nhập thủ công] [Xuất Excel] [Làm mới] (srs-fr-05:1663). (3) 6 tab trạng thái với count realtime: Tất cả / Chờ tiếp nhận / Đang xử lý / Chờ PD / Hoàn thành / Từ chối (srs-fr-05:1664). (4) Filter-bar 7 control: Ô tìm kiếm + Lĩnh vực + Trạng thái (12 option) + Kênh (5 option) + Mức SLA (4 option BINH_THUONG/SAP_HET/QUA_HAN/QUA_HAN_NGHIEM_TRONG — **theo SCR-V.I-01:1669, lưu ý SPEC-CLARIFY-VV-DS-03**) + Date range + nút Tìm/Xóa (srs-fr-05:1665-1671). (5) Table header **11 cột** (rows 11-21 SRS): checkbox + Mã VV + Tên DN + Lĩnh vực + Kênh + Trạng thái + Người xử lý/Tổ chức + Ngày tiếp nhận + Deadline SLA + Cảnh báo SLA + Hành động (srs-fr-05:1672-1682). (6) Sau check 1 dòng → action-bar hiện "[Trình PD hàng loạt] [Xóa hàng loạt]" (srs-fr-05:1683). (7) Pagination "Hiển thị 1-20 / N kết quả" (srs-fr-05:1684). | Happy | P1 |
| TC-VV-DS-UI-02 | FR-V.I-01 / SCR-V.I-01 cột 17 | Verify cột "Người xử lý / Tổ chức" hiển thị đúng cho 3 case: chưa phân công / cá nhân / tổ chức | `cb_nv_tw_01`. Có 3 VV: VV1 chưa phân công, VV2 phân công CA_NHAN (TVV `tvv_01`), VV3 phân công TO_CHUC (TC `TO-AG-01` cử `tvv_02`). | — | 1. Quan sát cột 17 "Người xử lý / Tổ chức" cho 3 VV. | **UI**: VV1 hiển thị "—" (chưa phân công). VV2 hiển thị "Tư vấn viên 01 (AG)" (TAI_KHOAN.ho_ten của TVV cá nhân). VV3 hiển thị tên tổ chức (TO_CHUC_TU_VAN.ten_to_chuc) + tooltip hover hiện "TVV xử lý: Tư vấn viên 02 (BG)" (srs-fr-05:1678). Cell width 150px, text cắt > 30 ký tự + tooltip (srs-fr-05:1596). | Happy | P1 |
| TC-VV-DS-UI-03 | FR-V.I-01 / SCR-V.I-01 cột 20 | Verify cột "Cảnh báo SLA" 4 mức màu badge | `cb_nv_tw_01`. Có 4 VV mỗi muc_do_canh_bao 1 record (BINH_THUONG/SAP_HET/QUA_HAN/QUA_HAN_NGHIEM_TRONG). | — | 1. Quan sát cột 20 cho 4 VV. | **UI**: 🟢 BINH_THUONG xanh lá (>50% còn lại) / 🟡 SAP_HET vàng (≤50%) / 🔴 QUA_HAN đỏ (>100%) / ⚫ QUA_HAN_NGHIEM_TRONG đen (>200%) (srs-fr-05:1681 + BR-SLA-02 srs-fr-05:2457). Cell width 80px, badge có icon + text. | Happy | P0 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DS-101 | FR-V.I-01 AC1 | Hiển thị DS VV phân quyền theo đơn vị (CB NV TW xem toàn quốc) | `cb_nv_tw_01`. ≥20 VV thuộc nhiều đơn vị (TW + BN + DP). | — | 1. Login `cb_nv_tw_01`. 2. Vào DS VV. | **STATE**: Backend filter `WHERE is_deleted=0` (BR-DATA-02). CB NV TW không filter don_vi_id (toàn quốc, BR-AUTH-03/04 srs-fr-05:2469). **UI**: Bảng hiển thị tất cả VV (≥20). Pagination "1-20 / N". Badge trạng thái 12 màu theo srs-fr-05:1531-1546. **PERSIST**: AUDIT_LOG SELECT (read action — verify gián tiếp qua `list_network_requests` GET /vu-viec). | Happy | P0 |
| TC-VV-DS-102 | FR-V.I-01 / SCR-V.I-01 tab | Tab "Đang xử lý" filter trạng thái DA_TIEP_NHAN..DANG_XU_LY | `cb_nv_tw_01`. ≥3 VV mỗi state. | — | 1. Click tab "Đang xử lý". | **STATE**: Backend filter `trang_thai IN ('DA_TIEP_NHAN','DANG_KIEM_TRA','YEU_CAU_BO_SUNG','DA_PHAN_CONG','DANG_XU_LY')` (srs-fr-05:1664). **UI**: Bảng chỉ hiện VV trong 5 state này. Tab badge số count realtime cập nhật. **PERSIST**: — | Happy | P0 |
| TC-VV-DS-103 | FR-V.I-01 AC3 / BR-DATA-07 | Pagination 20/trang default + chuyển trang | `cb_nv_tw_01`. ≥45 VV. | — | 1. Quan sát "Hiển thị 1-20 / 45". 2. Click trang 2. 3. Click trang 3. | **STATE**: Backend `LIMIT 20 OFFSET (page-1)*20` (BR-DATA-07 srs-fr-05:2427). **UI**: Trang 1: 20 dòng. Trang 2: 20 dòng. Trang 3: 5 dòng. Pagination cập nhật "21-40", "41-45". **PERSIST**: — | Happy | P0 |
| TC-VV-DS-104 | FR-V.I-01 AC2 | Click vào dòng VV → mở SCR-V.I-03 chi tiết | `cb_nv_tw_01`. Có VV đang DANG_XU_LY. | — | 1. Click vào "Mã VV" (text link). | **STATE**: Backend GET /vu-viec/{id}. **UI**: Chuyển sang SCR-V.I-03. URL `/vu-viec/{id}`. Hiển thị Stepper + 8 Accordion + Timeline. **PERSIST**: AUDIT_LOG VIEW (verify network GET). | Happy | P0 |
| TC-VV-DS-105 | FR-V.I-01 / SCR-V.I-01 sort | Sort theo cột "Ngày tiếp nhận" DESC/ASC | `cb_nv_tw_01`. ≥10 VV. | — | 1. Click header "Ngày tiếp nhận". 2. Click lại. | **STATE**: Backend `ORDER BY ngay_tiep_nhan DESC/ASC`. **UI**: Mặc định sort `updated_at DESC` (srs-fr-05:1690). Click lần 1 → sort ngày DESC, biểu tượng ▼. Click lần 2 → ASC, biểu tượng ▲. **PERSIST**: — | Happy | P1 |
| TC-VV-DS-106 | FR-V.I-01 toolbar export | Xuất Excel danh sách VV (max 10,000 rows BR-DATA-06) | `cb_nv_tw_01`. Filter "Trạng thái = HOAN_THANH". | — | 1. Filter trạng thái HOAN_THANH. 2. Click [Xuất Excel]. | **STATE**: Backend stream Excel với cùng filter context (BR-DATA-06 srs-v3 max 10K rows). **UI**: Browser download `vu-viec-DS-{YYYYMMDD-HHmm}.xlsx`. Mở file → cột tương ứng table CMS, không chứa cột nội bộ ẩn (cột 17 hiển thị tên Tổ chức/Cá nhân theo logic UI). **PERSIST**: AUDIT_LOG action='EXPORT_VU_VIEC' (verify gián tiếp). | Happy | P1 |
| TC-VV-DS-107 | FR-V.I-01 / SCR-V.I-01:1664 tab coverage | 5 tab còn lại filter trạng thái đúng theo SCR-V.I-01 mapping | `cb_nv_tw_01`. ≥1 VV mỗi nhóm trạng thái: CHO_TIEP_NHAN, CHO_PHE_DUYET, DA_DUYET, HOAN_THANH, DA_DANH_GIA, TU_CHOI. | — | 1. Click tab "Tất cả" → quan sát. 2. Click "Chờ tiếp nhận". 3. Click "Chờ PD". 4. Click "Hoàn thành". 5. Click "Từ chối". | **STATE+UI** mỗi tab: (Tất cả) không filter trạng thái — tất cả VV is_deleted=0 hiện. (Chờ tiếp nhận) filter `trang_thai='CHO_TIEP_NHAN'`. (Chờ PD) filter `trang_thai='CHO_PHE_DUYET'`. (Hoàn thành) filter `trang_thai IN ('DA_DUYET','HOAN_THANH','DA_DANH_GIA')` (3 state — srs-fr-05:1664). (Từ chối) filter `trang_thai='TU_CHOI'`. Mỗi tab badge count realtime khớp số dòng table. **PERSIST**: — | Happy | P0 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DS-201 | FR-V.I-01 / E1 INF-VV-01 | UC51 Filter (không từ khóa) ra 0 kết quả → INF-VV-01 | `cb_nv_tw_01`. | trang_thai=TU_CHOI + linh_vuc=lĩnh-vực-không-tồn-tại-data (KHÔNG nhập tu_khoa) | 1. Filter trạng thái TU_CHOI + Lĩnh vực không có VV nào (tu_khoa rỗng). 2. Click Tìm. | **STATE**: Backend trả empty result, nhánh UC51 (filter only). **UI**: Empty state với icon thư mục trống + "Không có vụ việc nào trong phạm vi quản lý" (srs-fr-05:1605) — đây là trạng thái dữ liệu chung của SCR. **PERSIST**: — | Negative | P1 |
| TC-VV-DS-206 | FR-V.I-08 / E1 INF-VV-TK-01 | UC58 Search có từ khóa 0 kết quả → INF-VV-TK-01 (tách bạch UC51 INF-VV-01) | `cb_nv_tw_01`. | tu_khoa="VV-NONEXIST-99999999-999" (mã VV chắc chắn không tồn tại) | 1. Nhập tu_khoa định dạng đúng nhưng record không tồn tại. 2. Click Tìm. | **STATE**: Backend trả empty cho nhánh search có từ khóa (UC58). **UI**: Toast/inline message "Không tìm thấy hồ sơ phù hợp" — INF-VV-TK-01 (srs-fr-05:681), hoặc empty state SCR với cùng nội dung. Phân biệt với INF-VV-01 (UC51): khi user gõ từ khóa thì error code phải là INF-VV-TK-01 chứ KHÔNG phải INF-VV-01. **PERSIST**: — **Note dev**: nếu BE trả cùng INF code cho 2 nhánh → flag bug spec-implementation diverge. | Negative | P1 |
| TC-VV-DS-202 | FR-V.I-08 / ERR-VV-TK-01 | tu_ngay > den_ngay | `cb_nv_tw_01`. | tu_ngay=2026-12-31, den_ngay=2026-01-01 | 1. Chọn tu_ngay sau den_ngay. 2. Click Tìm. | **STATE**: BE/FE reject (srs-fr-05:682). **UI**: Toast error nguyên văn "Ngày bắt đầu phải trước ngày kết thúc" (ERR-VV-TK-01) hoặc inline error trên DateRange picker. **PERSIST**: — | Negative | P1 |
| TC-VV-DS-203 | BR-EC-13 / search sanitize | XSS payload trong ô tìm kiếm | `cb_nv_tw_01`. | tu_khoa=`<script>alert('XSS-VV')</script>` (boundary 200 ký tự) | 1. Gõ XSS payload vào ô tìm kiếm. 2. Click Tìm. | **STATE**: Backend sanitize input (escape HTML). KHÔNG execute script. **UI**: Bảng load result (likely empty), `list_console_messages` clean (no alert fired). Input field hiển thị raw text payload (escaped). **PERSIST**: KHÔNG persist payload vào DB. **CRITICAL**: Nếu BE quên sanitize → XSS persistent qua filter URL share. | Negative | P0 |
| TC-VV-DS-204 | BR-EC-13 / search boundary 200 | Từ khóa > 200 ký tự | `cb_nv_tw_01`. | tu_khoa = "A" × 201 ký tự | 1. Gõ 201 ký tự A. 2. Click Tìm. | **STATE**: BE truncate hoặc reject. **UI**: Hoặc client maxlength=200 (input bị cắt), hoặc submit → toast error "Từ khóa tối đa 200 ký tự" (SRS Gap message — mark **SPEC-CLARIFY-VV-DS-01**). **PERSIST**: — | Negative | P1 |
| TC-VV-DS-205 | BR-EC-13 / SQL LIKE escape | Từ khóa chứa `%` và `_` (SQL LIKE wildcard) | `cb_nv_tw_01`. | tu_khoa = `100%` (literal phần trăm), `test_dn` (literal underscore) | 1. Tạo VV có MST chứa "100%". 2. Tìm với `100%`. 3. Tìm với `test_dn` (underscore literal). | **STATE**: BE escape `%` → `\%`, `_` → `\_` trước khi LIKE query. **UI**: Bảng hiển thị CHÍNH XÁC VV chứa "100%" hoặc "test_dn", KHÔNG match wildcard. **PERSIST**: — **CRITICAL**: Nếu BE quên escape → user search "test_dn" sẽ match "test1dn", "test2dn" — false positive. | Negative | P1 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-DS-301 | FR-V.I-01 / D — Empty state CMS | Empty state khi đơn vị chưa có VV nào | `cb_nv_bn_01` (giả lập user CB_NV_BN scope đơn vị mới chưa có VV — **SPEC-CLARIFY-VV-PERM-01**). | — | 1. Login user thuộc đơn vị chưa có VV. 2. Vào DS VV. | **UI**: Empty state với icon + chữ "Không có vụ việc nào trong phạm vi quản lý" (srs-fr-05:1605). KHÔNG hiển thị 5 dòng skeleton kéo dài → phải clear sau khi xác nhận empty. | Edge | P2 |
| TC-VV-DS-302 | BR-AUTH-03/04 / scope chéo BN-DP | CB NV BN không thấy VV của ĐP và ngược lại | `cb_nv_bn_01`. Có VV-1 của BN, VV-2 của DP-AG. | — | 1. Login `cb_nv_bn_01`. 2. Vào DS. | **STATE**: Backend filter `don_vi_id = user.don_vi_id` (BR-AUTH-08 srs-fr-05:2391). **UI**: Bảng chỉ hiện VV-1 (BN). KHÔNG có VV-2 (DP). 2 cấp ngang cấp KHÔNG thấy nhau (BR-AUTH-02). **PERSIST**: — | Edge | P0 |
| TC-VV-DS-303 | FR-V.I-01 / batch action eligible filter | Batch [Trình PD hàng loạt] chỉ áp dụng VV ở DANG_XU_LY | `cb_nv_tw_01`. Chọn 5 VV mixed (2 ở DANG_XU_LY + 3 ở khác state). | — | 1. Check 5 VV mixed. 2. Click [Trình PD hàng loạt]. | **STATE**: Backend chỉ process 2 VV ở DANG_XU_LY (BR-FLOW-04). **UI**: Confirm modal "Trình phê duyệt 2/5 vụ việc đủ điều kiện. 3 vụ việc khác state sẽ bị bỏ qua." Sau confirm → toast warning "Đã trình {2}/{5} vụ việc. {3} vụ việc gặp lỗi (nhấn để xem chi tiết)" (srs-fr-05:1622). 2 VV chuyển CHO_PHE_DUYET. **PERSIST**: AUDIT_LOG TRINH_PD x2. | Edge | P1 |
| TC-VV-DS-304 | BR-EC-01 / Optimistic lock | 2 CB NV cùng tiếp nhận 1 VV CHO_TIEP_NHAN | Tab1 `cb_nv_tw_01` + Tab2 `cb_nv_tw_02`. VV-X ở CHO_TIEP_NHAN. | — | 1. Tab1 mở DS, click [Tiếp nhận] VV-X. 2. Tab2 (chưa reload) cũng click [Tiếp nhận] VV-X. | **STATE**: Tab1 SUCCESS — VV-X chuyển DA_TIEP_NHAN, nguoi_tiep_nhan_id=cb_nv_tw_01. Tab2 FAIL với optimistic lock conflict (BR-EC-01). **UI**: Tab1 toast success. Tab2 modal "Vụ việc đã được CB Nghiệp vụ TW 01 cập nhật lúc dd/mm HH:mm. Vui lòng tải lại để xem thông tin mới nhất." + nút [Tải lại] (srs-fr-05:1623). **PERSIST**: AUDIT_LOG 1 entry TIEP_NHAN bởi `cb_nv_tw_01`. | Edge | P0 |
| TC-VV-DS-305 | FR-V.I-01 / D — Loading + lỗi tải | Hiển thị skeleton loading + error retry khi BE 500 | `cb_nv_tw_01`. Mock BE GET /vu-viec trả 500. | — | 1. Vào DS VV. 2. Đợi BE response. | **UI**: Trong 200ms đầu → skeleton 5 dòng giả + spinner header (srs-fr-05:1604). Sau khi BE 500 → empty state với icon cảnh báo + "Không tải được dữ liệu. Vui lòng thử lại sau ít phút." + nút [Thử lại] (srs-fr-05:1608). Click [Thử lại] → re-fetch. | Edge | P1 |
| TC-VV-DS-306 | FR-V.I-01 / FR-V.I-08 combined | Filter kết hợp 5 điều kiện AND (lĩnh vực + trạng thái + kênh + SLA + date range) | `cb_nv_tw_01`. ≥15 VV varied. | — | 1. Set 5 filter. 2. Click Tìm. | **STATE**: Backend WHERE 5 condition AND (srs-fr-05:656). **UI**: Bảng chỉ hiện VV match đủ 5 điều kiện. Pagination cập nhật. URL có thể chứa query params cho deep-link (verify behavior — nếu KHÔNG có deep-link thì mark **SPEC-CLARIFY-VV-DS-02**). **PERSIST**: — | Edge | P1 |
| TC-VV-DS-307 | FR-V.I-01 / count realtime sau action | Tab badge count cập nhật sau khi tiếp nhận 1 VV | `cb_nv_tw_01`. Tab "Chờ tiếp nhận" badge=5, "Đang xử lý" badge=10. | — | 1. Quan sát badge ban đầu. 2. Click [Tiếp nhận] 1 VV ở tab "Chờ tiếp nhận". 3. Quan sát badge sau action. | **STATE**: VV chuyển CHO_TIEP_NHAN → DA_TIEP_NHAN. **UI**: Badge "Chờ tiếp nhận" giảm 5→4, "Đang xử lý" tăng 10→11 (srs-fr-05:1664 — count realtime). Polling hoặc websocket cập nhật trong vòng 2 giây. **PERSIST**: AUDIT_LOG TIEP_NHAN. | Edge | P1 |
| TC-VV-DS-308 | FR-V.I-01 / SCR-V.I-01:1683 batch delete | Batch [Xóa hàng loạt] eligible filter + confirm + soft-delete | `cb_nv_tw_01`. Chọn 4 VV mixed: 2 VV ở MOI_TAO/CHO_TIEP_NHAN (chưa tiếp nhận) + 2 VV ở DANG_XU_LY/CHO_PHE_DUYET (đã tiếp nhận). | — | 1. Check 4 VV mixed. 2. Click [Xóa hàng loạt]. 3. Quan sát confirm modal C12. 4. Confirm. | **STATE**: BR-DATA-02 soft delete (`is_deleted=1`). Eligible state để xóa cần được spec rõ — **SPEC-CLARIFY-VV-DS-04** (SRS không định nghĩa UC/BR cho Xóa VV individual hay batch — không có ràng buộc trạng thái nào được phép xóa hay phải khôi phục thế nào). **UI**: Confirm modal "Bạn có chắc xóa N vụ việc?" — sau confirm: toast result. **PERSIST**: AUDIT_LOG action='DELETE_VU_VIEC' cho mỗi VV. **CRITICAL**: nếu BE cho xóa VV ở state DANG_XU_LY/CHO_PHE_DUYET → flag bug nghiệp vụ (cấp dưới đang xử lý mà bị xóa = mất dữ liệu trace). | Edge | P1 |
| TC-VV-DS-309 | FR-V.I-01 / SCR-V.I-01:1690 sort cột khác | Sort theo cột Mã VV (text) và Trạng thái (enum order) | `cb_nv_tw_01`. ≥10 VV varied. | — | 1. Click header "Mã VV". 2. Click lại. 3. Click header "Trạng thái". | **STATE**: Backend `ORDER BY ma_vu_viec ASC/DESC` rồi `ORDER BY trang_thai`. **UI**: Mã VV sort theo string ASC/DESC (icon ▲/▼). Trạng thái sort theo thứ tự enum SM-VUVIEC (MOI_TAO → CHO_TIEP_NHAN → ... → DA_DANH_GIA) — verify sort order khớp định nghĩa trong SCR-V.I-01:1690 "sort theo từng cột". **PERSIST**: — | Edge | P2 |

---

## Tổng kết file

**Tổng TC: 25** (3 UI + 7 Happy + 6 Negative + 9 Edge) — sau Codex review 2026-05-09

| Section | TC IDs | Count |
|---------|--------|------:|
| A. UI verification | UI-01, UI-02, UI-03 | 3 |
| B. CRUD Happy | 101, 102, 103, 104, 105, 106, **107** ⭐ | 7 |
| C. Negative | 201, 202, 203, 204, 205, **206** ⭐ | 6 |
| D. Edge | 301, 302, 303, 304, 305, 306, 307, **308** ⭐, **309** ⭐ | 9 |

⭐ = thêm sau Codex review 2026-05-09.

**Priority**: P0=9 / P1=14 / P2=2

**Coverage:**
- BR: BR-AUTH-01/03/04/08, BR-DATA-02/06/07, BR-EC-01/13, BR-FLOW-04, BR-SLA-02
- Error codes: INF-VV-01 (UC51), INF-VV-TK-01 (UC58 — TC-206 mới tách bạch), ERR-VV-TK-01 (full coverage UC51 + UC58 documented errors)
- AC SRS: 3/3 UC51 (srs-fr-05:144-146) + 3/3 UC58 (srs-fr-05:685-687)
- SCR-V.I-01: 23/23 component tested (TC-107 cover 5 tab còn lại + TC-308 cover [Xóa hàng loạt] + TC-309 cover sort multi-column)

**SPEC-CLARIFY:**
- **VV-DS-01**: search boundary 200 char message — SRS không spec wording cụ thể
- **VV-DS-02**: deep-link query params — SRS không mandate URL params
- **VV-DS-03 (mới)**: muc_sla enum mismatch — UC51 input liệt kê 3 enum (BINH_THUONG/SAP_HET/QUA_HAN, srs-fr-05:107) vs SCR-V.I-01 dropdown 4 enum (+QUA_HAN_NGHIEM_TRONG, srs-fr-05:1669). BR-SLA-02 (srs-fr-05:2457) confirm 4 mức. Đề xuất BA: sửa UC51 input thành 4 enum để đồng bộ.
- **VV-DS-04 (mới)**: Xóa VV individual + batch — SRS không có UC/FR cho hành động Xóa VV, không có BR ràng buộc state nào được phép xóa, không định nghĩa khôi phục. SCR-V.I-01 row 1683 nhắc "🗑 Xóa (C12 confirm)" + "[Xóa hàng loạt]" nhưng không có hậu xử lý spec. Đề xuất BA: tạo FR-V.I-XX "Xóa hồ sơ" với state guard (chỉ MOI_TAO/CHO_TIEP_NHAN được xóa hard? Hoặc soft-delete mọi state?) + permission rule.
- **VV-PERM-01**: CSV thiếu user BN/DP để verify scope đơn vị

**Codex review changelog 2026-05-09:**
- ADD TC-VV-DS-107 (Tab coverage 5 tab còn lại — gap SCR-V.I-01:1664 mapping)
- ADD TC-VV-DS-206 (UC58 search empty INF-VV-TK-01 — gap tách bạch UC51 vs UC58)
- ADD TC-VV-DS-308 (Batch Xóa hàng loạt — gap SCR-V.I-01:1683)
- ADD TC-VV-DS-309 (Sort cột Mã VV + Trạng thái — gap SCR-V.I-01:1690 "sort theo từng cột")
- FIX TC-VV-DS-UI-01 "12 cột" → "11 cột" (SCR-V.I-01 rows 11-21 = 11 cột, không phải 12)
- ADD SPEC-CLARIFY-VV-DS-03 (muc_sla enum mismatch UC51 vs SCR vs BR-SLA-02)
- ADD SPEC-CLARIFY-VV-DS-04 (Xóa VV không có UC/BR/state guard)
