# Test Cases — FR-XI-03 (UC162): Trình phê duyệt CT

> **SRS Ref**: FR-XI-03, SCR-XI-01 action-bar Tab Thông tin (button [Gửi phê duyệt])
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: Transition DU_THAO → CHO_PHE_DUYET. Validate đủ thông tin trước khi trình. Gửi notification CB PD cùng cấp.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User CB NV đã login, CT thuộc đơn vị user

---

## Trường input

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | chuong_trinh_id | Y | identifier | FK → CHUONG_TRINH_HTPL, context |

---

## A. TRÌNH PHÊ DUYỆT — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TR-CT-001 | FR-XI-03 / Processing step 1-6 + AC | Trình PD CT đầy đủ thông tin | cb_nv_tw_01 login. CT-DT04 DU_THAO, đầy đủ ten/muc_tieu/thoi_gian_bat_dau/doi_tuong. | — | 1. Mở chi tiết CT-DT04. 2. Click [Gửi phê duyệt]. | (1) PATCH `/api/v1/.../submit` 200. (3) Trạng thái → CHO_PHE_DUYET. Notification gửi CB PD cùng cấp (cb_pd_tw_01). Audit log. | Happy 🔴 |
| TC-TR-CT-002 | FR-XI-03 / Processing step 5 | Notification gửi CB PD cùng cấp | cb_nv_dp_01 (Sở TP AG) login. CT-AG02 DU_THAO. | — | 1. Trình PD. | (3) Notification chỉ gửi `cb_pd_dp_01` (Sở TP AG cùng cấp + cùng đơn vị). KHÔNG gửi cb_pd_tw_01 hoặc cb_pd_bn_01. | Happy 🟡 |

---

## B. TRÌNH PHÊ DUYỆT — NEGATIVE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TR-CT-003 | FR-XI-03 / E1 ERR-XI-03-01 | Trình PD khi state ≠ DU_THAO | cb_nv_tw_01 login. CT-PD04 CHO_PHE_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Gửi phê duyệt] ẩn. Force API → reject "CT không ở trạng thái cho phép trình duyệt" (ERR-XI-03-01). | Negative 🔴 |
| TC-TR-CT-004 | FR-XI-03 / Processing step 3 (validate) | Trình PD khi thiếu trường bắt buộc | cb_nv_tw_01 login. CT-DT05 DU_THAO, thiếu `doi_tuong`. | — | 1. Mở chi tiết. 2. Click [Gửi phê duyệt]. | (2) Error "Vui lòng nhập đầy đủ thông tin bắt buộc" trước khi cho transition. KHÔNG persist trạng thái. | Negative 🔴 |
| TC-TR-CT-005 | FR-XI-03 / Permission | CB PD trình PD → reject | cb_pd_tw_01 login. CT-DT06 DU_THAO. | — | 1. Mở chi tiết. | (1) Nút [Gửi phê duyệt] ẩn (chỉ CB NV). | Negative 🟡 |

---

## C. TRÌNH PHÊ DUYỆT — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-TR-CT-006 | FR-XI-03 / Concurrency | Concurrent submit 2 tab | cb_nv_tw_01 login. CT-DT07 DU_THAO mở 2 tab. | — | 1. Tab1 click [Gửi PD]. 2. Tab2 click [Gửi PD] trong 1s. | (2) 1 request thành công, 1 reject với optimistic-lock hoặc state-already-changed (ERR-SYS-02 hoặc ERR-XI-03-01). | Edge 🟢 |

---

## Tổng kết file 04-TC

- **6 TC**: 2 Happy + 3 Negative + 1 Edge
- **Critical TC (🔴)**: 001, 003, 004

*Generated 2026-05-06 — Phase A step A3*
