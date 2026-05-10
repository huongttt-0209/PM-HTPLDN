# R7.2.4 Verify Report — Seed Doanh nghiệp

**Task:** R7.2.4 — Seed DN cover 3 quy mô × 3 ngành kinh doanh (chuẩn v3.5)
**Round:** R7 (2026-05-09)
**Tester:** huongttt + Claude (MCP chrome-devtools)
**Verdict:** ✅ PASS — 25 DN, 9/9 combo cover, gap VUA × CONG_NGHIEP fill 0→2 qua self-reg UI

---

## 1. Mục đích

User yêu cầu re-verify R7.2.4 sau khi todo claim "36 DN" (R7) → state-snapshot 2026-05-09 0h38 ghi 23 DN. Drift 36→23 cần xác minh + nếu thiếu combo gap thì seed bù.

## 2. Phương pháp

| Phase | Cách làm | Tool |
|---|---|---|
| Re-verify pool count + filter coverage | Fetch `GET /api/v1/doanh-nghieps?page=1&size=20` page 1+2, gộp 25 record, group by `quyMo` × `nganhNghe` | MCP `evaluate_script` |
| Phát hiện gap | Compare combo distribution với rule "≥1/combo" | Local JS reduce |
| Seed gap fill | Self-reg UI tại `/register/doanh-nghiep` (FR-VIII-22), full 21 trường, isolated context `dn-self-reg`, không account login | MCP `fill_form` + `click` listbox + `evaluate_script` cho spinbutton/date |
| Verify post-seed | Fetch lại `GET /api/v1/doanh-nghieps?search=<MST>` xác nhận record DB | MCP `evaluate_script` qua page QTHT |

## 3. Phase 1 — Pool re-verify (drift 36→23)

```
Total: 23 (page1=20 + page2=3) — trước seed
Total: 25 — sau seed 2 DN bổ sung
```

Drift 36→23 do scope cleanup (admin xoá test data). Acceptance gốc R7.2.4 "≥3 record/filter" vẫn thoả với 23, nhưng combo VUA × CONG_NGHIEP = 0 → vi phạm rule mỗi combo ≥1.

### Coverage trước seed (23 DN)
| Quy mô \ Ngành | CONG_NGHIEP | NONG_LAM | THUONG_MAI | Total |
|---|:-:|:-:|:-:|:-:|
| **VUA** | **0** ❌ | 2 | 4 | 6 |
| **NHO** | 5 | 1 | 1 | 7 |
| **SIEU_NHO** | 2 | 5 | 3 | 10 |
| **Total** | 7 | 8 | 8 | **23** |

Gap: VUA × CONG_NGHIEP = 0.

## 4. Phase 2 — Seed 2 DN gap fill

Cả 2 đăng ký qua **luồng self-reg công khai** (FR-VIII-22, không cần login QTHT) — verify đúng entry chính DN sẽ dùng trong production.

### DN #1 — DN-BGG-0001
| Trường | Giá trị |
|---|---|
| Tên DN | Công ty Cổ phần Vạn Lộc BG |
| MST | 5600000018 (checksum-valid prefix `5600000001` weights `[31,29,23,19,17,13,7,5,3]` → digit 8) |
| Loại DN | Công ty cổ phần (CP) |
| Tỉnh | Bắc Giang |
| Ngành | Công nghiệp và xây dựng (CONG_NGHIEP) |
| Quy mô | Vừa (VUA) |
| Số LĐ / Nữ / Khuyết tật | 150 / 50 / 5 |
| Doanh thu | 75 tỷ |
| Tổng vốn | 80 tỷ |
| Người ĐD | Phan Văn Lộc — Giám đốc |

**API verify:** `seqId=25`, `id=f51c342b-304d-4d4a-9bfa-aa6612d166f4`, `ngayTao=2026-05-08T18:06:59.908Z`. ✅

### DN #2 — Phú Cường BN
| Trường | Giá trị |
|---|---|
| Tên DN | Công ty TNHH Phú Cường BN |
| MST | 5700000029 (checksum-valid) |
| Loại DN | Công ty trách nhiệm hữu hạn (TNHH) |
| Tỉnh | Bắc Ninh |
| Ngành | Công nghiệp và xây dựng (CONG_NGHIEP) |
| Quy mô | Vừa (VUA) |
| Số LĐ / Nữ / Khuyết tật | 180 / 70 / 8 |
| Doanh thu | 90 tỷ |
| Tổng vốn | 95 tỷ |
| Người ĐD | Đỗ Văn Cường — Tổng giám đốc |

**API verify:** `seqId=26`, `id=ee79911c-a33c-4a50-91c2-9ae9c07d47b8`, `ngayTao=2026-05-08T18:10:06.944Z`. ✅

## 5. Phase 3 — Pool sau seed (25 DN)

| Quy mô \ Ngành | CONG_NGHIEP | NONG_LAM | THUONG_MAI | Total |
|---|:-:|:-:|:-:|:-:|
| **VUA** | **2** ✅ | 2 | 4 | 8 |
| **NHO** | 5 | 1 | 1 | 7 |
| **SIEU_NHO** | 2 | 5 | 3 | 10 |
| **Total** | 9 | 8 | 8 | **25** |

**Coverage:** 9/9 combo ≥1 ✅ — gap VUA × CN closed.

## 6. Findings phụ

1. **BUG-LOAI-DN-002 closed verified:** dropdown Loại DN render đúng 5 enum loại (Hợp danh / TNHH / CP / DNTN / HKD), KHÔNG còn show quy mô. ✅
2. **Quy mô dropdown chỉ 3 options** (Siêu nhỏ / Nhỏ / Vừa) — đúng spec NĐ 80/2021 (DN "Lớn" không thuộc scope HTPLDN).
3. **Form self-reg behavior:** sau click `[Đăng ký]` thành công, page giữ nguyên route `/register/doanh-nghiep` không chuyển — không có toast/redirect khẳng định success. Phải verify qua API list. **Đây là UX gap candidate** cho future bug log (chưa log lần này — Spec FR-VIII-22 chưa rõ AC step 5 sau submit).
4. **Submit click qua MCP `click` không trigger lần đầu** — phải dùng `evaluate_script` `btn.click()` mới fire. UID-based click hoạt động sai khi button ở dưới fold. Workaround: scrollIntoView + JS click.

## 7. Bằng chứng

- `r7-2-4-dn1-form-filled.png` — DN #1 filled trước submit
- `r7-2-4-dn1-after-submit.png` — DN #1 sau submit (form vẫn render, no toast — bug UX)
- `r7-2-4-dn2-form-filled.png` — DN #2 filled trước submit
- `r7-2-4-verify-pool-23-page1.png` + `*-page2.png` — pool list trước seed (23 DN)

## 8. Tác động downstream

| Task | Trước | Sau |
|---|---|---|
| R7.7.4 Functional DN | có data đủ | thêm 2 DN mới có thể re-test DN-006 (hard delete — spec đổi soft → hard 2026-05-07, xem [r7-8-1-hard-delete](../../functional/cross-cutting/functional-test-report-r7-8-1-hard-delete.md) + R11.1 verify DN endpoint trong [r7-7-4-dn report](../../functional/doanh-nghiep/functional-test-report-r7-7-4-dn.md)) |
| R7.7.10 KPI cross-DN | 23 DN | 25 DN |
| R7.5.2 Cross-module DN tabs | thoả | thoả |
| R7.8.7 E2E full luồng (mới thêm) | cần ≥1 DN fresh | DN-BGG-0001 + Phú Cường BN ứng viên (chưa login lần đầu, chưa có VV) |

## 9. Conclusion

R7.2.4 ✅ PASS — pool drift 36→23 do cleanup, gap VUA×CN closed bằng 2 DN seed mới qua self-reg UI. Acceptance per filter (9/9 combo ≥1) thoả. State-snapshot updated 23→25.

**Next:** R7.8.7 E2E có thể dùng 1 trong 2 DN mới làm fresh actor (chưa kích hoạt → start từ FR-VIII-26 reset MK).

---

## 10. Addendum 2026-05-09 17:15:00 — Retry seed DN Nhỏ × Nông lâm × Lạng Sơn (post throttle clear)

Sau khi BE 500 fix 2026-05-09 sáng + throttle clear, retry self-reg DN Nhỏ Nông lâm tại Lạng Sơn để cover thêm vùng địa lý.

### DN #3 — DN Nông sản Lạng Sơn

| Trường | Giá trị |
|---|---|
| Tên DN | Công ty TNHH Nông sản Lạng Sơn |
| MST | 5800000030 |
| Loại DN | Công ty trách nhiệm hữu hạn (TNHH) |
| Tỉnh | Lạng Sơn |
| Ngành | Nông, lâm nghiệp và thủy sản (NONG_LAM) |
| Quy mô | Nhỏ (NHO) — 50 LĐ / 25 tỷ DT / **18 tỷ vốn** ≤ 20 tỷ ngưỡng NĐ39/2018 nông lâm Nhỏ (BR pass) |
| Số LĐ / Nữ / Khuyết tật | 50 / 20 / 2 |
| Người ĐD | Phạm Văn Sơn — Giám đốc |

**API verify:** `POST /api/v1/auth/register-doanh-nghiep` reqid 160 → **201**. `GET /api/v1/doanh-nghieps?search=5800000030` trả `seqId=28`, `id=66bac9ff-9f63-4ab3-9213-54e3e1849b8e`, `quyMo=NHO`, `nganhNghe=NONG_LAM`, `ngayTao=2026-05-09T10:14:38.096Z`. ✅

### Pool sau seed (27 DN)

| Quy mô \ Ngành | CONG_NGHIEP | NONG_LAM | THUONG_MAI | Total |
|---|:-:|:-:|:-:|:-:|
| **VUA** | 2 | 2 | 4 | 8 |
| **NHO** | 5 | **2** ⬆️ | 1 | 8 |
| **SIEU_NHO** | 3 | 5 | 3 | 11 |
| **Total** | 10 | 9 | 8 | **27** |

NHO×NL pool 1→2 (đa dạng vùng — Lạng Sơn cover Đông Bắc bộ).

**Bằng chứng:**
- `r7-2-4-dn-ls-form-filled.png` — full form 21 trường trước submit
- `r7-2-4-dn-ls-after-submit.png` — sau submit (form vẫn render — UX gap đã note Issue #3 phần 6, BE đã 201 OK)

### Note BE recovery

Lần test trước (sáng 2026-05-09) BE 500 sustained → BLOCKED (Rule 9 ENV DOWN). Sau khi dev fix, retry success ngay lần đầu — BE login + register flow ổn định trở lại.
