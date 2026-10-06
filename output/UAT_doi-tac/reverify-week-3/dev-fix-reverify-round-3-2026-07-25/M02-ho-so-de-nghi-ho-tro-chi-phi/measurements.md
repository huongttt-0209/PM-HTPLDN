# M02 — Hồ sơ đề nghị hỗ trợ chi phí · Reverify sau Dev fix (round 3, 25/07/2026)

Môi trường: https://18.143.165.120.nip.io · Tài khoản `cbnv_tw` / `Test@1234` (đúng precondition Dev nêu).
Tiêu chí chấm: mục **CÁCH VERIFY** trong cột "DEV phản hồi lần 1" của từng dòng — không tự đặt tiêu chí khác.
Thời điểm đo: 25/07/2026 ~04:50 (giờ VN).

| Dòng | Mã TC | Verify | Hồ sơ dùng |
|---|---|---|---|
| 16 | QLHSDNHTCP_03 | ❌ Reopen | CT-SEED-101 → 110 (toàn bộ 10 hồ sơ) |
| 18 | QLHSDNHTCP_09 | ✅ Pass | CT-SEED-101, 102, 107, 108 |
| 19 | QLHSDNHTCP_10 | ❌ Reopen | CT-SEED-101 (chưa quá hạn), 102 / 107 / 108 (đã quá hạn) |

---

## Bảng đo SLA — nền của cả TC_03 và TC_10

Chuẩn tính theo tiêu chí Dev bước 2: `hạn = ngày nộp + 10 ngày làm việc` (T2–T6, trừ ngày lễ lấy từ
`/api/v1/ngay-le?nam=2026`; tháng 6–7/2026 không có ngày lễ). Mốc đếm là **ngày nộp**, đúng lưu ý ⚠️ của Dev
(`srs-fr-06-chi-tra.md:119`). Ngưỡng BR-SLA-02 (`srs-fr-06-chi-tra.md:1514-1523`): còn >50% = Bình thường ·
còn <50% = Sắp hết hạn · quá hạn = Quá hạn · trễ vượt >200% thời lượng = Quá hạn nghiêm trọng.

| Mã HS | Ngày nộp | Hạn (10 NLV) | Đã dùng | % đúng | % app hiện (tooltip) | Mức đúng | App hiển thị | KQ |
|---|---|---|---|---|---|---|---|---|
| CT-SEED-101 | 15/07 | 29/07 | 7 NLV | 70% | 101% | Sắp hết hạn | Quá hạn · 0 ngày LV | ❌ |
| CT-SEED-102 | 10/07 | 24/07 | 10 NLV | 100% | 167% | Quá hạn | Quá hạn · 4 ngày LV | ✅ |
| CT-SEED-103 | 05/07 | 17/07 | 15 NLV | 150% | 188% | Quá hạn | Quá hạn · 7 ngày LV | ✅ |
| CT-SEED-104 | 08/07 | 22/07 | 12 NLV | 120% | 171% | Quá hạn | Quá hạn · 5 ngày LV | ✅ |
| CT-SEED-105 | 03/07 | 17/07 | 15 NLV | 150% | 250% | Quá hạn | Quá hạn nghiêm trọng · 9 ngày LV | ❌ |
| CT-SEED-106 | 01/07 | 15/07 | 17 NLV | 170% | 243% | Quá hạn | Quá hạn nghiêm trọng · 10 ngày LV | ❌ |
| CT-SEED-107 | 25/06 | 09/07 | 21 NLV | 210% | 350% | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 15 ngày LV | ✅ |
| CT-SEED-108 | 15/06 | 29/06 | 29 NLV | 290% | 363% | *(đã thanh toán 24/06 — trong hạn)* | Quá hạn nghiêm trọng · 21 ngày LV | ❌ |
| CT-SEED-109 | 20/06 | 03/07 | 25 NLV | 250% | 357% | *(đã từ chối 27/06 — trong hạn)* | Quá hạn nghiêm trọng · 18 ngày LV | ❌ |
| CT-SEED-110 | 12/06 | 26/06 | 30 NLV | 300% | 500% | *(đã hủy)* | Quá hạn nghiêm trọng · 24 ngày LV | ❌ |

**Gốc lỗi đo được:** `deadlineSla` BE trả về đúng bằng `ngayNop + 10 ngày LỊCH` ở cả 10 hồ sơ
(15/06→25/06, 10/07→20/07, 03/07→13/07…), không trừ T7/CN. FE lấy mốc đó quy ra ngày làm việc nên mẫu số
thời lượng SLA chỉ còn 6–8 NLV thay vì 10 → tỷ lệ đội lên → nhảy mức sớm.
Công thức FE khớp chính xác: `% = số NLV đã trôi / số NLV giữa ngayNop và deadlineSla`
(vd CT-SEED-110: 30/6 = 500%; CT-SEED-106: 17/7 = 243%).

**FE không dùng trường mức của BE.** So `mucDoCanhBao` trong `/api/v1/ho-so-chi-tras`:

| Mã HS | BE `mucDoCanhBao` | UI hiển thị |
|---|---|---|
| CT-SEED-101 | `SAP_HET_HAN` | Quá hạn |
| CT-SEED-108 / 109 / 110 | `BINH_THUONG` | Quá hạn nghiêm trọng |

**Độ phủ mức:** cả 5 thẻ trạng thái gộp lại đúng 10 hồ sơ (thẻ "Tất cả" đã hiện `Hiển thị 1-10 / 10 kết quả`),
chỉ xuất hiện 2/4 mức — không dòng nào ra "Bình thường" hay "Sắp hết hạn", kể cả hồ sơ mà BE đánh `SAP_HET_HAN`.
→ bước 3 của tiêu chí không thỏa.

---

## QLHSDNHTCP_03 (dòng 16) — Reopen

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Đọc cột SLA từng dòng | Cột SLA hiện nhãn mức + số ngày, dạng "Quá hạn · 4 ngày LV" — **đã hết lỗi cũ** (trước chỉ đếm ngày + tô màu) | ✅ |
| 2) Đối chiếu mức với hạn tính từ ngày nộp | Sai mức ở **CT-SEED-101 / 105 / 106**; thêm **108 / 109 / 110** đã kết thúc trong hạn vẫn bị đếm quá hạn | ❌ |
| 3) Duyệt các thẻ trạng thái để đủ 4 mức | Chỉ ra 2 mức (Quá hạn, Quá hạn nghiêm trọng); thiếu Bình thường + Sắp hết hạn | ❌ |

Không FAIL vì chuỗi "N ngày LV" bên cạnh nhãn (đúng lưu ý ⚠️ của Dev), không FAIL vì tên cột "SLA".

Ảnh: `image/QLHSDNHTCP_03-01-danh-sach-cot-sla-4-nhan.png`,
`image/QLHSDNHTCP_03-02-CT-SEED-108-da-thanh-toan-trong-han-van-qua-han-nghiem-trong.png`

## QLHSDNHTCP_09 (dòng 18) — Pass

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Mở hồ sơ thứ nhất, đọc đường dẫn | `Trang chủ / Chi trả chi phí / Chi tiết #CT-SEED-101` — đủ 3 cấp, cấp cuối có mã | ✅ |
| 2) Mở hồ sơ thứ hai, đọc lại | `… / Chi tiết #CT-SEED-102`; kiểm thêm `#CT-SEED-107`, `#CT-SEED-108` — mã đổi đúng theo hồ sơ đang mở | ✅ |
| 3) Bấm từng cấp trên đường dẫn | "Chi trả chi phí" → `/chi-tra/danh-sach` (10 dòng); "Trang chủ" → `/dashboard` ("Tổng quan hệ thống") | ✅ |

Đã áp dụng lưu ý ⚠️: **không chấm tiêu đề lớn** (đang hiện tên doanh nghiệp — BA đã kết luận không phải lỗi).

Ảnh: `image/QLHSDNHTCP_09-01-breadcrumb-CT-SEED-101.png`

## QLHSDNHTCP_10 (dòng 19) — Reopen

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Màn chi tiết hồ sơ **chưa quá hạn** (CT-SEED-101, Chờ tiếp nhận) | Thanh tổng quan chỉ có Mã HS / Quy mô DN / Trạng thái — **không có trường SLA nào**. Toàn trang 0 lần xuất hiện "Quá hạn/Sắp hết/Bình thường/ngày LV"; chỉ có câu gợi ý "Tiếp nhận để bắt đầu kiểm tra và đặt SLA". Trong khi ngoài danh sách hồ sơ này vẫn có nhãn SLA | ❌ |
| 2) Màn chi tiết hồ sơ **đã quá hạn** | Có trường SLA + nhãn + số ngày (CT-SEED-102 "Quá hạn · 4 ngày LV"; CT-SEED-107 "Quá hạn nghiêm trọng · 15 ngày LV") | ✅ nhãn có |
| 3) So nhãn danh sách ↔ chi tiết | Nhãn trùng, nhưng **tỷ lệ tính lệch**: CT-SEED-107 danh sách 350% vs chi tiết 400% → chi tiết đếm từ `ngayTiepNhan` (26/06) thay vì `ngayNop` (25/06), trái lưu ý ⚠️ "đếm từ NGÀY NỘP" | ❌ |
| Mức khớp ngưỡng | Sai giống TC_03 — CT-SEED-108 xử lý đúng hạn (thanh toán 24/06, hạn 29/06) vẫn "Quá hạn nghiêm trọng" | ❌ |

Đã áp dụng lưu ý ⚠️: không FAIL vì nhãn ô là "SLA"; chấm trên **thanh tổng quan màn Chi tiết**, không lấy màn danh sách thay thế.

Ảnh: `image/QLHSDNHTCP_10-01-chitiet-CT-SEED-102-thanh-tongquan-sla.png`,
`image/QLHSDNHTCP_10-02-chitiet-CT-SEED-101-thieu-truong-sla.png`
