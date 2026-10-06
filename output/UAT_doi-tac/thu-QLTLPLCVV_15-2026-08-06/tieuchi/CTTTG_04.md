# Tiêu chí verify — CTTTG_04 (tab `bug`, dòng 281)

Mã case: CTTTG_04          Thời điểm viết: 2026-08-06 14:03 (viết XONG trước khi mở màn Báo cáo thống kê
trên env verify)
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8**, dấu vân tay bó mã
giao diện **`assets/index-DIABnbIr.js`**. ⚠️ **Bản dựng đổi GIỮA phiên đo mà chuỗi phiên bản không đổi:**
lượt đo đầu của nhánh A (14:10–14:19) chạy trên bó mã **`assets/index-CNwX9JjX.js`**, từ 14:22 trở đi là
`index-DIABnbIr.js`. ⇒ Đã **đo lại toàn bộ nhánh A** (14:28–14:38) trên bó mã mới để hai nhánh nằm trên
cùng một bản dựng; mọi số dùng để chấm ở mục 7–8 là của `index-DIABnbIr.js`. Tab đo mở MỚI trong phiên
này (ngữ cảnh trình duyệt riêng `cttlg04-qa`, không tái dùng tab của phiên khác).

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A của flow):
`thu-QLTLPLCVV_15-2026-08-06/tieuchi/SLCTHT_06.md` (case cùng lô, đã Reopen) ·
`tieuchi/CTTLV_05.md` (BC Chương trình theo lĩnh vực — cùng họ báo cáo CT HTPLDN, có tiền lệ xử lý
"thẻ số DN bị BA gỡ") · `tieuchi/CTTDVQL_04.md` (BC Chương trình theo đơn vị) · `cau-hoi-BA.md` Mục 2
(câu hỏi "QTHT có được xuất báo cáo không") · `bug-report.md` Phần 2 (BUG-SLCTHT-006, BUG-CTTLV-005).
⚠️ Các hồ sơ trên chứa **số đo cũ** (vd "7 chương trình", "tệp xuất khớp màn", "QTHT bị 403"). Mục 4 và
mục 5 dưới đây suy từ **đặc tả** `srs-fr-11-bao-cao.md` + `srs-v3.5.md` §Phụ lục E (đã mở file đọc từng
dòng được quote), **không** lấy số đo cũ làm ngưỡng — cụ thể tiêu chí (e) đòi tệp khớp **số hiện trên màn
tại thời điểm đo**, không chốt cứng con số nào; và §9c của brief nói rõ **cấm suy kết quả từ case khác**:
mỗi loại báo cáo là một nhánh dữ liệu riêng, phải đo lại đầy đủ trên đúng màn của case này.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** (tách theo ô `Kết quả mong đợi` + `Kết quả thực tế` + `TKM phản hồi lần 1`):

- **(a) Không xuất được tệp.** Bấm **[Xuất Excel]** trên màn *Báo cáo thống kê*, loại báo cáo =
  **BC Chương trình theo thời gian**, thì hệ thống **không giao tệp nào**, chỉ hiện thông báo lỗi.
  - Vòng 1 (16/07/2026, bản dựng **V1.0**): thông báo đỏ ✗ **"Không thể tạo file xuất. Vui lòng thử lại."**
  - Vòng 2 (31/07/2026, bản dựng **V1.0.3**): thông báo đỏ ✗ **"Forbidden"** — **đổi hẳn câu chữ**, sang
    một chuỗi tiếng Anh thô.
- **(b) Tên tệp.** Kỳ vọng của đối tác: tệp tải về tên `BaoCaoChuongTrinh_{YYYYMMDD_HHmm}.xlsx`.
- **(c) Nội dung tệp.** Kỳ vọng của đối tác: *"Hệ thống xuất **toàn bộ** và tự động tải tệp về máy người
  dùng"* — tệp chứa trọn dữ liệu báo cáo đang xem, không phải một phần.

**Lệch giữa 2 vòng bằng chứng** (bắt buộc ghi theo §Cổng bằng chứng):

| | vòng 1 (`CTTTG_04.jpg`) | vòng 2 (`CTTTG_04_v2.jpg`) |
|---|---|---|
| bản dựng | `HTPLDN · V1.0` | `HTPLDN · V1.0.3` |
| thời điểm | 16/07/2026 16:58 (Thời điểm tạo BC 16:57) | 31/07/2026 15:35 (Thời điểm tạo BC 15:35) |
| bộ lọc *Đơn vị* | **Toàn quốc** | **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** |
| chữ hiện ra sau [Xuất Excel] | "Không thể tạo file xuất. Vui lòng thử lại." | "Forbidden" |

Cùng vai trò, cùng loại BC, cùng Kỳ **Năm** 01/01/2026 → 31/12/2026, cùng số liệu **1 · 0 · 0**;
**khác bản dựng · khác bộ lọc đơn vị · khác câu thông báo**. ⇒ Không được coi 2 vòng là cùng một triệu
chứng; vế (a) phải đo cho **cả hai** câu thông báo và **cả hai** cấu hình đơn vị.

**🔴 Ghi nhận về thanh địa chỉ ảnh vòng 2 — KHÔNG phải bằng chứng nhầm case.** Thanh địa chỉ trong
`CTTTG_04_v2.jpg` ghi `loai=ct-theo-linh-vuc&…&donViId=00000000-0000-4000-8000-000000000001`, **lệch**
với màn đang hiển thị. Nhưng ô *Loại báo cáo* ghi rõ **"BC Chương trình theo thời gian"**, tiêu đề khối
kết quả cũng là **"BC Chương trình theo thời gian"**, và bộ 3 thẻ số (*Tổng chương trình toàn kỳ / Tổng
DN toàn kỳ / Tổng ngân sách toàn kỳ*) đúng là bộ thẻ của báo cáo theo thời gian ở ảnh vòng 1 (URL vòng 1
ghi đúng `loai=ct-theo-thoi-gian`). ⇒ Đây là **URL cũ chưa cập nhật khi đổi loại báo cáo trong ứng dụng
một trang**, không phải ảnh của case khác. Nếu bản dựng hiện tại cũng không cập nhật URL khi đổi loại báo
cáo thì đó là **phát hiện ngoài phạm vi**, xử riêng ở mục 7, **không kéo verdict**.

**Bằng chứng đã mở đọc full-res:**

- `partner-evidence/CTTTG_04.jpg` (vòng 1). Thấy: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`;
  chân logo sidebar `HTPLDN · V1.0`; góc phải `BTP · TW` + chuông 99+ + avatar `QV` + **Quản trị viên
  QTHT**; breadcrumb *Trang chủ / Báo cáo thống kê*; **thông báo đỏ ✗ "Không thể tạo file xuất. Vui lòng
  thử lại."** nổi giữa đỉnh trang; form lọc: *Loại báo cáo* = **BC Chương trình theo thời gian**,
  *Kỳ báo cáo* = **Năm**, *Thời gian* **Từ 01/01/2026 — Đến 31/12/2026**, *Đơn vị* = **Toàn quốc**
  (chữ xám placeholder), **không có ô lọc đặc thù nào khác**; hàng nút **[Xem báo cáo] [Xuất Excel]
  [Xuất PDF]**; khối kết quả **"BC Chương trình theo thời gian"** — *Kỳ: Năm · 01/01/2026 → 31/12/2026 ·
  Đơn vị: Toàn quốc*, **Thời điểm tạo: 16/07/2026 16:57**, ba thẻ **Tổng chương trình toàn kỳ = 1** ·
  **Tổng DN toàn kỳ = 0** · **Tổng ngân sách toàn kỳ = 0**; nút **[Ẩn biểu đồ]** + phần đầu một **biểu
  đồ đường** (trục tung tới 1, có 1 điểm mốc tròn); đồng hồ máy **04:58 PM 2026-07-16**.
- `partner-evidence/CTTTG_04_v2.jpg` (vòng 2). Thấy: thanh địa chỉ `…loai=ct-theo-linh-vuc&kyBaoCao=NAM&
  tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001` (xem ghi nhận ở
  trên); chân logo `HTPLDN · V1.0.3`; cùng vai trò **Quản trị viên QTHT**, `BTP · TW`; **thông báo đỏ ✗
  "Forbidden"** ở đúng vị trí đó; *Loại báo cáo* = **BC Chương trình theo thời gian**, *Kỳ* = **Năm**,
  **Từ 01/01/2026 — Đến 31/12/2026**, *Đơn vị* = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**; khối kết
  quả **"BC Chương trình theo thời gian"** — *Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)*,
  **Thời điểm tạo: 31/07/2026 15:35**, ba thẻ **1 · 0 · 0** y hệt vòng 1; nút **[Ẩn biểu đồ]**; trên
  thanh trình duyệt có **biểu tượng tải xuống** (dấu vết các lượt tải trước, **không** chứng minh lượt
  này có tệp — ảnh không mở khay tải); đồng hồ máy **03:35 PM 2026-07-31**.

## 2. Đặc tả nói gì

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`
(+ `srs-v3.5.md` cho Phụ lục E). Đã **mở file đọc trực tiếp** từng dòng dưới đây, không lấy số dòng từ
trí nhớ.

**Vế (a) — quyền + luồng xuất:**

- `:62` — Preconditions chung TPL-REPORT-FULL: *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê
  duyệt (TW/BN/ĐP)"*.
- `:79` — Processing chung bước 1: `| 1 | Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01 |`
- `:81` — bước 3: *"Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc, BN chỉ thấy BN mình, ĐP chỉ thấy
  ĐP mình (BN và ĐP ngang cấp song song, không thấy nhau)"*.
- `:82` — bước 4: *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh
  toán)"* (BR-RPT-01).
- `:1052` — SCR-IX-01 thành phần 8: `| 8 | action-bar | Nút Xuất Excel | button | "Xuất Excel (.xlsx)" →
  xuất theo format TT17/2025 | click → auto-download | Sau khi đã "Xem báo cáo" |`
- `:1058` — thành phần 14: `| 14 | content | Toast xuất file | toast | "Đang tạo file..." → "Xuất thành
  công" + auto-download | — | Khi nhấn xuất |`
- `:116` — E6: `| E6 | Lỗi xuất file | ERR-RPT-04 | "Không thể tạo file xuất. Vui lòng thử lại" | ERROR |`
  ← **đúng nguyên văn câu đối tác chụp ở vòng 1** ⇒ vòng 1 là **nhánh lỗi**, không phải nhánh thành công.
- `:117` — E7: `| E7 | Không có quyền | ERR-RPT-05 | "Bạn không có quyền xem báo cáo này" | ERROR |`
  ← đối chiếu với chuỗi **"Forbidden"** ở vòng 2.
- `:1268` — BR-AUTH-08: *"chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. TW thấy toàn
  quốc, BN thấy BN, ĐP thấy ĐP"*, cột **Ngoại lệ = "QTHT bypass"**, cột Áp dụng = *"Toàn bộ FR-IX"*.

**Vế (b) — tên tệp:**

- `:85` — Processing chung bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên
  tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo
  `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]`"*.
- `:86` — bước 8 (PDF) định nghĩa token dùng chung: *"`{TenBaoCao}` là tên loại báo cáo viết liền kiểu
  PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số (dấu `/`, khoảng trắng, dấu câu)"*.
- `srs-v3.5.md:6716` — **Phụ lục E §H8** *Tên tệp xuất thống nhất*: *"Áp cho **tệp kết xuất dữ liệu**
  phần mềm sinh ra theo yêu cầu người dùng (xuất danh sách, xuất báo cáo), ở **mọi nhóm chức năng**…
  **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu
  tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số… Phần giờ-phút bắt buộc để xuất hai lần trong cùng
  ngày không đè tệp. Tổng độ dài tối đa **255 ký tự**… `[BA chốt 2026-08-06 — nâng phạm vi quyết định
  2026-08-04 của Nhóm IX thành quy ước chung]`"*.
- `:123` — AC chung: *"**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times
  New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"*.
- `:1092` — Quy tắc tương tác SCR-IX-01: *"Tên tệp cả hai định dạng theo **Phụ lục E §H8** —
  `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"*.

> 🔴 **Kỳ vọng (b) của đối tác lệch đặc tả — nhưng BA ĐÃ chốt đúng điểm này.** Đối tác đòi literal
> `BaoCaoChuongTrinh_…`; khuôn `:85`+`:86`+`srs-v3.5.md:6716` suy tên từ **tên loại báo cáo** (*"BC
> Chương trình theo thời gian"*), không phải một chuỗi cố định. Các dòng này mang nhãn nguồn + ngày
> **`[BA chốt 2026-08-04]`** / **`[BA chốt 2026-08-06]`**, tức **sau** cả 2 vòng test của đối tác (16/07
> và 31/07). Theo §Rẽ nhánh của flow (*"Ngoại lệ duy nhất — BA ĐÃ chốt trước đúng điểm tranh chấp này,
> dẫn được nguồn kèm ngày → áp quyết định có sẵn"*), vế (b) **áp khuôn của đặc tả**, KHÔNG đẩy sang
> cần-BA và KHÔNG chấm Fail vì tên khác literal của đối tác. Phần `_{YYYYMMDD_HHmm}` thì đối tác và đặc
> tả **trùng khớp** ⇒ vẫn là tiêu chí bắt buộc.

**Vế (c) — nội dung tệp:**

- `:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file."*
- `:1280` — BR-DATA-06: *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**,
  không vượt quá 10,000 rows/file"*, Áp dụng = *Toàn bộ FR-IX*.
- `:87` — bước 9: *"Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo"*.
- `:88` — bước 10: *"Ghi nhật ký thao tác (xem/xuất báo cáo)"* (BR-DATA-05, xem thêm `:1274`).
- `:92`–`:101` — **Output chung**, cột *Điều kiện* của cả 8 dòng đều là **"Luôn"**: `ten_bao_cao` ·
  `ky_bao_cao` · `tu_ngay / den_ngay` · `don_vi_ten` (*"Tên đơn vị hoặc 'Toàn quốc'"*) · `ngay_tao_bc` ·
  `nguoi_tao` · `tong_ban_ghi` · `data[]`.
- **FR-IX-23 (UC146) `:995`–`:1023`** — *BC CT theo thời gian*:
  - `:1006` Tác nhân: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*
  - `:1008` Template: *"Kế thừa TPL-REPORT-FULL (**không bổ sung input**)"* ⇒ màn này **không có bộ lọc
    đặc thù**, chỉ Kỳ + Thời gian + Đơn vị. (Khớp `:1086` — dòng UC146 của bảng mapping 23 loại BC có
    cột *Bộ lọc đặc thù* = **"—"**, cột *Biểu đồ* = **"Line chart trend"**.)
  - `:1010` Công thức: *"Đếm CT theo kỳ thời gian. Biểu đồ line chart"*
  - `:1012` Dimensions: *"Kỳ, Trend"*
  - `:1016`–`:1020` **Output đặc thù**, cột *Điều kiện* của cả 3 dòng đều là **"Luôn"**:
    `trend_data[]` = `{ky_label, so_ct}` · `chart_type` = `LINE` · `tong_ct` = *"Tổng CT toàn kỳ"*
  - `:1018` mang quyết định đã chốt: *"`[CTTLV_04 chốt 2026-07-24: **bỏ so_dn** — CSV UC146 chỉ 'thống kê
    chương trình theo thời gian', không có số DN; không có mô hình CT↔DN. Cùng lý do FR-IX-22.]`"*
  - `:1023` AC bổ sung: *"**Given** CB chọn 12 tháng **When** tạo BC **Then** hiển thị biểu đồ trend số
    CT theo thời gian"*
- `:113` — E3: `| E3 | Không có dữ liệu | INF-RPT-01 | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | INFO |`

**IM LẶNG về** (⇒ CẤM chấm Fail vì mấy thứ này):
tên sheet trong workbook · thứ tự cột trong tệp · có đóng khung / tô màu / in đậm không · có dòng tổng
cuối bảng không · định dạng số và định dạng ngày cụ thể trong ô · biểu đồ có được nhúng vào tệp `.xlsx`
không · tệp xuất có mấy sheet · nhãn kỳ (`ky_label`) phải viết theo mẫu chữ nào ("Tháng 01/2026" hay
"2026-01") · kỳ không có chương trình nào thì có xuất hiện thành điểm 0 hay bị bỏ qua · **vai trò QTHT có
được XEM/XUẤT báo cáo hay không** (`:62` và `:1006` chỉ **liệt kê** CB NV / CB PD, **không** viết câu cấm
QTHT; `:1268` lại cho QTHT **bypass** phạm vi đơn vị — hai chỗ này không đủ để kết luận QTHT bị cấm) ·
thông báo lỗi hiển thị ở dạng lớp nổi hay inline · mã lỗi có lộ ra giao diện hay không · **thẻ "Tổng ngân
sách toàn kỳ"** (xem §Hai điểm ghi nhận riêng ngay dưới) · URL trên thanh địa chỉ có được cập nhật khi
đổi loại báo cáo hay không.

**🔴 Hai điểm ghi nhận RIÊNG — không kéo verdict của case** (flow §Ca biên: phát hiện nằm trong đúng màn
đang tranh chấp nhưng **đối tác không nêu** ⇒ xử riêng; trái đặc tả **nói rõ** → log lỗi mới, rơi vào
đặc tả **im lặng** → thêm mục trong file gửi BA):

1. **Thẻ "Tổng DN toàn kỳ"** — `:1018` chốt ngày **2026-07-24**: *bỏ `so_dn`*, lý do *"không có mô hình
   CT↔DN"*. Cả 2 ảnh của đối tác (16/07 **trước** và 31/07 **sau** quyết định) đều **còn** thẻ đó. Ở lượt
   đo này: bản dựng còn thẻ/cột số DN ⇒ **trái `:1018`** (đặc tả nói rõ) → **log lỗi mới**; không còn ⇒
   chỉ ghi nhận là đã đúng.
2. **Thẻ "Tổng ngân sách toàn kỳ"** — danh sách Output đặc thù `:1016`–`:1020` **không** có mục ngân sách
   (chỉ `trend_data[]`, `chart_type`, `tong_ct`), nhưng đặc tả cũng **không có câu nào bỏ nó** như đã làm
   với `so_dn` ở `:1018`; loại BC anh em FR-IX-21 lại **có** `tong_ngan_sach` (`:944`). ⇒ **đặc tả im
   lặng** cho loại BC này → nếu bản dựng còn thẻ đó thì **thêm 1 mục hỏi BA**, **không** log lỗi.

## 3. Precondition

- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → menu **Báo cáo thống kê** → *Loại báo cáo* =
  **BC Chương trình theo thời gian** (URL mang `?loai=ct-theo-thoi-gian`).
- **Tài khoản — đo CẢ 2 nhánh, cùng bộ tiêu chí:**

  | Nhánh | Tài khoản | Vai trò | Dùng để |
  |---|---|---|---|
  | **A — ra verdict** | `cbnv_tw_04` / `Test@1234` | CB_NV_TW, cấp TW ⇒ phạm vi *Toàn quốc*, khớp `BTP · TW` của đối tác; đúng tác nhân `:62` + `:1006` | quyết Pass / Reopen |
  | **B — đối chứng** | `admin` / `Secret@123` | QTHT — **trùng khít vai trò trên cả 2 ảnh đối tác** | giải thích triệu chứng **"Forbidden"** vòng 2; đóng dòng GAP *Vai trò / tài khoản* |

  Tài khoản quản trị **không** được dùng để ra verdict (quyền rộng che lỗi phân quyền) — nhánh B chỉ đối
  chứng. Rule 7 nếu khoá: fallback **cùng vai trò + cùng cấp** `cbnv_tw_04` → `cbnv_tw_05` →
  `cbnv_tw_03`…, tuyệt đối không đổi vai trò/cấp; ghi rõ tài khoản THỰC đã dùng.
- **Xác nhận danh tính token NGAY TRƯỚC và NGAY SAU mỗi phép đo quyết định** (§9b brief — có phiên QA
  khác chạy song song trên cùng trình duyệt + cùng env): đọc `tenDangNhap` / `vaiTro` / `donViId` /
  `capDonVi` từ access_token. Trước ≠ sau ⇒ **phép đo VÔ HIỆU**, đăng nhập lại và đo lại.
- **Dữ liệu tiền đề:** ≥ 1 chương trình HTPL nằm trong khoảng đo, ở trạng thái được `:82` cho phép đếm
  (đã duyệt / hoàn thành / đã thanh toán), thuộc phạm vi TW. Để đo được **dạng ③ ở mục 5** (trend nhiều
  điểm) thì các chương trình đó phải **rơi vào ≥ 2 kỳ con khác nhau** trong khoảng đã chọn. Kiểm trước
  bằng màn **CT HTPLDN** hoặc `GET /api/v1/chuong-trinh-htpls` (đọc trường ngày để biết chúng trải trên
  mấy tháng). Thiếu → **được seed** qua BE API (`create → submit → approve bằng tài khoản KHÁC →
  publish/activate/complete bằng người tạo`, mỗi bước cần `version`) và **bắt buộc khai** bản ghi nào ·
  đổi gì · env nào vào mục 7 + bug entry. Tiền đề **tạo được mà không tạo → CẤM mọi verdict, kể cả ô
  trống.**
- **Bẫy cache máy chủ:** báo cáo thống kê có cache phía máy chủ. Sau khi seed mà số không đổi → đọc
  trường **"Thời điểm tạo"** trên màn; ép khoá cache mới bằng cách **đổi `denNgay` 1 ngày**.
  `cache:'reload'` chỉ bust cache trình duyệt ⇒ không dùng làm căn cứ.

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 6 điều dưới đây (đo được):**

- **(a) Nhánh A giao được tệp, không có thông báo lỗi.** Với `cbnv_tw_04`, ở dạng dữ liệu ① mục 5: bấm
  **[Xem báo cáo]** → chờ khối kết quả hiện → bấm **[Xuất Excel]**. Đo bằng bộ bắt thông báo cài **trước**
  khi bấm: **0** thông báo mang nội dung lỗi/từ chối (đếm theo **mốc giờ khác nhau**, không theo số phần
  tử), và hệ thống **giao ra một tệp** (tệp về máy, hoặc phản hồi máy chủ của chính thao tác đó có thân
  nhị phân tải về được). Số request của thao tác đếm bằng `list_network_requests` (nút có thể là GET nên
  `window.__qa.net` không ghi).
- **(b) Tệp là .xlsx thật.** Mở được bằng thư viện đọc xlsx (`openpyxl`) hoặc giải nén zip đọc được
  `xl/workbook.xml` — **không** phải HTML/JSON đổi đuôi. (Mã 200 + có bytes **không** đủ để đạt (b).)
- **(c) Tên tệp đúng khuôn `:85` + `:86` + `srs-v3.5.md:6716`:** dạng `<Tên>_<8 chữ số>_<4 chữ số>.xlsx`,
  trong đó `<Tên>` là **tên loại báo cáo viết liền, không dấu tiếng Việt, không khoảng trắng, không dấu
  câu**, và `<8 chữ số>_<4 chữ số>` là **ngày `YYYYMMDD` + gạch dưới + giờ phút `HHmm`** khớp thời điểm
  xuất (sai lệch ≤ 5 phút so với đồng hồ lúc bấm nút). Kiểm bằng biểu thức
  `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`; tổng độ dài ≤ 255 ký tự.
- **(d) Trong tệp có đủ phần đầu theo `:1092` (đối chiếu thêm Output chung `:94`–`:98`):** đọc nội dung ô
  của tệp phải tìm thấy **tiêu đề báo cáo**, **kỳ báo cáo**, **khoảng thời gian tu_ngay–den_ngay**,
  **tên đơn vị** (hoặc "Toàn quốc"), **ngày tạo báo cáo**. Đủ 5 mảnh ⇒ đạt; thiếu bất kỳ mảnh nào ⇒ không
  đạt.
- **(e) Nội dung tệp đúng hình hài của FR-IX-23 VÀ khớp số đang hiển thị trên màn** — phép đo quyết định,
  không được bỏ, gồm 3 phần:
  - **(e1) Có chuỗi trend theo kỳ (`:1018`).** Tệp phải chứa một **danh sách nhiều dòng mà mỗi dòng là
    một kỳ thời gian**, trên dòng đó có **cả hai** thứ: **nhãn kỳ** (`ky_label` — đọc được là mốc thời
    gian) và **số chương trình của kỳ đó** (`so_ct`). Thiếu hẳn chiều thời gian, hoặc chỉ có nhãn kỳ mà
    không có số, hoặc chỉ có số mà không có nhãn ⇒ không đạt.
  - **(e2) Có tổng toàn kỳ (`:1020`)** và **số trong tệp khớp số trên màn ở CÙNG một lần "Xem báo cáo"**:
    thẻ *Tổng chương trình toàn kỳ* trên màn = số tổng trong tệp; **và** mỗi điểm của **biểu đồ đường /
    bảng dữ liệu trên màn** có mặt trong tệp với **cùng nhãn kỳ và cùng số chương trình**; số điểm kỳ
    trong tệp = số điểm kỳ trên màn. (Không được dừng ở việc khớp mỗi thẻ tổng.)
  - **(e3) Cộng khớp:** cộng dọc cột số chương trình của các dòng kỳ = số tổng toàn kỳ. Lệch ⇒ theo
    §"phép đo đang nói dối" là số đang sai, **phải đo lại**, chưa được kết luận.
- **(f) Áp đúng bộ lọc hiện tại (`:1280`)** — chứng minh bằng **so sánh giữa các dạng ở mục 5**: nội dung
  tệp của dạng ② (đơn vị cụ thể) và dạng ③ (kỳ nhiều điểm) **khác** nội dung tệp dạng ①, và mỗi tệp khớp
  đúng màn của chính bộ lọc đó theo tiêu chí (e). Riêng dạng ③: tệp phải có **≥ 2 nhãn kỳ khác nhau**
  (một cấu hình ra đúng 1 điểm thì không phân biệt được "trend thật" với "chỉ in mỗi tổng").

**Nhánh B (đối chứng, `admin`/QTHT) — không quyết Pass/Fail của case, nhưng bắt buộc đo và ghi:**
lặp lại đúng dạng ① rồi ghi nhận: xuất được tệp, **hay** bị từ chối. Nếu bị từ chối thì đọc **nguyên văn**
chữ hiện ra và đối chiếu `:117`.

**❌ FAIL nếu (bất kỳ điều nào):**

- Nhánh A bấm [Xuất Excel] mà **không có tệp nào được giao**, hoặc hiện thông báo mang nghĩa từ chối/thất
  bại (gồm nhưng không giới hạn ở đúng 2 câu đối tác chụp).
- Tệp giao ra **không mở được** bằng thư viện đọc xlsx (HTML/JSON/tệp hỏng đổi đuôi).
- Tên tệp **không** có phần ngày-giờ `_YYYYMMDD_HHmm` trước `.xlsx`, hoặc còn dấu tiếng Việt / khoảng
  trắng / dấu câu trong phần tên báo cáo.
- Tệp **thiếu** bất kỳ mảnh nào trong 5 mảnh phần đầu ở (d).
- Tệp **không có chiều thời gian** ở (e1) — tức chỉ in các con số tổng mà không có danh sách theo kỳ,
  hoặc dòng kỳ thiếu một trong hai thành phần nhãn kỳ / số chương trình.
- Bất kỳ số nào trong (e2) **lệch** so với màn, hoặc số điểm kỳ trong tệp khác số điểm kỳ trên màn, hoặc
  cộng dọc ở (e3) không bằng tổng.
- Đổi bộ lọc mà **nội dung tệp không đổi** (dạng ②/③ ra tệp giống hệt dạng ①) ⇒ vi phạm `:1280`.
- Ở dạng ③ tệp vẫn **chỉ có 1 nhãn kỳ** trong khi màn hiển thị nhiều điểm trend.
- **Nhánh A xuất được nhưng nhánh B (QTHT) bị chặn bằng chuỗi tiếng Anh thô "Forbidden"** ⇒ vẫn là
  **Reopen**: đây là vế **(a) đối tác có nêu** (ô *TKM phản hồi lần 1*), và câu chữ đó trái yêu cầu của
  `:117` — hệ thống khi từ chối vì thiếu quyền phải nói bằng thông báo tiếng Việt cho biết người dùng
  không có quyền xem báo cáo.
- Nhánh B bị chặn bằng **đúng khuôn tiếng Việt của `:117`** ⇒ **không** Fail vì câu chữ, nhưng khi đó còn
  tranh chấp *"QTHT có được xuất BC không"* mà đặc tả im lặng ⇒ **cần BA** (kèm mâu thuẫn hành vi: app cho
  QTHT **XEM** được báo cáo — ảnh đối tác có đủ số liệu — nhưng cấm **XUẤT**; nếu QTHT thật sự không có
  quyền thì `:79` bước 1 phải chặn ngay từ bước Xem).

**KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):
tên sheet · thứ tự cột · đóng khung/tô màu/in đậm · có hay không dòng tổng cuối bảng · định dạng số và
ngày trong ô · biểu đồ có nhúng vào tệp hay không · số lượng sheet · cách viết nhãn kỳ · kỳ rỗng có hiện
thành điểm 0 hay bị bỏ · thẻ *Tổng ngân sách toàn kỳ* · URL không cập nhật khi đổi loại BC · thông báo
hiện dạng lớp nổi hay inline · mã lỗi có lộ ra giao diện hay không · **tên tệp khác literal
`BaoCaoChuongTrinh_…` mà đối tác ghi**, miễn vẫn đúng khuôn `:85`+`:86`+`srs-v3.5.md:6716` (BA chốt
2026-08-04 / 2026-08-06 — xem khối trích ở mục 2) · khổ giấy A4 và font Times New Roman cỡ 13 bên trong
tệp `.xlsx` **không** dùng để chặn Pass ở lượt này *(đặc tả `:85` có nêu, nhưng đó là thuộc tính trình
bày khi in; đo được thì ghi nhận, không đo được thì ghi rõ "chưa đo" chứ không suy ra Fail)* ·
**thẻ Tổng chương trình toàn kỳ bằng 1 hay bằng bao nhiêu** (đặc tả không đòi ngưỡng số lượng).

## 5. Dạng dữ liệu phải phủ — M = 3

| # | Dạng | Cấu hình bộ lọc trên màn | Dùng để kiểm |
|---|---|---|---|
| ① | **Khớp khít cấu hình vòng 1 của đối tác** | Kỳ = **Năm**, Từ **01/01/2026** → Đến **31/12/2026**, Đơn vị = **Toàn quốc** | tái hiện đúng điều kiện ảnh vòng 1; đo (a)(b)(c)(d)(e) |
| ② | **Khớp khít cấu hình vòng 2 của đối tác — đơn vị cụ thể** | như ① nhưng Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** | tái hiện đúng điều kiện ảnh vòng 2; kiểm phạm vi đơn vị `:81`/`:1268` + bộ lọc đơn vị có vào tệp không (`:1280`) |
| ③ | **Kỳ nhiều điểm — dạng đặc tả nêu đích danh** | Kỳ = **Tháng** với khoảng thời gian phủ trọn 12 tháng năm 2026 (01/01/2026 → 31/12/2026). Nếu giao diện tự ép khoảng của kỳ Tháng về đúng 1 tháng thì chuyển sang Kỳ = **Khoảng tùy chọn** 01/01/2026 → 31/12/2026 — **ghi rõ ở mục 7 đã dùng cấu hình nào** | dạng **duy nhất** kiểm được `trend_data[]` **nhiều điểm** (`:1018`) và AC `:1023` (*"chọn 12 tháng → hiển thị biểu đồ trend"*); kỳ Năm chỉ ra 1 điểm nên không đủ. Đồng thời kiểm `:1280` theo chiều **kỳ báo cáo** |

**Nguồn xác định M** (tra theo thứ tự flow §"Xác định M", dừng ở bước ②):

- Bước ① *(đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo)*: `:1010` — *"Đếm CT theo **kỳ thời
  gian**"*; `:1012` Dimensions = *"**Kỳ, Trend**"*; `:82` giới hạn tập bản ghi ở **đã duyệt / hoàn thành
  / đã thanh toán**. ⇒ Chiều phân tích duy nhất của báo cáo này là **thời gian**, nên độ phủ phải đi theo
  **kỳ báo cáo**, không theo bộ lọc đặc thù.
- Bước ② *(bộ lọc + giá trị enum ngay trên màn đó)*: `:1008` — *"Kế thừa TPL-REPORT-FULL (**không bổ sung
  input**)"* và `:1086` cột *Bộ lọc đặc thù* = **"—"** ⇒ màn này **không có bộ lọc đặc thù**; chỉ còn
  `:69` (`ky_bao_cao` ∈ **TUAN / THANG / QUY / NAM / KHOANG** — 5 giá trị), `:70`–`:71` (tu_ngay/den_ngay)
  và `:1049` dropdown đơn vị (*"TW: 'Toàn quốc' + chọn BN/ĐP bất kỳ"*).
- Ràng buộc quyết định: `:1280` đòi **"File xuất theo bộ lọc hiện tại"**. Một cấu hình bộ lọc duy nhất
  chỉ chứng minh *hệ thống xuất được một tệp*, **không** chứng minh được tệp có bám bộ lọc — muốn kết
  luận phải có **≥ 2 cấu hình khác nhau** cho ra **≥ 2 nội dung khác nhau**. ⇒ **M = 1 không hợp lệ cho
  case này.** Thêm nữa, `:1018` đòi `trend_data[]` là **mảng theo kỳ** và `:1023` nói đích danh *"12
  tháng"* — kỳ Năm 01/01→31/12/2026 chỉ sinh **1** điểm, không đủ chứng minh chiều trend ⇒ **bắt buộc**
  phải có dạng ③. Chọn M = 3 để phủ **2 chiều lọc độc lập** (đơn vị `:81`/`:1049`, kỳ báo cáo `:69`) trên
  cùng một nền ①.

⚠️ Bẫy đã biết cho mục 5: nếu **mọi** chương trình đều thuộc **một** đơn vị thì dạng ② sẽ trùng dạng ①
và không phân biệt được "bộ lọc có tác dụng" với "bộ lọc bị bỏ qua" → khi đó phải mở thêm nhánh phụ **②b**
(chọn một đơn vị **không có** chương trình nào) để chứng minh bộ lọc đơn vị thật sự lọc dữ liệu, và ghi rõ
vào mục 6. Tương tự, nếu **mọi** chương trình rơi vào **cùng một tháng** thì dạng ③ chỉ ra 1 điểm — khi
đó tiền đề chưa đủ, phải seed thêm chương trình ở tháng khác (mục 3) chứ không được coi như đã đóng.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên / QTHT**, đơn vị **BTP · TW** (góc phải màn, avatar `QV`) — **cả 2 vòng giống hệt nhau** | Đo **cả 2 nhánh**. **A** `cbnv_tw_04` — `/auth/me` trả `hoTen="CB Nghiệp vụ - Trung ương #04"`, `vaiTro=["CB_NV_TW"]`, `capDonVi="TW"`, `donViId=00000000-0000-4000-8000-000000000001`, màn hiện `BTP · TW`, phạm vi Toàn quốc (đúng tác nhân `:62`/`:1006`). **B** `admin` — `hoTen="Quản trị hệ thống"`, `vaiTro=["QTHT"]`, `capDonVi="TW"`, cùng `donViId` ⇒ **trùng khít vai trò + cấp + đơn vị của đối tác** (chỉ khác họ tên hiển thị: env đối tác là *"Quản trị viên"*, env này là *"Quản trị hệ thống"*). Danh tính kiểm **trước và sau** mỗi phép đo quyết định — trước = sau ở cả 2 nhánh | **Không** |
| Entity + trạng thái | **CHUONG_TRINH_HTPL**. Cả 2 ảnh chỉ lộ 3 thẻ **Tổng chương trình toàn kỳ = 1 · Tổng DN toàn kỳ = 0 · Tổng ngân sách toàn kỳ = 0**; báo cáo tạo thành công (*Thời điểm tạo* 16/07/2026 16:57 và 31/07/2026 15:35) ⇒ dữ liệu **có**, không rơi nhánh `:113`. Biểu đồ đường có **1 điểm mốc** | Cùng entity **CHUONG_TRINH_HTPL**. Trong kỳ 2026 báo cáo đếm **6** chương trình (Tổng DN 0 · Tổng ngân sách 250.000.000 ₫), rải trên **2 tháng**: *Tháng 1/2026 = 5 · Tháng 3/2026 = 1*, 10 tháng còn lại = 0 (cộng dọc = 6). Số bản ghi khác đối tác nhưng **cùng nhánh nghiệp vụ**: báo cáo CÓ dữ liệu (không rơi `:113`) và rơi vào **≥2 kỳ con** như mục 5 đòi | **Không** — triệu chứng tái hiện nằm ở tầng quyền (403 trước khi sinh tệp), không phụ thuộc số bản ghi; đã kiểm chéo bằng dạng ③ (12 kỳ con) và ②b (0 bản ghi), kết quả nhất quán |
| Dữ liệu tiền đề | 1 chương trình trong kỳ 2026 trên env `htpldn-uat.ospgroup.vn`; báo cáo **có dữ liệu** ⇒ lỗi xuất tệp **không** do rỗng dữ liệu | Env verify có sẵn **14 chương trình** (`GET /api/v1/chuong-trinh-htpls`): DU_THAO 3 · CHO_PHE_DUYET 1 · HUY 1 · TAM_DUNG 1 · **DA_DUYET 5 · DA_CONG_BO 1 · DANG_THUC_HIEN 1 · HOAN_THANH 1**; 6 trong số đó lọt bộ đếm của báo cáo và rơi vào 2 tháng khác nhau ⇒ đủ điều kiện đo dạng ③ ⇒ **KHÔNG cần seed, KHÔNG tạo/sửa/xoá bản ghi nào** | **Không** |
| Input / filter / giá trị nhập | Vòng 1: Kỳ **Năm** · **01/01/2026 → 31/12/2026** · Đơn vị **Toàn quốc**. Vòng 2: y hệt nhưng Đơn vị **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**. Không có ô lọc đặc thù nào (khớp `:1008`). Thao tác **[Xem báo cáo] rồi [Xuất Excel]** (đúng điều kiện hiển thị nút ở `:1052`) | **Giống hệt** ở dạng ① (khớp vòng 1) và dạng ② (khớp vòng 2), cho **cả nhánh A và nhánh B**. URL sinh ra trùng khít ảnh vòng 1: `/bao-cao?loai=ct-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`, bản dạng ② thêm `&donViId=00000000-0000-4000-8000-000000000001`. Xác nhận `:1052`: nút [Xuất Excel] **bị khoá** cho tới khi bấm [Xem báo cáo], và khoá lại khi báo cáo rỗng (dạng ②b). Xác nhận `:1008`: màn **không có** ô lọc đặc thù nào | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | **M = 2** — 2 cấu hình (Toàn quốc / BTP-TW), đều Kỳ **Năm** ⇒ trend chỉ 1 điểm; đối tác **không** thử kỳ nhiều điểm ⇒ bằng chứng của họ không nói được gì về `trend_data[]` nhiều điểm lẫn `:1280` theo chiều kỳ | Nhánh A: **M = 3** (① Kỳ Năm · Toàn quốc — ② Kỳ Năm · đơn vị BTP-TW — ③ Kỳ Tháng · 12 mốc) **+ 1 nhánh phụ ②b** (đơn vị Bộ Công an, 0 bản ghi). Nhánh B: dạng ① (đủ để tái hiện triệu chứng đối tác nêu). N = 6 chương trình ở dạng ①/②/③, 0 ở ②b | **Không** — dạng ② rơi đúng ca suy biến đã cảnh báo ở mục 5 (mọi CT thuộc cùng 1 đơn vị nên số liệu trùng dạng ①); đã đóng bằng **②b** chứng minh bộ lọc đơn vị thật sự lọc dữ liệu, và bằng **dạng ③** chứng minh nội dung tệp đổi theo bộ lọc kỳ |

**3 dữ kiện neo của đối tác:**

- URL/bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  (vòng 1 — URL đúng loại BC). Vòng 2 thanh địa chỉ còn giữ URL cũ `loai=ct-theo-linh-vuc&…&donViId=00000000-0000-4000-8000-000000000001`
  trong khi màn hiển thị *BC Chương trình theo thời gian* — đã đối chiếu nội dung ảnh, xem khối ghi nhận ở
  mục 1. Không có ID bản ghi đơn lẻ — đây là màn báo cáo tổng hợp, "bản ghi" chính là tập CT trong kỳ.
- Trạng thái entity: **1 chương trình** toàn kỳ (Tổng DN 0, Tổng ngân sách 0); báo cáo đã tạo thành công,
  *Thời điểm tạo* 16/07/2026 16:57 (vòng 1) và 31/07/2026 15:35 (vòng 2).
- Vai trò + env + bản dựng: **Quản trị viên / QTHT**, `BTP · TW`, env **`htpldn-uat.ospgroup.vn`**,
  bản dựng **V1.0** (vòng 1, 16/07/2026 16:58) và **V1.0.3** (vòng 2, 31/07/2026 15:35).

**Giới hạn hiệu lực (KHÔNG phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`; lượt này
đo trên env nội bộ `18.143.165.120.nip.io` theo chỉ định. Mọi kết luận Pass ở đây là **Pass tạm**, chỉ có
hiệu lực cho env + bản dựng ghi ở đầu file, cho tới khi bản dựng đó lên env của đối tác.

---

## 7. Kết quả đo (giai đoạn B)

**Bộ bắt thông báo:** script dùng chung `tools/toast-capture.js` (không lọc trùng · đọc `innerText` ·
đếm request). **Tự kiểm trước mỗi lượt: `soObserverDangSong = 1`** ⇒ số liệu hợp lệ (mọi lượt đều = 1).
Đếm thông báo theo **mốc giờ khác nhau**; mọi lượt đều **1 request ↔ 1 khung thông báo**, không có
double-toast. **Bổ sung bộ ghi chữ theo thời gian** (đọc `innerText` mỗi 100 ms) vì thư viện giao diện
**dùng lại một khung** và **đổi chữ tại chỗ** — chỉ nghe `addedNodes` thì bắt được chữ đầu
(*"Đang tạo file..."*) mà mất chữ cuối (*"Tạo file thành công."* / *"Forbidden"*).
**Bẫy cache máy chủ đã loại trừ:** trường *Thời điểm tạo* đổi theo từng lượt Xem báo cáo
(14:10 → 14:16 → 14:30 → 14:35 → 14:36 → 14:37), không phải số cũ đọc lại.

> ⚠️ **Bản dựng đổi giữa phiên.** Lượt đo đầu của nhánh A (14:10–14:19) chạy trên bó mã
> `assets/index-CNwX9JjX.js`; từ 14:22 env đã đổi sang `assets/index-DIABnbIr.js` mà chuỗi phiên bản
> vẫn in **V1.0.8**. Đã **đo lại toàn bộ nhánh A** trên bó mã mới (14:28–14:38). **Bảng dưới là số của
> bó mã mới**; kết quả 2 bó mã **giống nhau ở mọi tiêu chí** (đối chiếu ở tệp `.txt` kèm theo).

### Nhánh A — `cbnv_tw_04` (CB_NV_TW, cấp TW) — vai trò đặc tả, dùng để chấm

| Tiêu chí mục 4 | Đo được | Đạt? |
|---|---|:-:|
| (a) Giao được tệp, 0 thông báo lỗi | Dạng ①: 1 request `POST /api/v1/bao-cao/export` → **200**; 1 khung thông báo (1 mốc giờ), chữ **"Đang tạo file..." → "Tạo file thành công."**; **không** có *"Không thể tạo file xuất. Vui lòng thử lại."* và **không** có *"Forbidden"*; **tệp về máy** | ✅ |
| (b) Tệp là .xlsx thật | 6.758 byte, magic `PK\x03\x04`, giải nén có `xl/workbook.xml`, **mở được bằng `openpyxl`** | ✅ |
| (c) Tên tệp đúng khuôn `:85`+`:86`+`srs-v3.5.md:6716` | `BaoCaoCtTheoThoiGian_20260806_1430.xlsx` — khớp `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`, không dấu / khoảng trắng / dấu câu; `20260806_1430` = đúng ngày giờ bấm nút; dài 41 ký tự (≤ 255). Các lượt khác ra `_1436`, `_1437` ⇒ **xuất nhiều lần trong ngày không đè tệp** | ✅ |
| (d) Phần đầu tệp đủ 5 mảnh (`:1092`) | A1 *BC Chương trình theo thời gian* · A2 *Kỳ báo cáo: Năm* **+** *(từ 01/01/2026 đến 31/12/2026)* · A3 *Đơn vị: Toàn quốc* · A4 *Ngày tạo: 06/08/2026* ⇒ đủ tiêu đề + kỳ + khoảng thời gian + đơn vị + ngày tạo | ✅ |
| (e1) Có chuỗi trend theo kỳ (`:1018`) | Tệp có khối **"Theo kỳ"** với hàng tiêu đề `Kỳ \| Từ ngày \| Đến ngày \| Số chương trình \| …` — mỗi dòng là **một kỳ thời gian** mang **cả nhãn kỳ lẫn số chương trình**. Dạng ③ cho **12 dòng** *Tháng 1/2026 … Tháng 12/2026* | ✅ |
| (e2) Tổng toàn kỳ + khớp số trên màn | Dạng ①: thẻ *Tổng chương trình toàn kỳ* trên màn = **6** ↔ ô A8 trong tệp = **6**; hàng kỳ duy nhất trên màn *(Năm 2026 · 01/01/2026 · 31/12/2026 · 6)* ↔ hàng A20–F20 y hệt. Dạng ③: **12 điểm trên biểu đồ = 12 hàng trên màn = 12 hàng trong tệp**, khớp từng hàng (*Tháng 1 = 5 · Tháng 3 = 1 · 10 tháng còn lại = 0*) | ✅ |
| (e3) Cộng khớp | Dạng ③: 5 + 1 + 0×10 = **6** = ô A8 *Tổng số chương trình toàn kỳ* = thẻ tổng trên màn | ✅ |
| (f) Áp đúng bộ lọc hiện tại (`:1280`) | Dạng ③ (Kỳ Tháng): tệp `_1436` có **12 nhãn kỳ khác nhau**, A2 đổi thành *"Kỳ báo cáo: Tháng (từ 01/01/2026 đến 31/12/2026)"* — **khác hẳn** tệp dạng ① (1 nhãn kỳ). Dạng ② (đơn vị BTP-TW): A3 đổi thành *"Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp"*. Dạng ②b (đơn vị Bộ Công an): màn báo *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* (đúng `:113`) + [Xuất Excel]/[Xuất PDF] **bị khoá** ⇒ bộ lọc đơn vị thật sự lọc | ✅ |

⇒ **Nhánh A: đạt cả 6 tiêu chí.** Không tái hiện được câu *"Không thể tạo file xuất. Vui lòng thử lại."*
của vòng 1, cũng không gặp *"Forbidden"*.

### Nhánh B — `admin` (QTHT) — trùng khít vai trò đối tác, đối chứng

| Bước | Đo được |
|---|---|
| [Xem báo cáo] | `GET /api/v1/bao-cao/ct-theo-thoi-gian?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**. Màn hiện **đầy đủ**: Tổng chương trình toàn kỳ 6 · Tổng DN 0 · Tổng ngân sách 250.000.000 + biểu đồ + bảng *Theo kỳ*. **0 thông báo**, không bị chặn ⇒ **QTHT XEM ĐƯỢC báo cáo.** |
| [Xuất Excel] | 1 request `POST /api/v1/bao-cao/export` → **403**. 1 khung thông báo (1 mốc giờ), chữ người dùng thấy: **"Đang tạo file..." → "Forbidden"** (khung `position: fixed`, rộng 1432 × cao 40 px, sống 3,401 giây). **Không có tệp nào được giao.** Thân phản hồi: `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","timestamp":"2026-08-06T07:23:25.836Z","requestId":"bf96f7f7-e505-4dec-913e-930a903f70d9"}}`. Tái hiện **2 lần**, kết quả y hệt |

⇒ **Tái hiện ĐÚNG triệu chứng vòng 2 của đối tác**, trên env verify + bản dựng V1.0.8
(`index-DIABnbIr.js`). Rơi đúng nhánh `❌ FAIL nếu` áp chót của mục 4: chữ hiển thị là chuỗi tiếng Anh
thô **"Forbidden"**, trong khi `:117` đòi hệ thống khi từ chối vì thiếu quyền phải cho người dùng biết
**bằng tiếng Việt rằng họ không có quyền xem báo cáo**. Kèm **mâu thuẫn hành vi**: `:79` bước 1 đặt việc
kiểm quyền truy cập báo cáo ở đầu luồng, nhưng thực tế bước Xem cho qua (200) rồi mới chặn ở bước Xuất
(403).

### Đường đo thứ hai

Giao diện ↔ máy chủ **không mâu thuẫn**: mọi kết luận đều có đủ 2 nguồn — chữ đọc bằng `innerText` trên
DOM **và** mã + thân phản hồi lấy từ `list_network_requests` / `get_network_request`
(A: các lượt `POST /bao-cao/export` đều **200** kèm `content-disposition: attachment; filename="BaoCaoCtTheoThoiGian_…xlsx"`
và tệp thật đã mở đọc bằng `openpyxl` · B: **403** kèm thân JSON `Forbidden`, không tệp).
Thân yêu cầu của 2 nhánh **cùng khuôn**
(`{"loaiBaoCao":"BC_CT_THEO_THOI_GIAN","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","formatXuat":"XLSX"}`),
chỉ khác phiên đăng nhập.

### Hạn chế đã ghi nhận

- **Không chụp được ảnh lớp thông báo** (cả 2 nhánh; đã thử 3 lượt: chụp ngay sau khi bấm · 2 lượt hẹn
  giờ bấm sau 2500 ms rồi mới chụp). Thư viện giao diện dựng lớp thông báo qua portal — **tiền lệ đã
  có** ở BUG-QLTLPLCVV-015, BUG-SLCTHT-006, BUG-CTTLV-005 trong chính đợt này. Bằng chứng thay thế =
  chữ đọc bằng `innerText` + số đo chứng minh khung hiển thị **thật** với người dùng (`position: fixed`,
  rộng **1432 px**, cao 40 px, sống 2,5–3,4 giây) + nguyên văn phản hồi máy chủ. Lưu ở
  [`image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt`](../image/CTTTG_04-thong-bao-va-phan-hoi-may-chu.txt).
- **2 lượt xuất không rơi tệp xuống thư mục tải về** dù máy chủ trả 200 kèm `content-disposition`:
  lượt 14:32 (bấm bằng lệnh `click()` hẹn giờ, **không** phải cử chỉ người dùng thật) và lượt 14:37 của
  dạng ② (bấm chuột thật, nhưng là lượt tải liên tiếp thứ 3 trong ít phút). **Không** kết luận thành lỗi
  phần mềm: 6 lượt khác trong cùng phiên tệp về máy bình thường, và **2 phép đo quyết định** (dạng ①
  lúc 14:30, dạng ③ lúc 14:36) đều có tệp thật trên đĩa. Với lượt 14:37 đã lấy **nguyên si thân phản
  hồi** làm bằng chứng thay thế và mở đọc được bằng `openpyxl`.
- **Dạng ③ không đạt được bằng thao tác trên màn** — xem §Phát hiện mới (2). Đã đạt bằng cách mở đúng
  địa chỉ trên thanh địa chỉ trình duyệt, sau đó **bấm nút [Xuất Excel] thật** trên màn (không gọi
  thẳng API). Khai rõ ở đây và trong tệp `.txt`.
- Thao tác quyết định của dạng ① ở **cả 2 nhánh** dùng **công cụ bấm chuột thật** của trình duyệt.

### Dữ liệu đã seed / thay đổi trên env

**KHÔNG seed, KHÔNG tạo/sửa/xoá bất kỳ bản ghi nào.** Env đã sẵn 14 chương trình, trong đó 6 chương
trình lọt bộ đếm và rơi vào 2 tháng khác nhau — đủ điều kiện dạng ③ mà mục 5 đòi. Toàn bộ thao tác là
đọc (`GET` báo cáo) + xuất tệp (`POST /bao-cao/export`, chỉ sinh tệp, không đổi dữ liệu nghiệp vụ).
Có đăng xuất `cbnv_tw_04` → đăng nhập `admin` (nhánh B) → đăng nhập lại `cbnv_tw_04` (đo lại trên bó mã
mới). Tab đo dùng **ngữ cảnh trình duyệt riêng** (`cttlg04-qa`) nên không đụng phiên đăng nhập của phiên
QA khác đang chạy song song.

### Hai điểm ghi nhận riêng (mục 2) — kết quả

1. **Thẻ "Tổng DN toàn kỳ" (`:1018`, chốt 2026-07-24 *bỏ `so_dn`*).** Bản dựng V1.0.8 (`index-DIABnbIr.js`)
   **VẪN CÒN**: thẻ *Tổng DN toàn kỳ = 0* trên màn · đường *Số DN* trong chú giải biểu đồ · cột *Số DN*
   trong bảng *Theo kỳ* · trong tệp xuất là khối `Tổng số DN toàn kỳ | 0` và cột E *Số DN*. Loại BC anh
   em *BC Chương trình theo lĩnh vực* (case `CTTLV_05`, đo cùng ngày) thì **đã gỡ**. ⇒ **Trái `:1018`**
   (đặc tả nói rõ) → thuộc diện **log lỗi mới**, xem §Phát hiện mới (1).
2. **Thẻ "Tổng ngân sách toàn kỳ".** Bản dựng vẫn hiện thẻ này (250.000.000 ₫) + cột *Tổng ngân sách*
   trong bảng và trong tệp. Đặc tả `:1016`–`:1020` **không liệt kê** ngân sách cho FR-IX-23 nhưng cũng
   **không có câu bỏ** như đã làm với `so_dn`; loại BC anh em FR-IX-21 lại **có** `tong_ngan_sach`
   (`:944`) ⇒ **đặc tả im lặng** → **đã thêm mục hỏi BA**, KHÔNG log lỗi.

### 🔴 Phát hiện mới ngoài vế đối tác nêu — CHƯA mở phiếu

Cả 2 phát hiện dưới đây **không kéo verdict** (flow §Ca biên): phép đo quyết định của các vế đối tác nêu
chạy ở dạng ① và không bị chúng làm sai lệch. Đã tra cửa ② (grep toàn bộ `bug-report*.md` kể cả file
`Pass-`, tra theo **triệu chứng**): **chưa có phiếu nào**. Theo quy tắc của đợt, bug ngoài phạm vi cần
**mở dòng mới trên bảng theo dõi** phải được **phiên chính duyệt mã trước** ⇒ **đã DỪNG và báo về phiên
chính**, không tự ghi.

1. **Báo cáo vẫn thống kê "Số DN" dù đặc tả đã bỏ.** `:1018` ghi rõ *"[CTTLV_04 chốt 2026-07-24: bỏ
   `so_dn` — CSV UC146 chỉ 'thống kê chương trình theo thời gian', không có số DN; không có mô hình
   CT↔DN. Cùng lý do FR-IX-22.]"*; danh sách Output đặc thù `:1016`–`:1020` chỉ còn `trend_data[]`
   `{ky_label, so_ct}` · `chart_type` · `tong_ct`. Thực tế bản dựng vẫn in số DN ở **4 chỗ** (thẻ ·
   chú giải biểu đồ · cột bảng trên màn · khối + cột trong tệp xuất), luôn bằng 0.
   Ảnh: [`image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png`](../image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png).
2. **Không chọn được "12 tháng" trên màn ⇒ AC `:1023` không với tới được bằng giao diện.** `:1023` ghi
   *"Given CB chọn 12 tháng When tạo BC Then hiển thị biểu đồ trend số CT theo thời gian"*. Đo được
   (14:33–14:35): ô *Thời gian* **không phải ô chọn ngày** — là 2 ô ẩn hệ thống tự suy từ ô *Kỳ báo cáo*.
   Kỳ **Năm** → tự đặt 01/01–31/12/2026 → **1 điểm**; Kỳ **Tháng** → tự ép về **đúng 1 tháng**
   (01/08–31/08/2026) → **1 điểm**; Kỳ **Khoảng tùy chọn** → có ô chọn ngày, đặt 01/01–31/12/2026 →
   **vẫn 1 điểm** (nhãn *"01/01/2026 - 31/12/2026"*), không tách theo tháng. Máy chủ thì **làm được**:
   gọi `kyBaoCao=THANG` kèm khoảng cả năm trả về đủ **12 mốc** (dạng ③). ⇒ Đây là **thiếu ở giao diện**,
   không phải thiếu ở máy chủ.
   Ảnh: [`image/CTTTG_04-A7-dang3-ky-Thang-12-diem-ban-dung-moi-truoc-khi-xuat.png`](../image/CTTTG_04-A7-dang3-ky-Thang-12-diem-ban-dung-moi-truoc-khi-xuat.png)
   (trạng thái 12 mốc, đạt được qua thanh địa chỉ chứ không qua thao tác trên màn).

### Ảnh đã chụp (mỗi ảnh 1 dòng: tên tệp + thấy gì)

| Ảnh | Thấy gì |
|---|---|
| [`image/CTTTG_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png`](../image/CTTTG_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png) | Nhánh A, bó mã **cũ** `index-CNwX9JjX.js`; vai trò *CB Nghiệp vụ - Trung ương #04* (`BTP · TW`, avatar CƯ); bộ lọc trùng khít ảnh vòng 1 của đối tác (BC Chương trình theo thời gian · Năm · 01/01–31/12/2026 · Toàn quốc); *Thời điểm tạo 06/08/2026 14:10*, ba thẻ **6 · 0 · 250,000,000**, bảng *Theo kỳ* có cột **Số DN** |
| [`image/CTTTG_04-A2-dang1-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png`](../image/CTTTG_04-A2-dang1-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png) | Nhánh A, bó mã cũ, lượt hẹn giờ bấm trước 2500 ms — **không** bắt được lớp thông báo; màn không có thông báo lỗi nào |
| [`image/CTTTG_04-A3-dang3-ky-Thang-12-diem-man-hinh-truoc-khi-xuat-V108.png`](../image/CTTTG_04-A3-dang3-ky-Thang-12-diem-man-hinh-truoc-khi-xuat-V108.png) | Nhánh A dạng ③ trên bó mã cũ: biểu đồ đường **12 mốc Tháng 1…12/2026**, *Thời điểm tạo 14:16* |
| [`image/CTTTG_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png`](../image/CTTTG_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png) | Nhánh A dạng ②b trên bó mã cũ: Đơn vị = **Bộ Công an (BCA)** → *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"*, [Xuất Excel] và [Xuất PDF] **xám / bị khoá** |
| [`image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png`](../image/CTTTG_04-A5-dang1-doluong-lai-tren-ban-dung-moi-truoc-khi-xuat.png) | **Đo lại trên bó mã mới** `index-DIABnbIr.js`: cùng vai trò, cùng bộ lọc dạng ①, *Thời điểm tạo 06/08/2026 14:30*, ba thẻ **6 · 0 · 250,000,000** — trạng thái màn ngay trước khi bấm [Xuất Excel]. Cũng là ảnh cho §Phát hiện mới (1): còn thẻ *Tổng DN toàn kỳ* + chú giải *Số DN* + cột *Số DN* |
| [`image/CTTTG_04-A6-dang1-hen-gio-bam-xuat-excel-truoc-2500ms-ban-dung-moi.png`](../image/CTTTG_04-A6-dang1-hen-gio-bam-xuat-excel-truoc-2500ms-ban-dung-moi.png) | Nhánh A, bó mã mới, lượt hẹn giờ bấm trước 2500 ms — **vẫn không** bắt được lớp thông báo; màn không có thông báo lỗi nào |
| [`image/CTTTG_04-A7-dang3-ky-Thang-12-diem-ban-dung-moi-truoc-khi-xuat.png`](../image/CTTTG_04-A7-dang3-ky-Thang-12-diem-ban-dung-moi-truoc-khi-xuat.png) | Nhánh A dạng ③ trên bó mã mới: biểu đồ **12 mốc**, bảng *Theo kỳ* 12 hàng (Tháng 1 = 5 · Tháng 3 = 1 · còn lại 0), *Thời điểm tạo 14:36* — trạng thái ngay trước khi bấm [Xuất Excel] |
| [`image/CTTTG_04-A8-dang2b-donvi-BoCongAn-khong-co-du-lieu-ban-dung-moi.png`](../image/CTTTG_04-A8-dang2b-donvi-BoCongAn-khong-co-du-lieu-ban-dung-moi.png) | Nhánh A dạng ②b trên bó mã mới: Đơn vị = **Bộ Công an (BCA)** → *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"*, 2 nút xuất **bị khoá** |
| [`image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](../image/CTTTG_04-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png) | Nhánh B: vai trò **Quản trị hệ thống** (avatar QT, `BTP · TW`), bộ lọc dạng ① trùng khít ảnh đối tác; **báo cáo XEM ĐƯỢC đầy đủ** — Tổng chương trình toàn kỳ 6 + biểu đồ + bảng; nút [Xuất Excel] đang bật |
| [`image/CTTTG_04-B2-qtht-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png`](../image/CTTTG_04-B2-qtht-hen-gio-bam-xuat-excel-truoc-2500ms-V108.png) | Nhánh B, lượt hẹn giờ bấm [Xuất Excel] trước 2500 ms: nút đang được chọn, màn giữ nguyên báo cáo; **ảnh không bắt được lớp thông báo "Forbidden"** — chữ và phản hồi 403 ghi ở tệp `.txt` kèm theo |

## 8. Verdict

### 🔁 **Reopen**

**Case gộp 3 vế** (mục 1) → theo §Ca biên của flow: *còn ≥1 vế lỗi → Reopen*.

| Vế | Kết quả |
|---|---|
| (a) Không xuất được tệp | **CÒN LỖI ở vai trò của đối tác.** Vai trò đặc tả (CB Nghiệp vụ TW) xuất được bình thường; nhưng chính vai trò **QTHT** mà đối tác dùng ở **cả 2 vòng** vẫn bị chặn ở bước xuất, và chữ hiện ra vẫn đúng chuỗi **"Forbidden"** của vòng 2 — trái yêu cầu `srs-fr-11-bao-cao.md:117`. Câu của vòng 1 (`:116`) thì không còn tái hiện |
| (b) Tên tệp | **Đạt.** `BaoCaoCtTheoThoiGian_20260806_1430.xlsx` đúng khuôn `:85`+`:86`+`srs-v3.5.md:6716` (áp quyết định BA ngày 2026-08-04 / 2026-08-06), không chấm Fail vì khác literal `BaoCaoChuongTrinh_…` của đối tác |
| (c) Nội dung tệp + tự động tải về | **Đạt.** Tệp tự về máy khi bấm nút; đủ 5 mảnh phần đầu `:1092`; có **chuỗi trend theo kỳ** `{nhãn kỳ, số CT}` đúng `:1018`; số khớp màn từng hàng (12/12 hàng ở dạng ③) và cộng dọc = tổng; áp đúng bộ lọc `:1280` |

0 GAP (đủ 5 dòng mục 6) · M = 3 + 1 nhánh phụ ②b · chạy đủ luồng bằng thao tác giao diện thật · có
đường đo thứ hai · 2 nhánh vai trò đo trên **cùng một bó mã**. Đủ điều kiện ra verdict.

⚠️ **Giới hạn hiệu lực:** kết luận này chỉ có hiệu lực cho môi trường `18.143.165.120.nip.io` và bản
dựng **V1.0.8** bó mã **`assets/index-DIABnbIr.js`**. Đối tác báo lỗi trên `htpldn-uat.ospgroup.vn` —
chưa đối chiếu bản dựng của env đó. Phần đã hết lỗi (vế b, c và nhánh CB Nghiệp vụ của vế a) là **đạt
tạm**, cho tới khi bản dựng này lên env của đối tác.

⚠️ **Không kết luận "fix đã có tác dụng":** không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng
trước khi sửa, nên chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**.

---

## Mục sửa đổi

| Thời điểm | Sửa gì | Vì sao |
|---|---|---|
| 2026-08-06 14:03 | Viết xong mục 1–6 (cột *Đối tác*), mục 7–8 để trống | Cổng giai đoạn A: viết tiêu chí **trước** khi mở màn Báo cáo thống kê trên env verify |
| 2026-08-06 14:05 | Thay số đo bịa sẵn ở cột *Mình test lần này* + dòng bản dựng bằng `*(điền ở giai đoạn B)*` | Tự phát hiện đã điền trước khi đo — vi phạm chính cổng giai đoạn A |
| 2026-08-06 14:40 | Điền dấu vân tay bản dựng · cột *Mình test lần này* + *GAP?* của mục 6 · toàn bộ mục 7 · mục 8 | Kết thúc giai đoạn B |

**Mục 4 và mục 5 KHÔNG bị sửa sau khi bắt đầu đo** — ngưỡng chấm và độ phủ giữ nguyên như lúc 14:03.
Việc **bản dựng đổi giữa phiên** (`index-CNwX9JjX.js` → `index-DIABnbIr.js`) được xử bằng cách **đo lại
nhánh A**, không bằng cách nới tiêu chí.
