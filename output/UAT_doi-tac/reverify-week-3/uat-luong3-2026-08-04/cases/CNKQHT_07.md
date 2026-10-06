# CNKQHT_07 — dòng 315 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

## Tuần

Tuần 3

## Mã TC

CNKQHT_07

## Mô tả

Cập nhật thành công

## Điều kiện

1. Đăng nhập tài khoản
2. Hồ sơ vụ việc đang ở trạng thái "Đang xử lý".

## Các bước thực hiện

1. Chọn menu "Vụ việc HTPL"
2. Tìm kiếm và nhấn Xem chi tiết
3. Nhập nội dung và tải tệp, sau đó bấm nút "Cập nhật kết quả"

## Kết quả mong đợi

- Hệ thống hiển thị thông báo "Đã cập nhật kết quả hỗ trợ" và làm mới Nhóm 6.
+ Lưu nội dung, tệp và ghi chú vào hồ sơ.
+ Gửi thông báo cho cán bộ nghiệp vụ phụ trách để xem xét và chuẩn bị trình phê duyệt.
+ Lưu vết thao tác theo quy định.

## Kết quả thực tế

CBNV không nhận được thông báo

## Ảnh/vieo 1

CNKQHT_07.webm

## Trạng thái 1

Fail

## Trạng thái dev fix 1

dev done

## Verify

Pass

## DEV phản hồi lần 1

Đã kiểm tra lại — lỗi đã được khắc phục, chức năng Cập nhật kết quả hỗ trợ nay có gửi thông báo cho cán bộ nghiệp vụ phụ trách trên cả hai kênh. Đội kiểm thử đã dựng lại đúng tình huống trong video đối tác gửi: một vụ việc đang ở bước 6 "Đang xử lý", người bấm cập nhật là Tư vấn viên kiêm Chuyên gia được phân công, còn người phải nhận thông báo là Cán bộ Nghiệp vụ Trung ương phụ trách vụ việc — hai tài khoản khác nhau.
• Thông báo trong phần mềm: ĐÃ CÓ. Ngay sau khi lưu kết quả, mở chuông Thông báo bằng chính tài khoản cán bộ nghiệp vụ phụ trách thì thấy mục mới nằm trên cùng, tiêu đề "Kết quả hỗ trợ đã được cập nhật - VV-BTP-TW-20260803-001", nội dung ghi rõ "Người được phân công đã cập nhật kết quả hỗ trợ vụ việc", kèm mã vụ việc, tên doanh nghiệp và lời nhắc đăng nhập để xem xét, chuẩn bị trình phê duyệt. Số đếm trên chuông cũng tăng thêm tương ứng.
• Thông báo qua email: ĐÃ CÓ. Có thư gửi tới đúng địa chỉ email của cán bộ nghiệp vụ phụ trách vụ việc, phát sinh ngay sau thời điểm bấm lưu, tiêu đề và nội dung trùng khớp với thông báo trong phần mềm.
• Đúng người nhận: đội kiểm thử đã đối chiếu và xác nhận người nhận thông báo chính là cán bộ nghiệp vụ đã tiếp nhận và phụ trách vụ việc, không phải người vừa bấm cập nhật, cũng không phải doanh nghiệp.
• Lưu ý về cách kiểm: trong video đối tác gửi, phần kiểm tra chuông thông báo được thực hiện bằng một tài khoản cán bộ nghiệp vụ khác với tài khoản đang phụ trách vụ việc đó, nên chưa loại trừ được khả năng kiểm nhầm hộp thông báo. Lần này đội kiểm thử mở chuông bằng đúng tài khoản phụ trách nên kết quả là chắc chắn.
• Đội kiểm thử đã chạy thao tác cập nhật kết quả hai lần ở hai thời điểm khác nhau, sau khi tải lại trang để chắc chắn không dính bản cũ đang mở sẵn. Cả hai lần đều sinh đủ thông báo trong phần mềm và email. Mỗi lần bấm lưu chỉ gửi đi một yêu cầu và chỉ hiện một khung thông báo "Đã cập nhật kết quả", không bị lặp.
• Verify: vụ việc VV-BTP-TW-20260803-001 ở trạng thái Đang xử lý; tài khoản phụ trách là Cán bộ Nghiệp vụ Trung ương (cbnv_tw_03), tài khoản thao tác là Tư vấn viên kiêm Chuyên gia được phân công (qa_tvvseed28). Toàn bộ dữ liệu tiền đề (tiếp nhận, kiểm tra hồ sơ, phân công, xác nhận tham gia) do đội kiểm thử tự dựng chứ không dùng dữ liệu có sẵn.
