# Bảng đối chiếu điều kiện — TDHSTVV_12 (nút "Gửi kết quả thẩm định" bật/tắt theo Kết luận)

Evidence đối tác: `partner-evidence/TDHSTVV_12.jpg` (ảnh full-res) — "Kết luận thẩm định" **cả 3 lựa chọn đều chưa chọn**; hàng nút: "Hủy" · "Lưu nháp" · **"Gửi KQ" hiện rõ (bấm được)** · "Trình duyệt" **bị xám (khóa)**. Badge vai trò "Cán bộ NV Trung ương / CB_NV_TW", đơn vị BTP · TW, hồ sơ `/chuyen-gia-tvv/720eda6c-…`.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương — CB_NV_TW, đơn vị BTP · TW | CB Nghiệp vụ Trung ương — `cbnv_tw`, CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-BTP-TW-0011`, tab Thẩm định mở + form chấm điểm hiện ⇒ trạng thái "Đang thẩm định" | Hồ sơ TVV `TVV-BTP-TW-0003`, trạng thái "Đang thẩm định", tab Thẩm định | Không |
| Dữ liệu tiền đề (trạng thái biểu mẫu) | Chưa chọn "Kết luận thẩm định" (3 radio ĐẠT / KHÔNG ĐẠT / YÊU CẦU BỔ SUNG đều trống) | Chưa chọn "Kết luận thẩm định" — tải lại trang, kiểm bằng mã: cả 3 radio `checked = false` | Không |
| Input / thao tác | Quan sát trạng thái bật/tắt của nút "Gửi KQ" | Quan sát trạng thái bật/tắt của nút "Gửi KQ" (đọc thuộc tính `disabled` thật của phần tử) | Không |

Kết luận: **0 GAP** — đúng vai trò CB_NV_TW, đúng trạng thái "Đang thẩm định", đúng tình huống "chưa chọn Kết luận" của đối tác.

## Quan sát (artifact real-data)

Đọc trực tiếp thuộc tính `disabled` của từng nút, khi **chưa chọn Kết luận thẩm định**:

- "Hủy" → `disabled = false` (bấm được).
- "Lưu nháp" → `disabled = false` (bấm được).
- **"Gửi KQ" → `disabled = false` (bấm được) — SAI so với SRS dòng 1564.**
- "Trình duyệt" → `disabled = true` (bị khóa) — ĐÚNG theo SRS dòng 1565.

Bấm thử "Gửi KQ" khi chưa chọn Kết luận → biểu mẫu hiện lỗi kiểm tra tại chỗ: "Vui lòng chọn kết quả pháp lý" + "Vui lòng chọn kết luận"; **không** đổi trạng thái hồ sơ (vẫn "Đang thẩm định") ⇒ dữ liệu không bị hỏng, nhưng nút vẫn bật trái với điều kiện SRS quy định.

Ảnh: `bug-reports/image/BUG-TDHSTVV_12-web-nut-guikq-bam-duoc-du-chua-chon-ketluan.png` — trùng khớp ảnh đối tác.

## Đối chiếu SRS (Cổng 3)

- SRS dòng 1564 (ô 20c) — nút "Gửi kết quả thẩm định", điều kiện hiển thị: **"Tab Thẩm định, kết luận đã chọn"**. → Web: luôn bật, kể cả khi chưa chọn kết luận. **KHÔNG khớp.**
- SRS dòng 1565 (ô 20d) — nút "Trình phê duyệt", điều kiện hiển thị: "Tab Thẩm định, kết luận = Đạt". → Web: bị khóa khi chưa chọn kết luận. **Khớp.**

⇒ App đã cài đúng mẫu điều kiện cho nút anh em (20d) nhưng **bỏ sót cho 20c** — là thiếu sót cài đặt, không phải cách hiểu khác về đặc tả.

---

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data bug gốc: **CB_NV_TW `cbnv_tw`, đơn vị BTP·TW**, hồ sơ **TVV-BTP-TW-0009** trạng thái "Mới đăng ký" (thẩm định-accessible), tab Thẩm định, chưa chọn Kết luận.

**Kết quả FIXED (đọc thuộc tính `disabled` thật + test gating động):**
- Chưa chọn Kết luận thẩm định → "Gửi KQ" `disabled = true` (khóa đúng SRS dòng 1564), "Trình duyệt" `disabled = true`.
- Sau khi chọn Kết luận Pháp lý = Đạt + Kết luận thẩm định = ĐẠT → "Gửi KQ" `disabled = false`, "Trình duyệt" `disabled = false` (mở đúng).

⇒ Nút "Gửi KQ" nay gate đúng theo trạng thái chọn kết luận. **PASS.** Ảnh: `bug-reports/image/TDHSTVV_04-12-reverify-nhom3-nut-gating.png`.
