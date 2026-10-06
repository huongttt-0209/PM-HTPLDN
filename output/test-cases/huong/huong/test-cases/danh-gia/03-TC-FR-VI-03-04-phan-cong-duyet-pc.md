# TC FR-VI-03 + FR-VI-04 — Phân công người ĐG (UC85) + Phê duyệt phân công (UC86) — Tab 2

> **SRS:** [`srs-fr-08-danh-gia.-v3.1.md`](../../../input/srs-v3/srs-fr-08-danh-gia.-v3.1.md) §FR-VI-03 (line 231-302) + §FR-VI-04 (line 305-371) + §3 Tab 2 (line 843-852)
> **SCR:** SCR-VI-01 — Tab 2 Phân công
> **Actor:** CB NV (CRUD phân công + trình) / CB PD (duyệt PC + từ chối PC)
> **Entity:** PHAN_CONG_DANH_GIA (per đợt)
> **BR core:** BR-AUTH-05 (cùng cấp) + BR-FLOW-04 (lý do từ chối ≥10) + BR-NOTIF-01
> **SM transitions:** PHAN_CONG → CHO_DUYET_PC, CHO_DUYET_PC → THUC_HIEN, CHO_DUYET_PC → PHAN_CONG
> **Total TC:** 14

---

## Test Cases

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PC-001 | Mở Tab Phân công — bảng inline editable | Login `cb_nv_tw_01`. Đợt LAP_KE_HOACH có tiêu chí 100%. | 1. Mở chi tiết đợt<br>2. Tab "Phân công" | Tab hiển thị bảng cột: Người ĐG / Vai trò / Lĩnh vực phụ trách / Ghi chú / Hành động + info card đợt | High | SCR row #35-36 |
| TC-DG-PC-002 | Thêm người đánh giá — happy path | Login. cg_01 cùng đơn vị. | 1. Click [+ Thêm người đánh giá]<br>2. Chọn `cg_01`, vai_tro=`DANH_GIA_VIEN`, linh_vuc=DM-LV-01<br>3. Lưu | Row mới. Trạng thái đợt: LAP_KE_HOACH → PHAN_CONG (auto khi thêm phân công đầu tiên) | Critical | UC85 happy, SM-DANHGIA #2 |
| TC-DG-PC-003 | Cần ≥1 TRUONG_NHOM — block khi thiếu | Login. Phân công 2 người vai_tro=DANH_GIA_VIEN cả 2. | 1. Click [Trình phê duyệt] | Block + toast "Cần ít nhất 1 người vai trò Trưởng nhóm" (ERR-DG-PC-02). State giữ PHAN_CONG | Critical | ERR-DG-PC-02 |
| TC-DG-PC-004 | Phân công 0 người → ERR-DG-PC-01 | Login. Bảng phân công rỗng. | 1. Click [Trình phê duyệt] | Block + "Vui lòng phân công ít nhất 1 người" (ERR-DG-PC-01) | High | ERR-DG-PC-01 |
| TC-DG-PC-005 | Người trùng lặp → ERR-DG-PC-03 | Login. cg_01 đã có row. | 1. Thêm row mới chọn cg_01 lần 2 | Block "Người đánh giá đã được phân công" (ERR-DG-PC-03) | High | ERR-DG-PC-03 |
| TC-DG-PC-006 | Người ĐG khác đơn vị không xuất hiện trong dropdown | Login `cb_nv_tw_01`. cg_02 thuộc BN. | 1. Mở dropdown chọn người | Dropdown chỉ chứa CB/CG cùng đơn vị TW. cg_02 KHÔNG có | High | BR-AUTH-08, FR-VI-03 process step 4 |
| TC-DG-PC-007 | Trình duyệt PC — happy path | Login. ≥1 TRUONG_NHOM + tiêu chí 100% + state PHAN_CONG. | 1. Click [Trình phê duyệt] | Confirm modal → state PHAN_CONG → CHO_DUYET_PC. Toast success. BR-NOTIF-01 fire CB PD TW | Critical | SM-DANHGIA #3, BR-NOTIF-01 |
| TC-DG-PC-008 | CB PD duyệt PC — happy path | Login `cb_pd_tw_01`. Đợt CHO_DUYET_PC do cb_nv_tw_01 trình. | 1. Mở chi tiết đợt<br>2. Tab Phân công<br>3. Click [Phê duyệt PC]<br>4. Confirm | State CHO_DUYET_PC → THUC_HIEN. Auto-fill Common Approval Fields (người duyệt, thời gian). BR-NOTIF-01 fire CB NV. AUDIT_LOG có record | Critical | UC86 happy, SM-DANHGIA #4, BR-AUTH-05, BR-NOTIF-01 |
| TC-DG-PC-009 | CB PD từ chối PC — lý do bắt buộc ≥10 | Login `cb_pd_tw_01`. Đợt CHO_DUYET_PC. | 1. Click [Từ chối PC]<br>2. Nhập lý do "Sai" (4 ký tự)<br>3. Submit | Block + "Vui lòng nhập lý do từ chối (tối thiểu 10 ký tự)" (ERR-DG-PD-02) | High | ERR-DG-PD-02, BR-FLOW-04 |
| TC-DG-PC-010 | CB PD từ chối PC — happy path | Login `cb_pd_tw_01`. CHO_DUYET_PC. | 1. [Từ chối PC]<br>2. Nhập lý do "Phân công thiếu chuyên gia chuyên ngành A"<br>3. Submit | State CHO_DUYET_PC → PHAN_CONG. Lý do lưu. BR-NOTIF-01 fire CB NV. CB NV thấy lý do trên Tab 2 | Critical | UC86 reject, SM-DANHGIA #5, BR-FLOW-04, BR-NOTIF-01 |
| TC-DG-PC-011 | BR-AUTH-05 — CB PD BN không duyệt được đợt TW | Login `cb_pd_bn_01`. Đợt CHO_DUYET_PC scope TW. | 1. Truy cập URL chi tiết đợt | 403 hoặc danh sách filter ẩn đợt scope TW (BR-AUTH-08). Nếu force URL trigger Phê duyệt → toast NGUYÊN VĂN "Bạn không có quyền thực hiện thao tác này" (ERR-AUTH-01) | High | BR-AUTH-05, BR-AUTH-08, ERR-AUTH-01 |
| TC-DG-PC-012 | Duyệt PC khi state != CHO_DUYET_PC → ERR-DG-PD-01 | Login `cb_pd_tw_01`. Đợt LAP_KE_HOACH. | 1. Truy cập chi tiết<br>2. Tìm nút [Phê duyệt PC] | Nút Phê duyệt PC ẩn (per Tab 2 row #39 condition). Nếu trigger qua API → ERR-DG-PD-01 | Medium | ERR-DG-PD-01, SCR row #39 |
| TC-DG-PC-013 | Sửa phân công khi state CHO_DUYET_PC → block | Login `cb_nv_tw_01`. Đợt CHO_DUYET_PC. | 1. Click ô vai_tro inline edit | Inline edit disabled (read-only sau khi trình duyệt) | Medium | SM-DANHGIA flow |
| TC-DG-PC-014 | Cycle đầy đủ — Trình → Từ chối → Sửa → Trình lại → Duyệt | Login. | 1. cb_nv: Trình → CHO_DUYET_PC<br>2. cb_pd: Từ chối → PHAN_CONG<br>3. cb_nv: Sửa lại + Trình → CHO_DUYET_PC<br>4. cb_pd: Duyệt → THUC_HIEN | State chuỗi đúng. AUDIT_LOG có 4 entries (TRINH/TU_CHOI/TRINH/DUYET). BR-NOTIF-01 fire 4 lần | High | Cycle BR-AUTH-05 + BR-FLOW-04 |

---

## Edge bổ sung (A4 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PC-015 | Boundary lý do từ chối đúng 10 ký tự | Login `cb_pd_tw_01`. CHO_DUYET_PC. | 1. Lý do "1234567890" (10 chars)<br>2. Submit | Cho phép từ chối (boundary lower bound) | Medium | BR-FLOW-04 boundary |
| TC-DG-PC-016 | Boundary lý do 9 ký tự → block | Login. | 1. Lý do "123456789" (9 chars) | Block + ERR-DG-PD-02 | Medium | BR-FLOW-04 boundary |
| TC-DG-PC-017 | Lý do >= 1000 ký tự (long-text) | Login. | 1. Lý do 1500 chars | Cho phép (no upper bound trong spec) | Low | BR-FLOW-04 |
| TC-DG-PC-018 | Trình duyệt khi tiêu chí trọng số != 100% → block | Login. Phân công đầy đủ nhưng tiêu chí 90%. | 1. Click [Trình phê duyệt PC] | Block + ERR-DG-TC-01 (cross-tab guard từ Tab 1 sang Tab 2) | High | ERR-DG-TC-01 cross-tab |
| TC-DG-PC-019 | Trùng vai trò TRUONG_NHOM cho 2 người — cho phép | Login. | 1. Phân công cg_01 + cg_02 cùng vai_tro=TRUONG_NHOM | Lưu OK (spec yêu cầu ≥1 TRUONG_NHOM, KHÔNG cap upper) | Medium | UC85 |
| TC-DG-PC-020 | Người ĐG là chính `cb_nv_tw_01` (self-assign) — cho phép | Login `cb_nv_tw_01`. | 1. Phân công chính `cb_nv_tw_01` vai_tro=TRUONG_NHOM | Lưu OK (spec không cấm) | Low | SPEC-CLARIFY-DG-02 (BA xác nhận có cho self-assign?) |

## Fill GAP A5 (A6 — merge 2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PC-021 | Hủy đợt từ PHAN_CONG → HUY (GAP-A5-01) | Login `cb_nv_tw_01`. Đợt PHAN_CONG có 2 phân công. | 1. Mở chi tiết<br>2. Click [Hủy đợt]<br>3. Lý do "Hủy do thay đổi nhân sự"<br>4. Confirm | State PHAN_CONG → HUY. Audit log + lý do lưu | High | SM-DANHGIA #11 |
| TC-DG-PC-022 | Thêm phân công khi đợt CHO_DUYET_PC → ERR-DG-PC-04 (GAP-A5-04) | Login `cb_nv_tw_01`. Đợt CHO_DUYET_PC. | 1. Click [+ Thêm người ĐG] | Block "Đợt không ở trạng thái phù hợp để phân công" (ERR-DG-PC-04). Nút [+ Thêm] disabled | High | ERR-DG-PC-04 |
| TC-DG-PC-023 | DELETE row phân công (chưa trình duyệt) (GAP-A5-09) | Login. State PHAN_CONG, ≥2 row PC. | 1. Click icon Xóa row<br>2. Confirm | Row biến mất. AUDIT_LOG có DELETE. Số người PC giảm 1 | Medium | UC85 CRUD |

## Codex Review apply (2026-05-10)

| TC ID | Mô tả | Pre-condition | Steps | Expected | Priority | BR/AC/ERR |
|-------|-------|---------------|-------|----------|----------|-----------|
| TC-DG-PC-024 | TB người được phân công khi save (P1 F-005) | Login `cb_nv_tw_01`. | 1. Phân công cg_01 vai_tro=DANH_GIA_VIEN<br>2. Save<br>3. Login `cg_01`<br>4. Mở /thong-bao | cg_01 inbox có TB "Bạn được phân công đánh giá đợt: DG-..." per FR-VI-03 process step 6 + Outputs #2 | High | FR-VI-03 process step 6, Outputs #2 |
| TC-DG-PC-025 | Boundary `ghi_chu` phân công 500 chars (P1 F-011) | Login. | 1. Nhập ghi_chu 500 chars<br>2. Save | Lưu OK | Medium | FR-VI-03 input #5 max 500 |
| TC-DG-PC-026 | Boundary `ghi_chu` 501 chars → block (P1 F-011) | Login. | 1. Nhập 501 chars | Inline error "Ghi chú tối đa 500 ký tự" | Medium | FR-VI-03 input #5 max 500 |
| TC-DG-PC-027 | Force submit `quyet_dinh` invalid enum (P1 F-012) | Login `cb_pd_tw_01`. CHO_DUYET_PC. | 1. Force POST `/api/danh-gia/duyet-pc` body `quyet_dinh = "INVALID"` | 400/422 + lỗi enum constraint per FR-VI-04 input #2 (`DUYET / TU_CHOI`) | High | FR-VI-04 input #2 enum, security |
| TC-DG-PC-028 | `linh_vuc_phu_trach` multi-select + invalid FK (P2 F-027) | Login. | 1. Phân công cg_01 với linh_vuc_phu_trach = [DM-LV-01, DM-LV-02, DM-LV-03]<br>2. Force submit linh_vuc_phu_trach=[99999] | 1: lưu OK với 3 FK valid. 2: 400 FK constraint | Low | FR-VI-03 input #4 array FK |

## Tổng số TC: 28 (14 base + 6 edge A4 + 3 fill A6 + 5 Codex apply)

> **A4 done 2026-05-10** — 6 TC mới merge inline.
> **A6 placeholder — Fill GAP-A5.**
> **A7 placeholder — LOẠI/SỬA log.**
> **SPEC-CLARIFY-DG-02:** Self-assign người ĐG (cb_nv tự phân công chính mình) — pending BA.
