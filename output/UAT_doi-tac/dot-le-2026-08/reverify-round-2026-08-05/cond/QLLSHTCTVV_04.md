# Bảng đối chiếu điều kiện — QLLSHTCTVV_04 (re-verify vòng 1, 05/08/2026)

Loại bug: **ô lọc "Trạng thái vụ việc" bỏ sót phần lớn dữ liệu của chính bảng** → phụ thuộc trạng thái thật của các vụ việc trong hồ sơ ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 1*) CÓ khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy nguyên khối đó làm tiêu chí (Precondition / ✅ PASS khi / ❌ FAIL nếu / dòng ⚠️).

| Điều kiện | Bug gốc (khối CÁCH VERIFY) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | `cbnv_tw` | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp · cấp TW | Không |
| Hồ sơ | TVV-BTP-TW-0002 | Đúng hồ sơ **TVV-BTP-TW-0002** — "QA TVV Seed28 Active" | Không |
| Màn hình 1 | Tab "Lịch sử hỗ trợ" của hồ sơ đó | Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → chi tiết hồ sơ → thẻ **Lịch sử hỗ trợ** | Không |
| Tiền đề dữ liệu màn 1 | 6 vụ việc trải trên nhiều trạng thái | Hồ sơ nay có **8 vụ việc** trải trên nhiều trạng thái (gồm cả vụ đã hoàn thành lẫn vụ còn đang trong quy trình) — vẫn đủ để đo "có vụ việc nào lọt lưới không" | Không |
| Bước 1 | Không lọc: đếm tổng số vụ việc bảng trả về | Bỏ trống ô lọc, đọc tổng bảng trả về | Không |
| Bước 2 | Lần lượt chọn từng giá trị của ô lọc, ghi số vụ việc mỗi lần | Chọn **từng lựa chọn một** (xóa lựa chọn cũ trước mỗi lần đo) và ghi số vụ việc | Không |
| Bước 3 | Cộng kết quả của tất cả các giá trị lại | Cộng ba số, so với tổng khi không lọc; đồng thời chọn **cả ba lựa chọn cùng lúc** để đối chứng | Không |
| Bước 4 — màn hình 2 | Lặp bước 1-3 ở tab "Vụ việc đã hỗ trợ" của màn Người hỗ trợ pháp lý | Vào **Người hỗ trợ pháp lý** → chi tiết **NHT-STP-AG-0001** ("QA NHT An Giang UAT2") → thẻ **Vụ việc đã hỗ trợ**, lặp đúng bước 1-3 | Không |
| Kiểm nhãn lựa chọn | Ô lọc không được còn lựa chọn tên "Đã hủy" | Đọc **toàn bộ danh sách lựa chọn** của ô lọc ở cả hai màn | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò, đúng hồ sơ, đo đủ cả hai màn hình mà phiếu yêu cầu, chạy trọn tới chỗ sinh ra lỗi cũ (không chấm bằng quan sát tĩnh).

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Màn 1 — tab "Lịch sử hỗ trợ" của hồ sơ TVV-BTP-TW-0002

- ✅ **Không lọc: 8 vụ việc.**
- ✅ Lọc từng lựa chọn: **Đang xử lý → 5** · **Hoàn thành → 3** · **Từ chối → 0**.
- ✅ **Cộng lại đúng bằng tổng khi không lọc**: 5 + 3 + 0 = **8**. **Không vụ việc nào nằm ngoài mọi lựa chọn** — khác hẳn tình trạng cũ (4/6 vụ việc không lựa chọn nào lọc ra được).
- ✅ Chọn **cả ba lựa chọn cùng lúc** cũng ra đúng **8** — đối chứng thêm một lượt.
  Ảnh (ba lựa chọn, không có "Đã hủy"): [`../image/QLLSHTCTVV_04-r1-ba-lua-chon-tong-8.png`](../image/QLLSHTCTVV_04-r1-ba-lua-chon-tong-8.png)
  Ảnh (lọc "Từ chối" ra 0 — hồ sơ không có vụ việc bị từ chối): [`../image/QLLSHTCTVV_04-r1-loc-tu-choi-0.png`](../image/QLLSHTCTVV_04-r1-loc-tu-choi-0.png)

### Màn 2 — tab "Vụ việc đã hỗ trợ" của màn Người hỗ trợ pháp lý

- ✅ **Không lọc: 1 vụ việc** (VV-STP-AG-20260712-003, trạng thái hiển thị **Chờ phê duyệt**).
- ✅ Lọc từng lựa chọn: **Đang xử lý → 1** · **Hoàn thành → 0** · **Từ chối → 0**; cộng lại = **1** = tổng khi không lọc.
- ✅ Đây đúng là trường hợp trước kia lọt lưới: vụ việc ở "Chờ phê duyệt" nay **được lựa chọn "Đang xử lý" gom vào**, không còn nằm ngoài mọi lựa chọn.
- ✅ **Hai màn cho kết quả nhất quán** — cùng ba lựa chọn, cùng nguyên tắc gom, đều không bỏ sót bản ghi nào.
  Ảnh: [`../image/QLLSHTCTVV_04-r1-nht-loc-dang-xu-ly.png`](../image/QLLSHTCTVV_04-r1-nht-loc-dang-xu-ly.png)

### Nhãn lựa chọn

- ✅ Ô lọc ở **cả hai màn** chỉ có đúng ba lựa chọn **"Đang xử lý" · "Hoàn thành" · "Từ chối"**. **Không còn lựa chọn tên "Đã hủy"**.

### Ý note dặn KHÔNG chấm FAIL — tôn trọng

- ⚠️ Ô lọc **không mở ra đủ 12 trạng thái** — đúng như BA đã chốt giữ tập rút gọn ba lựa chọn. Không dùng ý này để chấm phiếu.

### Kết luận

Ở cả hai màn, tổng số vụ việc lọc được qua tất cả các lựa chọn bằng đúng tổng số khi không lọc, không bản ghi nào lọt lưới, và ô lọc không còn lựa chọn "Đã hủy" → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Ô lọc "Trạng thái vụ việc" cho phép **chọn nhiều lựa chọn cùng lúc**, nên khi đo từng lựa chọn phải xóa lựa chọn cũ trước. Chỉ ghi lại để đối tác biết cách đọc số liệu.
- Danh sách Người hỗ trợ pháp lý mà cán bộ Trung ương nhìn thấy chỉ có **1 hồ sơ** (NHT-STP-AG-0001) và hồ sơ này chỉ có 1 vụ việc, nên phép đo ở màn thứ hai có cỡ mẫu nhỏ. Không thuộc phạm vi phiếu, chỉ ghi lại.
