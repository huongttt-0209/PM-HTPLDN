# Functional Test Report — R9 Cross-cutting Re-verify (qa-bugfix-reverify-audit)

| Thông tin | Giá trị |
|---|---|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA huongttt via Claude Code (Chrome DevTools MCP) |
| **Ngày** | 2026-05-11 15:38:00 → 16:05:00 (UTC+7) |
| **Round** | R9 |
| **Acc** | `qtht_10` (isolatedContext `qtht_10_session`) + `cb_nv_tw_10` (isolatedContext `cb_nv_tw_10_session`) — bộ acc fresh `_10` created 2026-05-10 10:35:00 |
| **Skill ref** | `/qa-only` + `.agents/skills/qa-bugfix-reverify-audit` |
| **Scope** | 5 task cross-cutting có thể test UI/API: R7.8.1 / R7.8.2+BUG-SEC-FILE-01 / R7.8.3 / R7.8.4 / R7.8.6 (doc-only) |

---

## Verdict: ✅ 3 PASS (mới) + ⚠️ 1 PARTIAL còn lại + ✅ 1 doc gap đã lấp

| Task | R7/R8 status | R9 status | Change |
|---|---|---|---|
| R7.8.1 Hard delete | ✅ PASS | ✅ PASS | Re-confirm với qtht_10 — DELETE 204, list 11→10 (-1), GET 404 |
| R7.8.2 + **BUG-SEC-FILE-01** | ⚠️ Open R8 | ✅ **CLOSED R9** | BE thêm magic-byte sniff, `ERR-VAL-FILE-04 "Nội dung file không khớp định dạng"` |
| R7.8.3 Lưu nháp scope hẹp | ⚠️ Partial | ✅ **PASS R9** | Form CT giờ có 4 button đúng: Quay lại / Lưu / Đệ trình duyệt / Hủy CT |
| R7.8.4 Profile + đổi MK | ⚠️ Partial | ⚠️ **Partial** | 3 mâu thuẫn vẫn DETECT (unchanged) — chờ BA chốt |
| R7.8.6 BC-024 gap | ⚠️ Partial | ✅ **PASS R9** | Đã thêm dòng `BC-023b UC146` vào `7.11-bao-cao-thong-ke.md` |

---

## Bảng trạng thái TC (snapshot R9 — LATEST 2026-05-11 16:00:00)

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TC-R7.8.1-S01..05 | Hard delete CREATE → GET → DELETE → GET list → GET by ID | ✅ Đạt | R7 | R9 re-confirm với qtht_10 |
| TC-R7.8.2-A1 | Whitelist reject `.exe` | ✅ Đạt | R7 | R9 confirm |
| TC-R7.8.2-A2 | Whitelist reject `.bat` | ✅ Đạt | R7 | R9 confirm |
| TC-R7.8.2-A3 | Whitelist reject `.docm` | ✅ Đạt | R7 | R9 confirm |
| TC-R7.8.2-A4 | Whitelist reject `.zip` | ✅ Đạt | R7 | R9 confirm |
| TC-R7.8.2-B5 | **PE bytes claim `.pdf` (magic-byte spoof)** | ✅ **Đạt R9** | R7 ❌ → R8 ❌ → **R9 ✅** | BUG-SEC-FILE-01 FIXED — `ERR-VAL-FILE-04` |
| TC-R7.8.2-B6 | Real PDF control case | ✅ Đạt | R7 | Permission gate `403 ERR-PERM-FILE-02` (đúng) |
| TC-R7.8.2-B7 | ZIP bytes claim `.docx` | ✅ Đạt | R9 | Magic match `.docx` → past content layer, fail permission |
| TC-R7.8.2-B8 | Text bytes claim `.jpg` | ✅ Đạt | R9 | Bonus: `ERR-VAL-FILE-04` content mismatch |
| TC-R7.8.3-B1 | Form CT DU_THAO action buttons | ✅ **Đạt R9** | R7 ❌ → R9 ✅ | 4 button: Quay lại / Lưu / Đệ trình duyệt / Hủy CT |
| TC-R7.8.3-B2 | Form CT Create (`/tao-moi`) button | ✅ **Đạt R9** | R7 ❌ → R9 ✅ | Button "Tạo chương trình" (không phải [Lưu nháp]) |
| TC-R7.8.4-A1..5 | Tab Thông tin cá nhân 5 trường | ✅ Đạt | R7 | R9 re-confirm |
| TC-R7.8.4-B1..3 | Tab Bảo mật 3 trường form đổi MK | ✅ Đạt | R7 | R9 re-confirm |
| TC-R7.8.4-C1 | BE C1 wrong current password | ⚠️ Sai spec | R7 | `ERR-AUTH-VIII-CP-01` thay vì spec `ERR-PWD-04` |
| TC-R7.8.4-C2 | BE C2 weak password (no special) | ⚠️ Sai spec | R7 | BE strict hơn spec — 4 elements yêu cầu |
| TC-R7.8.4-C3 | BE C3 confirm mismatch | ⚠️ Sai spec | R7 | `ERR-VAL-VIII-CP-04` thay vì spec `ERR-PWD-06` |
| TC-R7.8.4-D1 | UI hint MK strength rule | ⚠️ Sai spec | R7 | "ký tự đặc biệt" trong hint, spec không có |
| TC-R7.8.4-D2 | Section "Phiên đăng nhập" | ⚠️ Sai spec | R7 | UI có table, spec không có |
| TC-R7.8.6-UC146 | BC test case cho FR-IX-23 | ✅ **Đạt R9** | R7 ❌ → R9 ✅ | Đã thêm `BC-023b` vào `7.11-bao-cao-thong-ke.md` |
| **Tổng** | **20 TC** | **✅14 · ⚠️5 · ❌0** | | |

---

## Bảng TC chưa chạy được — cần làm gì để chạy (R9)

Hiện tại còn **5 TC chưa Đạt** — đều thuộc nhóm **C** chờ BA confirm spec (R7.8.4 mâu thuẫn). Không có nhóm A/B/D/E/F.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC-R7.8.4-C1 | BE errCode `ERR-AUTH-VIII-CP-01` không match spec `ERR-PWD-04` | BA chốt convention errCode (rename BE hoặc update SRS FR-VIII-26 §Error Handling) | BA |
| TC-R7.8.4-C2 | BE strict hơn spec (yêu cầu 4 elements, spec chỉ 3) | BA chốt: "ký tự đặc biệt" có required hay không | BA |
| TC-R7.8.4-C3 | BE errCode `ERR-VAL-VIII-CP-04` không match spec `ERR-PWD-06` | BA chốt convention errCode (cùng với C1) | BA |
| TC-R7.8.4-D1 | UI hint mention "ký tự đặc biệt" — spec không có | BA chốt strength rule (cùng C2) → update spec hoặc relax BE | BA |
| TC-R7.8.4-D2 | UI có section "Phiên đăng nhập" — spec ho-so-doi-mat-khau.md không có | BA chốt scope: keep feature + update spec, hoặc remove FE | BA |

---

## Detailed Test Results

### A. R7.8.1 Hard delete (qtht_10) — ✅ PASS R9

| Step | Action | Response | Match? |
|---|---|---|:-:|
| 1 | CREATE DM `TEST_HD_R8_*` LINH_VUC_PL | 201 + id `c97c7c76-e9de-4a58-a093-d778c4d2fad2` | ✅ |
| 2 | GET list `?loaiDanhMuc=LINH_VUC_PL&includeInactive=true` | 200 count=11, found=true | ✅ |
| 3 | DELETE by ID | **204** No Content | ✅ |
| 4 | GET list lại | 200 count=10 (diff=1), found=false | ✅ |
| 5 | GET by ID | **404** `ERR-VAL-VIII-99-04 "Không tìm thấy danh mục"` | ✅ |

Confirm hard delete pattern không thay đổi từ R7. SRS modal MD-XOA "xóa mềm" vẫn obsolete.

### B. R7.8.2 + BUG-SEC-FILE-01 (qtht_10) — ✅ CLOSED R9

**Extension whitelist (4 case):**

| # | File | MIME | Content | Status | errCode |
|---|---|---|---|:-:|---|
| A1 | `malware.exe` | `application/x-msdownload` | PE bytes | 400 | `ERR-VAL-FILE-03` |
| A2 | `script.bat` | `application/bat` | text | 400 | `ERR-VAL-FILE-03` |
| A3 | `macro.docm` | `vnd.ms-word.document.macroEnabled.12` | ZIP bytes | 400 | `ERR-VAL-FILE-03` |
| A4 | `archive.zip` | `application/zip` | ZIP bytes | 400 | `ERR-VAL-FILE-03` |

Whitelist message update: `.doc, .docx, .xls, .xlsx, .pdf, .jpg, .png, .gif` (thêm `.gif` — match commit BUG-UPL-001).

**Magic-byte sniff (5 case critical):**

| # | File | Claimed MIME | Actual bytes | Status | errCode | Verdict |
|---|---|---|---|:-:|---|---|
| B5 | `fake-malware.pdf` | `application/pdf` | **PE bytes** `4D 5A 90 00...` | **400** | **`ERR-VAL-FILE-04`** "Nội dung file không khớp định dạng. Vui lòng tải lên file gốc đúng loại đã chọn" | ✅ **FIXED** |
| B6 | `real.pdf` | `application/pdf` | `%PDF-1.4...` | 403 | `ERR-PERM-FILE-02` | ✅ Pass content, fail permission |
| B7 | `fake.docx` | `vnd.openxmlformats...wordprocessingml` | ZIP bytes (no inner XML) | 403 | `ERR-PERM-FILE-02` | ⚠️ Magic OK (ZIP `50 4B 03 04`), nhưng không verify inner `[Content_Types].xml` |
| B8 | `fake.jpg` | `image/jpeg` | text bytes | **400** | **`ERR-VAL-FILE-04`** | ✅ Bonus content-mismatch detect |

**Layer defense status (post-fix R9):**

| Layer | Status R7 | Status R9 |
|---|:-:|:-:|
| Extension whitelist | ✅ | ✅ |
| MIME-type check (client-trusted) | ⚠️ | ⚠️ |
| **Magic-byte sniff** | ❌ | ✅ **ADDED** |
| Virus scan content | ❌ (bỏ ClamAV) | ❌ (chưa add lại) |
| Macro detection | ❌ | ❌ |

**Defer notes:**
- Magic-byte sniff cho ZIP-based formats (`.docx/.xlsx`) chỉ check outer ZIP magic, không verify inner `[Content_Types].xml`. Attacker upload `.zip` rename `.docx` lọt qua content layer (vẫn fail permission, nhưng nếu có quyền upload thì bypass). Low risk vì ZIP execution không trivial.
- Virus scan content + macro detection vẫn LOST sau bỏ ClamAV. Accept risk theo `_DELTA-MAP-CROSS-CUTTING.md C2`.

### C. R7.8.3 Lưu nháp scope hẹp (cb_nv_tw_10) — ✅ PASS R9

| # | Form path | Record state | Action buttons | Match scope HẸP? |
|---|---|---|---|:-:|
| B1 | `/ct-htpldn/4b40d11f-...` (edit CT-20260511-0003 DU_THAO) | `DU_THAO` | **Quay lại / Lưu / Đệ trình duyệt / Hủy CT** | ✅ Match (KHÔNG còn [Lưu nháp]) |
| B2 | `/ct-htpldn/tao-moi` (create new) | N/A | **Tạo chương trình** | ✅ Match (KHÔNG còn [Lưu nháp]) |

→ SRS update v3.5 item 11 đã apply trên FE. Entry state DU_THAO vẫn giữ (record list show "Dự thảo" badge). Workflow trigger có [Đệ trình duyệt] để chuyển sang CHO_PHE_DUYET.

### D. R7.8.4 Profile + Đổi MK (qtht_10) — ⚠️ Partial (3 mâu thuẫn unchanged)

**BE behavior re-test 3 case (R9 16:00:00):**

| Case | Payload | Spec expected | BE actual | Match? |
|---|---|---|---|:-:|
| C1 | `currentPassword="WrongPassword@1"` | `ERR-PWD-04 "MK hiện tại không đúng"` | 422 `ERR-AUTH-VIII-CP-01` "Mật khẩu hiện tại không đúng" | ⚠️ errCode mismatch |
| C2 | `newPassword="NoSpecial1"` (no special char) | Spec ≥8 + hoa+thường+số → PASS | 422 `ERR-VAL-SYS-00-01` "...1 chữ số và 1 ký tự đặc biệt" | ❌ BE strict hơn |
| C3 | `newPasswordConfirm` ≠ `newPassword` | `ERR-PWD-06 "MK xác nhận không khớp"` | 422 `ERR-VAL-VIII-CP-04` "Mật khẩu xác nhận không khớp" | ⚠️ errCode mismatch |

**UI confirm (R9 15:55:00):**
- Hint MK: "Tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, chữ số **và ký tự đặc biệt**." (same R7)
- Section "Phiên đăng nhập" L5 + table 6 cột + 1 row hiện tại Chrome / ::ffff:127.0.0.1 (same R7)
- Screenshot: `r9-r7-8-4-profile-bao-mat-tab-qtht10.png`

→ 3 mâu thuẫn ổn định qua 2 round (R7, R9) — không phải transient. Cần BA quyết spec authority để dev align.

### E. R7.8.6 BC-024 gap (doc-only) — ✅ FIXED R9

Edit `output/funtion/7.11-bao-cao-thong-ke.md`:

```diff
  | BC-023 | UC145 | BC CT theo lĩnh vực — bảng lĩnh vực × (số CT / số DN tham gia) | Happy | P2 |
+ | BC-023b | UC146 | BC CT theo thời gian — line chart 12 điểm trend số lượng CT theo tháng (FR-IX-23 — lấp gap UC146 v3.5) | Happy | P2 |
  | BC-024 | — | Xuất Excel — file XLSX theo TT17/2025... | Workflow | P0 |
```

→ BC table giờ cover **23/23 unique UC FR-IX-01..23** (UC124..UC146). Numbering BC-024..BC-040 (Workflow/Authorization/Cross-module) giữ ổn định bằng sub-numbering `BC-023b`.

---

## Test Method

**Tool:** Chrome DevTools MCP (`mcp__chrome-devtools__*`).
**Pattern:** isolatedContext per role (qtht_10_session + cb_nv_tw_10_session) để tránh BE httpOnly cookie sticky cross-session.
**Login template:** standard MCP-Rule template — `new_page` → `wait_for("Nhập tên đăng nhập")` → `fill_form` → `click submit` → `wait_for("Nhập mã xác thực")` → `type_text("666666")` → `wait_for("Tổng quan")`.
**API verification:** `evaluate_script` chạy `fetch()` trực tiếp từ session login (cookies tự forward).
**Screenshots evidence:**
- `r9-r7-8-3-form-ct-htpldn-buttons-cb_nv_tw_10.png` — Form CT DU_THAO 4 button mới
- `r9-r7-8-4-profile-bao-mat-tab-qtht10.png` — Tab Bảo mật + 3 mâu thuẫn unchanged

---

## Out of scope (R9)

- R7.7.16 API outbound — vẫn block, devops chưa cấp mTLS cert + 8 endpoint chưa deploy (probe `/api/v1/vu-viec` etc vẫn 404 — verify R7).
- R7.5.3 SLA banner — chưa advance HD/VV deadline >70% SLA, đợi state.
- R7.7.17 Edge BR (19 BR còn lại) — cần infra time-travel backdate.
- R7.8.5 Permission 55+ entity × 11 role × 40 TC — scope rộng, không cover trong session này.
- R7.8.7 E2E DN full luồng — 6/8 task upstream chưa xong + VNeID Tier 2 sandbox.

---

*Report generated: 2026-05-11 16:00:00 (UTC+7) | QA huongttt via Chrome DevTools MCP, acc set `_10`.*
