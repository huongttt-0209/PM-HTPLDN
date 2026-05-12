# Bug Report — Thư viện Biểu mẫu (FR-VII v3.5) — R7.7.10 Functional

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người test** | QA Automation (Claude Code MCP) |
| **Ngày** | 2026-05-07 13:54:12 (approx — git commit time) |
| **Loại test** | Functional 47 TC (CRUD + filter + file upload + preview + download) |
| **Round** | R7.7.10 |
| **Tài liệu tham chiếu** | [`output/funtion/7.9-bieu-mau.md`](../../../../funtion/7.9-bieu-mau.md) (47 TC) · [`srs-update-2026-5-5/_DELTA-MAP-FR09.md`](../../../../../input/srs-update-2026-5-5/_DELTA-MAP-FR09.md) · [`functional-test-report-r7-7-10-bm.md`](../../functional/bieu-mau/functional-test-report-r7-7-10-bm.md) |

---

## Tổng hợp

Phát hiện **3** lỗi trong functional test R7.7.10 (preview/download MinIO config sai + UI silent reject upload file invalid + 3 trường công khai không ẩn theo Switch). **2/3 đóng tại R8 lần 8 (2026-05-11); BUG-BM-010 mới log từ test 10 CR-01.** Các bug khác từ workflow đã log riêng tại [`Pass-bug-report-flow-bm-r7-4-c1.md`](Pass-bug-report-flow-bm-r7-4-c1.md) (6 bugs BUG-BM-001..006).

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial |
|------|----------|-------|--------|-------|---------|
| 3    | 1        | 0     | 2      | 0     | 0       |

### Status sau R8 lần 11 (2026-05-11)

| Đóng | Còn open | % đóng |
|---|---|---|
| **2/3** (BUG-BM-007 + BUG-BM-008) | 1/3 (BUG-BM-010 Medium — 3 fields visibility, **VẪN reproduced R8 lần 11**) | **67%** |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-BM-007~~ | Critical | P0 | Integration | BM-007 + BM-008 | `FR-VII-04 §Processing — Xem trực tuyến` + `§Processing — Tải về` | Preview + Download BM dùng MinIO presigned URL trỏ `localhost:9000` → user browser không kết nối được (`ERR_CONNECTION_REFUSED`) | **Closed (R8 lần 8 — BE đổi `MINIO_PUBLIC_HOST` sang `103.172.236.130:9000`, fetch status=200, content_length=917, 36ms)** |
| ~~BUG-BM-008~~ | Medium | P2 | UI/UX | BM-016 | `FR-VII-04 §Error Handling E1` (ERR-BM-01 "Chỉ chấp nhận file doc, docx, xls, xlsx") | Form Thêm BM upload file `.txt` → FE silent rejected (ẩn file khỏi upload list) nhưng KHÔNG hiển thị toast/error message → user không biết file không hợp lệ | **Closed (R8 lần 8 — MCP MutationObserver verified, toast `.ant-message-notice-wrapper` "Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx" rendered)** |
| BUG-BM-010 | Medium | P2 | UI/UX | BM-041 | `7.9-bieu-mau.md` line 122 (BM-041) + line 147 ("Switch OFF... → 3 trường ẩn") | Form Thêm BM — 3 trường công khai (Ảnh đại diện / Mô tả công khai / File đính kèm công khai) VẪN visible khi Switch "Công khai trên Cổng PLQG" OFF, vi phạm spec BM-041 "Switch công khai OFF → 3 trường (ảnh/mô tả/file) ẨN khỏi form" | **Open (R8 lần 11 reproduced — Switch ON/OFF không đổi visibility, same heights 203/128/203px both states)** |

---

## ~~BUG-BM-007~~ — Preview + Download Biểu mẫu trỏ MinIO `localhost:9000` không reachable [CLOSED]

> **Re-test 2026-05-11 R8 lần 8 (sau dev confirm fix MinIO config):** ✅ **CLOSED**. Account `cb_nv_tw_02` (kill all chrome MCP + relaunch fresh + LS/SS clear + fresh login + OTP `666666`). BM-20260509-001 cùng id `8a7211a6-7368-49d1-bb39-e9b5078b1037`. In-browser `fetch('/api/v1/bieu-maus/{id}/download', {credentials:'include'})` với `redirect:'follow'` → trả `status=200, redirected=true, final_url_host=103.172.236.130:9000, content_type=application/vnd.openxmlformats-officedocument.wordprocessingml.document, content_length=917, ms=36`. BE đã đổi `MINIO_PUBLIC_HOST` từ `localhost:9000` sang `103.172.236.130:9000` (public IP của server). Presigned URL signature mới có `X-Amz-Date=20260511T031816Z, X-Amz-Credential=htpldn_minio%2F20260511%2Fus-east-1%2Fs3%2Faws4_request`. Preview + Download giờ hoạt động cho mọi BM. Bug đóng.
>
> **Re-test 2026-05-08 R8:** ❌ **VẪN OPEN**. Account `cb_nv_tw_02`. Tạo BM mới + click Xem trước → BE redirect 302 đến `http://localhost:9000/htpldn/...?X-Amz-...` → `net::ERR_CONNECTION_REFUSED`. Cấu hình MinIO public host vẫn sai. Evidence: `screenshots/r8-verify-2026-05-08-bm-007-localhost-still.png` + network reqid 227-230.
>
> **Re-test 2026-05-09 R8 lần 2:** ❌ **VẪN OPEN**. Account `cb_nv_tw_02`. BM-20260509-001 (`8a7211a6-7368-49d1-bb39-e9b5078b1037`, TM SHTT đã CONG_KHAI sau R7.4.C1 R8 lần 2). GET `/api/v1/bieu-maus/{id}/download` → 302 → `http://localhost:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/f39d316d-bf34-4f8b-9d35-3f989ada4c8f/test-bm-r7-4-c1.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&...`. 2 lần redirect gặp `net::ERR_ABORTED` + `net::ERR_CONNECTION_REFUSED`. MinIO `MINIO_PUBLIC_HOST` vẫn `localhost:9000` chưa đổi. Evidence: `image/r8-bm-007-localhost-still-r8l2.png` + reqid 464-467.
>
> **Re-test 2026-05-09 R8 lần 3 (sau dev claim fix):** ❌ **VẪN OPEN — dev claim sai**. Account `cb_nv_tw_02` (cache clear toàn diện + SW unregister + hard reload + fresh login per memory `feedback_clear_cache_before_verify_fe_fix`). BM-20260509-001 cùng id. GET `/api/v1/bieu-maus/{id}/download` reqid=804 → 302 → reqid=805 GET **`http://localhost:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/f39d316d-bf34-4f8b-9d35-3f989ada4c8f/test-bm-r7-4-c1.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260509T125509Z&...`** → `net::ERR_ABORTED`. Cấu hình BE `MINIO_PUBLIC_HOST` chưa được đổi từ `localhost:9000` sang IP server `103.172.236.130:9000`. Bug giữ Open chờ dev verify lại config thật + restart service.
>
> **Re-test 2026-05-10 R8 lần 4 (curl direct verify, bypass CORS):** ❌ **VẪN OPEN — confirm 4 round liên tiếp**. Login `cb_nv_tw_02` qua API `/auth/login` + `/auth/verify-otp` (OTP `666666`) → cookie session. Curl `GET /api/v1/bieu-maus/8a7211a6-7368-49d1-bb39-e9b5078b1037/download` với `--max-redirs 0` để inspect Location header trực tiếp:
> ```text
> HTTP/1.1 302 Found
> location: http://localhost:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/f39d316d-bf34-4f8b-9d35-3f989ada4c8f/test-bm-r7-4-c1.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=htpldn_minio%2F20260509%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260509T192131Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=5d66f3f124cfd4ec468a1e98495edaa8f802df9a174f7a3f035ef595ec14a56a
> content-type: text/plain; charset=utf-8
> Found. Redirecting to http://localhost:9000/htpldn/...
> ```
> Cross-verify qua browser fetch `redirect: 'follow'` → `TypeError: Failed to fetch` (target unreachable từ user browser). Performance API resource entry `name=.../download type=fetch status=0`. **Identical pattern 4 round** (R8/R8 lần 2/R8 lần 3/R8 lần 4). BE `MINIO_PUBLIC_HOST=localhost:9000` config chưa đổi. Cần dev sửa env var + restart BE service. Bug giữ Open Critical P0.

### Mô tả

Khi user click "Xem trước" hoặc "Tải về" trên BM, FE gọi BE endpoint `/api/v1/bieu-maus/{id}/download` → BE trả 302 redirect đến MinIO presigned URL bắt đầu bằng `http://localhost:9000/htpldn/...?X-Amz-Algorithm=...`. Trên trình duyệt user thực, `localhost:9000` trỏ về máy user (không có MinIO), nên kết nối refused → preview hiện "Không kết nối được máy chủ", download thất bại. Cấu hình MinIO public host bị sai trên BE.

### Các bước tái hiện

1. Login `cb_nv_tw_01` → vào `/bieu-mau/danh-sach?thuMucId=...` (TM có ≥1 BM).
2. Click vào tên BM → mở chi tiết `/bieu-mau/{id}`.
3. Click `[Xem trước]` → modal "Xem trước biểu mẫu" mở, content area hiện thông báo lỗi "Không kết nối được máy chủ".
4. Click `[Tải về]` → không có file nào được tải. Network tab thấy `HEAD /api/v1/bieu-maus/{id}/download` → 302 → `HEAD http://localhost:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/.../test-bm-r7-4-c1.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&...` → `net::ERR_CONNECTION_REFUSED`.

### Kết quả mong đợi

BE phải dùng MinIO public host (vd `http://103.172.236.130:9000/...` hoặc subdomain `s3.htpldn.local`) thay vì `localhost`. URL presigned phải reachable từ user browser. Preview + Download phải hoạt động cho cả file `.docx` (917B test).

### Kết quả thực tế (R7 gốc — đã được fix tại R8 lần 8)

R7 gốc (2026-05-07): Preview hiện "Không kết nối được máy chủ". Download không trigger được file. Cả 2 chức năng broken.

**Trạng thái hiện tại (R8 lần 8 — 2026-05-11): BE đã fix `MINIO_PUBLIC_HOST`.** Fetch `/api/v1/bieu-maus/{id}/download` → 302 → MinIO presigned URL host `103.172.236.130:9000` (public IP server) → status 200, content-type `application/vnd.openxmlformats...`, content-length 917 đúng size file. Preview + Download hoạt động.

### Bằng chứng

**R7 gốc (historical — bug Open):**

![BUG-BM-007 — Preview modal hiện "Không kết nối được máy chủ" sau khi click Xem trước (R7 historical)](image/r7-7-10-bm-007-preview-fail-localhost.png)

**R8 lần 8 (đã fix):**

```text
GET /api/v1/bieu-maus/8a7211a6-7368-49d1-bb39-e9b5078b1037/download
→ 302 → http://103.172.236.130:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/f39d316d-bf34-4f8b-9d35-3f989ada4c8f/test-bm-r7-4-c1.docx
       ?X-Amz-Algorithm=AWS4-HMAC-SHA256
       &X-Amz-Credential=htpldn_minio%2F20260511%2Fus-east-1%2Fs3%2Faws4_request
       &X-Amz-Date=20260511T031816Z&X-Amz-Expires=300
       &X-Amz-SignedHeaders=host
       &X-Amz-Signature=8f22ae7e...

Response: 200 OK, content-type=application/vnd.openxmlformats-officedocument.wordprocessingml.document, content-length=917, elapsed=36ms
```

```text
GET /api/v1/bieu-maus/0f425c10-8bfd-4dcd-ac34-e724135a2872/download
→ 302 Found
Location: http://localhost:9000/htpldn/00000000-0000-4000-8000-000000000001/2026/05/d303f3e8-162f-48f8-82a3-153d04db805e/test-bm-r7-4-c1.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=htpldn_minio%2F20260507%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20260507T114850Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=cc448f4...

HEAD http://localhost:9000/...
→ net::ERR_CONNECTION_REFUSED  (browser của user, không có MinIO)
```

---

## ~~BUG-BM-008~~ — Form Thêm BM silent reject file invalid (không có toast/error) [CLOSED]

> **Re-test 2026-05-11 R8 lần 8 (MCP MutationObserver verify — sau bài học BUG-BM-005 false negative):** ✅ **CLOSED**. Account `cb_nv_tw_02` (kill chrome + fresh launch + LS/SS clear + fresh login). Form `/bieu-mau/them-moi` trong TM "Biểu mẫu STP-AG - R7.7.10b" (id `11fe7276-...`). **Install `MutationObserver` trên `document.body` BEFORE upload action.** Upload `test-bm-invalid.txt` 36B qua MCP `upload_file` uid `6_22`. Sleep 2500ms rồi inspect captured addedNodes:
> ```json
> [
>   {"tag":"DIV","cls":"ant-message ant-message-top css-dev-only-do-not-override-ch9ese css-var-_r_0_ ant-message-css-var",
>    "text":"Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx"},
>   {"tag":"DIV","cls":"ant-message-notice-wrapper ant-message-move-up-appear ant-message-move-up-appear-start ant-message-move-up",
>    "text":"Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx"}
> ]
> ```
> Toast đã render đúng spec FR-VII-04 §E1 ERR-BM-01. Tại thời điểm sleep-end DOM check (2500ms), toast đã auto-dismiss (`.ant-message-notice-wrapper` count=0) — chứng tỏ R8 lần 2/3/4 polling DOM AFTER action miss vì toast đã biến mất. **Root cause pattern false negative identical với BUG-BM-005:** (a) selector `.ant-message-notice` sai (AntD v5 dùng `.ant-message-notice-wrapper`), (b) polling sau action race với toast auto-dismiss 3s. Evidence: `image/r8l8-2026-05-11-bug-bm-008-toast-fixed-after-form.png` (form state sau toast biến mất — file `.txt` không hiện trong upload list).
>
> **Re-test 2026-05-09 R8 lần 2:** ❌ **VẪN OPEN**. Account `cb_nv_tw_02`. Form `/bieu-mau/them-moi`. Upload file `test-bm-invalid.txt` (36B) qua field "File biểu mẫu" (uid `45_58`). DOM check 1.5s sau upload: `toastCount=0, toastTexts=[], errCount=0, errTexts=[], fileItemCount=0, fileItems=[]`. FE filter client-side, file không xuất hiện trong upload list, KHÔNG có toast/notification/inline error. Evidence: `image/r8-bm-008-silent-reject-r8l2.png`.
>
> **Re-test 2026-05-09 R8 lần 3 (sau dev claim fix):** ❌ **VẪN OPEN — dev claim sai**. Account `cb_nv_tw_02` (cache clear toàn diện trước test). Form `/bieu-mau/them-moi` (verify BUG-BM-001 đã add Switch CR-01). Upload `test-bm-invalid.txt` 36B qua uid `6_58`. DOM check 2s sau: `toastCount=0, toastTexts=[], errCount=0, errTexts=[], fileItemCount=0, fileItems=[], allMessages=[]` (kiểm cả `.ant-message-notice` + `.ant-notification-notice`). FE vẫn silent reject — không add toast `ERR-BM-01` "Chỉ chấp nhận file doc, docx, xls, xlsx". Evidence: `image/r8l3-bm-008-still-silent.png`.
>
> **Re-test 2026-05-10 R8 lần 4:** ❌ **VẪN OPEN — confirm 4 round liên tiếp**. Account `cb_nv_tw_02` (kill chrome + restart browser + fresh OTP login). Form `/bieu-mau/them-moi` (BUG-BM-001 đã add Switch CR-01 verify R8 lần 3). Upload `test-bm-invalid-r4.txt` 57B (single line text content) vào "File biểu mẫu" qua MCP `upload_file` uid `34_30`. DOM check 2s sau:
> ```json
> {
>   "toastCount": 0, "toastTexts": [],
>   "errCount": 0, "errTexts": [],
>   "fileItemCount": 0, "fileItems": [],
>   "allMessageClassCount": 0,
>   "bodyHasErrBM01": false,
>   "bodyHasInvalidMsg": true,    ← từ static label "Chỉ chấp nhận: .doc, .docx, .xls, .xlsx" của upload area, KHÔNG phải toast lỗi
>   "bodyHasFilename": false      ← file `test-bm-invalid-r4.txt` không hiện trong upload list
> }
> ```
> File bị filter client-side (fileItemCount=0, bodyHasFilename=false), KHÔNG có toast/notification/inline error nào. `.ant-message-notice` count = 0, `.ant-notification-notice` count = 0. Pattern silent fail identical 4 round (R8/R8 lần 2/R8 lần 3/R8 lần 4). FE chưa hook beforeUpload → message.error(`ERR-BM-01`). Evidence: `image/r8l4-reverify-2026-05-10-bug-bm-008-still-silent.png`.

### Mô tả

Theo FR-VII-04 §Error Handling E1, khi user upload file sai định dạng (vd `.txt`, `.pdf`, `.exe`), hệ thống phải báo lỗi `ERR-BM-01` "Chỉ chấp nhận file doc, docx, xls, xlsx". Thực tế FE filter client-side: file invalid không xuất hiện trong upload list, nhưng KHÔNG hiển thị toast/notification/inline error nào → user không biết file đã bị reject, có thể nghĩ là upload chậm và bấm "Tạo biểu mẫu" → form lỗi 422 không clear cause.

### Các bước tái hiện

1. Login `cb_nv_tw_01` → vào `/bieu-mau/them-moi`.
2. Click vùng kéo-thả file (label "Kéo thả hoặc click để chọn file. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx — Tối đa 20MB") → upload file `.txt` (vd `test-bm-invalid.txt` 36 bytes).
3. Quan sát: vùng upload trống, không có file item, không có toast lỗi, không có inline error message.
4. `evaluate_script` query `.ant-message`, `.ant-notification`, `.ant-upload-list-item` → toastCount=0, fileItems=[].

### Kết quả mong đợi

FE phải hiển thị toast/notification màu đỏ với message `ERR-BM-01` ("Chỉ chấp nhận file doc, docx, xls, xlsx") khi user upload file sai format. Tương tự cho file vượt 20MB → `ERR-BM-02`.

### Kết quả thực tế (R7 gốc — đã được fix tại R8 lần 8)

R7 gốc + R8 lần 2/3/4 (2026-05-07 → 2026-05-10): UI polling `.ant-message-notice` returned 0, conclude "silent fail". Sau bài học BUG-BM-005 false negative (selector mismatch + polling timing race), retest với MutationObserver xác nhận FE thực tế đã hook beforeUpload → `message.error("Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx")`. Toast `.ant-message-notice-wrapper` (AntD v5) render đúng top-center, auto-dismiss sau ~3s.

### Bằng chứng

**R7 gốc (historical — bug Open):**

![BUG-BM-008 — Sau khi upload `test-bm-invalid.txt`, vùng upload vẫn trống, không có toast lỗi nào (R7 historical)](image/r7-7-10-bm-016-silent-reject-txt.png)

**R8 lần 8 (đã fix — MCP MutationObserver capture):**

```text
addedNode #1: <div class="ant-message ant-message-top css-dev-only-do-not-override-ch9ese css-var-_r_0_ ant-message-css-var">
                "Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx"
addedNode #2: <div class="ant-message-notice-wrapper ant-message-move-up-appear ant-message-move-up-appear-start ant-message-move-up">
                "Định dạng không hỗ trợ: .txt. Chỉ chấp nhận: .doc, .docx, .xls, .xlsx"
```

![BUG-BM-008 R8 lần 8 — Form state sau khi upload `.txt` bị reject (toast đã auto-dismiss, file không trong list)](image/r8l8-2026-05-11-bug-bm-008-toast-fixed-after-form.png)

```text
DOM check sau upload .txt:
{
  toastCount: 0,
  toastTexts: [],
  errCount: 0,
  errTexts: [],
  fileItems: [],          ← file đã bị filter client-side
  bodyHasInvalid: true    ← chỉ là static label, không phải error msg
}
```

---

## BUG-BM-010 — Form Thêm BM: 3 trường công khai visible khi Switch OFF (vi phạm BM-041)

> **Re-test 2026-05-11 R8 lần 11:** ❌ **VẪN OPEN — reproduce 100%, không có fix giữa R8 lần 8 và R8 lần 11.** Account `cb_nv_tw_02` (kill chrome + fresh launch + fresh login + OTP `666666`). Navigate `/bieu-mau/them-moi`. DOM check Switch + 3 fields:
> ```json
> Switch OFF (default):
>   { ariaChecked: "false", hasCheckedClass: false }
>   "Ảnh đại diện":          { visible: true, display: "block", height: 203px }
>   "Mô tả công khai":       { visible: true, display: "block", height: 128px }
>   "File đính kèm công khai": { visible: true, display: "block", height: 203px }
>
> Click Switch → toggle ON:
>   { ariaChecked: "true", hasCheckedClass: true }
>   "Ảnh đại diện":          { visible: true, height: 203px }  ← KHÔNG đổi
>   "Mô tả công khai":       { visible: true, height: 128px }  ← KHÔNG đổi
>   "File đính kèm công khai": { visible: true, height: 203px }  ← KHÔNG đổi
> ```
> Switch state thay đổi đúng (`aria-checked`/`ant-switch-checked` class). Nhưng 3 trường height/visibility **identical giữa Switch ON và OFF** — FE chưa hook conditional render based on Switch state. Bug NOT fixed sau ~3 ngày kể từ R8 lần 8 (2026-05-11 sáng). Evidence: `image/r8l11-2026-05-11-bug-bm-010-still-3fields-visible-switch-off.png`.
>
> **Bonus fix detected (separate, non-bug related):** UI hint "Ảnh đại diện" upload area changed from `Dung lượng tối đa: 20MB` (R8 lần 8 observation) → `Dung lượng tối đa: 5MB` (R8 lần 11 actual). Match spec BM-048 `anh_dai_dien ≤5MB`. Observation closed.
>
> **Recommend dev fix BUG-BM-010:** Wrap 3 Form.Item bằng conditional render based on `Form.useWatch('congKhai')`:
> ```jsx
> const congKhai = Form.useWatch('congKhai', form);
> {congKhai && (
>   <>
>     <Form.Item name="anhDaiDien" label="Ảnh đại diện">...</Form.Item>
>     <Form.Item name="moTaCongKhai" label="Mô tả công khai">...</Form.Item>
>     <Form.Item name="fileDinhKemCongKhai" label="File đính kèm công khai">...</Form.Item>
>   </>
> )}
> ```
> Clear value qua `form.resetFields(['anhDaiDien','moTaCongKhai','fileDinhKemCongKhai'])` trong `useEffect(() => { if (!congKhai) form.resetFields(...) }, [congKhai])` để match spec line 147 "tắt → ẩn **+ clear value khi save**".

### Mô tả

Theo spec test plan [`7.9-bieu-mau.md` line 122 BM-041](../../../../funtion/7.9-bieu-mau.md) + line 147 ghi chú thực thi: "Switch OFF mặc định khi tạo mới. **Bật → 3 trường (ảnh đại diện / mô tả công khai / file đính kèm công khai) hiện ngay; tắt → ẩn + clear value khi save.**" Thực tế form `/bieu-mau/them-moi` render 3 trường này **luôn visible** bất kể Switch ON/OFF — vi phạm spec CR-01 SCR-VII-02.

### Các bước tái hiện

1. Login `cb_nv_tw_02` → vào `/bieu-mau/them-moi`.
2. Quan sát Switch "Công khai trên Cổng PLQG" — default OFF (`aria-checked=false`, không có class `ant-switch-checked`).
3. Quan sát 3 trường: "Ảnh đại diện", "Mô tả công khai", "File đính kèm công khai" — **VẪN visible** dù Switch OFF.
4. `evaluate_script` query 3 `.ant-form-item` chứa các label trên — đều có `display=block, visibility=visible, height>0, offsetParent !== null`.
5. Click Switch ON → 3 trường KHÔNG thay đổi (cũng visible). Không có animation hide/show.

### Kết quả mong đợi

- Switch OFF (default): 3 trường (`anhDaiDien` upload / `moTaCongKhai` textbox / `fileDinhKemCongKhai` upload) PHẢI ẨN hoàn toàn (display:none hoặc unmount).
- Switch ON: 3 trường hiện + `thoiGianDangTai` auto-fill khi save.
- Switch OFF sau khi đã có value: clear value khi save (BE clear `anhDaiDien=null, moTaCongKhai=null, fileDinhKemCongKhai=null` theo BR-PUBLIC-02 analog).

### Kết quả thực tế

```json
{
  "switch": { "ariaChecked": "false", "antSwitchCheckedClass": false },
  "fieldStates": [
    { "label": "Ảnh đại diện",         "visible": true, "display": "block" },
    { "label": "Mô tả công khai",      "visible": true, "display": "block" },
    { "label": "File đính kèm công khai", "visible": true, "display": "block" }
  ]
}
```

3 trường visible khi Switch OFF — `display=block` (không phải `none`), `offsetParent !== null` (in DOM render).

### Bằng chứng

![BUG-BM-010 — Form Thêm BM với Switch OFF nhưng 3 trường công khai vẫn visible](image/r8l8-2026-05-11-bug-bm-010-3fields-visible-when-switch-off.png)

### Impact

- UX: User nhập dữ liệu vào 3 trường mà không biết Switch OFF → tạo BM thành công nhưng `anhDaiDien/moTaCongKhai/fileDinhKemCongKhai` không được lưu (hoặc lưu nhưng không hiển thị Cổng PLQG vì `congKhai=false`).
- Logic vô nghĩa: Form cho phép nhập trường công khai khi không công khai → user confusion.

### Recommend fix

FE form `BieuMauForm.tsx`: thêm conditional render dựa trên Switch state:
```jsx
{switchCongKhai && (
  <>
    <Form.Item label="Ảnh đại diện" ... />
    <Form.Item label="Mô tả công khai" ... />
    <Form.Item label="File đính kèm công khai" ... />
  </>
)}
```

Hoặc dùng `style={{ display: switchCongKhai ? 'block' : 'none' }}` nếu muốn giữ state value trong React Hook Form. Clear value trong `useEffect` khi Switch toggle OFF.

---

## Phụ lục — Môi trường test

| Thành phần | Giá trị |
|------------|---------|
| URL ứng dụng | http://103.172.236.130:3000/ |
| OTP login | `666666` (bypass) |
| MailHog (OTP inbox) | http://103.172.236.130:8025 |
| API base | http://103.172.236.130:3000/api/v1 |
| Frontend | React + Vite + Ant Design |
| Storage | MinIO (config sai — `localhost:9000` thay vì public host) |
| Tool test | Chrome DevTools MCP (`mcp__chrome-devtools__*`) |

**Account dùng test:** `cb_nv_tw_01` (CB Nghiệp vụ TW, role `CB_NV_TW`, đơn vị `BTP-TW`).

**Test data dùng:** BM-20260507-001 "Biểu mẫu SHTT - test R7.4.C1" id `0f425c10-8bfd-4dcd-ac34-e724135a2872` (file `test-bm-r7-4-c1.docx` 917B từ R7.4.C1) + file invalid `test-bm-invalid.txt` 36B (tạo riêng cho BM-016).

> **Liên quan:** Workflow bugs (BUG-BM-001..006) đã log tại [`Pass-bug-report-flow-bm-r7-4-c1.md`](Pass-bug-report-flow-bm-r7-4-c1.md). 10 TC CR-01 (BM-041..050) BLOCKED do BUG-BM-001 (form thiếu 4 trường công khai).

---

*Bug report generated: 2026-05-07 19:00 | QA Automation via Claude Code MCP*
