# Kế Hoạch Kiểm Thử — Hồ sơ cá nhân + Đổi mật khẩu (cross-cutting)

> **Phiên bản**: 1.1 (Revised 2026-05-12 13:00:00 — apply review REVISE 8 gap + 8 suggestion)
> **Ngày tạo**: 2026-05-12
> **SOURCE MODE**: LOCAL
> **Nguồn dữ liệu**: `srs-update-2026-5-5/ho-so-doi-mat-khau.md` (spec mới v3.5, không có baseline v3 riêng) + cross-ref `srs-update-2026-5-5/srs-fr-10-quan-tri.md` FR-VIII-26
> **SRS Reference**:
> - `srs-update-2026-5-5/ho-so-doi-mat-khau.md:1-26` (spec gốc tab Thông tin cá nhân + tab Bảo mật / Đổi mật khẩu)
> - `srs-update-2026-5-5/_DELTA-MAP-PROFILE-PWD.md` (delta map, mâu thuẫn rule MK profile vs FR-VIII-26)
> - `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1248-1316` (FR-VIII-26 Quên MK / Kích hoạt — KHÔNG cover ở plan này, chỉ dùng cross-ref rule MK)
> - `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1588` (SCR-VIII-03 "Đổi MK" button trên hàng QTHT — ngoài scope plan này)
> - `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1952-1964` (entity TAI_KHOAN: email, mat_khau_hash, so_lan_dang_nhap_sai, token_reset_mk)

> **Scope clarify (theo `_DELTA-MAP-PROFILE-PWD.md` §2 Mâu thuẫn 2):**
> - ✅ **Cover trong plan này:** Đổi MK SELF-SERVICE (user đang login → trang `/profile` tab Bảo mật, cần `currentPassword`) + Sửa hồ sơ cá nhân (hoTen, dienThoai, avatar).
> - ❌ **KHÔNG cover (đã có plan riêng tại fr-10-qtht):** Reset MK qua link mail FR-VIII-26 (chưa login, dùng token URL) + Kích hoạt TK lần đầu (TVV/NHT/CG/DN — token vĩnh viễn).

---

## 1. Phạm Vi Kiểm Thử

### 1.1 Chức năng được kiểm thử
- **Module cross-cutting:** áp dụng cho mọi role đã đăng nhập (11 role — xem §1.3). Mỗi user đều có entry "Hồ sơ cá nhân" trên header (top-right dropdown).
- **2 tab trong trang `/profile`:**
  - Tab "Thông tin cá nhân" — xem + sửa thông tin cá nhân (read-only: username/email/vaiTro; editable: hoTen, dienThoai, ảnh đại diện).
  - Tab "Bảo mật" — form đổi mật khẩu (3 field: currentPassword, newPassword, newPasswordConfirm).
- **Bảng dữ liệu chính:** `TAI_KHOAN` (đọc + write một số field own scope per `auth.userId`).
- **Màn hình:** `/profile` (1 SCR duy nhất, 2 tab) — không có SCR ID chính thức trong SRS (gap — xem §5 mâu thuẫn).

### 1.2 Danh sách FR / UC

| # | Mã FR | Use Case | Tên chức năng | Entity | File Test Case |
|---|---|---|---|---|---|
| 1 | (no FR) | UC-PROFILE-01 | Xem hồ sơ cá nhân của chính mình | TAI_KHOAN | `01-TC-xem-ho-so.md` |
| 2 | (no FR) | UC-PROFILE-02 | Sửa hồ sơ cá nhân (hoTen + dienThoai + avatar) | TAI_KHOAN | `02-TC-sua-ho-so.md` |
| 3 | (no FR) | UC-PWD-01 | Đổi mật khẩu self-service (tài khoản LOCAL) | TAI_KHOAN | `03-TC-doi-mat-khau.md` |
| 4 | FR-VIII-26 (cross-ref) | UC-PWD-VNeID | Ẩn / disable tab Bảo mật cho tài khoản VNeID | TAI_KHOAN | `04-TC-vneid-readonly.md` |

> **Chú thích "no FR":** Spec `ho-so-doi-mat-khau.md` chỉ 26 dòng (1 file riêng) — chưa được gán mã FR chính thức trong SRS v3.5. Đây là gap đã ghi `_DELTA-MAP-PROFILE-PWD.md` §2 Mâu thuẫn 3 (thiếu Acceptance + ERR code + permission matrix). Plan này tạm dùng UC-PROFILE-* / UC-PWD-* làm placeholder, chờ BA cấp FR ID.

### 1.3 Tài khoản & role liên quan — TẤT CẢ 11 role áp dụng

> **Iron rule cross-cutting:** Mọi role đăng nhập được vào hệ thống đều có quyền xem + sửa hồ sơ CỦA CHÍNH MÌNH (BR-AUTH-11 self-scope). KHÔNG có role nào bị ẩn entry "Hồ sơ cá nhân".

| Role | Cấp | Username (users.csv) | Tài khoản loại | Dùng cho TC loại |
|---|---|---|---|---|
| QTHT | — | `qtht_01` | LOCAL | CRUD hồ sơ own + Đổi MK self-service. Primary. `_02` fallback, `_03` permission test cross-user |
| CB_NV_TW | TW | `cb_nv_tw_01` | LOCAL | CRUD hồ sơ own (CB nội bộ) |
| CB_NV_BN | BN | `cb_nv_bn_01` | LOCAL | CRUD hồ sơ own |
| CB_NV_DP | ĐP | `cb_nv_dp_01` | LOCAL | CRUD hồ sơ own |
| CB_PD_TW | TW | `cb_pd_tw_01` | LOCAL | CRUD hồ sơ own |
| CB_PD_BN | BN | `cb_pd_bn_01` | LOCAL | CRUD hồ sơ own |
| CB_PD_DP | ĐP | `cb_pd_dp_01` | LOCAL | CRUD hồ sơ own |
| DN | — | `9999999990` (MST) | LOCAL hoặc VNeID Tổ chức | CRUD hồ sơ own. Test cả VNeID readonly. |
| NHT | ĐP | `nht_01` | LOCAL hoặc VNeID Cá nhân | CRUD hồ sơ own |
| TVV | — | `huongcg` (proxy TVV) | LOCAL hoặc VNeID Cá nhân | CRUD hồ sơ own |
| CG | — | `huongcg` | LOCAL hoặc VNeID Cá nhân | CRUD hồ sơ own |

> Reference: [input/users.csv](../../../input/users.csv), [output/permission-matrix.md](../../../output/permission-matrix.md), [input/test-accounts-isolation.csv](../../../input/test-accounts-isolation.csv) (usage guide permission cross-user).

---

## 2. Quy Tắc Nghiệp Vụ Trích Xuất Từ SRS

### 2.1 Business Rules (BR)

| Mã | Quy tắc | Nguồn (SRS line) | Áp dụng module này? | Ngoại lệ SRS-quoted | TC áp dụng |
|---|---|---|---|---|---|
| BR-AUTH-02 | Phân cấp 3 tầng TW/BN/ĐP | `srs-v3/srs-v3.md:3950` | ✅ Yes (precondition login) | — | TC-01 precondition |
| BR-AUTH-08 | Phân quyền dữ liệu theo `don_vi_id` (self-scope = user chỉ xem/sửa hồ sơ của chính mình) | `srs-v3/srs-v3.md:3958` | ✅ Yes (self-scope) | — | TC-12 cross-user 403 |
| BR-AUTH-11 | Self-scope: user CRUD được hồ sơ của chính mình bất kể role | `srs-v3/srs-v3.md:3961` (cross-cutting) | ✅ Yes (default cho mọi role) | — | TC-01..TC-05 |
| BR-AUTH-PROFILE-01 | `hoTen` bắt buộc, max 200 ký tự; `dienThoai` optional, format `0[3-9]xxxxxxxx` 10 số; để trống = xoá | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:11-12` | ✅ Yes | — | TC-04 negative validate |
| BR-AUTH-PROFILE-02 | `username`, `email`, `vaiTro` read-only trên trang profile | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:9, 10, 13` | ✅ Yes | "VNeID account: email đồng bộ tự động từ VNeID" (`ho-so-doi-mat-khau.md:10`) | TC-02 verify read-only |
| BR-AUTH-PWD-01 | MK profile: ≥8 ký tự + chữ hoa + chữ thường + số (KHÔNG yêu cầu ký tự đặc biệt) | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:22` | ✅ Yes (profile self-service) | — | TC-06..TC-09 negative validate MK |
| BR-AUTH-PWD-02 | Cần nhập `currentPassword` để xác thực trước khi đổi MK | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:21` | ✅ Yes | — | TC-08 currentPassword sai |
| BR-AUTH-PWD-03 | `newPasswordConfirm` phải khớp `newPassword` | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:23` | ✅ Yes | — | TC-09 confirm mismatch |
| BR-AUTH-PWD-04 | Sau đổi MK thành công → auto đăng xuất các phiên đăng nhập trên thiết bị khác | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:25` | ✅ Yes | — | TC-10 multi-session invalidate |
| BR-AUTH-PWD-05 | Tài khoản VNeID KHÔNG dùng MK nội bộ — đổi MK trên hệ thống VNeID | `srs-update-2026-5-5/ho-so-doi-mat-khau.md:17` | ✅ Yes (tab Bảo mật disabled / hidden cho VNeID user) | — | TC-11 VNeID readonly |
| BR-DATA-05 | Audit trail mọi thao tác CUD (đổi MK, sửa hồ sơ ghi `AUDIT_LOG`) | `srs-v3/srs-v3.md:3976` | ✅ Yes | — | TC-13 verify AUDIT_LOG INSERT |
| BR-EC-13 | Search/input sanitize max 200 ký tự, escape SQL/XSS | `srs-v3/srs-v3.md:4078` | ✅ Yes | — | TC-04 XSS hoTen field |

> **Bổ sung BR specific module:** BR-AUTH-PROFILE-01/02 + BR-AUTH-PWD-01..05 là module-specific. BR cross-cutting (AUTH/DATA/EC) đã giữ. **Mâu thuẫn rule MK** Profile (4 thành phần) vs FR-VIII-26 reset (5 thành phần — thêm ký tự đặc biệt) — xem §5 mâu thuẫn 1, cần BA confirm.

### 2.2 Error Codes

> ⚠️ Spec `ho-so-doi-mat-khau.md` THIẾU error code section (xem `_DELTA-MAP-PROFILE-PWD.md` §2 Mâu thuẫn 3). Bảng dưới là PROPOSED, cần BA cấp chính thức.

| Mã lỗi (proposed) | Điều kiện trigger | Message expected | Severity |
|---|---|---|---|
| ERR-PROFILE-01 | `hoTen` để trống | "Họ tên là bắt buộc" | ERROR |
| ERR-PROFILE-02 | `hoTen` > 200 ký tự | "Họ tên tối đa 200 ký tự" | ERROR |
| ERR-PROFILE-03 | `dienThoai` sai format `0[3-9]xxxxxxxx` | "Số điện thoại không đúng định dạng (10 số, bắt đầu 03/05/07/08/09)" | ERROR |
| ERR-PWD-PROFILE-01 | `currentPassword` sai | "Mật khẩu hiện tại không đúng" | ERROR |
| ERR-PWD-PROFILE-02 | `newPassword` không đủ độ mạnh (≥8 + hoa + thường + số) | "Mật khẩu mới phải tối thiểu 8 ký tự, gồm chữ hoa, chữ thường và số" | ERROR |
| ERR-PWD-PROFILE-03 | `newPasswordConfirm` ≠ `newPassword` | "Xác nhận mật khẩu không khớp" | ERROR |
| ERR-PWD-PROFILE-04 | `newPassword` == `currentPassword` (proposed extra) | "Mật khẩu mới không được trùng mật khẩu hiện tại" | ERROR — chờ BA confirm |

### 2.3 Permission Matrix (module-specific) — TẤT CẢ 11 role đều CRUD hồ sơ own

> ⚠️ **Cross-cutting rule:** Không có role nào "không xem được hồ sơ cá nhân". Mọi user đăng nhập được = có entry profile. Cột "Self" = thao tác trên hồ sơ của chính user (own scope). Cột "Other" = thao tác trên hồ sơ của user khác.

| Action / Role | QTHT | CB_NV_TW | CB_NV_BN | CB_NV_DP | CB_PD_TW | CB_PD_BN | CB_PD_DP | DN | NHT | TVV | CG |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Xem hồ sơ Self | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R | ✅ R |
| Sửa `hoTen` Self | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U |
| Sửa `dienThoai` Self | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U |
| Đổi MK Self (LOCAL) | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U | ✅ U |
| Đổi MK Self (VNeID) | n/a | n/a | n/a | n/a | n/a | n/a | n/a | ❌ disable | ❌ disable | ❌ disable | ❌ disable |
| Xem/sửa hồ sơ Other | ❌ 403 self-scope | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 | ❌ 403 |

> **Lưu ý QTHT:** QTHT có entry "Quản lý tài khoản" RIÊNG ở module QTHT (FR-VIII-15 + nút "Đổi MK" tại SCR-VIII-03 cột Hành động — `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1588`) để reset MK user khác. Đó là CHỨC NĂNG KHÁC, KHÔNG phải `/profile`. Plan này KHÔNG cover QTHT-as-admin reset MK của user khác.

### 2.4 UI Layout (`/profile` — gap SCR ID)

> ⚠️ **Spec gap:** `ho-so-doi-mat-khau.md` không có UX-Spec MH-XX.Y SCR ID. UI layout dưới đây inferred từ field list + naming convention "tab" (line 5, 15).

**Components (proposed dựa trên field list):**
- **Toolbar:** Breadcrumb `Trang chủ > Hồ sơ cá nhân`. Nút back optional.
- **Tabs (top):** [Thông tin cá nhân] | [Bảo mật].
- **Tab "Thông tin cá nhân" — Form:**
  - `username` (read-only display, không phải input).
  - `email` (read-only display; nếu VNeID account → thêm badge "Đồng bộ từ VNeID").
  - `hoTen` (input text, required, max 200).
  - `dienThoai` (input text, optional, regex `0[3-9]xxxxxxxx`).
  - `vaiTro` (read-only display — list role được gán; nếu user đa vai trò thì hiển thị tất cả).
  - Avatar upload (optional — proposed, gap SRS).
  - Nút [Lưu thay đổi] + [Hủy].
- **Tab "Bảo mật" — Form đổi MK:**
  - `currentPassword` (password input, required, show/hide toggle).
  - `newPassword` (password input, required, ≥8 + hoa + thường + số; indicator độ mạnh đề xuất).
  - `newPasswordConfirm` (password input, required, phải khớp).
  - Nút [Đổi mật khẩu] + [Hủy].
  - **Nếu tài khoản VNeID:** tab disabled hoặc hiện thông báo "Tài khoản VNeID — đổi mật khẩu trên hệ thống VNeID" (BR-AUTH-PWD-05).

**Cross-cutting features MẶC ĐỊNH có (theo BR global):**
- ☐ Audit log mọi CUD (BR-DATA-05) — đổi MK + sửa hoTen/dienThoai ghi `AUDIT_LOG`.
- ☐ Input sanitize 200 chars + escape XSS (BR-EC-13) — áp dụng `hoTen` (input free text).
- ☐ Optimistic lock UPDATE (BR-EC-01) — `version` field trên TAI_KHOAN khi 2 phiên cùng sửa hoTen.

**Feature module KHÔNG có (cần QUOTE SRS hoặc SPEC-CLARIFY):**
- Export Excel — không áp dụng (không phải module list).
- Pagination — không áp dụng.
- Filter / Search — không áp dụng.
- Toolbar Thêm mới / Xóa — không áp dụng (1-1 self-scope).

### 2.5 State Machine — KHÔNG áp dụng

Module này là form CRUD đơn giản, không có workflow phê duyệt, không có state machine. Trạng thái `TAI_KHOAN.trang_thai` (HOAT_DONG / TAM_KHOA / CHO_KICH_HOAT) được quản lý ở FR-VIII-15 + FR-VIII-26, KHÔNG đổi qua trang `/profile`.

### 2.6 Data dependencies & Seed / Workflow input

| Phase | Input file | Section dùng |
|---|---|---|
| **Precondition login** | [`input/users.csv`](../../../input/users.csv) | 11 account 11 role HOAT_DONG (xem §1.3) |
| **TAI_KHOAN entity ref** | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1952-1964` | Schema 12 field — verify mat_khau_hash, email, so_lan_dang_nhap_sai |
| **VNeID account ref** | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1145, 1207-1218` | Cách phân biệt LOCAL vs VNeID account để test BR-AUTH-PWD-05 |
| **Cross-ref FR-VIII-26** | `srs-update-2026-5-5/srs-fr-10-quan-tri.md:1248-1316` | Rule MK reset (KHÁC rule profile — xem §5 mâu thuẫn 1) |

**Upstream dependencies:**

| Entity của module | Tier | Phụ thuộc entity nào (upstream) | Seed trước tại module |
|---|:-:|---|---|
| `TAI_KHOAN` (self-scope) | 1 | — (entity gốc) | FR-VIII-15 (CB nội bộ + QTHT) + FR-VIII-22 (DN đăng ký) + FR-IV-07 (TVV/CG) + FR-IV-NHT-01 (NHT) |

> **Note:** Không cần seed mới cho plan này — chỉ cần có account HOAT_DONG để login (đã có sẵn 11 role trong `users.csv`). Test VNeID readonly cần ít nhất 1 account loại `LOAI_DK = VNEID` — gap nếu chưa có (cần seed FR-VIII-25 đồng bộ VNeID).

---

## 3. Cấu Trúc File Test Case

```
ho-so-doi-mat-khau/
├── test-plan.md                         ← File này
├── 01-TC-xem-ho-so.md                   ← UC-PROFILE-01 (read view 11 role)
├── 02-TC-sua-ho-so.md                   ← UC-PROFILE-02 (edit hoTen + dienThoai + avatar)
├── 03-TC-doi-mat-khau.md                ← UC-PWD-01 (đổi MK self-service LOCAL)
├── 04-TC-vneid-readonly.md              ← UC-PWD-VNeID (tab Bảo mật disabled cho VNeID)
└── 05-TC-permission-cross-user.md       ← Permission BR-AUTH-08 self-scope (other 403)
```

---

## 4. Tổng Quan Số Lượng Test Cases — 18 TC (revised 2026-05-12 13:00:00)

| TC ID | Tên TC ngắn | Loại | Priority | BR liên quan |
|---|---|---|:-:|---|
| TC-01 | Login QTHT → xem `/profile` tab Thông tin cá nhân, verify 5 field đúng dữ liệu DB | Happy | P0 | BR-AUTH-PROFILE-02 |
| TC-02 | Verify `username`, `email`, `vaiTro` read-only (không có input editable) trên 11 role | Happy | P0 | BR-AUTH-PROFILE-02 |
| TC-03 | Sửa `hoTen` (200 ký tự valid) + `dienThoai` (`0987654321` valid) → Save → reload verify DB persist | Happy | P0 | BR-AUTH-PROFILE-01 |
| TC-04 | Negative `hoTen`: để trống → ERR-PROFILE-01; > 200 ký tự → ERR-PROFILE-02; chèn XSS `<script>alert(1)</script>` → escape | Negative | P0 | BR-AUTH-PROFILE-01 + BR-EC-13 |
| TC-05 | Negative `dienThoai`: `0123456789` (đầu 1) / `09876` (5 số) / `abcd123456` → ERR-PROFILE-03 | Negative | P1 | BR-AUTH-PROFILE-01 |
| TC-06 | Đổi MK happy path LOCAL: `Secret@123` → `NewSecret123` (8+hoa+thường+số) → toast success + reload login với MK mới | Happy | P0 | BR-AUTH-PWD-01..03 |
| TC-06b | Sau TC-06: login lại với MK CŨ → expect FAIL `ERR-AUTH-INVALID-CRED` (positive-negative pair verify đổi MK persist DB, không phải "echo success") | Negative | P0 | BR-AUTH-PWD-01..03 |
| TC-07 | Negative `newPassword` độ mạnh (parameterized theo BA decision rule MK): `short` (5 ký tự) / `alllowercase` (thiếu hoa+số) / `12345678` (thiếu chữ) → ERR-PWD-PROFILE-02. **Nếu BA chốt 5 thành phần (Mâu thuẫn 1 §5) → thêm sub-case `Abc12345` (8+hoa+thường+số, THIẾU ký tự đặc biệt) → expect FAIL.** | Negative | P0 | BR-AUTH-PWD-01 |
| TC-08 | Negative `currentPassword` sai → ERR-PWD-PROFILE-01 + KHÔNG đổi MK trong DB (verify TC-06b vẫn login được MK cũ) | Negative | P0 | BR-AUTH-PWD-02 |
| TC-09 | Negative `newPasswordConfirm` mismatch (`Abc12345` vs `Abc12346`) → ERR-PWD-PROFILE-03 | Negative | P0 | BR-AUTH-PWD-03 |
| TC-10 | Multi-device invalidate sau đổi MK: (a) login session 1 (browser A) + session 2 (incognito B) cùng account → (b) đổi MK ở session 1 → (c) session 2 gọi `/api/v1/auth/me` qua `list_network_requests` → expect 401 (access token revoke server-side) + UI redirect `/login`. (d) Verify session 1 (đổi MK) KHÔNG bị invalidate, tiếp tục thao tác OK. (e) Đo timing invalidate ≤ ? giây (record). **Quirk:** `qa_htpldn_jwt_revoke_aggressive` — BE revoke JWT ~2 phút bất chấp `exp` claim; phải tách session đổi MK vs session bị invalidate để loại false positive từ TTL natural. | Edge | P1 | BR-AUTH-PWD-04 |
| TC-11 | VNeID readonly tab Bảo mật — áp dụng CHỈ cho DN/NHT/TVV/CG (4 role có thể LOAI_DK=VNEID). CB nội bộ (QTHT/CB_NV/CB_PD) luôn LOCAL → N/A. `[need: ≥1 VNeID account HOAT_DONG (✗ chờ seed FR-VIII-25)]` | Edge | P1 | BR-AUTH-PWD-05 |
| TC-12 | Cross-user permission: user A login → cố GET/PATCH endpoint profile của user_B qua DevTools → expected 403. **Endpoint phải verify thực tế qua MCP `list_network_requests` khi load `/profile`** trước khi viết TC (có thể `/api/v1/auth/me` / `/api/v1/users/me` / `/api/v1/tai-khoans/{id}` — SRS không nói rõ URL pattern). KHÔNG đoán endpoint. | Negative | P0 | BR-AUTH-08 (self-scope) |
| TC-13 | Audit log verify: sau TC-03 (sửa hoTen) + TC-06 (đổi MK) → query AUDIT_LOG row `PROFILE_UPDATE` + `PASSWORD_CHANGE` (action codes — gap, cần BA confirm). **Method:** ưu tiên endpoint admin Audit log viewer (nếu QTHT có UI). Nếu KHÔNG có endpoint API public → defer Nhóm F (DB-level only, DBA query). | Edge | P1 | BR-DATA-05 |
| TC-14 | Cross-role entry-point smoke 11 role: mỗi role login → verify entry "Hồ sơ cá nhân" visible trên header dropdown + click → landing `/profile` KHÔNG 403/blank. **KHÔNG lặp verify 5 field** (đã cover TC-01/TC-02). Scope thuần entry-point. | Happy | P0 | BR-AUTH-11 cross-cutting |
| TC-15 | Avatar upload (defer nếu BA bỏ field — Mâu thuẫn 4 §5): upload PNG/JPG ≤2MB → preview + Save → reload verify persist. Negative: SVG/exe format → reject; >2MB → reject. | Edge | P2 | BR-AUTH-PROFILE-01 (extend) |
| TC-16 | TAM_KHOA login + đổi MK behavior (gap permission §2.3): user state `trang_thai=TAM_KHOA` login → (a) login fail trực tiếp? (b) login OK nhưng đổi MK fail? **Defer Nhóm C — chờ BA quyết spec.** | Edge | P2 | BR-AUTH-PWD-01 (extend) |
| TC-17 | Rate-limit đổi MK liên tục (S8 review): 5 lần đổi MK trong 1 phút → BE có 429/cooldown không? Spec không nói. **Defer Nhóm C — chờ BA quyết.** | Edge | P2 | BR-AUTH-PWD-01 (extend) |

| File | Happy | Negative | Edge | Tổng |
|---|:-:|:-:|:-:|:-:|
| 01-TC-xem-ho-so.md | TC-01, TC-02, TC-14 | — | — | 3 |
| 02-TC-sua-ho-so.md | TC-03 | TC-04, TC-05 | TC-15 (avatar) | 4 |
| 03-TC-doi-mat-khau.md | TC-06 | TC-06b, TC-07, TC-08, TC-09 | TC-10, TC-16, TC-17 | 8 |
| 04-TC-vneid-readonly.md | — | — | TC-11 | 1 |
| 05-TC-permission-cross-user.md | — | TC-12 | — | 1 |
| (audit cross-cut) | — | — | TC-13 | 1 |
| **TỔNG** | **4** | **7** | **7** | **18** |

**Phân bổ priority:**

| Priority | Số TC | % |
|---|--:|--:|
| P0 (bắt buộc) | 10 | 56% |
| P1 (quan trọng) | 5 | 28% |
| P2 (nên có) | 3 | 16% |

---

## 5. Tiêu chí đạt/không đạt + Open issues

> Reference: [output/test-strategy.md §10](../../../output/test-strategy.md)

- ✅ **PASS:** 100% P0 (9 TC) + 90% P1 (≥5/5 thực ra do nhỏ) pass.
- ❌ **FAIL:** bất kỳ P0 nào FAIL, hoặc P1 pass rate < 90%.

### Open issues — Cần BA confirm trước khi viết TC detail

Theo `_DELTA-MAP-PROFILE-PWD.md` §5:

1. **Mâu thuẫn 1 — Password rule:** Profile MK `≥8 + hoa + thường + số` (4 thành phần — `ho-so-doi-mat-khau.md:22`) vs FR-VIII-26 reset MK `≥8 + hoa + thường + số + ký tự đặc biệt` (5 thành phần — `srs-fr-10-quan-tri.md:1271`). **Plan này tạm theo rule profile 4 thành phần (BR-AUTH-PWD-01).** Cần BA chốt: thống nhất 1 rule hay giữ 2 rule khác nhau cho self-service vs admin-reset.
2. **Mâu thuẫn 2 — VNeID tab Bảo mật:** Ẩn hoàn toàn (hide) hay disable + message redirect? Plan này theo "disable + message" (BR-AUTH-PWD-05 TC-11). Cần BA confirm UI.
3. **Mâu thuẫn 3 — Action code AUDIT_LOG:** `PROFILE_UPDATE` / `PASSWORD_CHANGE` chưa được spec confirm. TC-13 expected action code cần BA cấp.
4. **Mâu thuẫn 4 — Avatar field:** Spec line 5-13 không mention avatar. Plan này đề xuất TC nhưng đánh dấu gap. Cần BA confirm có hay không.
5. **Mâu thuẫn 5 — Permission scope DN sửa hoTen:** DN có được sửa `hoTen` của tài khoản đăng nhập (= chủ DN) không, hay chỉ admin DN sửa được? Plan này mặc định "có" (BR-AUTH-11 self-scope). Cần BA confirm.
6. **Mâu thuẫn 6 — Multi-device invalidate cơ chế:** BR-AUTH-PWD-04 nói "auto đăng xuất các phiên đăng nhập trên thiết bị khác" — implement bằng revoke JWT hay bump password version field? Plan này TC-10 chỉ verify HÀNH VI (session 2 bị invalidate), không verify CƠ CHẾ.

### Gap SRS — block phải có BA quyết trước khi RUN

- ❌ Không có SCR ID chính thức cho `/profile` (gap §2.4).
- ❌ Không có ERR code chính thức cho 6 validation error (gap §2.2 — proposed).
- ❌ Không có permission matrix dedicated cho profile (gap — plan tự inferred từ BR-AUTH-11 + BR-AUTH-08).

---

## 5.1 Bảng trạng thái TC — snapshot SKELETON (chưa run)

> Theo CLAUDE.md (enforced 2026-05-10): mỗi report sau Verdict phải có Bảng 1 + Bảng 2. Plan này có sẵn skeleton 18 dòng — tester fill round phát hiện + status sau khi RUN.

| TC ID | Tên TC ngắn | Status | Round phát hiện | Note (≤15 từ) |
|---|---|:-:|:-:|---|
| TC-01 | QTHT xem `/profile` verify 5 field | ⏳ chưa run | — | — |
| TC-02 | 11 role verify username/email/vaiTro read-only | ⏳ chưa run | — | — |
| TC-03 | Sửa hoTen + dienThoai + save persist DB | ⏳ chưa run | — | — |
| TC-04 | Negative hoTen (empty / >200 / XSS) | ⏳ chưa run | — | Tách 3 sub-case khi viết detail |
| TC-05 | Negative dienThoai regex | ⏳ chưa run | — | — |
| TC-06 | Đổi MK happy path LOCAL | ⏳ chưa run | — | — |
| TC-06b | MK cũ KHÔNG login được (verify persist DB) | ⏳ chưa run | — | Pair với TC-06 |
| TC-07 | Negative newPassword độ mạnh (4 vs 5 thành phần) | ⏳ chưa run | — | Parameterize chờ BA |
| TC-08 | Negative currentPassword sai | ⏳ chưa run | — | — |
| TC-09 | Negative newPasswordConfirm mismatch | ⏳ chưa run | — | — |
| TC-10 | Multi-device invalidate + 401 verify + timing | ⏳ chưa run | — | Quirk JWT revoke ~2 phút |
| TC-11 | VNeID tab Bảo mật disabled (4 role) | ⏳ chưa run | — | Nhóm A — seed VNeID account |
| TC-12 | Cross-user 403 (verify endpoint thực tế trước) | ⏳ chưa run | — | Verify endpoint qua MCP trước |
| TC-13 | Audit log verify | ⏳ chưa run | — | Nhóm F nếu không có API admin |
| TC-14 | Entry-point smoke 11 role | ⏳ chưa run | — | Thuần entry visible + landing 200 |
| TC-15 | Avatar upload (PNG/JPG/SVG/size) | ⏳ chưa run | — | Nhóm C — Mâu thuẫn 4 BA confirm |
| TC-16 | TAM_KHOA login + đổi MK | ⏳ chưa run | — | Nhóm C — gap permission spec |
| TC-17 | Rate-limit đổi MK liên tục | ⏳ chưa run | — | Nhóm C — spec không nói |
| **Tổng** | **18 TC** | ✅0 · ⚠️0 · ❌0 · 🚫0 · ⏭0 · 🤷0 · ⏳18 | | |

## 5.2 Bảng TC chưa chạy được — cần làm gì để chạy

> Hiện tại 18/18 TC chưa run (plan v1.1 chưa được execute). 6 TC đã pre-identified blocker (Nhóm A/C/F) — cần xử lý song song trước hoặc trong round run.

| TC ID | Vì sao chưa chạy được | Cần làm gì để chạy | Ai làm |
|---|---|---|:-:|
| TC-07 (5 thành phần) | Rule MK 4 vs 5 thành phần spec mâu thuẫn (Mâu thuẫn 1 §5) | BA chốt thống nhất rule cho self-service vs admin-reset | BA |
| TC-11 | Chưa có VNeID account HOAT_DONG cho DN/NHT/TVV/CG | Seed FR-VIII-25 đồng bộ VNeID ≥1 account/4 role | QA seed |
| TC-12 | Endpoint profile cross-user chưa biết URL pattern thực tế | Login QTHT, mở `/profile`, capture `list_network_requests` ghi endpoint thực | QA API |
| TC-13 | AUDIT_LOG verify chưa có API admin / chỉ DB-level | (a) BA confirm có API admin Audit log viewer? (b) Nếu không → DBA query | BA / DBA |
| TC-15 | Spec không xác định avatar có field không (Mâu thuẫn 4 §5) | BA chốt có / không avatar trên `/profile` | BA |
| TC-16 | Spec không nói TAM_KHOA login + đổi MK behavior | BA quyết: TAM_KHOA login fail / login OK nhưng đổi MK fail | BA |
| TC-17 | Spec không có rate-limit rule đổi MK | BA xác nhận có rate-limit không + ngưỡng | BA |

**Tóm tắt nhóm block:** 4 TC chờ BA confirm spec (Nhóm C: TC-07/15/16/17) · 1 TC chờ seed (Nhóm A: TC-11) · 1 TC chờ QA verify endpoint thực tế (Nhóm A method: TC-12) · 1 TC chờ BA + DBA (TC-13 Nhóm C/F).

---

## 6. Tham chiếu

- [input/srs-update-2026-5-5/ho-so-doi-mat-khau.md](../../../input/srs-update-2026-5-5/ho-so-doi-mat-khau.md) — spec gốc 26 dòng (v3.5 mới)
- [input/srs-update-2026-5-5/_DELTA-MAP-PROFILE-PWD.md](../../../input/srs-update-2026-5-5/_DELTA-MAP-PROFILE-PWD.md) — delta map + 3 mâu thuẫn critical + 5 open issue
- [input/srs-update-2026-5-5/srs-fr-10-quan-tri.md](../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) — cross-ref FR-VIII-26 (reset MK qua mail — KHÔNG cover plan này) + entity TAI_KHOAN schema (line 1952-1964) + SCR-VIII-03 (nút "Đổi MK" QTHT-as-admin — không cover plan này)
- [input/users.csv](../../../input/users.csv) — 11 role accounts cho cross-cutting test
- [output/test-strategy.md](../../../output/test-strategy.md) — chiến lược tổng thể
- [output/permission-matrix.md](../../../output/permission-matrix.md) — ma trận phân quyền 49 entity × 11 role
- [output/template/test-case-template.md](../../../output/template/test-case-template.md) — template TC field-level
- [output/template/bug-report-template.md](../../../output/template/bug-report-template.md) — template bug report

---

*Plan generated 2026-05-12. SOURCE MODE: LOCAL. Module S cross-cutting áp dụng 11 role. State machine: không có. Gap critical: SCR ID + ERR code + Permission matrix chưa có spec chính thức (chờ BA confirm 6 open issue trước khi viết TC detail).*
