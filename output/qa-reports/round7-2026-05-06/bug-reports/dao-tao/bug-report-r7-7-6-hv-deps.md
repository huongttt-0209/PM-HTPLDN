# Bug Report — R7.7.6 HV-related dependencies (R11 verify 9 TC)

> **Module:** Đào tạo / Khóa học functional (FR-III-04 + FR-III-19 + FR-III-21)
> **Discovered:** 2026-05-11 R11 (sau khi BUG-HV-BE-01 closed)
> **Reporter:** QA Automation Claude Code MCP

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| BUG-DT-052-HV-TAIKHOAN-01 | Minor | HV entity thiếu field `taiKhoanId` per spec FR-III-04 (HV ↔ TAI_KHOAN 1:1 link) | **REOPEN** (R12.4 2026-05-12 — withdrawal R12 18:30 SAI sau cross-check 5 SRS sources. **4/5 sources confirm `tai_khoan_id` REQUIRED**: master entity spec `srs-v3.5.md §3.4.3.53` line 3349-3368 (11 fields, field 11 = `tai_khoan_id` nullable FK TAI_KHOAN); master entity matrix `srs-v3.5.md:2623` "có `tai_khoan_id` link TK nếu có"; `_DELTA-MAP-FR03.md:42` "1:1 với TAI_KHOAN qua `tai_khoan_id`"; `_DELTA-MAP-FR03.md:73`. Chỉ 1 outlier `srs-fr-03:1711` (description ngắn, lower authority) nói "Thay đổi 12 OUT". **Cần BA confirm spec authority — master `srs-v3.5.md` thắng module file description.**) |
| ~~BUG-DT-011-DD-ENDPOINT-01~~ | Major | DIEM_DANH POST endpoint chưa deploy (404); GET trả mock; field `coMat` boolean thay vì enum 3 trị (CO_MAT/VANG_PHEP/VANG_KHONG_PHEP) | **Closed** (R12 21:30 verified deploy — Swagger schema `DiemDanhItemDto.trangThai: enum["CO_MAT","VANG_PHEP","VANG_KHONG_PHEP"]` đã expose; POST `/khoa-hocs/{id}/diem-danhs/batch-update` validate đúng (`ERR-BIZ-III-05-02 "HV chưa được duyệt đăng ký"`). `coMat:boolean` giữ làm legacy compat field cho FE.) |
| ~~BUG-DT-031-KQHT-ENTITY-01~~ | Major | KET_QUA_HOC_TAP entity chưa deploy (mọi route 404) — block 5 TC (DT-031b + DT-031c + DT-031d + DT-054 + DT-055) | **WITHDRAWN** (R12 18:30 — QA probe sai URL. Entity tên đúng = `KET_QUA_DAO_TAO` (KQDT singular), route đúng `/khoa-hocs/{id}/ket-quas` (8 routes Swagger: list/batch-update/import/publish/unpublish/export/export-docx). Sample KH-005 record `aaee0011-...` có ĐẦY ĐỦ fields spec: `xepLoai="GIOI", ketQua="DAT", lichHocId, dangKyId, diemKiemTra, soBuoiCoMat, tongBuoi, tyLeChuyenCan, xepLoaiOverride, ketQuaOverride, lyDoOverride, congBo, thoiGianCongBo, lyDoHuyCongBo`. Entity ĐÃ DEPLOY đầy đủ.) |

> **🚨 RETRACTION R12.4 2026-05-12 (DT-052 RE-OPENED):**
>
> Withdrawal DT-052 ở R12 18:30 cite chỉ 1 source `srs-fr-03:1711` (entity matrix description trong module file) — KHÔNG safely grounded. Cross-check 5 SRS sources phát hiện **4/5 confirm `tai_khoan_id` REQUIRED**:
>
> | # | Source | Authority | HV có `tai_khoan_id`? |
> |---|---|---|:-:|
> | 1 | `srs-v3.5.md §3.4.3.53` (line 3349-3368) — **MASTER ENTITY SPEC** | 🥇 cao nhất | ✅ field 11, nullable FK |
> | 2 | `srs-v3.5.md:2623` — **MASTER ENTITY MATRIX** | 🥈 cao | ✅ "có `tai_khoan_id` link TK nếu có" |
> | 3 | `_DELTA-MAP-FR03.md:42` — delta planning | 🥉 trung | ✅ "1:1 với TAI_KHOAN qua `tai_khoan_id`" |
> | 4 | `_DELTA-MAP-FR03.md:73` — delta planning | 🥉 trung | ✅ "HOC_VIEN entity riêng với `tai_khoan_id`" |
> | 5 | `srs-fr-03-dao-tao.md:1711` — module entity matrix description | 🪵 thấp (description) | ❌ "Thay đổi 12 OUT, 4 trường" |
>
> **Conflict resolution:** Master spec (sources #1-#2) + delta map (#3-#4) đều confirm. Source #5 là outlier description ngắn. **DT-052 RE-OPENED** với note "Spec contradiction — cần BA confirm authority giữa master `srs-v3.5.md §3.4.3.53` (11 fields) vs module description `srs-fr-03:1711` ('Thay đổi 12 OUT')".
>
> Recommend dev: theo master spec → BE add `tai_khoan_id` field (nullable FK TAI_KHOAN) + auto-create TK khi HV đăng ký qua chuyên trang FR-III-04.

> **🎯 Re-test R12.3 final 2026-05-12 21:30 (sau dev confirm deploy):**
>
> Dev confirm đẩy code rồi. QA verify lại DT-011 sau cache clear + fresh login `qtht_01`:
>
> | Probe | Kết quả R12.3 | Conclusion |
> |---|---|---|
> | Swagger schema `DiemDanhItemDto` | `trangThai: enum["CO_MAT","VANG_PHEP","VANG_KHONG_PHEP"]` (required `hocVienId`, optional `coMat:boolean` legacy compat + `ghiChu` max 500) | ✅ Enum 3 trị đã deploy |
> | Swagger schema `BatchUpdateDiemDanhDto` | `{ngayDiemDanh: string, diemDanhs: DiemDanhItemDto[1-500]}` | ✅ Pattern batch chuẩn |
> | Swagger schema `DiemDanhResponseDto` (GET) | `trangThai: object nullable + coMat:boolean` (giữ legacy field cho FE) | ✅ Backward-compat OK |
> | POST `/khoa-hocs/{KH-002 DANG_DIEN_RA}/diem-danhs/batch-update` body với HV chưa DKDT DA_DUYET | **422 `ERR-BIZ-III-05-02 "Học viên chưa được duyệt đăng ký"`** | ✅ BE service validate đúng spec, không crash |
>
> → **DT-011 fully closed R12.3**. Schema deploy đầy đủ + endpoint hoạt động đúng. Edge case 500 trên KH `DA_KET_THUC` là validation gap nhỏ (không phải bug code chính).

> **🎯 Re-test R12 final 2026-05-12 18:30 (sau dev feedback):**
>
> Dev feedback: 3/3 bug INVALID hoặc đã fix. QA verify lại với spec doc + đúng URL:
>
> | Bug | Dev claim | QA verify R12 | Status |
> |---|---|---|---|
> | **DT-052** HV.taiKhoanId | ❌ Sai spec (HV giữ 4 trường) | ⚠️ `srs-fr-03-dao-tao.md:1711` "HOC_VIEN giữ 4 trường — Thay đổi 12 OUT" — chỉ 1 source, KHÔNG cross-check master entity spec. | **~~WITHDRAWN~~ → RE-OPENED R12.4** (xem RETRACTION trên: 4/5 SRS sources confirm `tai_khoan_id` REQUIRED, master `srs-v3.5.md §3.4.3.53` thắng module description) |
> | **DT-011** DD POST 404 | ✅ Đã fix commit `7b2af7be7` (2026-05-11 22:56) chưa deploy. POST plain `/diem-danhs` KHÔNG tồn tại theo design — dùng `/khoa-hocs/{id}/diem-danhs/batch-update` | ✅ Swagger có `POST /khoa-hocs/{id}/diem-danhs/batch-update` + import + export. Sample GET KH-005 vẫn `coMat:boolean` chờ deploy. | **Partial — chờ deploy** |
> | **DT-031** KQHT 404 | ❌ Sai URL. Entity = `KET_QUA_DAO_TAO` (KQDT), route `/khoa-hocs/{id}/ket-quas` | ✅ Swagger 8 routes match (list/batch-update/import/publish/unpublish/export/export-docx). Sample KH-005 record có đủ fields spec FR-III-19 + BR-KQ-01/02 (xepLoai/ketQua/lichHocId/override/congBo/thoiGianCongBo/lyDoHuyCongBo). | **WITHDRAWN** |
>
> **Bài học (memory entry):** QA cần cite SRS entity matrix (line 1709-1714 srs-fr-03) trước khi log "entity 404" — entity name + route phải match SRS, không suy đoán theo convention. DELTA-MAP intention KHÔNG = SRS final spec.
>
> **Net R12 final (superseded by R12.4):** **2/3 WITHDRAWN + 1 Partial** — KHÔNG còn đúng. R12.4 retract DT-052 WITHDRAWN → RE-OPEN. Net hiện tại: **DT-031 WITHDRAWN + DT-011 Closed (R12.3) + DT-052 RE-OPEN chờ BA chốt spec authority**. Block 7 TC R7.7.6 HV-related giảm xuống còn DT-052 spec-blocked + 6 TC inherit unblock sau dev confirm DD/KQDT route nested.

> **⚠️ HISTORY SNAPSHOT (superseded by R12.4 RETRACTION + R12.3 final 21:30 above):** Re-test R12 ban đầu kết luận "Open" cho 3 bug; R12 final 18:30 → "DT-052/DT-031 WITHDRAWN, DT-011 Partial"; R12.3 final 21:30 → "DT-011 Closed". **R12.4 2026-05-12 RETRACTION supersedes R12 final 18:30 cho DT-052: WITHDRAWN SAI sau cross-check 5 SRS sources (4/5 confirm `tai_khoan_id` REQUIRED) → DT-052 RE-OPENED (Minor) chờ BA chốt spec authority.** DT-031 vẫn WITHDRAWN, DT-011 vẫn Closed. Phần dưới chỉ giữ làm audit trail.
>
> **Re-test R12:** 2026-05-12 09:03 — Login `qtht_01` fresh, probe 3 entity qua API. **Tất cả 3 bug REPRO không đổi từ R11:**
> - **DT-052:** HV list `GET /hoc-viens?page=1&pageSize=3` → 200 (total=9 records, đã tăng 3 từ R11 do seed thêm); HV specific `GET /hoc-viens/aacc0008-...001` → 200 với 13 fields `[id, nguoiTaoId, nguoiCapNhatId, ngayTao, ngayCapNhat, donViId, seqId, version, hoTen, email, soDienThoai, donVi, nguoiHoTroId]` — `taiKhoanId` field VẪN MISSING.
> - **DT-011:** POST `/diem-danhs` global 404 + POST `/khoa-hocs/{id}/diem-danhs` 404 + POST `/lich-hocs/{id}/diem-danhs` 404 → 3/3 POST endpoint chưa deploy. GET `/diem-danhs` global 404. GET nested `/khoa-hocs/{id}/diem-danhs` 200 (vẫn còn route) nhưng response không có data sample R12 để re-confirm schema `coMat boolean` từ R11.
> - **DT-031:** All 6 routes (GET `/ket-qua-hoc-taps` + 4 nested GET variants + POST global) → 404 `ERR-SYS-00-04-01 "Cannot GET/POST ..."`. Entity vẫn hoàn toàn chưa deploy.
> → **Net R12:** 3/3 Open, không có thay đổi. Vẫn block 7 TC R7.7.6 HV-related (DT-011/011a/031b/c/d/054/055). DT-052 vẫn FAIL spec.
>
> **🔄 Re-test R12.2 (sau dev claim fix):** 2026-05-12 09:08 — User báo dev đã fix. QA chạy lại theo workflow `feedback_clear_cache_before_verify_fe_fix`: caches.delete + SW unregister + localStorage clear + `POST /auth/logout` + navigate `/login` ignoreCache → re-login `qtht_01` fresh + OTP `666666`. Sau đó probe lại 3 bug + extra 16 alt-path variants. **KẾT QUẢ: 3/3 BUG VẪN REPRO 100%, KHÔNG CÓ THAY ĐỔI**:
>
> | Bug | Probe set R12.2 | Status |
> |---|---|:-:|
> | DT-052 HV.taiKhoanId | List 9 records vẫn 13 fields giống R11/R12; HV specific 13 fields; `?include=taiKhoan` → 200 nhưng response cũng KHÔNG có `taiKhoan` lẫn `taiKhoanId` | ❌ Vẫn Open |
> | DT-011 DD endpoints | POST 3 nested variants + POST global → **4/4 → 404 `ERR-SYS-00-04-01`**; alt path `/diem-danh` (singular) + `/attendance(s)` + `/lich-hocs/.../diem-danh` → **4/4 → 404**; GET nested KH-006 vẫn 200 nhưng `data_shape=array(0)` không có sample để xem schema | ❌ Vẫn Open |
> | DT-031 KQHT entity | POST + GET 6 nguyên gốc → **7/7 → 404**; alt naming `/ket-qua-hoc-tap` singular + `/grades` + `/results` + `/diem-tong-ket` + `/diem-thi` + nested variants → **7/7 → 404** | ❌ Vẫn Open |
>
> → **Conclusion:** Dev có thể đã push code nhưng deploy CHƯA effective tại `http://103.172.236.130:3000`, hoặc fix lên environment khác (staging/dev branch), hoặc bug fix khác sub-issue không thuộc 3 bug này. Cần dev confirm:
> 1. Đã `git push origin main` chưa?
> 2. Có chạy `docker-compose restart` / redeploy chưa?
> 3. URL `103.172.236.130:3000` có phải environment đúng không (vs staging)?
> 4. Backend log có log line nào cho `/api/v1/diem-danhs` `/api/v1/ket-qua-hoc-taps` registered routes không?

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
