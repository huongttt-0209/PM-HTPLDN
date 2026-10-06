# Test Cases — FR-IV-01: Quản lý Tư vấn viên (CRUD)

> **SRS Ref**: FR-IV-01, SCR-IV-01 + SCR-IV-02, Entity TU_VAN_VIEN
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:111-210`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-UI-01 | FR-IV-01 / SCR-IV-01 / UI | Verify SCR-IV-01 Danh sách Tư vấn viên (7 tab + 6 filter + table + 2 nút header) | qtht_01 đã đăng nhập | URL `/chuyen-gia-tvv/danh-sach` | 1. Login qtht_01<br>2. Click sidebar "Mạng lưới Tư vấn viên" → "Tư vấn viên / Chuyên gia"<br>3. Verify từng component | **LAYOUT**: Breadcrumb "Trang chủ > Tư vấn viên / Chuyên gia > Danh sách"; Header "Quản lý Tư vấn viên" + 2 nút (+ Thêm tư vấn viên / Xuất Excel với tooltip "Mẫu Phụ lục 1 — QĐ 1322/QĐ-BTP")<br>**TABS (7)**: Đang hoạt động (default), Tạm dừng, Mới đăng ký (chấm đỏ nếu >0), Chờ thẩm định (chấm đỏ nếu >0), Đang thẩm định, Yêu cầu bổ sung, Chờ phê duyệt (ẩn cho QTHT/CB NV; chỉ hiện cho CB PD)<br>**FILTERS (6)**: Ô tìm kiếm (Placeholder "Tìm theo tên, mã tư vấn viên hoặc Căn cước công dân"), Lĩnh vực (multi-select), Đơn vị quản lý (search dropdown), Tổ chức (search dropdown), Trạng thái (multi-select 10 enum, ẩn khi đang ở tab cụ thể), Ngày công nhận từ/đến (date picker)<br>**TABLE columns**: Mã TVV, Họ tên, Loại (TVV/CG badge), Tổ chức chính, Lĩnh vực (tags), Trạng thái (badge SM-TVV — 10 màu theo §3.0), Đơn vị quản lý, Ngày công nhận, Điểm TB (1.0-5.0 hoặc "—/5"), Hành động<br>**NEGATIVE**: KHÔNG có nút "Xóa hàng loạt"; KHÔNG có cột "Địa bàn" (NĐ 77/2008 Đ.19 bỏ). **SPEC-CLARIFY-CGTVV-27**: Nút "Tiếp nhận hồ sơ" header — CHANGELOG D.2.1 ghi OUT (gộp 1 thao tác) NHƯNG SRS body line 1606 vẫn có nút này + MD-TIEP-NHAN. Tester verify thực tế UI và log finding cho BA | Happy 🔴 |
| TC-TVV-UI-02 | FR-IV-01 / SCR-IV-02 / UI | Verify SCR-IV-02 Form Thêm/Sửa Tư vấn viên (5 accordion) | qtht_01 đã đăng nhập | URL `/chuyen-gia-tvv/form` | 1. Click "+ Thêm tư vấn viên" trên SCR-IV-01<br>2. Verify form mở dạng accordion 5 phần | **LAYOUT**: Breadcrumb + Header "Thêm tư vấn viên" + 2 nút footer (Hủy / Lưu)<br>**ACCORDION (5)**: (1) Loại + Ảnh đại diện (radio TVV/CG mặc định TVV; upload ảnh max 5MB jpg/png), (2) Thông tin cá nhân (Họ tên *, CCCD *, Ngày sinh *, Giới tính NAM/NU/KHAC, Email *, SĐT *, Địa chỉ *), (3) Hồ sơ năng lực (Trình độ * Cử nhân/Thạc sĩ/Tiến sĩ/Khác, Chứng chỉ, Số thẻ, Số năm KN, Chức vụ, Nơi công tác), (4) Tổ chức + Lĩnh vực (Tổ chức chính FK TO_CHUC_TU_VAN, Tổ chức đối tác multi N:N, Lĩnh vực * multi ≥1), (5) Phê duyệt + File (Số QĐ công bố, Ngày QĐ, File bằng cấp PDF max 10MB/file tổng 50MB max 10 files, Ghi chú max 5000 ký)<br>**FIELD readonly khi sửa**: ma_tvv (auto), trang_thai (badge), version (hidden)<br>**NEGATIVE**: KHÔNG có ô "Địa bàn" (bỏ theo NĐ 77/2008); KHÔNG có ô "Đơn vị quản lý" cho NHT/CB NV cấp ĐP/BN (auto-set theo current_user.don_vi_id); QTHT mới có dropdown chọn đơn vị | Happy 🔴 |
| TC-TVV-UI-03 | FR-IV-01 / SCR-IV-01 / UI Tab counter | Verify badge số đếm đúng cho 7 tab khi data thay đổi | qtht_01, ≥3 record per state | Seed: 3 MOI_DANG_KY + 2 CHO_THAM_DINH + 1 DANG_THAM_DINH + 1 YEU_CAU_BO_SUNG + 5 HOAT_DONG + 1 TAM_DUNG | 1. Mở SCR-IV-01<br>2. Verify badge số đếm 7 tab<br>3. Tạo 1 TVV mới → verify "Mới đăng ký" tăng +1 | Tab "Đang hoạt động": (5); "Tạm dừng": (1); "Mới đăng ký": (3) chấm đỏ; "Chờ thẩm định": (2) chấm đỏ; "Đang thẩm định": (1); "Yêu cầu bổ sung": (1); "Chờ phê duyệt": ẩn cho QTHT (chỉ hiện CB PD)<br>Sau tạo TVV: "Mới đăng ký" → (4) | Happy 🔴 |

## B. READ / LIST

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-001 | FR-IV-01 / AC1 | CB NV TW xem danh sách TVV thuộc TW | cb_nv_tw_01 đã đăng nhập, ≥5 TVV TW + ≥3 TVV BN + ≥3 TVV ĐP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-IV-01<br>3. Verify danh sách | **STATE**: Query `GET /api/v1/tu-van-vien?don_vi_id=TW&trang_thai=HOAT_DONG&page=1&size=20`<br>**UI**: Hiển thị ≥5 TVV TW (TW xem được toàn bộ theo BR-AUTH-08 ngoại lệ TW); KHÔNG có toast<br>**PERSIST**: Reload → vẫn 5 TVV TW + có thể thấy BN/ĐP (TW ngoại lệ) | Happy 🔴 |
| TC-TVV-002 | FR-IV-01 / BR-AUTH-08 | CB NV ĐP CHỈ xem TVV cùng đơn vị | cb_nv_dp_01 (Sở TP HN) | TVV thuộc HN: 3 record; TVV thuộc HP: 2 record | 1. Login cb_nv_dp_01<br>2. Mở SCR-IV-01<br>3. Verify network request | **STATE**: Query có filter `don_vi_id=current_user.don_vi_id`<br>**UI**: Chỉ hiển thị 3 TVV thuộc HN; 2 TVV HP KHÔNG xuất hiện<br>**PERSIST**: Cố direct URL `/chuyen-gia-tvv/chi-tiet/{tvv_hp_id}` → API trả 403 ERR-AUTH-08 | Negative 🔴 |
| TC-TVV-003 | FR-IV-01 / Tab filter | Switch tab "Đang hoạt động" → "Mới đăng ký" filter trang_thai chính xác | qtht_01, mixed state TVV | — | 1. Mở SCR-IV-01 mặc định Đang hoạt động<br>2. Click tab "Mới đăng ký"<br>3. Verify network request | Network call có param `trang_thai=MOI_DANG_KY,YEU_CAU_BO_SUNG` (theo §3 dòng 197 — Mới đăng ký gộp 2 trạng thái); table chỉ render record có trạng thái này | Happy 🟡 |
| TC-TVV-004 | FR-IV-01 / Pagination BR-DATA-07 | Pagination 20/trang khi >20 record | qtht_01, ≥25 TVV | — | 1. Mở SCR-IV-01 tab "Đang hoạt động"<br>2. Verify pagination UI<br>3. Click trang 2 | Page 1: 20 record; Footer "Hiển thị 1-20 trong tổng 25"; Click "2" → 5 record cuối; Network `?page=2&size=20` | Happy 🟡 |
| TC-TVV-005 | FR-IV-05 / Detail | Click row → mở SCR-IV-03 chi tiết với 5 tab | qtht_01, có TVV `TVV-TW-001` HOAT_DONG | — | 1. Mở SCR-IV-01<br>2. Click row TVV-TW-001 hoặc icon "Xem chi tiết"<br>3. Verify 5 tab | URL chuyển `/chuyen-gia-tvv/chi-tiet/TVV-TW-001`; 5 tab visible: Hồ sơ (default active) / Năng lực / Thẩm định (chỉ visible nếu DANG_THAM_DINH/YEU_CAU_BO_SUNG/CHO_PHE_DUYET) / Lịch sử / Đánh giá; Header có badge trạng thái "Đang hoạt động" xanh lá | Happy 🟡 |

## C. CREATE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-101 | FR-IV-01 / AC2 | Happy path tạo TVV mới đầy đủ field bắt buộc | cb_nv_tw_01 đã đăng nhập, ≥1 Tổ chức TV HOAT_DONG, ≥1 Lĩnh vực PL | Họ tên: "Nguyễn Văn A", CCCD: "001234567890", Email: "a@example.com", SĐT: "0901234567", Địa chỉ: "Hà Nội", Trình độ: "Cử nhân", Tổ chức chính: "Công ty Luật ABC", Lĩnh vực: ["Lao động"], Loại: TVV | 1. Click "+ Thêm tư vấn viên"<br>2. Nhập đủ 5 accordion<br>3. Click "Lưu"<br>4. Verify network request + DB state qua reload list | **STATE**: TU_VAN_VIEN insert mới với `ma_tvv=TVV-TW-{seq}`, `loai_tvv='TVV'`, `trang_thai='MOI_DANG_KY'`, `don_vi_id=current_user.don_vi_id`, `version=0`; TVV_TO_CHUC insert (to_chuc_chinh_id); TVV_LINH_VUC insert junction; AUDIT_LOG insert action=CREATE<br>**UI**: Toast "Thêm tư vấn viên 'Nguyễn Văn A' thành công"<br>**PERSIST**: Reload list tab "Mới đăng ký" → record mới hiển thị; Click row → 5 tab full data; Network response 201 với body `{ma_tvv, trang_thai: "MOI_DANG_KY"}` | Happy 🔴 |
| TC-TVV-102 | FR-IV-01 / E1 | Họ tên trống → ERR-TVV-01 | cb_nv_tw_01 | Họ tên: "" (rỗng) | 1. Mở form Thêm<br>2. Để trống Họ tên<br>3. Click Lưu | **STATE**: KHÔNG insert (count TU_VAN_VIEN trước/sau =)<br>**UI**: Inline error dưới field "Họ tên là bắt buộc" (NGUYÊN VĂN ERR-TVV-01); focus vào field Họ tên; Modal KHÔNG đóng<br>**PERSIST**: KHÔNG có record mới | Negative 🔴 |
| TC-TVV-103 | FR-IV-01 / E2 | CCCD trùng → ERR-TVV-02 | cb_nv_tw_01, đã có TVV với CCCD `001234567890` | CCCD: "001234567890" | 1. Mở form Thêm<br>2. Nhập CCCD trùng + đủ field khác<br>3. Click Lưu | **STATE**: KHÔNG insert<br>**UI**: Toast/inline error "Số Căn cước công dân đã tồn tại" (NGUYÊN VĂN ERR-TVV-02); focus field CCCD<br>**PERSIST**: count TU_VAN_VIEN không đổi | Negative 🔴 |
| TC-TVV-104 | FR-IV-01 / E3 | Email không hợp lệ RFC 5322 → ERR-TVV-03 | cb_nv_tw_01 | Email: "invalid@" | 1. Mở form Thêm<br>2. Nhập Email "invalid@"<br>3. Lưu | **STATE**: KHÔNG insert<br>**UI**: Inline error "Email không hợp lệ" (NGUYÊN VĂN); focus field Email | Negative 🟡 |
| TC-TVV-105 | FR-IV-01 / E4 | Tổ chức chính không tồn tại → ERR-TVV-04 | cb_nv_tw_01 | to_chuc_chinh_id: 99999 (FK invalid) | 1. Mở form Thêm<br>2. Sử dụng DevTools tamper to_chuc_chinh_id thành 99999<br>3. Submit | **STATE**: KHÔNG insert<br>**UI**: Toast "Tổ chức tư vấn không tồn tại" (NGUYÊN VĂN ERR-TVV-04) | Negative 🟡 |
| TC-TVV-106 | FR-IV-01 / E6 | File bằng cấp tổng vượt 50MB → ERR-TVV-06 | cb_nv_tw_01 | 6 file PDF × 9MB = 54MB | 1. Mở form Thêm<br>2. Accordion 5 upload 6 file<br>3. Lưu | **STATE**: KHÔNG insert; KHÔNG upload bất kỳ file nào<br>**UI**: Inline error "Tổng dung lượng file đính kèm tối đa 50MB" (NGUYÊN VĂN ERR-TVV-06) | Negative 🟡 |
| TC-TVV-107 | FR-IV-01 / E7 | Số file vượt 10 → ERR-TVV-07 | cb_nv_tw_01 | 11 file PDF × 1MB | 1. Mở form Thêm<br>2. Upload 11 file<br>3. Lưu | **STATE**: KHÔNG insert<br>**UI**: Inline error "Tối đa 10 file bằng cấp" (NGUYÊN VĂN ERR-TVV-07) | Negative 🟡 |
| TC-TVV-108 | FR-IV-01 / E8 | Virus scan ClamAV phát hiện → ERR-TVV-08 | cb_nv_tw_01 | EICAR test file `eicar.pdf` | 1. Upload file EICAR<br>2. Lưu | **STATE**: KHÔNG insert TU_VAN_VIEN; file bị reject ở backend (FILE_DINH_KEM không insert)<br>**UI**: Toast "File eicar.pdf chứa mã độc, bị từ chối" (NGUYÊN VĂN ERR-TVV-08 với tên file substitution) | Negative 🟡 |
| TC-TVV-109 | FR-IV-01 / E9 | loai_tvv không thuộc enum → ERR-TVV-09 | cb_nv_tw_01 | loai_tvv: "NHT" (đã loại bỏ enum) | 1. DevTools tamper request: `loai_tvv: "NHT"`<br>2. Submit | **STATE**: KHÔNG insert<br>**UI**: API 400 với message "Loại phải là Tư vấn viên/Chuyên gia" (NGUYÊN VĂN ERR-TVV-09) | Negative 🟡 |

## D. UPDATE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-201 | FR-IV-01 / Update | CB NV cùng đơn vị sửa thông tin TVV (chưa duyệt) | cb_nv_tw_01, TVV TVV-TW-005 trạng thái MOI_DANG_KY | Sửa Họ tên: "Nguyễn Văn B (sửa)" | 1. Mở chi tiết TVV-TW-005<br>2. Click "Sửa hồ sơ" tab Hồ sơ<br>3. Sửa Họ tên<br>4. Lưu | **STATE**: TU_VAN_VIEN.ho_ten cập nhật, updated_at + updated_by + version+1; AUDIT_LOG INSERT action=UPDATE diff old→new<br>**UI**: Toast "Cập nhật tư vấn viên thành công"<br>**PERSIST**: Reload chi tiết → "Nguyễn Văn B (sửa)" hiển thị; List → cell Họ tên cập nhật | Happy 🟡 |
| TC-TVV-202 | FR-IV-01 / BR-FLOW-03 | KHÔNG sửa được TVV đã CHO_KICH_HOAT/HOAT_DONG (sau phê duyệt) | cb_nv_tw_01, TVV TVV-TW-010 HOAT_DONG | — | 1. Mở chi tiết TVV-TW-010<br>2. Tab Hồ sơ — verify | Tab Hồ sơ: chỉ hiển thị readonly; KHÔNG có nút "Sửa hồ sơ" trong tab này (chỉ NHT cùng đơn vị mới sửa được qua FR-IV-11 — xem file 10); Action header chỉ có "Tạm dừng / Vô hiệu hóa / Công khai" theo SM-TVV | Happy 🟡 |
| TC-TVV-203 | FR-IV-01 / BR-AUTH-08 | CB NV khác đơn vị KHÔNG sửa được TVV | cb_nv_dp_01 (Sở TP HN), TVV TVV-HP-001 (Sở TP HP) | — | 1. Login cb_nv_dp_01<br>2. Tamper URL `/chuyen-gia-tvv/chi-tiet/TVV-HP-001`<br>3. Cố sửa | API 403 hoặc redirect; KHÔNG có nút Sửa visible | Negative 🟡 |

## E. DELETE (Soft Delete BR-DATA-01)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-301 | FR-IV-01 / Delete soft | Xóa mềm TVV chưa có VV | cb_nv_tw_01, TVV TVV-TW-099 MOI_DANG_KY (chưa có VU_VIEC) | — | 1. Mở chi tiết TVV-TW-099<br>2. Click icon Xóa hàng action<br>3. Modal MD-XOA confirm<br>4. Xác nhận | **STATE**: TU_VAN_VIEN.is_deleted=1, updated_at + updated_by; bản ghi vẫn tồn tại DB; AUDIT_LOG INSERT action=DELETE<br>**UI**: Toast "Xóa thành công"; Modal đóng<br>**PERSIST**: List tab "Mới đăng ký" → KHÔNG còn TVV-TW-099; Filter "Đã xóa" (nếu có) → vẫn truy được | Happy 🟡 |
| TC-TVV-302 | FR-IV-01 / E5 | Xóa TVV đang có VV → ERR-TVV-05 | cb_nv_tw_01, TVV-TW-100 HOAT_DONG có 1 VU_VIEC trạng thái DANG_XU_LY | — | 1. Mở chi tiết TVV-TW-100<br>2. Action Xóa<br>3. Xác nhận modal | **STATE**: KHÔNG xóa (is_deleted vẫn 0)<br>**UI**: Toast "Tư vấn viên đang có vụ việc chưa hoàn thành" (NGUYÊN VĂN ERR-TVV-05) | Negative 🟡 |

## F. PERMISSION + STATE-AWARE actions

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-401 | FR-IV-01 / Action visibility | Action visible khác nhau theo trạng thái TVV | cb_nv_tw_01, đủ TVV per state | — | 1. Mở chi tiết TVV mỗi trạng thái: MOI_DANG_KY, CHO_THAM_DINH, DANG_THAM_DINH, CHO_PHE_DUYET, HOAT_DONG, TAM_DUNG, VO_HIEU_HOA<br>2. Verify nút action header | **MOI_DANG_KY**: Sửa, Xóa (D.2.1 OUT — KHÔNG có "Tiếp nhận hồ sơ" nút riêng)<br>**CHO_THAM_DINH**: Bắt đầu thẩm định (chuyển DANG_THAM_DINH ngầm)<br>**DANG_THAM_DINH**: Yêu cầu bổ sung / Trình duyệt / Từ chối<br>**CHO_PHE_DUYET**: chỉ CB PD thấy Phê duyệt/Từ chối<br>**HOAT_DONG**: Tạm dừng, Vô hiệu hóa, Công khai/Hủy công khai<br>**TAM_DUNG**: Kích hoạt lại, Vô hiệu hóa<br>**VO_HIEU_HOA**: Khôi phục | Happy 🟡 |
| TC-TVV-402 | FR-IV-01 / TVV/CG self-view | TVV đăng nhập chuyên trang chỉ xem được hồ sơ của mình | tvv_01 đã đăng nhập chuyên trang; tvv_01 có hồ sơ TVV-TW-XYZ | — | 1. Login tvv_01<br>2. Truy cập chuyên trang `/chuyen-trang/ho-so-cua-toi`<br>3. Cố truy cập `/chuyen-trang/ho-so/{tvv_other_id}` | Hồ sơ tvv_01: read-only (KHÔNG có nút Sửa); Truy cập hồ sơ TVV khác → 403 hoặc redirect | Negative 🔴 |

---

## G. EDGE bổ sung (A4 inline merge — 7 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-501 | EDGE-A4-a / Concurrency | 2 user cùng tạo TVV CCCD trùng → unique constraint catch race | cb_nv_tw_01 + cb_nv_tw_02 | CCCD chưa có "001234567890" | 1. 2 tab cùng submit Create với CCCD đó | 1 PASS, 1 FAIL ERR-TVV-02 (race protected by DB unique constraint) | Edge 🔴 |
| TC-TVV-502 | EDGE-A4-e / Unicode + emoji | Họ tên Unicode tiếng Việt + emoji | cb_nv_tw_01 | ho_ten: "Nguyễn Văn 🇻🇳" | 1. Submit | DB save UTF-8 đầy đủ; UI render đúng emoji + dấu | Edge 🟡 |
| TC-TVV-503 | EDGE-A4-g / Whitespace trim CCCD | CCCD có leading/trailing whitespace | cb_nv_tw_01 | cmnd_cccd: "  001234567890  " | 1. Submit | Backend trim → save "001234567890"; uniqueness check sau trim | Edge 🟡 |
| TC-TVV-504 | EDGE-A4-h / Whitespace trim email | Email leading/trailing whitespace | cb_nv_tw_01 | email: "  a@b.com  " | 1. Submit | Trim trước RFC validate → PASS | Edge 🟡 |
| TC-TVV-505 | EDGE-A4-k / Filter Đã xóa | Filter "Đã xóa" hiển thị soft-deleted record | qtht_01, có TVV is_deleted=1 | filter_deleted: true | 1. Apply filter "Đã xóa" (nếu có) | Hiển thị soft-deleted record; SPEC-CLARIFY-CGTVV-10 nếu SRS không define filter này | Edge 🟡 |
| TC-TVV-506 | EDGE-A4-l / Restore admin only | Admin restore TVV soft-deleted | qtht_01 (admin), TVV-TW-099 is_deleted=1 | — | 1. Action "Khôi phục" (admin only) | is_deleted=0; AUDIT_LOG action=RESTORE; SPEC-CLARIFY nếu SRS không có chức năng này | Edge 🟡 |
| TC-TVV-507 | EDGE-A4-r / Leap year | Ngày sinh 29/02/2024 (leap year) | cb_nv_tw_01 | ngay_sinh: 2024-02-29 | 1. Submit | DB lưu OK; UI render dd/mm/yyyy "29/02/2024" | Edge 🟡 |

---

## H. A6 fill gap (Traceability matrix forward — 2 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TVV-601 | A6-FILL / BR-DATA-03 explicit | Verify common fields (created_at, created_by, updated_at, updated_by) per record | cb_nv_tw_01 vừa tạo TVV-TW-XYZ | — | 1. Tạo TVV mới<br>2. Reload chi tiết<br>3. Verify metadata fields | TVV record có created_at=NOW, created_by=cb_nv_tw_01.id, updated_at=NOW, updated_by=cb_nv_tw_01.id; sau update field bất kỳ → updated_at=NEW + updated_by=current_user (verify qua API response hoặc admin metadata view) | Happy 🟡 |
| TC-TVV-602 | A6-FILL / BR-LEGAL-04 N:N | Verify N:N TVV ↔ tổ chức (1 TVV thuộc nhiều tổ chức) | cb_nv_tw_01, ≥2 TC TV HOAT_DONG (TC-TW-001 chính + TC-TW-002 đối tác) | to_chuc_chinh_id: TC-TW-001, to_chuc_doi_tac_ids: [TC-TW-002] | 1. Tạo TVV với 2 TC<br>2. Verify list TC liên kết | TVV_TO_CHUC junction có 2 row (chính + đối tác); reload chi tiết TVV tab Hồ sơ hiển thị 2 TC; verify ngược: mở TC-TW-001 hoặc TC-TW-002 → cột "Số TVV liên kết" tăng | Happy 🔴 |

---

**Tổng số TC**: 34 (3 UI + 5 List + 9 Create + 3 Update + 2 Delete + 2 Permission/State + 1 self-view + 7 Edge A4 + 2 A6 fill)
