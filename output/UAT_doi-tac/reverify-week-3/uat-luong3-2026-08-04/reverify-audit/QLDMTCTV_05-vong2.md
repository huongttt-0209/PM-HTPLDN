# Re-verify vòng 2 — QLDMTCTV_05 (dòng 318, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (vai trò trùng ảnh đối tác) · `cbpd_tw` / `Test@1234` (đối chiếu phân quyền thẻ)
**Verdict:** ✅ Pass (cả 3 ý)

---

## Nhật ký đo

### 13:06 — Ảnh chụp ban đầu của thanh thẻ (vai trò Cán bộ Nghiệp vụ TW)
Đọc DOM `.ant-tabs-tab`: **5 thẻ** — Đang hoạt động · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa.
⇒ **Ý 3 ("Thẻ Chờ phê duyệt hiển thị đối với CBNV") không tái hiện**: vai trò Cán bộ Nghiệp vụ KHÔNG còn thấy thẻ "Chờ phê duyệt".

### 13:07 — Ý 1: số đếm trên thẻ
- Thẻ "Đang hoạt động" hiển thị số **8**; đọc `outerHTML` cho thấy số nằm trong `<span>` riêng có nền `rgb(9, 88, 217)` (xanh), chữ trắng.
- Bảng bên dưới đúng **8 dòng**, chân bảng "Hiển thị 1-8 / 8 kết quả" ⇒ số đếm là số thật, không phải số cứng.
- 4 thẻ còn lại đang 0 bản ghi nên không hiện số.
- Kiểm chéo bằng API trong phiên: `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200] → tổng 10, phân bố `HOAT_DONG: 8`, `CHO_PHE_DUYET: 2` ⇒ khớp.

### 13:20 — Dựng tiền đề cho Ý 2 (thẻ "Mới đăng ký" phải CÓ hồ sơ chưa trình duyệt)
Thẻ "Mới đăng ký" đang rỗng ⇒ **tự tạo tổ chức mới và cố ý KHÔNG trình phê duyệt**, đúng tình huống đối tác mô tả:
- Bấm "+ Thêm mới" → màn `Thêm mới Tổ chức tư vấn`, nhập: Tên `Cong ty Luat QA Reverify V2 04-08` · Loại hình `Công ty Luật` · Người đại diện `Nguyen Van Reverify V2` · Số Giấy ĐKHĐ `DKHD-QA-V2-0804` · Ngày cấp `01/01/2025` · Lĩnh vực `Doanh nghiệp` · Địa chỉ `So 1 Duong QA Reverify, Ba Dinh, Ha Noi` → **Lưu**.
- Sinh ra **TC-BTP-TW-0010**, trạng thái `MOI_DANG_KY`. (Sau này khi kiểm OOS_03 hồ sơ này được trình duyệt, nên đã tạo thêm **TC-BTP-TW-0011** giữ chỗ ở "Mới đăng ký".)

### 13:22 — Ý 2: màu huy hiệu thẻ "Mới đăng ký"
Đọc màu nền THẬT bằng `getComputedStyle` (không đoán qua ảnh), cùng một thời điểm:

| Thẻ | Số đếm | Màu nền huy hiệu |
|---|:-:|---|
| Đang hoạt động | 8 | `rgb(9, 88, 217)` — xanh |
| **Mới đăng ký** | **1** | **`rgb(245, 34, 45)` — ĐỎ** |
| Đã từ chối / Tạm dừng / Vô hiệu hóa | — | không có huy hiệu |

⇒ Khi có hồ sơ chưa trình phê duyệt, thẻ "Mới đăng ký" bật huy hiệu **nền đỏ**, trong khi thẻ "Đang hoạt động" cùng lúc vẫn xanh. **Ý 2 không tái hiện.**
Ảnh: `image/QLDMTCTV_05-v2-01-cbnv_tw-5-the-co-so-dem-moi-dang-ky-huy-hieu-do.png` (đã mở đọc: 5 thẻ, "Đang hoạt động 8" huy hiệu xanh, "Mới đăng ký 1" huy hiệu đỏ, không có thẻ "Chờ phê duyệt").

### 13:30 — Kiểm phần lọc của từng thẻ (yêu cầu "Hệ thống lọc danh sách theo trạng thái tương ứng")
Bấm lần lượt cả 5 thẻ, đọc cột "Trạng thái" của mọi dòng:

| Thẻ | Nhãn thẻ | Số dòng | Trạng thái các dòng |
|---|---|:-:|---|
| Đang hoạt động | `Đang hoạt động 8` | 8 | tất cả "Đang hoạt động" |
| Mới đăng ký | `Mới đăng ký 1` | 1 | "Mới đăng ký" |
| Đã từ chối | `Đã từ chối` | 0 | — |
| Tạm dừng | `Tạm dừng` | 0 | — |
| Vô hiệu hóa | `Vô hiệu hóa` | 0 | — |

Không có dòng nào lọt sai thẻ.

### 13:45 — Đối chứng phân quyền bằng vai trò Cán bộ Phê duyệt
Đăng xuất sạch (`POST /api/v1/auth/logout` → 200, xóa localStorage/sessionStorage), đăng nhập `cbpd_tw` (`CB_PD_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`), bấm menu vào lại màn Tổ chức tư vấn.
- Thanh thẻ nay có **6 thẻ**: Đang hoạt động 8 · **Chờ phê duyệt 3** · Mới đăng ký 1 · Đã từ chối · Tạm dừng · Vô hiệu hóa.
⇒ Thẻ "Chờ phê duyệt" **chỉ** hiện với vai trò Cán bộ Phê duyệt — đúng như đặc tả.
Ảnh: `image/QLDMTCTV_05-v2-02-cbpd_tw-thay-du-6-the-co-cho-phe-duyet.png` (đã mở đọc).

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`
- dòng 1627 — Tab "Mới đăng ký": `tab + số đếm + chấm đỏ nếu >0`
- dòng 1628 — Tab "Chờ phê duyệt": `tab + số đếm + chấm đỏ nếu >0` · `Hiển thị khi vai trò là Cán bộ Phê duyệt`

### Ghi chú (không phải triệu chứng đối tác nêu)
Thẻ đang có 0 bản ghi thì không hiện số `0`. Đặc tả chỉ ghi "tab + số đếm", không quy định cách hiển thị khi bằng 0. Triệu chứng gốc là "MỌI thẻ đều không có số đếm" — nay mọi thẻ có dữ liệu đều hiện số đúng.

### Kết luận
Cả 3 ý của phiếu đều không còn tái hiện ⇒ **Pass**.
