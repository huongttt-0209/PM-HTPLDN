# Hồ sơ đo — DGKQHTVV_04 (dòng 68) — GIAI ĐOẠN B

**Chuẩn chấm đã khóa:** [`../chuan/DGKQHTVV_04.md`](../chuan/DGKQHTVV_04.md) — `C1` `C2` route TEST · `C3` (làm tròn) để ngỏ cho người điều phối.
**Ô "Kết quả verify" trước khi ghi:** RỖNG ([`../audit/DGKQHTVV_04-ketqua-verify-CU.md`](../audit/DGKQHTVV_04-ketqua-verify-CU.md)).
**Bằng chứng đối tác:** KHÔNG CÓ (cột "Ảnh/vieo 1" của dòng 68 rỗng) ⇒ tiền đề suy từ chính "Điều kiện" + "Các bước" của phiếu.

---

## 1. Môi trường · bản dựng · tài khoản

| Hạng mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE lúc đo | **`assets/index-DsMHK7Dp.js`** (kiểm lại ngay sau khi tải lại trang — không đổi giữa lượt đo) |
| Tài khoản | `cbnv_tw_04` / `Test@1234` — `CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001` |
| Thời điểm | 07/08/2026 02:17 – 02:22 giờ VN |

## 2. Tiền đề (thoả đúng điều kiện cứng của chuẩn chấm §4.3)

| | |
|---|---|
| Vụ việc | **`VV-QAW7-DG01`** (`a7770001-0000-4000-8000-000000000001`) — "QAW7 — Vụ việc chờ chấm điểm" |
| Trạng thái trước khi đo | **`HOAN_THANH`** ("Hoàn thành") — đúng nhánh KHÔNG tranh chấp (né mâu thuẫn `:1751` ↔ `:1197`) |
| Đơn vị | `00000000-0000-4000-8000-000000000001` — **trùng đơn vị tài khoản đo** (`:1216`) |
| Đánh giá `CB_NV` trước đó | **KHÔNG có** — `danhGia = null`, nhóm Đánh giá hiện "Chưa có thông tin" |

Đã sàng 7 ứng viên `HOAN_THANH` cùng đơn vị bằng `GET /api/v1/vu-viecs/{id}` trước khi chọn; tất cả đều
`danhGia = null`. Chọn `VV-QAW7-DG01`, dự phòng `VV-QAW7-TRALOI-UBND`, `VV-QA-001` (không phải dùng đến).

## 3. 🔴 Khai báo thay đổi môi trường (Flow 04 §Giai đoạn B bước 4)

| Đổi bản ghi nào | Đổi gì | Trên env nào |
|---|---|---|
| `VV-QAW7-DG01` (`a7770001-…-000000000001`) | Tạo **1 bản ghi đánh giá loại `CB_NV`**: 4 · 8 · 9, nhận xét `QA-DGKQ-20260807-0220 bo diem phan biet 4-8-9 ky vong tong 7`, người đánh giá `CB Nghiệp vụ - Trung ương #04`. Hệ quả: trạng thái vụ việc **`HOAN_THANH` → `DA_DANH_GIA`** | `18.143.165.120.nip.io` (nội bộ) |

⚠️ Bản ghi này **đã bị tiêu hao** cho vế `C1`/`C2` — `:1219` + `:2114` chặn đánh giá lần 2 cùng loại người.
Muốn chạy lại phải dùng bản ghi khác (còn `VV-QAW7-TRALOI-UBND`, `VV-QAW7-TV-MANGLUOI`, `VV-QA-001`…`VV-QA-007`,
`VV-BTP-TW-20260712-005`, `EEE-VH-011`). Không đụng dữ liệu của đối tác.

## 4. Đường đo (UI thật) + đối chứng độc lập

1. Mở danh sách vụ việc → gõ mã `VV-QAW7-DG01` vào ô tìm kiếm bằng **bàn phím thật** → mở chi tiết.
2. Bấm nút **[Đánh giá]** → mở cửa sổ **"Đánh giá chất lượng"**.
3. **Chụp ảnh form khi CHƯA nhập gì** (bằng chứng `C2`).
4. Nhập **4 · 8 · 9** + chuỗi nhận xét mốc-giờ duy nhất. **Không chạm ô điểm tổng** (form không có ô đó).
5. Bấm **[Xác nhận]** — hành động tranh chấp thực hiện bằng UI thật, **bấm đúng 1 lần**.
6. **Tải lại trang bằng địa chỉ** → mở lại nhóm Đánh giá → đọc `innerText`.
7. Đối chứng: `GET /api/v1/vu-viecs/{id}` bằng chính phiên `cbnv_tw_04`.

---

## 5. Số đo

### 5.1 `C2` — hệ thống **tự** sinh điểm tổng, người dùng không nhập → **ĐẠT**

Cửa sổ "Đánh giá chất lượng" chỉ có **4 ô nhập**, đọc từ DOM:

| Ô | Tên nội bộ | Bắt buộc | Giá trị đã nhập |
|---|---|---|---|
| "Điểm chất lượng (0-10)" | `diemChatLuong` | Có (dấu `*`) | `4.0` |
| "Điểm thời gian (0-10)" | `diemTienDo` | Có (dấu `*`) | `8.0` |
| "Điểm thái độ (0-10)" | `diemThaiDo` | Có (dấu `*`) | `9.0` |
| "Nhận xét" | — | Không | chuỗi mốc-giờ, 60/2000 ký tự |

🔴 **Không có ô nào cho điểm tổng.** Chữ hiển thị trọn vẹn của cửa sổ:
`"Đánh giá chất lượng / Điểm chất lượng (0-10) / Điểm thời gian (0-10) / Điểm thái độ (0-10) / Nhận xét / 60 / 2000 / Hủy / Xác nhận"`
— không chứa chữ "tổng". Ảnh: [`../image/DGKQHTVV_04-form-truoc-khi-nhap-khong-co-o-diem-tong.png`](../image/DGKQHTVV_04-form-truoc-khi-nhap-khong-co-o-diem-tong.png).

⇒ Người dùng **không phải và không thể** tự nhập điểm tổng; giá trị vẫn được sinh ra (§5.2) ⇒ `C2` đạt.
Phù hợp **UI-13** (`srs-v3.5.md:585`): trường hệ thống tự gán **không** gắn dấu sao — đúng, vì ô này không tồn tại trên form.

### 5.2 `C1` — điểm tổng = trung bình cộng 3 điểm → **ĐẠT**

Thao tác gửi: `POST /api/v1/vu-viecs/a7770001-…-000000000001/danh-gia` → **HTTP 201**, xuất hiện **đúng 1 lần**
trong nhật ký mạng (không double-submit).

Sau khi **tải lại trang**, `innerText` vùng nhóm Đánh giá:

```
Điểm chất lượng tư vấn	4/10	Điểm đúng thời hạn	8/10	Điểm thái độ phục vụ	9/10
Điểm tổng (trung bình 3 điểm)	7/10	Người đánh giá	CB Nghiệp vụ - Trung ương #04	Ngày đánh giá	07/08/2026 02:18
Nhận xét	QA-DGKQ-20260807-0220 bo diem phan biet 4-8-9 ky vong tong 7
```

**Đối chứng độc lập** — `GET /api/v1/vu-viecs/a7770001-…-000000000001`:

```json
{"trangThai":"DA_DANH_GIA","diemDanhGia":7,
 "danhGia":{"diemChatLuong":4,"diemThoiGian":8,"diemThaiDo":9,"diemTong":7,
            "nhanXet":"QA-DGKQ-20260807-0220 bo diem phan biet 4-8-9 ky vong tong 7",
            "ngayDanhGia":"2026-08-06T19:18:28.092Z","nguoiDanhGia":"CB Nghiệp vụ - Trung ương #04"}}
```

| | Trên màn | Bản ghi máy chủ | Khớp |
|---|---|---|---|
| Điểm chất lượng tư vấn | `4/10` | `4` | ✅ |
| Điểm đúng thời hạn | `8/10` | `8` | ✅ |
| Điểm thái độ phục vụ | `9/10` | `9` | ✅ |
| **Điểm tổng** | **`7/10`** | **`7`** | ✅ |
| Nhận xét | đúng chuỗi mốc-giờ | đúng chuỗi | ✅ |

**Bộ điểm loại trừ được mọi công thức sai** (đúng yêu cầu chuẩn chấm §6.1 bẫy 1):

| Cách tính | Kết quả | Trùng số đo `7`? |
|---|---|---|
| **Trung bình cộng (4+8+9)/3** | **7** | ✅ **ĐÚNG** |
| Trung vị | 8 | ❌ |
| Nhỏ nhất | 4 | ❌ |
| Lớn nhất | 9 | ❌ |
| Tổng | 21 | ❌ |
| Trung bình 2 điểm đầu | 6 | ❌ |

⇒ Chỉ có công thức trung bình cộng 3 điểm cho ra `7`. **Hai đường đo khớp ⇒ dừng, không mở đường thứ ba.**
Ảnh sau khi tải lại: [`../image/DGKQHTVV_04-sau-tai-lai-diem-tong-7.png`](../image/DGKQHTVV_04-sau-tai-lai-diem-tong-7.png) (đã mở lại xem, khớp mô tả).

### 5.3 `C3` — làm tròn / chữ số thập phân → **QUYẾT ĐỊNH: NGOÀI PHẠM VI EXPECTED**

Chuẩn chấm §7 để ngỏ điểm này cho người điều phối chốt. **Chốt: `C3` không phải một vế của expected dòng 68.**

**Căn cứ (không phụ thuộc kết quả đo):** expected của dòng 68 là **đúng một câu** —
*"Tự động tính điểm tổng bằng trung bình cộng 3 điểm"* — **không nhắc gì** đến làm tròn hay số chữ số thập
phân. Flow 04 luật khóa 1: *"Tách đúng các vế trong expected đối tác, không thêm chức năng kế bên… Hành vi /
biến thể kế bên mà expected không nhắc thì **không thành tiêu chí chấm** và không được mở thêm phép đo."*

⇒ `C3` không tạo ra vế `GAP` cho case này, nên **không chặn Pass**. Đây **không phải** đổi quan hệ để khớp
kết quả (luật khóa 5): điểm này đã được nêu là ngỏ **từ Giai đoạn A**, và lý do loại nó nằm ở nội dung
expected chứ không ở số đo.

**Dữ kiện vẫn ghi lại cho đặc tả:** chuỗi hiển thị là `7/10`, không phần thập phân. Lượt này 4+8+9 = 21
**chia hết cho 3** nên **chưa lộ** quy tắc làm tròn. SRS vẫn **im lặng** cho UC67 (`srs-fr-05-vu-viec.md:2462`
loại trừ UC67 khỏi quy tắc làm tròn duy nhất) ⇒ nếu BA muốn chốt quy tắc thì cần một phép đo riêng bằng bộ
điểm không chia hết cho 3. **Không đo thêm trong case này** (luật khóa 3/4: expected không áp cho nhiều biến
thể, và bản ghi bị tiêu hao sau 1 lần).

---

## 6. Đối chiếu điều kiện với case đối tác

| Điều kiện | Đối tác | Lượt đo này | Ảnh hưởng |
|---|---|---|---|
| Vai trò | bước 1 là menu CMS ⇒ cán bộ | `CB_NV_TW` | Khớp |
| Trạng thái vụ việc | "Hoàn thành" **hoặc** "Đã đánh giá" | "Hoàn thành" | Khớp (chọn nhánh không tranh chấp) |
| Bước 4 của phiếu | Bấm "Đánh giá" rồi "Lưu đánh giá" | Bấm [Đánh giá] rồi [Xác nhận] | Nhãn nút khác — **không phải tiêu chí chấm**, SRS không quy định nhãn (`:1751`) |
| Env / bản dựng | `htpldn-uat.ospgroup.vn` | nội bộ, `index-DsMHK7Dp.js` | **Khác** ⇒ ghi giới hạn hiệu lực |

## 7. Cổng chốt verdict

| Câu hỏi | Trả lời |
|---|---|
| Vế chấm neo vào dòng SRS nào? | `C1` `:1208` + `:1220` + `:1734` + `:2120` (4 chỗ thống nhất) · `C2` `:1208` "Y (auto)" + `:1734` "AVG auto" + `:2120` "Auto = AVG(...)" + `srs-v3.5.md:585` |
| Mọi thao tác có trả lời một vế Cn không? | Có — 1 đường UI (nhập → gửi → tải lại → đọc) + 1 đối chứng máy chủ. Không đo chặn điểm ngoài 0–10, không đo chặn đánh giá lần 2, không đo chuyển trạng thái, không đo điểm trung bình tư vấn viên |
| Vế `DIFF/GAP` đã chặn Pass chưa? | Không còn vế `DIFF/GAP` nào trong phạm vi expected — xem §5.3 |
| Đã đọc đủ dòng 68 chưa? | Có, gồm cả ghi chú "đối tác xóa và đánh lệch ID" ⇒ kết quả neo vào **dòng 68** |
| Điều kiện đo khớp tiền đề case chưa? | Có, trừ env/bản dựng (đã khai) |

## 8. Verdict logic — **PASS**

Cả `C1` và `C2` đều `MATCH` và đều đạt bằng phép đo, có đối chứng độc lập khớp. Không còn vế `DIFF/GAP`
trong phạm vi expected ⇒ **Pass**.

⚠️ Theo Flow 04 §Ca biên: **không** viết *"fix đã có tác dụng"* — không có ảnh "lỗi cũ" của chính QA nên chỉ
kết luận được **hiện trạng đúng so với đặc tả**, không kết luận được fix có tác dụng hay không.

Hiệu lực: env nội bộ `18.143.165.120.nip.io`, bó mã `index-DsMHK7Dp.js`, 07/08/2026 02:22.

## 9. Bug mới / candidate

Không có bug mới tự lộ trong bước bắt buộc của `C1`/`C2`.

**Ghi nhận chéo (không đổi verdict dòng 68):** trên chính màn này, ô giá trị cột thứ nhất của bảng nhóm
Đánh giá bị **bẻ dòng** — `4/1`⏎`0` và `7/1`⏎`0`. Hiện tượng này thuộc vế `C5` của **dòng 65**, đã được ghi
vào ô "Kết quả verify" của dòng 65 kèm chẩn đoán nguyên nhân (cột giá trị thứ nhất chỉ rộng 64px / vùng chữ
31px, trong khi cột 2 rộng 238px và cột 3 rộng 152px). SRS im lặng ⇒ không log thành bug riêng, đã thành
câu hỏi BA ở dòng 65.
