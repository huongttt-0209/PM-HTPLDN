# Row 174 — QLPQCN_03 — re-verify 2026-07-25 R5

Kết quả: **PASS**. Tài khoản `admin` (QTHT), màn phân quyền vai trò **CB_PD_BN — Cán bộ Phê duyệt Bộ/Ngành** (chọn vai trò không dùng cho test khác).

## Đối chiếu tiêu chí

| Bước | Yêu cầu | Kết quả |
|---|---|---|
| 1 | Đủ 12 nhóm chức năng dạng gập-mở | ✅ **14 nhóm** — Báo cáo · Biểu mẫu · Chi trả · Chương trình HTPL doanh nghiệp · Đánh giá · Đào tạo · Doanh nghiệp · Hỏi đáp pháp luật · HTPL địa phương · Người hỗ trợ pháp lý · Quản trị hệ thống · Tư vấn nhanh · Tư vấn viên · Vụ việc HTPL |
| 2 | Nhóm "Báo cáo" có cả quyền cơ bản và quyền nghiệp vụ, tên tiếng Việt đọc hiểu được | ✅ Cơ bản đủ 6 loại: Tạo / Xem / Cập nhật / Xóa / Duyệt / Xuất. Nghiệp vụ riêng: Xem bảng điều khiển, Xem–Xuất nhật ký kiểm toán, nhóm thông báo |
| 3 | Mở thêm 2 nhóm khác, cùng cấu trúc, không nhóm nào rỗng | ✅ Mở toàn bộ 14 nhóm — **không nhóm nào rỗng**; tổng 306 dòng quyền. Chi trả và Đào tạo đều có đủ quyền cơ bản + quyền nghiệp vụ (Thẩm định / Kiểm tra / Trình phê duyệt; Công bố / Hủy công bố / Nhập / Kích hoạt…) |
| 4 | Tích 1 quyền → Lưu → tải lại còn giữ; bỏ tích → Lưu hoàn nguyên | ✅ Tích `read_audit_log` (Xem nhật ký kiểm toán) → thông báo "Đã lưu phân quyền" → tải lại trang, quyền vẫn được tích. Bỏ tích → Lưu → về đúng **102 quyền** như ban đầu |
| 5 | (chỉ ghi nhận) Ô chọn nhanh cả nhóm | Có ô chọn ở đầu mỗi nhóm — không dùng để chấm |

## So với lượt kiểm trước (sáng 25/07)

Cả hai điểm bị báo lỗi trước đó đều đã sửa:

- **Tên nhóm dùng mã kỹ thuật** — trước có 5 nhóm hiện `BIEU_MAU`, `CT_HTPLDN`, `DOANH_NGHIEP`, `NGUOI_HO_TRO`, `TU_VAN`. Nay cả 14 nhóm đều là tên tiếng Việt: "Biểu mẫu", "Chương trình HTPL doanh nghiệp", "Doanh nghiệp", "Người hỗ trợ pháp lý", "Tư vấn nhanh".
- **Tên quyền viết tiếng Việt không dấu** — trước là "Cap nhat bao cao", "Duyet bao cao", "Xem nhat ky kiem toan". Nay đã có dấu đầy đủ: "Cập nhật báo cáo", "Duyệt báo cáo", "Xem nhật ký kiểm toán". Mã kỹ thuật vẫn hiển thị nhưng ở dòng phụ dưới tên tiếng Việt.

## Ghi nhận thêm (không đủ để FAIL theo tiêu chí)

Còn **2/306** nhãn quyền chưa bỏ dấu xong: `create_doanh_nghiep` hiện "Tao doanh nghiep" và `submit_tu_van_vien` hiện "Nop lai ho so TVV (CG)". Đây vẫn là tên tiếng Việt đọc hiểu được (không phải mã kỹ thuật) nên không rơi vào điều kiện FAIL "quyền hiển thị bằng mã kỹ thuật không có tên tiếng Việt". Ghi lại để đối tác quyết có nêu riêng hay không.

Về nhóm "Tư vấn chuyên sâu" trong danh sách 12 mảng nghiệp vụ: không có panel riêng mang tên này, nhưng 9 quyền tư vấn chuyên sâu (`create/read/update/delete/approve/publish/unpublish/cancel/export_noi_dung_tu_van_cs`) đều có mặt, nằm trong nhóm Tư vấn viên. Tiêu chí cho phép tên panel lấy theo dữ liệu và không bắt trùng từng chữ, số nhóm 14 ≥ 12 → không tính thiếu nhóm.

## Ảnh hưởng dữ liệu

Vai trò CB_PD_BN đã được hoàn nguyên về đúng 102 quyền ban đầu. Tập quyền gốc lưu tại `../QLPQCN_02/quyen-goc-CB_PD_BN.json`.
