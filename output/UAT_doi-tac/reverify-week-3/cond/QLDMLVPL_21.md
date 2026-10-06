# Bảng đối chiếu điều kiện — QLDMLVPL_21 (row 127)

**Case:** Danh mục Lĩnh vực pháp lý — click tên cột để sắp xếp.
**Đối tác phản ánh:** Nhấn tên cột KHÔNG sắp xếp (kỳ vọng luân phiên tăng/giảm; mặc định Thứ tự↑ rồi Tên↑).
**Loại bug:** Sắp xếp (data-dependent) → cần bảng đối chiếu.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res QLDMLVPL_21.webm) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT" góc phải video) | admin / QTHT | Không |
| Entity + trạng thái | DM Lĩnh vực PL, list view, 11 record tên khác nhau | DM Lĩnh vực PL, list view, 10 record tên khác nhau | Không |
| Dữ liệu tiền đề | ≥3 record tên khác nhau để thấy đổi thứ tự khi sort (video có 11) | 10 record tên khác nhau (Thuế, Lao động, Đất đai... Đầu tư) — đủ ≥3 | Không |
| Input / filter (cột click) | Click header Tên (URL sortBy=ten&sortOrder=DESC ở frame t010) | Click header Tên (URL sortBy=ten&sortOrder=ASC→DESC) | Không |

**0 GAP.** Đã tái hiện đúng điều kiện đối tác (cùng màn, cùng loại data, cùng thao tác click header Tên, cùng vai trò QTHT).

## Kết quả test (real-data, artifact)

- Baseline (không sort): thứ tự theo Thứ tự tăng — Thuế(1), Lao động(2), Đất đai(3)... Đầu tư(10). Ảnh `reverify-audit/QLDMLVPL_21/baseline-thutu-order.png`.
- Click header **Tên** lần 1 → `sortBy=ten&sortOrder=ASC`, `aria-sort=ascending`, bảng RE-SORT theo tên tăng: Dân sự, Doanh nghiệp, Đất đai, Đầu tư, Hành chính, Hình sự, Lao động, Sở hữu trí tuệ, Thuế, Thương mại (cột Thứ tự lộn xộn 4,9,3,10,7,6,2,8,1,5 → chứng minh sort theo ten). Ảnh `ten-asc.png`.
- Click header **Tên** lần 2 → `sortBy=ten&sortOrder=DESC`, `aria-sort=descending`, đảo ngược: Thương mại, Thuế, Sở hữu trí tuệ, Lao động, Hình sự, Hành chính, Đầu tư, Đất đai, Doanh nghiệp, Dân sự. Tooltip "Nhấp để hủy sắp xếp" (click lần 3 → về mặc định). Ảnh `ten-desc.png`.

→ Sort theo cột Tên hoạt động đúng, luân phiên ASC↔DESC, DOM thực sự đổi thứ tự. Khớp SRS SCR-VIII-01 (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` + `:1608`): chỉ cột Tên cho sort tương tác `ten` ASC↔DESC; các cột Mã/Mô tả/Thứ tự không sortable (env này đúng — chỉ Tên có mũi tên sort).

**Lỗi đối tác báo (click tên cột không sắp xếp) KHÔNG tái hiện trên env được giao.** → Reject + đối tác kiểm tra lại (nghi env/build cũ của đối tác — frame t010 cho thấy URL đổi sortBy=ten nhưng data vẫn thứ tự thu_tu, tức build cũ chưa fix; build hiện tại đã fix).
