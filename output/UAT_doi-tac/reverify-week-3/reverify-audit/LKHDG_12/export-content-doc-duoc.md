# Nội dung file Excel export thực tế — LKHDG_12 (đọc trực tiếp từ blob export env 18.143, cbnv_tw)

File `.xlsx` do nút "Xuất Excel" sinh ra (client-side). Đọc trực tiếp cell values từ blob (giải nén `sharedStrings.xml` + `sheet1.xml`).

## Cấu trúc: dimension A1:G4 → **7 cột**, 4 dòng (1 header + 3 đợt)

## Header (dòng 1) — 7 cột
| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Mã KH | Tên đợt | Tần suất | Đối tượng | Từ ngày | Đến ngày | Trạng thái |

→ **Thiếu 3 cột so với bảng danh sách trên UI: "Số vụ việc", "Người tạo", "Ngày tạo".**

## Dữ liệu (3 đợt)
| Mã KH | Tên đợt | Tần suất | Đối tượng | Từ ngày | Đến ngày | Trạng thái |
|---|---|---|---|---|---|---|
| DG-20260720-0002 | QA-LKHDG-Test-LapKeHoach-20260720 | `TRON_NAM` | `VU_VIEC` | 1/8/2026 | 31/12/2026 | `LAP_KE_HOACH` |
| DG-20260720-0001 | DGHQ-B1-20260720 Batch B downstream | `TRON_NAM` | `VU_VIEC` | 1/1/2026 | (—) | `CHO_PHE_DUYET` |
| KHDG-SEED-0001 | Đợt đánh giá seed 2026 | `TRON_NAM` | `VU_VIEC` | (—) | 30/6/2026 | `HOAN_THANH` |

→ **Cột Tần suất / Đối tượng / Trạng thái ghi MÃ ENUM THÔ** (`TRON_NAM`, `VU_VIEC`, `LAP_KE_HOACH`, `CHO_PHE_DUYET`, `HOAN_THANH`) thay vì nhãn tiếng Việt như UI ("Trọn năm", "Vụ việc", "Lập kế hoạch", "Chờ phê duyệt", "Hoàn thành"). Đối tác mô tả là "hiển thị không dấu".

## File gốc
- `export-danhsach-dot.xlsx` — file thật tải về (sheet1.xml nguyên vẹn xác nhận 7 cột A1:G4; sharedStrings đọc qua giải nén in-browser).

## Claim (a) "sai tiêu chí lọc"
- Lần test này export ở chế độ KHÔNG lọc → trả đúng 3 đợt đang có. Chưa tái hiện được lỗi lọc (phiên đăng nhập hết hạn khi thử áp filter tab "Lập kế hoạch"). (b) + (c) đã đủ để kết luận Open.
