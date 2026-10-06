# QLLKHDTBD_09 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 119 · Verdict Verify 2: `Pass`
> Bug gốc: màn `Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách`, tab **Tất cả**, đặt **Từ ngày 01/07/2026** +
> **Đến ngày 31/07/2026** rồi bấm **[Xuất Excel]** → màn ghi "Hiển thị 1-1 / 1 kết quả" nhưng **tệp Excel có 13 dòng**
> (toàn bộ danh sách, 12 dòng nằm ngoài khoảng lọc). Đo lại theo chiều lọc thứ hai (từ khoá) cũng ra 13 dòng.
> Bug FILTER — phụ thuộc vai trò + dữ liệu + giá trị lọc ⇒ bắt buộc điền bảng này.
> **Phạm vi case (đã chốt ở vòng 1):** chỉ xét *số bản ghi trong tệp có khớp bộ lọc hay không*; danh sách cột và
> định dạng bên trong tệp KHÔNG thuộc phạm vi.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(bản dựng MỚI; dữ liệu khác vòng trước — kho có 15 kế hoạch, không còn bản ghi `RECON`/`KH-20260803-0003` của vòng trước).

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — Cán bộ Nghiệp vụ Trung ương (`CB_NV_TW`), đơn vị Bộ Tư pháp - Trung ương (`BTP · TW`) | Đăng nhập đúng **`cbnv_tw`** (`Test@1234`) — `vaiTro:["CB_NV_TW"]`, `capDonVi:"TW"`, `donViId: 00000000-0000-4000-8000-000000000001`; thanh trên hiện `Cán bộ NV Trung ương · CB_NV_TW · BTP · TW` | Không |
| Màn hình + tab đang đứng | Màn `/dao-tao/ke-hoach/danh-sach`, tab **Tất cả** | Cùng màn `/dao-tao/ke-hoach/danh-sach`, tab **Tất cả** (badge `Tất cả 15` khi chưa lọc) | Không |
| Dữ liệu tiền đề (phải có bản ghi NẰM NGOÀI khoảng lọc thì phép đo mới phân biệt được) | Kho có 13 kế hoạch, chỉ 1 rơi vào khoảng lọc, 12 nằm ngoài (vd `01/09/2026–31/12/2026`, `01/01/2026–31/12/2026`) | Kho có **15 kế hoạch**: **3** rơi vào khoảng `01/07–31/07/2026`, **12** nằm ngoài (`31/12/2025–30/12/2026`, `01/01–31/12/2026`, `15/05–30/06/2026`, `03/08–27/09/2026`…). Cấu hình dữ liệu tương đương bug gốc (có trong + có ngoài) ⇒ **không cần seed thêm**, phép đo không suy biến | Không |
| Input / filter / giá trị nhập | **Đúng 1 bộ lọc:** từ khoá **trống** · Năm **trống** · **Từ ngày = 01/07/2026** · **Đến ngày = 31/07/2026** · tab Tất cả. Địa chỉ trang `…?tuNgay=2026-07-01&denNgay=2026-07-31&page=1` | **Phép A — trùng khít từng giá trị với bug gốc:** từ khoá trống · Năm trống · **Từ ngày 01/07/2026** · **Đến ngày 31/07/2026** · tab Tất cả → địa chỉ trang ra **đúng chuỗi** `…?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`.<br>**Phép B — chiều lọc KHÁC** (từ khoá `TKM`, ô ngày trống).<br>**Phép C — chiều lọc thứ BA** (tab trạng thái `Nháp`).<br>**Phép D — phân trang** (không lọc, 10/trang) để loại giả thuyết "tệp chỉ là trang đang xem" | Không |
| Cách kích hoạt xuất tệp | Bấm nút **[Xuất Excel]** góc phải tiêu đề màn | Bấm đúng nút **[Xuất Excel]** cùng vị trí; mỗi lần đúng **1 thông báo "Xuất Excel thành công"** (bắt bằng `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`), đúng **1 request ghi** | Không |

## Đo NỘI DUNG tệp, không dừng ở "tải được tệp"

Trình duyệt của bộ công cụ kiểm thử không đổ tệp ra thư mục tải về, nên **bắt thẳng luồng byte của chính tệp mà nút
[Xuất Excel] tạo ra**, ghi ra `.xlsx` rồi mở bằng `openpyxl` để đếm dòng và đọc từng ô:

- **Mốc 0 (đối chứng)** — không lọc, 20/trang: màn **15** → trong tệp **15** ✅
- **Phép A (đúng bộ lọc bug gốc)** — Từ ngày `01/07/2026` + Đến ngày `31/07/2026`: màn **3** → trong tệp **3** ✅
- **Phép B (chiều lọc khác)** — từ khoá `TKM`: màn **2** → trong tệp **2** ✅
- **Phép C (chiều lọc thứ ba)** — tab trạng thái `Nháp`: màn **1** → trong tệp **1** ✅
- **Phép D (phân trang)** — không lọc, **10/trang**, màn chỉ hiện **10/15** → trong tệp **15** ✅ (đúng "theo bộ lọc", không phải "theo trang đang xem")

**Kiểm cả GIÁ TRỊ chứ không chỉ số lượng:**
- Tệp phép A chứa **đúng 3 mã** đang hiện trên màn — `KH-20260725-0003` (25/07–31/07), `KH-20260725-0001` (01/07–31/07), `KH-20260723-0001` (01/07–28/07); **không lẫn** bản ghi nào ngoài khoảng, kể cả `KH-20260725-0002` (01/07–**31/08**) và `KH-20260525-0001` (01/07–**30/09**) là hai bản ghi bắt đầu trong tháng 7 nhưng kết thúc ngoài.
- Tệp phép B chứa đúng 2 bản ghi có chữ `TKM` trong tên.
- Tệp phép C chứa đúng bản ghi trạng thái `Nháp` (`KH-20260509-0003`).

Tệp bằng chứng: `fixtures/QLLKHDTBD_09/v2-00-khong-loc.xlsx`, `v2-01-locA-tungay-denngay.xlsx`,
`v2-02-locB-tukhoa-TKM.xlsx`, `v2-03-locC-tab-Nhap.xlsx`, `v2-04-phantrang-pagesize10.xlsx`.

## Đã cố BÁC BỎ kết luận Pass bằng những cách sau — không bác được

1. **Dùng đúng bộ lọc của bug gốc, không dùng bộ lọc dễ tái hiện** — hai giá trị `01/07/2026` và `31/07/2026`, sinh ra đúng chuỗi tham số trên địa chỉ trang mà bug gốc ghi.
2. **Loại giả thuyết "trùng số ngẫu nhiên"** — đo thêm 2 chiều lọc hoàn toàn khác (từ khoá, trạng thái), cả hai đều khớp.
3. **Loại giả thuyết "tệp chỉ là trang đang xem"** (kiểu fix giả tạo ra Pass giả): đặt 10/trang, màn chỉ hiện 10/15, tệp vẫn ra **đủ 15** ⇒ tệp dựng theo **bộ lọc**, không phải theo trang.
4. **Đọc từng ô, không chỉ đếm dòng** — soi cả 2 bản ghi "bẫy" bắt đầu trong tháng 7 nhưng kết thúc ngoài tháng 7: cả hai đều **không** có trong tệp phép A, đúng như màn.
5. **Đo trường hợp biên 0 kết quả** — lọc từ khoá không tồn tại: màn báo "Không có kế hoạch đào tạo nào phù hợp." và nút **[Xuất Excel] tự vô hiệu hoá**, không sinh tệp rỗng vô nghĩa.
6. **Kiểm thông báo bằng bộ đo chuẩn** — mỗi lần bấm đúng 1 request ghi ↔ 1 thông báo "Xuất Excel thành công", không lặp.

**Kết luận: 0 GAP** — đã tái lập đúng vai trò, đúng màn, đúng cấu hình dữ liệu và **đúng từng giá trị bộ lọc** của bug gốc; đo nội dung tệp ở 5 cấu hình khác nhau đều khớp màn ⇒ `Pass`.
