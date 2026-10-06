# State Machines Reference — SRS v3.5

> **Trạng thái file:** ⚠️ **DRAFT v2 — 2026-05-16.** Verification breakdown:
> - **5/14 module ✅ Verified** — FR-05 Vụ việc (12 states, deep-verify 2026-05-16), FR-06 Chi trả (10 states), FR-08 Đánh giá (8 states), FR-12 TVCS (7 states), FR-15 CT HTPLDN (8 states + đợt BC).
> - **1/14 module ⚠️ Partial** — FR-10 QTHT (enum LOAI_HINH_HO_TRO verified, state machine user/role chưa verify).
> - **6/14 module ❌ Chưa verified** — skeleton từ trí nhớ + flow-module.md, **CẤM quote trực tiếp trong bug report** (FR-02/03/04/07/09/13/14).
> - **2/14 module không có SM** — FR-01 Dashboard + FR-11 Báo cáo (read-only).
>
> Tester phải tự mở SRS file verify line số TRƯỚC KHI log bug citing state code từ file này.
>
> **Mục đích:** Bảng tra cứu nhanh state machine của 14 module (+ cross-cutting) trong SRS v3.5. Dùng TRƯỚC khi viết test plan / log bug / verify spec.
>
> **Quan trọng:** SRS v3 (legacy) ≠ SRS v3.5 — nhiều module đã đổi state machine. Đừng dùng trí nhớ v3 cũ. Quote line từ file SRS v3.5 cụ thể khi log bug.
>
> **Nguồn:** `input/srs-update-2026-5-5/srs-fr-NN-*.md`. Mỗi state có quote line gốc — KHÔNG bịa.
>
> **TODO trước R21:** Verify từng state code + line số cho 11 module `⚠️ Check` qua script `scripts/verify-state-machines.sh` (chưa có — cần viết). Tracking: `tasks/srs-contradictions.md` SRS-C-NNN nếu phát hiện contradict trong quá trình verify.

---

## Cách dùng file này

1. **Trước test:** Mở module cần test → đọc transition table → biết state nào → state nào hợp lệ.
2. **Trước log bug:** Verify expected state theo bảng + quote line SRS gốc.
3. **Sau dev fix:** So sánh state thực tế (UI/API) vs bảng + quote line.
4. **Khi spec ambiguous:** Cross-check NotebookLM HTPLDN (ID `a4ae45bf-cea0-4325-8fee-b1e0be702cf2`) + escalate BA + log vào `tasks/srs-contradictions.md`.

---

## Tổng quan 14 module — state machine có/không + verification status

| FR | Module | Có SM? | File SRS v3.5 | Đổi vs v3? | Verified (date) | Safe để quote? |
|:-:|---|:-:|---|:-:|:-:|:-:|
| FR-01 | Dashboard | Không | srs-fr-01-dashboard.md | - | - | - |
| FR-02 | Hỏi đáp | Có (TV nhanh) | srs-fr-02-hoi-dap.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-03 | Đào tạo | Có (SM-KHOAHOC 9 state + SM-CTDT + SM-KE_HOACH_NAM + HOC_VIEN) | srs-fr-03-dao-tao.md | ✅ Đổi (BA OUT Thay đổi 3 — giữ 9 v3, KHÔNG thêm TU_CHOI) | ⚠️ 2026-05-16 KHOA_HOC verify | ⚠️ KHOA_HOC safe quote — CTDT/HOC_VIEN chưa verify |
| FR-04 | Chuyên gia / TVV | Có (TVV state + workflow) | srs-fr-04-chuyen-gia-tvv.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-05 | Vụ việc | Có (VV 12 state + LICHSU 18 enum) | srs-fr-05-vu-viec.md | ✅ Đổi (12 state + LICHSU 18 enum) | ✅ 2026-05-16 deep-verify | ✅ Safe quote |
| FR-06 | Chi trả | Có (HO_SO_CHI_TRA 10 state) | srs-fr-06-chi-tra.md | ✅ Đổi (7→10 state) | ✅ 2026-05-16 deep-verify | ✅ Safe quote |
| FR-07 | Doanh nghiệp | Có (DN profile + xác thực) | srs-fr-07-doanh-nghiep.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-08 | Đánh giá | Có **8 states** (đổi từ v3 6 states) | srs-fr-08-danh-gia.md | ✅ Đổi (bỏ DA_DANH_GIA) | ✅ 2026-05-13 deep-verify | ✅ Safe quote |
| FR-09 | Biểu mẫu | Có (BM state) | srs-fr-09-bieu-mau.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-10 | Quản trị (QTHT) | Có (danh mục + user role) | srs-fr-10-quan-tri.md | ⚠️ Check | ⚠️ Partial 2026-05-13 (enum LOAI_HINH_HO_TRO) | ⚠️ Partial — enum verified, state chưa |
| FR-11 | Báo cáo | Không (read-only KPI) | srs-fr-11-bao-cao.md | - | - | - |
| FR-12 | TV chuyên sâu | Có (TUVCS 7 state workflow) | srs-fr-12-tv-chuyen-sau.md | ✅ Đổi (5→7 state, Thay đổi 3) | ✅ 2026-05-16 deep-verify | ✅ Safe quote |
| FR-13 | TV nhanh | Có (Q&A state) | srs-fr-13-tv-nhanh.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-14 | Hợp đồng TV | Có (HD state) | srs-fr-14-hop-dong-tv.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-15 | CT HTPLDN | Có (SM-KH-CTHTPL 8 state + SM-DOT-BC) | srs-fr-15-ct-htpldn.md | ✅ Đổi (6→8 state, rename DU_THAO/HOAN_THANH) | ✅ 2026-05-16 deep-verify | ✅ Safe quote |

**Verification status legend:**
- ✅ Verified — Mọi state code + line số đã grep từ SRS thật + cross-check NotebookLM. Safe để quote trực tiếp.
- ⚠️ Partial — Một phần verified (vd chỉ enum, chưa state machine; hoặc chỉ list state, chưa line số). Phải tự verify line số trước khi quote bug.
- ❌ Chưa — Skeleton từ trí nhớ + flow-module.md. **CẤM quote trực tiếp**, phải tự mở SRS file verify trước.

**⚠️ Check** ở cột "Đổi vs v3" = nghi đổi vs v3, cần verify bằng CHANGELOG-v3-to-v3.5.md trước khi log bug.

**Quy trình verify 1 module (10-15 phút/module):**
1. `grep -n "trang_thai\|state\|enum" input/srs-update-2026-5-5/srs-fr-NN-*.md` → list state code.
2. Cross-check với `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` xem có đổi vs v3.
3. Query NotebookLM HTPLDN câu hỏi "State machine của module {tên} là gì?" → đối chiếu.
4. Update bảng entry + cột Verified date.
5. Nếu phát hiện contradict 2 nguồn → add entry SRS-C-NNN vào `tasks/srs-contradictions.md`.

---

## Detail per module — quote line SRS gốc

### FR-05 — Vụ việc (Vu viec) — ✅ Verified 2026-05-16

> **Status:** SM-VUVIEC 12 trạng thái + 14 transition. Verified từ `srs-fr-05-vu-viec.md:48-66` (Mermaid diagram). Safe để quote trực tiếp.

**SM-VUVIEC — 12 trạng thái (`srs-fr-05-vu-viec.md:48`):**

| # | Code | Tên Việt | Quote SRS |
|:-:|---|---|---|
| 1 | `MOI_TAO` | Mới tạo (API inbound DVC) | srs-fr-05-vu-viec.md:52 |
| 2 | `CHO_TIEP_NHAN` | Chờ tiếp nhận | srs-fr-05-vu-viec.md:52,53 |
| 3 | `DA_TIEP_NHAN` | Đã tiếp nhận | srs-fr-05-vu-viec.md:53,54 |
| 4 | `DANG_KIEM_TRA` | Đang kiểm tra | srs-fr-05-vu-viec.md:54 |
| 5 | `YEU_CAU_BO_SUNG` | Yêu cầu bổ sung HS | srs-fr-05-vu-viec.md:55,56 |
| 6 | `DA_PHAN_CONG` | Đã phân công | srs-fr-05-vu-viec.md:57 |
| 7 | `TU_CHOI` | Từ chối (CB NV/CB PD) | srs-fr-05-vu-viec.md:58 |
| 8 | `DANG_XU_LY` | Đang xử lý (TVV) | srs-fr-05-vu-viec.md:59,60 |
| 9 | `CHO_PHE_DUYET` | Chờ phê duyệt KQ | srs-fr-05-vu-viec.md:61 |
| 10 | `DA_DUYET` | Đã duyệt KQ | srs-fr-05-vu-viec.md:62,63 |
| 11 | `HOAN_THANH` | Hoàn thành | srs-fr-05-vu-viec.md:64 |
| 12 | `DA_DANH_GIA` | DN đã đánh giá | srs-fr-05-vu-viec.md:65 |

**Transition map (Mermaid `srs-fr-05-vu-viec.md:50-66`):**
```
MOI_TAO → CHO_TIEP_NHAN → DA_TIEP_NHAN → DANG_KIEM_TRA
DANG_KIEM_TRA ↔ YEU_CAU_BO_SUNG (DN bổ sung)
DANG_KIEM_TRA → DA_PHAN_CONG | TU_CHOI
DA_PHAN_CONG → DANG_XU_LY | DA_TIEP_NHAN (TVV từ chối, srs:815)
DANG_XU_LY → CHO_PHE_DUYET → DA_DUYET | DANG_XU_LY (CB PD reject, srs:74-75)
DA_DUYET → HOAN_THANH → DA_DANH_GIA
```

**Self-loop CONG_KHAI / HUY_CONG_KHAI:** flag boolean `cong_khai` (CR-01 v3.5), không phải state riêng. Áp dụng khi `trang_thai = HOAN_THANH` (BR-PUBLIC-04).

**Soft-delete:** `is_deleted = 1` chỉ cho phép khi `trang_thai = CHO_TIEP_NHAN` (BR-DATA-01, `srs-fr-05:424`).

**LICHSU enum 18 actions (v3.5 NEW):**
- `TIEP_NHAN`, `PHAN_CONG`, `DUYET_PC`, `TU_CHOI_PHAN_CONG`, `TU_CHOI_PD`
- `BAT_DAU_THUC_HIEN`, `BAO_CAO_TIEN_DO`, `HOAN_THANH_THUC_HIEN`
- `DUYET_KET_QUA`, `TU_CHOI_KET_QUA`
- `CONG_KHAI`, `HUY_CONG_KHAI`
- `HUY`, `BO_SUNG_HO_SO`, `CAP_NHAT_THONG_TIN`
- (+ 3 actions khác — verify trong SRS line)

**Error code chính:**
- `ERR-VV-01`..`ERR-VV-NN` (verify trong SRS §Error codes)

**Đổi vs v3:** v3 chỉ có ~10 LICHSU actions, v3.5 mở rộng 18. Bug log v3 actions sẽ invalid.

---

### FR-08 — Đánh giá (Danh gia) — **CRITICAL CHANGE v3 → v3.5**

**v3 (CŨ — KHÔNG dùng):** 6 states với `DA_DANH_GIA` ở cuối.

**v3.5 (MỚI — dùng cho mọi bug/test từ 2026-05-05):** **8 states**, KHÔNG có `DA_DANH_GIA`.

| # | Code | Tên Việt | Transition tới |
|:-:|---|---|---|
| 1 | `LAP_KE_HOACH` | Lập kế hoạch | → PHAN_CONG |
| 2 | `PHAN_CONG` | Phân công đoàn ĐG | → CHO_DUYET_PC |
| 3 | `CHO_DUYET_PC` | Chờ duyệt phân công | → THUC_HIEN / → PHAN_CONG (reject) |
| 4 | `THUC_HIEN` | Đang thực hiện đánh giá | → BAO_CAO |
| 5 | `BAO_CAO` | Lập báo cáo đánh giá | → CHO_PHE_DUYET |
| 6 | `CHO_PHE_DUYET` | Chờ phê duyệt báo cáo | → HOAN_THANH / → BAO_CAO (reject) |
| 7 | `HOAN_THANH` | Hoàn thành | (end state) |
| 8 | `HUY` | Hủy | (end state, từ bất kỳ state nào ngoại trừ HOAN_THANH) |

**Quote SRS:** `input/srs-update-2026-5-5/srs-fr-08-danh-gia.md` §State machine (verify exact line).

**Bài học (R20):** BUG-FUNC-DG-016 log v3 state `DA_DANH_GIA` → false bug, close INVALID 2026-05-13.

---

### FR-10 — Quản trị (QTHT) — enum danh mục

**Source-of-truth danh mục** chung cho cả hệ thống. Module khác (FR-05, FR-12) consume.

**Enum loại danh mục chính (verify trong srs-fr-10-quan-tri.md §Danh mục seed):**
- `LOAI_HINH_HO_TRO` (v3.5 chuẩn) — 6 items: Tư vấn pháp luật / Tham gia tố tụng / Đại diện ngoài tố tụng / Tư vấn ngoài tố tụng / ...
- `LINH_VUC_PHAP_LY` — 10 items
- `LOAI_DOANH_NGHIEP`
- `TRANG_THAI_VV`
- ...

**⚠️ Contradiction đã biết (2026-05-13):**
- FR-05 line 176 dùng `LOAI_HINH_HT` (legacy short form)
- FR-10 line 234 dùng `LOAI_HINH_HO_TRO` (canonical long form)
- BE seed theo FR-10 → FE follow FR-05 → dropdown empty (BUG-E2E-S4-011)
- **Quyết định khuyến nghị:** Align về `LOAI_HINH_HO_TRO` (FR-10 là source-of-truth). Chờ BA confirm.

---

### FR-04 — Chuyên gia / TVV — actor state

**State TVV (verify srs-fr-04-chuyen-gia-tvv.md §UC + §State):**

| Code | Tên Việt |
|---|---|
| `DANG_KY` | Đăng ký mới |
| `CHO_DUYET` | Chờ duyệt hồ sơ |
| `DA_DUYET` | Đã duyệt, chưa hoạt động |
| `DANG_HOAT_DONG` | Đang hoạt động |
| `TAM_NGUNG` | Tạm ngưng |
| `NGUNG_HOAT_DONG` | Ngừng hoạt động |
| `TU_CHOI` | Từ chối duyệt |

**Loại TVV (loaiTvv enum):**
- `TVV` — Tư vấn viên thường
- `CG` — Chuyên gia (mời ngoài)
- `NHT` — Người hỗ trợ (phối hợp)

**Verify filter downstream (FR-05 Vụ việc phân công):**
```
?loaiTvv=CG&trangThai=DANG_HOAT_DONG → ≥1 record
?loaiTvv=NHT&trangThai=DANG_HOAT_DONG → ≥1 record
?loaiTvv=TVV&trangThai=DANG_HOAT_DONG → ≥1 record
```

**Bài học (A5 R5-R7):** Acceptance seed "12 variant TVV" gộp loại → 0 CG / 12 TVV → block 4 round. Phải split per `loaiTvv`.

---

### FR-06 — Chi trả (HO_SO_CHI_TRA) — ✅ Verified 2026-05-16

> **Status:** SM-CHITRA 10 trạng thái, đồng bộ Entity enum + Section 5 (`srs-fr-06-chi-tra.md:62`). Safe để quote.

**SM-CHITRA — 10 trạng thái (`srs-fr-06-chi-tra.md:62-77`):**

| # | Code | Tên Việt | Quote SRS |
|:-:|---|---|---|
| 1 | `CHO_TIEP_NHAN` | Chờ tiếp nhận (API/UI tạo) | srs-fr-06-chi-tra.md:65 |
| 2 | `DANG_KIEM_TRA` | Đang kiểm tra (CB NV) | srs-fr-06-chi-tra.md:65-69 |
| 3 | `YEU_CAU_BO_SUNG` | Yêu cầu DN bổ sung | srs-fr-06-chi-tra.md:67,69 |
| 4 | `DANG_DANH_GIA` | Đang đánh giá mức hỗ trợ | srs-fr-06-chi-tra.md:66,70 |
| 5 | `DANG_THAM_DINH` | Đang thẩm định | srs-fr-06-chi-tra.md:70-72,74 |
| 6 | `CHO_PHE_DUYET` | Chờ CB PD duyệt | srs-fr-06-chi-tra.md:71,73-74 |
| 7 | `DA_DUYET` | CB PD đã duyệt | srs-fr-06-chi-tra.md:73,75 |
| 8 | `DA_THANH_TOAN` | Đã thanh toán | srs-fr-06-chi-tra.md:75 |
| 9 | `TU_CHOI` | Từ chối (kiểm tra/thẩm định/thanh toán) | srs-fr-06-chi-tra.md:68,72,75 |
| 10 | `HUY` | Hủy (DN rút / CB NV hủy ở CHO_TIEP_NHAN) | srs-fr-06-chi-tra.md:76 |

**Transition map:**
```
CHO_TIEP_NHAN → DANG_KIEM_TRA | HUY
DANG_KIEM_TRA ↔ YEU_CAU_BO_SUNG (DN bổ sung)
DANG_KIEM_TRA → DANG_DANH_GIA | TU_CHOI
DANG_DANH_GIA → DANG_THAM_DINH
DANG_THAM_DINH → CHO_PHE_DUYET | TU_CHOI
CHO_PHE_DUYET → DA_DUYET | DANG_THAM_DINH (CB PD reject, trả về sửa)
DA_DUYET → DA_THANH_TOAN | TU_CHOI (ly_do = "THANH_TOAN")
```

**Đổi vs v3 (Major):** v3 = 7 state đơn giản (KHOI_TAO/CHO_DUYET/DA_DUYET/CHO_TT/DA_TT/TU_CHOI/HUY). v3.5 = 10 state phân tách rõ kiểm tra/đánh giá/thẩm định/phê duyệt/thanh toán + thêm YEU_CAU_BO_SUNG cycle. Bug log v3 state sẽ invalid.

---

### FR-09 — Biểu mẫu (BM)

**State BM (verify srs-fr-09-bieu-mau.md):**

| Code | Tên Việt |
|---|---|
| `BAN_NHAP` | Bản nháp |
| `CHO_DUYET` | Chờ duyệt |
| `DA_DUYET` | Đã duyệt (có thể public) |
| `DA_CONG_KHAI` | Đã công khai |
| `TU_CHOI` | Từ chối |
| `KHOA` | Khóa (ngưng dùng) |

---

### FR-03 — Đào tạo (Khoá học + Bài giảng + Học viên) — ⚠️ Partial verify 2026-05-16

> **SM-KHOAHOC 9 state** (BA OUT "Thay đổi 3" 2026-05-06; cite `srs-fr-03-dao-tao.md:35` + `:43` + `:64` + `:1889`). DELTA-MAP-FR03 từng nêu 11 state (thêm TU_CHOI/TU_CHOI_KQ) đã OUT — xem [SRS-C-003](../../tasks/srs-contradictions.md#srs-c-003--fr-03-đào-tạo--sm-khoahoc-số-state-9-vs-11--open) chờ BA confirm dẹp DELTA-MAP.
> **CTDT + KE_HOACH_DAO_TAO** (entity cha): SM riêng có TU_CHOI (refinement Cách 2 — chỉ áp với 2 entity cha, KHÔNG áp KHOA_HOC). Xem `srs-fr-03-dao-tao.md:43` + Processing block FR-III-01.

**SM-KHOAHOC — 9 trạng thái (`srs-fr-03-dao-tao.md:64` + Section 3.4.3.6):**

| # | Code | Tên Việt | Quote SRS |
|:-:|---|---|---|
| 1 | `DU_THAO` | Dự thảo (CB NV tạo, có thể edit; CB PD từ chối quay về đây — gộp, KHÔNG tách TU_CHOI) | srs-fr-03-dao-tao.md:53 + :64 |
| 2 | `CHO_DUYET` | Chờ duyệt | srs-fr-03-dao-tao.md:53 |
| 3 | `DA_DUYET` | Đã duyệt | srs-fr-03-dao-tao.md:54 |
| 4 | `DA_CONG_KHAI` | Đã công khai (mở đăng ký) | srs-fr-03-dao-tao.md:56 |
| 5 | `DANG_DIEN_RA` | Đang diễn ra | srs-fr-03-dao-tao.md:57 |
| 6 | `DA_KET_THUC` | Đã kết thúc | srs-fr-03-dao-tao.md:58 |
| 7 | `CHO_DUYET_KQ` | Chờ duyệt kết quả | srs-fr-03-dao-tao.md:59 |
| 8 | `HOAN_THANH` | Hoàn thành | srs-fr-03-dao-tao.md:60 |
| 9 | `DA_HUY` | Đã hủy | srs-fr-03-dao-tao.md:61 + :64 |

**SM-CTDT + SM-KE_HOACH_NAM:** xem `srs-fr-03-dao-tao.md` Processing block FR-III-NEW-02/03 (refinement Cách 2 — có TU_CHOI riêng).

**State Học viên (HOC_VIEN — entity mới v3.5, 1:1 TAI_KHOAN; chưa deep-verify):**
| Code | Tên Việt |
|---|---|
| `DA_DANG_KY` | Đã đăng ký |
| `XAC_NHAN_THAM_GIA` | Xác nhận tham gia |
| `DANG_HOC` | Đang học |
| `HOAN_THANH` | Hoàn thành |
| `BO_KHOA` | Bỏ khóa |

---

### FR-07 — Doanh nghiệp (DN profile)

**State DN xác thực:**
| Code | Tên Việt |
|---|---|
| `CHUA_XAC_THUC` | Chưa xác thực |
| `CHO_DUYET` | Chờ duyệt xác thực |
| `DA_XAC_THUC` | Đã xác thực |
| `TU_CHOI` | Từ chối |
| `KHOA` | Khóa tài khoản |

---

### FR-12 — TV chuyên sâu (TUVCS) — ✅ Verified 2026-05-16

> **Status:** SM-TVCS 7 trạng thái — đồng bộ Entity field `trang_thai` Section 5 (`srs-fr-12-tv-chuyen-sau.md:115`). Safe để quote.

**SM-TVCS — 7 trạng thái (`srs-fr-12-tv-chuyen-sau.md:115`):**

| # | Code | Tên Việt | Quote SRS |
|:-:|---|---|---|
| 1 | `TIEP_NHAN` | Tiếp nhận (default khi tạo) | srs-fr-12:115,159,184 |
| 2 | `PHAN_CONG` | Đã phân công CG | srs-fr-12:154,161,165,170 |
| 3 | `DANG_TU_VAN` | CG đang tư vấn | srs-fr-12:165,172,188,193,218 |
| 4 | `HOAN_THANH` | Đã hoàn thành | srs-fr-12:188 |
| 5 | `CHO_PHE_DUYET` | Chờ phê duyệt | srs-fr-12:196,199,204,211,216 |
| 6 | `DA_DUYET` | Đã duyệt (CB PD approve) | srs-fr-12:199,204 |
| 7 | `HUY` | Hủy (từ TIEP_NHAN/PHAN_CONG/DANG_TU_VAN) | srs-fr-12:222,227 |

**Transition map (`srs-fr-12:154-227`):**
```
TIEP_NHAN → PHAN_CONG (CB NV phân công CG) | HUY
PHAN_CONG → DANG_TU_VAN (CG xác nhận) | TIEP_NHAN (CG từ chối) | HUY
DANG_TU_VAN → CHO_PHE_DUYET (auto khi hoàn thành, BR-FLOW-01) | HUY
CHO_PHE_DUYET → DA_DUYET (CB PD approve) | DANG_TU_VAN (CB PD reject)
```

**Đổi vs v3 (Major — Thay đổi 3):** v3 = 5 state Mô hình B (BAN_NHAP/CHO_DUYET/DA_DUYET/DA_CONG_KHAI/TU_CHOI). v3.5 = 7 state workflow phân công CG → tư vấn → phê duyệt. Field cong_khai = boolean flag riêng (BR-PUBLIC-01), không phải state.

---

### FR-13 — TV nhanh (Q&A)

**State TV nhanh:**
| Code | Tên Việt |
|---|---|
| `DA_GUI` | DN đã gửi câu hỏi |
| `DA_TIEP_NHAN` | CB đã tiếp nhận |
| `DA_PHAN_CONG` | Phân công TVV trả lời |
| `DA_TRA_LOI` | TVV đã trả lời |
| `DA_DUYET` | Đã duyệt trả lời |
| `CONG_KHAI` | Công khai |
| `HUY` | Hủy |

---

### FR-14 — Hợp đồng TV

**State HD:**
| Code | Tên Việt |
|---|---|
| `KHOI_TAO` | Khởi tạo |
| `CHO_KY_DN` | Chờ DN ký |
| `CHO_KY_TVV` | Chờ TVV ký |
| `DA_KY` | Đã ký 2 bên |
| `DANG_THUC_HIEN` | Đang thực hiện |
| `KET_THUC` | Kết thúc |
| `HUY` | Hủy |

---

### FR-15 — CT HTPLDN (Chương trình hỗ trợ) — ✅ Verified 2026-05-16

> **Status:** 2 state machine — (a) SM-KH-CTHTPL kế hoạch chương trình 8 trạng thái + (b) SM-DOT-BC đợt báo cáo. Verified từ `srs-fr-15-ct-htpldn.md:61-75`. Safe để quote.

**(a) SM-KH-CTHTPL — Kế hoạch CT HTPLDN — 8 trạng thái (`srs-fr-15:61`):**

| # | Code | Tên Việt | Quote SRS |
|:-:|---|---|---|
| 1 | `DU_THAO` | Dự thảo (default khi tạo) | srs-fr-15:64,74,115,145 |
| 2 | `CHO_PHE_DUYET` | Chờ phê duyệt | srs-fr-15:64,65 |
| 3 | `DA_DUYET` | Đã duyệt | srs-fr-15:65-67,69 |
| 4 | `DA_CONG_BO` | Đã công bố | srs-fr-15:67,68,70 |
| 5 | `DANG_THUC_HIEN` | Đang thực hiện | srs-fr-15:69-73 |
| 6 | `TAM_DUNG` | Tạm dừng | srs-fr-15:71,72 |
| 7 | `HOAN_THANH` | Hoàn thành | srs-fr-15:73 |
| 8 | `HUY` | Hủy (chỉ từ DU_THAO) | srs-fr-15:74 |

**Transition map (`srs-fr-15:63-75`):**
```
DU_THAO → CHO_PHE_DUYET (trình duyệt) | HUY (hủy)
CHO_PHE_DUYET → DA_DUYET (duyệt) | DU_THAO (từ chối)
DA_DUYET ↔ DA_CONG_BO (công bố / hủy công bố)
DA_DUYET → DANG_THUC_HIEN (kích hoạt)
DA_CONG_BO → DANG_THUC_HIEN (kích hoạt)
DANG_THUC_HIEN ↔ TAM_DUNG (tạm dừng / tiếp tục)
DANG_THUC_HIEN → HOAN_THANH (hoàn thành)
```

**(b) SM-DOT-BC — Đợt báo cáo CT HTPLDN (`srs-fr-15:77`):**
States: `TAO_DOT` → `DANG_LAP_BC` → `CHO_DUYET_KQ` → `DA_DUYET_KQ` ↔ `DANG_LAP_BC` (từ chối) → `DA_GUI_TW` → `TW_TONG_HOP`. Verify chi tiết `srs-fr-15:77+`.

**Đổi vs v3 (Major):** v3 = 6 state đơn giản (LAP_KE_HOACH/CHO_PHE_DUYET/DA_PHE_DUYET/DANG_TRIEN_KHAI/KET_THUC/HUY). v3.5 đổi tên `LAP_KE_HOACH→DU_THAO`, `DA_PHE_DUYET→DA_DUYET`, `DANG_TRIEN_KHAI→DANG_THUC_HIEN`, `KET_THUC→HOAN_THANH`, thêm `DA_CONG_BO` + `TAM_DUNG`. Bug log v3 state sẽ invalid.

---

## Workflow cập nhật file này

1. **Mỗi lần BA gửi SRS update batch:** đọc CHANGELOG-v3-to-v3.5.md → grep state machine mới → update bảng module tương ứng + đánh dấu ✅ Đổi.
2. **Mỗi lần phát hiện contradiction state:** add note vào module + log entry trong `tasks/srs-contradictions.md`.
3. **Mỗi lần BA confirm decision:** update bảng + xóa note contradict.
4. **CẤM tự bịa state code từ trí nhớ.** Mọi entry phải có quote line SRS.

---

## Quick lookup commands

```bash
# Tìm state machine cho module FR-NN
grep -n "trang_thai\|state\|LAP_KE_HOACH\|CHO_DUYET" input/srs-update-2026-5-5/srs-fr-NN-*.md

# Tìm enum LOAI_X cross-module
grep -rn "LOAI_HINH_HO_TRO\|LOAI_HINH_HT" input/srs-update-2026-5-5/

# Xem CHANGELOG đổi gì giữa v3 và v3.5
less input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md
```

---

*Version: 1.0 — 2026-05-13. Maintained by QA team.*
*Khi tìm thấy line số/enum/state code chưa verify trong file này — tester phải mở SRS file + verify trước khi quote.*
