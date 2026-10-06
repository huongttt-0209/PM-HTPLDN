# Bảng đối chiếu điều kiện — THDG_04

Loại bug: **Điểm tổng hợp hiển thị 1 chữ số thập phân (kỳ vọng 2).** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS quy định số chữ số thập phân.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP) | Không |
| Màn hình | Bảng Chấm điểm — cột "Điểm tổng" | Cùng cột | Không |
| Giá trị quan sát | Điểm tổng 1 chữ số thập phân | App: "8.0" / "10.0" (1 chữ số); BE trả "8.00" (2 chữ số) | Không |

**Kết luận: 0 GAP.** Tái hiện đúng: cột Điểm tổng hiển thị 1 chữ số thập phân. SRS FR-VI-06 Outputs #2 "Điểm tổng hợp | 2 số thập phân". BE trả 2 số, FE cắt còn 1 → lỗi hiển thị FE. → **Open (Minor)**.
