# Kế Hoạch Kiểm Thử — Biểu mẫu (FR-09, SCR-VII-01..03)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-12
> **Revised 2026-05-12 12:50:00** — apply review gaps G2/G5/G11 + suggestion S2/S10. Bump 1.0 → 1.1. Xem §8 Changelog.
> **Nguồn dữ liệu**: LOCAL — `srs-v3/srs-fr-09-bieu-mau.md` + `srs-update-2026-5-5/srs-fr-09-bieu-mau.md` + `srs-update-2026-5-5/_DELTA-MAP-FR09.md`
> **SRS Reference**: FR-VII-01 → FR-VII-07 (UC 92-98), SCR-VII-01 (Quản lý Thư mục), SCR-VII-02 (Quản lý Biểu mẫu), SCR-VII-03 (Nhập Biểu mẫu Hàng loạt)
> **SOURCE MODE**: LOCAL — mọi BR / Error code / state machine cite line file local theo prefix `srs-update-2026-5-5/srs-fr-09-bieu-mau.md` (v3.5) hoặc `srs-v3/srs-fr-09-bieu-mau.md` (v3 baseline) hoặc `srs-update-2026-5-5/_DELTA-MAP-FR09.md`.

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ nguồn LOCAL + sibling-check ≥2 module (FR-02 Mẫu phản hồi, FR-04 TVV/CG, FR-05 Vụ việc) + BA sign-off trước khi viết TC detail.
>
> **v3.0 (2026-04-23):** Test plan này dùng cho **GĐ 3 Functional + Auth + Edge**. GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng, output `seed-checklist-bieu-mau.md` + `workflow-test-report-bieu-mau.md`. Happy path đã cover ở GĐ 2 — TC ở đây chủ yếu **negative + edge + auth + cross-module** + bộ TC nội bộ cho 4 trường công khai CR-01 mới.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module**: Thư viện Biểu mẫu (Nhóm VII) — 7 FR (FR-VII-01 → FR-VII-07), UC 92 – UC 98. FR-VII-08 (HĐ Tư vấn — UC163) đã tách sang `srs-fr-14-hop-dong-tv.md`, **KHÔNG nằm trong scope test plan này** (DELTA-MAP §1 "TÁCH HOP_DONG_TU_VAN sang srs-fr-14").
- **Bảng dữ liệu chính**: `BIEU_MAU` (3.4.3.37 — 21 trường, +4 trường công khai CR-01), `THU_MUC_BIEU_MAU` (3.4.3.38 — 11 trường, enum trạng thái thống nhất `NHAP/CONG_KHAI/AN`).
- **Bảng đính kèm**: `FILE_DINH_KEM` (polymorphic, dùng cho file biểu mẫu + ảnh đại diện + file công khai).
- **Bảng cấu hình tham chiếu**: `DANH_MUC WHERE loai='LINH_VUC_PL'` (FR-10).
- **Màn hình**: SCR-VII-01 (`/bieu-mau/thu-muc`), SCR-VII-02 (`/bieu-mau`), SCR-VII-03 (`/bieu-mau/import`).
- **API outbound**: `GET /api/v1/bieu-mau` (FR-VII-07, cho Cổng PLQG) — chỉ trả `cong_khai=1` (`srs-update-2026-5-5/srs-fr-09-bieu-mau.md:303-306`, rename CR-01).

**Phạm vi GĐ 3 trong file này** (theo template v3.0 §0):

- Negative validation: file format, file size, tên trùng, lĩnh vực không tồn tại, ngày lọc đảo, switch công khai thiếu trường công khai.
- Edge case: upload bị ngắt, file virus, sync Cổng PLQG fail, import vượt 50 file / 500MB.
- Auth & permission: 11 role × 6 action (xem permission matrix §2.3).
- Cross-module: phụ thuộc FR-10 (DANH_MUC LINH_VUC_PL), FR-16 (API outbound filter `cong_khai`), Cổng PLQG (publish/unpublish).
- 4 trường công khai mới CR-01: `cong_khai`, `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai` + 3 BR-PUBLIC-01/02/03.

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | SCR | File Test Case |
|---|---|---|---|---|---|---|
| 1 | FR-VII-01 | UC92 | Quản lý thư mục biểu mẫu (CRUD) | THU_MUC_BIEU_MAU | SCR-VII-01 | `01-TC-thu-muc-crud.md` |
| 2 | FR-VII-02 | UC93 | Tìm kiếm thư mục biểu mẫu | THU_MUC_BIEU_MAU | SCR-VII-01 | `02-TC-thu-muc-search.md` |
| 3 | FR-VII-03 | UC94 | Công khai / hủy công khai thư mục lên Cổng PLQG | THU_MUC_BIEU_MAU | SCR-VII-01 | `03-TC-thu-muc-publish.md` |
| 4 | FR-VII-04 | UC95 | Quản lý biểu mẫu (CRUD + upload + preview + tải về + Switch công khai CR-01) | BIEU_MAU | SCR-VII-02 | `04-TC-bieu-mau-crud.md` + `05-TC-bieu-mau-cong-khai-cr01.md` |
| 5 | FR-VII-05 | UC96 | Tìm kiếm biểu mẫu | BIEU_MAU | SCR-VII-02 | `06-TC-bieu-mau-search.md` |
| 6 | FR-VII-06 | UC97 | Import biểu mẫu hàng loạt (max 50 file / 500MB) | BIEU_MAU | SCR-VII-03 | `07-TC-bieu-mau-import.md` |
| 7 | FR-VII-07 | UC98 | API chia sẻ biểu mẫu công khai cho Cổng PLQG | BIEU_MAU | — | `08-TC-api-outbound.md` |
| — | — | — | Permission matrix 11 role × 6 action | — | All SCR | `09-TC-permission.md` |
| — | — | — | Edge / regression (CR-01 rename, enum migration THU_MUC) | — | All | `10-TC-edge-regression.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|---|---|---|---|
| QTHT | — | `qtht_01` (`_02` fallback, `_03` permission test) | Admin override scope, restore soft-delete, audit log |
| CB_NV_TW | TW | `cb_nv_tw_01` (`_02` fallback, `_03` permission test) | CRUD biểu mẫu scope TW (Cục Bổ trợ tư pháp - BTP) |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH), `cb_nv_bn_02` (BTC), `cb_nv_bn_03` (BCT) | CRUD scope đơn vị BN — verify data isolation cross-BN |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (AG), `cb_nv_dp_02` (BG), `cb_nv_dp_03` (BNI) | CRUD scope đơn vị ĐP — verify data isolation cross-ĐP |
| CB_PD_TW | TW | `cb_pd_tw_01` | Read scope TW (BR-FLOW-07: KHÔNG cần phê duyệt biểu mẫu → CB_PD chỉ READ) |
| CB_PD_BN | BN | `cb_pd_bn_01` (BKH) | Read scope BN — verify CB_PD KHÔNG được CRUD biểu mẫu |
| CB_PD_DP | ĐP | `cb_pd_dp_01` (AG) | Read scope ĐP — same as trên |
| DN | — | `9999999990` (DN Test 01 HN) | Read CONG_KHAI qua chuyên trang / Cổng PLQG (không truy cập backoffice) |
| NHT | — | `nht_01` (AG) | Read CONG_KHAI thuộc đơn vị NHT (theo BR-AUTH-08) |
| CG | — | `huongcg` (CG BTP-TW) | Read CONG_KHAI thuộc đơn vị CG |
| Cổng PLQG | — | (mTLS + JWT machine cert) | GET /api/v1/bieu-mau (FR-VII-07 outbound) |

> Reference: [input/users.csv](../../../input/users.csv), [input/test-accounts-isolation.csv](../../../input/test-accounts-isolation.csv), [output/permission-matrix.md](../../../output/permission-matrix.md).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ **Quy định điền bảng:**
> - Cột "Ngoại lệ SRS-quoted" chỉ điền khi SRS có dòng ngoại lệ cụ thể (quote nguyên văn + cite line).
> - Để trống nếu không có ngoại lệ — nghĩa là **BR áp dụng 100%** cho module này.
> - BR đánh dấu `[CR-01]` là BR mới do bản v3.5 thêm để cover 4 trường công khai chuyên trang.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|---|---|---|---|---|---|
| BR-AUTH-01 | Xác thực 2-tier — Tier 1 (nội bộ + TOTP) cho CB/QTHT, Tier 2 (SSO VNeID OIDC) cho DN/TVV/CG/NHT. Không có VNPT eKYC. | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:877` | ✅ Yes | API outbound không yêu cầu session (dùng JWT mTLS) — áp riêng cho FR-VII-07 | Login precondition, TC permission |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` cho mọi bảng có cột này — không có exception ngoại trừ QTHT | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:883` | ✅ Yes (BIEU_MAU.don_vi_id + THU_MUC_BIEU_MAU.don_vi_id) | AUDIT_LOG không có phân quyền (immutable) | TC permission cross-don_vi (T-PERM-01..03) |
| BR-DATA-01 | Soft delete — set `is_deleted=1`, không xóa vật lý | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:889` | ✅ Yes (THU_MUC_BIEU_MAU + BIEU_MAU) | AUDIT_LOG: không xóa | TC DELETE = UPDATE is_deleted, TC restore QTHT |
| BR-DATA-03 | 7 common fields (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:895` | ✅ Yes | AUDIT_LOG: chỉ có id, thoi_gian, entity fields | TC verify DDL + payload |
| BR-DATA-05 | Audit trail mọi CUD + publish/unpublish + tải về | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:901` | ✅ Yes (PUBLISH/UNPUBLISH/TAI_BIEU_MAU/BULK_IMPORT) | — | TC verify AUDIT_LOG INSERT-only |
| BR-DATA-07 | Pagination default 20 rows/page, max 100 | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:907` | ✅ Yes | Dashboard: không phân trang (n/a) | TC pagination boundary 20/100/101 |
| BR-FLOW-05 | Công khai qua API trực tiếp tới Cổng PLQG (REST trực tiếp, không qua LGSP) | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:913` | ✅ Yes | "Biểu mẫu nhóm VII: công khai KHÔNG cần phê duyệt" — ngoại lệ với phần "chỉ bản ghi đã duyệt mới được công khai" | TC publish thư mục + biểu mẫu, TC API call → Cổng |
| BR-FLOW-07 | Biểu mẫu nhóm VII: công khai trực tiếp, KHÔNG cần phê duyệt. CB NV tự chịu trách nhiệm. | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:919` | ✅ Yes | — | TC publish không qua step phê duyệt, TC verify CB_PD KHÔNG có nút approve |
| BR-PUBLIC-01 `[CR-01]` | BIEU_MAU không có quy trình PD → được công khai bất kỳ lúc nào. Bản ghi đã xóa: KHÔNG được công khai. | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:925` | ✅ Yes | — | TC bật Switch khi BIEU_MAU bị xóa → từ chối; TC bật Switch khi NHAP → OK |
| BR-PUBLIC-02 `[CR-01]` | Tắt Switch công khai: set `cong_khai=0` + clear `thoi_gian_dang_tai=NULL` + gọi API gỡ khỏi Cổng PLQG | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:931` | ✅ Yes | — | TC tắt Switch verify timestamp NULL + API DELETE call |
| BR-PUBLIC-03 `[CR-01]` | `thoi_gian_dang_tai` auto fill = NOW() khi set `cong_khai=1`. Không cho sửa tay. | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:937` | ✅ Yes | — | TC verify timestamp auto khi bật + input field disabled/hidden |
| BR-EC-01 | Optimistic Locking — UPDATE conflict trả ERR-SYS-02 | `srs-v3/srs-v3.md:4066` (cross-cutting) | ✅ Yes | — | TC 2 CB NV edit cùng biểu mẫu → conflict |
| BR-EC-13 | Search sanitize max 200 ký tự, escape SQL/XSS | `srs-v3/srs-v3.md:4078` (cross-cutting) | ✅ Yes | — | TC search keyword 201 ký tự / SQL injection / XSS |
| BR-DATA-06 | Export Excel max 10k rows | `srs-v3/srs-v3.md:3977` (cross-cutting) | ✅ Yes (SCR-VII-01 nút "Xuất Excel") | — | TC export 10k + filter-aware |

> **Bổ sung:** BR-FLOW-05 ngoại lệ cần test cụ thể — "Biểu mẫu nhóm VII: công khai KHÔNG cần phê duyệt" theo `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:913` cột "Ngoại lệ" và BR-FLOW-07 mặc định.

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity | Nguồn |
|---|---|---|---|---|
| ERR-TM-01 | Tên thư mục trùng trong cùng đơn vị | "Thư mục '{tên}' đã tồn tại trong đơn vị" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:130` |
| ERR-TM-02 | Xóa thư mục có biểu mẫu chưa xóa | "Thư mục chứa {N} biểu mẫu, không thể xóa" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:131` |
| ERR-TM-03 | Tên thư mục vượt 500 ký tự | "Tên thư mục tối đa 500 ký tự" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:132` |
| ERR-TM-04 | Lĩnh vực PL không tồn tại trong DANH_MUC | "Lĩnh vực PL không tồn tại" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:133` |
| ERR-TK-01 | tu_ngay > den_ngay khi tìm kiếm | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:198` |
| ERR-CK-01 | Công khai thư mục rỗng (0 biểu mẫu) | "Thư mục chưa có biểu mẫu, không thể công khai" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:252` |
| ERR-CK-02 | API Cổng PLQG lỗi (timeout / 5xx) | "Lỗi kết nối Cổng PLQG. Vui lòng thử lại sau" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:253` |
| WRN-CK-01 | Công khai thư mục đã ở CONG_KHAI | "Thư mục đã ở trạng thái công khai" | WARNING | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:254` |
| ERR-BM-01 | File format không thuộc doc/docx/xls/xlsx | "Chỉ chấp nhận file doc, docx, xls, xlsx" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:344` |
| ERR-BM-02 | File vượt 20MB | "File vượt quá giới hạn 20MB. Kích thước: {size}MB" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:345` |
| ERR-BM-03 | Tên biểu mẫu trống | "Tên biểu mẫu là bắt buộc" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:346` |
| ERR-BM-04 | File bị lỗi/corrupt | "File không hợp lệ hoặc bị hỏng" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:347` |
| ERR-BM-05 | Thư mục đích không tồn tại / đã xóa | "Thư mục đích không tồn tại" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:348` |
| ERR-BM-06 | Upload bị ngắt giữa chừng (mất mạng) | "Upload bị gián đoạn, vui lòng thử lại" | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:383` (EC-01) |
| ERR-BM-07 | File chứa macro virus | (Theo EC-02 — system message thực tế) | ERROR | `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:384` (EC-02) |
| ERR-IMP-01 | Bulk import: tất cả file lỗi | "Không có file nào hợp lệ để import" | ERROR | `srs-v3/srs-fr-09-bieu-mau.md:464` |
| WRN-IMP-01 | Bulk import: 1 phần file lỗi | "Import thành công {N} file. {M} file lỗi: xem chi tiết" | WARNING | `srs-v3/srs-fr-09-bieu-mau.md:465` |
| ERR-IMP-02 | Bulk import > 50 file/lần | "Tối đa 50 file mỗi lần import" | ERROR | `srs-v3/srs-fr-09-bieu-mau.md:466` |
| ERR-IMP-03 | Bulk import tổng dung lượng > 500MB | "Tổng dung lượng tối đa 500MB" | ERROR | `srs-v3/srs-fr-09-bieu-mau.md:467` |
| 401 / 429 / 500 | API outbound FR-VII-07 JWT lỗi / rate limit / 5xx | `{"error":"Unauthorized"}` / `{"error":"Too many requests"}` / `{"error":"Internal server error"}` | ERROR | `srs-v3/srs-fr-09-bieu-mau.md:533-535` |

> ⚠️ Message phải quote nguyên văn — khi test negative, expected message match exact. Không "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). Bảng dưới chỉ extract entry FR-09.

| Entity / Action | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | CG | TVV |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| THU_MUC_BIEU_MAU — Create | ✅ | ✅ scope TW | ✅ scope BN | ✅ scope ĐP | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| THU_MUC_BIEU_MAU — Read (own scope) | ✅ all | ✅ TW | ✅ BN | ✅ ĐP | ✅ TW (read-only) | ✅ BN (read-only) | ✅ ĐP (read-only) | R CONG_KHAI | R CONG_KHAI | R CONG_KHAI | R CONG_KHAI |
| THU_MUC_BIEU_MAU — Update / Delete | ✅ | ✅ scope | ✅ scope | ✅ scope | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| THU_MUC_BIEU_MAU — Publish / Unpublish (FR-VII-03) | ✅ | ✅ scope | ✅ scope | ✅ scope | ❌ (BR-FLOW-07 không cần PD) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| BIEU_MAU — Create / Update / Delete | ✅ | ✅ scope | ✅ scope | ✅ scope | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| BIEU_MAU — Read (own scope) | ✅ all | ✅ TW | ✅ BN | ✅ ĐP | ✅ TW | ✅ BN | ✅ ĐP | R CONG_KHAI | R CONG_KHAI | R CONG_KHAI | R CONG_KHAI |
| BIEU_MAU — Toggle Switch `cong_khai` (CR-01) | ✅ | ✅ scope | ✅ scope | ✅ scope | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| BIEU_MAU — Download (TAI_BIEU_MAU) | ✅ | ✅ scope | ✅ scope | ✅ scope | ✅ scope | ✅ scope | ✅ scope | ✅ CONG_KHAI | ✅ CONG_KHAI | ✅ CONG_KHAI | ✅ CONG_KHAI |
| BIEU_MAU — Bulk Import (FR-VII-06) | ✅ | ✅ scope | ✅ scope | ✅ scope | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| API outbound `/api/v1/bieu-mau` (FR-VII-07) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a — chỉ Cổng PLQG qua mTLS + JWT |

**Ghi chú:**
- `scope` = `don_vi_id` của user — theo BR-AUTH-08. QTHT override toàn bộ.
- CB_PD_* KHÔNG có quyền publish/unpublish vì BR-FLOW-07 quy định biểu mẫu KHÔNG cần phê duyệt → vai trò Phê duyệt không can thiệp lifecycle BIEU_MAU.
- DN/NHT/CG/TVV chỉ Read các bản ghi `cong_khai=1` qua chuyên trang public hoặc Cổng PLQG outbound.

### 2.4 UI Layout (SCR-VII-01, SCR-VII-02, SCR-VII-03)

> ⚠️ **CẢNH BÁO:** Components trích từ SCR-VII-01..03 (file SRS v3.5). KHÔNG dùng absence để khẳng định "module KHÔNG có X" — cross-check §2.1 BR table trước.

#### SCR-VII-01 — Quản lý Thư mục Biểu mẫu (`/bieu-mau/thu-muc`)

**Toolbar:**
- Breadcrumb: "Trang chủ > Biểu mẫu > Thư viện biểu mẫu"
- Buttons: `[+ Thêm thư mục]` `[Xuất Excel]` `[Làm mới]`

**Filter-bar:**
- Search-box keyword (tên thư mục / mô tả)
- Select "Lĩnh vực PL" (load từ FR-10 `DANH_MUC WHERE loai='LINH_VUC_PL'`)
- Select "Trạng thái" (Tất cả / NHAP / CONG_KHAI / AN)
- Date-range picker "Khoảng ngày tạo"

**Content/Table:**
- Tab: Tất cả / Đã công khai / Nháp / Đã ẩn (kèm số đếm)
- Checkbox chọn hàng loạt
- Cột: Tên thư mục (icon expand → biểu mẫu trong) / Lĩnh vực / Số biểu mẫu (auto) / Trạng thái (badge NHAP xanh dương / CONG_KHAI xanh lá / AN đen) / Hành động
- Action bar khi chọn nhiều: `[Công khai hàng loạt] [Ẩn hàng loạt] [Xóa hàng loạt]`
- Hành động trên row: `[Công khai]` (khi NHAP/AN, có ≥1 BM) / `[Ẩn]` (khi CONG_KHAI) / `[Sửa]` / `[Xóa]` (khi NHAP/AN, rỗng)

**Form (drawer phải, tạo/sửa):**
- Tên thư mục (text, Y, max 500, unique per đơn vị)
- Lĩnh vực (select, Y, từ FR-10)
- Mô tả (textarea, N, max 2000)
- Thứ tự hiển thị (number, N, 1-20)

#### SCR-VII-02 — Quản lý Biểu mẫu (`/bieu-mau`)

**Toolbar:**
- `[+ Thêm biểu mẫu]` `[Nhập hàng loạt]`

**Filter-bar:**
- Search keyword + select Lĩnh vực / Loại hình / Thư mục / Định dạng

**Content/Table:**
- Cột: Mã BM auto / Tên / Loại tài liệu (icon) / Thư mục (link) / Kích thước / Trạng thái / Sync Cổng (Đã ĐB / Chờ / Lỗi) / Hành động (Xem trước / Tải về / Sửa / Xóa)
- Cột bổ sung CR-01: "Đã công khai" (Switch read-only) + "Ảnh đại diện" (thumbnail)

**Form (drawer phải, tạo/sửa):**
- Thư mục (select, Y)
- Tên biểu mẫu (text, Y, max 500)
- Lĩnh vực (select, N) / Loại hình (text, N) / Mô tả nội bộ (textarea long, N) / Thứ tự (number 1-20, N)
- File đính kèm (file-upload, Y, doc/docx/xls/xlsx, max 20MB, quét virus ClamAV)
- **Switch "Công khai trên Cổng PLQG"** `[CR-01]` — toggle `cong_khai`
- Khi Switch BẬT, expand 4 trường công khai:
  - Ảnh đại diện (file-upload jpg/png/gif, max 5MB, N — mặc định ảnh hệ thống) `[CR-01]`
  - Mô tả công khai (textarea long, N — tách biệt với mô tả nội bộ) `[CR-01]`
  - File đính kèm công khai (file[], N — PDF/DOC/DOCX/XLS/XLSX, max 20MB/file) `[CR-01]`
  - `thoi_gian_dang_tai` hiển thị read-only auto fill khi Lưu (BR-PUBLIC-03) `[CR-01]`

#### SCR-VII-03 — Nhập Biểu mẫu Hàng loạt (`/bieu-mau/import`) — Wizard

- Bước 1: Chọn thư mục đích + Tải file Excel metadata (`.xlsx` max 5MB, có nút `[Tải mẫu Excel]`) + multi-upload file nội dung (max 50 file, ≤20MB/file, tổng ≤500MB)
- Bước 2: Bảng kiểm tra (STT / Tên file / Định dạng / Kích thước / Trạng thái Hợp lệ-Lỗi)
- Label thống kê: "Tổng: {N} file. Hợp lệ: {X}. Lỗi: {Y}"
- Nút `[Xác nhận nhập {X} file hợp lệ]`

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**

- ☑ Nút `[Xuất Excel]` trên toolbar SCR-VII-01 (BR-DATA-06).
- ☑ Pagination 20/page default cả SCR-VII-01 + SCR-VII-02 (BR-DATA-07).
- ☑ Search sanitize max 200 chars + escape SQL/XSS (BR-EC-13).
- ☑ Audit log mọi CUD + PUBLISH + UNPUBLISH + TAI_BIEU_MAU + BULK_IMPORT (BR-DATA-05).
- ☑ Optimistic lock mọi UPDATE/DELETE (BR-EC-01).
- ☑ URL sync filter (BR-UX-01 — nếu áp dụng).

**Feature module KHÔNG có (cần QUOTE SRS):**

- KHÔNG có nút "Phê duyệt biểu mẫu" — `srs-update-2026-5-5/srs-fr-09-bieu-mau.md:919` BR-FLOW-07: "công khai trực tiếp, KHÔNG cần phê duyệt".
- KHÔNG có quản lý phiên bản (version control) — DELTA-MAP §6 T7: "UC97 Công khai biểu mẫu cá nhân OUT". 02-thu-tu-module.md:296 ghi "Upload version mới" nhưng SRS v3.5 KHÔNG có entity `BIEU_MAU_VERSION` → SPEC-CLARIFY-09-V1 ticket trước khi viết TC.
- KHÔNG có field `thu_tu_hien_thi` persist — DELTA-MAP §6 T8 BA chốt OUT: "xuất hiện ở Inputs/form nhưng KHÔNG persist". Test verify UI hiển thị input nhưng giá trị KHÔNG lưu → log SPEC-CLARIFY-09-V2.

### 2.5 State Machine — SM-BIEUMAU

**Entity:** BIEU_MAU (đồng thời áp cho THU_MUC_BIEU_MAU enum mới sau migration v3.5 — DELTA-MAP §1 "Đồng bộ enum trạng thái THU_MUC_BIEU_MAU")
**Tham chiếu FR:** FR-VII-01 → FR-VII-07 (`srs-update-2026-5-5/srs-fr-09-bieu-mau.md:816-848`).

```
[*] --> NHAP        : CB NV tạo (FR-VII-01 / FR-VII-04)
NHAP --> CONG_KHAI  : CB NV công khai (FR-VII-03, BR-FLOW-07)
CONG_KHAI --> AN    : CB NV ẩn (FR-VII-03)
AN --> CONG_KHAI    : CB NV công khai lại (FR-VII-03, BR-FLOW-07)
NHAP --> XOA        : CB NV xóa (guard: chưa công khai)
AN --> XOA          : CB NV xóa
```

**Bảng trạng thái:**

| Trạng thái | Mã | Mô tả |
|---|---|---|
| NHAP | draft | Mới tạo, chưa công khai. Default khi tạo. |
| CONG_KHAI | published | Đã công khai, DN/Cổng PLQG có thể xem/tải. `cong_khai=1` + `thoi_gian_dang_tai` set. |
| AN | hidden | Bị ẩn khỏi chuyên trang. Vẫn còn trong DB. `cong_khai=0`. |
| XOA | archived | Soft-delete (`is_deleted=1`). Chỉ QTHT restore. |

**Bảng chuyển trạng thái — chi tiết transitions:**

| Từ | Đến | Trigger | Guard | Action | FR | BR |
|---|---|---|---|---|---|---|
| [*] | NHAP | CB NV tạo biểu mẫu/thư mục | — | INSERT, `cong_khai=0`, `thoi_gian_dang_tai=NULL` | FR-VII-01 / FR-VII-04 | BR-DATA-03 |
| NHAP | CONG_KHAI | CB NV bật Switch / nhấn "Công khai" | Thư mục có ≥1 BM (FR-VII-03); BIEU_MAU không bị xóa (BR-PUBLIC-01) | `cong_khai=1`, `thoi_gian_dang_tai=NOW()`, API push Cổng | FR-VII-03 (thư mục) / FR-VII-04 (BIEU_MAU Switch) | BR-FLOW-07, BR-PUBLIC-01, BR-PUBLIC-03 |
| CONG_KHAI | AN | CB NV ẩn / tắt Switch | — | `cong_khai=0`, `thoi_gian_dang_tai=NULL`, API gỡ Cổng | FR-VII-03 / FR-VII-04 | BR-PUBLIC-02 |
| AN | CONG_KHAI | CB NV công khai lại | — | `cong_khai=1`, `thoi_gian_dang_tai=NOW()`, API push Cổng | FR-VII-03 / FR-VII-04 | BR-FLOW-07, BR-PUBLIC-03 |
| NHAP | XOA | CB NV xóa | Chưa từng công khai | `is_deleted=1`, audit log | FR-VII-01 / FR-VII-04 | BR-DATA-01 |
| AN | XOA | CB NV xóa | — | `is_deleted=1`, audit log | FR-VII-01 / FR-VII-04 | BR-DATA-01 |
| CONG_KHAI | (no direct) | — | — | Phải đi qua AN trước (UNPUBLISH) — không cho xóa thẳng khi đang công khai (EC-04 — gọi API gỡ trước) | — | EC-04 |

> **Lưu ý:** XOA là state kết thúc archived. Chỉ QTHT có thể restore (set `is_deleted=0`). DELTA-MAP §1 chốt `THU_MUC_BIEU_MAU` cùng dùng enum `NHAP/CONG_KHAI/AN` thay vì `KICH_HOAT/VO_HIEU_HOA` cũ → TC migration regression bắt buộc.

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|---|---|---|
| **GĐ 1 Seed (pure entry state)** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `bieu_mau_variants[1..6]` (sau apply rename `cong_khai`) + `thu_muc_bieu_mau_variants[1..6]` |
| **GĐ 1 click flow** | [`input/quy-trinh-nghiep-vu/flow-module.md`](../../../input/quy-trinh-nghiep-vu/flow-module.md) | §FR-09 Bước 1 (thủ công CB NV upload đơn lẻ + bulk import) |
| **GĐ 2 Workflow** | [`input/quy-trinh-nghiep-vu/02-thu-tu-module.md`](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §④ FR-09 line 276-302 | Bảng CRUD flow + Công khai Switch (line 298) + Đẩy API Cổng PLQG FR-16 |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | Verify BIEU_MAU + THU_MUC_BIEU_MAU "Tạo tại / Đọc tại" — sau move HOP_DONG_TU_VAN sang FR-14 |

**Upstream dependencies (Tier check):**

| Entity module | Tier | Phụ thuộc entity (upstream) | Seed trước tại module |
|---|:-:|---|---|
| THU_MUC_BIEU_MAU | 2 | `DANH_MUC WHERE loai='LINH_VUC_PL'`, `DON_VI` | FR-10 (QTHT seed DM + đơn vị) |
| BIEU_MAU | 2 | THU_MUC_BIEU_MAU (cùng module), `DANH_MUC WHERE loai='LINH_VUC_PL'`, `DON_VI` | FR-09 (thư mục trước), FR-10 |
| FILE_DINH_KEM (polymorphic) | — | (cha BIEU_MAU/THU_MUC_BIEU_MAU) | n/a — auto tạo cùng BIEU_MAU |

> **Lưu ý:** KHÔNG hardcode `N records, states X/Y` ở đây — fixture đã chốt 6 variants/entity. Workflow advance state là việc của GĐ 2 (workflow-test-report-bieu-mau.md). Tier 2 nghĩa là cần FR-10 (QTHT) live trước.

---

## 3. Cấu Trúc File Test Case

```
docs/todo-test/fr-09-bieu-mau/
├── test-plan.md                              ← File này (overview)
├── 01-TC-thu-muc-crud.md                     ← FR-VII-01 CRUD + negative
├── 02-TC-thu-muc-search.md                   ← FR-VII-02 search + edge (date đảo, no result)
├── 03-TC-thu-muc-publish.md                  ← FR-VII-03 publish/unpublish + ERR-CK-01/02 + WRN-CK-01
├── 04-TC-bieu-mau-crud.md                    ← FR-VII-04 CRUD core + ERR-BM-01..05 + EC-01..04
├── 05-TC-bieu-mau-cong-khai-cr01.md          ← FR-VII-04 4 trường công khai CR-01 + BR-PUBLIC-01/02/03 + Switch flow
├── 06-TC-bieu-mau-search.md                  ← FR-VII-05 search + filter combination
├── 07-TC-bieu-mau-import.md                  ← FR-VII-06 bulk import + ERR-IMP-01..03 + WRN-IMP-01
├── 08-TC-api-outbound.md                     ← FR-VII-07 GET /api/v1/bieu-mau + JWT/mTLS/rate limit
├── 09-TC-permission.md                       ← 11 role × 6 action permission matrix
├── 10-TC-edge-regression.md                  ← CR-01 rename regression, enum migration THU_MUC, cross-module FR-10
└── (11-REVIEW-edge-case-hunter.md)           ← Optional: review từ bmad-review-edge-case-hunter
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File | Happy | Negative | Edge | Tổng |
|---|---:|---:|---:|---:|
| 01-TC-thu-muc-crud (TM-001..006) | 1 | 4 | 1 | 6 |
| 02-TC-thu-muc-search (TM-007..009) | 1 | 1 | 1 | 3 |
| 03-TC-thu-muc-publish (TM-010..013) | 1 | 2 | 1 | 4 |
| 04-TC-bieu-mau-crud (BM-001..010) | 2 | 5 | 3 | 10 |
| 05-TC-bieu-mau-cong-khai-cr01 (BM-CR-001..012) | 4 | 5 | 3 | 12 |
| 06-TC-bieu-mau-search (BM-011..013) | 1 | 1 | 1 | 3 |
| 07-TC-bieu-mau-import (IMP-001..006) | 1 | 3 | 2 | 6 |
| 08-TC-api-outbound (API-001..005) | 1 | 3 | 1 | 5 |
| 09-TC-permission (PERM-001..006) | — | 4 | 2 | 6 |
| 10-TC-edge-regression (REG-001..005) | — | 2 | 3 | 5 |
| **TỔNG** | **12** | **30** | **18** | **60** |

**TC ID đại diện (≥15 TC):**

| TC ID | File | Loại | Mô tả ngắn | FR | BR / ERR |
|---|---|---|---|---|---|
| TM-001 | 01 | Happy | CB_NV_TW tạo thư mục "HĐ Lao động" + lĩnh vực Lao động → PASS, badge NHAP | FR-VII-01 | BR-DATA-03 |
| TM-002 | 01 | Negative | Tên thư mục trùng trong cùng đơn vị → ERR-TM-01 | FR-VII-01 | ERR-TM-01 |
| TM-003 | 01 | Negative | Xóa thư mục có 1 biểu mẫu → ERR-TM-02 + count đúng | FR-VII-01 | ERR-TM-02 |
| TM-004 | 01 | Negative | Tên 501 ký tự → ERR-TM-03 | FR-VII-01 | ERR-TM-03 |
| TM-005 | 01 | Negative | Chọn linh_vuc_id đã bị xóa ở FR-10 → ERR-TM-04 | FR-VII-01 | ERR-TM-04 |
| TM-006 | 01 | Edge | Soft delete = UPDATE is_deleted, QTHT restore được | FR-VII-01 | BR-DATA-01 |
| TM-007 | 02 | Happy | Tìm "Lao động" + lĩnh vực + tu_ngay → kết quả AND logic | FR-VII-02 | — |
| TM-008 | 02 | Negative | tu_ngay > den_ngay → ERR-TK-01 | FR-VII-02 | ERR-TK-01 |
| TM-009 | 02 | Edge | Keyword 201 ký tự → sanitize/reject (BR-EC-13) | FR-VII-02 | BR-EC-13 |
| TM-010 | 03 | Happy | CB_NV_TW publish thư mục 3 BM → CONG_KHAI + API call Cổng PLQG verify network | FR-VII-03 | BR-FLOW-07, BR-FLOW-05 |
| TM-011 | 03 | Negative | Publish thư mục rỗng → ERR-CK-01 | FR-VII-03 | ERR-CK-01 |
| TM-012 | 03 | Negative | Cổng PLQG trả 503 → ERR-CK-02 + rollback trạng thái | FR-VII-03 | ERR-CK-02 |
| TM-013 | 03 | Edge | Re-publish thư mục đã CONG_KHAI → WRN-CK-01 idempotent | FR-VII-03 | WRN-CK-01 |
| BM-001 | 04 | Happy | Upload file .docx 5MB hợp lệ → PASS, preview render | FR-VII-04 | — |
| BM-002 | 04 | Happy | Upload file .xlsx 19.9MB → PASS boundary | FR-VII-04 | — |
| BM-003 | 04 | Negative | Upload .pdf → ERR-BM-01 | FR-VII-04 | ERR-BM-01 |
| BM-004 | 04 | Negative | Upload .docx 20.1MB → ERR-BM-02 | FR-VII-04 | ERR-BM-02 |
| BM-005 | 04 | Negative | Tên biểu mẫu để trống → ERR-BM-03 | FR-VII-04 | ERR-BM-03 |
| BM-006 | 04 | Negative | File corrupt (header sai) → ERR-BM-04 | FR-VII-04 | ERR-BM-04 |
| BM-007 | 04 | Negative | Thư mục đích bị xóa trước khi Lưu → ERR-BM-05 | FR-VII-04 | ERR-BM-05 |
| BM-008 | 04 | Edge | Upload ngắt mạng giữa chừng → ERR-BM-06 + blob mồ côi cleanup | FR-VII-04 | EC-01 |
| BM-009 | 04 | Edge | File .docx chứa macro virus → ERR-BM-07 ClamAV reject | FR-VII-04 | EC-02 |
| BM-010 | 04 | Edge | 2 CB NV edit cùng BIEU_MAU đồng thời → ERR-SYS-02 (optimistic lock) | FR-VII-04 | BR-EC-01 |
| BM-CR-001 | 05 | Happy | CB_NV_TW tạo BM + bật Switch + nhập đủ 4 trường công khai → `cong_khai=1`, `thoi_gian_dang_tai=NOW()`, ảnh + mo_ta_cong_khai persist | FR-VII-04 | BR-PUBLIC-01, BR-PUBLIC-03 |
| BM-CR-002 | 05 | Happy | Đang CONG_KHAI tắt Switch → `cong_khai=0`, `thoi_gian_dang_tai=NULL`, API gỡ Cổng | FR-VII-04 | BR-PUBLIC-02 |
| BM-CR-003 | 05 | Happy | Switch tắt mặc định khi tạo mới — 4 trường công khai ẩn | FR-VII-04 | — |
| BM-CR-004 | 05 | Negative | Sửa tay `thoi_gian_dang_tai` qua API → 400/403 reject (BR-PUBLIC-03) | FR-VII-04 | BR-PUBLIC-03 |
| BM-CR-005 | 05 | Negative | Upload ảnh đại diện .pdf → reject (chỉ jpg/png/gif) | FR-VII-04 | — (constraint field) |
| BM-CR-006 | 05 | Negative | Upload ảnh đại diện 5.1MB → reject | FR-VII-04 | — |
| BM-CR-007 | 05 | Edge | BM bị soft-delete → bật Switch qua API → BR-PUBLIC-01 reject "không công khai bản ghi xóa" | FR-VII-04 | BR-PUBLIC-01 |
| BM-CR-008 | 05 | Edge | Tắt Switch nhưng Cổng PLQG 5xx → atomic rollback (giữ `cong_khai=1` + `thoi_gian_dang_tai` cũ, KHÔNG set `cong_khai=0` partial); toast retry. **G5 — escalate BA SPEC-CLARIFY-09-V3 trước test: spec BR-PUBLIC-02 line 931 ghi 3 action nhưng KHÔNG nói order/atomic guarantee khi API gỡ fail** | FR-VII-04 | EC-04, BR-PUBLIC-02 |
| BM-CR-009 | 05 | Edge | `mo_ta_cong_khai` ≠ `mo_ta` nội bộ — render chuyên trang chỉ thấy `mo_ta_cong_khai` | FR-VII-04 / FR-VII-07 | CR-01 D.2 |
| BM-CR-010 | 05 | Negative | **G2** — Upload `.pdf` vào field `file` chính (file biểu mẫu) → reject ERR-BM-01 (enum chỉ `doc/docx/xls/xlsx`, line 300) | FR-VII-04 | ERR-BM-01 |
| BM-CR-011 | 05 | Happy | **G2** — Upload `.pdf` 10MB vào field `file_dinh_kem_cong_khai` (khi Switch BẬT) → PASS (enum `PDF/DOC/DOCX/XLS/XLSX`, line 306+769). Verify 2 enum khác nhau giữa 2 field. | FR-VII-04 | CR-01 D.4 |
| BM-CR-012 | 05 | Negative | **G11** — Field `loai_hinh` constraint: nếu form là dropdown 4 enum `HOP_DONG/BIEU_MAU/MAU_DON/KHAC` (SRS line 761 CHECK constraint) thì verify ko cho free-text "HĐ lao động"; nếu form free-text → log SPEC-CLARIFY-09-V4 (line 761 ≠ form line 297). **Escalate BA trước test** | FR-VII-04 | line 761 |
| BM-011 | 06 | Happy | Search keyword + filter Lĩnh vực + Loại hình → AND result | FR-VII-05 | — |
| BM-012 | 06 | Negative | Keyword SQL injection `' OR 1=1` → sanitize, INF-BM-TK-01 | FR-VII-05 | BR-EC-13 |
| BM-013 | 06 | Edge | Pagination page=999 vượt total → trang trống, không lỗi | FR-VII-05 | BR-DATA-07 |
| IMP-001 | 07 | Happy | Upload 10 file hợp lệ → 10 thành công | FR-VII-06 | — |
| IMP-002 | 07 | Negative | Upload 51 file → ERR-IMP-02 | FR-VII-06 | ERR-IMP-02 |
| IMP-003 | 07 | Negative | Upload 30 file tổng 501MB → ERR-IMP-03 | FR-VII-06 | ERR-IMP-03 |
| IMP-004 | 07 | Negative | Upload toàn .pdf 10 file → ERR-IMP-01 + báo cáo chi tiết | FR-VII-06 | ERR-IMP-01 |
| IMP-005 | 07 | Edge | Mix 7 hợp lệ + 3 lỗi → WRN-IMP-01 + bảng chi tiết lỗi | FR-VII-06 | WRN-IMP-01 |
| IMP-006 | 07 | Edge | Audit log ghi BULK_IMPORT count = N (verify INSERT-only) | FR-VII-06 | BR-DATA-05 |
| API-001 | 08 | Happy | GET /api/v1/bieu-mau mTLS + JWT valid → 200 + JSON shape items[] + total + page | FR-VII-07 | — |
| API-002 | 08 | Negative | JWT expired → 401 Unauthorized | FR-VII-07 | API spec |
| API-003 | 08 | Negative | Rate limit > threshold → 429 | FR-VII-07 | API spec |
| API-004 | 08 | Negative | mTLS cert mismatch → reject TCP | FR-VII-07 | BR-AUTH-01 |
| API-005 | 08 | Edge | Filter `cong_khai=1` (verify rename CR-01) — chỉ trả CONG_KHAI, không trả NHAP/AN/XOA | FR-VII-07 | CR-01 rename |
| PERM-001 | 09 | Negative | CB_PD_TW thử POST /thu-muc → 403 (BR-FLOW-07 quy định CB_PD chỉ read) | FR-VII-01 | BR-FLOW-07 |
| PERM-002 | 09 | Negative | CB_NV_BN BKH thử GET thư mục của BTC → 403 (BR-AUTH-08 isolation) | FR-VII-01..02 | BR-AUTH-08 |
| PERM-003 | 09 | Negative | DN gọi backoffice `/bieu-mau` (non-public) → 403 | FR-VII-04 | BR-AUTH-08 |
| PERM-004 | 09 | Negative | NHT thử bật Switch công khai BIEU_MAU → 403 | FR-VII-04 | BR-AUTH-08 |
| PERM-005 | 09 | Edge | QTHT override scope cross-đơn vị → READ + restore là PASS, nhưng publish 1 BM của BN nào khác phải log audit `bypass_unit=true` | FR-VII-* | BR-AUTH-08 ngoại lệ QTHT |
| PERM-006 | 09 | Edge | CG download CONG_KHAI từ đơn vị BTP-TW → PASS chỉ Read | FR-VII-04 | BR-AUTH-08 |
| REG-001 | 10 | Negative | Tìm field `la_cong_khai` trong API response → KHÔNG được trả về (đã rename `cong_khai`) | FR-VII-04/07 | CR-01 rename |
| REG-002 | 10 | Negative | THU_MUC trạng thái `KICH_HOAT` cũ migration → phải migrate thành `NHAP` | FR-VII-01 | DELTA-MAP §1 enum |
| REG-003 | 10 | Edge | URL cũ `/bieu-mau/hop-dong-tu-van` → 404 hoặc redirect `/hop-dong-tv` (đã move sang FR-14) | — | DELTA-MAP §3 |
| REG-004 | 10 | Edge | SM-BIEUMAU transition `NHAP → CONG_KHAI` test FR ref đúng FR-VII-03 (không phải FR-VII-02) | FR-VII-03 | DELTA-MAP §5 |
| REG-005 | 10 | Edge | Verify `thu_tu_hien_thi` UI nhập nhưng KHÔNG persist (SPEC-CLARIFY-09-V2) | FR-VII-01 / FR-VII-04 | DELTA-MAP §6 T8 |

**Phân bổ priority:**

| Priority | Số TC | % |
|---|---:|---:|
| P0 (bắt buộc — happy path + auth + CR-01 core) | 22 | 39% |
| P1 (quan trọng — negative chính + edge core) | 25 | 44% |
| P2 (nên có — edge phụ + regression) | 10 | 17% |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 + 90% P1 pass + 0 Critical bug Open.
- ⚠️ **PASS WITH CONCERNS:** P0 100% + P1 ≥80% + ≤1 Major Open có workaround.
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 80%, hoặc ≥1 Critical Open.

**Bug severity guideline cho FR-09:**

- **Critical:** Schema `la_cong_khai` chưa rename (data migration fail); API outbound trả bản ghi `cong_khai=0`; **API outbound trả bản ghi `is_deleted=1` (soft-deleted leak ra public chuyên trang) — S2, verify filter `is_deleted=0 AND cong_khai=1` line 540**; mất file biểu mẫu sau upload thành công; CB_PD bypass được BR-FLOW-07 (approve flow rò rỉ); permission isolation thủng (BN-BKH thấy BN-BTC).
- **Major:** Switch CR-01 không auto-fill `thoi_gian_dang_tai`; bulk import vượt giới hạn 50/500MB không reject; preview docx fail mọi file; ERR-CK-02 không rollback trạng thái.
- **Minor:** Toast text không đúng SRS quote; pagination edge page=0; thumbnail ảnh đại diện render sai khi không upload (mặc định hệ thống).

**Gate cứng CR-01 (S10):** ngoài 100% P0, **BM-CR-001..004** (toggle Switch BẬT + 4 trường công khai persist + auto timestamp + tắt Switch clear timestamp + Switch tắt mặc định + sửa tay timestamp reject) BẮT BUỘC PASS clean. Nếu CR-01 core fail → release **BLOCK**, không qua được criteria PASS dù P0 khác đạt 100%.

---

## 6. Tham chiếu

- [input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md](../../../input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md) — SRS v3.5 (source of truth chính)
- [input/srs-v3/srs-fr-09-bieu-mau.md](../../../input/srs-v3/srs-fr-09-bieu-mau.md) — SRS v3 baseline (cross-reference FR-VII-06 import line)
- [input/srs-update-2026-5-5/_DELTA-MAP-FR09.md](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR09.md) — Delta map cho 6 thay đổi v3→v3.5
- [input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md](../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) line 1010-1127 — chi tiết CR-01 + tách HĐ TV
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §④ FR-09 (line 276-302) — workflow CRUD + Switch công khai
- [tasks/system-overview.md §4.5](../../../tasks/system-overview.md) (line 284-304) — Module 4 Biểu mẫu UI summary 3 SCR
- [input/users.csv](../../../input/users.csv) — 11 role test account (qtht_01..10, cb_nv_tw/bn/dp_01..10, cb_pd_*_01..10, dn 9999999990, nht_01, huongcg)
- [output/permission-matrix.md](../../../output/permission-matrix.md) — 49 entity × 11 role
- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể
- [output/template/test-plan-overview-template.md](../../../output/template/test-plan-overview-template.md) — template gốc

---

## 7. Ambiguity / Open issues defer khi test

Theo `_DELTA-MAP-FR09.md` §6 + cross-check 02-thu-tu-module.md:

- **T7 — UC97 "Công khai biểu mẫu cá nhân":** BA chốt OUT 2026-05-06 — field `cong_khai` chỉ set qua form FR-VII-04 hoặc cascade thư mục FR-VII-03. Defer phiên bản sau. KHÔNG viết TC cho UC97 personal mode.
- **T8 — Field `thu_tu_hien_thi`:** xuất hiện ở Inputs/form nhưng KHÔNG persist (không có entity column). BA chốt OUT. → Viết TC REG-005 verify gap + log SPEC-CLARIFY-09-V2 nếu UI vẫn cho nhập.
- **02-thu-tu-module.md line 296 "Upload version mới":** SRS v3.5 KHÔNG có entity `BIEU_MAU_VERSION` → SPEC-CLARIFY-09-V1, defer TC version control cho đến khi BA confirm.
- **THU_MUC_BIEU_MAU không có 4 CPF công khai** (DELTA-MAP §6 D.2): chỉ rename `la_cong_khai → cong_khai`. Thư mục KHÔNG có ảnh đại diện / mô tả công khai riêng. → KHÔNG viết TC 4 trường cho thư mục.
- **HOP_DONG_TU_VAN tách FR-14:** TC HĐ TV viết ở plan FR-14 (`docs/todo-test/fr-14-hop-dong-tv/test-plan.md` khi có). KHÔNG cite FR-09 nữa.

---

*Plan generated 2026-05-12 từ SRS v3.5 LOCAL + DELTA-MAP-FR09 — sẵn sàng cho BA sign-off trước khi viết TC detail 01-10.*

---

## 8. Changelog

### v1.1 — Revised 2026-05-12 12:50:00 (apply review gaps)

Apply ≥80% gap từ `review.md` (REVISE verdict). Adopt 5 critical gap + 3 suggestion:

- **G2** — Thêm 2 TC mới `BM-CR-010` (PDF reject ở field `file` chính) + `BM-CR-011` (PDF accept ở field `file_dinh_kem_cong_khai`) — phân biệt rõ 2 enum constraint khác nhau giữa 2 field (line 300 vs line 306+769). Risk dev nhầm 1 enum chung.
- **G5** — Update `BM-CR-008` thêm wording atomic rollback + escalate BA SPEC-CLARIFY-09-V3 trước test: BR-PUBLIC-02 line 931 không nói order/atomic guarantee khi API Cổng PLQG gỡ fail.
- **G11** — Thêm TC `BM-CR-012` verify `loai_hinh` form là dropdown 4 enum hay free-text — line 761 CHECK constraint vs line 297 form free-text "HĐ lao động". Escalate BA SPEC-CLARIFY-09-V4 trước test.
- **S2** — Bug severity guideline §5 bổ sung Critical case "API outbound trả `is_deleted=1` leak" (verify filter `is_deleted=0 AND cong_khai=1` line 540).
- **S10** — §5 Tiêu chí PASS/FAIL thêm "Gate cứng CR-01": BM-CR-001..004 PASS clean = release gate cứng. CR-01 core fail → block release dù P0 khác đạt 100%.

**Tổng TC sau revise:** 57 → 60 TC (+3 BM-CR-010/011/012).

### Defer / open issues sau revise

- **G1** (REG-006 version control no-version proof) — defer. SRS v3.5 không có `BIEU_MAU_VERSION`, defer SPEC-CLARIFY-09-V1 chốt OUT. Sẽ add TC sau khi BA confirm cycle 2.
- **G3** (virus scan MIME spoof / ZIP bomb / async detection) — skip cycle 1, raise security backlog. Cần liên hệ infra ClamAV config trước.
- **G4** (`mo_ta_cong_khai` max length boundary) — defer SPEC-CLARIFY-09-V5. Trong khi chờ BA test với 10k ký tự là happy path.
- **G6/G7/G8/G9/G10/G12** — defer cycle 2 sau khi BA sign-off v1.1. Không block sign-off.
- **S1/S3/S4/S5/S6/S7/S8/S9** — backlog v1.2. S8 (`thu_tu_hien_thi` SPEC-CLARIFY-09-V2) raise ngay khi gửi v1.1 BA review.
