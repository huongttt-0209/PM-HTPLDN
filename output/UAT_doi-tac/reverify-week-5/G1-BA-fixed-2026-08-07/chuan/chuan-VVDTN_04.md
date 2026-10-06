# Chuẩn đối chiếu — Cụm C: `VVDTN_04` (dòng 178) — biểu đồ tròn theo lĩnh vực + bảng đủ 2 chiều

> **File này KHÔNG chứa verdict.** Chỉ là chuẩn để agent đo đối chiếu. **BA CHƯA trả lời** câu hỏi treo của
> case này (`ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md` mục 1) — chuẩn dưới đây chỉ ghi **đặc tả nói gì**,
> không thay BA quyết.
>
> **Nguồn đặc tả duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`
> (**1.295 dòng**, mtime 06/08/2026 22:52). **Mọi số dòng do chính lượt này mở file đọc lại 2026-08-07.**

---

## 🔴 CẢNH BÁO — 4/4 SỐ DÒNG BRIEF NÊU CHO CASE NÀY ĐỀU ĐÃ LỆCH

`srs-fr-11-bao-cao.md` được sửa 06/08/2026 (thêm bước kiểm vai trò, mã lỗi `ERR-RPT-08`, 2 tiêu chí chấp nhận,
ghi chú điều kiện vào màn) → nội dung trôi xuống. Bảng đối chiếu:

| Nội dung | Brief / phiếu BA / ô sheet ghi | **Dòng THẬT (2026-08-07)** | Lệch |
|---|---|---|---|
| UC124 = `Donut + Trend` | `:1064` | **`:1069`** | +5 |
| UC125 = `Bar + Trend` | `:1065` | **`:1070`** | +5 |
| UC127 = `Bar + Donut` | `:1067` | **`:1072`** | +5 |
| `theo_linh_vuc[]` điều kiện "Luôn" | `:215` | **`:218`** | +3 |

Quote theo cột giữa = quote sai bản. **Dùng cột phải.**

---

## 0. Điều kiện phải dựng lại

| Hạng mục | Yêu cầu | Căn cứ / ghi chú |
|---|---|---|
| **Vai trò ra verdict** | `cbnv_tw_04` (`CB_NV_TW`, `Test@1234`) — đúng tác nhân | `srs-fr-11-bao-cao.md:195` — *"**Tác nhân:** CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*; `:51`, `:62` |
| **Vai trò đối tác dùng khi báo lỗi** | `admin` / QTHT | 🔴 **Sau lượt sửa SRS 06/08, QTHT KHÔNG còn vào được màn báo cáo** (`:1046`, `:79`, `:127`). Nếu bản dựng đã ẩn màn với QTHT thì **không đối chứng lại bằng QTHT được nữa** — và đó là hành vi ĐÚNG, không phải chặn phép đo. Lượt 06/08 đối chứng được vì màn khi đó chưa ẩn |
| **State entity** | Không cần dựng state — báo cáo read-only | `:105` — *"Không thay đổi dữ liệu nghiệp vụ (read-only)"* |
| **Dữ liệu tiền đề — vế (b)** | Trong kỳ đã chọn phải có vụ việc **đã tiếp nhận** trải trên **≥2 kênh tiếp nhận** và **≥2 lĩnh vực PL** | Không đủ 2 giá trị thì bảng chỉ có 1 dòng → không phân biệt được "có chiều dữ liệu" với "trùng số tổng" |
| **Dữ liệu tiền đề — vế (a)** | Cùng bộ dữ liệu trên; biểu đồ chỉ render **khi có dữ liệu** | `:1059` — *"| 10 | content | Biểu đồ | chart | Tùy loại BC: Line (trend) / Bar / Stacked bar / Donut / Radar. Toggle hiện/ẩn | toggle → show/hide | **Khi có dữ liệu** |"* |
| **Bộ lọc khuyến nghị** | Loại BC = **BC Vụ việc đã tiếp nhận** · Kỳ **Năm 01/01–31/12/2026** · Đơn vị **Toàn quốc** | Bộ lọc lượt 06/08 dựng đủ 2 kênh + 4 lĩnh vực (44 vụ việc) |
| **Bộ lọc của đối tác (để đối chứng)** | Kỳ Năm 01/01–31/12/2026 · Đơn vị **Cục Bổ trợ tư pháp – BTP·TW** | Ghi ở `cau-hoi-BA-tong-hop-2026-08-06.md:105`. Lượt 06/08 đo bộ lọc này ra tổng 34, kết luận **không khác** |
| **Bản dựng + môi trường** | `https://18.143.165.120.nip.io`; tải lại trang bằng địa chỉ; ghi nhãn bản dựng trước khi đo | Luật chung lô §3. Lượt 06/08: **V1.0.8** |

⚠️ **Bẫy tiền đề chung của màn báo cáo:** bấm **[Xem báo cáo] từ 2 lần trở lên** thì hai nút Xuất bị khoá cả
phiên (phiếu riêng `BCTK_QA07`, dòng 370). Case này không cần xuất tệp, nhưng vẫn nên **tải lại trang → chọn
bộ lọc → bấm [Xem báo cáo] đúng 1 lần** để trạng thái màn sạch.

---

## 1. Vế (a) — biểu đồ tròn theo lĩnh vực: đặc tả gán loại biểu đồ nào

### 1.1 Bảng gán loại biểu đồ — nguyên văn 3 dòng brief yêu cầu

Bảng *"Mapping 23 loại BC trong Dropdown"* của `SCR-IX-01`, tiêu đề ở `:1065`, header ở `:1067`:

| Dòng | Nguyên văn |
|---|---|
| `srs-v3.5/srs-fr-11-bao-cao.md:1069` | *"| **Hỏi đáp pháp luật** | UC124 | BC Số lượng hỏi đáp/vướng mắc pháp luật | Lĩnh vực PL, Trạng thái HD | **Donut + Trend** |"* |
| 🔴 `srs-v3.5/srs-fr-11-bao-cao.md:1070` | *"| **Vụ việc** | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | **Bar + Trend** |"* |
| `srs-v3.5/srs-fr-11-bao-cao.md:1072` | *"| | UC127 | BC Vụ việc đã hoàn thành | Lĩnh vực PL, Kết quả | **Bar + Donut** |"* |

### 1.2 Kết luận đọc được từ 3 dòng trên

🔴 **ĐẶC TẢ KHÔNG GÁN DONUT CHO UC125.** Đây **không** phải chỗ đặc tả im lặng, mà là **cố ý không gán**:

- Cùng **một bảng**, cùng **một cột "Biểu đồ"**, đặc tả **có** dùng khái niệm `Donut` — gán cho **UC124**
  (`:1069`) và cho **UC127** (`:1072`).
- Riêng **UC125** (`:1070`) — chính là loại báo cáo của `VVDTN_04` — được gán **`Bar + Trend`**, không có
  `Donut`.
- Danh sách loại biểu đồ hợp lệ của màn có đủ Donut: `:1059` — *"Tùy loại BC: Line (trend) / Bar / Stacked bar
  / **Donut** / Radar"*. Tức công cụ có sẵn, đặc tả chọn không dùng cho UC125.

⇒ **Kỳ vọng của đối tác (phải có biểu đồ tròn theo lĩnh vực) NGƯỢC với đặc tả hiện hành.** Đây là lý do case
này treo chờ BA, không phải lý do để chấm Fail dev.

### 1.3 Đặc tả đòi gì về chiều lĩnh vực — dữ liệu, không phải hình thức trình bày

> `srs-v3.5/srs-fr-11-bao-cao.md:218` — *"| 3 | theo_linh_vuc[] | structured | **Luôn** | {linh_vuc, ten, so_luong} |"*

Điều kiện **"Luôn"** = chiều lĩnh vực **bắt buộc phải có trong mọi lần tạo báo cáo**. Nhưng cột này nằm ở bảng
**Output đặc thù** (`:212–220`) — nói **phải có dữ liệu gì**, **không** nói phải trình bày bằng biểu đồ hay
bằng bảng.

Tiêu chí chấp nhận của chính FR cũng chỉ đòi *"phân theo"*, không đòi dạng trình bày:

> `srs-v3.5/srs-fr-11-bao-cao.md:223` — *"- **Given** CB chọn kỳ Tháng **When** tạo BC **Then** hiển thị tổng VV
> tiếp nhận, phân theo kênh + lĩnh vực"*

⇒ **Đặc tả IM LẶNG** về việc chiều lĩnh vực phải hiện dưới dạng **biểu đồ** hay **bảng**. Chỉ chốt: **phải có
dữ liệu theo lĩnh vực**, và **loại biểu đồ của UC125 là `Bar + Trend`**.

---

## 2. Vế (b) — bảng đủ chiều "Theo kênh" và "Theo lĩnh vực"

### 2.1 Chiều dữ liệu bắt buộc của UC125 (Output đặc thù, `:212–220`)

| Dòng | Nguyên văn | Ghi chú |
|---|---|---|
| `:216` | *"| 1 | tong_vu_viec | number | Luôn | Tổng số VV tiếp nhận |"* | |
| 🔴 `:217` | *"| 2 | theo_kenh[] | structured | **Luôn** | {kenh, so_luong} |"* | **vế (b) — chiều "Theo kênh"** |
| 🔴 `:218` | *"| 3 | theo_linh_vuc[] | structured | **Luôn** | {linh_vuc, ten, so_luong} |"* | **vế (b) — chiều "Theo lĩnh vực"** |
| `:219` | *"| 4 | theo_don_vi[] | structured | Luôn | {don_vi, ten, so_luong} |"* | |
| `:220` | *"| 5 | theo_ky[] | structured | Luôn | {ky, so_luong} |"* | |

Bổ trợ:

- `:208` — *"**Dimensions:** Kỳ, Đơn vị, Kênh tiếp nhận, Lĩnh vực PL"*
- `:210` — *"**Processing đặc thù (Bước 5):** Tổng hợp theo đơn vị, kênh tiếp nhận, lĩnh vực, kỳ thời gian"*
- `:206` — *"**Công thức:** Đếm số vụ việc đã tiếp nhận (**trừ từ chối**) trong kỳ, theo phạm vi đơn vị"*
  ← dùng để tự tính lại độc lập từ danh sách vụ việc
- `:203` — *"| 1 | kenh_tiep_nhan | text | N | **DVC / HE_THONG_KHAC / TRUC_TIEP / BUU_CHINH / DIEN_THOAI** | — | Chọn |"*
  ← tập giá trị hợp lệ của chiều kênh
- `:1060` — *"| 11 | content | Bảng dữ liệu | table | Nhóm theo chiều phân tích tùy loại BC. Cột sắp xếp. Sticky header. Hàng tổng cộng (bold) | sort → reorder | Khi có dữ liệu |"*

### 2.2 Chuẩn chấm vế (b) — 3 phép

1. **Có mặt cả 2 chiều.** Trên màn phải đọc được cả nhóm số **theo kênh tiếp nhận** và nhóm số **theo lĩnh vực
   pháp luật** (`:217`, `:218` — điều kiện "Luôn").
2. **Cộng khớp tổng.** Tổng từng chiều phải bằng `tong_vu_viec` (`:216`). Lượt 06/08: kênh 41+3 = 44; lĩnh vực
   16+13+12+3 = 44.
3. **Đối chứng độc lập.** Tự đếm lại từ danh sách vụ việc theo công thức `:206` (*đã tiếp nhận, trừ từ chối*)
   rồi so. Lượt 06/08: 45 bản ghi − 1 `TU_CHOI` = 44, khớp y hệt.

⚠️ **KHÔNG được chấm Fail vì nhãn cột không đúng chữ "Theo kênh" / "Theo lĩnh vực".** SRS không quy định nhãn
cột cho màn báo cáo — `:217`/`:218` chỉ đặt tên **trường dữ liệu** (`theo_kenh[]`, `theo_linh_vuc[]`). Lượt
06/08 ghi nhận màn dùng nhãn *"Kênh tiếp nhận"* và *"Thống kê theo lĩnh vực pháp luật"* và **không chấm lỗi vì
tên cột**. Chấm theo **khái niệm chiều dữ liệu**.

---

## 3. Hai vế là hai phép đo riêng — bảng tóm tắt

| Vế | Đặc tả nói gì | Quan hệ với kỳ vọng đối tác | Đo bằng gì |
|---|---|---|---|
| **(a) Biểu đồ tròn theo lĩnh vực** | UC125 = `Bar + Trend` (`:1070`); Donut cố ý gán cho UC124 (`:1069`) và UC127 (`:1072`), **không** cho UC125. Đặc tả **im lặng** về việc chiều lĩnh vực phải là biểu đồ hay bảng | **NGƯỢC** — đối tác đòi thứ đặc tả cố ý không gán | Đếm và **ghi rõ tên từng biểu đồ** đang render trên màn: có mấy biểu đồ, mỗi cái loại gì, vẽ theo chiều nào. Có biểu đồ **tròn theo lĩnh vực** hay không |
| **(b) Bảng có chiều Theo kênh + Theo lĩnh vực** | `:217` + `:218` điều kiện **"Luôn"** — bắt buộc | **KHỚP** — kỳ vọng đối tác có cơ sở đặc tả | 3 phép ở §2.2 |

**Quy tắc chốt verdict của lô** đã ghi ở `00-BRIEF-CHUNG.md` §Cụm C (3 nhánh: có donut + (b) đạt → Pass · vẫn
không có donut → `BA confirm`, **không** Reopen, **không** Pass · (b) tái hiện → Reopen). **File này không lặp
lại và không thay thế bảng đó** — agent đo đọc thẳng brief.

**Hai vế đo độc lập, không suy vế nọ sang vế kia.** Lượt 06/08 đã đo: (b) **không còn tái hiện**; (a) hiện
trạng là **không có biểu đồ tròn**, màn render biểu đồ **cột** theo kênh + biểu đồ **đường** theo kỳ — đúng
`Bar + Trend` của `:1070`.

---

## 4. Bẫy chấm sai

### 4.1 Bẫy **FAIL / Reopen oan**

1. 🔴 **Chấm Fail vế (a) vì không có biểu đồ tròn.** Không có donut là **đúng `:1070`**. Đây là điểm **BA chưa
   trả lời** — QA không tự bác đối tác, cũng không tự bác đặc tả.
2. **Chấm Fail vế (b) vì nhãn cột lệch chữ.** Xem §2.2.
3. **Chấm Fail vì thiếu chiều "theo đơn vị" hoặc "theo kỳ".** Hai chiều đó (`:219`, `:220`) cũng là "Luôn"
   nhưng **không thuộc 2 vế của phiếu này** — thiếu thì **ghi nhận riêng**, không kéo verdict `VVDTN_04`.
4. **Chấm Fail vì số liệu khác ảnh nghiệm thu của đối tác.** Khác env, khác bản dựng, khác dữ liệu. Điều phải
   đúng là **các chiều cộng khớp tổng** và **khớp phép đếm lại độc lập** (§2.2 phép 2 + 3).
5. **Chấm Fail vì QTHT không vào được màn.** Sau lượt sửa SRS 06/08 thì **đó là hành vi đúng** (`:79`,
   `:1046`, `:127`) và cũng chính là việc dev đang phải làm cho cụm A. Không phải lỗi của case này.
6. **Chấm Fail vì biểu đồ không hiện khi báo cáo rỗng.** `:1059` điều kiện *"Khi có dữ liệu"*.
7. **Tab mở lâu chạy bó mã cũ.** Tải lại trang bằng địa chỉ, ghi nhãn bản dựng.

### 4.2 Bẫy **PASS oan**

1. 🔴 **Thấy có biểu đồ tròn ở đâu đó trên màn là Pass vế (a).** Phải là biểu đồ tròn **theo chiều lĩnh vực**.
   Donut vẽ theo **kênh tiếp nhận** hay theo **đơn vị** thì không phải thứ đối tác đòi.
2. 🔴 **Thấy có bảng lĩnh vực là Pass vế (b).** Còn phải cộng khớp tổng **và** khớp phép đếm lại độc lập theo
   `:206`. Số hiện ra mà sai bản chất (vd không trừ vụ việc từ chối) vẫn "nhìn thấy được".
3. **Chỉ đo 1 chiều.** Vế (b) có **2** chiều — kênh **và** lĩnh vực. Đo một chiều là chưa xong vế.
4. **Bộ lọc chỉ có 1 giá trị.** Nếu kỳ đang chọn chỉ có 1 kênh hoặc 1 lĩnh vực thì bảng 1 dòng luôn "cộng
   khớp tổng" → **không chứng minh được gì**. Bắt buộc dựng bộ lọc có **≥2 kênh và ≥2 lĩnh vực**.
5. **Dùng `admin` để đo.** Không phải tác nhân (`:195`), và nếu bản dựng đã ẩn màn với QTHT thì cũng không vào
   được. Đo bằng `cbnv_tw_04`.

---

## 5. Danh sách CHƯA XÁC MINH ĐƯỢC — agent đo phải tự xác nhận trên màn

| # | Điểm | Vì sao chưa xác minh được từ file | Phải làm gì |
|---|---|---|---|
| C-1 | Bản dựng hôm nay đã bổ sung biểu đồ tròn theo lĩnh vực chưa | Không có ảnh chụp bản dựng hôm nay trong repo; lượt 06/08 (V1.0.8) là **không có** | Chụp trọn vùng biểu đồ, **ghi rõ số lượng + loại + chiều** của từng biểu đồ đang render |
| C-2 | Nhãn thật của 2 bảng chiều kênh / chiều lĩnh vực | SRS chỉ đặt tên **trường dữ liệu** (`theo_kenh[]`, `theo_linh_vuc[]`), không quy định nhãn hiển thị | Ghi nguyên văn nhãn; chấm theo khái niệm |
| C-3 | Kỳ / đơn vị nào hiện có ≥2 kênh và ≥2 lĩnh vực | Không có ảnh chụp state hiện tại | Bắt đầu bằng Kỳ Năm 2026 · Toàn quốc; nếu chỉ ra 1 giá trị thì đổi kỳ/đơn vị trước khi kết luận |
| C-4 | Có còn đối chứng được bằng vai trò QTHT không | Phụ thuộc dev đã ẩn màn với QTHT chưa (việc của cụm A) | Thử 1 lần; **bị chặn = ghi nhận là đúng đặc tả**, bỏ nhánh đối chứng đó, KHÔNG chấm Fail |
| C-5 | Đường dẫn / tham số thật của màn báo cáo ở bản dựng hôm nay | Lượt 06/08 dùng `/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=…&denNgay=…`; SRS không đặc tả đường dẫn | Ghi lại địa chỉ thật sau khi chọn bộ lọc; **không đoán** |
| C-6 | Chuỗi hiển thị thật của option *"BC Vụ việc đã tiếp nhận"* trong dropdown | SRS quy định khuôn *"[Mã UC] Tên BC"* (`:1052`) + tên ở `:1070`; chưa biết chữ thật trên màn | Ghi lại chính xác tên option đã chọn |
