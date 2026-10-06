# Test Cases — UC24: Quản lý Khóa học (FR-III-05) + SM-KHOAHOC 11 transitions + AT-01/AT-02

> **SRS Ref**: FR-III-05 (UC24 phần KH CRUD) + SCR-III-02 Tab "Thông tin" (`02-thu-tu-module.md` §⑨ dòng 597) + SM-KHOAHOC 11 transitions (Plan overview §2.2, dòng 619-631) + AT-01/AT-02 (SRS dòng 62-63).
> **Workflow critical**: Tạo KH (DU_THAO) → Gửi duyệt (CHO_DUYET) → CB PD duyệt (DA_DUYET) → CB NV công khai (DA_CONG_KHAI) → AT-time DANG_DIEN_RA → AT-time DA_KET_THUC → Trình KQ (CHO_DUYET_KQ) → Duyệt (HOAN_THANH).
> **Nguồn**: SRS local `srs-fr-03-dao-tao.md` dòng 412-555 + `02-thu-tu-module.md` §⑨ dòng 597, 619-631 + Plan overview §2.2 + SPEC-CLARIFY-DT-01.
> **Ngày tạo**: 2026-05-09 (Phase A re-run)
> **Phạm vi tài khoản**: cb_nv_tw_01 (Create/Update/Public/Trình KQ), cb_pd_tw_01 (Approve/Reject/Approve KQ), cb_nv_bn_01 (cross-cấp negative), DN/NHT (public read).

---

## A. UI VERIFICATION (SCR-III-02 Tab "Thông tin")

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-H-001 | FR-III-05 / SCR-III-02 Tab Thông tin / UI | Verify Tab "Thông tin" SCR-III-02 — đầy đủ 9 field theo SRS dòng 597 | CB_NV_TW (cb_nv_tw_01) đăng nhập. KH "KH-20260601-001" trạng thái `DU_THAO` tồn tại. | URL: `/dao-tao/khoa-hoc/{kh_id}` | 1. Đăng nhập. 2. Vào SCR-III-01, expand CTĐT, click row KH-001. 3. Tab "Thông tin" active mặc định. | **STATE**: Backend `GET /api/v1/khoa-hoc/{id}`. **UI**: Header card hiển thị: Mã KH bold, badge trạng thái (9 màu SM-KHOAHOC), CTĐT cha link, action-bar [Sửa] [Hủy] [Gửi duyệt]. 6 tabs: Thông tin (active) / Học viên / Lịch học & Điểm danh / KQ kiểm tra / Chứng nhận / Bài giảng. **9 field SRS dòng 597**: Mã khóa học (readonly), Tên khóa học * (text), CTĐT cha * (searchable select chỉ DA_DUYET), Hình thức * (radio TRUC_TUYEN/TRUC_TIEP), Ngày bắt đầu *, Ngày kết thúc *, Địa điểm (nếu TRUC_TIEP) hoặc Link Zoom (nếu TRUC_TUYEN), Số lượng HV tối đa * (≥1), Lĩnh vực PL * (FK), Ngân sách. **PERSIST**: Reload giữ tab + state. | Happy 🔴 |
| TC-KH-H-002 | FR-III-05 / SRS dòng 597 / Edit-rule | Tab "Thông tin" — read-only khi KH NOT `DU_THAO` | CB_NV_TW. KH "KH-002" `DA_DUYET`. | — | 1. Mở KH-002 Tab Thông tin. | **STATE**: — (read-only). **UI**: Per SRS dòng 597 "Chỉ cho sửa khi khóa học ở trạng thái `DU_THAO`". Tất cả input/select disabled. Action-bar [Sửa] **ẨN**. Hover label tooltip "Khóa học đã duyệt — không sửa được" (SPEC-CLARIFY-DT-21). **PERSIST**: Reload. | Happy 🟡 |

---

## B. READ / LIST — Expandable từ CTĐT

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-H-003 | FR-III-05 / SCR-III-01 Expandable | Expand CTĐT hiển thị KH con — filter `ctdt_id` chính xác | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" có 4 KH con (đa state). CTĐT khác có 2 KH không liên quan. | — | 1. SCR-III-01 → click ▶ row CTDT-TW01-2026-001. | **STATE**: Backend `GET /api/v1/khoa-hoc?ctdt_id=...`. **UI**: Nested table 4 KH với cột: Mã KH, Tên, Hình thức, Ngày BĐ→KT, Trạng thái (badge SM-KHOAHOC 9 màu). KHÔNG có KH của CTĐT khác. **PERSIST**: Click ▼ → collapse. | Happy |
| TC-KH-H-004 | FR-III-06 / BR-AUTH-08 | CB_NV_DP chỉ thấy KH thuộc đơn vị ĐP | CB_NV_DP. Seed KH cả 3 cấp + ĐP khác. | — | 1. CB_NV_DP vào danh sách KH (qua Tìm kiếm KH). | **STATE**: Backend `WHERE don_vi_id = cb_nv_dp_01.don_vi_id`. **UI**: Chỉ KH đơn vị ĐP của user. **PERSIST**: Reload. | Happy |
| TC-KH-H-005 | FR-III-06 / BR-DATA-07 | Pagination KH default 20/page | CB_NV_TW. Seed ≥25 KH thuộc TW. | — | 1. Vào Tìm kiếm KH. 2. Xem pagination. | **STATE**: Default `size=20`. **UI**: 20 row + pagination "Tổng: ≥25 mục". **PERSIST**: Reload. | Boundary |

---

## C. CREATE — Tạo KH mới (auto-gen mã, dropdown CTĐT chỉ DA_DUYET)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-H-006 | FR-III-05 / BR-DATA-04 / SRS dòng 621 | Tạo KH thành công TRUC_TIEP — verify auto-gen mã `KH-{YYYYMMDD}-{SEQ}` | CB_NV_TW. CTĐT "CTDT-TW01-2026-001" `DA_DUYET`. Lĩnh vực DAN_SU. GV `DANG_HOAT_DONG`. Ngày tạo 2026-06-01. | ten_khoa_hoc="KH Pháp luật DN T6/2026", ctdt_id=CTDT-001, hinh_thuc=TRUC_TIEP, ngay_bat_dau="2026-07-01", ngay_ket_thuc="2026-07-31", dia_diem="HT A", so_luong_toi_da=50, linh_vuc_id=DAN_SU, giang_vien_ids=[GV-001], bai_giang_ids=[BG-001, BG-002] | 1. SCR-III-01 → click [+ Thêm khóa học] (action-bar khi expand). 2. Form drawer điền đủ. 3. Lưu. | **STATE**: INSERT KHOA_HOC với `ma_kh` match regex `^KH-20260601-\d+$` (BR-DATA-04 format `KH-{YYYYMMDD}-{SEQ}` Plan overview §2.1 BR-DATA-04). `trang_thai='DU_THAO'` (SRS dòng 621). 7 common fields BR-DATA-03. AUDIT_LOG: hanh_dong='CREATE'. **UI**: Toast "Thêm khóa học thành công" (SPEC-CLARIFY-DT-21). Drawer đóng, KH mới xuất hiện trong expand row CTĐT cha với badge "Nháp". **PERSIST**: Reload — record tồn tại với mã `KH-20260601-001`. | Happy 🔴 |
| TC-KH-H-007 | FR-III-05 / SRS dòng 621 / Dropdown filter | Tạo KH — dropdown CTĐT cha CHỈ hiển thị CTĐT `DA_DUYET` | CB_NV_TW. Seed: CTĐT-A `DA_DUYET`, CTĐT-B `NHAP`, CTĐT-C `CHO_DUYET`. | — | 1. Form thêm KH. 2. Click dropdown "CTĐT cha". | **STATE**: Backend `GET /api/v1/chuong-trinh-dao-tao?trang_thai=DA_DUYET`. **UI**: Dropdown chỉ 1 option CTĐT-A. KHÔNG hiện CTĐT-B (NHAP) / CTĐT-C (CHO_DUYET). **PERSIST**: SRS dòng 621 nguyên văn "dropdown chỉ lấy CTĐT đã `DA_DUYET`". | Happy 🔴 |
| TC-KH-H-008 | FR-III-05 / Cross-module FR-04 | Tạo KH — Giảng viên dropdown lấy từ FR-04 TU_VAN_VIEN `DANG_HOAT_DONG` | CB_NV_TW. Seed FR-04 TVV: 2 GV active + 1 VO_HIEU_HOA. | — | 1. Form thêm KH Accordion GV. 2. Click dropdown. | **STATE**: Backend `GET /api/v1/tu-van-vien?trang_thai=DANG_HOAT_DONG&loai_tvv=GV` (SRS dòng 621 nguyên văn "Giảng viên chọn từ TU_VAN_VIEN, lọc trang_thai=DANG_HOAT_DONG"). **UI**: Dropdown chỉ 2 GV active. KHÔNG hiện GV vô hiệu hóa. **PERSIST**: — | Cross-module 🔴 |
| TC-KH-N-009 | ERR-KH-01 | Tạo KH — tên trống | CB_NV_TW. | ten_khoa_hoc="" | 1. Form. 2. Bỏ trống Tên. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline error "**Tên khóa học là bắt buộc**" (ERR-KH-01 nguyên văn Plan overview §2.3). Focus về field. **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-KH-N-010 | ERR-KH-02 | Tạo KH — ngày KT ≤ ngày BĐ | CB_NV_TW. | ngay_bat_dau="2026-07-01", ngay_ket_thuc="2026-06-30" | 1. Form. 2. Nhập 2 ngày. 3. Lưu. | **STATE**: KHÔNG INSERT. BE check ngay_ket_thuc > ngay_bat_dau (SRS dòng 621 "phải > ngày bắt đầu"). **UI**: Inline error "**Ngày kết thúc phải sau ngày bắt đầu**" (ERR-KH-02). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-KH-N-011 | ERR-KH-03 | Tạo KH — ctdt_id không tồn tại / FK fail | CB_NV_TW. | ctdt_id="CTDT-NOT-EXIST" | 1. API direct POST với ctdt_id sai. | **STATE**: KHÔNG INSERT. BE FK fail → 422. **UI**: Toast "**Chương trình đào tạo cha không tồn tại**" (ERR-KH-03). **PERSIST**: — | Negative |
| TC-KH-N-012 | FR-III-05 / so_luong_toi_da boundary | Tạo KH — so_luong_toi_da = 0 | CB_NV_TW. | so_luong_toi_da=0 | 1. Form. 2. Số HV=0. 3. Lưu. | **STATE**: KHÔNG INSERT. BE check ≥1 (SRS dòng 621 "≥1"). **UI**: Inline error "Số lượng HV tối đa phải ≥ 1" (SPEC-CLARIFY-DT-22 nguyên văn). **PERSIST**: — | Negative 🟡 |

---

## D. UPDATE — Sửa KH (chỉ DU_THAO per SRS dòng 597)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-H-013 | FR-III-05 / BR-DATA-05 / SRS dòng 597 | Sửa KH `DU_THAO` — đổi tên + ngân sách | CB_NV_TW. KH `DU_THAO`. | ten_moi="KH Pháp luật DN T7/2026 (sửa)", ngan_sach=150000000 | 1. Tab Thông tin → click [Sửa]. 2. Đổi 2 field. 3. Lưu. | **STATE**: UPDATE SET ten_khoa_hoc=..., ngan_sach=..., updated_at, updated_by. AUDIT_LOG: hanh_dong='UPDATE' du_lieu_cu/du_lieu_moi (BR-DATA-05). **UI**: Toast OK. **PERSIST**: Reload reflect. | Happy |
| TC-KH-N-014 | ERR-KH-04 / SRS dòng 597 / BR-FLOW-03 | Sửa KH `DA_DUYET` — bị chặn | CB_NV_TW. KH "KH-002" `DA_DUYET`. | — | 1. Tab Thông tin → cố click [Sửa] hoặc force API PUT. | **STATE**: KHÔNG UPDATE. **UI**: Nút [Sửa] **ẨN** trên DA_DUYET (TC-KH-H-002). Force API → BE reject "**Không thể sửa khóa học đã được duyệt**" (ERR-KH-04 nguyên văn). **PERSIST**: Record không đổi. | Negative 🔴 |

---

## E. DELETE / HUY (Hủy KH chưa có HV)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-H-015 | FR-III-05 / SM-KHOAHOC dòng 631 / BR-DATA-01 | Hủy KH `DU_THAO` — chưa có HV → DU_THAO → HUY | CB_NV_TW. KH `DU_THAO`, 0 đăng ký HV. | ly_do="Thay đổi kế hoạch đào tạo do điều chỉnh ngân sách" | 1. Action-bar → click [Hủy]. 2. Modal nhập lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='HUY', ly_do_huy=<text>, updated_by. AUDIT_LOG: hanh_dong='CANCEL'. **UI**: Toast "Hủy khóa học thành công" (SPEC-CLARIFY-DT-21). Badge "Đã hủy" (xám đậm). **PERSIST**: HUY. | Happy |
| TC-KH-N-016 | FR-III-05 / SM-KHOAHOC dòng 631 / Guard "chưa có HV" | Hủy KH `DA_DUYET` — đã có 5 HV `DA_DUYET` → bị chặn | CB_NV_TW. KH `DA_DUYET`, 5 đăng ký `DA_DUYET`. | — | 1. Click [Hủy]. | **STATE**: KHÔNG UPDATE. BE check `COUNT(DANG_KY WHERE khoa_hoc_id AND trang_thai='DA_DUYET') = 0` fail. **UI**: Toast "**Không thể hủy khóa học đã có học viên đăng ký**" (SPEC-CLARIFY-DT-23 nguyên văn). **PERSIST**: Record không đổi. | Negative 🔴 |

---

## F. STATE TRANSITIONS — SM-KHOAHOC 11 transitions + AT-01 + AT-02 + invalid

> Source: Plan overview §2.2 SM-KHOAHOC mermaid + SRS dòng 619-631 transition table (single source of truth).
> Mỗi happy transition = 1 TC. AT-01 (DU_THAO→CHO_DUYET) + AT-02 (DA_KET_THUC→CHO_DUYET_KQ) test ở section này (TC-KH-S-017 + TC-KH-S-024). Time-driven AT (theo ngay_bat_dau/ngay_ket_thuc) test ở FILE 04 (TC-LICH-S-013/014).

### F1. Happy transitions (11 + AT-01 + AT-02 = 13 TC)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-S-017 | FR-III-05 / AT-01 / SM dòng 622 | T1: DU_THAO → CHO_DUYET — CB NV [Gửi duyệt] (guard ≥1 bài giảng) | CB_NV_TW. KH `DU_THAO`, có 2 BAI_GIANG đã gắn. | — | 1. Action-bar → [Gửi duyệt]. | **STATE**: UPDATE SET trang_thai='CHO_DUYET'. AUDIT_LOG: hanh_dong='SUBMIT', actor=cb_nv_tw_01. Notification cb_pd_tw_01 (BR-NOTIF-01). **UI**: Toast OK. Badge "Chờ duyệt" (cam). Nút [Sửa]/[Gửi duyệt] ẩn. **PERSIST**: CHO_DUYET. | Happy 🔴 |
| TC-KH-S-018 | FR-III-05 / SM dòng 623 / BR-AUTH-05 | T2: CHO_DUYET → DA_DUYET — CB PD cùng cấp [Duyệt] | cb_pd_tw_01. KH `CHO_DUYET` cấp TW. | — | 1. CB PD vào danh sách Chờ duyệt. 2. Click [Duyệt]. | **STATE**: UPDATE SET trang_thai='DA_DUYET'. AUDIT_LOG: hanh_dong='APPROVE'. Notification cb_nv_tw_01. **UI**: Toast OK. Badge "Đã duyệt" (xanh dương). **PERSIST**: DA_DUYET. | Happy 🔴 |
| TC-KH-S-019 | FR-III-05 / SM dòng 624 / BR-FLOW-04 | T3: CHO_DUYET → DU_THAO — CB PD [Từ chối] với ly_do ≥10 ký tự | cb_pd_tw_01. KH `CHO_DUYET`. | ly_do="Thiếu mục tiêu định lượng cụ thể, đề nghị bổ sung KPI" | 1. Click [Từ chối]. 2. Modal lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='DU_THAO', ly_do_tu_choi=<text>. AUDIT_LOG: hanh_dong='REJECT'. **UI**: Toast OK. Badge "Nháp" trở lại. CB NV nhận notification + có thể sửa lại. **PERSIST**: DU_THAO + lý do hiển thị header. | Happy 🔴 |
| TC-KH-S-020 | FR-III-05 / SPEC-CLARIFY-DT-01 / Plan §2.2 | T4: DA_DUYET → DA_CONG_KHAI — CB NV toggle `la_cong_khai` (SPEC gap) | cb_nv_tw_01. KH `DA_DUYET`. | la_cong_khai=true | 1. Action-bar → click [Công khai] hoặc toggle `la_cong_khai`. | **STATE**: UPDATE SET trang_thai='DA_CONG_KHAI', la_cong_khai=true. AUDIT_LOG: hanh_dong='PUBLISH'. **UI**: Toast OK. Badge "Đã công khai" (xanh lá). KH xuất hiện ở Cổng PLQG public. **PERSIST**: DA_CONG_KHAI. **Note**: SPEC-CLARIFY-DT-01 — SRS Phụ lục C.2 thiếu transition này; test theo logic Plan §2.2 + 02-thu-tu-module dòng 617. | Happy 🔴 |
| TC-KH-S-021 | FR-III-05 / SM dòng 625 / AT time-driven | T5: DA_CONG_KHAI → DANG_DIEN_RA — CB NV manual [Bắt đầu] | cb_nv_tw_01. KH `DA_CONG_KHAI`, ngay_bat_dau=hôm nay. | — | 1. Action-bar → click [Bắt đầu]. | **STATE**: UPDATE SET trang_thai='DANG_DIEN_RA'. AUDIT_LOG: hanh_dong='START'. **UI**: Toast OK. Badge "Đang diễn ra" (vàng). Tab Lịch học enable edit (FILE 04 TC-001). **PERSIST**: DANG_DIEN_RA. **Cross-ref**: AT auto cùng transition test ở FILE 04 TC-LICH-S-013. | Happy 🔴 |
| TC-KH-S-022 | FR-III-05 / SM dòng 627 | T6: DANG_DIEN_RA → DA_KET_THUC — CB NV manual [Kết thúc] | cb_nv_tw_01. KH `DANG_DIEN_RA`. | — | 1. Click [Kết thúc]. | **STATE**: UPDATE SET trang_thai='DA_KET_THUC'. AUDIT_LOG: hanh_dong='END'. **UI**: Toast OK. Badge "Đã kết thúc" (xám). Tab "KQ kiểm tra" enable nhập (SRS dòng 600). **PERSIST**: DA_KET_THUC. **Cross-ref**: AT auto FILE 04 TC-LICH-S-014. | Happy |
| TC-KH-S-023 | FR-III-05 / AT-02 / SM dòng 628 | T7: DA_KET_THUC → CHO_DUYET_KQ — CB NV [Trình KQ] (guard điểm danh + điểm KT đầy đủ) | cb_nv_tw_01. KH `DA_KET_THUC`, đầy đủ điểm danh + điểm KT cho all HV. | — | 1. Tab KQ kiểm tra → click [Trình KQ] (action-bar). | **STATE**: UPDATE SET trang_thai='CHO_DUYET_KQ'. AUDIT_LOG: hanh_dong='SUBMIT_RESULT'. Notification cb_pd_tw_01. **UI**: Toast OK. Badge "Chờ duyệt KQ" (cam). **PERSIST**: CHO_DUYET_KQ. | Happy 🔴 |
| TC-KH-S-024 | FR-III-05 / SM dòng 629 (Plan §2.2 mapping) | T8: CHO_DUYET_KQ → HOAN_THANH — CB PD [Duyệt KQ + Cấp chứng nhận] | cb_pd_tw_01. KH `CHO_DUYET_KQ`. | — | 1. CB PD click [Duyệt KQ]. | **STATE**: UPDATE SET trang_thai='HOAN_THANH'. AUDIT_LOG: APPROVE_RESULT. INSERT CHUNG_NHAN cho HV `xep_loai='DAT'`. **UI**: Toast OK. Badge "Hoàn thành" (xanh đậm). Tab "Chứng nhận" enable + hiển thị danh sách CN. **PERSIST**: HOAN_THANH. | Happy 🔴 |
| TC-KH-S-025 | FR-III-05 / SM dòng (rejected KQ) / BR-FLOW-04 | T9: CHO_DUYET_KQ → DA_KET_THUC — CB PD [Từ chối KQ] với ly_do ≥10 ký tự | cb_pd_tw_01. KH `CHO_DUYET_KQ`. | ly_do="Số liệu điểm danh không khớp với báo cáo, đề nghị rà soát" | 1. CB PD click [Từ chối KQ]. 2. Lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='DA_KET_THUC', ly_do_tu_choi_kq=<text>. AUDIT_LOG: REJECT_RESULT. **UI**: Toast OK. Badge "Đã kết thúc" trở lại. CB NV được phép re-submit. **PERSIST**: DA_KET_THUC. | Happy 🔴 |
| TC-KH-S-026 | FR-III-05 / SM dòng 631 / Hủy từ DU_THAO | T10: DU_THAO → HUY (đã test TC-KH-H-015 — happy). Re-state để cover 11 transitions list. | Xem TC-KH-H-015. | — | — | Xem TC-KH-H-015. **STATE**: HUY. **UI**: Badge "Đã hủy". **PERSIST**: HUY. | Happy |
| TC-KH-S-027 | FR-III-05 / SM dòng 631 / Hủy từ CHO_DUYET (rút trình) | T11: CHO_DUYET → HUY — CB NV rút trình (guard chưa có HV) | cb_nv_tw_01. KH `CHO_DUYET`, 0 HV. | ly_do="Rút lại để bổ sung tài liệu" | 1. CB NV click [Rút trình] hoặc [Hủy]. 2. Lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='HUY', ly_do_huy=<text>. AUDIT_LOG: CANCEL. **UI**: Toast OK. Badge "Đã hủy". **PERSIST**: HUY. | Happy |
| TC-KH-S-028 | FR-III-05 / SM dòng 631 / Hủy từ DA_DUYET (chưa có HV) | T12: DA_DUYET → HUY — CB PD/CB NV hủy khi chưa có HV | cb_nv_tw_01. KH `DA_DUYET`, 0 HV. | ly_do="Thay đổi kế hoạch năm" | 1. Click [Hủy]. 2. Lý do. 3. Confirm. | **STATE**: UPDATE SET trang_thai='HUY'. AUDIT_LOG: CANCEL. **UI**: Toast OK. Badge "Đã hủy". **PERSIST**: HUY. | Happy 🟡 |

### F2. Invalid transitions / guard violations (5 TC)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-N-029 | ERR-KH-05 / SM dòng 622 guard | Trình duyệt KH `DU_THAO` thiếu bài giảng — bị chặn | cb_nv_tw_01. KH `DU_THAO`, 0 BAI_GIANG. | — | 1. Click [Gửi duyệt]. | **STATE**: KHÔNG UPDATE. BE check `COUNT(BAI_GIANG_KH) >= 1` fail. **UI**: Toast/inline "**Khóa học phải có ít nhất 1 bài giảng trước khi gửi duyệt**" (ERR-KH-05 nguyên văn Plan §2.3). **PERSIST**: DU_THAO. | Negative 🔴 |
| TC-KH-N-030 | FR-III-05 / SM invalid current state | Gửi duyệt KH `DA_DUYET` — invalid (đã duyệt rồi) | cb_nv_tw_01. KH `DA_DUYET`. | API direct POST `/khoa-hoc/{id}/submit` | 1. Force API. | **STATE**: KHÔNG UPDATE. BE check trang_thai NOT IN ('DU_THAO') → 422. **UI**: UI nút [Gửi duyệt] không hiển thị trên DA_DUYET. Force API → error code "**ERR-KH-INVALID-TRANSITION**" (SPEC-CLARIFY-DT-24 mã + nguyên văn). **PERSIST**: DA_DUYET. | Negative 🟡 |
| TC-KH-N-031 | ERR-PD-01 / BR-AUTH-05 | Phê duyệt KH cấp TW bằng CB_PD_BN — invalid actor cấp | cb_pd_bn_01 (cấp BN). KH `CHO_DUYET` cấp TW. | API direct PUT approve | 1. Force API. | **STATE**: KHÔNG UPDATE. BE check `cb_pd.don_vi_id == khoa_hoc.don_vi_id` (BR-AUTH-05 cùng cấp) fail → 403. **UI**: KH cấp TW không hiển thị trong danh sách CB_PD_BN. Force API → toast "**Người phê duyệt phải cùng cấp với khóa học**" (ERR-PD-01 nguyên văn Plan §2.3). **PERSIST**: CHO_DUYET. | Negative 🔴 |
| TC-KH-N-032 | ERR-PD-02 / BR-FLOW-04 | Từ chối KH thiếu lý do (< 10 ký tự) | cb_pd_tw_01. KH `CHO_DUYET`. | ly_do="Sai" (3 ký tự) | 1. Click [Từ chối]. 2. Lý do 3 ký. 3. Confirm. | **STATE**: KHÔNG UPDATE. BE check `LENGTH(ly_do) >= 10` fail. **UI**: Inline error "**Lý do từ chối phải tối thiểu 10 ký tự**" (ERR-PD-02 + BR-FLOW-04 Plan §2.1). Modal không đóng. **PERSIST**: CHO_DUYET. | Negative 🔴 |
| TC-KH-N-033 | FR-III-05 / SM dòng 631 guard | Hủy KH `DANG_DIEN_RA` — invalid (đã diễn ra) | cb_nv_tw_01. KH `DANG_DIEN_RA`. | API direct cancel | 1. Force API. | **STATE**: KHÔNG UPDATE. BE check `trang_thai NOT IN ('DANG_DIEN_RA','DA_KET_THUC',...)` per SM dòng 631 "Any (trừ đã công khai)" — interpretation: chỉ cho hủy ở DU_THAO/CHO_DUYET/DA_DUYET. **UI**: Nút [Hủy] không hiển thị trên DANG_DIEN_RA. Force API → "**Không thể hủy khóa học đang diễn ra**" (SPEC-CLARIFY-DT-25 nguyên văn). **PERSIST**: DANG_DIEN_RA. | Negative 🔴 |

---

## G. NEGATIVE — ERR-KH-01..05 explicit recap

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
<!-- A7 LOẠI: TC-KH-N-034 + TC-KH-N-035 (explicit recap, redundant với TC-009/014). Coverage không mất. -->

---

## H. PERMISSION (high-level — chi tiết ở 13-TC-permission-matrix.md)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-P-036 | Permission Matrix / Public_view | DN/NHT public_view KH `DA_CONG_KHAI` qua Cổng PLQG | DN (dn_01). KH `DA_CONG_KHAI` từ TW + BN + ĐP. | — | 1. DN truy cập trang công khai KH. | **STATE**: BE filter `WHERE trang_thai='DA_CONG_KHAI' AND is_deleted=0` (no scope cho public). **UI**: Hiển thị danh sách KH `DA_CONG_KHAI` từ tất cả đơn vị. CHỈ READ — KHÔNG có Sửa/Hủy/Trình duyệt. Có nút [Đăng ký] (FR-III-04). **PERSIST**: Reload. | Happy |
| TC-KH-P-037 | Permission Matrix / CB_NV cross-cấp | CB_NV_BN cố tạo KH thuộc CTĐT cấp TW — bị chặn | cb_nv_bn_01. CTĐT cấp TW `DA_DUYET`. | API POST với ctdt_id=TW | 1. Force API direct. | **STATE**: KHÔNG INSERT. BE check `cb_nv.don_vi_id == ctdt.don_vi_id` fail → 403. **UI**: HTTP 403. **PERSIST**: Count không đổi. | Negative 🔴 |

---

## I. EDGE — Concurrency, công khai sau ngày BĐ, hủy đã có ĐK

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-E-038 | FR-III-05 / BR-EC-01 | Optimistic lock — 2 CB_NV_TW cùng sửa 1 KH `DU_THAO` | cb_nv_tw_01 (A) + cb_nv_tw_02 (B). KH `DU_THAO`. | A đổi tên, B đổi ngân sách | 1. Cả 2 mở form (updated_at=T1). 2. A lưu T2. 3. B lưu. | **STATE**: A INSERT OK. B BE check `WHERE updated_at=T1` → 0 row → reject. **UI**: A toast OK. B toast "**Bản ghi đã bị thay đổi bởi người khác. Vui lòng tải lại trang**" (BR-EC-01 / ERR-SYS-02 — SPEC-CLARIFY-DT-26). **PERSIST**: KH reflect chỉ A change. | Edge 🟡 |
| TC-KH-E-039 | FR-III-05 / SPEC-CLARIFY-DT-27 | Edge — Công khai KH với ngay_bat_dau ĐÃ QUA hôm nay | cb_nv_tw_01. KH `DA_DUYET`, ngay_bat_dau=hôm qua. | — | 1. Click [Công khai] (transition DA_DUYET → DA_CONG_KHAI). | **STATE**: BE behavior 2 lựa chọn: (A) Cho phép công khai + AT cron lập tức tick → DANG_DIEN_RA (TC-LICH-S-013 trigger). (B) BE block với "Không thể công khai khóa học có ngày bắt đầu đã qua". SPEC-CLARIFY-DT-27 cần BA confirm. **UI**: Per behavior chọn. **PERSIST**: Per behavior. | Edge 🟡 |
| TC-KH-E-040 | FR-III-05 / SM dòng 631 / Edge guard | Hủy KH `DA_DUYET` đã có 1 HV `CHO_DUYET` (chưa được CB NV duyệt ĐK) | cb_nv_tw_01. KH `DA_DUYET`, 1 DANG_KY `CHO_DUYET`. | — | 1. Click [Hủy]. | **STATE**: SPEC-CLARIFY-DT-28: Plan §2.2 dòng 631 guard "chưa có HV" — định nghĩa "có" = `DA_DUYET` đăng ký hay bao gồm `CHO_DUYET`? Default logic: chỉ count `DA_DUYET` (HV đã được approve ĐK). → Cho phép hủy + cascade reject all DK CHO_DUYET. **UI**: Modal cảnh báo "Có {N} đăng ký chờ duyệt sẽ bị từ chối tự động — xác nhận hủy?". **PERSIST**: KH HUY + DK auto REJECT. | Edge 🟡 |
| TC-KH-E-041 | FR-III-05 / BR-DATA-04 / Auto-gen sequence | Tạo 3 KH cùng ngày → SEQ tăng dần 001/002/003 | CB_NV_TW. Ngày tạo 2026-06-01. Pre-state: 0 KH ngày này. | Tạo 3 KH liên tiếp | 1. Tạo KH-A, B, C. 2. Query DB. | **STATE**: 3 record với `ma_kh` = `KH-20260601-001/002/003` (BR-DATA-04 SEQ atomic). **UI**: Cột Mã hiển thị 3 mã. **PERSIST**: Filter `ma_kh LIKE 'KH-20260601-%'` → 3 record. | Edge 🟡 |
| TC-KH-E-042 | FR-III-05 / BR-DATA-05 / Audit full lifecycle | Verify AUDIT_LOG full chuỗi state KH qua FR-10 W1.1 UI | cb_nv_tw_01 + cb_pd_tw_01. KH lifecycle đầy đủ. FR-10 W1.1 Nhật ký HT screen sẵn. | Sequence: tạo→submit→approve→public→manual-start→manual-end→submit_kq→approve_kq | 1. Run lifecycle 8 bước (manual triggers thay AT cron). 2. qtht_01 mở FR-10 W1.1, filter entity_id=kh_id. | **STATE**: Backend ghi ≥8 row AUDIT_LOG. **UI**: FR-10 W1.1 lookup → bảng hiển thị ≥8 entries: CREATE, SUBMIT, APPROVE, PUBLISH, START, END, SUBMIT_RESULT, APPROVE_RESULT. Mỗi row: actor (cb_nv/cb_pd), thoi_gian, du_lieu_cu/du_lieu_moi (BR-DATA-05). **PERSIST**: Reload FR-10 → 8 entries giữ; UI immutable (no edit/delete). Note: 2 AUTO_TRANSITION SYSTEM entries verify riêng ở TC-LICH-S-013/014 (DEFER A7). | Edge 🔴 |

---

## J. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-KH-X-043 | FR-III-05 / Cross-module FR-04 cascade | GV (FR-04 TVV) bị VO_HIEU_HOA khi đang dạy KH `DANG_DIEN_RA` | cb_nv_tw_01 + qtht_01. KH "KH-GV-CASCADE" `DANG_DIEN_RA`, GV-001 đang gắn. cb_pd_tw_01 vô hiệu hóa GV-001 (FR-04 UC50). | qtht/cb_pd_tw_01 toggle GV-001 → VO_HIEU_HOA | 1. cb_pd_tw_01 vô hiệu hóa GV-001. 2. cb_nv_tw_01 mở KH-GV-CASCADE. 3. Quan sát Tab Thông tin GV field. | **STATE**: SRS Gap (FR-04 dòng 50 nói "auto gỡ Cổng PLQG khi VO_HIEU_HOA" nhưng FR-03 không quote behavior cho KH đang dạy). Default: KH giữ FK GV (soft FK) + UI cảnh báo "GV đã vô hiệu hóa". KH `DANG_DIEN_RA` không bị block. SPEC-CLARIFY-DT-EC-30. **UI**: GV field hiển thị "[Vô hiệu hóa]" badge bên cạnh tên. **PERSIST**: KH giữ DANG_DIEN_RA. AUDIT_LOG ghi GV vô hiệu hóa nhưng KH không transition. | Cross-module 🔴 |
| TC-KH-E-044 | FR-III-05 / Permission edge / Token still valid | CB_NV_TW bị demote thành QTHT giữa session (token cũ vẫn valid) | cb_nv_tw_01 đăng nhập + đang mở Tab Thông tin KH `DU_THAO`. Admin demote cb_nv_tw_01 role → QTHT. | Admin update role | 1. cb_nv_tw_01 đang giữ form sửa KH. 2. Admin update role qua API. 3. cb_nv_tw_01 click [Lưu]. | **STATE**: BE check role hiện tại từ DB (không trust JWT) → reject với 403. KHÔNG UPDATE. AUDIT_LOG ACCESS_DENIED. **UI**: Toast "Vai trò đã thay đổi, vui lòng đăng nhập lại". **PERSIST**: KH không đổi. SPEC-CLARIFY-DT-EC-31: BE phải re-check role mỗi mutation hay tin token? Best practice là re-check. | Edge 🟡 |
| TC-KH-S-045 | FR-III-05 / SM-KHOAHOC / Race AT-01 + manual | 2 CB_NV_TW cùng [Gửi duyệt] 1 KH `DU_THAO` (race) | cb_nv_tw_01 + cb_nv_tw_02. KH "KH-SUBMIT-RACE" DU_THAO, ≥1 BG. | Cả 2 click [Gửi duyệt] cùng updated_at=T1 | 1. CB-A click T2. 2. CB-B click T3. | **STATE**: CB-A success → CHO_DUYET. CB-B BE check `WHERE updated_at=T1 AND trang_thai='DU_THAO'` → 0 row → reject ERR-SYS-02. **UI**: A toast OK. B toast "KH đã được trình duyệt". **PERSIST**: AUDIT_LOG chỉ 1 SUBMIT entry. CB-A là submitter (notification cb_pd_tw_01 chỉ 1 lần). | Edge 🔴 |

---

## SPEC-CLARIFY tickets (file này)

| ID | Mô tả |
|----|-------|
| SPEC-CLARIFY-DT-21 | Toast message thành công CRUD KH (CREATE/UPDATE/CANCEL) — SRS FR-III-05 không có Error Handling table cho KH operations (chỉ có ERR-KQ-* cho phần kết quả). |
| SPEC-CLARIFY-DT-EC-30 | Cross-module FR-04 cascade — GV bị VO_HIEU_HOA khi đang dạy KH active. Behavior: soft FK warning hay block transition? |
| SPEC-CLARIFY-DT-EC-31 | Permission re-check mỗi mutation — BE phải query role hiện tại từ DB hay trust JWT cache? Best practice security là re-check. |
| SPEC-CLARIFY-DT-22 | Error message nguyên văn cho `so_luong_toi_da` boundary < 1 — SRS dòng 621 chỉ ghi "≥1" không có message. |
| SPEC-CLARIFY-DT-23 | Error message nguyên văn cho hủy KH có HV — SM dòng 631 guard "chưa có HV / chưa diễn ra" nhưng không có nguyên văn. |
| SPEC-CLARIFY-DT-24 | Mã lỗi + nguyên văn cho invalid SM transition (vd: gửi duyệt KH đã DA_DUYET) — SRS không có ERR-KH-INVALID-TRANSITION code. |
| SPEC-CLARIFY-DT-25 | Error message nguyên văn cho hủy KH `DANG_DIEN_RA` — SM dòng 631 ngầm định không cho hủy state này nhưng không có message. |
| SPEC-CLARIFY-DT-26 | BR-EC-01 / ERR-SYS-02 nguyên văn cho optimistic-lock conflict trên KHOA_HOC — SRS Phụ lục B chỉ có code. |
| SPEC-CLARIFY-DT-27 | Hành vi khi công khai KH có `ngay_bat_dau` đã qua — SRS không quy định: cho phép + AT trigger lập tức HAY block với error? |
| SPEC-CLARIFY-DT-28 | Định nghĩa "chưa có HV" trong SM dòng 631 guard hủy — count `DA_DUYET` only hay bao gồm `CHO_DUYET`? Default logic chỉ DA_DUYET + cascade reject CHO_DUYET. |
| SPEC-CLARIFY-DT-29 | Plan overview §2.2 quote "DU_THAO|CHO_DUYET|DA_DUYET → HUY" 3 transition gộp = 3 TC riêng. SRS không phân biệt rõ "rút trình" (CHO_DUYET → HUY) vs "hủy nháp" (DU_THAO → HUY) actor — đều là CB NV theo plan. Cần BA confirm có cần phân biệt button label không. |

---

## Tổng kết file 05

- **32 TC active sau A7** (loại 2 recap TC-KH-N-034/N-035 từ 34) phủ FR-III-05 KH workflow + SM-KHOAHOC 11 transitions + AT-01/AT-02 (manual trigger).
- **9 SPEC-CLARIFY** raise pending BA: DT-21 → DT-29 (DT-01 là spec gap chính từ Plan overview).
- **BR coverage:** BR-AUTH-05/08, BR-DATA-01/03/04/05, BR-FLOW-03/04, BR-NOTIF-01, BR-EC-01.
- **ERR coverage:** ERR-KH-01..05 (TC-009/010/011/014/029) + ERR-PD-01/02 (TC-031/032) + recap section G.
- **SM coverage:** Mọi happy transition trong Plan §2.2 (T1..T12 = 11 transitions + AT-01 manual + AT-02 manual). 5 invalid transitions (TC-029..033). Time-driven AT cross-ref FILE 04 TC-LICH-S-013/014 (DEFER A7).
- **Cross-module:** TC-008 (GV từ FR-04 TU_VAN_VIEN), TC-007 (CTĐT từ chính file 02 chỉ DA_DUYET), AUDIT_LOG verify ở FR-10 W1.1.

---

## A7 Filter Notes

- **LOẠI:** TC-KH-N-034 + TC-KH-N-035 — 2 explicit recap "xem TC-009/014" được A6 flag là acceptable nhưng A7 trim để slim. Coverage không mất (TC-009/014 đã cover ERR-KH-01/04).
- **SỬA:** TC-KH-E-042 — chuyển audit verify từ "Query AUDIT_LOG DB" sang FR-10 W1.1 UI lookup. Note 2 AUTO_TRANSITION entries verify riêng ở file 04 (DEFER).
- **KEEP all others:** Mọi TC khác observable qua UI + network. Permission-edge TC-KH-E-044 (role demote) keep — observable qua "click Lưu sau khi role đổi" → toast 403.
