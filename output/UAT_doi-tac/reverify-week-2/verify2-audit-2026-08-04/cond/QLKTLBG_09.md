# QLKTLBG_09 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 117 · Verdict Verify 2: `Pass`
> Bug gốc: bài giảng **Loại tài liệu = Slide (.pptx)**, đã công khai, có ảnh đại diện → bấm xem trước thì
> hệ thống **tải tệp xuống / khung xem trước TRẮNG**, không trình chiếu inline; đồng thời **không** có thông báo
> thay thế "Không thể xem trực tuyến" và **không** có nút "Tải về" ở hộp thoại lẫn ở cột Thao tác.
> Bug phụ thuộc **loại tệp / dữ liệu tiền đề** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(khác gói `index-BrKDNUvo.js` của vòng trước ⇒ đây là bản dựng MỚI, dữ liệu cũng khác: 14 bản ghi gốc,
không còn bản ghi nào do vòng trước tạo ⇒ mọi tiền đề phải seed lại từ đầu).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — Cán bộ nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị `BTP · TW` (Cục Bổ trợ tư pháp) | Đăng nhập đúng **`cbnv_tw`** (mật khẩu `Test@1234`) — không phải tài khoản dự phòng. `auth-store` trả `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `donViId: 00000000-0000-4000-8000-000000000001`; thanh trên cùng hiện `Cán bộ NV Trung ương · CB_NV_TW · BTP · TW` | Không |
| Màn hình + thao tác | Màn `Đào tạo, tập huấn → Kho tài liệu / Bài giảng → Danh sách`; bấm **icon con mắt** cột `Thao tác` → hộp thoại `Xem trước: …` | Cùng màn `/dao-tao/bai-giang/danh-sach`; bấm đúng **icon con mắt** cột `Thao tác` của đúng dòng Slide → mở hộp thoại `Xem trước: …` | Không |
| Entity + **trạng thái** | Bài giảng `Loại tài liệu = Slide`, `Công khai = Đã công khai`, **có Ảnh đại diện** | **Seed MỚI qua giao diện** (Nguyên tắc 4), 2 bản ghi: (1) `QA VERIFY2 04/08 - QLKTLBG_09 Slide PPTX cong khai` (id `bebead6a-1866-4595-b57c-cc7d88a51158`) — Slide, **Đã công khai 04/08/2026 15:12**, **có ảnh đại diện**; (2) `QA VERIFY2 04/08 - QLKTLBG_09 Slide PPTX phuc tap` — Slide, Đã công khai 04/08/2026 15:18. Đo thêm bản ghi Slide **có sẵn từ trước bản vá** (`Bài giảng 07 - Quản lý Hành chính DN (Slide)`, 2.4 MB, tạo 08/05/2026) ⇒ **3 bản ghi Slide** | Không |
| Dữ liệu tiền đề — **định dạng tệp bài giảng** | Tệp **`.pptx`** thật (đối tác dùng `10.2. Tia, đoạn thẳng.pptx`, 2.2 MB) | (1) `QLKTLBG_09-v2-slide-that.pptx` — PowerPoint thật 2 slide, chữ đọc được, 28.5 KB, md5 `86b20236…`; (2) **tệp phức tạp** `QLKTLBG_09-v2-slide-phuc-tap.pptx` — 3 slide gồm bullet có dấu tiếng Việt, **ảnh nhúng**, **bảng 3×3**, 30.1 KB. Cả hai upload qua form `Thêm mới` với `Loại tài liệu = Slide` (form chỉ nhận `.pptx`) | Không |
| Input / filter | Không đặt bộ lọc; bản ghi đích nằm đầu danh sách | Giữ `Bộ lọc nâng cao (2)` mặc định, các ô lọc để trống; bản ghi đích nằm đầu danh sách | Không |

## Đã cố BÁC BỎ kết luận Pass bằng những cách sau — không bác được

1. **Không tin bản dựng cũ:** vòng trước chạy trên gói giao diện khác và dữ liệu khác; đã dựng lại toàn bộ tiền đề trên bản dựng hiện tại thay vì đọc lại kết quả cũ.
2. **Ép tệp khó:** ngoài tệp 2 slide đơn giản, seed thêm tệp `.pptx` **phức tạp** (ảnh nhúng + bảng + tiếng Việt có dấu + ký tự đặc biệt `& < > " '`). Khung xem trước dựng đủ **3/3 slide**, đọc được nguyên văn mọi chuỗi neo (`NEO-CPX-4471/4472/4473`), ảnh nhúng hiện đúng, bảng 3×3 ra đủ 9 ô.
3. **Không dừng ở "thấy nút":** bấm THẬT nút `Tải về` trong hộp thoại → tệp về máy 29.207 byte, mở lại bằng `python-pptx` ra đúng 2 slide với đúng chữ, **md5 `86b202364c7349557984b21e8bc9445d` trùng khít** tệp đã tải lên.
4. **Truy nhánh fallback của đặc tả** (SCR-III-03 §Thành phần 6, `srs-fr-03-dao-tao.md:1955`): mở bản ghi Slide cũ có tệp không đọc được → hộp thoại hiện đúng **"Không thể xem trực tuyến định dạng này" + nút "Tải về"** (ảnh `QLKTLBG_09-v2-05-fallback-khong-the-xem-truc-tuyen.png`). Nhánh này trước đây KHÔNG có.
5. **Quét toàn bảng cột `Thao tác`** (`srs-fr-03-dao-tao.md:1951`): 15/15 dòng — mọi dòng Slide/PDF đều có nút `Tải về`, mọi dòng Video đều KHÔNG có ⇒ đúng phạm vi "chỉ Slide/PDF".
6. **Nghi ngờ "lỗi im lặng":** bản ghi Slide cũ (tệp không còn trên máy chủ) khi bấm `Tải về` thoạt nhìn không phản hồi gì. Cài `tools/toast-capture.js` (tự kiểm `soObserverDangSong = 1`) rồi bấm lại → bắt được **đúng 1 thông báo "Không tải được tệp bài giảng."**, không lặp ⇒ không phải lỗi im lặng, chỉ là đọc DOM sau khi thông báo đã tự tắt.
7. **Kiểm đúng phản ánh gốc "hệ thống tự tải tệp xuống":** sau khi bấm xem trước, thư mục tải về **không** phát sinh tệp nào; tệp chỉ xuất hiện khi chủ động bấm `Tải về`.

## Ghi chú phương pháp

- Bộ bắt thông báo cài **trước** mỗi thao tác đổi trạng thái, tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.
- Lượt seed 1: **3 request ghi** (`upload-file`, `upload-anh`, `bai-giangs`) ↔ **3 thông báo** khác nhau, không lặp.
- Lượt seed 2: **2 request ghi** ↔ **2 thông báo**, không lặp.
- Ảnh chụp đã **mở ra đọc từng tấm**, không chỉ lưu.

**Kết luận: 0 GAP** — đã tái lập đúng vai trò, đúng màn, đúng loại tài liệu, đúng định dạng tệp và đúng trạng thái công khai của bug gốc; đã cố bác bằng 7 hướng ở trên mà lỗi không tái hiện ⇒ `Pass`.
