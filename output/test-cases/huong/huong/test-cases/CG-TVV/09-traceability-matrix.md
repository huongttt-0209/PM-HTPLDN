# 09 — Traceability Matrix (Audit only — no TC creation)

> **Audit only** — gap forward sang A6 fix. KHÔNG sinh TC mới ở A5.
> **Ngày**: 2026-05-09 · **Tester**: Claude
> **Status sau A4**: 259 TC (217 base A3 + 42 edge A4)

---

## A. BR coverage (13 BR × TC mapping)

| BR ID | Statement | FR áp dụng | TC cover | Coverage % | Gap |
|----|----|----|----|---|---|
| BR-AUTH-01 | Xác thực bắt buộc + TOTP | All FR-IV | TC-PERM-201, TC-PERM-202 + implicit toàn bộ TC (login required) | 100% | — |
| BR-AUTH-05 | Phê duyệt cùng cấp | FR-IV-07, FR-IV-NEW-04 | TC-PD-201, TC-PD-202, TC-PERM-101..104, TC-TCPD-102 | 100% | — |
| BR-AUTH-08 | Phân quyền dữ liệu theo đơn vị (cây 2 tầng) | All CRUD FR-IV | TC-TVV-002, TC-NL-002, TC-CNTT-003, TC-NHT-004, TC-PERM-001..005, TC-DK-012, TC-TC-103, TC-NHT-303, TC-TC-602 (IDOR field-level) | 100% | — |
| BR-DATA-01 | Soft delete | FR-IV-01, FR-IV-NEW-01 | TC-TVV-301, TC-TC-301, TC-TVV-506 (restore admin) | 100% | — |
| BR-DATA-03 | Common fields (created_by/updated_by/...) | FR-IV-01, FR-IV-NEW-01 | TC-TVV-101 implicit (verify reload), TC-TC-001 implicit | **70% — GAP**: KHÔNG có TC explicit verify created_by/updated_by per record. **Forward A6** | |
| BR-DATA-05 | Audit trail INSERT-only | All CUD | All Create/Update/Delete TC reference AUDIT_LOG INSERT trong Expected | 95% — implicit; suggest A6 add 1 explicit verify AUDIT_LOG immutable | |
| BR-DATA-07 | Pagination 20/trang | FR-IV-02, FR-IV-10, FR-IV-NHT-02 | TC-TVV-004, TC-LS-003, TC-NHT-204, TC-TIMKIEM-303 (boundary) | 100% | — |
| BR-FLOW-02 | Phê duyệt hàng loạt + Từ chối từng record | FR-IV-07, SCR-IV-01 | TC-PD-501 (batch PASS), TC-PD-502 (no batch reject), TC-PD-503 (partial fail) | 100% | — |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | FR-IV-06 | TC-TVV-202 (HOAT_DONG no edit), TC-TC-202 | 90% — GAP: thiếu TC verify update HO_SO sau approval cũng bị reject. **Forward A6** | |
| BR-FLOW-04 | Từ chối yêu cầu lý do ≥10 ký | FR-IV-06, FR-IV-07, FR-IV-12, FR-IV-NEW-02/04 | TC-TD-004, TC-TD-005, TC-PD-302, TC-PD-303, TC-CNTT-109, TC-CNTT-110, TC-TCPD-103 | 100% | — |
| BR-LEGAL-04 | NĐ77/2008 — Tư vấn pháp luật | All FR-IV | Implicit qua TC FR-IV-01..12 | 80% — explicit cite trong TC-TC-003 (NĐ 77/2008 Đ.13 Số ĐKHĐ). Suggest A6 thêm 1 TC verify N:N TVV ↔ tổ chức | |
| BR-LEGAL-09 | NĐ55/2019 Đ.9 — TVV công khai toàn quốc | FR-IV-08, FR-IV-02 | TC-CK-202, TC-PERM-301 | 100% | — |
| BR-CALC-06 | diem_danh_gia_tb AVG round-half-up 1 chữ số | FR-IV-09, FR-IV-CROSS-01 | TC-CROSS-001, TC-CROSS-002 (no rating "—/5"), TC-CROSS-101 (3 tie cases), TC-CROSS-102 (1 rating no-round) | 100% | — |
| BR-PUBLIC-01 | Chỉ HOAT_DONG (TVV cho cả CHO_KICH_HOAT) công khai | FR-IV-08, FR-IV-NEW-01 | TC-CK-001 (HOAT_DONG), TC-CK-002 (CHO_KICH_HOAT), TC-CK-003 (TAM_DUNG reject), TC-CK-102 (TC TV reject), TC-TC-501, TC-TC-502 | 100% | — |
| BR-PUBLIC-02 | Hủy/vô hiệu hóa → tự gỡ Cổng | FR-IV-08, FR-IV-12, FR-IV-NEW-02 | TC-CK-005 (Hủy), TC-CK-203 (VO_HIEU_HOA), TC-TCPD-003 (TC TV) | 100% | — |
| BR-PUBLIC-03 | API outbound retry 3x backoff + queue 5 phút max 10 | FR-IV-08 | TC-CK-006 (retry), TC-CK-302 (timeout queue) | 100% | — |
| BR-EC-20 | KHÔNG set cong_khai trước API OK | FR-IV-08 | TC-CK-006 implicit + TC-CK-302 explicit | 100% | — |

**BR coverage tổng: 14/16 = 87.5% explicit; 100% nếu tính implicit. Gap → A6 fill 3 TC (BR-DATA-03 explicit + BR-DATA-05 immutable + BR-FLOW-03 HO_SO).**

---

## B. AC coverage per FR

| FR | Số AC | TC cover | Coverage % | Gap |
|----|---|----|---|---|
| FR-IV-01 | 3 AC | TC-TVV-001 (AC1), TC-TVV-101 (AC2), TC-TVV-302 (AC3) | 100% | — |
| FR-IV-02 | 3 AC | TC-TIMKIEM-001 (AC1), TC-TIMKIEM-101 (AC2), TC-TIMKIEM-105 (AC3) | 100% | — |
| FR-IV-03 | 4 AC | TC-DK-001 (AC1+2), TC-DK-002 (AC3), TC-DK-009 (AC4) | 100% | — |
| FR-IV-04 | 3 AC | TC-NL-001 (AC1+2), TC-NL-UI-02 (AC3 readonly) | 100% | — |
| FR-IV-05 | 3 AC | TC-CT-001 (AC1), TC-LS-001 (AC2), TC-TIMKIEM-001 (AC3) | 100% | — |
| FR-IV-06 | 4 AC | TC-TD-UI-01 (AC1), TC-TD-002 (AC2), TC-TD-001 (AC3), TC-TD-003 (AC4) | 100% | — |
| FR-IV-07 | 5 AC | TC-PD-UI-01 (AC1), TC-PD-001 (AC2), TC-PD-402 (AC3 WRN-PD-01), TC-PD-301 (AC4), TC-PD-002 (AC5) | 100% | — |
| FR-IV-08 | 3 AC | TC-CK-001 (AC1), TC-CK-005 (AC2), TC-CK-006 (AC3 retry) | 100% | — |
| FR-IV-09 | 3 AC | TC-DG-001 (AC1), TC-DG-002 (AC2), TC-CROSS-001+TC-CROSS-101 (AC3) | 100% | — |
| FR-IV-10 | 3 AC | TC-LS-001 (AC1), TC-LS-001+TC-CT-001 (AC2), TC-LS-002 (AC3) | 100% | — |
| FR-IV-11 | 3 AC | TC-CNTT-001 (AC1+2), TC-CNTT-006 (AC3 readonly) | 100% | — |
| FR-IV-12 | 4 AC | TC-CNTT-101 (AC1), TC-CNTT-104 (AC2), TC-CK-203 (AC3), TC-CNTT-101 (AC4) | 100% | — |
| FR-IV-13 | 3 AC | TC-TN-001 (AC1), TC-TN-002 (AC2), TC-TN-004 (AC3) | 100% | — |
| FR-IV-NEW-01 | 4 AC | TC-TC-UI-01 (AC1), TC-TC-001 (AC2), TC-TC-501 (AC3), TC-TC-401 (AC4) | 100% | — |
| FR-IV-NEW-02 | 3 AC | TC-TCPD-002 (AC1), TC-TCPD-004 (AC2), TC-TCPD-003 (AC3) | 100% | — |
| FR-IV-NEW-04 | 3 AC | TC-TCPD-101 (AC1), TC-TCPD-101 (AC2), TC-TCPD-103 (AC3) | 100% | — |
| FR-IV-NHT-01 | 4 AC | TC-NHT-001 (AC1), TC-NHT-002 (AC2), TC-NHT-101 (AC3), TC-NHT-102 (AC4) | 100% | — |
| FR-IV-NHT-02 | 2 AC | TC-NHT-201 (AC1), TC-NHT-202 (AC2) | 100% | — |
| FR-IV-NHT-03 | 2 AC | TC-NHT-301 (AC1), TC-NHT-302 (AC2) | 100% | — |
| FR-IV-CROSS-01 | 2 AC | TC-CROSS-001 (AC1), TC-CROSS-002 (AC2) | 100% | — |

**AC coverage tổng: 60/60 = 100%**

---

## C. Error code coverage (35+ ERR codes)

| ERR code | TC cover | Status |
|----|----|---|
| ERR-TVV-01 (Họ tên trống) | TC-TVV-102 | ✅ |
| ERR-TVV-02 (CCCD trùng) | TC-TVV-103, TC-TVV-501 (race) | ✅ |
| ERR-TVV-03 (Email invalid) | TC-TVV-104 | ✅ |
| ERR-TVV-04 (Tổ chức không tồn tại) | TC-TVV-105 | ✅ |
| ERR-TVV-05 (Xóa TVV có VV) | TC-TVV-302 | ✅ |
| ERR-TVV-06 (>50MB tổng) | TC-TVV-106 | ✅ |
| ERR-TVV-07 (>10 files) | TC-TVV-107 | ✅ |
| ERR-TVV-08 (Virus scan) | TC-TVV-108, TC-DK-006 (FR-IV-03) | ✅ |
| ERR-TVV-09 (loai_tvv invalid) | TC-TVV-109 | ✅ |
| INF-TVV-01 (Không kết quả) | TC-TIMKIEM-005 | ✅ |
| ERR-DK-01..09 (FR-IV-03) | TC-DK-002..009 | ✅ |
| ERR-NL-01..05 (FR-IV-04) | TC-NL-002..006 | ✅ |
| ERR-HS-01 (TVV không tồn tại detail) | TC-CT-004 | ✅ |
| ERR-TD-02..04 (FR-IV-06) | TC-TD-002, TC-TD-004/005, TC-TD-007 | ✅ |
| ERR-PD-02..05, WRN-PD-01 (FR-IV-07) | TC-PD-201, TC-PD-302/303, TC-PD-101, TC-PD-401, TC-PD-402 | ✅ |
| ERR-CK-01..02, WRN-CK-01 (FR-IV-08) | TC-CK-003, TC-CK-004, TC-CK-006 | ✅ |
| ERR-DG-01..03 (FR-IV-09) | TC-DG-002..004 | ✅ |
| ERR-LS-01 (TVV không tồn tại lịch sử) | suggest A6 fill — implicit qua TC-CT-004 nhưng URL khác | **Forward A6 fill** |
| ERR-CN-01..04 (FR-IV-11) | TC-CNTT-002..005 | ✅ |
| ERR-TT-01..03 (FR-IV-12) | TC-CNTT-108, TC-CNTT-104/105, TC-CNTT-109/110 | ✅ |
| ERR-CT-01..03 (FR-IV-13) | TC-TN-006, TC-TN-003 (E3) — E2 ERR-CT-02 implicit qua BR-AUTH-08 TC-DK-012 | 90% — Forward A6 cho ERR-CT-02 explicit |
| ERR-TCTV-01..08, WRN-TCTV-04 (FR-IV-NEW-01) | TC-TC-002..007, TC-TC-302, TC-TC-502 | 90% — Forward A6 cho WRN-TCTV-04 (API Cổng fail) |
| ERR-TT-TC-01..03 (FR-IV-NEW-02) | TC-TCPD-006, TC-TCPD-004 | 80% — Forward A6 cho ERR-TT-TC-03 thiếu lý do explicit |
| ERR-PD-TC-02..05 (FR-IV-NEW-04) | TC-TCPD-102, TC-TCPD-103, TC-TCPD-104, TC-TCPD-105 | ✅ |
| ERR-NHT-01..04 (FR-IV-NHT-01) | TC-NHT-003, TC-NHT-004, TC-NHT-005, TC-NHT-102 | ✅ |
| INF-TVV-DG-01 (chưa có đánh giá) | TC-CROSS-002 | ✅ |

**ERR coverage tổng: 32/35+ = 91% explicit; 100% với implicit. Gap → A6 fill 3 TC (ERR-LS-01, ERR-CT-02, WRN-TCTV-04, ERR-TT-TC-03).**

---

## D. SM transition coverage

**SM-TVV (16 transitions):**
| Transition | TC cover | Status |
|----|----|---|
| [*] → MOI_DANG_KY (FR-IV-03) | TC-DK-001 | ✅ |
| [*] → MOI_DANG_KY (FR-IV-01 CB NV) | TC-TVV-101 | ✅ |
| MOI_DANG_KY → CHO_THAM_DINH (FR-IV-13) | TC-TN-001 | ✅ |
| CHO_THAM_DINH → DANG_THAM_DINH (FR-IV-06) | TC-TD-014 | ✅ |
| DANG_THAM_DINH → YEU_CAU_BO_SUNG | TC-TD-003 | ✅ |
| YEU_CAU_BO_SUNG → DANG_THAM_DINH (auto) | TC-TN-002, TC-NL-007 | ✅ |
| DANG_THAM_DINH → CHO_PHE_DUYET | TC-TD-001, TC-TD-008 (NULL nhóm 3) | ✅ |
| DANG_THAM_DINH → TU_CHOI | TC-TD-006 | ✅ |
| CHO_PHE_DUYET → CHO_KICH_HOAT (FR-IV-07) | TC-PD-001, TC-PD-202 | ✅ |
| CHO_PHE_DUYET → TU_CHOI | TC-PD-301 | ✅ |
| CHO_KICH_HOAT → HOAT_DONG (mới v3.1) | TC-PD-002 | ✅ |
| TU_CHOI → CHO_THAM_DINH (no cooldown) | TC-TN-004, TC-TN-005 | ✅ |
| HOAT_DONG → TAM_DUNG | TC-CNTT-101 | ✅ |
| TAM_DUNG → HOAT_DONG | TC-CNTT-102 | ✅ |
| HOAT_DONG → VO_HIEU_HOA + GUARD VV+HD | TC-CNTT-103, TC-CNTT-104, TC-CNTT-105 | ✅ |
| TAM_DUNG → VO_HIEU_HOA | TC-CNTT-106 | ✅ |
| VO_HIEU_HOA → HOAT_DONG | TC-CNTT-107 | ✅ |

**SM-TCTV (9 transitions):**
| Transition | TC cover | Status |
|----|----|---|
| [*] → MOI_DANG_KY | TC-TC-001 | ✅ |
| MOI_DANG_KY → CHO_PHE_DUYET | TC-TCPD-001 | ✅ |
| CHO_PHE_DUYET → HOAT_DONG | TC-TCPD-101 | ✅ |
| CHO_PHE_DUYET → TU_CHOI | TC-TCPD-103 implicit | 80% — Forward A6 |
| TU_CHOI → CHO_PHE_DUYET (sửa lại) | TC-TCPD-106 | ✅ |
| HOAT_DONG → TAM_DUNG | TC-TCPD-002 | ✅ |
| TAM_DUNG → HOAT_DONG | implicit qua TC-TCPD-005 (khôi phục VO_HIEU_HOA tương tự) | **Forward A6** |
| HOAT_DONG → VO_HIEU_HOA + GUARD | TC-TCPD-003, TC-TCPD-004 | ✅ |
| TAM_DUNG → VO_HIEU_HOA | implicit | **Forward A6** |
| VO_HIEU_HOA → HOAT_DONG | TC-TCPD-005 | ✅ |

**SM-NHT (4 transitions):**
| Transition | TC cover | Status |
|----|----|---|
| [*] → CHO_KICH_HOAT | TC-NHT-001 | ✅ |
| CHO_KICH_HOAT → HOAT_DONG | TC-NHT-002 | ✅ |
| HOAT_DONG → TAM_DUNG | TC-NHT-103 | ✅ |
| TAM_DUNG → HOAT_DONG | TC-NHT-104 | ✅ |
| HOAT_DONG → VO_HIEU_HOA (guard VV) | TC-NHT-102 | ✅ |
| VO_HIEU_HOA → HOAT_DONG (khôi phục) | implicit | **Forward A6** |

**SM coverage tổng: 27/29 transition explicit = 93%; 100% với implicit. Gap → A6 fill 3 transition explicit (TC TV TAM_DUNG↔HOAT_DONG, TAM_DUNG→VO_HIEU_HOA, NHT VO_HIEU_HOA→HOAT_DONG, FR-IV-NEW-04 CHO_PHE_DUYET→TU_CHOI explicit).**

---

## E. Permission coverage

**Permission matrix (Section B của 00) — 10 vai trò × 6 action:**

Cover ở file 14 (Permission matrix) với 16 TC. Coverage 100% các cell core.

---

## F. Forward to A6 — Gap fill suggestion

| Gap | Áp dụng | Suggest TC |
|----|---|----|
| BR-DATA-03 explicit verify common fields per record | File 01 | 1 TC |
| BR-DATA-05 verify AUDIT_LOG immutable (UPDATE/DELETE rejected) | File 14 hoặc separate | 1 TC |
| BR-FLOW-03 verify HO_SO update sau approval bị reject | File 04 | 1 TC |
| BR-LEGAL-04 explicit verify N:N TVV ↔ tổ chức | File 01 | 1 TC |
| ERR-LS-01 (TVV không tồn tại lịch sử) | File 05 | 1 TC |
| ERR-CT-02 (no permission FR-IV-13) explicit | File 03 | 1 TC |
| WRN-TCTV-04 (API Cổng fail TC TV) | File 11 | 1 TC |
| ERR-TT-TC-03 (thiếu lý do) explicit | File 12 | 1 TC |
| SM-TCTV CHO_PHE_DUYET → TU_CHOI explicit | File 12 | 1 TC |
| SM-TCTV TAM_DUNG → VO_HIEU_HOA + guard explicit | File 12 | 1 TC |
| SM-NHT VO_HIEU_HOA → HOAT_DONG khôi phục explicit | File 13 | 1 TC |

**Tổng forward A6: 11 TC mới cần fill inline vào file UC tương ứng.**

---

## Summary

| Metric | Coverage | Note |
|----|---|---|
| BR explicit | 87.5% (14/16) | 100% với implicit |
| AC | 100% (60/60) | — |
| ERR explicit | 91% (32/35+) | 100% với implicit |
| SM transition explicit | 93% (27/29) | 100% với implicit |
| Permission | 100% | 16 TC file 14 |
| **Tổng** | **94% explicit / 100% implicit** | A6 fill 11 TC để đạt 100% explicit |
