# TC FR-VI-02 — Thiết lập tiêu chí đánh giá (UC84) — Tab 1

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-02 (line 161-228) + §3 Tab 1 (line 831-841)
> **SCR:** SCR-VI-01 — Phần B Tab 1 Tiêu chí
> **Actor chính:** CB Nghiệp vụ — `cb_nv_*_01`
> **Entity:** TIEU_CHI_DANH_GIA (DM dùng chung FR-10) + per-đợt overrides
> **BR core:** BR-CALC-04 (tổng trọng số = 100%)
> **Total TC:** 10

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-TC-001 | Mở Tab Tiêu chí — bảng inline editable | Login `cb_nv_tw_01`. Đợt LAP_KE_HOACH (DG-20260502-0001). | 1. Mở chi tiết đợt<br>2. Tab "Tiêu chí" | Tab hiển thị bảng cột: STT / Tên tiêu chí / Mô tả / Trọng số % / Điểm tối đa / Thứ tự / Hành động. Header info card hiển thị mã đợt + kỳ + đối tượng | High | SCR row #28-29 |
| TC-DG-TC-002 | Thêm tiêu chí mới — happy path | Login. Tab Tiêu chí mở. | 1. Click [+ Thêm tiêu chí]<br>2. Nhập: ten_tieu_chi="Mức độ hoàn thành VV", trong_so=40, diem_toi_da=10, thu_tu=1<br>3. Lưu | Bảng có row mới. Realtime "Tổng trọng số: 40%" — màu đỏ (chưa = 100%) | Critical | UC84 happy, BR-CALC-04 partial |
| TC-DG-TC-003 | Thêm đủ 4 tiêu chí — tổng 100% | Login. | 1. Thêm 4 tiêu chí: 40% + 30% + 20% + 10% = 100% | Tổng trọng số "100%" — màu xanh lá. Banner cảnh báo `WRN-TC-01` ẩn | Critical | BR-CALC-04, ERR-DG-TC-01 negative case |
| TC-DG-TC-004 | Cảnh báo realtime khi `SUM != 100%` | Login. Tổng đang = 100%. | 1. Sửa trong_so tiêu chí 1 từ 40 → 50 | Tổng "110%" — màu đỏ. Banner WRN-TC-01 hiển thị "Tổng trọng số hiện tại: 110%. Cần đảm bảo = 100%" | High | SCR row #30-31, ERR-DG-TC-01 |
| TC-DG-TC-005 | Lưu khi `SUM != 100%` — cho phép lưu nhưng chặn khi trình duyệt | Login. Tổng = 110%. | 1. Click [Lưu]<br>2. Sau đó thử Trình duyệt PC từ Tab 2 | Lưu OK với cảnh báo. Khi Trình duyệt → block + ERR-DG-TC-01 "Tổng trọng số phải bằng 100%" | High | AC §3.7 quy tắc, ERR-DG-TC-01 |
| TC-DG-TC-006 | Sửa tên tiêu chí inline | Login. ≥1 tiêu chí. | 1. Click ô ten_tieu_chi<br>2. Đổi text<br>3. Tab/Enter | Cập nhật ngay. Toast nhỏ "Đã lưu" | Medium | SCR row #29 inline edit |
| TC-DG-TC-007 | Xóa tiêu chí | Login. | 1. Click icon Xóa hàng tiêu chí<br>2. Confirm | Tiêu chí biến mất. Tổng trọng số recalculate | High | UC84 |
| TC-DG-TC-008 | Drag & drop reorder thứ tự | Login. ≥3 tiêu chí. | 1. Drag tiêu chí #3 lên #1 | `thu_tu` cập nhật. STT bảng renumber 1-2-3 | Low | SCR row #29 (drag & drop) |
| TC-DG-TC-009 | Validate `diem_toi_da <= 0` → ERR-DG-TC-03 | Login. | 1. Thêm tiêu chí với diem_toi_da=0 | Inline error "Điểm tối đa phải lớn hơn 0" (ERR-DG-TC-03) | High | ERR-DG-TC-03 |
| TC-DG-TC-010 | Tham chiếu DM tiêu chí UC109 | Login. | 1. Click [Nhập từ danh mục]<br>2. Popup multi-select hiển thị | Popup load DM TIEU_CHI_DANH_GIA `KICH_HOAT` nhóm `HIEU_QUA_HTPL`. Chọn → bảng cập nhật | Medium | SCR row #32-33 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-TC-011 | Boundary `trong_so` = 100% với 1 tiêu chí duy nhất | Login. | 1. Thêm 1 tiêu chí trong_so=100<br>2. Verify tổng | Tổng = 100%. Cho phép trình duyệt | Low | BR-CALC-04 boundary |
| TC-DG-TC-012 | `trong_so` 101 → block | Login. | 1. Nhập trong_so=101 | Inline error "Trọng số phải từ 1-100" | Medium | UC84 input #4 1-100 |
| TC-DG-TC-013 | Tolerance ±0.01% per BR-CALC-04 ERR-DG-TC-01 | Login. Tổng = 99.99% (decimal). | 1. Trình duyệt PC | Cho phép trình (tolerance ±0.01%) per ERR-DG-TC-01 | Medium | ERR-DG-TC-01 tolerance |
| TC-DG-TC-014 | Boundary `ten_tieu_chi` 500 ký tự | Login. | 1. Nhập ten_tieu_chi 500 chars | Lưu OK | Low | UC84 input #2 max 500 |
| TC-DG-TC-015 | XSS payload trong `mo_ta` | Login. | 1. Nhập mo_ta = `<img src=x onerror=alert(1)>` | Lưu literal text. KHÔNG execute | High | Security baseline |
| TC-DG-TC-016 | Số thập phân `trong_so` 33.33 + 33.33 + 33.34 = 100 | Login. | 1. Nhập 3 tiêu chí decimal trọng số | Tổng = 100.00. Cho phép trình | Medium | BR-CALC-04 floating |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-TC-017 | Thiếu `ten_tieu_chi` khi lưu → ERR-DG-TC-02 (P0 F-001) | Login. Tab Tiêu chí mở. | 1. Click [+ Thêm tiêu chí]<br>2. Để trống `ten_tieu_chi`, nhập trong_so=10, diem_toi_da=5<br>3. Save | Inline error + toast NGUYÊN VĂN "Vui lòng nhập tên tiêu chí" (ERR-DG-TC-02) | Critical | ERR-DG-TC-02, AC E2 |
| TC-DG-TC-018 | `diem_toi_da` integer constraint — decimal/negative (P2 F-025) | Login. | 1. Nhập diem_toi_da=10.5<br>2. Save<br>3. Nhập diem_toi_da=-1<br>4. Save | Cả 2 reject. Inline error "Điểm tối đa phải là số nguyên dương" hoặc ERR-DG-TC-03 NGUYÊN VĂN "Điểm tối đa phải lớn hơn 0" cho âm | Medium | UC84 input #5 ràng buộc số nguyên dương |
| TC-DG-TC-019 | `thu_tu` validation — duplicate hoặc trống (P2 F-026) | Login. ≥2 tiêu chí. | 1. Sửa thu_tu của 2 tiêu chí cùng = 1<br>2. Save<br>3. Để thu_tu trống | Duplicate: cảnh báo "Thứ tự bị trùng" hoặc auto re-number. Trống: inline error required hoặc auto-fill kế tiếp | Low | UC84 input #6 ràng buộc bắt buộc |

## Tổng số TC: 19 (10 base + 6 edge A4 + 3 Codex apply)

> **A4 done 2026-05-10** — 6 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
