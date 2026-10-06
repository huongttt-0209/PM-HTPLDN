# Dòng 301 · `QLTLPLCVV_22` — "Tìm kiếm tư liệu hỗ trợ tiếng Việt có dấu"

**Verdict logic Flow 04: `Cần BA`** → ô `Trạng thái dev fix` = **`BA confirm`**

| Hạng mục | Giá trị |
|---|---|
| Ngày đo | 2026-08-07 (02:10 giờ VN) |
| Env | `https://18.143.165.120.nip.io` — env **NỘI BỘ** |
| Bản dựng đo được | **`HTPLDN · V1.0.9`** (chuỗi ở chân sidebar) · `GET /` etag `W/"6a74c6ea-428"` · last-modified `Thu, 06 Aug 2026 17:39:54 GMT` · bó mã `assets/index-B2W2Krcs.js` |
| Tài khoản | `cbnv_tw_05` / `Test@1234` — `CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW` (khớp vai trò `Cán bộ NV Trung ương` trong ảnh đối tác và Tác nhân SRS `:833`) |
| Bản ghi tiền đề | TVCS **`TVCS-20260806-0003`** — `id eb16294e-6231-45ce-9c50-fe480228f518`, trạng thái *Tiếp nhận*, đơn vị TW |
| Màn | Tư vấn → Tư vấn chuyên sâu → chi tiết → accordion **"Tư liệu pháp lý liên kết"** |

> 🔴 **Đính chính vân tay bản dựng so với lô trước:** lô `F5-flow04-2026-08-07` ghi bản dựng là *V1.0.10* (suy từ ghi chú lô khác).
> Chuỗi phiên bản **thực đọc trên màn** của cùng etag/bó mã này là **V1.0.9**. Báo cáo dùng số đo được, không dùng số suy.

---

## 1. Scope Lock (chốt ở Giai đoạn A, KHÔNG đổi sau khi mở màn)

Nguồn: [`chuan/QLTLPLCVV-301-302.md`](../chuan/QLTLPLCVV-301-302.md)

| Vế | Nội dung expected | Quan hệ SRS | Route |
|---|---|---|---|
| **C1** | Trong nhóm "Tư liệu pháp lý liên kết" của màn chi tiết TVCS, NSD **có phương tiện nhập từ khóa và/hoặc chọn bộ lọc** | **GAP** | BA — cấm Pass |
| **C2** | Nhập **từ khóa tiếng Việt CÓ DẤU** khớp tư liệu đang có ⇒ **hiển thị danh sách kết quả** | **MATCH** | TEST |

---

## 2. Tiền đề đã chuẩn bị — KHAI BÁO MUTATION

**Trước khi đo:** nhóm tư liệu của `TVCS-20260806-0003` chỉ có **1** bản ghi
(`QA B7 QLTLPLCVV_17 - tu lieu kiem thu xem tep 3 dinh dang`, loại *Tài liệu*, *Đã công khai*) — không có bản ghi nào
mang dấu tiếng Việt để phân biệt được có dấu / không dấu ⇒ chưa đo được C2.

**Đã thêm đúng 1 bản ghi** (dùng chính nút `[Thêm tư liệu]` của section, không đoán endpoint, không ghi thẳng DB):

| Trường | Giá trị |
|---|---|
| Tên tư liệu | `Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa` |
| Loại tư liệu | `Văn bản pháp luật` |
| Lĩnh vực / Mô tả / File | để trống (không thuộc vế đang chấm) |
| Trạng thái | `Nháp` (mặc định, SRS `:850`) |
| `id` sinh ra | `0d258d7c-9498-48b3-982d-db85a13cdb96` |
| Request | `POST /api/v1/tu-lieu-phap-ly-vvs` → **201** (reqid 177) |

**Khai đầy đủ theo Flow 04 §Giai đoạn B bước 4:** đổi bản ghi `TVCS-20260806-0003` · thêm **1** tư liệu · trên env
**nội bộ** `18.143.165.120.nip.io`. Không đụng dữ liệu đối tác. Bản ghi cũ giữ nguyên, dùng làm mẫu-phải-bị-loại.

Chỉ tạo **1** bản ghi (không tạo TL-B/TL-C như bản chuẩn dự phòng) vì đã đủ chứng minh tìm kiếm **thu hẹp** kết quả:
2 dòng → 1 dòng. Bản ghi cũ không chứa chuỗi `nghi dinh` sau khi bỏ dấu nên đóng đúng vai mẫu-phải-bị-loại.

---

## 3. Phép đo

### 3.1 C1 — có / không có phương tiện tìm kiếm trong section (đo 1 lần, dùng chung cho dòng 302)

Đếm control **nằm trong container của accordion** (không dump DOM, chỉ trả count + placeholder):

| Đo được | Giá trị |
|---|---|
| Số ô nhập/chọn trong section | **4** |
| Ô nhập từ khóa | `input[type=text]` · placeholder **`Tìm theo tên hoặc mô tả tư liệu`** |
| 3 dropdown | **`Loại tư liệu`** · **`Lĩnh vực`** · **`Trạng thái`** |
| Nút trong thanh lọc | **`Tìm kiếm`** · **`Xóa bộ lọc`** (ngoài ra có `Thêm tư liệu`) |
| Số cột bảng | **9** — `Tên tư liệu · Loại · Lĩnh vực · File · Trạng thái · Công khai lúc · Người tạo · Ngày tạo · Hành động` |

⇒ **Web hiện tại ĐÚNG kỳ vọng đối tác** ở vế C1, và bộ tiêu chí nhận vào (từ khóa · loại · lĩnh vực · trạng thái)
trùng khít với `srs-fr-12-tv-chuyen-sau.md:947`.

Ảnh: [`image/QLTLPLCVV-C1-section-co-o-tim-kiem-va-3-bo-loc-V109.png`](../image/QLTLPLCVV-C1-section-co-o-tim-kiem-va-3-bo-loc-V109.png)
→ Drive: https://drive.google.com/file/d/1KGFgkn36R1FI1bBLr1cp84WUShXqe1tr/view?usp=drivesdk

### 3.2 C2 — từ khóa tiếng Việt CÓ DẤU

| Bước | Đo được |
|---|---|
| Trước khi tìm | bảng **2** dòng |
| Gõ `Nghị định` (có dấu) vào ô tìm kiếm → bấm `[Tìm kiếm]` | bảng còn **1** dòng |
| Dòng còn lại | `Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa` |
| Dòng bị loại | `QA B7 QLTLPLCVV_17 - tu lieu kiem thu xem tep 3 dinh dang` |

**Đối chứng độc lập** (đường thứ hai, không phải bấm lại nút) — request do chính lượt tìm sinh ra, endpoint lấy từ
`list_network_requests` chứ không đoán:

```
GET /api/v1/tu-lieu-phap-ly-vvs?noiDungTvId=eb16294e-…&pageSize=100&search=Ngh%E1%BB%8B+%C4%91%E1%BB%8Bnh  → 200
meta = {"page":1,"pageSize":100,"total":1,"totalPages":1}
data[0].id = 0d258d7c-9498-48b3-982d-db85a13cdb96
data[0].tenTuLieu = "Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa"
```

Response lưu tại [`do/r301-C2-codau-search-response.network-response`](r301-C2-codau-search-response.network-response).

⇒ **UI 1 dòng = máy chủ `total` 1, cùng 1 mã bản ghi.** Hai đường khớp nhau ⇒ **C2 ĐẠT**, không mở đường thứ ba.

Ảnh: [`image/r301-C2-tukhoa-co-dau-Nghi-dinh-ra-1-ket-qua-V109.png`](../image/r301-C2-tukhoa-co-dau-Nghi-dinh-ra-1-ket-qua-V109.png)
→ Drive: https://drive.google.com/file/d/1Q2Y31zRZ55NZ_85fCf5s3f07jK0jEG70/view?usp=drivesdk

---

## 4. Chốt verdict

| Vế | Quan hệ | Kết quả đo | Ảnh hưởng verdict |
|---|---|---|---|
| C1 | `GAP` | web **có đủ** ô tìm kiếm + 3 bộ lọc — đúng kỳ vọng đối tác | **Cấm Pass** (luật khóa 5). Câu hỏi BA nhằm **bổ sung vào đặc tả**, KHÔNG phải chặn bàn giao |
| C2 | `MATCH` | **ĐẠT** — 2 dòng → 1 dòng đúng bản ghi, máy chủ `total=1` khớp | Không kéo về Reopen |

**⇒ Verdict logic: `Cần BA`.** Không vế `MATCH` nào sai ⇒ **không** Reopen.

**Giới hạn hiệu lực:** verdict chỉ đúng cho env nội bộ `18.143.165.120.nip.io` bản dựng **V1.0.9** tại thời điểm đo.
Đối tác chụp ảnh trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0` — ảnh đó cho thấy nhóm tư liệu
**không có** thanh lọc và bảng chỉ **7** cột (thiếu *Người tạo*, *Ngày tạo*). Tức hai bản dựng khác nhau thật; verdict
này không tuyên bố gì cho bản trên env đối tác.

**Không kết luận "fix đã có tác dụng":** QA không có ảnh "lỗi cũ" do chính mình chụp trên cùng env ⇒ chỉ kết luận được
**hiện trạng đúng/sai so với đặc tả**, đúng Flow 04 §Ca biên.

---

## 5. CẦN BA CONFIRM

> **CẦN BA CONFIRM:** đối tác kỳ vọng **nhóm "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu có ô nhập
> từ khóa và/hoặc bộ lọc để người dùng tìm tư liệu ngay tại đó**; SRS quy định **chức năng tìm kiếm tư liệu là yêu cầu
> bắt buộc của FR-X.1-06 — nhận từ khóa theo tên tư liệu + mô tả, lĩnh vực, loại tư liệu, trạng thái, AND logic, phân
> trang (`srs-fr-12-tv-chuyen-sau.md:942–951`) — và màn duy nhất chứa FR-X.1-06 chính là nhóm này (`:828`, `:1153`,
> `:1227–1229`, do SCR-X1-07 đã bị gộp vào), NHƯNG phần Thành phần màn hình của SCR-X1-02 chỉ khai cho nhóm này một
> bảng dữ liệu và nút [+ Thêm tư liệu], không khai ô tìm kiếm hay bộ lọc nào (`:1171`, `:1198`), và FR-X.1-06 không có
> tiêu chí chấp nhận nào cho tìm kiếm (`:986–996`)**; web/dev hiện tại **đã có đủ ô nhập từ khóa (gợi ý "Tìm theo tên
> hoặc mô tả tư liệu") + 3 bộ lọc Loại tư liệu / Lĩnh vực / Trạng thái + nút [Tìm kiếm] và [Xóa bộ lọc], chạy đúng —
> tức đang làm đúng kỳ vọng đối tác**.
>
> **Đề nghị BA chốt:** bổ sung thành phần tìm kiếm/lọc này vào SCR-X1-02 §Thành phần màn hình (nêu rõ tìm theo trường
> nào, có mấy bộ lọc) và bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06, để đặc tả khớp với sản phẩm đang chạy.
>
> *(Mục đích: bổ sung vào đặc tả — KHÔNG phải chặn bàn giao. Sản phẩm hiện đang đáp ứng kỳ vọng.)*

---

## 6. Ghi nhận ngoài phạm vi (candidate, KHÔNG điều tra trong case này)

- Tiêu đề nhóm trên env nội bộ là **"Tư liệu pháp lý liên kết"**, khớp SRS `:1171`; ảnh đối tác (bản V1.0) ghi
  **"Tư liệu pháp luật"**. Không thuộc vế nào của phiếu ⇒ chỉ ghi nhận.
- Bảng trên env nội bộ đủ **9** cột đúng `:1171`; ảnh đối tác chỉ **7** cột (thiếu *Người tạo*, *Ngày tạo*). Đây là
  chênh lệch giữa hai bản dựng, không phải lỗi quan sát được trên bản đang đo ⇒ **không log bug**.

## 7. Cổng chốt verdict

| # | Câu hỏi cổng | Trả lời |
|---|---|---|
| 1 | Mỗi vế neo dòng SRS nào? | C1 → `:942–951` + `:828`/`:1153`/`:1227–1229` đối chiếu `:1171`/`:1198`/`:986–996`. C2 → `:947`, `:950`, `:951`, `:946`. |
| 2 | Mọi thao tác có ánh xạ về vế Cn? | Có — 3 thao tác: mở accordion (C1), thêm 1 tư liệu (tiền đề C2), gõ từ khóa có dấu + đọc response (C2). Không thao tác thừa. |
| 3 | Vế `GAP` đã bị chặn Pass + có câu hỏi BA? | Rồi — §5. |
| 4 | Đã đọc đủ expected + phản hồi? | Rồi — Mô tả, Điều kiện, 4 bước, KQ mong đợi, `Trạng thái` Fail, `TKM phản hồi lần 1` = *"Màn hình không có chức năng"*, `Trạng thái dev fix` = `Fixed`, `DEV phản hồi lần 1` trống. |
| 5 | Điều kiện đo khớp tiền đề case? | Vai trò khớp (`CB_NV_TW`), màn khớp. Khác: env + bản dựng (đã ghi giới hạn hiệu lực §4) và bản ghi tư liệu là dữ liệu QA (ảnh đối tác không cho biết tư liệu của họ). |
