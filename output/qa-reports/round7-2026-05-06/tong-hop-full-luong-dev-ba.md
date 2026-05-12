# Tổng hợp full luồng Round 7 gửi Dev/BA

Ngày tổng hợp: 2026-05-12  
Phạm vi đọc: `tasks/tmp`, `functional`, `workflow`, `bug-reports` trong `output/qa-reports/round7-2026-05-06`.  
Nguyên tắc: chỉ đọc report hiện có, không chạy lại test, không sửa code. Nếu bug report mới hơn functional/workflow report thì ưu tiên kết luận theo bug report mới nhất. Tiêu chí "full luồng/không block" trong report này chỉ xét các luồng nội bộ hệ thống; các luồng đồng bộ/kết nối ngoài như Cổng PLQG, DVC, VNeID, mTLS/JWT staging được tách riêng và không làm hạ trạng thái core nội bộ.

## 1. Bảng tổng quan

| Module | Kết luận full luồng | Nhóm | Workflow | Functional coverage | Bug Open | Bug Closed | TC/path còn thiếu | Blocker chính | Phương án để full |
|---|---|---|---|---|---:|---:|---|---|---|
| Báo cáo | Chưa sẵn sàng | C | Export Excel core OK | Core render OK, export/scope còn fail | 3 | 5 | PDF export, scope nhóm Chi phí/CG-TVV/CT, `theoKy` Hỏi đáp | Lỗi BE/export/data scope | Wire scope middleware toàn bộ `/bao-cao/*`, build PDF generator, fix aggregation |
| Chi trả | Sẵn sàng nội bộ | B/A | Core 12 bước pass | Core v3.5 pass; FR14 phụ thuộc DVC/DN portal tách riêng | 0 core; 3 external | 7+ | FR-V.II-14 DN bổ sung HS 8/18 là nhánh ngoài | Không có core blocker nội bộ | Không cần action để full core; xử lý FR14 khi có DVC/DN portal |
| Cross-cutting/API/E2E | Chưa sẵn sàng nội bộ | A/C | E2E DN partial | API 8/44 pass + 30 blocked deploy | 1 core + external | 3+ | E2E DN UC52; API deploy/cert là nhánh ngoài | Thiếu DN UC52 nội bộ + phụ thuộc ngoài | Implement DN portal UC52; deploy API/cert/JWT tách riêng |
| Đánh giá hiệu quả | Có điều kiện | C | R12 đã đóng DG-008/009/012/015 | R11/R12 còn DG-010/013/014 | 3 | 12+ | TC07/07b, TC18, TC-LV | Sai UI trọng số, permission QTHT, raw UUID | Fix DG-010, DG-013, DG-014; rerun TC liên quan |
| Dashboard | Có điều kiện | B | N/A | 33/34 pass; DASH-P8 partial | 0 formal, 1 suspect | 5 | DASH-P8.4/5/6/7 | Edge auto-refresh/manual QA/BE mock | Manual QA visibility; mock timeout/fail; verify P8.4 trước khi log |
| Doanh nghiệp | Sẵn sàng | B | Cross-module DN tabs pass | 19/20 active pass; DN-020 cut scope | 0 | 7+ | Không block core | Không có core blocker | Theo dõi VNeID Tier 3 ngoài scope |
| Hỏi đáp | Sẵn sàng nội bộ | B/A | Nội bộ 10/11 pass; TP-HD-09 là bridge ngoài | Functional bug mới đã closed R11 | 0 core; external pending | nhiều | TVN_BRIDGE/PLQG tách riêng; HD-022e tier 4 là edge seed | Không có core blocker nội bộ | Không cần action để full core; deploy PLQG/TVN bridge tách riêng |
| Hợp đồng TV | Có điều kiện | B | CRUD/permission/audit/link pass | Sau 2026-05-12: 3 open Minor | 3 | 11 | BUG-034/037/038 | Route ẩn + i18n/pagination | Guard/redirect route standalone; Việt hóa enum/pagination |
| Kho QA | Sẵn sàng | B | Manual 8/8 + auto-feed pass | N/A | 0 | 3 | Không còn block core | Không có | Không cần action để full core |
| Người hỗ trợ | Sẵn sàng | B | Seed + activation pass | 11/11 active pass | 0 | 5 | Không còn block core | Không có | Không cần action để full core |
| Tổ chức tư vấn | Sẵn sàng | B | 8/8 pass | 10/10 pass | 0 | 2+ | Không còn block core | Không có | Không cần action để full core |
| Tư vấn nhanh | Sẵn sàng nội bộ, chưa sạch 100% | B/A | CMS B1-B4 pass; public chờ PLQG tách riêng | R15-P2: 6/8 bug closed, 2 Minor open | 2 minor | 6 | TVN-005, TVN-008; R7.6.3 public là nhánh ngoài | Minor audit/warning, không block core | Bổ sung module filter Tư vấn; surface warning ERR-TVN-01; deploy PLQG tách riêng |
| TVCS | Có điều kiện | B/C | 9/11 pass + 2 external covered | R20: 4/8 closed, 4 open/partial | 4 | 4+10 | TLPL, NHT route/list, Công khai UI, NHT happy DN path | Thiếu endpoint + permission/UI | Expose TLPL CRUD; fix route guard/BE scope; finish public UI |
| TVV/CG | Sẵn sàng | B | A1/A1-CG/A1.6/A2 pass | 33/33 pass | 0 | 9+ | Không còn block core | Không có | Không cần action để full core |
| Vụ việc | Có điều kiện | C/A | Core CMS 12/12 + public pass | R18/R7.8.7 còn 2 open functional + 2 E2E | 4 | nhiều | TVV permission, LICHSU, UC52 DN portal, Accordion label | Thiếu permission/endpoint nội bộ + UI | Implement TVV action perms; normalize history enum; build DN UC52; fix UI label |

## 2. Nhóm A - Cần kết nối/đồng bộ từ ngoài hệ thống

| Module/nhánh | Phần đã OK | Phần phụ thuộc ngoài | Loại blocker | Owner đề xuất |
|---|---|---|---|---|
| Hỏi đáp / TVN bridge | Core Hỏi đáp nội bộ đã pass, SLA bug đã closed | TP-HD-09/seed TVN_BRIDGE cần Cổng PLQG endpoint + TVN bridge | Phụ thuộc ngoài/endpoint | BE Integration + Infra |
| Tư vấn nhanh public | CMS proxy, công khai KCH, auto-import HD->KQA đã closed | R7.6.3 DN public qua Cổng PLQG/mTLS, phiên `cong_khai=1` | Phụ thuộc ngoài | Infra + BE |
| Vụ việc DN bổ sung/VNeID | Core CMS/manual workflow pass | DN bổ sung HS cần VNeID T2/DVC; phần DN portal UC52 nếu là màn nội bộ thì vẫn tính ở Nhóm C | Phụ thuộc VNeID/DVC | FE/BE + Infra |
| Chi trả FR14 | Core Chi trả v3.5 full | DN bổ sung HS qua DVC/DN portal, `ngayYCBS`/DVC sandbox | Phụ thuộc ngoài + data | BE + Infra + Dev seed |
| Cross-cutting API | Upload security, hard-delete, UC renumber đã pass | API inbound/outbound, mTLS/JWT/cert staging còn gap | Thiếu endpoint/cert | Infra + BE |

## 3. Nhóm B - Đã full/core luồng, không bị block core

| Module | Core/full flow đã pass | Chưa sạch 100% nếu có | Kết luận |
|---|---|---|---|
| Doanh nghiệp | CRUD/list/filter/permission active pass, bug DN closed | DN-020 VNeID Tier 3 BA cut scope | Sẵn sàng |
| Kho QA | Thủ công 8/8 + auto BR-FLOW-10 pass, bug closed | Không | Sẵn sàng |
| Người hỗ trợ | 11/11 active pass, mail activation fixed | Không | Sẵn sàng |
| Tổ chức tư vấn | Seed/phê duyệt/workflow/functional pass | Không | Sẵn sàng |
| TVV/CG | Workflow lifecycle + functional 33/33 pass | Không | Sẵn sàng |
| Chi trả core | 12 bước + 35 TC core v3.5 pass, flow bug 7/7 closed | FR14 DN bổ sung là nhánh ngoài, không block core nội bộ | Sẵn sàng nội bộ |
| Hỏi đáp core | Flow nội bộ và bug functional đã closed R11 | Bridge/public phụ thuộc ngoài, không block core nội bộ | Sẵn sàng nội bộ |
| Tư vấn nhanh core | CMS B1-B4 pass, auto-import nội bộ đã closed | Còn TVN-005/008 minor; public PLQG tách riêng | Sẵn sàng nội bộ, chưa sạch 100% |
| Hợp đồng TV core | CRUD, payment, audit, VV/TVV link đã pass | Chỉ còn route/i18n minor | Có điều kiện |
| Dashboard core | KPI/drill/permission bug closed | Auto-refresh edge còn partial/suspect | Có điều kiện |

## 4. Nhóm C - Chưa full luồng nội bộ hoặc đang bị block nội bộ

| Module | Block ở bước/TC nào | Nguyên nhân cụ thể | Phân loại | Điều kiện unblock |
|---|---|---|---|---|
| Báo cáo | BC-025, scope BC Chi phí/CG-TVV/CT, aggregation `/hoi-dap` | PDF 422; scope middleware mới fix HD/VV, còn leak chi phí/CG-TVV; `theoKy` flat | Lỗi nội bộ BE/export | Fix BC-025 PDF; close DATA-SCOPE cho Chi phí/CG-TVV/CT; fix KYBAOCAO aggregation |
| Đánh giá | TC07/07b, TC18, TC-LV | Modal/inline `trongSo` force 100; QTHT vẫn edit Tiêu chí đợt; LV dropdown raw UUID | Sai UI/permission/data | Fix DG-010 FE binding; fix DG-013 permission guard; fix DG-014 data label |
| TVCS | BUG-001/004/005/008 | TLPL endpoint 404; NHT direct route/list leak; Công khai UI thiếu Hủy/upload; NHT happy DN path 403 | Thiếu endpoint + permission/UI | Fix TVCS-001 TLPL; TVCS-004 NHT route/BE scope; TVCS-005 public UI; TVCS-008 BR-AUTH-10 |
| Vụ việc | TVV native action, LICHSU, E2E UC52 | TVV thiếu permission cập nhật/trình/hoàn thành; history enum 15/18; DN portal chưa implement | Permission + thiếu endpoint | Fix TVV-PERMISSION-GAP; LICHSU-01; E2E-S4 DN create request; E2E-S5 UI label |
| Cross-cutting/API | R7.8.7 E2E DN UC52 | DN UC52 chưa có CTA/endpoint trong hệ thống; các API deploy/cert là nhánh ngoài tách riêng | Thiếu endpoint/UI nội bộ | Implement DN UC52; API/cert R7.7.16/R7.7.17 xử lý ở Nhóm A |

## 5. Chi tiết module đang block/cần Dev-BA chú ý

| Module | TC/path | Trạng thái mới nhất | Nguyên nhân block | Loại blocker | Owner |
|---|---|---|---|---|---|
| Báo cáo | BC-025 | Open | `/bao-cao/export` PDF 422 `ERR-RPT-EXPORT-01` trên 6 sample | Thiếu export service | BE |
| Báo cáo | DATA-SCOPE | Partial Open | HD/VV fixed, nhóm Chi phí + CG/TVV vẫn leak full national cho BN/DP | Lỗi data scope BE | BE |
| Báo cáo | KYBAOCAO | Partial Open | Validation enum fixed 12/12, nhưng aggregation `/bao-cao/hoi-dap` không group theo enum | Lỗi BE aggregation | BE |
| Đánh giá | DG-010 | Open | Modal/inline edit `trongSo` reset 100, làm TC07/07b sai spec | Sai UI | FE |
| Đánh giá | DG-013 | Open | QTHT còn edit Tiêu chí đợt/Hủy đợt trong khi chỉ R theo BA | Sai permission | FE/BE |
| Đánh giá | DG-014 | Open | Dropdown Lĩnh vực render 2 raw UUID | Data/display | BE/FE |
| Hợp đồng TV | BUG-034 | Open Minor | `/hop-dong-tv/danh-sach` standalone vẫn render, BA đã chốt route ẩn/guard | Sai route/spec | FE |
| Hợp đồng TV | BUG-037/038 | Open Minor | TVV history HD section leak enum `DANG_THUC_HIEN`, pagination "mat hang" | i18n/UI | FE |
| Tư vấn nhanh | TVN-005 | Partial Open | KHO_CAU_HOI audit OK, TU_VAN_NHANH còn legacy action; dropdown module thiếu Tư vấn | Audit/UI | BE/FE |
| Tư vấn nhanh | TVN-008 | Open Minor | Kho QA rỗng tạo phiên OK nhưng response không có warning ERR-TVN-01 | BE warning contract | BE |
| TVCS | TVCS-001 | Open | TLPL CRUD endpoint aliases 404, detail không có TLPL field | Thiếu endpoint | BE |
| TVCS | TVCS-004 | Partial | NHT sidebar fixed, direct URL/list API vẫn render 4 records | Route guard/permission | FE/BE |
| TVCS | TVCS-005 | Partial | Có button Công khai, nhưng thiếu upload fields và không có Hủy công khai | Sai UI | FE |
| TVCS | TVCS-008 | Partial | Blanket deny removed, nhưng NHT happy path với DN/VV phân công vẫn 403 | Sai BR-AUTH-10 mapping | BE |
| Vụ việc | TVV-PERMISSION-GAP | Open | TVV detail fixed, nhưng thiếu perms cập nhật KQ/trình/hoàn thành | Sai permission | BE/BA |
| Vụ việc | LICHSU-01 | Open Partial | 15/18 enum, còn alias legacy/miss enum | Data/audit | BE |
| Vụ việc | E2E-S4 | Open Critical | DN portal không có CTA/endpoint UC52 gửi yêu cầu HTPL | Thiếu endpoint/UI | FE/BE |
| Vụ việc | E2E-S5 | Open Minor | Accordion Phân công vẫn label "Dia ban" + address thay "Don vi quan ly" | Sai UI/spec | FE |

## 6. Spec / BA confirmation check

| TC/vấn đề | Câu hỏi cần xác nhận | Nguồn đã đọc | Kết luận | Verdict |
|---|---|---|---|---|
| HĐ TV route standalone | Có public route `/hop-dong-tv/danh-sach` không? | Bug HDTV 2026-05-12, note BA 2026-05-11 | BA đã chốt không public/menu; nếu giữ route thì guard/redirect | Dev FE |
| Dashboard DASH-P8.4 | Pending filter có bắt buộc không bị overwrite khi auto-refresh? | Functional dashboard R5 | Suspect bug, cần 2-source spec verify trước khi log formal | QA/BA |
| TVCS NHT BR-AUTH-10 | NHT có được đọc DN nếu có VV phân công hay không? | TVCS R20 + SRS/permission matrix trong report | Có, theo row-level BR-AUTH-10; BE vẫn 403 happy path | Dev BE |
| Vụ việc duplicate đánh giá | Duplicate score đúng mã lỗi nào? | VV R15 + BA note 2026-05-11 | BA chốt duplicate = `ERR-DG-VV-03`, permission = `ERR-DG-VV-04` | Dev BE |

## 7. Phương án để hoàn thành full luồng

| Mục tiêu | Việc cần làm tiếp | Loại blocker | Owner | Điều kiện xác nhận xong | TC/path rerun |
|---|---|---|---|---|---|
| Xử lý riêng các nhánh phụ thuộc ngoài | Deploy PLQG/DVC/VNeID/mTLS/JWT staging, cấp DN test accounts | Phụ thuộc ngoài, không tính block core nội bộ | Infra + BE | Endpoint 200/expected auth, có data test | Hỏi đáp TP-HD-09, TVN public, Chi trả FR14, Vụ việc DN-BS/API |
| Làm sạch Báo cáo | PDF generator + dataScopeMiddleware cho tất cả endpoint + fix `theoKy` | Lỗi BE | BE | PDF 200 PDF, BN/DP không leak, aggregation đúng enum | BC-025, DATA-SCOPE, KYBAOCAO |
| Full TVCS | TLPL CRUD + NHT route/list guard + public UI full + BR-AUTH-10 happy path | Thiếu endpoint/permission | BE/FE | 4 open/partial bug closed | TVCS-001/004/005/008 |
| Full Vụ việc | TVV action perms + LICHSU enum + DN UC52 portal + UI label | Permission/endpoint/UI | BE/FE | TVV có thể cập nhật/trình/hoàn thành; DN có thể tạo VV; history enum normalized | TVV-PERM, LICHSU, E2E-S4/S5 |
| Làm sạch module core đã pass | HĐ TV route/i18n, TVN audit/warning, Dashboard P8 edge | UI/UX/edge | FE/BE/QA | Open minor/suspect closed hoặc có BA verdict | HDTV-034/037/038, TVN-005/008, DASH-P8 |

## 8. Tóm tắt cuối

- Sẵn sàng/core nội bộ pass: Doanh nghiệp, Kho QA, Người hỗ trợ, Tổ chức tư vấn, TVV/CG, Chi trả core, Hỏi đáp core.
- Sẵn sàng nội bộ nhưng chưa sạch 100%: Tư vấn nhanh còn TVN-005/008 minor; HĐ TV còn route/i18n minor; Dashboard còn DASH-P8 edge/suspect.
- Chưa sẵn sàng hoặc đang block luồng nội bộ: Báo cáo, Đánh giá, TVCS, Vụ việc, Cross-cutting/E2E DN UC52.
- Module cần đồng bộ ngoài hệ thống, không tính block core nội bộ: Hỏi đáp/TVN bridge, Tư vấn nhanh public, Chi trả FR14 DVC/DN portal, Vụ việc DN bổ sung qua VNeID/DVC, Cross-cutting API/cert.
- Nếu core đã pass nhưng chưa sạch 100%: ghi rõ là "core pass, chưa sạch 100%" thay vì hạ sang block core.
- Ưu tiên Dev nội bộ: Báo cáo data scope/PDF, TVCS TLPL/permission, Vụ việc TVV perms + DN UC52, Đánh giá DG-010/013/014.
- Ưu tiên BA: xác nhận/giữ route ẩn HĐ TV, Dashboard P8.4 nếu QA formalize bug.
- Sau khi unblock nội bộ cần rerun: BC-025/DATA-SCOPE/KYBAOCAO; DG-010/013/014; TVCS-001/004/005/008; VV TVV-PERM/LICHSU/E2E-S4/S5.
