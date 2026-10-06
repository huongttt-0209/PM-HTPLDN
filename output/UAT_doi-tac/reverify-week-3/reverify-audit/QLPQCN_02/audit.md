# Audit — QLPQCN_02 (row 173) — Verdict: BA confirm

**Đối tác báo:** Màn Phân quyền chức năng KHÔNG hiển thị "Bộ chọn vai trò" (kỳ vọng: chọn vai trò → tải ma trận quyền).

**Evidence đối tác đã xem:** `partner-evidence/QLPQCN_02.webm` (MD5 `ea8a0be3…`, ~34s; trùng file QLPQCN_03).
- Frame ~0-6s: web `htpldn-uat.ospgroup.vn/quan-tri/vai-tro/ff22d33f-.../quyen-han`, màn "Phân quyền vai trò", quyền theo panel module (Báo cáo/BIEU_MAU/Chi trả), KHÔNG có dropdown vai trò ở đầu màn.
- Frame ~9-34s: đối tác chiếu spec doc `HTPLDN-PTYC-CT-v2.0.docx` §4.10.4.2 — "Bộ chọn vai trò" (Danh sách chọn) + "Cây chức năng (cột trái)".

**3 dữ kiện neo:**
- (a) URL đối tác `/quan-tri/vai-tro/ff22d33f-1936-4f0a-8334-ab50f4eb49b2/quyen-han`, vai trò "Chuyên viên kiểm thử tkm".
- (b) State: màn đã load quyền của vai trò (panel module có checkbox); không có dropdown chọn vai trò trên màn.
- (c) Tiền đề: vai trò tồn tại (đủ để tải quyền).

**Verify web (env mình) 2026-07-21, admin/QTHT:**
- `https://18.143.165.120.nip.io/quan-tri/vai-tro/aaaaaaaa-0000-4000-8000-000000000010/quyen-han` (vai trò CB_NV_DP).
- Đo DOM: `selects: []` — không có dropdown/bộ chọn vai trò trên màn. Vai trò chọn qua điều hướng từ danh sách Vai trò → link "Số quyền" → `/quyen-han`.
- Quyền hiển thị collapse panel theo module + quyền chi tiết có tên, mỗi quyền 1 checkbox.
- Env đối tác render giống hệt.
- Screenshot: `quyen-han-screen.png`.

**Đối chiếu SRS (Cổng 3):**
- SCR-VIII-04 §Thành phần body (`srs-fr-10-quan-tri.md:1688`): "Dropdown vai trò | select | luôn hiển thị" → web KHÔNG có.
- CHANGELOG Pha 5 (`CHANGELOG-v3-to-v3.5.md:3246,3304`, BA+PM chốt 2026-05-08): redesign "ma trận 6 cột → 1 vùng panel theo module" → web KHỚP bản redesign.
- **Mâu thuẫn nội bộ SRS** (body vs changelog) → verdict `BA confirm`. Chi tiết + câu hỏi BA: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch9.md`.
