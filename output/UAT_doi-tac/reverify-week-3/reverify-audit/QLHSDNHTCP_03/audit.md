# Audit QLHSDNHTCP_03 — Cột dữ liệu bảng Hồ sơ Chi trả

- **Verdict:** BA confirm (ghi sheet row 16, P16, 2026-07-20).
- **Tài khoản verify:** cbnv_tw (CB_NV_TW, BTP·TW, phạm vi Toàn quốc — cùng vai trò đối tác trong evidence).
- **Env:** https://18.143.165.120.nip.io (khác env đối tác `htpldn-uat.ospgroup.vn` = 117.4.241.135). Data seed: 10 hồ sơ CT-SEED-101→110 đủ 10 trạng thái (dev seed 2026-07-20).

## Evidence đối tác (Cổng 1)
- File: `partner-evidence/QLHSDNHTCP_03.jpg` (env ospgroup.vn, 2026-07-10 10:09).
- Neo: URL `/chi-tra/danh-sach`; cột header "SLA" giá trị "Quá hạn 58 ngày LV" (highlighted); tài khoản "CB Nghiệp vụ TW 01 / CB_NV_TW".
- Đối tác phản ánh: cột "Mức cảnh báo thời hạn" không giống thiết kế.

## Cổng 3 — SRS vs Web
| SRS (SCR-V.II-01 #16 + BR-CALC-03) | Web (18.143.165.120) | Đạt |
|---|---|:-:|
| Thành phần "SLA" — 4 mức cảnh báo warning/urgent/critical/overdue (`:935`, `:1383`) | Cột "Hạn xử lý", đếm ngược + mã màu (xanh còn hạn / đỏ / đen quá hạn) | Chức năng ✅ / format ⚠️ khác |
| Nhãn tiếng Việt, không viết tắt (`:1041`) | "Hạn xử lý" (tiếng Việt) | ✅ (tốt hơn "SLA" build cũ) |
| Cột: Mã HS, Tên DN, Quy mô DN, Số tiền đề nghị, Số tiền được duyệt, Trạng thái, SLA, Ngày nộp, Hành động | Đủ 9 cột + thêm "Mức HT %" (#6); THIẾU cột checkbox chọn dòng (#9) | ~ |

## Kết luận
- Web đáp ứng yêu cầu chức năng (có cột SLA + cảnh báo qua màu). Cách trình bày (đếm ngược thay vì 4 nhãn rời + tên "Hạn xử lý") khác thiết kế đối tác; SRS không quy định chính xác → **BA confirm** (xem ../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md §QLHSDNHTCP_03).
- **Không phải tràn/đè:** cột "Hành động" là fixed column sticky (AntD chuẩn), bảng overflowX auto — cột "Hạn xử lý" hiện đầy đủ khi cuộn ngang.

## Phát hiện thêm (ngoài claim đối tác)
- Bảng có **thêm cột "Mức HT %"** (100%) không có trong SRS SCR-V.II-01 list spec (là field màn chi tiết). Mức nhẹ.
- **Thiếu cột checkbox chọn dòng** (SRS component #9). Mức nhẹ.
- 2 điểm này gộp vào câu hỏi BA "cột danh sách đúng thiết kế chưa" — không mở bug riêng (borderline design choice, chưa rõ vi phạm).
