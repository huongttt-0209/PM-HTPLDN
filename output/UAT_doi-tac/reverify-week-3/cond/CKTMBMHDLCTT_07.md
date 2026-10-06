# Bảng đối chiếu điều kiện — CKTMBMHDLCTT_07 (row 93)

Bug loại **Trạng thái UI sau thao tác bulk theo state** (selection sau công khai hàng loạt) → bắt buộc bảng điều kiện.

| Điều kiện | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW) | cbnv_tw — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Thư mục chọn | 2 thư mục đủ điều kiện công khai (trạng thái Đã ẩn/Nháp, có biểu mẫu) | 2 thư mục Đã ẩn có BM: QA Hidden Folder 715 (1 BM) + Thư mục biểu mẫu seed (3 BM) | Không |
| Thao tác | Công khai hàng loạt 2 thư mục | Công khai hàng loạt 2 thư mục | Không |
| Kết quả thao tác | Công khai thành công (toast "Đã công khai 2 thư mục.") | Công khai thành công (toast "Đã công khai 2 thư mục.", 2 thư mục → CONG_KHAI) | Không |

**Kết luận GAP:** 0 GAP trên điều kiện cốt lõi — cùng vai trò, cùng 2 thư mục đủ điều kiện, cùng thao tác công khai hàng loạt, cùng kết quả công khai thành công.
**Khác biệt không ảnh hưởng kết quả:** đối tác đứng tab "Đã ẩn" (2 thư mục vừa công khai rời khỏi tab → selection "bóng ma"), mình đứng tab "Tất cả" (2 thư mục vẫn hiện + vẫn tích). Cả hai đều cho CÙNG lỗi: **thanh "Đã chọn 2 thư mục" + nút bulk KHÔNG xóa sau khi công khai hàng loạt xong.**

**Quan sát (mình test):**
- Toast (observer, 1 toast, không nhân đôi): *"Đã công khai 2 thư mục."*
- Network: 1 request `POST /api/v1/thu-muc-bieu-maus/batch-cong-khai`.
- After-state: 715 + seed → "Đã công khai" (CONG_KHAI). Thanh **"Đã chọn 2 thư mục"** vẫn hiển thị + [Công khai/Ẩn/Xóa hàng loạt] + [Bỏ chọn] vẫn hiện + 2 checkbox vẫn tích (`anyRowChecked=true`).

**Đối chiếu SRS — vì sao BA confirm (KHÔNG Open):**
- `srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14): bar bulk hiển thị **"khi chọn nhiều"** — chỉ định điều kiện HIỂN THỊ, không định nghĩa xóa selection sau khi thao tác xong.
- `srs-fr-09-bieu-mau.md:261-262` (FR-VII-03 Postconditions UC94): chỉ về Cổng PLQG PULL + không cần phê duyệt; KHÔNG có postcondition về UI selection.
- FR-VII-03 đặc tả đơn thư mục; KHÔNG có FR bulk riêng → SRS im lặng về deselect sau bulk.

→ Không clause SRS bị vi phạm (dẫn line rõ), hệ thống KHÔNG chặn luồng hợp lệ (công khai hàng loạt vẫn thành công). Kỳ vọng đối tác (selection tự xóa) là chuẩn UX nhưng SRS không quy định → Protocol §Verdict (dòng 75, 79): **BA confirm**.

**Ghi chú cụm:** cùng gốc case 95 (ẩn hàng loạt) + BUG-QLTMBMHD_19 (Batch 1 — xóa hàng loạt). Đề nghị BA ra một quyết định chung cho cả 3 thao tác bulk.
