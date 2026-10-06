# Bản ghi thô phép thử tách biến Tỉnh/Thành phố — QLDKTK_01 — 04/08/2026 15:20 (giờ VN)

Cùng một thân yêu cầu, **chỉ đổi mỗi `tinhThanhId`**. Mã số thuế mỗi lần đều là mã hoàn toàn mới, chưa có trong hệ thống.

## A. Luồng doanh nghiệp tự đăng ký — `POST /api/v1/auth/register-doanh-nghiep` (không cần đăng nhập)

```
TP.HCM   6dd0bf43-54b5-4ab3-9d1c-7f30f6d50727  MST 0311224455
   -> HTTP 201 {"success":true,"data":{"id":"01d1f407-a436-42b2-aca8-44fc140ecf0e","trangThai":"CHO_KICH_HOAT",
                "message":"Đăng ký doanh nghiệp thành công. Vui lòng kiểm tra email để kích hoạt tài khoản..."}}
   => hệ thống cấp mã DN-HCM-0003

Hà Nội   7ab46d68-7aad-49b0-bee6-51465e301e4a  MST 0311224466
   -> HTTP 409 {"success":false,"error":{"code":"ERR-DN-02","field":"maSoThue",
                "message":"Mã số thuế đã tồn tại trong hệ thống"}}

An Giang a3f8a913-832b-456e-86a7-327bd81288fe  MST 0311224477
   -> HTTP 201 {"success":true,"data":{"id":"807da526-6faf-4ad4-a047-635defc19b1c","trangThai":"CHO_KICH_HOAT"}}
   => hệ thống cấp mã DN-AGG-0004
```

## B. Luồng cán bộ nghiệp vụ tạo hồ sơ doanh nghiệp — `POST /api/v1/doanh-nghieps` (tài khoản `cbnv_tw`)

```
TP.HCM  MST 0311224488 -> HTTP 201 {"success":true,...,"maDoanhNghiep":"DN-HCM-0004"}
Hà Nội  MST 0311224499 -> HTTP 409 {"success":false,"error":{"code":"ERR-STATE-SYS-00-01",
                                     "message":"Mã doanh nghiệp vừa bị trùng do thao tác đồng thời. Vui lòng thử lại."}}
```

Riêng Hà Nội đã thử **3 lần liên tiếp cách nhau 1 giây, 3 mã số thuế khác nhau** (0301998281 / 0301998282 / 0301998283)
— cả 3 lần đều trả đúng một câu như trên, nên **không phải** do "thao tác đồng thời".

## C. Bảng mã doanh nghiệp hiện có, nhóm theo tỉnh

Đọc `GET /api/v1/doanh-nghieps?page=1..3&limit=20` — 47 bản ghi.

```
tỉnh   số bản ghi  số thứ tự đang có                             (số bản ghi + 1)  kết quả
01              1  [1]                                                          2  trống -> tạo được
AG              4  [1, 2, 3, 4]                                                 5  trống -> tạo được
AGG             4  [1, 2, 3, 4]                                                 5  trống -> tạo được
BCT             1  [1]                                                          2  trống -> tạo được
BG              3  [1, 2, 3]                                                    4  trống -> tạo được
BGG             2  [1, 2]                                                       3  trống -> tạo được
BKH             1  [1]                                                          2  trống -> tạo được
BNI             3  [1, 2, 3]                                                    4  trống -> tạo được
BTC             1  [1]                                                          2  trống -> tạo được
HCM             4  [1, 2, 3, 4]                                                 5  trống -> tạo được
HNI            13  [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 16, 17]              14  *** TRÙNG với mã đã có -> BỊ CHẶN
TW              1  [1]                                                          2  trống -> tạo được
XX              5  [1, 2, 3, 4, 5]                                              6  trống -> tạo được
```

**Hà Nội là tỉnh duy nhất có lỗ hổng trong dãy số thứ tự** (thiếu 7, 8, 9, 10 — nhiều khả năng do bản ghi cũ bị xóa).
Vì vậy `số bản ghi + 1 = 14` rơi trúng `DN-HNI-0014` đang tồn tại.

## D. Bằng chứng bộ sinh mã chạy theo "đếm + 1" chứ không phải "lớn nhất + 1"

| Trước khi tạo | Mã được cấp |
|---|---|
| TP.HCM có 2 bản ghi (số thứ tự 1, 2) | **DN-HCM-0003** = 2 + 1 |
| TP.HCM có 3 bản ghi (số thứ tự 1, 2, 3) | **DN-HCM-0004** = 3 + 1 |
| An Giang AGG có 3 bản ghi (số thứ tự 1, 2, 3) | **DN-AGG-0004** = 3 + 1 |

Nếu là "lớn nhất + 1" thì Hà Nội sẽ ra `DN-HNI-0018` và không hề trùng.

## E. Suy ra

1. Bộ sinh mã doanh nghiệp lấy **số bản ghi hiện có của tỉnh + 1**, không lấy số lớn nhất + 1.
2. Tỉnh nào từng bị xóa bản ghi thì dãy số có lỗ hổng ⇒ mã sinh ra trùng mã cũ ⇒ vi phạm ràng buộc duy nhất trên cột mã doanh nghiệp.
3. Luồng tự đăng ký bắt lỗi vi phạm ràng buộc đó rồi **quy sai cho mã số thuế** → trả `ERR-DN-02` "Mã số thuế đã tồn tại trong hệ thống".
   Luồng cán bộ tạo thì quy sai cho **thao tác đồng thời** → `ERR-STATE-SYS-00-01`.
4. Hệ quả cần lưu ý: **mỗi lần xóa một doanh nghiệp là tạo thêm một lỗ hổng**, và tỉnh đó sẽ bị chặn đăng ký ngay sau đó.
