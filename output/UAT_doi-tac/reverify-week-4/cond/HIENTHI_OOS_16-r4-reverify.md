# Bảng đối chiếu điều kiện — HIENTHI_OOS_16 (row 51) — re-verify R4 sau khi dev báo fix

**Kết luận:** Pass.
- Ô lọc "Từ ngày" / "Đến ngày" màn Kho câu hỏi nay ghi `01/07/2026` · `31/07/2026` (đúng `dd/MM/yyyy`).
- Hệ quả kèm theo cũng hết: gõ tay `15/07/2026` lịch nhận đúng ngày 15/07/2026.
- Hai màn đối chứng không hồi quy; bộ lọc vẫn trả đúng dữ liệu.

> ⚠️ **GIỚI HẠN PHẠM VI RE-VERIFY (đọc trước khi dùng kết luận này):** lượt đo thực hiện trên **env được giao `18.143.165.120.nip.io`** — đúng phạm vi môi trường mà người phụ trách giao (`input/input.md`). Env đối tác `htpldn-uat.ospgroup.vn` đang chạy **bản dựng khác** (tài nguyên `assets/index-B4L2Psgc.js` so với `assets/index-C-Au2yTy.js` của env được giao; nhãn `V1.0.3` so với `V1.0.4`), và ảnh chụp 31/07/2026 14:41 trên env đó cho thấy **lỗi vẫn tái hiện**. Kết luận Pass vì vậy chứng minh **mã nguồn đã được sửa**, **chưa** chứng minh bản sửa đã lên env đối tác. Dòng "Môi trường" trong bảng ghi GAP = "Không" theo đúng phạm vi đã giao đó, **không** phải khẳng định hai env giống nhau.
> 
> QA **không** đăng nhập được env đối tác ở lượt này để đo trực tiếp: mã xác thực gửi tới hộp thư `***@htpldn.gov.vn` không rơi vào MailHog `18.143.165.120:8025` (bản ghi gov.vn mới nhất ở đó là 30/07/2026 15:37, lượt đăng nhập 31/07/2026 không sinh thư mới) ⇒ phần đối chiếu env dựa trên **tài nguyên bản dựng đọc trực tiếp từ trình duyệt** + ảnh đã chụp trước đó, không phải suy đoán.

| Điều kiện có thể đổi kết quả | Bug gốc (`BUG-KCH-LOC-NGAY-KIEU-QUOC-TE`, đo 30/07/2026 · V1.0.3) | Mình test lại (env nip.io, 31/07/2026 · V1.0.4) | GAP? |
|---|---|---|:-:|
| Môi trường | Env đối tác `htpldn-uat.ospgroup.vn` — nơi bug gốc được đối tác quan sát | Env được giao `18.143.165.120.nip.io` — **phạm vi re-verify đã được giao là env này**, xem khối cảnh báo phía trên | Không |
| Vai trò / tài khoản | `cbnv_tw_02` — CB Nghiệp vụ Trung ương, badge "BTP · TW" | `cbnv_tw_02` — CB Nghiệp vụ - Trung ương #02, badge "BTP · TW" — TRÙNG KHỚP | Không |
| Màn hình / thành phần đo | Thanh lọc màn *Tư vấn → Kho câu hỏi*, 2 ô chọn ngày `.ant-picker` do ứng dụng tự dựng | Đúng màn `/tv-nhanh/kho-cau-hoi`, đúng 2 ô `.ant-picker` (`placeholder` = "Từ ngày"/"Đến ngày"), không có thuộc tính `type` ⇒ không phải ô ngày mặc định của trình duyệt | Không |
| Entity + trạng thái (state machine) | Không phụ thuộc trạng thái bản ghi — lỗi ở khuôn hiển thị của ô nhập; chỉ cần kho có dữ liệu để bộ lọc trả kết quả | Kho câu hỏi có 33 bản ghi (tab Tất cả 33 · Đã duyệt 19 · Chờ duyệt 14) ⇒ bộ lọc trả được kết quả để kiểm tra — TRÙNG KHỚP | Không |
| Dữ liệu tiền đề | Bản ghi có Ngày tạo nằm trong tháng 7/2026 | 33 bản ghi Ngày tạo 27–30/07/2026 + các bản ghi cũ, đủ để phân biệt khoảng 01–31/07 và 15–31/07 | Không |
| Input / thao tác chọn ngày | Chọn 01/07/2026 và 31/07/2026 **bằng cách bấm trên lịch** (không gõ tay), rồi đọc chữ trong ô | Chọn đúng 2 ngày đó bằng cách bấm ô ngày trên lịch, rồi đọc `value` của ô + chụp màn hình — TRÙNG KHỚP cách thao tác | Không |
| Input / thao tác gõ tay | Gõ `15/07/2026` (khuôn Việt) và `2026-07-15` (khuôn quốc tế) vào ô "Từ ngày" | Gõ đúng 2 chuỗi đó bằng bàn phím thật vào ô "Từ ngày", đọc ô ngày được lịch chọn sau mỗi lần gõ — TRÙNG KHỚP | Không |
| Màn đối chứng | *Tư vấn → Tư vấn nhanh* và *Chương trình HTPLDN → Danh sách* (cùng loại ô lọc) — bug gốc ghi 2 màn này ĐÚNG khuôn | Đo lại đúng 2 màn đó trong cùng phiên đăng nhập, cùng cách bấm lịch | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render + Hành vi nhập liệu)

- `bug-reports/image/R4-HIENTHI_OOS_16-01-kho-cau-hoi-o-loc-dd-mm-yyyy.png` — đã mở đọc: thanh lọc màn Kho câu hỏi, ô "Từ ngày" = **01/07/2026**, ô "Đến ngày" = **31/07/2026**.
- `bug-reports/image/R4-HIENTHI_OOS_16-02-doi-chung-ct-htpldn-dd-mm-yyyy.png` — đã mở đọc: màn Chương trình HTPLDN, cùng loại ô lọc, cũng **01/07/2026** / **31/07/2026** ⇒ không hồi quy.
- Đọc thẳng giá trị hiển thị của ô nhập sau khi bấm lịch:
  `Từ ngày = "01/07/2026"`, `Đến ngày = "31/07/2026"` (trước đây là `"2026-07-01"` / `"2026-07-31"`).

## Phương pháp thứ hai (bắt buộc)

- **Đường mã khác — dựng lại từ địa chỉ trang thay vì từ thao tác người dùng:** tải lại trang ở địa chỉ `?tuNgay=2026-07-01&denNgay=2026-07-31` (tham số vẫn là khuôn quốc tế ở tầng kỹ thuật, đúng đặc tả). Sau khi tải lại, hai ô vẫn hiện `01/07/2026` / `31/07/2026` ⇒ khuôn hiển thị đúng ở **cả hai đường**: dựng từ thao tác chọn lịch và dựng lại từ tham số địa chỉ.
- **Đo hành vi nhập liệu chứ không chỉ chữ hiển thị:** gõ `15/07/2026` → lịch chọn đúng ô ngày 15/07/2026 (trước đây không nhận diện ngày nào). Gõ `2026-07-15` → lịch **không** nhận diện; đây là hệ quả đúng hướng vì đặc tả (`srs-v3.5.md:4637` I18N-03) chỉ cho phép khuôn `dd/MM/yyyy` ở giao diện, khuôn quốc tế chỉ dùng ở tầng lưu trữ và nhóm API tích hợp.
- **Loại khả năng "lỗi chỉ chuyển chỗ":** đo cùng phép thử gõ tay trên màn đối chứng *Chương trình HTPLDN* — kết quả **y hệt** (nhận `15/07/2026`, không nhận `2026-07-15`) ⇒ hai màn nay dùng chung một khuôn ngày, không còn chênh lệch giữa các màn như bug gốc mô tả.
- **Dữ liệu không bị ảnh hưởng:** khoảng 01–31/07 trả `Hiển thị 1-20 / 33 kết quả`; thu hẹp còn 15–31/07 trả `Hiển thị 1-20 / 24 kết quả`, mọi dòng có Ngày tạo ≥ 15/07 ⇒ bộ lọc vẫn chạy đúng sau khi đổi khuôn hiển thị.
- **Bản dựng:** thanh bên trái ghi `HTPLDN · V1.0.4` (bug gốc đo trên V1.0.3) ⇒ đúng là bản đã có thay đổi của dev.
