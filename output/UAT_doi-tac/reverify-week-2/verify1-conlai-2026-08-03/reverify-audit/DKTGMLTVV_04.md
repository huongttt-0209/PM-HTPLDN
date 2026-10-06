# DKTGMLTVV_04 — evidence audit (verify vòng 1, 2026-08-03)

## 0. Note CŨ của dev ở cột R (backup TRƯỚC khi đè)

> **R122 (DEV phản hồi lần 1) — giá trị cũ, dev ghi:**
> KHÔNG phải bug: Nhóm 3 gồm đúng 3 trường (Tổ chức chính / Tổ chức đối tác / Lĩnh vực) theo SRS v3.5 SCR-IV-02:1514. "Tổ chức đối tác" là trường được SRS quy định (kỳ vọng đang bám SRS v2.0 cũ).

> **P122 (Trạng thái dev fix 1) — giá trị hiện tại:** `Reject` (KHÔNG đụng vào cột P)

---

## 1. Cổng 1 — Bằng chứng đối tác (đã mở XEM full-res)

- **File:** `partner-evidence/DKTGMLTVV_04_v2.jpg` (219.226 bytes, md5 `929d428dafad27beab53ef1266866053`).
- ⚠️ **Ảnh này TRÙNG md5 với `DKTGMLTVV_05_v2.jpg`** — đối tác gắn cùng một ảnh cho 2 case. Tuy nhiên ảnh **CÓ chứa Nhóm 3** nên Cổng 1 của case 122 vẫn đóng được; không phải ô TRỐNG.
- **Đã mở đọc full-res**, không đọc từ montage thu nhỏ.

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Giá trị đọc từ ảnh |
|---|---|---|
| a | URL / màn hình | `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi` — breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới" |
| b | Trạng thái entity / vai trò đang đứng | Form tạo mới (chưa có bản ghi). Góc phải: "BTP · DP", "hương 3 NHT", nhãn vai trò **NHT** |
| c | Dữ liệu tiền đề | Không cần bản ghi — form rỗng, các trường nhóm 3 còn nguyên placeholder |

## 2. Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `DKTGMLTVV_04_v2.jpg`, vùng chứa lỗi = phần giữa ảnh, nhóm thu gọn "Tổ chức & Mạng lưới". Trong khung đó thấy **3 trường**: "Tổ chức hành nghề chính" (có dấu \*), "Tổ chức đối tác", "Lĩnh vực pháp luật" (có dấu \*).
2. **Đối tác phản ánh CỤ THỂ:** cột L ghi *"Nhóm 3 — Lĩnh vực pháp luật và Tổ chức: SRS quy định chỉ hiển thị các trường Lĩnh vực pháp luật đăng ký, Tổ chức tư vấn chủ quản. Nhưng hệ thống hiển thị nhiều hơn"* → tức đối tác kỳ vọng **2 trường**, web hiện **3**, trường "thừa" theo họ là **"Tổ chức đối tác"**.
3. **Data + bước tái hiện:** không cần seed. Đăng nhập NHT → Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → tab "Mới đăng ký" → nút "Thêm mới" → cuộn tới nhóm "Tổ chức & Mạng lưới".

> **Lưu ý nguồn:** cột O (TKM phản hồi lần 1) ghi *"Do tài liệu SRS được bàn giao lần 2 ngày 10/7 (v2.0) thay đổi nên log bug thay đổi theo"* → đối tác đang bám một bản SRS đánh số **v2.0**, còn QA/dev bám bản **v3.5** trong `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Đây là **mâu thuẫn giữa các nguồn**, không phải sai thao tác.

## 3. Verify LIVE trên web (Chrome DevTools MCP)

- **Env:** `https://18.143.165.120.nip.io` — build hiển thị ở sidebar: **HTPLDN · V1.0.5**.
- **Account:** `nht_qa_tw` / `Test@1234` → header hiện "QA NHT Trung uong", nhãn vai trò **NHT**, đơn vị **BTP · TW**. OTP lấy qua MailHog `18.143.165.120:8025` (`nht.qa.tw@htpldn.test`, mã 569541).
  - *Vì sao không dùng bộ `_02` như user yêu cầu:* bộ `_02` chỉ có các vai trò **CB Nghiệp vụ / CB Phê duyệt** (`cbnv_*_02`, `cbpd_*_02`). Case này bắt buộc vai trò **NHT** (chỉ NHT mới submit hồ sơ ứng viên — SRS :1476/:1477), mà NHT không có biến thể `_02` → dùng `nht_qa_tw`, đúng vai trò của đối tác trong ảnh.
  - **Không dùng admin** để ra verdict (protocol §Nguyên tắc 3).
- **Đường đi:** click sidebar (KHÔNG `navigate_page` — Rule 3) → "Tư vấn viên / Chuyên gia" → tab **"Mới đăng ký"** → nút **"Thêm mới"** → `/chuyen-gia-tvv/tao-moi`. Đúng 3 bước đối tác mô tả ở cột J.

### Đo DOM bằng `innerText` (CẤM `textContent` — postmortem §4)

Lần đo đầu trả `fieldCount: 0` cho mọi nhóm. **Không kết luận "form hỏng"** mà đọc HTML thô trước (postmortem §4, dòng "Selector không khớp") → phát hiện app dùng class `.ant-collapse-body`, không phải `.ant-collapse-content`. Sửa selector rồi đo lại:

| Nhóm trên web | Số trường đếm được |
|---|:-:|
| Thông tin cá nhân | 10 |
| Nghề nghiệp | 13 |
| **Tổ chức & Mạng lưới** | **3** |
| File đính kèm | 1 |
| Ghi chú | 1 |

**Nhóm 3 — danh sách trường đầy đủ, không cắt:**
1. `Tổ chức hành nghề chính` — dropdown có tìm kiếm, **không bắt buộc**, `id="toChucChinhId"`
2. `Tổ chức đối tác` — dropdown chọn nhiều, **không bắt buộc**
3. `Lĩnh vực pháp luật *` — dropdown chọn nhiều, **bắt buộc**

→ **Không có trường thứ 4.**

### Phủ cả 2 giá trị dropdown "Loại"

| Giá trị "Loại" | Số trường nhóm 3 | Danh sách |
|---|:-:|---|
| Tư vấn viên (TVV) — mặc định | 3 | Tổ chức hành nghề chính · Tổ chức đối tác · Lĩnh vực pháp luật \* |
| Chuyên gia (CG) | 3 | Tổ chức hành nghề chính · Tổ chức đối tác · Lĩnh vực pháp luật \* |

Giá trị "Loại" sau khi đổi được xác nhận lại bằng cách đọc thẳng `innerText` của ô đó = `"Chuyên gia (CG)"` (`id="loaiTvv"`) — không tin vào phép đo trả `null` ban đầu.

### Ảnh bằng chứng — ĐÃ MỞ ĐỌC

`image/DKTGMLTVV_04-web-nhom3.png` (viewport full-res 2880×1472). Mở ra đọc thấy: header "Tổ chức & Mạng lưới"; bên dưới đúng 3 ô — "Tổ chức hành nghề chính" (placeholder *Tìm kiếm tổ chức tư vấn...*), "Tổ chức đối tác" (placeholder *Chọn tổ chức đối tác (có thể chọn nhiều)*), "\* Lĩnh vực pháp luật" (placeholder *Chọn lĩnh vực hoạt động*, dấu \* đỏ). Ngay dưới là header nhóm kế tiếp "File đính kèm" → xác nhận nhóm 3 kết thúc sau 3 trường, không có trường bị khuất. Góc phải ảnh: "BTP · TW · QA NHT Trung uong · NHT".

- Console: **0 lỗi / 0 cảnh báo**.
- Network (xhr/fetch): 22 request, **không có 4xx/5xx** nào sau khi đăng nhập (chỉ 1 `GET /api/v1/auth/me [401]` là lần thăm dò TRƯỚC đăng nhập — bình thường).

## 4. Cổng 3 — Bảng đối chiếu SRS vs web

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — **đã mở file đọc lại số dòng, không dùng trí nhớ**. Màn hình SCR-IV-02 (dòng 1470), FR sử dụng: **FR-IV-03 (UC41)** / FR-IV-04.

| SRS (dòng) | SRS yêu cầu | Web thực tế | Đạt? |
|---|---|---|:-:|
| :1514 | Nhóm 3 tên **"Tổ chức & Mạng lưới"**, nhóm thu gọn | Nhóm 3 tên "Tổ chức & Mạng lưới", thu gọn được | ✅ |
| :1515 | 4.1 **Tổ chức chính** — dropdown có tìm kiếm, tùy chọn | "Tổ chức hành nghề chính" — dropdown có tìm kiếm, không bắt buộc | ✅ |
| :1516 | 4.2 **Tổ chức đối tác** — dropdown chọn nhiều, tùy chọn (N:N) | "Tổ chức đối tác" — dropdown chọn nhiều, không bắt buộc | ✅ |
| :1517 | 4.3 **Lĩnh vực pháp luật \*** — dropdown chọn nhiều, bắt buộc ≥ 1 | "Lĩnh vực pháp luật \*" — dropdown chọn nhiều, bắt buộc | ✅ |
| — | Không có mục 4.4 trong SRS | Web cũng không có trường thứ 4 | ✅ |

**→ Web khớp 100% SRS v3.5 cho nhóm 3. Không có trường thừa, không có trường thiếu.**

## 5. Lập luận verdict

- **Không phải `Open`:** tiêu chí Open của case này là "UI hiện trường THỨ 4 ngoài danh sách :1515-1517". Đo thực tế: đúng 3 trường, ở cả 2 giá trị "Loại". Không có trường thứ 4 → không sai clause SRS nào.
- **Không phải `Reject`:** protocol §Verdict quy định `Reject` **chỉ** dùng khi chứng minh được đối tác **thao tác/hiểu sai về THỰC TẾ**, tức lỗi họ báo *không có thật*. Ở đây đối tác **quan sát đúng thực tế** — ảnh của họ thể hiện đúng 3 trường, và web của ta cũng đúng 3 trường. Họ không thao tác sai bước nào (bước ở cột J trùng khớp bước ta chạy). Cái lệch là **kỳ vọng**: họ căn theo bản SRS ghi 2 trường. Protocol nói rõ: *"KHÔNG dùng Reject cho bất đồng kỳ vọng vs SRS (dù web đúng SRS)"* và *"evidence đúng actual mà chỉ tranh chấp expected/spec → BA confirm, không Reject"*.
- **→ `BA confirm`:** đúng định nghĩa *"Expected/kỳ vọng đối tác KHÁC SRS (kể cả khi SRS đã ghi rõ — đối tác quan sát đúng thực tế nhưng kỳ vọng thứ SRS quy định khác)"* **và** *"mâu thuẫn giữa các nguồn"* — cột O cho thấy đối tác bám bản SRS đánh số v2.0 (bàn giao 10/7), QA/dev bám v3.5.
- **Về P = `Reject` của dev:** đây là **claim của dev**, không ràng buộc QA. Nội dung kỹ thuật dev nói (3 trường theo :1514) là **đúng sự thật** — QA đã tự đo lại và xác nhận. Nhưng **cách phân loại** thì sai: chốt `Reject` cho một bất đồng đặc tả là vượt quyền dev/QA, phải để BA quyết. QA giữ nguyên P (không đụng), chỉ set Q = `BA confirm`.

### Tiền lệ: BA ĐÃ soi chính nhóm 3 này ngày 30/07/2026

Changelog SRS v3.5 dòng 26 (mục "Apply chốt UAT tuần 2 vòng 2") ghi:

> *"(2) `to_chuc_chinh_id` Y→N cho khớp **SCR-IV-02 mục 4.1**, FR-IV-03 §Inputs #14 và baseline — tư vấn viên tự do được để trống (**DKTGMLTVV_03** phần Open)"*

Tức BA đã trực tiếp xem xét **mục 4.1 = "Tổ chức chính"**, tức là **một trong 3 trường của chính nhóm 3 này**, khi xử lý case anh em `DKTGMLTVV_03` ở vòng 2 tuần 2. Trong đợt chốt đó BA **sửa mục 4.1 nhưng KHÔNG gỡ mục 4.2 "Tổ chức đối tác"** — và cùng đợt còn khẳng định *"form giữ đúng 5 nhóm, không tách nhóm thứ 6"*.

→ Đây là tín hiệu mạnh rằng cấu trúc 3 trường của nhóm 3 là **có chủ đích và đã qua tay BA gần đây**, không phải sót. Ghi ra đây để BA chốt nhanh, nhưng **không thay QA tự kết luận Reject** — thẩm quyền xác nhận đặc tả vẫn là của BA (protocol §Nguyên tắc 1).

**Câu hỏi cụ thể cho BA:**
1. Bản SRS nào là chuẩn cho màn SCR-IV-02 nhóm 3 — bản v3.5 (`srs-fr-04-chuyen-gia-tvv.md` :1514-1517, 3 trường) hay bản đối tác gọi là "v2.0" bàn giao 10/7 (2 trường)?
2. Trường **"Tổ chức đối tác"** (:1516, quan hệ N:N) có giữ lại trên form Thêm mới TVV không? Nếu bỏ thì phải cập nhật SRS v3.5; nếu giữ thì cập nhật lại tài liệu phía đối tác. (Gợi ý: BA đã đụng mục 4.1 cùng nhóm ngày 30/07 mà giữ nguyên 4.2.)

## 6. Ngoài tiêu chí BA — có thấy gì bất thường không?

Dựa trên ảnh đã đọc + DOM đã đo (không suy đoán). **Trong phạm vi nhóm 3: không phát hiện thêm bất thường** — 3 ô đều render đúng, không tràn, không đè, không lẫn tiếng Anh, console 0 lỗi, network 0 request 4xx/5xx.

Quan sát **ngoài phạm vi nhóm 3** (ghi lại để không rơi khỏi tầm nhìn — postmortem §C1), đều là **lệch nhãn so với SRS**, thuộc nhóm 1/2/4 nên là phạm vi của các mã TC khác (DKTGMLTVV_02/03/05), **chưa tự log**:

| Nơi | SRS ghi | Web hiện | Ghi chú |
|---|---|---|---|
| Tiêu đề nhóm 2 | "Thông tin nghề nghiệp" (:1500) | "Nghề nghiệp" | rút gọn nhãn |
| Nhóm 1, mục 2.7 | "Số Căn cước công dân" (:1495) | "Số CMND/CCCD" | SRS dùng thuật ngữ mới, web còn "CMND" |
| Nhóm 2, mục 3.1 | "Trình độ" (:1503) | "Trình độ học vấn" | thêm chữ |
| Nhóm 4, mục 5.1 | "Bằng cấp / Chứng chỉ **\***" — **bắt buộc** khi NHT đăng ký ứng viên mới (:1519) | "File đính kèm (Bằng cấp / Chứng chỉ)" — **không có dấu \***, không bắt buộc | thuộc case 123 (DKTGMLTVV_05) đang chờ verify |

→ Đã báo lại cho người điều phối để quyết có mở dòng TC mới hay gộp vào case liên quan; **không tự ý bỏ qua**.
