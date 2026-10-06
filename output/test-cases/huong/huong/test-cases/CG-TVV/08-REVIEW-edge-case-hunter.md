# 08 — Edge Case Hunter Review (Audit Log)

> **Audit only** — TC mới đã MERGE TRỰC TIẾP vào file UC tương ứng (Section "E. Edge bổ sung"). File này chỉ ghi history proposal + reasoning + merge mapping. KHÔNG phải TC source — Phase B chỉ ref file UC `01-14-TC-*.md`.
> **Ngày**: 2026-05-09 · **Tester**: Claude · **Iron rule**: BMAD A4 inline merge

---

## Edge categories scan + merge mapping

| Category | Coverage trong A3 base? | Edge mới đề xuất | Merge target file |
|----|---|---|---|
| **EC-01 Concurrency / Race** | Partial (TC-PD-101 OptLock TVV; TC-TCPD-104 OptLock TC TV) | (a) 2 CB NV cùng tạo TVV CCCD trùng → unique constraint catch race | File 01 §E |
| | | (b) NHT update song song CB NV thẩm định → who-wins | File 04 §E |
| | | (c) Concurrent công khai + vô hiệu hóa → vô hiệu hóa precedence | File 08 §E |
| | | (d) Concurrent SM-TCTV transition (Tạm dừng vs Vô hiệu hóa) | File 12 §E |
| **EC-02 Unicode / Boundary** | Limited | (e) Họ tên Unicode + emoji `Nguyễn Văn 🇻🇳` → save OK render đúng | File 01 §E |
| | | (f) Mã TC TV with diacritics `TC-TW-Hà-Nội-001` → escape OK | File 11 §E |
| **EC-03 Whitespace / Sanitize** | Partial (XSS TC-NL-010, TC-DG-005) | (g) CCCD whitespace `  001234567890  ` → trim trước validate | File 01 §E |
| | | (h) Email leading whitespace `  a@b.com` → trim | File 01 §E + File 03 §E |
| | | (i) Mô tả công khai chứa `javascript:` URI → strip | File 08 §E |
| | | (j) so_quyet_dinh chứa SQL injection `'; DROP TABLE--` → sanitize | File 07 §E |
| **EC-04 Soft-delete / Restore** | Partial (TC-TVV-301) | (k) Tìm kiếm có hiển thị soft-deleted record (filter "Đã xóa") | File 02 §E |
| | | (l) Restore TVV soft-deleted (admin only?) | File 01 §E |
| **EC-05 SQL injection / XSS** | Partial | (m) Tìm kiếm SQL injection `'; DROP TABLE` → sanitize PASS | File 02 §E |
| **EC-06 Pagination boundary** | Partial (BR-DATA-07) | (n) Page=0 / Page=very-large → reject hoặc default page=1 | File 02 §E |
| | | (o) Sort secondary tie-breaker (cùng created_at) | File 02 §E |
| **EC-07 Date boundary / Timezone** | None | (p) Ngày công nhận filter UTC+7 vs UTC — boundary 2026-05-08 23:59 vs 2026-05-09 00:00 | File 02 §E |
| | | (q) tu_ngay > den_ngay reversed → reject hoặc swap | File 02 §E + File 05 §E |
| | | (r) Leap year ngày sinh 29/02/2024 → save OK | File 01 §E |
| **EC-08 Session timeout** | None | (s) Session expired khi đang submit form → re-auth + restore data | File 14 §E |
| | | (t) Permission change real-time (admin thay đổi vai trò user đang login) → next request 403 | File 14 §E |
| **EC-09 File upload edge** | Partial (size + virus + count) | (u) File 0-byte → reject với SPEC-CLARIFY-CGTVV | File 01 §E + File 03 §E |
| | | (v) File extension mismatch (.pdf rename .exe) → reject (ClamAV + magic bytes) | File 03 §E |
| **EC-10 API retry / Network** | Partial (BR-PUBLIC-03 TC-CK-006) | (w) API Cổng timeout 30s → retry queue verify (BR-PUBLIC-03) | File 08 §E |
| | | (x) Mail server fail giữa batch approve → partial result UI MD-CONG-KHAI-PARTIAL-FAIL | File 07 §E |
| **EC-11 Round-half-up edge** | Partial (TC-CROSS-001) | (y) Round-half-up tie 4.45→4.5 / 4.55→4.6 / 4.65→4.7 (3 case) | File 09 §E |
| | | (z) AVG khi mới có 1 đánh giá → diem_tb = exact value (no round) | File 09 §E |
| **EC-12 Cross-tenant IDOR** | Partial (TC-PERM-004) | (aa) IDOR API trực tiếp KHÔNG qua UI: PUT /tu-van-vien/{id} → 403 + audit | File 14 §E |
| | | (bb) IDOR field-level (sửa don_vi_id của hồ sơ chính mình) → backend reject | File 11 §E |
| **EC-13 Mass action edge** | Partial | (cc) Batch approve 50 record (max?) | File 07 §E |
| | | (dd) Batch công khai mixed states (mostly HOAT_DONG + 1 TAM_DUNG) → partial fail report | File 08 §E |
| **EC-14 Optimistic lock + Version** | Done (TC-PD-101, TC-TCPD-104) | (ee) Reload sau OptLock conflict → version refresh OK retry | File 07 §E |
| **EC-15 SM-TVV CHO_KICH_HOAT special** | Partial | (ff) TVV CHO_KICH_HOAT bấm link nhưng token expired → request resend qua FR-VIII-26 Quên MK | File 07 §E |
| | | (gg) TVV CHO_KICH_HOAT bị vô hiệu hóa trước khi kích hoạt → SM jump TU_CHOI hay VO_HIEU_HOA? SPEC-CLARIFY | File 10 §E |
| **EC-16 NHT edge** | Partial | (hh) NHT email trùng TVV email → reject hay allow? (cross-entity unique) | File 13 §E |
| | | (ii) NHT bị vô hiệu hóa giữa khi đang đăng ký TVV (form đang mở) → block submit | File 13 §E |
| **EC-17 Phụ lục BTP edge** | Partial (TC-TIMKIEM-201) | (jj) Export PL1 với 0 record → file Excel có header but 0 row | File 02 §E |
| | | (kk) Export PL2 khi TC TV chưa có Số ĐKHĐ (data legacy) → cell trống vẫn export | File 11 §E |

**Tổng đề xuất:** 37 edge case mới (jj+kk merge → 35 individual)

---

## Inline merge mapping (BẮT BUỘC ÁP DỤNG VÀO FILE UC)

Các edge sẽ được Edit inline vào Section `## E. Edge bổ sung` của file UC tương ứng (đánh dấu `EDGE-A4-{NN}`):

- **File 01**: a, e, g, h, k, l, r → 7 edge
- **File 02**: m, k, n, o, p, q, jj → 7 edge
- **File 03**: b (auto-trigger race), h, u, v → 4 edge
- **File 04**: b → 1 edge
- **File 05**: q → 1 edge
- **File 06**: (covered) → 0
- **File 07**: cc, dd, ee, ff, j, x → 6 edge
- **File 08**: c, w, dd, i → 4 edge
- **File 09**: y, z → 2 edge
- **File 10**: gg → 1 edge
- **File 11**: f, bb, kk → 3 edge
- **File 12**: d → 1 edge
- **File 13**: hh, ii → 2 edge
- **File 14**: aa, s, t → 3 edge

**Tổng inline merge:** ~42 TC mới (35 unique + 7 duplicate cross-file edge cùng category)

---

**Iron rule reminder:** File này CHỈ là audit log. Phase B chạy từ file UC `01-14-TC-*.md` — KHÔNG ref file 08. Edge mới PHẢI Edit vào file UC trước khi flip Phase A ✅.
