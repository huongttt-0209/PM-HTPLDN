# Số liệu đo — Reverify round 7 (2026-07-25)

Tài khoản: `cbnv_tw_04` (CB Nghiệp vụ Trung ương) · Web `https://18.143.165.120.nip.io` · Chrome DevTools MCP.

---

## TKBMHD_03 (dòng 113) — Danh sách biểu mẫu `/bieu-mau/danh-sach`

**Verdict: Pass** — ghi sheet 2026-07-25 12:24:00.

### Bước 1 — 4 ô lọc lúc mới mở màn (URL sạch `/bieu-mau/danh-sach`, chưa bấm gì)

Ô đối chiếu chuẩn = ô "20 / trang" ở phân trang (chắc chắn CÓ giá trị).

| Ô lọc | class node chứa giá trị | `title` | màu chữ (computed) | Kết luận |
|---|---|---|---|---|
| Thư mục | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| Lĩnh vực | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| Loại hình | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| Định dạng | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| **(đối chiếu) 20 / trang** | `ant-select-content ant-select-content-has-value` | `20 / trang` | `rgb(31, 31, 31)` | mốc "đã chọn" |

- KHÔNG còn node `ant-select-selection-placeholder` / `ant-select-placeholder` trên cả 4 ô (`hasPlaceholderFlag=false`).
- Màu chữ mờ placeholder tham chiếu lượt trước là `rgb(191, 191, 191)` — round này KHÔNG xuất hiện.
- Tổng bản ghi lúc mở màn: **`Hiển thị 1-14 / 14 kết quả`**, 14 dòng bảng. (Lượt trước 11 — chênh do QA seed thêm 3 biểu mẫu ở case khác.)

### Bước 2 — nội dung 4 dropdown (đã cuộn hết, đối chiếu `scrollHeight` vs `clientHeight`)

| Dropdown | Số mục | Mục đầu | "Tất cả" có `ant-select-item-option-selected` | scrollHeight/clientHeight | Có mục ẩn? |
|---|---|---|---|---|---|
| Thư mục | 10 | Tất cả | ✅ true | 320 / 256 (10×32) | không |
| Lĩnh vực | 11 (Tất cả + 10 lĩnh vực) | Tất cả | ✅ true | 352 / 256 (11×32) | không — cuộn hết thấy đủ, "Đầu tư" là mục cuối |
| Loại hình | 5 (Tất cả, Hợp đồng, Biểu mẫu, Mẫu đơn, Khác) | Tất cả | ✅ true | 160 / 160 | không |
| **Định dạng** | **5 — Tất cả, DOC, DOCX, XLS, XLSX** | Tất cả | ✅ true | 160 / 160 | không |

- Ô Định dạng: `coPDF = false` — **không còn mục PDF** (ý (b) vẫn giữ đạt).

### Bước 3–4 — lọc chạy đúng

| Thao tác | URL sau thao tác | Kết quả |
|---|---|---|
| Mở màn (URL sạch) | `/bieu-mau/danh-sach` | 14 / 14 |
| Định dạng = DOCX + bấm [Tìm kiếm] | `?dinhDang=DOCX&page=1` | **12 / 12**, cả 12 dòng cột "Loại TL" đều icon `file-word` |
| Chọn lại Định dạng = Tất cả + [Tìm kiếm] | `?page=1` | **14 / 14** — trở về đúng tổng bước 1 |

- Lưu ý thao tác: bộ lọc KHÔNG tự áp dụng khi chọn; phải bấm nút **[Tìm kiếm]** (màn có sẵn nút này) — không phải lỗi, chỉ là cách vận hành của màn.
- Cross-check giá trị `selected`: khi đang chọn DOCX, mở lại dropdown thì `DOCX selected=true` và `Tất cả selected=false` → cờ `ant-select-item-option-selected` phản ánh lựa chọn thật, nên "Tất cả selected=true" lúc mở màn là lựa chọn thật chứ không phải highlight mặc định.

### Phương pháp thứ hai (xác nhận lại)

Tải lại cứng URL sạch `https://18.143.165.120.nip.io/bieu-mau/danh-sach` (`navigate_page`, không qua click sidebar) → đo lại: cả 4 ô vẫn `ant-select-content-has-value`, `title="Tất cả"`, `rgb(31,31,31)`; 14 / 14. Trùng kết quả lần đo 1.

### Đối chiếu (A) / (B)

| Điều kiện (A) | Kết quả |
|---|---|
| (i) 4 ô hiện "Tất cả" dạng giá trị đã chọn, không phải chữ mờ | ✅ |
| (ii) dropdown Định dạng đúng 5 mục, không có PDF | ✅ |
| (iii) chọn DOCX ra đúng nhóm .docx | ✅ 12/12 icon file-word |
| (iv) chọn lại "Tất cả" trở về đúng tổng bước 1 | ✅ 14 = 14 |

(B) — 3 gạch đầu dòng "CHƯA ĐẠT" của lượt Reopen gần nhất đều KHÔNG tái hiện.

### Ảnh
- `TKBMHD_03/image/r7-01-4-o-loc-luc-moi-mo-man.png`
- `TKBMHD_03/image/r7-02-dropdown-thu-muc-tat-ca-duoc-chon.png`
- `TKBMHD_03/image/r7-03-dropdown-linh-vuc-tat-ca-duoc-chon.png`
- `TKBMHD_03/image/r7-04-dropdown-dinh-dang-5-muc-khong-co-pdf.png`
- `TKBMHD_03/image/r7-05-loc-dinh-dang-docx-12-ket-qua.png`
- `TKBMHD_03/image/r7-06-url-sach-tai-lai-4-o-loc-va-o-doi-chieu-20-trang.png`

---

## TKTMBMHD_04 (dòng 89) — Thư mục biểu mẫu `/bieu-mau/thu-muc`

**Verdict: Pass** — ghi sheet 2026-07-25 12:28:02.

### Bước 1 — 2 ô lọc lúc mới mở màn (URL sạch `/bieu-mau/thu-muc`, chưa bấm gì)

| Ô lọc | class node chứa giá trị | `title` | màu chữ (computed) | Kết luận |
|---|---|---|---|---|
| Lĩnh vực | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| Trạng thái | `ant-select-content ant-select-content-has-value` | `Tất cả` | `rgb(31, 31, 31)` | ✅ giá trị đã chọn |
| **(đối chiếu) 20 / trang** | `ant-select-content ant-select-content-has-value` | `20 / trang` | `rgb(31, 31, 31)` | mốc "đã chọn" |

- Cả 2 ô `hasPlaceholderNode = false` — không còn node chữ gợi ý mờ. Màu mờ tham chiếu lượt trước `rgb(191,191,191)` KHÔNG xuất hiện.
- Tổng thư mục lúc mở màn: **`Hiển thị 1-9 / 9 kết quả`**, 9 dòng bảng. (Lượt trước 4 — chênh do QA seed thêm thư mục ở case khác.)
- Đã tách bạch với dãy tab phía trên bảng (`Tất cả 9 / Đã công khai / Nháp / Đã ẩn`) — tab là control khác, không dùng để chấm case này.

### Bước 2–3 — nội dung 2 dropdown (đã cuộn hết, đối chiếu `scrollHeight` vs `clientHeight`)

| Dropdown | Số mục | Mục đầu | "Tất cả" có `ant-select-item-option-selected` | scrollHeight/clientHeight | Có mục ẩn? |
|---|---|---|---|---|---|
| **Lĩnh vực** | **11 — Tất cả + 10 lĩnh vực** (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư) | **Tất cả** | ✅ true | 352 / 256 (11×32) | không — cuộn hết, số mục đếm được = số hàng tính từ scrollHeight |
| Trạng thái | 4 — Tất cả, Nháp, Đã công khai, Đã ẩn | Tất cả | ✅ true | 128 / 128 | không |

- Lỗi lượt trước "dropdown Lĩnh vực chỉ có 10 lĩnh vực, KHÔNG có mục Tất cả" → **đã hết**: mục "Tất cả" nay đứng trước toàn bộ lĩnh vực.

### Bước 4 — lọc chạy đúng

| Thao tác | URL sau thao tác | Kết quả |
|---|---|---|
| Mở màn (URL sạch) | `/bieu-mau/thu-muc` | 9 / 9 |
| Trạng thái = Nháp + [Tìm kiếm] | `?trangThai=NHAP&page=1` | **3 / 3** — cả 3 dòng cột Trạng thái đều "Nháp" (QA-IMPORT-KQ, QA-CK-RONG, BM-B3-0720-Rong-1) |
| Chọn lại Trạng thái = Tất cả + [Tìm kiếm] | `?page=1` | **9 / 9** — trở về đủ số thư mục lúc mở màn |

- Cross-check giá trị `selected`: khi đang chọn Nháp, mở lại dropdown thì `Nháp selected=true` / `Tất cả selected=false` → cờ phản ánh lựa chọn thật, nên "Tất cả selected=true" lúc mở màn là lựa chọn thật.
- Bộ lọc cũng cần bấm nút **[Tìm kiếm]** mới áp dụng (giống màn Danh sách biểu mẫu).

### Phương pháp thứ hai (xác nhận lại)

Tải lại cứng URL sạch `https://18.143.165.120.nip.io/bieu-mau/thu-muc` → đo lại: cả 2 ô vẫn `ant-select-content-has-value`, `title="Tất cả"`, `rgb(31,31,31)`; 9 / 9. Trùng kết quả lần đo 1.

### Đối chiếu (A) / (B)

| Điều kiện (A) | Kết quả |
|---|---|
| (i) 2 ô hiện "Tất cả" dạng giá trị đã chọn | ✅ |
| (ii) dropdown Trạng thái đúng 4 mục, "Tất cả" đứng đầu | ✅ |
| (iii) dropdown Lĩnh vực có mục "Tất cả" đứng trước toàn bộ lĩnh vực | ✅ |
| (iv) chọn lại "Tất cả" trở về đủ số thư mục lúc mở màn | ✅ 9 = 9 |

(B) — 4 gạch đầu dòng của lượt Reopen gần nhất: 2 gạch "chưa đạt" đã hết, 2 gạch "đã đạt" vẫn giữ.

### Ảnh
- `TKTMBMHD_04/image/r7-01-2-o-loc-luc-moi-mo-man.png`
- `TKTMBMHD_04/image/r7-02-dropdown-linh-vuc-co-muc-tat-ca-dung-dau.png`
- `TKTMBMHD_04/image/r7-03-dropdown-trang-thai-4-muc-tat-ca-duoc-chon.png`
- `TKTMBMHD_04/image/r7-04-loc-trang-thai-nhap-3-ket-qua.png`
- `TKTMBMHD_04/image/r7-05-url-sach-tai-lai-2-o-loc-va-o-doi-chieu-20-trang.png`

---

## QLTMBMHD_20 (dòng 86) — Thao tác hàng loạt trên Thư mục biểu mẫu `/bieu-mau/thu-muc`

**Verdict: Pass** — ghi sheet 2026-07-25 12:40:44.

### Bước 0 — Tiền đề tự dựng (seed)

4 thư mục mới, tiền tố `QA-R7-`, lĩnh vực Thương mại, đơn vị BTP·TW, đều `NHAP` lúc tạo:

| Thư mục | id | Số biểu mẫu | Dùng cho nhánh |
|---|---|---|---|
| `QA-R7-A-CO-BM` | 4ebd9f07-2731-4277-a2ba-3df171d19f58 | 1 (`BM-20260725-001`) | Xóa (bị bỏ qua) → Công khai (thành công) → Ẩn (thành công) |
| `QA-R7-B-RONG` | 84754133-7d24-47c8-a227-f31b0699e081 | 0 | Xóa (thành công) |
| `QA-R7-D-RONG` | 55071ee8-fd34-44d2-8c7a-8feb20d37e21 | 0 | Công khai (bị bỏ qua — rỗng) |
| `QA-R7-E-CO-BM` | 1def14a9-cae4-43d0-bafd-ea6ae183fdcf | 1 (`BM-20260725-002`) | Ẩn (bị bỏ qua — chưa công khai) |

- Biểu mẫu trong A và E dùng tệp `qa-r7-seed.docx` (922 B), upload trả 201, `trangThaiQuet=SACH`.
- E cố tình có biểu mẫu để lý do bỏ qua ở nhánh Ẩn **chỉ có thể là** "chưa công khai" (loại trừ lý do "rỗng").
- Tổng thư mục trước khi đo: **13**. Ảnh: `r7-00-seed-4-thu-muc-qa-r7.png`.

### Bộ bắt thông báo

`tools/toast-capture.js` dán nguyên khối, tự kiểm trước mỗi lô: **`soObserverDangSong = 1`** → số liệu hợp lệ.

### Nhánh 1 — XÓA hàng loạt (A có biểu mẫu + B rỗng)

| Mục | Nguyên văn đo được (`innerText`) |
|---|---|
| Hộp xác nhận — tiêu đề | `Xóa 1 thư mục?` |
| Hộp xác nhận — nội dung | `Hành động này không thể hoàn tác. Bạn có chắc không? (1 thư mục không đủ điều kiện (còn biểu mẫu) sẽ được bỏ qua)` |
| Thông báo kết quả | `Đã xóa 1/2 thư mục. 1 thư mục không đủ điều kiện (còn biểu mẫu).` |
| SO_KHUNG_THONG_BAO | **1** |
| SO_REQUEST | **1** — `DELETE /api/v1/thu-muc-bieu-maus/84754133-…` (đúng id thư mục RỖNG) |

**Trạng thái sau thao tác:** `QA-R7-B-RONG` biến mất khỏi danh sách; `QA-R7-A-CO-BM` **còn nguyên, vẫn 1 biểu mẫu**. Tổng 13 → **12**.
→ ⚠️ Bẫy 2 sạch: thư mục còn biểu mẫu KHÔNG bị xóa nhầm.

### Nhánh 2 — CÔNG KHAI hàng loạt (A có biểu mẫu + D rỗng)

| Mục | Nguyên văn đo được |
|---|---|
| Hộp xác nhận — tiêu đề | `Công khai 1 thư mục?` |
| Hộp xác nhận — nội dung | `Đặt cờ công khai cho các thư mục đủ điều kiện (có biểu mẫu). Cổng PLQG sẽ tự cập nhật ở lượt kéo dữ liệu tiếp theo. (1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu) sẽ được bỏ qua)` |
| Thông báo kết quả | `Đã công khai 1/2 thư mục. 1 thư mục không đủ điều kiện (rỗng, chưa có biểu mẫu).` |
| SO_KHUNG_THONG_BAO | **1** |
| SO_REQUEST | **1** — `POST /api/v1/thu-muc-bieu-maus/batch-cong-khai` |

**Trạng thái sau:** A `NHAP → CONG_KHAI` (UI "Đã công khai", nút hàng đổi thành [Ẩn]); D vẫn `NHAP`.
→ **Điểm CÒN LẠI của lượt trước ĐÃ SỬA:** hộp xác nhận nay nêu số bỏ qua + lý do (lượt trước chỉ có "Công khai 2 thư mục?" + câu chung).

### Nhánh 3 — ẨN hàng loạt (A đã công khai + E chưa công khai, có biểu mẫu)

| Mục | Nguyên văn đo được |
|---|---|
| Hộp xác nhận — tiêu đề | `Ẩn 1 thư mục?` |
| Hộp xác nhận — nội dung | `Gỡ cờ công khai cho các thư mục đủ điều kiện. Cổng PLQG sẽ tự loại khỏi kết quả ở lượt kéo dữ liệu tiếp theo. (1 thư mục không đủ điều kiện (chưa công khai) sẽ được bỏ qua)` |
| Thông báo kết quả | `Đã ẩn 1/2 thư mục. 1 thư mục không đủ điều kiện (chưa công khai).` |
| SO_KHUNG_THONG_BAO | **1** |
| SO_REQUEST | **1** — `POST /api/v1/thu-muc-bieu-maus/batch-an` |

**Trạng thái sau:** A `CONG_KHAI → AN`; E vẫn `NHAP`.
→ **Điểm CÒN LẠI của lượt trước ĐÃ SỬA:** hộp xác nhận nay nêu số bỏ qua + lý do "chưa công khai".

### Phương pháp thứ hai (xác nhận lại)

Đọc lại trạng thái bằng đường dữ liệu (không qua bảng UI) ngay sau lô đo — trùng khớp 100% với những gì bảng hiển thị:

```
QA-R7-E-CO-BM: trangThai=NHAP,      soBieuMau=1
QA-R7-D-RONG : trangThai=NHAP,      soBieuMau=0
QA-R7-A-CO-BM: trangThai=AN,        soBieuMau=1
tổng thư mục = 12   (QA-R7-B-RONG đã bị xóa)
```

### Đối chiếu (A) / (B)

| Điều kiện (A) | Kết quả |
|---|---|
| (i) CẢ hộp xác nhận LẪN thông báo kết quả nêu số xử lý được + số bỏ qua + lý do — cho cả 3 nhánh | ✅ 3/3 nhánh |
| (ii) không còn chữ "thất bại" gán cho thư mục bị bỏ qua; dùng "không đủ điều kiện" | ✅ cả 6 chuỗi đo được đều dùng "không đủ điều kiện", 0 lần xuất hiện "thất bại" |
| (iii) đếm đúng — xóa 1/2 (còn biểu mẫu), công khai 1/2 (rỗng, chưa có biểu mẫu), ẩn 1/2 (chưa công khai) | ✅ đúng cả 3, không có "0/2" |

(B) — 6 gạch đầu dòng lượt Reopen gần nhất: 2 gạch "còn thiếu" (hộp xác nhận Công khai và Ẩn) **KHÔNG còn tái hiện**; 4 gạch "đã đạt" vẫn giữ nguyên.

⚠️ Bẫy 1 (dòng đã tích + thanh hành động hàng loạt còn sót) — thuộc QLTMBMHD_19, KHÔNG dùng để chấm case này. Quan sát được ghi riêng ở `phat-hien-them.md`.

### Ảnh
- `QLTMBMHD_20/image/r7-00-seed-4-thu-muc-qa-r7.png`
- `QLTMBMHD_20/image/r7-01-xoa-hop-xac-nhan.png`
- `QLTMBMHD_20/image/r7-02-xoa-sau-thao-tac-con-12-thu-muc.png`
- `QLTMBMHD_20/image/r7-03-cong-khai-hop-xac-nhan.png`
- `QLTMBMHD_20/image/r7-04-cong-khai-sau-thao-tac-a-da-cong-khai-d-van-nhap.png`
- `QLTMBMHD_20/image/r7-05-an-hop-xac-nhan.png`
- `QLTMBMHD_20/image/r7-06-an-sau-thao-tac-a-da-an-e-van-nhap.png`

---

## QLBMHD_13 (dòng 106) — Form Sửa biểu mẫu `/bieu-mau/danh-sach` → Sửa

**Verdict: Pass** — ghi sheet 2026-07-25 12:53:06.

### Bước 0 — Tiền đề tự dựng (⚠️ Bẫy 2: bản ghi MỚI qua luồng chuẩn)

Tạo biểu mẫu mới **qua giao diện `/bieu-mau/them-moi`** (không tạo bằng đường dữ liệu) để loại trừ khả năng bản ghi cũ có dữ liệu tệp đóng băng từ trước khi dev sửa:

| Trường | Giá trị |
|---|---|
| Mã biểu mẫu | **BM-20260725-003** |
| Tên | `QA-R7-SUA-BM-goc` |
| Thư mục | Thư mục biểu mẫu seed |
| Tệp đính kèm | **`qa-edit-src.docx`** — **931 B**, DOCX |

- Ảnh: `r7-00-seed-form-them-moi-da-chon-tep.png`.
- Ghi chú lúc seed: lần bấm [Thêm mới] đầu tiên chọn thư mục `QA-IMPORT-KQ` bị máy chủ từ chối (`ERR-BM-05` — "Thư mục biểu mẫu không tồn tại hoặc không thuộc đơn vị") vì thư mục đó thuộc đơn vị khác nhưng vẫn nằm trong danh sách chọn. Đổi sang thư mục cùng đơn vị thì tạo được. Chi tiết ở `phat-hien-them.md` mục 4.

### Bước 1–2 — Vùng "File biểu mẫu" trên form Sửa (đo bằng `evaluate_script`, `innerText`)

Toàn bộ chữ hiển thị trong vùng:

```
File biểu mẫu
Kéo thả hoặc click để chọn file
Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB
qa-edit-src.docx
Để trống nếu muốn giữ nguyên tệp đang đính kèm (qa-edit-src.docx). Chỉ chọn tệp mới khi cần thay thế.
```

Liệt kê phần tử tương tác trong vùng:

| Loại | Số lượng | Chi tiết |
|---|---|---|
| `a[href]` | **1** | chữ `qa-edit-src.docx` · `href="/api/v1/bieu-maus/339d8d21-…/download"` · `target="_blank"` → **tên tệp bấm được** |
| `button` | **2** | ① `title="Tải tập tin"` (icon `download`) ② `title="Gỡ bỏ tập tin"` (icon `delete`) |
| phần tử có `onclick` | 7 | gồm cả thẻ `<a>` tên tệp và 2 nút trên |

- Nhãn "File biểu mẫu" trên form Sửa **KHÔNG còn dấu `*` bắt buộc** (`BAT_BUOC_co_dau_sao = false`) — khác form Thêm mới (vẫn có `*`).
- 2 nút hành động là kiểu chỉ hiện khi rê chuột (`ant-upload-list-item-action`) — ảnh `r7-02` chụp lúc rê chuột cho thấy rõ icon tải xuống và icon thùng rác.
- → **Cả 2 gạch "Còn thiếu" của lượt Reopen gần nhất đều KHÔNG còn tái hiện.**

### Bước 3 — Sửa Tên biểu mẫu, KHÔNG chọn lại tệp, bấm Lưu

| Mục | Kết quả |
|---|---|
| Tên mới | `QA-R7-SUA-BM-goc - r1` |
| Thông báo | **`Cập nhật biểu mẫu thành công`** |
| SO_KHUNG_THONG_BAO | **1** |
| SO_REQUEST | **1** — `PATCH /api/v1/bieu-maus/339d8d21-…` |
| Lỗi "bắt buộc" ở ô File biểu mẫu | **không có** (mảng `.ant-form-item-explain-error` rỗng) |

### Bước 4 — Tệp đính kèm sau khi lưu

| Mục | Tệp gốc lúc seed | Sau khi lưu |
|---|---|---|
| Tên tệp | `qa-edit-src.docx` | **`qa-edit-src.docx`** |
| Kích thước | 931 B | **931 B** (màn Chi tiết hiện "Kích thước 931 B") |
| Định dạng | DOCX | DOCX |

**Tải tệp về THẬT (phương pháp thứ hai):** lấy đúng địa chỉ tệp mà máy chủ trả cho nút tải rồi tải trực tiếp → `HTTP 200`, `931 byte`, `content-type` đúng kiểu .docx. So khớp với tệp gốc:

```
SHA-256 tệp tải về : b815f21d7535e595c69e309e4d840e5b32acb4379057ef37cc83a25d44be4505
SHA-256 tệp gốc    : b815f21d7535e595c69e309e4d840e5b32acb4379057ef37cc83a25d44be4505   → TRÙNG KHỚP
```

→ Lưu mà không chọn lại tệp: tệp cũ được giữ **nguyên vẹn từng byte**.

### Quan sát thêm về thao tác tải tệp (KHÔNG dùng để chấm case này)

Bấm nút tải **ngay trên form Sửa**: yêu cầu CÓ tới máy chủ (số lượt tải của bản ghi tăng), nhưng tệp **không về máy** — trình duyệt chặn vì trang chạy `https` còn máy chủ chuyển hướng sang địa chỉ kho tệp dùng `http` (lỗi Mixed Content trong console).

Kiểm chéo 2 chỗ tải khác cùng bản ghi:

| Chỗ bấm tải | Máy chủ có được gọi? (số lượt tải) | Tệp có về máy? |
|---|---|---|
| Nút tải trên form Sửa | ✅ 1 → 2 | ❌ |
| [Tải về] màn Chi tiết | ✅ 2 → 3 | ❌ |
| [Tải về] trên dòng Danh sách | ✅ 3 → 4 | ❌ |

→ Hỏng **giống hệt nhau ở cả 3 chỗ** ⇒ là vấn đề chung của môi trường triển khai (kho tệp phục vụ qua `http` trong khi ứng dụng chạy `https`), **không phải lỗi riêng của form Sửa** và không nằm trong (A) hay (B) của case này. Ghi ở `phat-hien-them.md` mục 3 để đội dự án xử lý riêng.

### Đối chiếu (A) / (B)

| Điều kiện (A) | Kết quả |
|---|---|
| (i) form Sửa hiện tên tệp đang đính kèm VÀ có lối tải tệp đó ngay trên form | ✅ tên tệp là liên kết bấm được + có nút riêng "Tải tập tin" (trước đây 0 phần tử tệp, 0 liên kết tải) |
| (ii) form nêu rõ để trống ô tải = giữ tệp hiện tại; ô File không báo lỗi bắt buộc khi không tải lại | ✅ có câu "Để trống nếu muốn giữ nguyên tệp đang đính kèm (qa-edit-src.docx)…" + nhãn bỏ dấu `*` + lưu không báo lỗi |
| (iii) lưu được; tệp đính kèm vẫn đúng tệp cũ, tên và kích thước không đổi | ✅ "Cập nhật biểu mẫu thành công"; `qa-edit-src.docx` / 931 B; SHA-256 trùng tệp gốc |

3 điều kiện ❌ FAIL của bar gốc — **không điều nào xảy ra**: form Sửa không còn "chỉ có ô tải trống"; lưu không bị chặn vì báo bắt buộc; tệp sau khi lưu không mất/rỗng.

(B) — 5 gạch đầu dòng lượt Reopen gần nhất: 2 gạch "Còn thiếu" **KHÔNG còn tái hiện**; 3 gạch "đã đạt" vẫn giữ nguyên.

### Ảnh
- `QLBMHD_13/image/r7-00-seed-form-them-moi-da-chon-tep.png`
- `QLBMHD_13/image/r7-01-form-sua-vung-file-co-nut-tai-va-cau-giai-thich.png`
- `QLBMHD_13/image/r7-02-form-sua-hien-nut-tai-tap-tin-khi-ro-chuot.png`
- `QLBMHD_13/image/r7-03-danh-sach-sau-khi-luu-ten-bieu-mau-da-doi.png`
- `QLBMHD_13/image/r7-04-chi-tiet-sau-khi-luu-931B-docx-giu-nguyen.png`

---

## QLBMHD_08 (dòng 101) — Chặn tệp chứa mã độc `/bieu-mau/them-moi`

**Verdict: Pass** — ghi sheet 2026-07-25 12:58:57.

> Chấm theo **quyết định đã chốt với user** (BRIEF §4): hạng mục "bộ quét chạy TRƯỚC khi ghi tệp vào kho" là chi tiết triển khai nội bộ, kiểm thử hộp đen không quan sát được → KHÔNG dùng để giữ Reopen. Chỉ chấm 3 điều quan sát được: (i) tệp bị từ chối · (ii) thông báo đúng nội dung ERR-BM-07 · (iii) không tạo được bản ghi.

### Bộ bắt thông báo
`tools/toast-capture.js` dán nguyên khối; tự kiểm trước lô đo: **`soObserverDangSong = 1`**.

### Bước 1 — `eicar.docx` (chuỗi EICAR thô đổi đuôi, 68 B)

| Mục | Kết quả |
|---|---|
| Mã trả về `POST /api/v1/bieu-maus/upload` | **HTTP 400** |
| Mã lỗi trong nội dung trả về | **`ERR-BM-07`** |
| Nguyên văn thông báo (toast) | **`Tệp chứa mã độc, không thể lưu trữ`** |
| SO_KHUNG_THONG_BAO / SO_REQUEST | **1 / 1** |
| Dòng tệp trên form | `eicar.docx` — class `ant-upload-list-item-error`, chữ ĐỎ, **không được đính kèm** |

→ Khác lượt đo 20/07/2026: trước đây tệp này bị chặn ở bước kiểm **ĐỊNH DẠNG** ("Nội dung file không khớp định dạng…"), nay bị chặn với đúng lý do **mã độc**.

### Bước 2 — `valid-eicar.docx` (**phép thử quyết định**, .docx đúng cấu trúc Office, EICAR nằm trong `word/document.xml`, 1028 B)

| Mục | Kết quả |
|---|---|
| Mã trả về `POST /api/v1/bieu-maus/upload` | **HTTP 400** (lượt 20/07 là **201** — máy chủ NHẬN tệp) |
| Nội dung trả về nguyên văn | `{"success":false,"error":{"code":"ERR-BM-07","message":"Tệp chứa mã độc, không thể lưu trữ",…}}` |
| Nguyên văn thông báo (toast) | **`Tệp chứa mã độc, không thể lưu trữ`** |
| SO_KHUNG_THONG_BAO / SO_REQUEST | **1 / 1** (không lặp khung, không gửi 2 lần) |
| Dòng tệp trên form | `valid-eicar.docx` — trạng thái lỗi (`ant-upload-list-item-error`), `ant-upload-list-item-done` = **false** → **không đính kèm được** |

→ ⚠️ Bẫy 1 đã xử lý đúng: **không** kết luận từ bước 1; phép thử quyết định (bước 2) cho kết quả CHẶN.

### Bước 3 — Vẫn cố tạo bản ghi

Điền Thư mục `Thư mục biểu mẫu seed` + Tên `QA-eicar-r7-row101` rồi bấm **[Thêm mới]**:

| Mục | Kết quả |
|---|---|
| Thông báo | **`Vui lòng upload file biểu mẫu`** |
| SO_KHUNG_THONG_BAO | **1** |
| SO_REQUEST | **0** — **không có** lệnh `POST /api/v1/bieu-maus` nào được gửi |
| URL sau khi bấm | vẫn ở `/bieu-mau/them-moi` (không chuyển trang) |

### Bước 4 — Kiểm tra danh sách biểu mẫu

| Mục | Kết quả |
|---|---|
| Tổng bản ghi trước lô đo mã độc | **17** (`Hiển thị 1-17 / 17 kết quả`) |
| Tổng bản ghi sau lô đo mã độc | **17** — KHÔNG đổi |
| Tìm từ khóa `eicar` (đã bấm [Tìm kiếm], URL `?keyword=eicar&page=1`) | **`Hiển thị 1-1 / 1 kết quả`** |
| Bản ghi duy nhất khớp | `BM-20260720-006 · QA-eicar-malware-test-row101` — **ngày tạo 2026-07-20**, tồn dư từ lượt đo trước (khi bộ quét chưa chặn) |
| Bản ghi tên `QA-eicar-r7-row101` | **0** |
| Bản ghi tạo ngày 25/07 | đúng 3 bản, đều của case khác: `BM-20260725-001/002/003` — **không bản nào sinh từ lô đo mã độc** |

### Đối chiếu 3 điều kiện đã chốt

| Điều kiện | Kết quả |
|---|---|
| (i) `valid-eicar.docx` bị TỪ CHỐI — yêu cầu tải lên không trả mã thành công, tệp không được đính kèm | ✅ HTTP 400, dòng tệp trạng thái lỗi, không đính kèm |
| (ii) Thông báo nói rõ tệp chứa mã độc, đúng chuỗi ERR-BM-07 "Tệp chứa mã độc, không thể lưu trữ" — không phải chuỗi chung chung | ✅ đúng nguyên văn, cả ở toast lẫn nội dung máy chủ trả về; KHÔNG còn "Upload file thất bại. Vui lòng thử lại." |
| (iii) Không bản ghi biểu mẫu nào được tạo | ✅ tổng 17 → 17; `QA-eicar-r7-row101` = 0 bản ghi |

Đạt cả 3 → **Pass**.

(B) — 6 gạch đầu dòng lượt Reopen gần nhất: 5 gạch mô tả trạng thái ĐÃ ĐẠT đều tái lập đúng; gạch cuối (chờ Dev/An toàn thông tin xác nhận bộ quét chạy trước khi ghi tệp) đã được user quyết bỏ khỏi bar chấm.

### Ảnh
- `QLBMHD_08/image/r7-01-eicar-docx-dong-tep-bao-loi-khong-dinh-kem.png`
- `QLBMHD_08/image/r7-02-valid-eicar-docx-dong-tep-bao-loi-khong-dinh-kem.png`
- `QLBMHD_08/image/r7-03-bam-them-moi-bi-chan-van-o-lai-form.png`
- `QLBMHD_08/image/r7-04-tim-eicar-chi-con-ban-ghi-cu-20-07-khong-co-r7-row101.png`

---

## IBMHD_07 (dòng 119) — Nhập biểu mẫu hàng loạt, màn kết quả `/bieu-mau/nhap-hang-loat`

Tài khoản `cbnv_bn_04` (CB Nghiệp vụ - Bộ ngành #04, `CB_NV_BN`, đơn vị `...-8001-...0001`). Đo 25/07/2026 ~13:05–13:14.

### Bước 0 — Tiền đề tự dựng (seed)

| Việc | Kết quả |
|---|---|
| Tạo thư mục đích mới, RỖNG | `QA-IMPORT-R7` · Lĩnh vực Thuế · id `a2fa2704-39b8-46a9-9c26-d815e8184a70` |
| Trạng thái lúc tạo | **0 biểu mẫu**, Nháp — ảnh `00-seed-thu-muc-QA-IMPORT-R7.png` |
| Bộ bắt thông báo khi tạo | `soObserverDangSong = 1` · SO_REQUEST 1 (`POST /api/v1/thu-muc-bieu-maus`) · SO_KHUNG 1 (`Tạo thư mục thành công`) |
| 4 tệp fixture | `qa-ok-1.docx` 922 B · `qa-ok-2.docx` 922 B · `qa-loi.txt` 48 B · `qa-hong.docx` 3010 B |

Không nhầm với thư mục lượt trước: `QA-IMPORT-KQ` (2 biểu mẫu, tạo 25/07 lúc 03:01) là của lượt đo cũ, giữ nguyên.

### Bước 1 — Chọn tệp (dòng đếm) — nguyên văn

```
Thư mục đích: QA-IMPORT-R7
qa-ok-1.docx
qa-ok-2.docx
qa-hong.docx          ← chữ đỏ
Đã tải lên thành công: 2/3 · Có file lỗi
```

| Chỉ số | Giá trị |
|---|---|
| `soObserverDangSong` (tự kiểm trước khi tin số liệu) | **1** ✅ |
| Khi tải `qa-ok-1` + `qa-ok-2` | SO_REQUEST 2 (`POST /api/v1/bieu-maus/upload` → **201** ×2) · SO_KHUNG **0** |
| Khi tải `qa-hong.docx` | SO_REQUEST **1** (`POST /api/v1/bieu-maus/upload` → **400**) · SO_KHUNG **1** · chữ: `Tệp không hợp lệ hoặc bị hỏng` · không lặp |
| `qa-loi.txt` | KHÔNG hiện trong danh sách tệp, KHÔNG có thông báo, KHÔNG có request — dòng đếm vẫn ghi mẫu số **3** (xem §8 phát hiện thêm) |

### Bước 2 — Kiểm tra (bảng) — nguyên văn

```
Tổng số file 4 | Hợp lệ 2 | Lỗi 2
Có 2 tệp lỗi sẽ bị bỏ qua khi nhập. Xem chi tiết trong bảng bên dưới.
Chi tiết file
STT  Tên file        Định dạng  Kích thước  Trạng thái  Lý do / Ghi chú
1    qa-ok-1.docx    DOCX       922 B       Hợp lệ      —
2    qa-ok-2.docx    DOCX       922 B       Hợp lệ      —
3    qa-loi.txt      TXT        48 B        Lỗi         Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx)
4    qa-hong.docx    DOCX       2.9 KB      Lỗi         Tệp không hợp lệ hoặc bị hỏng
```

→ Khác lượt trước: `qa-hong.docx` **NAY ĐÃ CÓ dòng** trong bảng Kiểm tra (lượt Reopen trước ghi nhận thiếu). `qa-loi.txt` vẫn được liệt kê kèm lý do.

### Bước 3 — Xác nhận nhập → màn Kết quả — nguyên văn TOÀN MÀN

```
Nhập biểu mẫu hoàn tất: 2 thành công / 2 lỗi
2 tệp lỗi: xem chi tiết bên dưới.
Quay lại danh sách   Nhập tiếp
Chi tiết 2 tệp lỗi
STT  Tên biểu mẫu / tệp  Giai đoạn  Lý do lỗi
1    qa-loi.txt          Chọn tệp   Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx)
2    qa-hong.docx        Tải lên    Tệp không hợp lệ hoặc bị hỏng
```

Nhãn nút đã bấm: `Xác nhận nhập 2 file hợp lệ`. SO_REQUEST **1** (`POST /api/v1/bieu-maus/import/confirm` → 200) · SO_KHUNG **0**.

**Liệt kê mọi phần tử bấm được trên màn Kết quả** (`evaluate_script`, `innerText` — KHÔNG dùng `textContent`): tổng **4** phần tử — `button "Quay lại danh sách"`, `button "Nhập tiếp"`, và 2 nút phân trang `.ant-pagination-item-link` của chính bảng chi tiết. Bảng chi tiết **hiện sẵn ngay trên màn**, không cần bấm để mở.

### Đối chiếu con số máy chủ trả về vs con số giao diện hiển thị

| Nguồn | Nội dung |
|---|---|
| `POST /import/validate` → 200 | gửi lên chỉ 2 `fileIds` (2 tệp tải lên thành công); trả `summary {total:2, valid:2, invalid:0}`, `invalidFiles: []` |
| `POST /import/confirm` → 200 | trả `{imported: 2, failed: 0}` + 2 bản ghi `BM-20260725-004` (Qa-ok-1), `BM-20260725-005` (Qa-ok-2) |
| Giao diện màn Kết quả | `2 thành công / **2 lỗi**` + bảng 2 dòng kèm cột **Giai đoạn** (`Chọn tệp` / `Tải lên`) |

→ Máy chủ chỉ đếm phần nó xử lý (2 tệp hợp lệ, 0 lỗi lúc ghi). **Giao diện tự gộp thêm 2 tệp bị loại sớm** (1 loại lúc chọn tệp, 1 loại lúc tải lên) vào số tệp lỗi — đúng yêu cầu "gộp cả tệp bị loại từ bước chọn tệp lẫn tệp phát sinh lỗi khi đang ghi". Không phải lỗi hiển thị.

### Bước 4 — Đếm biểu mẫu trong thư mục đích

Mở `/bieu-mau/danh-sach`, chọn bộ lọc Thư mục = `QA-IMPORT-R7`, **bấm [Tìm kiếm]** (bộ lọc không tự áp dụng — xem §1).

| Cách đo | Kết quả |
|---|---|
| Giao diện sau khi bấm [Tìm kiếm] | `Hiển thị 1-2 / 2 kết quả` — `BM-20260725-004` (Qa-ok-1) · `BM-20260725-005` (Qa-ok-2) |
| Phương pháp thứ hai (đọc lại dữ liệu cùng phiên) | danh sách biểu mẫu lọc theo thư mục = **2**; ô "Số biểu mẫu" của thư mục = **2** |

### Đối chiếu (A) / (B)

| Điều kiện PASS (A) | Kết quả |
|---|---|
| (i) Màn kết quả nêu CẢ HAI con số — thành công VÀ lỗi | ✅ `Nhập biểu mẫu hoàn tất: 2 thành công / 2 lỗi` |
| (ii) Có lối xem chi tiết + bảng liệt kê từng tệp lỗi kèm tên tệp và lý do, **trong đó có `qa-loi.txt`** | ✅ bảng `Chi tiết 2 tệp lỗi` hiện sẵn trên màn, có `qa-loi.txt` kèm lý do + cột Giai đoạn |
| (iii) Đếm đúng 2 biểu mẫu trong thư mục đích — tệp hợp lệ vẫn được nhập, không chặn cả lô | ✅ đúng 2, xác nhận bằng 2 cách đo |

| Gạch (B) lượt Reopen trước | Kết quả |
|---|---|
| Phần ĐÃ ĐẠT: 2 tệp hợp lệ vẫn được nhập, đếm đúng 2 | ✅ tái lập đúng |
| Còn lỗi 1: màn kết quả ghi `2 thành công / 0 lỗi`, báo 0 lỗi dù mất 2 tệp | ✅ **ĐÃ HẾT** — nay ghi `2 thành công / 2 lỗi` |
| Còn lỗi 2: màn kết quả không có lối xem chi tiết tệp lỗi, chỉ có 2 nút | ✅ **ĐÃ HẾT** — nay có bảng `Chi tiết 2 tệp lỗi` (tên tệp + giai đoạn + lý do) |
| Ghi nhận thêm: bảng bước Kiểm tra thiếu dòng `qa-hong.docx` | ✅ **ĐÃ HẾT** — nay có đủ 4 dòng |

Đạt cả (A) và (B) → **Pass**.

### Ảnh
- `IBMHD_07/image/00-seed-thu-muc-QA-IMPORT-R7.png`
- `IBMHD_07/image/01-buoc-chon-tep-dong-dem.png`
- `IBMHD_07/image/02-buoc-kiem-tra-bang-chi-tiet.png`
- `IBMHD_07/image/03-man-ket-qua-2-thanh-cong-2-loi.png`
- `IBMHD_07/image/04-man-ket-qua-bang-chi-tiet-2-tep-loi.png`
- `IBMHD_07/image/05-dem-2-bieu-mau-trong-QA-IMPORT-R7.png`

---

## QLHSDNHTCP_03 (dòng 16) — mức cảnh báo thời hạn màn DANH SÁCH `/chi-tra/danh-sach`

**Verdict: Reopen** — ghi sheet 2026-07-25 13:41 (GMT+7). Tài khoản `cbnv_tw_04` (CB Nghiệp vụ Trung ương, TW).

Hôm nay thứ Bảy 25/07/2026. Đã xác nhận qua UI (`/api/v1/ngay-le?nam=2026`, HTTP 200): 2026 chỉ có 4 ngày lễ (01/01, 30/04, 01/05, +1), **tháng 6-7/2026 không có ngày lễ** → NLV = trừ T7/CN. Chuẩn: hạn = ngày nộp + 10 NLV, mốc đếm = ngày nộp.

Danh sách nay có **12 hồ sơ** (10 CT-SEED cũ + CT-QAW7-CLOSED + CT-QAW7-OVERDUE). Cột "SLA" hiện nhãn mức + số ngày + tooltip `N% thời hạn đã dùng`. Đọc nguyên văn `title` từng ô SLA bằng evaluate_script.

### Bảng đo (đọc trực tiếp trên UI — nhãn, tooltip %)

| Mã HS | Ngày nộp | Hạn (10 NLV) | NLV đã dùng tới 25/07 | % đúng | % app (tooltip) | Mức đúng | App hiển thị | KQ |
|---|---|---|---|---|---|---|---|---|
| CT-SEED-101 | 15/07 | 29/07 | 7 | 70% | **101%** | Sắp hết hạn | Quá hạn · 0 ngày LV | ❌ |
| CT-SEED-102 | 10/07 | 24/07 | 10 | 100% | 167% | Quá hạn (biên) | Quá hạn · 4 ngày LV | ✅ nhãn |
| CT-SEED-103 | 05/07 | 17/07 | 15 | 150% | **188%** | Quá hạn | Quá hạn · 7 ngày LV | ❌ (% sai) |
| CT-SEED-104 | 08/07 | 22/07 | 12 | 120% | 171% | Quá hạn | Quá hạn · 5 ngày LV | ✅ nhãn |
| CT-SEED-105 | 03/07 | 17/07 | 15 | 150% | **250%** | Quá hạn | **Quá hạn nghiêm trọng · 9 ngày LV** | ❌ |
| CT-SEED-106 | 01/07 | 15/07 | 17 | 170% | **243%** | Quá hạn | **Quá hạn nghiêm trọng · 10 ngày LV** | ❌ |
| CT-SEED-107 | 25/06 | 09/07 | 21 | 210% | 350% | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 15 ngày LV | ✅ nhãn (% sai) |
| CT-SEED-108 | 15/06 | 29/06 | — (thanh toán 24/06, đúng hạn) | — | — | không quá hạn | **Đã hoàn thành** (xám) | ✅ đã sửa |
| CT-SEED-109 | 20/06 | 03/07 | — (từ chối 27/06, trong hạn) | — | — | không quá hạn | **Đã hoàn thành** (xám) | ✅ đã sửa |
| CT-SEED-110 | 12/06 | 26/06 | — (đã hủy) | — | — | không quá hạn | **Đã hoàn thành** (xám) | ✅ đã sửa |
| CT-QAW7-CLOSED | 01/06 | — | — (đã thanh toán) | — | — | không quá hạn | Đã hoàn thành (xám) | ✅ |
| CT-QAW7-OVERDUE | 04/05 | — | — | — | — | Quá hạn nghiêm trọng | Quá hạn nghiêm trọng · 44 ngày LV | ✅ nhãn |

Tooltip % của 101/102/103/104/105/106/107 **trùng KHÍT với lượt round-3** (101/167/188/250/243/350) → công thức SLA KHÔNG đổi. Gốc lỗi vẫn là: hạn (deadlineSla) = ngày nộp + 10 ngày **lịch**, không trừ T7/CN → mẫu số thời lượng chỉ còn 6-8 NLV → % đội lên → nhảy mức sớm.

### Đối chiếu (A) / (B)

| Điều kiện | Kết quả |
|---|---|
| (A) Cột SLA hiện nhãn mức BR-SLA-02 + số ngày | ✅ có nhãn (Quá hạn / Quá hạn nghiêm trọng) |
| (A) Nhãn khớp ngưỡng 50/100/200 tính từ dữ liệu thực | ❌ 101 (Sắp hết hạn→Quá hạn), 105/106 (Quá hạn→Nghiêm trọng) |
| (A) Bước 3: cả 4 mức xuất hiện ≥1 lần | ❌ chỉ 2/4 mức (Quá hạn, Quá hạn nghiêm trọng). "Bình thường" + "Sắp hết hạn" vắng mặt |
| (B) gạch 1: hồ sơ còn hạn báo quá hạn (101) | ❌ tái hiện — 101 "Quá hạn · 0 ngày LV" |
| (B) gạch 2: 105/106 đẩy lên nghiêm trọng | ❌ tái hiện |
| (B) gạch 3: 108/109/110 kết thúc vẫn đếm quá hạn | ✅ **ĐÃ SỬA** — nay "Đã hoàn thành" |
| (B) gạch 4: tooltip % sai (103=188% vs 150%) | ❌ tái hiện |
| (B) gạch 5: chỉ thấy 2 mức | ❌ tái hiện (2/4) |

→ 4/5 gạch (B) tái hiện + (A) trượt điều kiện khớp ngưỡng và đủ 4 mức → **Reopen**. Điểm đã sửa: hồ sơ đã kết thúc (108/109/110/CT-QAW7-CLOSED) không còn bị tính quá hạn.

**Về tiền đề "mức Bình thường":** KHÔNG tạo được hồ sơ chi trả mới trong môi trường này. Luồng tạo hồ sơ chi trả DUY NHẤT là webhook DVC `/api/v1/ho-so-chi-tras/tiep-nhan-dvc` (xác thực LGSP mTLS/API key — đã thử 8 biến thể key/header, đều HTTP 401 ERR-CT-AUTH-01); tài khoản Doanh nghiệp `0109998887` đăng nhập cổng nội bộ KHÔNG có menu nộp hồ sơ chi trả (chỉ có Đào tạo / Vụ việc HTPL / Doanh nghiệp); không có endpoint tạo bằng cookie-auth. Dù có seed được 1 hồ sơ nộp hôm nay (→ Bình thường) thì mức "Sắp hết hạn" vẫn không xuất hiện vì 101 (đáng lẽ Sắp hết hạn) đang bị tính sai thành Quá hạn → bước "đủ 4 mức" không thể đạt do chính lỗi này. Verdict Reopen không phụ thuộc tiền đề: đã chốt từ các gạch 1/2/4 trên dữ liệu sẵn có.

### Ảnh
- `QLHSDNHTCP_03/image/01-danh-sach-cot-sla-12-ho-so.png` — full danh sách 12 hồ sơ, cột SLA: closed = "Đã hoàn thành" (xám), active = Quá hạn / Quá hạn nghiêm trọng.

---

## QLHSDNHTCP_10 (dòng 19) — trường SLA trên THANH TỔNG QUAN màn CHI TIẾT

**Verdict: Reopen** — ghi sheet 2026-07-25 13:42 (GMT+7). Tài khoản `cbnv_tw_04`.

Mở 3 màn chi tiết, đọc trường SLA trên thanh tổng quan (Mã HS / Quy mô DN / Trạng thái / SLA) + tooltip %, so với danh sách:

| Mã HS | Trạng thái | Danh sách (nhãn / %) | Chi tiết (nhãn / %) | 2 màn khớp? | Mức đúng | KQ |
|---|---|---|---|---|---|---|
| CT-SEED-101 | Chờ tiếp nhận | Quá hạn · 0 ngày LV / 101% | **Quá hạn · 0 ngày LV / 101%** (trường SLA CÓ mặt) | ✅ khớp | Sắp hết hạn (70%) | ❌ mức sai |
| CT-SEED-107 | Đã duyệt | Quá hạn nghiêm trọng · 15 ngày LV / 350% | Quá hạn nghiêm trọng · 15 ngày LV / **350%** | ✅ khớp | Quá hạn nghiêm trọng (% đúng 210) | ✅ nhãn |
| CT-SEED-108 | Đã thanh toán | Đã hoàn thành | **Đã hoàn thành** | ✅ khớp | không quá hạn | ✅ đã sửa |

### Đối chiếu (A) / (B)

| Điều kiện | Kết quả |
|---|---|
| (B) gạch 1: hồ sơ chưa quá hạn — thanh tổng quan KHÔNG có trường SLA (101) | ✅ **ĐÃ SỬA** — 101 nay có trường SLA "Quá hạn · 0 ngày LV" |
| (B) gạch 2: mức gắn sai — 108 đúng hạn vẫn "Quá hạn nghiêm trọng · 21 ngày LV" | ✅ **ĐÃ SỬA** phần 108 (nay "Đã hoàn thành"); nhưng mức vẫn sai chung: 101 chi tiết "Quá hạn" thay vì "Sắp hết hạn" |
| (B) gạch 3: 2 màn tính lệch — 107 danh sách 350% vs chi tiết 400% | ✅ **ĐÃ SỬA** — chi tiết nay = 350% = danh sách (đếm từ ngày nộp) |
| (A) trường SLA có nhãn BR-SLA-02 + số ngày | ✅ có |
| (A) cùng hồ sơ cùng nhãn ở 2 màn | ✅ khớp (101/107/108) |
| (A) **nhãn khớp ngưỡng tính từ dữ liệu thực** | ❌ 101 chi tiết "Quá hạn · 0 ngày LV" (101%) trong khi đúng phải "Sắp hết hạn" (70%) |

→ 3 gạch (B) đặc thù màn chi tiết đều ĐÃ SỬA (có trường SLA, 2 màn nhất quán, đếm từ ngày nộp), NHƯNG (A) trượt điều kiện "nhãn khớp ngưỡng" — thanh tổng quan vẫn hiển thị sai mức do cùng gốc lỗi tính ngày lịch của TC_03 → **Reopen**.

### Ảnh
- `QLHSDNHTCP_10/image/01-chitiet-CT-SEED-101-thanh-tongquan-co-truong-sla.png` — thanh tổng quan 101 nay CÓ trường SLA (đỏ "Quá hạn · 0 ngày LV"), trạng thái Chờ tiếp nhận.
- `QLHSDNHTCP_10/image/02-chitiet-CT-SEED-107-sla-350-khop-danh-sach.png` — 107 chi tiết "Quá hạn nghiêm trọng · 15 ngày LV" (tooltip 350%) = danh sách.
- `QLHSDNHTCP_10/image/03-chitiet-CT-SEED-108-da-hoan-thanh.png` — 108 (Đã thanh toán) SLA "Đã hoàn thành", không còn báo quá hạn.
