# Bug Report — Đánh giá Hiệu quả HTPL (FR-VI-10 read-only)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000 |
| **Người test** | QA Automation (Chrome DevTools MCP) |
| **Ngày** | 2026-05-14 12:30:00 |
| **Loại test** | Functional / Permission |
| **Round** | R23 |
| **Tài liệu tham chiếu** | [srs-fr-08-danh-gia.md §FR-VI-10](../../../../input/srs-update-2026-5-5/srs-fr-08-danh-gia.md) line 755-791 |

---

## Tổng hợp

Phát hiện **1** lỗi có SRS reference cụ thể trong quá trình test TC R7.4.D2b (FR-VI-10 CB NV read-only cross-co-quan). **R23 update**: VPD gate đã FIX → đề xuất downgrade Major P1 → Minor P3, giữ Open chờ dev đổi error code wording mismatch (ERR-AUTH-VPD-00-02 → ERR-DG-10).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 0     | 0      | 1     | 0       | 0      | 1    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | SRS Reference | Title | Status |
|--------|----------|----------|------|--------|---------------|-------|--------|
| BUG-FUNC-DG-013 | Minor | P3 | Wording | R7.4.D2b TC2 | `srs-update-2026-5-5/srs-fr-08-danh-gia.md:786` ERR-DG-10 | BE trả error code `ERR-AUTH-VPD-00-02` khi CB NV cross-cơ quan bị deny, spec yêu cầu `ERR-DG-10` (VPD gate đã fix R23, còn wording mismatch) | Open |

---

## BUG-FUNC-DG-013 — BE trả error code `ERR-AUTH-VPD-00-02` cross-cơ quan thay vì spec `ERR-DG-10` (residual sau VPD gate fix R23)

> **Re-test:** 2026-05-14 12:30:00 R23-verify3 (UI-first per user feedback) — ⚠️ CONFIRMED OPEN Minor P3 (wording residual sau VPD gate fix). Verify UI step-by-step 2 role mới: (1) `cb_pd_dp_01` STP-AG (CB_PD_DP same cơ quan) — sidebar Đánh giá HQ → list `/danh-gia/ke-hoach/danh-sach` thấy 4 KH gồm DG-20260513-0001 ✓; click eye button → FE redirect `/403` "Bạn không có quyền truy cập" + "Vai trò hiện tại: CB_PD_DP"; nhưng API direct GET 3 endpoint detail/bao-cao/ket-quas đều 200 OK → **FE route guard chặn role CB_PD_DP dù BE allow** (FE/BE permission disconnect — finding mới ngoài bug gốc). (2) `cb_nv_dp_02` STP-BG (CB_NV_DP cross-cơ quan) — sidebar list render "Không có kế hoạch đánh giá nào phù hợp" (BE filter VPD ẩn KH cross-cơ quan) ✓; force navigate `/danh-gia/ke-hoach/{DG-AG-id}` → FE redirect `/403` text generic; API direct GET 3 endpoint trả 403 `code=ERR-AUTH-VPD-00-02` (KHÔNG phải `ERR-DG-10` per `srs-fr-08-danh-gia.md:786`). **Kết luận:** bug gốc ERR code wording vẫn open (cần BE đổi mapping 403 cross-cơ quan FR-VI-10 → ERR-DG-10); thêm phát hiện FE generic `/403` thiếu domain-specific message + FE chặn CB_PD_DP same cơ quan dù SRS line 766 chỉ require "thuộc cơ quan được đánh giá" (không giới hạn role nội bộ). Evidence: [image/r23-bug-dg-013-FIXED-cbnvdp01-see-DG-20260513-0001-2026-05-14.png](../../reverify-2026-05-12/image/r23-bug-dg-013-FIXED-cbnvdp01-see-DG-20260513-0001-2026-05-14.png) · [image/r23v2-bug-dg-013-ui-generic-403-2026-05-14.png](../../reverify-2026-05-12/image/r23v2-bug-dg-013-ui-generic-403-2026-05-14.png).

### 1. Mô tả

CB NV thuộc đúng cơ quan được đánh giá (`don_vi_id` trùng `co_quan_duoc_danh_gia_id` của kế hoạch) cố truy cập kết quả đánh giá đợt đã HOAN_THANH thì bị BE từ chối với mã `ERR-AUTH-VPD-00-02` "Đơn vị không nằm trong phạm vi truy cập của bạn". Đợt DG-20260513-0001 do `cb_nv_tw_02` (BTP-TW) tạo nhưng `co_quan_duoc_danh_gia_id = STP-AG`. Trong khi đó cb_nv_dp_01 thuộc STP-AG = chính cơ quan được đánh giá, theo SRS phải xem được read-only.

### 2. Các bước tái hiện

1. Login `cb_nv_tw_02` / `Secret@123` — tạo đợt đánh giá với coQuanDuocDanhGiaId=STP-AG; walk LKH→PC→THUC_HIEN→DANG_DANH_GIA→DA_DANH_GIA→CHO_PHE_DUYET.
2. Login `cb_pd_tw_01` / `Secret@123` — phê duyệt báo cáo BCDG-20260513-0002. Đợt chuyển HOAN_THANH (verify GET `/api/v1/ke-hoach-danh-gias/{id}` trả `trangThai=HOAN_THANH` + `coQuanDuocDanhGiaId=00000000-0000-4000-8002-000000000006`).
3. Login `cb_nv_dp_01` / `Secret@123` (STP-AG, `donViId=00000000-0000-4000-8002-000000000006`).
4. Mở danh sách kế hoạch đánh giá `/danh-gia/ke-hoach/danh-sach` — danh sách chỉ render 3 đợt do STP-AG sở hữu (KHDG-HDSD-AG-001/002/003), KHÔNG có DG-20260513-0001.
5. Gọi trực tiếp `GET /api/v1/ke-hoach-danh-gias/{id}` với id đợt trên.
6. Gọi trực tiếp `GET /api/v1/ke-hoach-danh-gias/{id}/bao-cao` và `/ket-quas`.

### 3. Kết quả mong đợi (theo SRS)

SRS `srs-update-2026-5-5/srs-fr-08-danh-gia.md`:
- Line 763: "Tác nhân: CB NV (thuộc co_quan_duoc_danh_gia_id)".
- Line 766: "User đã đăng nhập, thuộc cơ quan được đánh giá".
- Line 777 (Processing Bước 1, BR-AUTH-01): "Kiểm tra user thuộc co_quan_duoc_danh_gia_id".
- Line 790 (AC): "Given CB NV thuộc cơ quan được ĐG When truy cập KH đã hoàn thành Then xem được KQ read-only".
- Line 786 (E1, ERR-DG-10): khi user **KHÔNG** thuộc cơ quan được ĐG mới trả "Bạn không có quyền xem kết quả đánh giá này".

Vậy với cb_nv_dp_01 thuộc đúng STP-AG = coQuanDuocDanhGiaId, BE phải cho phép GET detail + bao-cao + ket-quas + render dữ liệu read-only ở tab Báo cáo (không có button edit/submit).

### 4. Kết quả thực tế

- Danh sách `/api/v1/ke-hoach-danh-gias?page=1&pageSize=20` trả 3 đợt của STP-AG, không có DG-20260513-0001 (BE filter theo donViSoHuu).
- `GET /api/v1/ke-hoach-danh-gias/440b6dd1-d086-41d6-a842-45d2a323c94a` → HTTP 403, body:
  ```json
  {"code":"ERR-AUTH-VPD-00-02","message":"Đơn vị không nằm trong phạm vi truy cập của bạn"}
  ```
- `GET .../bao-cao` và `.../ket-quas` cùng trả 403 ERR-AUTH-VPD-00-02.
- `GET /api/v1/auth/me` xác nhận user thuộc `donViId=00000000-0000-4000-8002-000000000006` = STP-AG = đúng `coQuanDuocDanhGiaId` của đợt.

Hành vi đang gate theo VPD (vùng phạm vi dữ liệu) của donVi sở hữu kế hoạch (BTP-TW), bỏ qua hoàn toàn quy tắc match `co_quan_duoc_danh_gia_id` quy định trong SRS BR-AUTH-01 FR-VI-10. Mã lỗi cũng không đúng — SRS quy định ERR-DG-10, BE trả ERR-AUTH-VPD-00-02 (chung của VPD).

### 5. Bằng chứng

- Screenshot danh sách cb_nv_dp_01 STP-AG không thấy DG-20260513-0001: [image/r22-d2b-tc1-cbnvdp01-stpag-not-see.png](image/r22-d2b-tc1-cbnvdp01-stpag-not-see.png)
- Screenshot seed HOAN_THANH thành công (cb_pd_tw_01 sau approve BC): [../../workflow/danh-gia/image/r22-d2b-seed-hoanthanh-cbpdtw01.png](../../workflow/danh-gia/image/r22-d2b-seed-hoanthanh-cbpdtw01.png)
- API response 403 ERR-AUTH-VPD-00-02 (quote line 4 mục 4 ở trên — captured 2026-05-13 16:15:56 timestamp từ response).

### 6. So sánh (Permission matrix)

| Account | Vai trò | donVi | coQuanDuocDanhGiaId của đợt | Hành vi mong đợi theo SRS | Hành vi thực tế |
|---|---|---|---|---|---|
| cb_nv_dp_01 | CB_NV_DP | STP-AG | STP-AG (match) | VIEW read-only OK | ❌ 403 ERR-AUTH-VPD-00-02 |
| cb_nv_dp_02 | CB_NV_DP | STP-BG | STP-AG (≠) | DENY với ERR-DG-10 | ⚠️ 403 ERR-AUTH-VPD-00-02 (deny đúng nhưng error code mismatch SRS line 786) |
