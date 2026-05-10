# Report tổng hợp full luồng Round 7 - gửi Dev/BA

Ngày tổng hợp: 2026-05-10  
Nguồn kiểm tra:

- `output/qa-reports/round7-2026-05-06/functional`
- `output/qa-reports/round7-2026-05-06/workflow`
- `output/qa-reports/round7-2026-05-06/bug-reports`
- `output/funtion`

## 1. Kết luận nhanh

### Nhóm đã full luồng / không còn block core

| Module | Kết luận | Ghi chú |
| --- | --- | --- |
| 7.5 Vụ việc | Đã full luồng core | Workflow nội bộ đạt đủ 12/12 transition. Các nhánh DN portal/public/VNeID là phần phụ thuộc ngoài hệ thống. |
| 7.4 TVV/CG | Đã pass core lifecycle | Đã kiểm tra lại theo bug report: các bug A1/A6/7.2 chính đã closed. Không đưa 7.4 vào nhóm block core. Vẫn còn vài edge/cross-module chưa sạch 100%, xem mục 3. |
| 7.4a Người hỗ trợ | Đã pass | Functional active TC đạt 11/11, bug mail link đã closed. |
| 7.4b Tổ chức tư vấn | Đã pass | Workflow 8/8 transition, functional core cũng pass. |
| Kho QA - luồng thủ công | Đã pass | Bug report mới nhất ghi 2/2 bug closed, bao gồm nút chuyển `HET_HIEU_LUC -> DA_DUYET`. |
| 7.13 Tư vấn nhanh - core CMS | Đã pass có điều kiện | Luồng CMS nội bộ đủ dữ liệu đã pass. Các phần public/DN/mTLS là phụ thuộc ngoài. |
| 7.7 Doanh nghiệp - CMS | Gần full luồng | Core CMS đã pass phần lớn. Còn lỗi `/me` thiếu `linhVucIds`; VNeID/self-service là phụ thuộc ngoài. |
| QTHT Vai trò | Đã pass core | Create/update/toggle/delete/guard/audit đã đạt. |
| QTHT Nhật ký | Đã pass core | Read/search audit log đạt. |
| QTHT Tài khoản | Đã pass core chính | Activation/reset/profile cơ bản đạt; còn một số mismatch nhỏ/defer không chặn core. |

### Nhóm còn block full luồng do lỗi nội bộ

| Module | Mức độ | Nguyên nhân chính |
| --- | --- | --- |
| 7.8 Đánh giá | Block full luồng | Bước B9 chấm điểm PUT trả 200 nhưng GET lại không lưu/version reset/null, nên UI mất điểm và block B10/B11. |
| 7.15 CT HTPLDN / Đợt báo cáo | Block full luồng | GĐ1 còn B10 fail 409 do điều kiện `0/0 đợt báo cáo chưa ĐÃ_TỔNG_HỢP`; GĐ2 UI bị blocker và BE thiếu endpoint cho một nhánh. Cần BA/dev xác nhận rule. |
| 7.9 Biểu mẫu | Chưa full luồng | Core CRUD/state đạt nhưng còn 3 bug critical: thiếu 4 field public, clear timestamp BR-PUBLIC-02, preview/download MinIO trả localhost; 11 TC bị block. |
| 7.14 Hợp đồng tư vấn | Chưa full luồng | 13/17 pass có điều kiện. Còn auth bypass QTHT CUD, thiếu cập nhật trạng thái thanh toán, thiếu audit endpoints, link N:N lỗi, chưa có picker TVV. |
| 7.1 Dashboard | Chưa full luồng drill-down/KPI | Có 4 bug open: KPI mismatch, URL drill-down thiếu filter, composite state mismatch, một số KPI điều hướng sai page. |
| 7.3 Đào tạo | Chưa full luồng phân phối | 6/8 pass. Bước distribute bị block do DB không có Khóa học hợp lệ, endpoint có tồn tại và check FK. Đây là thiếu dữ liệu nội bộ, không phải tích hợp ngoài. |
| Kho QA - auto-feed | Chưa full luồng tự động | Luồng thủ công đã pass nhưng auto-feed BR-FLOW-10 vẫn open: Hồ sơ/biểu mẫu được duyệt chưa tự đẩy vào Kho QA với `nguon=TU_DONG`. |
| 7.4 TVV/CG - edge/cross-module | Core pass, còn lỗi phụ | Còn 3 bug retry open: xóa TVV đang link VV trả 204 thay vì 409; thiếu transition `TU_CHOI -> CHO_THAM_DINH`; thiếu endpoint `DANH_GIA_SAU_VU_VIEC`. Không chặn core lifecycle nhưng chưa sạch 100% functional. |
| 7.2 Hỏi đáp | Chưa full luồng một số nhánh | Nhiều phase đã pass, nhưng modal phân công tab Tổ chức không render danh sách TC dù API có dữ liệu; ngoài ra inbound PLQG/TVN bridge phụ thuộc ngoài. |
| 7.12 Tư vấn chuyên sâu | Chưa full luồng | Functional mới nhất còn nhiều blocked/fail; workflow bị kẹt do BE chưa ack `ketQua`, cascade block B6/B7-B11; thêm lỗi permission HSPL overgrant và detail 500. |
| QTHT Danh mục | Chưa sạch hoàn toàn | Phần lớn pass nhưng bug tạo Ngày lễ silent fail vẫn open. |

### Nhóm cần kết nối/đồng bộ từ ngoài hệ thống

| Module | Phụ thuộc ngoài | Ghi chú cho Dev/BA |
| --- | --- | --- |
| 7.16 API kết nối chia sẻ | mTLS/JWT/TLS staging, outbound service | 38/44 TC bị block; nhiều cặp endpoint outbound 404. Cần môi trường/cert/endpoint tích hợp đúng. |
| 7.6 Chi trả | LGSP/DVC/PLQG, dữ liệu DN bổ sung, credentials | Có cả lỗi nội bộ B9/BR-OK và phụ thuộc ngoài. Cần tách rõ phần nội bộ có thể fix trước, phần tích hợp cần môi trường. |
| 7.13 Tư vấn nhanh | DN portal/Cổng/mTLS/public submit/evaluate | Core CMS đã pass; các TC public/DN/mTLS chưa kết luận nếu chưa có tích hợp ngoài. |
| 7.2 Hỏi đáp | Inbound PLQG, TVN_BRIDGE | Core nhiều nhánh pass; HD-027 inbound CONG_PLQG endpoint 404 và HD-048 thiếu dữ liệu bridge. |
| 7.5 Vụ việc | VNeID, DN portal, public portal | Core nội bộ đã full. Các nhánh ngoài không nên tính là block core nội bộ. |
| 7.12 Tư vấn chuyên sâu | Portal/PLQG/inbound ngoài hệ thống | Ngoài phụ thuộc ngoài, module này vẫn còn lỗi nội bộ cần sửa trước. |
| 7.7 Doanh nghiệp | VNeID/self-service/OOS | Core CMS gần full; VNeID và một số OOS cần môi trường ngoài. |
| 7.10 VNeID | VNeID/OOS | Cần môi trường/luồng tích hợp ngoài để xác nhận end-to-end. |

## 2. Chi tiết theo module

### 7.1 Dashboard

Trạng thái: **Chưa full luồng**.

Nguyên nhân:

- KPI-02 mismatch số liệu.
- KPI-07 drill-down URL thiếu filter.
- KPI-03/04 composite state mismatch.
- KPI-05/06 điều hướng sai page.

Hướng xử lý:

- Dev kiểm tra mapping trạng thái, rule tổng hợp KPI và URL filter.
- BA xác nhận công thức KPI nếu spec hiện tại chưa rõ.

### 7.2 Hỏi đáp

Trạng thái: **Pass nhiều nhánh core, nhưng chưa full toàn module**.

Nguyên nhân:

- Modal phân công tab Tổ chức không render danh sách TC dù API trả dữ liệu.
- Inbound PLQG/CONG_PLQG endpoint 404.
- TVN_BRIDGE thiếu dữ liệu/luồng đồng bộ.

Phân loại:

- Lỗi render tab Tổ chức: lỗi nội bộ cần dev sửa.
- PLQG/TVN_BRIDGE: cần kết nối/đồng bộ ngoài hệ thống.

### 7.3 Đào tạo

Trạng thái: **Chưa full luồng phân phối**.

Nguyên nhân:

- 6/8 pass.
- Bước distribute bị block vì DB không có Khóa học hợp lệ.
- Endpoint tồn tại và check FK đúng, nên hiện tại là thiếu dữ liệu prerequisite nội bộ.

Hướng xử lý:

- Chuẩn bị seed Khóa học hợp lệ để chạy lại full luồng.
- BA xác nhận rule dữ liệu đầu vào nếu cần.

### 7.4 TVV/CG

Trạng thái: **Đã pass core lifecycle**.

Ghi chú quan trọng:

- Đã kiểm tra lại bug report mới: các bug chính của luồng A1/A6/7.2 đã closed.
- Không còn xếp 7.4 TVV/CG vào nhóm block core.

Phần còn mở nhưng không chặn core lifecycle:

- Xóa TVV đang link VV vẫn trả 204/hard-delete, kỳ vọng 409 `ERR-TVV-05`.
- Thiếu transition endpoint `TU_CHOI -> CHO_THAM_DINH`.
- Thiếu endpoint `DANH_GIA_SAU_VU_VIEC`.

Hướng xử lý:

- Dev xử lý 3 bug retry để module sạch functional/cross-module 100%.
- BA xác nhận rule transition và đánh giá sau vụ việc nếu spec còn thiếu.

### 7.4a Người hỗ trợ

Trạng thái: **Đã pass**.

Ghi chú:

- Functional active TC đạt 11/11.
- Bug mail link đã closed.

### 7.4b Tổ chức tư vấn

Trạng thái: **Đã pass**.

Ghi chú:

- Workflow 8/8 transition.
- Functional core pass, bug liên quan đã closed.

### 7.5 Vụ việc

Trạng thái: **Đã full luồng core nội bộ**.

Ghi chú:

- Core workflow đạt 12/12 transition.
- Các nhánh DN portal/public/VNeID là phụ thuộc ngoài hệ thống, không tính là block core nội bộ.

### 7.6 Chi trả

Trạng thái: **Chưa full luồng**.

Nguyên nhân:

- Có các bước bị block do phụ thuộc LGSP/DVC/PLQG/credentials.
- Có lỗi/dữ liệu nội bộ ở B9: CPD -> `DA_DUYET` bị block do điều kiện BR-OK/calculation.

Phân loại:

- Phụ thuộc ngoài: LGSP/DVC/PLQG, dữ liệu DN bổ sung, credentials.
- Nội bộ: rule BR-OK/calculation và dữ liệu CPD cần dev/BA kiểm tra.

### 7.7 Doanh nghiệp

Trạng thái: **Core CMS gần full luồng, chưa sạch 100%**.

Nguyên nhân còn lại:

- `/me` thiếu `linhVucIds`.
- VNeID/self-service/OOS là phụ thuộc ngoài hệ thống.

Hướng xử lý:

- Dev bổ sung field `/me`.
- BA/dev tách tiêu chí pass cho CMS nội bộ và tiêu chí cần VNeID/OOS.

### 7.8 Đánh giá

Trạng thái: **Block full luồng**.

Nguyên nhân:

- B9 chấm điểm PUT `/ket-quas` trả 200 và có score tính toán.
- Sau đó GET lại trả version=1/null, UI reset điểm.
- Vì không persist kết quả nên B10/B11 bị block.

Hướng xử lý:

- Dev kiểm tra persistence/versioning của kết quả đánh giá.
- BA xác nhận rule cập nhật version nếu có.

### 7.9 Biểu mẫu

Trạng thái: **Chưa full luồng**.

Nguyên nhân:

- Core CRUD/state đạt.
- Thiếu 4 public fields.
- BR-PUBLIC-02 clear timestamp.
- Preview/download MinIO trả URL localhost.
- 11 TC bị block.

Hướng xử lý:

- Dev sửa contract public fields và public timestamp.
- Dev cấu hình MinIO/public URL đúng môi trường test.

### 7.10 VNeID

Trạng thái: **Cần kết nối ngoài để kết luận end-to-end**.

Nguyên nhân:

- Phụ thuộc VNeID/OOS.
- Không nên tính fail nội bộ nếu chưa có môi trường tích hợp đầy đủ.

### 7.12 Tư vấn chuyên sâu

Trạng thái: **Chưa full luồng**.

Nguyên nhân nội bộ:

- BE chưa ack `ketQua`, làm cascade block B6/B7-B11.
- Permission HSPL overgrant.
- Detail API có lỗi 500.

Phụ thuộc ngoài:

- Portal/PLQG/inbound ngoài hệ thống.

Hướng xử lý:

- Dev ưu tiên sửa BE ack `ketQua`, permission, detail 500.
- Sau đó mới chạy lại các nhánh portal/PLQG khi có môi trường ngoài.

### 7.13 Tư vấn nhanh

Trạng thái: **Core CMS pass có điều kiện**.

Ghi chú:

- Core CMS đã pass khi đủ dữ liệu.
- B5 và các nhánh public/DN/mTLS cần đồng bộ ngoài hệ thống.

Các điểm còn theo dõi:

- Authz CB_NV approve/reject.
- Audit naming.
- Suggestion count minor.

### 7.14 Hợp đồng tư vấn

Trạng thái: **Chưa full luồng**.

Nguyên nhân:

- 13/17 pass có điều kiện.
- Auth bypass với QTHT CUD.
- Thiếu cập nhật trạng thái thanh toán.
- Thiếu audit endpoints.
- N:N link lỗi.
- Chưa có TVV picker.

Hướng xử lý:

- Dev fix authz trước vì đây là rủi ro nghiêm trọng.
- BA xác nhận rule thanh toán, audit và liên kết N:N.

### 7.15 CT HTPLDN / Đợt báo cáo

Trạng thái: **Block full luồng**.

Nguyên nhân:

- GĐ1: 10/11 pass, B10 fail 409 với thông báo `0/0 đợt báo cáo chưa ĐÃ_TỔNG_HỢP`.
- GĐ2: UI bị blocker toàn luồng; API chỉ pass một phần, có endpoint còn thiếu.

Hướng xử lý:

- BA xác nhận rule điều kiện tổng hợp khi số lượng đợt báo cáo là 0/0.
- Dev bổ sung endpoint/khơi thông UI flow.

### 7.16 API kết nối chia sẻ

Trạng thái: **Block do kết nối ngoài/môi trường tích hợp**.

Nguyên nhân:

- 38/44 TC bị block.
- Thiếu mTLS cert/TLS staging/JWT setup.
- 8/9 outbound endpoint pairs 404.

Hướng xử lý:

- Dev/Infra cung cấp cert, endpoint staging, config JWT/mTLS.
- Sau khi có môi trường đúng, QA chạy lại toàn bộ API integration.

### Kho QA

Trạng thái: **Luồng thủ công pass, auto-feed chưa pass**.

Ghi chú:

- Manual Kho QA: 2/2 bug closed, luồng duyệt/hiệu lực đã pass.
- Auto-feed BR-FLOW-10 vẫn open: hồ sơ/biểu mẫu được duyệt chưa tự đẩy Kho QA với `nguon=TU_DONG`.

Hướng xử lý:

- Dev kiểm tra job/event auto-feed sau khi hồ sơ/biểu mẫu chuyển trạng thái duyệt.
- BA xác nhận nguồn `TU_DONG` và thời điểm tạo bản ghi Kho QA.

### QTHT Danh mục

Trạng thái: **Phần lớn pass, còn bug nhỏ nhưng cần fix**.

Nguyên nhân:

- Bug tạo Ngày lễ silent fail vẫn open.

Hướng xử lý:

- Dev sửa create Ngày lễ để trả lỗi rõ hoặc tạo thành công đúng DB.

## 3. Danh sách ưu tiên xử lý

### Ưu tiên P0/P1 cho Dev

1. 7.14 Hợp đồng tư vấn: auth bypass QTHT CUD.
2. 7.8 Đánh giá: kết quả chấm điểm không persist, block B10/B11.
3. 7.12 Tư vấn chuyên sâu: BE không ack `ketQua`, cascade block workflow.
4. 7.15 CT HTPLDN / Đợt báo cáo: UI blocker và endpoint thiếu.
5. 7.16 API kết nối chia sẻ: chuẩn bị mTLS/JWT/endpoint staging nếu muốn test integration.
6. 7.9 Biểu mẫu: public fields/timestamp/MinIO URL.
7. Kho QA auto-feed: dữ liệu duyệt chưa tự vào Kho QA.
8. 7.1 Dashboard: KPI/drill-down sai mapping.

### Cần BA xác nhận rule

1. 7.15: rule tổng hợp khi `0/0 đợt báo cáo`.
2. 7.4 TVV/CG: transition `TU_CHOI -> CHO_THAM_DINH` và `DANH_GIA_SAU_VU_VIEC`.
3. 7.14: rule thanh toán, audit, liên kết N:N.
4. 7.6 Chi trả: rule BR-OK/calculation CPD.
5. 7.8 Đánh giá: rule versioning khi cập nhật kết quả.

### Cần môi trường/kết nối ngoài

1. 7.16 API kết nối chia sẻ: mTLS/JWT/TLS staging/outbound endpoint.
2. 7.6 Chi trả: LGSP/DVC/PLQG/credentials.
3. 7.13 Tư vấn nhanh: DN portal/Cổng/mTLS/public.
4. 7.2 Hỏi đáp: PLQG/TVN_BRIDGE.
5. 7.5 Vụ việc: VNeID/DN portal/public.
6. 7.12 Tư vấn chuyên sâu: Portal/PLQG.
7. 7.7 Doanh nghiệp và 7.10 VNeID: VNeID/OOS.

## 4. Note riêng về 7.4 TVV/CG

Kết luận sau khi kiểm tra lại bug report: **7.4 TVV/CG đã pass core lifecycle**.

Không nên ghi 7.4 là module bị block full luồng core. Cách ghi đúng hơn:

- Core lifecycle: **Pass**.
- Functional/cross-module edge cases: **còn 3 bug open**, cần fix để đạt sạch 100%.

Ba bug còn mở không làm phủ định kết quả pass core, nhưng cần đưa vào backlog để dev xử lý.
