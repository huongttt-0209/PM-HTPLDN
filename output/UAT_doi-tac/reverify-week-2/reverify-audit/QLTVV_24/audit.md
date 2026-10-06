# Audit verify vòng 2 — QLTVV_24

| Mục | Nội dung |
|---|---|
| **Mã ca kiểm thử** | QLTVV_24 (dòng 47, tab `UAT_TGPL Doanh Nghiệp-tuần 2`) |
| **Mô tả ca** | Sửa — Dữ liệu hợp lệ |
| **Phản ánh vòng 2 của đối tác** | "Khi nhấn Xóa file ảnh chân dung đính kèm, hệ thống hiển thị thông báo 'Lỗi hệ thống. Vui lòng thử lại sau'" |
| **Bằng chứng đối tác** | `QLTVV_22_v2.jpg` (số hiệu tệp lệch một bậc — đối chiếu theo nội dung) |
| **Môi trường QA kiểm lại** | https://18.143.165.120.nip.io — tài khoản `cbnv_tw` (CB_NV_TW, Cục Bổ trợ tư pháp – Bộ Tư pháp) |
| **Thời điểm** | 2026-07-27 15:00–15:10 |
| **Bảng đối chiếu điều kiện** | [`../../cond/QLTVV_24-r2.md`](../../cond/QLTVV_24-r2.md) — **0 GAP** |
| **Kết luận** | **Open** — tái hiện 100%, đã cô lập được điều kiện gây lỗi |

---

## Cổng 1 — Bằng chứng đọc được gì

Ảnh `QLTVV_22_v2.jpg` (full-res) cho đủ 5 dữ kiện cần để dựng lại tình huống:

| Dữ kiện | Giá trị đọc từ ảnh |
|---|---|
| Màn hình | `/chuyen-gia-tvv/d973a0e6-e63b-4499-b7a2-ea4bcf5c4e06/chinh-sua` — Chỉnh sửa hồ sơ tư vấn viên |
| Vai trò | "BTP · TW" · "Cán bộ NV Trung ương" · `CB_NV_TW` |
| Bản ghi | `TVV-BTP-TW-0059` — Hoàng Thị Thanh Thảo, Loại "Tư vấn viên (TVV)" |
| Trạng thái tệp ảnh | Dòng tệp **"Ảnh chân dung — Xem — Xóa"** hiện sẵn khi mở màn sửa + ô xem trước có ảnh ⇒ ảnh **đã lưu vào hồ sơ từ trước**, không phải tệp vừa chọn chưa lưu |
| Kết quả | Hộp thông báo đỏ **"Lỗi hệ thống, vui lòng thử lại sau"** |

Ảnh **không** cho biết mã trả về của lời gọi máy chủ — QA tự đo phần này ở Cổng 2.

## Cổng 2 — Hiểu đúng bug đối tác báo

Đối tác báo **một** ý: thao tác **xóa ảnh chân dung đã lưu** trên màn sửa hồ sơ bị hệ thống từ chối bằng thông báo lỗi hệ thống chung.

Không phải "không tải được ảnh lên", không phải "lưu hồ sơ thất bại" — hai việc đó chạy bình thường trong chính ảnh của đối tác (ảnh đã nằm trong hồ sơ và có xem trước).

## Cổng 3 — Đối chiếu đặc tả

| # | Điểm đối chiếu | Đặc tả (`Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`) | Bản đang chạy | Đánh giá |
|---|---|---|---|---|
| 1 | Ảnh chân dung là trường **không bắt buộc** | `:136` — bảng Inputs, dòng 2: `anh_chan_dung \| structured \| **Bắt buộc = N** \| Max 5MB, .jpg/.png \| Mặc định "Ảnh hệ thống"` | Không thể đưa hồ sơ về trạng thái không có ảnh chân dung: mọi lần bấm Xóa đều bị chặn bằng lỗi hệ thống | **Sai** — trường không bắt buộc nhưng người dùng bị khóa cứng ở giá trị đã nhập |
| 2 | Màn sửa hồ sơ phải cho quản lý ảnh chân dung | `:1486` — SCR-IV-02, nhóm 1 mục 2.3: "Ảnh chân dung \| tải ảnh \| Tối đa 5MB, định dạng .jpg / .png; hiển thị xem trước 120x160" | Vùng kéo thả và dòng tệp có đủ, riêng thao tác gỡ tệp trả lỗi hệ thống | **Sai** — luồng hợp lệ bị hệ thống chặn |
| 3 | Thông báo lỗi phải nói đúng bản chất | `:198-199` (bảng lỗi FR-IV-03: `ERR-TVV-01` "Họ tên là bắt buộc", `ERR-TVV-02` "Số Căn cước công dân đã tồn tại") và `:1487`, `:1490` (SCR-IV-02) — đặc tả luôn gắn thông báo nghiệp vụ cụ thể cho từng tình huống lỗi | Thông báo trả về là câu lỗi hệ thống chung "Lỗi hệ thống, vui lòng thử lại sau" (mã `ERR-SYS-00-00-01`, HTTP 500) | **Sai** — lỗi không được xử lý, người dùng không biết phải làm gì |

**Kết luận Cổng 3:** thao tác đối tác thực hiện là thao tác hợp lệ trên một trường đặc tả ghi rõ **không bắt buộc**; hệ thống chặn bằng lỗi hệ thống chưa xử lý ⇒ **Open**.

---

## Các phép đo

Tất cả phép đo đọc lại trạng thái hồ sơ **ngay trước và ngay sau** mỗi thao tác.

### Đo 1 — Dựng lại đúng tình huống của đối tác qua giao diện

| Bước | Thao tác | Kết quả đo |
|---|---|---|
| 1 | Mở `/chuyen-gia-tvv/de22ef5c-…/chinh-sua` (`TVV-BTP-TW-0020`, cùng đơn vị) | Khối "Ảnh chân dung" trống |
| 2 | Chọn tệp ảnh `qa-anh-dai-dien.png` (7,7 KB, .png) → bấm **Lưu** | Tải tệp lên: **201**; cập nhật hồ sơ: **200**; thông báo "Cập nhật hồ sơ TVV thành công" |
| 3 | Tải lại màn sửa | Dòng tệp hiện đúng như ảnh đối tác: `Ảnh chân dung \| Xem \| Xóa` |
| 4 | Đọc dữ liệu hồ sơ ngay trước khi bấm Xóa | `anhChanDungFileId = c100d6bf-f6dd-4dc0-98e1-5de545e2778e` (khác rỗng) |
| 5 | Bấm **Xóa** trên dòng ảnh chân dung | Lời gọi xóa trả **500**; thông báo đỏ **"Lỗi hệ thống, vui lòng thử lại sau"**; dòng tệp **vẫn còn** |

Nội dung máy chủ trả về ở bước 5:

```
DELETE /api/v1/tu-van-viens/de22ef5c-5358-418a-a0e4-ca4d06c37393/files/c100d6bf-f6dd-4dc0-98e1-5de545e2778e
→ 500
{"success":false,"error":{"code":"ERR-SYS-00-00-01",
 "message":"Lỗi hệ thống, vui lòng thử lại sau",
 "requestId":"5ae22e43-bab8-4b72-8701-7658248e14c8"}}
```

Bộ bắt thông báo cài trước khi bấm (không lọc trùng, chỉ đọc chữ hiển thị): ghi nhận 2 khung `Lỗi hệ thống, vui lòng thử lại sau`; số hộp thông báo **cùng tồn tại** tại mọi thời điểm lấy mẫu (120 ms/lần) **tối đa = 1** ⇒ chỉ có **một** hộp thông báo thật, không phải lỗi hiện thông báo trùng. Số bộ bắt đang sống = 1.

### Đo 2 — Kiểm lại bằng cách khác (gọi thẳng máy chủ, không qua giao diện)

Lặp 2 lần liên tiếp trên cùng bản ghi:

```
DELETE …/files/c100d6bf-…  (lần 1) → 500  ERR-SYS-00-00-01
DELETE …/files/c100d6bf-…  (lần 2) → 500  ERR-SYS-00-00-01
```

⇒ Lỗi **cố định**, không phải trục trặc nhất thời.

### Đo 3 — Phép thử đối chứng: điều kiện nào gây lỗi?

Làm trên **bản ghi thứ hai độc lập** `TVV-BTP-TW-0018` (`cb90a345-…`), cùng một tệp ảnh, chỉ đổi **một** biến duy nhất là "ảnh đã được gắn vào hồ sơ hay chưa":

| Lần | Tình huống | Kết quả xóa |
|---|---|---|
| A | Tải ảnh lên, **chưa** gắn vào hồ sơ (`anhChanDungFileId` rỗng) | **204 — xóa thành công** |
| B | Tải ảnh lên, **đã** gắn vào hồ sơ (`anhChanDungFileId = ce747e72-…`) | **500 — Lỗi hệ thống** |
| C | Vẫn tệp ở lần B, gỡ liên kết khỏi hồ sơ trước (`anhChanDungFileId → rỗng`) rồi xóa | **204 — xóa thành công** |

⇒ Điều kiện gây lỗi được cô lập: **ảnh còn đang được hồ sơ tham chiếu**. Đây đúng là tình huống của mọi người dùng thật, vì ảnh chỉ hiện nút "Xóa" sau khi đã lưu vào hồ sơ.

### Đo 4 — Cùng thao tác, nhưng với tệp đính kèm loại khác

Trên cùng bản ghi `TVV-BTP-TW-0020`, bấm "Xóa" dòng tệp PDF đính kèm (`qa-tep-dinh-kem.pdf`):

```
DELETE …/files/15d7f4ce-… → 422
{"code":"ERR-VAL-FILE-08","message":"Tệp đang được tham chiếu bởi bản ghi khác, không thể xoá"}
```

⇒ Với tệp đính kèm, cùng tình huống "tệp đang được tham chiếu" được **xử lý tử tế**: trả về thông báo nghiệp vụ đọc hiểu được. Riêng nhánh ảnh chân dung **không có nhánh xử lý này** nên rơi thẳng vào lỗi hệ thống. Đây là lý do đưa mức độ về **Major** chứ không phải Critical: chức năng còn lại của màn sửa vẫn chạy, nhưng người dùng mất hẳn khả năng gỡ ảnh và nhận thông báo không nói lên điều gì.

### Đo 5 — Quan sát kèm theo (ngoài phạm vi ý đối tác báo)

Sau khi lưu ảnh thành công, mở màn **chi tiết** `/chuyen-gia-tvv/de22ef5c-…`:

- Thẻ thông tin chính chỉ hiện chữ cái đầu của họ tên ("Q"), **không** hiện ảnh chân dung đã lưu.
- Dữ liệu hồ sơ đọc từ máy chủ: `anhChanDungFileId = c100d6bf-…` (có giá trị) nhưng trường ảnh dùng để hiển thị trả **rỗng**.
- Đặc tả `:1543` (SCR-IV-03, dòng 3 — Thẻ thông tin chính) yêu cầu thẻ này gồm *"**Ảnh chân dung 80x100** + Họ tên + Mã tư vấn viên + Trạng thái + Điểm đánh giá trung bình + Ngày công nhận"*.

Quan sát này trùng với phần đối tác đã nêu ở **vòng 1** của cùng ca ("sau khi lưu, ảnh chân dung không hiển thị ở màn chi tiết") ⇒ ghi kèm vào cùng mục lỗi để dev xử lý một lượt.

**Không** tính vào bug: ô **xem trước** ở màn sửa trên bản QA đang chạy không tải được ảnh, nhưng nguyên nhân là cấu hình đường dẫn kho tệp của **riêng máy chủ QA** (đường dẫn ảnh trả về dùng giao thức không bảo mật trong khi trang chạy giao thức bảo mật nên trình duyệt chặn). Trên bản của đối tác ô xem trước hiển thị bình thường ⇒ đây là chuyện môi trường, không phải lỗi sản phẩm.

---

## Verdict

| Ý | Nội dung | Verdict |
|---|---|---|
| 1 | Xóa ảnh chân dung đã lưu → "Lỗi hệ thống, vui lòng thử lại sau", không gỡ được ảnh | **Open** |
| 2 | (kèm theo) Màn chi tiết không hiển thị ảnh chân dung đã lưu, trái `:1543` | **Open** — gộp vào cùng mục lỗi |

**Verdict tổng: `Open`.**

Mục lỗi: [`../../bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md`](../../bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md) → `BUG-QLTVV_24`.

## Dọn dẹp môi trường

- `TVV-BTP-TW-0018`: đã gỡ liên kết ảnh và xóa tệp thử → hồ sơ trở lại nguyên trạng (`anhChanDungFileId` rỗng).
- `TVV-BTP-TW-0020`: **giữ nguyên** ảnh chân dung đang lỗi để dev tái hiện trực tiếp (`anhChanDungFileId = c100d6bf-f6dd-4dc0-98e1-5de545e2778e`).
