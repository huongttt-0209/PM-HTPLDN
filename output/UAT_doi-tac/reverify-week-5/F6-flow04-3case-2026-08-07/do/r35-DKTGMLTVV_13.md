# Dòng 35 · `DKTGMLTVV_13` — "Gửi đăng ký khi Dữ liệu hợp lệ"

**Verdict logic Flow 04: `Cần BA`** → ô `Trạng thái dev fix` = **`BA confirm`**

| Hạng mục | Giá trị |
|---|---|
| Ngày đo | 2026-08-07, 02:25–02:35 giờ VN |
| Env · bản dựng | `https://18.143.165.120.nip.io` (nội bộ) · **`HTPLDN · V1.0.9`** (đọc từ chân sidebar trong chính phiên đo) |
| Màn đo | `/chuyen-gia-tvv/tao-moi` (SCR-IV-02) — vào bằng **click menu** Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → `[+ Thêm mới]` |
| Tài khoản thao tác | `nht_ag_uat2` / `Test@1234` — vai trò `NHT`, cấp `DP`, `donViId = 00000000-0000-4000-8002-000000000006` (Sở Tư pháp An Giang) |
| Tài khoản đọc side-effect | `cbnv_dp_05` (C6 — **cùng `donViId`**, đã xác minh trước khi chấm) · `admin` (C7 — chỉ đọc Nhật ký hệ thống) |
| Bản ghi tạo ra | `TVV-STP-AG-0004` · id `b26e0722-19bd-4f78-85fc-b2e169edc80d` |

> **Khai mutate môi trường:** lượt đo tạo **01 hồ sơ TVV mới** trên env nội bộ (`TVV-STP-AG-0004`, họ tên
> `QA F6 DKTGMLTVV13 0225`, CCCD `086802252547`, email `qa.f6.dktgmltvv13.022525@htpldn.test`, trạng thái
> `MOI_DANG_KY`), kèm 2 tệp PDF đính. Không đụng dữ liệu của đối tác, không sửa/xóa bản ghi có sẵn.

---

## 1. Scope Lock (khóa ở Giai đoạn A, KHÔNG đổi sau khi mở màn)

Chuẩn chấm đầy đủ: [`chuan/DKTGMLTVV_13-row35.md`](../chuan/DKTGMLTVV_13-row35.md).

| Vế | Expected đối tác | Quan hệ | Route |
|---|---|---|---|
| C1 | Hệ thống tạo hồ sơ tư vấn viên | **MATCH** | TEST |
| C2 | …với loại **"Người hỗ trợ"** | **DIFF** | **BA — cấm Pass** |
| C3 | …ở trạng thái **"Mới đăng ký"** | **MATCH** | TEST |
| C4 | Tạo liên kết đến các **lĩnh vực pháp luật đã chọn** | **MATCH** | TEST |
| C5 | …và **tổ chức chủ quản (nếu có)** | **MATCH** | TEST |
| C6 | Gửi thông báo đến **Cán bộ nghiệp vụ cùng đơn vị** | **MATCH** | TEST |
| C7 | **Lưu vết thao tác** | **MATCH** | TEST |
| C8 | Thông báo **"Đăng ký thành công, chờ thẩm định"** | **MATCH** | TEST |
| C9 | …**cùng mã hồ sơ đã tạo** | **GAP** | **BA** |
| C10 | Chuyển sang **"trang theo dõi tiến độ"** | **DIFF** | **BA — cấm Pass** |

---

## 2. Phép đo

Một lượt tạo hồ sơ duy nhất (**1 POST `/api/v1/tu-van-viens` → `201`**, không double-submit — đã đếm request
kèm toast). Dữ liệu nhập theo §4.3 của chuẩn, tệp đính theo §4.4.

### 2.1 C2 — đo hiện trạng TRƯỚC khi nhập liệu (không bấm gì thêm)

Mở ô **"Loại"** trên chính form `/chuyen-gia-tvv/tao-moi`, đọc nhãn từng option bằng `innerText`:

| Số option | Nhãn đọc được |
|---:|---|
| **2** | `Tư vấn viên (TVV)` · `Chuyên gia (CG)` |

**Không có giá trị "Người hỗ trợ".** Hồ sơ tạo ra mang `loaiTvv = "TVV"`, hiển thị trên danh sách là
`Tư vấn viên`.

Ảnh: [`image/r35-C2-dropdown-Loai-chi-co-TVV-va-CG-V109.png`](../image/r35-C2-dropdown-Loai-chi-co-TVV-va-CG-V109.png)
→ Drive: https://drive.google.com/file/d/1ShIqR8mfpMvkTVO0ZDZFQrgqlfsFMfSQ/view?usp=drivesdk

⇒ **Web đang theo SRS, KHÁC expected đối tác.** Quan hệ `DIFF` giữ nguyên ⇒ **cấm Pass**, chuyển BA (§4.1).

### 2.2 C8 + C9 — toast (cài `MutationObserver` TRƯỚC khi bấm `Lưu`, không lọc trùng, đọc `innerText`)

Chuỗi bắt được (4 node = wrapper + notice của **cùng 1 toast**, khớp đúng **1** POST tạo):

```
19:30:40.288Z  .ant-message-notice-wrapper …   "Đăng ký thành công, chờ thẩm định"
19:30:40.289Z  .ant-message-notice-success     "Đăng ký thành công, chờ thẩm định"
19:30:40.289Z  .ant-message-notice-wrapper …   "Đăng ký thành công, chờ thẩm định"
19:30:40.289Z  .ant-message-notice-success     "Đăng ký thành công, chờ thẩm định"
```

- **C8 ĐẠT** — trùng **nguyên văn** `srs-fr-04-chuyen-gia-tvv.md:351` *"Đăng ký thành công, chờ thẩm định"*.
- **C9** — chuỗi toast **KHÔNG chứa mã hồ sơ**. Mã `TVV-STP-AG-0004` chỉ có trong thân phản hồi máy chủ, không
  ghép vào câu thông báo. Quan hệ `GAP` (SRS im lặng) ⇒ chuyển BA, **không chấm đạt/không đạt**.

### 2.3 C10 — điều hướng sau khi lưu (chỉ đọc, không bấm thêm)

| Đo | Giá trị |
|---|---|
| `location.href` ngay sau khi lưu | `https://18.143.165.120.nip.io/chuyen-gia-tvv/danh-sach` |
| Breadcrumb | `Trang chủ / Mạng lưới Tư vấn viên / Danh sách` |
| Tiêu đề màn | `Tư vấn viên / Chuyên gia` |

⇒ Web chuyển về **trang Danh sách**, đúng `srs-v3.5.md:6759` §H7 (BẮT BUỘC), **khác** expected đối tác
("trang theo dõi tiến độ"). Quan hệ `DIFF` giữ nguyên ⇒ **cấm Pass**, chuyển BA.

### 2.4 C1 · C3 · C4 · C5 — bản ghi vừa tạo

**UI:** tab `Mới đăng ký` đếm **1 → 2**; hàng mới hiển thị:

| Mã TVV | Họ tên | Loại | Lĩnh vực | Tổ chức | Trạng thái |
|---|---|---|---|---|---|
| `TVV-STP-AG-0004` | `QA F6 DKTGMLTVV13 0225` | `Tư vấn viên` | `Lao động` · `Thương mại` | `Trung tam Tu van Phap luat QA Dia phuong` | **`Mới đăng ký`** |

Ảnh: [`image/r35-C1-C3-C4-C5-ban-ghi-moi-Moi-dang-ky-V109.png`](../image/r35-C1-C3-C4-C5-ban-ghi-moi-Moi-dang-ky-V109.png)
→ Drive: https://drive.google.com/file/d/1BxtC8GIHUqMBcveAI0a-_FPe6rHQQYl5/view?usp=drivesdk

**Đối chứng độc lập bằng API** — thân phản hồi `POST /api/v1/tu-van-viens` `201` (lưu tại
[`do/r35-POST-tu-van-viens-201.network-response`](r35-POST-tu-van-viens-201.network-response)) và
`GET /api/v1/tu-van-viens/b26e0722-…`:

```
id          = b26e0722-19bd-4f78-85fc-b2e169edc80d
maTvv       = TVV-STP-AG-0004
trangThai   = MOI_DANG_KY
loaiTvv     = TVV
donViId     = 00000000-0000-4000-8002-000000000006   ← trùng donViId của NHT thao tác
linhVucs    = [{Thương mại}, {Lao động}]             ← đúng 2 lĩnh vực đã chọn
toChucChinh = {Trung tam Tu van Phap luat QA Dia phuong}
```

- **C1 ĐẠT** — bản ghi được tạo, `donViId` auto-set theo NHT (`srs-fr-04-chuyen-gia-tvv.md:311`).
- **C3 ĐẠT** — `MOI_DANG_KY` / badge `Mới đăng ký` (`:349`, `:1350`).
- **C4 ĐẠT** — đủ **cả 2** lĩnh vực đã chọn, không thiếu không thừa.
- **C5 ĐẠT** — `toChucChinhId` trỏ đúng tổ chức đã chọn (`:310`, `:1515`). Dropdown **không rỗng** nên không
  phải dùng nhánh "Chưa đo được" của §4.5.

### 2.5 C6 — thông báo tới Cán bộ Nghiệp vụ cùng đơn vị

**Xác minh điều kiện bắt buộc trước khi chấm** (§4.1): `cbnv_dp_05` có `donViId = 00000000-0000-4000-8002-000000000006`
— **trùng** `donViId` của NHT thao tác. Đủ điều kiện chấm.

Đăng nhập `cbnv_dp_05` → chuông Thông báo:

| Mốc giờ | Tiêu đề | Nội dung |
|---|---|---|
| `2026-08-06T19:30:39.789Z` | `Hồ sơ tư vấn viên mới cần thẩm định` | `Hồ sơ TVV QA F6 DKTGMLTVV13 0225 vừa được tạo và đang chờ thẩm định.` |

**Chống phép đo nói dối:** không dùng số badge/độ dài mảng — đối chiếu **mốc giờ** (sau POST `19:30:39.737Z`
đúng 52 ms) **+ tên ứng viên** vừa tạo. ⇒ **C6 ĐẠT**.

Ảnh: [`image/r35-C6-CBNV-cung-don-vi-nhan-thong-bao-ho-so-moi-V109.png`](../image/r35-C6-CBNV-cung-don-vi-nhan-thong-bao-ho-so-moi-V109.png)
→ Drive: https://drive.google.com/file/d/1ZQC2MR-A3zxENbL1uC4DQLIUYtIoobog/view?usp=drivesdk

### 2.6 C7 — lưu vết thao tác

Đăng nhập `admin` → Quản trị hệ thống → **Nhật ký hệ thống** (`srs-fr-10-quan-tri.md:1373` — chỉ QTHT):

| Thời gian | Người dùng | Đơn vị | Module | Entity | Mã bản ghi | Loại thao tác |
|---|---|---|---|---|---|---|
| `07/08/2026 02:30:39` | `QA NHT An Giang UAT2` | `Sở Tư pháp An Giang` | `CG-TVV` | `TU_VAN_VIEN` | `b26e0722…` | **`Tạo mới`** |

**Đối chứng:** bản ghi log đọc qua API chứa `entityId = b26e0722-…`, `hanhDong = CREATE`,
`nguoiThucHienUsername = nht_ag_uat2`, `endpoint = POST /api/v1/tu-van-viens`, `responseCode = 201`,
`thoiGian = 2026-08-06T19:30:39.796Z`. ⇒ **C7 ĐẠT** (`:328`, BR-DATA-05 `:2514`).

Ảnh: [`image/r35-C7-nhat-ky-he-thong-dong-Tao-moi-TU-VAN-VIEN-V109.png`](../image/r35-C7-nhat-ky-he-thong-dong-Tao-moi-TU-VAN-VIEN-V109.png)
→ Drive: https://drive.google.com/file/d/1-jTowDFawc_xbJtUMD8h6Pc0Tm2p_KXq/view?usp=drivesdk

---

## 3. Chốt verdict

| Vế | Quan hệ | Kết quả đo | Ảnh hưởng verdict |
|---|---|---|---|
| C1 | MATCH | **ĐẠT** | — |
| C2 | DIFF | web chỉ có `TVV`/`CG`, không có "Người hỗ trợ" | **Cấm Pass** → BA-1 |
| C3 | MATCH | **ĐẠT** | — |
| C4 | MATCH | **ĐẠT** | — |
| C5 | MATCH | **ĐẠT** | — |
| C6 | MATCH | **ĐẠT** | — |
| C7 | MATCH | **ĐẠT** | — |
| C8 | MATCH | **ĐẠT** (đúng nguyên văn) | — |
| C9 | GAP | toast không kèm mã hồ sơ | BA-2 |
| C10 | DIFF | về trang Danh sách, không phải "trang theo dõi tiến độ" | **Cấm Pass** → BA-3 |

**7/7 vế MATCH đều ĐẠT ⇒ không có phần nào kéo về `Reopen`. Còn 2 `DIFF` + 1 `GAP` ⇒ verdict logic = `Cần BA`.**

**Giới hạn hiệu lực:** chỉ đúng cho env nội bộ bản dựng **V1.0.9** tại thời điểm đo. Bằng chứng đối tác chụp
trên `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0`. Chưa đo lại trên env nghiệm thu.

**Không kết luận "fix đã có tác dụng"** — QA không có ảnh "lỗi cũ" tự chụp trên cùng env.

---

## 4. CẦN BA CONFIRM

### BA-1 (vế C2 — DIFF, chặn Pass)

> **CẦN BA CONFIRM:** đối tác kỳ vọng hồ sơ tạo ở màn Thêm mới Tư vấn viên (`/chuyen-gia-tvv/tao-moi`) mang loại
> **"Người hỗ trợ"**; SRS quy định trường Loại của hồ sơ này **chỉ nhận `TVV` hoặc `CG`** và "Người hỗ trợ" là
> **entity + màn riêng** (`srs-fr-04-chuyen-gia-tvv.md:296` Inputs #0 `CHECK IN ('TVV','CG')`; `:1490` dropdown
> 2 lựa chọn "Tư vấn viên"/"Chuyên gia"; `:1381–1386` bảng ánh xạ `loai_tvv` chỉ TVV/CG; `:2019` entity
> TU_VAN_VIEN *"NHT lưu ở entity riêng NGUOI_HO_TRO"*; `:1799` màn tạo Người hỗ trợ ở
> `/chuyen-gia-tvv/nguoi-ho-tro/tao-moi`; `:2073` NHT khởi tạo ở `CHO_KICH_HOAT` chứ không phải `MOI_DANG_KY`;
> `:18` lịch sử thay đổi 2026-05-03 gỡ NHT khỏi enum `loai_tvv`); **web/dev hiện tại**: ô "Loại" chỉ mở ra đúng
> **2** lựa chọn `Tư vấn viên (TVV)` và `Chuyên gia (CG)`, hồ sơ tạo ra mang `loaiTvv = TVV`.
>
> **Đề nghị BA chốt 1 trong 2 hướng:** (a) expected của đối tác đang nhầm giữa *vai trò người thao tác (NHT)* với
> *loại hồ sơ* ⇒ sửa expected về loại "Tư vấn viên"/"Chuyên gia"; hoặc (b) nghiệp vụ thật sự cần thêm giá trị
> "Người hỗ trợ" vào trường Loại của hồ sơ TVV ⇒ BA nhập thay đổi vào SRS (Inputs #0 + SCR-IV-02 mục 2.2 + §3.0 +
> entity TU_VAN_VIEN) rồi mới verify lại.

### BA-2 (vế C9 — GAP, SRS im lặng)

> **CẦN BA CONFIRM:** đối tác kỳ vọng thông báo thành công hiển thị **kèm mã hồ sơ vừa tạo**; SRS **im lặng** —
> §Outputs của FR-IV-03 tách riêng `ma_tvv` (`srs-fr-04-chuyen-gia-tvv.md:348`) và `thong_bao`
> *"Đăng ký thành công, chờ thẩm định"* (`:351`), không dòng nào yêu cầu ghép mã vào câu thông báo; SCR-IV-02
> cell 7 (`:1522`) và §Postconditions (`:353–357`) cũng không nhắc. Đối chứng cho thấy khi SRS muốn kèm mã thì
> viết rõ: FR-IV-07 Processing bước 2 (`:597`) *"gửi mail link kích hoạt … kèm mã số TVV"*; **web/dev hiện tại**:
> toast đúng nguyên văn *"Đăng ký thành công, chờ thẩm định"*, **không** kèm mã — mã `TVV-STP-AG-0004` chỉ có
> trong thân phản hồi máy chủ.
>
> **Đề nghị BA chốt:** câu thông báo sau khi đăng ký có bắt buộc kèm mã hồ sơ không? Nếu có, bổ sung câu chuẩn
> vào §Outputs FR-IV-03 để dev và QA cùng một chuẩn.

### BA-3 (vế C10 — DIFF, chặn Pass)

> **CẦN BA CONFIRM:** đối tác kỳ vọng sau khi gửi đăng ký thành công, hệ thống chuyển sang **"trang theo dõi tiến
> độ"**; SRS quy định **ngược lại và ở mức BẮT BUỘC**: Phụ lục E §H7 (`srs-v3.5.md:6759`) *"Sau khi thực hiện
> thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông
> báo"*, ngoại lệ giữ lại trang Chi tiết chỉ hợp lệ khi *"có ghi chú riêng tại FR cụ thể"* — FR-IV-03 và SCR-IV-02
> (`srs-fr-04-chuyen-gia-tvv.md:280–363` và `:1470–1529`) **không** có ghi chú ngoại lệ nào; toàn bộ thư mục
> `srs-v3.5/` cũng không có màn nào tên "trang theo dõi tiến độ" cho luồng này (chuỗi này chỉ xuất hiện 1 lần ở
> `srs-fr-15-ct-htpldn.md:621`, thuộc nghiệp vụ đợt báo cáo CT HTPLDN); **web/dev hiện tại**: sau khi lưu, trang
> chuyển về `/chuyen-gia-tvv/danh-sach`, breadcrumb *Trang chủ / Mạng lưới Tư vấn viên / Danh sách*.
>
> **Đề nghị BA chốt 1 trong 2 hướng:** (a) giữ §H7 ⇒ sửa expected của đối tác về *"quay lại trang Danh sách tư vấn
> viên"*; hoặc (b) nghiệp vụ cần một màn theo dõi tiến độ hồ sơ cho Người hỗ trợ ⇒ BA định nghĩa màn đó và ghi
> ngoại lệ §H7 ngay tại FR-IV-03 trước khi verify lại.

---

## 5. Ghi nhận ngoài phạm vi chấm + candidate (không điều tra trong case này)

- **Nhãn nút submit:** ô TKM ghi *"BA xác nhận tên button sai"*, nhưng SRS v3.5 hiện hành vẫn quy định nhãn nút
  của SCR-IV-02 là **"Lưu"** (`srs-fr-04-chuyen-gia-tvv.md:1522` + quy ước chung BẮT BUỘC `srs-v3.5.md:6756` §H4);
  chuỗi "Gửi đăng ký" **0 kết quả** trên toàn thư mục `srs-v3.5/`. Web đang đúng SRS hiện hành ở điểm này.
  Quyết định BA chỉ có hiệu lực khi đã nhập vào chính bản SRS ⇒ **không phải bug, không phải vế Cn, không đo**.
- **Candidate 1:** toàn bộ form nhập bị **xóa trắng** (không lỗi, không request) ngay sau lượt chụp ảnh full-page
  của công cụ đo — nghi do thao tác chụp làm remount component; đã nhập lại và lưu bình thường. Ngoài vế Cn.
- **Candidate 2:** câu thông báo thực tế gửi CB NV là *"Hồ sơ tư vấn viên mới cần thẩm định / Hồ sơ TVV {tên} vừa
  được tạo và đang chờ thẩm định"*, khác câu SRS `:1522` *"Hồ sơ tư vấn viên mới đăng ký: [tên]"*. Câu chữ thông
  báo **không nằm trong expected** của case ⇒ không thành tiêu chí chấm.

---

## 6. Cổng chốt verdict

| # | Câu hỏi cổng | Trả lời |
|---|---|---|
| 1 | Neo dòng SRS nào? | C1 `:326`/`:354`/`:361`/`:2329` · C2 `:296`/`:1490`/`:1381-1386`/`:2019`/`:137` · C3 `:349`/`:1350` · C4 `:309`/`:1517` · C5 `:310`/`:1515` · C6 `:327`/`:356` · C7 `:328`/`:2514` · C8 `:351` · C9 IM LẶNG (`:348` vs `:351`) · C10 `srs-v3.5.md:6759` |
| 2 | Thao tác có ánh xạ vế Cn? | Có — 1 lượt tạo hồ sơ (C1/C3/C4/C5/C8/C9/C10) + 1 lượt đọc dropdown (C2) + 2 lượt đọc side-effect (C6, C7). Không thao tác thừa |
| 3 | Vế DIFF/GAP chặn Pass + có câu hỏi BA? | Rồi — C2 → BA-1, C10 → BA-3 (DIFF, cấm Pass); C9 → BA-2 (GAP) |
| 4 | Đã đọc đủ expected + phản hồi? | Rồi — Mô tả, Các bước ("nhấn Lưu"), KQ mong đợi (10 vế), `Trạng thái` Fail, `Dopai` N/R, `Trạng thái dev fix` Fixed, ô TKM ("BA xác nhận tên button sai" + "các trường thông tin không đúng thiết kế") |
| 5 | Điều kiện đo khớp tiền đề case? | Vai trò NHT cấp ĐP + màn `/chuyen-gia-tvv/tao-moi` khớp bằng chứng đối tác. Khác env/bản dựng — đã ghi giới hạn hiệu lực §3 |
