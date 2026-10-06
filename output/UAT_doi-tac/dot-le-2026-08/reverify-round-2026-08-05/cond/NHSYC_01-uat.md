# NHSYC_01 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối `── CÁCH VERIFY sau Dev fix ──` ở cột `DEV phản hồi lần 1`, dòng 127
(tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — bundle `assets/index-Dn5IWt_M.js`, nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò (bước 1, 2, 4) | `cbnv_tw` — cán bộ nghiệp vụ | `cbnv_tw` · CB_NV_TW · `donViId 00000000-0000-4000-8000-000000000001` · cấp TW | Không |
| Vai trò (bước 3) | Tài khoản doanh nghiệp thuộc diện ưu tiên | `0151554887` — TKM Company, vai trò DN, đang hoạt động | Không |
| Màn hình | Vụ việc HTPL → tạo hồ sơ yêu cầu hỗ trợ pháp lý thủ công | "Nhập thủ công" trên màn Vụ việc HTPL | Không |
| DN thuộc diện ưu tiên (bước 1-2) | DN do phụ nữ làm chủ, hoặc nhiều lao động nữ theo ngưỡng NĐ 80/2021 | `Công ty TNHH Bình Minh AG` (DN-AG-001) — do phụ nữ làm chủ, 18 lao động trong đó 12 nữ (67%) | Không |
| DN thuộc diện ưu tiên (bước 3) | như trên | `TKM Company` (MST 0151554887) — do phụ nữ làm chủ, 50 lao động trong đó 25 nữ | Không |
| Ngày tiếp nhận | Chọn từ ô chọn ngày trên giao diện | Mở lịch, bấm chọn ngày 05/08/2026 (không gõ tay) | Không |
| Bản ghi đối chứng nhãn chữ | Cần đọc nhãn ở nhiều mức để biết đúng chiều | Đọc thêm hồ sơ mức 1 (`VV-BTP-TW-20260804-005`) và mức 5 (`VV-STP-AG-20260709-001`) | Không |
| Thao tác đo | Bấm thật trên giao diện | Toàn bộ bấm trên màn; thông báo bắt bằng bộ theo dõi DOM không lọc trùng | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- Bước 1 · **tạo được hồ sơ, không còn lỗi định dạng ngày**: bấm Lưu & Tiếp nhận → thông báo
  "Đã tiếp nhận — VV-BTP-TW-20260805-001". Không còn thông báo lỗi định dạng ngày tiếp nhận nào.
- Bước 1 · **trạng thái và mã hồ sơ**: hồ sơ vào trạng thái "Đã tiếp nhận"; mã `VV-BTP-TW-20260805-001`
  đúng quy tắc mã đơn vị + ngày + số thứ tự. Ngày tiếp nhận ghi nhận 05/08/2026, thời hạn xử lý 20/08/2026.
- Bước 2 · **mức ưu tiên tự tính, khớp tiêu chí của doanh nghiệp**: màn chi tiết hiện
  `Ưu tiên: 3 — DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ`. Không nhập tay ô Độ ưu tiên
  (để trống theo gợi ý "Để trống để hệ thống tự tính theo hồ sơ doanh nghiệp"). Giá trị khớp đúng hồ sơ
  Bình Minh AG (do phụ nữ làm chủ, tỷ lệ lao động nữ 67%).
- Bước 3 · **luồng doanh nghiệp tự gửi cũng có mức ưu tiên**: đăng nhập tài khoản doanh nghiệp, bấm
  "Gửi yêu cầu hỗ trợ pháp lý" → tạo được `VV-STP-HN-20260805-001`, kênh tiếp nhận "Doanh nghiệp",
  mức ưu tiên **3** với đúng nhãn "DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ". Mở lại bằng
  `cbnv_tw` đọc được cùng giá trị ⇒ vế FAIL "hồ sơ do doanh nghiệp tự gửi không có mức ưu tiên" không xảy ra.
- **Giá trị nằm trong thang 1-5**: cả hai hồ sơ đo được đều là 3; rà toàn bộ hồ sơ hiện có trên môi trường
  chỉ thấy các giá trị 1, 3, 5 — không có giá trị nào vượt ngoài 1-5.
- **Nhãn chữ đúng chiều với giá trị số**: mức 1 → "Mức thường — xét theo thứ tự nộp hồ sơ";
  mức 3 → "DN do phụ nữ làm chủ hoặc sử dụng nhiều lao động nữ"; mức 5 → "Cán bộ nâng mức khẩn, kèm lý do".
  Số càng lớn thì mức càng khẩn ⇒ không còn hiện tượng nhãn ngược chiều.
- Bước 4 · **không còn chuỗi mã quy tắc nội bộ lộ ra giao diện**: màn danh sách không có cột Độ ưu tiên
  và không hiện chuỗi mã nào; màn chi tiết chỉ hiện số kèm câu mô tả tiếng Việt; ô "Độ ưu tiên" trên màn
  Thêm mới có gợi ý tiếng Việt và danh sách chọn chỉ gồm "4 — Cán bộ nâng mức, kèm lý do" và
  "5 — Cán bộ nâng mức khẩn, kèm lý do" (mức 1-3 do hệ thống tự tính) — không chuỗi nào là mã quy tắc.

Ảnh: `../image/NHSYC_01-uat-ho-so-nhap-tay-uu-tien-3.png` · `../image/NHSYC_01-uat-dn-tu-gui-uu-tien-3.png`

## Ghi nhận thêm

- Dòng ⚠️ của phiếu nhắc hai phiếu `NHSYC_09` và `NHSYC_10` (cửa nghiệm thu phần mức ưu tiên) đã bị xóa
  khỏi sổ bàn giao và cần khôi phục từ tab Bản sao. Đây là việc của sổ bàn giao, không phải điều kiện
  PASS/FAIL của phiếu này — vẫn cần xử lý trước khi nghiệm thu phần mức ưu tiên.
- Thay đổi môi trường do QA thực hiện: đặt lại mật khẩu tài khoản doanh nghiệp kiểm thử `0151554887`
  ("Tester TKM") qua luồng "Quên mật khẩu?" + hộp thư của môi trường, nay là `Test@1234` — vì không có
  tài khoản doanh nghiệp nào biết mật khẩu để chạy bước 3.
- Dữ liệu phát sinh khi đo (là bước bắt buộc của chính khối tiêu chí, không xóa được bằng giao diện):
  `VV-BTP-TW-20260805-001` (nhập tay) và `VV-STP-HN-20260805-001` (doanh nghiệp tự gửi).
