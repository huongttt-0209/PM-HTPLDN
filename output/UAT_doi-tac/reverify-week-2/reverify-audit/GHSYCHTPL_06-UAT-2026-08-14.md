# GHSYCHTPL_06 — Re-verify UAT ngày 2026-08-14

## Kết luận

**FAIL / Reopen — lỗi thông báo vẫn còn trên UAT v1.0.14.** Bốn vế đầu đã đạt, nhưng hệ thống không tạo thông báo cho Cán bộ Nghiệp vụ Địa phương cùng đơn vị. Vì chưa đạt toàn bộ kết quả mong đợi, không đổi `Trạng thái dev fix` sang `UAT done`.

## Điều kiện kiểm thử

| Thành phần | Giá trị |
|---|---|
| Môi trường | `https://htpldn-uat.ospgroup.vn` |
| Bản dựng | `HTPLDN · v1.0.14` |
| Tài khoản gửi | `0151554887` — vai trò `DN`, TKM Company / Tester TKM |
| Tài khoản kiểm thông báo | `cbnv_dp` — vai trò `CB_NV_DP`, Cán bộ Nghiệp vụ Địa phương |
| Đơn vị hai tài khoản | Cùng `donViId = 00000000-0000-4000-8002-000000000001` — Sở Tư pháp Hà Nội |
| Hồ sơ tạo mới | `VV-STP-HN-20260814-002` |
| ID hồ sơ | `97dc1871-db46-4f94-b8bf-6a37f9cbb7f7` |
| Tiêu đề | `QA GHSYCHTPL_06 UAT 20260814 1513` |
| Thời điểm tạo | `14/08/2026 15:15:04` (Asia/Ho_Chi_Minh) |
| Tệp kiểm thử | `GHSYCHTPL_06-UAT-before-submit.png`, 345.1 KB |

## Các bước đã thực hiện

1. Đăng nhập `cbnv_dp`; đọc `auth/me`, xác nhận vai trò `CB_NV_DP`, đơn vị Sở Tư pháp Hà Nội; ghi mốc thông báo: `25` chưa đọc, `26` tổng.
2. Đăng xuất; đăng nhập doanh nghiệp `0151554887`; đọc `auth/me`, xác nhận vai trò `DN` và cùng `donViId` với `cbnv_dp`.
3. Mở **Vụ việc HTPL → Gửi yêu cầu hỗ trợ pháp lý**; điền đủ nội dung, lĩnh vực Thuế, hình thức Tư vấn pháp luật, loại tài liệu Khác và tải một tệp PNG.
4. Bấm gửi đúng một lần. Request tải tệp trả `201`; request `POST /api/v1/vu-viecs/dn-submit` trả `201`.
5. Mở danh sách và chi tiết hồ sơ vừa tạo; đối chiếu mã, ưu tiên, trạng thái, tài liệu và dòng thời gian bằng UI và API.
6. Đăng xuất doanh nghiệp; đăng nhập lại `cbnv_dp`; mở chuông và trang **Thông báo**.
7. Chờ quá 5 phút kể từ thời điểm tạo, tải lại trang và đọc lại API thông báo để loại trừ độ trễ.

## Đối chiếu từng kết quả mong đợi

| STT | Kết quả mong đợi trong sheet | Kết quả thực tế | Trạng thái |
|---:|---|---|---|
| 1 | Hệ thống tự sinh mã vụ việc | API và UI sinh `VV-STP-HN-20260814-002` | PASS |
| 2 | Hệ thống tự tính mức ưu tiên | `uuTien = 3`; UI ghi lý do DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ | PASS |
| 3 | Tạo vụ việc ở bước “Mới tạo” và lưu tài liệu đính kèm | Thanh tiến trình có bước `Mới tạo`, trạng thái hiện tại `Chờ tiếp nhận`; tệp 345.1 KB hiện diện, trạng thái quét `Sạch`; API trả `trangThaiQuet = SACH` | PASS |
| 4 | Lịch sử “Tạo vụ việc” do doanh nghiệp thực hiện | UI có `Tạo vụ việc — 14/08/2026 15:15 — Tester TKM`; API trả `hanhDong = TAO_VV`, người thực hiện trùng user DN | PASS |
| 5 | Gửi thông báo cho cán bộ nghiệp vụ | Sau hơn 5 phút, `cbnv_dp` vẫn `25` chưa đọc / `26` tổng; danh sách mới nhất không có mã `VV-STP-HN-20260814-002` và không có `entityId = 97dc1871-db46-4f94-b8bf-6a37f9cbb7f7` | **FAIL** |

## Bằng chứng kỹ thuật

- Submit hồ sơ: upload `201`, `dn-submit` `201`.
- Chi tiết hồ sơ: `maVuViec = VV-STP-HN-20260814-002`, `trangThai = CHO_TIEP_NHAN`, `kenhTiepNhan = DOANH_NGHIEP`, `uuTien = 3`.
- Lịch sử: một bản ghi `TAO_VV`, actor `Tester TKM`, ID người thực hiện trùng tài khoản doanh nghiệp.
- Tài liệu: đúng tệp đã tải, `trangThaiQuet = SACH`.
- Thông báo trước khi tạo: `unread = 25`, `total = 26`.
- Thông báo sau khi tạo và chờ quá 5 phút: `unread = 25`, `total = 26`; bản ghi mới nhất của `cbnv_dp` vẫn là thông báo hệ thống lúc `14/08/2026 14:00:12`, sớm hơn thời điểm tạo hồ sơ.
- Console sau lần tải lại cuối: `0` error, `2` warning; warning không liên quan tới verdict.

## Ảnh bằng chứng

- `GHSYCHTPL_06-UAT-v2-before-submit-2026-08-14.png` — biểu mẫu đầy đủ trước khi gửi.
- `GHSYCHTPL_06-UAT-v2-after-submit-2026-08-14.png` — hồ sơ mới xuất hiện trong danh sách.
- `GHSYCHTPL_06-UAT-v2-detail-timeline-file-2026-08-14.png` — mã, ưu tiên, bước Mới tạo, tệp sạch và lịch sử Tạo vụ việc.
- `GHSYCHTPL_06-UAT-v2-cbnv-notification-final-2026-08-14.png` — trang Thông báo của `cbnv_dp` sau lần tải lại cuối, không có thông báo vụ việc mới.

## Trạng thái sheet

- Sheet: `bug`, `gid = 1714340219`.
- Dòng: `385`, `Mã TC = GHSYCHTPL_06`.
- Cột: `Trạng thái dev fix` (`R385`).
- Giá trị giữ nguyên: `Test done`.
- Không cập nhật sang `UAT done` vì còn một kết quả mong đợi bị FAIL.
- Đã nối thêm kết quả re-verify ngày 14/08/2026 vào cột `Kết quả verify` (`T385`) lúc 15:25; giữ nguyên toàn bộ nội dung verify cũ.
