# Bảng đối chiếu điều kiện — TPDBC_02

Loại bug: **Nút "Trình phê duyệt" hiện dù đợt sai state / báo cáo chưa lưu.** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) nút có thực sự hiện sai trạng thái không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP) | Không |
| Trạng thái đợt khi nút hiện | "sai state" | API xác nhận đợt trangThai=BAO_CAO (đúng state để trình) | Không |
| Trạng thái báo cáo | "chưa lưu" | Báo cáo BCDG-...-0001 record đã tồn tại (DU_THAO, auto-lưu); Nội dung/Nhận xét/Kiến nghị trống nhưng SRS để optional | Không |
| Hành vi bấm nút | — | Hộp xác nhận → trình thành công (toast "Đã trình phê duyệt") | Không |

**Kết luận: 0 GAP role/state.** Không tái hiện "sai state": nút gate theo state (vắng ở Thực hiện/Đang đánh giá, chỉ hiện ở giai đoạn báo cáo — re-verify live 2026-07-23), báo cáo đã auto-lưu (Dự thảo) khi nút hiện. Đối tác có bằng chứng ⇒ không Reject. → **Resolved** (Verify).
