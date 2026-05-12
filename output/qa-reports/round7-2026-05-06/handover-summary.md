# Handover Summary Round 7

Quy ước đếm: dùng snapshot/latest trong từng report, không cộng các đoạn archive/retest cũ đã bị report mới thay thế. `Còn lại` gồm các trạng thái không phải ✅ Pass hoặc ❌ Fail: ⚠️ partial/sai spec/obs, 🚫 blocked, ⏭ defer, external/N/A/chưa test.

| Module | Workflow (Pass/Tổng) | Functional (Pass/Tổng) | Tổng TC | Pass | Fail | Còn lại | Pass rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| bao-cao | 7/7 | 34/40 | 47 | 41 | 6 | 0 | 87.2% |
| bieu-mau | 8/8 | 38/47 | 55 | 46 | 0 | 9 | 83.6% |
| chi-tra | 12/12 | 28/53 | 65 | 40 | 1 | 24 | 61.5% |
| cross-cutting | 2/13 | 35/97 | 110 | 37 | 1 | 72 | 33.6% |
| ct-htpldn | 18/18 | 25/25 | 43 | 43 | 0 | 0 | 100.0% |
| danh-gia | 8/11 | 15/22 | 33 | 23 | 5 | 5 | 69.7% |
| dao-tao | 52/54 | 18/40 | 94 | 70 | 0 | 24 | 74.5% |
| doanh-nghiep | 4/4 | 19/20 | 24 | 23 | 0 | 1 | 95.8% |
| hoi-dap | 10/11 | 48/60 | 71 | 58 | 0 | 13 | 81.7% |
| hop-dong-tv | - | 21/24 | 24 | 21 | 1 | 2 | 87.5% |
| kho-qa | 14/14 | - | 14 | 14 | 0 | 0 | 100.0% |
| nguoi-ho-tro | - | 11/11 | 11 | 11 | 0 | 0 | 100.0% |
| qtht-danh-muc | - | 25/25 | 25 | 25 | 0 | 0 | 100.0% |
| qtht-nhat-ky | - | 7/7 | 7 | 7 | 0 | 0 | 100.0% |
| qtht-tai-khoan | 37/38 | 29/29 | 67 | 66 | 0 | 1 | 98.5% |
| qtht-vai-tro | - | 11/11 | 11 | 11 | 0 | 0 | 100.0% |
| to-chuc-tu-van | 8/8 | 10/10 | 18 | 18 | 0 | 0 | 100.0% |
| tu-van-chuyen-sau | 9/11 | 56/61 | 72 | 65 | 0 | 7 | 90.3% |
| tu-van-nhanh | 4/5 | 31/44 | 49 | 35 | 0 | 14 | 71.4% |
| tu-van-vien-cg | 35/35 | 33/33 | 68 | 68 | 0 | 0 | 100.0% |
| vu-viec | 12/28 | 40/72 | 100 | 52 | 1 | 47 | 52.0% |
| **Tổng cộng** |  |  | **1008** | **774** | **15** | **219** | **76.8%** |

## Nguyên nhân các case Fail/Còn lại

Đang có **234 case chưa sạch** = **15 Fail + 219 Còn lại**. Đếm dưới đây theo **nguyên nhân chính** của từng case để tránh cộng trùng khi một case vừa thiếu dữ liệu vừa phụ thuộc endpoint ngoài.

### Tổng hợp theo nguyên nhân chính

- **86 case do Cổng PLQG / mTLS / endpoint chưa deploy**
  - Tập trung ở `cross-cutting`, `tu-van-nhanh`, `hoi-dap`, `vu-viec`.
  - Cần deploy endpoint outbound/inbound, cấp cert mTLS, có endpoint Cổng PLQG và seed dữ liệu công khai tương ứng.

- **52 case do bug nội bộ**
  - Bug FE/BE hoặc workflow/state machine chưa đúng.
  - Tập trung ở `bao-cao`, `danh-gia`, `dao-tao`, `hop-dong-tv`, `tu-van-nhanh`, `tu-van-chuyen-sau`, `vu-viec`, `tu-van-vien-cg`.

- **42 case do thiếu dữ liệu đúng trạng thái / cron / infra test**
  - Cần seed đúng state, backdate cron, wait-time, hoặc chuẩn bị pool dữ liệu.
  - Gặp nhiều ở `cross-cutting`, `chi-tra`, `hoi-dap`, `vu-viec`, `tu-van-nhanh`.

- **29 case do VNeID / DVC / DN portal**
  - Gồm VNeID Tier 2/Tier 3, DVC sandbox, chuyên trang DN hoặc DN portal chưa sẵn sàng.
  - Tập trung ở `vu-viec`, `chi-tra`, `doanh-nghiep`, một phần `tu-van-chuyen-sau`.

- **23 case do BA/spec/permission cần chốt**
  - Cần BA xác nhận rule hoặc cập nhật spec/permission matrix.
  - Tập trung ở `bieu-mau`, `dao-tao`, `hop-dong-tv`, `vu-viec`.

- **2 case do test-method / fixture / workflow legacy**
  - Không phải bug hiện hành.
  - Gồm fixture/test-env phụ trợ và workflow cũ cần rerun đúng method.

### Theo từng module

- **bao-cao: 6 case chưa sạch**
  - **6 do bug nội bộ/partial scope**
  - Còn lỗi PDF export, scope leak nhóm Chi phí/TVV, kỳ báo cáo partial.
  - Dữ liệu BC HD/VV đã có, không phải do VNeID hay PLQG.

- **bieu-mau: 9 case chưa sạch**
  - **6 do BA/spec/permission cần chốt**
  - **3 do fixture/test-env phụ trợ**
  - Bug workflow/function/bulk import đã closed.
  - Còn BM-045 mâu thuẫn BR-PUBLIC-01 vs test plan, NHT scope permission-matrix, TVV password/CMS-mTLS/DN portal phụ trợ.

- **chi-tra: 25 case chưa sạch**
  - **10 do DVC/LGSP sandbox hoặc receiver endpoint chưa sẵn sàng**
  - **8 do bug nội bộ**
  - **5 do dữ liệu hồ sơ đúng state**
  - **2 do external/DVC out-of-scope tạm thời**
  - **0 case đang chờ BA/spec để quyết định hướng xử lý chính.**
  - BA/spec update đã được áp dụng: FR-V.II-14 là **DVC-only**, không phải CB NV upload thủ công trên CMS. Wording "hoặc CB NV (thủ công)" chỉ còn là doc drift/minor, không phải blocker nghiệp vụ.
  - Còn nhiều vì nhóm FR-V.II-14 mới có 18 TC riêng: 8 pass, 1 fail bug nội bộ `ngayYeuCauBoSung = null`, 7 blocked do thiếu LGSP/DVC receiver endpoint, 2 skip/defer do DVC sandbox ngoài scope.

- **cross-cutting: 73 case chưa sạch**
  - **55 do Cổng PLQG / mTLS / endpoint chưa deploy**
  - **15 do cron/backdate/wait-time/infra test**
  - **3 do bug E2E nội bộ**
  - Cần deploy 9 outbound + 3 internal endpoint, cấp mTLS cert, seed CT `DA_CONG_BO`, xử lý UC52/POST `/vu-viecs`.

- **ct-htpldn: 0 case**
  - Đã sạch trong scope tổng hợp.

- **danh-gia: 10 case chưa sạch**
  - **10 do bug nội bộ**
  - Còn lỗi PUT kết quả không persist, thiếu nút Hủy đợt, state không advance, permission/dropdown/UX.
  - Cần dev fix rồi seed đợt `HOAN_THANH` để rerun.

- **dao-tao: 24 case chưa sạch**
  - **8 do bug nội bộ**
  - **8 do endpoint/entity chưa deploy**
  - **8 do BA/spec/permission matrix**
  - Còn DT-038 gán bài giảng, DT-053 CPF công khai, KQHT/Điểm danh 404, chuyên trang DN/NHT thiếu inbound public endpoints, DT-032..036 chờ permission-matrix.

- **doanh-nghiep: 1 case chưa sạch**
  - **1 do VNeID Tier 3 / scope BA**
  - DN-020 blocked do xác thực Tier 3 VNeID, BA đã ghi nhận cắt scope round này.

- **hoi-dap: 13 case chưa sạch**
  - **8 do Cổng PLQG / TVN bridge**
  - **5 do dữ liệu/spec/SLA tier đặc biệt hoặc partial cần rerun**
  - TP-HD-09 và TVN_BRIDGE chờ R7.6.3: endpoint Cổng PLQG deploy + seed phiên TVN bridge.

- **hop-dong-tv: 3 case chưa sạch**
  - **2 do bug nội bộ**
  - **1 do BA/spec**
  - BUG-032 thiếu section Hợp đồng TV trong TVV detail.
  - BUG-034 standalone route `/hop-dong-tv/danh-sach` chờ BA quyết định xóa hay giữ ẩn.

- **kho-qa: 0 case**
  - Đã sạch trong scope tổng hợp.

- **nguoi-ho-tro: 0 case**
  - Đã sạch trong scope tổng hợp.

- **qtht-danh-muc: 0 case**
  - Đã sạch, bug danh mục đã closed.

- **qtht-nhat-ky: 0 case**
  - Đã sạch, audit log pass 7/7.

- **qtht-tai-khoan: 1 case chưa sạch**
  - **1 do workflow legacy/test method**
  - Không phải bug open. Folder `bug-reports/qtht-tai-khoan` đã pass/closed toàn bộ.
  - Còn partial workflow mail kích hoạt do UI-only/token race ở report cũ.

- **qtht-vai-tro: 0 case**
  - Đã sạch, pass 11/11.

- **to-chuc-tu-van: 0 case**
  - Đã sạch trong scope tổng hợp.

- **tu-van-chuyen-sau: 7 case chưa sạch**
  - **4 do bug nội bộ/partial open**
  - **2 do Portal DN/cron/external**
  - **1 do thiếu seed liên kết Vụ việc**
    - Cụ thể: **TV-041** cần một TVCS có `vuViecId` trỏ tới Vụ việc seed hợp lệ để verify link TVCS -> Vụ việc. Hiện field `vuViecId` có trong detail nhưng chưa có record TVCS gắn với Vụ việc đủ điều kiện, nên chưa test được link.
    - Cách xử lý: hoàn tất/confirm seed R7.4.A3 Vụ việc, tạo hoặc patch một TVCS hợp lệ gắn `vuViecId`, rồi rerun TV-041.
  - Workflow core đã cover, còn bug R16 001/004/005/008 và nhánh Portal DN/cron/external.

- **tu-van-nhanh: 14 case chưa sạch**
  - **7 do Cổng PLQG / mTLS / DN-side outbound**
  - **4 do defer data/infra/search/DB-level**
  - **3 do bug nội bộ**
  - Workflow public DN chờ phiên `cong_khai=1` và endpoint PLQG deploy.

- **tu-van-vien-cg: 0 case chưa sạch**
  - Workflow/functional chính đã pass 100%; các bug retry/permission/mail đã closed.

- **vu-viec: 48 case chưa sạch**
  - **16 do VNeID Tier 2 / DN portal**
  - **8 do Cổng PLQG / mTLS**
  - **8 do bug nội bộ**
  - **8 do dữ liệu/state/privacy setup**
  - **8 do BA/spec/permission cần chốt**
  - DN bổ sung hồ sơ cần VNeID T2 sandbox URL/token, DN account verified T2, seed VV `YEU_CAU_BO_SUNG`, endpoint DN portal. Functional còn cần mTLS PLQG cert và fix CG pool/TVV detail 403/TVV permission.

## Các TC chưa chạy do thiếu data/setup

Quy ước lọc: chỉ liệt kê TC còn kẹt vì thiếu seed/data đúng trạng thái, account test, hoặc backdate/time-state setup. Không tính các TC kẹt thuần do bug, VNeID, DVC/Cổng PLQG/mTLS, endpoint chưa deploy, hoặc BA/spec.

### Tổng hợp nhanh

| Module | Số TC/data setup | TC |
|---|---:|---|
| chi-tra | 5 | TC-FULL-04, CT-014, CT-017, CT-018, CT-032 |
| cross-cutting | 1 | API-027 |
| danh-gia | 5 | D2-B6..B10 |
| dao-tao | 9 | DT-011, DT-011a, DT-019, DT-031b/c/d, DT-054, DT-055, DT-056a/ERR-LH-05 |
| tu-van-chuyen-sau | 1 | TV-041 |
| tu-van-nhanh | 4 | TVN-032, TVN-034-positive, TVN-035/036 role variants, TVN-039 phần audit còn thiếu data/event |
| vu-viec | 5 | C3-1/2/3, R7.7.3-PRIVACY-1/2 |
| **Tổng** | **30** |  |

### Chi tiết dễ xử lý

- **chi-tra — 5 TC**
  - **TC-FULL-04 / B5 DN bổ sung:** cần DN owner hoặc HSCT `YEU_CAU_BO_SUNG` gắn với QA DN để DN login bổ sung hồ sơ.
  - **CT-014:** cần vòng lặp phê duyệt/trả về lần 2 để có ≥2 bản ghi `PHE_DUYET_CHI_TRA` cho cùng hồ sơ.
  - **CT-017:** cần hồ sơ/DN path có dữ liệu tiền không hợp lệ (`phi_tu_van <= 0` hoặc `so_tien_de_nghi <= 0`).
  - **CT-018:** cần DN đã chi khoảng 80-90% trần năm + HSCT mới để test over-cap.
  - **CT-032:** cần DN owner login được để test DN rút hồ sơ `CHO_TIEP_NHAN -> HUY`.

- **cross-cutting — 1 TC**
  - **API-027:** cần ít nhất 1 chương trình HTPLDN trạng thái `DA_CONG_BO`. Lưu ý: outbound endpoint cũng đang chưa deploy, nhưng data `DA_CONG_BO` vẫn là prerequisite phải chuẩn bị trước.

- **danh-gia — 5 bước workflow**
  - **D2-B6..B10:** cần ≥3 Vụ việc trạng thái `HOAN_THANH`, đúng date range và phạm vi đơn vị để chọn vào đợt đánh giá.
  - Lưu ý: hiện còn bug/state sau duyệt PC cần dev xử lý; sau khi fix vẫn phải seed lại VV `HOAN_THANH` để rerun nhóm này.

- **dao-tao — 9 TC**
  - **DT-011, DT-011a:** cần Học viên hợp lệ gắn `lich_hoc_id` để test điểm danh.
  - **DT-019:** cần đủ `DANG_KY_DAO_TAO` để chạm/vượt sức chứa khóa học.
  - **DT-031b/c/d:** cần Học viên + kết quả khóa học đã công bố + setup chuyên trang/mock để test công bố, hủy công bố, retry.
  - **DT-054, DT-055:** cần `KET_QUA_HOC_TAP` cho học viên đạt/không đạt ngưỡng.
  - **DT-056a / ERR-LH-05:** cần Học viên đã điểm danh để test xóa buổi học có điểm danh.

- **tu-van-chuyen-sau — 1 TC**
  - **TV-041:** cần TVCS có `vuViecId` trỏ tới Vụ việc seed hợp lệ để test link TVCS -> Vụ việc.

- **tu-van-nhanh — 4 mục**
  - **TVN-032:** cần phiên `MOI` backdated >30 ngày hoặc cron/test hook timeout.
  - **TVN-034-positive:** cần ít nhất 1 Kho câu hỏi scoped BN/BKH để verify BN thấy dữ liệu của chính BN. Negative no-leak đã pass.
  - **TVN-035/036 role variants:** phần NHT/CG/DN đã pass; còn cần account TVV/GV dedicated nếu muốn cover đủ toàn bộ role variants.
  - **TVN-039 phần audit còn thiếu:** cần đủ event IMPORT/CONG_KHAI/DANH_GIA/AUTO_HET_HAN để verify audit log đầy đủ.

- **vu-viec — 5 TC**
  - **C3-1/2/3:** cần Vụ việc có deadline backdated 11/16/21 ngày để test các mức SLA còn lại.
  - **R7.7.3-PRIVACY-1/2:** cần bộ dữ liệu multi-DN/cross-DN: DN test có Vụ việc của chính mình và Vụ việc của DN khác để verify privacy/scope.

### Không còn tính là thiếu data

- **Hỏi đáp HD-022c/d:** data backdate đã có, TC đã chạy và phát hiện bug SLA tier; hiện là bug, không phải thiếu data.
- **TVCS TV-038/TV-053/TV-059:** đã pass ở R20, không còn nằm trong danh sách data gap.
- **TVN-034/035/036 phần chính:** đã pass ở R13; chỉ còn các biến thể positive/role mở rộng như liệt kê trên.
