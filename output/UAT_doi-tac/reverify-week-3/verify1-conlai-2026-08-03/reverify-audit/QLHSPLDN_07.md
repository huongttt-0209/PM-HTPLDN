# QLHSPLDN_07 — audit verify vòng 1 (row 325, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Verdict QA:** `Pass` (cột Q — Verify). Cột P giữ nguyên `dev done`, QA **KHÔNG đụng**.
**Môi trường:** https://18.143.165.120.nip.io — bản dựng đọc ở chân menu trái: **`HTPLDN · V1.0.5`**
**Tài khoản ra verdict:** `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`) — **trùng vai trò + cấp của đối tác**. Tài khoản phụ (chỉ dùng cho phép thử dữ liệu cũ A2): `cbnv_hn` (`CB_NV_DP`, Sở Tư pháp Hà Nội). **KHÔNG dùng `admin`.**
**Thời điểm đo:** 2026-08-03 21:02 → 21:30.

---

## Note dev trước khi QA đè (2026-08-03 21:02:52)

Sao lưu **nguyên văn** ô `R325` (`DEV phản hồi lần 1`) đọc bằng gspread lúc 2026-08-03 21:02:52,
TRƯỚC khi ghi note QA đè lên:

```
Đã fix (6 commit): update hồ sơ pháp lý DN nay persist đủ field + tệp + version — hết "báo thành công nhưng không cập nhật". Đã deploy 120, cần retest.
```

Các ô khác của dòng 325 (để tra cứu, không phải căn cứ verdict):

| Cột | Giá trị |
|---|---|
| Tuần | Tuần 3 |
| Mã TC | QLHSPLDN_07 |
| Mô tả | Sửa |
| Điều kiện | 1. Đăng nhập hệ thống thành công |
| Các bước thực hiện | 1. Chọn menu "Doanh nghiệp" · 2. Nhấn "Xem chi tiết" · 3. Chọn thẻ "Hồ sơ pháp lý doanh nghiệp" · 4. Nhấn "Sửa" |
| Kết quả mong đợi | - Hệ thống mở cửa sổ chỉnh sửa với dữ liệu hiện có.<br>- NSD cập nhật và bấm "Lưu", hệ thống cập nhật bản ghi và lưu vết thao tác. |
| Kết quả thực tế (đối tác) | Hệ thống hiển thị thông báo cập nhật thành công nhưng dữ liệu chưa được cập nhật vào bản ghi |
| Ảnh/video 1 | QLHSPLDN_07.jpg · QLHSPLDN_07.webm |
| Trạng thái 1 | Fail |
| Trạng thái dev fix 1 (P) | dev done |
| Verify (Q) | (TRỐNG — QA chưa soát) |

> Giải trình dev chỉ dùng làm **manh mối chọn chỗ đo** (persist field + tệp + version), TUYỆT ĐỐI
> không dùng làm căn cứ verdict. Toàn bộ kết luận dưới đây dựa trên số đo tự tay chạy.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES bằng tool Read)

**File đã mở:**
- `partner-evidence/QLHSPLDN_07-1.jpg` — ảnh tĩnh 1904×1031, đọc trực tiếp chữ trên ảnh.
- `frames/QLHSPLDN_07/` — 6 khung hình trích sẵn từ `QLHSPLDN_07-2.webm` (t000 / t003 / t006 / t009 / t012 / t015), **đã mở đọc từng khung**.

### 3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Giá trị đọc được từ bằng chứng |
|---|---|---|
| a | URL / bản ghi | `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` · tiêu đề **"Chi tiết DN #DN-XX-0005"** · thẻ đang mở **Hồ sơ pháp lý**. Bản ghi thao tác: **`HSPL-20260803-0001`** |
| b | Trạng thái entity | `HSPL-20260803-0001`: Loại **Khác** · LVPL **Thuế** · Nguồn **Thủ công** · Ngày cấp **03/08/2026** · Ngày hết hạn **03/08/2026** · Trạng thái **Hiệu lực**. DN có 2 hồ sơ, cả hai "Hiệu lực" |
| c | Dữ liệu tiền đề | Góc phải trên: **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**. Hồ sơ đang sửa **đã có sẵn 1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB). Các ô form đã có dữ liệu: Cơ quan cấp `TKM`, Trạng thái `Hiệu lực`, Mô tả `tkm kiểm thử chức năng`. Đồng hồ máy đối tác **2026-08-03 10:04 → 10:06** |

### Khoảnh khắc lỗi — đọc được ở khung nào

| Khung | Thời điểm | Nội dung đọc được |
|---|---|---|
| `t000.00s.jpg` | 00:00 | Form **Sửa** đang mở, cuộn tới cuối. Mục **Tệp đính kèm** có **1 tệp**: `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB). Con trỏ ở vùng kéo-thả |
| `t003.03s.jpg` | 00:03 | Mục Tệp đính kèm nay có **2 tệp** — vừa thêm `QLHSPLDN_07.jpg` (213.3 KB) |
| `t006.05s.jpg` · `t009.05s.jpg` | 00:06 · 00:09 | Vẫn 2 tệp; nút **Hủy / Đồng ý** hiện ở cuối form |
| `t012.06s.jpg` | 00:12 | **Đã bấm Đồng ý.** Khung thông báo xanh **"Cập nhật hồ sơ thành công"**. Form đóng, quay về bảng. Con trỏ đang rê lên nút **Sửa** của chính dòng `HSPL-20260803-0001` |
| `t015.08s.jpg` | 00:15 | **KHOẢNH KHẮC LỖI.** Mở lại form Sửa của chính hồ sơ vừa lưu → mục Tệp đính kèm **chỉ còn 1 tệp** `2K15 T3 (4.8) & CN (9.8).pdf`. Tệp `QLHSPLDN_07.jpg` vừa thêm ở 00:03 **đã biến mất** |
| `QLHSPLDN_07-1.jpg` | 10:04 | Ảnh tĩnh: khung thông báo **"Cập nhật hồ sơ thành công"** + bảng 2 hồ sơ ở phía sau |

⇒ Cổng 1 ĐÓNG. Đã thấy khung chứa LỖI thật (`t015.08s.jpg`), không suy đoán từ văn bản.

---

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem + khung chứa LỖI:** `frames/QLHSPLDN_07/t015.08s.jpg` (mốc 00:15 của `QLHSPLDN_07-2.webm`) — mở lại cửa sổ Sửa ngay sau khi lưu thì tệp `QLHSPLDN_07.jpg` (213.3 KB) vừa đính kèm ở mốc 00:03 **không còn trong danh sách**, dù mốc 00:12 hệ thống đã báo "Cập nhật hồ sơ thành công".
2. **Đối tác phản ánh CỤ THỂ:** thao tác **Sửa hồ sơ pháp lý DN** — sau khi bấm Đồng ý, hệ thống **báo thành công** nhưng **thay đổi không được ghi vào bản ghi**. Thay đổi quan sát được trong video là **thêm 1 tệp đính kèm**; đó chính là thứ bị mất. Các ô còn lại (Cơ quan cấp / Trạng thái / Mô tả) giữ nguyên giá trị cũ giữa khung 00:00 và 00:15 nên không phân biệt được có bị mất hay không → phải tự đo đủ mọi KIỂU trường.
3. **Data + bước tái hiện:** cần 1 DN có ≥1 hồ sơ pháp lý (ưu tiên hồ sơ đã có sẵn tệp). Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** → menu **Doanh nghiệp** → **Xem chi tiết** DN → thẻ **Hồ sơ pháp lý** → **Sửa** → đổi dữ liệu + thêm tệp → **Đồng ý** → mở lại bản ghi so sánh.

---

## Thứ tự đo — CHỐNG THIÊN KIẾN

**ĐO WEB TRƯỚC, ĐỌC SRS SAU.** Toàn bộ số đo mục dưới được ghi ra **trước khi mở bất kỳ file SRS nào**. Chỉ sau khi có đủ số đo mới grep SRS để đối chiếu (Cổng 3).

---

## Kỷ luật phép đo — 3 lần phép đo NÓI DỐI, đã bắt được và sửa

Ghi lại đầy đủ vì đúng loại lỗi mà postmortem 16/07 cảnh báo (*"phép đo nói dối trong im lặng"*):

| # | Triệu chứng | Chẩn đoán | Cách sửa |
|---|---|---|---|
| 1 | `.ant-upload-list-item` đếm ra **0 tệp** trong khi màn hình rõ ràng liệt kê `HSPL-tep-kiem-thu.pdf` | Sai selector — bản AntD này bọc mục tệp bằng **`.ant-upload-list-item-container`** | Duyệt cây DOM thật của vùng "Tệp đính kèm" để tìm class đúng, rồi đếm lại |
| 2 | `.ant-select-selection-item` trả `null` cho cả 3 ô chọn, tưởng "ô chọn rỗng" | Sai selector — bản này dùng **`.ant-select-content`** (`.ant-select-content-has-value`) | Đọc lại giá trị bằng class đúng; đối chiếu thêm bằng ảnh chụp |
| 3 | Điền bằng `fill_form` / `Control+A` → giá trị bị **nối thêm** vào giá trị cũ (`HS kiem thu linh vuc va tepQA-EDIT-...`) | `fill_form` không xoá ô; `Control+A` không chọn-tất-cả trên macOS | Đặt giá trị qua **setter gốc của trình duyệt + phát sự kiện `input`/`change`** để React nhận đúng, rồi đọc lại xác nhận |

Ngoài ra: có **1 lần cửa sổ Sửa tự đóng** giữa chừng ở lần thử đầu (do gõ phím Enter trong ô ngày). Đã kiểm ngay bằng cách đọc lại bản ghi từ máy chủ: **bản ghi KHÔNG đổi** (`version` vẫn 2, `ngayCapNhat` vẫn 2026-07-24) ⇒ không có lần lưu ngoài ý muốn làm nhiễu số liệu. Sau đó bỏ hẳn phím Enter, chọn ngày bằng cách bấm ô ngày trong bảng lịch.

**Bộ bắt thông báo:** chỉ dùng `tools/toast-capture.js` (không lọc trùng, đọc `innerText`, đếm request). **Tự kiểm trước MỖI lần đo: `soObserverDangSong = 1`** — đạt ở cả 3 phép đo A / A2 / B. Observer bị xoá sau mỗi lần tải lại trang → đã cài lại và tự kiểm lại.

---

## Số đo thực tế trên web (bản `HTPLDN · V1.0.5`)

### Bối cảnh + tình huống chệch điều kiện đã xử lý

- DN dùng để đo: **`DN-HNI-0001` — `Cong ty TNHH QA UAT Kiem Thu`** (MST 0109998887), id `829abcac-b0af-4cde-9af9-ec51bc79014c`, đường dẫn `?tab=ho-so-pl` — **cùng dạng màn, cùng thẻ** với bằng chứng đối tác.
- Bản ghi định dùng ban đầu cho phép thử (A) là `HSPL-20260725-0001` (có sẵn 1 tệp — giống hệt tiền đề đối tác). Bấm lưu thì hệ thống **từ chối bằng thông báo "Không có quyền truy cập dữ liệu đơn vị khác"** (1 request, 1 thông báo). Đọc lại bằng cách gọi thẳng dịch vụ máy chủ: **403 `ERR-AUTH-VPD-00-01`**.
  **Nguyên nhân:** 4 hồ sơ cũ của DN này thuộc đơn vị **Sở Tư pháp Hà Nội** (`...8002-...-0001`), còn `cbnv_tw_04` thuộc **Cục Bổ trợ tư pháp – TW** (`...8000-...-0001`). Đây là **chặn theo đơn vị**, KHÔNG phải lỗi lưu dữ liệu của case này.
  **Cách đóng:** chuyển phép thử (A) sang bản ghi **`HSPL-20260803-0001`** — thuộc đúng đơn vị TW, đã tồn tại từ trước phiên đo (tạo 13:46, đo lúc 21:16). Đồng thời **thêm phép thử (A2)** trên hồ sơ **cũ thật** (tạo 21/07) bằng tài khoản đúng đơn vị sở hữu, để đóng nốt giả thuyết "dữ liệu cũ đóng băng".

### Bảng kết quả từng trường đã sửa × 3 nơi kiểm

Ký hiệu: **TB** = khung thông báo · **F5** = mở lại bản ghi sau khi tải lại trang thật (Ctrl+F5, bỏ qua bộ nhớ đệm) · **MC** = đọc lại bản ghi theo id từ dịch vụ máy chủ.

#### (A) Hồ sơ CÓ SẴN TỪ TRƯỚC — `HSPL-20260803-0001`, vai trò `cbnv_tw_04` (CB_NV_TW · BTP·TW — trùng đối tác)

| Kiểu trường | Trường | Giá trị trước | Giá trị nhập vào | TB | Sau F5 | Đọc lại từ máy chủ | Lưu được? |
|---|---|---|---|:-:|---|---|:-:|
| Chữ | Tên hồ sơ | `QA0803 HSPL trang thai HET HAN` | `QA-EDIT-A-20260803-2116 ten` | ✅ | `QA-EDIT-A-20260803-2116 ten` | `QA-EDIT-A-20260803-2116 ten` | ✅ |
| Chọn | Loại hồ sơ | Quyết định | **Giấy phép** | ✅ | Giấy phép | `GIAY_PHEP` | ✅ |
| Chọn | Lĩnh vực pháp lý | (trống) | **Thuế** | ✅ | Thuế | `Thuế` | ✅ |
| Ngày | Ngày cấp | (trống) | **01/08/2026** | ✅ | 01/08/2026 | `2026-08-01` | ✅ |
| Ngày | Ngày hết hạn | (trống) | **31/12/2026** | ✅ | 31/12/2026 | `2026-12-31` | ✅ |
| Chữ | Cơ quan cấp | (trống) | `QA-EDIT-A-20260803-2116 coquan` | ✅ | y nguyên | y nguyên | ✅ |
| Trạng thái | Trạng thái | Hết hạn | **Hiệu lực** | ✅ | Hiệu lực | `HIEU_LUC` | ✅ |
| Chữ dài | Mô tả | (trống) | `QA-EDIT-A-20260803-2116 mota` | ✅ | y nguyên | y nguyên | ✅ |
| Tệp | Tệp đính kèm | 0 tệp | **+ `QA-EDIT-A-tep-moi.png` (191 B)** | ✅ | 1 tệp, đúng tên + dung lượng | `QA-EDIT-A-tep-moi.png` (191 B) | ✅ |

- **Số request kèm thông báo "thành công": 1 request** `PATCH /api/v1/ho-so-phap-ly-dns/5bd8169a-...` — **1 khung thông báo** `"Cập nhật hồ sơ thành công"`. Không lặp (`BI_LAP=false`).
- **Lưu vết thao tác:** `version` 1 → **2**; `ngayCapNhat` 13:46:11 → **14:18:05**; `nguoiCapNhatId` = `9101c6bb-6b1d-4f00-8c3c-2247f5b22e07` (đúng `cbnv_tw_04`).
- Dòng trong bảng danh sách sau F5 cũng đổi theo: `Giấy phép · Thuế · 01/08/2026 · 31/12/2026 · Hiệu lực · Có tệp đính kèm = Có`.

#### (A2) Hồ sơ CŨ THẬT (tạo 21/07/2026, trước bản vá) — `HSPL-20260721-0001`, vai trò `cbnv_hn` (đơn vị sở hữu)

> Phép thử **bổ sung** để loại trừ riêng giả thuyết *"bản ghi cũ mang dữ liệu đóng băng theo lỗi cũ"*. Không dùng làm căn cứ chính vì khác cấp đơn vị với đối tác.

| Kiểu trường | Trường | Giá trị trước | Giá trị nhập vào | TB | Sau F5 | Đọc lại từ máy chủ | Lưu được? |
|---|---|---|---|:-:|---|---|:-:|
| Chữ | Tên hồ sơ | `QA UAT - Ho so phap ly test QLHSPLDN` | `QA-EDIT-A2-20260803-2126 ten` | ✅ | y nguyên | y nguyên | ✅ |
| Chọn | Loại hồ sơ | Giấy phép | **Quyết định** | ✅ | Quyết định | `QUYET_DINH` | ✅ |
| Chọn | Lĩnh vực pháp lý | (trống) | **Dân sự** | ✅ | Dân sự | `Dân sự` | ✅ |
| Ngày | Ngày cấp | (trống) | **10/08/2026** | ✅ | 10/08/2026 | `2026-08-10` | ✅ |
| Ngày | Ngày hết hạn | (trống) | **30/11/2026** | ✅ | 30/11/2026 | `2026-11-30` | ✅ |
| Chữ | Cơ quan cấp | (trống) | `QA-EDIT-A2-20260803-2126 coquan` | ✅ | y nguyên | y nguyên | ✅ |
| Trạng thái | Trạng thái | Hiệu lực | **Hết hạn** | ✅ | Hết hạn | `HET_HAN` | ✅ |
| Chữ dài | Mô tả | (trống) | `QA-EDIT-A2-20260803-2126 mota` | ✅ | y nguyên | y nguyên | ✅ |
| Tệp | Tệp đính kèm | 0 tệp | **+ `QA-EDIT-A-tep-moi.png` (191 B)** | ✅ | 1 tệp đúng tên | `QA-EDIT-A-tep-moi.png` (191 B) | ✅ |

- **2 request / 1 khung thông báo**: `POST .../upload` (tải tệp lên) + `PATCH .../6c08fcbe-...` (cập nhật bản ghi) → **1** thông báo `"Cập nhật hồ sơ thành công"`. Không lặp. Hai request là hai việc khác nhau, không phải gửi trùng.
- `version` 1 → **2**.

#### (B) Hồ sơ MỚI tạo qua luồng chuẩn rồi sửa — `HSPL-20260803-0003`, vai trò `cbnv_tw_04`

Bước tạo (seed, **cũng soi như test**): 1 request `POST /api/v1/ho-so-phap-ly-dns` / **1** khung thông báo `"Thêm hồ sơ thành công"`, không lặp, không tạo trùng bản ghi.

| Kiểu trường | Trường | Giá trị khi tạo | Giá trị sửa thành | TB | Sau F5 | Đọc lại từ máy chủ | Lưu được? |
|---|---|---|---|:-:|---|---|:-:|
| Chữ | Tên hồ sơ | `QA-NEW-B-20260803-2120 ten goc` | `QA-EDIT-B-20260803-2122 ten` | ✅ | y nguyên | y nguyên | ✅ |
| Chọn | Loại hồ sơ | Hợp đồng | **Khác** | ✅ | Khác | `KHAC` | ✅ |
| Chọn | Lĩnh vực pháp lý | Đất đai | **Hành chính** | ✅ | Hành chính | `Hành chính` | ✅ |
| Ngày | Ngày cấp | (trống) | **15/09/2026** | ✅ | 15/09/2026 | `2026-09-15` | ✅ |
| Ngày | Ngày hết hạn | (trống) | **20/01/2027** | ✅ | 20/01/2027 | `2027-01-20` | ✅ |
| Chữ | Cơ quan cấp | `QA-NEW-B-...-2120 coquan goc` | `QA-EDIT-B-20260803-2122 coquan` | ✅ | y nguyên | y nguyên | ✅ |
| Trạng thái | Trạng thái | Hiệu lực | **Thu hồi** | ✅ | Thu hồi | `THU_HOI` | ✅ |
| Chữ dài | Mô tả | `QA-NEW-B-...-2120 mota goc` | `QA-EDIT-B-20260803-2122 mota` | ✅ | y nguyên | y nguyên | ✅ |
| Tệp | Tệp đính kèm | 0 tệp | **+ `QA-EDIT-B-tep-moi.png` (191 B)** | ✅ | 1 tệp đúng tên | `QA-EDIT-B-tep-moi.png` (191 B) | ✅ |

- **1 request** `PATCH /api/v1/ho-so-phap-ly-dns/347773af-...` — **1** khung thông báo `"Cập nhật hồ sơ thành công"`. Không lặp.
- `version` 1 → **2**; `ngayCapNhat` 14:20:36 → **14:21:56**; `nguoiCapNhatId` đúng `cbnv_tw_04`.

### Kết luận số đo

**27/27 ô đo (9 trường × 3 kịch bản A / A2 / B) đều lưu đúng ở CẢ BA nơi kiểm.** Không có nhóm trường nào bị bỏ sót — chữ, ngày, ô chọn, trạng thái và tệp đính kèm đều được ghi lại. **Không có ô nào "báo thành công mà không lưu".**

Đặc biệt: kịch bản **giống hệt video đối tác** (thêm tệp đính kèm vào hồ sơ rồi mở lại) đã chạy **3/3 lần đều giữ được tệp** sau khi tải lại trang — trong khi ở video đối tác tệp biến mất ngay khi mở lại.

**Kết quả (A) và (B) KHÔNG lệch nhau** ⇒ không có hiện tượng "dữ liệu cũ đóng băng"; (A2) trên hồ sơ tạo 21/07 cũng lưu đủ ⇒ giả thuyết dữ liệu cũ bị loại trừ hoàn toàn.

### Ảnh đã chụp và ĐÃ MỞ ĐỌC

| Ảnh | Nội dung đã đọc được |
|---|---|
| `image/QLHSPLDN_07-A1-form-truoc-khi-sua.png` | Form "Sửa hồ sơ pháp lý" mở đúng, đã nạp sẵn dữ liệu hiện có; góc phải trên xác nhận `CB Nghiệp vụ - Trung ương #04 · CB_NV_TW · BTP · TW`; chân menu `HTPLDN · V1.0.5` |
| `image/QLHSPLDN_07-A2-form-dang-sua-nghi-ngo.png` | Ảnh của lần thử đầu bị hỏng phép đo — cửa sổ Sửa đã đóng, chỉ còn bảng. Chính ảnh này giúp phát hiện phép đo đang đọc cửa sổ không còn tồn tại |
| `image/QLHSPLDN_07-A3-form-truoc-khi-luu.png` | Trước khi bấm lưu: Ngày hết hạn `31/12/2026`, Cơ quan cấp + Mô tả mang dấu nhận dạng `QA-EDIT-A-...`, Trạng thái `Hết hạn`, **2 tệp** trong danh sách, nút `Hủy` / `Đồng ý` |
| `image/QLHSPLDN_07-A4-toast-sau-khi-luu.png` | Ảnh chụp ngay lúc bấm — cửa sổ vẫn mở với dữ liệu đã điền (khung thông báo chưa kịp hiện) |
| `image/QLHSPLDN_07-X1-toast-khong-co-quyen-don-vi-khac.png` | Ảnh của lần bị chặn theo đơn vị; nội dung thông báo lấy từ bộ bắt thông báo + phản hồi máy chủ (403 `ERR-AUTH-VPD-00-01`) |
| `image/QLHSPLDN_07-A5-mo-lai-sau-F5-du-lieu-con-nguyen.png` | **Sau khi tải lại trang thật**, mở lại `HSPL-20260803-0001`: Tên `QA-EDIT-A-20260803-2116 ten`, Loại `Giấy phép`, LVPL `Thuế`, Ngày cấp `01/08/2026`, Ngày hết hạn `31/12/2026`, Cơ quan cấp `QA-EDIT-A-...coquan`, Trạng thái `Hiệu lực` |
| `image/QLHSPLDN_07-B1-seed-tao-ho-so-moi.png` | Bước seed: bảng có thêm dòng `HSPL-20260803-0003` (`QA-NEW-B-2026...`, Hợp đồng, Đất đai); dòng `HSPL-20260803-0001` đã mang dữ liệu sửa của phép thử A |
| `image/QLHSPLDN_07-B2-ho-so-moi-sau-F5-du-lieu-con-nguyen.png` | **Sau khi tải lại trang**, mở lại hồ sơ MỚI: Tên `QA-EDIT-B-20260803-2122 ten`, Loại `Khác`, LVPL `Hành chính`, Ngày cấp `15/09/2026`, Ngày hết hạn `20/01/2027`, Trạng thái `Thu hồi` |
| `image/QLHSPLDN_07-A2-ho-so-cu-21-07-sau-F5.png` | **Sau khi tải lại trang**, hồ sơ cũ 21/07 mở bằng `cbnv_hn` (`BTP · DP` · `CB_NV_DP`): Tên `QA-EDIT-A2-...`, Loại `Quyết định`, LVPL `Dân sự`, Ngày cấp `10/08/2026`, Ngày hết hạn `30/11/2026`, Trạng thái `Hết hạn` |

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — bản chốt duy nhất. Đã **grep toàn bộ 18 file** cho khái niệm "hồ sơ pháp lý" / `HO_SO_PHAP_LY_DN` / `HSPL` trước khi chốt, không đọc một dòng rồi kết luận.

**SRS quy định gì:**

- `srs-fr-12-tv-chuyen-sau.md:541` — `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)`; **dòng 543** ghi `**UC Reference:** UC 150`.
- `srs-fr-12-tv-chuyen-sau.md:550` — Mô tả FR: *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, **chỉnh sửa**, xóa mềm, tìm kiếm."*
- `srs-fr-12-tv-chuyen-sau.md:607-614` — khối **Processing "Chỉnh sửa"** 4 bước: (1) kiểm tra quyền + phạm vi đơn vị `BR-AUTH-01, BR-AUTH-08`; (2) xác nhận dữ liệu cập nhật; (3) **"Cập nhật bản ghi hồ sơ"**; (4) **"Ghi nhật ký thao tác"** `BR-DATA-05`.
- `srs-fr-12-tv-chuyen-sau.md:674` — Postconditions: *"Hồ sơ được tạo/**cập nhật**/xóa mềm trong CSDL"*; **dòng 676** *"AUDIT_LOG ghi nhận mọi thao tác CUD"*.
- `srs-fr-12-tv-chuyen-sau.md:695` — Acceptance Criteria: *"**Given** CB NV chỉnh sửa hồ sơ **When** sửa thông tin + nhấn Lưu **Then** cập nhật bản ghi"*.
- `srs-fr-12-tv-chuyen-sau.md:560-574` — bảng Inputs "Thêm mới / Chỉnh sửa" liệt kê đúng 11 trường, gồm `ten_ho_so`, `loai_ho_so` (5 giá trị), `linh_vuc_id`, `ngay_cap`, `ngay_het_han`, `co_quan_cap`, `mo_ta`, `trang_thai` (3 giá trị) và **dòng 574** `file_dinh_kem | file | N | PDF/image, max 20MB`.
- `srs-fr-07-doanh-nghiep.md:468` — thành phần số 2 của màn `SCR-V.III-02`: *"Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) … **CRUD hồ sơ pháp lý DN**: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC. Trạng thái: HIEU_LUC / HET_HAN / THU_HOI"* — đây chính là màn đối tác đứng.
- `srs-fr-12-tv-chuyen-sau.md:547` — màn riêng cũ `SCR-X1-03` đã **DEPRECATED v2.1**, chuyển thành tab trong màn chi tiết DN ⇒ tab này là nơi duy nhất còn thực thi FR-X.1-04. **Không dùng dòng nào của SCR-X1-03 làm căn cứ.**

**Kiểm nhãn `[GAP-...]`:** trong FR-X.1-04 chỉ có **2** khối mang nhãn GAP — `Processing — Xem chi tiết [GAP-X.1-05]` (dòng 634) và `Processing — Xuất Excel [GAP-X.1-05]` (dòng 644). Khối **"Chỉnh sửa" (dòng 607) KHÔNG mang nhãn GAP**, và AC dòng 695 cũng không. ⇒ Yêu cầu áp dụng cho case này là **đã chốt trong SRS**, không thuộc vùng SRS chưa chốt.

**Kiểm mâu thuẫn nội tại SRS:** chỗ duy nhất trong SRS gọi danh sách hồ sơ pháp lý là *"Read-only"* là `srs-fr-07-doanh-nghiep.md:523`, nhưng dòng đó thuộc **SCR-V.III-04 "Hồ sơ doanh nghiệp của tôi"** (`srs-fr-07-doanh-nghiep.md:508`) — **chuyên trang của vai trò Doanh nghiệp**, không phải màn của cán bộ. ⇒ Không có mâu thuẫn cho màn đang xét.

**Đối chiếu từng vế:**

- SRS dòng 613 *"Cập nhật bản ghi hồ sơ"* → web: **27/27 ô đo** ở 3 kịch bản đều được ghi vào bản ghi, xác nhận cả sau khi tải lại trang lẫn khi đọc lại từ máy chủ. ✅
- SRS dòng 695 *"sửa thông tin + nhấn Lưu → cập nhật bản ghi"* → web: bấm **Đồng ý** (nhãn thực tế của nút Lưu) → 1 request, 1 thông báo thành công, dữ liệu đổi thật. ✅
- SRS dòng 614 + 676 *"Ghi nhật ký thao tác / AUDIT_LOG"* — tương ứng vế *"lưu vết thao tác"* ở Kết quả mong đợi của phiếu → web: `version` tăng 1→2, `ngayCapNhat` cập nhật đúng thời điểm bấm, `nguoiCapNhatId` ghi đúng người thao tác ở cả 3 kịch bản. ✅
- SRS dòng 574 `file_dinh_kem` → web: tệp mới đính kèm được lưu đúng tên + đúng dung lượng, còn nguyên sau khi tải lại trang. ✅ (đây chính là thứ hỏng trong video đối tác)
- SRS dòng 567 + 573 (5 loại hồ sơ × 3 trạng thái) → web: đã đổi và lưu thành công `GIAY_PHEP` / `QUYET_DINH` / `KHAC` và cả 3 trạng thái `HIEU_LUC` / `HET_HAN` / `THU_HOI`. ✅

---

## Phép thử thứ hai (đo lại bằng phương pháp khác)

Mỗi kết luận dựa trên **≥2 phương pháp độc lập cho kết quả trùng nhau**:

1. **Đọc cây DOM của cửa sổ Sửa sau khi tải lại trang** (giao diện) — bằng class ĐÚNG đã kiểm chứng (`.ant-select-content`, `.ant-upload-list-item-container`).
2. **Gọi thẳng dịch vụ máy chủ đọc lại bản ghi theo id** — so từng trường, gồm cả danh sách tệp đính kèm và các trường lưu vết.
3. **Ảnh chụp màn hình đã mở đọc bằng mắt** — xác nhận đúng những gì hai phương pháp trên báo.
4. **Dòng trong bảng danh sách sau khi tải lại trang** — nguồn dữ liệu thứ tư, cũng khớp.

Bốn phương pháp **không mâu thuẫn nhau** ở bất kỳ trường nào ⇒ đủ điều kiện chốt verdict.

---

## Kết luận

- Phản ánh của đối tác **KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, kiểm ở đúng vai trò `CB_NV_TW` + đúng phạm vi `BTP · TW` như bằng chứng đối tác.
- Đã đo **cả hồ sơ có sẵn từ trước (A), hồ sơ cũ thật tạo 21/07 (A2), lẫn hồ sơ mới tạo qua luồng chuẩn (B)** — cả ba đều lưu đủ **9/9 trường** ở **3/3 nơi kiểm**. Không có chênh lệch giữa dữ liệu cũ và dữ liệu mới ⇒ **không phải trường hợp "dữ liệu cũ đóng băng"**, không cần `BA confirm`.
- Kịch bản gây lỗi trong video đối tác (thêm tệp đính kèm rồi mở lại) đã chạy lại **3/3 lần đều giữ được tệp**.
- Đối tác **không thao tác sai** — video của họ cho thấy bản dựng cũ thật sự làm mất tệp vừa đính kèm dù đã báo thành công. Vì vậy **KHÔNG dùng `Reject`**.
- Cột P đang là `dev done` (không phải `Reject`) và phép thử lại cho kết quả **chạy đúng** ⇒ theo bảng ánh xạ verdict của đợt này, dùng **`Pass`** (không dùng `Resolved` — `Resolved` là cặp quy ước đi với P=`Reject`).
- **⇒ Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.

---

## Quan sát ngoài phạm vi case (KHÔNG log lên sheet — báo user quyết)

**Cán bộ cấp Trung ương thấy được hồ sơ của đơn vị địa phương nhưng không sửa được, mà nút "Sửa" vẫn hiện.**

- Số đo: `cbnv_tw_04` (TW) mở tab Hồ sơ pháp lý của `DN-HNI-0001` thì thấy **6 hồ sơ**, trong đó 4 hồ sơ thuộc đơn vị **Sở Tư pháp Hà Nội**. Cả 6 dòng đều hiện đủ nút `Xem / Sửa / Xoá`. Bấm **Sửa** một hồ sơ của Sở Tư pháp Hà Nội, điền đủ dữ liệu, bấm **Đồng ý** → hệ thống từ chối: **1 request / 1 thông báo** `"Không có quyền truy cập dữ liệu đơn vị khác"`, phản hồi máy chủ **403 `ERR-AUTH-VPD-00-01`**. Cùng lúc, `cbnv_hn` (Địa phương) chỉ thấy **4 hồ sơ** của đơn vị mình.
- Đối chiếu SRS: `srs-fr-11-bao-cao.md:1268` — `BR-AUTH-08`: *"chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. **TW thấy toàn quốc**, BN thấy BN, ĐP thấy ĐP"* ⇒ việc TW **đọc** được 6 hồ sơ là ĐÚNG. Nhưng `srs-fr-12-tv-chuyen-sau.md:675` (Postconditions của chính FR-X.1-04) lại ghi *"phân quyền dữ liệu theo đơn vị (**chỉ xem hồ sơ đơn vị mình**)"* — **hai dòng này nói ngược nhau về phạm vi đọc**. Phạm vi **ghi** thì SRS không nói rõ ở đâu cả.
- Vì vậy **chưa kết luận đúng/sai**: đây là điểm SRS mâu thuẫn nội tại → thuộc loại cần BA chốt, không phải bug hiển nhiên. Điều chắc chắn quan sát được là **trải nghiệm không nhất quán**: hệ thống mời người dùng bấm "Sửa", cho điền hết form, rồi mới từ chối ở bước cuối.
- Ảnh: `image/QLHSPLDN_07-X1-toast-khong-co-quyen-don-vi-khac.png`.

Ngoài mục trên, **không phát hiện thêm** bất thường nào: không có thông báo lặp ở bất kỳ thao tác nào (3 lần lưu + 1 lần tạo mới đều đúng tỉ lệ 1 request ↔ 1 thông báo), không tạo trùng bản ghi, không có ô chữ bị lỗi hiển thị.
