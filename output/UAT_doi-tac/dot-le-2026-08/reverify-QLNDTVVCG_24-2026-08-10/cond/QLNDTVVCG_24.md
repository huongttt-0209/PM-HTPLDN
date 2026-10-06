# Bảng đối chiếu điều kiện — QLNDTVVCG_24 (re-verify 10/08/2026)

Loại claim: sự kiện *"chuyên gia được phân công bấm Chấp nhận"* phải sinh thông báo cho **doanh nghiệp** và **cán bộ nghiệp vụ phụ trách**.

| Điều kiện có thể đổi kết quả | Bug gốc (đối tác, 03/08 · V1.0.3) | Mình test 10/08 | GAP? |
|---|---|---|---|
| Bản dựng + môi trường | HTPLDN · V1.0.3 trên env nghiệm thu `ospgroup` | **V1.0.10 trên CHÍNH env `ospgroup`** (2 lượt) + đối chiếu thêm trên dev `nip.io` | Không — đã đóng GAP môi trường của bản báo cáo trước |
| Vai trò thao tác | Chuyên gia được phân công (`huongcg`, CG + TVV, BTP · TW) | Chuyên gia được phân công (`truong_16` — Trương Văn Mười Sáu, loại CG, HOAT_DONG, BTP · TW) | Không — cùng loại CG, cùng đơn vị. Khác: `huongcg` có thêm vai trò TVV (chi tiết ở ghi chú dưới) |
| Trạng thái bản ghi trước thao tác | Đã phân công (PHAN_CONG) | Đã phân công — vừa phân công lúc 07:03:30 / 07:11:16 nên **chưa quá SLA 2 ngày LV** (bước 3, `:189`) | Không |
| Bản ghi + doanh nghiệp | `TVCS-20260803-0001`, DN *TKM Company* | Lượt 1 `TVCS-20260608-0001` (*Cty Verify Dup*) · **Lượt 2 `TVCS-20260810-0001` — đúng DN *TKM Company*, email `tkm@gmail.com`** | Không |
| Loại người được phân công | CG | CG (hệ thống chỉ nhận loại CG — BA chốt 06/08, `:172`) | Không — dạng "TVV" không còn là kịch bản hợp lệ |
| Kênh thông báo được coi là đạt | Đối tác chỉ ghi "không nhận được thông báo", không nói kênh | Chấm theo SRS **đã sửa sau BA chốt 06/08**: CB NV in-app + email; **DN chỉ thư điện tử** tới `DOANH_NGHIEP.email` (`:192`) | Không |
| Kênh email của hệ thống có sống không | Không nêu | **Control:** bước *phân công* gửi email thật cho CG ở cả 2 lượt (848→849, 855→856) ⇒ nếu bước xác nhận không gửi thì là thiếu sót tính năng, không phải SMTP hỏng | Không |
| Bộ đo có bị nhân bản không | — | Tự kiểm bộ bắt thông báo trước mỗi lượt: `soObserverDangSong = 1` | Không |
| Kết quả quan sát được | DN mở chuông: không có mục nào về bản ghi · CB NV mở chuông: không có mục nào về bản ghi | DN: **có thư điện tử** đúng mốc giây, **không** có in-app (đúng `hien_trong_ung_dung = 0`) · CB NV: **có in-app + có thư điện tử** đúng mốc giây | Không |

**Kết luận: 0 GAP.** Vế nghiệp vụ đối tác phản ánh **không tái hiện** trên chính môi trường nghiệm thu.

> **Chốt trước/sau trên cùng một DN:** chuông của TKM Company vẫn còn mục *"Chuyên gia đã xác nhận tư vấn:
> TVCS-20260803-0003"* ngày 04/08 (hành vi cũ), nhưng cùng sự kiện ngày 10/08 **không** sinh mục in-app nào —
> chỉ có thư tới `tkm@gmail.com`. Đây là đổi kênh có chủ đích, không phải mất thông báo.

> **Ghi chú về khác biệt vai trò tài khoản CG:** `huongcg` (đối tác dùng) có CG + TVV; `truong_16` (mình dùng)
> chỉ có CG. Khác biệt này **không** ảnh hưởng kết quả đo — luồng `POST …/xac-nhan` và bộ thông báo sinh ra
> giống hệt nhau. Nhưng nó làm lộ một vấn đề khác: tài khoản chỉ-CG **không có menu vào bản ghi**
> (xem mục 8.2 của báo cáo) — đã ghi thành bug candidate riêng, không gộp vào phiếu này.

> **Vì sao không dùng đúng `huongcg`:** mật khẩu `Test@1234` bị từ chối (`ERR-AUTH-LOGIN-01`). Dừng ngay sau
> 1 lần thử, không đoán tiếp (giới hạn 5 lượt/60 giây) và **không** đặt lại mật khẩu tài khoản của đối tác.
