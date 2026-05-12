# Review — Cross-cutting Permission test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:45:00
**File reviewed:** `docs/todo-test/cross-cutting-permission/test-plan.md` (271 lines)

## Gaps

1. **SRS line cite lệch 4–6 dòng — BR-AUTH master block.** Plan ghi `srs-v3/srs-v3.md:3949` cho BR-AUTH-01 và `:3945-3966` cho cả khối. Verified thực tế: BR-AUTH-01 ở **line 3949** OK, nhưng BR-AUTH-02→3950, BR-AUTH-03→3951, BR-AUTH-04→**3952** (plan đúng), BR-AUTH-05→**3955** (plan ghi 3955 OK), BR-AUTH-06→**3956** (OK), BR-AUTH-07→**3957**, BR-AUTH-08→**3958**, BR-AUTH-09→**3959**, BR-AUTH-10→**3963**, BR-AUTH-11→**3964**. Plan §2.1 mostly OK nhưng header §1 ghi `lines 3945-3966` — chính xác phải `3945-3966` (B.1 header to BR-AUTH-11 line + status note) — verified. **Cite OK overall.**

2. **BR-AUTH-04 v3.5 "2-tier reaffirm" không có ref SRS cụ thể.** Plan TC2 dùng claim "v3.5 2-tier — BN không có ĐP trực thuộc theo FR-V.I refactor" nhưng không quote line update. SRS line 3952 đã ghi "BN KHÔNG thấy ĐP" từ v3 — không phải v3.5 mới. Phải clarify: đây là **reaffirm** v3 (không phải change), không cite delta-map dòng nào — sửa wording hoặc thêm cite `permission-matrix.md:4` (BN/ĐP 2 tầng ngang cấp).

3. **9 entity mới v3.5 coverage chỉ liệt kê bullet — không có TC riêng.** §2.1 footnote (line 76) list 14 entity (NGUOI_HO_TRO, TO_CHUC_TU_VAN, NGAY_LE, PHAN_CONG_VU_VIEC, DANH_GIA_VU_VIEC, LICH_SU_VU_VIEC, HO_SO_PHAP_LY_DN, TU_LIEU_PHAP_LY_VV, DANH_GIA_CHAT_LUONG_TV, THAM_DINH_HO_SO, PHE_DUYET_CHI_TRA, DOT_BAO_CAO, DOANH_NGHIEP_LINH_VUC, DANH_GIA_SAU_VU_VIEC) — nhưng §2.3 chỉ sample 4 entity mới (NGUOI_HO_TRO, TO_CHUC_TU_VAN, PHAN_CONG_VU_VIEC, HO_SO_PHAP_LY_DN). Thiếu: LICH_SU_VU_VIEC (audit read scope), TU_LIEU_PHAP_LY_VV (BR-FLOW-07 không cần phê duyệt — high risk leak), DANH_GIA_CHAT_LUONG_TV (DN 🔌 C† qua API — BR-AUTH-11 case mới), THAM_DINH_HO_SO + PHE_DUYET_CHI_TRA (FR-06 chi-tra). **Khuyến nghị:** thêm 5 entity vào §2.3 + 1 TC/entity new = +5 TC.

4. **BR-AUTH-10 lọc kép missing: scope "Lớp 1 only" cho data chung (UC21, UC27).** SRS line 3963 ghi "Dữ liệu chung (UC21, UC27): chỉ Lớp 1". Plan TC5 chỉ test happy path NHT/TVV/CG thấy VV phân công + cross-unit negative — KHÔNG có TC verify dữ liệu chung (tài liệu ĐT/CTĐT) áp Lớp 1 only (không filter `nguoi_ho_tro_id`). Thiếu test này → false negative khi BE accidentally apply Lớp 2 vào tài liệu chung → NHT không thấy tài liệu ĐT chung.

5. **BR-AUTH-08 exception v3.5 "Cán bộ Trung ương" không có line ref chính xác.** Plan TC4.3 mention "v3.5 CB_NV_TW exception cho VU_VIEC.cong_khai" — cite `permission-matrix.md line 4 v3.5 update FR-05`. Verified line 4 của permission-matrix có ghi "BR-AUTH-08 thêm exception 'Cán bộ Trung ương' (V4-CHƯA-SỬA #1)". **OK** nhưng `_DELTA-MAP-CROSS-CUTTING.md` (file delta cross-cutting) KHÔNG có exception này — exception nằm trong `_DELTA-MAP-FR05.md`. Plan ghi nguồn `_DELTA-MAP-CROSS-CUTTING.md` cho BR-AUTH-08 v3.5 là **sai**. Phải đổi cite sang FR05 delta hoặc permission-matrix.md.

6. **C1 Hard-delete + AUDIT_LOG conflict — chưa test action DELETE ghi audit.** Plan TC4.4 chỉ verify "DELETE → GET 404 / record không trong list". Thiếu verify positive: sau hard-delete → AUDIT_LOG có row action=DELETE (BR-DATA-05 INSERT-only, SRS line 3976). Risk: BE hard-delete bỏ qua audit log → vi phạm compliance NĐ55/Luật Dữ liệu 2024 (BR-LEGAL-07).

7. **C2 ClamAV remove KHÔNG có TC verify behavior thực tế.** SRS update bỏ virus scan toàn hệ thống. Plan KHÔNG có TC verify `.exe`/`.bat`/file độc → BE accept/reject ra sao. `_DELTA-MAP-CROSS-CUTTING.md` line 81-84 đã list action "thêm test case security upload file .exe/.bat" — plan miss.

8. **TC count target 71 ≥ 30 OK, nhưng phân bổ priority dồn P0 (70%).** Thực tế 11×3 role TC × 33 (line 200) đa số là menu visibility — thường P1. Plan đánh P0 toàn bộ → inflate P0 count + nguy cơ block release vì TC P1 fail.

9. **Account `dn_user_01`/`nht_user_01`/`tvv_user_01`/`cg_user_01` "cần seed" — không có dep marker `[need: ...]` per CLAUDE.md State marker workflow.** Plan §1.3 chỉ ghi "(cần seed)" — không có format `[need: ≥N account state X (verify query)]`. Vi phạm Rule 2 CLAUDE.md §State marker workflow.

10. **Memory `qa_htpldn_qtht_permission_bypass` cite có nhưng KHÔNG có TC dedicated.** Plan line 229 đề cập "QTHT bypass permission gate sai (vd DELETE TU_VAN_VIEN)" trong FAIL criteria, nhưng §4 không có TC chạy probe API trước UI để verify QTHT 👁️ R only trên TU_VAN_VIEN/NGUOI_HO_TRO (BA chốt 2026-05-09). Thêm 1 TC P0.

## Suggestions

1. **Thêm cột "v3.5 status" vào §2.3 matrix** — phân biệt entity legacy vs entity mới (NEW/CHANGED), giúp tester ưu tiên test entity NEW trước.

2. **Split TC §07-TC-role-{role}.md theo entity high-risk** thay vì 3 TC sample đại trà 11 file. Vd `07-TC-role-cb_nv_tw.md` nên cover ≥5 entity (HOI_DAP CRUD + MAU_PHAN_HOI MPH_CREATE_TW action-level + VU_VIEC scope TW + DOANH_NGHIEP no-Create v3.5 + LICH_SU_VU_VIEC read scope).

3. **Bổ sung TC `MPH_CREATE_TW/BN/DP` action-level** (FR-02 v3.5 MAU_PHAN_HOI Hybrid Model B) — đây là **permission mới ở level action**, không phải entity-level CRUD. Plan §2.3 row 2 có note nhưng §4 chưa có TC. Cite: `permission-matrix.md:4` v3.5 FR-02 line item (4).

4. **Cite SRS section §3.2.0.4 (lines 661-695)** trong §2.1 vì đây là tổng hợp gốc BR-DATA-02 + BR-AUTH-08/10/11 — plan có cite ở §6 nhưng §2.1 chỉ cite Phụ lục B. Add cross-ref để verify scope nhất quán.

5. **MCP isolated context naming convention** — plan ghi `isolatedContext: "<role>_<unit>"`. Khuyến nghị format chi tiết hơn: `<role>_<don_vi_ma>_<session_idx>` để track ≥2 session/role cho TC isolation cross-unit (DI-04/DI-05). Verify hook `chrome-devtools-mcp` không có max length 32 char.

6. **Thêm regression TC cho `qa_htpldn_api_wrap_bug` memory** — verify dropdown DON_VI/VAI_TRO render khi BE wrap envelope 2 lần. Permission test thường gặp dropdown rỗng do API double-wrap → false negative "role không có quyền".

7. **§5 Tiêu chí PASS thiếu metric "menu visibility match 100%"** — đã có "100% match matrix" nhưng không gọi rõ check menu hide/button hide separately. Tách:
   - Menu visibility match per role: 100%
   - Button visibility match per role: 100%
   - Record scope match per query: 100%
   - 0 leak cross-unit
   - 0 deep-link bypass (403 enforced).

8. **Thêm dep marker `[need: ...]` cho mỗi TC §3 file** theo template CLAUDE.md State marker workflow — vd `01-TC-auth-tier1.md` cần `[need: ≥1 TK HOAT_DONG mỗi role × cấp (✓ verify query SELECT COUNT WHERE trang_thai='HOAT_DONG' GROUP BY vai_tro, cap)]`. Hook `auto-rescan-todo.py` round-agnostic sẽ tự flip khi marker thoả.

## Verdict

**REVISE** — Plan có structure tốt (8 nhóm, ≥71 TC, cite đa nguồn) nhưng có 3 gap blocker phải fix trước approve:

1. **Gap #5** (cite delta-map sai cho BR-AUTH-08 v3.5 exception) — risk: tester không tìm thấy spec gốc khi log bug.
2. **Gap #3** (5 entity v3.5 mới thiếu TC) — risk: miss regression entity NEW.
3. **Gap #9** (account seed không có state marker) — vi phạm CLAUDE.md Rule 2 enforced workflow.

Sau khi fix 3 gap blocker + add 2 TC mới (C1 audit log, C2 file upload security) → approve. Estimated effort: 30 phút edit.

**Justification:** Plan covers BR-AUTH-01..11 đầy đủ, cite SRS line precise (line 3949-3964 verified), method MCP isolated context đúng memory `qa_htpldn_round5_t01`, account convention theo `users.csv` chuẩn. Gap chủ yếu là **completeness** (entity v3.5 mới + edge case C1/C2) chứ không phải **correctness** structural.
