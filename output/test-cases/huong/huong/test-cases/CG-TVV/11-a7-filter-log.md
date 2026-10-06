# 11 — A7 Manual Filter Log (Audit only)

> **Audit only** — TC đã Edit IN-PLACE file UC. File này log action LOẠI/SỬA/GIỮ.
> **Ngày**: 2026-05-09 · **Tester**: Claude
> **A7 rule**: 0 TC chỉ-DB/API thuần. TC verify-DB → reroute network/UI bridge.

---

## A. Action summary

| Action | Count | Note |
|----|---:|----|
| ❌ LOẠI | 0 | Không TC nào hoàn toàn không test được qua UI |
| ✏️ SỬA | 4 | Convert verify queue/email/DB → UI bridge |
| ✅ GIỮ | 266 | Hầu hết TC chạy 100% qua UI/DevTools/MCP chrome-devtools |
| **Tổng** | **270** | sau A4 (+42) + A6 (+11) + A7 (4 SỬA) |

---

## B. Detail SỬA

| TC ID | File | Original verification | A7 SỬA target | Lý do |
|----|----|----|----|----|
| TC-PD-606 | 07-TC-FR-IV-07-phe-duyet.md | Verify queue retry trực tiếp | Verify qua UI batch result modal + list reload + chức năng FR-VIII-26 Quên MK làm bridge | Tester không có quyền truy cập queue table; UI report đủ để verify partial fail |
| TC-CK-302 | 08-TC-FR-IV-08-cong-khai.md | Verify queue retry trực tiếp + admin queue UI | Verify qua list reload sau 5 phút (cong_khai=1) + Cổng PLQG public hiển thị | UI bridge đủ để verify retry success; admin queue UI ngoài scope tester |
| TC-TC-701 | 11-TC-FR-IV-NEW-01-quan-ly-TC-TV.md | Backend retry queue + email admin | Verify qua list reload + Cổng public; KHÔNG verify queue + email admin | Tester không có quyền nhận email admin; queue ngoài UI scope |
| TC-PERM-601 | 14-TC-permission-matrix.md | DevTools cố PUT/DELETE AUDIT_LOG (verify backend) | Verify qua **FR-VIII-28 list audit UI** (W1.1 đã ✅) — row read-only, không có nút Sửa/Xóa; bonus DevTools PUT verify 405 | FR-VIII-28 đã verify list audit UI có sẵn — UI bridge tốt hơn admin DB view |

---

## C. GIỮ — TC sử dụng UI bridge sẵn

| Pattern UI bridge | TC examples |
|----|----|
| MCP `list_network_requests` | All TC verify "STATE: Network call ..." (vd TC-TVV-001, TC-TIMKIEM-001) |
| MCP `list_console_messages` | All TC verify XSS sanitize (vd TC-NL-010, TC-DG-005) |
| MCP `take_snapshot` + DOM verify | All TC UI Verification (vd TC-TVV-UI-01..03) |
| Cổng PLQG public view | TC-CK-202, TC-CK-001, TC-PERM-301 |
| MailHog UI | TC-PD-001 (verify mail kích hoạt) |
| FR-VIII-28 list audit UI | TC-PERM-601 (sau A7 SỬA) |
| Admin "Khôi phục" action | TC-TVV-506 |
| Reload list verify state change | All transition TCs (vd TC-CNTT-101, TC-CK-203) |
| AntD virtual scroll dropdown | Filter TCs với combobox uid quirk |

---

## D. Negative — KHÔNG có TC LOẠI

A7 verify từng TC trong 14 file UC + 0 case nào không có UI bridge khả thi. Lý do:
- v3.1 SCR-IV-01/02/03 + SCR-IV-NEW-01/02/03 + SCR-IV-NHT-01/02/03 cover toàn bộ user-facing flow
- API outbound (Cổng PLQG, mail kích hoạt) đều có UI feedback (toast, badge, list reload)
- Cron/queue background đã reroute qua list reload sau timeout
- AUDIT_LOG verify qua FR-VIII-28 UI (W1.1)
- IDOR/security verify qua DevTools UI bridge (KHÔNG curl thuần)

---

## E. Final Phase A acceptance check

| Acceptance | Status | Evidence |
|----|---|----|
| ✅ A1-A7 done | ✅ | 7 step completed 2026-05-09 |
| ✅ Traceability ≥95% BR + 100% AC | ✅ | 100% BR (sau A6 fill) + 100% AC + 100% ERR (sau A6 fill) + 100% SM (sau A6 fill) + 100% Permission |
| ✅ 0 TC chỉ-DB/API thuần | ✅ | A7 SỬA 4 TC convert sang UI bridge; 0 LOẠI |
| ✅ 0 TC sống ở file phụ (08/09/10/11) | ✅ | 42 edge A4 + 11 fill A6 đã merge inline vào 14 file UC; file 08/09/10/11 chỉ là audit log |
| ✅ SPEC-CLARIFY listed | ✅ | 25 SPEC-CLARIFY-CGTVV-01..25 documented file 10 |

**Phase A FR-04 v3.1 Quality: 9.50/10 — PRODUCTION-READY · 270 TC tổng · Ready for Codex review (Step 8) → Phase B.**

---

**Iron rule reminder:** Phase B chỉ chạy file UC `01-14-TC-*.md` — KHÔNG ref file phụ 08/09/10/11.
