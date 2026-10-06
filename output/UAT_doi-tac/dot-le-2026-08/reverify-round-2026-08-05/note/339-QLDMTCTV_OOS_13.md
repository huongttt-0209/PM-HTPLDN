## [UAT_TGPL Doanh Nghiệp-tuần 3] row 339 — QLDMTCTV_OOS_13 — S1
Tên chức năng: 
Tác nhân: 
Mô tả: Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — thứ tự trường và tên gọi Giấy ĐKHĐ chưa thống nhất với đặc tả
Điều kiện: 1. Đăng nhập tài khoản Cán bộ Nghiệp vụ cấp Trung ương (cbnv_tw_04), đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp.
2. Chọn menu "Mạng lưới Tư vấn viên" -> "Tổ chức tư vấn".
Dữ liệu đầu vào: Không cần dữ liệu — chỉ đọc thứ tự và nhãn trường trên biểu mẫu.
Các bước: 1. Bấm nút "Thêm mới" để mở biểu mẫu Thêm mới Tổ chức tư vấn.
2. Ghi lại thứ tự 15 trường theo đúng trình tự hiển thị.
3. So với bảng thành phần màn hình SCR-IV-NEW-02 (dòng 1676 đến 1695).
4. Đối chiếu tên gọi và tính bắt buộc của trường "Số Giấy ĐKHĐ Sở TP" với các dòng 1052, 1053, 1073, 1681, 1682, 2216 và 2217 của đặc tả.
KQ mong đợi: Đặc tả SCR-IV-NEW-02 xếp "Lĩnh vực pháp luật" và "Số lao động" cùng nhóm 2 (dòng 1684 đến 1685), đứng TRƯỚC nhóm Liên hệ gồm Địa chỉ, Số điện thoại, Email, Website (dòng 1686 đến 1690). Tên gọi và tính bắt buộc của Giấy đăng ký hoạt động cũng phải thống nhất giữa các phần của đặc tả.
KQ thực tế (l1): Thứ tự trên web là: Tên tổ chức, Loại hình, Người đại diện, Chức vụ đại diện, Số Giấy ĐKHĐ Sở TP, Ngày cấp, Số lao động, Địa chỉ, Điện thoại, Email, Website, Lĩnh vực pháp lý, Số quyết định công bố, Ngày quyết định công bố, Ghi chú.
Tức "Số lao động" bị tách khỏi nhóm 2 và chen vào trước "Địa chỉ"; "Lĩnh vực pháp lý" bị đẩy xuống sau "Website".
Về Giấy ĐKHĐ: web ghi nhãn "Số Giấy ĐKHĐ Sở TP" và đặt là bắt buộc. Đối chiếu thì chính đặc tả đang gọi giấy này bằng ba cách khác nhau và ghi tính bắt buộc khác nhau ở các phần khác nhau (nêu rõ ở phần trao đổi).
Trạng thái 1: Fail | P dev fix1: dev done | Q Verify: Open
KQ thực tế lần 2: 
Trạng thái 2:  | W dev fix2:  | X Verify2: 
--- NOTE (R: DEV phản hồi lần 1) ---
✅ Bug đúng (BA 04/08/2026 + QA đo lại 04/08/2026 trên bản dựng V1.0.5). Dev FE/BE: giấy tờ hành nghề của tổ chức tư vấn đang được gọi bằng HAI tên khác nhau cho hai trường của cùng một loại giấy, và không tên nào là tên chuẩn. Trên biểu mẫu Thêm mới: một trường ghi "Số Giấy ĐKHĐ Sở TP", trường ngay bên cạnh ghi "Ngày cấp Giấy đăng ký hành nghề". Câu báo lỗi của hệ thống cũng lệch tương ứng: một câu nói "Số Giấy đăng ký hành nghề là bắt buộc (NĐ 77/2008 Đ.13)", câu kia nói "Ngày cấp Giấy ĐKHĐ là bắt buộc (NĐ 77/2008 Đ.13)".
BA chốt tên gọi chuẩn là "Giấy đăng ký hoạt động" — căn cứ chính NĐ 77/2008 Điều 13 mà câu báo lỗi đang viện dẫn: điều luật này quy định Sở Tư pháp cấp Giấy đăng ký HOẠT ĐỘNG cho tổ chức; "giấy đăng ký hành nghề" là khái niệm của cá nhân tư vấn viên, không phải của tổ chức. Dev thống nhất tên gọi ở cả nhãn trường lẫn câu báo lỗi.
Phần MỨC BẮT BUỘC thì phần mềm ĐANG ĐÚNG, Dev không đụng: QA đo cả hai chiều — biểu mẫu đánh dấu bắt buộc cho cả hai trường, và gửi hồ sơ trống thẳng lên máy chủ bị từ chối kèm đúng hai câu báo lỗi trên, không tạo ra bản ghi nào. Điều kiện "nếu phần mềm đang cho lưu hồ sơ trống giấy này" mà BA nêu KHÔNG xảy ra. Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw + màn Mạng lưới Tư vấn viên → Tổ chức tư vấn → Thêm mới.
1) Đọc nhãn của hai trường giấy tờ trong nhóm "Thông tin cơ bản".
2) Để trống cả hai trường đó, điền đủ các trường bắt buộc còn lại → bấm Lưu, đọc câu báo lỗi.
3) Mở màn Chỉnh sửa một tổ chức đã có, đọc lại nhãn hai trường đó.
✅ PASS khi: cả hai nhãn và cả hai câu báo lỗi đều dùng cùng một tên gọi "Giấy đăng ký hoạt động", nhất quán giữa màn Thêm mới và màn Chỉnh sửa; bước 2 vẫn bị chặn, hồ sơ không được tạo.
❌ FAIL nếu: còn chỗ nào dùng chữ "hành nghề" cho giấy tờ của tổ chức; hoặc hai trường vẫn gọi tên khác nhau; hoặc bước 2 lưu được hồ sơ trống giấy này.
⚠️ Viết tắt "ĐKHĐ" chỉ được chấp nhận nếu tên đầy đủ đã xuất hiện ở nhãn hoặc chú giải cùng màn. Đừng chấm PASS khi màn chỉ có chữ viết tắt.
Bằng chứng đo: do-lai-nhom-xuat-pdf-va-row339-2026-08-04.md + image/QLDMTCTV_OOS_13-form-themmoi-hai-ten-goi-khac-nhau.png