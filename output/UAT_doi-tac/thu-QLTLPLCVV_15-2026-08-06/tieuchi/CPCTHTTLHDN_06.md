Mã case: CPCTHTTLHDN_06 (tab `bug` dòng 258)        Thời điểm viết: 2026-08-06 12:39
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: **V1.0.8** (sidebar; gói `assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết file này** (khai theo flow §Giai đoạn A):
`reverify-week-3/cond/CPCTHTTLHDN_06.md` (số đo 21/07/2026, bản dựng cũ) ·
`reverify-round-2026-08-05/RECIPE.md` §6 (quy trình lấy tệp xuất, bản V1.0.6).
→ Mục 4 và 5 dưới đây suy từ **đặc tả** `srs-v3.5/srs-fr-11-bao-cao.md`, KHÔNG lấy số đo cũ làm ngưỡng.

---

## 1. Đối tác phản ánh

- **Vế a —** Màn Báo cáo thống kê, loại **BC Chi phí theo loại hình DN**, đã Xem báo cáo ra số liệu, bấm
  **Xuất Excel** → hệ thống **không tạo được tệp**, hiện *"Không thể tạo file xuất. Vui lòng thử lại."*
  (16/07/2026), không có tệp nào tải về.
- **Vế b —** Đối tác thử lại 31/07/2026: thông báo đổi thành *"Forbidden"*.
- **Vế c — Kỳ vọng:** hệ thống xuất toàn bộ và tự động tải tệp về máy, tên tệp
  `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`.

**Bằng chứng đã mở xem:** `partner-evidence/CPCTHTTLHDN_06.jpg` (full-res 1902×1031, md5 `ffd86f3a…`) —
đúng màn của case này (URL `loai=chi-phi-theo-loai-dn`), ô **Loại DN** để trống (*"Chọn Loại DN"*). Không
có ảnh cho lần thử 31/07.

## 2. Đặc tả nói gì

- `srs-fr-11-bao-cao.md:1052` — nút **Xuất Excel (.xlsx)**, hành vi *click → auto-download*, hiện **sau
  khi đã "Xem báo cáo"**.
- `:85` — tạo .xlsx, tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`, giờ-phút bắt buộc `[BA chốt 2026-08-04]`.
- `:1092` — export chèn tiêu đề BC + kỳ + đơn vị + ngày tạo vào header tệp.
- `:116` — E6 `ERR-RPT-04` *"Không thể tạo file xuất. Vui lòng thử lại"* = đúng nguyên văn câu đối tác thấy.
- `:117` — E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"*; *"Forbidden"* không có trong bảng lỗi.
- `:804`–`:842` — FR-IX-18 (UC141) BC Chi phí theo loại hình DN: **input đặc thù** `loai_dn` (không bắt
  buộc, ràng buộc **`SIEU_NHO / NHO / VUA`**, `:823`); **output đặc thù 7 cột** `loai_dn` · `ten_loai_dn`
  (Siêu nhỏ/Nhỏ/Vừa) · `muc_ho_tro` (100%/30%/10%) · `so_ho_so` · `tong_chi_phi` · `tran_chi_phi` (trần
  theo NĐ55) · `chenh_lech` — **cả 7 điều kiện *Luôn*** (`:831-839`).
- `:62` — tác nhân: **CB Nghiệp vụ hoặc CB Phê duyệt** (TW/BN/ĐP).

**IM LẶNG về:** vai trò **Quản trị viên (QTHT)** có được xem/xuất báo cáo hay không.

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw_03`** (CB Nghiệp vụ - Trung ương, cấp TW). Mật khẩu `Test@1234`, OTP ở
  MailHog `http://18.143.165.120:8025`.
- Tài khoản đóng GAP vai trò (không ra verdict): **`admin`** (QTHT).
- Màn **Báo cáo thống kê** (`/bao-cao`) → Loại báo cáo = **BC Chi phí theo loại hình DN**.
- Bộ lọc khớp đối tác: Kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, **Loại DN để trống**.
- Dữ liệu tiền đề: ≥1 hồ sơ chi trả **đã thanh toán** trong kỳ (`:82`).

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 5:**

1. Với `cbnv_tw_03`, sau khi Xem báo cáo ra số liệu, thao tác **Xuất Excel** làm hệ thống **giao được một
   tệp .xlsx**: không còn thông báo hỏng khâu tạo tệp, không còn bị từ chối truy cập.
2. **Hai đường đo độc lập cùng nói thành công**: (a) lấy được tệp thật, kích thước > 0, mở đọc được bằng
   thư viện đọc .xlsx; (b) phản hồi máy chủ của **chính lượt bấm đó** là thành công kèm nội dung tệp.
3. Tên tệp đủ **ngày + giờ-phút** đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`; xuất lần 2 sang phút khác
   ra **tên khác**.
4. Mở tệp đọc nội dung: đủ **4 mục header** (tên báo cáo · kỳ · đơn vị · ngày tạo) **và** bảng có đủ **7
   thông tin đặc tả đòi ở `:831-839`** (loại DN · tên loại DN · mức hỗ trợ · số hồ sơ · tổng chi phí · trần
   chi phí · chênh lệch), **số dòng và số liệu khớp bảng đang hiện trên màn**.
5. Lặp lại đúng thao tác đó bằng vai trò **Quản trị viên (`admin`)** — hệ thống **không từ chối**.

**❌ FAIL nếu** với `cbnv_tw_03`: hiện thông báo hỏng khâu tạo tệp · bị từ chối truy cập · không có tệp về ·
tệp rỗng/hỏng · thiếu ≥1 trong 4 mục header · **thiếu ≥1 trong 7 thông tin** đặc tả đòi · thiếu dòng so với
màn · số liệu lệch màn hình · tên tệp thiếu giờ-phút.

**⚠️ Nhánh không được tự chấm:** mục 1–4 đạt với `cbnv_tw_03` nhưng mục 5 hỏng (Quản trị viên bị từ chối)
→ **KHÔNG Pass và KHÔNG Fail**, chuyển **cần BA** (đặc tả im lặng về vai trò QTHT), kèm số đo cả hai vai trò.

**KHÔNG được chấm Fail vì:**

- Tên tệp `BaoCaoChiPhiTheoLoaiHinhDN_…` thay vì `BaoCaoChiPhi_…` như ô *Kết quả mong đợi* của đối tác —
  **BA đã chốt 2026-08-04** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`.
- Số liệu env QA khác env đối tác (25 hồ sơ / 226.308.268 ₫).
- Bảng chỉ hiện **một** loại DN nếu env chỉ có hồ sơ của một quy mô DN — đó là **dữ liệu**; điều phải đúng
  là tệp **khớp** màn hình và vẫn đủ 7 thông tin của dòng đó.
- Cột chênh lệch mang giá trị âm (tổng chi phí chưa chạm trần NĐ55) — đúng công thức `:839`.
- Tên phông nhúng đọc ra không đúng chữ "Times New Roman" nhưng là bản tương thích số đo (vd `Tinos`).

## 5. Dạng dữ liệu phải phủ

**M = 2 lượt xuất khác bộ lọc**, để chứng minh tệp **bám theo bộ lọc đang chọn**:
① **Loại DN để trống** (mọi loại — khớp đúng ảnh đối tác) · ② **chọn 1 giá trị cụ thể** trong ô Loại DN
(Siêu nhỏ / Nhỏ / Vừa — enum đặc tả `:823`). Tệp ② phải chỉ còn dòng của loại DN đã chọn, khớp màn lượt đó.

**Nguồn xác định M:** tra đường ① của flow — đặc tả `:819-823` khai đúng ô lọc `loai_dn` với 3 giá trị, và
`:1050` khai bộ lọc đặc thù của màn. Đủ để chốt, không cần hỏi dev/BA.
Ô Loại DN không có giá trị nào chọn được, hoặc chọn xong bảng rỗng ở **mọi** giá trị ⇒ ghi rõ vào mục 6 là
**không dựng được biến thể ②** và xử theo quy tắc GAP (ô trống), **không** tự hạ M xuống 1.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên (QTHT)**, phạm vi `BTP · TW` (góc phải ảnh) | Đo **cả hai**: `cbnv_tw_03` (CB Nghiệp vụ TW — tác nhân `:62`, dùng ra verdict) **và** `admin` (QTHT, `BTP · TW` — đúng vai trò trong ảnh) | Không |
| Entity + trạng thái | Báo cáo **BC Chi phí theo loại hình DN** đã chạy xong (`Thời điểm tạo: 16/07/2026 16:25`), đang hiện số liệu | Cùng loại báo cáo, đã Xem báo cáo xong đang hiện số liệu — đo lúc 13:52/13:53 (cbnv) và 13:55 (QTHT) | Không |
| Dữ liệu tiền đề | Có dữ liệu: Tổng hồ sơ `25` · Tổng chi phí `226.308.268` | Có dữ liệu: Tổng số hồ sơ `2` · Tổng chi phí `23.000.000`, thuộc quy mô **Siêu nhỏ** — khác **số**, cùng **loại tình huống** | Không |
| Input / filter / giá trị nhập | Kỳ **Năm** 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · **Loại DN để trống** · thao tác **Xuất Excel** | Y hệt, kể cả chuỗi tham số `?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 25 hồ sơ; ảnh dừng ở thông báo lỗi nên không rõ tệp có mấy dòng loại DN | Dựng đủ **M = 2** và thêm 1 biến thể kiểm chứng: ① Loại DN **để trống** · ② **Siêu nhỏ** (`fd_loaiDn=SIEU_NHO`) · ③ **Nhỏ** (`fd_loaiDn=NHO`) → màn rỗng, nút Xuất tự tắt | Không |

**3 dữ kiện neo của đối tác:** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
· báo cáo đã chạy xong, thao tác dừng ở bước xuất tệp · vai trò **Quản trị viên (QTHT)**, env
`htpldn-uat.ospgroup.vn`, bản dựng sidebar **HTPLDN · V1.0**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` bản **V1.0**; đợt này đo
trên `18.143.165.120.nip.io` bản **V1.0.8**. Verdict chỉ có hiệu lực cho env + bản dựng đã ghi.

---

## 7. Sửa tiêu chí giữa chừng (ghi theo flow — có mốc giờ + lý do)

### Sửa 1 — 2026-08-06 13:58, sau khi đo xong cả hai vai trò

Áp dụng **y hệt** cách xử đã ghi ở [`CPHTCT_06.md`](CPHTCT_06.md) § 7 Sửa 1: tách nhánh ⚠️ ở mục 4 thành hai
vế — *"QTHT có được phép xuất không"* (đặc tả **im lặng** → **cần BA**, đã có câu hỏi ở `cau-hoi-BA.md`
Mục 2) và *"câu hiện cho người dùng khi bị từ chối"* (đặc tả **quy định rõ** ở `:117` → **Reopen**). Phép thử
quyết định: khuyết tật vế sau tồn tại ở **cả hai nhánh trả lời của BA**. **Không** hạ chuẩn điều kiện PASS nào.

## 8. Số đo thực tế (giai đoạn B)

**Màn hình sau [Xem báo cáo]** — bảng có **đủ 7 cột** đặc tả `:831-839` đòi:
`Quy mô DN · Số hồ sơ · Tổng chi phí · Mức hỗ trợ (%) · Trần / hồ sơ · Trần chi phí · Chênh lệch`;
dòng duy nhất `Siêu nhỏ | 2 | 23.000.000 ₫ | 100,0 | 30.000.000 ₫ | 60.000.000 ₫ | -37.000.000 ₫`.
Chênh lệch âm khớp công thức `:839` (23.000.000 − 60.000.000), đúng mục *KHÔNG được chấm Fail vì*.

| Vai trò / biến thể | Xem báo cáo | Bấm Xuất Excel | Câu người dùng thấy | Tệp giao ra |
|---|---|---|---|---|
| `cbnv_tw_03` ① Loại DN để trống | **200** | **200** | *"Đang tạo file..."* → *"Tạo file thành công."* | `BaoCaoChiPhiTheoLoaiDn_20260806_1352.xlsx` — 6 774 B, md5 `01cca4cf…` |
| `cbnv_tw_03` ② Loại DN = Siêu nhỏ | **200** | **200** | *"Tạo file thành công."* | `BaoCaoChiPhiTheoLoaiDn_20260806_1353.xlsx` — 6 775 B, md5 `57ced0ca…` |
| `cbnv_tw_03` ③ Loại DN = Nhỏ | **200**, màn **rỗng** (không có bảng, có chữ báo trống) | nút Xuất **tự tắt** | — | không có (đúng, vì không có dữ liệu) |
| `admin` (QTHT — vai trò của đối tác) | **200**, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | **`Forbidden`** (hiện ở mốc 151 ms, khung `w=118 h=40`, tắt ở 3 478 ms) | **0 tệp**, **0 blob** |

- Mục 1 ✅ · mục 2 ✅ · mục 3 ✅ (`…_1352` vs `…_1353` — tên khác) · mục 4 ✅ (đủ 4 mục header; bảng trong
  tệp có **đủ 7 cột** `Quy mô DN · Số hồ sơ · Tổng chi phí (₫) · Mức hỗ trợ (%) · Trần / hồ sơ (₫) · Trần chi
  phí (₫) · Chênh lệch (₫)`, số khớp màn từng con số) · **mục 5 ❌**.
- **Nói thẳng về giới hạn của phép đo bám-bộ-lọc:** env chỉ có dữ liệu quy mô *Siêu nhỏ*, nên tệp ① và ② có
  **nội dung trùng nhau** (khác tên, khác md5 do dấu thời gian bên trong). Cặp ①–② vì thế **không** tự chứng
  minh tệp bám bộ lọc. Điều chứng minh được là biến thể ③: chọn *Nhỏ* thì màn rỗng và nút Xuất tự tắt ⇒ bộ
  lọc có tác dụng thật ở tầng dựng báo cáo, và tệp xuất khớp màn ở mọi lượt đo được.
- Triệu chứng gốc `ERR-RPT-04` (16/07) **không còn tái hiện**. Triệu chứng 31/07 *"Forbidden"* **tái hiện
  nguyên vẹn** ở đúng vai trò đối tác đã dùng.

**→ Verdict: Reopen** (theo mục 7 Sửa 1), kèm câu hỏi BA cho vế phân quyền.
