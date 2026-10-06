# QLDXDTTH_01 — Cổng 3 (đối chiếu SRS)

> **Case đối tác:** Tuần 2, log row 337 — *"Quản lý các đề xuất tổ chức đào tạo/tập huấn từ các đơn vị/cá nhân khác"*.
> **Đối tác báo:** *"Gửi đề xuất báo thành công nhưng đề xuất không hiển thị trên màn hình danh sách."*
> **Kỳ vọng đối tác:** tạo đề xuất trạng thái "Mới" + thông báo cho CB nghiệp vụ đơn vị tiếp nhận + toast *"Đã gửi đề xuất đào tạo"*.
> **Nguồn SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).

---

## Mục SRS liên quan

### A. FR-III-13 — Quản lý đề xuất đào tạo (UC32)

Toàn bộ FR gói gọn trong `srs-fr-03-dao-tao.md:1040`–`:1063`. Trích nguyên văn các dòng quyết định:

**`:1043`**
> **Màn hình:** SCR-III-01 (tab "De xuat")

**`:1045`**
> **Mô tả:** DN/NHT gửi đề xuất đào tạo. CB NV tiếp nhận. Sửa/xóa khi chưa tiếp nhận.

**`:1047`**
> **Tác nhân:** DN / NHT

**`:1051`**
> **Inputs:** linh_vuc_id (identifier, Y), noi_dung (text long, Y), thoi_gian_mong_muon (text, N), dia_diem_mong_muon (text, N), so_luong_du_kien (number, N).

**`:1053`** — dòng quan trọng nhất:
> **Processing:** Validate → **Tạo DE_XUAT_DAO_TAO (MOI)** → **Thông báo CB NV** → Ghi nhật ký. Sửa: chỉ khi MOI. Xóa: chỉ khi MOI, xóa mềm.

**`:1055`**
> **Outputs:** id, linh_vuc, noi_dung (truncate), **trang_thai (MOI/DA_TIEP_NHAN/DA_THUC_HIEN)**, ngay_tao.

**`:1057`**
> **Postconditions:** Đề xuất được tạo/cập nhật/xóa mềm. **CB NV nhận thông báo.**

**`:1059`**
> **Error Handling:** ERR-DX-01 "Nội dung đề xuất là bắt buộc". ERR-DX-02 "Không thể sửa đề xuất đã tiếp nhận". ERR-DX-03 "Đề xuất đã tiếp nhận không thể xóa".

**`:1062`** — Acceptance Criteria:
> - **Given** DN/NHT thêm mới **When** nhập nội dung + lĩnh vực **Then** gửi cho đơn vị quản lý

→ **Không có** mục *Preconditions* chi tiết ngoài `:1049` (*"DN/NHT đã đăng nhập."*); **không có** đặc tả toast thành công; **không có** đặc tả bộ lọc mặc định của danh sách.

### B. SCR-III-01 — nơi đề xuất được hiển thị (phía cán bộ)

**`srs-fr-03-dao-tao.md:1875`** — Thành phần 8 (nguyên văn):

> **Thành phần 8 — Tab "Đề xuất đào tạo":** Tab phụ tiếp nhận đề xuất từ DN/NHT. Bảng cột Lĩnh vực · Nội dung (cắt 150 ký tự) · Người đề xuất · Trạng thái (3 nhãn v3 — giữ nguyên do BA OUT Thay đổi 15) · Ngày tạo · Hành động (Xem · Tiếp nhận · Đánh dấu thực hiện).

**`srs-fr-03-dao-tao.md:1817`** — nguyên văn:

> **FR sử dụng:** FR-III-01 (CRUD CTDT + workflow phê duyệt CTDT mới), FR-III-02 (Tìm kiếm), FR-III-03 (Quản lý đăng ký), FR-III-04 (Đăng ký HV), **FR-III-13 (Đề xuất — tab phụ)**

→ **Đây là màn hình DUY NHẤT** trong toàn bộ SRS v3.5 mà đề xuất đào tạo được liệt kê hiển thị. Đã grep toàn bộ 18 tệp SRS v3.5: không có mục nào tên *"Đề xuất đào tạo của tôi"* / *"Đề xuất của tôi"*, và `srs-fr-01-dashboard.md` / `srs-fr-07-doanh-nghiep.md` / `srs-fr-15-ct-htpldn.md` **không nhắc** đề xuất đào tạo lần nào.

### C. Entity DE_XUAT_DAO_TAO — trạng thái khởi tạo + chủ sở hữu dữ liệu

**`srs-v3.5.md:2665`** (nguyên văn):
> | 6 | trang_thai | text | Y | CHECK IN ('MOI','DA_TIEP_NHAN','DANG_XU_LY','DA_THUC_HIEN','TU_CHOI') | **'MOI'** | Trạng thái (sync naming với FR-03 — F-FR03-06) |

**`srs-v3.5.md:2667`** (nguyên văn):
> | 8 | don_vi_id | identifier | Y | FK → DON_VI(id) | — | **Đơn vị tiếp nhận (phân quyền)** |

**`srs-v3.5.md:2661`** (nguyên văn):
> | 2 | nguoi_de_xuat_id | identifier | Y | FK → TAI_KHOAN(id) | — | Người đề xuất |

→ `trang_thai` mặc định `'MOI'` khớp kỳ vọng đối tác. `don_vi_id` là **đơn vị tiếp nhận** và là trục phân quyền → CB NV **thuộc đúng đơn vị đó** mới thấy bản ghi.

### D. Ma trận phân quyền — DN/NHT có quyền ĐỌC nhưng SRS không cấp màn hình

**`srs-v3.5.md:1309`** (nguyên văn; thứ tự cột theo dòng tiêu đề `:1295`: QTHT · CB_NV_TW · CB_NV_BN · CB_NV_DP · CB_PD_TW · CB_PD_BN · CB_PD_DP · DN · NHT · TVV · CG; ký hiệu giải nghĩa tại `:1293`):

> | DE_XUAT_DAO_TAO | R | R | R* | R* | R | R* | R* | **C†RU*** | **C†RU*** | — | — |

**`srs-v3.5.md:1375`** — chú thích dấu † (nguyên văn):

> † DN không truy cập CMS trực tiếp. Quyền Create/Read của DN thực hiện qua API inbound từ Cổng PLQG (SI-04, Nhóm XII). **Permission Matrix ghi nhận quyền LOGIC, không phải quyền CMS UI.**

**`srs-v3.5.md:1373`** (nguyên văn):
> - **Ngang cấp KHÔNG thấy nhau** — chính sách phân quyền dữ liệu đảm bảo chỉ thấy dữ liệu đơn vị mình

→ Đây là mấu chốt của case: DN/NHT **có quyền logic** `R*`/`U*` trên đề xuất của mình, nhưng SRS **không mô tả màn hình nào** cho DN/NHT xem lại. Đối chiếu tiền lệ: khi BA muốn DN tra cứu dữ liệu của mình, SRS **viết hẳn một FR + gắn vào một tab cụ thể** — xem FR-III-NEW-05 *"DN tra cứu đăng ký đào tạo của mình"* (`srs-fr-03-dao-tao.md:1668`) được render tại `srs-fr-07-doanh-nghiep.md:511` + `:526` (Tab 5 của SCR-V.III-04). **Đề xuất đào tạo không có cặp FR+tab tương đương.**

---

## UC Reference

| Mục SRS | UC Reference | Dòng |
|---|---|---|
| **FR-III-13 Quản lý đề xuất đào tạo** | **UC 32** | `srs-fr-03-dao-tao.md:1042` — *"**UC Reference:** UC 32 \| **Priority:** Essential \| **Stability:** High"* |
| (đối chiếu) FR-III-NEW-05 DN tra cứu đăng ký đào tạo của mình | *"— (phantom FR, gap SRS phát hiện từ báo cáo review HDSD §6.4 #2)"* | `srs-fr-03-dao-tao.md:1670` |
| **SCR-III-01 Chương trình đào tạo (chứa tab Đề xuất)** | **KHÔNG có dòng `UC Reference`** — mục đặc tả màn hình không mang trường này. Thay thế: `srs-fr-03-dao-tao.md:1814` (heading SCR-III-01) + `:1817` (**FR sử dụng** … FR-III-13) + `:1875` (Thành phần 8) | 1814 / 1817 / 1875 |

> **Truy vết chéo:** `srs-v3.5.md:4773` — *"| FR-III-13 | Quản lý đề xuất đào tạo (UC32) | D, T | TP-III-13 | Tạo/trình đề xuất, workflow phê duyệt | ⬜ |"*; `srs-v3.5.md:5148` — *"| FR-III-13 | Quản lý đề xuất đào tạo | UC32 | PRD §4.3 | NĐ 55/2019 (Đ.10 K.2) | III |"*.

---

## Bảng Cổng 3 (khung, chưa điền cột thực tế web)

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| Form gửi đề xuất có trường **Lĩnh vực** — bắt buộc (`srs-fr-03:1051`) | | |
| Form có trường **Nội dung** — bắt buộc (`:1051`) | | |
| Form có trường **Thời gian mong muốn** — tuỳ chọn (`:1051`) | | |
| Form có trường **Địa điểm mong muốn** — tuỳ chọn (`:1051`) | | |
| Form có trường **Số lượng dự kiến** — tuỳ chọn (`:1051`) | | |
| Bỏ trống Nội dung → từ chối kèm thông báo tương ứng **ERR-DX-01** *"Nội dung đề xuất là bắt buộc"* (`:1059`) | | |
| Gửi thành công → bản ghi được **tạo** (`:1053`) — ghi lại mã/ID bản ghi + phản hồi của yêu cầu tạo | | |
| Bản ghi vừa tạo có **trạng thái "Mới" (`MOI`)** (`:1053`, `srs-v3.5.md:2665`) | | |
| Bản ghi ghi nhận **người đề xuất** = tài khoản đang đăng nhập (`srs-v3.5.md:2661`) | | |
| Bản ghi ghi nhận **đơn vị tiếp nhận** (`don_vi_id`) (`srs-v3.5.md:2667`) — ghi rõ đơn vị nào | | |
| **CB NV của đơn vị tiếp nhận nhận được thông báo** (`:1053`, `:1057`) — kiểm hộp thông báo trong ứng dụng của tài khoản CB NV đúng đơn vị | | |
| Đề xuất **hiển thị ở tab "Đề xuất đào tạo"** của màn Chương trình đào tạo, phía CB NV cùng đơn vị (`:1043`, `:1875`) | | |
| Tab Đề xuất có cột **Lĩnh vực** (`:1875`) | | |
| Tab Đề xuất có cột **Nội dung** (cắt 150 ký tự) (`:1875`) | | |
| Tab Đề xuất có cột **Người đề xuất** (`:1875`) | | |
| Tab Đề xuất có cột **Trạng thái** (3 nhãn) (`:1875`) | | |
| Tab Đề xuất có cột **Ngày tạo** (`:1875`) | | |
| Tab Đề xuất có Hành động **Xem · Tiếp nhận · Đánh dấu thực hiện** (`:1875`) | | |
| DN/NHT **sửa được** đề xuất khi còn ở trạng thái Mới (`:1053` — *"Sửa: chỉ khi MOI"*; quyền `U*` tại `srs-v3.5.md:1309`) | | |
| DN/NHT **xóa được** (xóa mềm) khi còn Mới (`:1053`) | | |
| Sửa đề xuất đã tiếp nhận → từ chối kèm thông báo tương ứng **ERR-DX-02** (`:1059`) | | |
| **[SRS chưa quy định — chỉ ghi nhận]** Toast sau khi gửi: nội dung thực tế là gì | | — |
| **[SRS chưa quy định — chỉ ghi nhận]** DN/NHT có màn hình nào xem lại đề xuất đã gửi không (`srs-v3.5.md:1375` cho quyền logic nhưng không có SCR) | | — |
| **[SRS chưa quy định — chỉ ghi nhận]** Bộ lọc **mặc định** của tab Đề xuất khi mới mở (có ẩn trạng thái Mới không) | | — |

> **Ghi chú cho người verify — phải tách bạch 2 phía, nếu không sẽ chấm nhầm:**
> - **Phía CB NV** (đúng đơn vị tiếp nhận): nếu bản ghi đã tạo mà **không** xuất hiện ở tab Đề xuất → vi phạm `:1043` + `:1875` → hướng `Open`.
> - **Phía DN/NHT** (người gửi): nếu chỉ là "người gửi không xem lại được đề xuất của mình" → SRS không có màn hình cho việc này → hướng `BA confirm`, KHÔNG log Open.
> - Bắt buộc thử **tài khoản CB NV đúng đơn vị** rồi mới kết luận. Xem `srs-v3.5.md:1373` — đơn vị khác thì không thấy là **đúng thiết kế**, không phải bug.

---

## SRS có/không quy định

**Kết luận chính: (a) — SRS quy định RÕ ở phía CB NV. Nhánh phụ: (c) SRS SILENT ở phía DN/NHT.**

**Nhánh (a) — quy định RÕ, nếu sai thì `Open`:**
1. **Trạng thái khởi tạo `MOI`** — `:1053` + `srs-v3.5.md:2665` (default `'MOI'`). Không mơ hồ.
2. **Thông báo cho CB NV** — `:1053` (*"Thông báo CB NV"*) + `:1057` (*"CB NV nhận thông báo"*). Nêu hai lần, là yêu cầu cứng.
3. **Nơi hiển thị** — `:1043` (*"Màn hình: SCR-III-01 (tab 'De xuat')"*) + `:1875` (bảng cột đầy đủ của tab). Nếu CB NV đúng đơn vị mở tab Đề xuất mà không thấy bản ghi vừa tạo → vi phạm rõ.

**Nhánh (c) — SILENT, phải `BA confirm`, KHÔNG được chấm Open:**
1. **Không có màn hình cho DN/NHT xem lại đề xuất của mình.** Ma trận `srs-v3.5.md:1309` cấp `R*`/`U*` cho DN/NHT nhưng `:1375` nói rõ đó là **quyền logic, không phải quyền giao diện**; và toàn bộ SRS v3.5 không có SCR nào render danh sách này cho DN. Trong khi cùng nhóm III, BA đã viết hẳn FR-III-NEW-05 + Tab 5 SCR-V.III-04 cho việc DN tra cứu đăng ký đào tạo (`srs-fr-03-dao-tao.md:1668`, `srs-fr-07-doanh-nghiep.md:526`) — nghĩa là khi BA muốn có, BA viết ra. Đề xuất đào tạo thiếu cặp tương đương → khoảng trống đặc tả thật, không phải app cắt bớt.
2. **Không có đặc tả nội dung toast thành công.** `:1059` chỉ liệt kê 3 mã lỗi ERR-DX-01/02/03, không có mẫu thông báo thành công. Chuỗi *"Đã gửi đề xuất đào tạo"* là kỳ vọng của đối tác, **không xuất hiện trong SRS**. Phụ lục E §I (`srs-v3.5.md:6713`–`:6724`) chỉ chuẩn hoá toast cho luồng **công khai lên Cổng PLQG**, không áp cho luồng này.
3. **Không có đặc tả bộ lọc mặc định** của tab Đề xuất. Nếu bản ghi tồn tại nhưng bị bộ lọc mặc định che → SRS không có căn cứ để nói đúng/sai.

**Cảnh báo tra chéo:** đã kiểm `tasks/srs-contradictions.md` — module Đào tạo có **2 entry Open** liên quan: `SRS-C-007` (FR-III-12, filter `vai_tro` giảng viên) và `SRS-C-008` (FR-III, optimistic-lock / **idempotency chống double-submit khi gửi đề xuất** — TC-DEXUAT-E-015). `SRS-C-008` chạm luồng gửi đề xuất: SRS **không quy định** chống double-submit. Nếu triệu chứng thực tế là "gửi 2 lần / bản ghi trùng" thì phải ghi *"depends on SRS-C-008 BA decision"*, không log như spec bình thường.

---

## Câu hỏi cho BA

1. Người gửi (DN/NHT) **có cần** một màn hình xem lại các đề xuất đào tạo mình đã gửi không? Ma trận quyền `srs-v3.5.md:1309` cấp `R*`/`U*` cho DN/NHT nhưng không mục SCR nào của SRS v3.5 render danh sách này. (có/không)
2. Nếu **có** — đặt ở đâu: thêm một tab vào *"Hồ sơ doanh nghiệp của tôi"* (SCR-V.III-04, theo đúng khuôn FR-III-NEW-05 đã làm cho Đăng ký đào tạo), hay một màn hình riêng? (chọn 1)
3. Đề xuất vừa gửi có bắt buộc hiển thị **ngay** ở tab "Đề xuất đào tạo" của CB NV đơn vị tiếp nhận, **không cần thao tác lọc nào**, hay bộ lọc mặc định của tab được phép ẩn trạng thái "Mới"? (hiển thị ngay / được phép ẩn)
4. Sau khi gửi đề xuất thành công, hệ thống có bắt buộc hiển thị thông báo xác nhận cho người gửi không? Nếu có, nội dung chuẩn là gì (SRS hiện chưa có mẫu — `srs-fr-03-dao-tao.md:1059` chỉ có 3 mã lỗi)? (có/không + nội dung)
5. `SRS-C-008` (Open) hỏi hệ thống có phải chống gửi trùng (double-submit) khi gửi đề xuất hay không — BA chốt được chưa? Việc này ảnh hưởng trực tiếp cách chấm case này nếu triệu chứng là bản ghi trùng/nuốt. (có/không)
