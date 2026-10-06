# GHSYCHTPL_06 — Verify lại trên UAT ngày 2026-08-12

## Kết luận

**Open — lỗi còn một phần.** UAT đã ghi lịch sử tạo vụ việc đúng, nhưng vẫn không tạo thông báo cho cán bộ nghiệp vụ phụ trách.

## Điều kiện kiểm thử

| Thành phần | Giá trị |
|---|---|
| Môi trường | `https://htpldn-uat.ospgroup.vn` |
| Tài khoản gửi hồ sơ | `0151554887` — Doanh nghiệp, TKM Company / Tester TKM |
| Tài khoản nhận thông báo | `cbnv_dp` — Cán bộ Nghiệp vụ Địa phương, Sở Tư pháp Hà Nội |
| Hồ sơ kiểm thử | `VV-STP-HN-20260812-001` — `QA GHSYCHTPL_06 UAT 20260812 2157` |
| Thời điểm tạo | 12/08/2026 21:57 (Asia/Ho_Chi_Minh) |
| Kênh tiếp nhận | Doanh nghiệp |

## Đối chiếu SRS

- `FR-V.I-02 (UC52)` dòng 195-200 yêu cầu tự sinh mã, tự tính ưu tiên, tạo vụ việc, lưu tệp, ghi lịch sử `TAO_VV` với vai trò `DN` và gửi thông báo cho CB NV theo tỉnh/thành của doanh nghiệp.
- Postcondition dòng 205-206 yêu cầu hồ sơ được tạo chờ tiếp nhận và CB NV nhận thông báo.

## Kết quả thực tế

1. Doanh nghiệp gửi hồ sơ thành công; hệ thống sinh mã `VV-STP-HN-20260812-001` và chỉ phát sinh một request gửi hồ sơ (`POST /api/v1/vu-viecs/dn-submit`), ngoài request upload tệp.
2. Chi tiết vụ việc hiển thị ưu tiên `3`, kênh `Doanh nghiệp`, trạng thái chờ tiếp nhận và dòng thời gian `Tạo vụ việc — 12/08/2026 21:57 — Tester TKM`.
3. API lịch sử trả `hanhDong = TAO_VV`; người thực hiện trùng tài khoản đang đăng nhập với role `DN`.
4. API hồ sơ trả tệp `GHSYCHTPL_06-attachment.png`, trạng thái quét `SACH`.
5. Đăng nhập `cbnv_dp` đúng đơn vị Sở Tư pháp Hà Nội. Trang Thông báo lúc 21:59 không có thông báo cho mã vụ việc vừa tạo; thông báo mới nhất vẫn là dữ liệu lúc 15:30.
6. API `GET /api/v1/thong-baos?sortBy=createdAt&sortOrder=DESC&page=1&pageSize=20` trả 18 bản ghi, không có `entityId = 5c759371-0f52-45e7-9080-ce2855bafb28`, không có mã `VV-STP-HN-20260812-001`, và không có thông báo nào tạo sau thời điểm 21:57.

## Bằng chứng

- `GHSYCHTPL_06-UAT-after-submit.png`: toast gửi thành công và mã vụ việc mới.
- `GHSYCHTPL_06-UAT-timeline.png`: ưu tiên, kênh và lịch sử `Tạo vụ việc` đã được ghi nhận.
- `GHSYCHTPL_06-UAT-cbnv-notifications.png`: danh sách thông báo của `cbnv_dp` không có vụ việc vừa tạo.
- `partner-evidence/GHSYCHTPL_06.webm`: video gốc của đối tác.
- `GHSYCHTPL_06-partner-t023.png`: bằng chứng cũ hiển thị `Chưa có lịch sử hoạt động`.

## Phân loại

- Nội dung “không ghi lịch sử tạo vụ việc, vai trò DN”: **đã sửa trên UAT**.
- Nội dung “không gửi thông báo cho CBNV”: **vẫn lỗi trên UAT**.
- Trạng thái chung của testcase: **Bug / Open**.
