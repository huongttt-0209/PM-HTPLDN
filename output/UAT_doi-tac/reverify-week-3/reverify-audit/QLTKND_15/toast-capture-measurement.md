# QLTKND_15 — Đo duplicate toast bằng tools/toast-capture.js (vùng nóng)

**Env:** https://18.143.165.120.nip.io · **Ngày:** 2026-07-21 · **Account:** admin (QTHT)
**Thao tác:** Thêm tài khoản mới với **tên đăng nhập trùng** = `cbnv_tw` (đã tồn tại), email mới `qa.dup.uname.0721@htpldn.test`, Loại=Cán bộ, Đơn vị=Bộ Công an, Vai trò=Cán bộ Nghiệp vụ Bộ/Ngành → bấm "Thêm mới".

## Kết quả đo (mandated tool, KHÔNG lọc trùng, innerText, observer=1 đã self-check)

```json
{
  "SO_REQUEST": 1,
  "request": ["POST /api/v1/tai-khoan"],
  "SO_TOAST": 2,
  "chu": ["Username đã tồn tại trong hệ thống", "Tên đăng nhập 'cbnv_tw' đã tồn tại"],
  "toastZIndex": ["2010", "2010"],
  "modalZIndex": "1000",
  "rect": [{"top": -32, "left": 0, "w": 1200, "h": 40}, {"top": 8, "left": 0, "w": 1200, "h": 40}]
}
```

## Đọc kết quả (theo bảng toast-capture.js)
- **1 request + 2 khung thông báo** → lỗi HIỂN THỊ phía FE (không tạo trùng bản ghi — chỉ 1 POST, và bị BE từ chối do trùng username).
- **2 chữ KHÁC nhau** ("Username đã tồn tại trong hệ thống" vs "Tên đăng nhập 'cbnv_tw' đã tồn tại") → loại trừ artifact observer nhân bản (nhân bản sẽ cho 2 chữ GIỐNG hệt). Self-check `soObserverDangSong = 1` (hợp lệ) trước mỗi lần đo.
- **toast z-index 2010 > modal z-index 1000** → 2 toast render NỔI TRÊN modal, hiển thị thật trên màn hình (không bị modal che). rect top:8 và top:-32 = xếp chồng ở đỉnh viewport.
- Tái hiện **≥5 lần** submit, kết quả y hệt (vd chuỗi 3 submit liên tiếp không reset observer → 3 request : 6 toast = đúng tỷ lệ 1 request : 2 toast).
- Ảnh chụp của QA (`BUG-QLTKND_15-dup-username-toast.png`) bắt được state form (username `cbnv_tw`); toast tự tắt ~3s nên khung chụp lỡ nhịp — nhưng observer (công cụ bắt buộc) + evidence full-res đối tác (`partner-evidence/QLTKND_15.jpg`, hiện đúng 2 toast này) xác nhận trực quan.

## Verdict
`Open` — 1 lần submit trùng username sinh **2 thông báo lỗi** (đối chiếu FR-VIII-15 §Error Handling E1 `ERR-TK-01` dòng 727: chỉ cần 1 thông báo "Username '{username}' đã tồn tại"). Cross-ref cụm duplicate B5.
