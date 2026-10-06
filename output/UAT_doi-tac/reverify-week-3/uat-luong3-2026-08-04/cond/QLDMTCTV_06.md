# Bảng đối chiếu điều kiện — QLDMTCTV_06 (dòng 319) — Biểu mẫu Thêm mới thiếu 3 trường

**Kết luận:** Pass — biểu mẫu Thêm mới đã có đủ Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm; nhập và lưu xuống đúng.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (`cbnv_tw`, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương, đơn vị Bộ Tư pháp | `cbnv_tw` — Cán bộ NV Trung ương, Cục Bổ trợ tư pháp – Bộ Tư pháp (đúng vai trò + cấp trong ảnh đối tác) | Không |
| Màn hình / entity + trạng thái | Biểu mẫu **Thêm mới** Tổ chức tư vấn (`/chuyen-gia-tvv/to-chuc/tao-moi`), chế độ nhập liệu mới | Cùng màn, mở từ nút "+ Thêm mới" trên danh sách Tổ chức tư vấn | Không |
| Dữ liệu tiền đề | Không cần — chỉ mở biểu mẫu trống | Mở biểu mẫu trống; ngoài ra tạo thật 1 bản ghi mới để kiểm việc lưu | Không |
| Thao tác / input | Đối tác chỉ mở biểu mẫu rồi đọc trường → thấy thiếu 3 trường | Mở biểu mẫu → đọc 15 nhãn (có "Số quyết định công bố", "Ngày quyết định công bố") → mở nhóm "File đính kèm" thấy vùng kéo thả (accept .pdf/.doc/.docx/.xls/.xlsx, tối đa 10 tệp, 20MB/tệp) → nhập cả 3 trường + bấm Lưu | Không |
| Trường có bị ẩn theo nhóm thu gọn không | — (vòng 1 biểu mẫu để phẳng) | Nay biểu mẫu chia 6 nhóm; 3 trường nằm ở nhóm "Công bố" + "File đính kèm", bấm tiêu đề nhóm là bung ra, không ô nào bị mất | Không |

**Bằng chứng:**
- `image/QLDMTCTV_06-v2-02-them-moi-mo-het-6-nhom-du-3-truong-cong-bo-va-tep.png` — biểu mẫu Thêm mới, thấy ô "Số quyết định công bố", ô "Ngày quyết định công bố" (có biểu tượng lịch), vùng kéo thả tệp ghi rõ giới hạn định dạng/dung lượng, nhóm "Ghi chú", 2 nút Hủy / Lưu.
- `image/QLDMTCTV_06-v2-03-nhap-3-truong-cong-bo-va-dinh-kem-tep-truoc-khi-luu.png` — đã nhập `QD-QA-A2-0804/2026`, `04/08/2026`, đính kèm `qd-cong-bo-alpha-reverify-v2.pdf (237 B)` kèm nút Xem / Xóa.
- network `POST /api/v1/to-chuc-tu-vans` [200] — 1 request, 1 thông báo "Tạo Tổ chức tư vấn thành công"; sinh `TC-BTP-TW-0012`.
- đọc lại `GET /api/v1/to-chuc-tu-vans/{id}` [200]: `soQdCongBo = "QD-QA-A2-0804/2026"`, `ngayQdCongBo = "2026-08-04"`, `fileDinhKem` có 1 tệp PDF (`trangThaiQuet: SACH`).
