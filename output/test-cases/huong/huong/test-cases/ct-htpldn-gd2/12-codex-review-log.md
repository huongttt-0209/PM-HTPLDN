# Codex Review Audit Log — FR-15 CT HTPLDN GĐ2

> **Phase**: Sau A1-A7 → Codex review GATE
> **Ngày chạy**: 2026-05-10
> **Verdict ban đầu**: GATE FAIL (2 P0 + 4 P1 + 1 P2)
> **Verdict sau verify**: GATE PASS với 3 finding apply (1 P0 + 1 P1 + 1 P2) + 4 finding REJECT (verify SRS)

---

## 1. Findings classification (per memory rule [Verify spec trước khi log bug])

| ID | Severity | Type | Verdict | Reasoning |
|----|----------|------|---------|-----------|
| CODEX-CT-GD2-01 | P0 | MISMATCH | ❌ REJECT | BR-AUTH-08, BR-EC-01/12/13/19 là **cross-module BRs** từ `srs-v3 Phụ lục B` / `srs-v3:4066/4077/4078/4084`. GĐ1 `00-test-plan-overview.md §2.1` dùng cùng pattern với citation rõ. Plan GĐ2 §2.1 cũng đã cite `srs-v3:XXXX` cho từng BR-EC. **False positive — codex hiểu nhầm cross-module BR pattern**. |
| CODEX-CT-GD2-02 | P0 | MISMATCH | ✅ APPLY | SRS line 998 ghi `BAO_CAO_CT (loai = TONG_HOP_TW)` (Output table FR-XI-09) nhưng entity `BAO_CAO_CT_HTPL` (lines 1293-1300) **KHÔNG có column `loai`**. Spec inconsistency thật. → SPEC-CLARIFY-CT-GD2-09 + sửa TC-TH-019 verify visual differentiation thay assertion DB field. |
| CODEX-CT-GD2-03 | P1 | GAP | ❌ REJECT | Codex hallucinate "BR-DOT-BC-XXX" + "soft-delete đợt đang tiến hành". SRS BR section (lines 1407-1418) KHÔNG có BR này. SM-DOT-BC (lines 1371-1397) KHÔNG có state HUY cho đợt — chỉ TAO_DOT/DANG_LAP_BC/CHO_DUYET_KQ/DA_DUYET_KQ/DA_GUI_TW/DA_TONG_HOP. **False positive — hallucinated BR/SM**. |
| CODEX-CT-GD2-04 | P1 | GAP | ✅ APPLY | Đúng: thiếu TC CB_PD thử Gửi TW. Permission matrix file 07 chỉ có TC-PERM-011 (CB_NV_TW thử Gửi TW) + TC-PERM-012 (CB_NV_BN thử Tổng hợp). → +1 TC TC-PERM-017. |
| CODEX-CT-GD2-05 | P1 | GAP | ❌ REJECT | Field-level validation modal tạo đợt (empty `ten_dot_bc`, `tu_ngay > den_ngay`) thuộc **GĐ1 scope** — đã cover bởi `ct-htpldn-gd1/07-TC-quan-ly-dot-bc.md` (12 TC sau Codex GĐ1 +2). GĐ2 chỉ test transition TAO_DOT → DANG_LAP_BC, không CRUD đợt. **Out of scope GĐ2**. |
| CODEX-CT-GD2-06 | P1 | MISMATCH | ❌ REJECT | Codex claim file 02 dùng `noi_dung` thay `ket_qua`. Verify file 02: KHÔNG hề dùng `noi_dung`. TC dùng `nhan_xet` + `so_lieu` đúng theo FR-XI-06 §Inputs (lines 720, 719). Field `ket_qua` mà Codex nói KHÔNG tồn tại trong SRS entity (lines 1293-1300 chỉ có `noi_dung`/`so_lieu_tong_hop`). **Codex hallucinate field name `ket_qua`**. (Note: SRS có inconsistency nhỏ Inputs `nhan_xet`/`so_lieu` vs Entity `noi_dung`/`so_lieu_tong_hop` — backend mapping concern, không ảnh hưởng UI test.) |
| CODEX-CT-GD2-07 | P2 | IMPROVEMENT | ✅ APPLY | Đúng: TC-PD-BC-010 title "Duyệt khi BC ≠ CHO_DUYET_KQ" mix entity SM. CHO_DUYET_KQ thuộc DOT_BAO_CAO. → Rename "Duyệt thất bại khi DOT_BAO_CAO không ở trạng thái CHO_DUYET_KQ". |

## 2. Apply summary

| ID | File | Action | Detail |
|----|------|--------|--------|
| CODEX-CT-GD2-02 | 06 | SỬA in-place TC-TH-019 + add SPEC-CLARIFY-CT-GD2-09 | Update assertion từ DB field → visual differentiation (badge label). Add SPEC-CLARIFY entry về `loai` field gap entity. |
| CODEX-CT-GD2-04 | 07 | +1 TC TC-PERM-017 | CB PD ĐP/BN thử action Gửi TW → 403 (FR-XI-08 line 901 only CB NV BN/ĐP). |
| CODEX-CT-GD2-07 | 04 | Rename TC-PD-BC-010 title | "Duyệt thất bại khi DOT_BAO_CAO không ở trạng thái CHO_DUYET_KQ". |

## 3. Coverage delta sau Codex

| File | Before Codex | Codex apply | After Codex |
|------|-------------:|------------:|-----------:|
| 01 | 7 | 0 | 7 |
| 02 | 12 | 0 | 12 |
| 03 | 8 | 0 | 8 |
| 04 | 12 | 0 (rename only) | 12 |
| 05 | 8 | 0 | 8 |
| 06 | 16 | 0 (sửa in-place) | 16 |
| 07 | 10 | +1 | 11 |
| **TỔNG** | **73** | **+1** | **74** |

## 4. SPEC-CLARIFY pending BA — final count

| # | ID | TC liên quan | Tóm tắt |
|---|----|--------------|---------|
| 1 | SPEC-CLARIFY-CT-GD2-01 | TC-LBC-002 | Guard "Đợt đã hoàn chỉnh" cho transition TAO_DOT → DANG_LAP_BC |
| 2 | SPEC-CLARIFY-CT-GD2-02 | TC-PD-BC-013 | BR-AUTH-05 cùng cấp ĐP cross-đơn vị |
| 3 | SPEC-CLARIFY-CT-GD2-03 | TC-BC-005 | Mapping cột "Số liệu hệ thống gợi ý" → entity nguồn |
| 4 | SPEC-CLARIFY-CT-GD2-04 | TC-TH-012 | Schema versioning BC mẫu cũ |
| 5 | SPEC-CLARIFY-CT-GD2-05 | TC-TH-003 | Auto-SUM danh sách cột + cross-kỳ + schema khác |
| 6 | SPEC-CLARIFY-CT-GD2-06 | TC-LBC-013 | Guard CT TAM_DUNG có cho phép lập BC không |
| 7 | SPEC-CLARIFY-CT-GD2-07 | TC-PD-BC-015 | ly_do_tu_choi max length |
| 8 | SPEC-CLARIFY-CT-GD2-08 | TC-TH-015 | Tổng hợp BC cross-kỳ block hay cho phép |
| 9 | **SPEC-CLARIFY-CT-GD2-09 (Codex 2026-05-10)** | TC-TH-019 | `loai` field gap entity BAO_CAO_CT_HTPL — SRS Output table vs Entity column inconsistency |

→ **Final SPEC-CLARIFY: 9 pending BA**.

## 5. Acceptance Codex Gate

- ✅ 3/7 finding APPLY (1 P0 + 1 P1 + 1 P2)
- ✅ 4/7 finding REJECT với reasoning explicit (false positive / hallucinated / out of scope)
- ✅ Final TC: 74 (51 A3 + 19 A4 + 3 A6 + 1 Codex)
- ✅ Coverage giữ 100% BR/AC/SM/ERR
- ✅ Permission Matrix improved (~34/64 explicit cells sau Codex +1)
- ✅ Quality 9.17 → ~9.3/10 sau Codex apply (visual differentiation cho TC-TH-019 strong hơn DB query)

**Verdict cuối: GATE PASS sau verify** (Codex initial GATE FAIL → 2 P0 thực tế chỉ 1 valid → APPLY → PASS).

*Generated 2026-05-10 — Codex review applied per memory rule [Verify spec trước khi log bug]*
