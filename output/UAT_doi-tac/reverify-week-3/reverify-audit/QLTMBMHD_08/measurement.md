# QLTMBMHD_08 — Đo hành vi giới hạn 500 ký tự (ô "Tên thư mục")

**Ngày đo:** 2026-07-20 · **Tài khoản:** cbnv_tw (CB Nghiệp vụ - TW, BTP·TW) · **Màn:** /bieu-mau/thu-muc → modal "Thêm thư mục biểu mẫu"
**Phương pháp:** `evaluate_script` inspect DOM trực tiếp (2 phương pháp độc lập).

## Phương pháp 1 — Thuộc tính ô nhập
```json
{"modalTitle":"Thêm thư mục biểu mẫu","nameTag":"INPUT","id":"tenThuMuc",
 "maxlength":"500","placeholder":"Nhập tên thư mục...","counters":[]}
```
- Ô `#tenThuMuc` có **`maxlength="500"`** → trình duyệt CHẶN CỨNG khi người dùng gõ/dán quá 500 ký tự (cắt âm thầm ở 500).
- **KHÔNG có bộ đếm ký tự** (`counters: []`) → không có phản hồi trực quan "còn bao nhiêu ký tự".

## Phương pháp 2 — Ép value vượt 500 (bypass maxlength bằng programmatic set)
Set `#tenThuMuc.value` = chuỗi ~620 ký tự (bằng native setter, bypass maxlength của trình duyệt) rồi dispatch `input`:
```json
{"inputLenTyped":620,"maxlengthAttr":"500","valueLenAfterSet":620,
 "errMessages":["Tối đa 500 ký tự","Tối đa 500 ký tự"],"counters":[]}
```
- Khi value THỰC SỰ vượt 500 (chỉ đạt được bằng bypass), app CÓ luật kiểm tra → hiện lỗi inline **"Tối đa 500 ký tự"**.
- ("Tối đa 500 ký tự" xuất hiện 2 lần = selector khớp cả `.ant-form-item-explain` (cha) lẫn `.ant-form-item-explain-error` (con) — CÙNG 1 element, KHÔNG phải nhân đôi thật.)

## Kết luận hành vi
1. Người dùng gõ/dán > 500 ký tự → **maxlength cắt cứng ở 500, âm thầm, KHÔNG bộ đếm, KHÔNG thông báo** (đúng như đối tác phản ánh).
2. App CÓ sẵn message "Tối đa 500 ký tự" nhưng **chỉ hiện khi value > 500** — mà maxlength lại chặn không cho value vượt 500 → **message thực tế KHÔNG BAO GIỜ hiện với người dùng qua thao tác bàn phím/paste bình thường**.
3. Giới hạn 500 ký tự ĐƯỢC enforce đúng (toàn vẹn dữ liệu OK) — điểm tranh luận chỉ là "có cần hiện thông báo/bộ đếm khi chạm giới hạn hay không".

## Đối chiếu SRS
- SRS `srs-fr-09-bieu-mau.md:132` — Error Handling E3: **"Tên vượt 500 ký tự | ERR-TM-03 | 'Tên thư mục tối đa 500 ký tự' | ERROR"**.
- App enforce giới hạn nhưng bằng cơ chế chặn-cứng (maxlength) thay vì cho-nhập-rồi-báo → thông báo ERR-TM-03 không tới người dùng.
- Message app ("Tối đa 500 ký tự") cũng khác chữ SRS ("**Tên thư mục** tối đa 500 ký tự") nhưng vì message không reachable qua UI nên khác biệt này không ảnh hưởng người dùng.

## Bằng chứng đối tác (Cổng 1)
- `partner-evidence/QLTMBMHD_08.jpg` — modal "Thêm thư mục", ô Tên chứa chuỗi rất dài (đã bị cắt ở giới hạn), Lĩnh vực "Thuế", KHÔNG có thông báo lỗi nào hiển thị.
