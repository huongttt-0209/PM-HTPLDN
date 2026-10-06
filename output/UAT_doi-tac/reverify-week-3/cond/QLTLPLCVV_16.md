# Bảng đối chiếu điều kiện — QLTLPLCVV_16 (row 301) — Xóa tệp đính kèm: không hiển thị xác nhận

**Kết luận:** BA confirm (Dạng A). Đối tác quan sát ĐÚNG thực tế (xóa file đính kèm → không có hộp xác nhận), nhưng **SRS 904–913 "Processing — Xóa file đính kèm" KHÔNG có step "Hiển thị xác nhận"** (khác "Xóa mềm tư liệu" dòng 900 CÓ confirm). Hành vi hiện tại (không confirm) **khớp SRS**; kỳ vọng đối tác (cần confirm) là thứ SRS **không quy định** → bất đồng ĐẶC TẢ, để BA chốt có bổ sung confirm cho thao tác xóa file hay không. QA KHÔNG tự Reject.

> Verdict (BA confirm) đến từ **câu hỏi đặc tả** "xóa file có cần confirm?" — trả lời bằng SRS 904–913, KHÔNG phụ thuộc điều kiện role/state/data. Các điều kiện dưới đây đều khớp (0 GAP): tức khiếu nại đối tác hợp lệ, tranh chấp thuần về spec. (Việc form Sửa trên nip.io không render file cũ là **anomaly riêng**, không đổi câu trả lời spec — xem mục Anomaly.)

| Điều kiện có thể đổi kết quả | Đối tác (video `partner-evidence/QLTLPLCVV_16.webm`, frames t000–t004) | Mình test (cbnv_tw / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW | cbnv_tw (CB_NV_TW — đúng Tác nhân SRS dòng 806, CRUD đầy đủ) | Không |
| Entity + trạng thái | Tư liệu "TKM kiểm thử chức năng" **Nháp (NHAP)**, có 1 file đính kèm ("2K15 T5 (16.7) & T7 (18.7).pdf") | Tư liệu seed **TL-BF-0721-NHAP** **NHAP**, có 1 file (seed_clean.pdf), soFile=1 | Không |
| Thao tác + kết quả tranh chấp | Bấm xóa 1 file đính kèm → **không có hộp xác nhận** (frames t002→t004: file biến mất ngay) | Actual "không confirm" được xác nhận bằng video đối tác + **KHỚP SRS 904–913** (không có step confirm). Verdict là câu hỏi spec, không phụ thuộc việc render trên nip.io (repro trực tiếp bị chặn — xem Anomaly) | Không |

## Bằng chứng đối tác (đọc frame video)

- **t002.02s:** trên `htpldn-uat.ospgroup.vn`, form "Sửa tư liệu pháp luật" mục **File đính kèm** hiển thị file cũ `2K15 T5 (16.7) & T7 (18.7).pdf` (icon 📎 + tên file + **icon thùng rác** bên phải). Con trỏ hover icon thùng rác.
- **t003.04s → t004.07s:** sau khi bấm icon thùng rác, file **biến mất ngay** (mục File đính kèm chỉ còn ô "Kéo thả hoặc nhấp để chọn tệp") — **KHÔNG có hộp xác nhận** nào hiện ra giữa 2 frame. ⇒ Đối tác quan sát đúng: xóa file đính kèm không hỏi xác nhận.

## Đối chiếu SRS (nguồn chuẩn để BA quyết)

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:904–913` — Processing "Xóa file đính kèm": 6 bước (kiểm quyền → kiểm file tồn tại → xóa khỏi storage → cập nhật liên kết → cảnh báo nếu CONG_KHAI hết file → ghi log). **KHÔNG có step "Hiển thị xác nhận".**
- `...:900` — Processing "Xóa mềm **tư liệu**" step 4 CÓ: *"Hiển thị xác nhận: 'Bạn có chắc chắn muốn xóa tư liệu {tên}?'"*. ⇒ Spec CHỦ ĐÍCH đặt confirm cho xóa **tư liệu** nhưng KHÔNG đặt cho xóa **file**. Không rõ là cố ý (file dễ thêm lại nên bỏ confirm) hay sót → **cần BA xác nhận**.

## Reproduction trên nip.io + Anomaly (out-of-scope, cần dev/BA)

Không thao tác được đúng bước "bấm xóa file trong form Sửa" trên env verify vì **form "Sửa tư liệu pháp luật" của nip.io KHÔNG hiển thị file đính kèm cũ** (chỉ có ô upload trống). Đo 2 phương pháp:
- **UI:** a11y tree + `evaluate_script` quét `[role=dialog]` → 0 `ant-upload-list-item`, text modal KHÔNG chứa tên file. Ảnh: `reverify-audit/QLTLPLCVV_16/nipio-edit-form-no-existing-file.png`.
- **API:** `GET /api/v1/tu-lieu-phap-ly-vvs/{id}` trả **`files: []`** dù `soFile: 1`, cho CẢ 2 tư liệu (NHAP mới tạo `39f2f1fb…` và CONG_KHAI seed `172a8cfa…`). Tư liệu CONG_KHAI chắc chắn CÓ file (đã công khai — SRS dòng 867 bắt buộc ≥1 file), nhưng detail vẫn trả `files:[]`.

⇒ Trên nip.io, CB NV **không xem/xóa được file đính kèm cũ** qua form Sửa (endpoint detail không trả mảng `files`). Đây là **vấn đề khác** với khiếu nại đối tác (confirm dialog) — verdict case này vẫn BA confirm theo câu hỏi spec confirm; anomaly `files:[]` báo dev/BA riêng (xem note + báo cáo cuối batch). *Chưa chốt Open vì chưa loại trừ khả năng FE dùng endpoint khác để nạp/xóa file (env đối tác hiển thị được file → build khác).*
