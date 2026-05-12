# Kế Hoạch Kiểm Thử — Doanh nghiệp (FR-07, SCR-V.III-01..03)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-12 11:30:00
> **Revised**: 2026-05-12 12:25:00 — applied review.md feedback (số trường lock 22+7, MISS cross-module quy_mo→FR-06, Xuất Excel contradiction escalate BA, thêm TC negative email/nguoi_dai_dien/tong_nguon_von, dep state-explicit).
> **Source mode**: LOCAL (đọc file trong `input/srs-v3/` và `input/srs-update-2026-5-5/`)
> **SRS Reference**: FR-V.III-01, FR-V.III-02, ~~FR-V.III-NEW-01~~ (đã bỏ v3.5), SCR-V.III-01, SCR-V.III-02, ~~SCR-V.III-03~~ (dead spec)
> **Module nhóm**: V.III — Quản lý DN được Hỗ trợ
> **Delta map**: `input/srs-update-2026-5-5/_DELTA-MAP-FR07.md`

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module:** Quản lý Doanh nghiệp được Hỗ trợ Pháp lý (HTPL) — entity trung tâm `DOANH_NGHIEP` ghi nhận hồ sơ DNNVV được hỗ trợ.
- **UC range:** UC81 (Quản lý DN) + UC82 (Tìm kiếm DN). UC mới Import Excel (UC ngoài CSV gốc) **đã bị BỎ** trong v3.5 (cite `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:17`).
- **Số FR:** 2 FR — FR-V.III-01 / FR-V.III-02 (giảm từ 3 FR ở v3 do bỏ FR-V.III-NEW-01).
- **Entity owned:** `DOANH_NGHIEP` (**22 attribute nghiệp vụ + 7 common fields = 29 cột DB**, cite `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:438-462`. UI SCR-V.III-02 render 28 component visible — gồm cả label/readonly Mã DN/file upload — KHÔNG đếm bằng số field. TC verify form đếm theo SCR line `:323-354` component, không theo "28 trường" nguyên văn), `DOANH_NGHIEP_LINH_VUC` (bảng nối M-N mới v3.5 — `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:474-487`).
- **Entity referenced:** `DON_VI`, `DANH_MUC` (loại `TINH_THANH` / `LOAI_DN` / `LINH_VUC_KINH_DOANH`), `TAI_KHOAN`, `VU_VIEC`, `HO_SO_CHI_TRA`, `HO_SO_PHAP_LY_DN`.
- **Màn hình test:**
  - SCR-V.III-01 — Danh sách DN — URL `/doanh-nghiep/danh-sach` (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:275`).
  - SCR-V.III-02 — Chi tiết / Chỉnh sửa DN — URL `/doanh-nghiep/:id` hoặc `/doanh-nghiep/:id/sua` (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:318`).
  - ~~SCR-V.III-03 Import DN từ Excel~~ — **không test** (BA chốt 2026-05-05 là dead spec, cite `_DELTA-MAP-FR07.md:99`).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity owned | File Test Case |
|---|---|---|---|---|---|
| 1 | FR-V.III-01 | UC81 | Quản lý DN được HTPL (xem/sửa/xóa, lịch sử hỗ trợ, hồ sơ PL DN, hồ sơ chi trả) | DOANH_NGHIEP, DOANH_NGHIEP_LINH_VUC | `01-TC-CRUD-doanh-nghiep.md` |
| 2 | FR-V.III-02 | UC82 | Tìm kiếm DN (tu_khoa, quy_mo, tinh_thanh_id, linh_vuc_ids[], khoảng ngày hỗ trợ) | DOANH_NGHIEP | `02-TC-tim-kiem-doanh-nghiep.md` |
| 3 | (cross-module) | (UC ngoài) | Verify dropdown DN ở module consumer (FR-05/06/08/12/14) chỉ thấy DN `is_deleted=0` + phạm vi đơn vị BR-AUTH-08 | DOANH_NGHIEP | `03-TC-cross-module-dropdown.md` |
| 4 | (cross-cutting) | — | Permission matrix + 2-tier BR-AUTH-08 (TW xem toàn quốc / BN/ĐP theo `tinh_thanh_id` đơn vị) | DOANH_NGHIEP | `04-TC-permission-matrix.md` |
| 5 | (negative + edge) | — | Negative + edge case (validate, MST trùng, CHECK constraint, soft-delete block) | DOANH_NGHIEP | `05-TC-negative-edge.md` |

> **Lưu ý:** Test plan này KHÔNG cover luồng tạo DN — DN được tạo qua self-registration FR-VIII-22 (`srs-update-2026-5-5/srs-fr-10-quan-tri.md:1005-1090`) → cover ở test plan FR-10. Test plan FR-07 chỉ cover Read/Update/Delete + Search + 4 tab chi tiết.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|---|---|---|---|
| QTHT | — | `qtht_01` | Admin smoke + verify Audit log (BR-DATA-05) |
| CB_NV_TW | TW | `cb_nv_tw_01` | CRUD chính scope TW (xem toàn quốc) |
| CB_NV_BN | BN | `cb_nv_bn_01` (BKH) | CRUD scope BN — verify BR-AUTH-08 |
| CB_NV_DP | ĐP | `cb_nv_dp_01` (STP-AG) | CRUD scope ĐP — verify chỉ thấy DN `tinh_thanh_id=AG` |
| CB_PD_TW | TW | `cb_pd_tw_01` | Read-only scope TW (verify quyền chỉ R) |
| CB_PD_DP | ĐP | `cb_pd_dp_01` | Read-only scope ĐP |
| DN (self) | — | `9999999990` (MST), `9999999991` | Verify DN không có quyền vào module CMS DN |
| NHT | ĐP | `nht_01` (STP-AG) | Verify NHT có quyền vào tab Hồ sơ PL DN không (FR-12 cross) |
| QTHT fallback | — | `qtht_02`, `qtht_03` | Account lock fallback (xem CLAUDE.md Rule 7) |

> Reference: [input/users.csv](../../../input/users.csv) — schema mới 2026-04-23, suffix `_01` primary / `_02` fallback / `_03` permission test dedicated.

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|---|---|---|:-:|---|---|
| BR-AUTH-01 | Mọi user phải xác thực trước khi truy cập hệ thống | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:519, 529-533` | ✅ Yes | — | Precondition mọi TC, TC unauthenticated → 401 redirect login |
| BR-AUTH-08 | Phân quyền theo đơn vị — 2 tầng: TW xem toàn quốc; BN/ĐP xem theo `tinh_thanh_id` thuộc đơn vị (BN không có ĐP trực thuộc) | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:276, 319, 377, 535-539` | ✅ Yes | — | TC permission cross-unit (CB NV ĐP-AG không thấy DN STP-BG) |
| BR-DATA-01 | Soft delete — đặt `is_deleted=1`, không hard delete | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:541-545` | ✅ Yes | — | TC DELETE: `is_deleted=1`, không còn trong list nhưng AUDIT_LOG giữ |
| BR-DATA-02 | Multi-tenant scoping — `don_vi_id` NOT NULL trên mọi bản ghi nghiệp vụ | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:547-551` | ✅ Yes | — | TC verify cột `don_vi_id` không NULL khi self-reg + sửa |
| BR-DATA-03 | Common fields — 7 trường (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:553-557` | ✅ Yes | — | TC verify response có đủ 7 field cross-cutting |
| BR-DATA-04 | Auto-gen mã DN theo format `DN-{TINH}-{SEQ}` — TINH lấy từ `tinh_thanh_id` (GSO 01-63) | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:559-563, 97, 102` | ✅ Yes | — | TC sửa DN không cho đổi `ma_doanh_nghiep`; TC verify format pattern |
| BR-DATA-05 | Audit trail — mọi CUD ghi vào `AUDIT_LOG`, immutable | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:134, 142, 565-569` | ✅ Yes | — | TC verify AUDIT_LOG INSERT khi sửa/xóa DN (giá trị cũ → mới) |
| BR-DATA-06 | Export Excel max 10k rows (mặc định toàn dự án) | global Phụ lục B (sibling FR-05/06/10) | ⚠️ **SPEC-CLARIFY-FR07-05** | **Contradiction nội tại SRS:** Lịch sử thay đổi line 17 nói "BỎ chức năng Xuất Excel khỏi FR-V.III-01" nhưng SCR-V.III-01 line 284 vẫn list nút Xuất Excel. ESCALATE BA trước khi chạy TC. Nếu BỎ → drop DN-022/023. Nếu giữ → áp full BR-DATA-06. | TC export happy + filter-aware + 10k boundary (chỉ chạy sau BA chốt) |
| BR-DATA-07 | Pagination default 20 rows/page, max 100 | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:126, 233, 571-575` | ✅ Yes | — | TC pagination — verify `page_size=20`, max=100, page 2/3 nhảy đúng |
| BR-CALC-05 | Kiểm tra quy mô DNNVV (NĐ39/2018) — auto-suggest `SIEU_NHO` / `NHO` / `VUA` dựa vào `so_lao_dong` + `doanh_thu_nam` + `tong_nguon_von` | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:42-46, 158, 309, 577-581` | ✅ Yes | — | TC auto-suggest quy mô; TC WARNING `WRN-DN-01` khi user override |
| BR-AUTH-EMAIL-01 | Email DN KHÔNG UNIQUE — khác `TAI_KHOAN.email` (kênh login). Tự đăng ký set bằng TK; có thể đổi không cần OTP | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:449` | ✅ Yes | — | TC verify đổi `email` DN không bắt OTP; TC verify 2 DN trùng `email` được phép |
| BR-EC-01 | Optimistic Locking — 2 user sửa cùng 1 DN → user sau nhận `ERR-SYS-02` | global Phụ lục B (cite `srs-v3.md:4066`) | ✅ Yes | — | TC 2 tab cùng sửa DN, save tab sau → conflict |
| BR-EC-13 | Search sanitize max 200 ký tự (chống SQL/XSS) | global Phụ lục B (cite `srs-v3.md:4078`) | ✅ Yes | — | TC search ô `tu_khoa` >200 ký tự bị truncate; payload `<script>` không exec |
| BR-FK-LINH-VUC | `linh_vuc_ids[]` lưu vào `DOANH_NGHIEP_LINH_VUC` bảng M-N — UNIQUE(`doanh_nghiep_id`, `linh_vuc_id`) | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:113, 222, 350, 485` | ✅ Yes | — | TC multi-select 1/2/N lĩnh vực; TC chọn trùng cùng lĩnh vực → 409 hoặc dedupe |
| BR-DN-SOFT-DEL-BLOCK | Không xóa DN nếu còn `VU_VIEC` đang xử lý (state ≠ HOAN_THANH/HUY) | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:138-142, 187` | ✅ Yes | — | TC delete DN có VV đang `DANG_XU_LY` → `ERR-DN-03` |
| BR-FK-TINH-THANH | `tinh_thanh_id` FK → `DANH_MUC` loai='TINH_THANH', mã GSO 01-63 theo QĐ 124/2004/QĐ-TTg | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:102, 221, 335, 447` | ✅ Yes | — | TC dropdown Tỉnh/TP có 63 options; TC chọn mã ngoài 01-63 → 400 |
| BR-CHECK-CONSTRAINTS | CHECK DB: `so_lao_dong ≥ 0`, `so_lao_dong_nu ≤ so_lao_dong`, `so_lao_dong_khuyet_tat ≤ so_lao_dong`, `doanh_thu ≥ 0`, `tong_nguon_von ≥ 0` | `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:464-470` | ✅ Yes | — | TC nhập số âm bị reject 400 (full 5 trường — bao gồm `tong_nguon_von < 0` line 469) |
| BR-CALC-CHITRA-DN | Đổi `quy_mo` DN (NHO ↔ VUA) → công thức chi trả % VV của DN có recompute không (cross-module FR-06) | `srs-update-2026-5-5/srs-fr-06-chi-tra.md` (check BR-CALC-04) + `_DELTA-MAP-FR07.md` | ⚠️ **SPEC-CLARIFY-FR07-06** | Cần BA confirm cascade recompute hay snapshot tại thời điểm tạo VV. Nếu recompute → cần test. | TC `DN-041` (mới) — xem §4 |

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity | TC áp dụng |
|---|---|---|---|---|
| ERR-DN-01 | Tên DN rỗng khi save | "Tên doanh nghiệp là bắt buộc" (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:184`) | ERROR | TC negative ten_doanh_nghiep=blank |
| ERR-DN-02 | MST trùng DN khác trong hệ thống | "Mã số thuế đã tồn tại" (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:185`) | ERROR | TC update DN nhập MST của DN khác |
| WRN-DN-01 | Quy mô user chọn không khớp số liệu LĐ/doanh thu (NĐ39/2018) | "Quy mô {X} không khớp với số liệu lao động/doanh thu. Vẫn lưu?" (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:186`) | WARNING | TC auto-suggest gợi NHO, user override VUA → warning |
| ERR-DN-03 | Xóa DN có VV đang xử lý | "Không thể xóa DN đang có vụ việc xử lý" (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:187`) | ERROR | TC delete DN còn VV `DANG_XU_LY` |
| INF-DN-TK-01 | Search không có kết quả | "Không tìm thấy doanh nghiệp phù hợp" (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:257`) | INFO | TC search MST không tồn tại → empty state |
| ERR-SYS-02 | Optimistic lock conflict (2 user sửa cùng DN) | (Quote từ global Phụ lục B) | ERROR | TC concurrent edit |

> ⚠️ Mọi TC negative phải match **nguyên văn** message từ SRS. KHÔNG "close enough" accept. Nếu app trả message khác → log Minor severity (UI copy bug).

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). Bảng dưới là subset cho entity `DOANH_NGHIEP`.

| Action trên `DOANH_NGHIEP` | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN (self) | NHT | TVV | CG |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Read list (SCR-V.III-01) | ✅ Toàn quốc | ✅ Toàn quốc | ✅ Đơn vị BN | ✅ Đơn vị ĐP | ✅ Toàn quốc | ✅ Đơn vị BN | ✅ Đơn vị ĐP | ❌ | ✅ Đơn vị | ❌ | ❌ |
| Read detail (SCR-V.III-02) — 4 tab | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ chính DN mình | tab 1+2 | ❌ | ❌ |
| Create (POST) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ qua FR-VIII-22 self-reg | ❌ | ❌ | ❌ |
| Update (PUT/PATCH) | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | ❌ | ❌ | ❌ | ✅ chính DN mình (1 số field) | ❌ | ❌ | ❌ |
| Delete (soft, BR-DN-SOFT-DEL-BLOCK) | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Xuất Excel | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | ✅ | ✅ Đơn vị | ✅ Đơn vị | ❌ | ❌ | ❌ | ❌ |
| Tab Hồ sơ PL DN (CRUD HSPL — FR-12 cross) | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | R | R Đơn vị | R Đơn vị | R chính DN | CRUD (UC150) | ❌ | ❌ |
| Tab Lịch sử Hỗ trợ (Read VU_VIEC join) | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | ✅ | ✅ Đơn vị | ✅ Đơn vị | R chính DN | ❌ | ❌ | ❌ |
| Tab Hồ sơ Chi trả (Read HO_SO_CHI_TRA join) | ✅ | ✅ | ✅ Đơn vị | ✅ Đơn vị | ✅ | ✅ Đơn vị | ✅ Đơn vị | R chính DN | ❌ | ❌ | ❌ |

**Lưu ý quan trọng (v3.5):** CB NV ở MỌI cấp **đã bỏ quyền Create** DN. DN chỉ vào hệ thống qua self-registration FR-VIII-22 (cite `_DELTA-MAP-FR07.md:38` + `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:83`). TC permission phải verify nút `[Thêm mới]` KHÔNG tồn tại trên SCR-V.III-01 (cite line `:282-285` — toolbar chỉ có Xuất Excel + Làm mới).

### 2.4 UI Layout (SCR-V.III-01 + SCR-V.III-02)

**SCR-V.III-01 — Danh sách DN** (cite `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:280-303`):

- **Breadcrumb**: "Trang chủ > Doanh nghiệp > Danh sách"
- **Toolbar**: Tiêu đề "Quản lý Doanh nghiệp" + nút `[Xuất Excel]` + nút `[Làm mới]`. **KHÔNG có nút `[+ Thêm mới]`, KHÔNG có `[Import Excel]`** (v3.5 đã bỏ).
- **Filter-bar**: Từ khóa (tên/MST) | Quy mô (`SIEU_NHO/NHO/VUA`) | Tỉnh/TP (DANH_MUC TINH_THANH) | Lĩnh vực KD (multi-select v3.5 — line `:289`) | Từ ngày | Đến ngày | `[Tìm kiếm]` | `[Xóa bộ lọc]`.
- **Table** (8 cột): checkbox | Mã DN | Tên DN | MST | Quy mô (badge) | Địa chỉ (cắt 30 ký) | Số lần hỗ trợ | Tổng chi phí | Hành động (Xem/Sửa/Xóa).
- **Pagination**: 20/page (BR-DATA-07).

**SCR-V.III-02 — Chi tiết / Chỉnh sửa DN** (cite `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:323-354`):

- **4 tab dọc:**
  1. **Tab Thông tin cơ bản** — form **28 component visible** (verify theo SCR-V.III-02 bảng line `:323-354`, KHÔNG đếm theo entity 22 attribute): Mã DN auto / Tên / MST / Giấy CNĐKKD / Ngày cấp / Địa chỉ / Tỉnh / Loại DN / Quy mô auto-suggest / Ngành nghề / Số LĐ / Doanh thu năm / Tổng nguồn vốn / Người ĐD / Chức vụ ĐD / Email / SĐT / Fax / Phụ nữ làm chủ / Số LĐ nữ / Số LĐ khuyết tật / Lĩnh vực KD multi-select / Ghi chú / File đính kèm.
  2. **Tab Hồ sơ PL DN** (mới v2.1 gộp MH-12.3) — CRUD `HO_SO_PHAP_LY_DN` (entity FR-12), 5 loại × 3 trạng thái.
  3. **Tab Lịch sử Hỗ trợ** — list `VU_VIEC WHERE doanh_nghiep_id=:id` + 3 KPI (Tổng VV / VV hoàn thành / Tổng chi phí).
  4. **Tab Hồ sơ Chi trả** — list `HO_SO_CHI_TRA WHERE doanh_nghiep_id=:id`.
- **Action-bar**: `[Hủy]` + `[Lưu]`. **KHÔNG có chế độ tạo mới** — chỉ xem/sửa (cite `:317`).

**Cross-cutting features MẶC ĐỊNH có:**
- ⚠️ Nút `[Xuất Excel]` SCR-V.III-01 — **SPEC-CLARIFY-FR07-05** (Lịch sử thay đổi line 17 nói BỎ vs SCR line 284 vẫn render). Escalate BA.
- ☑ Pagination 20/page (BR-DATA-07).
- ☑ Search với sanitize max 200 chars (BR-EC-13).
- ☑ URL sync filter (BR-UX-01 default — KHÔNG có quote ngoại lệ).
- ☑ Audit log mọi CUD (BR-DATA-05).
- ☑ Optimistic lock mọi UPDATE (BR-EC-01).

**Feature module KHÔNG có (đã QUOTE SRS):**
- ❌ Nút `[+ Thêm mới]` SCR-V.III-01 — bỏ v3.5 (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:83, 282-285`).
- ❌ Nút `[Import Excel]` SCR-V.III-01 + cả SCR-V.III-03 — bỏ v3.5 (`_DELTA-MAP-FR07.md:13-15` + BA confirm 2026-05-05).
- ❌ Chế độ tạo mới SCR-V.III-02 — bỏ v3.5 (`srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:317`).
- ❌ 5 trường công khai chuẩn CR-01 (cong_khai / anh_dai_dien / thoi_gian_dang_tai / mo_ta_cong_khai / file_dinh_kem_cong_khai) — **KHÔNG áp dụng cho DN entity v3.5**. Grep `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md` không có mention → kết luận dứt khoát: CR-01 chỉ áp `VU_VIEC` (FR-05) + `TU_VAN_VIEN` (FR-04) line `:399`. KHÔNG test 5 trường này cho DN. SPEC-CLARIFY-FR07-01 hạ bậc thành "nhắc nhở" — chỉ cần BA xác nhận lần cuối, không block test.

### 2.5 State Machine (nếu có)

> Cite `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:503-507`: "Nhóm này không có state machine. Entity DOANH_NGHIEP không có vòng đời trạng thái (lifecycle) trong SRS. Bản ghi DN được tạo/sửa/xóa mềm trực tiếp."

→ **Không có SM lifecycle** cho `DOANH_NGHIEP`. Chỉ có flag `is_deleted` (soft delete) và liên kết gián tiếp đến state của `TAI_KHOAN` (DN tạo qua self-reg → TK `CHO_KICH_HOAT` → `HOAT_DONG`) ở FR-10.

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|---|---|---|
| **Seed danh mục dùng chung** | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | Phần `danh_muc_variants`: loại `TINH_THANH` (63 records GSO 01-63), `LOAI_DN` (UC105), `LINH_VUC_KINH_DOANH` (multi) |
| **Seed DN qua self-reg** | [`input/flow-module.md`](../../../input/flow-module.md) | §FR-10 Module 1 — FR-VIII-22 self-reg workflow (TK-first → kích hoạt mail → `HOAT_DONG`) |
| **Cross-module map** | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | DOANH_NGHIEP "Tạo tại": FR-10 self-reg; "Đọc tại": FR-05/06/07/08/12/14 dropdown |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|---|:-:|---|---|
| DOANH_NGHIEP | 2 | DANH_MUC (TINH_THANH/LOAI_DN/LINH_VUC_KINH_DOANH), DON_VI, TAI_KHOAN | FR-10 Quản trị (danh mục + cây đơn vị) |
| DOANH_NGHIEP_LINH_VUC | 2 | DOANH_NGHIEP + DANH_MUC(LINH_VUC_KINH_DOANH) | FR-10 (DM lĩnh vực) + chính FR-07 (DN parent) |

**Tiền điều kiện seed cho test plan này** (format state-explicit theo CLAUDE.md "State marker workflow"):

- `[need: ≥6 DOANH_NGHIEP trạng_thái=HOAT_DONG (verify GET /doanh-nghiep?trang_thai=HOAT_DONG count≥6); phân bố 2 ĐP-AG / 2 BN (BKH+BTC) / 2 TW; tạo qua FR-VIII-22 self-reg — upstream FR-10 module]`
- `[need: ≥3 DOANH_NGHIEP quy_mo distinct (SIEU_NHO + NHO + VUA, verify GROUP BY quy_mo count≥1 mỗi giá trị); phục vụ filter quy_mo + cross-module FR-06 chi trả]`
- `[need: ≥2 DOANH_NGHIEP is_deleted=1 (verify GET /doanh-nghiep?include_deleted=1&is_deleted=1 count≥2); generate sau TC DN-006]`
- `[need: ≥1 DOANH_NGHIEP có VU_VIEC trạng_thai=DANG_XU_LY (verify GET /vu-viec?doanh_nghiep_id=X&trang_thai=DANG_XU_LY count≥1); phục vụ DN-007 ERR-DN-03 block xóa — upstream FR-05]`
- `[need: DANH_MUC loại=TINH_THANH đủ 63 record HOAT_DONG (GSO 01-63 theo QĐ 124/2004/QĐ-TTg, verify count=63); upstream FR-10 DM]`
- `[need: DANH_MUC loại=LINH_VUC_KINH_DOANH ≥5 record HOAT_DONG (verify count≥5); phục vụ multi-select DN-011/017 + FR-FK-LINH-VUC; upstream FR-10 DM]`
- `[need: DANH_MUC loại=LOAI_DN ≥3 record HOAT_DONG (UC105, verify count≥3); upstream FR-10 DM]`
- `[need: DON_VI ≥7 record (TW + 2 BN + 4 ĐP gồm STP-AG/STP-BG); upstream FR-10 cây đơn vị]`

---

## 3. Cấu Trúc File Test Case

```
docs/todo-test/fr-07-doanh-nghiep/
├── test-plan.md                          ← File này (overview)
├── 01-TC-CRUD-doanh-nghiep.md            ← Read/Update/Delete + 4 tab (FR-V.III-01)
├── 02-TC-tim-kiem-doanh-nghiep.md        ← Search 6 filter + pagination + sort (FR-V.III-02)
├── 03-TC-cross-module-dropdown.md        ← Dropdown DN ở FR-05/06/08/12/14 (regression)
├── 04-TC-permission-matrix.md            ← 11 role × 9 action (BR-AUTH-08 2-tier)
├── 05-TC-negative-edge.md                ← MST trùng / số âm / CHECK constraint / optimistic lock
└── (06-REVIEW-edge-case-hunter.md)       ← Optional: review bmad-review-edge-case-hunter
```

---

## 4. Tổng Quan Số Lượng Test Cases

| File / Nhóm TC | TC ID | Tên TC ngắn | Loại | Priority |
|---|---|---|:-:|:-:|
| `01-TC-CRUD-doanh-nghiep.md` | DN-001 | Xem danh sách DN — pagination default 20 | Happy | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-002 | Xem chi tiết DN — tab Thông tin cơ bản 28 trường | Happy | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-003 | Sửa DN — đổi tên + lưu — verify AUDIT_LOG ghi giá trị cũ → mới | Happy | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-004 | Sửa DN — auto-suggest quy mô khi nhập `so_lao_dong=5` + `doanh_thu=2tỷ` → gợi `SIEU_NHO` | Happy | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-005 | Sửa DN — user override quy mô → WARNING `WRN-DN-01` "Vẫn lưu?" | Negative | P1 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-006 | Xóa DN không có VV — soft delete `is_deleted=1`, AUDIT_LOG giữ | Happy | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-007 | Xóa DN có VV `DANG_XU_LY` → `ERR-DN-03` block | Negative | P0 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-008 | Tab Hồ sơ PL DN — CRUD `HO_SO_PHAP_LY_DN` (5 loại × 3 trạng thái) | Happy | P1 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-009 | Tab Lịch sử Hỗ trợ — 3 KPI khớp `VU_VIEC` của DN | Happy | P1 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-010 | Tab Hồ sơ Chi trả — list `HO_SO_CHI_TRA` của DN | Happy | P1 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-011 | Multi-select Lĩnh vực KD — chọn 3 lĩnh vực → 3 row `DOANH_NGHIEP_LINH_VUC` | Happy | P1 |
| `01-TC-CRUD-doanh-nghiep.md` | DN-012 | Đổi email DN — KHÔNG bắt OTP (BR-AUTH-EMAIL-01) | Happy | P2 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-013 | Search `tu_khoa` theo Tên DN partial match | Happy | P0 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-014 | Search `tu_khoa` theo MST exact | Happy | P0 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-015 | Filter `quy_mo=NHO` — chỉ trả DN quy mô NHO | Happy | P1 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-016 | Filter `tinh_thanh_id=01` (Hà Nội) | Happy | P1 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-017 | Filter `linh_vuc_ids[]` multi-select 2 lĩnh vực — logic AND/OR? **SPEC-CLARIFY-FR07-04** (SRS line 231 chỉ nói AND cross-field, không clarify trong-field) | Happy | P1 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-018 | Filter khoảng ngày hỗ trợ — chỉ DN có VV trong [tu_ngay, den_ngay] | Happy | P2 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-019 | Search MST không tồn tại → empty state `INF-DN-TK-01` | Negative | P1 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-020 | Search `tu_khoa` >200 ký tự — truncate sanitize (BR-EC-13) | Edge | P2 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-021 | Pagination — chuyển trang 2/3, page_size=20 (BR-DATA-07) | Happy | P0 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-022 | Xuất Excel filter-aware — **PENDING SPEC-CLARIFY-FR07-05** (BA chốt giữ hay bỏ) | Happy | P1 |
| `02-TC-tim-kiem-doanh-nghiep.md` | DN-023 | Xuất Excel >10k cap — **PENDING SPEC-CLARIFY-FR07-05** | Edge | P2 |
| `03-TC-cross-module-dropdown.md` | DN-024 | Dropdown DN ở FR-05 Vụ việc — chỉ thấy DN `is_deleted=0` thuộc đơn vị user | Cross | P0 |
| `03-TC-cross-module-dropdown.md` | DN-025 | Dropdown DN ở FR-06 Chi trả — verify scope | Cross | P1 |
| `03-TC-cross-module-dropdown.md` | DN-026 | Dropdown DN ở FR-12 TVCS — verify chỉ DN `HOAT_DONG` (TK đã kích hoạt) | Cross | P1 |
| `04-TC-permission-matrix.md` | DN-027 | CB_NV_DP (AG) chỉ thấy DN `tinh_thanh_id=AG` — không thấy DN BG (BR-AUTH-08) | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-028 | CB_NV_BN (BKH) thấy DN `tinh_thanh_id` thuộc BKH scope (không cross BTC) | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-029 | CB_NV_TW thấy toàn quốc, không lọc theo `tinh_thanh_id` | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-030 | CB_PD mọi cấp — chỉ Read, KHÔNG có nút Sửa/Xóa | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-031 | DN (self) `9999999990` — chỉ vào hồ sơ DN của mình, không thấy DN khác | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-032 | Verify nút `[+ Thêm mới]` KHÔNG tồn tại trên SCR-V.III-01 (v3.5) | Permission | P0 |
| `04-TC-permission-matrix.md` | DN-033 | Verify nút `[Import Excel]` KHÔNG tồn tại — dead spec SCR-V.III-03 | Permission | P0 |
| `05-TC-negative-edge.md` | DN-034 | Sửa DN — `ten_doanh_nghiep=blank` → `ERR-DN-01` | Negative | P0 |
| `05-TC-negative-edge.md` | DN-035 | Sửa DN — MST trùng DN khác → `ERR-DN-02` | Negative | P0 |
| `05-TC-negative-edge.md` | DN-036 | Sửa DN — `so_lao_dong=-5` → 400 CHECK constraint | Edge | P1 |
| `05-TC-negative-edge.md` | DN-037 | Sửa DN — `so_lao_dong_nu=10` + `so_lao_dong=5` → 400 CHECK | Edge | P1 |
| `05-TC-negative-edge.md` | DN-038 | Sửa DN — `tinh_thanh_id=99` (ngoài GSO 01-63) → 400 FK violation | Edge | P2 |
| `05-TC-negative-edge.md` | DN-039 | Concurrent edit — 2 tab cùng sửa, save tab sau → `ERR-SYS-02` (BR-EC-01) | Edge | P2 |
| `05-TC-negative-edge.md` | DN-040 | Search payload `<script>alert(1)</script>` — sanitize, không exec (BR-EC-13) | Edge | P1 |
| `05-TC-negative-edge.md` | DN-041 | Sửa DN — `email` format invalid (`abc@`, `abc.com`, blank) → 400 / message format | Negative | P1 |
| `05-TC-negative-edge.md` | DN-042 | Sửa DN — `nguoi_dai_dien=blank` (Y bắt buộc theo SRS Inputs line `:109`) → 400 / message | Negative | P0 |
| `05-TC-negative-edge.md` | DN-043 | Sửa DN — `tong_nguon_von=-100` → 400 CHECK constraint (BR-CHECK line `:469`) | Edge | P1 |
| `05-TC-negative-edge.md` | DN-044 | Sửa DN — `doanh_thu_nam=-50` → 400 CHECK constraint | Edge | P1 |
| `03-TC-cross-module-dropdown.md` | DN-045 | **Cross-module quy_mo → FR-06 chi trả** — đổi DN từ NHO → VUA, verify VV cũ chi trả % recompute hay snapshot (PENDING SPEC-CLARIFY-FR07-06) | Cross | P1 |

**Tổng cộng:** **45 TC** (≥15 yêu cầu).

**Phân bổ priority:**

| Priority | Số TC | % |
|---|---:|---:|
| P0 (bắt buộc) | 19 | 42.2% |
| P1 (quan trọng) | 18 | 40.0% |
| P2 (nên có) | 8 | 17.8% |
| **Tổng** | **45** | **100%** |

**Phân bổ loại:**

| Loại | Số TC | % |
|---|---:|---:|
| Happy path | 17 | 37.8% |
| Negative | 9 | 20.0% |
| Edge | 8 | 17.8% |
| Cross-module | 4 | 8.9% |
| Permission | 7 | 15.6% |
| **Tổng** | **45** | **100%** |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 (18/18) + ≥90% P1 (≥13/14) pass.
- ❌ **FAIL:** Bất kỳ P0 nào FAIL, hoặc P1 pass rate <90%.
- ⚠️ **Sai spec:** TC PASS nhưng lệch SRS (vd message UI khác `ERR-DN-01` quote → Minor severity log + tiếp tục).
- 🚫 **BLOCKED:** Thiếu seed (≥6 DN self-reg), thiếu DM TINH_THANH 63 records, thiếu DM LINH_VUC_KINH_DOANH ≥5 records, hoặc FR-VIII-22 self-reg chưa làm xong.

**SPEC-CLARIFY tickets cần BA confirm trước khi đóng test plan:**

- **SPEC-CLARIFY-FR07-01** (hạ bậc, không block test): DN có công khai hồ sơ ra Cổng PLQG không? Grep SRS FR-07 v3.5 KHÔNG có 5 trường CR-01 → kết luận KHÔNG áp dụng cho DN, chỉ áp `VU_VIEC` + `TU_VAN_VIEN`. BA xác nhận lần cuối.
- **SPEC-CLARIFY-FR07-02**: Migration DN cũ tạo bằng CB Nghiệp vụ trước v3.5 — có TK liên kết không, có cần migration script auto-tạo TK? (`_DELTA-MAP-FR07.md:104`)
- **SPEC-CLARIFY-FR07-03**: NHT có quyền vào tab Hồ sơ PL DN trong SCR-V.III-02 không? UC150 cho NHT nhập tay HSPL — nhưng permission entry-point có đi qua SCR-V.III-02 hay riêng SCR FR-12? **Move NHT row khỏi permission matrix chính, đặt vào "pending" tạm**.
- **SPEC-CLARIFY-FR07-04** (mới): `linh_vuc_ids[]` multi-select filter — AND hay OR giữa các option cùng field? SRS line 231 chỉ nói AND cross-field, không clarify trong-field.
- **SPEC-CLARIFY-FR07-05** (mới — **BLOCKING**): Xuất Excel BỎ hay GIỮ? Lịch sử thay đổi line 17 nói BỎ vs SCR-V.III-01 line 284 vẫn render nút. DN-022/023 PENDING.
- **SPEC-CLARIFY-FR07-06** (mới): Đổi `quy_mo` DN → công thức chi trả % VV cũ recompute hay snapshot? Cross-module FR-06. DN-045 PENDING.

**Permission row NHT** (line 105) — **move sang pending** chờ SPEC-CLARIFY-FR07-03, KHÔNG test trong round đầu để tránh false negative.

---

## 6. Tham chiếu

- **SRS chính (v3.5):** [input/srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md](../../../input/srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md) — 586 dòng, BA chốt 2026-05-06.
- **SRS gốc (v3.0):** [input/srs-v3/srs-fr-07-doanh-nghiep.md](../../../input/srs-v3/srs-fr-07-doanh-nghiep.md) — 681 dòng (reference cho phần Import Excel đã bỏ).
- **Delta map:** [input/srs-update-2026-5-5/_DELTA-MAP-FR07.md](../../../input/srs-update-2026-5-5/_DELTA-MAP-FR07.md) — 107 dòng, list module impact + question BA confirm.
- **Self-registration upstream:** [input/srs-update-2026-5-5/srs-fr-10-quan-tri.md](../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) — FR-VIII-22 (line 1005-1090) + FR-VIII-26 (line 1241-1312).
- **System overview:** [tasks/system-overview.md §4.3](../../../tasks/system-overview.md) — Module 2 Doanh nghiệp.
- **Thứ tự module:** [input/quy-trinh-nghiep-vu/02-thu-tu-module.md](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) §②FR-07.
- **Users CSV:** [input/users.csv](../../../input/users.csv) — 9 role × N record.
- **Permission matrix tổng:** [output/permission-matrix.md](../../../output/permission-matrix.md).
- **Template:** [output/template/test-plan-overview-template.md](../../../output/template/test-plan-overview-template.md).
- **Template TC:** [output/template/test-case-template.md](../../../output/template/test-case-template.md).
- **Template bug report:** [output/template/bug-report-template.md](../../../output/template/bug-report-template.md).

---

*Test plan generated 2026-05-12 11:30:00 — Plan Drafter agent (LOCAL source mode). Sibling-check chưa làm — cần đối chiếu §2.1 với test plan FR-05 + FR-12 trước khi BA sign-off.*
