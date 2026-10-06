# Bảng đối chiếu điều kiện — KTDGKQHT_20

> Lỗi do QA tự phát hiện khi verify KTDGKQHT_02 (không có phản ánh đối tác) → cột giữa ghi điều kiện của **bug gốc do QA đo**.
>
> ⚠️ **Đây là trường LƯU TRONG CSDL, không tính lại lúc hiển thị** (dev đã cảnh báo). Bản ghi tạo trước bản vá giữ nguyên giá trị cũ ⇒ đo lại trên đúng bản ghi cũ sẽ cho kết luận SAI. Vì vậy vòng re-test 2026-08-04 **cố ý dựng dữ liệu chuyên cần MỚI hoàn toàn qua giao diện** thay vì dùng lại bản ghi cũ — đây là điều kiện **bắt buộc để phép đo có giá trị**, không phải sai lệch điều kiện.

| Điều kiện có thể đổi kết quả | Điều kiện khi phát hiện lỗi | Mình test (re-test 2026-08-04) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ Trung ương (cbnv_tw, CB_NV_TW, Cục Bổ trợ tư pháp) | Chính vai trò + đơn vị đó — `cbnv_tw_01` (CB_NV_TW, `BTP · TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`) | Không |
| Entity + trạng thái | Khóa học trạng thái **Đang diễn ra**, có học viên đã duyệt | Khóa học `KH-20260730-001` — QA tự đưa lên **Đang diễn ra** ngay trong phiên (Đã duyệt → Khai giảng), 3 học viên đã duyệt | Không |
| Dữ liệu tiền đề — hình dạng dữ liệu quyết định kết quả | Lịch học có **3 buổi**, mới điểm danh **1/3 buổi** (có "Vắng có phép" và "Có mặt") | **Đúng hình dạng đó, dựng mới 100% qua giao diện**: thêm 3 buổi vào tab Lịch học, chỉ điểm danh **1 buổi**, HV1 = "Vắng có phép", HV2 = "Có mặt", HV3 = "Vắng không phép" | Không |
| Dữ liệu tiền đề — bản ghi chuyên cần phải là bản ghi MỚI (sinh sau bản vá) | Bản ghi cũ, sinh trước bản vá | Khóa được chọn có **0 lần điểm danh từ trước**: đã chụp lại tab "Kết quả" TRƯỚC khi điểm danh — cột "Chuyên cần" của cả 3 học viên đều `—` ⇒ giá trị đo được sau đó là giá trị **mới sinh trong phiên này**, không phải giá trị đóng băng | Không |
| Input / thao tác đo | Đọc ô "Chuyên cần" trên tab Kết quả + mở tệp xuất ra đọc nội dung | Đúng như vậy: (1) đọc ô "Chuyên cần" trên tab Kết quả; (2) bấm "Xuất DOCX" rồi **mở đọc nội dung tệp** ở cột "Tổng số buổi" + "Tỉ lệ chuyên cần (%)" | Không |

**Kết luận: 0 GAP.**

**Hai phương pháp đo độc lập, khớp nhau (re-test 2026-08-04, gói giao diện `index-BrKDNUvo.js`):**

- **HV1 — điểm danh buổi 1 = "Vắng có phép":** ô "Chuyên cần" trên tab Kết quả `0/3 (33.33%)` · trong tệp DOCX: Tổng số buổi `3`, Tỉ lệ chuyên cần (%) `33.33`
- **HV2 — điểm danh buổi 1 = "Có mặt":** ô "Chuyên cần" trên tab Kết quả `1/3 (33.33%)` · trong tệp DOCX: Tổng số buổi `3`, Tỉ lệ chuyên cần (%) `33.33`
- **HV3 — điểm danh buổi 1 = "Vắng không phép":** ô "Chuyên cần" trên tab Kết quả `0/3 (0.00%)` · trong tệp DOCX: Tổng số buổi `3`, Tỉ lệ chuyên cần (%) `0.00`

**Đối chiếu kỳ vọng đặc tả:** BR-KQ-02 (`srs-fr-03-dao-tao.md` dòng 2251) — tỷ lệ chuyên cần = (số buổi Có mặt + số buổi Vắng có phép) / **tổng số buổi của khóa** × 100. Với 3 buổi mà mới điểm danh 1 buổi: học viên "Vắng có phép" và học viên "Có mặt" đều phải ra **33.33%**, học viên "Vắng không phép" phải ra **0%**. Kết quả đo **khớp cả 3 dòng** ⇒ mẫu số nay là **tổng số buổi của khóa (3)**, không còn là số buổi đã điểm danh (1).

**Ghi nhận thêm (không thuộc phạm vi lỗi này):** ô "Chuyên cần" hiển thị phân số theo *số buổi có mặt* trong khi phần trăm tính theo BR-KQ-02 (gồm cả Vắng có phép), nên dòng HV1 đọc là `0/3` nhưng `33.33%`. Cách gộp `số buổi có mặt / tổng buổi (tỷ lệ %)` vào cùng một ô đang là câu hỏi **chờ BA** ở dòng 116 `KTDGKQHT_02` — không log trùng ở đây. Tệp DOCX tách rõ thành 2 cột nên không có nhập nhằng này.

**Bản ghi cũ (chỉ để tham chiếu, KHÔNG dùng làm căn cứ):** khóa `KH-QAW7-HOINGHI` đo trong cùng phiên vẫn hiện `0/1 (100.00%)` và `1/1 (100.00%)` — đúng như dev đã cảnh báo về giá trị lưu sẵn: khóa cũ chỉ tự đúng khi có lần điểm danh kế tiếp.
