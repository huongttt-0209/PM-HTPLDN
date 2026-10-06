# Re-verify vòng 2 — QLDMTCTV_OOS_07 (dòng 333, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` — `CB_NV_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`
**Verdict:** ✅ Pass

---

## Nhật ký đo

### 13:23 — Dựng trạng thái rỗng: KHÔNG phải bịa, thẻ rỗng có sẵn
Đo bằng API trong phiên `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200]: toàn bộ bản ghi chỉ nằm ở `HOAT_DONG` / `CHO_PHE_DUYET` / `MOI_DANG_KY`.
⇒ 3 thẻ **Đã từ chối · Tạm dừng · Vô hiệu hóa** đang có **0 bản ghi thật**, không cần lọc/tìm kiếm giả để ép rỗng.
Ngoài ra, tại thời điểm đo thẻ **"Mới đăng ký"** cũng đang rỗng ⇒ tranh thủ đo luôn nút "+ Thêm tổ chức tư vấn" — đúng thứ vòng 1 chưa kiểm được. (Việc tạo tổ chức mới cho các phiếu khác được làm SAU phép đo này.)

### 13:24 — Thẻ "Mới đăng ký" rỗng
Bấm thẻ → `?trangThai=MOI_DANG_KY`. Đọc vùng `.ant-table-placeholder`:
- **Có** phần tử hình minh họa: `.ant-empty-image > svg` (hình hộp tài liệu màu xám).
- Chữ hiển thị (`innerText`): **"Chưa có tổ chức tư vấn nào trong mục này"**.
- Trong vùng rỗng có **nút "+ Thêm tổ chức tư vấn"**.
- **Không còn chữ "Trống"** trên màn hình.
Ảnh: `image/QLDMTCTV_OOS_07-v2-01-the-moi-dang-ky-rong-co-hinh-cau-huong-dan-va-nut-them.png` (đã mở đọc: hình minh họa xám ở giữa, bên dưới là câu tiếng Việt, bên dưới nữa là nút xanh "+ Thêm tổ chức tư vấn").

*Kiểm chéo chuỗi "Trống":* chuỗi này chỉ còn nằm trong thẻ `<title>Trống</title>` BÊN TRONG hình minh họa (phần dành cho trình đọc màn hình) — `innerText` không lấy nó và ảnh chụp cũng không thấy nó. Người dùng không đọc được chữ "Trống" nữa.

### 13:26 — 3 thẻ rỗng còn lại
Bấm lần lượt "Đã từ chối" → "Tạm dừng" → "Vô hiệu hóa", đọc vùng rỗng từng thẻ:

| Thẻ | Số dòng | Có hình minh họa | Chữ hiển thị | Nút trong vùng rỗng |
|---|:-:|:-:|---|---|
| Đã từ chối | 0 | Có | "Chưa có tổ chức tư vấn nào trong mục này" | (không có) |
| Tạm dừng | 0 | Có | "Chưa có tổ chức tư vấn nào trong mục này" | (không có) |
| Vô hiệu hóa | 0 | Có | "Chưa có tổ chức tư vấn nào trong mục này" | (không có) |

Ảnh: `image/QLDMTCTV_OOS_07-v2-02-the-vo-hieu-hoa-rong-co-hinh-va-cau-huong-dan.png` (đã mở đọc: thẻ "Vô hiệu hóa" đang chọn, vùng bảng có hình minh họa + câu hướng dẫn, không có nút thêm).

⇒ Việc **không** có nút "+ Thêm tổ chức tư vấn" ở 3 thẻ này là ĐÚNG đặc tả (nút chỉ ở thẻ "Mới đăng ký").

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1649:
`| 27 | trạng thái rỗng | Empty state | minh họa + label | Khi tab không có bản ghi: hình ảnh + "Chưa có tổ chức tư vấn nào trong mục này" + nút "+ Thêm tổ chức tư vấn" (chỉ ở tab Mới đăng ký) |`

### Kết luận
Vùng rỗng nay có **đủ cả hình minh họa lẫn câu hướng dẫn tiếng Việt**, và nút "+ Thêm tổ chức tư vấn" xuất hiện đúng ở thẻ "Mới đăng ký" ⇒ **Pass**. (Điểm vòng 1 nêu là "mất hình minh họa" cũng không còn: hình đã hiện lại.)
