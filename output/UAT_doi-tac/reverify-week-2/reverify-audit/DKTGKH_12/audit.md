# Audit verify vòng 2 — DKTGKH_12 (row 3, tab tuần 2)

**Verdict:** `Open` · **Bug ID:** `BUG-DKTGKH_12` · **Ngày:** 2026-07-27
**Bảng đối chiếu điều kiện (0 GAP):** [`../../cond/DKTGKH_12-r2.md`](../../cond/DKTGKH_12-r2.md)

## Cổng 1 — bằng chứng đối tác

| Mục | Nội dung |
|---|---|
| File | `DKTGKH_12_v2.webm` (5.465.454 byte, tải bằng `fetch_evidence.py --col-header "Ảnh/video 2"`) |
| Frame chứa LỖI | `frames/t018.13s.jpg` — modal "Import danh sách đăng ký từ Excel": Tổng dòng 3 · Thành công 0 · Bỏ qua (trùng) 0 · Lỗi 3; danh sách "Dòng 2/3/4: Email không hợp lệ" |
| Frame dữ liệu nguồn | `frames/t024.16s.jpg` — file `dang-ky-dao-tao-template.xlsx` mở trong Excel: 3 dòng, cột Email là **ô liên kết** (chữ xanh gạch chân, tooltip `mailto:linh@gmail.com`) |
| Dữ kiện neo | (a) `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/9a72d61b-…?tab=hoc-vien` · (b) khóa học ở bước Đã duyệt, tab Học viên · (c) vai trò CB_NV_TW, đơn vị BTP·TW |

## Cổng 3 — đối chiếu SRS vs thực tế web (loại bug: Import/Upload)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-03-dao-tao.md:461` — FR-III-04 (UC23) Inputs #4: `email \| text \| Y \| Email` — bắt buộc, không đặt ràng buộc nào hẹp hơn định dạng email thông thường | 3 email đúng định dạng bị từ chối hết với lý do "Email không hợp lệ" | **Thiếu** |
| `srs-fr-03-dao-tao.md:475` — Processing bước 6: "Nếu import Excel: validate template, import từng dòng, báo cáo KQ" | Import từ chính file mẫu của hệ thống → 0/3 dòng vào được dù dữ liệu hợp lệ | **Thiếu** |
| `srs-fr-03-dao-tao.md:443` — "3 cách: chuyên trang, nhập tay, import Excel" (import ngang hàng nhập tay) | Cùng `linh@gmail.com`: nhập tay → HTTP 201, `trangThai=CHO_DUYET`; import Excel → "Email không hợp lệ" ⇒ 2 đường nhập liệu trái ngược trên cùng một giá trị | **Thiếu** |

## Phép đo đã chạy (artifact QUAN SÁT trên data thật)

| # | Phép đo | Kết quả | Artifact |
|---|---|---|---|
| 1 | Tái hiện đúng điều kiện đối tác — file A (ô Email có liên kết) | `Tổng 3 · Thành công 0 · Bỏ qua 0 · Lỗi 3`, "Dòng 2/3/4: Email không hợp lệ" — trùng khít frame t018.13s | `DKTGKH_12-r2-import-A-hyperlink.png` |
| 2 | Đối chứng tách biến — file B (cùng 3 email, ô Email text thường) | `Tổng 3 · Thành công 2 · Bỏ qua (trùng) 1 · Lỗi 0`, bảng hiện đủ học viên | `DKTGKH_12-r2-import-B-text-thuong.png` |
| 3 | Đối chứng đường nhập liệu khác — `linh@gmail.com` qua luồng nhập tay | HTTP **201 Created**, `trangThai=CHO_DUYET` ⇒ email hợp lệ theo chính rule hệ thống | `import-response-A-hyperlink.json` |
| 4 | Response body của chính request import (gốc rễ) | `{"row":2,"email":"[object Object]","reason":"Email không hợp lệ"}` — máy chủ đọc ô Email ra `[object Object]` rồi kiểm định dạng chuỗi đó | `import-response-A-hyperlink.json` |
| 5 | Đo thông báo (`tools/toast-capture.js`, `soObserverDangSong=1`) | `SO_REQUEST=1` (POST …/import) · `SO_KHUNG_THONG_BAO=1` · chữ "Import hoàn tất" | `import-response-A-hyperlink.json` |

Lưu ý phép đo 2: dòng "Bỏ qua (trùng) 1" là do bản ghi `linh@gmail.com` đã được tạo ở phép đo 3 ngay trước đó — 2 + 1 = 3, số liệu nhất quán, không phải lỗi.

## Ngoài tiêu chí BA — có thấy gì bất thường không?

**Có, 1 điểm (đã gộp vào cùng bug entry vì cùng một thao tác):** hệ thống hiện thông báo **"Import hoàn tất"** (thông báo thành công) trong khi 100% số dòng bị loại, `Thành công 0`. Đo bằng `toast-capture.js` cho `SO_KHUNG_THONG_BAO=1`, chữ đúng là "Import hoàn tất" — không phải bug ma, không phải double-toast.

## Ghi chú nội bộ (KHÔNG đưa vào note sheet)

- **Mâu thuẫn spec cần BA để mắt, KHÔNG ảnh hưởng verdict này:** `srs-fr-03-dao-tao.md:443` + `:475` mô tả import Excel là 1 trong 3 cách
  đăng ký, nhưng `srs-fr-03-dao-tao.md:1683` lại ghi theo CSV UC22/UC23 v1.1 rằng CB NV **không** có luồng "import Excel danh sách đăng ký".
  Sản phẩm hiện đang cho CB NV nút Import Excel → dù BA chốt theo hướng nào, việc đọc sai ô Email vẫn là lỗi.
- **Dữ liệu test còn lại trên env:** khóa `KH-QAW7-HOINGHI` phát sinh 3 đăng ký `CHO_DUYET` do QA tạo (QA Probe Email / Nguyễn Văn Ngọc / Nguyễn Văn A).
  UI chỉ có Phê duyệt / Từ chối, không có xóa → để lại, ghi nhận tại đây.
- **File tái hiện:** `files/A-hyperlink-giong-doi-tac.xlsx` · `files/B-text-thuong-du-sdt.xlsx` · `files/dang-ky-dao-tao-template.xlsx` (file mẫu gốc tải từ hệ thống).
