# Re-verify vòng 2 — QLDMTCTV_OOS_12 (dòng 338, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` — `CB_NV_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`
**Verdict:** ✅ Pass

> Ghi chú số dòng: phiếu này nằm ở **dòng 338** của tab tuần 3 (đọc trực tiếp từ Google Sheet), không phải 336.

---

## Nhật ký đo

### 13:28 — Nội dung gợi ý trong ô tìm kiếm
Đọc thuộc tính `placeholder` của ô tìm kiếm:
**"Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện"** — khớp nguyên văn đặc tả (bug gốc: web chỉ ghi "Tìm theo tên hoặc mã tổ chức").

### 13:29 — Chọn từ khóa: lấy người đại diện CÓ THẬT trên bảng
Tổ chức mà phiếu gốc dùng (TC-STP-AG-0001 / "Nguyen Van QA") không nằm trong thẻ "Đang hoạt động" trên môi trường mới — bản ghi TC-STP-AG-0001 hiện ở trạng thái "Chờ phê duyệt" và người đại diện là "Nguyen Van AG".
⇒ Lấy tên người đại diện đang hiển thị ngay ở cột "Người đại diện" của bảng làm từ khóa, KHÔNG bịa tên:
`Nguyễn Văn A` (TC-BTP-TW-0001) · `Le Van Kappa` (TC-BTP-TW-0008) · `Phạm Thị D` (TC-BTP-TW-0004) · `Tran Thi Iota` (TC-BTP-TW-0007).
Cả 4 tên này **không** nằm trong tên tổ chức tương ứng ⇒ nếu ra kết quả thì chỉ có thể do khớp tiêu chí người đại diện.

### 13:30 — Phép 1 (đối chứng theo TÊN)
Gõ `Trung tâm TVPL` → bấm **Tìm kiếm** → `?tuKhoa=Trung+tâm+TVPL` → **2 kết quả**: TC-BTP-TW-0008 ("Trung tam TVPL Kappa Da Nang R8") và TC-BTP-TW-0003 ("Trung tâm TVPL Gamma Đà Nẵng"). Chân bảng "Hiển thị 1-2 / 2 kết quả".

### 13:31 — Phép 2 (đối chứng theo MÃ)
Xóa sạch ô (đặt lại `value=''` + bắn sự kiện `input`, vì gõ đè sẽ nối thêm vào từ khóa cũ), gõ `TC-BTP-TW-0001` → **1 kết quả**: TC-BTP-TW-0001 "Công ty Luật TNHH Alpha Hà Nội".

### 13:32 — Phép 3 (phép đo chính — theo NGƯỜI ĐẠI DIỆN)
Xóa ô, gõ `Nguyễn Văn A` → bấm Tìm kiếm → `?tuKhoa=Nguyễn+Văn+A` → **1 kết quả**: **TC-BTP-TW-0001**, cột "Người đại diện" = `Nguyễn Văn A`. Chân bảng "Hiển thị 1-1 / 1 kết quả". Bảng KHÔNG rơi vào trạng thái rỗng.
Ảnh: `image/QLDMTCTV_OOS_12-v2-01-tim-theo-nguoi-dai-dien-Nguyen-Van-A-ra-1-ket-qua.png` (đã mở đọc: ô tìm kiếm chứa "Nguyễn Văn A", 1 dòng TC-BTP-TW-0001, thẻ "Đang hoạt động" hiện số đếm 1 theo kết quả lọc).

⇒ **Triệu chứng gốc "tìm theo người đại diện trả 0 kết quả" KHÔNG còn tái hiện.**

### 13:33 — Lặp lại với 3 người đại diện khác cho chắc

| Từ khóa | Số kết quả | Bản ghi trả về | Người đại diện của bản ghi |
|---|:-:|---|---|
| `Le Van Kappa` | 1 | TC-BTP-TW-0008 | Le Van Kappa |
| `Phạm Thị D` | 1 | TC-BTP-TW-0004 | Phạm Thị D |
| `Tran Thi Iota` | 1 | TC-BTP-TW-0007 | Tran Thi Iota |

4/4 phép tìm theo người đại diện đều ra đúng một tổ chức tương ứng.

### 13:34 — Trả màn về nguyên trạng
Bấm "Xóa bộ lọc" → về đủ 8 dòng thẻ "Đang hoạt động".

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1631:
`| 9 | bộ lọc | Ô tìm kiếm | ô tìm kiếm | Placeholder: "Tìm theo mã tổ chức, tên tổ chức hoặc người đại diện" | Tìm theo mã / tên / người đại diện |`

### Kết luận
Cả 2 ý của phiếu đều hết: tìm được theo người đại diện, và nội dung gợi ý đã ghi đủ 3 tiêu chí ⇒ **Pass**.
