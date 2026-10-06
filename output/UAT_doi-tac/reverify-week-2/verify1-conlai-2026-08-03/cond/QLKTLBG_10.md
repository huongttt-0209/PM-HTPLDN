# QLKTLBG_10 — Bảng đối chiếu điều kiện (re-verify sau dev fix, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 132 · Verdict re-verify 2026-08-04: `Pass` (vòng 1 ngày 2026-08-03 là `Open`)
> Dòng TC do QA mở mới khi verify `QLKTLBG_09`: bài giảng loại **PDF** cũng không xem trực tuyến được — khung xem trước báo *"18.143.165.120.nip.io refused to connect."*, không có thông báo thay thế, không có nút *"Tải về"*.
> Đây là bug phụ thuộc **loại tệp / dữ liệu tiền đề** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1, 2026-08-03) | Mình test (2026-08-04) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — **CB Nghiệp vụ Trung ương (`CB_NV_TW`)**, đơn vị `BTP · TW` (Cục Bổ trợ tư pháp); là tác nhân `FR-III-07` cho phép thao tác trên màn Kho tài liệu | `cbnv_tw_01` (mật khẩu `Test@1234`, OTP MailHog) — header web hiện đúng `CB Nghiệp vụ - Trung ương #01` · `CB_NV_TW` · `BTP · TW`; `auth-store` trả `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `donViId: …-8000-000000000001` (**trùng khít đơn vị của `cbnv_tw`**), có quyền `create_bai_giang` / `read_bai_giang` | **Không** |
| Màn hình + thao tác | Màn `Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách`; bấm **icon con mắt** cột `Thao tác` của dòng PDF → mở hộp thoại `Xem trước: …` | Cùng màn `/dao-tao/bai-giang/danh-sach`; bấm **icon con mắt** cột `Thao tác` của đúng dòng PDF → mở hộp thoại `Xem trước: …` (gói giao diện `index-BrKDNUvo.js`) | **Không** |
| Entity + **trạng thái** | Bài giảng `QA VERIFY 03/08 - QLKTLBG_10 PDF that cong khai` — `Loại tài liệu = PDF`, `Công khai = Đã công khai` (ngày công khai `03/08/2026 16:09`) | **Seed MỚI qua giao diện** (Nguyên tắc 4) bài giảng `QA RETEST 04/08 - QLKTLBG_10 PDF that cong khai` — `Loại tài liệu = PDF`, `Công khai` bật (`Đã công khai`, ngày công khai `03/08/2026 23:25`). Đo thêm **đúng bản ghi của bug gốc** (`QA VERIFY 03/08 …`, 979 B, seed trước bản vá) → **2/2 bản ghi cùng kết quả** | **Không** |
| Dữ liệu tiền đề — **định dạng tệp bài giảng** | Tệp `QLKTLBG_10-pdf-that-QA.pdf` — PDF **thật** 2 trang có chữ đọc được (kiểm chứng bằng PyMuPDF), 979 B, upload qua form `Thêm mới` với `Loại tài liệu = PDF` (form chỉ nhận `.pdf`) | Tệp `QLKTLBG_10-pdf-that-QA-retest0804.pdf` — PDF **thật** 2 trang có chữ đọc được (sinh + kiểm chứng bằng PyMuPDF), **1.6 KB**, upload qua form `Thêm mới` với `Loại tài liệu = PDF`. Cùng phần mở rộng, cùng kiểu MIME `application/pdf` | **Không** |
| Input / filter | Không đặt bộ lọc nào; bản ghi đích nằm đầu danh sách | Giữ nguyên `Bộ lọc nâng cao (2)` mặc định của màn, các ô lọc để trống; bản ghi đích nằm đầu danh sách | **Không** |

## Đối chứng đã chạy để khu trú lỗi (cùng màn, cùng tài khoản, cùng hộp thoại "Xem trước") — đo 2026-08-04

- **PDF** — bản ghi `QA RETEST 04/08 …` (seed mới) và `QA VERIFY 03/08 …` (chính bản ghi của bug gốc): khung xem trước **hiển thị đúng trang PDF ngay trong trang**, không còn dòng *"refused to connect"*. Hộp thoại có thêm nút **Tải về**.
- **Slide (.pptx)** — xem mục riêng của `QLKTLBG_09`: cũng đã trình chiếu được nội dung trong trang.
- **Video (YouTube)** — vẫn xem được như trước.

→ So với vòng 1: cả 3 loại tài liệu nay đều xem trực tuyến được.

## Ghi chú phương pháp (re-verify 2026-08-04)

- **Đo 2 cách độc lập, khớp nhau:** (a) ảnh chụp toàn cỡ chính hộp thoại → đọc rõ nguyên văn chữ trang 1 của tệp (`QA RETEST 04/08 - QLKTLBG_10 - Trang 1` + dòng mô tả); (b) trình xem bên trong khung báo đúng **2 trang** (`1 / 2` + 2 ảnh thu nhỏ) — khớp số trang tệp đã tải lên. Không phải khung trắng.
- **Kiểm nút "Tải về" bằng cách BẤM THẬT**, không dừng ở "thấy nút": tệp về máy, mở lại bằng PyMuPDF ra đúng 2 trang với đúng chữ, mã băm MD5 **trùng khít** tệp đã tải lên (`dcb6273e…`).
- **Bản ghi cũ (tạo trước bản vá) cũng đo:** nội dung nạp vào khung là dữ liệu PDF thật — kiểm bằng cách đọc lại nguồn của khung, ra đúng **979 byte** khớp dung lượng bảng hiển thị và đúng đầu tệp `%PDF-1.4`; ảnh chụp cũng thấy rõ chữ 2 trang. ⇒ Không phải chỉ bản ghi mới mới xem được.
- **Cột `Thao tác`** (`:1951`): liệt kê nút của toàn bộ dòng → mọi dòng Slide/PDF đều có nút `Tải về` (tooltip "Tải về"), riêng dòng Video **không** có — đúng phạm vi "chỉ Slide/PDF".
- Bộ bắt thông báo cài **trước** thao tác lưu: đúng **1 thông báo** "Tạo bài giảng thành công", không lặp.

**Kết luận: 0 GAP** — đã tái lập đúng vai trò, đúng màn, đúng loại tài liệu và đúng định dạng tệp của bug gốc, và còn đo lại trên chính bản ghi của bug gốc.
