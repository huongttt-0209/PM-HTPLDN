# Test Cases — UC-LOG-02: Xuất Excel Nhật ký (FR-VIII-28 step 6 + AC2)

> **SRS Ref**: FR-VIII-28 step 6 (srs-fr-10:1348), AC2 (srs-fr-10:1371), SCR-VIII-10 nút [Xuất Excel] (srs-fr-10:1816), BR-DATA-06 Phụ lục B (srs-v3.1.md:5331)
> **Ngày tạo**: 2026-05-08 (BMAD A3, A4 inline merge)
> **Tài khoản chính**: `qtht_01`

> **NHATKY-01 RESOLVED 2026-05-08 (theo business spec):** Excel limit = **10.000 dòng** (per FR-VIII-28 step 6 + AC2 + BR-DATA-06 Phụ lục B). SCR-VIII-10 line 1830 ghi 50K **SAI** so với business spec → coi như UI spec chưa update. Test theo 10K. Nếu Phase B phát hiện BE accept 50K → BUG implementation không khớp business.

> **Pre-condition chung:** `qtht_01` đăng nhập, vào SCR-VIII-10. AUDIT_LOG seed đa dạng để cover các filter combination.

---

## A. HAPPY PATH — EXPORT THEO FILTER

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-EXP-001 | FR-VIII-28 AC2 + step 6 (sync SPEC-CLARIFY-NHATKY-07) | Xuất Excel — default filter (7 ngày) | `qtht_01`. AUDIT_LOG có 1.500 bản ghi trong 7 ngày. | (default filter) | 1. Mở SCR-VIII-10. 2. Click [Xuất Excel] toolbar. | **STATE**: BE query đúng filter hiện tại + export `.xlsx`. **AUDIT_LOG INSERT cho EXPORT — defer**: SPEC-CLARIFY-NHATKY-07 — FR-VIII-28 line 1337 (hanh_dong enum) + BR-DATA-05 (line 5330) chỉ define 7 action: CREATE/UPDATE/DELETE/APPROVE/REJECT/LOGIN/LOGOUT. KHÔNG có EXPORT action. Nếu BE có log EXPORT → action enum cần extend; nếu không log → BR-DATA-05 không bị vi phạm. KHÔNG assert EXPORT log Phase A. **UI**: File download `nhat-ky-he-thong-YYYY-MM-DD-HHmmss.xlsx` (hoặc tên tương đương). Toast success "Xuất file thành công" (verify text). **PERSIST**: File chứa 1.500 dòng + header 7 cột. | Happy | P0 |
| TC-NK-EXP-002 | FR-VIII-28 step 6 | Excel header đúng 7 cột + format dd/mm/yyyy HH:mm:ss | `qtht_01`. ≥ 1 bản ghi. | — | 1. Export. 2. Mở file `.xlsx`. | **STATE**: — (verify file). **UI**: Row 1 = header ["Thời gian","Người dùng","Đơn vị","Module","Entity","Mã bản ghi","Loại thao tác","Chi tiết thay đổi"] (8 cột — bao gồm chi_tiet JSON theo SCR-VIII-10 #9). Row 2+ = data. Cột Thời gian định dạng `dd/mm/yyyy HH:mm:ss`. **PERSIST**: — | Happy | P0 |
| TC-NK-EXP-003 | FR-VIII-28 step 6 | Export theo combo filter (4 trường) | `qtht_01`. Filter: tu=today-30, den=today, module="Doanh nghiệp", hanh_dong="Sửa". | — | 1. Set 4 filter (giống TC-NK-107). 2. Click [Xuất Excel]. | **STATE**: BE query EXPORT cùng filter (AND logic). **UI**: File chứa **chỉ** dòng match combo filter (KHÔNG export full DB). **PERSIST**: Verify count file == count UI. | Happy | P0 |
| TC-NK-EXP-004 | ⚠️ SPEC-CLARIFY-NHATKY-07 (EXPORT action chưa có ở SRS) | Audit log của hành động EXPORT — defer pending BA | `qtht_01`. | — | 1. Click [Xuất Excel]. 2. Sau khi download, refresh SCR-VIII-10 + dropdown filter `hanh_dong`. 3. Quan sát có giá trị "EXPORT" / "Xuất Excel" không. | **STATE**: SPEC-CLARIFY-NHATKY-07 — FR-VIII-28 line 1337 + BR-DATA-05 (srs-v3.1.md:5330) liệt kê 7 action enum (CREATE/UPDATE/DELETE/APPROVE/REJECT/LOGIN/LOGOUT). EXPORT không có. **2 behavior hợp lệ:** (a) BE log EXPORT với action mới ngoài enum → spec cần extend; (b) BE không log EXPORT → BR-DATA-05 không vi phạm vì EXPORT không phải CUD/PD/login/logout. **UI**: Verify behavior thực tế Phase B; KHÔNG bug nếu không log; log SPEC-CLARIFY nếu BE thêm action ngoài enum. **PERSIST**: — | Edge | P1 |

---

## B. NEGATIVE — VALIDATION + EMPTY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-EXP-005 | A4 empty result (tightened — codex weak fix) | Export khi 0 bản ghi match filter — verify behavior cụ thể | `qtht_01`. | nguoi_dung=`tvv_99` (không có log) | 1. Filter no-match. 2. Click [Xuất Excel]. | **STATE**: BE detect 0 row. **UI Phase B verify behavior cụ thể (1 trong 2):** (a) Nút [Xuất Excel] **disabled** khi count=0 + tooltip "Không có dữ liệu" → KHÔNG download; (b) Nút active → toast WARNING nguyên văn "Không có dữ liệu để xuất" + KHÔNG download. **Behavior FAIL**: download file rỗng (chỉ header) — UX bug, expected toast warning rõ ràng. Log SPEC-CLARIFY nếu BA muốn behavior khác. **PERSIST**: — | Negative | P1 |
| TC-NK-EXP-006 | ERR-LOG-02 | Export với khoảng > 90 ngày bị block trước khi click Export | `qtht_01`. | tu=today-91, den=today | 1. Set 91 ngày. 2. Click [Xuất Excel] (nếu nút active) hoặc verify nút disabled. | **STATE**: FE/BE validate trước Export. **UI**: WARNING "Khoảng thời gian tối đa là 90 ngày" giống TC-NK-120/136. KHÔNG có file download. KHÔNG INSERT audit-log EXPORT. **PERSIST**: — | Negative | P0 |

---

## C. BOUNDARY — 10.000 DÒNG (BR-DATA-06)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-EXP-007 | BR-DATA-06 boundary (A4 merged) | **Boundary 9.999 dòng — VALID** | `qtht_01`. Seed AUDIT_LOG đúng 9.999 bản ghi trong 90 ngày. | tu=today-90, den=today | 1. Filter 90 ngày. 2. Click [Xuất Excel]. | **STATE**: BE export đầy đủ. **UI**: File 9.999 row data + header. KHÔNG có warning truncate. **PERSIST**: — | Edge | P0 |
| TC-NK-EXP-008 | BR-DATA-06 boundary (A4 merged) | **Boundary chính xác 10.000 dòng — VALID** | `qtht_01`. Seed đúng 10.000 bản ghi. | tu=today-90, den=today | 1. Export. | **STATE**: BE export đầy đủ 10.000. **UI**: File 10.000 row data + header. KHÔNG có warning. **PERSIST**: — | Edge | P0 |
| TC-NK-EXP-009 | BR-DATA-06 over-limit (NHATKY-01 RESOLVED — theo business 10K) | **Over-limit 10.001 dòng — TRUNCATE hoặc REJECT (cứng tại 10K)** | `qtht_01`. Seed 10.001 bản ghi. | tu=today-90, den=today | 1. Export. | **STATE**: BE PHẢI áp limit 10K theo BR-DATA-06 + FR-VIII-28 step 6 + AC2. 2 behavior hợp lệ: (a) BE truncate xuống 10.000 và toast WARNING "Chỉ xuất tối đa 10.000 dòng. Vui lòng thu hẹp bộ lọc."; (b) BE reject với ERROR. **UI**: file đúng ≤10.000 + warning HOẶC KHÔNG file + ERROR. **Nếu BE accept đầy đủ 10.001 → BUG implementation vi phạm BR-DATA-06.** **PERSIST**: — | Edge | P0 |
| TC-NK-EXP-010 | NHATKY-01 RESOLVED (verify limit cứng 10K, không phải 50K) | **Verify limit cứng 10K — KHÔNG được phép vượt** | `qtht_01`. Seed 50.001 bản ghi. | tu=today-90, den=today | 1. Export. 2. Đếm số dòng file `.xlsx` (qua MCP `evaluate_script` parse blob). | **STATE**: BE áp limit 10K (per business spec). **UI**: File chứa ≤ 10.000 dòng (KHÔNG phải 50.000). Toast WARNING/ERROR theo behavior TC-009. **Nếu BE accept 50.000 → BUG: implementation theo SCR-VIII-10 line 1830 (50K) thay vì BR-DATA-06 (10K).** Bug log: "Implementation Excel limit 50K vi phạm BR-DATA-06 Phụ lục B = 10K". **PERSIST**: — | Edge | P0 |

---

## D. PERFORMANCE & SECURITY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|---------------|----------------|-----------|----------|------------------|------|----------|
| TC-NK-EXP-011 | A4 perf (A4 merged) | Export 10.000 dòng — response ≤ 30s | `qtht_01`. 10.000 bản ghi. | — | 1. Click [Xuất Excel]. 2. Đo thời gian từ click → file download. | **STATE**: BE async hoặc sync response ≤ 30s. **UI**: Loading spinner xuất hiện. KHÔNG block UI. Sau ≤ 30s → file download. **PERSIST**: Verify `list_network_requests` thấy POST/GET `/api/audit-log/export` status=200. | Edge | P1 |
| TC-NK-EXP-012 | A4 download URL security (A4 merged) | URL download file Excel — không phải public | `qtht_01`. Sau export. | — | 1. Lấy URL file (nếu là URL). 2. Logout `qtht_01`. 3. Login bằng `cb_nv_tw_01` (không phải QTHT). 4. Paste URL. | **STATE**: BE verify JWT/role trước khi serve file. **UI**: 403 hoặc redirect. **PERSIST**: File KHÔNG được tải. (Nếu là blob streaming trực tiếp — không có URL — TC bypass; ghi note vào execution report.) | Negative | P1 |

---

## Tổng số TC: 12 (4 Happy + 2 Negative + 4 Boundary + 2 Performance/Security) — A3 base 8 + A4 merged 4
**Priority**: P0=6 / P1=6 / P2=0

**Coverage:**
- BR: BR-DATA-05 (audit log của EXPORT — TC004), BR-DATA-06 (10K boundary — TC007-009)
- AC SRS: AC2 ✅ (TC001, 002, 003)
- Error codes: ERR-LOG-02 reuse (TC006)
- A4 merged 2026-05-08: TC005-012 (empty, boundary 9999/10K/10001/50001, perf, download security)
- SPEC-CLARIFY: NHATKY-01 (10K vs 50K — TC009, TC010 sẽ rõ ở Phase B)
