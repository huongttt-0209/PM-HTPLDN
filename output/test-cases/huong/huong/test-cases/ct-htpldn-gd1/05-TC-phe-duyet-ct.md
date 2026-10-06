# Test Cases — FR-XI-04 (UC163): Phê duyệt / Từ chối CT

> **SRS Ref**: FR-XI-04, SCR-XI-01 action-bar Tab Thông tin (button [Phê duyệt] + [Từ chối])
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: BR-AUTH-05 (cùng cấp). BR-FLOW-04 (TC bắt buộc lý do). Transition CHO_PHE_DUYET → DA_DUYET / DU_THAO.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User CB PD đã login, có quyền "Phê duyệt CT HTPLDN"

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | chuong_trinh_id | Y | identifier | Context |
| 2 | quyet_dinh | Y | enum | DUYET / TU_CHOI |
| 3 | ly_do_tu_choi | Conditional | text (long) | Bắt buộc khi TU_CHOI |
| 4 | ghi_chu_phe_duyet | N | text (long) | — |

---

## A. PHÊ DUYỆT — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-CT-001 | FR-XI-04 / Processing step 1-6 + AC | CB PD duyệt CT cùng cấp | cb_pd_tw_01 login. CT-PD05 CHO_PHE_DUYET (trình bởi cb_nv_tw_01). | quyet_dinh=DUYET, ghi_chu="OK" | 1. Mở chi tiết CT-PD05. 2. [Phê duyệt] → modal confirm + ghi chú → OK. | (1) PATCH `/api/v1/.../approve` 200. (3) Trạng thái → DA_DUYET. `nguoi_phe_duyet_id=cb_pd_tw_01.id`, `ngay_phe_duyet=NOW()`. Notification CB NV. Audit log. | Happy 🔴 |
| TC-PD-CT-002 | FR-XI-04 / Processing step 4 | CB PD từ chối có lý do | cb_pd_dp_01 login. CT-PD06 CHO_PHE_DUYET (trình bởi cb_nv_dp_01). | quyet_dinh=TU_CHOI, ly_do_tu_choi="Cần bổ sung đối tượng" | 1. [Từ chối] → modal nhập lý do → OK. | (3) Trạng thái → DU_THAO (KHÔNG phải HOAN_CHINH). Lý do persist. Notification CB NV kèm lý do. Audit log. | Happy 🔴 |
| TC-PD-CT-010 | FR-XI-04 / Processing step 5 (A6 merged) | CB NV nhận notification sau khi PD duyệt | cb_pd_tw_01 + cb_nv_tw_01 login (2 session). CT-PD11 CHO_PHE_DUYET (trình bởi cb_nv_tw_01). | quyet_dinh=DUYET | 1. cb_pd_tw_01 [Phê duyệt]. 2. Switch sang cb_nv_tw_01 session. 3. Mở Notification panel. | (3) cb_nv_tw_01 thấy notification mới: "CT '...' đã được phê duyệt". Click → mở chi tiết CT-PD11, trạng thái=DA_DUYET. | Happy 🟡 |
| TC-PD-CT-003 | FR-XI-04 / E2 ERR-XI-04-02 + BR-FLOW-04 | Từ chối thiếu lý do → reject | cb_pd_tw_01 login. CT-PD07 CHO_PHE_DUYET. | quyet_dinh=TU_CHOI, ly_do_tu_choi="" | 1. [Từ chối] → bỏ trống lý do → Submit. | (2) Error inline "Vui lòng nhập lý do từ chối" (ERR-XI-04-02). KHÔNG transition. | Negative 🔴 |

---

## B. PHÊ DUYỆT — PERMISSION (BR-AUTH-05 cùng cấp)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-CT-004 | FR-XI-04 / E3 ERR-XI-04-03 + BR-AUTH-05 | CB PD ĐP duyệt CT của BN → reject | cb_pd_dp_01 (Sở TP AG) login. CT-BN01 CHO_PHE_DUYET (trình bởi cb_nv_bn_01 BKHĐT). | — | 1. Force xem chi tiết CT-BN01. | (1) CT-BN01 KHÔNG xuất hiện trong DS scope (BR-AUTH-08); deep-link → 403 hoặc nút [Phê duyệt] ẩn. Force API → reject "Bạn chỉ được phê duyệt CT cùng cấp" (ERR-XI-04-03). | Negative 🔴 |
| TC-PD-CT-005 | FR-XI-04 / BR-AUTH-05 cross-đơn vị cùng cấp (A6 strengthen) | CB PD ĐP đơn vị X duyệt CT đơn vị Y cùng cấp ĐP | cb_pd_dp_01 (Sở TP AG) login. CT-BG01 CHO_PHE_DUYET (Sở TP BG, cùng cấp ĐP). | — | 1. Mở DS. | **Primary expected (per BR-AUTH-08 default scope):** (1) CT-BG01 KHÔNG xuất hiện trong DS scope của Sở TP AG. Force deep-link → 403 hoặc redirect Empty. **Alternative (cần BA xác nhận):** Nếu rule diễn giải "cùng cấp" = cấp ĐP trên toàn quốc → CT-BG01 visible read-only nhưng [Phê duyệt] ẩn / API reject ERR-XI-04-03. **B-Verify ưu tiên Primary, fallback Alternative qua 2-source check.** **SPEC-CLARIFY-CT-01:** cần BA. | Edge / SPEC 🟡 |
| TC-PD-CT-006 | FR-XI-04 / Permission | CB NV không được phê duyệt | cb_nv_tw_01 login. CT-PD08 CHO_PHE_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Phê duyệt] / [Từ chối] ẩn. | Negative 🟡 |

---

## C. PHÊ DUYỆT — STATE GUARD

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-CT-007 | FR-XI-04 / E1 ERR-XI-04-01 | Phê duyệt khi state ≠ CHO_PHE_DUYET | cb_pd_tw_01 login. CT-DD06 DA_DUYET. | quyet_dinh=DUYET | 1. Mở chi tiết. | (1) Nút [Phê duyệt] ẩn. Force API → reject "CT không ở trạng thái chờ phê duyệt" (ERR-XI-04-01). | Negative 🟡 |
| TC-PD-CT-008 | FR-XI-04 / Concurrency | 2 CB PD duyệt cùng lúc | cb_pd_tw_01 + cb_pd_tw_02 login. CT-PD09 CHO_PHE_DUYET. | — | 1. tw_01 click [Duyệt]. 2. tw_02 click [Duyệt] trong 1s. | (2) 1 request thành công, 1 reject (optimistic lock ERR-SYS-02 hoặc state-changed ERR-XI-04-01). | Edge 🟡 |

---

## D. PHÊ DUYỆT — UI / UX

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-CT-009 | FR-XI-04 / SCR-XI-01 row#21 | Modal duyệt hiển thị thông tin CT đầy đủ | cb_pd_tw_01 login. CT-PD10 CHO_PHE_DUYET. | — | 1. Click [Phê duyệt]. | (3) Modal hiển thị tóm tắt: Mã CT, Tên CT, Mục tiêu, Đơn vị trình, Người trình + textarea ghi chú. | UI 🟢 |

---

## Tổng kết file 05-TC

- **10 TC**: 4 Happy + 4 Negative/Permission + 1 Edge + 1 UI (A3 base 9 + A6 merged 1)
- **Critical TC (🔴)**: 001, 002, 003, 004
- **A6 merged 2026-05-06**: TC-PD-CT-010 (notification CB NV)
- **A6 strengthen 2026-05-06**: TC-PD-CT-005 expected primary/alternative

*Generated 2026-05-06 — Phase A step A3 + A6 inline merge*
