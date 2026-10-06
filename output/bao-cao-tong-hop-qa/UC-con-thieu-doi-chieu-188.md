# Đối chiếu UC: File report vs Danh sách gốc 188 UC

**Ngày kiểm tra:** 2026-06-30
**Nguồn gốc (chuẩn):** `input/Input/Danh sách transaction_v1.1_2026-03-27.csv` — 188 UC (STT 1–188)
**File report kiểm tra:** `report-dot-1.xlsx` / `report-dot-2.xlsx` / `report-dot-3.xlsx` (cả 3 đợt giống nhau về UC)

---

## 1. Kết luận nhanh

| Chỉ số | Số lượng |
|---|---|
| Tổng UC theo danh sách gốc | **188** (170 chức năng + 18 API) |
| UC report đã có (nhãn trong cột UC) | **162** |
| → Quy về số UC gốc thực sự cover | **160** (162 = 160 + 2 biến thể UC159E, UC163E trùng số 159/163) |
| **UC còn THIẾU so với 188** | **28** |
| – Thiếu nhóm **chức năng** | **11** |
| – Thiếu nhóm **API kết nối chia sẻ dữ liệu** | **17** |

> **Vì sao ra con số 162:** Report gắn nhãn 162 UC, nhưng có 2 nhãn là biến thể (UC159E, UC163E) trùng số với UC159/UC163 → tính theo số UC gốc chỉ cover được **160** UC. Trong 160 đó có **1 UC API (UC183)** đã được test trong sheet "15. Tư vấn chuyên sâu".
>
> ⇒ Tính riêng chức năng: gốc 170 → report cover 159 → **thiếu 11 UC chức năng.**
> ⇒ Tính cả API: gốc 188 → report cover 161 (160 số + UC183 thuộc API) → **thiếu 27**... *(xem mục 4 để hiểu cách đếm 28 vs 27)*

---

## 2. UC chức năng còn thiếu (11 UC) — cần bổ sung test case

| Module (sheet report) | UC thiếu | Tên chức năng |
|---|:--|---|
| **09. Chi trả chi phí** | UC78 | Trình phê duyệt hồ sơ đề nghị thanh toán |
| **12. Biểu mẫu** | UC97 | Công khai biểu mẫu, hợp đồng lên cổng thông tin |
| **13. Quản trị hệ thống** | UC100 | Quản lý danh mục loại hình hỗ trợ |
| **13. Quản trị hệ thống** | UC116 | Quản lý loại hình tiếp nhận hồ sơ |
| **13. Quản trị hệ thống** | UC117 | Quản lý danh mục kênh tiếp nhận hồ sơ |
| **13. Quản trị hệ thống** | UC118 | Quản lý đăng nhập |
| **13. Quản trị hệ thống** | UC119 | Quản lý đăng xuất |
| **13. Quản trị hệ thống** | UC121 | Quản lý đăng nhập bằng VNeID |
| **13. Quản trị hệ thống** | UC122 | Quản lý đăng xuất bằng VNeID |
| **13. Quản trị hệ thống** | UC123 | Quản lý đồng bộ tài khoản VNeID |
| **18. Chương trình HTPLDN** | UC167 | Trình phê duyệt báo cáo kết quả thực hiện chương trình |

**Tập trung nhiều nhất ở Module 13 — Quản trị hệ thống (8/11 UC):** chủ yếu là nhóm Đăng nhập/Đăng xuất, đăng nhập–đồng bộ VNeID, và 3 danh mục quản trị (loại hình hỗ trợ, loại hình/kênh tiếp nhận hồ sơ).

---

## 3. UC API còn thiếu (17 UC) — nhóm "API kết nối chia sẻ dữ liệu"

Đây chính là phần đối tác nói "tính cả phần API". Nhóm này (Section XII, UC171–188) gồm 18 UC, report mới test 1 (UC183), còn thiếu 17:

| UC thiếu | Tên |
|:--|---|
| UC171 | API chia sẻ thông tin hỏi đáp, vướng mắc pháp lý |
| UC172 | API tìm kiếm thông tin hỏi đáp, vướng mắc pháp lý |
| UC173 | API chia sẻ thông tin đào tạo, bồi dưỡng cán bộ |
| UC174 | API tìm kiếm thông tin đào tạo, bồi dưỡng cán bộ |
| UC175 | API chia sẻ thông tin chuyên gia, tư vấn viên pháp lý |
| UC176 | API tìm kiếm thông tin chuyên gia, tư vấn viên pháp lý |
| UC177 | API chia sẻ vụ việc hỗ trợ pháp lý cho doanh nghiệp |
| UC178 | API tìm kiếm vụ việc hỗ trợ pháp lý cho doanh nghiệp |
| UC179 | API chia sẻ kiểm tra, đánh giá hiệu quả hỗ trợ pháp lý |
| UC180 | API tìm kiếm kiểm tra, đánh giá hiệu quả hỗ trợ pháp lý |
| UC181 | API chia sẻ thư viện biểu mẫu, hợp đồng |
| UC182 | API tìm kiếm thư viện biểu mẫu, hợp đồng |
| UC184 | API tìm kiếm tư vấn chuyên sâu với chuyên gia |
| UC185 | API chia sẻ kế hoạch thực hiện chương trình HTPLDN |
| UC186 | API tìm kiếm kế hoạch thực hiện chương trình HTPLDN |
| UC187 | API chia sẻ hồ sơ pháp lý doanh nghiệp |
| UC188 | API tìm kiếm hồ sơ pháp lý doanh nghiệp |

*(UC183 "API chia sẻ tư vấn chuyên sâu" đã có test trong sheet 15.)*

---

## 4. Giải thích chênh lệch con số (cho khớp cách đối tác đếm)

- Đối tác nói: **188** (cả API) / **170** (chỉ chức năng) / report **162**.
- Thực tế đếm theo số UC gốc: report cover **160** số UC + 2 biến thể E (159E, 163E).
- **Thiếu 11 UC chức năng** + **17 UC API** = **28 UC** chưa có test case trong report.
- 11 UC chức năng này đã kiểm tra kỹ: **không xuất hiện ở bất kỳ ô nào** trong cả 3 file report (không phải chỉ quên gắn nhãn cột UC).

---

## 5b. Trừ phần API — còn thiếu bao nhiêu & đã pass chưa (trạng thái đợt 3 — mới nhất)

**Trừ 18 UC API → chỉ xét 170 UC chức năng:**

| Nhóm | Số lượng |
|---|:-:|
| UC chức năng (gốc) | 170 |
| – Đã có test case | 159 |
| – **Còn THIẾU (chưa có TC)** | **11** |

> ⚠️ 11 UC còn thiếu này **chưa có test case nào → chưa kiểm thử → không có kết quả Pass/Fail.** Muốn biết pass hay không thì phải **viết bổ sung test case** trước.

**Trong 159 UC chức năng đã có test case — trạng thái đợt 3:**

| Trạng thái | Số UC |
|---|:-:|
| ✅ Pass hết (mọi TC PASS) | **101** |
| ❌ Còn TC FAIL (đang lỗi) | **11** |
| ⏳ Còn TC "Chưa chạy" (chưa fail) | **47** |

*(Đợt 1 → đợt 3: số TC FAIL giảm 130 → 55 → 14, cho thấy đang được fix dần.)*

### 11 UC chức năng CÒN LỖI (có TC FAIL) — đợt 3

| Module | UC | TC fail / tổng | Tên |
|---|:--|:-:|---|
| 03. Hỏi đáp pháp lý | UC10 | 3/63 | Quản lý thông tin hỏi đáp, vướng mắc |
| 03. Hỏi đáp pháp lý | UC18 | 1/8 | Quản lý câu hỏi, vướng mắc đã xử lý |
| 04. Đào tạo tập huấn | UC24 | 1/71 | Quản lý kiểm tra, đánh giá kết quả học tập |
| 04. Đào tạo tập huấn | UC26 | 1/39 | Quản lý kho tài liệu, bài giảng |
| 08. Vụ việc HTPL | UC51 | 2/73 | Quản lý hồ sơ yêu cầu hỗ trợ pháp lý |
| 10. Quản lý doanh nghiệp | UC81 | 1/161 | Quản lý doanh nghiệp được hỗ trợ pháp lý |
| 13. Quản trị hệ thống | UC99 | 1/221 | Quản lý danh mục lĩnh vực pháp lý |
| 13. Quản trị hệ thống | UC105 | 1/6 | Quản lý danh mục loại doanh nghiệp |
| 10. QLDN / 13. QTHT | UC120 | 1/65 | Quản lý đăng ký tài khoản |
| 14. Báo cáo thống kê | UC124 | 1/107 | Báo cáo thống kê số lượng hỏi đáp, vướng mắc |
| 10. QLDN / 15. TVCS | UC150 | 1/69 | Quản lý hồ sơ pháp lý doanh nghiệp |

### 47 UC chức năng còn TC "Chưa chạy" (chưa fail nhưng chưa test hết)

UC1, UC2, UC5, UC11, UC12, UC16, UC17, UC20, UC23, UC32, UC35, UC37, UC38, UC39, UC42, UC43, UC46, UC47, UC50, UC52, UC54, UC55, UC57, UC62, UC64, UC66, UC67, UC68, UC83, UC92, UC94, UC95, UC108, UC112, UC113, UC125, UC147, UC148, UC149, UC151, UC152, UC153, UC154, UC156, UC157, UC159, UC164.

*(Tổng cộng 228 test case ở trạng thái "Chưa chạy" trải trên 47 UC này.)*

---

## 5. Đề xuất

1. **Bổ sung 11 test case** cho 11 UC chức năng (mục 2) — ưu tiên Module 13 Quản trị hệ thống (8 UC).
2. **Thống nhất với đối tác về phạm vi API (17 UC):** các UC171–188 là API kết nối/chia sẻ dữ liệu — cần xác nhận có nằm trong phạm vi test đợt này không (thường cần môi trường tích hợp/mTLS riêng). Nếu trong phạm vi thì lên kế hoạch test API riêng.
3. **Làm rõ 2 biến thể UC159E / UC163E:** đây là 2 nhãn QA tự thêm, không có trong danh sách gốc 188 — nên ghi chú lại để tránh đếm lệch.
