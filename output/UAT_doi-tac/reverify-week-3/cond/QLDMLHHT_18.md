# Bảng đối chiếu điều kiện — QLDMLHHT_18 (row 132)

**Case:** Danh mục Loại hình hỗ trợ — click tên cột để sắp xếp.
**Đối tác phản ánh:** Nhấn tên cột KHÔNG sắp xếp.
**Loại bug:** Sắp xếp (data-dependent) → cần bảng đối chiếu.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLDMLHHT_18.webm) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT" góc phải video) | admin / QTHT | Không |
| Entity + trạng thái | DM Loại hình HT, list view, 7 record tên khác nhau | DM Loại hình HT, list view, 6 record tên khác nhau | Không |
| Dữ liệu tiền đề | ≥3 record tên khác nhau (video có 7) | 6 record tên khác nhau (Tư vấn pháp luật, Tham gia tố tụng, Đại diện ngoài tố tụng, Hòa giải, Đào tạo/bồi dưỡng, Trợ giúp khác) — đủ ≥3 | Không |
| Input / filter (cột click) | Click header Tên (frame t012 URL sortBy=ten&sortOrder=DESC) | Click header Tên (URL sortBy=ten ASC→DESC) | Không |

**0 GAP.** Cùng màn, cùng loại data, cùng thao tác, cùng vai trò.

## Kết quả test (real-data, artifact)

- Baseline (không sort): thu_tu ASC — Tư vấn pháp luật(1), Tham gia tố tụng(2), Đại diện ngoài tố tụng(3), Hòa giải(4), Đào tạo/bồi dưỡng(5), Trợ giúp khác(6). Ảnh `reverify-audit/QLDMLHHT_18/baseline-thutu-order.png`.
- Click header **Tên** → `sortBy=ten&sortOrder=ASC`, `aria-sort=ascending`, RE-SORT theo tên tăng: Đại diện ngoài tố tụng, Đào tạo/bồi dưỡng, Hòa giải, Tham gia tố tụng, Trợ giúp khác, Tư vấn pháp luật (cột Thứ tự lộn xộn → sort theo ten). Ảnh `ten-asc.png`.
- Click **Tên** lần 2 → `sortBy=ten&sortOrder=DESC`, `aria-sort=descending`, đảo ngược: Tư vấn pháp luật, Trợ giúp khác, Tham gia tố tụng, Hòa giải, Đào tạo/bồi dưỡng, Đại diện ngoài tố tụng. Tooltip "Nhấp để hủy sắp xếp". Ảnh `ten-desc.png`.

→ Sort theo cột Tên hoạt động đúng, luân phiên ASC↔DESC. Khớp SRS SCR-VIII-01 (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` + `:1608`). Chỉ cột Tên có mũi tên sort (đúng STT69).

**Lỗi đối tác báo KHÔNG tái hiện.** → Reject + đối tác kiểm tra lại (nghi build cũ chưa fix — cùng triệu chứng với QLDMLVPL_21).
