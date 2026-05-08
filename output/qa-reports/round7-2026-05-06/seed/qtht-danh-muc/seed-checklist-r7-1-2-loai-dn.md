# Seed Checklist — Loại Doanh nghiệp (R7.1.2)

**Ngày:** 2026-05-06 14:09 • **Tài khoản:** `qtht_01` • **Trạng thái mong đợi:** `KICH_HOAT`
**Màn:** SCR-VIII-01 — Quản lý Danh mục (tab "Loại doanh nghiệp") • **Đường dẫn:** `/quan-tri/danh-muc/LOAI_DOANH_NGHIEP`
**Dữ liệu mẫu:** [seed-fixture.yaml > dn_variants[].loai_doanh_nghiep_id (TNHH/CP/DNTN/HKD)](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-VII-01 §Inputs row 7 `loai_doanh_nghiep_id` FK → DANH_MUC](../../../../input/srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md)

---

## Downstream consumer × filter

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.2.4 Seed 15 DN | `dn_variants[].loai_doanh_nghiep_id ∈ {TNHH,CP,DNTN,HKD}` (fixture v2.7.2) | 4 loại hình DN | `KICH_HOAT` | `GET /api/v1/danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP&ma=TNHH` → ≥1 | ✅ |
| R7.7.4 DN functional 8 TC | `dn.loaiDoanhNghiepId` valid FK | 4 loại hình DN | `KICH_HOAT` | same | ✅ |

**Acceptance pass:** 4 record `TNHH/CP/DNTN/HKD` tồn tại với `trangThai=KICH_HOAT`.

---

## Kết quả: ✅ XONG 4/4 fixture (re-verify 2026-05-08 23:30)

> **Re-verify 2026-05-08 23:30 (qtht_02 + Chrome DevTools MCP API + UI):**
> - **API check:** `GET /api/v1/danh-muc?loaiDanhMuc=LOAI_DOANH_NGHIEP&pageSize=100` → 5 records, distribution: TNHH/CP/DNTN/HKD (4 fixture) + CTHD_TEST (Re-test BUG-LOAI-DN-002 sau dev fix). Tất cả `trangThai=KICH_HOAT`.
> - **UI render:** `/quan-tri/danh-muc/LOAI_DOANH_NGHIEP` table 5/5 mục, all switch=checked. Old quy_mo DM (DN_SIEU_NHO/NHO/VUA) đã được dev tách sang DM riêng theo Phương án A (BUG-LOAI-DN-002 Closed-verified R7 lần 2026-05-07).
> - **Evidence:** [r7-1-2-loai-dn-reverify-2026-05-08-5records.png](r7-1-2-loai-dn-reverify-2026-05-08-5records.png).

**Snapshot lịch sử (2026-05-06 → 2026-05-07):** Lần đầu R7 sáng → 3/7 (3 quy_mo pre-existing) + BE 422 block 4 fixture. Sau dev fix lần 1 chiều → BE 500 (fix nửa chừng) + spec contradiction FR-10 vs FR-07. Sau dev fix lần 2 (2026-05-07, Phương án A — tách DM quy_mo riêng) → DM `LOAI_DOANH_NGHIEP` chỉ chứa loại hình pháp lý (TNHH/CP/DNTN/HKD), POST CTHD_TEST → 201 OK ⇒ BUG-LOAI-DN-002 Closed-verified.

**Bug:** [`BUG-LOAI-DN-002`](../../bug-reports/qtht-danh-muc/bug-report-seed-r7-1-2-loai-dn.md) — 1/1 đóng (Closed-verified R7 2026-05-07).

---

## Bảng dữ liệu seed (cuối — re-verify 2026-05-08 23:30)

| # | Mã | Tên | Thuộc nhóm | Trạng thái | Status |
|---|----|-----|------------|:-:|:-:|
| 1 | TNHH | Công ty trách nhiệm hữu hạn | loai_hinh (FR-VII-01 row 6) | KICH_HOAT | ✅ |
| 2 | CP | Công ty cổ phần | loai_hinh | KICH_HOAT | ✅ |
| 3 | DNTN | Doanh nghiệp tư nhân | loai_hinh | KICH_HOAT | ✅ |
| 4 | HKD | Hộ kinh doanh | loai_hinh | KICH_HOAT | ✅ |
| 5 | CTHD_TEST | Công ty hợp danh test verify | test record (re-test BUG-002) | KICH_HOAT | ✅ extra |

**Tổng:** 5 vào kho (4 fixture + 1 test). Old quy_mo (DN_SIEU_NHO/NHO/VUA) đã được dev tách sang DM riêng theo Phương án A.

---

## Ảnh chụp

- [LOAI_DN table chỉ 3 records (R7 historical — sáng 2026-05-06)](r7-1-2-loai-dn-3-of-7-only.png)
- [Modal Thêm TNHH bị toast "Dữ liệu không hợp lệ" (R7 historical)](../../bug-reports/image/bug-loai-dn-002-tnhh-rejected-toast.png)
- [LOAI_DN table 5 records sau dev fix Phương án A (R8 re-verify 2026-05-08)](r7-1-2-loai-dn-reverify-2026-05-08-5records.png)

---

*2026-05-06 14:09 — QA chạy bằng Chrome DevTools MCP*
