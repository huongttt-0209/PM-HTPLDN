# Mô tả lỗi cho các case FAIL cũ trong 3 report — BẢN REVIEW (chưa cập nhật)

> Mục đích: bổ sung cột **Lý do** = mô tả lỗi ngắn cho các case FAIL (theo yêu cầu đối tác Ánh).
> 10 case FAIL bổ sung (UC167/biểu mẫu/danh mục/VNeID) **đã** có mô tả — file này là **130 case FAIL cũ còn lại**.
>
> **Nguyên tắc trung thực:** mỗi mô tả nói lại đúng "điều mong đợi đã không xảy ra" (suy từ tên case + Kết quả mong đợi trong chính report). Không gán mã lỗi/triệu chứng cụ thể mà report không lưu. Mô tả **giống nhau** ở cả 3 file, chỉ hiển thị ở dòng đang FAIL của từng vòng.
>
> Cờ vòng: **[d3]** = còn FAIL ở dot-3 (mới nhất, bug hiện tại) · **[d2]** = FAIL tới dot-2, đã fix ở dot-3 · **[d1]** = chỉ FAIL ở dot-1, fix sớm.

---

## 02. Dashboard tổng quan (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| DASH-001 | d2 | Sau đăng nhập, Dashboard không hiển thị đầy đủ các thẻ KPI/biểu đồ như thiết kế. |
| DASH-002 | d2 | Header Dashboard thiếu nhãn "Cập nhật lúc" và/hoặc nút "Làm mới". |
| DASH-005 | d2 | Giao diện Dashboard không co giãn đúng ở độ phân giải 1024–1279px. |
| DASH-004 | d1 | Thẻ KPI không hiển thị chỉ dấu xu hướng (tăng/giảm) so với kỳ trước. |
| DASH-004a | d1 | Hai KPI cảnh báo không đảo màu xu hướng (tăng = xấu) như yêu cầu. |
| DASH-004b | d1 | Không hiển thị dấu "—" khi thiếu dữ liệu kỳ trước để so sánh. |
| DASH-029b | d1 | Thẻ KPI ảnh chụp thiếu chú thích mốc thời gian "Tính đến...". |

## 03. Hỏi đáp pháp lý (11)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-HD-001 | d2 | Danh sách hỏi đáp không hiển thị đúng (7 tab trạng thái/dữ liệu) cho CB NV TW. |
| TC-HD-002 | d2 | Phân quyền phạm vi sai: CB NV BN thấy cả dữ liệu hỏi đáp ngoài đơn vị mình. |
| TC-HD-003 | d2 | Phân trang danh sách hỏi đáp không đổi được số bản ghi/trang. |
| TC-HD-004 | d1 | Không tạo được hỏi đáp mới (luồng cơ bản). |
| TC-HD-007 | d1 | Không chặn/không báo lỗi khi nội dung hỏi đáp vượt 5000 ký tự. |
| TC-HD-008 | d1 | Không báo lỗi khi chọn lĩnh vực pháp luật không tồn tại. |
| TC-HD-009 | d1 | Không chặn file chứa mã độc khi upload (không quét/không báo lỗi). |
| TC-HD-206 | d3 | Không chặn khi upload vượt 10 file/lần. |
| TC-HD-207 | d3 | Không chặn khi upload file vượt 20MB. |
| TC-HD-208 | d3 | Không chặn khi upload file rỗng (0 byte). |
| TC-PD-061 | d3 | Không hiển thị đúng trạng thái rỗng khi chưa có hỏi đáp đã xử lý. |

## 04. Đào tạo tập huấn (9)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| DT-041 | d2 | Không tạo được Kế hoạch đào tạo năm (mã tự sinh/trạng thái NHAP). |
| DT-041a | d2 | Phân quyền phạm vi sai: CB NV TW không thấy đúng Kế hoạch năm theo cấp. |
| DT-041b | d2 | Phân trang Kế hoạch năm không đúng mặc định 20/trang. |
| DT-041c | d1 | Không chặn khi ngày kết thúc ≤ ngày bắt đầu của Kế hoạch năm. |
| DT-041d | d1 | Ràng buộc ngân sách không đúng (cho phép âm hoặc xử lý sai giá trị 0). |
| DT-041e | d1 | Không chặn khi tên Kế hoạch vượt 500 ký tự. |
| DT-042 | d1 | Không sửa được Kế hoạch năm ở trạng thái NHAP. |
| TC-KH-H-015 | d3 | Hủy Kế hoạch (Dự thảo) không chuyển đúng trạng thái Đã hủy. |
| TC-XUAT-H-003 | d3 | Không xuất được DOCX ký số cho chương trình đào tạo đã duyệt. |

## 05. Chuyên gia tư vấn (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-CG-UI-01 | d2 | Giao diện danh sách TVV không đúng thiết kế (toolbar/5 tab/bộ lọc). |
| TC-CG-UI-02 | d2 | Form Thêm/Sửa TVV không đủ 5 nhóm thông tin theo thiết kế. |
| TC-TVV-001 | d2 | CB NV TW không xem được danh sách TVV toàn quốc theo phạm vi. |
| TC-CG-002 | d1 | Phân quyền phạm vi sai: CB NV ĐP thấy cả TVV ngoài đơn vị. |
| TC-TVV-003 | d1 | Lọc theo tab trạng thái TVV không đúng. |
| TC-CG-004 | d1 | Phân trang danh sách TVV không đúng mặc định 20/trang. |
| TC-TVV-005 | d1 | Không mở được màn chi tiết TVV (5 tab) khi click bản ghi. |

## 06. Người hỗ trợ pháp luật (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| NHT-001 | d2 | Không tạo được Người hỗ trợ mới với đủ trường bắt buộc. |
| NHT-003 | d2 | Không kích hoạt được tài khoản NHT qua link email / đặt mật khẩu lần đầu. |
| NHT-004 | d2 | Không báo lỗi khi email/tên đăng nhập NHT bị trùng. |
| NHT-005 | d1 | Không chặn khi tạo NHT mà chưa chọn lĩnh vực chuyên môn. |
| NHT-006 | d1 | Không cập nhật được lĩnh vực chuyên môn của NHT khi sửa. |
| NHT-007 | d1 | Không đổi được đơn vị của NHT khi sửa. |
| NHT-002 | d1 | Trường đơn vị không bị khóa theo đơn vị cán bộ khi tạo NHT. |

## 07. Tổ chức tư vấn (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-TCTV-001 | d2 | Không tạo được Tổ chức tư vấn mới với đủ trường bắt buộc. |
| TC-TCTV-002 | d2 | Phân quyền phạm vi sai: đơn vị không bị khóa khi CB ĐP tạo Tổ chức tư vấn. |
| TCTV-003 | d2 | Không chặn khi tạo Tổ chức tư vấn mà chưa chọn lĩnh vực. |
| TCTV-004 | d1 | Không báo lỗi khi nhập email sai định dạng cho Tổ chức tư vấn. |
| TCTV-006 | d1 | Không xuất được Excel danh sách Tổ chức tư vấn. |
| TCTV-020 | d1 | Xóa được Tổ chức tư vấn khi còn TVV đang hoạt động (đáng lẽ phải chặn). |
| TCTV-024 | d1 | Không chặn khi file đính kèm Tổ chức tư vấn vượt 20MB. |

## 08. Vụ việc HTPL (9)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| VV-001 | d2 | Danh sách vụ việc không lọc đúng theo trạng thái / số đếm tab sai. |
| VV-002 | d2 | Tìm kiếm vụ việc không trả đúng kết quả. |
| VV-003 | d2 | Không tạo được vụ việc nhập tay (mã tự sinh/trạng thái). |
| VV-004 | d1 | Không báo đủ lỗi khi bỏ trống 5 trường bắt buộc lúc tạo vụ việc. |
| VV-006 | d1 | Hạn xử lý không tính đúng (ngày tiếp nhận + 15 ngày làm việc). |
| VV-007 | d1 | Không chuyển được vụ việc sang "Đang kiểm tra" khi duyệt Đạt. |
| VV-008 | d1 | Không chuyển được vụ việc sang "Yêu cầu bổ sung". |
| TC-VV-DS-105 | d3 | Sắp xếp danh sách vụ việc theo ngày tiếp nhận không đúng. |
| TC-VV-DS-201 | d3 | Không hiển thị đúng trạng thái rỗng khi lọc vụ việc ra 0 kết quả. |

## 09. Chi trả chi phí (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| CT-001 | d2 | Danh sách hồ sơ chi trả không hiển thị đúng (5 tab/9 cột). |
| CT-002 | d2 | Bộ lọc kết hợp (quy mô + trạng thái) hồ sơ chi trả không đúng. |
| CT-001b | d1 | Không hiển thị đúng placeholder khi tìm kiếm hồ sơ chi trả ra 0 kết quả. |
| CT-007a | d1 | Không mở được chi tiết hồ sơ chi trả khi click bản ghi. |
| CT-022 | d1 | Không xuất được Excel danh sách hồ sơ chi trả. |
| CT-004 | d1 | Không chuyển được hồ sơ chi trả sang "Đang đánh giá" khi duyệt Đạt. |
| CT-005 | d1 | Không chuyển được hồ sơ chi trả sang "Yêu cầu bổ sung". |

## 10. Quản lý doanh nghiệp (10)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-DN-UI-01 | d2 | Giao diện danh sách Doanh nghiệp không đúng thiết kế. |
| TC-DN-UI-02 | d2 | Form Doanh nghiệp không đủ 4 tab/trường theo thiết kế. |
| TC-HSPL-UI-01 | d1 | Giao diện tab "Hồ sơ PL doanh nghiệp" không đúng thiết kế. |
| TC-LSHT-UI-01 | d1 | Giao diện tab "Lịch sử Hỗ trợ" không đúng (3 KPI/bảng). |
| TC-DN-UI-04 | d1 | Bốn tab chi tiết Doanh nghiệp không hiển thị đúng. |
| TC-DN-001 | d1 | CB NV TW không xem được danh sách Doanh nghiệp toàn quốc. |
| TC-DN-002 | d1 | Phân quyền phạm vi sai: CB NV BN thấy cả Doanh nghiệp ngoài đơn vị. |
| TC-DN-101 | d3 | Không xóa mềm được Doanh nghiệp không có vụ việc. |
| TC-HSPL-201 | d3 | Không xóa mềm được hồ sơ pháp lý Doanh nghiệp. |
| TC-DN-PERM-404 | d3 | Truy cập chéo đơn vị bị chặn (403) nhưng không ghi nhật ký kiểm toán. |

## 11. Đánh giá (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| DG-001 | d2 | Danh sách đợt đánh giá không hiển thị/lọc đúng. |
| DG-002 | d2 | Không tạo được đợt đánh giá mới (luồng cơ bản). |
| DG-002b | d1 | Dropdown tần suất đợt đánh giá không giới hạn đúng 2 lựa chọn. |
| DG-003 | d1 | Không xem được chi tiết đợt đánh giá đầy đủ 4 tab. |
| DG-010 | d1 | Không xuất được Excel danh sách đợt đánh giá. |
| DG-011 | d1 | Không báo lỗi khi tạo đợt đánh giá thiếu trường bắt buộc. |
| DG-012 | d1 | Không chặn khi từ ngày ≥ đến ngày của đợt đánh giá. |

## 12. Biểu mẫu (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-TM-001 | d2 | Không tạo được thư mục biểu mẫu (luồng cơ bản). |
| TC-TM-002 | d2 | Không sửa được thư mục biểu mẫu. |
| TC-TM-003 | d1 | Không xóa được thư mục biểu mẫu rỗng. |
| TC-TM-004 | d1 | Danh sách thư mục không phân trang đúng. |
| TC-TM-005 | d1 | Không xuất được Excel danh sách thư mục. |
| TC-TM-010 | d1 | Không báo lỗi khi tạo thư mục trùng tên trong đơn vị. |
| TC-TM-011 | d1 | Xóa được thư mục đang chứa biểu mẫu (đáng lẽ phải chặn). |

## 13. Quản trị hệ thống (9)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-SLA-023 | d2 | Giao diện tab cấu hình SLA không đúng thiết kế. |
| TC-SLA-001 | d2 | Danh sách cấu hình SLA mặc định không hiển thị đúng. |
| TC-SLA-002 | d1 | Không sửa được thời hạn xử lý SLA (sửa trực tiếp trên lưới). |
| TC-SLA-003 | d1 | Không sửa được mức cảnh báo CB1/CB2 của SLA. |
| TC-SLA-005 | d1 | Không bật/tắt được tùy chọn gửi email cảnh báo SLA. |
| TC-SLA-006 | d1 | Không báo lỗi khi nhập thời hạn SLA = 0. |
| TC-SLA-007 | d1 | Không báo lỗi khi nhập thời hạn SLA là số âm. |
| TC-CRUD-027 | d3 | Không báo lỗi tương tranh khi xóa bản ghi vừa bị người khác sửa. |
| TC-LODN-002 | d3 | Không thêm được bản ghi khi chỉ nhập Mã + Tên (tiêu chí để trống). |

## 14. Báo cáo thống kê (8)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-BC-UI-01 | d2 | Giao diện báo cáo thống kê không đúng (breadcrumb/tiêu đề/nút Làm mới). |
| TC-BC-UI-02 | d2 | Dropdown loại báo cáo không nhóm đúng 8 nhóm/23 loại. |
| TC-BC-UI-03 | d1 | Bộ lọc đặc thù không tự cập nhật khi đổi loại báo cáo. |
| TC-BC-UI-04 | d1 | Nút "Xem báo cáo" không bị khóa khi chưa chọn loại báo cáo. |
| TC-BC-UI-05 | d1 | Nút Xuất không bị khóa khi chưa chạy "Xem báo cáo". |
| TC-BC-UI-06 | d1 | Không ẩn/hiện được biểu đồ báo cáo. |
| TC-BC-UI-07 | d1 | Bảng báo cáo không giữ header dính / không sắp xếp cột / thiếu hàng tổng. |
| TC-BC-REP-023 | d3 | Không hiển thị đúng thông báo khi truy vấn báo cáo quá 30 giây. |

## 15. Tư vấn chuyên sâu (7)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TV-001 | d2 | Danh sách Tư vấn chuyên sâu không hiển thị đúng (3 tab/phân trang). |
| TV-002 | d2 | Không xem được chi tiết Tư vấn chuyên sâu đầy đủ các tab. |
| TV-003 | d1 | Không tạo được yêu cầu Tư vấn chuyên sâu mới. |
| TV-004 | d1 | Không cập nhật được Tư vấn chuyên sâu ở trạng thái Tiếp nhận. |
| TV-030 | d1 | Không báo lỗi khi tạo Tư vấn chuyên sâu với nội dung trống. |
| TV-031 | d1 | Không chặn khi chọn chuyên gia đã ngừng hoạt động cho Tư vấn chuyên sâu. |
| TV-005 | d1 | Tìm kiếm toàn văn Tư vấn chuyên sâu không trả đúng kết quả. |

## 16. Tư vấn nhanh (6)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TVN-002 | d2 | Tìm kiếm/lọc Tư vấn nhanh không trả đúng kết quả. |
| TVN-004 | d2 | Cập nhật Q&A ở trạng thái Chờ duyệt không đúng (nội dung/trạng thái). |
| TVN-004b | d1 | Sửa Q&A ở trạng thái Nhập (đã bị từ chối) không đúng. |
| TVN-005 | d1 | Import Excel Tư vấn nhanh không hiển thị preview/kết quả đúng. |
| TVN-006 | d1 | Không báo lỗi khi import Excel sai định dạng. |
| TVN-007 | d1 | Không báo lỗi khi tạo Q&A với câu hỏi trống. |

## 17. Hợp đồng tư vấn (6)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| HDTV-001 | d2 | Danh sách Hợp đồng tư vấn không hiển thị/lọc/phân trang đúng. |
| HDTV-002 | d2 | Tìm kiếm Hợp đồng tư vấn không trả đúng kết quả. |
| HDTV-002b | d1 | Lọc Hợp đồng theo khoảng ngày ký + TVV không đúng. |
| HDTV-012 | d1 | Không xuất được Excel danh sách Hợp đồng tư vấn. |
| HDTV-003 | d1 | Không tạo được Hợp đồng mới (mã tự sinh/bên A tự điền). |
| HDTV-003b | d1 | Mã hợp đồng không đảm bảo duy nhất khi tạo nhiều HĐ cùng ngày. |

## 18. Chương trình HTPLDN (6)

| Mã | Vòng | Mô tả lỗi đề xuất |
|---|:-:|---|
| TC-CT-CRUD-001 | d2 | Không tạo được Chương trình HTPLDN mới (luồng cơ bản). |
| TC-CT-CRUD-002 | d2 | Không sửa được Chương trình ở trạng thái Dự thảo. |
| TC-CT-CRUD-003 | d1 | Không xóa được Chương trình ở trạng thái Dự thảo. |
| TC-CT-CRUD-004 | d1 | Danh sách Chương trình không phân trang/hiển thị đúng cột. |
| TC-CT-CRUD-005 | d1 | Không xem được chi tiết Chương trình (tab Thông tin/thanh tiến trình). |
| TC-CT-CRUD-010 | d1 | Không báo lỗi khi tạo Chương trình thiếu trường bắt buộc. |

---

## Tổng kết

- **130 mô tả** cho 130 case FAIL cũ (chưa tính 10 case bổ sung đã có mô tả).
- Phân bố vòng: **[d3] = 14 case** (bug còn ở report mới nhất) · **[d2] = ~41 case** · **[d1] = ~75 case** (đã fix sớm).
- Tất cả mô tả là **nói lại trung thực** điều mong đợi đã không xảy ra — không gán mã lỗi/triệu chứng report không lưu.

### Lưu ý để bạn quyết
1. Nếu đối tác chỉ quan tâm **bug hiện tại**, có thể chỉ điền 14 case **[d3]** (3 file vẫn nhất quán vì dot-1/dot-2 sẽ để trống dòng đã PASS ở dot-3 — nhưng dòng đó vẫn FAIL ở dot-1/dot-2). → Khuyến nghị điền **đủ 130** để 3 report đồng bộ, không có dòng FAIL nào trống Lý do.
2. Muốn mô tả **sâu hơn** (root-cause thật) cho vài case trọng điểm → có nguồn dev `FIXED-BUGS-SUMMARY.md` + `qa-tracking.md`, tôi tra bổ sung riêng từng case bạn chỉ định.
