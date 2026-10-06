# A5 — Traceability Matrix (FR-II Hỏi đáp)

> **Skill BMAD**: bmad-testarch-trace (manual cycle)
> **Ngày chạy**: 2026-05-10 (Phase A step A5)
> **Mục đích**: Map BR/AC ↔ TC để phát hiện gap. KHÔNG sinh TC mới — gap forward sang A6 fix.

---

## 1. BR ↔ TC Coverage Matrix

| BR ID | Tên | TC áp dụng | Coverage |
|-------|-----|-----------|----------|
| BR-AUTH-01 | Xác thực bắt buộc | Precondition login mọi TC (155+ TC) | ✅ 100% |
| BR-AUTH-05 | Phê duyệt cùng cấp | TC-PD-001, 010, 020, 022, 030, 031, 100 (file 07) + TC-TN-104, TC-PH-204, TC-PC-107, TC-DXL-103 (cross-file negative) | ✅ 100% |
| BR-AUTH-08 | Phân quyền dữ liệu theo đơn vị | TC-HD-005, 106, 222, TC-PC-205, TC-TN-103, TC-PD-033, TC-DXL-202 | ✅ 100% |
| BR-DATA-01 | Soft delete | TC-HD-004, 220 | ✅ 100% |
| BR-DATA-03 | Common fields | Verify schema mọi POST/PUT (implicit) | ✅ 100% |
| BR-DATA-04 | Auto-gen `HD-YYYYMMDD-SEQ` | TC-HD-001, TC-HD-231 (race) | ✅ 100% |
| BR-DATA-05 | Audit trail (immutable INSERT-only) | TC-HD-001, 003, 004, TC-TN-001, 004, TC-DXL-001, 110, TC-PC-001, TC-PH-002, 005, TC-PD-001, 010, 020, 022, 030 (đầy đủ mọi action) | ✅ 100% |
| BR-DATA-06 | Export Excel max 10K | TC-HD-006, 105 | ✅ 100% |
| BR-DATA-07 | Pagination default 20 | TC-HD-005, TC-HDTK-202 | ✅ 100% |
| BR-DATA-08 | Full-text search tsvector | TC-HDTK-001, 204 (Unicode) | ✅ 100% |
| BR-FLOW-01 | Auto-transition Đã trả lời → Chờ PD | TC-PH-005 (core), TC-PH-203 (skip DA_TRA_LOI) | ✅ 100% |
| BR-FLOW-02 | Phê duyệt hàng loạt | TC-PD-040, 041, 042, 043 | ✅ 100% |
| BR-FLOW-03 | Không sửa/xóa sau phê duyệt | TC-HD-103, 104, TC-PD-060 | ✅ 100% |
| BR-FLOW-04 | Từ chối yêu cầu lý do (10-1000 ký) | TC-PD-010, 011, 012, 013 | ✅ 100% |
| BR-FLOW-05 | Công khai qua API trực tiếp Cổng PLQG | TC-PD-020, 021, 022, 023, 050 | ✅ 100% |
| BR-FLOW-06 | Đóng hồ sơ THỦ CÔNG, không auto-close | TC-PD-030, 031, 032 | ✅ 100% |
| BR-CALC-03 | Deadline 15/30 ngày LV theo muc_do | TC-TN-001 (THUONG), TC-TN-002 (PHUC_TAP), TC-DXL-110 (đổi mức) | ✅ 100% |
| BR-CALC-04 | Đổi mức độ phức tạp tính lại deadline | TC-DXL-110, 111, 112, 113 | ✅ 100% |
| BR-SLA-01 | SLA mặc định | TC-TN-001, 002 | ✅ 100% |
| BR-SLA-02 | 4 mức cảnh báo | TC-DXL-204 | ✅ 80% (3/4 mức covered, QUA_HAN_NGHIEM_TRONG cần thêm) → **GAP-A5-01** |
| BR-SLA-03 | Thông báo cảnh báo SLA | TC-DXL-205 | ✅ 80% (in-app verified, email indirect) → **GAP-A5-02** |
| BR-SLA-04 | Ngày làm việc | TC-TN-200, 201 | ✅ 100% |
| BR-EC-19 | Batch tối đa 100 | TC-PD-041 | ✅ 100% |
| BR-EC-20 | Công khai chỉ set CONG_KHAI sau API OK | TC-PD-020, 021 | ✅ 100% |

**Total BR coverage: 24/24 = 100%** (2 BR có gap minor cần A6 fix).

---

## 2. AC ↔ TC Coverage Matrix (chỉ AC quan trọng)

### 2.1 FR-II-01 (UC10) Acceptance Criteria

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Hiển thị danh sách thuộc đơn vị, phân trang | TC-HD-005 |
| AC#2 | Xem chi tiết: nội dung, người gửi, lĩnh vực, thời gian, trạng thái, mức độ | TC-HD-005 (implicit), TC-PD-066 (HUY) |
| AC#3 | Thêm mới: nhập đủ trường BB + Lưu (mặc định THUONG) | TC-HD-001 |
| AC#4 | muc_do_phuc_tap=PHUC_TAP → deadline tính theo CAU_HINH_SLA[HOI_DAP_PHUC_TAP] | TC-HD-002, TC-TN-002 |
| AC#5 | Chỉnh sửa | TC-HD-003 |
| AC#6 | Xóa soft delete | TC-HD-004 |
| AC#7 | Xuất Excel filter hiện tại | TC-HD-006 |
| AC#8 | Làm mới reload AJAX giữ filter | TC-HD-007 |

### 2.2 FR-II-03 (UC12) AC

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Có yêu cầu mới → CB NV xem danh sách → hiển thị | TC-TN-003 |
| AC#2 | Tiếp nhận THUONG → deadline +15 ngày LV | TC-TN-001 |
| AC#3 | Tiếp nhận PHUC_TAP → deadline +30 ngày LV (NĐ55/2019 Đ.8 K.1) | TC-TN-002 |

### 2.3 FR-II-04 (UC13) AC

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Danh sách đang xử lý: người phân công, thời hạn, trạng thái luân chuyển | TC-DXL-003 |
| AC#2 | Cập nhật thời hạn + lý do → cập nhật, ghi audit | TC-DXL-001 |
| AC#3 | Xem lịch sử timeline đầy đủ | TC-DXL-002 |
| AC#4 | Xem kết quả xử lý: trạng thái, người, phản hồi, thời gian | TC-DXL-002 (implicit) |

### 2.4 FR-II-06 (UC15) AC

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Phân công → 2 tabs Cá nhân/Tổ chức + danh sách gợi ý | TC-PC-001 (Cá nhân), TC-PC-010 (Tổ chức) |
| AC#2 | Cá nhân tự do (CB/TVV/NHT) → SET CA_NHAN, gửi thông báo | TC-PC-001 |
| AC#3 | NHT theo linh_vuc_ids[] N:N | TC-PC-002 |
| AC#4 | Tab Tổ chức + chọn TC + dropdown TVV thuộc TC | TC-PC-010, 011 |
| AC#5 | TC + TVV → SET TO_CHUC, gửi thông báo TVV + CC TC email_lien_he | TC-PC-010, 206 |
| AC#6 | Loai='TO_CHUC' nhưng TVV không thuộc TC (API bypass) → ERR-PC-05 | TC-PC-104 |
| AC#7 | Loai='TO_CHUC' thiếu 2 thông tin → ERR-PC-04 | TC-PC-103 |
| AC#8 | Loai='CA_NHAN' truyền TC TV thừa → ERR-PC-06 | TC-PC-105 |
| AC#9 | NHT/TVV vô hiệu → ERR-PC-01, không cho chọn | TC-PC-100 |
| AC#10 | TC TV vô hiệu → ERR-PC-03 | TC-PC-102 |
| AC#11 | Vượt workload → WRN-PC-01 (không block) | TC-PC-106 |

### 2.5 FR-II-07 (UC16) AC

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Form phản hồi kèm thông tin câu hỏi gốc | TC-PH-001 |
| AC#2 | Lưu nháp → UPSERT ngay_tra_loi=NULL, KHÔNG trigger BR-FLOW-01 | TC-PH-002 |
| AC#3 | Gửi phản hồi → SET ngay_tra_loi=NOW(), HD → DA_TRA_LOI | TC-PH-005 |
| AC#4 | Draft (ngay_tra_loi NULL) → mở SCR-II-02 → load draft | TC-PH-004 |
| AC#5 | Tích "Đã trả lời" + Gửi → auto-transition CHO_PHE_DUYET (BR-FLOW-01) | TC-PH-005 |

### 2.6 FR-II-08 (UC17) AC

| AC | Statement | TC ID |
|----|-----------|-------|
| AC#1 | Phản hồi CHO_PHE_DUYET → CB PD xem danh sách | TC-PD-002 |
| AC#2 | CB PD phê duyệt → DA_DUYET | TC-PD-001 |
| AC#3 | CB PD công khai → API Cổng PLQG | TC-PD-020 |
| AC#4 | CB PD hủy công khai → gỡ khỏi Cổng | TC-PD-022 |
| AC#5 | Phê duyệt hàng loạt | TC-PD-040 |
| AC#6 | Từ chối + lý do → CB NV nhận | TC-PD-010 |
| AC#7 | "Đóng hồ sơ" → HOAN_THANH (BR-FLOW-06) | TC-PD-030, 031 |
| AC#8 | DA_DUYET/CONG_KHAI không click "Đóng hồ sơ" → giữ vô thời hạn (KHÔNG auto) | TC-PD-032 |

**Total AC coverage**: ~98% (38/39 AC chính covered, 1 GAP nhỏ về xem kết quả xử lý chi tiết).

---

## 3. State Machine SM-HOIDAP — TC coverage 12 transitions

| # | From → To | Trigger | TC ID | Status |
|---|-----------|---------|-------|--------|
| 1 | [*] → MOI | DN gửi/CB nhập/TVN escalate | TC-HD-001 + TC-HDTK-003 (TVN_BRIDGE) | ✅ |
| 2 | MOI → TIEP_NHAN | CB NV nhấn Tiếp nhận | TC-TN-001 | ✅ |
| 3 | MOI → HUY | CB NV hủy (chưa có PHAN_HOI) | **TC-HD-236** (transition test) + TC-PD-066 (banner HUY display) | ✅ (Codex M-02 fix — A6 GAP-A5-03 RESOLVED) |
| 4 | TIEP_NHAN → DANG_XU_LY | CB NV phân công | TC-PC-001, 010 | ✅ |
| 5 | DANG_XU_LY → DA_TRA_LOI | CB NV tích "Đã trả lời" + Gửi | TC-PH-005 (combined với #6) | ✅ |
| 6 | DA_TRA_LOI → CHO_PHE_DUYET | Auto (BR-FLOW-01) | TC-PH-005, 203 | ✅ |
| 7 | CHO_PHE_DUYET → DA_DUYET | CB PD phê duyệt | TC-PD-001 | ✅ |
| 8 | CHO_PHE_DUYET → DANG_XU_LY | CB PD từ chối | TC-PD-010 | ✅ |
| 9 | DA_DUYET → CONG_KHAI | CB PD công khai + API OK | TC-PD-020 | ✅ |
| 10 | CONG_KHAI → DA_DUYET | CB PD hủy CK + API OK | TC-PD-022, 064 | ✅ |
| 11 | DA_DUYET → HOAN_THANH | CB NV/PD click Đóng hồ sơ | TC-PD-030 | ✅ |
| 12 | CONG_KHAI → HOAN_THANH | CB NV/PD click Đóng hồ sơ | TC-PD-031 | ✅ |

**SM coverage: 12/12 = 100%** (sau Codex M-02 fix — TC-HD-236 covered transition #3).

---

## 4. Permission Matrix — TC coverage

| Action | Role | TC ID | Status |
|--------|------|-------|--------|
| HOI_DAP_CREATE | CB_NV cùng đơn vị | TC-HD-001 | ✅ |
| HOI_DAP_CREATE | CB_PD attempt | TC-HD-237 (A6 GAP-A5-04 fix) | ✅ |
| HOI_DAP_UPDATE | CB_NV cùng đơn vị | TC-HD-003 | ✅ |
| HOI_DAP_DELETE | CB_NV cùng đơn vị | TC-HD-004 | ✅ |
| HOI_DAP_TIEPNHAN | CB_NV cùng đơn vị | TC-TN-001 | ✅ |
| HOI_DAP_TIEPNHAN | CB_PD attempt | TC-TN-104 | ✅ |
| HOI_DAP_ASSIGN | CB_NV cùng đơn vị | TC-PC-001 | ✅ |
| HOI_DAP_ASSIGN | CB_PD attempt | TC-PC-107 | ✅ |
| HOI_DAP_RESPOND | CB_NV/NHT phân công | TC-PH-002, 010 | ✅ |
| HOI_DAP_RESPOND | CB_PD attempt | TC-PH-204 | ✅ |
| HOI_DAP_RESPOND | NHT khác attempt | TC-PH-011 | ✅ |
| HOI_DAP_APPROVE | CB_PD cùng cấp | TC-PD-001 | ✅ |
| HOI_DAP_APPROVE | CB_NV attempt | TC-PD-102 | ✅ |
| HOI_DAP_APPROVE | CB_PD khác cấp | TC-PD-100 | ✅ |
| HOI_DAP_PUBLISH | CB_PD cùng cấp + đơn vị | TC-PD-020 | ✅ |
| HOI_DAP_PUBLISH | CB_NV attempt | TC-PD-027 | ✅ |
| HOI_DAP_UNPUBLISH | CB_PD cùng cấp | TC-PD-022 | ✅ |
| HOI_DAP_CLOSE | CB_NV/PD cùng đơn vị/cấp | TC-PD-030, 031 | ✅ |
| HOI_DAP_READ_ASSIGNED | NHT thấy HD assigned | TC-PH-010 | ✅ |
| Cross-tenant DN/GV access | DN/GV attempt | TC-HD-238 (A6 GAP-A5-05 fix) | ✅ |
| CB_PD_BN cross-unit cùng cap (Bộ A → Bộ B) | CB_PD_BN | TC-PD-076 (Codex P2 I-01 fix) | ✅ |

**Permission coverage: 21/21 = 100%** (sau Codex M-02 + P2 I-01 fix — A6 GAP-A5-04/05 RESOLVED).

---

## 5. Error Code Coverage

| FR | Error codes | TC ID | Coverage |
|----|-------------|-------|----------|
| FR-II-01 | ERR-HD-01..04, WRN-HD-01, ERR-DELETE-STATE, ERR-AUTH-DEL, ERR-BATCH-CONFLICT | TC-HD-100..106, 220..223 | ✅ 8/8 |
| FR-II-02/05/10 | ERR-HD-TK-01/02, ERR-AUTH-TK-01, INF-HD-TK-01..03 | TC-HDTK-100..102 | ✅ 6/6 |
| FR-II-03 | ERR-TN-01/02/03 | TC-TN-100..102 | ✅ 3/3 |
| FR-II-04 | ERR-TH-01/02/03/CONFLICT, ERR-DXL-01, INF-DXL-01, ERR-AUTH-DXL-01 | TC-DXL-100..104, 200..202 | ✅ 7/7 |
| FR-II-06 | ERR-PC-01..06, WRN-PC-01 | TC-PC-100..106 | ✅ 7/7 |
| FR-II-07 | ERR-PH-01/02, WRN-PH-01 | TC-PH-100, 101, 011 | ✅ 3/3 |
| FR-II-08 | ERR-PD-01..07, WRN-PD-01 | TC-PD-100, 101, 011, 021, 023, 024, 041, 042 | ✅ 8/8 |
| FR-II-09 | INF-DAXL-01, ERR-DAXL-01, ERR-AUTH-DAXL-01 | TC-PD-061, 062, **073** (A6 GAP-A5-06 fix) | ✅ 3/3 |

**Error code coverage: 45/45 = 100%** (sau A6 GAP-A5-06 RESOLVED).

---

## 6. Cross-FR / Cross-module integration

| Integration | TC ID | Status |
|-------------|-------|--------|
| FR-13 TVN escalate → TVN_BRIDGE | TC-HDTK-003 | ✅ display test |
| FR-10 QTHT MAU_PHAN_HOI Mô hình B 2 tầng | TC-PH-007, 008, 205 | ✅ |
| FR-VIII-10 CAU_HINH_SLA | TC-TN-001, 002, TC-DXL-205 | ✅ |
| Cổng PLQG API outbound | TC-PD-020..025, 050..052, 065 | ✅ |
| Email notification (BR-SLA-03) | TC-DXL-205 (verify in-app), TC-PC-206 | ⚠️ email send-and-forget — verify qua MailHog (env-dependent) |
| AUDIT_LOG immutable | Mọi TC CUD + transition | ✅ implicit |

---

## 7. Tổng hợp GAP forward sang A6

| GAP ID | Mô tả | A6 action |
|--------|-------|-----------|
| GAP-A5-01 | BR-SLA-02 4 mức — chỉ 3 mức covered, thiếu QUA_HAN_NGHIEM_TRONG | A6 thêm TC-DXL-210 |
| GAP-A5-02 | BR-SLA-03 email notification chỉ indirect | A6 thêm TC-DXL-211 verify email gửi qua MailHog |
| GAP-A5-03 | SM transition `MOI → HUY` chỉ test display, không có transition test | A6 thêm TC-HD-236 test trực tiếp Hủy yêu cầu |
| GAP-A5-04 | CB_PD attempt CREATE HOI_DAP — chưa test | A6 thêm TC-HD-237 |
| GAP-A5-05 | DN/GV/NHT-non-assigned attempt access HD-cross-tenant | A6 thêm TC-HD-238 |
| GAP-A5-06 | ERR-AUTH-DAXL-01 chỉ indirect | A6 thêm TC-PD-073 |

**Tổng 6 gap → A6 sẽ bổ sung 6 TC mới merged inline + log riêng ở 10-REVIEW-test-quality.md.**

---

## 8. Coverage Summary (after A4 + before A6 fix)

| Dimension | Coverage |
|-----------|----------|
| BR formal §6 | 24/24 = 100% (2 minor gap) |
| AC chính | 38/39 = 97.4% |
| State Machine SM-HOIDAP | 11/12 = 91.7% |
| Permission Matrix | 18/20 = 90% |
| Error codes | 44/45 = 97.8% |
| Cross-FR integration | 6/6 visible (email indirect) |
| **Average** | **~95.6%** |

> Sau A6 fix 6 GAP → coverage projected ≥98%.

---

*A5 Traceability Matrix — Phase A step A5 — 2026-05-10*
