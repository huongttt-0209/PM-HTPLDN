# A7 — Manual Filter UI/Function-Testable (audit log)

> **Method**: Manual review + Edit IN-PLACE | **Date**: 2026-05-10 | **Module**: FR-06 Chi trả
> **Rule**: Edit IN-PLACE file UC tương ứng — loại / sửa TC chỉ test được DB/API thuần. File này CHỈ là audit log action LOẠI/SỬA/GIỮ.

---

## 1. A7 Filter rule

Test phải thực hiện được qua **MCP chrome-devtools** (UI hoặc network request có UI trigger). KHÔNG giữ TC chỉ test được:
- Direct DB SELECT/INSERT/UPDATE
- API thuần JWT/mTLS validation (không có UI hiển thị)
- Cron/scheduled job background không có UI feedback
- Email content verify (không có UI mail viewer)

---

## 2. A7 Action Log

### File 01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-LIST-001..012, TC-CT-TIEP-NHAN-001..003, TC-CT-RUT-001..004 | **GIỮ** | Mọi TC qua UI: DS, filter, click action, modal confirm — chrome-devtools accessible |

### File 02-TC-FR-V.II-03-kiem-tra-HS.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-KT-001..010, 011..015 | **GIỮ** | UI section 3 có UI checkbox + radio + textarea. Force POST API testable qua MCP fetch |

### File 03-TC-FR-V.II-05-danh-gia-tieu-chi.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-DG-001..017 | **GIỮ** | UI section 4 có UI auto-calc readonly fields visible |
| TC-CT-DG-012 (client tampering) | **GIỮ** (sửa Steps cho rõ) | Kiểm thử client-side bypass — DOM tampering qua DevTools console |
| TC-CT-DG-018, TC-CT-DG-019 | **GIỮ** | UI render auto-calc + cột SLA hiển thị |

### File 04-TC-FR-V.II-09-tham-dinh.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-TD-001..009, 010..013 | **GIỮ** | UI section 5 có UI checklist + radio + textarea + nút Lưu |

### File 05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-TRINH-001..003, TC-CT-PD-001..015 | **GIỮ** | UI section 5 (Trình PD) + section 6 (Phê duyệt) có nút + modal confirm |
| TC-CT-PD-013 (race CB PD) | **GIỮ** (note Phase B đa session) | 2 tab/2 user concurrent test qua MCP |

### File 06-TC-FR-V.II-13-cap-nhat-thanh-toan.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-TT-001..012 | **GIỮ** | UI section 7 có UI input + DatePicker + nút |
| TC-CT-TT-006 (Từ chối TT) | **GIỮ với note** | Status SPEC-CLARIFY-CT-01 — nếu UI không có nút thì Phase B mark N/A |

### File 07-TC-FR-V.II-14-DN-bo-sung-HS.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-BS-001..010 | **GIỮ** | UI chuyên trang DN có file upload + form input. Test qua MCP `upload_file` |

### File 08-TC-FR-V.II-08-thong-bao-TVV.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-TB-001..006 | **GIỮ** | Trang Thông báo có UI list + click chi tiết |

### File 09-TC-API-side-effect.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-API-001 | **GIỮ** | Verify side-effect UI sau LGSP push (HS xuất hiện CHO_TIEP_NHAN trên DS) |
| TC-CT-API-002 | **GIỮ** | Verify cột status DVC / cảnh báo retry trên UI |
| TC-CT-API-003 | **GIỮ** | Verify FILE_DINH_KEM xuất hiện trong section UI |
| TC-CT-API-004 | **GIỮ** | Verify in-app TB xuất hiện trên trang Thông báo TVV |
| TC-CT-API-005 (idempotent) | **GIỮ với note Phase B B-Seed** | Cần admin endpoint trigger push 2 lần — note dùng Postman/curl trong B-Seed setup, verify UI HS không bị duplicate |
| TC-CT-API-006 (retry timeout) | **GIỮ với note** | Verify cảnh báo CB NV in-app sau 3 lần retry — Phase B mock LGSP fail (set timeout > 30s × 3) hoặc disable network |
| TC-CT-API-007 (DVC reject 4xx) | **GIỮ với note** | Phase B mock DVC return 403 token expired |
| ❌ ERR-CT-AUTH-01 (JWT invalid) | **LOẠI** | API thuần JWT/mTLS validation — không có UI test (đã LOẠI từ A2) |
| ❌ ERR-CT-01 (thiếu trường) | **LOẠI** | API thuần payload schema validation — không có UI |
| ❌ Email content verify | **LOẠI** | Không có UI mail viewer (chỉ giữ in-app TB ở TC-CT-API-004) |

### File 10-TC-permission-matrix.md

| TC | Action | Reasoning |
|----|--------|-----------|
| TC-CT-PERM-001..018 | **GIỮ** | Mọi TC test qua UI login + force navigate URL hoặc force POST từ DevTools console |

---

## 3. A7 Summary

| Metric | Pre-A7 | Post-A7 | Delta |
|--------|--------|---------|-------|
| Total TC files | 10 | 10 | 0 |
| Total TC | 137 | 137 | 0 |
| TC LOẠI A7 | — | 0 explicit (mọi TC ban đầu đã được lọc qua A2 LOẠI nhánh API thuần — viết trong test plan overview phần ~~LOẠI~~) | 0 |
| TC SỬA A7 | — | 0 (file 09 TC-CT-API-* đã ghi rõ "GIỮ với note Phase B B-Seed mô tả cách trigger") | 0 |
| TC GIỮ A7 | 137 | 137 | — |

**Pre-emption A2:** Đã loại 4 nhánh API thuần ngay từ test plan overview (FR-V.II-01 JWT/mTLS, FR-V.II-04 LGSP outbound auto, FR-V.II-07 DN gửi inbound, FR-V.II-10 email backend). Chỉ giữ side-effect UI trong file 09. Vì vậy A7 không phải xóa thêm TC nào — đã chuẩn UI/function-testable từ A3.

---

## 4. Verification

- [x] Mọi TC trong 10 file UC đều test được qua MCP chrome-devtools (UI flow, force navigate URL, DevTools console fetch, network request inspection)
- [x] 0 TC chỉ-DB thuần (không có TC dùng SQL trực tiếp)
- [x] 0 TC chỉ-API thuần không có UI side-effect verify
- [x] 0 TC sống ở file phụ (08/10/11) — mọi TC đã inline merged vào file UC NN-TC-*.md
- [x] Phase B handoff rule pass — B-block ref được file UC gốc

**Pass A7 acceptance gate** ✅

---

## 5. Total TC sau Phase A (A1..A7)

| File | Base (A3) | Sau A4 | Sau A6 | Final A7 |
|------|-----------|--------|--------|----------|
| 01-TC-FR-V.II-02-quan-ly-HS-de-nghi.md | 13 | 18 | 19 | **19** |
| 02-TC-FR-V.II-03-kiem-tra-HS.md | 10 | 14 | 15 | **15** |
| 03-TC-FR-V.II-05-danh-gia-tieu-chi.md | 12 | 17 | 19 | **19** |
| 04-TC-FR-V.II-09-tham-dinh.md | 9 | 13 | 13 | **13** |
| 05-TC-FR-V.II-11-12-trinh-PD-phe-duyet.md | 13 | 18 | 18 | **18** |
| 06-TC-FR-V.II-13-cap-nhat-thanh-toan.md | 8 | 12 | 12 | **12** |
| 07-TC-FR-V.II-14-DN-bo-sung-HS.md | 6 | 10 | 10 | **10** |
| 08-TC-FR-V.II-08-thong-bao-TVV.md | 4 | 6 | 6 | **6** |
| 09-TC-API-side-effect.md | 4 | 6 | 7 | **7** |
| 10-TC-permission-matrix.md | 14 | 18 | 18 | **18** |
| **Tổng** | **93** | **132** | **137** | **137** |

> Final: **137 TC** sau Phase A complete (A1-A7 + 5 GAP fill A6 + 0 LOẠI A7).
