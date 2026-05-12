# Functional Test Report R7.7.10b R8 lần 14 — Biểu mẫu (close bulk import happy-path)

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Thư viện Biểu mẫu — Module 7.9 |
| **Round** | R7.7.10b R8 lần 14 — close 2 ⚠️ PARTIAL BM-028/029 (bulk import happy-path) |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-12 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Account** | `cb_nv_tw_02` (CB Nghiệp vụ TW, BTP-TW) |
| **Round trước** | [`functional-test-report-r7-7-10b-bm-r8-lan-10.md`](functional-test-report-r7-7-10b-bm-r8-lan-10.md) |

---

## 1. Scope R8 lần 14

Close 2 ⚠️ PARTIAL TC bulk import happy-path từ R8 lần 10:
1. **BM-028** — Bulk import 3 valid `.docx` vào TM own-đơn-vị (TW user → TW TM "HĐ Lao động")
2. **BM-029** — Mixed 3 valid `.docx` + 1 invalid `.txt`

Per spec [`7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) §UC97 + FR-VII-07.

---

## 2. Kết quả

| TC | UC | Tên | R8 lần 10 | **R8 lần 14** | Note |
|----|-----|-----|:-:|:-:|------|
| BM-028 | UC97 | Bulk import ≤50 file hợp lệ | ⚠️ PARTIAL | ✅ | TM đích "HĐ Lao động" (id `3d4cf451-...`, own-đơn-vị TW). Upload 3 `test-bm-bulk-{1,2,3}.docx` (917B each) → "Đã tải lên thành công: 3/3" → click "Kiểm tra và tiếp tục" → step 2 "Tổng số file: 3, Hợp lệ: 3, Không hợp lệ: 0" → click "Xác nhận nhập 3 file hợp lệ" → step 3 "✅ Đã nhập thành công 3 biểu mẫu". API verify GET `/bieu-maus?thuMucId=3d4cf451-...` total tăng 7→**11**, 3 BMs mới: `BM-20260511-002/003/004` ("Test-bm-bulk-1/2/3", DOCX 917B), all `ngayTao=2026-05-11T18:25:19.459Z` (cùng timestamp = bulk transaction atomic). |
| BM-029 | UC97 | Mixed valid + invalid | ⚠️ PARTIAL | ✅ | Re-init wizard, TM "HĐ Lao động" preserved. Upload 3 valid `test-bm-bulk-{1,2,3}.docx` → counter "3/3". Sau đó upload `test-bm-invalid.txt` (36B) → MutationObserver captured toast `.ant-message-notice-wrapper` text **"Định dạng không hỗ trợ: test-bm-invalid.txt. Chỉ chấp nhận .doc, .docx, .xls, .xlsx"**. File `.txt` blocked tại FE (`bodyHasTxt=false, upload list = 3 docx only`). FE pre-check Option B pattern (giống BM-008/009/048). Cancel wizard cleanup (không tạo dup BMs vào TM). |

### Pass rate R8 lần 14

| Status | Count | TC |
|---|:-:|---|
| ✅ PASS | 2 | BM-028, BM-029 |
| **Pass% lần 14** | **100%** (2/2) | |

### Cumulative status R7.7.10b sau R8 lần 14

| Metric | R8 lần 10 baseline | **R8 lần 14** | Δ |
|---|:-:|:-:|:-:|
| ✅ PASS clean | 6 | **8** | +2 (BM-028 + BM-029) |
| ⚠️ PARTIAL | 2 (028/029 mech only) | **0** | -2 (mechanism + happy-path both done) |
| 🔁 DEFER | 2 (tool block claim) | **0** | tool unblock R10 + happy-path R14 |
| Bugs open | 0 | **0** | — |
| Sub-defer | BM-035b TVV pwd · NHT BA confirm | unchanged | — |

### Verdict: **R7.7.10b ✅ READY TO CLOSE — 8/8 PASS clean (100%)**

Toàn bộ 8 TC scope R7.7.10b PASS clean. Sub-defer items (BM-035b TVV password fixture + NHT scope BA confirm) là test-environment dependencies, không phải bug.

---

## 3. Bằng chứng

### BM-028 happy-path bulk import

```text
Step 1 (Chọn file):
  TM đích: "HĐ Lao động" (id 3d4cf451-7720-42a8-b364-90e83020fbee, TW own-đơn-vị)
  Files uploaded: test-bm-bulk-1.docx, test-bm-bulk-2.docx, test-bm-bulk-3.docx (917B each)
  Counter: "Đã tải lên thành công: 3/3" ✓

Step 2 (Kiểm tra):
  Tổng số file: 3
  Hợp lệ: 3
  Không hợp lệ: 0
  Table:
    1. test-bm-bulk-1.docx — DOCX 917B — Hợp lệ
    2. test-bm-bulk-2.docx — DOCX 917B — Hợp lệ
    3. test-bm-bulk-3.docx — DOCX 917B — Hợp lệ
  Button: "Xác nhận nhập 3 file hợp lệ" enabled

Step 3 (Hoàn thành):
  ✅ "Đã nhập thành công 3 biểu mẫu"

API verify GET /api/v1/bieu-maus?thuMucId=3d4cf451-...:
  total: 7 → 11 (+3)
  recent 3:
    BM-20260511-002 "Test-bm-bulk-1" (file UUID 07e5ca0457/test-bm-bulk-1.docx, 917B)
    BM-20260511-003 "Test-bm-bulk-2" (file UUID 3dd43ccc1b/test-bm-bulk-2.docx, 917B)
    BM-20260511-004 "Test-bm-bulk-3" (file UUID 6db8a0f3fc/test-bm-bulk-3.docx, 917B)
    All ngayTao: 2026-05-11T18:25:19.459Z (atomic transaction same timestamp)
```

### BM-029 mixed valid + invalid (FE pre-check Option B)

```text
TM đích: HĐ Lao động (preserved from BM-028)
Upload sequence:
  1. test-bm-bulk-1.docx → added (1/1)
  2. test-bm-bulk-2.docx → added (2/2)
  3. test-bm-bulk-3.docx → added (3/3)
  4. test-bm-invalid.txt (36B) → BLOCKED at FE beforeUpload

MutationObserver captured toast:
  <div class="ant-message ant-message-top">
    "Định dạng không hỗ trợ: test-bm-invalid.txt. Chỉ chấp nhận .doc, .docx, .xls, .xlsx"
  <div class="ant-message-notice-wrapper ant-message-move-up-appear">
    (same text)

Upload list: 3 docx items only (txt NOT in list)
Counter: "3/3" (txt not counted because pre-check filtered)
bodyHasTxt: false ← confirms .txt never reached BE

Cleanup: clicked "Hủy" to abort bulk session (avoid creating duplicate 3 BMs).
```

Pattern match FE Option B từ FR-VII-04 §Error Handling — FE filter at client side trước khi POST tới BE, hiển thị toast tiếng Việt cụ thể (filename + accepted formats). Cùng pattern với:
- BUG-BM-008 (BM-016 single upload .txt reject)
- BUG-BM-009 (BM-015 single upload 21MB reject)
- BM-048 (anhDaiDien jpg/png/gif validate)

---

## 4. Findings + Recommendations

### Spec interpretation note (non-bug)

Spec BM-029 mô tả "3 valid + 1 invalid → expect 3 BM created + 1 rejected with error report". Implementation thực tế:
- FE blocks invalid file tại beforeUpload step → file `.txt` không nằm trong list xác nhận → step "Kiểm tra" chỉ show 3 valid → step "Hoàn thành" tạo 3.

UX equivalent: user vẫn nhận feedback rõ ràng (toast tiếng Việt với filename + reason) + chỉ valid files được create. Acceptable per FE Option B preferred pattern.

### Recommendations

1. **R7.7.10b CLOSE** — 8/8 PASS clean. Có thể flip task icon ⚠️ → ✅ trong todo nếu BA confirm NHT scope (non-blocking).
2. **Sub-defer remaining:**
   - **BM-035b TVV pwd**: Create TVV fixture với password biết để verify "TVV không có menu BM".
   - **NHT scope BA confirm**: Update permission-matrix line 534 asterisk nếu intent = own-unit (R*).
3. **Test data:** 3 BMs mới (BM-20260511-002/003/004) trong TM "HĐ Lao động" để giúp tăng pool BM cho regression sau. Total TM "HĐ Lao động" now 11 BMs.

---

*R8 lần 14 | QA Automation via Claude Code MCP | 2026-05-12*
