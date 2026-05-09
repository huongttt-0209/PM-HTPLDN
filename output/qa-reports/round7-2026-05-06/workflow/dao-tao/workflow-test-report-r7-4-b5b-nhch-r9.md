# Workflow Test Report — NHCH State Machine (R7.4.B5b — R9 re-verify)

> **Module:** Workflow NHCH (FR-III-09 SM-NHCH) · **SRS:** [`srs-fr-03-dao-tao.md FR-III-09`](../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-09) · **Round:** R9 · **Date:** 2026-05-09 22:18 · **Tester:** QA Automation Claude Code MCP

---

## Kết luận

✅ **N/A confirmed (R9 re-verify) — workflow original `NHAP→CONG_KHAI→AN` KHÔNG tồn tại trong impl. Replacement workflow toggle `KICH_HOAT/VO_HIEU_HOA` PASS.**

R9 re-verify pattern đã verified ở R7-R8 — không có thay đổi. Spec drift `FR-III-09 line 783` (3 state) vs `Entity §3.4.3.21 row 9` (2 state) vẫn còn — cần BA update SRS doc-side.

---

## R9 verify steps

### 1. Probe legacy endpoints (confirm KHÔNG tồn tại workflow gốc)

```
POST /api/v1/ngan-hang-cau-hois/{id}/publish     → 404
POST /api/v1/ngan-hang-cau-hois/{id}/cong-khai   → 404
POST /api/v1/ngan-hang-cau-hois/{id}/an          → 404
```

→ 3/3 endpoint cho transition `NHAP→CONG_KHAI→AN` đều 404. Workflow gốc theo SRS `FR-III-09 Inputs row 7` KHÔNG IMPLEMENT.

### 2. Test PATCH toggle replacement (KICH_HOAT ↔ VO_HIEU_HOA)

| Step | Action | State trước | State sau | Version | Status |
|:-:|---|:--:|:--:|:--:|:-:|
| 1 | PATCH `{trangThai:VO_HIEU_HOA, version:2}` | KICH_HOAT (v2) | VO_HIEU_HOA (v3) | v3 | ✅ 200 |
| 2 | PATCH `{trangThai:KICH_HOAT, version:3}` | VO_HIEU_HOA (v3) | KICH_HOAT (v4) | v4 | ✅ 200 |

→ Toggle 2 chiều PASS. State machine 2 state confirmed (không phải 3 state như SRS FR-III-09).

**Sample:** NHCH-SHTT-Trung bình-TN nhiều R9 (id `1ac5596e-33e8-4b54-b6f8-607cb4d22659`) — toggle về KICH_HOAT cuối, không leak state cho downstream.

---

## Spec drift vẫn còn (chưa fix R9)

| Source | State machine quy định |
|---|---|
| SRS `FR-III-09 line 783` Inputs row 7 | `NHAP / CONG_KHAI / AN` (3 state) |
| SRS `Entity §3.4.3.21 row 9` | `KICH_HOAT / VO_HIEU_HOA` (2 state) |
| BE impl actual | `KICH_HOAT / VO_HIEU_HOA` (match Entity, không match Inputs) |

→ FR-III-09 line 783 typo copy-paste từ SM-BIEUMAU C.9. Cần BA cập nhật sync về Entity §3.4.3.21.

**Bug ref:** BUG-SRS-NHCH-STATE-01 — Closed FE side 2026-05-07 (form default KICH_HOAT đúng). SRS doc-side chưa fix.

---

## Lịch sử round

| Round | Date | Kết quả |
|---|---|---|
| R6 | 2026-04 | Workflow gốc 3 state quy định trong task — chưa test |
| R7-R8 | 2026-05-06/08 | Closed N/A do spec contradiction. Replacement toggle verified R7.3.8 R8 PATCH 5/5 |
| R9 | 2026-05-09 | ✅ Re-verify N/A — endpoint /publish + /cong-khai + /an all 404, PATCH toggle 2 chiều PASS |

---

## Bằng chứng

```js
// Probe legacy endpoints
POST /ngan-hang-cau-hois/{id}/publish    → 404
POST /ngan-hang-cau-hois/{id}/cong-khai  → 404
POST /ngan-hang-cau-hois/{id}/an         → 404

// Replacement workflow
PATCH /ngan-hang-cau-hois/1ac5596e... {trangThai:VO_HIEU_HOA, version:2} → 200, version=3
PATCH /ngan-hang-cau-hois/1ac5596e... {trangThai:KICH_HOAT, version:3}   → 200, version=4
```

---

*R9 re-verify | QA Automation via Claude Code | 2026-05-09 22:18 — API direct mode*
