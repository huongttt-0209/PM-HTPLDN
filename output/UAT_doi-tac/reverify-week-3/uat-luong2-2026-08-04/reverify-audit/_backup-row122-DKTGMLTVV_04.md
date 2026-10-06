# Sao lưu nguyên văn dòng 122 — DKTGMLTVV_04 (trước khi QA ghi đè cột R)

## Mã TC

DKTGMLTVV_04

## Mô tả

Kiểm tra hiển thị Nhóm 3  Tổ chức và Mạng lưới

## Điều kiện

1. Đăng nhập tài khoản

## Dữ liệu đầu vào

(trống)

## Các bước thực hiện

1. Chọn menu "Mạng lướt tư vấn viên" -> "Tư vấn viên/Chuyên gia"
2. Chọn tab "Mới đăng ký"
3. Nhấn Thêm mới

## Kết quả mong đợi

- Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị

## Kết quả thực tế

- Nhóm 3 — Lĩnh vực pháp luật và Tổ chức:  SRS quy định chỉ hiển thị các trường Lĩnh vực pháp luật đăng ký, Tổ chức tư vấn chủ quản. Nhưng hệ thống hiển thị nhiều hơn

## Ảnh/vieo 1

DKTGMLTVV_04_v2.jpg

## Trạng thái 1

Fail

## Trạng thái dev fix 1

BA confirm

## Verify

BA confirm

## DEV phản hồi lần 1

⚠️ Cần BA xác nhận — trạng thái: CHỜ BA XÁC NHẬN (chưa phải việc của dev).
- Kiểm tra lại trên web (vai trò Người hỗ trợ pháp lý, màn Thêm mới Tư vấn viên): nhóm "Tổ chức & Mạng lưới" hiển thị đúng 3 trường — "Tổ chức hành nghề chính", "Tổ chức đối tác", "Lĩnh vực pháp luật" (bắt buộc). Không có trường thứ 4. Đã kiểm cả 2 giá trị của ô "Loại" (Tư vấn viên và Chuyên gia), số trường không đổi.
- ⚠️ Như vậy quan sát của bên kiểm thử là chính xác: web đang hiển thị nhiều hơn 2 trường. Phần cần chốt là ĐẶC TẢ, không phải lỗi phần mềm.
- Theo SRS v3.5 hiện hành — FR-IV-03 (UC41), màn SCR-IV-02 (dòng 1470), bảng thành phần dòng 1514-1517 — nhóm 3 gồm đúng 3 mục: 4.1 Tổ chức chính (dòng 1515), 4.2 Tổ chức đối tác (dòng 1516), 4.3 Lĩnh vực pháp luật bắt buộc (dòng 1517). Web khớp 100% bản này.
- Kỳ vọng "chỉ 2 trường" đang bám bản SRS bàn giao lần 2 ngày 10/7. Hai bản tài liệu lệch nhau ở đúng trường "Tổ chức đối tác".
- ⚠️ Đề nghị BA xác nhận 2 điểm:
  (1) Bản SRS nào là chuẩn cho nhóm 3 màn SCR-IV-02: bản v3.5 (3 trường) hay bản bàn giao 10/7 (2 trường)?
  (2) Trường "Tổ chức đối tác" (SRS v3.5 dòng 1516, quan hệ nhiều-nhiều) có giữ trên form Thêm mới Tư vấn viên không? Lưu ý BA đã chốt mục 4.1 cùng nhóm này ngày 30/07/2026 (case DKTGMLTVV_03) và giữ nguyên mục 4.2.
- Chốt xong xin cập nhật đồng bộ cả 2 bản tài liệu để tránh lệch tiếp.
- Verify: tài khoản Người hỗ trợ pháp lý cấp Trung ương, bản dựng V1.0.5, ngày 03/08/2026.
