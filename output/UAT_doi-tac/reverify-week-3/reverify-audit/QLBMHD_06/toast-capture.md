# QLBMHD_06 (row 99) — Upload file >20MB — đo thông báo (Chrome DevTools MCP + toast observer)

- **Tài khoản:** `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP·TW) — đúng vai trò đối tác (CB Nghiệp vụ).
- **Màn:** Form Thêm biểu mẫu (`/bieu-mau/them-moi`), trường "File biểu mẫu" (accept .doc/.docx/.xls/.xlsx, max 20MB).
- **File test:** `big-21mb.docx` (~21.0 MB, docx hợp lệ nhồi media để vượt ngưỡng).
- **Đo bằng:** `tools/toast-capture.js` (observer KHÔNG lọc trùng, `innerText`, đếm request).

## Kết quả đo (2026-07-20)

```json
{ "SO_TOAST": 1, "chu_toast": ["File vượt quá 20MB (21.0 MB)"], "SO_REQUEST": 0 }
```

- Thông báo web: **"File vượt quá 20MB (21.0 MB)"** — 1 khung toast, **0 request ghi** (FE chặn client-side, không gọi upload). File KHÔNG được đính kèm.
- Khớp với evidence đối tác: "File vượt quá 20MB (24.7 MB)" (file 24.7MB).

## Đối chiếu SRS

- SRS ERR-BM-02 (`srs-fr-09:343`): **"File vượt quá giới hạn 20MB. Kích thước: {size}MB"**.
- Web: "File vượt quá 20MB ({size} MB)".
- **Cùng nội dung nghiệp vụ** (báo file vượt 20MB + kích thước thực). Khác: bỏ chữ "giới hạn"; format "(21.0 MB)" thay vì ". Kích thước: 21.0MB".

## Verdict

- Yêu cầu nghiệp vụ ERR-BM-02 (báo file vượt 20MB kèm kích thước) **được đáp ứng**; chỉ khác **cách diễn đạt** so với chuỗi mẫu SRS.
- → **BA confirm**: app có báo đúng thông tin (vượt 20MB + size), wording khác chuỗi SRS mẫu → BA quyết có bắt buộc đúng nguyên văn ERR-BM-02 không. QA không tự Reject (đối tác quan sát đúng thực tế) cũng không Open (yêu cầu nghiệp vụ đã đạt).
