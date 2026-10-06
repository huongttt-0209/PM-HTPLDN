# QLDKTK_10 — Liên kết hợp lệ và doanh nghiệp đặt mật khẩu thành công (đo Giai đoạn B)

**Case:** QLDKTK_10 · dòng 169 · tab `bug`
**Chuẩn chấm đã khóa:** [`../chuan/QLDKTK_10.md`](../chuan/QLDKTK_10.md) — Giai đoạn B **không đổi** quan hệ MATCH/DIFF/GAP, **không mở rộng** phép đo, **không ghi Google Sheet**.
**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — mọi số dòng dẫn ở dưới đã **tự mở file đọc lại** trong lượt này (không bê từ chuẩn chấm, không lấy từ trí nhớ).
**Trạng thái đối tác:** Fail · Dopai N/R · TKM lần 1 "sau khi tc QLDKTK_01 được fix sẽ test" · Trạng thái dev fix: Fixed · **KHÔNG có ảnh bằng chứng đối tác** ⇒ mọi vế tự dựng, tự đo.

---

## 1. Điều kiện đo

| Hạng mục | Giá trị thực |
|---|---|
| **Env** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn`) |
| **Bó mã FE** | `assets/index-D4Buvu4S.js` · `assets/index-DVlgOkLg.css` — đọc trực tiếp từ DOM lúc 03:33 giờ VN. Khớp bản dựng **sau** lần deploy 02:23:01 ghi ở [`../BAN-DUNG.md`](../BAN-DUNG.md) |
| FE etag / last-modified | `W/"6a74df15-428"` · `Thu, 06 Aug 2026 19:23:01 GMT` (= 02:23:01 giờ VN 07/08) — đo bằng `curl` lúc 03:18:11 |
| Phiên bản app | sidebar hiện `HTPLDN · V1.0.9` |
| **Thời điểm đo** | 2026-08-07 giờ VN: 03:19:05 mở form đăng ký · 03:21:04 đăng ký #1 · 03:21:58 mở liên kết #1 · 03:24:39 đăng ký #2 · 03:25:24 mở liên kết #2 · 03:29 đọc đối chứng · 03:29:46 thử mật khẩu B · 03:31:16 đăng nhập được · 03:32 mở surface DN |
| MailHog | `http://18.143.165.120:8025` — lọc **đúng mailbox** của từng bản ghi, dùng `limit=15..20` (không `limit=1`, vì có phiên khác chạy song song) |
| **Tài khoản ra verdict** | **`9908070102` / `QaW5FormA@2026`** — tài khoản DN **QA tự dựng** qua luồng tự đăng ký. Không dùng bộ `_03` (case này không cần). |
| **Tài khoản chỉ để ĐỌC đối chứng** | **`admin` / `Secret@123`** — dùng **duy nhất** ở bước đọc lại `trangThai` (§4), trong **browser context riêng biệt** `adminreadonly` (cookie/localStorage tách hoàn toàn khỏi tab đo DN), **đăng xuất ngay sau khi đọc** (`POST /auth/logout` → 200). **Không dùng admin để ra verdict cho bất kỳ vế nào.** |
| Số tab dùng phiên | 2 (1 tab đo DN + 1 tab context riêng cho admin). Tab `about:blank` của profile `--isolated` không dùng phiên. |

### Ghi chú kỹ thuật lệch với BAN-DUNG.md

[`../BAN-DUNG.md`](../BAN-DUNG.md) ghi "ô nhập tên đăng nhập **mất** thuộc tính placeholder" trên bó mã này.
Đo lại trên `/login` của **cùng bó mã `index-D4Buvu4S.js`**: ô tên đăng nhập **có** `id="login-username"` **và có**
`placeholder="Nhập tên đăng nhập"`; ô mật khẩu có `id="login-password"` · `placeholder="Nhập mật khẩu"`.
Lượt này dùng `id` để chọn ô (bền hơn placeholder), nên không bị ảnh hưởng dù kết luận nào đúng.
Ghi lại để lô sau không đi theo giả định sai.

---

## 2. Dữ liệu QA đã tạo — khai đầy đủ (seed là mutate môi trường của người khác)

Cả 2 bản ghi là **dữ liệu QA mới**, tạo qua **luồng UI tự đăng ký** của chính app. **Không đụng dữ liệu đối tác.**
Cả 2 hiện còn trên env ở trạng thái `HOAT_DONG` (nếu cần dọn: username `9908070101`, `9908070102`).

| | Bản ghi #1 (lượt đo C1 lần 1 / spare) | **Bản ghi #2 (bản ghi CHÍNH của case)** |
|---|---|---|
| Env | `https://18.143.165.120.nip.io` | `https://18.143.165.120.nip.io` |
| Tên DN | QA W5 QLDKTK10 Cong ty TNHH Kiem Thu | QA W5 QLDKTK10 lan 2 Cong ty TNHH Kiem Thu |
| **Mã số thuế** (= tên đăng nhập) | **`9908070101`** | **`9908070102`** |
| **Email** | **`qa.w5.qldktk10.01@htpldn.test`** | **`qa.w5.qldktk10.02@htpldn.test`** |
| **Mật khẩu A** (nhập ở **form đăng ký**) | **`QaW5FormA@2026`** | **`QaW5FormA@2026`** |
| **Mật khẩu B** (dự định đặt ở **màn kích hoạt**) | **`QaW5LinkB@2026`** — **không đặt được** | **`QaW5LinkB@2026`** — **không đặt được** |
| Điện thoại DN | 0912345678 | 0912345679 |
| Tỉnh/TP · Loại DN | Hà Nội · Công ty trách nhiệm hữu hạn | Hà Nội · Công ty trách nhiệm hữu hạn |
| Ngành nghề · Quy mô | Thương mại và dịch vụ · Siêu nhỏ | Thương mại và dịch vụ · Siêu nhỏ |
| Người đại diện | Nguyen Van QA | Nguyen Van QA Hai |
| `id` TAI_KHOAN | `dcd3fb30-e5be-40cf-9b2e-48fb928cd8e1` | `0675c1d7-0bd9-4d39-af03-d07516d7071a` |
| `id` DOANH_NGHIEP | — (không đọc) | `b0d23c98-6978-4bd7-a9b7-c4c63be870f9` |

**Mã số thuế chọn bắt đầu `99` + email `qa.w5.qldktk10.*@htpldn.test`** để dễ nhận là dữ liệu QA. Cả 2 mã số thuế **đăng ký được ngay lần đầu** (`201`), không gặp báo trùng ⇒ chưa tồn tại trong hệ thống, **không phải brute force**.

**Vì sao có 2 bản ghi:** liên kết kích hoạt **chỉ dùng được một lần** (đã tự kiểm, xem §3 C1). Lượt #1 tiêu token trước khi kịp chụp màn kích hoạt — màn đó chỉ hiện **~3 giây** rồi app tự chuyển `/login`. Bản ghi #2 dựng riêng để chụp đúng màn đó. Hai lượt cho **cùng một kết luận**.

**13 trường bắt buộc** (theo chuẩn chấm §3.2) đã điền đủ ở cả 2 lượt; `linh_vuc_ids` bỏ trống (không bắt buộc) để giảm biến số. Ô **"Tên đăng nhập"** (disabled, placeholder "Tự động theo Mã số thuế") **tự hiện đúng mã số thuế** — khớp `srs-fr-10-quan-tri.md:1080` ("Set username = ma_so_thue (auto-derived...)"). 5 dòng quy tắc mật khẩu dưới ô Mật khẩu **đều tick ✓** (Ít nhất 8 ký tự / Chữ hoa / Chữ thường / Chữ số / Ký tự đặc biệt).

---

## 3. Bảng kết quả theo từng vế

| Vế | Quan hệ (đã khóa) | Số đo / chuỗi thật quan sát được | Kết quả | Artifact |
|---|---|---|---|---|
| **C1a** — mở liên kết kích hoạt hợp lệ thì vào được, **không lỗi** | **MATCH (đường chính) → TEST** | `GET /auth/verify-email?token=...` → **200**; `POST /api/v1/auth/verify-email` → **200**; **không** toast lỗi, **không** 4xx/5xx trong bước này, **không** bị đẩy về `/login` như một lỗi (chuyển `/login` là bước cuối có chủ đích của app kèm câu "Đang chuyển đến trang đăng nhập..."). Chuỗi thật: `Đang kích hoạt tài khoản...` (+362 ms) → `Kích hoạt thành công! / Tài khoản của bạn đã được kích hoạt. Đang chuyển đến trang đăng nhập...` (+483 ms) | ✅ **PASS** | `QLDKTK_10-C1-man-kich-hoat.png` · `QLDKTK_10-timeline.txt` |
| **C1b** — trên màn đó phải có **bước đặt mật khẩu** | **GAP có điều kiện → BA** *(trigger §4.1 chuẩn chấm ĐÃ NỔ)* | **KHÔNG có màn đặt mật khẩu.** Số ô `input[type=password]` trên màn kích hoạt = **0** ở **mọi mẫu** của cả 2 lượt. Không nút lưu mật khẩu. `POST /api/v1/auth/verify-email` gửi lên **chỉ** `{"token":"..."}` — không có field mật khẩu nào | — *(cấm chấm Pass/Fail; chuyển BA — xem §5)* | `QLDKTK_10-C1-man-kich-hoat.png` · `QLDKTK_10-C2-verify-email-response.network-response` |
| **C2** — tài khoản **chuyển sang trạng thái hoạt động** | **MATCH → TEST** | Sau đăng ký: `"trangThai":"CHO_KICH_HOAT"`. Sau khi mở liên kết: phản hồi `"trangThai":"HOAT_DONG"` + **đọc lại bản ghi độc lập** cho **cả 2** bản ghi → `"trangThai": "HOAT_DONG"`, `"vaiTros":[{"maVaiTro":"DN"}]`, **`"lanDangNhapCuoi": null`** (đổi trạng thái xảy ra **trước** mọi lần đăng nhập) | ✅ **PASS** | `QLDKTK_10-doi-chung-trangthai.txt` · `QLDKTK_10-doi-chung-raw.json` · `QLDKTK_10-C2-sau-dat-mat-khau.png` |
| **C3** — DN **đăng nhập được bằng mã số thuế + mật khẩu** | **MATCH → TEST** | `9908070102` + **mật khẩu A** → `POST /auth/login` **200** → bước mã xác thực 6 số (`Mã 6 chữ số đã gửi đến email qa.***@htpldn.test`, `Hiệu lực 4:35`) → OTP `833015` ở MailHog → `POST /auth/verify-otp` **200** · `GET /auth/me` **200**. URL sau đăng nhập **`/dao-tao/chuong-trinh/danh-sach`** (KHÔNG còn ở `/login`). Phiên: `vaiTro:["DN"]` · `authMethod:"LOCAL"` · `doanhNghiepId:"b0d23c98-..."`. Header hiện "Nguyen Van QA Hai · Doanh nghiệp" | ✅ **PASS** | `QLDKTK_10-C3-dang-nhap-bang-MST.png` · `QLDKTK_10-C3-auth-me.network-response` |
| **C4** — "và sử dụng đầy đủ chức năng" | **GAP → BA** | Đo **tối thiểu, đúng một lần**: bấm sidebar "Doanh nghiệp" → app tự tới **`/doanh-nghiep/me/sua`**, hiện "Hồ sơ doanh nghiệp — QA W5 QLDKTK10 lan 2 Cong ty TNHH Kiem Thu · MST: 9908070102" với 4 nhóm (Thông tin liên hệ / Người đại diện / Lao động & tài chính / Lĩnh vực kinh doanh), dữ liệu **đúng của chính DN mình**. `GET /api/v1/doanh-nghieps/me` → **200**. **Không 403, không trang trắng.** | — *(cấm chấm Pass/Fail; chỉ ghi hiện trạng)* | `QLDKTK_10-C4-surface-DN.png` |

**Tổng: 3/3 vế route TEST đều PASS (C1a · C2 · C3). 2 vế route BA (C1b · C4) chỉ ghi hiện trạng, không chấm.**

### Đếm request kèm thông báo (chống double-submit che lỗi)

| Thao tác | Số request thật | Thông báo bắt được (observer **không lọc trùng**, dùng `innerText`) |
|---|---|---|
| Bấm [Đăng ký] | **đúng 1** `POST /auth/register-doanh-nghiep` → 201 | 1 khối `.ant-message-notice-wrapper`: `Đăng ký thành công, vui lòng kiểm tra email kích hoạt` |
| Mở liên kết kích hoạt | **đúng 1** `POST /auth/verify-email` → 200 | không có toast; câu trên thân màn: `Kích hoạt thành công! ...` |
| Đăng nhập bằng mật khẩu B | **đúng 1** `POST /auth/login` → 401 | 1 khối `.ant-notification-notice-wrapper`: `Tên đăng nhập hoặc mật khẩu không đúng.` |
| Đăng nhập bằng mật khẩu A | **đúng 1** `POST /auth/login` → 200, **đúng 1** `POST /auth/verify-otp` → 200 | không toast lỗi |

**Toàn bộ 4xx/5xx gặp trong lượt đo:** `GET /auth/me` → 401 khi **chưa** đăng nhập (hành vi bình thường của app) và `POST /auth/login` → 401 **đúng 1 lần do QA chủ động thử mật khẩu B** (là phép thử của case). **Không có 5xx.** Không có 4xx ngoài dự kiến trong các bước bắt buộc của C1→C4 ⇒ không có bug candidate loại "workaround 4xx/5xx".

---

## 4. KẾT QUẢ PHÉP THỬ 2 MẬT KHẨU (dữ kiện quyết định)

Hai mật khẩu **khác nhau**, cả hai đều hợp lệ theo quy tắc SRS (≥8 ký tự, có chữ hoa + chữ thường + số + ký tự đặc biệt):

- **Mật khẩu A = `QaW5FormA@2026`** — nhập ở **form đăng ký** (SCR-VIII-08).
- **Mật khẩu B = `QaW5LinkB@2026`** — **dự định** đặt ở **màn kích hoạt**.

| Bước của phép thử | Kết quả đo |
|---|---|
| Đặt được mật khẩu B ở màn kích hoạt? | **KHÔNG.** Màn kích hoạt không có ô nhập mật khẩu (0 ô `input[type=password]` ở mọi mẫu, cả 2 lượt), không có nút lưu, và request lên máy chủ chỉ gửi `{"token":"..."}`. Mật khẩu B **không bao giờ tồn tại** trong hệ thống. |
| Đăng nhập bằng **mã số thuế + mật khẩu B** | ❌ `POST /auth/login` → **401** · thông báo thật `Tên đăng nhập hoặc mật khẩu không đúng.` · vẫn ở `/login` |
| Đăng nhập bằng **mã số thuế + mật khẩu A** | ✅ `POST /auth/login` → **200** → bước mã xác thực → `verify-otp` **200** → vào `/dao-tao/chuong-trinh/danh-sach` |

> ### ⇒ **Đăng nhập được bằng MẬT KHẨU A — mật khẩu đặt ở FORM ĐĂNG KÝ. Không phải mật khẩu B.**

**Nghĩa của dữ kiện này:** bản dựng đang chạy **đường A** của FR-VIII-22 — `srs-fr-10-quan-tri.md:1070` + `:1071` (Inputs #25 `mat_khau` bắt buộc + #26 `mat_khau_xac_nhan`), `:1081` ("Kiểm tra mật khẩu đủ độ mạnh + khớp xác nhận"), `:1083` ("Mã hóa mật khẩu (hash 1 chiều)"). Đúng như dự đoán trong chuẩn chấm, liên kết trong thư chỉ còn nhiệm vụ **xác thực email + chuyển `CHO_KICH_HOAT → HOAT_DONG`**, nên **bước 2 của phiếu UAT ("Doanh nghiệp đặt mật khẩu thành công") không tồn tại để đo trên bản dựng này**.

**Đối chiếu 3 điểm ràng buộc ở phía máy chủ** (chỉ để xác nhận cùng một kết luận, không dùng làm verdict): mô tả API công khai của env cho thấy bước đăng ký DN **bắt buộc** có `password` + `passwordConfirm`, còn bước xác thực email **chỉ nhận** `token`.

**Vì sao KHÔNG chấm FAIL cho vế này:** SRS **tự mâu thuẫn trong cùng một FR** — bên cạnh đường A ở trên, chính FR-VIII-22 lại nói đường B:
- `srs-fr-10-quan-tri.md:1109` — "DN bấm link kích hoạt **+ đặt mật khẩu lần đầu** (qua FR-VIII-XX Quên mật khẩu / Kích hoạt) → TAI_KHOAN chuyển HOAT_DONG → DN có thể đăng nhập + dùng đầy đủ chức năng..."
- `srs-fr-10-quan-tri.md:1116` — "**Given** DN bấm link kích hoạt **+ đặt mật khẩu** **When** lưu thành công **Then** TAI_KHOAN chuyển HOAT_DONG, DN đăng nhập bằng MST + mật khẩu"
- `srs-fr-10-quan-tri.md:2299` — "| CHO_KICH_HOAT | HOAT_DONG | User kích hoạt qua email **+ đặt mật khẩu lần đầu** | Token hợp lệ + MK đủ độ mạnh | Cho phép đăng nhập | FR-VIII-15, FR-VIII-22, FR-VIII-26 |"
- `srs-fr-10-quan-tri.md:1325` (FR-VIII-26 bước 13) + `:1327` (bước 15 — "Đặt mật khẩu thành công, vui lòng đăng nhập")

Hai đường **loại trừ nhau**, và dev đang đúng **một trong hai đường của chính SRS**. Đúng caveat chống-FAIL-oan của chuẩn chấm ⇒ **route BA, không chấm FAIL** (xem §5 Q1).

**Về đối chứng độc lập cho C2:** đã **không** chỉ tin câu thông báo trên màn. Đọc lại bản ghi bằng `GET /api/v1/tai-khoan?...&search=<MST>` (`credentials:'include'`) và **giá trị enum thật đọc được là `HOAT_DONG`** (ghi nguyên trạng, không dịch). `lanDangNhapCuoi: null` chứng minh trạng thái đã đổi **trước** mọi lần đăng nhập ⇒ chính bước kích hoạt làm việc đó. Chi tiết + khai rõ việc dùng `admin` để đọc: `QLDKTK_10-doi-chung-trangthai.txt`.

**Về nhãn trạng thái:** phiếu UAT viết "Đang hoạt động"; hệ thống dùng enum `HOAT_DONG` và nhãn tài khoản là "Hoạt động" (`srs-fr-10-quan-tri.md:2290` "| HOAT_DONG | active | Tài khoản đang hoạt động bình thường |", enum ở `:2106`). **Không chấm Fail vì lệch nhãn** — điều cần đúng là tài khoản đã ở trạng thái dùng được, và C3 đã chứng minh dùng được thật.

---

## 5. Hiện trạng 2 vế route BA (ghi nhận, không chấm)

### C1b — bản dựng không có bước đặt mật khẩu ở màn kích hoạt

Chuỗi thật trên màn kích hoạt (`innerText` phần tử đang hiển thị, **không** dùng `textContent`):

```
Đang kích hoạt tài khoản...
```
```
Kích hoạt thành công!
Tài khoản của bạn đã được kích hoạt. Đang chuyển đến trang đăng nhập...
```

Sau đó app tự chuyển `/login` (hẹn giờ thật của app: **3000 ms**). Không có ô mật khẩu ở bất kỳ mẫu nào.

**Kèm dữ kiện phụ về tính 1-lần-dùng:** mở **lại chính** liên kết #1 lần thứ hai → màn hiện (và **đứng yên**, không tự chuyển):

```
Link không hợp lệ
Link có thể đã được sử dụng trước đó hoặc không hợp lệ.
Nếu tài khoản của bạn đã được kích hoạt, vui lòng đăng nhập.
Nếu chưa, vui lòng kiểm tra lại email hoặc liên hệ quản trị viên.
```

Khớp câu trong thư ("chỉ dùng được một lần") và khớp `srs-fr-10-quan-tri.md:1088` ("link vĩnh viễn, 1 lần dùng"). **Không gặp** báo hết hạn trên DN vừa dựng ⇒ không chạm mâu thuẫn "vĩnh viễn vs 7 ngày" (`:1088` · `:1317` vs `:2306`) trong lượt này.

**Nội dung thư kích hoạt** (thân thư có **đúng 1 liên kết**, không phải chọn giữa nhiều link):

```
Xin chào Nguyen Van QA Hai,
Doanh nghiệp "QA W5 QLDKTK10 lan 2 Cong ty TNHH Kiem Thu" đã được đăng ký thành công.
Tên đăng nhập của bạn là mã số thuế: 9908070102
Link kích hoạt: http://18.143.165.120.nip.io/auth/verify-email?token=0b57c2ca-4025-494a-a015-625bfd88c400
Link kích hoạt có hiệu lực vĩnh viễn và chỉ dùng được một lần.
Vui lòng kích hoạt sớm để tránh tài khoản bị thu hồi sau 7 ngày không hoạt động.
```

> Thư gửi qua MailHog — env **chưa tích hợp email thật**, đây là giả lập. **Không** log bug loại "không nhận được email".

### C4 — hiện trạng surface vai trò DN

- Menu bên trái của phiên DN **chỉ có 3 mục**: "Đào tạo, tập huấn" (3 mục con: Chương trình đào tạo / Khóa học / Kho tài liệu-Bài giảng) · "Vụ việc HTPL" · "Doanh nghiệp". **Không có menu quản trị của cán bộ.** Việc DN không thấy màn quản trị là **đúng** `srs-fr-01-dashboard.md:685` ("**Vai trò KHÔNG có quyền:** Doanh nghiệp (sử dụng Cổng DN riêng — Nhóm VII)...") ⇒ **không phải lỗi**.
- Surface hồ sơ DN **mở được bằng phiên đăng nhập mã số thuế + mật khẩu**, render đủ dữ liệu của chính DN mình, `GET /doanh-nghieps/me` → 200, **không 403, không trắng**.
- **Khác biệt ghi nhận (không chấm):** đường dẫn thật của surface là **`/doanh-nghiep/me/sua`**, còn SRS đặc tả `srs-fr-07-doanh-nghiep.md:513` **URL:** `/doanh-nghiep/ho-so-cua-toi`; và `:514` ghi **Quyền truy cập: Doanh nghiệp (Tier 2 VNeID)** trong khi phiên đo là mã số thuế + mật khẩu (`authMethod: "LOCAL"`, env nội bộ không có VNeID). Đây đúng là phần **GAP** đã khóa ⇒ **không** chấm, **không** log bug, chuyển BA (Q2).
- **Dừng đúng ở đây.** Không mở ma trận quyền, không quét toàn menu, không thử các chức năng khác — theo luật khóa của chuẩn chấm.

### Câu hỏi BA (giữ nguyên như chuẩn chấm §5, nay đã có số đo kèm)

- **Q1 (ảnh hưởng C1b, C2):** luồng DN tự đăng ký, mật khẩu được đặt ở bước nào — form đăng ký (`:1070`-`:1071`, `:1081`, `:1083`) hay màn kích hoạt (`:1109`, `:1116`, `:2299`, `:1325`)? Và khi DN mở liên kết kích hoạt hợp lệ thì hệ thống phải hiển thị màn gì? **Số đo kèm:** bản dựng chạy đường form đăng ký; đăng nhập được bằng mật khẩu đặt lúc đăng ký; màn kích hoạt chỉ xác nhận rồi chuyển `/login`; tài khoản vẫn sang `HOAT_DONG` và đăng nhập được bằng mã số thuế.
- **Q2 (ảnh hưởng C4):** vai trò DN sau khi tài khoản hoạt động được dùng những chức năng nào, trên giao diện nào? (a) danh sách chức năng/màn hình; (b) phiên mã số thuế + mật khẩu có được vào các màn đó, hay bắt buộc qua VNeID Tier 2 (`srs-fr-07-doanh-nghiep.md:514`); (c) BR-AUTH-11 còn hiệu lực hay đã bị FR-VIII-22 thay thế. **Số đo kèm:** phiên mã số thuế + mật khẩu vào được hồ sơ DN của chính mình tại `/doanh-nghiep/me/sua` (không phải URL `:513`), không 403; DN không thấy màn quản trị (đúng `:685`).
- **Q3 (housekeeping):** liên kết kích hoạt vĩnh viễn (`:1088`, `:1317`) hay tài khoản tự vô hiệu hóa sau 7 ngày (`:2306`)? **Số đo kèm:** thư ghi **cả hai** ý trong cùng một thư ("hiệu lực vĩnh viễn" + "bị thu hồi sau 7 ngày không hoạt động") ⇒ mâu thuẫn của SRS đã lan vào nội dung thư gửi cho doanh nghiệp.

---

## 6. Bug mới / candidate

- **Không log bug mới.** Toàn bộ 3 vế route TEST đều PASS; phần lệch với phiếu UAT (không có bước đặt mật khẩu ở màn kích hoạt) truy được về **SRS tự mâu thuẫn trong cùng FR-VIII-22** ⇒ theo luật FLOW 04 phải BA confirm, **không** tự chấm Fail và cũng **không** tự chấm "không phải lỗi".
- **Candidate (1 dòng, không mở rộng điều tra):** surface hồ sơ DN chạy ở `/doanh-nghiep/me/sua` trong khi `srs-fr-07-doanh-nghiep.md:513` đặc tả `/doanh-nghiep/ho-so-cua-toi` và `:514` gate ở Tier 2 VNeID — nằm trọn trong vế C4 đã khóa route BA, chờ Q2 chốt rồi mới xử.
- **Candidate (1 dòng):** thư kích hoạt gửi cho doanh nghiệp ghi đồng thời "hiệu lực vĩnh viễn" và "thu hồi sau 7 ngày không hoạt động" — cùng gốc mâu thuẫn SRS ở Q3, chờ BA chốt.
- **Không có blocker.** Tiền đề dựng được trọn vẹn; không phải kết luận "Chưa chốt".

---

## 7. Đề xuất verdict logic

**⚠️ Cần BA xác nhận** — bước 2 của phiếu ("Doanh nghiệp đặt mật khẩu thành công") **không tồn tại trên bản dựng** vì dev đang chạy đường "đặt mật khẩu ngay ở form đăng ký" của chính FR-VIII-22, còn kết quả cuối mà phiếu yêu cầu thì **đã đạt** (tài khoản sang `HOAT_DONG` — đọc lại bản ghi xác nhận; đăng nhập được bằng mã số thuế + mật khẩu; vào được hồ sơ DN, không 403). SRS mâu thuẫn nội bộ nên **không được** tự chấm Fail cũng **không được** tự chấm "không phải lỗi".

---

## 8. Artifact

| File | Nội dung |
|---|---|
| `../image/QLDKTK_10-C1-man-kich-hoat.png` | Màn kích hoạt: "Kích hoạt thành công! / Tài khoản của bạn đã được kích hoạt. Đang chuyển đến trang đăng nhập..." — **không có ô mật khẩu** |
| `../image/QLDKTK_10-C2-sau-dat-mat-khau.png` | Trạng thái ngay sau khi kích hoạt: app đã ở `/login` (bước "đặt mật khẩu" không tồn tại nên ảnh này là mốc kế tiếp thật của luồng) |
| `../image/QLDKTK_10-C2-verify-email-response.network-response` | Phản hồi thật của bước kích hoạt: `{"message":"Tài khoản đã được kích hoạt. Vui lòng đăng nhập để tiếp tục.","trangThai":"HOAT_DONG"}` |
| `../image/QLDKTK_10-C3-dang-nhap-bang-MST.png` | Sau khi đăng nhập bằng mã số thuế + mật khẩu A: `/dao-tao/chuong-trinh/danh-sach`, header "Nguyen Van QA Hai · Doanh nghiệp" |
| `../image/QLDKTK_10-C3-auth-me.network-response` | Phiên DN: `vaiTro:["DN"]` · `authMethod:"LOCAL"` · `doanhNghiepId` · danh sách quyền |
| `../image/QLDKTK_10-C4-surface-DN.png` | Surface DN `/doanh-nghiep/me/sua` — hồ sơ của chính DN, MST 9908070102, không 403/trắng |
| `../image/QLDKTK_10-C0-form-dang-ky.png` | Form đăng ký đã điền đủ 13 trường (bản ghi #1) — có ô Mật khẩu + Xác nhận mật khẩu, ô Tên đăng nhập tự hiện mã số thuế |
| `../image/QLDKTK_10-timeline.txt` | Mọi mốc thời gian, dữ liệu QA đã tạo, **liên kết kích hoạt thật** của cả 2 bản ghi, thống kê 4xx/5xx, **khai rõ kỹ thuật chụp có can thiệp** |
| `../image/QLDKTK_10-doi-chung-trangthai.txt` | Đối chứng `trangThai` — cách đọc, enum thật, **khai rõ dùng `admin` chỉ để đọc** |
| `../image/QLDKTK_10-doi-chung-raw.json` | JSON đầy đủ chưa cắt của lượt đọc đối chứng |
