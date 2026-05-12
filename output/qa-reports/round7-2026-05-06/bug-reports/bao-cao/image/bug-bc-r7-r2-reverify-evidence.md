# R7-r2 Re-verify Evidence — 2026-05-12 01:58:00 (3 isolatedContext)

Tool: Chrome DevTools MCP. Login UI flow đầy đủ (username + password + OTP 666666). Session ổn định ~5 phút không bị revoke. Sang ngày mới (2026-05-12) so với R7 (2026-05-11), verify pattern còn ổn định không.

## Kết quả tổng

| Bug | R7 verdict | R7-r2 verdict | Diff |
|---|---|---|:-:|
| BUG-BC-PDF-NOT-SUPPORTED | Open (6/6 fail) | Open (4/4 sample lặp fail) | Không đổi |
| BUG-BC-XLSX-PARTIAL-SUPPORT | Closed (3/3 PASS) | Closed (3/3 PASS confirm) | Không đổi |
| BUG-BC-KYBAOCAO-NOT-VALIDATED Validation | Closed (12/12 reject) | Closed (2/2 confirm reject) | Không đổi |
| BUG-BC-KYBAOCAO-NOT-VALIDATED Aggregation | Open (flat key) | Open (vẫn flat key `2026-05` cả 4 enum) | Không đổi |
| BUG-BC-DATA-SCOPE-LEAK HD+VV | Closed (4/4 role) | Closed (mở rộng VV tiếp nhận + VV đang hỗ trợ cũng OK) | **Mở rộng PASS** |
| BUG-BC-DATA-SCOPE-LEAK ChiPhi+TVV | Open (leak) | Open (+ phát hiện `/chi-phi-theo-don-vi` cũng leak) | **Mở rộng FAIL** |

## 1. PDF universal — 4/4 vẫn 422

POST `/api/v1/bao-cao/export` với `formatXuat: "PDF"` (account `cb_nv_tw_08`):

| BC enum | Status | Code |
|---|:---:|---|
| `BC_HOI_DAP` | 422 | `ERR-RPT-EXPORT-01` |
| `BC_VU_VIEC_HOAN_THANH` | 422 | `ERR-RPT-EXPORT-01` |
| `BC_CHI_PHI_CHI_TRA` | 422 | `ERR-RPT-EXPORT-01` |
| `BC_SO_LUONG_CG_TVV` | 422 | `ERR-RPT-EXPORT-01` |

## 2. XLSX bonus confirm — 3/3 vẫn PASS

| BC enum | Status | Binary len |
|---|:---:|---:|
| `BC_HOI_DAP` | 200 | 6392 |
| `BC_VU_VIEC_THEO_LINH_VUC` | 200 | 6440 |
| `BC_DANH_GIA_HIEU_QUA` | 200 | 6328 |

## 3. Validation kyBaoCao — 2/2 BC R6 fail vẫn FIXED

| Endpoint | Status | Code | Field |
|---|:---:|---|---|
| `/bao-cao/hoi-dap?kyBaoCao=INVALID` | 422 | `ERR-VAL-SYS-00-01` | `kyBaoCao` |
| `/bao-cao/danh-gia-hieu-qua?kyBaoCao=INVALID` | 422 | `ERR-VAL-SYS-00-01` | `kyBaoCao` |

## 4. Aggregation `/bao-cao/hoi-dap` theoKy — Vẫn flat 4/4 enum

| Enum | `theoKy[0].ky` | `theoKy[0].soLuong` |
|---|---|---:|
| TUAN | `2026-05` | 20 |
| THANG | `2026-05` | 20 |
| QUY | `2026-05` | 20 |
| NAM | `2026-05` | 20 |

→ Aggregation chưa fix — 4 enum trả response identical.

## 5. DATA-SCOPE-LEAK — Mở rộng matrix với `cb_pd_dp_08` (Sở BG)

| Endpoint | TW baseline | cb_pd_dp_08 | Scope đúng? |
|---|---:|---:|:-:|
| `/bao-cao/hoi-dap` | 26 | **0** | ✅ |
| `/bao-cao/vu-viec-hoan-thanh` | 4 | **0** | ✅ |
| `/bao-cao/vu-viec-tiep-nhan` (mới) | — | **0** | ✅ |
| `/bao-cao/vu-viec-dang-ho-tro` (mới) | — | **0** | ✅ |
| `/bao-cao/chi-phi-chi-tra` | 209.592.242 | 209.592.242 | ❌ LEAK |
| `/bao-cao/chi-phi-theo-don-vi` (mới) | — | 209.592.242 | ❌ LEAK |
| `/bao-cao/so-luong-cg-tvv` | 8 | 8 | ❌ LEAK |

Mở rộng matrix R7-r2 cho thấy:
- **Module HD + VV (4 endpoint):** wire `dataScopeMiddleware` ĐÚNG (4/4 role nhận 0).
- **Module Chi phí + TVV:** wire MISSING — `/chi-phi-chi-tra`, `/chi-phi-theo-don-vi`, `/so-luong-cg-tvv` đều leak. Cần dev wire middleware tất cả endpoint trong group này (gồm `/chi-phi-theo-linh-vuc`, `/chi-phi-theo-loai-dn`, `/chi-phi-theo-thoi-gian` chưa test).
- **Module CT HTPLDN:** chưa test rõ (response shape khác — `ct_dv` không có field summary tongCT).

## 6. cb_nv_bn_08 (BTC) — confirm pattern không đổi với role NV

| Endpoint | tongHoiDap | tongVuViec | tongChiPhi | tongTvv |
|---|---:|---:|---:|---:|
| `/bao-cao/hoi-dap` | **0** ✅ | — | — | — |
| `/bao-cao/vu-viec-hoan-thanh` | — | **0** ✅ | — | — |
| `/bao-cao/chi-phi-chi-tra` | — | — | 209.592.242 ❌ | — |
| `/bao-cao/so-luong-cg-tvv` | — | — | — | 8 ❌ |

Confirm: cả role NV (cb_nv_bn_08) + PD (cb_pd_dp_08) đều cùng pattern bug systematic theo module BE, không random theo role.
