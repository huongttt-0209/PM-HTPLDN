# BA confirmation needed — QTHT Batch 3 (DM Form Thêm/Sửa nhóm C — "Danh mục cha" + tên trường) — 2026-07-21

> **File này để làm gì:** gom các testcase QA không tự chốt Open được (đối tác kỳ vọng khác SRS hoặc SRS im lặng về chi tiết tranh chấp), kèm đối chiếu SRS + evidence UI để BA quyết. Bug có SRS reference rõ ràng → log vào `bug-reports/bug-report-qtht-batch3.md`.

> **SRS dùng:** v3.5 — `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md`. Template chung: TPL-DM-CRUD (dòng 64–171). Màn: SCR-VIII-01 (dòng 1558).

> **Cụm gốc chung Batch 3:** 8/8 case đều nằm trên form Thêm/Sửa của các tab danh mục **dạng phẳng** (Tiêu chí ĐG chi phí, Loại tài khoản, Loại hình tiếp nhận, Kênh tiếp nhận). Cả 8 form đều render thêm trường **"Danh mục cha"** (tùy chọn) mà SRS TPL-DM-CRUD §Inputs (dòng 78–82) + SCR-VIII-01 modal (rows 11–16, dòng 1577–1582) KHÔNG liệt kê → nghi **1 bug FE gốc chung** (component form danh mục dùng chung render nhầm trường cha cho mọi loại). Riêng 2 case TCDGHTCP (160/161) thêm ý "tên trường bổ sung khác SRS". Vì trường thừa để **tùy chọn, không chặn lưu** và tên field form không được SRS quy định cứng → chuyển **BA confirm** thay vì Open (tránh quote sai clause / prescribe implementation).

---

## QLDMTCDGHTCP_06 & QLDMTCDGHTCP_12 — Form Thêm/Sửa "Tiêu chí đánh giá chi phí": trường "Danh mục cha" thừa + tên 2 trường bổ sung khác SRS

**Bối cảnh testcase**

- Dòng Excel: 160 (`QLDMTCDGHTCP_06` — Thêm mới) và 161 (`QLDMTCDGHTCP_12` — Sửa).
- Nội dung kiểm tra: QTHT mở form Thêm mới / Sửa danh mục ở tab **Tiêu chí đánh giá chi phí** (Quản trị hệ thống → Danh mục dùng chung).
- Expected trong file UAT (đối tác):
  - Form không có trường "Danh mục cha" (danh mục phẳng, không phân cấp).
  - Tên trường bổ sung phải giống thiết kế: không phải "Tỷ lệ phần trăm" / "Mức chi phí tối đa".
- Actual đối tác ghi: form hiển thị thêm "Danh mục cha" và 2 trường tên "Tỷ lệ phần trăm", "Mức chi phí tối đa" (đối tác tô vàng 2 label này).

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Inputs chung (áp dụng cho FR-VIII-12) chỉ có 5 trường: `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường cha**.
- SCR-VIII-01 §Thành phần màn hình, modal CRUD (rows 11–16): Mã, Tên, Mô tả, Thứ tự, Trạng thái, nút Hủy/Lưu — **KHÔNG có trường cha**.
- FR-VIII-12 §Inputs — trường riêng: `quy_mo_dn`, `muc_ho_tro_phan_tram` (VD 100/30/10), `tran_ho_tro_nam` (money, VNĐ/năm) — tên logic, không có "danh_muc_cha".
- SCR-VIII-01 §Thành phần đặc biệt — DM Tiêu chí ĐG Chi phí (row 23): cột bổ sung được đặt tên **"Quy mô DN, Mức hỗ trợ (%), Trần hỗ trợ/năm (VNĐ)"** — khác với label form app ("Tỷ lệ phần trăm", "Mức chi phí tối đa"). Đây là label **cột danh sách**, SRS không quy định riêng label **trường trên form**.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:78-82` (TPL-DM-CRUD §Inputs chung — 5 trường, không có cha)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1577-1582` (SCR-VIII-01 modal CRUD — không có trường cha)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:575-579` (FR-VIII-12 §Inputs trường riêng)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1604` (SCR-VIII-01 §Thành phần đặc biệt UC110 — "Mức hỗ trợ (%)", "Trần hỗ trợ/năm (VNĐ)")

**Kết quả verify UI hiện tại**

- Verify lại 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin` / vai trò QTHT, env `https://18.143.165.120.nip.io`.
- Mở `/quan-tri/danh-muc/TIEU_CHI_DG_CHI_PHI` → nút "Thêm mới" → drawer "Thêm mới danh mục".
- Form (đọc DOM `innerText` + ảnh full-res) có 9 trường: Mã*, Tên*, Mô tả, Thứ tự, **Danh mục cha (không bắt buộc)**, Trạng thái, Quy mô doanh nghiệp*, **Tỷ lệ phần trăm* (%)**, **Mức chi phí tối đa* (VNĐ)**.
- "Danh mục cha" là dropdown "Chọn danh mục cha (tùy chọn)" — **không có dấu `*`, không chặn lưu**. Tab này dạng phẳng, không phân cấp cha-con.
- Tái hiện đúng cả 2 ý đối tác phản ánh. Cùng form dùng cho Thêm (160) và Sửa (161).
- Evidence: `../../reverify-audit/QLDMTCDGHTCP_06/form-them-moi-tcdghtcp.png`, `../../reverify-audit/QLDMTCDGHTCP_06/form-them-moi-tcdghtcp-fields.png`; evidence đối tác `../../partner-evidence/QLDMTCDGHTCP_06.jpg`.

**Kết luận QA**

- Cả 2 ý tái hiện đúng trên web hiện tại — không phải "không tái hiện" (không Reject).
- Ý (1) "Danh mục cha" thừa: SRS §Inputs/modal không liệt kê trường cha cho danh mục phẳng → app thêm là **lệch SRS**, nhưng để **tùy chọn + không chặn lưu** → không phá luồng → chưa đủ mức Open, cần BA chốt có bỏ trường này khỏi danh mục phẳng không.
- Ý (2) tên trường: SRS chỉ đặt tên **cột danh sách** ("Mức hỗ trợ (%)", "Trần hỗ trợ/năm (VNĐ)") + tên **field logic** (snake_case); **không quy định cứng label trường trên form**. App dùng "Tỷ lệ phần trăm"/"Mức chi phí tối đa" — khác cách gọi SRS nhưng SRS không prescribe label form → cần BA chốt có chuẩn hóa theo SRS không.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận cho cụm form danh mục dạng phẳng (áp dụng chung cả Batch 3):

- Trường "Danh mục cha" (tùy chọn) hiện xuất hiện trên form của mọi danh mục phẳng: BA có yêu cầu ẩn/bỏ trường này ở các danh mục không phân cấp (chỉ giữ ở DM Cơ quan đơn vị / Lĩnh vực kinh doanh vốn có cấu trúc cây) hay chấp nhận giữ dạng tùy chọn?
- Với TCDGHTCP: BA có yêu cầu đổi tên 2 trường form về đúng SRS SCR-VIII-01 ("Mức hỗ trợ (%)", "Trần hỗ trợ/năm") hay chấp nhận label hiện tại ("Tỷ lệ phần trăm", "Mức chi phí tối đa")?
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt theo SRS → chuyển **Dev FE**; nếu chấp nhận hiện trạng → cập nhật lại expected của đối tác.

---

## QLDMLTK_06/_12 · QLLHTNHS_06/_12 · QLDMKTNHS_06/_12 — Trường "Danh mục cha" thừa trong form Thêm/Sửa các danh mục phẳng (Loại tài khoản · Loại hình tiếp nhận · Kênh tiếp nhận)

**Bối cảnh testcase**

- Dòng Excel: 162 (`QLDMLTK_06` — Thêm), 163 (`QLDMLTK_12` — Sửa), 175 (`QLLHTNHS_06` — Thêm), 176 (`QLLHTNHS_12` — Sửa), 177 (`QLDMKTNHS_06` — Thêm), 178 (`QLDMKTNHS_12` — Sửa).
- Nội dung kiểm tra: QTHT mở form Thêm mới / Sửa danh mục ở 3 tab **Loại tài khoản**, **Loại hình tiếp nhận**, **Kênh tiếp nhận** (Quản trị hệ thống → Danh mục dùng chung).
- Expected đối tác: form không có trường "Danh mục cha" (các danh mục này dạng phẳng).
- Actual đối tác ghi: form hiển thị thêm trường "Danh mục cha".

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Inputs chung: 5 trường `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường cha**.
- SCR-VIII-01 §Thành phần màn hình modal CRUD (rows 11–16): Mã, Tên, Mô tả, Thứ tự, Trạng thái, nút Hủy/Lưu — **KHÔNG có trường cha**.
- FR-VIII-13 (LTK, UC111), FR-VIII-18 (LHTNHS, UC116), FR-VIII-19 (KTNHS, UC117) §Inputs trường riêng: chỉ thêm `loai_danh_muc` (system) — KHÔNG có "danh_muc_cha". Cả 3 đều là danh mục **phẳng** (không phân cấp cha-con). SRS ghi rõ chỉ DM Cơ quan đơn vị (UC103, Tree View) mới có cấu trúc cây.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:78-82` (TPL-DM-CRUD §Inputs chung)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1577-1582` (SCR-VIII-01 modal CRUD)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:595-599` (FR-VIII-13 LTK)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:863-869` (FR-VIII-18 LHTNHS)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:882-888` (FR-VIII-19 KTNHS)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1584-1590` (SCR-VIII-01 — Tree View chỉ áp cho DM Cơ quan đơn vị)

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin` / QTHT, env `https://18.143.165.120.nip.io`.
- 3 tab đều có sẵn record chuẩn (LTK: CB/NHT/TVV/CG/DN/QTHT; LHTNHS: TRUC_TUYEN…; KTNHS: CONG_DVC…) → mở được cả Thêm và Sửa.
- Cả 6 form (đọc DOM `innerText` + ảnh full-res): trường gồm Mã*, Tên*, Mô tả, Thứ tự, **Danh mục cha (không bắt buộc)**, Trạng thái — không có trường đặc biệt khác. "Danh mục cha" = dropdown "Chọn danh mục cha (tùy chọn)", **không có `*`, không chặn lưu**.
- Tái hiện đúng phản ánh đối tác trên cả 6 case (3 tab × Thêm/Sửa).
- Evidence: `../../reverify-audit/QLDMLTK_06/form-them-moi-ltk.png`, `../../reverify-audit/QLDMLTK_12/form-sua-ltk.png`, `../../reverify-audit/QLLHTNHS_06/form-them-moi-lhtnhs.png`, `../../reverify-audit/QLLHTNHS_12/form-sua-lhtnhs.png`, `../../reverify-audit/QLDMKTNHS_06/form-them-moi-ktnhs.png`, `../../reverify-audit/QLDMKTNHS_12/form-sua-ktnhs.png`; evidence đối tác `../../partner-evidence/QLDMLTK_06.jpg`, `QLDMLTK_11.jpg`, `QLLHTNHS_06.jpg`, `QLLHTNHS_12.jpg`, `QLDMKTNHS_06.jpg`, `QLDMKTNHS_12.jpg`.

**Kết luận QA**

- 6 case tái hiện đúng — không phải "không tái hiện" (không Reject).
- Trường "Danh mục cha" lệch SRS (SRS §Inputs/modal không liệt kê cho danh mục phẳng) nhưng để **tùy chọn + không chặn lưu** → không phá luồng → chưa đủ mức Open. Đây là **1 bug FE gốc chung** (component form danh mục dùng chung render trường cha cho mọi loại), cùng bản chất với cụm TCDGHTCP ở trên.

**Nội dung đề xuất BA phản hồi đối tác**

- Cùng câu hỏi với cụm TCDGHTCP: BA có yêu cầu ẩn/bỏ trường "Danh mục cha" khỏi form của các danh mục phẳng (LTK, LHTNHS, KTNHS và các tab phẳng khác), chỉ giữ ở danh mục cấu trúc cây (Cơ quan đơn vị / Lĩnh vực kinh doanh) hay chấp nhận giữ dạng tùy chọn?
- Verdict QA đề xuất: `Cần BA xác nhận`. Vì nghi 1 bug FE gốc chung xuyên Batch 1·2·3 → nếu BA chốt bỏ, đề nghị **Dev FE** sửa 1 lần ở component form danh mục dùng chung (áp cho mọi tab phẳng).

---
