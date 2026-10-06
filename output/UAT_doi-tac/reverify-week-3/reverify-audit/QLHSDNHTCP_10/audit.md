# Audit QLHSDNHTCP_10 — Nhóm 0 Thanh thông tin tổng quan (màn Chi tiết)

- **Verdict:** BA confirm (ghi sheet row 19, P19, 2026-07-20).
- **Tài khoản:** cbnv_tw (CB_NV_TW, BTP·TW). Env https://18.143.165.120.nip.io. Data seed 10 hồ sơ CT-SEED-101→110 (dev seed 2026-07-20).
- **Hồ sơ verify:** CT-SEED-103 (`/chi-tra/3cc417aa-...`), trạng thái Yêu cầu bổ sung (khớp state evidence đối tác).

## Cổng 1 — Evidence đối tác
- `partner-evidence/QLHSDNHTCP_10.jpg` (env ospgroup.vn, 10/07). Màn Chi tiết HSCT000066 (Yêu cầu bổ sung): thanh tổng quan gồm Mã HS, Quy mô DN, Trạng thái, SLA "Quá hạn 58 ngày LV".
- Đối tác phản ánh (Kết quả thực tế): "Mức cảnh báo thời hạn không giống với thiết kế".

## Cổng 3 — SRS vs Web (data thật)
| SRS SCR-V.II-02 | Web (18.143.165.120, CT-SEED-103) | Đạt |
|---|---|:-:|
| #3 Header info: Mã hồ sơ / Tên DN / Quy mô / Trạng thái / SLA (`:979`) | Đủ Mã HS CT-SEED-103, Quy mô Nhỏ, Trạng thái Yêu cầu bổ sung, SLA; layout gọn không tràn/đè | ✅ trường đủ |
| SLA = "4 mức cảnh báo theo BR-CALC-03": warning "Sắp đến hạn" / urgent "Cần xử lý gấp" / critical "Sát hạn" / overdue "Quá hạn" (`:1383-1392`) | Trường "SLA" giá trị "Quá hạn 3 ngày LV" (badge đỏ, đếm ngược) — không phải 4 nhãn mức rời | ⚠️ format khác |
| Nhãn tiếng Việt (`:1041`) | "SLA" + "Quá hạn N ngày LV" (tiếng Việt) | ✅ |

- Ghi chú backend: enum `mucDoCanhBao` = BINH_THUONG / SAP_HET_HAN / QUA_HAN / QUA_HAN_NGHIEM_TRONG — mô hình 4 mức của BE khác 4 mức BR-CALC-03 (warning/urgent/critical/overdue). Nhưng đây là data model, phần đối tác phản ánh là DISPLAY (format hiển thị).

## Kết luận
- Thanh tổng quan (Nhóm 0) có đủ trường bắt buộc theo component #3, tiếng Việt, không tràn/đè → đạt yêu cầu chức năng. Riêng trường SLA hiển thị đếm ngược + màu thay vì 4 nhãn mức rời BR-CALC-03 → khác thiết kế đối tác nhưng SRS không quy định chính xác format → **BA confirm**.
- **Cùng gốc câu hỏi với QLHSDNHTCP_03** (SLA đếm ngược vs 4 nhãn discrete), khác ở chỗ đây là thanh tổng quan màn Chi tiết (label "SLA" khớp SRS #3), _03 là cột danh sách (label "Hạn xử lý"). Gộp chung câu hỏi BA. Chi tiết: `../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md §QLHSDNHTCP_10`.
- Bảng đối chiếu điều kiện 0 GAP (`condition-table.md`): cùng vai trò + cùng màn + cùng state Yêu cầu bổ sung + SLA đều có giá trị overdue → bug tái hiện, không phải build cũ.

## Phát hiện thêm (ngoài claim đối tác)
- Không có phát hiện mới ngoài SLA format (các trường Nhóm 0 khác đều đúng).
