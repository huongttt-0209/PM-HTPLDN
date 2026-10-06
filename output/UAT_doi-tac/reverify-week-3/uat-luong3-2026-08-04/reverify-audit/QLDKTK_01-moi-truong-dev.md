# Nhật ký đo bổ sung — QLDKTK_01 trên môi trường dev — 04/08/2026 15:45–16:00

**Môi trường:** `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025`
**Khác UAT:** OTP **không** cố định `666666`, phải lấy từ MailHog.
**Tài khoản:** `cbnv_tw` · `cbnv_hn` (Sở Tư pháp Hà Nội) · `cbnv_dp_01` (An Giang) · `admin` — mật khẩu theo `input/input.md`.

**Mục đích:** kiểm chứng độc lập giả thuyết rút ra từ UAT. Đây là phép thử **phản nghiệm**, không phải phép thử để đóng bug —
dù dev có chạy được thì kết luận Reopen trên UAT vẫn giữ, vì lỗi phụ thuộc dữ liệu từng môi trường.

---

## 1. Dự đoán ghi TRƯỚC khi bấm

Đọc dãy mã doanh nghiệp trên dev (`GET /api/v1/doanh-nghieps`, 8 bản ghi):

```
tỉnh   số bản ghi  số thứ tự đang có   (đếm+1)  dự đoán
HNI             5  [1, 2, 3, 5, 6]           6  *** SẼ BỊ CHẶN (trùng DN-HNI-0006)
AGG             1  [1]                       2  đăng ký được
07              1  [1]                       2  đăng ký được
SEED            1  [1]                       2  đăng ký được
```

## 2. Kết quả — dự đoán TRÚNG ở ca chính

`POST /api/v1/auth/register-doanh-nghiep`, cùng thân yêu cầu, chỉ đổi `tinhThanhId`:

```
Hà Nội   (deac39eb…) MST 0311990011 -> HTTP 409 ERR-DN-02 "Mã số thuế đã tồn tại trong hệ thống"
An Giang (0a01fc3e…) MST 0311990022 -> HTTP 201, cấp DN-AGG-0002
```

Quét rộng thêm, mỗi tỉnh 1 mã số thuế mới:

```
Hà Nội lần 1  -> ERR-DN-02
Hà Nội lần 2  -> ERR-DN-02      (xác định, lặp lại được)
TP.HCM        -> OK 201
Hải Phòng     -> OK 201
Đà Nẵng       -> OK 201
```

⇒ **Trùng khớp UAT:** chỉ Hà Nội bị chặn, các tỉnh khác chạy bình thường, trên hai môi trường khác nhau.

## 3. Luồng cán bộ nghiệp vụ — mã lỗi nói thẳng nguyên nhân

`POST /api/v1/doanh-nghieps` bằng `cbnv_hn` (Sở Tư pháp Hà Nội):

```
Hà Nội  -> HTTP 409 ERR-STATE-SYS-00-01 "Mã doanh nghiệp vừa bị trùng do thao tác đồng thời. Vui lòng thử lại."
TP.HCM  -> ERR-DN-05 "Tỉnh/thành không khớp với đơn vị quản lý của bạn"   (đúng nghiệp vụ, không phải lỗi)
```

Y hệt UAT. ⇒ Thứ bị trùng là **mã doanh nghiệp hệ thống tự cấp**, không phải mã số thuế người dùng nhập.
Luồng tự đăng ký gộp lỗi này vào `ERR-DN-02` nên câu báo ra màn hình sai bản chất.

## 4. Phép can thiệp — BÁC BỎ công thức "đếm + 1" mà tôi nêu ở vòng UAT

Tự dựng lỗ hổng trên An Giang bằng chính bản ghi của mình:

| Bước | Trạng thái dãy AGG | Thao tác | Mã được cấp |
|---|---|---|---|
| 1 | `[1]` | đăng ký | DN-AGG-0002 |
| 2 | `[1,2]` | đăng ký | DN-AGG-0003 |
| 3 | `[1,2,3]` | đăng ký | DN-AGG-0004 |
| 4 | `[1,2,3,4]` | đăng ký | DN-AGG-0005 |
| 5 | `[1,2,3,4,5]` | **xóa DN-AGG-0003** (bằng `cbnv_dp_01`, HTTP 204) → `[1,2,4,5]` | — |
| 6 | `[1,2,4,5]` — đếm = 4, đếm+1 = **5 (đã có)** | đăng ký | **DN-AGG-0006**, HTTP 201 |

Nếu bộ sinh chạy theo "đếm + 1" thì bước 6 phải trả về trùng `DN-AGG-0005` và **bị chặn**. Thực tế **chạy được** và cấp `0006`.

⇒ **Công thức "số bản ghi của tỉnh + 1" mà tôi viết trong kết luận UAT là SAI.** Trên UAT nó khớp chỉ vì
với các tỉnh ở đó, số bản ghi tình cờ bằng giá trị bộ đếm.

Cũng không phải "số lớn nhất + 1": Hà Nội trên dev có số lớn nhất là 6 → 7 còn trống, mà vẫn bị chặn;
trên UAT số lớn nhất là 17 → 18 còn trống, cũng vẫn bị chặn.

## 5. Giả thuyết còn lại (CHƯA chứng minh được từ ngoài)

Bộ cấp số thứ tự theo tỉnh nhiều khả năng là một **bộ đếm lưu riêng**, và bộ đếm của Hà Nội đang **lệch so với
dữ liệu nạp sẵn** — các bản ghi Hà Nội được seed thẳng vào cơ sở dữ liệu với mã đặt cứng mà không đẩy bộ đếm lên,
nên số kế tiếp mà bộ đếm sinh ra rơi trúng mã đã có.

Khớp với mọi quan sát:
- Hà Nội (dev): 5 bản ghi seed, bộ đếm đứng ở 5 → sinh `DN-HNI-0006` → đã có → chặn.
- Hà Nội (UAT): 13 bản ghi seed, bộ đếm đứng ở 13 → sinh `DN-HNI-0014` → đã có → chặn.
- An Giang (dev): mọi bản ghi từ 0002 trở đi do QA tạo qua API nên bộ đếm chạy đúng → xóa bản giữa cũng không sao.
- TP.HCM / Hải Phòng / Đà Nẵng (dev): chưa có bản ghi nào, bộ đếm bằng 0 → chạy bình thường.

**Không kiểm chứng được từ ngoài** vì không xóa được bản ghi Hà Nội (chỉ đơn vị chủ quản mới xóa được;
`cbnv_tw` 403, `admin` 403 — `ERR-PERM-SYS-00-01`). Phần này ghi là **giả thuyết**, đã bỏ khỏi note gửi đối tác;
note chỉ nêu sự thật đo được + gợi ý chỗ soi.

## 6. Kết luận

- Lỗi **tái hiện trên cả dev lẫn UAT**, xác định, chỉ với Hà Nội ⇒ là lỗi mã nguồn, không phải sự cố dữ liệu riêng của UAT.
- Verdict `Reopen` cho dòng 321 **giữ nguyên**.
- Note trên sheet đã được **ghi đè lại** để bỏ công thức "đếm+1" đã bị bác.

## 7. Dữ liệu QA tạo trên môi trường dev

Doanh nghiệp + tài khoản Chờ kích hoạt, mã số thuế: `0311990022` `0311990033` (đã xóa) `0311990044` `0311990055`
`0311990066` `0322110003` `0322110004` `0322110005` `0333110002` `0333110003` `0333110004` — tên đều bắt đầu bằng "QA ".
Đã xóa `DN-AGG-0003` (MST `0311990033`) trong lúc làm phép can thiệp; các bản ghi còn lại giữ nguyên.
