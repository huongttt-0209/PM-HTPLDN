# Bảng đối chiếu điều kiện — TDHSTVV_08 (Lưu nháp kết quả thẩm định)

Evidence đối tác: `partner-evidence/TDHSTVV_08.webm` — frame 00:13 (điền Nhận xét "a" + Kết luận ĐẠT, trỏ chuột vào nút "Lưu nháp"), frame 00:16 (sau khi bấm — không có thông báo), frame 00:18–00:21 (lộ header hồ sơ: **TVV-BTP-TW-0011 "Lê Văn Chuyên Gia (R32 NHT edit)" — trạng thái "Đang thẩm định"**).
Trích dày 2 fps trong 8 giây sau cú bấm (crop vùng đỉnh màn hình nơi toast Ant Design hiện) → **không frame nào có toast**.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương — badge "Cán bộ NV Trung ương / CB_NV_TW", đơn vị BTP · TW | CB Nghiệp vụ Trung ương — `cbnv_tw`, badge CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-BTP-TW-0011`, trạng thái **"Đang thẩm định"** (đọc từ frame 00:18) | Hồ sơ TVV `TVV-BTP-TW-0003`, trạng thái **"Đang thẩm định"** — tự seed: bấm Lưu nháp lần 1 khiến hệ thống ngầm chuyển Mới đăng ký → Đang thẩm định (POST /tham-dinh trả `trangThai: DANG_THAM_DINH`), sau đó **chạy lại đúng thao tác Lưu nháp tại trạng thái Đang thẩm định** | Không |
| Dữ liệu tiền đề | Biểu mẫu thẩm định đã điền: Nhận xét = "a", Nhóm 4 tích chọn, Kết luận thẩm định = ĐẠT | Biểu mẫu đã điền: Kết luận Pháp lý = Đạt, 3 ô Nhận xét (Nhóm 2/3/4) có nội dung, Kết luận thẩm định = ĐẠT — tương đương, phủ rộng hơn (3 ô nhận xét thay vì 1) | Không |
| Input / thao tác | Bấm nút "Lưu nháp" trên tab Thẩm định | Bấm nút "Lưu nháp" trên tab Thẩm định (cùng nút, cùng màn) | Không |

Kết luận: **0 GAP** — đã verify đúng vai trò CB_NV_TW và đúng trạng thái "Đang thẩm định" của đối tác, trên biểu mẫu đã điền tương đương.

## Quan sát (artifact real-data)

- MutationObserver cài **trước** cú bấm, chờ 3.5s: `addedNodes = 0`, không có `.ant-message-notice-wrapper` / `.ant-notification-notice` / `[role=alert]` → **không có thông báo nào hiện ra**.
- Network: `POST /api/v1/tu-van-viens/{id}/tham-dinh` → **200 OK** (thao tác có chạy, BE lưu thành công) — chứng minh "im lặng" là lỗi FE không phản hồi, không phải do request thất bại.
- **Payload gửi lên thiếu 3 ô Nhận xét:** `{"nhom1KetQua":true,"nhom2Diem":3,"nhom3Diem":3,"nhom4ThamGia":false,"ketLuan":"DAT","version":2,"trinhDuyet":false}` — FE không gửi nội dung nhận xét đã nhập.
- Sau khi tải lại trang (ignoreCache): 3 ô Nhận xét **trống**, radio "Kết luận Pháp lý" và "Kết luận thẩm định" **không được chọn lại** → nháp không được nạp lại, dù BE đã lưu `nhom1KetQua=true` và `ketLuan=DAT`.

---

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data bug gốc: **CB_NV_TW `cbnv_tw`, BTP·TW**, hồ sơ **TVV-BTP-TW-0009**, tab Thẩm định. Điền Kết luận Pháp lý=Đạt, 3 ô Nhận xét (Nhóm 2/3/4), Kết luận thẩm định=ĐẠT → bấm "Lưu nháp".

**Kết quả FIXED (chạy luồng UI + MutationObserver + reload):**
1. Toast **"Đã lưu kết quả thẩm định"** hiện (bắt bằng MutationObserver ngay sau click) — trước đây im lặng.
2. + 3. Tải lại trang → mở lại tab Thẩm định: 3 ô Nhận xét nạp lại **đầy đủ nguyên văn**, Kết luận Pháp lý=Đạt + Kết luận thẩm định=ĐẠT vẫn được chọn. Hồ sơ chuyển "Đang thẩm định".

⇒ 3 điểm lỗi gốc (không toast · mất Nhận xét · nháp không nạp lại) đều hết. **PASS.** Ảnh: `bug-reports/image/TDHSTVV_08-reverify-nhanxet-persist-sau-reload.png`.
