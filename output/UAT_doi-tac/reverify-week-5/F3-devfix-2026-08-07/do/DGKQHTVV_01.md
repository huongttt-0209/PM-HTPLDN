# Nhật ký đo — DGKQHTVV_01 (dòng 64) · R3 2026-08-07

**Chuẩn chấm đã khóa:** [`../chuan/DGKQHTVV_01.md`](../chuan/DGKQHTVV_01.md)
**Bug entry:** `BUG-VV-DGKQHTVV-01` trong `../../../reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/bug-report.md`
**Verdict đề xuất: 🔁 REOPEN** (vế quyết định D2 — nhánh DOANH NGHIỆP — vẫn hỏng)

---

## 1. Vân tay bản dựng

| Mục | Giá trị đo được | Đối chiếu |
|---|---|---|
| Chuỗi phiên bản chân sidebar | `HTPLDN · V1.0.10` | **TRÙNG** |
| Bó mã FE | `assets/index-B2W2Krcs.js` | **TRÙNG** |
| `last-modified` | `Thu, 06 Aug 2026 17:39:54 GMT` | **TRÙNG** |
| `etag` | `W/"6a74c6ea-428"` | **TRÙNG** |

Không có triển khai mới xen giữa 2 case.

---

## 2. Tài khoản thực dùng — **ra verdict bằng DOANH NGHIỆP**

| Vai trò | Tài khoản | Định danh đọc từ `/api/v1/auth/me` |
|---|---|---|
| **DN #1 — ra verdict** | `0209888006` | `userId b9c7f944-989f-48f4-8457-9d2e28875fc5` · `hoTen "QA UAT DN An Giang"` · `vaiTro ["DN"]` · `doanhNghiepId c03a66bc-f584-437d-89c8-1371f6a69772` |
| **DN #2 — ra verdict** | `0109998887` | `userId 996cc5db-43c5-4903-b3d1-1c21adb2ece8` · `hoTen "QA UAT Kiem Thu DN"` · `vaiTro ["DN"]` · `doanhNghiepId 829abcac-b0af-4cde-9af9-ec51bc79014c` |

**Không dùng `admin`. Không dùng tài khoản cán bộ để ra verdict.** Đăng nhập DN bằng tên đăng nhập = mã số thuế, mật khẩu `Test@1234`, OTP lấy ở MailHog — cả 2 tài khoản đăng nhập được ngay lần đầu, không phải fallback.

---

## 3. Xác minh quyền sở hữu (không đoán)

`GET /api/v1/vu-viecs` bằng chính phiên DN — backend cố định lọc theo DN đăng nhập (`:1846`), nên **mọi dòng trả về đều là vụ việc của chính DN đó**.

- **DN #1 `0209888006`: 8 vụ việc**, cả 8 đều mang tên doanh nghiệp *Cong ty QA UAT An Giang* (xem ảnh R3-02). Gồm `VV-STP-AG-20260806-005 / -004 / -003 / -002 / -001` và `VV-STP-AG-20260712-003 / -002 / -001`.
- **DN #2 `0109998887`: 5 vụ việc** — `VV-STP-HN-20260806-002` · `-001` · `VV-STP-HN-20260805-003` · `-002` · `-001`.

🔴 **Trả lời câu hỏi D3 của chuẩn chấm §10.7:** `VV-BTP-TW-20260806-003` và `-004` **KHÔNG có** trong danh sách của `0109998887` ⇒ theo đúng quy tắc đã khóa ("Không có ⇒ chuyển đường B"), **Đường A của D3 bị loại**. (Ghi chú kỹ thuật để dev tra: `doanhNghiepId` của 2 vụ việc TW đó là `829abcac…` — **trùng** `doanhNghiepId` của `0109998887`, nhưng danh sách của DN vẫn không trả về chúng. Đây là **quan sát ngoài phạm vi**, không kết luận, không dùng làm căn cứ verdict.)

---

## 4. Phép đo quyết định — D2: DN mở chi tiết vụ việc CỦA CHÍNH MÌNH

### 4.1 Bước 1 khối CÁCH VERIFY — "phải xem được nội dung hồ sơ, không bị đẩy sang trang báo không có quyền"

Thử **cả 2 đường vào** (không prescribe URL, theo bẫy 11):

| # | Cách mở | Tài khoản | Vụ việc | Kết quả |
|---|---|---|---|---|
| 1 | Tải trang bằng địa chỉ chi tiết | DN #1 | `VV-STP-AG-20260806-005` (`0dfb2b25…`, **"Đã đánh giá"**) | ❌ **bị đẩy sang `/403`** — *"Bạn không có quyền truy cập trang này. Vai trò hiện tại: Doanh nghiệp"* |
| 2 | **Bấm mã vụ việc trong danh sách của chính DN** (đường UI chuẩn `:1834`) | DN #1 | `VV-STP-AG-20260806-005` | ❌ **bị đẩy sang `/403`** — y hệt |
| 3 | Tải trang bằng địa chỉ chi tiết | DN #2 | `VV-STP-HN-20260806-001` (`ac866cde…`, "Đang kiểm tra") | ❌ **bị đẩy sang `/403`** |
| 4 | Tải trang bằng địa chỉ chi tiết | DN #1 | `VV-STP-AG-20260806-004` (`4100caae…`, "Đã tiếp nhận") | ✅ **mở được** |

⇒ **Lặp lại được trên 2 doanh nghiệp khác nhau**, và lặp lại qua **cả 2 đường vào**. Không phải lỗi ngẫu nhiên.

### 4.2 Bước 2 — đếm số phần tử tương tác dẫn tới việc đánh giá

Trên các vụ việc ở trạng thái đánh giá được ("Hoàn thành" / "Đã đánh giá"), **màn chi tiết không mở ra được** ⇒ **đếm được 0 phần tử**. Trên màn danh sách, cột **Hành động** chỉ có **1 biểu tượng con mắt (Xem)**, **không có nút [Đánh giá]** (ảnh R3-02).

⇒ Rơi thẳng vào vế FAIL đã khóa: *"doanh nghiệp vẫn không mở được chi tiết vụ việc của chính mình; hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá"*. **Bước 3 (tải lại trang đọc Nhóm 8) không thực hiện được vì chưa qua nổi bước 1.**

### 4.3 Nguyên nhân đọc tại chỗ (đường đo thứ hai, bằng chính phiên DN)

Gọi thẳng các nguồn dữ liệu màn chi tiết cần, **bằng cookie của phiên DN**:

| Nguồn dữ liệu | DN #1 (8/8 vụ việc) | DN #2 (2/2 vụ việc thử) | Mã lỗi |
|---|---|---|---|
| `GET /api/v1/vu-viecs/{id}` (hồ sơ chính) | **200** | **200** | — |
| `GET /api/v1/vu-viecs/{id}/ket-qua` (Nhóm 6) | **200** | **200** | — |
| `GET /api/v1/vu-viecs/{id}/phan-cong` (Nhóm 5) | **403** | **403** | `ERR-AUTH-DN-00-01` — *"Role không được phép truy cập endpoint CMS này"* |
| `GET /api/v1/vu-viecs/{id}/ket-qua-kiem-tra` (Nhóm 4) | **403** | **403** | `ERR-AUTH-DN-00-01` |

Nhật ký trình duyệt lúc bị đẩy sang `/403`:
```
[warn] [403] Yêu cầu bị từ chối: GET /vu-viecs/0dfb2b25-efa3-4fb4-86b7-31b4bfe78c86/ket-qua-kiem-tra
[error] Failed to load resource: the server responded with a status of 403 ()  [3 times]
```
🔴 **Đã kiểm cảnh báo chéo của điều phối:** dòng 403 ở đây là `/vu-viecs/{id}/ket-qua-kiem-tra`, **KHÔNG phải** `GET /files/…` `ERR-PERM-FILE-03` của hồ sơ tư vấn viên. Đây là triệu chứng thật của case 64, không phải lỗi đã log ở case khác.

**Tiến bộ so với vòng 06/08:** vòng trước **3** nguồn dữ liệu bị từ chối (phân công · kết quả · kết quả kiểm tra); nay `ket-qua` đã trả **200** ⇒ **dev đã sửa 1/3**. Còn **2 nguồn** vẫn bị từ chối và giao diện **vẫn bắt lỗi rồi chuyển thẳng sang trang không có quyền** thay vì ẩn 2 nhóm đó đi.

> Theo đặc tả, hai nhóm này **phải ẩn** ở chế độ DN chứ không phải để màn hình chết:
> `srs-fr-05-vu-viec.md:1805` — `| Nhóm 4 — Kết quả kiểm tra | **Ẩn hoàn toàn** (thông tin nội bộ) |`
> `srs-fr-05-vu-viec.md:1806` — `| Nhóm 5 — Phân công xử lý | **Ẩn hoàn toàn** (thông tin nội bộ — bảo mật cán bộ theo NĐ 13/2023)…`
> Bằng chứng ẩn đúng là **có thể làm được**: vụ việc `VV-STP-AG-20260806-004` mở ra bình thường và chỉ hiện *Thông tin Doanh nghiệp · Nội dung Yêu cầu · Tài liệu đính kèm · HĐ tư vấn liên kết* — **không** có Nhóm 4/5/7 (đúng `:1805` `:1806` `:1808`, **không log thành thiếu thông tin**).

### 4.4 Máy chủ ĐÃ cho phép doanh nghiệp đánh giá — nút thắt nằm ở màn chi tiết

Gọi thẳng thao tác đánh giá **bằng chính phiên DN #1**: `POST /api/v1/vu-viecs/{id}/danh-gia` **không còn trả `403 ERR-AUTH-DN-00-01`** như vòng 06/08 — nó vào tới tầng nghiệp vụ (trả `422` khi sai tên trường, `409` khi trùng).

Đồng thời trên `VV-STP-AG-20260806-005` đã tồn tại sẵn **một bản ghi đánh giá loại doanh nghiệp**, đọc bằng chính phiên DN:
```
diemChatLuong 9 · diemThoiGian 8 · diemThaiDo 10 · diemTong 9
nhanXet      "DN danh gia tren 120 v1.0.9"
ngayDanhGia  2026-08-06T13:06:09.881Z
nguoiDanhGia "QA UAT DN An Giang"
```
🔴 **KHÔNG dùng bản ghi này để chấm Pass:** nó **không do QA tạo trong vòng đo này**, chuỗi nhận xét không phải chuỗi mốc-giờ của QA, và nó được tạo trên **bản dựng v1.0.9** (khác bản đang đo). Nó chỉ chứng minh **tầng máy chủ đã mở quyền**; vế quyết định của phiếu là **doanh nghiệp có đường vào trên giao diện hay không** — và vế đó **vẫn hỏng**.

---

## 5. Bước 6 (chứng âm phạm vi) và bước 7 (kiểm trùng) — cả hai ĐẠT

| Bước | Thao tác | Kết quả | Đánh giá |
|---|---|---|---|
| **6 — chứng âm** | DN #1 đọc và thử đánh giá `VV-BTP-TW-20260806-001` (`1d26d8c7…`, của doanh nghiệp khác) | `GET` → **404** `ERR-VAL-VI-03-02` *"Vụ việc không tồn tại"*; `POST danh-gia` → **404** cùng mã; vụ việc **không** có trong danh sách của DN #1 | ✅ **bị từ chối** — đúng yêu cầu (chỉ chấm "bị từ chối hay không", không chấm theo mã lỗi) |
| **7 — kiểm trùng** | DN #1 đánh giá **lần 2** `VV-STP-AG-20260806-005` (đã có đánh giá loại DN) | `POST danh-gia` → **409** `ERR-STATE-SYS-00-01` — *"ERR-VAL-VI-16-02: Vụ việc đã được đánh giá"*. Đọc lại: **vẫn đúng 1 bộ điểm** 9·8·10, `diemTong 9`, `nhanXet` cũ **không bị ghi đè**, trạng thái vẫn `DA_DANH_GIA` | ✅ **bị từ chối, không ghi đè, không sinh bản ghi thứ hai** |

---

## 6. Bảng đối chiếu 5 dòng điều kiện

| # | Điều kiện | Yêu cầu | Thực tế | GAP |
|---|---|---|---|---|
| 1 | **Vai trò** | Ra verdict bằng **DOANH NGHIỆP**, cấm `admin`, cấm tài khoản cán bộ | Verdict ra từ phiên `0209888006` và `0109998887`. Không dùng `admin`, không dùng cán bộ | **Không** |
| 2 | **Entity + trạng thái** | Vụ việc ở "Hoàn thành" / "Đã đánh giá", DN chưa đánh giá | Đo trên `VV-STP-AG-20260806-005` (**"Đã đánh giá"**) + 9 vụ việc khác thuộc 2 DN ở nhiều trạng thái | ⚠️ **Có** — không có vụ việc nào của 2 DN đang ở "Hoàn thành" **mà DN chưa đánh giá**; xem §7 |
| 3 | **Dữ liệu tiền đề** | ≥2 vụ việc "Hoàn thành" chưa có đánh giá DN, trên ≥2 DN | **Không dựng được** — nút thắt nằm trước bước dựng: DN không mở nổi màn chi tiết. Đã đo trên toàn bộ 8 vụ việc của DN #1 + 5 của DN #2 | ⚠️ **Có** — nhưng **không cản verdict** vì FAIL xảy ra ở bước 1 |
| 4 | **Input** | 9·8·10 + chuỗi `QA-DGKQ-<YYYYMMDD-HHMM>` | **Không nhập được qua giao diện** (không có đường vào). Chuỗi đã chuẩn bị `QA-DGKQ-20260807-0150-kiem-trung` / `-0152-chung-am-pham-vi` dùng cho bước 6 + 7 | ⚠️ **Có** — do lỗi chặn |
| 5 | **Độ phủ biến thể** | N ≥ 3 · M = 4 dạng | **N = 10 vụ việc** đọc từ máy chủ (8 của DN #1 + 2 của DN #2), **3 vụ việc mở bằng giao diện**, **2 doanh nghiệp**. **M = 2/4 dạng đo được**: **D2 ❌ hỏng** (dạng quyết định) · **D4 ✅ đạt** | ⚠️ **Có** — **D1** (nhánh cán bộ, chỉ để kiểm hồi quy) **chưa chạy lại vòng này**; **D3 không dựng được** |

---

## 7. Ba dạng chưa đo được — nói rõ vì sao, không giấu

- **D1 (nhánh cán bộ nghiệp vụ — kiểm hồi quy, KHÔNG ra verdict): chưa chạy lại vòng này.** Đây là bước 8 bổ sung của chuẩn chấm, chỉ để chắc nhánh cán bộ không hỏng theo. **Không ảnh hưởng verdict** vì verdict do D2 quyết định và D2 đã hỏng dứt khoát. Đề nghị điều phối xếp vào vòng sau cùng lúc với re-verify D2.
- **D3 (một bên đã chấm, bên còn lại vào chấm): vẫn KHÔNG dựng được.** *Đường A* bị loại vì đã xác minh `VV-BTP-TW-20260806-003/-004` **không thuộc** danh sách của `0109998887` (§3). *Đường B* đòi doanh nghiệp chấm được trước — **chính là vế đang hỏng**. ⇒ Theo chuẩn chấm §7, **ghi nhận + gửi BA, KHÔNG chấm Fail, KHÔNG kéo verdict**.
- **Tiền đề "Hoàn thành chưa có đánh giá DN": không dựng được trong vòng này.** Vụ việc sẵn có duy nhất ở trạng thái đánh giá được (`VV-STP-AG-20260806-005`) **đã bị tiêu** bởi một lượt đánh giá DN tạo trên bản dựng `v1.0.9` trước khi vòng đo này bắt đầu. **Không tự dựng thêm** vì việc đó không đổi được kết quả: nút thắt nằm ở **bước 1** (mở màn chi tiết), xảy ra với **mọi trạng thái có dữ liệu nội bộ**, trên **cả 2 doanh nghiệp**, đã chứng minh bằng 10 bản ghi.

📌 **Dữ kiện mới cần ghi vào ô BA** (theo chuẩn chấm §7, không tự kết luận): mâu thuẫn "vụ việc đã ở *Đã đánh giá* thì bên còn lại có được vào đánh giá không" nằm ở **bảng nút chế độ CÁN BỘ** (`:1751`, chỉ có dòng `HOAN_THANH`); còn **bảng quy tắc chế độ DOANH NGHIỆP** khai *"Hoàn thành" / "Đã đánh giá"* **thống nhất ở cả 2 dòng** — `:1809` (Nhóm 8) và `:1811` (Thanh thao tác) ⇒ ở **nhánh DN, đặc tả không tự mâu thuẫn**.

---

## 8. Đối chiếu khối PASS/FAIL đã khóa

| Vế PASS (bug-report.md:890) | Kết quả |
|---|---|
| DN mở được chi tiết vụ việc của chính mình | ❌ **KHÔNG** — bị đẩy sang `/403`, 2 DN × 2 đường vào |
| Đếm được ≥1 phần tử dẫn tới việc đánh giá | ❌ **0 phần tử** |
| Sau khi tải lại trang, Nhóm 8 đọc đủ 3 điểm + nhận xét + điểm tổng | 🚫 **không thực hiện được** (chưa qua bước 1) |
| Đường đo thứ hai trùng khít + ghi loại người đánh giá là DN | 🚫 **không áp dụng được** cho bản ghi do QA tạo |
| Đúng trên ≥2 vụ việc và ≥2 doanh nghiệp | ❌ hỏng trên **cả 2 doanh nghiệp** |
| Chứng âm bước 6 bị từ chối | ✅ **đạt** |
| Kiểm trùng bước 7 bị từ chối | ✅ **đạt** |

Trúng vế FAIL nguyên văn: *"❌ FAIL nếu: doanh nghiệp vẫn không mở được chi tiết vụ việc của chính mình; hoặc mở được nhưng không có phần tử nào để bắt đầu đánh giá"*.

**Ba dấu hiệu CẤM dùng để Pass đều đã tránh:** không chấm theo nhãn trạng thái "Đã đánh giá", không chấm theo mục nhật ký `DANH_GIA`, không chấm theo thông báo thành công — và **không** chấm Pass dựa vào việc máy chủ đã mở quyền hay vào bản ghi đánh giá sẵn có của bản dựng v1.0.9.

**⇒ VERDICT: 🔁 REOPEN.**

---

## 9. Ảnh kèm chú thích (đã mở đọc lại, tên ↔ nội dung khớp)

| Tên file | Thấy gì |
|---|---|
| `DGKQHTVV_01-R3-01-DN0209888006-mo-VV005-cua-chinh-minh-bi-day-sang-403.png` | Phiên **QA UAT DN An Giang · Doanh nghiệp** (`0209888006`), sidebar `HTPLDN · V1.0.10`. Mở `VV-STP-AG-20260806-005` của **chính mình** → màn **403** *"Bạn không có quyền truy cập trang này. Vai trò hiện tại: Doanh nghiệp"*, chỉ còn 2 nút [Về trang chủ] [Quay lại]. |
| `DGKQHTVV_01-R3-02-DN0209888006-danh-sach-vu-viec-cua-minh-8-dong-khong-co-nut-Danh-gia.png` | Cùng phiên DN, màn **Vụ việc HTPL** — tab `Tất cả 8`, `Hoàn thành 1`. **Cả 8 dòng đều là *Cong ty QA UAT An Giang*** (chứng minh quyền sở hữu). Dòng đầu `VV-STP-AG-20260806-005` nhãn **Đã đánh giá**. Cột **Hành động** chỉ có **1 biểu tượng con mắt**, **không có nút [Đánh giá]**. |
| `DGKQHTVV_01-R3-03-DN0109998887-mo-vu-viec-cua-chinh-minh-cung-bi-day-sang-403.png` | Phiên **QA UAT Kiem Thu DN · Doanh nghiệp** (`0109998887`). Mở `VV-STP-HN-20260806-001` của **chính mình** → cũng **403** y hệt ⇒ lặp lại trên doanh nghiệp thứ hai. |

---

## 10. Hai câu bắt buộc

**a) Fix này có làm hỏng gì khác trong cùng luồng không? — Không thấy hỏng thêm; có 1 phần đã tốt lên.**
- `GET /vu-viecs/{id}/ket-qua` từ **403 → 200** cho phiên DN (1/3 nguồn dữ liệu đã mở).
- `POST /vu-viecs/{id}/danh-gia` **không còn** chặn theo vai trò ở tầng máy chủ.
- Chặn trùng (bước 7) và chặn vượt phạm vi (bước 6) **vẫn đúng**, không bị nới lỏng theo.
- DN vẫn mở được chi tiết ở các trạng thái sớm (`VV-STP-AG-20260806-004`) với Nhóm 4/5/7 **ẩn đúng đặc tả**.

**b) Ngoài phạm vi bug, có thấy gì bất thường không? — 2 điểm, cả hai xếp CANDIDATE, KHÔNG dùng làm căn cứ verdict:**

1. **Dòng thời gian ở chế độ DN đang hiện sự kiện nội bộ.** Trên `VV-STP-AG-20260806-004` mở bằng phiên DN, khối "Dòng thời gian" liệt kê cả **`Phân công`** và **`Từ chối phân công`** kèm tên cán bộ. Đặc tả `srs-fr-05-vu-viec.md:1810` ghi: *"Chỉ hiển thị các sự kiện liên quan đến DN: tiếp nhận, kết luận kiểm tra, kết quả phê duyệt, hoàn thành, từ chối, công khai/hủy công khai. **Ẩn sự kiện nội bộ (phân công, trao đổi giữa cán bộ)**"*. ⇒ **candidate** — chưa mở phiếu riêng vì (i) chưa chạy đường đo thứ hai chuyên cho vế này, (ii) màn chi tiết chế độ DN đang là đối tượng của chính bug này nên trạng thái hiện thời chưa ổn định. Đề nghị đo lại sau khi dev sửa xong lối vào.
2. **Danh sách của DN `0109998887` không trả 2 vụ việc mang cùng `doanhNghiepId`** (`VV-BTP-TW-20260806-003/-004`, `doanhNghiepId 829abcac…`). ⇒ **candidate** — có thể là lọc thêm theo đơn vị, đặc tả `:1846` chỉ nói lọc theo DN. Ghi để dev/BA tra, **không** kết luận.

🔴 Cả 2 candidate **không** được dùng làm căn cứ verdict. Không mở thêm màn / vai trò / bộ lọc nào chỉ để săn lỗi.

**Không log thành bug (đúng đặc tả, theo 2 bẫy điều phối đã cảnh báo):** DN không thấy Nhóm 4 / 5 / 7 (`:1805` `:1806` `:1808`) · Dòng thời gian chế độ DN không liệt kê sự kiện "Đánh giá" (`:1810`).

---

## 11. Dữ liệu đã dựng · đã hoàn nguyên

- **Không tạo, không sửa, không xóa** bản ghi nào cho case này.
- Hai lời gọi ghi duy nhất là **phép thử bắt buộc của bước 6 và bước 7**, và **cả hai đều bị máy chủ từ chối** (`404` và `409`) ⇒ **không phát sinh dữ liệu**. Đã đọc lại `VV-STP-AG-20260806-005` sau khi thử: bộ điểm và nhận xét **y nguyên**, trạng thái vẫn `DA_DANH_GIA`.
- Không đụng dữ liệu của đối tác. Không có gì cần hoàn nguyên.

---

## 12. Giới hạn hiệu lực

Kết luận chỉ có giá trị cho **env nội bộ `18.143.165.120.nip.io`** + **bản dựng `V1.0.10` / `assets/index-B2W2Krcs.js` / `last-modified Thu, 06 Aug 2026 17:39:54 GMT` / `etag W/"6a74c6ea-428"`**. Bằng chứng gốc của đối tác quay trên môi trường nghiệm thu khác.
