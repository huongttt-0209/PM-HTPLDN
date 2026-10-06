# Audit — TKDGHQHTPL_02 (verify phản ánh vòng 2 + kiểm chứng giải trình của dev)

> **Ngày:** 2026-07-27 · **Tester:** QA nội bộ · **Tài khoản:** bộ 02 (`cbnv_tw_02`)
> **Trạng thái ô W (dòng 47, tab tuần 1):** đã ghi **`Open, BA confirm`** lúc 27/07 14:2x. Trước đó ô đang là `dev done` (dev tự đổi sau 11:44), **không phải** `Reopen`.
> **Giải trình của dev cần kiểm chứng:** *"do BE vs FE chưa giống nhau"*

## 1. Claim vòng 2 của đối tác

Thẻ **"Điểm đánh giá hiệu quả hỗ trợ pháp lý"** (Tổng quan hệ thống) hiển thị **164.0/100** — vượt trần 100, trục biểu đồ chạy tới 172.

## 2. Triệu chứng ">100" — KHÔNG còn tái hiện

Kiểm tra lại trên **chính env đối tác** `htpldn-uat.ospgroup.vn`, **cùng bộ lọc** (`donViCap=TW` + `donViId=…0001`), **cùng tập dữ liệu chưa bị đụng vào**:

| Dấu hiệu neo (chứng minh cùng dữ liệu) | Ảnh đối tác 21/07 | Đo lại 27/07 |
|---|---|---|
| Tỷ lệ tuân thủ thời hạn xử lý | 17.4% | 17.4% ✅ |
| Thời gian xử lý trung bình | 0,3 ngày | 0,3 ngày ✅ |
| Số người hỗ trợ pháp lý | 9 | 9 ✅ |
| Số khóa học | 1 | 1 ✅ |
| **Điểm đánh giá hiệu quả** | **164.0**/100 · trục 7.5→**172** | **8.2**/100 · trục 7.5→**100** |

→ Dữ liệu **y hệt**, chỉ mỗi con số điểm đổi: `164.0 ÷ 8.2 = 20.0` **chẵn**. Đã quét thêm **33 tổ hợp bộ lọc** (cấp TW/BN/ĐP × đơn vị × kỳ) — **không tổ hợp nào vượt 100**.

### Hệ số 20 KHÔNG ngẫu nhiên — chính là mức lệch thang đã ghi trong CHANGELOG

`CHANGELOG-v3-to-v3.5.md:1729` giải thích lý do đổi thang khi nâng SRS v3 → v3.5:

> "v3 ghi điểm đánh giá theo thang **1-5** trong khi nhóm dữ liệu kết quả đánh giá thực tế lưu thang **0-100** (ràng buộc nghiệp vụ 'điểm tổng từ 0 đến 100') — **lệch nhau 20 lần**. Cán bộ nghiệp vụ nhìn biểu đồ Dashboard hiển thị '3.5' trong khi báo cáo chi tiết hiển thị '70' cho cùng một vụ, không cách nào đối chiếu."

`CHANGELOG-v3-to-v3.5.md:1734`: *"v4 sửa Outputs về thang 0-100 để đồng nhất với nhóm dữ liệu nguồn"*. Đối chiếu v3 gốc: `srs-v3/srs-fr-01-dashboard.md:295` — `diem_hai_long_tb` | **thang 1-5**.

**Kết luận phần này:** bản build đối tác test còn mang hệ số quy đổi **×20** của thang v3 cũ (1-5 → 0-100); bản hiện tại đã bỏ hệ số đó. Đây **đúng là** "BE vs FE chưa giống nhau" như dev giải trình — và mức lệch trùng khít con số 20 mà chính CHANGELOG đã ghi. Triệu chứng đối tác chụp không còn.

![Env đối tác 27/07 — 8.2/100, trục trần 100](TKDGHQHTPL_02-r3-partner-env-8.2-tren-100.png)

## 3. Kiểm chứng giải trình "BE vs FE chưa giống nhau" — **ĐÚNG, nhưng chưa phải là toàn bộ vấn đề**

Đo trên env được giao `18.143.165.120.nip.io` (env đối tác đang 404 tại thời điểm đo sâu; đã ghi nhận ở §6).

### 3.0 Đo lại 27/07 14:10 — bằng chứng NGAY TRÊN ENV ĐỐI TÁC (bổ sung, mạnh hơn §3.1-3.4)

Env đối tác đã hồi phục 404 → đo trực tiếp, không cần suy từ nip.io nữa.

**a) Cùng bộ lọc của đối tác** (`Cấp đơn vị = Trung ương` + `Đơn vị = Cục Bổ trợ tư pháp - Bộ Tư pháp` → URL `?donViId=…0001`):

| | Ảnh đối tác 21/07 | Đo lại 27/07 |
|---|---|---|
| Điểm đánh giá | **164.0**/100 · trục 0→**172** · cột **172** và **150** | **8.2**/100 · trục 7.5→**100** · cột **8.6** và **7.5** |
| Tỷ lệ tuân thủ (thẻ kế bên, neo dữ liệu) | **17.4%** | **17.4%** ✅ trùng khít |

→ `172 ÷ 8.6 = 20` và `150 ÷ 7.5 = 20`. **Cả hai cột đều đúng hệ số ÷20** — khớp mức lệch "20 lần" ở `CHANGELOG:1729`.

**b) Thang điểm thực của env đối tác** — 15 kế hoạch, 10 kết quả, **6 đã chấm** (đúng bằng "Dựa trên 6 đánh giá" trên thẻ):

| `diemTong` | Trần kế hoạch | % | `xepLoai` BE trả |
|---:|:-:|:-:|---|
| **10.00** | 10 | 100% | **`XUAT_SAC`** |
| 9.50 | 10 | 95% | `XUAT_SAC` |
| 8.90 | 10 | 89% | `TOT` |
| 8.00 | 10 | 80% | `TOT` |
| 7.90 | 10 | 79% | `TOT` |
| 5.00 | 10 | 50% | `DAT` |

`49.30 ÷ 6 = 8.216` → **khớp chính xác 8.2** trên thẻ. Mọi xếp loại khớp ngưỡng % ở `srs-fr-08-danh-gia.md:874`.

⇒ **Kết luận sắc nhất:** trên chính env đối tác đang tồn tại một kết quả **10.00/10 = `XUAT_SAC`** — tuyệt đối hoàn hảo — nhưng Dashboard gộp nó vào con số dán nhãn **"/100"**.

**c) Bằng chứng tự tố cáo trong cùng 1 viewport:** thẻ "Chất lượng đào tạo" ngay dưới ghi **"Điểm trung bình 7.3/10"** và **"Điểm kiểm tra trung bình 7.3/10"**, trong khi thẻ đánh giá phía trên với cột **8.6 / 7.5** lại ghi **"/100"**. Cùng màn, cùng độ lớn, hai mẫu số khác nhau.

![Env đối tác 27/07 — cùng bộ lọc: 8.2/100, Tỷ lệ tuân thủ 17.4% trùng ảnh đối tác](TKDGHQHTPL_02-r4-doitac-cung-boloc-8.2-tyle17.4.png)
![Env đối tác 27/07 — cột 8.6 / 7.5 dẹt sát đáy trục 100, ngay dưới là thẻ "7.3/10"](TKDGHQHTPL_02-r4-doitac-the-dao-tao-7.3tren10.png)

> **Lưu ý phạm vi:** lỗi "đếm cả bản chưa chấm / kế hoạch đã hủy" (§3.4, §3.5) **KHÔNG tái hiện trên env đối tác** — ở đó 6 bản có điểm đều đã `DA_DANH_GIA` và không có kế hoạch `HUY` nào có kết quả mang điểm. Lỗi đó phụ thuộc tiền đề dữ liệu, đã tách sang dòng `TKDGHQHTPL_OOS_01` kèm cảnh báo tiền đề cho dev.

### 3.1 BE tính điểm trên thang RIÊNG của từng kế hoạch

`diem_tong = Σ (điểm tiêu chí i × trọng số i / 100)` — BR-CALC-04 (`srs-fr-08-danh-gia.md:1239`). Với `diem_toi_da` mặc định **10** (`:1100`) và Σ trọng số = **100%**, trần thực tế của một kế hoạch là **10**, không phải 100.

| Kế hoạch | Số tiêu chí | Trần đạt được | `diemTong` | `xepLoai` | % trên trần |
|---|:-:|:-:|:-:|:-:|:-:|
| DG-20260723-0002 | 4 (trọng số 40/30/20/10) | **10** | 8.60 | `TOT` | 86% → Tốt ✅ |
| DG-20260727-0001 *(kế hoạch seed, `diemToiDa=200`)* | 1 | **200** | 100.00 | `DAT` | 50% → Đạt ✅ |
| KHDG-SEED-0001 *(dữ liệu cũ, 0 tiêu chí)* | 0 | — | 80.00 / 60.00 / 90.00 | `null` | — |

→ BE xếp loại **theo tỷ lệ phần trăm trên trần riêng của từng kế hoạch**, đúng `srs-fr-08-danh-gia.md:874` (≥90% Xuất sắc · ≥70% Tốt · ≥50% Đạt · <50% Chưa đạt). **BE đang chạy đúng đặc tả của mình.**

### 3.2 FE dashboard đóng cứng mẫu số 100

Thẻ hiển thị `"29.5/100"` và trục 0–100 (`srs-fr-01-dashboard.md:416` quy định thang 0–100).

**Hệ quả:** một kết quả **tuyệt đối hoàn hảo 10/10 — xếp loại "Xuất sắc"** sẽ hiện trên dashboard là **"10.0/100"**, trông như đạt 10%.

### 3.3 Dashboard đang trộn 3 thang điểm khác nhau vào một trung bình

Kiểm đếm toàn bộ: **16 kế hoạch · 16 kết quả · 14 bản ghi có điểm**.

```
Tổng điểm 412.40 ÷ 14 = 29.457  →  dashboard hiện 29.5/100   ✅ khớp
```

| Nhóm | Số bản ghi | Thang | Giá trị |
|---|:-:|---|---|
| Kế hoạch chuẩn (tiêu chí `diemToiDa=10`) | 11 | 0–10 | 7.70 … 8.90 |
| Kế hoạch seed `diemToiDa=200` | 1 | 0–200 | 100.00 |
| Dữ liệu cũ KHDG-SEED-0001 (0 tiêu chí) | 3 | 0–100 | 80 · 60 · 90 |

Cộng trung bình cộng 3 thang này với nhau rồi gắn nhãn "/100" ⇒ **con số 29.5 không mang ý nghĩa nào**. Các cột biểu đồ cũng vậy:

| Cột trên biểu đồ | Giá trị | Thực chất là |
|---|:-:|---|
| 02/2026 · 04/2026 · 05/2026 | 90.0 · 80.0 · 60.0 | 3 bản ghi cũ **chưa chấm**, thang 0–100 |
| 07/2026 | 16.6 | trung bình 11 bản ghi: 1 bản thang-200 (100.00) + 10 bản thang-10 |

→ Bỏ riêng bản ghi thang-200 ra thì cột 07/2026 là **8.24**; **một bản ghi lệch thang đã kéo cột lên gấp đôi**.

![Env được giao 27/07 — 29.5/100 · "Dựa trên 14 đánh giá" · cột 90/80/60/16.6](TKDGHQHTPL_02-r3-nipio-diem-29.5-tren-100.png)

### 3.4 Dashboard đếm cả bản ghi CHƯA chấm

| Chỉ số | Giá trị |
|---|:-:|
| Kết quả `DA_DANH_GIA` (đã chấm xong) | **11** |
| Kết quả `CHUA_DANH_GIA` | 5 |
| Dashboard báo "Dựa trên **N** đánh giá" | **14** |

14 = 11 đã chấm **+ 3 bản ghi `CHUA_DANH_GIA` nhưng đã có sẵn điểm** (chính 3 cột 90/80/60). Tức 3 cột cao nhất biểu đồ đến từ dữ liệu **chưa được chấm**.

### 3.5 Kế hoạch đã HỦY vẫn được tính

`DG-20260727-0001` ở trạng thái **`HUY`** nhưng kết quả 100.00 vẫn vào trung bình và vào cột 07/2026 (chính bản ghi làm cột này tăng gấp đôi). Đây là phát hiện ngoài phạm vi đã báo cáo trước đó — **nay có thêm số liệu định lượng**.

## 4. Vì sao con số ">100" của đối tác không thể do BE

`srs-fr-08-danh-gia.md:1049` — cột `diem_tong` có ràng buộc **CHECK 0–100**. Trong toàn bộ 14 bản ghi hiện có, giá trị lớn nhất là **100.00**. BE không sinh ra được 164.0 ⇒ con số đối tác chụp phát sinh ở tầng giao diện (hệ số ×20 nói ở §2).

## 5. Gốc rễ nằm ở đặc tả, không chỉ ở code

`srs-fr-01-dashboard.md:410` — FR-I-08 ghi rõ:

> **Source:** Đề xuất — **công thức tính chờ CĐT review**

Nghĩa là công thức của chính thẻ này **chưa được chốt**. Hai bên đang bám 2 đặc tả khác nhau: BE bám nhóm VI (thang riêng từng kế hoạch, xếp loại theo %), FE bám FR-I-08 (thang cứng 0–100 — `:416`, `:450`).

**Vì sao đặc tả tự mâu thuẫn:** khi nâng v3 → v3.5, BA sửa thang của Dashboard từ 1-5 lên 0-100 **căn cứ vào ràng buộc CSDL** `diem_tong CHECK BETWEEN 0 AND 100` (`srs-fr-08-danh-gia.md:1049`) — nhưng ràng buộc đó chỉ là **khoảng giá trị hợp lệ**, không phải thang chấm. Thang chấm thực tế do BR-CALC-04 quyết định: `Điểm tổng = SUM(diem_i × trọng_số_i / 100)`, với `diem_toi_da` mặc định **10** (`:1100`) và Σ trọng số = 100% thì trần chỉ là **10**. Sửa Dashboard theo ràng buộc CSDL mà không đối chiếu BR-CALC-04 chính là chỗ sinh ra lệch.

### 5.1 Sàng 3 hướng xử lý — chỉ 1 hướng sống sót

| Hướng | `:416` thang 0-100 theo `diem_tong` | `:1049` CHECK 0-100 | `:874` xếp loại % | `CHANGELOG:1729` đối chiếu được với màn chi tiết | Cộng TB chéo kế hoạch |
|---|:-:|:-:|:-:|:-:|:-:|
| (a) Dashboard quy đổi sang % | ✗ | ✓ | ✓ | **✗** | ✓ |
| (b) Giữ số thô, mẫu số theo trần từng kế hoạch | ✗ | ✓ | ✓ | ✓ | **✗** |
| **(c) Ràng buộc cấu hình để trần = 100** | ✓ | ✓ | ✓ | ✓ | ✓ |

- **(a) LOẠI.** `srs-fr-08-danh-gia.md:873` — màn chi tiết hiển thị cột *"Điểm tổng (tự tính = tổng điểm x trọng số / 100)"*, tức **số thô** (8,6). Quy đổi Dashboard sang % ⇒ Dashboard **86** vs chi tiết **8,6** cho cùng một vụ — tái tạo đúng lỗi mà `CHANGELOG:1729` đã chủ động sửa (*"nhìn biểu đồ Dashboard hiển thị '3.5' trong khi báo cáo chi tiết hiển thị '70' … không cách nào đối chiếu"*).
- **(b) LOẠI.** Mỗi kế hoạch một trần khác nhau ⇒ không cộng trung bình chéo kế hoạch được, mà đó là việc chính của thẻ.
- **(c) CHỌN.** Củng cố: dữ liệu đời trước `KHDG-SEED-0001` mang điểm **80 / 60 / 90**, tức đã ở thang 0-100 từ trước ⇒ 0-100 nhiều khả năng luôn là thiết kế gốc; `diem_toi_da` mặc định **10** (`:1100`) mới là chỗ lệch.

⇒ **Vị trí sửa: nhóm VI Đánh giá (cấu hình + validation `diem_toi_da`), KHÔNG phải Dashboard.** Thẻ Dashboard đang hiển thị đúng như `:416` mô tả.

### 5.2 BA confirm còn cần, nhưng đã thu hẹp còn 2 câu hỏi có/không

1. **Bổ sung ràng buộc còn thiếu** `Σ (diem_toi_da_i × trong_so_i / 100) = 100`. Hiện `:191` chỉ ghi *"> 0, số nguyên dương"*, `:850` UI chỉ *"number > 0"* — **không dòng nào ràng buộc tổng** (riêng trọng số đã bị ép SUM = 100% ở `:850` + BR-CALC-04). Thêm luật nghiệp vụ mới ⇒ dev không tự quyết.
2. **Duyệt migration** kế hoạch đang cấu hình `diem_toi_da = 10` và đã chấm xong — quy đổi hay chấp nhận lệch vĩnh viễn. Đụng kết quả đã chấm ⇒ cần thẩm quyền duyệt.

Cộng thêm `:410` vẫn ghi *"công thức tính chờ CĐT review"* ⇒ FR-I-08 chưa được ký chính thức.

**Lỗ hổng độc lập phát hiện kèm:** `diem_toi_da` để tự do (`:191`) trong khi `diem_tong` bị chặn CHECK 0-100 (`:1049`). Cấu hình `diem_toi_da = 200` rồi chấm 150 ⇒ `diem_tong = 150`, vi phạm chính ràng buộc đó — đã dựng thử trên env được giao, **hệ thống chấp nhận**. Câu hỏi 1 nếu được duyệt sẽ bịt luôn lỗ hổng này.

→ Dev sửa một phía mà không có công thức chốt thì sẽ lặp lại vòng lỗi. Đã ghi vào tracker: [`tasks/srs-contradictions.md` §SRS-C-009](../../../../../tasks/srs-contradictions.md).

**Phiếu gửi BA/CĐT (2 câu hỏi có/không + đủ citation):** [`ba-confirmation-needed-TKDGHQHTPL_02-r2.md`](../../ba-confirmation-needed-TKDGHQHTPL_02-r2.md).

## 6. Ghi chú độ tin cậy của phép đo

- Phần §2 (triệu chứng >100) đo **trên chính env đối tác** — kết luận áp dụng trực tiếp cho phản ánh của đối tác.
- Phần §3 (thang điểm BE/FE) đo trên **env được giao** `18.143.165.120.nip.io`, vì env đối tác trả 404 toàn bộ `/api/v1/*` trong khung giờ đo sâu (xác nhận bằng 3 lần curl; env được giao cũng từng 502, phục hồi 11:58:32). Cơ chế tính điểm là dùng chung mã nguồn nên kết luận vẫn có giá trị, nhưng **các con số cụ thể ở §3 là của env được giao**.
- Bản ghi seed do QA tạo trên env được giao: kế hoạch **DG-20260727-0001** (`b217202c-de53-4f6b-a3f9-6ec911f2dfe0`, trạng thái `HUY`, 1 tiêu chí `diemToiDa=200`, 1 kết quả 100.00) — **không xóa được**, đã ghi nhận để không nhầm là dữ liệu thật.
- **Không** seed bất kỳ dữ liệu nào lên env đối tác.

## 7. Kết luận

| Câu hỏi | Trả lời |
|---|---|
| Triệu chứng ">100" đối tác báo còn không? | **Không** — đã hết trên chính env đối tác, cùng dữ liệu (hệ số ×20 đã bỏ) |
| Giải trình "BE vs FE chưa giống nhau" đúng không? | **Đúng** — BE thang riêng từng kế hoạch (trần 10), FE đóng cứng "/100" |
| Sửa xong chưa? | **Chưa** — mới hết triệu chứng vượt trần; lệch thang, trộn thang, đếm cả bản chưa chấm và kế hoạch đã hủy vẫn còn |
| Sửa ở đâu? | **Nhóm VI Đánh giá** — ràng buộc cấu hình `diem_toi_da` để `diem_tong` đạt trần 100 (§5.1). **KHÔNG** sửa Dashboard: thẻ đang hiển thị đúng như `:416` mô tả |
| Nên để ô W ở trạng thái nào? | **`Open, BA confirm`** (đã ghi 27/07 14:2x) — phần lỗi đã đủ căn cứ chuyển dev, phần ràng buộc mới cần BA chốt |
| Cần ai quyết? | **BA/CĐT — 2 câu hỏi có/không** (§5.2): (1) bổ sung ràng buộc `Σ(diem_toi_da × trọng số/100) = 100`; (2) duyệt migration kế hoạch đã chấm. Kèm `:410` ghi "công thức tính chờ CĐT review" |

## 8. Ngoài tiêu chí BA — có gì bất thường không?

Có **2 điểm**, đều thuộc cùng thẻ dashboard nhưng khác bản chất với claim của đối tác:

1. **Đếm cả kết quả `CHUA_DANH_GIA`** vào "Dựa trên 14 đánh giá" (thực chỉ 11 đã chấm) — §3.4.
2. **Kế hoạch trạng thái `HUY` vẫn vào KPI** — §3.5. Đã được duyệt mở dòng TC mới.
