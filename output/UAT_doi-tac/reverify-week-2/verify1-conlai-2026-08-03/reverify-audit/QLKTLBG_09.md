# QLKTLBG_09 — Evidence audit verify vòng 1 (2026-08-03)

> Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · row **117**
> **Verdict QA (cột `Verify`): `Open`** · Bug ID **`BUG-QLKTLBG_09`**
> Tài khoản ra verdict: **`cbnv_tw`** (CB_NV_TW · BTP · TW) — đúng vai trò đối tác. Không dùng `admin`.
> Môi trường: `https://18.143.165.120.nip.io` · build hiển thị ở sidebar **HTPLDN · V1.0.5** · thời điểm test 03/08/2026 15:51–16:00.

## Note dev trước khi QA đè (đọc lại sheet lúc 2026-08-03 ~16:00)

Cột **R (`DEV phản hồi lần 1`) TRỐNG** tại thời điểm QA đọc lại sheet ngay trước khi ghi — dev **chưa** viết giải trình nào cho dòng này, nên **không có nội dung cũ bị đè**.

Cột **P (`Trạng thái dev fix 1`) = `BA confirm`** — giá trị này do **dev** điền trong ngày 03/08/2026, **không phải** giá trị gốc và **không** ràng buộc verdict của QA. QA chạy `--mode qaverdict` nên **không đụng cột P**.

Giá trị các cột gốc của đối tác (giữ nguyên, chỉ để tham chiếu):
- `Mô tả` = *Xem bài giảng/tài liệu chứa Slide*
- `Kết quả mong đợi` = *Hệ thống mở khu vực xem trước nội dung với Slide: trình chiếu inline*
- `Kết quả thực tế` = *Hệ thống thực hiện tải xuống slide, không trình chiếu inline*
- `Trạng thái 1` = `Fail` · `Ảnh/vieo 1` = `QLKTLBG_09_v2.webm`

---

## CỔNG 1 — bằng chứng đối tác (đã tự mở xem tới khoảnh khắc lỗi)

File: `partner-evidence/QLKTLBG_09_v2.webm` (1.968.889 bytes, ~6,2 giây). Frame trích ở `frames/QLKTLBG_09/dense/`.
**Người verify đã tự mở 4 frame full-res** (`t003.10s`, `t003.62s`, `t004.14s`, `t006.19s`), không đọc qua montage thu nhỏ.

**3 dữ kiện neo**

| # | Dữ kiện | Giá trị đọc trực tiếp từ pixel |
|---|---|---|
| (a) | URL / bản ghi | `htpldn-uat.ospgroup.vn/dao-tao/bai-giang/danh-sach` — dòng đầu bảng, tên **`TKM thêm mới slide bài giảng`**. Màn danh sách không hiển thị mã bản ghi. |
| (b) | Trạng thái entity | `Loại tài liệu = **Slide**` (thẻ xanh) · `Dung lượng = 2.2 MB` · trong hộp thoại xem trước: `Công khai = **Đã công khai**`, `Ngày công khai = 23/07/2026 16:01` |
| (c) | **Dữ liệu tiền đề — định dạng tệp** | **`10.2. Tia, đoạn thẳng.pptx`**, `Save as type = Microsoft PowerPoint Presentation (*.pptx)` — đọc từ hộp thoại Windows "Save As" ở frame `t004.14s`. **Đây là điểm quyết định điều kiện: đối tác dùng `.pptx`.** |

Vai trò đối tác: `Cán bộ NV Trung ương` · **CB_NV_TW** · đơn vị **BTP · TW** (header phải). Đồng hồ máy đối tác: 04:04 PM 23/07/2026.

## CỔNG 2 — hiểu bug (3 dòng)

1. **Evidence đã xem + frame chứa LỖI:** `QLKTLBG_09_v2.webm` — `t003.62s` hộp thoại *"Xem trước: TKM thêm mới slide bài giảng"* mở ra chỉ có 3 dòng dữ liệu (Công khai/Ngày công khai · Ảnh đại diện · Mô tả công khai), **không có khung trình chiếu**; **`t004.14s` là FRAME LỖI** — hộp thoại Windows "Save As" bung lên đè hộp thoại xem trước, `File name = 10.2. Tia, đoạn thẳng.pptx` → trình duyệt đang tải tệp về máy. Trạng thái này giữ nguyên tới hết video (`t006.19s`).
2. **Đối tác phản ánh CỤ THỂ:** với bài giảng **loại Slide**, bấm xem trước thì hệ thống **tải tệp `.pptx` xuống máy** thay vì **trình chiếu nội dung slide ngay trên trang**. Đối tác không nói gì về loại PDF/Video.
3. **Data + bước tái hiện:** đăng nhập CB_NV_TW → `Đào tạo, tập huấn` → `Kho tài liệu / Bài giảng` → chọn dòng có `Loại tài liệu = Slide`, tệp `.pptx`, `Đã công khai` → bấm icon con mắt (`Xem trước`) → quan sát khung xem trước và hành vi tải tệp.

## CỔNG 3 — đối chiếu SRS vs thực tế web

Nguồn SRS **duy nhất**: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`.
Số dòng dưới đây **đã tự mở file kiểm lại** (không lấy từ trí nhớ, không lấy từ `input/srs-update-2026-5-5/`).

| SRS yêu cầu (file:line + trích nguyên văn) | Thực tế web 03/08/2026 | Đủ/Thiếu |
|---|---|---|
| `srs-fr-03-dao-tao.md:726` — *"**Mô tả:** Quản lý tài liệu/bài giảng dùng chung. 3 loại: Slide (PPTX), PDF, Video (YouTube embed). **Preview inline.** Switch công khai lên chuyên trang."* | Slide `.pptx` **không** preview inline — khung xem trước trắng hoàn toàn | **Thiếu** |
| `:743` — *"\| 4 \| file_bai_giang \| structured \| Cond \| Max 20MB, .pptx/.pdf (bắt buộc nếu SLIDE/PDF) \|"* | Form `Thêm mới` với `Loại tài liệu = Slide` ghi rõ *"Định dạng: .pptx. Tối đa 20MB."* → `.pptx` **nằm trong** định dạng hợp lệ, không phải định dạng lạ | Đủ (khớp) |
| `:792` — *"- **Given** CB NV xem file **When** chọn preview **Then** hiển thị nội dung trên trình duyệt"* | Bấm xem trước → **không** hiển thị nội dung tệp trên trình duyệt | **Thiếu** |
| `:1951` — *"\| Hành động \| — \| Xem trực tuyến · Tải về (chỉ Slide/PDF) · Sửa · Xóa (xóa mềm, có hộp xác nhận) \|"* | Cột `Thao tác` chỉ có **3** hành động: xem trước (con mắt) · Sửa (bút) · Xóa (thùng rác). **Không có hành động "Tải về"** | **Thiếu** |
| `:1955` — *"**Thành phần 6 — Bảng xem trước:** **Slide/PDF xem trực tiếp trong trình duyệt**; Video nhúng khung YouTube; **định dạng không xem được → "Không thể xem trực tuyến" + nút "Tải về"**…"* | Slide: khung trắng. PDF: trang lỗi trình duyệt. **Không** có chuỗi *"Không thể xem trực tuyến"*, **không** có nút *"Tải về"* (hộp thoại chỉ có đúng 1 nút `Close`) | **Thiếu** |
| `:1955` — *"Video nhúng khung YouTube"* | Video: khung YouTube hiện đúng, phát được | Đủ |
| `:1955` — khối thông tin kèm theo: Ảnh đại diện · Ngày công khai · Mô tả công khai · Tệp đính kèm công khai | Hộp thoại hiện Công khai/Ngày công khai · Ảnh đại diện · Mô tả công khai. **Không thấy** dòng *Tệp đính kèm công khai* (bản ghi test không có tệp đính kèm nên chưa kết luận) | Chưa kết luận |

**UC Reference** (`:723`): *"**UC Reference:** UC 26 | **Priority:** Essential | **Stability:** High"* → **FR-III-07 (UC26)**. Mục màn hình: **SCR-III-03** (`:1918`), và `:1922` chốt *"Bảng cột đã nội hóa xuống dưới — khi hai bên khác nhau thì lấy mục này làm căn cứ nghiệm thu"* ⇒ SCR-III-03 trong SRS v3.5 là căn cứ nghiệm thu.

## Bằng chứng real-data (GATE) — artifact QUAN SÁT, chạy trên dữ liệu tự seed

Loại claim = **Thao tác/state + Hiển thị/render** ⇒ artifact = kết quả thao tác thật (DOM + mạng) + ảnh full-res đúng phần tử tranh chấp.

**Bản ghi tự seed để khớp đúng điều kiện đối tác** (Nguyên tắc 4):
`QA VERIFY 03/08 - QLKTLBG_09 Slide PPTX cong khai` · id `9e7e90d7-0b6b-4a98-ad7f-11a8a7e64da2` · `loaiTaiLieu = SLIDE` · tệp `QLKTLBG_09-slide-that-QA.pptx` (PowerPoint thật, 40 part OOXML, 2 slide có chữ, 28.5 KB) · `congKhai = true`, `thoiGianDangTai = 2026-08-03T08:57:37Z` · có ảnh đại diện.
Bước seed đo bằng `toast-capture.js`: **1 request `POST /api/v1/bai-giangs` → 1 thông báo "Tạo bài giảng thành công"** (không lặp) — ảnh `BUG-QLKTLBG_09-seed-01-form-truoc-khi-luu.png`, `BUG-QLKTLBG_09-seed-02-toast-sau-khi-luu.png`.

**Phương pháp 1 — DOM/giao diện** (bấm icon con mắt của bản ghi trên):
- Hộp thoại `Xem trước: QA VERIFY 03/08 - QLKTLBG_09 Slide PPTX cong khai`, toàn bộ chữ trong hộp thoại chỉ là: `Công khai · Đã công khai · Ngày công khai · 03/08/2026 15:57 · Ảnh đại diện · Mô tả công khai · —`.
- Bên dưới là 1 khung `iframe` **752×500** trỏ vào tệp `.pptx`, nhưng `location` bên trong khung = `about:blank`, nội dung **rỗng**.
- `Không thể xem trực tuyến` → **không có**. `Tải về` → **không có**. Số nút trong hộp thoại = **1** (`Close`).
- Bộ bắt thông báo: **0 thông báo · 0 request ghi** → người dùng không nhận được lời giải thích nào.

**Phương pháp 2 — mạng** (`list_network_requests` + `get_network_request`):
- `GET /api/v1/bai-giangs/9e7e90d7-…/preview-url` → 200 (trả URL ký sẵn kèm `response-content-disposition=inline`).
- `GET …/QLKTLBG_09-slide-that-QA.pptx?response-content-disposition=inline…` → HTTP 200 nhưng **`Request failed with net::ERR_ABORTED`**. Phản hồi kèm `content-type: application/vnd.openxmlformats-officedocument.presentationml.presentation`, `content-disposition: inline`, **`x-frame-options: DENY`**, **`content-security-policy: frame-ancestors 'none'`**.
- Bản ghi PDF `QA UAT Bài giảng Công khai QLKTLBG_08b` → cùng đường dẫn lưu trữ, phản hồi cũng có `x-frame-options: DENY` → **`net::ERR_BLOCKED_BY_RESPONSE`**, khung xem trước hiện trang lỗi *"18.143.165.120.nip.io refused to connect."*

**Hai phương pháp KHÔNG mâu thuẫn** — cùng kết luận: nội dung tệp không được hiển thị trong trang, và người dùng không được báo gì.

## Chênh lệch giữa triệu chứng đối tác và triệu chứng hiện tại (ghi rõ, không giấu)

| | Đối tác (23/07, env `htpldn-uat.ospgroup.vn`) | QA (03/08, env `18.143.165.120.nip.io`, V1.0.5) |
|---|---|---|
| Có trình chiếu slide inline không? | **Không** | **Không** |
| Có chữ "Không thể xem trực tuyến" / nút "Tải về" không? | Không | Không |
| Triệu chứng phụ | Trình duyệt **bung hộp thoại tải tệp `.pptx`** | Khung xem trước **trắng**, tệp bị chặn nhúng (`x-frame-options: DENY`), **không** tải |

⇒ **Yêu cầu chính của SRS (`:1955`, `:792`, `:726`) vẫn KHÔNG được đáp ứng** trên bản hiện tại; chỉ triệu chứng phụ đổi. **Đây không phải ca "không tái hiện"** — lỗi đối tác báo (Slide không trình chiếu inline) tái hiện đầy đủ.

## Tự vấn trước khi ghi sheet

- `Open` → sai clause SRS nào? → `srs-fr-03-dao-tao.md:1955` (*"Slide/PDF xem trực tiếp trong trình duyệt"* + nhánh dự phòng *"Không thể xem trực tuyến" + nút "Tải về"*), `:792` (Acceptance Criteria *"chọn preview → hiển thị nội dung trên trình duyệt"*), `:726` (*"Preview inline"*), `:1951` (thiếu hành động *"Tải về"*). **Kể cả** đọc theo hướng có lợi nhất cho hệ thống (coi `.pptx` là "định dạng không xem được") thì app vẫn sai, vì nhánh dự phòng của `:1955` bắt buộc phải hiện chữ *"Không thể xem trực tuyến"* + nút *"Tải về"* — hiện không có cả hai.
- Có phải `BA confirm` không? → **Không.** Kỳ vọng của đối tác (*"trình chiếu inline"*) **trùng khớp** với SRS, không phải bất đồng đặc tả. SRS không silent, không mâu thuẫn giữa các nguồn.
- Có phải `Reject` không? → **Không.** Không chứng minh được đối tác thao tác/hiểu sai; ngược lại đã tái hiện được lỗi chính.
- Còn GAP điều kiện không? → **Không** — xem `cond/QLKTLBG_09.md`, đã đóng GAP định dạng tệp (`.pptx` thật) và GAP trạng thái (`Đã công khai`) bằng **seed + test thật**, không bằng lập luận.

## Ảnh đã chụp và **đã mở đọc**

| Ảnh | Nội dung đã đọc được từ pixel |
|---|---|
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-web-01-sau-khi-bam-xem-truoc-slide.png` | Hộp thoại *Xem trước: RECON 03/08 - Bai giang SLIDE (pptx)…* — 3 dòng dữ liệu + vùng trắng lớn phía dưới, không có nội dung slide |
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-web-02-doi-chung-xem-truoc-PDF.png` | Hộp thoại xem trước bản ghi PDF — vùng xám kèm biểu tượng tệp lỗi của trình duyệt |
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-seed-01-form-truoc-khi-luu.png` | Form Thêm bài giảng: `Slide` · `QLKTLBG_09-slide-that-QA.pptx (28.5 KB)` · ảnh đại diện xanh · công tắc `Công khai` **bật** |
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-seed-02-toast-sau-khi-luu.png` | Danh sách sau khi lưu — dòng mới `QA VERIFY 03/08 - QLKTLBG_09 Slid…` · `Slide` · `28.5 KB` · có ảnh đại diện |
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-web-03-xem-truoc-slide-dacongkhai-trong.png` | **Ảnh bằng chứng chính** — hộp thoại *Xem trước: QA VERIFY 03/08 - QLKTLBG_09 Slide PPTX cong khai*, `Đã công khai`, `03/08/2026 15:57`, ảnh đại diện hiện; khung xem trước bên dưới **trắng hoàn toàn**, không chữ, không nút |
| `bug-reports/dao-tao/image/BUG-QLKTLBG_09-web-04-doi-chung-video-youtube-hien-duoc.png` | Đối chứng: hộp thoại xem trước bản ghi Video — khung YouTube hiện đúng, có nút phát |

## Ngoài tiêu chí của case, có gì bất thường không?

**Có 1 lỗi ngoài phạm vi — ĐÃ mở dòng TC mới trên sheet để tới được dev:**

- **Bài giảng loại PDF cũng không xem trực tuyến được.** SRS `:1955` yêu cầu *"Slide/**PDF** xem trực tiếp trong trình duyệt"*, nhưng khung xem trước của bản ghi PDF hiện trang lỗi *"18.143.165.120.nip.io refused to connect."*, cũng không có chữ *"Không thể xem trực tuyến"* và không có nút *"Tải về"*. Đối tác chỉ báo loại Slide nên đây là lỗi **ngoài phạm vi** case này.
- Đã đóng GAP dữ liệu trước khi log: tự seed bài giảng `QA VERIFY 03/08 - QLKTLBG_10 PDF that cong khai` với **tệp PDF thật 2 trang có chữ đọc được** (`QLKTLBG_10-pdf-that-QA.pdf`, kiểm chứng bằng PyMuPDF: `so trang 2`, đọc được chuỗi *"QLKTLBG_10 - BAI GIANG PDF KIEM THU QA"*), `Đã công khai` → vẫn không hiển thị. Tái hiện **3/3** trên 3 bản ghi PDF khác nhau.
- **Đã ghi vào sheet:** `tools/sheet_add_bug_row.py` → tab `UAT_TGPL Doanh Nghiệp-tuần 2`, **dòng 132**, Mã TC **`QLKTLBG_10`** (trùng đúng mã TC gốc của đối tác trong danh mục "Trang tính6": *"Xem bài giảng/tài liệu chứa PDF"*), `Trạng thái 1 = Fail`, `Verify = Open`. Bug ID nội bộ **`BUG-QLKTLBG_10`** — entry đầy đủ ở [`bug-reports/dao-tao/bug-report-dao-tao.md`](../bug-reports/dao-tao/bug-report-dao-tao.md).
- Ảnh đã mở đọc: `bug-reports/dao-tao/image/BUG-QLKTLBG_10-xem-truoc-pdf-khong-hien-noi-dung.png` (hộp thoại xem trước PDF hiện đúng dòng chữ *"18.143.165.120.nip.io refused to connect."*) và `BUG-QLKTLBG_10-seed-01-tao-bai-giang-pdf.png`.

Quan sát khác (đã đọc từ ảnh, **chưa** đủ căn cứ log thành bug riêng):
- Cột `Thao tác` được ghim cố định bên phải và che mất phần cuối các cột `Công khai` / `Người tạo` / `Ngày tạo` khi bảng rộng hơn khung nhìn — đã ghi vào bug entry như một phần của `:1951` (thiếu hành động *Tải về*), không tách dòng TC riêng.
- Hộp thoại "Xem trước" chỉ hiển thị 4 dòng dữ liệu; chưa xác minh được dòng *Tệp đính kèm công khai* của `:1955` vì bản ghi test không có tệp đính kèm.

## Note dev bị QA đè lần 2 (2026-08-03, khi đồng bộ cột P = cột Verify)

> Dev viết note này SAU khi QA ghi verdict `Open` vòng đầu (cột R lúc QA ghi vòng đầu là TRỐNG).
> Lưu nguyên văn ở đây trước khi bị đè:

```
BA chốt Loại 1 (SRS FR-III-07): Slide phải xem inline. Fix theo hướng FE render (pptx-preview client-side, cùng triết lý biểu mẫu, không LibreOffice/Docker): thêm khu vực render nội dung slide inline + fallback "Không thể xem trực tuyến"+Tải (SRS:1955), mở preview không auto-tải, tách nút Tải về. BE thêm endpoint stream cùng-origin. Commit abca9b459 (PR #71). Verify e2e local: render inline 0 iframe, không auto-tải; PDF/Video giữ nguyên. "Q-3" chỉ áp tệp đính kèm hỏi-đáp, không áp bài giảng.
```

**Ý nghĩa:** dev đã XÁC NHẬN đây là bug thật (khớp verdict `Open` của QA) và khai đã fix ở commit `abca9b459` (PR #71) — nhưng bản trên môi trường UAT lúc QA đo (V1.0.5, bundle build 2026-08-03 07:59 GMT) VẪN lỗi. Cần một vòng re-verify sau khi PR #71 được deploy lên UAT.
