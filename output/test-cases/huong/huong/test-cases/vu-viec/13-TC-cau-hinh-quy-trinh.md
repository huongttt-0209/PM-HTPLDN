# Test Cases — UC mới: Cấu hình Quy trình hỗ trợ TVPLDN (FR-V.I-NEW-01)

> **SRS Ref**: FR-V.I-NEW-01 (srs-fr-05:1231-1284), Entity CAU_HINH_QUY_TRINH (referenced — srs-fr-05:1943)
> **Ngày tạo**: 2026-05-06 (BMAD A3) · **A7 filter applied**: 2026-05-06
> **Tài khoản chính**: `qtht_01` (QTHT — quyền cấu hình hệ thống), `cb_nv_tw_01` (negative — non-QTHT verify 403)
> **A7 note**: SRS chưa spec SCR-ID cụ thể cho NEW-01 — giả định reuse SCR QTHT generic (tab "Cấu hình quy trình" trong module QTHT chung). URL placeholder `/qtht/cau-hinh-quy-trinh` (verify Phase B). Mark **SPEC-CLARIFY-VV-NEW-01**.

---

## A. UI FIELD VERIFICATION

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-CFQT-UI-01 | FR-V.I-NEW-01 / SCR cấu hình quy trình | Verify form CRUD bước quy trình: 5 field (ten_buoc, thu_tu, sla_ngay, dieu_kien_chuyen, mo_ta) | `qtht_01`. Login → vào "QTHT > Cấu hình Quy trình hỗ trợ TVPLDN" (URL placeholder). | — | 1. Click [+ Thêm bước]. 2. Quan sát form modal. | **UI**: Modal form 5 field theo srs-fr-05:1248-1253: (1) `ten_buoc` text bắt buộc; (2) `thu_tu` number bắt buộc; (3) `sla_ngay` number không bắt buộc — placeholder "Ngày làm việc"; (4) `dieu_kien_chuyen` textarea long không bắt buộc; (5) `mo_ta` textarea long không bắt buộc. Footer 2 nút [Hủy] [Lưu]. **SPEC-CLARIFY-VV-NEW-01**: SRS không spec UI design cụ thể, verify Phase B. | Happy | P1 |
| TC-VV-CFQT-UI-02 | FR-V.I-NEW-01 / DS bước quy trình | Verify DS bước quy trình hiển thị sort theo thu_tu ASC | `qtht_01`. Có ≥3 bước cấu hình sẵn. | — | 1. Vào "Cấu hình Quy trình". | **UI**: Bảng hiển thị các bước sort theo `thu_tu` ASC (bước 1, 2, 3...). Cột: thu_tu / ten_buoc / sla_ngay / dieu_kien_chuyen (rút gọn ≤80 + tooltip) / mo_ta (rút gọn) / [Sửa] [Xóa] / phiên bản (versioning indicator). | Happy | P1 |

---

## B. CRUD HAPPY PATH

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-CFQT-101 | FR-V.I-NEW-01 AC1 + AC2 / Processing B2 | Thêm bước quy trình mới với đủ field bắt buộc | `qtht_01`. Hiện có 5 bước (thu_tu 1-5). | ten_buoc="Bước rà soát chéo", thu_tu=6, sla_ngay=2, dieu_kien_chuyen="Hoàn tất bước 5", mo_ta="Rà soát chéo trước khi đóng VV" | 1. Click [+ Thêm bước]. 2. Fill 5 field. 3. Click [Lưu]. | **STATE**: Backend (1) verify quyền QTHT (BR-AUTH-01); (2) check thu_tu=6 chưa tồn tại; (3) INSERT CAU_HINH_QUY_TRINH với version='current'. **UI**: Modal đóng. Toast success "Đã thêm bước quy trình mới". Bảng reload, dòng mới ở vị trí thu_tu=6. **PERSIST**: AUDIT_LOG action='CREATE_QUY_TRINH' (BR-DATA-05 srs-fr-05:1264). | Happy | P0 |
| TC-VV-CFQT-102 | FR-V.I-NEW-01 / UPDATE | Sửa bước quy trình — đổi sla_ngay + mo_ta | `qtht_01`. Bước "Phân công NHT/TVV" thu_tu=3, sla_ngay=3. | sla_ngay=5, mo_ta="Cập nhật mở rộng SLA" | 1. Click [Sửa] dòng bước 3. 2. Update sla_ngay + mo_ta. 3. [Lưu]. | **STATE**: Backend UPDATE CAU_HINH_QUY_TRINH SET sla_ngay=5, mo_ta=..., updated_at=NOW(), updated_by=qtht_01.id, **version mới** (versioning). **UI**: Toast success. Bảng reload sla_ngay=5. **PERSIST**: AUDIT_LOG UPDATE. **CRITICAL**: Per srs-fr-05:1262 "HS mới: áp dụng quy trình mới, HS cũ: giữ quy trình cũ". Verify VV cũ (đã DA_PHAN_CONG trước update) vẫn dùng SLA cũ = 3 ngày — không bị thay đổi backwards. | Happy | P0 |
| TC-VV-CFQT-103 | FR-V.I-NEW-01 / Versioning isolation | VV mới sau update apply quy trình mới, VV cũ giữ quy trình cũ | `qtht_01` đã thực hiện TC-VV-CFQT-102 (đổi sla_ngay 3→5). Có VV-OLD tạo trước update + VV-NEW tạo sau. | — | 1. Tạo VV-NEW sau khi cập nhật bước 3. 2. Mở VV-OLD và VV-NEW. 3. So sánh deadline phân công. | **STATE**: Backend gắn VV.process_version snapshot tại thời điểm tạo (giả định — **SPEC-CLARIFY-VV-NEW-02**). VV-OLD reference version cũ (sla_ngay=3), VV-NEW reference version mới (sla_ngay=5). **UI**: Trong SCR-V.I-03 hoặc audit field, có thể hiển thị "Quy trình áp dụng: v{N}". Deadline phân công VV-NEW = 5 ngày từ ngày kiểm tra; VV-OLD = 3 ngày. **PERSIST**: 2 versions của bước 3 trong CAU_HINH_QUY_TRINH (active + archived). | Happy | P0 |
| TC-VV-CFQT-104 | FR-V.I-NEW-01 / DELETE | Xóa bước quy trình (chưa có VV active sử dụng) | `qtht_01`. Bước "Bước rà soát chéo" thu_tu=6 (vừa tạo TC-VV-CFQT-101) chưa có VV nào reference. | — | 1. Click [Xóa] dòng bước 6. 2. Confirm modal. | **STATE**: Backend (1) check NO active VV reference bước này; (2) soft delete is_deleted=1. **UI**: Toast success "Đã xóa bước quy trình". Hàng biến mất. **PERSIST**: AUDIT_LOG DELETE. | Happy | P1 |

---

## C. NEGATIVE — VALIDATION ERRORS

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-CFQT-201 | ERR-QT-01 / Thứ tự trùng | Thêm bước với thu_tu=3 (đã tồn tại) | `qtht_01`. Hiện đã có bước thu_tu=3 ("Phân công NHT/TVV"). | ten_buoc="Bước test trùng", thu_tu=3 | 1. Click [+ Thêm]. 2. Fill thu_tu=3. 3. [Lưu]. | **STATE**: Backend reject với ERR-QT-01 (srs-fr-05:1276). **UI**: Toast error nguyên văn "Thứ tự bước đã tồn tại". Form giữ data. Suggest user đổi thu_tu. **PERSIST**: KHÔNG có INSERT. | Negative | P0 |
| TC-VV-CFQT-202 | ERR-QT-02 / Tên trống | Thêm bước với ten_buoc="" | `qtht_01`. | ten_buoc="", thu_tu=10 | 1. Click [+ Thêm]. 2. Để trống ten_buoc. 3. Fill thu_tu=10. 4. [Lưu]. | **STATE**: Backend reject ERR-QT-02 (srs-fr-05:1277). **UI**: Hoặc client validate (border đỏ + helper "Tên bước quy trình là bắt buộc"); hoặc submit → toast error nguyên văn "Tên bước quy trình là bắt buộc". **PERSIST**: KHÔNG có INSERT. | Negative | P0 |
| TC-VV-CFQT-203 | BR-AUTH-01 / Permission | CB NV (non-QTHT) truy cập SCR cấu hình quy trình | `cb_nv_tw_01`. | — | 1. Login `cb_nv_tw_01`. 2. Truy cập URL `/qtht/cau-hinh-quy-trinh`. | **STATE**: Backend reject 403 (BR-AUTH-01 srs-fr-05:1260, NEW-01 PRE-02 "User có quyền QTHT" srs-fr-05:1244). **UI**: 403 page hoặc redirect dashboard với toast "Bạn không có quyền thực hiện thao tác này" (srs-fr-05:1619). **PERSIST**: AUDIT_LOG ATTEMPT_403. | Negative | P0 |

---

## D. EDGE CASES

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước | Kết quả mong đợi | Type | Priority |
|----|---------|--------------|----------------|-----------|----------|------------------|------|----------|
| TC-VV-CFQT-301 | FR-V.I-NEW-01 / Cascade VV active | Xóa bước quy trình đang được VV active reference → reject hoặc warning | `qtht_01`. Bước "Phân công NHT/TVV" thu_tu=3 có ≥5 VV đang DA_PHAN_CONG/DANG_XU_LY reference. | — | 1. Click [Xóa] dòng bước 3. | **STATE**: Backend reject (FK constraint hoặc business rule) — chỉ cho xóa nếu KHÔNG có VV active reference. **UI**: Toast error "Không thể xóa bước đang được sử dụng bởi 5 vụ việc đang xử lý" (SRS Gap exact message — mark **SPEC-CLARIFY-VV-NEW-03**). **PERSIST**: KHÔNG có DELETE. | Edge | P0 |
| TC-VV-CFQT-302 | BR-EC-01 / Optimistic lock concurrent | 2 QTHT cùng sửa bước quy trình | Tab1 `qtht_01` + Tab2 `qtht_02` (giả lập — CSV chỉ có 1 QTHT, **SPEC-CLARIFY-VV-NEW-04**). Bước thu_tu=3. | Tab1 sla_ngay=4, Tab2 sla_ngay=6 | 1. Tab1 [Lưu]. 2. Tab2 [Lưu] (chưa reload). | **STATE**: Tab1 SUCCESS. Tab2 FAIL với optimistic lock conflict (BR-EC-01). **UI**: Tab1 toast success. Tab2 modal "Bước quy trình đã được {qtht_01} cập nhật. Vui lòng tải lại." + nút [Tải lại]. **PERSIST**: 1 entry UPDATE. | Edge | P1 |

---

## Tổng kết file

**Tổng TC: 11** (2 UI + 4 Happy + 3 Negative + 2 Edge) — ổn định sau Codex review 2026-05-09

**Priority**: P0=8 / P1=3 / P2=0

**Coverage:**
- BR: BR-AUTH-01 (QTHT only — TC-203), BR-DATA-05 (audit), BR-EC-01 (optimistic lock — TC-302)
- Error codes: ERR-QT-01, ERR-QT-02 (**full 2/2**)
- AC SRS: 3/3 (srs-fr-05:1280-1282) — bước thêm/sửa/áp dụng versioning
- **Versioning isolation test (TC-103)**: HS mới apply mới, HS cũ giữ (srs-fr-05:1262-1263) — verify deadline render khác giữa VV-OLD vs VV-NEW
- Cascade FK (TC-301): xóa bước đang reference → reject

**SPEC-CLARIFY:**
- **VV-NEW-01**: SCR-ID cụ thể cho NEW-01 — SRS không spec UI design rõ ràng. Phase B verify URL pattern + form layout
- **VV-NEW-02**: Versioning mechanism — VV gắn process_version snapshot tại thời điểm tạo? hay reference current via FK + audit version field? — implementation detail cần BA confirm
- **VV-NEW-03**: Message reject xóa bước active — SRS không quote nguyên văn
- **VV-NEW-04**: CSV chỉ có 1 user QTHT (`qtht_01`) — concurrent test cần seed thêm `qtht_02` hoặc dùng single-user multi-session

**Lưu ý A7:**
- File này có 2 TC liên quan tới versioning (TC-VV-CFQT-102 + TC-VV-CFQT-103) — verify qua UI deadline thay đổi giữa VV cũ vs mới (UI bridge OK).
- KHÔNG có TC chỉ-DB query (versioning verify gián tiếp qua deadline UI render).
- Cascade FK (TC-VV-CFQT-301) verify qua UI toast error, không cần DB inspect.

> **Codex review 2026-05-09:**
> - File coverage đã đầy đủ — KHÔNG thêm TC mới. UC NEW-01 scope nhỏ (cấu hình QTHT), 11 TC đã cover 100% AC + ERR + critical versioning isolation
> - TC-103 (versioning isolation) là TC quan trọng nhất file — verify quy trình mới KHÔNG ảnh hưởng VV cũ (regression risk khi BA đổi cấu hình)
