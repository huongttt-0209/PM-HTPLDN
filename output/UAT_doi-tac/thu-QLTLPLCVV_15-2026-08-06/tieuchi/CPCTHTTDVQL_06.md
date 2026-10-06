Mã case: CPCTHTTDVQL_06 (tab `bug` dòng 243)        Thời điểm viết: 2026-08-06 12:39
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: **V1.0.8** (sidebar; gói `assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết file này** (khai theo flow §Giai đoạn A):
`reverify-week-3/cond/CPCTHTTDVQL_06.md` (số đo 21/07/2026, bản dựng cũ) ·
`reverify-round-2026-08-05/RECIPE.md` §6 (quy trình lấy tệp xuất, bản V1.0.6).
→ Mục 4 và 5 dưới đây suy từ **đặc tả** `srs-v3.5/srs-fr-11-bao-cao.md`, KHÔNG lấy số đo cũ làm ngưỡng.

---

## 1. Đối tác phản ánh

- **Vế a —** Màn Báo cáo thống kê, loại **BC Chi phí theo đơn vị**, đã Xem báo cáo ra số liệu, bấm
  **Xuất Excel** → hệ thống **không tạo được tệp**, hiện *"Không thể tạo file xuất. Vui lòng thử lại."*
  (16/07/2026), không có tệp nào tải về.
- **Vế b —** Đối tác thử lại 31/07/2026: thông báo đổi thành *"Forbidden"*.
- **Vế c — Kỳ vọng:** hệ thống xuất toàn bộ và tự động tải tệp về máy, tên tệp
  `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`.

**Bằng chứng đã mở xem:** `partner-evidence/CPCTHTTDVQL_06.jpg` (full-res 1907×1041, md5 `97084c43…`) —
đúng màn của case này (URL `loai=chi-phi-theo-don-vi`). Không có ảnh cho lần thử 31/07.

## 2. Đặc tả nói gì

- `srs-fr-11-bao-cao.md:1052` — nút **Xuất Excel (.xlsx)**, hành vi *click → auto-download*, hiện **sau
  khi đã "Xem báo cáo"**.
- `:85` — tạo .xlsx, tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`, giờ-phút bắt buộc `[BA chốt 2026-08-04]`.
- `:1092` — export chèn tiêu đề BC + kỳ + đơn vị + ngày tạo vào header tệp.
- `:123` — AC chung cho thao tác Xuất Excel.
- `:116` — E6 `ERR-RPT-04` *"Không thể tạo file xuất. Vui lòng thử lại"* = đúng nguyên văn câu đối tác thấy.
- `:117` — E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"*; chữ *"Forbidden"* không có trong bảng lỗi.
- `:731`–`:761` — FR-IX-16 (UC139) BC Chi phí theo đơn vị: cross-tab **hàng = đơn vị**, output đặc thù
  `don_vi_id` · `ten_don_vi` · `tong_chi_phi` · `so_ho_so` · `trung_binh` (cả 5 điều kiện *Luôn*);
  AC `:761`: *"CB TW tạo BC → cross-tab: hàng = đơn vị, cột = số HS + tổng CP + TB"*.
- `:62` — tác nhân: **CB Nghiệp vụ hoặc CB Phê duyệt** (TW/BN/ĐP).
- `:81` — phạm vi 2 tầng: TW thấy toàn quốc, BN/ĐP chỉ thấy đơn vị mình.

**IM LẶNG về:** vai trò **Quản trị viên (QTHT)** — vai trò đối tác dùng trong ảnh — có được xem/xuất báo
cáo hay không.

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw_03`** (CB Nghiệp vụ - Trung ương, cấp TW — để thấy phạm vi Toàn quốc
  theo `:81`). Mật khẩu `Test@1234`, OTP ở MailHog `http://18.143.165.120:8025`.
- Tài khoản đóng GAP vai trò (không ra verdict): **`admin`** (QTHT).
- Màn **Báo cáo thống kê** (`/bao-cao`) → Loại báo cáo = **BC Chi phí theo đơn vị**.
- Bộ lọc khớp đối tác: Kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**.
- Dữ liệu tiền đề: ≥1 hồ sơ chi trả **đã thanh toán** trong kỳ (`:82`).

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 5:**

1. Với `cbnv_tw_03`, sau khi Xem báo cáo ra số liệu, thao tác **Xuất Excel** làm hệ thống **giao được một
   tệp .xlsx**: không còn thông báo hỏng khâu tạo tệp, không còn bị từ chối truy cập.
2. **Hai đường đo độc lập cùng nói thành công**: (a) lấy được tệp thật, kích thước > 0, mở đọc được bằng
   thư viện đọc .xlsx; (b) phản hồi máy chủ của **chính lượt bấm đó** là thành công kèm nội dung tệp.
3. Tên tệp đủ **ngày + giờ-phút** đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`; xuất lần 2 sang phút khác
   ra **tên khác**.
4. Mở tệp đọc nội dung: đủ **4 mục header** (tên báo cáo · kỳ · đơn vị · ngày tạo) **và** bảng bên trong
   là cross-tab **hàng = đơn vị** với đủ các cột đặc tả đòi (tên đơn vị · số hồ sơ · tổng chi phí · trung
   bình), **số dòng và số liệu khớp bảng đang hiện trên màn** — không thiếu đơn vị nào.
5. Lặp lại đúng thao tác đó bằng vai trò **Quản trị viên (`admin`)** — hệ thống **không từ chối**.

**❌ FAIL nếu** với `cbnv_tw_03`: hiện thông báo hỏng khâu tạo tệp · bị từ chối truy cập · không có tệp về ·
tệp rỗng/hỏng · thiếu ≥1 trong 4 mục header · thiếu cột mà đặc tả đòi · **thiếu dòng đơn vị** so với màn ·
số liệu lệch màn hình · tên tệp thiếu giờ-phút.

**⚠️ Nhánh không được tự chấm:** mục 1–4 đạt với `cbnv_tw_03` nhưng mục 5 hỏng (Quản trị viên bị từ chối)
→ **KHÔNG Pass và KHÔNG Fail**, chuyển **cần BA** (đặc tả im lặng về vai trò QTHT), kèm số đo cả hai vai trò.

**KHÔNG được chấm Fail vì:**

- Tên tệp `BaoCaoChiPhiTheoDonVi_…` thay vì `BaoCaoChiPhi_…` như ô *Kết quả mong đợi* của đối tác — **BA đã
  chốt 2026-08-04** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`, `{TenBaoCao}` là tên loại báo cáo PascalCase.
- Số liệu env QA khác env đối tác (25 hồ sơ / 226.308.268 ₫).
- Chỉ có **một** đơn vị xuất hiện trong bảng nếu env chỉ có chi phí ở một đơn vị — đó là **dữ liệu**, không
  phải lỗi cross-tab; điều phải đúng là tệp **khớp** màn hình.
- Tên phông nhúng đọc ra không đúng chữ "Times New Roman" nhưng là bản tương thích số đo (vd `Tinos`).

## 5. Dạng dữ liệu phải phủ

**M = 2 lượt xuất khác bộ lọc**, để chứng minh tệp **bám theo bộ lọc đang chọn** chứ không xuất cứng:
① Đơn vị = **Toàn quốc** (khớp đối tác) · ② Đơn vị = **một đơn vị cụ thể** chọn trong dropdown Đơn vị.
Tệp ② phải có ô "Đơn vị" ở header và bộ dòng **hẹp hơn hoặc bằng** tệp ①, khớp đúng màn của lượt đó.

**Nguồn xác định M:** tra đường ② của flow — bộ lọc trên chính màn đó (`:1049` dropdown Đơn vị: *"TW:
'Toàn quốc' + chọn BN/ĐP bất kỳ"*). Đủ để chốt, không cần hỏi dev/BA.
Dropdown Đơn vị chỉ có đúng một lựa chọn ⇒ ghi rõ vào mục 6 là **không dựng được biến thể ②** và xử theo
quy tắc GAP (ô trống), **không** tự hạ M xuống 1.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên (QTHT)**, phạm vi `BTP · TW` (góc phải ảnh) | Đo **cả hai**: `cbnv_tw_03` (CB Nghiệp vụ TW — tác nhân `:62`, dùng ra verdict) **và** `admin` (QTHT, `BTP · TW` — đúng vai trò trong ảnh) | Không |
| Entity + trạng thái | Báo cáo **BC Chi phí theo đơn vị** đã chạy xong (`Thời điểm tạo: 16/07/2026 16:19`), đang hiện số liệu | Cùng loại báo cáo, đã Xem báo cáo xong đang hiện số liệu — `Thời điểm tạo 06/08/2026 13:34` / `13:36` (cbnv) và `13:38` / `13:41` (QTHT) | Không |
| Dữ liệu tiền đề | Có dữ liệu: Tổng hồ sơ `25` · Tổng chi phí `226.308.268` | Có dữ liệu: Tổng hồ sơ `2` · Tổng chi phí `23.000.000` · TB `11.500.000` — khác **số**, cùng **loại tình huống** | Không |
| Input / filter / giá trị nhập | Kỳ **Năm** 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · thao tác **Xuất Excel** | Y hệt, kể cả chuỗi tham số trên thanh địa chỉ `?loai=chi-phi-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 25 hồ sơ; ảnh dừng ở thông báo lỗi nên không rõ tệp có mấy dòng đơn vị | Dựng đủ **M = 2**: ① Đơn vị **Toàn quốc** · ② Đơn vị **Cục Bổ trợ tư pháp - Bộ Tư pháp**. Hai tệp khác md5, dòng header tệp đổi theo đúng đơn vị đang lọc | Không |

**3 dữ kiện neo của đối tác:** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=chi-phi-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
· báo cáo đã chạy xong, thao tác dừng ở bước xuất tệp · vai trò **Quản trị viên (QTHT)**, env
`htpldn-uat.ospgroup.vn`, bản dựng sidebar **HTPLDN · V1.0**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` bản **V1.0**; đợt này đo
trên `18.143.165.120.nip.io` bản **V1.0.8**. Verdict chỉ có hiệu lực cho env + bản dựng đã ghi.

---

## 7. Sửa tiêu chí giữa chừng (ghi theo flow — có mốc giờ + lý do)

### Sửa 1 — 2026-08-06 13:45, sau khi đo xong cả hai vai trò

Áp dụng **y hệt** cách xử đã ghi ở [`CPHTCT_06.md`](CPHTCT_06.md) § 7 Sửa 1: tách nhánh ⚠️ ở mục 4 thành
hai vế — vế *"QTHT có được phép xuất không"* (đặc tả **im lặng** → **cần BA**, câu hỏi đã có ở
`cau-hoi-BA.md` Mục 2) và vế *"câu hiện cho người dùng khi bị từ chối"* (đặc tả **quy định rõ** ở `:117`
→ **Reopen**). Phép thử quyết định: khuyết tật vế sau tồn tại ở **cả hai nhánh trả lời của BA**, nên không
bị chặn bởi BA. **Không** hạ chuẩn bất kỳ điều kiện PASS nào ở mục 4.

## 8. Số đo thực tế (giai đoạn B)

| Vai trò | Xem báo cáo | Bấm Xuất Excel | Câu người dùng thấy | Tệp giao ra |
|---|---|---|---|---|
| `cbnv_tw_03` — biến thể ① Toàn quốc | `GET /bao-cao/chi-phi-theo-don-vi` → **200** | `POST /bao-cao/export` → **200** | *"Đang tạo file..."* → *"Tạo file thành công."* | `BaoCaoChiPhiTheoDonVi_20260806_1335.xlsx` — 6 676 B, md5 `710b2bfb…` |
| `cbnv_tw_03` — biến thể ② Cục Bổ trợ tư pháp | **200** | **200** | *"Tạo file thành công."* | `BaoCaoChiPhiTheoDonVi_20260806_1336.xlsx` — 6 670 B, md5 `6cb0acf8…` |
| `admin` (QTHT — vai trò của đối tác) | **200**, ra **đúng số liệu đó** | **403** `ERR-PERM-SYS-00-01` | **`Forbidden`** (hiện ở mốc 605 ms, khung `x=657 y=3..16 w=118 h=40`, sống ~3,3 s) | **0 tệp**, **0 blob** |

- Mục 1 ✅ · mục 2 ✅ (tệp thật mở bằng `openpyxl` + phản hồi 200 của **chính lượt bấm đó**) · mục 3 ✅
  (`…_1335` vs `…_1336` — tên khác, không đè tệp) · mục 4 ✅ (đủ 4 mục header; bảng chéo **hàng = đơn vị**
  đủ 4 cột *Đơn vị · Số hồ sơ · Tổng chi phí · Trung bình chi phí*; số khớp màn từng con số) · **mục 5 ❌**.
- **Bằng chứng tệp bám bộ lọc:** dòng header tệp ① ghi `Đơn vị: Toàn quốc`, tệp ② ghi `Đơn vị: Cục Bổ trợ
  tư pháp - Bộ Tư pháp`, md5 hai tệp khác nhau ⇒ tệp xuất theo bộ lọc đang chọn, không xuất cứng.
- Triệu chứng gốc `ERR-RPT-04` (16/07) **không còn tái hiện**. Triệu chứng 31/07 *"Forbidden"* **tái hiện
  nguyên vẹn**, đo **3 lượt** (13:38 qua giao diện · 13:40 gọi thẳng máy chủ · 13:41 qua giao diện).

**→ Verdict: Reopen** (theo mục 7 Sửa 1), kèm câu hỏi BA cho vế phân quyền.

## 9. Hiện tượng lạ — đã thử tái hiện nhưng KHÔNG lặp lại (không log bug, không kéo verdict)

Ở lượt đo đầu của vai trò QTHT: cú xuất thứ nhất trả **403** (`reqid 211`), cú xuất thứ hai ~1 phút sau trả
**401** (`reqid 213`), FE tự gọi `POST /auth/logout` (`reqid 214`) rồi đá về `/login` kèm chữ *"Phiên làm
việc hết hạn"* — trong khi phiên mới đăng nhập được ~2 phút.

**Đã thử tái hiện 2 đường, đều KHÔNG lặp lại:**
1. Gọi thẳng máy chủ: lành tính → **200**; xem báo cáo → **200**; xuất → **403**; lành tính lại → **200**;
   xem báo cáo lại → **200**. ⇒ cú 403 **không** giết phiên.
2. Bấm trên giao diện: sau khi bấm Xuất và nhận *"Forbidden"*, kho lưu phiên `auth-store` **không đổi**
   (231 ký tự trước và sau), gọi lành tính ngay sau đó → **200**.

⇒ Không đủ căn cứ quy cho thao tác xuất. Ghi lại kèm số hiệu request để nếu vòng sau gặp lại thì có mốc
đối chiếu. **Không** log thành lỗi, **không** tính vào verdict case này.
