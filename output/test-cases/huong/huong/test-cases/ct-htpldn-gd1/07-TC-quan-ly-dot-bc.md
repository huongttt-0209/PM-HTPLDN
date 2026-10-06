# Test Cases — FR-XI-05a (UC165): Quản lý đợt báo cáo CT HTPLDN — CRUD pure (TAO_DOT)

> **SRS Ref**: FR-XI-05a, SCR-XI-01 Tab "Đợt báo cáo" — bảng đợt + modal tạo/sửa
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: CRUD chỉ khi `trang_thai=TAO_DOT`. CT phải DANG_THUC_HIEN/HOAN_THANH. Validate không trùng đợt (cùng CT + kỳ + khoảng TG). Phân trang 20/page.
> **Scope GĐ1**: CHỈ test transition `[*] → TAO_DOT` (CRUD đợt). Lập BC / Trình duyệt KQ / Phê duyệt / Gửi TW / Tổng hợp **defer GĐ2**.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User CB NV đã login, có quyền "Quản lý đợt báo cáo CT HTPLDN", CT thuộc đơn vị

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | ma_dot | Y (auto) | text | `DOT-{CT_ID}-{SEQ}` |
| 2 | ten_dot | Y | text | — |
| 3 | chuong_trinh_id | Y | identifier | FK → CHUONG_TRINH_HTPL |
| 4 | ky_bao_cao | Y | enum | SO_BO_6_THANG / SO_BO_NAM / TRON_NAM |
| 5 | han_nop | Y | date | Theo deadline TT17/2025 |
| 6 | tu_ngay | Y | date | Kỳ từ ngày |
| 7 | den_ngay | Y | date | Kỳ đến ngày |
| 8 | bieu_mau_su_dung | Y | enum | MAU_21A / MAU_21B / CA_HAI |
| 9 | ghi_chu | N | text (long) | — |

---

## A. CRUD ĐỢT BC — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DOT-BC-001 | FR-XI-05a / Processing step 1-9 | Tạo đợt BC khi CT DANG_THUC_HIEN | cb_nv_tw_01 login. CT-TH08 DANG_THUC_HIEN. | ten="Đợt BC sơ bộ 6T 2026", ky=SO_BO_6_THANG, han_nop="2026-06-20", tu_ngay="2026-01-01", den_ngay="2026-06-30", bieu_mau=MAU_21A | 1. Tab "Đợt báo cáo" CT-TH08. 2. [+ Tạo đợt mới]. 3. Fill modal + Lưu. | (1) POST `/api/v1/dot-bao-cao` 200. (3) Đợt mới `ma_dot=DOT-{CT_TH08_ID}-001`, trạng thái=TAO_DOT. Hiển thị trong bảng. Audit log. | Happy 🔴 |
| TC-DOT-BC-002 | FR-XI-05a / Processing Cập nhật + AC#3 | Sửa đợt khi TAO_DOT | cb_nv_tw_01 login. Đợt DOT-001 trạng thái TAO_DOT. | ten="Đợt BC sơ bộ 6T 2026 (Sửa)" | 1. Click Sửa trên DOT-001. 2. Đổi tên + Lưu. | (1) PUT 200. (3) Tên mới hiển thị. Audit log. | Happy 🟡 |
| TC-DOT-BC-003 | FR-XI-05a / Processing Xóa step 7 + BR-DATA-01 | Xóa mềm đợt khi TAO_DOT | cb_nv_tw_01 login. Đợt DOT-002 TAO_DOT. | — | 1. Click Xóa. 2. Confirm. | (1) DELETE 200, soft delete `is_deleted=1`. (3) Biến mất khỏi DS. Audit log. | Happy 🔴 |
| TC-DOT-BC-004 | FR-XI-05a / AC#1 + BR-DATA-07 | Hiển thị DS đợt phân trang | cb_nv_tw_01 login. CT-TH09 có ≥25 đợt. | — | 1. Mở Tab "Đợt báo cáo" CT-TH09. | (3) DS phân trang 20/page. Cột: Mã đợt / Tên / Kỳ / Biểu mẫu / Khoảng TG / Hạn nộp / Trạng thái / Hành động. | Happy 🟡 |

---

## B. CRUD ĐỢT BC — STATE GUARD

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DOT-BC-005 | FR-XI-05a / Preconditions + E1 ERR-XI-05a-01 | Tạo đợt khi CT ≠ DANG_THUC_HIEN/HOAN_THANH | cb_nv_tw_01 login. CT-DT09 DU_THAO. | — | 1. Mở Tab "Đợt báo cáo". | (1) Nút [+ Tạo đợt mới] ẩn (Tab có thể disabled hoặc hiện info). Force API → reject "Chỉ tạo đợt BC cho CT đang thực hiện hoặc đã hoàn thành" (ERR-XI-05a-01). | Negative 🔴 |
| TC-DOT-BC-006 | FR-XI-05a / E3 ERR-XI-05a-03 | Xóa đợt khi ≠ TAO_DOT | cb_nv_tw_01 login. Đợt DOT-003 trạng thái DANG_LAP_BC. | — | 1. Click Xóa. | (1) Nút Xóa ẩn HOẶC reject "Chỉ xóa đợt BC ở trạng thái Tạo đợt" (ERR-XI-05a-03). | Negative 🔴 |

---

## C. CRUD ĐỢT BC — VALIDATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-DOT-BC-007 | FR-XI-05a / E2 ERR-XI-05a-02 + Processing step 5 | Đợt BC trùng kỳ | cb_nv_tw_01 login. CT-TH10 đã có đợt SO_BO_6_THANG 2026-01-01..2026-06-30 trạng thái TAO_DOT. | ky=SO_BO_6_THANG, tu_ngay="2026-01-01", den_ngay="2026-06-30" | 1. Tạo đợt mới với cùng kỳ + cùng range. | (2) Error "Đã tồn tại đợt báo cáo cho kỳ này" (ERR-XI-05a-02). KHÔNG persist. | Negative 🔴 |
| TC-DOT-BC-008 | FR-XI-05a / Inputs#5 deadline TT17 | han_nop khớp deadline TT17/2025 | cb_nv_tw_01 login. CT-TH11. | ky=SO_BO_6_THANG, han_nop="2026-06-20" (DP/BN: 10/06, TW: 20/06) | 1. Tạo đợt với hạn nộp khớp deadline. | (3) PASS — không cảnh báo deadline. UI có thể hiện info-box deadline. **SPEC-CLARIFY-CT-02**: SRS chưa rõ có validate strict han_nop ≤ deadline TT17 hay chỉ hiển thị info — cần BA. | Edge / SPEC 🟡 |
| TC-DOT-BC-009 | FR-XI-05a / Preconditions (A4 merged) | Tạo đợt khi CT HOAN_THANH (boundary state pre-condition) | cb_nv_tw_01 login. CT-HT01 HOAN_THANH (CT đã đóng đầy đủ đợt cũ). | ky=TRON_NAM, han_nop="2027-01-20", tu_ngay="2026-01-01", den_ngay="2026-12-31", bieu_mau=CA_HAI | 1. Tab Đợt báo cáo CT-HT01. 2. [+ Tạo đợt mới] → fill → Lưu. | (3) PASS — preconditions cho phép HOAN_THANH (per srs-fr-15:631). Đợt mới tạo, trạng thái=TAO_DOT. Lý do: CT đã hoàn thành nhưng vẫn cần tạo đợt BC sau (vd report tròn năm trễ). | Edge 🟡 |
| TC-DOT-BC-010 | FR-XI-05a / Inputs#6-7 (A4 merged) | tu_ngay > den_ngay validation đợt BC | cb_nv_tw_01 login. CT-TH12 DANG_THUC_HIEN. | tu_ngay="2026-12-31", den_ngay="2026-01-01" | 1. Tạo đợt với date range ngược + Lưu. | (2) Validation reject — DatePicker disable selection ngược, hoặc backend reject với inline error "Ngày bắt đầu kỳ phải trước Ngày kết thúc kỳ". KHÔNG persist. | Edge 🟡 |
| TC-DOT-BC-011 | FR-XI-05a / Processing step 6 (Codex 2026-05-09 DOT-001) | Sửa đợt BC khi state ≠ TAO_DOT | cb_nv_tw_01 login. Đợt DOT-005 trạng thái DANG_LAP_BC. | ten_dot="Sửa thử" | 1. Mở Tab "Đợt báo cáo". 2. Click Sửa trên DOT-005. | (1) Nút Sửa ẨN khi đợt đã ngoài TAO_DOT (per srs-fr-15:656 nguyên văn "Chỉnh sửa: chỉ khi trạng thái TAO_DOT"). Force API PUT → reject với error tương đương ERR-XI-05a-03 (xóa) hoặc message phân biệt sửa. **SPEC-CLARIFY-CT-06**: SRS quote rule sửa nhưng KHÔNG quote ERR code riêng cho "sửa sai state" — verify behavior thực tế (có thể reuse ERR-XI-05a-03 hay tạo mới). KHÔNG persist. | Negative 🔴 |
| TC-DOT-BC-012 | FR-XI-05a / Inputs bắt buộc (Codex 2026-05-09 DOT-002) | Tạo đợt thiếu trường bắt buộc — validate mỗi field | cb_nv_tw_01 login. CT-TH13 DANG_THUC_HIEN. | Test 6 case lần lượt thiếu: (a) ten_dot="", (b) ky_bao_cao=null, (c) han_nop=null, (d) tu_ngay=null, (e) den_ngay=null, (f) bieu_mau_su_dung=null | 1. Mở modal Tạo đợt. 2. Bỏ trống 1 trường, fill còn lại đầy đủ. 3. Click Lưu. 4. Lặp 6 lần với 6 case. | (2) Mỗi case: error inline trên field tương ứng "Vui lòng nhập [tên trường]" hoặc tổng hợp "Vui lòng nhập đầy đủ thông tin bắt buộc". Backend reject hoặc client validate trước khi submit. KHÔNG persist (PERSIST: 0 record sau 6 case). **Note:** SRS srs-fr-15:637-645 quote 6 trường bắt buộc Y; AC line 687 "validate + tạo đợt BC". | Negative 🔴 |

---

## Tổng kết file 07-TC

- **12 TC**: 4 Happy + 4 State Guard + 4 Validation/Edge (A3 base 8 + A4 merged 2 + Codex 2026-05-09 +2)
- **Critical TC (🔴)**: 001, 003, 005, 006, 007, 011, 012
- **A4 merged 2026-05-06**: TC-DOT-BC-009, TC-DOT-BC-010
- **Codex review 2026-05-09:**
  - TC-DOT-BC-011 (sửa đợt sai state — fix DOT-001) — SPEC-CLARIFY-CT-06 (ERR code cho sửa sai state).
  - TC-DOT-BC-012 (validate 6 trường bắt buộc — fix DOT-002).

*Generated 2026-05-06 — Phase A step A3 + A4 inline merge · Updated 2026-05-09 sau Codex review*
