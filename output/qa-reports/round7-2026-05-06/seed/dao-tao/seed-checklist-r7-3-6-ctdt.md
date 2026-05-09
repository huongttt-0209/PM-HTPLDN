# Seed Checklist — Chương trình Đào tạo (R7.3.6)

**Ngày:** 2026-05-09 18:45–19:00 • **Tài khoản:** `cb_nv_tw_02` (CB_NV_TW) • **Trạng thái mong đợi:** `Dự thảo (DU_THAO)`
**Màn:** SCR-III-01 — Chương trình đào tạo • **Đường dẫn:** `/dao-tao/chuong-trinh/danh-sach`
**Dữ liệu mẫu:** [seed-fixture.yaml > chuong_trinh_dao_tao_variants 1-5](../../../../../input/data/seed-fixture.yaml#L2373)
**SRS:** FR-III-01 — Tạo CTĐT cấp BTP TW + Mô hình A đảo chiều · **Round:** R9 2026-05-09

---

## Downstream consumer × filter (BẮT BUỘC trước khi seed)

| Task downstream | Đọc filter (quote SRS) | Số record cần | State entity yêu cầu | Verify query | Status |
|-----------------|------------------------|---------------|----------------------|--------------|:---:|
| R7.3.15 Khóa học (FR-III-02) | `ctdtId` FK strict, BE chấp nhận `DU_THAO` (verified R8 probe 2026-05-08) | ≥1 CTĐT mỗi LV cần khóa | `DU_THAO` (BE bypass workflow OK) | `GET /api/v1/khoa-hocs?ctdtId=<UUID>` (post-seed của khoa-hoc) | ✅ |
| R7.4.B1 Workflow CTĐT 3 state | `trangThai=DU_THAO` filter để advance → `CHO_DUYET` → `DA_DUYET` | ≥1 CTĐT/LV để cover advance | `DU_THAO` | `GET /api/v1/chuong-trinh-dao-taos?trangThai=DU_THAO` → ≥5 (cover 5 LV) | ✅ |
| FR-III-NEW-03 phân phối ĐKT | `ctdtId` từ ĐKT → CTĐT để build cấu trúc khóa | ≥1 CTĐT/LV match ĐKT LV | `DU_THAO`/`DA_DUYET` | đã verify R7.4.B10 endpoint live | ⏭ defer |

**Acceptance pass:**
- ✅ 5 CTĐT cấp TW cover **5/10 LV** (Doanh nghiệp + Lao động + Sở hữu trí tuệ + Đất đai + Thuế).
- ⏸ **5 LV còn lại** (Dân sự, Thương mại, Hình sự, Hành chính, Đầu tư) — defer khi cần khoá học cụ thể.
- 🚫 **Variant 6 cấp ĐP-DN (THUONG_MAI)** — chờ approve KH-0006 (cấp DP) bởi role `cb_pd_dp_*`. Logged riêng.

---

## Kết quả: ✅ XONG 5/5 (cấp TW)

Seeded 5 CTĐT entry trạng thái `Dự thảo (DU_THAO)` trên màn SCR-III-01 cấp TW, cover 5 LV. Endpoint UI `POST /api/v1/chuong-trinh-dao-taos` 200 OK. Liên kết keHoachId tới 2 KH năm DA_DUYET (KH-0001 + KH-0004 R8) tạo từ R9 verify R7.4.B0.

**Variant 6 (ĐP-DN)** defer pending: chưa có KH cấp DP `DA_DUYET` (KH-0006 vẫn `CHO_DUYET`, chờ `cb_pd_dp_01` approve).

**Form schema drift note:** Form FE đơn giản hơn fixture YAML — KHÔNG có các field `doi_tuong`, `hinh_thuc` (TRUC_TUYEN/TRUC_TIEP/KET_HOP), `thoi_gian_bat_dau`, `thoi_gian_ket_thuc`, `file_dinh_kem`. Có 8 field core: `Mã CTĐT (auto)` + `Tên` + `Kế hoạch năm (FK)` + `Lĩnh vực (FK)` + `Ngân sách` + `Số khóa` + `Mục tiêu` + `Mô tả`.

**Bug:** [bug-report-seed-r7-3-6-ctdt.md](../../../round7-2026-05-06/bug-reports/dao-tao/bug-report-seed-r7-3-6-ctdt.md) — 1/1 đóng (BUG-CTDT-FE-01 form `keHoachId` Closed-verified persists). Form filter dropdown KH năm: chỉ show 2 KH `DA_DUYET` (đúng spec).

---

## Bảng dữ liệu seed

| # | Tên CTĐT | LV | KH năm parent | Ngân sách | Số khóa | Mã | State |
|---|----------|------|----------------|-----------|---------|-----|:----:|
| 1 | CTĐT 2026 - Pháp luật cho DN nhỏ | Doanh nghiệp | KH-20260508-0004 (TW R8) | 800.000.000 | 6 | CTDT-BTP-TW-2026-0001 | DU_THAO |
| 2 | CTĐT 2026 - ATLĐ ngành xây dựng | Lao động | KH-20260508-0001 (TW R7) | 500.000.000 | 3 | CTDT-BTP-TW-2026-0002 | DU_THAO |
| 3 | CTĐT 2026 - SHTT cho startup | Sở hữu trí tuệ | KH-20260508-0004 (TW R8) | 300.000.000 | 2 | CTDT-BTP-TW-2026-0003 | DU_THAO |
| 4 | CTĐT 2025 - Luật đất đai | Đất đai | KH-20260508-0001 (TW R7) | 400.000.000 | 2 | CTDT-BTP-TW-2026-0004 | DU_THAO |
| 5 | CTĐT 2026 - Luật thuế DN xuất khẩu | Thuế | KH-20260508-0004 (TW R8) | 250.000.000 | 3 | CTDT-BTP-TW-2026-0005 | DU_THAO |

**Tổng:** 5/5 vào kho.

### Verify per-filter (BẮT BUỘC theo CLAUDE.md "Quy tắc seed task")

| Filter | Query | Expected | Actual |
|---|---|:--:|:--:|
| Total CTĐT cấp TW | `GET /chuong-trinh-dao-taos?page=1&pageSize=20` | ≥5 | ✅ 5 |
| State `DU_THAO` | filter `trangThai=DU_THAO` | 5/5 | ✅ 5/5 |
| LV Doanh nghiệp | `linhVucId=...001a` | ≥1 | ✅ 1 (CTDT-0001) |
| LV Lao động | `linhVucId=...0013` | ≥1 | ✅ 1 (CTDT-0002) |
| LV SHTT | `linhVucId=...0019` | ≥1 | ✅ 1 (CTDT-0003) |
| LV Đất đai | `linhVucId=...0014` | ≥1 | ✅ 1 (CTDT-0004) |
| LV Thuế | `linhVucId=...0018` | ≥1 | ✅ 1 (CTDT-0005) |
| KH parent KH-0001 | `keHoachId=<KH-0001 UUID>` | ≥1 | ✅ 2 (CTDT-0002 + 0004) |
| KH parent KH-0004 | `keHoachId=<KH-0004 UUID>` | ≥1 | ✅ 3 (CTDT-0001 + 0003 + 0005) |

---

## Bằng chứng API

```json
GET /api/v1/chuong-trinh-dao-taos?page=1&pageSize=20  status=200, total=5
[
  {"ma":"CTDT-BTP-TW-2026-0005","ten":"CTĐT 2026 - Luật thuế DN xuất khẩu","trangThai":"DU_THAO","ngan_sach":250000000},
  {"ma":"CTDT-BTP-TW-2026-0004","ten":"CTĐT 2025 - Luật đất đai","trangThai":"DU_THAO","ngan_sach":400000000},
  {"ma":"CTDT-BTP-TW-2026-0003","ten":"CTĐT 2026 - SHTT cho startup","trangThai":"DU_THAO","ngan_sach":300000000},
  {"ma":"CTDT-BTP-TW-2026-0002","ten":"CTĐT 2026 - ATLĐ ngành xây dựng","trangThai":"DU_THAO","ngan_sach":500000000},
  {"ma":"CTDT-BTP-TW-2026-0001","ten":"CTĐT 2026 - Pháp luật cho DN nhỏ","trangThai":"DU_THAO","ngan_sach":800000000}
]
```

---

## Ảnh chụp

- [List 5 CTĐT DU_THAO sau seed R9](r7-3-6-ctdt-list-5-du-thao.png)

---

*2026-05-09 19:00 — QA chạy bằng Chrome DevTools MCP via Claude Code*
