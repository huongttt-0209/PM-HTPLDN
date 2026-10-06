# QLDKTK_01 — Audit verify (dòng 321, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày verify:** 2026-08-03 · **Người verify:** QA (Chrome DevTools MCP)
**Môi trường:** https://18.143.165.120.nip.io · **Bản dựng ghi nhận:** `HTPLDN · V1.0.5` (đọc ở chân thanh menu sau khi đăng nhập, ảnh `image/QLDKTK_01-11-dang-nhap-thanh-cong-bang-MST.png`); gói giao diện `assets/index-BrKDNUvo.js`
**Hộp thư giả lập:** http://18.143.165.120:8025/
**Verdict:** **`Resolved`** ghi vào cột **Q (`Verify`)**. Cột **P (`Trạng thái dev fix 1`) giữ nguyên `Reject`** — KHÔNG đụng.
**Bảng đối chiếu điều kiện + Cổng 1/2/3 đầy đủ:** [`cond/QLDKTK_01.md`](../cond/QLDKTK_01.md)

---

## 1. Nguyên văn dữ liệu dòng 321 trước khi QA ghi

Sao lưu gốc: [`_backup-dev-note-321-QLDKTK_01.md`](_backup-dev-note-321-QLDKTK_01.md)

| Cột | Giá trị nguyên văn |
|---|---|
| Mã TC | `QLDKTK_01` |
| Mô tả | `Quản lý đăng ký tài khoản trên hệ thống` |
| Điều kiện | `1. Truy cập hệ thống` |
| Dữ liệu đầu vào | *(trống)* |
| Các bước thực hiện | `1. Chọn "Đăng ký tài khoản doanh nghiệp"` / `2. Nhập thông tin hợp lệ và nhấn Đăng ký` |
| Kết quả mong đợi | `Dữ liệu hợp lệ, hệ thống hiển thị trang xác nhận "Đăng ký thành công. Vui lòng kiểm tra thư điện tử và nhấn liên kết kích hoạt để đặt mật khẩu".` |
| Kết quả thực tế | `Một số trường thông tin không giống với tài liệu` |
| Ảnh/vieo 1 | `QLDKTK_02.webm` |
| Trạng thái 1 | `Fail` |
| Trạng thái dev fix 1 (P) | `Reject` |
| Verify (Q) | *(trống)* |

### Nguyên văn note của DEV ở cột R (trước khi QA ghi đè)

> KHÔNG phải bug: Chặn "MST đã tồn tại" khi MST đã có trong DOANH_NGHIEP là ĐÚNG SRS (srs-fr-10:1078). Triệu chứng do dữ liệu test (lượt trước đã tạo DN cùng MST) — dùng MST mới hoặc chức năng Quên mật khẩu để verify.

---

## 2. Hai cái bẫy của case này — đã xử lý ra sao

### Bẫy 1 — bằng chứng đính kèm lệch mã TC

- Ô "Ảnh/vieo 1" của dòng 321 ghi **`QLDKTK_02.webm`**, tức tệp mang mã của **case khác**. Theo `id-crosswalk.csv`, `QLDKTK_02` là một dòng độc lập (partner_row 1223 ↔ log_row 185).
- Xử lý: **vẫn tải và trích khung hình ra xem** (`tools/fetch_evidence.py --row 321` báo *"Link Drive tìm thấy: 1"*, không rỗng → Cổng 1 không rơi vào nhánh ô TRỐNG), ghi lại đầy đủ những gì quan sát được vào Cổng 1 của `cond/QLDKTK_01.md`, **nhưng ghi rõ là bằng chứng lệch mã TC nên KHÔNG dùng làm căn cứ verdict**.
- **Không suy ra bất cứ điều gì từ tên tệp.** Verdict dựa 100% vào phép đo trực tiếp trên bản dựng hiện tại.
- Ghi nhận trung thực: **nội dung** video lại đúng chủ đề của dòng 321 (đối tác mở song song tài liệu `HTPLDN-PTYC-CT-v2.0(1).docx` mục *4.10.8.2 — Trang Đăng ký tài khoản doanh nghiệp* và biểu mẫu đăng ký, rà từng dòng bảng trường). Nhưng video **dừng ở ô "Ghi chú"**, **không bấm Đăng ký**, **không có khung nào hiện trang xác nhận** ⇒ dù có coi là bằng chứng của dòng 321 thì nó cũng chỉ chứng minh phần *trường thông tin*, không chứng minh phần *trang xác nhận*.

### Bẫy 2 — dev trả lời lạc đề

- Note dev nói về **"chặn MST đã tồn tại"**. Đó là nội dung của case **QLDKTK_04 (dòng 187)**, **không phải** khiếu nại của dòng 321.
- Khiếu nại của dòng 321 là **"một số TRƯỜNG THÔNG TIN không giống tài liệu"**. Vì vậy QA **không đi theo hướng MST** của dev, mà đi hướng đúng: **đối chiếu từng trường của biểu mẫu với bảng Thành phần màn hình SCR-VIII-08**.
- Để chắc chắn không vô tình rơi vào nhánh MST của dev, lượt đo dùng **mã số thuế và email hoàn toàn mới** ⇒ máy chủ trả **201** chứ không trả lỗi trùng, xác nhận đã đo đúng nhánh "dữ liệu hợp lệ" mà bước 2 của case yêu cầu.

---

## 3. Trình tự đo (chống thiên kiến — đo trước, đọc đặc tả sau)

| Bước | Việc | Kết quả cốt lõi |
|---|---|---|
| A | Liệt kê toàn bộ thành phần biểu mẫu **trước khi mở SRS** — quét cây DOM theo `label` (dùng `innerText`) + mở ảnh ra đọc; bung cả 5 ô chọn; di chuột đọc 2 chú thích; kiểm `multiple` của vùng tải tệp | **28 thành phần nhập + 2 nút**, chia 3 mục: *Thông tin doanh nghiệp* · *Quy mô (theo NĐ39/2018)* · *Tài khoản đăng nhập* |
| B | Mở `srs-v3.5/srs-fr-10-quan-tri.md` — SCR-VIII-08 (bảng trường **dòng 1907–1939**, tiêu đề dòng 1895, ghi chú dòng 1941) + FR-VIII-22 (tiêu đề **dòng 1024**, bảng Inputs **dòng 1042–1072**) | Bảng SCR-VIII-08 có **đúng 30 dòng** = 24 trường DN + 4 mục tài khoản + 2 nút. Đối chiếu 1-1 → **khớp hoàn toàn**, chỉ 1 điểm lệch kiểu điều khiển |
| C | Chạy thật luồng đăng ký với mã số thuế `9908032201` + email `qa.qldktk01.20260803@htpldn.test` (đều mới) | **1 request / 1 thông báo**, HTTP **201**, `CHO_KICH_HOAT`; thư kích hoạt về; bấm liên kết → `HOAT_DONG`; đăng nhập lại bằng mã số thuế → vào được |

> Số dòng SRS ở bảng trên **đều đã mở file xác minh**, không lấy từ trí nhớ. Số dòng gợi ý trong đề bài (FR-VIII-22 "quanh dòng 1030") thực tế là dòng **1030** của mục *Màn hình:* trong khối FR-VIII-22 — khối FR bắt đầu ở **dòng 1024**, bảng Inputs ở **1042–1072**.

---

## 4. Bảng lệch trường — kết quả cuối

**Không có trường nào thiếu, không có trường nào thừa.** Đối chiếu 1-1 chi tiết 30 dòng đặt ở [`cond/QLDKTK_01.md`](../cond/QLDKTK_01.md) §"Đối chiếu 1-1 TỪNG trường". Tóm tắt các điểm từng bị đối tác nêu:

| Điều đối tác thấy trên bản dựng của họ | Đặc tả nói gì | Bản dựng hiện tại | Kết quả |
|---|---|---|---|
| Thừa ô **"Họ và tên người đăng ký"** (bắt buộc), đặt ở đầu biểu mẫu | SCR-VIII-08 dòng 1907–1939 và Inputs dòng 1042–1072 **không có** trường này | **Đã gỡ khỏi biểu mẫu** | Hết lệch |
| Thừa ô **"Số điện thoại"** trong nhóm tài khoản (bắt buộc) | Đặc tả chỉ có *Số điện thoại liên hệ* của doanh nghiệp (dòng 1922), **không có** ô riêng cho tài khoản | **Đã gỡ**; chỉ còn "Điện thoại doanh nghiệp" | Hết lệch |
| Thừa công tắc **"Cho phép công khai thông tin"** | Đặc tả **không có** | **Đã gỡ** | Hết lệch |
| Nhãn **"Doanh thu (VNĐ)"** | Dòng 1917 ghi **"Doanh thu năm"**; Inputs dòng 1054 `doanh_thu_nam` | Nhãn nay là **"Doanh thu năm (VNĐ)"** | Hết lệch |
| *(đối tác không nêu)* | Dòng 1931 ghi *Doanh nghiệp do nữ làm chủ* loại **checkbox** | Web vẽ bằng **công tắc gạt**, nhãn "Nữ làm chủ" | Lệch **kiểu điều khiển**, không chấm là lỗi — xem §5 |

**Dấu vết độc lập cho thấy đây là thay đổi có chủ đích của dev:** lược đồ `RegisterDoanhNghiepDto` ở `/api/docs-json` **vẫn còn** 3 tham số `hoTen`, `soDienThoaiTaiKhoan`, `laCongKhai` nhưng **đều không bắt buộc**, và giao diện **không gửi** chúng nữa — khớp đúng 3 thứ đối tác báo thừa.

---

## 5. Vì sao điểm lệch còn lại KHÔNG đủ để chấm là lỗi

Chiếu theo thang phân biệt mức độ: *nhãn khác chữ nhưng cùng nghĩa (nhẹ)* < *sai loại điều khiển* < *thiếu hẳn trường* / *sai tính bắt buộc (nặng — chặn người dùng lưu)*.

- **Nhãn rút gọn nhưng cùng nghĩa (nhẹ, chấp nhận):** "Giấy CN ĐKKD" ↔ *Số Giấy đăng ký kinh doanh* (d.1910) · "Địa chỉ trụ sở" ↔ *Địa chỉ* (d.1911) · "Loại doanh nghiệp" ↔ *Loại hình doanh nghiệp* (d.1913) · "Người đại diện" ↔ *Người đại diện pháp luật* (d.1919) · "Điện thoại doanh nghiệp" ↔ *Số điện thoại liên hệ* (d.1922) · "Ngành nghề chính" ↔ *Ngành nghề* (d.1915). Không mục nào đổi nghĩa hay đổi loại dữ liệu.
- **Không có trường nào thiếu**, **không có trường nào thừa**, **không có trường nào sai tính bắt buộc** so với đặc tả — đây mới là hai mức nặng.
- **Riêng "Nữ làm chủ" (công tắc gạt thay ô tích, dòng 1931):**
  1. Trường **vẫn có mặt**, **vẫn tùy chọn**, **mặc định Tắt**, giá trị vẫn là bật/tắt (`laNuLamChu: boolean` ở hợp đồng API) ⇒ **không cản trở người dùng lưu**, không mất dữ liệu.
  2. Không phải nhầm lẫn hệ thống: đúng chỗ đặc tả bắt buộc là **ô tích** (dòng 1936 — ô Cam kết) thì web **vẫn vẽ đúng ô tích**, kèm nhãn khớp **nguyên văn**.
  3. **Chính đối tác cũng không coi đây là lệch** — khung `frames/QLDKTK_01_partner-video/t052.99s.jpg` cho thấy bản dựng của họ cũng dùng công tắc gạt cho mục này, và họ không nêu.
  4. Nếu lấy điểm này ra chấm `Open` thì QA đang **tự dựng một khiếu nại mà đối tác không hề đưa ra**.

---

## 6. Kiểm mâu thuẫn nội tại của đặc tả (mật khẩu đặt lúc nào)

Đã tự kiểm bằng cách mở file, không tin số dòng cho sẵn:

- **Chiều A — đặt mật khẩu ngay khi đăng ký:** SCR-VIII-08 **dòng 1934** (*Mật khẩu*) + **1935** (*Xác nhận mật khẩu*) nằm trên biểu mẫu; Inputs FR-VIII-22 **dòng 1070** `mat_khau`, **1071** `mat_khau_xac_nhan`; Processing **dòng 1081** (kiểm độ mạnh + khớp xác nhận), **dòng 1083** (mã hóa mật khẩu).
- **Chiều B — đặt mật khẩu khi bấm liên kết kích hoạt:** Postconditions **dòng 1109**; Acceptance **dòng 1116**; bảng máy trạng thái SM-TAIKHOAN **dòng 2299** ("CHO_KICH_HOAT → HOAT_DONG | User kích hoạt qua email **+ đặt mật khẩu lần đầu**", có liệt kê FR-VIII-22).

⇒ **Đặc tả thật sự tự mâu thuẫn.** Kỳ vọng của đối tác (*"…nhấn liên kết kích hoạt **để đặt mật khẩu**"*) nằm ở **chiều B**; hệ thống đang chạy theo **chiều A** (đã chứng minh bằng thực nghiệm: bấm liên kết kích hoạt → `POST /api/v1/auth/verify-email` trả 200 kèm *"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục."* + `trangThai: HOAT_DONG`, **không có bước đặt mật khẩu nào**).

**Nhưng mâu thuẫn này KHÔNG rơi vào chỗ quyết định của case,** nên **không** đẩy case sang `BA confirm`:

- Câu hỏi phải trả lời cho dòng 321 là *"biểu mẫu có đúng danh sách trường trong tài liệu không?"*.
- Bảng **Thành phần màn hình** — đúng bảng đặc tả trường của màn này — liệt kê rõ 2 ô mật khẩu ở **dòng 1934–1935**, và bảng **Inputs** cũng vậy (**dòng 1070–1071**). Vậy việc biểu mẫu **có** 2 ô mật khẩu là **đúng bảng trường**, kết luận được ngay mà không cần BA phân xử.
- Mâu thuẫn chỉ ảnh hưởng tới **câu chữ thông báo sau khi đăng ký**, mà đó **không phải điều đối tác báo sai** (Kết quả thực tế của họ chỉ nói về trường thông tin).
- Điểm này vẫn được ghi thành **mục cần BA chốt riêng** ở §"Ngoài phạm vi" của `cond/QLDKTK_01.md`, để các case họ hàng (kích hoạt / quên mật khẩu) không bị chấm lệch nhau.

---

## 7. Vì sao `Resolved` chứ không phải `Reject` / `Open` / `BA confirm` / ô TRỐNG

| Verdict | Vì sao KHÔNG chọn |
|---|---|
| `Open` | Không tìm được trường nào thiếu / thừa / sai tính bắt buộc so với SCR-VIII-08 dòng 1907–1939. Điểm lệch duy nhất (công tắc gạt ở "Nữ làm chủ") không chặn thao tác, đối tác không nêu, và có y hệt trên bản dựng của họ |
| `Reject` | **Không chứng minh được đối tác thao tác hay hiểu sai.** Video của họ cho thấy bản dựng khi đó thật sự có 3 trường thừa + nhãn "Doanh thu (VNĐ)" sai so với chính tài liệu họ mở song song. Đây là "không tái hiện", không phải "đối tác báo sai" |
| `BA confirm` | Mâu thuẫn của đặc tả **không nằm ở chỗ quyết định** của case (xem §6). Còn điểm "trang xác nhận / câu chữ thông báo" thì **không phải điều đối tác báo sai** — đưa nó lên làm verdict là tự đổi phạm vi khiếu nại của họ. Đã tách thành mục BA chốt riêng |
| ô TRỐNG | Không có blocker khách quan nào: bằng chứng **mở xem được** (script báo 1 link Drive, không phải exit 3), biểu mẫu là màn công khai nên **không cần tiền đề tài khoản**, và đã chạy trọn luồng đăng ký thật với dữ liệu tự sinh |
| **`Resolved`** ✅ | Đúng định nghĩa: bug **không tái hiện** trên bản dựng hiện tại, **đối tác đã có bằng chứng** cho thấy lệch là có thật ở bản dựng của họ, và QA **đã re-verify LIVE** (không phải kết luận tĩnh từ đọc đặc tả hay xem lại video) |

**Cặp mã hoá ghi sheet:** giữ **P = `Reject`** (của dev, không đụng) + đặt **Q (`Verify`) = `Resolved`** — đúng quy ước tuần 3.

---

## 8. Artifact quan sát (gate real-data) — mọi ảnh đều đã MỞ RA ĐỌC

| # | Tệp | Nội dung đã đọc được |
|---|---|---|
| 01 | [`image/QLDKTK_01-01-form-dangky-fullpage.png`](../image/QLDKTK_01-01-form-dangky-fullpage.png) | Toàn bộ biểu mẫu lúc trống: 3 mục, 28 thành phần, 2 nút Hủy / Đăng ký |
| 02 | [`image/QLDKTK_01-02-dropdown-loai-doanh-nghiep.png`](../image/QLDKTK_01-02-dropdown-loai-doanh-nghiep.png) | 5 lựa chọn Loại doanh nghiệp — **chứng minh 2 "UUID" mà kịch bản đo bắt được là nút ẩn, màn hình không có**; cũng là ảnh cho thấy dữ liệu kiểm thử "QTHT-B2 LDN 21/07 test doanh thu trong" đang lẫn trong danh mục |
| 03 | [`image/QLDKTK_01-03-dropdown-nganh-nghe-chinh.png`](../image/QLDKTK_01-03-dropdown-nganh-nghe-chinh.png) | Đúng 3 lựa chọn Ngành nghề chính, khớp SRS dòng 1915 |
| 04 | [`image/QLDKTK_01-04-dropdown-quy-mo.png`](../image/QLDKTK_01-04-dropdown-quy-mo.png) | Đúng 3 lựa chọn Quy mô (Siêu nhỏ / Nhỏ / Vừa), khớp SRS dòng 1914 |
| 05 | [`image/QLDKTK_01-05-tendangnhap-auto-theo-mst.png`](../image/QLDKTK_01-05-tendangnhap-auto-theo-mst.png) | Gõ mã số thuế `9908032201` → ô "Tên đăng nhập" (khóa, xám) hiện ngay `9908032201` — khớp SRS dòng 1933 + Acceptance dòng 1113 |
| 06 | [`image/QLDKTK_01-06-matkhau-yeu-thanh-do-manh-do-va-checklist.png`](../image/QLDKTK_01-06-matkhau-yeu-thanh-do-manh-do-va-checklist.png) | Mật khẩu yếu `abc` → 2 dòng cảnh báo đỏ + **thanh độ mạnh màu đỏ** + danh sách 5 tiêu chí ○/✓ — khớp yêu cầu "có indicator độ mạnh" dòng 1934. **Tệp đã đổi tên** cho khớp điểm ảnh (tên cũ nói "không có thanh độ mạnh" là kết luận sai của kịch bản đo) |
| 07 | [`image/QLDKTK_01-07-form-da-dien-day-du-truoc-khi-dangky.png`](../image/QLDKTK_01-07-form-da-dien-day-du-truoc-khi-dangky.png) | Biểu mẫu đã điền; thanh độ mạnh **xanh 100%** với đủ 5 dấu ✓; ô xác nhận mật khẩu đang báo lệch (do thao tác nhập của QA, đã sửa ở ảnh 08) |
| 08 | [`image/QLDKTK_01-08-form-hoan-tat-truoc-submit.png`](../image/QLDKTK_01-08-form-hoan-tat-truoc-submit.png) | Trạng thái sạch trước khi bấm: không còn cảnh báo, ô tích Cam kết đã tích, "Tên đăng nhập" = `9908032201` |
| 09 | [`image/QLDKTK_01-09-ngay-sau-khi-bam-dangky.png`](../image/QLDKTK_01-09-ngay-sau-khi-bam-dangky.png) | Ngay sau khi bấm Đăng ký: hệ thống **chuyển về trang đăng nhập**, không có trang xác nhận riêng |
| 10 | [`image/QLDKTK_01-10-trang-kich-hoat-tu-email.png`](../image/QLDKTK_01-10-trang-kich-hoat-tu-email.png) | Bấm liên kết kích hoạt trong thư → về thẳng trang đăng nhập, **không có màn đặt mật khẩu** |
| 11 | [`image/QLDKTK_01-11-dang-nhap-thanh-cong-bang-MST.png`](../image/QLDKTK_01-11-dang-nhap-thanh-cong-bang-MST.png) | Đăng nhập bằng `9908032201` + mật khẩu đã đặt lúc đăng ký → vào hệ thống, góc phải "Nguyễn Văn Kiểm Thử · **DN**"; chân menu ghi **`HTPLDN · V1.0.5`** |
| 12 | [`image/QLDKTK_01-12-linhvuc-multiselect-giu-2-lua-chon.png`](../image/QLDKTK_01-12-linhvuc-multiselect-giu-2-lua-chon.png) | Ô chọn nhiều "Lĩnh vực kinh doanh" giữ đủ 2 lựa chọn → bác bỏ ứng viên lỗi "rơi lựa chọn" |

**Khung hình bằng chứng đối tác (chỉ ghi nhận, KHÔNG dùng làm căn cứ):** `frames/QLDKTK_01_partner-video/` — 39 khung trích từ `partner-evidence/QLDKTK_02.webm` (md5 `cb8e5a7afa440ff24d969225d5911700`, 15 030 491 byte). Khung then chốt: `t008.01s.jpg` · `t012.06s.jpg` (2 ô thừa "Họ và tên người đăng ký" + "Số điện thoại") · `t024.18s.jpg` · `t046.73s.jpg` (ô Email chứa `admin` + lỗi đỏ) · `t052.99s.jpg` (ô "Doanh thu (VNĐ)" đang bôi đen + công tắc "Cho phép công khai thông tin") · `t000.00s.jpg` `t016.06s.jpg` `t030.22s.jpg` `t036.27s.jpg` `t040.63s.jpg` (cửa sổ Word — bảng trường mục 8–12, 17–22 của tài liệu).

### Phản hồi máy chủ (bằng chứng thao tác thật)

- `POST /api/v1/auth/register-doanh-nghiep` → **201**
  `{"success":true,"data":{"id":"6da41005-2a3e-4b3e-a496-35eb9c87f4dc","email":"qa.qldktk01.20260803@htpldn.test","trangThai":"CHO_KICH_HOAT","message":"Đăng ký doanh nghiệp thành công. Vui lòng kiểm tra email để kích hoạt tài khoản (link có hiệu lực vĩnh viễn)."}}`
- Thông báo trên màn hình (bắt bằng bộ quan sát, **không lọc trùng**, đọc bằng `innerText`): **1 khung**, nguyên văn *"Đăng ký thành công, vui lòng kiểm tra email kích hoạt"*, loại tự tắt. **Số request kèm theo: 1.**
- Thư kích hoạt (hộp thư giả lập, tiêu đề *"Kích hoạt tài khoản doanh nghiệp HTPLDN"*): *"Doanh nghiệp "Công ty TNHH QA UAT QLDKTK01" đã được đăng ký thành công. Tên đăng nhập của bạn là mã số thuế: 9908032201 … Link kích hoạt có hiệu lực vĩnh viễn và chỉ dùng được một lần."*
- `POST /api/v1/auth/verify-email` → **200** `{"message":"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục.","trangThai":"HOAT_DONG"}`

---

## 9. Dữ liệu QA tạo ra trong lượt verify này

| Thứ | Giá trị | Ghi chú |
|---|---|---|
| Doanh nghiệp | `Công ty TNHH QA UAT QLDKTK01` (viết tắt `QAUAT01`) | Hà Nội, Công ty trách nhiệm hữu hạn, Thương mại và dịch vụ, quy mô Nhỏ |
| Mã số thuế / tên đăng nhập | `9908032201` | Chưa từng tồn tại trước lượt đo |
| Email | `qa.qldktk01.20260803@htpldn.test` | Chưa từng tồn tại trước lượt đo |
| Mật khẩu | `Qa@Test2026` | Đặt ngay khi đăng ký |
| `taiKhoan.id` | `6da41005-2a3e-4b3e-a496-35eb9c87f4dc` | `CHO_KICH_HOAT` → `HOAT_DONG` |
| Vai trò | `DN` | Gán sẵn khi tạo, đúng SRS bước 7 (dòng 1084) |

Tài khoản này **đăng nhập được** và có thể tái dùng cho các case cần vai trò Doanh nghiệp thuộc Hà Nội.

---

## 10. Trả lời câu hỏi bắt buộc: "ngoài tiêu chí BA ra, có thấy gì bất thường không?"

**Có — 6 điểm, đều dựa trên ảnh đã mở đọc / phản hồi máy chủ đã đọc, không phải suy đoán.** Chưa mở dòng TC mới trên sheet, **chờ user quyết** (đề bài yêu cầu báo chứ không tự mở dòng). Danh sách đầy đủ ở §"Ngoài phạm vi case" của [`cond/QLDKTK_01.md`](../cond/QLDKTK_01.md); 2 điểm đáng chú ý nhất:

1. **Danh mục "Loại doanh nghiệp" trên trang đăng ký CÔNG KHAI đang lẫn dữ liệu kiểm thử** — lựa chọn đầu tiên là *"QTHT-B2 LDN 21/07 test doanh thu trong"* (ảnh `-02`), hiện ra cho mọi doanh nghiệp thật. Do đội kiểm thử tạo ở vòng trước, không phải lỗi mã nguồn, nhưng nên dọn trước khi bàn giao.
2. **Giao diện gửi cố định `captchaToken: "mock-captcha"`** trong yêu cầu đăng ký, trong khi hợp đồng API đánh dấu `captchaToken` là tham số **bắt buộc** — tức cơ chế chống máy tự động trên một điểm cuối công khai đang được thoả bằng một giá trị giả cố định. Đặc tả không nhắc tới captcha ở SCR-VIII-08 / FR-VIII-22.

## 11. Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Dùng đúng khối `tools/toast-capture.js` — **không lọc trùng**, đọc bằng `innerText`, **đếm request song song**; đã tự kiểm **`soObserverDangSong = 1`** trước khi tin số liệu. Kết quả: **1 request / 1 khung thông báo** ⇒ không lặp thông báo, không tạo trùng bản ghi.
- **Hai lần phép đo của QA nói dối, bắt được nhờ mở ảnh ra nhìn** (chi tiết ở `cond/QLDKTK_01.md` §Ghi chú đo lường): (1) đọc `innerText` cả khối thả xuống → ra 2 mã UUID không hề hiện trên màn hình (nút ẩn cho trình đọc màn hình); (2) tìm thanh độ mạnh mật khẩu **bên trong** khối trường → không thấy, suýt kết luận thiếu, trong khi ảnh cho thấy thanh đỏ + 5 tiêu chí hiện rõ (khối nằm **ngay sau** khối trường). Cả hai đều đã đo lại đúng.
- **Một ứng viên lỗi bị bác bằng phương pháp thứ hai:** lượt gửi đầu chỉ kèm 1 mã lĩnh vực dù bấm 2 mục → nghi ô chọn nhiều rơi lựa chọn; đo lại bằng thao tác bấm thật có chờ giữa 2 lần bấm thì giữ đủ 2 (ảnh `-12`) ⇒ lỗi kịch bản của QA, không phải lỗi ứng dụng.
- Trước khi chốt đã **tải lại trang bỏ qua bộ nhớ đệm** và lặp lại phép đo trong **phiên trình duyệt cách ly thứ hai** — cả hai lần cho danh sách trường trùng khớp.
