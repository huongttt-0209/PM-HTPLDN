# A4 Review — Edge Case Hunter (audit log)

> **Module**: QTHT Nhật ký Hệ thống (FR-VIII-28)
> **Ngày chạy**: 2026-05-08
> **Skill**: bmad-review-edge-case-hunter (manual) — tham chiếu pattern Biểu mẫu / Đào tạo
> **Output**: TC mới đã merge inline vào file UC; file này chỉ là audit log proposal + mapping.
> **Iron rule (plan §3.1):** TC mới PHẢI merge vào file UC gốc. File 08 là audit log, KHÔNG phải TC source.

---

## 1. Phương pháp

Phân tích FR-VIII-28 + SCR-VIII-10 v3.1 theo 7 categories edge case:

| Category | Mô tả | TC merged |
|----------|-------|-----------|
| Boundary numeric/date | 89/90/91 ngày, 9999/10K/10001 dòng | TC-NK-134/135/136, TC-NK-EXP-007/008/009 |
| Timezone / DST | UTC+7 day boundary | TC-NK-137 |
| Empty / null state | Empty result, default fallback | TC-NK-138, TC-NK-EXP-005 |
| Soft-delete reference | User đã `is_deleted=1` còn truy log | TC-NK-139 |
| Immutability invariant | BR-DATA-05 verify UI + BE | TC-NK-141, TC-NK-142, TC-NK-PERM-008, TC-NK-PERM-009 |
| Performance / large dataset | 50K rows trong 90 ngày | TC-NK-143, TC-NK-EXP-011 |
| UX state restore | Reset filter, sort badge | TC-NK-140, TC-NK-144 |
| Security download URL | Export URL không công khai | TC-NK-EXP-012 |
| Limit conflict (SPEC-CLARIFY) | 10K vs 50K limit | TC-NK-EXP-009, TC-NK-EXP-010 |

---

## 2. Proposal & Reasoning chi tiết

### 2.1 Boundary 90 ngày (constraint v3.1 mới — phải cover bound)

**Lý do:** FR-VIII-28 step 2 nguyên văn "den - tu <= 90 ngày" + ERR-LOG-02. Nếu chỉ có TC > 90 ngày (TC-NK-120) → miss bound 89/90/91. Off-by-one bug rất phổ biến với operator `<=` vs `<`.

**Merge mapping:**
- `01-TC-tra-cuu-loc-nhat-ky.md` Section C → TC-NK-134 (89 days VALID), TC-NK-135 (= 90 VALID — bound), TC-NK-136 (91 REJECT).

### 2.2 Boundary 10.000 dòng Excel (BR-DATA-06 + SPEC-CLARIFY-NHATKY-01)

**Lý do:** SRS line 1348 + 1371 + Phụ lục B đều ghi 10K. SCR-VIII-10 line 1830 ghi 50K. Bug phổ biến: BE/FE không đồng bộ limit. TC bao quát cả 2 limit để Phase B verify thực tế.

**Merge mapping:**
- `02-TC-xuat-excel-nhat-ky.md` Section C → TC-NK-EXP-007 (9999), TC-NK-EXP-008 (=10000), TC-NK-EXP-009 (10001 truncate/reject), TC-NK-EXP-010 (50001 — verify limit thực tế).

### 2.3 Timezone UTC+7

**Lý do:** Hệ thống VN dùng `Asia/Ho_Chi_Minh` (UTC+7). Bug phổ biến: BE lưu UTC nhưng filter dùng client TZ → mất bản ghi 23:59:59 hoặc lệch ngày. AUDIT_LOG là audit nên timestamp accuracy cực kỳ quan trọng cho compliance.

**Merge mapping:**
- TC-NK-137 (Section C 01-TC).

### 2.4 Soft-delete user filter

**Lý do:** SRS line 1335 nói dropdown "Người dùng" → TAI_KHOAN. Nhưng TAI_KHOAN có `is_deleted=1` (BR-DATA-01). Audit log immutable nên log của user xóa vẫn còn. Câu hỏi: dropdown filter có cho chọn user xóa không? Đây là edge case quan trọng để compliance retention 5 năm vẫn truy được log.

**Merge mapping:**
- TC-NK-139 — link SPEC-CLARIFY-NHATKY-06.

### 2.5 Immutability double-verify (UI + BE)

**Lý do:** BR-DATA-05 + A.3 nguyên văn AUDIT_LOG INSERT-only. Nhưng "không có nút UI" không đảm bảo BE cũng reject. Tester phải verify cả 2 layer (defense in depth).

**Merge mapping:**
- TC-NK-141 (UI verify), TC-NK-142 (BE reject DELETE/PATCH qua devtools).
- TC-NK-PERM-008 (immutable UI cross-check), TC-NK-PERM-009 (immutable BE cross-check).

### 2.6 Performance — 50K rows 90 ngày

**Lý do:** SCR-VIII-10 line 1831 nguyên văn "index trên (thoi_gian, module, entity_type), partition theo tháng nếu cần". Production AUDIT_LOG có thể đạt vài triệu rows. TC verify perf trong production-like dataset.

**Merge mapping:**
- TC-NK-143 (search perf), TC-NK-EXP-011 (export perf 30s).

### 2.7 UX state restore

**Lý do:** Khi search filter phức tạp + reload trang, user expect filter giữ. Tương tự nút "Xóa bộ lọc" phải clear hết. Bug phổ biến: clear không reset URL state, hoặc reload mất filter.

**Merge mapping:**
- TC-NK-144 ([Xóa bộ lọc] reset).
- TC-NK-140 (sort badge column behavior).
- TC-NK-138 (dropdown empty).

### 2.8 Security: download URL public

**Lý do:** Nếu BE serve file qua URL pre-signed/public, attacker có thể leak URL. Nếu serve qua streaming với JWT check thì OK.

**Merge mapping:**
- TC-NK-EXP-012.

---

## 3. Tổng kết merge

| File | Base TC (A3) | A4 merged | Final |
|------|-------------:|----------:|------:|
| 01-TC-tra-cuu-loc-nhat-ky.md | 21 | 9 | 30 |
| 02-TC-xuat-excel-nhat-ky.md | 8 | 4 | 12 |
| 03-TC-permission-matrix.md | 7 | 2 | 9 |
| **Total** | **36** | **15** | **51** |

> Ghi chú: số "A4 merged" tính theo TC mới phát sinh từ edge analysis. Một số TC trong base section C cũng có sẵn label edge — không double-count.

---

## 4. Edge case xét nhưng KHÔNG merge (out of scope hoặc duplicate)

| Đề xuất | Lý do drop |
|---------|-----------|
| Concurrent export — 2 QTHT cùng export 1 lúc | OUT-OF-SCOPE: Module read-only, không có lock contention. Performance test riêng nếu cần. |
| Audit log retention — sau 5 năm tự xóa? | OUT-OF-SCOPE Phase A — đây là cron job DB-level, A7 sẽ LOẠI nếu có. SRS không nói rõ retention enforcement (5 năm là policy, không phải code). |
| AUDIT_LOG schema migration backwards-compat | OUT-OF-SCOPE: data migration không phải user-facing. |
| Audit log từ scheduled job (cron) — actor là "system" | Đã cover qua TC-NK-105 (filter "Tạo") nếu seed có log từ scheduled job — không cần TC riêng. |
| Filter combine 5+ trường cùng lúc | DUPLICATE: TC-NK-107 đã cover 4-trường combo, 5+ là incremental không thêm value. |
