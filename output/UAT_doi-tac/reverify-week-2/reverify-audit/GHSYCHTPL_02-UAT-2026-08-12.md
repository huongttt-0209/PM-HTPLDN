# Audit verify UAT — GHSYCHTPL_02 — 12/08/2026

## Kết luận

- Verdict: `BA confirm`.
- Hai phần đối tác phản ánh về ô “Thông tin người gửi” và việc doanh nghiệp tự chọn độ ưu tiên đã không còn trên UAT, phù hợp SRS.
- Form UAT vẫn không hiển thị Tên doanh nghiệp/MST. Kỳ vọng đối tác yêu cầu hai trường này ở dạng chỉ đọc, nhưng FR-V.I-02 chỉ quy định lấy `doanh_nghiep_id` từ phiên đăng nhập, không quy định phải hiển thị Tên doanh nghiệp/MST trên form. Cần BA chốt giao diện mong muốn trước khi chuyển dev.

## Cổng 1 — Bằng chứng đối tác

- Đã chạy `UAT_TAB=bug python3 output/UAT_doi-tac/tools/fetch_evidence.py --row 384` và mở full-res cả hai ảnh.
- Evidence 1: `partner-evidence/GHSYCHTPL_02-partner-1.jpg`, URL `uat.phapluat.gov.vn/danh-sach-vu-viec-vuong-mac-phap-ly`; người dùng đã đăng nhập, modal gửi hồ sơ mở; form có khối “THÔNG TIN NGƯỜI GỬI” gồm Họ và tên, Email, Số điện thoại; không thấy Tên doanh nghiệp/MST.
- Evidence 2: `partner-evidence/GHSYCHTPL_02-partner-2.jpg`, cùng URL/modal; form có “Độ ưu tiên” và “Lý do ưu tiên”, cho phép doanh nghiệp nhập/chọn.
- Dữ liệu tiền đề: vai trò doanh nghiệp đã đăng nhập, đang tạo yêu cầu hỗ trợ pháp lý mới; chưa có entity/trạng thái vụ việc vì claim nằm ở form trước khi gửi.

## Cổng 2 — Hiểu bug

Case có ba ý cần chấm riêng:

1. Form không nên yêu cầu doanh nghiệp nhập lại “Thông tin người gửi”.
2. Doanh nghiệp không được tự chọn độ ưu tiên/lý do ưu tiên; hệ thống phải tự tính.
3. Kỳ vọng đối tác muốn hiển thị Tên doanh nghiệp và MST ở dạng chỉ đọc.

Live UAT dùng tài khoản DN `0151554887`, tên hiển thị `Tester TKM`, doanh nghiệp `TKM Company`; vào `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý`.

## Cổng 3 — SRS so với UAT

| Ý | SRS yêu cầu | Thực tế UAT | Kết luận con |
|---|---|---|---|
| Thông tin người gửi | FR-V.I-02 (UC52) Inputs dòng 179-185 chỉ gồm doanh nghiệp từ session, tiêu đề, loại hình, lĩnh vực, nội dung, mô tả vướng mắc và tệp; không có Họ tên/Email/SĐT người gửi. | Không còn khối “Thông tin người gửi”; kiểm ảnh và `innerText` dialog đều không có Họ tên/Email/SĐT. | `Resolved` |
| Độ ưu tiên | FR-V.I-02 Processing dòng 196: hệ thống tự tính `uu_tien` theo BR-CALC-07; mức 4/5 chỉ CB NV được nâng theo BR-CALC-07 dòng 2419-2423. | Form DN không có “Độ ưu tiên” hay “Lý do ưu tiên”; kiểm ảnh và `innerText` đều không có. | `Resolved` |
| Tên DN/MST chỉ đọc | FR-V.I-02 dòng 179 quy định `doanh_nghiep_id` lấy từ session, không nhập thủ công; dòng 187 nói thông tin DN được đọc từ DOANH_NGHIEP. SRS không có thành phần màn hình yêu cầu hiển thị Tên DN/MST trong form DN. | Form không hiển thị Tên doanh nghiệp/MST. | `BA confirm` vì expected đối tác chi tiết hơn SRS |

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test trên UAT | GAP? |
|---|---|---|---|
| Vai trò / đăng nhập | Người dùng DN đã đăng nhập trên chuyên trang | DN `0151554887`, role `Doanh nghiệp`, đã đăng nhập UAT | Không |
| Surface / state | Modal gửi hồ sơ mới, trước submit | `Vụ việc HTPL` → `Gửi yêu cầu hỗ trợ pháp lý`, form mới trước submit | Không |
| Dữ liệu DN | DN đã có phiên đăng nhập; expected muốn thấy Tên DN/MST | Header tài khoản hiển thị `Tester TKM · Doanh nghiệp`; danh sách phía sau xác nhận DN là `TKM Company`; form vẫn không có Tên DN/MST | Không |

## Gate real-data

- Artifact live đã mở đọc: `GHSYCHTPL_02-UAT-form-top.png`.
- Ảnh pixel cho thấy toàn bộ form hiện tại chỉ có: Tiêu đề, Nội dung, Lĩnh vực pháp lý, Loại hình hỗ trợ, Loại giấy tờ/Tài liệu đính kèm.
- Kiểm độc lập bằng `innerText` và danh sách label của dialog:
  - `coThongTinNguoiGui=false`.
  - `coDoUuTien=false`.
  - `coTenDoanhNghiep=false`.
  - `coMaSoThue=false`.
- Ngoài tiêu chí case: form UAT có trường “Loại giấy tờ” nhưng SRS FR-V.I-02 chưa mô tả; chưa log bug vì chưa có căn cứ xác định đây là hành vi sai và không ảnh hưởng ba claim đang chấm.

## Câu hỏi BA

Trên form doanh nghiệp gửi yêu cầu hỗ trợ pháp lý, BA chốt phương án nào?

1. Hiển thị Tên doanh nghiệp và Mã số thuế ở dạng chỉ đọc để DN nhận biết hồ sơ đang gửi dưới doanh nghiệp nào; nếu chọn phương án này, đề nghị bổ sung hai thành phần vào mô tả màn hình/FR-V.I-02 rồi chuyển dev.
2. Không hiển thị hai trường trên form, chỉ lấy `doanh_nghiep_id` từ phiên đăng nhập như UAT hiện tại; nếu chọn phương án này, đề nghị phản hồi đối tác rằng kỳ vọng cần điều chỉnh.

Hai phần “Thông tin người gửi” và “Độ ưu tiên/Lý do ưu tiên” không cần BA chốt lại vì UAT hiện tại đã bỏ và phù hợp SRS.
