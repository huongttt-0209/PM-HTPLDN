# Functional Test Report — R7.7.4.6 — Tổ chức tư vấn

**Ngày chạy:** 2026-05-09 02:21:00 → 02:42:30
**Verdict:** ⚠️ **8/10 PASS · 1 ⚠️ Sai spec FE (Minor) · 1 ❌ FAIL Critical** — pool TC TV còn 8 HOAT_DONG (giảm 1 do bug QTHT bypass DELETE).
**Accounts:** `cb_nv_tw_02` · `cb_pd_tw_02` · `cb_nv_dp_01` (AG) · `qtht_01` — isolated MCP context per role.
**Spec:** `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md` FR-IV-NEW-01..04 + permission-matrix v3.5 update 2026-05-05/2026-05-09.
**Method:** Chrome DevTools MCP — UI click chain + `evaluate_script` cho probe API authz.

## Kết quả tổng quan

| TC | Mô tả | Account | Endpoint key | Verdict |
|:-:|---|---|---|:-:|
| TC-001 | Read list 9 record + filter Loại hình | cb_nv_tw_02 | GET `/to-chuc-tu-vans` | ✅ Đạt |
| TC-002 | BR-AUTH-08 — CB NV ĐP tạo scope đơn vị | cb_nv_dp_01 | POST `/to-chuc-tu-vans` 201 | ✅ Đạt |
| TC-003 | Negative thiếu LV → FE block | cb_nv_dp_01 | (FE block, no POST) | ✅ Đạt |
| TC-004 | Negative email sai format → FE block | cb_nv_dp_01 | (FE block, no POST) | ✅ Đạt |
| TC-006 | Xuất Excel | cb_nv_tw_02 | POST `/to-chuc-tu-vans/export` 200 | ✅ Đạt |
| TC-010 | BR-AUTH-05/BR-FLOW-03 — TW PD không duyệt DP record | cb_pd_tw_02 | POST `/.../phe-duyet` **403** | ⚠️ **Sai spec FE** — BE block đúng, FE vẫn render [Phê duyệt]/[Từ chối] cross-cấp |
| TC-017 | Công khai 0→1 (modal mô tả) | cb_nv_tw_02 | POST `/.../cong-khai` 200 | ✅ Đạt |
| TC-018 | Hủy công khai 1→0 (toggle direct) | cb_nv_tw_02 | POST `/.../cong-khai` 200 | ✅ Đạt |
| TC-022 | QTHT R-only — POST/PATCH/DELETE phải 403 | qtht_01 | DELETE **204** | ❌ **Lỗi Critical** — QTHT DELETE thành công xóa record |
| TC-025 | Edit junction LV (2→3 LV) | cb_nv_tw_02 | PATCH `/to-chuc-tu-vans/{id}` 200 | ✅ Đạt |

## Chi tiết test

### TC-001 — Read list 9 record + filter Loại hình

- GET `/api/v1/to-chuc-tu-vans?page=1&pageSize=20&trangThai=HOAT_DONG` 200 → render 9 records (TC-BTP-TW-0001..0009).
- Click combobox "Loại hình" → 4 option (Công ty Luật / Văn phòng Luật sư / Trung tâm TVPL / Khác).
- Chọn "Văn phòng Luật sư" → URL `?loaiHinh=VP_LUAT_SU&page=1` → list filter còn 3 records (TC-0002 Beta + TC-0004 Đoàn LS HN + TC-0007 Iota R8) — đúng filter.
- Tab structure verified: 6 tabs (Đang hoạt động [9] · Chờ phê duyệt · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa).
- Evidence: [r7-7-4-6-tc01-list-filter-vplsu.png](image/r7-7-4-6-tc01-list-filter-vplsu.png).

### TC-002 — BR-AUTH-08 cb_nv_dp create scope

- cb_nv_dp_01 (Sở TP An Giang) tạo TC TV với form đầy đủ (Tên: "Cong ty Luat AG R7746", LV: Thuế).
- POST `/api/v1/to-chuc-tu-vans` 201 → BE auto-set `donViId` theo user.
- Detail page: **mã `TC-STP-AG-0001`** (prefix STP-AG khác hẳn TW prefix `TC-BTP-TW-*`). Trạng thái MOI_DANG_KY initial.
- BR-AUTH-08 scope verified — đúng spec FR-IV-NEW-01 step 5.
- Evidence: [r7-7-4-6-tc02-create-stp-ag.png](image/r7-7-4-6-tc02-create-stp-ag.png).

### TC-003 — Negative thiếu LV

- Form fill đủ trường BẮT BUỘC (Tên/Loại hình/Người đại diện/Số DKHĐ/Ngày cấp/Địa chỉ) **trừ Lĩnh vực**.
- Click [Tạo mới] → FE message inline `"Chọn ít nhất 1 lĩnh vực"` hiện dưới combobox LV. KHÔNG có POST request.
- Đúng spec ERR-TCTV-06 ("Phải chọn ≥1 lĩnh vực") — FE block client-side.
- Evidence: [r7-7-4-6-tc03-thieu-lv.png](image/r7-7-4-6-tc03-thieu-lv.png).

### TC-004 — Negative email sai format

- Email = `"invalid-email-format"` (no `@`) → FE message inline `"Email không phải kiểu email hợp lệ"` hiện ngay khi blur input.
- Đúng spec ERR-TCTV-07 (Email sai format) — FE block client-side, không gửi POST.
- Evidence: [r7-7-4-6-tc04-email-invalid.png](image/r7-7-4-6-tc04-email-invalid.png).

### TC-006 — Xuất Excel

- cb_nv_tw_02 click [Xuất Excel] trên list (filter Đang hoạt động).
- POST `/api/v1/to-chuc-tu-vans/export` 200 OK.
- Đúng spec FR-IV-NEW-01 step "CB NV xuất DS" + Phụ lục 2 QĐ 1322/QĐ-BTP.
- Evidence: [r7-7-4-6-tc06-export-excel.png](image/r7-7-4-6-tc06-export-excel.png).

### TC-010 — BR-AUTH-05 cross-cấp duyệt — ⚠️ Sai spec FE

**Setup:** cb_nv_dp_01 tạo TC-STP-AG-0001 → trình duyệt → state CHO_PHE_DUYET (POST `/.../trinh-phe-duyet` 200).

**Test:**
- cb_pd_tw_02 (TW PD) navigate trực tiếp `/chuyen-gia-tvv/to-chuc/{id}` → **vào được** detail TC-STP-AG-0001 (record cấp ĐP) **+ vẫn render button [Phê duyệt]/[Từ chối]**.
- Click [Phê duyệt] → modal "Xác nhận phê duyệt và công bố" mở, fill Số QĐ + Ý kiến → click [Phê duyệt].
- POST `/api/v1/to-chuc-tu-vans/{id}/phe-duyet` **403** ✅ — BE block đúng spec BR-FLOW-03.
- BUT FE: modal vẫn mở, không có toast lỗi, button vẫn enable. UX mơ hồ.

**Đánh giá:** BE đúng spec, FE thiếu permission gate cross-cấp + missing 403 toast handler.
- Evidence: [r7-7-4-6-tc10-cross-cap-be-403.png](image/r7-7-4-6-tc10-cross-cap-be-403.png).
- Bug: BUG-002 (Minor).

### TC-017 — Công khai 0→1

- Detail TC-BTP-TW-0009 (HOAT_DONG, laCongKhai=false) → click switch "Công khai".
- Modal "Công khai lên Cổng pháp luật quốc gia" mở yêu cầu Mô tả công khai (max 5000 ký) — đúng BR-PUBLIC-01/02/03.
- Fill mô tả 64 ký → click [Công khai].
- POST `/api/v1/to-chuc-tu-vans/{id}/cong-khai` 200 → switch checked + label "Đã công khai" hiện.
- Evidence: [r7-7-4-6-tc17-cong-khai.png](image/r7-7-4-6-tc17-cong-khai.png).

### TC-018 — Hủy công khai 1→0

- Click switch lần 2 (đang checked) → POST `/.../cong-khai` 200 → toast "Cập nhật trạng thái công khai thành công".
- Switch unchecked, badge "Đã công khai" mất. Note: Hủy CK KHÔNG yêu cầu modal — toggle direct.
- Đúng BR-PUBLIC-02 (clear `thoi_gian_dang_tai` khi cong_khai=0).
- Evidence: [r7-7-4-6-tc18-huy-cong-khai.png](image/r7-7-4-6-tc18-huy-cong-khai.png).

### TC-022 — QTHT R-only — ❌ Critical bypass

**Spec:** Permission matrix v3.5 update 2026-05-05/2026-05-09 — QTHT trên TO_CHUC_TU_VAN = **👁️ R only** (không có C/U/D).

**Test 4 method qua `evaluate_script` với session qtht_01:**

```
GET    /api/v1/to-chuc-tu-vans?page=1                      → 200 ✓ (R OK)
POST   /api/v1/to-chuc-tu-vans (body invalid)              → 422 ❌ (authz BYPASS, chỉ validation block)
PATCH  /api/v1/to-chuc-tu-vans/{id}                        → 422 ❌ (authz BYPASS, validation block)
DELETE /api/v1/to-chuc-tu-vans/25248ce2-...-d2 (TC-0009)   → 204 ❌ (DELETE thành công)
```

**Hậu quả thực:** TC-BTP-TW-0009 (Cong ty Luat TNHH Lambda R8 A6 — record evidence R7.4.A6) đã **bị xóa**. GET cùng id sau DELETE → 404 "Bản ghi không tồn tại" (ERR-VAL-VII-02-01). Pool TC TV HOAT_DONG **9 → 8**.

**Đánh giá:** Lặp pattern memory `qa_htpldn_qtht_permission_bypass` (BUG R14 W1 trên TU_VAN_VIEN). BE authz layer thiếu gate role QTHT cho entity TC TV. Critical/Blocker.
- Evidence: [r7-7-4-6-tc22-qtht-bypass-delete.png](image/r7-7-4-6-tc22-qtht-bypass-delete.png).
- Bug: BUG-001 (Critical).

### TC-025 — Edit junction LV (2→3 LV)

- TC-BTP-TW-0009 (trước khi bị TC-022 xóa) — edit form: LV hiện 2 (Doanh nghiệp + Thương mại).
- Click combobox LV → chọn "Thuế" (3 LV) → click [Cập nhật].
- PATCH `/api/v1/to-chuc-tu-vans/{id}` 200 → navigate về detail.
- Verify GET response: `linhVucs[].length=3`, `linhVucIds=["...001a","...001c","...0018"]`, `version=7` (5 sau A6 → 6 sau công khai → 7 sau edit). Junction N:N TVV_TO_CHUC_LINH_VUC update đúng.
- Evidence: [r7-7-4-6-tc25-edit-junction-lv.png](image/r7-7-4-6-tc25-edit-junction-lv.png).

## Bug count

**2 bug.**
- BUG-001 Critical: QTHT bypass authz POST/PATCH/DELETE TO_CHUC_TU_VAN — đã DELETE thực tế TC-BTP-TW-0009. Lặp pattern bug R14 W1.
- BUG-002 Minor: FE thiếu permission gate cross-cấp — TW PD render [Phê duyệt]/[Từ chối] cross-cấp DP record dù BE 403.

Chi tiết: [Pass-bug-report-r7-7-4-6-tctv.md](../../bug-reports/to-chuc-tu-van/Pass-bug-report-r7-7-4-6-tctv.md).

## Observation (không log bug, defer BA confirm)

**Scope cb_nv_dp_01 list:** cb_nv_dp_01 (Sở TP AG) thấy đủ 9 record cấp TW (`TC-BTP-TW-*`) trong list trang Đang hoạt động. Per BR-AUTH-08 strict spec ("danh sách TC TV thuộc đơn vị"), ĐP chỉ thấy TC TV của Sở TP AG. Update 2026-05-06 chỉ thêm exception TW (TW thấy all), không nói ĐP thấy TW. Cần BA chốt: ĐP có quyền đọc cross-cấp xuống TW (national registry) hay strict scope?

## Pool sau test

```
total=8, byState={HOAT_DONG:7, MOI_DANG_KY:0, CHO_PHE_DUYET:1, TU_CHOI:0, TAM_DUNG:0, VO_HIEU_HOA:0}
```

| Mã | Tên | State | Note |
|---|---|:-:|---|
| TC-BTP-TW-0001..0008 | (pool TW R7.2.3) | HOAT_DONG | Còn 8 (TC-0009 bị TC-022 DELETE) |
| TC-STP-AG-0001 | Cong ty Luat AG R7746 | CHO_PHE_DUYET | Tạo bởi cb_nv_dp_01 (TC-002), đã trình duyệt nhưng cb_pd_tw_02 không duyệt được (TC-010 cross-cấp 403). Cần cb_pd_dp_01 duyệt cùng cấp để vào HOAT_DONG. |

## Downstream

- ⚠️ R7.7.4.6 ⚠️ Sai spec — 8/10 đạt + 1 sai spec FE + 1 lỗi critical authz bypass. Block đề xuất escalate dev khẩn cấp BUG-001.
- Pool TC TV HOAT_DONG giảm 9→7 (TC-0009 bị xóa + TC-STP-AG chưa HOAT_DONG). Downstream TVV `to_chuc_chinh_id` dropdown cần re-verify.
- Lặp lại pattern memory `qa_htpldn_qtht_permission_bypass` — đề xuất audit toàn bộ entity QTHT R\* để catch bypass tương tự (NHT, GIẢNG VIÊN, etc.).
