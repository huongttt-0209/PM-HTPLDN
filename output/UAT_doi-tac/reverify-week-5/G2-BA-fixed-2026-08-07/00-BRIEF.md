# Lô G2 — Re-verify bug `Dopai = BA` + `Trạng thái dev fix ∈ {Fixed, Reopen}`

**Ngày:** 07/08/2026 · **Env:** `https://18.143.165.120.nip.io` (env NỘI BỘ, không phải env nghiệm thu đối tác)
**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** (gid `1714340219`)
**SRS chuẩn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Phiếu BA đã chốt:** `../ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md`
**Tài khoản:** bộ `_01` (`cbnv_tw_01`, `cbpd_tw_01`, … / `Test@1234`); vai trò QTHT dùng `admin` / `Secret@123`
(admin không có sibling `_01` — Rule 7: KHÔNG fallback).

---

## Vân tay bản dựng — đo đầu phiên 07/08/2026 ~16:2x giờ VN

| Hạng mục | Giá trị |
|---|---|
| Bó mã FE | `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 06:47:57 GMT` = **13:47 giờ VN 07/08** |
| `GET /` etag | `W/"6a757f9d-428"` |

🔴 **Nhãn phiên bản ở sidebar KHÔNG dùng làm định danh** (`../BAN-DUNG.md`: bản #4 bó mã mới hơn #3
nhưng nhãn lùi V1.0.10 → V1.0.9). Định danh thật = **bó mã + last-modified**.
🔴 **BẮT BUỘC lấy vân tay CẢ ĐẦU VÀ CUỐI phiên.** Hai đầu khác nhau ⇒ ghi rõ quan sát nào rơi
trước/sau mốc deploy. Tab mở lâu vẫn chạy JS cũ ⇒ **tải lại trang trước mỗi case**.

### Hệ quả đã biết trước khi đo

| Case | Bản dựng lượt verify gần nhất | So với bản hiện tại | Đo lại có thông tin mới không |
|---|---|---|---|
| 178 · 226 · 230 · 234 · 263 · 362 | `index-DIABnbIr.js` (V1.0.8, 06/08 14:13) | **CŨ hơn** | ✅ Có — đo thật |
| 189 · 222 | `index-BbPPdate.js` (07/08 13:47) | **TRÙNG KHÍT** | ⚠️ Không có bản mới kể từ lượt Reopen 15:26–16:09 hôm nay |

⇒ 189 · 222: chạy **lượt xác nhận rút gọn** (xuất 1 tệp, mở đọc, kiểm đúng bảng đang thiếu).
KHÔNG diễn lại toàn bộ sweep 2 vai trò đã làm lúc 15:26–16:09. Nếu tái hiện y hệt → giữ `Reopen`
và ghi rõ trong ô verify rằng **bó mã không đổi kể từ lượt trước**, tức chưa có bản sửa nào để đo.

---

## 8 dòng trong phạm vi

| Dòng | Mã TC | Trạng thái dev fix | Vấn đề gốc | Cụm |
|---|---|---|---|---|
| 178 | `VVDTN_04` | Fixed | "BC Vụ việc đã tiếp nhận" không có **biểu đồ tròn** theo lĩnh vực | A — chờ BA |
| 189 | `VVDHTHT_06` | Reopen | Tệp Excel "BC Vụ việc đã hoàn thành" **thiếu bảng theo kỳ** | B — nội dung tệp |
| 222 | `VVTDVQL_06` | Reopen | Tệp Excel "BC Vụ việc theo đơn vị QL" **thiếu cột cấp đơn vị** | B — nội dung tệp |
| 226 | `VVTLV_05` | Fixed | QTHT bấm Xuất Excel → 403 `Forbidden` | C — QTHT/quyền |
| 230 | `VVTLHDN_05` | Fixed | như trên | C |
| 234 | `VVTTGCT_05` | Fixed | như trên | C |
| 263 | `CPCTHTTTG_05` | Fixed | QTHT **xem được** báo cáo rồi mới bị chặn ở bước Xuất + chữ Anh "Forbidden" | C |
| 362 | `QLNDTVVCG_OOS_04` | Fixed | Nhật ký thao tác "CG từ chối" **không lưu lý do** | D — TVCS |

---

## Điều BA đã chốt 06/08 — đọc trước khi ra verdict

### Cụm C (189 · 222 · 226 · 230 · 234 — và liên quan 263)

`phan-hoi-ba-7-diem-can-chot-2026-08-06.md` **§5** chốt:

> **Vai trò Quản trị hệ thống KHÔNG phải tác nhân của chức năng báo cáo thống kê — không xuất tệp,
> và cũng không vào màn báo cáo. Máy chủ chặn xuất là ĐÚNG, không nới quyền. Giao diện sai ở chỗ
> vẫn mở màn và vẫn mời bấm nút xuất. Dev action: Có (giao diện) · Sửa đặc tả: Có · Sheet: giữ xử
> lý cho cả 5 phiếu (189 · 222 · 226 · 230 · 234).**

Căn cứ: `srs-fr-11-bao-cao.md:51` + `:62` (tác nhân chỉ CB Nghiệp vụ / CB Phê duyệt, 23/23 mục FR) ·
`srs-v3.5.md:684` quy ước M-05 *"Ẩn (không disable) nếu không có quyền"* · `srs-fr-11-bao-cao.md:86`
(tệp xuất là văn bản hành chính có quốc hiệu + họ tên cán bộ xuất).

**⇒ Hệ quả cho verdict cụm C:**
- QTHT bị chặn xuất = **ĐÚNG**, không còn là lỗi. **Không** chấm Fail vì lý do này nữa.
- Nhưng BA đòi thêm **Dev action (giao diện)**: phải **ẩn menu + chặn vào màn** báo cáo với QTHT,
  không được "mời rồi chặn".
- Phép đo quyết định của cụm C = **2 vế**:
  1. `admin` (QTHT): menu KHÔNG còn mục "Báo cáo thống kê" (ẩn hẳn, không phải làm mờ) **VÀ**
     gõ thẳng địa chỉ màn báo cáo thì không vào được. Phải đối chứng phiên còn hiệu lực bằng
     cách gõ một địa chỉ khác vào được bình thường (chống nhầm "rớt phiên").
  2. `cbnv_tw_01` (CB Nghiệp vụ TW — đúng tác nhân `:62`): xuất Excel ra tệp thật, **MỞ TỆP RA ĐỌC**,
     số khớp màn, và đổi bộ lọc → tệp đổi theo.
- ✅ **Test done** khi cả 2 vế đạt. ❌ **Reopen** nếu QTHT vẫn vào được màn báo cáo / vẫn thấy nút
  Xuất, hoặc CB Nghiệp vụ bị chặn theo, hoặc tệp thiếu thông tin so với màn.

> ⚠️ **Bẫy đã ghi sẵn từ lượt trước:** CB Nghiệp vụ xuất được **không** chứng minh đã fix — vai trò
> đó vốn tốt từ 06/08. Phép đo quyết định là chạy bằng chính `admin`.

**Riêng 189 · 222 KHÔNG đóng theo cụm C** — hai dòng này Reopen vì lỗi **nội dung tệp Excel**
(thiếu bảng theo kỳ / thiếu cột cấp đơn vị), độc lập hoàn toàn với chuyện quyền QTHT.

### Cụm D (362)

`phan-hoi-ba-7-diem-can-chot-2026-08-06.md` **§6** chốt: yêu cầu *"ghi nhật ký kèm lý do từ chối"*
là **ĐẠT — không phải lỗi**; phần **hiện lý do có kiểm soát** trên khối nhật ký là **cải tiến**
(Dev action: Có · Sửa đặc tả: Có). Ô `DEV phản hồi lần 1` ghi dev đã tách nhãn thao tác
"Từ chối" khỏi "Cập nhật" chung và hiển thị lý do có kiểm soát.

**⇒ Phép đo:** mở khối "Nhật ký thao tác" của một bản ghi TVCS vừa bị chuyên gia từ chối →
dòng nhật ký phải phân biệt được thao tác **Từ chối** (không còn nhãn "Cập nhật" chung) và
hiện được lý do. Đối chiếu đường thứ 2 bằng dữ liệu nhật ký của chính bản ghi đó.

### Cụm A (178)

BA **CHƯA trả lời**. Chỉ có phiếu hỏi `../ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md` §`VVDTN_04`
(2 hướng: giữ đặc tả `Bar + Trend` / đổi đặc tả thêm Donut). Không có phiếu chốt nào cho case này —
đã grep toàn thư mục `ba-confirm/`.

**⇒ Phép đo:** đo lại trên bản dựng hiện tại xem "BC Vụ việc đã tiếp nhận" đã có biểu đồ tròn chưa,
và bảng có đủ 2 chiều (theo kênh / theo lĩnh vực) chưa.
- Nếu **đã có** biểu đồ tròn → hết vướng, chấm `Test done`.
- Nếu **vẫn không có** → verdict `BA confirm` (kỳ vọng đối tác ngược `srs-fr-11-bao-cao.md:1065`
  vốn chốt UC125 = `Bar + Trend`; QA không tự bác đối tác).

---

## 🔴 PHẠM VI — CHỈ VERIFY BUG GỐC (chỉ đạo user 07/08, ĐÈ mọi mục phía trên)

**Bug gốc = đúng triệu chứng ghi ở ô `Kết quả thực tế` (cột L) so với ô `Kết quả mong đợi` (cột K)
của chính dòng đó.** Không mở rộng.

- Bug gốc **hết** → verdict `Test done`. Chuyển trạng thái, xong case.
- Bug gốc **còn** → `Reopen` (hoặc `BA confirm` nếu kỳ vọng đối tác ngược đặc tả).
- **Mọi phát hiện KHÁC bug gốc → BỎ QUA.** Không log, không đưa vào ô verify, không dùng để
  chặn Pass. Cụ thể **KHÔNG** dùng những thứ sau làm lý do Reopen:
  - Menu/màn báo cáo còn hiện với QTHT (đó là Dev action BA thêm vào, không phải bug gốc).
  - Chữ từ chối là tiếng Anh `Forbidden` / thiếu mã lỗi tiếng Việt.
  - Tệp xuất thiếu bảng theo kỳ · thiếu cột cấp đơn vị · in mã kỹ thuật `KHOANG`.
  - Nút Xuất bị khoá khi bấm [Xem báo cáo] lần 2.
  - Bất kỳ lỗi nào gặp lúc đo nhưng không phải triệu chứng ở cột L.

### Bảng bug gốc — chốt trước khi đo

| Dòng | Mã TC | **Bug gốc (cột L)** | Đạt khi |
|---|---|---|---|
| 178 | `VVDTN_04` | (a) không hiển thị **biểu đồ tròn** theo lĩnh vực · (b) bảng tổng hợp **thiếu cột** Theo kênh + Theo lĩnh vực | cả (a) và (b) đều hết |
| 189 | `VVDHTHT_06` | bấm Xuất excel → **"Không thể tạo file xuất. Vui lòng thử lại."** (lượt 31/7: `Forbidden`) | xuất ra được tệp thật, tải về máy, không còn 2 thông báo đó |
| 222 | `VVTDVQL_06` | như 189 | như 189 |
| 226 | `VVTLV_05` | như 189 | như 189 |
| 230 | `VVTLHDN_05` | như 189 | như 189 |
| 234 | `VVTTGCT_05` | như 189 | như 189 |
| 263 | `CPCTHTTTG_05` | như 189 | như 189 |
| 362 | `QLNDTVVCG_OOS_04` | nhật ký thao tác "CG từ chối" **không lưu lý do từ chối** | dòng nhật ký của thao tác từ chối mang được lý do (BA đã chốt yêu cầu này là ĐẠT — xác nhận lại trên bản dựng hiện tại) |

**Vai trò để đo bug gốc của 189·222·226·230·234·263:** BA đã chốt QTHT không phải tác nhân của
chức năng báo cáo (`srs-fr-11-bao-cao.md:51`, `:62`). Nên phép đo bug gốc chạy bằng **`cbnv_tw_01`**
(CB Nghiệp vụ TW — đúng tác nhân). Việc QTHT bị chặn **không** tính là bug gốc còn tồn tại.

**Vẫn giữ:** mở tệp `.xlsx` ra đọc để chứng minh tệp **thật** chứ không phải file rỗng/hỏng — đó là
một phần của "xuất được tệp". Nhưng **không** audit tệp thiếu bảng nào.

---

## Quy tắc chạy — BẮT BUỘC

1. **Tuần tự từng case.** Hoàn tất 1 case (đo → viết report → ghi sheet → đọc lại xác nhận) rồi mới
   sang case kế. Không gộp lô ghi sheet.
2. **Tool đo: Chrome DevTools MCP** (`mcp__chrome-devtools__*`). Không dùng gstack `$B`.
3. **Verify NỘI DUNG tệp xuất, không chỉ "tệp tạo được".** Mở `.xlsx` đọc bằng `openpyxl`
   (hoặc parse zip trong trang nếu MCP isolated không đổ file về `~/Downloads` — xem memory
   `reference-read-xlsx-content-in-browser-zip-parse`). `200 + binary` chỉ chứng minh CREATE ≠ CORRECT.
4. **Toast tự tắt ~3s và đổi chữ NGAY TRONG khung cũ** (không mọc khung mới) → công cụ đếm
   "khung mới" sẽ báo nhầm là im lặng. Theo dõi **nội dung** khung theo thời gian; muốn chụp ảnh thì
   **hẹn giờ bấm nút sau ~2500ms rồi mới gọi lệnh chụp**. App gửi lời gọi xuất qua **XHR**, không
   phải `fetch`. Observer **CẤM dedupe** và **CẤM `textContent`**.
5. **Quote SRS phải mở file đọc số dòng thật.** Cấm quote từ trí nhớ, cấm lấy số dòng từ
   `input/srs-update-2026-5-5/` (lệch +5..+14 dòng). Quote sai bản = bug invalid.
6. **Wording: mô tả YÊU CẦU, không kê ĐƠN implementation.** ✅ "theo SRS dòng N, khi X thì hệ thống
   phải từ chối và giữ nguyên trạng thái" · ❌ "phải gọi `POST /api/...` trả 200" / "phải có mã `ERR-...`".
7. **Lỗi gặp ngoài bug gốc → CHỈ ghi 1 dòng vào `99-quan-sat-ngoai-pham-vi.md`, KHÔNG đưa vào sheet,
   KHÔNG dùng để chặn Pass, KHÔNG điều tra thêm.** (Theo chỉ đạo user 07/08 — xem §PHẠM VI ở trên.)
8. **Ảnh lưu tại** `G2-BA-fixed-2026-08-07/image/`, **tệp xuất tại** `.../files/`.
   Tên: `<MaTC>-<so>-<mo-ta-khong-dau>.png`.

## Ghi sheet — ô được ghi và ô CẤM ghi

| Ô | Được ghi | Giá trị |
|---|---|---|
| `Trạng thái dev fix` (cột **R**) | ✅ | `Test done` (Pass) · `Reopen` (còn lỗi) · `BA confirm` (cần BA) |
| `Kết quả verify` (cột **T**) | ✅ | Diễn giải verdict |
| `Ảnh/video verify` (cột **U**) | ✅ | Link Drive xem được (theo tiền lệ các lô F/G trước) |
| `Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) · `DEV phản hồi lần 1` (S) | ❌ **CẤM** | chỉ đọc |

**Lệnh ghi** (dry-run trước, rồi bỏ `--dry-run`):

```bash
python3 output/UAT_doi-tac/tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s \
  --sheet-title bug --sheet-gid 1714340219 \
  --row <N> --id-column 'Mã TC' --id-value '<MA_TC>' \
  --expect 'Trạng thái dev fix=<GIÁ TRỊ CŨ>' --set 'Trạng thái dev fix=<MỚI>' \
  --expect-file 'Kết quả verify=<file cũ>' --set-file 'Kết quả verify=<file mới>' \
  --reason '<ngữ cảnh>' --dry-run
```

Script tự đọc lại sau khi ghi. Vẫn phải **đọc lại độc lập** bằng
`UAT_TAB=bug python3 tools/sheet_dump_bug_rows_2026-08-07.py --rows <N>` rồi mới sang case kế.

## Văn phong ô `Kết quả verify` (partner-facing)

- Tiếng Việt, cho người đọc nghiệp vụ. **KHÔNG** lộ chuyện test 2 môi trường theo kiểu nội bộ.
- Mở đầu bằng verdict: `✅ ĐÃ HẾT LỖI` / `🔁 CÒN LỖI — chuyển lại dev` / `⚠️ CẦN BA CHỐT`.
- Nêu rõ: đo cái gì · vai trò nào · thấy gì · vì sao kết luận vậy (kèm căn cứ đặc tả diễn giải
  bằng lời, không nhồi số dòng cho đối tác) · phần nào đã đạt thì ghi **"ĐÃ HẾT LỖI — đừng đụng lại"**.
- Case `Reopen` **BẮT BUỘC** có mục `CÁCH KIỂM LẠI SAU KHI SỬA` (điều kiện trước · các bước ·
  ✅ đạt khi · ❌ chưa đạt khi · ⚠️ bẫy) — ghi giống hệt từng chữ với file report.
- Ghi **giới hạn hiệu lực**: kết quả ứng với bản dựng đã đo, đề nghị xác nhận lại khi bản dựng
  này lên môi trường nghiệm thu.
