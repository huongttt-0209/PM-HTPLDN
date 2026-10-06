# Đo lại `QLDXDTTH_11` theo yêu cầu `[CẦN ĐO LẠI]` của BA — 04/08/2026

> **Nguồn yêu cầu:** `phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md` §Vấn đề 10 — BA không chốt được vì
> sổ chính ghi `QLDXDTTH_08` (dòng 337) **Pass** trên môi trường bàn giao, còn phiếu re-verify của tổ
> kiểm thử lại nói không có nút Tiếp nhận. BA yêu cầu **đo lại trên đúng môi trường bàn giao**.
>
> **Dòng trên sổ nội bộ:** tab `UAT_TGPL Doanh Nghiệp-tuần 2` (gid `1905542591`) row **135**,
> hiện `Trạng thái dev fix 1` = `BA confirm`, `Verify` = `BA confirm`.

## Điều kiện đo — đã khớp đúng điều kiện BA nêu

| Điều kiện | Giá trị |
|---|---|
| Môi trường | `https://htpldn-uat.ospgroup.vn` — **môi trường bàn giao**, không phải `nip.io` |
| Bản dựng | **HTPLDN · V1.0.5** (đọc từ thanh bên trái) |
| Tài khoản | `cbnv_tw` · vai trò `CB_NV_TW` · đơn vị **Cục Bổ trợ tư pháp — Bộ Tư pháp** · `donViId = 00000000-0000-4000-8000-000000000001` · `capDonVi = TW` |
| Đường đi | **Chương trình đào tạo → tab "Đề xuất đào tạo"** — đúng đường mà BA nói `QLDXDTTH_08` đã đi |
| Thời điểm | 04/08/2026 |

**GAP "khác đơn vị" đã đóng:** trong 16 bản ghi có **4 bản ghi trạng thái "Mới gửi" thuộc chính đơn vị
Cục Bổ trợ tư pháp — Bộ Tư pháp** (25/07, 23/07 ×2, 12/06). Đây là các bản ghi mà cán bộ này chắc chắn
có thẩm quyền tiếp nhận.

## Kết quả đo — lỗi TÁI HIỆN trên môi trường bàn giao

**1. Danh sách — cột "Hành động" rỗng ở 16/16 dòng**

Không dòng nào có thao tác, kể cả 4 dòng "Mới gửi" cùng đơn vị. Nội dung ô là dấu gạch ngang.

Đọc thẳng DOM của ô "Hành động" trên dòng *"kiểm thử độc lập test"* (Mới gửi · Cục Bổ trợ tư pháp):

```html
<span style="color: rgb(153, 153, 153);">—</span>
```

Chỉ đúng **một** phần tử, không có nút nào bị ẩn (`display`/`visibility` đã kiểm) ⇒ loại trừ khả năng
"nút có nhưng bị CSS giấu".

Ảnh: `image/BUG-QLDXDTTH_11-doban-giao-danhsach-hanhdong-gachngang.png`

**2. Màn chi tiết — chỉ có "Quay lại danh sách"**

Mở `/dao-tao/de-xuat/cb26b79d-6abd-4044-bc70-957b3728205f` (bản ghi trên, trạng thái "Mới gửi"):
toàn màn chỉ có duy nhất nút **"Quay lại danh sách"**. Không có Tiếp nhận, không có Đánh dấu thực hiện,
không có Từ chối. Vùng thao tác cuối màn là một khối trống.

Ảnh: `image/BUG-QLDXDTTH_11-doban-giao-chitiet-chi-co-quaylai.png`

**3. Nút "Gửi đề xuất mới" VẪN hiện với vai trò cán bộ** — đúng như tổ kiểm thử ghi nhận trước đó.

## Đo bằng phương pháp thứ hai (gọi thẳng máy chủ) — chỉ ra chỗ hỏng nằm ở giao diện

**a. Máy chủ CÓ đủ chức năng.** Đọc `/api/docs-json` (không cần đăng nhập):

| Đường dẫn | Mô tả trong tài liệu API |
|---|---|
| `POST /api/v1/de-xuat-dao-taos/{id}/receive` | **Tiếp nhận đề xuất đào tạo** |
| `POST /api/v1/de-xuat-dao-taos/{id}/process` | Xử lý đề xuất đào tạo |
| `POST /api/v1/de-xuat-dao-taos/{id}/complete` | Hoàn thành xử lý đề xuất đào tạo |
| `POST /api/v1/de-xuat-dao-taos/{id}/reject` | Từ chối đề xuất đào tạo |

**b. Vai trò `CB_NV_TW` ĐƯỢC máy chủ cấp quyền tiếp nhận.** `GET /api/v1/auth/me` trả 242 quyền,
trong đó nhóm đề xuất đào tạo gồm:

```
create_de_xuat_dao_tao · delete_de_xuat_dao_tao · read_de_xuat_dao_tao
receive_de_xuat_dao_tao · update_de_xuat_dao_tao
```

**c. Phép thử quyền không làm đổi dữ liệu.** Gọi `POST /api/v1/de-xuat-dao-taos/{uuid-không-tồn-tại}/receive`
bằng chính phiên đăng nhập `cbnv_tw`:

```json
HTTP 404 — {"code":"ERR-VAL-VII-02-01","message":"Bản ghi không tồn tại"}
```

Trả **404** chứ không phải **403** ⇒ yêu cầu đã **qua được lớp kiểm tra quyền**, chỉ dừng ở bước tra bản ghi.
Chọn UUID giả để không làm đổi trạng thái bản ghi thật nào.

## Kết luận

**Đây là lỗi thật, và KHÔNG còn cần BA xác nhận cho câu hỏi chính.**

Câu hỏi mà tổ kiểm thử đưa lên BA là *"đặc tả tự mâu thuẫn: FR-III-13 giao việc tiếp nhận cho CB NV,
nhưng Ma trận phân quyền `srs-v3.5.md:1309` chỉ cấp quyền đọc"*. Phép đo hôm nay **đã tự trả lời** mâu thuẫn đó:

- Máy chủ **đã cấp** `receive_de_xuat_dao_tao` + `update_de_xuat_dao_tao` cho `CB_NV_TW`;
- Bản bàn giao `.docx` mục **4.3.13.1** và **4.3.13.2.3 STT 4/5** cũng giao việc tiếp nhận cho cán bộ nghiệp vụ;
- `srs-fr-03-dao-tao.md:1045` (§Mô tả) và `:1875` (SCR-III-01 Thành phần 8) nói cùng một điều.

⇒ Ba nguồn cùng chiều, chỉ riêng dòng ma trận `:1309` lệch. Đó là **việc dọn tài liệu của BA**, không phải
điều kiện để chốt verdict. Phần hỏng nằm ở **giao diện không dựng thao tác** dù máy chủ đã sẵn sàng và đã
cấp quyền → **lỗi FE**, dev sửa được ngay.

**Về việc sổ chính ghi `QLDXDTTH_08` = Pass:** phép đo hôm nay trên **đúng môi trường bàn giao** cho kết quả
ngược lại. Nghĩa là hoặc phiếu Pass đó được chấm ở bản dựng trước rồi bị hồi quy, hoặc chấm chưa chặt.
Hiện trạng đo được ngày 04/08/2026 là **không có thao tác nào**. Trên môi trường vẫn còn bản ghi ở trạng thái
"Đã tiếp nhận" / "Đang xử lý" / "Đã xử lý" — phù hợp với giả thuyết chức năng từng chạy được rồi mất,
hoặc trạng thái được dựng qua máy chủ.

### Verdict đề xuất cho row 135

| Ô | Giá trị đề xuất |
|---|---|
| `Trạng thái dev fix 1` (đang là `BA confirm`) | **`Open`** |
| `Verify` (đang là `BA confirm`) | **`Open`** |
| `DEV phản hồi lần 1` | note theo mẫu Open + khối CÁCH VERIFY (đã soạn, chờ ghi) |

### Ý phụ (a) VẪN CẦN BA — tách riêng, không chặn verdict trên

*"Vai trò cán bộ có được phép **gửi** đề xuất đào tạo không?"* — phiếu BA ngày 04/08 **không trả lời ý này**.

Dữ kiện đo được làm câu hỏi rõ hơn:
- Máy chủ **có** cấp `create_de_xuat_dao_tao` cho `CB_NV_TW`, và trên môi trường bàn giao có **4 bản ghi**
  ghi người đề xuất là *"CB Nghiệp vụ TW 01 — Cục Bổ trợ tư pháp"* ⇒ cán bộ đã gửi được trên thực tế.
- Nhưng `srs-fr-03-dao-tao.md:1047` (§Tác nhân) chỉ ghi **DN / NHT**, và bản bàn giao mục **4.3.13.2.3 STT 1**
  ghi người gửi là *"doanh nghiệp hoặc người hỗ trợ pháp lý"*.

⇒ Hai tài liệu cùng loại trừ cán bộ khỏi vai trò người gửi, trong khi phần mềm cho phép. Cần BA chốt:
giữ như hiện tại (và sửa §Tác nhân), hay ẩn nút "Gửi đề xuất mới" với vai trò cán bộ.
