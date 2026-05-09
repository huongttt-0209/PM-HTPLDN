# Seed Checklist — Mẫu phản hồi (R7.2.1)

**Ngày:** 2026-05-08 23:11 • **Tài khoản seed:** `cb_nv_tw_01` (TW) + `cb_nv_bn_01/03` (BN) + `cb_nv_dp_01/03` (DP) • **Account verify cuối:** `qtht_02` • **Trạng thái mong đợi:** `KICH_HOAT`
**Màn:** SCR-VIII-04 — Cấu hình hệ thống (tab "Mẫu phản hồi") • **Đường dẫn:** `/quan-tri/cau-hinh?tab=mau-phan-hoi`
**Dữ liệu mẫu:** [seed-fixture.yaml v2.7.2](../../../../../input/data/seed-fixture.yaml) `mau_phan_hoi_variants` (1-6 TW) + `mau_phan_hoi_bn_variants` (7-9 BN) + `mau_phan_hoi_dp_variants` (10-12 DP)
**SRS:** `srs-update-2026-5-4/srs-fr-02-hoi-dap.md §FR-II-NEW-02` (CĐT chốt 2026-05-02)
**Upstream:** R7.1.1 ✅ DM `LINH_VUC_PL` 10/10 LV SRS (re-verify 2026-05-08 22:55) — BUG-DM-LVPL-001 closed R8 lần 4

---

## Downstream consumer × filter

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.3.1 HD seed (FR-II-NEW-02) | `mau_phan_hoi.linh_vuc_id ∈ HD.linh_vuc_id` + `pham_vi_ap_dung` matching role | ≥1 MPH per LV in 6 LV core | `KICH_HOAT` | UI dropdown "Chọn mẫu phản hồi" trong reply HD form | ✅ |
| R7.3.x HD reply per cấp | TW: 6 mẫu shared / BN: own + TW / DP: own + TW | ≥6 TW + ≥1 BN-BKH/BCT + ≥1 DP-AG/BNI | `KICH_HOAT` | filter "Phạm vi" = TW_QUOC_GIA (6) / BN_RIENG (3) / DP_RIENG (3) | ✅ |
| R7.7.5 functional MPH 22 TC | CRUD + filter combo (LV × Loại × Trạng thái × Phạm vi) | ≥12 mẫu cover all combos | `KICH_HOAT` | full table | ✅ |

**Acceptance pass:** 12 mẫu KICH_HOAT (6 TW + 3 BN + 3 DP) cover 6 LV × 2/LV. Match fixture v2.7.2 100%.

---

## Kết quả: ✅ XONG 12/12 (cover 6 LV × 2/LV)

> **Cascade unblock từ R7.1.1 close R8 lần 4 (2026-05-08 22:55):** DM master `LINH_VUC_PL` 10/10 LV SRS + dropdown filter MPH sync 10 LV → R7.2.1 chuyển từ 🚫 → 🟢 → ✅ trong cùng phiên QA.

**3 mẫu pre-existing (R7 ngày 07/05/2026):**
- HD - Lao động (cb_nv_tw_01, TW_QUOC_GIA)
- BN-BTC - Thuế (cb_nv_bn_02, BN_RIENG)
- DP-BG - Sở hữu trí tuệ (cb_nv_dp_02, DP_RIENG)

**9 mẫu seed mới (R8 ngày 08/05/2026):**

| # | Account | Tên mẫu | Lĩnh vực | Phạm vi | Trạng thái |
|:-:|---|---|---|---|:-:|
| 1 | cb_nv_tw_01 | Mẫu phản hồi HD - Doanh nghiệp | Doanh nghiệp | Trung ương | ✅ KH |
| 2 | cb_nv_tw_01 | Mẫu phản hồi HD - Thương mại | Thương mại | Trung ương | ✅ KH |
| 3 | cb_nv_tw_01 | Mẫu phản hồi HD - Thuế | Thuế | Trung ương | ✅ KH |
| 4 | cb_nv_tw_01 | Mẫu phản hồi HD - Sở hữu trí tuệ | Sở hữu trí tuệ | Trung ương | ✅ KH |
| 5 | cb_nv_tw_01 | Mẫu phản hồi HD - Đất đai | Đất đai | Trung ương | ✅ KH |
| 6 | cb_nv_bn_01 | Mẫu phản hồi BN-BKH - Doanh nghiệp | Doanh nghiệp | Bộ ngành | ✅ KH |
| 7 | cb_nv_bn_03 | Mẫu phản hồi BN-BCT - Lao động | Lao động | Bộ ngành | ✅ KH |
| 8 | cb_nv_dp_01 | Mẫu phản hồi DP-AG - Hợp đồng | Thương mại | Địa phương | ✅ KH |
| 9 | cb_nv_dp_03 | Mẫu phản hồi DP-BNI - Đất đai | Đất đai | Địa phương | ✅ KH |

**Bug:** Không có (R7.2.1 cascade chỉ block bởi R7.1.1 — đã closed; bản thân flow seed UI không có defect).

---

## Bảng dữ liệu cuối (verify qtht_02)

| LV | Count | Phạm vi distribution |
|---|:-:|---|
| Doanh nghiệp | 2 | TW (HD) + BN (BKH) |
| Thương mại | 2 | TW (HD) + DP (AG-Hợp đồng) |
| Lao động | 2 | TW (HD) + BN (BCT) |
| Thuế | 2 | TW (HD) + BN (BTC) |
| Sở hữu trí tuệ | 2 | TW (HD) + DP (BG) |
| Đất đai | 2 | TW (HD) + DP (BNI) |
| **Tổng** | **12** | 6 TW + 3 BN + 3 DP |

---

## Ảnh chụp

- [12 records final cover 6 LV × 2](r7-2-1-mph-12-records-final-2026-05-08.png)

---

## Ghi chú technical

**Pattern seed UI Ant Design:** Modal "Thêm mẫu phản hồi" có 4 fields (Tên mẫu / LV combobox / Loại mẫu combobox / Nội dung textarea). Combobox cần `mousedown+mouseup+click` (không phải click thuần) để trigger AntD dropdown open. Textarea cần native HTMLTextAreaElement setter + dispatch `input`/`change` event để React state update (fill_form MCP không persist multiline).

**App-side cross-scope visibility:** CB_NV_TW thấy 6 (own TW + 1 BN-BKH cũng thấy → tổng 7 sau seed)? **Không** — TW thấy 6 own. CB_NV_BN-BKH thấy 6 TW (shared) + own BN = 7. CB_NV_DP-AG thấy 6 TW + own DP = 7. QTHT thấy ALL 12. Verified 2026-05-08 23:11.

*2026-05-08 23:11 — QA chạy bằng Chrome DevTools MCP, 5 account login switches.*
