# Re-verify vòng 2 — QLDMTCTV_02 (dòng 317, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** gói mã `assets/index-DpIXRGaI.js` · nhãn trên sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (chính) · `cbpd_tw` / `Test@1234` (đối chiếu)
**Verdict:** ✅ Pass

---

## Nhật ký đo

### 13:04 — Đăng nhập `cbnv_tw`
- Vào thẳng `/login`, nhập `cbnv_tw` / `Test@1234` → **vào thẳng `/dashboard`, KHÔNG hỏi mã OTP**. (Môi trường mới bỏ bước OTP ở luồng này — không log thành lỗi.)
- `evaluate_script` liệt kê `script[src]` → **chỉ 1 gói: `https://htpldn-uat.ospgroup.vn/assets/index-DpIXRGaI.js`** ⇒ đúng bản dựng cần đo.
- Sidebar: `HTPLDN · V1.0.5`; đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`; nhãn tài khoản `Cán bộ NV Trung ương / CB_NV_TW`; phạm vi `BTP · TW`.

### 13:06 — Mở màn cần đo (bấm menu bên trái, KHÔNG gõ URL)
- Bấm `Mạng lưới Tư vấn viên → Tổ chức tư vấn` → `/chuyen-gia-tvv/to-chuc`, tiêu đề "Quản lý Tổ chức tư vấn".
- Thanh thẻ: 5 thẻ (Đang hoạt động 8 · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa).

### 13:07 — Đọc cấu trúc bảng (đây là phép đo chính của phiếu)
Đọc trực tiếp `.ant-table-thead th` bằng `evaluate_script`, được **11 cột theo đúng thứ tự**:

`(ô tích chọn)` · **STT** · Mã tổ chức · Tên tổ chức · Loại hình · Lĩnh vực · Đơn vị quản lý · Người đại diện · Trạng thái · Công khai · Hành động

- Ô tích chọn ở hàng tiêu đề có nhãn trợ năng `Select all`; mỗi dòng dữ liệu đều có 1 ô tích chọn riêng.
- Cột STT đánh số **1 → 8** theo đúng số dòng của trang.
⇒ **Hai thứ đối tác báo thiếu (ô tích chọn + STT) nay đều có.**
Ảnh: `image/QLDMTCTV_02-v2-01-bang-co-o-tich-chon-va-cot-STT.png` (đã mở đọc: thấy ô tích chọn ngoài cùng trái ở cả hàng tiêu đề lẫn 8 dòng, cột STT 1–8, cột Hành động ghim bên phải với 3 biểu tượng mắt / bút chì / ba chấm).

### 13:09 — Kiểm phần cột bị che sau thanh cuộn ngang
Đẩy `scrollLeft` của `.ant-table-body` về hết bên phải (vùng cuộn rộng 1686px / khung 1136px) rồi chụp.
- Thấy rõ: **Người đại diện** (TKM · Le Van Kappa · Tran Thi Iota · Vũ Thị F · Phạm Thị D …), **Trạng thái** (nhãn nền xanh nhạt "Đang hoạt động"), **Công khai** (công tắc + chữ "Chưa công khai"), **Hành động**.
- Chữ tiếng Việt thống nhất, không thấy chữ tràn ra ngoài ô hay đè lên nhau; các thẻ lĩnh vực tự xuống dòng trong ô.
Ảnh: `image/QLDMTCTV_02-v2-02-cuon-ngang-cot-nguoi-dai-dien-trang-thai-cong-khai-hanh-dong.png` (đã mở đọc).

### 13:11 — Ô tích chọn có DÙNG ĐƯỢC không (không chỉ hiển thị)
Bấm thật ô tích chọn của dòng 1:
- Ô chuyển sang tích xanh, ô ở hàng tiêu đề chuyển sang trạng thái "chọn một phần".
- Hiện thanh thao tác hàng loạt: **"Đã chọn 1 tổ chức tư vấn"** + 3 nút **Công khai · Hủy công khai · Bỏ chọn**.
Ảnh: `image/QLDMTCTV_02-v2-03-tich-chon-dong-hien-thanh-thao-tac-hang-loat.png` (đã mở đọc).
Bấm "Bỏ chọn" để trả lại nguyên trạng.

### 13:40 — Đối chiếu bằng vai trò Cán bộ Phê duyệt (thẻ "Chờ phê duyệt")
Đăng xuất sạch (`POST /api/v1/auth/logout` → 200 + xóa localStorage/sessionStorage), đăng nhập `cbpd_tw`.
- Thẻ "Chờ phê duyệt" (3 dòng): bảng vẫn có **ô tích chọn** + **cột STT** (1–3).
- Chọn cả 3 dòng → thanh thao tác **"Đã chọn 3 tổ chức tư vấn"** + nút **"Phê duyệt hàng loạt"** + "Bỏ chọn".
Ảnh: `image/QLDMTCTV_02-v2-04-cbpd_tw-tich-chon-hien-nut-phe-duyet-hang-loat.png` (đã mở đọc).

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`
- dòng 1637 — `| 15 | bảng | Ô chọn | checkbox | Chọn nhiều dòng cho thao tác hàng loạt |`
- dòng 1638 — `| 16 | bảng | Số thứ tự | cột | Tự động đánh số theo trang |`

### Kết luận
Triệu chứng gốc "Thiếu ô chọn và trường STT" **không còn tái hiện** trên bản dựng mới, ở cả 2 vai trò và mọi thẻ có dữ liệu. Các cột còn lại hiển thị đủ, đúng định dạng, không tràn/đè. ⇒ **Pass**.
