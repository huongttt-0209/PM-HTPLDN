# QLKTLBG_10 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 132 · Verdict Verify 2: `Pass`
> Bug gốc (cùng gốc `QLKTLBG_09`, nhánh loại **PDF**): bấm xem trước bài giảng PDF thì khung xem trước chỉ hiện
> biểu tượng tệp lỗi kèm dòng **"…nip.io refused to connect."** (máy chủ trả tệp kèm thiết lập chặn nhúng trang),
> **không** có thông báo thay thế "Không thể xem trực tuyến", **không** có nút "Tải về" ở hộp thoại lẫn cột Thao tác.
> Bug phụ thuộc **loại tệp / dữ liệu tiền đề** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(bản dựng MỚI, khác gói `index-BrKDNUvo.js` của vòng trước; dữ liệu cũng khác ⇒ seed lại tiền đề từ đầu).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — Cán bộ nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị `BTP · TW` | Đăng nhập đúng **`cbnv_tw`** (`Test@1234`) — `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `donViId: 00000000-0000-4000-8000-000000000001`; thanh trên hiện `Cán bộ NV Trung ương · CB_NV_TW · BTP · TW` | Không |
| Màn hình + thao tác | Màn `Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách`; bấm **icon con mắt** cột `Thao tác` của dòng PDF → hộp thoại `Xem trước: …` | Cùng màn `/dao-tao/bai-giang/danh-sach`; bấm đúng **icon con mắt** của dòng PDF → mở hộp thoại `Xem trước: …` | Không |
| Entity + **trạng thái** | Bài giảng `Loại tài liệu = PDF`, tệp `.pdf` hợp lệ, `Công khai = Đã công khai` | **Seed MỚI qua giao diện** (Nguyên tắc 4): `QA VERIFY2 04/08 - QLKTLBG_10 PDF cong khai` — PDF, **Đã công khai 04/08/2026 15:29**. Đo thêm **3 bản ghi PDF có sẵn từ trước bản vá** (tệp thật còn trên máy chủ): `Tài liệu công khai cổng…` (3.1 MB, **514 trang**, tải lên 28/07/2026), `sdsdsdsss11` (329 B, 04/06/2026), `Bài giảng số 10` (28.7 KB, 25/05/2026) ⇒ **4 bản ghi PDF có tệp thật** | Không |
| Dữ liệu tiền đề — **định dạng tệp** | Tệp `.pdf` thật (bug gốc dùng `QLKTLBG_10-pdf-that-QA.pdf`, 2 trang, 979 B) | `QLKTLBG_10-v2-pdf-that.pdf` — PDF thật **2 trang**, chữ đọc được, 1.266 B, md5 `db816dd2…` (sinh + kiểm bằng PyMuPDF); upload qua form `Thêm mới` với `Loại tài liệu = PDF` (form chỉ nhận `.pdf`) | Không |
| Input / filter | Không đặt bộ lọc; bản ghi đích ở đầu danh sách | Giữ `Bộ lọc nâng cao (2)` mặc định, các ô lọc để trống; bản ghi đích ở đầu danh sách | Không |

## Đã cố BÁC BỎ kết luận Pass bằng những cách sau — không bác được

1. **Nhắm thẳng cơ chế gây lỗi cũ (chặn nhúng trang):** khung xem trước nay nạp bằng địa chỉ tạm **cùng gốc** (`blob:https://htpldn-uat.ospgroup.vn/…`) thay vì trỏ thẳng vào địa chỉ tệp trên máy chủ ⇒ không còn bị trình duyệt chặn. Nhật ký lỗi trình duyệt **không** còn dòng nào về chặn nhúng trang.
2. **Không tin 1 bản ghi:** đo **4 bản ghi PDF** khác nhau (1 seed mới + 3 bản ghi cũ có tệp thật, trong đó có tệp **3.1 MB / 514 trang** tải lên **trước** bản vá) → **4/4 hiện nội dung PDF ngay trong trang**, có thanh trang `1 / N`, dải ảnh thu nhỏ và ảnh bìa đọc được (ảnh `QLKTLBG_10-v2-02-pdf-cu-3.1MB-cung-render-inline.png`).
3. **Đọc được chữ thật trong khung, không chỉ "có khung"**: ảnh chụp toàn cỡ đọc rõ nguyên văn chuỗi neo `QA VERIFY2 04/08 - QLKTLBG_10 - Trang 1 | Neo: ZXQ-PDF-2263-TRANG1`, và số trang hiển thị `1 / 2` khớp tệp đã tải lên.
4. **Không dừng ở "thấy nút":** bấm THẬT `Tải về` → tệp về máy 1.266 byte, mở bằng PyMuPDF ra đúng **2 trang** với đúng chữ, **md5 `db816dd27bf019fb813ffeed367fb26b` trùng khít** tệp đã tải lên.
5. **Truy nhánh fallback của đặc tả** (`srs-fr-03-dao-tao.md:1955`): 2 bản ghi PDF cũ (`Bài giảng 08`, `Bài giảng 09`) có đường dẫn tệp trỏ tới chỗ **không còn tệp trên máy chủ** → hộp thoại hiện đúng **"Không thể xem trực tuyến định dạng này" + nút "Tải về"** (ảnh `QLKTLBG_10-v2-03-fallback-pdf-khong-doc-duoc.png`), không còn để trắng hay báo lỗi kỹ thuật.
6. **Quét toàn bảng cột `Thao tác`** (`srs-fr-03-dao-tao.md:1951`): mọi dòng Slide/PDF đều có nút `Tải về`, mọi dòng Video đều KHÔNG có ⇒ đúng phạm vi "chỉ Slide/PDF".
7. **Khu trú nguyên nhân 2 bản ghi không xem được:** tra đường dẫn tệp của từng bản ghi — chỉ 3 bản ghi mẫu cũ (`Bài giảng 07/08/09`) trỏ vào `/uploads/bai-giang/…` là chỗ **không tồn tại tệp** trên môi trường này; mọi bản ghi có tệp thật đều xem được ⇒ không phải bản vá hụt, mà là dữ liệu mẫu treo.

## Ghi chú phương pháp

- Bộ bắt thông báo `tools/toast-capture.js` cài **trước** thao tác lưu, tự kiểm `soObserverDangSong = 1`.
- Lượt seed PDF: **2 request ghi** (`upload-file`, `bai-giangs`) ↔ **2 thông báo** khác nhau, không lặp.
- Ảnh chụp đã **mở ra đọc từng tấm**.

**Kết luận: 0 GAP** — đã tái lập đúng vai trò, đúng màn, đúng loại tài liệu, đúng định dạng tệp và đúng trạng thái công khai của bug gốc; cố bác bằng 7 hướng mà lỗi không tái hiện ⇒ `Pass`.
