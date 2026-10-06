# Đối chiếu điều kiện — QLBMHD_09 (Tải tệp bị gián đoạn — thông báo)

Loại: **Validation upload — thông báo khi upload gián đoạn (mất mạng).** Đối tác báo thông báo "sai thiết kế".

## Bảng đối chiếu điều kiện

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLBMHD_09.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | CB Nghiệp vụ upload biểu mẫu | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Màn / trường upload | Form Thêm biểu mẫu, trường File biểu mẫu | Đúng form `/bieu-mau/them-moi`, trường File biểu mẫu | Không |
| Điều kiện gián đoạn | Upload mất mạng / gián đoạn | Chrome DevTools `emulate Offline` (mất mạng) khi upload | Không |
| Cách đo thông báo | Quan sát toast UI | `toast-capture.js` observer + trạng thái upload item | Không |

**0 GAP** cho điều kiện "mất mạng khi upload". (Xem caveat: mình test Offline TRƯỚC upload, chưa phải ngắt-giữa-chừng — ghi rõ ở audit.)

## Cổng 3 — SRS vs web (dạng bullet)

- SRS EC-01 (`srs-fr-09:381`): "Upload bị ngắt giữa chừng (mất mạng) → Dọn blob mồ côi → ERR-BM-06 'Upload bị gián đoạn, vui lòng thử lại'".
- Web đo được: upload khi Offline → toast "Không kết nối được máy chủ.", upload item `ant-upload-list-item-error`, file không đính kèm (1 request POST upload thất bại).
- Đối chiếu: app CÓ báo lỗi + đánh dấu upload thất bại khi mất mạng (đúng ý EC-01), khác **cách diễn đạt** so chuỗi ERR-BM-06; vế "dọn blob mồ côi" + ngắt-giữa-chừng thật không kiểm được ở tầng UI.

## Verdict

- App xử lý + báo lỗi khi upload mất mạng (nghiệp vụ đạt), wording khác ERR-BM-06 + còn phần chưa kiểm được (ngắt-giữa-chừng, dọn blob).
- → **BA confirm**: BA quyết wording ERR-BM-06; Dev xác nhận xử lý ngắt-giữa-chừng + dọn blob mồ côi.

Evidence: [`../reverify-audit/QLBMHD_09/toast-capture.md`](../reverify-audit/QLBMHD_09/toast-capture.md).
