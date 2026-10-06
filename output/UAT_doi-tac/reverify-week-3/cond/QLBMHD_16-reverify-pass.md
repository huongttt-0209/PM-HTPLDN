# Bảng đối chiếu điều kiện — QLBMHD_16 RE-VERIFY PASS (dữ liệu mới, sau dev fix 2026-07-23)

Re-verify sau khi dev claim fix. Cột giữa = điều kiện của BUG GỐC (BUG-BM-B5-01 trong Pass-bug-report-bieu-mau-batch5.md). Re-test phải khớp vai trò/state/data mà bug gốc mô tả. Phương pháp: tạo biểu mẫu MỚI qua luồng chuẩn (upload file gốc có tên phân biệt rõ) → Tải về → đọc header `location` 302 của `/download` (fetch redirect:manual + Chrome DevTools MCP `get_network_request`).

| Điều kiện có thể đổi kết quả | Bug gốc (BUG-BM-B5-01) | Mình test (re-verify) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ - TW (CB_NV_TW, BTP·TW) | `cbnv_tw` — CB Nghiệp vụ - Trung ương (BTP·TW), cùng vai trò | Không |
| Nút thao tác | Tải về màn Chi tiết → endpoint `/download` | Tải về `/download` record BM-20260723-001 (id 9f54203b...), cùng endpoint | Không |
| Tên file gốc vs tên biểu mẫu | Tên file gốc KHÁC tên biểu mẫu | Tên file gốc `GOCFILE-abc123-QLBMHD16.xlsx` KHÁC tên BM "Verify QLBMHD16 - tenBM khac tenfilegoc 0723" — phân biệt rõ ràng | Không |

**Kết luận: 0 GAP trên các điều kiện quyết định. Fix HOẠT ĐỘNG trên dữ liệu mới → tên tải về = tên file gốc. PASS.**

`GET /api/v1/bieu-maus/9f54203b-2fb5-4f3b-b484-4c847b01e147/download` → **302**, `location`:
`.../GOCFILE-abc123-QLBMHD16.xlsx?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27GOCFILE-abc123-QLBMHD16.xlsx`
→ decode `attachment; filename*=UTF-8''GOCFILE-abc123-QLBMHD16.xlsx` = **TÊN FILE GỐC** (không phải tên biểu mẫu). Đúng SRS `srs-update-2026-5-5`/`srs-fr-09-bieu-mau.md:335` "giữ nguyên tên file gốc".

Cơ chế fix: luồng `POST /bieu-maus/upload` nay lưu đúng tên file thật vào trường `tenFile`; `/download` set `content-disposition` = `tenFile`.

**Caveat (legacy data, KHÔNG phải lỗi code live):** Record CŨ tạo trước fix (vd BM-20260715-001) có `tenFile` đã bị ghi = tên biểu mẫu ("QA BM001 Hidden Parent 715.docx") → tải về vẫn ra tên biểu mẫu. Nếu yêu cầu áp dụng cả record cũ → dev cần backfill/migrate `tenFile`. Evidence đầy đủ: `../reverify-audit/QLBMHD_16/reverify-newdata-2026-07-23.md`.
