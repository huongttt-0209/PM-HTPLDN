# Tiêu chí verify — DGHQHTPL_06

```
Mã case: DGHQHTPL_06 (tab `bug` dòng 214)      Thời điểm viết: 2026-08-06 15:05
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 15:06 → 15:39
Bản dựng (TỰ ĐO — đo 2 lần, đầu phiên 15:06 và cuối phiên 15:36, KHÔNG chép từ case khác):
  index.html      etag W/"6a74340b-428"     last-modified Thu, 06 Aug 2026 07:13:15 GMT
  gói giao diện   assets/index-DIABnbIr.js  etag W/"6a74340b-1124ed"
                  md5 3904131cf562e0349890ac1bd058eb1f · 1.123.565 B
  nhãn trong ứng dụng: HTPLDN · V1.0.8
  ⇒ hai lần đo GIỐNG NHAU ⇒ bản dựng KHÔNG trôi thêm trong suốt phiên đo.
Verdict: 🔁 REOPEN
```

> ⚠️ **Cảnh báo trôi bản dựng (phiên chính báo, mình tự kiểm lại):** môi trường được dựng lại lúc **07:13 GMT
> (14:13 giờ máy)** — gói giao diện đổi từ `index-CNwX9JjX.js` sang `index-DIABnbIr.js` — mà **nhãn trong ứng
> dụng vẫn là V1.0.8**. ⇒ **Nhãn ứng dụng không dùng để nhận diện bản dựng được.** Verdict dưới đây chỉ có
> hiệu lực cho **đúng bó mã md5 `3904131c…`** ghi ở khối trên; bó mã đổi ⇒ phải đo lại.

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `tieuchi/CGTVPL_06.md` — file tiêu chí case **anh em** (màn *BC Số lượng CG/TVV*, FR-IX-08). Đọc để
>   tham khảo **bố cục** và **bẫy thao tác**. **Không chép kết luận:** khác màn (`danh-gia-hieu-qua` ≠
>   `so-luong-cg-tvv`), khác bộ lọc đặc thù (màn tôi có **1** bộ lọc — *Đợt đánh giá*; màn đó có **2** —
>   Loại TVV + Lĩnh vực CM), khác bộ chỉ số đầu ra (`diem_trung_binh` / `so_vu_viec_danh_gia` /
>   `theo_tieu_chi[]` / `theo_dot[]` thay vì `tong_tvv` / `so_tvv` / `so_cg`), và **khác bản chất báo cáo**
>   — FR-IX-09 tính **điểm trung bình có trọng số trong kỳ**, không phải snapshot đếm người.
> - `bug-report.md` §Phần 3 (`BUG-SLHDVM-006`), §Phần 6 (`BUG-CLDTBDDDR-006`), §Phần 7
>   (`BUG-LDTBDDDR-006`), §Phần 8 (`BUG-CGTVPL-006`) — bốn phiếu cùng gốc 403 ở vai trò QTHT.
> - `cau-hoi-BA.md` §Mục 2 — câu hỏi *"QTHT có được xuất báo cáo thống kê không"* **đã mở** lúc 12:40 khi
>   verify `SLCTHT_06`, đã có 4 blockquote bổ sung của các màn khác. ⇒ **Không mở mục hỏi mới.**
> - `B5-CONTEXT.md` §4 có nhắc **số đo cũ 03/08/2026** (bản dựng V1.0.4, env đối tác): tệp xuất khi đó tên
>   `bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu hẳn giờ-phút.
> - Phiên chính báo trước: bộ lọc *Lĩnh vực* của các màn báo cáo đang **lệch tên tham số giữa giao diện và
>   máy chủ** — FR-IX-06 gửi `linhVuc`, FR-IX-08 gửi `linhVucCm`, máy chủ nhận `linhVucId`; FR-IX-07 không
>   dính vì không có bộ lọc đó.
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ**, không lấy số đo cũ, không lấy kết quả case anh em làm ngưỡng.
> Riêng thông tin về lỗi tên khoá bộ lọc chỉ dùng để **quyết định phải đo bộ lọc đặc thù của màn tôi**
> (*Đợt đánh giá*), **không** dùng làm kết luận — phải tự đo trên màn của mình.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** — 2 vế triệu chứng (2 vòng nghiệm thu, cùng thao tác bấm **[Xuất Excel]** trên màn
*Báo cáo thống kê → **BC Đánh giá hiệu quả HTPL***) + 1 vế kỳ vọng về tên tệp:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo
  **"Forbidden"** ⇒ vẫn không có tệp; triệu chứng đổi từ *lỗi tạo tệp* sang *bị chặn quyền*.
- **Vế c (ô `Kết quả mong đợi`)** — *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.
  **Tên tệp xuất: `BaoCaoDanhGia_{YYYYMMDD_HHmm}.xlsx` / `.pdf`**"*

🔴 **Vế c đo được, KHÔNG đẩy sang BA.** BA đã chốt **2026-08-04** khuôn tên tệp cho nhóm IX và đặc tả đã sửa
theo (dấu `[BA chốt 2026-08-04]` nằm ngay trong `:85`, `:86`, `:1092`); ngày **2026-08-06** khuôn này còn được
nâng thành quy ước chung ở **Phụ lục E §H8** (`srs-v3.5.md:6716`). Đây là **áp quyết định có sẵn**, QA chấm được.

⚠️ **Đo theo KHUÔN, không đo theo chuỗi đối tác viết.** Đặc tả chỉ đòi `{TenBaoCao}` = **tên loại báo cáo của
chính báo cáo được xuất**, viết liền PascalCase, bỏ dấu, bỏ ký tự không phải chữ/số. Với màn này, chuỗi
`BaoCaoDanhGia` mà đối tác viết **có thể** là một cách rút gọn hợp lệ của *BC Đánh giá hiệu quả HTPL* — nhưng
**cấm chấm Fail chỉ vì tên tệp không đúng y hệt chuỗi đó** (đó là prescribe), và cũng **cấm chấm Pass** nếu
tên tệp mang tên **một loại báo cáo khác** (vd *số lượng CG/TVV*, *đào tạo*, *chi phí*).

### Bằng chứng — đã MỞ XEM full-res (2026-08-06 14:58 và 15:00)

| Vòng | Tệp | Thấy gì |
|---|---|---|
| **1** | `partner-evidence/DGHQHTPL_06.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=**danh-gia-hieu-qua**&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&**fd_dotDanhGiaId=c4c16832-f885-4fd1-8a96-969ece726…**` (đuôi bị thanh địa chỉ cắt). Loại BC = *BC Đánh giá hiệu quả HTPL*, Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Toàn quốc**, **Đợt đánh giá = *TKM kiểm thử 2*** (có chọn). Báo cáo đã render: *Thời điểm tạo **16/07/2026 14:25***, **3 thẻ**: Tổng đợt đánh giá **1** · Tổng lượt đánh giá **2** · Điểm trung bình chung **7**. Khung thông báo đỏ **"Không thể tạo file xuất. Vui lòng thử lại."** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0**. Đồng hồ máy: 02:25 PM 2026-07-16 |
| **2** | `partner-evidence/DGHQHTPL_06_v2.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=**danh-gia-hieu-qua**&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (**không** có `fd_dotDanhGiaId`). Loại BC = *BC Đánh giá hiệu quả HTPL*, Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Toàn quốc**, **Đợt đánh giá để trống** (ô hiện placeholder *"Chọn Đợt đánh giá"*). Báo cáo đã render: *Thời điểm tạo **31/07/2026 14:59***, **4 thẻ**: Tổng đợt đánh giá **7** · Tổng lượt đánh giá **7** · Tổng số vụ việc đã đánh giá **5** · Điểm trung bình chung **7**. Khung thông báo đỏ **"Forbidden"** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0.3**. Đồng hồ máy: 03:00 PM 2026-07-31 |

🔴 **Cả 2 vòng đều có bằng chứng riêng, đều đúng màn của case này** (kiểm bằng 3 chỗ: chuỗi
`loai=danh-gia-hieu-qua` trong URL · chữ trong ô chọn *Loại báo cáo* · tiêu đề khối kết quả *BC Đánh giá hiệu
quả HTPL*). **Không** nhầm với *BC Số lượng CG/TVV* (FR-IX-08, dòng 210 — màn đó có bộ lọc *Loại TVV* +
*Lĩnh vực CM* và 3 thẻ đếm người), cũng **không** nhầm với màn nghiệp vụ *Đánh giá hiệu quả* ở sidebar
(màn đó là danh sách kế hoạch/đợt đánh giá, không có nút Xuất Excel của báo cáo thống kê).

⚠️ **Hai vòng KHÔNG so sánh trực tiếp được với nhau** (bắt buộc ghi theo flow §Cổng bằng chứng): **cùng vai
trò** (QTHT · BTP·TW), **cùng loại báo cáo**, **cùng kỳ + cùng đơn vị**, nhưng **khác bản dựng**
(V1.0 → V1.0.3), **khác bộ lọc Đợt đánh giá** (*TKM kiểm thử 2* → trống) và **khác cả số thẻ hiện trên màn**
(3 thẻ → 4 thẻ, vòng 2 có thêm *Tổng số vụ việc đã đánh giá*). Vì vậy phải đo **cả hai cấu hình bộ lọc**, chứ
không chỉ cấu hình vòng 2.

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (+ Phụ lục E ở
`srs-v3.5.md`) — **đã mở file đọc đúng dòng 2026-08-06 15:00**, số dòng lấy bằng `grep -n` / `awk`, không lấy
từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-11-bao-cao.md:62` | Preconditions chung — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"* |
| `:69` | Input chung #1 — `ky_bao_cao`, **bắt buộc**, ràng buộc `TUAN / THANG / QUY / NAM / KHOANG` |
| `:72` | Input chung #4 — `don_vi_id`, **không bắt buộc**, *"Auto phân quyền nếu không truyền"* |
| `:79` | Processing chung bước 1 — *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị"* (BR-AUTH-01) ⇒ kiểm quyền nằm **đầu luồng**, trước cả bước truy vấn và bước xuất |
| `:82` | Bước 4 — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* |
| `:85` | Bước 7 — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). **Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo"* `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` |
| `:86` | Bước 8 — PDF theo TT17/2025; *"Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo Phụ lục E §H8"* `[BA chốt 2026-08-04]` — *"`{TenBaoCao}` là tên loại báo cáo **viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số** (dấu `/`, khoảng trắng, dấu câu)"* |
| `:113` | E3 · Không có dữ liệu · **INF-RPT-01** · *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* · INFO |
| `:116` | E6 · Lỗi xuất file · **ERR-RPT-04** · *"Không thể tạo file xuất. Vui lòng thử lại"* · ERROR ⇒ **đúng câu vế a** |
| `:117` | E7 · Không có quyền · **ERR-RPT-05** · *"Bạn không có quyền xem báo cáo này"* · ERROR ⇒ nhánh quyền của **vế b** |
| `:123` | AC chung — *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (Phụ lục E §H8)"* |
| `:124` | AC chung — *"**Given** CB nhấn 'Xuất PDF' … **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`** (Phụ lục E §H8)"* |
| `:474` | **FR-IX-09: BC Đánh giá hiệu quả HTPL (UC132)** — màn hình SCR-IX-01 |
| `:483` | Mô tả — *"Báo cáo **điểm đánh giá hiệu quả HTPL trung bình có trọng số**, phân theo **đơn vị, đợt đánh giá, tiêu chí**"* |
| `:485` | **Tác nhân:** *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:493` | Input đặc thù (**duy nhất 1**) — `ke_hoach_danh_gia_id`, identifier, **không bắt buộc**, **`FK → KE_HOACH_DANH_GIA`** ⇒ bộ lọc đặc thù của màn này là **Đợt đánh giá** |
| `:495` | Công thức — *"Tính điểm đánh giá trung bình (**có trọng số**) theo **đơn vị, đợt, trong kỳ**"* ⇒ báo cáo **theo kỳ**, không phải snapshot |
| `:497` | Dimensions — *"**Kỳ, Đơn vị, Đợt đánh giá, Tiêu chí (trọng số)**"* |
| `:503`–`:507` | Output đặc thù, **điều kiện hiển thị "Luôn"**: `diem_trung_binh` (Điểm TB tổng) · `so_vu_viec_danh_gia` (Tổng VV được đánh giá) · `theo_don_vi[]` {don_vi, ten, diem_tb, so_vv} · `theo_tieu_chi[]` {tieu_chi, ten, trong_so, diem_tb} · `theo_dot[]` {dot_id, ten_dot, diem_tb} |
| `:510` | AC bổ sung — *"**Given** CB chọn kỳ Năm **When** tạo BC **Then** hiển thị điểm TB, phân theo **đơn vị + tiêu chí**"* |
| `:511` | AC bổ sung — *"**Given** CB **chọn đợt cụ thể** **When** filter **Then** hiển thị **chi tiết đợt đánh giá đó**"* ⇒ bộ lọc *Đợt đánh giá* **phải có tác dụng thật** |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: **Sau khi đã 'Xem báo cáo'**"* (không kèm điều kiện vai trò) |
| `:1053` | SCR-IX-01 item 9 — *"Nút Xuất PDF · 'Xuất PDF (.pdf)' · **click → auto-download** · Điều kiện hiển thị: Sau khi đã 'Xem báo cáo'"* |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1072` | Mapping dropdown — **UC132 *BC Đánh giá hiệu quả HTPL*, bộ lọc đặc thù = *Đợt đánh giá*** (chỉ 1), biểu đồ *Bar + Radar*. (So sánh: `:1071` UC131 có tới 3 bộ lọc) |
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
đặc tả **tự mâu thuẫn** (`:62`/`:485` liệt kê tác nhân CB Nghiệp vụ / CB Phê duyệt ↔ `:1268` ghi ngoại lệ
*"QTHT bypass"* áp *"Toàn bộ FR-IX"*). Câu hỏi này **đã có mục sẵn** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§Mục 2 (mở lúc 12:40 khi verify `SLCTHT_06`, cùng nguyên nhân gốc) ⇒ **không mở mục trùng**. Mục đó **không
kéo verdict** của case: dù BA chốt hướng nào, hành vi hiện tại vẫn phải thoả `:117`.

**IM LẶNG về:**
- **Chữ chính xác của thông báo thành công** khi xuất được — `:1058` mô tả *"Xuất thành công"* ở bảng thành
  phần màn hình, nhưng bảng Error Handling **không** có mã INF/WRN tương ứng ⇒ không chấm Fail vì chữ khác.
- **Có bắt buộc hiện toast *"Đang tạo file…"* hay không** — cùng lý do trên.
- **Bố cục bên trong tệp**: tên sheet, thứ tự cột, cách trình bày bảng. Đặc tả chỉ quy định **header file**
  phải có tiêu đề BC + kỳ + đơn vị + ngày tạo (`:1092`).
- **Có bao nhiêu thẻ số liệu phải vẽ trên màn, và tên các thẻ đó.** `:503`–`:507` quy định **output của báo
  cáo**, không quy định màn hình phải vẽ đủ mấy thẻ hay đặt nhãn gì. Đặc biệt: thẻ *"Tổng đợt đánh giá"* và
  *"Tổng lượt đánh giá"* mà đối tác chụp **không** nằm trong danh sách `:503`–`:507`; ngược lại
  `so_vu_viec_danh_gia` chỉ hiện ở vòng 2 chứ không hiện ở vòng 1 ⇒ **không chấm Fail** vì số thẻ hay nhãn thẻ.
- **Ý nghĩa của việc điểm trung bình có thể trùng nhau giữa các cấu hình lọc** — `:495` không quy định điểm
  TB phải khác nhau khi đổi bộ lọc; chỉ `:511` đòi lọc đợt phải **hiển thị chi tiết đợt đó**.
- **Trọng số cụ thể của từng tiêu chí** và **công thức làm tròn** điểm TB — đặc tả không nêu con số.

---

## 3. Precondition

- **Tài khoản ra verdict cho vế a + vế c:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương**
  (`CB_NV_TW`), cấp **TW**, phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-09 (`:485`).
  Fallback (Rule 7, **cùng vai trò + cùng cấp**): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Tài khoản bắt buộc dùng cho vế b:** vai trò **Quản trị viên · QTHT**, đơn vị **BTP · TW** — **chính vai
  trò đối tác dùng ở CẢ HAI vòng** (đọc từ góc phải trên `DGHQHTPL_06.jpg` và `DGHQHTPL_06_v2.jpg`). Vế b là
  *"Forbidden"*, tức **triệu chứng phân quyền**; đo bằng vai trò khác thì không tái hiện được điều đối tác nêu.
  > **Vì sao không vướng quy tắc "tài khoản quản trị không ra verdict":** quy tắc đó chặn việc **quyền rộng
  > che lỗi phân quyền**. Ở đây chiều ngược lại — QTHT là vai trò **bị chặn**, dùng nó để **phơi** lỗi chứ
  > không che. Vế a và vế c vẫn ra verdict bằng `cbnv_tw_05`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**, Loại BC = **BC Đánh giá hiệu
  quả HTPL** (`loai=danh-gia-hieu-qua`). 🔴 **Không được nhầm sang *BC Số lượng CG/TVV*** (FR-IX-08, dòng 210)
  **cũng không nhầm sang màn nghiệp vụ *Đánh giá hiệu quả*** ở sidebar — kiểm bằng cả 3 chỗ: chuỗi trong URL ·
  chữ trong ô chọn *Loại báo cáo* · tiêu đề khối kết quả.
- **Dữ liệu tiền đề:** ≥1 **đợt đánh giá đã có lượt chấm** trong kỳ + phạm vi đơn vị được chọn (`:495` —
  điểm TB *"theo đơn vị, đợt, trong kỳ"*), và để đo được bộ lọc thì cần **≥2 đợt đánh giá khác nhau có dữ
  liệu**. Không có dữ liệu → đó là `INF-RPT-01` hợp lệ (`:113`), **phải đổi kỳ/đơn vị/đợt** để có dữ liệu rồi
  mới đo nút xuất. **Mọi cấu hình đều rỗng ⇒ GAP chưa đóng ⇒ verdict ô trống**, nêu rõ cần seed gì.
- **Bộ lọc neo theo đối tác — 2 cấu hình, phải phủ CẢ HAI:**
  - **Vòng 2:** Kỳ **Năm** · 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · **Đợt đánh giá để trống**.
  - **Vòng 1:** cùng kỳ, cùng đơn vị · **Đợt đánh giá = *TKM kiểm thử 2*** (hoặc một đợt khác có dữ liệu nếu
    env không có đợt tên đó — khai rõ đã đổi sang đợt nào và vì sao).
  - Thao tác cả hai: [Xem báo cáo] → [Xuất Excel].
- **Cache máy chủ:** trước khi kết luận *"không có dữ liệu"* hoặc *"bộ lọc không tác dụng"*, kiểm trường
  **"Thời điểm tạo"** / `ngayTaoBc` xem có nhảy theo từng lượt bấm không; nghi cache thì đổi `denNgay` 1 ngày
  để lấy khoá cache mới.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi `soObserverDangSong = 1`; **đếm thông báo theo mốc giờ khác nhau**, không theo số phần tử.
  > ⚠️ Bài học đã ghi ở `tieuchi/SLHDVM_06.md` §8 và `tieuchi/CGTVPL_06.md` §3: bộ bắt kiểu *"nghe node mới
  > được thêm"* **bỏ sót** chữ *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**. Phải đo bù bằng
  > cách lấy mẫu **nội dung** vùng thông báo theo thời gian (`innerText`, ~100 ms/lần) + ghi hình học
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
5. **Số liệu trong tệp khớp số liệu đang hiện trên màn.** So từng cặp, tối thiểu **2 chỉ số tổng điều kiện
   "Luôn"** của FR-IX-09 (`:503`, `:504`): **điểm trung bình** và **tổng số vụ việc được đánh giá**. Chỉ số
   nào màn không vẽ thẻ riêng thì lấy từ **phản hồi của chính lần chạy báo cáo đó**. Có bảng phân theo đơn vị
   (`:505`), theo tiêu chí (`:506`) hoặc theo đợt (`:507`) trong tệp thì các dòng phải **nhất quán** với chỉ
   số tổng: tổng số vụ việc cộng theo đơn vị = `so_vu_viec_danh_gia`, và điểm TB tổng phải **nằm trong khoảng
   [min, max]** của các điểm TB thành phần (đặc tả `:495` nói *trung bình có trọng số*, không cho phép suy ra
   phép cộng đơn thuần trên cột điểm).
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280`): với 4 dạng ở mục 5, số liệu trong tệp **đổi theo** và mỗi
   lần đều khớp số trên màn của **chính lần đó** — không phải luôn trả bản không lọc. Kiểm chéo bằng md5 các
   tệp: 2 dạng cho số trên màn khác nhau mà tệp giống hệt ⇒ vi phạm.
7. **Bộ lọc đặc thù *Đợt đánh giá* có tác dụng thật** (`:493` `ke_hoach_danh_gia_id`; `:511` đòi *"chọn đợt cụ
   thể → hiển thị chi tiết đợt đánh giá đó"*): chọn một đợt cụ thể thì **số trên màn** và **số máy chủ trả
   về** phải thu hẹp về đúng đợt đó, và **tham số giao diện gửi lên phải được máy chủ áp dụng**.
   Phép đo quyết định: so **số liệu trên màn** với **số liệu gọi thẳng máy chủ đúng tham số đó**; hai đường
   lệch nhau ⇒ bộ lọc không có tác dụng. **Loại trừ nhớ đệm bằng `ngayTaoBc`**: khoá bị máy chủ bỏ qua thì
   `ngayTaoBc` **không đổi** so với lượt không lọc.
   *(Đây là điều kiện của chính đặc tả `:511`, không phải suy từ lỗi của màn FR-IX-06/FR-IX-08.)*
8. **Tên tệp .xlsx đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (`:85`, `:123`, `:1092`, §H8
   `srs-v3.5.md:6716`) — lấy tên từ **nguồn người dùng thật thấy** (tệp rơi về máy, hoặc `content-disposition`
   của phản hồi). Đo đủ **4 điều kiện của khuôn**:
   - **8a.** Có đoạn thời gian `_YYYYMMDD_HHmm` ngay trước đuôi tệp: **8 chữ số ngày + `_` + 4 chữ số giờ-phút**,
     và **giá trị khớp thời điểm xuất** (không phải hằng số/ngày cũ). *Phần giờ-phút là bắt buộc.*
   - **8b.** Phần `{TenBaoCao}` chỉ gồm **chữ cái không dấu và chữ số**; **không** dấu gạch nối, **không**
     khoảng trắng, **không** dấu tiếng Việt, **không** dấu câu. Gạch dưới chỉ dùng để ngăn đoạn.
   - **8c.** Phần `{TenBaoCao}` **nhận ra được là tên của chính loại báo cáo này** — báo cáo **đánh giá hiệu
     quả HTPL**. 🔴 Tên tệp trỏ sang loại báo cáo khác (vd chuỗi mang nghĩa *số lượng CG/TVV*, *đào tạo*,
     *chi phí*, *vụ việc*) là **trượt**, vì `:85` đòi `{TenBaoCao}` là *tên loại báo cáo* của chính báo cáo
     được xuất. *(Cấm đòi đúng y hệt chuỗi `BaoCaoDanhGia` — đó là prescribe; một chuỗi dài hơn nhưng vẫn
     mang đúng nghĩa loại báo cáo này thì ĐẠT.)*
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
- Số liệu trong tệp **lệch** số trên màn ở bất kỳ chỉ số nào trong 2 chỉ số tổng bắt buộc, hoặc các dòng chi
  tiết **không nhất quán** với tổng theo điều 5.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc cho số trên màn khác nhau nhưng tệp giống hệt nhau).
- **Bộ lọc *Đợt đánh giá* không có tác dụng** (điều 7): chọn đợt mà số liệu không đổi trong khi gọi thẳng máy
  chủ với đúng giá trị đó **lại đổi** ⇒ bộ lọc hỏng.
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
- **Kỳ/đơn vị/đợt không có dữ liệu** → `INF-RPT-01` (`:113`) là hành vi **hợp lệ**, không phải lỗi xuất tệp.
- **Số thẻ trên màn khác giữa hai vòng của đối tác** (3 thẻ ở vòng 1 · 4 thẻ ở vòng 2), hoặc nhãn thẻ khác
  danh sách `:503`–`:507` — đặc tả quy định **output báo cáo**, không quy định số thẻ vẽ trên màn.
- **Số liệu trên màn khác số liệu đối tác chụp** (1/2/7 vòng 1 · 7/7/5/7 vòng 2) — khác env, khác thời điểm,
  dữ liệu QA đã đổi.
- **Điểm trung bình không đổi khi đổi bộ lọc** — chỉ là dấu hiệu cần kiểm thêm bằng `ngayTaoBc` và các chỉ số
  khác; **một mình nó** không đủ kết luận, vì các đợt có thể cùng điểm TB.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).
- **Câu hỏi "QTHT có được xuất hay không"** — điểm đặc tả tự mâu thuẫn, đã có mục BA sẵn, không kéo verdict.

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — cả 10 điều
> đều đếm được / so được / nhìn thấy được, không có chữ *"hiển thị đúng"* hay *"hợp lý"*.

---

## 5. Dạng dữ liệu phải phủ — **M = 4**

**Nguồn xác định M** (tra theo đúng thứ tự của flow, dừng khi đủ):
① **đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo**: `:495` *"Tính điểm đánh giá trung bình (có trọng
số) theo đơn vị, đợt, trong kỳ"* ⇒ chỉ **một** nguồn bản ghi, chưa đủ chia dạng.
② **bộ lọc + giá trị ngay trên màn**: `:493` `ke_hoach_danh_gia_id` (FK → KE_HOACH_DANH_GIA) — và `:1072`
xác nhận bộ lọc đặc thù của **UC132 chỉ có *Đợt đánh giá***; cộng thêm 2 chiều của input chung có mặt trên
màn là **Kỳ** (`:69`) và **Đơn vị** (`:72`), đều nằm trong Dimensions `:497`.
**Dừng ở ②** — đây là các chiều đổi được nội dung tệp xuất, và `:1280` buộc *"file xuất theo bộ lọc hiện
tại"* nên mỗi chiều phải có ít nhất một lượt đo.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc đợt** (Đợt đánh giá trống, Đơn vị Toàn quốc, Kỳ Năm 2026) | Đúng điều kiện **vòng 2 của đối tác** (`DGHQHTPL_06_v2.jpg`) — nhánh sinh ra *"Forbidden"* |
| 2 | **Lọc Đợt đánh giá = đợt A có dữ liệu** (đối tác dùng *TKM kiểm thử 2* ở vòng 1) | Chiều lọc `:493` + **đúng câu AC `:511`**; **đúng điều kiện vòng 1 của đối tác** (`DGHQHTPL_06.jpg`), nhánh sinh ra *"Không thể tạo file xuất"* |
| 3 | **Lọc Đợt đánh giá = đợt B khác** | Nhánh thứ hai của cùng chiều — cần để phân biệt *"bộ lọc có tác dụng"* với *"máy chủ luôn trả cùng một tập"*. Hai đợt phải cho 2 kết quả khác nhau (hoặc chứng minh được vì sao giống) |
| 4 | **Thu hẹp Đơn vị = 1 đơn vị cụ thể** (đợt để trống) | Chiều **Đơn vị** của Dimensions `:497` + `:72`; kiểm `:1280` trên một chiều **độc lập** với bộ lọc đặc thù, để nếu chiều đợt hỏng thì vẫn còn đường chứng minh tệp bám bộ lọc |

Kỳ báo cáo giữ cố định **Năm 2026** (01/01/2026 → 31/12/2026) cho cả 4 dạng — đúng kỳ đối tác dùng ở cả hai
vòng. Đơn vị giữ **Toàn quốc** cho dạng 1–3 (trùng cả hai vòng của đối tác); riêng dạng 4 đổi đơn vị.

> ⚠️ **Nếu một nhánh không có dữ liệu** (vd env chỉ có 1 đợt đánh giá, hoặc đơn vị chọn không có lượt chấm):
> vẫn chạy dạng đó, ghi rõ màn trả `INF-RPT-01` và **không** chấm Fail vì thiếu dữ liệu (`:113`); nhưng phải
> khai trong mục 6 rằng dạng đó **không** dùng để chứng minh điều 6/7, và phải chứng minh bằng dạng còn lại.
> Đợt *TKM kiểm thử 2* không tồn tại trên env thì **đổi sang đợt khác có dữ liệu** và khai rõ đã đổi sang gì.

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 15:05). 2 cột sau điền sau khi đo xong.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Cả 2 vòng:** *Quản trị viên · QTHT*, đơn vị **BTP · TW** (đọc góc phải trên cả `DGHQHTPL_06.jpg` và `DGHQHTPL_06_v2.jpg`) | **Phủ CẢ HAI vai trò, hai ngữ cảnh trình duyệt tách biệt.** ① `cbnv_tw_05` — `/auth/me` trả `hoTen "CB Nghiệp vụ - Trung ương #05"` · `vaiTro ["CB_NV_TW"]` · `capDonVi "TW"` · `donViId …0001` (đúng tác nhân đặc tả `:485`; **không** dùng fallback Rule 7). ② tài khoản quản trị `admin` — `/auth/me` trả `hoTen "Quản trị hệ thống"` · `vaiTro ["QTHT"]` · `capDonVi "TW"` · **`donViId …0001` TRÙNG đơn vị với ①** ⇒ đúng *Quản trị viên · QTHT · BTP·TW* của đối tác, và khác ① **chỉ ở vai trò** | **Không** |
| Entity + trạng thái | **Vòng 1:** BC *Đánh giá hiệu quả HTPL* đã render có dữ liệu (Tổng đợt **1** · Tổng lượt **2** · Điểm TB **7**), *Thời điểm tạo 16/07/2026 14:25*. **Vòng 2:** đã render (Tổng đợt **7** · Tổng lượt **7** · Tổng VV đã ĐG **5** · Điểm TB **7**), *Thời điểm tạo 31/07/2026 14:59*. Cả 2 vòng nút [Xuất Excel]/[Xuất PDF] đều bấm được | **Cùng trạng thái: báo cáo đã chạy xong, có dữ liệu, nút xuất bật.** Vai trò ①: dạng 1 hiện **4 đợt · 8 lượt · 7 VV · điểm TB 33**, *Thời điểm tạo 06/08/2026 15:13*. Vai trò ② (QTHT): GET `danh-gia-hieu-qua` → **200**, màn render đủ **4 · 8 · 7 · 33**, *Thời điểm tạo 06/08/2026 15:31*, **cả 2 nút xuất hiện và bật** (`disabled=false`) — ảnh `…-06-…`. ⇒ tái hiện đúng tình huống đối tác: **xem được, bấm xuất được, chỉ chết ở bước xuất** | **Không** |
| Dữ liệu tiền đề | Có đợt đánh giá đã chấm trong kỳ Năm 2026, phạm vi Toàn quốc: vòng 1 lọc 1 đợt ra 2 lượt chấm; vòng 2 không lọc ra 7 đợt / 7 lượt / 5 vụ việc | **Đủ, không phải seed.** Kỳ Năm 2026 · Toàn quốc có **4 đợt / 8 lượt / 7 vụ việc** đã chấm, trải **3 đơn vị** (Bộ KH&ĐT · Cục Bổ trợ tư pháp · Sở TP Hà Nội) ⇒ đủ để đo **2 đợt khác nhau đều có dữ liệu** (điều kiện của dạng 2 và 3) và **1 đơn vị thu hẹp** (dạng 4). Không lượt nào rơi vào `INF-RPT-01`. **Không seed, không sửa, không xoá bất kỳ dữ liệu nào** | **Không** |
| Input / filter / giá trị nhập | **Vòng 1:** Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Toàn quốc**, **Đợt đánh giá = *TKM kiểm thử 2***; URL có `fd_dotDanhGiaId=c4c16832-f885-4fd1-8a96-969ece726…`. **Vòng 2:** cùng kỳ, cùng đơn vị, **Đợt đánh giá trống** (URL không có `fd_dotDanhGiaId`). Thao tác cả 2 vòng: [Xem báo cáo] → [**Xuất Excel**] | **Giữ nguyên kỳ + đơn vị của đối tác, phủ cả 2 cấu hình bộ lọc của họ.** Kỳ **Năm** 01/01→31/12/2026 ở cả 4 dạng. Dạng 1 = **đúng vòng 2** (Toàn quốc, đợt trống). Dạng 2 = **đúng kiểu vòng 1** (Toàn quốc, có chọn đợt) — env **không có** đợt tên *TKM kiểm thử 2*, đã **đổi sang *"Đợt đánh giá seed 2026"*** và khai ở đây. Dạng 3 = đợt thứ hai *"QA-THDG05-partial-save-te…"*. Dạng 4 = Đơn vị **Sở Tư pháp Hà Nội (STP-HN)**, đợt trống. Thao tác: [Xem báo cáo] → [Xuất Excel] (+ [Xuất PDF] ở dạng 4) | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 2 lượt xuất (1 mỗi vòng). M = **2** dạng (không lọc đợt · lọc 1 đợt). Không thấy đối tác thử đổi đơn vị, cũng không thấy thử [Xuất PDF] | **N = 21 lượt xuất · M = 4 dạng (≥ 2 của đối tác).** Vai trò ①: 4 dạng × [Xuất Excel] + 1 lượt **xuất lại dạng 4** (phép thử chống đè) + 1 lượt [**Xuất PDF**] + 2 lượt gọi thẳng máy chủ (không lọc · có lọc đợt) = **8 lượt, 8/8 ra tệp**. Vai trò ② (QTHT): **11 lượt bấm chuột (8 Excel + 3 PDF) + 2 lượt gọi thẳng = 13/13 lỗi 403**, 0 tệp. **Đã phủ thêm phần đối tác BỎ TRỐNG:** chiều **Đơn vị**, đợt **thứ hai**, và nút [**Xuất PDF**] | **Không** |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** vòng 1 `htpldn-uat.ospgroup.vn/bao-cao?loai=danh-gia-hieu-qua&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&fd_dotDanhGiaId=c4c16832-f885-4fd1-8a96-969ece726…`
  · vòng 2 `htpldn-uat.ospgroup.vn/bao-cao?loai=danh-gia-hieu-qua&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu — vòng 1 *Thời điểm tạo* **16/07/2026 14:25**,
  **1 đợt / 2 lượt / điểm TB 7**; vòng 2 *Thời điểm tạo* **31/07/2026 14:59**, **7 đợt / 7 lượt / 5 VV /
  điểm TB 7**.
- **Vai trò + env + bản dựng:** **Quản trị viên QTHT** (BTP · TW) · env `htpldn-uat.ospgroup.vn` ·
  nhãn **HTPLDN · V1.0** (vòng 1, đồng hồ 16/07/2026 14:25) → **V1.0.3** (vòng 2, đồng hồ 31/07/2026 15:00).

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn (V1.0 / V1.0.3 → bản đang đo).
⇒ Mọi kết luận *hết lỗi* chỉ là **tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

---

## 7. Kết quả chấm

# 🔁 REOPEN — còn lỗi, chuyển lại dev

**Một câu:** Hai vế *không tạo được tệp* và *tên tệp* đã hết lỗi trên bản dựng này, nhưng vế **"Forbidden"**
tái hiện **nguyên vẹn 13/13 lượt** với **đúng vai trò đối tác dùng** (Quản trị viên · QTHT · BTP·TW): người
dùng xem được báo cáo, cả hai nút xuất đều bật, bấm xuất thì nhận **chuỗi tiếng Anh thô "Forbidden"** và
**không có tệp nào về máy** — lệch dòng `:117` (đòi câu tiếng Việt *"Bạn không có quyền xem báo cáo này"*).

### 7.1 Chấm theo TỪNG VẾ đối tác nêu

| Vế | Đối tác gặp | Mình đo được | Kết |
|---|---|---|:-:|
| **a** — *"Không thể tạo file xuất. Vui lòng thử lại."* | vòng 1, 16/07, vai trò QTHT | **Không tái hiện** ở vai trò đặc tả `cbnv_tw_05`: **8/8 lượt** ra tệp thật. Chữ trên màn mọi lượt: *"Đang tạo file..."* → *"Tạo file thành công."*, **không** có chữ nào mang nghĩa `:116`. Ở vai trò QTHT thì lỗi hiện tại **không phải** `:116` mà là nhánh quyền (403) ⇒ câu *"Không thể tạo file xuất"* đã hết | ✅ |
| **b** — *"Forbidden"* | vòng 2, 31/07, vai trò QTHT | **TÁI HIỆN NGUYÊN VẸN.** Vai trò QTHT: 11 lượt bấm chuột (8 Excel + 3 PDF) + 2 lượt gọi thẳng = **13/13** đều `403`, thân trả về `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden",…}}`; chữ **nhìn thấy trên màn** đúng là `Forbidden` (khung sống ~3,3 s); **0 tệp** về máy | ❌ |
| **c** — tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}` | ô *Kết quả mong đợi* | **Đúng khuôn, đủ 8a–8d.** `BaoCaoDanhGiaHieuQua_20260806_1514.xlsx` — lấy từ **2 nguồn người dùng thật thấy**: tệp rơi về máy **và** `content-disposition` của chính phản hồi (md5 hai nguồn TRÙNG nhau). Chống đè đạt (15:23 vs 15:25 → 2 tên khác nhau). Khuôn cũ 03/08 `bao-cao-<slug>-YYYY-MM-DD.xlsx` (gạch nối, thiếu giờ-phút) **đã được sửa**. Tên thực **dài hơn** chuỗi đối tác viết (`BaoCaoDanhGia`) nhưng vẫn là **tên đúng loại báo cáo này** ⇒ theo điều 8c là ĐẠT, cấm đòi đúng y hệt chuỗi | ✅ |

> **Verdict do vế b quyết.** Flow §Verdict: *fix một phần → Reopen*. Hai vế a/c sạch **không** cứu được case
> khi vế b còn nguyên.

### 7.2 Chấm 10 điều của mục 4

| # | Điều kiện | Đo được | Kết |
|:-:|---|---|:-:|
| 1 | Không báo lỗi tạo tệp / không bị chặn quyền (vai trò đặc tả) | `cbnv_tw_05`, 4/4 dạng: 1 request · chữ *"Đang tạo file..."* → *"Tạo file thành công."* | ✅ |
| 2 | Người dùng thật sự nhận được tệp | 6/6 lượt bấm chuột có tệp về máy; 2 lượt gọi thẳng có `content-disposition: attachment` | ✅ |
| 3 | Mở được như workbook thật | `openpyxl.load_workbook()` mở được cả 5 tệp `.xlsx`, sheet *"BC Đánh giá hiệu quả"*, có ô không rỗng | ✅ |
| 4 | Header đủ 4 thông tin `:1092` | Mọi tệp có ① *"BC Đánh giá hiệu quả HTPL"* ② *"Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)"* ③ *"Đơn vị: Toàn quốc"* (dạng 4 đổi đúng thành *"Đơn vị: Sở Tư pháp Hà Nội"*) ④ *"Ngày tạo: 06/08/2026"* | ✅ |
| 5 | Số liệu trong tệp khớp màn + cộng khớp | Dạng 1: tệp 4 đợt / 8 lượt / **7 VV** / **33.9** = màn 4 · 8 · 7; cộng *Theo đơn vị*: lượt 1+4+3 = 8 ✓, vụ việc 1+4+2 = 7 ✓, điểm TB tổng 33.9 ∈ [25.53 , 80] ✓. Dạng 2 tệp 1/3/3/76.67 = màn; (90+80+60)/3 = 76.67 ✓. Dạng 3 tệp 1/3/3/8.2 = màn. Dạng 4 tệp 2/3/2/25.53 = màn | ✅ |
| 6 | Tệp phản ánh bộ lọc hiện tại (`:1280`) | 4 dạng → **4 md5 khác nhau** (7.358 / 7.018 / 7.128 / 7.166 B), mỗi tệp khớp màn của **chính lần đó**; header ③ đổi theo đơn vị. Gọi thẳng máy chủ: không lọc 7.358 B · lọc đợt 7.018 B (đúng bằng dạng 2). Không có cặp "màn khác số mà tệp giống hệt" | ✅ |
| 7 | **Bộ lọc đặc thù *Đợt đánh giá* có tác dụng thật** (`:493` + `:511`) | **ĐẠT.** Dạng 2 và dạng 3 cùng chiều lọc cho **hai kết quả khác hẳn** (76.67 / 3 đơn vị ↔ 8.2 / 1 đơn vị). Đường thứ hai khớp: màn ↔ máy chủ trùng số ở cả 2 dạng. Loại trừ nhớ đệm bằng `ngayTaoBc`: khoá `dotDanhGiaId` sinh mốc **MỚI** `08:37:40.679Z`, còn `fd_dotDanhGiaId` / `keHoachDanhGiaId` / `ke_hoach_danh_gia_id` **dùng chung mốc** `08:37:40.580Z` với lượt không lọc ⇒ bị bỏ qua. Giao diện gửi đúng khoá máy chủ nhận (`dotDanhGiaId`), cả ở lượt XEM lẫn trong `filterDacThu` của lượt XUẤT ⇒ **không** dính lỗi lệch tên khoá | ✅ |
| 8 | Tên tệp `.xlsx` đúng khuôn (8a–8d + chống đè) | 8a ✓ (7 tệp, 6 mốc giờ-phút khác nhau, khớp giờ xuất thật) · 8b ✓ (chỉ chữ không dấu + số) · 8c ✓ (*DanhGiaHieuQua* = đúng loại báo cáo này) · 8d ✓ (`.xlsx`, 40 ký tự) · chống đè ✓ (15:23 vs 15:25) | ✅ |
| 9 | Nút [Xuất PDF] — nhận tệp + tên đúng cùng khuôn | `BaoCaoDanhGiaHieuQua_20260806_1524.pdf` (34.996 B, `%PDF`, khổ A4). Ghi nhận: nút mở hộp thoại *"Tùy chọn in báo cáo PDF"* trước, không tải ngay — **không chấm** (ngoài vế đối tác nêu, đặc tả im lặng) | ✅ |
| 10 | **Vai trò QTHT: nhận tệp HOẶC bị từ chối kèm thông báo tiếng Việt** (`:117`) | **Trượt cả hai nhánh.** Không nhận tệp (0/13 lượt), và chữ hiện ra là chuỗi tiếng Anh thô **`Forbidden`** — không phải câu tiếng Việt cho người dùng biết họ không có quyền | ❌ |

**⇒ Trượt duy nhất điều 10, mà điều 10 chính là vế b đối tác nêu ⇒ REOPEN.**

### 7.3 Vì sao chắc chắn là lỗi phân quyền, không phải đường xuất tệp hỏng

Phép đối chứng đổi **đúng một biến**: cùng đường dẫn `POST /api/v1/bao-cao/export`, **cùng thân yêu cầu từng
chữ**, cùng `donViId …0001`, cùng phiên đo — chỉ khác vai trò:

| Vai trò | Mã | Header trả về | Kết quả cho người dùng |
|---|:-:|---|---|
| `CB_NV_TW` (`cbnv_tw_05`) | **200** | `content-disposition: attachment; filename="BaoCaoDanhGiaHieuQua_20260806_1539.xlsx"` | nhận tệp 7.358 B |
| `QTHT` (`admin`) | **403** | *(không có `content-disposition`)* | `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}` — 0 tệp |

Và ở chính phiên QTHT, bước **XEM** báo cáo lại **200** với dữ liệu đầy đủ (4 · 8 · 7 · 33) — tức hệ thống cho
vai trò này **vào tận nơi, thấy hết số liệu, bật cả hai nút xuất**, rồi mới chặn ở cú bấm cuối bằng một chuỗi
tiếng Anh. Đây đúng là hình ảnh đối tác chụp ở vòng 2. Nhánh **PDF** cũng vậy: hộp thoại *"Tùy chọn in báo
cáo PDF"* mở bình thường, bấm [Xuất file] mới nhận `Forbidden`.

**Không kết luận** QTHT *nên* hay *không nên* được xuất — đó là chỗ đặc tả tự mâu thuẫn (`:62`/`:485` ↔
`:1268` *"QTHT bypass"* áp *"Toàn bộ FR-IX"*), đã có mục hỏi BA sẵn ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§Mục 2. **Dù BA chốt hướng nào**, hành vi hiện tại vẫn lệch `:117`: chặn thì phải nói bằng tiếng Việt cho
người dùng hiểu, không phải ném mã kỹ thuật.

### 7.4 Quan sát NGOÀI vế đối tác nêu — **không kéo verdict của case**

> Theo flow §Ca biên: *"Phát hiện mới nằm trong đúng màn/cột đang tranh chấp nhưng đối tác KHÔNG nêu →
> verdict của case chỉ do các vế đối tác nêu quyết định."* Verdict trên đã là REOPEN vì vế b, nên phần này
> **không** làm đổi kết quả — ghi lại để phiên chính xử. **Không mở dòng bug mới trên bảng.**

**(a) Thiếu nhóm output `theo_dot[]` điều kiện "Luôn" (`:507`).** Phản hồi của màn này trả các khoá
`["tenBaoCao","ngayTaoBc","tuNgay","denNgay","tongDotDanhGia","tongLuotDanhGia","soVuViecDanhGia",
"diemTrungBinhChung","theoDonVi","theoTieuChi","chartTypes"]` — **không có** `theoDot`; tệp xuất cũng chỉ có
bảng *Theo đơn vị* và *Theo tiêu chí*, **không có** bảng *Theo đợt*. Đối tác không nêu vế này.

**(b) Thẻ "Điểm trung bình chung" trên màn cắt phần thập phân.** 33.9 → hiện `33`; 76.67 → `76`; 8.2 → `8`;
25.53 → `25`. Bảng *Theo đơn vị* trên màn thì làm tròn 1 chữ số (80,0 · 28,7 · 25,5), còn tệp giữ đủ
(80 · 28.65 · 25.53). Mục 4 đã ghi trước là **không chấm Fail** vì đặc tả im lặng về công thức làm tròn.

**Trả lời câu phiên chính hỏi (lỗi lệch tên khoá bộ lọc *Lĩnh vực* có lan tới màn này không):**
**KHÔNG.** Màn FR-IX-09 **không có** bộ lọc *Lĩnh vực*; bộ lọc đặc thù duy nhất là *Đợt đánh giá* (`:1072`),
và nó **chạy đúng** — giao diện gửi `dotDanhGiaId`, máy chủ nhận đúng khoá đó (bảng đo ở điều 7 và
`image/DGHQHTPL_06-09-…txt` §PHẦN 5). Tên `ke_hoach_danh_gia_id` viết trong `:493` chỉ là tên khái niệm,
không phải tên khoá trên đường truyền ⇒ **không** phải lỗi.

### 7.5 Bằng chứng

| Tệp | Chú thích |
|---|---|
| `image/DGHQHTPL_06-01-dang1-khong-loc-dot-man-hinh-truoc-khi-xuat-V108.png` | Dạng 1 — vai trò `cbnv_tw_05`, Toàn quốc, đợt để trống (**đúng cấu hình vòng 2 của đối tác**): màn hiện 4 đợt · 8 lượt · 7 vụ việc · điểm TB 33, *Thời điểm tạo 06/08/2026 15:13*, trước khi bấm [Xuất Excel] |
| `image/DGHQHTPL_06-02-dang2-loc-DotDanhGia-seed2026-man-hinh-truoc-khi-xuat-V108.png` | Dạng 2 — lọc **Đợt đánh giá = *Đợt đánh giá seed 2026*** (thay cho *TKM kiểm thử 2* không có trên env): số đổi thành 1 · 3 · 3 · 76 ⇒ bộ lọc đợt có tác dụng |
| `image/DGHQHTPL_06-03-dang3-loc-DotDanhGia-THDG05-so-lieu-doi-V108.png` | Dạng 3 — lọc **đợt thứ hai *QA-THDG05-partial-save-te…***: 1 · 3 · 3 · **8** — khác hẳn dạng 2 ⇒ máy chủ không trả cùng một tập, đúng AC `:511` |
| `image/DGHQHTPL_06-04-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png` | Dạng 4 — thu hẹp **Đơn vị = Sở Tư pháp Hà Nội (STP-HN)**, đợt để trống: 2 · 3 · 2 · 25; header tệp đổi đúng thành *"Đơn vị: Sở Tư pháp Hà Nội"* |
| `image/DGHQHTPL_06-05-hop-thoai-tuy-chon-in-PDF-V108.png` | Nút [Xuất PDF] mở hộp thoại *"Tùy chọn in báo cáo PDF"* (A4/A3/Letter · Dọc/Ngang · [Hủy] [Xuất file]) trước khi tải — ghi nhận bẫy thao tác, không chấm |
| `image/DGHQHTPL_06-06-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png` | Vai trò **Quản trị viên · QTHT · BTP·TW** XEM được báo cáo (4 · 8 · 7 · 33, *Thời điểm tạo 15:31*), cả hai nút xuất hiện và bật |
| `image/DGHQHTPL_06-07-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png` | Vai trò QTHT bấm [Xuất Excel] → khung thông báo **đỏ chữ "Forbidden"** ở đỉnh màn, báo cáo vẫn hiện 4 · 8 · 7 · 33, không tệp nào về máy — tái hiện đúng ảnh vòng 2 của đối tác |
| `image/DGHQHTPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png` | Nhánh **[Xuất PDF]** của cùng vai trò QTHT: hộp thoại mở bình thường, bấm [Xuất file] → cũng **"Forbidden"** ⇒ lỗi không riêng nhánh Excel |
| `image/DGHQHTPL_06-09-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt` | Nguyên văn chữ trên màn từng lượt (kèm mốc thời gian, chứng minh khung sống ~3,3 s) · thân + header phản hồi máy chủ (kể cả `403`) · nội dung 5 tệp `.xlsx` đọc bằng `openpyxl` · md5 · phép thử chống đè · bảng đo bộ lọc + `ngayTaoBc` |
| `testfiles/DGHQHTPL_06-*.xlsx` · `DGHQHTPL_06-pdf-*.pdf` | 5 tệp Excel + 1 tệp PDF thật do bản dựng này xuất ra, giữ nguyên tên gốc để soi khuôn tên tệp |

### 7.6 Không đo được / giới hạn hiệu lực

- **Env khác env nghiệm thu.** Đo trên `18.143.165.120.nip.io` (env kiểm thử nội bộ); đối tác chụp trên
  `htpldn-uat.ospgroup.vn`. Kết luận *hết lỗi* của vế a và vế c chỉ có hiệu lực **khi bản dựng này lên môi
  trường nghiệm thu**.
- **Bản dựng:** đo 2 lần trong phiên (15:06 và 15:36) — **giống nhau**, nên trong phiên này không trôi. Nhưng
  môi trường **đã trôi trước đó** lúc 07:13 GMT mà nhãn ứng dụng không đổi ⇒ verdict chỉ có hiệu lực cho
  đúng bó mã `md5 3904131c…`.
- **Không đo** khổ giấy A4 / font Times New Roman cỡ 13 bên trong tệp, nội dung bên trong PDF, bố cục sheet —
  ngoài vế đối tác nêu, đã khai ở mục 4 §*"KHÔNG được chấm Fail vì"*.
- **Không đo được đúng đợt của đối tác** — env không có đợt tên *TKM kiểm thử 2*; đã đổi sang
  *"Đợt đánh giá seed 2026"* và khai ở mục 6. Điều này **không ảnh hưởng** verdict: vế b của đối tác nằm ở
  cấu hình **không lọc đợt** (vòng 2), đã đo đúng nguyên bản.
- **Không kết luận** QTHT có quyền xuất hay không — chỗ đặc tả tự mâu thuẫn, đã có mục BA sẵn.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 15:05** — viết mục 1–6 **TRƯỚC khi mở màn tranh chấp**. Đã đọc: bằng chứng đối tác (2 tệp,
  full-res), đặc tả (`srs-fr-11-bao-cao.md`, `srs-v3.5.md` §H8), dòng 214 tab `bug`, và hồ sơ QA nội bộ đã
  khai ở đầu file.
- **2026-08-06 15:36** — điền bản dựng **tự đo** vào khối đầu file. Đo **2 lần** (đầu phiên 15:06, cuối phiên
  15:36): `assets/index-DIABnbIr.js` · md5 `3904131cf562e0349890ac1bd058eb1f` · 1.123.565 B ·
  etag `W/"6a74340b-1124ed"` — **hai lần giống hệt** ⇒ bản dựng **không trôi thêm** trong phiên đo. Nhãn ứng
  dụng vẫn V1.0.8 dù môi trường đã dựng lại lúc 07:13 GMT ⇒ đã thêm cảnh báo "nhãn không dùng để nhận diện
  bản dựng".
- **2026-08-06 15:39 — làm rõ điều 8c, KHÔNG nới tiêu chí.** Lúc 15:05 mục 4 đã ghi sẵn: đo theo **khuôn**,
  cấm đòi đúng y hệt chuỗi `BaoCaoDanhGia` của đối tác. Đo ra tên thật là `BaoCaoDanhGiaHieuQua_…` — **dài
  hơn** chuỗi đối tác viết nhưng vẫn là tên của **chính loại báo cáo này**. Chấm **ĐẠT** theo đúng câu chữ đã
  viết trước khi đo; **không** sửa lại 8c cho khớp kết quả. Ghi rõ ở §7.1 để người đọc tự kiểm.
- **2026-08-06 15:39 — điều 7 (bộ lọc *Đợt đánh giá*) ĐẠT, ghi lại cách loại trừ nhớ đệm.** Phiên chính cảnh
  báo lỗi lệch tên khoá bộ lọc ở màn khác; mục 3 + mục 4 đã buộc phải **tự đo trên màn của mình**, không lấy
  kết quả màn khác. Kết quả: màn này **không dính** — nhưng cách đo thì vẫn giữ nguyên như đã cam kết
  (so màn ↔ máy chủ + loại trừ nhớ đệm bằng `ngayTaoBc`), và bảng đo đầy đủ được lưu ở
  `image/DGHQHTPL_06-09-…txt` §PHẦN 5 để dev/BA kiểm lại.
