# Bảng đối chiếu điều kiện — QLDMTCTV_05 (dòng 318) — Thẻ trạng thái: số đếm, nhãn đỏ, phân quyền thẻ "Chờ phê duyệt"

**Kết luận:** Pass — cả 3 ý đối tác nêu đều không còn tái hiện (có số đếm · thẻ "Mới đăng ký" huy hiệu nền đỏ khi có hồ sơ chưa trình · thẻ "Chờ phê duyệt" ẩn với Cán bộ Nghiệp vụ).

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (cbnv_tw + cbpd_tw, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Ảnh đối tác chụp ở vai trò Cán bộ Nghiệp vụ (thấy thẻ "Chờ phê duyệt" là sai) | `cbnv_tw` (CB_NV_TW, Cục Bổ trợ tư pháp – Bộ Tư pháp) → chỉ **5 thẻ**, KHÔNG có "Chờ phê duyệt". `cbpd_tw` (CB_PD_TW, cùng đơn vị) → **6 thẻ**, có "Chờ phê duyệt 3" | Không |
| Màn hình / entity + trạng thái | Mạng lưới Tư vấn viên → Tổ chức tư vấn, thanh thẻ trạng thái | Đúng màn `/chuyen-gia-tvv/to-chuc` | Không |
| Dữ liệu tiền đề (ý 1 – số đếm) | Không rõ đối tác có bao nhiêu bản ghi | Đang hoạt động **8** · Chờ phê duyệt **3** · Mới đăng ký **1**; số trên thẻ khớp đúng số dòng trong bảng ở cả 5/6 thẻ. Thẻ 0 bản ghi (Đã từ chối / Tạm dừng / Vô hiệu hóa) để trống, không hiện số 0 | Không |
| Dữ liệu tiền đề (ý 2 – nhãn đỏ) | "tồn tại tổ chức chưa trình duyệt" mà thẻ vẫn không đỏ | Đầu phiên thẻ "Mới đăng ký" đang RỖNG → **tự tạo** tổ chức mới và cố ý không trình duyệt (TC-BTP-TW-0010, sau đó TC-BTP-TW-0011) để dựng đúng tình huống. Đo màu nền huy hiệu bằng `getComputedStyle`: "Mới đăng ký" = `rgb(245,34,45)` (ĐỎ) trong khi "Đang hoạt động" = `rgb(9,88,217)` (XANH) cùng lúc | Không |
| Thao tác / input | Bấm lần lượt từng thẻ | Bấm đủ 5 thẻ với cbnv_tw: danh sách lọc đúng, trạng thái mọi dòng khớp tên thẻ (Đang hoạt động 8/8 · Mới đăng ký 1/1 · 3 thẻ còn lại 0 dòng). Bấm thẻ "Chờ phê duyệt" với cbpd_tw: 3 dòng đều "Chờ phê duyệt" | Không |

**Ghi chú quan sát (không phải lỗi đối tác nêu):** thẻ chưa có bản ghi thì không hiện số `0` — đặc tả dòng 1625–1630 chỉ ghi "tab + số đếm", không quy định cách hiển thị khi bằng 0; đây cũng đúng thông lệ thư viện giao diện. Triệu chứng gốc "mỗi thẻ không hiển thị số đếm" (khi đó KHÔNG thẻ nào có số) đã hết.

**Bằng chứng:**
- `image/QLDMTCTV_05-v2-01-cbnv_tw-5-the-co-so-dem-moi-dang-ky-huy-hieu-do.png` — vai trò CB_NV_TW: thanh thẻ có **5 thẻ**, "Đang hoạt động" huy hiệu xanh số 8, "Mới đăng ký" huy hiệu **ĐỎ** số 1, không có thẻ "Chờ phê duyệt".
- `image/QLDMTCTV_05-v2-02-cbpd_tw-thay-du-6-the-co-cho-phe-duyet.png` — vai trò CB_PD_TW: **6 thẻ**, có "Chờ phê duyệt" huy hiệu đỏ số 3.
- Đo màu bằng `getComputedStyle` (không đoán qua ảnh): Đang hoạt động `rgb(9,88,217)` · Mới đăng ký `rgb(245,34,45)` · Chờ phê duyệt `rgb(245,34,45)`.
- Đặc tả: `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1627 (Mới đăng ký — "tab + số đếm + chấm đỏ nếu >0"), dòng 1628 (Chờ phê duyệt — "Hiển thị khi vai trò là Cán bộ Phê duyệt").
- Network: `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` [200] → HOAT_DONG 8 · CHO_PHE_DUYET 3 · MOI_DANG_KY 1.
