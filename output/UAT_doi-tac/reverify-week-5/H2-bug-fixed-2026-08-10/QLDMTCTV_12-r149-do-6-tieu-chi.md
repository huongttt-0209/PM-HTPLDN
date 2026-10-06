# QLDMTCTV_12 (sheet `bug` row 149) — đo đủ 8 bước / 6 tiêu chí PASS

- Môi trường: https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: `cbnv_tw_03` (CB Nghiệp vụ Trung ương, Cục Bổ trợ tư pháp - Bộ Tư pháp) — đúng Precondition
- Bản ghi: `TC-TW-DEMO-001` "Công ty Luật TNHH Demo Kiểm Thử" (cùng đơn vị) + `TVV-BTP-TW-0002`
- Thời điểm: 2026-08-10 ~21:16–21:22

| Tiêu chí | Đo được | Kết |
|---|---|---|
| (a) 5.000 ký tự lưu được, đọc lại ĐỦ 5.000 | Lưu thành công → `Tạm dừng`. Tab Lịch sử: chuỗi dài **đúng 5000** ký tự | ✅ |
| (b) dán 8.000 giữ nguyên 8.000, không tự cắt | `textarea.value.length = 8000`, thuộc tính `maxlength` = **null** (không chặn cứng 1.000) | ✅ |
| (c) bộ đếm `{n}/5000` + cảnh báo khi n > 5000 | `0/5000` → `5000/5000` → `8000/5000` → `5001/5000`; vượt mốc hiện dòng chữ đỏ `rgb(245,34,45)` | ✅ |
| (d) 5.001 và 9 ký tự đều KHÔNG lưu được VÀ có câu báo tại ô | 5001 → "Lý do thay đổi tối đa 5.000 ký tự"; 9 → "Lý do thay đổi là bắt buộc (≥ 10 ký tự)". Bấm xác nhận: **0 request**, hộp thoại không đóng | ✅ |
| (e) máy chủ từ chối 5.001 bằng mã lỗi riêng của chức năng | Tổ chức: `POST /to-chuc-tu-vans/{id}/cap-nhat-trang-thai` → **422 `ERR-TT-TC-03`** field `lyDo`. Tư vấn viên: → **422 `ERR-VAL-IV-TT-03`** field `lyDo`. Không phải mã hệ thống chung `ERR-SYS-*`. Trạng thái KHÔNG đổi | ✅ |
| (f) cả hai màn cùng hành vi | Màn Chi tiết Tư vấn viên: dán 8000 giữ 8000 · đếm `8000/5000` · chữ đỏ · bấm Xác nhận ở 5001 và 9 đều bị chặn tại ô, 0 request · dán 5000 lưu được | ✅ |

**Schema máy chủ (đọc `/api/docs-json`)** — cả 2 chức năng khai `lyDo: {minLength: 10, maxLength: 5000}`:
`CapNhatTrangThaiTctvDto` (Tổ chức) và DTO tương ứng của Tư vấn viên.

## Bẫy đã tôn trọng

- **Bẫy 1** — Thẻ Thao tác của `TC-TW-DEMO-001` hiện đủ **4 mục** (Chỉnh sửa · Cập nhật trạng thái · Công khai · Xóa) khi đo bằng CB Nghiệp vụ CÙNG đơn vị → KHÔNG log lại "Màn hình không có nút chức năng".
- **Bẫy 2** — chỉ đo "có câu báo tại ô + chặn được nút", không bắt bẻ câu chữ.
- **Bẫy 3** — dropdown "Trạng thái mới" lọc theo trạng thái hiện tại: `Đang hoạt động` → `Tạm dừng` + `Vô hiệu hóa`; `Tạm dừng` → `Đang hoạt động` + `Vô hiệu hóa`. ĐÚNG, không báo thiếu lựa chọn.
- **Bẫy 4** — ngoài việc làm mờ nút, đã có THÊM dòng chữ đỏ tại ô ở cả hai màn → đạt việc (4).

## Hoàn nguyên (bước 8)

`TC-TW-DEMO-001` → `HOAT_DONG` · `TVV-BTP-TW-0002` → `HOAT_DONG`. Đã đọc lại xác nhận.
