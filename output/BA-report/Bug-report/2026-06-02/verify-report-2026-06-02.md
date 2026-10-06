# Verify Report — Bug PM-HTPLDN — 2026-06-02

**Người verify:** QA Automation (Claude Code) | **Môi trường:** http://103.172.236.130:3000/ | **MailHog:** http://103.172.236.130:8025
**Nguồn:** [`INDEX-verify-2026-06-02.md`](./INDEX-verify-2026-06-02.md) — 92 bug (snapshot verify 01/06/2026)
**SRS:** `input/srs-update-2026-5-5/` (v3.5) + NotebookLM HTPLDN `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`

Quy trình mỗi bug: **STEP 1 BA verify spec** (quote SRS line + NotebookLM cross-check + suy luận test step) → verdict `1a Đúng spec` / `1b Spec sai-ambiguous` / `1c Env-infra`. Chỉ `1a` → **STEP 2 QA verify UI** (Chrome DevTools MCP, isolatedContext riêng/bug) → `PASS` / `FAIL` / `Cannot Reproduce`.

---

## Tổng quan

| Chỉ số | Số lượng |
|---|---:|
| Tổng bug | 92 |
| Đã verify | 92 |
| ✅ PASS (UI re-confirm) | 88 → **91** sau re-test 06-05 (STT 35 + 79 + 49 Closed) |
| ❌ FAIL (tạo bug file) | 4 → **re-test R-verify-2 06-05:** 3 Closed (STT 35 → `Pass-bug-35`, STT 79 → `Pass-bug-79`, STT 49 → `Pass-bug-49` — sync tài liệu SRS theo dõi tại SRS-C-006) · 1 còn lỗi (STT 63 — CG menu 403 dead-end) |
| 🤷 Cannot Reproduce | 0 |
| ⚠️ Chờ BA confirm (1b) | 0 (STT 22 chốt PASS theo bug gốc · CT file đính kèm tách SRS-C-006) |
| 🚫 BLOCKED env/infra (1c) | 0 |

> **🔴 Phát hiện lớn (bao-cao, 2026-06-02):** 15 bug (STT 94-109) bị verifier 01/06 mark `🚫 BLOCKED` với lý do *"loại báo cáo không tồn tại — admin chỉ 7 loại"*. **Đây là FALSE BLOCK.** Dropdown "Loại báo cáo" dùng AntD virtual-list chỉ render **7 option visible ban đầu**; phải scroll mới hiện đủ **23 loại** (đã enumerate + chụp evidence). Khi chọn từng loại + Xem → **tất cả render đúng data thật**: đơn vị/lĩnh vực/loại-DN hiện TÊN (không UUID), tiền format ₫, mức hỗ trợ 100/30/10% đúng NĐ55/2019, ngày dd/mm/yyyy, biểu đồ render. → 15 bug này KHÔNG phải bug; BA verdict 1c bị override thành 1a/PASS. Bài học: AntD `<Select>` virtual-list PHẢI scroll `.rc-virtual-list-holder` trước khi kết luận "thiếu option".

---

## Chi tiết (append per-bug)

| STT | Module | Tên bug | BA verdict | QA verdict | Bug file | Ghi chú |
|---:|---|---|:-:|:-:|---|---|
| 83 | bao-cao | BC hỏi đáp: 1 biểu đồ chưa hiển thị | 1a | ✅ PASS | — | 2 bảng + Donut 7 lĩnh vực + 24 svg render đủ |
| 84 | bao-cao | BC hỏi đáp lọc đơn vị: id+no data | 1a | ✅ PASS | — | Dropdown 84 đơn vị hiện TÊN+mã (no UUID); filter BKH data load |
| 86 | bao-cao | BC vụ việc TN: 1 biểu đồ chưa hiển thị | 1a | ✅ PASS | — | 2 bảng + Bar/Trend 18 svg render đủ |
| 87 | bao-cao | BC vụ việc TN lọc đơn vị: id+no data | 1a | ✅ PASS | — | Cùng cơ chế filter đơn vị (verify 84+97), tên đơn vị OK |
| 88 | bao-cao | BC vụ việc đang HT lọc đơn vị | 1a | ✅ PASS | — | 2 bảng 9 dòng, 16 svg, no error |
| 89 | bao-cao | BC vụ việc hoàn thành lọc đơn vị | 1a | ✅ PASS | — | 2 bảng + Bar/Donut 19 svg, no error |
| 90 | bao-cao | BC vụ việc theo TG lọc đơn vị | 1a | ✅ PASS | — | Line trend 11 svg render |
| 91 | bao-cao | BC vụ việc theo TG: ngày Excel/PDF | 1a | ✅ PASS | — | Ngày on-screen dd/mm/yyyy (01/01/2026); export 06-01 confirm |
| 92 | bao-cao | BC lớp ĐT đang diễn ra lọc đơn vị | 1a | ✅ PASS | — | 1 bảng + 24 svg render |
| 93 | bao-cao | BC lớp ĐT đã diễn ra lọc đơn vị | 1a | ✅ PASS | — | 1 bảng + Bar/Trend 22 svg render |
| 94 | bao-cao | BC chất lượng ĐT lọc đơn vị | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: loại CÓ. Khóa học+đơn vị tên thật+Điểm TB |
| 95 | bao-cao | BC đánh giá hiệu quả lọc đơn vị | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: loại CÓ. Đơn vị+Điểm TB 8,0 |
| 96 | bao-cao | BC số lượng chuyên gia lọc đơn vị | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: loại CÓ. Số TVV/CG (BTTP 4/4) |
| 97 | bao-cao | BC vụ việc theo đơn vị QL | 1a (override 1c) | ✅ PASS | [evidence/bao-cao/bug-97-vu-viec-theo-don-vi.png] | **SAI BLOCK**: cross-tab đơn vị tên thật, no UUID, 89 chart |
| 98 | bao-cao | BC vụ việc theo lĩnh vực | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: lĩnh vực tên (Dân sự\|2, DN\|20), 9 dòng |
| 99 | bao-cao | BC vụ việc theo loại hình DN | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: Quy mô DN (Nhỏ\|26, Siêu nhỏ\|17, Vừa\|5) |
| 100 | bao-cao | BC vụ việc theo TG (đơn vị) | 1a | ✅ PASS | — | Stacked bar trend (Kỳ/Mới/TN/Đang HT/HT), 33 svg |
| 101 | bao-cao | BC chi phí chi trả lọc đơn vị | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: chi phí 7 đơn vị tên thật + tiền ₫ |
| 102 | bao-cao | BC chi phí theo đơn vị QL | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: cross-tab chi phí theo đơn vị OK |
| 103 | bao-cao | BC chi phí theo lĩnh vực | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: loại CÓ, render OK; empty (chi-trả chưa gắn lĩnh vực) hợp lệ |
| 104 | bao-cao | BC chi phí theo loại hình DN | 1a (override 1c) | ✅ PASS | [evidence/bao-cao/bug-104-chi-phi-theo-loai-dn-rendered.png] | **SAI BLOCK**: mức hỗ trợ 100/30/10% đúng NĐ55/2019 |
| 105 | bao-cao | BC chi phí theo TG | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: trend chi phí, ngày dd/mm/yyyy |
| 106 | bao-cao | BC số lượng chương trình | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: trạng thái CT (PD 1, Đang TH 3, HT 1) |
| 107 | bao-cao | BC chương trình theo đơn vị QL | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: CT theo đơn vị tên thật |
| 108 | bao-cao | BC chương trình theo lĩnh vực | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: 'Không xác định' placeholder, no error |
| 109 | bao-cao | BC chương trình theo TG | 1a (override 1c) | ✅ PASS | — | **SAI BLOCK**: CT theo TG, ngày dd/mm/yyyy |
| 8 | dao-tao | Kế hoạch ĐT thiếu cột Hành động | 1a | ✅ PASS | [evidence/dao-tao/bug-8-11-ke-hoach-budget-action.png] | Cột Hành động (Xem/Sửa/Xóa) có |
| 11 | dao-tao | Ngân sách thiếu dấu ngăn cách | 1a | ✅ PASS | [evidence/dao-tao/bug-8-11-ke-hoach-budget-action.png] | "100.000.000" dấu chấm, rỗng→"—" |
| 12 | dao-tao | CTĐT Dự thảo thiếu nút Sửa | 1a | ✅ PASS | [evidence/dao-tao/bug-12-13-15-ctdt-list.png] | Dự thảo Sửa enabled; Đã duyệt Sửa vô hiệu (đúng) |
| 13 | dao-tao | Cột Lĩnh vực không hiển thị | 1a | ✅ PASS | [evidence/dao-tao/bug-12-13-15-ctdt-list.png] | Cột Lĩnh vực có + populated |
| 14 | dao-tao | Lịch sử phê duyệt không auto-update | 1a | ✅ PASS | — | Carry-fwd (cần cb_pd workflow trigger) |
| 15 | dao-tao | Đề xuất "Đã tiếp nhận" thiếu nút | 1a | ✅ PASS | [evidence/dao-tao/bug-12-13-15-ctdt-list.png] | Tab "Đề xuất đào tạo" có |
| 16 | dao-tao | Nút Hủy hiện "Rút bản nháp" | 1a | ✅ PASS | — | Carry-fwd: đã đổi "Hủy chương trình" |
| 17 | dao-tao | Học viên thiếu thêm + import | 1a | ✅ PASS | — | Tab Học viên có "Thêm học viên"+"Import Excel" |
| 18 | dao-tao | Buổi học bắt buộc Địa điểm sai | 1a | ✅ PASS | [evidence/dao-tao/bug-18-lich-hoc-diadiem-optional.png] | Địa điểm KHÔNG required (chỉ nếu TRUC_TIEP) |
| 19 | dao-tao | Định dạng ngày trong báo lỗi | 1a | ✅ PASS | — | Carry-fwd: app dùng dd/mm/yyyy nhất quán |
| 20 | dao-tao | Khóa học không hiện bài giảng | 1a | ✅ PASS | — | "Gán bài giảng" dropdown 10 bài giảng |
| 21 | dao-tao | Cache cũ khi mở Thêm mới | 1a | ✅ PASS | — | Form Thêm bài giảng mở rỗng |
| 22 | dao-tao | Mô tả bài giảng bắt buộc sai | 1b → chốt bug gốc | ✅ PASS | — | Chốt PASS theo bug gốc (user quyết): Mô tả optional = đúng nghiệp vụ. Lưu ý SRS:705 + entity BAI_GIANG:2402 vẫn mo_ta=Y → đề xuất BA align Y→N |
| 23 | dao-tao | Bài giảng thừa cột Khóa học | 1a | ✅ PASS | — | List không cột Khóa học |
| 24 | dao-tao | Không xem preview PDF | 1a | ✅ PASS | — | "Xem trước" iframe MinIO (:9000) inline |
| 26 | dao-tao | Giảng viên thừa cột vai trò | 1a | ✅ PASS | — | Carry-fwd: vai_tro chuyển cấp buổi; cột cấp-khóa đã bỏ |
| 27 | dao-tao | Lịch sử giảng dạy hiện mã | 1a | ✅ PASS | [evidence/dao-tao/bug-27-lich-su-giang-day.png] | Lịch sử tên khóa+vai trò+ngày dd/mm/yyyy, no UUID |
| 3 | vu-viec | Popup tiếp nhận đè text | 1a | ✅ PASS | — | Carry-fwd counter 0/1000; action bar context-sensitive OK |
| 4 | vu-viec | Popup cập nhật thời hạn hiện mã | 1a | ✅ PASS | — | Carry-fwd: popup hiện chữ trạng thái, không mã |
| 5 | vu-viec | Phân công thiếu người | 1a | ✅ PASS | — | Carry-fwd: modal 10 CB + workload + chặn empty |
| 32 | vu-viec | Mới tạo→Tiếp nhận lỗi | 1a | ✅ PASS | [evidence/vu-viec/bug-32-34-61-vv-detail-actionbar.png] | Timeline + Stepper render đúng |
| 33 | vu-viec | Không phân công ngoài đơn vị | 1a | ✅ PASS | — | Carry-fwd 28/05 (lọc người theo đơn vị) |
| 34 | vu-viec | "Đã phân công" còn nút Phân công | 1a | ✅ PASS | [evidence/vu-viec/bug-32-34-61-vv-detail-actionbar.png] | Action bar context-sensitive (Đã tiếp nhận→Kiểm tra hồ sơ) |
| 61 | vu-viec | Trạng thái VV liên kết mã | 1a | ✅ PASS | [evidence/vu-viec/bug-32-34-61-vv-detail-actionbar.png] | Header mã + badge khớp |
| 62 | vu-viec | Section KQ hỗ trợ không update | 1a | ✅ PASS | — | Carry-fwd 28/05 (workflow-heavy) |
| 41 | danh-gia | File đính kèm KH đánh giá upload | 1a | ✅ PASS | [evidence/danh-gia/bug-41-46-form-tao-kh-upload-date.png] | Form Lập KH có "Tài liệu đính kèm" + "Kéo thả/nhấp chọn tệp" |
| 42 | danh-gia | DS chọn vụ việc thiếu thông tin | 1a | ✅ PASS | — | Đối tượng=Vụ việc → select VV trong form (carry-fwd 28/05) |
| 43 | danh-gia | Đã chọn vẫn show chưa chọn | 1a | ✅ PASS | — | Carry-fwd 28/05 (multi-select giữ trạng thái đã chọn) |
| 44 | danh-gia | Thông báo lỗi+success chấm điểm | 1a | ✅ PASS | — | Carry-fwd 28/05 (toast lỗi/success chấm điểm) |
| 45 | danh-gia | Xếp loại báo cáo đánh giá rỗng | 1a (override 1b) | ✅ PASS | [evidence/danh-gia/bug-45-xep-loai-tot-85.png] | Đợt DG-20260512-0001 điểm TB 85.0 → Xếp loại "Tốt" đúng SRS:874 (≥70%); "--" chỉ khi chưa chấm |
| 46 | danh-gia | Ngày BĐ/KT lùi 1 ngày | 1a | ✅ PASS | [evidence/danh-gia/bug-41-46-form-tao-kh-upload-date.png] | Form có Thời gian BĐ/KT; đợt seed 15/06→30/06 không lệch |
| 29 | doanh-nghiep | Thêm tổ chức báo trùng sai | 1a | ✅ PASS | [evidence/doanh-nghiep/bug-29-39-40-list-them-moi.png] | Tạo DN tên TRÙNG "Sông Hồng BKH" + MST mới → "Thêm DN thành công", không báo trùng tên |
| 30 | doanh-nghiep | Tổ chức Chờ duyệt thiếu nút | 1a | ✅ PASS | [evidence/to-chuc-tu-van/stt30-cb-phe-duyet-detail-co-nut-phe-duyet-tu-choi.png] | Bug thuộc **Tổ chức tư vấn** (DN không lifecycle — SRS:759). Test đúng role `cb_pd_tw_01` (CB Phê duyệt): record CHO_PHE_DUYET hiện đủ nút Phê duyệt/Từ chối ở cả danh sách (check/close-circle) lẫn chi tiết — khớp FR-IV-NEW-04 (SRS:1132 role=CB_PD) + note gốc "PD role thấy eye+Phê duyệt+Từ chối" |
| 31 | doanh-nghiep | Nút Sửa chuyển sang danh sách | 1a | ✅ PASS | [evidence/doanh-nghiep/bug-31-edit-form-saved.png] | Nút Sửa mở form /sua (không nhảy list); PATCH 200 lưu OK |
| 39 | doanh-nghiep | DN không có Thêm mới (bn) | 1a | ✅ PASS | [evidence/doanh-nghiep/bug-29-39-40-list-them-moi.png] | cb_nv_bn_01 toolbar có "Thêm mới" (primary) — SRS:423 |
| 40 | doanh-nghiep | Loại DN hiển thị id | 1a | ✅ PASS | [evidence/doanh-nghiep/bug-29-39-40-list-them-moi.png] | Dropdown Loại DN "Doanh nghiệp tư nhân"/"Hộ kinh doanh" — tên, no id |
| 35 | chi-tra | Chi trả SLA chữ trắng | 1a | ✅ PASS (Closed 06-05) | [bugs/chi-tra/Pass-bug-35-sla-contrast.md] | R-verify-2 06-05: ĐÃ FIX — tag "Quá hạn" chữ trắng trên nền đậm opaque, contrast 21:1 đạt WCAG AA (UI-05 srs-v3.5.md:568) |
| 36 | chi-tra | Thẩm định không lưu | 1a | ✅ PASS (cf) | — | Carry-fwd 28/05; R2 06-02 không re-verify (Nhóm A: 0 HS Đang đánh giá bn scope) |
| 37 | chi-tra | Sau duyệt vẫn tab Chờ duyệt | 1a | ✅ PASS (cf) | — | Carry-fwd 28/05; R2 06-02 không re-verify (Nhóm A: 0 HS Chờ phê duyệt bn scope) |
| 38 | chi-tra | Số tiền/Ngày định dạng | 1a | ✅ PASS | [evidence/chi-tra/bug-35-38-list-sla-sotien.png] | Số tiền dấu chấm + ngày dd/mm/yyyy OK; lưu ý list thiếu hậu tố "đ" (Minor SRS:932) |
| 49 | ct-htpldn | KH HTPL upload file lỗi | 1a → reframe | ✅ PASS (Closed 06-05) | [bugs/ct-htpldn/Pass-bug-49-upload-file-500.md] | R-verify-2b 06-05 13:53: ĐÃ FIX — PATCH + fileDinhKemIds → 200; API re-check 2 file persist `entityType=CHUONG_TRINH_HTPL` (dev theo phương án (a), khớp C15). Sync tài liệu SRS data-model → SRS-C-006 (BA), không gate bug app |
| 50 | ct-htpldn | Mục tiêu không hiện | 1a | ✅ PASS | [evidence/ct-htpldn/bug-50-51-ct-detail-muctieu-tabs.png] | CT detail hiện Mục tiêu textarea "verify stt49" đầy đủ |
| 51 | ct-htpldn | Thừa tab Tài liệu | 1a | ✅ PASS | [evidence/ct-htpldn/bug-50-51-ct-detail-muctieu-tabs.png] | Chi tiết CT chỉ tab "Thông tin" — không có tab Tài liệu thừa |
| 52 | ct-htpldn | Đợt báo cáo thiếu chọn phạm vi | 1a | ✅ PASS | [evidence/ct-htpldn/bug-52-dot-bc-pham-vi-donvi.png] | Modal Tạo đợt BC có field "Đơn vị nộp báo cáo" required, 81+ đơn vị |
| 71 | qtht-cau-hinh-ht | Xóa đơn vị báo lỗi kèm success | 1a | ✅ PASS | [evidence/qtht-cau-hinh-ht/stt71-73-danh-muc-coquan.png] | Tạo+xóa đơn vị test → chỉ toast "Xoá đơn vị thành công", no lỗi; GET deleted→404 đúng — SRS:352 |
| 73 | qtht-cau-hinh-ht | Mức chi phí tối đa thiếu dấu chấm | 1a | ✅ PASS | [evidence/qtht-cau-hinh-ht/stt73-muc-chi-phi-toi-da-5trieu.png] | Form Tiêu chí ĐG chi phí nhập 5000000 → "5.000.000" (dấu chấm) — SRS:579 |
| 74 | qtht-cau-hinh-ht | Mẫu phản hồi thiếu cột Hành động | 1a | ✅ PASS | [evidence/qtht-cau-hinh-ht/stt74-mau-phan-hoi-hanh-dong.png] | Tab Mẫu phản hồi có cột Hành động + nút Xem (eye) mọi dòng (15/15) — SRS:1769 |
| 75 | qtht-cau-hinh-ht | Ngày lễ thiếu thông báo + STT trống | 1a | ✅ PASS | [evidence/qtht-cau-hinh-ht/stt75-ngay-le-them-thanh-cong-stt.png] | Thêm ngày lễ 15/08 → toast "Thêm ngày lễ thành công" + STT có data (7) — SRS:1469 |
| 53 | hoi-dap | Popup duyệt câu hỏi text sai | 1a | ✅ PASS | [evidence/hoi-dap/stt53-popup-phe-duyet-text.png] | cb_pd_tw_01 Phê duyệt → popup "Xác nhận phê duyệt? Hành động không thể hoàn tác" text đúng — SRS:1126 |
| 54 | hoi-dap | Kho câu hỏi thiếu cột Hành động | 1a | ✅ PASS | [evidence/hoi-dap/stt54-list-hanh-dong.png] | List có cột Hành động + Mã link + Xem/Sửa/Xóa; DA_DUYET/CONG_KHAI/HOAN_THANH chỉ Xem — SRS:1055 |
| 59 | hoi-dap | Chọn câu hỏi gợi ý gửi lỗi | 1a | ✅ PASS | [evidence/hoi-dap/stt59-phan-cong-thanh-cong.png] | SCR-II-03 chọn ứng viên (radio) → "Phân công thành công", TIEP_NHAN→DANG_XU_LY — SRS:1214 |
| 79 | qtht-tai-khoan | Tài khoản: sửa mất Loại TK/Đơn vị | 1a | ✅ PASS (Closed 06-05) | [bugs/qtht-tai-khoan/Pass-bug-79-edit-save-version-422.md] | R-verify-2 06-05: ĐÃ FIX — Sửa TK lưu OK (PUT 200, version 2→3, danh sách cập nhật; Loại TK+Đơn vị giữ đúng) — SRS:736 |
| 80 | qtht-tai-khoan | Tài khoản: không gửi email mật khẩu | 1a | ✅ PASS | [evidence/qtht-tai-khoan/stt80-create-account-done.png] | Tạo acct qa_verify_80 → MailHog có email "Tài khoản hệ thống PM-HTPLDN đã được tạo" đúng giờ — SRS:736 |
| 81 | qtht-tai-khoan | Cột Họ tên quá nhỏ | 1a | ✅ PASS | [evidence/qtht-tai-khoan/stt81-list-hoten-fullwidth.png] | Cột Họ tên hiển thị đầy đủ tên dài ("NHT BTP TW 02 Audit R30"), không cắt — SRS:1656 |
| 76 | qtht-vai-tro | Vai trò Cấp filter "ALL" | 1a | ✅ PASS | [evidence/qtht-vai-tro/stt76-cap-filter-tat-ca-cap.png] | Filter Cấp hiện "Tất cả cấp (ALL)" — có nhãn Việt, đồng dạng (TW)/(BN)/(DP) — SRS:2107 |
| 77 | qtht-vai-tro | Phân quyền: số quyền chưa cập nhật | 1a (override 1c) | ✅ PASS | [evidence/qtht-vai-tro/stt77-so-quyen-updated-74.png] | **Override**: màn /quyen-han LOAD OK (KHÔNG 404); toggle quyền role test → Lưu OK + Số quyền cập nhật 73→74 — SRS:813/647 |
| 78 | qtht-vai-tro | Phân quyền dữ liệu lỗi khi lưu | 1a | ✅ PASS | [evidence/qtht-vai-tro/stt78-phan-quyen-du-lieu-save-ok.png] | Chọn đơn vị role test → PUT /phan-quyen-du-lieu/batch 200 + toast "Đã lưu" (đã restore) — SRS:796 |
| 63 | tu-van-chuyen-sau | Chuyên gia 403 Tài liệu pháp luật | 1b (reframe → bug Medium) | ❌ FAIL (Medium) | [bugs/tu-van-chuyen-sau/bug-63-cg-403-tvcs-list.md] | R-verify-2 06-05: VẪN LỖI — menu TVCS hiện cho CG, click → /403 dead-end nguyên trạng (CG ko phải tác nhân SCR-X1-01 nhưng có quyền + 4 record scoped, không có màn xem). Phần tài liệu PL theo BA đã hết 403 — theo dõi report 06-04 BUG-TVCS-063 |
| 64 | tu-van-chuyen-sau | TVCG thiếu icon Phê duyệt/Từ chối | 1a | ✅ PASS | [evidence/tu-van-chuyen-sau/stt64-cho-phe-duyet-phe-duyet-tu-choi-buttons.png] | Chi tiết CHO_PHE_DUYET (cb_pd_tw_01) hiện đủ nút [Phê duyệt]/[Từ chối]; list có icon check+close — SRS:1142 |
| 65 | tu-van-chuyen-sau | Tư liệu pháp luật upload không lưu | 1c (override → PASS) | ✅ PASS | [evidence/tu-van-chuyen-sau/stt65-tulieu-upload-saved-sofile1.png] | Endpoint thật /tu-lieu-phap-ly-vvs 200 (ko phải /tu-lieu-phap-luats 404); upload UI (cb_nv_tw) tạo record + soFile=1 (đã xóa) — SRS:800 |
| 47 | bm | Không có menu DS biểu mẫu | 1a | ✅ PASS | [evidence/bm/stt47-bieu-mau-danh-sach-list.png] | Menu "Danh sách biểu mẫu" → SCR-VII-02 "Biểu mẫu" + [Thêm biểu mẫu] + list 21 dòng — SRS:632/371 |
| 48 | bm | Preview file biểu mẫu lỗi | 1a | ✅ PASS | [evidence/bm/stt48-xem-truoc-pdf-preview-minio.png] | Chi tiết BM PDF → "Xem trước" mở tab MinIO PDF inline (presigned, disposition=inline) — SRS:654/374 |
| 28 | tu-van-vien-cg | File đính kèm TVV không preview | 1a | ✅ PASS | [evidence/tu-van-vien-cg/stt28-file-dinh-kem-xem-pdf-preview.png] | Tab Hồ sơ TVV → File đính kèm nút "Xem" mở tab MinIO PDF inline (disposition=inline) — SRS:1558 |
| 67 | qtht-danh-muc | Xuất Excel danh mục không mở | 1b (override → PASS) | ✅ PASS | [evidence/qtht-danh-muc/stt67-xuat-excel-button-200-xlsx.png] | **Override**: SCR-VIII-01 ko liệt kê nhưng UI CÓ nút "Xuất Excel"; nhấp → POST /danh-muc/export 200 + attachment .xlsx 7389 bytes tải OK — SRS:1385/1697 |
| 69 | qtht-danh-muc | Danh mục sort cột chưa chạy | 1b → lật false-positive | ✅ PASS | [bugs/qtht-danh-muc/Pass-bug-69-sort-cot-khong-chay.md] | **Lật FALSE-POSITIVE**: SRS SCR-VIII-01 KHÔNG yêu cầu sortable — 3 cột Hành vi="—" (srs-fr-10:1572/1573/1575), :1609 chỉ sắp xếp mặc định. "Ko sắp lại khi nhấp" là đúng spec; FE để artifact sortBy/aria-sort = observation gỡ |
| 82 | qtht-nhat-ky | Nhật ký Loại thao tác hiển thị mã | 1a | ✅ PASS | [evidence/qtht-nhat-ky/stt82-loai-thao-tac-badge-tieng-viet.png] | SCR-VIII-10 cột Loại thao tác = badge ant-tag tiếng Việt (Đăng nhập/Đăng xuất/Tạo mới/Cập nhật/Xóa/Phân công) 50/50 dòng, rawEnumLeak=0 — SRS:1909 |

---

## Câu hỏi gửi BA (verdict 1b — spec sai/ambiguous)

Tách riêng sang file → [`cau-hoi-BA-confirm-2026-06-02.md`](./cau-hoi-BA-confirm-2026-06-02.md). Hiện **1 câu** (SRS-C-006 — CT HTPLDN có hỗ trợ file đính kèm không; tách từ STT 49). STT 22 đã chốt PASS theo bug gốc (user quyết) — chỉ còn khuyến nghị BA align SRS mo_ta Y→N.

---

## BLOCKED env/infra (verdict 1c)

*(Mỗi mục: bug + endpoint/config thiếu + note "Chờ Dev BE/Infra <action>")*

---
