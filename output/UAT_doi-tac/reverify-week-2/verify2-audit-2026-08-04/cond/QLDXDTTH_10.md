# QLDXDTTH_10 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 134 · Verdict Verify 2: `Reopen`
> Bug gốc: tab **"Đề xuất đào tạo"** (màn Chương trình đào tạo) **thiếu cột "Người đề xuất"** → *"Cán bộ không
> biết đề xuất là của ai"*. Bảng khi đó chỉ có 8 cột; màn chi tiết cũng không hiển thị người đề xuất.
> Kết quả mong đợi của phiếu: *"Bảng đề xuất có cột 'Người đề xuất' để cán bộ biết đề xuất là của
> **doanh nghiệp / người hỗ trợ** nào."* — chiếu `srs-fr-03-dao-tao.md:1898`:
> *"**Thành phần 8 — Tab "Đề xuất đào tạo":** Tab phụ tiếp nhận đề xuất **từ DN/NHT**. Bảng cột Lĩnh vực ·
> Nội dung (cắt 150 ký tự) · **Người đề xuất** · Trạng thái · Ngày tạo · Hành động…"*
> Bug phụ thuộc **vai trò cán bộ + dữ liệu đề xuất có sẵn** ⇒ KHÔNG phải bug tĩnh (cột có tồn tại nhưng **giá trị**
> phụ thuộc nguồn gửi) ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Đăng nhập tài khoản **Cán bộ nghiệp vụ**"* | Đo bằng **2 tài khoản cán bộ nghiệp vụ**: (1) **`cb_nv_dp_01`** — `CB NV DP 01 (AG)`, `CB_NV_DP`, đơn vị `Sở Tư pháp An Giang`; (2) **`cbnv_tw`** — `Cán bộ NV Trung ương`, `CB_NV_TW`, đơn vị `Cục Bổ trợ tư pháp - Bộ Tư pháp` (phạm vi rộng hơn, thấy 16 đề xuất của nhiều đơn vị). **Cả 2 ra cùng kết quả** | Không |
| Dữ liệu tiền đề — đơn vị **phải có ít nhất 1 đề xuất do DN gửi** | *"Đơn vị của cán bộ có ít nhất 1 đề xuất đào tạo do Doanh nghiệp gửi"*; dữ liệu phiếu là 1 đề xuất DN gửi ngày 03/08 | **Tự dựng cho dày hơn phiếu** (Nguyên tắc 4): tạo mới **2 đề xuất từ 2 doanh nghiệp KHÁC NHAU** (`0311224477` – *QA Kiem Chung*; `1234567899` – *Nguyễn QA Test R7*) để loại khả năng cột hiện giá trị cố định. Ngoài ra kho còn **14 đề xuất có sẵn** thuộc 4 đơn vị, gồm **10 đề xuất do doanh nghiệp/người dân gửi từ chuyên trang** và **4 đề xuất do cán bộ tạo trong phần mềm** ⇒ phủ đủ **cả 2 nguồn gửi** | Không |
| Nguồn gửi đề xuất (biến quyết định, bug gốc không tách) | Phiếu nêu chung *"đề xuất của doanh nghiệp / người hỗ trợ"* | Tách hẳn 2 nguồn: **(A) gửi bằng tài khoản trong phần mềm** (6/16 bản ghi) · **(B) gửi từ chuyên trang, người gửi không phải tài khoản trong phần mềm** (10/16 bản ghi, trong đó có **chính đề xuất của đối tác**: *"TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026"*) | Không |
| Trạng thái bản ghi | Phiếu: trạng thái *"Mới gửi"* | Phủ **4 trạng thái** có trong kho: `Mới gửi` · `Đã tiếp nhận` · `Đang xử lý` · `Đã xử lý` — cột trống ở cả 4, nên không thể đổ cho "chỉ hỏng ở một trạng thái" | Không |
| Màn hình + thao tác quan sát | *"Xem danh sách, **cuộn hết thanh ngang** của bảng"* + *"Bấm vào nội dung đề xuất để mở **màn chi tiết**"* | Làm đúng cả 2: đếm cột ở thanh tiêu đề (**9 cột**), **cuộn ngang hết sang phải** (`scrollLeft 272 / scrollWidth 1400 / clientWidth 1136`) rồi chụp; sau đó mở **màn chi tiết** của cả bản ghi có tên lẫn bản ghi trống | Không |

## Kết quả

**Cột đã được thêm thật** — bảng nay có **9 cột**: `Nội dung · Lĩnh vực · Thời gian mong muốn · Địa điểm mong muốn ·
SL dự kiến · **Người đề xuất** · Trạng thái · Ngày tạo · Hành động`. Màn chi tiết cũng có dòng **"Người đề xuất"**.

**Nhưng giá trị chỉ có ở một nửa dữ liệu.** Đếm trên đúng 16 bản ghi mà cán bộ Trung ương nhìn thấy:

- **Gửi bằng tài khoản trong phần mềm** (2 DN mình vừa tạo + 4 do cán bộ tạo) — **6 bản ghi** — ✅ cột hiện
  **họ tên + đơn vị**, đúng từng người (`QA Kiem Chung`, `Nguyễn QA Test R7`, `CB Nghiệp vụ TW 01`).
- **Gửi từ chuyên trang** (người gửi không phải tài khoản trong phần mềm) — **10 bản ghi** — ❌ cột chỉ có
  **`—`** + tên đơn vị; **không có họ tên, không có tên doanh nghiệp**.

Trong 10 bản ghi trống có **chính đề xuất của đối tác**: *"TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026"*
(23/07/2026) và *"TKM đề xuất kiểm thử chức năng"*. Mở **màn chi tiết** bản ghi này
(`/dao-tao/de-xuat/b9e25926-0452-440e-a3e4-df351bd3a615`) → dòng **"Người đề xuất: — · Cục Bổ trợ tư pháp - Bộ Tư pháp"**
⇒ cán bộ **vẫn không biết đề xuất là của doanh nghiệp nào**, đúng như điều phiếu than phiền.

## Đã cố BÁC BỎ chính phát hiện của mình (tránh báo lỗi oan)

1. **Nghi "chỉ là bản ghi cũ tạo trước bản vá"** → **BÁC**: bản ghi **cũ nhất** trong kho (`11/05/2026` và
   `25/05/2026`) lại **hiện đủ tên** `CB Nghiệp vụ TW 01`, trong khi nhóm trống nằm ở `23/06` → `25/07`.
   Ngày tháng **không** phải yếu tố phân biệt — **nguồn gửi** mới là yếu tố phân biệt.
2. **Nghi "do vai trò / phạm vi xem dữ liệu"** → **BÁC**: đo bằng cả `cb_nv_dp_01` (Địa phương) và `cbnv_tw`
   (Trung ương), kết quả giống nhau.
3. **Nghi "chỉ hỏng ở một trạng thái"** → **BÁC**: nhóm trống trải đều `Mới gửi`, `Đã tiếp nhận`, `Đang xử lý`, `Đã xử lý`.
4. **Nghi "cột chỉ hiện được một giá trị cố định"** → **BÁC**: tự tạo 2 đề xuất từ **2 doanh nghiệp khác nhau**,
   bảng hiện **2 tên khác nhau** ⇒ phần chạy được là chạy thật, không phải giá trị cứng.
5. **Nghi "chỉ bảng danh sách thiếu, màn chi tiết vẫn có"** → **BÁC**: màn chi tiết cũng hiện `—`.
6. **Nghi "mình đọc nhầm chữ ẩn"** → **BÁC**: đọc bằng `innerText` (chỉ chữ nhìn thấy) **và** chụp ảnh đối chiếu,
   hai phép đo khớp nhau.

## Vì sao là `Reopen` chứ không phải `Pass`

- Yêu cầu của phiếu là **để cán bộ biết đề xuất là của doanh nghiệp / người hỗ trợ nào**. Đặc tả cũng nói rõ tab này
  *"tiếp nhận đề xuất **từ DN/NHT**"* (`srs-fr-03-dao-tao.md:1898`). Đúng **nhóm đề xuất do DN/NHT gửi từ chuyên trang**
  — tức nhóm chính mà cột này sinh ra để phục vụ — lại là nhóm **không có tên**.
- **10/16 bản ghi** (62,5%) trên màn hình của cán bộ vẫn trống, gồm cả bản ghi của chính đối tác.
- Theo quy tắc **"fix một phần = Reopen"** ⇒ verdict `Reopen`.

**Kết luận: 0 GAP về điều kiện.** Đã tái lập đúng vai trò cán bộ (2 cấp), đúng tiền đề dữ liệu (tự tạo thêm 2 đề xuất
DN), đúng thao tác (cuộn ngang hết + mở chi tiết), phủ đủ 4 trạng thái và **cả 2 nguồn gửi**.
