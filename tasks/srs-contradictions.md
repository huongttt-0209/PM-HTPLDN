# SRS Contradictions Tracker

> **Mục đích:** Theo dõi mọi mâu thuẫn / ambiguity / spec drift trong SRS v3.5 (và v3 legacy) cần BA chốt. Tránh defer BA mà không có evidence + tránh quên BA decision sau khi confirm.
>
> **Workflow:** Phát hiện contradiction → add entry vào đây → escalate BA → BA confirm → update CHANGELOG + close entry.
>
> **Khi nào add entry:** Đã làm 2-source verify (SRS local grep + NotebookLM HTPLDN query) + đã cross-check FR khác → vẫn có ≥2 spec line conflict.

---

## Cách dùng

1. **Trước log bug:** Search file này → nếu module bug đang touch đã có entry contradict đang Open → KHÔNG log bug như spec normal, ghi note "depends on BA decision SRS-C-NNN".
2. **Khi phát hiện mâu thuẫn mới:** Đọc qua hết entry hiện có để không log trùng → add entry mới với ID tăng dần.
3. **Khi BA confirm:** Update entry status Open → Resolved + decision date + decision summary. Update CHANGELOG-v3-to-v3.5.md (hoặc tạo CHANGELOG-fix-NNN.md) + update tất cả bug/test reference theo decision mới.

---

## Format entry

```markdown
## SRS-C-NNN — {Module/Topic} — {Status}

**Phát hiện:** YYYY-MM-DD HH:MM:SS — R{N}
**Trạng thái:** Open / BA-pending / Resolved
**Tester:** {tên}

### Mâu thuẫn
- Source 1: `{file path}:{line}` — quote nguyên văn
- Source 2: `{file path}:{line}` — quote nguyên văn
- NotebookLM HTPLDN cùng câu hỏi: {match Source 1 / Source 2 / khác / im lặng}

### Impact
- Bug/TC ảnh hưởng: BUG-X-001, TC-Y-002
- Round bị block: R{N}
- Severity: P0/P1/P2

### Câu hỏi BA
{Câu hỏi 1-2 dòng, cụ thể, choose-between-A-and-B format}

### Phương án đề xuất
- (a) Theo Source 1 — pros / cons
- (b) Theo Source 2 — pros / cons
- **Khuyến nghị:** (a) hoặc (b) — vì {lý do}

### BA decision  ← fill khi resolved
- Date: YYYY-MM-DD HH:MM:SS
- Decision: {tóm tắt 1-2 câu}
- CHANGELOG updated: ✓ (link)
- Bug/TC affected updated: ✓ (list link)
```

---

## Entries

### SRS-C-001 — FR-05 vs FR-10 — LOAI_HINH_HT vs LOAI_HINH_HO_TRO — Open

**Phát hiện:** 2026-05-13 12:30:00 — R20
**Trạng thái:** Open (BA-pending)
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1: `input/srs-update-2026-5-5/srs-fr-05-vu-viec.md:176` — quote:
  > "loai_hinh_ht_id | identifier | Y | FK → DANH_MUC (loai='LOAI_HINH_HT'): Tư vấn / Đại diện / Hỗ trợ khác"
- Source 2: `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:234` — quote:
  > "loai_danh_muc | text | Y (system) | = 'LOAI_HINH_HO_TRO' | LOAI_HINH_HO_TRO | system"
- NotebookLM HTPLDN query 2026-05-13 17:40:00 (conv `6b311936-4b86-4a63-8fc6`): **CONFIRM contradiction**. Quote: "Tài liệu SRS v3.5 đang ghi nhận cả hai giá trị LOAI_HINH_HT và LOAI_HINH_HO_TRO ở 2 phân hệ khác nhau". NotebookLM khuyến nghị `LOAI_HINH_HO_TRO` (FR-VIII-02 Quản trị danh mục là source-of-truth). Match Source 2.

#### Impact
- Bug ảnh hưởng: BUG-E2E-S4-011 (Major) — dropdown rỗng UC52 DN gửi yêu cầu HTPL
- TC ảnh hưởng: E2E-S4 toàn bộ flow DN gửi yêu cầu → CB tiếp nhận → phân công TVV
- Round bị block: R20 reverify (2026-05-12 → 13)
- Severity: P1 (block UC52 end-to-end)

#### Câu hỏi BA
Enum key danh mục cho "Loại hình hỗ trợ pháp lý" đúng là `LOAI_HINH_HT` (theo FR-05) hay `LOAI_HINH_HO_TRO` (theo FR-10)? FE đang follow FR-05 → BE seed theo FR-10 → query trả `data:[]`.

#### Phương án đề xuất
- (a) Align về `LOAI_HINH_HT` — FR-05 (Vụ việc) là module sử dụng trực tiếp. Pros: FE đang dùng. Cons: phải đổi BE seed + đổi FR-10 spec.
- (b) Align về `LOAI_HINH_HO_TRO` — FR-10 (QTHT) là source-of-truth danh mục. Pros: BE đã seed sẵn 6 items. Cons: phải đổi FE + đổi FR-05 spec.
- **Khuyến nghị:** (b) vì FR-10 QTHT là source-of-truth danh mục dùng chung cho mọi module. Module Vụ việc (FR-05) phải align theo QTHT, không ngược lại. Cost: chỉ đổi 1 chỗ FE + 1 dòng spec FR-05.

#### BA decision  ← chưa có
- Date: TBD
- Decision: TBD
- CHANGELOG updated: ❌
- Bug/TC affected updated: ❌

---

### SRS-C-003 — FR-03 Đào tạo — SM-KHOAHOC số state (9 vs 11) — Resolved

**Phát hiện:** 2026-05-16 16:00:00 — round audit input/data
**Trạng thái:** Resolved 2026-05-16 17:30:00 (NotebookLM HTPLDN confirm)
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1 (DELTA-MAP): `input/srs-update-2026-5-5/_DELTA-MAP-FR03.md:21` — nêu SM-KHOAHOC tăng 9 → **11 state** (thêm `TU_CHOI` + `TU_CHOI_KQ`)
- Source 2 (SRS final): `input/srs-update-2026-5-5/srs-fr-03-dao-tao.md:35` — *"SM-KHOAHOC (giữ 9 trạng thái v3)"*; `:43` *"Khóa học giữ nguyên SM-KHOAHOC v3 9 trạng thái... quyết định BA OUT Thay đổi 3 lượt 2026-05-06"*; `:1863` confirm 9 state
- NotebookLM HTPLDN query 2026-05-16 17:25:00 (conv `6b311936-4b86-4a63-8fc6`): **CONFIRM 9 state**. Quote master `srs-v3.5.md` §C.2: *"11 trạng thái → 9 trạng thái... Bỏ trạng thái tách riêng TU_CHOI... Khóa học khi bị từ chối → quay về DU_THAO (gộp); kết quả khóa khi bị từ chối → quay về DA_KET_THUC (gộp)"*. Audit info lưu tại 3 trường `ly_do_tu_choi`/`nguoi_tu_choi`/`thoi_gian_tu_choi` trong entity KHOA_HOC (master :1934-1936).

#### Impact (resolved scope)
- Artifact đã đồng bộ: `input/data/state-machines-v3.5.md:209-225` (đã update 9 state với SRS line cite trong session audit 2026-05-16) + `input/quy-trinh-nghiep-vu/flow-module.md:273-282` (đã update SM-KHOAHOC 11→9 + DANG_HOAT_DONG→HOAT_DONG rename)
- TC ảnh hưởng: FR-03 đào tạo workflow test plan + Round 7 task R7.3
- Severity: P0 (đã unblock state-machines.md + flow-module.md refresh)

#### Kết luận (canonical sau verify NotebookLM)
- **9 state CHUẨN** (giữ v3): `DU_THAO → CHO_DUYET → DA_DUYET → DA_CONG_KHAI → DANG_DIEN_RA → DA_KET_THUC → CHO_DUYET_KQ → HOAN_THANH → DA_HUY`
- **DELTA-MAP 11-state đã DEPRECATED** — TU_CHOI + TU_CHOI_KQ KHÔNG tách riêng (BA OUT Thay đổi 3 cổng duyệt 2026-05-06 + giữ Q1/CR-1 chốt 2026-05-08).
- **Xử lý từ chối:** `CHO_DUYET → DU_THAO` (gộp) + `CHO_DUYET_KQ → DA_KET_THUC` (gộp). Phân biệt "chưa từng trình" vs "đã bị từ chối" qua field `ly_do_tu_choi` (NULL = chưa trình; có giá trị = đã bị từ chối).
- **Đảo OUT phần Processing (CR-2 chốt 2026-05-08):** transition `CHO_DUYET → DA_DUYET` cho Khóa học được mô tả qua Processing block trong FR-III-01 (KHÔNG tạo FR-III-21 riêng như Thay đổi 3 đề xuất ban đầu).

#### BA decision
- Date: 2026-05-06 (BA OUT Thay đổi 3 cổng duyệt 2b) + 2026-05-08 (Q1/CR-1 confirm)
- Decision: Giữ SM-KHOAHOC v3 9 trạng thái; không tách TU_CHOI/TU_CHOI_KQ. Processing phê duyệt gộp vào FR-III-01 (CR-2).
- CHANGELOG updated: ✓ (`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` Chặng 3.3 + master `srs-v3.5.md` §C.2 update 2026-05-09)
- Bug/TC affected updated: ✓ (state-machines-v3.5.md + flow-module.md đã refresh trong audit session 2026-05-16)

---

### SRS-C-004 — FR-05 vs FR-08 — BR-CALC-04 ID conflict — Resolved (test artifact stale)

**Phát hiện:** 2026-05-16 16:00:00 — round audit output/funtion
**Trạng thái:** Resolved 2026-05-16 17:35:00 (NotebookLM confirm — SRS v3.5 đã fix; test artifact 7.8-danh-gia.md có stale conflict note cần update)
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1 (FR-05 Vụ việc — old v3): `BR-CALC-04` = "Ưu tiên phân công NĐ55 Đ.4" (auto-calc điểm ưu tiên DN)
- Source 2 (FR-08 Đánh giá): `BR-CALC-04` = "Tổng trọng số tiêu chí đánh giá = 100%"
- Source 3 (FR-10 Quản trị): `BR-CALC-04` alias cite FR-08 (cùng ngữ cảnh trọng số)
- **Ghi chú:** mô tả ban đầu "tỷ lệ chi 30/50/70%" trong tracker là phán đoán sai — đó là `BR-CALC-01` (NĐ18/2026), không phải BR-CALC-04. Nghiệp vụ FR-05 thực sự là "Ưu tiên phân công NĐ55".

#### NotebookLM query 2026-05-16 17:30:00 (conv `6b311936-4b86-4a63-8fc6`)
- **CONFIRM**: ID collision đã được fix ở SRS v3.5 trong "Chặng 3.3 cross-file fix" ngày 2026-05-06. Đổi mã ở `srs-fr-05` → **`BR-CALC-07`**. Giữ nguyên `BR-CALC-04` ở `srs-fr-08`/`srs-fr-10` (ngữ cảnh "Tổng trọng số = 100%").
- 19 vị trí refs trong `srs-fr-05-vu-viec.md` đã rename → BR-CALC-07 (Lịch sử thay đổi changelog + Inputs/Processing/Errors/Cross-ref/Bảng tổng quan BR §6 + tiêu đề BR-CALC-07).
- Master `srs-v3.5.md` Phụ lục B.4 line 4838 đã thêm BR-CALC-07 (cite NĐ55 Đ.4) + ghi chú lịch sử rename.
- Local verify: grep `BR-CALC-04` trong `srs-fr-05-vu-viec.md` = 0 ref body (chỉ còn ở header line 19 ghi rename history). Grep `BR-CALC-07` = 20 ref. → Khớp NotebookLM.
- Naming convention SRS v3.5: prefix theo loại rule (BR-CALC/BR-AUTH/BR-DATA/BR-FLOW/BR-SLA/BR-LEGAL/...), KHÔNG theo module — nên phương án (a) `BR-EVAL-CALC-04` / (b) `BR-COST-CALC-04` ban đầu đề xuất là SAI convention. SRS v3.5 dùng cách rename số tăng dần (BR-CALC-04 → BR-CALC-07).

#### Impact (resolved scope)
- SRS v3.5 đã fix → KHÔNG còn ID collision trong SRS hiện hành.
- **Stale test artifact:** `output/funtion/7.8-danh-gia.md:21` còn ghi *"BR-CALC-04 ID conflict (2026-05-06 detected): File 7.8 dùng BR-CALC-04 = 'Tổng trọng số 100%'. File 7.5 (FR-05 v3.5) dùng BR-CALC-04 = 'Ưu tiên phân công NĐ55'..."* → SAI vì FR-05 đã rename → BR-CALC-07. **Cần update note hoặc xóa** (FR-08 vẫn dùng BR-CALC-04 hợp lệ).
- TC ảnh hưởng: không (TC FR-08 vẫn dùng BR-CALC-04 đúng nghiệp vụ; TC FR-05 phải dùng BR-CALC-07).

#### BA decision
- Date: 2026-05-06 (Chặng 3.3 cross-file fix — SRS Agent apply)
- Decision: Giữ BR-CALC-04 ở FR-08 + FR-10 (Tổng trọng số tiêu chí = 100%). Rename FR-05 → BR-CALC-07 (Ưu tiên phân công NĐ55 Đ.4).
- CHANGELOG updated: ✓ (`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` Chặng 3.3 — Issue A. + master `srs-v3.5.md` B.4 line 4838 thêm BR-CALC-07 + ghi chú lịch sử)
- Bug/TC affected updated: ⏳ Cần update note stale ở `output/funtion/7.8-danh-gia.md:21` (action audit-followup)

---

### SRS-C-005 — FR-05 — actor scope TVV/CG (mở rộng 5 entity) — Open

**Phát hiện:** 2026-05-16 (audit Permission Matrix sync round)
**Trạng thái:** Open (BA-pending) — enriched 2026-05-16 17:40:00 với NotebookLM evidence + scope mở rộng
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1 (Master Permission Matrix): `input/srs-update-2026-5-5/srs-v3.5.md:1289-1291` — `PHAN_CONG_VU_VIEC | ... | TVV=— | CG=—` + `LICH_SU_VU_VIEC | ... | TVV=— | CG=—`
- Source 1 mở rộng (cùng matrix Section 3.4.2): `VU_VIEC | TVV=— | CG=—` + `HO_SO_VU_VIEC | TVV=— | CG=—` + `KET_QUA_VU_VIEC | TVV=— | CG=—`
- Source 2 (FR-05 narrative + BA decision Round 7): `srs-fr-05-vu-viec.md:21` *"Round 7 BA decision: FR-V.I-10... actor chính thức là người được phân công xử lý vụ việc (`PHAN_CONG_VU_VIEC.nguoi_xu_ly_id`), bao gồm **NHT/TVV/CG cá nhân** hoặc TVV do tổ chức tư vấn cử."* + `:792` + `:1883`
- Source 3 (Master footnote ‖): `srs-v3.5.md:1322` — *"NHT/TVV/CG có quyền `RU* (own)` chỉ trên bản ghi mà chính họ là một phía của liên kết"* → footnote ĐÃ cấp quyền own scope, NHƯNG cell trong bảng vẫn ghi `—`.
- Source 4 (BR-AUTH-10): master Phụ lục B.1 — *"Lọc kép cho NHT/TVV/CG (NĐ77/2008): Lớp 2 — NHT/TVV chỉ thấy vụ việc HTPL được phân công (VU_VIEC.nguoi_ho_tro_id / .tu_van_vien_id = current user); CG chỉ thấy yêu cầu TV chuyên sâu được phân công"* → BR-AUTH-10 quy định TVV/CG PHẢI có quyền đọc dữ liệu vụ việc/phân công.

Nếu TVV/CG = — (no permission) trên 5 entity vụ việc, BR-AUTH-10 + footnote ‖ + BA decision Round 7 đều KHÔNG thực thi được. Hệ thống RBAC sẽ trả 403 khi TVV/CG cá nhân login chuyên trang xem VV của mình hoặc thực hiện FR-V.I-10/15/16.

#### NotebookLM query 2026-05-16 17:35:00 (conv `6b311936-4b86-4a63-8fc6`)
- **CONFIRM**: Đây là **lỗi omission/bug** trong quá trình tổng hợp master matrix, KHÔNG phải cố ý.
- Nguyên nhân: v3 cũ chỉ có NHT là actor xử lý vụ việc → matrix gốc chỉ cấp quyền cột NHT. Khi BA Round 7 mở rộng actor → NHT/TVV/CG cá nhân, narrative SRS được update nhưng các cột TVV/CG trong matrix BỊ QUÊN không update.
- Khuyến nghị NotebookLM sửa master matrix `srs-v3.5.md` Section 3.4.2 (line 1289-1291 + các dòng VU_VIEC/HO_SO_VU_VIEC/KET_QUA_VU_VIEC):
  - `VU_VIEC`: TVV/CG đổi `—` → **`RU* (own)`**
  - `HO_SO_VU_VIEC`: TVV/CG đổi `—` → **`CRU* (own)`** (upload tài liệu đính kèm)
  - `KET_QUA_VU_VIEC`: TVV/CG đổi `—` → **`CRU* (own)`** (FR-V.I-15)
  - `PHAN_CONG_VU_VIEC ‖`: TVV/CG đổi `—` → **`R* (own)`** hoặc **`RU* (own)`** (FR-V.I-10 chấp nhận/từ chối)
  - `LICH_SU_VU_VIEC ‖`: TVV/CG đổi `—` → **`R* (own)`** (audit own actions)

#### Impact (mở rộng scope)
- Artifact ảnh hưởng:
  - `output/permission-matrix-by-fr.md` lines 122-124 (PCVV/DGVV/LSVV) — cần update TVV/CG khi BA confirm
  - `output/permission-matrix-by-fr.md` các dòng VU_VIEC/HO_SO_VU_VIEC/KET_QUA_VU_VIEC — cần update TVV/CG cùng đợt
  - `output/permission-matrix-by-role.md` 22 row FR-V.I-09 + FR-V.I-17 (đã update theo matrix literal trong audit 2026-05-16) — cần re-update khi BA confirm
  - `output/permission-matrix.md` master role-by-entity — cần update tương tự
- TC ảnh hưởng: FR-V.I-09/10/15/16/17 toàn bộ negative test "TVV/CG access vụ việc của mình → 200 hay 403?"
- Severity: P0 (block test design + FE/BE implement RBAC cho chuyên trang TVV/CG)

#### Câu hỏi BA
TVV/CG cá nhân được phân công có quyền `RU*(own)` trên VU_VIEC + `CRU*(own)` trên HO_SO_VU_VIEC/KET_QUA_VU_VIEC + `R*/RU*(own)` trên PHAN_CONG_VU_VIEC + `R*(own)` trên LICH_SU_VU_VIEC không? Hay actor FR-V.I-10 thực ra chỉ là NHT + TVV-via-TC TV (matrix-friendly)?

Cụ thể câu hỏi cần BA chốt 1 trong 2 hướng:
- **Hướng A — Master matrix sai, sửa matrix:** Cập nhật 5 dòng matrix Section 3.4.2 theo NotebookLM khuyến nghị + giữ narrative + BR-AUTH-10 + footnote ‖ nguyên trạng.
- **Hướng B — Narrative sai, sửa narrative:** Bỏ TVV/CG khỏi danh sách actor FR-V.I-10 ở line 21 + 792 + 1883 + bỏ footnote ‖ phần "NHT/TVV/CG có RU*(own)" + bỏ BR-AUTH-10 phần "TVV chỉ thấy VV được phân công".

#### Phương án đề xuất
- (a) **Hướng A — sửa matrix**: 4 nguồn (narrative line 21/792/1883 + footnote ‖ line 1322 + BR-AUTH-10) đều khẳng định TVV/CG là actor có quyền own scope. Chỉ matrix bị miss. Sửa matrix là minimal-impact + đúng nghiệp vụ. **Khuyến nghị**.
- (b) Hướng B — sửa narrative: cost cao (sửa 4 nơi) + trái BA decision Round 7 + trái BR-AUTH-10 + trái NĐ77/2008 (TVV là tác nhân hợp pháp xử lý VV).

#### BA decision  ← fill khi resolved
- Date: TBD
- Decision: TBD
- CHANGELOG updated: ❌
- Bug/TC affected updated: ❌

---

### SRS-C-002 — FR-08 Đánh giá — DA_DANH_GIA state v3 vs v3.5 — Resolved

**Phát hiện:** 2026-05-13 11:30:00 — R20 deep-verify
**Trạng thái:** Resolved (v3.5 chuẩn, v3 deprecated)
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1 (v3 cũ): `input/srs-v3/...` — 6 states với `DA_DANH_GIA` ở cuối
- Source 2 (v3.5 mới): `input/srs-update-2026-5-5/srs-fr-08-danh-gia.md` §State machine — 8 states, KHÔNG có `DA_DANH_GIA`

  New states: `LAP_KE_HOACH → PHAN_CONG → CHO_DUYET_PC → THUC_HIEN → BAO_CAO → CHO_PHE_DUYET → HOAN_THANH (+ HUY end)`

- NotebookLM HTPLDN: match v3.5 (verify 2026-05-13 deep-verify)

#### Impact
- Bug ảnh hưởng: BUG-FUNC-DG-016 (đã close INVALID 2026-05-13)
- TC ảnh hưởng: tất cả TC ĐG dùng state cũ v3
- Round bị block: R20 deep-verify (đã xử lý)

#### BA decision
- Date: SRS v3.5 publish 2026-05-05 (implicit BA decision qua publish CHANGELOG)
- Decision: Dùng 8 states v3.5, deprecate `DA_DANH_GIA`. Test/bug từ R20 trở đi phải dùng v3.5.
- CHANGELOG updated: ✓ (`input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`)
- Bug/TC affected updated: ✓ (BUG-FUNC-DG-016 closed INVALID, lessons-learned 2026-05-13 entry)

---

### SRS-C-006 — FR-XI / FR-15 CT HTPLDN — File đính kèm: màn hình (C15) hứa upload vs data-model không có chỗ lưu — Open

**Phát hiện:** 2026-06-02 22:42:00 — Verify batch 2026-06-02 (STT 49)
**Trạng thái:** Open (BA-pending)
**Tester:** huongttt via Claude Code

#### Mâu thuẫn
- Source 1 (tầng màn hình): `input/srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:1132` — quote:
  > "| 19 | form | File dinh kem | file-upload (C15) | -- | upload | khi DU_THAO |"
  → SCR-XI-01 Tab Thông tin prescribe component upload file khi CT ở trạng thái DU_THAO.
- Source 2 (tầng Inputs): `input/srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:127-137` — FR-XI-01 Inputs liệt kê đúng 9 trường, KHÔNG có `file_dinh_kem`.
- Source 3 (tầng Entity): `input/srs-update-2026-5-5/srs-v3.5.md:2070-2083` — entity CHUONG_TRINH_HTPL (12-13 attribute) KHÔNG có cột file; ERD `srs-fr-15:1247-1259` không có quan hệ file.
- Source 4 (ràng buộc CHECK): `input/srs-update-2026-5-5/srs-v3.5.md:3238` — FILE_DINH_KEM CHECK liệt kê 8 `entity_type` (HOI_DAP, PHAN_HOI, VU_VIEC, LICH_SU_TRAO_DOI_TV, HOP_DONG_TU_VAN, BIEU_MAU, TVV_HO_SO, HO_SO_CHI_TRA) — **KHÔNG có CHUONG_TRINH_HTPL**.
- Changelog: A-ITEM-07 (CR-07 "upload PDF/Word mọi chức năng quản lý") liệt 8 entity áp dụng — KHÔNG gồm CHUONG_TRINH_HTPL.
- NotebookLM HTPLDN query 2026-06-02 (adversarial verify): **CONFIRM** — "Màn hình hứa upload nhưng Backend không có định nghĩa để lưu trữ" → khuyến nghị báo lỗi tài liệu cho BA.

#### Impact
- Bug ảnh hưởng: BUG-VERIFY-2026-06-02-#49 (Medium) — PATCH `/chuong-trinh-htpls/:id` có `fileDinhKemIds` → 500 `ERR-SYS-00-00-01`; không kèm → 200.
- Round: Verify batch 2026-06-02
- Severity: P2 (block xác lập expected của bug #49: "file phải lưu" hay "CT không hỗ trợ file")

> **Cập nhật 2026-06-05 13:53 (R-verify-2b):** Dev đã hiện thực **theo phương án (a)** — PATCH + `fileDinhKemIds` → 200, file persist với `entityType=CHUONG_TRINH_HTPL` (API verify CT-20260604-0001, 2 file). Bug #49 **Closed** (app hết defect, khớp màn hình C15 + yêu cầu đối tác) → entry này KHÔNG còn block bug nào, chỉ còn **việc sync tài liệu SRS**: thêm `CHUONG_TRINH_HTPL` vào CHECK `srs-v3.5.md:3245` + field file vào Inputs FR-XI-01 + entity 3.4.3.10/ERD. Khuyến nghị BA chốt **(a)** để tài liệu khớp hiện trạng; nếu chốt (b) thì là change request gỡ tính năng đang chạy.

#### Câu hỏi BA
CT HTPLDN (FR-XI-01) **có** hỗ trợ đính kèm file (component C15 ở line 1132) hay không? Nếu CÓ → cần bổ sung định nghĩa lưu trữ (Inputs + entity + FILE_DINH_KEM entity_type CHUONG_TRINH_HTPL). Nếu KHÔNG → gỡ component C15 khỏi màn SCR-XI-01.

#### Phương án đề xuất
- (a) **CT có hỗ trợ file:** bổ sung `CHUONG_TRINH_HTPL` vào FILE_DINH_KEM CHECK (`srs-v3.5.md:3238`) + thêm quan hệ file vào entity/ERD. Pros: khớp affordance UI line 1132. Cons: sửa data-model + BE persist. → khi đó bug #49 nâng Major (Data: ko lưu được file).
- (b) **CT không hỗ trợ file:** gỡ C15 khỏi `srs-fr-15:1132` + FE ẩn nút upload. Pros: data-model hiện tại nhất quán. Cons: bỏ tính năng đã vẽ ở UI.
- **Khuyến nghị:** BA chốt theo nghiệp vụ. Độc lập với (a)/(b): BE PHẢI sửa trả lỗi 4xx rõ ràng thay vì 500 `ERR-SYS` (lỗi xử lý ngoại lệ — bug #49).

#### BA decision  ← chưa có
- Date: TBD
- Decision: TBD
- CHANGELOG updated: ❌
- Bug/TC affected updated: ❌

---

### SRS-C-007 — FR-III-12 Đào tạo — Filter `vai_tro` ở tìm kiếm Giảng viên vs STT26 chuyển vai_tro xuống cấp buổi — Open

**Phát hiện:** 2026-06-26 17:30:00 — dot-3 rerun
**Trạng thái:** Open (BA-pending)
**Tester:** QA (Claude Code)

### Mâu thuẫn
- Source 1: `input/srs-update-2026-5-5/srs-fr-03-dao-tao.md:992` — FR-III-12 Inputs: "tu_khoa (text, N), linh_vuc_id (identifier, N), **vai_tro (text, N: GIANG_VIEN / TRO_GIANG)**" → tìm kiếm GV theo vai_tro cấp giảng viên.
- Source 2: `input/srs-update-2026-5-5/srs-fr-03-dao-tao.md:1883,1952,1963` — STT26 UAT 2026-05-26: "bỏ thuộc tính `vai_tro`" khỏi `KHOA_HOC_GIANG_VIEN`; "Vai trò gắn cấp buổi qua `LICH_HOC_GIANG_VIEN`, không gắn cấp Khóa nữa" → 1 GV không còn 1 vai_tro cố định.
- Quan sát UI: màn Giảng viên chỉ có filter "Lĩnh vực" + "Trạng thái", KHÔNG có filter vai_tro (đúng theo model mới Source 2).

### Impact
- TC ảnh hưởng: TC-GV-002 (report-dot-3 đánh FAIL → reclass Chờ BA).
- Severity: P2 (không block nghiệp vụ).

### Câu hỏi BA
Filter `vai_tro` ở tìm kiếm Giảng viên (FR-III-12): (a) bỏ hẳn theo STT26 (vai_tro giờ cấp buổi), hay (b) giữ filter với ngữ nghĩa "GV từng đảm nhận vai trò X ở ≥1 buổi"?

### Phương án đề xuất
- (a) Bỏ filter vai_tro khỏi FR-III-12 — khớp UI hiện tại + model STT26. Cons: mất khả năng lọc nhanh trợ giảng.
- (b) Giữ filter, đổi ngữ nghĩa thành "tồn tại buổi có vai_tro=X". Cons: cần BE join LICH_HOC_GIANG_VIEN.
- **Khuyến nghị:** (a) — đồng bộ STT26, UI đã theo hướng này.

### BA decision
- Date: TBD
- Decision: TBD
- CHANGELOG updated: ❌
- Bug/TC affected updated: ❌

---

### SRS-C-008 — FR-III Đào tạo — TC test optimistic-lock / idempotency / cảnh báo-sửa mà SRS không quy định — Open

**Phát hiện:** 2026-06-26 17:30:00 — dot-3 rerun
**Trạng thái:** Open (BA-pending)
**Tester:** QA (Claude Code)

### Mâu thuẫn
- Source 1 (TC kỳ vọng): TC-CTDT-E-030 / KH-E-038 / GV-022 kỳ vọng "2 user sửa đồng thời → ERR-SYS-02 'Bản ghi đã bị thay đổi…'" (optimistic-lock `updated_at`); TC-DEXUAT-E-015 kỳ vọng debounce double-click; TC-NHCH-008 kỳ vọng cảnh báo khi sửa câu hỏi đã phân phối.
- Source 2 (SRS): `srs-fr-03-dao-tao.md:510` chỉ có EC-03 "import KQ đồng thời → row-lock → ERR-DK-DT-04" (KHÁC cơ chế); `:889` WRN-NHCH-01 chỉ áp cho XÓA câu hỏi; SRS KHÔNG có ERR-SYS-02, không quy định optimistic-lock generic / idempotency double-submit / cảnh báo khi SỬA.

### Impact
- TC ảnh hưởng: TC-CTDT-E-030, TC-KH-E-038, TC-GV-022, TC-DEXUAT-E-015, TC-NHCH-008 (report-dot-3 đánh FAIL → reclass Chờ BA).
- Severity: P2.

### Câu hỏi BA
SRS có yêu cầu (1) optimistic-lock khi 2 cán bộ sửa đồng thời 1 bản ghi (CTĐT/KH/GV), (2) chống double-submit khi gửi đề xuất, (3) cảnh báo khi sửa câu hỏi đang dùng trong đề đã phân phối — hay đó là kỳ vọng TC tự thêm?

### Phương án đề xuất
- (a) SRS không yêu cầu → TC over-specify → bỏ/đổi các TC này thành non-applicable.
- (b) SRS thiếu sót, cần bổ sung yêu cầu concurrency/idempotency → BA viết clause + dev implement.
- **Khuyến nghị:** BA xác nhận từng mục; nếu (b) thì bổ sung SRS rồi mới re-test.

### BA decision
- Date: TBD
- Decision: TBD
- CHANGELOG updated: ❌
- Bug/TC affected updated: ❌

---

## Hướng dẫn workflow

### Phát hiện contradiction mới

1. **3-step verify TRƯỚC khi add entry:**
   - Grep SRS local hai version (v3 + v3.5) tìm cả 2 line conflict.
   - Query NotebookLM HTPLDN cùng câu hỏi.
   - Cross-check FR khác có cite enum/state/error code này.

2. **Add entry với ID tăng dần** (SRS-C-NNN).

3. **Update bug-report entry liên quan:**
   - Add note "depends on SRS-C-NNN BA decision".
   - Status: Open → BA-pending hoặc giữ Open kèm note.

4. **Update dev-fix-list:**
   - Move bug từ "Dev fix" section sang "Waiting BA confirm" section.

### Khi BA confirm

1. **Update entry status:** Open → Resolved + decision date + decision summary.
2. **Update CHANGELOG:** Append vào `CHANGELOG-v3-to-v3.5.md` hoặc tạo `CHANGELOG-fix-NNN.md`.
3. **Update SRS file gốc** (nếu BA yêu cầu): edit line conflict → align theo decision.
4. **Update tất cả bug/test reference:**
   - Bug entry liên quan: update quote + Status (đóng INVALID nếu decision invalidate bug, hoặc giữ Open chờ dev fix theo decision).
   - TC test plan: update expected behavior + state code.
   - Reference card `input/data/state-machines-v3.5.md`: update bảng nếu state machine đổi.

### Khi BA không phản hồi sau N round

- Round 1 sau escalate: gửi lại reminder + impact.
- Round 2: escalate tester lead + ghi blocker `[BA-NO-RESPONSE-NNN]` vào round report.
- Round 3+: defer bug/TC liên quan + ghi rõ "Waiting BA-Q-NNN >3 rounds, blocking ship UC X" trong dev-fix-list + escalate user (PO).

---

*Version: 1.0 — 2026-05-13. Maintained by QA team.*
*Mỗi entry phải có ≥2 source quote nguyên văn — không bịa, không suy luận.*

---

### SRS-C-009 — FR-I-08 Dashboard vs Nhóm VI Đánh giá — thang điểm `diem_tong` (0-100 vs trần thực 10) + thiếu điều kiện lọc trạng thái — Open

**Phát hiện:** 2026-07-27 — UAT đối tác tab tuần 1 (verify `TKDGHQHTPL_02` dòng 47)
**Phiếu gửi BA:** [`output/UAT_doi-tac/reverify-week-1/ba-confirmation-needed-TKDGHQHTPL_02-r2.md`](../output/UAT_doi-tac/reverify-week-1/ba-confirmation-needed-TKDGHQHTPL_02-r2.md)
**Trạng thái:** Open (BA/CĐT-pending)
**Tester:** QA nội bộ

#### Mâu thuẫn

**Phần A — thang điểm:**
- Source 1: `srs-v3.5/srs-fr-01-dashboard.md:416` — *"Biểu đồ trái — Điểm đánh giá hiệu quả hỗ trợ pháp lý (biểu đồ cột, **thang 0-100** theo điểm tổng đánh giá `KET_QUA_DANH_GIA.diem_tong` — ràng buộc 0-100)"*. Xem thêm `:450` — `diem_hai_long_tb` format *"thang **0-100**"*.
- Source 2: `srs-v3.5/srs-fr-08-danh-gia.md:1239` (BR-CALC-04) — *"Điểm tổng = SUM(diem_i * trong_so_i / 100)"*; `:1100` — `diem_toi_da` mặc định **10**; `:479` — ràng buộc `0 ≤ diem ≤ diem_toi_da`. ⇒ Với Σ trọng số = 100% và `diem_toi_da` mặc định, **trần thực tế của `diem_tong` là 10, không phải 100**.
- Nguồn gây lệch: `srs-v3.5/CHANGELOG-v3-to-v3.5.md:1734` — *"v3 FR-I-08 Outputs ghi `diem_hai_long_tb` thang 1-5, nhưng nhóm dữ liệu KET_QUA_DANH_GIA tại §4 v3 ràng buộc `diem_tong` từ 0 đến 100. **v4 sửa Outputs về thang 0-100 để đồng nhất với nhóm dữ liệu nguồn**"*. BA lấy **ràng buộc CSDL** (`:1049` `CHECK BETWEEN 0 AND 100` — vốn chỉ là khoảng giá trị hợp lệ) làm căn cứ đổi thang, **không đối chiếu BR-CALC-04**.
- `CHANGELOG-v3-to-v3.5.md:1729` còn ghi rõ mức lệch: *"v3 ghi điểm đánh giá theo thang 1-5 trong khi nhóm dữ liệu kết quả đánh giá thực tế lưu thang 0-100 — **lệch nhau 20 lần**"*.
- Hệ quả 3: xếp loại. `srs-fr-08-danh-gia.md:874` quy định *">=90% Xuất sắc / >=70% Tốt / >=50% Đạt / <50% Chưa đạt"* — theo **tỷ lệ %** trên trần riêng từng kế hoạch, không theo giá trị tuyệt đối. Nên một kết quả **10/10 = Xuất sắc** sẽ lên Dashboard thành **"10.0/100"**.

**Phần B — thiếu điều kiện lọc trạng thái:**
- Source 1: `srs-v3.5/srs-v3.5.md:5608` (BR-RPT-01) — *"Báo cáo thống kê SHALL chỉ tính trên bản ghi đã ở trạng thái cuối hợp lệ... Bản ghi `DU_THAO`, `CHO_PHE_DUYET`, `TU_CHOI`, `DA_HUY` **KHÔNG** được tính vào số liệu thống kê"* — nhưng cột "Áp dụng FR" chỉ ghi **`FR-IX-01..23` (toàn bộ nhóm Báo cáo)**, KHÔNG bao gồm FR-I-08 Dashboard.
- Source 2: `srs-v3.5/srs-fr-01-dashboard.md:441` — bước 2 chỉ ghi chung chung *"Tính điểm đánh giá hiệu quả hỗ trợ pháp lý trung bình từ kết quả đánh giá thuộc phạm vi"*, **không** nêu điều kiện `KET_QUA_DANH_GIA.trang_thai = 'DA_DANH_GIA'` hay `KE_HOACH_DANH_GIA.trang_thai != 'HUY'`.
- **NotebookLM HTPLDN cùng câu hỏi:** **match Source 2** cho cả 2 phần — xác nhận độc lập *"có sự mâu thuẫn nội bộ rất rõ ràng"* ở phần A, và gọi phần B là *"một sự bỏ sót trong đặc tả FR-I-08"*, khuyến nghị BA bổ sung filter guard vào bước 2.

#### Impact
- Bug/TC ảnh hưởng: `TKDGHQHTPL_02` (tuần 1 dòng 47 — đối tác báo Dashboard hiện **164.0/100**, `164.0 ÷ 8.2 = 20` đúng bằng mức lệch 20 lần ở `CHANGELOG:1729`) · `TKDGHQHTPL_OOS_01` (tuần 1 dòng 276 — phần B)
- Số liệu quan sát: Dashboard hiện **29.5/100 "Dựa trên 14 đánh giá"** trong khi chỉ có **11** kết quả `DA_DANH_GIA`; trung bình trộn 11 bản thang-10 + 1 bản thang-200 + 3 bản legacy thang-100.
- Severity: **P1** — chỉ số quản trị cấp Bộ đang hiển thị sai bản chất; dev không thể tự sửa vì công thức chưa chốt.

#### Phân tích phương án (làm lại 2026-07-27 lượt 2 — kết luận ĐẢO so với lượt 1)

Lượt 1 khuyến nghị (a) "quy đổi % ở Dashboard". **Lượt 2 loại (a)** sau khi đọc ý định gốc của BA ở `CHANGELOG-v3-to-v3.5.md:1729` và cách màn chi tiết hiển thị ở `srs-fr-08-danh-gia.md:873`.

| Phương án | `:416` thang 0-100 theo `diem_tong` | `:1049` CHECK 0-100 | `:874` xếp loại % | `CHANGELOG:1729` đối chiếu được với màn chi tiết | Cộng TB chéo kế hoạch |
|---|:-:|:-:|:-:|:-:|:-:|
| (a) Dashboard quy đổi sang % | ✗ | ✓ | ✓ | **✗** | ✓ |
| (b) Giữ số thô, đổi mẫu số theo trần từng kế hoạch | ✗ | ✓ | ✓ | ✓ | **✗** |
| **(c) Ràng buộc cấu hình để trần luôn = 100** | ✓ | ✓ | ✓ | ✓ | ✓ |

- **(a) LOẠI:** `srs-fr-08-danh-gia.md:873` — màn chi tiết hiển thị cột *"Điểm tổng (tự tính = tổng điểm x trọng số / 100)"*, tức **số thô** (8,6). Quy đổi Dashboard sang % ⇒ Dashboard **86** vs chi tiết **8,6**. Đây đúng là lỗi `CHANGELOG:1729` đã chủ động sửa: *"Cán bộ nghiệp vụ nhìn biểu đồ Dashboard hiển thị '3.5' trong khi báo cáo chi tiết hiển thị '70' cho cùng một vụ, **không cách nào đối chiếu**"*. (a) tái tạo lại đúng lỗi cũ.
- **(b) LOẠI:** mỗi kế hoạch một trần khác nhau ⇒ không cộng trung bình chéo kế hoạch được, mà đó lại là mục đích chính của thẻ.
- **(c) CHỌN — thoả toàn bộ.** Củng cố: dữ liệu đời trước `KHDG-SEED-0001` mang điểm **80 / 60 / 90**, tức đã ở thang 0-100 từ trước ⇒ thang 0-100 nhiều khả năng luôn là thiết kế gốc, còn `diem_toi_da` mặc định **10** (`:1100`) mới là chỗ lệch.

⇒ **Vị trí sửa: nhóm VI Đánh giá (cấu hình + validation `diem_toi_da`), KHÔNG phải Dashboard.** Dashboard đang hiển thị đúng như `:416` mô tả.

#### Câu hỏi BA / CĐT (đã thu hẹp — chỉ cần trả lời có/không)

1. **Bổ sung ràng buộc còn thiếu:** `Σ (diem_toi_da_i × trong_so_i / 100) = 100` cho mỗi kế hoạch. Hiện `:191` chỉ ghi `diem_toi_da` — *"> 0, số nguyên dương"*, `:850` UI cũng chỉ *"number > 0"*; **không dòng nào ràng buộc tổng** (riêng trọng số thì đã bị ép SUM=100% ở `:850` + BR-CALC-04). Đây là **thêm luật nghiệp vụ mới** ⇒ dev không tự quyết.
2. **Duyệt migration:** kế hoạch đang cấu hình `diem_toi_da = 10` phải quy đổi hay chấp nhận lệch vĩnh viễn? Đụng kết quả đã chấm ⇒ cần thẩm quyền duyệt.
3. **Phần B:** FR-I-08 có chịu ràng buộc BR-RPT-01 không — Dashboard có phải loại `KET_QUA_DANH_GIA.trang_thai = 'CHUA_DANH_GIA'` và kết quả thuộc kế hoạch `HUY` khỏi cả trung bình lẫn cỡ mẫu? Đề nghị **mở rộng phạm vi áp dụng BR-RPT-01 sang FR-I-08** — hiện `srs-v3.5.md:5608` mới liệt kê `FR-IX-01..23`.

#### Lỗ hổng độc lập phát hiện kèm

`diem_toi_da` để tự do (`:191` *"> 0, số nguyên dương"*) trong khi `diem_tong` bị chặn `CHECK BETWEEN 0 AND 100` (`:1049`). Cấu hình `diem_toi_da = 200` rồi chấm 150 ⇒ `diem_tong = 150`, **vi phạm chính ràng buộc đó**. Đã dựng thử kế hoạch `diem_toi_da = 200` trên env nip.io — **hệ thống chấp nhận**. Câu hỏi 1 nếu được duyệt sẽ bịt luôn lỗ hổng này.

#### BA decision  ← fill khi resolved
- Date:
- Decision:
- CHANGELOG updated:
- Bug/TC affected updated:

---

### SRS-C-010 — FR-IX Báo cáo thống kê — tệp PDF xuất ra có phải theo khung văn bản hành chính TT 17/2025 (quốc hiệu + khối ký) hay không — Open

**Phát hiện:** 2026-08-03 — re-verify vòng 2 UAT đối tác (đợt 53 bug Reopen)
**Trạng thái:** Open
**Tester:** QA (huongttt)

#### Mâu thuẫn

- **Source 1 —** `srs-fr-11-bao-cao.md:86` (Processing chung TPL-REPORT-FULL): *"Nếu xuất PDF: tạo file .pdf giữ nguyên định dạng trình bày theo Thông tư 17/2025 (khổ A4, font Times New Roman cỡ 13)"*. Lặp lại ở `:124` (Tiêu chí chấp nhận) và `:1052-1053` (SCR — nút Xuất Excel/Xuất PDF "→ xuất theo format TT17/2025").
- **Source 2 —** `srs-v3.5.md:6670-6675` (Phụ lục D.2.4, khối *"Format chung theo TT 17/2025"*): *"Header: Quốc hiệu + Tên cơ quan ban hành"* · *"Footer: Ngày ký + Chức danh người ký + Con dấu (nếu in chính thức)"*. Khối này nằm dưới heading **D.2.4 Mapping mẫu biểu TT 17/2025/TT-BTP** vốn chỉ liệt kê **Mẫu 21a / 21b** — và `D.2.3 Export format` khai định dạng xuất của 2 mẫu đó là **Excel (.xlsx) + Word (.docx)**, KHÔNG có PDF.
- **Source 3 —** cũng bảng D.2.4, cột *"FR tham chiếu"* lại gán 2 mẫu 21a/21b cho **`FR-IX-01~23 (TPL-REPORT-FULL)`** — tức buộc cả họ báo cáo nhóm IX vào khung TT 17/2025.
- **Source 4 —** `srs-fr-11-bao-cao.md:1092` (Quy tắc tương tác SCR): *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file"* — mô tả header tệp xuất gồm đúng 4 mục, không nhắc quốc hiệu/khối ký.
- **NotebookLM HTPLDN cùng câu hỏi:** khớp **Source 2 + 3** — trả lời *"CÓ BẮT BUỘC"*, dẫn chính khối D.2.4 và ghi nhận việc bảng này gán tham chiếu cho toàn bộ 23 chức năng báo cáo IX. Đồng thời trích CHANGELOG v3→v4: đổi Word→PDF với lập luận *"PDF giữ đúng định dạng A4, font Times New Roman 13pt theo Thông tư 17/2025"*, **kèm cảnh báo ngay trong đặc tả**: *"Cần Cán bộ phụ trách xác nhận Thông tư 17/2025 có thực sự yêu cầu PDF hay chấp nhận Word — đoạn trích dẫn về Mẫu 21a/21b cũng chưa được tra cứu lại"*.

Hai nguồn **thống nhất** ở 2 điểm phụ: quy ước đặt tên tệp `BaoCaoXxx_{YYYYMMDD_HHmm}` **không có** trong SRS cho nhóm IX (chỉ FR-II-01 có `HoiDap_{YYYYMMDD_HHmm}.xlsx`), và **"hỗ trợ ký số điện tử" không có** ở nhóm IX (chỉ FR-III-20 Đào tạo yêu cầu ký số).

#### Trạng thái phần mềm (đo trực tiếp 03/08/2026, build V1.0.4)

Tệp PDF xuất từ màn Báo cáo thống kê: A4 (595×842 pt) ✔ · font Tinos (bản tương đương chuẩn của Times New Roman) ✔ · header đủ 4 mục theo Source 4 ✔ · **không có quốc hiệu / tên cơ quan** ✘ · **không có ngày ký / chức danh** ✘ · tên tệp `bao-cao-<slug>-YYYY-MM-DD.pdf`.

Đối chiếu: báo cáo theo mẫu TT 17/2025 thật (Đánh giá hiệu quả → tab Báo cáo → Xuất DOCX/XLSX) **đã có đủ** quốc hiệu, tiêu ngữ, dòng *"(Theo mẫu Thông tư số 17/2025/TT-BTP)"*, mục I→V và bảng ký — xem `BUG-BCDG-XLSX-KHONG-THEO-MAU-TT17` (Closed 29/07). Tức hệ thống có làm khung TT17, nhưng chỉ ở báo cáo đó.

#### Impact

- **TC ảnh hưởng:** 22 phiếu UAT xuất PDF (SLHDVM_07, VVDTN_07, VVDHT_07, VVDHTHT_07, VVTTG_06, CLDTBDDDR_07, LDTBDDDR_07, CGTVPL_07, DGHQHTPL_07, CLDTBDPL_07, VVTDVQL_07, VVTLV_06, VVTLHDN_06, VVTTGCT_06, CPHTCT_07, CPCTHTTDVQL_07, CPCTHTTLHDN_07, CPCTHTTTG_06, SLCTHT_07, CTTDVQL_05, CTTLV_06, CTTTG_05) — sheet đối tác tuần 3.
- **Round bị chặn:** re-verify vòng 2 (03/08/2026) — đã ghi `Verify 2 = BA confirm` cho các phiếu này thay vì Pass/Reopen.
- **Severity:** P1 — chấm Pass thì lờ chỗ lệch, chấm Reopen thì đẩy sang dev một yêu cầu chưa chắc có trong đặc tả.
- **22 phiếu xuất Excel — đã chấm `Pass`**, nhưng **17/22 phiếu** (CLDTBDDDR_06, LDTBDDDR_06, CGTVPL_06, DGHQHTPL_06, CLDTBDPL_06, VVTDVQL_06, VVTLV_05, VVTLHDN_05, VVTTGCT_05, CPHTCT_06, CPCTHTTDVQL_06, CPCTHTTLHDN_06, CPCTHTTTG_05, SLCTHT_06, CTTDVQL_04, CTTLV_05, CTTTG_04) có KQ mong đợi ghi thêm tên tệp dạng `BaoCaoXxx_{YYYYMMDD_HHmm}.xlsx`, trong khi app đặt `bao-cao-<slug>-YYYY-MM-DD.xlsx` (vd `bao-cao-lop-dao-tao-dang-dien-ra-2026-08-03.xlsx`). **Vẫn để Pass** vì đây là chênh lệch hình thức, không đổi tính dùng được của tệp, và SRS không quy định — nhưng nếu BA chốt câu 3 theo hướng "có quy ước tên tệp" thì **17 phiếu này phải mở lại**. 5 phiếu còn lại (SLHDVM_06, VVDTN_06, VVDHT_06, VVDHTHT_06, VVTTG_05) không đòi tên tệp → Pass sạch, không phụ thuộc quyết định BA.

#### Câu hỏi BA

1. Tệp PDF của **màn Báo cáo thống kê (nhóm IX)** có phải trình bày theo khung văn bản hành chính TT 17/2025 — quốc hiệu + tên cơ quan ở đầu, ngày ký + chức danh người ký ở cuối — hay chỉ cần 4 mục header theo `srs-fr-11-bao-cao.md:1092`?
2. Nếu **có**: khối D.2.4 cần ghi rõ áp cho cả nhóm IX và bổ sung PDF vào D.2.3; nếu **không**: cần bỏ cụm *"theo Thông tư 17/2025"* ở `:86`/`:124`/`:1052-1053` vì đang kéo theo cả khung hành chính ngoài ý định.
3. Quy ước đặt tên tệp xuất của nhóm IX — **áp cho cả .xlsx lẫn .pdf**: bổ sung (theo kiểu `BaoCaoXxx_{YYYYMMDD_HHmm}` như đối tác kỳ vọng và như FR-II-01 đang dùng `HoiDap_{YYYYMMDD_HHmm}.xlsx`, hay theo kiểu chữ-thường-gạch-nối như FR-XIII `kho-cau-hoi-{YYYYMMDD-HHmm}.xlsx` và như app hiện làm) hay xác nhận không quy định? Câu này quyết định 17 phiếu Excel đang để `Pass` có phải mở lại hay không, nên xin BA trả lời cả khi câu 1 chốt là "không bắt buộc khung hành chính".
4. Báo cáo nhóm IX có cần hỗ trợ ký số điện tử không? (Hiện chỉ FR-III-20 yêu cầu.)

#### Phương án đề xuất

Chốt **câu 1 theo hướng "không bắt buộc"** + dọn câu chữ `:86`/`:124`/`:1052-1053`: báo cáo nhóm IX là báo cáo nghiệp vụ nội bộ (chính CHANGELOG mô tả vậy — *"phục vụ cán bộ và lãnh đạo trong nội bộ cơ quan, khác báo cáo định kỳ gửi cấp trên thuộc nhóm FR-15"*), không phải văn bản trình ký. Khung TT 17/2025 giữ nguyên cho mẫu 21a/21b và báo cáo Đánh giá hiệu quả. Nếu BA chốt ngược lại thì đây là bug thật của dev và 22 phiếu chuyển Reopen.

#### BA decision  ← fill khi resolved
- Date:
- Decision:
- CHANGELOG updated:
- Bug/TC affected updated:
