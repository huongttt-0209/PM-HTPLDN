# Audit verify — CBKQDTBD_01 (row 121, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Công bố kết quả đào tạo bồi dưỡng · **Ngày verify:** 2026-08-03
**Cột P (dev điền):** `dev done` · **Cột Q (Verify) trước khi ghi:** TRỐNG

## Note dev trước khi QA đè (đọc lại sheet 2026-08-03)

**Cột R (`DEV phản hồi lần 1`) TRỐNG tại thời điểm QA ghi (2026-08-03).**
Dev chỉ điền cột P = `dev done`, không kèm giải trình. Không có nội dung nào bị đè mất.

---

## CỔNG 1 — Bằng chứng đối tác (đã mở FULL-RES)

**File:** `partner-evidence/CBKQDTBD_01.jpg` (1915×1036, JPEG) — ảnh tĩnh, không phải video.
**Crop phóng to đã đọc:** `frames/CBKQDTBD_01/tabbar-zoom.png` · `stepper-zoom.png` · `url-zoom.png` · `role-zoom.png`

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Giá trị đọc được từ ảnh |
|---|---|---|
| (a) | **URL / ID bản ghi** | `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/0aad5545-9361-4fe4-854a-18e3fdce5862?tab=ket-qua-kiem-tra` |
| (b) | **Trạng thái entity** (stepper) | Dự thảo ✓ · Chờ duyệt ✓ · Đã duyệt ✓ · Đang diễn ra ✓ · Đã kết thúc ✓ · Chờ duyệt KQ ✓ · **Hoàn thành = bước 7 ĐANG ĐỨNG (vòng tròn xanh đậm, số 7)** ⇒ khóa ở **HOAN_THANH** |
| (c) | **Dữ liệu tiền đề** | Banner xanh **"Kết quả đào tạo đã được phê duyệt"** + bảng 2 học viên có Điểm kiểm tra (5.0 / 10.0), Kết quả (Đạt / Không đạt), Xếp loại (Trung bình / Giỏi) ⇒ **có ≥1 KQ đã duyệt** |

### (a)(b)(c)(d) theo yêu cầu case

- **(a) Mã + tên khóa học:** ảnh **không hiện mã/tên khóa** (khung chi tiết bị cuộn, chỉ thấy breadcrumb `Trang chủ / Đào tạo, tập huấn / Khóa học / Chi tiết`). Định danh duy nhất = **UUID `0aad5545-9361-4fe4-854a-18e3fdce5862`** trên URL. UUID này thuộc env đối tác `htpldn-uat.ospgroup.vn`, **không tồn tại** trên env QA `18.143.165.120.nip.io`.
- **(b) Trạng thái khóa học:** **Hoàn thành (HOAN_THANH)** — đọc rõ từ stepper, bước 7 tô đậm. Đây là **dữ kiện quyết định verdict**.
- **(c) Danh sách tab đang hiện trên màn chi tiết của đối tác — 7 tab:**
  `Thông tin` · `Học viên` · `Lịch học` · `Điểm danh` · `Kết quả` (đang chọn) · `Bài giảng đã gán` · `Đề kiểm tra`
  ⇒ **KHÔNG có tab "Công bố kết quả".**
- **(d) Vai trò / đơn vị:** góc phải hiện `BTP · TW` + **`Cán bộ NV Trung ương`** + mã vai trò **`CB_NV_TW`**. Đồng hồ máy đối tác: **2026-07-28 11:03 AM**.

### Quan sát bổ sung từ ảnh (dùng cho phân tích, không phải tiêu chí case)

Trong **tab "Kết quả"** của đối tác đã có sẵn nút **"Công bố kết quả"** (nút xanh, icon upload) nằm cạnh "Xuất DOCX", và một nút **"Công khai"** ở cuối bảng. ⇒ Ở env đối tác, chức năng công bố **có tồn tại** nhưng được đặt **bên trong tab "Kết quả"**, KHÔNG phải một tab thứ 8 riêng như SRS mô tả.

---

## CỔNG 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `partner-evidence/CBKQDTBD_01.jpg`, vùng chứa LỖI = **thanh tab ngay dưới stepper** (crop `frames/CBKQDTBD_01/tabbar-zoom.png`). Lỗi thấy trong vùng đó: màn chi tiết khóa học chỉ có **7 tab**, thiếu hẳn tab **"Công bố kết quả"**, dù stepper cho thấy khóa **đã Hoàn thành** và banner báo **kết quả đã được phê duyệt**.
2. **Đối tác phản ánh CỤ THỂ:** Theo bước thực hiện họ ghi trên sheet — *"3. Chọn tab 'Công bố kết quả'"* — họ **không tìm thấy tab đó** để bấm. Kết quả thực tế họ ghi: *"Màn hình chi tiết không có tab riêng 'Công bố kết quả'"*. Đây là phản ánh về **cấu trúc tab của màn chi tiết khóa học**, KHÔNG phải về nút bấm hay thông báo.
3. **Data + bước tái hiện:** Khóa học ở **Hoàn thành** + có ≥1 học viên có kết quả **đã được phê duyệt** → đăng nhập vai trò **CB Nghiệp vụ Trung ương** → Đào tạo, tập huấn → Khóa học → xem chi tiết khóa → đọc danh sách tab.

---

## CỔNG 3 — Đối chiếu SRS vs thực tế web

**Nguồn SRS duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`

### Trích nguyên văn (đã tự mở file xác nhận số dòng)

| file:line | Nguyên văn |
|---|---|
| `srs-fr-03-dao-tao.md:1347` | `### FR-III-19: Công bố kết quả đào tạo (UC38) [v3.5 — Hướng B viết lại theo Thay đổi 9 cổng duyệt 2026-05-06]` |
| `srs-fr-03-dao-tao.md:1349` | `**UC Reference:** UC 38 | **Priority:** Essential | **Stability:** Medium` |
| `srs-fr-03-dao-tao.md:1350` | `**Màn hình:** SCR-III-02 (Tab "Công bố kết quả")` |
| `srs-fr-03-dao-tao.md:1363` | `| PRE-02 | Khóa học ở HOAN_THANH (kết quả đã được CB PD duyệt — FR-III-18) |` |
| `srs-fr-03-dao-tao.md:1364` | `| PRE-03 | Có ≥1 KET_QUA_DAO_TAO trạng thái DA_DUYET |` |
| `srs-fr-03-dao-tao.md:1891` | `**Loại màn hình:** Chi tiết với **8 tabs** (Thay đổi 4 thêm Tab Lịch học; Thay đổi 9 thay Tab Chứng nhận v3 bằng Tab Công bố kết quả; STT 25 UAT 2026-05-26 thêm Tab Đề kiểm tra):` |
| `srs-fr-03-dao-tao.md:1909` | `8. **Tab 8 — Công bố kết quả** [v3.5 — Thay đổi 9 — thay Tab Chứng nhận v3]: Nút "Công bố tất cả" + công tắc "Công bố lên Cổng PLQG (Cổng tự kéo)" + nút "Hủy công bố tất cả". Bảng HV có kết quả: Cột Chọn dòng · **Họ tên · Email · Số điện thoại · Đơn vị** · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động (Công bố/Hủy công bố cá nhân). …` |
| `srs-fr-03-dao-tao.md:1735` | `> 3. **SCR-III-02 Khóa học** (sub-menu 3) — quản lý khóa cấp 3 với 7 tab: Thông tin · Lịch học (Thay đổi 4) · Học viên · Điểm danh · Kết quả kiểm tra · Bài giảng · Công bố kết quả (Thay đổi 9 — thay tab Chứng nhận v3)` |
| `srs-fr-03-dao-tao.md:1914` | `**Tab v3 cũ "Chứng nhận" đã LOẠI BỎ:** … Tab Chứng nhận thay bằng Tab 7 Công bố kết quả.` |

### DANH SÁCH TAB CHUẨN của SCR-III-02 (SRS `:1891-1909` — 8 tab)

| # | Tên tab theo SRS | Có trên màn đối tác? |
|:-:|---|:-:|
| 1 | Thông tin | ✅ |
| 2 | Lịch học | ✅ |
| 3 | Học viên | ✅ |
| 4 | Điểm danh | ✅ |
| 5 | Kết quả kiểm tra | ✅ (web đặt tên `Kết quả`) |
| 6 | Bài giảng | ✅ (web đặt tên `Bài giảng đã gán`) |
| 7 | Đề kiểm tra | ✅ |
| 8 | **Công bố kết quả** | ❌ **THIẾU** |

> **Lưu ý mâu thuẫn nội bộ SRS (không đổi kết luận):** dòng `:1891` ghi "8 tabs" và liệt kê đủ 8 mục; dòng `:1735` và `:1914` còn ghi "7 tab" / "Tab 7 Công bố kết quả" — đây là **số thứ tự sót lại chưa cập nhật sau khi thêm Tab Đề kiểm tra** (STT 25 UAT 2026-05-26). **Cả 3 dòng đều thống nhất một điểm:** "Công bố kết quả" là **MỘT TAB** của SCR-III-02. Vì vậy đây **không** phải ca SRS silent → **không** phải `BA confirm`.

### Vùng SRS SILENT — KHÔNG bắt lỗi

Chuỗi thông báo **"Đã công bố kết quả cho {số lượng} học viên"** mà đối tác ghi ở cột *Kết quả mong đợi* **KHÔNG được SRS quy định** (FR-III-19 §Outputs `:1403-1410` chỉ định nghĩa `so_hv_cong_bo`, không quy định câu chữ thông báo). ⇒ **KHÔNG log lỗi wording thông báo trong case này.**

---

## ĐO THỰC TẾ TRÊN WEB (re-verify LIVE)

**Env:** `https://18.143.165.120.nip.io` · **Bản dựng:** **HTPLDN · V1.0.5** (đọc ở chân sidebar; asset bundle `index-bJhJGCw4.js`, đã **tải lại trang bỏ qua cache** `ignoreCache:true` trước khi đo).
**Account thực dùng:** **`cbnv_tw`** — "CB Nghiệp vụ - Trung ương", `CB_NV_TW`, `donViId 00000000-0000-4000-8000-000000000001`, `capDonVi TW`. (**Không** dùng `admin` ra verdict; `cbpd_tw_01` chỉ dùng khảo sát danh sách khóa trước khi đăng xuất.)
**Thời điểm đo:** 2026-08-03 ~17:46–17:56.

### 1. Tab "Công bố kết quả" — ĐÃ CÓ, ở CẢ 2 trạng thái khóa học

Bảng đo đầy đủ + phương pháp soi node ẩn: xem `cond/CBKQDTBD_01.md` §Đo đối chiếu ≥2 trạng thái.

| Khóa | Trạng thái | Số tab | Có "Công bố kết quả"? | Ảnh (đã mở đọc) |
|---|---|:-:|:-:|---|
| `KH-QAW7-HOINGHI` | Đang diễn ra (bước 4) | 8 | ✅ CÓ | `image/CBKQDTBD_01-A-dangdienra-tabs.png` |
| `AAA-KH-TW` | **Hoàn thành (bước 7)** — đúng tiền đề đối tác | 8 | ✅ CÓ | `image/CBKQDTBD_01-B-hoanthanh-tabs.png` |

### 2. Nội dung tab — KHÔNG phải "Chức năng đang phát triển", KHÔNG phải empty state

Phân loại theo CLAUDE.md §Quy trình phân loại tab trống: `coDangPhatTrien = false`, `.ant-empty` = 0 phần tử, bảng render **4 dòng dữ liệu thật**.
Thành phần quan sát được (ảnh `image/CBKQDTBD_01-C-tab-congbo-noidung.png`): công tắc **"Công bố lên Cổng PLQG"** · nút **"Công bố tất cả"** · nút **"Hủy công bố tất cả"** · bảng học viên · nút Công bố/Hủy từng dòng.

### 3. Thao tác thật — chạy ĐÚNG (artifact QUAN SÁT loại "Thao tác/state")

Bộ bắt thông báo: **chỉ dùng `tools/toast-capture.js`** (không lọc trùng, đọc `innerText`, đếm request). **Tự kiểm `soObserverDangSong = 1`** trước mỗi lần đo ⇒ số liệu hợp lệ.

| Thao tác | Request | Thông báo | Kết quả bảng |
|---|---|---|---|
| **Hủy công bố tất cả** (nhập lý do 66 ký tự) | `1` — `POST /api/v1/khoa-hocs/{id}/ket-quas/unpublish` | `1` khung — *"Đã gửi yêu cầu hủy công bố."* | 4 dòng → **"Chưa công bố"**, Thời điểm công bố = `—` |
| **Công bố tất cả** (qua hộp thoại xác nhận) | `1` — `POST /api/v1/khoa-hocs/{id}/ket-quas/publish` | `1` khung — *"Đã gửi yêu cầu công bố. Hệ thống sẽ đẩy sang Cổng PLQG."* | 4 dòng → **"Đã công bố"**, Thời điểm công bố = **`03/08/2026 17:55`** |

- **1 request ↔ 1 thông báo** ở cả 2 thao tác ⇒ **không** có lỗi thông báo lặp trong luồng này.
- Hộp thoại hủy công bố **bắt buộc lý do ≥10 ký tự** (`placeholder` "Nhập lý do hủy công bố (tối thiểu 10 ký tự)…") ⇒ khớp **BR-FLOW-04** (SRS `:1380`, `:1397`).
- Hộp thoại xác nhận công bố nêu rõ đẩy sang Cổng PLQG qua hàng đợi + ghi audit log ⇒ khớp **BR-FLOW-05** (SRS `:1389`) và Postcondition AUDIT_LOG (SRS `:1416`).
- **Trạng thái dữ liệu đã khôi phục nguyên trạng:** trước khi đo 4 KQ ở "Đã công bố", sau khi đo cũng ở "Đã công bố". Ảnh `image/CBKQDTBD_01-F-sau-congbo-thanhcong.png`.

> **Lưu ý về "Thời điểm công bố":** trước khi đo, 4 dòng hiển thị "Đã công bố" nhưng Thời điểm công bố = `—` (dữ liệu seed đặt cờ `congBo=true` trực tiếp, chưa từng qua luồng công bố). Sau khi công bố lại **qua đúng luồng**, cột này hiển thị đủ `03/08/2026 17:55` ⇒ **`thoi_gian_cong_bo` được ghi đúng**, không phải lỗi. Đây đúng bài học "re-verify trường lưu trong DB phải test trên dữ liệu MỚI".

### 4. Đối chiếu SRS vs thực tế web (Cổng 3 — kết luận)

| SRS yêu cầu (file:line) | Thực tế web V1.0.5 | Đạt? |
|---|---|:-:|
| SCR-III-02 có **8 tab**, tab thứ 8 là **"Công bố kết quả"** (`:1891`, `:1909`) | Có đủ 8 tab, tab "Công bố kết quả" nằm giữa "Kết quả" và "Bài giảng đã gán" | ✅ |
| FR-III-19 thao tác trên **SCR-III-02 Tab "Công bố kết quả"** (`:1350`) | Toàn bộ thao tác công bố / hủy công bố nằm trong đúng tab đó | ✅ |
| PRE-02 khóa **HOAN_THANH** (`:1363`) | Đo trên `AAA-KH-TW` ở Hoàn thành — thao tác chạy | ✅ |
| PRE-03 có **≥1 KQ DA_DUYET** (`:1364`) | 4 học viên có kết quả đã duyệt, đều công bố được | ✅ |
| Nút "Công bố tất cả" + công tắc "Công bố lên Cổng PLQG" + nút "Hủy công bố tất cả" (`:1909`) | Có đủ cả 3 | ✅ |
| Hộp thoại hủy công bố yêu cầu lý do ≥10 ký tự — BR-FLOW-04 (`:1909`, `:1380`) | Có, chặn đúng | ✅ |
| Cột bảng HV: Chọn dòng · **Họ tên · Email · Số điện thoại · Đơn vị** · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động (`:1909`) | Chỉ có: Chọn dòng · STT · **Họ tên** · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động — **thiếu Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm** | ❌ **(ngoài phạm vi case này — xem §Phát hiện thêm)** |

---

## GIẢI THÍCH: vì sao đối tác KHÔNG thấy tab (bắt buộc cho verdict `Pass`)

Chính **ảnh của đối tác** chứa lời giải, không cần suy đoán:

Trong ảnh, ở **tab "Kết quả"**, đối tác đang nhìn một thanh công cụ có nút **"Công bố kết quả"** (nút xanh, icon upload) đặt ngay cạnh nút "Xuất DOCX", cùng một nút "Công khai" ở cuối bảng. Nghĩa là **ở bản dựng họ kiểm thử (28/07/2026), chức năng công bố kết quả được đặt làm MỘT NÚT BÊN TRONG tab "Kết quả"** — chứ không phải một tab riêng. Vì vậy màn chi tiết chỉ có 7 tab và họ **không tìm thấy tab "Công bố kết quả"** để bấm theo bước 3 trong kịch bản của họ.

Trên bản dựng hiện tại **V1.0.5**, chức năng này **đã được tách thành tab riêng thứ 6 trên thanh tab** ("Công bố kết quả"), đúng như SRS `:1350` + `:1909` mô tả — và nút "Công bố kết quả" trong tab "Kết quả" cũng không còn.

⇒ Phản ánh của đối tác **đúng tại thời điểm họ kiểm thử**, và **đã được khắc phục** ở bản dựng hiện tại. Không phải đối tác thao tác sai (nên **không** dùng `Reject`); cũng không phải "không tái hiện được mà không giải thích nổi" (nên **không** cần `Resolved`) — đây là ca **dev đã sửa, QA test lại chạy đúng ⇒ `Pass`**.

---

## VERDICT

**`Pass`** (ghi cột `Verify` — Q; **không đụng cột P** đang là `dev done`).

Căn cứ: tab "Công bố kết quả" **đã tồn tại** trên màn chi tiết khóa học, hiển thị ở **cả** khóa chưa đủ tiền đề lẫn khóa **đúng tiền đề của đối tác** (Hoàn thành + có kết quả đã duyệt), và **hoạt động đúng** — công bố / hủy công bố đều đổi trạng thái thật, 1 request ↔ 1 thông báo, có ràng buộc lý do ≥10 ký tự.

**Vùng SRS silent — KHÔNG bắt lỗi:** chuỗi *"Đã công bố kết quả cho {số lượng} học viên"* ở cột *Kết quả mong đợi* của đối tác không được SRS quy định. Thông báo thực tế của web là *"Đã gửi yêu cầu công bố. Hệ thống sẽ đẩy sang Cổng PLQG."* — khác câu chữ đối tác kỳ vọng nhưng **không log**, đúng chỉ dẫn.

---

## PHÁT HIỆN THÊM NGOÀI PHẠM VI CASE

### (1) Tab "Công bố kết quả" thiếu 5 cột so với SRS `:1909` — ĐÃ log dòng TC mới

SRS `srs-fr-03-dao-tao.md:1909` liệt kê cột bảng học viên của Tab 8 gồm: *Chọn dòng · **Họ tên · Email · Số điện thoại · Đơn vị** · Đề kiểm tra · Điểm · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động*.
Web V1.0.5 chỉ render **7 cột**: Chọn dòng · STT · Họ tên · Kết quả · Trạng thái công bố · Thời điểm công bố · Hành động.
**Thiếu: Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm.**

Đo bằng **2 phương pháp độc lập** (chống "bug ma"):
1. DOM: `[...document.querySelectorAll('.ant-table-thead th')].map(x=>x.innerText.trim())` → `["","STT","Họ tên","Kết quả","Trạng thái công bố","Thời điểm công bố","Hành động"]` (7 phần tử).
2. Ảnh full-res `image/CBKQDTBD_01-F-sau-congbo-thanhcong.png` — đọc bằng mắt, bảng **không có thanh cuộn ngang**, các cột hiển thị trọn vẹn, không cột nào bị cắt.
Hai phương pháp **khớp nhau** ⇒ đủ điều kiện log.

→ Đã mở dòng TC mới `CBKQDTBD_02` trên sheet để tới được dev.

### (2) Phiên đăng nhập bị đăng xuất giữa chừng — KHÔNG log, đã truy ra nguyên nhân là NHIỄU TỪ PHIÊN QA KHÁC

Trong lúc verify, tài khoản `cbnv_tw` bị đá về `/login` **5 lần**, mỗi lần khoảng 90–120 giây sau khi đăng nhập. Dấu vết mạng lặp lại giống nhau:
`GET /api/v1/thong-baos/unread-count` → **401** → ứng dụng tự gọi `POST /api/v1/auth/logout` → chuyển `/login` kèm thông báo **"Đăng xuất thành công"**.

**Ban đầu tôi nghi là lỗi hạ tầng env** (có 1 lần `POST /api/v1/auth/login` trả **HTTP 502**, gợi ý backend khởi động lại làm mất hiệu lực token). **Nhưng kiểm chứng lại bằng nguồn thứ hai thì KHÔNG phải:**

Đọc `tools/sheet_write.log` thấy có **phiên QA khác chạy song song trong cùng khung giờ**, ghi sheet lúc `17:59:07`, `18:00:10`, `18:00:43` — trong đó dòng `CNDSMLTVV_OOS_01` ghi rõ *"Tài khoản kiểm tra: **cbnv_tw_02**"*. Chrome DevTools MCP là **một tiến trình trình duyệt duy nhất, dùng chung profile** cho mọi phiên; phiên kia đăng nhập tài khoản khác (và chạy thủ tục đăng xuất theo Rule 3: `POST /api/v1/auth/logout` + xóa `localStorage`) thì **phiên của tôi bị đăng xuất theo** — khớp chính xác thông báo "Đăng xuất thành công" quan sát được.

⇒ **Không phải lỗi sản phẩm, KHÔNG log lên sheet.** Đây đúng loại nhiễu mà `PROMPT-verify1-conlai-2026-08-03.md` §4 đã cảnh báo (*"các agent dùng trình duyệt phải chạy TUẦN TỰ, KHÔNG song song"*). **Không** ảnh hưởng kết luận của case: mọi phép đo quyết định (danh sách tab ở 2 trạng thái; công bố / hủy công bố kèm ảnh + số request + số thông báo) đều lấy trọn vẹn **bên trong một phiên đăng nhập còn hiệu lực**, và đã **mở ảnh đọc lại** để xác nhận đúng nội dung.

**Bài học ghi lại:** ảnh chụp đầu tiên của tôi (`CBKQDTBD_01-A-*.png` bản đầu) thực chất chụp trúng **màn hình đăng nhập** chứ không phải màn khóa học — nếu chỉ lưu ảnh mà không mở ra đọc thì đã lấy nhầm ảnh làm bằng chứng. Đúng điều postmortem 16/07 cảnh báo ở mục A2. (Ảnh đã được chụp lại đúng nội dung.)

**Vệ sinh bằng chứng:** một ảnh từng được lưu với tên `CBKQDTBD_01-E-toast-congbo.png` nhưng nội dung pixel lại là **màn hình đăng nhập** (do phiên bị đá đúng lúc chụp) — tên file KHÔNG khớp nội dung = bằng chứng INVALID theo §GATE. Đã **đổi tên thành `CBKQDTBD_01-X-phien-bi-dang-xuat-boi-phien-khac.png`** cho đúng nội dung thật; ảnh này chỉ dùng minh hoạ mục (2) này, **không** dùng làm bằng chứng cho verdict.

---

## DANH MỤC BẰNG CHỨNG (đều đã MỞ RA ĐỌC, tên file khớp nội dung)

| File | Nội dung thực tế đã đọc |
|---|---|
| `partner-evidence/CBKQDTBD_01.jpg` | Ảnh gốc đối tác — khóa Hoàn thành, 7 tab, thiếu tab Công bố kết quả |
| `frames/CBKQDTBD_01/tabbar-zoom.png` | Phóng to thanh tab của đối tác — đọc rõ 7 tên tab |
| `frames/CBKQDTBD_01/stepper-zoom.png` | Phóng to stepper — bước 7 "Hoàn thành" đang đứng |
| `image/CBKQDTBD_01-A-dangdienra-tabs.png` | `KH-QAW7-HOINGHI` — Đang diễn ra, **8 tab có "Công bố kết quả"** |
| `image/CBKQDTBD_01-B-hoanthanh-tabs.png` | `AAA-KH-TW` — Hoàn thành, **8 tab có "Công bố kết quả"** |
| `image/CBKQDTBD_01-C-tab-congbo-noidung.png` | Nội dung tab Công bố kết quả — công tắc + 2 nút + bảng 4 HV |
| `image/CBKQDTBD_01-D-modal-huycongbo.png` | Hộp thoại hủy công bố, bắt lý do ≥10 ký tự |
| `image/CBKQDTBD_01-F-sau-congbo-thanhcong.png` | Sau khi công bố — 4 HV "Đã công bố" + mốc `03/08/2026 17:55` |
| `image/CBKQDTBD_01-X-phien-bi-dang-xuat-boi-phien-khac.png` | Màn đăng nhập kèm "Đăng xuất thành công" — minh hoạ nhiễu phiên, KHÔNG dùng cho verdict |
