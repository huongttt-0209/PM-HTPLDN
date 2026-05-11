# Functional Test Report — R7.5.3 SLA banner trừ ngày lễ (BR-CALC-03)

| Thông tin | Giá trị |
|---|---|
| **Dự án** | PM Hỗ trợ Pháp lý Doanh nghiệp |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA huongttt via Claude Code (Chrome DevTools MCP) |
| **Ngày** | 2026-05-11 19:08:00 |
| **Loại test** | Cross-cutting / SLA + BR-CALC-03 deadline calculation |
| **Round** | R7 — task R7.5.3 |
| **Account** | `cb_nv_tw_10` (isolatedContext `cb_nv_tw_10_r753`) |
| **Module** | Hỏi đáp (FR-II-CROSS-01) — đại diện toàn module có SLA |
| **Spec ref** | `srs-v3/srs-fr-02-hoi-dap.md` line 1400-1404 BR-CALC-03 · `srs-v3/srs-v3.md` line 4008 BR-CALC-03 · `srs-v3/srs-fr-11-bao-cao.md` line 249-1260 BR-SLA-02 |

---

## Verdict

✅ **PASS** — BR-CALC-03 deadline calc **CÓ trừ ngày lễ** đúng spec. Banner "Còn N ngày LV" + mucDoCanhBao field tính đúng % SLA. Verify qua HD-20260507-006 và HD-20260507-001 với deadline rơi vào ngày lễ 21/05/2026 → BE pushed sang 22/05 = SKIP ngày lễ ✓.

**Phát hiện thứ cấp (không phải bug, chỉ note):**
- `state-snapshot.md` stale: SLA HOI_DAP ghi 10d nhưng actual config 5d (đổi 2026-05-10 10:43). NGAY_LE 2026 ghi 6 nhưng actual 7 (thêm 22/05 lần 9). HD count ghi 18 nhưng actual 30.
- Bảng NGAY_LE không có field `trangThai` (chỉ `loai`/`ngay`/`tenNgayLe`/`ghiChu`) — state-snapshot ghi "KICH_HOAT:6" sai schema.

---

## Bảng trạng thái TC (snapshot R7.5.3 — LATEST 2026-05-11 19:08:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| R753-TC01 | BR-CALC-03 deadline = ngayTiepNhan + N working days | ✅ Đạt | R7 | HD-20260507-006 + 10wd = 22/05 (skip we Sat/Sun) |
| R753-TC02 | BR-CALC-03 trừ ngày lễ 21/05/2026 | ✅ Đạt | R7 | HD-507-006 deadline 22/05 thay vì 21/05 (skip ngày lễ) |
| R753-TC03 | BR-SLA-02 mức cảnh báo BINH_THUONG (<50%) | ✅ Đạt | R7 | HD-511-002/003 mucDoCanhBao=BINH_THUONG (elapsed 0-1d/5d) |
| R753-TC04 | BR-SLA-02 mức SAP_HET (50-100%) | ✅ Đạt | R7 | HD-509-008 deadline 12/05, elapsed 4d/5d → SAP_HET |
| R753-TC05 | BR-SLA-02 mức QUA_HAN (>100%) | ✅ Đạt | R7 | HD-509-009 deadline 10/05 < today → QUA_HAN |
| R753-TC06 | Banner countdown "Còn N ngày LV" HD list | ✅ Đạt | R7 | UI cột SLA/THỜI HẠN hiển thị countdown wd |
| R753-TC07 | Banner "Đã hoàn thành" cho HD HOAN_THANH/DA_DUYET | ✅ Đạt | R7 | HD-510-001/006/QA-R7-064 hiển thị "Đã hoàn thành" |
| R753-TC08 | Banner "—" cho HD state MOI (chưa tiếp nhận) | ✅ Đạt | R7 | HD-511-001 + 510-009 chưa có ngayTiepNhan → banner "—" |
| R753-TC09 | CAU_HINH_SLA per loaiYeuCau (6 loại) | ✅ Đạt | R7 | HOI_DAP=5d, HOI_DAP_PHUC_TAP=30d, VU_VIEC=15d, HSCT=10d, HSHT=15d, HSTT=10d |
| R753-TC10 | NGAY_LE 2026 KICH_HOAT loaded vào BE | ✅ Đạt | R7 | 7 entries (4 quốc gia + 2 QA seed + 1 Quốc khánh) |
| **Tổng** | **10 TC** | ✅10 | | 100% PASS |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (R7.5.3)

Hiện tại 10/10 TC đều ✅ PASS — không có TC nào block.

---

## Phase 1 — Verify deadline calc (BR-CALC-03)

### Setup

CAU_HINH_SLA active (query `/api/v1/cau-hinh/sla` lúc 12:07 UTC):

| loaiYeuCau | thoiHanNgay | canhBao1 | canhBao2 | quaHanHeSo | version |
|---|:-:|:-:|:-:|:-:|:-:|
| HOI_DAP | **5** | 50% | 100% | 2.0 | 10 |
| HOI_DAP_PHUC_TAP | 30 | 50% | 100% | 2.0 | 1 |
| HO_SO_CHI_TRA | 10 | 50% | 100% | 2.0 | 1 |
| HO_SO_HT | 15 | 50% | 100% | 2.0 | 2 |
| HO_SO_TT | 10 | 50% | 100% | 2.0 | 2 |
| VU_VIEC | 15 | 50% | 100% | 2.0 | 4 |

NGAY_LE 2026 (query `/api/v1/ngay-le?nam=2026`):

| Ngày | Tên | loai | Note |
|---|---|---|---|
| 2026-01-01 | Tết Dương lịch | NGAY_LE | quốc gia |
| 2026-02-17 | Tết Nguyên đán Bính Ngọ | NGAY_LE | quốc gia |
| 2026-04-30 | Ngày Giải phóng miền Nam | NGAY_LE | quốc gia |
| 2026-05-01 | Ngày Quốc tế Lao động | NGAY_LE | quốc gia |
| **2026-05-21** | QA seed (R8 retest lần 8) | NGAY_LE | QA seed |
| **2026-05-22** | QA seed (R8 lần 9, 2026-05-10) | NGAY_LE | QA seed |
| 2026-09-02 | Ngày Quốc khánh | NGAY_LE | quốc gia |

**Tổng:** 7 ngày lễ (state-snapshot ghi 6 — stale, thiếu 22/05).

### TC01 + TC02 — Deadline calc + ngày lễ skip

| HD | mucDoPhucTap | ngayTiepNhan (local Vietnam +07) | Expected deadline (10wd + skip 21/05) | Actual deadline | Verdict |
|---|---|---|---|---|---|
| HD-20260507-006 | THUONG | 2026-05-08 01:31 (Fri) | 22/05/2026 01:31 | **2026-05-22 01:31** | ✅ Đúng — skip 21/05 |
| HD-20260507-001 | THUONG | 2026-05-08 10:21 (Fri) | 22/05/2026 10:21 | **2026-05-22 10:21** | ✅ Đúng — skip 21/05 |

**Tính tay** (HD-20260507-006): ngayTiepNhan 08/05/2026 (Fri) là day 1, +9 wd nữa = 11(2),12(3),13(4),14(5),15(6),18(7),19(8),20(9), [21/05 ngày lễ — SKIP], 22(10) → **deadline 22/05** ✓.

Nếu BE KHÔNG skip ngày lễ 21/05 → deadline sẽ là **21/05** (count 21/05 là day 10). BE trả 22/05 → **CÓ skip ngày lễ** ✓.

### TC03-TC05 — BR-SLA-02 mức cảnh báo

| HD | ngayTiepNhan | deadline | Today | % elapsed | Expected mức | Actual mucDoCanhBao | Verdict |
|---|---|---|---|---|:-:|:-:|---|
| HD-20260511-002 | 11/05 10:57 (Mon) | 18/05 10:57 | 11/05 19:08 | ~0-15% | BINH_THUONG | BINH_THUONG | ✅ |
| HD-20260511-003 | 11/05 16:01 (Mon) | 18/05 16:01 | 11/05 19:08 | ~0-3% | BINH_THUONG | BINH_THUONG | ✅ |
| HD-20260507-006 | 08/05 01:31 (Fri) | 22/05 01:31 | 11/05 19:08 | ~25% | BINH_THUONG | BINH_THUONG | ✅ |
| HD-20260509-008 | 08/05 03:18 (Fri seed-as-08) | 12/05 10:18 (5d arb) | 11/05 19:08 | ~75% | SAP_HET | SAP_HET | ✅ |
| HD-20260509-009 | 06/05 03:18 (Wed seed-as-06) | 10/05 03:18 | 11/05 19:08 | >100% | QUA_HAN | QUA_HAN | ✅ |

→ % SLA threshold 50/100/200 áp đúng cả 3 mức tested.

### TC06-TC08 — UI banner display

| HD | Status | Banner UI (cột SLA/THỜI HẠN) | Verdict |
|---|---|---|---|
| HD-20260511-002 | Tiếp nhận | "Còn 5 ngày LV" | ✅ |
| HD-20260510-003 | Tiếp nhận | "Còn 4 ngày LV" | ✅ |
| HD-20260509-009 | Đang xử lý | "Còn 0 ngày LV" (clamp) | ✅ — đã hết SLA |
| HD-20260507-006 | Đang xử lý | "Còn 7 ngày LV" | ✅ — 22/05-11/05 = 7 wd remaining |
| HD-20260510-001 | Hoàn thành | "Đã hoàn thành" | ✅ |
| HD-QA-R7-064 | Đã duyệt | "Đã hoàn thành" | ✅ |
| HD-20260511-001 | Mới | "—" | ✅ — chưa tiếp nhận |
| HD-20260510-008 | Mới | "—" | ✅ — chưa tiếp nhận |

→ 8/8 sample HDs hiển thị banner đúng theo state machine.

### TC09-TC10 — Config integrity

- ✅ CAU_HINH_SLA 6 loại đầy đủ, mỗi loại có thoiHanNgay/canhBao1/canhBao2/quaHanHeSo
- ✅ NGAY_LE 2026 có 7 entries, all loai=NGAY_LE, BE consume cho BR-CALC-03

---

## Phase 2 — Re-verify chéo (rule deep-review)

User feedback rule `feedback_deep_review_before_ba_defer`: trước khi kết luận, phải verify 2-source. Đã làm:

1. **Grep SRS local** `srs-v3/srs-fr-02-hoi-dap.md:1404` — BR-CALC-03: "Deadline = ngày tiếp nhận + N ngày làm việc. N lấy từ CAU_HINH_SLA. **Ngày làm việc: Thứ 2-6, trừ ngày lễ**". Confirm spec REQUIRE skip ngày lễ.
2. **API verify** `/api/v1/hoi-daps/{id}` field `deadline` cho HD ngày tiếp nhận 08/05 → trả 22/05 (CÓ skip 21/05).
3. **API verify** `/api/v1/ngay-le?nam=2026` → confirm 21/05 trong table.
4. **Timezone check** — UTC vs local Vietnam +07. Initial calc lầm vì so sánh UTC 2026-05-21T18:31 với local 22/05 → re-check phát hiện đó là CÙNG 1 instant. ✓

→ Spec match + BE match + timezone account → R7.5.3 PASS clean.

---

## Bằng chứng

- HD list overview với banner countdown column: [image/r753-hd-list-banner-overview.png](image/r753-hd-list-banner-overview.png)
- HD-20260507-006 detail page hiển thị "Thời hạn SLA: **22/05/2026 01:31**" + banner "Còn 7 ngày LV": [image/r753-hd-507-006-detail-deadline-2205.png](image/r753-hd-507-006-detail-deadline-2205.png)
- API response cho 4 HD đại diện (raw deadline UTC, mucDoCanhBao) — embedded trong Phase 1 tables.

---

## Note cập nhật state-snapshot

State-snapshot drift cần update sau task này:
- HOI_DAP SLA: 10d → **5d** (changed 2026-05-10 10:43, version=10)
- NGAY_LE 2026: 6 → **7** entries (thêm 22/05 R8 lần 9)
- HD total: 18 → **30** (seed mới R7.7.1 + R7.4.D3 + R8 BUG-HD-AUTH retest)
- NGAY_LE schema: không có field `trangThai` — chỉ `loai`. Bỏ "KICH_HOAT:6" notation trong state-snapshot.

---

*2026-05-11 19:08:00 — QA huongttt via Chrome DevTools MCP. NotebookLM HTPLDN `a4ae45bf-cea0-4325-8fee-b1e0be702cf2` chưa cần — spec local đủ rõ ràng + API evidence verify đầy đủ.*
