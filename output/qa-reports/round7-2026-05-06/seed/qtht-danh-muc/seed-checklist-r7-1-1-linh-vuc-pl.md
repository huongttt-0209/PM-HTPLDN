# Seed Checklist — Lĩnh vực Pháp lý (R7.1.1)

**Ngày:** 2026-05-06 14:08 • **Tài khoản:** `qtht_01` • **Trạng thái mong đợi:** `KICH_HOAT`
**Màn:** SCR-VIII-01 — Quản lý Danh mục (tab "Lĩnh vực pháp lý") • **Đường dẫn:** `/quan-tri/danh-muc/LINH_VUC_PL`
**Dữ liệu mẫu:** [seed-fixture.yaml > linh_vuc_pl_variants](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-VIII-01..13 §3.4.10 Quản lý Danh mục](../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md)

---

## Downstream consumer × filter

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.2.1 MPH 12 mẫu (6 LV × 2) | `mau_phan_hoi.linh_vuc_id ∈ DM LINH_VUC_PL` (FR-II-NEW-02) | ≥6 LV | `KICH_HOAT` | `GET /api/v1/danh-muc?loaiDanhMuc=LINH_VUC_PL` → ≥6 record | ✅ |
| R7.2.5/6 TVV/CG seed | `tu_van_vien.linh_vuc_ids[] ⊆ DM LINH_VUC_PL` | ≥6 LV | `KICH_HOAT` | same | ✅ |
| R7.3.1/2/3 HD/VV/TVCS entry | `linh_vuc_id ∈ DM LINH_VUC_PL` (FR-I/II/V) | ≥6 LV | `KICH_HOAT` | same | ✅ |
| R7.4.A3/A4/A5 Workflow phân công | dropdown filter `linh_vuc_id` matching | ≥6 LV | `KICH_HOAT` | same | ✅ |

**Acceptance pass:** ≥6 LV với `trangThai=KICH_HOAT` cover 6 LV fixture (LAO_DONG/THUE/DOANH_NGHIEP/SO_HUU_TRI_TUE/DAT_DAI/HOP_DONG nhóm).

---

## Kết quả: ✅ XONG 10/10 SRS (re-verify 2026-05-08 22:55)

> **Re-verify 2026-05-08 22:55 sau BUG-DM-LVPL-001 R8 lần 4 close (qtht_02 + Chrome DevTools MCP):**
> - **Layer 1 — DM master `/quan-tri/danh-muc/LINH_VUC_PL`:** table render đúng **10/10 LV SRS line 204** (THUE/LAO_DONG/DAT_DAI/DAN_SU/**THUONG_MAI**/HINH_SU/HANH_CHINH/SHTT/**DOANH_NGHIEP**/**DAU_TU**), pagination "1-10/10 mục", tất cả switch checked = KICH_HOAT. Bỏ 3 non-SRS (HON_NHAN_GIA_DINH/KINH_DOANH_TM/KHIEU_NAI_TO_CAO), thêm THUONG_MAI. Evidence: [r7-1-1-reverify-2026-05-08-layer1-dm-10-lv-srs.png](r7-1-1-reverify-2026-05-08-layer1-dm-10-lv-srs.png).
> - **Layer 2 — Dropdown filter MPH `/quan-tri/cau-hinh?tab=mau-phan-hoi`:** filter "Lĩnh vực PL" mở dropdown render **10 options sync DM master** (Thuế/Lao động/Đất đai/Dân sự/**Thương mại**/Hình sự/Hành chính/Sở hữu trí tuệ/**Doanh nghiệp**/**Đầu tư**). Sub-bug FE hardcode/cache đã đóng. Evidence: [r7-1-1-reverify-2026-05-08-layer2-dropdown-mph-10-lv.png](r7-1-1-reverify-2026-05-08-layer2-dropdown-mph-10-lv.png).
> - **Cascade unblock:** R7.2.1 (12 MPH cover 6 LV × 2) + R7.2.2/R7.2.6/R7.2.11 sẵn sàng re-attempt với fixture v2.7.2.

**Snapshot lịch sử (2026-05-06 14:08):** 12 LV pre-existing post-reset 2026-05-05 — vượt ngưỡng 6 LV fixture. Cover đầy đủ 6 LV core + 6 LV mở rộng. Sau dev fix R8 lần 4, DM gọn về đúng 10 LV SRS.

**Bug:** [Pass-bug-report-seed-r7-1-1-dm-linh-vuc-pl.md](../../bug-reports/qtht-danh-muc/Pass-bug-report-seed-r7-1-1-dm-linh-vuc-pl.md) — 1/1 đóng (BUG-DM-LVPL-001 Closed-verified R8 lần 4 2026-05-08).

---

## Bảng dữ liệu seed

| # | Mã | Tên | Thứ tự | Trạng thái | Trùng fixture? |
|---|----|-----|:-:|:-:|:-:|
| 1 | DAN_SU | Dân sự | 1 | KICH_HOAT | (mở rộng) |
| 2 | HINH_SU | Hình sự | 2 | KICH_HOAT | (mở rộng) |
| 3 | HANH_CHINH | Hành chính | 3 | KICH_HOAT | (mở rộng) |
| 4 | LAO_DONG | Lao động | 4 | KICH_HOAT | ✅ fixture |
| 5 | DAT_DAI | Đất đai | 5 | KICH_HOAT | ✅ fixture |
| 6 | HON_NHAN_GIA_DINH | Hôn nhân gia đình | 6 | KICH_HOAT | (mở rộng) |
| 7 | KINH_DOANH_TM | Kinh doanh thương mại | 7 | KICH_HOAT | (≈ HOP_DONG nhóm) |
| 8 | KHIEU_NAI_TO_CAO | Khiếu nại tố cáo | 8 | KICH_HOAT | (mở rộng) |
| 9 | THUE | Thuế | 9 | KICH_HOAT | ✅ fixture |
| 10 | SO_HUU_TRI_TUE | Sở hữu trí tuệ | 10 | KICH_HOAT | ✅ fixture |
| 11 | DOANH_NGHIEP | Doanh nghiệp | 11 | KICH_HOAT | ✅ fixture |
| 12 | DAU_TU | Đầu tư | 12 | KICH_HOAT | (mở rộng) |

**Tổng:** 12 vào kho / 0 bị chặn (5/6 fixture LV match trực tiếp, 1/6 HOP_DONG ≈ KINH_DOANH_TM).

---

## Ảnh chụp

- [LV table 12 records (R7 historical)](r7-1-1-linh-vuc-pl-12records.png)
- [Layer 1 DM master 10 LV SRS (R8 re-verify 2026-05-08)](r7-1-1-reverify-2026-05-08-layer1-dm-10-lv-srs.png)
- [Layer 2 dropdown MPH 10 LV sync (R8 re-verify 2026-05-08)](r7-1-1-reverify-2026-05-08-layer2-dropdown-mph-10-lv.png)

---

*2026-05-06 14:08 — QA chạy bằng Chrome DevTools MCP*
