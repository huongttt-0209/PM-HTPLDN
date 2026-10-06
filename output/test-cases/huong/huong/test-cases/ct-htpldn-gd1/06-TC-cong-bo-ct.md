# Test Cases — FR-XI-05 (UC164): Công bố / Hủy công bố CT lên Cổng PLQG

> **SRS Ref**: FR-XI-05, SCR-XI-01 action-bar Tab Thông tin (button [Công bố] + [Hủy công bố])
> **Ngày tạo**: 2026-05-06
> **Đặc thù**: BR-FLOW-05 (REST trực tiếp Cổng PLQG, không qua LGSP). Fail rollback DA_DUYET. Hủy công bố gỡ khỏi Cổng.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **Pre-conditions mặc định**: User CB NV đã login. CT thuộc đơn vị user.

---

## A. CÔNG BỐ — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-CT-001 | FR-XI-05 / Công bố step 1-5 + BR-FLOW-05 | Công bố CT lên Cổng PLQG | cb_nv_tw_01 login. CT-DD07 DA_DUYET. | — | 1. Mở chi tiết. 2. [Công bố] → modal confirm → OK. | (1) PATCH `/api/v1/.../publish` 200. (2) Outbound API call tới Cổng PLQG (verify qua MCP `list_network_requests` — endpoint FR-XII-15). (3) Trạng thái → DA_CONG_BO. `la_cong_bo=1`, `ngay_cong_bo=NOW()`. Audit log. | Happy 🔴 |
| TC-CB-CT-002 | FR-XI-05 / E2 ERR-XI-05-02 + Rollback (A6 strengthen) | API Cổng PLQG fail → rollback persistent | cb_nv_tw_01 login. CT-DD08 DA_DUYET. Cổng PLQG mock unavailable hoặc 5xx. | — | 1. [Công bố] → confirm. 2. Sau toast error → reload page (F5). | (2) Outbound API trả 5xx/timeout. Toast error "Không thể kết nối Cổng PLQG. Vui lòng thử lại" (ERR-XI-05-02). (3) Trạng thái rollback → DA_DUYET (KHÔNG persist DA_CONG_BO). `la_cong_bo=0`. **(4) Sau reload F5 → GET CT-DD08 trả về `trang_thai=DA_DUYET, la_cong_bo=0` — verify state KHÔNG transient persist DA_CONG_BO trong DB.** | Negative 🔴 |

---

## B. HỦY CÔNG BỐ — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-CT-003 | FR-XI-05 / Hủy công bố step 1-3 | Hủy công bố CT — gỡ khỏi Cổng | cb_nv_tw_01 login. CT-CB02 DA_CONG_BO. | — | 1. [Hủy công bố] → modal confirm → OK. | (1) PATCH `/api/v1/.../unpublish` 200. (2) Outbound API DELETE/PATCH Cổng PLQG (gỡ). (3) Trạng thái → DA_DUYET. `la_cong_bo=0`. Audit log. | Happy 🔴 |

---

## C. CÔNG BỐ — STATE GUARD + PERMISSION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-CT-004 | FR-XI-05 / E1 ERR-XI-05-01 | Công bố khi state ≠ DA_DUYET | cb_nv_tw_01 login. CT-DT08 DU_THAO. | — | 1. Mở chi tiết. | (1) Nút [Công bố] ẩn. Force API → reject "CT chưa được phê duyệt" (ERR-XI-05-01). | Negative 🔴 |
| TC-CB-CT-005 | FR-XI-05 / Permission | CB PD không được công bố | cb_pd_tw_01 login. CT-DD09 DA_DUYET. | — | 1. Mở chi tiết. | (1) Nút [Công bố] ẩn (chỉ CB NV). | Negative 🟡 |
| TC-CB-CT-006 | FR-XI-05 / BR-AUTH-08 | CB NV BN không công bố CT của ĐP | cb_nv_bn_01 login. CT-AG03 DA_DUYET (đơn vị Sở TP AG). | — | 1. Force deep-link. | (1) Không thấy CT (scope BR-AUTH-08). Force API → 403 / ERR-XI-05-01. | Negative 🟡 |

---

## D. CÔNG BỐ — EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-CB-CT-007 | FR-XI-05 / Công bố lặp | Công bố lại CT đã DA_CONG_BO | cb_nv_tw_01 login. CT-CB03 DA_CONG_BO. | — | 1. Mở chi tiết. | (1) Nút [Công bố] ẩn (chỉ hiện [Hủy công bố]). Force API → reject ERR-XI-05-01. | Edge 🟢 |
| TC-CB-CT-008 | FR-XI-05 / Concurrency | 2 tab công bố cùng lúc | cb_nv_tw_01 login. CT-DD10 DA_DUYET, mở 2 tab. | — | 1. Tab1 click [Công bố]. 2. Tab2 click [Công bố] trong 1s. | (2) 1 thành công, 1 reject (optimistic lock ERR-SYS-02 hoặc state-changed ERR-XI-05-01). KHÔNG double-publish lên Cổng. | Edge 🟡 |
| TC-CB-CT-009 | FR-XI-05 / Preconditions / SPEC-CLARIFY-CT-04 (A4 merged) | Công bố CT có `thoi_gian_ket_thuc` đã qua hôm nay | cb_nv_tw_01 login. CT-DD11 DA_DUYET, `thoi_gian_ket_thuc="2025-12-31"` (đã quá khứ so với hôm nay 2026-05-06). | — | 1. [Công bố] → confirm. | (3) **SRS Gap**: SRS không quy định cấm công bố CT đã hết hạn. Behavior có thể: (a) PASS — công bố OK (default per spec); (b) WARN — toast "CT đã quá hạn"; (c) REJECT — soft cấm. **SPEC-CLARIFY-CT-04** — cần BA xác nhận. Hiện tại expect (a) per spec literal. | Edge / SPEC 🟡 |

---

## Tổng kết file 06-TC

- **9 TC**: 3 Happy + 3 Negative/Permission + 3 Edge (A3 base 8 + A4 merged 1)
- **Critical TC (🔴)**: 001, 002, 003, 004
- **A4 merged 2026-05-06**: TC-CB-CT-009 (SPEC-CLARIFY-CT-04)

*Generated 2026-05-06 — Phase A step A3 + A4 inline merge*
