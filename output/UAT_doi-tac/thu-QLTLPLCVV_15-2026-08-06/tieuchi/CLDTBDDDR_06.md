# Tiêu chí verify — CLDTBDDDR_06

```
Mã case: CLDTBDDDR_06 (tab `bug` dòng 200)      Thời điểm viết: 2026-08-06 13:02
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 13:07 → 13:24
Bản dựng (TỰ ĐO 2026-08-06 13:05 bằng curl, KHÔNG chép từ B5-CONTEXT):
  · nhãn hiển thị trong app: HTPLDN · V1.0.8 (đọc ở chân sidebar, cả 2 phiên vai trò)
  · bó mã: assets/index-CNwX9JjX.js · etag W/"6a73f6a4-1124fd" · 1 123 581 byte
  · index.html etag W/"6a73f6a4-428" · last-modified: Thu, 06 Aug 2026 02:51:16 GMT
  · DẤU VÂN TAY: md5 bó mã = e0e4f737b1fb7ab9409f459a4d0fa051
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `tieuchi/SLHDVM_06.md` — file tiêu chí của case đã chạy xong cùng lô (tham khảo **cách trình bày**).
> - `bug-report.md` §Phần 2 (`BUG-SLCTHT-006`) và §Phần 3 (`BUG-SLHDVM-006`) — hai phiếu cùng gốc 403.
> - `cau-hoi-BA.md` §Mục 2 — câu hỏi *"QTHT có được XUẤT báo cáo thống kê không"* đã mở sẵn.
> - `B5-CONTEXT.md` §4 có nhắc **số đo cũ 03/08/2026** (bản dựng V1.0.4, env đối tác): tệp xuất khi đó tên
>   `bao-cao-lop-dao-tao-dang-dien-ra-2026-08-03.xlsx`.
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ, KHÔNG lấy số đo cũ làm ngưỡng.** Cụ thể: số đo cũ và kết quả của
> `SLHDVM_06` chỉ chứng minh *"trên màn khác, endpoint từng chạy"* — chúng **không** được dùng làm tiêu chí
> Pass cho màn này. Bar Pass của case này đòi **mở tệp ra đọc nội dung** + **đo tên tệp theo khuôn đặc tả**.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** — 2 vế triệu chứng (2 vòng nghiệm thu, cùng thao tác bấm **[Xuất Excel]** trên màn
*Báo cáo thống kê → BC Lớp đào tạo đang diễn ra*) + 1 vế kỳ vọng về tên tệp:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo lỗi
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo
  **"Forbidden"** ⇒ vẫn không có tệp; triệu chứng đổi từ *"lỗi tạo tệp"* sang *"bị chặn quyền"*.
- **Vế c (ô `Kết quả mong đợi`)** — *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.
  **Tên tệp xuất: `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx` hoặc `BaoCaoDaoTao_{YYYYMMDD_HHmm}.pdf`**"*
  ⇒ case này **CÓ** vế tên tệp (khác `SLHDVM_06` cùng lô).

🔴 **Vế c đo được, KHÔNG đẩy sang BA.** BA đã chốt **2026-08-04** khuôn tên tệp cho nhóm IX và đặc tả đã sửa
theo (dấu `[BA chốt 2026-08-04]` nằm ngay trong `:85`, `:86`, `:1092`); ngày **2026-08-06** khuôn này còn được
nâng thành quy ước chung ở **Phụ lục E §H8** (`srs-v3.5.md:6716`). Đây là **áp quyết định có sẵn**, QA chấm được.

⚠️ **Đo theo KHUÔN, không đo theo chuỗi đối tác viết.** Đối tác viết cứng `BaoCaoDaoTao` — nhưng đặc tả chỉ
đòi `{TenBaoCao}` = *tên loại báo cáo* viết liền PascalCase, bỏ dấu, bỏ ký tự không phải chữ/số. Cấm chấm Fail
chỉ vì tên tệp không đúng y hệt chữ `BaoCaoDaoTao` (đó là **prescribe**, không phải yêu cầu nghiệp vụ).

### Bằng chứng — đã MỞ XEM full-res (2026-08-06 13:00)

| Vòng | Tệp | Thấy gì |
|---|---|---|
| 1 | `partner-evidence/CLDTBDDDR_06.jpg` | Màn *Báo cáo thống kê*, URL `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Loại BC = **BC Lớp đào tạo đang diễn ra**, Kỳ **Năm** 01/01/2026→31/12/2026, Đơn vị **Toàn quốc**, **Hình thức trống**, **Lĩnh vực trống**. Báo cáo đã render: *Kỳ: Năm • Khoảng thời gian: 01/01/2026 → 31/12/2026 • Đơn vị: Toàn quốc • Thời điểm tạo: **15/07/2026 17:32*** · **Tổng số = 3**. Khung thông báo đỏ **"Không thể tạo file xuất. Vui lòng thử lại."**. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0**. Đồng hồ máy: 05:32 PM 2026-07-15 |
| 2 | `partner-evidence/CLDTBDDDR_06_v2.jpg` | **Cùng URL, cùng bộ lọc** (Hình thức + Lĩnh vực vẫn trống). Báo cáo: *Thời điểm tạo **31/07/2026 14:52*** · **Tổng số = 6 · Số trực tuyến = 6 · Số trực tiếp = 0**. Khung thông báo đỏ **"Forbidden"**. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0.3**. Đồng hồ máy: 02:53 PM 2026-07-31 |

✅ **Kiểm bằng chứng có đúng case này không:** cả 2 ảnh đều là màn *BC Lớp đào tạo đang diễn ra*
(`loai=lop-dao-tao-dang-dien-ra`, FR-IX-06/UC129) — **đúng case**, không lệch mã, không nhầm sang FR-IX-07.

⚠️ **Hai vòng KHÔNG cùng bản dựng, KHÔNG cùng dữ liệu** (bắt buộc ghi theo flow §Cổng bằng chứng):
- Bản dựng: vòng 1 **V1.0**, vòng 2 **V1.0.3**.
- Dữ liệu: vòng 1 Tổng 3 (chưa có ô trực tuyến/trực tiếp trên màn), vòng 2 Tổng 6 / TT 6 / TTiếp 0.
- **Giống nhau:** cùng env `htpldn-uat.ospgroup.vn`, cùng vai trò **Quản trị viên · QTHT** (BTP · TW),
  cùng bộ lọc (Hình thức trống + Lĩnh vực trống), cùng kỳ Năm 2026, cùng đơn vị Toàn quốc.

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (+ Phụ lục E ở
`srs-v3.5.md`) — **đã mở file đọc đúng dòng 2026-08-06 13:00**, không lấy số dòng từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-11-bao-cao.md:62` | Preconditions chung — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"* |
| `:82` | Processing chung bước 4 — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* |
| `:85` | Bước 7 — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). **Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo"* `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` |
| `:86` | Bước 8 — PDF theo TT17/2025; *"Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo Phụ lục E §H8"* `[BA chốt 2026-08-04]` — *"`{TenBaoCao}` là tên loại báo cáo **viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số** (dấu `/`, khoảng trắng, dấu câu)"* |
| `:113` | E3 · Không có dữ liệu · **INF-RPT-01** · *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* · INFO |
| `:116` | E6 · Lỗi xuất file · **ERR-RPT-04** · *"Không thể tạo file xuất. Vui lòng thử lại"* · ERROR ⇒ đúng câu **vế a** |
| `:117` | E7 · Không có quyền · **ERR-RPT-05** · *"Bạn không có quyền xem báo cáo này"* · ERROR ⇒ nhánh quyền của **vế b** |
| `:123` | AC chung — *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (Phụ lục E §H8)"* |
| `:124` | AC chung — *"**Given** CB nhấn 'Xuất PDF' … **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`** (Phụ lục E §H8)"* |
| `:346` | **FR-IX-06: BC Lớp đào tạo đang diễn ra (UC129)** — màn hình SCR-IX-01 |
| `:355` | Mô tả — *"Báo cáo **snapshot** khóa học **đang diễn ra**, phân theo hình thức (trực tuyến/trực tiếp), lĩnh vực, đơn vị"* |
| `:357` | **Tác nhân:** *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:365`–`:366` | Input đặc thù — `hinh_thuc` ∈ {`TRUC_TUYEN`, `TRUC_TIEP`} (không bắt buộc) · `linh_vuc_id` FK → DANH_MUC (không bắt buộc) |
| `:368` | Công thức — *"Đếm khóa học đang diễn ra (snapshot), theo phạm vi đơn vị"* |
| `:376`–`:381` | Output đặc thù, **điều kiện hiển thị "Luôn"**: `tong_dang_dien_ra` · `truc_tuyen` · `truc_tiep` · `theo_don_vi[]` · `theo_linh_vuc[]` · `ds_khoa_hoc[]` |
| `:385` | AC bổ sung — *"**Given** CB lọc 'Trực tuyến' **When** filter **Then** chỉ hiển thị KH trực tuyến"* |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: **Sau khi đã 'Xem báo cáo'**"* (không kèm điều kiện vai trò) |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1071` | Mapping dropdown — UC129 *BC Lớp đào tạo đang diễn ra*, **bộ lọc đặc thù = Hình thức, Lĩnh vực**, biểu đồ Bar (snapshot) |
| `:1092` | Quy tắc tương tác — *"Export XLSX/PDF **chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file**… Tên tệp cả hai định dạng theo Phụ lục E §H8 — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`"* `[BA chốt 2026-08-04]` |
| `:1268` | BR-AUTH-08 — cột *Ngoại lệ* ghi **"QTHT bypass"**, cột *Áp dụng* ghi **"Toàn bộ FR-IX"** |
| `:1280` | BR-DATA-06 — *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |
| `srs-v3.5.md:6716` | **Phụ lục E §H8 — Tên tệp xuất thống nhất** (BẮT BUỘC): *"Khuôn: `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (**kể cả dấu gạch nối**, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn… **Phần giờ-phút bắt buộc** để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa 255 ký tự"* `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]` |

**Rẽ nhánh — quyết TRƯỚC khi viết mục 4 (rẽ theo TỪNG VẾ):**

| Vế | Đặc tả | Verdict nhánh |
|---|---|---|
| **a** — *"Không thể tạo file xuất"* | **Nói rõ** và **khớp** kỳ vọng: `:1052` ghi thẳng *click → auto-download*, `:123` ghi *tải file .xlsx*; `:116` cho biết ERR-RPT-04 chỉ dành cho tình huống lỗi tạo tệp thật | Chấm được → viết mục 4 |
| **b** — *"Forbidden"* | **Nói rõ** về **câu chữ** khi từ chối vì quyền: `:117` đòi thông báo tiếng Việt *"Bạn không có quyền xem báo cáo này"*. Dù nghiệp vụ chốt hướng nào thì chuỗi tiếng Anh thô cũng lệch dòng này | Chấm được → viết mục 4 |
| **c** — khuôn tên tệp | **Nói rõ** và **khớp** kỳ vọng, **BA đã chốt 2026-08-04** (+ §H8 2026-08-06). Áp quyết định có sẵn | Chấm được → viết mục 4 |

⚠️ **Một điểm KHÔNG chấm, đã có mục BA sẵn:** câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo
thống kê"* là chỗ đặc tả **tự mâu thuẫn** (`:62`/`:357` liệt kê tác nhân CB Nghiệp vụ / CB Phê duyệt ↔ `:1268`
ghi ngoại lệ *"QTHT bypass"* áp *"Toàn bộ FR-IX"*). Mục này **đã có** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§ *Mục 2* (mở lúc 12:40 khi verify `SLCTHT_06`, cùng nguyên nhân gốc) ⇒ **không mở mục trùng**. Mục đó
**không kéo verdict** của case: dù BA chốt hướng nào, hành vi hiện tại vẫn phải thoả `:117`.

**IM LẶNG về:**
- **Chữ chính xác của thông báo thành công** khi xuất được — `:1058` mô tả *"Xuất thành công"* ở bảng thành
  phần màn hình, nhưng bảng Error Handling **không** có mã INF/WRN tương ứng ⇒ không chấm Fail vì chữ khác.
- **Có bắt buộc hiện toast *"Đang tạo file…"* hay không** — cùng lý do trên.
- **Bố cục bên trong tệp**: tên sheet, thứ tự cột, cách trình bày bảng. Đặc tả chỉ quy định **header file**
  phải có tiêu đề BC + kỳ + đơn vị + ngày tạo (`:1092`).
- **Có bao nhiêu ô số liệu phải hiện trên màn** — `:376`–`:378` khai 3 chỉ số điều kiện *"Luôn"*, nhưng
  không quy định màn hình phải vẽ đủ 3 thẻ.

---

## 3. Precondition

- **Tài khoản ra verdict cho vế a + vế c:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương**
  (`CB_NV_TW`), cấp **TW**, phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-06 (`:357`).
  Fallback (Rule 7, **cùng vai trò + cùng cấp**): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Tài khoản bắt buộc dùng cho vế b:** vai trò **Quản trị viên · QTHT** — **chính vai trò đối tác dùng** ở cả
  2 vòng (đọc từ góc phải trên của cả 2 ảnh). Vế b là *"Forbidden"*, tức là **triệu chứng phân quyền**; đo bằng
  vai trò khác thì không tái hiện được điều đối tác nêu.
  > **Vì sao không vướng quy tắc "tài khoản quản trị không ra verdict":** quy tắc đó chặn việc **quyền rộng che
  > lỗi phân quyền**. Ở đây chiều ngược lại — QTHT là vai trò **bị chặn**, dùng nó để **phơi** lỗi chứ không che.
  > Vế a và vế c vẫn ra verdict bằng `cbnv_tw_05`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**, Loại BC = *BC Lớp đào tạo đang diễn ra*.
- **Dữ liệu tiền đề:** ≥1 **khóa học đang diễn ra** (snapshot, `:368`) thuộc bản ghi đã duyệt (`:82`), nằm trong
  kỳ đo và trong phạm vi đơn vị. Kỳ rỗng → đó là `INF-RPT-01` hợp lệ (`:113`), **phải đổi kỳ/đơn vị** để có dữ
  liệu rồi mới đo nút xuất. **Mọi kỳ đều rỗng ⇒ GAP chưa đóng ⇒ verdict ô trống**, nêu rõ cần seed gì.
- **Bộ lọc neo theo đối tác:** Kỳ = **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị = **Toàn quốc** ·
  Hình thức **trống** · Lĩnh vực **trống**. Thao tác: [Xem báo cáo] → [Xuất Excel].
- **Cache máy chủ:** trước khi kết luận *"không có dữ liệu"*, kiểm trường **"Thời điểm tạo"** trên màn; nghi
  cache thì đổi `denNgay` 1 ngày để lấy khoá cache mới.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi `soObserverDangSong = 1`; **đếm thông báo theo mốc giờ khác nhau**, không theo số phần tử.
  > ⚠️ Bài học đã ghi ở `tieuchi/SLHDVM_06.md` §8: bộ bắt kiểu *"nghe node mới được thêm"* **bỏ sót** chữ
  > *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**. Phải đo bù bằng cách theo dõi **nội dung**
  > vùng thông báo theo thời gian (`innerText`) + ghi hình học để chứng minh người dùng nhìn thấy thật.

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
5. **Số liệu trong tệp khớp số liệu đang hiện trên màn.** So từng cặp, tối thiểu **3 chỉ số điều kiện "Luôn"**
   của FR-IX-06 (`:376`–`:378`): **Tổng số KH đang diễn ra · Số trực tuyến · Số trực tiếp**. Chỉ số nào màn
   không vẽ thẻ riêng thì lấy từ phản hồi của chính lần chạy báo cáo đó. Có bảng phân theo đơn vị / lĩnh vực
   trong tệp (`:379`, `:380`) thì **tổng các dòng phải cộng khớp** tổng số.
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280` + `:385`): với 3 dạng lọc ở mục 5, số liệu trong tệp **đổi
   theo** và mỗi lần đều khớp số trên màn của **chính lần đó** — không phải luôn trả bản không lọc.
   Kiểm chéo bằng md5 các tệp: 2 dạng cho số trên màn khác nhau mà tệp giống hệt ⇒ vi phạm.
7. **Tên tệp .xlsx đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (`:85`, `:123`, `:1092`, §H8
   `srs-v3.5.md:6716`) — lấy tên từ **nguồn người dùng thật thấy** (tệp rơi về máy, hoặc `content-disposition`
   của phản hồi). Đo đủ **4 điều kiện của khuôn**:
   - **7a.** Có đoạn thời gian `_YYYYMMDD_HHmm` ngay trước đuôi tệp: **8 chữ số ngày + `_` + 4 chữ số giờ-phút**,
     và **giá trị khớp thời điểm xuất** (không phải hằng số/ngày cũ). *Phần giờ-phút là bắt buộc.*
   - **7b.** Phần `{TenBaoCao}` chỉ gồm **chữ cái không dấu và chữ số**; **không** dấu gạch nối, **không**
     khoảng trắng, **không** dấu tiếng Việt, **không** dấu câu. Gạch dưới chỉ dùng để ngăn đoạn.
   - **7c.** Phần `{TenBaoCao}` **nhận ra được là tên của chính loại báo cáo này** (đào tạo / lớp đào tạo đang
     diễn ra) — không phải tên loại báo cáo khác, không phải chuỗi vô nghĩa.
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
- Số liệu trong tệp **lệch** số trên màn ở bất kỳ chỉ số nào trong 3 chỉ số bắt buộc.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc cho số trên màn khác nhau nhưng tệp giống hệt nhau).
- **Tên tệp trượt bất kỳ điều kiện nào trong 7a–7d** — đặc biệt: **thiếu phần giờ-phút**, hoặc ngày ghi dạng
  có dấu gạch nối (`YYYY-MM-DD`), hoặc tên có gạch nối/khoảng trắng, hoặc 2 lần xuất cùng ngày trùng tên.
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
- **Số liệu trên màn khác số liệu đối tác chụp** (3 / 6 khóa học) — khác env, khác thời điểm, dữ liệu QA đã đổi.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).
- **Màn không vẽ đủ 3 thẻ số liệu** — `:376`–`:378` quy định output, không quy định số thẻ trên màn.
- **Câu hỏi "QTHT có được xuất hay không"** — điểm đặc tả tự mâu thuẫn, đã có mục BA sẵn, không kéo verdict.

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — cả 9 điều đều
> đếm được / so được / nhìn thấy được, không có chữ *"hiển thị đúng"* hay *"hợp lý"*.

---

## 5. Dạng dữ liệu phải phủ — **M = 3**

**Nguồn xác định M** (tra theo đúng thứ tự của flow, dừng khi đủ):
① **đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo**: `:368` *"Đếm khóa học đang diễn ra (snapshot), theo
phạm vi đơn vị"* + `:82` *"CHỈ bản ghi đã duyệt"* ⇒ chỉ **một** nguồn bản ghi, chưa đủ chia dạng.
② **bộ lọc + giá trị enum ngay trên màn**: `:365` `hinh_thuc` ∈ {`TRUC_TUYEN`, `TRUC_TIEP`} · `:366`
`linh_vuc_id` (FK DANH_MUC) · `:1071` xác nhận bộ lọc đặc thù của UC129 = **Hình thức, Lĩnh vực**.
**Dừng ở ②** — bộ lọc là chiều duy nhất đổi được nội dung tệp xuất, và `:1280` buộc *"file xuất theo bộ lọc
hiện tại"* nên mỗi nhánh lọc là một dạng phải đo. `:385` còn có AC riêng cho nhánh *"Trực tuyến"*.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc đặc thù** (Hình thức trống + Lĩnh vực trống) | Đúng điều kiện **của cả 2 vòng** đối tác (cả 2 ảnh đều để trống 2 bộ lọc) — nhánh sinh ra *"Không thể tạo file xuất"* rồi *"Forbidden"* |
| 2 | **Lọc Hình thức** (`TRUC_TUYEN`, hoặc `TRUC_TIEP` nếu trực tuyến rỗng — khai rõ) | Nhánh enum `:365`, có AC riêng ở `:385`; cần để chứng minh `:1280` (*file xuất theo bộ lọc hiện tại*) |
| 3 | **Lọc Lĩnh vực** (một lĩnh vực có dữ liệu — khai rõ chọn lĩnh vực nào và vì sao) | Nhánh bộ lọc còn lại `:366`/`:1071`; kiểm chiều `theo_linh_vuc[]` (`:380`) có bám lọc không |

Kỳ báo cáo giữ cố định **Năm 2026** (01/01/2026 → 31/12/2026) và Đơn vị **Toàn quốc** cho cả 3 dạng, để phép so
số liệu giữa các dạng có nghĩa và trùng đúng điều kiện đối tác dùng.

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 13:02). 2 cột sau điền ở **giai đoạn B**.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên · QTHT**, đơn vị **BTP · TW** (đọc từ góc phải trên ở **cả 2 ảnh**) | **Đo cả 2 nhánh vai trò.** ① **Ra verdict vế a + vế c:** `cbnv_tw_05` — *CB Nghiệp vụ - Trung ương #05*, `CB_NV_TW`, cấp TW, `donViId 00000000-0000-4000-8000-000000000001`, phạm vi **Toàn quốc**, có quyền `export_bao_cao` = đúng **tác nhân đặc tả** `:357`; **không** dùng fallback. ② **Ra verdict vế b:** `admin` — *Quản trị hệ thống*, `vaiTro ["QTHT"]`, cấp TW, cùng `donViId` = **trùng khít vai trò + đơn vị đối tác dùng** (BTP · TW) | **Không** |
| Entity + trạng thái | Báo cáo *BC Lớp đào tạo đang diễn ra* đã **render có dữ liệu** (nút Xuất Excel bấm được). Vòng 1: Tổng số **3**, *Thời điểm tạo 15/07/2026 17:32*. Vòng 2: Tổng **6** · Trực tuyến **6** · Trực tiếp **0**, *Thời điểm tạo 31/07/2026 14:52* | Cùng trạng thái: báo cáo **đã render có dữ liệu**, nút [Xuất Excel] + [Xuất PDF] **bật** ở **cả 2 vai trò**. Dạng 1: Tổng 2 / TT 1 / TTiếp 1 (*tạo 13:07*) · dạng 2: 1 / 1 / 0 (*13:11*) · dạng 3: 2 / 1 / 1 (*13:13*) · nhánh QTHT: 2 / 1 / 1 (*13:20* và *13:23*). Mọi lượt đều đọc trường *Thời điểm tạo* để loại trừ cache máy chủ — luôn là mốc giờ của chính lượt đo | **Không** |
| Dữ liệu tiền đề | Có khóa học **đang diễn ra** trong kỳ Năm 2026, phạm vi Toàn quốc (đủ để báo cáo ra số > 0) | Có sẵn, **KHÔNG cần seed**: 2 lớp đang diễn ra trong kỳ Năm 2026 phạm vi Toàn quốc, trải **2 hình thức** (1 trực tuyến + 1 trực tiếp) và **2 đơn vị** (Cục Bổ trợ tư pháp - Bộ Tư pháp · Bộ Kế hoạch và Đầu tư), thuộc **2 lĩnh vực** (Dân sự 1 · Thương mại 1) ⇒ đủ dựng cả 3 dạng mục 5 | **Không** |
| Input / filter / giá trị nhập | Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, **Hình thức trống**, **Lĩnh vực trống** (cả 2 vòng giống nhau). Thao tác: [Xem báo cáo] → [**Xuất Excel**] | Trùng khít: Loại BC *BC Lớp đào tạo đang diễn ra*, kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, thao tác [Xem báo cáo] → [Xuất Excel] bằng **chuột thật** trên giao diện. Dạng 1 sinh URL `…?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` — **trùng đúng URL của cả 2 vòng** đối tác. Phủ thêm dạng 2 (Hình thức *Trực tuyến*) · dạng 3 (Lĩnh vực *Dân sự*) · và **[Xuất PDF]** (vế `.pdf` trong câu kỳ vọng) | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 lượt xuất mỗi vòng (2 lượt tổng). M = **1** dạng lọc duy nhất (không lọc đặc thù). Không thấy đối tác thử lọc Hình thức hay Lĩnh vực, cũng không thấy thử [Xuất PDF] | **N = 9 lượt xuất**: vai trò CB Nghiệp vụ 5 lượt (dạng 1 ×2 để thử chống đè tệp, dạng 2, dạng 3, PDF) + vai trò QTHT 4 lượt (tái hiện 4/4). Phủ đủ **M = 3 dạng** mục 5. **4 tệp .xlsx + 1 tệp .pdf đều mở ra đọc nội dung** (`openpyxl` / PyMuPDF); md5 3 tệp dạng khác nhau đều khác nhau; tệp dạng 2 khác hẳn dạng 1 ⇒ chứng minh tệp bám bộ lọc | **Không** |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** `htpldn-uat.ospgroup.vn/bao-cao?loai=lop-dao-tao-dang-dien-ra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  — **giống hệt nhau ở cả 2 vòng**, không có tham số bộ lọc đặc thù.
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu; *Thời điểm tạo* **15/07/2026 17:32** (vòng 1, Tổng 3)
  · **31/07/2026 14:52** (vòng 2, Tổng 6 / TT 6 / TTiếp 0).
- **Vai trò + env + bản dựng:** **Quản trị viên QTHT** (BTP · TW) · env `htpldn-uat.ospgroup.vn` · nhãn
  **HTPLDN · V1.0** (vòng 1, 15/07/2026 17:32) và **HTPLDN · V1.0.3** (vòng 2, 31/07/2026 14:53).

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn (V1.0 / V1.0.3 → V1.0.8).
⇒ Mọi kết luận *hết lỗi* chỉ là **tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

**Kết luận mục 6: 5/5 dòng đã điền, 0 GAP.**

---

## 7. Kết quả chấm (điền 2026-08-06 13:26)

| Vế đối tác nêu | Kết quả đo | Kết luận |
|---|---|---|
| **a** — *"Không thể tạo file xuất. Vui lòng thử lại."* (ERR-RPT-04, `:116`) | Vai trò CB Nghiệp vụ TW: **3/3 dạng xuất được** + PDF. Mỗi lượt 1 request ↔ chữ *"Đang tạo file..."* → *"Tạo file thành công."*, HTTP 200, tệp .xlsx thật, mở bằng `openpyxl` đủ 4 mục header (`:1092`), số liệu khớp màn **từng con số**, các chiều cộng khớp tổng. **Không** lượt nào ra câu ERR-RPT-04 | **HẾT LỖI** |
| **b** — *"Forbidden"* | Vai trò **QTHT — đúng vai trò + đơn vị đối tác dùng**: [Xem báo cáo] **200** (hiện đủ 2/1/1, nút xuất **bật**), nhưng [Xuất Excel] → `POST /api/v1/bao-cao/export` trả **HTTP 403** `ERR-PERM-SYS-00-01`, chữ trên màn đúng một chữ **"Forbidden"** (hiện +102 ms sau khi bấm, sống ~3,2 giây, x=0 y=8 w=1432 h=40, opacity 1). Tái hiện **4/4 lượt**, đã chụp được ảnh | **CÒN LỖI — TÁI HIỆN** |
| **c** — tên tệp đúng khuôn | Tên tệp app giao cho trình duyệt **trùng khít** `content-disposition`: `BaoCaoLopDaoTaoDangDienRa_20260806_1308.xlsx` (và `_1310`, `_1311`, `_1314`), PDF `…_1317.pdf`. Thoả **7a** (có `_YYYYMMDD_HHmm`, khớp giờ xuất thật) · **7b** (chỉ chữ cái + số, PascalCase, không dấu, không gạch nối) · **7c** (nhận ra đúng loại BC này) · **7d** (đuôi đúng, độ dài ngắn). **Phép thử chống đè tệp:** xuất 2 lần cùng ngày lúc 13:08 và 13:10 → **2 tên khác nhau** | **ĐẠT** |

**Verdict: REOPEN.** Theo flow §Ca biên — *case gộp nhiều vế: mọi vế hết lỗi mới Pass · còn ≥1 vế lỗi → Reopen*.
Vế a và vế c đã đạt, **vế b tái hiện nguyên vẹn** ⇒ Reopen.

**Vì sao KHÔNG chấm *"không phải lỗi"* dù `:62`/`:357` chỉ liệt kê tác nhân là CB Nghiệp vụ / CB Phê duyệt:**
verdict đó đòi chứng minh **đối tác thao tác sai**, mà ở đây chính phần mềm đã (1) cho vai trò QTHT vào màn
báo cáo, (2) cho chạy báo cáo ra dữ liệu (HTTP 200), (3) **hiện nút [Xuất Excel] ở trạng thái bấm được** —
`:1052` ghi điều kiện hiển thị của nút chỉ là *"Sau khi đã 'Xem báo cáo'"*, **không kèm điều kiện vai trò**.
Người dùng bấm một nút mà phần mềm đang mời bấm thì không thể gọi là thao tác sai. Thêm nữa, dù sau này BA
chốt QTHT **không** được xuất, hành vi hiện tại vẫn lệch `:117` (từ chối vì thiếu quyền phải báo bằng câu
tiếng Việt đã định, không phải chuỗi tiếng Anh thô *"Forbidden"*).

**Vì sao KHÔNG chấm *"cần BA"*:** vế b có căn cứ đặc tả rõ ở `:117` (+ `:1052`) nên chấm được ngay. Riêng câu
hỏi *"QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo"* là điểm đặc tả tự mâu thuẫn (`:62`/`:357` vs `:1268`) —
**đã có sẵn** mục ở [`cau-hoi-BA.md`](../cau-hoi-BA.md) § *Mục 2* (mở lúc 12:40 khi verify `SLCTHT_06`, cùng
nguyên nhân gốc) ⇒ **không mở mục trùng**, chỉ trỏ tới. Mục đó **không kéo verdict** của case.

**Vế c KHÔNG đẩy sang BA** — BA đã chốt 2026-08-04 (+ §H8 2026-08-06), đây là áp quyết định có sẵn.

**Giới hạn hiệu lực:** đo trên env kiểm thử nội bộ `18.143.165.120.nip.io`, bản dựng V1.0.8
(md5 bó mã `e0e4f737b1fb7ab9409f459a4d0fa051`) — khác env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác.

**Ghi nhận ngoài vế đối tác nêu (KHÔNG kéo verdict, đã báo phiên chính, chưa mở dòng bảng):**
- **D1 — bộ lọc *Lĩnh vực* không có tác dụng:** giao diện gửi `?linhVuc=<id>` trong khi máy chủ nhận
  `?linhVucId=<id>`; gọi đúng tên trả Tổng 1, giao diện trả Tổng 2. Lệnh xuất cũng mang sai khoá
  (`filterDacThu:{linhVuc:…}`). Bộ lọc *Hình thức* thì chạy đúng. Đặc tả: `:366` · `:370` · `:1071` · `:1280`.
- **D2 — thiếu 2 chiều dữ liệu điều kiện "Luôn":** `:380` `theo_linh_vuc[]` và `:381` `ds_khoa_hoc[]` không có
  trong phản hồi máy chủ, không có trên màn, không có trong tệp xuất.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 13:26** — **Không sửa mục 4 và mục 5**; hai mục này giữ **nguyên văn như lúc viết trước khi mở
  màn tranh chấp**. Chỉ điền **Bản dựng** ở đầu file, 2 cột sau của mục 6, và thêm mục 7 + mục 8.
- **2026-08-06 13:14 — ghi nhận giới hạn của phép đo, KHÔNG hạ tiêu chí:** dạng 3 (lọc *Lĩnh vực*) **không dùng
  được** để chứng minh điểm 6 (*tệp bám bộ lọc hiện tại*), vì bản thân bộ lọc Lĩnh vực đang hỏng ở tầng giao
  diện (mục 7 §D1) nên màn và tệp đều ra như không lọc. Điểm 6 vẫn được chứng minh **bằng dạng 2** (lọc *Hình
  thức*): số trên màn đổi 2→1 và tệp xuất đổi theo, md5 khác nhau. Ghi lại đây để người đọc không tưởng dạng 3
  đã chứng minh điều nó không chứng minh được.
- **2026-08-06 13:16 — bổ sung phương pháp đo, không đổi tiêu chí:** phát hiện [Xuất PDF] **không xuất ngay** mà
  mở hộp thoại *"Tùy chọn in báo cáo PDF"* (khổ giấy · hướng giấy) đòi bấm [Xuất file] lần nữa. Lần đo đầu tôi
  tưởng nút "bấm không có phản ứng" (0 request, 0 thông báo) — thực chất hộp thoại đang mở và **nuốt luôn cú
  click kế tiếp** vào [Xuất Excel]. Đã tải lại trang, làm lại bằng chuột thật rồi hoàn tất luồng. Ghi lại vì
  nếu tin phép đo đầu thì đã log **sai** một lỗi *"nút Xuất PDF không hoạt động"* không hề tồn tại.
- **2026-08-06 13:12 — cảnh báo phương pháp:** khi tôi xoá bộ lọc bằng sự kiện chuột **giả lập** trong script,
  hai nút xuất bị kẹt ở trạng thái mờ (disabled) dù báo cáo đã render. Tải lại trang thì hết. ⇒ Đó là **hệ quả
  của cách đo**, không phải lỗi của phần mềm; **không** log. Mọi phép đo quyết định verdict sau đó đều thực
  hiện bằng **chuột thật** trên giao diện.
- **2026-08-06 13:24 — chụp ảnh khung thông báo tự tắt:** khung *"Forbidden"* chỉ sống **~3,2 giây**, ngắn hơn
  độ trễ của công cụ chụp. Đã thử **4 lượt**, lượt thứ 4 (hẹn giờ bấm sau 3 500 ms rồi mới gọi chụp) bắt được
  ảnh. Kèm số đo hình học + vòng đời để chứng minh người dùng nhìn thấy thật.
