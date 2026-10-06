# CNHSNLTVV_03 (sheet `bug` dòng 36) — Trường Ngày ở tab Năng lực sau khi lưu

- Môi trường: https://htpldn-uat.ospgroup.vn — bản dựng **HTPLDN · V1.0.11**
- Tài khoản: **`nht_01`** = `NHT-STP-AG-0001` "Phùng Thị NHT An Giang", **Sở Tư pháp An Giang** (tài khoản địa phương; cách giành lại phiên xem file dòng 35)
- Bản ghi đo: **`TVV-STP-AG-0003`** — hồ sơ do chính tài khoản này tạo ở dòng 35
- Thời điểm: 2026-08-11 ~10:26 – 10:32

## Ô "Kết quả verify" không có tiêu chí sẵn — verify theo đúng nội dung lỗi ghi trong ô

Nguyên văn ô: *"Lỗi hiển thị thông tin Ngày sau khi lưu thành công / Tab Năng lực: '…cấp invalid Date.'"*

⇒ Phép đo: nhập một trường Ngày trong phần năng lực, lưu thành công, rồi đọc lại trường đó ở tab **Năng lực** — nếu vẫn hiện "invalid Date" thì còn lỗi.

Đo cả **hai đường vào** dẫn tới cùng chỗ hiển thị đó:

| Lượt | Đường vào | Ngày đã nhập | Phản hồi lượt lưu | Tab Năng lực hiện |
|---|---|---|---|---|
| 1 | Chi tiết hồ sơ → **Sửa hồ sơ** → Chứng chỉ chi tiết → ô "Ngày cấp" → Lưu | 15/06/2020 | "Cập nhật hồ sơ TVV thành công", `PATCH /api/v1/tu-van-viens/b1f1a182-…` → **200** | "… — So Tu phap An Giang — **cấp 15/06/2020**" |
| 2 | Tab **Năng lực** → nút **Cập nhật năng lực** → thêm chứng chỉ → ô "Ngày cấp" → Lưu | 01/03/2024 | "Cập nhật năng lực thành công", `PATCH /api/v1/tu-van-viens/b1f1a182-…/nang-luc` → **200** | "… — **cấp 01/03/2024**" |
| 3 | Lặp lại lượt 2 sau khi **tải lại trang** (để đo sạch, xem mục cảnh báo bên dưới) | 02/04/2024 | `PATCH …/nang-luc` → **200**, đúng **1** request cho 1 lần bấm Lưu | "… — **cấp 02/04/2024**" |

## Kết quả

| Điểm chấm | Đo được | Kết |
|---|---|---|
| Trường Ngày sau khi lưu có còn hiện "invalid Date"? | **Không.** Quét toàn bộ nội dung tab Năng lực ở cả 3 lượt: không có chuỗi "invalid Date", không có "NaN", không có "null/undefined" | ✅ |
| Ngày hiện ra có đúng ngày đã nhập? | Đúng từng lượt: 15/06/2020 · 01/03/2024 · 02/04/2024 | ✅ |
| Có lưu được thật (không phải chỉ hiển thị)? | Cả 3 lượt máy chủ trả 200; đọc lại sau khi tải lại trang vẫn đúng ngày | ✅ |

Nội dung tab Năng lực đọc được ở lượt cuối:

```
Năng lực chuyên môn · Trình độ Thạc sĩ · Số năm kinh nghiệm 7 năm
Bằng cấp chi tiết:   Luat kinh te — Truong Dai hoc Luat Ha Noi — Năm tốt nghiệp 2010
Chứng chỉ chi tiết:  Chung chi hanh nghe tu van phap luat R36 — So Tu phap An Giang — cấp 15/06/2020
                     Chung chi bo sung do qua nut Cap nhat nang luc — So Tu phap An Giang — cấp 02/04/2024
Số thẻ hành nghề TVV-AG-R35-110826 · Chuyên ngành Luật doanh nghiệp · Lĩnh vực Doanh nghiệp, Thuế
```

## Cảnh báo về cách đo (không phải lỗi phần mềm)

Ở lượt 2, bộ đếm request của tôi ghi **2** lượt `PATCH …/nang-luc` và thông báo hiện lặp nhiều lần. Nguyên nhân là chính tôi đã cài chồng bộ theo dõi qua nhiều lần gọi (mỗi lần gọi lại bọc thêm một lớp), nên **một** thao tác bị ghi thành nhiều lượt. Đã tải lại trang, cài đúng một lớp, và đếm lại bằng công cụ mạng gốc ở lượt 3: **1 lần bấm Lưu = đúng 1 request**, trên màn cũng chỉ có 1 thông báo. **Không có** chuyện gửi trùng hay hiện thông báo đôi — nếu không đo lại thì đã báo oan một lỗi không tồn tại.

## Bằng chứng

- [image/CNHSNLTVV_03-r36-uat-tab-nang-luc-ngay-cap-hien-dung.png](image/CNHSNLTVV_03-r36-uat-tab-nang-luc-ngay-cap-hien-dung.png) — tab Năng lực của `TVV-STP-AG-0003`, hai dòng chứng chỉ hiện đúng ngày cấp
