# QLTMBMHD_07 — Đo thông báo trùng tên (bộ bắt toast dùng chung `tools/toast-capture.js`)

**Ngày đo:** 2026-07-20 · **Tài khoản:** cbnv_tw (CB Nghiệp vụ - Trung ương, BTP·TW) · **Màn:** /bieu-mau/thu-muc
**Công cụ:** `tools/toast-capture.js` (KHÔNG lọc trùng · đọc `innerText` · đếm request song song số toast). Self-check `soObserverDangSong = 1` (hợp lệ) trước mỗi lần đo.

## Tiền đề
- Thư mục "BM-B1-0720 Trung" (Nháp, Thương mại, BTP·TW) đã tồn tại (seed).
- Thao tác: Thêm thư mục → nhập lại đúng tên trùng "BM-B1-0720 Trung" → Lưu.

## Kết quả 2 lần đo độc lập (2 lần submit trùng)

| Lần | SO_REQUEST (POST) | request | SO_KHUNG_THONG_BAO | chữ | BI_LAP |
|---|---|---|---|---|---|
| 1 | 1 | `POST /api/v1/thu-muc-bieu-maus` | 1 | "Tên thư mục đã tồn tại trong đơn vị" | false |
| 2 | 1 | `POST /api/v1/thu-muc-bieu-maus` | 1 | "Tên thư mục đã tồn tại trong đơn vị" | false |

**Kết luận:** 1 request → 1 khung thông báo (cả 2 lần). KHÔNG nhân đôi. Cả 2 tầng đều nhất quán:
- Tầng network: 1 POST (không gửi trùng).
- Tầng hiển thị: 1 toast frame (observer không lọc trùng — nếu có 2 khung sẽ đếm 2).

→ Triệu chứng đối tác báo ("thông báo bị duplicate") KHÔNG tái hiện trên build hiện tại.

## Ghi chú phụ (ngoài tiêu chí case — wording)
- Toast hiển thị: **"Tên thư mục đã tồn tại trong đơn vị"**.
- SRS ERR-TM-01 (`srs-fr-09-bieu-mau.md:130`): **"Thư mục '{tên}' đã tồn tại trong đơn vị"**.
- Khác biệt: app KHÔNG chèn tên thư mục cụ thể + đổi "Thư mục '{tên}'" → "Tên thư mục". Ý nghĩa tương đương (báo đúng lỗi trùng tên). Deviation cosmetic, đối tác KHÔNG phản ánh mục này. Ghi nhận để nêu ở mục "bất thường ngoài tiêu chí".

## Bằng chứng đối tác (Cổng 1)
- File: `reverify-week-3/partner-evidence/QLTMBMHD_07.jpg` — chụp env đối tác `htpldn-uat.ospgroup.vn`, hiện **2 toast xếp chồng** "Tên thư mục đã tồn tại trong đơn vị". (Env đối tác khác env test — đã tái hiện đúng điều kiện trên env test và không thấy nhân đôi.)
