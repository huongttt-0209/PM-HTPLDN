# A7 — Manual Filter Log (FR-14 Hợp đồng Tư vấn)

> **Ngày:** 2026-05-10
> **Phương pháp:** Manual sweep 80 TC theo rule "UI/function-testable, KHÔNG TC chỉ test DB/API thuần".

---

## 1. Tiêu chí filter

- ❌ **LOẠI**: TC chỉ chạy được qua curl/Postman/DB inspect (không có UI để observe).
- ✅ **GIỮ**: TC có thể quan sát qua chrome-devtools MCP (UI render, form, table, toast, badge, redirect, audit timeline, file download).
- 🔧 **REWRITE**: TC concept đúng nhưng cần điều chỉnh step để observable trên UI (vd: thay vì check DB row, check qua reload + xem accordion / nhật ký).

---

## 2. Sweep result per file

### File 01 (25 TC) — `01-TC-quan-ly-hd-tv-CRUD.md`

| TC | Verdict | Note |
|----|---------|------|
| TC-HDTV-001..006 (Happy) | ✅ GIỮ | UI: Form, list, badge, Excel download |
| TC-HDTV-010..014 (Negative) | ✅ GIỮ | UI: toast/inline error |
| TC-HDTV-020 (boundary date) | ✅ GIỮ | Form submit |
| TC-HDTV-021 (highlight đỏ ≤30d) | ✅ GIỮ | UI: cell color via Snapshot |
| TC-HDTV-022 (concurrent SEQ) | ✅ GIỮ | 2 tab + check mã trên list |
| TC-HDTV-023 (ben_a auto) | ✅ GIỮ | Form field readonly |
| TC-HDTV-024..028 (A4) | ✅ GIỮ | Dropdown filter, Excel scope, file upload, mã format observable |
| TC-HDTV-030..033 (A6 SM) | ✅ GIỮ | UI button click (a) hoặc form field edit (b) |
| TC-HDTV-034 (A6 ghi_chu) | ✅ GIỮ | Textarea paste + form submit |

**Verdict file 01:** 25/25 GIỮ.

### File 02 (9 TC) — `02-TC-moc-tien-do.md`

| TC | Verdict |
|----|---------|
| Tất cả 9 TC | ✅ GIỮ — Inline-edit table observable; JSON array verify qua reload |

### File 03 (11 TC) — `03-TC-thanh-toan-giai-doan.md`

| TC | Verdict |
|----|---------|
| Tất cả 11 TC | ✅ GIỮ — Inline-edit + progress bar UI observable |

### File 04 (11 TC) — `04-TC-lien-ket-vu-viec.md`

| TC | Verdict |
|----|---------|
| Tất cả 11 TC | ✅ GIỮ — Modal multi-select, badge count, embedded drawer cross-module observable |

### File 05 (12 TC) — `05-TC-tim-kiem-hd-tv.md`

| TC | Verdict |
|----|---------|
| TC-HDTK-001..022 (12 TC) | ✅ GIỮ — Filter form, list refresh, empty state, pagination, SQL injection input observable |

### File 06 (12 TC) — `06-TC-permission-matrix.md`

| TC | Verdict |
|----|---------|
| TC-PERM-001..003 (Happy) | ✅ GIỮ — UI menu / button visibility |
| TC-PERM-010..015 (Negative) | ✅ GIỮ — 403 page / no menu / IDOR direct URL |
| TC-PERM-014 (force POST) | 🔧 REWRITE-OK — vẫn UI testable: log action qua DevTools Network tab + observe response |
| TC-PERM-020..022 (A4) | ✅ GIỮ — Same pattern |

**Verdict file 06:** 12/12 GIỮ.

---

## 3. Tổng kết A7 (sau Codex review apply)

| Metric | Value |
|--------|-------|
| Total TC sau A1-A7 | 80 |
| Codex review +5 (TC-HDTV-029 + TC-PERM-023..026) | 85 |
| LOẠI | 0 |
| REWRITE concept (P0-1 SM → status field) | 4 (TC-HDTV-030..033 — vẫn UI testable, chỉ thay framing) |
| OBS Excluded (so_hop_dong, ngay_ky entity field; JSON CHECK constraint) | 3 (HDTV-17 + HDTV-18) |
| GIỮ | 85 |
| **Phase A done count** | **85 TC** |

---

## 4. Lý do KHÔNG có TC API thuần

- FR-14 KHÔNG có API outbound (business §9 line 152 quote: "Không chia sẻ qua Cổng PLQG, HĐ TV không nằm trong 18 API FR-16").
- KHÔNG có API inbound (02-thu-tu-module:641 quote "Có thể upload nhiều file đính kèm. Không có API inbound").
- Toàn bộ 80 TC là UI flow trong CMS, có thể chạy qua chrome-devtools MCP.

---

*A7 done 2026-05-10 — 0 LOẠI / 0 REWRITE / 80 GIỮ. 100% UI/function-testable.*
