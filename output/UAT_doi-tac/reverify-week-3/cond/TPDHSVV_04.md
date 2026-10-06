# Bảng đối chiếu điều kiện — TPDHSVV_04

Loại bug: **phụ thuộc role + state + data + kênh nhận** (thông báo sau khi Trình phê duyệt gửi tới đúng Cán bộ Phê duyệt cùng đơn vị) → BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người trình | Header frame video: **Cán bộ NV Trung ương · CB_NV_TW**, đơn vị BTP·TW, chuông 96 | `cbnv_tw` — CB_NV_TW, đơn vị BTP·TW, là người tiếp nhận vụ việc | Không |
| Entity + trạng thái trước thao tác | Vụ việc `9ed9d021...` (VV-BTP-TW-20260709-001) ở **Đang xử lý**, có nút [Cập nhật kết quả] [Trình phê duyệt] | Vụ việc VV-BTP-TW-20260712-001 ở **Đang xử lý** (`DANG_XU_LY`), đủ 2 nút tương ứng | Không |
| Đã có kết quả hỗ trợ | Đã có — đối tác test luồng "trình phê duyệt thành công" (điều kiện 3: người hỗ trợ đã cập nhật kết quả) | Đã có — người được phân công (TVV) đã cập nhật kết quả (`POST cap-nhat-ket-qua` 201, nhóm "Kết quả hỗ trợ" hiện nội dung) | Không |
| Thao tác thực hiện | Bấm [Trình phê duyệt] → xác nhận | Bấm [Trình phê duyệt] → hộp thoại "Gửi vụ việc lên cán bộ phê duyệt?" → [Trình duyệt] | Không |
| Kết quả chuyển trạng thái | Vụ việc chuyển **Đang xử lý → Chờ phê duyệt** (đối tác báo phần này đạt) | Vụ việc chuyển sang **CHO_PHE_DUYET**, timeline ghi "Trình phê duyệt 20/07/2026 12:43", toast "Đã trình phê duyệt" | Không |
| Người nhận thông báo được kiểm tra | **Cán bộ Phê duyệt cùng đơn vị (CB_PD_TW · BTP·TW)** — đối tác đăng nhập CB_PD_TW, mở chuông → chỉ thấy thông báo đăng nhập + đăng ký đào tạo, **không có** thông báo vụ việc chờ duyệt | `cbpd_tw` — CB_PD_TW cùng đơn vị BTP·TW, là người phê duyệt vụ việc (vụ việc nằm trong danh sách "Chờ phê duyệt" của chính tài khoản này, có nút [Phê duyệt]/[Từ chối]) | Không |
| Kênh kiểm tra thông báo | Chuông trong hệ thống (in-app) | Chuông in-app (số chưa đọc + danh sách `/thong-baos`) **và** email (MailHog) — kiểm cả 2 kênh | Không |

**Kết luận: 0 GAP.** Mọi điều kiện của đối tác đều tái lập bằng test thật, đúng vai trò người trình (CB_NV_TW), đúng trạng thái (Đang xử lý, đã có kết quả), đúng người nhận cần kiểm (CB_PD_TW cùng đơn vị — là người phê duyệt thực sự của vụ việc). Chiều "kênh kiểm tra" mình đo **chặt hơn** đối tác (in-app + email, có mốc baseline trước/sau) — chặt hơn không tạo GAP.

**Đo lường:**
- Baseline CB_PD_TW trước khi trình: chuông = **27 chưa đọc**, thông báo mới nhất **16/07/2026**, không có thông báo nào về vụ việc này; email = 18 thư, **toàn bộ là mã OTP đăng nhập**, 0 thư nghiệp vụ.
- Sau khi CB_NV_TW trình phê duyệt (vụ việc → Chờ phê duyệt, 20/07/2026 12:43): CB_PD_TW chuông **vẫn 27**, thông báo mới nhất **vẫn 16/07**, **không** có thông báo về vụ việc; email **vẫn 0 thư nghiệp vụ**.
- Loại trừ nhiễu: CB_PD_TW **vẫn nhận** thông báo "chờ phê duyệt" cho khóa học + hồ sơ TVV → kênh thông báo hoạt động, chỉ **thiếu riêng** thông báo trình phê duyệt vụ việc. Vụ việc đã nằm trong hàng chờ phê duyệt của đúng CB_PD_TW → không phải sai người nhận.

Chi tiết diễn biến + phép đo: xem [`../reverify-audit/TPDHSVV_04/audit.md`](../reverify-audit/TPDHSVV_04/audit.md).
