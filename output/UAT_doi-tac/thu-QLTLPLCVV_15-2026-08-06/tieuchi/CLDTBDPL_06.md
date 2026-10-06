# Tiêu chí verify — CLDTBDPL_06

```
Mã case: CLDTBDPL_06 (tab `bug` dòng 218)      Thời điểm viết: 2026-08-06 15:58
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 16:02 → 16:19
Bản dựng (TỰ ĐO, 2 lần — 16:01 đầu phiên và 16:19 cuối phiên — KHÔNG chép từ case khác):
  index.html      etag W/"6a74340b-428"        last-modified Thu, 06 Aug 2026 07:13:15 GMT
  gói giao diện   assets/index-DIABnbIr.js     etag W/"6a74340b-1124ed"
                  md5 3904131cf562e0349890ac1bd058eb1f   ·   1.123.565 B
  nhãn trong ứng dụng: HTPLDN · V1.0.8
  ⇒ HAI LẦN ĐO GIỐNG HỆT NHAU ⇒ bản dựng KHÔNG trôi trong suốt phiên đo.
Verdict: 🔁 REOPEN — còn lỗi, chuyển lại dev (trượt điều 10, xem mục 7)
```

> ⚠️ **Cảnh báo trôi bản dựng do phiên chính báo — phải tự kiểm lại, không chép:** môi trường đã được dựng
> lại **1 lần giữa lô** (`index-CNwX9JjX.js` → `index-DIABnbIr.js`, md5 `3904131cf562e0349890ac1bd058eb1f`,
> `last-modified Thu, 06 Aug 2026 07:13:15 GMT`) **mà nhãn trong ứng dụng vẫn V1.0.8**. ⇒ **Nhãn ứng dụng
> KHÔNG dùng để nhận diện bản dựng.** Verdict chỉ có hiệu lực cho đúng bó mã ghi ở khối trên; đo ra giá trị
> khác giá trị phiên chính nêu ⇒ bản dựng lại trôi, phải ghi rõ như **giới hạn hiệu lực**.
>
> ✅ **Đã tự kiểm (16:01 và 16:19):** hai lần đo ra **đúng** bó mã phiên chính nêu (`index-DIABnbIr.js`,
> md5 `3904131cf562e0349890ac1bd058eb1f`, `last-modified 06/08/2026 07:13:15 GMT`) và **giống hệt nhau**
> ⇒ **không** có lần trôi nào nữa trong phiên đo của tôi. Verdict dưới đây có hiệu lực cho **đúng** bó mã này.

> **Khai báo hồ sơ QA nội bộ đã đọc TRƯỚC khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `tieuchi/DGHQHTPL_06.md` — file tiêu chí case **anh em** (màn *BC Đánh giá hiệu quả HTPL*, FR-IX-09).
>   Đọc để tham khảo **bố cục** + **bẫy thao tác**. 🔴 **Không chép kết luận** — khác màn
>   (`chat-luong-dao-tao` ≠ `danh-gia-hieu-qua`), khác bộ lọc đặc thù (màn tôi lọc **Khóa học** `:534`;
>   màn đó lọc *Đợt đánh giá* `:493`), khác bộ chỉ số đầu ra (`diem_trung_binh` / `ty_le_dat` /
>   `tong_hoc_vien` / `theo_khoa_hoc[]` / `theo_don_vi[]` — `:544`–`:548`, **không** có `theo_dot[]`), và
>   khác bản chất báo cáo (FR-IX-10 tính **tỷ lệ đạt** = số HV đạt điểm chuẩn / tổng HV, `:536`).
> - `bug-report.md` §Phần 3 (`BUG-SLHDVM-006`), §Phần 6 (`BUG-CLDTBDDDR-006`), §Phần 7 (`BUG-LDTBDDDR-006`),
>   §Phần 8 (`BUG-CGTVPL-006`), §Phần 9 (`BUG-DGHQHTPL-006`) — **5 phiếu cùng gốc 403 ở vai trò QTHT**.
>   ⇒ Case tôi **vẫn viết phiếu riêng**, dẫn chiếu 5 phiếu này, **không** mở dòng bug mới trên bảng.
> - `cau-hoi-BA.md` §Mục 2 — câu hỏi *"QTHT có được xuất báo cáo thống kê không"* **đã mở** lúc 12:40 khi
>   verify `SLCTHT_06`, đã có 5 blockquote bổ sung của các màn khác ⇒ **không mở mục hỏi mới**, cùng lắm
>   thêm 1 blockquote theo đúng khuôn đang dùng.
> - `B5-CONTEXT.md` §4 nhắc **số đo cũ 03/08/2026** (bản dựng V1.0.4, env đối tác): tệp xuất khi đó tên
>   `bao-cao-<slug>-YYYY-MM-DD.xlsx`, thiếu hẳn giờ-phút.
> - Phiên chính báo: bộ lọc đặc thù nhóm báo cáo này đang **lệch tên tham số giữa giao diện và máy chủ** —
>   FR-IX-06 gửi `linhVuc`, FR-IX-08 gửi `linhVucCm`, máy chủ nhận `linhVucId` ⇒ bị bỏ qua; FR-IX-07 và
>   FR-IX-09 không dính.
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ**, không lấy số đo cũ 03/08 làm ngưỡng, không lấy kết quả case anh em
> làm kết luận. Riêng thông tin lệch tên khoá bộ lọc chỉ dùng để **quyết định phải tự đo bộ lọc đặc thù của
> màn tôi** (*Khóa học*) — **không** dùng làm kết luận.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** — 2 vế triệu chứng (2 vòng nghiệm thu, cùng thao tác bấm **[Xuất Excel]** trên màn
*Báo cáo thống kê → **BC Chất lượng đào tạo***) + 1 vế kỳ vọng về tên tệp:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo
  **"Forbidden"** ⇒ vẫn không có tệp; triệu chứng đổi từ *lỗi tạo tệp* sang *bị chặn quyền*.
- **Vế c (ô `Kết quả mong đợi`)** — *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng.
  **Tên tệp xuất: `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx`**"*

🔴 **Vế c đo được, KHÔNG đẩy sang BA.** BA đã chốt **2026-08-04** khuôn tên tệp cho nhóm IX, đặc tả đã sửa
theo (dấu `[BA chốt 2026-08-04]` nằm ngay trong `:85`, `:86`, `:1092`); ngày **2026-08-06** khuôn được nâng
thành quy ước chung ở **Phụ lục E §H8** (`srs-v3.5.md:6716`). Đây là **áp quyết định có sẵn**, QA chấm được.

⚠️ **Đo theo KHUÔN, không đo theo chuỗi đối tác viết.** Đặc tả chỉ đòi `{TenBaoCao}` = **tên loại báo cáo của
chính báo cáo được xuất**, viết liền PascalCase, bỏ dấu, bỏ mọi ký tự không phải chữ/số. Với màn này chuỗi
`BaoCaoDaoTao` mà đối tác viết **có thể** là một cách rút gọn hợp lệ của *BC Chất lượng đào tạo* — nhưng
**cấm chấm Fail chỉ vì tên tệp không đúng y hệt chuỗi đó** (đó là prescribe), và **cấm chấm Pass** nếu tên tệp
mang tên **một loại báo cáo khác** (vd *đánh giá hiệu quả*, *CG/TVV*, *chi phí*, *vụ việc*).

### Bằng chứng — đã MỞ XEM full-res (2026-08-06 15:52 và 15:54)

| Vòng | Tệp | Thấy gì |
|---|---|---|
| **1** | `partner-evidence/CLDTBDPL_06.jpg` | **ĐÚNG case.** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=**chat-luong-dao-tao**&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (**không** có khoá lọc khóa học). Ô *Loại báo cáo* = ***BC Chất lượng đào tạo***; Kỳ **Năm**, Thời gian *Từ 01/01/2026 — Đến 31/12/2026*; Đơn vị **Toàn quốc**; bộ lọc đặc thù trên màn là ***Khóa học***, đang **để trống** (placeholder *"Chọn Khóa học"*). Báo cáo đã render, tiêu đề khối kết quả *BC Chất lượng đào tạo*, *Thời điểm tạo **16/07/2026 15:18***, **3 thẻ**: Tổng khóa học **3** · Điểm trung bình **7** · Tỷ lệ đạt **80.0 %**. Khung thông báo đỏ **"Không thể tạo file xuất. Vui lòng thử lại."** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0**. Đồng hồ máy: **03:18 PM 2026-07-16** |
| **2** | `partner-evidence/CLDTBDPL_06_v2.jpg` | **ĐÚNG case** (căn cứ **nội dung màn**, xem cảnh báo ngay dưới). Ô *Loại báo cáo* = ***BC Chất lượng đào tạo***; Kỳ **Năm** 01/01→31/12/2026; Đơn vị **Toàn quốc**; bộ lọc ***Khóa học*** **để trống**. Tiêu đề khối kết quả *BC Chất lượng đào tạo*, *Thời điểm tạo **31/07/2026 15:02***, **4 thẻ**: Tổng khóa học **5** · Tổng học viên **14** · Điểm trung bình **7** · Tỷ lệ đạt **58.0 %**. Khung thông báo đỏ **"Forbidden"** ở đỉnh màn. Góc phải trên: **BTP · TW · Quản trị viên · QTHT**. Sidebar: **HTPLDN · V1.0.3**. Đồng hồ máy: **03:03 PM 2026-07-31** |

🔴 **Lệch giữa URL và nội dung màn ở ảnh vòng 2 — ghi lại theo flow §Cổng bằng chứng.** Thanh địa chỉ của
`CLDTBDPL_06_v2.jpg` vẫn còn `loai=**danh-gia-hieu-qua**` (loại báo cáo của case `DGHQHTPL_06`, dòng 214),
trong khi **ô chọn *Loại báo cáo*, bộ lọc đặc thù *Khóa học*, tiêu đề khối kết quả và cả 4 thẻ số liệu** đều
là ***BC Chất lượng đào tạo***. Giải thích khớp nhất: đối tác chụp liền mạch nhiều case trong một phiên, đổi
loại báo cáo trong ô chọn rồi bấm [Xem báo cáo] nhưng **thanh địa chỉ chưa đồng bộ lại**. ⇒ **Vẫn nhận ảnh
này là bằng chứng của case CLDTBDPL_06** vì 4 dấu hiệu nội dung đều trỏ đúng màn, nhưng **khai rõ ở đây** và
**không** dùng URL của ảnh vòng 2 làm dữ kiện neo. *(Ảnh vòng 1 thì URL và nội dung khớp nhau hoàn toàn.)*

⚠️ **Hai vòng KHÔNG so sánh trực tiếp với nhau được:** **cùng vai trò** (QTHT · BTP·TW), **cùng loại báo
cáo**, **cùng kỳ + cùng đơn vị**, **cùng bộ lọc Khóa học để trống** — nhưng **khác bản dựng** (V1.0 →
V1.0.3), **khác số thẻ hiện trên màn** (3 thẻ → 4 thẻ, vòng 2 có thêm *Tổng học viên*) và **khác số liệu**
(3 khóa / 80.0 % → 5 khóa / 14 HV / 58.0 %).

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (+ Phụ lục E ở
`srs-v3.5.md`) — **đã mở file đọc đúng dòng 2026-08-06 15:55**, số dòng lấy bằng `grep -n` / `awk`, không lấy
từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `srs-fr-11-bao-cao.md:62` | Preconditions chung — *"User đã đăng nhập, có role **CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)**"* |
| `:69` | Input chung #1 — `ky_bao_cao`, **bắt buộc**, ràng buộc `TUAN / THANG / QUY / NAM / KHOANG` |
| `:72` | Input chung #4 — `don_vi_id`, **không bắt buộc**, *"Auto phân quyền nếu không truyền"* |
| `:79` | Processing chung bước 1 — *"**Kiểm tra quyền truy cập báo cáo** + phạm vi theo đơn vị"* (BR-AUTH-01) ⇒ kiểm quyền nằm **đầu luồng**, trước cả bước truy vấn và bước xuất |
| `:82` | Bước 4 — *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"* |
| `:85` | Bước 7 — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). **Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo"* `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` |
| `:86` | Bước 8 — PDF theo TT17/2025; *"Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` theo Phụ lục E §H8"* `[BA chốt 2026-08-04]` — *"`{TenBaoCao}` là tên loại báo cáo **viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số**"* |
| `:113` | E3 · Không có dữ liệu · **INF-RPT-01** · *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* · INFO |
| `:116` | E6 · Lỗi xuất file · **ERR-RPT-04** · *"Không thể tạo file xuất. Vui lòng thử lại"* · ERROR ⇒ **đúng câu vế a** |
| `:117` | E7 · Không có quyền · **ERR-RPT-05** · *"Bạn không có quyền xem báo cáo này"* · ERROR ⇒ nhánh quyền của **vế b** |
| `:123` | AC chung — *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (Phụ lục E §H8)"* |
| `:124` | AC chung — *"**Given** CB nhấn 'Xuất PDF' … **tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`** (Phụ lục E §H8)"* |
| `:515` | **FR-IX-10: BC Chất lượng đào tạo (UC133)** — màn hình SCR-IX-01 |
| `:524` | Mô tả — *"Báo cáo chất lượng đào tạo: **điểm TB kiểm tra, tỷ lệ đạt**, phân theo **khóa học, đơn vị**"* |
| `:526` | **Tác nhân:** *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:534` | Input đặc thù (**duy nhất 1**) — `khoa_hoc_id`, identifier, **không bắt buộc**, **`FK → KHOA_HOC`** ⇒ bộ lọc đặc thù của màn này là **Khóa học** |
| `:536` | Công thức — *"Tính điểm TB kiểm tra, **tỷ lệ đạt (số đạt điểm chuẩn / tổng)** theo khóa học, đơn vị **trong kỳ**"* ⇒ báo cáo **theo kỳ** |
| `:538` | Dimensions — *"**Kỳ, Đơn vị, Khóa học, Tỷ lệ đạt**"* |
| `:544`–`:548` | Output đặc thù, **điều kiện hiển thị "Luôn"** (cả 5): `diem_trung_binh` (Điểm TB kiểm tra) · `ty_le_dat` (% HV đạt) · `tong_hoc_vien` (Tổng HV tham gia) · `theo_khoa_hoc[]` {khoa_hoc, ten_kh, diem_tb, ty_le_dat, so_hv} · `theo_don_vi[]` {don_vi, ten, diem_tb, ty_le_dat} |
| `:551` | AC bổ sung — *"**Given** CB chọn kỳ Quý **When** tạo BC **Then** hiển thị **điểm TB + tỷ lệ đạt**, phân theo **KH + đơn vị**"* |
| `:552` | AC bổ sung — *"**Given** CB **chọn KH cụ thể** **When** filter **Then** hiển thị **chi tiết KH đó**"* ⇒ bộ lọc *Khóa học* **phải có tác dụng thật** |
| `:1050` | SCR-IX-01 item 6 — *"Bộ lọc đặc thù · select/text-input (dynamic) · Tùy loại BC: … **khóa học** … · change → filter · Khi loại BC cần lọc đặc thù"* |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: **Sau khi đã 'Xem báo cáo'**"* (không kèm điều kiện vai trò) |
| `:1053` | SCR-IX-01 item 9 — *"Nút Xuất PDF · 'Xuất PDF (.pdf)' · **click → auto-download** · Điều kiện hiển thị: Sau khi đã 'Xem báo cáo'"* |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1073` | Mapping dropdown — **UC133 *BC Chất lượng đào tạo*, bộ lọc đặc thù = *Khóa học cụ thể*** (chỉ 1), biểu đồ *Bar + Line* (*"nhãn trục = khóa học: mã/tên khóa, KHÔNG dùng tên đơn vị"*) |
| `:1092` | Quy tắc tương tác — *"Export XLSX/PDF **chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file**… Tên tệp cả hai định dạng theo Phụ lục E §H8 — `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`"* `[BA chốt 2026-08-04]` |
| `:1268` | BR-AUTH-08 — cột *Ngoại lệ* ghi **"QTHT bypass"**, cột *Áp dụng* ghi **"Toàn bộ FR-IX"** |
| `:1280` | BR-DATA-06 — *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |
| `srs-v3.5.md:6716` | **Phụ lục E §H8 — Tên tệp xuất thống nhất** (BẮT BUỘC): *"Khuôn `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (**kể cả dấu gạch nối**, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn… **Phần giờ-phút bắt buộc** để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa 255 ký tự"* `[BA chốt 2026-08-06]` |

**Rẽ nhánh — quyết TRƯỚC khi viết mục 4 (rẽ theo TỪNG VẾ):**

| Vế | Đặc tả | Verdict nhánh |
|---|---|---|
| **a** — *"Không thể tạo file xuất"* | **Nói rõ** và **khớp** kỳ vọng: `:1052` ghi thẳng *click → auto-download*, `:123` ghi *tải file .xlsx*; `:116` cho biết ERR-RPT-04 chỉ dành cho tình huống lỗi tạo tệp thật | Chấm được → viết mục 4 |
| **b** — *"Forbidden"* | **Nói rõ** về **câu chữ** khi từ chối vì quyền: `:117` đòi thông báo tiếng Việt *"Bạn không có quyền xem báo cáo này"*. Dù nghiệp vụ chốt hướng nào thì chuỗi tiếng Anh thô cũng lệch dòng này | Chấm được → viết mục 4 |
| **c** — khuôn tên tệp | **Nói rõ** và **khớp** kỳ vọng, **BA đã chốt 2026-08-04** (+ §H8 2026-08-06). Áp quyết định có sẵn | Chấm được → viết mục 4 |

⚠️ **Một điểm KHÔNG chấm:** câu hỏi *"vai trò QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo thống kê"* là chỗ
đặc tả **tự mâu thuẫn** (`:62`/`:526` liệt kê tác nhân CB Nghiệp vụ / CB Phê duyệt ↔ `:1268` ghi ngoại lệ
*"QTHT bypass"* áp *"Toàn bộ FR-IX"*). Câu hỏi này **đã có mục sẵn** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md)
§Mục 2 (mở lúc 12:40 khi verify `SLCTHT_06`) ⇒ **không mở mục hỏi mới**. Mục đó **không kéo verdict** của
case: dù BA chốt hướng nào, hành vi hiện tại vẫn phải thoả `:117`.

**IM LẶNG về:**
- **Chữ chính xác của thông báo thành công** khi xuất được — `:1058` mô tả *"Xuất thành công"* ở bảng thành
  phần màn hình, nhưng bảng Error Handling **không** có mã INF/WRN tương ứng ⇒ không chấm Fail vì chữ khác.
- **Có bắt buộc hiện toast *"Đang tạo file…"* hay không** — cùng lý do trên.
- **Bố cục bên trong tệp**: tên sheet, thứ tự cột, cách trình bày bảng. Đặc tả chỉ quy định **header file**
  phải có tiêu đề BC + kỳ + đơn vị + ngày tạo (`:1092`).
- **Có bao nhiêu thẻ số liệu phải vẽ trên màn, và nhãn các thẻ đó.** `:544`–`:548` quy định **output của báo
  cáo**, không quy định màn hình phải vẽ đủ mấy thẻ hay đặt nhãn gì. Đặc biệt: thẻ *"Tổng khóa học"* mà đối
  tác chụp **không** nằm trong danh sách `:544`–`:548`; ngược lại `tong_hoc_vien` chỉ hiện ở vòng 2 chứ không
  hiện ở vòng 1 ⇒ **không chấm Fail** vì số thẻ hay nhãn thẻ.
- **Công thức làm tròn** điểm TB / tỷ lệ đạt, và **điểm chuẩn để tính "đạt"** là bao nhiêu — đặc tả không nêu con số.
- **Kiểu biểu đồ và nhãn trục** (`:1073` *Bar + Line*, nhãn trục = khóa học) — nằm ngoài vế đối tác nêu; đo
  thì ghi nhận, không chấm.

---

## 3. Precondition

- **Tài khoản ra verdict cho vế a + vế c:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương**
  (`CB_NV_TW`), cấp **TW**, phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-10 (`:526`).
  Fallback (Rule 7, **cùng vai trò + cùng cấp**): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Tài khoản bắt buộc dùng cho vế b:** vai trò **Quản trị viên · QTHT**, đơn vị **BTP · TW** — **chính vai
  trò đối tác dùng ở CẢ HAI vòng** (đọc từ góc phải trên `CLDTBDPL_06.jpg` và `CLDTBDPL_06_v2.jpg`). Vế b là
  *"Forbidden"*, tức **triệu chứng phân quyền**; đo bằng vai trò khác thì không tái hiện được điều đối tác nêu.
  > **Vì sao không vướng quy tắc "tài khoản quản trị không ra verdict":** quy tắc đó chặn việc **quyền rộng
  > che lỗi phân quyền**. Ở đây chiều ngược lại — QTHT là vai trò **bị chặn**, dùng nó để **phơi** lỗi chứ
  > không che. Vế a và vế c vẫn ra verdict bằng `cbnv_tw_05`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**, Loại BC = **BC Chất lượng
  đào tạo** (`loai=chat-luong-dao-tao`). 🔴 **Không được nhầm** sang *BC Lớp đào tạo **đang** diễn ra*
  (FR-IX-06, dòng 200) hay *BC Lớp đào tạo **đã** diễn ra* (FR-IX-07, dòng 205) — hai màn đó lọc theo *Hình
  thức / Lĩnh vực*, còn màn tôi lọc theo **Khóa học** và có thẻ **Tỷ lệ đạt**. Kiểm bằng cả 3 chỗ: chuỗi
  trong URL · chữ trong ô chọn *Loại báo cáo* · tiêu đề khối kết quả.
- **Dữ liệu tiền đề:** ≥1 **khóa học đã kết thúc + có điểm kiểm tra học viên** trong kỳ + phạm vi đơn vị được
  chọn (`:536` — *"điểm TB kiểm tra, tỷ lệ đạt … trong kỳ"*), và để đo được bộ lọc thì cần **≥2 khóa học khác
  nhau có dữ liệu**. Không có dữ liệu → đó là `INF-RPT-01` hợp lệ (`:113`), **phải đổi kỳ/đơn vị/khóa học**
  để có dữ liệu rồi mới đo nút xuất. **Mọi cấu hình đều rỗng ⇒ GAP chưa đóng ⇒ verdict ô trống**, nêu rõ
  cần seed gì.
- **Bộ lọc neo theo đối tác:** cả **hai vòng** đều dùng **cùng một cấu hình** — Kỳ **Năm** · 01/01/2026 →
  31/12/2026 · Đơn vị **Toàn quốc** · **Khóa học để trống**. Thao tác: [Xem báo cáo] → [Xuất Excel].
  ⇒ Cấu hình này **bắt buộc phải có** trong bộ đo; các cấu hình còn lại là phần **phủ thêm** (mục 5).
- **Cache máy chủ:** trước khi kết luận *"không có dữ liệu"* hoặc *"bộ lọc không tác dụng"*, kiểm trường
  **"Thời điểm tạo"** / `ngayTaoBc` xem có nhảy theo từng lượt bấm không; nghi cache thì đổi `denNgay` 1 ngày
  để lấy khoá cache mới.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi bộ theo dõi còn sống; **đếm thông báo theo mốc giờ khác nhau**, không theo số phần tử; đọc `innerText`.
  > ⚠️ Bài học đã ghi ở `tieuchi/SLHDVM_06.md` §8 và `tieuchi/CGTVPL_06.md` §3: bộ bắt kiểu *"nghe node mới
  > được thêm"* **bỏ sót** chữ *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**. Phải đo bù bằng
  > cách lấy mẫu **nội dung** vùng thông báo theo thời gian (`innerText`, ~100 ms/lần) + ghi hình học
  > (vị trí · kích thước · thời gian sống) để chứng minh người dùng nhìn thấy thật.
- ⚠️ **Bẫy thao tác đã biết** (ghi trước khi đo, để không log oan): nút **[Xuất PDF]** mở hộp thoại
  *"Tùy chọn in báo cáo PDF"* chứ **không** tải ngay; **hộp thoại còn mở sẽ nuốt cú bấm kế tiếp** → phải đóng
  trước khi bấm nút khác. Khung thông báo sống **~3,2 s** → **hẹn giờ bấm rồi mới chụp**, đừng chụp sau.

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
   "Luôn"** của FR-IX-10 (`:544`, `:545`): **điểm trung bình kiểm tra** và **tỷ lệ đạt**; có thẻ *Tổng học
   viên* (`:546`) trên màn thì so cả chỉ số đó. Chỉ số nào màn không vẽ thẻ riêng thì lấy từ **phản hồi của
   chính lần chạy báo cáo đó**. Có bảng phân theo khóa học (`:547`) hoặc theo đơn vị (`:548`) trong tệp thì
   các dòng phải **nhất quán** với chỉ số tổng: tổng số học viên cộng theo khóa học = `tong_hoc_vien`; điểm
   TB tổng và tỷ lệ đạt tổng phải **nằm trong khoảng [min, max]** của các giá trị thành phần (`:536` là trung
   bình theo khóa/đơn vị, không cho phép suy ra phép cộng đơn thuần trên cột điểm hay cột %).
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280`): với 4 dạng ở mục 5, số liệu trong tệp **đổi theo** và mỗi
   lần đều khớp số trên màn của **chính lần đó** — không phải luôn trả bản không lọc. Kiểm chéo bằng md5 các
   tệp: 2 dạng cho số trên màn khác nhau mà tệp giống hệt ⇒ vi phạm.
7. **Bộ lọc đặc thù *Khóa học* có tác dụng thật** (`:534` `khoa_hoc_id`; `:552` đòi *"chọn KH cụ thể → hiển
   thị chi tiết KH đó"*): chọn một khóa học cụ thể thì **số trên màn** và **số máy chủ trả về** phải thu hẹp
   về đúng khóa đó, và **tham số giao diện gửi lên phải được máy chủ áp dụng**.
   Phép đo quyết định: so **số liệu trên màn** với **số liệu gọi thẳng máy chủ đúng tham số đó**; hai đường
   lệch nhau ⇒ bộ lọc không có tác dụng. **Loại trừ nhớ đệm bằng `ngayTaoBc`**: khoá bị máy chủ bỏ qua thì
   `ngayTaoBc` **không đổi** so với lượt không lọc.
   *(Đây là điều kiện của chính đặc tả `:552`, không phải suy từ lỗi của màn FR-IX-06/FR-IX-08.)*
8. **Tên tệp .xlsx đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`** (`:85`, `:123`, `:1092`, §H8
   `srs-v3.5.md:6716`) — lấy tên từ **nguồn người dùng thật thấy** (tệp rơi về máy, hoặc `content-disposition`
   của phản hồi). Đo đủ **4 điều kiện của khuôn**:
   - **8a.** Có đoạn thời gian `_YYYYMMDD_HHmm` ngay trước đuôi tệp: **8 chữ số ngày + `_` + 4 chữ số giờ-phút**,
     và **giá trị khớp thời điểm xuất** (không phải hằng số/ngày cũ). *Phần giờ-phút là bắt buộc.*
   - **8b.** Phần `{TenBaoCao}` chỉ gồm **chữ cái không dấu và chữ số**; **không** dấu gạch nối, **không**
     khoảng trắng, **không** dấu tiếng Việt, **không** dấu câu. Gạch dưới chỉ dùng để ngăn đoạn.
   - **8c.** Phần `{TenBaoCao}` **nhận ra được là tên của chính loại báo cáo này** — báo cáo **chất lượng đào
     tạo**. 🔴 Tên tệp trỏ sang loại báo cáo khác (vd chuỗi mang nghĩa *đánh giá hiệu quả*, *CG/TVV*, *chi
     phí*, *vụ việc*) là **trượt**, vì `:85` đòi `{TenBaoCao}` là *tên loại báo cáo* của chính báo cáo được
     xuất. *(Cấm đòi đúng y hệt chuỗi `BaoCaoDaoTao` — đó là prescribe; một chuỗi khác/dài hơn nhưng vẫn mang
     đúng nghĩa loại báo cáo này thì ĐẠT.)*
   - **8d.** Đuôi tệp là `.xlsx` khi bấm [Xuất Excel]; tổng độ dài tên ≤ 255 ký tự.
   - **Phép thử chống đè tệp** (lý do BA chốt bắt buộc giờ-phút): xuất **2 lần cùng ngày ở 2 phút khác nhau**
     phải ra **2 tên tệp khác nhau**.
9. **Nút [Xuất PDF]** — đối tác chỉ nêu `.xlsx` ở ô *Kết quả mong đợi*, nhưng `:1053` + `:124` quy định nút
   này cùng hành vi *click → auto-download* + cùng khuôn tên. Đo: người dùng nhận được tệp `.pdf` và tên tệp
   đúng **cùng khuôn** theo 8a–8d (đuôi `.pdf`).
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
- Số liệu trong tệp **lệch** số trên màn ở bất kỳ chỉ số tổng bắt buộc nào, hoặc các dòng chi tiết **không
  nhất quán** với tổng theo điều 5.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc cho số trên màn khác nhau nhưng tệp giống hệt nhau).
- **Bộ lọc *Khóa học* không có tác dụng** (điều 7): chọn khóa học mà số liệu không đổi trong khi gọi thẳng
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
- **Kỳ/đơn vị/khóa học không có dữ liệu** → `INF-RPT-01` (`:113`) là hành vi **hợp lệ**, không phải lỗi xuất tệp.
- **Số thẻ trên màn khác giữa hai vòng của đối tác** (3 thẻ vòng 1 · 4 thẻ vòng 2), hoặc nhãn thẻ khác danh
  sách `:544`–`:548` — đặc tả quy định **output báo cáo**, không quy định số thẻ vẽ trên màn.
- **Số liệu trên màn khác số liệu đối tác chụp** (3 khóa / 7 / 80.0 % vòng 1 · 5 khóa / 14 HV / 7 / 58.0 %
  vòng 2) — khác env, khác thời điểm, dữ liệu QA đã đổi.
- **Kiểu biểu đồ / nhãn trục** (`:1073` Bar + Line, nhãn trục = khóa học) — ngoài vế đối tác nêu.
- **Cách làm tròn** điểm TB / tỷ lệ đạt trên màn so với trong tệp — đặc tả im lặng về công thức làm tròn.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).
- **Thanh địa chỉ ở ảnh vòng 2 của đối tác ghi `loai=danh-gia-hieu-qua`** — đã phân tích ở mục 1, là URL chưa
  đồng bộ chứ không phải đối tác thao tác sai màn; **không** dùng để bác đối tác.
- **Câu hỏi "QTHT có được xuất hay không"** — điểm đặc tả tự mâu thuẫn, đã có mục BA sẵn, không kéo verdict.

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — cả 10 điều
> đều đếm được / so được / nhìn thấy được, không có chữ *"hiển thị đúng"* hay *"hợp lý"*.

---

## 5. Dạng dữ liệu phải phủ — **M = 4**

**Nguồn xác định M** (tra theo đúng thứ tự của flow, dừng khi đủ):
① **đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo**: `:536` *"Tính điểm TB kiểm tra, tỷ lệ đạt (số đạt
điểm chuẩn / tổng) theo khóa học, đơn vị trong kỳ"* ⇒ chỉ **một** nguồn bản ghi, chưa đủ chia dạng.
② **bộ lọc + giá trị ngay trên màn**: `:534` `khoa_hoc_id` (FK → KHOA_HOC) — và `:1073` xác nhận bộ lọc đặc
thù của **UC133 chỉ có *Khóa học cụ thể***; cộng thêm 2 chiều của input chung có mặt trên màn là **Kỳ**
(`:69`) và **Đơn vị** (`:72`), đều nằm trong Dimensions `:538`.
**Dừng ở ②** — đây là các chiều đổi được nội dung tệp xuất, và `:1280` buộc *"file xuất theo bộ lọc hiện
tại"* nên mỗi chiều phải có ít nhất một lượt đo.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc khóa học** (Khóa học trống, Đơn vị Toàn quốc, Kỳ Năm 2026) | **Đúng điều kiện của CẢ HAI vòng đối tác** (`CLDTBDPL_06.jpg` + `_v2.jpg`) — nhánh sinh ra *"Không thể tạo file xuất"* rồi *"Forbidden"* |
| 2 | **Lọc Khóa học = khóa A có dữ liệu** | Chiều lọc `:534` + **đúng câu AC `:552`** (*chọn KH cụ thể → hiển thị chi tiết KH đó*) |
| 3 | **Lọc Khóa học = khóa B khác** | Nhánh thứ hai của cùng chiều — cần để phân biệt *"bộ lọc có tác dụng"* với *"máy chủ luôn trả cùng một tập"*. Hai khóa phải cho 2 kết quả khác nhau (hoặc chứng minh được vì sao giống) |
| 4 | **Thu hẹp Đơn vị = 1 đơn vị cụ thể** (khóa học để trống) | Chiều **Đơn vị** của Dimensions `:538` + `:72`; kiểm `:1280` trên một chiều **độc lập** với bộ lọc đặc thù, để nếu chiều khóa học hỏng thì vẫn còn đường chứng minh tệp bám bộ lọc |

Kỳ báo cáo giữ cố định **Năm 2026** (01/01/2026 → 31/12/2026) cho cả 4 dạng — đúng kỳ đối tác dùng ở cả hai
vòng. Đơn vị giữ **Toàn quốc** cho dạng 1–3 (trùng cả hai vòng của đối tác); riêng dạng 4 đổi đơn vị.

> ⚠️ **Nếu một nhánh không có dữ liệu** (vd env chỉ có 1 khóa học có điểm, hoặc đơn vị chọn không có học
> viên): vẫn chạy dạng đó, ghi rõ màn trả `INF-RPT-01` và **không** chấm Fail vì thiếu dữ liệu (`:113`);
> nhưng phải khai trong mục 6 rằng dạng đó **không** dùng để chứng minh điều 6/7, và phải chứng minh bằng
> dạng còn lại. Đối tác không nêu tên khóa học cụ thể nào ⇒ chọn khóa có dữ liệu trên env và **khai rõ**.

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 15:58). 2 cột sau điền sau khi đo xong (16:20).

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Cả 2 vòng:** *Quản trị viên · QTHT*, đơn vị **BTP · TW** (đọc góc phải trên cả `CLDTBDPL_06.jpg` và `CLDTBDPL_06_v2.jpg`) | **Đo CẢ HAI vai trò.** ① `cbnv_tw_05` / `Test@1234` — *CB Nghiệp vụ - Trung ương* (`CB_NV_TW`), cấp **TW**, `donViId …0001`, **không** dùng fallback Rule 7 → ra verdict vế a + vế c. ② `admin` — *Quản trị hệ thống* (`QTHT`), cấp **TW**, `donViId …0001` = **đúng vai trò đối tác dùng** → ra verdict vế b. Danh tính cả hai đọc từ `/api/v1/auth/me` của chính phiên đo. **Hai tài khoản chỉ khác nhau ở VAI TRÒ, cùng đơn vị** ⇒ đổi đúng 1 biến | **Không** |
| Entity + trạng thái | **Vòng 1:** BC *Chất lượng đào tạo* đã render có dữ liệu (Tổng khóa học **3** · Điểm TB **7** · Tỷ lệ đạt **80.0 %**), *Thời điểm tạo 16/07/2026 15:18*. **Vòng 2:** đã render (Tổng khóa học **5** · Tổng học viên **14** · Điểm TB **7** · Tỷ lệ đạt **58.0 %**), *Thời điểm tạo 31/07/2026 15:02*. Cả 2 vòng nút [Xuất Excel]/[Xuất PDF] đều bấm được | **Cùng trạng thái entity:** báo cáo render xong, **có dữ liệu**, cả hai nút xuất **bấm được** (`disabled=false`) ở **cả hai vai trò**. Số liệu env tôi: **7 khóa học · 17 học viên · điểm TB 6.35 · tỷ lệ đạt 28.6 %** (*Thời điểm tạo 06/08/2026 16:04*). Vai trò QTHT bước [Xem báo cáo] cũng **200 + đủ số liệu** (7 · 17 · 6.35 · 28.6) ⇒ đúng tình huống *"vào được, thấy hết, chặn ở cú bấm cuối"* như ảnh đối tác | **Không** *(số liệu khác đối tác vì khác env — mục 4 đã ghi trước là không chấm Fail vì điều này)* |
| Dữ liệu tiền đề | Có khóa học đã chấm điểm trong kỳ Năm 2026, phạm vi Toàn quốc: vòng 1 ra 3 khóa; vòng 2 ra 5 khóa / 14 học viên | **Đủ và phủ rộng hơn đối tác:** kỳ Năm 2026 / Toàn quốc có **7 khóa học đã chấm điểm, 17 học viên, trải 3 đơn vị** (Cục Bổ trợ tư pháp · Sở Tư pháp Hà Nội · Bộ Kế hoạch và Đầu tư) ⇒ đủ để đo **2 khóa học khác nhau** (dạng 2/3) và **1 đơn vị thu hẹp** (dạng 4). **Không lượt nào rơi vào `INF-RPT-01`** ⇒ không phải đổi kỳ/đơn vị để né rỗng | **Không** |
| Input / filter / giá trị nhập | **Cả 2 vòng dùng CÙNG cấu hình:** Kỳ **Năm** 01/01→31/12/2026, Đơn vị **Toàn quốc**, **Khóa học để trống** (placeholder *"Chọn Khóa học"*). Vòng 1 URL có `loai=chat-luong-dao-tao`; vòng 2 URL còn sót `loai=danh-gia-hieu-qua` (chưa đồng bộ — xem mục 1). Thao tác cả 2 vòng: [Xem báo cáo] → [**Xuất Excel**] | **Bao trùm cấu hình đối tác** (= dạng 1: kỳ Năm 01/01→31/12/2026 · Toàn quốc · Khóa học trống · [Xem báo cáo] → [Xuất Excel]) **và phủ thêm 3 dạng**: lọc Khóa học `KH-2026-001` (dạng 2), lọc Khóa học `KH-20260716-002` (dạng 3), thu hẹp Đơn vị = *Sở Tư pháp Hà Nội* (dạng 4). Kiểm đúng màn bằng cả 3 chỗ: URL `loai=chat-luong-dao-tao` · ô chọn *Loại báo cáo* · tiêu đề khối kết quả | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 2 lượt xuất (1 mỗi vòng). M = **1** dạng duy nhất (không lọc khóa học). Không thấy đối tác thử lọc khóa học, đổi đơn vị, hay bấm [Xuất PDF] | **M = 4/4 dạng, phủ hết mục 5.** Vai trò `cbnv_tw_05`: **10 lượt xuất** (5 [Xuất Excel] qua chuột thật + 1 [Xuất PDF] + 1 lượt bắt thân yêu cầu + 3 lượt gọi thẳng máy chủ) → **10/10 ra tệp thật**, mở đọc bằng `openpyxl`/PyMuPDF. Vai trò `admin` (QTHT): **19 lượt** (10 [Xuất Excel] + 7 [Xuất PDF] qua chuột thật + 2 gọi thẳng) → **0 tệp**. Có cả **phép thử chống đè tệp** (2 phút khác nhau) và **phép đo tên khoá bộ lọc** (5 cách viết) mà đối tác không làm | **Không** |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** vòng 1 `htpldn-uat.ospgroup.vn/bao-cao?loai=chat-luong-dao-tao&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  (không có khoá lọc khóa học) · vòng 2 **không dùng URL làm neo** (thanh địa chỉ còn sót `loai=danh-gia-hieu-qua`,
  lệch nội dung màn — đã khai ở mục 1); neo của vòng 2 lấy theo **nội dung màn**: ô *Loại báo cáo* =
  *BC Chất lượng đào tạo*, bộ lọc *Khóa học* để trống, kỳ Năm 2026, đơn vị Toàn quốc.
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu — vòng 1 *Thời điểm tạo* **16/07/2026 15:18**,
  **3 khóa học / điểm TB 7 / tỷ lệ đạt 80.0 %**; vòng 2 *Thời điểm tạo* **31/07/2026 15:02**, **5 khóa học /
  14 học viên / điểm TB 7 / tỷ lệ đạt 58.0 %**.
- **Vai trò + env + bản dựng:** **Quản trị viên QTHT** (BTP · TW) · env `htpldn-uat.ospgroup.vn` ·
  nhãn **HTPLDN · V1.0** (vòng 1, đồng hồ 16/07/2026 15:18) → **V1.0.3** (vòng 2, đồng hồ 31/07/2026 15:03).

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn (V1.0 / V1.0.3 → bản đang đo).
⇒ Mọi kết luận *hết lỗi* chỉ là **tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

---

## 7. Kết quả chấm

### Verdict: 🔁 **REOPEN** — còn lỗi, chuyển lại dev

**Một câu lý do:** vai trò *Quản trị viên · QTHT* — **đúng vai trò đối tác dùng ở cả hai vòng** — vẫn xem được
báo cáo đầy đủ và vẫn bấm được hai nút xuất, nhưng **mọi** lượt xuất đều bị từ chối và chữ hiện lên màn là
chuỗi tiếng Anh thô **"Forbidden"**, lệch dòng `:117` vốn đòi câu tiếng Việt cho người dùng.

### Chấm theo từng vế đối tác nêu

| Vế | Đối tác nêu | Đo được | Kết |
|---|---|---|:-:|
| **a** | [Xuất Excel] → *"Không thể tạo file xuất. Vui lòng thử lại."* | Vai trò đặc tả cho phép (`cbnv_tw_05`): **10/10 lượt ra tệp thật**, chữ trên màn luôn là *"Đang tạo file..."* → *"Tạo file thành công."*, **không lượt nào** hiện câu `:116` | ✅ **hết lỗi** |
| **b** | Retest 31/07 → **"Forbidden"** | Vai trò QTHT: **19/19 lượt bị từ chối, 0 tệp**; chữ trên màn đúng chuỗi **"Forbidden"** (khung sống ~3,2 s, rộng ~1.416 px, sát đỉnh màn ⇒ người dùng nhìn thấy thật); máy chủ **403** `ERR-PERM-SYS-00-01` `"message":"Forbidden"`, không có `content-disposition` | ❌ **tái hiện nguyên vẹn** |
| **c** | Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` | `BaoCaoChatLuongDaoTao_20260806_1605.xlsx` — lấy từ **cả hai** nguồn người dùng thật thấy (tệp rơi về máy + `content-disposition: attachment; filename="BaoCaoChatLuongDaoTao_20260806_1613.xlsx"`); PDF cùng khuôn | ✅ **hết lỗi** |

> **Vế a và c hết lỗi nhưng KHÔNG kéo được verdict lên Pass** — flow ghi rõ: *case gộp nhiều vế, mọi vế hết
> lỗi mới Pass; còn ≥1 vế lỗi → **Reopen***; và *fix một phần → Reopen*.

### Chấm theo 10 điều của mục 4

| # | Điều kiện | Đo được | Kết |
|:-:|---|---|:-:|
| 1 | Không báo lỗi tạo tệp / không bị chặn quyền (vai trò đặc tả cho phép) | 4/4 dạng, mỗi lượt **1 request · 1 khung thông báo**; nguyên văn *"Đang tạo file..."* → *"Tạo file thành công."*. Không lượt nào ra câu `:116` hay `:117` | ✅ |
| 2 | Người dùng thật sự nhận được tệp | 4/4 dạng có tệp rơi về thư mục tải xuống; gọi thẳng máy chủ trả `content-disposition: attachment` + đúng `content-type` của .xlsx | ✅ |
| 3 | Tệp mở được như workbook thật | Cả 6 tệp `.xlsx` mở được bằng `openpyxl.load_workbook()`, 1 sheet *"BC Chất lượng đào tạo"*, có ô không rỗng. PDF: magic `%PDF-`, 1 trang, khổ 595.28 × 841.89 pt (A4) | ✅ |
| 4 | Header đủ 4 thông tin `:1092` | `A1` *BC Chất lượng đào tạo* ① · `A2` *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* ② · `A3` *Đơn vị: Toàn quốc* ③ (dạng 4 đổi đúng thành *Đơn vị: Sở Tư pháp Hà Nội*) · `A4` *Ngày tạo: 06/08/2026* ④ | ✅ |
| 5 | Số liệu trong tệp khớp màn + nội bộ nhất quán | 4/4 dạng khớp (7·17·6.35·28.6 / 1·2·7.85·100 / 1·2·1.5·0 / 1·3·6·0). Cộng số HV theo 7 dòng khóa học = **17** = `tong_hoc_vien`; đếm dòng = **7** = `tong_khoa_hoc`; điểm TB tổng 6.35 ∈ [1.5 , 10]; tỷ lệ đạt tổng 28.6 ∈ [0 , 100] | ✅ |
| 6 | Tệp bám bộ lọc hiện tại (`:1280`) | 6 tệp → **6 md5 khác nhau**; dòng `A3` đổi theo đơn vị; không có cặp *"màn khác số mà tệp giống hệt"*. Kiểm chéo đường thứ hai: kích thước tệp gọi thẳng máy chủ **7.423 / 6.950 / 6.964 B** trùng khít tệp giao diện tải về của dạng 1/2/3 | ✅ |
| 7 | Bộ lọc đặc thù *Khóa học* có tác dụng thật (`:534`, `:552`) | Giao diện gửi khoá **`khoaHocId`**, máy chủ **áp dụng đúng** khoá này (7 khóa → 1 khóa). Thử 5 cách viết: `khoaHocId` **có tác dụng**; `fd_khoaHocId` / `khoa_hoc_id` / `khoaHoc` bị bỏ qua ⇒ **màn này KHÔNG dính lỗi lệch tên khoá** mà phiên chính báo ở FR-IX-06/FR-IX-08 | ✅ |
| 8 | Tên tệp `.xlsx` đúng khuôn | **8a** `_20260806_1605` — 8 chữ số ngày + `_` + 4 chữ số giờ-phút, **khớp thời điểm xuất thật** ✔ · **8b** `BaoCaoChatLuongDaoTao` chỉ chữ không dấu + số, không gạch nối/khoảng trắng ✔ · **8c** *"ChatLuongDaoTao"* = **đúng loại báo cáo này**, không trỏ sang loại khác ✔ · **8d** đuôi `.xlsx`, dài 41 ký tự ≤ 255 ✔ · **chống đè**: 16:09 → `…_1609.xlsx`, 16:11 → `…_1611.xlsx`, **2 tên khác nhau** ✔ | ✅ |
| 9 | Nút [Xuất PDF] cùng hành vi + cùng khuôn tên | Hộp thoại *"Tùy chọn in báo cáo PDF"* → [Xuất file] → nhận `BaoCaoChatLuongDaoTao_20260806_1610.pdf` (34.281 B), **cùng khuôn 8a–8d**, đuôi `.pdf` | ✅ |
| **10** | **Vai trò QTHT: hoặc (a) nhận được tệp, hoặc (b) bị từ chối kèm thông báo tiếng Việt theo `:117`** | **Trượt cả hai nhánh.** (a) 19 lượt · **0 tệp**. (b) Chữ hiện ra là chuỗi tiếng Anh thô **"Forbidden"** — không phải câu tiếng Việt `:117` *"Bạn không có quyền xem báo cáo này"*, cũng không phải bất kỳ câu tiếng Việt nào | ❌ |

**9/10 đạt · điều 10 trượt ⇒ FAIL theo mục 4 ⇒ verdict REOPEN.**

### So sánh vai trò — phép đối chứng đổi đúng một biến

Cùng đường dẫn `POST /api/v1/bao-cao/export` · **cùng thân yêu cầu từng chữ** · cùng `donViId …0001` ·
cùng bó mã `3904131c…`:

| Vai trò | Bước [Xem báo cáo] | Nút xuất | Bước xuất | Tệp về máy |
|---|---|---|---|---|
| `CB_NV_TW` (`cbnv_tw_05`) | 200 · 7 · 17 · 6.35 · 28.6 | bật | **200** · `content-disposition: attachment; filename="BaoCaoChatLuongDaoTao_20260806_1613.xlsx"` | **có** (7.423 B) |
| `QTHT` (`admin`) | **200 · 7 · 17 · 6.35 · 28.6** (thấy đủ) | **bật** | **403** · `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}` · **không** có `content-disposition` | **0** |

⇒ Chênh lệch **chỉ do vai trò**. Hệ thống cho QTHT vào tận nơi, thấy hết số liệu, **bật cả hai nút xuất**,
rồi mới chặn ở cú bấm cuối bằng một chuỗi tiếng Anh — đúng hình ảnh đối tác chụp ở vòng 2.

> **Điều 10 KHÔNG phụ thuộc câu hỏi BA.** Dù BA chốt QTHT **được** xuất (`:1268` *"QTHT bypass"* áp *"Toàn bộ
> FR-IX"*) hay **không được** xuất (`:62`/`:526` chỉ liệt kê CB Nghiệp vụ / CB Phê duyệt), hành vi hiện tại
> vẫn trượt: chốt *được* ⇒ trượt nhánh (a); chốt *không được* ⇒ vẫn trượt nhánh (b) vì `:117` đòi câu tiếng
> Việt. **Đây là lý do vế b ra verdict được ngay mà không phải chờ BA.**

### Quan sát ngoài vế đối tác nêu — ghi nhận, **không** kéo verdict, **không** mở dòng bug mới

| # | Quan sát | Vì sao không chấm |
|:-:|---|---|
| a | **Thiếu nhóm đầu ra `theo_don_vi[]`** điều kiện *"Luôn"* (`:548`). Phản hồi máy chủ chỉ có `danhSachKhoaHoc` (≈ `theo_khoa_hoc[]` `:547`); tệp xuất cũng chỉ có bảng *"Danh sách khóa học"*, không có bảng tổng hợp theo đơn vị | Ngoài 3 vế đối tác nêu (đối tác chỉ nói về **xuất tệp**). Đã báo phiên chính | 
| b | **Hai lần xuất trong CÙNG một phút ra TRÙNG tên tệp**: 2 lượt lúc 16:12 đều nhận `…_20260806_1612.xlsx`, trình duyệt phải tự thêm `" (1)"`; 3 lượt gọi thẳng lúc 16:13 cũng cùng tên. Phụ lục E §H8 (`srs-v3.5.md:6716`) đòi *"trùng tên thì tự thêm hậu tố `_1`, `_2`"* | Đối tác chỉ đòi khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}`; **phép thử chống đè của mục 4 (2 phút khác nhau) vẫn ĐẠT**. Đã báo phiên chính |
| c | Thẻ *"Điểm trung bình"* trên màn **cắt** phần thập phân (6.35 → `6`; 7.85 → `7`; 1.5 → `1`); bảng khóa học trên màn làm tròn 1 chữ số; tệp giữ đủ ⇒ **3 cách hiển thị cho cùng một con số** | Mục 4 đã ghi TRƯỚC: đặc tả **im lặng** về công thức làm tròn |
| d | Thẻ *"Tỷ lệ đạt"* tổng = 28.6 % ứng với **2/7 khóa học**, trong khi cộng theo học viên là 4/17 ≈ 23.5 % | `:536` chỉ ghi *"số đạt điểm chuẩn / tổng"*, **không nói mẫu số là học viên hay khóa học** ⇒ không đủ căn cứ chấm |

### Bằng chứng

| Tệp | Nội dung |
|---|---|
| [`…-01-dang1-khong-loc-khoahoc-man-hinh-truoc-khi-xuat-V108.png`](../image/CLDTBDPL_06-01-dang1-khong-loc-khoahoc-man-hinh-truoc-khi-xuat-V108.png) | Dạng 1 (đúng cấu hình đối tác) — màn *BC Chất lượng đào tạo*, Khóa học để trống, 7 khóa · 17 HV · 6 · 28.6 %, ngay trước khi bấm [Xuất Excel] |
| [`…-02-dang1-ngay-sau-bam-xuat-excel-V108.png`](../image/CLDTBDPL_06-02-dang1-ngay-sau-bam-xuat-excel-V108.png) | Ngay sau cú bấm [Xuất Excel] ở vai trò `cbnv_tw_05` — khung thông báo *"Tạo file thành công."*, **không** có câu lỗi nào |
| [`…-03-dang2-loc-KhoaHoc-KH2026001-man-hinh-truoc-khi-xuat-V108.png`](../image/CLDTBDPL_06-03-dang2-loc-KhoaHoc-KH2026001-man-hinh-truoc-khi-xuat-V108.png) | Dạng 2 — lọc Khóa học `KH-2026-001`, số liệu thu về 1 khóa · 2 HV · 7 · 100.0 % |
| [`…-04-dang3-loc-KhoaHoc-KH20260716002-so-lieu-doi-V108.png`](../image/CLDTBDPL_06-04-dang3-loc-KhoaHoc-KH20260716002-so-lieu-doi-V108.png) | Dạng 3 — đổi sang khóa học khác `KH-20260716-002`, số liệu **đổi hẳn** (1 khóa · 2 HV · 1 · 0.0 %) ⇒ bộ lọc *Khóa học* có tác dụng thật |
| [`…-05-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png`](../image/CLDTBDPL_06-05-dang4-donvi-SoTuPhapHaNoi-man-hinh-truoc-khi-xuat-V108.png) | Dạng 4 — thu hẹp Đơn vị = *Sở Tư pháp Hà Nội*, 1 khóa · 3 HV · 6 · 0.0 % |
| [`…-06-hop-thoai-tuy-chon-in-PDF-V108.png`](../image/CLDTBDPL_06-06-hop-thoai-tuy-chon-in-PDF-V108.png) | Bẫy thao tác — [Xuất PDF] mở hộp thoại *"Tùy chọn in báo cáo PDF"* chứ không tải ngay |
| [`…-07-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png`](../image/CLDTBDPL_06-07-vaitro-QTHT-xem-duoc-bao-cao-nut-xuat-bat-V108.png) | Vai trò **QTHT** xem được báo cáo đầy đủ (7 · 17 · 6 · 28.6 %) và **cả hai nút xuất đều bật** |
| [`…-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png`](../image/CLDTBDPL_06-08-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-excel-V108.png) | Vai trò **QTHT** bấm [Xuất Excel] → khung thông báo đỏ **"Forbidden"** ở đỉnh màn — tái hiện đúng ảnh vòng 2 của đối tác |
| [`…-09-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png`](../image/CLDTBDPL_06-09-vaitro-QTHT-thong-bao-Forbidden-khi-xuat-pdf-V108.png) | Nhánh PDF cũng vậy — vai trò **QTHT** bấm [Xuất file] trong hộp thoại → cùng chuỗi **"Forbidden"** |
| [`…-10-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt`](../image/CLDTBDPL_06-10-nguyen-van-thong-bao-va-phan-hoi-may-chu.txt) | **Nguyên văn** chữ trên màn theo mốc giờ + thân phản hồi máy chủ + nội dung tệp đọc bằng `openpyxl` + md5 + bảng đo tên khoá bộ lọc |
| `testfiles/BaoCaoChatLuongDaoTao_20260806_16{05,07,08,09,11,12}.xlsx` + `…_1610.pdf` | 7 tệp xuất thật, giữ nguyên để đối chiếu md5 |

### Giới hạn hiệu lực

- Đo trên **env kiểm thử nội bộ** `18.143.165.120.nip.io`, **khác** env nghiệm thu `htpldn-uat.ospgroup.vn`
  của đối tác. Kết luận *hết lỗi* của vế a + vế c là **tạm**, chưa có hiệu lực cho tới khi bó mã
  `3904131cf562e0349890ac1bd058eb1f` lên môi trường nghiệm thu.
- **Chưa đo được:** ① khổ giấy / font bên trong tệp `.xlsx` (`:85` Times New Roman 13 — ngoài vế đối tác nêu,
  không mở tới mức đọc style); ② nội dung chi tiết bên trong PDF ngoài phần header (quốc hiệu / khối ký cuối
  trang theo `:86`); ③ hành vi ở **đúng** env nghiệm thu của đối tác.
- **Không dùng được kỹ thuật loại trừ nhớ đệm bằng `ngayTaoBc`** trên màn này: phản hồi máy chủ **không có**
  trường đó (dòng *"Thời điểm tạo"* trên màn do giao diện tự sinh). Đã loại trừ nhớ đệm bằng cách khác —
  gọi 5 biến thể khoá bộ lọc trong **cùng một phiên, cùng thời điểm**, thu về 2 tập kết quả khác nhau
  ⇒ máy chủ tính lại theo tham số thật, không trả bản nhớ đệm chung.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 15:58** — viết mục 1–6 **TRƯỚC khi mở màn tranh chấp**. Đã đọc: bằng chứng đối tác (2 tệp,
  full-res), đặc tả (`srs-fr-11-bao-cao.md`, `srs-v3.5.md` §H8), dòng 218 tab `bug`, và hồ sơ QA nội bộ đã
  khai ở đầu file.
- **2026-08-06 16:20** — điền khối bản dựng (đo 2 lần, giống hệt nhau ⇒ không trôi trong phiên), 2 cột cuối
  mục 6, và mục 7. **Không sửa một chữ nào ở mục 4 và mục 5** sau khi mở màn — 10 điều kiện và M = 4 giữ
  nguyên như lúc 15:58.
- **2026-08-06 16:28** — hồ sơ đi kèm đã xong: phiếu lỗi
  [`bug-report.md` § Phần 10 · `BUG-CLDTBDPL-006`](../bug-report.md) (kèm khối *CÁCH VERIFY sau Dev fix* vì
  verdict là Reopen); 1 blockquote bổ sung vào [`cau-hoi-BA.md`](../cau-hoi-BA.md) § *Mục 2* (**không** mở
  mục hỏi mới); ghi bảng bằng `tools/sheet_bug_verify_write.py` — tab `bug` dòng 218, `Trạng thái dev fix`
  `Fixed → Reopen`, `Kết quả verify` = nội dung `note-CLDTBDPL_06.txt`.
- **2026-08-06 16:20 — ghi nhận điều đo được mà mục 4 đã chặn trước, để không tự nới tiêu chí:** ba quan sát
  (thiếu `theo_don_vi[]`, trùng tên tệp trong cùng phút, cắt thập phân điểm TB) đều **không** được kéo vào
  bảng 10 điều; chúng nằm ở phần *"Quan sát ngoài vế đối tác nêu"* của mục 7 và đã báo về phiên chính,
  **không** mở dòng bug mới.
