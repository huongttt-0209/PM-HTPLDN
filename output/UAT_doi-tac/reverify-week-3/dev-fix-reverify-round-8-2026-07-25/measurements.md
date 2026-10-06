# Measurements — Reverify round 8 (2026-07-25)

- Môi trường: `https://18.143.165.120.nip.io` · tài khoản `cbnv_tw_04` (CB Nghiệp vụ Trung ương), login UI + OTP MailHog.
- Công cụ: Chrome DevTools MCP. Verdict lấy 100% từ giao diện (`innerText` + ảnh chụp). curl/fetch chỉ dùng đối chiếu.
- Mốc thời gian đo: **thứ Bảy 25/07/2026, 15:02–15:09**.
- Ngày lễ 2026 (`GET /api/v1/ngay-le?nam=2026`, đã xác thực): 01/01, 30/04, 01/05, 02/09 → **tháng 6–7/2026 KHÔNG có ngày lễ**. Ngày làm việc = T2–T6.
- Ngưỡng chấm: BR-SLA-02 — `srs-v3.5/srs-fr-06-chi-tra.md:1514-1523` (còn >50% = Bình thường · còn <50% = Sắp hết hạn · >100% = Quá hạn · >200% = Quá hạn nghiêm trọng); mốc tính là **ngày nộp** (`:1309`, `:1310`).
- Cách tính: % = (NLV đã trôi từ ngày nộp đến hôm nay) / (NLV giữa ngày nộp và hạn của CHÍNH bản ghi đó).

---

## CASE 1 — QLHSDNHTCP_03 (dòng 16) — màn DANH SÁCH `/chi-tra/danh-sach`

Nguồn số liệu: `evaluate_script` đọc `innerText` ô SLA + thuộc tính `title` của từng dòng (13/13 dòng, thẻ "Tất cả").

| Mã HS | Ngày nộp | Hạn | NLV đã dùng | NLV tổng | % đúng | % app hiện | Mức đúng | App hiển thị | ✅/❌ |
|---|---|---|---|---|---|---|---|---|---|
| CT-QAW7-NORMAL | 24/07 | 14/08 | 0 | 15 | 0% | 0% | Bình thường | Bình thường · còn 15 ngày LV | ✅ |
| CT-SEED-101 | 15/07 | 29/07 | 7 | 10 | 70% | 70% | Sắp hết hạn | Sắp hết hạn · còn 3 ngày LV | ✅ |
| CT-SEED-102 | 10/07 | 24/07 | 10 | 10 | 100% (hạn 24/07 đã trôi qua) | 101% | Quá hạn | Quá hạn · 0 ngày LV | ✅ |
| CT-SEED-104 | 08/07 | 22/07 | 12 | 10 | 120% | 120% | Quá hạn | Quá hạn · 2 ngày LV | ✅ |
| CT-SEED-103 | 05/07 | 17/07 | 15 | 10 | 150% | 150% | Quá hạn | Quá hạn · 5 ngày LV | ✅ |
| CT-SEED-105 | 03/07 | 17/07 | 15 | 10 | 150% | 150% | Quá hạn | Quá hạn · 5 ngày LV | ✅ |
| CT-SEED-106 | 01/07 | 15/07 | 17 | 10 | 170% | 170% | Quá hạn | Quá hạn · 7 ngày LV | ✅ |
| CT-SEED-107 | 25/06 | 09/07 | 21 | 10 | 210% | 210% | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 11 ngày LV | ✅ |
| CT-QAW7-OVERDUE | 04/05 | 25/05 | 59 | 15 | 393% | 393% | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 44 ngày LV | ✅ |
| CT-SEED-108 (Đã thanh toán 24/06, hạn 29/06 — đúng hạn) | 15/06 | 29/06 | — kết thúc | 10 | — | (không có) | không đếm quá hạn | Đã hoàn thành | ✅ |
| CT-SEED-109 (Từ chối 27/06, hạn 03/07 — đúng hạn) | 20/06 | 03/07 | — kết thúc | 10 | — | (không có) | không đếm quá hạn | Đã hoàn thành | ✅ |
| CT-SEED-110 (Hủy) | 12/06 | 26/06 | — kết thúc | 10 | — | (không có) | không đếm quá hạn | Đã hoàn thành | ✅ |
| CT-QAW7-CLOSED (Đã thanh toán) | 01/06 | 22/06 | — kết thúc | 15 | — | (không có) | không đếm quá hạn | Đã hoàn thành | ✅ |

### Đối chiếu 5 gạch (B) của lượt Reopen

| # | Gạch lỗi lượt trước | Kết quả round 8 | Trạng thái |
|---|---|---|---|
| 1 | CT-SEED-101 hiện "Quá hạn · 0 ngày LV", đúng ra "Sắp hết hạn" | UI: **Sắp hết hạn · còn 3 ngày LV** (70%) | ✅ hết lỗi |
| 2 | CT-SEED-105 / CT-SEED-106 hiện "Quá hạn nghiêm trọng" | UI: **Quá hạn · 5 ngày LV** (150%) / **Quá hạn · 7 ngày LV** (170%) | ✅ hết lỗi |
| 3 | CT-SEED-108/109/110 đã kết thúc trong hạn vẫn bị đếm quá hạn | UI: cả 3 = **Đã hoàn thành**, không còn nhãn quá hạn | ✅ hết lỗi |
| 4 | CT-SEED-103 chú thích 188% (đúng phải 150%) | UI `title` = **"150% thời hạn đã dùng"** | ✅ hết lỗi |
| 5 | Duyệt 5 thẻ chỉ thấy 2 mức | Đủ **4 mức**; riêng thẻ "Chờ xử lý" đã có cả 4 | ✅ hết lỗi |

### Duyệt 5 thẻ trạng thái (đọc UI từng thẻ)

| Thẻ | Bản ghi | Mức xuất hiện |
|---|---|---|
| Tất cả (13) | 13/13 | Bình thường · Sắp hết hạn · Quá hạn · Quá hạn nghiêm trọng (+ Đã hoàn thành cho HS đã kết thúc) |
| Chờ xử lý (5) | QAW7-NORMAL, QAW7-OVERDUE, SEED-103, SEED-102, SEED-101 | **đủ 4 mức trong 1 màn** |
| Đang đánh giá (2) | SEED-104 (120%), SEED-105 (150%) | Quá hạn |
| Chờ phê duyệt (1) | SEED-106 (170%) | Quá hạn |
| Đã xử lý (5) | QAW7-CLOSED, SEED-108/109/110 (Đã hoàn thành), SEED-107 (210%) | Quá hạn nghiêm trọng + Đã hoàn thành |

### Đối chiếu phương pháp thứ hai (chỉ để điều tra)

`GET /api/v1/ho-so-chi-tras?tab=TAT_CA` trả `mucDoCanhBao` khớp 100% nhãn UI cho các hồ sơ đang xử lý (101 = SAP_HET_HAN, 102–106 = QUA_HAN, 107 + QAW7-OVERDUE = QUA_HAN_NGHIEM_TRONG, QAW7-NORMAL = BINH_THUONG). Không còn mâu thuẫn UI–máy chủ như lượt trước (round 7: máy chủ trả SAP_HET_HAN nhưng UI hiện "Quá hạn · 0 ngày LV"). FE gọi `/api/v1/ngay-le?nam=2026` + `?nam=2027` khi dựng danh sách → có trừ T7/CN và ngày lễ.

**VERDICT CASE 1: Pass** — (A) đủ điều kiện PASS (4 nhãn đúng bộ, kèm số ngày, khớp ngưỡng 50/100/200 tính từ dữ liệu thực) và (B) 5/5 gạch đều không tái hiện.

**Ảnh:**
- `QLHSDNHTCP_03/image/danh-sach-cot-sla-day-du-13-dong.png` — 13 dòng, cột SLA đọc trọn nhãn.
- `QLHSDNHTCP_03/image/tooltip-phan-tram-doc-tu-dom-13-dong.png` — bảng % đọc thẳng từ thuộc tính `title` (CT-SEED-103 = 150%).
- `QLHSDNHTCP_03/image/the-cho-xu-ly-du-4-muc-canh-bao.png` — 1 màn có đủ 4 mức.
- `QLHSDNHTCP_03/image/danh-sach-13-dong-cot-sla.png`, `danh-sach-viewport-cot-sla-mau-nhan.png` — ảnh phụ (màu nhãn).

> Ghi chú kỹ thuật: chú thích % là thuộc tính `title` gốc của trình duyệt nên không lọt vào ảnh chụp CDP. Vì vậy bằng chứng % được đọc trực tiếp từ DOM và in ra bảng trong ảnh `tooltip-phan-tram-doc-tu-dom-13-dong.png`.

---

## CASE 2 — QLHSDNHTCP_10 (dòng 19) — màn CHI TIẾT, thanh thông tin tổng quan

| Mã HS | Ngày nộp | Hạn | NLV đã dùng | NLV tổng | % đúng | % app (chi tiết) | Mức đúng | Thanh tổng quan hiển thị | Danh sách hiển thị | Khớp 2 màn |
|---|---|---|---|---|---|---|---|---|---|---|
| CT-QAW7-NORMAL | 24/07 | 14/08 | 0 | 15 | 0% | 0% | Bình thường | Bình thường · còn 15 ngày LV | Bình thường · còn 15 ngày LV | ✅ |
| CT-SEED-101 | 15/07 | 29/07 | 7 | 10 | 70% | 70% | Sắp hết hạn | Sắp hết hạn · còn 3 ngày LV | Sắp hết hạn · còn 3 ngày LV | ✅ |
| CT-SEED-107 | 25/06 | 09/07 | 21 | 10 | 210% | 210% | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 11 ngày LV | Quá hạn nghiêm trọng · 11 ngày LV | ✅ |
| CT-SEED-108 (kết thúc đúng hạn) | 15/06 | 29/06 | — | 10 | — | (không có) | không đếm quá hạn | Đã hoàn thành | Đã hoàn thành | ✅ |

Thanh tổng quan cả 4 hồ sơ đều có đủ 4 ô: **Mã HS · Quy mô DN · Trạng thái · SLA**.

### Đối chiếu 3 gạch (B) của lượt Reopen

| # | Gạch lỗi lượt trước | Kết quả round 8 | Trạng thái |
|---|---|---|---|
| 1 | HS chưa quá hạn không có trường SLA trên thanh tổng quan (CT-SEED-101 chỉ có Mã HS / Quy mô DN / Trạng thái) | CT-SEED-101 có ô **SLA = Sắp hết hạn · còn 3 ngày LV**; CT-QAW7-NORMAL có **SLA = Bình thường · còn 15 ngày LV** | ✅ hết lỗi |
| 2 | CT-SEED-108 kết thúc đúng hạn vẫn hiện "Quá hạn nghiêm trọng · 21 ngày LV" ở chi tiết | Chi tiết hiện **Đã hoàn thành** | ✅ hết lỗi |
| 3 | Hai màn lệch %: CT-SEED-107 danh sách 350% vs chi tiết 400% | Cả hai màn đều **210%**, nhãn giống nhau | ✅ hết lỗi |
| 4 (gạch còn lại của round 7) | Thanh tổng quan CT-SEED-101 hiện "Quá hạn · 0 ngày LV" thay vì "Sắp hết hạn" | Thanh tổng quan hiện **Sắp hết hạn · còn 3 ngày LV** (70%) | ✅ hết lỗi |

**VERDICT CASE 2: Pass** — (A) đủ điều kiện PASS (thanh tổng quan có nhãn mức BR-SLA-02 kèm số ngày, khớp ngưỡng tính từ dữ liệu thực, và 4/4 hồ sơ cho cùng nhãn + cùng % ở cả 2 màn) và (B) không còn gạch nào tái hiện.

**Ảnh:**
- `QLHSDNHTCP_10/image/chi-tiet-ct-qaw7-normal-thanh-tong-quan.png`
- `QLHSDNHTCP_10/image/chi-tiet-ct-seed-101-thanh-tong-quan.png`
- `QLHSDNHTCP_10/image/chi-tiet-ct-seed-107-thanh-tong-quan.png`
- `QLHSDNHTCP_10/image/chi-tiet-ct-seed-108-thanh-tong-quan.png`

---

## Ghi sheet

| Dòng | Mã TC | Ô | Trước | Sau | Giờ ghi |
|---|---|---|---|---|---|
| 16 | QLHSDNHTCP_03 | Q16 | Reopen | **Pass** | 25/07/2026 15:09:56 |
| 19 | QLHSDNHTCP_10 | Q19 | Reopen | **Pass** | 25/07/2026 15:10:00 |

Chỉ đụng cột Verify (Q), không đổi P/R — đúng quy tắc mục 4 của BRIEF.
