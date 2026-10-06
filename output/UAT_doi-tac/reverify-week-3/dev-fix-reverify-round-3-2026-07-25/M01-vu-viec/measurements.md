# M01 — Vụ việc · Reverify sau Dev fix (round 3, 25/07/2026)

Môi trường: https://18.143.165.120.nip.io · Tài khoản bộ **_05** (trừ vai trò bắt buộc theo tiêu chí Dev).
Tiêu chí chấm: cột **DEV phản hồi lần 1** của từng dòng — không tự đặt tiêu chí khác.

| Dòng | Mã TC | Verify | Tài khoản dùng | Vụ việc |
|---|---|---|---|---|
| 9 | PDHSVV_04 | ✅ Pass | `cbpd_tw_05` | VV-BTP-TW-20260712-004 (Chờ phê duyệt) |
| 11 | CNKQHT_03 | ❌ Reopen | `qa_tvvseed28` (người xử lý) + `cbnv_tw_05` | VV-BTP-TW-20260712-004 (Đang xử lý) |
| 13 | CNKQVV_02 | ✅ Pass | `cbnv_tw_05` | VV-BTP-TW-20260712-005 (Đã duyệt) |

---

## PDHSVV_04 (dòng 9) — Pass

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Nhập 9 ký tự → xác nhận | Ô báo đỏ **"Tối thiểu 10 ký tự"**, bộ đếm `9 / 2000`, **0 request** gửi đi | ✅ |
| 2) Dán đúng 2.000 ký tự → xác nhận | Bộ đếm `2000 / 2000`; 1 request `POST .../phe-duyet`, 1 thông báo **"Đã từ chối phê duyệt"**; vụ việc quay về **Đang xử lý** | ✅ |
| 3) Thử 2.001 ký tự | Dán 2.001 → chỉ vào 2.000; gõ thêm 1 ký tự → không vào, giữ `2000 / 2000` | ✅ |
| 4) Mở lại đọc lý do đã lưu | Khung "Vụ việc bị từ chối phê duyệt" hiển thị lý do **đủ 2.000 ký tự**, còn nguyên mốc đầu `BAT DAU\|` và mốc cuối `\|KET-THUC-2000` → không cắt cụt | ✅ |

Ảnh: `image/PDHSVV_04-01…04-*.png`

## CNKQVV_02 (dòng 13) — Pass

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Nhãn nút thao tác | **"Cập nhật kết quả cuối"** — không còn nhãn "Hoàn thành" | ✅ |
| 2) Các ô trong màn nhập | Chỉ 1 ô **"Kết luận cuối cùng"**; **không còn** ô "Kết quả xử lý" (Thành công / Không thành công) | ✅ |
| 3) Nhập kết luận → xác nhận | 1 request `POST .../hoan-thanh`, 1 thông báo **"Vụ việc đã hoàn thành"**; badge → **Hoàn thành**; dòng thời gian ghi **25/07/2026 02:23**; kết luận đọc lại đúng nguyên văn | ✅ |

Ảnh: `image/CNKQVV_02-01…05-*.png`
Lưu ý đã áp dụng: chữ "Hoàn thành" ở badge / thanh tiến trình là **tên trạng thái** → không tính FAIL.

## CNKQHT_03 (dòng 11) — Reopen

Đạt 3/4 nhóm tiêu chí, **hỏng ở nhóm tệp đính kèm**.

| Bước theo tiêu chí Dev | Đo được | KQ |
|---|---|---|
| 1) Liệt kê các ô trong màn nhập | Đúng 3 ô: **Nội dung kết quả** · **Tệp kết quả hỗ trợ** (kéo-thả, ≤10 tệp, 20MB/tệp) · **Ghi chú**. **Không còn** ô "Kết luận" | ✅ |
| 2) Dán 10.000 ký tự, rồi thử 10.001 | Bộ đếm `10000 / 10000`; ký tự thứ 10.001 không vào được; lưu xuống `noiDung` đủ **10.000** | ✅ |
| 3) Đính kèm 1 tệp rồi Lưu | **Vai trò TVV được phân công** (`qa_tvvseed28`): `POST /api/v1/vu-viecs/upload` → **403 `ERR-PERM-SYS-00-01` "Forbidden"**, không đính kèm được tệp nào. Xác minh 2 cách: thao tác trên màn hình + gọi trực tiếp cùng phiên | ❌ |
| 4) Mở lại xem phần Kết quả hỗ trợ | **Vai trò CB Nghiệp vụ** (`cbnv_tw_05`): upload **201**, tệp hiện trong cửa sổ nhập, lưu báo "Đã cập nhật kết quả". Payload lưu **có** `fileIds:["530a64e1-…"]` nhưng bản ghi kết quả trả về **không có trường tệp nào**; mở lại vụ việc thì mục *Kết quả hỗ trợ* chỉ còn phần nội dung, mục *Tài liệu đính kèm* cũng rỗng → **mất tệp** | ❌ |

Khớp đúng điều kiện ❌ mà Dev nêu: *"đính kèm được nhưng sau khi lưu mở lại mất tệp"*.

Ảnh: `image/CNKQHT_03-01…05-*.png`

**Quan sát thêm (ngoài tiêu chí):** thông báo lỗi khi TVV đính kèm hiển thị nguyên văn tiếng Anh **"Forbidden"** — đã ghi kèm trong mô tả lỗi ở cột R, không mở dòng riêng vì thuộc cùng thao tác đang lỗi.

---

## Ghi chú kỹ thuật khi đo

- Ô nhập nhiều dòng của app không nhận giá trị qua `fill` của công cụ (React không bắt sự kiện) → nhập bằng bàn phím thật / `execCommand('insertText')` (vẫn tôn trọng `maxLength`, nên phép thử "vượt mốc" là hợp lệ).
- `upload_file` của Chrome DevTools MCP không đẩy được tệp qua nút chọn của AntD Upload → dùng sự kiện kéo-thả với `DataTransfer` trên `span.ant-upload-btn`; app chạy đúng handler upload của nó (có request `POST /vu-viecs/upload` thật).
- Bộ bắt thông báo: `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` trước khi tin số liệu. Mọi thao tác đều **1 request ↔ 1 thông báo**, không có thông báo lặp.

## Dữ liệu đã tự seed (để mở khoá tiền đề)

- VV-BTP-TW-20260712-004: `Đang xử lý` → cập nhật kết quả → **Trình phê duyệt** → `Chờ phê duyệt` (lấy tiền đề cấp TW cho PDHSVV_04; env chỉ có sẵn 1 VV Chờ phê duyệt thuộc Sở Tư pháp An Giang, sai cấp). Sau khi test từ chối, VV nay ở `Đang xử lý`.
- VV-BTP-TW-20260712-005: sau CNKQVV_02 nay ở **Hoàn thành** (còn `VV-SEED-0001` là VV `Đã duyệt` dự phòng).
