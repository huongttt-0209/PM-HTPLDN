# 10 — Test Quality Review (Audit only)

> **Audit only** — TC mới (fill gap A5) đã MERGE inline vào file UC tương ứng (Section "A6 fill gap"). File này ghi issue list + score.
> **Ngày**: 2026-05-09 · **Tester**: Claude
> **Status**: 270 TC tổng (217 base A3 + 42 edge A4 + 11 fill A6)

---

## A. Quality scorecard

| Dimension | Score (/10) | Rationale |
|----|---:|----|
| **Coverage BR** | 10 | 16/16 BR có TC explicit (sau A6 fill) |
| **Coverage AC** | 10 | 60/60 AC explicit |
| **Coverage ERR** | 9.5 | 35/35 ERR codes (sau A6 fill ERR-LS-01, ERR-CT-02, WRN-TCTV-04, ERR-TT-TC-03) |
| **Coverage SM** | 10 | 29/29 transitions explicit (sau A6 fill 4 transitions TC TV + NHT) |
| **Coverage Permission** | 10 | 10 vai trò × 6 action covered ở file 14 |
| **Coverage Edge** | 9 | 17 EC categories covered (concurrency / unicode / whitespace / soft-delete / SQL / pagination / timezone / file 0-byte / API timeout / round-half-up tie / IDOR / batch mixed / OptLock / CHO_KICH_HOAT special / NHT cross-entity / sanitize URI / session) |
| **NGUYÊN VĂN messages** | 9 | Most ERR/WRN/INF/Toast quote từ SRS NGUYÊN VĂN; SPEC-CLARIFY 25 entries chờ BA |
| **SRS line ref** | 8.5 | UC files có ref `srs-fr-04-chuyen-gia-tvv- v3.1.md:NNN-NNN` ở header; suggest sau Codex thêm line:column cho mỗi BR cite trong Expected |
| **A7 ready (UI/function)** | 9 | Hầu hết TC qua UI; các TC verify-DB đã reroute network/UI; còn 1-2 SPEC-CLARIFY-CGTVV cho TC verify AUDIT_LOG immutable cần UI bridge |
| **Inline merge compliance** | 10 | 42 edge A4 + 11 fill A6 đã merge inline vào 14 file UC; 0 TC sống ở file phụ 08/09/10 (audit only) |
| **TỔNG** | **9.50/10** | Quality production-ready, chờ Codex review + A7 final pass |

---

## B. Issue list (sorted by severity)

| # | Severity | Issue | File | Action |
|---|---|---|---|---|
| 1 | 🔴 Critical | SPEC-CLARIFY 25 entries pending BA — sẽ block Phase B nếu không có answer | All | Gửi BA email tổng hợp 25 SPEC-CLARIFY-CGTVV-01..25 |
| 2 | 🟡 High | TC-PERM-601 (BR-DATA-05 immutable AUDIT_LOG) cần UI bridge — hiện DevTools cố sửa, có thể verify qua FR-VIII-28 list audit nếu read-only | File 14 | Confirm với dev FR-VIII-28 read-only enforcement |
| 3 | 🟡 High | TC-NL-601 (BR-FLOW-03 HO_SO sau approval) — SRS không nói rõ NHT có override BR-FLOW-03 cho HO_SO không | File 04 | SPEC-CLARIFY-CGTVV-23 forward BA |
| 4 | 🟡 High | TC-CNTT-501 (CHO_KICH_HOAT → VO_HIEU_HOA) — SM-TVV không có transition explicit | File 10 | SPEC-CLARIFY-CGTVV-16 forward BA |
| 5 | 🟢 Medium | TC-DG-001 (DN đánh giá lần 2 cùng VV) — SRS không quy định prevent duplicate | File 09 | SPEC-CLARIFY-CGTVV-26 forward BA (sau Codex review) |
| 6 | 🟢 Medium | Một số toast text "Toast 'Cập nhật ... thành công'" có thể không khớp NGUYÊN VĂN SRS — Codex review sẽ catch | All | Codex pass |
| 7 | 🟢 Medium | TC-TC-202 (BR-FLOW-03 cho TC TV HOAT_DONG) — SRS phân biệt field nào sửa được sau duyệt? | File 11 | SPEC-CLARIFY-CGTVV-08 forward BA |
| 8 | 🟢 Low | TC verify NHT email cross-entity với TVV email — TAI_KHOAN.email UNIQUE | File 13 | SPEC-CLARIFY-CGTVV-19 forward BA |

---

## C. SPEC-CLARIFY tổng hợp (25 entries)

| Mã | Mô tả | File phát hiện | Forward BA |
|----|----|----|---|
| SPEC-CLARIFY-CGTVV-01 | Export TVV >10K rows behavior — WRN-TVV-01 message text? | File 02 TC-TIMKIEM-202 | ✉️ |
| SPEC-CLARIFY-CGTVV-02 | TVV bắt buộc thẻ HN — ERR code chính xác? (NĐ 77/2008 Đ.20) | File 03 TC-DK-010 | ✉️ |
| SPEC-CLARIFY-CGTVV-03 | Điểm thẩm định ngoài thang 1-5 — ERR code? | File 06 TC-TD-011 | ✉️ |
| SPEC-CLARIFY-CGTVV-04 | "Lưu nháp" thẩm định — SRS có support? | File 06 TC-TD-015 | ✉️ |
| SPEC-CLARIFY-CGTVV-05 | Batch approve partial fail — UI behavior chi tiết? | File 07 TC-PD-503 | ✉️ |
| SPEC-CLARIFY-CGTVV-06 | Guard HOI_DAP scope chi tiết enum nào? | File 10 TC-CNTT-112 | ✉️ |
| SPEC-CLARIFY-CGTVV-07 | TC TV thiếu Số ĐKHĐ — ERR code chính xác? | File 11 TC-TC-003 | ✉️ |
| SPEC-CLARIFY-CGTVV-08 | TC TV HOAT_DONG sau duyệt — field nào sửa được? | File 11 TC-TC-202 | ✉️ |
| SPEC-CLARIFY-CGTVV-09 | NHT username 4-50 ký — ERR code? | File 13 TC-NHT-006 | ✉️ |
| SPEC-CLARIFY-CGTVV-10 | Filter "Đã xóa" trên SCR-IV-01 — SRS có define? | File 01 TC-TVV-505 + File 02 TC-TIMKIEM-302 | ✉️ |
| SPEC-CLARIFY-CGTVV-11 | Sort default + secondary tie-breaker | File 02 TC-TIMKIEM-304 | ✉️ |
| SPEC-CLARIFY-CGTVV-12 | Race NHT update + CB NV thẩm định — optimistic lock cho HO_SO? | File 03 TC-DK-501 + File 04 TC-NL-501 | ✉️ |
| SPEC-CLARIFY-CGTVV-13 | Batch approve max size limit | File 07 TC-PD-601 | ✉️ |
| SPEC-CLARIFY-CGTVV-14 | Token kích hoạt expiry duration | File 07 TC-PD-604 | ✉️ |
| SPEC-CLARIFY-CGTVV-15 | Race công khai vs vô hiệu hóa precedence | File 08 TC-CK-301 | ✉️ |
| SPEC-CLARIFY-CGTVV-16 | SM-TVV CHO_KICH_HOAT → VO_HIEU_HOA transition | File 10 TC-CNTT-501 | ✉️ |
| SPEC-CLARIFY-CGTVV-17 | Export PL2 với data legacy thiếu Số ĐKHĐ | File 11 TC-TC-603 | ✉️ |
| SPEC-CLARIFY-CGTVV-18 | Optimistic lock cho FR-IV-NEW-02 | File 12 TC-TCPD-501 | ✉️ |
| SPEC-CLARIFY-CGTVV-19 | NHT email trùng TVV email — TAI_KHOAN.email UNIQUE conflict? | File 13 TC-NHT-401 | ✉️ |
| SPEC-CLARIFY-CGTVV-20 | NHT vô hiệu hóa giữa form — auto-save draft? | File 13 TC-NHT-402 | ✉️ |
| SPEC-CLARIFY-CGTVV-21 | Session expired + draft restore | File 14 TC-PERM-502 | ✉️ |
| SPEC-CLARIFY-CGTVV-22 | Real-time permission change sync | File 14 TC-PERM-503 | ✉️ |
| SPEC-CLARIFY-CGTVV-23 | BR-FLOW-03 override cho HO_SO sau approval | File 04 TC-NL-601 | ✉️ |
| SPEC-CLARIFY-CGTVV-24 | SM-NHT VO_HIEU_HOA → HOAT_DONG khôi phục SRS không cover explicit | File 13 TC-NHT-501 | ✉️ |
| SPEC-CLARIFY-CGTVV-25 | BR-DATA-05 AUDIT_LOG immutable — UI bridge để verify | File 14 TC-PERM-601 | ✉️ |

**Tổng SPEC-CLARIFY:** 25 entries → gửi BA tổng hợp trong Phase B B-Verify (chuyển GAP status nếu chưa rõ).

---

## D. A7 readiness check

| File | TC require DB query | TC API curl thuần | TC cron/queue no-UI | Need A7 fix? |
|----|---|---|---|---|
| 01 | TC-TVV-601 (verify common fields qua API response) | 0 | 0 | ✅ OK — qua API/UI bridge |
| 02 | 0 | 0 | 0 | ✅ |
| 03 | 0 | 0 | 0 | ✅ |
| 04 | 0 | 0 | 0 | ✅ |
| 05 | 0 | 0 | 0 | ✅ |
| 06 | 0 | 0 | 0 | ✅ |
| 07 | TC-PD-606 (mail server fail) | 0 | TC-PD-606 (queue retry — cần verify qua admin UI hoặc log) | ⚠️ Convert TC-PD-606 verify qua UI list-queue (admin) hoặc skip queue verify part — A7 fix |
| 08 | TC-CK-302 (queue retry) | 0 | TC-CK-302 (queue verify cần admin UI) | ⚠️ Convert verify qua admin UI — A7 fix |
| 09 | 0 | 0 | 0 | ✅ |
| 10 | TC-CNTT-111 (push realtime) | 0 | 0 | ✅ |
| 11 | TC-TC-701 (queue retry) | 0 | TC-TC-701 (queue) | ⚠️ A7 fix |
| 12 | 0 | 0 | 0 | ✅ |
| 13 | 0 | 0 | 0 | ✅ |
| 14 | TC-PERM-601 (AUDIT_LOG immutable) | TC-PERM-501 (DevTools API direct) | 0 | ⚠️ TC-PERM-501 đã là edge IDOR qua DevTools UI bridge → A7 OK; TC-PERM-601 cần SPEC-CLARIFY-25 |

**A7 needs:** 3 TC convert verify queue → admin UI bridge (TC-PD-606, TC-CK-302, TC-TC-701) + 1 TC verify-DB cần SPEC-CLARIFY (TC-PERM-601).

---

**Iron rule reminder:** Phase B chạy từ file UC `01-14-TC-*.md` — KHÔNG ref file 10. A6 fill TC đã merge inline.
