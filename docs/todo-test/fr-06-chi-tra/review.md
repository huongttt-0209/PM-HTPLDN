# Review — FR-06 Chi trả test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:49:01

## Gaps

- **G1 — Thiếu TC dedicate "CHẶN nhập tay UI".** Plan có quote line 950 ("Nguồn duy nhất: DVC qua LGSP") tại §2.4 và bullet ❌ Nút [Thêm mới], nhưng **bảng TC §4 không có TC nào verify "SCR-V.II-01 KHÔNG render nút [Thêm mới] cho cả 7 role CB_NV/CB_PD"**. Đặc thù module duy nhất bị chặn nhập tay (system-overview §4.12 line 717) phải có TC chuyên — đề nghị thêm `TC-LIST-04: 7 role × SCR-V.II-01 không có button [Thêm mới] / [Tạo HS chi trả] (absence assertion + DOM grep)`.

- **G2 — TC-BS-05 conflate 2 hành vi khác nhau.** Dòng plan ghi "Loop 3 lần bổ sung — bo_sung_count: 1→2→3 + Lần 4 hành vi chờ BA Q1" gộp 2 việc trong 1 TC. Loop 3 lần là **happy path verify count + UI highlight đỏ ≥2** (đã có SRS quote line 977/1184), KHÔNG defer. Lần 4 là `🤷 BA Q1`. Phải split: `TC-BS-05a Happy P0` (loop 3 lần) + `TC-BS-05b Edge P1` (lần 4 mark 🤷 nhóm C BA per CLAUDE.md TC classification).

- **G3 — Cross-ref FR-05 (VV HOAN_THANH) chưa có TC.** SRS line 1248-1252 + plan §2.6 (Tier 4 upstream) khẳng định HSCT phụ thuộc VU_VIEC ở state `HOAN_THANH`, nhưng §4 không có TC verify "LGSP inbound với `vu_viec_id` ở state `DANG_XU_LY` (chưa HOAN_THANH) phải reject". Đề nghị `TC-API-07: payload reference VV ≠ HOAN_THANH → 400 (FK-state gate)`.

- **G4 — Cross-ref FR-14 (số HĐ TVPL) chưa test.** SRS line 1164-1165 (`so_hop_dong_tvpl`, `ngay_hop_dong`) — không có TC verify số HĐ phải khớp HOP_DONG_TU_VAN entity (FR-14). Đề nghị `TC-API-08: HSCT inbound có `so_hop_dong_tvpl` không tồn tại trong FR-14 → reject hoặc warning`.

- **G5 — Cross-ref FR-07 DOANH_NGHIEP.quy_mo: snapshot (EC-04) test coverage mỏng.** TC-CALC-09 đề cập snapshot SIEU_NHO → NHO nhưng KHÔNG nói rõ cách trigger DN đổi quy mô (qua FR-07 update endpoint? Backend seed? UI?). Acceptance ambiguous. Đề nghị viết step rõ "Step 1 seed DN quy_mo=SIEU_NHO, Step 2 LGSP inbound HSCT-A, Step 3 update FR-07 DN.quy_mo=NHO, Step 4 verify HSCT-A.muc_ho_tro_phan_tram giữ 100%".

- **G6 — TC-CALC boundary thiếu 2 edge.** Plan có 9 TC-CALC nhưng miss: (a) **`da_chi_trong_nam = tran_ho_tro_nam` exact** (EC-05 line 430): test boundary chính xác = trần, không phải > trần; (b) **Snapshot quy mô năm cũ vs năm mới (1/1 reset)** — SRS line 1028 "Reset trần chi phí/năm vào 1/1 hàng năm". Đề nghị thêm `TC-CALC-11: da_chi=5M exact = trần NHO → 0 + cảnh báo` và `TC-CALC-12: HS năm 2025 đã chi 5M, HS năm 2026 mới reset → 5M available`.

- **G7 — Permission matrix §2.3 inconsistent với §1.3.** §1.3 list `TVV/CG (huongcg, BTP-TW)` cho UC75 (in-app nhận TB) — đúng. Nhưng matrix §2.3 row "HO_SO_CHI_TRA Read" ghi `TVV: R (chỉ HS gắn TVV mình)` — chưa có SRS quote line. SRS line 514-548 (FR-V.II-08) chỉ nói TVV nhận **THONG_BAO**, KHÔNG nói TVV được GET HSCT detail. TC-PERM-07 đang test "TVV truy cập `/chi-tra/:id` mà không phải tu_van_vien_id mình → 403" — implicit assume TVV có permission Read khi đúng `tu_van_vien_id`. Đề nghị BA confirm trước, mark 🤷 nhóm C BA nếu ambiguous, hoặc split: TC-PERM-07a (TVV truy cập HS không match → 403) + TC-PERM-07b (TVV truy cập HS match `tu_van_vien_id` → 403 hoặc 200, defer BA).

- **G8 — CR-01 hard-delete TC ambiguous về phương pháp test.** TC-CR-01 ghi "Hard-delete HSCT — record gone DB, AUDIT_LOG retained". Nhưng SRS không có endpoint DELETE cho HSCT (UC duy nhất là DVC inbound, không có "xóa" UC nào trong FR-V.II-01..14). Hard-delete chỉ áp dụng cho admin / cleanup script? Plan không nói rõ trigger. Đề nghị clarify "Hard-delete chỉ áp dụng khi `trang_thai=HUY` qua admin script, KHÔNG có UC user-facing delete" hoặc defer mark 🤷 BA.

- **G9 — Thiếu TC LGSP outbound (FR-V.II-04 + FR-V.II-10).** Plan có FR-V.II-04 "Thông báo qua DVC outbound" + BR-RETRY-01 retry 3×30s, TC-API-05 test timeout. Nhưng **không có TC verify outbound success-case** (CB NV xác nhận kiểm tra → DVC nhận TB → DN nhận TB) end-to-end. Cũng không có TC verify FR-V.II-10 (TB kết quả thẩm định cho TVV in-app + email). Đề nghị thêm `TC-NOTIF-02: state transition → THONG_BAO INSERT + verify channel (DVC outbound / in-app / email)`.

- **G10 — TC-PD-02 acceptance thiếu side-effect.** "CB PD trả về DANG_THAM_DINH" — SRS line 737 chỉ rõ "KHÔNG ghi `thoi_gian_tu_choi`". Acceptance TC-PD-02 chưa list verify `thoi_gian_tu_choi` vẫn NULL sau khi trả về. Phải bổ sung step "verify `HO_SO_CHI_TRA.thoi_gian_tu_choi IS NULL` qua API GET detail".

- **G11 — BR-AUTH-02 nhắc "Δ v3.5 đổi từ 3 cấp xuống 2 cấp" nhưng KHÔNG có TC.** §2.1 row BR-AUTH-02 ref `_DELTA-MAP-FR06.md:45` "TW → {BN, ĐP}". Bảng TC §4 không có TC nào verify "không còn cấp HUYEN/XA" (ví dụ login CB_NV_HUYEN nếu user còn tồn tại → 403 hoặc map về DP). Đề nghị `TC-PERM-08: account cấp cũ (nếu tồn tại) thử Read HSCT → 403`.

- **G12 — Pagination TC trùng + miss boundary.** TC-LIST-02 "Pagination 20/page default, max 100" — chỉ 1 TC cover 2 BR (default + max). Đề nghị split: TC-LIST-02a (default 20) + TC-LIST-02b (request size=150 → cap 100 + warning hoặc 400). BR-DATA-07 line 1400-1404.

- **G13 — Số tiền duyệt boundary > so_tien_duoc_ho_tro (EC-02 line 427) không có TC.** EC-02 nói "so_tien_thuc_tra KHÔNG được > so_tien_duoc_ho_tro. Validate tại bước phê duyệt". Plan có TC-CALC-10 + TC-TT-02 cover bước thanh toán, nhưng KHÔNG có TC verify CB PD nhập `so_tien_duyet > so_tien_de_nghi` → reject (validate at approval). Đề nghị `TC-PD-05: CB PD nhập so_tien_duyet > tính toán BR-CALC-02 → reject hoặc warning`.

- **G14 — TC-AUDIT-01 quá coarse — 14 transition cần 14 row AUDIT.** "Mỗi state transition INSERT AUDIT_LOG đủ 4 field" — quá generic, không verify đủ 14 transition trong SM. Đề nghị split thành TC-AUDIT-01a (transition 1-7) + TC-AUDIT-01b (transition 8-14) hoặc parametrize bằng table 14 row.

## Suggestions

- **S1 — Thêm cột "Test method" trong bảng §4** (UI MCP / API curl / DB query). TC-API-* chắc chắn API; TC-PERM-* chắc UI MCP `new_page isolatedContext` per role; TC-CALC-* hybrid (UI verify display + API verify response). Hiện tại tester phải đoán.

- **S2 — Reorder §4 chi tiết bảng theo FR order, không random.** Hiện tại TC-API-01..06 → TC-LIST → TC-TN → TC-KT → TC-BS → TC-CALC → TC-TD → TC-PD → TC-FLOW → TC-TT → TC-PERM → TC-AUDIT → TC-EDGE → TC-CR. Đề nghị nhóm theo FR (V.II-01 → V.II-14) + appendix cross-cutting (PERM, AUDIT, EDGE, CR) để dễ trace SRS coverage.

- **S3 — Sửa BR-CALC-04 nguồn cite.** §2.1 BR-CALC-04 ghi "suy diễn từ EC-04" line 429 — nên đổi quote nguyên văn EC-04 "Áp dụng quy mô tại thời điểm nộp hồ sơ (snapshot)" thay vì "suy diễn".

- **S4 — Thêm mock LGSP setup chi tiết trong §2.6 hoặc phụ lục.** "Mock LGSP" nhắc 3 lần nhưng không có script template. Đề nghị bổ sung sample curl `POST /api/v1/lgsp/chi-tra/inbound` payload (Mẫu 01 NĐ55 18 trường + JWT header) trong appendix để tester copy-paste.

- **S5 — TC-PD-02 (trả về) nên có TC mirror "CB NV trình lại sau khi sửa".** Đã có TC-FLOW-01 (2 lần trả về + 1 duyệt) nhưng acceptance gộp 3 lần. Tách thêm `TC-PD-02b: sau trả về, CB NV [Trình PD] lại → CHO_PHE_DUYET + bản ghi PHE_DUYET thứ 2 INSERT`.

- **S6 — Add data table cho TC-CALC.** TC-CALC-01..09 mỗi TC 1 dòng — đề nghị 1 bảng input/expected matrix (`quy_mo / phi_tv / da_chi / so_tien_de_nghi / expected so_tien_duoc_duyet`) dễ review formula correctness.

- **S7 — §7 Open issues item 4 (Đối tác TT CNTT mục 07) viết "không áp được" — nên reword thành "out-of-scope FR-06"** hoặc chuyển sang section "Excluded from scope" tách bạch open-issue (cần BA confirm) khỏi confirmed-exclusion (đã quyết định OUT).

- **S8 — Thêm acceptance dòng "negative absence" cho TC-LIST/SCR.** UI test thường miss verify "element X **không hiển thị**". Plan §2.4 đã list 4 ❌ feature không có, nhưng TC §4 không có TC absence-assertion tương ứng. Đề nghị thêm `TC-LIST-05: DOM grep absence button "[Thêm mới]" / "[Auto từ chối]"`.

- **S9 — TC-EDGE-02 (optimistic lock) nên có version conflict scenario rõ.** "2 CB NV cùng thẩm định 1 HS — version conflict → ERR-SYS-02". Đề nghị spec rõ: CB_NV_TW + CB_NV_BN cùng GET → cả 2 nhận `version=1` → CB_NV_TW PATCH thành công (`version=2`) → CB_NV_BN PATCH với `version=1` → 409 ERR-SYS-02.

- **S10 — Verdict gate §5 nên add cross-cutting gate.** "100% P0 + 90% P1 pass" chưa cover regression với FR-05/07/14. Đề nghị thêm gate "Sau khi FR-06 PASS, smoke 5 phút FR-05 (VV HOAN_THANH) + FR-07 (DN.quy_mo) + FR-14 (HĐ) để chắc không break upstream" (per CLAUDE.md Rule 4 nhóm C IMPACT).

- **S11 — File §3 11-REVIEW-edge-case-hunter.md đánh dấu optional — nên required cho XL module.** XL module 14 FR + 5 BR-CALC + cross-cutting CR — edge-case-hunter pass đáng giá để catch combinatorial gap.

- **S12 — §1.3 user table có lỗi typo cấp "(BN)".** Row `CB_NV_BN: cb_nv_bn_01 (BKH) / cb_nv_bn_02 (BTC)`. Convention `_02` là **fallback cùng đơn vị** (xem CLAUDE.md Rule 7), nhưng BKH ≠ BTC = khác đơn vị BN. Phải dùng `cb_nv_bn_01 (BKH)` primary và `cb_nv_bkh_02` (nếu có) làm fallback. Cross-bộ test cần TC riêng, không phải fallback. Đề nghị verify users.csv + correct convention.

## Verdict

**REVISE** — test plan có chiều sâu tốt (28 BR + 26 ERR code + 14 transition + 55 TC), cover được BR-CALC-01/02 formula chính xác + DN bổ sung 3 lần loop + CB PD trả về DANG_THAM_DINH (Δ v3.5 đúng SRS line 737/766) + permission matrix 10 role + cross-cutting CR-01/02. Tuy nhiên có 14 gap cần fix trước khi execute, đặc biệt:

1. **G1 thiếu TC chặn nhập tay UI** — đây là đặc thù UC duy nhất, không thể merge.
2. **G2 TC-BS-05 conflate** — happy path loop 3 lần và defer lần 4 phải tách.
3. **G3+G4+G5 cross-module FR-05/07/14 chưa có TC trực tiếp** — Tier 4 upstream dep mention ở §2.6 nhưng không xuống TC.
4. **G6 calc boundary thiếu 2 edge** (exact-trần + 1/1 reset) — XL module cần coverage tối thiểu 11 TC-CALC.

Sau khi fix 14 gap + 12 suggestion (ưu tiên S1, S6, S9, S11), test plan đạt mức APPROVE. Estimate effort revision: 4-6 giờ (thêm 8-10 TC mới + restructure §4 + bổ sung mock LGSP appendix).
