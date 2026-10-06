# QLBMHD_16 — Re-verify trên DỮ LIỆU MỚI sau dev fix (2026-07-23)

Env: `https://18.143.165.120.nip.io` · Tài khoản `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW) · Chrome DevTools MCP · 2026-07-23 09:2x.
Mục tiêu: kiểm tra dev đã fix QLBMHD_16 chưa + kiểm chứng verdict "Reopen" (2026-07-22) có chính xác không.

## Vì sao phải test dữ liệu mới
Verdict "Reopen" (2026-07-22) chỉ test trên record CŨ **BM-20260715-001** (tạo 15/07, trước khi dev fix). Nếu cơ chế fix dựa vào tên file gốc lưu lúc upload, record cũ có thể mang data lỗi cũ → test record cũ không đủ kết luận fix. Vì vậy tạo record MỚI với tên file gốc phân biệt rõ ràng.

## Cơ chế (đã xác định)
Endpoint `GET /api/v1/bieu-maus/<id>/download` → **302**, `location` trỏ presigned MinIO URL kèm `response-content-disposition` do BE tự set. BE lấy tên tải về từ trường **`tenFile`** của record (KHÔNG phải object path thực trên storage).

## Test A — Record CŨ (baseline) BM-20260715-001
- `tenBieuMau` = "QA BM001 Hidden Parent 715"
- `tenFile` (DB) = **"QA BM001 Hidden Parent 715.docx"** ⚠️ (data cũ đã lưu = tên biểu mẫu, KHÔNG phải tên file thật)
- `duongDanFile` object thực = `.../valid.docx`
- `/download` (reqid=99) 302 `location`:
  `.../valid.docx?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27QA%2520BM001%2520Hidden%2520Parent%2520715.docx`
  → decode: `attachment; filename*=UTF-8''QA BM001 Hidden Parent 715.docx`
- **Tên tải về = tên biểu mẫu ❌** (giống hệt Reopen cũ) — nhưng do `tenFile` mang data lỗi từ trước fix.

## Test B — Record MỚI (quyết định) BM-20260723-001
Tạo qua UI: **Thêm biểu mẫu** → tên BM = "Verify QLBMHD16 - tenBM khac tenfilegoc 0723", upload file gốc tên **`GOCFILE-abc123-QLBMHD16.xlsx`** (khác hẳn tên BM).

- `POST /api/v1/bieu-maus/upload` (reqid=117) → 201, response `tenFile` = **"GOCFILE-abc123-QLBMHD16.xlsx"** (lưu ĐÚNG tên file thật upload).
- `POST /api/v1/bieu-maus` (reqid=118) → 201, id `9f54203b-2fb5-4f3b-b484-4c847b01e147`, maBM `BM-20260723-001`, `tenFile` = "GOCFILE-abc123-QLBMHD16.xlsx", `duongDanFile` = `.../GOCFILE-abc123-QLBMHD16.xlsx`.
- `/download` (reqid=123) → **302**, `location` (get_network_request reqid=123):
  `http://18.143.165.120:9000/htpldn/.../GOCFILE-abc123-QLBMHD16.xlsx?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27GOCFILE-abc123-QLBMHD16.xlsx&...`
  → decode: `attachment; filename*=UTF-8''GOCFILE-abc123-QLBMHD16.xlsx`
- **Tên tải về = `GOCFILE-abc123-QLBMHD16.xlsx` = TÊN FILE GỐC ✅** (KHÔNG phải tên biểu mẫu "Verify QLBMHD16...").

## Kết luận
- **Fix HOẠT ĐỘNG trên dữ liệu mới → PASS.** Luồng upload nay lưu đúng tên file gốc vào `tenFile`, và `/download` trả `content-disposition` = tên file gốc → giữ nguyên tên file gốc, đúng SRS `srs-fr-09-bieu-mau.md:335`.
- Verdict "Reopen" (2026-07-22) **không còn chính xác cho luồng go-forward** — nó test trên record cũ mang data lỗi từ trước fix.
- **Caveat (còn tồn tại):** Record CŨ tạo trước fix (vd BM-20260715-001) có `tenFile` đã bị ghi = tên biểu mẫu → tải về vẫn ra tên biểu mẫu. Không phải lỗi code live; là legacy data. Nếu yêu cầu áp dụng cả record cũ → cần dev backfill/migrate `tenFile` cho các record pre-fix.

## Verify 2 method (theo SOP §4.4)
1. Fetch endpoint `/download` (redirect:manual) → CDP `list_network_requests` + `get_network_request` đọc header `location` 302. (cả record cũ + mới)
2. `GET /api/v1/bieu-maus/<id>` đọc trực tiếp trường `tenFile` — giải thích chênh lệch cũ/mới.

Bằng chứng ảnh: `../../bug-reports/bieu-mau/image/QLBMHD_16-reverify-0723-newdata-detail.png` + `...-newdata-list.png`.
File test upload: `GOCFILE-abc123-QLBMHD16.xlsx` (cùng thư mục này).
