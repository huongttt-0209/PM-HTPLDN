# Functional Test Report — Biểu mẫu (Module 7.9 v3.5) — R7.7.10 R8 lần 13

| Thông tin | Giá trị |
|-----------|---------|
| **Module** | Thư viện Biểu mẫu — Module 7.9 |
| **Round** | R7.7.10 R8 lần 13 — close 5 ⏳ Pending TC sau BUG-BM-010 closed R8 lần 12 |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-12 |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Account** | `cb_nv_tw_02` (CB Nghiệp vụ TW, BTP-TW) |
| **Round trước** | [`functional-test-report-r7-7-10-bm-r8-lan-8.md`](functional-test-report-r7-7-10-bm-r8-lan-8.md) |

---

## 1. Scope R8 lần 13

Close 5 ⏳ Pending TC còn lại:
1. **BM-010** Sửa BM + upload file mới (was DEFER do BM-007/008 cascade, unblock R8 lần 8)
2. **BM-043** Workflow tắt Switch → clear `thoiGianDangTai` + gỡ Cổng PLQG (unblock R8 lần 12)
3. **BM-045** Reject toggle Switch on AN/HUY → ERR-PUBLIC-01
4. **BM-048** Upload `anhDaiDien` jpg/png/gif ≤5MB validate
5. **BM-049** Upload nhiều `fileDinhKemCongKhai` ≤10 tệp

---

## 2. Kết quả

| TC | UC | Tên | R8 lần 12 | **R8 lần 13** | Note |
|----|-----|-----|:-:|:-:|------|
| BM-010 | UC95 | Sửa BM + upload file mới | ⏳ DEFER | ✅ | Edit BM `01e35f61-...` "Sample-valid" (945B `Sample-valid.docx`) → upload `test-bm-r7-4-c1.docx` (917B) → Save → API GET trả `duongDanFile=.../92a34919-.../test-bm-r7-4-c1.docx, kichThuoc=917`. File replaced thành công (UUID khác). Redirect to detail page. |
| BM-043 | UC95 | Tắt Switch → clear `thoiGianDangTai` + gỡ Cổng | ⏳ Pending | ✅ | Edit BM `daba0030-...` "BM KDTM" (CONG_KHAI, `congKhai=true, thoiGianDangTai=2026-05-10T14:25:11Z`). Form load với Switch `checked`. Toggle Switch OFF → click "Lưu thay đổi" → API GET sau save: `congKhai: true → false, thoiGianDangTai: filled → null, syncStatus: SUCCESS`. **BR-PUBLIC-02 enforced** (clear timestamp + API gỡ Cổng PLQG đã gọi). |
| **BM-045** | UC95 | Reject toggle Switch on AN/HUY → ERR-PUBLIC-01 | ⏳ Pending | ⚠️ PARTIAL | Edit BM `ebeac9ac-...` "BM Lao động" trạng thái **AN**. Toggle Switch OFF→ON → click "Lưu thay đổi" → toast "Cập nhật biểu mẫu thành công" ✅ (200 success). API GET sau save: `trangThai=AN, congKhai=true, thoiGianDangTai=2026-05-11T17:59:35Z`. **BE accept toggle Switch ON cho BM AN state** — KHÔNG reject 422 ERR-PUBLIC-01 như test plan BM-045 mô tả. **Spec contradiction:** BR-PUBLIC-01 ([`srs-fr-12-tv-chuyen-sau.md`](../../../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md)) chỉ nói "Hủy/Từ chối (HUY/TU_CHOI) KHÔNG được công khai" — không nhắc AN; nhưng test plan BM-045 ([`7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) line 126) lại ghi "AN/HUY → reject". Cần BA confirm intent. Cleanup: revert Switch OFF + save → state restored. |
| BM-048a | UC95 | Upload `anhDaiDien` invalid format (.pdf) | ⏳ Pending | ✅ | Form Thêm BM, Switch ON → upload `test-bm-image-invalid.pdf` (181B fake PDF) → MutationObserver captured toast `.ant-message-notice-wrapper` text **"test-bm-image-invalid.pdf: Định dạng không được hỗ trợ. Chấp nhận: .jpg, .png, .gif"**. File NOT added to list. |
| BM-048b | UC95 | Upload `anhDaiDien` 6MB jpg (>5MB) | ⏳ Pending | ✅ | Upload `test-bm-image-6mb.jpg` (6291478 bytes, ~6MB) → toast **"test-bm-image-6mb.jpg: Kích thước vượt quá giới hạn 5MB."** File NOT added. FE pre-check enforce ≤5MB. |
| BM-048c | UC95 | Upload `anhDaiDien` valid 1KB jpg | ⏳ Pending | ✅ | Upload `test-bm-image-valid.jpg` (1022 bytes) → KHÔNG có toast lỗi + file ADDED vào upload list. Valid jpg accepted. |
| BM-049 | UC95 | Upload multi-file `fileDinhKemCongKhai` | ⏳ Pending | ✅ | Form Thêm BM, Switch ON → upload `test-bm-r7-4-c1.docx` + `test-bm-image-valid.jpg` cùng field → both files visible trong upload list (count=2 in `.ant-upload-list-item` selector). Multi-file mixed format support (docx + jpg) OK per spec FR-VII-04 list 8 formats. |

### Pass rate R8 lần 13 (7 sub-TC chạy = 5 main TC)

| Status | Count | TC |
|---|:-:|---|
| ✅ PASS | 4 main | BM-010, BM-043, BM-048 (3 sub), BM-049 |
| ⚠️ PARTIAL | 1 main | BM-045 (spec contradiction BA confirm) |
| **Pass% lần 13** | **80%** PASS only (4/5) · **100%** PASS+PARTIAL (5/5) — 0 FAIL | |

### Cumulative status sau R8 lần 13

| Metric | R8 lần 12 baseline | R8 lần 13 today | Δ |
|---|:-:|:-:|:-:|
| ✅ PASS | 32 (68%) | **36 (77%)** | +4 |
| ⚠️ PARTIAL | 5 | **6** | +1 (BM-045) |
| ❌ FAIL | 0 | **0** | — |
| ⏳ Pending | 5 | **0** | -5 (all closed) |
| ⏭ DEFER | 5 | **5** | — (BM-028/029 mechanism unblock R8 lần 10 nhưng happy-path defer; BM-036/038 out-of-CMS) |
| Bugs open | 0 | **0** | — |

### Verdict: **R7.7.10 — 0 ⏳ Pending còn lại, 36/47 PASS clean, 6 PARTIAL với clear documentation, 0 bug open**

Module BM v3.5 hoàn tất regression cho R7.7.10 scope chính. PARTIAL items:
- BM-015 (TCP reset edge case observation)
- BM-018/019/021 (English error msg leak — observation, không phải bug)
- BM-035 (NHT scope sub-observation + TVV pwd defer)
- BM-045 (spec ambiguity BR-PUBLIC-01 vs BM-045 wording — BA confirm)

DEFER items:
- BM-028/029 (bulk import happy-path — mechanism unblock R8 lần 10, cần own-đơn-vị TM template)
- BM-036 (DN portal out-of-CMS scope)
- BM-038 (Postman mTLS out-of-MCP scope)

---

## 3. Bằng chứng

### BM-010 file replacement

```text
Before: GET /bieu-maus/01e35f61-... → duongDanFile=".../Sample-valid.docx", kichThuoc=945
Action: form Sửa → upload test-bm-r7-4-c1.docx (917B) → Lưu thay đổi → redirect /bieu-mau/{id}
After:  GET /bieu-maus/01e35f61-... → duongDanFile="00000000-0000-4000-8000-000000000001/2026/05/92a34919-4b20-4f82-9756-b82c24f45b48/test-bm-r7-4-c1.docx", kichThuoc=917
```

### BM-043 BR-PUBLIC-02 enforce

```text
Before: GET /bieu-maus/daba0030-... (BM KDTM)
  { trangThai: "CONG_KHAI", congKhai: true, thoiGianDangTai: "2026-05-10T14:25:11.760Z" }
Action: edit form → toggle Switch OFF → Lưu thay đổi
After:  GET /bieu-maus/daba0030-...
  { trangThai: "CONG_KHAI", congKhai: false, thoiGianDangTai: null, syncStatus: "SUCCESS" }
```

### BM-045 spec ambiguity finding

```text
Before: GET /bieu-maus/ebeac9ac-... (BM Lao động AN state)
  { trangThai: "AN", congKhai: false, thoiGianDangTai: null }
Action: edit form → toggle Switch OFF→ON → Lưu thay đổi
After:  toast "Cập nhật biểu mẫu thành công" ✓ (200 success)
        GET /bieu-maus/ebeac9ac-...
        { trangThai: "AN", congKhai: true, thoiGianDangTai: "2026-05-11T17:59:35.574Z" }

Spec quotes:
  BR-PUBLIC-01 (srs-fr-12-tv-chuyen-sau.md): "Bản ghi Hủy/Từ chối KHÔNG được công khai (BM-042, BM-045)"
    → mentions HUY/TU_CHOI only, not AN.
  Test plan BM-045 (7.9-bieu-mau.md line 126): "trang_thai=AN/HUY → bật Switch công khai → reject ERR-PUBLIC-01"
    → mentions AN/HUY both.

→ Spec contradiction. Cleanup: revert Switch OFF + save (state restored to congKhai=false, thoiGianDangTai=null).
```

### BM-048 anhDaiDien validation (3 scenarios via MutationObserver)

```text
(a) Invalid format pdf:
  Upload test-bm-image-invalid.pdf (181B)
  Toast: "test-bm-image-invalid.pdf: Định dạng không được hỗ trợ. Chấp nhận: .jpg, .png, .gif"
  Upload list: empty

(b) >5MB jpg:
  Upload test-bm-image-6mb.jpg (6291478 bytes)
  Toast: "test-bm-image-6mb.jpg: Kích thước vượt quá giới hạn 5MB."
  Upload list: empty

(c) Valid 1KB jpg:
  Upload test-bm-image-valid.jpg (1022 bytes)
  No toast (no error)
  Upload list: ["test-bm-image-valid.jpg"]
```

### BM-049 fileDinhKemCongKhai multi-file

```text
Upload via uid 7_10 (multi-file dropzone):
  1. test-bm-r7-4-c1.docx (917B)
  2. test-bm-image-valid.jpg (1022B)

After upload:
  fileDinhKem_upload_items: ["test-bm-r7-4-c1.docx", "test-bm-image-valid.jpg"]
  Multi-format mix (.docx + .jpg) ✓ accepted per spec FR-VII-04
```

---

## 4. Observations cho BA / dev review

### Spec contradiction BM-045 — cần BA confirm

**Hai source spec mâu thuẫn:**

| Source | Quote | Implication |
|---|---|---|
| BR-PUBLIC-01 (`srs-fr-12-tv-chuyen-sau.md`) | "Bản ghi Hủy/Từ chối KHÔNG được công khai" | Chỉ reject **HUY/TU_CHOI** (terminal states). AN reversible OK. |
| Test plan BM-045 (`7.9-bieu-mau.md` line 126) | "`trang_thai=AN/HUY` → bật Switch công khai → reject `ERR-PUBLIC-01`" | Reject cả **AN và HUY**. |

**Implementation thực tế:** BE accept toggle Switch ON cho BM `trangThai=AN` (giống BR-PUBLIC-01 strict reading) — không enforce test plan BM-045 wording.

**Recommendation:**
- (A) Nếu intent đúng theo BR-PUBLIC-01: update test plan BM-045 thành "trạng thái HUY/TU_CHOI → reject" → AN logic hiện tại đúng → BM-045 thành ✅ PASS partial.
- (B) Nếu intent đúng theo BM-045: update BR-PUBLIC-01 + BE add check `trangThai === 'AN' || trangThai === 'HUY' || trangThai === 'TU_CHOI'` → reject 422 ERR-PUBLIC-01. → Log BUG-BM-011 Major/Critical.

**Hệ luỵ nếu chọn (A):** User có thể toggle Switch ON cho BM AN, BM được publish trên Cổng PLQG dù state AN. Có thể dẫn đến state lệch UI (BM list show "Đã ẩn" nhưng vẫn "Công khai" badge).

---

## 5. Recommended Next Round (R8 lần 14 hoặc R9)

1. **BA confirm BM-045 spec intent** → close PARTIAL hoặc log BUG-BM-011.
2. **BA confirm NHT scope** (perm-matrix line 534 add asterisk nếu own-unit intent).
3. **Real browser test** Playwright cho BM-028/029 happy-path bulk import.
4. **TVV password fixture** → BM-035b.
5. **Postman mTLS** → BM-038.
6. **BM-036 DN portal** out-of-CMS — verify Cổng PLQG public side khi setup subdomain.

---

*R8 lần 13 | QA Automation via Claude Code MCP | 2026-05-12*
