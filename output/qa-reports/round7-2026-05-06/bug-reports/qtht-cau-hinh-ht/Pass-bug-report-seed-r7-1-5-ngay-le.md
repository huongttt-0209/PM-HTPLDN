# Bug Report — R7.1.5 Tab Ngày lễ FE submit silent fail (FR-VIII-29)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM Hỗ trợ Pháp lý Doanh nghiệp |
| **Môi trường** | http://103.172.236.130:3000/quan-tri/cau-hinh?tab=ngay-le |
| **Người test** | QA Automation via Claude Code (qtht_02) |
| **Ngày** | 2026-05-07 01:16:13 (approx — git commit time) |
| **Loại test** | Seed via UI (R7.1.5 Phase 1) |
| **Round** | Round 7 |
| **Tài liệu tham chiếu** | [SRS FR-VIII-29 line 1380-1414 srs-fr-10-quan-tri.md](../../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) · [SRS Entity §3.4.3.51 NGAY_LE line 2059-2070](../../../../../input/srs-update-2026-5-5/srs-fr-10-quan-tri.md) · [tasks/todo.md R7.1.5](../../../../../tasks/todo.md) |
| **2-source verify** | ✅ NotebookLM Haizz-HTPLDN (id `a4ae45bf-...`) + grep SRS local — match 100% |

---

## Tổng hợp

Phát hiện **1** lỗi khi seed Tết Nguyên đán Bính Ngọ qua UI Tab Ngày lễ SCR-VIII-06.

> **Note:** BUG-NGAY-LE-002 (thiếu Tab "Quy trình hỗ trợ") đã DROPPED 2026-05-07 — user chốt tạm thời bỏ tab Quy trình khỏi SCR-VIII-06 → 3 tab hiện tại (SLA / Mẫu phản hồi / Ngày lễ) đúng spec mới.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 1      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-NGAY-LE-001~~ | Major | P1 | UI/UX | R7.1.5 | `FR-VIII-29 §Processing bước 4` (line 1412) | Form Thêm mới ngày lễ — button [Đồng ý] click silent fail, không trigger POST + không hiện validation error | **Closed-verified R8 lần 8 (2026-05-09 11:18 sau cache clear toàn diện)** |

> **Re-test 2026-05-07:** ❌ STILL OPEN. Fill date `25/12/2026` qua DatePicker calendar click + tên + ghi chú → click [Đồng ý] vẫn silent: KHÔNG trigger POST `/api/v1/ngay-le`, KHÔNG toast, KHÔNG inline error. Modal stuck open. Bug chưa được dev fix.
>
> **Re-test 2026-05-07 14:00 (sau dev claim fix lần 2):** ❌ STILL OPEN. Account qtht_02. Mở modal Thêm mới Ngày lễ → click DatePicker chọn ngày 08/05/2026 (verify input value = `08/05/2026`) → fill tên "Test re-test BUG-NGAY-LE-001" → Loại default "Ngày lễ" → click [Đồng ý]. Network log chỉ có `auth/refresh + GET ngay-le?nam=2026 + GET unread-count` — KHÔNG có POST `/api/v1/ngay-le`. Modal vẫn open, không toast/error. Inline `Vui lòng chọn ngày` vẫn hiện dù đã chọn date qua DatePicker (FE chưa update validation state). Bug FE chưa được fix. Evidence: [r7-1-5-retest-still-silent-2026-05-07.png](image/r7-1-5-retest-still-silent-2026-05-07.png).
>
> **Re-verify 2026-05-07 14:30 (cache clear + hard reload):** ❌ CONFIRMED STILL OPEN. Đã clear `caches.delete()` + `localStorage.clear()` + `sessionStorage.clear()` + reload `ignoreCache:true` + login lại qtht_02 trong isolated context fresh. Mở modal Thêm mới Ngày lễ → click DatePicker chọn ngày 09/05/2026 (input value = `09/05/2026`) → fill tên "Test cache-clear NGAY-LE-001" → Loại default "Ngày lễ" → click [Đồng ý]. Network log: `auth/refresh + GET ngay-le?nam=2026 + GET unread-count` — KHÔNG có POST `/api/v1/ngay-le`. Modal stuck open. Không phải cache stale — bug FE thực sự. Evidence: [r7-1-5-cache-clear-still-silent.png](image/r7-1-5-cache-clear-still-silent.png).
>
> **Re-test 2026-05-07 R8 (16:42, sau dev claim fix lần 3):** ❌ **VẪN OPEN**. Account qtht_02. Modal Thêm mới Ngày lễ — click DatePicker chọn 15/05/2026 (input value `15/05/2026`) → fill tên "QA Re-test BUG-NGAY-LE-001 2026-05-07" → Loại default "Ngày lễ" → click [Đồng ý]. Network full session (13 requests) hoàn toàn KHÔNG có POST `/api/v1/ngay-le` — chỉ có baseline `auth/refresh + GET ngay-le?nam=2026 + GET unread-count + GET cau-hinh/sla`. Modal stuck open, form values preserved (date + tên), KHÔNG toast/error/inline validation. Table sau click vẫn 4 record (Tết DL/30-4/1-5/Quốc khánh — Tết Nguyên đán Bính Ngọ R7 đã reset cùng pool). Bug FE handler [Đồng ý] hoàn toàn không trigger submit. Screenshot: [r8-verify-2026-05-07-bug-ngay-le-001-still-silent.png](../../screenshots/r8-verify-2026-05-07-bug-ngay-le-001-still-silent.png).
>
> **Re-test 2026-05-08 R8 lần 5 (sau dev claim fix lần 4):** ❌ **VẪN OPEN**. Account qtht_02 (isolated context fresh). Vào `/quan-tri/cau-hinh?tab=ngay-le` → table 4 record năm 2026 → click [+ Thêm mới] → modal mở. Fill input "Ngày" type text `16/05/2026` (input value verify = `16/05/2026`) + tên `QA R8 retest BUG-NGAY-LE-001 2026-05-08` + Loại default "Ngày lễ" → click [Đồng ý]. Network full session (12 requests) KHÔNG có `POST /api/v1/ngay-le` — chỉ có `auth/login + verify-otp + auth/me + dashboard + cau-hinh/sla + GET ngay-le?nam=2026 + thong-baos/unread-count`. Modal stuck open với form values preserved, KHÔNG toast/error/inline validation. Bug FE handler chưa fix sau 5 lần verify.
>
> **Re-test 2026-05-08 23:38 R8 lần 6 (post DB reset — pool về 4 record):** ❌ **VẪN OPEN**. Account qtht_02. Tab Ngày lễ render 4 record (Tết DL/30-4/1-5/Quốc khánh — Tết NĐ R7 lần 5 đã bị reset cùng pool). Click [+ Thêm mới] → drawer mở (NOTE: form là `.ant-drawer-section`, không phải Modal — phát hiện mới R8 lần 6). Fill input Ngày `17/02/2026` + tên `QA R8 retest BUG-NGAY-LE-001 lần 6 (2026-05-08)` + Loại default "Ngày lễ" + Ghi chú text. Click [Đồng ý]. Network 24 request session (auth + dashboard + cau-hinh/sla + ngay-le?nam=2026 + thong-baos/unread-count polling) — KHÔNG có `POST /api/v1/ngay-le`. Drawer stuck open, form values preserved, toast inline `Vui lòng chọn ngày` (FE validation state stale dù input.value=`17/02/2026`). API direct probe POST → 201 OK record id `0647a404-4e84-4578-9718-8f2fa080f853`, table reload UI 5/5 record. Bug FE submit handler chưa fix sau 6 lần verify. Evidence: [bug-ngay-le-001-retest-lan-6-2026-05-08.png](bug-ngay-le-001-retest-lan-6-2026-05-08.png) + [r7-1-5-tab-ngay-le-5-records-reverify-2026-05-08.png](../../seed/qtht-cau-hinh-ht/r7-1-5-tab-ngay-le-5-records-reverify-2026-05-08.png) (sau API workaround).
>
> **Re-test 2026-05-09 02:05 R8 lần 7 (sau dev claim fix lần 5):** ❌ **VẪN OPEN — TESTED 3 INPUT METHODS, ALL FAIL.** Account qtht_02. Hard reload `ignoreCache:true` + drawer mở fresh. **Tested 3 method để rule out method limitation:**
>
> - **Method 1 — Programmatic native setter** (HTMLInputElement.prototype.value setter + dispatch input/change): Fill ngày `18/02/2026` + tên + ghi chú → click [Đồng ý]. Network: 4 baseline GET requests, KHÔNG có POST `/api/v1/ngay-le`. Drawer stuck.
> - **Method 2 — MCP keyboard type_text** (real keystroke vào focused DatePicker input): Fill `19/02/2026` qua type_text + Enter, fill_form Tên + Ghi chú → click [Đồng ý]. Network: KHÔNG có POST. Drawer stuck.
> - **Method 3 — Calendar click chọn ngày** (real user flow đúng nhất — click ô input → mở dropdown calendar → click cell ngày 20): Fill `20/05/2026` qua calendar dropdown click + fill_form Tên + Ghi chú → click [Đồng ý]. Network: KHÔNG có POST. Drawer stuck. KHÔNG có form errors, toasts, console errors.
> - **Console log:** Chỉ 1 warning Antd `[antd: Drawer] width is deprecated` — KHÔNG có error JS submit handler.
> - **Form state DOM:** input.value persist OK cả 3 method. Submit button không disabled.
> - **Mouse event sequence test:** dispatch full mousedown+mouseup+click + form.dispatchEvent('submit') → vẫn KHÔNG fire POST.
>
> **Conclusion:** Bug FE submit handler 100% confirmed — onClick/onSubmit React handler không gọi mutation API regardless of input method. Dev claim fix lần 5 KHÔNG thực sự fix bug. Cần dev:
> 1. Re-deploy với confirm code change đã push lên branch deploy
> 2. Check React Form `onFinish` handler có throw silent error không (try/catch swallow)
> 3. Check `useMutation` hook có conditional `enabled: false` chặn fire không
> 4. Test POST manual qua curl (đã verify R8 lần 6 BE 201 OK với token JWT) → BE không phải nguyên nhân, FE thuần.
>
> Evidence: [bug-ngay-le-001-retest-lan-7-2026-05-09.png](bug-ngay-le-001-retest-lan-7-2026-05-09.png).
>
> **Re-test 2026-05-09 11:18 R8 lần 8 (sau dev claim fix lần 5 + CACHE CLEAR TOÀN DIỆN):** ✅ **CLOSED-VERIFIED!** Account qtht_02. **Phương pháp:**
> 1. Clear `caches.delete()` toàn bộ + unregister service workers + `localStorage.clear()` + `sessionStorage.clear()` + BE logout (clear refresh-token cookie HttpOnly).
> 2. Hard reload `ignoreCache:true` /login + login fresh qtht_02 + OTP 666666.
> 3. Nav `/quan-tri/cau-hinh?tab=ngay-le` → table 5/5 (4 pre-existing + Tết NĐ R8 lần 6).
> 4. Click [+ Thêm mới] → drawer mở. Click DatePicker input → calendar dropdown mở → click cell ngày 21 (May 2026). Verify input value = `21/05/2026`. Fill Tên `QA R8 retest BUG-NGAY-LE-001 lần 8 (cache clear + calendar)` + Ghi chú text. Loại default "Ngày lễ".
> 5. Click [Đồng ý].
>
> **Result:** ✅
> - Network: `POST /api/v1/ngay-le` → **201 Created** ✅ (lần đầu trigger sau 7 lần fail)
> - Network: `GET /api/v1/ngay-le?nam=2026` → 200 (auto reload table)
> - Drawer: **đóng tự động** ✅
> - Table: render **6/6 mục** với record mới `21/05/2026 — QA R8 retest BUG-NGAY-LE-001 lần 8` ✅
>
> **Root cause analysis:** Dev fix lần 5 đã work, nhưng lần 6+7 verify FAIL là do **FE bundle cached** trong browser (chrome-devtools-mcp profile cache). Cache invalidate qua `caches.delete()` + service worker unregister + hard reload `ignoreCache:true` mới load FE bundle mới chứa fix.
>
> **Lesson learned (memory candidate):** Sau dev claim FE fix → BẮT BUỘC clear cache toàn diện (caches.delete + SW unregister + hard reload + fresh login) trước khi conclude FAIL. Pattern "FE silent fail" với input.value persist + no JS error + no network request thường là FE bundle cũ bị cache thay vì bug FE thực sự.
>
> **Status:** **Closed-verified R8 lần 8 (2026-05-09 11:18)**. Evidence: [bug-ngay-le-001-CLOSED-lan-8-2026-05-09.png](bug-ngay-le-001-CLOSED-lan-8-2026-05-09.png).
>
> **Re-verify 2026-05-10 R8 lần 9 (regression check 1 ngày sau closed):** ✅ **VẪN CLOSED — Bug không re-open.** Account qtht_02 fresh isolated context (cache clear toàn diện + service worker unregister + localStorage/sessionStorage clear + BE logout + hard reload `ignoreCache:true`). Nav `/quan-tri/cau-hinh?tab=ngay-le` → table 6/6 (4 pre-existing + Tết NĐ R7 + record R8 lần 8 21/05/2026). Click [+ Thêm mới] → drawer mở. Click input Ngày + type_text `22/05/2026` + Enter (input.value = `22/05/2026`). Fill Tên `QA verify BUG-NGAY-LE-001 R8 lần 9 (2026-05-10)` + Ghi chú. Loại default "Ngày lễ". Click [Đồng ý].
>
> **Result:** ✅
> - Network: `POST /api/v1/ngay-le` → **201 Created** ✅ (reqid=388)
> - Network: `GET /api/v1/ngay-le?nam=2026` → 200 (auto reload) ✅ (reqid=389)
> - Drawer: **đóng tự động** ✅
> - Table: render **7/7 mục** (record mới row 6: `22/05/2026 — QA verify BUG-NGAY-LE-001 R8 lần 9 (2026-05-10)`) ✅
> - Console: 0 error / 0 warn ✅
>
> **Conclusion:** Fix dev lần 5 stable, bug FE submit handler không regression sau 1 ngày. Confirm rename `Pass-` prefix là chính xác. Evidence: [bug-ngay-le-001-reverify-2026-05-10-still-closed.png](bug-ngay-le-001-reverify-2026-05-10-still-closed.png).

---

## BUG-NGAY-LE-001 — Form Thêm mới ngày lễ — submit silent fail (button [Đồng ý] không trigger POST)

### Mô tả

Modal "Thêm mới ngày lễ" trên Tab Ngày lễ SCR-VIII-06: sau khi fill đủ 3 trường bắt buộc (Ngày = `17/02/2026` chọn từ Antd DatePicker calendar, Tên ngày lễ = `Tết Nguyên đán Bính Ngọ`, Loại = `Ngày lễ` chọn từ dropdown listbox 3 option), click button [Đồng ý] **không trigger POST** tới `/api/v1/ngay-le`, modal vẫn open, không hiện toast thành công/thất bại, không hiện validation error message inline. Probe trực tiếp BE bằng API `POST /api/v1/ngay-le` với body camelCase đúng schema → BE trả **201 thành công**, record được lưu DB và hiện trong table sau reload — chứng minh BE work fine, FE bug khi handle submit.

### Các bước tái hiện

1. Login `qtht_02` / `Secret@123` / OTP `666666`.
2. Sidebar > Quản trị hệ thống > Cấu hình hệ thống → URL `/quan-tri/cau-hinh`.
3. Click tab "Quản lý ngày lễ" → URL `/quan-tri/cau-hinh?tab=ngay-le`. Quan sát table 4 record pre-existing năm 2026.
4. Click button [+ Thêm mới] → modal "Thêm mới ngày lễ" mở (4 trường: Ngày * / Tên ngày lễ * / Loại * / Ghi chú).
5. Click input "Ngày" → Antd date picker dropdown mở → click ngày 17 trong tháng 2/2026. Verify input value hiển thị `17/02/2026`.
6. Fill input "Tên ngày lễ" = `Tết Nguyên đán Bính Ngọ`.
7. Click combobox "Loại" → listbox 3 option (Ngày lễ / Nghỉ bù / Nghỉ khác) hiện → click "Ngày lễ".
8. Fill textarea "Ghi chú" = `Mùng 1 Tết âm lịch...`.
9. Click button [Đồng ý].
10. Quan sát: modal vẫn open, không thay đổi, không có toast/error.
11. Mở DevTools Network tab → KHÔNG thấy request `POST /api/v1/ngay-le` xuất hiện (chỉ có refresh + thong-baos polling).
12. Lặp lại click [Đồng ý] thêm 2 lần → vẫn silent.
13. Probe BE bằng `evaluate_script` fetch trực tiếp với JWT từ session → BE trả 201, record ID `7a2c4cf6-d68b-4947-8488-6b7049b84bff` lưu DB.
14. Click [Hủy] → close modal → reload trang → table render 5/5 record bao gồm `Tết Nguyên đán Bính Ngọ 17/02/2026`.

### Kết quả mong đợi

- Click [Đồng ý] → FE validate client-side → POST `/api/v1/ngay-le` body `{ngay, nam, tenNgayLe, loai, ghiChu}` → BE 201 → close modal + reload table + toast "Thêm mới thành công" (như flow đã verify ở DM6/7 SCR-VIII-01 trong R7.1.6).
- Theo SRS FR-VIII-29 §Processing bước 4 (line 1412): "Tạo / Cập nhật / Xóa (soft delete) bản ghi NGAY_LE".

### Kết quả thực tế

- Click [Đồng ý] silent — không POST, không error, không feedback.
- Modal stuck mở — user không biết vì sao.
- API direct probe POST 201 → BE work fine → loại trừ BE bug, confirm FE bug.

### Bằng chứng

**1. Ảnh modal sau click [Đồng ý] 3 lần — modal vẫn open, table chưa update:**

![BUG-NGAY-LE-001 — Modal Thêm mới stuck sau click Đồng ý](../../seed/qtht-cau-hinh-ht/r7-1-5-fe-submit-silent-fail.png)

**2. Ảnh table sau reload — 5/5 record (Tết NĐ đã save qua API workaround):**

![BUG-NGAY-LE-001 — Table 5/5 record sau API direct POST + reload](../../seed/qtht-cau-hinh-ht/r7-1-5-tab-ngay-le-5-record-final.png)

**3. Network log (full session 9 request) — KHÔNG có POST `/api/v1/ngay-le`:**

```
reqid=1116 POST /api/v1/auth/refresh [200]
reqid=1132 GET /api/v1/cau-hinh/sla [200]
reqid=1139 GET /api/v1/ngay-le?nam=2026 [200]
reqid=1140-1145 GET /api/v1/thong-baos/unread-count [304]
(KHÔNG có POST /api/v1/ngay-le sau 3 lần click Đồng ý)
```

**4. API direct probe — BE 201:**

```json
POST /api/v1/ngay-le
Headers: Authorization: Bearer <JWT-qtht_02>
Body: {"ngay":"2026-02-17","nam":2026,"tenNgayLe":"Tết Nguyên đán Bính Ngọ","loai":"NGAY_LE","ghiChu":"Mùng 1 Tết âm lịch..."}
Response 201: {"success":true,"data":{"id":"7a2c4cf6-d68b-4947-8488-6b7049b84bff","ngay":"2026-02-17","nam":2026,"tenNgayLe":"Tết Nguyên đán Bính Ngọ","loai":"NGAY_LE","ghiChu":"...","ngayTao":"2026-05-06T17:01:41.483Z","version":1}}
```

**5. SRS local quote nguyên văn (`input/srs-update-2026-5-5/srs-fr-10-quan-tri.md` line 1407-1413, FR-VIII-29 §Processing):**

```
| Bước | Mô tả xử lý | BR áp dụng |
| 1 | Kiểm tra quyền QTHT | BR-AUTH-01 |
| 2 | Validate: ngay_ket_thuc >= ngay_bat_dau | — |
| 3 | Kiểm tra trùng lặp: không có ngày lễ khác overlap cùng khoảng thời gian | — |
| 4 | Tạo / Cập nhật / Xóa (soft delete) bản ghi NGAY_LE | BR-DATA-01, BR-DATA-03 |
```

**6. NotebookLM verify** — query "FR-VIII-29 Processing bước 4 có tạo/sửa/xóa NGAY_LE không?" → AI confirmed match SRS local 100%.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` bypass |
| MailHog | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design (Modal, DatePicker, Select) |
| Xác thực | JWT + OTP |
| Tool test | Chrome DevTools MCP |
| Account dùng | qtht_02 (vai trò QTHT, cấp TW) |
| NotebookLM | https://notebooklm.google.com/notebook/a4ae45bf-cea0-4325-8fee-b1e0be702cf2 |

---

*Bug report generated: 2026-05-07 | QA Automation via Claude Code | 2-source verify NotebookLM + SRS local*
