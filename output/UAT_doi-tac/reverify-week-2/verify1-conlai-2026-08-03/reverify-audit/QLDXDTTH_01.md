# QLDXDTTH_01 — Evidence audit verify vòng 1 (2026-08-03)

> Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · row **118**
> Cột P (`Trạng thái dev fix 1`, do dev điền) = `dev done` — **KHÔNG đụng**. QA chỉ ghi cột Q (`Verify`) + R.
> **Verdict QA: `Pass`** — dev khai đã fix, QA chứng minh được luồng chạy đúng end-to-end trên bản dựng hiện tại.
>
> Cổng 1 + Cổng 2 (đọc video + trích frame) đã làm ở phiên trước, lưu tại
> [`QLDXDTTH_01-evidence.md`](QLDXDTTH_01-evidence.md). Phiên này **tự mở lại 4 frame quyết định** để đóng Cổng 1, không nhận vay.
> Cổng 3 (đối chiếu SRS) dựng ở [`../srs/QLDXDTTH_01-srs.md`](../srs/QLDXDTTH_01-srs.md), phiên này **đã tự mở SRS xác minh lại từng số dòng**.

---

## Note dev trước khi QA đè (2026-08-03)

Nguyên văn cột R (`DEV phản hồi lần 1`) đọc lại từ sheet lúc 2026-08-03 trước khi ghi:

> Code đã đúng: create/list nhất quán (cùng đơn vị) + double-refresh (invalidate+refetch) — triệu chứng "đề xuất không hiển thị" do bản build cũ. Đã có trên nhánh fix + deploy 120.

Các ô khác của row 118 tại thời điểm ghi (không đổi):

| Cột | Giá trị |
|---|---|
| D `Mã TC` | `QLDXDTTH_01` |
| E `Tên chức năng` | `Quản lý đề xuất đào tạo, tập huấn` |
| F `Tác nhân` | `Doanh nghiệp/Người hỗ trợ` |
| K `Kết quả mong đợi` | `- Tạo đề xuất ở trạng thái "Mới".` / `- Gửi thông báo cho Cán bộ nghiệp vụ thuộc đơn vị tiếp nhận.` / `- Gửi thành công, hệ thống hiển thị thông báo "Đã gửi đề xuất đào tạo".` |
| L `Kết quả thực tế` | `Hệ thống hiển thị thông báo thành công nhưng đề xuất không hiển thị trên màn hình` |
| N `Trạng thái 1` | `Fail` |
| O `TKM phản hồi lần 1` | `25/7: uc này đang lỗi nên các tc bên dưới test sau` |
| P `Trạng thái dev fix 1` | `dev done` |
| Q `Verify` | (trống — QA điền phiên này) |

---

## Bản dựng đã đo (bắt buộc ghi lại — bài học "tab mở lâu vẫn chạy mã cũ")

Đã **thoát phiên cũ + tải lại trang có bỏ qua bộ nhớ đệm** trước khi đo. 3 dấu hiệu nhận dạng bản dựng:

| Dấu hiệu | Giá trị |
|---|---|
| Số hiệu hiển thị trên giao diện (chân logo thanh bên) | **`HTPLDN · V1.0.5`** |
| Gói mã giao diện đang chạy | **`/assets/index-DeoB6dQU.js`** · ETag `"6a704a6a-111bb7"` · 1.121.207 byte |
| Thời điểm gói mã được tạo trên máy chủ | **`Mon, 03 Aug 2026 07:59:38 GMT`** (≈ 14:59 giờ VN **cùng ngày verify**) |

⇒ Bản dựng đang chạy **mới hơn** video đối tác (23/07/2026) đúng 11 ngày, và được deploy trong ngày verify. Điều này khớp với lời khai "đã có trên nhánh fix + deploy 120" của dev.

---

## Cổng 1 — 3 dữ kiện neo (tự mở lại frame, không nhận vay)

Frame đã tự mở đọc trong phiên này (full-res, không dùng ảnh ghép thu nhỏ):

| Frame | Đọc được gì |
|---|---|
| `frames/QLDXDTTH_01/t000.00s.jpg` | `uat.phapluat.gov.vn/danh-sach-ke-hoach-dao-tao`, đồng hồ trang `Thứ Năm, 23/07/2026, 16:18:41`. Màn **"Kế hoạch đào tạo"**, nút **"Gửi đề xuất đào tạo"** góc phải. Bảng **ĐÃ RỖNG SẴN**: *"Không tìm thấy kế hoạch đào tạo nào phù hợp."* — **trước** khi bấm gửi |
| `frames/QLDXDTTH_01/dense/t029.25s.jpg` | Form đã nhập: `LĨNH VỰC = Dân sự` · `ĐƠN VỊ TIẾP NHẬN = Cục Bổ trợ tư pháp – Bộ Tư pháp` · `NỘI DUNG = TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026` (51/5000) · `THỜI GIAN = quý 3/2026` · `ĐỊA ĐIỂM = Hà No…` (đang gõ) · `SỐ LƯỢNG` còn trống. Nút `Hủy` / `Gửi đề xuất` |
| `frames/QLDXDTTH_01/toast/t034.26s.jpg` | Đồng hồ `16:19:15`. Hộp thoại giữa màn, dấu tích xanh, tiêu đề **"Đã gửi đề xuất thành công!"**, phụ đề *"Cảm ơn bạn đã gửi ý kiến đóng góp đào tạo. Ban chuyên môn thuộc Câu lạc bộ Pháp chế Doanh nghiệp sẽ nghiên cứu tổng hợp và **đưa vào kế hoạch đào tạo** sớm nhất."* |
| `frames/QLDXDTTH_01/dense/t037.47s.jpg` | Đồng hồ `16:19:18`. Đã đóng hộp thoại, quay lại màn "Kế hoạch đào tạo", bảng vẫn *"Không tìm thấy kế hoạch đào tạo nào phù hợp."* — **đối tác bôi đen (highlight xanh) đúng dòng chữ này** để chỉ ra lỗi |

**(a) URL / mã bản ghi:** `uat.phapluat.gov.vn/danh-sach-ke-hoach-dao-tao`. Mã đề xuất **không đọc được** — hộp thoại thành công không trả mã, đối tác không mở màn nào khác.
**(b) Trạng thái entity:** không đọc được (không có màn nào hiển thị bản ghi trong video).
**(c) Dữ liệu tiền đề:** bộ 6 trường ở bảng trên; danh sách đích **rỗng từ trước** khi thao tác.

### 3 câu hỏi bắt buộc trả lời từ video

| # | Câu hỏi | Trả lời từ pixel |
|:-:|---|---|
| **(a)** | Đối tác đăng nhập vai trò nào? tên đăng nhập / đơn vị nào? | **Vai trò:** tài khoản đã đăng nhập trên **chuyên trang công khai** (có ảnh đại diện + chuông thông báo ở thanh đầu trang), khớp cột "Tác nhân" của sheet = **`Doanh nghiệp/Người hỗ trợ`**. Chắc chắn **không phải** tài khoản cán bộ. **Tên đăng nhập / đơn vị: KHÔNG xác định được** — thanh đầu trang chỉ hiện ảnh đại diện, đối tác không mở menu tài khoản trong suốt 50 giây video. Đơn vị *tiếp nhận* thì đọc được (`Cục Bổ trợ tư pháp – Bộ Tư pháp`) vì họ chọn tay trong form |
| **(b)** | Màn nào họ mong thấy đề xuất mà không thấy? | Màn **"Kế hoạch đào tạo"** của **chuyên trang DN** (`/danh-sach-ke-hoach-dao-tao`) — **không phải** tab "Đề xuất đào tạo" phía cán bộ. Xác định chắc chắn vì họ bôi đen đúng dòng *"Không tìm thấy kế hoạch đào tạo nào phù hợp."* trên chính màn đó |
| **(c)** | Thông báo thành công có hiện đúng như họ nói không? nội dung gì? | **CÓ.** Hộp thoại **"Đã gửi đề xuất thành công!"** + phụ đề nêu trên. Lưu ý: phiếu UAT ghi nội dung mong đợi là *"Đã gửi đề xuất đào tạo"* — khác câu chữ nhưng cùng ý, **không quy oan chỗ này** |

---

## Cổng 3 — SRS đối chiếu (đã tự mở file xác minh lại từng số dòng)

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25). Không dùng `input/srs-update-2026-5-5/`.

**Đã tự mở file và xác nhận số dòng khớp 100%** với phân tích dựng sẵn:

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-03-dao-tao.md:1040` | `### FR-III-13: Quản lý đề xuất đào tạo (UC32)` |
| `srs-fr-03-dao-tao.md:1042` | `**UC Reference:** UC 32 \| **Priority:** Essential \| **Stability:** High` |
| `srs-fr-03-dao-tao.md:1043` | `**Màn hình:** SCR-III-01 (tab "De xuat")` |
| `srs-fr-03-dao-tao.md:1047` | `**Tác nhân:** DN / NHT` |
| `srs-fr-03-dao-tao.md:1051` | `**Inputs:** linh_vuc_id (identifier, Y), noi_dung (text long, Y), thoi_gian_mong_muon (text, N), dia_diem_mong_muon (text, N), so_luong_du_kien (number, N).` |
| `srs-fr-03-dao-tao.md:1053` | `**Processing:** Validate → Tạo DE_XUAT_DAO_TAO (MOI) → Thông báo CB NV → Ghi nhật ký. Sửa: chỉ khi MOI. Xóa: chỉ khi MOI, xóa mềm.` |
| `srs-fr-03-dao-tao.md:1057` | `**Postconditions:** Đề xuất được tạo/cập nhật/xóa mềm. CB NV nhận thông báo.` |
| `srs-fr-03-dao-tao.md:1875` | `**Thành phần 8 — Tab "Đề xuất đào tạo":** Tab phụ tiếp nhận đề xuất từ DN/NHT. Bảng cột Lĩnh vực · Nội dung (cắt 150 ký tự) · Người đề xuất · Trạng thái (3 nhãn v3 …) · Ngày tạo · Hành động (Xem · Tiếp nhận · Đánh dấu thực hiện).` |
| `srs-v3.5.md:2665` | `\| 6 \| trang_thai \| text \| Y \| CHECK IN ('MOI','DA_TIEP_NHAN','DANG_XU_LY','DA_THUC_HIEN','TU_CHOI') \| 'MOI' \| Trạng thái …` |
| `srs-v3.5.md:2667` | `\| 8 \| don_vi_id \| identifier \| Y \| FK → DON_VI(id) \| — \| Đơn vị tiếp nhận (phân quyền) \|` |
| `srs-v3.5.md:1309` | `\| DE_XUAT_DAO_TAO \| R \| R \| R* \| R* \| R \| R* \| R* \| C†RU* \| C†RU* \| — \| — \|` |
| `srs-v3.5.md:1375` | `> † DN không truy cập CMS trực tiếp. … Permission Matrix ghi nhận quyền LOGIC, không phải quyền CMS UI.` |

**Đã tự grep lại toàn bộ 18 tệp SRS v3.5** (`grep -rn "đề xuất đào tạo\|DE_XUAT_DAO_TAO\|de-xuat-dao-tao"`): chỉ ra đúng các dòng trên + `srs-fr-03:31`, `:2003`, `srs-v3.5.md:1211/4245/4440-4442/4773/5148`. **Không có** mục SCR nào khác render danh sách đề xuất; `srs-fr-07-doanh-nghiep.md` và `srs-fr-01-dashboard.md` **không nhắc** đề xuất đào tạo lần nào (2 kết quả grep trong 2 tệp đó là "đề xuất quy mô" và "Đề xuất BA", không liên quan).
⇒ Kết luận "SRS silent về màn hình cho DN xem lại đề xuất" là **có căn cứ tìm kiếm**, không phải mặc định.

### Bảng Cổng 3 — SRS yêu cầu vs thực tế web (đã điền)

| SRS yêu cầu (dẫn line) | Thực tế web (bản dựng V1.0.5, 03/08/2026) | Đủ/Thiếu |
|---|---|:-:|
| Form có đúng 5 trường: Lĩnh vực (bắt buộc) · Nội dung (bắt buộc) · Thời gian · Địa điểm · Số lượng (`srs-fr-03:1051`) | Hộp thoại "Gửi đề xuất đào tạo" có **đúng 5 trường đó**, 2 trường đầu có dấu `*` | **Đủ** |
| Gửi thành công → **bản ghi được tạo** (`:1053`) | Bản ghi `b69a9545-59e4-4121-9760-91be29b65c19` được tạo, phản hồi máy chủ `201` | **Đủ** |
| Bản ghi ở **trạng thái khởi tạo "Mới"** (`:1053`, `srs-v3.5.md:2665`) | Giao diện hiển thị badge **"Mới gửi"** ở cả danh sách lẫn màn chi tiết; lọc tab "Mới gửi" ra đúng bản ghi này. Giá trị nội bộ máy chủ trả `MOI_GUI` | **Đủ** (xem ghi chú 1 bên dưới) |
| Bản ghi ghi nhận **người đề xuất** = tài khoản đang đăng nhập (`srs-v3.5.md:2661`) | `nguoiDeXuatId` = `996cc5db-43c5-4903-b3d1-1c21adb2ece8` = đúng tài khoản DN đang đăng nhập | **Đủ** |
| Bản ghi ghi nhận **đơn vị tiếp nhận** (`srs-v3.5.md:2667`) | `donViId` = `00000000-0000-4000-8002-000000000001` | **Đủ** |
| **CB NV của đơn vị tiếp nhận nhận được thông báo** (`:1053`, `:1057`) | `cbnv_hn` (đơn vị trùng khít) nhận thông báo trong ứng dụng: **"Đề xuất đào tạo mới — Có đề xuất đào tạo mới từ người dùng QA UAT Kiem Thu DN"**, giờ tạo `09:22:39.277Z` — **trùng giây** với giờ tạo bản ghi `09:22:39.183Z` | **Đủ** |
| Đề xuất **hiển thị ở tab "Đề xuất đào tạo"** phía CB NV cùng đơn vị (`:1043`, `:1875`) | `cbnv_hn` mở tab → thấy đúng bản ghi, badge "Mới gửi", ngày tạo 03/08/2026 | **Đủ** |
| Tab Đề xuất có cột **Lĩnh vực · Nội dung · Trạng thái · Ngày tạo** (`:1875`) | Có đủ 4 cột | **Đủ** |
| Tab Đề xuất có cột **Người đề xuất** (`:1875`) | **KHÔNG có.** Bộ cột thực tế: Nội dung · Lĩnh vực · Thời gian mong muốn · Địa điểm mong muốn · SL dự kiến · Trạng thái · Ngày tạo · Hành động | **Thiếu** → ngoài phạm vi case, xem §Lỗi phát hiện thêm |
| Tab Đề xuất có Hành động **Xem · Tiếp nhận · Đánh dấu thực hiện** (`:1875`) | Với `cbnv_hn`, ô Hành động của **cả 2 dòng** đều là `—` (mã nguồn ô: `<span style="color: rgb(153,153,153);">—</span>`, 0 nút). Màn chi tiết cũng chỉ có nút **"Quay lại danh sách"** | **Thiếu** → ngoài phạm vi case, xem §Lỗi phát hiện thêm |
| DN/NHT **sửa/xóa được** khi còn ở trạng thái Mới (`:1053`) | Dòng mới hiện đúng 2 nút **Sửa** · **Xóa** cho người gửi; dòng cũ (Đã tiếp nhận) hiện `—` | **Đủ** |
| **[SRS chưa quy định]** Nội dung thông báo thành công | Thực tế: *"Đề xuất đào tạo đã được gửi thành công"* (1 khung, không lặp) | — |
| **[SRS chưa quy định]** DN/NHT có màn xem lại đề xuất của mình không | Thực tế **CÓ** — tab "Đề xuất đào tạo" hiển thị cho cả vai trò DN, và **chỉ** đề xuất của chính DN đó | — |

**Ghi chú 1 — chênh tên trạng thái:** SRS `srs-v3.5.md:2665` đặt tên hằng là `MOI`, phần mềm dùng `MOI_GUI`, nhãn hiển thị **"Mới gửi"**. Đây là chênh **cách đặt tên nội bộ**, không phải chênh nghiệp vụ: yêu cầu là "đề xuất được tạo ở trạng thái Mới" và nhãn người dùng nhìn thấy đúng là "Mới gửi". Theo quy tắc *mô tả yêu cầu, không áp đặt cách hiện thực*, **không log thành lỗi**; chỉ ghi nhận tại đây.

---

## Phép đo — 2 phương pháp, không mâu thuẫn

**Bộ bắt thông báo:** chỉ dùng `tools/toast-capture.js` (không lọc trùng, đọc bằng `innerText`, đếm request song song). **Tự kiểm trước khi tin số liệu:** `soObserverDangSong = 1` ⇒ số liệu hợp lệ.

| Phép đo | Kết quả |
|---|---|
| **Số request kèm số thông báo** (thao tác Gửi) | `SO_REQUEST = 1` (`POST /api/v1/de-xuat-dao-taos`) · `SO_KHUNG_THONG_BAO = 1` · nội dung `"Đề xuất đào tạo đã được gửi thành công"` · `BI_LAP = false` ⇒ **không có lỗi thông báo lặp** ở luồng này |
| **Phản hồi máy chủ của chính thao tác Gửi** | `201` · `id b69a9545-59e4-4121-9760-91be29b65c19` · `trangThai "MOI_GUI"` · `nguoiDeXuatId 996cc5db…` · `donViId 00000000-0000-4000-8002-000000000001` · `ngayTao 2026-08-03T09:22:39.183Z` |
| **Phương pháp 1 — giao diện** (người gửi) | Ngay sau khi hộp thoại đóng: bảng chuyển từ `Hiển thị 1-1 / 1 kết quả` → `Hiển thị 1-2 / 2 kết quả`, dòng mới đứng đầu. Sau **tải lại trang bỏ qua bộ nhớ đệm**: vẫn `1-2 / 2`, badge "Mới gửi" |
| **Phương pháp 2 — hỏi thẳng máy chủ** (cookie-auth, `cache:'no-store'`) | `GET /api/v1/de-xuat-dao-taos` → `total = 2`, có đúng bản ghi `b69a9545…` `trangThai MOI_GUI` |
| **Đối chiếu 2 phương pháp** | **Khớp nhau** (2 = 2, cùng trạng thái). Không có ca "giao diện rỗng mà máy chủ có dữ liệu" hay ngược lại ⇒ không rơi vào tình huống phải dừng hỏi user |
| **Dấu vết đúng như dev khai** | Sau `POST` quan sát thấy **2 lần** gọi lại danh sách (`GET …/de-xuat-dao-taos` → `200` rồi `304`) = đúng cơ chế "double-refresh (invalidate + refetch)" dev mô tả ⇒ lời khai của dev **có bằng chứng quan sát được**, không phải chỉ là lời nói |

---

## Verdict theo từng ý (case gộp nhiều ý)

| # | Ý | Kết luận | Căn cứ |
|:-:|---|---|---|
| **1** | Đề xuất có hiện ở tab "Đề xuất đào tạo" của CB NV **đúng đơn vị tiếp nhận** không? | **ĐẠT** | `cbnv_hn` (mã đơn vị trùng khít bản ghi) thấy đúng đề xuất, badge "Mới gửi" — đúng `srs-fr-03:1043` + `:1875` |
| **2** | Người gửi (DN) có màn xem lại đề xuất của mình không? | **ĐẠT — không còn tranh chấp** | SRS **silent** về màn này (`srs-v3.5.md:1309` cấp quyền logic, `:1375` nói rõ không phải quyền giao diện; grep toàn bộ v3.5 không có SCR nào). **Nhưng phần mềm ĐÃ cung cấp**: DN thấy tab "Đề xuất đào tạo" chứa đúng đề xuất của mình, kèm Sửa/Xóa. Kỳ vọng của đối tác **được đáp ứng** ⇒ không có bất đồng đặc tả nào cần BA chốt ⇒ **không gán `BA confirm`** |
| **3** | Đề xuất được tạo ở trạng thái "Mới" chưa? | **ĐẠT** | Badge "Mới gửi", lọc tab "Mới gửi" ra đúng 1 kết quả |
| **4** | CB NV đơn vị tiếp nhận có nhận thông báo không? | **ĐẠT** | Thông báo "Đề xuất đào tạo mới", trùng giây với giờ tạo bản ghi |
| **5** | Có hiện thông báo gửi thành công cho người gửi không? | **ĐẠT** | 1 request → đúng 1 khung thông báo, không lặp |

**Không ý nào lỗi + không ý nào còn SRS silent gây tranh chấp** ⇒ **Verdict tổng = `Pass`**.

### Vì sao `Pass` chứ không phải "không tái hiện được"

Đây **không** phải ca "chạy thử không thấy lỗi rồi kết luận". QA **chứng minh dương tính** toàn bộ chuỗi trên bản dựng hiện tại: tạo bản ghi mới → nhận `201` kèm mã bản ghi → trạng thái đúng → danh sách người gửi tự cập nhật **không cần thao tác** → còn nguyên sau khi tải lại trang bỏ qua bộ nhớ đệm → cán bộ đúng đơn vị thấy được → cán bộ nhận thông báo. Kèm theo, cơ chế dev khai (double-refresh) **quan sát được trực tiếp** trong dấu vết mạng.
⇒ Đúng định nghĩa `Pass` = *dev đã fix, nay chạy đúng*, không phải `Resolved` = *không tái hiện được*. Vì vậy **không rơi vào** quy tắc "dừng hỏi user khi tab tuần 2 thiếu lựa chọn `Resolved`".

### Vì sao không phải `Reject`

Dù màn đối tác đứng ("Kế hoạch đào tạo") không phải nơi chứa đề xuất, QA **không** kết luận đối tác thao tác/hiểu sai: (i) dev đã tự nhận có sửa mã và deploy lại, tức phía dev thừa nhận có vấn đề; (ii) chuyên trang là bản triển khai khác, QA không kiểm được nên không phủ nhận được quan sát của họ. Theo quy trình, `Reject` chỉ dùng khi **chứng minh** được báo cáo vô hiệu — ở đây không chứng minh được, nên dùng `Pass`.

---

## Lỗi phát hiện thêm ngoài phạm vi case (dựa trên ảnh ĐÃ MỞ ĐỌC)

> Đây là các quan sát **ngoài** tiêu chí của QLDXDTTH_01. Ghi lại theo đúng yêu cầu "bug ngoài phạm vi cũng phải log", **không** gộp vào verdict của case này.

| # | Quan sát | Đo bằng 2 phương pháp? | Đánh giá |
|:-:|---|---|---|
| **1** | **Tab "Đề xuất đào tạo" thiếu cột "Người đề xuất"** mà `srs-fr-03-dao-tao.md:1875` liệt kê. Bộ cột thực tế 8 cột (Nội dung · Lĩnh vực · Thời gian mong muốn · Địa điểm mong muốn · SL dự kiến · Trạng thái · Ngày tạo · Hành động). Màn chi tiết cũng không hiện người đề xuất | Có — đọc `thead th` bằng mã + đối chiếu pixel ảnh `…-07…png` (đã cuộn hết thanh ngang, xác nhận không phải cột bị khuất) | **Lỗi thật, lệch SRS rõ.** Ảnh hưởng: cán bộ không biết đề xuất của ai khi nhìn danh sách |
| **2** | **Cán bộ nghiệp vụ đúng đơn vị tiếp nhận không có thao tác "Tiếp nhận"** — ô Hành động của mọi dòng đều `—` (0 nút), màn chi tiết chỉ có "Quay lại danh sách". `srs-fr-03:1875` yêu cầu Hành động *Xem · Tiếp nhận · Đánh dấu thực hiện*; `:1045` ghi *"CB NV tiếp nhận"* | Có — đọc mã nguồn ô (`0 nút`) + pixel ảnh `…-07…png` và `…-08…png`. Máy chủ **có sẵn** các đầu việc `/receive`, `/process`, `/complete`, `/reject` | ⚠️ **Cần BA chốt trước khi quy lỗi.** Có **mâu thuẫn trong chính SRS**: ma trận phân quyền `srs-v3.5.md:1309` chỉ cấp `R*` (chỉ đọc) cho `CB_NV_DP`, **không** cấp quyền sửa cho bất kỳ vai trò cán bộ nào — trái với `:1045`/`:1875`. Không log thành lỗi dứt khoát, phải hỏi BA |
| **3** | **Vai trò Cán bộ nghiệp vụ vẫn thấy nút "Gửi đề xuất mới"** trên tab Đề xuất, trong khi `srs-fr-03:1047` ghi Tác nhân là **DN / NHT**, và ma trận `srs-v3.5.md:1309` không cấp quyền tạo (`C`) cho vai trò cán bộ nào | Có — nút hiện trong cây trợ năng **và** trong pixel ảnh `…-07…png`. Chưa bấm thử để tránh sinh dữ liệu rác | Lệch SRS ở mức **hiển thị**. Cần kiểm thêm máy chủ có chặn không |
| **4** | **Lộ mã kỹ thuật ra giao diện người dùng:** ô chọn lĩnh vực trong form hiện `DAN_SU - Dân sự`, `THUE - Thuế`, `LAO_DONG - Lao động`… và màn chi tiết cũng hiện `Lĩnh vực: DAN_SU - Dân sự`. Trong khi cột "Lĩnh vực" của bảng lại hiện đúng `Dân sự` | Có — pixel ảnh `…-02…png` (form) + `…-08…png` (chi tiết), đối chiếu với bảng danh sách hiện tên sạch | Lỗi hiển thị mức nhẹ, nhưng lộ ra người dùng cuối |
| **5** | **Thông báo "Đề xuất đào tạo mới" dùng biểu tượng lỗi (dấu ✗ đỏ)** trong khi đây là thông báo thông tin bình thường; các thông báo khác cùng danh sách dùng dấu ✓ | Có — pixel ảnh `…-06…png` (thấy rõ vòng tròn đỏ) + đọc lớp biểu tượng bằng mã: `anticon-close-circle` cho dòng này, `anticon-check-circle` cho 4 dòng còn lại | Lỗi hiển thị mức nhẹ, gây hiểu nhầm là có sự cố |

---

## Ảnh đã chụp — TẤT CẢ đều đã mở đọc lại pixel

Thư mục: `../bug-reports/dao-tao/image/`

| Tệp | Nội dung đã đọc được từ pixel |
|---|---|
| `BUG-QLDXDTTH_01-01-baseline-DN-tab-de-xuat.png` | Trước khi gửi. Vai trò `QA UAT Kiem Thu DN` · `DN`, bản dựng `HTPLDN · V1.0.5`. Tab "Đề xuất đào tạo", `Hiển thị 1-1 / 1 kết quả` |
| `BUG-QLDXDTTH_01-02-form-truoc-khi-gui.png` | Hộp thoại "Gửi đề xuất đào tạo" đã nhập đủ 5 trường. Thấy `DAN_SU - Dân sự` (quan sát thêm #4) |
| `BUG-QLDXDTTH_01-03-ngay-sau-khi-bam-gui.png` | **Ngay sau khi bấm Gửi, chưa tải lại trang:** `Hiển thị 1-2 / 2 kết quả`, dòng `QA-VERIFY-0803…` đứng đầu kèm nút `Sửa` `Xóa` |
| `BUG-QLDXDTTH_01-04-DN-sau-tai-lai-trang-van-hien-Moi-gui.png` | **Sau khi tải lại trang bỏ qua bộ nhớ đệm:** vẫn `1-2 / 2`, bản ghi còn nguyên |
| `BUG-QLDXDTTH_01-05-DN-loc-tab-Moi-gui-thay-de-xuat-vua-gui.png` | Lọc tab "Mới gửi": đúng 1 kết quả, badge **"Mới gửi"**, Ngày tạo **03/08/2026**, nút `Sửa` `Xóa` |
| `BUG-QLDXDTTH_01-06-CBNV-nhan-thong-bao-de-xuat-moi.png` | Vai trò `QA CB Nghiep vu Ha Noi` · `CB_NV_DP`. Hộp thông báo: **"Đề xuất đào tạo mới — Có đề xuất đào tạo mới từ người dùng QA UAT Kiem Thu DN — 4 phút trước"**. Thấy biểu tượng ✗ đỏ (quan sát thêm #5) |
| `BUG-QLDXDTTH_01-07-CBNV-tab-de-xuat-thay-de-xuat-Moi-gui.png` | Cán bộ đúng đơn vị thấy đề xuất, badge "Mới gửi" 03/08/2026. Thấy ô Hành động `—` (quan sát thêm #2) + nút "Gửi đề xuất mới" (quan sát thêm #3) + thiếu cột Người đề xuất (quan sát thêm #1) |
| `BUG-QLDXDTTH_01-08-CBNV-man-chi-tiet-khong-co-nut-Tiep-nhan.png` | Màn chi tiết `/dao-tao/de-xuat/b69a9545…` phía cán bộ: chỉ có nút "Quay lại danh sách"; `Lĩnh vực: DAN_SU - Dân sự` |

## Tài khoản đã dùng

| Vai trò | Tài khoản | Ghi chú |
|---|---|---|
| Người gửi (đúng vai trò đối tác) | **`0109998887`** / `Test@1234` — `QA UAT Kiem Thu DN`, vai trò `DN` | Không dùng `admin` để ra verdict |
| Người phải thấy đề xuất | **`cbnv_hn`** / `Test@1234` — `QA CB Nghiep vu Ha Noi`, vai trò `CB_NV_DP` | Mã đơn vị trùng khít mã đơn vị tiếp nhận của bản ghi |

Không tài khoản nào bị khoá, không phải áp dụng quy tắc dự phòng tài khoản. Đổi vai trò bằng cách thoát phiên đúng cách + xoá dữ liệu phiên trước khi đăng nhập lại, tránh nhiễm quyền.

## Dữ liệu để lại trên môi trường

Bản ghi test `b69a9545-59e4-4121-9760-91be29b65c19` — nội dung bắt đầu bằng `QA-VERIFY-0803`, trạng thái **Mới gửi**, thuộc DN `QA UAT Kiem Thu DN`, đơn vị `00000000-0000-4000-8002-000000000001`. **Chưa xoá** để dev/BA soi lại được. Xoá được bằng nút "Xóa" ở vai trò DN.
