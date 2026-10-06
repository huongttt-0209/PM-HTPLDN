# Re-verify lại 3 lỗi Reopen — Vòng 7, ngày 25/07/2026

Tab sheet: `UAT_TGPL Doanh Nghiệp-tuần 3` · Môi trường `https://18.143.165.120.nip.io`
Công cụ: Chrome DevTools MCP (thao tác trên giao diện thật).

## Kết quả

| Dòng | Mã TC | Vòng 6 | Vòng 7 | Vì sao |
|---|---|---|---|---|
| 293 | QLHSPLDN_03 | Reopen | **Pass** | Bấm [Xem] mở được tệp, không còn bị đá sang trang 403 |
| 70 | THDG_03 | Reopen | **Pass** | Thông báo điểm ngoài khoảng đã bằng tiếng Việt, hết chuỗi tiếng Anh thô |
| 290 | QLNDTVVCG_40 | Reopen | **Pass** | Giờ-phút trong tên tệp Excel đã là giờ Việt Nam |

Đã ghi Verify=Pass ở sheet tuần 3 và `Trạng thái dev fix` = `dev done` ở sheet đối tác
(P1525 · P813 · P1510). Không thêm dòng nào ở sheet đối tác.

## Cách kiểm từng lỗi

### 293 — QLHSPLDN_03 (tài khoản cbnv_hn)

Dữ liệu dựng mới: hồ sơ pháp lý **HSPL-20260725-0004** trên DN-HNI-0006, kèm tệp
`R7-HSPL-RETEST.pdf` tạo mới hoàn toàn. Mở [Sửa] → bấm [Xem]:

- Trang vẫn ở màn hồ sơ, mở tab mới hiện đúng nội dung tệp (`R7-HSPL-RETEST vong 7 - 2026-07-25`).
- Lệnh tải tệp trả về **200**, trước đây là 403 kèm mã `ERR-PERM-FILE-03`.
- Kiểm thêm hồ sơ **cũ** HSPL-20260725-0003 (tạo trước bản sửa): cũng mở được →
  bản sửa phủ cả dữ liệu cũ, không chỉ dữ liệu mới.

Ảnh: `image/R7-QLHSPLDN_03-01-bam-Xem-mo-duoc-tep.png`

### 70 — THDG_03 (tài khoản cbnv_hn)

Chấm trên đợt **DG-20260725-0003**, vụ việc EEE-VH-014 **chưa từng được chấm lần nào**.
Bốn phép thử:

| Điểm nhập | Thông báo nhận được | Số khung |
|---|---|---|
| −3 (tiêu chí 1) | Điểm cho tiêu chí 'Mức độ hoàn thành vụ việc' phải từ 0 đến 10 | 1 |
| 15 (tiêu chí 1) | Điểm cho tiêu chí 'Mức độ hoàn thành vụ việc' vượt quá điểm tối đa (10) | 1 |
| 9 / 8 / 7 / 10 (hợp lệ) | Đã lưu kết quả chấm điểm → vụ việc chuyển "Đã chấm 8.40 Tốt" | 1 |
| −0.5 (tiêu chí 3, trên bản ghi **đã chấm**) | Điểm cho tiêu chí 'Sự hài lòng của người được trợ giúp pháp lý' phải từ 0 đến 10 | 1 |

Máy chủ trả mã `ERR-DG-SC-06` kèm đúng câu tiếng Việt trên. Vòng 6 câu này là
`diem must not be less than 0`. Thông báo gọi đúng tên tiêu chí bị sai, thử ở 2 tiêu chí
khác nhau và 2 trạng thái dữ liệu khác nhau (chưa chấm / đã chấm).

Ảnh: `image/R7-THDG_03-01-thong-bao-diem-am-tieng-viet.png` ·
`image/R7-THDG_03-02-luu-diem-hop-le-thanh-cong.png`

### 290 — QLNDTVVCG_40 (tài khoản cbnv_tw_02)

Màn "Tư vấn" → "Tư vấn chuyên sâu" → [Xuất Excel]. Bấm lúc **14:15 giờ Việt Nam**:

- Tên tệp về máy: `TVCS-danh-sach-20260725-1415.xlsx` — khớp đúng giờ bấm.
  Vòng 6 bấm lúc 12:10 nhưng tên tệp là `…-0510`, lệch 7 tiếng.
- Cột "Ngày tạo" khớp **5/5** dòng với màn hình, trong đó 2 dòng nằm đúng khung rạng sáng
  (02:33 và 02:22 ngày 25/07) — nếu còn tính theo giờ quốc tế thì hai dòng này phải lùi về 24/07.
- Cột đầy đủ: Mã tư vấn · Doanh nghiệp · Chuyên gia · Lĩnh vực · Tiêu đề · Trạng thái ·
  Ngày bắt đầu · Ngày tạo, cộng thêm "Ngày hoàn thành" và "Nội dung tư vấn (đầy đủ)".

Dữ liệu dựng mới: **TVCS-20260725-0008** (tạo lúc 14:14) — có mặt trong tệp xuất với đúng giờ.

Tệp bằng chứng: `tep-xuat/TVCS-danh-sach-20260725-1415.xlsx` ·
ảnh `image/R7-QLNDTVVCG_40-01-man-danh-sach-ngay-tao.png`

## Ghi nhận thêm, chưa báo thành lỗi

Cột "Ngày bắt đầu" trong tệp Excel hiện dạng "07:00 25/07/2026", trong khi màn hình chỉ hiện
"25/07/2026". Trường này chỉ có ngày, máy chủ lưu là `2026-07-25T00:00:00.000Z`; phần "07:00"
là do tệp xuất dùng chung khuôn giờ-phút với cột "Ngày tạo". **Phần ngày vẫn đúng**, không lệch,
nên đây chỉ là chi tiết hình thức và nằm ngoài nội dung case 290. Ghi lại để đối tác quyết định
có nêu thành mục riêng hay không.

## Đính chính ghi chú vòng 6

Bảng kết quả vòng 6 ghi lỗi còn lại của dòng 290 là *"cột Ngày tạo trong tệp Excel lệch 1 ngày"*.
Cách ghi đó không chính xác: tại vòng 6 cột "Ngày tạo" đã đúng, lỗi còn lại nằm ở **giờ-phút trong
tên tệp**. Nội dung đúng đã ghi trong ô "DEV phản hồi lần 1" của sheet.

## Ghi chú kỹ thuật — cách chụp được thông báo tự tắt

Vòng 6 không chụp được thông báo nổi vì nó chỉ sống ~3 giây còn lệnh chụp mất ~2,5 giây.
Vòng 7 xử lý được: **hẹn giờ bấm nút sau 2,5 giây rồi mới gọi lệnh chụp**, để lúc ảnh được
chụp thì thông báo vừa hiện. Cách này áp dụng lại được cho mọi thông báo nổi.
