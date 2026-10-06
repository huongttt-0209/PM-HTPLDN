# Edge Case Hunter Review — FR-V.I Vụ việc TGPL (BMAD A4) — MERGE AUDIT LOG

> **Ngày**: 2026-05-06 · **Reviewer**: BMAD edge-case-hunter (manual + LLM-augmented)
> **Status**: ✅ **MERGED 2026-05-06** — 4 cross-cutting edge case mới + audit existing inline edges trong 14 file UC.
> **File này KHÔNG còn là TC source** — chỉ là audit history "đã merge gì vào đâu". Phase B B-block KHÔNG ref file này.

---

## Quy ước severity

| Severity | Action |
|----------|--------|
| 🔴 P0 | Bắt buộc merge vào file UC |
| 🟡 P1 | Nên merge — bug khả năng cao |
| 🟢 P2 | Optional — nice-to-have |

---

## 1. Tổng hợp edge case existing (đã merge inline trong A3)

> **Lý do edge cases đã có trong A3:** A3 prompts cho 4 agent + 3 file tự viết đã include explicit edge case requirements (per brief), nên A3 output đã edge-case-aware. A4 hunter phase này chủ yếu **audit + thêm cross-cutting** không nằm trong brief A3.

### Cross-cutting edges đã có sẵn (audit confirm)

| Edge case category | Files có | Note |
|--------------------|----------|------|
| BR-EC-01 Optimistic Locking (concurrent edit/save) | 01, 03, 05, 06, 07, 08, 09, 11, 13 | Đa số UC có concurrent test |
| BR-EC-13 XSS sanitize (rich-text + textarea) | 01 (search), 02 (noi_dung), 03 (noi_dung), 05 (ly_do), 06 (noi_dung_yeu_cau), 11 (mo_ta_cong_khai) | Critical paths covered |
| File upload boundaries (20MB, 100MB total, 10 file max) | 02, 03, 06, 09, 11, 12 | Tất cả UC có file_attachment |
| ClamAV virus scan (EICAR) | 02, 03, 06, 09, 11, 12 | Cross-cutting trong BR-DATA-06 |
| Network throttle Offline (upload interrupt) | 02, 06, 11 | Part of file_attachment edge |
| IDOR (sửa URL truy cập VV ngoài scope) | 06 (DN), 14 (cross-role) | Security |
| Session timeout mid-flow | 14 | Auth Tier 1/Tier 2 |
| Batch action mixed scope | 01 (batch trình PD), 08 (batch PD), 14 (batch mixed scope) | BR-FLOW-04 |

---

## 2. Edge case mới đề xuất — A4 propose (4 case cross-cutting)

| Original ID (proposal) | Severity | Mô tả | Merge target file | Final TC ID | Section |
|-----------------------|----------|-------|-------------------|-------------|---------|
| EC-VV-A4-01 | 🔴 P0 | BR-SLA-01 deadline calc với VN holidays — Tết âm lịch / Quốc khánh nằm giữa khoảng tiếp nhận → hoàn thành. Verify deadline +15 ngày làm việc EXCLUDE holidays | 03-TC-nhap-thu-cong-vv.md | **TC-VV-NH-307** | D. Edge |
| EC-VV-A4-02 | 🟡 P1 | Browser back button sau upload file — quay lại form cũ có giữ data + file đã upload? hoặc reset hoàn toàn? UX expected behavior | 02-TC-tao-vu-viec-DN.md | **TC-VV-DN-308** | D. Edge |
| EC-VV-A4-03 | 🔴 P0 | Concurrent CB PD: tab1 [Công khai] VV-X tab2 [Hủy công khai] VV-X (mâu thuẫn quyết định cùng lúc) — verify atomicity + final state consistent | 11-TC-cong-khai-vv.md | **TC-VV-CK-307** | D. Edge |
| EC-VV-A4-04 | 🟡 P1 | Email notification deep-link click — DN click link `/ho-so-cua-toi/vu-viec/{id}` từ email khi chưa login → redirect VNeID Tier 2 → sau auth thành công, redirect lại đúng VV (preserve context) | 12-TC-DN-bo-sung-thong-bao.md | **TC-VV-TB-306** | D. Edge |

**Tổng: 4 edge case mới → MERGE inline vào 4 file UC tương ứng.**

---

## 3. Reasoning từng case mới

### EC-VV-A4-01: BR-SLA-01 với VN holidays (P0)

**Vì sao critical:** NĐ55/2019 Đ.8 K.1 quote "15 ngày làm việc" — implementation phải EXCLUDE Tết âm lịch (7 ngày), Quốc khánh (2 ngày), Giải phóng + Quốc tế lao động (2 ngày), v.v. Nếu BE đếm naive 15 ngày bất kỳ → deadline sai vào dịp lễ → over-/under-charge SLA.

**Test:**
- Seed VV tiếp nhận ngày 2026-02-08 (gần Tết 2026-02-09 đến 15 — giả định 7 ngày Tết). Deadline mong đợi = 2026-03-04 (skipping holidays), KHÔNG phải 2026-02-23 (naive).
- Verify cột Deadline SLA + Cảnh báo SLA tính đúng theo working calendar.
- Mark **SPEC-CLARIFY-VV-A4-01**: SRS không quote calendar source — production có table HOLIDAY_VN không?

**Merge target:** File 03 (UC54 nhập thủ công, có deadline calc trong Processing B8 srs-fr-05:334) — section D. Edge.

---

### EC-VV-A4-02: Browser back button form data preservation (P1)

**Vì sao quan trọng:** UC52 form DN gửi HS có 4 Accordion + file upload. Nếu DN nhấn back giữa chừng (vd sau upload xong, navigate đi rồi quay lại) — data có giữ trong form? hay reset? — common UX bug.

**Test:**
- Nhập 70% form, upload 1 file → navigate qua tab khác → back.
- Expected: hoặc auto-save draft (toast "Đã lưu nháp"), hoặc giữ form state in browser memory (FE state), hoặc reset hoàn toàn (warning trước khi reset).
- Mark **SPEC-CLARIFY-VV-A4-02**: SRS không spec auto-save draft cho UC52.

**Merge target:** File 02 (UC52 DN gửi HS) — section D. Edge.

---

### EC-VV-A4-03: Concurrent CB PD công khai/hủy (P0)

**Vì sao critical:** Workflow công khai có cả 2 hành động ngược chiều (CK ⟷ Hủy CK). 2 CB PD cùng cấp có thể nhấn 2 hành động khác nhau cùng lúc trên cùng VV → race condition. BR-EC-20 atomic chỉ đảm bảo từng action atomic, KHÔNG đảm bảo concurrent reconciliation.

**Test:**
- VV-X DA_DUYET cong_khai=1.
- Tab1 `cb_pd_tw_01` click [Hủy công khai] + nhập lý do.
- Tab2 `cb_pd_tw_02` (cùng cấp) đồng thời open VV-X (state stale) — không thấy badge "Đã công khai" cập nhật yet → click [Công khai] (form ảnh + mô tả).
- Tab1 submit trước → cong_khai=0 + clear cột.
- Tab2 submit → expected: optimistic lock conflict (vì version đã thay đổi). NẾU không có optimistic lock → tab2 có thể overwrite tab1, resulting cong_khai=1 với mô tả mới NHƯNG audit log lẫn lộn.

**Merge target:** File 11 (NEW-05 công khai) — section D. Edge.

---

### EC-VV-A4-04: Email deep-link auth flow Tier 2 (P1)

**Vì sao quan trọng:** UC64 (DN nhận TB) + NEW-02 (DN bổ sung) + NEW-05 (DN nhận TB CK) đều gửi email với deep-link đến SCR-V.I-03 chế độ DN. DN click email → browser chưa có session → expected: redirect VNeID Tier 2 OAuth → sau auth → redirect lại deep-link.

**Test:**
- DN nhận email TB "VV-X yêu cầu bổ sung hồ sơ" với link `/ho-so-cua-toi/vu-viec/{id-X}`.
- Logout DN. Click link từ email.
- Expected: redirect `/auth/vneid?return_url=/ho-so-cua-toi/vu-viec/{id-X}` → DN nhập OTP VNeID → callback success → redirect đúng VV-X (preserve context).
- Edge: nếu return_url bị lỗi encode → DN landing /dashboard generic (loss of context) — bug.
- Mark **SPEC-CLARIFY-VV-A4-04**: VNeID OIDC return_url spec trong Tier 2 flow (BR-AUTH-01 srs-fr-05:2381).

**Merge target:** File 12 (NEW-02 + UC64 phần TB) — section D. Edge.

---

## 4. Rejected proposals (không merge)

| Proposal | Severity | Lý do reject |
|----------|----------|-------------|
| Performance test DS VV với 10,000 records | 🟢 P2 | Out of scope functional A3. Move to performance plan riêng nếu có |
| Accessibility (a11y) — keyboard navigation Stepper SCR-V.I-03 | 🟢 P2 | Out of scope functional, defer A11y review pass |
| i18n EN translation cho UI labels | 🟢 P2 | Spec hiện chỉ Vietnamese. Defer khi có tickets i18n |
| Mobile responsive cho SCR-V.I-01 CMS | 🟢 P2 | SRS quote "tối thiểu hỗ trợ máy tính bảng 1024×768. Không bắt buộc mobile" (srs-fr-05:1629) → out of scope |

---

## 5. Lesson learned cho A6 / A7 / Phase B

- **Cross-cutting BR consistency:** Khi file phụ thuộc vào BR đã được test trong file khác (vd BR-EC-13 XSS đã test ở file 01 thì file 06 không cần lặp y hệt), ghi reference cross-file để tránh trùng. A6 review.
- **A7 Filter rule reminder:** A4 KHÔNG được tạo TC chỉ-DB (vd "verify HOLIDAY_VN table có records") hoặc API thuần. Mọi edge case đề xuất ở §2 đều có UI bridge: deadline calc verify qua cột Cảnh báo SLA (UI), versioning verify qua deadline trong VV-OLD vs VV-NEW (UI), browser back qua FE state observation, concurrent qua 2 tab UI.
- **SPEC-CLARIFY accumulating:** A4 thêm 4 SPEC-CLARIFY mới (VV-A4-01..04). A5/A6 cần consolidate toàn bộ vào 1 backlog gửi BA.

---

## 6. Total impact A4

| File | A3 base count | A4 thêm | Final count |
|------|--------------:|--------:|------------:|
| 01-TC-quan-ly-vu-viec-DS.md | 21 | 0 | 21 |
| 02-TC-tao-vu-viec-DN.md | 22 | +1 (TC-VV-DN-308) | 23 |
| 03-TC-nhap-thu-cong-vv.md | 24 | +1 (TC-VV-NH-307) | 25 |
| 04-TC-tiep-nhan-cms-ht-khac.md | 14 | 0 | 14 |
| 05-TC-kiem-tra-hs.md | 19 | 0 | 19 |
| 06-TC-quan-ly-hs-vv.md | 21 | 0 | 21 |
| 07-TC-phan-cong-xac-nhan.md | 25 | 0 | 25 |
| 08-TC-trinh-phe-duyet-pd.md | 21 | 0 | 21 |
| 09-TC-cap-nhat-ket-qua.md | 21 | 0 | 21 |
| 10-TC-danh-gia-vv.md | 19 | 0 | 19 |
| 11-TC-cong-khai-vv.md | 26 | +1 (TC-VV-CK-127) | 27 |
| 12-TC-DN-bo-sung-thong-bao.md | 27 | +1 (TC-VV-TB-128) | 28 |
| 13-TC-cau-hinh-quy-trinh.md | 11 | 0 | 11 |
| 14-TC-permission-matrix.md | 18 | 0 | 18 |
| **Total** | **289** | **+4** | **293** |

---

## 7. Next step

- **A5** (Traceability matrix): generate `09-traceability-matrix.md` map BR/AC ↔ TC. Dùng final count 293 sau A4 merge.
- **A6** (Test review): 6-axis quality score, có thể propose thêm gap-fill TC nếu A5 phát hiện BR/AC chưa cover.
- **A7** (UI/function-testable filter): manual scan loại TC chỉ-DB/API thuần (đã chủ động filter ở A3 prompt — predict A7 LOẠI ≤ 5 TC).
