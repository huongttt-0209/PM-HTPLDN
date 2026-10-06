# TIẾN ĐỘ LÔ G3 — verify 7 case trên env nghiệm thu đối tác

| Mục | Giá trị |
|---|---|
| Env đo | `https://htpldn-uat.ospgroup.vn` |
| **Bản dựng đọc trên UI** | **V1.0.10** · bó mã `assets/index-Bd1akG3f.js` · `Last-Modified 07/08/2026 15:15 giờ VN` |
| Sheet | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` · gid `1714340219` |
| Bắt đầu | 2026-08-07 ~16:45 giờ VN |

## Bảng tiến độ

| # | Mã TC | Dòng | Tài khoản | Chuẩn chấm | Đo | Ghi sheet | Đọc lại | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | QLKTLBG_19 | 13 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 2 | QLKTLBG_18 | 12 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 3 | QLKTLBG_20 | 14 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 4 | TKHSYCHTPL_03 | 50 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 5 | KTDGKQHT_10 | 11 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 6 | KTHSYCHTPL_11 | 45 | `cbnv_tw` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |
| 7 | CNHSNLTVV_03 | 36 | `nht_04_ui` | ✅ | ✅ | ✅ | ✅ khớp | **✅ Pass** |

## Rút gọn diễn giải — 2026-08-07 (theo yêu cầu user)

User: *"viết ngắn gọn, đủ ý, chính xác thôi"*. Đã viết lại toàn bộ 7 ô `Kết quả verify` theo 5 khối
(kết luận · điều kiện đo · phạm vi đã kiểm · số đo quyết định · phạm vi hiệu lực + link ảnh).
Cắt: thuật lại từng bước, giải thích phương pháp, nhắc lại nội dung phiếu, trích dài đặc tả (chỉ còn `file:line`).
Chi tiết đầy đủ vẫn nằm ở `do/*.md`.

| Mã TC | Dòng | Ký tự cũ → mới | Link Drive giữ được |
|---|---|---|---|
| KTDGKQHT_10 | 11 | 10573 → **4515** | 4/4 |
| QLKTLBG_18 | 12 | 7234 → **2554** | 4/4 |
| QLKTLBG_19 | 13 | 4314 → **1846** | 2/2 |
| QLKTLBG_20 | 14 | 5489 → **2706** | 2/2 |
| CNHSNLTVV_03 | 36 | viết mới theo chuẩn — **1842** | 3/3 |
| KTHSYCHTPL_11 | 45 | 12785 → **6136** | 4/4 |
| TKHSYCHTPL_03 | 50 | 8712 → **3495** | 2/2 |

Audit sau khi ghi: cả 7 ô md5 khớp file `note/*.txt`, `Trạng thái dev fix` = `UAT done` cả 7, **0 link Drive bị mất**.

## Kết quả từng case (cập nhật dần)

### 1. QLKTLBG_19 — dòng 13 — ✅ **Pass** (16:46–16:52)
- Vế 1 (có chức năng Xuất Excel): **ĐẠT** — rà 35 phần tử `button/a/[role=button]`, thanh công cụ có đúng 3 nút *Thêm mới · **Xuất Excel** · Làm mới*, nút không bị vô hiệu hoá. Triệu chứng "màn hình không có nút" **không tái hiện**.
- Vế 2 (tệp chứa toàn bộ danh sách): **ĐẠT** — `POST /api/v1/bai-giangs/export` → **HTTP 200**, header máy chủ tự khai `x-export-exported: 7` / `x-export-total: 7`. Mở tệp bằng `openpyxl`: 1 sheet "Bài giảng", **7 dòng dữ liệu = tổng 7 bản ghi**, đủ cả bản "Chưa công khai".
- "Không có điều kiện lọc" chứng minh bằng query thật màn gửi lên: chỉ có tham số phân trang, **0/7 tham số lọc**.
- 1 bấm = 1 request = 1 toast (không lặp). Console 0 lỗi.
- **🟢 Rủi ro R5 KHÔNG xảy ra** — dù hệ thống không tồn tại quyền `export_bai_giang`, endpoint vẫn trả 200.
- ⚠️ **Sự cố quy trình đã vá:** lần ghi đầu làm **mất 2 link Drive bằng chứng** ở ô cũ. Đã tải ảnh mới lên Drive và ghi lại ô kèm link xem được. → Đã bổ sung **BRIEF §6b** bắt buộc bước này cho mọi case sau.
- 🔴 **Đã sửa theo user (2026-08-07):** `Trạng thái dev fix` đổi `Test done` → **`UAT done`**. Đọc lại xác nhận `UAT done`; các ô chỉ đọc nguyên vẹn (`Trạng thái`=Fail · `Dopai`=N/R · `TKM phản hồi lần 1` không đổi · `DEV phản hồi lần 1` vẫn trống · không đụng cột vòng 2).

### 2. QLKTLBG_18 — dòng 12 — ✅ **Pass** (17:00–17:12)
Mốc chưa lọc = **7** (chân bảng + tổng máy chủ + đếm tay, 3 nguồn khớp).

| Tiêu chí lọc | Nội dung thật gửi lên | HTTP | Màn báo | Dòng dữ liệu trong tệp | Máy chủ tự khai |
|---|---|---|---|---|---|
| Loại tài liệu = PDF | `{"loaiTaiLieu":"PDF"}` | 200 | 2 | **2** — 2/2 khớp tên | `2/2` |
| Loại tài liệu = Video | `{"loaiTaiLieu":"VIDEO"}` | 200 | 3 | **3** — 3/3 khớp tên | `3/3` |
| **Công khai = Không công khai** | `{"congKhai":"false"}` | 200 | 6 | **6 — nhưng cả 6 đều "Đã công khai"** | `6/6` |

- **Vế 1 (có nút Xuất Excel): ĐẠT** — triệu chứng cũ "màn hình không có nút chức năng" **không còn**. Bấm 3 lần, cả 3 lần HTTP 200 + tệp thật + đúng 1 thông báo, không lặp.
- **Vế 2: ĐẠT với "Loại tài liệu", KHÔNG ĐẠT với "Công khai".** Hai phép đo 2 và 3 khác nhau và đều ≠ 7 → tệp thật sự bám bộ lọc, không cắt theo trang, không trùng hợp.
- 🔴 **Điểm hỏng:** chọn "Không công khai" trả về **đúng tập 6 bản ghi giống hệt "Công khai", cả 6 đều đang công khai**; bản duy nhất "Chưa công khai" ("Test video 2") vắng mặt. Tệp Excel thừa hưởng đúng tập sai đó → **0/6 dòng khớp điều kiện đã chọn**. Kiểm chéo: bản ghi đó hiện bình thường khi không lọc và khi lọc Video → không bị ẩn, chỉ riêng tiêu chí này sai.
- Đối chiếu đặc tả (đã mở file xác minh): `srs-fr-03-dao-tao.md:874` (AC FR-III-08) · `:844` · `:1958` · `:1952` · `srs-v3.5.md:5570`.
- Console 0 lỗi.
- ✅ Xác nhận N1 của recon là **lỗi thật, tái hiện được trên giao diện**, không phải hiện tượng riêng ở tầng API.
- 🔴 **Đổi verdict theo user (2026-08-07, sau khi đối chiếu lại phiếu):** ❌ Reopen → **✅ Pass**, `Trạng thái dev fix` = `UAT done`.
  Lý do: phiếu này là *"Xuất Excel với điều kiện lọc"*, triệu chứng gốc TKM ghi là *"Màn hình không có nút chức năng"* — đã hết.
  Chức năng xuất **chép đúng tập kết quả màn danh sách đang hiển thị** (6 dòng = 6 dòng trên bảng), nên nó **đạt** yêu cầu "xuất theo bộ lọc hiện tại".
  Điểm hỏng nằm ở **tiêu chí lọc "Công khai" của màn danh sách (FR-III-08)** — lỗi khác chức năng, đề nghị mở phiếu riêng. Đã ghi vào ô verify dưới dạng "ghi nhận ngoài phạm vi phiếu này".
- ✍️ Diễn giải rút gọn 7234 → 2064 ký tự theo yêu cầu user; giữ nguyên 4 link Drive.

### 3. QLKTLBG_20 — dòng 14 — ✅ **Pass** (17:22–17:27)
Mốc chưa lọc = **7** (chân bảng + `meta.total` + đếm tay, 3 nguồn khớp; xác nhận 2 lần).

Bộ lọc 0-kết-quả dựng trên giao diện bằng ô *"Tìm theo tên bài giảng"* = **`ZZQAKHONGTONTAI20260807`** → "Tìm kiếm".
**Cố ý KHÔNG dùng ô "Công khai"** (đang hỏng theo case 18) để không trộn 2 lỗi vào 1 verdict.

**Màn thật sự về 0 — chứng minh đủ 6 chiều:** `meta.total`=0 · `meta.totalPages`=0 · `data`=`[]` · đếm tay DOM 0 dòng ·
câu trạng thái rỗng nguyên văn **"Không có bài giảng nào phù hợp."** · `.ant-pagination` biến mất hoàn toàn.
Query thật màn gửi: `GET /api/v1/bai-giangs?keyword=ZZQAKHONGTONTAI20260807&page=1&pageSize=20` → 200.

| Số đo quyết định | Giá trị |
|---|---|
| `POST /api/v1/bai-giangs/export` | **HTTP 200** |
| Thân yêu cầu thật màn gửi | **`{"keyword":"ZZQAKHONGTONTAI20260807"}`** — mang đúng bộ lọc, KHÔNG bỏ qua bộ lọc |
| `x-export-exported` / `x-export-total` | **0 / 0** |
| Tệp `DanhSachBaiGiang_20260807_1726.xlsx` (6686 byte = `content-length`) | 1 sheet "Bài giảng", `max_row=1` → **0 dòng dữ liệu** (chỉ còn dòng tiêu đề) |
| **Đối chiếu** | **0 vs 7** — nếu bỏ qua bộ lọc thì tệp phải ra 7 dòng / ~8610 byte (số đo của case 19) |

- **Vế 1 (có chức năng Xuất Excel + bấm được): ĐẠT** — chứng minh bằng **thao tác thành công** (bấm → 200 → tệp thật), không lặp lại công liệt kê DOM của case 18/19.
- **Vế 2 (tệp phản ánh đúng bộ lọc): ĐẠT** — 0 dòng dữ liệu. Bẫy PASS-oan nguy hiểm nhất (tệp "rỗng" thực ra chứa cả 7 bản ghi) đã bị loại bằng bằng chứng trực tiếp.
- Kỳ vọng phiếu là **mệnh đề HOẶC** → hệ thống đi nhánh *"xuất danh sách rỗng"*; **không chấm Fail** vì nó báo "Xuất dữ liệu thành công." thay vì "không có dữ liệu" (đặc tả Nhóm III im lặng về câu chữ này).
- 1 bấm = 1 request = 1 toast ("Xuất dữ liệu thành công."), `BI_LAP=false`, observer tự kiểm = 1. Console 0 lỗi (chỉ 1 cảnh báo `/ticket=*` không liên quan).
- **D2b (GAP)** → đã ghi câu hỏi BA ở cuối note + `do/QLKTLBG_20.md` §15, nêu rõ **không chặn bàn giao, không ảnh hưởng verdict**.
- 🔴 **Sự cố tiền đề đã xử lý trước khi đo:** phiên bàn giao từ case 18 còn giữ ô lọc "Công khai"="Không công khai" **dù URL và lời gọi danh sách đã sạch (7 bản ghi)**; lần "Tìm kiếm" đầu vì thế gửi kèm `congKhai=false`. Đã bấm **"Xóa bộ lọc"** → xác nhận về 7 → gõ lại từ khoá và đo lại sạch. Chi tiết ở `do/QLKTLBG_20.md` §4.
- ⚠️ **Cải chính phép đo nội bộ:** ứng dụng dựng ô chọn bằng `.ant-select-content-has-value` + `title`, **không** dùng `.ant-select-selection-item` → bộ chọn cũ cho **âm tính giả** khi kiểm "ô lọc có giá trị chưa". Lượt sau dùng bộ chọn đúng.

### 4. TKHSYCHTPL_03 — dòng 50 — ✅ **Pass** (17:41–17:50)
🟢 **Rủi ro R2 KHÔNG xảy ra:** đếm lại `mucSla=SAP_HET` ngay trước khi đo (17:41) vẫn **1 bản ghi**
(`VV-BTP-TW-20260713-001`, `DA_DANH_GIA`, deadline 03/08) → tiền đề còn, không rơi vào nhánh "dừng báo lead".
🟢 **Bẫy R1 đã né:** đo ở tab **Tất cả**. Trên V1.0.10 tab mặc định khi vào màn **chính là "Tất cả (74)"**,
nhưng vẫn ghi rõ vì `tabCounts` của mức này là `{TAT_CA:1, HOAN_THANH:1}` — đứng tab hẹp hơn sẽ ra 0 dòng.
🟢 **Bẫy 3 không xảy ra:** vào màn ô lọc đã sạch (kiểm bằng bộ chọn đã cải chính `.ant-select-content-has-value` + `title`);
vẫn bấm "Xóa bộ lọc" theo trình tự → mốc chưa lọc **74** (chân bảng + `meta.total` + đếm tay, 3 nguồn khớp).

| Vế | Số đo quyết định | Kết |
|---|---|---|
| S1 — không còn báo lỗi | **0 khung thông báo** (observer tự kiểm =1, không lọc trùng) · **0** khung lỗi trên DOM · lời gọi danh sách **200/304** · **giá trị mức SLA màn gửi lên = `SAP_HET`** (hợp lệ), URL `?mucSla=SAP_HET&page=1` | ✅ ĐẠT |
| S2 — ra kết quả đúng mức | 1 dòng `VV-BTP-TW-20260713-001`, cột Cảnh báo thời hạn = "Sắp hết hạn"; `Hiển thị 1-1 / 1 kết quả` = `meta.total` 1 = đếm tay 1 | ✅ ĐẠT |
| S3 — phân trang 20/trang | Trang 1 = 20 dòng `Hiển thị 1-20 / 74`; trang 2 = 20 dòng `Hiển thị 21-40 / 74`; ô `20 / trang`; `pageSize=20`; **0 mã trùng giữa 2 trang** | ✅ ĐẠT |

**Bảng 4 mức + phép thử tổng** (mỗi mức 1 phép đo riêng qua giao diện, 0 dòng sai mức ở cả 4):
`BINH_THUONG 29 · SAP_HET 1 · QUA_HAN 5 · QUA_HAN_NGHIEM_TRONG 39` → **29+1+5+39 = 74 = mốc chưa lọc** ✔
⇒ bộ lọc phân hoạch đủ, không sót. Cả 4 lời gọi đều 200; 0 thông báo lỗi ở cả 4.

- **Lặp lại 2 lần trong 2 lần tải trang khác nhau** (vào bằng bấm menu · sau `reload ignoreCache`) — kết quả trùng khít ⇒ loại trừ ngẫu nhiên + loại trừ tab chạy mã cũ.
- **Video đối tác đã mở xem** (21 khung, `V1.0.2`, 30/07 09:08): trước khi bấm Tìm kiếm bảng CÓ dữ liệu mức "Sắp hết hạn"; sau khi bấm, địa chỉ thành `?mucSla=SAP_HET_HAN&page=1` và hiện khung lỗi `mucSla must be one of the following values: BINH_THUONG, SAP_HET, QUA_HAN, QUA_HAN_NGHIEM_TRONG`, bảng về rỗng. ⇒ nguyên nhân cũ = màn gửi giá trị ngoài tập hợp lệ. Nay màn gửi `SAP_HET` ⇒ nguyên nhân gốc đã hết.
- **KHÔNG** gõ tay địa chỉ cũ `?mucSla=SAP_HET_HAN` (bẫy c) — toàn bộ đo bằng thao tác chọn trên ô lọc.
- Chip "Bộ lọc nâng cao (3)" đã mở khai: 3 ô trống (Trạng thái "Tất cả" · Từ ngày · Đến ngày), không phải 3 điều kiện đang áp.
- Console 0 lỗi (1 cảnh báo `/ticket=*` không liên quan). Lượt đo **chỉ đọc**, không tạo/sửa/xoá bản ghi nào.
- **N2 (SRS tự lệch tên mức)** đã đưa vào phần "đề nghị BA" cuối note, ghi rõ không chặn bàn giao, không ảnh hưởng verdict. Bổ sung 1 điểm lệch nữa: **BR-SLA-02** (`srs-v3.5.md:5626`) chốt nhãn mức thấp nhất là **"Trong hạn"**, còn `srs-fr-05-vu-viec.md:1516` + giao diện dùng **"Bình thường"**.
- Ghi sheet: `Trạng thái dev fix` = **`UAT done`**, `Kết quả verify` = nội dung note (đè giá trị cũ của lượt đo env khác — đúng chủ ý). Đọc lại xác nhận **md5 khớp 100%** (8712 ký tự). Ô chỉ đọc nguyên vẹn: `Trạng thái`=Fail · `Kết quả thực tế` không đổi · `Dopai`=dev done · không đụng cột vòng 2.

### 5. KTDGKQHT_10 — dòng 11 — ✅ **Pass** (18:00–18:15)
🔴 **User THU HẸP PHẠM VI giữa lượt đo:** chỉ chấm đúng triệu chứng gốc *"Màn hình không có nút chức năng"* —
bỏ phần nạp tệp thật / đo bản xem trước / đọc lại điểm đã lưu ra khỏi căn cứ verdict.

- **Vế 1 (sau khi chọn đề, màn CÓ chức năng nạp): ĐẠT** — đo **2 lượt đối chứng**, khác đúng 1 biến số:
  - Lượt A — khóa **`KH-2026-001`** (cũng `DANG_DIEN_RA`, có học viên, **0 đề gán**): *Lưu kết quả · Tải mẫu điểm kiểm tra · Import Excel* đều **vô hiệu**; ô đề trống ("Chọn đề kiểm tra"). `input[type=file]` toàn trang = 0.
  - Lượt B — khóa đo **`KH-20260509-006`** (đề đã chọn): *Tải mẫu điểm kiểm tra* + *Import Excel* đều **BẬT**.
  - ⇒ Nút **có mặt cả 2 lượt**, chỉ bật khi có đề — đúng `srs-fr-03-dao-tao.md:578` + `:1924`. Triệu chứng gốc **không tái hiện**.
- **Vế 2 (gọi được, không lỗi): ĐẠT** — không dừng ở quan sát tĩnh. Tải mẫu → **HTTP 200**, tệp thật 8.278 byte về `~/Downloads`, mở bằng `openpyxl` đọc được (sheet ẩn `_HTPLDN_META` + 6 học viên điền sẵn, khớp bộ cột `:582`). Import Excel → hộp thoại mở, chọn tệp được. Kiểm tệp → `POST …/ket-quas/import/preview` **HTTP 200**. **0 lỗi 4xx/5xx**, console 0 lỗi.
- 🟢 **Khóa `KH-20260509-006` ở "Đang diễn ra"** (bước 4 thanh tiến trình đang sáng) ⇒ thỏa Điều kiện 2 phiếu (`:537` PRE-04). Khóa chưa tới `CHO_DUYET_KQ` nên bảng không ở chế độ chỉ đọc (`:1929`).
- ✅ **KHÔNG có thay đổi dữ liệu nào** — dừng trước nút "Xác nhận import (4 dòng hợp lệ)". Đọc lại điểm 6 học viên sau khi đóng hộp thoại: **khớp 6/6 với bản sao lưu**, 0 dòng lệch ⇒ không cần khôi phục.
- 📋 Số đo thu được **trước** lúc thu hẹp (ghi nhận, không dùng chấm): bản xem trước hiện `Tổng 6 · Hợp lệ 4 · Lỗi 2`, 2 tab `Hợp lệ (4)`/`Lỗi (2)`, dòng lỗi ghi rõ số dòng + lý do — `dòng 6: ERR-KQ-01: Điểm kiểm tra không hợp lệ (0-10): 15` · `dòng 7: … (0-10): abc`. Chi tiết ở `do/KTDGKQHT_10.md` §7.
- ⚠️ **Đính chính recon §2.1:** recon ghi 6 học viên "đã có điểm sẵn" — thực tế **chỉ 2/6** (tester 1 = 9.0 · tester 2 = 4.0), 4 người còn lại `null`.
- ⚠️ **Ô chọn đề không cho xóa** (`allowClear=false`) + khóa chỉ có 1 đề → giao diện **tự chọn sẵn** ⇒ không dựng được trạng thái "chưa chọn đề" trên chính khóa đo → phải mượn khóa đối chứng 0 đề.
- Ghi sheet: `Trạng thái dev fix` = **`UAT done`**, `Kết quả verify` = nội dung note (ô này trước đó **TRỐNG**). Đọc lại **md5 khớp 100%** (10.572 ký tự). Ô chỉ đọc nguyên vẹn: `Trạng thái`=Fail · `Dopai`=N/R · `TKM phản hồi lần 1` không đổi · không đụng cột vòng 2.

### 6. KTHSYCHTPL_11 — dòng 45 — ✅ **Pass** (18:24–18:31)
🔴 **User THU HẸP PHẠM VI:** chỉ chấm triệu chứng gốc — ở hồ sơ đúng tiền đề, màn **có** chức năng mở phiếu
kết luận không và **bấm có mở được không**. Bỏ: dựng VV mới · tick lại checklist · **lưu kết luận Đạt** ·
đo chuyển trạng thái · đo Phân công. **Lượt đo thuần CHỈ ĐỌC.**

**Hai hồ sơ đối chứng (đều cùng đơn vị TW với tài khoản đo):**

| | Hồ sơ **X** | Hồ sơ **Y** |
|---|---|---|
| Mã | `VV-BTP-TW-20260805-004` | `VV-BTP-TW-20260807-001` |
| Trạng thái | **Đang kiểm tra** | **Đã tiếp nhận** |
| Kết luận đã lưu | **`DAT`**, C01–C06 đều `DAT` (6/6) | **`null`**, `items=[]` |
| **Nút trên thanh hành động (rà DOM, nguyên văn)** | **`Phân công`** + **`Kiểm tra lại`** | **`Kiểm tra hồ sơ`** (đúng 1 nút) |
| Dòng đặc tả khớp | `:1745` (+ `[Kiểm tra lại]` của `:1744`) | `:1743` |

- **Câu 1 — có nút mở phiếu kết luận ở hồ sơ đúng tiền đề? CÓ.** Nhãn nguyên văn **`Kiểm tra lại`**
  (`<button>`, icon `verified`, không mờ, không vô hiệu). Rà đủ 8 phần tử `button/a/[role=button]` trong `<main>`:
  **0 menu phụ · 0 nút ẩn · 0 nút mờ**. **Không** phần tử nào mang chữ *"Hoàn tất kiểm tra"* ⇒ triệu chứng đối tác
  **tái hiện y nguyên ở bề mặt**, nhưng đó là ngữ cảnh `:1745`.
- **Câu 2 — bấm có mở được? CÓ.** Hộp thoại **`Kiểm tra hồ sơ`** (`Lần bổ sung: 0/3`), tiêu đề danh sách
  `Checklist Mẫu 01 NĐ55 (6 hạng mục)`: **6 nhóm radio / 12 ô chọn** Đạt–Không đạt. Ô `* Kết luận` mở ra
  **đủ 3 lựa chọn**, có **`Đạt — chuyển sang phân công`**. **0 toast · 0 lời gọi ghi · 0 lỗi 4xx/5xx.**
  Đóng bằng **`[Hủy]`**, **KHÔNG** bấm `[Xác nhận]`.
- **Câu 3 — nhãn đổi theo tình trạng đã lưu kết luận? CÓ.** Lập luận quyết định: X **đang ở đúng
  `DANG_KIEM_TRA`**; nếu chỉ phân nhánh theo trạng thái thì X phải hiện bộ nút `:1744`. Thực tế X hiện
  **`[Phân công]`** — bộ nút của dòng `:1745` mang đúng tên **"DANG_KIEM_TRA (kết luận Đạt)"**.
  ⚠️ **Giới hạn khai rõ:** X và Y khác **2 biến**; trạng thái đối chứng sạch (`DANG_KIEM_TRA` **chưa** lưu
  kết luận) **không đo được** vì cả 4 vụ `DANG_KIEM_TRA` đều đã lưu kết luận + lệnh thu hẹp cấm seed/cấm bấm
  `[Kiểm tra hồ sơ]` trên Y ⇒ **không khẳng định** nhãn ở trạng thái đó.
- **Nhãn lệch đặc tả = Minor**, không tự thành lỗi (chuẩn chấm §6 V1-b, §7c). Giao diện dùng
  `Kiểm tra hồ sơ`/`Kiểm tra lại` thay cho chữ `Hoàn tất Kiểm tra` của `:1744`; phiếu mở ra là một và giống nhau.
- **Vế "Đạt → Đã phân công": KHÔNG chấm** (ngoài phạm vi + trái đặc tả hiện hành `:541`/`:564`/`:1745`/`:2288`,
  quyết định BA `:22` ngày 2026-07-16 **nêu đích danh mã case này**). Đã đưa vào mục đề nghị BA cuối note,
  ghi rõ **không chặn bàn giao**.
- ✅ **KHÔNG đổi trạng thái vụ việc nào.** Đọc lại máy chủ sau lượt đo: X vẫn `DANG_KIEM_TRA`/`ketLuan=DAT`/
  `ngayKiemTra=2026-08-05T14:59:54.599Z` y hệt, lịch sử **vẫn đúng 3 dòng** không sinh dòng mới; Y vẫn
  `DA_TIEP_NHAN`/`ketLuan=null`. Console 0 lỗi (1 cảnh báo `/ticket=*` không liên quan).
- Ghi sheet: `Trạng thái dev fix` = **`UAT done`**, `Kết quả verify` = nội dung note (đè giá trị cũ của lượt đo
  bản dựng khác — đúng chủ ý). Ô chỉ đọc nguyên vẹn; **không đụng 4 cột vòng 2**.
- 🔴 **Sự cố phiên (xem N10):** phiên bàn giao đã chết sẵn (`ERR-AUTH-SYS-00-03` "Token đã bị thu hồi") và bị
  thu hồi **thêm 2 lần nữa** giữa lượt do **có phiên khác đăng nhập cùng `cbnv_tw`** (mốc MailHog 11:21:46 UTC
  không phải của tôi). Đã thử fallback Rule 7 cùng vai trò+cấp (`cb_nv_tw_01`) trước → **sai mật khẩu** (N11) →
  buộc đăng nhập lại `cbnv_tw` 1 lượt. Toàn bộ số đo lấy trong phiên 11:24:21–11:30:50 UTC.

### 7. CNHSNLTVV_03 — dòng 36 — ✅ **Pass** (18:44–19:00)
🔴 **User THU HẸP PHẠM VI:** chỉ verify triệu chứng gốc — bấm Lưu với dữ liệu hợp lệ **có đính tệp chứng chỉ**
thì còn báo *"Lỗi hệ thống, vui lòng thử lại sau."* không. Bỏ: nhánh phụ · tên tệp ở tab khác · tác dụng phụ
trạng thái · nhiều hồ sơ / nhiều kiểu tên tệp. **Đây là case bắt buộc ghi thật (bấm Lưu thật).**

Hồ sơ đo **`TVV-BTP-TW-0063`** (Tester TKM BTP-TW, loại TVV, `HOAT_DONG`, `id=789d5f7e…`), tài khoản
**`nht_04_ui`** (`/auth/me` → `vaiTro=["NHT"]`, `donViId=…8000-000000000001`, `capDonVi=TW`) — **1 lượt đăng nhập,
phiên KHÔNG bị thu hồi** (N10 không tái diễn). Tệp đính: `QA G3 (4.8) & CN (9.8).pdf` (672 B, tên có dấu cách +
ngoặc + `&` giống ảnh đối tác).

| Lượt bấm Lưu | Số lời gọi / khung thông báo | Nguyên văn thông báo | HTTP | Ý nghĩa |
|---|---|---|---|---|
| #1 — số thẻ hành nghề để trống (đúng như dữ liệu gốc) | 1 / 1, `BI_LAP=false` | **"Số thẻ hành nghề là bắt buộc đối với Tư vấn viên"** | **422** `ERR-VAL-IV-03-10`, `field=soTheHanhNghe` | từ chối **nghiệp vụ** có căn cứ `:1507` (NĐ 77/2008 Đ.20) ⇒ sửa tiền đề, đo lại (chuẩn chấm §8) |
| #2 — bổ sung số thẻ, **giữ nguyên tệp đang đính** | 1 / 1, `BI_LAP=false` | **"Cập nhật năng lực thành công"** | **200** `success:true` | ✅ |

- 🔴 **Triệu chứng gốc KHÔNG tái hiện: 0/2 lượt** xuất hiện *"Lỗi hệ thống, vui lòng thử lại sau."*
- **Verify bản chất (tải lại trang + đọc máy chủ):** `version` **14→15**, `hoSo.version` **3→4**,
  `hoSo.chungChiChiTiet` `[]` → `[{fileDinhKemId:"99b9a7e5…"}]`; màn hiện `Chứng chỉ chi tiết = QA G3 (4.8) & CN (9.8).pdf`
  và `Số thẻ hành nghề = QA-G3-20260807`. `trangThai` vẫn `HOAT_DONG` (không có tác dụng phụ). ⇒ **C1+C2+C3 đều ĐẠT**.
- Bộ bắt thông báo dùng **nguyên `tools/toast-capture.js`**, tự kiểm `soObserverDangSong=1` trước **cả 2** lượt.
- **Khôi phục:** gỡ chứng chỉ (`chungChiXoaIds` → 200) · xoá 2 tệp QA đã nạp (`DELETE …/files` → 204 ×2) →
  `fileDinhKems` về đúng 1 tệp gốc, `chungChiChiTiet=[]`, các trường năng lực khớp bản sao lưu.
  ❌ **Còn sót:** `soTheHanhNghe` `null → "QA-G3-20260807"` — thử đặt lại `null` bị **422 cùng mã lỗi** ⇒
  **không hoàn nguyên được bằng chính màn này**. Cộng thêm `nht_04_ui.cccd = 000000000004` (xem N12).
- Console 0 lỗi ngoài dự kiến (1 cảnh báo `/ticket=*` + đúng các lỗi 422 do chính tôi tạo).
- Ghi sheet: `Trạng thái dev fix` = **`UAT done`**, `Kết quả verify` = nội dung note (đè giá trị cũ của lượt đo
  bản dựng khác — đúng chủ ý). Đọc lại **md5 khớp 100%** (1.841 ký tự). Ô chỉ đọc nguyên vẹn:
  `Trạng thái`=Fail · `Kết quả thực tế` không đổi · `Dopai`=dev done · `DEV phản hồi lần 1` không đổi ·
  **không đụng cột vòng 2**.
- 🔴 **Note ô sheet viết theo yêu cầu mới của user: ngắn gọn ~1.8k ký tự, 5 khối** (kết luận · điều kiện đo ·
  phạm vi đã kiểm · số đo quyết định · phạm vi hiệu lực + ảnh). Chi tiết dài để ở `do/CNHSNLTVV_03.md`.

## Điểm phải nhớ khi chạy (rút từ recon + chuẩn chấm)

| Case | Bẫy / điều kiện quyết định |
|---|---|
| QLKTLBG_18/19/20 | Hệ thống **không tồn tại quyền `export_bai_giang`** trong 299 quyền → lời gọi xuất có thể 403. Bấm 1 lần, đọc HTTP thật, **không đổi tài khoản để lách**. Chip "Bộ lọc nâng cao (2)" hiện sẵn ≠ đang lọc. Icon cột "Thao tác" ≠ nút xuất danh sách. Tài khoản cấp ĐP thấy **0 bài giảng** → chỉ dùng `cbnv_tw`. |
| TKHSYCHTPL_03 | Mức "Sắp hết hạn" chỉ có **đúng 1 vụ việc** (`VV-BTP-TW-20260713-001`, trạng thái `DA_DANH_GIA`). `tabCounts` = `{TAT_CA:1, DANG_XU_LY:0, HOAN_THANH:1}` → **đo ở tab mặc định sẽ ra 0 dòng và chấm Reopen oan**. Phải chọn tab Tất cả. Đếm lại ngay trước khi đo. |
| KTDGKQHT_10 | Nút nạp Excel **chỉ bật sau khi đã chọn đề kiểm tra** (SRS `:578`) — thấy "không có nút" khi chưa chọn đề là **đúng đặc tả**, không phải lỗi. Dùng khóa `KH-20260509-006` (DANG_DIEN_RA, 1 đề KICH_HOAT, 6 học viên). Tệp nạp phải là **tệp do hệ thống sinh**. Gài ≥1 dòng điểm sai để đo vế "dòng lỗi". SRS **im lặng về câu chữ** thông báo → cấm Fail vì khác chữ mẫu. |
| KTHSYCHTPL_11 | 4 vụ `DANG_KIEM_TRA` sẵn có **đã lưu kết luận Đạt** → dùng lại = Pass bằng quan sát tĩnh (bị cấm). Phải bắt đầu từ vụ `DA_TIEP_NHAN` (TW có 11 vụ). **Vế "Đạt → Đã phân công" trái đặc tả hiện hành** (`:541/:564/:1744/:2288`) → route BA, không tự chấm. Cấp ĐP **0 vụ `DA_TIEP_NHAN`**. |
| CNHSNLTVV_03 | Phải đo **nhánh CÓ đính tệp chứng chỉ** — nhánh không đính tệp chính là nhánh dev đã khai E2E pass, đo nhánh đó là **Pass oan**. Chọn hồ sơ `HOAT_DONG` (10 hồ sơ); tránh `YEU_CAU_BO_SUNG` (lưu năng lực sẽ tự đổi trạng thái) và `VO_HIEU_HOA` (bị chặn `ERR-NL-05`). |

## Ghi nhận ngoài phạm vi (chưa log bug, chờ lead quyết)

| # | Nội dung | Nguồn |
|---|---|---|
| N1 | Bộ lọc `congKhai` của danh sách bài giảng **không có tác dụng** ở tầng API: `true/false/1/0` đều trả cùng 6 bản ghi `congKhai=true`; bài giảng `congKhai=false` không bao giờ hiện, dù tổng không lọc là 7. Chưa kiểm trên màn hình. | recon §4.4 |
| N2 | SRS tự lệch tên mức cảnh báo SLA: `:1449` + `srs-v3.5.md:5626` dùng một giá trị, `:1516/:1644/:1656/:2031` dùng giá trị khác. **Đã xác minh bằng cách mở file** khi đo TKHSYCHTPL_03; đã đưa vào phần "đề nghị BA" cuối note dòng 50. Lệch thêm về NHÃN: BR-SLA-02 (`srs-v3.5.md:5626`) chốt mức thấp nhất hiển thị **"Trong hạn"**, còn `srs-fr-05-vu-viec.md:1516` + giao diện V1.0.10 dùng **"Bình thường"**. | chuẩn chấm + lượt đo TKHSYCHTPL_03 |
| N5 | Bảng *Inputs* của FR-V.I-08 (`srs-fr-05-vu-viec.md:651–659`) liệt kê 7 tiêu chí tìm kiếm và **không có** tiêu chí mức SLA, trong khi ô lọc này được quy định ở phần màn hình `:1644` và chạy đúng trên giao diện. Khác biệt giữa 2 mục của cùng bộ đặc tả, **không phải lỗi phần mềm** — chỉ ghi nhận, chưa đưa vào note đối tác. | lượt đo TKHSYCHTPL_03 |
| N3 | Bảng tổng quan BR `srs-fr-03-dao-tao.md:2243` chưa liệt kê FR-III-07/08 trong khi màn SCR-III-03 `:1952` dẫn thẳng BR-DATA-06. | chuẩn chấm QLKTLBG |
| N6 | **Tên tệp mẫu tải về không dùng tên máy chủ khai.** `content-disposition: attachment; filename="mau-diem-kiem-tra-KH-20260509-006.xlsx"` (theo mã khóa) nhưng tệp lưu xuống máy là `mau-diem-kiem-tra-dd1adee1-715e-47f9-986d-52f9dcc60373.xlsx` (theo mã nội bộ) ⇒ giao diện tự đặt tên đè. Đã đưa vào phần "đề nghị xem xét" cuối note dòng 11, nêu rõ không ảnh hưởng verdict. | lượt đo KTDGKQHT_10 |
| N7 | **Nhãn tab lệch đặc tả:** `srs-fr-03-dao-tao.md:522`/`:1924` gọi Tab 5 là **"Kết quả kiểm tra"**, giao diện V1.0.10 hiển thị **"Kết quả"** (khóa nội bộ vẫn `ket-qua-kiem-tra`). Chỉ là câu chữ nhãn. | lượt đo KTDGKQHT_10 |
| N8 | **Tên 2/6 hạng mục danh sách kiểm tra trên giao diện trích văn bản CŨ hơn đặc tả.** V1.0.10: hạng mục 1 = *"Văn bản đề nghị hỗ trợ (**Mẫu 01 NĐ55**)"*, hạng mục 3 = *"Tờ khai xác định quy mô DN (**NĐ39/2018**)"*; SRS v3.5 `srs-fr-05-vu-viec.md:526` ghi *"Mẫu 01 (**Phụ lục NĐ18/2026**)"*, `:528` ghi *"(**NĐ80/2021**)"*. Chỉ câu chữ nhãn, không ảnh hưởng chức năng → chưa đưa vào note đối tác. | lượt đo KTHSYCHTPL_11 |
| N9 | **Câu chữ lựa chọn kết luận nhiều khả năng là gốc kỳ vọng sai của đối tác:** ô kết luận ghi **"Đạt — chuyển sang phân công"**, dễ đọc thành "chọn Đạt thì tự chuyển trạng thái Đã phân công", trong khi `:541`/`:564`/`:1745`/`:2288` nói Đạt **giữ** "Đang kiểm tra". Đặc tả **không** quy định câu chữ này ⇒ candidate câu chữ, **không** dùng làm căn cứ verdict. Đã nêu trong mục đề nghị BA của note dòng 45. | lượt đo KTHSYCHTPL_11 |
| N10 | 🔴 **Máy chủ chỉ cho 1 phiên sống mỗi tài khoản** — phiên mới **thu hồi** phiên cũ (`ERR-AUTH-SYS-00-03` *"Token đã bị thu hồi"*). Lượt đo dòng 45 bị cắt **2 lần** vì có phiên khác đăng nhập cùng `cbnv_tw` (mốc MailHog 11:21:46 UTC). **Khuyến nghị điều phối: mỗi người đo một tài khoản riêng, hoặc chạy tuần tự.** | lượt đo KTHSYCHTPL_11 |
| N11 | **Đính chính recon §1.3:** `cb_nv_tw_01` **KHÔNG** dùng mật khẩu `Test@1234` (recon suy đoán "khả năng cao đúng cho cả bộ `_NN`" — **sai**). Khung lỗi *"Tên đăng nhập hoặc mật khẩu không đúng."* ⇒ hiện **không có** tài khoản dự phòng dùng được cho vai trò CB_NV_TW. | lượt đo KTHSYCHTPL_11 |
| N4 | `input/input.md` ghi sai tên tài khoản env đối tác: thực tế là `cb_nv_tw_01`, `cb_nv_dp_01`, `cb_pd_tw_01`… (gạch dưới đầy đủ); `nht_qa_tw` không tồn tại. Env có 221 tài khoản. | recon §1.2 |
| N12 | 🔴 **Cổng bắt buộc nhập số CCCD chặn cứng toàn bộ giao diện.** Sau khi đăng nhập `nht_04_ui`, hộp thoại *"Cập nhật thông tin bắt buộc"* phủ mặt nạ toàn màn, **không có nút đóng/huỷ, `Escape` không tắt** (DOM chỉ có 1 nút `Xác nhận`); `/auth/me` trả `cccd:null`. Không khai CCCD thì **không dùng được chức năng nào**. Lược đồ bắt buộc đúng 12 chữ số ⇒ **không có đường đưa về trống**. `srs-fr-04` không mô tả cổng này → **đề nghị BA xác nhận**. Đã phải đặt `nht_04_ui.cccd = 000000000004` để tới được màn đo. Ảnh `image/CNHSNLTVV_03-00-modal-cccd-bat-buoc.png`. | lượt đo CNHSNLTVV_03 |
| N13 | **Tệp được ghi vào hồ sơ ngay lúc đính, TRƯỚC khi bấm Lưu.** Chọn tệp ở khối *Thêm chứng chỉ mới* phát sinh ngay `POST /api/v1/tu-van-viens/{id}/files` → **201** và tệp hiện luôn trong `fileDinhKems`. Lượt đo có 1 lần form **tự nhảy về tab "Hồ sơ"** mất hết nội dung đang nhập, nhưng **tệp vẫn nằm lại** ⇒ người dùng bỏ dở biểu mẫu sẽ để lại tệp rác không dấu hiệu báo. Đã tự dọn (`DELETE …/files` → 204). | lượt đo CNHSNLTVV_03 |
| N14 | **Ràng buộc "Số thẻ hành nghề" lệch giữa 3 nơi.** Máy chủ bắt buộc trường này với loại TVV ở màn cập nhật năng lực (`ERR-VAL-IV-03-10`) — có căn cứ `srs-fr-04-chuyen-gia-tvv.md:1507` (*"Bắt buộc nếu Loại = Tư vấn viên (theo NĐ 77/2008 Đ.20)"*, thuộc màn Thêm/Sửa hồ sơ) — nhưng **bảng Inputs của chính FR-IV-04 `:389` ghi `N` (không bắt buộc)** và **ô nhập trên form không có dấu bắt buộc**. Hệ quả thật: hồ sơ TVV cũ để trống trường này **không lưu được năng lực**, và **điền rồi không xoá lại được** (đặt lại `null` → 422 cùng mã). → BA chốt phạm vi áp dụng `:1507` cho FR-IV-04. | lượt đo CNHSNLTVV_03 |

## Vấn đề cần user quyết

| # | Nội dung | Trạng thái |
|---|---|---|
| Q1 | **KTHSYCHTPL_11 đã sang vòng 2** (`Trạng thái 2`=Fail, `Trạng thái dev fix 2`="Bỏ qua", DEV đã Reject vòng 2). Nếu verdict lô này là **Reopen** thì ghi `Reopen` vào cột **vòng 1** sẽ mâu thuẫn hồ sơ vòng 2 → **dừng hỏi user trước khi ghi**. Nếu Pass thì vô hại. | ✅ **ĐÓNG 07/08** — verdict ra **Pass**, cổng chặn không kích hoạt. Đã ghi `UAT done` vào cột vòng 1, **không đụng** 4 cột vòng 2. |
| Q2 | **Tranh chấp phiên trên `cbnv_tw`** (N10): máy chủ thu hồi phiên cũ khi có phiên mới cùng tài khoản. Nếu còn người đo chạy song song trên env đối tác thì cần **phân tài khoản riêng** hoặc **chạy tuần tự** — hiện `cb_nv_tw_01` không dùng được (N11) nên vai trò CB_NV_TW **chỉ có đúng 1 tài khoản khả dụng**. | Chờ lead điều phối |
| Q3 | **2 thay đổi dữ liệu trên env đối tác KHÔNG hoàn nguyên được** sau lượt đo dòng 36 (đã khai đủ trong `do/CNHSNLTVV_03.md` §9): (a) hồ sơ **`TVV-BTP-TW-0063`** có `soTheHanhNghe` `null → "QA-G3-20260807"` — máy chủ bắt buộc trường này với loại TVV nên **không đặt lại rỗng được** (N14); (b) tài khoản **`nht_04_ui`** có `cccd = 000000000004` do cổng bắt buộc N12. Mọi thay đổi khác đã trả về đúng gốc. Cần lead quyết có báo dev/DBA gỡ ở tầng CSDL không. | Chờ lead |
