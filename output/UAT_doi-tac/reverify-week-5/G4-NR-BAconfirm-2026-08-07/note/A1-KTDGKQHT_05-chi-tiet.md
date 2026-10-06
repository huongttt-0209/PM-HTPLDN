# A1 — Dòng 10 · `KTDGKQHT_05` — Nhật ký đo lượt G4 (2026-08-07 chiều)

> Luật chung của lô ở [`00-BRIEF-CHUNG.md`](../00-BRIEF-CHUNG.md) — không lặp lại ở đây.

## 0. Kết luận

| Mục | Giá trị |
|---|---|
| **Verdict cột R** | **`Test done`** |
| Lỗi đối tác báo ban đầu (ô Q) | KHÔNG còn tái hiện |
| Dev khai ở ô S (ERR-KQ-09 mới + đổi câu ERR-KQ-03) | Đo thật → **đã làm, làm ĐÚNG** |
| Điểm còn treo | Đặc tả chưa quy định câu chữ của **báo cáo kết quả nạp**. BA 04/08 KHÔNG chạm tới điểm này ⇒ vẫn treo, nhưng **không quyết định đạt/không đạt** (hệ thống đã nêu đủ 2 con số phiếu yêu cầu) ⇒ theo bảng verdict của brief rơi vào hàng 1 → `Test done`, ghi rõ điểm treo trong ô T |

## 1. Tham số lượt đo

| Mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` (nội bộ) |
| **Bản dựng TRƯỚC lượt đo** | `index-BbPPdate.js` · `last-modified 2026-08-07 06:47:57 GMT` = **13:47:57 VN** — đo bằng curl lúc **19:29:11 VN** |
| **Bản dựng SAU lượt đo** | `index-BbPPdate.js` · cùng `last-modified` — đo bằng curl lúc **19:49:46 VN** ⇒ không có bản mới xen giữa |
| Bản dựng tab đang chạy | `evaluate_script` đọc `script[src]` = `…/assets/index-BbPPdate.js` (đã **tải lại trang** giữa lượt, không chạy JS cũ) |
| Nhãn phiên bản trên giao diện | `HTPLDN · V1.0.10` — khớp câu "Đã lên bản v1.0.10" của dev ở ô S |
| Bản dựng lượt đo CŨ (12:04–12:06) | `index-eWHwDgt2.js` (09:11 VN) ⇒ lượt này là đo lại thật trên bản mới |
| Tài khoản | `cbnv_tw_03` — Cán bộ Nghiệp vụ Trung ương (CB_NV_TW, BTP·TW). **Không phải fallback** — đúng tài khoản lượt cũ dùng |
| Khung giờ đo | 19:33 – 19:49 VN, 2026-08-07 |
| Bộ bắt thông báo | `output/UAT_doi-tac/tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` trước MỖI phép đo · cài lại sau mỗi lần điều hướng |

> **Sự cố quy trình (không phải lỗi phần mềm):** đầu phiên tôi đăng nhập song song `cbnv_tw_03` bằng API để lấy khoá phiên → phiên trình duyệt bị đẩy ra ("Phiên làm việc hết hạn"). Đây là hành vi 1-phiên/1-tài khoản do chính tôi gây ra, đã đăng nhập lại và bỏ hẳn phiên API. Không tính là phát hiện.

## 2. Tiền đề đã dựng

Ô T lượt cũ ghi: khóa `KH-QAW7-HOINGHI` sau lượt 12:04 **không còn buổi nào chưa điểm danh** (Buổi 4 đã bị lượt cũ ghi 3 bản ghi).

⇒ Lượt này **tạo thêm Buổi 5** trên chính khóa đó (Tab Lịch học → "Thêm buổi học"):

| Mục | Giá trị |
|---|---|
| Khóa học | `KH-QAW7-HOINGHI` — "QAW7 — Hội nghị đối thoại DN 2026", trạng thái **Đang diễn ra**, 4/100 học viên đã duyệt |
| ID khóa | `a7480002-0000-4000-8000-000000000002` |
| **Buổi 5 (mới, tạo 19:35)** | 11/05/2026 · 16:30:00–18:00:00 · "Buổi 5 - QA G4 KTDGKQHT_05 re-verify 07/08" · id `2b643da6-7a79-470a-8228-b941827594d1` |
| Buổi 4 (của lượt cũ) | 11/05/2026 · 14:00:00–16:00:00 · id `bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2` — dùng làm **tệp sai ngữ cảnh** để đo ERR-KQ-09 |
| 4 học viên của khóa | Nguyễn Văn A · QA R3 Mailto Ba · QA R3 Mailto Hai · QA R3 Mailto Mot |
| Học viên "khóa khác" dùng cho dòng lỗi | `f0dddddd-0000-4000-8000-000000000002` — Trần Thị B, thuộc khóa `KH-2026-001` |

Tạo Buổi 5: 1 request `POST …/lich-hocs` · 1 khung thông báo "Đã thêm buổi học" (không lặp).

**Tệp nạp** — lấy từ chính nút **"Tải mẫu điểm danh"** của hệ thống (bắt blob của nút tải, không tự dựng cấu trúc):
- `do/mau_buoi5.xlsx` — tệp mẫu gốc của Buổi 5 (8.189 byte).
- `do/nap_buoi5_3hople_2loi.xlsx` — mẫu Buổi 5 sau khi điền: **3 dòng hợp lệ + 2 dòng cố ý sai**.
- `do/mau_buoi4.xlsx` → `do/nap_sai_buoi_tepbuoi4.xlsx` — mẫu của **Buổi 4**, dùng để nạp nhầm vào Buổi 5 (đo ERR-KQ-09).

## 3. Từng ý chấm

### Ý 1 — Điều kiện bật nút "Tải mẫu điểm danh" + trạng thái rỗng — **ĐẠT**

- Chưa chọn buổi: cả 4 nút (Lưu điểm danh / Tải mẫu điểm danh / Import Excel / Xuất Excel) **disabled**, bảng hiện đúng câu "Vui lòng chọn buổi học để bắt đầu điểm danh".
- Bộ chọn buổi là **danh sách buổi** hiện `Ngày · Khung giờ · Nội dung` (không phải ô chọn ngày).
- Chọn Buổi 5 → 4 nút bật, bảng hiện đủ 4 học viên.
- Đối chiếu: `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-03-dao-tao.md:577` (điều kiện bật nút Tải mẫu điểm danh) · `:1919` (Tab 4 có nút "Tải mẫu điểm danh") · `:1920` (bộ chọn buổi Ngày·Khung giờ·Nội dung) · `:1921` (câu trạng thái rỗng).
- Ảnh: `KTDGKQHT_05-01-…`, `KTDGKQHT_05-02-…`.

### Ý 2 — Nội dung tệp mẫu tải về — **ĐẠT**

Đọc bằng openpyxl (`do/mau_buoi5.xlsx`):

| Kiểm | Kết quả đo |
|---|---|
| Bộ cột trang "Mẫu điểm danh" | `hoc_vien_id` · Họ tên · Email · Đơn vị · Trạng thái điểm danh · Ghi chú — **đúng thứ tự, đúng 6 cột** |
| `hoc_vien_id` điền sẵn | Có, đủ 4/4 học viên |
| `hoc_vien_id` khoá/ẩn | Cột A `hidden = True` |
| Cột cần cán bộ điền | "Trạng thái điểm danh" để trống |
| Định danh buổi học | Nằm ở trang phụ **`_HTPLDN_META` (veryHidden)**: `khoa_hoc_id = a7480002-…-0002`, `lich_hoc_id = 2b643da6-…` — **không phải cột từng dòng** |

Đối chiếu: `srs-fr-03-dao-tao.md:581` (bộ cột mẫu điểm danh, `hoc_vien_id` điền sẵn khoá/ẩn) · `:583` (`lich_hoc_id` nhúng ở vùng metadata, không phải cột từng dòng) · AC `:651`.

### Ý 3 — Bản xem trước trước khi ghi — **ĐẠT**

Nạp `nap_buoi5_3hople_2loi.xlsx` → 1 request `POST …/diem-danhs/import/preview`, **không ghi dữ liệu**:

```
Kết quả kiểm tra - chưa nhập dữ liệu
Tổng dòng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2
Tab "Hợp lệ (3)"  → dòng 2/3/4 kèm giá trị điểm danh + ghi chú
Tab "Lỗi/Bỏ qua (2)" → mỗi dòng có SỐ DÒNG + MÃ LỖI + LÝ DO RIÊNG
```

Đối chiếu `srs-fr-03-dao-tao.md:593` (bước 5 — dòng lỗi ghi rõ mã lỗi + số dòng). Ảnh `KTDGKQHT_05-03-…`, `KTDGKQHT_05-04-…`.

### Ý 4 — Câu chữ `ERR-KQ-03` mà BA yêu cầu đổi — **ĐẠT (dev khai đúng)**

- Đo được (dòng 6, học viên Trần Thị B thuộc khóa khác):
  `ERR-KQ-03: Không tìm thấy học viên ở dòng 6 (định danh không hợp lệ hoặc không thuộc khóa học này)`
- Đặc tả `srs-fr-03-dao-tao.md:637` (E3): `"Không tìm thấy học viên ở dòng {N} (định danh không hợp lệ hoặc không thuộc khóa học này)"` → **trùng khít**, có số dòng, có vế "không thuộc khóa học này".
- Đúng yêu cầu bản chất ở `:592` (ERR-KQ-03 = học viên phải TỒN TẠI **VÀ** THUỘC khóa đang thao tác) và AC `:654` (dòng đó báo ERR-KQ-03 và bị bỏ qua).
- Văn bản đầy đủ có sẵn ở thuộc tính `title` của ô (rê chuột xem hết) — cột bị cắt ngắn trên bảng là hành vi hiển thị bình thường, không mất thông tin.

### Ý 5 — `ERR-KQ-04` (giá trị điểm danh sai) — **ĐẠT**

- Đo được (dòng 5, giá trị "XYZ"): `ERR-KQ-04: Giá trị điểm danh không hợp lệ: XYZ`
- Đặc tả `:638`: `"Giá trị điểm danh không hợp lệ"` → khớp, phần `: XYZ` là thông tin thêm giúp cán bộ sửa, không mâu thuẫn.

### Ý 6 — `ERR-KQ-09` (tệp mẫu lệch buổi) — **ĐẠT (dev khai đúng, đây là mã lỗi MỚI của bản chốt 04/08)**

Kịch bản: đang chọn **Buổi 5** trên màn → nạp tệp mẫu tải về của **Buổi 4**.

- Máy chủ trả **422**, thân phản hồi:
  `{"code":"ERR-KQ-09","message":"Tệp mẫu không khớp buổi học / đề kiểm tra đang chọn. Vui lòng tải mẫu đúng và thử lại"}`
  (lưu tại `do/ERR-KQ-09-phanhoi-may-chu.txt`; yêu cầu gửi lên có `lichHocId` = Buổi 5 trong khi metadata tệp = Buổi 4)
- Bộ bắt thông báo: `SO_REQUEST = 1`, `SO_KHUNG_THONG_BAO = 1`, chữ trùng khít câu trên (không lặp thông báo).
- Đặc tả `srs-fr-03-dao-tao.md:643` (E9) và `:590` (bước 2 — đọc `lich_hoc_id` từ metadata, lệch → ERR-KQ-09); AC `:653`.
- **Không ghi bất kỳ dữ liệu nào**: đọc lại điểm danh Buổi 5 sau phép thử vẫn đúng 3 bản ghi cũ.
- Ảnh không bắt kịp thông báo (tự tắt ~3s, đã thử 4 nhịp bấm/chụp khác nhau) → theo hướng dẫn `toast-capture.js` dùng **phản hồi máy chủ** làm bằng chứng; ảnh `KTDGKQHT_05-08-…` chỉ ghi lại trạng thái đã chọn đúng tệp Buổi 4 trong ngữ cảnh Buổi 5.

### Ý 7 — Bước ghi dữ liệu + báo cáo kết quả nạp — **ĐẠT phần dữ liệu, còn treo phần câu chữ**

Bấm "Xác nhận import (3 dòng hợp lệ)" → 1 request `POST …/diem-danhs/import/confirm`:

```
Import hoàn tất
Đã nhập 3 · Bỏ qua 0 · Lỗi 2
+ bảng chi tiết 5 dòng (3 Hợp lệ có tên/giá trị, 2 Lỗi kèm lý do)
```

Không còn lỗi hệ thống như lượt đo trước. Kiểm chứng bằng **2 đường độc lập**:

1. Đọc lại dữ liệu điểm danh Buổi 5 từ máy chủ:
   - QA R3 Mailto Ba → `CO_MAT`
   - QA R3 Mailto Hai → `VANG_PHEP`
   - QA R3 Mailto Mot → `VANG_KHONG_PHEP`
   - Nguyễn Văn A (dòng ghi sai trạng thái) → **không có bản ghi trạng thái**
   - Trần Thị B (khóa khác) → **không xuất hiện**
   ⇒ đúng 3/3 dòng hợp lệ được ghi, 0/2 dòng lỗi lọt — khớp `:594` (chỉ merge dòng hợp lệ) + AC `:654`.
2. **Tải lại trang** (bản dựng xác nhận vẫn `index-BbPPdate.js`) → chọn lại Buổi 5: bảng hiện đúng 3 học viên có trạng thái + ghi chú, học viên dòng lỗi trống. Ảnh `KTDGKQHT_05-06-…`.

**Điểm treo (không chặn bàn giao):** phiếu (ô K) kỳ vọng câu `"Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ"`. Hệ thống hiện `Import hoàn tất` + `Đã nhập 3 / Bỏ qua 0 / Lỗi 2`.
- Đặc tả **không quy định câu chữ nào** cho báo cáo nạp: `:595` chỉ ghi "Trả về báo cáo import"; bảng xử lý lỗi `:635–:643` không khai thông báo thành công; SCR-III-02 Tab 4 (`:1919–:1923`) cũng không.
- **Bản sửa 04/08 mà BA chốt (`:14`) không chạm tới điểm này** — nội dung chốt chỉ gồm: giữ `hoc_vien_id` không thêm trường, cơ chế Tải mẫu → điền → tải lên, `lich_hoc_id` ở metadata, **bổ sung ERR-KQ-09**, **đổi câu ERR-KQ-03**.
- ⇒ Vẫn là điểm đặc tả bỏ ngỏ. Nhưng hệ thống **đã nêu đủ cả hai con số phiếu yêu cầu**, và theo nguyên tắc "mô tả yêu cầu, không áp cách làm", không có căn cứ chấm sai vì khác cách diễn đạt ⇒ **không quyết định đạt/không đạt** ⇒ verdict `Test done`, ghi rõ điểm treo trong ô T.

### Ý 8 — Việc đối tác báo ban đầu (ô Q) — **KHÔNG còn tái hiện**

"Màn hình danh sách không hiển thị mã học viên nhưng khi nhập file excel điểm danh hệ thống bắt buộc có mã học viên":
- Bảng Tab Điểm danh vẫn (đúng đặc tả `:1919`) chỉ hiện STT · Họ tên · Email · Số điện thoại · Đơn vị · Trạng thái · Ghi chú — **không có mã học viên**, và không cần có.
- Import **không còn đòi cán bộ tự nhập định danh**: tệp mẫu do hệ thống sinh đã điền sẵn định danh ở cột ẩn/khoá, cán bộ chỉ điền cột trạng thái.
⇒ Khe hở mà đối tác chỉ ra đã được bịt bằng đúng hướng nghiệp vụ BA chốt 04/08 (`:14`).

## 4. Bảng tổng hợp verdict từng ý

| # | Ý chấm | Verdict | Căn cứ |
|---|---|---|---|
| 1 | Điều kiện bật nút Tải mẫu + trạng thái rỗng + bộ chọn buổi | ✅ Đạt | `:577` `:1919` `:1920` `:1921` |
| 2 | Nội dung tệp mẫu (6 cột, định danh điền sẵn/ẩn, metadata buổi) | ✅ Đạt | `:581` `:583` AC `:651` |
| 3 | Bản xem trước có số dòng hợp lệ/lỗi + lý do từng dòng | ✅ Đạt | `:593` |
| 4 | Câu chữ ERR-KQ-03 (BA yêu cầu đổi) | ✅ Đạt — dev đã làm | `:637` `:592` AC `:654` |
| 5 | ERR-KQ-04 | ✅ Đạt | `:638` |
| 6 | ERR-KQ-09 (mã lỗi mới BA yêu cầu bổ sung) | ✅ Đạt — dev đã làm | `:643` `:590` AC `:653` |
| 7a | Ghi dữ liệu: chỉ 3 dòng hợp lệ, 0 dòng lỗi lọt | ✅ Đạt | `:594` AC `:654` |
| 7b | Câu chữ báo cáo kết quả nạp | ⚠️ Đặc tả bỏ ngỏ — không chặn | `:595` `:635–:643` |
| 8 | Lỗi đối tác báo ban đầu (mã học viên) | ✅ Hết | `:14` `:1919` |

**Tổng:** không có ý nào Reopen · các ý đo được đều Đạt · ý treo duy nhất là câu chữ đặc tả chưa quy định và không chặn bàn giao → **`Test done`**.

## 4b. Vòng R2 — chạy lại trên buổi trắng (Buổi 6)

> **Ghi chú về nguồn mục này:** người đo bị ngắt kết nối trước khi kịp viết mục này. Nội dung dưới đây do
> lead dựng lại bằng cách **mở đọc lại chính các ảnh và tệp vòng R2 để lại**, và chỉ ghi những gì đọc
> được trên ảnh — không suy diễn thao tác không có bằng chứng.

**Vì sao chạy lại:** vòng 1 nạp vào Buổi 5 là buổi vừa được tạo trong cùng phiên đo, và ý 7 (ghi dữ liệu)
được kiểm bằng đường đọc lại máy chủ. R2 lặp lại trọn luồng trên **một buổi trắng khác** để loại khả năng
kết quả vòng 1 phụ thuộc trạng thái riêng của Buổi 5.

**Tiền đề R2:** cùng khóa `KH-QAW7-HOINGHI`, cùng tài khoản `cbnv_tw_03` (ảnh hiện "CB Nghiệp vụ – Trung
ương #03"), cùng nhãn bản dựng **V1.0.10** trên thanh bên. Buổi mới:
`11/05/2026 · 18:30:00–20:00:00 · "Buoi 6 - QA G4 KTDGKQHT_05 do lai 07/08 toi"`.
Tệp: `do/mau_buoi6.xlsx` (mẫu tải từ hệ thống) → `do/nap_buoi6_3hople_2loi.xlsx` (3 hợp lệ + 2 cố ý sai)
và `do/nap_sai_buoi_tepbuoi5_vao_buoi6.xlsx` (mẫu Buổi 5 dùng để nạp nhầm vào Buổi 6).

| Ý | Vòng 1 (Buổi 5) | Vòng R2 (Buổi 6) | Kết luận |
|---|---|---|---|
| 1 — nút mờ khi chưa chọn buổi | 4 nút disabled | ảnh `-09-` : 4 nút mờ, chưa chọn buổi | **trùng khít** |
| 1 — chọn buổi thì 4 nút bật | bật | ảnh `-10-` : chọn Buổi 6 → 4 nút bật | **trùng khít** |
| 3 — bản xem trước | Tổng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2, "chưa nhập dữ liệu" | ảnh `-12-` : **Tổng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2**, cùng câu "Kết quả kiểm tra – chưa nhập dữ liệu" | **trùng khít** |
| 3 — lý do riêng từng dòng lỗi | dòng 5 `ERR-KQ-04`, dòng 6 `ERR-KQ-03` | ảnh `-13-` : dòng 5 `ERR-KQ-04: Giá trị điểm danh không hợp l…`, dòng 6 `ERR-KQ-03: Không tìm thấy học viên ở dòng 6…` | **trùng khít** |
| 7a — báo cáo sau khi nạp | "Import hoàn tất — Đã nhập 3 · Bỏ qua 0 · Lỗi 2" | ảnh `-14-` : **Import hoàn tất — Đã nhập 3 · Bỏ qua 0 · Lỗi 2** + bảng chi tiết đủ 5 dòng (3 Hợp lệ có tên/giá trị, 2 Lỗi kèm lý do) | **trùng khít** |
| 7a — chỉ dòng hợp lệ được ghi | 3/3 ghi, 0/2 dòng lỗi lọt | ảnh `-15-` (sau **tải lại trang**): Buổi 6 hiện `QA R3 Mailto Ba = Có mặt`, `QA R3 Mailto Hai = Vắng có phép`, ghi chú "QA G4 luot2 do…"; **`Nguyễn Văn A` — dòng ghi sai giá trị — không ô trạng thái nào được chọn, ghi chú trống** | **trùng khít** |
| 6 — tệp lệch buổi | 422 + `ERR-KQ-09`, có lưu phản hồi máy chủ | ảnh `-16-`/`-17-` chỉ bắt được **bước dựng phép thử** (hộp Import của Buổi 6 đã chọn `nap_sai_buoi_tepbuoi5_vao_buoi6.xlsx`, trước khi bấm "Kiểm tra tệp") | ⚠️ **R2 không để lại bằng chứng kết quả** — vế này vẫn dựa vào bằng chứng vòng 1 (`do/ERR-KQ-09-phanhoi-may-chu.txt`) |

**Bổ sung mới mà vòng 1 chưa có bằng chứng — vế "điểm kiểm tra" của BA chốt:**
ảnh `-18-` chụp tab **Kết quả** của cùng khóa: có nút **"Tải mẫu điểm kiểm tra"** đứng cạnh "Import Excel"
và "Xuất DOCX", kèm bộ chọn đề `QA-DEKT-0803`. BA chốt 04/08 yêu cầu cơ chế "Tải mẫu → điền → tải lên"
**áp cho cả điểm danh lẫn điểm kiểm tra** (2 nút Tải mẫu, Tab 4 và Tab 5); vòng 1 mới chứng minh được Tab
Điểm danh, ảnh này đóng nốt vế Tab Kết quả.

**Ảnh hưởng tới verdict:** R2 xác nhận lại vòng 1, **không đổi verdict ý nào và không đổi verdict tổng**.
Bảng §4 giữ nguyên. Riêng vế "điểm kiểm tra" của BA nay đã có bằng chứng trực tiếp thay vì chỉ suy từ
Tab Điểm danh.

## 5. Danh sách ảnh

| Tệp trong `image/` | Chứng minh điều gì |
|---|---|
| `KTDGKQHT_05-01-tab-diemdanh-chua-chon-buoi.png` | Chưa chọn buổi: 4 nút mờ + câu hướng dẫn "Vui lòng chọn buổi học để bắt đầu điểm danh" |
| `KTDGKQHT_05-02-chon-buoi5-nut-taimau-bat.png` | Chọn Buổi 5 → nút "Tải mẫu điểm danh"/"Import Excel" bật, bảng hiện 4 học viên chưa có trạng thái |
| `KTDGKQHT_05-03-xemtruoc-hople-3.png` | Bản xem trước "chưa nhập dữ liệu": Tổng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2 |
| `KTDGKQHT_05-04-xemtruoc-tab-loi-2dong.png` | Tab Lỗi: dòng 5 báo ERR-KQ-04, dòng 6 báo ERR-KQ-03 (hai lý do khác nhau, có số dòng) |
| `KTDGKQHT_05-05-ngay-sau-xacnhan-import.png` | Ngay sau khi xác nhận nạp: "Import hoàn tất — Đã nhập 3 · Bỏ qua 0 · Lỗi 2" + bảng chi tiết 5 dòng |
| `KTDGKQHT_05-06-bang-diemdanh-sau-nap-taitrang.png` | Sau khi **tải lại trang**: 3 học viên có đúng 3 trạng thái, học viên dòng lỗi vẫn trống |
| `KTDGKQHT_05-07-tep-sai-buoi-ERR-KQ-09.png` | Ngữ cảnh phép thử ERR-KQ-09 (đang ở Buổi 5, đã nạp tệp mẫu của buổi khác) |
| `KTDGKQHT_05-08-nap-tep-buoi-khac-vao-buoi5.png` | Tệp `nap_sai_buoi_tepbuoi4.xlsx` đã chọn trong hộp Import của Buổi 5, trước khi bấm kiểm tra |

Bằng chứng phi-ảnh: `do/ERR-KQ-09-phanhoi-may-chu.txt` (phản hồi 422 + mã ERR-KQ-09 + chữ thông báo bộ đo bắt được).

### Ảnh vòng R2 (Buổi 6)

| Tệp trong `image/` | Chứng minh điều gì |
|---|---|
| `KTDGKQHT_05-09-R2-chua-chon-buoi-4nut-mo.png` | Buổi trắng khác: chưa chọn buổi thì 4 nút vẫn mờ |
| `KTDGKQHT_05-10-R2-chon-buoi6-4nut-bat.png` | Chọn Buổi 6 → 4 nút bật, bảng hiện học viên chưa có trạng thái |
| `KTDGKQHT_05-11-R2-hop-import-da-chon-tep.png` | Hộp Import đã chọn `nap_buoi6_3hople_2loi.xlsx`, kèm dòng hướng dẫn "Chỉ dùng tệp từ nút Tải mẫu điểm danh" |
| `KTDGKQHT_05-12-R2-xemtruoc-tong5-hople3-loi2.png` | Bản xem trước "chưa nhập dữ liệu": Tổng 5 · Hợp lệ 3 · Bỏ qua 0 · Lỗi 2 (trùng vòng 1) |
| `KTDGKQHT_05-13-R2-xemtruoc-tab-loi-2dong-ly-do-rieng.png` | Tab Lỗi: dòng 5 `ERR-KQ-04`, dòng 6 `ERR-KQ-03` — hai lý do khác nhau, có số dòng |
| `KTDGKQHT_05-14-R2-ngay-sau-xacnhan-import.png` | "Import hoàn tất — Đã nhập 3 · Bỏ qua 0 · Lỗi 2" + bảng chi tiết đủ 5 dòng |
| `KTDGKQHT_05-15-R2-bang-diemdanh-buoi6-sau-nap-taitrang.png` | Sau **tải lại trang**: 3 dòng hợp lệ đã ghi đúng trạng thái; `Nguyễn Văn A` (dòng sai giá trị) **không** có trạng thái nào được chọn |
| `KTDGKQHT_05-16-R2-buoi6-da-chon-tep-cua-buoi5.png` | Dựng phép thử lệch buổi vòng R2: đang ở Buổi 6, đã chọn tệp mẫu của Buổi 5 |
| `KTDGKQHT_05-17-R2-nguc-canh-phep-thu-tep-lech-buoi.png` | Hộp Import Buổi 6 hiện tên tệp `nap_sai_buoi_tepbuoi5_vao_buoi6.xlsx`, **trước** khi bấm "Kiểm tra tệp" (chỉ là bước dựng, không phải kết quả) |
| `KTDGKQHT_05-18-R2-tab-ketqua-co-nut-tai-mau-diem-kiem-tra.png` | Tab **Kết quả** có nút **"Tải mẫu điểm kiểm tra"** → đóng vế "áp cho cả điểm kiểm tra" của bản chốt 04/08 |

## 6. Ngoài tiêu chí đang chấm — có gì bất thường không?

**Không phát hiện thêm lỗi.** Ba quan sát nhỏ, đều KHÔNG log:

1. Nhật ký trình duyệt chỉ có đúng 6 lần `422` — là 6 lần tôi cố ý nạp tệp sai buổi để đo ERR-KQ-09. Không có lỗi mã nguồn nào khác.
2. Giao diện dùng chữ "Import" (Import Excel · Import điểm danh từ Excel · Import hoàn tất · Xác nhận import) xen tiếng Việt. Chính đặc tả cũng gọi chức năng là "Import Excel" (`:585`, `:650`) nên **không phải sai đặc tả** — chỉ ghi nhận để BA cân nhắc thống nhất từ ngữ nếu muốn.
3. Ô "Lý do" trong bảng lỗi bị cắt ngắn theo bề rộng cột, nhưng **đủ chữ ở tooltip** (thuộc tính `title`) — không mất thông tin.

**Dấu vết dữ liệu để lại (do chính thao tác đang kiểm):** khóa `KH-QAW7-HOINGHI` nay có thêm **Buổi 5** với 3 bản ghi điểm danh. Lượt kiểm sau nếu cần buổi trắng thì tạo Buổi 6 theo đúng cách trên (Tab Lịch học → Thêm buổi học), không cần khóa khác.
