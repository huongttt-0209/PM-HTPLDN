# Test Plan Overview — FR-01 Dashboard (Nhóm I)

> **Module:** FR-01 Dashboard (Nhóm I)
> **SRS:** `input/srs-v3/srs-fr-01-dashboard-v3.1.md` (v3.5, 1167 lines)
> **Phase:** A — Phase A của detailed-tc plan §3.1 (BMAD A1-A7 manual variant)
> **Tester:** QA Automation Lead
> **Generated:** 2026-05-10 (Phase A2)
> **Wave:** W5.3 (LỚP 5 — Tổng hợp & Đầu ra)

---

## 1. Phạm vi

**11 FR + 1 SCR + 5 BR + 9 entity referenced**

| Loại | Mã | Tên | Test File |
|------|----|----|-----------|
| FR | FR-I-01 | Tổng hợp hỏi đáp (KPI-01) | `01-TC-FR-I-01-04-vu-viec-hoi-dap.md` |
| FR | FR-I-02 | Vụ việc đã tiếp nhận (KPI-02) | `01-TC-FR-I-01-04-vu-viec-hoi-dap.md` |
| FR | FR-I-03 | Vụ việc đang hỗ trợ (KPI-03) — **ảnh chụp** 5 enum sống | `01-TC-FR-I-01-04-vu-viec-hoi-dap.md` |
| FR | FR-I-04 | Vụ việc đã hoàn thành (KPI-04) | `01-TC-FR-I-01-04-vu-viec-hoi-dap.md` |
| FR | FR-I-05 | Khóa học đang diễn ra (KPI-05) — **ảnh chụp** | `02-TC-FR-I-05-07-khoa-hoc-tvv.md` |
| FR | FR-I-06 | Khóa học đã kết thúc (KPI-06) | `02-TC-FR-I-05-07-khoa-hoc-tvv.md` |
| FR | FR-I-07 | TVV/CG/NHT đang hoạt động (KPI-07) — **ảnh chụp** | `02-TC-FR-I-05-07-khoa-hoc-tvv.md` |
| FR | FR-I-08 | UC8 — 2 biểu đồ cột song song (Đánh giá hiệu quả + SLA) | `03-TC-FR-I-08-bieu-do-danh-gia-sla.md` |
| FR | FR-I-09 | UC9 — Biểu đồ vành (Chất lượng đào tạo) | `04-TC-FR-I-09-bieu-do-dao-tao.md` |
| KPI-S | KPI-S-01 | Tỷ lệ vụ việc phải bổ sung | `05-TC-KPI-S-bo-sung.md` |
| KPI-S | KPI-S-02 | Thời gian xử lý trung bình (ngày làm việc) | `05-TC-KPI-S-bo-sung.md` |
| FR | FR-I-CROSS-02 | Auto-refresh 60s + per-widget fail isolation | `06-TC-FR-I-CROSS-02-auto-refresh.md` |
| SCR | SCR-I-01 Vùng 1+2 | Tiêu đề + Bộ lọc (Năm + Tháng + L1 + L2) | `07-TC-SCR-I-01-bo-loc-header.md` |
| Permission | P1-P8 | Ma trận phân quyền 8×12 | `08-TC-permission-matrix.md` |

**OUT of scope:**
- Drill-down chi tiết module target (đó là test của Nhóm II/III/IV/V — chỉ test redirect URL ở đây)
- Chi tiết tính toán BR-CALC-03 (test ở Nhóm VIII / FR-VIII-29 ngày lễ)
- Design system: màu/icon cụ thể (đội thiết kế UI quyết — chỉ test semantic state)

---

## 2. Test Approach

**Loại test:**
- **Functional happy path** — KPI/biểu đồ render đúng giá trị
- **Negative** — error handling (E1/E2/E3 INFO-DASH-01/02/04 + ERR-DASH-02)
- **Edge** — boundary giá trị (kỳ trước = 0, mẫu N < 10, audit log thiếu, kỳ đóng vs hiện tại)
- **Permission** — BR-AUTH-08 scope theo đơn vị + 8 quyền P1-P8 cho 12 vai trò
- **Behavior** — auto-refresh 60s + tab visibility + filter pending/apply
- **Drill-down URL** — ✅ chỉ verify URL params đúng spec, KHÔNG vào module target test sâu

**Tools:**
- chrome-devtools MCP (headless mode)
- Login OTP=666666
- App URL `http://103.172.236.130:3000/`
- Tài khoản test trong `users.csv` (Secret@123 cho mọi user)

---

## 3. Quy ước số TC

- **Priority:** 🔴 P0 (critical) · 🟡 P1 (high) · 🟢 P2 (medium)
- **Test type:** Happy / Negative / Edge / Permission / Behavior / DrillDown
- **TraceID:** `FR-I-{NN} / {section}` link SRS line/heading
- **TC ID:** `TC-DASH-{NNN}` chạy số liên tục

---

## 4. Account Map (per Permission Matrix SCR-I-01)

| Vai trò | username (primary) | don_vi_id |
|---------|--------------------|-----------|
| QTHT | `qtht_01` | (no don_vi_id, see all) |
| CB_NV_TW | `cb_nv_tw_01` | BTP-TW |
| CB_NV_BN | `cb_nv_bn_01` | BKH (Bộ KH&ĐT) |
| CB_NV_DP | `cb_nv_dp_01` | STP-AG (Sở TP An Giang) |
| CB_PD_TW | `cb_pd_tw_01` | BTP-TW |
| CB_PD_BN | `cb_pd_bn_01` | BKH |
| CB_PD_DP | `cb_pd_dp_01` | STP-AG |
| DN | `dn_01` | (Cổng DN — không có DASHBOARD_VIEW) |
| NHT | `nht_01` | (Form public — không có DASHBOARD_VIEW) |
| TVV | `tvv_01` | (Form public — không có DASHBOARD_VIEW) |
| CG | `cg_01` | (Form public — không có DASHBOARD_VIEW) |

---

## 5. Business Rules áp dụng (5 BR)

| BR | Phát biểu (tóm tắt) | TC apply |
|----|---------------------|----------|
| BR-AUTH-01 | Xác thực bắt buộc (Tier 1 nội bộ + Tier 2 SSO VNeID) — không có VNPT eKYC | TC permission login |
| BR-AUTH-03 | Ngang cấp không thấy nhau (BN ≠ ĐP, DP ≠ DP khác) | TC scope cross-unit |
| BR-AUTH-04 | TW thấy cấp con (BN + ĐP ngang cấp song song) | TC TW scope |
| BR-AUTH-08 | Scope dữ liệu theo `don_vi_id` mọi entity có cột này | Mọi KPI/chart |
| BR-SLA-05 | Tỷ lệ tuân thủ SLA = HT đúng hạn / (HT + đang xử lý quá hạn) — tránh tỷ lệ ảo | UC8 phải |
| BR-CALC-03 | Deadline = ngày làm việc (T2-T6, trừ ngày lễ FR-VIII-29) | KPI-S-02 |

---

## 6. State Machine (read-only, không own)

| SM | Entity | Dùng cho KPI |
|----|--------|--------------|
| SM-HOIDAP | HOI_DAP | KPI-01 (count `MOI`) |
| SM-VUVIEC | VU_VIEC | KPI-02 (count tiếp nhận) / KPI-03 (5 sống) / KPI-04 (`HOAN_THANH`) |
| SM-KHOAHOC | KHOA_HOC | KPI-05 (`DANG_DIEN_RA`) / KPI-06 (`DA_KET_THUC`) |
| SM-TVV | TU_VAN_VIEN | KPI-07 (`DANG_HOAT_DONG`) |

> Dashboard KHÔNG sở hữu state machine — chỉ tổng hợp.

---

## 7. Error codes (3 Info + 1 Error)

| Code | Severity | Trigger | UI |
|------|----------|---------|----|
| INFO-DASH-01 | INFO | Không có dữ liệu KPI | "0" + "Chưa có dữ liệu trong kỳ" |
| INFO-DASH-02 | INFO | Không có dữ liệu UC8 | Biểu đồ trống + caption |
| INFO-DASH-03 | INFO | Không có dữ liệu UC9 | Donut trống + caption |
| INFO-DASH-04 | INFO | Audit log thiếu kỳ trước | xu_huong=NULL → UI "—" + tooltip "Chưa đủ dữ liệu lịch sử" |
| ERR-DASH-02 | ERROR | DB/API 5xx → widget hỏng | Trạng thái 28 — "Không tải được dữ liệu" + nút "Thử lại" cục bộ widget (không toast/modal toàn trang) |

---

## 8. Coverage targets

| Loại coverage | Target | Đo bằng |
|---------------|--------|---------|
| BR | 100% (5/5) | A5 traceability |
| AC | ≥97% | A5 traceability |
| Permission Matrix | 100% (8 quyền × 12 vai trò = 96 cells; 8×7=56 cells effective) | A5 |
| Error code | 100% (5/5) | A5 |
| State enum source | 100% — KPI mapping enum đúng | A4 + A5 |
| Inputs (Năm/Tháng/L1/L2) | 100% boundary | A4 edge case |
| Outputs (12 fields TPL-DASH-KPI + UC8/9 specific) | 100% — verify field xuất hiện trên UI | A6 |

---

## 9. Estimate

| File | UC scope | TC base (A3) | A4 edge | A6 fill | Total ước |
|------|----------|--------------|---------|---------|-----------|
| 01-TC | KPI-01..04 (HD + VV) | 14 | +5 | +2 | ~21 |
| 02-TC | KPI-05..07 (KH + TVV) | 12 | +4 | +2 | ~18 |
| 03-TC | UC8 (2 biểu đồ cột) | 14 | +5 | +2 | ~21 |
| 04-TC | UC9 (donut) | 9 | +3 | +1 | ~13 |
| 05-TC | KPI-S-01/02 | 9 | +3 | +1 | ~13 |
| 06-TC | Auto-refresh 60s + per-widget fail | 14 | +4 | +2 | ~20 |
| 07-TC | SCR-I-01 Bộ lọc + Header | 16 | +5 | +2 | ~23 |
| 08-TC | Permission 8×7 active roles | 14 | +2 | +1 | ~17 |
| **Tổng** | | **102** | **+31** | **+13** | **~146** |

**vs estimate todo.md (~40 TC):** Cao hơn nhiều — do SRS v3.5 có 30 UI components + 5 BR + per-widget fail + filter pending/apply rich behavior + Permission Matrix 7 active roles (4 dropped: DN/NHT/TVV/CG có sẽ test redirect).

> **Note:** Sau A7 filter loại TC chỉ-DB-thuần + /codex review apply có thể tăng/giảm 10-20 TC.

---

## 10. Risk & Mitigation

| Risk | Mitigation |
|------|-----------|
| Khó verify "Audit log không đủ kỳ trước" trên prod env (E2 INFO-DASH-04) | Mark **OBS** + SPEC-CLARIFY-DASH-AUDIT, không block ship; verify qua 1 vài KPI thực có/không có audit |
| Auto-refresh 60s khó stabilize trong test (timing race) | Polling-based assertion với window ±5s; pause/resume tab visibility test cần `evaluate_script` Page Visibility API |
| Per-widget fail isolation cần stub backend lỗi 5xx — không có hook backend dev | Mark scenario "stub server" → **DEFERRED** chờ dev cung cấp hoặc dùng Chrome DevTools network throttling |
| Filter URL params invalid → silently fallback default | Edge test với URL params crafted (year out of range, don_vi_id không tồn tại) |
| Drill-down URL test sâu module target = blow scope | **OUT scope** — chỉ verify URL params chính xác, không test module target |

---

## 11. SPEC-CLARIFY pending (sẽ phát hiện trong A4-A6)

> Reserved cho Phase A4-A7 + Codex.
> Format: `SPEC-CLARIFY-DASH-{NN}` — cross-ref bug-report khi Phase B.

---

*Generated 2026-05-10 — Phase A2 (test-plan-overview)*
