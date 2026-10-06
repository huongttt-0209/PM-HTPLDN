# Condition table — BUG-EM-HDD-007 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Tên file | `HoiDap_{YYYYMMDD_HHmm}.xlsx` | `HoiDap_20260825_1103.xlsx` | Không |
| Số cột | Đủ 19 cột | Sheet `Hỏi đáp` có 19 cột | Không |
| Thứ tự cột | Khớp SRS | Khớp đủ từ `Số thứ tự` đến `Ngày duyệt`; `Email` ở cột 7 | Không |
| Header | In đậm, nền xám | 19/19 ô bold, fill `FFCCCCCC` | Không |
| Freeze header | Cố định dòng 1 | `freeze_panes = A2` | Không |
| Footer | Đủ 4 dòng sau dữ liệu | Có `Xuất lúc`, `Bởi`, `Bộ lọc áp dụng`, `Tổng số bản ghi` ở dòng 7–10 | Không |
| Dữ liệu | Xuất đúng phạm vi tài khoản | 4 bản ghi Bộ KH&ĐT; Email biên 100 ký tự hiển thị đúng, email rỗng giữ rỗng | Không |
| An toàn công thức | Không có formula injection/error | Workbook không có ô công thức | Không |

**Kết luận:** PASS — cấu trúc, định dạng, footer, freeze panes và tên file đều khớp đặc tả.

**Evidence workbook:** [BUG-EM-HDD-007-r3-export-2026-08-25.xlsx](../bug-report/evidence/BUG-EM-HDD-007-r3-export-2026-08-25.xlsx) — SHA-256 `5bcb2e71457e8a06b78febe2625eff883f274f69dcd0b9744f0b96fb841ac872`.
