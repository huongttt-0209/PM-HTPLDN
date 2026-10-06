# Bảng đối chiếu điều kiện — TDHSTVV_14 (Gửi kết quả thẩm định, kết luận "Không đạt")

Evidence đối tác: `partner-evidence/TDHSTVV_14.webm` — frame 00:41: toast lỗi đỏ **"Dữ liệu đã bị thay đổi, vui lòng tải lại"** (đối tác bôi đen), Kết luận thẩm định = KHÔNG ĐẠT + Lý do "TKM test không đạt". Frame 00:46: header hồ sơ `TVV-BTP-TW-0011` ("Lê Văn Chuyên Gia (R32 NHT edit)") — **trạng thái "Yêu cầu bổ sung"**.
⇒ Đối tác chạy case này ngay trên hồ sơ vừa bị case TDHSTVV_13 đẩy sang trạng thái **"Yêu cầu bổ sung"**.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương — CB_NV_TW, đơn vị BTP · TW | CB Nghiệp vụ Trung ương — `cbnv_tw`, CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-BTP-TW-0011`, trạng thái **"Yêu cầu bổ sung"** (đọc từ frame 00:46) | Hồ sơ TVV `TVV-BTP-TW-0003`, trạng thái **"Yêu cầu bổ sung"** (do case TDHSTVV_13 vừa đẩy sang — đúng y kịch bản đối tác), tải lại trang mới hoàn toàn trước khi thao tác | Không |
| Dữ liệu tiền đề | Biểu mẫu đã điền, Kết luận Pháp lý đã chọn, Lý do "TKM test không đạt" | Biểu mẫu đã điền: Kết luận Pháp lý = Đạt, Lý do 81 ký tự (> mức tối thiểu 10) | Không |
| Input / thao tác | Chọn Kết luận thẩm định = "KHÔNG ĐẠT" → bấm "Gửi KQ" | Chọn Kết luận thẩm định = "KHÔNG ĐẠT" → bấm "Gửi KQ" (cùng nút, cùng màn) | Không |

Kết luận: **0 GAP** — đúng vai trò CB_NV_TW, đúng trạng thái "Yêu cầu bổ sung", đúng kết luận "Không đạt" của đối tác. Tái hiện **chính xác** thông báo lỗi đối tác gặp.

## Quan sát 1 — tái hiện đúng điều kiện đối tác (trạng thái "Yêu cầu bổ sung")

- Bấm "Gửi KQ" (KHÔNG ĐẠT) → toast đỏ **"Dữ liệu đã bị thay đổi, vui lòng tải lại"** (MutationObserver bắt được đúng chuỗi này). Trạng thái hồ sơ **không đổi**, vẫn "Yêu cầu bổ sung" ⇒ đúng như đối tác than "tải lại dữ liệu vẫn là dữ liệu cũ".
- **Quan trọng — lỗi xảy ra NGAY CẢ trên trang vừa tải mới** (đã reload bỏ qua bộ nhớ đệm trước khi thao tác) ⇒ **KHÔNG** phải do giao diện giữ phiên bản dữ liệu cũ.
- **Nguyên nhân thật (đọc từ phản hồi máy chủ):**
  - `POST /api/v1/tu-van-viens/{id}/tham-dinh` → **HTTP 409**
  - `error.code` = **`ERR-STATE-IV-TD-01`**
  - `error.message` = **"TVV không ở trạng thái hợp lệ để thẩm định"**
- ⇒ Máy chủ báo **sai trạng thái**, nhưng giao diện lại hiện thông báo **xung đột dữ liệu đồng thời** ("Dữ liệu đã bị thay đổi, vui lòng tải lại"). Giao diện ánh xạ nhầm mọi lỗi 409 thành thông báo xung đột → người dùng tải lại trang vô ích, không bao giờ biết lý do thật.
- Ảnh: `bug-reports/image/BUG-TDHSTVV_14-web-toast-sai-du-lieu-da-bi-thay-doi.png`.

## Quan sát 2 — đối chứng trên trạng thái HỢP LỆ (để xác định phạm vi lỗi)

Tự seed hồ sơ mới `TVV-BTP-TW-0004` ("QA TVV Khong Dat R14") ở trạng thái **"Mới đăng ký"** — là trạng thái **hợp lệ** để thẩm định theo SRS dòng 495 (Preconditions: TVV ở trạng thái MOI_DANG_KY hoặc DANG_THAM_DINH):

- Chọn KHÔNG ĐẠT + Lý do → "Gửi KQ" → hồ sơ chuyển sang **"Từ chối"** (máy chủ: `trangThai = TU_CHOI`). ⇒ **Nghiệp vụ từ chối chạy ĐÚNG** khi trạng thái hợp lệ.
- **NHƯNG vẫn không có thông báo thành công nào** (MutationObserver: `addedNodes = 0`) — trong khi Kết quả mong đợi của đối tác là thông báo "Đã từ chối hồ sơ".

⇒ Case này có **2 lỗi tách biệt**: (1) thông báo lỗi sai bản chất khi trạng thái không hợp lệ; (2) thiếu thông báo thành công khi thao tác thành công.

## Đối chiếu SRS (Cổng 3)

- `srs-fr-04-chuyen-gia-tvv.md` dòng 1555 (ô 13) — tab "Thẩm định" **chỉ hiển thị khi trạng thái ∈ {Đang thẩm định, Chờ phê duyệt}**. → Web: vẫn hiện tab + biểu mẫu + nút "Gửi KQ" ở trạng thái "Yêu cầu bổ sung", dẫn người dùng vào thao tác mà máy chủ chắc chắn từ chối. **KHÔNG khớp.**
- `srs-fr-04-chuyen-gia-tvv.md` dòng 495 (Preconditions) — TVV phải ở MOI_DANG_KY hoặc DANG_THAM_DINH mới thẩm định được. → Máy chủ chặn đúng; **giao diện mới là nơi sai** (cho vào + báo sai lý do).
- `srs-v3.5.md` dòng 571 — **UI-04**: "Toast notification cho **thao tác thành công**". → Web: từ chối thành công nhưng không có thông báo. **KHÔNG khớp.**
- `srs-fr-04-chuyen-gia-tvv.md` dòng 520 + 1564 — kết luận KHÔNG ĐẠT → chuyển trạng thái Đã từ chối + thông báo chủ hồ sơ. → Web: chuyển trạng thái **đúng**.

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Vai trò CB_NV_TW (`cbnv_tw`), đơn vị BTP · TW — 0 GAP điều kiện.

**Lỗi 1 — thông báo lỗi sai bản chất ở trạng thái không hợp lệ: ĐÃ FIX.**
- Mở hồ sơ trạng thái **"Yêu cầu bổ sung"** → tab "Thẩm định" nay **bị vô hiệu hóa** (disabled), không vào được biểu mẫu thẩm định sai trạng thái.
- ⇒ Người dùng không còn bị dẫn vào thao tác mà máy chủ chắc chắn từ chối → không còn toast lỗi sai bản chất "Dữ liệu đã bị thay đổi". Khớp SCR-IV-03 (tab chỉ hiển thị/thao tác khi trạng thái hợp lệ).

**Lỗi 2 — thiếu thông báo thành công khi từ chối: ĐÃ FIX.**
- Seed hồ sơ mới `TVV-BTP-TW-0011` ("QA TVV RV14L2 KhongDat") ở trạng thái **"Mới đăng ký"** (hợp lệ theo SRS dòng 495).
- Kết luận Pháp lý = Đạt; Kết luận thẩm định = **KHÔNG ĐẠT**; Lý do 92 ký tự → "Gửi KQ".
- Kết quả: trạng thái chuyển **"Từ chối"** ✅ **VÀ** hiện toast thành công **"Đã lưu kết quả thẩm định"** (MutationObserver bắt được — trước đây `addedNodes = 0`). Khớp UI-04 "Toast notification cho thao tác thành công".
- Ảnh: `bug-reports/image/TDHSTVV_14-reverify-loi2-tuchoi-toast-thanhcong.png`.

Kết luận: **cả 2 lỗi đã fix → PASS/Closed.**
