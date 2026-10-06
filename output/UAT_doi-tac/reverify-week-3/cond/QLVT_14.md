# Bảng đối chiếu điều kiện — QLVT_14 (row 164)

**Case:** Màn Vai trò (SCR-VIII-02) — click tên cột để sắp xếp.
**Đối tác phản ánh:** KHÔNG sắp xếp theo cột (kỳ vọng mặc định Tên vai trò↑).
**Loại:** Sắp xếp — nhưng finding là "không có control sort" (thuộc tính UI tĩnh, không phụ thuộc data). Vẫn điền bảng để chứng minh reproduce đúng điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLVT_14.jpg) | Mình test (18.143.165.120.nip.io, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT" góc phải ảnh) | admin / QTHT | Không |
| Entity + trạng thái | Màn Vai trò `/quan-tri/vai-tro`, list 10+ vai trò | Màn Vai trò `/quan-tri/vai-tro`, list 11 vai trò | Không |
| Dữ liệu tiền đề | ≥3 vai trò tên khác nhau (ảnh có 10) | 11 vai trò tên khác nhau (CB_NV_BN…TVV) — đủ ≥3 | Không |
| Input / filter (thao tác) | Kỳ vọng click header cột để sort | Click header "Tên vai trò" → không đổi | Không |

**0 GAP.** Cùng màn, cùng vai trò QTHT, cùng loại data.

## Kết quả test (real-data, artifact)

- Kiểm DOM 8 header màn Vai trò (Mã vai trò / Tên vai trò / Mô tả / Số tài khoản / Số quyền / Cấp / Trạng thái / Hành động): TẤT CẢ `ant-table-column-has-sorters=false`, `aria-sort=null`, không có sorter icon, `cursor:auto` → **không cột nào sortable**.
- Click header "Tên vai trò": URL không đổi (`/quan-tri/vai-tro`, không thêm sortBy), thứ tự không đổi (CB_NV_BN, CB_NV_DP, CB_NV_TW, CB_PD_BN, CB_PD_DP, CB_PD_TW, CG, DN, NHT, QTHT, TVV giữ nguyên). Ảnh `reverify-audit/QLVT_14/vaitro-baseline.png`.
- Thứ tự mặc định hiện tại = theo Mã vai trò↑ (trùng Tên vai trò↑ do mã & tên đồng biến) → phần "mặc định Tên vai trò↑" của đối tác ĐANG được đáp ứng.

## Đối chiếu SRS
- SRS SCR-VIII-02 (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1625`): cột "Tên vai trò" cột Hành vi = "—" (không sort). SCR-VIII-02 KHÔNG có §Quy tắc tương tác (khác SCR-VIII-01 Danh mục dòng 1606-1608 có click-to-sort cột Tên [STT69]).
- FR-VIII-14 (`:660-663`): AC chỉ nêu "danh sách vai trò, phân trang" — không quy định click-to-sort.
→ SRS **silent** về sắp xếp tương tác click cột trên màn Vai trò.

## Kết luận
Đối tác quan sát ĐÚNG (không sort được theo cột — vì màn này không có control sort), nhưng kỳ vọng click-to-sort **KHÔNG được SRS SCR-VIII-02 quy định**. Bất đồng về ĐẶC TẢ (SRS silent) → **BA confirm**: BA quyết có bổ sung click-to-sort cho màn Vai trò (giống cột Tên màn Danh mục) hay giữ nguyên. QA KHÔNG tự Reject (đối tác quan sát đúng thực tế) và KHÔNG phải Open (không vi phạm rule SRS nào).
