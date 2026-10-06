# Bảng đối chiếu điều kiện — TDHSTVV_17 (Trình phê duyệt, CB NV cấp Trung ương)

Evidence đối tác: `partner-evidence/TDHSTVV_17.webm` — đối tác nhập Nhận xét ("TKM test trình duyệt"), chọn Kết luận thẩm định = ĐẠT, bấm "Trình duyệt" trên hồ sơ **`TVV-BTP-TW-0007` ("Nguyễn Văn Tư Vấn 15")**. Frame 00:36-00:40: hồ sơ chuyển sang **"Chờ phê duyệt"** (nghiệp vụ chạy được); frame cuối: mở lại tab Thẩm định — ô **Nhận xét trống**.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ **Trung ương** — CB_NV_TW, đơn vị BTP · TW (đúng cấp mà case yêu cầu: TW hoặc Bộ/Ngành) | CB Nghiệp vụ Trung ương — `cbnv_tw`, CB_NV_TW, đơn vị BTP · TW (trùng khớp) | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-BTP-TW-0007`, trạng thái trước thao tác cho phép thẩm định; sau thao tác = "Chờ phê duyệt" | Hồ sơ TVV `TVV-BTP-TW-0005` ("QA TVV Trinh Duyet R17") — **tự seed mới**, trạng thái hợp lệ để thẩm định; sau thao tác = "Chờ phê duyệt" | Không |
| Dữ liệu tiền đề | Biểu mẫu đã điền: Kết luận Pháp lý, điểm, **Nhận xét có nội dung**, Kết luận thẩm định = ĐẠT | Biểu mẫu đã điền: Kết luận Pháp lý = Đạt, điểm 3/3, **cả 3 ô Nhận xét (Nhóm 2/3/4) có nội dung**, Kết luận thẩm định = ĐẠT | Không |
| Input / thao tác | Bấm nút "Trình duyệt" | Bấm nút "Trình duyệt" (cùng nút, cùng màn) | Không |
| Người nhận thông báo | CB Phê duyệt cùng đơn vị (BTP · TW) | `cbpd_tw` — CB_PD_TW, **cùng đơn vị** `00000000-...-0001` với `cbnv_tw`; đã đăng nhập bằng phiên cách ly để kiểm hộp thông báo | Không |

Kết luận: **0 GAP** — đúng vai trò CB_NV_TW cấp Trung ương, đúng trạng thái hồ sơ, đúng thao tác, và kiểm thông báo bằng **đúng tài khoản CB Phê duyệt cùng đơn vị**.

## Quan sát (artifact real-data) — cả 3 ý đối tác đều TÁI HIỆN

**Ý 1 — Không hiển thị thông báo:** MutationObserver cài trước cú bấm, theo dõi 4 giây → không có `.ant-message` / `.ant-notification` nào (3 phần tử mới ghi nhận được chỉ là biểu mẫu chuyển sang chế độ chỉ đọc). ⇒ **Không có thông báo thành công.**

**Ý 2 — Nhận xét mất sau khi tải lại:** tải lại trang (bỏ qua bộ nhớ đệm) → tab Thẩm định hiển thị Nhận xét Nhóm 2 / 3 / 4 đều là **"-"** (trống), trong khi "Kết luận thẩm định = ĐẠT" vẫn còn. ⇒ Nhận xét **không được lưu**. Cùng gốc với **BUG-TDHSTVV_08**: giao diện **không gửi** nội dung Nhận xét lên máy chủ (dữ liệu gửi lên chỉ có `nhom1KetQua / nhom2Diem / nhom3Diem / nhom4ThamGia / ketLuan / lyDo`).

**Ý 3 — Cán bộ phê duyệt không nhận được thông báo:** đăng nhập `cbpd_tw` (CB_PD_TW, **cùng đơn vị** với người thẩm định) bằng phiên cách ly ngay sau thao tác:
- Hồ sơ `TVV-BTP-TW-0005` **CÓ** nằm trong hàng chờ "Chờ phê duyệt" của tài khoản này ⇒ đúng thẩm quyền, lẽ ra phải được báo.
- Quét **50 thông báo** gần nhất → **0 thông báo** nào liên quan tư vấn viên / thẩm định / trình duyệt. Thông báo mới nhất là "19 giờ trước" (đăng nhập nơi khác) và "2 ngày trước" (đào tạo).
- Cơ chế thông báo của hệ thống **vẫn hoạt động** cho luồng khác (đào tạo, hỏi đáp đã gửi phê duyệt) ⇒ thiếu sót nằm **riêng ở luồng trình duyệt hồ sơ TVV**.
- Ảnh: `bug-reports/image/BUG-TDHSTVV_17-cbpd-khong-nhan-thong-bao-trinh-duyet.png`.

## Phát hiện thêm (ngoài 3 ý đối tác)

- **Không có hộp thoại xác nhận:** bấm "Trình duyệt" → chuyển trạng thái ngay, **không** hiện hộp thoại xác nhận. SRS dòng 1565 (ô 20d) quy định: Click → **MD-TRINH-DUYET** (dòng 1396: tiêu đề "Xác nhận trình phê duyệt?", nội dung cảnh báo không sửa được kết quả sau khi trình, nút "Trình duyệt").
- **Không ghi nhận người trình / ngày trình:** đọc bản ghi TVV sau thao tác → `nguoiGuiDuyetId = null`, `ngayGuiDuyet = null`, dù trạng thái đã là `CHO_PHE_DUYET`.

## Đối chiếu SRS (Cổng 3)

- `srs-fr-04-chuyen-gia-tvv.md` dòng 518 (Processing bước 4) — Trình duyệt → chuyển `CHO_PHE_DUYET` + **gửi thông báo CB_PD cùng đơn vị**. → Web: chuyển trạng thái **đúng**, **KHÔNG gửi thông báo**. **KHÔNG khớp.**
- dòng 551 (Acceptance Criteria) — "**Given** CB NV kết luận ĐẠT **When** nhấn 'Trình duyệt' **Then** TVV → CHO_PHE_DUYET, **CB PD nhận thông báo**". **KHÔNG khớp.**
- dòng 1565 (ô 20d) — Click → **MD-TRINH-DUYET** → đặt trạng thái Chờ phê duyệt + thông báo CB PD cùng đơn vị. → Web: **không có hộp thoại xác nhận**. **KHÔNG khớp.**
- dòng 1557-1559 — Nhóm 2/3/4 có **ô nhận xét** là một phần kết quả thẩm định. → Web: nhận xét **không được lưu**. **KHÔNG khớp.**
- `srs-v3.5.md` dòng 571 — **UI-04**: "Toast notification cho thao tác thành công". → Web: **không có thông báo**. **KHÔNG khớp.**

---

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data bug gốc: **CB_NV_TW `cbnv_tw`** thẩm định hồ sơ **TVV-BTP-TW-0010** (đơn vị BTP·TW), kết luận ĐẠT + nhập 3 ô Nhận xét → bấm "Trình duyệt"; sau đó đăng nhập **CB_PD_TW `cbpd_tw` cùng đơn vị** kiểm hộp thông báo.

**Kết quả FIXED (4/4 điểm):**
1. **Thông báo CB Phê duyệt:** cbpd_tw NHẬN thông báo "Hồ sơ TVV chờ phê duyệt — Hồ sơ TVV QA TVV RV17 TrinhDuyet đã được thẩm định và chờ phê duyệt" (mốc "2 phút trước", khớp thời điểm trình).
2. **Nhận xét lưu:** tải lại trang → 3 ô Nhận xét (Nhóm 2/3/4) hiển thị đầy đủ ở chế độ chỉ đọc.
3. **Toast thành công:** "Đã trình hồ sơ lên cấp phê duyệt" (MutationObserver).
4. **Hộp thoại xác nhận MD-TRINH-DUYET:** modal "Trình phê duyệt hồ sơ thẩm định — Sau khi trình... Bạn xác nhận trình phê duyệt?" [Hủy/Trình phê duyệt] hiện trước khi chuyển trạng thái.

⇒ Hồ sơ chuyển "Chờ phê duyệt". **PASS.** Ảnh: `bug-reports/image/TDHSTVV_17-reverify-cbpd-nhan-thong-bao-trinh-duyet.png`, `TDHSTVV_17-reverify-confirm-dialog-trinh-duyet.png`.
