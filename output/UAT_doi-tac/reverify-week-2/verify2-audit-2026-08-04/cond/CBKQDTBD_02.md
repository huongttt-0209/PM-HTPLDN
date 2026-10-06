# Bảng đối chiếu điều kiện — CBKQDTBD_02 (vòng soát lại 2, 2026-08-04)

> Lỗi "thiếu 5 cột" nghe như bug tĩnh, nhưng **vẫn điền bảng** vì bảng học viên của tab "Công bố kết quả"
> CHỈ hiện khi khóa có bản ghi kết quả, và 2 trong 5 cột tranh chấp (**Đề kiểm tra**, **Điểm**) chỉ có giá trị
> khi dữ liệu kết quả trỏ tới đề / đã nhập điểm ⇒ kết quả phụ thuộc dữ liệu tiền đề.
> Cột giữa = điều kiện của **BUG GỐC** (QA đo 03/08/2026 17:55, bảng chỉ có 7 cột).
> Cột phải = điều kiện **thực tế test lại** 04/08/2026 17:05–17:25 trên `https://htpldn-uat.ospgroup.vn`.
>
> Môi trường lần này **không còn** khóa `AAA-KH-TW` của lần đo trước ⇒ dựng lại tiền đề tương đương:
> khóa **Hoàn thành + có học viên đã được phê duyệt kết quả**, do đúng đơn vị của cán bộ đăng nhập.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ nghiệp vụ đúng đơn vị của khóa học — `CB_NV_TW`, Cục Bổ trợ tư pháp (`donViId 00000000-0000-4000-8000-000000000001`); lần đo cũ dùng `cbnv_tw_05` | Đúng vai trò + đúng đơn vị: **`cbnv_tw`** — "Cán bộ NV Trung ương", `CB_NV_TW`, `capDonVi TW`, hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp". (Thử `cbnv_tw_01` trước: máy chủ trả "Tên đăng nhập hoặc mật khẩu không đúng" nên quay lại tài khoản gốc cùng vai trò + cùng đơn vị.) Không dùng `admin` ra verdict | Không |
| Entity + trạng thái (state machine) | Khóa `AAA-KH-TW` — "Tập huấn pháp lý cấp Trung ương 2026", trạng thái **Hoàn thành** | Đo trên **3 khóa**: `KH-20260703-005` "test thêm mới khóa học" (**Hoàn thành** — trùng trạng thái bug gốc, là khóa chính), `KH-20260703-007` "Test khóa đào tạo" (**Hoàn thành**, kết quả **đã công bố**), `KH-20260509-006` (Đang diễn ra — dùng làm phép thử cột có rỗng cứng hay không) | Không |
| Dữ liệu tiền đề — học viên có kết quả ĐÃ ĐƯỢC PHÊ DUYỆT | 4 học viên đã duyệt kết quả | `KH-20260703-005`: 2 học viên đã duyệt kết quả (Hoàng Minh Đức 5.0 · Đạt; tester tkm 10.0 · Không đạt). `KH-20260703-007`: 1 học viên đã duyệt + **đã công bố** (mốc 28/07/2026 11:00) — để đọc giá trị thật của 2 cột "Trạng thái công bố" / "Thời điểm công bố" | Không |
| Dữ liệu tiền đề — kết quả có gắn ĐỀ KIỂM TRA (điểm dễ Pass oan: cột có mà luôn rỗng) | Không có trong phiếu gốc; lần Pass vòng 1 đã nêu cột "Đề kiểm tra" hiện "—" khi khóa chưa gán đề | Đóng bằng **test thật trên dữ liệu có đề**: khóa `KH-20260509-006` có 2 học viên mà bản ghi kết quả trỏ tới đề "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" ⇒ đọc ô của đúng 2 học viên đó ở tab "Công bố kết quả" | Không |
| Input / bộ lọc | Không có bộ lọc — chỉ mở tab và đọc tiêu đề cột | Như vậy; thêm 2 thao tác chống "cột bị che": **cuộn ngang hết cỡ sang phải** + đo bề rộng/thuộc tính ẩn của từng cột trong mã trang | Không |

**Số ô GAP còn lại: 0** → đủ điều kiện chốt verdict.

---

## Kết quả đo (bản dựng V1.0.5 · gói giao diện `index-DpIXRGaI.js` · đã tải lại trang bỏ bộ nhớ đệm trước khi đo)

### 1. Đủ cột — đo bằng 2 cách độc lập

**Cách 1 — đọc mã trang** (khóa `KH-20260703-005`, đúng trạng thái Hoàn thành của bug gốc):
số ô tiêu đề = **12**, số thẻ định nghĩa cột = **12**, khớp nhau:

`(ô tích chọn)` · `STT` · `Họ tên` · `Email` · `Số điện thoại` · `Đơn vị` · `Đề kiểm tra` · `Điểm` ·
`Kết quả` · `Trạng thái công bố` · `Thời điểm công bố` · `Hành động`

Không cột nào bị ẩn: cả 12 cột đều `display: table-cell`, `visibility: visible`, bề rộng 32–200 px, chiều cao 77 px.

**Cách 2 — nhìn bằng mắt trên ảnh full-res:** bảng CÓ thanh cuộn ngang (bề rộng nội dung 1632 px > khung 1136 px)
nên phải cuộn mới thấy hết. Đã chụp 2 ảnh ghép đủ 12 cột và **mở ra đọc lại**:
- `evidence/CBKQDTBD_02-v2-01-khoa-hoan-thanh-bang-tu-cot-chon-dong-den-ket-qua.png` (từ ô tích chọn → Kết quả)
- `evidence/CBKQDTBD_02-v2-02-cuon-het-sang-phai-du-12-cot-den-hanh-dong.png` (→ Trạng thái công bố · Thời điểm công bố · Hành động)

⇒ **5 cột bị báo thiếu (Email, Số điện thoại, Đơn vị, Đề kiểm tra, Điểm) đều đã có mặt.**

### 2. Cột KHÔNG rỗng cứng — điểm dễ Pass oan, đã đóng bằng dữ liệu thật

- **Họ tên** — "Hoàng Minh Đức" · "tester tkm" (khóa `KH-20260703-005`).
- **Email** — `hoangminhduc@gmail.com` · `tkm@gmail.com` (khóa `KH-20260703-005`).
- **Số điện thoại** — `0105545484` · `0105545486` (khóa `KH-20260703-005`).
- **Đơn vị** — "Cục Bổ trợ tư pháp - Bộ Tư pháp" · "TKM": 2 giá trị KHÁC nhau trên cùng bảng ⇒ không phải hằng số.
- **Đề kiểm tra** — "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026" hiện đúng ở 2 học viên mà bản ghi kết quả
  có gắn đề, 4 học viên chưa có đề vẫn "—" (khóa `KH-20260509-006`; ảnh
  `evidence/CBKQDTBD_02-v2-03-cot-de-kiem-tra-hien-ten-de-that-tren-khoa-co-de.png`).
- **Điểm** — `5.0` · `10.0` (khóa 005); `9.0` · `4.0` (khóa 006).
- **Kết quả** — "Đạt" (nhãn xanh) · "Không đạt" (nhãn đỏ) (khóa `KH-20260703-005`).
- **Trạng thái công bố** — "Chưa công bố" (khóa 005) **và** "Đã công bố" (khóa `KH-20260703-007`).
- **Thời điểm công bố** — "28/07/2026 11:00" trên khóa đã công bố `KH-20260703-007`.
- **Hành động** — nút "Công bố" khi chưa công bố / nút "Hủy" khi đã công bố, có hiển thị ở cả 2 khóa.

**Đối chiếu chéo giá trị bằng màn khác:** mở tab "Học viên" của chính khóa `KH-20260703-005` — Email và
Số điện thoại của 2 học viên **trùng khớp từng ký tự** với những gì tab "Công bố kết quả" hiển thị
⇒ cột không lấy nhầm nguồn dữ liệu.

**Kiểm cả chiều ngược lại (dữ liệu rỗng thì ô phải rỗng):** trên khóa `KH-20260703-005` bản ghi kết quả
không gắn đề nào và ô "Đề kiểm tra" hiện "—"; trên khóa `KH-20260509-006`, 2 học viên có đề thì hiện tên đề,
4 học viên chưa nhập điểm thì "—". ⇒ cột đi theo dữ liệu ở **cả hai chiều**, không phải cột trang trí.

### 3. Đặc tả đối chiếu

`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1932`
(FR-III-19 / UC38 · §Đặc tả màn hình SCR-III-02 — Tab 8 "Công bố kết quả"):
*"Bảng HV có kết quả: Cột Chọn dòng · **Họ tên · Email · Số điện thoại · Đơn vị** · Đề kiểm tra · Điểm ·
Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động (Công bố/Hủy công bố cá nhân)"*
⇒ đặc tả liệt kê **11 mục**, web có **12 cột** = đủ 11 mục + thêm cột `STT` (thêm cột không nằm trong nội dung
phản ánh của phiếu này).

---

## Đã cố bác bỏ kết luận Pass bằng 5 hướng — không bác được

1. **Không chấm tĩnh trên 1 màn:** đo trên **3 khóa học** ở 2 trạng thái, trong đó khóa chính đúng trạng thái
   "Hoàn thành + có kết quả đã phê duyệt" của phiếu gốc.
2. **Bẫy "cột có nhưng luôn rỗng"** (đúng kiểu lỗi vừa bắt được ở `QLLKHDTBD_50` — cột Số chương trình luôn = 0):
   đã tìm bằng được dữ liệu để mỗi cột hiện ít nhất 1 giá trị thật, kể cả cột "Đề kiểm tra" và
   "Thời điểm công bố" — phải sang khóa khác mới có dữ liệu nên đã sang.
3. **Bẫy "cột bị che":** bảng có thanh cuộn ngang thật (1632 px > 1136 px) nên đã cuộn hết cỡ sang phải, chụp
   ảnh và **mở ảnh ra đọc**, đồng thời đo bề rộng + thuộc tính ẩn của từng cột trong mã trang.
4. **Bẫy "hiển thị sai nguồn":** đối chiếu Email / Số điện thoại với màn "Học viên" của cùng khóa — khớp.
5. **Bẫy "đo trên bản dựng cũ trong tab mở lâu":** tải lại trang bỏ bộ nhớ đệm trước khi đo, ghi lại tên gói
   giao diện đang chạy (`index-DpIXRGaI.js`, bản dựng V1.0.5).

⇒ Không bác được: **phần "thiếu 5 cột" của phiếu này đã hết lỗi → Pass.**

---

## Ngoài phạm vi lỗi này (ghi nhận, KHÔNG tính vào verdict của dòng 146)

1. **Nút ở cột "Hành động" luôn mờ, bấm không được** — đây chính là nội dung dòng `CBKQDTBD_01` (row 121) và
   đã được chấm **Reopen** ở vòng soát lại này, nên không log trùng ở dòng 146. Dòng 146 chỉ hỏi *cột có đủ không*.
2. **Cột "Thời điểm công bố" giữ mốc thời gian cũ khi trạng thái đã về "Chưa công bố"** — đã ghi trong phản hồi
   của dòng 121.
3. **Cùng một học viên, cùng một khóa, hai màn hình hiển thị "Đơn vị" khác nhau:** màn "Học viên" hiện `-`
   (không có đơn vị) trong khi màn "Kết quả" và "Công bố kết quả" hiện "Cục Bổ trợ tư pháp - Bộ Tư pháp".
   Đo được ở cả 2 khóa `KH-20260703-005` (Hoàng Minh Đức) và `KH-20260509-006` (tester 2–5); những học viên có
   đơn vị thật (`TKM`) thì cả 3 màn đều hiện `TKM`. Đặc tả SRS liệt kê cột "Đơn vị" ở cả 3 tab (dòng 1918 ·
   1924 · 1932) nhưng không nói ba màn lấy dữ liệu từ ba nguồn khác nhau ⇒ đã mở **dòng TC mới
   `CBKQDTBD_OOS_01` (dòng 150 của tab tuần 2)** kèm 2 ảnh đã tải lên Drive để dev/BA rà, không tính vào
   verdict dòng 146.

> **Lưu ý số dòng SRS:** tệp `srs-fr-03-dao-tao.md` được sửa trong ngày 04/08/2026 nên số dòng dịch **+23** so với đầu giờ chiều; số dòng ở trên đã theo bản mới nhất (Tab 8 = dòng 1932, Tab 5 = 1924, Tab 3 = 1918).
