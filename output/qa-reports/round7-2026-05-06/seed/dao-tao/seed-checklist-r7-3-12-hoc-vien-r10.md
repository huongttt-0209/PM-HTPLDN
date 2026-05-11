# Seed Checklist — Học viên (R7.3.12 — R10 re-probe)

> **Module:** HOC_VIEN entity (FR-III + Mô hình A 1:1 với TAI_KHOAN) · **SRS:** [`02-thu-tu-module.md §HOC_VIEN`](../../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) · **Round:** R10 · **Date:** 2026-05-10 02:48-02:55 · **Tester:** QA Automation Claude Code MCP
> **Trigger:** User explicit "chạy lại R7.3.12 xem đã thật sự được fix chưa".

---

## 🎯 Tóm tắt nhanh (cho PM/BA)

**Kết quả: 🚫 STILL BLOCKED — block reason đổi từ "BE chưa code" → "BE service POST handler crash 500 (admin endpoint)".**

| R9 (2026-05-09) | R10 (2026-05-10) | Status change |
|---|---|---|
| BE 404 — entity 0 routes | BE 200 GET (qtht_01) + 500 POST với valid DTO | ✅ Routes registered, ❌ Service POST crash |
| FE CMS chưa code | FE 404 cho route HV master | ✅ **Đúng spec** — HV tạo qua chuyên trang DN/NHT FR-III-04, không CMS |
| 0 record seeded | 0 record seeded (POST 500 + chuyên trang chưa test) | ❌ Block persist |

**Findings (corrected sau SRS cite):**
1. ✅ BE `/api/v1/hoc-viens` registered 5 endpoints (GET list + POST + GET/PATCH/DELETE by id)
2. ✅ Swagger DTO available: `{hoTen* string, email* string, soDienThoai? string, donVi? string}` — match SRS FR-III-04 inputs
3. ❌ POST với valid DTO (qtht_01) → 500 `ERR-SYS-00-00-01` (service crash — **BUG-HV-BE-01 Major Open**)
4. ✅ Permission gate đúng spec: cb_nv_tw_02 + cb_pd_tw_02 403 đúng theo SRS FR-III-04 (Tác nhân = DN/NHT, không phải CB NV). qtht_01 200 với scope admin `👁️ R` toàn hệ thống.
5. ✅ FE missing CMS page đúng spec — HV được tạo qua chuyên trang DN/NHT FR-III-04 (UC23), KHÔNG phải CMS. FE chỉ render tab "Học viên" trong KH detail (= DKDT list, đã có).
6. ⏭ **Cần follow-up:** Verify chuyên trang DN/NHT FR-III-04 form đăng ký KH có hoạt động không (out of scope task seed này — sẽ test riêng).

**Pool count:** 0 record (target ≥5). Block bởi BUG-HV-BE-01 + chưa test chuyên trang DN/NHT.

---

## Probe results detail

### Endpoint deployment status
```
GET  /api/v1/hoc-viens               → 200 (qtht_01) | 403 (cb_nv_tw_02, cb_pd_tw_02)
GET  /api/v1/hoc-vien                → 404 (singular không có)
GET  /api/v1/hoc-viens?pageSize=10   → 200 data:[] total:0 (empty list, đúng pagination shape)
GET  /api/v1/khoa-hocs/{id}/hoc-viens → 404 (nested route không có)
GET  /api/v1/students                → 404
POST /api/v1/hoc-viens               → 500 ERR-SYS-00-00-01 (valid body) | 422 (invalid email)
```

→ Endpoint `/hoc-viens` plural chuẩn deployed. POST handler crash nội bộ.

### Swagger DTO (`/api/docs-json`)
```json
CreateHocVienDto:
  required: [hoTen, email]
  properties:
    - hoTen: string
    - email: string
    - soDienThoai: string
    - donVi: string
```

→ Schema simple 4 fields. KHÔNG có `taiKhoanId`/`dnId` field (Mô hình A 1:1 link có thể auto-create từ email).

### POST attempts (all 500 except validation triggers)
| Body | Status |
|---|:-:|
| `{hoTen:"x",email:"valid@test"}` | 500 |
| `{hoTen,email,soDienThoai,donVi}` (full DTO) | 500 |
| `{hoTen,email,sdt,...}` (extra fields) | 500 |
| `{email:"invalid",...}` | 422 ERR-VAL email |
| `{}` empty | 422 ERR-VAL hoTen+email |

→ Validation layer OK, service layer broken.

### UI investigation
1. Sidebar `qtht_01` group "Quản lý đào tạo, tập huấn" expanded → 6 items (Kế hoạch / Chương trình / Khóa học / Kho tài liệu / NHCH ĐKT / Giảng viên). **0 item "Học viên"**.
2. Route `/dao-tao/hoc-vien/danh-sach` → redirect `/dao-tao/chuong-trinh/danh-sach`.
3. Route `/hoc-vien/danh-sach` → 404 page render.
4. Tab "Học viên" trong KH detail → DANG_KY_DAO_TAO list (cột `Ngày đăng ký`, `Nguồn`, `Trạng thái`), KHÔNG phải HV master CRUD.

→ FE chưa implement page HV master.

---

## Bug logged

[Pass-bug-report-r7-3-12-hoc-vien-deploy-partial.md](../../bug-reports/dao-tao/Pass-bug-report-r7-3-12-hoc-vien-deploy-partial.md):
- ~~BUG-HV-BE-01~~ Major **Closed R11 2026-05-11** — BE thay crash 500 bằng 403 guard đúng spec FR-III-04
- ~~BUG-HV-FE-01~~ WITHDRAWN — FE missing CMS đúng spec FR-III-04 (HV qua chuyên trang DN/NHT)
- ~~BUG-HV-PERM-01~~ WITHDRAWN — 403 cb_nv_tw đúng spec FR-III-04 line 397-399 (Tác nhân = DN/NHT)

---

## Cascade impact (post-R10)

| Task | Pre-R10 | Post-R10 | Reason |
|---|---|---|---|
| **R7.3.12 Seed Học viên** | 🚫 BE 404 | 🚫 BE deploy partial + POST broken (FE CMS missing đúng spec FR-III-04 — DN/NHT chuyên trang) | Reason update; vẫn 0 record seeded |
| R7.7.6 DT-011 Điểm danh | 🚫 chờ R7.3.12 | 🚫 vẫn chờ | HOC_VIEN POST broken → không tạo được data |
| R7.7.6 DT-019 Đăng ký vượt sức chứa | 🚫 chờ R7.3.12 | 🚫 vẫn chờ | Cascade |
| R7.7.6 DT-031b Công bố KQ + chuyên trang | 🚫 chờ R7.3.12 | 🚫 vẫn chờ | Cascade |
| R7.7.6 DT-052 HOC_VIEN entity | 🚫 chờ R7.3.12 | 🚫 vẫn chờ | Cascade |
| R7.7.6 DT-054/055 Auto-classify + đạt khóa | 🚫 chờ R7.3.12 | 🚫 vẫn chờ | Cascade |

→ 6 TC functional vẫn block. Không thể unblock cho đến khi BUG-HV-BE-01 đóng + verify chuyên trang DN/NHT FR-III-04.

---

## Lịch sử round

| Round | Date | Kết quả |
|---|---|---|
| R8 | 2026-05-08 | (chưa probe) |
| R9 | 2026-05-09 20:33 | 🚫 BE 404 entity chưa code [seed-checklist R9](./seed-checklist-r7-3-12-hoc-vien-r9.md) |
| **R10** | **2026-05-10** | **🚫 BE deploy 5 routes + POST handler broken (500)** — 1 BUG Major Open (BUG-HV-BE-01). 2 bug ban đầu (FE-01 + PERM-01) đã withdraw sau cite SRS FR-III-04 (HV tạo qua chuyên trang DN/NHT, FE missing CMS + 403 cb_nv_tw đúng spec). |

---

*R10 verify | QA Automation via Claude Code MCP + curl | 2026-05-10 02:55*
