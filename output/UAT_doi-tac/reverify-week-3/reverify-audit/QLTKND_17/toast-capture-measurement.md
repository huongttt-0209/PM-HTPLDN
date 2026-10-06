# QLTKND_17 — Đo duplicate EMAIL toast bằng tools/toast-capture.js (vùng nóng)

**Env test:** https://18.143.165.120.nip.io · **Ngày:** 2026-07-21 · **Account:** admin (QTHT)
**Thao tác:** Thêm tài khoản mới với **email trùng** = `nht_qa_01@htpldn.test` (đã tồn tại), tên đăng nhập MỚI (unique), Loại=Cán bộ, Đơn vị=Bộ Công an, Vai trò=Cán bộ Nghiệp vụ Bộ/Ngành → bấm "Thêm mới".

## Kết quả đo (mandated tool, KHÔNG lọc trùng, innerText, observer=1 đã self-check mỗi lần)

| Lần | Username | observer self-check | SO_REQUEST | Response | SO_TOAST | Chữ |
|-----|----------|--------------------|-----------|----------|----------|-----|
| #1 | qadupemail0721 | =1 (hợp lệ) | 1 (`POST /api/v1/tai-khoan`) | lỗi email trùng | **1** | "Email đã tồn tại trong hệ thống" |
| #2 | qadupemail0721b | =1 (hợp lệ) | 1 (`POST /api/v1/tai-khoan`) | lỗi email trùng | **1** | "Email đã tồn tại trong hệ thống" |
| #3 | qadupemail0721c | =1 (hợp lệ) | 1 (`POST /api/v1/tai-khoan` → **409**) | 409 Conflict | 0 (miss) | — (xem ghi chú) |

```json
// Lần #1
{"SO_REQUEST":1,"request":["POST /api/v1/tai-khoan"],"SO_TOAST":1,"chu":["Email đã tồn tại trong hệ thống"],"BI_LAP":false,"khoangCachMs":null}
// Lần #2
{"SO_REQUEST":1,"request":["POST /api/v1/tai-khoan"],"SO_TOAST":1,"chu":["Email đã tồn tại trong hệ thống"],"BI_LAP":false,"khoangCachMs":null}
// Lần #3
{"SO_REQUEST":1,"request":["POST /api/v1/tai-khoan"],"SO_TOAST":0,"chu":[],"BI_LAP":false,"khoangCachMs":null}
```

## Đọc kết quả
- **2 lần đo sạch (#1, #2)** đều `1 request : 1 toast` "Email đã tồn tại trong hệ thống". Observer self-check `soObserverDangSong = 1` hợp lệ trước MỖI lần (loại trừ artifact nhân bản observer — bài học 16-17/07).
- **Lần #3** observer bắt 0 toast: KHÔNG kết luận từ run này. Network xác nhận POST `/api/v1/tai-khoan` trả **409 Conflict** (reqid=433) = server từ chối do email trùng; ngay sau đó có `POST ... [net::ERR_ABORTED]` + các GET `unread-count [net::ERR_ABORTED]` ⇒ trang đang điều hướng đi (session sắp hết hạn) làm miss toast + có thể AntD tái dùng `.ant-message-notice-wrapper` cũ nên observer (chỉ bắt `addedNodes`) không ghi nhận. Đây là miss của công cụ, KHÔNG phải bằng chứng 2 toast.
- **KHÔNG lần nào (trong 3 lần) trên env này bắt được 2 toast cho email trùng.**

## Đối chiếu evidence đối tác (khác build)
- Ảnh đối tác `partner-evidence/QLTKND_17.jpg` (14/07/2026) chụp trên **build/env KHÁC**: URL `htpldn-uat.ospgroup.vn/quan-tri/tai-khoan`, nút submit **"Tạo tài khoản"**, tổng **201** tài khoản, ghi chú form "hệ thống tự sinh mật khẩu tạm gửi qua email".
- Env đang verify (`18.143.165.120.nip.io`): nút **"Thêm mới"**, **27** tài khoản, ghi chú form "gửi liên kết kích hoạt để người dùng tự đặt mật khẩu, KHÔNG gửi mật khẩu qua email".
- ⇒ 2 build khác nhau. Trên ảnh đối tác email `aibox@gmail.com` trùng → **2 toast "Email đã tồn tại trong hệ thống"** (bug thật ở build cũ). Trên build hiện tại: **1 toast**.

## Verdict
`Reject` — Trên build hiện tại, thêm tài khoản email trùng chỉ sinh **1 thông báo lỗi** (đúng đặc tả). Hành vi 2 toast đối tác báo (build cũ ospgroup.vn) KHÔNG tái hiện trên env đang verify. Lưu ý: case chị em **QLTKND_15** (trùng **tên đăng nhập**) VẪN double-toast trên build hiện tại → đã log Open riêng.
