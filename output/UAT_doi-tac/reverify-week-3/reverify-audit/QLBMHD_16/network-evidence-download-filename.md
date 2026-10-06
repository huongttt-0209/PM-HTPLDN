# QLBMHD_16 — Network evidence: tải về KHÔNG giữ tên file gốc

Env: `18.143.165.120.nip.io` · Tài khoản `cbnv_tw` (CB Nghiệp vụ - TW) · 2026-07-20.
Biểu mẫu: BM-20260715-001 "QA BM001 Hidden Parent 715" (Định dạng DOCX).

## Thao tác
Màn Chi tiết biểu mẫu → bấm nút **Tải về**. FE gọi `window.open('/api/v1/bieu-maus/28104008-7b0d-4783-9825-a188ad11a289/download', '_blank')`.

## Chuỗi request (Chrome DevTools MCP `list_network_requests` + `get_network_request` reqid=937)

1. `GET /api/v1/bieu-maus/28104008-7b0d-4783-9825-a188ad11a289/download` → **302**
   - Response header `location`:
     ```
     http://18.143.165.120:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/07/e29b802a-a867-4a2d-9b42-a5c8b16b57ee/valid.docx?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27QA%2520BM001%2520Hidden%2520Parent%2520715.docx&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=...&X-Amz-Expires=300&X-Amz-Signature=...
     ```
2. Browser đi tiếp tới presigned MinIO URL ở trên để tải file.

## Giải mã (decode)
- **Object lưu trên storage (tên file gốc):** `valid.docx`  ← lấy từ path `.../e29b802a-.../valid.docx` (khớp `duongDanFile` trong API detail).
- **`response-content-disposition` (BE ép tên file tải về):**
  `attachment; filename*=UTF-8''QA%20BM001%20Hidden%20Parent%20715.docx`
  → **Tên file tải về = `QA BM001 Hidden Parent 715.docx`** = **TÊN BIỂU MẪU** (`tenBieuMau`), KHÔNG phải tên file gốc.

## Kết luận
BE (`/download`) chủ động set `response-content-disposition` = **tên biểu mẫu** thay vì **tên file gốc** (`valid.docx` / output field `file_ten`). → Tên tệp gốc KHÔNG được giữ nguyên khi tải về.

- SRS `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-09-bieu-mau.md:335` — Processing Tải về, Bước 3: "Truyền file gốc về máy người dùng (**giữ nguyên tên file gốc**)".
- SRS `:356` — Outputs #5 `file_ten` = "Tên file gốc" (hệ thống có lưu tên gốc, đáng lẽ dùng cho tải về).

Khớp đối tác QLBMHD_16 (evidence: hộp thoại Save As hiện tên = tên biểu mẫu, không phải tên file gốc).
