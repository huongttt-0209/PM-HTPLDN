# A5 — Traceability Matrix (FR-VIII-14..17 + FR-VIII-22 + FR-VIII-26)

> **Tác nhân**: bmad-testarch-trace
> **Ngày**: 2026-05-08 · **Cập nhật**: 2026-05-10 (append UC120 / FR-VIII-22)
> **Mục đích**: Map BR / AC / SM transition / Error code / Permission combo ↔ TC ID. Phát hiện gap → forward A6.

---

## 1. BR ↔ TC

| BR ID | Phát biểu | TC bao phủ | Coverage |
|-------|-----------|------------|----------|
| BR-AUTH-01 | Xác thực + chỉ QTHT (Tier 1) cho UC112-115 + password strength UC120 | 01 (TC-101 + TC-132 IDOR), 02 (TC-101 + TC-184 IDOR), 03 (TC-101 + TC-130 IDOR), 04 (TC-101 + TC-130 IDOR), 05 (TC-101 public OK), 06 (TC-001..025), **12 (TC-REG-157..163, 183 password strength)** | ✅ 100% |
| **BR-DATA-02** | Unique constraint MST/email/username toàn HT (UC120) | **12 (TC-REG-180 MST trùng + TC-REG-181 email trùng + TC-REG-182 username trùng + TC-REG-206 MST soft-delete + TC-REG-207 email VHH + TC-REG-199 concurrent MST)** | ✅ 100% (UC120 — KHÔNG dùng cho UC112-115 vì đã có UC-specific ERR codes; xem SPEC-CLARIFY-TKPQ-35 cho note BR-DATA-02 ref context) |
| BR-AUTH-02 v3.1 | Cây 2-tầng TW → {BN, ĐP} ngang cấp song song | 03 (TC-102 cây render + TC-104 cascade), 02 (TC-105 filter đơn vị tree) | ✅ 100% |
| BR-AUTH-03 | Ngang cấp KHÔNG thấy nhau | 03 (TC-120-122 ERR-PQ-01 ba combo) | ✅ 100% |
| BR-AUTH-04 | Chỉ TW thấy cấp con | 03 (TC-104 cascade + TC-105 user view + TC-124 cap=ALL/TW gán BN/DP) | ✅ 100% |
| BR-AUTH-06 | Session timeout 30 phút (CMS) / 15 phút (JWT) | 02 (TC-197 NEW Codex R2 — session 30 phút idle + redirect login) | ✅ 100% (sau Codex R2 fill) |
| BR-AUTH-07 | Khóa TK sau 5 lần sai + auto unlock 30 phút | 02 (TC-136 auto khóa 5 lần + TC-139 auto unlock) | ✅ 100% |
| BR-AUTH-08 | Chính sách phân quyền dữ liệu | 02 (TC-180 cross-tenant), 06 (TC-005, TC-040-041), 03 (TC-131 cache refresh) | ✅ 100% |
| BR-AUTH-09 | CB nội bộ chỉ Tier 1, không VNeID | 02 (TC-198 NEW Codex R2 — VNeID login từ chối CB qua ERR-VN-04) + 07 (TC-IDOR-TK-003 inject vneid_subject API-level) | ✅ 100% (sau Codex R2 fill) |
| BR-DATA-01 | Soft delete | 01 (TC-104 vai trò + TC-128 cross is_deleted), 02 (TC-195 TK soft delete + TC-170 cross is_deleted) — sau Codex R2 verify qua UI list + AUDIT_LOG (không SELECT raw) | ✅ 100% |
| BR-DATA-03 | Common fields 7 trường | 02 (TC-199 NEW Codex R2 — verify network response chứa đủ 7 field qua MCP `list_network_requests`) | ✅ 100% (sau Codex R2 fill) |
| BR-DATA-05 | Audit trail mọi CUD + đăng nhập + phê duyệt + self-register | 01 (TC-130-131), 02 (TC-185-186), 03 (TC-136), 04 (TC-105, 136), 05 (TC-148), 06 (TC-050-051), **12 (TC-REG-190 SELF_REGISTER_DN)** | ✅ 100% |
| BR-DATA-07 | Pagination default 20, max 100 | 01 (TC-109), 02 (TC-192-193) | ✅ 100% |
| BR-EC-13 | Search sanitize max 200 ký tự + escape SQL/XSS | 01 (TC-125-126), 02 (TC-182-183), 05 (TC-146 + TC-151 NEW Codex R2 boundary 200 + TC-152 over 201), **12 (TC-REG-113 ten XSS)** | ✅ 100% (sau Codex R2 boundary fill + UC120) |
| **SM-TAIKHOAN** | 12 transitions T1-T12 | 02 (TC-130-142) + 05 (TC-102/103/105/106 transitions từ FR-VIII-26) + **12 (TC-REG-195 T1 + TC-REG-196 T4 v3.1 path)** | ✅ 100% |

**BR Coverage Summary (sau Codex R2 fill + UC120 2026-05-10):** 15/15 ✅ 100% — BR-AUTH-06/09, BR-DATA-02 (UC120 unique), BR-DATA-03, BR-EC-13 boundary đều có TC. **Avg 100%**.

---

## 2. AC ↔ TC

### UC112 (FR-VIII-14) — 3 AC (srs-fr-10:649-652)

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | QTHT truy cập danh sách + phân trang | 01 TC-101, TC-109 |
| AC2 | Thêm mới vai trò đầy đủ trường → lưu thành công | 01 TC-102, TC-103 |
| AC3 | Xóa vai trò đang gán cho TK → từ chối | 01 TC-123 |

### UC113 (FR-VIII-15) — 4 AC (srs-fr-10:730-734)

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | QTHT truy cập danh sách + phân trang + filter (vai trò/đơn vị/trạng thái) | 02 TC-101, TC-103-110 |
| AC2 | Thêm mới TK → tạo + gửi mail kích hoạt | 02 TC-115 |
| AC3 | Khóa TK | 02 TC-137 |
| AC4 | Mở khóa TK | 02 TC-138 |

### UC114 (FR-VIII-16) — 3 AC (srs-fr-10:789-792)

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | Chọn vai trò X → load quyền hiện tại | 03 TC-101 |
| AC2 | Gán quyền dữ liệu → user thuộc X chỉ thấy data đơn vị Y | 03 TC-103, TC-105 |
| AC3 | Quy tắc: ngang cấp KHÔNG thấy nhau, cha thấy con | 03 TC-104, TC-120-124 |

### UC115 (FR-VIII-17) — 2 AC (srs-fr-10:840-842)

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | Chọn vai trò → cây menu + bật/tắt | 04 TC-101, TC-108 |
| AC2 | Gán quyền cho vai trò → user truy cập menu | 04 TC-102, TC-103, TC-107 |

### FR-VIII-26 — 4 AC (srs-fr-10:1306-1310)

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | TVV mới → kích hoạt mail → đặt MK lần đầu → TVV + TK đồng thời HOAT_DONG | 05 TC-102 + TC-142 |
| AC2 | NHT mới → tương tự AC1 | 05 TC-103 + TC-143 |
| AC3 | User HOAT_DONG quên MK → nhận mail link 30 phút → reset OK | 05 TC-101 + TC-104 + TC-106 |
| AC4 | Email không tồn tại → thông báo trung tính (chống enumerate) | 05 TC-120 |

### FR-VIII-22 (UC120) — 4 AC (srs-fr-10:1085-1088) **NEW 2026-05-10**

| AC | Mô tả | TC bao phủ |
|----|-------|------------|
| AC1 | DN truy cập SCR-VIII-07 → bấm "Đăng ký" → form 22 trường mở | 12 TC-REG-101 |
| AC2 | DN điền đủ thông tin + submit → tạo TAI_KHOAN CHO_KICH_HOAT + DOANH_NGHIEP + gửi mail kích hoạt | 12 TC-REG-102 + TC-REG-190 audit + TC-REG-195 SM verify |
| AC3 | DN bấm link kích hoạt + đặt MK → TAI_KHOAN HOAT_DONG → DN đăng nhập | 12 TC-REG-103 + TC-REG-196 T4 + TC-REG-197 portal access |
| AC4 | MST/email đã tồn tại → ERR-REG-01/02 reject | 12 TC-REG-180 + TC-REG-181 |

**AC Coverage Summary: 20/20 = 100%** (tăng từ 16 → 20 sau UC120 4 AC)

---

## 3. Error Code ↔ TC

| Error Code | Severity | Message | TC bao phủ |
|-----------|----------|---------|------------|
| ERR-VT-01 | ERROR | "Mã vai trò '{ma}' đã tồn tại" | 01 TC-120 |
| ERR-VT-02 | ERROR | "Không thể xóa. Vai trò đang gán cho {N} tài khoản" | 01 TC-123 |
| ERR-TK-01 | ERROR | "Username '{username}' đã tồn tại" | 02 TC-150 |
| ERR-TK-02 | ERROR | "Email '{email}' đã được sử dụng" | 02 TC-151, TC-170 |
| ERR-TK-03 | ERROR | "Mật khẩu phải >= 8 ký tự, chứa chữ hoa, chữ thường, số và ký tự đặc biệt" | 02 TC-152, TC-153 |
| ERR-TK-04 | ERROR | "Username chỉ chấp nhận chữ cái, số và dấu gạch dưới" | 02 TC-155, TC-183 |
| ERR-TK-05 | ERROR | "Đơn vị không tồn tại hoặc đã bị vô hiệu hóa" | 02 TC-160 |
| ERR-TK-06 | ERROR | "Vai trò ID {id} không tồn tại" | 02 TC-161 |
| ERR-PQ-01 | ERROR | "Không thể gán quyền xem đơn vị {A} cho vai trò thuộc đơn vị {B} (ngang cấp)" | 03 TC-120, TC-121, TC-122 |
| ERR-PQ-02 | ERROR | "Vai trò không tồn tại" | 03 TC-125, 04 TC-120 |
| ERR-PQ-03 | ERROR | "Đơn vị ID {id} không tồn tại" | 03 TC-126 |
| ERR-PQ-04 | ERROR | "Quyền chức năng ID {id} không tồn tại" | 04 TC-121 |
| ERR-PWD-01 | INFO | Trung tính "Nếu email đã đăng ký, link đặt mật khẩu sẽ được gửi đến hộp thư của bạn" | 05 TC-120 |
| ERR-PWD-02 | ERROR | "Tài khoản đã bị khóa hoặc vô hiệu hóa..." | 05 TC-121, TC-122 |
| ERR-PWD-03 | ERROR | "Link đặt mật khẩu đã hết hạn..." | 05 TC-123, TC-129 |
| ERR-PWD-04 | ERROR | "Link đặt mật khẩu đã được sử dụng..." | 05 TC-124 |
| ERR-PWD-05 | ERROR | "Mật khẩu chưa đủ mạnh" | 05 TC-125, TC-126 |
| ERR-PWD-06 | ERROR | "Mật khẩu xác nhận không khớp" | 05 TC-128 |
| ERR-DN-04 | ERROR | "Tài khoản đã bị tạm khóa do đăng nhập sai quá 5 lần" (cross UC118) | 02 TC-136 |
| **ERR-REG-01** | ERROR | "Mã số thuế này đã đăng ký trong hệ thống" (UC120 E1, srs-fr-10:1070) | 12 TC-REG-180, TC-REG-199 (concurrent) |
| **ERR-REG-02** | ERROR | "Email đã được sử dụng" (UC120 E2, srs-fr-10:1071) | 12 TC-REG-181, TC-REG-207 (VHH soft-delete edge) |
| **ERR-REG-03** | ERROR | "Tên đăng nhập đã được sử dụng" (UC120 E3, srs-fr-10:1072) | 12 TC-REG-182 |
| **ERR-REG-04** | ERROR | "Mật khẩu chưa đủ mạnh" (UC120 E4, srs-fr-10:1073) | 12 TC-REG-183, TC-REG-157..162 (5 nhóm) |
| **ERR-REG-05** | ERROR | "Mật khẩu xác nhận không khớp" (UC120 E5, srs-fr-10:1074) | 12 TC-REG-184, TC-REG-165 |
| **ERR-REG-06** | ERROR | "Vui lòng đồng ý Điều khoản sử dụng để tiếp tục" (UC120 E6, srs-fr-10:1075) | 12 TC-REG-185, TC-REG-166 |

**Error Coverage: 25/25 = 100%** (tăng từ 19 → 25 sau UC120 6 ERR-REG)

---

## 4. SM-TAIKHOAN Transitions ↔ TC

| ID | Từ | Đến | Trigger | TC bao phủ |
|----|----|-----|---------|------------|
| T1 | [*] | CHO_KICH_HOAT | QTHT tạo TK / User self-reg DN | 02 TC-115, TC-130, **12 TC-REG-102 (UC120 self-reg) + TC-REG-195 verify state** |
| T2 | CHO_KICH_HOAT | CHO_PHAN_QUYEN | User kích hoạt mail (vai_tro NULL — luồng cũ) | 05 TC-105, 02 TC-131 |
| T3 | CHO_PHAN_QUYEN | HOAT_DONG | QTHT phê duyệt + gán vai trò + đơn vị | 02 TC-132 (+ TC-133 negative) |
| T4 | CHO_KICH_HOAT | HOAT_DONG | User kích hoạt mail (vai_tro NOT NULL — TVV/NHT/DN v3.1) | 02 TC-134 + 05 TC-102, TC-103, **12 TC-REG-103 (UC120 DN activate) + TC-REG-196 verify v3.1 path** |
| T5 | CHO_KICH_HOAT | HOAT_DONG | QTHT kích hoạt thủ công | 02 TC-135 |
| T6 | HOAT_DONG | TAM_KHOA | Auto 5 lần sai | 02 TC-136 |
| T7 | HOAT_DONG | TAM_KHOA | QTHT khóa thủ công | 02 TC-137 |
| T8 | TAM_KHOA | HOAT_DONG | QTHT mở khóa | 02 TC-138 |
| T9 | TAM_KHOA | HOAT_DONG | Auto 30 phút | 02 TC-139 |
| T10 | HOAT_DONG | VO_HIEU_HOA | QTHT vô hiệu hóa | 02 TC-140 |
| T11 | VO_HIEU_HOA | HOAT_DONG | QTHT khôi phục | 02 TC-141 |
| T12 | CHO_KICH_HOAT | VO_HIEU_HOA | Auto > 7 ngày | 02 TC-142 |

**SM Coverage: 12/12 = 100%**

---

## 5. Permission Combo ↔ TC

| Action | QTHT | CB_NV (TW/BN/DP) | CB_PD (TW/BN/DP) | Tier 2 (DN/CG/TVV/NHT) | Public no-auth |
|--------|------|------------------|-------------------|-------------------------|----------------|
| UC112 | 01 TC-101..103 / 06 TC-001 | 06 TC-010-012 | 06 TC-013 | 06 TC-014 | — |
| UC113 | 02 TC-101..119 / 06 TC-002 | 06 TC-015-016 | 06 TC-016 | 06 TC-014 (cùng pattern) | — |
| UC114 | 03 TC-101..107 / 06 TC-003 | 06 TC-017 | 06 TC-017 | (cross TC-014) | — |
| UC115 | 04 TC-101..108 / 06 TC-004 | 06 TC-018 | 06 TC-018 | (cross TC-014) | — |
| FR-VIII-26 (Quên MK) | 05 TC-101 / 06 TC-032 | 06 TC-032 (CB cross) | 06 TC-032 | 06 TC-030 + 05 TC-101 (DN), TC-102 (TVV), TC-103 (NHT) | — |
| **UC120 (Self-reg DN)** | (audit/view qua UC113 — **12 TC-REG-190/195/196**) | (CB submit edge — **12 TC-REG-193/194**, SPEC-CLARIFY-TKPQ-41) | (cùng pattern CB) | (DN — không qua VNeID, dùng form public) | **✅ 12 TC-REG-101 (truy cập từ login) + TC-REG-192 (direct URL)** |
| IDOR | — | 06 TC-020-025 | 06 TC-020-025 (cross) | (Tier 2 không có JWT CMS) | (UC120 public — không có IDOR concept) |

**Permission Coverage: 100%** (5 UC × 4 nhóm role + IDOR + public access UC120 đều có TC)

---

## 6. Field Validation Coverage (BVA + EP)

| Field | Constraint | TC boundary |
|-------|------------|-------------|
| ma_vai_tro | Unique, max length implicit | 01 TC-120 (unique), TC-124 (60 chars), TC-127 (case), TC-128 (cross is_deleted), TC-135 (unicode) |
| ten_vai_tro | Required | 01 TC-121 (empty) |
| username | Unique, 4-50, regex `[a-z0-9_]` | 02 TC-150 (unique), TC-155 (regex), TC-156-159 (boundary 3/4/50/51) |
| email | Unique, RFC 5322 | 02 TC-151 (unique), TC-162 (format), TC-170 (cross is_deleted), 05 TC-130 (sanitize), TC-146 (XSS) |
| mat_khau | ≥ 8, 4 nhóm | 02 TC-152 (length), TC-153 (complexity), TC-154 (boundary 8 valid), TC-169 (= username), 05 TC-125-127 |
| ho_ten | Required | 02 TC-182 (XSS) |
| vai_tro_ids | Required ≥ 1 | 02 TC-163 (empty), TC-161 (invalid id) |
| don_vi_id | FK → DON_VI | 02 TC-164 (empty), TC-160 (invalid id) |
| loai_tai_khoan | FK → DM | 02 TC-165 (empty) |
| cccd | Optional, 12 digits | 02 TC-166 (11), TC-167 (12), TC-168 (empty) |
| token_reset_mk | System-gen random | 05 TC-129 (random fake), TC-145 (cross-account) |
| token_het_han | 30 phút HOAT_DONG / vĩnh viễn CHO_KICH_HOAT | 05 TC-123 (expired), TC-140 (vĩnh viễn), TC-141 (boundary 30 phút) |
| **UC120 ten_doanh_nghiep** | Required, default max 255 (SPEC-CLARIFY-TKPQ-38) | 12 TC-REG-110 (empty), TC-REG-111 (255), TC-REG-112 (256 over), TC-REG-113 (XSS), TC-REG-200 (Unicode), TC-REG-208 (duplicate name OK) |
| **UC120 ma_so_thue** | Required, Unique HT, format TCT 10/13 (SPEC-CLARIFY-TKPQ-31) | 12 TC-REG-114 (empty), TC-REG-115 (9), TC-REG-116 (10), TC-REG-117 (13), TC-REG-118 (14 over), TC-REG-119 (chữ), TC-REG-180 (trùng), TC-REG-202 (leading zero), TC-REG-206 (soft-delete edge) |
| **UC120 dia_chi** | Required | 12 TC-REG-120 |
| **UC120 tinh_thanh_id** | Required FK DON_VI | 12 TC-REG-121 (empty), TC-REG-122 (load tree) |
| **UC120 loai_doanh_nghiep_id** | Required FK DANH_MUC UC105 | 12 TC-REG-123 (empty), TC-REG-124 (load DM) |
| **UC120 quy_mo** | Required enum 3 | 12 TC-REG-125 (enum verify), TC-REG-126 (empty) |
| **UC120 nganh_nghe** | Required enum 3 | 12 TC-REG-127 (enum), TC-REG-128 (empty) |
| **UC120 so_lao_dong/doanh_thu_nam/tong_nguon_von** | Optional, ≥ 0 | 12 TC-REG-129..133 |
| **UC120 nguoi_dai_dien** | Required | 12 TC-REG-134 |
| **UC120 email (form đăng ký)** | Required, RFC 5322, Unique HT | 12 TC-REG-135 (empty), TC-REG-136 (format), TC-REG-137 (254 boundary), TC-REG-181 (trùng), TC-REG-211 (IDN edge) |
| **UC120 so_dien_thoai** | Required | 12 TC-REG-138 (empty), TC-REG-139 (format VN), TC-REG-203 (intl) |
| **UC120 file_dinh_kem** | Optional, multi | 12 TC-REG-140 (empty OK), TC-REG-141 (single), TC-REG-142 (multi), TC-REG-143 (size/ext), TC-REG-204 (dup name), TC-REG-205 (MIME spoof), TC-REG-212 (cancel cleanup) |
| **UC120 username (form đăng ký)** | Required, 4-50, regex `[a-z0-9_]`, Unique HT | 12 TC-REG-150 (empty), TC-REG-151 (4), TC-REG-152 (3), TC-REG-153 (50), TC-REG-154 (51), TC-REG-155 (regex), TC-REG-182 (trùng) |
| **UC120 mat_khau (form đăng ký)** | Required, ≥ 8, 4 nhóm | 12 TC-REG-156 (empty), TC-REG-157 (7), TC-REG-158 (8 valid), TC-REG-159..162 (thiếu nhóm), TC-REG-163 (indicator), TC-REG-183 (gộp), TC-REG-210 (autofill) |
| **UC120 mat_khau_xac_nhan** | Required, match | 12 TC-REG-164 (match), TC-REG-165 (mismatch), TC-REG-184 (ERR-REG-05) |
| **UC120 dong_y_dieu_khoan** | Required (checkbox) | 12 TC-REG-166 (unchecked), TC-REG-167 (tick enable), TC-REG-185 (ERR-REG-06) |

**Field Coverage: 100%** trong scope CRUD + edge + UC120 22 fields.

---

## 7. Output Format Coverage

| UC | Output | TC verify |
|----|--------|-----------|
| UC112 | so_tai_khoan derive | 01 TC-137 |
| UC112 | so_quyen derive | 01 TC-108 |
| UC113 | trang_thai badge 5 màu | 02 TC-102 |
| UC113 | tab counter 5 trạng thái | 02 TC-101, TC-108 |
| UC113 | ten_vai_tro multi-tag | 02 TC-117 |
| UC113 | ngay_tao + lan_dang_nhap_cuoi | 02 TC-194 |
| UC114 | tag-list đơn vị | 03 TC-103, TC-106 |
| UC115 | matrix 6 cột | 04 TC-101 |
| FR-VIII-26 | Mail link format | 05 TC-149 |
| **UC120 SCR-VIII-08** | Form 22 trường (18 DN + 4 TK) hiển thị đủ | 12 TC-REG-101 |
| **UC120 mail kích hoạt** | Mail SMTP gửi đến email DN khai (vĩnh viễn 1 lần dùng) | 12 TC-REG-102, TC-REG-104 |
| **UC120 AUDIT_LOG action** | `SELF_REGISTER_DN` + `ACCOUNT_ACTIVATE` | 12 TC-REG-190, TC-REG-103 |

---

## 8. Gap Forward → A6

A5 phát hiện các gap sau, forward sang A6 để FILL TC inline:

| Gap ID | Mô tả | A6 fill TC |
|--------|-------|-----------|
| A5-GAP-01 | UC112 search box (SCR không liệt kê) — nếu UI có thì test | A6 → 01 TC-110 |
| A5-GAP-02 | UC112 cap field (ERD có, form input không) — verify behavior | A6 → 01 TC-138 |
| A5-GAP-03 | UC113 click username → chi tiết (SCR-VIII-03 #10) | A6 → 02 TC-110 |
| A5-GAP-04 | UC113 SM-T2 backward compat verify (FR-VIII-22 v3.1 đã chuyển sang T4) | A6 → 02 TC-131 |
| A5-GAP-05 | UC113 SM-T5 button manual activate (UI có không?) | A6 → 02 TC-135 |
| A5-GAP-06 | UC113 lan_dang_nhap_cuoi update sau login | A6 → 02 TC-194 |
| A5-GAP-07 | UC113 button [Xóa] vs [Vô hiệu hóa] (SCR không tường minh) | A6 → 02 TC-195 |
| A5-GAP-08 | UC112 cột "Số tài khoản" derive realtime | A6 → 02 TC-196 |
| A5-GAP-09 | UC114 vai trò mới chưa quyền — cây render rỗng | A6 → 03 TC-137 |
| A5-GAP-10 | UC114 đơn vị TAM_DUNG có hiện trong cây? | A6 → 03 TC-138 |
| A5-GAP-11 | UC115 cây menu count (SRS không liệt kê hết) | A6 → 04 TC-108 |
| A5-GAP-12 | FR-VIII-26 mail link format verify | A6 → 05 TC-149 |
| A5-GAP-13 | FR-VIII-26 token cleanup cron | A6 → 05 TC-150 |
| **A5-GAP-14 (UC120)** | UC120 SCR-VIII-08 form layout — verify tab order + label vị trí Group 1/Group 2 | A6 → 12 TC-REG-101 fill detail |
| **A5-GAP-15 (UC120)** | UC120 mail link format kích hoạt — endpoint cụ thể `/reset-password?token=...&type=activate` hay đường dẫn khác | A6 → 12 TC-REG-102 verify mail HTML |
| **A5-GAP-16 (UC120)** | UC120 trigger mail SMTP — kiểm verify endpoint MailHog API | A6 → 12 TC-REG-102 step "Mở MailHog" |
| **A5-GAP-17 (UC120)** | UC120 file_dinh_kem storage path — verify file thực tế lưu (sample) | A6 → 12 TC-REG-141 fill verify network response |

**Tất cả A5-GAP đã được fill ở A6 → merged inline vào file UC.**

---

## 9. Quality metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| BR coverage | 100% (15/15 sau UC120 add BR-DATA-02 unique) | ≥95% | ✅ |
| AC coverage | 100% (20/20 — tăng từ 16 sau UC120 +4 AC) | 100% | ✅ |
| Error code coverage | 100% (25/25 — tăng từ 19 sau UC120 +6 ERR-REG) | 100% | ✅ |
| SM-TAIKHOAN transitions | 100% (12/12 — UC120 add T1 + T4 paths) | 100% | ✅ |
| Permission combo | 100% (5 UC × 4 nhóm role + IDOR + UC120 public no-auth) | 100% | ✅ |
| Field validation BVA | 100% in-scope (UC112-117 fields + UC120 22 fields) | ≥95% | ✅ |
| Output format | 100% (UC120 SCR-VIII-08 form + mail + AUDIT_LOG) | — | ✅ |
| TC chỉ-DB/API thuần | 0 (đã filter A7 cho UC112-117; UC120 sẽ filter A7 ngay sau A6) | 0 | ⏳ A7 UC120 pending |

**Phase A acceptance (UC112-117 đã PASS từ 2026-05-08; UC120 ⏳ chờ A6+A7):** ✅ trace done

---

## 10. SPEC-CLARIFY tổng hợp (29 entries → forward Phase B / BA)

| ID | Module | Mô tả ngắn | TC ref |
|----|--------|-----------|--------|
| TKPQ-01 | UC112 | VAI_TRO field `cap` ẩn vs hiện trên form | 01 TC-138 |
| TKPQ-02 | UC113 | DM `LOAI_TAI_KHOAN` enum | (Phase B verify) |
| TKPQ-03 | UC113 | UI phê duyệt CHO_PHAN_QUYEN — modal SCR-VIII-08a vs riêng | 02 TC-132 |
| TKPQ-04 | UC113 | SM-T2 v3.1 có còn áp dụng không (vai_tro luôn gán sẵn?) | 02 TC-131 + 05 TC-105 |
| TKPQ-05 | UC114 | Vai trò "thuộc đơn vị" suy thế nào (VAI_TRO không có don_vi_id) | 03 TC-120-122 |
| TKPQ-06 | UC115 | Reset về mặc định template gì? | 04 TC-106 |
| TKPQ-07 | UC113 | Button "Đổi MK" trực tiếp vs FR-VIII-26 only | 02 TC-118 |
| TKPQ-08 | FR-VIII-26 | Rate limit gửi mail | 05 TC-144 |
| TKPQ-09 | UC113 + FR-VIII-26 | T12 (7 ngày auto disable) vs token vĩnh viễn conflict | 02 TC-142 + 05 TC-140 |
| TKPQ-10 | UC115 | Cây menu count exact | 04 TC-108 |
| TKPQ-11 | FR-VIII-26 | Trigger SM-TVV side-effect cross srs-fr-04 | 05 TC-142 |
| TKPQ-12 | UC112 | Search box (không tường minh trong SCR) | 01 TC-110 |
| TKPQ-13 | UC112 | Mã max length | 01 TC-124 |
| TKPQ-14 | UC112 | Mã unique case-sensitive vs insensitive | 01 TC-127 |
| TKPQ-15 | UC112 + UC113 | Unique cross is_deleted | 01 TC-128 + 02 TC-170 |
| TKPQ-16 | UC112 | Mã unicode accept hay reject | 01 TC-135 |
| TKPQ-17 | UC113 | Button "Kích hoạt" manual SM-T5 | 02 TC-135 |
| TKPQ-18 | UC113 | MK = username | 02 TC-169 |
| TKPQ-19 | UC113 | Button [Xóa] vs [Vô hiệu hóa] | 02 TC-195 |
| TKPQ-20 | UC114 | Bỏ trống don_vi_ids | 03 TC-127 |
| TKPQ-21 | UC114 + UC115 | Cache refresh strategy | 03 TC-131 + 04 TC-131 |
| TKPQ-22 | UC114 | Vai trò cap=ALL có chịu BR-AUTH-03 không | 03 TC-133 |
| TKPQ-23 | UC114 | entity_type filter UI | 03 TC-135 |
| TKPQ-24 | UC114 | Đơn vị TAM_DUNG có hiện cây không | 03 TC-138 |
| TKPQ-25 | UC115 | Vai trò KHÔNG có quyền nào — accept? | 04 TC-122 |
| TKPQ-26 | UC115 | Inconsistent cha tick + con không tick | 04 TC-123 |
| TKPQ-27 | FR-VIII-26 | Boundary 30 phút token | 05 TC-141 |
| TKPQ-28 | FR-VIII-26 | Session cũ khi user đổi MK qua reset | 05 TC-147 |
| TKPQ-29 | FR-VIII-26 | Token cleanup cron | 05 TC-150 |
| **TKPQ-30** | UC120 | T2 vs T4 SM-TAIKHOAN mismatch (FR-VIII-22 step 7 vs SM bảng line 2109) — DN có vai_tro gán sẵn → T4 path; SM bảng vẫn ghi T2 | 12 TC-REG-196 + 102 + 195 |
| **TKPQ-31** | UC120 | MST format chuẩn TCT 10/13 chữ số — SRS chỉ ghi "Unique" không nêu format | 12 TC-REG-115/116/117/118/119 |
| **TKPQ-32** | UC120 | URL public form đăng ký — pattern path cụ thể + CSRF | 12 TC-REG-192 |
| **TKPQ-33** | UC120 | File đính kèm — max size + extension + AV scan | 12 TC-REG-143 + 205 (MIME spoof) |
| **TKPQ-34** | UC120 | Token mail kích hoạt vĩnh viễn vs SM-T12 7 ngày auto disable conflict | 12 TC-REG-104 (cross TKPQ-09 cũ) |
| **TKPQ-35** | UC120 | BR-DATA-02 ref sai context (line 1054 dùng cho unique nhưng BR-DATA-02 nguyên văn về multi-tenant) | (note SRS) |
| **TKPQ-36** | UC120 | Cancel button "Hủy" — confirm dialog khi form đã có dữ liệu? | 12 TC-REG-105 |
| **TKPQ-37** | UC120 | Login với TK chưa kích hoạt — error message cụ thể (KHÔNG nằm trong ERR-REG) | 12 TC-REG-106 |
| **TKPQ-38** | UC120 | Field length max — SRS không cap explicit; default DB varchar 255? Email RFC 5322 max 254? | 12 TC-REG-111/112/137 |
| **TKPQ-39** | UC120 | so_dien_thoai regex VN vs international `+84` | 12 TC-REG-139, 203 |
| **TKPQ-40** | UC120 | Password strength indicator implementation (real-time + autofill react) | 12 TC-REG-163, 210 |
| **TKPQ-41** | UC120 | CB nội bộ truy cập SCR-VIII-08 (public route) — block / cảnh báo / cho phép tạo TK DN? | 12 TC-REG-193, 194 |
| **TKPQ-42** | UC120 (A4) | Re-register với MST đã soft-delete / email VHH — unique check filter is_deleted? | 12 TC-REG-206, 207 |
| **TKPQ-43** | UC120 (A4) | Email IDN (Unicode local-part / domain) — SRS RFC 5322 không hỗ trợ IDN, RFC 6531 mới có | 12 TC-REG-211 |
