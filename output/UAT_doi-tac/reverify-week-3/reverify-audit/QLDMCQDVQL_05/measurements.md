# Audit — QLDMCQDVQL_05 (row 139) — Tìm kiếm cây đơn vị không ra kết quả → thiếu message empty

**Verdict:** `BA confirm` (actual tái hiện đúng; tranh chấp kỳ vọng vs SRS silent)
**Ngày verify:** 2026-07-21 · **Account:** `admin` (QTHT) · **Tool:** Chrome DevTools MCP
**URL test:** https://18.143.165.120.nip.io/quan-tri/danh-muc/CO_QUAN_DON_VI

## Cổng 1 — Evidence đối tác (ảnh full-res)
- File: `partner-evidence/QLDMCQDVQL_05.jpg` (chụp 2026-07-14).
- Env đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/CO_QUAN_DON_VI`, tab "Cơ quan đơn vị" (Tree View).
- Thao tác: gõ từ khóa **"tư pháp HCM"** vào ô tìm "Cây đơn vị" → **vùng cây trắng hoàn toàn**, không kết quả, KHÔNG có message "Không tìm thấy mục danh mục phù hợp".
- → Đối tác kỳ vọng có thông báo "Không tìm thấy mục danh mục phù hợp"; thực tế không hiện gì.

## Verify env được giao (tái hiện đúng điều kiện đối tác)
- Vào tab "Cơ quan đơn vị" → cây có node "Cục Bổ trợ tư pháp - Bộ Tư pháp".
- Gõ đúng từ khóa **"tư pháp HCM"** (không match) vào ô "Cây đơn vị".
- Kết quả (evaluate_script + ảnh `search-empty-tree.png`):
  - Vùng cây `.ant-tree` innerText length = **0** (trắng, không node hiển thị).
  - `.ant-empty` trong vùng cây = **0** → KHÔNG có empty-state/message trong panel cây.
  - Block empty duy nhất trên màn là panel PHẢI "Chọn một đơn vị từ cây bên trái để xem chi tiết" (placeholder chi tiết, không liên quan search).
- → **TÁI HIỆN ĐÚNG**: search cây đơn vị không ra kết quả → vùng cây trắng, không message nào.

## Đối chiếu SRS (Cổng 3)
| SRS yêu cầu | Dòng | Thực tế web | Đủ/thiếu |
|---|---|---|---|
| SEARCH: nhận từ khóa → tìm theo mã/tên → phân trang + trả kết quả | `srs-v3.5/srs-fr-10-quan-tri.md:130-136` | Search chạy, lọc còn 0 node | Đủ (chức năng search hoạt động) |
| Message chuẩn khi search rỗng ("Không tìm thấy...") | — | Không hiện gì | **SRS SILENT** — không quy định message empty-search |
| AC: "Given tìm kiếm When nhập từ khóa Then hiển thị kết quả matching" | `srs-v3.5/srs-fr-10-quan-tri.md:170` | Không có kết quả matching → không hiển thị | AC chỉ nói hiện kết quả matching, không nói empty-state |

**Kết luận:** Actual (vùng cây trắng, không message) đối tác quan sát là ĐÚNG và tái hiện được. Đối tác kỳ vọng message "Không tìm thấy mục danh mục phù hợp" — **SRS TPL-DM-CRUD §SEARCH không quy định** message này. Bất đồng ở KỲ VỌNG vs ĐẶC TẢ → `BA confirm` (không Reject vì actual đúng; không Open vì SRS không bắt buộc). BA quyết có bổ sung empty-state message cho tìm kiếm cây đơn vị không.

**Cross-ref:** cùng cụm empty-state với QLTKND_06 (B8 — màn Tài khoản hiện "Trống" thay vì "Không tìm thấy tài khoản phù hợp"). Ở đây (cây đơn vị) còn không hiện cả "Trống". Nghi thiếu empty-state chuẩn ở component tìm kiếm.

## Evidence ảnh
- `reverify-audit/QLDMCQDVQL_05/search-empty-tree.png` — vùng cây trắng sau khi search "tư pháp HCM".
