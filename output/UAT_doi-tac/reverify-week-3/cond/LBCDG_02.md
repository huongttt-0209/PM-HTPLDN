# Bảng đối chiếu điều kiện — LBCDG_02

Loại bug: **Trường thông tin màn Lập báo cáo không giống thiết kế.** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS prescribe bộ trường báo cáo.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP) | Không |
| Trạng thái đợt | Tab Báo cáo (BAO_CAO) | Đợt DGHQ-B1 ở BAO_CAO, tab Báo cáo | Không |
| Đối tượng so sánh | Bộ trường báo cáo | App form edit: Tiêu đề, Nội dung, Nhận xét tổng thể, Kiến nghị + "Số liệu tổng hợp" rút gọn | Không |

**Kết luận: 0 GAP role/state.** SRS FR-VI-07 Inputs nhập tay = kp_hoat_dong_khac, kp_xa_hoi_hoa, nhan_xet_tong_the, kien_nghi + bảng 13 cột số liệu TT17/2025. App thiếu 2 ô KP + 13 cột số liệu, thừa "Nội dung"; "Số liệu tổng hợp" rút gọn. Trường app lệch cả SRS lẫn thiết kế đối tác; SRS mô tả template TT17 phức tạp, app rút gọn → cần BA chốt scope. → **BA confirm**.
