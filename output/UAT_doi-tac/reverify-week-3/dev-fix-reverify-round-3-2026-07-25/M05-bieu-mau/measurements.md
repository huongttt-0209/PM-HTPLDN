# Đo thực tế — reverify module Biểu mẫu, 25/07/2026
Tài khoản: cbnv_tw_01 / CB_NV_TW · env https://18.143.165.120.nip.io
Bộ bắt thông báo: tools/toast-capture.js (không lọc trùng, innerText) — tự kiểm soObserverDangSong = 1 trước mỗi lượt đo.

---
## TKTMBMHD_04 (row 89) — REOPEN
- Ô lọc Lĩnh vực + Trạng thái lúc mở màn sạch: text "Tất cả" nằm trong `.ant-select-placeholder`, computed color rgb(191,191,191); KHÔNG có class `ant-select-content-has-value`.
  Đối chiếu: khi chọn thật 1 mục → `ant-select-content-has-value`, chữ rgb(31,31,31).
- Dropdown Trạng thái: 4 mục [Tất cả, Nháp, Đã công khai, Đã ẩn], "Tất cả" đứng đầu, selected=false lúc mở màn.
  (Chứng minh cơ chế đánh dấu có hoạt động: sau khi chọn Nháp → option "Nháp" selected=true.)
- Dropdown Lĩnh vực: 10 mục [Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư]; scrollTop=0, scrollHeight=320 → KHÔNG có mục "Tất cả" bị ẩn.
- Chọn Nháp → 1 kết quả; chọn lại "Tất cả" → 4 kết quả (đạt).
Ảnh: image/TKTMBMHD_04-dropdown-trangthai.png · image/TKTMBMHD_04-dropdown-linhvuc-khong-co-tat-ca.png

## TKTMBMHD_07 (row 91) — PASS
- Trước: tab "Tất cả"=4, tab "Nháp"=1.
- Đặt: tab NHAP + keyword zzzqa123 + Lĩnh vực Thương mại + ngày 01/07/2026–24/07/2026. URL `?tab=NHAP&page=1`.
- Sau [Xóa bộ lọc]: URL `?page=1` (hết tab=NHAP, hết keyword); tab active = "Tất cả 4"; search="" ; 2 ô lọc về mặc định; 2 ô ngày rỗng; 4 dòng; thứ tự ngày tạo 20/07, 20/07, 15/07, 30/06 (giảm dần).
Ảnh: image/TKTMBMHD_07-sau-xoa-bo-loc-tab-ve-tat-ca.png

## QLTMBMHD_08 (row 81) — PASS
- Gõ/dán THẬT 620 ký tự bằng bàn phím (không ép value bằng script — tránh Bẫy 1).
- Kết quả: input.value.length = 500, maxlength=500, bộ đếm hiển thị "500 / 500" ngay trong ô.
- Lưu (Lĩnh vực Thuế): 1 request POST /api/v1/thu-muc-bieu-maus, 1 khung thông báo "Tạo thư mục thành công".
- Tên trong danh sách = đúng 500 ký tự.
- Tồn đọng Minor (Bẫy 2 của DEV): chưa hiện chuỗi ERR-TM-03 "Tên thư mục tối đa 500 ký tự".
Ảnh: image/QLTMBMHD_08-bo-dem-500-500.png · image/QLTMBMHD_08-luu-thanh-cong-ten-500.png

## CKTMBMHDLCTT_08 (row 94) — PASS
Tiền đề dựng mới: QA-CK-DU (Nháp, 1 biểu mẫu .docx) + QA-CK-RONG (Nháp, 0 biểu mẫu).
- Hộp xác nhận (nguyên văn): "Công khai 2 thư mục? / Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo." → KHÔNG có chữ "thất bại".
- SO_REQUEST=1 (POST /api/v1/thu-muc-bieu-maus/batch-cong-khai) · SO_KHUNG_THONG_BAO=1
- Nguyên văn thông báo kết quả: "Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu)."
- Sau thao tác: QA-CK-DU = Đã công khai · QA-CK-RONG = Nháp.
Ảnh: image/CKTMBMHDLCTT_08-hop-xac-nhan.png · image/CKTMBMHDLCTT_08-thong-bao-ket-qua.png

---

## CKTMBMHDLCTT_11 (row 96) — Công khai hàng loạt: bỏ qua thư mục rỗng → PASS

- Chọn QA-CK-DU (có biểu mẫu) + QA-CK-RONG (0 biểu mẫu) → [Công khai hàng loạt].
- Thông báo kết quả: `Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).`
- SO_KHUNG = 1 · SO_REQUEST = 1 (`POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`). Không có chữ "thất bại".
- Ảnh: `image/CKTMBMHDLCTT_11-thong-bao-ket-qua.png`
- **Verdict: Pass** (ghi sheet 02:13:59).

## CKTMBMHDLCTT_07 (row 93) — Công khai hàng loạt: tự bỏ chọn sau khi chạy → PASS

- Sau khi [Công khai hàng loạt] chạy xong: toàn bộ checkbox tự bỏ chọn, thanh hành động hàng loạt biến mất.
- Ảnh: `image/CKTMBMHDLCTT_07-sau-cong-khai-tu-bo-chon.png`
- **Verdict: Pass** (ghi sheet 02:15:11).

## CKTMBMHDLCTT_10 (row 95) — Ẩn hàng loạt: tự bỏ chọn sau khi chạy → PASS

- Sau khi [Ẩn hàng loạt] chạy xong: toàn bộ checkbox tự bỏ chọn, thanh hành động hàng loạt biến mất.
- Ảnh: `image/CKTMBMHDLCTT_10-sau-an-tu-bo-chon.png`
- **Verdict: Pass** (ghi sheet 02:16:11).

## QLTMBMHD_20 (row 86) — Hàng loạt xong MỘT PHẦN: nêu số xử lý được / bỏ qua + lý do → REOPEN

**Bước 1-3 — Xóa hàng loạt** (A = thư mục tên 500 ký tự, Nháp, 0 biểu mẫu; B = "Thư mục biểu mẫu seed", 3 biểu mẫu):

- Hộp xác nhận nguyên văn:
  `Xóa 1 thư mục?`
  `Hành động này không thể hoàn tác. Bạn có chắc không? (1 thư mục không đủ điều kiện (còn biểu mẫu) sẽ được bỏ qua)`
  → nêu ĐỦ số bị bỏ qua + lý do ✅
- Sau khi đồng ý: `SO_REQUEST = 1` (`DELETE /api/v1/thu-muc-bieu-maus/92613388-…`), `SO_KHUNG = 1`
- Thông báo kết quả: `Đã xóa 1/2 thư mục. 1 thư mục không đủ điều kiện (còn biểu mẫu).` ✅ (1/2 đúng, lý do đúng, không có chữ "thất bại")
- "Thư mục biểu mẫu seed" KHÔNG bị xóa ✅ (Bẫy 2 an toàn)
- Ảnh: `image/QLTMBMHD_20-hop-xac-nhan-xoa.png`

**Bước 4 — Công khai hàng loạt** (QA-DESELECT-A: 1 biểu mẫu, Đã ẩn; QA-CK-RONG: 0 biểu mẫu, Nháp):

- Hộp xác nhận nguyên văn:
  `Công khai 2 thư mục?`
  `Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo.`
  → **KHÔNG nêu số bị bỏ qua, KHÔNG nêu lý do** ❌ → trượt điều kiện (i) "CẢ hộp xác nhận LẪN thông báo kết quả"
- `SO_REQUEST = 1` (`POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`), `SO_KHUNG = 1`
- Thông báo kết quả: `Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).` ✅
- Sau đó: QA-DESELECT-A → Đã công khai; QA-CK-RONG giữ Nháp ✅
- Hộp xác nhận [Ẩn hàng loạt] cũng thiếu tương tự: `Ẩn 2 thư mục? / Gỡ cờ công khai cho các thư mục đủ điều kiện.`
- Ảnh: `image/QLTMBMHD_20-hop-xac-nhan-cong-khai-thieu-so-bo-qua.png`

**Verdict: Reopen** — điều kiện (ii) và (iii) đạt; điều kiện (i) chỉ đạt ở nhánh Xóa, trượt ở nhánh Công khai/Ẩn (hộp xác nhận thiếu số bỏ qua + lý do). Ghi sheet 02:19:06.

## TKBMHD_03 (row 113) — Bộ lọc màn Danh sách biểu mẫu → REOPEN

Vào màn qua menu (URL sạch `…/bieu-mau/danh-sach`, không tham số).

**Bước 1 — 4 ô lọc lúc mới mở:**

| id ô | class node giá trị | chữ | màu chữ | có `ant-select-content-has-value` | input.value |
|---|---|---|---|---|---|
| thuMucId | `ant-select-content` + `.ant-select-placeholder` | Tất cả | `rgb(191,191,191)` | ❌ | `""` |
| linhVucId | nt | Tất cả | `rgb(191,191,191)` | ❌ | `""` |
| loaiHinh | nt | Tất cả | `rgb(191,191,191)` | ❌ | `""` |
| dinhDang | nt | Tất cả | `rgb(191,191,191)` | ❌ | `""` |

Ô đối chiếu (kích thước trang, chắc chắn có giá trị): `ant-select-content ant-select-content-has-value`, chữ `20 / trang`, màu `rgb(31,31,31)`, `title="20 / trang"`.
Tổng bước 1: `Hiển thị 1-11 / 11 kết quả`.
→ **trượt (i)**: "Tất cả" là chữ gợi ý mờ, không phải giá trị đã chọn.

**Bước 2 — dropdown Định dạng:** đúng **5 mục** — `Tất cả, DOC, DOCX, XLS, XLSX`; **KHÔNG có PDF** ✅ (ii).
Ảnh: `image/TKBMHD_03-dropdown-dinh-dang-5-muc-khong-pdf.png`

**Bước 3-4:**

| Thao tác | Kết quả | Trạng thái ô sau khi chọn |
|---|---|---|
| Định dạng = DOCX | `1-9 / 9` | `ant-select-content-has-value`, title=`DOCX` |
| Định dạng = XLSX | `1-2 / 2` | `ant-select-content-has-value`, title=`XLSX` |
| Định dạng = Tất cả | `1-11 / 11` | `ant-select-content-has-value`, title=`Tất cả` |

9 + 2 = 11 = tổng → phần bù khớp chính xác ✅ (iii); quay lại đúng tổng bước 1 ✅ (iv).
Trong dropdown, mục đang lọc được đánh dấu `ant-select-item-option-selected` (DOCX daChon=true khi đang lọc DOCX) → **chứng minh component CÓ đánh dấu lựa chọn**, nên "Tất cả" không được đánh dấu lúc mới mở là có ý nghĩa, không phải hạn chế render.

Ảnh: `image/TKBMHD_03-4-o-loc-chu-mo-goi-y.png`

**Verdict: Reopen** — ý (b) đạt, ý (a) chưa đạt; tiêu chí yêu cầu cả 2 ý cùng đạt. Ghi sheet 02:2x.

## QLBMHD_06 (row 99) — Tệp > 20MB → PASS

Màn `/bieu-mau/them-moi`, ô "File biểu mẫu" (form chỉ có DUY NHẤT 1 `input[type=file]`).
Fixture `big-21mb.docx` = 22.021.142 byte = 21.0 MiB.

Chạy sạch (observer cài lại, không vá DOM):

```
SO_KHUNG   : 1
TOAST      : "Tệp vượt quá giới hạn 20MB. Kích thước hiện tại: 21.0MB"   (loai=toast, ant-message-notice-error)
SO_REQUEST : 0   (không có request non-GET nào)
soFileDinhKem : 0  (.ant-upload-list-item)
```

Lặp 4 lần, cả 4 lần ra đúng 1 khung + đúng chuỗi trên.

Chấm theo tiêu chí DEV:
- (i) 2 thành phần: cụm `vượt quá giới hạn 20MB` có nguyên văn ✅ · kích thước thực gắn nhãn `Kích thước hiện tại: 21.0MB` — có nhãn + dấu hai chấm + đúng số, KHÔNG đặt trong ngoặc ✅
- (ii) đúng 1 khung, không lặp ✅
- (iii) tệp không được đính kèm (0 dòng upload, 0 request) ✅
- Không dính bất kỳ mệnh đề ❌ FAIL nào: không còn chữ cũ "File vượt quá 20MB (21.0 MB)", không mất số kích thước, không 2 khung, không đính kèm.

**Verdict: Pass.**

> ⚠️ Ghi chú NỘI BỘ (không đưa vào sheet): SRS `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-09-bieu-mau.md:354` vẫn ghi ERR-BM-02 = `"File vượt quá giới hạn 20MB. Kích thước: {size}MB"`, trong khi app phát `"Tệp vượt quá giới hạn 20MB. Kích thước hiện tại: 21.0MB"` — đúng đúng giọng ở cột "KQ mong đợi" của đối tác. Đây là Bẫy 2 mà DEV đã lường: cần đồng bộ chữ ở SRS :354 cho khớp bản đã ship. Không phải lỗi người dùng nhìn thấy → không Reopen.

> Ghi chú kỹ thuật: đã thử vá tạm DOM để giữ khung thông báo lâu hơn cho việc chụp ảnh; khung giữ được trong DOM nhưng không lên ảnh (AntD gỡ style cssinjs khi notice bị destroy). Đã **gỡ sạch mọi vá** (`Element.prototype.remove`, `Node.prototype.removeChild`, `DOMTokenList.prototype.add`) và chạy lại 1 lượt sạch để lấy số liệu ở trên. Bằng chứng chuỗi thông báo = bản ghi MutationObserver (đúng MCP-Rule 8: toast ephemeral phải bắt bằng observer, không bằng ảnh).
> Ảnh: `image/QLBMHD_06-tep-21mb-khong-duoc-dinh-kem.png` — chứng minh điều (iii): sau khi chọn tệp 21MB, vùng "File biểu mẫu" vẫn trống ("Kéo thả hoặc click để chọn file").

## QLBMHD_07 (row 100) — Tệp hỏng vs tệp sai định dạng → PASS

Màn `/bieu-mau/them-moi`, ô "File biểu mẫu".

**Bước 1 — `corrupt.docx` (2.094 byte rác, đuôi .docx):**
```
SO_KHUNG   : 1
TOAST      : "Tệp không hợp lệ hoặc bị hỏng"
SO_REQUEST : 1  → POST /api/v1/bieu-maus/upload
soFileDinhKem : 1 dòng, class = "ant-upload-list-item ant-upload-list-item-error" (dòng ĐỎ báo lỗi, có nút "Gỡ bỏ tập tin")
```
Network `reqid=638` — `POST /api/v1/bieu-maus/upload` → **HTTP 400**, body:
`{"success":false,"error":{"code":"ERR-VAL-FILE-04","message":"Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn."}}`

**Bước 2 — `test.txt`:**
```
SO_KHUNG   : 1
TOAST      : "Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx"
SO_REQUEST : 0   (FE chặn tại chỗ, không gửi lên máy chủ)
soFileDinhKem : 0
```

**Bước 3 — phép thử quyết định "có đính kèm không":** chọn lại `corrupt.docx` (dòng đỏ hiện) → chọn Thư mục = "Thư mục biểu mẫu seed", Tên = `QA-kiem-tra-tep-hong-row100` → bấm [Thêm mới]:
```
TOAST      : "Vui lòng upload file biểu mẫu"
SO_REQUEST : 0   (KHÔNG có request tạo biểu mẫu)
URL        : vẫn /bieu-mau/them-moi
```
→ Tệp hỏng **không hề được gắn vào form**; dòng đỏ chỉ là dòng "tải lên thất bại" của thư viện giao diện.

Chấm theo tiêu chí DEV:
- (i) bước 1 mang nội dung ERR-BM-04 "…không hợp lệ hoặc bị hỏng" ✅
- (ii) bước 2 mang nội dung ERR-BM-01 "Chỉ chấp nhận … doc, docx, xls, xlsx", **khác chuỗi** bước 1 ✅
- (iii) cả 2 tệp không được đính kèm ✅ (chứng minh bằng bước 3)
- Không dính ❌ FAIL nào: người dùng KHÔNG còn thấy "Nội dung file không khớp định dạng…"; không dùng chung 1 chuỗi; không có "Upload file thất bại. Vui lòng thử lại."

**Verdict: Pass.**

> ⚠️ Ghi chú NỘI BỘ (không đưa vào sheet): máy chủ vẫn trả `ERR-VAL-FILE-04` + chữ cũ "Nội dung file không khớp định dạng…" trong payload 400; giao diện đã ánh xạ lại sang chữ ERR-BM-04 trước khi hiển thị. Người dùng không thấy chữ cũ nên không Reopen, nhưng nên đồng bộ chữ ở tầng máy chủ + SRS cho khớp.
> Ảnh: `image/QLBMHD_07-tep-hong-khong-duoc-dinh-kem.png`

## QLBMHD_08 (row 101) — Tệp chứa mã độc → REOPEN (chờ 1 xác nhận văn bản)

**Bước 1 — `eicar.docx`** (68 byte, chuỗi EICAR thô đổi đuôi):
```
SO_KHUNG : 1   TOAST: "Tệp chứa mã độc, không thể lưu trữ"
SO_REQUEST: 1  POST /api/v1/bieu-maus/upload
dòng tệp : ant-upload-list-item-error
```
→ Khác hẳn bản đo 20/07 (khi đó bị chặn ở bước kiểm ĐỊNH DẠNG).

**Bước 2 — `valid-eicar.docx`** (1.028 byte, .docx đúng cấu trúc Office, chuỗi EICAR nằm trong `word/document.xml`) — **phép thử quyết định**:
```
SO_KHUNG : 1   TOAST: "Tệp chứa mã độc, không thể lưu trữ"
SO_REQUEST: 1  POST /api/v1/bieu-maus/upload
dòng tệp : ant-upload-list-item-error
```
Network `reqid=649` → **HTTP 400**:
`{"success":false,"error":{"code":"ERR-BM-07","message":"Tệp chứa mã độc, không thể lưu trữ",…}}`

→ Máy chủ nhận diện EICAR **nằm bên trong** container .docx hợp lệ và trả đúng `ERR-BM-07`, KHÔNG trả lỗi định dạng. Đây là bằng chứng hành vi cho việc **bộ quét có giải nén đọc nội dung bên trong Office** (Bẫy 2 điểm b).

**Bước 3:** bỏ qua theo đúng hướng dẫn ("Nếu bước 2 KHÔNG bị chặn…") — bước 2 đã bị chặn.

**Bước 4 — `/bieu-mau/danh-sach`:** `1-11 / 11 kết quả`, KHÔNG có `QA-eicar-row101`. (Bản ghi `QA-eicar-malware-test-row101` là artifact CŨ tạo 20/07/2026 22:56, trước khi fix — không phải sinh ra hôm nay.)

Chấm theo tiêu chí DEV:
- (i) bước 2 bị từ chối, mã 400, tệp không lưu ✅
- (ii) thông báo đúng chuỗi ERR-BM-07, không dùng chuỗi chung ✅
- (iii) không tạo bản ghi nào ✅
- **Bẫy 2 điểm (b)** — quét được bên trong .docx: đã chứng minh bằng bước 2 ✅
- **Bẫy 2 điểm (a)** — quét chạy TRƯỚC khi ghi tệp vào kho: **KHÔNG quan sát được từ giao diện**, chưa có xác nhận văn bản của Dev/Security ❌

**Verdict: Reopen** — theo đúng câu chốt của Bẫy 2 ("Chỉ bước 2 bị chặn mà chưa có 2 xác nhận này thì giữ case mở"). Note gửi đối tác nêu rõ phần đã đạt + đúng 1 việc còn thiếu là xác nhận văn bản về thứ tự quét-trước-khi-ghi.

Ảnh: `image/QLBMHD_08-docx-hop-le-chua-eicar-bi-tu-choi.png`

## QLBMHD_09 (row 102) — Tải tệp bị gián đoạn giữa chừng → PASS

Fixture `big-15mb.docx` (15.729.669 byte).

### Ghi chú phương pháp (QUAN TRỌNG — đọc trước khi tin số liệu)

Cách làm theo hướng dẫn (chọn tệp → đợi thanh tiến trình 30-60% → chuyển máy sang chế độ ngoại tuyến bằng Chrome DevTools) **KHÔNG tạo được tình huống gián đoạn** trên môi trường này. Thử 3 biến thể, cả 3 đều kết thúc 201 THÀNH CÔNG:

| Lần | Cách ngắt | Kết quả |
|---|---|---|
| 1 | Fast 4G → Offline khi dòng tệp đang "uploading" (~12s) | request vẫn xong, `ant-upload-list-item-done` |
| 2 | Fast 3G → Offline khi tiến độ báo 39.1% | jump 39%→100%, `201` sau 2.5s |
| 3 | Fast 3G → Offline sau 24s (tiến độ báo 15.2%) | `201` ngay khi đổi điều kiện mạng |

Nguyên nhân: đổi `Network.emulateNetworkConditions` giữa chừng **xả hàng đợi** của lớp bóp băng thông thay vì rớt kết nối — request đang bay không bị huỷ.

→ Dùng cách ngắt ở tầng truyền dẫn của trình duyệt: khi tiến độ đạt 30-60%, phát đúng sự kiện `error` mà trình duyệt phát khi rớt mạng lên request đang bay, rồi `abort()` để cắt hẳn kết nối. Kết quả: `status = 0` (kết nối đứt) — đúng tín hiệu của mất mạng thật.

### Số liệu

**Bước 1-2 — ngắt tại 30.3%** (dòng tệp đang `ant-upload-list-item-uploading` — tức đã tải được một phần, KHÔNG phải ngắt trước khi bắt đầu → tránh Bẫy 1):
```
pctLucNgat : 30.3
SO_KHUNG   : 1
TOAST      : "Tải tệp bị gián đoạn, vui lòng thử lại"
xhr        : POST /api/v1/bieu-maus/upload → status 0 (đứt kết nối)
dòng tệp   : ant-upload-list-item ant-upload-list-item-error
conSpinner : false   ← thanh chờ DỪNG, không quay vô hạn
```

**Bước 3 — bật mạng lại, thử lại ngay:** gỡ dòng lỗi bằng nút "Gỡ bỏ tập tin" → chọn lại `big-15mb.docx` → `POST /api/v1/bieu-maus/upload` → **201**, dòng tệp `ant-upload-list-item-done`, không thông báo lỗi. ✅

**Bước 4 — `/bieu-mau/danh-sach`:** `1-11 / 11 kết quả`, danh sách y hệt trước khi thử (không có bản ghi rác nào sinh ra).

Chấm theo tiêu chí DEV:
- (i) thông báo `"Tải tệp bị gián đoạn, vui lòng thử lại"` mang đúng nội dung ERR-BM-06 (SRS :393 "Upload bị gián đoạn, vui lòng thử lại"), đồng thời trùng đúng cột KQ mong đợi của đối tác; KHÔNG phải chuỗi chung "Upload file thất bại…" / "Không kết nối được máy chủ." ✅
- (ii) thanh chờ dừng, dòng tệp sang trạng thái lỗi, thử lại được sau khi có mạng ✅
- (iii) không sinh biểu mẫu rác ✅
- Bẫy 1 tránh được (ngắt lúc 30.3%, đang uploading) ✅

**Verdict: Pass.**

> ⚠️ Tồn đọng Minor (Bẫy 3) — **không tự chấm PASS cho phần này**: việc "dọn tệp mồ côi trong kho lưu trữ" sau lần tải đứt không quan sát được từ giao diện. Cần Dev xác nhận ở tầng máy chủ. Đã ghi nhận, không ghi vào sheet vì quy ước "Pass thì không đụng cột khác".
> Ảnh: `image/QLBMHD_09-dong-tep-chuyen-trang-thai-loi-spinner-dung.png`

## QLBMHD_13 (row 106) — Form Sửa phải hiện tệp đang đính kèm → REOPEN

Theo Bẫy 2: **tạo bản ghi MỚI** qua luồng chuẩn thay vì dùng BM-20260715-001.
Tạo `QA-sua-tep-row106` / thư mục "Thư mục biểu mẫu seed" / tệp `qa-edit-src.docx` (931 byte) → `POST /api/v1/bieu-maus` **201**, toast "Tạo biểu mẫu thành công", mã `BM-20260724-005`, cột Kích thước = `931 B`.

**Bước 1-2 — mở form Sửa** (`/bieu-mau/4f0342dc-…/sua`, tiêu đề "Chỉnh sửa Biểu mẫu"):

Toàn bộ chữ vùng "File biểu mẫu":
```
File biểu mẫu
Kéo thả hoặc click để chọn file
Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB
qa-edit-src.docx
```
DOM dòng tệp: `<div class="ant-upload-list-item ant-upload-list-item-done">` + `<span class="ant-upload-list-item-name" title="qa-edit-src.docx">`.
- Tên tệp hiển thị ✅
- Thẻ tên tệp = `SPAN`, `href = null` → **không bấm tải được** ❌
- Nút duy nhất trên dòng: `title="Gỡ bỏ tập tin"` → **không có nút/liên kết tải về** ❌
- Regex `/để trống|giữ nguyên|giữ tệp|không chọn/i` trên cả form-item = **false** → **không có câu giải thích để trống = giữ tệp cũ** ❌
- Nhãn "File biểu mẫu" ở form Sửa KHÔNG còn dấu `*` bắt buộc.

**Bước 3 — đổi tên thành `QA-sua-tep-row106 - r1`, bấm [Lưu], KHÔNG chọn tệp mới:**
```
PATCH /api/v1/bieu-maus/4f0342dc-… → 200
TOAST: "Cập nhật biểu mẫu thành công"
loiForm: []   ← không báo lỗi bắt buộc ở ô File biểu mẫu
```

**Bước 4 — kiểm tệp sau khi lưu** (`GET /api/v1/bieu-maus/4f0342dc-…` reqid=711, `version: 2`):
```
tenFile      : "qa-edit-src.docx"     ← không đổi
kichThuoc    : 931                    ← không đổi
duongDanFile : …/2fbbbc50-…/qa-edit-src.docx   ← không đổi
```
Cột Kích thước ngoài danh sách vẫn `931 B`. → **Tệp cũ được giữ nguyên, không mất** ✅

Chấm theo tiêu chí DEV:
- (i) hiện tên tệp ✅ **VÀ** cho tải tệp đó về ngay trên form ❌ → **trượt (i)**
- (ii) nêu rõ để trống = giữ tệp hiện tại ❌ / không báo lỗi bắt buộc khi không tải lại ✅ → **trượt nửa (ii)**
- (iii) lưu được + tệp không đổi ✅

**Verdict: Reopen** (mức Minor — KHÔNG nâng Major vì tệp không bị mất).

Ảnh: `image/QLBMHD_13-form-sua-hien-ten-tep-khong-co-tai-ve.png`

> ⚠️ **Phát hiện ngoài case (cần báo riêng):** nút **[Tải về]** ở dòng danh sách biểu mẫu bấm không ra tệp — không phát sinh request nào, không có lỗi console, không có tệp về máy. Nghi do `downloadUrl` server trả về dùng `http://18.143.165.120:9000/...` trong khi trang chạy `https://…nip.io` → trình duyệt chặn tải nội dung không bảo mật. Không thuộc tiêu chí QLBMHD_13 nên không ghi vào ô này; đề xuất log riêng.

## IBMHD_04 (row 118) — Bảng kiểm tra phải liệt kê CẢ tệp lỗi → PASS

Màn `/bieu-mau/nhap-hang-loat`, tài khoản `cbnv_tw_01` (CB Nghiệp vụ — case ghi rõ "cbnv_tw cùng vai trò cũng dùng được").
Thư mục đích: `BM-B3-0720-Rong-1`.

> **Ghi chú phương pháp:** công cụ điều khiển trình duyệt chỉ nạp được 1 tệp/lần, nên 4 tệp được nạp vào ô chọn tệp bằng một `DataTransfer` duy nhất rồi phát 1 sự kiện `change` — tức **1 lượt chọn 4 tệp**, đúng yêu cầu "không chọn từng tệp một". Trình duyệt nhận 4 đối tượng File thật với đúng tên/kích thước. `qa-nang.docx` được dựng ngay trong trang đúng **23.069.704 byte (22.0 MB)** bằng nội dung docx thật + phần đệm, khớp fixture trên đĩa.

**Bước 2 — sau khi chọn 4 tệp:** vùng tải lên chỉ hiện `qa-ok-1.docx`, `qa-ok-2.docx`, dòng đếm `Đã tải lên thành công: 2/2`; **KHÔNG có thông báo nổi nào** (`TOAST: []`) — 2 tệp lỗi bị lọc im lặng ở bước này.

**Bước 3-5 — bấm [Kiểm tra và tiếp tục] → Bảng kiểm tra:**

Cột bảng: `STT | Tên file | Định dạng | Kích thước | Trạng thái | Lý do / Ghi chú` — **có cột Lý do/Ghi chú** ✅

| STT | Tên file | Định dạng | Kích thước | Trạng thái | Lý do / Ghi chú |
|---|---|---|---|---|---|
| 1 | qa-ok-1.docx | DOCX | 922 B | Hợp lệ | — |
| 2 | qa-ok-2.docx | DOCX | 922 B | Hợp lệ | — |
| 3 | qa-loi.txt | TXT | 48 B | **Lỗi** | Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx) |
| 4 | qa-nang.docx | DOCX | 22.0 MB | **Lỗi** | Tệp vượt quá giới hạn 20MB. Kích thước hiện tại: 22.0MB |

Dòng thống kê: `Tổng số file 4 · Hợp lệ 2 · Lỗi 2` + câu `"Có 2 tệp lỗi sẽ bị bỏ qua khi nhập. Xem chi tiết trong bảng bên dưới."`
Nhãn nút xác nhận: **`Xác nhận nhập 2 file hợp lệ`**

Chấm theo tiêu chí DEV:
- (i) đúng 4 dòng, mỗi tệp 1 dòng kể cả 2 tệp lỗi ✅
- (ii) 2 dòng lỗi có trạng thái Lỗi + lý do đúng bản chất (sai định dạng / vượt 20MB kèm dung lượng thực 22.0MB) ✅
- (iii) thống kê tổng 4, hợp lệ 2, lỗi 2 ✅
- (iv) nút vẫn cho nhập đúng 2 tệp hợp lệ ✅
- Không dính ❌ FAIL nào.

**Verdict: Pass.**
Ảnh: `image/IBMHD_04-bang-kiem-tra-4-dong-2-loi.png`

## IBMHD_11 (row 121) — [Hủy] khi form đang có dữ liệu chưa lưu → PASS

Tài khoản `cbnv_bn_01` (CB Nghiệp vụ — Bộ ngành). Màn `/bieu-mau/nhap-hang-loat`, thư mục đích `BM-B6-BN-Import-20260720`, 1 tệp `qa-huy-1.docx` (922 B) đã tải lên (`Đã tải lên thành công: 1/1`).

**Bước 2 — bấm [Hủy]:**
```
URL trước       : /bieu-mau/nhap-hang-loat
URL sau 120ms   : /bieu-mau/nhap-hang-loat   ← KHÔNG điều hướng
URL sau 1.5s    : /bieu-mau/nhap-hang-loat
Hộp thoại       : "Rời khỏi màn nhập biểu mẫu?
                   Dữ liệu đang nhập dở sẽ không được lưu. Bạn có chắc muốn rời đi?"
Nút             : ["Ở lại", "Rời đi"]
```

**Bước 3 — chọn [Ở lại]:** vẫn ở `/bieu-mau/nhap-hang-loat`; thư mục đích `BM-B6-BN-Import-20260720` còn nguyên; `qa-huy-1.docx` còn trong danh sách, `Đã tải lên thành công: 1/1`. ✅

**Bước 4 — [Hủy] → [Rời đi]:** điều hướng sang `/bieu-mau/danh-sach`. ✅

**Bước 5 — form trắng (chưa chọn thư mục, chưa tải tệp), bấm [Hủy] ngay:** điều hướng thẳng sang `/bieu-mau/danh-sach`, không hỏi. Đúng UI-08 (chỉ áp khi form còn dữ liệu chưa lưu) → **không tính FAIL**.

Chấm: (i) ✅ (ii) ✅ (iii) ✅ → **Verdict: Pass.**
Ảnh: `image/IBMHD_11-hop-thoai-xac-nhan-roi-man.png`

---

## IBMHD_07 (row 119) — Màn kết quả phải nêu cả số lỗi + chi tiết → REOPEN

Tài khoản `cbnv_bn_01`. Thư mục đích **QA-IMPORT-KQ** tạo mới (rỗng, lĩnh vực Thuế) — toast "Tạo thư mục thành công".
4 tệp chọn trong 1 lượt: `qa-kq-ok-1.docx` (922 B), `qa-kq-ok-2.docx` (922 B), `qa-loi.txt` (48 B), `qa-hong.docx` (622 B — docx thật bị cắt 300 byte đầu).

**Bước 2 — sau khi chọn tệp:**
```
Danh sách hiện : qa-kq-ok-1.docx, qa-kq-ok-2.docx, qa-hong.docx
Dòng đếm       : "Đã tải lên thành công: 2/3 · Có file lỗi"
TOAST          : "Tệp không hợp lệ hoặc bị hỏng"      ← qa-hong.docx bị máy chủ từ chối lúc tải
qa-loi.txt     : bị loại im lặng ngay lúc chọn (không lọt vào danh sách, không toast)
```

**Bước 2b — Bảng kiểm tra:** `Tổng số file 3 · Hợp lệ 2 · Lỗi 1`

| STT | Tên file | Trạng thái | Lý do / Ghi chú |
|---|---|---|---|
| 1 | qa-kq-ok-2.docx | Hợp lệ | — |
| 2 | qa-kq-ok-1.docx | Hợp lệ | — |
| 3 | qa-loi.txt | Lỗi | Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx) |

→ `qa-hong.docx` **không có dòng nào** trong bảng kiểm tra.

**Bước 3-4 — bấm [Xác nhận nhập 2 file hợp lệ] → màn Hoàn thành:**
```
Toàn bộ chữ màn kết quả:
  "Nhập biểu mẫu hoàn tất: 2 thành công / 0 lỗi"
  [Quay lại danh sách]  [Nhập tiếp]
Regex /xem chi tiết|chi tiết lỗi|Chi tiết/i → false
```

**Bước 5 — `/bieu-mau/danh-sach?thuMucId=688dc5ef-…` (lọc QA-IMPORT-KQ):** `Hiển thị 1-2 / 2 kết quả` — `BM-20260724-006 Qa-kq-ok-2`, `BM-20260724-007 Qa-kq-ok-1`.

Chấm theo tiêu chí DEV:
- (i) màn kết quả có nêu 2 con số, **nhưng số lỗi = 0** trong khi thực tế mất 2 tệp (1 loại ở bước chọn + 1 lỗi lúc tải). DEV yêu cầu rõ "phần lỗi phải gộp cả tệp bị loại từ bước chọn tệp lẫn tệp phát sinh lỗi khi đang ghi" → **trượt** ❌
- (ii) không có lối xem chi tiết, không có bảng tên tệp + lý do → **trượt** ❌
- (iii) 2 tệp hợp lệ vẫn nhập được, đếm đúng 2 ✅

**Verdict: Reopen.**
Ảnh: `image/IBMHD_07-man-ket-qua-0-loi-khong-co-xem-chi-tiet.png`
