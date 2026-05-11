# Report tổng hợp full luồng Round 7 - gửi Dev/BA

Ngày tổng hợp lại: 2026-05-11  
Phạm vi nguồn đã đọc:

- `output/qa-reports/round7-2026-05-06/bug-reports`
- `output/qa-reports/round7-2026-05-06/workflow`
- `output/qa-reports/round7-2026-05-06/functional`
- `tasks/state-snapshot.md`
- `tasks/todo-bao-cao.md`
- `tasks/todo-danh-gia-hq.md`
- `tasks/todo-dashboard.md`
- `tasks/todo-doanh-nghiep.md`
- `tasks/todo-hoi-dap.md`
- `tasks/todo-hop-dong-tv.md`
- `tasks/todo-kho-qa.md`
- `tasks/todo-nht.md`
- `tasks/todo-tc-tv.md`
- `tasks/todo-tv-nhanh.md`
- `tasks/todo-tvcs.md`
- `tasks/todo-tvv-cg.md`
- `tasks/todo-vu-viec.md`

Nguyên tắc chốt trạng thái:

- Nếu `bug-reports` hoặc `tasks/todo-*` mới hơn `functional/workflow` thì ưu tiên trạng thái mới nhất.
- Nếu core workflow đã pass nhưng còn edge/cross-module bug thì ghi rõ "core pass, chưa sạch 100%".
- Những case cần VNeID, Cổng PLQG, mTLS, DVC/LGSP hoặc DN portal được note riêng là phụ thuộc ngoài hệ thống.

---

## 1. Kết luận nhanh

### 1.1 Module đã full luồng core / không còn block core

| Module | Kết luận mới nhất | Ghi chú |
| --- | --- | --- |
| 7.4 TVV/CG | Core workflow pass | R7.4.A1, A1-CG, A1.6, A2 đều pass. R7.7.2 functional còn 1 bug edge RETRY-005, không block core lifecycle. |
| 7.4a Người hỗ trợ | Pass | 11/11 active TC pass, bug mail link port `:3000` closed. |
| 7.4b Tổ chức tư vấn | Pass | Seed + phê duyệt + workflow 8/8 + functional 10/10 pass. |
| 7.5 Vụ việc | Core pass | Workflow nội bộ 12/12 pass, public công khai pass. DN bổ sung qua VNeID là phụ thuộc ngoài. |
| 7.6 Chi trả | Core pass sau R3 | Full flow R3 pass 11/12, 7/7 bug closed, pool 40/40 BR-OK. Chỉ còn DN-only bổ sung hồ sơ cần DN credential/portal. |
| 7.7 Doanh nghiệp | Pass CMS | R14 pass 19/20 active; DN-020 VNeID Tier 3 đã BA confirm cắt scope. 6/6 bug closed. |
| Kho QA | Pass toàn bộ core | Manual workflow 8/8 pass và auto-feed `TU_DONG` BR-FLOW-10 pass R10d, bug auto closed. |
| 7.12 TVCS workflow | Pass core workflow | R7.4.A5 R15 đạt 9/11 + 2 external = 11/11 covered, BUG-004 closed. Functional vẫn partial, xem mục block. |
| 7.13 Tư vấn nhanh workflow | Pass core CMS | B1-B4 pass; B5 external sync đúng spec. Functional còn partial và external. |
| QTHT Vai trò | Pass core | CRUD/guard/audit pass. |
| QTHT Nhật ký | Pass core | Read/search audit log pass. |
| QTHT Tài khoản | Pass core chính | Activation/reset/profile/self-reg các bug chính đã closed; còn một số scope nhỏ/defer không block core. |
| QTHT Danh mục/Cấu hình | Pass theo snapshot mới | Ngày lễ 2026 đã closed-verified R8; DM còn lại đủ dữ liệu/pass. |

### 1.2 Module chưa full luồng do lỗi nội bộ hoặc thiếu dữ liệu nội bộ

| Module | Mức độ | Nguyên nhân cụ thể |
| --- | --- | --- |
| 7.8 Đánh giá hiệu quả HTPL | Block full luồng | BUG-DG-008/DG-012: PUT kết quả/chấm điểm không persist hoặc không advance state, block B10/B11 và TC14/17. BUG-DG-009: UI thiếu nút Hủy ở 4 state nguồn. |
| 7.15 CT HTPLDN / Đợt báo cáo | Block full luồng | GĐ1 B10 fail 409 rule `0/0 đợt báo cáo chưa ĐÃ_TỔNG_HỢP`; GĐ2 UI blocker và BE thiếu endpoint. Cần BA xác nhận rule. |
| 7.9 Biểu mẫu | Chưa full functional | Workflow 7/8 pass, SM pass; còn MinIO public URL trỏ `localhost:9000` (BUG-BM-007 Critical), upload file sai định dạng silent reject (BUG-BM-008), UI silent khi BE 409 (BUG-BM-005). 10 CR-01 đã unblock nhưng cần retest riêng. |
| 7.3 Đào tạo | Partial | Khóa học workflow chính pass, nhưng functional còn DT-004 block do FE form thiếu `giangVienIds`; Học viên POST crash 500; lịch học thiếu validation; UI gán bài giảng thiếu nút. |
| 7.1 Dashboard | Partial | 4 bug KPI/drill-down đã closed, nhưng BUG-DASH-005 open: DN vẫn render full `/dashboard` dù permission matrix không cho DN/NHT/TVV/CG. Auto-refresh chỉ verify 1/7 sub-aspect, 6 sub-aspect cần manual QA. |
| 7.11 Báo cáo | Partial | R4 còn PDF export chưa support đúng TT17/2025 (`422 ERR-RPT-EXPORT-01`) và FE dropdown thiếu 3 loại báo cáo. Một số cross-module bị BE list 500/JWT regression trong round trước. |
| 7.14 Hợp đồng tư vấn | Conditional pass, chưa sạch | R3 16/17 pass; còn BUG-020 UI tab audit thiếu và BUG-030 FE tạo HĐ gọi `pageSize=200` vượt max 100 làm dropdown TVV/CG empty. |
| 7.12 TVCS functional | Partial | R17 53/61 pass; còn bug R16 open: permission/validation/regression nhóm 001/004/005/006/008. Workflow core đã pass. |
| 7.13 Tư vấn nhanh functional | Partial | R13 31/35 pass; còn 3 bug open/partial, 5 blocked do public/DN/mTLS, 7 defer. |
| 7.4 TVV/CG functional edge | Core pass, chưa sạch 100% | R7.7.2 đạt 32/33; RETRY-005 còn open: rule permission "NHT cùng đơn vị", bỏ endpoint `/nop-lai` riêng, BA cần fix SRS line 2314. |
| 7.2 Hỏi đáp functional | Partial | 43/60 pass Phase 9. Flow bug chính đã closed, nhưng HD-055 UX publish fail handling và HD-014 errCode mismatch vẫn open Minor; nhiều TC còn chờ Cổng PLQG/TVN bridge/seed. |
| 7.5 Vụ việc functional | Partial | Core workflow pass, nhưng functional R15 mới 29/72; NOTIF/LICHSU còn partial open, nhiều TC cần DN VNeID Tier 2. |

### 1.3 Module phụ thuộc kết nối/đồng bộ ngoài hệ thống

| Module | Phụ thuộc ngoài | Ghi chú |
| --- | --- | --- |
| 7.16 API kết nối chia sẻ | TLS/mTLS cert, JWT, outbound endpoints staging | 38/44 blocked; 8/9 cặp outbound endpoint 404; test env HTTP-only chưa verify mTLS thật. |
| 7.5 Vụ việc - DN bổ sung | VNeID T2 sandbox, DN portal, DN test account | R7.4.A3-DN-BS blocked do thiếu sandbox/token/account và endpoint chuyên trang DN. |
| 7.6 Chi trả - DN bổ sung | DN credential/portal, DVC/LGSP/PLQG | Core CMS pass; TC-FULL-04 DN-only đúng spec nên cần DN upload/credential để test. |
| 7.13 Tư vấn nhanh public | Cổng PLQG/DN portal/mTLS | Core CMS pass; R7.6.3 public còn chờ endpoint Cổng PLQG và phiên công khai. |
| 7.2 Hỏi đáp TVN bridge/PLQG | Cổng PLQG endpoint, TVN_BRIDGE | Workflow 10/11 pass; TP-HD-09 và seed TVN_BRIDGE chờ R7.6.3/external. |
| 7.7 Doanh nghiệp / 7.10 VNeID | VNeID/OOS | DN CMS pass; DN-020 Tier 3 VNeID đã được BA cắt scope trong round này. |
| 7.12 TVCS public/portal | Portal/PLQG/inbound ngoài hệ thống | Workflow core pass; các nhánh ngoài chỉ kết luận khi có môi trường tích hợp. |

---

## 2. Chi tiết theo module

### 7.1 Dashboard

Trạng thái: **Partial, không còn block KPI core nhưng còn permission bug**.

- R3 đã closed 4 bug KPI/drill-down: KPI-02, KPI-07 URL filter, KPI-03/04 composite, KPI-05/06 đúng page Khóa học.
- R3.1/R3.2 mở **BUG-DASH-005 Major**: DN render full `/dashboard` dù permission matrix SCR-I-01 không cấp dashboard cho DN/NHT/TVV/CG.
- Auto-refresh P8 mới verify chắc 1/7 sub-aspect; 6 sub-aspect cần manual QA hoặc FE refactor dropdown AntD để automation test được.

Dev cần xử lý: chặn dashboard theo permission matrix cho DN/NHT/TVV/CG.  
QA cần chạy bổ sung: manual auto-refresh 6 sub-aspect còn lại.

### 7.2 Hỏi đáp

Trạng thái: **Core workflow pass phần lớn, functional partial**.

- Workflow R7.4.A4: 10/11 pass, TP-HD-09 hoãn do TVN_BRIDGE/Cổng PLQG.
- Functional R7.7.1 Phase 9: 43/60 pass.
- Bug flow chính đã closed: HD-049 tab Tổ chức, HD-053, HD-021/022/016, HD-032/043.
- Còn open:
  - HD-055 Minor: modal publish fail UX chưa hiện đúng lỗi/nút retry.
  - HD-014 Minor: reject errCode mismatch `ERR-VAL-SYS-00-01` thay vì `ERR-PD-02`.
- Block ngoài hệ thống: PLQG inbound, TVN_BRIDGE, một số seed backdate SLA.

Kết luận: không block core nội bộ lớn, nhưng chưa full 60/60 functional.

### 7.3 Đào tạo

Trạng thái: **Partial, còn block nội bộ**.

- Workflow Khóa học/B7/B11/B12 đã unblock nhiều phần; 7 TC state machine inherit pass.
- Functional R7.7.6 R10: 15/19 TC Khóa học-pure chạy được, còn:
  - **DT-004 blocked**: FE form tạo Khóa học thiếu field required `giangVienIds`.
  - Học viên: entity đã deploy route GET nhưng POST `/hoc-viens` crash 500, block 9 TC liên quan học viên/điểm danh/kết quả.
  - Lịch học: CRUD pass nhưng validation còn 4 bug candidates open (`ERR-LH-01/03/04`, conflict overlap).
  - UI tab "Bài giảng đã gán" thiếu nút "Gán bài giảng".

Dev cần ưu tiên: FE form `giangVienIds`, Học viên POST 500, validation Lịch học.

### 7.4 TVV/CG

Trạng thái: **Core workflow pass, functional edge chưa sạch 100%**.

- R7.4.A1 TVV: 14/14 pass, 5/5 bug closed.
- R7.4.A1-CG: 14/14 pass, bug state closed.
- R7.4.A1.6: 4/4 pass, login/dashboard TVV fixed.
- R7.4.A2: R23 pass 3/3, NHT permission gap + transition bổ sung + đăng ký lại đã closed.
- R7.7.2 functional: R30 đạt 32/33, 8/9 retry bug closed.

Còn open:

- RETRY-005: rule permission "NHT cùng đơn vị", deadlock TVV `TU_CHOI` có `taiKhoanId=null`, cần bỏ endpoint `/nop-lai` riêng và BA sửa SRS line 2314.

Kết luận: **không ghi 7.4 TVV/CG là block core**. Chỉ ghi còn 1 edge/cross-module bug.

### 7.4a Người hỗ trợ

Trạng thái: **Pass**.

- Seed NHT pass.
- Functional 11/11 active pass.
- Mail activation link đã đủ host + port `:3000`; 5/5 bug closed.

### 7.4b Tổ chức tư vấn

Trạng thái: **Pass**.

- Seed + phê duyệt TC TV pass.
- Workflow 8/8 transition pass.
- Functional 10/10 pass.
- 2/2 bug functional closed.

### 7.5 Vụ việc

Trạng thái: **Core pass, functional/public/DN branches partial**.

- R7.4.A3 core workflow 12/12 pass.
- R7.4.A3-PUBLIC công khai vụ việc pass.
- Bug core flow 6/7 closed, còn PC-WRN-01 Minor open.
- R7.7.3 functional R15 mới 29/72; NOTIF/LICHSU partial open.
- R7.4.A3-DN-BS blocked do môi trường: VNeID T2 sandbox, DN test account, DN VV `YEU_CAU_BO_SUNG`, endpoint chuyên trang DN.

Kết luận: core nội bộ đạt, full module chưa đạt vì nhánh DN/VNeID và functional còn nhiều TC.

### 7.6 Chi trả

Trạng thái: **Core pass sau R3**.

- Report R3 full flow: 11/12 TC executed pass, 7/7 bug closed.
- Pool seed 40/40 BR-OK, BR-CALC đúng, BR-AUTH-05 enforced cả BE 403 và UI.
- B2/B3/B4/B6/B7/B8/B9/B10/B12 pass.
- TC-FULL-04 B5 DN bổ sung bị blocked nhưng đúng spec vì DN-only path; cần DN upload/credential.

Kết luận: không còn block core CMS. Phần còn lại là DN-only/external.

### 7.7 Doanh nghiệp

Trạng thái: **Pass CMS**.

- R7.7.4 R14 pass 19/20 active.
- 6/6 bug closed.
- DN-020 VNeID Tier 3 đã BA confirm cắt scope.
- Cross-module DN tab HSPL/KPI/Chi trả pass.

Kết luận: full CMS nội bộ đạt; VNeID/OOS không tính block nội bộ.

### 7.8 Đánh giá hiệu quả HTPL

Trạng thái: **Block full luồng**.

- Workflow D2: 8/11, còn BUG-DG-008 open: PUT `/ket-quas` không persist/không advance đúng, block B10/B11.
- D2a: BUG-DG-009 open: UI thiếu nút Hủy ở 4 state nguồn.
- D2b: blocked vì chưa có đợt `HOAN_THANH`.
- Functional R7.7.9: 12/18 pass + bug DG-010/011/012/013 open; DG-012 block TC14/17 + B7-B11.

Dev cần xử lý: persistence/advance state kết quả đánh giá, nút Hủy, các bug functional DG-010..013.  
BA cần xác nhận: rule versioning/advance state khi cập nhật kết quả.

### 7.9 Biểu mẫu

Trạng thái: **Workflow gần pass, functional chưa release được**.

- Workflow R8 lần 2: 7/8 checkpoint pass; SM 3/3 pass; BR-PUBLIC-02/03 pass; field rename và 3 field public đã present.
- R8 lần 3: BUG-BM-001 switch đã closed, 10 CR-01 unblocked nhưng chưa retest riêng.
- Còn open:
  - BUG-BM-007 Critical: preview/download redirect MinIO về `http://localhost:9000`, browser user không truy cập được.
  - BUG-BM-008 Medium: upload `.txt` bị silent reject, không toast/error.
  - BUG-BM-005 Medium: UI silent fail khi BE trả 409 `ERR-CK-01` cho thư mục rỗng.

Dev cần xử lý: `MINIO_PUBLIC_HOST`, toast validation upload, toast lỗi công khai thư mục rỗng.

### 7.10 VNeID

Trạng thái: **Phụ thuộc ngoài**.

- Các nhánh cần VNeID/OOS chưa thể kết luận end-to-end nếu chưa có sandbox/credential/endpoint.
- Không tính fail nội bộ nếu test env chưa được cấp môi trường.

### 7.11 Báo cáo

Trạng thái: **Partial, chưa ship full module**.

- R7.5.4 export Excel đã pass.
- R7.7.13 R4: 4/6 bug closed.
- Còn open:
  - BUG-BC-PDF-NOT-SUPPORTED Major: export PDF trả 422 `ERR-RPT-EXPORT-01`, chưa support PDF theo TT17/2025.
  - BUG-BC-FE-DROPDOWN-MISSING-3 Medium: dropdown chỉ hiển thị 20/23 báo cáo, thiếu `danh-gia-hieu-qua`, `chat-luong-dao-tao`, `so-luong-cg-tvv`.
- Một số cross-module từng bị block do BE list 500/JWT regression; cần retest sau khi ổn định.

Dev cần xử lý: export PDF và dropdown 23/23 loại báo cáo.  
BA cần xác nhận: format PDF theo TT17/2025 nếu chưa rõ template.

### 7.12 Tư vấn chuyên sâu

Trạng thái: **Workflow core pass, functional partial**.

- Seed TVCS pass.
- Workflow R7.4.A5 R15: 9/11 pass + 2 external = 11/11 covered, BUG-004 closed.
- Functional R7.7.5 R17: 53/61 pass, còn regression/open từ bug-report R16: 001/004/005/006/008.
- Các nhánh portal/PLQG/inbound vẫn phụ thuộc ngoài.

Kết luận: không còn block core workflow, nhưng chưa sạch functional.

### 7.13 Tư vấn nhanh

Trạng thái: **Core CMS pass, public/external partial**.

- Workflow R7.6.2: B1-B4 pass; B5 external sync Cổng PLQG/mTLS đúng spec.
- R7.6.3 public workflow chờ Cổng PLQG endpoint và phiên công khai.
- Functional R7.7.11 R13: 31/35 pass, 5 blocked, 7 defer, 3 bug open/partial.

Kết luận: core CMS đạt, full module cần môi trường public/DN/mTLS.

### 7.14 Hợp đồng tư vấn

Trạng thái: **Conditional pass, chưa sạch 100%**.

- Seed HĐ TV pass 6/6 lĩnh vực linked với Vụ việc.
- R7.7.14 R3: 16/17 pass.
- 4/6 bug closed.
- Còn open:
  - BUG-020 Medium: BE audit logs 200 và có event, nhưng UI tab audit vẫn thiếu.
  - BUG-030 Major regression: FE tạo HĐ gọi `pageSize=200`, BE max 100 nên 422, dropdown TVV/CG empty.
- Cần ≥1 VV `HOAN_THANH`; hiện snapshot có `HOAN_THANH=0` vì vụ việc auto-flip sang `DA_DANH_GIA`.

Dev cần sửa: pageSize dropdown và UI tab audit.  
BA cần xác nhận: cách lấy VV hoàn thành khi hệ thống auto-flip sang `DA_DANH_GIA`.

### 7.15 CT HTPLDN / Đợt báo cáo

Trạng thái: **Block full luồng**.

- GĐ1: 10/11 pass, B10 fail 409 với message `0/0 đợt báo cáo chưa ĐÃ_TỔNG_HỢP`.
- GĐ2: UI blocker, API chỉ pass một phần, còn endpoint thiếu.

BA cần xác nhận: rule tổng hợp khi số lượng đợt báo cáo là 0/0.  
Dev cần xử lý: endpoint thiếu và UI flow GĐ2.

### 7.16 API kết nối chia sẻ

Trạng thái: **Blocked do deployment/integration gap**.

- 6/44 test được, 38/44 blocked.
- 8/9 cặp outbound API endpoint 404.
- Test env HTTP-only, chưa có TLS/mTLS cert để verify handshake thật.
- `/api/v1/hoi-dap` là cặp duy nhất deployed nhưng vẫn bị mTLS/JWT gate.

Dev/Infra cần cung cấp: TLS staging, client cert/key, JWT test, deploy đủ 8 cặp outbound còn thiếu.

### Kho QA

Trạng thái: **Pass toàn bộ core**.

- Seed Kho QA pass.
- Manual workflow 8/8 pass.
- Auto-feed BR-FLOW-10 pass R10d: HD `DA_DUYET` tạo Kho QA `nguon=TU_DONG`.
- BUG-KHOQA-AUTO-001 closed sau dev fix lần 2.

### QTHT

Trạng thái: **Pass core**.

- Vai trò: CRUD/guard/audit pass.
- Nhật ký: read/search audit pass.
- Tài khoản: activation/reset/profile/self-reg các bug chính closed.
- Danh mục/Cấu hình: theo `state-snapshot.md`, Ngày lễ 2026 closed-verified; DM còn lại đủ dữ liệu và pass.

---

## 3. Ưu tiên xử lý cho Dev

1. **7.8 Đánh giá**: fix BUG-DG-008/DG-012 persistence + advance state, vì đang block B10/B11 và functional downstream.
2. **7.16 API kết nối chia sẻ**: deploy đủ endpoint + cấp TLS/mTLS/JWT staging.
3. **7.15 CT HTPLDN/GĐ2**: sửa endpoint thiếu và UI blocker; phối hợp BA rule `0/0 đợt báo cáo`.
4. **7.9 Biểu mẫu**: sửa MinIO public URL `localhost:9000`, upload invalid silent reject, UI silent 409.
5. **7.3 Đào tạo**: thêm `giangVienIds` vào form Khóa học, fix Học viên POST 500, validation Lịch học.
6. **7.11 Báo cáo**: implement export PDF, dropdown đủ 23/23 loại báo cáo.
7. **7.1 Dashboard**: chặn dashboard cho DN/NHT/TVV/CG theo permission matrix.
8. **7.14 HĐ tư vấn**: fix dropdown TVV/CG `pageSize=200` và UI audit tab.
9. **7.4 TVV/CG functional edge**: xử lý RETRY-005 để đạt sạch 100%.
10. **7.12 TVCS + 7.13 TV nhanh functional**: đóng các bug open còn lại sau core workflow.

## 4. Cần BA xác nhận

1. 7.15: rule tổng hợp khi `0/0 đợt báo cáo chưa ĐÃ_TỔNG_HỢP`.
2. 7.8: rule versioning/advance state khi cập nhật kết quả đánh giá.
3. 7.4 TVV/CG: SRS line 2314 cho luồng NHT cùng đơn vị và nộp lại TVV bị từ chối.
4. 7.11 Báo cáo: template PDF theo TT17/2025 và danh sách 23 báo cáo bắt buộc hiển thị.
5. 7.14 HĐ TV: nguồn VV hoàn thành khi hệ thống auto-flip `HOAN_THANH -> DA_DANH_GIA`.

## 5. Cần môi trường/kết nối ngoài

1. 7.16 API: TLS/mTLS cert, JWT, endpoint outbound staging.
2. 7.5 Vụ việc DN bổ sung: VNeID T2 sandbox, DN account, endpoint DN portal.
3. 7.6 Chi trả DN bổ sung: DN credentials/portal, DVC/LGSP/PLQG.
4. 7.13 Tư vấn nhanh public: Cổng PLQG/DN portal/mTLS.
5. 7.2 Hỏi đáp: PLQG inbound và TVN_BRIDGE.
6. 7.12 TVCS: Portal/PLQG/inbound.
7. 7.7/7.10: VNeID/OOS nếu muốn test ngoài scope CMS.

## 6. Note tránh hiểu nhầm

- **7.4 TVV/CG đã pass core workflow.** Không ghi module này là block core. Chỉ còn 1 bug edge ở R7.7.2.
- **Kho QA auto-feed đã pass.** Bản cũ từng ghi auto-feed open, nhưng todo + bug report mới nhất đã closed R10d.
- **Chi trả core đã pass sau R3.** Bản cũ từng ghi B9/B10/B12 blocked; report full flow R3 mới hơn đã đóng 7/7 bug. Chỉ còn DN-only bổ sung cần credential/portal.
- **TVCS workflow đã pass R15.** Functional vẫn partial nhưng không còn block core workflow.
- **Dashboard không còn 4 bug KPI cũ.** Hiện còn permission BUG-DASH-005 và auto-refresh sub-aspect cần manual QA.
