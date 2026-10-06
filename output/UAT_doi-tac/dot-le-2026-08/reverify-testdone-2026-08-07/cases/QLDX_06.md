# QLDX_06 — row 166 (tab `bug`)

## [2] Tuần

Tuần 3

## [3] Mã TC

QLDX_06

## [6] Mô tả

Xác nhận "Đăng xuất" trên hộp thoại cảnh báo hết phiên

## [7] Điều kiện

1. Đăng nhập hệ thống thành công

## [9] Các bước thực hiện

1. Không thao tác suốt 25 phút kể từ lần thao tác cuố
2. Bấm "Đăng xuất" hoặc tiếp tục không thao tác đến phút thứ 30

## [10] Kết quả mong đợi

Chuyển NSD về trang đăng nhập kèm thông báo "Phiên làm việc đã hết hạn do không có thao tác".

## [13] Trạng thái

Fail

## [14] Dopai

Open

## [17] Trạng thái dev fix

Test done

## [19] Kết quả verify

✅ Đã hết lỗi — verify lại 07/08/2026 02:45–03:05 trên env nội bộ 18.143.165.120.nip.io, bó mã FE index-D4Buvu4S.js (dev deploy lại lúc 02:23:01 cùng ngày, giữa lô verify), vai trò Cán bộ Nghiệp vụ Trung ương (cbnv_tw_03). Không dùng tài khoản quản trị để chấm. Phiếu có hai nhánh ("bấm Đăng xuất" HOẶC "để đến phút thứ 30") nên đo cả hai, mỗi nhánh một phiên riêng.

NHÁNH ĐỂ ĐẾN PHÚT THỨ 30 — đúng y phiếu yêu cầu
- Hệ thống tự đăng xuất đúng mốc 30 phút không thao tác: mẫu đo còn sống cuối cùng ở mức không thao tác 30,004 phút; yêu cầu đăng xuất được máy chủ xử lý lúc 02:58:55, so với mốc 30 phút tính từ mốc gốc là 02:58:54.888 — lệch dưới 1 giây.
- Chuyển đúng về trang đăng nhập, kèm đúng MỘT thông báo, trùng từng ký tự phiếu yêu cầu: "Phiên làm việc đã hết hạn do không có thao tác."
- Đối chứng độc lập: gọi /api/v1/auth/me sau khi bị đưa về trang đăng nhập trả HTTP 401 — phiên bị hủy thật ở máy chủ, khớp srs-fr-10-quan-tri.md:1000–:1002 (bước "Hủy hiệu lực JWT token (thêm vào danh sách đen)").
- Đã loại khả năng "bị đá vì máy chủ trả lỗi 401" chứ không phải do đồng hồ: toàn bộ 11 yêu cầu chạy nền trong 5 phút chờ đều trả 304, không có 401 nào trước lúc chuyển trang; mốc tính không thao tác giữ nguyên ở 100% mẫu nên cũng loại khả năng màn hình tự làm mới.

NHÁNH BẤM [Đăng xuất] TRÊN HỘP THOẠI — về trang đăng nhập đúng, câu thông báo khác và đúng theo đặc tả
- Bấm lúc 02:49:37 (mức không thao tác ~25,5 phút): chuyển đúng về trang đăng nhập, có form đăng nhập, kèm đúng MỘT thông báo (không nhân đôi): "Đăng xuất thành công."
- Đối chứng độc lập: /api/v1/auth/me sau đó trả HTTP 401; POST /auth/logout trả 200 và máy chủ hết hạn cả access_token lẫn refresh_token ⇒ phiên bị hủy thật.
- Câu thông báo ở nhánh này KHÁC câu ghi trong phiếu, nhưng đây KHÔNG phải lỗi: ở phút thứ 25 phiên chưa hết hạn mà người dùng chủ động bấm đăng xuất, nên theo srs-fr-10-quan-tri.md:1011 (Outputs: message = "Đăng xuất thành công" / "Phiên hết hạn") thì "Đăng xuất thành công" đúng là câu dành cho tình huống chủ động. Câu "Phiên làm việc đã hết hạn do không có thao tác" thuộc nhánh hết phiên, và ở nhánh đó hệ thống đã hiện đúng y như vậy.
- Nếu nghiệp vụ vẫn muốn hiện câu hết-phiên ở CẢ hai nhánh thì cần BA chốt lại, vì yêu cầu đó ngược với :1011.

Đề nghị BA bổ sung đặc tả (không chặn bàn giao, không phải lỗi dev): trong SRS v3.5 câu thông báo hết phiên tồn tại ở bốn dạng lệch nhau — srs-fr-10-quan-tri.md:964 (ERR-DN-07 "Phiên làm việc hết hạn"), :1011, srs-fr-05-vu-viec.md:1593, srs-fr-02-hoi-dap.md:1135 — và không dạng nào có cụm "do không có thao tác" như bản đang chạy và như phiếu. Đề nghị chốt một câu chuẩn.

Bằng chứng (output/UAT_doi-tac/reverify-week-5/F5-devfix-2026-08-07/): image/QLDX_06-C2a-modal-truoc-moc-30.png · image/QLDX_06-C2-sau-tu-dang-xuat.png · image/QLDX_06-C2b-thongbao-idle-cap1.png · image/QLDX_06-C2b-thongbao-idle-cap2.png · image/QLDX_06-C1a-truoc-khi-bam-dang-xuat.png · image/QLDX_06-C1a-sau-khi-bam-ve-login.png · image/QLDX_06-thongbao.txt · image/QLDX_06-timeline.txt · image/QLDX_06-doi-chung-api.txt · do/QLDX_06.md
