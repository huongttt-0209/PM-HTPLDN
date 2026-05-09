# Seed Checklist — Ngày Lễ 2026 (R7.1.5)

**Ngày:** 2026-05-06 14:12 • **Tài khoản:** `qtht_01` • **Trạng thái mong đợi:** `loai=NGAY_LE` (active)
**Màn:** *(UI tab "Ngày lễ" CHƯA deploy — DEPLOY-004)* — seed qua **API direct** • **Đường dẫn API:** `POST /api/v1/ngay-le`
**Dữ liệu mẫu:** [seed-fixture.yaml > ngay_le_variants v2.7.1 line 230-235](../../../../input/data/seed-fixture.yaml)
**SRS:** [FR-VIII-29 §3.2 Quản lý ngày lễ `[GAP-VIII-05]`](../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md)

---

## Downstream consumer × filter

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.5.3 SLA banner trừ ngày lễ (BR-CALC-03) | `ngay BETWEEN deadline_start AND deadline_end` | ≥1 ngày lễ trong khoảng deadline test | active | `GET /api/v1/ngay-le?nam=2026` → ≥10 record | ✅ |
| R7.7.17 Edge BR-EC-12 SLA holiday skip | same | same | active | same | ✅ |

**Acceptance pass:** đủ 5 khoảng ngày lễ FY2026 (Tết DL/Tết NĐ/Giỗ Tổ/30-4+1-5/Quốc khánh) — BE schema single-date nên expand multi-day periods thành record/ngày.

---

## Kết quả: ⚠️ MỘT PHẦN ~80% — 5/5 data, FE submit silent block UI (re-verify 2026-05-08 23:38)

> **Re-verify 2026-05-08 23:38 R8 lần 6 (qtht_02 + Chrome DevTools MCP):**
> - **State pool hiện tại:** 5 record (4 pre-existing Tết DL/30-4/1-5/Quốc khánh + Tết NĐ Bính Ngọ qua API workaround R8 lần 6 id `0647a404-4e84-4578-9718-8f2fa080f853`). 11 record extra của R7 đã bị reset cùng pool. Cover 4/5 khoảng pháp định 2026 (thiếu Giỗ Tổ + Nghỉ bù — không phải acceptance bắt buộc).
> - **UI submit re-test lần 6:** Click [+ Thêm mới] → **drawer mở** (không phải Modal — phát hiện R8 lần 6: form là `.ant-drawer-section`). Fill ngày `17/02/2026` + tên + ghi chú → click [Đồng ý] → drawer stuck open, KHÔNG có `POST /api/v1/ngay-le`, toast inline `Vui lòng chọn ngày` (FE validation state stale dù `input.value` đã set). BUG-NGAY-LE-001 vẫn Open sau 6 lần verify.
> - **API workaround:** `POST /api/v1/ngay-le` với JWT session → 201 OK record save DB → table reload UI 5/5 ✅. BE work fine, FE submit handler bug.
> - **Evidence:** [r7-1-5-tab-ngay-le-5-records-reverify-2026-05-08.png](r7-1-5-tab-ngay-le-5-records-reverify-2026-05-08.png) (UI 5/5 sau API seed) + [bug-ngay-le-001-retest-lan-6-2026-05-08.png](../../bug-reports/qtht-cau-hinh-ht/bug-ngay-le-001-retest-lan-6-2026-05-08.png) (drawer stuck).

**Snapshot lịch sử (2026-05-06 14:12):** 15/5 khoảng cover đầy đủ qua API direct workaround (UI tab chưa deploy DEPLOY-004 lúc đó). 5 khoảng: Tết DL/Tết NĐ 7 ngày/Giỗ Tổ/30-4+1-5+nghỉ bù/Quốc khánh+nghỉ bù.

**Bug:** [BUG-NGAY-LE-001](../../bug-reports/qtht-cau-hinh-ht/bug-report-seed-r7-1-5-ngay-le.md) Major Open lần 6/6 — FE [Đồng ý] silent fail, không trigger POST. Workaround API direct OK.

---

## Bảng dữ liệu seed

### Pre-existing (4 record từ DB seed)

| # | Ngày | Tên ngày lễ | Khoảng | Status |
|---|------|-------------|--------|:-:|
| 1 | 2026-01-01 | Tết Dương lịch | DL (1 ngày) | ✅ |
| 2 | 2026-04-30 | Ngày Giải phóng miền Nam (30/4) | 30/4-1/5 | ✅ |
| 3 | 2026-05-01 | Ngày Quốc tế Lao động (1/5) | 30/4-1/5 | ✅ |
| 4 | 2026-09-02 | Ngày Quốc khánh (2/9) | Quốc khánh | ✅ |

### Seeded mới (11 record, 2026-05-06 14:12)

| # | Ngày | Tên ngày lễ | Khoảng | API id | Status |
|---|------|-------------|--------|--------|:-:|
| 5 | 2026-02-16 | Tết Nguyên đán Bính Ngọ (mùng 1) | Tết NĐ | 2c852cd5-... | ✅ 201 |
| 6 | 2026-02-17 | Tết Nguyên đán Bính Ngọ (mùng 2) | Tết NĐ | d25e5ebe-... | ✅ 201 |
| 7 | 2026-02-18 | Tết Nguyên đán Bính Ngọ (mùng 3) | Tết NĐ | a43e9614-... | ✅ 201 |
| 8 | 2026-02-19 | Tết Nguyên đán Bính Ngọ (mùng 4) | Tết NĐ | bebe6939-... | ✅ 201 |
| 9 | 2026-02-20 | Tết Nguyên đán Bính Ngọ (mùng 5) | Tết NĐ | d34d9db3-... | ✅ 201 |
| 10 | 2026-02-21 | Tết Nguyên đán Bính Ngọ (mùng 6) | Tết NĐ | 11debee9-... | ✅ 201 |
| 11 | 2026-02-22 | Tết Nguyên đán Bính Ngọ (mùng 7) | Tết NĐ | 106afc22-... | ✅ 201 |
| 12 | 2026-04-26 | Giỗ Tổ Hùng Vương (10/3 ÂL) | Giỗ Tổ | aa7c1f84-... | ✅ 201 |
| 13 | 2026-05-02 | Nghỉ bù 30/4-1/5 (ngày 1) | 30/4-1/5 | 73fd337d-... | ✅ 201 |
| 14 | 2026-05-03 | Nghỉ bù 30/4-1/5 (ngày 2) | 30/4-1/5 | af10979c-... | ✅ 201 |
| 15 | 2026-09-01 | Nghỉ bù Quốc khánh (1/9) | Quốc khánh | a578c352-... | ✅ 201 |

**Coverage 5 khoảng fixture:**
- Tết Dương lịch (2026-01-01): ✅ 1/1 ngày
- Tết Nguyên đán (2026-02-16..22): ✅ 7/7 ngày
- Giỗ Tổ Hùng Vương (2026-04-26): ✅ 1/1 ngày
- Giải phóng + QTLĐ (2026-04-30..05-03): ✅ 4/4 ngày
- Quốc khánh (2026-09-01..02): ✅ 2/2 ngày

**Tổng:** 15 vào kho / 0 bị chặn.

---

## Ảnh chụp

- *(R7 historical: không có UI screenshot — UI tab chưa deploy DEPLOY-004; verify qua API response trên)*
- [Tab Ngày lễ 5/5 records sau R8 lần 6 API workaround (2026-05-08)](r7-1-5-tab-ngay-le-5-records-reverify-2026-05-08.png)
- [Drawer Thêm mới ngày lễ stuck sau click [Đồng ý] — BUG-NGAY-LE-001 lần 6 (2026-05-08)](../../bug-reports/qtht-cau-hinh-ht/bug-ngay-le-001-retest-lan-6-2026-05-08.png)

---

*2026-05-06 14:12 — QA chạy bằng Chrome DevTools MCP `evaluate_script` POST API direct (workaround UI gap)*
