# CNDSMLTVV_OOS_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 140 · Verdict Verify 2: `Pass`
> **Bug gốc:** *"Hủy công khai hàng loạt"* **không hỏi lại** — bấm nút là hệ thống gỡ ngay. Đo 7 mốc trong 2,2 giây đều
> không có hộp thoại; **ngay mốc 50 mili-giây lệnh gỡ công khai đã được gửi**; tái hiện 3/3 lần.
> **Kết quả mong đợi:** phải hỏi lại trước khi gỡ khỏi Cổng pháp luật quốc gia —
> `srs-fr-04-chuyen-gia-tvv.md:1465` (*"Hủy công khai hàng loạt (tab Đang hoạt động): chọn dòng đã công khai → nút
> 'Hủy công khai' → **MD-HUY-CONG-KHAI**"*) + mẫu MD-HUY-CONG-KHAI ở `:1407` (tiêu đề *"Xác nhận hủy công khai?"*,
> nút chính *"Hủy công khai"*) + `:663` (bước xử lý: `cong_khai = 0`, chuyển HUY_CONG_KHAI).
> Bug phụ thuộc **vai trò + trạng thái entity (phải đang Công khai)** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | *"Cán bộ nghiệp vụ cấp Trung ương, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp"*; lần đo trước dùng `cbnv_tw_02` | **`cbnv_tw`** — `CB_NV_TW`, `capDonVi TW`, `donViId 00000000-0000-4000-8000-000000000001`, thanh trên hiện `BTP · TW`. `cbnv_tw_02` **không tồn tại** trên môi trường này nên dùng tài khoản gốc cùng vai trò + cùng cấp + cùng đơn vị (Rule 7). Đã thử thêm **`cbnv_bn`** (bộ ngành): đơn vị đó **0 hồ sơ tư vấn viên** nên không quan sát được thao tác — xem ảnh `LO-D-v2-00-tai-khoan-bo-nganh-cbnv_bn-thay-0-tu-van-vien.png` | Không |
| Entity + **trạng thái** (state machine) | Ở tab *"Đang hoạt động"* có **ít nhất 1 hồ sơ đang ở trạng thái Công khai**; bug gốc dùng hồ sơ vừa được công khai bằng chính luồng hàng loạt | **`TVV-BTP-TW-0063`** (*Tester TKM BTP-TW*), Trạng thái *"Đang hoạt động"*, cột Công khai = **"Công khai"** — và đúng như bug gốc, hồ sơ này **vừa được công khai bằng chính luồng công khai hàng loạt** ngay trước đó trong cùng phiên (mô tả *"QA soat lai 2 - 04/08/2026…"*), không phải dữ liệu cũ | Không |
| Dữ liệu tiền đề | Hồ sơ TVV-SEED-0001 (môi trường cũ) | Môi trường này **không có** TVV-SEED-0001; đã **tự dựng tiền đề tương đương** thay vì để trống: công khai `TVV-BTP-TW-0063` qua luồng hàng loạt rồi mới đo hủy công khai | Không |
| Input / lối vào thao tác | *"Tích chọn 1 dòng đang Công khai → bấm nút 'Hủy công khai' trên **thanh thao tác hàng loạt**"* | Đúng lối vào đó: tích 1 dòng ở tab "Đang hoạt động" → bấm **"Hủy công khai"** trên thanh thao tác hàng loạt của `/chuyen-gia-tvv/danh-sach` | Không |
| Cách quan sát | *"Quan sát liên tục trong 2,2 giây kể từ lúc bấm"* (7 mốc: 50/150/300/600/1000/1500/2200 ms) + đọc trạng thái dòng sau thao tác | Lặp **đúng 7 mốc thời gian đó**, cùng lúc đếm số lệnh gửi đi và số khung thông báo tại từng mốc; sau đó **chạy tiếp tới cùng** (xác nhận thật) và đọc lại trạng thái dòng | Không |

## Kết quả đo

**1. Đã có bước hỏi lại — và nó chặn thật.** Cả **7/7 mốc** trong 2,2 giây đều **có hộp thoại**, và tại **mọi mốc**:
**0 lệnh gửi đi · 0 thông báo**. Đây đúng là điểm đã hỏng trước đây (mốc 50 ms lệnh đã bay đi) — nay không còn.

**2. Hộp thoại đúng mẫu đặc tả.** Tiêu đề **"Xác nhận hủy công khai?"** (khớp `:1407`); nội dung
*"1 tư vấn viên đã chọn sẽ bị gỡ khỏi Cổng pháp luật quốc gia. Bạn có thể công khai lại bất kỳ lúc nào."*;
2 nút **"Hủy bỏ"** / **"Hủy công khai"** (nút chính đúng tên đặc tả). Ảnh pixel: `CNDSMLTVV_OOS_01-v2-01`.

**3. Phép thử quyết định — nhánh "Hủy bỏ".** Bấm **"Hủy bỏ"**: **0 lệnh · 0 thông báo**, hộp thoại đóng, dòng
**giữ nguyên "Công khai"**. Chứng minh hộp thoại là **cổng chặn thật**, không phải lớp trang trí hiện sau khi lệnh đã gửi.

**4. Nhánh xác nhận — chạy tới cùng.** Mở lại hộp thoại rồi bấm **"Hủy công khai"**: **1 lệnh**
(`POST /api/v1/tu-van-viens/batch-cong-khai`) — **1 thông báo** (*"Đã hủy công khai tư vấn viên thành công"*),
`BI_LAP = false`. Bảng sau thao tác: `TVV-BTP-TW-0063` chuyển **"Công khai" → "Chưa công khai"**
(ảnh `CNDSMLTVV_OOS_01-v2-03`), các hồ sơ không chọn giữ nguyên. Bộ bắt thông báo tự kiểm `soObserverDangSong = 1`.

## Đã cố BÁC BỎ kết luận `Pass` bằng những cách nào

1. **Nghi "hộp thoại chỉ là hiệu ứng, lệnh vẫn bay đi ngay như cũ"** → **BÁC** bằng phép thử nhánh **"Hủy bỏ"**:
   0 lệnh và trạng thái **không đổi**. Nếu hệ thống vẫn gỡ trước rồi mới hỏi thì dòng đã phải chuyển "Chưa công khai".
2. **Nghi "chỉ mở hộp thoại ở một số mốc thời gian"** (đo trúng lúc may) → **BÁC**: đo lại **đúng 7 mốc** của lần phát hiện
   lỗi, cả 7 đều có.
3. **Nghi "dữ liệu cũ nên hành vi khác"** → **BÁC**: hồ sơ đem đo được **tạo trạng thái Công khai ngay trong phiên này**
   bằng chính luồng hàng loạt, giống hệt cách bug gốc dựng dữ liệu.
4. **Nghi "xác nhận xong lại không gỡ thật"** (fix phần hỏi, hỏng phần làm) → **BÁC**: 1 lệnh — 1 thông báo và cột
   Công khai đổi đúng.
5. **Nghi "gửi 2 lệnh / hiện 2 thông báo"** → **BÁC**: đúng 1 — 1.

**Đã cân nhắc, KHÔNG tính là lỗi:** mẫu ở `:1407` viết *"Thông tin **{tên}** sẽ bị gỡ…"*, còn hộp thoại hàng loạt hiển thị
*"**1 tư vấn viên đã chọn** sẽ bị gỡ…"*. Với thao tác **hàng loạt** (N hồ sơ) thì chỗ `{tên}` không áp được nguyên văn;
yêu cầu nghiệp vụ của phiếu là **phải hỏi lại trước khi gỡ**, và điều đó đã được đáp ứng.

**Kết luận: 0 GAP** — đúng vai trò, đúng trạng thái entity (đang Công khai), đúng lối vào hàng loạt, đúng cách quan sát
7 mốc của bug gốc, và đã chạy trọn **cả hai nhánh** (hủy bỏ + xác nhận).
