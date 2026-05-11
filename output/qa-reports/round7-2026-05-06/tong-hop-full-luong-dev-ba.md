# Tổng hợp full luồng Round 7 - Dev/BA

Ngày tổng hợp: 2026-05-11  
Phạm vi: `tasks/tmp`, `output/qa-reports/round7-2026-05-06/workflow`, `functional`, `bug-reports`.  
Cách đọc: ưu tiên kết luận mới nhất trong `bug-reports` và `tasks/tmp/todo-*.md`; bug report mới ghi đè functional/workflow cũ. Không sửa code, không chạy lại test.

Quy ước:

- `✅`: full/core flow OK.
- `⚠️`: core flow chạy được nhưng còn edge/partial/defer.
- `🚫`: đang block full luồng hoặc block nhóm TC chính.
- `⏳`: chờ upstream/phụ thuộc ngoài là nguyên nhân chính.
- Nhóm `A`: phụ thuộc ngoài. Nhóm `B`: full/core luồng không block core. Nhóm `C`: chưa full luồng/block nội bộ hoặc data/endpoint/UI/spec.
- Cột `Phân nhóm` trong bảng tổng quan là kết luận ở mức module. Mục Nhóm A bên dưới có thể liệt kê cả nhánh phụ thuộc ngoài của module đã được chốt nhóm B ở core CMS.

## 1. Bảng tổng quan module

| Module | Full flow OK? | Phân nhóm | Bug Open | Ghi chú 1 dòng |
|---|:-:|:-:|---:|---|
| Báo cáo | 🚫 | C | 2 | Excel pass; R7.7.13 còn PDF 422, BE list 500/block và 15 defer. |
| Biểu mẫu | 🚫 | C | 3 | Workflow pass nhưng functional còn MinIO `localhost`, invalid upload silent reject, 21MB/413 UX. |
| Chi trả | ⚠️ | B | 0 | Core v3.5 pass R3, 7/7 bug closed; DN bổ sung HS bị block do thiếu HSCT/DN portal. |
| Cross-cutting/API/Edge | 🚫 | C | 3+ | API 38/44 blocked do endpoint 404/mTLS; upload security còn magic-byte gap; lưu nháp CT còn UI gap. |
| CT HTPLDN | 🚫 | C | 4 | Functional P0 CT pass nhưng GĐ1 B10 partial, GĐ2 thiếu UI/endpoint/tổng hợp. |
| Đánh giá hiệu quả HTPL | 🚫 | C | 6 | BUG-DG-008/009/010/011/012/013 đang block workflow/functional. |
| Đào tạo | 🚫 | C | 7+ | Nhiều workflow pass nhưng Học viên POST 500, ĐKT form, Khóa học `pageSize=200`, DT-004/9 TC HV block. |
| Dashboard | ⚠️ | B | 1 | KPI core 33/34; còn BUG-DASH-005 permission và auto-refresh cần manual QA. |
| Doanh nghiệp | ✅ | B | 0 | CMS pass 19/20 active; DN-020 VNeID Tier 3 BA cắt scope. |
| Hỏi đáp | ⚠️ | A | 2 | Workflow 10/11; TVN_BRIDGE/PLQG và seed backdate còn chờ, 2 minor open. |
| Hợp đồng tư vấn | ⚠️ | B | 2 | R3 16/17 pass; còn UI audit tab và dropdown TVV/CG `pageSize=200`. |
| Kho QA | ✅ | B | 0 | Manual workflow 8/8 + auto-feed TU_DONG pass R10d. |
| Người hỗ trợ | ✅ | B | 0 | 11/11 active pass, 5/5 bug closed. |
| QTHT | ✅ | B | 0 | Danh mục, tài khoản, vai trò, audit log core pass; các bug chính closed. |
| Tổ chức tư vấn | ✅ | B | 0 | Seed/phê duyệt/workflow/functional pass, 2/2 bug closed. |
| Tư vấn nhanh | ⚠️ | A | 3 | Core CMS pass; public/PLQG/mTLS còn chờ, functional 31/35. |
| TVCS | ⚠️ | B | 5 | Workflow core pass R15; functional R17 còn 5 bug open. |
| TVV/CG | ⚠️ | B | 1 | Core workflow TVV/CG pass; functional còn RETRY-005 edge. |
| Vụ việc | ⚠️ | A | 3 | Core workflow/public pass; DN bổ sung cần VNeID T2/DN portal, functional 29/72. |
| Pre-test/Deploy gap | ✅ | B | 0 | Deploy-gap audit 6/6 closed; SRS FR10 còn câu hỏi BA, không tính product flow. |

## 2. Nhóm A - Module/nhánh phụ thuộc ngoài

| Module | Phần đã OK | Phần đang phụ thuộc ngoài | Owner tiếp theo |
|---|---|---|---|
| Hỏi đáp | Seed MOI, MoB, workflow nội bộ 10/11, bug flow chính closed. | TP-HD-09, TVN_BRIDGE, PLQG endpoint, seed backdate SLA. | Infra/Integration + QA seed. |
| Tư vấn nhanh | B1-B4 CMS pass, pool 50 phiên cover state. | R7.6.3 public cần Cổng PLQG endpoint, phiên công khai, mTLS/DN portal. | Infra/Integration. |
| Vụ việc | Core workflow 12/12, công khai pass. | DN bổ sung HS cần VNeID T2 sandbox, DN account, DN portal endpoint, seed VV `YEU_CAU_BO_SUNG`. | Infra + Dev seed. |
| Chi trả | Core v3.5 pass R3, pool 40/40 BR-OK. | DN bổ sung HS cần HSCT thuộc QA DN hoặc DVC/DN portal path. | Dev seed + Infra. |
| Cross-cutting/API | 4 infra TC pass. | 8/9 outbound endpoint 404, mTLS test env chưa có cert/JWT. | Infra/BE. |

## 3. Nhóm B - Full/core luồng không block core

| Module | Core/full flow OK | Bug/edge còn lại |
|---|---|---|
| Doanh nghiệp | CMS functional R14 pass 19/20 active, 6/6 bug closed. | DN-020 VNeID Tier 3 đã BA cắt scope. |
| Kho QA | 8/8 manual workflow + auto-feed BR-FLOW-10 pass. | Không còn open bug core. |
| Người hỗ trợ | 11/11 active pass. | Không còn open bug core. |
| QTHT | Danh mục, vai trò, tài khoản, reset, audit log pass. | Profile đổi MK có 3 mâu thuẫn tài liệu cần BA rà, không block core. |
| Tổ chức tư vấn | Workflow 8/8 + functional 10/10 pass. | Không còn open bug. |
| TVV/CG | Core workflow TVV/CG/NHT transition pass. | RETRY-005 edge permission/SRS. |
| TVCS | Workflow core 11/11 covered. | Functional chưa sạch 100%, 5 bug open. |
| Dashboard | KPI core gần sạch. | BUG-DASH-005 permission; 6 sub-aspect auto-refresh cần manual QA. |
| Hợp đồng tư vấn | 16/17 pass. | BUG-020 audit UI, BUG-030 dropdown TVV/CG. |
| Chi trả | Core CMS pass R3. | DN-only bổ sung HS cần data/portal. |

## 4. Nhóm C - Chưa full luồng / block

| Module | Bước/TC bị block | Nguyên nhân | Phân loại chuẩn | Bug/Open liên quan |
|---|---|---|---|---|
| Báo cáo | R7.7.13 PDF export, BE list report, 15 defer. | PDF chưa support đúng, BE list 500/deploy gap, dropdown thiếu report. | Thiếu endpoint / Lỗi nội bộ BE/FE | BUG-BC-PDF-NOT-SUPPORTED, LEGEND-002. |
| Biểu mẫu | R7.7.10/R7.7.10b upload/preview/download. | MinIO public URL trỏ localhost, invalid `.txt` silent reject, 21MB reset thay vì 413. | Lỗi nội bộ BE/FE / Sai UI | BUG-BM-007/008/009. |
| Cross-cutting/API | R7.7.16 38/44 API blocked. | Outbound endpoint chưa deploy, mTLS test env thiếu cert. | Thiếu endpoint / Phụ thuộc ngoài | API Critical + Major open. |
| CT HTPLDN | R7.6.4 B10, R7.6.5 GĐ2, CT-038. | Rule tổng hợp partial, UI Đợt BC chưa build, thiếu `/tong-hop`, ID mismatch. | Lỗi nội bộ BE/FE / Thiếu endpoint / Sai rule BA | B10-001, DOTBC-UI-001, DOTBC-API-001/002. |
| Đánh giá hiệu quả HTPL | B10/B11, D2a HUY, D2b HOAN_THANH, TC14/17. | Kết quả không persist/advance, thiếu nút HUY, chưa tạo được đợt HOAN_THANH. | Lỗi nội bộ BE/FE | DG-008..013. |
| Đào tạo | Học viên seed, ĐKT sửa/tạo, Khóa học DT-004, HV-related TC. | POST `/hoc-viens` 500, FE form lỗi, dropdown `pageSize=200`, thiếu assignment CRUD. | Lỗi nội bộ BE/FE / Thiếu data | BUG-HV-BE-01, DKT form, DT-FORM-GV-02. |
| Vụ việc | R7.7.3 functional còn 43 TC, DN bổ sung HS. | VNeID/DN portal thiếu, NOTIF/LICHSU partial. | Phụ thuộc ngoài / Lỗi nội bộ BE/FE | NOTIF/LICHSU, PC-WRN-01. |
| Tư vấn nhanh | R7.7.11 5 blocked + 7 defer. | Public/DN/mTLS và 3 bug open/partial. | Phụ thuộc ngoài / Lỗi nội bộ BE/FE | TVN-001/005/007. |
| TVCS | R7.7.5 8 TC chưa pass. | Permission/validation/regression còn open. | Lỗi nội bộ BE/FE | TVCS 001/004/005/006/008. |
| Hỏi đáp | TP-HD-09, HD-045/047/048/060..062, HD-022b/c/d/057. | PLQG/TVN_BRIDGE, backdate SLA seed, UX/errCode minor. | Phụ thuộc ngoài / Thiếu data / Sai UI | HD-055, HD-014. |

## 5. Module core pass, chưa sạch 100%

| Module | Core pass | Chưa sạch 100% |
|---|---|---|
| Chi trả | Full flow v3.5 pass R3, 7/7 bug closed. | DN bổ sung HS cần HSCT thuộc QA DN/DN portal; DN count smoke cần investigate. |
| TVV/CG | A1/A1-CG/A1.6/A2 pass. | RETRY-005 còn open: permission NHT cùng đơn vị + SRS/nộp lại. |
| Vụ việc | Workflow 12/12 + công khai pass. | Functional mới 29/72, DN VNeID branch chưa test, NOTIF/LICHSU partial. |
| TVCS | Workflow R15 covered 11/11. | Functional 53/61, còn 5 bug open. |
| Tư vấn nhanh | CMS B1-B4 pass, pool 50. | Public/PLQG/mTLS và functional 31/35 chưa full. |
| Dashboard | KPI/drill-down cũ closed, 33/34. | BUG-DASH-005 permission, auto-refresh manual. |
| Hợp đồng tư vấn | R3 16/17. | BUG-020 audit tab, BUG-030 dropdown TVV/CG. |
| Hỏi đáp | Workflow nội bộ 10/11, bug flow chính closed. | PLQG/TVN bridge, backdate seed, HD-055/014 minor. |
| Đào tạo | B0/B1/B7/B11/B12 nhiều flow pass. | Học viên/ĐKT/Khóa học functional còn block. |

## 6. Block cần Dev/BA xử lý chi tiết

| Module | Block cụ thể | Nguyên nhân | Phân loại chuẩn | Action đề xuất |
|---|---|---|---|---|
| Đánh giá hiệu quả HTPL | BUG-DG-008/DG-012 block B10/B11, TC14/17. | PUT kết quả/chấm điểm không persist hoặc không advance state. | Lỗi nội bộ BE/FE | Dev fix persistence/state transition, QA rerun D2/D2b/R7.7.9. |
| Đánh giá hiệu quả HTPL | BUG-DG-009 block HUY 4 state. | UI không render nút HUY. | Sai UI | FE wire HUY button + retest positive transition. |
| CT HTPLDN | GĐ1 B10 409, GĐ2 chưa full. | Rule tổng hợp chưa rõ, thiếu UI Story 13.6 và `/tong-hop`. | Sai rule BA / Thiếu endpoint / Sai UI | BA chốt rule; BE build endpoint; FE build tab Đợt BC. |
| Báo cáo | PDF export và list/dropdown báo cáo. | PDF chưa support, dropdown thiếu 3 loại, BE list 500. | Thiếu endpoint / Lỗi nội bộ BE/FE | BE/FE support PDF + đủ 23 loại; rerun R7.7.13. |
| Biểu mẫu | Preview/download/upload. | MinIO URL public sai; invalid/oversize upload UX sai. | Lỗi nội bộ BE/FE / Sai UI | Fix public host, graceful 413, toast error. |
| Đào tạo | Học viên POST 500, 9 TC HV-related. | BE crash valid body; thiếu seed học viên. | Lỗi nội bộ BE/FE / Thiếu data | BE fix `/hoc-viens`; QA seed học viên DN/NHT. |
| Đào tạo | DT-004 dropdown giảng viên empty. | FE gọi `pageSize=200` vượt BE max 100. | Lỗi nội bộ BE/FE | FE đổi pageSize <=100/paging đúng. |
| Đào tạo | ĐKT create/edit form. | Form/modal lỗi FE. | Sai UI | FE fix BUG-DKT-EDIT-FORM-01/CREATE-FORM-01. |
| Cross-cutting/API | R7.7.16 API blocked. | Endpoint 404, mTLS/JWT staging thiếu. | Thiếu endpoint / Phụ thuộc ngoài | Infra/BE deploy endpoint + cấp cert/JWT. |
| Vụ việc | DN bổ sung HS. | Thiếu VNeID T2, DN portal, DN VV YCBS. | Phụ thuộc ngoài / Thiếu data | Infra cấp sandbox; Dev/QA seed DN/VV. |
| Hỏi đáp | TP-HD-09/TVN_BRIDGE. | PLQG/Cổng TV nhanh chưa deploy. | Phụ thuộc ngoài | Deploy PLQG endpoint + seed TVN_BRIDGE. |
| Hợp đồng tư vấn | BUG-030 dropdown TVV/CG. | FE call pageSize=200 gây 422. | Lỗi nội bộ BE/FE | FE paging đúng max 100. |

## 7. Cần xác nhận thêm

- CT HTPLDN: rule tổng hợp khi `0/0` hoặc khi còn đợt chưa `DA_TONG_HOP`; điều kiện nào cho phép advance B10/GĐ2?
- Đánh giá hiệu quả HTPL: rule versioning và advance state khi cập nhật kết quả/chấm điểm; trạng thái nào được HUY?
- TVV/CG: BA sửa/chốt SRS cho RETRY-005, permission “NHT cùng đơn vị”, có bỏ endpoint `/nop-lai` riêng không?
- Báo cáo: template PDF theo TT17/2025, danh sách 23 loại report bắt buộc, các report nào defer theo scope?
- Hợp đồng tư vấn: cách xác định VV `HOAN_THANH` khi hệ thống auto-flip sang `DA_DANH_GIA`.
- Đào tạo: enum hình thức khóa học có hỗ trợ “Kết hợp” không; ĐKT có đúng chỉ 2 state `NHAP/DA_PHAN_PHOI` không; NHCH còn dùng `NHAP/CONG_KHAI/AN` hay chỉ `KICH_HOAT/VO_HIEU_HOA`.
- Cross-cutting hard delete: SRS modal “xóa mềm” có obsolete chính thức không.
- Profile/đổi mật khẩu: rule độ mạnh mật khẩu, errCode và tab “Phiên đăng nhập” có thuộc scope release không.

## 8. Action ưu tiên cho Dev/BA

### Critical

- Đánh giá: fix DG-008/DG-012 persistence/advance state để unblock B10/B11, D2b, TC14/17.
- Cross-cutting/API: deploy outbound endpoint và cấp mTLS/JWT staging cho R7.7.16.
- Báo cáo: xử lý PDF export/list 500/dropdown thiếu loại nếu báo cáo nằm trong release scope.
- Biểu mẫu: fix MinIO public URL `localhost:9000` vì làm user không preview/download được.

### Major

- CT HTPLDN: build UI Đợt BC Story 13.6, endpoint `/tong-hop`, xử lý ID mismatch.
- Đào tạo: fix POST `/hoc-viens` 500, FE Khóa học `pageSize=200`, ĐKT create/edit form.
- Hợp đồng tư vấn: fix BUG-030 dropdown TVV/CG và BUG-020 UI audit tab.
- Dashboard: enforce permission `/dashboard` cho DN/NHT/TVV/CG theo matrix.
- TVCS/TV nhanh/Vụ việc: đóng bug open còn lại sau khi core flow đã pass.

### Cần BA chốt

- CT HTPLDN rule tổng hợp.
- Đánh giá rule HUY/versioning/advance state.
- TVV/CG RETRY-005 và SRS line liên quan.
- Báo cáo PDF/23 report.
- Đào tạo state/enum drift.
- Hợp đồng TV rule VV hoàn thành.

### Cần Infra/Integration

- PLQG/Cổng TV nhanh/Hỏi đáp bridge endpoints.
- VNeID Tier 2 sandbox, DN portal URL/token/account.
- API mTLS cert/key/JWT staging.
- DVC/LGSP/DN portal path cho Chi trả DN bổ sung.

### Cần QA seed

- HSCT thuộc QA DN `MST 1234567899` hoặc DN credential phù hợp cho Chi trả DN bổ sung.
- VV `YEU_CAU_BO_SUNG` thuộc DN test cho Vụ việc DN-BS.
- TVN_BRIDGE + phiên TVN `cong_khai=1` sau khi PLQG deploy.
- Backdate SLA cho HD-022b/c/d và HD-057.
- Học viên DN/NHT sau khi BE `/hoc-viens` fix.
- VV/HĐ TV đủ trạng thái để retest Hợp đồng TV/VV hoàn thành.

## 9. Note tránh hiểu nhầm trạng thái pass/fail

- TVV/CG không block core: workflow pass, chỉ còn RETRY-005 edge.
- Kho QA auto-feed đã pass R10d, không còn open core.
- Chi trả core đã pass R3, các bug flow 7/7 closed; DN-only bổ sung không phải fail core CMS.
- TVCS workflow đã pass R15; functional vẫn partial.
- Vụ việc core/public đã pass; DN-BS là môi trường/VNeID/DN portal.
- Dashboard 4 bug KPI cũ đã closed; open hiện tại là permission BUG-DASH-005.
- Doanh nghiệp CMS pass; DN-020 VNeID Tier 3 đã BA cắt scope.
