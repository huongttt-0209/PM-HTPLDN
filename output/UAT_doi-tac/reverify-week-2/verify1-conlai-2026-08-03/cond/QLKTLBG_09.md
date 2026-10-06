# QLKTLBG_09 — Bảng đối chiếu điều kiện (re-verify sau dev fix, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 117 · Verdict re-verify 2026-08-04: `Pass` (vòng 1 ngày 2026-08-03 là `Open`)
> Đối tác báo: Xem bài giảng loại **Slide** → hệ thống **tải tệp xuống**, **không trình chiếu inline**.
> Đây là bug phụ thuộc **loại tệp / dữ liệu tiền đề** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `Cán bộ NV Trung ương` — mã vai trò **CB_NV_TW**, đơn vị **BTP · TW** (đọc header phải, frame `t000.00s` / `t003.10s` của `QLKTLBG_09_v2.webm`) | Đăng nhập **`cbnv_tw_01`** (mật khẩu `Test@1234`, OTP MailHog) — header web hiện đúng `CB Nghiệp vụ - Trung ương #01` · `CB_NV_TW` · `BTP · TW`; `auth-store` trả `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `donViId: …-8000-000000000001` (**trùng khít đơn vị của `cbnv_tw` dùng ở vòng 1**), có quyền `create_bai_giang` / `read_bai_giang` | **Không** |
| Màn hình + thao tác | Màn `Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách`; bấm **icon con mắt** cột `Thao tác`, tooltip **"Xem trước"** (frame `t003.10s`) | Cùng màn `/dao-tao/bai-giang/danh-sach`; bấm **icon con mắt** cột `Thao tác` của đúng dòng Slide → mở hộp thoại `Xem trước: …` (gói giao diện `index-BrKDNUvo.js`) | **Không** |
| Entity + **trạng thái** (state machine) | Bài giảng `TKM thêm mới slide bài giảng` — `Loại tài liệu = **Slide**`, `Công khai = **Đã công khai**`, `Ngày công khai = 23/07/2026 16:01`, có **Ảnh đại diện** (frame `t003.62s`) | **Seed MỚI qua giao diện** (Nguyên tắc 4) bài giảng `QA RETEST 04/08 - QLKTLBG_09 Slide PPTX cong khai` (id `154371fa-fe23-444c-9679-1ff2b54a7a47`) — `Loại tài liệu = Slide`, `Công khai` bật (`Đã công khai`, ngày công khai `03/08/2026 23:19`). Đo thêm bản ghi Slide seed TRƯỚC bản vá (`QA VERIFY 03/08 …`, `9e7e90d7-…`) → **2/2 bản ghi cùng kết quả** | **Không** |
| Dữ liệu tiền đề — **định dạng tệp bài giảng** | Tệp **`10.2. Tia, đoạn thẳng.pptx`**, `Save as type = Microsoft PowerPoint Presentation (*.pptx)`, dung lượng **2.2 MB** (đọc từ hộp thoại Save As, frame `t004.14s`) | Tệp **`QLKTLBG_09-slide-that-QA-retest0804.pptx`** — PowerPoint **thật** (2 slide có chữ đọc được, sinh bằng `python-pptx`), **28.5 KB**, upload qua form `Thêm mới` với `Loại tài liệu = Slide` (form chỉ nhận `.pptx`). Cùng phần mở rộng, cùng kiểu MIME `application/vnd.openxmlformats-officedocument.presentationml.presentation` như đối tác | **Không** |
| Input / filter | Đối tác đang bật `Bộ lọc nâng cao (2)`, các ô lọc còn lại để trống (frame `t003.10s`) — bộ lọc chỉ ảnh hưởng danh sách, không ảnh hưởng thao tác xem trước | Giữ nguyên `Bộ lọc nâng cao (2)` mặc định của màn, các ô lọc để trống; bản ghi đích vẫn hiện ở đầu danh sách nên không cần đổi lọc | **Không** |

## Đối chứng đã chạy để khu trú lỗi (cùng màn, cùng tài khoản, cùng hộp thoại "Xem trước") — đo lại 2026-08-04

- **Slide (.pptx)** — bản ghi `QA RETEST 04/08 …` (seed mới) và `QA VERIFY 03/08 …` (seed trước bản vá): khung xem trước **trình chiếu đúng nội dung slide ngay trong trang**, đọc được nguyên văn chữ trong tệp. Hộp thoại có thêm nút **Tải về**.
- **PDF** — xem mục riêng của `QLKTLBG_10`: cũng đã xem được nội dung trong trang.
- **Video (YouTube)** — vẫn xem được như trước.

→ So với vòng 1: cả 3 loại tài liệu nay đều xem trực tuyến được.

## Ghi chú phương pháp (re-verify 2026-08-04)

- **Đo 2 cách độc lập, khớp nhau:** (a) đọc chữ hiển thị trong mã trang của hộp thoại → ra đúng 5 dòng chữ của tệp `.pptx` đã tải lên; (b) ảnh chụp toàn cỡ chính hộp thoại → nhìn thấy rõ trang slide 1.
- **Kiểm nút "Tải về" bằng cách BẤM THẬT**, không dừng ở "thấy nút": tệp về máy, mở lại bằng `python-pptx` ra đúng 2 slide, mã băm MD5 **trùng khít** tệp đã tải lên (`c96ee3f0…`).
- **Cột `Thao tác`** (`:1951`): liệt kê nút của toàn bộ 10 dòng → 9 dòng Slide/PDF đều có nút `Tải về` (tooltip "Tải về"), riêng dòng Video **không** có — đúng phạm vi "chỉ Slide/PDF".
- Bộ bắt thông báo cài **trước** thao tác lưu: đúng **1 thông báo** "Tạo bài giảng thành công", không lặp.
