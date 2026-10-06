# Test Cases — FR-II-02 + FR-II-05 + FR-II-10 (UC11+UC14+UC19): Tìm kiếm Hỏi đáp

> **SRS Ref**: FR-II-02 (lines 213-271), FR-II-05 (lines 430-465), FR-II-10 (lines 844-882), SCR-II-01 filter-bar rows 12-18
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: 3 search variants share filter UI nhưng khác filter cứng `trang_thai`:
> - **FR-II-02 Tìm kiếm tổng hợp**: KHÔNG filter cứng (toàn bộ trạng thái)
> - **FR-II-05 Đang xử lý**: filter cứng `trang_thai IN (TIEP_NHAN, DANG_XU_LY)` — Tab "Đang xử lý"
> - **FR-II-10 Đã xử lý**: filter cứng `trang_thai IN (DA_DUYET, CONG_KHAI, HOAN_THANH)` — Tab "Hoàn thành"
> Full-text search BR-DATA-08 trên tsvector(noi_dung). AND logic giữa các filter. Pagination BR-DATA-07.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-02|05|10 / {section}`
- **Pre-conditions mặc định**: User đã login, scope theo `don_vi_id` (BR-AUTH-08).

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | keyword | N | text | Full-text search trên `noi_dung`, max 200 ký tự |
| 2 | linh_vuc_id | N | identifier | FK DANH_MUC |
| 3 | tu_ngay | N | date | dd/mm/yyyy |
| 4 | den_ngay | N | date | dd/mm/yyyy, ≥ tu_ngay |
| 5 | trang_thai | N | enum 8 | (FR-II-02 only) MOI/TIEP_NHAN/DANG_XU_LY/CHO_PHE_DUYET/DA_DUYET/CONG_KHAI/HOAN_THANH/HUY |
| 6 | kenh_tiep_nhan | N | enum 5 | DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC/TVN_BRIDGE |
| 7 | muc_do_phuc_tap | N | enum 2 | THUONG/PHUC_TAP (filter row 15a SCR-II-01) |
| 8 | page | N | number | ≥1, default 1 |
| 9 | page_size | N | number | IN (10, 20, 50, 100), default 20 |

---

## A. FR-II-02 TÌM KIẾM TỔNG HỢP — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-001 | FR-II-02 / AC #1 + BR-DATA-08 | Tìm theo keyword full-text | cb_nv_tw_01 login. ≥3 HD chứa "sổ đỏ" trong noi_dung. | keyword="sổ đỏ" | 1. Tab "Tất cả". 2. Nhập keyword vào filter row 12. 3. Click [Tìm kiếm]. | (3) Hiển thị ≥3 records matching. URL chứa `?keyword=sổ+đỏ`. Pagination BR-DATA-07. | Happy 🔴 |
| TC-HDTK-002 | FR-II-02 / AC #2 | Filter Lĩnh vực + Tu_ngay + Den_ngay (AND logic) | cb_nv_tw_01 login. HD ≥5 thuộc Đất đai trong tháng 4/2026. | Lĩnh vực=Đất đai, từ=01/04/2026, đến=30/04/2026 | 1. Apply 3 filters. 2. [Tìm kiếm]. | (3) Kết quả AND logic — chỉ HD Đất đai + ngày_tao ∈ tháng 4. URL `?linh_vuc=...&tu_ngay=2026-04-01&den_ngay=2026-04-30`. | Happy 🔴 |
| TC-HDTK-003 | FR-II-02 / Filter row 15 | Filter Kênh tiếp nhận = TVN_BRIDGE | cb_nv_tw_01 login. ≥2 HD escalate từ TVN. | kenh=TVN_BRIDGE | 1. Dropdown Kênh chọn "Từ Tư vấn nhanh". | (3) Chỉ records có `kenh_tiep_nhan='TVN_BRIDGE'` + `tu_van_nhanh_goc_id NOT NULL`. Cell Kênh hiển thị badge "Từ Tư vấn nhanh" (xanh dương). | Happy 🟡 |
| TC-HDTK-004 | FR-II-02 / Filter row 15a | Filter Mức độ = PHUC_TAP | cb_nv_dp_01 login. ≥3 HD muc_do_phuc_tap=PHUC_TAP. | muc_do_phuc_tap=PHUC_TAP | 1. Dropdown Mức độ chọn "Phức tạp (30 ngày làm việc)". | (3) Chỉ records `muc_do_phuc_tap='PHUC_TAP'`. Cột "Mức độ" hiển thị badge "Phức tạp" (cam). | Happy 🟡 |
| TC-HDTK-005 | FR-II-02 / SCR-II-01 row 18 | Click "Xóa bộ lọc" reset toàn bộ | cb_nv_tw_01 login. Đã apply 3 filters. | — | 1. Click [Xóa bộ lọc]. | (3) URL về `/hoi-dap/danh-sach` (no params). Tất cả filter clear. Bảng full data. | Happy 🟢 |

---

## B. FR-II-05 ĐANG XỬ LÝ (Tab) — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-010 | FR-II-05 / AC #1 + filter cứng | Tab "Đang xử lý" filter cứng IN(TIEP_NHAN, DANG_XU_LY) | cb_nv_tw_01 login. HD seed: 3 MOI + 5 TIEP_NHAN + 7 DANG_XU_LY + 2 CHO_PHE_DUYET. | — | 1. Click tab "Đang xử lý". | (3) Hiển thị 12 records (5+7), KHÔNG hiển thị MOI/CHO_PD. Tab badge "(12)". | Happy 🔴 |
| TC-HDTK-011 | FR-II-05 / AC #2 | Search trong Tab Đang xử lý + linh_vuc filter | cb_nv_tw_01 login. Tab Đang xử lý active, ≥5 HD Đất đai DANG_XU_LY. | keyword="thủ tục", linh_vuc=Đất đai | 1. Apply filter trên tab. 2. Search. | (3) AND logic: kết quả ∩ filter cứng tab. Records `(TIEP_NHAN OR DANG_XU_LY) AND linh_vuc=Đất đai AND keyword match`. | Happy 🟡 |

---

## C. FR-II-10 ĐÃ XỬ LÝ (Tab Hoàn thành) — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-020 | FR-II-10 / AC #1 + filter cứng | Tab "Hoàn thành" filter cứng IN(DA_DUYET, CONG_KHAI, HOAN_THANH) | cb_nv_tw_01 login. HD seed: 4 DA_DUYET + 3 CONG_KHAI + 5 HOAN_THANH + 2 HUY + 6 khác. | — | 1. Click tab "Hoàn thành". | (3) Hiển thị 12 records (4+3+5). HUY hiển thị riêng (theo SRS:1045 tab "Hoàn thành" gộp HOAN_THANH + HUY) → kiểm thực tế: nếu UI hiển thị cả HUY thì 14 records. **Mark SPEC-CLARIFY-HD-01** if discrepancy. | Happy 🔴 |
| TC-HDTK-021 | FR-II-10 / AC + read-only | Read-only — không cho sửa/xóa từ tab | cb_nv_tw_01 login. Tab Hoàn thành. | — | 1. Hover icon Hành động cột 29. | (3) Chỉ icon Xem (mở SCR-II-02). Sửa/Xóa disabled (BR-FLOW-03). | Happy 🟡 |
| TC-HDTK-022 | FR-II-10 / AC date filter | Filter "Đã xử lý" theo ngày duyệt | cb_pd_tw_01 login (vì có cả 2 quyền view). ≥5 HD CONG_KHAI tháng 4/2026. | từ=01/04/2026, đến=30/04/2026, trang_thai=CONG_KHAI | 1. Apply filter. | (3) Records CONG_KHAI có `ngay_duyet ∈ tháng 4`. | Happy 🟡 |

---

## D. NEGATIVE & EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-100 | FR-II-02 / E2 ERR-HD-TK-01 | tu_ngay > den_ngay | cb_nv_tw_01 login. | từ=15/04/2026, đến=10/04/2026 | 1. Nhập từ > đến. 2. Search. | (2) Inline error đỏ dưới date-picker: **"Ngày bắt đầu phải trước ngày kết thúc"** (ERR-HD-TK-01). KHÔNG GET. | Negative 🔴 |
| TC-HDTK-101 | FR-II-02 / E1 INF-HD-TK-01 | Không có kết quả | cb_nv_tw_01 login. | keyword="xyzkhongton" | 1. Search keyword vô nghĩa. | (3) Empty state variant 4: **"Không tìm thấy hỏi đáp phù hợp với bộ lọc. [Xóa bộ lọc]"** (INF-HD-TK-01 message). | Negative 🟡 |
| TC-HDTK-102 | FR-II-10 / E3 ERR-AUTH-TK-01 | Cross-tenant search | cb_nv_dp_02 (BG) login. | keyword chứa từ trong HD-AG | 1. Search. | (3) Empty (BR-AUTH-08 scope BG). KHÔNG hiện HD-AG. | Negative 🟡 |
| TC-HDTK-200 | FR-II-04 / Inputs #2 | Keyword 200 ký (boundary inclusive) | cb_nv_tw_01 login. | keyword=200 ký | 1. Paste 200 ký. 2. Search. | (3) Search OK. | Edge 🟢 |
| TC-HDTK-201 | FR-II-04 / Inputs #2 | Keyword 201 ký (over) | cb_nv_tw_01 login. | keyword=201 ký | 1. Paste 201 ký. | (2) Client truncate ở 200 hoặc reject + toast. **SPEC-CLARIFY-HDTK-02** behavior. | Edge 🟢 |
| TC-HDTK-202 | FR-II-04 / Pagination | page_size=100 (max option) | cb_nv_tw_01 login. ≥150 HD. | page_size=100 | 1. Đổi page_size dropdown. | (3) 100 records/page. Pagination "Hiển thị 1-100 / 150". | Edge 🟢 |
| TC-HDTK-203 | FR-II-02 / SQL injection sanitize | Keyword chứa SQL injection payload | cb_nv_tw_01 login. | keyword="' OR 1=1--" | 1. Paste payload. 2. Search. | (3) Sanitize → search literal "' OR 1=1--". KHÔNG SQL inject. Result empty hoặc match literal. | Edge 🔴 |
| TC-HDTK-204 | FR-II-02 / Unicode | Keyword tiếng Việt có dấu | cb_nv_tw_01 login. ≥2 HD chứa "đất đai". | keyword="đất đai" | 1. Search. | (3) Match đúng records. tsvector hỗ trợ Unicode. | Edge 🟡 |
| TC-HDTK-205 | FR-II-02 / URL state | Reload page giữ filter qua URL | cb_nv_tw_01 login. | URL `?keyword=đất&trang_thai=DANG_XU_LY` | 1. Paste URL. 2. Reload. | (3) Filter pre-fill từ URL params. Search auto-trigger. | Edge 🟢 |

---

---

## E. EDGE BỔ SUNG (A4 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-HDTK-206 | FR-II-02 / Inputs #2 vô hiệu bypass | Filter Lĩnh vực vô hiệu (URL bypass) | cb_nv_tw_01 login. Lĩnh vực "Cổ phần" `is_deleted=1`. | URL `?linh_vuc=Co-phan-vohieu` | 1. Paste URL bypass. | (3) Backend filter records có FK trỏ Lĩnh vực vô hiệu (data cũ). UI tag "(Đã vô hiệu)" trong cột Lĩnh vực. | Edge 🟡 |
| TC-HDTK-207 | FR-II-02 / Inputs #3-4 boundary | tu_ngay = den_ngay (1 ngày exact) | cb_nv_tw_01 login. ≥2 HD tạo ngày 15/04/2026. | từ=15/04/2026, đến=15/04/2026 | 1. Apply filter. | (3) Records có ngay_tao ∈ 15/04/2026 (00:00 - 23:59). | Edge 🟢 |
| TC-HDTK-208 | FR-II-02 / Filter combination ALL | 5 filters đồng thời | cb_nv_tw_01 login. | keyword="luật" + linh_vuc=Đất đai + tu/den ngày + trang_thai=DANG_XU_LY + kenh=DVC + muc_do_phuc_tap=THUONG | 1. Apply 5 filters. | (3) AND logic strict. URL chứa toàn bộ params. Có thể empty result nếu không HD nào match all. | Edge 🟢 |
| TC-HDTK-209 | FR-II-02 / Unicode NFC vs NFD | Tiếng Việt 2 cách encode (NFC vs NFD) | cb_nv_tw_01 login. HD chứa "đất" encode NFC. | keyword="đất" encode NFD | 1. Search NFD form. | (3) Backend normalize tsvector → match NFC + NFD. Verify Vietnamese collation rule. Hoặc fail (chỉ NFC) → SPEC-CLARIFY. | Edge 🟡 |

---

## Tổng kết file 02

- **Tổng số TC: 22** (5 FR-II-02 happy + 2 FR-II-05 + 3 FR-II-10 + 8 negative/edge + 4 A4 merged)
- **Critical TC (🔴)**: TC-HDTK-001, 002, 010, 020, 100, 203
- **Coverage**: BR-AUTH-08, BR-DATA-07, BR-DATA-08, 3 search variants với filter cứng đặc thù
- **Error codes**: ERR-HD-TK-01/02, ERR-AUTH-TK-01, INF-HD-TK-01/02/03
- **SPEC-CLARIFY**: HD-01 (HUY trong tab Hoàn thành?), HDTK-02 (keyword >200 ký truncate vs reject)

*Generated 2026-05-10 — Phase A step A3*
