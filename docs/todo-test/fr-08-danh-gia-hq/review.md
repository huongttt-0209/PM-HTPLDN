# Review — FR-08 ĐG HQ test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:42:00

## Gaps

- **`tan_suat` enum contradiction chưa flag** — Plan §2.1 BR-LEGAL-08 + TC-DG (negative tần suất ngoài enum → ERR) khẳng định "KHÔNG cho đột xuất" (`srs-update-2026-5-5/srs-fr-08-danh-gia.md:1235`), nhưng entity field §4.0 line 1006 CHECK IN `('SO_BO_6_THANG','TRON_NAM','DOT_XUAT')` — **enum DB vẫn cho phép `DOT_XUAT`**. Hai vị trí SRS mâu thuẫn nội bộ. Phải thêm SPEC-CLARIFY-FR08-05 (BA chốt DOT_XUAT giữ hay xoá enum) trước khi viết TC negative — nếu không TC-DG (tần suất ngoài enum) có thể PASS với DOT_XUAT input + FAIL false-positive.

- **TC-DG-17 / TC-DG-37 quote sai filter VV** — Plan ghi "Dropdown chỉ hiển thị VV `HOAN_THANH`" và "verify backend reject nếu hack request VV `DANG_XU_LY`". SRS line 858 thực tế: "vụ việc có trạng thái **Hoàn thành hoặc Đã đánh giá**, trong kỳ đợt ĐG". Plan miss state `DA_DANH_GIA` (VV đã được chấm ở KH khác vẫn cho chọn lại) → mâu thuẫn với BR-VI-08-03 ngoại lệ "Nếu VV đã ở KH khác, cảnh báo nhưng vẫn cho phép" plan tự ghi ở TC-DG-18. Phải sửa filter expected = `HOAN_THANH ∪ DA_DANH_GIA`.

- **Data migration KH cũ thiếu `co_quan_duoc_danh_gia_id` chưa có TC** — Delta map §3 Finding 5 + §6 Open issue (`_DELTA-MAP-FR08.md:81`) flag rõ: KH cũ DB `DOT_DANH_GIA` không có cột này → backfill thế nào? Plan chỉ note "Open issues" cuối file nhưng KHÔNG có TC verify migration (vd: KH legacy có `co_quan_duoc_danh_gia_id=NULL` → FR-VI-10 read-only behavior gì? edit form load có default value gì? reject save không cho NULL trên record cũ?). Là `Required=Y` (line 1017) → migration mandatory.

- **`PHAN_CONG_DANH_GIA` entity dùng nhưng KHÔNG verify schema** — §1.2 row 3 ghi entity `PHAN_CONG_DANH_GIA` cho FR-VI-03 nhưng §4 SRS (line 893-1109) **KHÔNG list entity này** — chỉ có 4 owned (`KE_HOACH_DANH_GIA`, `KET_QUA_DANH_GIA`, `BAO_CAO_DANH_GIA`, `TIEU_CHI_DANH_GIA`). Phải xác nhận entity tồn tại trên DB schema hay là sub-table inline trong `KE_HOACH_DANH_GIA` (FK assignees JSON) — TC-DG-09/10/11 thiếu acceptance "DB record nào lưu phân công".

- **Permission matrix §2.3 chưa cover CB NV cấp ngoài cùng cấp với cơ quan ĐG** — `co_quan_duoc_danh_gia_id` FK DON_VI có thể là cấp ĐP (vd STP-AG) trong khi `don_vi_id` là TW. CB NV ĐP của cơ quan được ĐG (vd `cb_nv_dp_01` AG) có quyền R-only theo FR-VI-10. Matrix line 151 chỉ ghi "CB NV (`co_quan_duoc_danh_gia_id`)" mà KHÔNG break theo cấp. TC-DG-29 chỉ test 1 pair (BTP-TW × STP-AG) — thiếu test BN×BN (vd BKH × BTC), BN×ĐP, ĐP×ĐP, vô hiệu cấp (vd KH `don_vi_id`=BKH muốn ĐG STP-AG — cross-tier BN→ĐP có hợp lệ không?).

- **Edge BR-EC-VI-08-05 viết sai constraint** — Line 102 BR ghi "UNIQUE(`ke_hoach_id`, `vu_viec_id`)" rồi TC-DG-39 ghi "Trùng VV trong 2 KH cùng kỳ (UNIQUE per KH, KHÔNG UNIQUE cross-KH) → cảnh báo nhưng cho phép". Nhưng `srs-update-2026-5-5/srs-fr-08-danh-gia.md:1029-1043` (KET_QUA_DANH_GIA entity, plan không cite line cụ thể) cần grep lại `UNIQUE` constraint — plan "inferred từ ERD" (line 102) chưa quote constraint thật. Nếu constraint chỉ là FK không UNIQUE thì TC-DG-39 dư thừa; nếu UNIQUE cross-KH thì BR-VI-08-03 ngoại lệ (line 100) tự mâu thuẫn.

- **BR-VI-08-06 hard-delete claim chưa khớp SRS line được cite** — Plan §2.1 line 103 ghi cite `system-overview:845 (C1)` nhưng entity field line 1015 vẫn có `is_deleted boolean DEFAULT 0` (soft-delete flag). SRS line 1167 SM table ghi action HUY = "Audit, **soft-delete**". 2 nguồn mâu thuẫn: claim hard-delete vs schema/SM soft-delete. Phải verify lại C1 cross-cutting có override field-level không, hoặc đổi label thành soft-delete.

- **Notification BR-NOTIF-01 thiếu TC verify channel + payload** — Plan ghi "TC verify gửi TB đúng 4 thời điểm" nhưng không có TC-DG dedicated cho FR-VI-03/04/08 (chỉ TC-DG-09/12/22 piggyback). Missing: ai nhận TB (CB NV creator? CB PD reviewer? cả 2?), channel (in-app / email / SMS), retry logic, TB content fields. Delta map Finding 6 đánh dấu "ưu tiên test" — coverage hiện tại quá nông.

- **FR-VI-10 chưa test mutation attempt** — TC-DG-26/27/28/29 đều test READ. Thiếu test "CB NV của `co_quan_duoc_danh_gia_id` cố PUT/PATCH/DELETE qua API direct" → expected 403. Memory `qa_htpldn_qtht_permission_bypass` cảnh báo BE có thể bypass khi role không trong matrix nhưng có permission Read. **Critical: read-only must mean read-only at API layer, không chỉ UI hide button.**

- **Edge file_dinh_kem chưa test multi-file + count limit** — TC-DG-40 chỉ test 1 file >20MB / sai định dạng. Field `file[]` (line 1016) array — thiếu edge: upload 50 file cùng lúc, tổng dung lượng aggregate, drag-drop reorder, replace file, server timeout khi upload concurrent. PDF/DOC/DOCX/XLS/XLSX 5 format — chỉ test 1 sai format không đủ matrix.

- **HUY transition thiếu test guard "lý do"** — SRS line 1167 SM table ghi `Guard: Có lý do, chưa HOAN_THANH`. Plan TC-DG-30/31 không có TC negative HUY thiếu lý do hoặc HUY từ `HOAN_THANH`/`HUY` (terminal state, không allow). Thiếu negative path.

- **TC-DG-35 cross-unit CB_NV_TW chưa rõ scope** — Note "CB NV cross-unit (TW xem KH của BN khác) → empty / 403 theo BR-AUTH-08". Nhưng v3.5 ghi "2-tier TW/BN, BN không có ĐP trực thuộc" (line 86). CB_NV_TW theo BR-AUTH-08 có quyền xem **all** (delta map cũ?) hay **chỉ scope TW**? Expected của TC ambiguous ("empty / 403") — phải chốt 1 cái trước khi run.

## Suggestions

- **Tách TC-DG-21 thành 2 TC riêng** — TC-DG-21 hiện combine 2 dimension (auto-calc formula + xếp loại boundary 89.9/90/70/50/49.9). Nên split: TC-DG-21a calc formula (verify `Σ điểm × trọng số / 100`), TC-DG-21b xếp loại boundary 5 case (≥90 / ≥70 / ≥50 / <50). Mix 2 acceptance trong 1 TC làm khó pinpoint khi fail.

- **Thêm TC permission cho FR-VI-10 với QTHT** — Matrix line 151 ghi QTHT có ✅ R-only. Cần TC verify QTHT đọc được KH `HOAN_THANH` của bất kỳ `co_quan_duoc_danh_gia_id` nào (BR-AUTH-03 ngoại lệ). Hiện 0 TC test QTHT × FR-VI-10.

- **TC-DG-08 tolerance ±0.01% scenarios thiếu boundary âm** — Plan test 99% / 100.01% nhưng thiếu 99.99% (just within tolerance) và 100.02% (just outside upper tolerance). Số boundary chuẩn = 4 (lower-1ε, lower, upper, upper+1ε).

- **Bổ sung TC export TT17 verify nội dung file** — TC-DG-24 happy path chỉ ghi "xuất XLSX/DOCX". Mẫu 21a/21b TT17/2025 có template cố định — cần verify cell A1/B2/heading có đúng mẫu (`mau_bao_cao` enum `MAU_21A`/`MAU_21B` line 1058 chọn template nào).

- **Sửa cite SRS line consistent prefix `srs-update-2026-5-5/`** — BR-AUTH-03 / BR-AUTH-08 / BR-DATA-06 / BR-DATA-07 / BR-EC-01 / BR-EC-13 hiện cite `srs-v3/srs-v3.md:XXXX` mà rule project (memory `feedback_bug_srs_ref_path`) require prefix `srs-update-2026-5-5/` cho v3.5 update — verify BR cross-cutting có còn tồn tại trong v3.5 master không. Nếu có nguyên văn, switch prefix; nếu không, đánh dấu inherited from v3 baseline.

- **Mỗi TC-DG nên có Precondition state machine cụ thể** — Hiện bảng 40 TC chỉ ghi tên TC + FR/BR + Loại + Priority. Khi viết detail TC (01..12 file riêng), template phải có dòng "Precondition: KH ID=X, trang_thai=`PHAN_CONG`, đã có ≥1 tiêu chí 100%, ≥2 người ĐG". Hiện không có column.

- **Thêm SPEC-CLARIFY-FR08-06: SM HUY có cho phép từ `CHO_DUYET_PC` / `CHO_PHE_DUYET`?** — SRS line 1167 list HUY chỉ từ `LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO` — không có `CHO_DUYET_PC` và `CHO_PHE_DUYET`. Plan §2.5 diagram line 209 ghi "[*bất kỳ*] → HUY" — mâu thuẫn. Phải confirm: 2 state chờ duyệt CB PD có cancel-able không?

- **Performance test scope thiếu** — Plan không có TC pagination 10k record (BR-DATA-06 export limit) / search response time / Tab 3 chấm điểm 100 VV inline calc. Module có Tier 4 entity + Mermaid radar/bar chart — perf risk cao. Đề xuất 2-3 P1 perf TC.

- **TC-DG-09 acceptance "save + trình duyệt" gộp 2 action** — Nên split happy path tạo phân công (TC-DG-09a) và submit duyệt PC (TC-DG-09b) — vì transition `PHAN_CONG → CHO_DUYET_PC` (FR-VI-03 trình) có guard riêng (BR-AUTH-05 send TB CB PD). Mix sẽ làm khó test reject path TC-DG-13.

- **File structure §3 nên thêm `13-TC-data-migration.md`** — Để cover gap 3 (KH legacy thiếu `co_quan_duoc_danh_gia_id`) + gap rename `DOT_DANH_GIA` → `KE_HOACH_DANH_GIA` reference cũ trong code/API path/i18n string.

## Verdict

**REVISE** — Plan có cấu trúc tốt (40 TC × 3 loại × 12 file, SM 8 state đúng v3.5, FR-VI-10 cross-unit cover 4 TC, file_dinh_kem edge cover) nhưng còn **12 gap critical/important** trước khi viết TC detail. Phải xử lý 4 blocker:

1. **`tan_suat` DOT_XUAT enum vs BR-LEGAL-08 contradiction** — log SPEC-CLARIFY-FR08-05 BA chốt trước, nếu không TC-DG negative tần suất ngoài enum sai expected.
2. **Filter VV `HOAN_THANH ∪ DA_DANH_GIA`** — sửa TC-DG-17/37 expected, đồng bộ với BR-VI-08-03 ngoại lệ.
3. **Data migration gap** — thêm file `13-TC-data-migration.md` cover KH legacy.
4. **FR-VI-10 mutation attempt** — thêm TC API-level verify PUT/PATCH/DELETE 403 (không chỉ UI hide).

Sau khi fix 4 blocker + 8 important gap còn lại → APPROVE để viết file 01..13 detail TC.
