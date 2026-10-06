# Tiêu chí verify — QLTLPLCVV_17

```
Mã case: QLTLPLCVV_17 (tab `bug`, dòng 300)     Thời điểm viết: 2026-08-06 14:19
Môi trường verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên env nghiệm thu khác)
Bản dựng: HTPLDN · V1.0.8 · bó mã FE `assets/index-DIABnbIr.js` (+ `assets/index-DVlgOkLg.css`)
          · `GET /` last-modified `Thu, 06 Aug 2026 07:13:15 GMT` (14:13:15 giờ VN) · etag `W/"6a74340b-428"`
          Đo lúc 14:22 và đo lại cuối phiên — không đổi.
          ⚠️ Bó mã này KHÁC lô B6 sáng nay (`index-CNwX9JjX.js`, last-modified 02:51:16 GMT) trong khi
          số phiên bản vẫn là V1.0.8 ⇒ env deploy lại lúc 14:13 mà không đổi số phiên bản. Chỉ ghi
          "V1.0.8" là không truy được đã đo bản nào.
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow 04 §Giai đoạn A):
> - `output/UAT_doi-tac/reverify-week-3/verify1-conlai-2026-08-03/reverify-audit/QLTLPLCVV_17.md`
>   — vòng verify 2026-08-03 trên bản dựng **V1.0.5**, kết luận `Pass`, kèm bảng số đo cũ.
> - `output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.md` (dòng 416-417 — bảng theo dõi bug đối tác).
>
> **Mục 4 và mục 5 dưới đây suy TỪ ĐẶC TẢ + kỳ vọng đối tác, KHÔNG lấy số đo cũ làm ngưỡng.**
> Số đo cũ đo trên bản dựng khác (V1.0.5) nên **không có giá trị chứng minh** cho lượt đo này;
> phải đo lại từ đầu, tự seed dữ liệu của lượt này.

---

## 1. Đối tác phản ánh

Mô tả case: **"Xem tệp trực tuyến"**. Kết quả thực tế đối tác ghi: **"Hệ thống disable nút chức năng Xem"**.

Tách vế:

| Vế | Nội dung | Trạng thái đặc tả |
|---|---|---|
| **(a)** | Nút/điều khiển mở tệp đính kèm trong Nhóm 3 "Tư liệu pháp lý liên kết" **bị vô hiệu hoá** → người dùng không mở được tệp | đặc tả **nói rõ** (:818, :958, :981) |
| **(b)** | Định dạng **xem trực tuyến được** (PDF, hình ảnh) phải mở **trình xem trực tuyến** | đặc tả **nói rõ** (:981) |
| **(c)** | Định dạng **không** xem trực tuyến được phải **tải tệp về máy** người dùng | FR-X.1-06 **IM LẶNG** (chỉ nhóm VII — Biểu mẫu — có quy định này, module khác) |

**Bằng chứng đã xem:** `partner-evidence/QLTLPLCVV_17_v2.jpg` (214.164 byte, ảnh tĩnh, đã mở **full-res**
1920×1041 bằng Read tool). Đọc được trên ảnh:

- Hộp thoại chi tiết tư liệu đang mở: Tên = "tài liệu kiểm thử" · Loại tư liệu = **Tài liệu** ·
  Lĩnh vực pháp luật = Sở hữu trí tuệ · Mô tả = "tkm" · chỉ có nút **[Đóng]** (không có nút Lưu).
- Khung "File đính kèm" ghi rõ điều kiện tải lên: *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls,
  .xlsx, .jpg, .png. Dung lượng tối đa 20MB/tệp."*
- Dòng dưới cùng: `📎 Báo cáo mẫu.docx` kèm chữ `👁 Xem` **màu xám nhạt** (trong khi nút `Xem tệp` của
  bảng phía sau vẫn màu xanh) ⇒ đúng triệu chứng "disable nút Xem".
- Bảng phía sau hộp thoại: hàng tư liệu "tài liệu kiểm thử" có hành động `Xem tệp / Hủy công khai / Xóa`
  ⇒ tư liệu đang ở trạng thái **Đã công khai**; có nút **[Thêm tư liệu]** ⇒ vai trò có quyền CRUD.

**Kiểm bằng chứng có đúng case này không:** ✅ đúng. Ảnh chụp đúng màn *Tư vấn chuyên sâu → chi tiết →
Nhóm "Tư liệu pháp lý liên kết"*, đúng triệu chứng *nút Xem bị vô hiệu*, khớp cả mô tả lẫn 4 bước của case.

> ⚠️ Ghi chú lệch mã (không ảnh hưởng phạm vi): trên bảng theo dõi cũ của đối tác
> (`bug-con-fail-doi-tac-2026-07-31.md`) dòng 1513 mang mã `QLTLPLCVV_17` lại là case *"Xóa tệp đính kèm
> khi tư liệu Công khai"*, còn *"Xem tệp trực tuyến"* nằm ở dòng 1514 (`QLTLPLCVV_18`). Phạm vi lượt này
> bám **dòng 300 tab `bug`** như prompt giao, và nội dung dòng 300 khớp khít ảnh bằng chứng.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`
— **FR-X.1-06: Quản lý tư liệu pháp lý của vụ việc (UC152)** (bắt đầu dòng 809).

Quote nguyên văn (đã mở file đọc đúng dòng, không lấy từ trí nhớ):

- `:818` — *"CRUD tư liệu pháp lý gắn với vụ việc tư vấn chuyên sâu. Hỗ trợ upload/xóa/**preview file**,
  công khai/hủy công khai tư liệu lên Cổng PLQG."*
- `:843` — bảng *Inputs — File tư liệu*, hàng 1: *"file_data | file | Y (khi tải lên) |
  **PDF/DOCX/XLS/image**, max 20MB"*.
- `:958` — Postconditions: *"File được tải lên/xóa/**preview**"*.
- `:981` — Acceptance Criteria: *"**Given** CB NV xem file trực tuyến **When** chọn file **Then**
  hiển thị preview"*.
- `:979` — AC `[STT63 UAT 2026-06-02]`: *"**Given** Chuyên gia được phân công mở section "Tư liệu pháp lý"
  của TVCS mình phụ trách (trạng thái ≥ PHAN_CONG) **When** xem/tải tư liệu **Then** hiển thị chế độ chỉ đọc
  (**xem + tải/preview**), ẩn nút Thêm/Sửa/Xóa/Công khai (BR-AUTH-14)…"*
- `:815` — *"**Màn hình:** ~~SCR-X1-07~~ (DEPRECATED v2.1 — gộp thành tab "Tư liệu PL" trong
  SCR-X1-02 / MH-12.2)"* ⇒ surface hợp lệ để đo là **accordion "Tư liệu pháp lý liên kết" trong màn chi tiết
  TVCS**, không phải màn đã bỏ.
- `:1158` — SCR-X1-02 thành phần 6: *"Accordion: Tư liệu PL liên kết (UC152) | table | Bảng tư liệu:
  Tên / Loại / Lĩnh vực / Số file / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / **Hành động**.
  Nút [+ Thêm tư liệu] (inline trong tab này)"*.
- `:902` — Processing Chỉnh sửa bước 3: *"Kiểm tra trạng thái: nếu CONG_KHAI → từ chối sửa (phải hủy công
  khai trước)"* ⇒ tư liệu **Đã công khai** mở ra ở chế độ chỉ đọc là ĐÚNG đặc tả — **không** được lấy
  "hộp thoại không có nút Lưu" làm lỗi.

**IM LẶNG về:**

1. **Fallback khi định dạng không xem trực tuyến được** — FR-X.1-06 không có bước nào tương ứng.
   *(Quy định "Nếu không hỗ trợ preview: thông báo + chuyển sang tải về" chỉ tồn tại ở
   `srs-fr-09-bieu-mau.md:338` — FR-VII-03, module **Biểu mẫu**, KHÔNG áp cho nhóm X.1.)*
2. **Nhãn / hình thức của điều khiển mở tệp** (gọi "Xem", "Xem tệp", "Tải về"…), số lượng điều khiển,
   mở ở tab mới hay trong trang.
3. **Định dạng nào bắt buộc render inline** — `:981` chỉ nói "xem file trực tuyến → hiển thị preview",
   không liệt kê danh sách định dạng; không đòi .docx phải chuyển sang PDF.
4. **Trình xem cụ thể** (thư viện, giao diện, nút xoay/phóng).

## 3. Precondition

- **Tài khoản:** `cbnv_tw_02` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), mật khẩu `Test@1234`.
  Đây đúng vai trò đọc được trên ảnh đối tác ("Cán bộ NV Trung ương · CB_NV_TW", đơn vị BTP · TW).
  Fallback theo Rule 7 nếu login fail: `cbnv_tw_03` (cùng vai trò + cùng cấp).
- **Màn:** `https://18.143.165.120.nip.io` → menu **Tư vấn → Tư vấn chuyên sâu** → mở chi tiết 1 bản ghi
  (`/tv-chuyen-sau/{id}`) → nhóm **"Tư liệu pháp lý liên kết"**.
- **Dữ liệu tiền đề:** ≥1 tư liệu pháp lý gắn TVCS, có đính **≥3 tệp thật** phủ đủ 3 dạng ở mục 5.
  Đo ở **cả 2 trạng thái tư liệu**: `Nháp` và `Đã công khai` (ảnh đối tác là **Đã công khai**).
  Thiếu dữ liệu → **tự seed bằng chính luồng chuẩn** ([+ Thêm tư liệu] trên giao diện), khai rõ đã seed gì.

## 4. Tiêu chí chấm

✅ **PASS khi ĐỦ CẢ 5 điều** dưới đây (đo trên vai trò CB Nghiệp vụ, ở cả 2 trạng thái tư liệu):

1. **Điều khiển mở tệp thao tác được** — với **từng tệp** trong M dạng, ở **cả 2 lối vào** (hành động trên
   hàng bảng của Nhóm 3, và điều khiển cạnh tên tệp trong hộp thoại chi tiết tư liệu): điều khiển tồn tại
   trong trang, **không ở trạng thái vô hiệu hoá** — đo được bằng `disabled` = false · `pointer-events` ≠
   `none` · `opacity` = 1 · màu chữ không phải xám nhạt · kích thước > 0.
2. **Bấm thật có kết quả** — bấm bằng thao tác giao diện thật (không gọi API thay), hệ thống phản hồi:
   mở trình xem, mở tab/khung xem, hoặc chuyển tệp về máy. **Bấm không có gì xảy ra = FAIL.**
3. **Định dạng xem trực tuyến được (PDF, ảnh): nội dung tệp thật sự hiện ra** — không phải khung trống:
   PDF đọc được chữ đã nạp vào tệp gốc; ảnh render đúng, `naturalWidth × naturalHeight` khớp kích thước
   thật của tệp đã tải lên.
4. **Định dạng còn lại (.docx): người dùng tiếp cận được nội dung tệp** — nhận được tệp về máy (hoặc được
   thông báo rõ kèm đường tải), và tệp nhận được **đúng tên · đúng số byte · đúng chữ ký định dạng**
   so với tệp đã tải lên. *(Nhánh này đặc tả im lặng về CÁCH làm — xem mục 4 "KHÔNG chấm Fail vì".)*
5. **Đối chứng bằng đường thứ hai** — sau khi đo giao diện, gọi thẳng API tải tệp trong cùng phiên và so
   số byte / chữ ký với tệp gốc. **Hai đường mâu thuẫn ⇒ chưa được chốt.**

❌ **FAIL nếu** bất kỳ điều nào xảy ra ở **bất kỳ** dạng tệp / trạng thái tư liệu nào:

- Điều khiển mở tệp **bị vô hiệu hoá** (mờ / `disabled` / `pointer-events:none`) — chính triệu chứng đối tác.
- Điều khiển bấm được nhưng **không có phản hồi nào**.
- Mở ra **khung trống** / tệp nhận về **0 byte** / nội dung **không phải tệp đã tải lên**.
- Chỉ **một phần** dạng chạy được (vd PDF mở được nhưng .docx vẫn kẹt) ⇒ fix một phần ⇒ **Reopen**.

🚫 **KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):

- .docx **không** được chuyển sang PDF để xem trực tuyến (quy định đó thuộc `srs-fr-09-bieu-mau.md:338`,
  module Biểu mẫu — không áp cho nhóm X.1).
- Nhãn điều khiển là "Xem" / "Xem tệp" / "Tải về", số lượng lối vào, mở tab mới hay mở trong trang.
- Giao diện trình xem (thiếu nút xoay/phóng/in, thanh công cụ khác kỳ vọng).
- Hộp thoại tư liệu **Đã công khai** không có nút Lưu (đúng `:902`).

## 5. Dạng dữ liệu phải phủ — **M = 3**

| # | Dạng | Vì sao nằm trong M |
|---|---|---|
| D1 | `.pdf` | Đối tác nêu đích danh trong kỳ vọng ("PDF"); `:843` liệt kê PDF |
| D2 | `.png` (hình ảnh) | Đối tác nêu đích danh ("hình ảnh"); `:843` liệt kê image |
| D3 | `.docx` | **Đúng định dạng tệp trong ảnh bằng chứng** (`Báo cáo mẫu.docx`) — nhánh "không xem trực tuyến được"; `:843` liệt kê DOCX |

**Nguồn xác định M:** ① đặc tả `:843` (bảng Inputs — File tư liệu, ràng buộc định dạng) ·
② ô "Kết quả mong đợi" của đối tác chia **2 nhánh** định dạng (hỗ trợ / không hỗ trợ) ·
③ chú thích định dạng cho phép ngay trên khung tải tệp trong ảnh bằng chứng
(`.pdf, .doc, .docx, .xls, .xlsx, .jpg, .png`).
⇒ **M = 1 là không hợp lệ** cho case này vì kỳ vọng có 2 nhánh định dạng.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — badge "Cán bộ NV Trung ương · CB_NV_TW", đơn vị BTP · TW | `cbnv_tw_02` — vai trò **CB_NV_TW**, cấp **TW**, đơn vị `00000000-0000-4000-8000-000000000001` (Cục Bổ trợ tư pháp - Bộ Tư pháp). **Trùng khít cả vai trò lẫn cấp**, không phải nới chiều nào. Không dùng tài khoản quản trị để ra verdict | **Không** |
| Entity + trạng thái | Tư liệu **Đã công khai** (hàng có `Xem tệp / Hủy công khai / Xóa`); TVCS không đọc được trạng thái vì bị hộp thoại che | Đo **CẢ 2** trạng thái tư liệu: **Nháp** (14:27) và **Đã công khai** (14:33 — hàng hiện `Xem tệp / Hủy công khai / Xóa`, trùng khít hàng trong ảnh đối tác, xem ảnh `-08`). TVCS ở **Tiếp nhận**; trạng thái TVCS không đọc được trên ảnh đối tác nên không thể đối chiếu — nhưng kết quả **giống nhau ở cả 2 trạng thái tư liệu**, và đặc tả FR-X.1-06 không gắn quyền xem tệp với trạng thái TVCS | **Không** |
| Dữ liệu tiền đề | 1 tư liệu "tài liệu kiểm thử", Loại = Tài liệu, Lĩnh vực = Sở hữu trí tuệ, **1 tệp `Báo cáo mẫu.docx`** | 1 tư liệu QA tự seed `14cef4af-cb15-497b-88d6-8ed3ad22d9e7`, **Loại = Tài liệu**, **Lĩnh vực = Sở hữu trí tuệ** (giống hệt đối tác), đính **3 tệp thật**: `.pdf` 629 B · `.png` 45.802 B · **`.docx` 964 B** (bao trùm đúng định dạng `.docx` của đối tác) | **Không** |
| Input / filter / giá trị nhập | Không có ô lọc nào trong ảnh; thao tác = bấm `👁 Xem` cạnh tên tệp trong hộp thoại chi tiết tư liệu | Bấm **thật** nút `👁 Xem` cạnh từng tên tệp trong hộp thoại **"Xem tư liệu pháp luật"** (mở từ hành động `[Xem tệp]` của hàng — đúng lối vào ảnh đối tác). Kiểm thêm nút `[Xem]` trong hộp thoại "Thêm tư liệu" và thử bấm vào **chữ tên tệp** | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 tư liệu · M = 1 dạng (`.docx`) | **N = 1 tư liệu × 2 trạng thái = 2 bản ghi-trạng thái · M = 3/3 dạng** (`.pdf` · `.png` · `.docx`) ⇒ **6 lượt bấm thật** + 3 lượt đối chứng API + 3 lượt đo nút trong hộp thoại Thêm. Phủ rộng hơn đối tác (1×1) | **Không** |

**Sửa đổi tiêu chí giữa chừng:** không có. Mục 4 và 5 giữ nguyên như lúc 14:19, trước khi mở màn.

**Kết quả chấm theo mục 4** (đo 14:22 → 14:37):

| # | Tiêu chí PASS | Kết quả |
|---|---|---|
| 1 | Điều khiển mở tệp không bị vô hiệu hoá, cả 2 lối vào | ✅ 6/6 lượt: `disabled=false` · `pointer-events:auto` · `opacity:1` · màu `rgb(9,88,217)` xanh · `cursor:pointer` · 68×24 px |
| 2 | Bấm thật có kết quả | ✅ 6/6 lượt đều có phản hồi (mở trình xem / mở khung ảnh / chuyển tệp về máy) |
| 3 | PDF + ảnh: nội dung hiện thật | ✅ PDF render đọc được đúng câu đã nạp; ảnh render `naturalWidth×Height = 240×90` đúng tệp gốc |
| 4 | `.docx`: người dùng nhận được tệp | ✅ tệp về máy đúng tên, **964 B**, **md5 `a397f16763a5e49b88637f87fc779697` trùng tệp gốc**, mở zip đọc được đúng nội dung |
| 5 | Đối chứng đường thứ hai | ✅ API trả 200 cho cả 3 tệp, số byte 629 / 45.802 / 964 + chữ ký `%PDF` / `\x89PNG` / `PK` khớp gốc — **không mâu thuẫn** với giao diện |

⇒ Vế (a) và (b) **hết lỗi**. Vế (c) (đặc tả im lặng): bản dựng **tải tệp `.docx` về máy** — **đúng như đối tác
mong đợi** ⇒ theo flow §"Đo xong thấy hết bất đồng → bỏ khỏi danh sách hỏi BA", **không mở câu hỏi BA**.

**Quan sát phụ (không kéo verdict):** chữ tên tệp là `<span>` thường (`cursor:auto`, màu đen), bấm vào không
làm gì; chỗ bấm là nút `[Xem]` ngay cạnh. Đặc tả không quy định hình thức/nhãn điều khiển, và chính đối tác
ghi *"Hệ thống disable nút chức năng Xem"* ⇒ họ cũng thao tác trên nút này. Không log lỗi, không hỏi BA.

**Số đo đầy đủ:** [`../ketqua-QLTLPLCVV_17.txt`](../ketqua-QLTLPLCVV_17.txt)

**3 dữ kiện neo của đối tác:**
`htpldn-uat.ospgroup.vn/tv-chuyen-sau/07e06acc-bdfc-43af-9e62-d600bdc4c258` ·
tư liệu **Đã công khai**, 1 tệp `.docx` ·
vai trò **CB_NV_TW** (BTP · TW), env **nghiệm thu `htpldn-uat.ospgroup.vn`**, bản dựng **HTPLDN · V1.0.3**,
thời điểm **03/08/2026 10:31**.

> **Giới hạn hiệu lực (không phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản dựng
> **V1.0.3**; lượt này đo trên env **nội bộ** `18.143.165.120.nip.io` với bản dựng ghi ở đầu file. Verdict
> chỉ có hiệu lực cho env + bản dựng đã ghi, phải re-verify khi bản dựng đó lên env nghiệm thu.
