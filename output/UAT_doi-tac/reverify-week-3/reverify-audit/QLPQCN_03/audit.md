# Audit — QLPQCN_03 (row 174) — Verdict: BA confirm

**Đối tác báo:** Ma trận phân quyền KHÔNG hiển thị theo "Cây chức năng" (danh sách cây).

**Evidence đối tác đã xem:** `partner-evidence/QLPQCN_03.webm` (MD5 `ea8a0be3…`, ~34s; TRÙNG file QLPQCN_02 — đối tác dùng chung 1 video cho 2 case).
- Frame web: màn "Phân quyền vai trò", quyền theo panel module dạng danh sách quyền chi tiết, không phải ma trận cây × cột hành động.
- Frame spec doc `HTPLDN-PTYC-CT-v2.0.docx` §4.10.4.2: "Cây chức năng (cột trái) | Danh sách cây | Danh sách các nhóm chức năng tổ chức theo cây phân cấp".

**3 dữ kiện neo:**
- (a) URL đối tác `/quan-tri/vai-tro/ff22d33f-.../quyen-han`.
- (b) State: quyền render theo panel module (Báo cáo/BIEU_MAU/Chi trả), mỗi quyền 1 checkbox — không có ma trận 6 cột.
- (c) Tiền đề: vai trò có quyền để hiển thị.

**Verify web (env mình) 2026-07-21, admin/QTHT:**
- `https://18.143.165.120.nip.io/quan-tri/vai-tro/aaaaaaaa-0000-4000-8000-000000000010/quyen-han` (CB_NV_DP).
- Đo DOM: `hasActionColumns` = false toàn bộ (không có cột Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất). Quyền nhóm theo module ("Báo cáo 11 quyền", "BIEU_MAU 10 quyền"…) dạng collapse panel + quyền chi tiết có tên. 612 checkbox.
- Screenshot: `quyen-han-grouped-list.png`.

**Đối chiếu SRS (Cổng 3):**
- SCR-VIII-04 §Thành phần body (`srs-fr-10-quan-tri.md:1689-1694`): "Cây menu (cột trái) tree" + 6 cột `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất` → web KHÔNG theo layout này.
- CHANGELOG Pha 5 (`CHANGELOG-v3-to-v3.5.md:3246,3262,3270,3304`, BA+PM chốt 2026-05-08): redesign "ma trận 6 cột → 1 vùng panel theo module"; UI render panel theo `module_code`; 218 quyền / 12 module (BAO_CAO, BIEU_MAU, CHI_TRA…) → web KHỚP CHÍNH XÁC bản redesign này.
- **Mâu thuẫn nội bộ SRS** (body ma trận 6 cột vs changelog panel-theo-module). Web đúng bản redesign, kỳ vọng đối tác theo bản cũ → verdict `BA confirm`. Chi tiết + câu hỏi BA: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch9.md`.
