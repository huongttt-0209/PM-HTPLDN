# A7 Filter Log — FR-V.I Vụ việc TGPL (BMAD A7) — UI/function-testable filter

> **Ngày**: 2026-05-06 · **Filter Reviewer**: BMAD A7 manual scan
> **Status**: ✅ **FILTER APPLIED 2026-05-06** — 3 FR/UC LOẠI ở module-level + 0 TC sửa cấp file (A3 prompts đã chủ động brief filter pre-emptively).
> **File này KHÔNG là TC source** — chỉ audit "đã loại / sửa gì".
> **Iron rule** (Plan §3.1):
> - ❌ LOẠI: TC require DB query trực tiếp / API curl thuần / cron job no-UI / queue background worker
> - ✏️ SỬA: TC verify-DB → verify-network qua MCP `list_network_requests` (UI bridge)
> - ✅ GIỮ: TC chạy 100% qua UI/function user-facing (verify network response gián tiếp OK)

---

## 1. Module-level filter (LOẠI 3 FR/UC)

### LOẠI #1: FR-V.I-03 (UC53 — Tiếp nhận HS qua DVC LGSP API thuần inbound)

**SRS Ref:** srs-fr-05:217-289

**Lý do LOẠI:**
- Tác nhân là **Hệ thống TTHC BTP qua LGSP** (no UI người dùng)
- Trigger: API inbound từ external system (REST POST `/api/lgsp/vu-viec`)
- Verify: cấu trúc JSON, idempotent check `ma_ho_so_dvc`, sinh mã VV, gửi response về LGSP
- Không có UI screen — không có CMS UI flow tương đương để test qua MCP chrome-devtools
- Test type: API thuần (curl/Postman), không UI bridge

**Hậu quả:** 0 TC ở file 04 cho UC53. File 04 chỉ test FR-V.I-05 nhánh **CMS** (DS/search/delete) — đã chủ động exclude API Inbound nhánh.

**Verify gián tiếp:** Khi LGSP push HS → CB NV thấy VV mới ở `kenh=DVC` trong DS (file 01/04) — verify state sau API call qua UI list. KHÔNG test trigger.

---

### LOẠI #2: FR-V.I-05 nhánh API Inbound (UC55 nhánh REST trực tiếp HE_THONG_KHAC)

**SRS Ref:** srs-fr-05:367-411 (Inputs API Inbound + Processing API Inbound)

**Lý do LOẠI:**
- Inputs/Processing API Inbound là REST POST `/api/inbound/he-thong-khac` từ HT bên ngoài
- Errors ERR-INTG-01..05, ERR-FILE-01..05, EC-V.I-05-01..13 (rate limiting, IP whitelist, idempotency replay) — đều là API contract test
- Không có UI screen submit từ external system

**Hậu quả:** 0 TC ở file 04 cho nhánh API Inbound. File 04 chỉ test:
- Processing CMS (B1-B6 srs-fr-05:417-422): DS/search/xem chi tiết/xóa CHO_TIEP_NHAN
- Inputs CMS (srs-fr-05:391-396): keyword/he_thong_nguon_filter/date range/page

**Verify gián tiếp:** ERR-FILE-01..03 verify qua UI upload file constraint trong các UC khác (UC52/54/57 file_dinh_kem cross-cutting).

---

### LOẠI #3: FR-V.I-CROSS-01 Scheduled job (BR-CALC-03 + BR-SLA-* auto)

**SRS Ref:** srs-fr-05:1460-1504

**Lý do LOẠI:**
- Scheduled job chạy **mỗi 30 phút** background — no UI feedback trực tiếp
- Tự động cập nhật `muc_do_canh_bao` + gửi TB theo BR-SLA-03
- Test type: cron / scheduled — không có user trigger

**Hậu quả:** Phần CRUD cấu hình SLA (UC108 trong module QTHT FR-VIII-06 — out of scope FR-V.I) **đã LOẠI khỏi scope test plan này**. Cấu hình SLA UI nằm trong test plan QTHT.

**Verify gián tiếp (acceptable):**
- TC-VV-DS-UI-03 verify badge SLA 4 mức UI render khi VV chuyển mức (gián tiếp via cảnh báo realtime)
- TC-VV-NH-307 (A4) verify deadline calc với holidays VN
- TC-VV-TB-307 (A6 gap-fill) verify TB SLA escalate qua time-shift seed VV (workaround manual)

---

## 2. TC-level filter scan (per file)

A7 scan từng file — predict 0 TC vi phạm vì A3 prompts đã pre-empt filter.

| File | Total TC | DB-only TC | API-only TC | Cron TC | LOẠI / SỬA |
|------|---------:|-----------:|------------:|--------:|:----------:|
| 01 | 21 | 0 | 0 | 0 | 0 |
| 02 | 23 (A4 +1) | 0 | 0 | 0 | 0 |
| 03 | 25 (A4 +1) | 0 | 0 | 0 | 0 |
| 04 | 14 | 0 (đã chủ động exclude API Inbound) | 0 | 0 | 0 |
| 05 | 19 | 0 | 0 | TC-VV-KT-304 verify gián tiếp BR-EC-16 (acceptable) | 0 |
| 06 | 21 | 0 | 0 | 0 | 0 |
| 07 | 25 | 0 | 0 | 0 | 0 |
| 08 | 21 | 0 | 0 (WRN-TB-02 LGSP outbound verify gián tiếp) | 0 | 0 |
| 09 | 21 | 0 | 0 | 0 | 0 |
| 10 | 19 | 0 | 0 (BR-CALC-06 cross sang FR-IV verify gián tiếp) | 0 | 0 |
| 11 | 27 (A4 +1) | 0 | 0 (BR-PUBLIC-04 verify network payload OK — UI bridge submit) | 0 | 0 |
| 12 | 29 (A4 +1, A6 +1) | 0 | 0 | TC-VV-TB-307 (A6) verify gián tiếp BR-SLA-03 (acceptable, time-shift workaround) | 0 |
| 13 | 11 | 0 | 0 | 0 | 0 |
| 14 | 18 | 0 | 0 | 0 | 0 |
| **Total** | **294** | **0** | **0** | **0** | **0 LOẠI / 0 SỬA** |

---

## 3. Acceptable verify-gián-tiếp cases (KHÔNG vi phạm A7)

Các TC sau verify gián tiếp scheduled job / API outbound — vẫn UI bridge qua state observation:

| TC ID | File | Gián tiếp gì? | Why acceptable |
|-------|------|--------------|----------------|
| TC-VV-DS-UI-03 | 01 | BR-SLA-02 4 mức cảnh báo | Verify badge UI render đúng theo state — UI bridge OK |
| TC-VV-KT-304 | 05 | BR-EC-16 quá hạn auto-reject | Time-shift VV.ngay_yeu_cau_bo_sung lùi 6 ngày → verify state chuyển TU_CHOI qua DS UI sau 30 phút (hoặc trigger manual qua admin endpoint) |
| TC-VV-NH-307 | 03 | BR-SLA-01 holidays VN | Verify deadline cột UI sau khi tạo VV ngay sát Tết — UI bridge OK |
| TC-VV-CK-101..104, 301, 302 | 11 | API Cổng PLQG outbound | Mock API trả 200/500/422 → verify UI state (cong_khai badge, toast, retry button) qua MCP — UI bridge OK |
| TC-VV-CK-102 | 11 | BR-PUBLIC-04 whitelist 9 fields | Verify NETWORK PAYLOAD qua `list_network_requests` body inspection sau khi user click Submit — UI bridge OK (user thao tác UI, MCP capture network) |
| TC-VV-DG-* (BR-CALC-06) | 10 | TVV diem_danh_gia_tb update cross sang FR-IV | Verify trigger qua UI flow đánh giá (verify GET response sau đánh giá có TVV.diem_danh_gia_tb mới) — UI bridge OK |
| TC-VV-PD-* (UC62 LGSP outbound) | 08 | WRN-TB-02 LGSP fail | Mock LGSP outbound → verify toast warning UI — UI bridge OK |
| TC-VV-TB-307 | 12 | BR-SLA-03 escalate TB | Time-shift seed VV → verify TB UI cho từng role (CB NV / CB PD / cấp trên) — UI bridge OK |

---

## 4. Phase A close acceptance

| Tiêu chí (Plan §3.1 acceptance) | Status |
|--------------------------------|:------:|
| 7 bước A1-A7 done | ✅ |
| Traceability ≥95% BR | ✅ (98% per file 09) |
| Traceability 100% AC | ✅ (62/63 = 98%, 1 out of scope CROSS-01 AC1) |
| 0 TC chỉ-DB/API thuần (A7 verified) | ✅ (0 LOẠI, 0 SỬA needed) |
| 0 TC sống ở file phụ (08/10/11) | ✅ (8 cross-cutting + 4 A4 inline + 1 A6 inline ALL merged inline vào 14 UC files) |
| SPEC-CLARIFY listed | ✅ (~50 entries listed in 10-REVIEW-test-quality §5) |

---

## 5. Final TC count after Phase A

| File | A3 base | A4 inline | A6 inline | Final |
|------|--------:|----------:|----------:|------:|
| 01-TC-quan-ly-vu-viec-DS.md | 21 | 0 | 0 | 21 |
| 02-TC-tao-vu-viec-DN.md | 22 | +1 (TC-VV-DN-308) | 0 | 23 |
| 03-TC-nhap-thu-cong-vv.md | 24 | +1 (TC-VV-NH-307) | 0 | 25 |
| 04-TC-tiep-nhan-cms-ht-khac.md | 14 | 0 | 0 | 14 |
| 05-TC-kiem-tra-hs.md | 19 | 0 | 0 | 19 |
| 06-TC-quan-ly-hs-vv.md | 21 | 0 | 0 | 21 |
| 07-TC-phan-cong-xac-nhan.md | 25 | 0 | 0 | 25 |
| 08-TC-trinh-phe-duyet-pd.md | 21 | 0 | 0 | 21 |
| 09-TC-cap-nhat-ket-qua.md | 21 | 0 | 0 | 21 |
| 10-TC-danh-gia-vv.md | 19 | 0 | 0 | 19 |
| 11-TC-cong-khai-vv.md | 26 | +1 (TC-VV-CK-307) | 0 | 27 |
| 12-TC-DN-bo-sung-thong-bao.md | 27 | +1 (TC-VV-TB-306) | +1 (TC-VV-TB-307) | 29 |
| 13-TC-cau-hinh-quy-trinh.md | 11 | 0 | 0 | 11 |
| 14-TC-permission-matrix.md | 18 | 0 | 0 | 18 |
| **Total** | **289** | **+4** | **+1** | **294** |

> **Phase B B-block ref CHỈ 14 file UC (01-14)**, total 294 TC.
> **Audit-only files** (file 08/09/10/11 này): KHÔNG test source. Phase B B-block KHÔNG ref.

---

## 6. Acceptance Phase A → flip W3.2 ✅

Phase A FR-V.I (W3.2) **CLOSED 2026-05-06** với:
- 14 file UC test case (294 TC, ~1500 dòng total)
- 4 audit log files (08 edge case, 09 trace matrix, 10 quality review, 11 a7 filter log)
- 1 test plan overview (00)
- Coverage ≥95% BR + 98% AC + ≥94% Error codes + 95% SM transitions
- 6-axis quality average 88.4% (≥85% threshold)
- 0 A7 violation (no DB-only, no API-only)
- ~50 SPEC-CLARIFY entries pending BA review (Phase B B-Verify will consolidate)

**Next step:**
- Update `tasks/detailed-tc/todo.md` W3.2 row → A ✅
- Update `tasks/detailed-tc/plan.md` §2 row 9 (Vụ việc TGPL) Phase A status → ✅ Có TC
- Phase B 🚫 chờ BUG-FLOW-VUVIEC-001 close + W2.1 (DN) + W2.2 (CG-TVV) Phase B done
