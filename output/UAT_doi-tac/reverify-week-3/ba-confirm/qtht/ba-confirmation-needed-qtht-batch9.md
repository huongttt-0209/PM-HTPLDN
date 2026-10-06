# BA confirmation needed — QTHT Batch 9 (Phân quyền chức năng — SCR-VIII-04) — 2026-07-21

> **File này để làm gì:** gom testcase QA không tự chốt verdict được vì **SRS tự mâu thuẫn** (body SCR-VIII-04 vs CHANGELOG Pha 5 redesign), kèm đối chiếu + evidence để BA quyết + phản hồi đối tác.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` — đã mở file verify số dòng thực. SRS v3.5 (`input/srs-update-2026-5-5/`).

---

## QLPQCN_02 (và QLPQCN_03) — Màn "Phân quyền chức năng" (SCR-VIII-04): app theo bản redesign panel-theo-module, còn body SRS + kỳ vọng đối tác theo ma trận 6 cột cũ

**Bối cảnh testcase**

- Dòng Excel: 173, mã TC `QLPQCN_02` — đối tác phản ánh màn KHÔNG hiển thị **Bộ chọn vai trò** (kỳ vọng: chọn vai trò → tải ma trận quyền).
- Dòng Excel: 174, mã TC `QLPQCN_03` — đối tác phản ánh ma trận phân quyền KHÔNG hiển thị theo **Cây chức năng** (danh sách cây).
- Nội dung kiểm tra: QTHT mở màn Phân quyền chức năng của 1 vai trò (`/quan-tri/vai-tro/{id}/quyen-han`).
- Expected trong file UAT (đối tác): màn có dropdown "Bộ chọn vai trò" + ma trận quyền tổ chức theo cây chức năng phân cấp với các cột hành động. Đối tác dẫn chứng spec doc `HTPLDN-PTYC-CT-v2.0` §4.10.4.2 (ma trận Phân quyền Chức năng theo Vai trò: Bộ chọn vai trò = Danh sách chọn; Cây chức năng cột trái = Danh sách cây).

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `admin` (vai trò QTHT). Mở `https://18.143.165.120.nip.io/quan-tri/vai-tro/aaaaaaaa-0000-4000-8000-000000000010/quyen-han` (vai trò "Cán bộ Nghiệp vụ Địa phương").
- Màn tiêu đề "Phân quyền vai trò". Quyền hiển thị dạng **collapse panel theo module**: "Báo cáo (11 quyền)", "BIEU_MAU (10 quyền)", "Chi trả (16 quyền)"… — mỗi panel có checkbox nhóm + expand ra danh sách **quyền chi tiết có tên** (Cập nhật báo cáo `update_bao_cao`, Duyệt báo cáo `approve_bao_cao`, Xem bảng điều khiển `read_dashboard`, Công khai thư mục biểu mẫu `publish_thu_muc_bieu_mau`…), mỗi quyền 1 checkbox.
- Đo DOM: `selects: []` → **không có dropdown/bộ chọn vai trò** nào trên màn (vai trò chọn qua điều hướng từ danh sách Vai trò). Không có cột `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất` (`hasActionColumns` = false toàn bộ). 612 checkbox, nút "Quay lại" + "Lưu".
- Env đối tác (`ospgroup.vn`, video QLPQCN_02/03.webm) render **giống hệt**: cùng panel-theo-module, cùng không có dropdown vai trò.
- Evidence: `../../reverify-audit/QLPQCN_02/quyen-han-screen.png`, `../../reverify-audit/QLPQCN_03/quyen-han-grouped-list.png`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-VIII-04 §Thành phần màn hình (body SRS)** — màn là **ma trận 6 cột**:
   - Toolbar có "Dropdown vai trò" (select) — luôn hiển thị.
   - Content "Cây menu (cột trái)" (tree) + 6 cột checkbox `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất`.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1688` (Dropdown vai trò | select | luôn hiển thị)
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1689` (Cây menu cột trái | tree | Phân cấp module)
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1690-1694` (6 cột hành động)

2. Nhưng **CHANGELOG-v3-to-v3.5 §Pha 5 "Tái thiết kế Phân quyền chức năng" (2026-05-08, ✅ BA + PM chốt)** đã **redesign** SCR-VIII-04 sang **1 vùng panel theo module** (bỏ ma trận 6 cột):
   - "SCR-VIII-04 dùng **1 vùng duy nhất** — danh sách collapse panel theo module. Mỗi panel chứa block CRUD compact (6 checkbox) + block đặc thù dọc (các quyền workflow theo 9 nhóm verb)."
   - QUYEN_HAN thêm `module_code`/`module_name` → "UI render panel theo `module_code`, không parse prefix `ma_quyen`". 218 quyền chia **12 module** (BAO_CAO, BIEU_MAU, CHI_TRA, HOI_DAP, DAO_TAO, VU_VIEC, DANH_GIA, QUAN_TRI, TVCS, TV_NHANH, CT_HTPL, TVV_CG).
   - Tổng kết: "1 SCR redesign hoàn chỉnh (SCR-VIII-04: **ma trận 6 cột → 1 vùng panel theo module**)".

   Citation:
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3246` (1 vùng collapse panel theo module)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3262` (UI render panel theo module_code)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3270` (218 quyền / 12 module)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3304` (ma trận 6 cột → 1 vùng panel theo module)

   → **Body SCR-VIII-04 §Thành phần chưa được đồng bộ với bản redesign đã chốt trong changelog** (cả 3 bản srs-fr-10: input v3.5, Docs v3.5, Docs v4 đều còn giữ ma trận 6 cột). Web hiện tại render **đúng bản redesign panel-theo-module** (khớp `module_code` + 12 module + quyền chi tiết), KHÔNG khớp ma trận 6 cột.

**Câu hỏi cần BA xác nhận**

Màn "Phân quyền chức năng" (SCR-VIII-04) cần theo bản nào?

1. **Hướng 1 — theo body SCR-VIII-04 (ma trận 6 cột cũ):** cần dropdown "Bộ chọn vai trò" trên màn + ma trận cây chức năng × 6 cột `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất`. → Web hiện tại **sai thiết kế**, kỳ vọng đối tác **đúng**.
2. **Hướng 2 — theo CHANGELOG Pha 5 redesign (panel theo module, đã BA+PM chốt 2026-05-08):** 1 vùng collapse panel theo module với quyền chi tiết; chọn vai trò qua điều hướng danh sách. → Web hiện tại **đúng bản redesign**, kỳ vọng đối tác (ma trận 6 cột) **dựa trên thiết kế cũ đã bị thay**, cần cập nhật body SRS + báo đối tác.

- Riêng `QLPQCN_02` (không có dropdown vai trò): kể cả theo Hướng 2, changelog chỉ mô tả lại vùng hiển thị quyền, chưa nêu rõ có bỏ dropdown vai trò hay không → BA xác nhận màn redesign có cần dropdown chọn vai trò không, hay chọn vai trò qua điều hướng danh sách là chấp nhận được.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `QLPQCN_02` và `QLPQCN_03`: `BA confirm`.
- **QA nghiêng Hướng 2:** CHANGELOG Pha 5 là quyết định BA+PM sau cùng (2026-05-08, trạng thái "✅ chốt"), thứ bậc `BA duyệt > expected đối tác`. Web đang khớp bản redesign này (panel theo `module_code`, 12 module, quyền chi tiết) → nhiều khả năng web ĐÚNG, kỳ vọng đối tác dựa trên ma trận 6 cột đã bị thay. Nếu BA chọn Hướng 2: cần (a) cập nhật body SCR-VIII-04 §Thành phần cho khớp changelog, (b) phản hồi đối tác rằng thiết kế màn đã đổi sang panel-theo-module, cập nhật lại expected của QLPQCN_02/03.
- Nếu BA chọn Hướng 1: web `Vẫn lỗi`, owner `Dev FE` (dựng lại dropdown vai trò + ma trận 6 cột).

**Quan sát thêm (cùng cụm SCR-VIII-04, để BA cân nhắc chung — QA chưa mở dòng bug riêng vì phụ thuộc cùng 1 quyết định source-truth):**
- Màn `/quyen-han` chỉ có nút "Quay lại" + "Lưu", **không có nút "Reset về mặc định"** (body SCR-VIII-04 comp 10 `srs-fr-10-quan-tri.md:1696`; spec doc đối tác cũng có "Khôi phục về mặc định"). Nếu BA chốt Hướng 1 → thiếu nút này là lỗi; nếu Hướng 2 → cần xác nhận bản redesign có giữ nút Reset không.

