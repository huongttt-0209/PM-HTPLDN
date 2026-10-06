# Test Case — FR-X.2-06 Công khai / Hủy công khai Kho Câu hỏi (UC156)

> **File:** `05-TC-FR-X2-06-cong-khai-kho.md`
> **FR:** FR-X.2-06 (CB NV công khai / hủy công khai Q&A đã duyệt lên Cổng PLQG)
> **SCR:** SCR-X2-01 (action button [Công khai] / [Hủy công khai] trên dòng)
> **SRS Reference:** [`srs-fr-13-tv-nhanh-v3.1.md`](../../../input/srs-v3/srs-fr-13-tv-nhanh-v3.1.md) §FR-X.2-06 line 421-507
> **Loại:** B (browser, MCP chrome-devtools + verify network outbound API Cổng PLQG)

## TC Index

| TC ID | Tên TC | Trace | Tag | Role |
|-------|--------|-------|-----|------|
| TC-CK-001 | Công khai DA_DUYET → CONG_KHAI + thoi_gian_dang_tai | FR-X.2-06 / Processing CK 1-4 + BR-PUBLIC-03 | Happy core | CB_NV_TW |
| TC-CK-002 | Modal xác nhận hiển thị anh_dai_dien + mo_ta_cong_khai + file_dinh_kem trước khi đẩy | FR-X.2-06 / SCR row 12 | Happy | CB_NV_TW |
| TC-CK-003 | API outbound payload đẩy đủ 5 field công khai | FR-X.2-06 / Processing CK 3 | Happy | CB_NV_TW |
| TC-CK-004 | Hủy công khai CONG_KHAI → DA_DUYET + clear thoi_gian_dang_tai | FR-X.2-06 / Processing HCK 1-4 + BR-PUBLIC-02 | Happy core | CB_NV_TW |
| TC-CK-005 | thoi_gian_dang_tai format dd/mm/yyyy hh:mm + disabled input | BR-PUBLIC-03 line 927 | Happy | CB_NV_TW |
| TC-CK-006 | cong_khai cờ UI vs trang_thai - 2 cờ tách biệt | SRS line 430+693 | Happy edge | CB_NV_TW |
| TC-CK-007 | Re-publish DA_DUYET → CONG_KHAI sau khi đã hủy 1 lần | SM ⟷ DA_DUYET/CONG_KHAI | Happy | CB_NV_TW |
| TC-CK-008 | AUDIT_LOG ghi action='CONG_KHAI' và 'HUY_CONG_KHAI' | BR-DATA-05 + Processing 6 | Happy | CB_NV_TW |
| TC-CK-100 | E1 — API Cổng PLQG fail công khai → giữ DA_DUYET + ERR-TVN-CK-01 | FR-X.2-06 / E1 + BR-FLOW-05 | Negative core | CB_NV_TW |
| TC-CK-101 | E2 — API Cổng PLQG fail hủy công khai → giữ CONG_KHAI + ERR-TVN-CK-02 | FR-X.2-06 / E2 + BR-FLOW-05 | Negative core | CB_NV_TW |
| TC-CK-102 | E3 — Công khai bản ghi CHO_DUYET → block ERR-TVN-CK-03 (BR-PUBLIC-01) | FR-X.2-06 / E3 + BR-PUBLIC-01 | Negative core | CB_NV_TW |
| TC-CK-103 | Hủy công khai bản ghi DA_DUYET (chưa CK) → button không hiển thị | SCR row 12 | Negative state | CB_NV_TW |
| TC-CK-200 | Concurrent CK 2 CB NV cùng QA → race | A4 edge | Edge | CB_NV_TW |
| TC-CK-201 | API outbound timeout 30s → ERR + retry | A4 edge | Edge | CB_NV_TW |
| TC-CK-202 | thoi_gian_dang_tai timezone render | A4 edge | Edge | CB_NV_TW |
| TC-CK-203 | CK Q&A nguon=TU_DONG (anh_dai_dien default) | SPEC-CLARIFY-TVN-09 | Edge | CB_NV_TW |

---

## Test Cases

### TC-CK-001 — Công khai DA_DUYET → CONG_KHAI + thoi_gian_dang_tai

**Trace:** FR-X.2-06 / Processing CK 1-4 + BR-PUBLIC-03
**Precondition:**
- Login `cb_nv_tw_01`.
- Q&A QA-100 trang_thai=DA_DUYET, hieu_luc=1, có anh_dai_dien + mo_ta_cong_khai + 1 file_dinh_kem.
- Mock API Cổng PLQG return 200.

**Steps:**
1. Mở SCR-X2-01 → tìm QA-100 → click [Công khai].
2. Modal xác nhận hiển thị → click [Xác nhận].

**Expected (Codex P2 fix — UI bridge):**
- Toast "Đã công khai câu hỏi lên Cổng PLQG."
- Cột Trạng thái trên SCR-X2-01: CONG_KHAI (badge "Đã công khai").
- Cột "thoi_gian_dang_tai" hiển thị NOW() format dd/mm/yyyy hh:mm.
- Cột "Hiệu lực": ON.
- Network MCP outbound: `POST {ApiCongPLQG}/api/v1/cong-plqg/kho-cau-hoi/publish` body chứa cau_hoi + cau_tra_loi + anh_dai_dien + mo_ta_cong_khai + file_dinh_kem_cong_khai → 200.
- AUDIT_LOG (qua trang Nhật ký HT FR-10 W1.1): entry action='CONG_KHAI', entity=KHO_CAU_HOI, entity_id=QA-100, user=cb_nv_tw_01 + timestamp=NOW().
- Refresh list → record QA-100 vẫn DA_DUYET column nay đổi sang CONG_KHAI (verify persisted).

---

### TC-CK-002 — Modal xác nhận hiển thị 5 field công khai

**Trace:** FR-X.2-06 / SCR row 12 line 536
**Precondition:** QA-100 DA_DUYET có ảnh đại diện + mô tả công khai + 1 file đính kèm.

**Steps:**
1. Click [Công khai] → modal mở.

**Expected:**
- Modal xác nhận hiển thị preview:
  - Câu hỏi: ... (full text)
  - Câu trả lời: ... (rich text)
  - Ảnh đại diện: thumbnail
  - Mô tả công khai: ...
  - File đính kèm: tên file PDF + link download.
- Có nút [Hủy] và [Xác nhận đẩy lên Cổng].

---

### TC-CK-003 — API outbound payload đẩy đủ 5 field công khai

**Trace:** FR-X.2-06 / Processing CK 3
**Steps:**
1. MCP `list_network_requests` → click [Công khai] → [Xác nhận].
2. Inspect outbound request body.

**Expected:** Body JSON/multipart chứa:
- cau_hoi (text)
- cau_tra_loi (text/HTML rich)
- anh_dai_dien (file binary hoặc URL)
- mo_ta_cong_khai (text)
- file_dinh_kem_cong_khai (array files binary hoặc URLs)

---

### TC-CK-004 — Hủy công khai CONG_KHAI → DA_DUYET + clear thoi_gian_dang_tai

**Trace:** FR-X.2-06 / Processing HCK 1-4 + BR-PUBLIC-02
**Precondition:** QA-100 trang_thai=CONG_KHAI (sau TC-CK-001).

**Steps:**
1. Click [Hủy công khai] trên dòng QA-100 → modal xác nhận.
2. Click [Xác nhận hủy].

**Expected (Codex P2 fix — UI bridge):**
- Toast "Đã hủy công khai."
- Cột Trạng thái trên SCR-X2-01: DA_DUYET.
- Cột thoi_gian_dang_tai: trống.
- Network MCP outbound: `DELETE {ApiCongPLQG}/api/v1/cong-plqg/kho-cau-hoi/QA-100` → 200.
- AUDIT_LOG (qua trang Nhật ký HT FR-10 W1.1): entry action='HUY_CONG_KHAI', entity=KHO_CAU_HOI, entity_id=QA-100, user=cb_nv_tw_01 + timestamp=NOW().
- Refresh list → record QA-100 hiển thị DA_DUYET (persisted).

---

### TC-CK-005 — thoi_gian_dang_tai format dd/mm/yyyy hh:mm + disabled input

**Trace:** BR-PUBLIC-03 line 927
**Steps:**
1. Sau công khai → mở chi tiết QA-100 (hoặc edit).
2. Quan sát field thoi_gian_dang_tai.

**Expected:**
- Format hiển thị: vd "10/05/2026 14:30".
- Field disabled / read-only — KHÔNG cho user sửa tay.
- Network: nếu user thử PATCH thoi_gian_dang_tai → backend reject.

---

### TC-CK-006 — cong_khai cờ UI vs trang_thai - 2 cờ tách biệt

**Trace:** SRS line 430 + 693
**Precondition:** Mock API Cổng PLQG delay 5s trước khi return 200.

**Steps:**
1. Click [Công khai] → [Xác nhận].
2. Trong 5s chờ API, refresh list.

**Expected:**
- Trong 5s: cong_khai = 1, trang_thai = DA_DUYET (chưa CONG_KHAI).
- UI hiển thị spinner "Đang đẩy lên Cổng..." hoặc badge "Pending".
- Sau 5s API trả 200: trang_thai chuyển CONG_KHAI.
- Verify 2 cờ tách biệt: cong_khai=1 nhưng trang_thai≠CONG_KHAI nghĩa là đang chờ API.

---

### TC-CK-007 — Re-publish DA_DUYET → CONG_KHAI sau khi đã hủy 1 lần

**Trace:** SM ⟷ DA_DUYET/CONG_KHAI
**Precondition:** QA-100 đã CK, đã hủy CK (DA_DUYET).

**Steps:**
1. Click [Công khai] lại.

**Expected:**
- Public lại thành công, trang_thai → CONG_KHAI.
- thoi_gian_dang_tai = NEW NOW() (cập nhật, không giữ giá trị cũ).

---

### TC-CK-008 — AUDIT_LOG ghi action='CONG_KHAI' và 'HUY_CONG_KHAI'

**Trace:** BR-DATA-05 + Processing 6
**Steps:**
1. Công khai QA-100 → verify AUDIT_LOG.
2. Hủy công khai → verify AUDIT_LOG.

**Expected:**
- 2 entry AUDIT_LOG:
  - action='CONG_KHAI', entity=KHO_CAU_HOI, entity_id=QA-100.id, user_id=cb_nv_tw_01.id, timestamp=NOW().
  - action='HUY_CONG_KHAI', cùng entity, user_id, timestamp khác.
- Verify trên FR-10 W1.1 Nhật ký HT (`/quan-tri/audit-log`).

---

### TC-CK-100 — E1 API Cổng PLQG fail công khai → giữ DA_DUYET + ERR-TVN-CK-01

**Trace:** FR-X.2-06 / E1 + BR-FLOW-05
**Precondition:** Mock API Cổng PLQG return 500.

**Steps:**
1. Click [Công khai] → [Xác nhận].

**Expected:**
- Toast lỗi ERR-TVN-CK-01 "Lỗi kết nối Cổng PLQG khi công khai. Vui lòng thử lại".
- Cột Trạng thái: GIỮ DA_DUYET (KHÔNG chuyển CONG_KHAI).
- Cột thoi_gian_dang_tai: trống.
- DB: KHO_CAU_HOI.cong_khai có thể = 0 hoặc 1 (tùy implementation pre-flight) nhưng trang_thai PHẢI giữ DA_DUYET (BR-FLOW-05 line 897).
- Nút [Công khai] vẫn enabled để user thử lại.

---

### TC-CK-101 — E2 API Cổng PLQG fail hủy công khai → giữ CONG_KHAI + ERR-TVN-CK-02

**Trace:** FR-X.2-06 / E2 + BR-FLOW-05
**Precondition:** QA-100 CONG_KHAI. Mock API Cổng PLQG DELETE return 500.

**Steps:**
1. Click [Hủy công khai] → [Xác nhận].

**Expected:**
- Toast ERR-TVN-CK-02 "Lỗi kết nối Cổng PLQG khi hủy công khai. Vui lòng thử lại".
- Cột Trạng thái: GIỮ CONG_KHAI.
- thoi_gian_dang_tai: GIỮ giá trị cũ.

---

### TC-CK-102 — E3 Công khai bản ghi CHO_DUYET → block ERR-TVN-CK-03

**Trace:** FR-X.2-06 / E3 + BR-PUBLIC-01
**Precondition:** QA-200 trang_thai=CHO_DUYET.

**Steps:**
1. Cố gắng public bản ghi CHO_DUYET — nút [Công khai] KHÔNG hiển thị (theo SRS row 12 line 536: chỉ hiển thị khi DA_DUYET).
2. Truy cập trực tiếp API: `POST /api/v1/kho-cau-hoi/QA-200/publish`.

**Expected:**
- UI: Nút [Công khai] không có trên dòng CHO_DUYET.
- API: Reject 400 ERR-TVN-CK-03 "Không thể thực hiện. Trạng thái hiện tại không cho phép".

---

### TC-CK-103 — Hủy công khai bản ghi DA_DUYET (chưa CK) → button không hiển thị

**Trace:** SCR row 12
**Steps:**
1. QA-100 ở DA_DUYET (chưa từng CK) → quan sát action column.

**Expected:** Chỉ nút [Công khai] hiển thị, KHÔNG có [Hủy công khai] (vì chưa CK).

---

---

## Edge bổ sung A4

### TC-CK-200 — Concurrent CK 2 CB NV cùng QA — race condition

**Trace:** A4 edge (sibling FR-02 BUG-EC-04 lock TTL pattern)
**Steps:**
1. CB-A và CB-B (cùng đơn vị) cùng mở QA-100 DA_DUYET.
2. CB-A click [Công khai] + [Xác nhận] → API outbound đang chạy (lock TTL).
3. CB-B click [Công khai] trên cùng QA-100 trong khi CB-A đang chờ API.

**Expected:**
- CB-B nhận error "Câu hỏi đang được công khai bởi CB khác. Vui lòng thử lại sau."
- API call lần 2 từ CB-B reject hoặc 409.
- KHÔNG tạo 2 lệnh push API outbound song song (chống ghi trùng Cổng PLQG).
- **SPEC-CLARIFY:** SRS FR-13 không khai báo lock TTL — lấy pattern sibling FR-II line F-42 (lock TTL 30s).

---

### TC-CK-201 — API outbound timeout 30s → ERR-TVN-CK-01 + retry

**Steps:**
1. Mock API Cổng PLQG response delay 35s (timeout 30s threshold).
2. Click [Công khai].

**Expected:**
- Sau 30s timeout: hiển thị toast ERR-TVN-CK-01.
- Trang_thai giữ DA_DUYET.
- Nút [Công khai] enabled lại để retry.

---

### TC-CK-202 — thoi_gian_dang_tai timezone server vs client

**Steps:**
1. Client browser TZ = GMT+7 (Asia/Ho_Chi_Minh).
2. Server TZ = UTC.
3. Click [Công khai] lúc 14:30 GMT+7 (07:30 UTC).

**Expected:**
- thoi_gian_dang_tai hiển thị "10/05/2026 14:30" (theo TZ user, không phải 07:30 UTC).
- DB lưu UTC nhưng UI render local TZ.
- **SPEC-CLARIFY:** SRS không nói rõ TZ render — sibling pattern các module khác đều render local TZ.

---

### TC-CK-203 — CK Q&A nguon=TU_DONG (kế thừa từ HOI_DAP)

**Trace:** SPEC-CLARIFY-TVN-09
**Precondition:** QA-AUTO nguon=TU_DONG, hoi_dap_goc_id=HD-100, KHÔNG có anh_dai_dien custom (kế thừa default).

**Steps:**
1. Click [Công khai] trên QA-AUTO.

**Expected:**
- **SPEC-CLARIFY-TVN-09:** TU_DONG có anh_dai_dien default (ảnh hệ thống) hay null?
  - **Option A:** Mặc định ảnh hệ thống (theo SRS line 110 default).
  - **Option B:** Bắt CB NV phải set anh_dai_dien trước khi CK.
- Default Option A: Modal CK hiển thị ảnh hệ thống → API outbound đẩy ảnh hệ thống.

---

**Tổng số TC:** 16 TC (8 Happy + 4 Negative + 4 Edge A4)

*Generated 2026-05-10 — Phase A step A3 (bmad-qa-generate-e2e-tests) + A4 edge merge*
