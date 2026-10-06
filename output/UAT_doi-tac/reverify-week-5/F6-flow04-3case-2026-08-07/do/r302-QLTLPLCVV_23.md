# Dòng 302 · `QLTLPLCVV_23` — "Tìm kiếm hỗ trợ tiếng Việt không dấu."

**Verdict logic Flow 04: `Cần BA`** → ô `Trạng thái dev fix` = **`BA confirm`**

| Hạng mục | Giá trị |
|---|---|
| Ngày đo | 2026-08-07 (02:15 giờ VN) — cùng phiên, cùng vai trò với dòng 301 |
| Env · bản dựng | `https://18.143.165.120.nip.io` (nội bộ) · **`HTPLDN · V1.0.9`** · etag `W/"6a74c6ea-428"` · bó mã `assets/index-B2W2Krcs.js` |
| Tài khoản | `cbnv_tw_05` / `Test@1234` — `CB_NV_TW`, cấp TW |
| Bản ghi tiền đề | `TVCS-20260806-0003` (`eb16294e-…`) — **dùng lại nguyên tiền đề của dòng 301, không seed thêm** |

---

## 1. Scope Lock

| Vế | Nội dung expected | Quan hệ SRS | Route |
|---|---|---|---|
| **C1** | Nhóm tư liệu của màn chi tiết TVCS **có phương tiện nhập từ khóa và/hoặc bộ lọc** | **GAP** | BA — cấm Pass |
| **C2** | Nhập **từ khóa tiếng Việt KHÔNG DẤU** của tư liệu có tên viết **có dấu** ⇒ **vẫn hiển thị danh sách kết quả** | **MATCH** (`srs-fr-12-tv-chuyen-sau.md:948`) | TEST |

> 🔴 Hai dòng 301/302 dùng **chung một ảnh bằng chứng** (md5 `3d926926a8bbdfd3352f9328d55c1c39`) ⇒ ảnh không phân biệt
> được vế có dấu với không dấu. Đã **đo riêng** vế C2 của dòng này bằng một lượt gõ khác, **không suy từ dòng 301**.
> Riêng C1 là quan sát trên **cùng một màn** nên dùng chung số đo (Flow 04 §BUG SCOPE LOCK luật 3 — không lặp thao
> tác chỉ để "chắc"), nhưng kết quả được ghi riêng cho dòng này.

---

## 2. Phép đo C2 — từ khóa KHÔNG DẤU

| Bước | Đo được |
|---|---|
| Bấm `[Xóa bộ lọc]` để về mốc gốc | ô từ khóa rỗng · bảng **2** dòng |
| Gõ **`Nghi dinh`** (bỏ dấu hoàn toàn) → bấm `[Tìm kiếm]` | bảng còn **1** dòng |
| Dòng còn lại | **`Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa`** — tên bản ghi viết **CÓ DẤU** |
| Dòng bị loại | `QA B7 QLTLPLCVV_17 - tu lieu kiem thu xem tep 3 dinh dang` |

**Đối chứng độc lập** — response của chính lượt tìm đó:

```
GET /api/v1/tu-lieu-phap-ly-vvs?noiDungTvId=eb16294e-…&pageSize=100&search=Nghi+dinh  → 200
meta = {"page":1,"pageSize":100,"total":1,"totalPages":1}
data[0].id = 0d258d7c-9498-48b3-982d-db85a13cdb96
data[0].tenTuLieu = "Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa"
```

**So tập ID với lượt CÓ DẤU của dòng 301** (đúng phép đối chứng đã khóa ở Giai đoạn A):

| Lượt | `total` | tập `id` |
|---|---:|---|
| `search=Nghị định` (có dấu) | 1 | `0d258d7c-9498-48b3-982d-db85a13cdb96` |
| `search=Nghi dinh` (không dấu) | 1 | `0d258d7c-9498-48b3-982d-db85a13cdb96` |

⇒ **Hai tập ID trùng khít, không rỗng.** UI 1 dòng = máy chủ `total` 1 ở cả hai lượt ⇒ **C2 ĐẠT** — bỏ dấu vẫn ra
đúng bản ghi có dấu, đúng `srs-fr-12-tv-chuyen-sau.md:948` *"Full-text search trên ten_tu_lieu + mo_ta (hỗ trợ tiếng
Việt unaccent)"*.

Response lưu tại [`do/r302-C2-khongdau-search-response.network-response`](r302-C2-khongdau-search-response.network-response).

Ảnh: [`image/r302-C2-tukhoa-khong-dau-Nghi-dinh-van-ra-ban-ghi-co-dau-V109.png`](../image/r302-C2-tukhoa-khong-dau-Nghi-dinh-van-ra-ban-ghi-co-dau-V109.png)
→ Drive: https://drive.google.com/file/d/1PPH3XpTzzzcdmkT5ZYICy0PSgIxuq18i/view?usp=drivesdk

**Vì sao chọn cụm 2 từ `Nghi dinh`, không dùng 1 từ:** bỏ dấu của `nghị` là `nghi`, trùng tiền tố của `nghiệp`
(`nghiep`) ⇒ tìm 1 từ sẽ mất khả năng phân biệt. Cụm 2 từ giữ được sức chứng minh.

## 3. Phép đo C1 (dùng chung quan sát với dòng 301, ghi kết quả riêng cho dòng 302)

Trong đúng khung accordion **"Tư liệu pháp lý liên kết"**: **4** ô nhập/chọn — 1 ô từ khóa (placeholder
`Tìm theo tên hoặc mô tả tư liệu`) + 3 dropdown `Loại tư liệu` · `Lĩnh vực` · `Trạng thái`; nút `[Tìm kiếm]`,
`[Xóa bộ lọc]`, `[Thêm tư liệu]`; bảng đủ **9** cột. ⇒ **Web hiện tại ĐÚNG kỳ vọng đối tác.**

Ảnh: → Drive https://drive.google.com/file/d/1KGFgkn36R1FI1bBLr1cp84WUShXqe1tr/view?usp=drivesdk

---

## 4. Chốt verdict

| Vế | Quan hệ | Kết quả đo | Ảnh hưởng verdict |
|---|---|---|---|
| C1 | `GAP` | web **có đủ** — đúng kỳ vọng đối tác | **Cấm Pass** (luật khóa 5); câu hỏi BA nhằm **bổ sung vào đặc tả** |
| C2 | `MATCH` | **ĐẠT** — bỏ dấu ra đúng bản ghi có dấu, 2 lượt trùng tập ID | Không kéo về Reopen |

**⇒ Verdict logic: `Cần BA`.**

**Giới hạn hiệu lực:** chỉ đúng cho env nội bộ bản dựng **V1.0.9** tại thời điểm đo. Ảnh đối tác chụp trên
`htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0`, ở đó nhóm tư liệu chưa có thanh lọc.

**Không kết luận "fix đã có tác dụng"** — QA không có ảnh "lỗi cũ" tự chụp trên cùng env.

---

## 5. CẦN BA CONFIRM

### 5.1 Câu hỏi chính (vế C1 — giống dòng 301)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu có ô nhập
> từ khóa và/hoặc bộ lọc để người dùng tìm tư liệu ngay tại đó**; SRS quy định **chức năng tìm kiếm tư liệu là yêu cầu
> bắt buộc của FR-X.1-06 (`srs-fr-12-tv-chuyen-sau.md:942–951`) và màn duy nhất chứa FR-X.1-06 chính là nhóm này
> (`:828`, `:1153`, `:1227–1229`), NHƯNG Thành phần màn hình của SCR-X1-02 chỉ khai bảng dữ liệu + nút [+ Thêm tư liệu]
> (`:1171`, `:1198`), và FR-X.1-06 không có tiêu chí chấp nhận nào cho tìm kiếm (`:986–996`)**; web/dev hiện tại
> **đã có đủ ô tìm kiếm + 3 bộ lọc + nút [Tìm kiếm] [Xóa bộ lọc] và chạy đúng**.
>
> **Đề nghị BA chốt:** bổ sung thành phần này vào SCR-X1-02 §Thành phần màn hình + bổ sung tiêu chí chấp nhận cho
> FR-X.1-06. *(Mục đích: bổ sung vào đặc tả — KHÔNG chặn bàn giao.)*

### 5.2 Câu hỏi phụ — riêng dòng này (độ lệch phạm vi BR-DATA-08)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **tìm kiếm tư liệu bằng từ khóa tiếng Việt không dấu vẫn ra bản ghi có tên viết
> có dấu**; SRS quy định **hai chỗ lệch nhau — bước xử lý của chính FR-X.1-06 ghi *"Full-text search trên ten_tu_lieu
> + mo_ta (hỗ trợ tiếng Việt unaccent)"* (`srs-fr-12-tv-chuyen-sau.md:948`), trong khi BR-DATA-08 ở bản gốc file chính
> **không nhắc chữ unaccent** và chỉ áp cho FR-II-02 / FR-X.1-02 / FR-X.2-04, phần Ngoại lệ ghi *"Các entity khác:
> search by tìm kiếm theo từ khóa"* (`srs-v3.5.md:5572`); hai bảng tham chiếu trong FR-12 cũng chỉ gán BR-DATA-08 cho
> FR-X.1-02 (`:1579`, `:1635`)**; web/dev hiện tại **đã hỗ trợ không dấu — gõ `Nghi dinh` ra đúng bản ghi
> `Nghị định 55/2019…`, tập ID trùng với lượt gõ có dấu**.
>
> **Đề nghị BA chốt:** tìm kiếm tư liệu pháp lý (FR-X.1-06) có bắt buộc hỗ trợ tiếng Việt không dấu hay không, và đồng
> bộ lại phạm vi BR-DATA-08 giữa file chính với bản trích ở FR-12.
>
> *(Chuẩn chấm vòng này vẫn lấy `:948`. Câu hỏi chỉ nhằm dọn mâu thuẫn tài liệu, KHÔNG đổi quan hệ đã khóa.)*

---

## 6. Cổng chốt verdict

| # | Câu hỏi cổng | Trả lời |
|---|---|---|
| 1 | Neo dòng SRS nào? | C1 → `:942–951` + `:828`/`:1153`/`:1227–1229` đối chiếu `:1171`/`:1198`/`:986–996`. C2 → `:948`. |
| 2 | Thao tác có ánh xạ vế Cn? | Có — 2 thao tác: `[Xóa bộ lọc]` (lập lại mốc gốc cho C2) và gõ không dấu + đọc response (C2). C1 dùng lại quan sát cùng màn, không lặp. |
| 3 | Vế `GAP` chặn Pass + có câu hỏi BA? | Rồi — §5.1. Vế `MATCH` C2 kèm câu hỏi phụ §5.2 nhưng **không** đổi quan hệ. |
| 4 | Đã đọc đủ expected + phản hồi? | Rồi — Mô tả, Điều kiện, 4 bước, KQ mong đợi, `Trạng thái` Fail, `TKM phản hồi lần 1` = *"Màn hình không có chức năng"*, `Trạng thái dev fix` = `Fixed`, `DEV phản hồi lần 1` trống. |
| 5 | Điều kiện đo khớp tiền đề case? | Vai trò + màn khớp. Khác env/bản dựng — đã ghi giới hạn hiệu lực §4. |
