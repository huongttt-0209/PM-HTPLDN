# QLDKTK_01 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLDKTK_01 · **Dòng sheet:** 321 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Môi trường:** https://18.143.165.120.nip.io · **Bản dựng:** `HTPLDN · V1.0.5` (đọc ở chân menu sau khi đăng nhập); gói giao diện `assets/index-BrKDNUvo.js`
**Cột P (`Trạng thái dev fix 1`):** `Reject` — của DEV, QA KHÔNG đụng · **Cột Q (`Verify`):** rỗng tại thời điểm QA verify
**Phản ánh đối tác (Kết quả thực tế):** "**Một số trường thông tin không giống với tài liệu**" — Trạng thái 1 = Fail.
**Kết quả mong đợi của đối tác:** dữ liệu hợp lệ → hiện trang xác nhận *"Đăng ký thành công. Vui lòng kiểm tra thư điện tử và nhấn liên kết kích hoạt để đặt mật khẩu"*.

> Bảng ở mục "Bảng đối chiếu điều kiện" là **bảng markdown DUY NHẤT** trong file (script `sheet_write.py` đọc mọi bảng trong file này). Mọi đối chiếu trường bên dưới trình bày dạng gạch đầu dòng. Lập luận đầy đủ + nguyên văn note dev đặt ở `reverify-audit/QLDKTK_01.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- Lấy bằng `python3 tools/fetch_evidence.py --row 321` → script báo **"Link Drive tìm thấy: 1"** (KHÔNG rỗng, không phải exit 3). Ô "Ảnh/vieo 1" của dòng 321 ghi tên tệp **`QLDKTK_02.webm`**.
- **🔴 Bằng chứng LỆCH MÃ TC:** tên tệp mang mã **QLDKTK_02**, không phải QLDKTK_01. Theo `id-crosswalk.csv`, `QLDKTK_02` là một dòng riêng (partner_row 1223 ↔ log_row 185). ⇒ Tệp này **KHÔNG được dùng làm căn cứ ra verdict cho dòng 321**. Vẫn mở xem để ghi lại quan sát, và **tuyệt đối không suy kết luận từ tên tệp**.
- Đã trích 15 + 24 khung hình (`tools/extract_frames.py`, mỗi 4s rồi mỗi 2s) vào `frames/QLDKTK_01_partner-video/`, mở đọc ở **độ phân giải gốc 1920×1080**, không đọc từ ảnh ghép thu nhỏ. Video dài ~57 giây, đồng hồ máy đối tác **2026-07-15 02:22–02:23 PM**.
- **3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết):**
  - (a) **URL / màn hình đối tác đứng:** `htpldn-uat.ospgroup.vn/register/doanh-nghiep` — màn *Đăng ký tài khoản Doanh nghiệp*, đọc rõ ở thanh địa chỉ các khung t008 / t012 / t024 / t046 / t052 / t056. Đây là màn công khai, **không đăng nhập**, nên không có vai trò nào để so.
  - (b) **Trạng thái entity:** chưa có bản ghi nào — biểu mẫu ở trạng thái **trống, chưa bấm Đăng ký**. Trong toàn bộ 57 giây video **KHÔNG có khung nào bấm nút Đăng ký**, **KHÔNG có khung nào hiện trang xác nhận hay thông báo kết quả**.
  - (c) **Dữ liệu tiền đề:** không nhập gì ngoài 2 ô — ô *Mật khẩu* đã có sẵn giá trị (10 chấm) và ô *Email doanh nghiệp* đang chứa chữ `admin` kèm lỗi đỏ *"Email không hợp lệ"*. Đây là dữ liệu rác còn lại của lượt thao tác trước, không phải "dữ liệu hợp lệ" như bước 2 của case.
- **Nội dung video thực chất là gì:** đối tác **mở song song 2 cửa sổ** — cửa sổ Word tài liệu `HTPLDN-PTYC-CT-v2.0(1).docx` mục *4.10.8.2 PM10.QTHT.DK.MH01 – Trang Đăng ký tài khoản doanh nghiệp → Mô tả thông tin trên màn hình* (các khung t000/t004/t016/t030/t036/t040) và cửa sổ trình duyệt biểu mẫu đăng ký (t008/t012/t024/t046/t052/t056), rồi **rà từng dòng bảng trường trong tài liệu đối chiếu với biểu mẫu**. Trong Word còn thấy tiêu đề mục **"Ghi chú chênh lệch giữa SRS và prototype (Mô tả thông tin)"**.
- **Khác biệt đọc được trên biểu mẫu bản dựng của đối tác (so với bảng trường trong tài liệu họ đang mở):**
  - Có **thừa** nhóm *Thông tin tài khoản* đặt ở ĐẦU biểu mẫu với 2 ô **"Họ và tên người đăng ký"** (bắt buộc) và **"Số điện thoại"** (bắt buộc) — bảng trường trong tài liệu không có 2 mục này.
  - Có **thừa** công tắc **"Cho phép công khai thông tin"** (khung t052).
  - Nhãn ô doanh thu là **"Doanh thu (VNĐ)"** — đối tác bôi đen chính ô này ở khung t052, trong khi tài liệu ghi **"Doanh thu năm"** (mục 10, khung t036/t040).
  - Tài liệu liệt kê mục 19 *Tên đăng nhập* (Ký tự, **chỉ đọc**, "Hiển thị tự động bằng giá trị Mã số thuế"), mục 20 *Mật khẩu*, 21 *Nhập lại mật khẩu*, 22 *Cam kết thông tin đúng sự thật* (Ô chọn, bắt buộc, mặc định Tắt) — video **dừng ở ô "Ghi chú"**, không cuộn tới cuối nên không xác minh được 4 mục này trên bản dựng của họ.
- ⇒ Kết luận Cổng 1: bằng chứng **mở xem được, không rỗng**, và nội dung của nó đúng là **đối chiếu trường biểu mẫu với tài liệu** — trùng chủ đề phản ánh của dòng 321. **Nhưng vì tệp mang mã TC khác nên chỉ ghi nhận, KHÔNG dùng làm căn cứ verdict.** Verdict dưới đây dựa 100% vào phép đo trực tiếp trên bản dựng hiện tại.

## Cổng 2 — Hiểu bug

- **Đối tác phản ánh CỤ THỂ gì:** *một số trường thông tin trên biểu mẫu Đăng ký tài khoản doanh nghiệp không giống bảng trường trong tài liệu* — tức tranh chấp về **danh sách trường / nhãn / loại điều khiển / tính bắt buộc**, KHÔNG phải về luồng xử lý.
- **Khung hình chứa lỗi + mô tả 1 câu:** khung `t052.99s.jpg` — biểu mẫu hiện ô **"Doanh thu (VNĐ)"** (đang bôi đen) và công tắc **"Cho phép công khai thông tin"**, hai thứ không khớp bảng trường trong tài liệu đang mở ở cửa sổ Word bên cạnh; khung `t008.01s.jpg` / `t012.06s.jpg` hiện thêm 2 ô **"Họ và tên người đăng ký"** và **"Số điện thoại"** ở đầu biểu mẫu, cũng không có trong bảng trường.
- **Không đi theo hướng dev nêu:** note dev xoay quanh "chặn MST đã tồn tại là đúng đặc tả". Đó là nội dung của case **QLDKTK_04** (dòng 187), **không phải** khiếu nại của dòng 321. Dòng 321 khiếu nại **trường thông tin**, nên phép đo bên dưới đi theo hướng đối chiếu từng trường.
- **Dữ liệu + bước tái hiện:** mở `/login` → bấm *"Đăng ký tài khoản doanh nghiệp"* → liệt kê toàn bộ thành phần biểu mẫu theo đúng thứ tự hiển thị → bung từng ô chọn xem danh sách lựa chọn → nhập bộ dữ liệu hợp lệ với mã số thuế + email **chưa từng dùng** → bấm Đăng ký → đọc nguyên văn thông báo → kiểm hộp thư kích hoạt.

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | **Khách vãng lai, KHÔNG đăng nhập** — video quay thẳng `htpldn-uat.ospgroup.vn/register/doanh-nghiep`, không có thanh bên, không có avatar/tên người dùng ở góc phải, biểu mẫu vào thẳng từ trang đăng nhập. Đây là màn tự đăng ký công khai nên không tồn tại vai trò nào khác để so | **Khách vãng lai, KHÔNG đăng nhập** — mở `/login` rồi bấm liên kết "Đăng ký tài khoản doanh nghiệp", đo trong **phiên trình duyệt cách ly hoàn toàn** (`isolatedContext=qldktk01-lv`) để chắc chắn không dính phiên đăng nhập nào còn sống. Đo lại lần hai trong một phiên cách ly thứ hai (`qldktk01-activate`) cho kết quả trùng khớp | Không |
| Entity + trạng thái (state machine) | `DOANH_NGHIEP` + `TAI_KHOAN` **chưa tồn tại** — biểu mẫu trống, chưa bấm Đăng ký; toàn bộ 57 giây video không có khung nào đã submit | Đo ở **đúng trạng thái "chưa có bản ghi"**: biểu mẫu vừa mở, trống hoàn toàn (ảnh `QLDKTK_01-01`). Sau đó chạy tiếp trọn vòng đời để phủ hết: submit → `TAI_KHOAN` sinh ra ở **CHO_KICH_HOAT** → bấm liên kết trong thư → chuyển **HOAT_DONG** → đăng nhập được bằng mã số thuế. Cả 4 mốc trạng thái đều có ảnh + phản hồi máy chủ | Không |
| Dữ liệu tiền đề (mã số thuế + email đã dùng hay chưa) | Ô *Email doanh nghiệp* chứa `admin` + báo đỏ *"Email không hợp lệ"*; ô *Mật khẩu* đã có sẵn giá trị. Mã số thuế để trống. ⇒ **dữ liệu rác của lượt trước, chưa phải bộ dữ liệu hợp lệ** | Dùng **mã số thuế `9908032201` và email `qa.qldktk01.20260803@htpldn.test` đều CHƯA từng tồn tại** (tự sinh cho lượt đo này) — đúng tinh thần bước 2 "nhập thông tin hợp lệ", và tránh hẳn nhánh "MST đã tồn tại" mà note dev nhắc tới. Máy chủ trả **201** chứ không trả lỗi trùng, xác nhận tiền đề đúng là dữ liệu mới | Không |
| Input / filter / giá trị nhập | Đối tác **chỉ đọc biểu mẫu để đối chiếu trường**, không nhập bộ dữ liệu hợp lệ nào và không bấm Đăng ký | Đo **2 pha tách bạch**: (1) pha ĐỌC — biểu mẫu trống, liệt kê đủ 28 thành phần + 2 nút theo đúng thứ tự hiển thị, bung cả 5 ô chọn để đọc danh sách lựa chọn, di chuột đọc 2 chú thích, kiểm tra `multiple` của vùng tải tệp; (2) pha NHẬP — điền đủ 13 trường bắt buộc + 12 trường tùy chọn rồi bấm Đăng ký. Có thử thêm mật khẩu yếu `abc` để xem cảnh báo và thanh độ mạnh. **Tải lại trang bỏ qua bộ nhớ đệm** rồi đo lại trước khi chốt | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md` — bản chốt duy nhất, đã **mở file đọc từng dòng**, KHÔNG lấy số dòng từ trí nhớ và KHÔNG dùng `input/srs-update-2026-5-5/`.
Màn: **SCR-VIII-08 "Đăng ký Tài khoản Doanh nghiệp"** — tiêu đề **dòng 1895**, bảng Thành phần màn hình **dòng 1907–1939**, ghi chú auto-pass **dòng 1941**. FR: **FR-VIII-22** — tiêu đề **dòng 1024**, bảng Inputs **dòng 1042–1072**, Processing **1074–1089**, Error Handling **1091–1101**, Postconditions **1103–1109**, Acceptance **1111–1122**.

### Thứ tự đo (chống thiên kiến)

- Danh sách thành phần biểu mẫu được liệt kê **TRƯỚC** khi mở SRS: quét thô cây DOM theo `label` (dùng `innerText`, **không dùng `textContent`**) + mở ảnh chụp ra đọc bằng mắt. Chỉ sau khi có danh sách 28 thành phần mới mở SRS đối chiếu.

### Đối chiếu 1-1 TỪNG trường — SCR-VIII-08 (dòng 1907–1939) vs web

- Nhóm 1 — Thông tin doanh nghiệp (SRS dòng 1907–1931), web gom vào 2 mục *Thông tin doanh nghiệp* + *Quy mô (theo NĐ39/2018)*:
  - **1 Tên doanh nghiệp** (d.1908, text, Bắt buộc) → ✅ "Tên doanh nghiệp", ô chữ, có dấu \* bắt buộc.
  - **2 Mã số thuế** (d.1909, text, Bắt buộc, khóa định danh) → ✅ "Mã số thuế", ô chữ, bắt buộc.
  - **3 Số Giấy đăng ký kinh doanh** (d.1910, text, Tùy chọn) → ✅ "Giấy CN ĐKKD", ô chữ, không bắt buộc. *Nhãn rút gọn, cùng nghĩa.*
  - **4 Địa chỉ** (d.1911, text, Bắt buộc) → ✅ "Địa chỉ trụ sở", ô chữ, bắt buộc. *Nhãn cụ thể hơn, cùng nghĩa.*
  - **5 Tỉnh / Thành phố** (d.1912, select, Bắt buộc) → ✅ ô chọn có tìm kiếm, nạp từ danh mục `TINH_THANH` (`GET /api/v1/danh-muc/public?loai=TINH_THANH` → 200), lựa chọn đầu: Hà Nội, TP. Hồ Chí Minh, Hải Phòng, Đà Nẵng, Cần Thơ…
  - **6 Loại hình doanh nghiệp** (d.1913, select, Bắt buộc) → ✅ "Loại doanh nghiệp", ô chọn, nạp từ `LOAI_DOANH_NGHIEP`. *Nhãn rút gọn, cùng nghĩa.*
  - **7 Quy mô doanh nghiệp** (d.1914, select, Bắt buộc, *Siêu nhỏ / Nhỏ / Vừa*) → ✅ "Quy mô", ô chọn, **đúng 3 lựa chọn Siêu nhỏ · Nhỏ · Vừa** (ảnh `-04`).
  - **8 Ngành nghề** (d.1915, select, Bắt buộc, *Nông Lâm / Công nghiệp / Thương mại*) → ✅ "Ngành nghề chính", **đúng 3 lựa chọn** "Nông, lâm nghiệp và thủy sản" · "Công nghiệp và xây dựng" · "Thương mại và dịch vụ" (ảnh `-03`).
  - **9 Số lao động** (d.1916, number, Tùy chọn ≥0) → ✅ ô số, `min=0`.
  - **10 Doanh thu năm** (d.1917, number, Tùy chọn ≥0) → ✅ **"Doanh thu năm (VNĐ)"**, ô số, `min=0`. *Đây chính là nhãn đối tác bôi đen là sai; bản hiện tại đã đúng chữ "Doanh thu năm".*
  - **11 Tổng nguồn vốn** (d.1918, number, Tùy chọn ≥0) → ✅ "Tổng nguồn vốn (VNĐ)", ô số, `min=0`.
  - **12 Người đại diện pháp luật** (d.1919, text, Bắt buộc) → ✅ "Người đại diện", bắt buộc.
  - **13 Chức vụ người đại diện** (d.1920, text, Tùy chọn) → ✅ "Chức vụ đại diện", không bắt buộc.
  - **14 Email** (d.1921, text, Bắt buộc, có chú thích) → ✅ "Email doanh nghiệp", `type=email`, bắt buộc, **có chú thích**: *"Email này dùng để nhận link kích hoạt và liên hệ chính thức"*.
  - **15 Số điện thoại liên hệ** (d.1922, text, Bắt buộc) → ✅ "Điện thoại doanh nghiệp", **có dấu \* bắt buộc**.
  - **16 Lĩnh vực kinh doanh** (d.1923, multi-select có search, Tùy chọn, hiển thị *"mã cấp 4 — tên cấp 4"*) → ✅ ô chọn NHIỀU, gợi ý "Chọn một hoặc nhiều ngành VSIC cấp 4", lựa chọn đúng dạng **"0111 — Trồng lúa"**, "2610 — …". Đã kiểm chọn 2 mục → **giữ đủ 2** (ảnh `-12`).
  - **17 Ghi chú** (d.1924, textarea, Tùy chọn) → ✅ ô văn bản dài.
  - **18 File đính kèm** (d.1925, file-upload, Tùy chọn, **multi**) → ✅ "Tệp đính kèm" + nút "Tải lên", thuộc tính `multiple = true`.
  - **19 Tên viết tắt** (d.1926, text, Tùy chọn) → ✅.
  - **20 Ngày cấp ĐKKD** (d.1927, date-picker, Tùy chọn) → ✅ ô chọn ngày có biểu tượng lịch.
  - **21 Fax** (d.1928, text, Tùy chọn) → ✅.
  - **22 Số lao động nữ** (d.1929, number, Tùy chọn ≥0) → ✅ ô số, `min=0`.
  - **23 Số lao động khuyết tật** (d.1930, number, Tùy chọn ≥0) → ✅ ô số, `min=0`.
  - **24 Doanh nghiệp do nữ làm chủ** (d.1931, **checkbox**, Tùy chọn) → ✅ có mặt với nhãn "Nữ làm chủ", **nhưng vẽ bằng công tắc gạt thay vì ô tích**. Vẫn là 1 giá trị bật/tắt, tùy chọn, mặc định Tắt, không cản trở lưu. Xem mục "Điểm lệch duy nhất" bên dưới.
- Nhóm 2 — Tài khoản đăng nhập (SRS dòng 1932–1936), web có mục *Tài khoản đăng nhập*:
  - **25 Tên đăng nhập (auto từ Mã số thuế), chỉ đọc, cập nhật tức thời** (d.1933) → ✅ ô **khóa (disabled)**, gợi ý "Tự động theo Mã số thuế", chú thích *"Tên đăng nhập được tạo tự động theo Mã số thuế của doanh nghiệp"*. **Đã kiểm hành vi tức thời:** gõ `9908032201` vào ô Mã số thuế thì ô Tên đăng nhập lập tức hiện `9908032201` (ảnh `-05`).
  - **26 Mật khẩu** (d.1934, password, Bắt buộc, ≥8 + hoa + thường + số + đặc biệt, **có indicator độ mạnh**) → ✅ ô mật khẩu bắt buộc, gợi ý "Tối thiểu 8 ký tự, gồm chữ hoa, thường, số và ký tự đặc biệt"; **có thanh độ mạnh** (thanh tiến trình đổi màu: đỏ 20% với `abc`, xanh 100% với mật khẩu đủ mạnh) **kèm danh sách 5 tiêu chí có dấu ○/✓** (ảnh `-06`, `-08`).
  - **27 Xác nhận mật khẩu** (d.1935, password, Bắt buộc, phải khớp) → ✅ bắt buộc; nhập lệch thì báo ngay *"Mật khẩu xác nhận không khớp"*.
  - **28 Cam kết thông tin đúng sự thật** (d.1936, **checkbox**, Bắt buộc, kèm nhãn nguyên văn) → ✅ **đúng ô tích**, nhãn khớp **nguyên văn** SRS: *"Tôi cam kết các thông tin doanh nghiệp khai báo ở trên là đúng sự thật và chịu trách nhiệm trước pháp luật về nội dung khai báo."*
- Hành động (SRS dòng 1937–1939): **29 Nút "Đăng ký"** → ✅ · **30 Nút "Hủy"** → ✅. Đúng 2 nút, đúng tên, đúng thứ tự.
- **Tổng: 28 thành phần nhập + 2 nút = 30, khớp đúng 30 dòng bảng SCR-VIII-08.** Không thiếu trường nào, **không thừa trường nào**.

### 3 trường đối tác thấy THỪA trên bản dựng của họ — nay đã KHÔNG còn

- **"Họ và tên người đăng ký"** và **"Số điện thoại"** (nhóm *Thông tin tài khoản* ở đầu biểu mẫu): **không còn trên biểu mẫu**. SRS SCR-VIII-08 và bảng Inputs FR-VIII-22 (dòng 1042–1072) **không có** 2 trường này ⇒ bỏ đi là **đúng đặc tả**.
- **"Cho phép công khai thông tin"**: **không còn trên biểu mẫu**. SRS cũng không có ⇒ đúng đặc tả.
- **Bằng chứng độc lập rằng đây là thay đổi có chủ đích của dev:** đọc thẳng hợp đồng API tại `/api/docs-json` → lược đồ `RegisterDoanhNghiepDto` **vẫn còn** 3 tham số `hoTen`, `soDienThoaiTaiKhoan`, `laCongKhai` nhưng **đều KHÔNG bắt buộc**, và giao diện **không gửi** chúng nữa. Đây là dấu vết của việc gỡ 3 trường khỏi biểu mẫu — khớp đúng 3 thứ đối tác báo thừa.
- **Nhãn "Doanh thu (VNĐ)" → nay là "Doanh thu năm (VNĐ)"**, khớp chữ "Doanh thu năm" ở SRS dòng 1917 và Inputs `doanh_thu_nam` dòng 1054.

### Đo bằng phương pháp thứ hai — hợp đồng API (độc lập với giao diện)

- `GET /api/docs-json` (fetch trong phiên, `credentials:'include'`) → 200. Lược đồ `RegisterDoanhNghiepDto` có **32 tham số**, danh sách **bắt buộc gồm 13**: `email`, `password`, `passwordConfirm`, `dongYDieuKhoan`, `captchaToken`, `tenDoanhNghiep`, `maSoThue`, `loaiDnId`, `diaChi`, `tinhThanhId`, `nganhNghe`, `nguoiDaiDien`, `quyMo`.
- Đối chiếu với 13 ô có dấu \* trên giao diện: Tên doanh nghiệp · Mã số thuế · Loại doanh nghiệp · Địa chỉ trụ sở · Tỉnh/Thành phố · **Điện thoại doanh nghiệp** · Email doanh nghiệp · Người đại diện · Ngành nghề chính · Quy mô · Mật khẩu · Xác nhận mật khẩu · ô tích Cam kết.
- **Hai phép đo khớp nhau ở 12/13 mục.** Lệch duy nhất: `dienThoai` **không** nằm trong danh sách bắt buộc của API, trong khi giao diện đánh dấu bắt buộc. **SRS dòng 1922 và Inputs dòng 1059 đều ghi số điện thoại là BẮT BUỘC** ⇒ **giao diện đang đúng SRS**, phần lỏng hơn nằm ở tầng máy chủ. Theo nguyên tắc "UI mâu thuẫn API → verdict theo UI + SRS", điểm này **không làm đổi kết luận**; đã ghi lại ở mục ngoài phạm vi.
- `nganhNghe` API nhận đúng 3 giá trị `NONG_LAM / CONG_NGHIEP / THUONG_MAI` (khớp SRS dòng 1915/1052); `quyMo` nhận đúng `SIEU_NHO / NHO / VUA` (khớp dòng 1914/1051).

### Chạy thật luồng đăng ký với dữ liệu hợp lệ (bước 2 của case)

- Mã số thuế `9908032201` + email `qa.qldktk01.20260803@htpldn.test` (đều mới). Bấm **Đăng ký**.
- **Đo kèm số request:** **1 request** `POST /api/v1/auth/register-doanh-nghiep` → **HTTP 201**; **1 khung thông báo** duy nhất, **không lặp**.
- **Nguyên văn thông báo trên màn hình:** *"**Đăng ký thành công, vui lòng kiểm tra email kích hoạt**"* — dạng thông báo nổi **tự tắt**, kèm **chuyển thẳng về trang đăng nhập**; **KHÔNG có trang xác nhận riêng**.
- **Nguyên văn phản hồi máy chủ:** *"Đăng ký doanh nghiệp thành công. Vui lòng kiểm tra email để kích hoạt tài khoản (link có hiệu lực vĩnh viễn)."*, kèm `trangThai: "CHO_KICH_HOAT"` — khớp SRS Postconditions dòng 1104.
- **Thư kích hoạt về hộp thư giả lập:** đúng 1 thư, tiêu đề *"Kích hoạt tài khoản doanh nghiệp HTPLDN"*, nội dung ghi rõ *"Tên đăng nhập của bạn là mã số thuế: 9908032201"* + liên kết kích hoạt + *"Link kích hoạt có hiệu lực vĩnh viễn và chỉ dùng được một lần"* — khớp SRS bước 10 (dòng 1088) và dòng 1938.
- **Bấm liên kết kích hoạt:** `POST /api/v1/auth/verify-email` → 200, phản hồi *"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục."*, `trangThai: "HOAT_DONG"`. **Không có bước đặt mật khẩu nào** ở khâu này.
- **Đăng nhập lại bằng `9908032201` + mật khẩu đã đặt lúc đăng ký** → qua bước mã xác thực → vào được hệ thống, góc phải hiện "Nguyễn Văn Kiểm Thử · **DN**" (ảnh `-11`). Khớp trọn Acceptance dòng 1112–1116.

### Điểm lệch duy nhất tìm được, và vì sao KHÔNG đủ để chấm là lỗi

- SRS dòng **1931** ghi trường *Doanh nghiệp do nữ làm chủ* loại **checkbox**; web vẽ bằng **công tắc gạt** nhãn "Nữ làm chủ".
- Không chấm là lỗi vì: (1) trường **vẫn có mặt**, **vẫn tùy chọn**, **mặc định Tắt**, giá trị vẫn là bật/tắt, **không cản trở người dùng lưu**; (2) đây là khác biệt **kiểu vẽ điều khiển cho một giá trị bật/tắt**, trong khi ô tích thật sự bắt buộc theo SRS dòng 1936 (ô Cam kết) thì web **vẫn vẽ đúng là ô tích** ⇒ không phải nhầm lẫn hệ thống; (3) **chính đối tác cũng không coi đây là lệch** — khung `t052.99s.jpg` cho thấy bản dựng của họ cũng dùng công tắc gạt cho mục này mà họ không nêu.

### Mâu thuẫn nội tại của SRS — đã kiểm, KHÔNG rơi vào chỗ quyết định của case

- **Chiều A (mật khẩu đặt ngay khi đăng ký):** SCR-VIII-08 dòng **1934** (*Mật khẩu*) và **1935** (*Xác nhận mật khẩu*) nằm ngay trên biểu mẫu; bảng Inputs FR-VIII-22 dòng **1070** `mat_khau` và **1071** `mat_khau_xac_nhan` cũng là đầu vào của chính bước đăng ký; Processing bước 4 dòng **1081** "Kiểm tra mật khẩu đủ độ mạnh + khớp xác nhận", bước 6 dòng **1083** "Mã hóa mật khẩu".
- **Chiều B (mật khẩu đặt khi bấm liên kết kích hoạt):** Postconditions dòng **1109** "DN bấm link kích hoạt + **đặt mật khẩu lần đầu**…"; Acceptance dòng **1116** "Given DN bấm link kích hoạt **+ đặt mật khẩu**"; bảng máy trạng thái SM-TAIKHOAN dòng **2299** "CHO_KICH_HOAT → HOAT_DONG | User kích hoạt qua email **+ đặt mật khẩu lần đầu**" (có liệt kê FR-VIII-22).
- ⇒ **SRS thật sự tự mâu thuẫn** ở chỗ *đặt mật khẩu lúc nào*. Kỳ vọng của đối tác ("…nhấn liên kết kích hoạt **để đặt mật khẩu**") nằm đúng ở **chiều B**; web đang làm theo **chiều A**.
- **Nhưng mâu thuẫn này KHÔNG rơi vào chỗ quyết định của case:** câu hỏi phải trả lời cho dòng 321 là *"biểu mẫu có đúng danh sách trường trong tài liệu không?"*. Bảng **Thành phần màn hình** — tức đúng bảng đặc tả trường của màn này — liệt kê rõ ràng 2 ô mật khẩu ở dòng 1934–1935, và bảng Inputs cũng vậy. Vậy việc biểu mẫu **có** 2 ô mật khẩu là **đúng bảng trường**, không cần BA phân xử mới kết luận được. Mâu thuẫn chỉ ảnh hưởng tới **câu chữ thông báo sau khi đăng ký**, mà cái đó **không phải điều đối tác báo sai** (Kết quả thực tế của họ chỉ nói về trường thông tin).
- Điểm liên quan còn lại — SRS **không quy định** trang xác nhận hay câu chữ thông báo sau khi bấm Đăng ký (đã tìm nguyên cụm "Đăng ký thành công" trong toàn bộ thư mục `srs-v3.5/`: chỉ khớp 1 lần ở `srs-fr-04-chuyen-gia-tvv.md:351`, thuộc chức năng khác) — đã ghi ở mục ngoài phạm vi để BA quyết riêng, **không dùng chấm case này**.

---

## Kết luận

- Phản ánh *"một số trường thông tin không giống với tài liệu"* **KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, đo ở **đúng điều kiện khách vãng lai không đăng nhập** như video đối tác.
- Biểu mẫu hiện có **đúng 28 thành phần nhập + 2 nút**, **khớp 1-1 với đủ 30 dòng** bảng Thành phần màn hình SCR-VIII-08 (dòng 1907–1939): **không thiếu trường, không thừa trường**, tính bắt buộc khớp, danh sách lựa chọn của cả 3 ô chọn cố định (Quy mô / Ngành nghề / Lĩnh vực) khớp đặc tả.
- **Đúng 3 thứ đối tác thấy thừa đã được gỡ**: "Họ và tên người đăng ký", "Số điện thoại", "Cho phép công khai thông tin"; **nhãn "Doanh thu (VNĐ)" đã sửa thành "Doanh thu năm (VNĐ)"** đúng đặc tả.
- Chạy thật luồng đăng ký bằng dữ liệu hợp lệ hoàn toàn mới: **1 request / 1 thông báo**, máy chủ trả **201**, tài khoản sinh ra ở **CHO_KICH_HOAT**, thư kích hoạt về đúng hộp thư, bấm liên kết chuyển **HOAT_DONG**, đăng nhập lại được bằng **mã số thuế** + mật khẩu. Toàn bộ khớp Acceptance dòng 1112–1116.
- Điểm lệch duy nhất (công tắc gạt thay ô tích ở "Nữ làm chủ") **không cản trở thao tác, không bị đối tác nêu, và tồn tại y hệt trên bản dựng của họ** ⇒ không đủ để chấm là lỗi.
- **Đối tác KHÔNG thao tác sai và KHÔNG hiểu sai:** video của họ cho thấy bản dựng khi đó thật sự có 3 trường thừa và nhãn sai so với chính tài liệu họ mở song song. Vì vậy **KHÔNG được dùng `Reject`** ở cột Verify.
- Lưu ý đã ghi rõ ở Cổng 1: tệp bằng chứng gắn cho dòng 321 mang mã của case khác (`QLDKTK_02.webm`) nên **không dùng làm căn cứ**; kết luận dựa hoàn toàn vào phép đo trực tiếp trên bản dựng hiện tại.
- **⇒ Verdict: `Resolved`** (ghi vào cột **Q — Verify**). Cột **P giữ nguyên `Reject`** của dev, KHÔNG đụng tới.

## Ngoài phạm vi case (chưa log — chờ user quyết)

1. **Sau khi đăng ký thành công, hệ thống chỉ hiện thông báo nổi tự tắt rồi chuyển thẳng về trang đăng nhập, không có trang xác nhận riêng.** Kỳ vọng của đối tác là một trang xác nhận với câu chữ cụ thể. **SRS không quy định** trang xác nhận lẫn câu chữ này (SCR-VIII-08 dòng 1938 chỉ mô tả hành vi tạo bản ghi + gửi thư). ⇒ điểm cần **BA chốt**, không phải lỗi dev; không dùng chấm case này vì không phải điều đối tác báo sai.
2. **SRS tự mâu thuẫn về thời điểm đặt mật khẩu** — chi tiết + số dòng ở mục "Mâu thuẫn nội tại của SRS" phía trên. Cần BA chốt để các case họ hàng (kích hoạt, quên mật khẩu) không bị chấm lệch nhau.
3. **Danh mục "Loại doanh nghiệp" trên biểu mẫu đăng ký công khai đang lẫn dữ liệu kiểm thử.** Lựa chọn đầu tiên trong danh sách là **"QTHT-B2 LDN 21/07 test doanh thu trong"** (ảnh `-02`) — hiện ra cho **mọi doanh nghiệp thật** truy cập trang đăng ký. Là dữ liệu do đội kiểm thử tạo ở vòng trước, không phải lỗi mã nguồn, nhưng nên dọn.
4. **Giao diện gửi cố định `captchaToken: "mock-captcha"`** trong yêu cầu đăng ký, trong khi hợp đồng API đánh dấu `captchaToken` là **tham số bắt buộc**. Tức cơ chế chống máy tự động đang được thoả bằng một giá trị giả cố định trên một điểm cuối công khai. SRS không nhắc tới captcha ở SCR-VIII-08 / FR-VIII-22.
5. **Số điện thoại doanh nghiệp: giao diện bắt buộc (đúng SRS dòng 1922/1059) nhưng API không đặt bắt buộc** — gọi thẳng API có thể tạo hồ sơ thiếu số điện thoại.
6. **Ô chọn "Tỉnh/Thành phố" chỉ nạp 10 mục đầu**, phần còn lại phụ thuộc thao tác gõ tìm kiếm. SRS dòng 1912 yêu cầu đủ 63 mã tỉnh/thành. Chưa đủ dữ kiện để kết luận là thiếu hay chỉ là nạp dần theo cuộn — cần đo riêng, không thuộc phạm vi case này.

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng khối `tools/toast-capture.js`, **không lọc trùng**, đọc bằng `innerText`; đã tự kiểm **`soObserverDangSong = 1`** *trước* khi tin số liệu. Thao tác ghi dữ liệu đo kèm số request: **1 request / 1 khung thông báo** ⇒ không lặp, không tạo trùng bản ghi.
- **Mọi ảnh đều đã được mở ra đọc**, không chỉ lưu.
- **Hai lần phép đo của QA nói dối — bắt được nhờ mở ảnh ra nhìn, nên không log oan:**
  1. Đọc danh sách lựa chọn ô "Loại doanh nghiệp" bằng `innerText` của cả khối thả xuống thì ra **2 dòng mã định danh dạng UUID** trông như lỗi hiển thị. Mở ảnh `-02` ra nhìn thì màn hình **chỉ có 5 lựa chọn chữ**, không hề có UUID — đó là các nút ẩn dành cho trình đọc màn hình. Đo lại đúng bằng `.ant-select-item-option-content` → khớp ảnh.
  2. Kiểm "thanh độ mạnh mật khẩu" bằng cách tìm `.ant-progress` **bên trong** khối trường thì ra **không có**, suýt kết luận thiếu. Mở ảnh `-06` ra nhìn thì **thanh đỏ + danh sách 5 tiêu chí hiện rõ**; thực tế khối đó nằm **ngay sau** khối trường chứ không nằm trong. Đã đổi tên tệp ảnh `-06` cho khớp nội dung điểm ảnh.
- **Một ứng viên lỗi đã bị bác bằng phương pháp thứ hai:** lượt gửi đầu chỉ kèm **1** mã lĩnh vực dù đã bấm 2 mục ⇒ nghi ô chọn nhiều bị rơi lựa chọn. Đo lại bằng thao tác bấm thật có chờ giữa 2 lần bấm thì **giữ đủ 2 mục** (ảnh `-12`). Nguyên nhân là kịch bản của QA bấm 2 mục liên tiếp trong cùng một nhịp nên tham chiếu mục thứ hai đã cũ ⇒ **lỗi phép đo, không phải lỗi ứng dụng**.
- Trước khi chốt đã **tải lại trang bỏ qua bộ nhớ đệm** và đo lại toàn bộ danh sách trường, đồng thời lặp lại phép đo trong **phiên trình duyệt cách ly thứ hai** — cả hai lần cho kết quả trùng khớp.
