# Condition table — BUG-EM-DN-004 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Hồ sơ DN có trước | Hồ sơ do cán bộ tạo, chưa có tài khoản | DN `DN-01-0009`, MST `0127000002`, tạo bởi `cbnv_tw_03` lúc `2026-08-24T10:53:19Z` | Không |
| Claim Flow | DN dùng MST để nhận lại quyền truy cập | Tài khoản DN `3499f94a-6075-4174-9cf2-2d92ddd13cdf` được tạo lúc `2026-08-24T10:53:35.811Z`, gắn cùng MST | Không |
| Mã audit | Phải là `DN_CLAIM` | API audit trả `hanhDong = DN_CLAIM`, id `87e170a4-7541-4984-b71d-dc4ff39c2476` | Không |
| Nhãn UI | Phải phân biệt với tự đăng ký | Nhật ký hệ thống hiển thị “Doanh nghiệp nhận lại quyền truy cập (Claim)” | Không |
| Không dùng nhãn cũ | Không được là `SELF_REGISTER_DN` / “Doanh nghiệp tự đăng ký” | Bản ghi Claim chỉ có `DN_CLAIM`; không còn nhãn cũ | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — luồng Claim đã có mã audit riêng `DN_CLAIM` và nhãn UI phân biệt rõ với tự đăng ký.

**Ghi chú kiểm thử:** một MST mới được tạo trong R3 nhưng endpoint Quên mật khẩu bị rate-limit môi trường; verdict dựa trên bản ghi Claim post-fix gần nhất, được đối chiếu trực tiếp lại bằng UI và API trong phiên R3.
