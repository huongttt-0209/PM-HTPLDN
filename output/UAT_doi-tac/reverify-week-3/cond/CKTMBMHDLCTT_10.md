# Bảng đối chiếu điều kiện — CKTMBMHDLCTT_10 (row 95)

Bug loại **Trạng thái UI sau thao tác bulk theo state** (selection sau ẩn hàng loạt) → bắt buộc bảng điều kiện.

| Điều kiện | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW) | cbnv_tw — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Thư mục chọn | 2 thư mục trạng thái Đã công khai (CONG_KHAI) | 2 thư mục Đã công khai: QA Hidden Folder 715 + Thư mục biểu mẫu seed | Không |
| Thao tác | Ẩn hàng loạt 2 thư mục | Ẩn hàng loạt 2 thư mục | Không |
| Kết quả thao tác | Ẩn thành công (toast "Đã ẩn 2 thư mục.") | Ẩn thành công (toast "Đã ẩn 2 thư mục.", 2 thư mục → AN) | Không |

**Kết luận GAP:** 0 GAP trên điều kiện cốt lõi — cùng vai trò, cùng 2 thư mục CONG_KHAI, cùng thao tác ẩn hàng loạt, cùng kết quả ẩn thành công.
**Khác biệt không ảnh hưởng kết quả:** đối tác đứng ở tab "Đã công khai" (2 thư mục vừa ẩn rời khỏi tab → selection thành "bóng ma"), mình đứng tab "Tất cả" (2 thư mục vẫn hiện + vẫn tích). Cả hai đều cho CÙNG lỗi cốt lõi: **thanh "Đã chọn 2 thư mục" + nút bulk KHÔNG được xóa sau khi ẩn hàng loạt hoàn tất.**

**Quan sát (mình test):**
- Toast (observer, 1 toast, không nhân đôi): *"Đã ẩn 2 thư mục."*
- Network: 1 request `POST /api/v1/thu-muc-bieu-maus/batch-an`.
- After-state: 715 + seed → "Đã ẩn" (AN). Thanh **"Đã chọn 2 thư mục"** vẫn hiển thị + [Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt] [Bỏ chọn] vẫn hiện + 2 checkbox vẫn tích (`cbChecked=true`), `anyRowChecked=true`.

**Đối chiếu SRS — vì sao BA confirm (KHÔNG Open):**
- `srs-fr-09-bieu-mau.md:616` (SCR-VII-01 #14): bar hành động hàng loạt hiển thị **"khi chọn nhiều"** — chỉ định nghĩa điều kiện HIỂN THỊ, không định nghĩa việc **xóa selection sau khi thao tác xong**. Sau ẩn, 2 thư mục vẫn "được chọn" nên bar hiển thị vẫn đúng điều kiện #14 → KHÔNG vi phạm clause này.
- `srs-fr-09-bieu-mau.md:261-262` (FR-VII-03 Postconditions UC94): chỉ nói về Cổng PLQG PULL + không cần phê duyệt. **KHÔNG có** postcondition nào về trạng thái selection/UI sau thao tác.
- FR-VII-03 đặc tả thao tác **đơn thư mục** (Inputs: `thu_muc_id` số ít); **KHÔNG có FR riêng cho bulk** → SRS **im lặng** về hành vi UI (deselect) sau bulk công khai/ẩn/xóa.

→ Không có clause SRS bị vi phạm (dẫn line rõ) và hệ thống KHÔNG chặn luồng hợp lệ (ẩn hàng loạt vẫn thành công). Kỳ vọng đối tác (selection tự xóa sau bulk — chuẩn UX phổ biến) là thứ **SRS không quy định** → theo Protocol §Verdict (dòng 75, 79): **BA confirm**, không Open.

**Ghi chú cụm:** cùng gốc với case 93 (công khai hàng loạt) + BUG-QLTMBMHD_19 (Batch 1 — xóa hàng loạt). Với **xóa** hàng loạt, selection tồn đọng trỏ vào bản ghi đã mất → mức nghiêm trọng cao hơn. Đề nghị BA ra **một quyết định chung** cho cả 3 thao tác bulk: có bắt buộc tự xóa selection sau khi thao tác hoàn tất không.
