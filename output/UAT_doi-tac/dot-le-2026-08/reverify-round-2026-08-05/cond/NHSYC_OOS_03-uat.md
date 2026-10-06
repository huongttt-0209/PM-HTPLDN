# NHSYC_OOS_03 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 156 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Tiền đề | Một hồ sơ vụ việc đã có mức ưu tiên | Có sẵn 72 hồ sơ, phân theo mức: mức 1 (5 hồ sơ) · mức 3 (63) · mức 4 (2) · mức 5 (2) | Không |
| Màn hình | Chi tiết hồ sơ, trường "Ưu tiên" | Đúng màn Chi tiết, đúng trường "Ưu tiên" trong khối Nội dung Yêu cầu | Không |
| Số hồ sơ phải kiểm | Ít nhất 2 hồ sơ có mức ưu tiên KHÁC nhau | Kiểm **4 hồ sơ ở 4 mức khác nhau**: mức 1, 3, 4, 5 | Không |
| Bảng đối chiếu | Bảng chú giải 5 mức trong đặc tả | Đối chiếu `srs-v3.5/srs-fr-05-vu-viec.md:1524-1530` — cả cột "Chú giải hiển thị" và cột "Màu badge" | Không |
| Cách đo màu | Nhìn huy hiệu màu | Đọc màu nền thật của huy hiệu bằng giá trị màu tính toán của trình duyệt, không đoán bằng mắt | Không |
| Phạm vi loại trừ | Màn danh sách không có cột mức ưu tiên là ĐÚNG — không chấm FAIL | Không dùng ý đó làm căn cứ; chỉ đo màn chi tiết | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Trường "Ưu tiên" nay hiện con số KÈM chú giải bằng chữ**, đúng ý "chú giải kèm theo, không thay thế
  con số". Chữ hiển thị trùng từng chữ với cột "Chú giải hiển thị" của đặc tả:

  | Mức | Trên màn chi tiết | Đặc tả (`srs-fr-05-vu-viec.md:1526-1530`) | Hồ sơ đo |
  |---|---|---|---|
  | 1 | `1 — Mức thường — xét theo thứ tự nộp hồ sơ` | Mức thường — xét theo thứ tự nộp hồ sơ | `VV-BTP-TW-20260804-005` |
  | 3 | `3 — DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ` | DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ | `VV-STP-HN-20260805-003` |
  | 4 | `4 — Cán bộ nâng mức, kèm lý do` | Cán bộ nâng mức, kèm lý do | `VV-QA-R7-SLA-SH` |
  | 5 | `5 — Cán bộ nâng mức khẩn, kèm lý do` | Cán bộ nâng mức khẩn, kèm lý do | `VV-STP-AG-20260709-001` |

- **Có huy hiệu màu và màu đúng theo bảng**: mỗi mức render thành một huy hiệu nền màu; đọc màu nền thật
  của huy hiệu — mức 1 `#bfbfbf` **xám nhạt**, mức 3 `#52c41a` **xanh lá**, mức 4 `#fa8c16` **cam**,
  mức 5 `#ff4d4f` **đỏ** — khớp đúng cột "Màu badge" của đặc tả. Tình trạng "chỉ có con số trần, không chú
  giải, không huy hiệu màu" ở phản ánh gốc **không còn**.
- **Hai hồ sơ khác mức thì hiện chú giải và màu khác nhau**: bốn hồ sơ ở bốn mức cho ra bốn cặp
  chữ + màu khác nhau như bảng trên, không hồ sơ nào rơi về nhãn mặc định.
- **Chỗ khác cũng không còn con số trần**: ô "Độ ưu tiên" trên biểu mẫu Thêm mới hồ sơ vẫn hiển thị đúng
  dạng `4 — Cán bộ nâng mức, kèm lý do` / `5 — Cán bộ nâng mức khẩn, kèm lý do` (cán bộ chỉ được chọn nâng
  lên mức 4 hoặc 5; mức 1–3 do hệ thống tự tính, đúng BR-CALC-07 nên không có trong danh sách chọn).
- **Phần phiếu dặn KHÔNG được chấm sai đã tôn trọng**: màn danh sách không có cột / bộ lọc / sắp xếp theo
  mức ưu tiên — không dùng làm căn cứ trượt.

Ảnh: `../image/NHSYC_OOS_03-uat-uu-tien-muc-1-xam.png` · `../image/NHSYC_OOS_03-uat-uu-tien-muc-5-do.png`

## Ghi nhận thêm

- **Mức 2 không có hồ sơ nào trên môi trường này** nên không quan sát trực tiếp trên màn được. Đã kiểm gián
  tiếp bằng chính bảng ánh xạ mà giao diện dùng để render: bảng có đủ 5 mức, mức 2 = màu `#bfbfbf`
  (xám nhạt) + chú giải "DN có từ 30% lao động là người khuyết tật" — khớp đặc tả. Mức 2 dùng chung màu với
  mức 1 (đã quan sát trực tiếp), nên rủi ro còn lại không đáng kể. Không tự chỉnh mức ưu tiên của hồ sơ nào
  để ép ra mức 2, vì đó là giá trị hệ thống tự tính từ hồ sơ doanh nghiệp.
- Không tạo, không sửa, không xóa hồ sơ nào khi đo phiếu này — chỉ mở xem.
