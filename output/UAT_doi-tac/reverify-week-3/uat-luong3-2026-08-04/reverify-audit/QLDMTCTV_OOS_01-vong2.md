# Re-verify vòng 2 — QLDMTCTV_OOS_01 (dòng 327, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbpd_tw` / `Test@1234` — vai trò `CB_PD_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp` (đúng vai trò + cấp + đơn vị của phiếu gốc)
**Verdict:** ✅ Pass

---

## Nhật ký đo

### 13:20 — Dựng đủ tiền đề TRƯỚC khi đo
Phiếu yêu cầu **cả hai** thẻ "Chờ phê duyệt" và "Mới đăng ký" cùng đang có hồ sơ thì mới so sánh được màu huy hiệu.
- Đầu phiên (đo bằng `cbnv_tw`): `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200] → `HOAT_DONG: 8`, `CHO_PHE_DUYET: 2`, **`MOI_DANG_KY: 0`** ⇒ thiếu vế "Mới đăng ký".
- Đã **tự tạo** tổ chức mới qua luồng chuẩn (màn "+ Thêm mới") → **TC-BTP-TW-0010** ở `MOI_DANG_KY`; sau đó hồ sơ này được dùng để kiểm lệnh "Trình phê duyệt" (phiếu OOS_03) nên chuyển sang `CHO_PHE_DUYET`, và đã tạo tiếp **TC-BTP-TW-0011** để thẻ "Mới đăng ký" vẫn còn hồ sơ.
- Trạng thái lúc đo: `HOAT_DONG: 8` · `CHO_PHE_DUYET: 3` · `MOI_DANG_KY: 1`.

### 13:45 — Đăng nhập đúng vai trò Cán bộ Phê duyệt Trung ương
- Đăng xuất phiên `cbnv_tw` cho sạch: `POST /api/v1/auth/logout` → **200**, xóa localStorage + sessionStorage, mở lại `/login`.
- Đăng nhập `cbpd_tw` / `Test@1234` → vào thẳng `/dashboard`, **không hỏi OTP**.
- Xác nhận danh tính hiển thị: `Cán bộ PD Trung ương` · `CB_PD_TW` · `BTP · TW` · đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`.
- Xác nhận lại gói mã đang chạy: `assets/index-DpIXRGaI.js`, nhãn `HTPLDN · V1.0.5`.
- Bấm menu `Mạng lưới Tư vấn viên → Tổ chức tư vấn` (không gõ URL).

### 13:47 — Đo màu huy hiệu (phép đo quyết định)
Đọc **màu nền thật** bằng `getComputedStyle` trên từng huy hiệu, cùng một lần, thay vì đoán qua ảnh:

| Thẻ | Số đếm | Màu nền huy hiệu | Màu chữ |
|---|:-:|---|---|
| Đang hoạt động | 8 | `rgb(9, 88, 217)` — xanh | trắng |
| **Chờ phê duyệt** | **3** | **`rgb(245, 34, 45)` — ĐỎ** | trắng |
| Mới đăng ký | 1 | `rgb(245, 34, 45)` — ĐỎ | trắng |
| Đã từ chối | — | (không có huy hiệu) | — |
| Tạm dừng | — | (không có huy hiệu) | — |
| Vô hiệu hóa | — | (không có huy hiệu) | — |

Thuộc tính `style` gắn thẳng trên huy hiệu của thẻ "Chờ phê duyệt": `background: rgb(245, 34, 45); color: white; …` — **giống hệt** huy hiệu của thẻ "Mới đăng ký".

⇒ **Triệu chứng gốc không còn tái hiện**: thẻ "Chờ phê duyệt" đang có 3 hồ sơ thì huy hiệu là NỀN ĐỎ, không còn nền xanh; hai thẻ được đặc tả bằng cùng một mệnh đề nay hiển thị giống nhau.

Ảnh: `image/QLDMTCTV_OOS_01-v2-01-cbpd_tw-the-cho-phe-duyet-huy-hieu-do-giong-moi-dang-ky.png`
(đã mở đọc: góc phải trên hiện `Cán bộ PD Trung ương · CB_PD_TW`; thanh thẻ có 6 thẻ, "Đang hoạt động 8" huy hiệu XANH, "Chờ phê duyệt 3" và "Mới đăng ký 1" đều huy hiệu ĐỎ, 3 thẻ rỗng không có huy hiệu).

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`
- dòng 1627 — `| 5 | tab | Tab "Mới đăng ký" | tab + số đếm + chấm đỏ nếu >0 | …`
- dòng 1628 — `| 6 | tab | Tab "Chờ phê duyệt" | tab + số đếm + chấm đỏ nếu >0 | Hiển thị khi vai trò là Cán bộ Phê duyệt | …`

### Kết luận
Cán bộ Phê duyệt nay CÓ tín hiệu cảnh báo đỏ trên đúng thẻ chứa việc của mình ⇒ **Pass**.
