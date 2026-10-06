# Test Cases — Tab "Lịch học & Điểm danh" + Auto-transition KHOA_HOC theo ngày (SCR-III-02)

> **SRS Ref**: SCR-III-02 Tab 3 (`02-thu-tu-module.md` §⑨ dòng 599) — `KET_QUA_DAO_TAO WHERE khoa_hoc_id=<current>`. Cấu trúc buổi học (slot) trong khoảng `KHOA_HOC.ngay_bat_dau..ngay_ket_thuc`. Auto-transition `DA_CONG_KHAI → DANG_DIEN_RA` khi đến `ngay_bat_dau`, `DANG_DIEN_RA → DA_KET_THUC` khi qua `ngay_ket_thuc` (SM-KHOAHOC dòng 625, 627). Edit-rule: chỉ cho sửa Tab Lịch học & Điểm danh khi KH ở `DANG_DIEN_RA` (SRS dòng 599).
> **Nguồn**: SRS local `srs-fr-03-dao-tao.md` dòng 412-498 (FR-III-05 KQ workflow) + `02-thu-tu-module.md` §⑨ dòng 599, 625-627 + Plan overview §2.2.
> **Ngày tạo**: 2026-05-09 (Phase A re-run)
> **Phạm vi tài khoản**: cb_nv_tw_01 (CRUD buổi học scope TW), cb_pd_tw_01 (read-only audit), system cron (auto-transition).

---

## A. UI VERIFICATION (Tab "Lịch học & Điểm danh" trong SCR-III-02)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-H-001 | FR-III-05 / SCR-III-02 Tab 3 / UI | Verify Tab "Lịch học & Điểm danh" — layout + toolbar khi KH `DANG_DIEN_RA` | CB_NV_TW (cb_nv_tw_01) đăng nhập. KH "KH-20260601-001" trạng thái `DANG_DIEN_RA`, `ngay_bat_dau=2026-06-01`, `ngay_ket_thuc=2026-06-30`, có 3 buổi học đã cấu hình. ≥3 HV `DANG_KY_DAO_TAO.trang_thai='DA_DUYET'`. | URL: `/dao-tao/khoa-hoc/{kh_id}` — chọn Tab "Lịch học & Điểm danh" | 1. Đăng nhập CB_NV_TW. 2. Vào SCR-III-01, expand CTĐT, click row KH-20260601-001. 3. Click Tab "Lịch học & Điểm danh". | **STATE**: Backend `GET /api/v1/khoa-hoc/{kh_id}/buoi-hoc` + `GET /api/v1/khoa-hoc/{kh_id}/diem-danh`. **UI**: Tab "Lịch học & Điểm danh" active. Sub-section 1 — "Lịch học" (toolbar [+ Thêm buổi học] [Import Excel lịch] enabled vì KH `DANG_DIEN_RA`). Bảng buổi học cột: STT, Ngày học (dd/mm/yyyy), Khung giờ (HH:mm-HH:mm), Địa điểm/Link Zoom, Giảng viên, Hành động (Sửa/Xóa). Sub-section 2 — "Điểm danh từng buổi" — bảng matrix: rows=HV, columns=các buổi, cell=checkbox Có mặt/Vắng mặt. Cột cuối "Tỷ lệ chuyên cần" (% auto-tính). **PERSIST**: Reload tab → đúng dữ liệu seed. | Happy 🔴 |
| TC-LICH-H-002 | FR-III-05 / SCR-III-02 Tab 3 / Edit-rule | Tab "Lịch học & Điểm danh" — read-only khi KH `DA_CONG_KHAI` (chưa bắt đầu) | CB_NV_TW. KH "KH-20260701-001" `DA_CONG_KHAI`, `ngay_bat_dau=2026-07-01` (future). | — | 1. Vào Tab Lịch học. | **STATE**: — (read-only). **UI**: Per SRS dòng 599 "Chỉ cho sửa khi khóa học đang ở `DANG_DIEN_RA`". Toolbar [+ Thêm buổi học] / [Sửa] / [Xóa] **DISABLE / ẨN**. Bảng buổi học read-only. Sub-section "Điểm danh" hiển thị nhưng checkbox disabled. Hover tooltip: "Chỉ chỉnh sửa được khi khóa học đang diễn ra" (SPEC-CLARIFY-DT-12 nguyên văn). **PERSIST**: Reload — read-only state. | Happy 🟡 |

---

## B. READ — Xem lịch học theo Khóa học

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-H-003 | FR-III-05 / FR-III-06 / Filter scope | Xem danh sách buổi học của 1 KH — filter chính xác `khoa_hoc_id` | CB_NV_TW. KH "KH-20260601-001" có 5 buổi (2026-06-02, 06-09, 06-16, 06-23, 06-30). KH khác "KH-20260601-002" có 3 buổi không liên quan. | — | 1. Vào KH-20260601-001 Tab Lịch học. | **STATE**: Backend `GET /api/v1/khoa-hoc/{kh_id_001}/buoi-hoc` → 5 record với `khoa_hoc_id=kh_id_001`. **UI**: Bảng hiển thị **đúng 5 buổi** sắp xếp theo ngày tăng dần. KHÔNG có buổi của KH-002. **PERSIST**: Reload giữ. | Happy |
| TC-LICH-H-004 | FR-III-05 / SCR-III-02 / Tỷ lệ chuyên cần | Tỷ lệ chuyên cần auto-tính theo công thức (số buổi có mặt / tổng buổi) × 100% | CB_NV_TW. KH `DANG_DIEN_RA` 5 buổi đã diễn ra. HV "Nguyễn Văn A" có 4 buổi `co_mat=true`, 1 buổi `co_mat=false`. | — | 1. Vào Tab Lịch học. 2. Quan sát cột "Tỷ lệ chuyên cần" hàng HV "Nguyễn Văn A". | **STATE**: Backend tính `4/5 × 100 = 80%`. **UI**: Cột hiển thị "80%" (định dạng 1 chữ số sau dấu phẩy hoặc làm tròn — SPEC-CLARIFY-DT-13). **PERSIST**: Toggle 1 buổi từ Vắng → Có mặt → reload → tỷ lệ thành 100%. | Happy |
| TC-LICH-H-005 | FR-III-05 / Empty state | KH `DANG_DIEN_RA` chưa có buổi học cấu hình | CB_NV_TW. KH "KH-EMPTY" `DANG_DIEN_RA`, 0 buổi học. | — | 1. Vào Tab Lịch học. | **STATE**: Backend trả mảng rỗng. **UI**: Empty state "Chưa có buổi học nào — vui lòng [+ Thêm buổi học]" (SPEC-CLARIFY-DT-14 nguyên văn). Toolbar [+ Thêm buổi học] vẫn enabled. Sub-section điểm danh ẩn (không có cột). **PERSIST**: Reload. | Edge |

---

## C. CREATE — Thêm buổi học mới

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-H-006 | FR-III-05 / KET_QUA_DAO_TAO struct buổi | Thêm buổi học thành công — KH `DANG_DIEN_RA` (TRUC_TIEP) | CB_NV_TW. KH "KH-20260601-001" `DANG_DIEN_RA`, hình thức `TRUC_TIEP`, `ngay_bat_dau=2026-06-01`, `ngay_ket_thuc=2026-06-30`. | ngay_hoc="2026-06-15", gio_bat_dau="08:00", gio_ket_thuc="11:30", dia_diem="Hội trường A — 123 Lê Lợi, HCM", giang_vien_id=GV-001 | 1. Tab Lịch học → click [+ Thêm buổi học]. 2. Điền form drawer. 3. Click [Đồng ý]. | **STATE**: INSERT KET_QUA_DAO_TAO/buổi học với `khoa_hoc_id`, `ngay_hoc`, `gio_bat_dau/ket_thuc`, `dia_diem`, `giang_vien_id` (per SRS dòng 599 entity scope). 7 common fields BR-DATA-03. AUDIT_LOG: hanh_dong='CREATE', entity='BUOI_HOC' (SPEC-CLARIFY-DT-15: tên entity buổi học). **UI**: Toast "Thêm buổi học thành công" (SPEC-CLARIFY-DT-12). Drawer đóng, bảng cập nhật +1 row. **PERSIST**: Reload → buổi học hiển thị. | Happy 🔴 |
| TC-LICH-H-007 | FR-III-05 / Hình thức TRUC_TUYEN | Thêm buổi học TRUC_TUYEN — yêu cầu Link Zoom thay địa điểm | CB_NV_TW. KH `DANG_DIEN_RA`, hình thức `TRUC_TUYEN`. | ngay_hoc="2026-06-15", gio_bat_dau="14:00", gio_ket_thuc="16:00", link_zoom="https://zoom.us/j/123456789" | 1. Click [+ Thêm buổi học]. 2. Form hiển thị field "Link Zoom" thay "Địa điểm". 3. Điền + Lưu. | **STATE**: INSERT với `link_zoom`, `dia_diem=NULL` (SRS dòng 597 conditional field). **UI**: Toast OK. Bảng hiển thị link Zoom (clickable, external open). **PERSIST**: Reload — link giữ nguyên. | Happy |
| TC-LICH-H-008 | FR-III-05 / Edit-rule violation | Thêm buổi học khi KH `DA_CONG_KHAI` (chưa bắt đầu) — bị chặn | CB_NV_TW. KH `DA_CONG_KHAI`. | force API POST `/api/v1/khoa-hoc/{id}/buoi-hoc` | 1. UI: nút [+ Thêm buổi học] disable (TC-LICH-H-002). 2. Force API direct POST. | **STATE**: KHÔNG INSERT. BE check `khoa_hoc.trang_thai='DANG_DIEN_RA'` fail → 422. **UI**: Button disabled. Direct API → error "**Chỉ chỉnh sửa được khi khóa học đang diễn ra**" (SPEC-CLARIFY-DT-12). **PERSIST**: Count buổi học không đổi. | Negative 🔴 |

---

## D. UPDATE — Sửa buổi học (chỉ khi KH `DANG_DIEN_RA`)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-H-009 | FR-III-05 / SRS dòng 599 / BR-DATA-05 | Sửa buổi học — đổi giờ + địa điểm thành công | CB_NV_TW. KH `DANG_DIEN_RA`. Buổi học id=BH-001 ngay_hoc=2026-06-15, gio="08:00-11:30", dia_diem="HT A". | gio_moi="09:00-12:30", dia_diem_moi="HT B" | 1. Row BH-001 → click [Sửa]. 2. Đổi giờ + địa điểm. 3. Lưu. | **STATE**: UPDATE buổi học SET gio_bat_dau='09:00', gio_ket_thuc='12:30', dia_diem='HT B', updated_at=NOW(), updated_by=cb_nv_tw_01. AUDIT_LOG: hanh_dong='UPDATE' du_lieu_cu/du_lieu_moi (BR-DATA-05). **UI**: Toast OK. Bảng row reflect. **PERSIST**: Reload. | Happy |
| TC-LICH-H-010 | FR-III-05 / Edit-rule | Sửa buổi học khi KH `DA_KET_THUC` — bị chặn | CB_NV_TW. KH `DA_KET_THUC`. Buổi học BH-002. | API PUT | 1. UI [Sửa] disable. 2. Force API direct PUT. | **STATE**: KHÔNG UPDATE. BE reject. **UI**: Force API → error "**Chỉ chỉnh sửa được khi khóa học đang diễn ra**" (SPEC-CLARIFY-DT-12). **PERSIST**: Buổi học không đổi. | Negative 🔴 |

---

## E. DELETE — Xóa buổi học

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-H-011 | FR-III-05 / BR-DATA-01 | Xóa mềm buổi học — KH `DANG_DIEN_RA`, chưa có điểm danh | CB_NV_TW. KH `DANG_DIEN_RA`. Buổi học BH-003 chưa có row điểm danh. | — | 1. Row BH-003 → click [Xóa]. 2. Confirm. | **STATE**: UPDATE buổi học SET is_deleted=1, deleted_at=NOW(), deleted_by=cb_nv_tw_01 (BR-DATA-01). AUDIT_LOG: hanh_dong='DELETE'. **UI**: Toast "Xóa buổi học thành công" (SPEC-CLARIFY-DT-12). Row biến mất. **PERSIST**: Reload — row ẩn. | Happy |
| TC-LICH-H-012 | FR-III-05 / Edge / SPEC-CLARIFY-DT-16 | Xóa buổi học đã có điểm danh — định nghĩa hành vi | CB_NV_TW. Buổi học BH-004 có 5 row điểm danh. | — | 1. Click [Xóa] BH-004. 2. Confirm. | **STATE**: SPEC-CLARIFY-DT-16: SRS dòng 599 không quy định guard. Hành vi mặc định: cảnh báo "Buổi học có {N} điểm danh — xác nhận xóa sẽ xóa luôn dữ liệu điểm danh?" → nếu confirm: cascade soft-delete điểm danh con. **UI**: Modal confirm 2-tier. **PERSIST**: Sau confirm → buổi + điểm danh đều `is_deleted=1`. | Edge 🟡 |

---

## F. AUTO-TRANSITION (Time-driven cron job — SM-KHOAHOC dòng 625, 627)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-S-013 | 🟠 DEFER (A7) FR-III-05 / SM-KHOAHOC dòng 625 / AT time-driven | Auto-transition `DA_CONG_KHAI → DANG_DIEN_RA` khi đến `ngay_bat_dau` | KH "KH-AUTO-001" `DA_CONG_KHAI`, `ngay_bat_dau` sẵn để env auto-tick (seed với ngày BĐ = NOW()-5min). Cron `transition-khoa-hoc` chạy mỗi 5 phút (SPEC-CLARIFY-DT-17 tần suất). | KH có ngay_bat_dau ≤ NOW() | 1. Seed KH với ngay_bat_dau ≤ NOW(). 2. Đợi cron tick (5 phút). 3. Vào SCR-III-02. 4. Verify badge + network `GET /api/v1/khoa-hoc/{id}`. | **STATE**: Cron query `WHERE trang_thai='DA_CONG_KHAI' AND ngay_bat_dau <= NOW()` → UPDATE SET trang_thai='DANG_DIEN_RA'. **UI**: SCR-III-02 badge "Đang diễn ra" (vàng). Tab Lịch học toolbar enable (per TC-LICH-H-001). Network response field `trang_thai='DANG_DIEN_RA'`. **PERSIST**: Reload — DANG_DIEN_RA. | Happy 🔴 (DEFER A7) |
| TC-LICH-S-014 | 🟠 DEFER (A7) FR-III-05 / SM-KHOAHOC dòng 627 / AT time-driven | Auto-transition `DANG_DIEN_RA → DA_KET_THUC` khi qua `ngay_ket_thuc` | KH "KH-AUTO-002" `DANG_DIEN_RA`, `ngay_ket_thuc` ≤ NOW()-5min (seed với date đã qua). | KH có ngay_ket_thuc < NOW() | 1. Seed KH state DANG_DIEN_RA với ngay_ket_thuc < NOW(). 2. Đợi cron tick. 3. Vào SCR-III-02. | **STATE**: Cron query `WHERE trang_thai='DANG_DIEN_RA' AND ngay_ket_thuc < NOW()` → UPDATE SET trang_thai='DA_KET_THUC'. **UI**: Badge "Đã kết thúc" (xám). Tab Lịch học → read-only. Tab "KQ kiểm tra" enable nhập (SRS dòng 600). Network `GET /api/v1/khoa-hoc/{id}` trả `trang_thai='DA_KET_THUC'`. **PERSIST**: Reload. | Happy 🔴 (DEFER A7) |
| TC-LICH-S-015 | 🟠 DEFER (A7) FR-III-05 / AT idempotency | Cron chạy 2 lần liên tiếp — KH đã `DANG_DIEN_RA` không bị transition lại | KH "KH-AUTO-003" `DANG_DIEN_RA` từ tick trước (đã observe AUTO_TRANSITION ở TC-LICH-S-013). | 2 lần cron tick liên tiếp 5 phút | 1. Sau khi KH chuyển DANG_DIEN_RA, đợi tick thứ 2. 2. Verify FR-10 audit log UI → vẫn chỉ 1 entry AUTO_TRANSITION cho KH-AUTO-003. | **STATE**: Cron query `trang_thai='DA_CONG_KHAI' AND ngay_bat_dau <= NOW()` — KH đã DANG_DIEN_RA nên không match → không UPDATE. **UI**: Badge giữ nguyên. FR-10 audit log lookup theo entity_id → 1 entry AUTO_TRANSITION (idempotent — SPEC-CLARIFY-DT-19). **PERSIST**: 1 entry. | Edge 🟡 (DEFER A7) |

---

## G. NEGATIVE / EDGE — Buổi học ngoài khoảng KH + trùng giờ

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-N-016 | FR-III-05 / Boundary `ngay_bat_dau..ngay_ket_thuc` | Thêm buổi học `ngay_hoc` < KH.ngay_bat_dau — bị chặn | CB_NV_TW. KH `DANG_DIEN_RA`, ngay_bat_dau=2026-06-01, ngay_ket_thuc=2026-06-30. | ngay_hoc="2026-05-31" (1 ngày trước BĐ) | 1. Form thêm buổi. 2. ngay_hoc=2026-05-31. 3. Lưu. | **STATE**: KHÔNG INSERT. BE check `ngay_hoc BETWEEN khoa_hoc.ngay_bat_dau AND khoa_hoc.ngay_ket_thuc` fail. **UI**: Inline error "**Ngày buổi học phải nằm trong khoảng ngày học của khóa**" (SPEC-CLARIFY-DT-20 nguyên văn). **PERSIST**: Count không đổi. | Negative 🔴 |

---

## H. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-LICH-S-017 | FR-III-05 / SM dòng 625 / State race | Race: AT cron tick + CB NV manual [Bắt đầu] cùng lúc | cb_nv_tw_01. KH "KH-RACE-001" `DA_CONG_KHAI`, `ngay_bat_dau=NOW()`. Cron và CB NV trigger đồng thời. | Cron + manual click cùng moment | 1. Setup mock cron tick. 2. Đồng thời cb_nv_tw_01 click [Bắt đầu]. 3. Query AUDIT_LOG. | **STATE**: BE phải dùng row-lock hoặc CAS update — UPDATE chỉ 1 lần. AUDIT_LOG chỉ 1 entry transition (actor=SYSTEM hoặc cb_nv_tw_01 — first wins). **UI**: 1 toast OK; lần 2 → idempotent no-op. **PERSIST**: DANG_DIEN_RA. SPEC-CLARIFY-DT-EC-04: actor convention khi race với SYSTEM. | Edge 🔴 |
| TC-LICH-N-019 | FR-III-05 / Boundary buổi học trùng giờ | Thêm 2 buổi học cùng ngày + overlap giờ — verify rule overlap | cb_nv_tw_01. KH `DANG_DIEN_RA`. Buổi A: 2026-06-15 08:00-11:30, GV-001. | Thêm buổi B: 2026-06-15 09:00-12:00, GV-001 | 1. Buổi A đã có. 2. Form thêm buổi B với GV trùng + giờ overlap. 3. Lưu. | **STATE**: SRS không quote rule overlap GV. SPEC-CLARIFY-DT-EC-06: BE check overlap `(buổi B.start < buổi A.end AND buổi B.end > buổi A.start) AND giang_vien_id=GV-001` reject hay allow? Default: reject với message "GV đã có buổi học khác trong khung giờ này". **UI**: Inline/toast error. **PERSIST**: Count buổi học không đổi (nếu reject). | Negative 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| ID | Mô tả |
|----|-------|
| SPEC-CLARIFY-DT-12 | Toast/error message nguyên văn cho CRUD buổi học (success + edit-rule violation) — SRS FR-III-05 không có Error Handling table riêng cho Tab Lịch học. |
| SPEC-CLARIFY-DT-EC-04 | Race AT cron + manual trigger — actor convention trong AUDIT_LOG khi cả 2 đồng thời. |
| SPEC-CLARIFY-DT-EC-05 | Timezone convention — SRS không quote. Default UTC store + compare. Cần BA confirm cho display + cron logic. |
| SPEC-CLARIFY-DT-EC-06 | Rule overlap buổi học cùng GV cùng giờ — SRS không quote. Default reject. |
| SPEC-CLARIFY-DT-13 | Format hiển thị "Tỷ lệ chuyên cần" — số nguyên (80%) hay 1 chữ số sau dấu phẩy (80.0%) — SRS dòng 599 không quy định. |
| SPEC-CLARIFY-DT-14 | Empty state message khi KH chưa có buổi học — SRS không có nguyên văn. |
| SPEC-CLARIFY-DT-15 | Tên entity cho "buổi học" — SRS dòng 599 dùng `KET_QUA_DAO_TAO` cho điểm danh nhưng struct buổi học (slot ngày + giờ + địa điểm) chưa có entity riêng quy định. Có phải là `BUOI_HOC` con của `KHOA_HOC`? |
| SPEC-CLARIFY-DT-16 | Hành vi xóa buổi học đã có điểm danh — SRS không quy định guard / cascade. Mặc định cảnh báo + cascade soft-delete. |
| SPEC-CLARIFY-DT-17 | Tần suất cron job auto-transition KH theo ngày — SRS không quy định (5 phút / 15 phút / hourly). Ảnh hưởng độ trễ chuyển trạng thái. |
| SPEC-CLARIFY-DT-18 | Actor convention trong AUDIT_LOG cho auto-transition — `SYSTEM` / `CRON` / `null` — chưa quy định. |
| SPEC-CLARIFY-DT-19 | Idempotency cron transition — SRS không quy định. Test giả định BE đã idempotent (WHERE clause filter state đúng). |
| SPEC-CLARIFY-DT-20 | Validation rule "buổi học nằm trong khoảng ngày KH" — SRS dòng 599 ngầm định nhưng không có error code/message nguyên văn. |

---

## Tổng kết file 04

- **18 TC active sau A7** (16H/N/S/Edge giữ + 3 DEFER cron + LOẠI 1 timezone) phủ Tab Lịch học & Điểm danh + AT time-driven.
- **9 SPEC-CLARIFY** raise pending BA: DT-12 → DT-20.
- **BR coverage:** BR-DATA-01 (soft-delete), BR-DATA-03 (common fields), BR-DATA-05 (audit), edit-rule SRS dòng 599.
- **SM coverage:** AT-driven `DA_CONG_KHAI → DANG_DIEN_RA` (TC-013 DEFER) và `DANG_DIEN_RA → DA_KET_THUC` (TC-014 DEFER). Idempotency (TC-015 DEFER).
- **Cross-ref FILE 05:** AT-01/AT-02 (manual trigger) test ở 05-TC-khoa-hoc-quan-ly.md section F.

---

## A7 Filter Notes

- **LOẠI:** TC-LICH-S-018 (Timezone — cần DB server TZ control, env không support test override) — replaced bằng assumption "BE store UTC + compare UTC" + DEFER follow-up production.
- **DEFER (A7):** TC-LICH-S-013, TC-LICH-S-014, TC-LICH-S-015 — cron auto-transition cần đợi tick 5 phút trong env smoke (no admin trigger endpoint exposed). SỬA observability từ "Query DB AUDIT_LOG" → "FR-10 audit log UI lookup theo entity_id" + network response trả trang_thai. Test trong Phase B chỉ chạy nếu seed time đã expire HOẶC FR-10 audit screen ready.
