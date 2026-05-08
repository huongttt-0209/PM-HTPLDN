# Seed Checklist — Đơn vị (R7.1.3)

**Ngày:** 2026-05-06 14:11 • **Tài khoản:** `qtht_01` • **Trạng thái mong đợi:** `HOAT_DONG`
**Màn:** SCR-VIII-01 — Quản lý Danh mục (tab "Cơ quan đơn vị") • **Đường dẫn:** `/quan-tri/danh-muc/DON_VI`
**Dữ liệu mẫu:** [seed-fixture.yaml > don_vi_variants (TW + 3 BN + AG/BG/BNI)](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-VIII-04 §Inputs DON_VI](../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md)

---

## Downstream consumer × filter

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.2.4 DN seed | `dn.don_vi_quan_ly` ∈ DON_VI {TW + BN + DP} | TW + 3 BN + 3 DP | `HOAT_DONG` | `GET /api/v1/don-vi?cap=BN` → ≥3 / `?cap=DP` → AG/BG/BNI | ✅ |
| R7.2.5/6 TVV/CG seed | `tu_van_vien.don_vi_id` ∈ DON_VI | ≥7 đơn vị | `HOAT_DONG` | same | ✅ |
| R7.2.8 Account `cb_nv_dp_*` | username suffix `dp_*` map DON_VI cấp DP | ≥3 DP | `HOAT_DONG` | `?cap=DP` → AG/BG/BNI | ✅ |
| R7.4.A1.5 PC modal | dropdown đơn vị quản lý | ≥7 | `HOAT_DONG` | same | ✅ |

**Acceptance pass:** đủ 7 đơn vị: 1 TW (BTP-TW) + 3 BN (BKH/BTC/BCT) + 3 DP (STP-AG/STP-BG/STP-BNI).

---

## Kết quả: ✅ XONG 7/7 (re-verify 2026-05-08 23:25)

> **Re-verify 2026-05-08 23:25 (qtht_02 + Chrome DevTools MCP API call):**
> - **API check:** `GET /api/v1/don-vi?pageSize=100` → 84 records, distribution: 1 TW + 20 BN + 63 DP, ALL HOAT_DONG.
> - **7 đơn vị bắt buộc:** BTP-TW ✅ + BKH ✅ + BTC ✅ + BCT ✅ + STP-AG ✅ + STP-BG ✅ + STP-BNI ✅, tất cả `trangThai=HOAT_DONG`.
> - **UI render:** `/quan-tri/danh-muc/DON_VI` cây đơn vị TW root + tab "Cơ quan đơn vị" active. Evidence: [r7-1-3-don-vi-tree-reverify-2026-05-08.png](r7-1-3-don-vi-tree-reverify-2026-05-08.png).

**Snapshot lịch sử (2026-05-06 14:11):** 7/7 đơn vị pre-existing post-reset, tổng 84 đơn vị trong DB — vượt ngưỡng. Convention app đã ổn định từ R6 (AG/BG/BNI thay cho HN/HP/DN của fixture cũ).

**Bug:** Không có.

---

## Bảng dữ liệu seed

| # | Mã | Tên | Cấp | Status |
|---|----|-----|:-:|:-:|
| 1 | BTP-TW | Cục Bổ trợ tư pháp - Bộ Tư pháp | TW | ✅ |
| 2 | BKH | Bộ Kế hoạch và Đầu tư | BN | ✅ |
| 3 | BTC | Bộ Tài chính | BN | ✅ |
| 4 | BCT | Bộ Công Thương | BN | ✅ |
| 5 | STP-AG | Sở Tư pháp An Giang | DP | ✅ |
| 6 | STP-BG | Sở Tư pháp Bắc Giang | DP | ✅ |
| 7 | STP-BNI | Sở Tư pháp Bắc Ninh | DP | ✅ |

**Tổng:** 7 vào kho / 0 bị chặn (84 record tổng trong DB).

---

## Ảnh chụp

- [Cây đơn vị TW root (R7 historical)](r7-1-3-don-vi-tree-tw-root.png)
- [Cây đơn vị tab CQ-ĐV (R8 re-verify 2026-05-08)](r7-1-3-don-vi-tree-reverify-2026-05-08.png)

---

*2026-05-06 14:11 — QA chạy bằng Chrome DevTools MCP*
