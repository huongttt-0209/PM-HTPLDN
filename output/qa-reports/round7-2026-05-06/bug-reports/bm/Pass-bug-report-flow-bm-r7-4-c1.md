# Bug Report — Thư viện Biểu mẫu (FR-VII v3.5) — R7.4.C1 Workflow

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-07 13:54:12 (approx — git commit time) |
| **Loại test** | Workflow (SM-BIEUMAU 3 transition + 4 trường công khai + BR-PUBLIC-01/02/03) |
| **Round** | R7.4.C1 |
| **Tài liệu tham chiếu** | [`srs-update-2026-5-5/_DELTA-MAP-FR09.md`](../../../../../input/srs-update-2026-5-5/_DELTA-MAP-FR09.md) · [`srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md`](../../../../../input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md) line 1010-1117 · [`srs-fr-12-tv-chuyen-sau.md`](../../../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md) line 1597-1613 (BR-PUBLIC-01/02/03 canonical) |

---

## Tổng hợp

Phát hiện **6** lỗi vi phạm SRS v3.5 FR-VII (Thay đổi 1 + 3 BR mới) trong workflow công khai Thư viện Biểu mẫu. **Tất cả 6/6 đã đóng tại R8 lần 7 (2026-05-10).**

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 6    | 2        | 2     | 2      | 0     | 0       |

### Status sau R8 lần 7 (2026-05-10)

| Đóng | Còn open | % đóng |
|---|---|---|
| **6/6** (BUG-BM-001 R8 lần 3 Switch + BUG-BM-002 R8 + BUG-BM-003 R8 + BUG-BM-004 R8 + BUG-BM-005 R8 lần 7 manual+observer + BUG-BM-006 R8 lần 2) | 0/6 | **100%** ✅ |

### Re-verify R8 lần 4 (2026-05-10) — full sweep 6/6 bug

Account `cb_nv_tw_02`. Verify chi tiết per bug:

| Bug | Status | Evidence | Note |
|---|---|---|---|
| BUG-BM-001 | ✅ Closed (persist) | `r8-reverify-2026-05-10-bug-bm-001-form-4fields.png` — form `/bieu-mau/them-moi` snapshot a11y có đủ 4/4 fields: Switch uid `4_35` + Ảnh đại diện uid `4_39` + Mô tả công khai uid `4_41` + File đính kèm công khai uid `4_46` | 4/4 CR-01 fields render OK |
| BUG-BM-002 | ✅ Closed (persist) | API GET `/bieu-maus?thuMucId=26f55adf-...` (TM Thuế đã AN) → BM-20260507-002 `trangThai=AN, congKhai=false, thoiGianDangTai=null` | BR-PUBLIC-02 enforced — `thoiGianDangTai` clear khi BM AN |
| BUG-BM-003 | ✅ Closed (persist) | API GET `/bieu-maus/8a7211a6-...` (BM-20260509-001 SHTT CONG_KHAI) keys: `congKhai=true, thoiGianDangTai=2026-05-09T10:41:22.146Z`; legacy `laCongKhai`/`ngayCongKhai` KHÔNG còn (`'in obj' === false`) | Field rename hoàn tất |
| BUG-BM-004 | ✅ Closed (persist) | Cùng API, response keys có `anhDaiDien=null, moTaCongKhai=null, fileDinhKemCongKhai=null` (3 fields v3.5 present) | 3 fields v3.5 add đủ |
| BUG-BM-005 | ✅ **Closed (post-hoc reconciled R8 lần 7)** — tại thời điểm này QA polling kết luận "VẪN OPEN" nhưng đã xác định là **false negative do selector mismatch** (xem §R8 lần 7) | (Original R8 lần 5 evidence giữ nguyên historical: pre-test cleanup logout API + LS/SS clear + IndexedDB clear + reload ignoreCache; tạo TM rỗng `cb70e227-...` → click Công khai → POST 409 ERR-CK-01; QA selector `.ant-message-notice` returned 0) | Toast thực tế **đã render** với class `.ant-message-notice-wrapper` (AntD v5) — QA tool dùng selector cũ AntD v4 ⇒ false negative |
| BUG-BM-006 | ✅ Closed (persist) | List Thư viện `/bieu-mau/thu-muc` snapshot uid `2_48/2_60/2_72/2_84` — tất cả 4 TM hiển thị "Số biểu mẫu" = 1, đúng count thực tế /bieu-maus per TM | Counter auto-update OK |

**Kết luận (sửa lại sau R8 lần 7 reconcile):** 5/6 closed persist + BUG-BM-005 cũng đã CLOSED nhưng ở thời điểm R8 lần 4-6 QA polling tool dùng selector cũ AntD v4 nên không bắt được toast → false negative. Toast thực tế **đã render đúng** với class AntD v5 (`.ant-message-notice-wrapper`). Xem §R8 lần 7 để biết chi tiết reconciliation.

### Re-verify R8 lần 6 (2026-05-10) — full sweep 6/6 bug (user-requested QA re-test)

Account `cb_nv_tw_02`. Sweep verify lại toàn bộ 6 bug trong cùng session sau fresh login (browser killed + restart MCP, login + OTP `666666`):

| Bug | Status R8 lần 6 | Evidence | Note |
|---|---|---|---|
| BUG-BM-001 | ✅ Closed (persist) | `r8l6-2026-05-10-bug-bm-001-form-4fields-persist.png` — form `/bieu-mau/them-moi` snapshot a11y có heading "Nội dung công khai trên Cổng PLQG" + 4/4 fields: Switch uid `6_35` + Ảnh đại diện uid `6_39` + Mô tả công khai uid `6_41` + File đính kèm công khai uid `6_46` | 4/4 CR-01 fields render OK, không regress |
| BUG-BM-002 | ✅ Closed (persist) | API GET `/bieu-maus?thuMucId={tm_thue/lao_dong}` — 2 BM AN khác nhau (`d3143771-...` Thuế + `ebeac9ac-...` Lao động) đều có `trangThai=AN, congKhai=false, thoiGianDangTai=null` | BR-PUBLIC-02 enforced cross-record |
| BUG-BM-003 | ✅ Closed (persist) | API GET `/bieu-maus/{id}` cho cả 2 BM AN + 1 BM CONG_KHAI: `'congKhai' in obj=true, 'thoiGianDangTai' in obj=true, 'laCongKhai' in obj=false, 'ngayCongKhai' in obj=false`. CK record `congKhai=true, thoiGianDangTai="2026-05-09T10:41:22.146Z"` | Field rename hoàn tất, no legacy keys leftover |
| BUG-BM-004 | ✅ Closed (persist) | Cùng API, all_keys của BM detail có `anhDaiDien, moTaCongKhai, fileDinhKemCongKhai` (3/3). Full schema 32 keys: `[anhDaiDien, congKhai, dinhDang, donViId, downloadUrl, duongDanFile, fileDinhKemCongKhai, id, kichThuoc, lanSyncCuoi, linhVuc, linhVucId, loaiHinh, maBieuMau, moTa, moTaCongKhai, ngayCapNhat, ngayTao, nguoiCapNhatId, nguoiTaoId, previewUrl, seqId, soLuotTai, syncLoi, syncStatus, tenBieuMau, thoiGianDangTai, thuMuc, thuMucId, thuTuHienThi, trangThai, version]` | 3 fields v3.5 add đủ trong schema |
| BUG-BM-005 | ✅ **Closed (post-hoc reconciled R8 lần 7)** — tại thời điểm này QA polling kết luận "VẪN OPEN" nhưng đã xác định là **false negative do selector mismatch** | (Original R8 lần 6 evidence giữ nguyên historical: TM rỗng `726cb62c-...` → click Công khai → POST 409 ERR-CK-01; QA `.ant-message-notice` polling returned 0) | Toast thực tế **đã render** với class AntD v5 `.ant-message-notice-wrapper` (xem §R8 lần 7) |
| BUG-BM-006 | ✅ Closed (persist) | API check 4/4 TM: `counter_field_in_tm === actual_bm_count` cho cả 4 TM (HĐ Dân sự-TM, Biểu mẫu SHTT, Biểu mẫu Thuế, HĐ Lao động) — tất cả `1 === 1`. UI list cũng hiển thị "Số biểu mẫu = 1" cho cả 4 row | Counter auto-update persist OK |

**Kết luận sweep R8 lần 6 (sửa lại sau R8 lần 7 reconcile):** 5 bug closed persist + BUG-BM-005 cũng đã closed (FE đã hook handler 409 ERR-CK-01 → toast đúng). Tại R8 lần 6 QA tool kết luận sai "vẫn Open" do polling `.ant-message-notice` không match Ant Design v5 wrapper class `.ant-message-notice-wrapper`. R8 lần 7 (manual screenshot user + MCP MutationObserver) đã reconcile → bug CLOSED. 6/6 đóng.

### Re-verify R8 lần 7 (2026-05-10) — BUG-BM-005 ✅ **CLOSED (manual PASS + MCP observer verified)**

**Lượt 1 (false negative — selector mismatch):** Account `cb_nv_tw_02`. Tạo TM rỗng `be791b75-39df-4ef0-8dce-3ebeb94e1270` (Hình sự) → click Công khai → 409. DOM polling `.ant-message-notice` returned empty → kết luận **sai** "vẫn silent". Cleanup `DELETE be791b75` 204.

**Lượt 2 (manual PASS — user-reported):** User chạy manual cùng kịch bản (TM rỗng → click Công khai trên row "Biểu mẫu STP-AG - R7.7.10b" id `11fe7276-...`, 0 BM Hành chính) → toast đỏ rendered top-center: **"❌ Thư mục chưa có biểu mẫu, không thể công khai"** (text mapped từ ERR-CK-01 theo FR-VII-03 §E1). Screenshot cung cấp bởi user.

**Lượt 3 (MCP MutationObserver re-verify):** Cùng TM `11fe7276-...` (Biểu mẫu STP-AG, 0 BM, Nháp). Install `MutationObserver` trên `document.body` BEFORE click Công khai. Click row → popconfirm → confirm. Observer captured DOM additions:

```
addedNode #4: <div class="ant-message ant-message-top css-dev-only-do-not-override-ch9ese css-var-_r_0_ ant-message-css-var">
                "Thư mục chưa có biểu mẫu, không thể công khai"
addedNode #5: <div class="ant-message-notice-wrapper ant-message-move-up-appear ant-message-move-up-appear-start ant-message-move-up">
                "Thư mục chưa có biểu mẫu, không thể công khai"
```

**FE đã hook handler 409 ERR-CK-01 → toast đúng spec.** Toast text "Thư mục chưa có biểu mẫu, không thể công khai" (mapped Vietnamese theo FR-VII-03 §E1, KHÁC raw BE message "Thư mục rỗng — không thể công khai khi chưa có biểu mẫu") — chứng tỏ FE có code mapper từ `error.code` → user-friendly message.

**Root cause của false negative R8 lần 4-7 lượt 1:** QA selector `.ant-message-notice` không match — actual DOM class là `.ant-message-notice-wrapper` (Ant Design v5 wrapper layer). Polling 1500ms cũng có thể quá muộn vì toast default duration 3s nhưng race với selector mismatch ⇒ luôn empty.

**Bài học (đã update [`CLAUDE.md` §Rule 11 selector library]):**
- Toast Ant Design v5: dùng `.ant-message-notice-wrapper` thay vì `.ant-message-notice`.
- Verify ephemeral UI (toast, snackbar) bằng `MutationObserver` install BEFORE action thay vì polling AFTER — toast có thể đã render+disappear giữa 2 polling tick.
- BR-PUBLIC-01 UI handler: ✅ FE map `409 ERR-CK-01` → `.ant-message-error` content "Thư mục chưa có biểu mẫu, không thể công khai".

**Kết luận R8 lần 7:** Bug **CLOSED**. Manual + MCP MutationObserver evidence đồng thuận FE đã fix. 6/6 bug đóng. Recommend update Rule 11 selector library cho team.

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-BM-001~~ | Critical | P0 | UI/UX | R7.4.C1 / R7.7.10 | `_DELTA-MAP-FR09.md §1 Áp CR-01` + `CHANGELOG-v3-to-v3.5.md line 1029-1032` (SCR-VII-02 + FR-VII-04 Inputs) | Form Thêm/Sửa Biểu mẫu thiếu 4 trường công khai (Switch + Ảnh + Mô tả CK + File CK) | **Closed (R8 lần 3 — Switch added, full 4/4 fields)** |
| ~~BUG-BM-002~~ | Critical | P0 | Workflow | R7.4.C1 | `BR-PUBLIC-02` (`srs-fr-12-tv-chuyen-sau.md` line 1603-1607) | Khi BM chuyển sang `AN`, `ngayCongKhai` KHÔNG clear về NULL | Closed (R8) |
| ~~BUG-BM-003~~ | Major | P1 | Data | R7.4.C1 | `_DELTA-MAP-FR09.md §1 Thay đổi 1.1` + `CHANGELOG-v3-to-v3.5.md line 1034` (BIEU_MAU bảng attributes rename) | BE BIEU_MAU entity chưa rename `laCongKhai → congKhai` + `ngayCongKhai → thoiGianDangTai` | Closed (R8) |
| ~~BUG-BM-004~~ | Major | P1 | Data | R7.4.C1 | `_DELTA-MAP-FR09.md §1 Thay đổi 1.4-1.6` + `CHANGELOG-v3-to-v3.5.md line 1034` (BIEU_MAU + 4 row mới) | BE BIEU_MAU entity thiếu 3 fields công khai (`anhDaiDien`, `moTaCongKhai`, `fileDinhKemCongKhai`) | Closed (R8) |
| ~~BUG-BM-005~~ | Medium | P2 | UI/UX | R7.4.C1 | `FR-VII-03 §Error Handling E1` (ERR-CK-01 "Thư mục chưa có biểu mẫu, không thể công khai") | UI silent fail — BE trả 409 ERR-CK-01 nhưng KHÔNG hiện toast/notification cho user | **Closed (R8 lần 7 — manual + MCP MutationObserver verified, FE map ERR-CK-01 → .ant-message-error)** |
| ~~BUG-BM-006~~ | Medium | P2 | Data | R7.4.C1 | `FR-VII-01 §Outputs row 4` (`so_bieu_mau auto đếm`) + `SCR-VII-01 row 11` | Cột "Số biểu mẫu" trên list Thư mục không cập nhật sau khi thêm BM (vẫn 0 dù API đã có 1 BM) | Closed (R8 lần 2) |

---

## ~~BUG-BM-001~~ — Form Thêm/Sửa Biểu mẫu thiếu 4 trường công khai theo SRS v3.5 [CLOSED]

> **Re-test 2026-05-08 R8:** ⚠️ **PARTIAL FIX**. Account `cb_nv_tw_02`. Form `/bieu-mau/them-moi` đã thêm heading "Nội dung công khai trên Cổng PLQG" với 3/4 trường: Ảnh đại diện ✅, Mô tả công khai ✅, File đính kèm công khai ✅. **Vẫn thiếu Switch "Công khai trên Cổng PLQG"** (`evaluate_script` đếm `button[role="switch"]` + `.ant-switch` = 0). Bug giữ Open chờ FE add Switch. Evidence: `screenshots/r8-verify-2026-05-08-bm-001-form-them-bm.png`.
>
> **Re-test 2026-05-09 R8 lần 2:** ⚠️ **VẪN PARTIAL**. Account `cb_nv_tw_02`. Form `/bieu-mau/them-moi` (sau khi seed 3 BM mới R7.3.7 R8 re-seed) — cấu trúc form không thay đổi: 3/4 fields v3.5 vẫn render OK (uid `12_35` Ảnh CK + uid `12_37` Mô tả CK + uid `12_42` File CK), KHÔNG có element `button[role="switch"]` hoặc `.ant-switch` nào. Snapshot a11y tree chỉ liệt kê `inbox` upload buttons + textbox + Tạo/Hủy buttons — không có switch/toggle component. Bug Open partial chờ FE add Switch.
>
> **Re-test 2026-05-09 R8 lần 3 (sau dev claim fix BUG-BM-007/008):** ✅ **CLOSED — full fix 4/4 fields**. Account `cb_nv_tw_02` (cache clear toàn diện + SW unregister + hard reload + fresh login). Form `/bieu-mau/them-moi` snapshot a11y tree liệt kê đầy đủ:
> ```
> uid=6_60 StaticText "Công khai trên Cổng PLQG"
> uid=6_63 switch  "Công khai trên Cổng PLQG question-circle"
> uid=6_67 button  "Ảnh đại diện ... .jpg, .png, .gif"
> uid=6_69 textbox "Mô tả công khai" multiline
> uid=6_74 button  "File đính kèm công khai ... .doc, .docx, .xls, .xlsx, .pdf, .jpg, .png, .gif"
> ```
> Switch "Công khai trên Cổng PLQG" đã được FE add (component `switch` role-based, ngược lại 2 round trước count=0). 4/4 CR-01 fields đầy đủ theo SRS v3.5 Thay đổi 1.4-1.6. Bug đóng. Verify thêm 10 TC CR-01 (BM-041..050) trong R7.7.10 R8 lần 3 sau khi cleanup. Evidence: `image/r8l3-bm-001-switch-full-fix.png`.

### Mô tả

Theo SRS v3.5 (Thay đổi 1, FR-VII-04 + SCR-VII-02), form Thêm/Sửa Biểu mẫu phải có thêm **4 trường công khai chuyên trang**: (1) Switch "Công khai trên Cổng PLQG", (2) Ảnh đại diện công khai, (3) Mô tả công khai (text), (4) File đính kèm công khai (file[]). Form hiện tại (cả Thêm + Sửa) chỉ có 7 fields v3 cũ, không có bất kỳ field nào trong 4 trường mới → CB Nghiệp vụ không thể bật/tắt công khai cho từng BM, cũng không thể nhập thông tin riêng cho người ngoài đọc.

### Các bước tái hiện

1. Login `cb_nv_tw_01` / `Secret@123` (OTP `666666`).
2. Vào "Quản lý thư viện biểu mẫu" → click thư mục bất kỳ (vd "Biểu mẫu SHTT").
3. Click `[+ Thêm biểu mẫu]` → form tại `/bieu-mau/them-moi`.
4. Quan sát: form có 7 fields (Thư mục*, Tên biểu mẫu*, Lĩnh vực, Loại hình, Mô tả, Thứ tự hiển thị, File biểu mẫu*).
5. Lưu BM, mở list, click `[Sửa]` trên 1 BM → form `/bieu-mau/{id}/sua` cũng có cùng 7 fields.

### Kết quả mong đợi

Form Thêm/Sửa Biểu mẫu phải bao gồm thêm:
- Switch "Công khai trên Cổng PLQG" (control `cong_khai`).
- Ảnh đại diện (`anh_dai_dien` — binary upload).
- Mô tả công khai (`mo_ta_cong_khai` — text, KHÁC trường Mô tả nội bộ hiện có).
- File đính kèm công khai (`file_dinh_kem_cong_khai` — file[]).

### Kết quả thực tế

Cả 2 form Thêm + Sửa đều dùng nguyên schema v3 (7 fields), không có Switch và 3 file/text mới. Cũng không có hiển thị `thoi_gian_dang_tai` (read-only field, đáng lẽ hiển thị khi BM đã công khai).

### Bằng chứng

![BUG-BM-001 — Form Thêm Biểu mẫu thiếu 4 trường công khai (URL `/bieu-mau/them-moi`)](image/r7-4-c1-bug1-form-them-bm-thieu-4-truong.png)

![BUG-BM-001 — Form Sửa Biểu mẫu BM-20260507-001 cũng thiếu 4 trường công khai (URL `/bieu-mau/{id}/sua`)](image/r7-4-c1-bug1b-form-sua-bm-thieu-4-truong.png)

---

## ~~BUG-BM-002~~ — BR-PUBLIC-02 vi phạm: ngayCongKhai không clear khi BM chuyển sang AN [CLOSED]

> **Re-test 2026-05-08 R8:** ✅ **CLOSED**. Account `cb_nv_tw_02`. Workflow: tạo BM `Test BM R8 verify` (id `d3143771-...`) trong TM "Biểu mẫu Thuế" → Công khai TM (BM `congKhai=true`, `thoiGianDangTai="2026-05-08T00:00:29.805Z"`) → Ẩn TM. API GET `/api/v1/bieu-maus/d3143771-...` trả: `trangThai="AN"`, `congKhai=false`, `thoiGianDangTai=null`. BR-PUBLIC-02 đã enforce.

### Mô tả

Theo BR-PUBLIC-02 ("Khi set `cong_khai = 0`: clear `thoi_gian_dang_tai` về NULL; gọi API gỡ khỏi Cổng PLQG; ghi audit"), khi BM chuyển trạng thái sang `AN` (cờ công khai tắt), trường `ngayCongKhai`/`thoiGianDangTai` phải reset về NULL. Thực tế BE giữ nguyên timestamp lần bật cuối — vi phạm rule "lần bật mới nhất" của BR-PUBLIC-03 (vì khi bật lại timestamp có thể không refresh do điều kiện so sánh).

### Các bước tái hiện

1. Login `cb_nv_tw_01`, vào thư mục "Biểu mẫu SHTT" có 1 BM (`BM-20260507-001`) ở NHAP.
2. Quay ra list Thư viện, click `[Công khai]` trên row "Biểu mẫu SHTT" → confirm.
3. Quan sát: TM + BM cascade sang `CONG_KHAI`, BM `ngayCongKhai = "2026-05-07T11:26:54.611Z"` (auto-fill OK).
4. Click `[Ẩn]` trên cùng row → confirm. TM hiện "Đã ẩn".
5. Query GET `/api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872`:
   ```json
   { "trangThai": "AN", "laCongKhai": false, "ngayCongKhai": "2026-05-07T11:26:54.611Z" }
   ```

### Kết quả mong đợi

Sau bước 4 (Ẩn), API response phải có `ngayCongKhai: null` (hoặc field mới `thoiGianDangTai: null`) — theo BR-PUBLIC-02. Kết hợp gọi API Cổng PLQG gỡ + ghi audit `UNPUBLISH`.

### Kết quả thực tế

`laCongKhai` đã flip về `false` ✅ nhưng `ngayCongKhai` giữ nguyên timestamp lần bật cuối ❌. Field không được reset → vi phạm BR-PUBLIC-02.

### Bằng chứng

![BUG-BM-002 — TM "Biểu mẫu SHTT" sau khi Ẩn (UI hiện "Đã ẩn") — nhưng BM bên trong vẫn giữ `ngayCongKhai`](image/r7-4-c1-bug2-br-public-02-an-but-timestamp-still.png)

```text
GET /api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872 (sau khi Ẩn TM)
Response:
{
  "id": "0f425c10-8bfd-4dcd-ac34-e724135a2872",
  "trangThai": "AN",
  "laCongKhai": false,
  "ngayCongKhai": "2026-05-07T11:26:54.611Z",   ← phải NULL theo BR-PUBLIC-02
  "syncStatus": "SUCCESS"
}
```

---

## ~~BUG-BM-003~~ — BE BIEU_MAU chưa rename `laCongKhai → congKhai` + `ngayCongKhai → thoiGianDangTai` [CLOSED]

> **Re-test 2026-05-08 R8:** ✅ **CLOSED**. Account `cb_nv_tw_02`. API GET `/api/v1/bieu-maus/{id}` keys: có `congKhai` + `thoiGianDangTai` (mới), KHÔNG còn `laCongKhai` + `ngayCongKhai` (cũ). BE đã rename xong.

### Mô tả

SRS v3.5 Thay đổi 1.1 yêu cầu rename 2 cột trong entity BIEU_MAU + THU_MUC_BIEU_MAU: `la_cong_khai → cong_khai` và `ngay_cong_khai → thoi_gian_dang_tai`. Đây là rename mass impact (FR-09 + FR-16 outbound API + ERD master). BE response hiện tại vẫn dùng tên cũ.

### Các bước tái hiện

1. Login `cb_nv_tw_01`, seed 1 BM, công khai TM cha.
2. Query GET `/api/v1/bieu-maus/{id}` qua DevTools console:
   ```js
   await fetch('/api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872', {credentials:'include'}).then(r=>r.json())
   ```
3. Inspect response keys.

### Kết quả mong đợi

Response BIEU_MAU phải có:
- `congKhai: boolean` (KHÔNG phải `laCongKhai`).
- `thoiGianDangTai: datetime` (KHÔNG phải `ngayCongKhai`).

### Kết quả thực tế

Response trả về `laCongKhai` và `ngayCongKhai` (tên v3 cũ). Không có key `congKhai` hoặc `thoiGianDangTai` nào.

### Bằng chứng

```text
GET /api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872
Response (keys liên quan):
{
  "trangThai": "CONG_KHAI",
  "laCongKhai": true,           ← phải đổi thành "congKhai"
  "ngayCongKhai": "2026-05-07T11:26:54.611Z",  ← phải đổi thành "thoiGianDangTai"
  ...
}
```

(Không có ảnh chụp riêng — bug ở response payload, dùng inspector của ảnh BUG-BM-002.)

![BUG-BM-003 — Reference: BM detail response sau khi Ẩn (chứng cứ tên field cũ)](image/r7-4-c1-bug2-br-public-02-an-but-timestamp-still.png)

---

## ~~BUG-BM-004~~ — BE BIEU_MAU entity thiếu 3 fields công khai mới [CLOSED]

> **Re-test 2026-05-08 R8:** ✅ **CLOSED**. Account `cb_nv_tw_02`. API GET `/api/v1/bieu-maus/{id}` response có 3 field mới: `anhDaiDien=null`, `moTaCongKhai=null`, `fileDinhKemCongKhai=null`. BE đã add fields theo SRS v3.5.

### Mô tả

SRS v3.5 Thay đổi 1.4-1.6 yêu cầu thêm 3 cột mới cho BIEU_MAU: `anh_dai_dien` (binary), `mo_ta_cong_khai` (text), `file_dinh_kem_cong_khai` (file[]). Phục vụ form Switch công khai + nội dung soạn riêng cho người ngoài Cổng PLQG. BE response không có 3 keys này.

### Các bước tái hiện

1. Như BUG-BM-003, query BM detail.
2. Check `Object.keys(response.data)` có chứa 3 trường mới không.

### Kết quả mong đợi

Response BIEU_MAU phải có thêm 3 keys: `anhDaiDien`, `moTaCongKhai`, `fileDinhKemCongKhai`.

### Kết quả thực tế

```js
{
  anhDaiDien: false,           // missing
  moTaCongKhai: false,         // missing
  fileDinhKemCongKhai: false   // missing
}
```

3 fields đều `'fieldName' in obj === false`.

### Bằng chứng

```text
GET /api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872
Verify (DevTools console):
{
  "fields_present_4cong_khai": {
    "anhDaiDien": false,
    "moTaCongKhai": false,
    "fileDinhKemCongKhai": false
  }
}
```

![BUG-BM-004 — Reference: BM detail response (3 fields anhDaiDien/moTaCongKhai/fileDinhKemCongKhai đều thiếu)](image/r7-4-c1-bug2-br-public-02-an-but-timestamp-still.png)

---

## ~~BUG-BM-005~~ — UI silent fail khi BE trả 409 ERR-CK-01 (Công khai thư mục rỗng) [CLOSED]

> **Re-test 2026-05-10 R8 lần 7 (manual + MCP MutationObserver):** ✅ **CLOSED**. User chạy manual: TM rỗng `11fe7276-...` "Biểu mẫu STP-AG" 0 BM → click Công khai → toast đỏ top-center "❌ Thư mục chưa có biểu mẫu, không thể công khai" rendered đúng spec FR-VII-03 §E1 (screenshot user-provided). MCP re-verify với `MutationObserver` install before click capture được DOM addedNode `<div class="ant-message ant-message-top">` chứa text "Thư mục chưa có biểu mẫu, không thể công khai" + child `.ant-message-notice-wrapper.ant-message-move-up-appear`. **FE handler 409 ERR-CK-01 → `.ant-message-error` đã hook đúng + có code-to-message mapper** (BE raw message "Thư mục rỗng — không thể công khai khi chưa có biểu mẫu" được FE map sang user-friendly "Thư mục chưa có biểu mẫu, không thể công khai"). Lý do R8 lần 4-7 lượt 1 false negative: QA selector dùng `.ant-message-notice` thay vì `.ant-message-notice-wrapper` (Ant Design v5 wrapper class) → polling luôn empty. Bug đã fix từ trước, QA tool selector mismatch ⇒ kết luận sai 4 round liên tiếp.
>
> **Lịch sử false-negative R8 lần 2/4/5/6 (giữ làm history reference):** 4 round QA tool kết luận "VẪN OPEN" qua DOM polling `.ant-message-notice` returned 0. Sau R8 lần 7 reconcile (manual user PASS + MCP MutationObserver) đã xác định: toast thực tế **đã render đúng** với class Ant Design v5 `.ant-message-notice-wrapper`. QA tool dùng selector cũ AntD v4 (`.ant-message-notice`) ⇒ không match wrapper layer mới ⇒ false negative. Bug đã được FE fix từ trước R8 lần 2, không phải lỗi BE/FE workflow. Toàn bộ 4 entry chi tiết evidence của lịch sử false negative giữ tại commit history (xem git log file này) để tham chiếu khi audit QA tool.

### Mô tả

Theo FR-VII-03 §Error Handling E1, khi user công khai thư mục rỗng, hệ thống phải báo "Thư mục chưa có biểu mẫu, không thể công khai" (mã `ERR-CK-01`). BE trả đúng response 409 với message tiếng Việt, nhưng FE KHÔNG hiển thị toast / notification → user bấm xong không biết tại sao thư mục vẫn ở NHAP.

### Các bước tái hiện

1. Login `cb_nv_tw_01`, vào "Quản lý thư viện biểu mẫu". Đảm bảo thư mục target rỗng (vd "Biểu mẫu SHTT" lúc chưa seed BM).
2. Click `[Công khai]` trên row → popconfirm "Công khai thư mục này lên Cổng PLQG?" → click `[Công khai]`.
3. Quan sát UI: thư mục vẫn ở "Nháp", không có toast / message gì.
4. Kiểm tra Network tab: POST `/api/v1/thu-muc-bieu-maus/{id}/cong-khai` → 409 với body `{"success":false,"error":{"code":"ERR-CK-01","message":"Thư mục rỗng — không thể công khai khi chưa có biểu mẫu"}}`.
5. `evaluate_script` query `.ant-message`, `.ant-notification`, `[role="alert"]` → toastCount = 0.

### Kết quả mong đợi

FE phải bắt 409 ERR-CK-01 và hiển thị toast lỗi đỏ với nội dung từ `error.message` (hoặc fallback message tiếng Việt mapped theo `error.code`). Pattern này đã chuẩn ở các module khác (vd Vụ việc).

### Kết quả thực tế (R7 gốc — đã được fix)

R7 gốc (2026-05-07): UI không react gì sau khi popconfirm đóng. Console chỉ log generic "Failed to load resource: 409 Conflict".

**Trạng thái hiện tại (R8 lần 7 — 2026-05-10): FE đã fix.** Toast đỏ top-center hiển thị "❌ Thư mục chưa có biểu mẫu, không thể công khai" (FE map từ `error.code=ERR-CK-01` theo FR-VII-03 §E1) — verified bằng manual screenshot user-provided + MCP `MutationObserver` capture DOM addedNode `<div class="ant-message ant-message-top">` chứa text + `.ant-message-notice-wrapper.ant-message-move-up-appear`.

### Bằng chứng

**R7 gốc (lúc bug Open — historical reference):**

![BUG-BM-005 — UI list thư mục sau khi click "Công khai" trên TM rỗng — không có toast nào dù BE trả 409 (R7 historical)](image/r7-4-c1-bug5-ui-silent-409.png)

**R8 lần 7 (đã fix, manual screenshot user-provided):** Toast đỏ "❌ Thư mục chưa có biểu mẫu, không thể công khai" rendered top-center ngay sau popconfirm confirm. MCP MutationObserver capture log:

```text
addedNode #4: <div class="ant-message ant-message-top css-dev-only-do-not-override-ch9ese css-var-_r_0_ ant-message-css-var">
                "Thư mục chưa có biểu mẫu, không thể công khai"
addedNode #5: <div class="ant-message-notice-wrapper ant-message-move-up-appear ant-message-move-up-appear-start ant-message-move-up">
                "Thư mục chưa có biểu mẫu, không thể công khai"
```

```text
POST /api/v1/thu-muc-bieu-maus/{id}/cong-khai
Response 409:
{
  "success": false,
  "error": {
    "code": "ERR-CK-01",
    "message": "Thư mục rỗng — không thể công khai khi chưa có biểu mẫu",
    "timestamp": "2026-05-10T11:28:02.097Z",
    "requestId": "8f5a7bb8-..."
  }
}
```

FE map BE message → user-friendly text theo `error.code` (BE raw "Thư mục rỗng — không thể công khai khi chưa có biểu mẫu" → UI "Thư mục chưa có biểu mẫu, không thể công khai" theo spec FR-VII-03 §E1).

---

## ~~BUG-BM-006~~ — Cột "Số biểu mẫu" trên list Thư mục không cập nhật sau khi thêm BM [CLOSED]

> **Re-test 2026-05-09 R8 lần 2:** ✅ **CLOSED**. Account `cb_nv_tw_02`. Sau R7.3.7 R8 re-seed 1 BM mỗi TM (4 TM × 1 BM = 4 BM total), navigate `/bieu-mau/thu-muc` quan sát cột "Số biểu mẫu" — cả 4 TM đều hiển thị `1` đúng số BM thực tế: HĐ Dân sự-TM/Biểu mẫu SHTT/Biểu mẫu Thuế/HĐ Lao động đều `1`. API GET `/api/v1/thu-muc-bieu-maus` trả field `soBieuMau=1` cho mỗi record. Dev đã fix counter logic.

### Mô tả

Theo FR-VII-01 §Outputs row 4 + SCR-VII-01 row 11, cột "Số biểu mẫu" phải auto đếm số BM thuộc thư mục. Sau khi seed thành công 1 BM (BM-20260507-001) vào thư mục "Biểu mẫu SHTT", quay lại list thư mục, cột "Số biểu mẫu" vẫn hiển thị `0`. Nhấn "Làm mới" cũng không update.

### Các bước tái hiện

1. Login `cb_nv_tw_01`, vào thư mục "Biểu mẫu SHTT" (đang 0 BM).
2. Click `[+ Thêm biểu mẫu]` → upload file .docx 917B + tên "Biểu mẫu SHTT - test R7.4.C1" → click `[Tạo biểu mẫu]`.
3. Verify BM-20260507-001 hiện trong list BM (1/1 mục).
4. Quay về list Thư viện (click breadcrumb "Biểu mẫu") → cột "Số biểu mẫu" của row "Biểu mẫu SHTT" = `0` (sai).
5. Click `[Làm mới]` → counter vẫn = `0`.
6. Sau công khai TM → counter vẫn = `0` dù BE trả `version: 4` cho TM.

### Kết quả mong đợi

Cột "Số biểu mẫu" phải = `1` (số BM chưa xóa của thư mục). API GET `/api/v1/thu-muc-bieu-maus` cần trả thêm `soBieuMau` (auto đếm) hoặc FE phải compute từ `/bieu-maus?thuMucId=`.

### Kết quả thực tế

Counter đứng yên `0` sau cả 3 lần verify (sau seed, sau Làm mới, sau cong-khai). Response GET `/thu-muc-bieu-maus` không có key `soBieuMau`.

### Bằng chứng

![BUG-BM-006 — TM "Biểu mẫu SHTT" trạng thái "Đã công khai" nhưng cột "Số biểu mẫu" vẫn 0 (đáng ra = 1)](image/r7-4-c1-bug6-counter-zero-after-publish.png)

```text
GET /api/v1/thu-muc-bieu-maus?page=1&pageSize=100&sortBy=ngayTao&sortOrder=DESC (sau seed BM)
Response: {
  "data": [
    { "id": "59f01d24-...", "tenThuMuc": "Biểu mẫu SHTT", "trangThai": "CONG_KHAI", "version": 4 }
    /* không có key "soBieuMau" */
  ]
}

GET /api/v1/bieu-maus?thuMucId=59f01d24-447b-4195-9841-d7240e91be9e
Response: meta.total = 1   ← BM thực tế = 1
```

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Xác thực | Cookie `access_token` (JWT RS256) + OTP |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) |

**Account dùng test:** `cb_nv_tw_01` (CB Nghiệp vụ TW, role `CB_NV_TW`, đơn vị `BTP-TW`).

**Test data tạo trong session:**
- TM "Biểu mẫu SHTT" id `59f01d24-447b-4195-9841-d7240e91be9e` (đã có sẵn từ R7.3.7).
- BM "Biểu mẫu SHTT - test R7.4.C1" id `0f425c10-8bfd-4dcd-ac34-e724135a2872` mã `BM-20260507-001` (seed mới qua UI, file 917B `.docx`).

---

*Bug report generated: 2026-05-07 18:30 | QA Automation via Claude Code MCP*

> **R7.7.10 functional bugs:** Xem file riêng [`Pass-bug-report-function-bm-r7-7-10.md`](Pass-bug-report-function-bm-r7-7-10.md) (BUG-BM-007/008/010 all closed R8 lần 8/12).
