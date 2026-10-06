# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_09 (dòng 335) — Đường dẫn điều hướng màn Sửa

**Kết luận:** Pass — đường dẫn ở chế độ Sửa nay kèm tên tổ chức và không còn cấp "Chi tiết".

**Case thuần tĩnh.** Thanh đường dẫn của màn Chỉnh sửa chỉ lấy tên tổ chức đang mở; đặc tả (SCR-IV-NEW-02 dòng 1675) quy định một chuỗi duy nhất cho chế độ sửa, không phân nhánh theo vai trò hay theo trạng thái hồ sơ. Màn Sửa cũng chỉ mở được với Cán bộ Nghiệp vụ cùng đơn vị (dòng 1667) — đúng vai trò đã dùng. Vì vậy phép đo là **đọc nguyên văn chuỗi chữ trên thanh đường dẫn**, và để loại trừ khả năng tên bị gán cứng thì đo trên 2 hồ sơ khác nhau.

| Ý của bug gốc | Chuỗi vòng 1 | Chuỗi mình đọc được (04/08/2026) | Hết lỗi? |
|---|---|---|:-:|
| Thiếu tên tổ chức đang sửa | `… / Tổ chức tư vấn / Chi tiết / Chỉnh sửa` | TC-BTP-TW-0001: `Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Chỉnh sửa Công ty Luật TNHH Alpha Hà Nội**` | ✔ |
| Chèn thừa cấp "Chi tiết" | có cấp "Chi tiết" | không còn cấp "Chi tiết" — đúng 4 cấp | ✔ |
| Tên có gán cứng không | — | TC-BTP-TW-0003: `… / Tổ chức tư vấn / **Chỉnh sửa Trung tâm TVPL Gamma Đà Nẵng**` — tên đổi theo hồ sơ | ✔ |

Đối chiếu thêm cho chắc không nhầm màn: chế độ **Thêm mới** cho `… / Tổ chức tư vấn / Thêm mới`; màn **Chi tiết** cho `… / Tổ chức tư vấn / Công ty Luật TNHH Alpha Hà Nội`.

**Đặc tả:** `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1675 — `"Trang chủ > Mạng lưới Tư vấn viên > Tổ chức tư vấn > Thêm mới" hoặc "... > Chỉnh sửa [Tên TC]"`.

**Bằng chứng:**
- `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` — thanh trên cùng ghi "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chỉnh sửa Trung tâm TVPL Gamma Đà Nẵng".
- `image/QLDMTCTV_09-v2-01-sua-TC-BTP-TW-0001-duong-dan-co-ten-to-chuc-va-du-lieu-dien-san.png` — hồ sơ thứ 2 với tên tương ứng.
