# Nhật ký đo — `QLHDTVVCG_03` (dòng 309 tab `bug`)

**Ngày:** 2026-08-07 · **Quy trình:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
**Chuẩn chấm đã khóa (Giai đoạn A — CẤM sửa):** [`chuan/QLHDTVVCG_03.md`](../chuan/QLHDTVVCG_03.md) — **đúng 1 vế: C1 `MATCH` → route TEST**.

> ⚠️ Phiếu **route TEST** ⇒ theo chỉ đạo điều phối 07/08 (đợt cắt công): **KHÔNG cắt gì**. Đo đủ 2 đường độc lập,
> chạy trọn luồng, ghi đủ bằng chứng.

---

## 0. Đọc lại dòng phiếu trên bảng trước khi đo (bắt buộc)

Đọc lúc **15:3x ngày 07/08/2026** bằng `tools/sheet_dump_bug_rows_2026-08-07.py --rows 309` (chỉ đọc).

| Ô | Giá trị đọc được |
|---|---|
| `Mã TC` (D) | `QLHDTVVCG_03` |
| `Trạng thái` (N) `N/R` · `Dopai` (O) `N/R` | phiếu **chưa từng chạy** |
| `Kết quả thực tế` (L) · `Ảnh/vieo 1` (M) · `TKM phản hồi lần 1` (Q) | **RỖNG cả ba** |
| `Trạng thái dev fix` (R) | `Fixed` |
| `Kết quả verify` (T) | **RỖNG** |
| `Mô tả` (G) | `Tìm kiếm có kết quả` |
| `Điều kiện` (H) | `1. Đăng nhập hệ thống thành công` / `2. Tồn tại bản ghi phù hợp` |
| `Các bước` (J) | `1. Chọn menu "Hợp đồng Tư vấn"` / `2. Nhập tiêu chí tìm kiếm` / `3. Nhấn "Tìm kiếm"` |
| `Kết quả mong đợi` (K) | `Có kết quả, hệ thống hiển thị danh sách hợp đồng phù hợp trên bảng kết quả.` |
| `DEV phản hồi lần 1` (S) | *"BA chốt 06/08/2026 … giữ quyết định BA 11/05/2026 bỏ menu riêng … **Phần nội dung chức năng Dev đã bổ sung theo SRS: bộ lọc ngữ cảnh cho màn danh sách hợp đồng.**"* |

Không có phiên khác vừa ghi dòng 309.

## 1. Môi trường + vân tay bản dựng

| Hạng mục | Giá trị |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| **Vân tay đầu phiên** (14:14:57) | `assets/index-BbPPdate.js` · `assets/index-DVlgOkLg.css` · `last-modified: Fri, 07 Aug 2026 06:47:57 GMT` · `etag "6a757f9d-428"` |
| **Vân tay kiểm lại** (08:33:07 GMT = 15:33 giờ VN, ngay trước khi chốt phiếu này) | **Y HỆT** — cùng 2 tệp, cùng `last-modified`, cùng `etag` ⇒ **không có bản dựng mới chen giữa**, kết quả đo trong phiếu này và các phiếu trước cùng một bản phần mềm |
| Tài khoản đo | **`cbnv_tw_03`** / `Test@1234` — vai trò **CB NV TW**, đúng `:203`. Không gặp `ERR-AUTH-SYS-00-03`, **không** fallback sang `cbnv_tw_05` |
| Cửa sổ | 1440×900 |
| Thời điểm đo | 15:2x–15:3x ngày 07/08/2026 |

## 2. Bề mặt đã chấm — **MÀN 1**

**Chi tiết Vụ việc → mục "HĐ tư vấn liên kết"** (`/vu-viec/6bf98a2e-77ee-4c03-8e1f-a51561406a3b`), theo chỉ đạo
điều phối: đây là bề mặt chấm chính thức của cả đợt A.

Ô tìm kiếm trên bề mặt này mang **chú thích gợi ý nguyên văn `"Tìm theo tên HĐ, mã HĐ, bên B"`** — trùng khít
3 trường mà `srs-fr-14-hop-dong-tv.md:226` khai là vùng tìm toàn văn. Tức **chính phần mềm tự công bố phạm vi
tìm kiếm đúng bằng phạm vi đặc tả**, nên không có chuyện "gõ trường ngoài đặc tả rồi chấm oan".

> Bước J ghi *"Chọn menu Hợp đồng Tư vấn"* — menu này đã bị bỏ theo `:266`/`:268`. Đây là **tiền đề**, không phải
> vế chấm; đã ghi đường vào thực tế, không log lỗi (câu hỏi BA gộp ở `00-TONG-HOP-QLHDTVVCG.md`).

## 3. Tiền đề đã dựng

| Yêu cầu của chuẩn chấm | Đã có |
|---|---|
| ≥2 hợp đồng trong phạm vi, trong đó **≥1 khớp** và **≥1 KHÔNG khớp** tiêu chí sắp nhập | ✅ 2 hợp đồng trên Màn 1 |
| Từ khóa phải **chỉ khớp đúng 1 bản ghi** (chống bẫy "từ khóa quá chung") | ✅ đã chọn từ khóa phân biệt được, xem §4 |

| Mã | Tên hợp đồng | Bên B |
|---|---|---|
| `HDTV-20260807-0006` | *Hợp đồng tư vấn xác lập quyền **sở hữu trí tuệ** và nhãn hiệu cho **doanh** **nghiệp** nhỏ và vừa* | Chuyên gia **UAT** **QLNDTVVCG** 38 |
| `HDTV-20260807-0007` | *Hợp đồng tư vấn pháp luật lao động và bảo hiểm xã hội cho **doanh** **nghiệp** siêu nhỏ* | QA TVV **PheDuyet** TW R19 |

Cả 2 bản ghi đã tồn tại trước khi phiếu này bắt đầu (`0006` do `_15` tạo, `0007` do `_02` dựng tiền đề).
**Phiếu này không tạo/sửa/xóa bản ghi nào** — xem §8.

## 4. Đo vế C1

### C1 — "Có kết quả, hệ thống hiển thị danh sách hợp đồng phù hợp trên bảng kết quả" · `MATCH` · ❌ **KHÔNG ĐẠT (một phần)**

**Neo đặc tả** (đã mở file đọc lại từng dòng):

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-14-hop-dong-tv.md:226` | `| 2 | Tìm kiếm toàn văn trên tên HĐ, mã HĐ, bên B | — |` |
| `:227` | `| 3 | Áp dụng bộ lọc AND logic | — |` |
| `:228` | `| 4 | Phân trang và trả về | BR-DATA-07 |` |
| `:255` | `- **Given** CB NV nhập từ khóa **When** tìm kiếm **Then** trả DS HĐ matching, phân trang` |
| `:216` | `| 1 | keyword | text | N | Từ khóa (tên HĐ, mã HĐ, bên B) | — | người dùng nhập |` |

---

#### 4.1 · Đường đo 1 — giao diện thật (mỗi lượt: gõ từ khóa → **bấm nút [Tìm kiếm] bằng chuột trên trang**)

| # | Từ khóa gõ vào ô tìm kiếm | Từ khóa này nằm ở đâu | Số dòng bảng trả về | Bảng liệt kê | Ảnh |
|---|---|---|---|---|---|
| 1 | `sở hữu trí tuệ` | **tên HĐ** của `0006`, nguyên văn, đang hiển thị trên chính bảng đó | **0** — hiện dòng *"Không tìm thấy hợp đồng phù hợp"* | — | 01 |
| 2 | `HDTV-20260807-0007` | **mã HĐ** của `0007` | **1** · phân trang *"1-1 / 1 mục"* | `HDTV-20260807-0007` | 02 |
| 3 | `doanh` | **tên HĐ** của cả hai (*"cho **doanh** nghiệp…"*) — **không** có trong mã HĐ, **không** có trong bên B | **2** · *"1-2 / 2 mục"* | `0007`, `0006` | 03 |
| 4 | `nghiệp` | **tên HĐ** của cả hai — **từ đứng ngay sau `doanh` trong cùng một chuỗi tên** | **0** — *"Không tìm thấy hợp đồng phù hợp"* | — | 04 |
| 5 | `UAT QLNDTVVCG` | **bên B** của `0006` — hai từ, cách nhau bằng dấu cách | **1** · *"1-1 / 1 mục"* | `HDTV-20260807-0006` | 05 |

#### 4.2 · Đường đo 2 — đối chứng độc lập: đọc thẳng dữ liệu tìm kiếm từ máy chủ

Gọi thẳng dịch vụ tìm kiếm hợp đồng với **cùng từ khóa**, cùng phạm vi vụ việc, rồi so `tổng số` + danh sách mã
với số dòng đang hiện trên bảng:

| Từ khóa | Máy chủ trả `total` / mã | Bảng trên màn | Khớp? |
|---|---|---|---|
| `sở hữu trí tuệ` | `0` / — | 0 dòng | ✅ khớp |
| `HDTV-20260807-0007` | `1` / `0007` | 1 dòng `0007` | ✅ khớp |
| `doanh` | `2` / `0007`,`0006` | 2 dòng | ✅ khớp |
| `nghiệp` | `0` / — | 0 dòng | ✅ khớp |
| `UAT QLNDTVVCG` | `1` / `0006` | 1 dòng `0006` | ✅ khớp |

**Hai đường khớp nhau từng lượt ⇒ hiện tượng nằm ở phần xử lý tìm kiếm, không phải lỗi vẽ bảng, cũng không phải
"kết quả cũ còn sót trên màn".**

#### 4.3 · Loại trừ các nguyên nhân có thể làm chấm oan

| Nghi vấn | Phép loại trừ | Kết luận |
|---|---|---|
| *Trường **tên HĐ** không nằm trong vùng tìm kiếm?* | `doanh` chỉ xuất hiện trong **tên HĐ** (không có trong mã HĐ, không có trong bên B) mà vẫn trả về **2 bản ghi** | ❌ loại — **tên HĐ CÓ được tìm** |
| *Do nhiều từ cách nhau bằng dấu cách?* | `UAT QLNDTVVCG` (2 từ, có dấu cách) trả **1 bản ghi** đúng; đối chứng thêm `QA TVV`, `QA R19`, `doanh HDTV` đều trả đúng và ghép điều kiện **VÀ** qua nhiều trường | ❌ loại — **nhiều từ hoạt động bình thường**, đúng `:227` |
| *Do chữ hoa / chữ thường?* | `PheDuyet`, `pheduyet`, `PHEDUYET` đều trả cùng 1 bản ghi | ❌ loại |
| *Do bản ghi này bất thường (dữ liệu bẩn)?* | Đối chứng trên **tập dữ liệu khác** (4 hợp đồng gắn 1 tư vấn viên, trong đó 3 hợp đồng nền có cụm *"sở hữu trí tuệ"* ngay trong tên): `sở hữu trí tuệ` → **0**, `hữu` → **0**, nhưng `UAT` → **1**, `QLNDTVVCG` → **1** | ❌ loại — **hiện tượng lặp lại y hệt trên tập dữ liệu khác** |
| *Do ô tìm kiếm và dịch vụ hiểu khác nhau về dấu cách khi truyền đi?* | Trường hợp `nghiệp` chỉ có **một từ, không có dấu cách nào** mà vẫn trả 0 | ❌ loại |

#### 4.4 · Cặp đối chứng quyết định

> `doanh` → **2 bản ghi**   ·   `nghiệp` → **0 bản ghi**

Hai từ này **đứng liền nhau trong cùng một chuỗi tên hợp đồng, của cùng những bản ghi đó** (*"…cho doanh nghiệp
nhỏ và vừa"*). Khác biệt duy nhất giữa chúng: `nghiệp` **có dấu tiếng Việt**, `doanh` **không có dấu**.

Bổ sung cùng chiều, cùng một trường bên B của cùng một bản ghi *"Chuyên gia UAT QLNDTVVCG 38"*:
`UAT` → **1 bản ghi** · `QLNDTVVCG` → **1 bản ghi** · `Chuyên` → **0 bản ghi**.

#### 4.5 · Kết luận C1

Ô tìm kiếm **có lọc thật** (không trả bừa toàn bộ danh sách), **có phân trang**, **ghép nhiều từ theo điều kiện
VÀ** — các phần này đúng `:226`–`:228`.

Nhưng **từ khóa chứa chữ tiếng Việt có dấu thì không bao giờ khớp được bản ghi nào**, kể cả khi từ khóa được lấy
**nguyên văn từ tên hợp đồng đang hiển thị ngay trên bảng đó**. Gõ lại phiên bản **không dấu** của chính từ đó
cũng không ra kết quả. Hiện tượng xảy ra ở **cả 3 trường** `:226` khai (đo được ở tên HĐ và bên B; mã HĐ theo
quy tắc sinh `HDTV-{ngày}-{số thứ tự}` vốn không có dấu nên không quan sát được).

Tên hợp đồng trong hệ thống này là **tiếng Việt có dấu**, nên trên thực tế người dùng gõ tên hợp đồng để tìm sẽ
**luôn ra rỗng**. Đây chính là mệnh đề cột `K` của phiếu: *"Có kết quả, hệ thống hiển thị danh sách hợp đồng phù
hợp"* — có bản ghi phù hợp thật (điều kiện `H` mục 2 đã thoả) mà bảng trả về rỗng.

⇒ **Vế C1 (`MATCH`) bị chứng minh là hỏng** ở lớp từ khóa tiếng Việt có dấu.

## 5. Verdict

| Vế | Quan hệ | Kết quả đo |
|---|---|---|
| C1 — nhập từ khóa → bảng hiện danh sách hợp đồng phù hợp | `MATCH` | ❌ **KHÔNG ĐẠT** — đạt với từ khóa không dấu (mã HĐ); **hỏng với mọi từ khóa tiếng Việt có dấu**, kể cả lấy nguyên văn từ tên HĐ đang hiển thị |

Phiếu chỉ có **1 vế**, vế đó là `MATCH` và **bị chứng minh hỏng** ⇒ theo bảng Verdict flow 04 + `QĐ-01`:
**Verdict = Reopen** ⇒ ô `Trạng thái dev fix` (R) = **`Reopen`**.

> Không viết *"fix không có tác dụng"*: phiếu chưa từng chạy (`N/R`), không có ảnh lỗi cũ để so ⇒ chỉ kết luận
> **hiện trạng đo được hôm nay**.

## 6. Ghi nhận (KHÔNG chấm, không kéo verdict)

- **Khớp theo TỪ TRỌN VẸN, không khớp chuỗi con.** `0007` → 0 bản ghi (dù `HDTV-20260807-0007` → 1);
  `PheDuy` → 0 (dù `PheDuyet` → 1). Đặc tả `:226` dùng chữ **"tìm kiếm toàn văn"** — khớp theo từ là **đúng bản
  chất** của tìm kiếm toàn văn, đặc tả không đòi khớp chuỗi con ⇒ **KHÔNG tính lỗi**. Ghi lại để đợt sau
  **không chấm oan** khi gõ một mẩu mã hợp đồng rồi thấy rỗng.
- **Ghi chú kỹ thuật cho người đo sau:** tham số từ khóa mà giao diện gửi đi tên là `search`, và tham số này
  **KHÔNG được khai** trong bản mô tả dịch vụ `/api/docs-json` (ở đó chỉ khai `trangThai`, `tuVanVienId`,
  `toChucTuVanId`, `vuViecId`, `tuNgay`, `denNgay`). Ai định đối chứng bằng cách gọi thẳng dịch vụ mà đi tra tài
  liệu sẽ tưởng là không có tìm kiếm — phải đọc đúng lời gọi mà giao diện phát ra.
- **Nội dung HĐ và ghi chú không nằm trong vùng tìm** — đúng `:226`. `tue`, `huu` (có mặt nguyên văn trong ô
  *Nội dung* của `0006`) trả 0 bản ghi. **Không tính lỗi.**

## 7. Quan sát ngoài vế — **candidate**, KHÔNG log thành bug

Không có. Toàn bộ hiện tượng đo được trong phiếu này nằm **trong** vế C1 hoặc thuộc nhóm "đúng đặc tả" ở §6.

> **Cổng "bug mới tự lộ"** (flow 04, luật 3): phiếu này **không dùng phép xác nhận thêm nào** ngoài các lượt đo
> của chính vế C1.

## 8. Dữ liệu đã thay đổi trên môi trường (bắt buộc khai)

**KHÔNG THAY ĐỔI GÌ.** Phiếu này chỉ đọc: `:244` ghi *"Read-only, không thay đổi dữ liệu"*.

| Đổi gì | Bản ghi | Env | Lúc |
|---|---|---|---|
| — không tạo, không sửa, không xóa bản ghi nào | — | `18.143.165.120.nip.io` (**nội bộ**) | — |

Bối cảnh dữ liệu (đã khai ở phiếu trước, nhắc lại để đọc độc lập được): `HDTV-20260807-0006` do `_15` tạo lúc
14:43; `HDTV-20260807-0007` do `_02` dựng tiền đề lúc 15:1x; 1 tệp đính kèm do điều phối nạp vào `0006` lúc
14:57. **Không** đụng dữ liệu đối tác.

## 9. Ảnh bằng chứng (đã mở lại xem từng ảnh trước khi dùng)

| Ảnh | Nội dung | Liên kết xem được |
|---|---|---|
| `QLHDTVVCG_03-01-tu-khoa-co-dau-lay-tu-ten-HD-khong-ra-ket-qua.png` | Ô tìm kiếm chứa `sở hữu trí tuệ` (lấy nguyên văn từ tên HĐ `0006`) → bảng hiện *"Không tìm thấy hợp đồng phù hợp"*; thấy rõ chú thích ô là *"Tìm theo tên HĐ, mã HĐ, bên B"* | https://drive.google.com/file/d/1VCmA9j7KjRNaBmgxRM99IWQR9s-HHrKd/view?usp=drivesdk |
| `QLHDTVVCG_03-02-tu-khoa-ma-HD-ra-dung-1-dong-loai-ban-ghi-khong-khop.png` | Ô tìm kiếm chứa `HDTV-20260807-0007` → đúng **1** dòng, phân trang *"1-1 / 1 mục"*, bản ghi kia bị loại | https://drive.google.com/file/d/176lLNuo0jHqY7NgtaWYvnwUGil6aPgvx/view?usp=drivesdk |
| `QLHDTVVCG_03-03-tu-khoa-khong-dau-trong-ten-HD-ra-2-dong.png` | Ô tìm kiếm chứa `doanh` (chỉ có trong **tên HĐ**) → **2** dòng, *"1-2 / 2 mục"* ⇒ tên HĐ CÓ được tìm | https://drive.google.com/file/d/1SdPtfO5oMifK8WknCCuJb2aDvV0Iq0PB/view?usp=drivesdk |
| `QLHDTVVCG_03-04-tu-khoa-co-dau-ke-ben-trong-cung-ten-HD-khong-ra-dong-nao.png` | Ô tìm kiếm chứa `nghiệp` — **từ đứng ngay cạnh `doanh`** trong cùng chuỗi tên → **0** dòng | https://drive.google.com/file/d/1HKYC0s9d8kvmrpeB6be5Q-XdVHvsnCE3/view?usp=drivesdk |
| `QLHDTVVCG_03-05-hai-tu-khong-dau-cach-nhau-van-ra-dung-1-dong.png` | Ô tìm kiếm chứa `UAT QLNDTVVCG` (2 từ, có dấu cách) → đúng **1** dòng ⇒ nhiều từ hoạt động bình thường | https://drive.google.com/file/d/1xsWwQj-HFptoufcElBCMGCcGhEbi5t1z/view?usp=drivesdk |

## 10. Cổng chốt verdict — trả lời đủ 5 câu (flow 04)

1. **Hành động tranh chấp đã bấm trên giao diện thật chưa?** Rồi — cả **5 lượt** tìm kiếm đều gõ vào ô tìm kiếm
   trên trang rồi **bấm nút [Tìm kiếm]**; không có lượt nào kết luận bằng cách gọi dịch vụ thay cho thao tác.
2. **Vế có đủ 2 đường đo độc lập không?** Có — giao diện (§4.1) và đọc thẳng dữ liệu tìm kiếm từ máy chủ (§4.2),
   khớp nhau **cả 5/5 lượt**.
3. **Có Pass/Fail bằng quan sát tĩnh không?** Không. Bảng có **2 bản ghi thật**, mỗi kết luận đều dựa trên một
   lượt bấm tìm kiếm có ảnh, và mỗi lượt đều đối chiếu với `tổng số` do máy chủ trả.
4. **Có hạ `MATCH` xuống `DIFF`/`GAP` để né kết luận không?** Không. C1 giữ `MATCH` và kết **không đạt**.
5. **Đã khai dữ liệu thay đổi chưa?** Rồi — §8: **không thay đổi gì**, phiếu chỉ đọc.

---

## Phụ lục — điều phối kiểm lại độc lập (15:55 ngày 07/08/2026)

Lý do: `_03` là kết quả `Reopen` **duy nhất** của cả lô 23 phiếu ⇒ là thứ duy nhất bộ phận phát triển
sẽ thật sự bắt tay sửa. Kiểm lại bằng **đường thứ ba**: gọi thẳng máy chủ bằng `curl`, tài khoản
`cbnv_tw_03`, **không qua giao diện** (loại trừ khả năng lỗi nằm ở khâu hiển thị).

Ngữ cảnh: vụ việc `VV-BTP-TW-20260804-004` · 1 hợp đồng `HDTV-20260807-0006`
tên `"Hợp đồng tư vấn xác lập quyền sở hữu trí tuệ và nhãn hiệu cho doanh nghiệp nhỏ và vừa"`.

**Mọi từ dưới đây đều lấy từ ĐÚNG chuỗi tên đó** — cùng một trường, cùng một bản ghi:

| Từ khóa | Có dấu | HTTP | Số bản ghi |
|---|---|---|---|
| `cho` | không | 200 | **1** |
| `doanh` | không | 200 | **1** |
| `Hợp` | có | 200 | 0 |
| `hiệu` | có | 200 | 0 |
| `hữu` | có | 200 | 0 |
| `lập` | có | 200 | 0 |
| `nghiệp` | có | 200 | 0 |
| `nhãn` | có | 200 | 0 |

⇒ **6/6 từ có dấu trả về rỗng · 2/2 từ không dấu trả về đúng bản ghi.** Mở rộng cặp đối chứng của
nhóm đo (1 từ) lên 6 từ, trên cùng một chuỗi. Kết luận `Reopen` **được xác nhận**, không phải chấm oan.

Mọi lượt đều HTTP 200 ⇒ không phải lỗi quyền, không phải lỗi máy chủ; máy chủ trả về danh sách rỗng
một cách bình thường.

Kịch bản: `scratchpad/verify_search_dau.py`.
