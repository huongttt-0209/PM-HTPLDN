⚠️ Cần BA xác nhận.
- Case: kiểm tra cột dữ liệu bảng danh sách Hồ sơ Chi trả (FR-V.II-02, UC69 · màn SCR-V.II-01).
- Đối tác phản ánh: cột "Mức cảnh báo thời hạn" không giống thiết kế.
- Thực tế web (đã seed 10 hồ sơ, tài khoản CB Nghiệp vụ TW): cột này tên "Hạn xử lý", hiển thị đếm ngược + mã màu (xanh: còn hạn; đỏ/đen: quá hạn) — vd "Còn 4 ngày LV", "Quá hạn 17 ngày LV".
- SRS (SCR-V.II-01 thành phần SLA + BR-CALC-03) quy định cột cảnh báo SLA 4 mức: Sắp đến hạn / Cần xử lý gấp / Sát hạn / Quá hạn (tiếng Việt). App gộp thành đếm ngược + màu, không hiện đủ 4 nhãn mức rời và tên khác ("Hạn xử lý" thay vì "Mức cảnh báo thời hạn").
- Câu hỏi BA: cột SLA có bắt buộc hiển thị đúng 4 nhãn mức cảnh báo theo BR-CALC-03 và/hoặc đúng tên "Mức cảnh báo thời hạn" như thiết kế không, hay dạng "Hạn xử lý" (đếm ngược + màu) hiện tại được chấp nhận?
