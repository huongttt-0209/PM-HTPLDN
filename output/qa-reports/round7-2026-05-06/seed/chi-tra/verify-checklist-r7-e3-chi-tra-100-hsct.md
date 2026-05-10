# Verify Checklist — Chi trả 100 HSCT data còn (R7.E3)

**Ngày R3:** 2026-05-09 23:40:00 • **Ngày R2:** 2026-05-09 23:17:00 • **Ngày R1:** 2026-05-07 17:35 • **Tài khoản:** `qtht_01` (R3) / `qtht_02` (R2/R1)
**Màn:** SCR-V.II-01 — Hồ sơ Đề nghị Hỗ trợ Chi phí • **Đường dẫn:** `/chi-tra/danh-sach`
**API endpoint:** `GET /api/v1/ho-so-chi-tras?tab=TAT_CA&page={1,2}&pageSize=100` (BE giới hạn pageSize≤100, gọi 2 page)
**Spec ref:** [funtion/7.6-chi-tra-chi-phi.md](../../../funtion/7.6-chi-tra-chi-phi.md) • SRS FR-V.II-01..15 + [02-thu-tu-module.md §10 SM-CHI-TRA + BR-CALC-01](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md)
**Trigger R3:** B9 retry HSCT000027 FAIL 422 ERR-CT-PD-06 do `tranHoTroNam=100M` (BR-CALC-01 yêu cầu 3M). Phải verify trần (chiều 2) cho toàn pool → R2 BR-OK list (chỉ check %) overly optimistic.
**Trigger R2:** Re-verify sau bug seed BUG-CHITRA-001 (R7.6.1) + chuẩn bị B9/B12 rerun + chuẩn bị R7.7.12.2/3 + R7.7.12 35 TC.

---

## R3 Kết quả: 🚫 **0/12 CHO_PHE_DUYET BR-OK** · 11/108 toàn pool BR-OK (10.2%) · B9 BLOCKED toàn pool

**BR-CALC-01 có 2 chiều:** `mucHoTroPhanTram` (%) + `tranHoTroNam` (VND/năm). R2 chỉ check % → 34/108 OK. **R3 deep check thêm trần → chỉ 11/108 OK.** Trong 23 record OK-% nhưng SAI-trần, BE lưu `tranHoTroNam=100,000,000` thay vì `3,000,000` (SIEU_NHO) — sai 33×. Mặc dù BE list endpoint không trả `tranHoTroNam` (R2 không thể detect), nhưng BR-CALC-01 BE check trên detail → chặn B9 phê duyệt.

### State distribution × full BR check (% + trần) (R3)

| Trạng thái | Tổng | BR % OK | BR đầy đủ OK | Sample BR-OK | Action B-step |
|---|:-:|:-:|:-:|---|---|
| `CHO_TIEP_NHAN` | 10 | 2 | **0** | (không có) | B2 dùng record OK-% (HSCT000004/061) — B2 không gate BR |
| `DANG_KIEM_TRA` | 9 | 3 | **0** | (không có) | **B5 DKT→TU_CHOI ✅** (rejection không gate BR) — đã PASS HSCT000007 R2 |
| `YEU_CAU_BO_SUNG` | 10 | 2 | **0** | (không có) | R7.7.12.2 — B7 (DN bổ sung) không gate BR |
| `DANG_DANH_GIA` | 7 | 1 | **0** | (không có) | B6 (DDG→DTD) không gate BR |
| `DANG_THAM_DINH` | 16 | 10 | **8** | HSCT000073/075/077/076/072/074/001/017 | B7/B8 OK |
| `CHO_PHE_DUYET` | 12 | 3 | **0** | (không có) | **🚫 B9 CPD→DA_DUYET BLOCKED toàn pool — escalate dev** |
| `DA_DUYET` | 10 | 4 | **1** | HSCT000071 (AG) | **B12 DA_DUYET→TU_CHOI_TT ✅** (rejection không gate BR) — dùng HSCT000031 (AG, sai trần OK) |
| `DA_THANH_TOAN` | 18 | — | 1 | HSCT000078 | terminal |
| `TU_CHOI` | 11 | — | 1 | HSCT000067 | terminal |
| `HUY` | 5 | — | 0 | (không có) | terminal |

### Critical: B-step gate BR-CALC-01 vs không

| B-step | Transition | Gate BR-CALC-01? | Lý do |
|---|---|:-:|---|
| B5 | * → TU_CHOI | ❌ KHÔNG | Reject = state transition + reason, không recompute soTienDuyet |
| **B9** | **CPD → DA_DUYET** | ✅ **CÓ** | **PD nhập soTienDuyet → BE check % + trần + da_chi_trong_nam** |
| B12 | DA_DUYET → TU_CHOI_TT | ❌ KHÔNG | Reject thanh toán, không recompute amount |
| B7 | YCBS → DKT | ❌ KHÔNG | DN bổ sung, không recompute amount |
| B6 | DDG → DTD | ❌ KHÔNG | Đánh giá done, chuyển state |

→ **B9 là transition DUY NHẤT bị BR-CALC-01 chặn cứng.** B5/B12 vẫn chạy được trên record sai-trần.

### Detail 23 record OK-% nhưng SAI-trần (mới phát hiện R3)

23 record SIEU_NHO có `pct=100` ✅ NHƯNG `tranHoTroNam=100,000,000` (sai, phải 3,000,000):

| Cluster | Records | Sample state |
|---|---|---|
| AG | HSCT000004, 000007, 000011, 000014, 000021, 000024, 000027, 000031, 000034, 000037, 000041, 000044, 000047 (13) | CTN/DKT/YCBS/DTD/CPD/DA_DUYET/DTT/TU_CHOI |
| BG | HSCT000007 (in AG already), HSCT000027, 000037, 000044, 000047 — gồm 1 trùng | CTN/CPD/DTT/TU_CHOI |
| BN | HSCT000010, 000020, 000030, 000040, 000050 (5) | DKT/DDG/CPD/DTT/HUY |
| BCT | HSCT000061, 000062, 000063, 000064, 000065 (5) | CTN/DKT/CPD/DA_DUYET/DTT |

→ Toàn bộ 23 record do bug seed BE: stored `tranHoTroNam=100M` (default 100 triệu thay vì spec 3M). Cluster lan rộng 4 đơn vị (AG/BG/BN/BCT).

### 11 record full BR-OK toàn pool (R3 verified)

| Trạng thái | Records | Đơn vị |
|---|---|---|
| DANG_THAM_DINH | HSCT000001 (SN), 000017 (SN), 000072 (SN), 000073 (NHO), 000074 (NHO), 000075 (VUA), 000076 (VUA), 000077 (SN) | AG (7) + BG (1) |
| DA_DUYET | HSCT000071 (SN) | AG |
| DA_THANH_TOAN | HSCT000078 (SN) | AG |
| TU_CHOI | HSCT000067 (NHO) | Cục BTTP - Bộ Tư pháp |

### Tác động Bước 1-3 (R3 update)

| Task | B-step | Data đủ R3? | Note |
|---|---|:-:|---|
| R7.6.1 B5 DKT→TU_CHOI | DKT bất kỳ | ✅ | HSCT000007 PASS R2 — không cần BR-OK |
| **R7.6.1 B9 CPD→DA_DUYET** | CPD BR-OK | 🚫 | **0/12 CPD BR-OK toàn pool** → BLOCKED, escalate dev fix `tranHoTroNam` cluster AG/BG/BN/BCT |
| R7.6.1 B12 DA_DUYET→TU_CHOI_TT | DA_DUYET bất kỳ | ✅ | HSCT000031 (AG sai trần OK vì rejection không gate BR) hoặc HSCT000071 (BR-OK) |
| R7.7.12.2 DN bổ sung HS | YCBS bất kỳ | ✅ | B7 không gate BR — HSCT000011 hoặc 000014 |
| R7.7.12.3 CB PD trả về (B8) + N:1 (B9) | B8 OK / B9 block | ⚠️ | B8 (CPD→DTD) không gate BR ✅; B9 N:1 cần BR-OK CPD → BLOCKED |
| R7.7.12 35 TC | mixed | ⚠️ | TC nào trigger B9 phê duyệt → block; TC khác chạy được |

---

## R2 Kết quả: ⚠️ PARTIAL 108 record state cover OK · **74/108 vi phạm BR-CALC-01** (68.5%)

**Pool đã tăng 78 → 108 record** (thêm 30 record HSCT000079..108 + HSCT200xxx series). State distribution cover 11/10 trạng thái SM-CHI-TRA — đủ scope test workflow + functional R7.7.12. **Vấn đề chính:** 74/108 record (68.5%) lưu mức HT % SAI BR-CALC-01 — mở rộng scope BUG-CHITRA-001 (R1 chỉ 4/5 R6 walk, R2 thấy 74/108 lan toàn pool).

### State distribution × BR-CALC-01 compliance (R2)

| Trạng thái | Tổng | BR đúng | BR sai | BR-OK list (sample) | Action B-step |
|---|:-:|:-:|:-:|---|---|
| `CHO_TIEP_NHAN` | 10 | 2 | 8 | HSCT000004, 000061 | B2 (CTN→DKT) |
| `DANG_KIEM_TRA` | 10 | 3 | 7 | HSCT000007, 000062, 000010 | **B5 DKT→TU_CHOI ✅ đủ data** |
| `YEU_CAU_BO_SUNG` | 10 | 2 | 8 | HSCT000011, 000014 | **R7.7.12.2 ✅ đủ data** |
| `DANG_DANH_GIA` | 7 | 1 | 6 | HSCT000020 | B6 (DDG→DTD) |
| `DANG_THAM_DINH` | 16 | 10 | 6 | HSCT000073, 000072, 000075, 000077, 000076 | B7/B8 OK |
| `CHO_PHE_DUYET` | 12 | 3 | 9 | HSCT000027, 000063, 000030 | **B9 CPD→DA_DUYET ✅ đủ data + R7.7.12.3** |
| `DA_DUYET` | 10 | 4 | 6 | HSCT000071, 000064, 000031, 000034 | **B12 DA_DUYET→TU_CHOI_TT ✅ đủ data** |
| `DA_THANH_TOAN` | 18 | — | — | (terminal, không cần test) | terminal |
| `TU_CHOI` | 10 | — | — | (terminal) | terminal |
| `TU_CHOI_THANH_TOAN` | — | — | — | (gộp vào TU_CHOI? cần verify) | — |
| `HUY` | 5 | — | — | (terminal) | terminal |

### Quy mô DN distribution (R2 = 108 record)

| Quy mô | Count | BR-CALC-01 spec | BR sai phổ biến |
|---|:-:|---|---|
| `SIEU_NHO` | 39 | 100% / 3M | 80% (HSCT200xxx series) |
| `NHO` | 37 | **30% / 5M** | **50% (HSCT000xxx) + 60% (HSCT200xxx)** |
| `VUA` | 32 | 10% / 10M | **30% (HSCT000xxx) + 40% (HSCT200xxx)** |

**74 record vi phạm** chia 4 cluster:
1. HSCT000001..050 series (cluster 1, 50%/Nhỏ + 30%/Vừa) — seed gốc sai
2. HSCT200001..030 series (cluster 2, 60%/Nhỏ + 40%/Vừa + 80%/Siêu nhỏ) — seed gốc khác sai khác value
3. HSCT000066..070 (R6 walk pool, 50%/Nhỏ) — đã log R1
4. HSCT000071..078 — **đa số ĐÚNG** BR (re-seed sau R6) ✅

### Tác động downstream R2

| Task | R7.6.1 bước | Data đủ? | Note |
|---|---|:-:|---|
| R7.6.1 B5 DKT→TU_CHOI | DKT BR-OK 3 record | ✅ | HSCT000007 hoặc 062 hoặc 010 |
| R7.6.1 B9 CPD→DA_DUYET | CPD BR-OK 3 record | ✅ | HSCT000027 hoặc 063 hoặc 030 (sẽ unblock B9 R1 block) |
| R7.6.1 B12 DA_DUYET→TU_CHOI_TT | DA_DUYET BR-OK 4 record | ✅ | HSCT000031, 000034, 000064, 000071 |
| R7.7.12.2 DN bổ sung HS | YCBS BR-OK 2 + 8 sai | ✅ | HSCT000011 hoặc 000014 (file mock 5 định dạng) |
| R7.7.12.3 CB PD trả về + N:1 | CPD BR-OK 3 record + 2 CB PD | ✅ | HSCT000027/063/030 + cb_pd_tw_06+07 |
| R7.7.12 35 TC | đủ 11 trạng thái | ⚠️ | TC nào cite mã BR-correct → cần map sang HSCT pool 071-077 hoặc bg-OK list |

---

## Bảng dữ liệu verify (R2 vs R1)

| Metric | R1 (2026-05-07) | R2 (2026-05-09) | Delta |
|---|:-:|:-:|:-:|
| Total record | 78 | **108** | +30 |
| Pagination UI | "1-20 / 78 mục" | "1-20 / **108 mục**" (6 page) | +30 |
| State cover | 11/10 | 11/10 | = |
| BR-CALC-01 violations | (chưa đo) | **74/108 (68.5%)** | mới |
| HSCT000079..100 (R1 missing) | 22 thiếu | **0 thiếu** (đủ 100 + 8 R7-walk) | +22 |
| HSCT200001..030 series | (chưa thấy) | **30 record mới** | +30 |

R1 nói 78/100. R2 thấy 108. Pool đã re-seed thêm 30 record nhưng đa số vẫn vi phạm BR.

---

## Phương pháp test R2

**Tool:** Chrome DevTools MCP. **Account:** `qtht_02`.
**Setup:** Login → click sidebar "Quản lý chi trả chi phí" → React Router navigate `/chi-tra/danh-sach`.
**Verify UI:** `take_snapshot` đọc table 20 row đầu + pagination text "1-20 / 108 mục" + 6 page button.
**Verify API:** 2 lần `fetch('/api/v1/ho-so-chi-tras?tab=TAT_CA&page={1,2}&pageSize=100')` (BE chặn pageSize>100 với HTTP 422 ERR-VAL-SYS-00-01).
**BR check:** filter mỗi record qua `expected = {SIEU_NHO:100, NHO:30, VUA:10}` (theo BR-CALC-01 từ `02-thu-tu-module.md` line 735) — count violations × state.
**Pagination cap:** pageSize=200 → 422 (BE limit max 100 — confirm R1 quirk vẫn).

---

## Ảnh chụp R2

- [r7-e3-r2-pool-108-records.png](r7-e3-r2-pool-108-records.png) — UI list view 20 record đầu pool 108 (page 1/6)
- (R1) [r7-e3-chi-tra-78-records.png](r7-e3-chi-tra-78-records.png) — pool 78 ngày 2026-05-07

---

## Recommendation R2

**Pool đã đủ chạy mọi task (Bước 1-3) nhờ subset BR-OK đủ phủ B5/B9/B12 + R7.7.12.x.** KHÔNG cần re-seed thêm để chạy. NHƯNG bug BUG-CHITRA-001 phải mở rộng scope từ "4/5 R6 walk" → "74/108 toàn pool" → log update bug + tăng severity từ Major lên **Critical** (block báo cáo + KPI nếu chưa fix trước go-live).

| Option | Hành động | Effort | Khi nào |
|---|---|---|---|
| **A** | Chạy ngay Bước 1-3 với HSCT BR-OK list trên (verify-checklist này là source) | 0 phút | **Mặc định — đề xuất chính** |
| B | Đợi dev fix BUG-CHITRA-001 toàn pool 74 record | ~30-60 phút dev | Nếu cần test cả TC negative-path "BE từ chối hợp lệ" trên pool sai BR |
| C | Re-seed riêng 30 record HSCT200xxx (cluster 2) | ~30 phút | Optional — pool 108 đã thừa cho 35 TC, cluster 2 chỉ noise |

**Đề xuất:** Option A — chạy luôn với HSCT BR-OK list. BUG-CHITRA-001 expand từ 4/5 → 74/108 → severity Critical → escalate dev sau.

---

## Out of scope R2

- HSCT lifecycle workflow (CTN → DA_THANH_TOAN) — thuộc R7.6.1 Bước 1.
- HSCT permission test theo role — thuộc R7.7.12 / R7.8.5.
- DN bổ sung HS qua VNeID — thuộc R7.7.12.2 Bước 2a.
- Re-seed pool BR-correct toàn bộ — defer sau khi dev fix BUG-CHITRA-001.

R7.E3 R2 scope = verify count + state distribution + BR-CALC-01 compliance + identify BR-OK list cho Bước 1-3.

---

## R1 Kết quả (archive 2026-05-07): ⚠️ PARTIAL 78/100 (REGRESSION — thiếu 22 record HSCT000079..100)

**78 record HSCT còn** (HSCT000001..HSCT000078 contiguous, không có gap), **thiếu 22 record HSCT000079..HSCT000100** so với expected 100. Range thiếu là tail-end (079→100), không phải gap giữa — gợi ý partial deploy / partial seed / batch hard-delete cuối, không phải mất rời rạc.

**Tác động downstream:**
- ✅ R7.7.12.1 smoke regression IMPACT FR-07/08/11/13 — vẫn chạy được (78 ≥ smoke threshold).
- ⚠️ R7.7.12 Chi trả 35 TC functional — đa số chạy được (cover đủ 11 trạng thái — xem breakdown).
- ⚠️ TC nào cite cụ thể HSCT000079..100 sẽ FAIL — cần đổi mã hoặc re-seed.

---

## Bảng dữ liệu verify

| Metric | Expected | Actual | Match? |
|---|---|---|:-:|
| Total record | 100 (HSCT000001..100) | **78** (HSCT000001..078) | ❌ thiếu 22 |
| Min mã | HSCT000001 | HSCT000001 | ✅ |
| Max mã | HSCT000100 | **HSCT000078** | ❌ |
| Range contiguous | yes (no gap) | yes (001..078 không gap) | ✅ |
| Pagination UI | "1-20 / 100 mục" | "1-20 / **78 mục**" (4 page × 20) | ❌ |

### Breakdown theo trạng thái (78 record)

| Trạng thái | Count | Ghi chú |
|---|:-:|---|
| `CHO_TIEP_NHAN` | 15 | Mới nộp, chờ CB tiếp nhận |
| `DA_THANH_TOAN` | 14 | Hoàn thành flow |
| `CHO_PHE_DUYET` | 9 | Chờ CB PD ký |
| `DANG_KIEM_TRA` | 8 | Đang kiểm tra HS |
| `DANG_THAM_DINH` | 7 | Đang thẩm định nội dung |
| `DA_DUYET` | 7 | Đã duyệt, chờ TT |
| `YEU_CAU_BO_SUNG` | 6 | Trả về DN bổ sung HS |
| `DANG_DANH_GIA` | 4 | Đang đánh giá đợt |
| `TU_CHOI_THANH_TOAN` | 3 | Bị từ chối TT cuối |
| `TU_CHOI` | 3 | Từ chối toàn bộ HS |
| `HUY` | 2 | Bị hủy |

**Cover 11/10 trạng thái SM-CHI-TRA v3.5** — đủ scope test functional 35 TC R7.7.12 nếu TC dùng filter trạng thái thay vì cite mã cụ thể.

---

## Phương pháp test

**Tool:** Chrome DevTools MCP.
**Setup:** Click sidebar uid `4_13` "Quản lý chi trả chi phí" → React Router navigate `/chi-tra/danh-sach` (giữ session).
**Verify UI:** `take_snapshot` đọc 20 row table + pagination text "1-20 / 78 mục" + 4 trang button.
**Verify API:** `evaluate_script` chạy `fetch('/api/v1/ho-so-chi-tras?tab=TAT_CA&page=1&pageSize=100')` — endpoint thực phát hiện qua `list_network_requests` reqid=640.
**Sample verify:** sort theo mã → confirm contiguous 001..078, không gap; min=HSCT000001 ✅, max=HSCT000078 (≠ HSCT000100 expected).
**Pagination cap:** pageSize=200 → 422 (BE limit max 100).

---

## Ảnh chụp

- [r7-e3-chi-tra-78-records.png](r7-e3-chi-tra-78-records.png) — UI list view 20 record đầu + pagination "1-20 / 78 mục" (4 page).

---

## Recommendation

| Option | Hành động | Effort | Khi nào dùng |
|---|---|---|---|
| **A** | Giữ 78 record, run R7.7.12 với scope state-based (không cite mã cụ thể) | 0 phút | Nếu TC R7.7.12 không strict cite HSCT000079+ |
| **B** | Re-seed 22 HSCT (HSCT000079..100) qua self-reg DN flow | ~30 phút (5 DN × 4-5 HSCT mỗi DN qua /api/v1/ho-so-chi-tras POST) | Nếu cần đúng 100 cho parity với baseline |
| **C** | Log bug seed gap + escalate dev re-deploy seed script | 5 phút log | Nếu xác định 22 record bị mất do partial deploy chứ không phải initial seed = 78 |

**Đề xuất:** Option A trước (chạy R7.7.12 + R7.7.12.1 với 78 HSCT đã có), nếu fail TC nào do thiếu state coverage thì mới Option B/C.

---

## Out of scope (không test trong R7.E3)

- HSCT lifecycle workflow (CHO_TIEP_NHAN → DA_THANH_TOAN) — thuộc R7.6.1.
- HSCT permission test theo role — thuộc R7.7.12 / R7.8.5.
- DN bổ sung HS qua VNeID — thuộc R7.7.12.2.

R7.E3 scope = chỉ verify count + range mã HSCT (data readiness check).

---

*2026-05-07 17:35 — QA huongttt chạy bằng Chrome DevTools MCP, account qtht_02.*
