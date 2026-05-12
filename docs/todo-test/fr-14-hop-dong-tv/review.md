# Review — FR-14 HĐTV test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:48:26

## Gaps

- **Bên A field semantics over-extended (line 80 test plan, BR-HDTV-10).** Plan claim "Bên A auto-fill từ `don_vi_id` của user login (KHÔNG cho user nhập)" cite `srs-v3/srs-fr-14-hop-dong-tv.md:81,263`. SRS line 81 chỉ ghi `ben_a | text | Y | Bên A (đơn vị quản lý) | auto đơn vị | hệ thống` — "auto đơn vị" + "Nguồn: hệ thống" KHÔNG explicit cấm user edit. SRS line 263 form spec ghi `Bên A (auto đơn vị)` — vẫn ambiguous. Cần SPEC-CLARIFY "Bên A là readonly hay editable sau auto-fill?" trước khi P0 TC-CRUD-02 fail UI có thể chỉnh.

- **Liên kết Vụ việc — hướng FK ngược.** Plan TC-LINK-VV-01..03 model "N:N" cite `srs-v3/srs-fr-14-hop-dong-tv.md:88` (`vu_viec_ids | identifier[]` input field) + `:241` (entity-map). Nhưng ERD line 325-326, 346-347 + 397 mô tả `VU_VIEC.hop_dong_tv_id FK → HOP_DONG_TU_VAN` — đây là **1:N** (1 VV → 1 HĐ), KHÔNG N:N. Mâu thuẫn nội tại SRS (input table vs ERD). Plan default theo input "N:N" mà chưa flag contradiction → MISS bug spec. Cần SPEC-CLARIFY-HDTV-04.

- **BR-HDTV-03 wording (xóa khi có VV) — chưa định nghĩa "có VV liên kết".** SRS line 122 + 159 + 272 chỉ nói "không có vụ việc liên kết". Sau soft-delete VV (`is_deleted=1` / `da_xoa=1`) thì còn count là "có liên kết" không? Plan TC-DEL-02 không cover edge "VV liên kết đã soft-deleted → xóa HĐ có cho phép không?". Bug latent: BE có thể filter `da_xoa=0` hoặc không.

- **CR-01 cross-cutting cite vô căn cứ (line 8, 84, 260, 315).** Plan reference "CR-01 — 5 trường công khai" cho HĐTV, nhưng KHÔNG cite SRS line. SRS local `srs-fr-14-hop-dong-tv.md` không có mention "5 trường công khai" / "CR-01" / "publish PLQG" → đây là cross-cutting context, plan đã correctly mark NOT applicable (line 150) nhưng TC-CROSS-02 (P1) test "negative — KHÔNG có toggle Công khai" vẫn keep — risk waste effort. Nếu là spec global cross-cutting, phải cite file SRS update v3.5 cross-cutting cụ thể. Hiện chỉ cite từ CLAUDE.md narrative.

- **Status workflow defer correct nhưng P2 phân loại không nhất quán.** SPEC-CLARIFY-HDTV-01 đúng. Tuy nhiên §4 không có TC-SM-01..04 thực tế (chỉ ref §2.5). Nếu defer = bỏ luôn TC, plan nên loại khỏi danh sách §1.2 row 1 ("CRUD + Accordion" không bao gồm transition). Hiện inconsistent giữa §2.5 (mark UNVERIFIED) và §4 (không có hàng TC-SM nào).

- **Permission TVV/CG "Xem HĐ chính mình" — SRS không có explicit grant.** Plan TC-PERM-TVV-01 (P1) cite `02-thu-tu-module.md:650` (tab "Lịch sử hỗ trợ" SCR-IV-03). SRS FR-X.3-01 line 67 chỉ ghi tác nhân CB_NV; FR-X.3-02 line 183 thêm CB_PD. KHÔNG nhắc TVV/CG có quyền read HĐ. Cite `02-thu-tu-module.md` là quy trình nghiệp vụ, KHÔNG phải SRS BR. Cần verify NotebookLM + grep SRS FR-IV (TVV) cho UC tab Lịch sử trước khi keep TC này.

- **TC-CRUD-04 concurrency (BR-HDTV-07 UNIQUE) — test method missing.** P1 test "2 user TW tạo HĐ cùng ngày → 2 SEQ khác nhau". Plan không nêu cách reproduce concurrency qua MCP (single browser session). Cần script API parallel POST hoặc 2 isolatedContext race. Risk: tester PASS bằng tạo tuần tự (không phải concurrency thực).

- **Pagination TC thiếu test "max 100" (BR-DATA-07).** Line 79 BR define "default 20, max 100". Plan TC-PAG-01 chỉ test 20/page default. Thiếu TC verify reject `?limit=101` hoặc UI dropdown cap 100.

- **Audit log diff content not specified.** TC-CRUD-06 "verify AUDIT_LOG ghi diff trước/sau". SRS BR-DATA-05 line 491-497 chỉ nói "ghi vào AUDIT_LOG" — không define "diff trước/sau" format. Cần SPEC-CLARIFY or pull từ Phụ lục B file chính srs-v3.md.

- **Bảng 2 nguyên nhân block (CLAUDE.md §6 nhóm A-F) chưa có cho 3 SPEC-CLARIFY.** Plan §5 nêu BLOCKED criteria. Đã liệt kê 3 ticket nhưng chưa phân nhóm theo A-F (nên là **C** Chờ BA confirm spec) trong format Bảng 2 chuẩn project.

## Suggestions

- Thêm TC-SEARCH-06 verify `keyword` SQL injection / XSS sanitize — search input free-text qua `bên B` là vector inject thường gặp. Cross-ref BR-EC-13 file chính srs-v3.md Phụ lục B nếu có.

- Split TC-LINK-VV-02 (filter VV theo BR-AUTH-08) thành 2 case: (a) CB_NV BN-BKH thấy chỉ VV BN-BKH, (b) khi cross-link VV BN-BKH vào HĐ TW → reject/accept? SRS chưa rõ.

- Thêm explicit verify query trong TC-CROSS-01 (rename `is_deleted` → `da_xoa`): list `list_network_requests` filter `/api/v1/hop-dong-tu-van` response payload schema có field `da_xoa` (không phải `is_deleted`). Nêu file cross-cutting SRS để cite line (hiện chỉ "v3.5 cross-cutting" generic).

- TC-TT-EDGE-02 (SUM + 1đ → reject) thêm boundary âm: SUM `= 0` (no payment) — verify progress bar 0% render đúng.

- Thêm TC-FILE-01 file upload edge: MIME validation, size cap, max number files (BR-EC-12 file size limit nếu có Phụ lục B). Plan TC-CRUD-05 chỉ test "save multi-file" không cover negative.

- §1.3 thêm role `cb_pd_bn` / `cb_pd_dp` để verify CB_PD scope theo cấp đơn vị (FR-X.3-02 line 183 nói "TW/BN/ĐP"). Hiện chỉ `cb_pd_tw_01`.

- Phối lại §4 chia subsection theo file (01 / 02 / 03...) thay vì flat 39-row table — dễ navigate cho tester.

- Thêm tag `[SPEC-CLARIFY]` inline trong TC ảnh hưởng (vd TC-SM-* TC-CROSS-03 TC-PERM-TVV-01) để khi BA reply, tester grep nhanh ticket → TC.

## Verdict

**REVISE** — Plan structure solid, BR/Error coverage thorough, sibling-check OK, 3 SPEC-CLARIFY tickets correct. Tuy nhiên 3 gap nghiêm trọng: (1) BR-HDTV-10 "Bên A readonly" over-extend SRS, (2) hướng FK VV mâu thuẫn ERD vs Input table chưa flag, (3) TC-PERM-TVV-01 cite quy trình thay vì SRS BR. Cần SPEC-CLARIFY-HDTV-04 (FK direction) + clarify BR-HDTV-10 readonly + verify quyền TVV embedded trước khi sign-off GĐ 3.
