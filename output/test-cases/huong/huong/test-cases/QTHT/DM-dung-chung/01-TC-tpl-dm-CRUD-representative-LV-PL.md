# Test Cases — UC99: TPL-DM-CRUD Representative qua DM Lĩnh vực Pháp lý (FR-VIII-01)

> **SRS Ref**: FR-VIII-01, SCR-VIII-01 (MH-10.1), Entity DANH_MUC (loai_danh_muc='LINH_VUC_PL')
> **Nguồn**: LOCAL `srs-fr-10-quan-tri-v3.1.md` (lines 56-205, 1444-1496); cross-ref `srs-v3.1.md` Phụ lục B (BR-AUTH-01, BR-DATA-01..07, BR-EC-13)
> **Ngày tạo**: 2026-05-08 (POC convert format mới 2026-05-08)
> **URL**: `/quan-tri/danh-muc` (sub-tab "Lĩnh vực PL")
> **Template áp dụng**: TPL-DM-CRUD (srs-fr-10:58-163)
> **Mục đích**: File này test toàn bộ hành vi TPL-DM-CRUD chung qua DM Lĩnh vực PL như đại diện. 11 DM khác chỉ test smoke 5 TC differences ở file 02.
> **Tổng số TC active**: 56 (58 declared − 2 LOẠI R3) + 1 UI Verification = **57 TC**

---

## A. UI FIELD VERIFICATION

> Section bắt buộc — verify SCR-VIII-01 layout đúng SRS spec TRƯỚC khi chạy chức năng. Nếu UI render sai, các TC chức năng có thể fail không phản ánh bug nghiệp vụ.

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-UI-01 | FR-VIII-01 / SCR-VIII-01 / UI | Verify SCR-VIII-01 layout tab Lĩnh vực PL: 16 components — breadcrumb, sidebar 13 sub-tab, toolbar (Thêm mới + Search), table 6 cột, modal CRUD 6 fields. **Phần tử KHÔNG có:** nút Xóa hàng loạt, nút Export Excel (BR-DATA-06 không expose ở SCR-VIII-01) | qtht_01 đăng nhập, env seed ≥3 record `loai_danh_muc='LINH_VUC_PL'` | URL `/quan-tri/danh-muc/LINH_VUC_PL` | 1. Mở URL trên<br>2. Verify từng component theo SCR-VIII-01 row-by-row<br>3. Hover cột Mô tả nếu có truncate<br>4. Click [+ Thêm mới] → verify modal 6 fields | ▸ **LAYOUT**: Breadcrumb "Trang chủ > Quản trị > Danh mục" (#1, line 1454); sidebar 13 sub-tab (line 1455); toolbar có nút [+ Thêm mới] (#3) + ô search "Tìm theo mã hoặc tên" (#4)<br>▸ **TABLE 6 cột** (line 1458-1463): Mã / Tên / Mô tả (truncate) / Thứ tự / Trạng thái (toggle) / Hành động (Sửa, Xóa)<br>▸ **MODAL CRUD 6 fields** (line 1464-1469): Mã (text required, max 20) / Tên (text required) / Mô tả (textarea optional) / Thứ tự (text default 0) / Trạng thái (toggle default ON) / 2 nút [Hủy] [Đồng ý]<br>▸ **NEGATIVE — KHÔNG có**: nút Xóa hàng loạt, nút Export Excel, cột Ngày tạo/Sửa (BR-DATA-03 verify qua audit log W1.1), cột don_vi_id (BR-DATA-02 ngoại lệ DM hệ thống NULL) | Happy 🔴 |

---

## B. READ / LIST (Render danh sách)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-001 | FR-VIII-01 / SCR-VIII-01 #5-10 | Render bảng 6 cột chuẩn | qtht_01 đăng nhập, sub-tab "Lĩnh vực PL" có ≥3 record seed | (đã seed env) | 1. Mở URL `/quan-tri/danh-muc/LINH_VUC_PL`<br>2. Quan sát table | ▸ **STATE**: GET `/api/v1/danh-muc?loai=LINH_VUC_PL` trả 200, list ≥3 record<br>▸ **UI**: Bảng render 6 cột (Mã, Tên, Mô tả, Thứ tự, Trạng thái toggle, Hành động); badge sub-tab "Lĩnh vực PL" active highlight<br>▸ **PERSIST**: Verify network request qua MCP `list_network_requests` | Happy |
| TC-LV-002 | FR-VIII-01 / BR-DATA-07 (line 85) | Pagination 20/page mặc định | env có ≥21 record LINH_VUC_PL | record 21+ | 1. Mở list<br>2. Scroll xuống pagination footer<br>3. Click "Trang 2" | ▸ **STATE**: GET request `?page=2&size=20` trả record 21+<br>▸ **UI**: Pagination footer hiển thị "Hiển thị 1-20 / N" page 1; click trang 2 → "Hiển thị 21-N / N"<br>▸ **PERSIST**: Trang 2 render record 21+ đúng | Happy |
| TC-LV-003 | FR-VIII-01 / SCR-VIII-01 line 1460 | Truncate cột Mô tả khi text dài | env có ≥1 record với mo_ta >100 ký tự | record có mo_ta="Lorem ipsum..." 150 ký tự | 1. Mở list<br>2. Hover cột Mô tả của record có text dài | ▸ **UI**: Cột Mô tả truncate hiển thị "..." cuối cùng (~100 ký tự đầu)<br>▸ **PERSIST**: Tooltip/hover hiển thị full text 150 ký tự | Happy |
| TC-LV-004 | FR-VIII-01 / BR-DATA-07 (line 2227) | Đổi page size dropdown 20/50/100 | list không rỗng, page size dropdown hiển thị | options: 20, 50, 100 | 1. Mở list<br>2. Click dropdown page size<br>3. Đổi 20 → 50 → 100 | ▸ **STATE**: GET `?size=50` rồi `?size=100` mỗi lần đổi<br>▸ **UI**: List reload theo size mới; pagination cap max 100 — KHÔNG có option > 100<br>▸ **PERSIST**: Số dòng table khớp size selected | Happy |
| TC-LV-005 | FR-VIII-01 / BR-DATA-07 | Boundary 100 rows/page | list page size 100, env có ≥150 record | size=100 | 1. Set page size 100<br>2. Quan sát table + pagination | ▸ **UI**: Table hiển thị 100 dòng trang 1; pagination "Hiển thị 1-100 / 150"<br>▸ **PERSIST**: Click trang 2 → record 101-150 | Happy |
| TC-LV-006 | FR-VIII-01 / line 86 | Sort mặc định thu_tu ASC + ten ASC secondary | list không rỗng, có record cùng thu_tu khác ten | 3 record cùng thu_tu=5, ten "Apple"/"Banana"/"Cherry" | 1. Mở list (KHÔNG click sort)<br>2. Quan sát thứ tự | ▸ **UI**: Records sắp theo thu_tu ASC primary; cùng thu_tu → ten ASC secondary<br>▸ **PERSIST**: 3 record cùng thu_tu=5 hiển thị Apple → Banana → Cherry | Happy |
| TC-LV-007 | FR-VIII-01 / SCR-VIII-01 line 1462 + `[SPEC-CLARIFY-DM-01]` | Empty state khi list rỗng | env không có record LINH_VUC_PL nào (xóa hết hoặc chưa seed) | (empty) | 1. Mở list LV PL | ▸ **STATE**: GET trả 200, data=[]<br>▸ **UI**: Empty state hiển thị thông báo (vd "Không tìm thấy danh mục phù hợp" — text exact `[SPEC-CLARIFY-DM-01]`)<br>▸ **PERSIST**: KHÔNG có row nào trong tbody | Happy |
| TC-LV-008 | FR-VIII-01 / SCR-VIII-01 #1 (line 1454) | Breadcrumb đúng path | list không rỗng | — | 1. Mở list<br>2. Quan sát breadcrumb top page | ▸ **UI**: Breadcrumb nguyên văn "Trang chủ > Quản trị > Danh mục"<br>▸ **PERSIST**: Click "Trang chủ" → navigate /dashboard | Happy |

---

## C. CREATE (Tạo mới)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-009 | FR-VIII-01 / line 89-98 / BR-DATA-05 | Happy path tạo record mới | qtht_01 ở tab "Lĩnh vực PL" active | ma="THUE_TEST", ten="Thuế test", mo_ta="Test", thu_tu=99, trang_thai=Hoạt động | 1. Click [+ Thêm mới] → modal mở<br>2. Nhập đủ 5 fields<br>3. Click [Đồng ý] | ▸ **STATE**: DANH_MUC mới insert với ma="THUE_TEST", loai_danh_muc='LINH_VUC_PL', trang_thai=1, is_deleted=0<br>▸ **UI**: Modal đóng, toast success (`[SPEC-CLARIFY-DM-01]` text); list refresh tự động hiển thị record mới<br>▸ **PERSIST**: AUDIT_LOG action=CREATE, entity=DANH_MUC, ma_ban_ghi=THUE_TEST, user=qtht_01 (cross-ref Nhật ký HT W1.1) | Happy |
| TC-LV-010 | FR-VIII-01 / E3 (line 151) | Reject mã trùng | env có record ma="THUE_TEST" rồi | ma="THUE_TEST" trùng | 1. Click [+ Thêm mới]<br>2. Nhập ma="THUE_TEST"<br>3. Submit | ▸ **STATE**: DB không thêm record mới (count trước/sau =)<br>▸ **UI**: Toast error nguyên văn "Mã 'THUE_TEST' đã tồn tại trong danh mục Lĩnh vực pháp lý" (ERR-DM-01); modal vẫn mở<br>▸ **PERSIST**: Form giữ nguyên data nhập | Negative |
| TC-LV-011 | FR-VIII-01 / E4 (line 152) | Reject tên trống | modal Thêm mới đang mở | ma="TEST_TEN_TRONG", ten="" (rỗng), mo_ta="x" | 1. Nhập ma + mo_ta<br>2. Để trống ten<br>3. Submit | ▸ **STATE**: DB không insert<br>▸ **UI**: Validation error inline ERR-DM-02 nguyên văn "Tên danh mục là bắt buộc"; modal vẫn mở<br>▸ **PERSIST**: Focus về field ten | Negative |
| TC-LV-012 | FR-VIII-01 / line 71 (Y bắt buộc) | Reject mã trống | modal Thêm mới đang mở | ma="", ten="Test" | 1. Nhập ten<br>2. Để trống ma<br>3. Submit | ▸ **STATE**: DB không insert<br>▸ **UI**: Validation error inline "Mã danh mục là bắt buộc"; modal vẫn mở<br>▸ **PERSIST**: Focus về field ma | Negative |
| TC-LV-013 | FR-VIII-01 / E7 (line 155) | Reject mã > 20 ký tự | modal mở | ma=21 ký tự "A" * 21 | 1. Nhập ma 21 ký tự<br>2. Submit | ▸ **STATE**: DB không insert<br>▸ **UI**: Validation ERR-DM-05 nguyên văn "Mã danh mục tối đa 20 ký tự"<br>▸ **PERSIST**: Modal vẫn mở | Negative |
| TC-LV-014 | FR-VIII-01 / line 72 (boundary) | Boundary mã 20 ký tự (on-bound) | modal mở | ma="X" * 20 (đúng 20 ký tự) | 1. Nhập ma 20 ký tự<br>2. Submit | ▸ **STATE**: DB insert thành công<br>▸ **UI**: Toast success<br>▸ **PERSIST**: Record có ma đúng 20 ký tự X | Edge |
| TC-LV-015 | FR-VIII-01 / line 75 (default 0) | Mã thu_tu rỗng → default 0 | modal mở | ma="TEST_TT", ten="Test", thu_tu=(rỗng) | 1. Nhập ma + ten<br>2. Để trống thu_tu<br>3. Submit | ▸ **STATE**: DB insert với thu_tu=0 (default theo TPL)<br>▸ **UI**: Toast success<br>▸ **PERSIST**: List hiển thị thu_tu=0 | Happy |
| TC-LV-016 | FR-VIII-01 / line 76 + 1468 | Toggle default ON khi mở modal | qtht_01 ở tab | (chưa có data) | 1. Click [+ Thêm mới]<br>2. Quan sát toggle Trạng thái | ▸ **UI**: Toggle Trạng thái default ON (Hoạt động)<br>▸ **PERSIST**: Submit không đổi → trang_thai=1 trong DB | Happy |
| TC-LV-017 | FR-VIII-01 / `[SPEC-CLARIFY-DM-13]` | Mã có khoảng trắng | modal mở | ma="THUE_VN ACTIVE" (có space) | 1. Nhập ma có space<br>2. Submit | ▸ **STATE**: Verify behavior thực tế — chấp nhận hay reject?<br>▸ **UI**: Log finding `[SPEC-CLARIFY-DM-13]` về whitelist ký tự<br>▸ **PERSIST**: Spec không nguyên văn — Phase B observe + log GAP | Edge |
| TC-LV-018 | FR-VIII-01 / line 1469 | Hủy modal không tạo record | modal đang mở với data | ma="CANCELED", ten="Test" | 1. Nhập data<br>2. Click [Hủy] | ▸ **STATE**: DB không insert<br>▸ **UI**: Modal đóng<br>▸ **PERSIST**: List không thay đổi (count trước/sau =) | Happy |

---

## D. UPDATE (Cập nhật)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-019 | FR-VIII-01 / line 100-110 / BR-DATA-05 | Happy path sửa tên | record THUE_TEST tồn tại | ten cũ="Thuế test" → ten mới="Thuế (đã sửa)" | 1. Click action Sửa cùng dòng<br>2. Modal Sửa load data hiện tại<br>3. Đổi ten<br>4. Click [Đồng ý] | ▸ **STATE**: DB update ten + updated_at + updated_by<br>▸ **UI**: Modal đóng, toast success<br>▸ **PERSIST**: List refresh ten mới; AUDIT_LOG action=UPDATE diff old="Thuế test" → new="Thuế (đã sửa)" | Happy |
| TC-LV-020 | FR-VIII-01 / line 107 (E3) | Reject đổi mã trùng record khác | record THUE_TEST đang Sửa, env có record khác ma="LAO_DONG" | ma cũ="THUE_TEST" → ma mới="LAO_DONG" (trùng) | 1. Mở Sửa THUE_TEST<br>2. Đổi ma → "LAO_DONG"<br>3. Submit | ▸ **STATE**: DB không update<br>▸ **UI**: Toast error ERR-DM-01 nguyên văn "Mã 'LAO_DONG' đã tồn tại"<br>▸ **PERSIST**: Modal vẫn mở, ma giữ giá trị mới nhập | Negative |
| TC-LV-021 | FR-VIII-01 / line 107 (loại trừ self) | Sửa giữ nguyên ma không reject | record THUE_TEST đang Sửa | ma không đổi="THUE_TEST" | 1. Mở Sửa THUE_TEST<br>2. KHÔNG đổi ma<br>3. Đổi ten/mo_ta<br>4. Submit | ▸ **STATE**: DB update các field khác, ma giữ nguyên<br>▸ **UI**: Toast success (loại trừ chính mình khi check unique)<br>▸ **PERSIST**: Record giữ ma="THUE_TEST", các field khác cập nhật | Happy |
| TC-LV-022 | FR-VIII-01 / E4 | Reject sửa ten trống | record THUE_TEST đang Sửa | ten="" (xóa rỗng) | 1. Mở Sửa<br>2. Xóa hết ten<br>3. Submit | ▸ **STATE**: DB không update<br>▸ **UI**: Validation ERR-DM-02 "Tên danh mục là bắt buộc"<br>▸ **PERSIST**: Modal vẫn mở | Negative |
| TC-LV-023 | FR-VIII-01 / line 1462 | Sửa thu_tu + tắt trạng thái | record THUE_TEST đang Sửa, list có record khác thu_tu cao hơn | thu_tu 99→1, trang_thai ON→OFF | 1. Mở Sửa<br>2. Đổi thu_tu=1<br>3. Toggle trạng_thai OFF<br>4. Submit | ▸ **STATE**: DB update thu_tu=1, trang_thai=0<br>▸ **UI**: Toast success<br>▸ **PERSIST**: List sort lại — record nhảy lên đầu (thu_tu=1 ASC); badge "Không hoạt động" hiển thị | Happy |
| TC-LV-024 | FR-VIII-01 / E6 (line 154) | Reject sửa record đã xóa mềm | record THUE_TEST đã soft delete (is_deleted=1) | URL deeplink `/sua/THUE_TEST` | 1. Truy cập URL deeplink Sửa | ▸ **STATE**: DB không thay đổi<br>▸ **UI**: Error ERR-DM-04 nguyên văn "Bản ghi không tồn tại hoặc đã bị xóa"<br>▸ **PERSIST**: Redirect về list hoặc error page | Negative |
| TC-LV-025 | FR-VIII-01 / line 1469 | Hủy modal Sửa không lưu | record THUE_TEST đang Sửa, đã thay đổi data | đổi ten + click Hủy | 1. Mở Sửa<br>2. Đổi ten<br>3. Click [Hủy] | ▸ **STATE**: DB không update<br>▸ **UI**: Modal đóng<br>▸ **PERSIST**: List giữ data cũ | Happy |
| TC-LV-026 | FR-VIII-01 / BR-DATA-05 / `[SPEC-CLARIFY-DM-28]` | 2 user QTHT đồng thời edit cùng record | qtht_01 + qtht_02 đăng nhập cùng lúc | record THUE_TEST mở Sửa ở 2 session | 1. Cả 2 user mở Sửa cùng record<br>2. User 1 đổi ten + lưu<br>3. User 2 đổi ten khác + lưu | ▸ **STATE**: Verify hành vi: cả 2 user nhận response (success hoặc reject)<br>▸ **UI**: Resolution outcome (overwrite vs lock) không assume — log finding<br>▸ **PERSIST**: AUDIT_LOG có entries cho cả 2 attempts (BR-DATA-05). `[SPEC-CLARIFY-DM-28]` chờ BA quyết định concurrency strategy | Edge |

---

## E. DELETE (Soft delete)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-027 | FR-VIII-01 / line 112-121 / BR-DATA-01, BR-DATA-05 | Happy path soft delete | record THUE_TEST tồn tại, KHÔNG có entity downstream tham chiếu (linh_vuc_id=NULL ở HOI_DAP/VU_VIEC/TVV/CAU_HINH_PHAN_CONG/KHO_CAU_HOI) | THUE_TEST | 1. Click action Xóa cùng dòng<br>2. Modal confirm "Bạn chắc chắn muốn xóa?"<br>3. Click [Đồng ý] | ▸ **STATE**: DB update is_deleted=1 (soft delete)<br>▸ **UI**: Modal đóng, toast success<br>▸ **PERSIST**: Record ẩn khỏi list (refresh — BR-DATA-01 filter is_deleted=0); cross-ref Nhật ký HT W1.1 hiển thị audit entry "Xóa DANH_MUC THUE_TEST" | Happy |
| TC-LV-028 | FR-VIII-01 / E5 (line 153, 200) | Reject xóa khi có HOI_DAP tham chiếu | record THUE_TEST có 5 HOI_DAP.linh_vuc_id tham chiếu | THUE_TEST + 5 HOI_DAP | 1. Click Xóa<br>2. Confirm | ▸ **STATE**: DB không update is_deleted<br>▸ **UI**: Toast error ERR-DM-03 nguyên văn "Không thể xóa. Danh mục đang được sử dụng bởi 5 bản ghi HOI_DAP"<br>▸ **PERSIST**: Record vẫn tồn tại trong list | Negative |
| TC-LV-029 | FR-VIII-01 / line 200 | Reject xóa khi có VU_VIEC tham chiếu | record có VU_VIEC.linh_vuc_id tham chiếu | THUE_TEST + N VU_VIEC | 1. Xóa<br>2. Confirm | ▸ **STATE**: DB không update<br>▸ **UI**: ERR-DM-03 với count entity VU_VIEC<br>▸ **PERSIST**: Record vẫn tồn tại | Negative |
| TC-LV-030 | FR-VIII-01 / line 200 | Reject xóa khi có TVV mapping | record có TVV.linh_vuc_id tham chiếu | THUE_TEST + N TVV mapping | 1. Xóa<br>2. Confirm | ▸ **STATE**: DB không update<br>▸ **UI**: ERR-DM-03 với count entity TVV<br>▸ **PERSIST**: Record vẫn tồn tại | Negative |
| TC-LV-031 | FR-VIII-01 / BR-DATA-01 | Soft-deleted record ẩn khỏi list mặc định | THUE_TEST đã soft delete | is_deleted=1 | 1. Mở lại list LV PL | ▸ **STATE**: GET request `?is_deleted=false` (default filter)<br>▸ **UI**: Record THUE_TEST KHÔNG xuất hiện trong list<br>▸ **PERSIST**: DB vẫn còn record với is_deleted=1 | Happy |
| TC-LV-032 | FR-VIII-01 / line 1469 | Hủy modal confirm xóa | record THUE_TEST | THUE_TEST + click Hủy | 1. Click action Xóa<br>2. Modal confirm hiện<br>3. Click [Hủy] | ▸ **STATE**: DB không thay đổi<br>▸ **UI**: Modal đóng<br>▸ **PERSIST**: Record không bị xóa | Happy |
| TC-LV-033 | FR-VIII-01 / BR-DATA-05 | Verify audit log sau xóa | sau TC-LV-027 thành công | Module="Quản trị", entity="DANH_MUC" | 1. Mở Nhật ký HT (W1.1) `/quan-tri/audit-log`<br>2. Filter Module="Quản trị"<br>3. Tìm entry mã bản ghi="THUE_TEST" | ▸ **STATE**: AUDIT_LOG có row<br>▸ **UI**: Audit entry hiển thị action="Xóa" (DELETE), entity=DANH_MUC, ma_ban_ghi=THUE_TEST, user=qtht_01<br>▸ **PERSIST**: Click expand → JSON diff hiển thị trang_thai cũ + is_deleted change | Happy |

---

## F. SEARCH (Tìm kiếm)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-034 | FR-VIII-01 / line 124-129 | Search substring match ma + ten | list mở, có record ten="Thuế" + "Thuế thu nhập" | keyword="Thuế" | 1. Nhập "Thuế" vào search box<br>2. Wait debounce | ▸ **STATE**: GET `?keyword=Thu%E1%BA%BF`<br>▸ **UI**: List filter còn 2 record matching (substring trên ma hoặc ten)<br>▸ **PERSIST**: Network request chỉ trả 2 record | Happy |
| TC-LV-035 | FR-VIII-01 | Clear search restore full list | search box có keyword "Thuế" | (clear keyword) | 1. Click X clear search box<br>2. Hoặc xóa keyword → empty | ▸ **STATE**: GET `?keyword=` hoặc không có keyword<br>▸ **UI**: List restore full N record<br>▸ **PERSIST**: Pagination reset trang 1 | Happy |
| ~~TC-LV-036~~ | _LOẠI R3_ | _Case-insensitive search là assumption ngoài SRS. BR-EC-13 không nói case-insensitive. Verify behavior thực tế khi Phase B nếu cần (log SPEC-CLARIFY mới)._ | — | — | — | — | _removed_ |
| TC-LV-037 | FR-VIII-01 / `[SPEC-CLARIFY-DM-01]` | No match → empty state | list mở, search box | keyword="ZZZNOMATCH123" | 1. Nhập keyword không có trong env<br>2. Wait | ▸ **STATE**: GET trả data=[]<br>▸ **UI**: List rỗng + empty state "Không tìm thấy danh mục phù hợp" `[SPEC-CLARIFY-DM-01]`<br>▸ **PERSIST**: Pagination "Hiển thị 0-0 / 0" | Happy |
| TC-LV-038 | FR-VIII-01 / BR-EC-13 (line 5471 srs-v3.1) | Sanitize SQL injection | list mở | keyword="' OR 1=1 --" | 1. Nhập SQL injection string<br>2. Wait debounce | ▸ **STATE**: BE escape ký tự đặc biệt; KHÔNG thực thi SQL<br>▸ **UI**: List rỗng (escape) hoặc match literal string<br>▸ **PERSIST**: KHÔNG có data leak; audit không lỗi | Negative |
| TC-LV-039 | FR-VIII-01 / BR-EC-13 | Sanitize XSS | list mở | keyword=`<script>alert(1)</script>` | 1. Nhập XSS payload<br>2. Wait | ▸ **STATE**: BE sanitize<br>▸ **UI**: Hiển thị literal text trong search box; KHÔNG render HTML/JS; KHÔNG có alert popup<br>▸ **PERSIST**: List trả về 0 hoặc match literal | Negative |
| TC-LV-040 | FR-VIII-01 / BR-EC-13 (max 200 ký tự) | Boundary 200 ký tự | list mở | keyword=200 ký tự "a" * 200 | 1. Nhập 200 ký tự<br>2. Submit | ▸ **STATE**: BE chấp nhận, GET với keyword 200 ký tự<br>▸ **UI**: Cho phép submit; result theo full keyword<br>▸ **PERSIST**: List render kết quả | Edge |
| TC-LV-041 | FR-VIII-01 / BR-EC-13 | Boundary 201 ký tự (vượt cap) | list mở | keyword=201 ký tự | 1. Nhập 201 ký tự<br>2. Submit | ▸ **STATE**: BE truncate xuống 200 hoặc reject<br>▸ **UI**: Verify hành vi (FE có maxlength=200?)<br>▸ **PERSIST**: Verify network request keyword length | Edge |

---

## G. TOGGLE TRẠNG THÁI

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-042 | FR-VIII-01 / line 1462 / BR-DATA-05 | Toggle Hoạt động → Không hoạt động | record có trang_thai=1 | THUE_TEST trang_thai=ON | 1. Click toggle column trên list inline | ▸ **STATE**: DB update trang_thai=0<br>▸ **UI**: Toggle chuyển OFF; toast success<br>▸ **PERSIST**: AUDIT_LOG action=UPDATE, diff old=true → new=false | Happy |
| TC-LV-043 | FR-VIII-01 / BR-DATA-05 | Toggle Không hoạt động → Hoạt động | record trang_thai=0 | THUE_TEST trang_thai=OFF | 1. Click toggle | ▸ **STATE**: DB update trang_thai=1<br>▸ **UI**: Toggle chuyển ON; toast<br>▸ **PERSIST**: AUDIT_LOG UPDATE | Happy |
| ~~TC-LV-044~~ | _LOẠI R3_ | _Cross-module behavior (dropdown ở Hỏi đáp), out-of-scope W1.3 DM dùng chung. Test ở module dùng DM (FR-02) nếu cần._ | — | — | — | — | _removed (out-of-scope)_ |

---

## H. PERMISSION (Representative — full matrix file 10)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-045 | FR-VIII-01 / BR-AUTH-01 | QTHT happy path full CRUD | qtht_01 đăng nhập | qtht_01 + URL + CRUD ops | 1. Mở `/quan-tri/danh-muc/LINH_VUC_PL`<br>2. Thực hiện C/R/U/D | ▸ **STATE**: All allow<br>▸ **UI**: Sidebar có "Danh mục dùng chung"; mọi nút CRUD enabled<br>▸ **PERSIST**: Network requests trả 200 | Happy |
| TC-LV-046 | FR-VIII-01 / E1 (line 149) | CB_NV_TW reject 403 | cb_nv_tw_01 đăng nhập | cb_nv_tw_01 + URL trực tiếp | 1. Mở URL `/quan-tri/danh-muc/LINH_VUC_PL` | ▸ **STATE**: Backend trả 403<br>▸ **UI**: Toast/page error ERR-AUTH-01 nguyên văn "Bạn không có quyền thực hiện chức năng này"; sidebar KHÔNG có entry DM<br>▸ **PERSIST**: Redirect về dashboard hoặc error page | Negative |
| TC-LV-047 | FR-VIII-01 / E2 (line 150) / BR-AUTH-06 | Session expired redirect login | qtht_01 đã đăng nhập, idle 30+ phút | (idle timeout) | 1. Đợi 30+ phút idle<br>2. Thử thao tác CRUD | ▸ **STATE**: Backend trả 401<br>▸ **UI**: Redirect `/login` ERR-AUTH-02 + msg "Phiên làm việc hết hạn"<br>▸ **PERSIST**: Sau login lại, có thể tiếp tục thao tác | Negative |

---

## I. EDGE CASES (A4 inline merge)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-EDGE-001 | FR-VIII-01 / E3 (line 151) / BR-DATA-05 | Race condition concurrent CREATE cùng mã | qtht_01 + qtht_02 đăng nhập song song | ma="CONCURRENT_TEST" | 1. Cả 2 user mở [+ Thêm mới]<br>2. Cùng nhập ma="CONCURRENT_TEST"<br>3. User 1 submit thành công<br>4. User 2 submit ngay sau | ▸ **STATE**: DB chỉ 1 record với ma="CONCURRENT_TEST"<br>▸ **UI**: User 2 nhận toast ERR-DM-01 "Mã 'CONCURRENT_TEST' đã tồn tại"<br>▸ **PERSIST**: Refresh list chỉ 1 record; AUDIT_LOG W1.1 chỉ có 1 INSERT entry | Edge |
| TC-LV-EDGE-002 | FR-VIII-01 / line 71-72 / charset UTF-8 | Unicode tiếng Việt có dấu | modal Thêm mới mở | ma="DAO_TAO_BD", ten="Đào tạo / Bồi dưỡng (Tiếng Việt có dấu)" | 1. Nhập data<br>2. Submit | ▸ **STATE**: DB lưu UTF-8 đúng dấu<br>▸ **UI**: Toast success<br>▸ **PERSIST**: List hiển thị đúng dấu Việt + slash | Edge |
| TC-LV-EDGE-003 | FR-VIII-01 / line 71-72 / `[SPEC-CLARIFY-DM-20]` | Whitespace leading/trailing | modal mở | ma=" THUE_WS " (có space đầu/cuối), ten=" Thuế WS " | 1. Nhập data có space<br>2. Submit | ▸ **STATE**: Verify backend trim hay save có space<br>▸ **UI**: Log SPEC-CLARIFY-DM-20<br>▸ **PERSIST**: Phase B observe + log GAP | Edge |
| TC-LV-EDGE-004 | FR-VIII-01 / BR-DATA-01 / line 95 / `[SPEC-CLARIFY-DM-21]` | Soft-deleted + re-create cùng mã | record ma="TEMP_DEL" đã soft delete (is_deleted=1) | ma="TEMP_DEL" tạo lại | 1. Click [+ Thêm mới]<br>2. Nhập ma="TEMP_DEL"<br>3. Submit | ▸ **STATE**: Verify reject (vì soft-deleted vẫn occupy ma) hay cho phép re-create<br>▸ **UI**: Log SPEC-CLARIFY-DM-21<br>▸ **PERSIST**: Phase B observe + log GAP | Edge |
| TC-LV-EDGE-005 | FR-VIII-01 / BR-EC-13 | XSS sanitize trong mo_ta | modal mở | mo_ta=`<script>alert('XSS')</script>` | 1. Nhập payload XSS vào mo_ta<br>2. Submit | ▸ **STATE**: BE sanitize trước khi save<br>▸ **UI**: Cột Mô tả hiển thị literal text; KHÔNG render HTML/JS; KHÔNG có alert popup<br>▸ **PERSIST**: DB lưu sanitized hoặc raw — Phase B verify | Edge |
| TC-LV-EDGE-006 | FR-VIII-01 / BR-EC-13 (line 5471 srs-v3.1) | Search regex special chars escape | search box | keyword="(.*)" hoặc "[A-Z]+" | 1. Nhập regex special chars<br>2. Wait | ▸ **STATE**: BR-EC-13 "escape ký tự đặc biệt truy vấn"<br>▸ **UI**: Search treat as literal; KHÔNG match all (no regex execution)<br>▸ **PERSIST**: List trả kết quả tương ứng keyword literal | Edge |
| TC-LV-EDGE-007 | FR-VIII-01 / BR-DATA-07 | Pagination boundary record 21 | env có 21 record sort thu_tu ASC | size=20 | 1. Mở list page 1<br>2. Click "Trang 2" | ▸ **UI**: Page 1 hiển thị record 1-20; trang 2 chỉ record 21 standalone<br>▸ **PERSIST**: Pagination footer "Hiển thị 1-20 / 21" rồi "21-21 / 21" | Edge |
| TC-LV-EDGE-008 | FR-VIII-01 / line 86 | Sort secondary deterministic | env có 3 record cùng thu_tu=5, ten "Apple"/"Banana"/"Cherry" | (đã seed) | 1. Mở list<br>2. Quan sát thứ tự 3 record cùng thu_tu | ▸ **UI**: Sort thu_tu ASC primary + ten ASC secondary → Apple → Banana → Cherry order<br>▸ **PERSIST**: Refresh list → thứ tự deterministic giữ nguyên | Edge |

---

## J. GAP FILL (A6 test review — trace gap)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|---------------|---------------------------|----------------------|---------------------|-------------------|------|
| TC-LV-FILL-001 | FR-VIII-01 / BR-AUTH-08 ngoại lệ §3.4.3.39 (line 2191) | Verify DM hệ thống NULL don_vi_id không bị scoped | qtht_01 (don_vi=TW), env có DM hệ thống NULL don_vi_id | (env seed) | 1. Mở list LV PL | ▸ **STATE**: GET trả tất cả record DM (KHÔNG filter theo don_vi của user)<br>▸ **UI**: List render đầy đủ tất cả record<br>▸ **PERSIST**: BR-AUTH-08 ngoại lệ DM hệ thống NULL applied — verify network request KHÔNG có param don_vi_id | Happy |
| TC-LV-FILL-002 | FR-VIII-01 / BR-DATA-02 ngoại lệ + BR-DATA-03 | Verify form chi tiết hiển thị fields | qtht_02 vừa tạo record TEST_BR_DATA | TEST_BR_DATA | 1. Click chi tiết hoặc Sửa<br>2. Quan sát form fields | ▸ **UI form chi tiết**: ma/ten/mo_ta/thu_tu/trang_thai luôn hiển thị; created_at + updated_at có thể hiển thị (nếu UI exposed)<br>▸ **NEGATIVE**: KHÔNG có field don_vi_id (DM hệ thống NULL — BR-DATA-02 ngoại lệ)<br>▸ **PERSIST**: Cross-ref Nhật ký HT W1.1 cho `created_by/updated_by/thoi_gian` (BR-DATA-03 verify qua audit log thay vì DDL inspect) | Happy |
| TC-LV-FILL-003 | FR-VIII-01 / BR-DATA-03 / BR-DATA-05 | Verify audit log có 7 common fields | qtht_02 tạo mới record AUDIT_TEST | AUDIT_TEST | 1. Tạo record<br>2. Mở Nhật ký HT W1.1<br>3. Filter entity=DANH_MUC, mã=AUDIT_TEST | ▸ **STATE**: AUDIT_LOG insert 1 row<br>▸ **UI audit entry**: created_by=qtht_02; updated_by=NULL (mới tạo); thoi_gian=đúng; entity=DANH_MUC; ma_ban_ghi=AUDIT_TEST<br>▸ **PERSIST**: 7 common fields được populate (id, created_at, updated_at, created_by, updated_by, is_deleted=0, don_vi_id=NULL ngoại lệ DM) | Happy |

---

**Tổng số TC active:** 56 (58 base sau A4+A6 − 2 LOẠI R3) + 1 UI Verification = **57 TC**

- LOẠI TC-LV-036 (case-insensitive assumption — BR-EC-13 không nói)
- LOẠI TC-LV-044 (dropdown HD cross-module — out-of-scope W1.3)
- REPHRASE TC-LV-026 (last-write-wins → verify behavior + SPEC-CLARIFY-DM-28)
- REPHRASE TC-LV-027 (DB is_deleted → UI list refresh + audit log cross-ref)
- REPHRASE TC-LV-EDGE-001 (DB count → UI list refresh + audit 1 INSERT)
- REPHRASE TC-LV-EDGE-006 (regex escape → BR-EC-13 escape literal)
- REPHRASE TC-LV-FILL-002 (schema → form UI + audit cross-ref BR-DATA-03)

**Phase A done acceptance:** 6 SPEC-CLARIFY tagged (DM-01, DM-13, DM-20, DM-21, DM-28 — sẽ gửi BA Phase B)

**Type breakdown:** Happy 35 / Negative 11 / Edge 11 (Edge bao gồm boundary + edge case + concurrent)
