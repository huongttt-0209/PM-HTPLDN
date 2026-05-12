# Review — FR-04 CG/TVV/NHT/TC-TV test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:41:26
**Plan reviewed:** `docs/todo-test/fr-04-chuyen-gia-tvv/test-plan.md` (416 dòng, 25 BR, 73 TC, 3 SM)

---

## Gaps

1. **FR-VIII reference sai — `FR-VIII-26` không tồn tại.** Plan §1.2 hàng FR-IV-07 + §2.5.1 SM-TVV mermaid `CHO_KICH_HOAT --> HOAT_DONG : ... (FR-VIII-26)` + §2.5.3 SM-NHT cũng cite `FR-VIII-26`. SRS update line 589, 2311, 2403, 2404 chỉ cite **`FR-VIII-15`** (quy trình tạo + kích hoạt tài khoản). Cần đổi toàn bộ ref FR-VIII-26 → FR-VIII-15 (3 chỗ ít nhất) để tránh tester defer "FR-VIII-26 không tìm thấy".

2. **TC migration `loai_tvv='NHT'` chưa có TC riêng — chỉ là note "Open issue" §7 #9.** SRS update §131 + §1998 đã bỏ `'NHT'` khỏi CHECK constraint nhưng KHÔNG cover migration plan. §7 nói "log bug edge case ở GĐ 2 Workflow" — nhưng GĐ 2 đã đóng theo §1 v3.0 note. Cần thêm TC E (edge) trong `01-TC-tvv-cg-crud.md`: probe DB record cũ `loai_tvv='NHT'` (nếu có) → verify FE crash / 500 / silent skip → log `SPEC-MIGRATION-IV-01`. Hiện 73 TC không có 1 TC nào target migration → MISS nguy cơ regression v3→v3.5.

3. **Rename `DANG_HOAT_DONG`→`HOAT_DONG` impact 8 module consumer chỉ liệt kê 1 dòng `15-TC-cross-module-impact.md` (4 TC).** SRS v3 line 41 + v3.5 line 2296 chứng minh enum rename. Plan §2.6 list 8 consumer (FR-05/12/14/03/02/11/01/16) nhưng `15-TC` allocate Happy 0 + Negative 2 + Edge 2 = 4 TC tổng — không đủ cover 8 consumer × filter dropdown. Cần ≥1 TC/consumer = ≥8 TC, hiện chỉ 4.

4. **BR-AUTH-10 "lọc kép" cho NHT/TVV/CG nhưng plan chỉ test CG ở permission matrix.** SRS v3 line 3963 + 668 quy định BR-AUTH-10 áp dụng cả **NHT + TVV + CG** với Lớp 2 lọc theo `VU_VIEC.nguoi_ho_tro_id` / `.tu_van_vien_id` / `YEU_CAU_TU_VAN.chuyen_gia_id`. §1.3 plan chỉ liệt kê `huongcg` test BR-AUTH-10. Thiếu TC NHT login chuyên trang chỉ thấy VV được phân công + TVV login chỉ thấy VV được phân công. `14-TC-permission-cross-role.md` 8 TC tổng — chỉ N1-N3 cho BR-AUTH-05, N4-N5 cho BR-AUTH-08, còn 3 TC không rõ scope BR-AUTH-10.

5. **TC mới cho SM-TCTV `TU_CHOI → CHO_PHE_DUYET` (re-submit) thiếu.** SRS update §2363 quy định transition này có guard `updated_at > thoi_gian_tu_choi`. Plan §2.5.2 mermaid có vẽ nhưng `10-TC-tctv-state-update.md` (4 TC) + `11-TC-tctv-phe-duyet.md` (5 TC) không list TC verify guard updated_at. Negative case "submit lại mà chưa sửa" → expect error chưa được cover.

6. **Permission `R-public Cổng` cho DN ở TCTV không có TC cụ thể.** §2.3 matrix dòng `TO_CHUC_TU_VAN — CRUD list` ghi DN = "R-public Cổng" nhưng SCR-IV-NEW-01 cho phép DN xem TCTV `cong_khai=1` trên Cổng PLQG. `09-TC-tctv-crud.md` (5 TC) không có TC DN role view public list — gap cho BR-LEGAL-09.

7. **BR-VIRUS-01 (ClamAV) test với NHT chưa rõ.** §2.1 BR-VIRUS-01 áp dụng FR-IV-01/03/04 + NEW-01 — bỏ qua NHT. SRS update §1206-1212 NHT form không có file upload nên đúng — nhưng note này nên hiện rõ "NHT KHÔNG cần ClamAV (form 5 field không upload)" ở §2.4 Feature module KHÔNG có (đã có dòng "Form upload bằng cấp" cho NHT nhưng không mention ClamAV explicit).

8. **`nht_btp_tw_audit_r30` ở §1.3 không có doc/CSV trace.** §1.3 list account này cho "Permission test khác đơn vị" nhưng `input/users.csv` chỉ có `nht_01/02` theo `qa_htpldn_accounts_convention`. Account `nht_btp_tw_audit_r30` có thể là leftover từ round 30 — cần verify có thực sự trong CSV trước khi commit plan.

9. **Bảng `5. Tiêu chí đạt/không đạt` không cover 73 TC pass rate target rõ ràng.** Chỉ liệt kê 6 "Bắt buộc cover" item nhưng không nói "P0 30 TC phải PASS 100%, P1 28 TC PASS ≥90%, P2 15 TC PASS ≥70%" tính ra số TC absolute. Tester GĐ 3 đọc xong khó tự verify "đạt" hay không.

10. **`BR-FLOW-TCTV-01` viết ngược logic.** §2.1 BR-FLOW-TCTV-01 ghi "TCTV phải qua phê duyệt CB PD ... trước khi `HOAT_DONG` — KHÔNG tạo trực tiếp `HOAT_DONG`" — đúng. Nhưng cite line `:2328 + :1058` — line 2328 chỉ là pháp lý NĐ 55/2019 Đ.9, không phải BR statement. Cần thêm cite line 2334 (transition `CHO_PHE_DUYET → HOAT_DONG`) làm primary citation.

11. **Section 7 mâu thuẫn #9 "Migration" không có owner/timeline.** Marker "Open issue" mà không nói ai chốt (BA? dev?) → defer mãi. Cần thêm cột "Owner" + "Deadline confirm" cho 10 ambiguity §7.

12. **§2.3 permission matrix dòng `TU_VAN_VIEN` — CG cell `R-own (BR-AUTH-10 nội bộ)` confusing.** "BR-AUTH-10 nội bộ" là gì? BR-AUTH-10 lọc kép theo `YEU_CAU_TU_VAN.chuyen_gia_id` — không có khái niệm "nội bộ". Nên đổi thành "R-own (chuyên trang FR-IV-11)".

---

## Suggestions

1. **Thêm 1 TC E1 trong `01-TC-tvv-cg-crud.md`:** "TVV record cũ DB `loai_tvv='NHT'` → verify UI rendering + filter behavior + log `SPEC-MIGRATION-IV-01`". Bump 01 từ 8 TC → 9 TC.

2. **Tách `15-TC-cross-module-impact.md` thành 8 TC (1/consumer):** FR-05 dropdown phân công VV (UC59) / FR-12 dropdown CG (TVCS) / FR-14 dropdown TVV (HĐ) / FR-03 dropdown GV / FR-02 dropdown NHT+TVV (FR-II-06) / FR-11 KPI count / FR-01 KPI-07 / FR-16 API public visibility. Bump 15 từ 4 TC → 8 TC.

3. **Thêm dòng giải thích `FR-VIII-15` thay vì `FR-VIII-26`** ở §1.2 hàng FR-IV-07 + §2.5.1/2.5.3 mermaid. Cross-ref `srs-fr-10-quan-tri.md` để confirm FR-VIII-15 là quy trình "Tạo tài khoản" (FR-VIII tier).

4. **Verify `nht_btp_tw_audit_r30` trong `input/users.csv` trước commit plan.** Nếu không có → đổi sang account nht khác hoặc bỏ. Hook `check-report-path-convention.py` không catch lỗi reference account.

5. **Thêm BR-AUTH-10 explicit TC cho cả 3 actor NHT/TVV/CG** trong `14-TC-permission-cross-role.md`: TC.N6 NHT login → chỉ thấy VV được phân công + TC.N7 TVV login → chỉ thấy VV được phân công + TC.N8 CG login → chỉ thấy YC TVCS được phân công. Bump 14 từ 8 TC → 11 TC.

6. **Thêm TC trong `10-TC-tctv-state-update.md` cho transition `TU_CHOI → CHO_PHE_DUYET` (re-submit):** Happy = sửa rồi trình → PASS; Negative = chưa sửa trình lại → expect error guard `updated_at > thoi_gian_tu_choi`.

7. **§5 Tiêu chí đạt — thêm số TC absolute:** "P0: 30/30 PASS (100%) | P1: ≥25/28 PASS (≥89%) | P2: ≥11/15 PASS (≥73%)". Dễ verify hơn % rỗng.

8. **Bổ sung column "Owner" + "Deadline" cho bảng §7 Ambiguity.** Mỗi row có "BA confirm by 2026-05-XX" hoặc "dev verify by 2026-05-XX".

9. **Cite chính xác `BR-FLOW-TCTV-01`** thay vì `:2328` (pháp lý) bằng `:2334` (transition spec) + `:1058` (FR-IV-NEW-01 processing). Cite line precise → dev verify nhanh.

10. **Thêm TC negative `09-TC-tctv-crud.md` E2:** DN role login Cổng PLQG → search TCTV `cong_khai=1` → expect list public + KHÔNG thấy `cong_khai=0`. Cover BR-LEGAL-09 + BR-PUBLIC-01.

11. **§2.4 thêm dòng "Feature module KHÔNG có":** `❌ ClamAV scan upload cho NHT — form NHT KHÔNG có upload field (`:1206-1212`)` — explicit để tránh tester log false bug.

12. **Probe API memory `qa_htpldn_qtht_permission_bypass` cho cả `/nguoi-ho-tros` + `/to-chuc-tu-vans`** ngay đầu `14-TC-permission-cross-role.md` (TC P0). Plan §2.3 note đã có nhưng nên tách TC ID riêng `TC14.P0-PROBE-API` thay vì lồng ghép.

---

## Verdict

**REVISE** — Plan có structure tốt + cover BR/SM/permission comprehensive nhưng có 3 critical gap:
- `FR-VIII-26` ref sai (gap #1) → tester defer block khi không tìm thấy spec.
- Migration `loai_tvv='NHT'` thiếu TC riêng (gap #2) → MISS regression v3→v3.5.
- BR-AUTH-10 lọc kép chỉ test 1/3 actor (gap #4) → MISS permission risk NHT/TVV cũng cần test.

12 gap khác hầu hết là precision issue (cite line, account verify, TC count) — chỉnh trong 30 phút. Sau khi fix 3 critical + apply ≥8/12 suggestion → APPROVE.
