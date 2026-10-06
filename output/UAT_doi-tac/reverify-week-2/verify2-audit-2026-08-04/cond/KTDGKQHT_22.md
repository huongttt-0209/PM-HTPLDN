# Bảng đối chiếu điều kiện — KTDGKQHT_22 (vòng soát lại 2, 2026-08-04)

> Lỗi "thiếu cột + thiếu thao tác Xem chi tiết" ở tab "Đề kiểm tra" của màn chi tiết khóa học. Bảng này
> vẫn phải điền vì bảng CHỈ hiện khi khóa đã được gán ít nhất 1 đề (chưa gán thì tab chỉ có dòng "Chưa có
> đề kiểm tra nào được gán cho khóa học này") ⇒ kết quả phụ thuộc dữ liệu tiền đề.
> Cột giữa = điều kiện của **BUG GỐC** (đo 03/08/2026), cột phải = điều kiện **thực tế test lại** 04/08/2026.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ đúng đơn vị khóa học (`CB_NV_TW`, Cục Bổ trợ tư pháp) | Chính vai trò + đơn vị đó — `cbnv_tw` (`CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`). Tài khoản `cbnv_tw_05` của lần đo trước không đăng nhập được trên môi trường này nên dùng tài khoản gốc cùng vai trò + cùng đơn vị | Không |
| Entity + trạng thái | Khóa `AAA-KH-TW` trạng thái **Hoàn thành** | Đo trên **2 khóa, 2 trạng thái**: `KH-20260703-005` "test thêm mới khóa học" (**Hoàn thành** — đúng trạng thái bug gốc) và `KH-20260509-006` (Đang diễn ra) | Không |
| Dữ liệu tiền đề — có ≥1 đề kiểm tra trạng thái "Kích hoạt" | Đề `QA-DEKT-0803` do tổ kiểm thử tự tạo (Kích hoạt) | Môi trường này đã sẵn có đề "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" (mã `DKT-000012`, 1 câu hỏi, cách tạo Thủ công, điểm đạt 5, trạng thái **Kích hoạt**) — không phải tạo mới | Không |
| Dữ liệu tiền đề — khóa đã được gán đề đó | Đã gán đề vào khóa lúc 03/08 20:04 | Tự gán đề `DKT-000012` vào **cả 2 khóa** qua nút "Gán đề kiểm tra" (mỗi lần 1 lệnh gửi, 1 thông báo "Đã gán đề kiểm tra") | Không |
| Input / bộ lọc | Không có bộ lọc — chỉ mở tab, đọc tiêu đề cột và xem các thao tác ở cột Hành động | Như vậy; thêm thao tác **cuộn ngang hết cỡ sang phải** + kiểm cột ẩn trong mã trang + **bấm thật** biểu tượng Xem chi tiết | Không |

**Kết luận: 0 GAP.**

---

## Kết quả đo (bản dựng V1.0.5, gói giao diện `index-DpIXRGaI.js`)

Bảng đề kiểm tra đã gán nay có **9 cột** (`<colgroup><col>` = 9, không cột nào ẩn):
STT · **Mã đề** · Tên đề · Số câu hỏi · **Lĩnh vực** · **Người thêm** · Trạng thái · Thời điểm thêm · Hành động.

⇒ **Đủ cả 4 cột trước đây thiếu** (STT, Mã đề, Lĩnh vực, Người thêm).

**Các cột KHÔNG rỗng — giá trị thật đọc được trên cả 2 khóa:**
STT `1` · Mã đề `DKT-000012` · Tên đề "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" · Số câu hỏi `1` ·
Lĩnh vực `Lao động` · Người thêm `Cán bộ NV Trung ương` · Trạng thái `Kích hoạt` ·
Thời điểm thêm `04/08/2026 16:27` (khóa Đang diễn ra) và `04/08/2026 16:35` (khóa Hoàn thành).

**Cột Hành động nay có 2 thao tác:** biểu tượng con mắt (Xem chi tiết) và thùng rác (Gỡ khỏi khóa).
Đã **bấm thật** con mắt: mở được màn chi tiết đề `.../dao-tao/de-kiem-tra/{id}` với nội dung thật
(Tên đề · Cách tạo Thủ công · Số câu hỏi 1 · Thời gian làm bài 30 phút · Điểm đạt 5 · Trạng thái Kích hoạt ·
Ngày tạo 25/05/2026) — ảnh `KTDGKQHT_22-v2-03-...`. Không phải nút trang trí.

**Đặc tả đối chiếu:** FR-III-05 (UC24) §Đặc tả màn hình SCR-III-02 – Tab 7 "Đề kiểm tra" —
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1908`: "Cột: STT · Mã đề ·
Tên đề · Số câu · Lĩnh vực · Người thêm · Thời điểm thêm · Hành động (Xem chi tiết · Gỡ khỏi khóa)".
Đủ 8/8 mục đặc tả.

## Đã cố bác bỏ kết luận Pass bằng 4 hướng — không bác được

1. **Không chấm theo quan sát tĩnh:** tự gán đề qua giao diện để bảng có dữ liệu thật rồi mới đọc cột.
2. **Kiểm cột bị che:** cuộn ngang hết cỡ sang phải, chụp 2 ảnh ghép đủ 9 cột (ảnh `-v2-01` và `-v2-02`),
   đồng thời đếm `colgroup` và kiểm cột ẩn trong mã trang.
3. **Kiểm "cột có nhưng rỗng":** cả 9 cột đều có giá trị thật, không cột nào để trống hoặc bằng 0.
4. **Kiểm thao tác Xem chi tiết có thật sự chạy:** bấm và mở được màn chi tiết đề với đủ thông tin.

## Ghi nhận thêm — khớp với 2 điểm bug gốc để ngỏ

- Cột "Trạng thái" (đặc tả không liệt kê) vẫn còn. Bug gốc đã ghi rõ đây **chỉ là ghi nhận, không tính lỗi**.
- Nút "Gỡ công khai" mà bug gốc đề nghị dev xác nhận: lần đo này thấy rõ nút đó nằm ở **thanh thao tác
  chung của màn chi tiết khóa học** (hiện dưới MỌI tab, và đổi theo trạng thái khóa — khóa Đang diễn ra
  hiện "Gỡ công khai / Kết thúc", khóa Hoàn thành hiện "Công khai"), **không phải nút của riêng tab
  "Đề kiểm tra"**. Vì vậy không có mâu thuẫn với đặc tả tab 7.
