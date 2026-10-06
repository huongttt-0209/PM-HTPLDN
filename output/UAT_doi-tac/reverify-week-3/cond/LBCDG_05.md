# Bảng đối chiếu điều kiện — LBCDG_05

Loại bug: **Không có nút "Xuất Word".** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS yêu cầu xuất Word.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP) | Không |
| Màn hình | Tab Báo cáo — nút xuất | Cùng | Không |
| Đối tượng so sánh | Có nút xuất Word? | App: chỉ 1 nút "Xuất báo cáo" → luôn .xlsx; API mọi param docx/word đều trả .xlsx | Không |

**Kết luận: 0 GAP.** SRS FR-VI-07 Outputs #2 "Excel (.xlsx) / Word (.docx)" + SCR item 53 [Xuất DOCX] + AC 612 yêu cầu xuất cả Excel và Word. App không có xuất Word cả FE lẫn BE (verified 4 param API). → **Open**.
