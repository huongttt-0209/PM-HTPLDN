# Test Cases — FR-IV-02: Tìm kiếm Tư vấn viên + Xuất Phụ lục 1 BTP

> **SRS Ref**: FR-IV-02, SCR-IV-01 (filter), Entity TU_VAN_VIEN
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:212-272`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TIMKIEM-UI-01 | FR-IV-02 / SCR-IV-01 / UI Filter Bar | Verify thanh filter 6 trường + nút Xuất Excel | qtht_01 đã đăng nhập | URL `/chuyen-gia-tvv/danh-sach` | 1. Mở SCR-IV-01<br>2. Verify từng filter component | **FILTERS (6)**: (1) Ô tìm kiếm (Placeholder "Tìm theo tên, mã tư vấn viên hoặc Căn cước công dân"), (2) Lĩnh vực (multi-select dropdown), (3) Đơn vị quản lý (search dropdown — KHÔNG còn "Địa bàn" theo NĐ 77/2008 Đ.19), (4) Tổ chức (search dropdown), (5) Trạng thái (multi-select 10 enum SM-TVV — ẩn khi tab cụ thể), (6) Ngày công nhận từ/đến (date range picker)<br>**EXPORT**: Nút "Xuất Excel" header tooltip "Mẫu Phụ lục 1 — QĐ 1322/QĐ-BTP" (10 cột cố định) | Happy 🔴 |

## B. SEARCH (single filter)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TIMKIEM-001 | FR-IV-02 / AC1 | Tìm theo từ khóa Họ tên | qtht_01, có TVV "Nguyễn Văn A" + "Trần Thị B" + "Lê Văn C" | tu_khoa: "Nguyễn" | 1. Mở SCR-IV-01<br>2. Nhập "Nguyễn" vào ô tìm kiếm<br>3. Wait debounce ~300ms | **STATE**: Network call `GET /api/v1/tu-van-vien?tu_khoa=Nguyễn&don_vi_id=...&page=1`<br>**UI**: Table chỉ hiển thị "Nguyễn Văn A"; pagination total=1; KHÔNG toast<br>**PERSIST**: Reload với URL có `?tu_khoa=Nguyễn` → vẫn lọc đúng | Happy 🔴 |
| TC-TIMKIEM-002 | FR-IV-02 / Search by ma_tvv | Tìm theo mã TVV | qtht_01, TVV-TW-005 tồn tại | tu_khoa: "TVV-TW-005" | 1. Nhập "TVV-TW-005"<br>2. Verify | Table 1 record TVV-TW-005 | Happy 🟡 |
| TC-TIMKIEM-003 | FR-IV-02 / Search by CCCD | Tìm theo CCCD | qtht_01, TVV CCCD 001234567890 | tu_khoa: "001234567890" | 1. Nhập CCCD đầy đủ<br>2. Verify | Table 1 record TVV có CCCD này | Happy 🟡 |
| TC-TIMKIEM-004 | FR-IV-02 / Search empty | Tìm với từ khóa rỗng → trả full list | qtht_01, ≥5 TVV | tu_khoa: "" | 1. Xóa ô tìm kiếm<br>2. Verify | Trở về list mặc định 20/trang theo BR-DATA-07 | Happy 🟡 |
| TC-TIMKIEM-005 | FR-IV-02 / E1 | Không có kết quả → INF-TVV-01 | qtht_01 | tu_khoa: "ZZZZ-not-exists" | 1. Nhập "ZZZZ-not-exists"<br>2. Verify | **STATE**: Network response `{data: [], total: 0}`<br>**UI**: Empty state "Không tìm thấy tư vấn viên phù hợp" (NGUYÊN VĂN INF-TVV-01); KHÔNG toast | Negative 🟡 |

## C. SEARCH (multi-filter AND)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TIMKIEM-101 | FR-IV-02 / AC2 | Filter Lĩnh vực + Trạng thái (AND) | qtht_01, ≥3 TVV LV "Lao động" HOAT_DONG + 2 TVV LV "Thuế" TAM_DUNG | linh_vuc_ids: ["Lao động"], trang_thai: ["HOAT_DONG"] | 1. Click filter Lĩnh vực chọn "Lao động"<br>2. Click filter Trạng thái chọn "Đang hoạt động"<br>3. Verify | Network `?linh_vuc_ids=Lao động&trang_thai=HOAT_DONG`; Table 3 record (AND logic — chỉ HOAT_DONG VÀ LV Lao động) | Happy 🔴 |
| TC-TIMKIEM-102 | FR-IV-02 / Filter Đơn vị | Filter Đơn vị quản lý (cây 2 tầng TW/BN/ĐP) | qtht_01, TVV thuộc Sở TP HN/HP/Bộ TP | don_vi_id: "Sở TP HN" | 1. Click filter Đơn vị, search "Hà Nội"<br>2. Chọn "Sở Tư pháp Hà Nội"<br>3. Verify | Table chỉ TVV thuộc Sở TP HN; cb_nv_dp_01 (HN) sẽ thấy filter Đơn vị disabled/auto-set HN (BR-AUTH-08) | Happy 🟡 |
| TC-TIMKIEM-103 | FR-IV-02 / Filter Tổ chức | Filter Tổ chức tư vấn | qtht_01, TVV thuộc "Công ty Luật ABC" | to_chuc_id: "Công ty Luật ABC" | 1. Filter Tổ chức search "ABC"<br>2. Verify | Table chỉ TVV có to_chuc_chinh_id = ABC | Happy 🟡 |
| TC-TIMKIEM-104 | FR-IV-02 / Filter Ngày công nhận | Filter Ngày từ-đến | qtht_01, TVV ngày công nhận: 2026-01-15, 2026-03-20, 2026-05-01 | tu_ngay: "2026-01-01", den_ngay: "2026-04-30" | 1. Pick range 01/01-30/04<br>2. Verify | Table 2 record (15/01 + 20/03), 01/05 KHÔNG hiển thị (boundary EXCLUSIVE den_ngay+1) | Happy 🟡 |
| TC-TIMKIEM-105 | FR-IV-02 / Combine 4 filter | Combine 4 filter cùng lúc (AND) | qtht_01, data đa dạng | tu_khoa+linh_vuc+don_vi+trang_thai | 1. Set 4 filter cùng lúc<br>2. Verify | Network có đủ 4 param; Table chỉ record match TẤT CẢ điều kiện | Happy 🟡 |

## D. EXPORT Phụ lục 1 BTP (Excel 10 cột)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TIMKIEM-201 | FR-IV-02 / Export PL1 BTP | Xuất Excel theo Phụ lục 1 — QĐ 1322/QĐ-BTP | qtht_01, ≥10 TVV thỏa filter hiện tại | Filter: Lĩnh vực Lao động + Trạng thái HOAT_DONG | 1. Apply filter<br>2. Click "Xuất Excel"<br>3. Verify file tải xuống | **STATE**: Network `GET /api/v1/tu-van-vien/export-pl1?linh_vuc_ids=Lao động&trang_thai=HOAT_DONG`; response Content-Type `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`<br>**UI**: Toast "Xuất Excel thành công"; File tự download<br>**PERSIST**: Mở file Excel — header chứa **10 cột Phụ lục 1**: STT / Họ tên / Năm sinh / Thông tin liên hệ (SĐT, địa chỉ, email gộp 1 cell) / Chức danh vị trí / Trình độ chuyên môn + số văn bằng / Chứng chỉ (tên + ngày cấp) / Lĩnh vực chuyên ngành / Kinh nghiệm (số năm + mô tả) / Ghi chú; Số dòng = số record sau filter (chỉ HOAT_DONG + LV Lao động) | Happy 🔴 |
| TC-TIMKIEM-202 | FR-IV-02 / WRN-TVV-01 | Export khi >10K rows → cảnh báo | qtht_01, có ≥10001 TVV | filter no-op | 1. Click "Xuất Excel"<br>2. Verify warning | **UI**: Modal/Toast cảnh báo "WRN-TVV-01: Export tối đa 10.000 dòng — vui lòng thu hẹp filter"; KHÔNG xuất file đầy đủ; SPEC-CLARIFY-CGTVV-01 nếu SRS không định nghĩa rõ message | Edge 🟡 |

---

## E. EDGE bổ sung (A4 inline merge — 7 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-TIMKIEM-301 | EDGE-A4-m / SQL injection | Tìm với SQL injection payload | qtht_01 | tu_khoa: `'; DROP TABLE TU_VAN_VIEN--` | 1. Nhập payload<br>2. Submit | Sanitize PASS — query parameterized; KHÔNG execute SQL; trả empty INF-TVV-01 (không match record nào) | Edge 🔴 |
| TC-TIMKIEM-302 | EDGE-A4-k / Filter Đã xóa | Filter hiển thị soft-deleted (admin) | qtht_01 | filter_deleted: true | 1. Apply filter | Hiển thị TVV is_deleted=1; SPEC-CLARIFY nếu SRS không define | Edge 🟡 |
| TC-TIMKIEM-303 | EDGE-A4-n / Page boundary | Pagination page=0 hoặc page=99999 | qtht_01 | page=0 | 1. Tamper URL `?page=0` | Backend default page=1 hoặc 400 invalid; KHÔNG crash | Edge 🟡 |
| TC-TIMKIEM-304 | EDGE-A4-o / Sort secondary | Sort cùng created_at → tie-breaker by id DESC | qtht_01, 5 TVV created cùng giây | — | 1. Sort default<br>2. Verify order | Sort by ngay_cong_nhan DESC → tie by id DESC (consistent ordering); SPEC-CLARIFY-CGTVV-11 nếu SRS không quy định sort default | Edge 🟡 |
| TC-TIMKIEM-305 | EDGE-A4-p / Timezone UTC+7 | Date filter boundary timezone | qtht_01, TVV ngay_cong_nhan: 2026-05-08 23:59:00 +0700 | tu_ngay: 2026-05-09 | 1. Filter từ 09/05<br>2. Verify | TVV 23:59:00 ngày 08/05 KHÔNG xuất hiện (vì tu_ngay BẮT ĐẦU 00:00 09/05); boundary EXCLUSIVE | Edge 🟡 |
| TC-TIMKIEM-306 | EDGE-A4-q / Reversed date range | tu_ngay > den_ngay → reject | qtht_01 | tu_ngay: 2026-05-09, den_ngay: 2026-05-01 | 1. Pick reversed range | Inline error "Từ ngày phải nhỏ hơn hoặc bằng Đến ngày"; SPEC-CLARIFY nếu SRS không có ERR code | Edge 🟡 |
| TC-TIMKIEM-307 | EDGE-A4-jj / Export 0 record | Export PL1 với 0 record sau filter | qtht_01 | filter no-match | 1. Click Xuất Excel | File Excel có header 10 cột Phụ lục 1 nhưng 0 row data; toast "Không có dữ liệu để xuất" hoặc cho phép tải file rỗng | Edge 🟡 |

---

**Tổng số TC**: 19 (1 UI + 5 Search single + 5 Search combo + 2 Export + 7 Edge A4) — A6 sẽ điều chỉnh
