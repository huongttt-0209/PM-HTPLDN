# QLHDTVVCG_13 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 319 · **Mô tả (G):** Kiểm tra khi nhấn nút chức năng Thêm hợp đồng
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "+ Thêm hợp đồng"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — FR-X.3-01 (Inputs + Processing) và §3 SCR-X3-01

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống mở màn hình biểu mẫu ở chế độ "Thêm mới" **với các trường trống**" | `srs-fr-14-hop-dong-tv.md:279`, `:290` + cột **Mặc định** của bảng Inputs `:82`, `:84`–`:92` (đều là `—`, tức không có giá trị khởi tạo) | **MATCH** | TEST | **UI:** bấm nút thêm hợp đồng → biểu mẫu mở ra; đọc `value` của các ô nhập người dùng (Tên / Bên B / Giá trị / Thời hạn bắt đầu / Thời hạn kết thúc / Nội dung / Ghi chú) phải rỗng. **Đối chứng:** `list_network_requests` — không có request đọc bản ghi hợp đồng nào (chứng minh là chế độ tạo mới, không phải mở nhầm bản ghi cũ) |
| **C2** | "…trường **"Mã hợp đồng"** được hệ thống **tự điền**" (ngay khi mở biểu mẫu) | **MÂU THUẪN**: `:290` ghi trường "Mã (auto)" trên biểu mẫu và `:81` ghi Mặc định `auto-gen`, nhưng `:119` xếp việc sinh mã vào **bước xử lý khi Thêm mới**, tức lúc lưu. Đặc tả **không nói thời điểm** mã xuất hiện | **GAP** | **BA** | Chỉ đo hiện trạng (ô Mã có sẵn giá trị lúc mở form hay không) để mô tả cho BA. **CẤM Pass/Reopen vế này** |
| **C3** | "…và **"Bên A"** được hệ thống tự điền" | `srs-fr-14-hop-dong-tv.md:83` (Mặc định `auto đơn vị`, Nguồn `hệ thống`) + `:290` ("Bên A (auto đơn vị)") | **MATCH** | TEST | **UI:** đọc `innerText`/`value` ô Bên A ngay khi biểu mẫu vừa mở — phải có sẵn tên đơn vị của tài khoản đang đăng nhập. **Đối chứng:** so chuỗi đó với tên đơn vị lấy từ hồ sơ tài khoản qua API |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:81`** (Inputs — dòng mã hợp đồng)
```
| 1 | ma_hop_dong | text | Y (auto) | Format: HDTV-{YYYYMMDD}-{SEQ} | auto-gen | hệ thống |
```

**`srs-fr-14-hop-dong-tv.md:83`** (Inputs — dòng Bên A)
```
| 3 | ben_a | text | Y | Bên A (đơn vị quản lý) | auto đơn vị | hệ thống |
```

**`srs-fr-14-hop-dong-tv.md:82`** + **`:84`–`:92`** (Inputs — các trường người dùng nhập, cột **Mặc định** đều `—`)
```
| 2 | ten_hop_dong | text | Y | — | — | người dùng nhập |
| 4 | ben_b | text | Y | Bên B (TVV/Tổ chức tư vấn/Chuyên gia) | — | người dùng nhập |
| 5 | tvv_id | identifier | N | FK -> TU_VAN_VIEN (liên kết nếu có; có thể trỏ đến TVV hoặc CG, xác định qua TU_VAN_VIEN.loai_tvv) | — | người dùng chọn |
| 6 | gia_tri_hop_dong | money | Y | Giá trị HĐ | — | người dùng nhập |
| 7 | thoi_han_bat_dau | date | Y | — | — | người dùng chọn |
| 8 | thoi_han_ket_thuc | date | Y | >= thoi_han_bat_dau | — | người dùng chọn |
| 9 | noi_dung | text (long) | N | Nội dung tóm tắt HĐ | — | người dùng nhập |
| 10 | vu_viec_ids | identifier[] | N | FK[] -> VU_VIEC (many-to-many) | — | người dùng chọn |
| 11 | ghi_chu | text (long) | N | — | — | người dùng nhập |
| 12 | file_dinh_kem | file[] | N | Upload nhiều file | — | người dùng upload |
```

**`srs-fr-14-hop-dong-tv.md:119`** (Processing FR-X.3-01, bước 2 — **vế C2 mâu thuẫn ở đây**)
```
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
```
> Đây là **bước xử lý** của giao dịch Thêm mới (cùng bảng với bước 5 "Tạo hoặc cập nhật bản ghi"), hàm ý sinh mã **khi lưu**. Đối chọi với `:290` khai "Mã (auto)" như một **trường trên biểu mẫu**. Đặc tả **không phát biểu** mã phải hiện ngay lúc mở biểu mẫu ⇒ `GAP`.

**`srs-fr-14-hop-dong-tv.md:290`**
```
| 6 | content (form) | Thông tin chung | form | Mã (auto) / Tên (bắt buộc) / Bên A (auto đơn vị) / Bên B (bắt buộc + TVV dropdown) / Giá trị (bắt buộc) / Thời hạn bắt đầu (bắt buộc) / Thời hạn kết thúc (bắt buộc, >= bắt đầu) / Nội dung / Ghi chú / File đính kèm | input -> validate | trang thêm/sửa — **CHỈ vai trò CB NV; TVV/CG không truy cập trang form** |
```

**`srs-fr-14-hop-dong-tv.md:286`** (nút mở biểu mẫu — điều kiện hiển thị theo vai trò)
```
| 2 | toolbar | Tiêu đề + nút | label + button | "Quản lý Hợp đồng Tư vấn" + [+ Thêm hợp đồng] [Xuất Excel] [Làm mới] | click -> action | luôn hiển thị; **nút [+ Thêm hợp đồng] CHỈ hiển thị với CB NV — ẩn với TVV/CG** |
```

**`srs-fr-14-hop-dong-tv.md:279`**
```
**Form thêm/sửa:** Trang mới với Accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký.
```

**`srs-fr-14-hop-dong-tv.md:514`** (BR-DATA-04 — khuôn mã)
```
| **Phát biểu** | Các entity nghiệp vụ có mã tự sinh theo format `PREFIX-YYYYMMDD-SEQ` (VD: HDTV-20260325-001) |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68` (CB NV — CRUD đầy đủ), `:286` (nút thêm **CHỈ** hiện với CB NV) và `:290` (**CHỈ** CB NV vào được trang biểu mẫu). Đo bằng TVV/CG thì không có nút ⇒ Fail oan | `:68`, `:286`, `:290` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234`. Ghi rõ **tên đơn vị** của tài khoản này trước khi đo — cần để đối chứng vế C3 | brief §3 |
| **Dữ liệu** | **Không cần seed.** Đây là kiểm tra trạng thái khởi tạo của biểu mẫu, không phụ thuộc dữ liệu sẵn có | `:82`–`:92` |
| **Kỷ luật thao tác** | Mở biểu mẫu bằng **một lần bấm duy nhất từ màn danh sách**, không mở bản ghi cũ trước đó trong cùng phiên — biểu mẫu có thể còn giữ giá trị của lần mở trước và làm C1 sai lệch | `:290` |
| **Không được lưu** | Phiếu này **dừng ở bước mở biểu mẫu**. **KHÔNG bấm Lưu** — hành vi lưu thuộc phiếu `_15`. Bấm Lưu ở đây sẽ sinh dữ liệu rác và làm nhiễu `_15` | bước J của phiếu |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Ô "Bên A" có chữ nhưng là chữ mờ gợi ý (placeholder), không phải giá trị thật.** C3 đòi hệ thống **tự điền**. Phải đọc `value` của ô nhập (hoặc nội dung ô chỉ-đọc), **không** đọc `placeholder`. Chữ mờ = **chưa** tự điền ⇒ Fail C3.
- **"Bên A" tự điền nhưng sai đơn vị.** Điền sẵn tên đơn vị bất kỳ vẫn "trông đúng". `:83` ghi "Bên A (đơn vị quản lý)" ⇒ phải là đơn vị của **tài khoản đang đăng nhập**. Bắt buộc đối chứng với hồ sơ tài khoản.
- **Biểu mẫu mở ra là bản ghi cũ ở chế độ sửa.** Nếu bấm nhầm hoặc ứng dụng điều hướng sai, các trường có sẵn dữ liệu sẽ bị đọc nhầm thành "đã tự điền". Đối chứng bằng `list_network_requests`: chế độ thêm mới **không** gọi API đọc bản ghi.
- **Kết luận C2 "đạt" vì thấy ô Mã có số.** C2 đã khóa `GAP` — **kết quả đo không được đổi quan hệ** (flow 04 luật khóa 5). Dù ô Mã có sẵn mã đúng khuôn, vẫn **không Pass** vế này; chỉ ghi hiện trạng cho BA.

**Dễ Fail oan:**
- **Fail vì ô "Mã hợp đồng" trống lúc mở biểu mẫu.** Đây chính là điểm `GAP`: `:119` xếp việc sinh mã vào bước xử lý khi lưu. Ô Mã trống lúc mở form **có thể là đúng đặc tả** ⇒ **không Fail**, chuyển BA.
- **Fail vì nhãn nút không phải "+ Thêm hợp đồng".** `:286` ghi `[+ Thêm hợp đồng]`, còn Phụ lục E §H4 (`srs-v3.5.md:6756`) bắt nút thêm mới luôn là **"Thêm mới"** — hai dòng của chính đặc tả lệch nhau. Phiếu này chấm **màn hình mở ra sau khi bấm**, không chấm nhãn nút ⇒ không Fail; đưa vào câu hỏi BA gộp.
- **Fail vì biểu mẫu là ngăn kéo/hộp thoại chứ không phải trang mới.** `:272` khai rõ "Form (**trang moi/modal/drawer**)" — cả ba hình thức đều hợp lệ.
- **Fail vì các nhóm 2/3/4 (Vụ việc liên kết / Mốc tiến độ / Thanh toán) đang trống.** Ở chế độ Thêm mới các nhóm này **phải** trống; cột K của phiếu này cũng chỉ nói tới "các trường trống".
- **Fail vì thiếu trường `so_hop_dong` / `ngay_ky`.** Hai trường này có ở phần thực thể (`:385`, `:390`) nhưng **không** được liệt kê ở `:290`. Thiếu chúng trên biểu mẫu ⇒ ghi nhận cho BA, không Fail.
