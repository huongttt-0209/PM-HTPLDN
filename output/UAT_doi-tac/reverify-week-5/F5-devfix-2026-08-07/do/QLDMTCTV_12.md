# QLDMTCTV_12 — Cửa sổ Cập nhật trạng thái hoạt động của Tổ chức tư vấn (đo Giai đoạn B)

**Case:** QLDMTCTV_12 · dòng 149 · tab `bug`
**Chuẩn chấm đã khóa:** [`../chuan/QLDMTCTV_12.md`](../chuan/QLDMTCTV_12.md) — Giai đoạn B **không đổi** quan hệ MATCH/DIFF/GAP, **không mở rộng** phép đo, **không ghi Google Sheet**.
**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — mọi số dòng dẫn dưới đây đã **tự mở file đọc lại** trong lượt này (`sed -n '<N>p' srs-fr-04-chuyen-gia-tvv.md`), không bê từ chuẩn chấm, không lấy từ trí nhớ.
**Trạng thái đối tác:** Fail · Dopai N/R · **TKM phản hồi lần 1: "Màn hình không có nút chức năng"** · Trạng thái dev fix: Fixed · có 1 ảnh bằng chứng.

---

## 1. Điều kiện đo

| Hạng mục | Giá trị thực |
|---|---|
| **Env** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| **Bó mã FE** | `assets/index-D4Buvu4S.js` · `assets/index-DVlgOkLg.css` — đọc trực tiếp từ DOM lúc 03:44:39 giờ VN. Khớp bản dựng **sau** lần deploy 02:23:01 ghi ở [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| FE etag / last-modified | `W/"6a74df15-428"` · `Thu, 06 Aug 2026 19:23:01 GMT` (= **02:23:01 giờ VN 07/08**) — đo bằng `curl` lúc 03:44:09 |
| Phiên bản app | sidebar hiện **`HTPLDN · V1.0.9`** (ảnh đối tác là `V1.0.2`, 31/07/2026) |
| **Thời điểm đo** | 2026-08-07 giờ VN, 03:44:09 → 03:53:24 (mốc từng bước ở [`../image/QLDMTCTV_12-do-chi-tiet.txt`](../image/QLDMTCTV_12-do-chi-tiet.txt)) |
| MailHog | `http://18.143.165.120:8025` — lọc đúng mailbox `cbnv_tw_03@htpldn.test`, `limit=8` |
| **Tài khoản ra verdict** | **`cbnv_tw_03` / `Test@1234`** — `/auth/me` 200: `vaiTro:["CB_NV_TW"]` · `capDonVi:"TW"` · `donViId:"00000000-0000-4000-8000-000000000001"` · `hoTen:"CB Nghiệp vụ - Trung ương #03"`. Header hiện "Cán bộ Nghiệp vụ Trung ương · BTP · TW", chân sidebar "Bộ Tư Pháp · Cục Bổ trợ tư pháp" |
| **Không dùng admin/QTHT** | ✅ **KHÔNG** dùng `admin` hay QTHT ở **bất kỳ** bước nào của case này (kể cả chuẩn bị dữ liệu). Đó chính là lỗi tiền đề của ảnh đối tác |
| Tab dùng phiên | 1 tab, ngữ cảnh trình duyệt riêng biệt `tctv12` (cookie/localStorage tách khỏi các phiên khác trong lô) |
| Số lần bấm sidebar | **1** (chỉ "Tổ chức tư vấn") — dưới ngưỡng 3 của lỗi app đã biết "bấm sidebar lần thứ 4 làm trang mất ổn định" |

### Hòa giải điểm tranh chấp ghi ở BAN-DUNG.md

[`../BAN-DUNG.md`](../BAN-DUNG.md) ghi selector ô đăng nhập "CHƯA KẾT LUẬN" (lượt QLDX_06 báo mất placeholder, lượt QLDKTK_10 báo còn). Lượt này **lấy uid thật bằng `take_snapshot`** rồi mới điền, đúng yêu cầu. Đọc thêm DOM để chốt: trên **cùng bó mã `index-D4Buvu4S.js`**, ô tên đăng nhập có **CẢ HAI**: `id="login-username"` **và** `placeholder="Nhập tên đăng nhập"`; ô mật khẩu có `id="login-password"` · `placeholder="Nhập mật khẩu"`. ⇒ Quan sát của QLDKTK_10 đúng; báo cáo của QLDX_06 sai ở điểm này. Ghi lại để lô sau không đi theo giả định sai.

---

## 2. Bản ghi dùng để đo — **DÙNG LẠI dữ liệu QA có sẵn, KHÔNG tạo mới**

| Hạng mục | Giá trị |
|---|---|
| **Mã tổ chức** | **`TC-TW-DEMO-001`** |
| Tên | Công ty Luật TNHH Demo Kiểm Thử |
| `id` | `fbeea7e9-118e-49ce-abaf-6245a9ebe604` |
| **Đơn vị chủ bản ghi** | `donViId = 00000000-0000-4000-8000-000000000001` = **ĐÚNG đơn vị của `cbnv_tw_03`** (Bộ Tư Pháp · Cục Bổ trợ tư pháp, cấp TW) |
| **Trạng thái trước khi đo** | **Đang hoạt động** (`HOAT_DONG`) · `version` 5 |
| **Số TVV liên kết** | **0** (ô "Số TVV liên kết" trên màn = 0 · API `soTvvLienKet: 0`) |
| Loại hình · Người đại diện | Công ty Luật · Nguyễn Văn Demo |
| Có tạo mới không? | **KHÔNG.** Dùng lại bản ghi QA sẵn có trên env, không chạy luồng tạo + trình phê duyệt + phê duyệt |

**Vì sao chọn bản ghi này.** `GET /api/v1/to-chuc-tu-vans?page=1&limit=100` trả `meta.countByTrangThai = {MOI_DANG_KY:2, CHO_PHE_DUYET:2, TU_CHOI:0, HOAT_DONG:3, TAM_DUNG:0, VO_HIEU_HOA:0}`. Trong 3 bản ghi *Đang hoạt động* có **2 thuộc đúng đơn vị** của tài khoản đo: `TCTV-SEED-0001` và `TC-TW-DEMO-001`; bản thứ 3 (`TC-STP-AG-0001`, `donViId 00000000-0000-4000-8002-000000000006`) **khác đơn vị nên không dùng**. Chọn `TC-TW-DEMO-001` để chừa `TCTV-SEED-0001` làm dữ liệu nền cho các phép đo khác.

**Không đụng dữ liệu đối tác.** Bản ghi trong ảnh đối tác (`TC-STP-HN-0001`, `d6434545-b76b-47ae-8be7-8bceea2d01a7`, đơn vị Sở Tư pháp Hà Nội) **không được mở, không được sửa** — khác đơn vị với vai trò bắt buộc.

**Nhánh đo: "Tạm dừng".** Không đo nhánh "Vô hiệu hóa" (theo chuẩn chấm §9 mục 5). Ghi rõ: bản ghi này có **0 TVV liên kết**, nên chốt `:992`/`:1015`/`:2394` sẽ **không** chặn — nhưng vẫn giữ nhánh Tạm dừng để đúng phạm vi đã khóa và để khôi phục được.

---

## 3. Bảng kết quả theo từng vế

| Vế | Quan hệ (đã khóa) | Số đo / nguyên văn quan sát được | Kết quả |
|---|---|---|---|
| **C1** — chi tiết TCTV **có** đường vào chức năng cập nhật trạng thái | **MATCH → TEST** | Thẻ **"Thao tác"** chứa **4** điều khiển, nguyên văn nhãn: **`Chỉnh sửa`** · **`Cập nhật trạng thái`** · công tắc `Công khai:` · **`Xóa`**. Vùng header chỉ có `← Quay lại danh sách`. Tổng nút/liên kết hiển thị trong `<main>` = **6**. **Không có menu "…"** nào trên màn chi tiết (0 phần tử `.ant-dropdown-trigger` hiển thị) — đã tìm cả header, cả thẻ "Thao tác", cả menu "…" trước khi kết luận. Đếm bằng `innerText` + lọc `getClientRects()`/`offsetParent`; **không dùng `textContent`** | ✅ **PASS** |
| **C2** — cửa sổ có trường **Trạng thái mới** | **MATCH → TEST** *(dạng widget = GAP, chỉ ghi)* | Bấm nút → mở **HỘP THOẠI (modal)**, `class="ant-modal"`, `role=dialog aria-modal`, tiêu đề **`Cập nhật trạng thái hoạt động`**. Có trường **`Trạng thái mới`** dạng **danh sách chọn** (`.ant-select-single`), chỗ giữ chỗ `Chọn trạng thái mới`. Có trường **`Lý do thay đổi`** (`<textarea>`), chỗ giữ chỗ `Nhập lý do thay đổi trạng thái (tối thiểu 10 ký tự)`. Nút: `Hủy` · `Đồng ý`. Ghi nhận (không Fail): là **hộp thoại đúng như `:1721`**, không phải khay bên; widget **đúng là "danh sách chọn"** như phiếu yêu cầu, không phải radio; nhãn xác nhận là **[Đồng ý]** | ✅ **PASS** |
| **C3a** — tập lựa chọn ⊆ {Đang hoạt động, Tạm dừng, Vô hiệu hóa} | **MATCH → TEST** | Ở bản ghi *Đang hoạt động*: **tổng node `.ant-select-item-option` trong DOM = 2**, **số node hiển thị thật = 2** (hai số **trùng nhau** ⇒ không có node ẩn bị đếm oan). Nguyên văn: **`Tạm dừng`** · **`Vô hiệu hóa`**. Cây trợ năng cùng lúc cũng chỉ có 2 mục. **Không lẫn** `Mới đăng ký` / `Chờ phê duyệt` / `Đã từ chối` | ✅ **PASS** |
| **C3b** — **chỉ hiển thị trạng thái chuyển được** theo máy trạng thái | **GAP → BA** | **Hiện trạng, 2 điểm dữ liệu:** bản ghi *Đang hoạt động* → hiện `Tạm dừng` · `Vô hiệu hóa`; bản ghi *Tạm dừng* → hiện `Đang hoạt động` · `Vô hiệu hóa`. Cả 2 lần: node DOM = node hiển thị (2 = 2). Không lần nào hiện lại chính trạng thái hiện tại. Đối chiếu SM-TCTV: `HOAT_DONG → {TAM_DUNG (:2392), VO_HIEU_HOA (:2394)}`, `TAM_DUNG → {HOAT_DONG (:2393), VO_HIEU_HOA (:2395)}` — **khớp**. ⇒ Bản dựng **đang lọc** theo trạng thái hiện tại | — **KHÔNG chấm** (chuyển BA) |
| **C4** — Lý do thay đổi **bắt buộc** | **MATCH → TEST** | Chọn `Tạm dừng`, **để trống** ô Lý do (bộ đếm `0 / 1000`): nút **`Đồng ý` có thuộc tính `disabled`**, `cursor: not-allowed`, không bị phần tử khác che. Bấm bằng công cụ → *"The element did not become interactive"*. Thử 2 đường vòng: (a) bắn đủ chuỗi `pointerdown/mousedown/pointerup/mouseup/click` lên chính nút → **0 yêu cầu ghi**; (b) gõ Enter trong ô + bắn `submit` (ô không nằm trong `<form>`) → **0 yêu cầu ghi**. **Thông báo chặn thật: KHÔNG có chữ nào** — bộ bắt thông báo (cài **trước** khi bấm, **không lọc trùng**) ghi 0 khối; 0 phần tử `.ant-form-item-explain-error` / `[role=alert]`. Cách chặn là **làm mờ + vô hiệu hóa nút**. **Hệ quả:** không có `POST .../cap-nhat-trang-thai` nào trong khoảng đo C4; badge **giữ nguyên `Đang hoạt động`** | ✅ **PASS** |
| **C5** — Lý do **tối thiểu 10 ký tự** (đo **cả 2 phía biên**) | **MATCH → TEST** | **Biên 9 ký tự** — chuỗi `TamDung09` (đọc lại từ ô: 9, không có khoảng trắng đầu/cuối), bộ đếm `9 / 1000`: `Đồng ý` **disabled**, bắn đủ chuỗi sự kiện chuột → **0 yêu cầu ghi**, **0 thông báo chặn** (chặn bằng nút mờ), badge giữ `Đang hoạt động` ⇒ **bị chặn**. **Biên đúng 10 ký tự** — chuỗi `TD07080351` (đọc lại: 10), bộ đếm `10 / 1000`: `Đồng ý` **bấm được** → **đúng 1** `POST .../cap-nhat-trang-thai` (không double-submit), thân yêu cầu `{"trangThaiMoi":"TAM_DUNG","lyDo":"TD07080351","version":5}` → **200**, thân trả về `trangThai:"TAM_DUNG"` · `version:6` · **`lyDoTamDung:"TD07080351"`** ⇒ **được nhận, lưu nguyên vẹn** | ✅ **PASS** |
| **C6** — Lý do **tối đa 5.000 ký tự** | **GAP → BA** | **Hiện trạng:** cố nhập **5001** ký tự → ô **chỉ nhận 1000**; bộ đếm `1000 / 1000`; **thuộc tính thật của ô: `maxlength="1000"`**; **không có thông báo / cảnh báo nào** (0 khối thông báo, 0 phần tử báo lỗi) ⇒ **cắt âm thầm** phần vượt, người dùng không được báo. Ngưỡng thực tế **1.000 ≠ 5.000** như phiếu yêu cầu | — **KHÔNG chấm** (chuyển BA) |

**Tổng: 5/5 vế route TEST đều PASS (C1 · C2 · C3a · C4 · C5). 2 vế route BA (C3b · C6) chỉ ghi hiện trạng, không chấm, không log bug.**

### Thao tác thành công + đếm request kèm thông báo

| Thao tác | Số request thật | Thông báo bắt được (observer **không lọc trùng**, `innerText`) |
|---|---|---|
| Bấm [Đồng ý] khi ô Lý do **trống** | **0** `POST cap-nhat-trang-thai` | **0 khối** — không có chữ nào |
| Bấm [Đồng ý] khi Lý do **9 ký tự** | **0** `POST cap-nhat-trang-thai` | **0 khối** — không có chữ nào |
| Bấm [Đồng ý] khi Lý do **10 ký tự** | **đúng 1** `POST` → **200** | **`Cập nhật trạng thái thành công`** — 4 bản ghi observer nhưng **cùng 1 chuỗi, cùng mốc `20:51:07.719Z`**, do 1 node bị 2 bộ chọn lồng nhau bắt trùng ⇒ **1 thông báo**, không phải 4. Chốt bằng số request = 1 ⇒ **không double-submit** |
| Bấm [Đồng ý] khi khôi phục | **đúng 1** `POST` → **200** | **`Cập nhật trạng thái thành công`** |

Sau thao tác thành công: hộp thoại tự đóng (0 `.ant-modal` hiển thị) · badge đổi **`Tạm dừng`** · thẻ "Thao tác" còn `Chỉnh sửa` / `Cập nhật trạng thái` / `Xóa` (công tắc `Công khai` biến mất vì bản ghi không còn Đang hoạt động — **chỉ ghi nhận**) · nút `Cập nhật trạng thái` **vẫn hiện** ở trạng thái Tạm dừng.

### Đối chứng độc lập — **đúng MỘT đường**: tab "Lịch sử"

`GET .../fbeea7e9-.../lich-su?page=1&pageSize=20` → 200. Cột nguyên văn: `Thời gian` · `Người thực hiện` · `Hành động` · `Ghi chú / lý do`.

Dòng mới nhất, nguyên văn:

| Thời gian | Người thực hiện | Hành động | Ghi chú / lý do |
|---|---|---|---|
| `07/08/2026 03:51` | `CB Nghiệp vụ - Trung ương #03` | `Cập nhật` | **`TD07080351`** ← khớp **từng chữ** chuỗi vừa nhập |

⇒ Lý do **thực sự được lưu**, không chỉ hiện thông báo. **Chỉ dùng một đường này** để chốt; không mở đường thứ ba. (Lần đọc lại bản ghi qua `fetch` ở §5 là bước **kiểm hoàn nguyên**, không dùng làm căn cứ verdict.)

### Toàn bộ 4xx/5xx trong phiên đo

Duyệt **45** yêu cầu `xhr`/`fetch` của phiên: chỉ có `GET /api/v1/auth/me` → **401** đúng 1 lần **trước khi đăng nhập** (hành vi bình thường của app). **Không 5xx, không 4xx nào khác.** Đúng **2** lần `POST cap-nhat-trang-thai`, cả 2 đều 200 và đều do QA chủ động (1 đo + 1 khôi phục). ⇒ Không có bug candidate loại "workaround 4xx/5xx".

---

## 4. So sánh với tiền đề trong ảnh bằng chứng đối tác

| Hạng mục | **Ảnh đối tác** (`../partner-evidence/QLDMTCTV_12.jpg`) | **Lượt đo này** |
|---|---|---|
| Env | `htpldn-uat.ospgroup.vn` (env nghiệm thu) | `18.143.165.120.nip.io` (env nội bộ) |
| Bản dựng | `HTPLDN · V1.0.2` — 31/07/2026 08:47 | `HTPLDN · V1.0.9` — bó mã `index-D4Buvu4S.js`, deploy 02:23:01 VN 07/08 |
| 🔴 **Vai trò đăng nhập** | **Quản trị viên · `QTHT`** (góc phải: `BTP · TW` + `Quản trị viên` + `QTHT`) | **Cán bộ Nghiệp vụ Trung ương** (`vaiTro:["CB_NV_TW"]`) |
| 🔴 **Đơn vị chủ bản ghi vs đơn vị người đo** | Bản ghi `TC-STP-HN-0001` (**Sở Tư pháp Hà Nội**) — người đo ở **`BTP · TW`** ⇒ **KHÁC đơn vị** | Bản ghi `TC-TW-DEMO-001` (`donViId ...0001`) — người đo `donViId ...0001` ⇒ **CÙNG đơn vị** |
| Trạng thái bản ghi | Đang hoạt động | Đang hoạt động |
| Số TVV liên kết | **3** | **0** |
| Thẻ "Thao tác" | **RỖNG HOÀN TOÀN** — không nút nào | **`Chỉnh sửa` · `Cập nhật trạng thái` · công tắc `Công khai` · `Xóa`** |

**Kết luận so sánh.** Tiền đề của ảnh đối tác **lệch 2 chiều cùng lúc** so với điều kiện hiển thị nút mà đặc tả chốt: **sai vai trò** (QTHT thay vì Cán bộ Nghiệp vụ) **và khác đơn vị** (đo bản ghi của Sở Tư pháp Hà Nội bằng tài khoản ở Bộ Tư pháp cấp TW). `srs-fr-04-chuyen-gia-tvv.md:1721` chốt điều kiện hiển thị là *"Vai trò = Cán bộ Nghiệp vụ cùng đơn vị; trạng thái ∈ {Đang hoạt động, Tạm dừng, Vô hiệu hóa}"*; `:1705`–`:1706` chỉ cấp quyền màn này cho Cán bộ Nghiệp vụ và Cán bộ Phê duyệt cùng đơn vị, **không** có QTHT. Vì thế thẻ "Thao tác" rỗng trong ảnh **không đủ căn cứ** kết luận "màn hình không có nút chức năng". Khi dựng lại đúng tiền đề (Cán bộ Nghiệp vụ **cùng đơn vị** với bản ghi), **nút có mặt, bấm được, chạy trọn luồng và lưu đúng dữ liệu**.

> Nếu điều phối muốn chốt luôn việc "thẻ Thao tác rỗng khi đăng nhập QTHT là đúng đặc tả hay bỏ sót khi soạn" thì đó là **Câu 3** trong chuẩn chấm §8 (đối chiếu `:1848` màn Người hỗ trợ **có ghi rõ** "HOẶC Quản trị hệ thống", màn Tổ chức tư vấn **không ghi**). Lượt này **không** đo bằng QTHT nên **không** kết luận về vế đó.

---

## 5. Dữ liệu đã đổi + đã khôi phục

**Đã đổi (khai đầy đủ — 2 lần ghi, cả 2 qua UI thật, không dùng API tay):**

| Lúc (giờ VN) | Thao tác | Lý do nhập | Kết quả |
|---|---|---|---|
| 03:51:07 | Đang hoạt động → **Tạm dừng** | `TD07080351` (10 ký tự) | 200 · `trangThai:"TAM_DUNG"` · `version` 5→6 · `lyDoTamDung:"TD07080351"` |
| 03:53:13 | Tạm dừng → **Đang hoạt động** (khôi phục) | `KhoiPhuc07080353 - hoan nguyen sau do QLDMTCTV_12` (49 ký tự) | 200 · `trangThai:"HOAT_DONG"` · `version` 6→7 · `lyDoTamDung:null` |

**Đã khôi phục:** ✅ Bản ghi `TC-TW-DEMO-001` **về đúng trạng thái ban đầu**. Kiểm hoàn nguyên (bước dọn dẹp, **không** dùng làm căn cứ verdict): badge header `Đang hoạt động`; đọc lại bản ghi cho `trangThai:"HOAT_DONG"` · `version:7` · `lyDoTamDung:null` · `soTvvLienKet:0` · `laCongKhai:false` (**giữ nguyên** như trước khi đo); thẻ "Thao tác" đã có lại công tắc `Công khai`.

**Còn lại sau lượt đo (không thể và không nên hoàn nguyên):** `version` tăng 5 → 7, và tab "Lịch sử" của bản ghi còn **2 dòng nhật ký** mang tên `CB Nghiệp vụ - Trung ương #03` (03:51 và 03:53 ngày 07/08). Đúng bản chất nhật ký thao tác theo `:1731` — **không phải lỗi**. Không tạo bản ghi mới nào; không xóa bản ghi nào.

---

## 6. Trích nguyên văn SRS đã tự mở đọc trong lượt này

File `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`:

| Dòng | Nguyên văn (cắt) |
|---|---|
| `:974` | `**Tác nhân:** CB Nghiệp vụ (có quyền Quản lý TC TV)` |
| `:976` | `**Preconditions:** TC TV tồn tại, CB NV cùng đơn vị.` |
| `:983` | `\| 2 \| trang_thai_moi \| text \| Y \| HOAT_DONG / TAM_DUNG / VO_HIEU_HOA (theo SM-TCTV) \|` |
| `:984` | `\| 3 \| ly_do \| text (long) \| Y \| Min 10 ký tự \|` |
| `:991` | `\| 2 \| Kiểm tra transition hợp lệ theo SM-TCTV \| SM-TCTV \|` |
| `:1016` | `\| E3 \| Thiếu lý do \| ERR-TT-TC-03 \| "Lý do thay đổi là bắt buộc (≥ 10 ký tự)" \| ERROR \|` |
| `:1701` | `**Loại màn hình:** Trang chi tiết 3 tab + 6 nút hành động ở header` |
| `:1703` | `**Đường dẫn:** /chuyen-gia-tvv/to-chuc/:id` |
| `:1705` | `- Cán bộ Nghiệp vụ: xem + sửa + trình phê duyệt + cập nhật trạng thái + công khai (Tổ chức tư vấn thuộc đơn vị)` |
| `:1706` | `- Cán bộ Phê duyệt cùng đơn vị: xem + phê duyệt / từ chối` |
| 🔴 `:1721` | `\| 8 \| header \| Nút **Cập nhật trạng thái** \| nút phụ \| "Cập nhật trạng thái" \| Click → mở hộp thoại chọn trạng thái mới (Tạm dừng / Khôi phục / Vô hiệu hóa) + lý do (≥ 10 ký tự) → áp dụng MD-TAM-DUNG hoặc MD-VO-HIEU-HOA. … \| Vai trò = Cán bộ Nghiệp vụ cùng đơn vị; trạng thái ∈ {Đang hoạt động, Tạm dừng, Vô hiệu hóa} \|` |
| `:1731` | `\| 12 \| tab 3 \| Tab "Lịch sử" \| … Thời gian + Người thực hiện + Hành động ("Tạo mới" / "Cập nhật" / … / "Tạm dừng" / "Vô hiệu hóa" / "Khôi phục" / …) + Ghi chú/lý do \|` |
| `:2392` | `\| HOAT_DONG \| TAM_DUNG \| Cán bộ Nghiệp vụ tạm dừng \| Có lý do ≥ 10 ký \| Audit log \| FR-IV-NEW-02 \|` |
| `:2393` | `\| TAM_DUNG \| HOAT_DONG \| Cán bộ Nghiệp vụ kích hoạt lại \| — \| Audit log \| FR-IV-NEW-02 \|` |
| `:2394` | `\| HOAT_DONG \| VO_HIEU_HOA \| Cán bộ Nghiệp vụ vô hiệu hóa \| **KHÔNG có TVV đang liên kết hoạt động** … \|` |
| `:2395` | `\| TAM_DUNG \| VO_HIEU_HOA \| Cán bộ Nghiệp vụ vô hiệu hóa \| Same guard \| Gỡ khỏi Cổng, audit \| FR-IV-NEW-02 \|` |

Toàn bộ 20 dòng kiểm lại đều **trùng khít** với chuẩn chấm Giai đoạn A — chuẩn chấm không quote sai dòng nào.

---

## 7. Bẫy đã chặn

**Chống PASS-oan:** đã **bấm thật** nút chứ không kết luận từ ảnh · đã **mở hộp thoại**, **submit thật**, **đối chứng tab Lịch sử** thấy đúng chuỗi lý do · đếm lựa chọn bằng **`innerText` + lọc phần tử hiển thị** và đối chứng "node DOM = node hiển thị (2 = 2)" ⇒ không bug ma · bộ bắt thông báo cài **TRƯỚC** khi bấm, **CẤM lọc trùng**, và luôn **đếm kèm số request** ⇒ chứng minh 1 thông báo = 1 request, không double-submit · **C5 đo cả 2 phía biên** (9 bị chặn **và** đúng 10 được nhận) · C4 kiểm **cả hệ quả** (0 request + badge giữ nguyên), không dừng ở "nút mờ" · mỗi lượt dùng **chuỗi lý do riêng có mốc giờ** · **không** suy "dev đã fix" từ ô "Trạng thái dev fix: Fixed" — đã ghi bản dựng thật khi đo.

**Chống FAIL-oan:** không Fail vì bố cục (nút nằm trong thẻ "Thao tác" thay vì header như `:1701`) · không Fail vì nhãn xác nhận là **[Đồng ý]** thay [Lưu] · không đòi app hiện mã lỗi `ERR-TT-TC-*` · **C6 = GAP** nên không Fail dù ngưỡng thực tế là 1.000 thay vì 5.000 · **C3b = GAP** nên không chấm dù bản dựng có lọc · không kết luận "không có nút" từ ảnh đối tác (sai vai trò + khác đơn vị) · không mở rộng case sang màn/vai trò/bộ lọc khác.

---

## 8. Bug mới / candidate

- **Candidate (1 dòng, KHÔNG kéo verdict QLDMTCTV_12):** ở lượt **Khôi phục** (Tạm dừng → Đang hoạt động), chuỗi lý do gửi lên là `KhoiPhuc07080353 - hoan nguyen sau do QLDMTCTV_12` nhưng dòng nhật ký `07/08/2026 03:53` ở tab "Lịch sử" hiện `Mo ta cong khai kiem thu re-verify QLDMTCTV_OOS_02 ngay 04/08/2026.` — là giá trị **trường mô tả công khai cũ**, không phải lý do vừa nhập (lượt Tạm dừng thì hiện **đúng**). Ngoài phạm vi 6 vế C1–C6 (cả 6 vế đo trên nhánh Tạm dừng) ⇒ ghi candidate, **không điều tra thêm**, **không** kéo verdict.
- **Ghi nhận (không phải bug, đối tác không nêu):** cột "Hành động" của tab Lịch sử ghi `Cập nhật` cho cả lượt Tạm dừng và lượt Khôi phục, trong khi `:1731` liệt kê bộ nhãn có riêng "Tạm dừng" / "Khôi phục". Chỉ ghi nhận.
- **Không có bug mới nào** thuộc 5 vế route TEST — cả 5 đều PASS.

---

## 9. Blocker

**Không có blocker.** Tiền đề dựng được bằng dữ liệu QA sẵn có; tài khoản `cbnv_tw_03` đăng nhập ngay lần đầu (không lock, không phải dùng dự phòng sibling); không gặp 5xx; không gặp lỗi mất ổn định sidebar (chỉ 1 lần bấm sidebar).

**Giới hạn hiệu lực của verdict:** đo trên **env nội bộ** `18.143.165.120.nip.io`, bó mã FE **`index-D4Buvu4S.js`** (deploy 02:23:01 VN 07/08), app **V1.0.9**. Đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản **V1.0.2**. Mọi PASS ở trên là **PASS cho đúng bó mã này**; tới khi bản dựng lên env đối tác thì phải đo lại.

---

## 10. Artifact

| File | Nội dung |
|---|---|
| [`../image/QLDMTCTV_12-do-chi-tiet.txt`](../image/QLDMTCTV_12-do-chi-tiet.txt) | Bảng đo từng vế: nguyên văn nhãn nút, nguyên văn lựa chọn, nguyên văn mọi thông báo, thuộc tính thật của ô Lý do, trạng thái bản ghi trước/sau, mốc giờ từng bước |
| [`../image/QLDMTCTV_12-C1-chi-tiet-co-nut.png`](../image/QLDMTCTV_12-C1-chi-tiet-co-nut.png) | C1 — màn chi tiết, thẻ "Thao tác" có nút `Cập nhật trạng thái`, badge `Đang hoạt động`, Số TVV liên kết 0, header `Cán bộ Nghiệp vụ Trung ương` |
| [`../image/QLDMTCTV_12-C2-C3-cua-so-trang-thai-moi.png`](../image/QLDMTCTV_12-C2-C3-cua-so-trang-thai-moi.png) | C2 + C3a/C3b — hộp thoại `Cập nhật trạng thái hoạt động`, danh sách chọn mở với đúng 2 lựa chọn `Tạm dừng` / `Vô hiệu hóa`, bộ đếm `0 / 1000` |
| [`../image/QLDMTCTV_12-C4-lydo-bat-buoc.png`](../image/QLDMTCTV_12-C4-lydo-bat-buoc.png) | C4 — đã chọn `Tạm dừng`, ô Lý do trống, nút `Đồng ý` mờ/vô hiệu hóa, badge sau hộp thoại vẫn `Đang hoạt động` |
| [`../image/QLDMTCTV_12-C5-bien-9-va-10.png`](../image/QLDMTCTV_12-C5-bien-9-va-10.png) | C5 phía bị chặn — `TamDung09`, bộ đếm `9 / 1000`, `Đồng ý` mờ |
| [`../image/QLDMTCTV_12-C5-bien-10-duoc-nhan.png`](../image/QLDMTCTV_12-C5-bien-10-duoc-nhan.png) | C5 phía được nhận — `TD07080351`, bộ đếm `10 / 1000`, `Đồng ý` xanh bấm được |
| [`../image/QLDMTCTV_12-C6-5001-ky-tu.png`](../image/QLDMTCTV_12-C6-5001-ky-tu.png) | C6 — cố nhập 5001 ký tự, bộ đếm dừng ở `1000 / 1000`, không thông báo |
| [`../image/QLDMTCTV_12-doi-chung-lich-su.png`](../image/QLDMTCTV_12-doi-chung-lich-su.png) | Đối chứng — badge `Tạm dừng`, tab Lịch sử có dòng `07/08/2026 03:51 · CB Nghiệp vụ - Trung ương #03 · Cập nhật · TD07080351` |
| [`../image/QLDMTCTV_12-hoan-nguyen-dang-hoat-dong.png`](../image/QLDMTCTV_12-hoan-nguyen-dang-hoat-dong.png) | Khôi phục — badge về `Đang hoạt động`, công tắc `Công khai` trở lại |
| [`../image/QLDMTCTV_12-cap-nhat-tam-dung-response.network-response`](../image/QLDMTCTV_12-cap-nhat-tam-dung-response.network-response) | Thân trả về của `POST cap-nhat-trang-thai` lượt Tạm dừng |
| [`../image/QLDMTCTV_12-hoan-nguyen-response.network-response`](../image/QLDMTCTV_12-hoan-nguyen-response.network-response) | Thân trả về của `POST cap-nhat-trang-thai` lượt Khôi phục |
