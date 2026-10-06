# Audit — QLVT_14 (row 164) — BA confirm

**Verdict:** BA confirm. Verify 21/07/2026, Chrome DevTools MCP, `admin`/QTHT, env `18.143.165.120.nip.io`.

## Evidence đối tác đã xem
- File: `partner-evidence/QLVT_14.jpg` (ảnh tĩnh, env `htpldn-uat.ospgroup.vn`, clock 14/07/2026).
- Nội dung: màn Vai trò `/quan-tri/vai-tro`, list 10 vai trò (CB_NV_BN…QTHT), cột Mã vai trò / Tên vai trò / Mô tả / Số tài khoản / Số quyền / Cấp. Ảnh tĩnh không thể hiện thao tác click — chỉ minh hoạ màn.

## Đối tác phản ánh
KHÔNG sắp xếp theo cột (kỳ vọng mặc định Tên vai trò↑ + click cột để sort).

## Kết quả verify web hiện tại (real-data)
- 11 vai trò (CB_NV_BN…TVV). Thứ tự mặc định theo Tên vai trò↑ (= Mã↑) → phần mặc định đáp ứng.
- DOM 8 header: không sortable (has-sorters=false, aria-sort=null, no sorter icon, cursor auto). Click "Tên vai trò" → URL + thứ tự KHÔNG đổi. `vaitro-baseline.png`.

## SRS line
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1625` — SCR-VIII-02 cột Tên vai trò Hành vi "—".
- `:1612` — SCR-VIII-02 không có §Quy tắc tương tác.
- `:660` — FR-VIII-14 AC chỉ "danh sách vai trò, phân trang".
- So sánh `:1608` — SCR-VIII-01 Danh mục CÓ click-to-sort cột Tên [STT69].
→ SRS silent về click-to-sort màn Vai trò.

## Kết luận
Đối tác quan sát đúng (không sort được), nhưng SRS không quy định click-to-sort cho màn Vai trò → bất đồng về đặc tả (SRS silent) → BA confirm. Không Reject (đối tác đúng thực tế), không Open (không vi phạm SRS). File BA: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch6.md`.
