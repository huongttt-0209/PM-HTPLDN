# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_01 (dòng 327) — Thẻ "Chờ phê duyệt" không chuyển dấu đỏ khi có hồ sơ

**Kết luận:** Pass — thẻ "Chờ phê duyệt" đang có 3 hồ sơ và huy hiệu nay là NỀN ĐỎ, đúng bằng màu của thẻ "Mới đăng ký".

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbpd_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Phê duyệt cấp Trung ương (`cbpd_tw_04`), đơn vị Cục Bổ trợ tư pháp – Bộ Tư pháp | `cbpd_tw` — vai trò `CB_PD_TW`, đơn vị hiển thị "Bộ Tư Pháp · Cục Bổ trợ tư pháp" (CÙNG vai trò + CÙNG cấp + CÙNG đơn vị với bug gốc; chỉ khác hậu tố tài khoản anh em) | Không |
| Màn hình / entity + trạng thái | Mạng lưới Tư vấn viên → Tổ chức tư vấn, thanh thẻ trạng thái | Đúng màn `/chuyen-gia-tvv/to-chuc` | Không |
| Dữ liệu tiền đề | Thẻ "Chờ phê duyệt" có 1 hồ sơ; thẻ "Mới đăng ký" cũng đang có hồ sơ (để so sánh) | Thẻ "Chờ phê duyệt" có **3** hồ sơ (TC-BTP-TW-0010, TC-STP-BG-0001, TC-STP-AG-0001) · thẻ "Mới đăng ký" có **1** hồ sơ (TC-BTP-TW-0011, tự tạo để dựng đủ điều kiện so sánh) ⇒ cả hai thẻ đều >0, đúng tình huống bug gốc | Không |
| Thao tác / input | Quan sát + so sánh màu huy hiệu 2 thẻ | Đọc màu nền THẬT bằng `getComputedStyle` (không đoán qua ảnh) trên cả 6 thẻ, cùng một lần chụp | Không |

**Số đo màu nền huy hiệu (cùng thời điểm, vai trò CB_PD_TW), đọc bằng `getComputedStyle`:**

- Thẻ "Đang hoạt động" — số đếm 8 — nền huy hiệu `rgb(9, 88, 217)` (xanh).
- **Thẻ "Chờ phê duyệt" — số đếm 3 — nền huy hiệu `rgb(245, 34, 45)` (ĐỎ).**
- Thẻ "Mới đăng ký" — số đếm 1 — nền huy hiệu `rgb(245, 34, 45)` (ĐỎ).
- Thẻ "Đã từ chối" / "Tạm dừng" / "Vô hiệu hóa" — 0 bản ghi — không có huy hiệu.

**Bằng chứng:** `image/QLDMTCTV_OOS_01-v2-01-cbpd_tw-the-cho-phe-duyet-huy-hieu-do-giong-moi-dang-ky.png` (đã mở đọc: thanh thẻ của tài khoản "Cán bộ PD Trung ương / CB_PD_TW" hiển thị "Chờ phê duyệt 3" với huy hiệu tròn ĐỎ nằm ngay cạnh "Mới đăng ký 1" cũng ĐỎ, còn "Đang hoạt động 8" là huy hiệu XANH) · đặc tả `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1628 ("tab + số đếm + chấm đỏ nếu >0") so với dòng 1627 của thẻ "Mới đăng ký" · network `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200].
