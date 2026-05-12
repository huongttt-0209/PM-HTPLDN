# Review — FR-13 TV nhanh test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:35:00
**Plan file:** `/Users/teamai/Downloads/antigravity/QA/skilkk/docs/todo-test/fr-13-tv-nhanh/test-plan.md` (395 dòng)
**SRS authoritative:** `input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md` (v3.5)

---

## Gaps

- **G1. Thiếu TC cross-module auto-feed FR-02 → KHO_CAU_HOI (TC-KHO-002 nông).** TC-KHO-002 chỉ mô tả "Auto-feed khi HOI_DAP → DA_DUYET" nhưng KHÔNG verify: (a) khi trigger từ FR-02 thì `nguon=TU_DONG` + `hoi_dap_goc_id` được set đúng FK, (b) Q&A auto KHÔNG đi qua CHO_DUYET (vào thẳng DA_DUYET — SRS §114), (c) idempotency khi HOI_DAP DA_DUYET → HUY → DA_DUYET lại (tạo dup record?). Cite SRS line 114, line 696 `hoi_dap_goc_id FK`.

- **G2. SM-KHOCAUHOI có state `NHAP` không khớp entity CHECK constraint — không có TC verify mâu thuẫn.** Plan §2.5 dòng 206 + transition table dòng 221 dùng state `NHAP` (từ chối → NHAP). SRS line 697 CHECK constraint chỉ có `('CHO_DUYET','DA_DUYET','CONG_KHAI','HET_HIEU_LUC')` — **không có `NHAP`**. Nhưng SRS line 103 (Inputs FR-X.2-01) + line 537 (UI filter) + line 543 (Tu choi SET NHAP) thì CÓ `NHAP`. Mâu thuẫn nội bộ SRS — plan phải log vào §7 SPEC-CLARIFY nhưng đang miss.

- **G3. CR-01 5 trường công khai không có TC validate boundary.** Plan liệt kê `anh_dai_dien` (max 5MB jpg/png/gif), `file_dinh_kem_cong_khai` (max 20MB/file, PDF/DOC/DOCX/XLS/XLSX, nhiều file), `mo_ta_cong_khai` (text long) — SRS line 105/107/704-705 — nhưng không có TC negative cho: upload file 5.1MB (boundary), upload .exe/.zip (MIME validation), upload 21MB PDF, upload 0 byte file. Đây là attack surface công khai ra Cổng PLQG, phải có Edge.

- **G4. Permission scope cho FR-X.2-06 Công khai theo `don_vi_id` chưa test.** SRS line 461 "Kiểm tra quyền CB NV + phạm vi phân quyền theo đơn vị". Plan có TC-KHO-PERM-01 cho Kho (BR-AUTH-03) nhưng **không có TC** verify CB_NV_BN BKH KHÔNG được công khai Q&A của BN BTC (BR-AUTH-08 cross BR-PUBLIC). FR-X.2-06 là entry point sensitive — đẩy data ra public Internet — thiếu permission test là gap nghiêm trọng.

- **G5. FR-X.2-04 (DN search Cổng PLQG) chỉ có 2 TC nhưng search là attack surface chính.** File `03-TC-cong-khai-search.md` chỉ 2 TC (1 Happy + 1 Permission), trong khi FR-X.2-04 cần: (a) full-text search Vietnamese diacritics (cà phê ≈ ca phe?), (b) ranking relevance DESC verify, (c) DN không thấy `CHO_DUYET`/`HET_HIEU_LUC`/`hieu_luc=false`, (d) outbound API endpoint exact path (Plan §7 dòng 387 đã đánh dấu TODO UNVERIFIED nhưng không tạo TC stub block status). Coverage < 3 TC cho FR Essential = under-spec.

- **G6. TC-TVN-API-002 Idempotency thiếu boundary 24h.** SRS line 380 + line 402 specify cache `Idempotency-Key` **24 giờ**. TC-TVN-API-002 chỉ test "gửi lại cùng key → 409". Thiếu Edge: (a) gửi lại sau 24h+1s với cùng key — phải tạo record mới hay reject? (b) `Idempotency-Key` không phải UUID format → 400? (c) concurrent 2 request cùng key trong 100ms — race condition.

- **G7. ERR-DG-TVN-01 boundary chưa kỹ.** TC-TVN-API-004 "điểm ngoài [1..5]" — nhưng `diem` SRS line 739 CHECK `diem ≥ 1 AND diem ≤ 5`. Plan không nêu rõ test float (4.5?), test 0/6 (boundary), test string "5" vs number 5, test negative -1. CHECK constraint là integer range hay decimal — SRS không chốt → plan phải log SPEC-CLARIFY hoặc cover all variants.

- **G8. Audit log TC-KHO-018 + TC-CK-005 chỉ "verify INSERT-only" — không verify schema fields.** BR-DATA-05 (SRS line 864) yêu cầu immutable. Plan không nêu fields cần check trong AUDIT_LOG row: actor_id, action, entity_id, before/after diff, timestamp, IP. Tester sẽ không biết verify cái gì. Cite SRS line 864 → expand acceptance.

- **G9. SM-TVNHANH transition `CB_TRA_LOI → HOAN_THANH` qua "Đẩy Nhóm II" KHÔNG có trong SRS chính thức.** SRS line 808-811 mermaid + bảng 826-829 CHỈ có 4 transition: [*]→MOI, MOI→CB_TRA_LOI, CB_TRA_LOI→HOAN_THANH (DN đánh giá), MOI→HET_HAN. Transition "Đẩy Nhóm II → HOAN_THANH" được nhắc ở FR-X.2-02 step 9 (line 204) + AC line 236 nhưng KHÔNG có trong SM table. Plan §2.5 dòng 190 "extrapolate" thêm transition này — đúng nghiệp vụ nhưng SRS-inconsistent. Phải flag SPEC-CLARIFY.

- **G10. `kenh_tu_van` enum mâu thuẫn được flag ở §7 nhưng KHÔNG có TC verify.** Plan §7 #5 nêu "enum `NHANH/THU_CONG` (line 719) vs `TV_NHANH/TV_THU_CONG` (line 262) mâu thuẫn" — nhưng không có TC `TC-TVN-API-005` test API inbound payload với cả 2 giá trị xem BE accept giá trị nào → reveal bug.

- **G11. Thiếu TC verify `tu_van_nhanh_goc_id` FK + history preservation khi Đẩy Nhóm II.** TC-TVN-006 chỉ verify tạo HOI_DAP `kenh_tiep_nhan=TVN_BRIDGE` + đóng phiên. Không verify: (a) HOI_DAP mới có `tu_van_nhanh_goc_id` trỏ về phiên gốc (FK valid), (b) lịch sử chat bubbles cũ được preserve để cán bộ Nhóm II xem (SRS line 271-272 "giữ toàn bộ lịch sử trao đổi"), (c) badge "Từ Tư vấn nhanh" hiển thị ở Nhóm II inbox (AC line 297).

- **G12. Pagination boundary TC-KHO-020 P2 — sai priority.** BR-DATA-07 (pagination 20/100) là cross-cutting áp dụng MỌI list endpoint. Q&A volume ~10k/năm (SRS line 707) — pagination phải P1 không P2. Lý do P1: nếu pagination FE bug → infinite scroll → DoS browser; nếu BE `max=100` không enforce → đẩy 10k row một request → DoS BE.

## Suggestions

- **S1. Tách `03-TC-cong-khai-search.md` thành Group con với ≥5 TC** — bổ sung Vietnamese diacritics, relevance ranking explicit verify, scope `DA_DUYET` only (không thấy CONG_KHAI riêng — clarify với BA theo §7 #2), boundary tu_khoa = 1 ký tự (ERR-TVN-TK-01) và = 200 ký tự (BR-EC-13).

- **S2. Thêm TC-KHO-PERM-04 / TC-CK-PERM-01 cho công khai cross-don_vi.** Test CB_NV_BN BKH KHÔNG thấy nút `[Công khai]` trên Q&A đơn vị BTC, hoặc click → 403. Đẩy Edge này lên P0 vì là gate ra Internet.

- **S3. Cụ thể hóa TC audit log (TC-KHO-018, TC-CK-005)** — list 6 field bắt buộc: `action_type`, `entity_id`, `entity_type`, `actor_id`, `timestamp`, `payload_diff_jsonb`. Verify INSERT-only bằng cách UPDATE row → expect FK/permission deny.

- **S4. Thêm row trong §7 cho mâu thuẫn `NHAP` enum (G2) + thiếu transition Đẩy Nhóm II trong SM table (G9).** §7 hiện 7 row — thêm 2 row nữa để BA chốt enum chính thức + state diagram cập nhật.

- **S5. Đổi TC-KHO-020 (pagination) từ P2 → P1.** Lý do trong §G12. Bổ sung sub-test: request `?size=101` → BE phải reject hoặc cap 100 (SRS line 546 "20 muc/trang" + BR-DATA-07).

- **S6. Bổ sung 3 TC Edge cho upload file công khai:** TC-CK-EDGE-01 (file 5.1MB jpg → reject), TC-CK-EDGE-02 (file .exe rename .pdf → MIME deep check), TC-CK-EDGE-03 (upload 0-byte file → reject). Gate Critical vì ảnh hưởng public Cổng PLQG.

- **S7. Thêm TC-TVN-API-006 + 007 cho Idempotency edge:** sau 24h cache expire (`Time-Shift` infra hoặc mock), key duplicate trong race condition concurrent 2 request.

- **S8. Bổ sung TC-TVN-007 verify history preservation khi Đẩy Nhóm II** — chat bubbles cũ phải còn ở phiên TV nhanh `HOAN_THANH` + HOI_DAP mới link về phiên gốc (verify qua API `GET /hoi-dap/{id}?include=tu_van_nhanh_goc`).

- **S9. Bổ sung Bảng 1 + Bảng 2 (snapshot TC × status + TC chưa chạy được × cần làm gì) theo rule CLAUDE.md §"Functional/Workflow report — 2 bảng tổng hợp BẮT BUỘC".** Hiện plan có Bảng 4.1 TC list nhưng chưa có cột Status + Note. Khi vào round QA đầu tiên phải có 2 bảng.

- **S10. Đổi cột "TC áp dụng" §2.1 BR table thành 1-to-many ID mapping** — hiện BR-DATA-08 ghi "TC-KHO-007 + TC-TVN-003" nhưng BR-DATA-08 cũng áp FR-X.2-04 (DN search). Phải thêm TC-DN-SEARCH-001. Coverage matrix sẽ rõ hơn khi viết TC detail.

## Verdict

**REVISE** (medium severity — không Critical block nhưng có 12 gap rõ ràng, 6 trong đó là P0/P1 coverage gap ảnh hưởng release readiness).

**Điểm tốt:** Phân tách 2 đơn vị test M13/M14 rõ ràng + flag chặn nhập tay TVN P0 (TC-TVN-NEG-04); Permission matrix §2.3 phân biệt CMS UI vs API inbound đúng; Section 7 SPEC-CLARIFY đã có 7 ambiguity (sót 2 cái G2/G9); BR coverage cross-cutting (BR-AUTH-01/02/03/08, BR-DATA-05/06/07/08, BR-EC-01/13) đầy đủ; cite SRS line cụ thể giúp trace nhanh.

**Justification REVISE:** G3 (file upload công khai) + G4 (permission công khai cross-don_vi) + G5 (FR-X.2-04 search under-spec) là 3 gap P0 ảnh hưởng security/data isolation ra Cổng PLQG public. G2 + G9 là mâu thuẫn SRS chưa flag — risk dev/BA build sai. Cần round V2 trước khi viết TC detail.

---

*Reviewed against SRS v3.5 (input/srs-update-2026-5-5/srs-fr-13-tv-nhanh.md) + v3.0 reference. Plan file 395 dòng — đầy đủ structure nhưng coverage cần đào thêm 6-8 TC.*
