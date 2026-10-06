# Bảng đối chiếu điều kiện — KTDGKQHT_20 (vòng soát lại 2, 2026-08-04)

> Bug TÍNH TOÁN (không phải hiển thị) → bắt buộc điền bảng. Cột giữa = điều kiện của **BUG GỐC**
> (do tổ kiểm thử đo ngày 03/08/2026), cột phải = điều kiện **thực tế test lại** ngày 04/08/2026.
>
> ⚠️ Tỷ lệ chuyên cần là **trường lưu trong CSDL**, tính lại tại thời điểm lưu điểm danh chứ không tính lại
> lúc hiển thị. Vì vậy phép thử quyết định là **dựng dữ liệu điểm danh MỚI hoàn toàn qua giao diện**, không
> dùng lại bản ghi cũ. Môi trường lần này (`htpldn-uat.ospgroup.vn`) **không có** khóa `KH-QAW7-HOINGHI` của
> lần đo trước, nên buộc phải dựng lại tiền đề từ đầu — đúng tinh thần "thiếu tiền đề thì tự tạo".

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ Trung ương (`cbnv_tw`, `CB_NV_TW`, Cục Bổ trợ tư pháp) | Chính vai trò + đơn vị đó — `cbnv_tw` (`CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`, hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp") | Không |
| Entity + trạng thái | Khóa học ở trạng thái **Đang diễn ra**, có học viên đã duyệt | Khóa `KH-20260509-006` "Luật đất đai cập nhật 2024 - R9" — bước 4 **Đang diễn ra**, 6 học viên trong danh sách kết quả | Không |
| Dữ liệu tiền đề — hình dạng quyết định kết quả (N buổi, mới điểm danh M buổi, M < N) | Lịch học **3 buổi**, mới điểm danh **1/3 buổi** | **Đúng hình dạng đó, dựng mới 100% qua giao diện**: khóa có sẵn 1 buổi, tự thêm 2 buổi (16/02 và 17/02) thành **3 buổi**; chỉ điểm danh **1 buổi** (15/02) | Không |
| Dữ liệu tiền đề — bản ghi chuyên cần phải MỚI (sinh sau bản vá) | Bản ghi sinh trước bản vá | Đã chụp tab "Kết quả" **TRƯỚC** khi điểm danh: cột "Chuyên cần" của cả 6 học viên đều `—` ⇒ giá trị đo sau đó là giá trị mới sinh trong phiên này (ảnh `KTDGKQHT_20-v2-01-...`) | Không |
| Input — trạng thái điểm danh của từng học viên | HV1 "Vắng có phép", HV2 "Có mặt" | Phủ đủ **cả 3 trạng thái** để kiểm luôn tử số: HV1+HV5 = "Vắng có phép", HV2+HV4 = "Có mặt", HV3+HV6 = "Vắng không phép" | Không |
| Thao tác đo | Đọc ô "Chuyên cần" trên tab Kết quả + mở tệp DOCX xuất ra đọc cột "Tổng số buổi" / "Tỉ lệ chuyên cần (%)" | Đúng như vậy: (1) đọc ô "Chuyên cần" trên tab Kết quả; (2) bấm "Xuất DOCX" rồi **mở đọc nội dung tệp**; (3) đối chiếu dữ liệu máy chủ trả cho màn hình | Không |

**Kết luận: 0 GAP.**

---

## Kết quả đo — 3 phương pháp độc lập, khớp nhau (bản dựng V1.0.5, gói giao diện `index-DpIXRGaI.js`)

Tiền đề: khóa có **3 buổi** trong Lịch học, mới điểm danh **1 buổi** (15/02/2026).
Mỗi dòng ghi: học viên → trạng thái điểm danh buổi 1 → ô "Chuyên cần" tab Kết quả → tệp DOCX
(số buổi có mặt / tổng số buổi / tỉ lệ %) → kỳ vọng theo BR-KQ-02.

- tester 1 → Vắng có phép → `0/3 (33.33%)` → DOCX 0 / 3 / 33.33 → kỳ vọng (0+1)/3 = 33.33% ✔
- tester 2 → Có mặt → `1/3 (33.33%)` → DOCX 1 / 3 / 33.33 → kỳ vọng (1+0)/3 = 33.33% ✔
- tester 3 → Vắng không phép → `0/3 (0.00%)` → DOCX 0 / 3 / 0.00 → kỳ vọng 0% ✔
- tester 4 → Có mặt → `1/3 (33.33%)` → DOCX 1 / 3 / 33.33 → kỳ vọng 33.33% ✔
- tester 5 → Vắng có phép → `0/3 (33.33%)` → DOCX 0 / 3 / 33.33 → kỳ vọng 33.33% ✔
- tester 6 → Vắng không phép → `0/3 (0.00%)` → DOCX 0 / 3 / 0.00 → kỳ vọng 0% ✔

⇒ **Mẫu số nay là TỔNG SỐ BUỔI CỦA KHÓA (3), không còn là số buổi đã điểm danh (1).**
Triệu chứng bug gốc ("0/1 (100.00%)", DOCX "Tổng số buổi = 1") **không tái hiện**.
Tử số cũng đúng quy tắc: "Vắng có phép" được tính vào tỷ lệ, "Vắng không phép" thì không.

**Đặc tả đối chiếu:** BR-KQ-02 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:2251`
"`ty_le_chuyen_can` = (số buổi Có mặt + số buổi Vắng có phép) / tổng số buổi × 100".

## Đã cố bác bỏ kết luận Pass bằng 4 hướng — không bác được hướng nào thuộc phạm vi lỗi này

1. **Dựng lại đúng tiền đề bug gốc trên dữ liệu mới hoàn toàn** (N=3 buổi, M=1 buổi điểm danh) → đúng 33.33%.
2. **Đo bằng phương pháp thứ hai — mở đọc nội dung tệp DOCX** (không chỉ nhìn màn hình) → cùng số liệu.
3. **Phủ cả 3 trạng thái điểm danh** để bắt lỗi tử số → đúng quy tắc từng trạng thái.
4. **Sửa lịch học SAU khi đã điểm danh** (thêm buổi 4) → phát hiện lệch, xem mục dưới.

## Phát hiện thêm — NGOÀI phạm vi lỗi này (tách thành dòng TC mới)

Sau khi đã điểm danh xong, thêm **buổi thứ 4** vào Lịch học rồi tải lại trang bỏ bộ nhớ đệm: mẫu số của
5 học viên **không cập nhật**, vẫn là 3 trong khi khóa đã có 4 buổi. Chỉ học viên nào được lưu điểm danh
lần kế tiếp mới nhảy sang mẫu số 4 (tester 1: `1/4 (50.00%)` nằm ngay cạnh tester 2: `1/3 (33.33%)` —
cùng bảng, cùng khóa, ảnh `KTDGKQHT_20-v2-05-...`).

Đây **không phải** tiền đề của bug gốc (bug gốc là "chưa điểm danh hết số buổi", không phải "sửa lịch sau
khi điểm danh") và cũng không do bản vá sinh ra — giá trị này vốn là trường lưu sẵn, tính tại thời điểm lưu
điểm danh. Theo quy trình, lỗi ngoài phạm vi case phải mở **dòng TC mới**, không gộp vào dòng này.
