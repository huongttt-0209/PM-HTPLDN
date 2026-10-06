# Condition table — BUG-EM-DT-004 (R4 — Chờ BA)

| Điểm đối chiếu | Căn cứ | Đánh giá R4 | Trạng thái |
|---|---|---|---|
| Đối tượng logic | “Tạo thông báo ... cho từng học viên” | Có thể hiểu mỗi kết quả học viên là một sự kiện | Cần BA chốt |
| Đích tài khoản/email | “in-app + email theo TK doanh nghiệp / NHT đã đăng ký HV” | Chỉ rõ nguồn nhận là `nguoiDangKyId → TAI_KHOAN.email`, không phải mặc định `HOC_VIEN.email` | Cần BA chốt cách áp dụng với học viên nhập tay/không có `nguoiDangKyId` |
| Bằng chứng R3 | Chỉ đếm `qa.hv.rv5.hai@htpldn.test` sau công bố | Không chứng minh được hộp thư của TK DN/NHT đăng ký có hay không nhận | Không đủ để Reopen |
| Tình trạng bản sửa | Dev phản hồi đang chờ BA chốt và chưa xác nhận đã fix trọn nhánh | Không có bản fix đã chốt để retest | Chưa chạy |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** CHỜ BA, chưa retest và không tính Reopen. Sau khi BA chốt người nhận/fallback và Dev báo đã fix, phải dựng fixture có `nguoiDangKyId` rõ ràng rồi kiểm cả in-app lẫn `TAI_KHOAN.email` của đúng DN/NHT đăng ký.
