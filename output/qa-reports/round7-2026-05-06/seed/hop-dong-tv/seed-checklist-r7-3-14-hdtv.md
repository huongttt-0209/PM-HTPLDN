# Seed Checklist — HĐ Tư vấn (R7.3.14)

**Ngày:** 2026-05-10 02:14:00 (lần đầu) · 2026-05-10 09:04:00 (retest dev fix) • **Tài khoản:** `cb_nv_tw_01` (R7 retest — sau dev fix BUG-HDTV-003) / `cb_nv_tw_02` (R6 fallback) • **Trạng thái mong đợi:** `Đang thực hiện` (DANG_THUC_HIEN)
**Màn:** SCR-X3-01 — accordion "HĐ tư vấn liên kết" trong VV detail • **Đường dẫn:** `/vu-viec/{vvId}` (HĐ TV không có menu độc lập, chỉ truy cập sub-resource per spec v2.1)
**SRS:** [FR-X.3-01 UC163 — Quản lý HĐ tư vấn](../../../../input/srs-v3/srs-fr-14-hop-dong-tv.md) §2 line 60-150

---

## Downstream consumer × filter

| Task downstream | Đọc filter | Số record cần | State entity yêu cầu | Verify query | Status |
|---|---|---|---|---|:-:|
| R7.7.14 (functional HĐ TV 38 TC) | HĐ `trangThai=DANG_THUC_HIEN` cover ≥6 LV qua VV link | ≥1 HĐ DANG_THUC_HIEN/LV × 6 LV = ≥6 HĐ | DANG_THUC_HIEN + ≥1 vuViecIds với LV match | `GET /api/v1/hop-dong-tu-vans` rồi GET sub `/vu-viecs` của từng HĐ | ✅ 6/6 (R7 retest) |

**Acceptance:** ≥1 HĐ DANG_THUC_HIEN/LV cover 6 LV (Lao động/Đất đai/SHTT/Thuế/Hành chính/Thương mại). HĐ phải link tới VV của LV tương ứng để R7.7.14 verify cross-module.

---

## Kết quả: ✅ ĐẠT 6/6 LV linked sau R7 retest dev fix

R7 (2026-05-10 09:04:00 retest sau dev claim fix bug): Tạo HDTV-20260510-0008 qua UI VV detail flow của VV-509-001 (Lao động — Phúc An AG) → form NAY có field "Vụ việc liên kết" auto-populated từ URL param `vuViecId` → POST 201 + section "HĐ tư vấn liên kết" của VV render row mới với cột Vụ việc=1 → API `soVuViecLienKet=1`. **Pool 6/6 LV cover** (Đất đai/SHTT/Thuế/Hành chính/Thương mại từ R6 + Lao động R7 fresh create).

**Bug đóng:** [Pass-bug-report-r7-3-14-hdtv.md](../../bug-reports/hop-dong-tv/Pass-bug-report-r7-3-14-hdtv.md) — 3/3 đóng:
- BUG-HDTV-001 (form thiếu VV field) → ✅ Closed: form có "Vụ việc liên kết" textbox disabled auto-fill
- BUG-HDTV-002 (POST 409 dai dẳng) → ✅ Closed: probe 201, không gặp lại 409
- BUG-HDTV-003 (FE route guard kick login) → ✅ Closed: sidebar VV click pass dù `cb_nv_tw_01` vẫn còn 3 role kèm ghost

---

## Bảng dữ liệu seed

| # | Mã HĐ | Tên HĐ | LV (qua VV link) | Bên A | Bên B | Giá trị | VV linked | Trạng thái | Có vào kho? |
|---|---|---|---|---|---|---|---|---|:-:|
| 1 | HDTV-20260510-0001 | HĐ TV Lao động - Phúc An AG (R7.3.14 seed) — pre-fix mồ côi | Lao động (chưa link VV) | Công ty Cổ phần Phúc An AG | TVV-BTP-TW-0014 | 50.000.000 | ✗ 0 | DANG_THUC_HIEN | ⚠️ giữ làm evidence pre-fix |
| 2 | HDTV-20260510-0003 | HĐ TV R7.3.14 - Đất đai - VV-BTP-TW-20260509-005 | Đất đai | Bộ Tư pháp - Cục Bổ trợ tư pháp | Công ty Cổ phần Thành Đạt BG | 50.000.000 | ✓ VV-509-005 | DANG_THUC_HIEN | ✅ |
| 3 | HDTV-20260510-0004 | HĐ TV R7.3.14 - Sở hữu trí tuệ - VV-BTP-TW-20260509-004 | Sở hữu trí tuệ | Bộ Tư pháp - Cục Bổ trợ tư pháp | Công ty TNHH Phương Đông BG | 55.000.000 | ✓ VV-509-004 | DANG_THUC_HIEN | ✅ |
| 4 | HDTV-20260510-0005 | HĐ TV R7.3.14 - Thuế - VV-BTP-TW-20260509-002 | Thuế | Bộ Tư pháp - Cục Bổ trợ tư pháp | DNTN Hoàng Gia AG | 60.000.000 | ✓ VV-509-002 | DANG_THUC_HIEN | ✅ |
| 5 | HDTV-20260510-0006 | HĐ TV R7.3.14 - Hành chính - VV-BTP-TW-20260507-006 | Hành chính | Bộ Tư pháp - Cục Bổ trợ tư pháp | DNTN Đông Dương BCT | 65.000.000 | ✓ VV-507-006 | DANG_THUC_HIEN | ✅ |
| 6 | HDTV-20260510-0007 | HĐ TV R7.3.14 - Thương mại - VV-BTP-TW-20260509-003 | Thương mại | Bộ Tư pháp - Cục Bổ trợ tư pháp | Hộ kinh doanh Đại Việt AG | 70.000.000 | ✓ VV-509-003 | DANG_THUC_HIEN | ✅ |
| 7 | HDTV-20260510-0008 | HĐ TV R7.3.14 - Lao động - VV-BTP-TW-20260509-001 (R7 retest fresh post-fix) | Lao động | Bộ Tư pháp - Cục Bổ trợ tư pháp | Công ty Cổ phần Phúc An AG | 60.000.000 | ✓ VV-509-001 | DANG_THUC_HIEN | ✅ |

**Tổng pool:** 7 HĐ DANG_THUC_HIEN trong DB (1 mồ côi pre-fix + 6 linked cover 6 LV).

---

## Phương pháp seed

**Tool:** Chrome DevTools MCP (`mcp__chrome-devtools__*`) + fallback `evaluate_script` POST API.

**HĐ #2 (HDTV-20260510-0002 — Lao động VV-009):**
- ✅ Tạo qua UI: login `cb_nv_tw_02` → click sidebar Vụ việc → click VV-009 row → expand accordion "HĐ tư vấn liên kết" → click "Tạo hợp đồng" → fill modal form (Tên/Bên A/Bên B/Giá trị/Trạng thái default DANG_THUC_HIEN/Date range 10/05-09/08) → click "Tạo mới" → POST `/api/v1/hop-dong-tu-vans` 201 → returned id `366a9bc7-...`
- ⚠️ Phát hiện: form modal KHÔNG có VV picker → HD tạo standalone, `soVuViecLienKet=0` (không auto-link VV-009 dù vào từ accordion VV-009)
- DELETE để retry với `vuViecIds: ['765920aa-...']` body → DELETE 204 OK
- POST tiếp với `vuViecIds` → **409 ERR-STATE-SYS-00-01** dai dẳng (6 lần retry với unique fields, vẫn 409). Cần dev fix BE.

**HĐ #3..#7 (5 LV còn lại):**
- ✅ Bulk POST API `/api/v1/hop-dong-tu-vans` với body có `vuViecIds: [<vvId>]` (do JWT revoke aggressive ~3-5 phút khiến UI navigation gãy giữa session). Tất cả 5 POST trả 201 + `soVuViecLienKet=1` confirmed.
- Per memory rule [`feedback_qa_block_must_seed_data`](../../../../../.claude/projects/-Users-teamai-Downloads-antigravity-QA-skilkk/memory/feedback_qa_block_must_seed_data.md) cho phép POST API khi UI block.

**Verify final:**
- `GET /api/v1/hop-dong-tu-vans` → 6 records, 5 linked (`soVuViecLienKet=1`) + 1 unlinked.
- UI verify: VV-005 detail accordion "HĐ tư vấn liên kết" hiển thị HDTV-20260510-0003 đầy đủ thông tin (xem screenshot).

---

## Ảnh chụp

- [HDTV-0003 link VV-005 — UI accordion verified](r7-3-14-vv005-hdtv-003-linked-2026-05-10.png) — VV detail Đất đai / Hợp đồng tư vấn liên kết / table 1 HĐ DANG_THUC_HIEN

---

## Lưu ý cho R7.7.14 downstream

**Pool 7 HĐ DANG_THUC_HIEN (6 linked cover 6 LV + 1 mồ côi)** — đủ data cho phần lớn TC functional R7.7.14.

### TC R7.7.14 chạy được ngay (pool hiện tại đủ)
- **HDTV-013/014/015 (negative validation):** Form `/hop-dong-tv/tao-moi` đầy đủ field bắt buộc → test trống tên / ngày bắt đầu > kết thúc / giá trị ≤ 0 → verify ERR-HDTV-01/02/05.
- **HDTV-018 (progress bar):** Tạo HD mới với 2 mốc thanh toán (30tr + 20tr / 100tr) qua field "Thêm giai đoạn thanh toán" → verify công thức 50%.
- **HDTV-019 (highlight đỏ ≤30 ngày):** Pool 7 HD có ngayKetThuc 09/08/2026 (90 ngày) → tạo thêm HD ngayKetThuc 5-6 ngày tới để test boundary.
- **HDTV-020 (audit log):** Verify CRUD audit qua tab Nhật ký HD detail.
- **HDTV-026 (link N:N):** HDTV-0001 (mồ côi) còn unlinked → test add VV via PATCH `vuViecIds` body để verify N:N (memory rule fixture mismatch SRS không log bug).
- **HDTV-027 (access from VV detail):** ✅ ĐÃ verify trong seed (VV-509-005 → HDTV-0003).
- **HDTV-021/022/023 (authorization):** Multi-role test với QTHT/TVV/CG/NHT/DN — verify permission matrix.
- **HDTV-024 (BR-AUTH-08 BN/Tinh scope):** Test với `cb_nv_bn_01` + `cb_nv_dp_01` → verify chỉ thấy HD đơn vị mình.
- **HDTV-025 (guard delete có VV link):** 6 HD linked → DELETE → verify ERR-HDTV-04 chặn.
- **HDTV-029/031 (TVV dropdown filter HOAT_DONG):** Cần check form có TVV picker hay chỉ Bên B textbox — observation post-fix form vẫn không thấy TVV dropdown rõ ràng → có thể là gap riêng cần tách bug nếu confirm.
- **HDTV-030 (verify hard delete):** DELETE HDTV-0001 (mồ côi) → GET 404.

### TC R7.7.14 BLOCKED bởi dep khác (KHÔNG do R7.3.14)
- **HDTV-001/002/003/004/005 (list/search/create/detail/edit qua SCR-X3-01 menu):** ⏳ BLOCKED — HD TV không có menu độc lập (R7.E1 verify FE/API 404). Phải test qua entry-point VV/TVV detail chứ không qua menu chính.
- **HDTV-028 (truy cập qua TVV detail "Lịch sử"):** Cần verify TVV detail có tab "Lịch sử" + HD list. Cần tách probe.
- **TC liên quan VV HOAN_THANH:** todo.md R7.7.14 dep `≥1 VV HOAN_THANH (✗ 0)` — TC nào cần HD ở VV HOAN_THANH (đánh giá cuối kỳ, thanh lý) sẽ block đến khi VV HOAN_THANH có sẵn. Tách subtask R7.7.14-LIFECYCLE riêng nếu cần.

### Khuyến nghị scope R7.7.14
- Chạy ngay batch ~20-22 TC (HDTV-013..015, 018..023, 025..027, 029..031) với pool hiện tại.
- Defer ~10-12 TC list/search/menu (001-005) đến khi BA confirm spec menu.
- 1-2 TC liên quan TVV history (028) cần probe thêm.

---

*2026-05-10 02:14 — QA chạy bằng Chrome DevTools MCP, fallback API POST do JWT revoke + BE 409 block UI retry*
