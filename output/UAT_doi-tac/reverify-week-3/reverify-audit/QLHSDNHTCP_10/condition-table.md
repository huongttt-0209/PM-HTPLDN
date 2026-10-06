# Bảng đối chiếu điều kiện — QLHSDNHTCP_10

| Điều kiện | Đối tác (evidence QLHSDNHTCP_10.jpg) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ TW (CB_NV_TW), env ospgroup.vn | cbnv_tw (CB_NV_TW), env 18.143.165.120 | Không |
| Màn hình | Chi tiết hồ sơ chi trả — thanh thông tin tổng quan (Nhóm 0) | Cùng màn Chi tiết, thanh tổng quan | Không |
| Trạng thái hồ sơ | Yêu cầu bổ sung (HSCT000066) | Yêu cầu bổ sung (CT-SEED-103) | Không |
| SLA có giá trị cảnh báo | "Quá hạn 58 ngày LV" (badge) | "Quá hạn 3 ngày LV" (badge đỏ) | Không |

- Cả 4 điều kiện match điều kiện đối tác (cùng vai trò, cùng màn, cùng state Yêu cầu bổ sung, SLA đều có giá trị) → 0 GAP.
- Khác biệt duy nhất là **giá trị đếm ngược** (58 vs 3 ngày) do deadline seed khác — không ảnh hưởng bản chất format. Cả 2 build đều hiển thị SLA dạng "đếm ngược + màu", không phải 4 nhãn mức rời BR-CALC-03 → format tái hiện đồng nhất.
