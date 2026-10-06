# Báo cáo đo — THBCTHCT_05 (dòng 345) — "Xuất tệp báo cáo tổng hợp (Excel/Word)"

> **Chuẩn chấm đã khóa:** [`chuan/THBCTHCT_05.md`](../chuan/THBCTHCT_05.md) — 8 vế:
> **C0–C5 + C8 MATCH** · **C6 DIFF** (chức danh người ký) · **C7 DIFF** (khuôn tên tệp).
> **Đặc tả nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> + cross-ref do chính `:1017` khai sang `srs-v3.5.md` §D.2.4 và Phụ lục E §H8.
> **Verdict:** ⚠️ **Cần BA** (`BA confirm`) — cả 6 vế MATCH đều ĐẠT trên **cả hai định dạng**,
> còn C6 + C7 là DIFF nên theo flow 04 §Verdict không được chấm Pass.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo

- 13:55 ngày 07/08/2026 — đọc lại dòng 345 tab `bug`.
- `Mã TC` = `THBCTHCT_05` · `Trạng thái dev fix` = `Fixed` · `Kết quả verify` = **RỖNG**.
- `Trạng thái` = `N/R`, `Kết quả thực tế` rỗng, không ảnh ⇒ **đối tác chưa từng chạy phiếu này**
  ⇒ chuẩn chấm lấy nguyên văn cột `Kết quả mong đợi` (K345) đối chiếu đặc tả (QĐ-03).

## 1. 🔴 Môi trường · dấu vân tay bản dựng — **ĐÃ ĐỔI GIỮA PHIÊN**

| Mốc | Bó mã giao diện | `last-modified` |
|---|---|---|
| **Đầu phiên** (12:40) và kiểm lại 13:15:28 | `assets/index-eWHwDgt2.js` | `Fri, 07 Aug 2026 02:11:03 GMT` (09:11 giờ VN) |
| **13:55:5x** (ngay trước khi đo phiếu này) | **`assets/index-BbPPdate.js`** | **`Fri, 07 Aug 2026 06:47:57 GMT`** (**13:47:57 giờ VN**) |

🔴 **Có một lượt lên bản mới lúc 13:47:57 giờ VN**, tức **sau khi đo xong 3 phiếu đầu và trước khi đo
phiếu này**. Phân định quan sát:

| Phiếu | Mốc đo | Bản dựng |
|---|---|---|
| TPDBCKQTHCT_02 (341) | 12:55–13:02 | `index-eWHwDgt2.js` (bản **cũ**) |
| THBCTHCT_02 (344) | 13:18–13:29 | `index-eWHwDgt2.js` (bản **cũ**) |
| THBCTHCT_01 (343) | 13:30–13:45 | `index-eWHwDgt2.js` (bản **cũ**) |
| **THBCTHCT_05 (345)** | **13:56–13:57** | **`index-BbPPdate.js` (bản MỚI)** |

**Đối chứng ảnh hưởng của lượt lên bản:** tệp Excel xuất lúc **13:32** (bản cũ, trong lúc đo 343) và tệp
Excel xuất lúc **13:56** (bản mới, phiếu này) **trùng khít từng ô nội dung** — đối chiếu chương trình 29×3 ô,
0 ô lệch (`md5` khác nhau là do dấu thời gian bên trong gói tệp). ⇒ Lượt lên bản **không** làm đổi kết quả
quan sát của phiếu này. Trang hiện đang chạy đúng bó mã mới (`document.querySelectorAll('script[src]')` =
`/assets/index-BbPPdate.js`).

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` |
| Tài khoản ra verdict | **`cbnv_tw_05`** — `CB_NV_TW`, cấp TW, `donViId 00000000-0000-4000-8000-000000000001` (lý do dùng #05 thay #03 khai ở [`do/THBCTHCT_02.md` §1](THBCTHCT_02.md)) |
| Tài khoản khác | **không dùng** cho phiếu này. Không dùng `admin`. |

## 2. Tiền đề — điều kiện H345 mục 2

Điều kiện phiếu: *"Đã hoàn thành tổng hợp báo cáo toàn quốc và NSD là cán bộ nghiệp vụ cấp TW."*

Kiểm sống lúc 13:55 (mở lại màn `/ct-htpldn/tong-hop` bằng địa chỉ, phiên vẫn sống):
- Hai báo cáo `c4801d2d…` (Bộ KH&ĐT) và `df6498aa…` (Sở TP An Giang) — cùng đợt `DOT-THBC01-UAT`,
  kỳ `SO_BO_6_THANG` — đọc lại được ở trạng thái **"Đã tổng hợp"**, tức bản tổng hợp toàn quốc lưu ở
  phiếu 343 (bản ghi `TH-TW-1786084251126`) **vẫn còn nguyên trên máy chủ** ⇒ điều kiện H345 mục 2 **đạt**.
- Báo cáo thứ ba (Sở TP Hà Nội, đợt khác) vẫn "Đã gửi TW" — không chọn.

**Bước chốt (khung chuẩn §2.2):** **không phải chạy** — sau khi tick chọn 2 báo cáo, hai nút
**[Xuất Excel]** và **[Xuất Word]** đã **bật sáng** ngay (ảnh 01), không bị chặn. Không gọi
`POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop`.

**Số liệu bản tổng hợp đã lưu — dùng để đối chiếu C8** (lấy từ phản hồi tạo bản ghi lúc 13:30:51, phiếu 343):
`12 · 4 · 3 · 7 · 7 · 37 · 29 · 7 · 14 · 8 · 680000000 · 160000000 · 30000000`.

## 3. Thao tác đã thực hiện (bằng giao diện thật)

Trên màn **"Tổng hợp báo cáo toàn quốc"** (`/ct-htpldn/tong-hop`), tài khoản `cbnv_tw_05`:

1. Tick 2 dòng Bộ KH&ĐT + Sở TP An Giang → nút **[Tổng hợp (2)]** ở trạng thái **mờ/không bấm được**
   (đúng: hai báo cáo đã tổng hợp rồi), hai nút **[Xuất Excel]** / **[Xuất Word]** **bật sáng** — ảnh 01.
2. Bấm **[Xuất Excel]** lúc **13:56:30**.
3. Bấm **[Xuất Word]** lúc **13:57:08** — ảnh 02.

**Cách thu tệp** (chuẩn §3 — khai rõ đã dùng cách nào): trình duyệt cách ly **không** đổ tệp ra thư mục tải
xuống ⇒ dùng **cách 2** — lấy **nguyên nội dung nhị phân của chính phản hồi mà lượt bấm sinh ra** rồi ghi
ra đĩa, **không** gọi lại đường dẫn xuất tệp. Kiểm tra tệp thu được:

| Lượt bấm | Đường dẫn máy chủ do chính lượt bấm gọi | Thân yêu cầu | Mã | `content-disposition` | Cỡ | Kiểu tệp thực (`file`) |
|---|---|---|---|---|---|---|
| [Xuất Excel] 13:56:30 | `POST /api/v1/dot-bao-caos/tong-hop/export` | `{"baoCaoIds":["c4801d2d…","df6498aa…"],"format":"xlsx"}` | **200** | `attachment; filename="BaoCaoTongHopCTHTPL_20260807_1356.xlsx"` | 7.957 B | `Microsoft Excel 2007+` |
| [Xuất Word] 13:57:08 | `POST /api/v1/dot-bao-caos/tong-hop/export` | `{"baoCaoIds":["c4801d2d…","df6498aa…"],"format":"docx"}` | **200** | `attachment; filename="BaoCaoTongHopCTHTPL_20260807_1357.docx"` | 9.848 B | `Microsoft Word 2007+` |

Đoạn `{YYYYMMDD_HHmm}` trong tên tệp (`…_1356` / `…_1357`) **trùng khít mốc giờ bấm** ⇒ đúng tệp của lượt
này, không phải tệp cũ (chống bẫy PASS oan #2).

## 4. Bảng đo — định dạng **`.xlsx`** (đọc bằng `openpyxl` 3.1.5)

Tệp: [`files/BaoCaoTongHopCTHTPL_20260807_1356.xlsx`](../files/BaoCaoTongHopCTHTPL_20260807_1356.xlsx)

| Vế | Đo được | Kết quả |
|---|---|---|
| **C0** | Mở được bằng `openpyxl`; **1 sheet** tên `Biểu mẫu 21a TP HTPLDN`; vùng dữ liệu `A1:C29` | ✅ ĐẠT |
| **C1** | `ws.page_setup.paperSize` = **`9`** (mã khổ **A4** theo ECMA-376) · `orientation` = `portrait` | ✅ ĐẠT |
| **C2** | Thân bảng chỉ tiêu — **đọc 42 ô** (hàng tiêu đề `A8:C8` + 13 hàng chỉ tiêu `A9:C21`): **tất cả 42/42** `font.name = 'Times New Roman'`, `font.size = 13.0`, **0 ô lệch** | ✅ ĐẠT |
| **C3** | `B1` = `'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM'` · `B2` = `'Độc lập - Tự do - Hạnh phúc'` | ✅ ĐẠT |
| **C4** | `A1` = `'BỘ TƯ PHÁP'` | ✅ ĐẠT |
| **C5** | `C23` = `'Ngày 07 tháng 08 năm 2026'` | ✅ ĐẠT |
| **C6** | *(DIFF — chỉ ghi nhận)* khối cuối tệp: `C23` ngày ký · `C24` `'NGƯỜI XUẤT BÁO CÁO'` (in đậm) · `C25` `'(Ký, ghi rõ họ tên và đóng dấu)'` · `C29` `'CB Nghiệp vụ - Trung ương #05'` (họ tên cán bộ xuất). **KHÔNG có dòng chức danh/chức vụ in sẵn** | 🔎 không chấm |
| **C7** | *(DIFF — chỉ ghi nhận)* tên tệp nguyên văn từ `content-disposition`: **`BaoCaoTongHopCTHTPL_20260807_1356.xlsx`** — viết liền `BaoCaoTongHopCTHTPL`, **không** có dấu gạch dưới giữa `TongHop` và `CTHTPL` | 🔎 không chấm |
| **C8** | Bảng 13 chỉ tiêu — xem bảng đối chiếu §6 | ✅ ĐẠT 13/13 |

**Ngoài thân bảng (ghi nhận, không chấm — bẫy FAIL oan #3):** `A4` tiêu đề `'BÁO CÁO TỔNG HỢP KẾT QUẢ THỰC
HIỆN CHƯƠNG TRÌNH HỖ TRỢ PHÁP LÝ CHO DOANH NGHIỆP'` = TNR **14** in đậm; `A5` `'Biểu mẫu 21a/TP/HTPLDN
(Theo Thông tư số 17/2025/TT-BTP)'` = TNR **11**; `C25` = TNR **11**; `A6` = `'THBCTHCT_01 - Đợt báo cáo sơ
bộ 6 tháng 2026 (seed UAT) — Kỳ báo cáo: SO_BO_6_THANG'` = TNR 13. Các ô **rỗng** (`A2`, `A23:B25`, `A29`)
mang phông mặc định `Calibri 11` — không có nội dung nên không tính vào thân bảng.

**Quốc hiệu đặt ở hàng đầu của sheet, không ở "header trang in"** (`ws.oddHeader` rỗng) — đúng như bẫy FAIL
oan #4 đã lường: `:6721` không quy định chỗ đặt trong tệp bảng tính ⇒ **đạt**.

**Lề trang (ngoài phạm vi chấm — §1.2, ghi nhận):** `page_margins` = trái `1.18"` ≈ **3,0 cm**, phải/trên/dưới
`0.79"` ≈ **2,0 cm** — **khớp** `srs-v3.5.md:6724`.

## 5. Bảng đo — định dạng **`.docx`** (đọc bằng `python-docx`)

Tệp: [`files/BaoCaoTongHopCTHTPL_20260807_1357.docx`](../files/BaoCaoTongHopCTHTPL_20260807_1357.docx)

| Vế | Đo được | Kết quả |
|---|---|---|
| **C0** | Mở được bằng `python-docx`; **9 đoạn văn + 2 bảng** | ✅ ĐẠT |
| **C1** | `section.page_width` = **21,00 cm** · `section.page_height` = **29,70 cm** · `orientation = PORTRAIT` | ✅ ĐẠT (A4) |
| **C2** | `word/styles.xml` → `docDefaults/rPrDefault/rPr`: `w:rFonts ascii/hAnsi/cs/eastAsia = "Times New Roman"`, `w:sz w:val="26"` = **13pt**. Thân tệp: bảng chỉ tiêu **14 hàng × 3 cột = 42 ô**, **tất cả 42/42** run khai `Times New Roman` và **không** đặt cỡ riêng ⇒ thừa hưởng đúng **13pt**; **0 ô lệch** | ✅ ĐẠT |
| **C3** | Bảng đầu tệp, ô phải: `'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\nĐộc lập - Tự do - Hạnh phúc'` | ✅ ĐẠT |
| **C4** | Bảng đầu tệp, ô trái: `'BỘ TƯ PHÁP'` | ✅ ĐẠT |
| **C5** | Đoạn 5 (căn phải): `'Ngày 07 tháng 08 năm 2026'` | ✅ ĐẠT |
| **C6** | *(DIFF — chỉ ghi nhận)* đoạn 6 `'NGƯỜI XUẤT BÁO CÁO'` (đậm) · đoạn 7 `'(Ký, ghi rõ họ tên và đóng dấu)'` · đoạn 8 `'CB Nghiệp vụ - Trung ương #05'` (đậm). **KHÔNG có dòng chức danh/chức vụ in sẵn** | 🔎 không chấm |
| **C7** | *(DIFF — chỉ ghi nhận)* **`BaoCaoTongHopCTHTPL_20260807_1357.docx`** | 🔎 không chấm |
| **C8** | Bảng 13 chỉ tiêu — xem §6 | ✅ ĐẠT 13/13 |

**Ngoài thân tệp (ghi nhận):** đoạn 1 tiêu đề TNR **15** in đậm; đoạn 2 `'Biểu mẫu 21a/TP/HTPLDN (Theo Thông
tư số 17/2025/TT-BTP)'` TNR **11**; đoạn 7 TNR **11**. `section.header` / `section.footer` **rỗng** — quốc
hiệu + tên cơ quan đặt ở bảng đầu thân văn bản (đạt, cùng lý do §4).
**Lề (ngoài phạm vi chấm):** trái **3,00 cm** · phải **2,00 cm** · trên **2,00 cm** · dưới **2,00 cm** —
khớp `:6724`.

## 6. Vế C8 — đối chiếu từng chỉ tiêu

| # | Chỉ tiêu (nguyên văn trong tệp) | Trong `.xlsx` | Trong `.docx` | Bản tổng hợp đã lưu | Khớp |
|---|---|---|---|---|---|
| 1 | 1. Số TVV kiện toàn | 12 | 12 | 12 | ✅ |
| 2 | 2. Cuộc tập huấn | 4 | 4 | 4 | ✅ |
| 3 | 3. Hội nghị đối thoại | 3 | 3 | 3 | ✅ |
| 4 | 4. VB trả lời UBND | 7 | 7 | 7 | ✅ |
| 5 | 5. VB TV mạng lưới TVV | 7 | 7 | 7 | ✅ |
| 6 | 6. HS tiếp nhận | 37 | 37 | 37 | ✅ |
| 7 | 7. HS giải quyết tổng | 29 | 29 | 29 | ✅ |
| 8 | 8. DN vừa | 7 | 7 | 7 | ✅ |
| 9 | 9. DN nhỏ | 14 | 14 | 14 | ✅ |
| 10 | 10. DN siêu nhỏ | 8 | 8 | 8 | ✅ |
| 11 | 11. KP hỗ trợ TVPL (NSNN) | 680000000 | 680.000.000 | 680000000 | ✅ |
| 12 | 12. KP chi HĐ khác | 160000000 | 160.000.000 | 160000000 | ✅ |
| 13 | 13. KP xã hội hóa | 30000000 | 30.000.000 | 30000000 | ✅ |

⇒ **13/13 khớp ở cả hai định dạng.** Tệp còn ghi đúng biểu mẫu đang dùng
(`Biểu mẫu 21a/TP/HTPLDN (Theo Thông tư số 17/2025/TT-BTP)`) và đúng đợt/kỳ (`THBCTHCT_01 - Đợt báo cáo sơ
bộ 6 tháng 2026 (seed UAT) — Kỳ báo cáo: SO_BO_6_THANG`).

> ⚠️ **Khai thẳng một giới hạn của phép đối chiếu:** thân yêu cầu xuất tệp chỉ gửi `baoCaoIds` + `format`,
> và bản dựng **không có** đường đọc lại bản ghi tổng hợp (tra `/api/docs-json`: `bao-cao-ct-htpl/{id}` chỉ
> có `chinh-sua-tong-hop` (sửa) và `hoan-thanh-tong-hop` (ghi), **không có** `GET`). Do đó **không phân biệt
> được** máy chủ đang *đọc bản ghi đã lưu* hay *cộng lại từ danh sách báo cáo*. Với vế C8 điều này **không
> đổi kết quả** — phiếu chỉ đòi *số trong tệp khớp số của bản tổng hợp đã lưu*, và 13/13 khớp. Nêu ra để
> người đọc không suy rộng thành "đã chứng minh tệp đọc từ bản ghi".

## 7. Kết luận theo từng vế

| Vế | Quan hệ (đã khóa) | `.xlsx` | `.docx` |
|---|---|---|---|
| **C0** tạo được tệp, mở đúng định dạng | MATCH | ✅ | ✅ |
| **C1** khổ A4 | MATCH | ✅ (`paperSize 9`) | ✅ (21,00 × 29,70 cm) |
| **C2** Times New Roman 13 (thân tệp) | MATCH | ✅ 42/42 ô | ✅ 42/42 ô |
| **C3** quốc hiệu đầu tệp | MATCH | ✅ | ✅ |
| **C4** tên cơ quan đầu tệp | MATCH | ✅ | ✅ |
| **C5** ngày ký cuối tệp | MATCH | ✅ | ✅ |
| **C6** chức danh người ký | **DIFF** | 🔎 không có dòng chức danh in sẵn | 🔎 như `.xlsx` |
| **C7** khuôn tên tệp | **DIFF** | 🔎 `BaoCaoTongHopCTHTPL_20260807_1356.xlsx` | 🔎 `BaoCaoTongHopCTHTPL_20260807_1357.docx` |
| **C8** số liệu khớp bản đã lưu | MATCH | ✅ 13/13 | ✅ 13/13 |

**Verdict phiếu:** ⚠️ **Cần BA** → ô `Trạng thái dev fix` = **`BA confirm`**
(chuẩn §4: *"Còn C6 + C7 = DIFF ⇒ verdict logic của phiếu là Cần BA, KHÔNG phải Pass — kể cả khi 6 vế MATCH
đều đạt"*).

## 8. Hai câu hỏi cho nghiệp vụ

### 8.1 C6 — cuối tệp có phải in sẵn dòng chức danh người ký không

> **CẦN BA CONFIRM:** phiếu kỳ vọng *"cuối trang có ngày ký và **chức danh người ký**"*. Đặc tả quy định
> **ngược lại**: `srs-fr-15-ct-htpldn.md:1017` khai khối ký cuối trang gồm *"ngày ký + họ tên cán bộ xuất báo
> cáo + chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức — **không in sẵn dòng chức danh**"*, và
> `srs-v3.5.md:6723` nêu ngoại lệ chung cho mọi tệp xuất `[BA chốt 2026-08-04, mở rộng phạm vi 2026-08-06]`
> với hai căn cứ: hồ sơ tài khoản không lưu chức vụ nên không có nguồn dữ liệu, và biểu mẫu gốc 21a/21b để
> trống chỗ này cho người ký tự ghi khi ký tay.
>
> **Web/dev hiện tại:** khối cuối tệp (giống nhau ở cả `.xlsx` và `.docx`) gồm **ngày ký** → dòng
> **"NGƯỜI XUẤT BÁO CÁO"** → dòng **"(Ký, ghi rõ họ tên và đóng dấu)"** → **họ tên cán bộ xuất**
> ("CB Nghiệp vụ - Trung ương #05"). **Không có dòng chức danh/chức vụ in sẵn** ⇒ đúng ngoại lệ SRS, lệch
> kỳ vọng phiếu.
>
> **Câu hỏi BA:** phiếu UAT 345 viết trước hay sau chốt 2026-08-06? Tệp xuất của nhóm XI có phải **in sẵn**
> dòng chức danh người ký không, hay giữ đúng ngoại lệ §D.2.4 (chỉ chừa chỗ trống)? Nếu giữ ngoại lệ, xin
> xác nhận để cập nhật lại kỳ vọng của phiếu.

### 8.2 C7 — khuôn tên tệp lệch đúng một dấu gạch dưới

> **CẦN BA CONFIRM:** phiếu kỳ vọng **`BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}`**; đặc tả quy định
> **`BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}.{ext}`** (`srs-fr-15-ct-htpldn.md:1017`, `[BA chốt 2026-08-06]`)
> theo khuôn Phụ lục E §H8 (`srs-v3.5.md:6760`) — `{TenTep}` viết liền PascalCase, dấu gạch dưới chỉ dùng
> để ngăn các đoạn, và `CTHTPL` không phải một trường đã khai trong entity nên không thể là `{DinhDanh}`.
>
> **Web/dev hiện tại:** **`BaoCaoTongHopCTHTPL_20260807_1356.xlsx`** và
> **`BaoCaoTongHopCTHTPL_20260807_1357.docx`** — viết liền, đúng khuôn `:1017`/§H8, lệch kỳ vọng phiếu đúng
> một dấu gạch dưới.
>
> **Câu hỏi BA:** chốt một khuôn duy nhất — `BaoCaoTongHopCTHTPL_…` (theo §H8) hay `BaoCaoTongHop_CTHTPL_…`
> (theo phiếu UAT)? Chốt xong xin sửa cho khớp giữa `:1017` và phiếu.

## 9. Ghi nhận cho dev (không ảnh hưởng verdict)

1. **Không có thông báo nào sau khi xuất tệp** — bấm [Xuất Excel] / [Xuất Word] không hiện thông báo thành
   công. FR-XI-09 **không khai** mã thông báo nào cho thao tác xuất (chỉ `:1032` cho lưu tổng hợp) ⇒
   **vùng đặc tả im lặng, không chấm**; nêu để BA cân nhắc bổ sung.
2. **Tệp Word không dùng phần đầu trang/chân trang của văn bản** (`section.header` / `section.footer` rỗng);
   quốc hiệu, tên cơ quan, khối ký đều nằm trong thân văn bản. Khi văn bản dài sang nhiều trang thì quốc
   hiệu sẽ không lặp lại. Đặc tả không quy định chỗ đặt ⇒ không chấm, nêu để dev cân nhắc.
3. **Dòng "họ tên cán bộ xuất báo cáo" đang lấy đúng trường họ tên của tài khoản** (`CB Nghiệp vụ - Trung
   ương #05`) — với tài khoản thật thì đây sẽ là họ tên người dùng, đúng `:1017`; nêu để dev lưu ý dữ liệu
   mẫu trên môi trường nội bộ trông giống một chức danh.
4. **Không có đường đọc lại bản ghi tổng hợp** — đã nêu ở [`do/THBCTHCT_01.md` §5](THBCTHCT_01.md).

## 10. 🔴 Dữ liệu đã thay đổi trên môi trường

**KHÔNG có.** Phiếu này chỉ **đọc**: hai lượt `POST …/tong-hop/export` là thao tác sinh tệp, không tạo và
không sửa bản ghi nào. Kiểm lại sau khi đo: đợt `DOT-THBC01-UAT` vẫn `DA_TONG_HOP`, hai báo cáo vẫn
"Đã tổng hợp", báo cáo Sở TP Hà Nội vẫn "Đã gửi TW" (ảnh 02).

*(Thay đổi dữ liệu của cả lô nằm ở [`do/THBCTHCT_01.md` §7](THBCTHCT_01.md) và
[`do/TPDBCKQTHCT_02.md`](TPDBCKQTHCT_02.md).)*

## 11. Bằng chứng

| # | Tệp | Chứng minh | Link |
|---|---|---|---|
| 01 | `image/THBCTHCT_05-01-chon-2-bc-da-tong-hop-nut-xuat-bat.png` | Tiền đề: 2 báo cáo "Đã tổng hợp" được chọn; [Tổng hợp (2)] mờ; [Xuất Excel] + [Xuất Word] bật sáng | https://drive.google.com/file/d/1B6sNDKhHrkbDvMcnt3vbDzWN9TVlhgTm/view?usp=drivesdk |
| 02 | `image/THBCTHCT_05-02-sau-khi-bam-xuat-excel-va-xuat-word.png` | Ngay sau hai lượt bấm xuất: không thông báo, trạng thái các dòng không đổi | https://drive.google.com/file/d/1LZrn-4tBkcpgxb-YlhCAPRkxMQtD5xOQ/view?usp=drivesdk |
| 03 | `files/BaoCaoTongHopCTHTPL_20260807_1356.xlsx` | Tệp Excel do chính lượt bấm 13:56:30 sinh ra | https://docs.google.com/spreadsheets/d/1SUjjrvUrzskgsQ4_vJF9askXGYhttDOh/edit?usp=drivesdk&rtpof=true&sd=true |
| 04 | `files/BaoCaoTongHopCTHTPL_20260807_1357.docx` | Tệp Word do chính lượt bấm 13:57:08 sinh ra | https://docs.google.com/document/d/14sOcHh5IytqiSChEwqtvY-InH0kKsw-a/edit?usp=drivesdk&rtpof=true&sd=true |

## 12. Năm câu hỏi cổng verdict (flow 04)

1. **Đã bấm bằng giao diện thật chưa?** Rồi — tick 2 dòng, bấm [Xuất Excel] rồi [Xuất Word] trên màn.
   Không gọi đường dẫn xuất tệp thay cho việc bấm nút.
2. **Có đủ hai đường đo độc lập không?** Có: **đường 1** = mở nội dung tệp bằng `openpyxl` / `python-docx`;
   **đường 2** = đối chiếu 13 chỉ tiêu với số liệu bản tổng hợp đã lưu ở 343 + đối chiếu mốc giờ bấm với
   đoạn thời gian trong tên tệp + đối chiếu tệp bản cũ 13:32 với tệp bản mới 13:56 (trùng khít). Không mâu thuẫn.
3. **Có Pass bằng quan sát tĩnh / bằng ảnh không?** Không — **mọi** kết luận đọc từ nội dung tệp bằng thư
   viện; ảnh chỉ để minh hoạ tiền đề và thao tác.
4. **Có hạ DIFF thành MATCH để ghi Test done không?** Không — C6 và C7 giữ DIFF, phiếu chốt `BA confirm`.
   Đáng nói: tên tệp thực tế **đúng SRS** và **lệch phiếu**, vẫn **không** chấm (luật khóa 5).
5. **Có khai đủ dữ liệu đã đổi không?** Có — §10: phiếu này không đổi gì.
