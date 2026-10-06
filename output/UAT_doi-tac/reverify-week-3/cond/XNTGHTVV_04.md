# Bảng đối chiếu điều kiện — XNTGHTVV_04

Loại bug: **phụ thuộc role + state + data + người nhận thông báo** (workflow) → BẮT BUỘC điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | `huongcg` — vai trò **TVV · CG**, đơn vị **BTP · TW**, là người được phân công (frame t000/t008 header + cột Người xử lý = huongcg) | `qa_tvvseed28` — vai trò **TVV · CG**, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp = **BTP · TW**; `auth/me` trả `["TVV","CG"]`; là `nguoiXuLyId` của VV | Không |
| Entity + trạng thái trước thao tác | VV-BTP-TW-20260709-001 ở **Đã phân công**, detail đủ 2 nút [Chấp nhận] [Từ chối], stepper bước 5 (frame t008) | VV-BTP-TW-20260712-001 ở **Đã phân công**, đủ 2 nút [Chấp nhận] [Từ chối], stepper bước 5, bản ghi phân công "Chờ xác nhận" (ảnh `11-truoc-khi-chap-nhan.png`) | Không |
| Người nhận thông báo (CB NV phụ trách) | Trường "Người tiếp nhận" = **Cán bộ NV Trung ương**, đối tác bôi đen nhấn mạnh (frame t008); sau đó đăng nhập đúng `cbnv_tw` để kiểm chuông (frame t016/t024) | `nguoiTiepNhanId` của VV = `f2e93500-f6dd-4660-a3f6-de7326acffd1` = đúng userId `cbnv_tw` (đối chiếu `nguoiNhanId` trên thông báo của chính tài khoản này) | Không |
| Thao tác thực hiện | Bấm [Chấp nhận] → hộp thoại "Chấp nhận phân công" → xác nhận (frame t008 → t012 chuyển Đang xử lý) | Bấm [Chấp nhận] → hộp thoại "Chấp nhận phân công" ("Bạn xác nhận tham gia hỗ trợ vụ việc này?") → [Chấp nhận] | Không |
| Kênh kiểm tra thông báo | Chuông in-app của `cbnv_tw` — 5 mục mới nhất, không có mục nào về vụ việc (frame t024) | Chuông in-app `cbnv_tw` (ảnh `BUG-XNTGHTVV_04-chuong-thong-bao-cbnv.png`) **+ mở rộng thêm** hộp thư email MailHog — kiểm cả 2 kênh mà BR-NOTIF-01 yêu cầu | Không |

**Kết luận: 0 GAP.** Mọi điều kiện của đối tác đều được tái lập bằng test thật, không đóng bằng lập luận. Riêng chiều "kênh kiểm tra" tôi kiểm **rộng hơn** đối tác (thêm email) — rộng hơn không tạo GAP, chỉ làm kết luận chắc hơn.

**Đo lường:** trước thao tác `cbnv_tw` có 117 thông báo (0 thông báo loại VU_VIEC), MailHog 311 thư. Sau thao tác (04:30:32Z): thông báo vẫn **117**, vẫn **0** loại VU_VIEC, **0** thông báo tạo sau mốc chấp nhận; MailHog không phát sinh thư nào sau 04:29:04Z.

Chi tiết diễn biến video, phép đo và trích dẫn SRS: xem [`../reverify-audit/XNTGHTVV_04/audit.md`](../reverify-audit/XNTGHTVV_04/audit.md).
