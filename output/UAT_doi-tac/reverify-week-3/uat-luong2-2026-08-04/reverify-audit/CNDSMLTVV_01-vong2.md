# Re-verify vòng 2 — CNDSMLTVV_01 (dòng 124, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng hiển thị trên giao diện:** `HTPLDN · V1.0.5` (góc trái sidebar)
**Verdict:** (đang đo)

---

## Nhật ký đo (ghi ngay sau mỗi phép đo)

### 12:36 — Đăng nhập lại từ đầu
- Đã đăng xuất phiên cũ (`POST /api/v1/auth/logout` → 200) + xoá localStorage/sessionStorage, rồi vào lại `/login`.
- Đăng nhập `cbnv_bn` / `Test@1234` → **vào thẳng `/dashboard`, KHÔNG qua bước nhập OTP**. (Môi trường mới bỏ bước OTP ở luồng này — không log thành lỗi.)
- Sidebar hiển thị: `HTPLDN · V1.0.5`; đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp`; nhãn tài khoản `Cán bộ NV Bộ ngành / CB_NV_BN`; phạm vi `Bộ ngành`.
- Ô KPI Tổng quan: **Chuyên gia / Tư vấn viên: 0 người**.

### 12:38 — `cbnv_bn` KHÔNG dựng được tiền đề → phải đổi tài khoản
Đo 2 cách độc lập, cùng kết luận:
1. **Giao diện:** Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia, tab "Đang hoạt động" → "Chưa có tư vấn viên nào trong mục này".
   Ảnh: `image/CNDSMLTVV_01-v2-01-cbnv_bn-danhsach-trong-0-tvv.png` (đã mở đọc: bảng rỗng, nhãn tài khoản `Cán bộ NV Bộ ngành / CB_NV_BN`, bản dựng `V1.0.5`).
2. **Gọi thẳng API trong phiên:** `GET /api/v1/tu-van-viens?page=1&limit=200` → 200, `meta.total = 0` (KHÔNG lọc trạng thái ⇒ phạm vi Bộ ngành **không có bất kỳ tư vấn viên nào**, không riêng tab Đang hoạt động).
   Ô KPI Tổng quan cũng hiện "Chuyên gia / Tư vấn viên: 0 người".

**Không phải vấn đề quyền:** `GET /api/v1/auth/me` cho thấy `cbnv_bn` **CÓ** quyền `publish_tu_van_vien` (và `manage_tu_van_vien`, `read_tu_van_vien`).
`donViId = 00000000-0000-4000-8001-000000000001`, `capDonVi = BN`.

**⇒ Lý do đổi sang `cbnv_tw`:** phạm vi dữ liệu của Bộ ngành trống hoàn toàn (0 bản ghi), không thể tích chọn ≥2 tư vấn viên "Đang hoạt động" chưa công khai.
Vòng 1 cũng đo bằng vai trò **Cán bộ Nghiệp vụ Trung ương** ⇒ đo lại trên TW mới là so sánh cùng điều kiện với kết luận Pass cần kiểm chứng.

### 12:42 — KIỂM TRA LẦN CHẠY TRƯỚC CÓ LỠ CÔNG KHAI AI KHÔNG → **KHÔNG**
Hai lớp bằng chứng:
1. **Phạm vi `cbnv_bn`** (tài khoản duy nhất mà lần chạy trước dùng — ảnh cũ để lại tên `...cbnv_bn...`): tổng số tư vấn viên trong phạm vi = **0**. Không có bản ghi nào để công khai.
2. **Phạm vi `cbnv_tw`** (68 tư vấn viên): có **8** bản ghi đang ở cờ công khai. Mở chi tiết từng bản ghi đọc `thoiGianDangTai`:
   | Mã TVV | thoiGianDangTai | Ghi chú |
   |---|---|---|
   | TVV-BTP-TW-0047 | (trống) | dữ liệu seed cũ, `ngayCapNhat` 10/05/2026 |
   | TVV-BTP-TW-0041 | (trống) | seed cũ 09/05/2026 |
   | TVV-BTP-TW-0040 | (trống) | seed cũ 09/05/2026 |
   | TVV-BTP-TW-0038 | (trống) | seed cũ 10/05/2026 |
   | TVV-BTP-TW-0035 | 2026-05-25T16:25:38Z | mô tả "12" |
   | TVV-BTP-TW-0030 | (trống) | seed cũ 10/05/2026 |
   | TVV-BTP-TW-0029 | 2026-07-25T10:35:49Z | mô tả "TKM kiểm thử công khai TVV" |
   | TVV-BTP-TW-0019 | 2026-05-09T18:58:35Z | mô tả "CHO_KICH_HOAT công khai test" |
   ⇒ Mốc công khai gần nhất là **25/07/2026**. **Không có bản ghi nào được công khai ngày 03 hoặc 04/08/2026.**

**Kết luận audit:** lần chạy bị chết giữa chừng **không công khai bất kỳ tư vấn viên nào**.

### 12:45 — Đăng nhập `cbnv_tw`, tiền đề ĐỦ, không cần seed
`GET /api/v1/auth/profile` → `cbnv_tw`, vai trò `CB_NV_TW`, `donViId = 00000000-0000-4000-8000-000000000001`, `capDonVi = TW`.
Phân bố trạng thái 68 bản ghi: MOI_DANG_KY 26 · HOAT_DONG 11 · CHO_KICH_HOAT 10 · TU_CHOI 10 · YEU_CAU_BO_SUNG 6 · CHO_PHE_DUYET 3 · DANG_THAM_DINH 1 · VO_HIEU_HOA 1.
**"Đang hoạt động" + CHƯA công khai = 8 bản ghi** ⇒ thoả tiền đề "≥2 tư vấn viên Đang hoạt động chưa công khai", **không phải seed thêm**.

### 12:52 — Cài bộ bắt thông báo dùng chung + tự kiểm
Dùng nguyên khối `tools/toast-capture.js` (không lọc trùng · đọc `innerText` · đếm request). Tự kiểm chèn node giả → `soObserverDangSong = 1` ⇒ số liệu hợp lệ.

### 12:55 — (a)(b) Mở cửa sổ nhập mô tả
Tích chọn 2 dòng **TVV-BTP-TW-0034** (TVV R12 A18 UI Walk) + **TVV-BTP-TW-0032** (TVV R11 Verify Mail Fix), cả 2 đang "Đang hoạt động" + cột Công khai = "Chưa công khai".
Thanh thao tác hàng loạt hiện: `Đã chọn 2 mục` + 3 nút **"Công khai lên Cổng PLQG"** · "Hủy công khai" · "Bỏ chọn tất cả".
> **Nhãn nút thật trên bản dựng này là "Công khai lên Cổng PLQG"** (phiếu ghi "Công khai hàng loạt" — chỉ khác cách gọi, cùng một nút).
Ảnh: `image/CNDSMLTVV_01-v2-02-chon-2-tvv-hien-nut-cong-khai-len-cong-plqg.png` (đã mở đọc).

Bấm nút → **cửa sổ MỞ RA**. Đo được:
- Số request khi mở cửa sổ = **0**; số khung thông báo nổi = **0** (không bắn thông báo thay cho cửa sổ).
- Tiêu đề: **"Công khai hàng loạt lên Cổng PLQG"**.
- Câu xác nhận: **"Công khai 2 tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"** ⇒ **N = 2 khớp đúng số đã chọn**.
- Ô **"Mô tả công khai"** có **dấu * bắt buộc**: nhãn mang lớp `ant-form-item-required`, đọc pseudo-element `::before` cho `content = "*"`, màu `rgb(245,34,45)` (đỏ) — tức dấu sao **thật sự hiển thị**, không phải chỉ có tên lớp. Ô nhập `aria-required = "true"`, `maxLength = 5000`, bộ đếm "0 / 5000".
- Ô "Tệp đính kèm (tùy chọn)" — không bắt buộc, đúng như đặc tả (tối đa 10 tệp, ≤20MB/tệp).
Ảnh: `image/CNDSMLTVV_01-v2-03-cuaso-mo-tieude-cong-khai-hang-loat-N2-o-mota-dau-sao.png` (đã mở đọc: thấy rõ tiêu đề, câu xác nhận có số 2, dấu `*` đỏ trước "Mô tả công khai", bộ đếm 0/5000).

### 12:58 — (c) Để TRỐNG mô tả rồi bấm "Công khai"
Hẹn giờ bấm nút sau 2500ms rồi mới gọi chụp màn hình (để bắt kịp thông báo tự tắt nếu có).
Kết quả đo:
- **SỐ REQUEST = 0** — không có yêu cầu nào gửi đi.
- **SỐ KHUNG THÔNG BÁO NỔI = 0** — không bắn thông báo ra ngoài màn danh sách.
- **Cửa sổ VẪN MỞ** (`ant-modal-wrap` còn trên trang).
- Lỗi hiện **ngay tại ô nhập**: `.ant-form-item-explain-error` = **"Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia"**; ô nhập viền đỏ, form item mang lớp `ant-form-item-has-error`.
Ảnh: `image/CNDSMLTVV_01-v2-04-bo-trong-mota-loi-do-tai-o-nhap-cuaso-van-mo.png` (đã mở đọc: cửa sổ còn nguyên, ô nhập viền đỏ, dòng chữ đỏ nằm ngay dưới ô).
⇒ **KHÔNG tái hiện triệu chứng đối tác phản ánh** (bắn thông báo nổi + không mở cửa sổ).
