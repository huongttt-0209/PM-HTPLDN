# Tiêu chí verify — LKHDG_12

Mã case: **LKHDG_12** (dòng 126, tab `bug`)  ·  Thời điểm viết: **2026-08-06 08:05**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: **HTPLDN · V1.0.8**, gói mã
`assets/index-DThrFe1_.js` (đọc ở chân thanh điều hướng + `script[src]`) · đo lúc **2026-08-06 08:02–08:12**

> **Case này KHÔNG viết tiêu chí mới.** Đã có sẵn bug entry + khối `CÁCH VERIFY sau Dev fix`
> (`flowtest-kiemdinh/bug-report.md:106-128`) nên theo flow 04 §Bước 0.2 chỉ cần **chạy lại đúng khối đó**.
> Mục 1-5 dưới đây **giữ nguyên** từ `flowtest-kiemdinh/tieuchi/LKHDG_12.md` (viết 2026-08-06 00:13, trước khi
> mở màn) — chép lại để file này tự chứa. **Mục 6 là số đo MỚI của lượt này**, không chép số cũ.

---

## 1. Đối tác phản ánh — tách 3 vế

| Vế | Nội dung đối tác ghi | Ghi chú |
|---|---|---|
| **a** | "Hệ thống xuất danh sách **không đúng với tiêu chí lọc**" | Vế duy nhất đối tác **retest lại 30/07** và vẫn ghi Fail (cột "TKM phản hồi lần 1") |
| **b** | "File excel xuất ra **thiếu cột** *Số vụ việc*, *Người tạo*, *Ngày tạo*" | |
| **c** | "Các cột *Tần suất*, *Đối tượng*, *Trạng thái* hiển thị **không dấu**" | Thực chất ghi **mã enum thô** (`TRON_NAM`, `VU_VIEC`, `LAP_KE_HOACH`) |

**Bằng chứng đã mở xem:** `partner-evidence/LKHDG_12.webm` (7.695.544 byte, 21s), đã trích frame đọc full-res:
- màn danh sách **sau khi lọc** `?tanSuat=TRON_NAM&page=1`, chân bảng **"Hiển thị 1-4 / 4 kết quả"**;
- tệp `ke-hoach-danh-gia-1783739630247.xlsx` mở trong Excel: **7 cột**, **14 dòng dữ liệu**, có cả
  `SO_BO_6_THANG` ⇒ tệp không áp bộ lọc `TRON_NAM` đang bật.

## 2. Đặc tả nói gì

- **BR-DATA-06** — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5525`:
  *"**Export Excel:** Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá
  10,000 rows/file"*. Cột "Áp dụng" = **"Toàn bộ CRUD list"**; cột "Ngoại lệ" chỉ nêu *"Báo cáo nhóm IX có xuất
  PDF theo khung TT 17/2025"* — **không** miễn trừ nhóm VI.
- **SCR-VI-01 Phần A** — `srs-fr-08-danh-gia.md:821`: thanh tiêu đề có nút **[Xuất Excel]**, hành vi
  *"click → tương ứng"*. Đây là chỗ duy nhất trong nhóm VI nhắc tới xuất Excel của màn danh sách.
- Cột bảng **trên màn** (`srs-fr-08-danh-gia.md:829-837`): Mã đợt · Tên đợt · Tần suất · Đối tượng · Kỳ đánh giá ·
  Trạng thái · **Người tạo** (`:835`) · **Ngày tạo** (`:836`) · Hành động. **Không có cột "Số vụ việc"**.

**IM LẶNG về:**
- **Tập cột của TỆP xuất** — nhóm VI không có FR nào đặc tả luồng xuất; BR-DATA-06 chỉ ràng buộc *bộ lọc* +
  *số dòng*. ⇒ không có căn cứ bắt tệp phải mang đủ cột của bảng trên màn.
- **Định dạng nhãn trong TỆP xuất** — bảng nhãn `:829-837` là đặc tả **màn hình**, không phải tệp.
- **"Số vụ việc"** — không có trong đặc tả màn hình lẫn tệp.

## 3. Precondition

- Tài khoản **`cbnv_tw`** (CB Nghiệp vụ Trung ương, `Test@1234`) — đúng vai trò đối tác dùng trong video.
  Không dùng `admin` để ra verdict.
- Màn **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**, URL `/danh-gia/ke-hoach/danh-sach`.
- Dữ liệu: mỗi cột lọc dùng để đo phải có **≥2 giá trị khác nhau**, và `n_lọc` < `n_tổng` — nếu lọc không cắt
  bớt gì thì phép đo vô nghĩa.

## 4. Tiêu chí chấm

### Vế (a) — bộ lọc: CHẤM ĐƯỢC

**✅ PASS khi** — thoả **cả 4** ý, đo trên **≥2 bộ lọc khác cột nhau**:
1. Chọn bộ lọc F sao cho chân bảng báo `n_lọc` **<** `n_tổng`.
2. Bấm **[Xuất Excel]** → mở tệp, **số dòng dữ liệu** (không kể tiêu đề) = **đúng `n_lọc`**.
3. **Tập mã đợt** trong tệp **trùng khít** tập mã trên màn sau lọc — so **từng mã**, không chỉ so số lượng.
4. Lặp ý 1-3 với bộ lọc ở **cột khác**; **cả hai lần đều thoả**.

**❌ FAIL nếu**: tệp chứa ≥1 mã **không** thuộc tập sau lọc · số dòng **≠** `n_lọc` · tệp trả toàn bộ danh sách
như khi không lọc · 2 lượt lọc khác nhau cho 2 tệp **cùng kích thước byte**.

### Vế (b) và (c) — KHÔNG CHẤM, chỉ ghi nhận hiện trạng

**KHÔNG được chấm Fail vì** tệp thiếu cột hay vì nhãn ghi mã thô — đặc tả **im lặng** cả hai (mục 2). Đòi tệp
phải sao đúng cột của bảng là QA tự đặt luật.

**Phép thử mục 4:** người chưa biết bug này, chỉ đọc mục 4, có chấm được PASS/FAIL không? → Có: lọc, đếm 2 con
số, so 2 tập mã.

## 5. Dạng dữ liệu phải phủ — M = 5

1. Tần suất `SO_BO_6_THANG` · 2. Tần suất `TRON_NAM` · 3. Đối tượng `VU_VIEC` ·
4. Đối tượng `DAO_TAO`/`TONG_HOP` · 5. ≥2 giá trị Trạng thái khác nhau.

**Nguồn xác định M:** cách ② — bộ lọc + giá trị enum ngay trên màn, SCR-VI-01 #4/#5/#6
(`srs-fr-08-danh-gia.md:823-825`). Không dùng cách ① vì nhóm VI không có FR nào nói về nguồn dữ liệu tệp xuất.

## 6. Bảng điều kiện — số đo LƯỢT NÀY (2026-08-06 08:02–08:12)

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — "Cán bộ NV Trung ương", đơn vị `BTP · TW` | **`cbnv_tw`** — CB_NV_TW, `BTP · TW`. Trùng vai trò + trùng cấp | Không |
| Entity + trạng thái | 14 đợt trải 5 trạng thái (LAP_KE_HOACH / THUC_HIEN / DANG_DANH_GIA / CHO_DUYET_PC / HOAN_THANH) | 20 đợt trải **7 trạng thái**: Lập kế hoạch · Đang đánh giá · Thực hiện · Hủy · Đã đánh giá · Chờ phê duyệt · Hoàn thành. Bản ghi đối tác nằm ở env khác → dùng bản ghi tương đương, phân bố trạng thái **rộng hơn** của đối tác | Không |
| Dữ liệu tiền đề | `n_tổng` ≥ 14; `n_lọc` = 4 khi `tanSuat=TRON_NAM` | `n_tổng` = **20**; `n_lọc` = **19** (lọc Tần suất) và **4** (lọc Trạng thái). Đợt `DG-20260806-0001` (Sơ bộ 6 tháng) đã seed từ lượt 00:22 cùng ngày, **vẫn còn** — không seed thêm gì ở lượt này | Không |
| Input / filter / giá trị nhập | Lọc **Tần suất = "Trọn năm"** → URL `?tanSuat=TRON_NAM&page=1` | Lượt 1: **Tần suất = "Tròn năm"** → `?tanSuat=TRON_NAM&page=1` (**trùng khít URL đối tác**). Lượt 2: **Trạng thái = "Hoàn thành"** → `?trangThai=HOAN_THANH&page=1` (cột lọc khác, theo mục 4 ý 4) | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 14 dòng trong tệp / 4 dòng trên màn | N = **20 dòng trong tệp** (cả 2 lượt) / 19 và 4 dòng trên màn. M = **5/5**: Sơ bộ 6 tháng ✓ · Tròn năm ✓ · Vụ việc ✓ · Đào tạo ✓ + Tổng hợp ✓ · 7 trạng thái ✓ | Không |

**GAP còn lại: 0.**

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** `https://htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/danh-sach?tanSuat=TRON_NAM&page=1`;
  tệp xuất `ke-hoach-danh-gia-1783739630247.xlsx`
- **Trạng thái entity:** 14 đợt trải 5 trạng thái
- **Vai trò + bản dựng:** CB_NV_TW · **HTPLDN · V1.0** · env `htpldn-uat.ospgroup.vn` · 2026-07-11 10:13-10:14

> ⚠️ **Lệch env + bản dựng:** đối tác quay trên env nghiệm thu `ospgroup.vn` bản V1.0; lượt này đo trên env dev
> `18.143.165.120.nip.io` bản V1.0.8. Đây là **giới hạn hiệu lực** của verdict, không phải GAP.

## 7. Sửa đổi so với lần viết trước

**2026-08-06 08:12** — bổ sung 1 ý vào `❌ FAIL nếu` của mục 4: *"2 lượt lọc khác nhau cho 2 tệp cùng kích
thước byte"*. Lý do: ý này vốn đã nằm trong khối `CÁCH VERIFY` (`flowtest-kiemdinh/bug-report.md:120-121`)
nhưng chưa được chép vào mục 4 của file tiêu chí; lượt này chính dấu hiệu đó bắt lỗi nhanh nhất
(8520 byte ở cả 2 lượt). **Không** nới lỏng tiêu chí nào, chỉ ghi thêm một dấu hiệu FAIL.
