# Re-verify vòng 2 — QLDMTCTV_OOS_02 (dòng 328, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` — `CB_NV_TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`
**Verdict:** ✅ Pass

---

## Nhật ký đo

### 13:09 — Cuộn ngang tới cột "Công khai" và soi phần tử thật
Thẻ "Đang hoạt động" (8 dòng). Đọc phần tử ở cột "Công khai" bằng `evaluate_script`:
- Không còn là nhãn tĩnh: đó là `<button role="switch" class="ant-switch ant-switch-small">`.
- `cursor` = **`pointer`** (bug gốc: "con trỏ chuột không đổi thành hình bàn tay").
- `disabled` = `false`, `aria-checked` = `false`.
- Nhãn chữ trong ô: **"Chưa công khai"**; màu chữ `rgb(140,140,140)` (xám), nền công tắc `rgb(191,191,191)` (xám).
⇒ Nhãn đã đúng đặc tả, không còn "Công khai" / "Riêng tư".

### 13:12 — Cài bộ bắt thông báo dùng chung + tự kiểm
Dùng nguyên khối `output/UAT_doi-tac/tools/toast-capture.js` (KHÔNG lọc trùng · đọc `innerText` · đếm cả request).
Tự kiểm bằng cách chèn 1 node giả → **`soObserverDangSong = 1`** ⇒ số liệu hợp lệ.

### 13:13 — BẤM THẬT công tắc lần 1 (dòng TC-BTP-TW-0001 "Công ty Luật TNHH Alpha Hà Nội")
Đo được:
- **Số request = 0** · **Số khung thông báo nổi = 0** (không bắn thông báo thay cho hộp thoại).
- **Hộp thoại MỞ RA**, tiêu đề **"Công khai lên Cổng pháp luật quốc gia"**.
- Nội dung: "Mô tả công khai cho tổ chức **Công ty Luật TNHH Alpha Hà Nội** — bắt buộc." + ô nhập + bộ đếm `0 / 5000` + nút **Hủy** / **Công khai** (nút Công khai đang bị vô hiệu vì chưa nhập mô tả).
Ảnh: `image/QLDMTCTV_OOS_02-v2-01-bam-cong-tac-cong-khai-mo-hop-thoai.png` (đã mở đọc).

⇒ **Triệu chứng gốc "bấm vào không mở hộp thoại nào" KHÔNG còn tái hiện.**

### 13:15 — Chạy trọn luồng để đo được cả nhãn "Đã công khai"
Đầu phiên cả 8 dòng đều "Chưa công khai" nên không có sẵn dòng đã công khai để đối chiếu ⇒ tự dựng.
- Nhập mô tả `QA re-verify vong 2 04/08/2026 — kiem tra cong tac Cong khai tren dong danh sach (OOS_02)` rồi bấm **Công khai**.
- Đo: **1 request** `POST /api/v1/to-chuc-tu-vans/beb25e6f-8560-44ce-8235-0783ddb01dd1/cong-khai` · **1 thông báo** "Đã công khai tổ chức tư vấn" · hộp thoại đóng.
- Dòng đó đổi sang: `aria-checked = true`, nền công tắc `rgb(9, 88, 217)` (xanh), nhãn **"Đã công khai"**.
Ảnh: `image/QLDMTCTV_OOS_02-v2-02-sau-cong-khai-nhan-da-cong-khai-cong-tac-bat.png` (đã mở đọc: đúng 1 dòng có công tắc xanh + "Đã công khai", 7 dòng còn lại xám + "Chưa công khai").

### 13:17 — BẤM THẬT công tắc lần 2 (chiều ngược lại)
- **Hộp thoại MỞ RA**: **"Hủy công khai tổ chức tư vấn"** — "Tổ chức "Công ty Luật TNHH Alpha Hà Nội" sẽ được gỡ khỏi Cổng pháp luật quốc gia ở lần đồng bộ kế tiếp." + nút **Đóng** / **Hủy công khai** (đỏ).
- 0 request, 0 thông báo tại thời điểm mở hộp thoại.
Ảnh: `image/QLDMTCTV_OOS_02-v2-03-bam-lai-cong-tac-mo-hop-thoai-huy-cong-khai.png` (đã mở đọc).

### 13:18 — Trả dữ liệu về nguyên trạng
Bấm **Hủy công khai** → **1 request** `POST …/cong-khai` · **1 thông báo** "Đã hủy công khai" · `aria-checked` về `false`, nhãn về **"Chưa công khai"**.
⇒ Bản ghi TC-BTP-TW-0001 đã trở lại đúng trạng thái ban đầu, không để lại thay đổi.

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1645:
`| 23 | bảng | Công khai | toggle | "Đã công khai" (xanh) / "Chưa công khai" (xám) | Click → mở MD-CONG-KHAI hoặc MD-HUY-CONG-KHAI; chỉ bật được khi trạng thái = Đang hoạt động |`

### Kết luận
Cả 2 ý của phiếu đều hết: (a) cột "Công khai" bấm được và mở đúng hộp thoại công khai / hủy công khai; (b) nhãn chữ đã là "Đã công khai" / "Chưa công khai" đúng đặc tả ⇒ **Pass**.
