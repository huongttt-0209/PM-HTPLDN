# State Machines Reference — SRS v3.5

> **Trạng thái file:** ⚠️ **DRAFT v1 — 2026-05-13.** Verification breakdown:
> - **1/14 module ✅ Verified** — FR-08 Đánh giá (8 states, deep-verify 2026-05-13).
> - **2/14 module ⚠️ Partial** — FR-05 Vụ việc (LICHSU 18 enum + state list verified, line số chưa fill), FR-10 QTHT (enum LOAI_HINH_HO_TRO verified, state machine user/role chưa verify).
> - **9/14 module ❌ Chưa verified** — skeleton từ trí nhớ + flow-module.md, **CẤM quote trực tiếp trong bug report**.
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
| FR-03 | Đào tạo | Có (khoá học + bài giảng + học viên) | srs-fr-03-dao-tao.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-04 | Chuyên gia / TVV | Có (TVV state + workflow) | srs-fr-04-chuyen-gia-tvv.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-05 | Vụ việc | Có (VV state + LICHSU 18 enum) | srs-fr-05-vu-viec.md | ✅ Đổi (LICHSU 18 enum mới) | ⚠️ Partial 2026-05-13 | ⚠️ Partial — cần verify line số |
| FR-06 | Chi trả | Có (PHIEU_CT state) | srs-fr-06-chi-tra.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-07 | Doanh nghiệp | Có (DN profile + xác thực) | srs-fr-07-doanh-nghiep.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-08 | Đánh giá | Có **8 states** (đổi từ v3 6 states) | srs-fr-08-danh-gia.md | ✅ Đổi (bỏ DA_DANH_GIA) | ✅ 2026-05-13 deep-verify | ✅ Safe quote |
| FR-09 | Biểu mẫu | Có (BM state) | srs-fr-09-bieu-mau.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-10 | Quản trị (QTHT) | Có (danh mục + user role) | srs-fr-10-quan-tri.md | ⚠️ Check | ⚠️ Partial 2026-05-13 (enum LOAI_HINH_HO_TRO) | ⚠️ Partial — enum verified, state chưa |
| FR-11 | Báo cáo | Không (read-only KPI) | srs-fr-11-bao-cao.md | - | - | - |
| FR-12 | TV chuyên sâu | Có (workflow approve) | srs-fr-12-tv-chuyen-sau.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-13 | TV nhanh | Có (Q&A state) | srs-fr-13-tv-nhanh.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-14 | Hợp đồng TV | Có (HD state) | srs-fr-14-hop-dong-tv.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |
| FR-15 | CT HTPLDN | Có (chương trình + cấp) | srs-fr-15-ct-htpldn.md | ⚠️ Check | ❌ Chưa | ❌ Không — tự verify SRS |

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

### FR-05 — Vụ việc (Vu viec) — ⚠️ Partial verified

> **Status:** State code list verified từ skim SRS 2026-05-13 nhưng line số CHƯA fill. Tester log bug cite VV state phải tự grep `input/srs-update-2026-5-5/srs-fr-05-vu-viec.md` lấy line số chuẩn TRƯỚC khi quote.

**State VV (chưa fill line số — TODO trước R21):**
| Code | Tên Việt | Quote SRS (TODO) |
|---|---|---|
| `DA_TIEP_NHAN` | Đã tiếp nhận | srs-fr-05-vu-viec.md (TODO: grep line) |
| `DA_PHAN_CONG` | Đã phân công TVV | (TODO: grep line) |
| `DANG_THUC_HIEN` | Đang thực hiện | (TODO: grep line) |
| `CHO_DUYET_KQ` | Chờ duyệt kết quả | (TODO: grep line) |
| `DA_HOAN_THANH` | Đã hoàn thành | (TODO: grep line) |
| `DA_HUY` | Đã hủy | (TODO: grep line) |
| `TU_CHOI_PHAN_CONG` | TVV từ chối phân công | (TODO: grep line) |

**Grep command nhanh:**
```bash
grep -n "DA_TIEP_NHAN\|DA_PHAN_CONG\|DANG_THUC_HIEN\|CHO_DUYET_KQ\|DA_HOAN_THANH\|DA_HUY\|TU_CHOI_PHAN_CONG" \
  input/srs-update-2026-5-5/srs-fr-05-vu-viec.md
```

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

### FR-06 — Chi trả (PHIEU_CT)

**State PHIEU_CT (verify srs-fr-06-chi-tra.md):**

| Code | Tên Việt |
|---|---|
| `KHOI_TAO` | Khởi tạo |
| `CHO_DUYET` | Chờ duyệt |
| `DA_DUYET` | Đã duyệt |
| `CHO_TT` | Chờ thanh toán |
| `DA_TT` | Đã thanh toán |
| `TU_CHOI` | Từ chối duyệt |
| `HUY` | Hủy |

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

### FR-03 — Đào tạo (Khoá học + Bài giảng + Học viên)

**State Khoá học:**
| Code | Tên Việt |
|---|---|
| `LAP_KE_HOACH` | Lập kế hoạch |
| `MO_DANG_KY` | Mở đăng ký |
| `DANG_DIEN_RA` | Đang diễn ra |
| `KET_THUC` | Kết thúc |
| `HUY` | Hủy |

**State Học viên:**
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

### FR-12 — TV chuyên sâu (workflow approve)

**State TVCS (verify srs-fr-12-tv-chuyen-sau.md):**
| Code | Tên Việt |
|---|---|
| `BAN_NHAP` | Bản nháp |
| `CHO_DUYET` | Chờ duyệt |
| `DA_DUYET` | Đã duyệt |
| `DA_CONG_KHAI` | Đã công khai |
| `TU_CHOI` | Từ chối |

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

### FR-15 — CT HTPLDN (Chương trình hỗ trợ)

**State Chương trình:**
| Code | Tên Việt |
|---|---|
| `LAP_KE_HOACH` | Lập kế hoạch |
| `CHO_PHE_DUYET` | Chờ phê duyệt |
| `DA_PHE_DUYET` | Đã phê duyệt |
| `DANG_TRIEN_KHAI` | Đang triển khai |
| `KET_THUC` | Kết thúc |
| `HUY` | Hủy |

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
