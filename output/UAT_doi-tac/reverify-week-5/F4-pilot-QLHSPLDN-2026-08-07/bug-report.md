# Bug Report — Hồ sơ pháp lý DN (lô chạy thử Flow 04 · 5 case QLHSPLDN_11→15)

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Môi trường** | https://18.143.165.120.nip.io — **env nội bộ**, KHÔNG phải env nghiệm thu của đối tác (`htpldn-uat.ospgroup.vn`) |
| **Bản dựng** | `HTPLDN · V1.0.9` · bó mã FE `assets/index-CxS5qW_0.js` · `etag W/"6a748299-112804"` · `last-modified: Thu, 06 Aug 2026 12:48:25 GMT` (19:48 giờ VN) · `/index.html` `etag W/"6a748299-428"` cùng mốc · `server: nginx/1.27.5`, `via: 1.1 Caddy`. **Khác vân tay lô tuần 5 hôm trước** (`V1.0.8`, `index-DIABnbIr.js`, 07:13:15 GMT) ⇒ FE đã dựng lại giữa 07:13 và 12:48 GMT ngày 06/08 |
| **Người test** | QA (Chrome DevTools MCP) |
| **Ngày** | 2026-08-07 00:11:53 |
| **Loại test** | Verify bug dev đã fix, không có hồ sơ nội bộ (flow `flows/04-verify-bug-dev-fix-khong-ho-so.md`) |
| **Round** | Tuần 5 — lô chạy thử Flow 04 ngày 2026-08-07 |
| **Tài liệu tham chiếu** | SRS bản chốt `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` (FR-X.1-04) · `srs-fr-07-doanh-nghiep.md` (SCR-V.III-02) · bảng `bug` (gid 1714340219) dòng 293→297 · [`ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md`](../ba-confirm/ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md) · [bao-cao-lo-2026-08-07.md](bao-cao-lo-2026-08-07.md) |

---

## Tổng hợp

Lô 5 dòng cùng một thẻ màn hình: *Chi tiết doanh nghiệp → tab **Hồ sơ pháp lý*** (`/doanh-nghiep/{id}?tab=ho-so-pl`,
`SCR-V.III-02` — nơi duy nhất còn thực thi `FR-X.1-04` sau khi `SCR-X1-03` bị gỡ, `srs-fr-12:560`, `:1205`).
Đối tác báo 2 cụm triệu chứng trên env nghiệm thu ngày 17/07/2026: *"Không có trường thông tin tìm kiếm trên
màn hình"* (dòng 293-295) và *"Màn hình không có nút chức năng"* (dòng 296-297).

Đo lại 2026-08-07 00:02→00:11 trên env nội bộ bản dựng `V1.0.9`, tài khoản `cbnv_tw_02`, DN `DN-HNI-0001`
(8 hồ sơ pháp lý), **không seed gì**: thẻ nay có đủ ô tìm kiếm + 4 bộ lọc + nút `Tìm kiếm` / `Xóa bộ lọc` /
`Xuất Excel`. **4 dòng Pass** (293 · 294 · 295 · 296 → `Trạng thái dev fix = Test done`), **1 dòng chờ BA**
(297 → `Trạng thái dev fix = BA confirm`; SRS im lặng về câu chữ khi xuất Excel với bộ lọc rỗng, xem
[`ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md`](../ba-confirm/ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md)).
Ô `Dopai` của dòng 297 **giữ nguyên `N/R`** — công cụ ghi chặn (chỉ cho ghi cột này từ `dev done`), chủ việc
chốt không nới guard.

> **Hiệu lực:** kết quả chỉ có giá trị cho env nội bộ + bản dựng ghi ở đầu file. Đối tác nghiệm thu trên
> `htpldn-uat.ospgroup.vn` ⇒ đây là **Pass tạm**, phải xác nhận lại khi bản dựng này lên env nghiệm thu.
> Không có ảnh "lỗi cũ" do QA tự chụp ⇒ hồ sơ này **chỉ kết luận hiện trạng đúng/sai so với đặc tả**, không
> kết luận bản vá có tác dụng hay không.

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 4    | 0        | 2     | 2      | 0     | 0       | 4      | 0    |

## Bug Summary Table

| Bug ID | Severity | Priority | Type | TC Ref | **SRS Reference** | Title | Status |
|--------|----------|----------|------|--------|-------------------|-------|--------|
| ~~BUG-HSPLDN-QLHSPLDN-11~~ | Major | P2 | Chức năng | QLHSPLDN_11 (tab `bug` dòng 293) | `FR-X.1-04 §Inputs — Tìm kiếm` (`srs-fr-12-tv-chuyen-sau.md:589-597`) · `§Processing — Tìm kiếm` (:638-645) · `§AC` (:710, :711) · `SCR-V.III-02` (`srs-fr-07-doanh-nghiep.md:468`) | Thẻ Hồ sơ pháp lý DN không có ô tìm kiếm và bộ lọc nên không tìm kiếm được hồ sơ | **Closed** |
| ~~BUG-HSPLDN-QLHSPLDN-12~~ | Medium | P3 | Chức năng | QLHSPLDN_12 (tab `bug` dòng 294) | `FR-X.1-04 §Error Handling E7 INF-HSPL-01` (`srs-fr-12-tv-chuyen-sau.md:701`) · `§Inputs — Tìm kiếm` (:589-597) | Không có ô tìm kiếm nên không kiểm được thông báo khi tìm không ra hồ sơ nào | **Closed** |
| ~~BUG-HSPLDN-QLHSPLDN-13~~ | Medium | P3 | Chức năng | QLHSPLDN_13 (tab `bug` dòng 295) | `FR-X.1-04 §Error Handling E6 ERR-HSPL-06` (`srs-fr-12-tv-chuyen-sau.md:700`) · `§Inputs — Tìm kiếm` ràng buộc `tu_ngay <= den_ngay` (:596) | Không có bộ lọc khoảng ngày nên không kiểm được cảnh báo khi ngày bắt đầu sau ngày kết thúc | **Closed** |
| ~~BUG-HSPLDN-QLHSPLDN-14~~ | Major | P2 | Chức năng | QLHSPLDN_14 (tab `bug` dòng 296) | `FR-X.1-04 §Processing — Xuất Excel` (`srs-fr-12-tv-chuyen-sau.md:657-665`, cột tệp tại :664, giới hạn 10.000 dòng tại :663) | Thẻ Hồ sơ pháp lý DN không có nút Xuất Excel nên không xuất được danh sách | **Closed** |

---

## ~~BUG-HSPLDN-QLHSPLDN-11~~ [CLOSED] — Thẻ Hồ sơ pháp lý DN không có ô tìm kiếm và bộ lọc nên không tìm kiếm được hồ sơ

> **Re-test:** 2026-08-07 14:14→14:20 — ✅ PASS trên env nghiệm thu htpldn-uat.ospgroup.vn (bó mã `assets/index-D4NhKEjr.js`, `last-modified Fri, 07 Aug 2026 04:17:55 GMT`, `HTPLDN · V1.0.10`, vân tay đầu = cuối case; tài khoản `cbnv_tw`; DN `DN-XX-0005` — chính DN trong bằng chứng đối tác, 4 hồ sơ, chỉ đọc, KHÔNG seed). Đã chạy đủ 2 biến thể bắt buộc: từ khóa `202608` → bảng 4→3 dòng, rồi giữ từ khóa + chọn thêm *Trạng thái = Hiệu lực* → 3→2 dòng; mỗi lượt `meta.total` và danh sách mã trong phản hồi của chính lệnh tìm trùng khít bảng, tham số lọc có mặt thật trong lệnh gửi lên ⇒ lọc chạy phía máy chủ và áp đồng thời cả hai điều kiện (`:644`, `:711`).

### Mô tả

Thẻ **Hồ sơ pháp lý** trong màn *Chi tiết doanh nghiệp* (`SCR-V.III-02`, `srs-fr-07-doanh-nghiep.md:455`,
`:468` — tab này là **CRUD** hồ sơ pháp lý DN) là nơi duy nhất còn thực thi `FR-X.1-04` sau khi màn cũ
`SCR-X1-03` bị gỡ (`srs-fr-12-tv-chuyen-sau.md:560`, `:1205`). Đặc tả yêu cầu chức năng này có **tìm kiếm**
(`srs-fr-12:563`) với **5 điều kiện lọc** — từ khóa, loại hồ sơ, doanh nghiệp, khoảng ngày, trạng thái
(`:589-597`) — xử lý *"áp dụng tất cả bộ lọc"* và *"AND logic cho tất cả điều kiện"* (`:643`, `:644`), tiêu
chí chấp nhận `:710`: *"Given CB NV tìm kiếm theo từ khóa When nhập keyword Then kết quả matching trong phạm
vi đơn vị"*.

Đối tác báo trên env nghiệm thu ngày 17/07/2026: **màn hình không có trường thông tin tìm kiếm** ⇒ bước 4 của
phiếu (*"NSD nhập từ khóa và/hoặc chọn bộ lọc"*) không thực hiện được.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`) — ô *Tác nhân* của đặc tả là *"Cán bộ
   Nghiệp vụ (TW/BN/ĐP), Người hỗ trợ"* (`srs-fr-12:565`).
2. Menu trái → **Doanh nghiệp** → mở chi tiết một doanh nghiệp có sẵn hồ sơ pháp lý.
3. Chọn thẻ **Hồ sơ pháp lý**.
4. Nhập từ khóa khớp một phần mã/tên hồ sơ rồi chạy tìm kiếm.

### Kết quả mong đợi

Thẻ có ô nhập từ khóa và các bộ lọc theo `srs-fr-12:589-597`; chạy tìm kiếm thì bảng chỉ còn các hồ sơ khớp
điều kiện, trong phạm vi đơn vị (`:643`, `:644`, `:710`).

### Kết quả thực tế

**Trên bản dựng đối tác chụp (env nghiệm thu, 17/07/2026):** thẻ chỉ có tiêu đề *Hồ sơ pháp lý DN*, nút
`Thêm hồ sơ`, bảng và phân trang — không có ô tìm kiếm hay bộ lọc nào.

**Trên bản dựng đo lại (`V1.0.9`, env nội bộ, 2026-08-07 00:05→00:06): đã hết lỗi.**

| Nhóm đo | Số đo |
|---|---|
| Ô nhập trong đúng vùng thẻ (đếm thô, chưa lọc) | **5** — `Tìm theo mã hoặc tên hồ sơ` · 2 ô của khung chọn · `Từ ngày` · `Đến ngày` |
| Khung chọn trong vùng thẻ | **2** — *Loại hồ sơ* · *Trạng thái* |
| Nút trong vùng thẻ | `Thêm hồ sơ` · `Tìm kiếm` · `Xóa bộ lọc` · `Xuất Excel` + `Xem`/`Sửa`/`Xoá` từng dòng + 2 nút phân trang |
| Số dòng bảng trước khi lọc | **8** (máy chủ `meta.total = 8`) |
| Sau khi gõ từ khóa `QA-W5` và bấm *Tìm kiếm* | **2** — `HSPL-20260806-0001` *QA-W5-1926 ten moi* · `HSPL-20260803-0001` *QA-W5-1911 ten* |
| Đối chứng độc lập (đọc phản hồi máy chủ) | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=829abcac-…&keyword=QA-W5&pageSize=100` → 200, `meta.total = 2`, `data[].maHoSo` đúng 2 mã trên ⇒ **lọc chạy phía máy chủ**, tham số `keyword` được truyền thật |

Hai đường đo khớp nhau ⇒ dừng, không đo đường thứ ba.

### Bằng chứng

| Tệp | Thấy gì |
|---|---|
| [`image/QLHSPLDN_11-the-hoso-phaply-DN-HNI-0001-baseline-8dong.png`](image/QLHSPLDN_11-the-hoso-phaply-DN-HNI-0001-baseline-8dong.png) | 00:05 — thẻ *Hồ sơ pháp lý DN* của `DN-HNI-0001` trước khi lọc: đủ ô từ khóa, 2 khung chọn, 2 ô ngày, nút `Tìm kiếm` / `Xóa bộ lọc` / `Xuất Excel`, bảng **8 dòng** |
| [`image/QLHSPLDN_11-C1-timkiem-QA-W5-ra-2-dong.png`](image/QLHSPLDN_11-C1-timkiem-QA-W5-ra-2-dong.png) | 00:06 — sau khi gõ `QA-W5` và bấm *Tìm kiếm*: bảng còn **2 dòng** đúng 2 mã hồ sơ khớp từ khóa |
| [`image/c1-keyword-response.network-response`](image/c1-keyword-response.network-response) | Phần thân phản hồi gốc của lệnh tìm kiếm: `success:true`, `meta.total = 2` |

---

## ~~BUG-HSPLDN-QLHSPLDN-12~~ [CLOSED] — Không có ô tìm kiếm nên không kiểm được thông báo khi tìm không ra hồ sơ nào

> **Re-test:** 2026-08-07 14:36 — ✅ PASS trên env nghiệm thu htpldn-uat.ospgroup.vn. Bản dựng `assets/index-D4NhKEjr.js` (`last-modified Fri, 07 Aug 2026 04:17:55 GMT`, vân tay đầu = cuối) · `cbnv_tw` · `DN-XX-0005` 4 hồ sơ, chỉ đọc, KHÔNG seed: từ khóa rác `zzqqxx-khongtontai` → bảng 4 → **0 dòng**, chữ đọc bằng `innerText` khớp `:701` **0 ký tự lệch** (36/36 điểm mã, cả sau chuẩn hoá NFC), đối chứng máy chủ của chính lệnh tìm `total = 0` · `data = []` · HTTP 200. Câu báo là **trạng thái cuối** (còn nguyên ở +4s / +7s / +~80s, `offsetParent !== null`), và loại được ca chuỗi cứng vì cùng ô đó với từ khóa khác vẫn trả 3–4 hồ sơ.

### Mô tả

`FR-X.1-04` quy định nhánh **không có kết quả tìm kiếm** trả mã `INF-HSPL-01` với câu chữ
*"Không tìm thấy hồ sơ pháp lý phù hợp"*, mức INFO (`srs-fr-12-tv-chuyen-sau.md:701`). Đối tác báo trên env
nghiệm thu ngày 17/07/2026 rằng thẻ **không có trường thông tin tìm kiếm**, nên bước 4 của phiếu không chạy
được và nhánh rỗng không kiểm được.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`).
2. Menu trái → **Doanh nghiệp** → mở chi tiết một doanh nghiệp → thẻ **Hồ sơ pháp lý**.
3. Nhập từ khóa chắc chắn không khớp bản ghi nào (ví dụ `zzqqxx-khongtontai`) rồi bấm **Tìm kiếm**.

### Kết quả mong đợi

Bảng không còn dòng nào và hệ thống hiển thị đúng câu *"Không tìm thấy hồ sơ pháp lý phù hợp"*
(`srs-fr-12:701`).

### Kết quả thực tế

**Trên bản dựng đối tác chụp (env nghiệm thu, 17/07/2026):** không thao tác được vì thẻ không có ô tìm kiếm.

**Trên bản dựng đo lại (`V1.0.9`, env nội bộ, 2026-08-07 00:06→00:07): đã hết lỗi.**

| Nhóm đo | Số đo |
|---|---|
| Số dòng bảng sau khi lọc từ khóa rác | **0** |
| Chữ hiển thị khi rỗng (đọc bằng `innerText`, không lấy `textContent`) | nguyên văn `Không tìm thấy hồ sơ pháp lý phù hợp` |
| So từng ký tự với chuỗi đặc tả `srs-fr-12:701` | `exactMatch = true`, danh sách ký tự lệch **rỗng** |
| Đối chứng độc lập (phản hồi máy chủ) | `GET /api/v1/ho-so-phap-ly-dns?doanhNghiepId=829abcac-…&keyword=zzqqxx-khongtontai&pageSize=100` → 200, `{"success":true,"data":[],"meta":{...,"total":0,"totalPages":0}}` |

Lần thao tác đầu ô từ khóa bị **nối chuỗi** vào giá trị cũ (`QA-W5zzqqxx-khongtontai`) do cách điền của công
cụ; đã xoá sạch ô rồi đo lại — số liệu ghi ở đây là của lượt đo sạch với đúng `keyword=zzqqxx-khongtontai`.

### Bằng chứng

| Tệp | Thấy gì |
|---|---|
| [`image/QLHSPLDN_12-C2-khong-tim-thay-thongbao.png`](image/QLHSPLDN_12-C2-khong-tim-thay-thongbao.png) | 00:06 — ô từ khóa đang chứa `zzqqxx-khongtontai`, bảng rỗng và hiện đúng dòng chữ *Không tìm thấy hồ sơ pháp lý phù hợp* |
| [`image/c2-keyword-rac-response.network-response`](image/c2-keyword-rac-response.network-response) | Thân phản hồi gốc: `data: []`, `total: 0` |

---

## ~~BUG-HSPLDN-QLHSPLDN-13~~ [CLOSED] — Không có bộ lọc khoảng ngày nên không kiểm được cảnh báo khi ngày bắt đầu sau ngày kết thúc

> **Re-test:** 2026-08-07 15:00 — ✅ PASS trên env nghiệm thu htpldn-uat.ospgroup.vn. Thẻ Hồ sơ pháp lý của `DN-XX-0005` đã có 2 ô ngày: đặt *Từ ngày* `31/12/2026` > *Đến ngày* `01/01/2026` rồi bấm **Tìm kiếm** → đúng **1** thông báo, nguyên văn *"Ngày bắt đầu phải trước ngày kết thúc"* (0 ký tự lệch, 37/37 điểm mã, kể cả sau chuẩn hoá `NFC`), bảng giữ nguyên 4 hàng, **0 lệnh nghiệp vụ**; lượt bấm lặp y hệt và ca "nhân đôi thông báo" đã loại bằng định danh node + điểm danh DOM 22 mẫu. Bản dựng `assets/index-D4NhKEjr.js` (`last-modified Fri, 07 Aug 2026 04:17:55 GMT`), vân tay đầu = cuối case, tài khoản `cbnv_tw`, chỉ đọc — **KHÔNG seed, không sửa/xoá bản ghi nào**.

### Mô tả

`FR-X.1-04` đặt ràng buộc `tu_ngay <= den_ngay` cho bộ lọc khoảng ngày (`srs-fr-12-tv-chuyen-sau.md:596`) và
quy định nhánh lỗi E6 — `tu_ngay > den_ngay (tìm kiếm)` → mã `ERR-HSPL-06`, câu *"Ngày bắt đầu phải trước ngày
kết thúc"*, mức ERROR (`:700`). Đối tác báo trên env nghiệm thu ngày 17/07/2026 rằng thẻ **không có trường
thông tin tìm kiếm**, nên bước 4 của phiếu (*"Ngày bắt đầu sau ngày kết thúc"*) không thực hiện được.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`).
2. Menu trái → **Doanh nghiệp** → mở chi tiết một doanh nghiệp → thẻ **Hồ sơ pháp lý**.
3. Đặt *Từ ngày* = `31/12/2026` và *Đến ngày* = `01/01/2026` (ngày bắt đầu sau ngày kết thúc).
4. Bấm **Tìm kiếm**.

### Kết quả mong đợi

Hệ thống từ chối tìm kiếm và báo đúng câu *"Ngày bắt đầu phải trước ngày kết thúc"* (`srs-fr-12:700`, ràng
buộc `:596`).

### Kết quả thực tế

**Trên bản dựng đối tác chụp (env nghiệm thu, 17/07/2026):** không thao tác được vì thẻ không có ô ngày nào.

**Trên bản dựng đo lại (`V1.0.9`, env nội bộ, 2026-08-07 00:07→00:08): đã hết lỗi.**

| Nhóm đo | Số đo |
|---|---|
| Ô chọn ngày trong vùng thẻ | **2** ô rời (*Từ ngày* · *Đến ngày*), không phải một khung chọn khoảng; ô không chặn nhập ngược |
| Số thông báo bắt được (bộ bắt cài trước khi bấm, **không lọc trùng**, đọc `innerText`) | **1** — nguyên văn `Ngày bắt đầu phải trước ngày kết thúc`, khớp tuyệt đối câu ở `:700` |
| Lỗi hiển thị kèm ô nhập (`.ant-form-item-explain-error`) | **0** |
| Lượt bấm lặp lần 2 | vẫn **1** thông báo — không nhân đôi |
| Đối chứng độc lập (đếm lượt gọi máy chủ) | **0** lượt gọi phát sinh ở cả 2 lần bấm; lượt gọi `ho-so-phap-ly-dns` gần nhất là lượt trước đó (`tuNgay=2026-12-31`) ⇒ giao diện chặn trước, không gửi truy vấn sai lên máy chủ |
| Tự kiểm bộ bắt thông báo | `soObserverDangSong = 1` ⇒ số liệu trên là của bộ bắt còn sống, không phải đếm hụt |

### Bằng chứng

| Tệp | Thấy gì |
|---|---|
| [`image/QLHSPLDN_13-C3-toast-ngay-batdau-truoc-ngay-ketthuc.png`](image/QLHSPLDN_13-C3-toast-ngay-batdau-truoc-ngay-ketthuc.png) | 00:08 — hai ô ngày đang là `31/12/2026` và `01/01/2026`, thông báo đỏ nguyên văn *Ngày bắt đầu phải trước ngày kết thúc* ở đầu trang |

---

## ~~BUG-HSPLDN-QLHSPLDN-14~~ [CLOSED] — Thẻ Hồ sơ pháp lý DN không có nút Xuất Excel nên không xuất được danh sách

> **Re-test:** 2026-08-07 00:09→00:10 — ✅ PASS (Closed-verified) · env nội bộ `18.143.165.120.nip.io` ·
> bản dựng `HTPLDN · V1.0.9`, bó mã `assets/index-CxS5qW_0.js`, `last-modified Thu, 06 Aug 2026 12:48:25 GMT` ·
> tài khoản `cbnv_tw_02` (`CB_NV_TW`) · dữ liệu DN `DN-HNI-0001` thẻ `?tab=ho-so-pl`, **8 hồ sơ** · bấm thật nút
> **Xuất Excel** → tải về `ho-so-phap-ly-dn-1786036166247.xlsx` (7007 byte) · **mở nội dung tệp**: hàng tiêu đề
> đúng **8 cột theo đúng thứ tự đặc tả**, thân tệp **8 dòng** khớp 8 bản ghi đang hiển thị · biến thể đã phủ:
> 1 lượt xuất không lọc (8/8 bản ghi) + 1 lượt xuất có lọc (ghi ở `BUG-HSPLDN-QLHSPLDN-15`, 2/8 bản ghi).
> **Chưa chạm ngưỡng 10.000 dòng** — toàn env chỉ có 12 hồ sơ pháp lý, không seed để thử ngưỡng. **KHÔNG seed gì.**
> **Hiệu lực:** Pass **tạm** cho env nội bộ + bản dựng trên; chưa xác nhận trên env nghiệm thu của đối tác.

### Mô tả

`FR-X.1-04` có khối xử lý riêng **Xuất Excel** (`srs-fr-12-tv-chuyen-sau.md:657-665`): áp dụng bộ lọc hiện tại
(`:662`), truy vấn tất cả bản ghi khớp **giới hạn tối đa 10.000 dòng** (`:663`), tạo tệp `.xlsx` với **8 cột**
*mã hồ sơ · tên · DN · loại · ngày cấp · hết hạn · trạng thái · cơ quan cấp* (`:664`) rồi trả tệp cho người
dùng (`:665`).

Đối tác báo trên env nghiệm thu ngày 17/07/2026: **màn hình không có nút chức năng** ⇒ bước 4 của phiếu
(*"Bấm nút Xuất Excel trên thẻ"*) không thực hiện được.

### Các bước tái hiện

1. Đăng nhập vai trò **Cán bộ Nghiệp vụ Trung ương** (`CB_NV_TW`).
2. Menu trái → **Doanh nghiệp** → mở chi tiết một doanh nghiệp có hồ sơ pháp lý → thẻ **Hồ sơ pháp lý**.
3. Bấm nút **Xuất Excel** trên thẻ.
4. Mở tệp tải về và đối chiếu hàng tiêu đề + số dòng với danh sách đang hiển thị.

### Kết quả mong đợi

Thẻ có nút **Xuất Excel**; bấm ra tệp `.xlsx` chứa đúng các bản ghi theo bộ lọc hiện tại, hàng tiêu đề đủ 8 cột
theo `srs-fr-12:664`, tổng số dòng không vượt 10.000 (`:663`).

### Kết quả thực tế

**Trên bản dựng đối tác chụp (env nghiệm thu, 17/07/2026):** thẻ chỉ có nút `Thêm hồ sơ`, không có nút Xuất Excel.

**Trên bản dựng đo lại (`V1.0.9`, env nội bộ, 2026-08-07 00:09→00:10): đã hết lỗi.**

| Nhóm đo | Số đo |
|---|---|
| Nút **Xuất Excel** trong đúng vùng thẻ | có, bấm được (trang này không có thanh công cụ của màn danh sách DN nên không nhầm nút của màn khác) |
| Kết quả bấm | thông báo *"Xuất Excel thành công"* + tải tệp `ho-so-phap-ly-dn-1786036166247.xlsx`, **7007 byte**, kiểu `…spreadsheetml.sheet` |
| **Nội dung tệp** — hàng tiêu đề | **8 cột, đúng thứ tự**: `Mã hồ sơ` · `Tên hồ sơ` · `Doanh nghiệp` · `Loại hồ sơ` · `Ngày cấp` · `Ngày hết hạn` · `Trạng thái` · `Cơ quan cấp` — khớp từng chữ với `:664` |
| **Nội dung tệp** — số dòng | **9 dòng = 1 tiêu đề + 8 dòng dữ liệu**, đúng 8 bản ghi đang hiển thị |
| Mẫu đối chiếu dữ liệu | dòng 2 `HSPL-20260806-0001 / QA-W5-1926 ten moi / Cong ty TNHH QA UAT Kiem Thu / Quyết định / 07/03/2026 / 05/08/2026 / Hết hạn / QA-W5-1926 coquan`; dòng cuối `HSPL-20260721-0001` |
| Đối chứng độc lập (đường gọi máy chủ) | `GET /api/v1/ho-so-phap-ly-dns/export?doanhNghiepId=829abcac-…` — tệp do máy chủ sinh, không phải ghép ở trình duyệt |
| Giới hạn **10.000 dòng** (`:663`) | **chưa đo được** — toàn env chỉ có 12 hồ sơ pháp lý; muốn chạm ngưỡng phải seed hơn 10.000 bản ghi, chi phí cao và nằm ngoài phạm vi lô |

### Bằng chứng

| Tệp | Thấy gì |
|---|---|
| [`image/QLHSPLDN_14-15-C4-C5a-loc-QA-W5-roi-xuat-excel.png`](image/QLHSPLDN_14-15-C4-C5a-loc-QA-W5-roi-xuat-excel.png) | 00:10 — thẻ có nút *Xuất Excel*; ảnh chụp ở lượt xuất **có lọc** (ô từ khóa `QA-W5`, bảng 2 dòng) kèm thông báo *Xuất Excel thành công* đang tan |
