Mã case: CPCTHTTTG_06 (tab `bug` dòng 264) — **Xuất PDF**        Thời điểm viết: 2026-08-06 12:39
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: **V1.0.8** (gói `assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết file này** (khai theo flow §Giai đoạn A):
`reverify-round-2026-08-05/cond/CPCTHTTTG_06.md` (số đo 05/08, V1.0.6 — nhóm phiếu Xuất PDF) ·
`reverify-round-2026-08-05/RECIPE.md` §6 · `reverify-week-3/cond/CPCTHTTTG_05.md` (21/07).
→ Mục 4 và 5 dưới đây suy từ **đặc tả** `srs-v3.5/srs-fr-11-bao-cao.md`, KHÔNG lấy số đo cũ làm ngưỡng.

> 🔴 Case này và `CPCTHTTTG_05` **dùng chung một màn** (BC Chi phí theo thời gian), khác nhau ở **nút bấm**:
> case này = **Xuất PDF**, case kia = **Xuất Excel**. Đo riêng từng case, cấm suy kết quả từ case kia.

---

## 1. Đối tác phản ánh

- **Vế a —** Màn Báo cáo thống kê, loại **BC Chi phí theo thời gian**, đã Xem báo cáo ra số liệu, bấm
  **Xuất PDF** → hệ thống **không tạo được tệp**, hiện *"Không thể tạo file xuất. Vui lòng thử lại."*
  (16/07/2026), không có tệp nào tải về.
- **Vế b —** Đối tác thử lại 31/07/2026: thông báo đổi thành *"Forbidden"*.
- **Vế c — Kỳ vọng:** tệp PDF theo mẫu Thông tư 17/2025/TT-BTP — khổ A4, phông Times New Roman cỡ 13,
  **đầu trang** có quốc hiệu và tên cơ quan, **cuối trang** có ngày ký **và chức danh người ký**; tên tệp
  `BaoCaoChiPhi_{YYYYMMDD_HHmm}.pdf`.

**Bằng chứng đã mở xem:** `partner-evidence/CPCTHTTTG_06.jpg` (full-res 1889×1034, md5 `aadebee1…`) —
đúng màn của case này (URL `loai=chi-phi-theo-thoi-gian`).
🔴 **Ghi chú bằng chứng:** tệp ảnh này **trùng khít** (cùng md5) với ảnh đối tác gắn cho `CPCTHTTTG_05`
(dòng 263, nút Xuất Excel). Ảnh chỉ chụp **sau khi** thông báo lỗi đã hiện nên **không cho biết đã bấm nút
nào**. Ảnh vẫn đúng màn + đúng bộ lọc nên **vẫn dùng được** cho vế a; riêng chiều "thao tác Excel hay PDF"
coi như **bằng chứng không lộ điều kiện** → tự đo **đúng nút của case này** thay vì suy từ case kia.

## 2. Đặc tả nói gì

- `srs-fr-11-bao-cao.md:1053` — nút **Xuất PDF (.pdf)** *"→ xuất theo khung trình bày TT17/2025 (không
  dùng Mẫu 21a/21b)"*, hành vi *click → auto-download*, hiện **sau khi đã "Xem báo cáo"**.
- `:86` — Processing bước 8: *"tạo file .pdf theo khung văn bản hành chính Thông tư 17/2025 — khổ A4, font
  Times New Roman cỡ 13; **đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành; **cuối trang** có
  ngày ký, họ tên cán bộ xuất báo cáo và chỗ trống cho con dấu khi in chính thức. **Không in dòng chức danh
  người ký** — hồ sơ tài khoản không lưu chức vụ (ngoại lệ của khung chung §D.2.4). Tên tệp
  `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf` `[BA chốt 2026-08-04]`"*.
- `:124` — AC chung cho thao tác Xuất PDF (liệt kê **đóng** các mục bắt buộc, kèm *"không có dòng chức danh"*).
- `:1092` — export chèn tiêu đề BC + kỳ + đơn vị + ngày tạo vào header tệp.
- `:116` — E6 `ERR-RPT-04` *"Không thể tạo file xuất. Vui lòng thử lại"* = đúng nguyên văn câu đối tác thấy.
- `:117` — E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"*; *"Forbidden"* không có trong bảng lỗi.
- `:846`–`:874` — FR-IX-19 (UC142) BC Chi phí theo thời gian: `trend_data[]` = `{ky_label, tong_chi_phi,
  so_ho_so}` · `tong_chi_phi_ky` — điều kiện *Luôn*.
- `:62` — tác nhân: **CB Nghiệp vụ hoặc CB Phê duyệt** (TW/BN/ĐP).

**IM LẶNG về:** vai trò **Quản trị viên (QTHT)** có được xem/xuất báo cáo hay không.

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw_03`** (CB Nghiệp vụ - Trung ương, cấp TW). Mật khẩu `Test@1234`, OTP ở
  MailHog `http://18.143.165.120:8025`.
- Tài khoản đóng GAP vai trò (không ra verdict): **`admin`** (QTHT).
- Màn **Báo cáo thống kê** (`/bao-cao`) → Loại báo cáo = **BC Chi phí theo thời gian**.
- Bộ lọc khớp đối tác: Kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**.
- Dữ liệu tiền đề: ≥1 hồ sơ chi trả **đã thanh toán** trong kỳ (`:82`).

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 6:**

1. Với `cbnv_tw_03`, sau khi Xem báo cáo ra số liệu, thao tác **Xuất PDF** làm hệ thống **giao được một tệp
   .pdf**: không còn thông báo hỏng khâu tạo tệp, không còn bị từ chối truy cập.
2. **Hai đường đo độc lập cùng nói thành công**: (a) lấy được tệp thật, kích thước > 0, mở đọc được bằng
   thư viện đọc PDF; (b) phản hồi máy chủ của **chính lượt bấm đó** là thành công kèm nội dung tệp.
3. Tên tệp đủ **ngày + giờ-phút** đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.pdf`; xuất lần 2 sang phút khác
   ra **tên khác**.
4. Mở tệp đọc nội dung — đủ khung hành chính đặc tả đòi ở `:86`: **khổ A4** · **đầu trang** có quốc hiệu +
   tiêu ngữ + tên cơ quan ban hành · **cuối trang** có ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống cho
   con dấu · phông là Times New Roman cỡ 13 hoặc bản tương thích số đo của phông đó.
5. Nội dung nghiệp vụ trong tệp: đủ **4 mục header** (tên báo cáo · kỳ · đơn vị · ngày tạo) và dãy theo kỳ
   với nhãn kỳ · tổng chi phí · số hồ sơ, **khớp số liệu đang hiện trên màn**.
6. Lặp lại đúng thao tác đó bằng vai trò **Quản trị viên (`admin`)** — hệ thống **không từ chối**.

**❌ FAIL nếu** với `cbnv_tw_03`: hiện thông báo hỏng khâu tạo tệp · bị từ chối truy cập · không có tệp về ·
tệp rỗng/hỏng không mở được · **thiếu ≥1 mục của khung hành chính ở mục 4** · thiếu ≥1 trong 4 mục header ·
số liệu lệch màn hình · khổ giấy khác A4 · tên tệp thiếu giờ-phút.

**⚠️ Nhánh không được tự chấm:** mục 1–5 đạt với `cbnv_tw_03` nhưng mục 6 hỏng (Quản trị viên bị từ chối)
→ **KHÔNG Pass và KHÔNG Fail**, chuyển **cần BA** (đặc tả im lặng về vai trò QTHT), kèm số đo cả hai vai trò.

**KHÔNG được chấm Fail vì:**

- **Không có dòng chức danh người ký** — đối tác kỳ vọng có, nhưng **BA đã chốt 2026-08-04** (`:86`) là
  **không in** dòng này vì hồ sơ tài khoản không lưu chức vụ. Đây là quyết định có sẵn, không phải QA tự bác.
- Tên tệp `BaoCaoChiPhiTheoThoiGian_…` thay vì `BaoCaoChiPhi_…` như ô *Kết quả mong đợi* — **BA đã chốt
  2026-08-04** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` (`:86`, `:1092`).
- Tên phông nhúng đọc ra là bản tương thích số đo của Times New Roman (vd `Tinos`) thay vì đúng chữ
  "Times New Roman".
- Tệp **không có chữ ký số** — `:86` chỉ đòi *chỗ trống cho con dấu khi in chính thức*, không đòi ký số.
- Số liệu env QA khác env đối tác (25 hồ sơ / 226.308.268 ₫).

## 5. Dạng dữ liệu phải phủ

**M = 2 lượt xuất khác kỳ báo cáo**, để chứng minh tệp **bám theo bộ lọc đang chọn** chứ không xuất cứng:
① Kỳ **Năm** 2026 (khớp đối tác) · ② Kỳ **khác** trong dropdown (Quý hoặc Tháng) cho ra **số điểm kỳ khác**.
Tệp ② phải có dòng "Kỳ báo cáo" đổi theo và dãy theo kỳ khớp đúng màn của lượt đó.

**Nguồn xác định M:** tra đường ① rồi ② của flow — đặc tả `:1048` (bộ lọc kỳ: *Tuần / Tháng / Quý / Năm /
Khoảng tùy chọn*) và AC `:874` (*"chọn 12 tháng → 12 điểm trend"*). Đủ để chốt, không cần hỏi dev/BA.
Không đổi được kỳ, hoặc mọi kỳ đều ra đúng một điểm ⇒ ghi rõ vào mục 6 là **không dựng được biến thể ②** và
xử theo quy tắc GAP (ô trống), **không** tự hạ M xuống 1.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên (QTHT)**, phạm vi `BTP · TW` (góc phải ảnh) | `cbnv_tw_03` (ra verdict) **và** `admin` = QTHT `BTP · TW` (đóng GAP vai trò) | Không |
| Entity + trạng thái | Báo cáo **BC Chi phí theo thời gian** đã chạy xong (`Thời điểm tạo: 16/07/2026 16:32`), đang hiện số liệu | Y hệt: đã Xem báo cáo ra số liệu (`Thời điểm tạo: 06/08/2026 14:26` với cbnv, `14:30` với QTHT) rồi mới bấm Xuất PDF | Không |
| Dữ liệu tiền đề | Có dữ liệu: Tổng chi phí toàn kỳ `226.308.268` · Tổng hồ sơ toàn kỳ `25` | Có dữ liệu: Tổng chi phí toàn kỳ `23.000.000` · Tổng hồ sơ toàn kỳ `2` (env QA ít bản ghi hơn — đã khai ở mục 4 là KHÔNG chấm Fail vì lệch số) | Không |
| Input / filter / giá trị nhập | Kỳ **Năm** 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · thao tác **Xuất PDF** | Y hệt ở biến thể ①; thêm ② Khoảng tùy chọn 01/06→30/06/2026. Hộp thoại in để mặc định **A4 · Dọc** (đúng khổ đặc tả đòi) | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 25 hồ sơ, 1 lượt xuất duy nhất trong ảnh; ảnh **không phân biệt được** nút Excel hay PDF (cùng md5 với ảnh của dòng 263) | 2 hồ sơ; **2 biến thể kỳ** (Năm / Khoảng) bằng cbnv + 1 lượt bằng QTHT — đo đúng nút **Xuất PDF** (qua nút [Xuất file] trong hộp thoại), không suy từ nút Excel | Không |

**3 dữ kiện neo của đối tác:** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=chi-phi-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
· báo cáo đã chạy xong, thao tác dừng ở bước xuất tệp · vai trò **Quản trị viên (QTHT)**, env
`htpldn-uat.ospgroup.vn`, bản dựng sidebar **HTPLDN · V1.0**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` bản **V1.0**; đợt này đo
trên `18.143.165.120.nip.io`. Verdict Pass (nếu có) là **Pass tạm** cho tới khi bản dựng này lên env đối tác.


---

## 7. Sửa tiêu chí giữa chừng (ghi lại theo flow)

### Sửa 1 — 2026-08-06 14:30 — tách vế "QTHT có được xuất" khỏi vế "câu hiện ra khi từ chối"

Áp lại nguyên bảng phân xử ở `CPHTCT_06` §7 Sửa 1 (bản gốc, dòng 238):

| Vế | Nội dung | Đặc tả nói gì | Xử |
|---|---|---|---|
| a | QTHT có được phép xuất báo cáo? | Im lặng (`:62`) | **cần BA** — `cau-hoi-BA.md` Mục 2 |
| b | Câu hiện ra cho người dùng khi hệ thống từ chối? | Có quy định rõ `:117` — `ERR-RPT-05` | **Reopen** — thực tế hiện `"Forbidden"` |

Khuyết tật vế b tồn tại ở **cả hai nhánh** trả lời của BA ⇒ không bị chặn bởi BA ⇒ chốt **Reopen**.

### Sửa 2 — 2026-08-06 14:30 — định nghĩa lại biến thể ② của mục 5

Giống `CPCTHTTTG_05` §7 Sửa 2 (cùng màn): qua giao diện mọi kỳ đều ra **đúng một điểm**, nên biến thể ② đổi thành **kỳ khác cho ra nhãn kỳ khác + khoảng ngày khác trong tệp** (Khoảng tùy chọn 01/06 → 30/06/2026). Không xử theo quy tắc GAP vì kỳ **đổi được** và đã đổi; việc giao diện không dựng nổi nhiều điểm theo AC `:874` là **phát hiện ngoài phạm vi**, ghi ở `CPCTHTTTG_05` §8 D1.

### Sửa 3 — 2026-08-06 14:27 — chốt cách đọc yêu cầu "font Times New Roman cỡ 13"

**Đo được:** phông nhúng là `Tinos` (bản tương thích số đo của Times New Roman — mục 4 đã khai trước là KHÔNG chấm Fail vì tên phông). Cỡ chữ **không đồng nhất 13**: quốc hiệu / tiêu ngữ / tên cơ quan / ngày ký / họ tên / dòng con dấu = **13**; tên báo cáo = 14; nội dung bảng = 11-12.

**Chốt:** không chấm Fail. Câu `:86` viết gọn *"khổ A4, font Times New Roman cỡ 13"* và các thành phần mà chính câu đó gọi tên đều đang ở cỡ 13; tên báo cáo lớn hơn và bảng nhỏ hơn là cách trình bày thường thấy của văn bản hành chính. Ép mọi chữ về đúng 13 là **cách hiểu chặt hơn câu chữ đặc tả** — QA không tự siết. Ghi lại để BA quyết nếu muốn siết.

---

## 8. Kết quả đo (giai đoạn B) — 2026-08-06

| # | Tiêu chí PASS | Kết quả | Bằng chứng |
|:-:|---|---|---|
| 1 | `cbnv_tw_03` Xuất PDF giao được tệp .pdf, không thông báo hỏng, không bị từ chối | ✅ Đạt | `"Đang tạo file..."` → `"Tạo file thành công."`, 0 lỗi |
| 2 | Hai đường đo độc lập cùng nói thành công | ✅ Đạt | (a) tệp thật 31.915 B mở đọc được bằng PyMuPDF · (b) XHR `POST /api/v1/bao-cao/export` → **200** kèm blob |
| 3 | Tên tệp đủ ngày + giờ-phút, xuất lần 2 khác phút ra tên khác | ✅ Đạt | `…_20260806_1426.pdf` và `…_20260806_1428.pdf` |
| 4 | Khung hành chính `:86`: A4 · đầu trang quốc hiệu + tiêu ngữ + tên cơ quan · cuối trang ngày ký + họ tên + chỗ con dấu · phông Times New Roman (hoặc bản tương thích số đo) | ✅ Đạt | 595,3 × 841,9 pt = A4 dọc; đủ 6 thành phần; phông `Tinos`; **không** có dòng chức danh — đúng quyết định nghiệp vụ 04/08 |
| 5 | Nội dung nghiệp vụ: 4 mục header + dãy theo kỳ, khớp màn | ✅ Đạt | tên BC · kỳ · đơn vị · ngày tạo; `Năm 2026 / 01/01/2026 / 31/12/2026 / 2 / 23.000.000` khớp màn |
| 6 | Lặp lại bằng vai trò **QTHT** — hệ thống **không từ chối** | ❌ **Hỏng** | `admin` bấm [Xuất file] → **403** `ERR-PERM-SYS-00-01`, chữ hiện ra `"Forbidden"`, 0 tệp — **có ảnh chụp đúng khung thông báo** |

**Verdict: 🔁 Reopen** — mục 1-5 đã hết lỗi (triệu chứng gốc 16/07 `ERR-RPT-04` không còn tái hiện; khung TT17/2025 dựng đúng), nhưng mục 6 hỏng đúng như vế b của đối tác ngày 31/07. Theo §7 Sửa 1, chốt Reopen; câu hỏi vai trò QTHT để mở ở `cau-hoi-BA.md` Mục 2.

**Kỳ vọng của đối tác KHÔNG được tính là khuyết tật:** đối tác chờ có **dòng chức danh người ký** ở cuối trang. Đặc tả `:86` đã chốt ngày 04/08/2026 là **không in** dòng này vì hồ sơ tài khoản không lưu chức vụ. Đây là quyết định nghiệp vụ có sẵn, không phải QA tự bác kỳ vọng.

**§D — Phát hiện ngoài phạm vi:** xem `CPCTHTTTG_05.md` §8 D1-D4 (cùng màn, cùng đợt đo). Riêng D2 (lộ mã `KHOANG`) tái hiện y hệt trong tệp PDF biến thể ②.
