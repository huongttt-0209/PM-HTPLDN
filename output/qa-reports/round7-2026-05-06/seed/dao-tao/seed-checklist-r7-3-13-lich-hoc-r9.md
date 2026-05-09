# Seed Checklist — Lịch học (R7.3.13 — R9 probe)

**Ngày:** 2026-05-09 20:33 • **Tài khoản:** N/A (probe via curl) • **Trạng thái mong đợi:** `LICH_HOC` entity endpoint plural deploy
**Màn:** SCR-III-22 Lịch học • **Đường dẫn:** `/dao-tao/lich-hoc/danh-sach` (chưa rõ FE deploy)
**SRS:** [FR-III-22 — Quản lý Lịch học](../../../../../input/srs-update-2026-5-5/srs-fr-03-dao-tao.md#fr-iii-22)
**Round:** R9 — probe BE endpoint, **BLOCKED do naming inconsistent**.

---

## Kết quả: 🚫 BLOCKED — Endpoint naming inconsistent

R9 probe phát hiện **route singular đã register (401 = needs auth) nhưng plural vẫn 404**. FE convention dùng plural cho tất cả module list call → FE list page sẽ 404.

```
GET /api/v1/lich-hocs?page=1&pageSize=5  →  HTTP 404  ❌ (plural — FE convention)
GET /api/v1/lich-hoc?page=1&pageSize=5   →  HTTP 401  ⚠️ (singular — needs auth)
```

**Đối chiếu các module Đào tạo khác (đều plural):**
- `/api/v1/ke-hoach-dao-taos` ✅
- `/api/v1/chuong-trinh-dao-taos` ✅
- `/api/v1/khoa-hocs` ✅
- `/api/v1/ngan-hang-cau-hois` ✅
- `/api/v1/de-kiem-tras` ✅
- `/api/v1/bai-giangs` ✅
- `/api/v1/giang-viens` ✅
- `/api/v1/lich-hoc` (singular) ⚠️ **EXCEPTION**

→ LICH_HOC singular là exception so với toàn bộ pattern. FE list call dùng plural sẽ fail.

---

## Cần dev clarify

- ☐ Endpoint chính thức: `/lich-hoc` (singular) hay `/lich-hocs` (plural)?
- ☐ Nếu giữ singular: FE list page phải sửa từ `/lich-hocs` → `/lich-hoc`
- ☐ Nếu đổi sang plural (recommend match convention): BE thêm route alias hoặc rename `/lich-hoc` → `/lich-hocs`
- ☐ Confirm schema đầy đủ field theo FR-III-22 (ngày, giờ, giảng viên link, khóa học link, phòng học, hình thức)
- ☐ Permission cho CB_NV_TW/BN/DP create/manage

---

## Impact downstream

| Task | Cascade |
|---|---|
| **R7.3.13** | BLOCKED trực tiếp — không seed được lịch học |
| R7.4.B12 (Quản lý lịch học workflow) | Cascade — không có data để test workflow |
| R7.7.6 (functional 40 TC) | Cascade — TC FR-III-22 block |

---

## Bug tracking

R9 không log bug formal — đây là **inconsistent naming** (potential FE/BE contract mismatch), defer log Minor sau khi dev clarify endpoint chính thức. Đã ghi escalation note ở [dev-escalation-r9-hoc-vien-lich-hoc.md](../../dev-escalation-r9-hoc-vien-lich-hoc.md).

---

*2026-05-09 20:33 — QA chạy bằng curl probe via Bash (singular trả 401 = route exists nhưng cần auth, plural trả 404 = route chưa register)*
