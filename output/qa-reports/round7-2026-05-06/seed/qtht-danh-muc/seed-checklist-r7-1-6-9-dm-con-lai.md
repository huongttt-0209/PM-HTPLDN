# Seed Checklist — R7.1.6: 9 DM còn lại qua UI SCR-VIII-01

| Thông tin | Giá trị |
|-----------|---------|
| **Task** | R7.1.6 (Phase 1 — Tier 0 seed) |
| **Ngày** | 2026-05-06 |
| **Account** | `qtht_02` / Secret@123 / OTP 666666 (theo user chốt 2026-05-06) |
| **Tool** | Chrome DevTools MCP (per CLAUDE.md routing) |
| **URL** | http://103.172.236.130:3000/quan-tri/danh-muc/{LOAI_DM} |
| **SRS ref** | FR-VIII-02/03/04/08/09/11/12/18/19 |

## Verdict

**✅ 9/9 DM PASS** — 9 DM đạt acceptance ≥3 record cover dropdown downstream. DM2 CHUONG_TRINH_HT đã unblocked sau dev fix R7 + R8 seed thêm CT_HTPLDN (2026-05-08 23:52 — đạt 3/3).

> **Re-verify 2026-05-08 23:50 (qtht_02 + Chrome DevTools MCP API batch):**
> - **9 DM API check:** all `GET /api/v1/danh-muc?loaiDanhMuc=...&pageSize=100` → 200, count match. DM1=6, DM2=3 (sau seed +1), DM3=12, DM4=4, DM5=4, DM6=3, DM7=3, DM8=5, DM9=4. Tất cả KICH_HOAT.
> - **DM2 CHUONG_TRINH_HT seed CT_HTPLDN 2026-05-08 23:52:** UI form đầy đủ 3 trường SRS (Thời gian bắt đầu/kết thúc/Đơn vị chủ trì) — BUG-DM-CTHT-002 fix verified. URL routing `/CHUONG_TRINH_HT` đúng SRS — BUG-DM-CTHT-001 fix verified. UI submit programmatic (native setter trên Antd DatePicker) chưa update React state → fallback API direct POST với schema `duLieuMoRong: {donViChuTri, thoiGianBatDau, thoiGianKetThuc}` → 201 OK record id `02ca6ef1-...`. UI reload → table 3/3 mục. Evidence: [r7-1-6-dm2-chuong-trinh-ht-3-records-2026-05-08.png](r7-1-6-dm2-chuong-trinh-ht-3-records-2026-05-08.png).

## Per-DM result table

| # | DM | URL key | Acceptance | Records | Status | Note |
|---|---|---|---|---|---|---|
| 1 | LOAI_HINH_HT | `LOAI_HINH_HO_TRO` | ≥3 | **6 pre-existing** | ✅ PASS | TU_VAN/TO_TUNG/DAI_DIEN_NGOAI_TT/HOA_GIAI/DAO_TAO/TRO_GIUP_KHAC. Match SRS Seed Data. |
| 2 | CHUONG_TRINH_HT | `CHUONG_TRINH_HT` (đúng SRS) | ≥3 | **3** (2 pre-existing + 1 R8 seed CT_HTPLDN) | ✅ PASS | R7: BUG-DM-CTHT-001 routing + BUG-DM-CTHT-002 form 3 fields. R7 dev fix Closed-verified (URL `/CHUONG_TRINH_HT` đúng + form đủ 3 trường). R8 2026-05-08 seed thêm `CT_HTPLDN` qua API workaround (UI Antd DatePicker programmatic setter chưa fire React onChange) → 3/3 đạt acceptance. **Bug closed:** [bug-report-seed-r7-1-6-dm-cthttp.md](../../bug-reports/qtht-danh-muc/bug-report-seed-r7-1-6-dm-cthttp.md). |
| 3 | TINH_TRANG_VV | `TINH_TRANG_VU_VIEC` | ≥3 | **12 pre-existing** | ✅ PASS | 12 SM state VV (MOI_TAO/CHO_TIEP_NHAN/.../TU_CHOI). |
| 4 | HO_SO_DE_NGHI_HT | `HO_SO_DE_NGHI_HT` | ≥3 | **4 pre-existing** | ✅ PASS | DON_DE_NGHI_HT/CMND_CCCD/GCNDK_KD/HS_CHUNG_MINH_DK + cột "LOẠI" Bắt buộc/Tùy chọn. |
| 5 | HO_SO_DE_NGHI_TT | `HO_SO_DE_NGHI_TT` | ≥3 | **4 pre-existing** | ✅ PASS | BANG_KE_CHI_PHI/BIEN_LAI_THU_PHI/HOP_DONG_DV_TV/BIEN_BAN_NGHIEM_THU. |
| 6 | TIEU_CHI_DG_HQ | `TIEU_CHI_DG_HIEU_QUA` | ≥3 + Σ=100 | **3 seed** | ✅ PASS | TC-PL/TC-NL/TC-HQ trọng số 30/30/40, Σ=100% ✓ (BR-CALC-04). Form có Trọng số/Min/Max. |
| 7 | TIEU_CHI_DG_CP | `TIEU_CHI_DG_CHI_PHI` | ≥3 + Σ=100 | **3 seed** | ✅ PASS ⚠️ | TC-CP-NL/TC-CP-DL/TC-CP-VP trọng số 40/30/30, Σ=100% ✓. **Note:** Form same DM6 (Trọng số/Min/Max) — nếu SRS yêu cầu `quy_mo_dn`/`muc_ho_tro` riêng → cần BA verify. |
| 8 | LOAI_HINH_TIEP_NHAN | `LOAI_HINH_TIEP_NHAN` | ≥3 | **5 pre-existing** | ✅ PASS | TRUC_TUYEN/TRUC_TIEP/BUU_CHINH/DIEN_THOAI/HE_THONG_KHAC. |
| 9 | KENH_TIEP_NHAN | `KENH_TIEP_NHAN` | ≥3 | **4 pre-existing** | ✅ PASS ⚠️ | CONG_DVC/THU_DIEN_TU/FAX/BO_PHAN_MOT_CUA. **Note:** fixture YAML `seed-fixture.yaml` enum (DVC/CONG_PLQG/TRUC_TIEP/HE_THONG_KHAC) khác DB — fixture cần update, KHÔNG phải bug FE per memory `feedback_fixture_mismatch_not_bug`. |

## Records seed mới R7.1.6 + R8

### R7 seed (2026-05-06)

| DM | Mã | Tên | Trọng số | Min | Max |
|---|---|---|---|---|---|
| DM6 TIEU_CHI_DG_HIEU_QUA | TC-PL | Tính pháp lý | 30 | 1 | 5 |
| DM6 TIEU_CHI_DG_HIEU_QUA | TC-NL | Năng lực | 30 | 1 | 5 |
| DM6 TIEU_CHI_DG_HIEU_QUA | TC-HQ | Hiệu quả | 40 | 1 | 5 |
| DM7 TIEU_CHI_DG_CHI_PHI | TC-CP-NL | Chi phí nhân lực | 40 | 1 | 5 |
| DM7 TIEU_CHI_DG_CHI_PHI | TC-CP-DL | Chi phí đi lại | 30 | 1 | 5 |
| DM7 TIEU_CHI_DG_CHI_PHI | TC-CP-VP | Chi phí văn phòng + pháp lý | 30 | 1 | 5 |

### R8 seed (2026-05-08)

| DM | Mã | Tên | Mô tả | Thời gian | Đơn vị chủ trì | API id |
|---|---|---|---|---|---|---|
| DM2 CHUONG_TRINH_HT | CT_HTPLDN | Chương trình hỗ trợ pháp lý doanh nghiệp | Theo NĐ 55/2019/NĐ-CP | 2026-01-01 → 2030-12-31 | Cục Bổ trợ tư pháp - Bộ Tư pháp | `02ca6ef1-...` |

Tổng record (R7+R8): 50 = 41 pre-existing (DM1: 6 + DM3: 12 + DM4: 4 + DM5: 4 + DM8: 5 + DM9: 4 + DM2: 2 + DM6: 0 + DM7: 0) + 6 R7 seed (DM6+DM7) + 1 R8 seed (DM2). Acceptance per-filter ≥3 **đạt 9/9 DM**.

## Screenshots

- [r7-1-6-dm1-loai-hinh-ht.png](r7-1-6-dm1-loai-hinh-ht.png)
- [r7-1-6-dm2-be-422-empty.png](r7-1-6-dm2-be-422-empty.png) (R7 BUG evidence — historical)
- [r7-1-6-dm2-form-thieu-truong.png](r7-1-6-dm2-form-thieu-truong.png) (R7 BUG evidence — historical)
- [r7-1-6-dm2-chuong-trinh-ht-3-records-2026-05-08.png](r7-1-6-dm2-chuong-trinh-ht-3-records-2026-05-08.png) (R8 — DM2 unblocked + seeded CT_HTPLDN, 3/3 mục)
- [r7-1-6-dm3-tinh-trang-vv.png](r7-1-6-dm3-tinh-trang-vv.png)
- [r7-1-6-dm4-ho-so-de-nghi-ht.png](r7-1-6-dm4-ho-so-de-nghi-ht.png)
- [r7-1-6-dm5-ho-so-de-nghi-tt.png](r7-1-6-dm5-ho-so-de-nghi-tt.png)
- [r7-1-6-dm6-tieu-chi-dg-hq.png](r7-1-6-dm6-tieu-chi-dg-hq.png)
- [r7-1-6-dm7-tieu-chi-dg-cp.png](r7-1-6-dm7-tieu-chi-dg-cp.png)
- [r7-1-6-dm8-loai-hinh-tiep-nhan.png](r7-1-6-dm8-loai-hinh-tiep-nhan.png)
- [r7-1-6-dm9-kenh-tiep-nhan.png](r7-1-6-dm9-kenh-tiep-nhan.png)

## Cascade impact

- **R7.7.8** QTHT 14 DM CRUD functional: 9/9 DM seed đủ → unblock toàn bộ. DM2 CHUONG_TRINH_HT đã 3 record sau R8 seed → FR-VIII-03 unblock.
- **DM6/7 BR-CALC-04**: Σ trọng số = 100% verified — alert UI bật badge ✓.

*Generated: 2026-05-06 | QA Automation via Claude Code | account: qtht_02*
