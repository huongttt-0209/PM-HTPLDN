# Tổng hợp reverify 5 bug — môi trường dev

- Môi trường: `https://18.143.165.120.nip.io`
- Phương thức: thao tác nghiệp vụ qua Chrome DevTools/UI; không gọi API trực tiếp để tạo verdict.
- Chuẩn đối chiếu: mô tả bug gốc, SRS và cột `DEV phản hồi lần 1`/nội dung BA chốt.
- Nguyên tắc: chỉ Pass khi đo đủ các điểm quyết định; thiếu bằng chứng được ghi Blocked/Inconclusive và không cập nhật Sheet.

| Dòng | Mã bug | Verdict | Google Sheet | Ghi chú quyết định |
|---:|---|---|---|---|
| 343 | THBCTHCT_01 | PASS | `Test done` (đã đọc lại) | Đủ 8/8 điểm: chọn/không chọn/not-sent, trạng thái, reload, toast và audit. |
| 379 | QLHSPLDN_QA01 | PASS | `Test done` | Đo lại trên `cbnv_tw_05`: đăng nhập mới, 2 hard reload không modal; mở Hỏi đáp 23 bản ghi và Vụ việc 60 bản ghi thành công, console 0 lỗi. |
| 308 | QLHDTVVCG_02 | PASS | `Test done` (đã đọc lại) | Đường vào contextual theo BA; 5 nhóm lọc, format/badge/progress, cảnh báo hạn và layout đều đạt. |
| 321 | QLHDTVVCG_15 | BLOCKED/INCONCLUSIVE | Không ghi | Tạo và persistence đạt; connector Chrome chặn upload file trước browser nên chưa kiểm được attachment persistence. |
| 345 | THBCTHCT_05 | PASS | `Test done` (đã đọc lại) | Xuất và mở file thật Excel + Word; tên file, TT17, A4, TNR13, khối ký và 13 chỉ tiêu đều đạt BA. |

Không có case nào được kết luận Reopen trong lượt này. Case Blocked còn lại không phải bằng chứng bug còn tồn tại và không được dùng để cập nhật `Trạng thái dev fix`.
