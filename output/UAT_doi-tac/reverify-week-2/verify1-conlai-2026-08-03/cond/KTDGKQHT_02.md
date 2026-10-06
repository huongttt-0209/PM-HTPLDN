# KTDGKQHT_02 — Bảng đối chiếu điều kiện (verify vòng 1, 2026-08-03)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 116 · Verdict: `BA confirm`
> Đối tác báo: Tab "Kết quả kiểm tra" thiếu 4 cột *Số buổi có mặt · Số buổi vắng có phép · Số buổi vắng không phép · Tổng số buổi*.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `Cán bộ NV Trung ương` — mã vai trò **CB_NV_TW**, đơn vị **BTP · TW** (đọc từ header phải của cả 2 ảnh `KTDGKQHT_02_v2-1.jpg` / `-2.jpg`) | Đăng nhập **`cbnv_tw`** — header web hiện đúng `CB Nghiệp vụ - Trung ương` · `CB_NV_TW` · `BTP · TW`, đơn vị `Bộ Tư Pháp · Cục Bổ trợ tư pháp` | **Không** |
| Entity + **trạng thái** (state machine) | Khoá học id `0362c6e3-1968-4644-9001-d24b267e6b21`, stepper bước **4 · Đang diễn ra**; tab Kết quả có băng vàng *"Kết quả tạm tính"* | Khoá **`KH-QAW7-HOINGHI`** (id `a7480002-0000-4000-8000-000000000002`), stepper bước **4 · Đang diễn ra**, cùng đơn vị Cục Bổ trợ tư pháp; tab Kết quả hiện đúng băng *"Kết quả tạm tính"* | **Không** |
| Dữ liệu tiền đề (học viên · buổi học · điểm danh) | 1 học viên (`Hoàng Minh Đức`); khoá có **3 buổi** (đọc từ ô `Chuyên cần = 0/3`); đã điểm danh buổi `15/07/2026 14:00–15:00` với trạng thái **Vắng có phép** | **Đã tự seed** (Nguyên tắc 4): thêm **3 buổi học** qua tab Lịch học (10/05 08:00–10:00 · 10/05 14:00–16:00 · 11/05 08:00–10:00), khoá sẵn có **2 học viên**; đã điểm danh buổi 1: HV#1 = **Vắng có phép**, HV#2 = **Có mặt**, lưu thành công (`POST …/diem-danhs/batch-update`, 1 request → 1 thông báo *"Đã lưu điểm danh"*) | **Không** |
| Input / filter / giá trị nhập | Không có filter nào được áp (ô "Tìm theo tên học viên" trống, dropdown "Kết quả" chưa chọn) | Giữ nguyên mặc định: ô tìm kiếm trống, dropdown "Kết quả" chưa chọn; **cuộn hết thanh ngang** của bảng để lộ cột cuối | **Không** |

## Kiểm chứng bổ sung — cột có phụ thuộc trạng thái khoá học không?

Giả thuyết cần loại trừ: *4 cột chỉ hiện khi khoá ở trạng thái khác*. Đã đo bộ cột tab "Kết quả" trên **3 trạng thái**:

- `KH-QAW7-HOINGHI` — **Đang diễn ra** — **10 cột**: STT · Họ tên · Email · Số điện thoại · Đơn vị · Chuyên cần · Điểm kiểm tra · Kết quả · Xếp loại · Ghi chú
- `KH-SEED-0001` — **Đã kết thúc** — **10 cột**, y hệt danh sách trên
- `AAA-KH-TW` — **Hoàn thành** — **10 cột**, y hệt danh sách trên

→ Bộ cột **không đổi theo trạng thái**. Kết luận không phụ thuộc state ⇒ 0 GAP ở mọi trạng thái đã thử.

## Ghi chú phương pháp

- Danh sách cột lấy bằng `querySelectorAll('thead th')` **trong đúng `.ant-tabs-tabpane-active`** (AntD giữ mount cả tabpanel ẩn — lấy toàn trang sẽ gộp nhầm cột của tab Lịch học/Điểm danh).
- Bảng có `scrollWidth 1315` vs `clientWidth 1128` → còn **187px** khuất bên phải; đã cuộn `scrollLeft = scrollWidth` và chụp lại: cột khuất duy nhất là **Ghi chú**, không có cột nào trong 4 cột đối tác nêu.
