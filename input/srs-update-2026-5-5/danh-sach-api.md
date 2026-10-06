# Danh sách API tích hợp & chia sẻ thông tin — Phần mềm HTPLDN

**Phạm vi:** API tích hợp với hệ thống ngoài (Outbound + Inbound). KHÔNG bao gồm API nội bộ giữa frontend ↔ backend.

**Nguồn:**
- `srs-fr-16-api.md` — đặc tả Nhóm XII
- `srs-v3.5.md` — file master
- 15 file FR còn lại trong `srs-v3.5/` (cho 6 inbound rải rác ngoài FR-16)

---

## Mục lục

- [1. Tổng quan](#1-tổng-quan)
- [2. Nhóm A — 19 API trong FR-16](#2-nhóm-a--19-api-trong-fr-16)
  - [2.1. 18 API Outbound — Chia sẻ + Tìm kiếm](#21-18-api-outbound--chia-sẻ--tìm-kiếm)
  - [2.2. 1 API Inbound — Tiếp nhận hỏi đáp từ Cổng PLQG](#22-1-api-inbound--tiếp-nhận-hỏi-đáp-từ-cổng-plqg)
- [3. Nhóm B — 11 API có FR riêng ngoài FR-16](#3-nhóm-b--11-api-có-fr-riêng-ngoài-fr-16)
- [4. Nhóm C — 2 API định nghĩa nghiệp vụ, chuẩn bị tương lai](#4-nhóm-c--2-api-định-nghĩa-nghiệp-vụ-chuẩn-bị-tương-lai)

---

## 1. Tổng quan

### Số lượng API

| Loại | Số lượng | Ghi chú |
|---|---|---|
| Outbound chia sẻ dữ liệu công khai (Cổng PLQG / HT khác gọi vào CMS để pull) | **18** | FR-XII-01..18 |
| Outbound khác (CMS gọi ra VNeID, DVC) | **4** | FR-VIII-23 (đăng nhập VNeID), FR-VIII-25 (đồng bộ VNeID), FR-V.I-12 (TB trạng thái vụ việc về DVC), FR-V.II-04 (TB DVC kết quả kiểm tra hồ sơ chi trả) |
| Inbound (CMS tiếp nhận từ HT ngoài) | **8** | 1 trong FR-16 (FR-XII-19) + 7 rải rác (FR-V.I-03, FR-V.I-05, FR-V.II-01, FR-X.1-03/05/07, FR-X.2-05) |
| **Tổng API có FR riêng (Nhóm A + B)** | **30 API** | Đã có FR/UC trong SRS hiện tại |
| API định nghĩa nghiệp vụ chuẩn bị tương lai (Nhóm C) | **2** | Đồng bộ danh mục từ LGSP BTP + Tra cứu VBPL từ HT VBPL quốc gia. Chưa có FR/UC, chờ CĐT chốt phạm vi + cung cấp tài liệu LGSP |

### Mô hình tích hợp Cổng PLQG

"Công khai/Hủy công khai" trong nghiệp vụ HTPLDN là thao tác nội bộ trên CSDL CMS — CB NV/PD set cờ `cong_khai = 1/0` + chuyển `trang_thai`. Cổng PLQG tự pull định kỳ qua 18 outbound API; bản ghi có cờ công khai sẽ tự xuất hiện/biến mất khỏi response. KHÔNG có API push/gỡ riêng từ CMS gọi RA Cổng PLQG.

### Phân loại theo bên đối tác

| Bên đối tác | API có FR riêng |
|---|---|
| Cổng PLQG | 16 outbound (UC171-186) + 5 inbound (UC149/151/153/158/189) = 21 API |
| Hệ thống khác | 2 outbound (UC187/188 — hồ sơ pháp lý DN) + 1 inbound (UC55 — hồ sơ vụ việc) = 3 API |
| HT TTHC BTP (DVC) qua LGSP | 2 inbound (UC53 — hồ sơ vụ việc; UC68 — hồ sơ chi phí TVPL) + 2 outbound (UC62 — TB trạng thái vụ việc; UC71 — TB kết quả kiểm tra hồ sơ chi trả) = 4 API |
| VNeID (qua NDXP) | 2 outbound (UC121 đăng nhập + UC123 đồng bộ tài khoản) |

---

## 2. Nhóm A — 19 API trong FR-16

> Nguồn: `srs-fr-16-api.md`. 18 outbound + 1 inbound.

### 2.1. 18 API Outbound — Chia sẻ + Tìm kiếm

> Mỗi loại nội dung có 1 cặp API: "Chia sẻ" (lấy danh sách + filter) và "Tìm kiếm" (toàn văn theo từ khóa).

| Mã FR | UC | Tên API | Mục đích nghiệp vụ | Bên gọi | Bên nhận | Thông tin nghiệp vụ trao đổi |
|---|---|---|---|---|---|---|
| **FR-XII-01** | UC171 | API Chia sẻ hỏi đáp/vướng mắc PL | Cung cấp danh sách câu hỏi & câu trả lời pháp lý đã được phê duyệt và công khai cho HT bên ngoài đọc | Cổng PLQG | CMS HTPLDN | **Đầu vào:** lĩnh vực pháp luật, khoảng ngày, đơn vị tiếp nhận, phân trang. **Đầu ra:** mã hỏi đáp, câu hỏi, câu trả lời, lĩnh vực, ngày trả lời, người trả lời |
| **FR-XII-02** | UC172 | API Tìm kiếm hỏi đáp/vướng mắc PL | Tìm hỏi đáp công khai theo từ khóa (toàn văn) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa (≥2 ký tự), lĩnh vực, phân trang. **Đầu ra:** mã hỏi đáp, câu hỏi, câu trả lời, lĩnh vực, ngày trả lời, người trả lời, **điểm liên quan** (sắp theo độ khớp giảm dần) |
| **FR-XII-03** | UC173 | API Chia sẻ đào tạo/bồi dưỡng | Cung cấp danh sách khóa đào tạo/bồi dưỡng cán bộ | Cổng PLQG | CMS HTPLDN | **Đầu vào:** hình thức (trực tuyến/trực tiếp), khoảng ngày, phân trang. **Đầu ra:** mã khóa học, tên, hình thức, ngày bắt đầu/kết thúc, số học viên, trạng thái |
| **FR-XII-04** | UC174 | API Tìm kiếm đào tạo/bồi dưỡng | Tìm khóa đào tạo theo từ khóa | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, phân trang. **Đầu ra:** mã khóa học, tên khóa học, hình thức (trực tuyến/trực tiếp), ngày bắt đầu, ngày kết thúc, số học viên, trạng thái, **điểm liên quan** (sắp theo độ khớp giảm dần) |
| **FR-XII-05** | UC175 | API Chia sẻ chuyên gia, tư vấn viên (CG/TVV) | Cung cấp danh mục chuyên gia, tư vấn viên đang hoạt động (loại trừ thông tin nhạy cảm cá nhân) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** lĩnh vực chuyên môn, địa bàn (tỉnh/TP), loại (TVV/CG), phân trang. **Đầu ra:** họ tên, loại, lĩnh vực, địa bàn, tổ chức hành nghề, trạng thái. **KHÔNG trả:** CMND/CCCD, SĐT, địa chỉ cá nhân |
| **FR-XII-06** | UC176 | API Tìm kiếm chuyên gia, tư vấn viên | Tìm CG/TVV theo từ khóa (tên hoặc tổ chức) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, lĩnh vực, địa bàn, phân trang. **Đầu ra:** họ tên, loại (TVV/CG), lĩnh vực chuyên môn, địa bàn, tổ chức hành nghề, trạng thái HOAT_DONG. **KHÔNG trả:** CMND/CCCD, SĐT, địa chỉ cá nhân |
| **FR-XII-07** | UC177 | API Chia sẻ vụ việc HTPL | Cung cấp danh sách vụ việc đã hoàn thành/duyệt (loại trừ thông tin DN nhạy cảm) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** lĩnh vực, trạng thái (HOAN_THANH/DA_DUYET), khoảng ngày, phân trang. **Đầu ra:** mã vụ việc, lĩnh vực, trạng thái, đơn vị xử lý, ngày tiếp nhận, ngày hoàn thành. **KHÔNG trả:** MST DN, địa chỉ DN chi tiết, tên DN |
| **FR-XII-08** | UC178 | API Tìm kiếm vụ việc HTPL | Tìm vụ việc theo từ khóa | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, lĩnh vực, trạng thái, phân trang. **Đầu ra:** mã vụ việc, lĩnh vực, trạng thái (HOAN_THANH/DA_DUYET), đơn vị xử lý, ngày tiếp nhận, ngày hoàn thành. **KHÔNG trả:** MST DN, địa chỉ DN chi tiết, tên DN |
| **FR-XII-09** | UC179 | API Chia sẻ kết quả đánh giá hiệu quả HTPL | Cung cấp kết quả đánh giá đã duyệt báo cáo | Cổng PLQG | CMS HTPLDN | **Đầu vào:** kỳ (sơ bộ 6 tháng / sơ bộ năm / tròn năm), đơn vị, phân trang. **Đầu ra:** tên đợt, kỳ, điểm trung bình, số vụ việc đánh giá, đơn vị, trạng thái HOAN_THANH, mã mẫu BC (MAU_21A/MAU_21B), thời gian duyệt BC |
| **FR-XII-10** | UC180 | API Tìm kiếm đánh giá hiệu quả | Tìm đợt đánh giá theo từ khóa (tên đợt, đơn vị) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, kỳ, đơn vị, phân trang. **Đầu ra:** tên đợt, kỳ (sơ bộ 6 tháng / sơ bộ năm / tròn năm), điểm trung bình, số vụ việc đánh giá, đơn vị, trạng thái HOAN_THANH, mã mẫu báo cáo (MAU_21A/MAU_21B), thời gian duyệt báo cáo |
| **FR-XII-11** | UC181 | API Chia sẻ thư viện biểu mẫu, hợp đồng | Cung cấp danh sách biểu mẫu đã duyệt + công khai kèm đường dẫn tải về | Cổng PLQG | CMS HTPLDN | **Đầu vào:** danh mục, định dạng (docx/pdf/xlsx), phân trang. **Đầu ra:** tên biểu mẫu, danh mục, định dạng, kích thước, URL tải về, thời gian đăng tải |
| **FR-XII-12** | UC182 | API Tìm kiếm biểu mẫu, hợp đồng | Tìm biểu mẫu theo từ khóa | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, danh mục, phân trang. **Đầu ra:** tên biểu mẫu, danh mục, định dạng (docx/pdf/xlsx), kích thước file, đường dẫn tải về, thời gian đăng tải |
| **FR-XII-13** | UC183 | API Chia sẻ tư vấn chuyên sâu (TVCS) | Cung cấp danh sách tư vấn chuyên sâu đã hoàn thành — chỉ siêu dữ liệu, KHÔNG nội dung văn bản tư vấn chi tiết | Cổng PLQG | CMS HTPLDN | **Đầu vào:** lĩnh vực, khoảng ngày, đơn vị tiếp nhận, phân trang. **Đầu ra:** mã yêu cầu, lĩnh vực, trạng thái, chuyên gia, ngày hoàn thành |
| **FR-XII-14** | UC184 | API Tìm kiếm tư vấn chuyên sâu | Tìm TVCS theo từ khóa (lĩnh vực, chuyên gia) | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, lĩnh vực, đơn vị, phân trang. **Đầu ra:** mã yêu cầu, lĩnh vực, trạng thái HOAN_THANH, chuyên gia, ngày hoàn thành. **CHỈ siêu dữ liệu** — KHÔNG nội dung văn bản tư vấn chi tiết |
| **FR-XII-15** | UC185 | API Chia sẻ chương trình HTPLDN | Cung cấp danh sách chương trình HTPLDN đã công bố — chỉ kế hoạch, KHÔNG kết quả thực hiện | Cổng PLQG | CMS HTPLDN | **Đầu vào:** đơn vị, năm, phân trang. **Đầu ra:** mã CT, tên CT, mục tiêu, thời gian bắt đầu/kết thúc, đơn vị, trạng thái |
| **FR-XII-16** | UC186 | API Tìm kiếm chương trình HTPLDN | Tìm CT theo từ khóa | Cổng PLQG | CMS HTPLDN | **Đầu vào:** từ khóa, đơn vị, năm, phân trang. **Đầu ra:** mã chương trình, tên chương trình, mục tiêu, thời gian bắt đầu, thời gian kết thúc, đơn vị, trạng thái DA_CONG_BO. **CHỈ kế hoạch** — KHÔNG kết quả thực hiện |
| **FR-XII-17** | UC187 | API Chia sẻ hồ sơ pháp lý của DN (HSPL) | Cung cấp danh sách hồ sơ pháp lý của DN cho HT khác đồng bộ — chỉ siêu dữ liệu hồ sơ, mặc định lọc đang hiệu lực | Hệ thống khác | CMS HTPLDN | **Đầu vào:** đơn vị sở hữu, ID doanh nghiệp, loại hồ sơ (giấy phép/hợp đồng/giấy CN/quyết định/khác), lĩnh vực, ngày cấp từ-đến, phân trang. **Đầu ra:** mã hồ sơ, tên, loại, doanh_nghiep_id, ngày cấp, ngày hết hạn, cơ quan cấp, trạng thái. **KHÔNG trả:** mô tả dài, file đính kèm, thông tin DN gốc |
| **FR-XII-18** | UC188 | API Tìm kiếm hồ sơ pháp lý của DN | Tìm HSPL theo từ khóa (tên hồ sơ + cơ quan cấp) | Hệ thống khác | CMS HTPLDN | **Đầu vào:** từ khóa, loại hồ sơ, lĩnh vực, ID doanh nghiệp, phân trang. **Đầu ra:** mã hồ sơ, tên hồ sơ, loại hồ sơ (giấy phép/hợp đồng/giấy CN/quyết định/khác), ID doanh nghiệp (consumer tự nối), ngày cấp, ngày hết hạn, cơ quan cấp, trạng thái HIEU_LUC. **KHÔNG trả:** mô tả dài, file đính kèm, thông tin DN gốc |

**Quy tắc nghiệp vụ chung cho 18 outbound:**
- Chỉ trả bản ghi đã được phê duyệt + công khai (`trang_thai = CONG_KHAI` AND `cong_khai = true` AND `is_deleted = false`) — theo BR-INTG-07.
- Loại bỏ thông tin nhạy cảm trước khi trả (CCCD, CMND, mật khẩu, số TK, SĐT cá nhân, địa chỉ cá nhân, OTP) — theo BR-SEC-01.
- Mỗi consumer giới hạn 100 yêu cầu/phút (BR-INTG-03 / BR-API-01); vượt sẽ bị từ chối tạm thời.
- Mọi yêu cầu được ghi nhật ký (consumer_id, endpoint, thời điểm, mã phản hồi) — BR-DATA-05.

### 2.2. 1 API Inbound — Tiếp nhận hỏi đáp từ Cổng PLQG

| Mã FR | UC | Tên API | Mục đích nghiệp vụ | Bên gọi | Bên nhận | Thông tin nghiệp vụ trao đổi |
|---|---|---|---|---|---|---|
| **FR-XII-19** | UC189 | API Tiếp nhận hỏi đáp/vướng mắc PL từ Cổng PLQG | Tiếp nhận câu hỏi pháp lý do DN gửi qua Cổng PLQG, lưu vào CSDL hỏi đáp với kênh = "Cổng PLQG" để CB nghiệp vụ tiếp nhận xử lý theo luồng FR-II-01. Hỗ trợ chống trùng (idempotency) khi Cổng gửi lại | Cổng PLQG (gửi sang) | CMS HTPLDN | **Đầu vào:** ID gốc trên Cổng (chống trùng), nội dung câu hỏi (≤5000 ký tự), lĩnh vực pháp luật, người gửi (tên/email/SĐT — tùy chọn), DN (nếu có TK), đơn vị tiếp nhận do DN chọn (mặc định Sở Tư pháp tỉnh DN), độ phức tạp (thường/phức tạp), siêu dữ liệu file đính kèm (≤10 file). **Đầu ra:** ID nội bộ, mã hỏi đáp, ID gốc (echo), thời điểm tiếp nhận, đường dẫn upload file (tạm 1 giờ), trạng thái ("đã tiếp nhận" / "đã tiếp nhận trước đó nếu retry") |

**Quy tắc nghiệp vụ then chốt:**
- Cùng 1 ID gốc gửi lại → KHÔNG tạo bản ghi mới, trả về ID nội bộ đã có.
- Cùng 1 ID gốc gửi lại với nội dung KHÁC → từ chối (xung đột dữ liệu, cần Cổng đối soát).
- Tự động tính hạn xử lý SLA theo độ phức tạp (BR-CALC-03).
- Tự động thông báo CB nghiệp vụ của đơn vị tiếp nhận khi có hỏi đáp mới.

---

## 3. Nhóm B — 11 API có FR riêng ngoài FR-16

> Các API này có FR riêng + UC riêng nhưng KHÔNG nằm trong FR-16. Gồm 7 inbound (Cổng PLQG / DVC / HT khác đẩy data về CMS) + 4 outbound (CMS gọi ra VNeID / DVC).

| Mã FR | UC | Tên API | Hướng | Bên gọi | Bên nhận | Mục đích nghiệp vụ | Thông tin nghiệp vụ trao đổi | File SRS |
|---|---|---|---|---|---|---|---|---|
| **FR-V.I-03** | UC53 | Tiếp nhận hồ sơ vụ việc qua DVC | Inbound | HT TTHC Bộ Tư pháp (qua LGSP) | CMS HTPLDN | Tiếp nhận hồ sơ yêu cầu HTPL do DN nộp trên Dịch vụ công, đẩy về CMS qua LGSP. Tự động tạo bản ghi vụ việc, idempotent theo mã hồ sơ DVC | **Đầu vào:** mã hồ sơ DVC (chống trùng), tên DN, MST, địa chỉ, người đại diện, nội dung yêu cầu, lĩnh vực, file đính kèm. **Đầu ra:** success (boolean), mã vụ việc PM, trạng thái Chờ tiếp nhận; nếu lỗi: error_code + error_message | `srs-fr-05-vu-viec.md` |
| **FR-V.I-05** | UC55 | Tiếp nhận hồ sơ vụ việc HTPL từ hệ thống khác | Inbound | Hệ thống bên ngoài (REST trực tiếp, không qua LGSP) | CMS HTPLDN | Tiếp nhận hồ sơ yêu cầu HTPL do HT bên ngoài (đã đăng ký với PM) đẩy sang để CB NV xử lý | **Đầu vào:** mã HT nguồn, mã hồ sơ trên HT nguồn (chống trùng), thông tin DN (tên/MST/địa chỉ/người đại diện/SĐT/email), nội dung yêu cầu, lĩnh vực, file đính kèm. **Đầu ra:** mã hồ sơ vụ việc PM, trạng thái tiếp nhận | `srs-fr-05-vu-viec.md` |
| **FR-V.I-12** | UC62 | Thông báo trạng thái vụ việc về DVC qua LGSP | Outbound | CMS HTPLDN | HT TTHC BTP qua LGSP | Khi CB NV hoàn tất kiểm tra hồ sơ vụ việc (đã phân công hoặc từ chối), nếu hồ sơ gốc đến từ kênh DVC thì tự động đồng bộ trạng thái về HT TTHC BTP qua LGSP để DN theo dõi trên cổng DVC | **Đầu vào (CMS gửi):** mã hồ sơ DVC gốc, mã vụ việc PM, trạng thái mới (đã phân công / từ chối), ghi chú/lý do (nếu từ chối). **Đầu ra:** trạng thái nhận của DVC. Chỉ trigger khi `kenh_tiep_nhan = DVC`. Retry 3 lần (BR-RETRY-01) nếu lỗi | `srs-fr-05-vu-viec.md` |
| **FR-V.II-01** | UC68 | Tiếp nhận hồ sơ chi phí TVPL từ DVC qua LGSP | Inbound | HT TTHC Bộ Tư pháp (qua LGSP) | CMS HTPLDN | Tiếp nhận hồ sơ đề nghị hỗ trợ chi phí TVPL do DN nộp trên DVC, vào CSDL chi trả CMS | **Đầu vào:** mã hồ sơ DVC (chống trùng), JSON hồ sơ 18 trường theo Mẫu 01 NĐ55, file đính kèm (Giấy CNĐKKD, HĐ TVPL, VB TVPL), ngày nộp. **Đầu ra:** mã hồ sơ chi trả PM, trạng thái Chờ tiếp nhận | `srs-fr-06-chi-tra.md` |
| **FR-V.II-04** | UC71 | Thông báo kết quả kiểm tra hồ sơ chi trả qua DVC | Outbound | CMS HTPLDN | HT TTHC BTP qua LGSP | Tự động gửi kết quả kiểm tra hồ sơ chi phí TVPL về HT TTHC BTP qua LGSP, sau khi CB NV hoàn tất kiểm tra | **Đầu vào (CMS gửi):** mã hồ sơ DVC, kết quả kiểm tra (Đạt/Không đạt/Cần bổ sung), ghi chú, danh sách trường thiếu. **Đầu ra:** trạng thái nhận của DVC. Retry 3 lần nếu lỗi, sau đó cảnh báo CB NV | `srs-fr-06-chi-tra.md` |
| **FR-VIII-23** | UC121 | Đăng nhập bằng VNeID (OIDC) | Outbound | CMS HTPLDN | VNeID (qua NDXP) | Cho phép DN, TVV, CG, NHT đăng nhập CMS qua VNeID OIDC Authorization Code (DN dùng VNeID Tổ chức; TVV/CG/NHT dùng VNeID Cá nhân). Áp dụng khi Tier 2 đã triển khai | **Đầu vào (CMS gửi):** chuyển hướng user đến VNeID authorization endpoint với scope=openid. **Đầu ra (VNeID trả qua callback):** authorization code; CMS exchange lấy ID token + thông tin user (CCCD, họ tên, MST với DN). Liên kết với tài khoản nội bộ | `srs-fr-10-quan-tri.md` |
| **FR-VIII-25** | UC123 | Đồng bộ tài khoản với VNeID | Outbound | CMS HTPLDN | VNeID (qua NDXP) | User (DN/NHT/TVV/CG) đã có tài khoản nội bộ thực hiện liên kết với danh tính VNeID. Sau liên kết, user có thêm cách đăng nhập VNeID. Có scheduled job hàng ngày tự đồng bộ thông tin từ VNeID cho các tài khoản đã liên kết; thu hồi VNeID → tạm khóa TK | **Đầu vào (CMS gửi):** redirect VNeID xác thực + sau đó gọi VNeID UserInfo để lấy thông tin định danh. **Đầu ra:** thông tin định danh từ VNeID; CMS đối chiếu (DN: MST khớp; TVV/CG/NHT: CCCD khớp); nếu khớp → liên kết, nếu không → từ chối với lý do | `srs-fr-10-quan-tri.md` |
| **FR-X.1-03** | UC149 | Tiếp nhận nội dung tư vấn chuyên sâu từ Cổng PLQG | Inbound | Cổng PLQG (REST trực tiếp) | CMS HTPLDN | Tiếp nhận hồ sơ TVCS do DN gửi qua chuyên trang Cổng PLQG, tạo bản ghi TVCS, thông báo CB NV | **Đầu vào:** thông tin DN, lĩnh vực PL, nội dung yêu cầu TVCS, đơn vị tiếp nhận (DN chọn). **Đầu ra:** mã TVCS, trạng thái Tiếp nhận | `srs-fr-12-tv-chuyen-sau.md` |
| **FR-X.1-05** | UC151 | Tiếp nhận hồ sơ pháp lý DN từ Cổng PLQG | Inbound | Cổng PLQG (REST trực tiếp) | CMS HTPLDN | Tiếp nhận hồ sơ pháp lý DN (giấy phép/hợp đồng/giấy CN/quyết định) do DN upload qua Cổng PLQG | **Đầu vào:** ID DN, tên hồ sơ, loại hồ sơ, lĩnh vực, ngày cấp/hết hạn, cơ quan cấp, file. **Đầu ra:** mã hồ sơ HSPL, trạng thái Hiệu lực | `srs-fr-12-tv-chuyen-sau.md` |
| **FR-X.1-07** | UC153 | Tiếp nhận đánh giá chất lượng TVCS từ Cổng PLQG | Inbound | Cổng PLQG (REST trực tiếp) | CMS HTPLDN | Tiếp nhận đánh giá DN dành cho phiên TVCS, cập nhật điểm trung bình chuyên gia. Hỗ trợ gửi lại (idempotency) | **Đầu vào:** ID TVCS gốc, ID DN, điểm (1-5), nhận xét. **Đầu ra:** ID đánh giá, điểm trung bình mới của chuyên gia | `srs-fr-12-tv-chuyen-sau.md` |
| **FR-X.2-05** | UC158 | Tiếp nhận đánh giá chất lượng tư vấn nhanh từ Cổng PLQG | Inbound | Cổng PLQG (REST trực tiếp, có khoá idempotency) | CMS HTPLDN | Tiếp nhận đánh giá DN dành cho phiên tư vấn nhanh (Q&A từ kho), cải thiện kho và phục vụ báo cáo. Idempotency 24 giờ | **Đầu vào:** ID phiên TV nhanh, ID DN, điểm (1-5), nhận xét. **Đầu ra:** ID đánh giá, điểm trung bình mới. **Quy tắc:** trùng khoá idempotency trong 24h → trả kết quả lần đầu, KHÔNG tạo bản ghi mới | `srs-fr-13-tv-nhanh.md` |

---

## 4. Nhóm C — 2 API định nghĩa nghiệp vụ, chuẩn bị tương lai

> 2 API dưới đây đã định nghĩa **mục đích nghiệp vụ + thông tin trao đổi** để chuẩn bị cho khả năng tích hợp tương lai khi LGSP BTP sẵn sàng. **Hiện trạng:** CSV v1.1 chưa có UC tương ứng + chưa có FR riêng trong SRS + CĐT chưa cung cấp tài liệu kỹ thuật LGSP. Khi triển khai cần: (1) CĐT chốt đưa vào phạm vi + cung cấp tài liệu LGSP; (2) BA tạo FR riêng + UC tương ứng (đề xuất nhóm VIII Quản trị); (3) Architecture Design bổ sung schema/protocol/auth.

| Tên API | Hướng | Bên gọi | Bên nhận | Thông tin nghiệp vụ trao đổi | Quy tắc nghiệp vụ then chốt |
|---|---|---|---|---|---|
| **Đồng bộ danh mục chuẩn từ HT Danh mục dùng chung BTP** | Outbound (CMS → LGSP) | CMS HTPLDN (scheduled job hoặc QTHT trigger thủ công) | HT Danh mục dùng chung BTP qua LGSP | **Đầu vào (CMS gửi):** loại danh mục cần đồng bộ (ví dụ: lĩnh vực pháp luật / tỉnh-thành / loại văn bản pháp luật / loại doanh nghiệp / loại hình hỗ trợ — danh sách loại danh mục mà BTP có chuẩn quốc gia, tương ứng các loại PM hiện quản lý nội bộ ở UC99-110 + các UC danh mục mới); thời điểm đồng bộ gần nhất (để delta sync — chỉ lấy entries thay đổi). **Đầu ra (BTP trả):** danh sách entries với mã chuẩn quốc gia, tên, mã cha (nếu có cấu trúc cây), trạng thái (hoạt động/không hoạt động), ngày cập nhật gần nhất. | **(1)** PM giữ ánh xạ giữa mã danh mục nội bộ và mã chuẩn BTP. **(2)** Entries mới từ BTP → PM tự thêm vào danh mục nội bộ với trạng thái hoạt động. **(3)** Entries đã đồng bộ trước đây mà BTP đổi tên → PM cập nhật tên. **(4)** Entries BTP đánh dấu không hoạt động → PM cũng đánh dấu không hoạt động (KHÔNG xóa, để giữ nguyên các bản ghi tham chiếu cũ). **(5)** Dự phòng: nếu HT BTP không khả dụng → PM dùng danh mục nội bộ đã đồng bộ lần cuối, vẫn vận hành bình thường (theo INT-05). |
| **Tra cứu văn bản pháp luật (VBPL) từ HT VBPL quốc gia** | Outbound (CMS → LGSP) | CMS HTPLDN (trigger khi CB NV mở widget tra cứu VBPL trong giao diện soạn câu trả lời hỏi đáp / vụ việc / tư vấn chuyên sâu) | HT VBPL quốc gia / CSDL VBPL BTP qua LGSP | **Đầu vào (CMS gửi):** từ khóa, loại văn bản (luật/nghị định/thông tư/quyết định/...), số hiệu, năm ban hành, cơ quan ban hành, trạng thái hiệu lực mong muốn lọc. **Đầu ra (HT VBPL trả):** danh sách văn bản matching với: số hiệu đầy đủ, tên VB, ngày ban hành, ngày hiệu lực, cơ quan ban hành, trạng thái (đang hiệu lực / hết hiệu lực / sửa đổi bổ sung / thay thế), đường dẫn tới VB chi tiết trên Cổng PLQG (để CB NV mở xem nguyên văn). | **(1)** Real-time on-demand — không cache lâu dài (vì hiệu lực VB có thể thay đổi bất cứ lúc nào do văn bản mới ban hành). **(2)** Khi CB NV chọn 1 VB từ kết quả tra cứu để cite vào câu trả lời → PM lưu lại số hiệu + tên + đường dẫn vào câu trả lời (snapshot tại thời điểm cite, không live link). **(3)** Dự phòng: nếu HT VBPL không khả dụng → hiển thị thông báo lỗi nhẹ trong widget, CB NV vẫn nhập số hiệu + tên VBPL bằng tay được, không chặn quy trình soạn câu trả lời. |
