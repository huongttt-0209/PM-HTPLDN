# Bảng đối chiếu điều kiện — KTDGKQHT_21 (vòng soát lại 2, 2026-08-04)

> Lỗi "thiếu cột" nhưng **có nghi vấn render theo điều kiện dữ liệu** (khóa đã gán đề / bản ghi kết quả đã
> trỏ tới đề) nên vẫn điền bảng thay vì khai bug tĩnh. Cột giữa = điều kiện của **BUG GỐC** (đo 03/08/2026),
> cột phải = điều kiện **thực tế test lại** 04/08/2026 trên môi trường `htpldn-uat.ospgroup.vn`.
>
> Môi trường lần này **không có** đề `QA-DEKT-0803` lẫn 2 khóa `KH-QAW7-HOINGHI` / `AAA-KH-TW` của lần đo
> trước ⇒ phải dựng lại tiền đề tương đương từ đầu.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ đúng đơn vị khóa học (`CB_NV_TW`, Cục Bổ trợ tư pháp, `donViId 00000000-0000-4000-8000-000000000001`) | Chính vai trò + đơn vị đó — `cbnv_tw` (`CB_NV_TW`, `capDonVi TW`, hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp"). Tài khoản `cbnv_tw_05` của lần đo trước KHÔNG đăng nhập được trên môi trường này (máy chủ trả "Tên đăng nhập hoặc mật khẩu không đúng") nên dùng tài khoản gốc cùng vai trò + cùng đơn vị | Không |
| Entity + trạng thái | Đo trên 2 khóa ở 2 trạng thái: "Đang diễn ra" và "Hoàn thành" | Cũng đo **2 khóa, 2 trạng thái**: `KH-20260509-006` (Đang diễn ra) và `KH-20260703-005` (Hoàn thành, kết quả đã được phê duyệt) | Không |
| Dữ liệu tiền đề — khóa ĐÃ gán đề kiểm tra (điểm nghi vấn chính của bug gốc) | Đã tạo đề trạng thái "Kích hoạt" rồi gán vào khóa; cột vẫn không hiện | Gán đề "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" (mã `DKT-000012`, trạng thái **Kích hoạt**) vào `KH-20260509-006` qua tab "Đề kiểm tra"; đo cột **trước** và **sau** khi gán | Không |
| Dữ liệu tiền đề — bản ghi kết quả đã trỏ tới đề | Đã nhập điểm 9.0 / 4.0 để bản ghi kết quả trỏ đúng vào đề; cột vẫn không hiện | Nhập điểm **9.0** (tester 1) và **4.0** (tester 2) rồi bấm [Lưu kết quả] (1 lệnh gửi, 1 thông báo "Đã lưu kết quả"); đo lại cột | Không |
| Input / bộ lọc | Không có bộ lọc — chỉ mở tab và đọc tiêu đề cột | Như vậy; thêm thao tác **cuộn ngang hết cỡ sang phải** + kiểm cột ẩn trong mã trang để loại trừ cột bị che | Không |

**Kết luận: 0 GAP.**

---

## Kết quả đo (bản dựng V1.0.5, gói giao diện `index-DpIXRGaI.js`)

Bảng học viên tab "Kết quả" nay có **11 cột**, trong đó **CÓ cột "Đề kiểm tra"**:
STT · Họ tên · Email · Số điện thoại · Đơn vị · **Đề kiểm tra** · Chuyên cần · Điểm kiểm tra · Kết quả ·
Xếp loại · Ghi chú. Số phần tử `<colgroup><col>` = 11, không cột nào bị ẩn (`display:none` / bề rộng 0).

**Cột KHÔNG rỗng — đã kiểm bằng thao tác thật, không chỉ nhìn tiêu đề:**

- Trước khi gán đề: ô "Đề kiểm tra" của cả 6 học viên hiện `—`.
- Sau khi gán đề nhưng chưa nhập điểm: vẫn `—` (bản ghi kết quả chưa trỏ tới đề nào).
- Sau khi nhập điểm 9.0 / 4.0 và bấm [Lưu kết quả]: ô "Đề kiểm tra" của **đúng 2 học viên đó** hiện
  **"Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026"**, 4 học viên chưa nhập điểm vẫn `—`.
  ⇒ cột lấy đúng đề gắn với điểm của từng học viên, không phải cột trang trí luôn rỗng.
- Đo lại trên khóa `KH-20260703-005` trạng thái **Hoàn thành** (kết quả đã phê duyệt): cũng đủ 11 cột, có
  "Đề kiểm tra".

**Đặc tả đối chiếu:** FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 – Tab 5 "Kết quả kiểm tra" —
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1901`: "Cột STT · Họ tên ·
Email · Số điện thoại · Đơn vị · **Đề kiểm tra** · Điểm · Xếp loại · Kết quả · Ghi chú". Đủ 10/10 cột đặc tả.

## Đã cố bác bỏ kết luận Pass bằng 4 hướng — không bác được

1. **Không chấm theo quan sát tĩnh:** chạy trọn luồng gán đề → nhập điểm → lưu → đọc lại cột.
2. **Kiểm cột luôn rỗng:** so 3 trạng thái dữ liệu (chưa gán đề / đã gán chưa nhập điểm / đã nhập điểm) —
   cột đổi giá trị đúng theo dữ liệu.
3. **Kiểm cột bị che:** cuộn ngang hết cỡ sang phải, chụp ảnh đọc lại bằng mắt (thấy tận cột "Ghi chú"),
   đồng thời đếm `colgroup` và kiểm cột ẩn trong mã trang.
4. **Đo ở 2 trạng thái khóa khác nhau** (Đang diễn ra và Hoàn thành) — kết quả như nhau.

**Ngoài phạm vi lỗi này (không tính vào verdict):** cột "Chuyên cần" mà bản dựng thêm vào tab (đặc tả
dòng 1901 không liệt kê) đang là **câu hỏi chờ BA** ở dòng 116 `KTDGKQHT_02` — không log trùng ở đây.
