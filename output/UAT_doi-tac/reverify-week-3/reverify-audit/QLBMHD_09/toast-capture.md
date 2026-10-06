# QLBMHD_09 (row 102) — Tải tệp bị gián đoạn (mất mạng) — đo thông báo

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - TW, BTP·TW).
- **Màn:** Form Thêm biểu mẫu (`/bieu-mau/them-moi`), trường "File biểu mẫu".
- **Mô phỏng gián đoạn:** Chrome DevTools `emulate networkConditions=Offline` (mất mạng) → upload `valid.docx`.

## Kết quả đo (2026-07-20)

```json
{ "SO_REQUEST": 1, "request": ["POST /api/v1/bieu-maus/upload"], "SO_TOAST": 1,
  "chu_toast": ["Không kết nối được máy chủ."],
  "uploadItemClasses": ["ant-upload-list-item ant-upload-list-item-error"] }
```

- Khi mất mạng, app thử gọi upload → thất bại → toast **"Không kết nối được máy chủ."**, upload item chuyển trạng thái **lỗi** (`ant-upload-list-item-error`), file KHÔNG đính kèm. → App CÓ xử lý + báo lỗi khi upload không tới được server.

## Đối chiếu SRS

- EC-01 (`srs-fr-09:381`): "Upload bị ngắt giữa chừng (mất mạng) → Dọn blob mồ côi trong storage. **ERR-BM-06 'Upload bị gián đoạn, vui lòng thử lại'**".
- App: "Không kết nối được máy chủ." — truyền tải đúng ý "không kết nối được / mất mạng", khác **cách diễn đạt** so với chuỗi ERR-BM-06.

## Caveat (ghi trung thực)

- Mình mô phỏng **Offline TRƯỚC khi upload bắt đầu** (không tới server) — chưa phải **ngắt GIỮA CHỪNG** khi 1 phần file đã lên (path "dọn blob mồ côi" của EC-01 chỉ xảy ra khi đã có phần dữ liệu lên server). Vế "dọn blob mồ côi" không kiểm được ở tầng UI.

## So sánh evidence đối tác

- Đối tác (env `htpldn-uat.ospgroup.vn`): thông báo generic "Upload file thất bại. Vui lòng thử lại." (không nêu gián đoạn/kết nối).
- Env kiểm thử: "Không kết nối được máy chủ." — rõ nguyên nhân kết nối hơn.

## Verdict

- App có báo lỗi kết nối khi upload mất mạng (truyền tải đúng ý EC-01), nhưng wording khác chuỗi ERR-BM-06; ngoài ra không kiểm được path ngắt-giữa-chừng thật + dọn blob mồ côi.
- → **BA confirm**: BA quyết có bắt buộc đúng wording ERR-BM-06 "Upload bị gián đoạn, vui lòng thử lại" không; Dev xác nhận xử lý ngắt-giữa-chừng + dọn blob mồ côi.
