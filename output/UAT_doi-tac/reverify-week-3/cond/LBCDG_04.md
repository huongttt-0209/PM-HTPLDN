# Bảng đối chiếu điều kiện — LBCDG_04

Loại bug: **Tên nút "Xuất Excel" không giống thiết kế.** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS prescribe nhãn nút xuất.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP) | Không |
| Màn hình | Tab Báo cáo — nút xuất | Cùng | Không |
| Đối tượng so sánh | Nhãn nút xuất | App: 1 nút "Xuất báo cáo" (bấm → file .xlsx) | Không |

**Kết luận: 0 GAP.** SRS SCR item 53 mô tả 2 nút "[Xuất XLSX] / [Xuất DOCX]"; app dùng 1 nút "Xuất báo cáo". Chức năng xuất Excel đúng, chỉ khác nhãn → cần BA chốt nhãn. → **BA confirm**.
