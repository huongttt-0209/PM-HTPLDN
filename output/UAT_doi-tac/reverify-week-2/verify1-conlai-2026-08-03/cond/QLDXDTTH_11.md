# Bảng đối chiếu điều kiện — QLDXDTTH_11

> Lỗi do QA tự phát hiện khi verify QLDXDTTH_01 (không có phản ánh đối tác) → cột giữa ghi điều kiện của **bug gốc do QA đo**.

| Điều kiện có thể đổi kết quả | Điều kiện khi phát hiện lỗi | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ thuộc **đúng đơn vị tiếp nhận** của đề xuất (cbnv_hn, CB_NV_DP, Sở Tư pháp Hà Nội) | Chính tài khoản đó — mã đơn vị trùng khít đơn vị tiếp nhận của bản ghi | Không |
| Entity + trạng thái | Đề xuất đào tạo `QA-VERIFY-0803`, trạng thái **Mới gửi** (MOI_GUI) | Chính bản ghi đó, trạng thái Mới gửi | Không |
| Dữ liệu tiền đề | Đề xuất do tài khoản Doanh nghiệp cùng đơn vị gửi lên trong cùng phiên | Đúng bản ghi vừa gửi, đã xác nhận cặp gửi↔nhận khớp đơn vị | Không |
| Input / filter | Mở tab "Đề xuất đào tạo", xem cột Hành động + mở màn chi tiết | Như vậy, đã xem cả danh sách lẫn màn chi tiết | Không |

**Kết luận: 0 GAP.** Cột "Hành động" của mọi dòng là dấu gạch ngang; màn chi tiết chỉ có nút "Quay lại danh sách"; đồng thời nút "Gửi đề xuất mới" lại hiện với vai trò cán bộ.

**Vì sao `BA confirm` chứ không `Open`:** đặc tả tự mâu thuẫn — FR-III-13 (UC32) dòng 1045 + SCR-III-01 Thành phần 8 dòng 1875 giao việc tiếp nhận cho CB NV, nhưng Ma trận phân quyền (srs-v3.5.md dòng 1309) chỉ cấp quyền ĐỌC cho mọi vai trò cán bộ. Cần BA chốt trước khi dev sửa.
