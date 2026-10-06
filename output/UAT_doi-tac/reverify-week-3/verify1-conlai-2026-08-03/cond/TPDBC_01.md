# Bảng đối chiếu điều kiện — TPDBC_01 (row 316, tab UAT_TGPL Doanh Nghiệp-tuần 3)

| Điều kiện có thể đổi kết quả | Đối tác (từ video bằng chứng, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản người trình báo cáo | Cán bộ NV Trung ương, vai trò CB_NV_TW, phạm vi BTP · TW (frame t000/t003) | cbnv_tw_04 — vai trò CB_NV_TW, capDonVi TW, donViId 00000000-0000-4000-8000-000000000001 | Không |
| Vai trò / tài khoản người nhận thông báo | Cán bộ PD Trung ương, vai trò CB_PD_TW, phạm vi BTP · TW — cùng đơn vị người trình (frame t018/t024) | cbpd_tw_04 VÀ cbpd_tw_01 — đều vai trò CB_PD_TW, capDonVi TW, cùng donViId 00000000-0000-4000-8000-000000000001 với người trình | Không |
| Entity + trạng thái trước thao tác | Kế hoạch đánh giá (đợt đánh giá) đang ở bước lập báo cáo, còn nút "Trình phê duyệt" ở màn chi tiết (frame t000) | Kế hoạch đánh giá DG-20260725-0001, trạng thái "Lập báo cáo" (BAO_CAO), stepper bước 7, nút "Trình phê duyệt" khả dụng | Không |
| Dữ liệu tiền đề (báo cáo đã lưu) | Đợt đã có kết quả chấm điểm và số liệu tổng hợp hiển thị ở màn báo cáo: tổng số vụ việc 1, đã đánh giá 1, điểm trung bình 10 (frame t000/t003) | Báo cáo BCDG-20260725-0001 đã lưu (bản sửa lần 3), đợt có tổng số vụ việc 1, đã đánh giá 1, điểm trung bình 8.0 | Không |
| Thao tác + input | Bấm "Trình phê duyệt" tại màn chi tiết đợt đánh giá; không nhập thêm dữ liệu | Bấm "Trình phê duyệt" tại tab "Báo cáo" của màn chi tiết, xác nhận hộp thoại "Trình phê duyệt báo cáo?"; không nhập thêm dữ liệu | Không |
| Trạng thái sau thao tác | Đợt chuyển sang "Chờ phê duyệt" (frame t021 — dòng đợt hiển thị badge Chờ phê duyệt) | Đợt chuyển sang "Chờ phê duyệt", stepper nhảy bước 8 | Không |

**Ghi chú đóng GAP (không phải bảng thứ hai):**

- Đối tác dùng chính tài khoản `cbpd_tw`. Trên môi trường được giao, `cbpd_tw` đăng nhập FAIL (401) từ 30/07/2026 — đã ghi trong `input/input.md`. Áp Rule 7 (fallback CÙNG vai trò CB_PD_TW + CÙNG cấp TW): dùng `cbpd_tw_04`, và kiểm chứng thêm `cbpd_tw_01` để loại trừ khả năng thông báo chỉ tới đúng một người. Cả hai đều cùng `donViId` với người trình ⇒ điều kiện "cán bộ phê duyệt cùng đơn vị" được giữ nguyên.
- Chênh lệch điểm trung bình (10 của đối tác vs 8.0 của mình) không nằm trong đường dẫn sinh thông báo: thông báo được sinh ở bước chuyển trạng thái BAO_CAO → CHO_PHE_DUYET, không phụ thuộc điểm. Đã kiểm chứng bằng thao tác thật, không bằng lập luận: cùng thao tác đó, hai tài khoản phê duyệt cùng đơn vị đều nhận thông báo.
