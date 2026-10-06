# CNDSMLTVV_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 124 · Verdict Verify 2: `Pass`
> **Bug gốc:** chọn nhiều tư vấn viên rồi bấm công khai hàng loạt thì hệ thống **không mở cửa sổ nhập**, mà bắn ngay
> thông báo *"Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia"* ra màn danh sách.
> **Kết quả mong đợi của phiếu:** mở cửa sổ nhập mô tả công khai (bắt buộc) + câu xác nhận *"Công khai {N} tư vấn viên
> đã chọn lên Cổng pháp luật quốc gia?"*; sau khi xác nhận thì **lưu mô tả, đặt cờ công khai, chuyển trạng thái, ghi thời điểm**.
> Chiếu `srs-fr-04-chuyen-gia-tvv.md:1464` (công khai hàng loạt → mở MD-CONG-KHAI) + `:1406` (mẫu MD-CONG-KHAI) + `:656-657`
> (trường `mo_ta_cong_khai` bắt buộc, `file_dinh_kem_cong_khai` tùy chọn) + `:662` (bước xử lý: lưu mô tả, `cong_khai = 1`,
> chuyển CONG_KHAI, auto fill `thoi_gian_dang_tai`).
> Bug phụ thuộc **vai trò + trạng thái entity + tiền đề dữ liệu** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Cán bộ nghiệp vụ"* (phiếu ghi tác nhân TW, BN, ĐP); lần đo trước dùng `cbnv_tw_02` — Cán bộ Nghiệp vụ Trung ương, đơn vị Cục Bổ trợ tư pháp | **`cbnv_tw`** — `Cán bộ NV Trung ương`, vai trò `CB_NV_TW`, `capDonVi TW`, `donViId 00000000-0000-4000-8000-000000000001`, thanh trên hiện `BTP · TW`. `cbnv_tw_02` **không tồn tại** trên môi trường này (máy chủ trả "Tên đăng nhập hoặc mật khẩu không đúng") nên dùng tài khoản gốc **cùng vai trò + cùng cấp + cùng đơn vị** đúng Rule 7. Không dùng `admin` ra verdict | Không |
| Cấp đơn vị của cán bộ (đã thử mở rộng sang **Bộ ngành** theo yêu cầu) | Phiếu cho phép cả cấp **BN** | Đã đăng nhập **`cbnv_bn`** (`CB_NV_BN`, `capDonVi BN`, đơn vị Bộ Kế hoạch và Đầu tư): danh sách Tư vấn viên **rỗng ở cả 10 tab** — *"Chưa có tư vấn viên nào trong mục này"* (ảnh `LO-D-v2-00-tai-khoan-bo-nganh-cbnv_bn-thay-0-tu-van-vien.png`). Đơn vị bộ ngành **không có hồ sơ nào** để chọn công khai, và cũng **không có tài khoản Người hỗ trợ của Cục Bổ trợ tư pháp** để dựng hồ sơ sang đơn vị đó ⇒ chỉ cấp TW quan sát được thao tác. Đây là **giới hạn dữ liệu của môi trường**, không phải điều kiện bị bỏ sót: cấp TW đúng bằng cấp mà lần đo phát hiện lỗi đã dùng | Không |
| Entity + **trạng thái** (state machine) | Hồ sơ ở tab **"Đang hoạt động"** | 2 hồ sơ **`TVV-BTP-TW-0063`** (*Tester TKM BTP-TW*) và **`TVV-BTP-TW-0034`** (*TVV R12 A18 UI Walk*), cột Trạng thái = **"Đang hoạt động"**, đọc trực tiếp trên bảng trước khi tích chọn | Không |
| Dữ liệu tiền đề | Điều kiện phiếu: hồ sơ *"Đang hoạt động" và **chưa được công khai*** | Cả 2 hồ sơ có cột Công khai = **"Chưa công khai"** tại thời điểm tích chọn (ảnh `CNDSMLTVV_01-v2-01`). Kho có sẵn 11 hồ sơ Đang hoạt động (8 chưa công khai) nên **không phải seed** | Không |
| Input / lối vào thao tác | *"Tích chọn các ứng viên hợp lệ → nhấn Công khai hàng loạt và Xác nhận"* | Tích **2 dòng** (thanh hiện *"Đã chọn 2 mục"*) → bấm **"Công khai lên Cổng PLQG"** trên thanh thao tác hàng loạt của màn danh sách `/chuyen-gia-tvv/danh-sach` → nhập mô tả → bấm **"Công khai"** (chạy **hết** luồng, không dừng ở chỗ hộp thoại mở) | Không |

## Kết quả đo

**1. Hộp thoại có mở thật, không phải bắn thông báo như lỗi cũ.** Quan sát tại **7 mốc thời gian** sau khi bấm
(50 / 150 / 300 / 600 / 1000 / 1500 / 2200 mili-giây): **cả 7 mốc đều có hộp thoại**, và tại mọi mốc **0 lệnh gửi đi ·
0 thông báo** — tức hệ thống dừng lại chờ người dùng nhập, đúng như phiếu yêu cầu.

**2. Nội dung hộp thoại khớp mẫu đặc tả.** Tiêu đề *"Công khai hàng loạt lên Cổng PLQG"*; câu xác nhận
*"**Công khai 2 tư vấn viên đã chọn lên Cổng pháp luật quốc gia?**"* (đúng số lượng đã chọn); ô *"Mô tả công khai"*
gắn dấu bắt buộc, đếm ký tự `0 / 5000`; có vùng *"Tệp đính kèm (tùy chọn)"*; có câu cảnh báo về việc Cổng tự kéo dữ liệu.

**3. Chạy hết luồng — dữ liệu đổi đúng.** Nhập mô tả 83 ký tự → bấm "Công khai":
**1 lệnh** (`POST /api/v1/tu-van-viens/batch-cong-khai`) — **1 thông báo** (*"Đã công khai tư vấn viên thành công"*),
`BI_LAP = false`. Bộ bắt thông báo đã tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.

**4. Trạng thái + dữ liệu lưu đúng.** Bảng sau thao tác: `TVV-BTP-TW-0063` và `TVV-BTP-TW-0034` chuyển
**"Chưa công khai" → "Công khai"**; **9 hồ sơ không chọn giữ nguyên** trạng thái cũ. Mở màn chi tiết `TVV-BTP-TW-0063`
(`/chuyen-gia-tvv/789d5f7e-ecf2-44d1-92e0-e3bfe1805a3a`) → mục **"Thông tin công khai"**: *Mô tả công khai* = đúng
nguyên văn chuỗi vừa nhập, *Thời gian đăng tải* = **04/08/2026**, header xuất hiện nút **"Hủy công khai"**.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "hộp thoại chỉ chớp hiện rồi hệ thống vẫn tự gửi lệnh"** → **BÁC**: đo 7 mốc trong 2,2 giây, mốc sớm nhất
   (50 ms) đã có hộp thoại và **0 lệnh**; lệnh duy nhất chỉ xuất hiện **sau khi** bấm nút xác nhận trong hộp thoại.
2. **Nghi "thông báo lỗi cũ vẫn bắn ra ngoài, chỉ bị hộp thoại che"** → **BÁC**: bộ bắt thông báo (không lọc trùng,
   đọc `innerText`) ghi **0 khung thông báo** trong suốt 2,2 giây kể từ lúc bấm.
3. **Nghi "mở được hộp thoại nhưng lưu hỏng"** (fix mặt tiền, phần lưu vẫn lỗi) → **BÁC**: chạy tới cùng, trạng thái
   2 hồ sơ đổi đúng và mô tả công khai đọc lại được ở màn chi tiết.
4. **Nghi "áp nhầm cho cả danh sách chứ không chỉ dòng đã chọn"** → **BÁC**: 9 hồ sơ còn lại giữ nguyên "Chưa công khai".
5. **Nghi "gửi 2 lệnh / hiện 2 thông báo"** → **BÁC**: đúng **1 lệnh — 1 thông báo**.
6. **Nghi "chỉ đúng ở cấp Trung ương"** → **không bác được bằng thực nghiệm** vì đơn vị bộ ngành không có hồ sơ nào
   (đã ghi ở dòng "Cấp đơn vị" phía trên) — nhưng đây là giới hạn dữ liệu, **không** phải dấu hiệu lỗi còn tồn tại.

**Kết luận: 0 GAP** — đúng vai trò, đúng trạng thái entity, đúng tiền đề "Đang hoạt động + chưa công khai", đúng lối vào
hàng loạt, và đã chạy **trọn** thao tác tới lúc dữ liệu đổi.
