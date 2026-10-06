# Kế Hoạch Kiểm Thử — Tài khoản & Phân quyền (FR-VIII-14..17 + FR-VIII-22 + FR-VIII-26)

> **Phiên bản**: 1.1
> **Ngày tạo**: 2026-05-08 · **Cập nhật**: 2026-05-10 (mở rộng scope FR-VIII-22 / UC120 self-registration DN)
> **Nguồn dữ liệu**: SRS v3.1 ([srs-fr-10-quan-tri-v3.1.md](../../../../input/srs-v3/srs-fr-10-quan-tri-v3.1.md) lines 595-844 + 1005-1089 + 1241-1311 + 1499-1606 + 1722-1768 + 1772-1786 + 2077-2118, kèm [srs-v3.1.md](../../../../input/srs-v3/srs-v3.1.md) Phụ lục B/C cho BR + SM cross-cutting)
> **SRS Reference**: FR-VIII-14 (UC112 Vai trò) / FR-VIII-15 (UC113 TK NSD) / FR-VIII-16 (UC114 PQ Dữ liệu) / FR-VIII-17 (UC115 PQ Chức năng) / FR-VIII-22 (UC120 Self-registration DN, NEW v1.1) / FR-VIII-26 (Quên MK / Kích hoạt v3.1), SCR-VIII-02..05 + SCR-VIII-08 đăng ký DN + SCR-VIII-08a phê duyệt QTHT + form đặt MK, SM-TAIKHOAN 5-state/v3.1 CHO_PHAN_QUYEN
>
> **Scope:** Test plan GĐ Functional + Auth + Edge cho 4 sub-module TKPQ + 1 luồng v3.1 mới (Quên MK / Kích hoạt) + 1 luồng public Self-registration DN (UC120). Bao gồm CRUD, lifecycle TK, RBAC matrix, cây phân quyền 2-tầng (BR-AUTH-02 v3.1), form public 22 trường + chain kích hoạt.

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử

- **6 FR** trên **5 màn hình** + form/link đặt MK + form public đăng ký DN:
  - FR-VIII-14 → SCR-VIII-02 — Quản lý Vai trò (CRUD entity VAI_TRO).
  - FR-VIII-15 → SCR-VIII-03 — Quản lý Tài khoản NSD (CRUD + Khóa/Mở khóa/Vô hiệu/Khôi phục + Gửi lại email + Phê duyệt CHO_PHAN_QUYEN).
  - FR-VIII-16 → SCR-VIII-05 — Phân quyền Dữ liệu (Tree multi-select cây 2-tầng TW → {BN, ĐP}).
  - FR-VIII-17 → SCR-VIII-04 — Phân quyền Chức năng (Matrix checkbox 6 quyền × cây menu).
  - FR-VIII-22 (UC120) → SCR-VIII-08 — **Public Self-registration DN** (form 22 trường + tạo TK CHO_KICH_HOAT đã gán vai trò DN + chain mail kích hoạt → FR-VIII-26 step 11 → HOAT_DONG). Auto-pass — không validate ngoài.
  - FR-VIII-26 (v3.1) → SCR-VIII-07 link "Quên mật khẩu" + form đặt MK qua URL token.
- **Đặc thù v3.1:**
  - **BR-AUTH-02 v3.1**: Cấu trúc **2 tầng** TW (cấp 1) → {BN, ĐP} (cấp 2 ngang cấp song song). KHÔNG có nested BN→ĐP. Cây phân quyền dữ liệu (UC114) phải render đúng mô hình này (srs-fr-10:2161 + srs-fr-10:1602).
  - **SM-TAIKHOAN v3.1 CHO_PHAN_QUYEN**: state mới giữa CHO_KICH_HOAT và HOAT_DONG cho luồng self-registration cũ (FR-VIII-22) — `CHO_KICH_HOAT → CHO_PHAN_QUYEN → HOAT_DONG`. Filter trạng thái + tab SCR-VIII-03 phải có lựa chọn này (srs-fr-10:1537, 1539, 1546, 2099-2117).
  - **FR-VIII-26 v3.1**: Workflow chung Quên MK + Kích hoạt lần đầu — token vĩnh viễn cho CHO_KICH_HOAT (TVV/NHT chậm kích hoạt) vs 30 phút cho HOAT_DONG; trigger đồng thời TU_VAN_VIEN/NGUOI_HO_TRO chuyển HOAT_DONG (srs-fr-10:1241-1311).
  - **CCCD field** trong form tạo TK (SCR-VIII-03 #24, srs-fr-10:1560) — không bắt buộc nhưng validate 12 chữ số (dùng cho đồng bộ VNeID UC123 sau).
- **Entity chính:** `VAI_TRO` (UC112), `TAI_KHOAN` (UC113), `TAI_KHOAN_VAI_TRO` (junction N:M), `QUYEN_HAN` (UC114/115), `DON_VI` (read-only ref).
- **State Machine:** SM-TAIKHOAN — **5 states** (CHO_KICH_HOAT, CHO_PHAN_QUYEN, HOAT_DONG, TAM_KHOA, VO_HIEU_HOA) × **~12 transitions** (xem §2.4).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|--------|----------|--------------|--------|----------------|
| 1 | FR-VIII-14 | UC112 | CRUD Vai trò + filter + toggle trạng thái | VAI_TRO | `01-TC-vai-tro.md` |
| 2 | FR-VIII-15 | UC113 | CRUD Tài khoản + Khóa/Mở/VHH/Khôi phục/Gửi mail/Phê duyệt CHO_PHAN_QUYEN + filter + tab 5 states | TAI_KHOAN, TAI_KHOAN_VAI_TRO | `02-TC-tai-khoan.md` |
| 3 | FR-VIII-16 | UC114 | Phân quyền Dữ liệu (cây 2-tầng + BR-AUTH-03/04) | QUYEN_HAN, VAI_TRO_QUYEN_HAN, DON_VI | `03-TC-phan-quyen-du-lieu.md` |
| 4 | FR-VIII-17 | UC115 | Phân quyền Chức năng (matrix 6×N + cây menu cascade) | QUYEN_HAN, VAI_TRO_QUYEN_HAN | `04-TC-phan-quyen-chuc-nang.md` |
| 5 | FR-VIII-26 | (mới v3.1) | Quên mật khẩu / Kích hoạt lần đầu (token + form + SM transitions) | TAI_KHOAN, TU_VAN_VIEN, NGUOI_HO_TRO | `05-TC-quen-mk-kich-hoat.md` |
| 6 | — | — | Permission matrix cross-FR (4 UC) — Role-based UI access + Tier 2 chặn + cross-tenant + audit | All | `06-TC-permission-matrix.md` |
| 7 | — | — | **Security/IDOR suite (NEW Codex R2 2026-05-08)** — 16 TC API authorization test (POST/PUT/PATCH/DELETE direct via fetch). Tách khỏi functional UC để compliant A7. KHÔNG nằm trong B-block functional, security/dev team chạy riêng. | All | `07-TC-security-IDOR.md` |
| 8 | FR-VIII-22 | UC120 | **Self-registration DN (NEW v1.1 2026-05-10)** — Public form đăng ký 22 trường + tạo TAI_KHOAN (CHO_KICH_HOAT, gán vai trò DN sẵn) + DOANH_NGHIEP + gửi mail link kích hoạt vĩnh viễn 1 lần dùng. Chain với FR-VIII-26 step 11 → HOAT_DONG (skip CHO_PHAN_QUYEN). | TAI_KHOAN, DOANH_NGHIEP, TAI_KHOAN_VAI_TRO | `12-TC-self-registration-dn.md` |

> Mỗi UC có 1 file UC riêng (Phase B B-block tham chiếu CHỈ 7 file UC `01-06` + `12`). File `07-TC-security-IDOR.md` là security suite riêng (chạy ngoài Phase B functional). File 08/09/10/11 là audit log — KHÔNG phải TC source.

### 1.3 Tài khoản & role liên quan

| Role | Cấp | Username (users.csv) | Dùng cho TC loại |
|------|-----|-----------------------|-------------------|
| QTHT | — | qtht_01 | Primary CRUD + phê duyệt + phân quyền. `_02` fallback, `_03` permission/IDOR test |
| CB_NV_TW | TW | cb_nv_tw_01 | Negative — verify 403 chặn UC112-115 |
| CB_NV_BN | BN | cb_nv_bn_01 | Negative — verify 403 + BR-AUTH-08 cross-tenant |
| CB_NV_DP | DP | cb_nv_dp_01 | Negative — verify 403 |
| CB_PD_TW/BN/DP | — | cb_pd_tw_01 / cb_pd_bn_01 / cb_pd_dp_01 | Negative — verify 403 |
| NHT/TVV/CG/DN | — | nht_01, tvv_01, cg_01, dn_01 | (a) Negative CMS access; (b) Test FR-VIII-26 kích hoạt lần đầu (TVV/NHT) hoặc reset MK (DN/CG) |
| **(public — không đăng nhập)** | — | — | **UC120 — DN tự đăng ký**. KHÔNG cần đăng nhập trước; truy cập SCR-VIII-07 → button "Đăng ký (dành cho doanh nghiệp)" → SCR-VIII-08. Không có tài khoản → tạo TK mới. |

> **Permission rule:** UC112-115 chỉ QTHT (BR-AUTH-01 Tier 1 srs-fr-10:623, 689, 767, 823). FR-VIII-26 cho phép user **bất kỳ có email** (DN/NHT/TVV/CG/CB) — public link "Quên mật khẩu" không cần đăng nhập trước (srs-fr-10:1252). **UC120 (FR-VIII-22) public hoàn toàn — chỉ DN tự đăng ký**, vai trò khác KHÔNG có form tự đăng ký (srs-fr-10:1734). Auto-pass: hệ thống không validate nội dung khai với cơ quan ngoài (srs-fr-10:1768).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn SRS | Áp dụng? | TC áp dụng |
|----|---------|-----------|----------|-----------|
| BR-AUTH-01 | Xác thực + chỉ QTHT (Tier 1 nội bộ) cho UC112-115 | srs-fr-10:623, 689, 767, 823, 2155 | ✅ | Precondition mọi UC + permission matrix |
| BR-AUTH-02 (v3.1) | Cấu trúc **2 tầng** TW → {BN, ĐP} ngang cấp song song. ĐP.don_vi_cha_id = TW (KHÔNG qua BN) | srs-fr-10:2161, 1602, 1967 | ✅ | UC114 cây render + UC113 tree filter đơn vị |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau (BN/ĐP độc lập) | srs-fr-10:2167 | ✅ | UC114 ERR-PQ-01 ngang cấp + verify policy |
| BR-AUTH-04 | **Chỉ TW** thấy cấp con (TW thấy toàn bộ; BN/ĐP không có cấp con) | srs-fr-10:2173 | ✅ | UC114 cha-con verify |
| BR-AUTH-06 | Session timeout 30 phút idle (CMS) / 15 phút JWT (API) | srs-fr-10:2179 | ✅ | UC113 verify session vẫn còn sau khóa/mở khóa |
| BR-AUTH-07 | Khóa TK sau **5 lần** đăng nhập sai. Auto unlock sau 30 phút HOẶC QTHT mở khóa | srs-fr-10:2185 | ✅ | UC113 lifecycle TAM_KHOA |
| BR-AUTH-08 | Chính sách phân quyền dữ liệu cho mọi bảng có `don_vi_id` | srs-fr-10:2191 | ✅ | UC113 filter cross-tenant + permission matrix |
| BR-AUTH-09 | CB nội bộ chỉ Tier 1, không VNeID | srs-fr-10:2197 | ✅ | UC113 + permission matrix CCCD-only sync (không VNeID cho CB) |
| BR-DATA-01 | Soft delete (`is_deleted=1`) | srs-fr-10:2203 | ✅ | UC112/113 verify DELETE = UPDATE is_deleted |
| BR-DATA-03 | Common fields 7 trường (id, created_at, updated_at, created_by, updated_by, is_deleted, don_vi_id) | srs-fr-10:2215 | ✅ | UC112/113 verify entity DDL qua list_network_requests |
| BR-DATA-05 | Audit trail mọi CUD + đăng nhập + phê duyệt | srs-fr-10:2221 | ✅ | Mọi UC ghi AUDIT_LOG (verify qua module Nhật ký HT W1.1) |
| BR-DATA-07 | Pagination default 20, max 100 | srs-fr-10:2227 | ✅ | UC112/113 list + filter |
| BR-EC-13 | Search sanitize max 200 ký tự + escape SQL/XSS | srs-v3.1.md §B BR-EC-13 | ✅ | TC sanitize search filter + form input |
| **SM-TAIKHOAN v3.1** | 5 states + 12 transitions với CHO_PHAN_QUYEN intermediate | srs-fr-10:2077-2118 | ✅ | UC113 + UC quên MK + UC120 (T1 + T4 path) |
| **UC120-specific** | UC120 dùng BR-DATA-02 (unique MST/email/username — toàn HT, không multi-tenant scope) + BR-AUTH-01 (password strength) + BR-DATA-05 (audit `SELF_REGISTER_DN`). Auto-pass — không validate ngoài (srs-fr-10:1768). | srs-fr-10:1054-1064 | ✅ | UC120 self-reg flow |

### 2.2 Error Codes / Messages

**FR-VIII-14 — Vai trò (UC112):**
- `ERR-VT-01` ERROR — "Mã vai trò '{ma}' đã tồn tại" (E1, srs-fr-10:642)
- `ERR-VT-02` ERROR — "Không thể xóa. Vai trò đang gán cho {N} tài khoản" (E2, srs-fr-10:643)

**FR-VIII-15 — Tài khoản (UC113):**
- `ERR-TK-01` ERROR — "Username '{username}' đã tồn tại" (E1, srs-fr-10:717)
- `ERR-TK-02` ERROR — "Email '{email}' đã được sử dụng" (E2, srs-fr-10:718)
- `ERR-TK-03` ERROR — "Mật khẩu phải >= 8 ký tự, chứa chữ hoa, chữ thường, số và ký tự đặc biệt" `[GAP-VIII-04]` (E3, srs-fr-10:719)
- `ERR-TK-04` ERROR — "Username chỉ chấp nhận chữ cái, số và dấu gạch dưới" (E4, srs-fr-10:720)
- `ERR-TK-05` ERROR — "Đơn vị không tồn tại hoặc đã bị vô hiệu hóa" (E5, srs-fr-10:721)
- `ERR-TK-06` ERROR — "Vai trò ID {id} không tồn tại" (E6, srs-fr-10:722)

**FR-VIII-16 — Phân quyền dữ liệu (UC114):**
- `ERR-PQ-01` ERROR — "Không thể gán quyền xem đơn vị {A} cho vai trò thuộc đơn vị {B} (ngang cấp)" (E1, srs-fr-10:780)
- `ERR-PQ-02` ERROR — "Vai trò không tồn tại" (E2, srs-fr-10:781)
- `ERR-PQ-03` ERROR — "Đơn vị ID {id} không tồn tại" (E3, srs-fr-10:782)

**FR-VIII-17 — Phân quyền chức năng (UC115):**
- `ERR-PQ-02` ERROR — "Vai trò không tồn tại" (E1, srs-fr-10:833)
- `ERR-PQ-04` ERROR — "Quyền chức năng ID {id} không tồn tại" (E2, srs-fr-10:834)

**FR-VIII-26 — Quên MK / Kích hoạt (v3.1):**
- `ERR-PWD-01` INFO — "Nếu email đã đăng ký, link đặt mật khẩu sẽ được gửi đến hộp thư của bạn" (chống enumerate, E1, srs-fr-10:1290)
- `ERR-PWD-02` ERROR — "Tài khoản đã bị khóa hoặc vô hiệu hóa. Liên hệ quản trị viên để được hỗ trợ" (E2, srs-fr-10:1291)
- `ERR-PWD-03` ERROR — "Link đặt mật khẩu đã hết hạn. Vui lòng yêu cầu link mới" (E3, srs-fr-10:1292)
- `ERR-PWD-04` ERROR — "Link đặt mật khẩu đã được sử dụng. Vui lòng yêu cầu link mới" (E4, srs-fr-10:1293)
- `ERR-PWD-05` ERROR — "Mật khẩu chưa đủ mạnh" (E5, srs-fr-10:1294)
- `ERR-PWD-06` ERROR — "Mật khẩu xác nhận không khớp" (E6, srs-fr-10:1295)

**FR-VIII-22 — Self-registration DN (UC120):**
- `ERR-REG-01` ERROR — "Mã số thuế này đã đăng ký trong hệ thống" (E1, srs-fr-10:1070)
- `ERR-REG-02` ERROR — "Email đã được sử dụng" (E2, srs-fr-10:1071)
- `ERR-REG-03` ERROR — "Tên đăng nhập đã được sử dụng" (E3, srs-fr-10:1072)
- `ERR-REG-04` ERROR — "Mật khẩu chưa đủ mạnh" (E4, srs-fr-10:1073)
- `ERR-REG-05` ERROR — "Mật khẩu xác nhận không khớp" (E5, srs-fr-10:1074)
- `ERR-REG-06` ERROR — "Vui lòng đồng ý Điều khoản sử dụng để tiếp tục" (E6, srs-fr-10:1075)

**Cross-cutting (khi không có quyền):**
- `403 Forbidden` + toast "Bạn không có quyền truy cập" (BR-AUTH-01) — áp dụng cho mọi non-QTHT vào UC112-115.

### 2.3 Permission Matrix

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | NHT/TVV/CG/DN |
|--------|------|------------------|-------------------|---------------|
| UC112 — CRUD Vai trò | ✅ | ❌ 403 | ❌ 403 | ❌ Tier 2 không vào CMS |
| UC113 — CRUD Tài khoản | ✅ | ❌ 403 | ❌ 403 | ❌ |
| UC113 — Khóa/Mở khóa/VHH/Khôi phục | ✅ | ❌ 403 | ❌ 403 | ❌ |
| UC113 — Phê duyệt CHO_PHAN_QUYEN | ✅ | ❌ 403 | ❌ 403 | ❌ |
| UC114 — Phân quyền dữ liệu | ✅ | ❌ 403 | ❌ 403 | ❌ |
| UC115 — Phân quyền chức năng | ✅ | ❌ 403 | ❌ 403 | ❌ |
| FR-VIII-26 — Quên MK | ✅ | ✅ | ✅ | ✅ (DN/NHT/TVV/CG email-based, không cần đăng nhập) |
| FR-VIII-26 — Kích hoạt lần đầu | — | — | — | ✅ TVV/NHT/DN (token vĩnh viễn cho self-reg DN) |
| **UC120 — DN self-registration** | — (chỉ admin/audit) | ❌ (CB không tự đăng ký — phải qua FR-VIII-15) | ❌ | ✅ **public** (chỉ DN; NHT/TVV/CG đăng ký qua quy trình riêng — srs-fr-10:1734) |

> **Iron rule:** UC112-115 thuần QTHT. CB_NV_BN/DP/TW dù làm việc với data của TKPQ vẫn KHÔNG được vào — không có ngoại lệ "ngang cấp" như Mẫu phản hồi (Mô hình B Hybrid). FR-VIII-26 ngược lại — public link, mọi role có email đều dùng được.

### 2.4 State Machine — SM-TAIKHOAN (5 states, 12 transitions) — srs-fr-10:2077-2118

| ID | Từ | Đến | Trigger | Guard | Action | FR Ref |
|----|----|-----|---------|-------|--------|--------|
| T1 | [*] | CHO_KICH_HOAT | QTHT tạo TK / User self-register DN | — | Gửi email kích hoạt | FR-VIII-15, FR-VIII-22 |
| T2 | CHO_KICH_HOAT | CHO_PHAN_QUYEN | User kích hoạt qua email (self-registration cũ — chưa có vai trò) | Token hợp lệ + `vai_tro IS NULL` | TB QTHT gán quyền | FR-VIII-22 (legacy) + v3.1 FR-VIII-26 step 11 |
| T3 | CHO_PHAN_QUYEN | HOAT_DONG | QTHT duyệt + gán vai trò + đơn vị | vai_tro + don_vi đã gán | Cho phép đăng nhập | FR-VIII-15 (modal phê duyệt SCR-VIII-08a) |
| T4 | CHO_KICH_HOAT | HOAT_DONG | User kích hoạt qua mail (đã có vai trò sẵn — TVV/NHT/DN) | Token hợp lệ + `vai_tro IS NOT NULL` | Cho phép đăng nhập + trigger TVV/NHT.HOAT_DONG | FR-VIII-26 step 11 + FR-VIII-22 step 7 (DN v3.1 vai trò DN gán sẵn → chạy nhánh T4, KHÔNG qua T2/T3) |
| T5 | CHO_KICH_HOAT | HOAT_DONG | QTHT kích hoạt thủ công (đã gán quyền) | — | Cho phép đăng nhập | FR-VIII-15 button "Kích hoạt" |
| T6 | HOAT_DONG | TAM_KHOA | Auto: 5 lần đăng nhập sai | so_lan_sai >= 5 | Ghi AUDIT, TB QTHT | FR-VIII-20 BR-AUTH-07 |
| T7 | HOAT_DONG | TAM_KHOA | QTHT khóa thủ công | — | Ghi AUDIT | FR-VIII-15 button "Khóa" |
| T8 | TAM_KHOA | HOAT_DONG | QTHT mở khóa | — | Reset so_lan_sai = 0 | FR-VIII-15 button "Mở khóa" |
| T9 | TAM_KHOA | HOAT_DONG | Auto: sau 30 phút | elapsed >= 30 phút | Reset so_lan_sai = 0 | FR-VIII-20 BR-AUTH-07 |
| T10 | HOAT_DONG | VO_HIEU_HOA | QTHT vô hiệu hóa | — | Invalidate session, ghi AUDIT | FR-VIII-15 |
| T11 | VO_HIEU_HOA | HOAT_DONG | QTHT khôi phục | — | Cho phép đăng nhập lại | FR-VIII-15 |
| T12 | CHO_KICH_HOAT | VO_HIEU_HOA | Auto: quá 7 ngày chưa kích hoạt | activation_token_expired | Ghi AUDIT, TB QTHT | (auto) |

> **TC coverage SM-TAIKHOAN:** Mỗi transition T1-T12 có ≥ 1 TC trong `02-TC-tai-khoan.md` hoặc `05-TC-quen-mk-kich-hoat.md`. Verify guard + action + audit log entry.

### 2.5 Inputs & Validation Fields

**UC112 — Vai trò (4 inputs, srs-fr-10:612-617):**

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `ma_vai_tro` | text | Y | Unique toàn HT | — |
| 2 | `ten_vai_tro` | text | Y | Không trống | — |
| 3 | `mo_ta` | text | N | — | — |
| 4 | `trang_thai` | toggle (boolean) | Y | 1=Hoạt động, 0=Vô hiệu hóa | 1 |

> Note ERD VAI_TRO (srs-fr-10:1985-1989): có thêm field `cap` (TW/BN/DP/ALL, mặc định ALL) — KHÔNG hiện trong form UC112 input nhưng hiện trong `cap` filter của UC114. SPEC-CLARIFY-TKPQ-01.

**UC113 — Tài khoản (9 inputs, srs-fr-10:673-683 + SCR-VIII-03 #17-24 srs-fr-10:1553-1560):**

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `username` | text | Y | Unique, **4-50 ký tự**, chỉ a-z0-9_ (regex) | — |
| 2 | `email` | text | Y | Unique, RFC 5322 | — |
| 3 | `ho_ten` | text | Y | — | — |
| 4 | `dien_thoai` | text | N | — | — |
| 5 | `mat_khau` | password | Y (tạo mới) | ≥ 8 ký tự, chữ hoa+thường+số+đặc biệt `[GAP-VIII-04]` | — |
| 6 | `vai_tro_ids` | multi-select | Y | Chọn ≥ 1 từ VAI_TRO | — |
| 7 | `don_vi_id` | tree-select | Y | FK → DON_VI | — |
| 8 | `loai_tai_khoan` | select | Y | UC111 DANH_MUC | — |
| 9 | `cccd` | text | N | 12 chữ số (validate format, không unique vì optional) | — |
| 10 | `trang_thai` | system | Y | enum 5 giá trị (xem SM) | CHO_KICH_HOAT |

**UC114 — Phân quyền dữ liệu (3 inputs, srs-fr-10:758-761):**

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `vai_tro_id` | dropdown | Y | FK → VAI_TRO | — |
| 2 | `don_vi_ids` | tree-checkbox | Y | Cây 2-tầng TW → BN/ĐP, ngang cấp KHÔNG cùng vai trò | — |
| 3 | `entity_type` | text | N | null = áp dụng tất cả entity | null |

**UC115 — Phân quyền chức năng (2 inputs + 6 cột quyền, srs-fr-10:814-817 + SCR-VIII-04 #2-8):**

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `vai_tro_id` | dropdown | Y | FK → VAI_TRO | — |
| 2 | `quyen_ids[]` | matrix checkbox | Y | 6 cột × N menu (Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất) | — |

**FR-VIII-26 — Quên MK / Kích hoạt (4 inputs, srs-fr-10:1260-1265):**

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| 1 | `email` | text | Y | RFC 5322 | — |
| 2 | `reset_token` | text (URL param) | Y | Sinh hệ thống | — |
| 3 | `mat_khau_moi` | password | Y | ≥ 8 ký tự, chữ hoa+thường+số+đặc biệt | — |
| 4 | `mat_khau_xac_nhan` | password | Y | Phải khớp `mat_khau_moi` | — |

**FR-VIII-22 — Self-registration DN (22 inputs, srs-fr-10:1023-1048 + SCR-VIII-08 #1-22 srs-fr-10:1740-1763):**

> Form public chia 2 nhóm: **Nhóm 1 — Thông tin doanh nghiệp** (18 trường, đồng nhất Inputs FR-V.III-01 — DN entity) + **Nhóm 2 — Tài khoản đăng nhập** (4 trường — username/password/confirm/checkbox điều khoản).

| # | Field | Type | Bắt buộc | Constraint | Default |
|---|-------|------|---------|------------|---------|
| **Nhóm 1 — Thông tin DN** | | | | | |
| 1 | `ten_doanh_nghiep` | text | Y | Không rỗng | — |
| 2 | `ma_so_thue` | text | Y | **Unique toàn HT** — khóa định danh DN xuyên suốt (10 hoặc 13 chữ số per chuẩn TCT) | — |
| 3 | `giay_cndk` | text | N | Số Giấy CN đăng ký kinh doanh | — |
| 4 | `dia_chi` | text | Y | Không rỗng | — |
| 5 | `tinh_thanh_id` | tree-select | Y | FK → DON_VI (chỉ chọn cấp tỉnh) | — |
| 6 | `loai_doanh_nghiep_id` | select | Y | FK → DANH_MUC UC105 | — |
| 7 | `quy_mo` | select (enum) | Y | SIEU_NHO / NHO / VUA (theo NĐ 39/2018) | — |
| 8 | `nganh_nghe` | select (enum) | Y | NONG_LAM / CONG_NGHIEP / THUONG_MAI | — |
| 9 | `so_lao_dong` | number | N | ≥ 0 integer | — |
| 10 | `doanh_thu_nam` | number | N | ≥ 0 (tỷ VNĐ) | — |
| 11 | `tong_nguon_von` | number | N | ≥ 0 (tỷ VNĐ) | — |
| 12 | `nguoi_dai_dien` | text | Y | Họ tên người đại diện pháp luật | — |
| 13 | `chuc_vu_dd` | text | N | Chức vụ người đại diện | — |
| 14 | `email` | text | Y | **RFC 5322 + Unique toàn HT** — dùng nhận mail kích hoạt | — |
| 15 | `so_dien_thoai` | text | Y | Số điện thoại liên hệ | — |
| 16 | `linh_vuc_kinh_doanh` | text | N | Lĩnh vực kinh doanh chính | — |
| 17 | `ghi_chu` | textarea | N | — | — |
| 18 | `file_dinh_kem` | file-upload (multi) | N | Giấy ĐKKD, chứng từ phụ | — |
| **Nhóm 2 — Tài khoản** | | | | | |
| 19 | `username` | text | Y | **4-50 ký tự + Unique toàn HT** | — |
| 20 | `mat_khau` | password | Y | ≥ 8 ký tự, chữ hoa + chữ thường + số + ký tự đặc biệt; có indicator độ mạnh | — |
| 21 | `mat_khau_xac_nhan` | password | Y | Phải khớp `mat_khau` | — |
| 22 | `dong_y_dieu_khoan` | checkbox | Y | Phải tích đồng ý Điều khoản sử dụng + Chính sách quyền riêng tư | unchecked |

### 2.6 Output Columns / Outputs

**UC113 List (10 outputs, srs-fr-10:700-711 + SCR-VIII-03 #10-16):** Username | Họ tên | Email | Đơn vị | Vai trò (multi-tag màu) | Loại TK | Trạng thái (badge 5 màu) | Ngày tạo | Lần đăng nhập cuối | Hành động.

**Trạng thái badge (5 màu, srs-fr-10:1546):** HOAT_DONG xanh / CHO_KICH_HOAT vàng / TAM_KHOA đỏ / VO_HIEU_HOA đen / CHO_PHAN_QUYEN xanh dương.

**Tab counter (srs-fr-10:1539):** Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa / Chờ phân quyền (mỗi tab có số đếm).

---

## 3. Cấu Trúc File Test Case

```
QTHT/Tai-khoan-phan-quyen/
├── 00-test-plan-overview.md           ← file này (A2)
├── 01-TC-vai-tro.md                   ← FR-VIII-14 UC112 (27 TC, A3+A4+A6+Codex R2)
├── 02-TC-tai-khoan.md                 ← FR-VIII-15 UC113 (65 TC, A3+A4+A6+Codex R2 +3 fill BR) — file lớn nhất
├── 03-TC-phan-quyen-du-lieu.md        ← FR-VIII-16 UC114 (22 TC, A3+A4+A6+Codex R2)
├── 04-TC-phan-quyen-chuc-nang.md      ← FR-VIII-17 UC115 (19 TC, A3+A4+A6+Codex R2)
├── 05-TC-quen-mk-kich-hoat.md         ← FR-VIII-26 v3.1 (30 TC, A3+A4+A6+Codex R2 +2 BR-EC-13)
├── 06-TC-permission-matrix.md         ← Role-based UI access cross-FR (21 TC, A3+A4)
├── 07-TC-security-IDOR.md             ← **NEW Codex R2** Security/IDOR suite (16 TC, tách từ 5 file UC)
├── 08-REVIEW-edge-case-hunter.md      ← A4 audit log (proposal + merge mapping; 2026-05-10 append UC120)
├── 09-traceability-matrix.md          ← A5 BR/AC ↔ TC matrix (Codex R2 update; 2026-05-10 append UC120)
├── 10-REVIEW-test-quality.md          ← A6 6-axis quality score (Codex R2 update; 2026-05-10 append UC120)
├── 11-a7-filter-log.md                ← A7 filter UI/function-testable log (Codex R2 update; 2026-05-10 append UC120)
└── 12-TC-self-registration-dn.md      ← **NEW v1.1 2026-05-10** FR-VIII-22 UC120 self-registration DN (Phase A A1-A7)
```

> **Phase B B-block ref CHỈ 7 file UC functional (01-06 + 12)**, total **184 + UC120 TC**. File 07 là Security/IDOR suite chạy độc lập (security/dev team), không nằm trong functional Phase B. Tổng grand total: **200 + UC120 TC**. File 08/09/10/11 là audit log, KHÔNG phải TC source.

---

## 4. Coverage Target

| Loại | Target | Note |
|------|--------|------|
| BR coverage | 100% | 14 BR áp dụng — BR-AUTH-01..09 + BR-DATA-01/02/03/05/07 + BR-EC-13 + SM-TAIKHOAN |
| AC coverage | 100% | 20 AC tổng (3 + 4 + 3 + 2 + 4 across 5 UC + 4 UC120) |
| Error code coverage | 100% | 25 ERR codes (2+6+3+2+6 across 5 UC + 6 ERR-REG UC120) |
| SM-TAIKHOAN transitions | 100% | 12 transitions T1-T12 đều có ≥1 TC. UC120 cover T1 + T4 paths (DN role pre-assigned) |
| Permission combo | 100% | 4 nhóm role × 5 UC + IDOR cross-tenant + public path UC120 (no auth) |
| Field validation (BVA + EP) | ≥95% | username 4-50 boundary, password ≥8, email RFC, CCCD 12 digits, ma_vai_tro unique, **MST 10/13 chữ số TCT, 22 trường UC120** |
| Negative path | ≥1 TC/error code + boundary off-by-one | — |

---

## 5. Open Items / SPEC-CLARIFY

| ID | Mô tả | SRS line | Action |
|----|-------|----------|--------|
| SPEC-CLARIFY-TKPQ-01 | VAI_TRO ERD có field `cap` (TW/BN/DP/ALL) nhưng UC112 form input không có. Có phải ẩn auto-set theo cấp QTHT tạo, hay BA defer cấp = ALL mặc định? | srs-fr-10:1988 vs 612-617 | Test theo behavior hiện tại; query NotebookLM xác nhận. |
| SPEC-CLARIFY-TKPQ-02 | UC113 input có `loai_tai_khoan` (UC111 DANH_MUC) nhưng UC111 chưa rõ enum. Có chấp nhận tự định nghĩa (NOI_BO/DOANH_NGHIEP/...)? | srs-fr-10:682, 575 | Test với DANH_MUC seed có ≥ 2 loại; confirm BA. |
| SPEC-CLARIFY-TKPQ-03 | SCR-VIII-08a (modal phê duyệt) chỉ ở UC120 self-reg DN, nhưng SM-TAIKHOAN T3 (CHO_PHAN_QUYEN → HOAT_DONG) áp dụng cho self-reg cũ. UC113 có modal/form phê duyệt riêng cho TKPQ không, hay reuse SCR-VIII-08a? | srs-fr-10:1772-1786 vs 2110 | Test theo flow thực tế (button "Phê duyệt" tab "Chờ phân quyền"); nếu không có UI riêng → log GAP. |
| SPEC-CLARIFY-TKPQ-04 | FR-VIII-26 step 11 nguyên văn "Nếu TK đang CHO_KICH_HOAT + chưa có vai trò → CHO_PHAN_QUYEN". Nhưng SM-TAIKHOAN T2 ghi trigger là "User kích hoạt qua email" (self-reg). Có 2 tình huống khác nhau hay là 1? | srs-fr-10:1281 vs 2109 | Test cả 2 tình huống: (a) DN tự đăng ký kích hoạt; (b) QTHT tạo TK chưa gán vai trò → user click link → CHO_PHAN_QUYEN; verify guard. |
| SPEC-CLARIFY-TKPQ-05 | UC114 ERR-PQ-01 nguyên văn "Không thể gán quyền xem đơn vị {A} cho vai trò thuộc đơn vị {B} (ngang cấp)". Nhưng VAI_TRO không có `don_vi_id` (chỉ có `cap`). Vậy "vai trò thuộc đơn vị" được suy ra như thế nào? | srs-fr-10:780 + 1985-1989 | Test với vai trò có `cap=BN` cố gán đơn vị thuộc DP → expect ERR-PQ-01. Confirm BA cách suy. |
| SPEC-CLARIFY-TKPQ-06 | SCR-VIII-04 line 1583 có nút "[Reset về mặc định]" cho phân quyền chức năng. Nhưng SRS Processing FR-VIII-17 không nói rõ "mặc định" là gì (template theo loại vai trò?). | srs-fr-10:1583 vs 819-827 | Test thực tế: click Reset → quan sát quyền load. Nếu rỗng → log SPEC-CLARIFY. |
| SPEC-CLARIFY-TKPQ-07 | UC113 button "Đổi MK" trên cột Hành động (SCR-VIII-03 #16, srs-fr-10:1547). QTHT có thể đổi MK trực tiếp (qua form UC113) hay luôn phải dùng FR-VIII-26 (gửi mail link)? | srs-fr-10:1547 | Test cả 2 path; nếu UC113 có form đổi MK riêng → verify validation password strength + audit log. |
| SPEC-CLARIFY-TKPQ-08 | FR-VIII-26 không nói rate-limiting cho request "Quên MK". Có thể spam trigger gửi mail liên tục? | srs-fr-10:1271-1284 | Test gửi liên tục 10 request → verify behavior (rate limit / debounce / silent OK). NotebookLM verify. |
| SPEC-CLARIFY-TKPQ-09 | SM-TAIKHOAN T12 (CHO_KICH_HOAT → VO_HIEU_HOA quá 7 ngày) — auto job. Nhưng FR-VIII-26 v3.1 step 3 nói "vĩnh viễn nếu là kích hoạt lần đầu". Có conflict không? | srs-fr-10:1273 vs 2118 | Test: tạo TK CHO_KICH_HOAT → chờ 8 ngày simulation → verify trạng thái (vẫn CHO_KICH_HOAT theo FR-VIII-26 hay VO_HIEU_HOA theo SM-T12). NotebookLM verify. |
| SPEC-CLARIFY-TKPQ-10 | UC115 cây menu (cột trái) — "Phân cấp module: Dashboard / Hỏi đáp / Đào tạo / ..." (srs-fr-10:1575). Cây cụ thể bao nhiêu node? Có sub-menu (vd Vụ việc → Tab DS / Tab Tạo) không? | srs-fr-10:1575 | Test thực tế UI: count node cây + verify cha-con cascade. |
| SPEC-CLARIFY-TKPQ-11 | FR-VIII-26 step 12 trigger "TU_VAN_VIEN.trang_thai từ CHO_KICH_HOAT → HOAT_DONG". Nhưng entity TU_VAN_VIEN có state machine SM-TVV riêng (srs-fr-04). Trigger này có conflict guard SM-TVV? | srs-fr-10:1282 + srs-fr-04 SM-TVV | Test với TVV mới được CB Phê duyệt (T-TVV-X) → verify song song chuyển state TVV + TK. NotebookLM cross-check. |
| **SPEC-CLARIFY-TKPQ-30 (NEW UC120)** | FR-VIII-22 step 7 nói: "Tạo TK ở CHO_KICH_HOAT, gán vai trò DN sẵn (KHÔNG qua CHO_PHAN_QUYEN — vì vai trò DN đã rõ)". Nhưng SM-TAIKHOAN T2 (line 2109) vẫn ghi `CHO_KICH_HOAT → CHO_PHAN_QUYEN | self-registration | FR-VIII-22`. Hai chỗ MÂU THUẪN. Spec dự kiến T4 path (vai_tro IS NOT NULL → HOAT_DONG) cho UC120, nhưng bảng SM còn legacy T2. | srs-fr-10:1060 vs 2109 | Test theo flow FR-VIII-22 step 7 + FR-VIII-26 step 11 (T4 path); query NotebookLM verify intent. Nếu app implement theo T2 (sai spec mới) → log bug Phase B. |
| **SPEC-CLARIFY-TKPQ-31 (NEW UC120)** | MST format. SRS chỉ ghi "Unique toàn HT" (srs-fr-10:1027) không nêu chuẩn TCT 10/13 chữ số. Có validate format không hay chỉ check unique? | srs-fr-10:1027 | Test BVA: 9 / 10 / 11 / 12 / 13 / 14 chữ số + chữ + ký tự đặc biệt → quan sát behavior (reject vs accept với note "auto-pass"). Nếu app accept tùy ý → log GAP/SPEC-CLARIFY. |
| **SPEC-CLARIFY-TKPQ-32 (NEW UC120)** | Form mở từ link nào? SRS line 1722-1723 ghi button "Đăng ký (dành cho doanh nghiệp)" trong SCR-VIII-07 (login). UX-Spec cũng có thể có URL public direct (`/dang-ky-doanh-nghiep` chẳng hạn). Public URL có cần CSRF token không? | srs-fr-10:1722-1723 + 1728 | Test: navigate SCR-VIII-07 → click button → verify URL. Direct goto URL public → verify accessible. Network check CSRF cookie set. |
| **SPEC-CLARIFY-TKPQ-33 (NEW UC120)** | File đính kèm (#18) — SRS chỉ ghi "binary[] tùy chọn multi". Không nêu max size, max file count, allowed extension. Anti-virus scan? | srs-fr-10:1043 + 1758 | Test BVA: 1 file 100MB / 10 file × 10MB / .exe / .pdf / EICAR test virus → quan sát reject vs accept. Mặc định fallback theo BR-DATA chung (xem srs-v3.1 §B). |
| **SPEC-CLARIFY-TKPQ-34 (NEW UC120)** | SRS step 10 "gửi mail link kích hoạt vĩnh viễn 1 lần dùng". "Vĩnh viễn" mâu thuẫn với SM-TAIKHOAN T12 (CHO_KICH_HOAT → VO_HIEU_HOA quá 7 ngày). Cùng vấn đề SPEC-CLARIFY-TKPQ-09. | srs-fr-10:1063 vs 2118 | Test simulation 8 ngày → trạng thái mong đợi. NotebookLM xác nhận. |
| **SPEC-CLARIFY-TKPQ-35 (NEW UC120)** | UC120 step 1 "Kiểm tra mã số thuế chưa tồn tại" áp dụng BR-DATA-02 (line 1054). Nhưng BR-DATA-02 nguyên văn "Multi-tenant scoping — mọi bản ghi nghiệp vụ PHẢI có don_vi_id NOT NULL" (line 2208). Đây không phải BR về unique. SRS dùng BR-DATA-02 sai context? | srs-fr-10:1054 vs 2208 | Test unique MST/email/username toàn HT (logic spec đúng); ghi nhận BR ref có thể sai trong SRS. Đề xuất BA correct sang BR khác (vd "BR-DATA-XX Unique constraint"). |
| **SPEC-CLARIFY-TKPQ-36 (NEW UC120)** | Cancel "Hủy" — có hiển thị confirm dialog "Bạn có chắc muốn hủy?" khi form đã có dữ liệu nhập? Hay redirect thẳng về login? | srs-fr-10:1766 | Test: nhập vài field → click Hủy → quan sát dialog. |
| **SPEC-CLARIFY-TKPQ-37 (NEW UC120)** | Login với TK chưa kích hoạt — error message cụ thể là gì? KHÔNG nằm trong ERR-REG-XX (đó là registration); có thể là ERR-AUTH-XX (login). SRS không liệt kê tường minh. | srs-fr-10:1078-1083 | Test: tạo TK CHO_KICH_HOAT → cố login → quan sát text. |
| **SPEC-CLARIFY-TKPQ-38 (NEW UC120)** | Field length max — SRS không cap explicit cho ten_doanh_nghiep, dia_chi, ghi_chu, email (chỉ ghi RFC 5322). Default DB varchar 255? Email RFC 5322 = 254 chars max. | srs-fr-10:1023-1048 | Test BVA boundary 255/256 cho ten_doanh_nghiep, 254 cho email. |
| **SPEC-CLARIFY-TKPQ-39 (NEW UC120)** | so_dien_thoai regex VN — SRS chỉ ghi "Số điện thoại liên hệ", không nêu format. App có validate `0[3-9]\d{8,9}` hay accept international `+84...`? | srs-fr-10:1040 | Test BVA: VN format / international / chữ. |
| **SPEC-CLARIFY-TKPQ-40 (NEW UC120)** | Password strength indicator (SCR-VIII-08 #20 ghi "có indicator độ mạnh") — implement chưa? Real-time react với keystroke + autofill? | srs-fr-10:1761 | Test: gõ tăng dần → quan sát indicator. |
| **SPEC-CLARIFY-TKPQ-41 (NEW UC120)** | CB nội bộ truy cập SCR-VIII-08 (vì public route). Submit form → tạo TK DN mới? Hay block / cảnh báo? Theo srs-fr-10:1734 vai trò khác KHÔNG có form tự đăng ký, nhưng UI public không phân biệt. | srs-fr-10:1734 | Test: CB login → goto SCR-VIII-08 → submit → quan sát. |
| **SPEC-CLARIFY-TKPQ-42 (NEW UC120, A4)** | Re-register với MST đã soft-delete / email TK đã VO_HIEU_HOA — unique check có filter is_deleted/HOAT_DONG không? Sibling cross-ref TKPQ-15 cũ pattern. | srs-fr-10:1027, 1039, 1054-1055 | Test BVA: tạo DN/TK → soft delete/VHH → re-register cùng MST/email → quan sát. |
| **SPEC-CLARIFY-TKPQ-43 (NEW UC120, A4)** | Email IDN (Unicode local-part / domain) — RFC 5322 KHÔNG hỗ trợ IDN; RFC 6531 mới hỗ trợ. SRS chỉ ghi RFC 5322 (line 1039) → chuẩn nào áp dụng? | srs-fr-10:1039 | Test: email Unicode → quan sát accept/reject. |

---

## 6. Liên kết

- SRS FR-VIII-14: `input/srs-v3/srs-fr-10-quan-tri-v3.1.md` lines 595-653
- SRS FR-VIII-15: lines 656-735
- SRS FR-VIII-16: lines 738-793
- SRS FR-VIII-17: lines 796-843
- SRS FR-VIII-22 (UC120 self-reg DN, NEW v1.1): lines 1005-1089
- SRS FR-VIII-26 (v3.1): lines 1241-1311
- SCR-VIII-02 (Vai trò): lines 1499-1520
- SCR-VIII-03 (Tài khoản NSD): lines 1522-1561
- SCR-VIII-04 (PQ Chức năng): lines 1564-1588
- SCR-VIII-05 (PQ Dữ liệu): lines 1591-1606
- SCR-VIII-07 (Đăng nhập — button "Đăng ký dành cho doanh nghiệp" #11): lines 1701-1725
- SCR-VIII-08 (Đăng ký TK DN — form 24 thành phần): lines 1728-1768
- SCR-VIII-08a (QTHT phê duyệt TK đăng ký — chỉ liên quan UC120 nếu app implement T2 path; theo v3.1 KHÔNG dùng cho UC120): lines 1772-1786
- SM-TAIKHOAN: lines 2077-2118
- BR Phụ lục B: `input/srs-v3/srs-v3.1.md` (BR-AUTH-01..09, BR-DATA-01/03/05/07, BR-EC-13)
- Sibling W1.1 Nhật ký HT: `output/test-cases/QTHT/Nhat-ky-he-thong/00-test-plan-overview.md`
- Sibling W1.2 Cấu hình HT: `output/test-cases/QTHT/Cau-hinh-he-thong/00-test-plan-overview.md`
- Plan: `Ver3.1/tasks/detailed-tc/plan.md` §3.1 Phase A workflow
- NotebookLM SRS: https://notebooklm.google.com/notebook/4dd0675e-a4fa-4ea6-80ae-48e76b3fa264 (verify trước khi log bug Phase B)
