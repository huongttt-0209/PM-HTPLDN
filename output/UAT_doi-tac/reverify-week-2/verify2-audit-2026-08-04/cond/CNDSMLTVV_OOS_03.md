# CNDSMLTVV_OOS_03 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 143 · Verdict Verify 2: `Pass`
> **Bug gốc:** bỏ trống *"Mô tả công khai"* rồi bấm công khai thì hệ thống **hiện 2 dòng báo lỗi cùng nghĩa** xếp chồng
> dưới cùng một ô nhập — *"Vui lòng nhập mô tả công khai"* và *"Mô tả công khai không được để trống"* (mỗi dòng 592×22
> điểm ảnh, đã loại trừ chữ ẩn cho trình đọc màn hình). Ngoài việc lặp, **cả 2 câu đều không đúng nội dung đặc tả**.
> **Kết quả mong đợi:** báo **đúng một lần**, dùng đúng mã lỗi duy nhất mà đặc tả quy định cho tình huống này —
> `srs-fr-04-chuyen-gia-tvv.md:682`: *"E2 | Thiếu mô tả công khai khi CONG_KHAI | **ERR-CK-02** | **"Mô tả công khai là
> bắt buộc trước khi công khai lên Cổng pháp luật quốc gia"** | ERROR"* (đối chiếu thêm `:656` — `mo_ta_cong_khai` bắt
> buộc khi CONG_KHAI).
> Bug phụ thuộc **vai trò + trạng thái entity + thao tác thật trên hộp thoại** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền
> bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp"*; lần đo trước dùng `cbnv_tw_02` | **`cbnv_tw`** — `CB_NV_TW`, `capDonVi TW`, `donViId 00000000-0000-4000-8000-000000000001`, thanh trên hiện `BTP · TW`. `cbnv_tw_02` **không tồn tại** trên môi trường này nên dùng tài khoản gốc cùng vai trò + cùng cấp + cùng đơn vị (Rule 7). Đã thử thêm **`cbnv_bn`** (bộ ngành) theo yêu cầu: đơn vị đó **0 hồ sơ tư vấn viên** nên không mở được hộp thoại — ảnh `LO-D-v2-00-tai-khoan-bo-nganh-cbnv_bn-thay-0-tu-van-vien.png` | Không |
| Entity + **trạng thái** | *"Đang mở hộp thoại công khai của một hồ sơ tư vấn viên"*; hồ sơ phiếu dùng là `TVV-SEED-0001` | Môi trường này **không có** `TVV-SEED-0001` ⇒ **tự dựng tiền đề tương đương**, và dựng ở **2 hồ sơ khác nhau** để loại yếu tố hồ sơ: **`TVV-MOCK-999`** (*Chuyên gia Nguyễn Văn A*, Đang hoạt động – Chưa công khai) cho hộp thoại hàng loạt và **`TVV-BTP-TW-0032`** (*TVV R11 Verify Mail Fix*) cho hộp thoại màn chi tiết | Không |
| Lối vào mở hộp thoại | *"Tích chọn 1 dòng, bấm 'Công khai lên Cổng PLQG' để mở hộp thoại"* (thanh thao tác hàng loạt) | Đúng lối vào đó, **và mở rộng thêm** hộp thoại ở **màn chi tiết** để loại khả năng "chỉ sửa một chỗ" | Không |
| Dữ liệu nhập | *"Ô 'Mô tả công khai' để trống (0 / 5000 ký tự)"* | Đúng ô trống (0/5000), **và phủ thêm 3 biến thể** dễ làm lộ nhánh kiểm tra còn sót: bấm **2 lần liên tiếp** · **gõ 1 ký tự rồi xóa** (kích hoạt kiểm tra khi thay đổi) · nhập **toàn dấu cách** (5/5000) | Không |
| Cách quan sát | *"Đếm số dòng báo lỗi hiện ra dưới ô nhập"* + *"kiểm cả 2 dòng đều thực sự hiển thị, không phải chữ ẩn cho trình đọc màn hình"* (bug gốc đo 592×22 mỗi dòng) | Lặp đúng phép đo đó, chặt hơn: đếm **phần tử lá** `.ant-form-item-explain-error` (tránh đếm trùng vỏ + ruột) · quét **mọi chữ màu đỏ hiển hình** trong hộp thoại (bắt cả dòng lỗi không dùng lớp giao diện chuẩn) · đo **kích thước + tọa độ** từng dòng · đếm **khung thông báo nổi** bằng `tools/toast-capture.js` (không lọc trùng, đọc `innerText`) · đếm **số lệnh gửi đi** | Không |

## Kết quả đo

**Cả 4 kịch bản đều ra đúng 1 dòng báo lỗi, cùng nội dung, cùng vị trí — mọi kịch bản đều 0 lệnh gửi đi, 0 thông báo
nổi, hộp thoại vẫn mở:**

- **A. Ô trống, bấm lần 1** → **1** dòng: *"Mô tả công khai là bắt buộc trước khi công khai lên Cổng pháp luật quốc gia"*.
- **B. Bấm tiếp lần 2** → vẫn **1** dòng, y hệt câu trên (không dồn thêm dòng).
- **C. Gõ 1 ký tự (lỗi biến mất, 0 dòng) rồi xóa** → **1** dòng, y hệt câu trên.
- **D. Nhập 5 dấu cách rồi bấm** → **1** dòng, y hệt câu trên.

Mỗi lần đo, dòng lỗi chiếm **592×22** điểm ảnh tại **cùng tọa độ (420, 437)**; quét toàn bộ chữ đỏ trong hộp thoại cũng
ra **đúng 1** phần tử (`rgb(245, 34, 45)`). Bộ bắt thông báo tự kiểm `soObserverDangSong = 1` trước mỗi phép đếm.

**Nội dung đúng nguyên văn đặc tả.** Câu hiện ra khớp **100%** chuỗi ERR-CK-02 ở `:682`. Hai câu sai của bug gốc
(*"Vui lòng nhập mô tả công khai"*, *"Mô tả công khai không được để trống"*) **không còn xuất hiện** trong bất kỳ kịch
bản nào. Ảnh: `CNDSMLTVV_OOS_03-v2-01` (hộp thoại hàng loạt).

**Chặn vẫn đúng.** Cả 4 kịch bản: **0 lệnh gửi ra máy chủ**, hộp thoại vẫn mở ⇒ sửa phần thông báo nhưng **không làm
hỏng phần chặn**. Riêng kịch bản D cho thấy chuỗi toàn dấu cách cũng bị coi là thiếu mô tả — đúng tinh thần `:656`.

**Hộp thoại ở màn chi tiết cũng 1 dòng.** Đo trên `TVV-BTP-TW-0032`: 1 dòng, cùng câu, 0 khung thông báo nổi, hộp thoại
vẫn mở — ảnh `CNDSMLTVV_OOS_03-v2-02`.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "vẫn 2 dòng nhưng xếp chồng khít nên nhìn tưởng 1"** → **BÁC**: đếm bằng **phần tử lá** (một phép đếm thô ban
   đầu ra "2" chính là do đếm cả vỏ `.ant-form-item-explain` lẫn ruột `.ant-form-item-explain-error` — đã loại) và quét
   **mọi chữ đỏ** trong hộp thoại, cả hai đều ra **1**.
2. **Nghi "dòng thứ 2 bị dời thành thông báo nổi"** (giấu chứ không bỏ) → **BÁC**: bộ bắt thông báo **không lọc trùng**
   ghi **0 khung** suốt 1,6 giây sau mỗi lần bấm, ở cả 4 kịch bản.
3. **Nghi "bấm nhiều lần thì dồn thêm dòng"** → **BÁC**: bấm lần 2 vẫn đúng 1 dòng.
4. **Nghi "nhánh kiểm tra khi gõ/xóa sinh câu khác"** → **BÁC**: gõ 1 ký tự (lỗi biến mất) rồi xóa → quay lại **đúng 1
   dòng, đúng câu đó**.
5. **Nghi "chuỗi toàn dấu cách đi nhánh khác"** → **BÁC**: vẫn bị chặn, vẫn 1 dòng, vẫn đúng câu.
6. **Nghi "chỉ sửa ở hộp thoại hàng loạt, màn chi tiết vẫn 2 dòng"** → **BÁC**: đo ở màn chi tiết cũng 1 dòng.
7. **Nghi "đủ 1 dòng nhưng câu chữ vẫn sai đặc tả"** (bug gốc phàn nàn **cả** số lượng lẫn nội dung) → **BÁC**: đối chiếu
   nguyên văn với `:682`, khớp từng chữ.
8. **Nghi "sửa thông báo nhưng làm hỏng phần chặn"** → **BÁC**: 0 lệnh gửi đi trong cả 4 kịch bản, hộp thoại không đóng.

**Kết luận: 0 GAP** — đúng vai trò, đúng trạng thái entity, đúng lối vào và dữ liệu nhập của phiếu, đúng phép đo loại
trừ chữ ẩn mà bug gốc đã dùng, phủ thêm 3 biến thể nhập và 2 lối vào để không bỏ sót nhánh còn lỗi.
