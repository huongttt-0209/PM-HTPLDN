# Tổng hợp full luồng Round 7 gửi Dev/BA

Ngày tổng hợp: 2026-05-11  
Phạm vi đọc: `tasks/tmp`, `functional`, `workflow`, `bug-reports` trong `output/qa-reports/round7-2026-05-06`.  
Nguyên tắc: chỉ tổng hợp từ report hiện có, không chạy lại test, không sửa code. Nếu bug report mới hơn functional/workflow report thì ưu tiên kết luận theo bug report mới nhất.

## 1. Bảng tổng quan

| Module | Kết luận full luồng | Nhóm | Workflow | Functional coverage | Bug Open | Bug Closed | TC/path còn thiếu | Blocker chính | Phương án để full |
|---|---|---|---|---|---:|---:|---|---|---|
| Báo cáo | Chưa sẵn sàng | C | Excel export pass | 31/40 pass, 6 fail | 4 | 4 | BC-025, BC-027/028/030/031, BC-034, XLSX analytic | Lỗi nội bộ BE/thiếu export/sai data scope | Wire scope `/bao-cao/*`, build PDF, XLSX đủ loại, validate `kyBaoCao` |
| Chi trả | Có điều kiện | A/B | Core 12 bước pass | Core v3.5 pass; DN bổ sung block | 0 | 7 | FR-V.II-14 DN bổ sung HS | Thiếu dữ liệu/endpoint DN portal ngoài CMS | Seed HSCT thuộc QA DN hoặc mở DVC/DN portal path |
| Cross-cutting/API | Chưa sẵn sàng | A/C | N/A | API 4/44 pass, 38 blocked | 2 | 1+ | R7.7.16, BR-EC còn lại, E2E DN | Thiếu endpoint + phụ thuộc mTLS/JWT/VNeID | Deploy 8/9 cặp API, cấp cert/JWT staging, chạy lại API |
| Đánh giá hiệu quả HTPL | Chưa sẵn sàng | C | 8/11 pass | R11: 15/22 pass, 7 chưa sạch | 7 | 7 | B9-B11, D2a HUY, D2b, TC14/17/18 | Lỗi nội bộ BE/FE, sai permission | Fix DG-012 trước, sau đó DG-008/009/010/013/014/015 |
| Dashboard | Có điều kiện | B | N/A | R3 core bug 4/4 closed; permission DN open | 1 | 4 | BUG-DASH-005, phần hoãn auto/filter/chart | Sai UI/permission | Chặn DN render `/dashboard`, rerun permission/auto-refresh |
| Doanh nghiệp | Sẵn sàng | B | Cross-module pass | CMS pass 19/20 active; DN-020 cắt scope | 0 | 6+ | Không block core | Không còn blocker core | Theo dõi VNeID Tier 3 ngoài scope |
| Hỏi đáp | Có điều kiện | A/C | Nội bộ 10/11 pass | Phase 9: 46/60 cover, 7 chờ PLQG, 2 SLA bug | 2 | nhiều | HD-027/045/047/048/060/061/062; HD-022c/d | Phụ thuộc PLQG/TVN bridge + sai SLA tier | Deploy Cổng PLQG/bridge; fix SLA badge ratio |
| Hợp đồng tư vấn | Có điều kiện | B | Seed/flow chính pass | R6: 21/24 pass, 2 partial/open, 1 fail/issue | 2 | 10 | HDTV-032, HDTV-034 | Sai UI/spec gap nhỏ | Bổ sung section HĐ ở TVV detail; BA xác nhận route standalone |
| Kho QA | Sẵn sàng | B | Manual 8/8 + auto-feed pass | N/A | 0 | 3 | Không còn block core | Không có | Không cần action để full core |
| Người hỗ trợ | Sẵn sàng | B | State machine pass | 11/11 active pass | 0 | 5 | Không còn block core | Không có | Không cần action để full core |
| Tổ chức tư vấn | Sẵn sàng | B | 8/8 pass | 10/10 pass | 0 | 2+ | Không còn block core | Không có | Không cần action để full core |
| Tư vấn nhanh | Có điều kiện | A/C | CMS B1-B4 pass; public chờ ngoài | 31/35 pass; 5 blocked + 7 defer | 3 | 4 | R7.6.3 public, bug 001/005/007 | Phụ thuộc PLQG/mTLS + lỗi nội bộ | Deploy public/PLQG; xử lý bug open, rerun 5 blocked |
| TVCS | Có điều kiện | B/C | 9/11 pass + 2 external covered | 53/61 pass | 5 | 13 | TVCS-001/004/005/006/008 | Lỗi nội bộ permission/validation/regression | Fix 5 bug open, rerun R7.7.5 |
| TVV/CG | Sẵn sàng | B | A1/A1-CG/A1.6/A2 pass | 33/33 pass | 0 | 9+ | Không còn block core | Không có | Không cần action để full core |
| Vụ việc | Có điều kiện | A/C | Core 12/12 + public pass; DN-BS block | R18: 40/72 pass | 4 | 6 | DN-BS, privacy mTLS, TVV/CG native, LICHSU | Phụ thuộc VNeID/mTLS + permission/UI | Cấp VNeID/mTLS, fix CG pool/TVV route/TVV perm/LICHSU |
| Pre-test/deploy gap | Sẵn sàng | B | 7/7 pass | N/A | 0 product | 6 deploy gap | SRS FR10 doc bugs riêng | BA/spec doc | Không block product flow Round 7 |

## 2. Nhóm A - Cần kết nối/đồng bộ từ ngoài hệ thống

| Module/nhánh | Phần đã OK | Phần phụ thuộc ngoài | Loại blocker | Owner đề xuất |
|---|---|---|---|---|
| Cross-cutting/API R7.7.16 | 4 infrastructure TC pass, entity prereq đủ | 8/9 cặp outbound endpoint 404; mTLS/JWT staging chưa có cert | Thiếu endpoint + phụ thuộc ngoài hệ thống | Infra + BE |
| Hỏi đáp | Workflow nội bộ, publish UX, backdate một phần đã verify | Cổng PLQG inbound + TVN_BRIDGE chưa deploy | Phụ thuộc ngoài hệ thống/thiếu endpoint | BE Integration |
| Tư vấn nhanh | CMS B1-B4, pool 50 phiên, E2E nội bộ NHAP→CONG_KHAI pass | Public Cổng PLQG, phiên `cong_khai=1`, mTLS | Phụ thuộc ngoài hệ thống | Infra + BE |
| Vụ việc | Core workflow 12/12, công khai pass, lifecycle fresh đến CHO_PHE_DUYET pass | DN bổ sung HS cần VNeID Tier 2, DN portal; privacy endpoint cần mTLS cert | Phụ thuộc ngoài hệ thống + thiếu data | Infra + Dev seed |
| Chi trả | Core CMS v3.5, pool 40/40, 7/7 bug flow closed | DN bổ sung HS cần HSCT thuộc QA DN hoặc DVC/DN portal path | Thiếu dữ liệu + phụ thuộc ngoài hệ thống | Dev seed + Infra |
| Cross-module E2E DN | DN/VV/Chi trả nhiều phần đã pass riêng | DN login VNeID T2, DN portal, mTLS, handoff VV→Chi trả | Phụ thuộc ngoài hệ thống | Infra + QA seed |

## 3. Nhóm B - Đã full/core luồng, không bị block core

| Module | Core/full flow đã pass | Chưa sạch 100% nếu có | Kết luận |
|---|---|---|---|
| Doanh nghiệp | CMS pass 19/20 active; bug chính closed | DN-020 VNeID Tier 3 đã BA cắt scope | Sẵn sàng |
| Kho QA | Manual workflow 8/8 + auto-feed BR-FLOW-10 pass | Không còn open core | Sẵn sàng |
| Người hỗ trợ | 11/11 active TC pass; mail activation closed | Không còn open core | Sẵn sàng |
| Tổ chức tư vấn | Seed/phê duyệt/workflow/functional 10/10 pass | Không còn open bug | Sẵn sàng |
| TVV/CG | Workflow + functional 33/33 pass; RETRY-005 closed R32 | Không còn block core | Sẵn sàng |
| Dashboard | KPI/drill-down core đã closed 4/4 bug | DN permission BUG-DASH-005 + auto/filter/chart còn hoãn | Có điều kiện |
| Hợp đồng tư vấn | 21/24 TC pass, Critical/Major cũ closed | 2 open không chặn CRUD core | Có điều kiện |
| Chi trả | Core CMS full flow pass, 7/7 bug flow closed | DN bổ sung HS là nhánh portal/data ngoài core | Có điều kiện |

## 4. Nhóm C - Chưa full luồng hoặc đang bị block

| Module | Block ở bước/TC nào | Nguyên nhân cụ thể | Phân loại | Điều kiện unblock |
|---|---|---|---|---|
| Báo cáo | BC-027/028/030/031; BC-025; BC-024 mở rộng; BC-034 | `/bao-cao/*` leak full national cho BN/DP; PDF 422; 2 XLSX analytic 422; 2 route không validate `kyBaoCao` | Lỗi nội bộ BE + thiếu export | Dev BE fix scope/export/DTO validation, rerun R7.7.13 |
| Đánh giá HTPL | B9/B10/B11, D2a, D2b, TC14/17/18 | Kết quả không persist, thiếu HUY button, state không advance `PHAN_CONG/CHO_DUYET_PC`, role quản trị vẫn edit được | Lỗi nội bộ BE/FE + sai permission | Fix DG-012 trước, rồi DG-008/009/010/013/014/015 |
| Hỏi đáp | 7 TC public/bridge; HD-022c/d | Cổng PLQG/TVN_BRIDGE chưa deploy; SLA badge tính theo ngày còn lại thay vì ratio | Phụ thuộc ngoài + sai UI/rule | Deploy endpoint; fix mapping SLA tier |
| Tư vấn nhanh | R7.6.3 public, 5 blocked + 7 defer | Public PLQG/mTLS chưa có; còn 3 bug open/partial | Phụ thuộc ngoài + lỗi nội bộ | Infra deploy/cert; Dev close TVN-001/005/007 |
| TVCS | R7.7.5 còn 8 TC chưa pass | 5 bug open permission/validation/regression | Lỗi nội bộ BE/FE | Fix TVCS-001/004/005/006/008 |
| Vụ việc | DN-BS, privacy mTLS, TVV native, LICHSU | VNeID/DN portal thiếu; CG không vào pool; TVV 403/thiếu permission; LICHSU 12/18 enum | Phụ thuộc ngoài + lỗi nội bộ | Infra cấp VNeID/mTLS; Dev fix CG pool, TVV route/permission, LICHSU |
| Cross-cutting/API | API-001/002; R7.8.7 E2E DN | mTLS cert missing; 8/9 cặp endpoint 404; DN E2E chờ VNeID/portal | Thiếu endpoint + phụ thuộc ngoài | Deploy API, cấp cert/JWT, chuẩn bị DN account |

## 5. Chi tiết module bị block

| Module | TC/path | Trạng thái | Nguyên nhân block | Loại blocker | Owner |
|---|---|---|---|---|---|
| Báo cáo | BC-027/028/030/031 | Fail | BN/DP nhận full national data như TW dù dashboard cùng role scope đúng | Lỗi nội bộ BE/data scope | BE |
| Báo cáo | BC-025 | Fail | PDF export universal 422 `ERR-RPT-EXPORT-01` | Thiếu export endpoint/logic | BE |
| Báo cáo | XLSX analytic | Fail | `BC_VV_THEO_LINH_VUC`, `BC_DANH_GIA_HIEU_QUA_HTPL` chưa support XLSX | Thiếu implementation | BE |
| Báo cáo | BC-034 | Fail | `/bao-cao/hoi-dap` và `/bao-cao/danh-gia-hieu-qua` không validate enum `kyBaoCao` | Lỗi validation BE | BE |
| Đánh giá | TC14/B7-B11 | Block/Fail | DG-012: đợt không advance sau phân công/trình phê duyệt | Lỗi state machine BE | BE |
| Đánh giá | B9/B10/B11 | Fail/Block | DG-008: PUT kết quả 200 nhưng GET không persist score/state | Lỗi persistence BE | BE |
| Đánh giá | D2a | Fail | DG-009: thiếu nút HUY ở 4 state nguồn | Sai UI | FE |
| Hỏi đáp | HD-027/045/047/048/060/061/062 | Block | Cổng PLQG inbound và TVN bridge endpoint 404/chưa deploy | Phụ thuộc ngoài/thiếu endpoint | BE Integration |
| Hỏi đáp | HD-022c/d | Fail | Badge SLA xanh/cam sai tier so với BR-SLA-02 ratio | Sai UI/rule | FE/BE |
| Vụ việc | R7.4.A3-DN-BS | Block | DN test không có VV `YEU_CAU_BO_SUNG`; DN portal/VNeID T2 chưa setup | Phụ thuộc ngoài + thiếu data | Infra + Dev seed |
| Vụ việc | TVV native VV-014/015/017 | Partial | TVV detail 403 và thiếu permission update/trình duyệt VV mình xử lý | Sai permission/UI | BA + BE/FE |
| Vụ việc | CG pool | Open | Pool cá nhân thiếu CG dù spec cho TVV/CG hoặc NHT | Lỗi filter BE | BE |
| Cross/API | API-013..030/032/044 | Block | 8/9 cặp outbound endpoint 404 | Thiếu endpoint | BE |
| Cross/API | API mTLS | Block | Test env thiếu mTLS cert/JWT staging | Phụ thuộc ngoài | Infra |

## 6. Module core pass nhưng chưa sạch 100%

| Module | Core pass | Chưa sạch 100% |
|---|---|---|
| Chi trả | Core CMS v3.5, pool 40/40, 7/7 bug flow closed | DN bổ sung HS chưa chạy do thiếu HSCT/DN portal |
| Dashboard | KPI/drill-down core đã pass sau R3 | DN vẫn vào được dashboard; auto-refresh/filter/chart còn hoãn |
| Hợp đồng tư vấn | CRUD/permission/scope chính pass, Critical/Major cũ closed | TVV detail thiếu section HĐ; route standalone chờ BA |
| Hỏi đáp | Workflow nội bộ và nhiều bug UX đã closed | PLQG/bridge chưa deploy; SLA tier sai |
| Tư vấn nhanh | CMS internal flow pass | Public PLQG/mTLS và 3 bug open |
| TVCS | Workflow core covered 11/11 | Functional 53/61, 5 bug open |
| Vụ việc | Core workflow/public/lifecycle fresh pass | DN portal, mTLS privacy, TVV native, LICHSU chưa sạch |

## 7. Câu hỏi/điểm cần BA chốt

| Vấn đề | Câu hỏi cần chốt | Module |
|---|---|---|
| TVV xử lý vụ việc | TVV có phải tự cập nhật kết quả và trình phê duyệt VV mình xử lý không, hay CB NV làm thay? | Vụ việc |
| Route Hợp đồng TV | Route standalone `/hop-dong-tv/danh-sach` có thuộc scope v3.5 hay phải ẩn hoàn toàn theo spec sub-resource? | Hợp đồng tư vấn |
| Báo cáo | PDF TT17/2025 và danh sách report bắt buộc ship gồm những loại nào? | Báo cáo |

## 8. Action ưu tiên

| Ưu tiên | Việc cần làm | Module | Owner | Rerun sau khi xong |
|---|---|---|---|---|
| P0 | Fix Báo cáo data-scope leak cho BN/DP trên `/bao-cao/*` | Báo cáo | BE | BC-027/028/030/031 |
| P0 | Deploy API outbound + cấp mTLS/JWT staging | Cross/API | Infra + BE | R7.7.16 |
| P0 | Fix DG-012 state advance | Đánh giá | BE | TC14/17, B7-B11 |
| P1 | Deploy PLQG/TVN bridge | Hỏi đáp/TV nhanh | BE Integration | HD public TC, R7.6.3 |
| P1 | Fix Vụ việc TVV route/permission + CG pool | Vụ việc | BA + BE/FE | VV-014/015/017/033 native |
| P1 | Fix PDF/XLSX report export | Báo cáo | BE | BC-025 + XLSX analytic |
| P2 | Fix Dashboard DN permission | Dashboard | FE/BE | DASH-P7 |

## 9. Note tránh hiểu nhầm pass/fail

- TVV/CG hiện là **Sẵn sàng**: functional R32 đã 33/33 pass, RETRY-005 closed.
- Vụ việc không còn bug PHANCONG-REVERT/NOTIF/DANHGIA: các bug này đã closed; open mới là LICHSU, CG pool, TVV detail/permission.
- Hỏi đáp không còn chờ dev SQL backdate; SQL đã verify, vấn đề mới là **SLA tier mapping sai** và PLQG/bridge chưa deploy.
- Chi trả core CMS không fail; nhánh DN bổ sung HS bị block vì thiếu HSCT/DN portal.
- Kho QA, NHT, TC TV, Doanh nghiệp, TVV/CG là nhóm không bị block core.
- Báo cáo phải kết luận theo R6 bug report mới nhất: 4 bug open, không dùng kết luận export Excel cũ để đánh giá full module.

## 10. Tóm tắt cuối

- **Sẵn sàng:** Doanh nghiệp, Kho QA, Người hỗ trợ, Tổ chức tư vấn, TVV/CG, Pre-test/deploy gap.
- **Có điều kiện:** Chi trả, Dashboard, Hỏi đáp, Hợp đồng tư vấn, Tư vấn nhanh, TVCS, Vụ việc.
- **Chưa sẵn sàng:** Báo cáo, Cross-cutting/API, Đánh giá hiệu quả HTPL.
- **Blocker chính:** API/PLQG/VNeID/mTLS ngoài hệ thống; các lỗi BE/FE nội bộ ở Báo cáo, Đánh giá, Vụ việc; một số rule cần BA chốt.
- **Điều kiện tối thiểu để hoàn tất:** fix các P0/P1 trong bảng action, chuẩn bị dữ liệu DN/HSCT/VV YCBS, deploy endpoint ngoài hệ thống, rồi rerun đúng TC/path đã nêu.
- **TC/path cần rerun sau unblock:** R7.7.13 Báo cáo; R7.7.16 API; R7.4.D2/D2a/D2b/R7.7.9 Đánh giá; R7.6.3/R7.7.11 TV nhanh; HD public + HD-022c/d; R7.4.A3-DN-BS/R7.7.3 Vụ việc.
