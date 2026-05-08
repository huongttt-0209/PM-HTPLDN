# Seed Checklist — R7.5.5 Audit log ≥100 entry

**Ngày:** 2026-05-09 00:38 • **Tài khoản:** `qtht_02` • **Trạng thái mong đợi:** active multi-action multi-entity multi-user
**Màn:** SCR-VIII-NK — Quản trị → Nhật ký hệ thống • **Đường dẫn UI:** `/quan-tri/audit-log` • **API:** `/api/v1/audit-logs?page=N&pageSize=100`
**SRS:** FR-VIII-28 §3.4.13 Quản lý nhật ký hệ thống

---

## Downstream consumer × filter

| Task downstream | Đọc filter | Số record cần | Verify query | Status |
|---|---|---|---|:-:|
| R7.7.X functional Nhật ký HT (filter date / module / action / user / entity) | tab Nhật ký + 5 filter | ≥100 entry | `GET /api/v1/audit-logs?pageSize=100` total ≥100 | ✅ |
| Audit trail compliance | Cover các action quan trọng | LOGIN/LOGOUT/CREATE/UPDATE/DELETE/APPROVE/PHE_DUYET | 20 distinct actions | ✅ |
| Multi-entity coverage | TAI_KHOAN / TVV / NHT / DM / etc. | ≥10 entity types | 15 entity types | ✅ |
| Multi-user coverage | QTHT/CB_NV_TW/BN/DP active | ≥5 users | 10+ users active | ✅ |

**Acceptance:** ≥100 entry tích lũy qua Phase 1-4 task chạy. Verify qua API count + UI render.

---

## Kết quả: ✅ XONG **1468 entries** (14.68× ngưỡng ≥100)

> **Verify 2026-05-09 00:38 (qtht_02 + Chrome DevTools MCP):**
> - **API:** `GET /api/v1/audit-logs?page=1&pageSize=100` → 200 OK, `meta.total = 1468`, `totalPages = 15`. Fetch full 15 page tổng 1468 record.
> - **UI:** `/quan-tri/audit-log?tuNgay=2026-05-02&denNgay=2026-05-09` render table với column "Thời gian / Người dùng / Đơn vị / Module / Entity / Mã bản ghi / Loại thao tác / Chi tiết thay đổi". Pagination "1-50 / 1440 mục" (filter date 2026-05-02 → 2026-05-09 hiện 1440; tổng all-time 1468).
> - **Filter UI:** date range / Người dùng / Module / Loại thao tác / Entity textbox / Tìm kiếm / Xóa bộ lọc / Xuất Excel.
> - **Evidence:** [r7-5-5-audit-log-1440-records-2026-05-09.png](../../workflow/qtht-tai-khoan/r7-5-5-audit-log-1440-records-2026-05-09.png).

---

## Distribution by action (top 20)

| # | hanhDong | Count | % |
|:-:|---|---:|---:|
| 1 | CREATE | 406 | 27.7% |
| 2 | LOGIN_OTP_PENDING | 318 | 21.7% |
| 3 | LOGIN | 293 | 20.0% |
| 4 | UPDATE | 87 | 5.9% |
| 5 | THAM_DINH | 58 | 4.0% |
| 6 | LOGOUT | 51 | 3.5% |
| 7 | SUBMIT | 33 | 2.2% |
| 8 | APPROVE | 29 | 2.0% |
| 9 | PHE_DUYET | 28 | 1.9% |
| 10 | DELETE | 21 | 1.4% |
| 11 | PHAN_CONG | 11 | 0.7% |
| 12 | TIEP_NHAN | 11 | 0.7% |
| 13 | UNPUBLISH | 10 | 0.7% |
| 14 | PUBLISH | 10 | 0.7% |
| 15 | DANH_GIA | 9 | 0.6% |
| 16 | KIEM_TRA | 9 | 0.6% |
| 17 | ACTIVATE_ACCOUNT | 8 | 0.5% |
| 18 | PASSWORD_CHANGE | 8 | 0.5% |
| 19 | TU_CHOI | 7 | 0.5% |
| 20 | CANCEL | 7 | 0.5% |

**20 distinct actions** cover full audit trail spectrum.

## Distribution by entity (top 15)

| # | entityType | Count |
|:-:|---|---:|
| 1 | TAI_KHOAN | 743 |
| 2 | UNKNOWN | 153 |
| 3 | TU_VAN_VIEN | 139 |
| 4 | CHUONG_TRINH_HTPL | 65 |
| 5 | DOT_BAO_CAO | 48 |
| 6 | HO_SO_CHI_TRA | 34 |
| 7 | HO_SO_PHAP_LY_DN | 29 |
| 8 | NGUOI_HO_TRO | 28 |
| 9 | KHO_CAU_HOI | 27 |
| 10 | NOI_DUNG_TU_VAN_CS | 25 |
| 11 | BAI_GIANG | 23 |
| 12 | TO_CHUC_TU_VAN | 18 |
| 13 | DANH_MUC | 18 |
| 14 | HOI_DAP | 18 |
| 15 | THU_MUC_BIEU_MAU | 15 |

**15 entity types** cover M3-M14 modules.

## Distribution by user (top 10)

| # | Username | Count |
|:-:|---|---:|
| 1 | cb_nv_tw_02 | 457 |
| 2 | cb_nv_tw_01 | 253 |
| 3 | qtht_02 | 146 |
| 4 | cb_nv_dp_01 | 81 |
| 5 | qtht_03 | 76 |
| 6 | cb_pd_tw_02 | 60 |
| 7 | qtht_01 | 44 |
| 8 | cb_nv_bn_01 | 40 |
| 9 | admin | 40 |
| 10 | cb_pd_tw_01 | 36 |

**10+ users active** cover QTHT / CB_NV_TW/BN/DP / CB_PD_TW / admin role.

---

## Sample record schema

```json
{
  "id": "95b276b0-8fff-4214-a48f-c53c10aeb20d",
  "entityType": "TAI_KHOAN",
  "entityId": "18806c47-a672-49c7-8f07-d16a9b7d6543",
  "hanhDong": "LOGIN",
  "nguoiThucHienId": "18806c47-a672-49c7-8f07-d16a9b7d6543",
  "systemActor": null,
  "consumerId": null,
  "thoiGian": "2026-05-08T17:36:33.878Z",
  "ipAddress": "::ffff:127.0.0.1",
  "endpoint": null,
  "responseCode": null,
  "sessionId": null,
  "module": null,
  "nguoiThucHienUsername": "qtht_02",
  "nguoiThucHienHoTen": "QTHT Test 02",
  "donViId": null,
  "donViTen": null,
  "nguoiThucHienVaiTro": "Quản trị hệ thống"
}
```

Schema match SRS FR-VIII-28: id / thời gian / người thực hiện / vai trò / đơn vị / loại thao tác / entity / endpoint / IP.

---

## Cascade impact

- ✅ **R7.7.X functional Nhật ký HT** unblocked: ≥1468 entry để test 5 filter (date / user / module / action / entity).
- ✅ **Audit trail compliance** đạt: cover 20 action × 15 entity × 10 user — đủ data để export Excel + báo cáo SRS.

---

## Ảnh chụp

- [Audit log table 1-50/1440 với filter date 2026-05-02 → 2026-05-09](../../workflow/qtht-tai-khoan/r7-5-5-audit-log-1440-records-2026-05-09.png)

---

*2026-05-09 00:38 — QA chạy bằng Chrome DevTools MCP API + UI.*
