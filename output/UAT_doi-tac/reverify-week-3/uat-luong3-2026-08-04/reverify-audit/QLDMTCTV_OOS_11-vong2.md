# Re-verify vòng 2 — QLDMTCTV_OOS_11 (dòng 337, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, Cục Bổ trợ tư pháp – Bộ Tư pháp)
**Verdict:** ✅ Pass

---

## Triệu chứng gốc cần kiểm (4 ý — phải hết cả bốn)

1. Màn Chi tiết **không có tab nào** (0 tab); thiếu cả "Thông tin", "Tư vấn viên liên kết", "Lịch sử".
2. **Không có mục tệp đính kèm**, không có nút "Xem" / "Tải xuống", dù tổ chức đang có tệp.
3. Bảng thông tin **thiếu mục "Lĩnh vực"** dù tổ chức có lĩnh vực.
4. Đường dẫn điều hướng **không kèm tên tổ chức**.

## Dựng tiền đề (không bỏ qua vì thiếu dữ liệu)

Đo bằng API trong phiên: **cả 12 tổ chức trên môi trường đều `fileDinhKem = []`** — không hồ sơ nào sẵn có tệp. Thiếu dữ liệu kiểu này tự tạo được nên đã tự dựng:
- Chọn **TC-BTP-TW-0001 "Công ty Luật TNHH Alpha Hà Nội"** vì đây là hồ sơ có sẵn từ trước, đủ dữ liệu, và **có 2 tư vấn viên liên kết** (`soTvvLienKet = 2`) — cần cho tab thứ 2.
- Mở chế độ Sửa, đính kèm `qd-cong-bo-alpha-reverify-v2.pdf` (237 B) rồi bấm Lưu: 1 request `PATCH /api/v1/to-chuc-tu-vans/beb25e6f-…`, 1 thông báo "Cập nhật thành công".
⇒ Có đúng 1 hồ sơ vừa có tệp, vừa có tư vấn viên liên kết, vừa có lĩnh vực — đủ để kiểm cả 4 ý trên cùng một màn.

## Nhật ký đo

### 13:52 — Vào màn Chi tiết
Sau khi lưu, hệ thống đưa thẳng sang `/chuyen-gia-tvv/to-chuc/beb25e6f-…`.

**Ý 4 — đường dẫn điều hướng:**
> **Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Công ty Luật TNHH Alpha Hà Nội**

Có tên tổ chức, không còn cấp "Chi tiết" ⇒ **ý 4 hết**. (Đặc tả dòng 1715.)

**Ý 1 — đếm tab:** đếm `.ant-tabs-tab` được **3 tab**, đúng tên đặc tả:
| Tab | Trạng thái |
|---|---|
| Thông tin | đang mở |
| Tư vấn viên liên kết | có |
| Lịch sử | có |

**Ý 3 — mục Lĩnh vực:** bảng thông tin có dòng **"Lĩnh vực pháp luật"** với 3 thẻ *Doanh nghiệp · Lao động · Thương mại* ⇒ **ý 3 hết**.

**Ý 2 — vùng tệp đính kèm:** dưới bảng thông tin có khối **"Tệp đính kèm"**, liệt kê `qd-cong-bo-alpha-reverify-v2.pdf (0.00 MB)` kèm **nút "Xem"** và **nút "Tải xuống"** ⇒ **ý 2 hết**.

Ảnh: `image/QLDMTCTV_OOS_11-v2-01-chi-tiet-3-tab-va-vung-tep-dinh-kem.png` (đã mở đọc: 3 tab trên đầu; bảng Mã/Loại hình/Người đại diện/Chức vụ/Số Giấy ĐKHĐ/Ngày cấp/Lĩnh vực pháp luật/Số lao động/Số TVV liên kết/Địa chỉ/Điện thoại/Email/Website/Số QĐ công bố/Ngày QĐ công bố/Ghi chú; khối "Tệp đính kèm" với nút Xem + Tải xuống; cột phải là nhóm nút Thao tác).

### 13:53 — Bấm nút "Xem" (kiểm hành vi, không chỉ nhìn thấy nút)
Bấm **Xem** → mở tab mới tới tệp trên kho lưu trữ (đường dẫn có chữ ký tạm thời), trình xem PDF hiện đúng tệp `qd-cong-bo-alpha-reverify-v2.pdf`, 1/1 trang.
Ảnh: `image/QLDMTCTV_OOS_11-v2-04-bam-Xem-mo-tep-PDF.png` (đã mở đọc: thanh tiêu đề trình xem ghi đúng tên tệp, trang 1/1). Đã đóng tab đó sau khi kiểm.
*Ghi chú:* đặc tả dòng 1729 mô tả "nút Xem mở hộp xem PDF"; phần mềm chọn cách mở tệp ở tab mới. Yêu cầu nghiệp vụ — xem được tệp ngay từ màn Chi tiết, không phải vào chế độ Sửa — đã đạt.

### 13:53 — Tab "Tư vấn viên liên kết"
Bấm tab → bảng có đủ 7 cột đặc tả (dòng 1730): STT · Mã tư vấn viên · Họ tên · Loại · Trạng thái tư vấn viên · Ngày tham gia · Trạng thái liên kết. **2 dòng dữ liệu thật**:
| STT | Mã TVV | Họ tên | Loại | Trạng thái TVV | Ngày tham gia | Trạng thái liên kết |
|---|---|---|---|---|---|---|
| 1 | TVV-BTP-TW-0059 | Hoàng Thị Thanh Thảo | Tư vấn viên | Từ chối | — | Đang kích hoạt |
| 2 | TVV-BTP-TW-0055 | Tester TKM | Tư vấn viên | Chờ kích hoạt tài khoản | — | Đang kích hoạt |

Họ tên là liên kết bấm được (sang chi tiết tư vấn viên). Ảnh: `image/QLDMTCTV_OOS_11-v2-02-tab-tu-van-vien-lien-ket-co-2-dong.png` (đã mở đọc).

### 13:54 — Tab "Lịch sử"
Bấm tab → bảng 4 cột đúng đặc tả dòng 1732: Thời gian · Người thực hiện · Hành động · Ghi chú / lý do. **9 dòng nhật ký**, gồm cả thao tác vừa làm:
`04/08/2026 13:52 · Cán bộ NV Trung ương · Cập nhật`, `04/08/2026 13:09 · Công khai`, `07/05/2026 01:35 · CB Phê duyệt TW 02 · Phê duyệt`, `07/05/2026 01:33 · Trình phê duyệt`…
Ảnh: `image/QLDMTCTV_OOS_11-v2-03-tab-lich-su-9-dong-nhat-ky.png` (đã mở đọc).

### Đối chiếu đặc tả
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`
- dòng 1702: "Trang chi tiết 3 tab + 6 nút hành động ở header" — đủ 3 tab.
- dòng 1715: đường dẫn "… > [Tên tổ chức]" — khớp.
- dòng 1729: tab "Thông tin" hiển thị 6 nhóm thông tin, trong đó nhóm file đính kèm "mỗi file có nút Xem mở hộp xem PDF, Tải xuống" — khớp (chi tiết cách mở xem ở mục 13:53).
- dòng 1730: tab "Tư vấn viên liên kết" với 7 cột — khớp.
- dòng 1732: tab "Lịch sử" nhật ký thao tác — khớp.

### Kết luận
Cả 4 ý của bug gốc đều hết trên cùng một hồ sơ đã dựng đủ tiền đề ⇒ **Pass**.

### Ghi nhận thêm (ngoài phạm vi 4 ý, KHÔNG làm đổi verdict)
- Cột **"Ngày tham gia"** ở tab Tư vấn viên liên kết hiện "—" cho cả 2 dòng (dữ liệu liên kết cũ chưa có ngày tham gia).
- Nút quay lại ghi **"← Danh sách"**, đặc tả dòng 1716 ghi "← Quay lại danh sách".

### Dữ liệu để lại trên môi trường
`TC-BTP-TW-0001` nay có thêm 1 tệp đính kèm `qd-cong-bo-alpha-reverify-v2.pdf` (do mình gắn để dựng tiền đề; các trường khác giữ nguyên).
