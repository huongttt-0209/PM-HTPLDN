# QLBMHD_17/18/19 — Network + FE evidence: "Xem trước" mở file thô (không convert preview)

Env: `18.143.165.120.nip.io` · Tài khoản `cbnv_tw` (CB Nghiệp vụ - TW) · 2026-07-20.
Áp dụng chung cho cụm preview: QLBMHD_17 (generic) · QLBMHD_18 (DOCX) · QLBMHD_19 (XLSX).

## Hành vi FE (Chrome DevTools MCP — chặn `window.open` + kiểm DOM)
Màn Chi tiết biểu mẫu → bấm nút **Xem trước**:
- FE gọi `window.open('/api/v1/bieu-maus/<id>/preview', '_blank')` — mở tab mới trỏ tới endpoint `/preview`.
- KHÔNG render bất kỳ khung xem trước in-app nào: `hasModal=false`, `hasIframe=false`, `hasPdfViewer=false` (không có `.ant-modal`/`iframe`/PDF viewer/canvas).
- `list_pages` sau khi bấm: có tab mới `https://18.143.165.120.nip.io/api/v1/bieu-maus/28104008-.../preview`.

→ Không có "cửa sổ xem trước" trong app; chỉ mở URL endpoint file trong tab mới.

## Hành vi BE — endpoint `/preview` (get_network_request)

### DOCX — biểu mẫu BM-20260715-001 (id 28104008-...), Định dạng DOCX
- `GET /api/v1/bieu-maus/28104008-7b0d-4783-9825-a188ad11a289/preview` → **302** (reqid=1005)
- `location` → `http://18.143.165.120:9000/htpldn/.../valid.docx?response-content-disposition=inline&X-Amz-...`
- → Redirect thẳng tới **file .docx THÔ** (object `valid.docx`), phục vụ `inline`. **KHÔNG** convert sang PDF.

### XLSX — biểu mẫu BM-B6-valid-2 (id ad4258c3-...), Định dạng XLSX
- `GET /api/v1/bieu-maus/ad4258c3-3a94-4f2c-b20b-82ab18226c22/preview` → **302** (reqid=1008)
- `location` → `http://18.143.165.120:9000/htpldn/.../BM-B6-valid-2.xlsx?response-content-disposition=inline&X-Amz-...`
- → Redirect thẳng tới **file .xlsx THÔ** (object `BM-B6-valid-2.xlsx`), phục vụ `inline`. **KHÔNG** convert sang bảng read-only.

## Hệ quả
Tab mới nhận file .docx/.xlsx thô với `content-disposition: inline`. Trình duyệt KHÔNG render inline được Office file → hiện **hộp thoại tải về** (Save As). Đúng như đối tác phản ánh (QLBMHD_17/18/19: "Xem trước mở hộp thoại tải file").

## Đối chiếu SRS v3.5 (`srs-fr-09-bieu-mau.md`)
- `:320-327` Processing — Xem trực tuyến (preview):
  - `:325` Bước 2: "Nếu doc/docx: **chuyển đổi sang PDF preview**".
  - `:326` Bước 3: "Nếu xls/xlsx: **hiển thị preview dạng bảng (read-only)**".
  - `:327` Bước 4: "Nếu không hỗ trợ preview: **thông báo + chuyển sang tải về**".
- Hệ thống hiện KHÔNG convert (docx→PDF, xlsx→bảng), cũng KHÔNG hiển thị "thông báo" theo Bước 4 — mà mở thẳng file thô để trình duyệt tự tải → vi phạm Processing preview.

## Ghi chú phụ (không phải trọng tâm case)
- Các request tới `http://18.143.165.120:9000` (MinIO) log `net::ERR_ABORTED` — do trang HTTPS mở tài nguyên HTTP (:9000) cổng object-storage có thể chặn mixed-content / không expose public. Đây là vấn đề hạ tầng riêng, độc lập với lỗi "preview không convert" ở trên (lỗi này nằm ở việc `/preview` trỏ tới file thô).
