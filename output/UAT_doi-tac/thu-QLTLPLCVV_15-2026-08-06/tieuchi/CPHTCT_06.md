Mã case: CPHTCT_06 (tab `bug` dòng 238)        Thời điểm viết: 2026-08-06 12:39
Môi trường verify: https://18.143.165.120.nip.io        Bản dựng: **V1.0.8** (sidebar; gói `assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết file này** (khai theo flow §Giai đoạn A):
`reverify-week-3/cond/CPHTCT_06.md` (số đo 21/07/2026, bản dựng cũ) ·
`reverify-round-2026-08-05/RECIPE.md` §6 + `cond/CPCTHTTTG_06.md` (số đo 05/08, V1.0.6).
→ Mục 4 và 5 dưới đây suy từ **đặc tả** `srs-v3.5/srs-fr-11-bao-cao.md`, KHÔNG lấy số đo cũ làm ngưỡng.

---

## 1. Đối tác phản ánh

- **Vế a —** Trên màn Báo cáo thống kê, loại **BC Chi phí chi trả hỗ trợ**, sau khi đã Xem báo cáo ra số
  liệu, bấm **Xuất Excel** thì hệ thống **không tạo được tệp**, hiện thông báo
  *"Không thể tạo file xuất. Vui lòng thử lại."* — không có tệp nào tải về (16/07/2026).
- **Vế b —** Đối tác thử lại 31/07/2026: lần này thông báo đổi thành *"Forbidden"* (ô *TKM phản hồi lần 1*).
- **Vế c — Kỳ vọng của đối tác:** hệ thống xuất toàn bộ và **tự động tải tệp về máy**, tên tệp
  `BaoCaoChiPhi_{YYYYMMDD_HHmm}.xlsx`.

**Bằng chứng đã mở xem:** `partner-evidence/CPHTCT_06.jpg` (full-res 1905×1036, md5 `3ab70301…`) — đúng
màn của case này. Đối tác **không** gắn ảnh cho lần thử 31/07 (chỉ mô tả chữ trong ô phản hồi).

## 2. Đặc tả nói gì

- `srs-fr-11-bao-cao.md:1052` — thành phần màn hình #8: *"Nút Xuất Excel | button | "Xuất Excel (.xlsx)"
  → xuất theo format TT17/2025 | **click → auto-download** | Sau khi đã "Xem báo cáo""* — điều kiện hiển
  thị **"Sau khi đã Xem báo cáo"**, tức bảng liệt kê **đóng**: nút này có mặt và phải chạy được.
- `:85` — Processing bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp
  `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp
  `[BA chốt 2026-08-04]`"*.
- `:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file."*
- `:123` — AC chung: *"Given CB nhấn "Xuất Excel" When click Then tải file .xlsx khổ A4 Times New Roman
  13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"*.
- `:116` — E6 `ERR-RPT-04` *"Không thể tạo file xuất. Vui lòng thử lại"* — **đúng nguyên văn câu đối tác
  thấy**, tức đây là mã lỗi của chính hệ thống khi khâu tạo tệp hỏng, không phải lỗi trình duyệt.
- `:117` — E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"* — đây mới là câu đặc tả quy định cho
  tình huống thiếu quyền; chữ *"Forbidden"* đối tác thấy ngày 31/07 **không** nằm trong bảng lỗi.
- `:697`–`:727` — FR-IX-15 (UC138) BC Chi phí chi trả hỗ trợ: output đặc thù gồm `tong_chi_phi`,
  `tong_ho_so`, `trung_binh_ho_so`, `theo_don_vi[]`, `theo_ky[]` (đều điều kiện *Luôn*).
- `:62` — Preconditions chung: *"User đã đăng nhập, có role **CB Nghiệp vụ hoặc CB Phê duyệt** (TW/BN/ĐP)"*.

**IM LẶNG về:** vai trò **Quản trị viên (QTHT)** — đúng vai trò đối tác dùng trong ảnh — có được xem/xuất
báo cáo hay không. Đặc tả chỉ khai tác nhân là CB Nghiệp vụ / CB Phê duyệt, **không nói QTHT bị cấm**,
cũng **không nói QTHT được phép**.

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw_03`** (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, cấp TW) — đúng tác nhân
  đặc tả khai ở `:62`. Mật khẩu `Test@1234`, OTP lấy ở MailHog `http://18.143.165.120:8025`.
- Tài khoản dùng để **đóng GAP vai trò** (không ra verdict): **`admin`** (QTHT) — đúng vai trò trong ảnh
  đối tác.
- Màn: **Báo cáo thống kê** (`/bao-cao`) → Loại báo cáo = **BC Chi phí chi trả hỗ trợ**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**.
- Dữ liệu tiền đề: có ≥1 hồ sơ chi trả **đã thanh toán** trong kỳ (đặc tả `:82` — chỉ lấy bản ghi đã
  duyệt/đã thanh toán) để "Xem báo cáo" ra số liệu và nút Xuất bật.

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 5:**

1. Với `cbnv_tw_03`, sau khi Xem báo cáo ra số liệu, thao tác **Xuất Excel** làm hệ thống **giao được một
   tệp .xlsx** cho người dùng: không còn thông báo báo hỏng khâu tạo tệp, không còn bị từ chối truy cập.
2. **Đo bằng hai đường độc lập** và cả hai cùng nói thành công: (a) lấy được tệp thật, kích thước > 0 và
   mở đọc được bằng thư viện đọc .xlsx; (b) phản hồi máy chủ của **chính lượt bấm đó** là thành công kèm
   nội dung tệp, không phải phản hồi lỗi.
3. Tên tệp có **đủ ngày và giờ-phút**, đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`; xuất lần 2 sang phút
   khác cho ra **tên khác** (chứng minh không đè tệp — đúng lý do BA chốt ở `:85`).
4. Mở tệp đọc nội dung: có **đủ 4 mục header** (tên báo cáo · kỳ báo cáo · đơn vị · ngày tạo) và **số liệu
   khớp màn hình** — tổng chi phí, tổng hồ sơ, trung bình/hồ sơ, và từng dòng của bảng.
5. Lặp lại đúng thao tác đó bằng vai trò **Quản trị viên (`admin`)** — đúng vai trò trong ảnh đối tác —
   hệ thống **không từ chối**.

**❌ FAIL nếu** bất kỳ điều nào sau đây với vai trò `cbnv_tw_03`: hiện thông báo hỏng khâu tạo tệp · bị từ
chối truy cập · không có tệp nào về · tệp về nhưng rỗng/hỏng không mở được · thiếu ≥1 trong 4 mục header ·
số liệu trong tệp lệch với số đang hiện trên màn · tên tệp thiếu phần giờ-phút (2 lần xuất cùng ngày đè nhau).

**⚠️ Nhánh không được tự chấm:** nếu mục 1–4 **đạt** với `cbnv_tw_03` nhưng mục 5 **hỏng** (Quản trị viên
bị từ chối) → **KHÔNG Pass và KHÔNG Fail**: đặc tả im lặng về vai trò QTHT trên màn báo cáo (mục 2) →
chuyển **cần BA**, kèm số đo của cả hai vai trò.

**KHÔNG được chấm Fail vì:**

- Tên tệp là `BaoCaoChiPhiChiTraHoTro_…` chứ không phải `BaoCaoChiPhi_…` như ô *Kết quả mong đợi* của đối
  tác — **BA đã chốt 2026-08-04** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` với `{TenBaoCao}` là tên loại
  báo cáo viết liền PascalCase (`:86`, `:1092`).
- Số liệu trên env QA khác số liệu env đối tác (25 hồ sơ / 226.308.268 ₫) — khác **dữ liệu**, không phải lỗi.
- Tên phông nhúng trong tệp không đọc đúng chữ "Times New Roman" nhưng là bản tương thích số đo (vd
  `Tinos`) — đã được chấp nhận ở nhóm phiếu xuất PDF cùng màn.
- Đặc tả **không** quy định thông báo phải hiện trong bao lâu, hay phải có toast "Đang tạo file…".

## 5. Dạng dữ liệu phải phủ

**M = 2** khối dữ liệu bắt buộc có trong tệp: ① `theo_don_vi[]` (chi phí + số hồ sơ theo từng đơn vị) ·
② `theo_ky[]` (chi phí + số hồ sơ theo từng kỳ) — cộng 3 chỉ số tổng (`tong_chi_phi`, `tong_ho_so`,
`trung_binh_ho_so`).
**Nguồn xác định M:** đặc tả `srs-fr-11-bao-cao.md:718-724` (bảng Output đặc thù FR-IX-15, cả 5 dòng đều
điều kiện *Luôn*) — tra theo đường ① của flow, đủ nên dừng.
Khối nào tồn tại trong đặc tả mà tệp không có → tính là thiếu, chấm theo mục 4 điều kiện FAIL "thiếu mục
header / số liệu lệch".

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên (QTHT)** — góc phải ảnh ghi `Quản trị viên  QTHT`, phạm vi `BTP · TW` | Đo **cả hai**: `cbnv_tw_03` (CB Nghiệp vụ TW — đúng tác nhân `:62`, dùng ra verdict) **và** `admin` (QTHT, `BTP · TW` — đúng vai trò trong ảnh đối tác) | Không |
| Entity + trạng thái | Báo cáo **BC Chi phí chi trả hỗ trợ** đã chạy xong (`Thời điểm tạo: 16/07/2026 16:12`), đang hiện số liệu | Cùng loại báo cáo, đã Xem báo cáo xong đang hiện số liệu — `Thời điểm tạo 06/08/2026 12:49` (cbnv) và `12:59` (QTHT) | Không |
| Dữ liệu tiền đề | Có dữ liệu: Tổng chi phí `226.308.268` · Tổng hồ sơ `25` · TB/hồ sơ `9.052.331` | Có dữ liệu: Tổng chi phí `23.000.000` · Tổng hồ sơ `2` · TB/hồ sơ `11.500.000` — khác **số**, cùng **loại tình huống** (kỳ có hồ sơ đã thanh toán, nút Xuất bật) | Không |
| Input / filter / giá trị nhập | Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**; thao tác **Xuất Excel** | Y hệt: Kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, bấm **Xuất Excel** | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 25 hồ sơ; ảnh không cho thấy tệp nào được tạo nên không rõ đủ M = 2 khối hay không | Dựng đủ **M = 2**: khối ① `theo_don_vi[]` **có** (1 dòng `Cục Bổ trợ tư pháp`, khớp màn) · khối ② `theo_ky[]` **vắng mặt** — đo 3 đường (màn hình · tệp .xlsx · phản hồi máy chủ) đều không có | Không |

**3 dữ kiện neo của đối tác:** URL `htpldn-uat.ospgroup.vn/bao-cao?loai=chi-phi-chi-tra&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
· báo cáo đã chạy xong đang hiển thị số liệu, thao tác dừng ở bước xuất tệp · vai trò **Quản trị viên
(QTHT)**, env `htpldn-uat.ospgroup.vn`, bản dựng ghi ở sidebar **HTPLDN · V1.0**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên env `htpldn-uat.ospgroup.vn` bản **V1.0**; đợt này
đo trên `18.143.165.120.nip.io` bản **V1.0.8**. Verdict chỉ có hiệu lực cho env + bản dựng đã ghi.

---

## 7. Sửa tiêu chí giữa chừng (ghi theo flow — có mốc giờ + lý do)

### Sửa 1 — 2026-08-06 13:10, sau khi đo xong cả hai vai trò

**Chỗ sửa:** nhánh ⚠️ ở mục 4 (*"mục 1–4 đạt nhưng mục 5 hỏng → cần BA"*).

**Sửa thành:** tách nhánh đó làm **hai vế**, vì số đo cho thấy lượt từ chối chứa **hai khuyết tật khác
loại**, không phải một:

| Vế | Nội dung | Đặc tả nói gì | Xử |
|---|---|---|---|
| a | Quản trị viên **có được phép** xuất báo cáo không? | **Im lặng** (`:62` chỉ khai CB Nghiệp vụ / CB Phê duyệt) | **cần BA** — câu hỏi đã gửi ở `cau-hoi-BA.md` Mục 2 |
| b | Khi hệ thống **quyết định từ chối**, câu hiện cho người dùng phải là gì? | **Có quy định rõ** — `:117` E7 `ERR-RPT-05` *"Bạn không có quyền xem báo cáo này"* | **Reopen** — thực tế hiện chuỗi kỹ thuật tiếng Anh *"Forbidden"* |

**Lý do sửa (không phải để chiều kết quả):** khi viết mục 4 ở giai đoạn A, tôi giả định nhánh "QTHT bị từ
chối" chỉ đẻ ra đúng một câu hỏi phân quyền. Đo xong mới thấy câu từ chối là chuỗi thô `Forbidden` — đây là
**dữ kiện mới do đo mà có**, và mục 2 của chính file này đã trích `:117` từ trước khi mở màn.

**Phép thử quyết định để chọn verdict:** giả sử BA trả lời theo **cả hai** hướng —
- BA nói *"QTHT không được xuất"* → hệ thống vẫn phải hiện câu tiếng Việt `:117`, hiện `Forbidden` là **sai**.
- BA nói *"QTHT được xuất"* → hệ thống chặn nhầm, càng **sai**.

Khuyết tật vế b **tồn tại ở cả hai nhánh trả lời của BA** ⇒ nó **không bị chặn bởi BA** ⇒ ghi verdict
**Reopen**, đồng thời vẫn giữ câu hỏi BA cho vế a. (Nếu khuyết tật chỉ tồn tại ở một nhánh thì mới phải để
ô trống chờ BA.)

**Không sửa:** toàn bộ 5 điều kiện PASS ở mục 4 và danh sách *"KHÔNG được chấm Fail vì"* giữ nguyên — không
hạ chuẩn dòng nào.

### Sửa 2 — 2026-08-06 13:10, phạm vi của khối `theo_ky[]` thiếu

**Chỗ sửa:** câu cuối mục 5 (*"Khối nào tồn tại trong đặc tả mà tệp không có → … chấm FAIL"*).

**Sửa thành:** khối `theo_ky[]` vắng mặt **không kéo verdict của case này**, mà tách thành **phát hiện
ngoài phạm vi** (xử theo flow §"bug ngoài phạm vi không kéo verdict").

**Lý do:** đo 3 đường thì khối ② vắng ở **cả màn hình lẫn phản hồi máy chủ**, không chỉ vắng trong tệp ⇒
đây là khuyết tật của khâu **dựng báo cáo** (FR-IX-15), không phải khâu **xuất tệp** — mà case này của đối
tác nói về khâu xuất tệp. Tiêu chí đúng cho khâu xuất là *"tệp khớp màn hình"*, và tệp **có khớp**. Gộp
khuyết tật của chức năng khác vào verdict case này sẽ làm dev sửa nhầm chỗ.

## 8. Số đo thực tế (giai đoạn B)

| Vai trò | Xem báo cáo | Bấm Xuất Excel | Câu người dùng thấy | Tệp giao ra |
|---|---|---|---|---|
| `cbnv_tw_03` (CB Nghiệp vụ TW) | `GET /api/v1/bao-cao/chi-phi-chi-tra` → **200**, ra số liệu | `POST /api/v1/bao-cao/export` → **200** | *"Đang tạo file..."* → *"Tạo file thành công."* | **1 tệp** `BaoCaoChiPhiChiTra_20260806_1249.xlsx`, 6918 B, mở đọc được |
| `admin` (QTHT — vai trò của đối tác) | `GET /api/v1/bao-cao/chi-phi-chi-tra` → **200**, ra **đúng số liệu đó** | `POST /api/v1/bao-cao/export` → **403** `ERR-PERM-SYS-00-01` | *"Đang tạo file..."* → **`Forbidden`** (sống 3,15 s) | **0 tệp** |

- Mục 1 ✅ · mục 2 ✅ (tệp thật 6918 B mở bằng `openpyxl` + phản hồi máy chủ 200 của **chính lượt bấm đó**)
  · mục 3 ✅ (xuất lần 2 lúc 12:51 ra `…_20260806_1251.xlsx`, **tên khác**) · mục 4 ✅ (đủ 4 mục header;
  `23.000.000` / `2` / `11.500.000` và dòng `Cục Bổ trợ tư pháp` khớp màn) · **mục 5 ❌**.
- Triệu chứng gốc `ERR-RPT-04` *"Không thể tạo file xuất"* (16/07) **không còn tái hiện** ở bất kỳ vai trò nào.
- Triệu chứng 31/07 *"Forbidden"* **vẫn tái hiện nguyên vẹn** ở đúng vai trò đối tác đã dùng.
- Phát hiện ngoài phạm vi: thiếu khối `theo_ky[]` (`:724`, điều kiện *Luôn*) — xem mục 7 Sửa 2.

**→ Verdict: Reopen** (theo mục 7 Sửa 1 vế b), kèm câu hỏi BA cho vế a.
