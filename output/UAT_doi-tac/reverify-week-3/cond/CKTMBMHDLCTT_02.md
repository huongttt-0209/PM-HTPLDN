# Bảng đối chiếu điều kiện — CKTMBMHDLCTT_02 (row 92)

Bug loại **Hiển thị nút theo state/data** (phụ thuộc soBieuMau + trạng thái + role/đơn vị) → bắt buộc bảng điều kiện.

| Điều kiện | Đối tác (evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | cbnv_tw — CB Nghiệp vụ Trung ương (CB_NV_TW) | Không |
| Trạng thái thư mục | Nháp (NHAP) — vd thư mục "TKM test" | Nháp (NHAP) — thư mục BM-B3-0720-Rong-1 | Không |
| Số biểu mẫu trong thư mục | Rỗng (Số biểu mẫu = 0) | Rỗng (Số biểu mẫu = 0) | Không |
| Đơn vị sở hữu thư mục | Cùng đơn vị người đăng nhập (TW) | Cùng đơn vị (BTP·TW), thư mục do chính cbnv_tw seed | Không |

**Kết luận GAP:** 0 GAP — tái hiện đúng vai trò + đúng state (NHAP, 0 biểu mẫu) + cùng đơn vị như đối tác.

**Quan sát:** Thư mục BM-B3-0720-Rong-1 (Nháp, 0 biểu mẫu) hiển thị nút **"Công khai"** ở cột Hành động (DOM: actionButtons = ["Công khai","Sửa","Xóa"]). Thư mục QA Hidden Folder 715 (Nháp, 1 biểu mẫu) cũng có "Công khai" (đúng). Thư mục "Thư mục biểu mẫu seed" (Đã công khai) có "Ẩn" (đúng).

**Đối chiếu SRS:** `srs-fr-09-bieu-mau.md:615` (SCR-VII-01, row 13 Cột Hành động): *"Công khai (khi NHAP/AN, **có BM**) / Ẩn (khi CONG_KHAI) / Sửa / Xóa (khi NHAP/AN, rỗng)"* → nút "Công khai" chỉ được hiện khi thư mục **có biểu mẫu**. Thư mục rỗng (0 BM) hiện nút → sai điều kiện "có BM".
