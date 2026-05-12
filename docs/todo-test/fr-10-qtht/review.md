# Review — FR-10 QTHT test plan

**Reviewer:** agent-skills:code-reviewer (Claude self-review)
**Date:** 2026-05-12 12:15:00
**Source:** docs/todo-test/fr-10-qtht/test-plan.md

## Gaps

- **BR-DATA-06 (Export Excel) referenced nhưng MISSING khỏi §2.1 BR table.** Plan §2.4 "Cross-cutting features" liệt kê `[Xuất Excel] toolbar (BR-DATA-06)` và §2.4 SCR-VIII-01 ghi `BR-DATA-06 default`, nhưng bảng §2.1 không có row BR-DATA-06. SRS `:1355` quote nguyên văn rule export max 10.000 dòng. Phải thêm row BR-DATA-06 với cite `:1355` + cột "Áp dụng" liệt kê DM/DV/Vai trò/TK/NGAY_LE/AUDIT_LOG.
- **BR-UX-01 (URL sync filter) + BR-EC-01 (Optimistic locking) + BR-EC-13 (Search sanitize 200 chars)** referenced §2.4 nhưng MISSING khỏi §2.1. Note cuối §2.1 nói "đối chiếu thêm BR-EC-01 + BR-EC-13 khi viết TC detail" — đây là dấu hiệu plan chưa hoàn chỉnh. Phải pull rule từ `srs-v3.md Phụ lục B` vào bảng §2.1 NGAY trong overview, không defer.
- **BR-AUTH-04 quote chưa match SRS authoritative.** SRS `:2182` viết "**Chỉ TW thấy cấp con.** TW thấy toàn bộ dữ liệu TW + BN + ĐP. BN không có cấp con trực thuộc..." — plan §2.1 quote OK, nhưng `Áp dụng` SRS chỉ ghi FR-VIII-14 (Vai trò). Plan claim áp cho TC-09 permission tree (FR-VIII-16) — out-of-scope mapping. Sửa: ghi rõ "BR-AUTH-04 áp dụng cho FR-VIII-14, suy luận cho FR-VIII-16 phân quyền dữ liệu (cross-FR inference)".
- **ERR-LOG-03 / ERR-NL-04 missing.** TC-15 plan §4 hứa test "export 10K cap" và TC-16 verify Excel import Ngày lễ, nhưng SRS Error Handling FR-VIII-28 (`:1369-1370`) CHỈ có ERR-LOG-01/02 và FR-VIII-29 (`:1430-1432`) CHỈ có ERR-NL-01/02/03. KHÔNG có error code cho (a) export Excel vượt 10K dòng, (b) Excel import file sai schema / row corrupt. Thêm vào Phụ lục A ambiguity hoặc escalate BA — không tự nghĩ ERR code mới.
- **SM-TAIKHOAN bảng §2.5 ghi "9 transitions" nhưng list chỉ 9 dòng — trùng row `HOAT_DONG → TAM_KHOA` (auto 5-fail vs QTHT khóa thủ công).** Đây là 1 state transition với 2 trigger, không phải 2 transition độc lập (SRS `:2119-2120` cũng list 2 dòng). Plan §5 PASS criteria "9 transition đều cover" — clarify: 8 transition cardinality + 9 trigger source. Tránh tester đếm sai khi viết TC.
- **CHO_KICH_HOAT → VO_HIEU_HOA (auto quá 7 ngày)** ở SRS `:2125` có FR Ref `—` (trống). Test plan §2.5 cũng để trống. Cần escalate BA: ai trigger auto-expire? Cron job FR nào own? Nếu không có FR ref → không có TC ownership → defer log Ambiguity §A.
- **Permission Matrix §2.3 thiếu 4 role bắt buộc theo `output/permission-matrix.md` (49 entity × 11 role).** Plan list 7 role group (QTHT, CB_NV_TW, CB_NV_BN/DP, CB_PD_*, DN, NHT, TVV/CG) — gộp CB_NV_BN+DP cùng cột. Cần tách BN vs DP để verify BR-AUTH-03 "BN không thấy DP và ngược lại" rõ ràng. Thiếu role `admin` và `LD_BTP` nếu permission-matrix có.
- **AUDIT_LOG ghi `R (90 ngày + export 10K)` cho QTHT only.** Theo BR-AUTH-08 ngoại lệ ":AUDIT_LOG không có phân quyền", các role có quyền truy cập audit log phải cover trong matrix. SRS `:1369` ERR-LOG-01 "Bạn không có quyền truy cập nhật ký hệ thống" implies có check role — cần spec rõ AI có quyền R (chỉ QTHT? Hay LD_BTP cũng có?). Escalate BA hoặc thêm ambiguity row.
- **§1.2 row 6 FR-VIII-06 marked "Out-of-scope, xem FR-04" — chính xác,** nhưng §3 file structure không ghi note tránh tester search nhầm. Thêm comment block đầu §3.
- **Phụ lục A §4 (Tập ký tự đặc biệt password)** đề xuất test data `Abc@1234` (đủ) vs `Abc12345` (thiếu) — quyết định này không có BA sign-off. Nếu UI accept `Abc12345` mà test plan claim "thiếu special" → false-positive bug. Phải escalate BA chốt regex TRƯỚC khi viết TC detail file `08-TC-taikhoan.md`, không log bug khi BA chưa chốt.
- **TC count §4 "TỔNG 197" nhưng split P0/P1/P2 chỉ dự kiến (≈98/79/20), KHÔNG có rule mapping.** TC nào P0 vs P1? VD TC happy CRUD Lĩnh vực PL = P0 hay P1? Thiếu mapping criteria → PASS/FAIL §5 ("100% P0 pass") không enforceable. Thêm rule: "Happy + Permission positive = P0; Negative ERR-* validation = P1; Edge boundary/race = P2" hoặc tương đương.
- **§2.4 SCR-VIII-08 row "21 trường (FR-VIII-22 đại tu)"** — SRS BA Q8 chốt là **18 trường** (xem changelog `:21` "Q8 Acceptance '19 DN' → '18 DN'"). Plan claim 21 — sai số, recount theo SRS hoặc cite line đúng. Critical vì TC-12 dependency 100% trên field list này.
- **TC-13 VNeID happy path defer khi feature flag off** (§5 BLOCKED criteria) — không có owner. Ai bật flag? Khi nào test? Plan im lặng. Thêm field "Defer owner: BA / Infra" + ngày dự kiến enable feature flag.
- **§2.6 Upstream dependencies bảng** ghi `TAI_KHOAN` phụ thuộc `VAI_TRO, DON_VI`. Thiếu `DANH_MUC LOAI_TK` (Loại TK FR-VIII-13). Khi tạo TK CB nội bộ qua FR-VIII-15, field `loai_tk` là FK DANH_MUC — nếu DM trống → form fail validation. Thêm dep DM_LOAI_TK.

## Suggestions

- **Tách §2.3 Permission Matrix thành 2 sub-table:** (a) Module-specific entity × role; (b) BR-AUTH cross-cutting (BR-AUTH-01/03/04/08/09) × role với cite SRS line cụ thể. Subset của permission-matrix.md đầy đủ giúp tester run TC permission không lật doc gốc.
- **Thêm cột "Severity / Priority hint"** trong §1.2 FR list để tester biết FR nào P0 vs P1. VD `FR-VIII-15 TK NSD` = P0 (security), `FR-VIII-13 DM Loại TK` = P1 (CRUD chuẩn). Mapping rõ giúp resourcing.
- **TC-08 (Tài khoản NSD) nên thêm boundary check** `username regex ^[a-z0-9_]{4,50}$` (BR-AUTH-USERNAME-01) với 4 test data: `abc` (3 chars FAIL), `abcd` (4 chars PASS lower bound), `a*50chars` (50 PASS upper bound), `a*51chars` (51 FAIL). Test plan §4 count "5 happy + 8 negative" thiếu boundary explicit.
- **TC-12 DN self-reg** nên có race condition test: 2 DN cùng MST đăng ký đồng thời. Expected: 1 thành công + 1 ERR-REG-01 (duplicate MST). BR-EC-01 Optimistic locking apply ở insert race — hiện chỉ apply UPDATE/DELETE per §2.4. Clarify rule.
- **Thêm TC idempotency cho FR-VIII-26 (Quên MK):** user click link reset 2 lần → lần 2 phải ERR-PWD-04 (token đã dùng). Plan §4 TC-14 có 6 negative nhưng không nêu rõ idempotency. SRS `:1300` ERR-PWD-04 exists.
- **§2.4 SCR-VIII-10 phân trang 50/trang là exception của BR-DATA-07 (default 20).** Thêm row riêng trong §2.1 BR table: `BR-DATA-07-OVERRIDE-AUDIT` hoặc note rõ "AUDIT_LOG 50/page exception per `:1843`". Hiện note cuối SCR-VIII-10 dễ miss.
- **Đổi §3 file naming consistency:** một số file có prefix `0X-TC-DM-` (DM = danh mục), một số `0X-TC-<entity>` (vaitro, taikhoan). Đề xuất rename tất cả thành `0X-TC-<entity-slug>.md` không trộn prefix DM. VD `01-TC-linhvuc-pl.md` thay `01-TC-DM-linhvuc.md`.
- **Phụ lục A item 6 (4 loại SLA: Hỏi đáp / VV / Hồ sơ HT / Hồ sơ TT vs TVCS)** có nhắc delta map line 156 nhưng KHÔNG cite SRS authoritative line. Mở `srs-fr-10-quan-tri.md:486-505` (FR-VIII-10 SLA Inputs) verify enum loai_yeu_cau — nếu có 4 enum cụ thể thì quote luôn vào Phụ lục A để defer/clarify rõ ràng.
- **Thêm TC cho 5 fix V4-CHƯA-SỬA (C.1-C.5)** explicit trong §4 count. Plan có ghi delta map nhưng không map vào TC ID nào. VD C.1 password "ký tự đặc biệt" → TC-08-NEG-03; C.5 nút Phân quyền đã revert → verify SCR-VIII-03 KHÔNG có nút này (sanity check).
- **§5 PASS criteria thêm "100% transition SM-TAIKHOAN cover bằng evidence screenshot"** — không chỉ count cardinality. Tránh tester claim PASS mà evidence sparse.
- **Thêm row mapping `[GAP-VIII-*]` ở Phụ lục A.** Plan ref `[GAP-VIII-02]` (audit log) + `[GAP-VIII-04]` (password regex) + `[GAP-VIII-05]` (NGAY_LE) rải rác. Tổng hợp 1 bảng `GAP ID | Mô tả | Owner | Dự kiến chốt`.
- **§2.6 Phase dependencies thiếu Phase 3 (Workflow integration test cross-module).** VD test FR-VIII-15 auto-tạo TK khi FR-IV-07 tạo TVV — cross-module workflow nào trigger? Phải nói rõ test depend FR-04 plan.

## Verdict

**REVISE — must address gaps before execution.** Bảng BR §2.1 thiếu 4 BR critical (DATA-06/UX-01/EC-01/EC-13) đã referenced khắp §2.4; permission matrix gộp BN+DP che mất BR-AUTH-03 verify; field count SCR-VIII-08 sai (21 vs BA-chốt 18); thiếu mapping P0/P1/P2 rule + thiếu error code cho 2 edge case (export 10K, Excel import) — phải log Ambiguity + escalate BA trước khi tester drill xuống file TC detail.
