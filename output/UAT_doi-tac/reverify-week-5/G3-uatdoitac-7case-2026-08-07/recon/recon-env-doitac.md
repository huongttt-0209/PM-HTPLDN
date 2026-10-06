# RECON — Môi trường nghiệm thu đối tác `htpldn-uat.ospgroup.vn`

> **Lượt CHỈ ĐỌC.** Toàn bộ số đo dưới đây lấy bằng `curl` (chỉ GET, trừ `POST /auth/login` +
> `POST /auth/verify-otp` để lấy phiên). **Không tạo / sửa / xoá bất kỳ bản ghi nghiệp vụ nào.**
> Không mở trình duyệt, không gọi MCP, không ghi sheet.

| Mục | Giá trị |
|---|---|
| Ngày khảo sát | **2026-08-07**, 09:20–09:40 UTC (16:20–16:40 giờ VN) |
| Env | `https://htpldn-uat.ospgroup.vn` |
| Bó mã FE | `assets/index-Bd1akG3f.js` · `Last-Modified: Fri, 07 Aug 2026 08:15:32 GMT` (15:15 giờ VN) — **khớp pre-flight ở BRIEF §3**, không đổi bản dựng trong ngày |
| `GET /api/docs-json` | HTTP 200, không cần đăng nhập, **624 path** |
| Số lượt đăng nhập đã dùng | 4 (`admin`, `cbnv_tw`, `nht_04_ui`, `cb_nv_dp_01`) — tuần tự, cách nhau > 60s |

---

## 1. Bảng tài khoản

### 1.1 Đã tự đăng nhập thử thành công trong lượt này (4/4 PASS)

| Tên đăng nhập | Mật khẩu | Vai trò | Đơn vị / cấp | Trạng thái | Email nhận mã xác thực | Login thử |
|---|---|---|---|---|---|---|
| `admin` | `Secret@123` | QTHT | (không gắn đơn vị) · TW | HOAT_DONG | `admin@htpldn.gov.vn` | ✅ PASS |
| `cbnv_tw` | `Test@1234` | CB_NV_TW | Cục Bổ trợ tư pháp - Bộ Tư pháp · **TW** (`…8000-000000000001`) | HOAT_DONG | `cbnv_tw@htpldn.gov.vn` | ✅ PASS |
| `nht_04_ui` | `Test@1234` | NHT | Cục Bổ trợ tư pháp - Bộ Tư pháp · **TW** (`…8000-000000000001`) | HOAT_DONG | `nht_04_ui@htpldn.test` | ✅ PASS |
| `cb_nv_dp_01` | `Test@1234` | CB_NV_DP | **Sở Tư pháp An Giang** · ĐP (`…8002-000000000006`) | HOAT_DONG | `cb_nv_dp_01@htpldn.test` | ✅ PASS |

### 1.2 🔴 Đính chính quan trọng về cách đặt tên tài khoản

`GET /api/v1/tai-khoan` (cookie `admin`, 12 trang, **221 tài khoản**) cho thấy env đối tác dùng
**tên có dấu gạch dưới đầy đủ**, KHÔNG phải kiểu viết tắt ghi trong `input/input.md`:

| Ghi trong `input.md` | Thực tế trên env đối tác |
|---|---|
| `cbnv_tw_01` … `cbnv_tw_05` | **`cb_nv_tw_01` … `cb_nv_tw_10`** |
| `cbnv_dp_01` … | **`cb_nv_dp_01` … `cb_nv_dp_10`** |
| `cbpd_tw_01` … | **`cb_pd_tw_01` … `cb_pd_tw_10`** |
| `cbpd_dp_01` … | **`cb_pd_dp_01` … `cb_pd_dp_10`** |
| `nht_qa_tw` | **không tồn tại** (thay bằng `nht_04_ui`, `nht_tc001_btp_tw`, `hunglk_test`…) |

→ Câu "các bộ `_01.._05` có thể không tồn tại" trong input.md **sai một phần**: chúng CÓ tồn tại,
chỉ là **sai chính tả tên** (thiếu 2 dấu gạch dưới). Thư MailHog gửi `cb_nv_tw_01@htpldn.test`
lúc 08:54/09:08 UTC là của tài khoản `cb_nv_tw_01`.

### 1.3 Tồn kho tài khoản theo vai trò (221 tài khoản, đếm thật)

| Vai trò | Tổng | Đơn vị/cấp có sẵn (HOAT_DONG) |
|---|---|---|
| `CB_NV_TW` | 14 | `cbnv_tw` + `cb_nv_tw_01..10` (đều Cục BTTP-BTP, TW) · `nghiepvu_angiang` · `nghiepvu_bkhdt` |
| `CB_NV_DP` | 15 | `cbnv_dp` (STP **Hà Nội**) · `cb_nv_dp_01/04/07/10` (An Giang) · `_02/05/08` (Bắc Giang) · `_03/06/09` (Bắc Ninh) · `cb_nv_dp2` (An Giang) |
| `CB_NV_BN` | 17 | (Bộ ngành, chưa dùng cho lô này) |
| `CB_PD_TW` | 14 | `cbpd_tw` + `cb_pd_tw_01..10` (Cục BTTP-BTP, TW) |
| `CB_PD_DP` | 14 | `cbpd_dp` (Hà Nội) · `cb_pd_dp_01..10` (An Giang / Bắc Giang / Bắc Ninh) |
| `CB_PD_BN` | 14 | (Bộ ngành) |
| `NHT` | 34 | **TW:** `nht_04_ui`, `nht_tc001_btp_tw`, `hunglk_test`, `huong2nht`, `huong3nht`, `nht_r10/r11/r12_bug003…` · **ĐP:** `nht_01` (An Giang), `nht_02` (Đà Nẵng), `nht_03` (Hải Phòng), `nhttest` (Hà Nội) |
| `DN` | 27 | `0151554887` (TKM Company, STP Hà Nội, email `tkm@gmail.com`) + 26 tài khoản khác |
| `TVV` / `CG` / `QTHT` / `TKM` | 26 / 15 / 19 / 2 | — |

> **Chỉ 4 tài khoản trên đã được đăng nhập thử thật.** Mật khẩu của các tài khoản còn lại
> **CHƯA kiểm chứng** — giới hạn 5 lượt/60s nên không thử bừa. `Test@1234` đúng cho cả 3 tài khoản
> nghiệp vụ đã thử (`cbnv_tw`, `nht_04_ui`, `cb_nv_dp_01`) → khả năng cao đúng cho cả bộ `_NN`.

### 1.4 Phạm vi dữ liệu theo tài khoản (đo thật, cùng thời điểm)

| Endpoint | `admin` | `cbnv_tw` (TW) | `nht_04_ui` (NHT/TW) | `cb_nv_dp_01` (ĐP An Giang) |
|---|---|---|---|---|
| `GET /api/v1/vu-viecs` | **74** | **74** | — | **20** |
| `GET /api/v1/khoa-hocs` | **22** | **22** | — | **3** |
| `GET /api/v1/bai-giangs` | **7** | **7** | — | **0** |
| `GET /api/v1/tu-van-viens` | **71** | **71** | **71** | **3** |
| `GET /api/v1/vu-viecs?mucSla=SAP_HET` | **1** | **1** | — | **0** |

🔴 **Hệ quả bắt buộc:** tài khoản cấp ĐP **KHÔNG thấy bài giảng nào (0)** và **không thấy vụ việc
SLA "Sắp hết hạn" nào (0)**. QLKTLBG_18/19/20 và TKHSYCHTPL_03 **phải chạy bằng `cbnv_tw`**.

---

## 2. Bảng dữ liệu tiền đề theo case

| Case | Endpoint đã gọi (GET) | HTTP | Tổng bản ghi | Mẫu 3 bản ghi | Kết luận |
|---|---|---|---|---|---|
| **KTDGKQHT_10**<br>Tải lên Excel Kết quả kiểm tra | `/khoa-hocs` · `/khoa-hocs/{id}/de-kiem-tras` · `/khoa-hocs/{id}/ket-quas` · `/khoa-hocs/{id}/ket-quas/template?deKiemTraId=…` | 200 | 22 khóa (DANG_DIEN_RA 7 · DA_KET_THUC 2 · HOAN_THANH 7 · CHO_DUYET 4 · DA_DUYET 2) | `KH-20260509-006` DANG_DIEN_RA · `KH-20260509-005` HOAN_THANH · `KH-20260703-004` DA_KET_THUC | ✅ **ĐỦ TIỀN ĐỀ** — dùng `KH-20260509-006` |
| **QLKTLBG_18/19/20**<br>Xuất Excel bài giảng | `/bai-giangs` (+ bộ lọc `loaiTaiLieu`, `keyword`, `tuNgay/denNgay`, `congKhai`) | 200 | **7** (toàn bộ thuộc đơn vị TW) | "Test ẩn file đính kèm" PDF · "Test video 2" VIDEO (congKhai=false) · "Hướng dẫn kê khai…" SLIDE | ✅ **ĐỦ TIỀN ĐỀ** cho cả 3 case (xem §2.2) |
| **CNHSNLTVV_03**<br>Lưu năng lực TVV | `/tu-van-viens?donViId=…8000-000000000001` · `/tu-van-viens/{id}` | 200 | **63** hồ sơ cùng đơn vị `nht_04_ui`; trong đó **10 HOAT_DONG** | `TVV-BTP-TW-0063` HOAT_DONG (v14) · `TVV-BTP-TW-0030` "huongcg" CG HOAT_DONG · `TVV-BTP-TW-0035` HOAT_DONG | ✅ **ĐỦ TIỀN ĐỀ** |
| **KTHSYCHTPL_11**<br>Hoàn tất kiểm tra — kết luận Đạt | `/vu-viecs` (74 bản, 4 trang) · `/vu-viecs/{id}` · `/vu-viecs/{id}/lich-su` · `/vu-viecs/{id}/ket-qua-kiem-tra` | 200 | **DA_TIEP_NHAN = 12** (11 thuộc TW) · **DANG_KIEM_TRA = 4** | `VV-BTP-TW-20260807-001` DA_TIEP_NHAN TW · `VV-BTP-TW-20260805-001` DA_TIEP_NHAN TW · `VV-BTP-TW-20260805-004` DANG_KIEM_TRA TW | ✅ **ĐỦ TIỀN ĐỀ** ở cấp TW — ⚠️ cấp ĐP xem §2.4 |
| **TKHSYCHTPL_03**<br>Lọc Mức SLA "Sắp hết hạn" | `/vu-viecs?mucSla={4 giá trị}` | 200 (cả 4) | `BINH_THUONG` **29** · `SAP_HET` **1** · `QUA_HAN` **5** · `QUA_HAN_NGHIEM_TRONG` **39** (cộng = 74 ✓) | Chỉ 1 bản ở `SAP_HET`: `VV-BTP-TW-20260713-001` "TKM test", trạng thái **DA_DANH_GIA**, đơn vị TW, deadline `2026-08-03` | ⚠️ **ĐỦ TIỀN ĐỀ TỐI THIỂU (đúng 1 bản ghi)** — xem §2.5 |

### 2.1 KTDGKQHT_10 — chi tiết tiền đề (đã kiểm chứng đến tận tệp mẫu)

Khóa **`KH-20260509-006`** "Luật đất đai cập nhật 2024 - R9"
(`id=dd1adee1-715e-47f9-986d-52f9dcc60373`, đơn vị TW, `DANG_DIEN_RA`, 01–17/02/2026):

- Đề kiểm tra đã gán: **1** — "Đề kiểm tra cuối khóa luật đất đai quý 3 năm 2026"
  (`deKiemTraId=bc334727-7065-4b63-8d58-f814fc31c95d`, trạng thái `KICH_HOAT`).
- Danh sách kết quả học tập: **6 học viên** (tester 1…6), đã có điểm sẵn (vd tester 1: điểm 9.0).
- `GET /khoa-hocs/{id}/ket-quas/template?deKiemTraId=…` → **HTTP 200, 8.280 byte**,
  `content-type: …spreadsheetml.sheet`, `filename="mau-diem-kiem-tra-KH-20260509-006.xlsx"`.
- **Đã mở tệp mẫu đọc nội dung thật:**
  - Sheet ẩn `_HTPLDN_META`: `template_version=1` · `template_type=DIEM_KIEM_TRA` · `khoa_hoc_id` · `de_kiem_tra_id`.
  - Sheet `Mẫu điểm kiểm tra`: cột `hoc_vien_id · Họ tên · Email · Đơn vị · Điểm kiểm tra · Ghi chú`,
    **6 dòng học viên điền sẵn**, cột Điểm để trống.
  - → Khớp đúng bộ cột SRS quy định (`srs-fr-03-dao-tao.md:575-583`).
- Điều kiện trạng thái: SRS `srs-fr-03-dao-tao.md:537` **PRE-04** — nhập điểm kiểm tra chỉ cho phép khi
  khóa ở `DANG_DIEN_RA` **hoặc** `DA_KET_THUC`. `KH-20260509-006` ở `DANG_DIEN_RA` → hợp lệ.

**Khóa dự phòng** (đều đủ đề + học viên, đơn vị TW): `KH-20260509-005` (HOAN_THANH, 1 đề / 5 KQ) ·
`KH-20260703-005` (HOAN_THANH, 1 đề / 2 KQ) · `KH-20260525-001` (DANG_DIEN_RA, 1 đề / 1 KQ).
⚠️ `KH-20260509-004` và `KH-20260703-004` tuy `DA_KET_THUC` nhưng **0 đề kiểm tra, 0 học viên** → không dùng được.

### 2.2 QLKTLBG_18/19/20 — chi tiết bộ lọc (đo thật trên `cbnv_tw`)

| Bộ lọc gọi | HTTP | Tổng | Dùng cho case |
|---|---|---|---|
| (không lọc) | 200 | **7** | **QLKTLBG_19** — xuất không điều kiện lọc |
| `loaiTaiLieu=PDF` | 200 | **2** | **QLKTLBG_18** — xuất có điều kiện lọc |
| `loaiTaiLieu=SLIDE` | 200 | 2 | (dự phòng 18) |
| `loaiTaiLieu=VIDEO` | 200 | 3 | (dự phòng 18) |
| `keyword=zzzkhongtontai999` | 200 | **0** | **QLKTLBG_20** — lọc không có kết quả |
| `tuNgay=2020-01-01&denNgay=2020-12-31` | 200 | **0** | (dự phòng 20) |
| `loaiTaiLieu=PDF&keyword=zzz999` | 200 | 0 | (dự phòng 20) |

7 bài giảng: 2 PDF · 2 SLIDE · 3 VIDEO; 6 công khai + 1 không công khai ("Test video 2");
lĩnh vực trải Thuế / Đất đai / Lao động / Dân sự / Thương mại.

### 2.3 CNHSNLTVV_03 — chi tiết tiền đề

- `nht_04_ui` thuộc đơn vị **`00000000-0000-4000-8000-000000000001`** (Cục Bổ trợ tư pháp - Bộ Tư pháp, TW).
- Hồ sơ TVV/CG **cùng đơn vị đó: 63** — phân bố trạng thái: `MOI_DANG_KY` 24 · `HOAT_DONG` 10 ·
  `CHO_KICH_HOAT` 10 · `TU_CHOI` 9 · `YEU_CAU_BO_SUNG` 6 · `CHO_PHE_DUYET` 2 · `DANG_THAM_DINH` 1 · `VO_HIEU_HOA` 1.
  Loại: 38 TVV / 25 CG.
- **≥2 hồ sơ cùng đơn vị dùng ngay được** (đều `HOAT_DONG`):

| Mã TVV | Họ tên | Loại | Trạng thái | `version` |
|---|---|---|---|---|
| `TVV-BTP-TW-0063` | Tester TKM BTP-TW | TVV | HOAT_DONG | 14 |
| `TVV-BTP-TW-0030` | huongcg | CG | HOAT_DONG | (đọc lúc đo) |
| `TVV-BTP-TW-0035` | TVV R13 A19 Gate Verify | TVV | HOAT_DONG | (đọc lúc đo) |

- Chi tiết `TVV-BTP-TW-0063` đọc bằng cookie `nht_04_ui` → HTTP 200, có đủ trường năng lực
  (`trinhDo="Cử nhân"`, `soNamKinhNghiem=1`, `chuyenNganh="Luật hành chính"`, `linhVucs` 3 mục, `version`).
- Endpoint `PATCH /api/v1/tu-van-viens/{id}/nang-luc` **có tồn tại** (bắt buộc `version`;
  nhận `trinhDo · soNamKinhNghiem · chuyenNganh · bangCapChiTiet · chungChiChiTiet · chungChiMoiIds ·
  chungChiXoaIds · soTheHanhNghe · linhVucIds · kinhNghiem · ghiChuCapNhat`).
- `nht_04_ui` có quyền **`update_tu_van_vien`** (36 quyền) → đủ quyền theo mô tả endpoint
  ("yêu cầu quyền Update, giới hạn theo phạm vi đơn vị").
- SRS: `srs-fr-04-chuyen-gia-tvv.md:367` FR-IV-04 — tác nhân **NHT**, tiền đề "TVV cùng đơn vị với NHT";
  `:1576` SCR-IV-03 tab 3 "Năng lực" hiển thị nút cho vai trò Người hỗ trợ.
  ⚠️ `:1590` + Processing bước 7: nếu TVV đang `YEU_CAU_BO_SUNG` thì lưu năng lực **tự đổi trạng thái**
  sang `DANG_THAM_DINH` → **chọn hồ sơ `HOAT_DONG` để tránh tác dụng phụ ngoài case**.
  ⚠️ `E5 / ERR-NL-05`: hồ sơ `VO_HIEU_HOA` không sửa được (env có 1 hồ sơ như vậy — đừng chọn nhầm).

### 2.4 KTHSYCHTPL_11 — chi tiết tiền đề + cảnh báo chọn sai trạng thái

**Máy trạng thái thật theo SRS** (`srs-fr-05-vu-viec.md:2286-2288`, bảng SM-VUVIEC):

```
CHO_TIEP_NHAN → DA_TIEP_NHAN   (CB NV tiếp nhận)
DA_TIEP_NHAN  → DANG_KIEM_TRA  (CB NV kiểm tra — FR-V.I-06, đối chiếu checklist UC106)
DANG_KIEM_TRA → DA_PHAN_CONG   (Đạt + chọn người/tổ chức xử lý — FR-V.I-09)
DANG_KIEM_TRA → YEU_CAU_BO_SUNG | TU_CHOI
```

🔴 **Tiền đề đúng của case là vụ việc ở `DA_TIEP_NHAN`, KHÔNG phải `DANG_KIEM_TRA`.**
Kiểm chứng bằng `GET /vu-viecs/{id}/lich-su` của `VV-BTP-TW-20260805-004`: chuỗi
`TAO_VV → TIEP_NHAN → KIEM_TRA`, và sau hành động `KIEM_TRA` vụ việc **đứng ở `DANG_KIEM_TRA`**.
Cả 4 vụ việc `DANG_KIEM_TRA` đều **đã có kết quả kiểm tra lưu sẵn với `ketLuan=DAT`, checklist C01–C06 đều DAT**
→ chúng là **tàn dư của lượt bấm trước**, dùng lại sẽ không tái hiện được thao tác "Hoàn tất kiểm tra".

**Vụ việc dùng được (trạng thái `DA_TIEP_NHAN`, đơn vị TW `…8000-000000000001` — `cbnv_tw` thao tác được):**

| Mã vụ việc | Ghi chú |
|---|---|
| `VV-BTP-TW-20260807-001` | "Vụ việc test luồng" — mới nhất, tạo hôm nay |
| `VV-BTP-TW-20260805-001` | "QA doi chung UAT 05-08 - ho so nhap tay" |
| `VV-BTP-TW-20260805-002` | "QA doi chung UAT 05-08 - ho so co tep dinh kem" |
| (+ 8 vụ việc `DA_TIEP_NHAN` khác cùng đơn vị TW) | `VV-BTP-TW-20260805-003`, `-20260804-001..005`, `-20260509-003`, `-20260509-007` |

**Nếu phiếu yêu cầu CẤP ĐỊA PHƯƠNG:**

| Đơn vị | DA_TIEP_NHAN | DANG_KIEM_TRA | CHO_TIEP_NHAN |
|---|---|---|---|
| TW — Cục BTTP (`…8000-…0001`) | **11** | 1 | 0 |
| STP **An Giang** (`…8002-…0006`) | **0** ❌ | 3 (đã kết luận sẵn) | 0 |
| STP **Hà Nội** (`…8002-…0001`) | **0** ❌ | 0 | **3** |
| STP `…8002-…0008` | 1 | 0 | 0 |
| Bộ ngành `…8001-…0005` | 0 | 0 | 2 |

→ **Cấp ĐP KHÔNG có sẵn vụ việc `DA_TIEP_NHAN` nào ở An Giang / Hà Nội.**
Muốn chạy bằng `cb_nv_dp_01` (An Giang) hoặc `cbnv_dp` (Hà Nội) thì **phải seed**: Hà Nội có
3 vụ `CHO_TIEP_NHAN` (`VV-STP-HN-20260805-001/002/003`) → `cbnv_dp` bấm **Tiếp nhận** 1 vụ là có ngay
tiền đề `DA_TIEP_NHAN`. (An Giang không có vụ `CHO_TIEP_NHAN` nào → phải tạo vụ việc mới.)

Cấu trúc kết quả kiểm tra (đọc từ `GET /vu-viecs/{id}/ket-qua-kiem-tra`): `items[]` gồm 6 mục
`C01…C06`, mỗi mục `{ma, ket_qua, ghi_chu}`; kèm `boSungCount`, `ketLuan` (`DAT`/`KHONG_DAT`/`YEU_CAU_BO_SUNG`),
`lyDo`, `nguoiKiemTraId/Ten`, `ngayKiemTra`.

### 2.5 TKHSYCHTPL_03 — chi tiết tham số lọc SLA

**Tên tham số thật:** `mucSla` (query param của `GET /api/v1/vu-viecs`), enum
`BINH_THUONG | SAP_HET | QUA_HAN | QUA_HAN_NGHIEM_TRONG`. "Sắp hết hạn" = **`SAP_HET`**.
Cột trả về trong bản ghi tên là `mucDoCanhBao`.

| Giá trị | HTTP | Tổng bản ghi (`cbnv_tw`) | Phân bố tab |
|---|---|---|---|
| `BINH_THUONG` | 200 | **29** | CHO_TIEP_NHAN 5 · DANG_XU_LY 11 · HOAN_THANH 8 · TU_CHOI 5 |
| **`SAP_HET`** | 200 | **1** | HOAN_THANH 1 |
| `QUA_HAN` | 200 | **5** | DANG_XU_LY 5 |
| `QUA_HAN_NGHIEM_TRONG` | 200 | **39** | DANG_XU_LY 28 · CHO_PHE_DUYET 3 · HOAN_THANH 7 · TU_CHOI 1 |
| `SAP_HET_HAN` (giá trị sai, để dò) | **400** | — | `error.code = ERR-VAL-SYS-00-01`, `field = mucSla`, message: *"mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG"* |

29 + 1 + 5 + 39 = **74 = tổng vụ việc** → bộ lọc phân hoạch đủ, không sót.

**Bản ghi `SAP_HET` duy nhất:**
`VV-BTP-TW-20260713-001` · "TKM test" · trạng thái **`DA_DANH_GIA`** · lĩnh vực Thuế ·
DN "TKM test tự động cập nhật địa chỉ" · người hỗ trợ `huongcg` · đơn vị TW ·
`ngayTiepNhan=2026-07-13` · `deadline=2026-08-03`.

⚠️ **Bẫy cần biết trước khi đo:** bản ghi này nằm ở **tab "Đã xử lý / Hoàn thành"**, không nằm ở tab
mặc định "Đang xử lý". Nếu màn hình mở tab mặc định rồi mới chọn Mức SLA = "Sắp hết hạn" thì
**kết quả sẽ là 0 dòng** dù bộ lọc chạy đúng → dễ chấm Reopen oan. Phải chọn tab **Tất cả** (hoặc
tab Hoàn thành) khi đo.

⚠️ **Bẫy thứ hai:** `deadline` của bản ghi là `2026-08-03`, đã **quá** ngày đo (07/08), nhưng
`mucDoCanhBao` vẫn lưu `SAP_HET` → trường này là **giá trị lưu trong CSDL, không tính lại theo thời gian thực**.
Số 1 bản ghi là ổn định trong lượt đo, nhưng nếu có job nền chạy lại mức cảnh báo thì bản ghi này
có thể rơi sang `QUA_HAN` và **`SAP_HET` về 0**. → **Đếm lại `mucSla=SAP_HET` ngay trước khi đo case này.**

---

## 3. Bảng endpoint hữu ích tra từ `docs-json`

| Đường dẫn | Method | Dùng cho case | Ghi chú |
|---|---|---|---|
| `/api/v1/auth/login` · `/auth/verify-otp` · `/auth/me` | POST/POST/GET | tất cả | Bắt buộc 2 bước OTP; giới hạn **5 lượt/60s** |
| `/api/v1/tai-khoan` | GET | khảo sát tài khoản | Lọc `trangThai · donViId · vaiTroId · loaiTaiKhoanId`; phân trang `page/pageSize`, mặc định 20 |
| `/api/v1/quyen-han` | GET | khảo sát quyền | 299 quyền, gom nhóm theo `nhomChucNang` |
| `/api/v1/khoa-hocs` | GET | KTDGKQHT_10 | Lọc `ctdtId · keyword · hinhThuc · trangThai · tuNgay/denNgay · dateField`; `meta.tabCounts` sẵn số theo trạng thái |
| `/api/v1/khoa-hocs/{id}/de-kiem-tras` | GET | KTDGKQHT_10 | Đề đã gán cho khóa |
| `/api/v1/khoa-hocs/{khoaHocId}/ket-quas` | GET | KTDGKQHT_10 | Danh sách kết quả học tập |
| `/api/v1/khoa-hocs/{khoaHocId}/ket-quas/template?deKiemTraId=` | **GET** | KTDGKQHT_10 | **Tải tệp mẫu** — bước bắt buộc trước khi nạp |
| `/api/v1/khoa-hocs/{khoaHocId}/ket-quas/import/preview` | POST | KTDGKQHT_10 | Xem trước, **chưa ghi dữ liệu** |
| `/api/v1/khoa-hocs/{khoaHocId}/ket-quas/import/confirm` | POST | KTDGKQHT_10 | Xác nhận ghi |
| `/api/v1/bai-giangs` | GET | QLKTLBG_18/19/20 | Lọc `loaiTaiLieu · linhVucId · khoaHocId · congKhai · tuNgay/denNgay · keyword` |
| `/api/v1/bai-giangs/export` | POST | QLKTLBG_18/19/20 | Body `BaiGiangExportDto` = **đúng 7 trường lọc như trên**. Mô tả: xuất .xlsx, cắt theo đơn vị sở hữu (BR-AUTH-08), tối đa 10.000 dòng (BR-DATA-06), màn SCR-III-03 |
| `/api/v1/tu-van-viens` | GET | CNHSNLTVV_03 | Lọc `tuKhoa · linhVucIds · toChucId · donViId · trangThai · loaiTvv · tuNgay/denNgay · dateField` |
| `/api/v1/tu-van-viens/{id}` | GET | CNHSNLTVV_03 | Lấy `version` trước khi sửa |
| `/api/v1/tu-van-viens/{id}/nang-luc` | **PATCH** | CNHSNLTVV_03 | Bắt buộc `version` (khoá lạc quan) |
| `/api/v1/vu-viecs` | GET | KTHSYCHTPL_11 · TKHSYCHTPL_03 | Lọc `keyword · linhVucId · donViId · trangThai[] · kenhTiepNhan · uuTien · **mucSla** · tuNgay/denNgay · dateField · tab · nguoiHoTroId · doanhNghiepId` |
| `/api/v1/vu-viecs/{id}` · `/lich-su` · `/ket-qua-kiem-tra` | GET | KTHSYCHTPL_11 | Đọc trạng thái, `version`, lịch sử hành động, checklist đã lưu |
| `/api/v1/vu-viecs/{id}/kiem-tra` | POST | KTHSYCHTPL_11 | Body `KiemTraVuViecDto`: **bắt buộc `checklist[]` + `ketLuan`** (`DAT`/`KHONG_DAT`/`YEU_CAU_BO_SUNG`), tuỳ chọn `lyDo`, `version` |
| `/api/v1/vu-viecs/{id}/tiep-nhan` | POST | (seed cho ĐP) | Đưa `CHO_TIEP_NHAN → DA_TIEP_NHAN` |
| `/api/v1/vu-viecs/export` | POST | (đối chứng TKHSYCHTPL_03) | Body có đúng `mucSla` → dùng đối chiếu số dòng nếu cần |
| `/api/docs-json` | GET | tra cứu | Mở công khai, không cần đăng nhập |

---

## 4. Rủi ro & khuyến nghị thứ tự chạy 7 case

### 4.1 Case chạy được ngay, không cần seed (6/7)

| # | Case | Tài khoản | Dữ liệu chốt sẵn |
|---|---|---|---|
| 1 | **QLKTLBG_19** (xuất không lọc) | `cbnv_tw` | 7 bài giảng |
| 2 | **QLKTLBG_18** (xuất có lọc) | `cbnv_tw` | `loaiTaiLieu=PDF` → 2 dòng |
| 3 | **QLKTLBG_20** (lọc không kết quả) | `cbnv_tw` | `keyword=zzzkhongtontai999` → 0 dòng |
| 4 | **TKHSYCHTPL_03** (lọc SLA Sắp hết hạn) | `cbnv_tw` | 1 vụ việc `VV-BTP-TW-20260713-001` — **tab Tất cả** |
| 5 | **KTDGKQHT_10** (nạp Excel kết quả) | `cbnv_tw` | `KH-20260509-006` + đề `bc334727…` + 6 học viên |
| 6 | **CNHSNLTVV_03** (lưu năng lực TVV) | `nht_04_ui` | 63 hồ sơ cùng đơn vị, chọn `TVV-BTP-TW-0063` (HOAT_DONG) |

### 4.2 Case cần seed / cần quyết định phạm vi (1/7)

| Case | Vấn đề | Cách seed (nhỏ nhất) |
|---|---|---|
| **KTHSYCHTPL_11** | Cấp **TW đủ tiền đề** (11 vụ `DA_TIEP_NHAN`). Nhưng **cấp ĐP có 0 vụ `DA_TIEP_NHAN`** ở cả An Giang lẫn Hà Nội. 4 vụ `DANG_KIEM_TRA` sẵn có **đã kết luận Đạt rồi** → dùng lại là Pass oan. | Nếu phiếu bắt buộc cấp ĐP: đăng nhập `cbnv_dp` (STP Hà Nội) → **Tiếp nhận** 1 trong 3 vụ `VV-STP-HN-20260805-001/002/003` (`CHO_TIEP_NHAN`) → có ngay `DA_TIEP_NHAN`. Nếu phiếu không ràng buộc cấp: chạy thẳng bằng `cbnv_tw`, không cần seed. |

### 4.3 Rủi ro bị chặn / dễ chấm sai

| # | Rủi ro | Mức | Hành động phòng ngừa |
|---|---|---|---|
| R1 | **`SAP_HET` chỉ có ĐÚNG 1 bản ghi, lại ở trạng thái `DA_DANH_GIA` (tab Hoàn thành).** Đo ở tab mặc định sẽ thấy 0 dòng → Reopen oan. | 🔴 Cao | Trước khi bấm, đếm lại `GET /vu-viecs?mucSla=SAP_HET`. Trên màn phải chọn tab **Tất cả**. Ghi rõ mã vụ việc kỳ vọng vào file `chuan/TKHSYCHTPL_03.md`. |
| R2 | `mucDoCanhBao` là **giá trị lưu**, `deadline` của bản ghi duy nhất đã qua (03/08 < 07/08). Nếu job nền tính lại, `SAP_HET` có thể về **0** → case mất tiền đề giữa chừng. | 🔴 Cao | Đo TKHSYCHTPL_03 **sớm trong lô**. Nếu về 0 → phải seed vụ việc mới có deadline còn ~40% và **KHÔNG** được Pass. |
| R3 | 4 vụ `DANG_KIEM_TRA` đã có checklist C01–C06 = DAT + `ketLuan=DAT` lưu sẵn. Mở ra thấy "đã Đạt" rồi kết luận Pass = **Pass bằng quan sát tĩnh** (BRIEF §4.2 cấm). | 🔴 Cao | Bắt buộc chạy từ vụ việc `DA_TIEP_NHAN` mới, tự tick checklist, tự bấm Hoàn tất kiểm tra. |
| R4 | Tài khoản cấp ĐP thấy **0 bài giảng** và **0 vụ SLA `SAP_HET`**. Dùng nhầm `cb_nv_dp_01` cho QLKTLBG hoặc TKHSYCHTPL_03 → màn trắng, dễ log bug ma. | 🟠 Vừa | 4 case đó **chỉ dùng `cbnv_tw`**. |
| R5 | **Không tồn tại quyền `export_bai_giang`** trong toàn bộ 299 quyền của hệ thống; `cbnv_tw` chỉ có `create/read/update/delete_bai_giang` (không có mục export nào cho bài giảng). Chưa xác minh được endpoint `POST /bai-giangs/export` guard theo quyền nào **vì lượt này chỉ đọc**. | 🟠 Vừa | Việc đầu tiên của người đo QLKTLBG: bấm nút Xuất Excel 1 lần, đọc mã HTTP. Nếu **403** → đó là phát hiện thật, log bug + báo lead, **không** đổi tài khoản để lách. |
| R6 | Tương tự, không có quyền `import_ket_qua_dao_tao`; `cbnv_tw` có `update_ket_qua_dao_tao` + `create_ket_qua_dao_tao`. | 🟢 Thấp | Nếu `import/preview` trả 403 thì log; nhiều khả năng endpoint guard theo `update_ket_qua_dao_tao` (đã có). |
| R7 | Hồ sơ TVV ở `YEU_CAU_BO_SUNG` khi lưu năng lực sẽ **tự nhảy sang `DANG_THAM_DINH`** (FR-IV-04 Processing bước 7) → đổi trạng thái ngoài ý muốn. Hồ sơ `VO_HIEU_HOA` bị chặn (`ERR-NL-05`). | 🟢 Thấp | Chọn hồ sơ `HOAT_DONG` (10 hồ sơ khả dụng). |
| R8 | Giới hạn **5 lượt đăng nhập / 60 giây** cho cả env. | 🟠 Vừa | Mỗi tài khoản đăng nhập **1 lần / phiên**, giữ cookie dùng xuyên suốt (JWT `idleTtl=1800` = 30 phút nhàn rỗi). Cách nhau ≥15s khi đổi tài khoản. |

### 4.4 🟡 Phát hiện ngoài phạm vi 7 case (ghi nhận theo BRIEF §4.12, chưa log bug)

**Bộ lọc `congKhai` của danh sách bài giảng không có tác dụng.** Gọi `GET /api/v1/bai-giangs`
với `congKhai=true` · `congKhai=false` · `congKhai=1` · `congKhai=0` → **cả 4 lần đều trả đúng
6 bản ghi giống hệt nhau, tất cả đều `congKhai=true`**; bài giảng "Test video 2" (`congKhai=false`)
không bao giờ xuất hiện, dù tổng danh sách không lọc là 7.
→ Đây là **quan sát ở tầng API**, chưa kiểm chứng trên màn hình. Vì `congKhai` cũng nằm trong
`BaiGiangExportDto`, người đo **QLKTLBG_18** nên thử bộ lọc này trên UI: nếu màn hình có ô lọc
"Công khai" thì đây là bug thật thuộc phạm vi case 18; nếu màn hình không có ô đó thì ghi vào `note/`
và báo lead, **không tự thêm dòng sheet mới**.

### 4.5 Thứ tự chạy đề xuất

| Bước | Case | Tài khoản | Lý do xếp thứ tự |
|---|---|---|---|
| 1 | **TKHSYCHTPL_03** | `cbnv_tw` | Tiền đề mong manh nhất (1 bản ghi, có thể bay theo job SLA) → đo trước tiên |
| 2 | **QLKTLBG_19** | `cbnv_tw` | Cùng phiên; đồng thời **dò sớm rủi ro R5** (quyền xuất Excel) — nếu 403 thì biết ngay cả 3 case QLKTLBG cùng số phận |
| 3 | **QLKTLBG_18** | `cbnv_tw` | Nối tiếp cùng màn Kho tài liệu |
| 4 | **QLKTLBG_20** | `cbnv_tw` | Nối tiếp, chỉ đổi bộ lọc |
| 5 | **KTDGKQHT_10** | `cbnv_tw` | Cùng phiên `cbnv_tw`, module Đào tạo; tiền đề đã chốt cứng |
| 6 | **KTHSYCHTPL_11** | `cbnv_tw` (hoặc `cbnv_dp` nếu phiếu bắt buộc ĐP) | Đổi màn Vụ việc; **thao tác này đổi trạng thái** nên để sau các case chỉ đọc |
| 7 | **CNHSNLTVV_03** | `nht_04_ui` | Case duy nhất phải đổi tài khoản → để cuối, tránh tốn lượt đăng nhập giữa chừng |

Tổng số lượt đăng nhập cần cho cả lô: **2** (`cbnv_tw` cho bước 1–6, `nht_04_ui` cho bước 7),
**+1** (`cbnv_dp`) nếu KTHSYCHTPL_11 phải chạy ở cấp địa phương.
