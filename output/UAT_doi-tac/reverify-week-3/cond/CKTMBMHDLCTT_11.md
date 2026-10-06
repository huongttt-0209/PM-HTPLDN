# Bảng đối chiếu điều kiện — CKTMBMHDLCTT_11 (row 96)

Bug loại **Nội dung thông báo phụ thuộc kết quả bulk theo state** (message "Ẩn X/Y, Z thất bại") → bắt buộc bảng điều kiện.

| Điều kiện | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ NV Trung ương (CB_NV_TW) | cbnv_tw — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Thư mục chọn (hỗn hợp đủ/không đủ đk ẩn) | 3 thư mục: 1 đủ đk ẩn (CONG_KHAI) + 2 không đủ đk (đã ẩn / Nháp) | 2 thư mục: 1 đủ đk ẩn (QA Hidden Folder 715 = CONG_KHAI) + 1 không đủ đk (BM-B3-0720-Rong-1 = Nháp) | Không |
| Thao tác | Ẩn hàng loạt | Ẩn hàng loạt | Không |
| Kết quả (một phần) | Ẩn được 1, còn lại thất bại → toast dạng "Ẩn X/Y thư mục, Z thất bại" | Ẩn được 715, Rong-1 thất bại → toast "Ẩn 1/2 thư mục, 1 thất bại." | Không |

**Kết luận GAP:** 0 GAP trên điều kiện cốt lõi — cùng vai trò, cùng kịch bản ẩn hàng loạt hỗn hợp đủ/không đủ điều kiện, cùng cho ra **đúng một dạng message "Ẩn {X}/{Y} thư mục, {Z} thất bại"**. Số lượng thư mục chọn khác nhau (đối tác 3, mình 2) chỉ đổi con số X/Y/Z, KHÔNG đổi dạng wording — mà case này xét chính là dạng wording.

**Quan sát (mình test):**
- Toast (observer, 1 toast, không nhân đôi): **"Ẩn 1/2 thư mục, 1 thất bại."**
- Network: 1 request `POST /api/v1/thu-muc-bieu-maus/batch-an`.
- After-state: 715 (CONG_KHAI) → "Đã ẩn" (thành công); Rong-1 (Nháp, không công khai) → vẫn "Nháp" (thất bại — đúng, không thể ẩn thư mục chưa công khai).
- (Ghi chú phụ: thanh "Đã chọn 2 thư mục" vẫn tồn tại sau thao tác — cùng lỗi selection cụm case 93/95.)

**Đối chiếu SRS — vì sao BA confirm:**
- `srs-fr-09-bieu-mau.md:250-251` (FR-VII-03 Error Handling): chỉ định nghĩa ERR-CK-01 (thư mục rỗng không công khai được) + WRN-CK-01 (thư mục đã công khai) — đều cho hướng **công khai đơn lẻ**. KHÔNG có message chuẩn cho **ẩn hàng loạt một phần**, cũng không có message cho hướng ẩn.
- Expected của đối tác (message kiểu "Đã ẩn {X}. {Y} không đủ điều kiện...") KHÔNG có nguồn SRS. SRS **im lặng** về nội dung message bulk một phần.

→ Không clause SRS quy định message này → không đủ căn cứ Open/Reject. Bất đồng về ĐẶC TẢ (wording) → **BA confirm**. Cùng bản chất sub-issue wording của case 94 (công khai hàng loạt một phần).
