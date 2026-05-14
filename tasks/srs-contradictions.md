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
