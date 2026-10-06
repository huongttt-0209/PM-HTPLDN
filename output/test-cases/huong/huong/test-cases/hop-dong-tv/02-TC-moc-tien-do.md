# Test Cases — FR-X.3-01 (UC159): Mốc tiến độ HĐ tư vấn

> **SRS Ref**: FR-X.3-01, SCR-X3-01 row#8 (Accordion "Mốc tiến độ"), Entity HOP_DONG_TU_VAN.moc_tien_do (JSON array)
> **Ngày tạo**: 2026-05-10
> **Đặc thù**: Inline-edit table. Không phê duyệt. Trạng thái mốc 3 giá trị: CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH. Lưu JSON array trong cột entity HĐ.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-X.3-01 / Mốc tiến độ`
- **Pre-conditions mặc định**: cb_nv_tw_01 login, đã có HĐ "HDTV-test-01" (DANG_THUC_HIEN), đang ở Form Sửa.

---

## Trường input (Mốc tiến độ — Accordion 3)

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hop_dong_id | Y (auto) | identifier | FK → HOP_DONG_TU_VAN |
| 2 | ten_moc | Y | text | — |
| 3 | ngay_du_kien | Y | date | — |
| 4 | ngay_thuc_te | N | date | — |
| 5 | trang_thai_moc | Y | enum | CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH (default CHUA_BAT_DAU) |

---

## A. MỐC TIẾN ĐỘ — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-MTD-001 | FR-X.3-01 / Mốc step 5 | Thêm mốc tiến độ — happy | Form Sửa HĐ "HDTV-test-01" mở. | ten_moc="Khảo sát hiện trạng", ngay_du_kien=2026-06-15, trang_thai_moc=CHUA_BAT_DAU | 1. Mở accordion "Mốc tiến độ". 2. Click [+ Thêm mốc]. 3. Inline-edit: nhập 3 trường + Save row. 4. [Lưu] HĐ. | (1) JSON array `moc_tien_do` thêm 1 entry. (2) UI hiển thị mốc mới với badge "Chưa bắt đầu". (3) Audit log UPDATE HĐ (BR-DATA-05). | Happy 🔴 |
| TC-MTD-002 | FR-X.3-01 / Mốc inline-edit | Cập nhật mốc — chuyển trạng thái sang HOAN_THANH | HĐ có mốc "Khảo sát" trạng thái DANG_THUC_HIEN. | trang_thai_moc=HOAN_THANH, ngay_thuc_te=2026-06-20 | 1. Click vào mốc (inline-edit). 2. Đổi trạng_thái + nhập ngày_thực_tế. 3. Save row + [Lưu] HĐ. | (1) JSON array entry update. (2) Badge đổi "Hoàn thành" + ngày_thực_tế lưu. | Happy 🔴 |
| TC-MTD-003 | FR-X.3-01 / Mốc | Xóa 1 mốc tiến độ | HĐ có 3 mốc. | — | 1. Click icon Xóa trên row mốc. 2. Confirm. 3. [Lưu] HĐ. | (1) Mốc bị xóa khỏi JSON array (HĐ còn 2 mốc). (2) Audit log UPDATE. | Happy 🟡 |

---

## B. MỐC TIẾN ĐỘ — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-MTD-010 | FR-X.3-01 / Mốc Inputs#2 | ten_moc trống | Form Sửa HĐ. | ten_moc="" | 1. Thêm mốc bỏ trống tên. 2. Save row. | (1) Inline error "Tên mốc là bắt buộc". (2) Row không save. | Negative 🟡 |
| TC-MTD-011 | FR-X.3-01 / Mốc Inputs#3 | ngay_du_kien trống | Form Sửa HĐ. | ngay_du_kien="" | 1. Thêm mốc bỏ trống ngày dự kiến. 2. Save row. | (1) Inline error "Ngày dự kiến là bắt buộc". | Negative 🟡 |

---

## C. MỐC TIẾN ĐỘ — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|-------------------|------------------|------|
| TC-MTD-020 | FR-X.3-01 / Mốc Inputs#5 | trang_thai_moc default CHUA_BAT_DAU khi tạo | Form Sửa HĐ. | Không touch trạng_thái | 1. Thêm mốc, để mặc định trạng thái. | (1) JSON entry có `trang_thai_moc=CHUA_BAT_DAU`. | Edge 🟢 |
| TC-MTD-021 | FR-X.3-01 / Mốc + ngay_thuc_te | ngay_thuc_te < ngay_du_kien (hoàn thành sớm) | HĐ có mốc DANG_THUC_HIEN, ngay_du_kien=2026-07-01. | ngay_thuc_te=2026-06-25 | 1. Update mốc với ngày thực tế trước ngày dự kiến. 2. Save. | SRS không cấm — phải PASS. UI chỉ display "Hoàn thành sớm 6 ngày" hoặc bình thường. | Edge 🟢 |
| TC-MTD-022 | FR-X.3-01 / Mốc Inputs#5 (A4 merged) | Trạng thái mốc enum invalid — UI restrict | Form Sửa HĐ. | trang_thai_moc="HUY" (không có trong enum) | 1. Cố submit JSON `trang_thai_moc=HUY` qua DevTools API. | (1) BE reject 400: enum value invalid. (2) UI dropdown chỉ có 3 giá trị {CHUA_BAT_DAU, DANG_THUC_HIEN, HOAN_THANH}, không cho nhập tay. | Edge 🟡 |
| TC-MTD-023 | FR-X.3-01 / JSON array order (A4 merged) | Thứ tự mốc tiến độ giữ nguyên sau Save (theo thứ tự nhập) | HĐ có 3 mốc thêm theo thứ tự A→B→C. | — | 1. Lưu HĐ. 2. Reload trang. 3. Xem accordion mốc. | Mốc hiển thị đúng thứ tự A, B, C (không sort theo ngày dự kiến trừ khi user click sort header). | Edge 🟢 |

---

## Tổng kết file 02-TC

- **Tổng số TC: 9** (3 Happy + 2 Negative + 4 Edge — A4 +2)
- **Critical TC (🔴)**: TC-MTD-001, 002
- **A4 merged 2026-05-10**: TC-MTD-022, 023

*Generated 2026-05-10 — Phase A step A3*
