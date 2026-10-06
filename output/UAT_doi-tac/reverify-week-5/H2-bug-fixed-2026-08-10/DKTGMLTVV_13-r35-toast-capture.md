# DKTGMLTVV_13 (sheet `bug` row 35) — bằng chứng toast sau khi Lưu hồ sơ TVV mới

- Môi trường: https://18.143.165.120.nip.io — bản dựng **HTPLDN · V1.0.11**
- Thời điểm đo: 2026-08-10 ~21:10 (giờ máy) / lượt tạo lúc 14:0x UTC
- Tài khoản: `nht_ag_uat2` (Người hỗ trợ pháp lý, Sở Tư pháp An Giang) — đúng Precondition ô "Kết quả verify"
- Đường đi: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → Thêm mới → nhập dữ liệu hợp lệ → **Lưu**

## Toast bắt được (MutationObserver cài TRƯỚC khi bấm, KHÔNG lọc trùng)

```
Đăng ký thành công, chờ thẩm định. Mã hồ sơ: TVV-STP-AG-0005
```

Ghi nhận 2 node (wrapper + notice) đúng như cấu trúc AntD v5 — không phải double-toast.

## Đối chiếu mã thật

| Đo | Giá trị |
|---|---|
| Mã trong câu thông báo | `TVV-STP-AG-0005` |
| Mã thật của hồ sơ vừa tạo (GET `/api/v1/tu-van-viens/52048ab9-5ac9-4a05-ae4b-8c5e263e03ce`) | `TVV-STP-AG-0005` |
| Trạng thái | `MOI_DANG_KY` → hiện ở tab "Mới đăng ký" |
| Loại | `TVV` (Tư vấn viên) |
| Lĩnh vực đã lưu | `Thương mại`, `Doanh nghiệp` (2/2) |
| Tổ chức chủ quản | `Trung tam Tu van Phap luat QA Dia phuong` (TC-STP-AG-0001) |
| Đơn vị quản lý tự gán | `Sở Tư pháp An Giang` (đúng đơn vị của người đăng ký) |

→ Trùng khớp, không rỗng / undefined / null, không phải mã hồ sơ khác. Đúng ✅ PASS (a)(b)(c).

## Bẫy đã tôn trọng

- Nút vẫn mang nhãn **"Lưu"** → KHÔNG log lại "thiếu nút Gửi đăng ký".
- Sau khi lưu hệ thống quay về **trang Danh sách** → KHÔNG log lại "không chuyển sang trang theo dõi tiến độ".
- Ô Loại chỉ có Tư vấn viên / Chuyên gia → KHÔNG log lại "thiếu loại Người hỗ trợ".

## Ghi nhận thêm (KHÔNG mở rộng case)

Khi lưu, phần mềm chặn tuần tự 2 điều kiện bắt buộc chưa nêu trong phiếu:
`File thẻ hành nghề là bắt buộc đối với Tư vấn viên` rồi `File đính kèm (Bằng cấp / Chứng chỉ) là bắt buộc khi đăng ký ứng viên mới`.
Đã nạp tệp cho cả hai rồi lưu được. Không thuộc phạm vi vế đang verify.
