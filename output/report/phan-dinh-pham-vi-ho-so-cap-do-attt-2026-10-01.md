# Phân định phạm vi cung cấp thông tin — Hồ sơ đề xuất cấp độ an toàn thông tin

Ngày lập: 01/10/2026

Tài liệu mẫu: `docs/Reference/HoSo_DeXuatCapDo3_BTP_Cong_PLQG_v1.0.docx`

## 1. Mục đích và phạm vi các bên

Tài liệu này xác định những mục trong hồ sơ đề xuất cấp độ an toàn thông tin mà DOPAI cung cấp được thông tin và những mục DOPAI không cung cấp được. Căn cứ phân định là phạm vi công việc của từng bên.

| Bên | Phạm vi công việc |
| --- | --- |
| DOPAI | Phát triển phần mềm; thiết kế API (đặc tả giao diện kết nối). Không thực hiện tích hợp, triển khai, hạ tầng. |
| OSP | Triển khai; hạ tầng (mạng, máy chủ, lưu trữ, thiết bị an ninh); tích hợp với hệ thống bên ngoài; vận hành. |
| Chủ đầu tư / Chủ quản hệ thống | Xác định cấp độ; ban hành chính sách; tổ chức, nhân sự; phê duyệt hồ sơ. |

Quy ước mức cung cấp:

- **Có**: DOPAI cung cấp được toàn bộ thông tin của mục.
- **Một phần**: DOPAI cung cấp phần liên quan đến phần mềm; phần còn lại do OSP hoặc Chủ đầu tư cung cấp.
- **Không**: mục nằm ngoài phạm vi của DOPAI.

## 2. Bảng phân định theo từng mục

Tổng hợp:

| Mức | Số mục | Các mục |
| --- | --- | --- |
| Có | 2 | 7.1.4.1, PL II – 3.1 |
| Một phần | 15 | I.3, I.4.1, I.4.4, 7.1.4.2, 7.1.4.3, 7.1.5.2, 7.1.5.3, 7.1.5.6, 7.1.5.7, 7.1.5.8, PL II – 3.2, 3.3, 3.4, 3.6, 4.2 |
| Không | 21 | Các mục còn lại |

Chi tiết từng mục:

| Mục | Tên mục | DOPAI | Phần DOPAI cung cấp | Người cung cấp trong DOPAI | Phần do OSP / Chủ đầu tư cung cấp |
| --- | --- | --- | --- | --- | --- |
| I.1 | Thông tin Chủ quản hệ thống thông tin | Không | — | — | Toàn bộ |
| I.2 | Thông tin Đơn vị vận hành | Không | — | — | Toàn bộ |
| I.3 | Mô tả phạm vi, quy mô của hệ thống | Một phần | Chức năng, đối tượng sử dụng | BA | Quy mô vận hành thực tế |
| I.4.1 | Mô hình logic tổng thể | Một phần | Kiến trúc tầng ứng dụng | Dev/SA | Vùng mạng, tường lửa, WAF, cân bằng tải |
| I.4.2 | Mô hình kết nối vật lý | Không | — | — | Toàn bộ |
| I.4.3 | Danh mục thiết bị sử dụng trong hệ thống | Không | — | — | Toàn bộ |
| I.4.4 | Danh mục các ứng dụng/dịch vụ | Một phần | Thành phần phần mềm | Dev/SA | Máy chủ, vùng mạng, hệ điều hành |
| I.4.5 | Quy hoạch địa chỉ IP các vùng mạng | Không | — | — | Toàn bộ |
| II | Thuyết minh cấp độ đề xuất | Không | — | — | Toàn bộ |
| III | Thuyết minh phương án bảo đảm an toàn hệ thống thông tin | Không | — | — | Toàn bộ |
| PL I – 7.1.1 | Thiết lập chính sách an toàn thông tin | Không | — | — | Toàn bộ |
| PL I – 7.1.2 | Tổ chức bảo đảm an toàn thông tin | Không | — | — | Toàn bộ |
| PL I – 7.1.3 | Tuyển dụng; trong quá trình làm việc; chấm dứt hoặc thay đổi công việc | Không | — | — | Toàn bộ |
| PL I – 7.1.4.1 | Thiết kế an toàn hệ thống thông tin | Có | Tài liệu thiết kế phần mềm | Dev/SA | — |
| PL I – 7.1.4.2 | Phát triển phần mềm thuê khoán | Một phần | Mã nguồn, kiểm thử, tự kiểm tra an toàn thông tin | Dev/SA (mã nguồn, tự kiểm tra); Tester (kiểm thử) | Biên bản, hợp đồng, cam kết với bên thuê khoán |
| PL I – 7.1.4.3 | Thử nghiệm và nghiệm thu hệ thống | Một phần | Kế hoạch, kết quả kiểm thử | Tester | Bên độc lập giám sát, phê duyệt nghiệm thu |
| PL I – 7.1.5.1 | Quản lý an toàn mạng | Không | — | — | Toàn bộ |
| PL I – 7.1.5.2 | Quản lý an toàn máy chủ và ứng dụng | Một phần | Phần ứng dụng | Dev/SA | Phần máy chủ, vận hành |
| PL I – 7.1.5.3 | Quản lý an toàn dữ liệu | Một phần | Danh mục dữ liệu cần sao lưu | Dev/SA | Thực hiện sao lưu, khôi phục |
| PL I – 7.1.5.4 | Quản lý an toàn thiết bị đầu cuối | Không | — | — | Toàn bộ |
| PL I – 7.1.5.5 | Quản lý phòng chống phần mềm độc hại | Không | — | — | Toàn bộ |
| PL I – 7.1.5.6 | Quản lý giám sát an toàn hệ thống thông tin | Một phần | Định dạng nhật ký ứng dụng | Dev/SA | Hệ thống giám sát |
| PL I – 7.1.5.7 | Quản lý điểm yếu an toàn thông tin | Một phần | Danh mục thư viện, vá lỗi ứng dụng | Dev/SA | Rà quét định kỳ |
| PL I – 7.1.5.8 | Quản lý sự cố an toàn thông tin | Một phần | Đầu mối xử lý lỗi phần mềm | Dev/SA | Quy trình ứng cứu, diễn tập |
| PL I – 7.1.5.9 | Quản lý an toàn người sử dụng đầu cuối | Không | — | — | Toàn bộ |
| PL I – 7.1.5.10 | Quản lý rủi ro an toàn thông tin | Không | — | — | Toàn bộ |
| PL I – 7.1.5.11 | Kết thúc vận hành, khai thác, thanh lý, hủy bỏ | Không | — | — | Toàn bộ |
| PL II – 1 | Bảo đảm an toàn mạng | Không | — | — | Toàn bộ |
| PL II – 2 | Bảo đảm an toàn máy chủ | Không | — | — | Toàn bộ |
| PL II – 3.1 | Xác thực | Có | Biện pháp xác thực của ứng dụng | Dev/SA | — |
| PL II – 3.2 | Kiểm soát truy cập | Một phần | Phân quyền, hết phiên, giới hạn phiên | Dev/SA | Kết nối và địa chỉ quản trị từ xa |
| PL II – 3.3 | Nhật ký hệ thống | Một phần | Ghi nhật ký ứng dụng | Dev/SA | Lưu trữ nhật ký tập trung |
| PL II – 3.4 | Bảo mật thông tin liên lạc | Một phần | Ứng dụng bắt buộc kênh mã hoá | Dev/SA | Chứng thư số, cấu hình kênh truyền |
| PL II – 3.5 | Chống chối bỏ (chữ ký số) | Không | — | — | Không áp dụng: phần mềm không có yêu cầu chức năng chữ ký số |
| PL II – 3.6 | An toàn ứng dụng và mã nguồn | Một phần | Kiểm tra dữ liệu đầu vào/đầu ra, chống tấn công phổ biến | Dev/SA | Giới hạn địa chỉ quản trị |
| PL II – 4.1 | Nguyên vẹn dữ liệu | Không | — | — | Toàn bộ |
| PL II – 4.2 | Bảo mật dữ liệu | Một phần | Mã hoá ở tầng ứng dụng | Dev/SA | Mã hoá hệ thống lưu trữ |
| PL II – 4.3 | Sao lưu dự phòng | Không | — | — | Toàn bộ |

PL I: Phụ lục I (yêu cầu quản lý). PL II: Phụ lục II (yêu cầu kỹ thuật).

Người cung cấp trong DOPAI: BA cung cấp thông tin mô tả nghiệp vụ từ SRS; Dev/SA cung cấp thông tin thiết kế và hiện trạng phần mềm; Tester cung cấp hồ sơ kiểm thử.
