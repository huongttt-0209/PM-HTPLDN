# QLDKTK_10 — Chuẩn chấm (Giai đoạn A, FLOW 04)

**Case:** dòng 169 tab `bug` — "Liên kết hợp lệ và doanh nghiệp đặt mật khẩu thành công"
**Ngày chốt chuẩn:** 2026-08-07
**Nguồn chuẩn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Trạng thái đối tác:** Fail · Dopai N/R · TKM lần 1 "sau khi tc QLDKTK_01 được fix sẽ test" · Trạng thái dev fix: Fixed · **KHÔNG có ảnh bằng chứng**
**FR sở hữu case:** FR-VIII-22 (Đăng ký TK doanh nghiệp — self-registration, UC120) + FR-VIII-26 (Quên mật khẩu / Kích hoạt tài khoản lần đầu) + FR-VIII-20 (Đăng nhập, UC118)

> ⚠️ Case KHÔNG có ảnh đối tác. Mọi vế phải tự dựng + tự đo. Không suy verdict từ ô "Fixed" của dev.

---

## 1. Bảng dòng khóa Cn

| Vế | Expected đối tác (nguyên văn cắt vế) | SRS `file:LINE` | Quan hệ | Route | Đường đo (UI ngắn nhất + đối chứng độc lập) |
|---|---|---|---|---|---|
| **C1** | "Mở thư và bấm liên kết kích hoạt" → vào được màn đặt mật khẩu, không lỗi | `srs-fr-10-quan-tri.md:1109` · `:1116` · `:2299` (đường chính) — **tự mâu thuẫn** với `:1070`+`:1071`+`:1081`+`:1083` (Inputs 25/26 buộc DN đặt MK ngay ở form đăng ký) | **MATCH** (đường chính) · **GAP có điều kiện** nếu dev theo vế Inputs | **TEST** · chuyển **BA** khi trigger ở §4.1 nổ | UI: MailHog → mở mail kích hoạt → bấm link → màn đặt MK render, không 4xx/5xx. Đối chứng: `list_network_requests` — request mở link trả 2xx và **KHÔNG** kèm toast lỗi/redirect `/login` |
| **C2** | "Tài khoản chuyển sang trạng thái \"Đang hoạt động\"" | `srs-fr-10-quan-tri.md:1109` · `:1116` · `:1325` · `:2299` · `:2106` (enum) · `:2290` (nhãn) | **MATCH** | **TEST** | UI: đặt MK mới hợp lệ → submit → thông báo thành công + redirect `/login` (`:1327`). Đối chứng độc lập: login `qtht_01` → SCR-VIII-03 Quản lý Tài khoản, lọc trạng thái = HOAT_DONG, tìm username = MST vừa dựng → có mặt (hoặc GET `/api/v1/tai-khoan` đọc `trang_thai`) |
| **C3** | "doanh nghiệp đăng nhập được bằng mã số thuế + mật khẩu" | `srs-fr-10-quan-tri.md:1116` · `:1080` · `:2100` · `:1232` (MST+MK vẫn dùng được sau đồng bộ VNeID) · `:1176` | **MATCH** | **TEST** | UI: `/login` → username = MST (10 số) + MK vừa đặt → bước OTP (`:1886` ô 6 số) lấy từ MailHog → vào được, không còn ở `/login`. Đối chứng: `list_network_requests` `POST /api/v1/auth/login` trả 2xx + phiên có `vai_tro[]` chứa DN (`:950`) |
| **C4** | "và sử dụng đầy đủ chức năng" | Không nơi nào định nghĩa **tập chức năng** của vai trò DN. Câu duy nhất gần nhất `srs-fr-10-quan-tri.md:1109` chỉ phủ định **1 điều kiện** (VNeID) chứ không liệt kê chức năng. Đối lập: `srs-v3.5.md:1380` · `srs-v3.5.md:5535` (BR-AUTH-11, **🟡 chờ CĐT** `:5537`) · `srs-fr-01-dashboard.md:685`. Surface DN duy nhất được đặc tả: `srs-fr-07-doanh-nghiep.md:508-514` (SCR-V.III-04) nhưng gate "Tier 2 VNeID" | **MÂU THUẪN → GAP** | **BA** | **Khóa ở mức đo được tối thiểu:** sau C3, DN vào được **một** surface vai trò DN (`/doanh-nghiep/ho-so-cua-toi` — SCR-V.III-04, `srs-fr-07-doanh-nghiep.md:513`) và **không** bị 403 / trang trắng. Đối chứng: `list_network_requests` API của trang trả 2xx, không 401/403. **CẤM mở rộng** thành CRUD matrix, CẤM quét toàn menu, CẤM test 5 tab đủ dữ liệu (luật khóa 3+4 Flow 04) |

**Tổng:** C1 TEST (kèm nhánh BA) · C2 TEST · C3 TEST · C4 BA (đo tối thiểu để ghi hiện trạng, KHÔNG chấm Pass/Fail cho vế "đầy đủ chức năng").

---

## 2. Trích nguyên văn SRS đã dẫn

### 2.1 Kích hoạt + chuyển trạng thái + đăng nhập MST (đường chính C1/C2/C3)

`srs-fr-10-quan-tri.md:1108-1109` (FR-VIII-22 Postconditions)
```
- Mail link kích hoạt đã gửi cho DN
- DN bấm link kích hoạt + đặt mật khẩu lần đầu (qua FR-VIII-XX Quên mật khẩu / Kích hoạt) → TAI_KHOAN chuyển HOAT_DONG → DN có thể đăng nhập + dùng đầy đủ chức năng (không hạn chế dù chưa đồng bộ VNeID Tổ chức)
```

`srs-fr-10-quan-tri.md:1116` (FR-VIII-22 Acceptance Criteria)
```
- **Given** DN bấm link kích hoạt + đặt mật khẩu **When** lưu thành công **Then** TAI_KHOAN chuyển HOAT_DONG, DN đăng nhập bằng MST + mật khẩu
```

`srs-fr-10-quan-tri.md:2299` (SM-TAIKHOAN — bảng chuyển trạng thái)
```
| CHO_KICH_HOAT | HOAT_DONG | User kích hoạt qua email + đặt mật khẩu lần đầu | Token hợp lệ + MK đủ độ mạnh | Cho phép đăng nhập | FR-VIII-15, FR-VIII-22, FR-VIII-26 | — |
```

`srs-fr-10-quan-tri.md:1325` (FR-VIII-26 Processing bước 13)
```
| 13 | **Chuyển trạng thái tài khoản:** Nếu TK đang CHO_KICH_HOAT → chuyển HOAT_DONG (vai trò luôn được gán sẵn khi tạo TK — BA chốt 2026-05-07 Q3 bỏ CHO_PHAN_QUYEN, mọi luồng tạo TK đều gán role trước); Nếu TK đang HOAT_DONG → giữ nguyên (chỉ cập nhật mật khẩu) | SM-TAIKHOAN |
```

`srs-fr-10-quan-tri.md:1327` (FR-VIII-26 Processing bước 15)
```
| 15 | Hiển thị thông báo "Đặt mật khẩu thành công, vui lòng đăng nhập" → redirect SCR đăng nhập | — |
```

`srs-fr-10-quan-tri.md:1080` (FR-VIII-22 Processing bước 3 — username = MST)
```
| 3 | Set username = ma_so_thue (auto-derived, không cần kiểm tra unique riêng vì đã đảm bảo từ bước 1) | BR-AUTH-USERNAME-01 |
```

`srs-fr-10-quan-tri.md:2100` (entity TAI_KHOAN.username)
```
| username | text | Y | UNIQUE, CHECK REGEXP `^[a-z0-9_]{4,50}$` | | Tên đăng nhập. Quy ước sinh theo BR-AUTH-USERNAME-01: (a) DN tự đăng ký auto = `ma_so_thue` (10 chữ số); …
```

`srs-fr-10-quan-tri.md:1232` (FR-VIII-25 — MST+MK vẫn hợp lệ, không bị VNeID thay thế)
```
… Sau đồng bộ, user có thêm cách đăng nhập bằng VNeID (vẫn dùng được tên đăng nhập + mật khẩu, không bắt buộc bỏ). …
```

`srs-fr-10-quan-tri.md:1176` (FR-VIII-23 Postconditions)
```
- KHÔNG tự tạo TK mới qua VNeID lần đầu — DN phải đăng ký qua FR-VIII-22, các vai trò khác phải có TK do quy trình tương ứng cấp
```

### 2.2 Enum + nhãn trạng thái tài khoản (C2 — chống chấm sai vì câu chữ)

`srs-fr-10-quan-tri.md:2106` (entity TAI_KHOAN.trang_thai)
```
| trang_thai | text | Y | CHECK IN ('CHO_KICH_HOAT','HOAT_DONG','TAM_KHOA','VO_HIEU_HOA') | 'CHO_KICH_HOAT' | Trạng thái TK (SM-TAIKHOAN: 4 states — BA chốt 2026-05-07 Q3 bỏ CHO_PHAN_QUYEN) |
```

`srs-fr-10-quan-tri.md:2289-2290` (bảng trạng thái SM-TAIKHOAN)
```
| CHO_KICH_HOAT | pending | Tài khoản mới tạo, chưa kích hoạt (vai trò đã gán sẵn) |
| HOAT_DONG | active | Tài khoản đang hoạt động bình thường |
```

`srs-fr-10-quan-tri.md:1713` + `:1720` (SCR-VIII-03 — nhãn tiếng Việt thực tế của SRS)
```
| 8 | content | Tab | tab | Tất cả / Hoạt động / Chờ kích hoạt / Tạm khóa (số đếm) | click → filter | luôn hiển thị |
| 15 | content | Cột Trạng thái | badge | HOAT_DONG (xanh) / CHO_KICH_HOAT (vàng) / TAM_KHOA (đỏ) / VO_HIEU_HOA (đen) | — | luôn hiển thị |
```
> **SRS dùng nhãn "Hoạt động"** cho TAI_KHOAN, KHÔNG dùng "Đang hoạt động" (đó là nhãn của SM-TVV / SM-NHT). Expected đối tác viết "Đang hoạt động" là cách nói, không phải yêu cầu câu chữ.

### 2.3 Quy tắc mật khẩu (C1/C2)

`srs-fr-10-quan-tri.md:1070-1071` (FR-VIII-22 Inputs 25-26)
```
| 25 | mat_khau | text | Y | Ít nhất 8 ký tự, gồm chữ hoa + chữ thường + số + ký tự đặc biệt | — | user input |
| 26 | mat_khau_xac_nhan | text | Y | Phải khớp mat_khau | — | user input |
```

`srs-fr-10-quan-tri.md:1301-1302` (FR-VIII-26 Inputs 3-4 — màn đặt MK qua link)
```
| 3 | mat_khau_moi | text | Y | Ít nhất 8 ký tự, gồm chữ hoa + chữ thường + số + ký tự đặc biệt | — | user input (form đặt mật khẩu) |
| 4 | mat_khau_xac_nhan | text | Y | Phải khớp mat_khau_moi | — | user input |
```
> Hai nơi **cùng một ràng buộc** ≥8 ký tự + hoa + thường + số + ký tự đặc biệt. Mã lỗi: `ERR-PWD-05` MK yếu (`:1339`), `ERR-PWD-06` xác nhận không khớp (`:1340`).

### 2.4 Hạn hiệu lực liên kết kích hoạt — **SRS TỰ MÂU THUẪN**

`srs-fr-10-quan-tri.md:1088` (FR-VIII-22 Processing bước 10) — **vĩnh viễn**
```
| 10 | Gửi mail link kích hoạt cho DN (link vĩnh viễn, 1 lần dùng) — gửi đến TAI_KHOAN.email | — |
```

`srs-fr-10-quan-tri.md:1317` (FR-VIII-26 Processing bước 5) — **vĩnh viễn khi CHO_KICH_HOAT**
```
| 5 | Sinh token reset (chuỗi ngẫu nhiên), lưu vào `token_reset_mk` + `token_het_han` của TAI_KHOAN. Hạn token: **vĩnh viễn** nếu TK ở CHO_KICH_HOAT (gồm TK mới tạo ở Claim Flow + TK kích hoạt lần đầu TVV/NHT); **30 phút** nếu TK đang HOAT_DONG (reset password thường) | — |
```

`srs-fr-10-quan-tri.md:2306` **VÀ** `srs-v3.5.md:6397` (SM-TAIKHOAN) — **hết hạn sau 7 ngày**
```
| CHO_KICH_HOAT | VO_HIEU_HOA | Auto: quá 7 ngày | activation_token_expired | Ghi audit, TB QTHT | — | — |
```
> **Mâu thuẫn thật, xuất hiện ở 2 file.** Không chặn case này (DN dựng mới, link dùng ngay trong phiên) nhưng phải hỏi BA — xem §5 Q3.

### 2.5 Tập chức năng vai trò DN — **SRS MÂU THUẪN, không có danh sách** (C4)

`srs-v3.5.md:1296` (đầu Permission Matrix — cảnh báo tự thân của SRS)
```
> **Bảng này là quyền ở MỨC DỮ LIỆU, không phải quyền chạy chức năng** `[làm rõ 2026-08-06]`. Một ô có `R` chỉ nói vai trò đó **được đọc dữ liệu** của thực thể; nó **không** đồng nghĩa vai trò đó là **tác nhân** của các chức năng thao tác trên thực thể ấy. …
```

`srs-v3.5.md:1380` (footnote † của Permission Matrix)
```
> † DN không truy cập CMS trực tiếp. Quyền Create/Read của DN thực hiện qua API inbound từ Cổng PLQG (SI-04, Nhóm XII). Permission Matrix ghi nhận quyền LOGIC, không phải quyền CMS UI.
```

`srs-v3.5.md:5535` (BR-AUTH-11) + `srs-v3.5.md:5537` (status)
```
| BR-AUTH-11 | **Lọc API cho DN (chuyên trang Cổng PLQG):** DN KHÔNG đăng nhập CMS → không có phiên phân quyền dữ liệu. DN tương tác qua API chuyên trang. …
**Trạng thái BR-AUTH-10 → BR-AUTH-11:** 🟡 Đề xuất — chờ CĐT xác nhận
```
> BR-AUTH-11 **chưa được CĐT chốt** → yếu hơn FR-VIII-22 (Priority Essential, AC đã chốt). Vì vậy C3 vẫn TEST; chỉ vế "đầy đủ chức năng" của C4 mới treo BA.

`srs-fr-01-dashboard.md:685` (SCR-I-01 quyền truy cập)
```
- **Vai trò KHÔNG có quyền:** Doanh nghiệp (sử dụng Cổng DN riêng — Nhóm VII), Tư vấn viên/Chuyên gia (có view riêng cho vụ việc được phân công — Nhóm IV/V), tài khoản chưa đăng nhập.
```
> ⇒ **DN KHÔNG được thấy dashboard CMS.** Nếu DN login xong không vào dashboard, đó là ĐÚNG SRS, không phải bug.

`srs-fr-07-doanh-nghiep.md:508` + `:512-514` (SCR-V.III-04 — surface DN duy nhất được đặc tả)
```
### SCR-V.III-04: Hồ sơ doanh nghiệp của tôi (chuyên trang DN) `[v3.5 — BA chốt 2026-05-13]`
**Mô tả:** Chuyên trang DN tự xem + cập nhật hồ sơ doanh nghiệp của chính mình sau khi đăng nhập VNeID Tier 2. Bố cục 4 tab giống SCR-V.III-02 …
**URL:** `/doanh-nghiep/ho-so-cua-toi`
**Quyền truy cập:** Doanh nghiệp (Tier 2 VNeID). Phạm vi dữ liệu theo nhân thân — chỉ DOANH_NGHIEP có MST khớp username. Vai trò khác KHÔNG truy cập trang này.
```

`srs-fr-07-doanh-nghiep.md:399` (FR-V.III-NEW-02 AC — 5 tab)
```
- **Given** DN đăng nhập VNeID Tier 2 **When** mở "Hồ sơ DN của tôi" **Then** hiển thị 5 tab (Thông tin / Hồ sơ pháp lý / Lịch sử hỗ trợ / Hồ sơ chi trả / Đăng ký đào tạo của tôi — tab cuối render FR-III-NEW-05) với dữ liệu của DN mình
```
> Cả `:512`, `:514`, `:399` đều gate **"Tier 2 VNeID"**, còn FR-VIII-22:1116 nói DN đăng nhập MST+MK. SRS không nói surface này có mở cho phiên MST+MK hay không ⇒ đúng nghĩa GAP.

### 2.6 Đăng nhập — bước OTP + khóa 5 lần sai (bẫy đo C3)

`srs-fr-10-quan-tri.md:923` (FR-VIII-20 Inputs 3)
```
| 3 | otp_code | text | Y (bước 2) | Mã TOTP 6 số sinh bởi ứng dụng xác thực (mã một lần theo thời gian) | — | user input |
```

`srs-fr-10-quan-tri.md:934` + `:963` (khóa sau 5 lần sai)
```
| 6 | Nếu sai: tăng số lần đăng nhập sai. Nếu >= 5 → tạm khóa tài khoản | BR-AUTH-07 |
| E4 | Đăng nhập sai >= 5 lần | ERR-DN-04 | "Tài khoản đã bị tạm khóa do đăng nhập sai quá 5 lần" | ERROR |
```

`srs-fr-10-quan-tri.md:1886` (SCR-VIII-07 — ô OTP)
```
| 7 | modal | Input OTP 6 so | text-input (6 o) | Tu chuyen focus, chi nhan so, hieu luc 5 phut | — | buoc 2 xac thuc |
```

`srs-fr-10-quan-tri.md:915` (FR-VIII-20 Preconditions) — **chặn PASS-oan trước C2**
```
- Tài khoản ở trạng thái HOAT_DONG
```

### 2.7 Không có bước cán bộ duyệt trước khi gửi thư kích hoạt (tiền đề)

`srs-fr-10-quan-tri.md:1945-1947` (SCR-VIII-08a đã bỏ)
```
### SCR-VIII-08a: ĐÃ BỎ — QTHT phê duyệt TK đăng ký
> **[ĐÃ BỎ — BA chốt 2026-05-07 Q3+Q10]** Sau khi bỏ trạng thái CHO_PHAN_QUYEN, không còn TK ở state này → màn hình duyệt không có dữ liệu hiển thị. Workflow tạo TK mới: TK đi thẳng từ CHO_KICH_HOAT → HOAT_DONG khi user kích hoạt qua email + đặt mật khẩu lần đầu (FR-VIII-26). …
```

`srs-fr-10-quan-tri.md:1941` (SCR-VIII-08 — auto-pass)
```
> **Auto-pass:** Hệ thống KHÔNG validate nội dung với cơ quan ngoài (Tổng cục Thuế, Bộ Công An...) — tin tưởng DN khai. Đồng bộ VNeID Tổ chức là bước xác thực thực sự sau khi có tài khoản (tùy chọn, qua FR-VIII-25). DN khai man → bỏ qua, không xử lý (BA chốt 2026-05-05).
```

`srs-fr-10-quan-tri.md:1104` (Postcondition 1 — state ban đầu)
```
- Bản ghi TAI_KHOAN được tạo ở trạng thái CHO_KICH_HOAT, đã gán vai trò DN
```

**⇒ KHÔNG có bước cán bộ duyệt.** Gửi thư kích hoạt là bước 10 của chính FR-VIII-22 (`:1088`), chạy ngay sau submit.

---

## 3. Tiền đề tối thiểu + luồng dựng cho Giai đoạn B

**Env:** `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025`

### 3.1 Cần dựng: 1 DN tự đăng ký mới, chưa kích hoạt

Đúng, đây là tiền đề hợp lý và **tự dựng được không cần cán bộ** — SRS không yêu cầu duyệt (§2.7).

- **Màn dựng:** SCR-VIII-07 `/login` → nút **"Đăng ký (dành cho doanh nghiệp)"** (`srs-fr-10-quan-tri.md:1890`) → **SCR-VIII-08** (`:1895`, FR-VIII-22).
- **Trạng thái ban đầu:** `TAI_KHOAN.trang_thai = CHO_KICH_HOAT`, `username = MST`, vai trò DN gán sẵn (`:1104`, `:2106`).

### 3.2 Trường BẮT BUỘC (13 trường — cột "Bắt buộc = Y" của FR-VIII-22 Inputs `:1044-1072`)

| # SRS | Trường | Ràng buộc phải thoả |
|---|---|---|
| 1 | `ten_doanh_nghiep` | không rỗng |
| 2 | `ma_so_thue` | **đúng 10 chữ số** `^\d{10}$`; **chưa tồn tại trong DOANH_NGHIEP** — nếu trùng sẽ ra `ERR-REG-MST-EXIST` (`:1096`) và rơi sang Claim Flow, KHÁC case |
| 4 | `dia_chi` | không rỗng |
| 5 | `tinh_thanh_id` | chọn từ dropdown Tỉnh/TP |
| 6 | `loai_doanh_nghiep_id` | chọn từ dropdown Loại hình DN |
| 7 | `quy_mo` | Siêu nhỏ / Nhỏ / Vừa |
| 8 | `nganh_nghe` | Nông Lâm / Công nghiệp / Thương mại |
| 12 | `nguoi_dai_dien` | không rỗng |
| 14 | `email` | RFC 5322, **unique trên TAI_KHOAN.email** — dùng email mới, tránh `ERR-REG-02` (`:1097`) |
| 15 | `so_dien_thoai` | `^0\d{9,10}$` |
| 25 | `mat_khau` | ≥8 ký tự + hoa + thường + số + ký tự đặc biệt |
| 26 | `mat_khau_xac_nhan` | khớp `mat_khau` |
| 27 | `cam_ket_thong_tin_dung_su_that` | **phải tích** — thiếu là `ERR-REG-06` (`:1100`) |

> `linh_vuc_ids` (#16) **không bắt buộc** — bỏ trống vẫn phải đăng ký được (`:1121`). Bỏ trống để giảm biến số.

### 3.3 Luồng dựng + đo (đường UI ngắn nhất)

1. `/login` → "Đăng ký (dành cho doanh nghiệp)" → điền 13 trường §3.2 → **Đăng ký**.
   Kiểm: ô "Tên đăng nhập" readonly hiện đúng MST (`:1933`, AC `:1113`).
2. MailHog: mở thư kích hoạt gửi tới email vừa khai (`:1088` gửi tới `TAI_KHOAN.email`) → lấy URL chứa token.
3. **Đo C1:** bấm/mở URL → màn đặt mật khẩu render.
4. **Đo C2:** đặt MK mới hợp lệ (khác MK lúc đăng ký để phân biệt được nhánh nào đang chạy) + xác nhận → submit → thông báo thành công + về `/login`. Đối chứng qua `qtht_01` ở SCR-VIII-03.
5. **Đo C3:** `/login` username = MST + MK vừa đặt → OTP 6 số từ MailHog → vào được.
6. **Đo C4 (chỉ mức tối thiểu):** vào `/doanh-nghiep/ho-so-cua-toi` → ghi hiện trạng render / 403 / trắng. **Dừng ở đây.**

> **Ghi rõ trong báo cáo:** MK dùng lúc đăng ký (bước 1) và MK đặt ở bước 4 phải **khác nhau** — đây là phép thử quyết định để biết dev implement theo vế nào của SRS (§4.1) và để biết C3 pass bằng MK nào.

---

## 4. Caveat — chặn PASS-oan và FAIL-oan

### 4.1 Chặn PASS-oan

| Bẫy | Vì sao sai | Phải làm |
|---|---|---|
| Thấy màn đặt mật khẩu hiện ra là kết luận cả case xong | C1 chỉ là 1 trong 4 vế. `:1109` yêu cầu tiếp **HOAT_DONG** + **đăng nhập được** | Chạy đủ C2 → C3, mỗi vế 1 bằng chứng riêng |
| Toast "Đặt mật khẩu thành công" là chấm C2 đạt | Toast là thông báo FE (`:1327`); `:1116`+`:2299` yêu cầu **TAI_KHOAN.trang_thai** thật đổi sang HOAT_DONG | Đối chứng độc lập qua `qtht_01` / API `trang_thai` — chỉ mình toast không đủ |
| C3 pass nhưng **không xác định pass bằng MK nào** | Nếu dev vẫn dùng MK đặt lúc đăng ký (nhánh Inputs 25/26) thì "đặt MK ở màn kích hoạt" có thể **không có hiệu lực** mà login vẫn được → Pass oan cho C1+C2 | Bắt buộc 2 MK khác nhau (§3.3). Login **phải** thành công bằng MK mới; nếu chỉ MK cũ chạy được → C2 chưa đạt, ghi bug |
| Bỏ đếm request khi bấm submit | Double-submit / toast kép có thể che lỗi | `list_network_requests` mỗi lần submit, đếm request kèm toast; observer **không dedupe** |
| Chấm C4 "đạt" vì DN vào được 1 trang bất kỳ | "đầy đủ chức năng" chưa có định nghĩa trong SRS | C4 **KHÔNG chấm Pass/Fail** — chỉ ghi hiện trạng + treo BA (§5 Q2) |

### 4.2 Chặn FAIL-oan

| Bẫy | Vì sao KHÔNG phải bug | Căn cứ |
|---|---|---|
| "Không nhận được email thật" | Env chưa tích hợp mail thật, giả lập qua MailHog (mở, no auth). Không log bug, không khuyên check Spam | memory `reference-uat-mailhog-env-doi-tac` |
| Link kích hoạt "hết hạn" | Với TK `CHO_KICH_HOAT`, SRS nói token **vĩnh viễn** (`:1088`, `:1317`). Nếu gặp `ERR-PWD-03` trên DN vừa dựng → đó là bug/hoặc mâu thuẫn §2.4, **không** kết luận "do QA để lâu" | `:1088`, `:1317` vs `:2306` |
| DN login xong không thấy dashboard CMS | SRS ghi rõ DN **KHÔNG có quyền** dashboard | `srs-fr-01-dashboard.md:685` |
| Badge/nhãn hiện "Hoạt động" chứ không phải "Đang hoạt động" | SRS dùng nhãn "Hoạt động" cho TAI_KHOAN; "Đang hoạt động" là nhãn SM-TVV/SM-NHT | `:1713`, `:1720`, `:2290` |
| Bước OTP ở login "phát sinh thêm" | SRS bắt buộc OTP 6 số bước 2 | `:923`, `:1886` |
| Login fail sau vài lần thử → kết luận "kích hoạt không thành công" | 5 lần sai → `TAM_KHOA` (`ERR-DN-04`); ngoài ra env có rate-limit login (`ERR-SYS-00-29-01`) | `:934`, `:963`; memory `reference-uat-account-passwords` |
| Không vào được `/doanh-nghiep/ho-so-cua-toi` bằng phiên MST+MK | SRS gate trang này ở **Tier 2 VNeID** (`:512`, `:514`, `:399`), env nội bộ không có VNeID → SRS mâu thuẫn với `:1109` | route BA, KHÔNG log bug (§5 Q2) |
| Bấm liên kết ra thẳng trạng thái hoạt động mà **không** có màn đặt MK | Là nhánh Inputs 25/26 của chính FR-VIII-22 (`:1070`, `:1081`, `:1083`) — SRS tự mâu thuẫn | route BA (§5 Q1), KHÔNG chấm FAIL |
| Gặp 4xx/5xx khi đổi màn / đổi role / đổi filter ngoài 6 bước §3.3 | Ngoài vế đang verify | ghi **candidate**, KHÔNG mở rộng case điều tra |

---

## 5. Câu hỏi BA nháp (cho vế DIFF/GAP)

### Q1 — FR-VIII-22: DN đặt mật khẩu ở form đăng ký hay ở màn kích hoạt? (ảnh hưởng C1, C2)

FR-VIII-22 quy định **hai đường loại trừ nhau** trong cùng một FR:

- **Đường A** — DN đặt mật khẩu **ngay ở form đăng ký**: Inputs #25 `mat_khau` bắt buộc + #26 `mat_khau_xac_nhan` (`srs-fr-10-quan-tri.md:1070-1071`), Processing bước 4 "Kiểm tra mật khẩu đủ độ mạnh + khớp xác nhận" (`:1081`), bước 6 "Mã hóa mật khẩu (hash 1 chiều)" (`:1083`), SCR-VIII-08 row 26-27 (`:1934-1935`).
- **Đường B** — DN đặt mật khẩu **lần đầu qua liên kết kích hoạt**: Postconditions (`:1109`), AC (`:1116`), SM-TAIKHOAN (`:2299`), FR-VIII-26 (`:1325`). Ghi chú `[STT80 UAT 2026-06-02]` tại `:704` và `:1730` cũng đi theo đường B cho luồng cán bộ.

Nếu đường A đúng thì mật khẩu đã có từ lúc đăng ký, và liên kết trong thư chỉ còn nhiệm vụ xác thực email + chuyển `CHO_KICH_HOAT → HOAT_DONG`; lúc đó **không tồn tại "màn đặt mật khẩu"** và bước 2 trong phiếu UAT ("Doanh nghiệp đặt mật khẩu thành công") là không đo được. Nếu đường B đúng thì Inputs #25/#26 phải bỏ khỏi form đăng ký (như đã làm cho FR-VIII-15 ở `:704`).

**Đề nghị BA chốt:** luồng DN tự đăng ký, mật khẩu được đặt ở bước nào? Và tương ứng, khi DN mở liên kết kích hoạt hợp lệ thì hệ thống phải hiển thị màn gì?

### Q2 — Vai trò DN sau khi tài khoản hoạt động được dùng những chức năng nào, trên giao diện nào? (ảnh hưởng C4)

Phiếu UAT yêu cầu "sử dụng đầy đủ chức năng". SRS hiện có 4 phát biểu không khớp nhau:

1. `srs-fr-10-quan-tri.md:1109` — DN "có thể đăng nhập + dùng đầy đủ chức năng (không hạn chế dù chưa đồng bộ VNeID Tổ chức)", nhưng **không liệt kê** chức năng nào.
2. `srs-v3.5.md:1380` — "DN không truy cập CMS trực tiếp. Quyền Create/Read của DN thực hiện qua API inbound từ Cổng PLQG".
3. `srs-v3.5.md:5535` (BR-AUTH-11) — "DN KHÔNG đăng nhập CMS → không có phiên phân quyền dữ liệu"; trạng thái BR này là **🟡 Đề xuất — chờ CĐT xác nhận** (`:5537`).
4. `srs-fr-07-doanh-nghiep.md:508-514` (SCR-V.III-04 `/doanh-nghiep/ho-so-cua-toi`) và AC `:399` — có màn cho DN, nhưng điều kiện truy cập ghi **"Doanh nghiệp (Tier 2 VNeID)"**, còn `srs-fr-10-quan-tri.md:1116` lại nói DN đăng nhập bằng MST + mật khẩu.

Thêm nữa `srs-fr-01-dashboard.md:685` ghi DN **không có quyền** vào dashboard, nên "đầy đủ chức năng" chắc chắn không bao gồm màn CMS của cán bộ.

**Đề nghị BA chốt 3 điểm:** (a) danh sách chức năng/màn hình mà vai trò DN được dùng sau khi tài khoản HOAT_DONG; (b) phiên đăng nhập bằng MST + mật khẩu có được vào các màn đó không, hay bắt buộc phải qua VNeID Tier 2; (c) BR-AUTH-11 còn hiệu lực hay đã bị FR-VIII-22 thay thế.

### Q3 — Liên kết kích hoạt có hạn hiệu lực không?

- FR-VIII-22 bước 10 (`srs-fr-10-quan-tri.md:1088`): "link **vĩnh viễn**, 1 lần dùng".
- FR-VIII-26 bước 5 (`:1317`): "Hạn token: **vĩnh viễn** nếu TK ở CHO_KICH_HOAT".
- SM-TAIKHOAN (`:2306`, lặp ở `srs-v3.5.md:6397`): `CHO_KICH_HOAT → VO_HIEU_HOA | Auto: quá 7 ngày | activation_token_expired`.

**Đề nghị BA chốt:** liên kết kích hoạt vĩnh viễn hay hết hiệu lực sau 7 ngày (và tài khoản có tự bị vô hiệu hóa không)? Chốt xong xin sửa cho khớp ở cả 3 vị trí trên.

---

## 6. Lệnh grep / Read đã chạy trong lượt này

Thư mục gốc mọi lệnh: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`

```bash
ls -la <srs-v3.5>/
grep -c "kích hoạt" *.md
grep -c "đăng ký tài khoản" *.md
grep -c "mã số thuế" *.md
grep -n "liên kết kích hoạt\|đường dẫn kích hoạt\|link kích hoạt\|token kích hoạt" *.md
grep -n "FR-VIII-26\|FR-VIII-2[0-9]\|Quên mật khẩu\|Kích hoạt tài khoản" srs-fr-10-quan-tri.md
grep -n "^#\{1,4\} \|^\*\*FR-" srs-fr-10-quan-tri.md
grep -n "kích hoạt\|mã số thuế\|Mã số thuế" srs-fr-07-doanh-nghiep.md
grep -n "Đang hoạt động" srs-fr-10-quan-tri.md            # → 0 hit (nhãn SRS là "Hoạt động")
grep -rn "activation_token_expired\|quá 7 ngày\|7 ngày" *.md
grep -n "Permission Matrix\|Ma trận quyền" srs-v3.5.md
grep -n "^| Entity\|^| Nhóm\|DN |" srs-v3.5.md
grep -rn "BR-AUTH-11" *.md
grep -rn "chuyên trang" *.md
grep -rn "M-05" *.md
grep -rn "giao diện DN" *.md
grep -rn "403\|Không có quyền truy cập\|ERR-SYS-03" srs-v3.5.md   # → 0 hit
grep -n "DN\b" srs-fr-01-dashboard.md
grep -n "^### SCR\|vai trò DN\|Vai trò DN\|DN đăng nhập\|Doanh nghiệp đăng nhập" srs-fr-07-doanh-nghiep.md
grep -rn "SCR-V.I-05" *.md
grep -n "FR-V.III-NEW-02" srs-fr-07-doanh-nghiep.md
grep -n "Hoạt động\|Chờ kích hoạt" srs-fr-10-quan-tri.md
grep -rn "ERR-SYS-00-29\|rate.limit\|Rate limit\|giới hạn số lần" srs-v3.5.md srs-fr-10-quan-tri.md
grep -n "Gửi lại email kích hoạt\|gửi lại mail kích hoạt" srs-fr-10-quan-tri.md
grep -rn "TOTP 2FA qua email\|OTP qua email\|mã OTP" srs-v3.5.md srs-fr-10-quan-tri.md
```

```
Read srs-fr-10-quan-tri.md offset 1024 limit 105    # FR-VIII-22 toàn bộ
Read srs-fr-10-quan-tri.md offset 1275 limit 92     # FR-VIII-26 toàn bộ
Read srs-fr-10-quan-tri.md offset  901 limit  76    # FR-VIII-20 đăng nhập
Read srs-fr-10-quan-tri.md offset 2093 limit  30    # entity TAI_KHOAN
Read srs-fr-10-quan-tri.md offset 1868 limit  85    # SCR-VIII-07 + SCR-VIII-08 + 08a
Read srs-fr-10-quan-tri.md offset 2265 limit  50    # SM-TAIKHOAN
Read srs-fr-10-quan-tri.md offset 1696 limit  42    # SCR-VIII-03
Read srs-fr-10-quan-tri.md offset 1172 limit   6    # FR-VIII-23 postconditions
Read srs-v3.5.md          offset 1292 limit  95    # Permission Matrix + footnote †
Read srs-v3.5.md          offset 5528 limit  14    # BR-AUTH-10/11/12 + status
Read srs-v3.5.md          offset  830 limit  30    # §3.2.0.4 phân quyền dữ liệu
Read srs-v3.5.md          offset 6393 limit   7    # SM-TAIKHOAN baseline (7 ngày)
Read srs-fr-01-dashboard.md offset 676 limit  14    # quyền truy cập SCR-I-01
Read srs-fr-07-doanh-nghiep.md offset 355 limit 55  # FR-V.III-NEW-02
Read srs-fr-07-doanh-nghiep.md offset 508 limit 42  # SCR-V.III-04
```

**Không mở** `input/srs-update-2026-5-5/`, `input/srs-v3/`, thư BA, phiếu UAT, báo cáo đợt cũ để lấy số dòng.
**Không** gọi `mcp__chrome-devtools__*`, **không** curl vào app — Giai đoạn A chỉ đọc đặc tả.
