# Condition table — BUG-EM-HDD-006 (R4 — Chờ BA)

| Nhánh | Kỳ vọng theo SRS v3.5 | Trạng thái R4 | Kết luận |
|---|---|---|---|
| `QUA_HAN` | In-app + email cho CB_NV xử lý và CB_PD quản lý/cùng đơn vị (`FR-II-CROSS-01`, BR-SLA-03) | Baseline R3 chứng minh CB_PD chưa nhận; Dev chưa báo fix | Chưa retest |
| `QUA_HAN_NGHIEM_TRONG` — CBPD cùng đơn vị | In-app + email cho CB_NV + CB_PD | Chưa có bản fix | Chưa retest |
| `QUA_HAN_NGHIEM_TRONG` — escalation | Thêm `escalate`; EC-01/bảng thông báo dùng CB_PD cấp trên | Dev đang chờ BA xác nhận đích/cách áp dụng cho SLA Hỏi đáp | Chờ BA |
| Tính đúng mức và chống gửi lặp | Job 30 phút, chỉ gửi khi chuyển mức | Baseline R3 đã chạy đúng phần này | Không thuộc phần chờ fix |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** CHỜ BA, chưa retest và không tính Reopen. Khi BA xác nhận đích escalation và Dev báo fix, cần chạy đủ hai mốc `QUA_HAN` và `QUA_HAN_NGHIEM_TRONG`, kiểm CB_NV, CB_PD cùng đơn vị, CB_PD cấp trên và mailbox âm.
