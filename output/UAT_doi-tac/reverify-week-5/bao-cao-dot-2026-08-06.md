# Báo cáo cuối đợt — verify bug dev đã fix (tuần 5 · 2026-08-06)

| Thông tin | Giá trị |
|---|---|
| **Luồng áp dụng** | [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../flows/04-verify-bug-dev-fix-khong-ho-so.md) |
| **Bảng nguồn** | Google Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** (gid `1714340219`) |
| **Bộ lọc phạm vi** | `Dopai = dev done` **và** `Trạng thái dev fix = fixed` → **7 dòng** khớp. Không module nào đủ 3 case (nhiều nhất `QLHSPLDN`: 2) ⇒ chạy **2 module / 3 case** đúng trần user đặt |
| **Case đã chạy** | `QLHSPLDN_06` (dòng 291) · `QLHSPLDN_07` (dòng 292) · `QLBMHD_02` (dòng 138) |
| **Môi trường đo** | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải env nghiệm thu `htpldn-uat.ospgroup.vn`) |
| **Bản dựng** | `HTPLDN · V1.0.8` · bó mã `assets/index-DIABnbIr.js` · `GET /` `last-modified Thu, 06 Aug 2026 07:13:15 GMT` · `etag W/"6a74340b-428"` — đo **3 lần** (18:54 · 19:24 · 19:41), **không đổi** giữa đợt ⇒ 3 verdict cùng một bản dựng, được phép đặt cạnh nhau |
| **Tài khoản ra verdict** | `cbnv_tw` (`CB_NV_TW`, cấp TW, đơn vị `…8000-000000000001` *Cục Bổ trợ tư pháp - Bộ Tư pháp*) cho cả 3 case · `admin` chỉ **đọc** Nhật ký hệ thống ở vế (c) của `QLHSPLDN_07` |
| **Hồ sơ chi tiết** | [`bug-report.md`](bug-report.md) · [`tieuchi/`](tieuchi/) · [`ba-confirm/cau-hoi-ba-tuan-5.md`](ba-confirm/cau-hoi-ba-tuan-5.md) · [`BAN-DUNG.md`](BAN-DUNG.md) |
| **Thời gian chạy** | 18:44 → 19:41 (giờ VN) ngày 06/08/2026 |

---

## 1. Kết quả từng case

| Mã TC | Dòng | Verdict | Đã ghi lên bảng | Đọc lại xác nhận |
|---|---|---|---|---|
| `QLHSPLDN_06` | 291 | ✅ **Pass** | `Trạng thái dev fix` = **Test done** · `Kết quả verify` = ghi | ✅ |
| `QLHSPLDN_07` | 292 | ✅ **Pass** | `Trạng thái dev fix` = **Test done** · `Kết quả verify` = ghi | ✅ |
| `QLBMHD_02` | 138 | ✅ **Pass** | `Dopai` = **dev done** · `Trạng thái dev fix` = **Test done** · `Kết quả verify` = ghi | ✅ |

Ô chỉ đọc (`Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`) — **đã đọc lại
cả 3 dòng sau khi ghi, nguyên vẹn**, không dòng nào bị đè.

### 1.1 `QLHSPLDN_06` (dòng 291 — *"Xem"*) — **Pass**

Case gộp **4 vế**: có nút xem chi tiết · bấm mở được · nội dung khớp hồ sơ gốc + tệp đính kèm · chế độ chỉ đọc.

**Quan sát quyết định verdict:**

- **Mọi hàng đều có điều khiển mở chi tiết** — đếm thô **7/7 hàng** của `DN-HNI-0001` (không lấy mẫu), **2 cách
  đếm độc lập cùng ra 7**; từng nút `disabled=false`, kích thước thật 68×24 px, nằm trong khung nhìn.
- **Nội dung khớp bản ghi gốc 10/10 trường** trên **cả 3 hồ sơ** mở thật, đối chiếu với `GET /api/v1/ho-so-phap-ly-dns/{id}`
  đọc lại trong cùng phiên; không trường nào lọt `null` / `undefined` / mã enum thô.
- **Tệp đính kèm khớp cả số lượng, tên và dung lượng** (`QA-EDIT-A-tep-moi.png` 191 B); hồ sơ không tệp hiện
  đúng chữ *"Chưa có tệp đính kèm"*, không trắng màn.
- **Chỉ đọc thật**: đếm thô trong cửa sổ = **0 ô nhập**, danh sách nút chỉ có `Xem`/`Tải`/`Đóng` ⇒ **hết bất
  đồng ở vế này, không phải hỏi BA**.
- Phủ **4/4 dạng** (có tệp · không tệp · đủ 3 trạng thái *Hiệu lực/Thu hồi/Hết hạn* · trường tuỳ chọn trống).

**Bằng chứng:** `image/QLHSPLDN_06-D1-chitiet-HSPL-20260803-0001-co-tep.png` ·
`image/QLHSPLDN_06-D2D4-chitiet-HSPL-20260803-0002-khong-tep-truong-trong.png` ·
`image/QLHSPLDN_06-D3-chitiet-HSPL-20260721-0001-het-han.png` · [`tieuchi/QLHSPLDN_06.md`](tieuchi/QLHSPLDN_06.md).

### 1.2 `QLHSPLDN_07` (dòng 292 — *"Sửa"*) — **Pass**

Case gộp **3 vế**: cửa sổ sửa mở kèm dữ liệu hiện có · bấm lưu thì **cập nhật thật** · **lưu vết** thao tác.

**Quan sát quyết định verdict:**

- **Triệu chứng đối tác không tái hiện.** Lượt lặp **đúng thao tác nêu trong phiếu** (chỉ thêm 1 tệp, không
  đụng ô nào) cho ra **đủ 2 tệp** ở **cả hai đường đo độc lập**.
- **Mỗi lượt đo 2 đường và cả 2 khớp**: (i) tải lại trang **bỏ bộ nhớ đệm** rồi mở lại cửa sổ · (ii) đọc lại
  bản ghi từ máy chủ **theo đúng đường dẫn giao diện phát ra** (không đoán tên khoá — khoá thật là `fileDinhKem`).
- **5 lần bấm lưu / tạo** (19:05:18 · 19:09:45 · 19:12:03 · 19:16:57 · 19:22:13) trên **2 bản ghi** (1 cũ +
  1 tạo mới **sau bản vá**), phủ **5/5 dạng**: chỉ-thêm-tệp · ô chữ · ô ngày · ô chọn/enum/FK · bản ghi mới ↔ cũ.
- **Mỗi lần lưu chỉ 1 lời gọi máy chủ ↔ 1 thông báo** — bộ bắt thông báo cài **trước** khi bấm, tự kiểm
  `soObserverDangSong = 1`, không lọc trùng ⇒ không nuốt lỗi, cũng không double-toast.
- **Vế lưu vết đóng bằng Nhật ký hệ thống** (`SCR-VIII-10`): **5 dòng** ứng đúng 5 thao tác, **đúng giây bấm**,
  đúng người dùng + đơn vị + mã bản ghi.

**Bằng chứng:** `image/QLHSPLDN_07-D5-luot3-sau-tai-lai-trang-2-tep.png` ·
`image/QLHSPLDN_07-D5-luot3b-sau-tai-lai-trang-8-o-doi-3-tep.png` ·
`image/QLHSPLDN_07-veC-nhat-ky-he-thong-5-dong-thao-tac.png` · [`tieuchi/QLHSPLDN_07.md`](tieuchi/QLHSPLDN_07.md).

### 1.3 `QLBMHD_02` (dòng 138 — *"Kiểm tra hiển thị các trường thông tin"*) — **Pass**

Case gộp **3 vế**: thiếu cột *Cơ quan ban hành* · thiếu *Định dạng* · thiếu *ô tích chọn*.

**Căn cứ chốt — đặc tả BA đã cập nhật cho chính phiếu này.** Dấu `[STT12]` xuất hiện **5 chỗ** trong
`srs-fr-09-bieu-mau.md` (`:315` · `:482` · `:671` · `:672` · `:796`) và **cả 5 đều là *Cơ quan ban hành***;
grep toàn file **không có** thành phần nào tên *"Cột Định dạng"*. Khi BA phân xử định dạng trên đúng màn này
(mục `TKBMHD_03`, 24/07) thì phạm vi chốt là **bộ lọc** — mặc định *"Tất cả"* và **bỏ "PDF"** — nay `:654` đã
ghi đúng vậy. ⇒ yêu cầu của BA = **1 cột + sửa bộ lọc**, không phải 2 cột.

| Yêu cầu trong đặc tả **đã cập nhật** | Đo được | Đạt? |
|---|---|:-:|
| `:671` #20 Cột **Cơ quan ban hành** `[STT12]` | 12 ô tiêu đề, đúng **1** nhãn; **27/27 bản ghi** có giá trị; **2 đơn vị** (19 + 8) ⇒ bám `don_vi_id` của **bản ghi**; đối chứng máy chủ **0/20 dòng lệch** | ✅ |
| `:654` #3 bộ lọc **Định dạng** `doc/docx/xls/xlsx`, mặc định *"Tất cả"* | Đúng `Tất cả · DOC · DOCX · XLS · XLSX`, **không còn "PDF"**; lọc `XLSX` ra **3/3**, máy chủ `total = 3`; *Xóa bộ lọc* về **27** | ✅ |
| `:657` #6 Cột **Loại tài liệu** — *"**Icon** doc/xls"* | Có; `file-excel` (xanh lá) ↔ `file-word` (xanh dương), phân biệt được. Đặc tả chỉ định **biểu tượng**, app làm đúng | ✅ |
| `:650-673` danh sách **đóng 22 thành phần**, **không** khai ô tích chọn | Đếm thô `input[type="checkbox"]` = **0**; không có nhóm nút hàng loạt cấp biểu mẫu | ✅ |

**Điểm phụ *ô tích chọn* — không phải lỗi:** BA chốt **2026-07-24 Loại 3 — không sửa** (thao tác hàng loạt đặt
ở cấp thư mục, thiết kế có chủ đích); câu trả lời cho đối tác **đã nằm sẵn** trong ô *DEV phản hồi lần 1* của
chính dòng 138 ⇒ đối tác đã được thông báo.

**Hai tiêu chí của một Pass đều thoả:** (1) dev làm **đúng và đủ** phần đặc tả BA cập nhật; (2) **lỗi đối tác
log đã hết** — bản dựng họ chụp (`V1.0`, 13/07) hàng tiêu đề chỉ 8 nhãn, **không có** `Cơ quan ban hành`, và
đó cũng là điểm duy nhất phía TKM còn nêu ở lần retest **27/07**.

**Bằng chứng:** `image/QLBMHD_02-veA-cot-co-quan-ban-hanh-2-don-vi.png` ·
`image/QLBMHD_02-veB1-bo-loc-dinh-dang-4-gia-tri.png` · `image/QLBMHD_02-veB1-loc-XLSX-3-ket-qua.png` ·
[`tieuchi/QLBMHD_02.md`](tieuchi/QLBMHD_02.md).

> **Ghi lại một lần đi sai của chính đợt này:** verdict đầu tiên ghi **cần BA** vì (i) tưởng quyết định BA
> 24/07 về ô tích chọn chưa tới tay đối tác — sai, câu trả lời nằm ngay trong ô *DEV phản hồi lần 1* của dòng
> 138; và (ii) treo vế *"cột tên Định dạng"* theo một tiêu chí **chặt hơn đặc tả** (đòi đọc được bằng chữ,
> trong khi `:657` chỉ định **biểu tượng**). Cả hai được gỡ khi mở **bản đặc tả BA đã cập nhật**. Bài học:
> **trước khi treo BA, kiểm xem BA đã trả lời bằng cách sửa đặc tả chưa** — dấu thay đổi (`[STT12]`) nói rõ
> hơn mọi câu chữ trong thư trả lời.


---

## 2. Bug mới phát hiện trực tiếp trong luồng

**Không mở phiếu bug mới nào.** Chi tiết từng phát hiện + lý do không mở phiếu:

| # | Phát hiện | Xử lý | Vì sao không mở phiếu |
|---|---|---|---|
| 1 | Cột **Module** của Nhật ký hệ thống hiện *"Tư vấn"* cho `HO_SO_PHAP_LY_DN`, trong khi đặc tả `srs-fr-10-quan-tri.md:1387` khai giá trị `DN` | **Candidate BA** | Lệch nhãn hiển thị ↔ đặc tả, chưa rõ là lỗi gán nhóm hay đặc tả cũ ⇒ theo luồng phải hỏi trước khi quy lỗi |
| 2 | Sửa **chỉ thêm tệp** không làm đổi `ngayCapNhat` / `version` của bản ghi | **Candidate BA** | Vế lưu vết **đã đóng bằng Nhật ký hệ thống** (có dòng đúng giây bấm) ⇒ không hỏng nghiệp vụ; đặc tả không nói tệp đính kèm có phải "cập nhật bản ghi" hay không |
| 3 | Vài dòng nhật ký hiện `Dữ liệu cũ: —` | **Candidate BA** | Đặc tả không quy định bắt buộc chụp trạng thái trước với mọi loại thao tác |
| 4 | Biểu tượng / nhãn trợ năng cột `Loại TL` là chữ tiếng Anh (`file-excel` / `file-word`); đặc tả §H6 tự mâu thuẫn về yêu cầu biểu tượng | **Candidate BA** | Đặc tả mâu thuẫn nội bộ ⇒ cấm tự chọn nhánh |
| 5 | **4 ô lọc không có nhãn chữ** (cả 4 chỉ hiện `Tất cả`) và **chọn giá trị không tự lọc** — phải bấm *Tìm kiếm*, trong khi `:653`/`:654` ghi hành vi `change → filter` và bảng thành phần không khai 2 nút `Tìm kiếm`/`Xóa bộ lọc` đang có | **Candidate BA** (mục 3.1 · 3.2 phiếu BA) | Đặc tả **im lặng** về nhãn ô lọc; phần hành vi thì đặc tả ngược bản dựng ⇒ phải BA chốt sửa mã hay sửa đặc tả |
| 6 | Ô chọn **Thư mục** ở form *Thêm biểu mẫu* mời cả thư mục **đơn vị khác**; chọn xong bị máy chủ từ chối `422 ERR-BM-05` | **Trùng — đã ghi 25/07** (`reverify-week-3/dev-fix-reverify-round-7-2026-07-25/phat-hien-them.md` §5), tester khi đó quyết không mở phiếu | Máy chủ chặn **đúng** `BR-AUTH-08`; chỉ nhắc lại ở mục 3.3 phiếu BA |
| 7 | Máy chủ **từ chối đúng** tệp có nội dung không khớp phần mở rộng (*"Nội dung file không khớp định dạng…"*) | Ghi nhận **tích cực** | Hành vi đúng, không phải lỗi |

> **Một phép đo suýt thành phiếu sai:** sau `422 ERR-BM-05`, lần đọc đầu (dò DOM **sau** khi bấm) cho ra
> *"không thông báo, không lỗi trường"* và suýt trở thành phiếu *"nuốt lỗi"*. Đo lại đúng cách — cài bộ bắt
> thông báo **trước** khi bấm, tự kiểm `soObserverDangSong = 1`, **không lọc trùng**, dùng `innerText` — ra
> **`SO_REQUEST = 1` ↔ `SO_KHUNG = 1`** kèm đúng câu lỗi ⇒ **không phải lỗi**. Số đo đầu là *phép đo nói dối*.

---

## 3. Dữ liệu đã seed / thay đổi

Toàn bộ nằm trên **env nội bộ `18.143.165.120.nip.io`**. **Không đụng dữ liệu trên env nghiệm thu của đối tác**,
không sửa/xoá bản ghi có sẵn ngoài phạm vi khai dưới đây.

| Case | Bản ghi | Đổi gì | Ghi chú |
|---|---|---|---|
| `QLHSPLDN_06` | — | **Không seed, không thay đổi gì** | Dữ liệu sẵn có của `DN-HNI-0001` đã phủ đủ 4 dạng |
| `QLHSPLDN_07` | `HSPL-20260803-0001` (id `5bd8169a-0997-493b-8503-ddfcc7d5830a`, DN `DN-HNI-0001`) — **có sẵn từ trước** | **Sửa**: lượt 1 thêm **1 tệp**; lượt 2 đổi **8 ô** (số hiệu · cơ quan cấp · mô tả · loại hồ sơ · nguồn · ngày cấp · ngày hết hạn · trạng thái) + thêm **1 tệp** ⇒ tổng **+2 tệp**, giá trị mang dấu nhận dạng `QA-W5-1911 …` | Bản ghi test có sẵn của QA, không phải dữ liệu nghiệp vụ thật |
| `QLHSPLDN_07` | `HSPL-20260806-0001` (id `11a5f733-58ce-4ed2-b898-6580a259b612`) — **TẠO MỚI** 19:12:03 | Tạo bằng **UI thật** (nút *Thêm hồ sơ*), cùng DN + đơn vị TW; sau đó lượt 3a thêm 1 tệp, lượt 3b đổi **8 ô** (`QA-W5-1926 …`) + thêm 1 tệp ⇒ **3 tệp** | Cần bản ghi **sinh ra sau bản vá** để loại giả thuyết "dữ liệu cũ đóng băng trước fix" |
| `QLHSPLDN_07` | Tệp seed `QA-W5-1907-tep-luot1…luot5.png` | PNG **thật** (73–99 B), thư mục [`seed-files/`](seed-files/) | Bản `luot4` lần đầu tạo bằng `printf` là văn bản ASCII → máy chủ từ chối đúng ⇒ đã tạo lại bằng PNG thật |
| `QLBMHD_02` | `BM-20260806-001` *"QA-W5-1936 BM moi trong luot do"* — **TẠO MỚI** | Tạo bằng **UI thật** (nút *Thêm biểu mẫu*), thư mục `QA-R7-A-CO-BM` (đúng đơn vị), tệp `QA-W5-QLBMHD02-bieu-mau-moi.xlsx` (4.869 B) | Phủ dạng **bản ghi mới** + bổ sung mẫu XLSX. **Không** seed dạng "đơn vị khác" vì env đã sẵn 8/27 bản ghi của *Bộ Kế hoạch và Đầu tư* |

---

## 4. Case chưa chốt được

**Không còn case nào treo vì thiếu căn cứ.** Cả 3 case đều chốt được bằng đặc tả + quyết định BA có sẵn.
Phần còn lại chỉ là việc phải làm, không phải câu hỏi:

| Việc | Vì sao | Cần gì | Ai |
|---|---|---|---|
| **Ghi verdict Pass của `QLBMHD_02` lên dòng 138** | Dòng đang kẹt ở `Dopai` = **BA** + `Trạng thái dev fix` = **BA confirm** do verdict cần-BA ghi lúc 19:47 rồi **rút lại**. Công cụ `sheet_bug_verify_write.py` chặn đúng thiết kế: verdict `pass` chỉ ghi khi ô đang là `Fixed`; và **không có** đường đưa `Dopai` về `dev done` | Xem §5 | **Chủ việc quyết** |
| 8 mục **ghi nhận đồng bộ đặc tả** (`1.1`–`1.8` trong [`ba-confirm/cau-hoi-ba-tuan-5.md`](ba-confirm/cau-hoi-ba-tuan-5.md)) | Đều là chỗ đặc tả **im lặng hoặc tự mâu thuẫn**, không kéo verdict phiếu nào | BA chốt để đồng bộ văn bản | **BA** |
| 4 dòng còn lại trong phạm vi lọc (`dev done` + `fixed`) | **Chưa chạy — đúng trần user đặt** (tối đa 3 case / 1–2 module) | Đợt sau chạy tiếp, giữ nguyên bộ lọc | QA |

---

## 5. Ghi chú: đường ghi cho dòng 138 (verdict bị rút rồi ghi lại)

Dòng 138 từng bị ghi verdict **cần BA** lúc 19:47 (`Dopai` = BA · `Trạng thái dev fix` = BA confirm) rồi
**rút lại** khi mở bản đặc tả BA đã cập nhật. `sheet_bug_verify_write.py` **chặn đúng thiết kế** —
verdict `pass` chỉ nhận nguồn `Fixed`, và không verdict nào đưa `Dopai` về `dev done`; docstring của nó ghi
rõ *"Nới `WRITABLE_FROM` để lách là SAI"*. Theo flow 04 §Công cụ bị chặn: **đã dừng và báo chủ việc**, không
ghi tay, không viết script dùng-một-lần.

**Chủ việc chọn đường:** dùng [`tools/sheet_fix_row_fields.py`](../tools/sheet_fix_row_fields.py) — công cụ
đã commit sẵn, mục đích ghi rõ là *"sửa nhiều ô của một dòng đã có sẵn … dòng đã log rồi nhưng phải viết lại
nội dung"*, giữ nguyên bộ guard riêng: khớp spreadsheet + tab allow-list, dò cột theo **tên header thật**,
khớp `Mã TC`, validate từng giá trị theo dropdown, **cấm sửa cột `Mã TC`**, in `cũ → mới` toàn bộ, `--dry-run`
trước, **đọc lại sau ghi**, log append-only. Không đụng gì tới guard của công cụ verify.

Đã ghi 3 ô, đọc lại khớp; giá trị cũ nằm trong cả 2 nhật ký (`sheet_bug_verify_write.log` và
`sheet_fix_row_fields.log`) nên khôi phục được. 4 ô chỉ đọc của dòng 138 đã đọc lại — **nguyên vẹn**.


---

## Hiệu lực của kết quả

Cả **2 verdict Pass** chỉ có hiệu lực cho **env nội bộ `18.143.165.120.nip.io` + bản dựng `HTPLDN · V1.0.8`
(bó mã `assets/index-DIABnbIr.js`, `last-modified Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"`)**
⇒ là **Pass tạm** cho tới khi chính bản dựng này lên môi trường nghiệm thu của đối tác. Bản dựng đổi (bó mã
hoặc `last-modified` khác) ⇒ **đo lại từ đầu**, không gộp số đo của 2 bản dựng vào một verdict.
