# Review — FR-16 API test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:08:00

## Gaps

- **G1 — Outbound coverage không cân giữa 9 cặp endpoint** (`test-plan.md:255-271` Bảng tổng TC). 3 endpoint `/danh-gia`, `/chuong-trinh-htpl`, `/ho-so-pl-dn` chỉ 2 TC/endpoint (1 happy + 1 negative), trong khi 6 endpoint kia có 3 TC bao gồm test exclude PII/MST/metadata. **Không có TC verify state filter** cho `/danh-gia` (chỉ `DA_DUYET_BC` được trả, không leak `DANG_THUC_HIEN`) — vi phạm BR-INTG-07 (SRS `srs-fr-16-api.md:1148-1155`). Cần thêm TC-OUT-DG-03 / TC-OUT-CT-03 / TC-OUT-DN-03 verify state filter draft KHÔNG hiện. Cũng thiếu cặp **list + search** đối xứng — endpoint search FR-XII-10/16/18 KHÔNG có happy TC riêng (chỉ gộp dưới "search edge" file 12).

- **G2 — Auth negative coverage chỉ 5 TC, thiếu 3 case quan trọng** (`test-plan.md:266`). Hiện có: no JWT, expired, sig sai, scope thiếu, mTLS cert sai. **Thiếu:** (a) JWT issuer sai (issuer ≠ `htpldn.moj.gov.vn` per SRS `srs-fr-16-api.md:83`), (b) JWT algorithm confusion (gửi HS256 thay vì RS256 — common attack pattern), (c) JWT thiếu claim `consumer_id`/`exp` (SRS line 84 yêu cầu 3 claims). 5 TC hiện tại chưa cover full BR-AUTH-01 surface. **Đề nghị nâng lên 8 TC auth negative.**

- **G3 — 8 TC Inbound BLOCKED hợp lệ NHƯNG thiếu trigger condition cụ thể** (`test-plan.md:55-70` + `:323-330` ambiguity §3). SRS FR-16 v3 KHÔNG có spec inbound (verify: SRS file 1176 dòng, không section "API Inbound"). Test plan đúng khi mark 🚫 Nhóm B "chờ dev BE spec". **Nhưng:** không nêu **acceptance gate** để unblock — cần điều kiện rõ "khi nào 8 TC này unblock" (BA confirm spec LGSP envelope + sandbox endpoint POST có sẵn + sample payload). Thiếu gate sẽ defer vô thời hạn. **Đề nghị:** thêm cột "Unblock condition" trong bảng §1.2.2 với 3 điều kiện: (a) BA confirm LGSP message envelope format, (b) Dev BE deploy sandbox `POST /api/v1/vu-viec`, (c) Sample client cert + signature key cấp cho QA.

- **G4 — Cross-module trigger auto-push KHÔNG được test** (user prompt nhắc "Cross-module trigger: auto push khi Hỏi đáp DA_DUYET / VV CONG_KHAI"). Test plan §1.2.2 hàng 8 có placeholder `POST /api/v1/notifications/cong-khai` (outbound trigger), nhưng **KHÔNG có TC riêng** trong bảng tổng (file 14 chỉ về inbound). SRS không quote rõ trigger này — chính là ambiguity #6 §7. Cần xác nhận **có cơ chế push event-driven hay không** (event bus / webhook / cron polling Cổng PLQG kéo về?). Nếu có, cần 2-3 TC: trigger fire khi state HD/VV/BM chuyển DA_DUYET/CONG_KHAI → notification call → log AUDIT_LOG bên outbound.

- **G5 — TC-FILTER chỉ có 2 sample, không cover 9 endpoint** (`test-plan.md:269` file 13). BR-INTG-07 (SRS `:1148-1155`) áp dụng cho **toàn bộ 9 endpoint outbound list**. Hiện chỉ TC-FILTER-01 (HOI_DAP) + TC-FILTER-02 (TVV). **Thiếu 7 endpoint:** dao-tao, vu-viec, danh-gia, bieu-mau, tvcs, ct-htpl, ho-so-pl-dn. State filter là kiểm chứng **chính** của module này — không thể sample 2/9. Đề nghị: TC-FILTER-01..09 (mỗi endpoint 1 TC verify draft/chờ duyệt KHÔNG xuất hiện). Hiện gộp vào "outbound happy" (file 01-09) không đủ — happy chỉ verify "có data DA_DUYET trả về", không verify "draft KHÔNG trả về".

- **G6 — Audit log compliance chỉ 1 TC, thiếu negative path** (`test-plan.md:269` file 13). TC-AUDIT-01 chỉ verify INSERT row sau call thành công. **Thiếu:** (a) verify AUDIT_LOG ghi cả khi response 401/403/429/500 (BR-DATA-05 SRS `:1157-1163` không loại trừ error case), (b) verify `consumer_id` chính xác trong row (không phải `null` khi JWT invalid), (c) verify `latency_ms` field có giá trị (test plan §2.1 ghi field này nhưng SRS line 1161-1163 KHÔNG có — fixture mismatch SRS, cần check lại). **Đề nghị:** mở rộng thành TC-AUDIT-01..04.

- **G7 — Performance test chỉ 1 TC, thiếu tail latency + load profile** (`test-plan.md:267` TC-PERF-01). BR-INTG-04 yêu cầu < 3s (SRS `:1139-1146`). TC-PERF-01 đo p95 < 3s qua sample 100 req — **chưa cover:** (a) concurrent load (vd 50 consumer × 2 req/s đồng thời), (b) tail p99/p99.9 (p95 thấp không loại trừ outlier 30s), (c) endpoint search (full-text thường chậm hơn list — cần đo riêng cho 9 search endpoint). Đề nghị thêm TC-PERF-02 (concurrent) + TC-PERF-03 (search latency).

- **G8 — Rate limit 429 chỉ 1 TC, thiếu reset window + per-endpoint scope** (`test-plan.md:267` TC-RATE-02). SRS `:1131-1136` ghi "100 req/min/consumer". **Câu hỏi mở chưa test:** (a) sliding window vs fixed window 60s? (b) rate limit per-consumer hay per-endpoint-per-consumer? (c) sau khi 429, đợi đủ retry-after có reset không? Cần TC-RATE-03 verify reset behavior + TC-RATE-04 verify scope (1 consumer call 50 req /hoi-dap + 60 req /vu-viec → 110 total nhưng mỗi endpoint < 100, expect 200 hay 429?). Ambiguity này cần BA confirm trước.

- **G9 — Pagination edge thiếu boundary 0 và overflow** (`test-plan.md:268` TC-PAG-01/02/03). Hiện có page=0→400, size=101→400/cap, size=100 boundary OK. **Thiếu:** (a) page âm (page=-1), (b) page=999999 (overflow, total_pages thực có 8), (c) size=0 (boundary dưới), (d) request không có `?page` `?size` → default 1+20 (SRS `:73` "default 20"). Đề nghị thêm 2-3 TC.

- **G10 — Bonus endpoint `/bieu-mau/{id}/download` chỉ 1 TC, thiếu binary integrity + auth scope** (`test-plan.md:53` + file 06 TC-OUT-BM-DL-01). SRS `:631` chỉ define `url_tai_ve` field, không spec auth scope cho download endpoint. Câu hỏi: (a) JWT scope `:read` đủ để download hay cần scope riêng `:download`? (b) Verify Content-Type (`application/pdf` vs `application/octet-stream`), (c) Verify file size match field `kich_thuoc` (SRS `:630`), (d) Verify file không corrupt (binary diff vs upload). Đề nghị mở rộng TC-OUT-BM-DL-01..03.

- **G11 — FR-XII-13 metadata-only verify field-level chưa rõ** (`test-plan.md:329` ambiguity §5). SRS `:697-704` list 6 field response (id, ma_yeu_cau, linh_vuc, trang_thai, chuyen_gia, ngay_hoan_thanh). Test plan ghi exclude `noi_dung_chi_tiet` (đúng — BR-FLOW-07 SRS `:685`). **Nhưng:** ambiguity về `tu_lieu_pl_lien_ket[]` chưa giải quyết (BA-confirm pending). TC-OUT-TVCS-03 cần định nghĩa **chính xác** list field whitelist + blacklist trước khi viết. Nếu BA confirm có expose `tu_lieu_pl_lien_ket`, schema response phải update.

- **G12 — JWT scope granularity test missing** (`test-plan.md:267` TC-AUTH-04). Hiện 1 TC "scope thiếu → 403". **Chưa test:** (a) JWT có scope `:read` call `/search` (scope khác `:search`) — expect 403, (b) JWT có scope `:read` 1 endpoint call endpoint khác (vd scope `hoi-dap:read` call `/vu-viec`) — expect 403, (c) JWT scope wildcard `htpldn:*:read` — accept hay reject? SRS `:124` ghi "Yêu cầu scope: {scope}" implies dynamic per-endpoint. Cần 3-4 TC scope-specific.

## Suggestions

- **S1 — Thêm cột "TC ID prefix per file" trong §3 (`test-plan.md:231-249`).** File 01-09 outbound: prefix `TC-OUT-<code>-NN`. File 10 auth: `TC-AUTH-NN`. File 11 rate/perf: `TC-RATE-NN` + `TC-PERF-NN` (đang trộn — split rõ). File 13: `TC-AUDIT-NN` + `TC-FILTER-NN`. Convention rõ → grep search cross-report dễ hơn.

- **S2 — Bổ sung section "Tooling matrix" §2.4.** Test plan ghi tool curl/Postman/Bruno/k6 nhưng không chỉ định **tool nào cho TC nào**. Đề nghị: curl + jq cho 30 TC functional (auth/outbound/payload), Bruno collection cho regression suite, k6 cho rate limit + perf, pytest+requests cho TC cần fixture pre-call (vd reset rate limit counter). Tooling assignment giúp QA mới onboard nhanh.

- **S3 — Cite SRS line cho cột "Filter state cuối" trong bảng §1.2.1 (`test-plan.md:32-51`).** Hiện chỉ paraphrase ("`trang_thai=DA_DUYET`"). Đề nghị thêm cite SRS line: vd FR-XII-01 → `srs-fr-16-api.md:168` (input default `DA_DUYET`) + `:1010` (entity CHECK constraint). Giúp tester verify nhanh khi viết TC chi tiết.

- **S4 — Thêm hyperlink cross-ref upstream module test plan §2.6.** Hiện list "Seed trước tại module FR-02/03/.../15" dưới dạng text. Đề nghị link `[FR-02 Hỏi đáp test plan](../hoi-dap/test-plan.md)` để khi seed upstream gap, tester click sang nhanh — đặc biệt với HOAT_DONG/DA_DUYET_BC/DA_CONG_BO là state cuối lifecycle riêng từng module.

- **S5 — `POST /api/v1/auth/token` (consumer xin JWT) nên ưu tiên cao hơn P2** (`test-plan.md:67`). SRS không spec — nhưng đây là **prerequisite** cho mọi TC khác (consumer cần JWT trước khi call 18 outbound). Nếu endpoint này không tồn tại / format khác, ALL 31 testable TC sẽ block. Đề nghị: split thành TC-AUTH-00 "Verify cấp JWT flow" — P0, làm trước cả TC-AUTH-01, có thể là smoke prerequisite cho round.

- **S6 — Pass gate G3 (`test-plan.md:296`) nên thêm requirement explicit về error envelope structure**, không chỉ "HTTP code đúng". BR-API-ERR-01 (SRS `:120-128`) yêu cầu envelope `{success: false, error: {code, message, details}}`. Tester có thể PASS HTTP code nhưng envelope sai format → vẫn miss bug FE consumer parser. Đề nghị G3 ghi "HTTP code + envelope match shape BR-API-ERR-01 + message text khớp SRS quoted exact".

- **S7 — Note ambiguity §7 nên có timestamp + owner** (`test-plan.md:323-330`). Hiện list 6 ambiguity không có deadline / owner cụ thể. Đề nghị format mỗi row: `Asked: <BA name>` + `Asked on: 2026-05-12` + `Deadline: 2026-05-19`. Tránh defer vô thời hạn — 6 ambiguity là gating cho file 10 + 14, cần chốt trước round live.

- **S8 — Audit log query verify cần định nghĩa `GET /api/admin/audit-log` endpoint** (`test-plan.md:160`). Test plan giả định có endpoint admin để query AUDIT_LOG nhưng SRS không spec. Nếu chưa có endpoint → fallback query DB trực tiếp (qua DBA). Đề nghị thêm pre-check: "Trước round, confirm với Dev BE: có endpoint admin audit log không? Nếu không, có quyền DB read AUDIT_LOG cho QA không?" Tránh G6 TC-AUDIT block phase verify.

- **S9 — TC `/danh-gia` chỉ 2 TC có thể không đủ** vì entity ghép `DOT_DANH_GIA` + `KET_QUA_DANH_GIA` (SRS `:567`). Cần verify response **không leak** `KET_QUA_DANH_GIA` chi tiết per-VV (đây là dữ liệu nhạy cảm DN-level). Đề nghị TC-OUT-DG-03: verify response chỉ chứa aggregate fields (`diem_trung_binh`, `so_vu_viec_danh_gia`), KHÔNG có array `vu_viec[]` detail.

- **S10 — Cân nhắc tách file 12 "Payload edge" thành 2 file:** (a) `12a-TC-PAYLOAD-pagination-search.md` (TC-PAG + TC-SEARCH), (b) `12b-TC-PAYLOAD-date-range.md` (TC-DATE). Hiện 6 TC trộn 3 nhóm (pagination, search keyword, date range) — split giúp rerun chỉ subset khi cần.

## Verdict

**REVISE** (không APPROVE)

**Justification:**

1. **Critical: TC-FILTER chỉ 2/9 endpoint cover BR-INTG-07** (G5) — đây là rule **chính** của FR-16 (chỉ chia sẻ data publishable, SRS `:1148-1155`). Sample 2/9 = 22% coverage cho rule core → có thể leak draft data ở 7 endpoint kia mà không biết. Phải có TC-FILTER-01..09 trước khi approve.

2. **Critical: Auth negative thiếu issuer/algorithm/claim** (G2) — JWT RS256 issuer = `htpldn.moj.gov.vn` (SRS `:83`) là core security boundary. Không test issuer mismatch / algorithm confusion / missing claim = miss 3 common JWT attack vector. P0 module no UI có security surface lớn nhất hệ thống, không thể skip.

3. **Important: G1 + G6 + G7 + G12 (uneven coverage, audit negative, perf single-TC, scope granularity)** — đều fix được trong 1 round revise. Test plan có baseline đúng (39 TC, phân P0/P1/P2 rõ, ambiguity tracked) nhưng gaps trên đủ để miss bug nghiêm trọng nếu release theo plan hiện tại.

4. **8 TC inbound BLOCKED hợp lệ** — phân loại Nhóm B đúng theo CLAUDE.md (chờ dev BE spec LGSP). Không count vào reject reason. Nhưng cần thêm unblock condition rõ (G3).

**Done well:**
- Phân nhóm SRS v3.5 chính xác (Nhóm D, Δ ≈ 0%) — sibling check 9 module upstream rõ.
- Ambiguity §7 chủ động list 6 unknowns trước khi viết TC chi tiết — đúng spirit "ask BA before defer".
- BR matrix §2.1 cite SRS line cụ thể từng row — verify nhanh khi tester onboard.
- Tách rõ KHÔNG có UI / state machine + giải thích tooling thay thế (curl/Bruno/k6) — phù hợp module no-SCR.
- Tier dependency §2.6 + entity-map link → workflow seed upstream-first đúng pattern.

**Next step:** Revise §3 file plan thêm TC-FILTER-01..09 + auth negative TC-AUTH-06..08 + audit TC-AUDIT-02..04. Re-submit review sau khi BA confirm 6 ambiguity §7 (đặc biệt #2 HMAC, #3 LGSP envelope, #5 TVCS field whitelist).
