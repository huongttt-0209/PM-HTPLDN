✅ Bug ĐÚNG.
- Đối tác báo: Nhóm 8 — Thông tin phê duyệt và Lịch sử xử lý; màn hình không có trường Thông tin phê duyệt.
- Kiểm tra lại trên màn Chi tiết hồ sơ, hồ sơ CT-SEED-107 trạng thái Đã duyệt (tài khoản CB Nghiệp vụ TW, data thật): các mục hiển thị gồm Thông tin Doanh nghiệp → Thông tin Tư vấn viên → Cập nhật thanh toán (form) → Lịch sử xử lý. KHÔNG có mục "Thông tin phê duyệt" với các trường Ngày/Người tiếp nhận, Thời gian/Người phê duyệt.
- Đối chiếu SRS SCR-V.II-02 (FR-06, UC69) component #35 "section-8 Thông tin phê duyệt & Lịch sử" (srs-fr-06-chi-tra.md:1011, điều kiện hiển thị "Luôn"): phải hiển thị Ngày tiếp nhận, Người tiếp nhận, Thời gian phê duyệt, Người phê duyệt, Thời gian/Người/Lý do từ chối, Lý do hủy.
- KHÔNG phải thiếu dữ liệu: hồ sơ Đã duyệt CT-SEED-107 đã có ngayTiepNhan, nguoiTiepNhanId, nguoiDuyetId, ngayDuyet ("2026-07-03"), nguoiGuiDuyetId, ngayGuiDuyet trong dữ liệu nhưng màn không hiển thị.
- Ghi chú: mục "Lịch sử xử lý" (Timeline, component #36) có tồn tại nhưng trống do AUDIT_LOG rỗng — phần khác, không thuộc bug này.
- Bug tái hiện đúng, có SRS reference cụ thể → lỗi thật, dev fix. Chi tiết: Pass-bug-report-UAT-tuan-3-chi-tra.md §BUG-QLHSDNHTCP_13.
