# Bug Report — R7.7.6 HV-related dependencies (R11 verify 9 TC)

> **Module:** Đào tạo / Khóa học functional (FR-III-04 + FR-III-19 + FR-III-21)
> **Discovered:** 2026-05-11 R11 (sau khi BUG-HV-BE-01 closed)
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| BUG-DT-052-HV-TAIKHOAN-01 | Minor | HV entity thiếu field `taiKhoanId` per spec FR-III-04 (HV ↔ TAI_KHOAN 1:1 link) | Open |
| BUG-DT-011-DD-ENDPOINT-01 | Major | DIEM_DANH POST endpoint chưa deploy (404); GET trả mock; field `coMat` boolean thay vì enum 3 trị (CO_MAT/VANG_PHEP/VANG_KHONG_PHEP) | Open |
| BUG-DT-031-KQHT-ENTITY-01 | Major | KET_QUA_HOC_TAP entity chưa deploy (mọi route 404) — block 5 TC (DT-031b + DT-031c + DT-031d + DT-054 + DT-055) | Open |

---

## Tổng hợp R11 verify 9 TC HV-related

Sau khi BUG-HV-BE-01 closed R11 + 6 HV records seeded R11, re-test 9 TC R7.7.6 HV-related (DT-011/011a/019/031b/c/d/052/054/055). Phát hiện entity dependencies chưa đầy đủ để verify hết 9 TC.

| TC | Status R11 | Detail |
|---|:-:|---|
| **DT-019** Đăng ký vượt sức chứa | ✅ **PASS** | KH-003 cap=3: 3 DKDT đầu 201 Created; attempt 4 → **422 `ERR-BIZ-III-04-03 "Khóa học đã đạt số lượng đăng ký tối đa"`** match spec ERR-DK-DT-03. Screenshot: [r11-dt019-capacity-422-pass.png](../../screenshots/r11-dt019-capacity-422-pass.png) |
| **DT-052** HV ↔ TAI_KHOAN 1:1 link | ❌ **FAIL Spec drift** | HV detail GET trả 13 fields (id/seqId/version/hoTen/email/soDienThoai/donVi/nguoiHoTroId/...) — **KHÔNG có `taiKhoanId`** field. Spec FR-III-04 yêu cầu HV link 1:1 với TAI_KHOAN qua field `tai_khoan_id`. → Log Minor BUG-DT-052-HV-TAIKHOAN-01 |
| **DT-011** Điểm danh per-buổi enum + công thức | ⚠️ **Partial** | GET `/khoa-hocs/{id}/diem-danhs` trả 200 với mock data (id rỗng + `coMat: boolean` thay vì enum 3 trị spec yêu cầu). POST endpoint 404 — không tạo được DD record. → Log Major BUG-DT-011-DD-ENDPOINT-01 |
| **DT-011a** Điểm danh không lich_hoc | 🚫 **BLOCKED** | Cascade DT-011 (DD POST 404) |
| **DT-031b** Công bố KQ FR-III-19 | 🚫 **BLOCKED** | KQHT entity 404 + Cổng PLQG mock chưa setup |
| **DT-031c** Hủy công bố KQ | 🚫 **BLOCKED** | Cascade DT-031b |
| **DT-031d** API Cổng PLQG retry | 🚫 **BLOCKED** | Cascade DT-031b |
| **DT-054** Auto xếp loại điểm | 🚫 **BLOCKED** | KQHT entity 404 (cần entity để verify auto-classify Giỏi/Khá/TB/Không đạt) |
| **DT-055** HV đạt khóa (chuyên cần + điểm) | 🚫 **BLOCKED** | KQHT 404 + DD POST 404 |

→ **Net result:** 1 PASS / 1 FAIL spec / 1 ⚠️ Partial / 6 BLOCKED.

---

## BUG-DT-052-HV-TAIKHOAN-01 — HV entity thiếu field `taiKhoanId`

### Mô tả
SRS FR-III-04 (UC23) Inputs row "tai_khoan_id" yêu cầu HOC_VIEN có FK `tai_khoan_id` → TAI_KHOAN (1:1 link). Khi tạo HV qua chuyên trang DN/NHT, BE phải đồng thời tạo TAI_KHOAN record và link qua field này. Hiện tại HV detail GET KHÔNG expose `taiKhoanId` field.

### Bước tái hiện
1. Login `qtht_01`.
2. `GET /api/v1/hoc-viens/aacc0008-0000-4000-8000-000000000001`.
3. Quan sát response.data fields.

### Kết quả mong đợi
- Schema có field `taiKhoanId: UUID | null` (link tới TAI_KHOAN).

### Kết quả thực tế
- 13 fields: `id, nguoiTaoId, nguoiCapNhatId, ngayTao, ngayCapNhat, donViId, seqId, version, hoTen, email, soDienThoai, donVi, nguoiHoTroId`.
- KHÔNG có `taiKhoanId`.

### Recommend
Cần BA confirm: TAI_KHOAN link là MUST (per FR-III-04 row spec) hay OPTIONAL? Nếu MUST → BE add field + auto-create TK khi POST HV. Nếu OPTIONAL/withdraw → cập nhật spec.

---

## BUG-DT-011-DD-ENDPOINT-01 — DIEM_DANH POST + enum schema mismatch

### Mô tả
SRS FR-III-04 + DT-011 yêu cầu:
- POST `/khoa-hocs/{id}/diem-danhs` để CB NV ghi điểm danh per-buổi
- Field `trang_thai_diem_danh` enum 3 giá trị: `CO_MAT`, `VANG_PHEP`, `VANG_KHONG_PHEP`
- Công thức chuyên cần: `(CO_MAT + VANG_PHEP) / tổng × 100` (VANG_PHEP KHÔNG trừ chuyên cần)
- FK `lich_hoc_id` mandatory link với LICH_HOC

Hiện tại:
- POST endpoint 404 (chưa deploy)
- GET endpoint trả mock data với schema sai: field `coMat: boolean` (binary) thay vì enum 3 giá trị

### Recommend
- Dev BE expose POST endpoint với schema match spec (3 enum + lich_hoc_id FK)
- Sửa GET response trả real data (không mock)

---

## BUG-DT-031-KQHT-ENTITY-01 — KET_QUA_HOC_TAP entity chưa deploy

### Mô tả
SRS FR-III-19 (Hướng B v3.5) + FR-III-21 yêu cầu entity `KET_QUA_HOC_TAP` (KQHT) lưu kết quả từng HV per khóa với fields:
- `dang_ky_id` (FK DKDT)
- `diem_kiem_tra` (decimal)
- `xep_loai` (enum Giỏi/Khá/TB/Không đạt — auto classify từ điểm)
- `ket_qua` (enum DAT/KHONG_DAT — auto classify từ chuyên cần + điểm)
- `xep_loai_override` + `ly_do_override` (manual override)

Hiện tại mọi route 404:
- `/api/v1/ket-qua-hoc-taps`
- `/api/v1/khoa-hocs/{id}/ket-qua-hoc-taps`
- `/api/v1/khoa-hocs/{id}/ket-qua`
- `/api/v1/khoa-hocs/{id}/diem`
- `/api/v1/dang-ky-dao-taos/{id}/ket-qua`

→ Block 5 TC: DT-031b (công bố KQ), DT-031c (hủy công bố), DT-031d (retry Cổng PLQG), DT-054 (auto xếp loại), DT-055 (HV đạt khóa).

### Recommend
Dev BE deploy KQHT entity + 5 routes (GET list, POST, GET/PATCH/DELETE by id) + auto-classify logic theo BR-KQ-01/02.

---

## So sánh — Entity status

| Entity | R10 status | R11 status | Action |
|---|---|---|---|
| HOC_VIEN | POST 500 crash | ✅ POST 403 (đúng spec); GET 200 (6 records seeded R11) | Closed BUG-HV-BE-01 |
| DKDT (DANG_KY_DAO_TAO) | 404 | ✅ POST/GET nested route OK; FR-III-04 schema (hoTen/email/sdt/nguonDangKy) | Verified DT-019 PASS |
| LICH_HOC | OK (R7.4.B12) | OK | Stable |
| DIEM_DANH | (chưa probe) | ⚠️ GET mock + POST 404 + schema sai | NEW BUG-DT-011-DD-ENDPOINT-01 |
| KET_QUA_HOC_TAP | 404 | 404 (chưa deploy) | NEW BUG-DT-031-KQHT-ENTITY-01 |
| HV.taiKhoanId | (chưa kiểm) | ❌ field thiếu | NEW BUG-DT-052-HV-TAIKHOAN-01 |

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL | http://103.172.236.130:3000 |
| Account | `qtht_01 / Secret@123` (admin scope) |
| OTP | `666666` |
| Tool | Chrome DevTools MCP |

---

*R11 log | QA Automation via Claude Code MCP | 2026-05-11*
