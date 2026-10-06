# BA confirmation needed — QTHT Batch 6 (Sắp xếp cột + Phân trang) — 2026-07-21

> Gom testcase QA không tự chốt verdict được (SRS silent / kỳ vọng đối tác vượt spec). Kèm đối chiếu SRS + evidence UI để BA quyết nhanh.

---

## QLVT_14 (row 164) — Màn Vai trò không có sắp xếp bằng bấm tiêu đề cột

**Bối cảnh testcase**

- Dòng Excel: 164, mã TC `QLVT_14`.
- Nội dung kiểm tra: QTHT mở màn Vai trò (`/quan-tri/vai-tro`), bấm tiêu đề cột để sắp xếp danh sách.
- Expected trong file UAT:
  - Bấm tên cột thì danh sách sắp xếp lại (luân phiên tăng/giảm).
  - Mặc định sắp theo "Tên vai trò" tăng dần.
- Actual đối tác ghi: không sắp xếp được theo cột.

**Đối chiếu SRS v3.5**

- SCR-VIII-02 (Quản lý Vai trò): cột "Tên vai trò" có cột Hành vi = "—" (không quy định sắp xếp tương tác). Màn này KHÔNG có mục "Quy tắc tương tác" — khác SCR-VIII-01 (Danh mục dùng chung) đã bổ sung click-to-sort cho cột "Tên" theo STT69 UAT 2026-06-02.
- FR-VIII-14 (UC112 — Quản lý vai trò): Acceptance Criteria chỉ nêu "danh sách vai trò, phân trang" — không quy định sắp xếp bằng bấm tiêu đề cột, cũng không nêu rõ tiêu chí sắp mặc định.
- → SRS **silent** về sắp xếp tương tác (click cột) trên màn Vai trò.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1625` (SCR-VIII-02, cột Tên vai trò — Hành vi "—")
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1612` (SCR-VIII-02 — không có §Quy tắc tương tác)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:660` (FR-VIII-14 AC — chỉ "danh sách vai trò, phân trang")
- So sánh: `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1608` (SCR-VIII-01 Danh mục — CÓ click-to-sort cột Tên [STT69])

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin` / QTHT, URL `https://18.143.165.120.nip.io/quan-tri/vai-tro`.
- Danh sách 11 vai trò (CB_NV_BN, CB_NV_DP, CB_NV_TW, CB_PD_BN, CB_PD_DP, CB_PD_TW, CG, DN, NHT, QTHT, TVV).
- Kiểm DOM 8 tiêu đề cột: tất cả không có class sortable, không `aria-sort`, không sorter icon, con trỏ `auto` (không click được). Bấm "Tên vai trò" → URL không đổi, thứ tự không đổi.
- Thứ tự mặc định hiện tại = theo Tên vai trò tăng dần (trùng Mã vai trò tăng dần) → phần "mặc định Tên vai trò↑" của đối tác ĐANG được đáp ứng.
- Evidence: `../../reverify-audit/QLVT_14/vaitro-baseline.png` (web) + `../../partner-evidence/QLVT_14.jpg` (đối tác).

**Kết luận QA**

- `QLVT_14`: đối tác quan sát ĐÚNG thực tế (màn Vai trò không sắp xếp được bằng bấm tiêu đề cột — vì màn này không có chức năng sort tương tác).
- Web hiện tại phù hợp SRS (SRS không quy định click-to-sort cho màn Vai trò). Không phải bug (không vi phạm rule SRS) và cũng không phải điều đối tác báo sai.
- Điểm cần BA: kỳ vọng "click cột để sắp xếp" của đối tác là bổ sung so với SRS — SRS chưa quy định cho màn Vai trò.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận hướng xử lý cho `QLVT_14`:
  - Có bổ sung chức năng bấm tiêu đề cột để sắp xếp cho màn Vai trò (tương tự cột "Tên" ở màn Danh mục dùng chung theo STT69) không?
  - Hay giữ nguyên: màn Vai trò chỉ sắp mặc định (Tên vai trò tăng dần), không có sort tương tác?
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA quyết bổ sung → chuyển Dev FE làm click-to-sort; nếu giữ nguyên → cập nhật expected testcase `QLVT_14` cho khớp SRS (không có click-to-sort).
