# Audit QLHSDNHTCP_09 — Tiêu đề trang + thanh tiến trình (màn Chi tiết)

- **Verdict:** BA confirm (ghi sheet row 18, P18, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io. Data seed 10 hồ sơ CT-SEED-101→110 (dev seed 2026-07-20).
- **Hồ sơ verify:** CT-SEED-101 (`/chi-tra/47b1f556-f559-4b75-9c2f-cd55c82e3ccb`), trạng thái Chờ tiếp nhận.

## Cổng 1 — Evidence đối tác
- `partner-evidence/QLHSDNHTCP_09.jpg` (env ospgroup.vn). Màn Chi tiết hồ sơ HSCT000066: tiêu đề trang = tên DN "Công ty TNHH Hữu Nghị TW", breadcrumb "… / Chi tiết", stepper 6 bước đủ.
- Đối tác phản ánh: tiêu đề trang không giống thiết kế (kỳ vọng "Chi tiết hồ sơ #{mã hồ sơ}").

## Cổng 3 — SRS vs Web (data thật)
| SRS SCR-V.II-02 | Web (18.143.165.120, CT-SEED-101) | Đạt |
|---|---|:-:|
| #1 Breadcrumb "Trang chủ > Chi trả chi phí > Chi tiết #{ma_ho_so}" (`:977`) | "Trang chủ / Chi trả chi phí / Chi tiết" — thiếu #mã | ⚠️ lệch |
| #3 Header info card: Mã hồ sơ, Tên DN, Quy mô, Trạng thái, SLA (`:979`) — KHÔNG quy định chuỗi tiêu đề h1 | h1 = tên DN "Công ty TNHH Seed Publishable"; đủ Mã HS CT-SEED-101, Quy mô Siêu nhỏ, Trạng thái Chờ tiếp nhận | ✅ trường đủ / tiêu đề spec silent |
| #4 Stepper 6 bước: Tiếp nhận→Kiểm tra→Đánh giá→Thẩm định→Phê duyệt→Thanh toán (`:980`) | Đủ 6 bước đúng thứ tự | ✅ |

## Kết luận
- Tiêu đề trang = tên DN tái hiện đúng như đối tác báo (bug reproduces), NHƯNG SRS component #3 không quy định chính xác chuỗi tiêu đề h1 phải là "Chi tiết hồ sơ #{mã}" — chỉ liệt kê các trường header. App đủ trường bắt buộc → không có SRS violation rõ ràng → **BA confirm** (xem ../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md §QLHSDNHTCP_09).
- Thanh tiến trình (stepper) đúng 6 bước theo component #4 → phần này KHÔNG phải lỗi.

## Phát hiện thêm (ngoài claim đối tác)
- Breadcrumb (#1, `:977`) hiển thị "Chi tiết" thiếu "#{ma_ho_so}" so với SRS → lệch nhẹ. Gộp vào câu hỏi BA (không mở bug riêng vì cùng chủ đề tiêu đề/định danh trang).

## Bug tĩnh (không phụ thuộc vai trò/trạng thái/dữ liệu)
- Tiêu đề trang + breadcrumb là thành phần hiển thị tĩnh — mọi hồ sơ / mọi vai trò / mọi trạng thái đều render giống nhau → dùng `--static-bug`, không cần bảng đối chiếu điều kiện.
