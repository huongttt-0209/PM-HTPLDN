# TC Permission Matrix — Cross BR-AUTH-01/05/08 + BR-FLOW-04 + BR-NOTIF-01

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §6 BR (line 1173-1244) + Permission Matrix [`00-test-plan-overview.md`](./00-test-plan-overview.md) §2.4
> **Scope:** Cross-cutting verification BR-AUTH-01 (xác thực) / BR-AUTH-05 (cùng cấp) / BR-AUTH-08 (scope đơn vị) / BR-FLOW-04 (lý do từ chối) / BR-NOTIF-01 (TB phê duyệt)
> **Total TC:** 8

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PERM-001 | TVV không truy cập SCR-VI-01 | Login `tvv_01`. | 1. Truy cập `/danh-gia/ke-hoach/danh-sach` | 403 hoặc redirect home + sidebar không hiển thị "Đánh giá hiệu quả" | High | BR-AUTH-01, Permission Matrix |
| TC-DG-PERM-002 | DN không truy cập SCR-VI-01 | Login `dn_01`. | 1. Truy cập URL danh sách đợt | 403 hoặc redirect cổng PLQG | High | BR-AUTH-01 |
| TC-DG-PERM-003 | qtht_01 read-only — không CRUD đợt | Login `qtht_01`. | 1. Truy cập danh sách đợt<br>2. Tìm nút [+ Tạo đợt] | Danh sách hiển thị (read). Nút [+ Tạo đợt] ẩn. Icon Sửa/Xóa ẩn | Medium | Permission Matrix qtht=R |
| TC-DG-PERM-004 | BR-AUTH-08 — cb_nv_dp_01 (AG) không thấy đợt scope BKH | Login `cb_nv_dp_01` (AG). Đợt scope BKH tồn tại. | 1. Mở danh sách đợt | Bảng KHÔNG hiển thị đợt BKH. Force URL chi tiết → 403 | Critical | BR-AUTH-08 |
| TC-DG-PERM-005 | BR-AUTH-05 cross-cấp — cb_pd_dp_01 không duyệt PC đợt TW (P0 F-003) | Login `cb_pd_dp_01`. Đợt CHO_DUYET_PC scope TW (force URL biết được). | 1. Truy cập chi tiết đợt URL trực tiếp | 403 hoặc nút [Phê duyệt PC] ẩn. Force trigger → toast NGUYÊN VĂN "Bạn không có quyền thực hiện thao tác này" (ERR-AUTH-01) | Critical | BR-AUTH-05 cross-cấp, ERR-AUTH-01 |
| TC-DG-PERM-006 | BR-AUTH-05 cùng cấp BN — cb_pd_bn_01 (BKH) không duyệt đợt BN BTC | Login `cb_pd_bn_01` (BKH). Đợt CHO_DUYET_PC scope BN BTC. | 1. Truy cập danh sách | Đợt BN BTC KHÔNG hiển thị. Force URL → 403 | High | BR-AUTH-05 + BR-AUTH-08 |
| TC-DG-PERM-007 | BR-NOTIF-01 — Trình PC fire 1 lần TB CB PD | Login. Đợt PHAN_CONG → CHO_DUYET_PC. | 1. cb_nv: [Trình duyệt PC]<br>2. Login `cb_pd_tw_01`<br>3. Mở /thong-bao | Inbox CB PD có 1 TB "Có đợt phân công chờ duyệt: DG-..." | Medium | BR-NOTIF-01 |
| TC-DG-PERM-008 | BR-NOTIF-01 — Duyệt + Từ chối BC fire TB CB NV | Login. Đợt CHO_PHE_DUYET. | 1. cb_pd: Duyệt → HOAN_THANH<br>2. Login cb_nv<br>3. Mở /thong-bao | TB "Đợt ĐG đã được duyệt: DG-..." xuất hiện 1 lần | Medium | BR-NOTIF-01 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PERM-009 | Session hết hạn khi đang chấm điểm | Login. Đang ở Tab 3 chấm. | 1. Force expire token<br>2. Click [Lưu] | Redirect login. Sau login → giữ data unsaved hoặc lost (per app policy) | Medium | BR-AUTH-01 session timeout |
| TC-DG-PERM-010 | CSRF token verify trên action Phê duyệt | Login `cb_pd_tw_01`. | 1. Inspect request POST `/danh-gia/duyet`<br>2. Verify header CSRF | Header X-CSRF-Token có. Bỏ token → 403 | Low | Security baseline |
| TC-DG-PERM-011 | IDOR — cb_nv_dp_01 force URL chi tiết đợt TW qua ID | Login `cb_nv_dp_01`. Đợt id=DG-X scope TW. | 1. GET `/danh-gia/ke-hoach/DG-X` | 403 hoặc 404. KHÔNG leak data | Critical | BR-AUTH-08 IDOR |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PERM-012 | Deny cell — CB_PD không tạo đợt được (P1 F-006) | Login `cb_pd_tw_01`. | 1. Truy cập danh sách đợt<br>2. Tìm nút [+ Tạo đợt đánh giá] | Nút [+ Tạo đợt] ẩn (Permission Matrix R only). Force POST `/api/danh-gia/ke-hoach` → 403 ERR-AUTH-01 | High | Permission Matrix CB_PD R only, BR-AUTH-01 |
| TC-DG-PERM-013 | Deny cell — qtht_01 không sửa tiêu chí được (P1 F-006) | Login `qtht_01`. | 1. Mở chi tiết đợt LAP_KE_HOACH<br>2. Tab Tiêu chí | Inline edit disabled. Nút [+ Thêm tiêu chí] / [Xóa] ẩn. Force PUT API → 403 | Medium | Permission Matrix qtht=R |
| TC-DG-PERM-014 | Deny cell — TVV force URL action Phê duyệt → 403 (P1 F-006) | Login `tvv_01`. Đợt CHO_DUYET_PC. | 1. Force POST `/api/danh-gia/duyet-pc` body valid | 403 + ERR-AUTH-01 NGUYÊN VĂN "Bạn không có quyền thực hiện thao tác này". KHÔNG side-effect DB | Critical | BR-AUTH-01, BR-AUTH-08 IDOR |
| TC-DG-PERM-015 | Deny cell — CG/NHT không phân công không xem được Tab Thực hiện (P1 F-006) | Login `cg_05` (KHÔNG được phân công đợt X). | 1. Force GET `/api/danh-gia/ke-hoach/{X}/cham-diem` | 403 hoặc empty payload. Nếu UI list ẩn đợt X | High | BR-AUTH-08 + UC88 step 2 |
| TC-DG-PERM-016 | BR-DATA-05 audit immutability + entity coverage (P1 F-008) | Login `qtht_01` (có quyền /quan-tri/audit-log). 1 đợt đã đi qua đầy đủ flow LAP_KE_HOACH → HOAN_THANH. | 1. Mở /quan-tri/audit-log<br>2. Filter theo entity KE_HOACH_DANH_GIA, TIEU_CHI_DANH_GIA per-đợt, PHAN_CONG, KET_QUA, BAO_CAO<br>3. Verify INSERT-only — không có UPDATE/DELETE row trong audit log<br>4. Verify mỗi action CUD + Approval có record audit | 5 entities có audit record. Audit table KHÔNG có UPDATE/DELETE row (immutable). Coverage tracker: CREATE/UPDATE/DELETE/APPROVE/REJECT đều có entry | Medium | BR-DATA-05, BR-DATA-03 |

## Tổng số TC: 16 (8 base + 3 edge A4 + 5 Codex apply)

> **A4 done 2026-05-10** — 3 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
