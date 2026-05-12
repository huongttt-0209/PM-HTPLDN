# Review — FR-12 TVCS test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 14:43:59

## Gaps

- **§2.5 SM transition table mâu thuẫn SRS — bỏ row `TIEP_NHAN → HUY`.** Test plan liệt kê 11 transition (line 213, 230) nhưng SRS bảng `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1481-1492` chỉ có **10 transition** — KHÔNG có row `TIEP_NHAN → HUY`. Plan tự thêm row này, vi phạm rule "KHÔNG suy luận từ SRS". Phải xóa hoặc cite SRS line cho phép.
- **DANG_TU_VAN → HOAN_THANH guard sai.** Plan ghi guard = "`ket_qua` khác rỗng" (line 226). SRS `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1487` ghi guard = "Có VB TVPL" (văn bản tư vấn pháp lý đính kèm). Test case TVCS-002 happy-path đi qua transition này sẽ verify sai field.
- **TVCS-001 cite SRS line 105-119 không đúng phạm vi.** §2 test plan + SRS line 105-119 thực chất là phần Inputs FR-X.1-01 (Ngày tư vấn, Mã CG, etc.) — không bao gồm SCR-X1-01 toolbar [+ Thêm yêu cầu]. Cite mơ hồ.
- **Inbound API coverage thiếu happy `linh_vuc_id null` + `tai_lieu_dinh_kem` multi-file.** §4 TVCS-API-001..006 có 6 TC nhưng KHÔNG có TC cover field 4 (`linh_vuc_id` optional `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:433`) và TC cover ràng buộc "Max 10 files, tổng max 100MB" (`:435`). Chỉ có TC file >20MB (ERR-FILE-SIZE-01 cấp file). Miss boundary tổng 100MB.
- **CROSS-001 outbound metadata-only — assertion mơ hồ.** Plan ghi "KHÔNG có `ket_qua`/`noi_dung` chi tiết" (line 333) nhưng cite `02-thu-tu-module.md:935` — KHÔNG cite SRS line trong `srs-fr-12-tv-chuyen-sau.md`. Phải define explicit field list được expose (mã / DN / Lĩnh vực / Tóm tắt / Ngày hoàn thành) vs field bị che (`noi_dung_tu_van`, `ket_qua`, `tai_lieu_dinh_kem`). Hiện assertion negative-only.
- **BR-AUTH-10 NHT lọc kép thiếu boundary case.** HSPL-002/003 cover "in scope vs out scope" (line 317-318) nhưng miss case: VV chuyển CG khác (NHT cũ mất quyền), VV `trang_thai=HOAN_THANH` rồi đóng (NHT còn quyền R hay không?). SRS line 669-671 không nêu rõ — phải add TC hoặc move xuống §7 ambiguity.
- **BR-FLOW-07 chỉ có 1 TC happy (TLPL-002) — thiếu negative permission.** Plan cite TLPL-002 = "CB NV bấm Công khai" nhưng KHÔNG có TC: (a) CG / NHT / DN bấm publish TLPL → 403, (b) `mo_ta_cong_khai` empty khi switch CONG_KHAI → reject? Đã liệt kê §7 ambiguity #5 nhưng vẫn cần TC negative phân quyền (không phải defer).
- **TVCS-002 transition full SM gộp 6 step vào 1 TC = anti-pattern.** Theo `feedback_seed_acceptance_strict_split` + lesson 2026-04-29 A5 (split combinatorial), TC happy 6-step nên split thành 6 sub-step verify per-transition (state DB + notification + audit row). Gộp 1 TC khó debug fail point.
- **CG enum rename `HOAT_DONG` cite ngắt mạch.** §0 Δ #8 cite "Δ v3.5 system-overview.md:817" nhưng cross-module test CROSS-004 cite "Δ v3.5 §8" (line 336) — 2 cite cùng nguồn khác format. Tester sẽ confuse. Cần cite uniform: `srs-update-2026-5-5/srs-fr-04-...md:<line>` nếu rename ở SRS FR-04, không phải system-overview snapshot.
- **§7 Open issues — 6 ambiguity thiếu cột "Owner" + "Deadline".** Plan ghi "Đề xuất hỏi BA" (line 384) nhưng KHÔNG đánh owner cụ thể (BA tên gì? Dev BE nào?) và KHÔNG deadline. Theo §"TC chưa chạy được" CLAUDE.md project, cột "Ai làm" phải role cụ thể (`BA` / `Dev BE`). Nếu defer >2 round, phải escalate.
- **Auto-save TRAO_DOI_NHAP 30s (TVCS-010) — endpoint chưa SRS spec rõ (§7 #6 đã defer) nhưng TC vẫn list P1.** Nếu endpoint chưa exist (defer), TC này BẮT BUỘC mark `🚫 chờ dev BE expose endpoint` ngay từ đầu, không phải treat happy. Hiện plan để P1 không note dep blocking.
- **Permission matrix §2.3 row "Phân công CG (modal SCR-II-03)"** ghi "TW: all units; BN/DP: own unit" (line 154) nhưng SRS không nêu rõ TW phân công CG cross-unit. Cite missing — cần SRS line hoặc quote permission-matrix.md row.

## Suggestions

- **Thêm TC TLPL-006 (negative permission BR-FLOW-07):** CG / NHT bấm [Công khai lên Cổng] → 403. Bổ sung cột FR/BR + cite SRS line 1583.
- **Split TVCS-002 transition full thành TVCS-002a..f** (mỗi transition 1 TC), mỗi TC verify: (1) DB state, (2) notification gửi đúng role, (3) AUDIT_LOG insert. Dễ debug khi fail giữa chain.
- **Thêm TC inbound API tổng dung lượng 101MB (10 file × 10MB + 1 file thừa):** verify ERR cấp tổng (không phải cấp file). Cite SRS line 435 ràng buộc.
- **Thêm bảng "Tóm tắt mapping FR ↔ TC ↔ BR" sau §4** để dễ trace coverage. Hiện chỉ có cite scattered, khó audit "BR-PUBLIC-03 có TC chưa".
- **CROSS-001 assertion phải liệt kê tường minh field expose vs hide** (vd: bảng 2 cột "Expose" / "Hide" + cite ERD `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1182-1210` ERD TVCS attributes).
- **§2.6 upstream dep thêm verify command** (`curl -s 'http://.../api/v1/tu-van-viens?trang_thai=HOAT_DONG' | jq '.total'`) để tester biết cách verify state-snapshot trước khi chạy GĐ 3 functional. Theo state-marker workflow CLAUDE.md.
- **§7 thêm cột "Owner" + "Deadline" + "Nhóm A-F":** map vào 6 nhóm A-F per CLAUDE.md `output/template/tc-block-classification-template.md`. VD #4 `hop_dong_tv_id` FR-14 = nhóm E (dependency upstream).
- **Tách BR-PUBLIC-01 (TVCS) vs BR-PUBLIC-01 (TLPL exception):** §2.1 line 110 gộp 2 case 1 row — confusing. Tách 2 row: `BR-PUBLIC-01-TVCS` (DA_DUYET required) vs `BR-PUBLIC-01-TLPL` (bất kỳ, theo BR-FLOW-07).
- **Add edge TC TVCS-011 (race auto BR-FLOW-01):** CG tích Hoàn thành đúng lúc CB NV bấm Hủy DANG_TU_VAN → SM conflict (auto HOAN_THANH→CHO_PHE_DUYET vs DANG_TU_VAN→HUY). Optimistic lock + state machine guard verify.
- **Note rõ TLPL state machine (NHAP / CONG_KHAI)** trong §2.5 — hiện plan reference "2 state" (line 236) nhưng không có diagram + bảng transition như SM-TVCS. Tester sẽ phải đoán transition guard.

## Verdict

**REVISE** — cần fix 3 critical:

1. SM transition table sai (thừa row `TIEP_NHAN → HUY` + guard `HOAN_THANH` sai field) — block test execution vì sẽ verify sai SRS line 1481-1492.
2. CROSS-001 outbound metadata assertion negative-only — thiếu explicit field-list expose/hide.
3. TLPL BR-FLOW-07 chỉ có TC happy, thiếu negative permission + missing TLPL SM diagram §2.5.

5 Suggestion priority HIGH (split TVCS-002, tách BR-PUBLIC-01 2 row, thêm TC inbound 100MB boundary, thêm cột Owner §7, thêm verify command upstream) nên áp dụng trước GĐ 3 functional.

Sau khi fix 3 critical + 5 suggestion HIGH → APPROVE. Coverage tổng 43 TC × 7 FR là reasonable (~6 TC/FR), BR-ROUTE-TVCS-01 đã có 3 case (TVCS-API-001/002/003) tốt, permission matrix §2.3 cover 7 role × 5 entity action — kỹ.
