# Tiêu chí verify — LKHDG_12

Mã case: **LKHDG_12** (dòng 126, tab `bug`)  ·  Thời điểm viết: **2026-08-06 00:13**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: **HTPLDN · V1.0.8** (chuỗi phiên bản chân
thanh điều hướng) · gói mã `assets/index-DThrFe1_.js` · đo lúc **2026-08-06 00:17–00:32** · khung nhìn 1440×741

> Viết TRƯỚC khi mở màn "Đánh giá hiệu quả" trên env verify. Nguồn duy nhất lúc viết: dòng bảng đối tác,
> video `LKHDG_12.webm` (đã trích frame + đọc), và đặc tả SRS v3.5.
> **Khai báo minh bạch:** trước khi viết mục 4 tôi có đọc `reverify-week-3/reverify-audit/LKHDG_12/note.txt`
> (ghi chép QA đợt trước, bản dựng CŨ). Ghi chép đó chỉ dùng để biết case từng được đo thế nào; mục 4 dưới đây
> suy ra từ **BR-DATA-06 + SCR-VI-01**, không lấy kết quả đo cũ làm tiêu chí.

---

## 1. Đối tác phản ánh — tách 3 vế

| Vế | Nội dung đối tác ghi | Ghi chú |
|---|---|---|
| **a** | "Hệ thống xuất danh sách **không đúng với tiêu chí lọc**" | Vế duy nhất đối tác **retest lại ngày 30/07** và vẫn ghi Fail (cột "TKM phản hồi lần 1") |
| **b** | "File excel xuất ra **thiếu cột** thông tin *Số vụ việc*, *Người tạo*, *Ngày tạo*" | |
| **c** | "Thông tin các cột: *Tần suất*, *Đối tượng*, *Trạng thái* hiển thị **không dấu**" | Thực chất là ghi **mã enum thô** (`TRON_NAM`, `VU_VIEC`, `LAP_KE_HOACH`) — thấy rõ ở frame t018 |

**Bằng chứng đã mở xem:** `partner-evidence/LKHDG_12.webm` (7.695.544 bytes, 21s) → trích 8 frame vào
`frames/LKHDG_12/`. Đã đọc full-res tới khoảnh khắc lỗi:
- `t009.06s.jpg` — màn danh sách **sau khi đã lọc**, URL `…/danh-gia/ke-hoach/danh-sach?tanSuat=TRON_NAM&page=1`,
  dropdown Tần suất = "Trọn năm", chân bảng ghi **"Hiển thị 1-4 / 4 kết quả"**, cả 4 dòng đều Tần suất "Trọn năm".
  Bảng trên màn **có** các cột "Số vụ việc", "Người tạo".
- `t018.13s.jpg` — tệp vừa tải mở trong Excel: `ke-hoach-danh-gia-1783739630247.xlsx`, sheet "Ke hoach danh gia",
  **7 cột** (Mã KH · Tên đợt · Tần suất · Đối tượng · Từ ngày · Đến ngày · Trạng thái), **14 dòng dữ liệu**
  (hàng 2→15) trong đó có cả `SO_BO_6_THANG` — tức tệp **không áp bộ lọc `TRON_NAM`** đang bật trên màn.
  Ô G2 = `LAP_KE_HOACH` (mã thô), cột C/D cũng mã thô.

## 2. Đặc tả nói gì

- **BR-DATA-06 (quy tắc nền, `srs-v3.5.md:5525`)** — *"**Export Excel:** Mọi danh sách có tính năng xuất Excel.
  **File xuất theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"*. Cột "Áp dụng" = **"Toàn bộ CRUD list"**;
  cột "Ngoại lệ" chỉ nêu *"Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025"* — **không** miễn trừ nhóm VI.
  Bản nhắc lại trong nhóm: `srs-fr-11-bao-cao.md:1276-1280`.
- **SCR-VI-01 Phần A (`srs-fr-08-danh-gia.md:821`)** — thanh tiêu đề có nút **[Xuất Excel]**, hành vi ghi
  *"click → tương ứng"*. Đây là chỗ duy nhất trong cả nhóm VI nhắc tới xuất Excel của màn danh sách.
- Cột bảng danh sách trên màn (`:829-837`): #10 Mã đợt · #11 Tên đợt · #12 Tần suất
  (*`SO_BO_6_THANG` → "Sơ bộ 6 tháng"*, *`TRON_NAM` → "Tròn năm"*) · #13 Đối tượng (đặc tả ghi thẳng
  *"VU_VIEC / DAO_TAO / TONG_HOP"*) · #14 Kỳ đánh giá · #15 Trạng thái (badge nhãn theo SM-DANHGIA) ·
  #16 Người tạo · #17 Ngày tạo · #18 Hành động. **Không có cột "Số vụ việc"** trong đặc tả.

**IM LẶNG về:**
- **Tập cột của TỆP xuất.** Cả nhóm VI không có FR nào đặc tả luồng xuất Excel danh sách đợt (FR-VI-01…10 —
  `srs-fr-08-danh-gia.md:84-805` — không FR nào về xuất). BR-DATA-06 chỉ ràng buộc *bộ lọc* + *số dòng*, không
  nói tệp phải có những cột nào. ⇒ **không có căn cứ nào bắt tệp phải mang đủ cột của bảng trên màn.**
- **Định dạng nhãn trong TỆP xuất.** Bảng nhãn ở `:829-837` là đặc tả **màn hình**, không phải tệp.
  `srs-v3.5.md:518` (C-05 Ngôn ngữ — *"**Giao diện** tiếng Việt, Unicode UTF-8"*) và `:4658` (I18N-07, mức
  🟡 *Đề xuất*) đều nói về **giao diện**, không nói tệp xuất. Riêng cột **Đối tượng**, đặc tả màn hình `:830`
  còn ghi thẳng mã thô `VU_VIEC / DAO_TAO / TONG_HOP` — tức chính đặc tả cũng không đòi nhãn có dấu ở cột này.
- **"Số vụ việc"** hoàn toàn không có trong đặc tả màn hình lẫn tệp.

## 3. Precondition

- Tài khoản: **`cbnv_tw`** (CB Nghiệp vụ Trung ương — đúng vai trò đối tác dùng trong video, xem mục 6).
  Mật khẩu `Test@1234` (`output/UAT_doi-tac/input/input.md`). Không dùng `admin` để ra verdict.
- Màn: **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**, URL `/danh-gia/ke-hoach/danh-sach`.
- Dữ liệu tiền đề: danh sách phải có **≥2 giá trị khác nhau ở mỗi cột lọc** dùng để đo (Tần suất, Trạng thái),
  và tổng số đợt `n_tổng` phải **lớn hơn** số đợt sau khi lọc `n_lọc` — nếu không, phép đo vô nghĩa
  (lọc không cắt bớt gì thì tệp đúng-hay-sai đều ra cùng kết quả). Thiếu → **seed thêm đợt** (khai ở báo cáo).

## 4. Tiêu chí chấm

### Vế (a) — bộ lọc: CHẤM ĐƯỢC

**✅ PASS khi** — thoả **cả 4** ý, đo trên **≥2 bộ lọc khác cột nhau**:
1. Chọn bộ lọc F trên màn sao cho chân bảng báo `n_lọc` **<** `n_tổng` (số kết quả khi không lọc).
2. Bấm **[Xuất Excel]** → mở tệp, đếm **số dòng dữ liệu** (không kể dòng tiêu đề) = **đúng `n_lọc`**.
3. **Tập mã đợt** trong tệp **trùng khít** tập mã đang hiện trên màn sau lọc — so **từng mã một**, không chỉ so
   số lượng (2 tập cùng số lượng vẫn có thể khác phần tử).
4. Lặp lại ý 1-3 với bộ lọc thứ hai ở **cột lọc khác** (vd lần 1 lọc Tần suất, lần 2 lọc Trạng thái) — **cả hai
   lần đều thoả**.

**❌ FAIL nếu** — bất kỳ điều nào: tệp chứa ≥1 mã đợt **không** thuộc tập đang hiện sau lọc · số dòng dữ liệu
**≠** `n_lọc` · tệp trả về toàn bộ danh sách như khi không lọc.

### Vế (b) và (c) — KHÔNG CHẤM, chỉ ghi nhận hiện trạng → đưa BA

**KHÔNG được chấm Fail vì:**
- Tệp xuất thiếu cột *Số vụ việc* / *Người tạo* / *Ngày tạo* → **đặc tả im lặng** về tập cột của tệp xuất
  (mục 2). Đòi tệp phải sao đúng cột của bảng là **QA tự đặt luật**.
- Các cột *Tần suất* / *Đối tượng* / *Trạng thái* trong tệp ghi mã enum thô → **đặc tả im lặng** về định dạng
  nhãn trong tệp; riêng *Đối tượng* thì đặc tả màn hình còn ghi chính mã thô đó.

Với 2 vế này: **đo và chụp ảnh hiện trạng, ghi vào file gửi BA, không kết luận đúng/sai.**

**Phép thử mục 4:** người chưa biết bug này, chỉ đọc mục 4, có chấm được PASS/FAIL không? → Có: mở màn, lọc,
đếm 2 con số, so 2 tập mã.

## 5. Dạng dữ liệu phải phủ — M = 5

1. Đợt có **Tần suất = Sơ bộ 6 tháng** (`SO_BO_6_THANG`)
2. Đợt có **Tần suất = Trọn năm** (`TRON_NAM`)
3. Đợt có **Đối tượng = Vụ việc** (`VU_VIEC`)
4. Đợt có **Đối tượng = Đào tạo hoặc Tổng hợp** (`DAO_TAO` / `TONG_HOP`)
5. **≥2 giá trị Trạng thái khác nhau** (vd `LAP_KE_HOACH` + `HOAN_THANH`)

**Nguồn xác định M:** cách ② của §Xác định M — **bộ lọc + giá trị enum ngay trên màn**: SCR-VI-01 #4 (lọc Tần
suất: 2 giá trị), #5 (lọc Đối tượng: 3 giá trị), #6 (lọc Trạng thái: 8 giá trị) — `srs-fr-08-danh-gia.md:823-825`.
Không dùng cách ① vì nhóm VI không có FR nào nói về nguồn dữ liệu của tệp xuất.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — "Cán bộ NV Trung ương", đơn vị `BTP · TW` (t009) | **`cbnv_tw`** — CB_NV_TW, `BTP · TW`. **Trùng vai trò + trùng cấp** | Không |
| Entity + trạng thái | 4 đợt Trọn năm trên màn: `DG-20260711-0001` (Lập kế hoạch) · `KHDG-HDSD-AG-001` (Lập kế hoạch) · `KHDG-HDSD-AG-002` (Đang đánh giá) · `KHDG-HDSD-AG-003` (Hoàn thành). Tệp xuất 14 dòng, phủ thêm `THUC_HIEN`, `CHO_DUYET_PC`, `DANG_DANH_GIA` | 20 đợt, phủ **7 trạng thái**: Lập kế hoạch 2 · Đang đánh giá 4 · Thực hiện 5 · Hủy 2 · Đã đánh giá 1 · Chờ phê duyệt 2 · Hoàn thành 4. Bản ghi đối tác không có trên env này (env khác) → dùng bản ghi tương đương cùng phân bố trạng thái | Không |
| Dữ liệu tiền đề | `n_tổng` ≥ 14 đợt; `n_lọc` = 4 khi lọc `tanSuat=TRON_NAM` | `n_tổng` = **20**; `n_lọc` = **19** (lọc Tần suất) và `n_lọc` = **4** (lọc Trạng thái). **Đã seed 1 đợt** `DG-20260806-0001` vì cả 19 đợt sẵn có đều `TRON_NAM` → lọc của đối tác không cắt được gì (xem §Dữ liệu đã seed trong báo cáo) | Không |
| Input / filter / giá trị nhập | Lọc **Tần suất = "Trọn năm"** qua dropdown → URL `?tanSuat=TRON_NAM&page=1`. Tab đang mở = "Tất cả". Không nhập từ khoá, không lọc ngày | Lần 1: **Tần suất = "Tròn năm"** → URL `?tanSuat=TRON_NAM&page=1` (**trùng khít URL đối tác**). Lần 2: **Trạng thái = "Hoàn thành"** → `?trangThai=HOAN_THANH&page=1` (cột lọc khác, theo tiêu chí mục 4 ý 4) | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 14 dòng trong tệp / 4 dòng trên màn; M ≥ 5 (đủ 2 Tần suất, 3 Đối tượng, 5 Trạng thái) | N = **20 dòng trong tệp** / 19 và 4 dòng trên màn. M = **5/5**: Sơ bộ 6 tháng ✓(seed) · Tròn năm ✓ · Vụ việc ✓ · Đào tạo ✓(seed) + Tổng hợp ✓ · 7 trạng thái ✓ | Không |

**GAP còn lại: 0.** Lệch env + bản dựng so với đối tác đã ghi rõ ở cuối mục 6 — đó là giới hạn hiệu lực của
verdict, không phải GAP điều kiện chưa đóng.

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** `https://htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/danh-sach?tanSuat=TRON_NAM&page=1`;
  tệp xuất `ke-hoach-danh-gia-1783739630247.xlsx`
- **Trạng thái entity:** 14 đợt trải 5 trạng thái (LAP_KE_HOACH / THUC_HIEN / DANG_DANH_GIA / CHO_DUYET_PC / HOAN_THANH)
- **Vai trò + bản dựng:** CB_NV_TW · **HTPLDN · V1.0** (chân sidebar t009) · env **`htpldn-uat.ospgroup.vn`** ·
  2026-07-11 10:13-10:14

> ⚠️ **Lệch env + bản dựng:** đối tác quay trên env nghiệm thu `ospgroup.vn` bản **V1.0**; đợt này verify trên env
> dev `18.143.165.120.nip.io` bản mới. Verdict Pass (nếu có) chỉ có hiệu lực cho env + bản dựng ghi ở đầu file.
