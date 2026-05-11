# Tổng hợp các nội dung Cross-cutting cần BA xác nhận - Round 7

**Ngày tổng hợp:** 2026-05-11  
**Nguồn đọc:** `tasks/todo-cross-cutting.md`

Report này chỉ liệt kê các nội dung Cross-cutting đang cần BA xác nhận. Không đưa các task đã pass, các bug đã rõ hướng dev fix, hoặc các note không cần BA.

## Bảng tổng hợp

| Nhóm | Số mục cần BA xác nhận | Nội dung chính |
|---|---:|---|
| Edge / Security | 1 | Có cần áp dụng CSRF token cho hệ thống hiện tại không |
| Profile / Đổi mật khẩu | 1 | Rule độ mạnh mật khẩu dùng 3 yếu tố hay 4 yếu tố |
| E2E DN full luồng | 1 | Chốt cách hiểu BR-CALC-04 cấp |
| **Tổng** | **3** |  |

## Edge / Security

### 1. Có cần áp dụng CSRF token không?

Trong task R7.7.17, report ghi cần BA xác nhận `BR-EC-06`. Đây là rule liên quan đến CSRF protection.

Hiện hệ thống đang dùng cơ chế đăng nhập bằng Bearer/JWT token. Với cách này, câu hỏi là rule CSRF trong spec có còn áp dụng như hệ thống dùng cookie session hay không.

**Cần BA xác nhận:** Hệ thống có bắt buộc phải enforce `X-CSRF-Token` không? Nếu hệ thống dùng Bearer/JWT token và BA xác nhận không cần CSRF token, thì spec `BR-EC-06` nên được cập nhật lại cho rõ.

**Nguồn:** `tasks/todo-cross-cutting.md` - R7.7.17

## Profile / Đổi mật khẩu

### 1. Rule độ mạnh mật khẩu khi đổi mật khẩu trong Profile

Trong task R7.8.4, report ghi còn một spec gap về rule độ mạnh mật khẩu.

Hiện có hai cách hiểu:

- Rule trong Profile đang được hiểu là cần 3 yếu tố.
- FR-VIII-26 lại yêu cầu 4 yếu tố, bao gồm ký tự đặc biệt.

BE/UI hiện đang đi theo rule chặt hơn, tức yêu cầu đủ 4 yếu tố và có ký tự đặc biệt. Đây là hướng an toàn hơn, nhưng cần BA chốt để Dev và QA thống nhất theo một rule chính thức.

**Cần BA xác nhận:** Đổi mật khẩu trong Profile dùng rule 3 yếu tố hay rule 4 yếu tố có ký tự đặc biệt?

**Nguồn:** `tasks/todo-cross-cutting.md` - R7.8.4

## E2E DN full luồng

### 1. Cách hiểu BR-CALC-04 cấp trong full luồng DN

Trong task R7.8.7, report ghi cần BA xác nhận `BR-CALC-04 cấp`.

Đây là rule liên quan đến cách xác định/cấp mức theo dữ liệu doanh nghiệp trong full luồng DN: đăng ký, tạo vụ việc, đánh giá, chi trả. Report ghi phần seam BR-CALC-04 đã pass, nhưng vẫn cần BA chốt cách hiểu rule để QA và Dev không lệch nhau khi chạy E2E.

**Cần BA xác nhận:** BR-CALC-04 cấp phải được hiểu và áp dụng chính xác như thế nào trong full luồng DN?

**Nguồn:** `tasks/todo-cross-cutting.md` - R7.8.7
