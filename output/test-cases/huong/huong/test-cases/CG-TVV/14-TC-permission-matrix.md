# Test Cases — Permission Matrix (Cross-FR-IV BR-AUTH-01/05/08 + IDOR)

> **SRS Ref**: BR-AUTH-01 (xác thực bắt buộc + TOTP 2FA), BR-AUTH-05 (cùng cấp), BR-AUTH-08 (đơn vị 2-tầng), BR-LEGAL-09 (toàn quốc khi cong_khai), Permission matrix Section B của 00-test-plan-overview.md
> **Nguồn**: NotebookLM `4dd0675e-a4fa-4ea6-80ae-48e76b3fa264` + LOCAL `srs-fr-04-chuyen-gia-tvv- v3.1.md:2471-2519`
> **Ngày tạo**: 2026-05-09

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-UI-01 | BR-AUTH-01 + Sidebar visibility per role | Verify sidebar menu visibility per role | 8 role test | — | 1. Login 8 role tuần tự<br>2. Verify sidebar | **qtht_01**: Cả 3 sub-menu (TVV/CG, Tổ chức TV, NHT)<br>**cb_nv_tw_01/bn_01/dp_01**: Cả 3 sub-menu (CRUD theo đơn vị)<br>**cb_pd_tw_01/bn_01/dp_01**: TVV/CG (Phê duyệt) + Tổ chức TV (Phê duyệt) + KHÔNG có NHT (chỉ CB NV/QTHT)<br>**nht_01**: TVV/CG (chỉ Đăng ký FR-IV-03) + KHÔNG có Tổ chức TV + NHT<br>**tvv_01/cg_01**: KHÔNG có sidebar CMS — chỉ chuyên trang xem hồ sơ của mình | Happy 🔴 |

## B. BR-AUTH-08 — Phân quyền dữ liệu theo đơn vị (cây 2 tầng)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-001 | BR-AUTH-08 / TW ngoại lệ | TW xem được toàn bộ data | cb_nv_tw_01, mixed data TW/BN/HN/HP | — | 1. Login cb_nv_tw_01<br>2. Mở SCR-IV-01 + SCR-IV-NEW-01 + SCR-IV-NHT-01 | TW thấy toàn bộ TVV + TC TV + NHT cả 3 cấp; READ ngoại lệ TW (BR-AUTH-08); CRUD chỉ trên data TW (theo phân quyền tạo) | Happy 🔴 |
| TC-PERM-002 | BR-AUTH-08 / BN ngang cấp HN | cb_nv_bn_01 (Bộ TP) KHÔNG xem được data HN | cb_nv_bn_01, TVV thuộc HN | — | 1. Login cb_nv_bn_01<br>2. Filter cố tìm TVV HN | Network response chỉ data BN; tampered URL → 403 | Negative 🔴 |
| TC-PERM-003 | BR-AUTH-08 / ĐP ngang cấp | cb_nv_dp_HN_01 KHÔNG xem được data HP (cùng cấp khác đơn vị) | cb_nv_dp_HN_01, TVV-HP-001 | — | 1. Direct URL `/chuyen-gia-tvv/chi-tiet/TVV-HP-001` | API 403; UI redirect hoặc empty | Negative 🔴 |
| TC-PERM-004 | BR-AUTH-08 / IDOR cross-tenant | IDOR: cb_nv_dp_HN_01 cố sửa TVV-HP-001 qua DevTools | cb_nv_dp_HN_01 | — | 1. DevTools call PUT `/api/v1/tu-van-vien/{TVV-HP-001-id}` body | API 403; AUDIT_LOG ghi attempt; KHÔNG cập nhật | Negative 🔴 |
| TC-PERM-005 | BR-AUTH-08 / NHT scope | nht_01 chỉ tạo TVV cùng đơn vị NHT.don_vi_id | nht_01 (HN) | DevTools tamper don_vi_id=HP | 1. Submit form đăng ký với tampered don_vi_id | Backend ghi đè don_vi_id = nht_01.don_vi_id (HN); ignore client value | Negative 🔴 |

## C. BR-AUTH-05 — Phê duyệt cùng cấp

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-101 | BR-AUTH-05 / TVV cùng cấp pass | cb_pd_tw_01 duyệt TVV cb_nv_tw_01 thẩm định | cb_pd_tw_01, TVV-TW-CHO_PHE_DUYET | — | 1. Phê duyệt | PASS — chuyển CHO_KICH_HOAT | Happy 🔴 |
| TC-PERM-102 | BR-AUTH-05 / TVV khác cấp reject | cb_pd_tw_01 duyệt TVV-DP (do cb_nv_dp_01 thẩm định) | cb_pd_tw_01, TVV-DP-CHO_PHE_DUYET | — | 1. Cố Phê duyệt | API 403 ERR-PD-02 (NGUYÊN VĂN); UI ẩn nút | Negative 🔴 |
| TC-PERM-103 | BR-AUTH-05 / TC TV cùng cấp | cb_pd_dp_HN_01 duyệt TC TV-HN cb_nv_dp_HN_01 tạo | cb_pd_dp_HN_01, TC-HN-CHO_PHE_DUYET | — | 1. Phê duyệt | PASS — chuyển HOAT_DONG | Happy 🟡 |
| TC-PERM-104 | BR-AUTH-05 / NĐ 121/2025 phân cấp | cb_pd_bn_01 (Bộ TP) duyệt TC TV-BN (Bộ TP công bố mạng lưới ngành) | cb_pd_bn_01, TC-BN-CHO_PHE_DUYET | — | 1. Phê duyệt | PASS theo NĐ 55/2019 Đ.9 (mỗi bộ tự công bố) | Happy 🟡 |

## D. BR-AUTH-01 — Xác thực + TOTP 2FA

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-201 | BR-AUTH-01 / Unauthorized | Truy cập SCR-IV-01 không login → redirect login | — | URL `/chuyen-gia-tvv/danh-sach` | 1. Direct URL không session | Redirect `/login`; URL gốc lưu để callback sau login | Negative 🔴 |
| TC-PERM-202 | BR-AUTH-01 / TOTP 2FA | Login Tier 1 + OTP qua email (mặc định 666666 trong môi trường test) | qtht_01 | OTP: 666666 | 1. Submit username/password<br>2. OTP screen<br>3. Nhập 666666 | Login PASS; redirect home | Happy 🟡 |

## E. BR-LEGAL-09 — Cổng PLQG toàn quốc

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-301 | BR-LEGAL-09 / Toàn quốc | TVV cong_khai=1 thuộc HN hiển thị toàn quốc qua Cổng PLQG public | tvv_HN_001 cong_khai=1, dn_001 ở HP | — | 1. Mở Cổng PLQG public<br>2. Tra cứu TVV LV Lao động | TVV HN xuất hiện trong kết quả tra cứu DN HP (cong_khai=1 toàn quốc); CMS thì BR-AUTH-08 vẫn ẩn cho HP user | Happy 🔴 |

## F. TVV/CG self-view

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-401 | BR-AUTH-08 / TVV self-only | tvv_01 chỉ xem được hồ sơ của mình | tvv_01, hồ sơ TVV-TW-001 | — | 1. Login chuyên trang<br>2. Profile<br>3. Cố URL hồ sơ TVV khác | Tự xem PASS readonly; URL TVV khác → 403 | Negative 🔴 |

---

## G. EDGE bổ sung (A4 inline merge — 3 edge)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-501 | EDGE-A4-aa / IDOR direct API | IDOR trực tiếp API KHÔNG qua UI: PUT /tu-van-vien/{cross-tenant-id} | cb_nv_dp_HN_01 | DevTools PUT cross-tenant TVV-HP-001 | 1. Capture token<br>2. PUT trực tiếp body | API 403 ERR-AUTH-08 (NGUYÊN VĂN); AUDIT_LOG ghi attempt với IP + user_id; KHÔNG cập nhật | Edge 🔴 |
| TC-PERM-502 | EDGE-A4-s / Session expired giữa update | Session expire khi đang submit form Create TVV | nht_01, session timeout 30 phút | — | 1. Mở form<br>2. Đợi 31 phút<br>3. Submit | API 401 "Phiên đăng nhập hết hạn"; UI redirect login + lưu draft data (sessionStorage); sau login lại → restore form data; SPEC-CLARIFY-CGTVV-21 nếu SRS không có draft restore | Edge 🟡 |
| TC-PERM-503 | EDGE-A4-t / Real-time permission change | Admin thay đổi vai trò user đang login → next request 403 | qtht_01 + cb_nv_tw_01 đang login | qtht_01 revoke quyền "Quản lý TVV" của cb_nv_tw_01 | 1. cb_nv_tw_01 mở SCR-IV-01 (PASS)<br>2. qtht_01 revoke quyền<br>3. cb_nv_tw_01 click "+ Thêm" | Submit fail 403 "Bạn không có quyền thực hiện thao tác này"; UI có thể hiển thị banner "Quyền của bạn vừa thay đổi, vui lòng tải lại trang"; SPEC-CLARIFY-CGTVV-22 nếu SRS không define real-time permission sync | Edge 🟡 |

---

## H. A6 fill gap (Traceability matrix forward — 1 TC)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|---------------|----------------|-----------|--------------------|-------------------|------|
| TC-PERM-601 | A6-FILL / BR-DATA-05 AUDIT_LOG immutable | Verify AUDIT_LOG INSERT-only qua FR-VIII-28 UI list audit | qtht_01 (admin) | — | 1. Tạo TVV (1 INSERT AUDIT_LOG)<br>2. **Mở FR-VIII-28 list audit** filter theo entity TU_VAN_VIEN<br>3. Verify entry visible nhưng **KHÔNG có nút Sửa/Xóa** trên row | UI FR-VIII-28: row AUDIT_LOG read-only, KHÔNG có action Sửa/Xóa; nếu DevTools tamper PUT → API 405; **A7 SỬA**: verify qua UI bridge FR-VIII-28 (W1.1 đã ✅), KHÔNG cần admin DB view; SPEC-CLARIFY-CGTVV-25 confirmed UI bridge OK | Edge 🔴 |

---

**Tổng số TC**: 17 (1 UI + 5 BR-AUTH-08 + 4 BR-AUTH-05 + 2 BR-AUTH-01 + 1 BR-LEGAL-09 + 1 TVV self + 3 Edge A4 + 1 A6 fill)
