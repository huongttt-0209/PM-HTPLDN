# CPCTHTTTG_06 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 2`, dòng 261 (tab `UAT_TGPL Doanh Nghiệp-tuần 3`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Bản mới nhất của môi trường nghiệm thu | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB_NV_TW · cấp TW · Cục Bổ trợ tư pháp | Không |
| Màn hình | Báo cáo thống kê | Sidebar → Báo cáo thống kê (`/bao-cao`) | Không |
| Loại báo cáo | Chi phí theo thời gian | `BC Chi phí theo thời gian` | Không |
| Kỳ báo cáo | Năm 2026 | Kỳ `Năm` → tự điền 01/01/2026 – 31/12/2026 | Không |
| Đơn vị | Toàn quốc | `Toàn quốc` | Không |
| Thao tác | Xem báo cáo → Xuất PDF → lưu tệp | Bấm [Xem báo cáo] → [Xuất PDF] → hộp thoại "Tùy chọn in báo cáo PDF" (A4 · Dọc) → [Xuất file] | Không |
| Số lần đo | Xuất lại lần nữa trong cùng ngày | Đo **5 lượt** trong cùng phiên: 3 lượt vào loại báo cáo này, 2 lượt vào loại khác để đối chứng | Không |
| Cách đọc tệp | Mở tệp, đọc đầu trang đầu + cuối trang cuối | Mở và đọc nội dung thật của từng tệp, kèm tên tệp và yêu cầu mạng của chính lệnh xuất | Không |

**Kết luận: 0 GAP → KHÔNG PASS (Reopen).** Điều kiện đo khớp bug gốc, nhưng lệnh [Xuất PDF] của báo cáo
này **xuất ra tệp của một báo cáo khác** trong tình huống dùng thông thường.

## Đối chiếu từng ý của khối tiêu chí

### Điều không đạt — tệp xuất ra không phải báo cáo đang xem

Màn hình hiển thị đúng `BC Chi phí theo thời gian` (số liệu đúng, thời điểm tạo đúng), nhưng tệp tải về lại
là **BC CHI PHÍ THEO ĐƠN VỊ** / **BC CHI PHÍ CHI TRẢ HỖ TRỢ** — tức báo cáo mà người dùng đã xem **ngay
trước đó** trong cùng phiên. Không có thông báo lỗi nào, tên tệp cũng mang tên báo cáo kia, nên người dùng
rất dễ nộp nhầm tệp mà không biết.

Năm lượt đo liên tiếp, có kèm yêu cầu mạng của chính lệnh xuất:

- **Lượt A — đúng.** Chọn `BC Chi phí theo đơn vị`; màn gọi dữ liệu `chi-phi-theo-don-vi`; lệnh xuất gửi
  `BC_CHI_PHI_THEO_DON_VI`; tệp về `BaoCaoChiPhiTheoDonVi_20260805_1705.pdf`, bên trong ghi
  `BC CHI PHÍ THEO ĐƠN VỊ`.
- **Lượt B — SAI.** Chọn `BC Chi phí theo thời gian`; màn gọi dữ liệu `chi-phi-theo-thoi-gian` (đúng), nhưng
  lệnh xuất vẫn gửi `BC_CHI_PHI_THEO_DON_VI`; tệp về `BaoCaoChiPhiTheoDonVi_20260805_1706.pdf`, bên trong
  ghi `BC CHI PHÍ THEO ĐƠN VỊ` — là báo cáo của lượt A.
- **Lượt C — đúng.** Chọn `BC Chi phí chi trả hỗ trợ`; màn gọi `chi-phi-chi-tra`; lệnh xuất gửi
  `BC_CHI_PHI_CHI_TRA`; tệp về `BaoCaoChiPhiChiTra_20260805_1707.pdf`, bên trong ghi
  `BC CHI PHÍ CHI TRẢ HỖ TRỢ`.
- **Lượt D — SAI.** Chọn lại `BC Chi phí theo thời gian`; màn gọi `chi-phi-theo-thoi-gian` (đúng), nhưng
  lệnh xuất vẫn gửi `BC_CHI_PHI_CHI_TRA`; tệp về `BaoCaoChiPhiChiTra_20260805_1707.pdf`, bên trong ghi
  `BC CHI PHÍ CHI TRẢ HỖ TRỢ` — là báo cáo của lượt C.
- **Lượt E — đúng.** Tải lại trang rồi chọn `BC Chi phí theo thời gian` làm loại **đầu tiên**; tệp về
  `BaoCaoChiPhiTheoThoiGian_20260805_1709.pdf`, bên trong ghi `BC CHI PHÍ THEO THỜI GIAN`.

Đọc theo bảng trên:

- **Tái hiện được, không phải ngẫu nhiên**: hai lượt B và D độc lập nhau, mỗi lượt đều ra tệp của đúng báo
  cáo vừa xem trước đó (đơn vị → rồi chi trả). Lượt đo ban đầu lúc 16:58 cũng vậy: màn hình là
  `BC Chi phí theo thời gian` nhưng tệp ra `BaoCaoChiPhiTheoLoaiDn_20260805_1658.pdf` — trùng báo cáo
  "Chi phí theo loại hình DN" đã xuất lúc 16:52.
- **Không phải lỗi chung của màn Báo cáo thống kê**: lượt A và C đổi sang loại khác thì tệp ra đúng. 19 loại
  báo cáo còn lại của đợt đo này (đã đối chiếu tiêu đề bên trong từng tệp) đều đúng loại. Chỉ riêng lối vào
  `BC Chi phí theo thời gian` bị.
- **Điều kiện xảy ra**: đã xem một báo cáo khác trước đó trong cùng phiên rồi mới chuyển sang báo cáo này.
  Nếu tải lại trang và chọn thẳng `BC Chi phí theo thời gian` làm loại đầu tiên (lượt E) thì tệp ra đúng —
  nên khi dev đo trên một tab mới sẽ thấy "đã chạy được", còn người dùng thật xem vài báo cáo liền nhau
  thì gặp lỗi.
- **Yêu cầu nghiệp vụ chưa đạt**: tệp người dùng tải về phải là chính báo cáo đang hiển thị trên màn hình
  với đúng điều kiện lọc đang chọn. Hiện tệp mang nội dung và tên của báo cáo khác mà không hề báo gì.

### Các ý còn lại của phiếu — đo trên tệp xuất đúng (lượt E)

Chỉ đo được khi báo cáo ra đúng loại; các ý này đạt, nhưng **không đủ để Pass** vì ý chính ở trên chưa đạt.

- **Tệp xuất được, không còn báo lỗi**: ra tệp PDF **31 783 byte, 1 trang**. Thông báo "Không thể tạo file
  xuất. Vui lòng thử lại." của phản ánh gốc không còn.
- **Tên tệp có đủ ngày lẫn giờ-phút**: `BaoCaoChiPhiTheoThoiGian_20260805_1709.pdf` — đúng dạng
  `{TênBáoCáo}_{YYYYMMDD_HHmm}.pdf`.
- **Hai lần xuất trong cùng ngày ra hai tên khác nhau**: lượt đo 16:58 → 16:59 cho hai tên khác nhau theo
  phút; các lượt A/C/E cũng vậy.
- **Đầu trang có quốc hiệu, tiêu ngữ và tên cơ quan ban hành**: `CỤC BỔ TRỢ TƯ PHÁP - BỘ TƯ PHÁP` ·
  `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` · `Độc lập - Tự do - Hạnh phúc`.
- **Đủ bốn mục**: `BC CHI PHÍ THEO THỜI GIAN` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` ·
  `Đơn vị: Toàn quốc` · `Ngày tạo: 05/08/2026`.
- **Khổ A4**: `595,28 × 841,89` điểm — đúng A4 dọc.
- **Hai điều phiếu dặn KHÔNG chấm FAIL đã tôn trọng**: tệp không có chữ ký số và không có dòng chức danh
  người ký — không dùng làm căn cứ trượt.

## Bằng chứng

- Bản bắt lượt đo đầu (16:58): `../evidence/CPCTHTTTG_06-pdf-capture.json` · tệp `../evidence/CPCTHTTTG_06.pdf`
- Năm lượt đối chứng: `../evidence/tn-buoc-A-donvi.json` · `tn-buoc-B-thoigian.json` ·
  `tn-buoc-C-chitra.json` · `tn-buoc-D-thoigian2.json` · `tn-buoc-E-tailaitrang.json`
  (mỗi tệp có nguyên văn yêu cầu mạng của lệnh xuất) · tệp PDF tương ứng `../evidence/tn-A.pdf` …
  `../evidence/tn-E.pdf`

## Ghi nhận thêm

- **Cỡ chữ trong bảng số liệu là 11, không phải 13** — giống toàn bộ nhóm báo cáo thống kê, đã ghi chi tiết
  ở `cond/SLHDVM_07-uat.md`; không dùng làm căn cứ trượt phiếu này.
- Đã rà lại tiêu đề bên trong **toàn bộ tệp PDF** đã xuất trong đợt đo này để chắc chắn không phiếu nào bị
  chấm nhầm vì cùng nguyên nhân — chỉ duy nhất phiếu này lệch.
- Không tạo, không sửa dữ liệu nghiệp vụ nào khi đo phiếu này — chỉ xem và xuất báo cáo.
