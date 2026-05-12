# Test Cases PASS — tv-nhanh
> **Nguồn**: result-tv-nhanh-all.md
> **Ngày tổng hợp**: 2026-05-11
> **Phạm vi**: chỉ Result ∈ {PASS, PASS-DEVIATE, PASS-RESOLVED}

## Summary

| File test-case | PASS | PASS-DEVIATE | PASS-RESOLVED | Tổng |
|----------------|------|--------------|---------------|------|
| 01-TC-FR-X2-01-quan-ly-kho-cau-hoi | 19 | 0 | 0 | 19 |
| 02-TC-FR-X2-02-quan-ly-phien-tu-van | 13 | 0 | 0 | 13 |
| 03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect | 2 | 0 | 0 | 2 |
| 04-TC-FR-X2-05-API-inbound-danh-gia | 6 | 0 | 0 | 6 |
| 05-TC-FR-X2-06-cong-khai-kho | 6 | 0 | 0 | 6 |
| 06-TC-permission-matrix | 1 | 0 | 0 | 1 |
| **Tổng** | **47** | **0** | **0** | **47** |

---

## 01-TC-FR-X2-01-quan-ly-kho-cau-hoi

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\01-TC-FR-X2-01-quan-ly-kho-cau-hoi.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-01-quan-ly-kho-cau-hoi\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-KHO-001 | FR-X.2-01 / AC1 line 162 | Hiển thị danh sách Kho Q&A | Login cb_nv_tw_01; Kho có ≥5 record DA_DUYET scope TW | — | Click sidebar Tư vấn → Kho câu hỏi hoặc navigate /tu-van/kho-cau-hoi; quan sát breadcrumb + table | Breadcrumb hiển thị; header `[+ Thêm câu hỏi] [Nhập Excel] [Làm mới]`; table 12 cột; phân trang 20/trang; GET /api/v1/kho-cau-hoi?page=1&size=20 200 | Happy | PASS |  |
| TC-KHO-003 | FR-X.2-01 / AC2 + Processing 3 | Thêm Q&A thủ công happy path → CHO_DUYET | Login cb_nv_tw_01; LV_THUE KICH_HOAT | cau_hoi + cau_tra_loi + linh_vuc=Thuế + tu_khoa | Mở modal Thêm → nhập 4 field → Gửi duyệt | Toast "Đã gửi duyệt câu hỏi"; modal đóng; record CHO_DUYET nguon=THU_CONG mã QA-YYYYMMDD-NNN; POST /api/v1/kho-cau-hoi 201 | Happy | PASS |  |
| TC-KHO-006 | FR-X.2-01 / Processing 3 | Sửa Q&A NHAP của mình | Login cb_nv_tw_01; có record NHAP do user tạo | cau_hoi mới | Tab Tất cả → tìm NHAP → Sửa → đổi cau_hoi → Lưu nháp | Modal pre-fill đúng; sau lưu cau_hoi mới hiển thị + AUDIT_LOG action=UPDATE | Happy | PASS |  |
| TC-KHO-007 | BR-DATA-01 | Xóa Q&A NHAP (soft delete) | Login cb_nv_tw_01; có record NHAP | — | Click Xóa trên dòng NHAP → modal xác nhận → Xác nhận | Toast "Đã xóa"; record không còn trong list; DB is_deleted=1; DELETE /api/v1/kho-cau-hoi/{id} 200 | Happy | PASS |  |
| TC-KHO-008 | FR-X.2-01 / Processing 6 | Toggle hieu_luc DA_DUYET → HET_HIEU_LUC | Có record DA_DUYET hieu_luc=1 | — | Click toggle Hiệu lực trên dòng DA_DUYET → tắt | Toggle OFF; cột Hiệu lực OFF; trang_thai=HET_HIEU_LUC; Q&A không xuất hiện trên Cổng PLQG; PATCH /hieu-luc 200 | Happy | PASS |  |
| TC-KHO-009 | FR-X.2-01 / Processing 2 + BR-FLOW-10 | Auto-tạo từ HOI_DAP DA_DUYET (nguồn TU_DONG) | HOI_DAP CHO_PHE_DUYET scope TW | — | cb_pd_tw_01 phê duyệt HOI_DAP → cb_nv_tw_01 mở Kho câu hỏi tab Tất cả | Record mới có nguon=TU_DONG, hoi_dap_goc_id, trang_thai=DA_DUYET (bypass duyệt); AUDIT_LOG INSERT nguon=TU_DONG | Happy cross-FR | PASS |  |
| TC-KHO-010 | FR-X.2-01 / SCR row 10 | Phê duyệt đơn lẻ → DA_DUYET + hieu_luc=1 | Login cb_pd_tw_01; ≥1 CHO_DUYET scope TW | — | Tab Chờ duyệt → click Duyệt → modal Xác nhận → Duyệt | Toast "Đã duyệt câu hỏi"; record chuyển tab Đã duyệt; trang_thai=DA_DUYET hieu_luc=1; TB CB NV gửi; POST /approve 200 | Happy | PASS |  |
| TC-KHO-011 | FR-X.2-01 / SCR row 10 | Từ chối đơn lẻ với lý do bắt buộc | Login cb_pd_tw_01; record CHO_DUYET | Lý do reject | Click Từ chối → modal Lý do BB → trống Xác nhận lỗi → nhập lý do Xác nhận | Lý do trống ERROR; record trang_thai=NHAP; TB CB NV gửi kèm lý do | Happy | PASS |  |
| TC-KHO-012 | FR-X.2-01 / SCR row 11 | Phê duyệt hàng loạt (modal xác nhận) | ≥3 CHO_DUYET | — | Tab Chờ duyệt → tick 3 checkbox → Duyệt hàng loạt → Xác nhận | 3 record cùng DA_DUYET + hieu_luc=1; toast "Đã duyệt 3 câu hỏi"; KHÔNG có nút Từ chối hàng loạt | Happy | PASS |  |
| TC-KHO-014 | FR-X.2-01 / Processing 5 + BR-DATA-08 | Tìm kiếm full-text (UC157) | Kho có Q&A "Thuế GTGT", "Thuế TNDN", "Hợp đồng lao động" | tu_khoa="thuế" | Filter bar nhập "thuế" → quan sát kết quả | 2 Q&A thuế match (loại trừ Hợp đồng); sort relevance DESC; GET ?q=thuế 200 total:2 | Happy | PASS |  |
| TC-KHO-015 | FR-X.2-01 / SCR row 4 | Lọc theo lĩnh vực + nguồn + trạng thái | — | linh_vuc=Thuế, nguon=TU_DONG, trang_thai=DA_DUYET | Filter 3 điều kiện AND → quan sát | Chỉ Q&A khớp 3 điều kiện AND; network query string chứa cả 3 filter | Happy | PASS |  |
| TC-KHO-016 | BR-DATA-07 | Phân trang 20 mục/trang | Kho có ≥41 record DA_DUYET | — | Trang 1 → trang 2 → trang 3 | Mỗi trang đúng 20 (trừ trang cuối); ?page=2&size=20 | Happy | PASS |  |
| TC-KHO-017 | BR-DATA-04 | Mã Q&A auto-gen QA-YYYYMMDD-SEQ | Tạo 3 record cùng ngày | — | Tạo Q&A 1, 2, 3 → ghi mã | Format QA-YYYYMMDD-NNN; SEQ tăng dần (001, 002, 003) cùng ngày, không trùng | Happy | PASS |  |
| TC-KHO-100 | FR-X.2-01 / E1 | E1 - câu hỏi trống → ERR-KHO-01 | — | cau_hoi rỗng | Modal Thêm → bỏ cau_hoi → điền field khác → Gửi duyệt | Inline error "Câu hỏi là bắt buộc" / ERR-KHO-01; form không submit | Negative | PASS |  |
| TC-KHO-101 | FR-X.2-01 / E2 | E2 - câu trả lời trống → ERR-KHO-02 | — | cau_tra_loi rỗng | Modal Thêm → cau_tra_loi rỗng → Gửi duyệt | Inline "Câu trả lời là bắt buộc" / ERR-KHO-02 | Negative | PASS |  |
| TC-KHO-102 | FR-X.2-01 / E3 | E3 - lĩnh vực không hợp lệ → ERR-KHO-03 | — | linh_vuc_id=99999 hoặc VO_HIEU_HOA | Đổi linh_vuc qua DevTools → Gửi | 400 / ERR-KHO-03 "Lĩnh vực PL không hợp lệ" | Negative | PASS |  |
| TC-KHO-204 | A4 edge | Concurrent edit 2 tab → 409 optimistic lock | — | Tab A v1 / Tab B v1 stale | Tab A mở edit chưa save; Tab B sửa + save 200; Tab A save | Tab A 409 Conflict (version mismatch); toast "Bản ghi đã bị thay đổi. Tải lại" | Edge | PASS |  |
| TC-KHO-300 | GAP-STATE-01 (A5) | Re-enable hieu_luc HET_HIEU_LUC → DA_DUYET | QA-100 HET_HIEU_LUC hieu_luc=0 | — | Toggle Hiệu lực ON | Toast "Đã bật lại hiệu lực"; hieu_luc=1; trang_thai chuyển DA_DUYET; AUDIT_LOG action=ENABLE_HIEU_LUC | Fill-gap A6 | PASS |  |

---

## 02-TC-FR-X2-02-quan-ly-phien-tu-van

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\02-TC-FR-X2-02-quan-ly-phien-tu-van.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-02-quan-ly-phien-tu-van\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PHIEN-001 | FR-X.2-02 / SCR row 5 | Hiển thị danh sách phiên TVN | Login cb_nv_tw_01; ≥3 phiên mix state TW | — | Sidebar Tư vấn → Tư vấn Nhanh hoặc navigate /tu-van/tu-van-nhanh | Breadcrumb + header Làm mới; table 8 cột; GET /api/v1/tu-van-nhanh?page=1&size=20 | Happy | PASS |  |
| TC-PHIEN-002 | FR-X.2-02 / SCR row 3 | Tab phân loại 4 | Có phiên ở mỗi state | — | Click 4 tab: Tất cả / Chờ xử lý / Đã gợi ý / Hoàn thành | Mỗi tab hiển thị số đếm + filter đúng | Happy | PASS |  |
| TC-PHIEN-003 | FR-X.2-02 / SCR row 4 | Lọc từ khóa + trạng thái + khoảng ngày | — | "thuế" + DA_GOI_Y + 7 ngày | Filter 3 điều kiện | Chỉ phiên khớp 3 điều kiện AND | Happy | PASS |  |
| TC-PHIEN-004 | FR-X.2-02 / SCR row 7-8 | Xem chi tiết phiên DA_GOI_Y → layout 2 cột | Có phiên DA_GOI_Y | — | Click Trả lời trên dòng DA_GOI_Y | Cột trái 40% (Mã + badge SM + DN + câu hỏi + lịch sử); cột phải 60% (TOP 5 + ô soạn + Gửi trả lời) | Happy | PASS |  |
| TC-PHIEN-005 | FR-X.2-02 / Processing 3 + BR-DATA-08 | TOP 5 gợi ý từ kho relevance DESC | Phiên cau_hoi "Thuế GTGT"; ≥10 Q&A liên quan | — | Mở chi tiết phiên | Tối đa 5 gợi ý; mỗi gợi ý có Mã/Câu hỏi/Trả lời/Điểm relevance/Chọn; sort DESC; GET /goi-y?limit=5 5 phần tử | Happy | PASS |  |
| TC-PHIEN-006 | FR-X.2-02 / SCR row 8 | Click Chọn gợi ý → auto-fill ô soạn Rich Text | — | — | Click Chọn trên gợi ý #1 | Ô soạn auto-fill nội dung cau_tra_loi của gợi ý | Happy | PASS |  |
| TC-PHIEN-007 | FR-X.2-02 / Processing 5 + SM trans #5 | Chỉnh sửa từ gợi ý → Gửi → CB_TRA_LOI | Phiên DA_GOI_Y đã chọn gợi ý | — | Sửa nội dung + Gửi trả lời + Xác nhận | Toast "Đã gửi trả lời"; trang_thai=CB_TRA_LOI; nguon_tra_loi=THU_CONG hoặc KHO; cb_xu_ly_id+ngay_tra_loi set; POST /tra-loi 200 | Happy | PASS |  |
| TC-PHIEN-011 | SM trans #8 | Auto MOI → HET_HAN sau 30 ngày | Seed phiên MOI ngay_tao=NOW-31 | — | Trigger batch job → verify record | Phiên HET_HAN; TB CB NV gửi; AUDIT_LOG action=AUTO_EXPIRE | Happy batch | PASS |  |
| TC-PHIEN-012 | BR-DATA-07 + SCR row 6 | Phân trang 20 mục/trang | ≥41 phiên | — | Trang 1, 2, 3 | Mỗi trang đúng 20 | Happy | PASS |  |
| TC-PHIEN-100 | FR-X.2-02 / E2 | E2 - nội dung trả lời rỗng → ERR-TVN-02 | — | — | Phiên DA_GOI_Y → KHÔNG nhập ô soạn → Gửi trả lời | Inline "Nội dung trả lời là bắt buộc" / ERR-TVN-02; form không submit | Negative | PASS |  |
| TC-PHIEN-102 | SM | Submit khi state HOAN_THANH → block | — | — | Mở phiên HOAN_THANH | Nút Gửi trả lời disabled/ẩn; POST /tra-loi reject 400 state không cho phép | Negative state cấm | PASS |  |
| TC-PHIEN-200 | A4 edge | TOP 5 trả 3 kết quả khi kho có ≤5 Q&A | Kho 3 Q&A liên quan keyword | — | DN gửi câu hỏi → mở chi tiết | TOP 5 hiển thị 3 (tất cả Q&A), KHÔNG lỗi; sort relevance DESC | Edge | PASS |  |
| TC-PHIEN-201 | A4 edge | Concurrent CB NV trả lời cùng phiên → 409 | — | — | CB-A và CB-B mở DA_GOI_Y; CB-A Gửi OK; CB-B Gửi | CB-B 409 hoặc state error "Phiên đã được trả lời bởi CB khác"; lịch sử có 1 trả lời | Edge | PASS |  |

---

## 03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\03-TC-FR-X2-03-04-DN-chuyen-trang-side-effect.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-03-DN-chuyen-trang-side-effect\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DN-003 | FR-X.2-03 / Processing 5 | DN chuyển kênh TV_NHANH → TV_THU_CONG → giữ lịch sử | Phiên TVN có ≥2 message lịch sử | kenh_moi=THU_CONG | DN nhấn Chuyển TV thủ công; API inbound /chuyen-kenh; login CB NV mở Hỏi đáp | HOI_DAP mới kenh_tiep_nhan=TVN_BRIDGE; tu_van_nhanh_goc_id=phiên cũ; noi_dung kế thừa câu hỏi gốc + lịch sử; phiên TVN gốc giữ trạng thái hoặc HET_HAN | Happy | PASS |  |
| TC-DN-100 | FR-X.2-03 / E1 | E1 - DN gửi câu hỏi trống → ERR-TVN-DN-01 | — | cau_hoi="" | Trigger API inbound qua admin; MCP list_network_requests; login qtht_01 mở audit-log | Network 400 ERR-TVN-DN-01 "Vui lòng nhập câu hỏi"; KHÔNG có TU_VAN_NHANH; AUDIT_LOG API_INBOUND_REJECT | Negative (Codex P1-001) | PASS |  |

---

## 04-TC-FR-X2-05-API-inbound-danh-gia

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\04-TC-FR-X2-05-API-inbound-danh-gia.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-04-API-inbound-danh-gia\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-DGTV-001 | FR-X.2-05 / Processing 2-3 + AC1 | API 200 - tạo DANH_GIA_TV mới + accordion hiển thị | Phiên X CB_TRA_LOI/DA_GOI_Y chưa có DG; DN=100; X-API-Key valid | tu_van_nhanh_id+doanh_nghiep_id+diem=5+nhan_xet | Trigger POST /inbound/danh-gia-tv-nhanh; login cb_nv_tw_01; mở chi tiết phiên | API 200 danh_gia_id; accordion DG hiển thị 5 sao + nhận xét + ngày; phiên HOAN_THANH; AUDIT_LOG INSERT DANH_GIA_TV | Happy | PASS |  |
| TC-DGTV-006 | SM trans #6/#7 | Phiên TVN HOAN_THANH sau đánh giá | — | — | Phiên CB_TRA_LOI → trigger API inbound DG | Phiên trang_thai=HOAN_THANH (trans #7) | Happy | PASS |  |
| TC-DGTV-100 | FR-X.2-05 / E1 | E1 - điểm = 0 → ERR-DG-TVN-01 | — | diem=0 | Trigger API | 400 + ERR-DG-TVN-01 "Điểm đánh giá phải từ 1 đến 5"; KHÔNG tạo bản ghi | Negative | PASS |  |
| TC-DGTV-101 | FR-X.2-05 / E1 | E1 - điểm = 6 → ERR-DG-TVN-01 | — | diem=6 | Trigger API | 400 + ERR-DG-TVN-01 | Negative | PASS |  |
| TC-DGTV-102 | FR-X.2-05 / E2 | E2 - tu_van_nhanh_id không tồn tại → 404 | — | tu_van_nhanh_id=999999 | Trigger API | 404 + ERR-DG-TVN-02 "Phiên tư vấn không tồn tại" | Negative | PASS |  |

---

## 05-TC-FR-X2-06-cong-khai-kho

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\05-TC-FR-X2-06-cong-khai-kho.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-05-cong-khai-kho\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-CK-001 | FR-X.2-06 / Processing CK 1-4 + BR-PUBLIC-03 | Công khai DA_DUYET → CONG_KHAI + thoi_gian_dang_tai | Login cb_nv_tw_01; QA-100 DA_DUYET có anh+mo_ta+file; mock API Cổng PLQG 200 | — | Mở SCR-X2-01 → tìm QA-100 → Công khai → Xác nhận | Toast "Đã công khai..."; CONG_KHAI badge; thoi_gian_dang_tai=NOW format dd/mm/yyyy hh:mm; Hiệu lực ON; outbound POST publish 200; AUDIT_LOG action=CONG_KHAI | Happy core | PASS |  |
| TC-CK-004 | FR-X.2-06 / Processing HCK 1-4 + BR-PUBLIC-02 | Hủy công khai CONG_KHAI → DA_DUYET + clear thoi_gian_dang_tai | QA-100 CONG_KHAI sau TC-CK-001 | — | Click Hủy công khai → Xác nhận hủy | Toast "Đã hủy công khai"; DA_DUYET; thoi_gian_dang_tai trống; outbound DELETE 200; AUDIT_LOG action=HUY_CONG_KHAI | Happy core | PASS |  |
| TC-CK-005 | BR-PUBLIC-03 line 927 | thoi_gian_dang_tai format dd/mm/yyyy hh:mm + disabled | — | — | Sau công khai → mở chi tiết QA-100 | Format "10/05/2026 14:30"; field disabled read-only; PATCH thử reject | Happy | PASS |  |
| TC-CK-007 | SM ⟷ DA_DUYET/CONG_KHAI | Re-publish DA_DUYET → CONG_KHAI sau khi đã hủy 1 lần | QA-100 đã CK → đã hủy CK (DA_DUYET) | — | Click Công khai lại | Public thành công CONG_KHAI; thoi_gian_dang_tai=NEW NOW (không giữ cũ) | Happy | PASS |  |
| TC-CK-102 | FR-X.2-06 / E3 + BR-PUBLIC-01 | E3 - Công khai bản ghi CHO_DUYET → block ERR-TVN-CK-03 | QA-200 CHO_DUYET | — | Nút Công khai không hiển thị; truy cập API trực tiếp POST /publish | UI: Nút Công khai không có trên dòng CHO_DUYET; API reject 400 ERR-TVN-CK-03 "Không thể thực hiện. Trạng thái hiện tại không cho phép" | Negative core | PASS |  |
| TC-CK-103 | SCR row 12 | Hủy công khai bản ghi DA_DUYET (chưa CK) → button không hiển thị | QA-100 DA_DUYET chưa CK | — | Quan sát action column | Chỉ nút Công khai hiển thị, KHÔNG có Hủy công khai | Negative state | PASS |  |

---

## 06-TC-permission-matrix

> Source TC: `c:\HoaAG\LuatDN5\Ver3.1\output\test-cases\tv-nhanh\06-TC-permission-matrix.md`
> Source report: `c:\HoaAG\LuatDN5\Ver3.1\output\execution-test\tv-nhanh\report-06-permission-matrix\Tcs-report\TCs-report.md`

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions (Tiền đề) | Test Data (Dữ liệu) | Các bước thực hiện | Kết quả mong đợi | Type (Happy/Negative/Edge) | Kết quả test (Result) | Chi tiết |
|----|------------------|---------------|--------------------------|---------------------|--------------------|------------------|----------------------------|------------------------|----------|
| TC-PERM-002 | Permission Matrix | TVV/CG/NHT 403 module FR-13 | — | — | Login tvv_01, cg_01, nht_01; truy cập /tu-van/kho-cau-hoi | Sidebar KHÔNG hiển thị; URL trực tiếp 403 hoặc redirect dashboard "Không có quyền"; API GET 403 | Negative | PASS |  |

---

## Skipped

Các section sau KHÔNG có TC PASS/PASS-DEVIATE/PASS-RESOLVED — đã bỏ qua:

- *(không có — tất cả 6 section đều có ít nhất 1 TC PASS)*

*Generated 2026-05-11 — filtered from result-tv-nhanh-all.md*
