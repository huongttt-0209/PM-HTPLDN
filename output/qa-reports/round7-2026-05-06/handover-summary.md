# Handover Summary Round 7

Quy ước đếm: dùng snapshot/latest trong từng report, không cộng các đoạn archive/retest cũ đã bị report mới thay thế. `Còn lại` gồm các trạng thái không phải ✅ Pass hoặc ❌ Fail: ⚠️ partial/sai spec/obs, 🚫 blocked, ⏭ defer, external/N/A/chưa test.

| Module | Workflow (Pass/Tổng) | Functional (Pass/Tổng) | Tổng TC | Pass | Fail | Còn lại | Pass rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| bao-cao | 4/7 | 34/40 | 47 | 38 | 8 | 1 | 80.9% |
| bieu-mau | 8/8 | 31/47 | 55 | 39 | 0 | 16 | 70.9% |
| chi-tra | 10/12 | 20/35 | 47 | 30 | 3 | 14 | 63.8% |
| cross-cutting | 2/13 | 35/97 | 110 | 37 | 1 | 72 | 33.6% |
| ct-htpldn | 17/18 | 25/25 | 43 | 42 | 1 | 0 | 97.7% |
| danh-gia | 8/11 | 15/22 | 33 | 23 | 5 | 5 | 69.7% |
| dao-tao | 51/54 | 17/40 | 94 | 68 | 0 | 26 | 72.3% |
| doanh-nghiep | 4/4 | 19/20 | 24 | 23 | 0 | 1 | 95.8% |
| hoi-dap | 3/11 | 46/60 | 71 | 49 | 2 | 20 | 69.0% |
| hop-dong-tv | - | 21/24 | 24 | 21 | 1 | 2 | 87.5% |
| kho-qa | 14/14 | - | 14 | 14 | 0 | 0 | 100.0% |
| nguoi-ho-tro | - | 11/11 | 11 | 11 | 0 | 0 | 100.0% |
| qtht-danh-muc | - | 24/25 | 25 | 24 | 0 | 1 | 96.0% |
| qtht-nhat-ky | - | 7/7 | 7 | 7 | 0 | 0 | 100.0% |
| qtht-tai-khoan | 37/38 | 22/29 | 67 | 59 | 1 | 7 | 88.1% |
| qtht-vai-tro | - | 8/11 | 11 | 8 | 0 | 3 | 72.7% |
| to-chuc-tu-van | 8/8 | 10/10 | 18 | 18 | 0 | 0 | 100.0% |
| tu-van-chuyen-sau | 9/11 | 56/61 | 72 | 65 | 0 | 7 | 90.3% |
| tu-van-nhanh | 4/5 | 30/44 | 49 | 34 | 0 | 15 | 69.4% |
| tu-van-vien-cg | 33/35 | 33/33 | 68 | 66 | 2 | 0 | 97.1% |
| vu-viec | 12/28 | 36/72 | 100 | 48 | 1 | 51 | 48.0% |
| **Tổng cộng** |  |  | **990** | **724** | **25** | **241** | **73.1%** |

## Nguyên nhân các case còn lại

| Module | Còn lại | Nguyên nhân chính |
|---|---:|---|
| bao-cao | 1 | BC04 export còn block theo dữ liệu Vụ việc `HOAN_THANH`; các lỗi còn lại chủ yếu là export Excel/body response chưa đúng định dạng file. |
| bieu-mau | 16 | Còn pending re-test một số TC đã unblock; một số case bulk import cần chuẩn bị đúng test data cùng đơn vị và template hợp lệ; một số case defer theo scope/permission. |
| chi-tra | 14 | Nhiều case phụ thuộc pool hồ sơ chi trả đúng trạng thái/nhánh nghiệp vụ; một số nhánh B9/B10/B12 còn blocked/defer theo dữ liệu và workflow downstream. |
| cross-cutting | 72 | Phụ thuộc hạ tầng ngoài: Cổng PLQG/mTLS, TLS staging, cert DN-side, endpoint outbound chưa deploy; một số edge case cần wait-time/infra hoặc seed chuyên biệt. |
| ct-htpldn | 0 | Không còn case còn lại trong scope đã tổng hợp. |
| danh-gia | 5 | Còn blocked/fail quanh state advance phân công, permission QTHT, dropdown dữ liệu raw UUID và UX toast state-gated; cần dev fix rồi re-test. |
| dao-tao | 26 | Một phần chờ HOC_VIEN entity/seed học viên, permission-matrix riêng, một số negative/state phụ của Đề kiểm tra/Lịch học cần dữ liệu đã sử dụng hoặc điểm danh để verify. |
| doanh-nghiep | 1 | Cần seed/chọn đúng doanh nghiệp có dữ liệu liên kết để verify tab lịch sử hỗ trợ/hồ sơ chi trả có số liệu thực. |
| hoi-dap | 20 | Một số TC còn chờ Cổng PLQG/TVN bridge deploy, một số chờ seed hoặc fix SLA/UX/phân công; workflow còn block ở nhánh phản hồi/DA_PHAN_CONG trong các report cũ. |
| hop-dong-tv | 2 | Còn sai spec/partial ở một số TC hợp đồng tư vấn, cần BA/dev chốt hoặc fix theo spec trước khi pass sạch. |
| kho-qa | 0 | Không còn case còn lại trong scope đã tổng hợp. |
| nguoi-ho-tro | 0 | Không còn case còn lại trong scope đã tổng hợp. |
| qtht-danh-muc | 1 | CREATE Ngày lễ còn block bởi bug FE submit silent/flow tạo ngày lễ; update/delete và các danh mục còn lại đã pass. |
| qtht-nhat-ky | 0 | Không còn case còn lại trong snapshot latest đã tổng hợp. |
| qtht-tai-khoan | 7 | Một số case defer do cần SQL backdate/token TTL, CAPTCHA/rate-limit khi test self-register, partial do mismatch spec UI/error code/profile password rule. |
| qtht-vai-tro | 3 | Partial do UI thiếu cột/trường theo SRS, errCode duplicate không khớp spec và non-QTHT vẫn thấy/mở được nút CRUD dù BE chặn. |
| to-chuc-tu-van | 0 | Không còn case còn lại trong scope đã tổng hợp. |
| tu-van-chuyen-sau | 7 | Còn external/defer: cron/Portal DN, một số TC functional chờ dữ liệu hoặc nhánh công khai/đánh giá downstream; workflow chính đã unblock. |
| tu-van-nhanh | 15 | Phụ thuộc Cổng PLQG/mTLS DN-side outbound, sandbox DN, race/batch infra; một số case defer do auto-import BR-FLOW-10 và DB-level/search outbound. |
| tu-van-vien-cg | 0 | Không còn case còn lại trong scope đã tổng hợp. |
| vu-viec | 51 | Lớn nhất do phụ thuộc VNeID Tier 2/DN portal, Cổng PLQG, DN bổ sung hồ sơ, public feature chưa implement, pool/data đúng state và một số permission/spec ambiguity cho CG/TVV/NHT. |
