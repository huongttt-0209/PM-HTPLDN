# Danh sách bug CÒN FAIL trong file UAT đối tác

> **Ngày lọc:** 2026-07-31 · **Nguồn:** file đối tác `1dJat1cc68…` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340) · **Chỉ đọc, không ghi gì lên sheet.**

## Cách lọc

Đối tác test **2 vòng**. Kết quả **vòng 2 là kết quả có hiệu lực**; vòng 2 để trống nghĩa là **chưa được xác nhận hết lỗi**, không phải đã pass. Toàn bộ 1635 dòng được soi **từng dòng một** — 724 dòng có khả năng là bug được chấm thủ công, 911 dòng Pass sạch vòng 1 loại bằng máy.

> **Lưu ý quan trọng:** ô `Trạng thái 2` trống **không luôn** nghĩa là chưa test lại. 65 dòng có TKM ghi rõ *"TKM retest &lt;ngày&gt;: lỗi chưa được fix"* mà vẫn bỏ trống ô trạng thái — đây là bug **đã được kiểm chứng lại**, không phải bug treo chờ test.

| Vòng 1 (`Trạng thái`) | Vòng 2 (`Trạng thái 2`) | Kết luận |
|---|---|---|
| Pass | — | Không phải bug → loại |
| Fail | Pass | Đã hết lỗi → loại (nhưng vẫn soi ngược tìm dòng chấm Pass oan) |
| Fail | Fail | **Còn lỗi** |
| Fail | (trống) | **Chưa test lại — vẫn treo** |
| N/R | — | Chưa chạy → loại (nhưng vẫn soi tìm lỗi bị giấu sau nhãn N/R) |

## Tổng hợp

| Nhóm | Số lượng |
|---|---:|
| ❌ Còn lỗi (vòng 2 vẫn Fail) | 20 |
| ⚠️ Mâu thuẫn — ô trạng thái nói ngược nội dung | 15 |
| 🕓 Chưa test lại vòng 2 (vẫn treo từ vòng 1) | 198 |
| 🔍 Gắn nhãn N/R nhưng có dấu vết lỗi | 95 |
| ❓ Mâu thuẫn nội tại — cần đối tác làm rõ | 8 |
| **TỔNG** | **336** |

### Theo tuần

| Nhóm | Tuần 1 | Tuần 2 | Tuần 3 | Tuần 4 | Tổng |
|---|---:|---:|---:|---:|---:|
| ❌ Còn lỗi (vòng 2 vẫn Fail) | 3 | 12 | 5 | 0 | **20** |
| ⚠️ Mâu thuẫn — ô trạng thái nói ngược nội dung | 1 | 6 | 8 | 0 | **15** |
| 🕓 Chưa test lại vòng 2 (vẫn treo từ vòng 1) | 5 | 25 | 135 | 33 | **198** |
| 🔍 Gắn nhãn N/R nhưng có dấu vết lỗi | 0 | 17 | 71 | 7 | **95** |
| ❓ Mâu thuẫn nội tại — cần đối tác làm rõ | 1 | 2 | 3 | 2 | **8** |
| **TỔNG** | **10** | **62** | **222** | **42** | **336** |

### Đối tác đã thực sự test lại lần 2 chưa?

Cột `Trạng thái 2` để trống **không đồng nghĩa chưa test lại**: có dòng TKM đã ghi rõ ngày test lại và kết luận vẫn lỗi, nhưng quên điền ô trạng thái. Tách bằng máy như sau:

| Đối tác đã test lại? | Số dòng | Ý nghĩa |
|---|---:|---|
| Có — vòng 2 chấm Fail | 20 | Bằng chứng mạnh nhất: test lại và chấm Fail. |
| Có — TKM ghi ngày test lại nhưng bỏ trống ô Trạng thái 2 | 65 | Đã test lại, kết luận vẫn lỗi, chỉ thiếu thao tác điền ô. |
| Có — vòng 2 chấm Pass | 10 | Chấm Pass nhưng nội dung ô nói ngược → cần xác nhận lại. |
| Chưa test lại | 241 | Chưa có cơ sở nào để coi là đã hết lỗi. |

### Theo module (top 15)

| Module | Số dòng còn lỗi |
|---|---:|
| `QLKCHTV` | 19 |
| `(dòng không có mã TC)` | 15 |
| `QLHSPLDN` | 14 |
| `QLTLPLCVV` | 12 |
| `QLDMTCTV` | 8 |
| `KHTHCTHTPLDN` | 8 |
| `QLNDTVVCG` | 7 |
| `QLDNDHTPL` | 7 |
| `NHSYC` | 6 |
| `QLDXDTTH` | 6 |
| `VVDHT` | 6 |
| `VVTTG` | 6 |
| `CPCTHTTLHDN` | 6 |
| `QLKTLBG` | 5 |
| `DKTGMLTVV` | 5 |

## ❌ Còn lỗi (vòng 2 vẫn Fail) — 20 dòng

Đối tác đã test lại lần 2 và **vẫn lỗi**. Đây là nhóm chắc chắn nhất.

| Tuần | Dòng | Mã TC | Mô tả | Lỗi | dev fix | Đã test lại? | Ghi chú |
|---|---:|---|---|---|---|---|---|
| Tuần 1 | 47 | `TKDGHQHTPL_02` | Biểu đồ hiệu quả hỗ trợ pháp lý | Điểm đánh giá hiệu quả hỗ trợ pháp lý theo thang 0–100 nhưng số liệu hiển thị trên màn hình vượt quá 100 | Reopent / dev done | ✔ đã test lại |  |
| Tuần 1 | 96 | `TKHDVMTH_07` | Kiểm tra lọc theo trạng thái | Lọc trạng thái Tiếp nhận nhưng danh sách vẫn trả về cả bản ghi Đang xử lý lẫn Tiếp nhận | dev done / dev done | ✔ đã test lại |  |
| Tuần 1 | 172 | `QLCHVMDXL_06` | Xem danh sách đã xử lý — Read-only | Các tab Đã duyệt, Công khai, Hoàn thành hiển thị bảng danh sách thiếu cột Nội dung | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 258 | `DKTGKH_12` | Tải lên tệp Excel | Nạp tệp Excel đăng ký báo Email không hợp lệ dù dữ liệu hợp lệ. | Reopent / dev done | ✔ đã test lại |  |
| Tuần 2 | 274 | `QLKTLBG_02` | Kiểm tra hiển thị bảng danh sách | Bảng danh sách bài giảng thiếu các cột Ảnh xem trước, Lĩnh vực, Người tạo. | Resoved / dev done | ✔ đã test lại |  |
| Tuần 2 | 326 | `QLGVTG_07` | Xem chi tiết | Tab Thông tin trong màn hình Xem chi tiết giảng viên vẫn cho phép chỉnh sửa. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 382 | `QLTVV_02` | Kiểm tra hiển thị bảng danh sách | Cột Điểm ĐG tràn đè cột Trạng thái, hiển thị không đồng nhất; nút Xem, Sửa bị xuống dòng. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 402 | `QLTVV_24` | Sửa Dữ liệu hợp lệ | Xóa file ảnh chân dung đính kèm báo Lỗi hệ thống. Vui lòng thử lại sau. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 415 | `DKTGMLTVV_02` | Kiểm tra hiển thị Nhóm 1 Thông tin cá nhân | Nhóm 1 Thông tin cá nhân ứng viên thiếu trường Đơn vị quản lý. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 416 | `DKTGMLTVV_03` | Kiểm tra hiển thị Nhóm 2 Thông tin nghề nghiệp | Nhóm 2 Thông tin chuyên môn hiển thị nhiều trường hơn mức SRS quy định. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 428 | `CNHSNLTVV_02` | Kiểm tra hiển thị các trường thông tin | Màn hình chi tiết khác màn hình cập nhật; trường Mô tả kinh nghiệm không hiển thị giá trị hiện tại. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 432 | `QLHSTVV_03` | Kiểm tra hiển thị Thẻ "Hồ sơ" nội dung chỉ xem, tổ chức thành 5 nhóm … | Nhóm 2 thừa trường Số quyết định công nhận; Nhóm 3 Tổ chức thừa trường Địa bàn. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 433 | `QLHSTVV_05` | Kiểm tra hiển thị thẻ "Thẩm định" khi người dùng là Người hỗ trợ hoặc… | Nhấn Xem chi tiết hồ sơ, hệ thống điều hướng sang màn hình 403 Forbidden. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 445 | `TDHSTVV_08` | Lưu nháp | Lưu nháp không lưu giá trị mà chuyển trạng thái bản ghi sang Đang thẩm định. | dev done / dev done | ✔ đã test lại |  |
| Tuần 2 | 450 | `TDHSTVV_14` | Gửi kết quả thẩm định Kết luận "Không đạt" | Từ chối hồ sơ: Người hỗ trợ không nhận được thông báo kèm lý do. | dev done / dev done | ✔ đã test lại |  |
| Tuần 3 | 563 | `XNTGHTVV_03` | Từ chối thành công | Từ chối tham gia vụ việc xong, cán bộ nghiệp vụ phụ trách không nhận được thông báo kèm lý do từ chối. | dev done | ✔ đã test lại |  |
| Tuần 3 | 617 | `QLHSDNHTCP_03` | Kiểm tra Cột dữ liệu trong bảng kết quả | Bảng danh sách: dữ liệu cột Mức cảnh báo thời hạn bị tràn sang cột Ngày nộp. | dev done | ✔ đã test lại |  |
| Tuần 3 | 736 | `LKHDG_16` | "Sửa" | Sửa đợt đánh giá: không hiển thị danh sách tệp đính kèm dù dữ liệu tồn tại. | dev done | ✔ đã test lại |  |
| Tuần 3 | 1209 | `QLDKTK_01` | Quản lý đăng ký tài khoản trên hệ thống | Đăng ký tài khoản báo Mã số thuế đã tồn tại trong hệ thống dù mã số thuế chưa tồn tại. | — | ✔ đã test lại |  |
| Tuần 3 | 1449 | `QLNDTVVCG_23` | Phân công thành công | Phân công chuyên gia xong, hệ thống không gửi thông báo tới doanh nghiệp về việc yêu cầu tư vấn đã được phân … | Resoved | ✔ đã test lại |  |

## ⚠️ Mâu thuẫn — ô trạng thái nói ngược nội dung — 15 dòng

Ô `Trạng thái 2` ghi Pass (hoặc để trống) nhưng chữ trong ô kết quả/phản hồi lại mô tả lỗi còn tồn tại. **Cần đối tác xác nhận lại.**

| Tuần | Dòng | Mã TC | Mô tả | Lỗi | dev fix | Đã test lại? | Ghi chú |
|---|---:|---|---|---|---|---|---|
| Tuần 1 | 116 | `QLTNXLHDVM_07` | Xem danh sách đã xử lý — Read-only | Tab Hoàn thành không gồm DA_DUYET và CONG_KHAI như kỳ vọng; dev coi là yêu cầu cải tiến, chưa fix | dev done | ✔ đã test lại | DEV phản hồi lần 1 nói lệch kỳ vọng và đề xuất cải tiến, nh… |
| Tuần 2 | 399 | `QLTVV_20` | Kiểm tra hiển thị và các nút tương tác khi tải tệp lên hệ thống thành… | Danh sách tệp đã tải không hiển thị dung lượng và các nút xem, tải lại. | dev done | ✔ đã test lại | Trạng thái 2=Pass nhưng Kết quả thực tế lần 2 vẫn ghi nguyê… |
| Tuần 2 | 449 | `TDHSTVV_13` | Gửi kết quả thẩm định Kết luận "Yêu cầu bổ sung" | Gửi kết luận Yêu cầu bổ sung: không hiển thị thông báo, Người hỗ trợ không nhận thông báo kèm lý do. | Reopent | ✔ đã test lại | Trạng thái 2 trống nhưng TKM ghi đã retest 25/7 và lỗi vẫn … |
| Tuần 2 | 454 | `PDHSTVV_01` | CB Phê duyệt xem xét và phê duyệt hồ sơ đã thẩm định để công nhận Tư … | Phê duyệt xong hồ sơ về trạng thái Chờ kích hoạt tài khoản, không gửi thông báo cho chủ hồ sơ. | Resoved | ✘ chưa | TKM ghi uc này pass nhưng Trạng thái=Fail; dòng PDHSTVV_06 … |
| Tuần 2 | 509 | `NHSYC_02` | Kiểm tra hiển thị các trường thông tin trong form nhập thủ công | Form nhập hồ sơ sai thiết kế: Loại hình hỗ trợ 6 giá trị, Lĩnh vực thiếu Khác, thiếu Thời điểm phát sinh. | Reopent | ✔ đã test lại | Trạng thái 2 trống nhưng TKM ghi retest 29/7 lỗi vẫn chưa đ… |
| Tuần 2 | 512 | `NHSYC_05` | Kiểm tra giới hạn ký tự nhập các trường thông tin | Nội dung vụ việc cho phép nhập tối đa 50.000 ký tự, vượt giới hạn 10.000 ký tự. | dev done | ✔ đã test lại | Trạng thái 2=Pass nhưng kết quả lần 2 vẫn ghi 50.000 ký tự,… |
| Tuần 2 | 529 | `KTHSYCHTPL_11` | Kiểm tra nút chức năng Hoàn tất kiểm tra khi chọn kết luận Đạt | Màn hình không có nút Hoàn tất kiểm tra, chỉ hiển thị nút Kiểm tra lại. | dev done | ✔ đã test lại | Trạng thái 2 trống nhưng TKM ghi retest 29/7 lỗi chưa được … |
| Tuần 3 | 792 | `PDBCDG_01` | Lãnh đạo CQQLNN xem xét và phê duyệt báo cáo đánh giá. | Phê duyệt báo cáo đánh giá: không gửi thông báo cho CBNV, thông báo thành công thiếu nội dung Đợt đánh giá ho… | dev done | ✔ đã test lại | TKM phản hồi lần 1 retest 27/7 ghi Lỗi chưa được fix nhưng … |
| Tuần 3 | 795 | `PDBCDG_04` | Từ chối báo cáo thành công | Từ chối báo cáo đánh giá: hệ thống không gửi thông báo kèm lý do cho Cán bộ nghiệp vụ | dev done | ✔ đã test lại | TKM phản hồi lần 1 retest 27/7 ghi Lỗi chưa được fix nhưng … |
| Tuần 3 | 842 | `QLBMHD_03` | Kiểm tra nút chức năng "+ Thêm mới" | Form thêm biểu mẫu thiếu trường Cơ quan ban hành khi bật công tắc Công khai (phần tệp đính kèm đã pass) | dev done | ✔ đã test lại | TKM retest 27/7 lần 1 còn ghi thiếu trường Cơ quan ban hành… |
| Tuần 3 | 1204 | `QLDX_02` | Kiểm tra Hộp thoại xác nhận đăng xuất | Đăng xuất: hệ thống không hiển thị hộp thoại xác nhận Bạn có chắc muốn đăng xuất khỏi hệ thống | dev done | ✔ đã test lại | TKM retest 28/7 lần 1 vẫn ghi không hiển thị hộp thoại xác … |
| Tuần 3 | 1210 | `QLDKTK_02` | Kiểm tra Thông tin doanh nghiệp | Form đăng ký tài khoản thiếu trường Tệp đính kèm; trường Doanh thu VNĐ sai tên so với SRS là Doanh thu năm | dev done | ✔ đã test lại | TKM phản hồi lần 1 retest 28/7 ghi Lỗi chưa được fix nhưng … |
| Tuần 3 | 1211 | `QLDKTK_03` | Kiểm tra Thông tin tài khoản | Màn hình đăng ký thiếu trường Tên đăng nhập; thừa trường Họ và tên người đăng ký và Số điện thoại so với SRS | dev done | ✔ đã test lại | TKM phản hồi lần 1 retest 28/7 ghi Lỗi chưa được fix nhưng … |
| Tuần 3 | 1326 | `VVTLV_01` | Thống kê số lượng vụ việc theo từng lĩnh vực pháp lý (Lao động, Thuế,… | Báo cáo vụ việc theo lĩnh vực: số liệu biểu đồ và bảng tổng hợp không trùng khớp nhau | dev done | ✔ đã test lại | TKM phản hồi lần 1 retest 28/7 ghi Lỗi chưa được fix nhưng … |
| Tuần 3 | 1479 | `QLHSPLDN_01` | Quản lý các tài liệu, hồ sơ pháp lý liên quan của DNNVV trong quá trì… | Biểu mẫu thêm mới hồ sơ pháp lý thiếu trường Lĩnh vực pháp lý, Mô tả, Tệp đính kèm và thừa trường Số/ký hiệu. | — | ✘ chưa | TKM phản hồi lần 1 ghi uc pass nhưng Trạng thái vẫn Fail và… |

## 🕓 Chưa test lại vòng 2 (vẫn treo từ vòng 1) — 198 dòng

Vòng 1 Fail, vòng 2 đối tác **chưa test lại** nên chưa có cơ sở coi là đã hết lỗi.

| Tuần | Dòng | Mã TC | Mô tả | Lỗi | dev fix | Đã test lại? | Ghi chú |
|---|---:|---|---|---|---|---|---|
| Tuần 1 | 62 | `TMHDVMPL_12` | Upload JPG | Upload file JPG: kỳ vọng hệ thống báo lỗi nhưng thực tế upload thành công | dev done | ✘ chưa |  |
| Tuần 1 | 66 | `TMHDVMPL_16` | Tổng >100MB | Tải tệp tổng dung lượng vượt 100MB: kỳ vọng báo lỗi nhưng hệ thống không thông báo lỗi | dev done | ✘ chưa |  |
| Tuần 1 | 207 | `TTCTDTTH_17` | Đang thực hiện | Chương trình Đã duyệt có khóa học Đang diễn ra/Đã công khai nhưng không tự chuyển trạng thái sang Đang thực h… | dev done | ✘ chưa |  |
| Tuần 1 | 208 | `TTCTDTTH_18` | Hoàn thành | Chương trình Đã duyệt có khóa học Hoàn thành nhưng không tự chuyển trạng thái chương trình sang Hoàn thành | dev done | ✘ chưa |  |
| Tuần 1 | 243 | `QLDKDTTH_07` | Duyệt học viên khi khoá học đã đóng đăng ký | Duyệt học viên khi khóa học đã đóng đăng ký: hệ thống báo thành công thay vì từ chối thao tác | dev done | ✘ chưa |  |
| Tuần 2 | 247 | `DKTGKH_01` | Đăng ký tham gia các khóa học. | Khóa học đã Công khai và Đang diễn ra nhưng không hiển thị trên Chuyên trang để doanh nghiệp đăng ký. | — | ✘ chưa |  |
| Tuần 2 | 260 | `KTDGKQHT_02` | Kiểm tra dữ liệu hiển thị trong mỗi tab | Tab Kết quả kiểm tra thiếu các trường Số buổi có mặt, vắng có phép, vắng không phép, tổng số buổi. | — | ✘ chưa |  |
| Tuần 2 | 281 | `QLKTLBG_09` | Xem bài giảng/tài liệu chứa Slide | Xem bài giảng dạng Slide: hệ thống tải tệp xuống thay vì trình chiếu inline. | — | ✘ chưa |  |
| Tuần 2 | 300 | `QLNHCH_02` | Kiểm tra hiển thị Thẻ thống kê tổng quan | Màn hình Ngân hàng câu hỏi không hiển thị Thẻ thống kê tổng quan theo thiết kế. | Reopent / Resoved | ✘ chưa |  |
| Tuần 2 | 302 | `QLNHCH_04` | Kiểm tra nút chức năng Thêm mới | Form Thêm mới câu hỏi: trường Trạng thái hiển thị danh sách giá trị không đúng thiết kế. | Reopent / Resoved | ✘ chưa |  |
| Tuần 2 | 337 | `QLDXDTTH_01` | Quản lý các đề xuất tổ chức đào tạo/tập huấn từ các đơn vị/cá nhân kh… | Gửi đề xuất báo thành công nhưng đề xuất không hiển thị trên màn hình danh sách. | — | ✘ chưa |  |
| Tuần 2 | 339 | `QLDXDTTH_03` | Xem chi tiết đề xuất | Màn hình đề xuất đào tạo không có chức năng Xem chi tiết. | dev done | ✘ chưa |  |
| Tuần 2 | 342 | `QLDXDTTH_06` | Xóa đề xuất ở trạng thái "Mới" và do chính Doanh nghiệp hoặc Người hỗ… | Xóa đề xuất trạng thái Mới: hệ thống không hiển thị thông báo xóa thành công. | dev done | ✘ chưa |  |
| Tuần 2 | 345 | `QLDXDTTH_09` | Kiểm tra Doanh nghiệp/Người hỗ trợ nhận thông báo | Doanh nghiệp/Người hỗ trợ không nhận được thông báo; đề xuất không được cập nhật trạng thái. | Reopent / Resoved | ✘ chưa |  |
| Tuần 2 | 354 | `QLLKHDTBD_09` | Xuất Excel với điều kiện lọc | Xuất Excel không theo điều kiện lọc, hệ thống xuất toàn bộ danh sách bài giảng. | — | ✘ chưa |  |
| Tuần 2 | 360 | `PDKHDTTH_04` | Cán bộ phê duyệt khác cấp với người lập | Cán bộ khác cấp phê duyệt: hệ thống không hiển thị thông báo lý do từ chối. | — | ✘ chưa |  |
| Tuần 2 | 375 | `CBKQDTBD_01` | Cung cấp chức năng công bố kết quả, cập nhật kết quả vào tài khoản củ… | Màn hình chi tiết khóa học không có tab riêng Công bố kết quả. | — | ✘ chưa |  |
| Tuần 2 | 417 | `DKTGMLTVV_04` | Kiểm tra hiển thị Nhóm 3 Tổ chức và Mạng lưới | Nhóm 3 Lĩnh vực pháp luật và Tổ chức hiển thị nhiều trường hơn mức SRS quy định. | — | ✘ chưa |  |
| Tuần 2 | 418 | `DKTGMLTVV_05` | Kiểm tra hiển thị Nhóm 4 Tệp đính kèm | Nhóm 4 Hồ sơ đính kèm: Tệp bằng cấp/chứng chỉ, Tệp thẻ hành nghề - ô kết quả không nêu rõ lỗi. | — | ✘ chưa |  |
| Tuần 2 | 431 | `QLHSTVV_02` | Kiểm tra hiển thị Khu vực thông tin đầu trang (thẻ giới thiệu tư vấn … | Thẻ đầu trang hồ sơ tư vấn viên thiếu các trường Loại, Tổ chức tư vấn, Lĩnh vực pháp luật. | Reopent / Resoved | ✘ chưa |  |
| Tuần 2 | 459 | `PDHSTVV_06` | Phê duyệt thành công | Phê duyệt xong hồ sơ về trạng thái Chờ kích hoạt tài khoản, không gửi thông báo cho chủ hồ sơ. | Reopent / Resoved | ✘ chưa |  |
| Tuần 2 | 461 | `PDHSTVV_08` | Từ chối khi nhập lý do hợp lệ | Từ chối hồ sơ: hệ thống không gửi thông báo đến Cán bộ nghiệp vụ đã thẩm định. | dev done | ✘ chưa |  |
| Tuần 2 | 462 | `CNDSMLTVV_01` | Thực hiện cập nhật danh sách các tư vấn viên đã được phê duyệt lên Cổ… | Không mở cửa sổ nhập mô tả công khai, chỉ báo Mô tả công khai là bắt buộc. | — | ✘ chưa |  |
| Tuần 2 | 473 | `DGTVV_05` | Kiểm tra hiển thị thông báo lỗi khi bỏ trống trường bắt buộc | Bỏ trống trường Vụ việc liên kết nhưng hệ thống không hiển thị thông báo lỗi. | Resoved | ✘ chưa |  |
| Tuần 2 | 478 | `QLLSHTCTVV_03` | Kiểm tra hiển thị Cột dữ liệu trong bảng danh sách vụ việc | Cột Đánh giá tràn màn hình; bảng danh sách vụ việc thiếu cột Trạng thái. | — | ✘ chưa |  |
| Tuần 2 | 479 | `QLLSHTCTVV_04` | Kiểm tra các trường thông tin tìm kiếm | Danh sách chọn Trạng thái thiếu giá trị so với định nghĩa của nhóm Quản lý vụ việc. | — | ✘ chưa |  |
| Tuần 2 | 508 | `NHSYC_01` | Cung cấp giao diện cho CB Nghiệp vụ nhập hồ sơ yêu cầu hỗ trợ pháp lý… | Tạo hồ sơ vụ việc báo lỗi ngayTiepNhan must be a valid ISO 8601 date string. | — | ✘ chưa |  |
| Tuần 2 | 514 | `NHSYC_07` | Kiểm tra chức năng Lưu nháp | Lưu nháp vẫn bắt buộc nhập đủ trường và không giữ nguyên màn hình sau khi lưu. | Resoved | ✘ chưa |  |
| Tuần 2 | 544 | `QLHSVV_07` | Tải tệp | Nhấn biểu tượng Tải xuống, hệ thống mở màn hình xem chi tiết thay vì tải tệp. | — | ✘ chưa |  |
| Tuần 2 | 548 | `TKHSYCHTPL_03` | Tìm kiếm bộ lọc có kết quả | Lọc Mức SLA Sắp hết hạn, hệ thống hiển thị thông báo lỗi. | — | ✘ chưa |  |
| Tuần 3 | 564 | `XNTGHTVV_04` | Xác nhận thành công | Xác nhận tham gia vụ việc xong, cán bộ nghiệp vụ phụ trách không nhận được thông báo. | dev done | ✔ đã test lại |  |
| Tuần 3 | 570 | `TBKQTNHS_01` | Cung cấp chức năng gửi thông báo kết quả kiểm tra hồ sơ (Đạt/Không đạ… | Màn hình không cung cấp chức năng gửi thông báo kết quả kiểm tra hồ sơ Đạt/Không đạt cho doanh nghiệp. | Resoved | ✘ chưa |  |
| Tuần 3 | 575 | `PDHSVV_02` | Phê duyệt thành công | Phê duyệt hồ sơ: không gửi thông báo cho cán bộ nghiệp vụ phụ trách; hiển thị sai thông tin Người duyệt. | dev done | ✔ đã test lại |  |
| Tuần 3 | 592 | `CNKQHT_03` | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết quả hỗ trợ | Nhóm 6 Kết quả hỗ trợ: thiếu trường Tệp kết quả, thừa trường Kết luận, nội dung giới hạn 5000 ký tự thay vì 1… | dev done | ✔ đã test lại |  |
| Tuần 3 | 596 | `CNKQHT_07` | Cập nhật thành công | Cập nhật kết quả hỗ trợ thành công nhưng cán bộ nghiệp vụ không nhận được thông báo. | — | ✘ chưa |  |
| Tuần 3 | 598 | `CNKQVV_02` | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết luận cuối | Nhóm 6 Kết luận cuối: tên nút chức năng và các trường thông tin không giống thiết kế. | dev done | ✔ đã test lại |  |
| Tuần 3 | 603 | `DGKQHTVV_01` | Cung cấp chức năng để CB Nghiệp vụ hoặc DNNVV đánh giá chất lượng của… | Không hiển thị nút Đánh giá kết quả hỗ trợ vụ việc dù bản ghi đang ở trạng thái phù hợp. | dev done | ✔ đã test lại |  |
| Tuần 3 | 697 | `QLDNDHTPL_13` | Thêm mới Nếu trường Tỉnh/Thành phố chưa nhập | Thêm mới doanh nghiệp: trường Tỉnh/Thành phố không tự đặt mặc định theo đơn vị của cán bộ đăng nhập. | dev done | ✔ đã test lại |  |
| Tuần 3 | 701 | `QLDNDHTPL_17` | Sắp xếp theo cột | Danh sách doanh nghiệp: bấm tiêu đề cột không sắp xếp tăng dần hay giảm dần. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 707 | `QLDNDHTPL_23` | Kiểm tra hiển thị Nhóm 1 — Thông tin doanh nghiệp (thẻ "Thông tin cơ … | Chi tiết doanh nghiệp: các trường Nhóm 1 Thông tin doanh nghiệp hiển thị không giống thiết kế. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 708 | `QLDNDHTPL_24` | Kiểm tra hiển thị Nhóm 2 — Người đại diện | Chi tiết doanh nghiệp: các trường Nhóm 2 Người đại diện hiển thị không giống thiết kế. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 709 | `QLDNDHTPL_25` | Kiểm tra hiển thị Nhóm 3 — Tiêu chí ưu tiên theo Nghị định 55/2019/NĐ… | Nhóm 3 Tiêu chí ưu tiên hiển thị Số lao động, Doanh thu, Tổng nguồn vốn — tài liệu yêu cầu đặt ở Nhóm 1. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 711 | `QLDNDHTPL_27` | Kiểm tra hiển thị Nhóm 5 — Chỉ số tổng hợp (chỉ hiển thị ở chế độ xem… | Màn hình chi tiết doanh nghiệp không hiển thị Nhóm 5 Chỉ số tổng hợp. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 712 | `QLDNDHTPL_28` | Kiểm tra hiển thị Nhóm 6 — Danh sách vụ việc liên kết (thẻ "Lịch sử h… | Nhóm 6 Lịch sử hỗ trợ: bảng vụ việc liên kết thiếu cột Lĩnh vực và Tư vấn viên. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 717 | `TKDNHTPL_02` | Kiểm tra Điều kiện tìm kiếm / bộ lọc | Bộ lọc doanh nghiệp: sai placeholder Lĩnh vực kinh doanh, không mặc định Tất cả, chỉ chọn được 1 lĩnh vực, th… | dev done | ✘ chưa |  |
| Tuần 3 | 730 | `LKHDG_10` | Lưu nháp thành công | Lưu nháp đợt đánh giá thành công nhưng hệ thống không giữ người dùng ở màn hình chi tiết đợt. | Resoved | ✘ chưa |  |
| Tuần 3 | 732 | `LKHDG_12` | Xuất Excel | Xuất Excel đợt đánh giá: sai tiêu chí lọc, thiếu cột Số vụ việc, Người tạo, Ngày tạo; nhiều cột hiển thị khôn… | dev done | ✔ đã test lại |  |
| Tuần 3 | 753 | `TLCTCDG_11` | Kiểm tra lưu thành công, tổng trọng số khác 100% | Lưu tiêu chí khi tổng trọng số khác 100%: hệ thống báo thành công, không hiển thị cảnh báo tổng trọng số hiện… | Reopent / InProcess | ✘ chưa |  |
| Tuần 3 | 766 | `PCNTHDG_11` | Trình phê duyệt thành công | Trình phê duyệt phân công đánh giá: không gửi thông báo cho cán bộ phê duyệt cùng đơn vị. | dev done | ✔ đã test lại |  |
| Tuần 3 | 767 | `PDPCDG_01` | Lãnh đạo CQQLNN phê duyệt danh sách người thực hiện đánh giá. | Phê duyệt phân công đánh giá xong, cán bộ nghiệp vụ không nhận được thông báo. | dev done | ✔ đã test lại |  |
| Tuần 3 | 771 | `PDPCDG_05` | Từ chối thành công | Từ chối phân công đánh giá: hệ thống không gửi thông báo kèm lý do từ chối. | dev done | ✔ đã test lại |  |
| Tuần 3 | 772 | `CVVDG_01` | Lựa chọn các vụ việc cụ thể để tiến hành kiểm tra, đánh giá chất lượn… | Lưu vụ việc vào đợt đánh giá: nội dung thông báo hiển thị không giống thiết kế. | Resoved | ✘ chưa |  |
| Tuần 3 | 773 | `CVVDG_02` | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (t… | Bảng chọn vụ việc đánh giá thiếu cột Tên doanh nghiệp, Ngày hoàn thành, Cảnh báo trùng đợt. | Resoved | ✘ chưa |  |
| Tuần 3 | 789 | `TPDBC_01` | Cung cấp quy trình để CB Nghiệp vụ trình Lãnh đạo CQQLNN phê duyệt bá… | Trình phê duyệt báo cáo đánh giá xong, cán bộ phê duyệt không nhận được thông báo. | — | ✘ chưa |  |
| Tuần 3 | 807 | `QLTMBMHD_10` | Kiểm tra hiển thị nút chức năng Sửa" thư mục | Nút Sửa thư mục vẫn hiển thị với thư mục đang ở trạng thái Công khai. | Resoved | ✘ chưa |  |
| Tuần 3 | 814 | `QLTMBMHD_17` | Kiểm tra hiển thị nút chức năng Xóa hàng loạt | Xóa hàng loạt: vẫn cho tích chọn thư mục Công khai và thư mục còn chứa biểu mẫu. | Resoved | ✘ chưa |  |
| Tuần 3 | 827 | `TKTMBMHD_07` | Xóa bộ lọc | Xóa bộ lọc thư mục biểu mẫu: hệ thống không đưa tab phân loại về Tất cả. | Reopent | ✘ chưa |  |
| Tuần 3 | 841 | `QLBMHD_02` | Kiểm tra hiển thị các trường thông tin | Danh sách biểu mẫu thiếu ô chọn biểu mẫu và thiếu cột Cơ quan ban hành, Định dạng. | dev done | ✔ đã test lại |  |
| Tuần 3 | 851 | `QLBMHD_12` | Kiểm tra hiển thị nút chức năng Sửa biểu mẫu | Nút Sửa biểu mẫu vẫn hiển thị với biểu mẫu đang ở trạng thái Công khai. | Resoved | ✘ chưa |  |
| Tuần 3 | 868 | `IBMHD_02` | Kiểm tra hiển thị các trường thông tin | Màn hình nhập biểu mẫu hàng loạt thiếu ô Tệp Excel mô tả dữ liệu và nút Tải mẫu Excel. | Resoved | ✘ chưa |  |
| Tuần 3 | 869 | `IBMHD_03` | Kiểm tra chức năng "Tải mẫu Excel" | Màn hình nhập hàng loạt không có nút Tải mẫu Excel để tải tệp XLSX mẫu. | Resoved | ✘ chưa |  |
| Tuần 3 | 958 | `QLDMCQDVQL_05` | Tìm kiếm không có kết quả | Tìm kiếm danh mục không có kết quả: hệ thống không hiển thị thông báo Không tìm thấy mục danh mục phù hợp. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 973 | `QLDMTCTV_02` | Kiểm tra hiển thị Cột dữ liệu trong bảng kết quả | Bảng danh mục tiêu chí tư vấn viên thiếu ô chọn và cột STT. | — | ✘ chưa |  |
| Tuần 3 | 976 | `QLDMTCTV_05` | Chọn thẻ trạng thái | Thẻ trạng thái không hiển thị số đếm; thẻ Mới đăng ký thiếu nhãn đỏ; thẻ Chờ phê duyệt vẫn hiện với CBNV. | — | ✘ chưa | Dòng bị bỏ trống cột Tuần trên sheet; cột Trạng thái dev fi… |
| Tuần 3 | 977 | `QLDMTCTV_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | Popup thêm mới thiếu trường Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm. | — | ✘ chưa |  |
| Tuần 3 | 980 | `QLDMTCTV_09` | Kiểm tra các trường thông tin trên màn hình/popup sửa | Popup sửa thiếu trường Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm. | — | ✘ chưa |  |
| Tuần 3 | 996 | `QLDMLDN_13` | Kiểm tra các trường thông tin trên màn hình/popup sửa | Popup sửa loại doanh nghiệp thừa trường Danh mục cha; trường Doanh thu bị đánh dấu bắt buộc dù tài liệu không… | dev done | ✘ chưa |  |
| Tuần 3 | 1037 | `QLCHTHXLHS_02` | Kiểm tra hiển thị Thanh thẻ (tab) ở đầu trang | Cấu hình xử lý hồ sơ: thiếu thẻ Phân công mặc định và Quy trình hỗ trợ, thừa thẻ Quản lý ngày lễ. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1038 | `QLCHTHXLHS_03` | Kiểm tra hiển thị Bảng cấu hình SLA (thẻ "Thời hạn xử lý / SLA") | Bảng cấu hình SLA sai thiết kế: tách đôi cột Loại yêu cầu, gộp 2 mức cảnh báo, thiếu cột Quá hạn (%). | Reopent | ✘ chưa |  |
| Tuần 3 | 1042 | `QLCHTHXLHS_07` | Kiểm tra màn hình/popup chỉnh sửa khi nhấn vàp biểu tượng chỉnh sửa t… | Popup sửa SLA thiếu trường Số ngày bổ sung tối đa và thừa trường Hệ số quá hạn. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1067 | `QLDMTCDGHTCP_06` | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | Popup thêm mới sai nhãn trường Tỷ lệ phần trăm, Mức chi phí tối đa và thừa trường Danh mục cha. | Reopent / dev done | ✘ chưa |  |
| Tuần 3 | 1073 | `QLDMTCDGHTCP_12` | Kiểm tra các trường thông tin trên màn hình/popup sửa | Popup sửa sai nhãn trường Tỷ lệ phần trăm, Mức chi phí tối đa và thừa trường Danh mục cha. | Reopent / dev done | ✘ chưa |  |
| Tuần 3 | 1108 | `QLVT_14` | Sắp xếp theo cột | Danh sách vai trò: bấm tiêu đề cột không sắp xếp được tăng dần hay giảm dần. | Resoved | ✘ chưa |  |
| Tuần 3 | 1114 | `QLTKND_03` | Kiểm tra Thẻ trạng thái (tab nhanh) | Quản lý tài khoản hiển thị 6 thẻ tab thay vì 5; thẻ Chờ kích hoạt không có màu nhấn. | Reopent | ✘ chưa |  |
| Tuần 3 | 1117 | `QLTKND_06` | Tìm kiếm không có kết quả | Tìm kiếm tài khoản không có kết quả: hệ thống hiển thị Trống thay vì Không tìm thấy tài khoản phù hợp. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1136 | `QLTKND_25` | Sắp xếp theo cột | Danh sách tài khoản: bấm tiêu đề cột không sắp xếp được tăng dần hay giảm dần. | Resoved | ✘ chưa |  |
| Tuần 3 | 1138 | `QLTKND_27` | Gửi liên kết đặt lại mật khẩu | Màn hình quản lý tài khoản không có nút Gửi liên kết đặt lại mật khẩu. | Resoved | ✘ chưa |  |
| Tuần 3 | 1203 | `QLDX_01` | Quản lý quy trình kết thúc phiên làm việc của người dùng. | Đăng xuất: hệ thống về trang đăng nhập nhưng không hiển thị thông báo Đăng xuất thành công. | dev done | ✔ đã test lại |  |
| Tuần 3 | 1205 | `QLDX_03` | Tự động đăng xuất khi hết phiên | Hết phiên: hệ thống không hiển thị hộp thoại cảnh báo sắp hết phiên dù để idle 30 phút. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1217 | `QLDKTK_09` | Kích hoạt và đặt mật khẩu lần đầu | Kích hoạt tài khoản: hệ thống không gửi liên kết đặt mật khẩu lần đầu đến thư điện tử. | Resoved | ✘ chưa |  |
| Tuần 3 | 1230 | `SLHDVM_03` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | Báo cáo số lượng hỏi đáp: bảng kết quả hiển thị không giống thiết kế. | Resoved | ✘ chưa |  |
| Tuần 3 | 1233 | `SLHDVM_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1234 | `SLHDVM_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1235 | `SLHDVM_08` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1236 | `SLHDVM_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1240 | `VVDTN_04` | Kiểm tra hiển thị Biểu đồ và bảng kết quả | Báo cáo vụ việc đã tiếp nhận thiếu biểu đồ tròn theo lĩnh vực; bảng tổng hợp thiếu cột Theo kênh, Theo lĩnh v… | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1242 | `VVDTN_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1243 | `VVDTN_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1244 | `VVDTN_08` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1245 | `VVDTN_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1246 | `VVDHT_01` | Thống kê số lượng vụ việc đang được xử lý theo đơn vị, chuyên gia. | Đơn vị có dữ liệu nhưng khi chọn người hỗ trợ, hệ thống báo không có dữ liệu báo cáo cho kỳ đã chọn. | dev done | ✔ đã test lại |  |
| Tuần 3 | 1248 | `VVDHT_03` | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | Chỉ số tổng hợp nhanh thiếu các chỉ số Sắp hết hạn, Quá hạn, Quá hạn nghiêm trọng. | Resoved | ✘ chưa |  |
| Tuần 3 | 1251 | `VVDHT_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1252 | `VVDHT_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1253 | `VVDHT_08` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1254 | `VVDHT_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1260 | `VVDHTHT_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1261 | `VVDHTHT_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1262 | `VVDHTHT_08` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1263 | `VVDHTHT_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1264 | `VVTTG_01` | Thống kê diễn biến số lượng vụ việc theo các mốc thời gian (ngày, tuầ… | Báo cáo vụ việc theo thời gian: số liệu thống kê hiển thị không chính xác. | dev done | ✔ đã test lại |  |
| Tuần 3 | 1265 | `VVTTG_02` | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | Màn hình hiển thị chỉ số tổng hợp trong khi tài liệu quy định báo cáo này không có chỉ số tổng hợp riêng. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1268 | `VVTTG_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1269 | `VVTTG_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1270 | `VVTTG_07` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1271 | `VVTTG_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1275 | `CLDTBDDDR_04` | Kiểm tra hiển thị cột kết quả | Biểu đồ cột vẽ theo Đơn vị thay vì theo hình thức, thiếu biểu đồ đường xu hướng, bảng tổng hợp sai cột. | Resoved | ✘ chưa |  |
| Tuần 3 | 1277 | `CLDTBDDDR_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1278 | `CLDTBDDDR_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1279 | `CLDTBDDDR_08` | Kiểm tra chức năng In báo cáo | Màn hình báo cáo không hiển thị nút In báo cáo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1280 | `CLDTBDDDR_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình báo cáo không hiển thị nút Xóa bộ lọc. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1284 | `LDTBDDDR_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | Biểu đồ cột vẽ theo Đơn vị trong khi tài liệu yêu cầu vẽ theo hình thức đào tạo. | Resoved | ✘ chưa |  |
| Tuần 3 | 1286 | `LDTBDDDR_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1287 | `LDTBDDDR_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1293 | `CGTVPL_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | Biểu đồ tròn vẽ theo Đơn vị thay vì theo loại; biểu đồ cột không hiển thị số lượng chuyên gia dù có dữ liệu. | Resoved | ✘ chưa |  |
| Tuần 3 | 1295 | `CGTVPL_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1296 | `CGTVPL_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1304 | `DGHQHTPL_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1305 | `DGHQHTPL_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1313 | `CLDTBDPL_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1314 | `CLDTBDPL_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1322 | `VVTDVQL_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1323 | `VVTDVQL_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1330 | `VVTLV_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1331 | `VVTLV_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1338 | `VVTLHDN_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1339 | `VVTLHDN_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1346 | `VVTTGCT_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1347 | `VVTTGCT_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1355 | `CPHTCT_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1356 | `CPHTCT_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1361 | `CPCTHTTDVQL_03` | Kiểm tra hiển thị Chỉ số tổng hợp | Màn hình hiển thị chỉ số tổng hợp trong khi tài liệu quy định báo cáo này không có chỉ số tổng hợp riêng. | Resoved | ✘ chưa |  |
| Tuần 3 | 1364 | `CPCTHTTDVQL_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1365 | `CPCTHTTDVQL_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1379 | `CPCTHTTLHDN_03` | Kiểm tra hiển thị Chỉ số tổng hợp | Màn hình hiển thị chỉ số tổng hợp trong khi tài liệu quy định báo cáo này không có chỉ số tổng hợp riêng. | Resoved | ✘ chưa |  |
| Tuần 3 | 1380 | `CPCTHTTLHDN_04` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | Biểu đồ cột vẽ thêm nhiều nhóm số liệu ngoài tài liệu và trục tung hiển thị toàn bộ giá trị 0. | Reopent / Resoved | ✘ chưa |  |
| Tuần 3 | 1382 | `CPCTHTTLHDN_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1383 | `CPCTHTTLHDN_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1388 | `CPCTHTTTG_03` | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | Biểu đồ đường chi phí theo thời gian: số liệu ở trục tung hiển thị toàn bộ giá trị 0. | Reopent / InProcess | ✘ chưa |  |
| Tuần 3 | 1390 | `CPCTHTTTG_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1391 | `CPCTHTTTG_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1399 | `SLCTHT_06` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1400 | `SLCTHT_07` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1404 | `CTTDVQL_02` | Kiểm tra hiển thị Chỉ số tổng hợp | Màn hình hiển thị chỉ số tổng hợp trong khi tài liệu quy định báo cáo này không có chỉ số tổng hợp riêng. | Resoved | ✘ chưa |  |
| Tuần 3 | 1406 | `CTTDVQL_04` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1407 | `CTTDVQL_05` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1412 | `CTTLV_03` | Kiểm tra hiển thị Chỉ số tổng hợp | Màn hình hiển thị chỉ số tổng hợp trong khi tài liệu quy định báo cáo này không có chỉ số tổng hợp riêng. | Resoved | ✘ chưa |  |
| Tuần 3 | 1414 | `CTTLV_05` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1415 | `CTTLV_06` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1421 | `CTTTG_04` | Kiểm tra chức năng Xuất excel | Bấm Xuất Excel thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1422 | `CTTTG_05` | Kiểm tra chức năng Xuất PDF | Bấm Xuất PDF thất bại, hệ thống báo Không thể tạo file xuất, vui lòng thử lại. | Reopent | ✔ đã test lại |  |
| Tuần 3 | 1453 | `QLNDTVVCG_27` | Kiểm tra nút chức năng Hoàn thành tư vấn | Hoàn thành tư vấn: hệ thống không gửi thông báo tới cán bộ phê duyệt cùng đơn vị. | dev done | ✘ chưa |  |
| Tuần 3 | 1462 | `QLNDTVVCG_36` | Xác nhận hủy Với trạng thái "Đang tư vấn" | Hủy yêu cầu Đang tư vấn: chuyển thẳng sang Đã hủy và báo Đã hủy yêu cầu, bỏ qua bước chờ duyệt hủy. | dev done | ✘ chưa |  |
| Tuần 3 | 1466 | `QLNDTVVCG_40` | Xuất Excel | Xuất Excel yêu cầu tư vấn: tên tệp sai thiết kế và thiếu cột Doanh nghiệp, Chuyên gia, Lĩnh vực. | dev done | ✘ chưa |  |
| Tuần 3 | 1470 | `TKNDTVVCG_03` | Tìm kiếm theo tên DN | Tìm kiếm theo tên doanh nghiệp không ra kết quả, hệ thống báo Không có nội dung tư vấn chuyên sâu nào. | dev done | ✘ chưa |  |
| Tuần 3 | 1480 | `QLHSPLDN_02` | Bảng danh sách hồ sơ pháp lý | Bảng danh sách hồ sơ pháp lý thiếu cột Lĩnh vực pháp lý, Nguồn, Có tệp đính kèm và thừa cột Số/ký hiệu. | dev done | ✘ chưa |  |
| Tuần 3 | 1481 | `QLHSPLDN_03` | Biểu mẫu thêm mới / chỉnh sửa hồ sơ pháp lý | Biểu mẫu thêm mới hồ sơ pháp lý thiếu trường Lĩnh vực pháp lý, Mô tả, Tệp đính kèm và thừa trường Số/ký hiệu. | dev done | ✘ chưa |  |
| Tuần 3 | 1498 | `QLTLPLCVV_02` | Bảng danh sách tư liệu pháp lý | Bảng danh sách tư liệu pháp lý thiếu cột Ngày tạo và Người tạo. | dev done | ✘ chưa |  |
| Tuần 3 | 1499 | `QLTLPLCVV_03` | Kiểm tra điều kiện hiển thị nút chức năng Thêm mới | Nút Thêm mới tư liệu vẫn hiển thị với yêu cầu tư vấn ở trạng thái Đã duyệt và Hủy. | Resoved | ✘ chưa |  |
| Tuần 3 | 1503 | `QLTLPLCVV_07` | Kiểm tra điều kiện hiển thị nút chức năng Sửa | Tư liệu ở trạng thái Công khai vẫn hiển thị nút Sửa. | dev done | ✘ chưa |  |
| Tuần 3 | 1504 | `QLTLPLCVV_08` | Sửa thành công | Cửa sổ sửa tư liệu không hiển thị tệp đính kèm dù dữ liệu tồn tại. | dev done | ✘ chưa |  |
| Tuần 3 | 1505 | `QLTLPLCVV_09` | Sửa tư liệu đã chuyển sang "Công khai" | Sửa tư liệu đang công khai: thông báo sai nội dung và lộ tên trường kỹ thuật moTa, fileDinhKemIds. | dev done | ✘ chưa |  |
| Tuần 3 | 1507 | `QLTLPLCVV_11` | Xóa tư liệu đang ở trạng thái "Công khai" | Tư liệu ở trạng thái Công khai bị vô hiệu hóa nút Xóa, không thực hiện được thao tác xóa. | dev done | ✘ chưa |  |
| Tuần 3 | 1511 | `QLTLPLCVV_15` | Tải lên tệp đính kèm chứa mã độc | Tải lên tệp chứa mã độc: hệ thống chỉ báo Tải file thất bại, không nêu tệp chứa mã độc. | dev done | ✘ chưa |  |
| Tuần 3 | 1512 | `QLTLPLCVV_16` | Xóa tệp đính kèm thành công | Xóa tệp đính kèm: hệ thống không hiển thị hộp xác nhận trước khi xóa. | Resoved | ✘ chưa |  |
| Tuần 4 | 1525 | `QLKCHTV_02` | Điều kiện tìm kiếm / bộ lọc | Bộ lọc mặc định rỗng thay vì Tất cả; nguồn Nhập Excel hiển thị Import; thiếu trạng thái Nháp, thừa trạng thái… | dev done | ✘ chưa |  |
| Tuần 4 | 1526 | `QLKCHTV_03` | Cột dữ liệu trong bảng kết quả | Bảng kết quả thiếu cột Ô chọn hàng loạt và Câu trả lời; cột Điểm trung bình hiển thị sai tên là Đánh giá. | dev done | ✘ chưa |  |
| Tuần 4 | 1527 | `QLKCHTV_04` | Kiểm tra khi nhấn nút chức năng Thêm câu hỏi | Cửa sổ Thêm câu hỏi mới: nút Gửi duyệt hiển thị là Lưu; thiếu nút Lưu nháp. | dev done | ✘ chưa |  |
| Tuần 4 | 1533 | `QLKCHTV_10` | Có dòng hợp lệ, NSD bấm "Xác nhận nhập" | Sau khi nhập Excel, hệ thống hiển thị nguồn nhập là Import thay vì Nhập Excel. | dev done | ✘ chưa |  |
| Tuần 4 | 1535 | `QLKCHTV_12` | Xuất Excel | Xuất Excel kho câu hỏi: tên file thiếu giờ HHmm; thiếu cột Ngày cập nhật; nguồn hiển thị Import thay vì Nhập … | dev done | ✘ chưa |  |
| Tuần 4 | 1536 | `QLKCHTV_13` | Xuất Excel Không có dữ liệu | Lọc không có dữ liệu: hệ thống vẫn xuất file Excel đã xuất ở QLKCHTV_12, không báo Không có dữ liệu để xuất. | dev done | ✘ chưa |  |
| Tuần 4 | 1537 | `QLKCHTV_14` | Xem | Màn hình chi tiết câu hỏi thiếu thông tin Người tạo, Từ khóa, Lịch sử thẩm định. | dev done | ✘ chưa |  |
| Tuần 4 | 1539 | `QLKCHTV_16` | Kiểm tra chức năng Sửa | Cửa sổ Sửa câu hỏi: nút Gửi duyệt hiển thị là Lưu; thiếu nút Lưu nháp. | dev done | ✘ chưa |  |
| Tuần 4 | 1541 | `QLKCHTV_18` | Kiểm tra chức năng Bật/tắt hiệu lực | Cửa sổ xác nhận Bật/tắt hiệu lực không giống thiết kế. | dev done | ✘ chưa |  |
| Tuần 4 | 1545 | `QLKCHTV_22` | Cột dữ liệu trong bảng kết quả | Cột Ngày gửi chỉ hiển thị dd/mm/yyyy, thiếu giờ HH:mm. | dev done | ✘ chưa |  |
| Tuần 4 | 1546 | `QLKCHTV_23` | Xem | Phiên trạng thái Cán bộ trả lời: Xem chi tiết mở màn hình Trả lời ở chế độ chỉnh sửa thay vì chỉ xem. | dev done | ✘ chưa |  |
| Tuần 4 | 1547 | `QLKCHTV_24` | Trả lời | Phiên trạng thái Cán bộ trả lời không hiển thị nút Trả lời trên dòng, nhưng Xem chi tiết lại cho phép chỉnh s… | dev done | ✘ chưa |  |
| Tuần 4 | 1549 | `QLKCHTV_26` | Cột trái — Thông tin phiên tư vấn | Chi tiết phiên: lỗi thanh tiến trình ở trạng thái Mới; thiếu MST, thư điện tử, người gửi câu hỏi; thiếu Lịch … | dev done | ✘ chưa |  |
| Tuần 4 | 1554 | `QLKCHTV_31` | Chọn câu trả lời từ kho | Chọn câu trả lời từ kho: hệ thống không cảnh báo thay thế khi ô trả lời đã có nội dung tùy chỉnh. | dev done | ✘ chưa |  |
| Tuần 4 | 1555 | `QLKCHTV_32` | Xem chi tiết câu trả lời | Nhấn mã câu trả lời trong kết quả tra cứu, hệ thống không mở cửa sổ chi tiết. | dev done | ✘ chưa |  |
| Tuần 4 | 1558 | `QLKCHTV_35` | Đẩy sang Nhóm II | Màn hình trả lời phiên tư vấn nhanh không có nút Đẩy sang Nhóm II. | dev done | ✘ chưa |  |
| Tuần 4 | 1559 | `QLKCHTV_36` | Lưu nháp | Màn hình trả lời phiên tư vấn nhanh không có nút Lưu nháp. | dev done | ✘ chưa |  |
| Tuần 4 | 1560 | `QLKCHTV_37` | Xuất Excel đánh giá | Màn hình không có nút chức năng Xuất Excel đánh giá. | dev done | ✘ chưa |  |
| Tuần 4 | 1562 | `PDNDCHTV_01` | Quản lý phê duyệt câu hỏi. | Duyệt câu hỏi: cán bộ tạo câu hỏi không nhận được thông báo. | dev done | ✘ chưa |  |
| Tuần 4 | 1565 | `PDNDCHTV_04` | NSD xác nhận từ chối | Từ chối câu hỏi: trạng thái chuyển thành Bị từ chối thay vì Nháp; cán bộ tạo không nhận thông báo kèm lý do. | dev done | ✘ chưa |  |
| Tuần 4 | 1568 | `PDNDCHTV_07` | NSD xác nhận duyệt hàng loạt | Duyệt hàng loạt: cán bộ tạo câu hỏi không nhận được thông báo. | dev done | ✘ chưa |  |
| Tuần 4 | 1570 | `QLCKCHTV_02` | Kiểm tra khi nhấn nút chức năng Công khai | Cửa sổ Công khai câu hỏi không có trường bổ sung mô tả hiển thị trên chuyên trang. | dev done | ✘ chưa |  |
| Tuần 4 | 1575 | `TKCHTV_01` | Cung cấp công cụ tìm kiếm phản hồi trong kho câu hỏi/tư vấn nhanh. | Kho câu hỏi: tìm theo từ khóa vẫn trả toàn bộ bản ghi; Tư vấn nhanh báo Không có phiên tư vấn nhanh nào. | dev done | ✘ chưa |  |
| Tuần 4 | 1576 | `TKCHTV_02` | Tìm kiếm không có kết quả | Kho câu hỏi: tìm từ khóa không có kết quả nhưng hệ thống vẫn hiển thị toàn bộ bản ghi, không báo Không tìm th… | dev done | ✘ chưa |  |
| Tuần 4 | 1577 | `TKCHTV_03` | ↻ Xóa bộ lọc | Màn hình Kho câu hỏi không có nút Xóa bộ lọc. | dev done | ✘ chưa |  |
| Tuần 4 | 1609 | `KHTHCTHTPLDN_02` | Điều kiện tìm kiếm / bộ lọc | Bộ lọc danh sách chương trình thiếu trường tìm kiếm theo Đơn vị và Trạng thái. | dev done | ✘ chưa |  |
| Tuần 4 | 1610 | `KHTHCTHTPLDN_03` | Bảng danh sách chương trình | Danh sách chương trình không có cột Đợt báo cáo liên kết màn hình Đợt báo cáo định kỳ, chỉ hiển thị Số đợt BC. | Resoved | ✘ chưa |  |
| Tuần 4 | 1614 | `KHTHCTHTPLDN_07` | Xuất tệp danh sách | Tên tệp Excel xuất danh sách chương trình không đúng thiết kế DanhSachChuongTrinh_{YYYYMMDD_HHmm}.xlsx. | dev done | ✘ chưa |  |
| Tuần 4 | 1615 | `KHTHCTHTPLDN_08` | Hành động nhanh trên dòng | Hành động nhanh trên dòng không hiển thị: Tạm dừng khi Đang thực hiện, Kích hoạt khi Đã duyệt/Đã công bố, Sửa… | dev done | ✘ chưa |  |
| Tuần 4 | 1619 | `KHTHCTHTPLDN_12` | Trang Chi tiết chương trình (thẻ Thông tin chương trình) - Đầu trang | Chi tiết chương trình: thanh điều hướng thiếu mã, tiêu đề thiếu tên, bước 2 viết tắt Chờ PD, thiếu khối thông… | dev done | ✘ chưa |  |
| Tuần 4 | 1623 | `TKKHCTHTPL_01` | Tìm kiếm kế hoạch thực hiện chương trình hỗ trợ theo tên, đơn vị quản… | Tìm kiếm kế hoạch chương trình thiếu trường lọc theo đơn vị quản lý và lĩnh vực. | dev done | ✘ chưa |  |
| Tuần 4 | 1624 | `TKKHCTHTPL_02` | Tìm kiếm không có kết quả | Tìm kiếm không có kết quả: hệ thống hiển thị Trống thay vì thông báo Không tìm thấy chương trình phù hợp. | dev done | ✘ chưa |  |
| Tuần 4 | 1635 | `LBCKQTHCT_01` | Cung cấp công cụ để CB Nghiệp vụ lập báo cáo kết quả thực hiện chương… | Lập báo cáo kết quả chương trình báo lỗi 403 ERR-AUTH-VPD-00-02 với vai trò CB_NV_DP dù tài khoản đã được cấp… | dev done | ✘ chưa |  |

## 🔍 Gắn nhãn N/R nhưng có dấu vết lỗi — 95 dòng

Đối tác đánh dấu *chưa chạy* nhưng trong ô lại có mô tả lỗi — lỗi bị giấu sau nhãn N/R.

| Tuần | Dòng | Mã TC | Mô tả | Lỗi | dev fix | Đã test lại? | Ghi chú |
|---|---:|---|---|---|---|---|---|
| Tuần 2 | 263 | `KTDGKQHT_05` | Tải lên tệp Excel điểm danh | Danh sách không hiển thị mã học viên nhưng import Excel điểm danh lại bắt buộc có mã học viên | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 268 | `KTDGKQHT_10` | Tải lên tệp Excel Kết quả kiểm tra | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 290 | `QLKTLBG_18` | Xuất Excel với điều kiện lọc | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 291 | `QLKTLBG_19` | Xuất excel không có điều kiện lọc | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 292 | `QLKTLBG_20` | Xuất Excel với điều kiện lọc không có kết quả | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 341 | `QLDXDTTH_05` | Chỉnh sửa Đề xuất đã tiếp nhận | Bản ghi không cập nhật trạng thái dù cán bộ nghiệp vụ đã phê duyệt thành Đã tiếp nhận | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 343 | `QLDXDTTH_07` | Xóa Đề xuất đã tiếp nhận | Bản ghi không cập nhật trạng thái dù cán bộ nghiệp vụ đã phê duyệt thành Đã tiếp nhận | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 364 | `CKKHDTBD_01` | Đăng tải kế hoạch đào tạo đã được phê duyệt lên Cổng để các đối tượng… | Đăng tải kế hoạch lên Cổng thất bại, hệ thống báo Cổng PLQG chưa được cấu hình | — | ✘ chưa | N/R nhưng ô Kết quả thực tế + TKM mô tả lỗi sản phẩm |
| Tuần 2 | 425 | `DKTGMLTVV_13` | Gửi đăng ký khi Dữ liệu hợp lệ | Thiếu button Gửi đăng ký (chỉ có Lưu) và các trường thông tin không đúng thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 429 | `CNHSNLTVV_03` | Lưu thành công khi nhập dữ liệu hợp lệ | Màn hình chi tiết và màn hình cập nhật chưa đồng bộ dữ liệu với nhau | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 506 | `—` | Cung cấp giao diện cho DNNVV gửi hồ sơ yêu cầu hỗ trợ pháp lý trực tu… | Chức năng chưa được xây dựng - ghi nhận chức năng đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 2 | 516 | `NHSYC_09` | Kiểm tra doanh nghiệp tồn tại trong hệ thống (đủ mã số thuế và tên do… | Các trường thông tin trên màn hình không đúng thiết kế nên chưa kiểm thử được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 517 | `NHSYC_10` | Tự động tính điểm ưu tiên xử lý theo Nghị định 55/2019/NĐ-CP Điều 4. | Các trường thông tin trên màn hình không đúng thiết kế nên chưa kiểm thử được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 523 | `KTHSYCHTPL_05` | Kiểm tra hiển thị Nhóm 3 — Tài liệu Đính kèm | Nhập hồ sơ thủ công bị hệ thống báo lỗi nên không tạo được dữ liệu kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 524 | `KTHSYCHTPL_06` | Kiểm tra nút chức năng Xem tài liệu đính kèm | Nhập hồ sơ thủ công bị hệ thống báo lỗi nên không tạo được dữ liệu kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 525 | `KTHSYCHTPL_07` | Kiểm tra nút chức năng Tải tài liệu đính kèm | Nhập hồ sơ thủ công bị hệ thống báo lỗi nên không tạo được dữ liệu kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 2 | 545 | `QLHSVV_08` | Xem tệp | Nút Xem chi tiết hiển thị sai biểu tượng Tải xuống | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 580 | `—` | Cung cấp giao diện cho DNNVV nhận thông báo kết quả kiểm tra/tiếp nhậ… | Chức năng chưa được xây dựng - ghi nhận chức năng đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 602 | `CNKQVV_06` | Cập nhật thành công | Các trường thông tin không đúng thiết kế nên chưa kiểm thử được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 634 | `—` | Cung cấp công cụ để CB Nghiệp vụ kiểm tra tính hợp lệ, đầy đủ của hồ … | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 642 | `—` | Cung cấp chức năng gửi thông báo kết quả kiểm tra hồ sơ đề nghị hỗ tr… | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 644 | `—` | Cung cấp công cụ để CB Nghiệp vụ đánh giá hồ sơ theo các tiêu chí địn… | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 651 | `—` | Cung cấp chức năng gửi hồ sơ đề nghị thanh toán cho bộ phận Kế toán/T… | Chức năng chưa có, còn trong giai đoạn tích hợp | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 653 | `—` | Cung cấp giao diện cho Tư vấn viên nhận thông báo về kết quả xử lý hồ… | Chức năng chưa có, còn trong giai đoạn tích hợp | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 655 | `—` | Cung cấp quy trình để CB Nghiệp vụ/Bộ phận Kế toán thẩm định tính hợp… | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 662 | `—` | Gửi thông báo kết quả thẩm định hồ sơ đề nghị thanh toán cho Tư vấn v… | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 664 | `—` | Cung cấp quy trình để CB Nghiệp vụ trình Lãnh đạo CQQLNN phê duyệt hồ… | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 668 | `—` | Cung cấp chức năng cho Lãnh đạo CQQLNN xem xét và phê duyệt hồ sơ đề … | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 677 | `—` | Cập nhật trạng thái cuối cùng của hồ sơ (Đã thanh toán/Từ chối thanh … | Chức năng chưa được xây dựng - ghi nhận UC đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng; d… |
| Tuần 3 | 979 | `QLDMTCTV_08` | Thêm mới dữ liệu hợp lệ | Trường thông tin màn hình Thêm mới không khớp tài liệu thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 981 | `QLDMTCTV_10` | Sửa dữ liệu hợp lệ | Trường thông tin màn hình Chỉnh sửa không khớp tài liệu thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 983 | `QLDMTCTV_12` | Kiểm tra cửa số Cập nhật trạng thái hoạt động của Tổ chức tư vấn | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1044 | `QLCHTHXLHS_09` | Lưu cấu hình khi Dữ liệu hợp lệ | Bị chặn do TC QLCHTHXLHS_07 lỗi | — | ✘ chưa | N/R; ô TKM phản hồi lần 1 nêu lỗi ở TC/UC khác chặn case này |
| Tuần 3 | 1218 | `QLDKTK_10` | Liên kết hợp lệ và doanh nghiệp đặt mật khẩu thành công | Bị chặn, chờ TC QLDKTK_01 được sửa lỗi | — | ✘ chưa | N/R; ô TKM phản hồi lần 1 nêu lỗi ở TC/UC khác chặn case này |
| Tuần 3 | 1221 | `QLDNV_01` | Đăng nhập bằng tài khoản Vneid | Tính năng chưa được xây dựng - ghi nhận tính năng đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng |
| Tuần 3 | 1224 | `QLDNBV_01` | Đăng xuất bằng tài khoản Vneid | Tính năng chưa được xây dựng - ghi nhận tính năng đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng |
| Tuần 3 | 1225 | `QLDBTK_01` | Cấu hình đồng bộ giữa tài khoản đăng ký và tài khoản Vneid | Tính năng chưa được xây dựng - ghi nhận tính năng đang phát triển | — | ✘ chưa | N/R; ô Kết quả thực tế + TKM ghi chức năng chưa xây dựng |
| Tuần 3 | 1288 | `LDTBDDDR_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1289 | `LDTBDDDR_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1297 | `CGTVPL_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1298 | `CGTVPL_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1306 | `DGHQHTPL_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1307 | `DGHQHTPL_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1315 | `CLDTBDPL_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1316 | `CLDTBDPL_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1324 | `VVTDVQL_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1325 | `VVTDVQL_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1332 | `VVTLV_07` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1333 | `VVTLV_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1340 | `VVTLHDN_07` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1341 | `VVTLHDN_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1348 | `VVTTGCT_07` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1349 | `VVTTGCT_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1357 | `CPHTCT_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1358 | `CPHTCT_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1366 | `CPCTHTTDVQL_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1367 | `CPCTHTTDVQL_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1384 | `CPCTHTTLHDN_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1385 | `CPCTHTTLHDN_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1392 | `CPCTHTTTG_07` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1393 | `CPCTHTTTG_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1401 | `SLCTHT_08` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1402 | `SLCTHT_09` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1408 | `CTTDVQL_06` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1409 | `CTTDVQL_07` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1416 | `CTTLV_07` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1417 | `CTTLV_08` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1423 | `CTTTG_06` | Kiểm tra chức năng In báo cáo | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1424 | `CTTTG_07` | Kiểm tra chức năng Xóa bộ lọc | Màn hình không hiển thị nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1450 | `QLNDTVVCG_24` | Chấp nhận phân công | Bị chặn do UC QLNDTVVCG_23 lỗi | — | ✘ chưa | N/R; ô TKM phản hồi lần 1 nêu lỗi ở TC/UC khác chặn case này |
| Tuần 3 | 1463 | `QLNDTVVCG_37` | Cán bộ phê duyệt duyệt hủy | Bị chặn do UC QLNDTVVCG_36 lỗi | — | ✘ chưa | N/R; ô TKM phản hồi lần 1 nêu lỗi ở TC/UC khác chặn case này |
| Tuần 3 | 1464 | `QLNDTVVCG_38` | Phân công chuyên gia hàng loạt | Phân công chuyên gia hàng loạt bị từ chối, popup báo chưa được hỗ trợ | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1471 | `TKNDTVVCG_04` | Tìm kiếm theo tên tiêu đề | Hệ thống không có trường Tiêu đề nên không tìm kiếm theo tiêu đề được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1483 | `QLHSPLDN_05` | Thêm mới Thành công | Các trường thông tin hiển thị không đồng nhất với tài liệu thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1484 | `QLHSPLDN_06` | Xem | Trường thông tin màn hình Thêm mới không khớp tài liệu thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1485 | `QLHSPLDN_07` | Sửa | Trường thông tin màn hình Thêm mới không khớp tài liệu thiết kế | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1487 | `QLHSPLDN_09` | Tải lên tệp đính kèm hợp lệ | Màn hình thiếu trường tải tệp đính kèm nên không kiểm thử được upload | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1488 | `QLHSPLDN_10` | Tải lên tệp đính kèm vượt quá 20 MB | Màn hình thiếu trường tải tệp đính kèm nên không kiểm thử được upload | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1489 | `QLHSPLDN_11` | Tải lên tệp đính kèm chứa mã độc | Màn hình thiếu trường tải tệp đính kèm nên không kiểm thử được upload | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1490 | `QLHSPLDN_12` | Tìm kiếm hồ sơ pháp lý có kết quả | Màn hình thiếu ô tìm kiếm nên không kiểm thử được chức năng tìm kiếm | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1491 | `QLHSPLDN_13` | Tìm kiếm hồ sơ pháp lý không có kết quả | Màn hình thiếu ô tìm kiếm nên không kiểm thử được chức năng tìm kiếm | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1492 | `QLHSPLDN_14` | Khoảng ngày không hợp lệ | Màn hình thiếu ô tìm kiếm nên không kiểm thử được chức năng tìm kiếm | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1493 | `QLHSPLDN_15` | Xuất Excel thành công | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1494 | `QLHSPLDN_16` | Xuất Excel Không có dữ liệu, | Màn hình không có nút chức năng cần kiểm thử nên không thao tác được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1513 | `QLTLPLCVV_17` | Xóa tệp đính kèm khi tư liệu đang ở trạng thái "Công khai" | Màn hình thiếu hẳn chức năng cần kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1514 | `QLTLPLCVV_18` | Xem tệp trực tuyến | Màn hình thiếu hẳn chức năng cần kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1519 | `QLTLPLCVV_23` | Tìm kiếm tư liệu hỗ trợ tiếng Việt có dấu | Màn hình thiếu hẳn chức năng cần kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 3 | 1520 | `QLTLPLCVV_24` | Tìm kiếm hỗ trợ tiếng Việt không dấu. | Màn hình thiếu hẳn chức năng cần kiểm thử | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 4 | 1529 | `QLKCHTV_06` | NSD bấm "Lưu nháp" | Màn hình chưa có nút chức năng cần kiểm thử (Lưu nháp) | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 4 | 1572 | `QLCKCHTV_04` | Công khai hàng loạt | Màn hình thiếu ô tích chọn nên không công khai hàng loạt được | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 4 | 1580 | `QLHDTVVCG_01` | Quản lý các hợp đồng dịch vụ tư vấn chuyên sâu giữa DNNVV và chuyên g… | Chưa có menu cho chức năng Hợp đồng tư vấn; SRS cũng chưa có prototype màn hình | — | ✘ chưa | N/R nhưng ô TKM phản hồi lần 1 mô tả lỗi sản phẩm |
| Tuần 4 | 1616 | `KHTHCTHTPLDN_09` | Tạm dừng thành công | Bị chặn do UC KHTHCTHTPLDN_08 lỗi | — | ✘ chưa | N/R; ô TKM phản hồi lần 1 nêu lỗi ở TC/UC khác chặn case này |
| Tuần 4 | 1642 | `—` | Trình Lãnh đạo CQQLNN phê duyệt báo cáo kết quả thực hiện chương trìn… | Bị chặn do UC 165 lỗi nên không thực hiện được luồng báo cáo | — | ✘ chưa | N/R; ô Kết quả thực tế nêu lỗi ở TC/UC khác chặn case này; … |
| Tuần 4 | 1644 | `—` | Gửi báo cáo kết quả thực hiện chương trình cho các bên liên quan. | Bị chặn do UC 165 lỗi nên không thực hiện được luồng báo cáo | — | ✘ chưa | N/R; ô Kết quả thực tế nêu lỗi ở TC/UC khác chặn case này; … |
| Tuần 4 | 1646 | `—` | Tổng hợp báo cáo thực hiện chương trình từ nhiều đơn vị. | Bị chặn do UC 165 lỗi nên không thực hiện được luồng báo cáo | — | ✘ chưa | N/R; ô Kết quả thực tế nêu lỗi ở TC/UC khác chặn case này; … |

## ❓ Mâu thuẫn nội tại — cần đối tác làm rõ — 8 dòng

Dòng tự mâu thuẫn (vd Pass nhưng dev fix = Reject, hoặc có mã TC mà không ai chấm).

| Tuần | Dòng | Mã TC | Mô tả | Lỗi | dev fix | Đã test lại? | Ghi chú |
|---|---:|---|---|---|---|---|---|
| Tuần 1 | 167 | `QLCHVMDXL_01` | Xem danh sách đang xử lý — hard filter đúng trạng thái | Đối tác báo tab Đang xử lý sai bộ lọc trạng thái và vẫn hiện nút Thêm mới/Xóa; dev khẳng định đúng thiết kế | Reject | ✘ chưa | Trạng thái Pass nhưng Trạng thái dev fix = Reject; DEV phản… |
| Tuần 2 | 313 | `QLNHCH_15` | Nhập excel | Đối tác báo nhập Excel ngân hàng câu hỏi lỗi nhiều dòng; dev khẳng định do file dùng nhãn tiếng Việt thay mã | Reject | ✘ chưa | Trạng thái Pass nhưng Trạng thái dev fix = Reject; DEV phản… |
| Tuần 2 | 549 | `TKHSYCHTPL_04` | Tìm kiếm khoảng thời gian hợp lệ | Đối tác báo tìm kiếm theo khoảng thời gian trả về bản ghi ngoài khoảng; dev không tái hiện được | Reject | ✘ chưa | Trạng thái Pass nhưng Trạng thái dev fix = Reject; DEV phản… |
| Tuần 3 | 972 | `QLDMTCTV_01` | Quản lý danh sách các Tổ chức tư vấn tham gia mạng lưới. | Đối tác báo thiếu mục Tổ chức tư vấn; dev khẳng định chức năng nằm ở menu Mạng lưới Tư vấn viên | Reject | ✘ chưa | Trạng thái Pass nhưng Trạng thái dev fix = Reject; DEV phản… |
| Tuần 3 | 1222 | `QLDNV_02` | Kiểm tra Biểu mẫu đăng nhập — VNeID | - | — | ✘ chưa | Có Mã TC nhưng ô Trạng thái và Kết quả thực tế đều trống — … |
| Tuần 3 | 1223 | `QLDNV_03` | Xác thực VNeID thất bại | - | — | ✘ chưa | Có Mã TC nhưng ô Trạng thái và Kết quả thực tế đều trống — … |
| Tuần 4 | 1620 | `KHTHCTHTPLDN_13` | Trang Chi tiết chương trình (thẻ Thông tin chương trình) - Thẻ nội du… | - | — | ✘ chưa | Có Mã TC nhưng ô Trạng thái và Kết quả thực tế đều trống — … |
| Tuần 4 | 1621 | `KHTHCTHTPLDN_14` | Trang Chi tiết chương trình (thẻ Thông tin chương trình) - Thẻ "Thông… | - | — | ✘ chưa | Có Mã TC nhưng ô Trạng thái và Kết quả thực tế đều trống — … |

---

## Cụm lỗi lớn — nhiều dòng có thể chung 1 nguyên nhân gốc

Đếm bằng máy trên 223 dòng nhóm còn lỗi (không tính nhóm N/R). Sửa 1 chỗ có thể đóng cả cụm, nên ưu tiên xử lý theo cụm thay vì theo từng dòng.

| Cụm | Số dòng | Ghi nhận |
|---|---:|---|
| **Xuất file Excel/PDF thất bại** — *"Không thể tạo file xuất. Vui lòng thử lại."* | 44 | Khi TKM test lại (31/7) tất cả đổi thành **"Forbidden"** → mùi 403/phân quyền hoặc cấu hình môi trường UAT, **không phải 44 bug riêng**. Trải trên ~20 báo cáo khác nhau, tập trung Tuần 3. 24 dòng dev trả lời *"chưa tái hiện được trên môi trường DEV"* — phù hợp giả thuyết lỗi chỉ có ở UAT. |
| **Không gửi / không nhận được thông báo** | ~25 | Rải khắp module (vụ việc, đánh giá, tư vấn chuyên sâu) → nghi 1 root cause ở dịch vụ thông báo. |
| **Không hiển thị nút "In báo cáo" / "Xóa bộ lọc"** | 32 | Thuộc nhóm N/R; đều là màn báo cáo thống kê → nghi 1 gap FE ở component dùng chung, không phải 32 bug. |
| **Dev không nhận là bug, đề nghị chuyển thành yêu cầu cải tiến** | ~50 (Tuần 3) | Tranh chấp phạm vi đặc tả, **BA phải chốt** — dev/QA không tự đóng được. |
| **Dev trả lời "bản SRS docx đang outdate, sẽ gửi bản cập nhật"** | 21 | Đóng bằng đường sửa tài liệu, không phải sửa phần mềm; đối tác chưa test lại dòng nào. |

## ⚠️ Cảnh báo độ tin cậy của các dòng đã chấm Pass

256 dòng được đối tác chấm Pass ở vòng 2 và **đã bị loại khỏi danh sách trên**. Ba dấu hiệu dưới đây cho thấy một phần trong đó có thể **chưa thực sự hết lỗi** — nếu đúng thì đây là bug còn sót. Số liệu đếm bằng máy trên toàn bộ dữ liệu:

| Dấu hiệu | Số dòng | Vì sao đáng ngờ |
|---|---:|---|
| Ô `Kết quả thực tế lần 2` **chép y nguyên** ô `Kết quả mong đợi` | **253/256 (98%)** | Kết quả retest được ghi bằng copy-paste kỳ vọng, không mô tả quan sát thật → gần như không có giá trị làm bằng chứng đã fix. |
| Tên file bằng chứng vòng 2 **lệch mã TC** của chính dòng đó | **36/256** | Vd dòng 134 mã `PCXLCHVM_01` nhưng ảnh `PCXLCHVM_02_v2.jpg`; lệch gần như đều ±1 → ảnh chứng minh Pass có thể là ảnh của case khác. |
| Chấm Pass trong khi chính TKM ghi *"Lỗi chưa được fix"* | **5** | Dòng 792, 795, 1210, 1211, 1326. Toàn sheet có 16 dòng TKM ghi "chưa fix": 11 dòng để trống vòng 2, **5 dòng chấm Pass, 0 dòng chấm Fail**. |
| 2 dòng chấm Pass vòng 2 mà **không đính bằng chứng nào** | 2 | Thuộc lô Tuần 3. |

→ **Đề nghị:** yêu cầu đối tác xác nhận lại 10 dòng đã liệt kê ở mục *"Mâu thuẫn — ô trạng thái nói ngược nội dung"*, và gửi lại bằng chứng cho 36 dòng lệch tên file.

## Phạm vi đã soi & những gì đã loại

| Nhóm | Số dòng | Xử lý |
|---|---:|---|
| Pass ngay vòng 1 | 911 | Loại bằng máy — chưa từng là bug. |
| Fail vòng 1 → Pass vòng 2 | 256 | Soi ngược từng dòng; giữ lại 10 dòng mâu thuẫn. |
| Fail vòng 1, chưa/vẫn chưa qua vòng 2 | 223 | Soi từng dòng — vào danh sách. |
| N/R (chưa chạy) | 226 | Soi từng dòng; 95 dòng có dấu vết lỗi → vào danh sách. |
| Dòng rìa (trống trạng thái / trống tuần / Pass mà dev Reject) | 20 | Soi từng dòng. |
| **Tổng dòng trên sheet** | **1635** | |

**Đối chiếu độc lập:** bảng pivot `Tổng hợp fix bug` do chính đối tác lập ghi Fail = 479 (dev done 310 · Reopent 82 · Resoved 63 · trống 24) — **khớp tuyệt đối** với số đếm được từ dữ liệu thô, xác nhận không sót và không thừa dòng nào.

**Kiểm tra tab khác:** file đối tác có tab `Bản sao của UAT_TGPL Doanh Nghiệp` chứa 20 case không có ở tab chính — đã kiểm: **19 N/R + 1 Pass, không có Fail nào** → không bỏ sót bug. Bản sao là ảnh chụp cũ hơn (chỉ 65 dòng có kết quả vòng 2 so với 256 ở tab chính).

---

**Ghi chú đọc bảng**

- `Dòng` = số dòng thật trên Google Sheet của đối tác — mở sheet nhảy thẳng tới dòng đó.
- Mã TC **không phải khoá duy nhất**: có 15 mã bị dùng lại cho 2 dòng khác nhau. Luôn đối chiếu bằng cột `Dòng`.
- `dev fix` = giá trị 2 cột `Trạng thái dev fix` / `Trạng thái dev fix 2` trên sheet đối tác (chính tả gốc: `Reopent` = Reopen, `Resoved` = Resolved).
- File CSV kèm theo có đầy đủ nội dung `Kết quả thực tế` cả 2 vòng và tên file ảnh/video bằng chứng.
