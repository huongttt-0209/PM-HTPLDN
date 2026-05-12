# R7 Re-verify Evidence — 2026-05-11 23:50:00 (cb_nv_tw_08 + cb_nv_bn_08 + cb_nv_dp_08 + cb_pd_bn_08 + cb_pd_dp_08)

Tool: Chrome DevTools MCP, 5 isolatedContext riêng (`cb_*_08-r7-reverify`). Login UI flow đầy đủ (username + password + OTP 666666). Session JWT ổn định ~5 phút không bị revoke.

## 1. BUG-BC-PDF-NOT-SUPPORTED — VẪN OPEN

POST `/api/v1/bao-cao/export` với `formatXuat: "PDF"` cho 4 BC sample + 2 BC analytic (enum mới):

| BC enum (R7 catalog) | Status | Error message |
|---|:---:|---|
| `BC_HOI_DAP` | 422 | `ERR-RPT-EXPORT-01` "Không thể tạo file PDF. Vui lòng thử lại sau hoặc xuất Excel." |
| `BC_VU_VIEC_HOAN_THANH` | 422 | (same) |
| `BC_CHI_PHI_CHI_TRA` | 422 | (same) |
| `BC_SO_LUONG_CG_TVV` | 422 | (same) |
| `BC_VU_VIEC_THEO_LINH_VUC` | 422 | (same) |
| `BC_DANH_GIA_HIEU_QUA` | 422 | (same) |

**6/6 sample fail universal.** RequestIds: `8c515c72, 18755ebd, 558816d4, c1b0cd4c, 67b7f76d, 58394b45`. Account: `cb_nv_tw_08`. Timestamp: `2026-05-11T16:49:38 → 16:50:07`. Dev chưa wire PDF generator service (puppeteer/wkhtmltopdf).

---

## 2. BUG-BC-XLSX-PARTIAL-SUPPORT — CLOSED (R7 Re-verify PASS)

R6 dùng enum cũ `BC_VV_THEO_LINH_VUC` + `BC_DANH_GIA_HIEU_QUA_HTPL` → 422 "Loại báo cáo không hỗ trợ xuất". R7 verify catalog `/api/v1/bao-cao/loai` thấy enum đã rename:
- `BC_VV_THEO_LINH_VUC` → `BC_VU_VIEC_THEO_LINH_VUC` (UC135)
- `BC_DANH_GIA_HIEU_QUA_HTPL` → `BC_DANH_GIA_HIEU_QUA` (UC132)

POST `/api/v1/bao-cao/export` với enum mới + `formatXuat: "XLSX"`:

| BC enum (R7 mới) | Status | Binary len | content-disposition |
|---|:---:|---:|---|
| `BC_HOI_DAP` (control) | 200 | 6392 | `bao-cao-hoi-dap-2026-05-11.xlsx` |
| `BC_VU_VIEC_THEO_LINH_VUC` | 200 | 6440 | `bao-cao-vu-viec-theo-linh-vuc-2026-05-11.xlsx` |
| `BC_DANH_GIA_HIEU_QUA` | 200 | 6328 | `bao-cao-danh-gia-hieu-qua-2026-05-11.xlsx` |

3/3 PASS với enum đúng. Dev đã (a) rename 2 enum để dài-từ chuẩn hóa, (b) implement template Excel cho 2 BC analytic. R6 fail thực ra là test method dùng enum stale từ R5.

---

## 3. BUG-BC-KYBAOCAO-NOT-VALIDATED — PARTIAL FIX

### 3.1 Validation enum: 12/12 PASS

Test 12 BC sub-route với `kyBaoCao=INVALID`:

| BC | Endpoint | Status | Verdict |
|---|---|:---:|---|
| BC-001 | `/bao-cao/hoi-dap` | **422** | ✅ FIXED (R6 silently 200) |
| BC-002 | `/bao-cao/vu-viec-tiep-nhan` | 422 | ✅ |
| BC-003 | `/bao-cao/vu-viec-dang-ho-tro` | 422 | ✅ |
| BC-004 | `/bao-cao/vu-viec-hoan-thanh` | 422 | ✅ |
| BC-006 | `/bao-cao/lop-dao-tao-dang-dien-ra` | 422 | ✅ |
| BC-007 | `/bao-cao/lop-dao-tao-da-dien-ra` | 422 | ✅ |
| BC-008 | `/bao-cao/chat-luong-dao-tao` | 422 | ✅ |
| BC-009 | `/bao-cao/so-luong-cg-tvv` | 422 | ✅ |
| BC-010 | `/bao-cao/danh-gia-hieu-qua` | **422** | ✅ FIXED (R6 silently 200) |
| BC-015 | `/bao-cao/chi-phi-chi-tra` | 422 | ✅ |
| BC-020 | `/bao-cao/so-luong-ct-ho-tro` | 422 | ✅ |
| BC-021 | `/bao-cao/ct-theo-don-vi` | 422 | ✅ |

Response body chuẩn: `{"code":"ERR-VAL-SYS-00-01","field":"kyBaoCao","message":"kyBaoCao must be one of the following values: TUAN, THANG, QUY, NAM, KHOANG"}`.

### 3.2 Aggregation `theoKy` theo enum: BC-001 vẫn chưa fix

| Enum | `/bao-cao/hoi-dap` `theoKy[0].ky` | `/bao-cao/vu-viec-hoan-thanh` (control) `theoKy[0].ky` |
|---|---|---|
| TUAN | `2026-05` | `2026-05-04` |
| THANG | `2026-05` | `2026-05-01` |
| QUY | `2026-05` | `2026-04-01` |
| NAM | `2026-05` | `2026-01-01` |

→ `/bao-cao/hoi-dap` aggregation flat (key=`YYYY-MM` cho mọi enum). Control BC-004 group đúng theo enum. BC-010 `/danh-gia-hieu-qua` không test được do 0 data.

**Verdict:** Validation phần CLOSED, Aggregation phần OPEN (giảm severity Medium → Minor — tester dùng filter UI sẽ chỉ thấy data summary, không bị crash; chỉ ảnh hưởng accuracy chart "Theo kỳ").

---

## 4. BUG-BC-DATA-SCOPE-LEAK — PARTIAL FIX

GET `/api/v1/bao-cao/*?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` cho 5 role (1 TW baseline + 4 BN/DP):

| Role | account | tongHoiDap | tongVuViec | tongChiPhi | tongTvv |
|---|---|---:|---:|---:|---:|
| CB_NV_TW | cb_nv_tw_08 | 26 | 4 | 209.592.242 | 8 |
| CB_NV_BN | cb_nv_bn_08 (BTC) | **0** ✅ | **0** ✅ | 209.592.242 ❌ | 8 ❌ |
| CB_NV_DP | cb_nv_dp_08 (Sở BG) | **0** ✅ | **0** ✅ | 209.592.242 ❌ | 8 ❌ |
| CB_PD_BN | cb_pd_bn_08 (BTC) | **0** ✅ | **0** ✅ | 209.592.242 ❌ | 8 ❌ |
| CB_PD_DP | cb_pd_dp_08 (Sở BG) | **0** ✅ | **0** ✅ | 209.592.242 ❌ | 8 ❌ |

→ Dev đã wire `dataScopeMiddleware` vào `/bao-cao/hoi-dap` + `/bao-cao/vu-viec-hoan-thanh` (2 endpoint FIXED). 2 endpoint còn lại `/bao-cao/chi-phi-chi-tra` + `/bao-cao/so-luong-cg-tvv` chưa wire → vẫn leak full national identical TW cho 4 role BN/DP.

**Verdict:** Partial fix — 2/4 endpoint sample FIXED, 2/4 vẫn LEAK. Giữ Critical (vi phạm multi-tenant BR-AUTH-08 + BR-DATA-02 vẫn còn). Cần dev wire middleware cho toàn bộ 12+ endpoint `/bao-cao/*` còn lại (chi-phi, cg-tvv, ct-htpldn, vu-viec-dang-ho-tro, vu-viec-tiep-nhan, đào tạo, etc.) — không chỉ 4 endpoint sample test.

---

## Phụ lục — Catalog `/api/v1/bao-cao/loai` (23 BC R7)

R7 catalog vs R6:
- R6 enum `BC_VV_THEO_LINH_VUC` → R7 `BC_VU_VIEC_THEO_LINH_VUC` (full-form).
- R6 enum `BC_DANH_GIA_HIEU_QUA_HTPL` → R7 `BC_DANH_GIA_HIEU_QUA` (drop suffix).

Toàn bộ 23 BC vẫn xuất hiện (group: Hỏi đáp pháp luật, Vụ việc, Đào tạo, Đánh giá, CG/TVV, VV phân tích, Chi phí, CT HTPLDN). Slug URL không đổi.
