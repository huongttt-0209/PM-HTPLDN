# Review — FR-11 Báo cáo test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:15:30

## Gaps

- **Word→PDF mô tả sai bản chất thay đổi v3.5** (test-plan §2.1 BR-RPT-FORMAT-01, §2.4 Action-bar, TC-FR11-EXPORT-03). CHANGELOG line 569-580 nêu rõ: v3.5 ĐỔI Word sang PDF (chỉ FR-11), không phải thêm flow "Word→PDF" hybrid. Test plan đang dùng cụm "Xuất Word→PDF" lặp 4 chỗ — gây hiểu nhầm có 3 format (XLSX + DOCX + PDF) trong khi spec là 2 (XLSX giữ + DOCX bị thay bằng PDF). TC-FR11-EXPORT-02 ([Xuất Word] → .docx) và TC-FR11-EXPORT-03 ([Xuất Word→PDF] → .pdf) cùng tồn tại = mâu thuẫn nội bộ. Cần BA confirm trạng thái cuối format (CHANGELOG §H.3 cũng đang treo cờ "Cần Cán bộ phụ trách xác nhận TT17/2025 yêu cầu PDF hay chấp nhận Word").

- **TC-FR11-IX08-01 sao chép mâu thuẫn nội bộ SRS v3.5 mà không flag** (test-plan dòng 288: "BC số lượng CG/TVV theo loại × lĩnh vực × địa bàn"). CHANGELOG line 542-549 + line 597 ghi: FR-IX-08 Inputs đã **bỏ** `dia_ban_id`, **bỏ** NHT khỏi enum `loai_tvv`. Nhưng Output `theo_dia_ban[]` + SCR optgroup vẫn nhắc "Địa bàn" — đây là **contradiction C.2 đang treo gate** (`srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:597`). Test plan không note "BA Q chờ confirm" — sẽ FAIL TC vô lý hoặc PASS nhầm cả khi BE bug.

- **Đổi tên "hỏi đáp pháp lý → hỏi đáp pháp luật" v3.5 chưa apply trong test plan** (CHANGELOG line 523-526, ITEM-14). Test plan §1.2 row 1 + sampling slot 1 + TC-FR11-IX01-* vẫn dùng "BC Hỏi đáp"/"BC Số lượng hỏi đáp/vướng mắc" thiếu hậu tố "pháp luật". Verify wording check trong TC sẽ miss bug nếu UI vẫn giữ "pháp lý" (regression risk).

- **Permission matrix §2.3 thiếu cột Word→PDF tách biệt** (test-plan dòng 138: gộp "Xuất Excel/Word/PDF" 1 cell). Theo Rule 4 phân nhóm + 11 role × {Xem, Export Excel, Export Word/PDF}, ma trận phải tách Export Excel vs Export PDF vì spec v3.5 có khả năng dropdown format restrict per role (chưa verify). Hiện gộp 3 format = không test được trường hợp "role X được Excel nhưng không được PDF".

- **BR-DATA-06 chốt 50K không có BA sign-off** (test-plan §2.1 BR-DATA-06 + TC-FR11-EXPORT-04). SRS v3 nội bộ mâu thuẫn: `srs-fr-11-bao-cao.md:85` (Processing step 9) + `:112` (WRN-RPT-01) + `:1088` ghi "50.000 dòng", trong khi `:1258` BR-DATA-06 bảng chính ghi "10,000 rows/file". Test plan tự quyết 50K = vi phạm `feedback_deep_review_before_ba_defer` (trigger "Sai spec" → BẮT BUỘC NotebookLM query + escalate BA, không tự quyết). Cần escalate BA chốt limit + log 1 row "BA-Q-FR11-001 chờ confirm".

- **Cross-module upstream dependency thiếu state machine cụ thể** (test-plan §2.6 dòng 199-210). Liệt kê 8 entity upstream nhưng KHÔNG nêu rõ "≥N record/đơn vị/lĩnh vực × kỳ" như Rule 1 seed actor. Vd HOI_DAP state `DA_TRA_LOI` cần "≥1 record/đơn vị TW/BN/ĐP × ≥3 lĩnh vực × ≥3 kỳ" — ngữ nghĩa filter coverage thiếu sẽ trùng pattern A5 R5 fail (CLAUDE.md §"Quy tắc seed task — BẮT BUỘC tránh gãy như A5"). Đặc biệt FR-IX-09 cần `BAO_CAO_DANH_GIA` + `KE_HOACH_DANH_GIA` (CHANGELOG line 556-560 — Đổi tên "Đợt đánh giá" → "Kế hoạch đánh giá") nhưng test plan vẫn dùng "Đợt đánh giá".

- **Strategy sampling 8/23 loại miss 1 nhóm "VV phân tích"** (test-plan §1.3 bảng sampling). 7 nhóm theo §1.2 = Hỏi đáp / Vụ việc / Đào tạo / CG-TVV / Đánh giá / Chi phí / CT HTPLDN — không có "VV phân tích" (UC134-137, 4 loại) như 1 nhóm riêng. §1.3 chú thích "1 đại diện/nhóm + 2 high-risk" nhưng sample chỉ cover 7 nhóm × 1 + 1 high-risk = 8. VV phân tích bị merge ngầm vào nhóm "Vụ việc" → 4 loại UC134-137 chỉ smoke 5 phút (group `Stacked bar/Grouped bar/Stacked trend` chart logic chưa cover).

- **TC-FR11-WF-01..04 dùng v3.5 state machine 4-state nhưng không có TC kiểm chứng từ chối lý do >=10 ký tự cụ thể** (test-plan dòng 184: CHO_DUYET → NHAP `[Từ chối]`). TC-FR11-WF-04 chỉ test lý do <10 ký tự = invalid. Thiếu happy path: lý do = đúng 10 ký tự (boundary) + lý do >500 ký tự (max sanitize BR-EC-13).

## Suggestions

- **Tách "Word→PDF" thành 2 TC riêng + BA Q-block:** TC-EXPORT-02 (XLSX happy), TC-EXPORT-03 (PDF v3.5 happy CHỈ FR-11), xóa "Xuất Word .docx" khỏi action-bar §2.4 trừ khi BA confirm Word giữ song song PDF.

- **Bổ sung BA-Q tracker section ngay sau §2.6:** 3 câu hỏi treo (Word vs PDF / FR-IX-08 dia_ban contradiction / BR-DATA-06 50K vs 10K) với template `BA-Q-FR11-{ID}` để gate TC tương ứng (Sai spec → 🚫 cho tới khi BA confirm, không tự PASS).

- **Mở rộng permission matrix thành 11 role × {Xem dropdown loại BC, Chạy query, Tạo NHAP, Trình duyệt, Duyệt/Từ chối, Xuất XLSX, Xuất PDF, Xem AUDIT_LOG}** = 88 cell matrix. Có thể compress bằng grouping role giống permission-matrix.md project pattern, nhưng KHÔNG gộp action.

- **Thêm Bảng 1 + Bảng 2 (TC status snapshot + TC chưa chạy được) vào test-plan** theo CLAUDE.md §"2 bảng tổng hợp BẮT BUỘC". Hiện test-plan thiếu cả 2 — round QA chạy sẽ phải bổ sung vào functional-test-report-r{N}.md, không phải vào test-plan baseline (acceptable), nhưng nên có template trống sẵn.

- **Update terminology trong toàn test plan từ "Đợt đánh giá" → "Kế hoạch đánh giá"** (CHANGELOG line 556-560) + "Hỏi đáp pháp lý" → "Hỏi đáp pháp luật" (CHANGELOG line 523-526). Grep + replace + cite CHANGELOG entry.

- **TC-FR11-PERM-04 dn_9999999990 → 403 ERR-RPT-05 hợp lý, nhưng thêm TC-FR11-PERM-06 verify NHT/TVV/CG cùng nhận 403 chứ không phải "menu BC ẩn"** (test-plan AUTH-02 hiện gộp "403 / không có menu BC" — 2 outcome khác nhau, một cái permission-level một cái UI-level — phải tách).

- **Bổ sung Edge UI render: chart library degradation khi data > 100 buckets (line trend 12 tháng × 30 ngày = 365 points)**. UC146 (FR-IX-23 CT theo TG) edge case test-plan đã note "no data, 1 kỳ, full kỳ" nhưng miss perf degrade.

- **Audit log verify cần TC riêng + curl API check** (test-plan §2.1 BR-DATA-05 + TC-FR11-AUDIT-01 chỉ 1 dòng). Spec ghi "xem + xuất" — 2 action × 8 sample loại = 16 verify point, không 1 TC.

## Verdict

**REVISE** — Test plan có nền tốt (UC renumber map đúng +4, sampling strategy rõ ràng, 43 TC bao quát), NHƯNG có 3 issue chặn:
1. Hiểu sai bản chất Word→PDF change v3.5 (đổi format, không phải thêm format hybrid).
2. Bê nguyên contradiction nội bộ SRS v3.5 (FR-IX-08 địa bàn) mà không flag BA-Q.
3. Tự quyết 50K limit không escalate BA dù SRS contradict 50K vs 10K — vi phạm `feedback_deep_review_before_ba_defer`.

Fix 3 issue trên + 5 suggestion top priority (BA-Q tracker, terminology update, permission matrix tách cột, sampling cover VV phân tích, Audit log TC riêng) → **APPROVE**.

---

*Cite SRS: `srs-v3/srs-fr-11-bao-cao.md:85, 112, 1258` (BR-DATA-06 contradiction), `srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:508-518` (UC renumber +4), `:523-526` (terminology), `:542-549, 597` (FR-IX-08 contradiction), `:569-580` (Word→PDF).*
