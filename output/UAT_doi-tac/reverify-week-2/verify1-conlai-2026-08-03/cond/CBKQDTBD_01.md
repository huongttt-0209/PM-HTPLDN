# Bảng đối chiếu điều kiện — CBKQDTBD_01

**Loại bug:** phụ thuộc **trạng thái entity** (khóa học) ⇒ **KHÔNG phải bug tĩnh** → bắt buộc điền bảng này.
**Nguồn điều kiện đối tác:** đọc full-res `partner-evidence/CBKQDTBD_01.jpg` + crop `frames/CBKQDTBD_01/*.png`.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `Cán bộ NV Trung ương` — mã vai trò `CB_NV_TW`, đơn vị `BTP · TW` (đọc ở góc phải ảnh) | `cbnv_tw` = "CB Nghiệp vụ - Trung ương", vaiTro `CB_NV_TW`, donViId `00000000-0000-4000-8000-000000000001`, capDonVi `TW`, đơn vị hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp" | Không |
| Entity + trạng thái (state machine) | Khóa học UUID `0aad5545-9361-4fe4-854a-18e3fdce5862`; stepper 6 bước đầu ✓, bước 7 "Hoàn thành" ĐANG ĐỨNG (vòng tròn xanh đậm số 7) ⇒ HOAN_THANH | Đo ở 2 trạng thái: (1) `KH-QAW7-HOINGHI` ở bước 4 "Đang diễn ra" — CHƯA đủ tiền đề; (2) `AAA-KH-TW` "Tập huấn pháp lý cấp Trung ương 2026" ở bước 7 "Hoàn thành" — ĐÚNG trạng thái đối tác | Không |
| Dữ liệu tiền đề (kết quả đã duyệt) | Banner "Kết quả đào tạo đã được phê duyệt" + bảng 2 học viên có Điểm (5.0 / 10.0), Kết quả (Đạt / Không đạt), Xếp loại ⇒ có ≥1 KQ đã duyệt (PRE-03) | `AAA-KH-TW` có 4 học viên kết quả đã duyệt (khóa đạt HOAN_THANH ⇒ KQ đã qua cổng duyệt); tab Công bố liệt kê đủ 4 dòng, thao tác Công bố / Hủy công bố chạy được trên cả 4 | Không |

**Số ô GAP còn lại: 0** → đủ điều kiện chốt verdict.

> Dòng "Input / filter" **không ghi** vì case đo *sự tồn tại của tab*, không có ô nhập / bộ lọc nào chi phối kết quả (theo hướng dẫn: chỉ ghi điều kiện **có khả năng đổi kết quả**).

---

## Đo đối chiếu ≥2 trạng thái — bằng chứng phân biệt "thiếu tính năng" vs "tab hiển thị có điều kiện"

Bảng đo chi tiết đặt ở `reverify-audit/CBKQDTBD_01.md` §1 (để file này chỉ chứa đúng Bảng đối chiếu điều kiện). Tóm tắt:

- Khóa **CHƯA đủ tiền đề** (`KH-QAW7-HOINGHI`, *Đang diễn ra*) — **8 tab**, **CÓ** tab "Công bố kết quả".
- Khóa **ĐÃ đủ tiền đề** (`AAA-KH-TW`, *Hoàn thành*, 4 KQ đã duyệt) — **8 tab**, **CÓ** tab "Công bố kết quả".
- Ảnh đối tác 28/07/2026 (*Hoàn thành*) — **7 tab**, **KHÔNG** có tab "Công bố kết quả".

**Kiểm tra node ẩn:** mỗi tab đều đọc `getComputedStyle().display / visibility / opacity` + `getBoundingClientRect()`; không tab nào `display:none` hay 0×0 ⇒ danh sách đầy đủ, không sót tab ẩn.

**Kết luận đo:** tab "Công bố kết quả" trên bản dựng hiện tại hiển thị ở **mọi** trạng thái khóa học, không phải tab có điều kiện hiển thị. Vì vậy việc đối tác không thấy tab **không** do họ mở nhầm khóa chưa đủ tiền đề — mà do bản dựng họ kiểm thử đặt chức năng này làm **nút bên trong tab "Kết quả"** (nhìn thấy rõ trong chính ảnh của họ), chưa tách thành tab riêng.
