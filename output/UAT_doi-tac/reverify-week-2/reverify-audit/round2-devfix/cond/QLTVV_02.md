# Bảng đối chiếu điều kiện — QLTVV_02 (reverify R2 sau dev fix)

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Màn hình | Mạng lưới TVV → Tư vấn viên/Chuyên gia (danh sách) | /chuyen-gia-tvv/danh-sach, tab "Đang hoạt động" | Không |
| Cột "Loại" | Hiển thị mã viết tắt "TVV"/"CG" (bug) | Cả 4 bản ghi cột Loại = "Tư vấn viên" (nhãn đầy đủ), không còn mã enum | Không |
| Cột "Điểm ĐG" — có đánh giá | Số thô thang /10 + 1 sao (đối tác thấy "8.3") | TVV-BTP-TW-0002 = "4.2/5" + 5 sao (đúng thang /5 + sao) | Không |
| Cột "Điểm ĐG" — chưa đánh giá | Chỉ "—" (thiếu "/5", thiếu sao) | 3 TVV chưa đánh giá = "—/5" | Không |
