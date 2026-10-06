# Tiêu chí verify — CGTVPL_06

```
Mã case: CGTVPL_06 (tab `bug` dòng 210)      Thời điểm viết: 2026-08-06 14:22
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 14:26 → 14:47
Bản dựng (TỰ ĐO 2026-08-06 14:47, không chép từ đâu):
  index.html      etag W/"6a74340b-428"     last-modified Thu, 06 Aug 2026 07:13:15 GMT
  gói giao diện   assets/index-DIABnbIr.js  etag W/"6a74340b-1124ed"
                  md5 3904131cf562e0349890ac1bd058eb1f · 1.123.565 B
  nhãn trong ứng dụng: HTPLDN · V1.0.8
Verdict: 🔁 REOPEN
```

🔴 **Cảnh báo trôi bản dựng — bắt buộc ghi.** Môi trường vừa được dựng lại lúc **07:13 GMT
(14:13 giờ máy)**, tức **sau khi** các case anh em trong cùng lô đo xong. Các case đó đo trên gói
`assets/index-CNwX9JjX.js` (md5 `e0e4f737b1fb7ab9409f459a4d0fa051`); tôi đo trên
`assets/index-DIABnbIr.js` (md5 `3904131cf562e0349890ac1bd058eb1f`). **Nhãn trong ứng dụng
KHÔNG đổi — vẫn `V1.0.8` ở cả hai lần dựng** ⇒ không được dùng nhãn để nhận biết bản dựng.
Hệ quả: số đo của tôi và số đo của case anh em **không so trực tiếp được với nhau**.

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `tieuchi/LDTBDDDR_06.md` — file tiêu chí case **anh em** (màn *BC Lớp đào tạo đã diễn ra*, FR-IX-07).
>   Đọc để tham khảo **bố cục** và **bẫy thao tác**. **Không chép kết luận**: khác màn, khác đường dẫn dữ
>   liệu, khác bộ lọc đặc thù (màn tôi có **2** bộ lọc: Loại TVV + Lĩnh vực chuyên môn), khác bộ chỉ số
>   đầu ra (`tong_tvv` / `so_tvv` / `so_cg` thay vì `tong_da_dien_ra` / `tong_hoc_vien`), và **khác bản
>   chất báo cáo** — FR-IX-08 là báo cáo **snapshot** (đếm CG/TVV *đang hoạt động*), không phải báo cáo
>   theo kỳ.
> - `bug-report.md` §Phần 3 (`BUG-SLHDVM-006`), §Phần 6 (`BUG-CLDTBDDDR-006`), §Phần 7 (`BUG-LDTBDDDR-006`)
>   — ba phiếu cùng gốc 403 ở vai trò QTHT.
> - `cau-hoi-BA.md` §Mục 2 — câu hỏi *"QTHT có được xuất báo cáo thống kê không"* **đã mở** lúc 12:40 khi
>   verify `SLCTHT_06`. ⇒ **Không mở mục trùng.**
> - `B5-CONTEXT.md` §4 có nhắc **số đo cũ 03/08/2026** (bản dựng V1.0.4, env đối tác): tệp xuất khi đó tên
>   `bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu hẳn giờ-phút.
> - Phiên chính báo trước: màn **FR-IX-06** có lỗi giao diện gửi `linhVuc=<id>` trong khi máy chủ nhận
>   `linhVucId=<id>` ⇒ bộ lọc Lĩnh vực vô tác dụng; màn **FR-IX-07** không dính (không có bộ lọc đó).
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ**, không lấy số đo cũ, không lấy kết quả case anh em làm ngưỡng.
> Riêng thông tin về lỗi `linhVuc`/`linhVucId` chỉ dùng để **quyết định phải đo bộ lọc Lĩnh vực** (màn của
> tôi **có** bộ lọc này), **không** dùng làm kết luận — phải tự đo trên màn của mình.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** — 2 vế triệu chứng (2 vòng nghiệm thu, cùng thao tác bấm **[Xuất Excel]** trên màn
*Báo cáo thống kê → **BC Số lượng CG/TVV***) + 1 vế kỳ vọng về tên tệp:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo
  **"Forbidden"** ⇒ vẫn không có tệp; triệu chứng đổi từ *lỗi tạo tệp* sang *bị chặn quyền*.
- **Vế c (ô `Kết quả mong đợi`)** — *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.
  **Tên tệp xuất: `BaoCaoDanhGia_{YYYYMMDD_HHmm}.xlsx` / `.pdf`**"*

🔴 **Vế c đo được, KHÔNG đẩy sang BA.** BA đã chốt **2026-08-04** khuôn tên tệp cho nhóm IX và đặc tả đã sửa
theo (dấu `[BA chốt 2026-08-04]` nằm ngay trong `:85`, `:86`, `:1092`); ngày **2026-08-06** khuôn này còn được
nâng thành quy ước chung ở **Phụ lục E §H8** (`srs-v3.5.md:6716`). Đây là **áp quyết định có sẵn**, QA chấm được.

⚠️ **Đo theo KHUÔN, không đo theo chuỗi đối tác viết.** Đối tác viết cứng `BaoCaoDanhGia` — chuỗi này thực
ra là tên của **loại báo cáo khác** (*BC Đánh giá hiệu quả HTPL*, FR-IX-09), đối tác chép sang dòng này.
Đặc tả chỉ đòi `{TenBaoCao}` = **tên loại báo cáo của chính báo cáo được xuất**, viết liền PascalCase, bỏ
dấu, bỏ ký tự không phải chữ/số. ⇒ **Cấm chấm Fail chỉ vì tên tệp không đúng y hệt chữ `BaoCaoDanhGia`**
(đó là prescribe), và cũng **cấm chấm Pass** nếu tên tệp mang tên một loại báo cáo khác.

### Bằng chứng — đã MỞ XEM full-res (2026-08-06 14:10 và 14:12)

| Vòng | Tệp | Thấy gì |
|---|---|---|
| **1** | `partner-evidence/CGTVPL_06.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=**so-luong-cg-tvv**&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001&**fd_li…**` (đoạn cuối bị thanh địa chỉ cắt). Loại BC = *BC Số lượng CG/TVV*, Kỳ **Năm** 01/01→31/12/2026, Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**, bộ lọc **Loại TVV để trống**, **Lĩnh vực chuyên môn = *Thuế***. Báo cáo đã render: *Thời điểm tạo **16/07/2026 14:16***, thẻ **Tổng Tư vấn viên = 9** · **Số Tư vấn viên = 4** · **Số Chuyên gia = 5**. Khung thông báo đỏ **"Không thể tạo file xuất. Vui lòng thử lại."** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0**. Đồng hồ máy: 02:17 PM 2026-07-16 |
| **2** | `partner-evidence/CGTVPL_06_v2.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=**so-luong-cg-tvv**&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Loại BC = *BC Số lượng CG/TVV*, Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Toàn quốc**, **cả 2 bộ lọc đặc thù để trống** (Loại TVV · Lĩnh vực chuyên môn). Báo cáo đã render: *Thời điểm tạo **31/07/2026 14:57***, thẻ **Tổng Tư vấn viên = 10** · **Số Tư vấn viên = 5** · **Số Chuyên gia = 5**. Khung thông báo đỏ **"Forbidden"** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0.3**. Đồng hồ máy: 02:57 PM 2026-07-31 |

🔴 **Cả 2 vòng đều có bằng chứng riêng, đều đúng màn của case này** (kiểm bằng 3 chỗ: chuỗi `so-luong-cg-tvv`
trong URL · chữ trong dropdown *Loại báo cáo* · tiêu đề khối kết quả *BC Số lượng CG/TVV*). **Không** nhầm với
*BC Đánh giá hiệu quả HTPL* (FR-IX-09, dòng 214) — màn đó có bộ lọc *Đợt đánh giá* và chỉ số điểm trung bình,
hoàn toàn khác 3 thẻ đếm người ở đây.

⚠️ **Hai vòng KHÔNG so sánh trực tiếp được với nhau** (bắt buộc ghi theo flow §Cổng bằng chứng): **cùng vai
trò** (QTHT · BTP·TW) và **cùng loại báo cáo**, nhưng **khác bản dựng** (V1.0 → V1.0.3), **khác đơn vị**
(Cục BTTP → Toàn quốc) và **khác bộ lọc Lĩnh vực** (Thuế → trống). Vì vậy phải đo **cả hai cấu hình bộ lọc**
chứ không chỉ cấu hình vòng 2.

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (+ Phụ lục E ở
`srs-v3.5.md`) — **đã mở file đọc đúng dòng 2026-08-06 14:15**, số dòng lấy bằng `grep -n`, không lấy từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-11-bao-cao.md:62` | Preconditions chung — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"* |
| `:79` | Processing chung bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị"* (BR-AUTH-01) ⇒ kiểm quyền nằm **đầu luồng**, trước cả bước truy vấn và bước xuất |
| `:82` | Bước 4 — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* |
| `:85` | Bước 7 — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). **Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo"* `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` |
| `:86` | Bước 8 — PDF theo TT17/2025; *"Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo Phụ lục E §H8"* `[BA chốt 2026-08-04]` — *"`{TenBaoCao}` là tên loại báo cáo **viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số** (dấu `/`, khoảng trắng, dấu câu)"* |
| `:113` | E3 · Không có dữ liệu · **INF-RPT-01** · *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* · INFO |
| `:116` | E6 · Lỗi xuất file · **ERR-RPT-04** · *"Không thể tạo file xuất. Vui lòng thử lại"* · ERROR ⇒ **đúng câu vế a** |
| `:117` | E7 · Không có quyền · **ERR-RPT-05** · *"Bạn không có quyền xem báo cáo này"* · ERROR ⇒ nhánh quyền của **vế b** |
| `:123` | AC chung — *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (Phụ lục E §H8)"* |
| `:124` | AC chung — *"**Given** CB nhấn 'Xuất PDF' … **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`** (Phụ lục E §H8)"* |
| `:429` | **FR-IX-08: BC Số lượng CG/TVV (UC131)** — màn hình SCR-IX-01 |
| `:438` | Mô tả — *"Báo cáo **snapshot** số lượng chuyên gia/tư vấn viên (CG/TVV) **đang hoạt động**, phân theo loại, lĩnh vực, đơn vị"* `[STT96 UAT 2026-06-02: bỏ chiều "địa bàn"; bỏ NHT khỏi báo cáo này]` |
| `:440` | **Tác nhân:** *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:448` | Input đặc thù #1 — `loai_tvv`, text, **không bắt buộc**, ràng buộc **`TVV / CG`** |
| `:449` | Input đặc thù #2 — `linh_vuc_id`, identifier, **không bắt buộc**, **`FK → DANH_MUC`** ⇒ màn này **CÓ** bộ lọc Lĩnh vực (khác hẳn FR-IX-07) |
| `:450` | Input đặc thù #3 — `don_vi_id`, FK → DON_VI (*đơn vị quản lý/công nhận TVV*) |
| `:452` | Công thức — *"Đếm TVV/CG **đang hoạt động** trong `TU_VAN_VIEN` (**snapshot**), theo phạm vi đơn vị. NHT lưu ở entity riêng `NGUOI_HO_TRO`"* |
| `:454` | Dimensions — *"Đơn vị, Loại (TVV/CG), Lĩnh vực chuyên môn"* |
| `:460`–`:466` | Output đặc thù, **điều kiện hiển thị "Luôn"**: `tong_tvv` (Tổng CG/TVV đang hoạt động) · `so_tvv` (Số TVV) · `so_cg` (Số CG) · `theo_don_vi[]` {don_vi, ten, tvv, cg} · `theo_linh_vuc[]` {linh_vuc, ten, so_luong}. Hai dòng `so_nht` và `theo_dia_ban[]` **đã BỎ** `[STT96 UAT 2026-06-02]` |
| `:469` | AC bổ sung — *"**Given** CB tạo BC snapshot **When** hiển thị **Then** tổng TVV/CG phân theo **đơn vị + lĩnh vực + loại**"* |
| `:470` | AC bổ sung — *"**Given** CB **lọc loại CG** **When** filter **Then** chỉ hiển thị Chuyên gia"* ⇒ bộ lọc Loại TVV **phải có tác dụng thật** |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: **Sau khi đã 'Xem báo cáo'**"* (không kèm điều kiện vai trò) |
| `:1053` | SCR-IX-01 item 9 — *"Nút Xuất PDF · 'Xuất PDF (.pdf)' · **click → auto-download** · Điều kiện hiển thị: Sau khi đã 'Xem báo cáo'"* |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1071` | Mapping dropdown — **UC131 *BC Số lượng CG/TVV*, bộ lọc đặc thù = *Loại TVV, Lĩnh vực CM, Đơn vị (quản lý/công nhận)***, biểu đồ *Donut + Bar*. (So sánh: `:1070` UC130 chỉ có *Hình thức*) |
| `:1092` | Quy tắc tương tác — *"Export XLSX/PDF **chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file**… Tên tệp cả hai định dạng theo Phụ lục E §H8 — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`"* `[BA chốt 2026-08-04]` |
| `:1268` | BR-AUTH-08 — cột *Ngoại lệ* ghi **"QTHT bypass"**, cột *Áp dụng* ghi **"Toàn bộ FR-IX"** |
| `:1280` | BR-DATA-06 — *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |
| `srs-v3.5.md:6716` | **Phụ lục E §H8 — Tên tệp xuất thống nhất** (BẮT BUỘC): *"Khuôn: `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (**kể cả dấu gạch nối**, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn… **Phần giờ-phút bắt buộc** để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa 255 ký tự"* `[BA chốt 2026-08-06]` |

**Rẽ nhánh — quyết TRƯỚC khi viết mục 4 (rẽ theo TỪNG VẾ):**

| Vế | Đặc tả | Verdict nhánh |
|---|---|---|
| **a** — *"Không thể tạo file xuất"* | **Nói rõ** và **khớp** kỳ vọng: `:1052` ghi thẳng *click → auto-download*, `:123` ghi *tải file .xlsx*; `:116` cho biết ERR-RPT-04 chỉ dành cho tình huống lỗi tạo tệp thật | Chấm được → viết mục 4 |
| **b** — *"Forbidden"* | **Nói rõ** về **câu chữ** khi từ chối vì quyền: `:117` đòi thông báo tiếng Việt *"Bạn không có quyền xem báo cáo này"*. Dù nghiệp vụ chốt hướng nào thì chuỗi tiếng Anh thô cũng lệch dòng này | Chấm được → viết mục 4 |
| **c** — khuôn tên tệp | **Nói rõ** và **khớp** kỳ vọng, **BA đã chốt 2026-08-04** (+ §H8 2026-08-06). Áp quyết định có sẵn | Chấm được → viết mục 4 |

⚠️ **Một điểm KHÔNG chấm:** câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* là chỗ
đặc tả **tự mâu thuẫn** (`:62`/`:440` liệt kê tác nhân CB Nghiệp vụ / CB Phê duyệt ↔ `:1268` ghi ngoại lệ
*"QTHT bypass"* áp *"Toàn bộ FR-IX"*). Câu hỏi này **đã có mục sẵn** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§Mục 2 (mở lúc 12:40 khi verify `SLCTHT_06`, cùng nguyên nhân gốc) ⇒ **không mở mục trùng**. Mục đó **không
kéo verdict** của case: dù BA chốt hướng nào, hành vi hiện tại vẫn phải thoả `:117`.

**IM LẶNG về:**
- **Chữ chính xác của thông báo thành công** khi xuất được — `:1058` mô tả *"Xuất thành công"* ở bảng thành
  phần màn hình, nhưng bảng Error Handling **không** có mã INF/WRN tương ứng ⇒ không chấm Fail vì chữ khác.
- **Có bắt buộc hiện toast *"Đang tạo file…"* hay không** — cùng lý do trên.
- **Bố cục bên trong tệp**: tên sheet, thứ tự cột, cách trình bày bảng. Đặc tả chỉ quy định **header file**
  phải có tiêu đề BC + kỳ + đơn vị + ngày tạo (`:1092`).
- **Có bao nhiêu thẻ số liệu phải vẽ trên màn** — `:460`–`:466` quy định **output của báo cáo**, không quy
  định màn hình phải vẽ đủ mấy thẻ.
- **Ý nghĩa của kỳ báo cáo với một báo cáo snapshot** — `:454` không liệt kê "Kỳ" trong Dimensions của
  FR-IX-08, nhưng `ky_bao_cao` vẫn là input **bắt buộc** của template chung (`:69`). Đặc tả không nói kỳ có
  ảnh hưởng tới con số snapshot hay không ⇒ **không chấm Fail** vì đổi kỳ mà số không đổi.

---

## 3. Precondition

- **Tài khoản ra verdict cho vế a + vế c:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương**
  (`CB_NV_TW`), cấp **TW**, phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-08 (`:440`).
  Fallback (Rule 7, **cùng vai trò + cùng cấp**): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Tài khoản bắt buộc dùng cho vế b:** vai trò **Quản trị viên · QTHT**, đơn vị **BTP · TW** — **chính vai
  trò đối tác dùng ở CẢ HAI vòng** (đọc từ góc phải trên `CGTVPL_06.jpg` và `CGTVPL_06_v2.jpg`). Vế b là
  *"Forbidden"*, tức **triệu chứng phân quyền**; đo bằng vai trò khác thì không tái hiện được điều đối tác nêu.
  > **Vì sao không vướng quy tắc "tài khoản quản trị không ra verdict":** quy tắc đó chặn việc **quyền rộng
  > che lỗi phân quyền**. Ở đây chiều ngược lại — QTHT là vai trò **bị chặn**, dùng nó để **phơi** lỗi chứ
  > không che. Vế a và vế c vẫn ra verdict bằng `cbnv_tw_05`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**, Loại BC = **BC Số lượng
  CG/TVV** (`loai=so-luong-cg-tvv`). 🔴 **Không được nhầm sang *BC Đánh giá hiệu quả HTPL*** (FR-IX-09, dòng
  214) — kiểm bằng cả 3 chỗ: chuỗi trong URL · chữ trong dropdown · tiêu đề khối kết quả.
- **Dữ liệu tiền đề:** ≥1 **chuyên gia / tư vấn viên đang hoạt động** (`:452`) trong phạm vi đơn vị được
  chọn, và để đo được bộ lọc thì cần **đủ cả 2 nhánh `loai_tvv`** (TVV và CG) + **≥1 lĩnh vực chuyên môn có
  người**. Không có dữ liệu → đó là `INF-RPT-01` hợp lệ (`:113`), **phải đổi kỳ/đơn vị/bộ lọc** để có dữ
  liệu rồi mới đo nút xuất. **Mọi cấu hình đều rỗng ⇒ GAP chưa đóng ⇒ verdict ô trống**, nêu rõ cần seed gì.
- **Bộ lọc neo theo đối tác — 2 cấu hình, phải phủ CẢ HAI:**
  - **Vòng 2:** Kỳ **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · Loại TVV trống · Lĩnh vực trống.
  - **Vòng 1:** Kỳ **Năm** · cùng khoảng · Đơn vị **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** · Loại TVV
    trống · **Lĩnh vực chuyên môn = *Thuế*** (hoặc lĩnh vực khác nếu môi trường không có người thuộc *Thuế*
    — khai rõ đã đổi sang lĩnh vực nào và vì sao).
  - Thao tác cả hai: [Xem báo cáo] → [Xuất Excel].
- **Cache máy chủ:** trước khi kết luận *"không có dữ liệu"* hoặc *"bộ lọc không tác dụng"*, kiểm trường
  **"Thời điểm tạo"** trên màn xem có nhảy theo từng lượt bấm không; nghi cache thì đổi `denNgay` 1 ngày để
  lấy khoá cache mới.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi `soObserverDangSong = 1`; **đếm thông báo theo mốc giờ khác nhau**, không theo số phần tử.
  > ⚠️ Bài học đã ghi ở `tieuchi/SLHDVM_06.md` §8 và `tieuchi/LDTBDDDR_06.md` §8: bộ bắt kiểu *"nghe node
  > mới được thêm"* **bỏ sót** chữ *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**. Phải đo bù
  > bằng cách lấy mẫu **nội dung** vùng thông báo theo thời gian (`innerText`, ~100 ms/lần) + ghi hình học
  > (vị trí · kích thước · thời gian sống) để chứng minh người dùng nhìn thấy thật.
- ⚠️ **Bẫy thao tác đã biết** (ghi trước khi đo, để không log oan): nút **[Xuất PDF]** mở hộp thoại
  *"Tùy chọn in báo cáo PDF"* chứ **không** tải ngay; hộp thoại còn mở sẽ **nuốt cú bấm [Xuất Excel] kế
  tiếp**. Phải đóng hộp thoại trước khi bấm nút khác. Bấm bằng **chuột thật**, không dùng sự kiện giả lập.

---

## 4. Tiêu chí chấm

### ✅ PASS khi — **đủ cả 10 điều, trên đủ M = 4 dạng ở mục 5**

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
5. **Số liệu trong tệp khớp số liệu đang hiện trên màn.** So từng cặp, tối thiểu **3 chỉ số tổng điều kiện
   "Luôn"** của FR-IX-08 (`:460`, `:461`, `:462`): **Tổng CG/TVV**, **Số TVV**, **Số CG**. Chỉ số nào màn
   không vẽ thẻ riêng thì lấy từ phản hồi của chính lần chạy báo cáo đó. Có bảng phân theo đơn vị
   (`:464`) hoặc theo lĩnh vực (`:465`) trong tệp thì **tổng các dòng phải cộng khớp** chỉ số tổng tương
   ứng. Ngoài ra `so_tvv + so_cg` phải **cộng khớp** `tong_tvv`.
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280`): với 4 dạng ở mục 5, số liệu trong tệp **đổi theo** và mỗi
   lần đều khớp số trên màn của **chính lần đó** — không phải luôn trả bản không lọc. Kiểm chéo bằng md5 các
   tệp: 2 dạng cho số trên màn khác nhau mà tệp giống hệt ⇒ vi phạm.
7. **Bộ lọc đặc thù có tác dụng thật ở CẢ HAI trường đặc tả khai** (`:448` `loai_tvv`, `:449` `linh_vuc_id`;
   `:470` đòi *"lọc loại CG → chỉ hiển thị Chuyên gia"*): với mỗi bộ lọc, **số trên màn** và **số máy chủ
   trả về** phải đổi đúng theo giá trị chọn, và **tham số giao diện gửi lên phải được máy chủ áp dụng**.
   Phép đo quyết định: so **số liệu trên màn** với **số liệu gọi thẳng máy chủ đúng tham số đó**; hai đường
   lệch nhau ⇒ bộ lọc không có tác dụng.
   *(Đây là điều kiện của chính đặc tả `:470`, không phải suy từ lỗi của màn FR-IX-06.)*
8. **Tên tệp .xlsx đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (`:85`, `:123`, `:1092`, §H8
   `srs-v3.5.md:6716`) — lấy tên từ **nguồn người dùng thật thấy** (tệp rơi về máy, hoặc `content-disposition`
   của phản hồi). Đo đủ **4 điều kiện của khuôn**:
   - **8a.** Có đoạn thời gian `_YYYYMMDD_HHmm` ngay trước đuôi tệp: **8 chữ số ngày + `_` + 4 chữ số giờ-phút**,
     và **giá trị khớp thời điểm xuất** (không phải hằng số/ngày cũ). *Phần giờ-phút là bắt buộc.*
   - **8b.** Phần `{TenBaoCao}` chỉ gồm **chữ cái không dấu và chữ số**; **không** dấu gạch nối, **không**
     khoảng trắng, **không** dấu tiếng Việt, **không** dấu câu. Gạch dưới chỉ dùng để ngăn đoạn.
   - **8c.** Phần `{TenBaoCao}` **nhận ra được là tên của chính loại báo cáo này** — báo cáo **số lượng
     CG/TVV**. 🔴 Tên tệp trỏ sang loại báo cáo khác (vd chuỗi mang nghĩa *đánh giá*, *đào tạo*, *chi phí*)
     là **trượt**, vì `:85` đòi `{TenBaoCao}` là *tên loại báo cáo* của chính báo cáo được xuất.
     *(Cấm đòi đúng chuỗi `BaoCaoDanhGia` — đó là prescribe, và chuỗi đó còn là tên của loại báo cáo khác.)*
   - **8d.** Đuôi tệp là `.xlsx` khi bấm [Xuất Excel]; tổng độ dài tên ≤ 255 ký tự.
   - **Phép thử chống đè tệp** (lý do BA chốt bắt buộc giờ-phút): xuất **2 lần cùng ngày ở 2 phút khác nhau**
     phải ra **2 tên tệp khác nhau**.
9. **Nút [Xuất PDF] — vế `hoặc .pdf` trong câu kỳ vọng của đối tác:** người dùng nhận được tệp `.pdf` và tên
   tệp đúng **cùng khuôn** (`:86`, `:124`) theo đúng 4 điều kiện 8a–8d (đuôi `.pdf`).
   *Chỉ đo tên tệp + có nhận được tệp — nội dung bên trong PDF không thuộc vế đối tác nêu.*
10. **Vai trò đối tác thật sự dùng (Quản trị viên · QTHT, BTP·TW)** — vế b. Thao tác [Xuất Excel] phải kết
    thúc bằng **một trong hai**:
    - **(a)** nhận được tệp thoả điều 2–8; **hoặc**
    - **(b)** bị từ chối kèm **thông báo tiếng Việt cho người dùng biết họ không có quyền**, theo `:117`.

### ❌ FAIL nếu — bất kỳ điều nào, ở bất kỳ dạng nào trong M

- Bất kỳ lượt nào trong M dạng sinh thông báo *không tạo được tệp* hoặc *từ chối quyền* ở vai trò
  `cbnv_tw_05` (tức tái hiện vế a).
- Bấm xuất mà **không** có tệp nào đến tay người dùng (không có tệp tải về **và** phản hồi không phải tệp đính kèm).
- Có "tệp" nhưng `openpyxl` **không** mở được (thực chất là JSON/HTML lỗi đổi đuôi).
- Tệp mở được nhưng **thiếu** ≥1 trong 4 thông tin header ở `:1092`.
- Số liệu trong tệp **lệch** số trên màn ở bất kỳ chỉ số nào trong 3 chỉ số tổng bắt buộc, hoặc các dòng chi
  tiết **không cộng khớp** tổng, hoặc `so_tvv + so_cg ≠ tong_tvv`.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc cho số trên màn khác nhau nhưng tệp giống hệt nhau).
- **Bộ lọc đặc thù không có tác dụng** (điều 7): chọn giá trị lọc mà số liệu không đổi trong khi gọi thẳng
  máy chủ với đúng giá trị đó **lại đổi** ⇒ bộ lọc hỏng.
- **Tên tệp trượt bất kỳ điều kiện nào trong 8a–8d** — đặc biệt: **thiếu phần giờ-phút**, hoặc ngày ghi dạng
  có dấu gạch nối (`YYYY-MM-DD`), hoặc tên có gạch nối/khoảng trắng, hoặc 2 lần xuất cùng ngày trùng tên,
  **hoặc tên tệp mang tên loại báo cáo khác**.
- Nút [Xuất PDF] không trả tệp, hoặc tên tệp PDF trượt khuôn (điều 9).
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
- **Kỳ/đơn vị/bộ lọc không có dữ liệu** → `INF-RPT-01` (`:113`) là hành vi **hợp lệ**, không phải lỗi xuất tệp.
- **Đổi kỳ báo cáo mà con số không đổi** — FR-IX-08 là báo cáo **snapshot** (`:438`, `:452`) và `:454` không
  liệt kê "Kỳ" trong Dimensions; đặc tả im lặng về ảnh hưởng của kỳ lên số snapshot.
- **Số liệu trên màn khác số liệu đối tác chụp** (9/4/5 vòng 1 · 10/5/5 vòng 2) — khác env, khác thời điểm,
  dữ liệu QA đã đổi.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).
- **Màn không vẽ đủ mọi bảng/thẻ số liệu** — `:460`–`:466` quy định output báo cáo, không quy định số thẻ trên màn.
- **Câu hỏi "QTHT có được xuất hay không"** — điểm đặc tả tự mâu thuẫn, đã có mục BA sẵn, không kéo verdict.

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — cả 10 điều
> đều đếm được / so được / nhìn thấy được, không có chữ *"hiển thị đúng"* hay *"hợp lý"*.

---

## 5. Dạng dữ liệu phải phủ — **M = 4**

**Nguồn xác định M** (tra theo đúng thứ tự của flow, dừng khi đủ):
① **đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo**: `:452` *"Đếm TVV/CG đang hoạt động trong
`TU_VAN_VIEN` (snapshot)"* ⇒ chỉ **một** nguồn bản ghi, chưa đủ chia dạng.
② **bộ lọc + giá trị enum ngay trên màn**: `:448` `loai_tvv` ∈ {`TVV`, `CG`} + `:449` `linh_vuc_id`
(FK → DANH_MUC) — và `:1071` xác nhận bộ lọc đặc thù của **UC131 gồm Loại TVV + Lĩnh vực CM + Đơn vị**.
**Dừng ở ②** — đây là các chiều đổi được nội dung tệp xuất, và `:1280` buộc *"file xuất theo bộ lọc hiện
tại"* nên mỗi chiều phải có ít nhất một lượt đo.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc đặc thù** (Loại TVV trống, Lĩnh vực trống, Đơn vị Toàn quốc) | Đúng điều kiện **vòng 2 của đối tác** (`CGTVPL_06_v2.jpg`) — nhánh sinh ra *"Forbidden"* |
| 2 | **Lọc Loại TVV = Tư vấn viên** (`TVV`) | Nhánh enum thứ nhất `:448`; cần để chứng minh `:1280` (*file xuất theo bộ lọc hiện tại*) |
| 3 | **Lọc Loại TVV = Chuyên gia** (`CG`) | Nhánh enum còn lại `:448`, và là **đúng câu AC `:470`** (*lọc loại CG → chỉ hiển thị Chuyên gia*). Hai nhánh cộng lại phải khớp dạng 1 — dùng làm phép cộng-khớp-tổng |
| 4 | **Lọc Lĩnh vực chuyên môn = 1 giá trị có dữ liệu** (đối tác dùng *Thuế* ở vòng 1) | Chiều lọc `:449` — **đúng điều kiện vòng 1 của đối tác** (`CGTVPL_06.jpg`), nhánh sinh ra *"Không thể tạo file xuất"*. Cũng là chiều duy nhất kiểm được điều 7 cho `linh_vuc_id` |

Kỳ báo cáo giữ cố định **Năm 2026** (01/01/2026 → 31/12/2026) cho cả 4 dạng. Đơn vị giữ **Toàn quốc** cho
dạng 1–3 (trùng vòng 2 của đối tác); riêng dạng 4 chạy **cả 2 phạm vi** — Toàn quốc (để so được với dạng 1)
và **Cục Bổ trợ tư pháp - BTP-TW** (trùng khít vòng 1 của đối tác).

> ⚠️ **Nếu một nhánh không có dữ liệu** (vd 0 chuyên gia, hoặc lĩnh vực *Thuế* không có ai): vẫn chạy dạng
> đó, ghi rõ màn trả `INF-RPT-01` và **không** chấm Fail vì thiếu dữ liệu (`:113`); nhưng phải khai trong
> mục 6 rằng dạng đó **không** dùng để chứng minh điều 6/7, và phải chứng minh bằng dạng còn lại. Lĩnh vực
> *Thuế* rỗng thì **đổi sang lĩnh vực khác có người** và khai rõ đã đổi sang gì.

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 14:22). 2 cột sau điền sau khi đo xong.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Cả 2 vòng:** *Quản trị viên · QTHT*, đơn vị **BTP · TW** (đọc góc phải trên cả `CGTVPL_06.jpg` và `CGTVPL_06_v2.jpg`) | **Phủ CẢ HAI vai trò, hai ngữ cảnh trình duyệt tách biệt.** ① `cbnv_tw_05` — `/auth/me` trả `hoTen "CB Nghiệp vụ - Trung ương #05"` · `vaiTro ["CB_NV_TW"]` · `capDonVi "TW"` · `donViId …0001` (đúng tác nhân đặc tả `:440`; **không** dùng fallback Rule 7). ② tài khoản quản trị `admin` — `/auth/me` trả `hoTen "Quản trị hệ thống"` · `vaiTro ["QTHT"]` · `capDonVi "TW"` · **`donViId …0001` TRÙNG đơn vị với ①** ⇒ đúng *Quản trị viên · QTHT · BTP·TW* của đối tác, và khác ① **chỉ ở vai trò** | **Không** |
| Entity + trạng thái | **Vòng 1:** BC *Số lượng CG/TVV* đã render có dữ liệu (Tổng TVV **9** · Số TVV **4** · Số CG **5**), *Thời điểm tạo 16/07/2026 14:16*. **Vòng 2:** đã render (Tổng **10** · TVV **5** · CG **5**), *Thời điểm tạo 31/07/2026 14:57*. Cả 2 vòng nút [Xuất Excel]/[Xuất PDF] đều bấm được | **Cùng trạng thái: báo cáo đã chạy xong, có dữ liệu, nút xuất bật.** Vai trò ①: Tổng **6** · TVV **4** · CG **2**, *Thời điểm tạo 06/08/2026 14:28*. Vai trò ② (QTHT): GET `so-luong-cg-tvv` → **200**, màn render đủ **6 / 4 / 2**, *Thời điểm tạo 06/08/2026 14:40*, **cả 2 nút xuất hiện và bật** (`disabled=false`) — ảnh `…-06-…`. ⇒ tái hiện đúng tình huống đối tác: **xem được, bấm xuất được, chỉ chết ở bước xuất** | **Không** |
| Dữ liệu tiền đề | Có CG/TVV **đang hoạt động** trong phạm vi chọn: vòng 1 phạm vi *Cục BTTP* + lĩnh vực *Thuế* ra 9 người; vòng 2 phạm vi *Toàn quốc* ra 10 người | **Có, và đủ cả 2 nhánh `loai_tvv`** — Toàn quốc có **6** người đang hoạt động (**4 TVV + 2 CG**), trải **4 đơn vị** và **5 lĩnh vực** (Thương mại 3 · Lao động 1 · Đất đai 1 · **Thuế 1** · Doanh nghiệp 1). Lĩnh vực **Thuế** đối tác dùng ở vòng 1 **có người** ⇒ **không phải đổi** sang lĩnh vực khác. Không lần nào rơi vào `INF-RPT-01`. **Số ít hơn đối tác (6 vs 9/10) là do khác env**, không phải thiếu dữ liệu — đã đủ để chấm cả 10 điều mục 4 | **Không** |
| Input / filter / giá trị nhập | **Vòng 1:** Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Cục Bổ trợ tư pháp - BTP-TW**, Loại TVV **trống**, **Lĩnh vực chuyên môn = Thuế**; URL có `donViId=…0001&fd_li…`. **Vòng 2:** cùng kỳ, Đơn vị **Toàn quốc**, **cả 2 bộ lọc trống**. Thao tác cả 2 vòng: [Xem báo cáo] → [**Xuất Excel**] | **Phủ cả 2 cấu hình đối tác + 2 cấu hình bù.** Kỳ **Năm** 01/01→31/12/2026 giữ cố định. Cấu hình **vòng 2** (Toàn quốc · 2 bộ lọc trống) = dạng 1; cấu hình **vòng 1** (Lĩnh vực = **Thuế**) = dạng 4, chạy cả phạm vi Toàn quốc và **Cục BTTP·TW**. Thêm dạng 2 (**Loại TVV = Tư vấn viên**) và dạng 3 (**Loại TVV = Chuyên gia**) mà đối tác không thử. Thao tác đúng chuỗi đối tác: [Xem báo cáo] → [**Xuất Excel**]; bấm bằng **chuột thật** | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 2 lượt xuất (1 mỗi vòng). M = **2** dạng (không lọc · lọc Lĩnh vực=Thuế). Không thấy đối tác thử lọc **Loại TVV**, cũng không thấy thử [Xuất PDF] | **N = 11 lượt xuất · M = 4 dạng (≥ 2 của đối tác).** Vai trò ①: 4 dạng × [Xuất Excel] + 1 lượt **xuất lại dạng 1** (phép thử chống đè) + 1 lượt [**Xuất PDF**] + 1 lượt gọi thẳng máy chủ = **7 lượt, 7/7 ra tệp**. Vai trò ② (QTHT): **2 lượt bấm chuột + 2 lượt gọi thẳng = 4/4 lỗi 403**, 0 tệp. **Đã phủ thêm phần đối tác BỎ TRỐNG:** bộ lọc Loại TVV (cả 2 nhánh enum) và nút [Xuất PDF] | **Không** |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** vòng 1 `htpldn-uat.ospgroup.vn/bao-cao?loai=so-luong-cg-tvv&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001&fd_li…`
  · vòng 2 `htpldn-uat.ospgroup.vn/bao-cao?loai=so-luong-cg-tvv&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu — vòng 1 *Thời điểm tạo* **16/07/2026 14:16**,
  **9 / 4 / 5**; vòng 2 *Thời điểm tạo* **31/07/2026 14:57**, **10 / 5 / 5**.
- **Vai trò + env + bản dựng:** **Quản trị viên QTHT** (BTP · TW) · env `htpldn-uat.ospgroup.vn` ·
  nhãn **HTPLDN · V1.0** (vòng 1, đồng hồ 16/07/2026 14:17) → **V1.0.3** (vòng 2, đồng hồ 31/07/2026 14:57).

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn (V1.0 / V1.0.3 → bản đang đo).
⇒ Mọi kết luận *hết lỗi* chỉ là **tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

---

## 7. Kết quả chấm

# 🔁 REOPEN — còn lỗi, chuyển lại dev

**Một câu:** Hai vế *không tạo được tệp* và *tên tệp* đã hết lỗi trên bản dựng này, nhưng vế **"Forbidden"**
tái hiện **nguyên vẹn 4/4 lượt** với **đúng vai trò đối tác dùng** (Quản trị viên · QTHT · BTP·TW): người
dùng xem được báo cáo, nút xuất bật, bấm xuất thì nhận **chuỗi tiếng Anh thô "Forbidden"** và **không có tệp
nào về máy** — lệch dòng `:117` (đòi câu tiếng Việt *"Bạn không có quyền xem báo cáo này"*).

### 7.1 Chấm theo TỪNG VẾ đối tác nêu

| Vế | Đối tác gặp | Mình đo được | Kết |
|---|---|---|:-:|
| **a** — *"Không thể tạo file xuất. Vui lòng thử lại."* | vòng 1, 16/07, vai trò QTHT | **Không tái hiện** ở vai trò đặc tả `cbnv_tw_05`: **7/7 lượt** ra tệp thật. Chữ trên màn mọi lượt: *"Đang tạo file..."* → *"Tạo file thành công."*, **không** có chữ nào mang nghĩa `:116`. Ở vai trò QTHT thì lỗi hiện tại **không phải** `:116` mà là nhánh quyền (403) ⇒ câu *"Không thể tạo file xuất"* đã hết | ✅ |
| **b** — *"Forbidden"* | vòng 2, 31/07, vai trò QTHT | **TÁI HIỆN NGUYÊN VẸN.** Vai trò QTHT: 2 lượt bấm chuột + 2 lượt gọi thẳng = **4/4** đều `403`, thân trả về `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",…}}`; chữ **nhìn thấy trên màn** đúng là `Forbidden`; **0 tệp** về máy | ❌ |
| **c** — tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}` | ô *Kết quả mong đợi* | **Đúng khuôn, đủ 8a–8d.** `BaoCaoSoLuongCgTvv_20260806_1429.xlsx` — lấy từ **2 nguồn người dùng thật thấy**: tệp rơi về máy **và** `content-disposition` của chính phản hồi. Chống đè đạt (14:29 vs 14:36 → 2 tên khác nhau). Khuôn cũ 03/08 `bao-cao-so-luong-cg-tvv-2026-08-03.xlsx` (gạch nối, thiếu giờ-phút) **đã được sửa** | ✅ |

> **Verdict do vế b quyết.** Flow §Verdict: *fix một phần → Reopen*. Hai vế a/c sạch **không** cứu được case
> khi vế b còn nguyên.

### 7.2 Chấm 10 điều của mục 4

| # | Điều kiện | Đo được | Kết |
|:-:|---|---|:-:|
| 1 | Không báo lỗi tạo tệp / không bị chặn quyền (vai trò đặc tả) | `cbnv_tw_05`, 4/4 dạng: 1 request · chữ *"Đang tạo file..."* → *"Tạo file thành công."* | ✅ |
| 2 | Người dùng thật sự nhận được tệp | 7/7 lượt có tệp rơi về máy; lượt gọi thẳng có `content-disposition: attachment` | ✅ |
| 3 | Mở được như workbook thật | `openpyxl.load_workbook()` mở được cả 5 tệp `.xlsx`, sheet *"BC Số lượng CG TVV"*, có ô không rỗng | ✅ |
| 4 | Header đủ 4 thông tin `:1092` | Mọi tệp có ① *"BC Số lượng CG/TVV"* ② *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ③ *"Đơn vị: Toàn quốc"* ④ *"Ngày tạo: 06/08/2026"* | ✅ |
| 5 | Số liệu trong tệp khớp màn + cộng khớp | Dạng 1 tệp 6/4/2 = màn 6/4/2; cộng cột *Theo đơn vị*: TVV 1+1+1+1=4 ✓ CG 2+0+0+0=2 ✓ Tổng 3+1+1+1=6 ✓; `so_tvv + so_cg` = 4+2 = 6 = `tong_tvv` ✓. Dạng 2 tệp 4/4/0 = màn; dạng 3 tệp 2/0/2 = màn | ✅ |
| 6 | Tệp phản ánh bộ lọc hiện tại (`:1280`) | Dạng 1/2/3 cho 3 nội dung tệp khác nhau (7.034 / 6.954 / 6.871 B), mỗi tệp khớp màn của **chính lần đó**. **Dạng 4 thì không** — xem điều 7 | ⚠️ |
| 7 | **Bộ lọc đặc thù có tác dụng thật ở CẢ HAI trường** (`:448` + `:449`) | **`loai_tvv` ĐẠT** — AC `:470` thoả: lọc CG → tệp chỉ còn Chuyên gia (2/0/2, 1 đơn vị); 2 nhánh cộng khớp 4+2=6. **`linh_vuc_id` KHÔNG ĐẠT** — chọn *Thuế*, số trên màn và **từng ô trong tệp** y hệt bản không lọc; gọi thẳng máy chủ đúng chiều đó thì số **đổi** (1/0/1) ⇒ hai đường lệch nhau | ❌ |
| 8 | Tên tệp `.xlsx` đúng khuôn (8a–8d + chống đè) | 8a ✓ (7 tệp, 7 mốc giờ-phút khác nhau, khớp giờ xuất thật) · 8b ✓ (chỉ chữ không dấu + số) · 8c ✓ (*SoLuongCgTvv* = đúng loại báo cáo này) · 8d ✓ (`.xlsx`, 38 ký tự) · chống đè ✓ | ✅ |
| 9 | Nút [Xuất PDF] — nhận tệp + tên đúng cùng khuôn | `BaoCaoSoLuongCgTvv_20260806_1437.pdf` (34.227 B, `%PDF-1.3`, 1 trang). Ghi nhận: nút mở hộp thoại *"Tùy chọn in báo cáo PDF"* trước, không tải ngay — **không chấm** (ngoài vế đối tác nêu, đặc tả im lặng) | ✅ |
| 10 | **Vai trò QTHT: nhận tệp HOẶC bị từ chối kèm thông báo tiếng Việt** (`:117`) | **Trượt cả hai nhánh.** Không nhận tệp (0/4 lượt), và chữ hiện ra là chuỗi tiếng Anh thô **`Forbidden`** — không phải câu tiếng Việt cho người dùng biết họ không có quyền | ❌ |

**⇒ Trượt điều 10 (vế b của đối tác) và điều 7/6 (ngoài vế đối tác nêu) ⇒ REOPEN.**

### 7.3 Vì sao chắc chắn là lỗi phân quyền, không phải đường xuất tệp hỏng

Phép đối chứng đổi **đúng một biến**: cùng đường dẫn `POST /api/v1/bao-cao/export`, **cùng thân yêu cầu từng
chữ**, cùng `donViId …0001`, cùng phiên đo — chỉ khác vai trò:

| Vai trò | Mã | Header trả về | Kết quả cho người dùng |
|---|:-:|---|---|
| `CB_NV_TW` (`cbnv_tw_05`) | **200** | `content-disposition: attachment; filename="BaoCaoSoLuongCgTvv_20260806_1445.xlsx"` | nhận tệp 7.034 B |
| `QTHT` (`admin`) | **403** | *(không có `content-disposition`)* | `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}` — 0 tệp |

Và ở chính phiên QTHT, bước **XEM** báo cáo lại **200** với dữ liệu đầy đủ (6/4/2) — tức hệ thống cho vai trò
này **vào tận nơi, thấy hết số liệu, bật cả nút xuất**, rồi mới chặn ở cú bấm cuối bằng một chuỗi tiếng Anh.
Đây đúng là hình ảnh đối tác chụp ở vòng 2.

**Không kết luận** QTHT *nên* hay *không nên* được xuất — đó là chỗ đặc tả tự mâu thuẫn (`:62`/`:440` ↔
`:1268` *"QTHT bypass"* áp *"Toàn bộ FR-IX"*), đã có mục hỏi BA sẵn ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§Mục 2. **Dù BA chốt hướng nào**, hành vi hiện tại vẫn lệch `:117`: chặn thì phải nói bằng tiếng Việt cho
người dùng hiểu, không phải ném mã kỹ thuật.

### 7.4 Quan sát NGOÀI vế đối tác nêu — **không kéo verdict của case**

> Theo flow §Ca biên: *"Phát hiện mới nằm trong đúng màn/cột đang tranh chấp nhưng đối tác KHÔNG nêu →
> verdict của case chỉ do các vế đối tác nêu quyết định."* Verdict trên đã là REOPEN vì vế b, nên phần này
> **không** làm đổi kết quả — ghi lại để phiên chính xử.

**Bộ lọc "Lĩnh vực chuyên môn" của màn này KHÔNG có tác dụng.** Giao diện gửi khoá `linhVucCm`, máy chủ chỉ
nhận `linhVucId`. Đo cùng phiên, cùng kỳ, chỉ đổi **tên khoá**:

| Khoá gửi lên | Mã | Tổng | TVV | CG | Dòng ĐV | Dòng LV | `ngayTaoBc` |
|---|:-:|:-:|:-:|:-:|:-:|:-:|---|
| *(không có)* | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
| **`linhVucCm`** ← giao diện gửi | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
| **`linhVucId`** ← máy chủ nhận | 200 | **1** | **0** | **1** | **1** | **1** | `07:47:30.053Z` |
| `linhVuc` | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
| `linh_vuc_id` | 200 | 6 | 4 | 2 | 4 | 5 | `07:45:41.477Z` |
| `loaiTvv=CG` *(đối chứng)* | 200 | **2** | **0** | **2** | 1 | 4 | `07:47:30.297Z` |
| `loaiTvv=TVV` *(đối chứng)* | 200 | **4** | **4** | **0** | 4 | 2 | `07:47:30.370Z` |

**Loại trừ nhớ đệm — bằng chứng cứng:** 4 dòng cho ra 6/4/2 dùng **CHUNG một `ngayTaoBc`**
`07:45:41.477Z` ⇒ máy chủ coi chúng là **cùng một khoá nhớ đệm**, tức `linhVucCm` / `linhVuc` /
`linh_vuc_id` **không hề tham gia** khoá. Ngược lại `linhVucId` và `loaiTvv` sinh `ngayTaoBc` **mới** ⇒ được
nhận. Hai hành vi này không thể giải thích bằng nhớ đệm.

Ảnh hưởng tới tệp xuất: dạng 4 (lọc *Thuế*) cho tệp **giống hệt từng ô** với bản không lọc ⇒ vi phạm
`:1280` (*"file xuất theo bộ lọc hiện tại"*). Kích thước qua gọi thẳng: không lọc 7.033 B · `linhVucCm`
7.033 B (y hệt) · `linhVucId` 6.789 B · `loaiTvv=CG` 6.870 B.

**Trả lời câu phiên chính hỏi (lỗi `linhVuc`/`linhVucId` của FR-IX-06 có lan tới đây không):**
**CÓ lan, nhưng KHÁC TÊN KHOÁ.** FR-IX-06 gửi `linhVuc`; màn này (FR-IX-08) gửi `linhVucCm`. Cùng một kiểu
sai (giao diện đặt tên khoá khác máy chủ), **không cùng một chuỗi** ⇒ ai sửa thì phải sửa **cả hai chỗ**,
không phải một chỗ. Bộ lọc **Loại TVV** của màn này chạy đúng, AC `:470` thoả.
**Không mở dòng bug mới trên bảng cho phát hiện này** — báo về phiên chính.

### 7.5 Bằng chứng

| Tệp | Chú thích |
|---|---|
| `image/CGTVPL_06-01-dang1-khong-loc-man-hinh-truoc-khi-xuat-V108.png` | Dạng 1 — vai trò `cbnv_tw_05`, không lọc đặc thù: màn hiện Tổng 6 · TVV 4 · CG 2, *Thời điểm tạo 06/08/2026 14:28*, trước khi bấm [Xuất Excel] |
| `image/CGTVPL_06-02-dang2-loc-LoaiTVV-TuVanVien-man-hinh-truoc-khi-xuat-V108.png` | Dạng 2 — lọc **Loại TVV = Tư vấn viên**: số đổi thành 4 · 4 · 0, chứng minh bộ lọc Loại TVV có tác dụng |
| `image/CGTVPL_06-03-dang3-loc-LoaiTVV-ChuyenGia-man-hinh-truoc-khi-xuat-V108.png` | Dạng 3 — lọc **Loại TVV = Chuyên gia**: 2 · 0 · 2, bảng theo đơn vị chỉ còn 1 dòng ⇒ AC `:470` thoả |
| `image/CGTVPL_06-04-dang4-loc-LinhVuc-Thue-so-lieu-khong-doi-V108.png` | Dạng 4 — lọc **Lĩnh vực chuyên môn = Thuế**: số liệu **vẫn 6 · 4 · 2**, y hệt dạng 1 ⇒ bộ lọc Lĩnh vực không tác dụng |
| `image/CGTVPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png` | Nút [Xuất PDF] mở hộp thoại *"Tùy chọn in báo cáo PDF"* trước khi tải — ghi nhận bẫy thao tác, không chấm |
| `image/CGTVPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png` | Vai trò **Quản trị viên · QTHT · BTP·TW** XEM được báo cáo (6 · 4 · 2, *Thời điểm tạo 14:40*), cả hai nút xuất hiện và bật |
| `image/CGTVPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png` | Vai trò QTHT bấm [Xuất Excel] → khung thông báo **đỏ chữ "Forbidden"** ở đỉnh màn, không tệp nào về máy — tái hiện đúng ảnh vòng 2 của đối tác |
| `image/CGTVPL_06-08-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt` | Nguyên văn chữ trên màn từng lượt · thân + header phản hồi máy chủ (kể cả `403`) · nội dung 5 tệp `.xlsx` đọc bằng `openpyxl` · md5 · phép thử chống đè · bảng đo bộ lọc |
| `testfiles/CGTVPL_06-*.xlsx` · `CGTVPL_06-pdf-*.pdf` | 5 tệp Excel + 1 tệp PDF thật do bản dựng này xuất ra, giữ nguyên tên gốc để soi khuôn tên tệp |

### 7.6 Không đo được / giới hạn hiệu lực

- **Env khác env nghiệm thu.** Đo trên `18.143.165.120.nip.io` (env kiểm thử nội bộ); đối tác chụp trên
  `htpldn-uat.ospgroup.vn`. Kết luận *hết lỗi* của vế a và vế c chỉ có hiệu lực **khi bản dựng này lên môi
  trường nghiệm thu**.
- **Bản dựng trôi giữa lô** — xem cảnh báo đầu file. Số của tôi không so trực tiếp được với case anh em.
- **Không đo** khổ giấy A4 / font Times New Roman cỡ 13 bên trong tệp, nội dung bên trong PDF, bố cục sheet —
  ngoài vế đối tác nêu, đã khai ở mục 4 §*"KHÔNG được chấm Fail vì"*.
- **Không kết luận** QTHT có quyền xuất hay không — chỗ đặc tả tự mâu thuẫn, đã có mục BA sẵn.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 14:22** — viết mục 1–6 **TRƯỚC khi mở màn tranh chấp**. Đã đọc: bằng chứng đối tác (2 tệp,
  full-res), đặc tả (`srs-fr-11-bao-cao.md`, `srs-v3.5.md` §H8), dòng 210 tab `bug`, và hồ sơ QA nội bộ đã
  khai ở đầu file.
- **2026-08-06 14:48 — phân loại lại điều 7, KHÔNG sửa nội dung điều 7.** Lúc 14:22 tôi xếp điều 7 (*bộ lọc
  đặc thù có tác dụng thật ở cả hai trường*) vào danh sách 10 điều PASS, suy từ AC `:470`. Đo xong thấy
  nhánh `linh_vuc_id` **trượt**, nhưng **đối tác không hề nêu vế bộ lọc** — cả hai ảnh chỉ nêu thông báo khi
  bấm xuất. Theo flow §Ca biên, phát hiện nằm đúng màn tranh chấp nhưng đối tác không nêu thì **không được
  kéo verdict của case**. ⇒ Giữ **nguyên văn** điều 7 và **giữ nguyên kết quả trượt** của nó ở bảng mục 7.2;
  chuyển phần luận vào §7.4 và đánh dấu rõ *không kéo verdict*.
  **Ghi rõ để không ai hiểu nhầm:** verdict REOPEN của case này **không** dựa vào điều 7 — nó đứng vững chỉ
  bằng **điều 10 / vế b** (*"Forbidden"*, đúng vế đối tác nêu). Nếu điều 7 đạt thì verdict **vẫn là REOPEN**.
  Không xoá, không làm nhẹ, không sửa mục 4 cho khớp kết quả.
- **2026-08-06 14:47** — điền bản dựng tự đo vào khối đầu file + thêm cảnh báo trôi bản dựng (môi trường
  được dựng lại lúc 07:13 GMT, **sau** khi các case anh em đo xong, mà **nhãn ứng dụng không đổi**).
