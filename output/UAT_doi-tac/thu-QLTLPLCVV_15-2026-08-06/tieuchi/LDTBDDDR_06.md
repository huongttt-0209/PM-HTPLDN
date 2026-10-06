# Tiêu chí verify — LDTBDDDR_06

```
Mã case: LDTBDDDR_06 (tab `bug` dòng 205)      Thời điểm viết: 2026-08-06 13:45
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 13:47 → 14:01
Bản dựng (TỰ ĐO 2026-08-06 13:41 bằng curl, KHÔNG chép từ B5-CONTEXT):
  · index.html etag W/"6a73f6a4-428" · last-modified: Thu, 06 Aug 2026 02:51:16 GMT
  · bó mã: assets/index-CNwX9JjX.js · etag W/"6a73f6a4-1124fd" · 1 123 581 byte
  · DẤU VÂN TAY: md5 bó mã = e0e4f737b1fb7ab9409f459a4d0fa051
  · nhãn hiển thị trong app: **HTPLDN · V1.0.8** (đọc ở chân sidebar, cả 2 phiên vai trò)
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `tieuchi/CLDTBDDDR_06.md` — file tiêu chí của case **anh em** (màn *đang* diễn ra, FR-IX-06). Đọc để
>   tham khảo **cách trình bày** và **bẫy thao tác**. **Không** chép kết luận: khác màn, khác endpoint,
>   khác bộ lọc đặc thù, khác bộ chỉ số đầu ra.
> - `bug-report.md` §Phần 3 (`BUG-SLHDVM-006`) và §Phần 6 (`BUG-CLDTBDDDR-006`) — hai phiếu cùng gốc 403.
> - `cau-hoi-BA.md` — kiểm xem câu hỏi *"QTHT có được xuất báo cáo thống kê không"* đã mở chưa.
> - `B5-CONTEXT.md` §4 có nhắc **số đo cũ 03/08/2026** (bản dựng V1.0.4, env đối tác): tệp xuất khi đó tên
>   `bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu hẳn giờ-phút.
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ, KHÔNG lấy số đo cũ và KHÔNG lấy kết quả case anh em làm ngưỡng.**
> Kết quả của `CLDTBDDDR_06` chỉ chứng minh *"trên màn FR-IX-06, endpoint xuất chạy được với vai trò CB
> nghiệp vụ"* — nó **không** chứng minh gì cho FR-IX-07. Màn của tôi có bộ chỉ số khác (`tong_da_dien_ra`,
> `tong_hoc_vien`), bộ lọc đặc thù khác (chỉ **Hình thức**, không có Lĩnh vực) và tên loại BC khác.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** — 2 vế triệu chứng (2 vòng nghiệm thu, cùng thao tác bấm **[Xuất Excel]** trên màn
*Báo cáo thống kê → BC Lớp đào tạo **đã** diễn ra*) + 1 vế kỳ vọng về tên tệp:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo
  **"Forbidden"** ⇒ vẫn không có tệp; triệu chứng đổi từ *"lỗi tạo tệp"* sang *"bị chặn quyền"*.
- **Vế c (ô `Kết quả mong đợi`)** — *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.
  **Tên tệp xuất: `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx` hoặc `BaoCaoDaoTao_{YYYYMMDD_HHmm}.pdf`**"*

🔴 **Vế c đo được, KHÔNG đẩy sang BA.** BA đã chốt **2026-08-04** khuôn tên tệp cho nhóm IX và đặc tả đã sửa
theo (dấu `[BA chốt 2026-08-04]` nằm ngay trong `:85`, `:86`, `:1092`); ngày **2026-08-06** khuôn này còn được
nâng thành quy ước chung ở **Phụ lục E §H8** (`srs-v3.5.md:6716`). Đây là **áp quyết định có sẵn**, QA chấm được.

⚠️ **Đo theo KHUÔN, không đo theo chuỗi đối tác viết.** Đối tác viết cứng `BaoCaoDaoTao` — nhưng đặc tả chỉ
đòi `{TenBaoCao}` = *tên loại báo cáo* viết liền PascalCase, bỏ dấu, bỏ ký tự không phải chữ/số. Cấm chấm Fail
chỉ vì tên tệp không đúng y hệt chữ `BaoCaoDaoTao` (đó là **prescribe**, không phải yêu cầu nghiệp vụ).

### Bằng chứng — đã MỞ XEM full-res (2026-08-06 13:35)

| Vòng | Tệp | Thấy gì |
|---|---|---|
| **1** | ô `Ảnh/vieo 1` của dòng 205 ghi tên `CLDTBDDDR_06.jpg` — **trỏ đúng cùng tệp Drive với dòng 200** | Đã mở `partner-evidence/CLDTBDDDR_06.jpg`: URL `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-**dang**-dien-ra&…`, dropdown Loại báo cáo = *BC Lớp đào tạo **đang** diễn ra*, tiêu đề khối kết quả = *BC Lớp đào tạo **đang** diễn ra*, có **2 bộ lọc đặc thù** (Hình thức + Lĩnh vực), thẻ số liệu *Tổng số = 3*. ⇒ Đây là màn của **FR-IX-06**, tức bằng chứng của **case khác** (dòng 200) |
| **2** | `partner-evidence/LDTBDDDR_06_v2.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-**da**-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Loại BC = *BC Lớp đào tạo đã diễn ra*, Kỳ **Năm** 01/01/2026→31/12/2026, Đơn vị **Toàn quốc**, **chỉ 1 bộ lọc đặc thù = Hình thức** và đang **để trống**. Báo cáo đã render: *Kỳ: Năm • Khoảng thời gian: 01/01/2026 → 31/12/2026 • Đơn vị: Toàn quốc • Thời điểm tạo: **31/07/2026 14:56*** · thẻ **Tổng khóa học = 8** · thẻ **Tổng học viên = 15**. Khung thông báo đỏ **"Forbidden"** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0.3**. Đồng hồ máy: 02:56 PM 2026-07-31 |

🔴 **Kết luận cổng bằng chứng — vòng 1 KHÔNG có bằng chứng riêng cho case này.** Ô `Ảnh/vieo 1` dòng 205 dùng
chung đúng tệp Drive của dòng 200, và nội dung tệp là màn *đang diễn ra* (FR-IX-06) chứ không phải màn *đã
diễn ra* (FR-IX-07). Theo flow §Cổng bằng chứng ⇒ **vế a đi nhánh "đối tác không gắn bằng chứng"**:
- Nếu **tự tái hiện được** vế a trên màn của tôi ⇒ lỗi có thật, chạy tiếp bình thường, GAP coi như đóng.
- Nếu **không tái hiện được** ⇒ 🔴 **CẤM verdict *không phải lỗi* cho vế a** (flow cấm rõ ở nhánh này) —
  chỉ được kết luận **hiện trạng đúng/sai so với đặc tả** trên bản dựng đang đo.
- **Không** vì thiếu bằng chứng vòng 1 mà bỏ case: vế b có bằng chứng riêng đúng case, vế c đo được từ đặc tả.

⚠️ **Hai vòng KHÔNG so sánh được với nhau** (bắt buộc ghi theo flow §Cổng bằng chứng): vòng 1 không có ảnh
của chính case này nên không biết bản dựng / dữ liệu / bộ lọc lúc đó. Chỉ vòng 2 có đủ 3 dữ kiện neo.

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (+ Phụ lục E ở
`srs-v3.5.md`) — **đã mở file đọc đúng dòng 2026-08-06 13:38**, không lấy số dòng từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-11-bao-cao.md:62` | Preconditions chung — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"* |
| `:79` | Processing chung bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị"* (BR-AUTH-01) ⇒ kiểm quyền nằm **đầu luồng**, trước cả bước truy vấn và bước xuất |
| `:82` | Bước 4 — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* |
| `:85` | Bước 7 — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). **Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo"* `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` |
| `:86` | Bước 8 — PDF theo TT17/2025; *"Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo Phụ lục E §H8"* `[BA chốt 2026-08-04]` — *"`{TenBaoCao}` là tên loại báo cáo **viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số** (dấu `/`, khoảng trắng, dấu câu)"* |
| `:113` | E3 · Không có dữ liệu · **INF-RPT-01** · *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* · INFO |
| `:116` | E6 · Lỗi xuất file · **ERR-RPT-04** · *"Không thể tạo file xuất. Vui lòng thử lại"* · ERROR ⇒ đúng câu **vế a** |
| `:117` | E7 · Không có quyền · **ERR-RPT-05** · *"Bạn không có quyền xem báo cáo này"* · ERROR ⇒ nhánh quyền của **vế b** |
| `:123` | AC chung — *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (Phụ lục E §H8)"* |
| `:124` | AC chung — *"**Given** CB nhấn 'Xuất PDF' … **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`** (Phụ lục E §H8)"* |
| `:389` | **FR-IX-07: BC Lớp đào tạo ĐÃ diễn ra (UC130)** — màn hình SCR-IX-01 |
| `:398` | Mô tả — *"Báo cáo khóa học **đã kết thúc trong kỳ**, phân theo hình thức, đơn vị, **kèm tổng số học viên**"* |
| `:400` | **Tác nhân:** *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:408` | Input đặc thù — **chỉ 1 trường**: `hinh_thuc` ∈ {`TRUC_TUYEN`, `TRUC_TIEP`}, không bắt buộc. **Không có `linh_vuc`** (khác hẳn FR-IX-06) |
| `:410` | Công thức — *"Đếm khóa học **đã kết thúc trong kỳ**, tổng hợp số học viên"* |
| `:412` | Dimensions — *"Kỳ, Đơn vị, Hình thức, Số học viên"* |
| `:418`–`:422` | Output đặc thù, **điều kiện hiển thị "Luôn"** cả 5 dòng: `tong_da_dien_ra` (Tổng KH đã diễn ra) · `tong_hoc_vien` (Tổng số học viên) · `theo_don_vi[]` {don_vi, ten, so_kh, so_hv} · `theo_hinh_thuc[]` {hinh_thuc, so_kh, so_hv} · `theo_ky[]` {ky, so_kh, so_hv} |
| `:425` | AC bổ sung — *"**Given** CB chọn kỳ Quý **When** tạo BC **Then** hiển thị tổng KH + tổng HV, phân theo đơn vị + hình thức"* |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: **Sau khi đã 'Xem báo cáo'**"* (không kèm điều kiện vai trò) |
| `:1053` | SCR-IX-01 item 9 — *"Nút Xuất PDF · 'Xuất PDF (.pdf)' · **click → auto-download** · Điều kiện hiển thị: Sau khi đã 'Xem báo cáo'"* |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1070` | Mapping dropdown — **UC130 *BC Lớp đào tạo đã diễn ra*, bộ lọc đặc thù = *Hình thức* (CHỈ MỘT)**, biểu đồ *Bar + Trend*. (So sánh: dòng ngay trên, `:1069`, UC129 *đang diễn ra* có **Hình thức, Lĩnh vực**) |
| `:1092` | Quy tắc tương tác — *"Export XLSX/PDF **chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file**… Tên tệp cả hai định dạng theo Phụ lục E §H8 — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`"* `[BA chốt 2026-08-04]` |
| `:1268` | BR-AUTH-08 — cột *Ngoại lệ* ghi **"QTHT bypass"**, cột *Áp dụng* ghi **"Toàn bộ FR-IX"** |
| `:1280` | BR-DATA-06 — *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |
| `srs-v3.5.md:6716` | **Phụ lục E §H8 — Tên tệp xuất thống nhất** (BẮT BUỘC): *"Khuôn: `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (**kể cả dấu gạch nối**, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn… **Phần giờ-phút bắt buộc** để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa 255 ký tự"* `[BA chốt 2026-08-06]` |

**Rẽ nhánh — quyết TRƯỚC khi viết mục 4 (rẽ theo TỪNG VẾ):**

| Vế | Đặc tả | Verdict nhánh |
|---|---|---|
| **a** — *"Không thể tạo file xuất"* | **Nói rõ** và **khớp** kỳ vọng: `:1052` ghi thẳng *click → auto-download*, `:123` ghi *tải file .xlsx*; `:116` cho biết ERR-RPT-04 chỉ dành cho tình huống lỗi tạo tệp thật | Chấm được → viết mục 4. ⚠️ Nhưng vòng 1 **không có bằng chứng riêng** ⇒ cấm verdict *không phải lỗi* cho vế này |
| **b** — *"Forbidden"* | **Nói rõ** về **câu chữ** khi từ chối vì quyền: `:117` đòi thông báo tiếng Việt *"Bạn không có quyền xem báo cáo này"*. Dù nghiệp vụ chốt hướng nào thì chuỗi tiếng Anh thô cũng lệch dòng này | Chấm được → viết mục 4 |
| **c** — khuôn tên tệp | **Nói rõ** và **khớp** kỳ vọng, **BA đã chốt 2026-08-04** (+ §H8 2026-08-06). Áp quyết định có sẵn | Chấm được → viết mục 4 |

⚠️ **Một điểm KHÔNG chấm:** câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* là chỗ
đặc tả **tự mâu thuẫn** (`:62`/`:400` liệt kê tác nhân CB Nghiệp vụ / CB Phê duyệt ↔ `:1268` ghi ngoại lệ
*"QTHT bypass"* áp *"Toàn bộ FR-IX"*). Câu hỏi này **đã có mục sẵn** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
(mở lúc 12:40 khi verify `SLCTHT_06`, cùng nguyên nhân gốc) ⇒ **không mở mục trùng**. Mục đó **không kéo
verdict** của case: dù BA chốt hướng nào, hành vi hiện tại vẫn phải thoả `:117`.

**IM LẶNG về:**
- **Chữ chính xác của thông báo thành công** khi xuất được — `:1058` mô tả *"Xuất thành công"* ở bảng thành
  phần màn hình, nhưng bảng Error Handling **không** có mã INF/WRN tương ứng ⇒ không chấm Fail vì chữ khác.
- **Có bắt buộc hiện toast *"Đang tạo file…"* hay không** — cùng lý do trên.
- **Bố cục bên trong tệp**: tên sheet, thứ tự cột, cách trình bày bảng. Đặc tả chỉ quy định **header file**
  phải có tiêu đề BC + kỳ + đơn vị + ngày tạo (`:1092`).
- **Có bao nhiêu thẻ số liệu phải vẽ trên màn** — `:418`–`:422` quy định **output của báo cáo**, không quy
  định màn hình phải vẽ đủ 5 thẻ.

---

## 3. Precondition

- **Tài khoản ra verdict cho vế a + vế c:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương**
  (`CB_NV_TW`), cấp **TW**, phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-07 (`:400`).
  Fallback (Rule 7, **cùng vai trò + cùng cấp**): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Tài khoản bắt buộc dùng cho vế b:** vai trò **Quản trị viên · QTHT** — **chính vai trò đối tác dùng** ở
  vòng 2 (đọc từ góc phải trên ảnh `LDTBDDDR_06_v2.jpg`). Vế b là *"Forbidden"*, tức **triệu chứng phân
  quyền**; đo bằng vai trò khác thì không tái hiện được điều đối tác nêu.
  > **Vì sao không vướng quy tắc "tài khoản quản trị không ra verdict":** quy tắc đó chặn việc **quyền rộng
  > che lỗi phân quyền**. Ở đây chiều ngược lại — QTHT là vai trò **bị chặn**, dùng nó để **phơi** lỗi chứ
  > không che. Vế a và vế c vẫn ra verdict bằng `cbnv_tw_05`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**, Loại BC = *BC Lớp đào tạo
  **đã** diễn ra* (`loai=lop-dao-tao-da-dien-ra`). 🔴 **Không được nhầm sang *đang* diễn ra** — kiểm bằng cả
  3 chỗ: chuỗi trong URL · chữ trong dropdown · tiêu đề khối kết quả.
- **Dữ liệu tiền đề:** ≥1 **khóa học ĐÃ KẾT THÚC trong kỳ** (`:410`) thuộc bản ghi đã duyệt (`:82`), nằm
  trong phạm vi đơn vị. Kỳ rỗng → đó là `INF-RPT-01` hợp lệ (`:113`), **phải đổi kỳ/đơn vị** để có dữ liệu
  rồi mới đo nút xuất. **Mọi kỳ đều rỗng ⇒ GAP chưa đóng ⇒ verdict ô trống**, nêu rõ cần seed gì.
- **Bộ lọc neo theo đối tác (vòng 2):** Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = **Toàn quốc** ·
  Hình thức **trống**. Thao tác: [Xem báo cáo] → [Xuất Excel].
- **Cache máy chủ:** trước khi kết luận *"không có dữ liệu"*, kiểm trường **"Thời điểm tạo"** trên màn; nghi
  cache thì đổi `denNgay` 1 ngày để lấy khoá cache mới.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi `soObserverDangSong = 1`; **đếm thông báo theo mốc giờ khác nhau**, không theo số phần tử.
  > ⚠️ Bài học đã ghi ở `tieuchi/SLHDVM_06.md` §8 và `tieuchi/CLDTBDDDR_06.md` §8: bộ bắt kiểu *"nghe node
  > mới được thêm"* **bỏ sót** chữ *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**. Phải đo bù
  > bằng cách theo dõi **nội dung** vùng thông báo theo thời gian (`innerText`) + ghi hình học để chứng minh
  > người dùng nhìn thấy thật.
- ⚠️ **Bẫy thao tác đã biết** (ghi trước khi đo, để không log oan): nút **[Xuất PDF]** mở hộp thoại
  *"Tùy chọn in báo cáo PDF"* chứ **không** tải ngay; hộp thoại còn mở sẽ **nuốt cú bấm [Xuất Excel] kế
  tiếp**. Phải đóng hộp thoại trước khi bấm nút khác. Bấm bằng **chuột thật**, không dùng sự kiện giả lập.

---

## 4. Tiêu chí chấm

### ✅ PASS khi — **đủ cả 9 điều, trên đủ M = 3 dạng ở mục 5**

1. **Không báo lỗi tạo tệp, không bị chặn quyền (vai trò đặc tả cho phép).** Với `cbnv_tw_05`, sau khi
   [Xem báo cáo] ra dữ liệu, thao tác [Xuất Excel] **không** sinh thông báo mang nghĩa *không tạo được tệp*
   (nhánh `:116`) và **không** sinh thông báo mang nghĩa *từ chối quyền* (nhánh `:117`). Đo bằng bộ bắt thông
   báo: đọc **nguyên văn** chữ trên màn, đối chiếu với 2 câu ở `:116`/`:117` và 2 câu đối tác gặp
   (*"Không thể tạo file xuất. Vui lòng thử lại."*, *"Forbidden"*).
2. **Người dùng thật sự nhận được một tệp** (`:1052` *click → auto-download*): quan sát được ở phía người
   dùng — tệp rơi về thư mục tải xuống, **hoặc** phản hồi của chính thao tác đó là một tệp đính kèm
   (`content-disposition: attachment`) chứ không phải trang lỗi / JSON lỗi.
3. **Tệp mở được như một workbook .xlsx thật** — `openpyxl.load_workbook()` chạy được, đọc ra ≥1 sheet có ô
   không rỗng. (Mã 200 + có bytes **không** đủ.)
4. **Header tệp có đủ 4 thông tin `:1092` đòi**: ① tiêu đề báo cáo ② thông tin kỳ (kỳ + khoảng thời gian)
   ③ đơn vị ④ ngày tạo. Đo bằng cách đọc các ô đầu sheet và tìm đủ 4 mẩu thông tin đó.
5. **Số liệu trong tệp khớp số liệu đang hiện trên màn.** So từng cặp, tối thiểu **2 chỉ số tổng điều kiện
   "Luôn"** của FR-IX-07 (`:418`, `:419`): **Tổng khóa học đã diễn ra** và **Tổng số học viên**. Chỉ số nào
   màn không vẽ thẻ riêng thì lấy từ phản hồi của chính lần chạy báo cáo đó. Có bảng phân theo đơn vị / hình
   thức / kỳ trong tệp (`:420`–`:422`) thì **tổng các dòng phải cộng khớp** hai chỉ số tổng — cả cột số khóa
   học lẫn cột số học viên.
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280`): với 3 dạng ở mục 5, số liệu trong tệp **đổi theo** và mỗi
   lần đều khớp số trên màn của **chính lần đó** — không phải luôn trả bản không lọc. Kiểm chéo bằng md5 các
   tệp: 2 dạng cho số trên màn khác nhau mà tệp giống hệt ⇒ vi phạm.
7. **Tên tệp .xlsx đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (`:85`, `:123`, `:1092`, §H8
   `srs-v3.5.md:6716`) — lấy tên từ **nguồn người dùng thật thấy** (tệp rơi về máy, hoặc `content-disposition`
   của phản hồi). Đo đủ **4 điều kiện của khuôn**:
   - **7a.** Có đoạn thời gian `_YYYYMMDD_HHmm` ngay trước đuôi tệp: **8 chữ số ngày + `_` + 4 chữ số giờ-phút**,
     và **giá trị khớp thời điểm xuất** (không phải hằng số/ngày cũ). *Phần giờ-phút là bắt buộc.*
   - **7b.** Phần `{TenBaoCao}` chỉ gồm **chữ cái không dấu và chữ số**; **không** dấu gạch nối, **không**
     khoảng trắng, **không** dấu tiếng Việt, **không** dấu câu. Gạch dưới chỉ dùng để ngăn đoạn.
   - **7c.** Phần `{TenBaoCao}` **nhận ra được là tên của chính loại báo cáo này** — báo cáo lớp đào tạo
     **đã** diễn ra. 🔴 Tên tệp trỏ sang loại báo cáo khác (vd chuỗi mang nghĩa *đang diễn ra*) là **trượt**,
     vì `:85` đòi `{TenBaoCao}` là *tên loại báo cáo* của chính báo cáo được xuất.
     *(Cấm đòi đúng chuỗi `BaoCaoDaoTao` — đó là prescribe; đặc tả chỉ đòi "tên loại báo cáo".)*
   - **7d.** Đuôi tệp là `.xlsx` khi bấm [Xuất Excel]; tổng độ dài tên ≤ 255 ký tự.
   - **Phép thử chống đè tệp** (lý do BA chốt bắt buộc giờ-phút): xuất **2 lần cùng ngày ở 2 phút khác nhau**
     phải ra **2 tên tệp khác nhau**.
8. **Nút [Xuất PDF] — vế `hoặc .pdf` trong câu kỳ vọng của đối tác:** người dùng nhận được tệp `.pdf` và tên
   tệp đúng **cùng khuôn** (`:86`, `:124`) theo đúng 4 điều kiện 7a–7d (đuôi `.pdf`).
   *Chỉ đo tên tệp + có nhận được tệp — nội dung bên trong PDF không thuộc vế đối tác nêu.*
9. **Vai trò đối tác thật sự dùng (Quản trị viên · QTHT)** — vế b. Thao tác [Xuất Excel] phải kết thúc bằng
   **một trong hai**:
   - **(a)** nhận được tệp thoả điều 2–7; **hoặc**
   - **(b)** bị từ chối kèm **thông báo tiếng Việt cho người dùng biết họ không có quyền**, theo `:117`.

### ❌ FAIL nếu — bất kỳ điều nào, ở bất kỳ dạng nào trong M

- Bất kỳ lượt nào trong M dạng sinh thông báo *không tạo được tệp* hoặc *từ chối quyền* ở vai trò
  `cbnv_tw_05` (tức tái hiện vế a).
- Bấm xuất mà **không** có tệp nào đến tay người dùng (không có tệp tải về **và** phản hồi không phải tệp đính kèm).
- Có "tệp" nhưng `openpyxl` **không** mở được (thực chất là JSON/HTML lỗi đổi đuôi).
- Tệp mở được nhưng **thiếu** ≥1 trong 4 thông tin header ở `:1092`.
- Số liệu trong tệp **lệch** số trên màn ở bất kỳ chỉ số nào trong 2 chỉ số tổng bắt buộc, hoặc các dòng chi
  tiết **không cộng khớp** tổng.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc cho số trên màn khác nhau nhưng tệp giống hệt nhau).
- **Tên tệp trượt bất kỳ điều kiện nào trong 7a–7d** — đặc biệt: **thiếu phần giờ-phút**, hoặc ngày ghi dạng
  có dấu gạch nối (`YYYY-MM-DD`), hoặc tên có gạch nối/khoảng trắng, hoặc 2 lần xuất cùng ngày trùng tên,
  **hoặc tên tệp mang tên loại báo cáo khác**.
- Nút [Xuất PDF] không trả tệp, hoặc tên tệp PDF trượt khuôn (điều 8).
- Vai trò **QTHT** bị chặn mà chữ hiện ra là **chuỗi tiếng Anh thô / mã kỹ thuật** (vd `Forbidden`,
  `ERR-PERM-…`), hoặc **bị chặn mà không hiện thông báo nào** (tức tái hiện vế b).
- **Fix một phần**: xuất được ở dạng này nhưng vẫn lỗi ở dạng khác trong M; hoặc Excel đúng khuôn tên nhưng
  PDF sai ⇒ vẫn FAIL (flow §Verdict: *fix một phần → Reopen*).

### KHÔNG được chấm Fail vì (đặc tả im lặng, hoặc ngoài vế đối tác nêu)

- **Khổ giấy A4 / font Times New Roman cỡ 13 bên trong tệp** (`:85`, `:123`) — đối tác không nêu; đo thì ghi
  nhận, không chấm.
- **Nội dung bên trong tệp PDF** (quốc hiệu, tiêu ngữ, khối ký cuối trang theo `:86`) — ngoài vế đối tác nêu.
- **Tên sheet, thứ tự cột, bố cục bảng bên trong tệp** — đặc tả im lặng.
- **Chữ của thông báo thành công** khác *"Xuất thành công"*, hoặc **thiếu** toast *"Đang tạo file…"* — đặc tả
  im lặng ở bảng Error Handling.
- **Kỳ/đơn vị không có dữ liệu** → `INF-RPT-01` (`:113`) là hành vi **hợp lệ**, không phải lỗi xuất tệp.
- **Số liệu trên màn khác số liệu đối tác chụp** (8 khóa học / 15 học viên) — khác env, khác thời điểm,
  dữ liệu QA đã đổi.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).
- **Màn không vẽ đủ 5 thẻ/bảng số liệu** — `:418`–`:422` quy định output báo cáo, không quy định số thẻ trên màn.
- **Câu hỏi "QTHT có được xuất hay không"** — điểm đặc tả tự mâu thuẫn, đã có mục BA sẵn, không kéo verdict.

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — cả 9 điều đều
> đếm được / so được / nhìn thấy được, không có chữ *"hiển thị đúng"* hay *"hợp lý"*.

---

## 5. Dạng dữ liệu phải phủ — **M = 3**

**Nguồn xác định M** (tra theo đúng thứ tự của flow, dừng khi đủ):
① **đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo**: `:410` *"Đếm khóa học đã kết thúc trong kỳ, tổng
hợp số học viên"* + `:82` *"CHỈ bản ghi đã duyệt"* ⇒ chỉ **một** nguồn bản ghi, chưa đủ chia dạng.
② **bộ lọc + giá trị enum ngay trên màn**: `:408` `hinh_thuc` ∈ {`TRUC_TUYEN`, `TRUC_TIEP`} — và `:1070` xác
nhận bộ lọc đặc thù của **UC130 chỉ có Hình thức**. **Dừng ở ②** — đây là chiều duy nhất đổi được nội dung tệp
xuất, và `:1280` buộc *"file xuất theo bộ lọc hiện tại"* nên mỗi giá trị enum là một dạng phải đo.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc đặc thù** (Hình thức để trống) | Đúng điều kiện **vòng 2 của đối tác** (ảnh `LDTBDDDR_06_v2.jpg` để trống bộ lọc Hình thức) — nhánh sinh ra *"Forbidden"* |
| 2 | **Lọc Hình thức = Trực tuyến** (`TRUC_TUYEN`) | Nhánh enum thứ nhất `:408`; cần để chứng minh `:1280` (*file xuất theo bộ lọc hiện tại*) |
| 3 | **Lọc Hình thức = Trực tiếp** (`TRUC_TIEP`) | Nhánh enum còn lại `:408`. Hai nhánh enum cộng lại phải khớp dạng 1 — dùng làm phép cộng-khớp-tổng |

Kỳ báo cáo giữ cố định **Năm 2026** (01/01/2026 → 31/12/2026) và Đơn vị **Toàn quốc** cho cả 3 dạng, để phép
so số liệu giữa các dạng có nghĩa và trùng đúng điều kiện đối tác dùng ở vòng 2.

> ⚠️ **Nếu một nhánh enum không có dữ liệu** (vd 0 khóa trực tiếp): vẫn chạy dạng đó, ghi rõ màn trả
> `INF-RPT-01` và **không** chấm Fail vì thiếu dữ liệu (`:113`); nhưng phải khai trong mục 6 rằng dạng đó
> **không** dùng để chứng minh điều 6, và điều 6 phải được chứng minh bằng dạng còn lại.

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 13:45). 2 cột sau điền sau khi đo xong (14:05).

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Vòng 2:** *Quản trị viên · QTHT*, đơn vị **BTP · TW** (đọc góc phải trên `LDTBDDDR_06_v2.jpg`). **Vòng 1:** KHÔNG BIẾT — ô ảnh trỏ nhầm sang tệp của dòng 200 | Đo **cả 2 vai trò**: ① `cbnv_tw_05` — CB Nghiệp vụ TW, Toàn quốc (**không** dùng fallback Rule 7) cho vế a + c; ② `admin` — `/auth/me` trả `vaiTro ["QTHT"]`, `capDonVi TW`, `donViId 0000…0001` (BTP) cho vế b ⇒ **trùng khít vai trò + đơn vị đối tác dùng ở vòng 2** | **Không** |
| Entity + trạng thái | **Vòng 2:** báo cáo *BC Lớp đào tạo đã diễn ra* đã render có dữ liệu (Tổng khóa học **8** · Tổng học viên **15**), *Thời điểm tạo 31/07/2026 14:56*, nút [Xuất Excel]/[Xuất PDF] bấm được. **Vòng 1:** không biết | Cùng loại BC, cũng đã render **có dữ liệu**, nút xuất **bấm được** ở cả 2 vai trò. CB nghiệp vụ: *Thời điểm tạo 06/08/2026 13:47* · **9 / 17**. QTHT: *13:56* · **9 / 17**. Số khác đối tác (8/15) vì khác env + khác thời điểm — đã khai ở mục 4 là **không** chấm Fail vì điều này | **Không** — cùng trạng thái entity (báo cáo đã chạy, có dữ liệu, nút xuất bấm được) |
| Dữ liệu tiền đề | Có khóa học **đã kết thúc** trong kỳ Năm 2026, phạm vi Toàn quốc (báo cáo ra số > 0) | Có sẵn, **không cần seed**: 9 khóa đã kết thúc / 17 học viên trong kỳ Năm 2026 Toàn quốc, trải **3 đơn vị** (Cục Bổ trợ tư pháp 6, Bộ KH&ĐT 1, Sở TP Hà Nội 2) và **đủ cả 2 nhánh hình thức** (Trực tuyến 8 · Trực tiếp 1). Không kỳ nào rỗng ⇒ không rơi vào nhánh `INF-RPT-01`. Đã kiểm *"Thời điểm tạo"* đổi theo từng lần chạy (13:47/13:49/13:51/13:52/13:56) ⇒ không phải số cache | **Không** |
| Input / filter / giá trị nhập | **Vòng 2:** Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, **Hình thức trống**; URL `…?loai=lop-dao-tao-da-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Thao tác: [Xem báo cáo] → [**Xuất Excel**] | **Trùng khít** ở dạng 1: `…/bao-cao?loai=lop-dao-tao-da-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`, Đơn vị Toàn quốc, Hình thức **trống**, thao tác [Xem báo cáo] → [Xuất Excel] bằng **chuột thật**. Phủ thêm 2 dạng lọc Hình thức + nút [Xuất PDF] (đi qua hộp thoại *Tùy chọn in báo cáo PDF*, đóng hộp thoại trước khi bấm nút khác) | **Không** — bao trùm đúng bộ lọc đối tác dùng, rồi mở rộng |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 lượt xuất ở vòng 2 (vòng 1 không có bằng chứng). M = **1** dạng (không lọc Hình thức). Không thấy đối tác thử lọc Hình thức, cũng không thấy thử [Xuất PDF] | **Phủ đủ M = 3** như mục 5 (không lọc · Trực tuyến · Trực tiếp), mỗi dạng đều ra dữ liệu > 0. **N = 8 lượt xuất**: CB nghiệp vụ 5 lượt (dạng1 13:48 · dạng2 13:50 · dạng3 13:51 · dạng1 lặp lại 13:53 để thử chống đè tệp · PDF 13:54) + QTHT 3 lượt (13:56→13:59). Mỗi kết quả đo lại bằng **đường thứ hai** (gọi thẳng máy chủ) và **khớp** | **Không** — phủ rộng hơn đối tác trên cả 2 chiều (vai trò và dạng lọc) |

**3 dữ kiện neo của đối tác (chỉ có ở vòng 2):**
- **URL/ID bản ghi:** `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-da-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu; *Thời điểm tạo* **31/07/2026 14:56**;
  Tổng khóa học **8** · Tổng học viên **15**.
- **Vai trò + env + bản dựng:** **Quản trị viên QTHT** (BTP · TW) · env `htpldn-uat.ospgroup.vn` · nhãn
  **HTPLDN · V1.0.3** · đồng hồ máy 31/07/2026 14:56.
- **Vòng 1: KHÔNG có 3 dữ kiện neo** — ô `Ảnh/vieo 1` dòng 205 dùng chung tệp Drive của dòng 200 và nội dung
  là màn *đang* diễn ra.

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn (V1.0.3 → bản đang đo).
⇒ Mọi kết luận *hết lỗi* chỉ là **tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

---

## 7. Kết quả chấm

### 7.0. Verdict

# 🔁 REOPEN

**Một câu:** vế a (*không tạo được tệp*) và vế c (*khuôn tên tệp*) đã đạt trên bản dựng V1.0.8, nhưng
**vế b tái hiện nguyên vẹn** — đúng vai trò *Quản trị viên · QTHT* đối tác dùng, bấm [Xuất Excel] vẫn hiện
đúng chữ **"Forbidden"**, không có tệp nào về máy.

> **Cơ sở chọn Reopen chứ không phải verdict khác** (flow §Ca biên — case nhiều vế):
> - **Không chọn *Pass*:** chỉ được Pass khi **mọi** vế sạch. Ở đây còn 1 vế hỏng nguyên vẹn.
> - **Không chọn *không phải lỗi*:** flow cấm verdict này ở nhánh vòng-1-không-có-bằng-chứng (mục 1), và
>   dù không vướng điều cấm đó thì vế b vẫn **tái hiện được** ⇒ không thể nói "không phải lỗi".
> - **Không chọn *cần BA*:** verdict *cần BA* chỉ dùng khi **không còn vế nào hỏng** mà vẫn vướng chỗ đặc tả
>   chưa rõ. Ở đây vế b hỏng theo một dòng đặc tả **đã rõ** (`:117` đòi thông báo tiếng Việt), nên dù BA sau
>   này chốt "QTHT được xuất" hay "QTHT không được xuất" thì hành vi hiện tại **vẫn sai ở cả hai nhánh**:
>   nhánh cho phép → phải ra tệp; nhánh cấm → phải báo bằng câu tiếng Việt của `:117`.
> - **Không chọn *ô trống*:** không có GAP nào chưa đóng (mục 6: 5/5 dòng "Không"), dữ liệu tiền đề có sẵn,
>   không bị chặn kỹ thuật.

### 7.1. Vế a — *"Không thể tạo file xuất. Vui lòng thử lại."* → ✅ **KHÔNG tái hiện**

Vai trò ra verdict: `cbnv_tw_05` (CB Nghiệp vụ TW — đúng tác nhân `:400`). Phủ đủ **M = 3** dạng.

| Dạng | Màn trước khi bấm | Bấm [Xuất Excel] | Chữ trên màn (bắt bằng bộ theo dõi, không lọc trùng) | Máy chủ |
|---|---|---|---|---|
| 1 · không lọc | 13:47 · **9** / **17** | 1 request | *"Đang tạo file..."* → *"Tạo file thành công."* | 200 · đính kèm .xlsx |
| 2 · Trực tuyến | 13:49 · **8** / **15** | 1 request | *"Đang tạo file..."* → *"Tạo file thành công."* | 200 · đính kèm .xlsx |
| 3 · Trực tiếp | 13:51 · **1** / **2** | 1 request | *"Đang tạo file..."* → *"Tạo file thành công."* | 200 · đính kèm .xlsx |
| PDF (điều 8) | 13:53 · 9 / 17 | 1 request (sau hộp thoại) | *"Đang tạo file..."* → *"Tạo file thành công."* | 200 · đính kèm .pdf |

- **Điều 1 ✅** — 4/4 lượt **không** có câu mang nghĩa *không tạo được tệp* (`:116`) và **không** có câu mang
  nghĩa *từ chối quyền* (`:117`). Mỗi lượt đúng **1** khung thông báo (đếm theo mốc giờ), **1** request.
- **Điều 2 ✅** — tệp **rơi thật về `~/Downloads`** ở cả 4 lượt, và phản hồi đúng là tệp đính kèm
  (`content-disposition: attachment`), không phải JSON lỗi.
- **Điều 3 ✅** — `openpyxl.load_workbook()` mở được cả 4 tệp .xlsx, sheet *"Lớp đào tạo đã diễn ra"* có dữ liệu.
- **Điều 4 ✅** — header tệp có **đủ 4** thông tin `:1092` đòi: ① *BC Lớp đào tạo đã diễn ra* ② *Kỳ báo cáo:
  Năm (từ 01/01/2026 đến 31/12/2026)* ③ *Đơn vị: Toàn quốc* ④ *Ngày tạo: 06/08/2026*.
- **Điều 5 ✅** — số trong tệp **khớp từng con số** với màn của chính lượt đó (9/17 · 8/15 · 1/2); các dòng
  phân theo đơn vị **cộng khớp** cả 2 cột: 6+1+2 = 9 khóa học · 11+3+3 = 17 học viên.
- **Điều 6 ✅** — 3 dạng ra **3 md5 khác nhau** (`2569fc2c…` · `15928d7b…` · `2a641099…`), tức tệp **bám bộ
  lọc hiện tại** (`:1280`). Kiểm chéo cộng-khớp giữa 2 nhánh enum: 8 + 1 = 9 khóa · 15 + 2 = 17 học viên.
- **Đường đo thứ hai** (gọi thẳng máy chủ, ngoài trình duyệt): GET báo cáo trả đúng 9/17 · 8/15 · 1/2;
  POST xuất trả 200 kèm tệp 6 822 byte **bằng đúng** tệp lấy từ giao diện ⇒ hai đường **không mâu thuẫn**.

> ⚠️ **Không suy ra "vế a không phải lỗi".** Vòng 1 không có bằng chứng riêng cho case này (mục 1), nên chỉ
> kết luận được **hiện trạng trên bản dựng đang đo**: thao tác này hiện chạy đúng đặc tả. Không kết luận gì
> về việc đối tác đã gặp gì trên V1.0.3.

### 7.2. Vế c — khuôn tên tệp → ✅ **ĐẠT**

Tên lấy từ **2 nguồn người dùng thật thấy** và 2 nguồn **trùng khít**: tệp rơi về `~/Downloads` và
`content-disposition` của chính phản hồi đó.

| Lượt | Tên tệp thật | 7a giờ-phút | 7b ký tự | 7c đúng loại BC | 7d đuôi/độ dài |
|---|---|:-:|:-:|:-:|:-:|
| dạng 1 · 13:48 | `BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx` | ✅ `20260806_1348` khớp giờ xuất | ✅ | ✅ | ✅ |
| dạng 2 · 13:50 | `BaoCaoLopDaoTaoDaDienRa_20260806_1350.xlsx` | ✅ | ✅ | ✅ | ✅ |
| dạng 3 · 13:51 | `BaoCaoLopDaoTaoDaDienRa_20260806_1351.xlsx` | ✅ | ✅ | ✅ | ✅ |
| dạng 1 lặp · 13:53 | `BaoCaoLopDaoTaoDaDienRa_20260806_1353.xlsx` | ✅ | ✅ | ✅ | ✅ |
| PDF · 13:54 | `BaoCaoLopDaoTaoDaDienRa_20260806_1354.pdf` | ✅ | ✅ | ✅ | ✅ đuôi `.pdf` |

- **7a ✅** — đủ 8 chữ số ngày + `_` + **4 chữ số giờ-phút**, và giá trị **khớp thời điểm xuất thật** (13:48,
  13:50, 13:51, 13:53, 13:54), không phải hằng số hay ngày cũ.
- **7b ✅** — `BaoCaoLopDaoTaoDaDienRa` chỉ gồm chữ cái không dấu + chữ số, PascalCase; **không** gạch nối,
  **không** khoảng trắng, **không** dấu tiếng Việt. Gạch dưới chỉ dùng để ngăn đoạn (§H8).
- **7c ✅** — chuỗi `DaDienRa` là tên **chính loại báo cáo này**, **không** phải `DangDienRa` của FR-IX-06.
  *(Chấm theo khuôn `{TenBaoCao}` của `:85`, **không** đòi đúng chuỗi `BaoCaoDaoTao` đối tác viết cứng —
  đòi vậy là prescribe.)*
- **7d ✅** — đuôi đúng theo nút bấm; độ dài 42 ký tự ≪ 255.
- **Phép thử chống đè tệp ✅** — cùng bộ lọc, cùng ngày, xuất lúc **13:48** và **13:53** ra **2 tên khác nhau**.
- **Điều 8 ✅** — nút [Xuất PDF] (qua hộp thoại *Tùy chọn in báo cáo PDF*, giữ mặc định A4 + Dọc) trả tệp
  `.pdf` thật (33 601 byte, `%PDF-1.3`, 1 trang) với **cùng khuôn tên**.

> **So với số đo cũ 03/08 ghi ở `B5-CONTEXT.md` §4** (`bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu giờ-phút, có
> gạch nối): khuôn tên tệp trên bản dựng V1.0.8 **đã đổi và đã đúng §H8**.

### 7.3. Vế b — *"Forbidden"* → ❌ **TÁI HIỆN NGUYÊN VẸN** (đây là lý do Reopen)

Vai trò: `admin` — `/api/v1/auth/me` trả `vaiTro ["QTHT"]`, `capDonVi "TW"`,
`donViId 00000000-0000-4000-8000-000000000001` (BTP) ⇒ **trùng khít** góc phải trên ảnh `LDTBDDDR_06_v2.jpg`.

| Bước | Kết quả đo |
|---|---|
| [Xem báo cáo] | **Chạy được**, ra **đầy đủ** số liệu 9 / 17, *Thời điểm tạo 06/08/2026 13:56* |
| Hai nút xuất | **Bấm được** (`disabled = false`) — đúng `:1052`/`:1053` (điều kiện hiển thị chỉ là *"Sau khi đã Xem báo cáo"*) |
| [Xuất Excel] | **3/3 lượt** → 1 request → HTTP **403** `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}` |
| Chữ người dùng thấy | **"Forbidden"** — nguyên văn, tiếng Anh, khung đỏ ở đỉnh màn, sống **3 201 ms**, hình học `x=0 y=8 w=1431 h=40 opacity=1` ⇒ **nhìn thấy thật** |
| Tệp về máy | **0** — đếm `~/Downloads` trước/sau: không thêm tệp nào |
| Đường đo thứ hai | Gọi thẳng máy chủ cùng phiên QTHT: GET báo cáo **200** (9/17) · POST xuất **403** JSON y hệt ⇒ **hai đường khớp nhau** |

**Trượt điều 9 của mục 4** — thao tác kết thúc **không** theo nhánh (a) *nhận được tệp*, cũng **không** theo
nhánh (b) *thông báo tiếng Việt cho người dùng biết họ không có quyền* (`:117`: *"Bạn không có quyền xem báo
cáo này"*). Chuỗi trả cho người dùng là **từ tiếng Anh thô của tầng kỹ thuật**, đúng gạch đầu dòng FAIL
*"bị chặn mà chữ hiện ra là chuỗi tiếng Anh thô / mã kỹ thuật"*.

Kèm theo, thứ tự kiểm quyền lệch `:79` (*bước 1 của luồng là kiểm quyền + phạm vi*): hệ thống **cho xem trọn
số liệu** rồi mới chặn ở bước xuất — người dùng chỉ biết mình không được phép **sau khi** đã bấm.

> **Cùng gốc với 2 phiếu đã có** — `BUG-SLHDVM-006` (§Phần 3) và `BUG-CLDTBDDDR-006` (§Phần 6) cùng dừng ở
> `POST /api/v1/bao-cao/export` → 403 `ERR-PERM-SYS-00-01` với vai trò QTHT. Case này **viết phiếu riêng, dẫn
> chiếu 2 phiếu đó**, **không** mở dòng bug mới trên bảng của đối tác.

> **Điểm KHÔNG kéo verdict:** câu hỏi *"QTHT rốt cuộc có được xuất báo cáo hay không"* đã có sẵn
> [`cau-hoi-BA.md` §Mục 2](../cau-hoi-BA.md) — **không mở mục trùng**. Verdict Reopen đứng vững ở **cả hai
> nhánh** BA có thể chốt (xem §7.0).

### 7.4. Quan sát NGOÀI vế đối tác nêu — ghi nhận, **không** kéo verdict

Theo flow §Ca biên: phát hiện ngoài vế đối tác nêu **không** đổi verdict của case. Ghi lại để phiên chính quyết.

- **D1 — hai nút xuất có lúc kẹt ở trạng thái không bấm được, và [Xem báo cáo] ngừng phát request.**
  13:52, sau khi **xóa bộ lọc Hình thức bằng biểu tượng ✕ (chuột thật)** rồi bấm [Xem báo cáo]: báo cáo
  **có chạy lại** (URL rụng `fd_hinhThuc`, *Thời điểm tạo* nhảy 13:52, tổng về lại 9) nhưng
  [Xuất Excel]/[Xuất PDF] **vẫn ở trạng thái không bấm được**, và các cú bấm [Xem báo cáo] tiếp theo
  **không sinh request nào**. Tải lại trang là hết. Lệch `:1052`/`:1053` (điều kiện hiển thị **chỉ** là
  *"Sau khi đã Xem báo cáo"*, không kèm điều kiện nào khác).
  - Giả thuyết "do bộ đệm 304" **đã bị bác bỏ**: chạy lại **đúng nguyên tham số** lúc 13:59 thì nút vẫn bấm
    được bình thường. **Chưa chốt được điều kiện kích hoạt tối thiểu** — lần tái hiện thứ hai (14:00) dùng sự
    kiện giả lập nên không dùng làm bằng chứng. Case anh em quy hiện tượng này **hoàn toàn** cho sự kiện giả
    lập; số đo của tôi cho thấy nó **cũng xảy ra sau cú bấm chuột thật**.
  - **Không ảnh hưởng phép đo nào của verdict:** 8/8 lượt xuất đều thực hiện trên báo cáo vừa render xong với
    nút ở trạng thái bấm được.
- **D2 — thiếu khối đầu ra so với `:418`–`:422` (điều kiện *"Luôn"*).** Phản hồi báo cáo có `theoDonVi[]` và
  `trendData[]` nhưng **không có `theoHinhThuc[]` riêng**; tệp .xlsx xuất ra **không có bảng "Theo kỳ"**
  (`theo_ky[]` ở `:422`) — dữ liệu tương ứng chỉ tồn tại trên màn dưới dạng biểu đồ xu hướng theo tháng.
  *(Không chấm Fail cho case: mục 4 đã khai trước rằng bố cục bên trong tệp và số thẻ trên màn không thuộc
  vế đối tác nêu; nhưng `:418`–`:422` ghi rõ điều kiện hiển thị "Luôn" nên đáng để phiên chính xem xét.)*
- **D3 — phép kiểm bộ lọc mà phiên chính đặt hàng: lỗi `linhVuc` vs `linhVucId` của FR-IX-06 KHÔNG lan sang
  màn này.** Màn FR-IX-07 **chỉ có 1 bộ lọc đặc thù = Hình thức** (đúng `:1070`), **không có** bộ lọc Lĩnh
  vực nào để mà sai. Bộ lọc Hình thức **chạy đúng**: giao diện gửi `?hinhThuc=TRUC_TUYEN` khi chạy báo cáo và
  `filterDacThu:{"hinhThuc":"TRUC_TUYEN"}` khi xuất; máy chủ áp đúng (9/17 → 8/15 → 1/2) và tệp xuất đổi theo.

### 7.5. Bằng chứng

| # | Tệp | Chú thích |
|---|---|---|
| 01 | `image/LDTBDDDR_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png` | Dạng 1 (không lọc Hình thức), vai trò CB Nghiệp vụ TW `cbnv_tw_05`, bản dựng V1.0.8 — báo cáo *BC Lớp đào tạo đã diễn ra*, Kỳ Năm 01/01→31/12/2026, Toàn quốc, *Thời điểm tạo 06/08/2026 13:47*, Tổng khóa học **9** · Tổng học viên **17**, hai nút xuất bấm được |
| 02 | `image/LDTBDDDR_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png` | Cùng màn ngay sau cú bấm [Xuất Excel] bằng chuột thật (nút đang được chọn) — khung thông báo **không** kịp vào khung hình; chữ và kết quả lấy từ bộ theo dõi + phản hồi máy chủ + tệp rơi về máy (ảnh 08) |
| 03 | `image/LDTBDDDR_06-03-dang2-loc-hinhthuc-TrucTuyen-man-hinh-truoc-khi-xuat-V108.png` | Dạng 2 — lọc Hình thức = **Trực tuyến**, *Thời điểm tạo 13:49*, Tổng **8** / **15**; ảnh chứng minh máy chủ áp bộ lọc trước khi xuất |
| 04 | `image/LDTBDDDR_06-04-dang3-loc-hinhthuc-TrucTiep-man-hinh-truoc-khi-xuat-V108.png` | Dạng 3 — lọc Hình thức = **Trực tiếp**, *Thời điểm tạo 13:51*, Tổng **1** / **2**; cộng với ảnh 03 ra đúng ảnh 01 (8+1=9 · 15+2=17) |
| 05 | `image/LDTBDDDR_06-05-hop-thoai-tuy-chon-in-PDF-V108.png` | Bẫy thao tác: nút [Xuất PDF] **mở hộp thoại** *"Tùy chọn in báo cáo PDF"* (Khổ giấy · Hướng giấy · [Hủy] [Xuất file]) chứ không tải ngay — hộp thoại còn mở sẽ nuốt cú bấm kế tiếp |
| 06 | `image/LDTBDDDR_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png` | Vai trò **Quản trị viên · QTHT** (BTP · TW) — **xem được** trọn số liệu 9 / 17, *Thời điểm tạo 13:56*, hai nút [Xuất Excel]/[Xuất PDF] **bấm được** |
| 07 | `image/LDTBDDDR_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png` | **Bằng chứng chính của Reopen** — cũng màn đó, sau khi bấm [Xuất Excel]: khung đỏ **"Forbidden"** (tiếng Anh) ở đỉnh màn, không tệp nào về máy |
| 08 | `image/LDTBDDDR_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt` | Nguyên văn chữ trên màn từng lượt + phản hồi máy chủ (mã, `content-disposition`, thân JSON 403), nội dung đọc từ tệp .xlsx, md5 3 dạng, phép thử chống đè tệp, và kết quả đo bằng đường thứ hai |

Tệp thật hệ thống giao ra, giữ lại tại `testfiles/` (tên gốc hệ thống đặt nằm **sau** tiền tố mã case):
`LDTBDDDR_06-dang1-khong-loc-BaoCaoLopDaoTaoDaDienRa_20260806_1348.xlsx` ·
`LDTBDDDR_06-dang2-loc-TrucTuyen-…_1350.xlsx` · `LDTBDDDR_06-dang3-loc-TrucTiep-…_1351.xlsx` ·
`LDTBDDDR_06-dang1-lap-lai-…_1353.xlsx` (phép thử chống đè tệp) · `LDTBDDDR_06-pdf-…_1354.pdf`.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 13:45** — viết mục 1–6 **TRƯỚC khi mở màn tranh chấp**. Đã đọc: bằng chứng đối tác (2 tệp),
  đặc tả (`srs-fr-11-bao-cao.md`, `srs-v3.5.md` §H8), dòng 205 tab `bug`, và hồ sơ QA nội bộ đã khai ở đầu file.
- **2026-08-06 14:05** — đo xong, điền mục 6 (2 cột) + mục 7. **Mục 4 và mục 5 KHÔNG sửa một chữ nào** sau khi
  mở màn: M vẫn = 3 (đúng 2 nhánh enum `hinh_thuc` + dạng không lọc), 9 điều PASS vẫn nguyên. Không có điều
  kiện nào phải nới hay siết sau khi thấy kết quả.
- **Ghi chú phương pháp (để phiên sau lặp lại được):**
  - Chữ **"Forbidden"** bắt được **ngay lượt đầu** nhờ **hẹn giờ bấm sau 2 500 ms rồi mới gọi chụp** (khung chỉ
    sống 3 201 ms, ngắn hơn độ trễ công cụ chụp). Bộ bắt kiểu *"nghe node mới"* chỉ trả về *"Đang tạo file..."*
    — đúng như bài học đã ghi ở `SLHDVM_06` §8 và `CLDTBDDDR_06` §8; phải **lấy mẫu nội dung mỗi 100 ms** mới
    thấy chữ thứ hai.
  - `window.__qa.net` rỗng sau [Xem báo cáo] **không phải lỗi ứng dụng**: bộ bắt cố ý bỏ qua request kiểu GET,
    mà chạy báo cáo là GET. Đã kiểm lại bằng danh sách request của trình duyệt.
  - Hiện tượng D1 phát hiện tình cờ khi chuyển giữa các dạng; đã **thử bác bỏ giả thuyết bộ đệm 304** bằng cách
    chạy lại đúng nguyên tham số (13:59, nút vẫn bấm được) ⇒ ghi lại đúng mức "chưa chốt được điều kiện kích
    hoạt", không phỏng đoán thêm.
