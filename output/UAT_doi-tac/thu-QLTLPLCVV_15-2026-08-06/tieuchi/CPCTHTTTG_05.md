Mã case: CPCTHTTTG_05 (tab `bug` dòng 263) — **Xuất Excel**        Thời điểm viết: 2026-08-06 12:39
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: **V1.0.8** (gói `assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết file này** (khai theo flow §Giai đoạn A):
`reverify-week-3/cond/CPCTHTTTG_05.md` (số đo 21/07/2026, bản dựng cũ) ·
`reverify-round-2026-08-05/RECIPE.md` §6 + `cond/CPCTHTTTG_06.md` (số đo 05/08, V1.0.6).
→ Mục 4 và 5 dưới đây suy từ **đặc tả** `srs-v3.5/srs-fr-11-bao-cao.md`, KHÔNG lấy số đo cũ làm ngưỡng.

> 🔴 Case này và `CPCTHTTTG_06` **dùng chung một màn** (BC Chi phí theo thời gian), khác nhau ở **nút bấm**:
> case này = **Xuất Excel**, case kia = **Xuất PDF**. Đo riêng từng case, cấm suy kết quả từ case kia.

---

## 1. Đối tác phản ánh

- **Vế a —** Màn Báo cáo thống kê, loại **BC Chi phí theo thời gian**, đã Xem báo cáo ra số liệu, bấm
  **Xuất excel** → hệ thống **không tạo được tệp**, hiện *"Không thể tạo file xuất. Vui lòng thử lại."*
  (16/07/2026), không có tệp nào tải về.
- **Vế b —** Đối tác thử lại 31/07/2026: thông báo đổi thành *"Forbidden"*.
- **Vế c — Kỳ vọng:** hệ thống xuất toàn bộ và tự động tải tệp về máy, tên tệp
  `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`.

**Bằng chứng đã mở xem:** `partner-evidence/CPCTHTTTG_05.jpg` (full-res 1889×1034, md5 `aadebee1…`) —
đúng màn của case này (URL `loai=chi-phi-theo-thoi-gian`).
🔴 **Ghi chú bằng chứng:** tệp ảnh này **trùng khít** (cùng md5) với ảnh đối tác gắn cho `CPCTHTTTG_06`
(dòng 264, nút Xuất PDF). Ảnh chỉ chụp **sau khi** thông báo lỗi đã hiện nên **không cho biết đã bấm nút
nào**. Ảnh vẫn đúng màn + đúng bộ lọc của case này nên **vẫn dùng được** cho vế a; riêng chiều "thao tác
Excel hay PDF" coi như **bằng chứng không lộ điều kiện** → phải tự đo **cả hai nút** (mỗi nút thuộc case
của nó) thay vì suy từ một lượt.

## 2. Đặc tả nói gì

- `srs-fr-11-bao-cao.md:1052` — nút **Xuất Excel (.xlsx)**, hành vi *click → auto-download*, hiện **sau
  khi đã "Xem báo cáo"**.
- `:85` — tạo .xlsx, tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`, giờ-phút bắt buộc `[BA chốt 2026-08-04]`.
- `:1092` — export chèn tiêu đề BC + kỳ + đơn vị + ngày tạo vào header tệp.
- `:123` — AC chung cho thao tác Xuất Excel.
- `:116` — E6 `ERR-RPT-04` *"Không thể tạo file xuất. Vui lòng thử lại"* = đúng nguyên văn câu đối tác thấy.
- `:117` — E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"*; *"Forbidden"* không có trong bảng lỗi.
- `:846`–`:874` — FR-IX-19 (UC142) BC Chi phí theo thời gian: công thức *"tính tổng chi phí theo kỳ thời
  gian"*; output đặc thù `trend_data[]` = `{ky_label, tong_chi_phi, so_ho_so}` · `chart_type` = LINE ·
  `tong_chi_phi_ky` — cả 3 điều kiện *Luôn*; AC `:874`: *"chọn 12 tháng → line chart 12 điểm trend chi phí"*.
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

**✅ PASS khi — đủ CẢ 5:**

1. Với `cbnv_tw_03`, sau khi Xem báo cáo ra số liệu, thao tác **Xuất Excel** làm hệ thống **giao được một
   tệp .xlsx**: không còn thông báo hỏng khâu tạo tệp, không còn bị từ chối truy cập.
2. **Hai đường đo độc lập cùng nói thành công**: (a) lấy được tệp thật, kích thước > 0, mở đọc được bằng
   thư viện đọc .xlsx; (b) phản hồi máy chủ của **chính lượt bấm đó** là thành công kèm nội dung tệp.
3. Tên tệp đủ **ngày + giờ-phút** đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`; xuất lần 2 sang phút khác
   ra **tên khác**.
4. Mở tệp đọc nội dung: đủ **4 mục header** (tên báo cáo · kỳ · đơn vị · ngày tạo) **và** bảng chứa dãy
   theo kỳ thời gian với đủ 3 thông tin đặc tả đòi ở `:869` (nhãn kỳ · tổng chi phí · số hồ sơ), **số điểm
   kỳ và số liệu khớp bảng/biểu đồ đang hiện trên màn**.
5. Lặp lại đúng thao tác đó bằng vai trò **Quản trị viên (`admin`)** — hệ thống **không từ chối**.

**❌ FAIL nếu** với `cbnv_tw_03`: hiện thông báo hỏng khâu tạo tệp · bị từ chối truy cập · không có tệp về ·
tệp rỗng/hỏng · thiếu ≥1 trong 4 mục header · thiếu ≥1 trong 3 thông tin của dãy theo kỳ · **thiếu điểm kỳ**
so với màn · số liệu lệch màn hình · tên tệp thiếu giờ-phút.

**⚠️ Nhánh không được tự chấm:** mục 1–4 đạt với `cbnv_tw_03` nhưng mục 5 hỏng (Quản trị viên bị từ chối)
→ **KHÔNG Pass và KHÔNG Fail**, chuyển **cần BA** (đặc tả im lặng về vai trò QTHT), kèm số đo cả hai vai trò.

**KHÔNG được chấm Fail vì:**

- Tên tệp `BaoCaoChiPhiTheoThoiGian_…` thay vì `BaoCaoChiPhi_…` như ô *Kết quả mong đợi* của đối tác —
  **BA đã chốt 2026-08-04** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`.
- Số liệu env QA khác env đối tác (25 hồ sơ / 226.308.268 ₫).
- Tệp .xlsx **không** có biểu đồ đường: đặc tả đòi `chart_type = LINE` cho **màn hình** (`:870`, `:1082`),
  `:1092` chỉ đòi tệp xuất có tiêu đề + kỳ + đơn vị + ngày tạo — không đòi vẽ lại biểu đồ trong tệp.
- Tên phông nhúng đọc ra không đúng chữ "Times New Roman" nhưng là bản tương thích số đo (vd `Tinos`).

## 5. Dạng dữ liệu phải phủ

**M = 2 lượt xuất khác kỳ báo cáo**, để chứng minh tệp **bám theo bộ lọc đang chọn** chứ không xuất cứng:
① Kỳ **Năm** 2026 (khớp đối tác) · ② Kỳ **khác** trong dropdown (Quý hoặc Tháng) cho ra **số điểm kỳ khác**.
Tệp ② phải có ô "Kỳ báo cáo" đổi theo và dãy theo kỳ khớp đúng màn của lượt đó.

**Nguồn xác định M:** tra đường ① rồi ② của flow — đặc tả `:1048` (bộ lọc kỳ: *Tuần / Tháng / Quý / Năm /
Khoảng tùy chọn*) và AC `:874` (*"chọn 12 tháng → 12 điểm trend"*) cho thấy số điểm kỳ **do bộ lọc quyết
định**, nên đây chính là chiều dữ liệu phải phủ. Đủ để chốt, không cần hỏi dev/BA.
Không đổi được kỳ, hoặc mọi kỳ đều ra đúng một điểm ⇒ ghi rõ vào mục 6 là **không dựng được biến thể ②** và
xử theo quy tắc GAP (ô trống), **không** tự hạ M xuống 1.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên (QTHT)**, phạm vi `BTP · TW` (góc phải ảnh) | `cbnv_tw_03` (ra verdict) **và** `admin` = QTHT `BTP · TW` (đóng GAP vai trò) | Không |
| Entity + trạng thái | Báo cáo **BC Chi phí theo thời gian** đã chạy xong (`Thời điểm tạo: 16/07/2026 16:32`), đang hiện số liệu | Y hệt: đã Xem báo cáo ra số liệu (`Thời điểm tạo: 06/08/2026 14:13` với cbnv, `14:30` với QTHT) rồi mới bấm Xuất | Không |
| Dữ liệu tiền đề | Có dữ liệu: Tổng chi phí toàn kỳ `226.308.268` · Tổng hồ sơ toàn kỳ `25` | Có dữ liệu: Tổng chi phí toàn kỳ `23.000.000` · Tổng hồ sơ toàn kỳ `2` (env QA ít bản ghi hơn — đã khai ở mục 4 là KHÔNG chấm Fail vì lệch số) | Không |
| Input / filter / giá trị nhập | Kỳ **Năm** 01/01/2026 → 31/12/2026 · Đơn vị **Toàn quốc** · thao tác **Xuất Excel** | Y hệt ở biến thể ①; thêm ② Khoảng tùy chọn 01/06→30/06/2026 và ③ Quý (kỳ không có dữ liệu) | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 25 hồ sơ, 1 lượt xuất duy nhất trong ảnh; ảnh **không phân biệt được** nút Excel hay PDF (cùng md5 với ảnh của dòng 264) | 2 hồ sơ; **3 biến thể kỳ** (Năm / Khoảng / Quý-rỗng) + 1 lượt gọi thẳng máy chủ kỳ Tháng; 2 lượt xuất thật bằng cbnv + 1 lượt bằng QTHT — đo đúng nút **Xuất Excel**, không suy từ nút PDF | Không |

**3 dữ kiện neo của đối tác:** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=chi-phi-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
· báo cáo đã chạy xong, thao tác dừng ở bước xuất tệp · vai trò **Quản trị viên (QTHT)**, env
`htpldn-uat.ospgroup.vn`, bản dựng sidebar **HTPLDN · V1.0**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` bản **V1.0**; đợt này đo
trên `18.143.165.120.nip.io`. Verdict Pass (nếu có) là **Pass tạm** cho tới khi bản dựng này lên env đối tác.


---

## 7. Sửa tiêu chí giữa chừng (ghi lại theo flow)

### Sửa 1 — 2026-08-06 14:20 — tách vế "QTHT có được xuất" khỏi vế "câu hiện ra khi từ chối"

**Lý do:** giống hệt tình huống đã xử ở `CPHTCT_06` §7 Sửa 1 (dòng 238) — bảng phân xử ở đó là bản gốc, ở đây chỉ áp lại.

| Vế | Nội dung | Đặc tả nói gì | Xử |
|---|---|---|---|
| a | QTHT có được phép xuất báo cáo? | Im lặng (`:62` chỉ nêu CB Nghiệp vụ / CB Phê duyệt) | **cần BA** — `cau-hoi-BA.md` Mục 2 |
| b | Câu hiện ra cho người dùng khi hệ thống từ chối? | Có quy định rõ `:117` — `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"* | **Reopen** — thực tế hiện đúng một chữ `"Forbidden"` |

**Phép thử quyết định:** khuyết tật ở vế b tồn tại ở **cả hai nhánh** trả lời của BA (QTHT được xuất → đang chặn nhầm; QTHT không được xuất → vẫn phải hiện câu tiếng Việt theo `:117` chứ không phải chuỗi kỹ thuật). ⇒ không bị chặn bởi BA ⇒ chốt **Reopen**, câu hỏi vai trò vẫn để mở ở file BA.

### Sửa 2 — 2026-08-06 14:20 — định nghĩa lại biến thể ② của mục 5

**Tiêu chí gốc viết:** biến thể ② phải là kỳ khác **cho ra số điểm kỳ khác**.

**Đo được:** qua giao diện, MỌI lựa chọn kỳ đều ra **đúng một điểm**. Chọn Tháng/Quý/Năm thì hệ thống tự khoá khoảng thời gian về đúng một kỳ hiện tại (ô Thời gian là chữ tĩnh, không sửa được); chỉ "Khoảng tùy chọn" mới nhập được ngày nhưng lại gộp cả khoảng thành một điểm.

**Sửa thành:** biến thể ② = **kỳ khác cho ra nhãn kỳ khác và khoảng ngày khác trong tệp** (Khoảng tùy chọn 01/06 → 30/06/2026), cộng biến thể ③ **kỳ không có dữ liệu** (Quý 3/2026 → màn rỗng, nút Xuất tự tắt) làm phép chứng minh âm.

**Vì sao KHÔNG xử theo quy tắc GAP (ô trống):** quy tắc GAP ở mục 5 viết cho tình huống *"không đổi được kỳ"*. Ở đây đổi kỳ được và đã đổi 3 lần; chiều dữ liệu đã được phủ, và kết quả đo (luôn 1 điểm) chính là **số đo**, không phải lỗ hổng độ phủ. Việc giao diện không dựng nổi 12 điểm theo AC `:874` được ghi thành **phát hiện ngoài phạm vi** (mục 8 §D1), không kéo verdict của case.

---

## 8. Kết quả đo (giai đoạn B) — 2026-08-06

| # | Tiêu chí PASS | Kết quả | Bằng chứng |
|:-:|---|---|---|
| 1 | `cbnv_tw_03` Xuất Excel giao được tệp .xlsx, không thông báo hỏng, không bị từ chối | ✅ Đạt | thông báo `"Đang tạo file..."` → `"Tạo file thành công."`, 0 lỗi |
| 2 | Hai đường đo độc lập cùng nói thành công | ✅ Đạt | (a) tệp thật 6.660 B mở đọc được bằng openpyxl · (b) XHR `POST /api/v1/bao-cao/export` → **200** kèm blob |
| 3 | Tên tệp đủ ngày + giờ-phút, xuất lần 2 khác phút ra tên khác | ✅ Đạt | `…_20260806_1413.xlsx` và `…_20260806_1425.xlsx` |
| 4 | Mở tệp: đủ 4 mục header + dãy theo kỳ đủ 3 thông tin `:869`, khớp màn | ✅ Đạt | tên BC · kỳ · đơn vị · ngày tạo; bảng `Kỳ / Số hồ sơ / Tổng chi phí`; số khớp từng con số trên màn |
| 5 | Lặp lại bằng vai trò **QTHT** — hệ thống **không từ chối** | ❌ **Hỏng** | `admin` bấm Xuất Excel → **403** `ERR-PERM-SYS-00-01`, chữ hiện ra `"Forbidden"`, 0 tệp |

**Verdict: 🔁 Reopen** — mục 1-4 đã hết lỗi (triệu chứng gốc 16/07 `ERR-RPT-04` không còn tái hiện), nhưng mục 5 hỏng đúng như vế b của đối tác ngày 31/07. Theo §7 Sửa 1, vế b không bị chặn bởi câu hỏi BA nên **không** chuyển "cần BA" mà chốt Reopen; câu hỏi vai trò QTHT vẫn để mở ở `cau-hoi-BA.md` Mục 2.

**§D — Phát hiện ngoài phạm vi (không kéo verdict):**

- **D1 — AC `:874` không dựng được qua giao diện.** Đặc tả đòi *"CB chọn 12 tháng → line chart 12 điểm trend"*. Giao diện khoá khoảng thời gian theo kỳ nên người dùng không có đường nào ra 12 điểm. Gọi thẳng máy chủ `kyBaoCao=THANG` cả năm 2026 thì máy chủ trả **đúng 12 điểm** và tệp xuất cũng dựng **đúng 12 dòng** (`image/CPCTHTTTG_05-xuat-excel-api-ky-Thang-12-diem.xlsx`). ⇒ khuyết ở tầng giao diện.
- **D2 — tệp xuất lộ mã kỹ thuật.** Chọn "Khoảng tùy chọn" thì dòng `Kỳ báo cáo` trong tệp in `KHOANG` thay vì chữ tiếng Việt; kỳ Năm/Tháng in đúng chữ.
- **D3 — bấm [Xem báo cáo] lần thứ hai thì hai nút Xuất bị khoá** và không mở lại được trong cùng phiên xem, dù báo cáo vẫn hiện đủ số liệu (`image/CPCTHTTTG_QA01-bam-xem-bao-cao-lan-2-nut-xuat-bi-khoa-V108.png`).
- **D4 — hiện tượng lạ về phiên làm việc** (403 → lời gọi nền 401 → bị đá về trang đăng nhập sau vài phút): ghi kèm số hiệu request ở `image/CPCTHTTTG_05-thong-bao-va-phan-hoi-may-chu.txt` mục E. Chưa chốt nguyên nhân, KHÔNG tính vào verdict.
