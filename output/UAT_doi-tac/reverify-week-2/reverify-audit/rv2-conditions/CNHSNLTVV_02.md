# Bảng đối chiếu điều kiện — CNHSNLTVV_02 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (Người hỗ trợ pháp lý) — `nht_qa_tw`, đơn vị Cục Bổ trợ tư pháp | NHT — `nht_qa_tw`, banner "QA NHT Trung uong / NHT", TVV cùng đơn vị | Không |
| Entity + trạng thái | TVV cùng đơn vị (bug kiểm 2 state, kết quả như nhau) | TVV-BTP-TW-0009 (Mới đăng ký, cùng đơn vị Cục Bổ trợ) | Không |
| Màn hình | Chi tiết TVV → thẻ "Năng lực" → nút "Cập nhật năng lực" → form sửa nhanh | Đúng màn, thẻ Năng lực → "Cập nhật năng lực" | Không |
| Thao tác kiểm | Đếm số trường của biểu mẫu | Form có **11 trường**: Trình độ · Số năm kinh nghiệm · Mô tả kinh nghiệm · Chuyên ngành · Số thẻ hành nghề · **Bằng cấp chi tiết** · **Chứng chỉ chi tiết** · Lĩnh vực pháp luật · Chứng chỉ hiện có · Thêm chứng chỉ mới · Ghi chú cập nhật | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Biểu mẫu "Cập nhật năng lực" nay có 11 trường — bổ sung đủ 5 trường trước đây thiếu (Bằng cấp chi tiết, Chứng chỉ chi tiết, Trình độ, Số năm kinh nghiệm, Số thẻ hành nghề). Sửa được đúng các mục thẻ Năng lực hiển thị.
