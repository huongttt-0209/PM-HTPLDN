# Bảng đối chiếu điều kiện — DKTGMLTVV_11 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | NHT (đối tác); bug ghi kiểm chéo CB_NV_TW cho kết quả như nhau | CB_NV_TW — `cbnv_tw` (role-independent theo ghi chú bug) | Không |
| Màn / field | Form Thêm mới TVV, trường "File đính kèm (Bằng cấp / Chứng chỉ)" giới hạn 10 tệp | `/chuyen-gia-tvv/tao-moi`, input "File đính kèm" (multiple, .pdf, max 10) | Không |
| Thao tác | Chọn 11 tệp `.pdf` cùng lúc → quan sát danh sách + mọi thông báo (nhánh SỐ LƯỢNG) | Nạp 11 tệp `.pdf` (DataTransfer) → hệ thống hiển thị thông báo "Chỉ được tải tối đa 10 tệp." (bắt qua `MutationObserver` + `.ant-message-notice`) | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix**. Nhánh số lượng (>10 tệp) nay CÓ hiển thị thông báo lỗi ("Chỉ được tải tối đa 10 tệp.") — trước đây lặng lẽ bỏ tệp thứ 11 không báo. Đáp ứng yêu cầu SRS FR-IV-01 §E7 (phải hiển thị thông báo lỗi khi vượt 10 tệp); từ ngữ thông báo do dev chọn.
