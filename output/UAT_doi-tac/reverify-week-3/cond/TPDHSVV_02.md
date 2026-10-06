# Bảng đối chiếu điều kiện — TPDHSVV_02

Loại bug: **phụ thuộc role + state + data** (thông báo chặn khi Trình phê duyệt phụ thuộc vai trò người thao tác, trạng thái vụ việc và việc đã/chưa có kết quả hỗ trợ) → BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Header frame: **Cán bộ NV Trung ương · CB_NV_TW**, đơn vị BTP·TW, chuông 96 | `cbnv_tw` — `auth/me` trả `["CB_NV_TW"]`, đơn vị BTP·TW, là `nguoiTiepNhanId` của vụ việc | Không |
| Entity + trạng thái trước thao tác | Vụ việc `9ed9d021...` (**VV-BTP-TW-20260709-001**) ở **Đang xử lý**, có nút [Cập nhật kết quả] [Trình phê duyệt] | Vụ việc VV-BTP-TW-20260712-001 ở **Đang xử lý** (`trangThai=DANG_XU_LY`), có đủ 2 nút tương ứng | Không |
| Đã/chưa có kết quả hỗ trợ | Chưa có — nhóm "Kết quả hỗ trợ" trống, thông báo chặn nói "chưa có kết quả xử lý từ tư vấn viên" | Chưa có — API `coKetQua=false`, nhóm "Kết quả hỗ trợ" hiện "Tư vấn viên chưa cập nhật kết quả" | Không |
| Thao tác thực hiện | Bấm [Trình phê duyệt] (khi chưa có kết quả) | Bấm [Trình phê duyệt] → hộp thoại xác nhận "Gửi vụ việc lên cán bộ phê duyệt?" → [Trình duyệt] | Không |
| Cách quan sát số thông báo | Nhìn màn hình — thấy **2 khung thông báo** lỗi chồng nhau | Đo bằng `tools/toast-capture.js` (không lọc trùng, đọc innerText, tự kiểm observer=1) **+ đếm DOM `.ant-message-notice-wrapper` suốt vòng đời toast**, lặp 4 lần | Không |

**Kết luận: 0 GAP.** Mọi điều kiện của đối tác đều tái lập bằng test thật, đúng vai trò (CB_NV_TW), đúng trạng thái (Đang xử lý), đúng tiền đề (chưa có kết quả hỗ trợ). Riêng chiều "cách quan sát" mình đo **chặt hơn** đối tác (observer no-dedupe + đếm DOM theo thời gian) — chặt hơn không tạo GAP, chỉ làm kết luận chắc hơn.

**Đo lường (4 lần chạy):** mỗi lần đúng **1 request** `POST .../trinh-phe-duyet` + **1 khung thông báo** "Chưa có kết quả xử lý từ tư vấn viên"; đếm DOM `.ant-message-notice-wrapper` tại 7 mốc thời gian (150ms→2600ms) đều = **1**; tự kiểm `soObserverDangSong=1`. **Không nhân đôi.** Vụ việc giữ nguyên "Đang xử lý" (chặn đúng).

Chi tiết diễn biến + phép đo: xem [`../reverify-audit/TPDHSVV_02/audit.md`](../reverify-audit/TPDHSVV_02/audit.md).
