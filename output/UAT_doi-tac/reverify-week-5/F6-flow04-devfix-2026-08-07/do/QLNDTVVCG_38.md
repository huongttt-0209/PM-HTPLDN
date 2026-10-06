# Hồ sơ đo — QLNDTVVCG_38 (dòng 288) · FLOW 04 Giai đoạn B

> Chuẩn chấm đã khóa TRƯỚC khi mở màn: [`../chuan/QLNDTVVCG_38.md`](../chuan/QLNDTVVCG_38.md).
> Quan hệ vào đo: **C1·C2·C3·C4 = `MATCH` → TEST** · **C5 = `GAP` → BA**. **Giữ nguyên sau khi đo** (luật khóa 5).

## 1. Verdict

| | |
|---|---|
| **Verdict** | 🟡 **Cần BA** |
| **Ô "Trạng thái dev fix"** | `BA confirm` |
| **🔴 WEB HIỆN TẠI** | **ĐÚNG kỳ vọng đối tác.** Cả 4 vế `MATCH` (C1–C4) đều đạt; triệu chứng TKM báo (*popup "Phân công hàng loạt chưa được hỗ trợ"*) **không còn tái hiện** |
| **Vì sao vẫn "Cần BA"** | Còn **1 vế `GAP`** — C5 (*"cùng MỘT chuyên gia cho tất cả"*). Đặc tả **im lặng** về việc chọn chuyên gia chung hay riêng từng hồ sơ ⇒ luật khóa 5 cấm biến `GAP` thành `MATCH` chỉ vì web làm đúng ý đối tác. Câu hỏi BA nhằm **bổ sung điều này vào đặc tả**, **KHÔNG chặn bàn giao** |
| **Lỗi mới phát sinh** | **Có 1** — nhãn trạng thái lệch bảng nhãn đặc tả (xem §7). Không kéo verdict của dòng này |

---

## 2. Hoàn cảnh đo

| | |
|---|---|
| **Môi trường** | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác |
| **Bó mã FE** | **`index-D4Buvu4S.js`** (`last-modified` `06 Aug 2026 19:23:01 GMT` = 07/08 02:23 giờ VN). Đã tải lại trang bằng địa chỉ trước khi đo. Xem [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| **Tài khoản** | `cbnv_tw_04` / `Test@1234` — `vaiTro: ["CB_NV_TW"]`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`. Đúng vai trò `TVCS_ASSIGN` của `srs-v3.5.md:1440`. **Không dùng `admin`** |
| **Thời điểm** | 07/08/2026 **02:33 – 02:42** giờ VN |
| **Bản ghi đo** | `TVCS-QLND38-UAT-01` + `TVCS-QLND38-UAT-02` — cả hai `TIEP_NHAN`, lĩnh vực **Thương mại** (`bbbbbbbb-…-001c`), đơn vị `00000000-…-0001` = **đúng đơn vị tài khoản đo** |
| **Chuyên gia đã chọn** | `Chuyên gia UAT QLNDTVVCG 38` — id `38383838-0000-4000-8000-000000000038`, `loai_tvv = CG`, `HOAT_DONG`, chuyên môn **Luật thương mại** |

### 2.1 🔴 Dữ liệu đã thay đổi trên môi trường — BẮT BUỘC khai

Vế C4 **buộc phải xác nhận thật** (bẫy PASS oan §6.2.1 cấm chấm bằng quan sát tĩnh), nên lượt đo này **có
thay đổi dữ liệu**:

| Bản ghi | Trước | Sau |
|---|---|---|
| `TVCS-QLND38-UAT-01` | `TIEP_NHAN`, chưa có CG, `version 1` | `PHAN_CONG`, CG = `Chuyên gia UAT QLNDTVVCG 38`, `ngayPhanCong 2026-08-06T19:38:14.431Z`, `version 2` |
| `TVCS-QLND38-UAT-02` | `TIEP_NHAN`, chưa có CG, `version 1` | `PHAN_CONG`, CG = `Chuyên gia UAT QLNDTVVCG 38`, `ngayPhanCong 2026-08-06T19:38:14.429Z`, `version 2` |

Ghi chú phân công đã nhập: `QA-QLND38-20260807-0240 phan cong hang loat 2 ho so`.

⚠️ **Hai bản ghi này đã bị tiêu**: không còn ở `TIEP_NHAN` nên **không dùng lại được** cho lượt đo sau.
Muốn đo lại phải dựng mới bằng `[+ Thêm yêu cầu TV]` (`srs-fr-12:1117`) — hoặc dùng các hồ sơ `TIEP_NHAN` cùng
lĩnh vực Thương mại còn lại trên env: `TVCS-20260805-0003`, `TVCS-20260805-0001`, `TVCS-20260803-0003`,
`TVCS-20260725-0008`, `TVCS-20260725-0007`, `TVCS-20260725-0001`, `TVCS-20260721-0001`, `TVCS-TNND01-UAT`,
`TVCS-20260806-0003`.
**Không đụng dữ liệu của đối tác** — hai hồ sơ này là dữ liệu UAT dựng riêng cho chính case này.

### 2.2 Kiểm tiền đề TRƯỚC khi bấm — chống FAIL oan §6.1.1

Bẫy FAIL oan số 1 là *"cửa sổ chọn chuyên gia rỗng vì đơn vị không có ai `loai_tvv='CG'`"* (sự cố có thật 21/07).
Đã kiểm trước bằng cách mở cửa sổ phân công **từng dòng** trên **một hồ sơ Thương mại KHÁC**
(`TVCS-20260805-0003`) — cố ý không đụng 2 hồ sơ mục tiêu — rồi **đóng bằng [Hủy], không xác nhận**.

Danh sách chuyên gia **không rỗng**, đúng 2 mục và **cả hai đều phủ lĩnh vực Thương mại**:
```
Chuyên gia UAT QLNDTVVCG 38 — Thương mại
QA TVV Seed28 Active — Đất đai, Lao động, Thuế, Thương mại
```
⇒ Bẫy đã loại trừ trước khi bấm nút hàng loạt.

---

## 3. Kết quả từng vế

| Vế | Nội dung | Đo được | Kết luận |
|---|---|---|---|
| **C1** | Danh sách TVCS có ô chọn trên từng dòng | Có ô chọn ở mỗi dòng + ô "chọn tất cả" ở hàng tiêu đề | ✅ Đạt |
| **C2** | Chọn ≥1 dòng `Tiếp nhận` → thanh hành động hàng loạt hiện, nút phân công dùng được | Tích 2 dòng → hiện thanh `Đã chọn 2 bản ghi` + nút **`Phân công hàng loạt (2)`** ở trạng thái **bấm được** (`disabled = false`) + nút `Bỏ chọn` | ✅ Đạt |
| **C3** 🔴 | Bấm nút → **mở bước chọn chuyên gia**, KHÔNG từ chối bằng thông báo *"chưa được hỗ trợ"* | Bấm nút → mở cửa sổ **"Phân công chuyên gia"** (cảnh báo SLA 2 ngày làm việc · ô chọn Chuyên gia bắt buộc · ô Ghi chú 0/500 · nút [Hủy] [Phân công]). **Quét toàn trang: chuỗi "chưa được hỗ trợ" KHÔNG xuất hiện.** Bộ bắt thông báo ghi **0 khung thông báo** trong 2,5s sau khi bấm | ✅ Đạt — **triệu chứng gốc không còn** |
| **C4** | Xác nhận xong → **TẤT CẢ** bản ghi được chọn đều được phân công | Sau khi tải lại danh sách **bằng địa chỉ**: **cả 2/2** hồ sơ đều có cột Chuyên gia = `Chuyên gia UAT QLNDTVVCG 38` và rời khỏi `Tiếp nhận`. Đối chứng máy chủ: **cả 2** `trangThai = PHAN_CONG`, **cùng** `chuyenGiaId 38383838-…-038`, `version 1 → 2` | ✅ Đạt |
| **C5** | Áp dụng **CÙNG MỘT** chuyên gia cho **TẤT CẢ** yêu cầu được chọn (một lần chọn) | **Hiện trạng: đúng như đối tác kỳ vọng.** Cửa sổ chỉ có **1 ô chọn chuyên gia + 1 ô ghi chú**, không có bảng nhập riêng từng hồ sơ. Một lời gọi duy nhất `POST /api/v1/noi-dung-tu-van-cs/phan-cong-hang-loat`. `ngayPhanCong` của 2 hồ sơ cách nhau **2 mili-giây** ⇒ một thao tác duy nhất, không phải 2 lần phân công lẻ | 🟡 **`GAP` — chỉ ghi nhận, KHÔNG chấm** |

### 3.1 Số liệu thô của bộ bắt thông báo

**Tự kiểm trước khi tin số liệu:** `soObserverDangSong = 1` ✔ (bắt buộc theo `tools/toast-capture.js`; khác 1 thì
số liệu vô hiệu). Bộ đo **không lọc trùng**, đọc bằng `innerText`, có mở rộng để bắt cả hộp thoại (vì bằng chứng
đối tác là hộp thoại chứ không phải toast).

| Mốc | Số lời gọi ghi | Số khung thông báo | Nội dung |
|---|---|---|---|
| Sau khi bấm **[Phân công hàng loạt (2)]** | **0** | **0** | — (chỉ mở cửa sổ, không gọi máy chủ, không thông báo) |
| Sau khi bấm **[Phân công]** trong cửa sổ | **1** — `POST /api/v1/noi-dung-tu-van-cs/phan-cong-hang-loat` | **1** | `Đã phân công chuyên gia cho 2 yêu cầu` |

⇒ **Không nhân đôi lời gọi, không nhân đôi thông báo.** Câu thông báo tự nó xác nhận phạm vi **2 yêu cầu**.

### 3.2 Ảnh

| Tệp | Bắt được gì |
|---|---|
| [`../image/QLNDTVVCG_38-01-thanh-hanh-dong-hang-loat-2-ban-ghi.png`](../image/QLNDTVVCG_38-01-thanh-hanh-dong-hang-loat-2-ban-ghi.png) | C1 + C2 — 2 dòng đã tích, thanh `Đã chọn 2 bản ghi` + nút `Phân công hàng loạt (2)` |
| [`../image/QLNDTVVCG_38-03-cua-so-phan-cong-chuyen-gia-mo-ra.png`](../image/QLNDTVVCG_38-03-cua-so-phan-cong-chuyen-gia-mo-ra.png) | **C3** — khung hình chụp **ngay sau khi bấm nút hàng loạt**: cửa sổ "Phân công chuyên gia" mở ra, phía sau vẫn thấy `Đã chọn 2 bản ghi` + `Phân công hàng loạt (2)`. **Đây là ảnh đối chiếu trực tiếp với ảnh của đối tác** |
| [`../image/QLNDTVVCG_38-04-ngay-sau-khi-bam-phan-cong.png`](../image/QLNDTVVCG_38-04-ngay-sau-khi-bam-phan-cong.png) | Ảnh phụ — chụp ngay sau khi xác nhận: cửa sổ đã đóng, thanh chọn đã biến mất, danh sách làm mới. **Không bắt được thông báo tự tắt** (nó chỉ sống ~3s); thông báo được ghi bằng bộ bắt ở §3.1 |
| [`../image/QLNDTVVCG_38-05-sau-tai-lai-ca-2-ho-so-da-co-chuyen-gia.png`](../image/QLNDTVVCG_38-05-sau-tai-lai-ca-2-ho-so-da-co-chuyen-gia.png) | **C4** — sau khi tải lại: cả 2 dòng `TVCS-QLND38-UAT-01/02` có chuyên gia và nhãn trạng thái đã đổi |

---

## 4. Đối chiếu với bằng chứng của đối tác

Tệp `../partner-evidence/QLNDTVVCG_38.jpg` **có trong repo** (đã mở xem được).
*(Chuẩn chấm §mở đầu ghi "không có trong repo" — viết trước khi khâu gom bằng chứng chép tệp về. Ghi nhận lại
cho đúng, không sửa file chuẩn chấm.)*

| | Ảnh đối tác (18/07/2026) | Lượt đo này (07/08/2026) |
|---|---|---|
| Địa chỉ | `htpldn-uat.ospgroup.vn/tv-chuyen-sau/danh-sach` | `18.143.165.120.nip.io/tv-chuyen-sau/danh-sach` |
| Chuỗi phiên bản chân sidebar | `HTPLDN · V1.0` | `HTPLDN · V1.0.9` |
| Tên các thẻ phân loại | `Tất cả` · `Mới tiếp nhận` · `Đang xử lý` · `Hoàn tất` | `Chờ xử lý` · `Đang tư vấn` · `Hoàn thành` |
| Đã chọn | 2 bản ghi lĩnh vực **Thuế** | 2 bản ghi lĩnh vực **Thương mại** |
| Bấm `Phân công hàng loạt (2)` | Hộp thoại **"Phân công hàng loạt chưa được hỗ trợ"** — *"Để đảm bảo CG khớp lĩnh vực của từng yêu cầu (srs-fr-12), vui lòng phân công từng row riêng lẻ."* — chỉ có nút `Đã hiểu` | Cửa sổ **"Phân công chuyên gia"** mở ra bình thường, phân công được cả 2 hồ sơ |

🔴 **Điểm cần nói thẳng:** lời từ chối trong ảnh đối tác **viện dẫn chính `srs-fr-12`** để biện minh cho việc
không hỗ trợ hàng loạt — nhưng `srs-fr-12-tv-chuyen-sau.md:1127` lại **quy định phải có** nút
`[Phân công CG hàng loạt]` cho bản ghi `TIEP_NHAN`, và yêu cầu này **có từ bản v3** (`srs-v3/srs-fr-12:886`).
Lý do "để CG khớp lĩnh vực từng yêu cầu" cũng không đứng vững vì `:178` chỉ buộc **kiểm** chuyên môn khớp lĩnh
vực, không cấm thao tác theo lô. **Bản đang chạy trên env nội bộ đã làm đúng đặc tả**, nên phần này coi như đã
xử lý; chỉ còn vế C5 cần BA chốt câu chữ.

---

## 5. Đối chứng độc lập — đúng MỘT đường (luật khóa 3)

**Đường đo 1 (giao diện):** danh sách → tích 2 dòng → bấm `Phân công hàng loạt (2)` → chọn CG → `Phân công` →
**tải lại danh sách bằng địa chỉ** → đọc lại cột Chuyên gia + nhãn trạng thái của **từng mã**.

**Đường đo 2 (đối chứng):** đọc lại chính 2 bản ghi đó **từ máy chủ, bằng chính phiên đăng nhập đó**, qua đường
dẫn **lấy từ lời gọi thật của màn danh sách** (`/api/v1/noi-dung-tu-van-cs`, tham số `search`) — không tự đoán:

| Mã | `trangThai` | `chuyenGiaId` | `chuyenGiaTen` | `ngayPhanCong` | `version` |
|---|---|---|---|---|---|
| `TVCS-QLND38-UAT-02` | `PHAN_CONG` | `38383838-…-038` | Chuyên gia UAT QLNDTVVCG 38 | `2026-08-06T19:38:14.429Z` | 2 |
| `TVCS-QLND38-UAT-01` | `PHAN_CONG` | `38383838-…-038` | Chuyên gia UAT QLNDTVVCG 38 | `2026-08-06T19:38:14.431Z` | 2 |

**Hai đường không mâu thuẫn** ⇒ chốt được C4. Không bấm lại nút lần hai (không tính là phương pháp thứ hai),
không mở đường đo thứ ba.

---

## 6. Đã chủ động tránh các bẫy nào

**FAIL oan:** cửa sổ chọn CG rỗng (§6.1.1 — đã kiểm trước, §2.2) · nút mờ do dòng không ở `Tiếp nhận`
(§6.1.2 — cả 2 dòng đều `TIEP_NHAN`) · lĩnh vực không khớp chuyên môn CG (§6.1.3 — cả 2 dòng **cùng** Thương mại,
CG chuyên môn **Luật thương mại**) · bản ghi khác đơn vị (§6.1.4 — cả 2 dòng cùng `donViId` với tài khoản) ·
hình thức cửa sổ (§6.1.5 — chấm bản chất, không chấm cửa sổ nổi hay ngăn kéo) · thiếu báo cáo lỗi từng bản
ghi / giới hạn 100 bản ghi (§6.1.6 — ngoài scope) · tưởng "mất dòng" (§6.1.7 — thẻ *Chờ xử lý* gộp
`TIEP_NHAN + PHAN_CONG` nên 2 dòng **vẫn nằm nguyên** đó, chỉ đổi nhãn).

**PASS oan:** không dừng ở "thấy nút" (§6.2.1 — đã bấm thật và chạy tới cùng) · không dừng ở thông báo thành công
(§6.2.2 — đã tải lại và đọc lại từng mã) · không chấp nhận "đúng một phần" (§6.2.3 — kiểm **2/2**) ·
không chọn 1 dòng rồi Pass (§6.2.4 — chọn đúng **2** dòng) · **không biến C5 thành `MATCH`** dù web làm đúng ý
đối tác (§6.2.5 — luật khóa 5) · không dùng `admin` (§6.2.6) · bộ bắt thông báo **không lọc trùng**, dùng
`innerText`, đã **tự kiểm số observer = 1** (§6.2.7) · đã tải lại bằng địa chỉ và ghi vân tay bản dựng (§6.2.8).

---

## 7. 🔴 Lỗi mới phát sinh — ngoài phạm vi dòng 288

**Nhãn trạng thái trên màn danh sách Tư vấn chuyên sâu không khớp bảng nhãn của đặc tả.**

Phát lộ ngay trong bước bắt buộc của vế C4 (phải đọc lại nhãn trạng thái của từng mã sau khi phân công).

Bảng nhãn đặc tả `srs-fr-12-tv-chuyen-sau.md:1130–1140` (*"Bảng nhãn trạng thái SM-TVCS"*, cột **Nhãn hiển thị**):

| Trạng thái | Nhãn theo đặc tả | Nhãn trên màn | |
|---|---|---|---|
| `TIEP_NHAN` | Tiếp nhận | Tiếp nhận | ✅ khớp |
| **`PHAN_CONG`** | **Đã phân công** (`:1135`) | **Phân công** | ❌ **lệch** |
| `DA_DUYET` | Đã duyệt | Đã duyệt | ✅ khớp |
| **`HUY`** | **Đã hủy** (`:1140`) | **Hủy** | ❌ **lệch** |

- Ảnh `PHAN_CONG`: [`../image/QLNDTVVCG_38-05-sau-tai-lai-ca-2-ho-so-da-co-chuyen-gia.png`](../image/QLNDTVVCG_38-05-sau-tai-lai-ca-2-ho-so-da-co-chuyen-gia.png)
- Ảnh `HUY`: [`../image/QLNDTVVCG_38-QA01-nhan-trang-thai-Huy-thay-vi-Da-huy.png`](../image/QLNDTVVCG_38-QA01-nhan-trang-thai-Huy-thay-vi-Da-huy.png)

**Không kéo verdict dòng 288**: vế của phiếu là *"áp dụng chuyên gia đã chọn cho tất cả yêu cầu được chọn"* —
kỳ vọng của đối tác **không nhắc câu chữ nhãn**, và bản chất chuyển trạng thái đã được máy chủ xác nhận
(`trangThai = PHAN_CONG`). Vì vậy đây là **dòng lỗi mới riêng**, ghi vào cuối bảng theo quy ước mã
`QLNDTVVCG_QA01`.

Chỉ khẳng định 2 trạng thái đã thực sự nhìn thấy trong các bước bắt buộc; **không mở rộng đi rà toàn bộ 7
trạng thái** (Flow 04 cấm mở rộng case để điều tra).

---

## 8. Câu hỏi BA cho vế `GAP` C5 — ghi nguyên văn

> `CẦN BA CONFIRM: đối tác kỳ vọng thao tác phân công hàng loạt áp dụng CÙNG MỘT chuyên gia đã chọn cho toàn bộ`
> `yêu cầu được chọn; SRS quy định có nút [Phân công CG hàng loạt] cho bản ghi Tiếp nhận nhưng KHÔNG quy định`
> `chọn chuyên gia chung hay chọn riêng từng bản ghi (srs-fr-12-tv-chuyen-sau.md:1127; khối Processing phân công`
> `:166-181 chỉ mô tả một bản ghi; module anh em srs-fr-04-chuyen-gia-tvv.md:1462 dùng khuôn nhập từng hồ sơ);`
> `web/dev hiện tại ĐANG LÀM ĐÚNG kỳ vọng đối tác — một ô chọn chuyên gia duy nhất, áp cho cả 2 hồ sơ trong`
> `một lời gọi.`

**Câu hỏi:** *Với phân công chuyên gia hàng loạt của Tư vấn chuyên sâu, cán bộ chọn **một** chuyên gia áp cho mọi
hồ sơ đã chọn, hay chọn chuyên gia **riêng cho từng hồ sơ** trong cùng một cửa sổ? Nếu là một chuyên gia chung
thì xử lý thế nào khi các hồ sơ đã chọn thuộc **lĩnh vực khác nhau**, trong khi bước 3 của khối Phân công
(`srs-fr-12:178`) buộc kiểm "chuyên môn phù hợp lĩnh vực"?*

> Lượt đo này **cố ý chọn 2 hồ sơ cùng lĩnh vực** để không lẫn với bẫy FAIL oan §6.1.3, nên **chưa** có dữ kiện
> về tình huống lĩnh vực khác nhau. Đó chính là phần BA cần chốt trước khi đặc tả bổ sung.

---

## 9. Giới hạn hiệu lực của verdict

1. **Chỉ có hiệu lực cho env nội bộ `18.143.165.120.nip.io` + bó mã `index-D4Buvu4S.js`.** Đối tác đo trên
   `htpldn-uat.ospgroup.vn` với bản dựng cũ hơn (`V1.0`, tên thẻ phân loại khác hẳn).
2. **Không có ảnh "lỗi cũ" do chính bên kiểm thử chụp** ⇒ chỉ kết luận được **hiện trạng đúng so với đặc tả**,
   không kết luận được "bản sửa có tác dụng". Ảnh của đối tác chứng minh triệu chứng **từng tồn tại trên env
   của họ**, không chứng minh được nó từng tồn tại trên env nội bộ.
3. **Chỉ đo với 2 hồ sơ cùng lĩnh vực, cùng đơn vị.** Chưa đo: chọn hồ sơ khác lĩnh vực · chọn lẫn dòng khác
   trạng thái · chọn dòng khác đơn vị · số lượng lớn. Tất cả đều nằm ngoài vế `Cn` (chuẩn chấm §3).
