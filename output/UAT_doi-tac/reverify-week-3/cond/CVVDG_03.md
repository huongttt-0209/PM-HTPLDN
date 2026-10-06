# Bảng đối chiếu điều kiện — CVVDG_03

Loại bug: **Chọn vụ việc đã thuộc đợt đánh giá khác KHÔNG hiển thị cảnh báo trùng đợt.** Verdict phụ thuộc: (1) đúng role/state chọn VV, (2) VV thực sự đã thuộc đợt khác (BE flag), (3) tái hiện đúng: FE có/không cảnh báo.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò chọn VV | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP Hà Nội) | Không |
| Trạng thái đợt khi chọn VV | THUC_HIEN | Đợt ở THUC_HIEN (đã duyệt phân công) | Không |
| VV đã thuộc đợt khác | Có (VV trùng) | BE `vu-viec-eligible` trả `daThuocDotKhac=true` cho VV đang chọn | Không |
| Hành vi tái hiện — hệ thống có cảnh báo trùng đợt? | Đối tác báo: không cảnh báo | Mình tái hiện đúng: chọn VV `daThuocDotKhac=true` → KHÔNG toast/modal/cột cảnh báo nào; VV vào danh sách chọn im lặng | Không |

**Kết luận: 0 GAP điều kiện.** Tái hiện đúng hiện tượng đối tác báo: BE cung cấp cờ `daThuocDotKhac=true` nhưng FE không hiển thị bất kỳ cảnh báo trùng đợt nào khi chọn. Vi phạm SRS FR-VI-05: L393 mô tả "Cảnh báo nếu VV đã thuộc đợt khác nhưng vẫn cho phép chọn lại"; L419 bước 5; AC L449 "Given VV đã thuộc đợt khác When chọn lại Then cảnh báo (vẫn cho phép)". → **Open**.
