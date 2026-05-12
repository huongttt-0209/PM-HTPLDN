# Kế Hoạch Kiểm Thử — Hợp đồng tư vấn (FR-14, SCR-X3-01)

> **Phiên bản**: 1.1 — Revised 2026-05-12 13:30:00 (apply review feedback ≥80%)
> **Ngày tạo**: 2026-05-12
> **Nguồn dữ liệu**: LOCAL — `input/srs-v3/srs-fr-14-hop-dong-tv.md` (baseline v3, KHÔNG có file v3.5)
> **SRS Reference**: Nhóm X.3 (FR-X.3-01, FR-X.3-02), SCR-X3-01
>
> **Revision 2026-05-12 13:30:00 — applied reviewer feedback:**
> - Escalated `SPEC-CLARIFY-HDTV-04` cho mâu thuẫn FK direction VV (input N:N vs ERD 1:N) + BR-HDTV-10 Bên A readonly ambiguous.
> - Re-classified TC-PERM-TVV-01 → P2 + tag `[SPEC-CLARIFY-HDTV-05]` (SRS không grant TVV/CG read HĐ; cite quy trình nghiệp vụ thay vì SRS BR).
> - Added TC-SEARCH-06 (SQL/XSS sanitize keyword) + TC-PAG-02 (boundary `?limit=101` reject — BR-DATA-07 max 100) + TC-TT-EDGE-03 (SUM=0 boundary) + TC-FILE-01 (file upload negative).
> - Inline `[SPEC-CLARIFY-HDTV-NN]` tag trong TC affected để tester grep nhanh khi BA reply.
> - §5 Tiêu chí đạt: phân loại 3 SPEC-CLARIFY theo nhóm **C** (Chờ BA confirm spec) theo CLAUDE.md §6.

> **Phân nhóm SRS update 2026-05-05:** **Nhóm C — IMPACT only.** Module HĐTV **KHÔNG** có file SRS update v3.5. **Chịu impact cross-cutting v3.5:** (1) **Hard-delete** (rename `is_deleted` → `da_xoa`, semantics giữ nguyên — soft delete column) áp dụng cho `HOP_DONG_TU_VAN`, (2) **CR-01 — 5 trường công khai** đối với entity có thể publish (HĐTV mặc định **KHÔNG** publish, nhưng vẫn cần verify regression do schema shared). Đây là module CRUD thuần (KHÔNG phê duyệt) — test full CRUD/permission + sample workflow happy path + regression cross-cutting, KHÔNG retest từ con số 0.

> **Quy trình:** Theo [scaling-test-strategy.md §4.1 Bước 3](../../../output/scaling-test-strategy.md) — trích BR từ SRS local + sibling-check ≥2 module cùng Lớp 4 (FR-06 Chi trả + FR-12 TV chuyên sâu) + BA sign-off trước GĐ 3 Functional.
>
> **v3.0 (2026-04-23):** Test plan này dùng cho **GĐ 3 Functional + Auth + Edge**. GĐ 1 Seed + GĐ 2 Workflow là 2 phase riêng → output `seed-checklist-hdtv.md` + `workflow-test-report-hdtv.md`. Happy path đã cover ở GĐ 2 — TC §4 ở đây tập trung **CRUD + negative + edge + auth + cross-module impact**.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **Module:** FR-14 Hợp đồng tư vấn — Nhóm X.3, UC163 + UC163e (`srs-v3/srs-fr-14-hop-dong-tv.md:5-7`).
- **Mục đích:** CRUD hợp đồng tư vấn giữa đơn vị và TVV/tổ chức tư vấn. Chỉ CRUD, KHÔNG có phê duyệt (`srs-v3/srs-fr-14-hop-dong-tv.md:25`).
- **Entity chính:** `HOP_DONG_TU_VAN` (owned) — entity trung tâm nhóm X.3, ~1,000 records/năm (`srs-v3/srs-fr-14-hop-dong-tv.md:287, 371`).
- **Màn hình:** SCR-X3-01 — Danh sách + Form Thêm/Sửa (5 accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký) (`srs-v3/srs-fr-14-hop-dong-tv.md:243-252`).
- **Cross-module impact:** số HĐ (`hop_dong_tv_id` + `so_hop_dong_tvpl` + `ngay_hop_dong`) feed vào hồ sơ Chi trả FR-06 (`02-thu-tu-module.md:681`); liên kết VV N:N với FR-05; chọn TVV/CG từ FR-04 Bên B (`srs-v3/srs-fr-14-hop-dong-tv.md:289-290`).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-X.3-01 | UC163 | Quản lý HĐ tư vấn (CRUD + Accordion) | HOP_DONG_TU_VAN | `01-TC-crud-hdtv.md` |
| 2 | FR-X.3-01 | UC163 | Mốc tiến độ (inline-edit JSON array) | HOP_DONG_TU_VAN.moc_tien_do | `02-TC-moc-tien-do.md` |
| 3 | FR-X.3-01 | UC163 | Thanh toán giai đoạn (inline-edit JSON array + validate SUM) | HOP_DONG_TU_VAN.thanh_toan_giai_doan | `03-TC-thanh-toan.md` |
| 4 | FR-X.3-01 | UC163 | Liên kết Vụ việc N:N | VU_VIEC × HOP_DONG_TU_VAN | `04-TC-link-vu-viec.md` |
| 5 | FR-X.3-02 | UC163e | Tìm kiếm + lọc HĐ | HOP_DONG_TU_VAN (read-only) | `05-TC-search-filter.md` |
| 6 | (cross-cutting) | — | Permission scope + soft-delete (cross-cutting v3.5) | HOP_DONG_TU_VAN | `06-TC-permission-auth.md` |

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | `qtht_01` / `qtht_02` / `qtht_03` | Admin override, xem tất cả đơn vị (BR-AUTH-08 ngoại lệ); `_03` permission test |
| CB_NV_TW | TW | `cb_nv_tw_01` / `_02` / `_03` | **Primary actor CRUD HĐ TW** (`02-thu-tu-module.md:644`); `_02` fallback Rule 7 |
| CB_NV_BN | BN (BKH/BTC/BCT) | `cb_nv_bn_01..03` | CRUD HĐ cấp bộ ngành — verify data scope đơn vị |
| CB_NV_DP | ĐP (STP-AG/BG/BNI) | `cb_nv_dp_01..03` | CRUD HĐ cấp địa phương — verify cross-unit isolation |
| CB_PD_TW | TW | `cb_pd_tw_01` | **Read-only** HĐ (FR-X.3-02 search allowed per `srs-v3/srs-fr-14-hop-dong-tv.md:183`); KHÔNG có quyền CRUD vì HĐ không có phê duyệt |
| TVV/CG | — | `huongcg` | Read-only HĐ của chính mình (embedded từ SCR-IV-03 tab "Lịch sử hỗ trợ") — verify scope |
| NHT | — | `nht_01` / `nht_02` | Negative permission — KHÔNG được CRUD HĐ |
| DN | — | `9999999990` | Negative permission — DN không truy cập SCR-X3-01 |

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../../output/permission-matrix.md). Account convention `_01` primary / `_02` fallback / `_03` permission test (theo CLAUDE.md §Rule 7).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

> ⚠️ **Quy định điền bảng:**
> - Cột "Nguồn" cite `srs-v3/<file>:<line>`.
> - Cột "Ngoại lệ SRS-quoted" chỉ điền khi SRS có dòng ngoại lệ cụ thể.
> - KHÔNG suy luận BR ngoài SRS — thiếu BR cần SPEC-CLARIFY.

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|----|---------|------------------|---------------------|---------------------|-----------|
| BR-AUTH-01 | Xác thực người dùng (login + TOTP 2FA email) | `srs-v3/srs-fr-14-hop-dong-tv.md:126,449,456-464` | ✅ Yes | "API outbound không yêu cầu session (dùng JWT)" (line 464) | TC-AUTH-01 (precondition login) |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` — áp dụng MỌI bảng có `don_vi_id` | `srs-v3/srs-fr-14-hop-dong-tv.md:450,465-472` | ✅ Yes | "Không có exception ngoại trừ QTHT" (line 469); "AUDIT_LOG không có phân quyền (immutable)" (line 472) | TC-PERM-01..04 (cross-unit isolation), TC-SEARCH-04 (FR-X.3-02 phạm vi đơn vị) |
| BR-DATA-01 | Soft delete — set `is_deleted = 1`. KHÔNG xóa vật lý ngoại trừ retention | `srs-v3/srs-fr-14-hop-dong-tv.md:451,474-481` | ✅ Yes (Cross-cutting v3.5 rename `is_deleted` → `da_xoa`, semantics giữ) | "AUDIT_LOG: không xóa" (line 481) | TC-DEL-01..04 (xóa HĐ → set flag, không xóa vật lý) |
| BR-DATA-04 | Sinh mã tự động format `HDTV-YYYYMMDD-SEQ` | `srs-v3/srs-fr-14-hop-dong-tv.md:452,483-489` | ✅ Yes | — | TC-CRUD-01 (verify mã auto), TC-CRUD-04 (verify uniqueness SEQ trong ngày) |
| BR-DATA-05 | Audit trail CUD (ghi AUDIT_LOG mọi CUD + login/logout) — immutable | `srs-v3/srs-fr-14-hop-dong-tv.md:453,491-497` | ✅ Yes | — | TC-AUDIT-01..03, TC accordion "Nhật ký" (SCR-X3-01 #10) |
| BR-DATA-07 | Pagination default 20 rows/page, max 100 | `srs-v3/srs-fr-14-hop-dong-tv.md:454,499-505` | ✅ Yes | — | TC-PAG-01..03 (danh sách HĐ + search result) |
| **BR-HDTV-01** | Ngày bắt đầu ≤ Ngày kết thúc | `srs-v3/srs-fr-14-hop-dong-tv.md:118` (Processing Bước 3), `:157` (ERR-HDTV-02) | ✅ Yes | — | TC-CRUD-NEG-02 (date validation) |
| **BR-HDTV-02** | Tổng `thanh_toan_giai_doan.so_tien` ≤ `gia_tri` HĐ | `srs-v3/srs-fr-14-hop-dong-tv.md:119` (Processing Bước 4), `:158` (ERR-HDTV-03) | ✅ Yes | — | TC-TT-NEG-01 (SUM overflow), TC-TT-EDGE-01 (SUM = giá trị HĐ exact) |
| **BR-HDTV-03** | Xóa HĐ: chỉ khi KHÔNG có vụ việc liên kết — set soft delete | `srs-v3/srs-fr-14-hop-dong-tv.md:122` (Processing Bước 7), `:159` (ERR-HDTV-04), `:272` (Quy tắc tương tác) | ✅ Yes | — | TC-DEL-02 (xóa khi có VV → reject), TC-DEL-03 (xóa khi không có VV → soft) |
| **BR-HDTV-04** | Giá trị HĐ > 0 | `srs-v3/srs-fr-14-hop-dong-tv.md:160` (ERR-HDTV-05) | ✅ Yes | — | TC-CRUD-NEG-04 (giá trị = 0 / âm) |
| **BR-HDTV-05** | UI: thời hạn kết thúc hiển thị **đỏ** nếu ≤ 30 ngày | `srs-v3/srs-fr-14-hop-dong-tv.md:261,273` | ✅ Yes | — | TC-UI-01 (red badge), TC-UI-02 (boundary 30 / 31 ngày) |
| **BR-HDTV-06** | Progress bar TT = SUM(đã thanh toán) / giá trị HĐ × 100% | `srs-v3/srs-fr-14-hop-dong-tv.md:274` | ✅ Yes | — | TC-TT-01 (progress bar render 0% / 50% / 100%) |
| **BR-HDTV-07** | Mã HĐ UNIQUE (constraint DB) | `srs-v3/srs-fr-14-hop-dong-tv.md:357` (UNIQUE), `:79` (Format) | ✅ Yes | — | TC-CRUD-04 (concurrency same-day → 2 SEQ khác nhau) |
| **BR-HDTV-08** | `moc_tien_do` và `thanh_toan_giai_doan` lưu JSON; CHECK constraint IS JSON | `srs-v3/srs-fr-14-hop-dong-tv.md:374-375` | ✅ Yes | — | TC-MTD-NEG-01 (payload malformed → BE reject) |
| **BR-HDTV-09** | Trạng thái HĐ ∈ `{DANG_THUC_HIEN, HOAN_THANH, HUY, TAM_DUNG}`, default `DANG_THUC_HIEN` | `srs-v3/srs-fr-14-hop-dong-tv.md:369,437` | ✅ Yes | "Không theo vòng đời phê duyệt" (line 437) | TC-CRUD-01 (verify default), TC-SM-01..04 (transition đơn giản — xem §2.5) |
| **BR-HDTV-10** ⚠️ | Bên A auto-fill từ `don_vi_id` của user login. **[SPEC-CLARIFY-HDTV-04]** SRS line 81 (`auto đơn vị`, Nguồn `hệ thống`) + line 263 (`Bên A (auto đơn vị)`) KHÔNG explicit cấm user edit sau auto-fill → readonly vs editable ambiguous. | `srs-v3/srs-fr-14-hop-dong-tv.md:81,263`, `02-thu-tu-module.md:656` | ⚠️ Partial — cần BA confirm readonly behavior | — | TC-CRUD-02 (Bên A auto-fill), TC-CRUD-02b (Bên A readonly enforce — defer chờ BA), TC-PERM-02 (cross-unit Bên A đúng đơn vị user) |

> **BR cross-cutting v3.5 áp dụng cho module này dù không có SRS update file v3.5:**
> - **Hard-delete rename** — column `is_deleted` đổi thành `da_xoa`, semantics giữ nguyên soft delete. Quan trọng: verify regression khi cross-cutting deploy → query API trả về `da_xoa` không phải `is_deleted` → TC-CROSS-01.
> - **CR-01 5 trường công khai** — HĐTV **mặc định NOT applicable** (KHÔNG có publish flag trong SRS HĐTV; khác Hỏi đáp/Biểu mẫu/VV có publish). Cite cross-cutting source: `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` (cross-cutting CR-01). **[SPEC-CLARIFY-HDTV-03]** BA confirm HĐTV không publish PLQG. TC-CROSS-02 (P2) test negative chỉ giữ khi BA chưa reply; nếu BA confirm NOT applicable → defer.
>
> **Mâu thuẫn nội tại SRS — FK direction VV ↔ HĐ [SPEC-CLARIFY-HDTV-04]:**
> - Input table line 88 ghi `vu_viec_ids | identifier[]` (mảng → suggest N:N).
> - ERD line 325-326, 346-347, 397 ghi `VU_VIEC.hop_dong_tv_id FK → HOP_DONG_TU_VAN` (1:N — 1 VV chỉ thuộc 1 HĐ).
> - **2 phương án test:**
>   - **Phương án A (N:N giả định):** TC-LINK-VV-01..03 keep nguyên — 1 VV link nhiều HĐ qua bảng trung gian.
>   - **Phương án B (1:N giả định):** TC-LINK-VV-01b — link VV1 vào HĐ-A rồi try link VV1 vào HĐ-B → expect reject hoặc move (VV1 mất khỏi HĐ-A).
> - Chạy cả 2 phương án trong R{N} tới rồi báo BA quyết model thật, KHÔNG tự kết luận trước.
>
> **Định nghĩa "VV liên kết" cho BR-HDTV-03 [SPEC-CLARIFY-HDTV-04 sub]:**
> - SRS không define VV `da_xoa=1` có còn count "liên kết" không. TC-DEL-02b verify edge case: soft-deleted VV → xóa HĐ allowed hay reject?

### 2.2 Error Codes

| Mã lỗi | Điều kiện trigger | Message (SRS-quoted) | Severity | Nguồn |
|--------|-------------------|----------------------|----------|-------|
| ERR-HDTV-01 | Tên HĐ trống | "Tên hợp đồng là bắt buộc" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:156` |
| ERR-HDTV-02 | Ngày bắt đầu > ngày kết thúc | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:157` |
| ERR-HDTV-03 | Tổng thanh toán > giá trị HĐ | "Tổng thanh toán vượt giá trị hợp đồng" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:158` |
| ERR-HDTV-04 | Xóa HĐ có VV liên kết | "Không thể xóa hợp đồng đang có vụ việc liên kết" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:159` |
| ERR-HDTV-05 | Giá trị HĐ không hợp lệ (≤ 0) | "Giá trị hợp đồng phải lớn hơn 0" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:160` |
| ERR-HDTV-TK-01 | `tu_ngay` > `den_ngay` (search) | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR | `srs-v3/srs-fr-14-hop-dong-tv.md:228` |
| INF-HDTV-TK-01 | Không có kết quả search | "Không tìm thấy hợp đồng phù hợp" | INFO | `srs-v3/srs-fr-14-hop-dong-tv.md:229` |

> ⚠️ Message phải quote **nguyên văn**. Test negative match exact, không "close enough" accept.

### 2.3 Permission Matrix (module-specific)

> Reference đầy đủ: [output/permission-matrix.md](../../../output/permission-matrix.md). Bảng dưới CHỈ cho entity `HOP_DONG_TU_VAN`.

| Action / Role | QTHT | CB_NV (cùng đơn vị) | CB_NV (khác đơn vị) | CB_PD | TVV/CG (Bên B của HĐ) | NHT | DN |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Xem danh sách HĐ (SCR-X3-01) | ✅ All | ✅ Đơn vị mình | ❌ (BR-AUTH-08) | ✅ Read-only đơn vị mình | ✅ Read-only HĐ chính mình (embedded SCR-IV-03) | ❌ | ❌ |
| Xem chi tiết HĐ | ✅ All | ✅ Đơn vị mình | ❌ | ✅ Đơn vị mình | ✅ HĐ chính mình | ❌ | ❌ |
| Tạo HĐ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Sửa HĐ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Xóa HĐ (soft) | ✅ | ✅ (BR-HDTV-03) | ❌ | ❌ | ❌ | ❌ | ❌ |
| Tìm kiếm HĐ (FR-X.3-02) | ✅ All | ✅ Đơn vị mình | ❌ | ✅ Đơn vị mình | ✅ HĐ mình | ❌ | ❌ |
| Liên kết VV vào HĐ | ✅ | ✅ (VV cùng đơn vị) | ❌ | ❌ | ❌ | ❌ | ❌ |

> **Nguồn quyền truy cập:**
> - CB_NV: `srs-v3/srs-fr-14-hop-dong-tv.md:67,72` (Tác nhân + Preconditions FR-X.3-01).
> - CB_PD: `srs-v3/srs-fr-14-hop-dong-tv.md:183` (FR-X.3-02 — "Cán bộ Nghiệp vụ, Cán bộ Phê duyệt").
> - TVV/CG embedded: `02-thu-tu-module.md:650` (truy cập từ tab "Lịch sử hỗ trợ" SCR-IV-03).
> - QTHT bypass: `srs-v3/srs-fr-14-hop-dong-tv.md:469` ("Không có exception ngoại trừ QTHT").

### 2.4 UI Layout (SCR-X3-01)

> ⚠️ **CẢNH BÁO:** Components từ SRS SCR-X3-01 (UX-Spec MH-14.1). Note v2.1: HĐ không còn menu riêng — truy cập embedded từ VV (SCR-V.I-03 → accordion "HĐ tư vấn liên kết") + TVV (SCR-IV-03 → tab "Lịch sử") (`srs-v3/srs-fr-14-hop-dong-tv.md:241`).
> KHÔNG dùng absence trên UI để khẳng định "module KHÔNG có X" — phải cite SRS line.

**Components (trích `srs-v3/srs-fr-14-hop-dong-tv.md:254-268`):**

- **Toolbar (1-2):** Breadcrumb "Trang chủ > Tư vấn > Hợp đồng tư vấn" + Tiêu đề + nút `[+ Thêm hợp đồng]` `[Xuất Excel]` `[Làm mới]`.
- **Filter-bar (3):** Full-text (tên HĐ / mã HĐ / Bên B) + TVV dropdown searchable + khoảng ngày.
- **Content/Table (4):** Mã HĐ / Tên HĐ / Bên A / Bên B / Giá trị (format VND) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu ≤30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động.
- **Pagination (5):** 20 mục/trang default.
- **Form Thêm/Sửa — 5 accordion (6-10):**
  1. **Thông tin chung (6):** Mã auto / Tên (Y) / Bên A auto / Bên B + TVV dropdown / Giá trị (Y) / Thời hạn bắt đầu (Y) / Thời hạn kết thúc (Y, ≥ bắt đầu) / Nội dung / Ghi chú / File đính kèm (multi).
  2. **Vụ việc liên kết (7):** Bảng VV (Mã / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]) + `[+ Liên kết VV]` → modal multi-select N:N.
  3. **Mốc tiến độ (8):** Inline-edit (Tên mốc / Ngày dự kiến / Ngày thực tế / Trạng thái `CHUA_BAT_DAU/DANG_THUC_HIEN/HOAN_THANH`). `[+ Thêm mốc]`.
  4. **Thanh toán giai đoạn (9):** Inline-edit (Giai đoạn / Số tiền / Ngày TT / Trạng thái `CHUA_THANH_TOAN/DA_THANH_TOAN`). Validate SUM ≤ giá trị HĐ. Progress bar phía trên.
  5. **Nhật ký (10):** Timeline CUD + mốc + thanh toán + liên kết VV.
- **Action-bar (11):** `[Hủy]` `[Lưu]` — **KHÔNG có nút Trình duyệt / Phê duyệt** (CRUD thuần, `srs-v3/srs-fr-14-hop-dong-tv.md:268,275`).

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**

- ☑ Nút `[Xuất Excel]` trên toolbar — SRS quote `srs-v3/srs-fr-14-hop-dong-tv.md:259`.
- ☑ Pagination 20/page (BR-DATA-07).
- ☑ Audit log mọi CUD (BR-DATA-05) + accordion Nhật ký #10.
- ☑ Soft delete (BR-DATA-01 + BR-HDTV-03).
- ☑ Search sanitize (giả định BR-EC-13 nếu có — cần verify trong Phụ lục B file chính srs-v3.md).

**Feature module KHÔNG có (QUOTE SRS):**

- ❌ Phê duyệt / Workflow CB_PD duyệt — quote `srs-v3/srs-fr-14-hop-dong-tv.md:25,65,268,275,435-437` ("KHÔNG có phê duyệt", "Chỉ CRUD thuần", "Trạng thái... không theo vòng đời phê duyệt").
- ❌ Publish ra Cổng PLQG — KHÔNG có trong SRS HĐTV (khác FR-V.I VV / FR-VII Biểu mẫu / FR-II Hỏi đáp). Cross-cutting CR-01 NOT applicable cho HĐTV.
- ❌ API inbound — `02-thu-tu-module.md:667` ("Không có API inbound").

### 2.5 State Machine — KHÔNG có (CRUD thuần)

> **Source quote:** `srs-v3/srs-fr-14-hop-dong-tv.md:435-437`
> "Nhóm X.3 (Hợp đồng tư vấn) không có state machine. HĐ tư vấn chỉ CRUD thuần, KHÔNG có phê duyệt. Trạng thái HĐ (`DANG_THUC_HIEN`, `HOAN_THANH`, `HUY`, `TAM_DUNG`) chỉ là status field đơn giản, không theo vòng đời phê duyệt."

**Status field 4 giá trị (enum đơn giản, không có guard transition):**

| Status | Mô tả | Default |
|---|---|:---:|
| `DANG_THUC_HIEN` | HĐ đang hiệu lực, đang triển khai | ✅ Default khi tạo (`:369`) |
| `TAM_DUNG` | HĐ tạm dừng (có thể chuyển về `DANG_THUC_HIEN`) | — |
| `HOAN_THANH` | HĐ đã đóng / hoàn thành | — |
| `HUY` | HĐ bị hủy | — |

> ⚠️ **TODO — UNVERIFIED transition flow** (`02-thu-tu-module.md:670-680`): SRS không có section SM-HOPDONG trong Phụ lục C — chỉ có enum 4 giá trị, KHÔNG có bảng transition formal. `02-thu-tu-module.md` suy luận 5 transition (— → `DANG_THUC_HIEN`; `DANG_THUC_HIEN` ↔ `TAM_DUNG`; `DANG_THUC_HIEN` → `HOAN_THANH` với guard SUM TT ≤ giá trị; `DANG_THUC_HIEN`/`TAM_DUNG` → `HUY`). **SPEC-CLARIFY-HDTV-01 — cần CĐT confirm transition rules trước khi test status workflow.** TC §4 vẫn cover transition basic, mark P2 (nên có) thay vì P0.

### 2.6 Data dependencies & Seed / Workflow input (v3.0)

| Phase | Input file | Section dùng |
|-------|-----------|--------------|
| GĐ 1 Seed (pure entry state) | [`input/data/seed-fixture.yaml`](../../../input/data/seed-fixture.yaml) | `hop_dong_tu_van_variants[1..6]` (nếu có; nếu fixture chưa cover thì manual seed qua UI) |
| GĐ 1 click flow | [`input/flow-module.md`](../../../input/flow-module.md) | §FR-14 / §X.3 Bước 1 thủ công CB_NV nhập |
| GĐ 2 Workflow | [`input/flow-module.md`](../../../input/flow-module.md) | §X.3 — CRUD thuần (1 bước nhập, không workflow phê duyệt) |
| Cross-module map | [`input/data/entity-map.md`](../../../input/data/entity-map.md) | `HOP_DONG_TU_VAN` — Tạo tại SCR-X3-01, Đọc tại SCR-V.II (Chi trả) + SCR-V.I-03 (VV) + SCR-IV-03 (TVV) |

**Upstream dependencies (Tier check):**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|-------------------|:----:|----------------------------------|-----------------------|
| HOP_DONG_TU_VAN | 4 | `DON_VI` (Bên A), `TU_VAN_VIEN` (Bên B, state `HOAT_DONG`), `VU_VIEC` (liên kết N:N), `TAI_KHOAN` (CB_NV creator) | FR-10 (DON_VI, TK), FR-04 (TVV state HOAT_DONG ≥3), FR-05 (VV state ≥ `DA_TIEP_NHAN`) |

**Downstream consumer × filter (entity-map verify):**

| Module đọc HĐ | Filter | Verify query | TC liên quan |
|---|---|---|---|
| FR-06 Chi trả | `hop_dong_tv_id` populate vào hồ sơ chi trả | `02-thu-tu-module.md:681` — số HĐ + ngày HĐ feed vào Mẫu 01 NĐ55 | TC-CROSS-03 (xóa HĐ có chi trả → guard?) |
| FR-05 VV (SCR-V.I-03 accordion) | `WHERE hop_dong_tv_id=<vv_id>` N:N | `srs-v3/srs-fr-14-hop-dong-tv.md:241,346` | TC-LINK-VV-01..03 |
| FR-04 TVV (SCR-IV-03 tab Lịch sử) | `WHERE tu_van_vien_id=<tvv_id>` | `02-thu-tu-module.md:650` | TC-PERM-TVV-01 (TVV chỉ thấy HĐ mình) |

> **Lưu ý:** KHÔNG hardcode `N records` — fixture chốt 6 variants nếu có. Seed cần đủ filter coverage:
> - ≥3 HĐ × mỗi đơn vị (TW + BN-BKH + DP-AG) → verify BR-AUTH-08 cross-unit.
> - ≥1 HĐ mỗi status (`DANG_THUC_HIEN`, `TAM_DUNG`, `HOAN_THANH`, `HUY`).
> - ≥1 HĐ có VV liên kết + ≥1 HĐ không có VV (test BR-HDTV-03 xóa).
> - ≥1 HĐ có Bên B là TVV / ≥1 Bên B nhập tay text-only.

---

## 3. Cấu Trúc File Test Case

```
fr-14-hop-dong-tv/
├── test-plan.md                       ← File này (00-overview)
├── 01-TC-crud-hdtv.md                 ← CRUD Thông tin chung + 11 input field + ERR-HDTV-01/02/05
├── 02-TC-moc-tien-do.md               ← Inline-edit JSON array Mốc tiến độ
├── 03-TC-thanh-toan.md                ← Inline-edit Thanh toán + BR-HDTV-02 SUM + ERR-HDTV-03 + BR-HDTV-06 progress
├── 04-TC-link-vu-viec.md              ← Modal multi-select N:N + BR-HDTV-03 xóa khi có VV
├── 05-TC-search-filter.md             ← FR-X.3-02 search + ERR-HDTV-TK-01 + pagination + BR-HDTV-05 UI red badge
├── 06-TC-permission-auth.md           ← BR-AUTH-01/08 + cross-unit + role negative + cross-cutting da_xoa
└── (11-REVIEW-edge-case-hunter.md)    ← Optional review từ bmad-review-edge-case-hunter
```

---

## 4. Tổng Quan Số Lượng Test Cases

> Trọng tâm: CRUD + Negative + Edge + Cross-module + Permission. Happy path đã chuyển sang GĐ 2 Workflow report.

| File | TC ID | Mô tả ngắn | Loại | Priority |
|------|-------|------------|------|:--------:|
| 01 | TC-CRUD-01 | Tạo HĐ đầy đủ 12 field → verify auto-gen mã `HDTV-YYYYMMDD-001` + default `DANG_THUC_HIEN` | Happy | P0 |
| 01 | TC-CRUD-02 | Bên A auto-fill từ `don_vi_id` của user login (BR-HDTV-10) | Happy | P0 |
| 01 | TC-CRUD-02b ⚠️ | **[SPEC-CLARIFY-HDTV-04]** Bên A readonly behavior — test thử edit field Bên A sau auto-fill (defer kết luận PASS/FAIL chờ BA) | Negative | P2 |
| 01 | TC-CRUD-NEG-01 | Tên HĐ trống → ERR-HDTV-01 exact message | Negative | P0 |
| 01 | TC-CRUD-NEG-02 | Ngày bắt đầu > ngày kết thúc → ERR-HDTV-02 (BR-HDTV-01) | Negative | P0 |
| 01 | TC-CRUD-NEG-04 | Giá trị HĐ = 0 / âm → ERR-HDTV-05 (BR-HDTV-04) | Negative | P0 |
| 01 | TC-CRUD-04 | Concurrency: 2 user TW tạo HĐ cùng ngày → 2 SEQ khác nhau (BR-HDTV-07 UNIQUE). **Test method:** script API parallel POST (curl bg `&`) hoặc 2 isolatedContext race; KHÔNG tạo tuần tự. | Edge | P1 |
| 01 | TC-CRUD-05 | Upload nhiều file đính kèm — verify multi-file save | Edge | P2 |
| 01 | TC-FILE-01 | File upload negative: MIME invalid (.exe), size > cap (vd 50MB), số file > max → reject | Negative | P1 |
| 01 | TC-CRUD-06 | Sửa HĐ — verify AUDIT_LOG ghi diff trước/sau (BR-DATA-05) | Happy | P1 |
| 02 | TC-MTD-01 | Inline-edit thêm 3 mốc tiến độ với 3 trạng thái khác nhau → save JSON array | Happy | P0 |
| 02 | TC-MTD-NEG-01 | Tên mốc trống / Ngày dự kiến trống → reject inline | Negative | P1 |
| 02 | TC-MTD-EDGE-01 | Thêm 50+ mốc tiến độ → verify performance + render | Edge | P2 |
| 03 | TC-TT-01 | Thêm 3 giai đoạn TT (SUM = 50% giá trị) → progress bar = 50% (BR-HDTV-06) | Happy | P0 |
| 03 | TC-TT-NEG-01 | Tổng `so_tien` > `gia_tri` → ERR-HDTV-03 (BR-HDTV-02) | Negative | P0 |
| 03 | TC-TT-EDGE-01 | SUM = giá trị HĐ exact → PASS (boundary, BR-HDTV-02 ≤) | Edge | P1 |
| 03 | TC-TT-EDGE-02 | SUM = giá trị HĐ + 1đ → ERR-HDTV-03 (boundary) | Edge | P1 |
| 03 | TC-TT-EDGE-03 | SUM = 0 (chưa có TT) → progress bar render 0% (boundary âm BR-HDTV-06) | Edge | P2 |
| 04 | TC-LINK-VV-01 | **[SPEC-CLARIFY-HDTV-04 Phương án A — N:N]** Modal multi-select 3 VV → liên kết N:N → bảng accordion #7 hiện 3 row | Happy | P0 |
| 04 | TC-LINK-VV-01b | **[SPEC-CLARIFY-HDTV-04 Phương án B — 1:N]** Link VV1 vào HĐ-A rồi try link VV1 vào HĐ-B → verify reject hoặc move (mất khỏi HĐ-A) | Negative | P0 |
| 04 | TC-LINK-VV-02a | Modal lọc BR-AUTH-08 — CB_NV BN-BKH thấy chỉ VV BN-BKH | Permission | P0 |
| 04 | TC-LINK-VV-02b | Cross-link: CB_NV TW try link VV BN-BKH vào HĐ TW → verify reject/accept (SRS chưa rõ — log evidence cho BA) | Permission | P1 |
| 04 | TC-LINK-VV-03 | Bỏ liên kết 1 VV → bảng accordion #7 còn N-1 | Happy | P1 |
| 04 | TC-DEL-02 | Xóa HĐ đang có VV liên kết → ERR-HDTV-04 (BR-HDTV-03) | Negative | P0 |
| 04 | TC-DEL-02b | **[SPEC-CLARIFY-HDTV-04 sub]** VV liên kết đã soft-delete (`da_xoa=1`) → xóa HĐ allowed hay reject? | Edge | P2 |
| 04 | TC-DEL-03 | Bỏ liên kết hết VV → xóa HĐ → soft delete (BR-DATA-01) | Happy | P0 |
| 04 | TC-DEL-04 | Verify sau soft delete: list ẩn HĐ, AUDIT_LOG có record DELETE | Edge | P1 |
| 05 | TC-SEARCH-01 | Search keyword full-text trên tên HĐ / mã HĐ / Bên B → match | Happy | P0 |
| 05 | TC-SEARCH-02 | Filter TVV dropdown searchable | Happy | P1 |
| 05 | TC-SEARCH-03 | `tu_ngay` > `den_ngay` → ERR-HDTV-TK-01 | Negative | P0 |
| 05 | TC-SEARCH-04 | Search scope BR-AUTH-08: CB_NV TW không thấy HĐ của CB_NV BN | Permission | P0 |
| 05 | TC-SEARCH-05 | Empty result → INF-HDTV-TK-01 "Không tìm thấy hợp đồng phù hợp" | Negative | P1 |
| 05 | TC-SEARCH-06 | Keyword SQL injection (`' OR 1=1--`) + XSS payload (`<script>alert(1)</script>`) qua tên HĐ/Bên B → sanitize, không exec; cross-ref BR-EC-13 Phụ lục B nếu có | Security | P0 |
| 05 | TC-PAG-01 | Pagination 20/page default → trang 1 hiện 20, click trang 2 hiện tiếp (BR-DATA-07) | Happy | P1 |
| 05 | TC-PAG-02 | Boundary BR-DATA-07 max 100: API `?limit=101` → reject (400) hoặc cap về 100; UI dropdown size không cho chọn >100 | Edge | P1 |
| 05 | TC-UI-01 | HĐ với `thoi_han_ket_thuc` còn 15 ngày → render đỏ (BR-HDTV-05) | UI | P1 |
| 05 | TC-UI-02 | Boundary: 30 ngày → đỏ; 31 ngày → bình thường | Edge | P2 |
| 06 | TC-PERM-01 | CB_NV TW login → CRUD HĐ scope TW only | Permission | P0 |
| 06 | TC-PERM-02 | CB_NV BN-BKH login → KHÔNG thấy HĐ của BN-BTC (cross-unit isolation BR-AUTH-08) | Permission | P0 |
| 06 | TC-PERM-03 | CB_PD TW login → chỉ search/view, nút `[+ Thêm hợp đồng]` ẩn / 403 khi POST | Permission | P0 |
| 06 | TC-PERM-04 | NHT / DN login → SCR-X3-01 redirect 403 hoặc ẩn menu | Permission | P0 |
| 06 | TC-PERM-05 | QTHT login → thấy tất cả HĐ mọi đơn vị (BR-AUTH-08 ngoại lệ QTHT) | Permission | P1 |
| 06 | TC-PERM-TVV-01 ⚠️ | **[SPEC-CLARIFY-HDTV-05]** TVV login → embedded view tab "Lịch sử" SCR-IV-03 chỉ HĐ chính mình. SRS FR-X.3-01/02 KHÔNG explicit grant TVV/CG quyền read HĐ — cite `02-thu-tu-module.md:650` là quy trình nghiệp vụ. Cần BA confirm + verify NotebookLM FR-IV trước khi PASS. | Permission | P2 |
| 06 | TC-AUTH-01 | Logout / session expire → POST /HĐ trả 401 (BR-AUTH-01) | Auth | P0 |
| 06 | TC-AUDIT-01 | Tạo HĐ → AUDIT_LOG INSERT record với `entity='HOP_DONG_TU_VAN'` | Audit | P1 |
| 06 | TC-CROSS-01 | **Cross-cutting v3.5 — Hard-delete rename:** verify API `/api/v1/hop-dong-tu-van` response payload có field `da_xoa` (KHÔNG `is_deleted`); list query filter `?da_xoa=0`. Cite: `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md` (cross-cutting rename). Method: MCP `list_network_requests` inspect response. | Regression | P0 |
| 06 | TC-CROSS-02 ⚠️ | **[SPEC-CLARIFY-HDTV-03]** Cross-cutting v3.5 — CR-01 negative: HĐTV KHÔNG có toggle "Công khai" / 5 trường công khai. Defer P2 chờ BA confirm HĐTV not-applicable cho CR-01 (SRS HĐTV không có publish flag). | Regression | P2 |
| 06 | TC-CROSS-03 ⚠️ | **[SPEC-CLARIFY-HDTV-02]** Cross-module FR-06: xóa HĐ đã có record Chi trả ref `hop_dong_tv_id` → confirm behavior (block / null FK). | Cross-module | P1 |

**Tổng số TC:** **48 TC** (sau revise 2026-05-12 13:30:00 — thêm 9 TC: CRUD-02b, FILE-01, TT-EDGE-03, LINK-VV-01b, LINK-VV-02a/02b, DEL-02b, SEARCH-06, PAG-02; reclassify TC-PERM-TVV-01 + TC-CROSS-02 → P2).

| Loại | Số TC | % |
|----------|------:|--:|
| Happy | 9 | 19% |
| Negative | 11 | 23% |
| Edge | 9 | 19% |
| Permission | 9 | 19% |
| Auth / Audit | 2 | 4% |
| UI | 2 | 4% |
| Regression / Cross-module / Security | 6 | 12% |

**Phân bổ priority:**

| Priority | Số TC | % |
|----------|------:|--:|
| P0 (bắt buộc) | 22 | 46% |
| P1 (quan trọng) | 14 | 29% |
| P2 (nên có) | 12 | 25% |

---

## 5. Tiêu chí đạt/không đạt

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 (22/22) + ≥90% P1 (≥13/14) pass; P2 mang tính nice-to-have / SPEC-CLARIFY defer.
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%.
- 🚫 **BLOCKED nếu** (CLAUDE.md §6 phân nhóm **C — Chờ BA confirm spec**):
  - SPEC-CLARIFY-HDTV-01 (transition rules) chưa BA confirm → TC §2.5 status workflow defer.
  - SPEC-CLARIFY-HDTV-02 (xóa HĐ có Chi trả) chưa confirm → TC-CROSS-03 defer.
  - SPEC-CLARIFY-HDTV-03 (CR-01 applicable HĐTV?) chưa confirm → TC-CROSS-02 defer.
  - SPEC-CLARIFY-HDTV-04 (FK direction VV + Bên A readonly + VV soft-deleted count) chưa confirm → TC-LINK-VV-01/01b/02b, TC-CRUD-02b, TC-DEL-02b defer; chạy cả 2 phương án A/B rồi escalate.
  - SPEC-CLARIFY-HDTV-05 (TVV/CG read HĐ embedded) chưa confirm → TC-PERM-TVV-01 defer P2.

---

## 6. Tham chiếu

- [input/srs-v3/srs-fr-14-hop-dong-tv.md](../../../input/srs-v3/srs-fr-14-hop-dong-tv.md) — SRS baseline v3 FR-14 (510 lines).
- [input/quy-trinh-nghiep-vu/02-thu-tu-module.md §FR-14](../../../input/quy-trinh-nghiep-vu/02-thu-tu-module.md) — bảng transition + dropdown + accordion + sibling module order.
- [tasks/system-overview.md §4.11 M10 HĐTV](../../../tasks/system-overview.md) — module overview 5 accordion + filter list.
- [input/users.csv](../../../input/users.csv) — accounts (CB_NV/CB_PD × 3 cấp + QTHT + TVV/CG/NHT/DN).
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền 49 entity × 11 role.
- [output/template/test-plan-overview-template.md](../../../output/template/test-plan-overview-template.md) — template gốc.
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — TC field-level template.
- [input/data/entity-map.md](../../../input/data/entity-map.md) — cross-module entity map.
- Sibling test plans (Lớp 4 cùng nhóm): [`fr-06-chi-tra/test-plan.md`](../fr-06-chi-tra/test-plan.md) (nếu có), [`fr-12-tv-chuyen-sau/test-plan.md`](../fr-12-tv-chuyen-sau/test-plan.md).

---

## SPEC-CLARIFY tickets cần BA confirm trước GĐ 3

| Ticket | Vấn đề | Ảnh hưởng TC | Đề xuất hỏi BA |
|--------|--------|--------------|----------------|
| SPEC-CLARIFY-HDTV-01 | SRS không có SM-HOPDONG formal trong Phụ lục C — chỉ enum 4 giá trị. `02-thu-tu-module.md` suy luận 5 transition nhưng cite "UNVERIFIED" (line 671). | Status workflow TC (P2 trong §4) — nếu BA confirm cho phép tự do chuyển status → no TC; nếu có guard → bổ sung TC. | Status `HOAN_THANH` có cho phép quay về `DANG_THUC_HIEN` không? `HUY` có irreversible không? Có yêu cầu lý do bắt buộc khi `TAM_DUNG` / `HUY` không? |
| SPEC-CLARIFY-HDTV-02 | Xóa HĐ đã có record Chi trả (FR-06) tham chiếu `hop_dong_tv_id` — SRS chỉ nói guard "không có VV liên kết" (BR-HDTV-03), KHÔNG nói guard Chi trả. | TC-CROSS-03 status. | Có cần guard "không xóa HĐ khi đã có Chi trả" không? Hay set FK = NULL ở bảng Chi trả? |
| SPEC-CLARIFY-HDTV-03 | Cross-cutting CR-01 (5 trường công khai) — HĐTV có publish ra Cổng PLQG không? Mặc định SRS HĐTV không có publish flag. | TC-CROSS-02. | Confirm HĐTV KHÔNG publish PLQG (khác VV / Hỏi đáp / Biểu mẫu)? |
| **SPEC-CLARIFY-HDTV-04** 🆕 | (a) Mâu thuẫn FK direction VV: input table line 88 `vu_viec_ids[]` (N:N) vs ERD line 325-326/346-347/397 `VU_VIEC.hop_dong_tv_id FK` (1:N). (b) BR-HDTV-10 Bên A line 81 `auto đơn vị` + line 263 `(auto đơn vị)` KHÔNG explicit cấm edit — readonly vs editable. (c) BR-HDTV-03 "không có VV liên kết" có tính VV đã soft-delete (`da_xoa=1`) không? | TC-LINK-VV-01/01b/02a/02b/03, TC-DEL-02/02b, TC-CRUD-02b. Test cả 2 phương án A/B rồi escalate. | (a) VV ↔ HĐ là N:N (bảng trung gian) hay 1:N (FK trên VV)? (b) Field Bên A có readonly sau auto-fill không? (c) VV `da_xoa=1` có còn count "liên kết" khi xóa HĐ không? |
| **SPEC-CLARIFY-HDTV-05** 🆕 | TVV/CG read HĐ embedded từ SCR-IV-03 tab "Lịch sử" — SRS FR-X.3-01/02 KHÔNG explicit grant. Cite hiện tại là `02-thu-tu-module.md:650` (quy trình nghiệp vụ, KHÔNG phải SRS BR). Cần verify NotebookLM + grep SRS FR-IV xem có UC riêng cho tab Lịch sử không. | TC-PERM-TVV-01 (defer P2). | TVV/CG có quyền xem danh sách HĐ của chính mình từ SCR-IV-03 không? Spec ở đâu? |

---

*Test plan generated 2026-05-12 — sibling-check với FR-12 TV chuyên sâu (Lớp 4) + FR-06 Chi trả (Lớp 4) + FR-02 Hỏi đáp (Lớp 3, downstream). Trước GĐ 3 Functional cần BA sign-off **5 SPEC-CLARIFY tickets** ở trên (HDTV-01..05).*

*Revised 2026-05-12 13:30:00 — apply reviewer feedback (REVISE verdict): 3 critical gaps escalated (FK direction + Bên A readonly + TVV embedded permission) + 6 suggestions adopted (SQL/XSS, max-100 boundary, file upload negative, SUM=0 boundary, split LINK-VV-02, inline `[SPEC-CLARIFY]` tags). Apply rate ≥80% (8/10 gaps + 5/7 suggestions accepted; remaining: §4 chia subsection theo file — deferred to TC files themselves; CB_PD theo cấp — covered indirect by §1.3 reference permission-matrix).*
