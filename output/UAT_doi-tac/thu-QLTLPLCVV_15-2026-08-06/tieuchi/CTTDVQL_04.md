# Tiêu chí verify — CTTDVQL_04 (tab `bug`, dòng 272)

Mã case: CTTDVQL_04          Thời điểm viết: 2026-08-06 12:50 (viết XONG trước khi mở màn Báo cáo thống kê)
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** (chuỗi phiên bản in
ở chân logo sidebar; **dấu vân tay bó mã giao diện `assets/index-CNwX9JjX.js`**) — đo lúc 2026-08-06 12:54–13:08.
Tab đo được **mở MỚI trong phiên này** bằng `new_page` với `isolatedContext="cttdvql04"` (cách ly cookie +
bộ nhớ khỏi phiên QA khác đang chạy song song trên cùng trình duyệt), nên chắc chắn chạy bản dựng hiện hành.

⚠️ **Đọc kỹ tên case trước khi đo:** nhãn batch cũ ghi `CT` = "chi trả" là **SAI**. Màn thật của case này là
**BC Chương trình theo đơn vị** (`CT` = **Chương trình**), URL mang `?loai=ct-theo-don-vi`, đặc tả tương ứng là
**FR-IX-21 (UC144)** chứ không phải nhóm Chi phí (UC138–UC142). Đã đối chiếu 2 ảnh bằng chứng: cả *Loại báo cáo*
trên form, *tiêu đề khối kết quả* và *tham số URL* đều ghi **BC Chương trình theo đơn vị / `ct-theo-don-vi`**
⇒ bằng chứng **đúng case này**.

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A của flow):
- `thu-QLTLPLCVV_15-2026-08-06/tieuchi/SLCTHT_06.md` (case cùng lô, cùng màn *Báo cáo thống kê*, khác loại BC —
  FR-IX-20/UC143) và `bug-report.md` § BUG-SLCTHT-006 · `cau-hoi-BA.md` Mục 2 + Mục 3.
- `thu-QLTLPLCVV_15-2026-08-06/tieuchi/QLTLPLCVV_15.md` (lấy văn phong + cách ghi hạn chế chụp lớp thông báo).

⚠️ Các hồ sơ trên chứa **số đo cũ của một loại báo cáo KHÁC** (vd "7 chương trình", "tệp
`BaoCaoSoLuongCtHoTro_20260806_1224.xlsx`", "QTHT bị 403"). Theo flow §BƯỚC 0 — *cùng chữ không có nghĩa cùng
nguyên nhân*: mỗi loại báo cáo là một truy vấn/luồng xuất riêng. Mục 4 và mục 5 dưới đây suy từ **đặc tả**
(`srs-fr-11-bao-cao.md` + `srs-v3.5.md` Phụ lục E §H8, đã mở file đọc từng dòng), **không** lấy số đo cũ làm
ngưỡng — cụ thể tiêu chí (e) đòi tệp khớp **số hiện trên màn tại thời điểm đo của chính màn này**, không chốt
cứng con số nào; và triệu chứng "Forbidden" của case kia **không** được dùng thay cho phép đo của case này.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** (tách theo ô `Kết quả mong đợi` + `Kết quả thực tế` + `TKM phản hồi lần 1`):

- **(a) Không xuất được tệp.** Bấm **[Xuất Excel]** trên màn *Báo cáo thống kê* với *Loại báo cáo* =
  **BC Chương trình theo đơn vị** thì hệ thống **không giao tệp nào**, chỉ hiện thông báo lỗi.
  - Vòng 1 (16/07/2026, bản dựng **V1.0**): thông báo đỏ ✗ **"Không thể tạo file xuất. Vui lòng thử lại."**
  - Vòng 2 (31/07/2026, bản dựng **V1.0.3**): thông báo đỏ ✗ **"Forbidden"** — **đổi hẳn câu chữ**, sang một
    chuỗi tiếng Anh thô.
- **(b) Tên tệp.** Kỳ vọng của đối tác: tệp tải về tên `BaoCaoChuongTrinh_{YYYYMMDD_HHmm}.xlsx`.
- **(c) Nội dung tệp.** Kỳ vọng của đối tác: *"Hệ thống xuất **toàn bộ** và tự động tải tệp về máy người dùng"*
  — tệp phải chứa trọn dữ liệu báo cáo đang xem, không phải một phần.

**Lệch giữa 2 vòng bằng chứng** (bắt buộc ghi theo §Cổng bằng chứng): **cùng** URL, **cùng** vai trò
(*Quản trị viên / QTHT*, `BTP · TW`), **cùng** bộ lọc, **cùng** số liệu trên màn (5 / 0); **khác** bản dựng
(V1.0 → V1.0.3) và **khác hẳn câu thông báo**. ⇒ Không được coi 2 vòng là cùng một triệu chứng; vế (a) phải
đo cho **cả hai** câu thông báo.

**Bằng chứng đã mở đọc full-res:**

- `partner-evidence/CTTDVQL_04.jpg` (vòng 1). Thấy: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`;
  chân logo sidebar **`HTPLDN · V1.0`**; góc phải `BTP · TW` + chuông `99+` + avatar `QV` +
  **Quản trị viên QTHT**; breadcrumb *Trang chủ / Báo cáo thống kê*; **thông báo đỏ ✗ "Không thể tạo file xuất.
  Vui lòng thử lại."** nổi giữa đỉnh trang; form lọc: *Loại báo cáo* = **BC Chương trình theo đơn vị**,
  *Kỳ báo cáo* = **Năm**, *Thời gian* **Từ 01/01/2026 — Đến 31/12/2026**, *Đơn vị* = **Toàn quốc**;
  **màn KHÔNG có ô lọc đặc thù nào khác** (chỉ 3 ô Kỳ + Thời gian + Đơn vị — khớp `:931`);
  hàng nút **[Xem báo cáo] [Xuất Excel] [Xuất PDF]**; khối kết quả **"BC Chương trình theo đơn vị"** —
  *Kỳ: Năm · Khoảng thời gian: 01/01/2026 → 31/12/2026 · Đơn vị: Toàn quốc*, **Thời điểm tạo: 16/07/2026 16:48**,
  hai thẻ **Tổng chương trình = 5** và **Tổng ngân sách = 0**, nút **[Ẩn biểu đồ]** + biểu đồ cột (trục tung tới 3);
  đồng hồ máy **04:48 PM 2026-07-16**.
- `partner-evidence/CTTDVQL_04_v2.jpg` (vòng 2). Thấy: **cùng URL, cùng bộ lọc, cùng vai trò Quản trị viên QTHT /
  `BTP · TW`**; chân logo **`HTPLDN · V1.0.3`**; **thông báo đỏ ✗ "Forbidden"** ở đúng vị trí đó; khối kết quả
  **Thời điểm tạo: 31/07/2026 15:29**, hai thẻ **Tổng chương trình = 5** và **Tổng ngân sách = 0**, nút
  **[Ẩn biểu đồ]** + biểu đồ cột; menu sidebar đã cuộn xuống nhóm khác (Doanh nghiệp / Biểu mẫu / Tư vấn /
  Chương trình HTPLDN / Đợt báo cáo / **Báo cáo thống kê** đang active); trên thanh trình duyệt có **biểu tượng
  tải xuống** (dấu vết các lượt tải trước — ảnh không mở khay tải nên **không** chứng minh lượt này có tệp);
  đồng hồ máy **03:30 PM 2026-07-31**.

## 2. Đặc tả nói gì

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (đã mở file đọc trực tiếp từng dòng
dưới đây, không lấy số dòng từ trí nhớ).

**Vế (a) — quyền + luồng xuất** (`srs-fr-11-bao-cao.md`):

- `:62` — Preconditions chung TPL-REPORT-FULL: *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt
  (TW/BN/ĐP)"*.
- `:79` — Processing chung bước 1: `| 1 | Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01 |`
- `:81` — bước 3: *"Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc, BN chỉ thấy BN mình, ĐP chỉ thấy ĐP mình
  (BN và ĐP ngang cấp song song, không thấy nhau)"*.
- `:82` — bước 4: *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)"*
  (BR-RPT-01).
- `:1052` — SCR-IX-01 thành phần 8: `| 8 | action-bar | Nút Xuất Excel | button | "Xuất Excel (.xlsx)" → xuất
  theo format TT17/2025 | click → auto-download | Sau khi đã "Xem báo cáo" |`
- `:1058` — thành phần 14: `| 14 | content | Toast xuất file | toast | "Đang tạo file..." → "Xuất thành công"
  + auto-download | — | Khi nhấn xuất |`
- `:116` — E6: `| E6 | Lỗi xuất file | ERR-RPT-04 | "Không thể tạo file xuất. Vui lòng thử lại" | ERROR |`
  ← **đúng nguyên văn câu đối tác chụp ở vòng 1** ⇒ vòng 1 là **nhánh lỗi**, không phải nhánh thành công.
- `:117` — E7: `| E7 | Không có quyền | ERR-RPT-05 | "Bạn không có quyền xem báo cáo này" | ERROR |`
  ← đối chiếu với chuỗi **"Forbidden"** ở vòng 2.
- `:1268` — BR-AUTH-08: *"chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. TW thấy toàn quốc, BN
  thấy BN, ĐP thấy ĐP"*, cột **Ngoại lệ = "QTHT bypass"**, cột Áp dụng = *"Toàn bộ FR-IX"*.

**Vế (b) — tên tệp:**

- `srs-fr-11-bao-cao.md:85` — Processing chung bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman
  cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo
  `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]`"*.
- `srs-fr-11-bao-cao.md:123` — AC chung: *"**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx
  khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"*.
- `srs-fr-11-bao-cao.md:1092` — Quy tắc tương tác SCR-IX-01: *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ +
  đơn vị + ngày tạo vào header file… Tên tệp cả hai định dạng theo **Phụ lục E §H8** —
  `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"*.
- `srs-v3.5.md:6716` — **Phụ lục E §H8** (quy ước chung, nguồn thật của khuôn tên tệp): *"Áp cho **tệp kết xuất
  dữ liệu** phần mềm sinh ra theo yêu cầu người dùng (xuất danh sách, xuất báo cáo)… **Khuôn:**
  `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ
  mọi ký tự không phải chữ hoặc số (kể cả dấu gạch nối, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các
  đoạn… Phần giờ-phút bắt buộc để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa **255 ký tự**…
  `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]`"*.

> 🔴 **Kỳ vọng (b) của đối tác lệch đặc tả — nhưng BA ĐÃ chốt đúng điểm này.** Đối tác đòi literal
> `BaoCaoChuongTrinh_…`; quy ước H8 suy tên tệp từ **tên loại báo cáo** (*"BC Chương trình theo đơn vị"*), không
> phải một chuỗi cố định. Cả `:85`, `:1092` và `srs-v3.5.md:6716` đều gắn nhãn nguồn + ngày **`[BA chốt
> 2026-08-04]`** / **`[BA chốt 2026-08-06]`**, tức **sau** cả 2 vòng test của đối tác (16/07 và 31/07). Theo
> §Rẽ nhánh của flow (*"Ngoại lệ duy nhất — BA ĐÃ chốt trước đúng điểm tranh chấp này, dẫn được nguồn kèm ngày →
> áp quyết định có sẵn"*), vế (b) **áp khuôn của đặc tả**, KHÔNG đẩy sang cần-BA và KHÔNG chấm Fail vì tên khác
> literal của đối tác. Phần `_{YYYYMMDD_HHmm}` thì đối tác và đặc tả **trùng khớp** ⇒ vẫn là tiêu chí bắt buộc.

**Vế (c) — nội dung tệp:**

- `srs-fr-11-bao-cao.md:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header
  file."*
- `srs-fr-11-bao-cao.md:1280` — BR-DATA-06: *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện
  tại**, không vượt quá 10,000 rows/file"*, Áp dụng = *"Toàn bộ FR-IX"*.
- `srs-fr-11-bao-cao.md:87` — bước 9: *"Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo"*.
- `srs-fr-11-bao-cao.md:88` — bước 10: *"Ghi nhật ký thao tác (xem/xuất báo cáo)"* (BR-DATA-05, xem `:1274`).
- `srs-fr-11-bao-cao.md:94`–`:101` — **Output chung** (Điều kiện cột 4 của cả 8 dòng đều là **"Luôn"**):
  `ten_bao_cao` · `ky_bao_cao` · `tu_ngay / den_ngay` · `don_vi_ten` (*"Tên đơn vị hoặc 'Toàn quốc'"*) ·
  `ngay_tao_bc` · `nguoi_tao` · `tong_ban_ghi` · `data[]`.
- **FR-IX-21 (UC144) `:918`–`:948`** — *BC CT theo đơn vị*:
  - `:927` Mô tả: *"Báo cáo **cross-tab** chương trình theo đơn vị: **hàng = đơn vị, cột = số CT + ngân sách**."*
  - `:929` Tác nhân: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*
  - `:931` Template: *"Kế thừa TPL-REPORT-FULL (**không bổ sung input**)"* ⇒ màn này **không có bộ lọc đặc thù**,
    chỉ có Kỳ + Thời gian + Đơn vị (khớp đúng 2 ảnh đối tác).
  - `:933` Công thức: *"Đếm CT + tính tổng ngân sách theo đơn vị, trong kỳ"*
  - `:935` Dimensions: *"Đơn vị (TW/BN/ĐP), Số CT, Ngân sách tổng"*
  - `:941`–`:945` **Output đặc thù**, cột *Điều kiện* của cả 5 dòng đều là **"Luôn"**:
    `don_vi_id` (ID đơn vị) · `ten_don_vi` (Tên đơn vị) · `cap_don_vi` (**TW / BN / DP**) · `so_ct` (Số CT) ·
    `tong_ngan_sach` (**money** — Tổng ngân sách)
  - `:948` AC bổ sung: *"**Given** CB TW tạo BC **When** hiển thị **Then** cross-tab: hàng = đơn vị, cột = số CT
    + ngân sách"*
- `srs-fr-11-bao-cao.md:1084` — Mapping 23 loại BC: `| | UC144 | BC CT theo đơn vị | — | Bar cross-tab |`
  ⇒ cột *Bộ lọc đặc thù* là **"—"** (xác nhận lại `:931`), biểu đồ là **Bar cross-tab**.
- `srs-fr-11-bao-cao.md:113` — E3: `| E3 | Không có dữ liệu | INF-RPT-01 | "Không có dữ liệu báo cáo cho kỳ và
  đơn vị đã chọn" | INFO |`

**IM LẶNG về** (⇒ CẤM chấm Fail vì mấy thứ này):
tên sheet trong workbook · thứ tự cột trong tệp · có đóng khung / tô màu / in đậm không · có dòng tổng cuối bảng
không · định dạng số tiền và định dạng ngày cụ thể trong ô · đơn vị tiền tệ ghi thế nào · biểu đồ có được nhúng
vào tệp `.xlsx` không · tệp xuất có mấy sheet · thông báo lỗi hiển thị ở dạng lớp nổi hay inline · mã lỗi có lộ
ra giao diện hay không · **vai trò QTHT có được XEM/XUẤT báo cáo hay không** (`:62` và `:929` chỉ **liệt kê**
CB NV / CB PD, **không** viết câu cấm QTHT; `:1268` lại cho QTHT **bypass** phạm vi đơn vị — hai chỗ này không đủ
để kết luận QTHT bị cấm) · **giá trị `tong_ngan_sach` bằng 0 có phải lỗi không** (`:945` chỉ đòi trường này tồn
tại kiểu *money*, không quy định phải > 0; chương trình chưa khai ngân sách thì 0 là hợp lệ).

## 3. Precondition

- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → menu **Báo cáo thống kê** → *Loại báo cáo* =
  **BC Chương trình theo đơn vị** (URL mang `?loai=ct-theo-don-vi`).
- **Tài khoản — đo CẢ 2 nhánh, cùng bộ tiêu chí:**

  | Nhánh | Tài khoản | Vai trò | Dùng để |
  |---|---|---|---|
  | **A — ra verdict** | `cbnv_tw_04` / `Test@1234` | CB_NV_TW, cấp TW ⇒ phạm vi *Toàn quốc*, khớp `BTP · TW` của đối tác; đúng tác nhân `:62` + `:929`; đúng chủ thể của AC `:948` (*"CB TW tạo BC"*) | quyết Pass / Reopen |
  | **B — đối chứng** | `admin` / `Secret@123` | QTHT — **trùng khít vai trò trên cả 2 ảnh đối tác** | giải thích triệu chứng **"Forbidden"** vòng 2; đóng dòng GAP *Vai trò / tài khoản* |

  Tài khoản quản trị **không** được dùng để ra verdict (quyền rộng che lỗi phân quyền) — nhánh B chỉ đối chứng,
  nhưng **không được bỏ**: bỏ thì không đóng được dòng GAP *Vai trò / tài khoản*.
  Rule 7 nếu khoá: fallback **cùng vai trò + cùng cấp** `cbnv_tw_04` → `cbnv_tw_05` → `cbnv_tw_03`…, tuyệt đối
  không đổi vai trò/cấp; ghi rõ tài khoản THỰC đã dùng.
- **Xác nhận danh tính token NGAY TRƯỚC và NGAY SAU mỗi phép đo quyết định** (có phiên QA khác chạy song song
  trên cùng trình duyệt + cùng env): gọi `/api/v1/auth/me` hoặc giải mã JWT, ghi lại `tenDangNhap` + `vaiTro` +
  `donViId` + `capDonVi` vào mục 7. **Trước ≠ sau ⇒ phép đo VÔ HIỆU**, đăng nhập lại và đo lại.
- **Dữ liệu tiền đề:** ≥ 1 chương trình HTPL trong khoảng **01/01/2026 – 31/12/2026** ở trạng thái được `:82`
  cho phép đếm (đã duyệt / hoàn thành / đã thanh toán), thuộc phạm vi TW. Để đo được **cả 3 dạng ở mục 5** thì
  cần thêm: các chương trình **không dồn hết vào một kỳ con** (để dạng ③ ra số khác dạng ①). Kiểm trước bằng màn
  **CT HTPLDN** hoặc `GET /api/v1/chuong-trinh-htpls`.
  Thiếu → **được seed** qua BE API (`create → submit → approve bằng tài khoản KHÁC → publish/activate/complete
  bằng người tạo`, mỗi bước cần `version`; endpoint số nhiều `/api/v1/chuong-trinh-htpls`, tra `/api/docs-json`)
  và **bắt buộc khai** bản ghi nào · đổi gì · env nào vào mục 7 + bug entry.
  Tiền đề **tạo được mà không tạo → CẤM mọi verdict, kể cả ô trống.**
- **Bẫy cache máy chủ:** báo cáo thống kê có cache phía máy chủ. Sau khi seed mà số không đổi → đọc trường
  **"Thời điểm tạo"** (`ngayTaoBc`) trên màn; ép khoá cache mới bằng cách **đổi `denNgay` 1 ngày**.
  `cache:'reload'` chỉ bust cache trình duyệt ⇒ không dùng làm căn cứ.

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 6 điều dưới đây (đo được):**

- **(a) Nhánh A giao được tệp, không có thông báo lỗi.** Với `cbnv_tw_04`, ở dạng dữ liệu ① mục 5: bấm
  **[Xem báo cáo]** → chờ khối kết quả hiện → bấm **[Xuất Excel]**. Đo bằng bộ bắt thông báo cài **trước** khi
  bấm: **0** thông báo mang nội dung lỗi/từ chối (đếm theo **mốc giờ khác nhau**, không theo số phần tử), và hệ
  thống **giao ra một tệp** (tệp về máy, hoặc phản hồi máy chủ của chính thao tác đó có thân nhị phân tải về
  được). Số request của thao tác đếm bằng `list_network_requests` (nút có thể là GET nên `window.__qa.net` của
  bộ bắt thông báo không ghi).
- **(b) Tệp là .xlsx thật.** Mở được bằng thư viện đọc xlsx (`openpyxl`) hoặc giải nén zip đọc được
  `xl/workbook.xml` — **không** phải HTML/JSON đổi đuôi. (Mã 200 + có bytes **không** đủ để đạt (b).)
- **(c) Tên tệp đúng khuôn `:85` + `:1092` + `srs-v3.5.md:6716`:** dạng `<Tên>_<8 chữ số>_<4 chữ số>.xlsx`,
  trong đó `<Tên>` là **tên loại báo cáo viết liền, không dấu tiếng Việt, không khoảng trắng, không dấu gạch nối,
  không dấu câu**, và `<8 chữ số>_<4 chữ số>` là **ngày `YYYYMMDD` + gạch dưới + giờ phút `HHmm`** khớp thời điểm
  xuất (sai lệch ≤ 5 phút so với đồng hồ lúc bấm nút). Kiểm bằng biểu thức: `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`;
  tổng độ dài ≤ 255 ký tự. Xuất **2 lần trong cùng ngày** phải ra **2 tên khác nhau** (không đè tệp).
- **(d) Trong tệp có đủ phần đầu theo `:1092` + Output chung `:94`–`:98`:** đọc nội dung ô của tệp phải tìm thấy
  **tiêu đề báo cáo**, **kỳ báo cáo**, **khoảng thời gian tu_ngay–den_ngay**, **tên đơn vị** (hoặc "Toàn quốc"),
  **ngày tạo báo cáo**. Đủ 5 mảnh ⇒ đạt; thiếu bất kỳ mảnh nào ⇒ không đạt.
- **(e) Tệp mang đúng hình hài cross-tab của FR-IX-21 VÀ số liệu KHỚP màn** — phép đo quyết định, không được bỏ:
  - **(e1) Chiều đơn vị + 2 cột bắt buộc** (`:927`, `:942`, `:944`, `:945`, `:948`): trong tệp phải có một **bảng
    mà mỗi hàng là một đơn vị**, và trên hàng đó có **cả hai** giá trị **số CT** và **tổng ngân sách**. Thiếu
    hẳn chiều đơn vị (chỉ có mấy thẻ tổng) ⇒ không đạt. Thiếu **một trong hai** cột ⇒ không đạt.
  - **(e2) Khớp số với màn:** mọi thẻ tổng đang hiện trên màn (tối thiểu *Tổng chương trình* và *Tổng ngân sách*)
    có mặt trong tệp với **đúng con số đó**, đo ở **cùng một lần "Xem báo cáo"**; mỗi hàng đơn vị trong tệp có mặt
    trên màn với **cùng số CT và cùng ngân sách**; **số hàng đơn vị của tệp = số hàng đơn vị trên màn**.
  - **(e3) Cộng khớp:** cộng dọc cột *số CT* của các hàng đơn vị = thẻ *Tổng chương trình*; cộng dọc cột *ngân
    sách* = thẻ *Tổng ngân sách*. Lệch ⇒ theo §"phép đo đang nói dối" là số đang sai, **phải đo lại**, chưa được
    kết luận.
- **(f) Áp đúng bộ lọc hiện tại (`:1280`)** — chứng minh bằng **so sánh giữa các dạng ở mục 5**: nội dung tệp của
  dạng ② (đơn vị cụ thể) và dạng ③ (kỳ hẹp hơn) **khác** nội dung tệp dạng ①, và mỗi tệp khớp đúng màn của chính
  bộ lọc đó theo tiêu chí (e). Riêng dạng ②: bảng cross-tab trong tệp **rút gọn còn đúng đơn vị đã chọn**
  (`:81` + `:1049`), và dòng *Đơn vị* ở phần đầu tệp đổi theo.

**Nhánh B (đối chứng, `admin`/QTHT) — không quyết Pass/Fail của case, nhưng bắt buộc đo và ghi:** lặp lại đúng
dạng ① rồi ghi nhận: xuất được tệp, **hay** bị từ chối. Nếu bị từ chối thì đọc **nguyên văn** chữ hiện ra và đối
chiếu `:117`; đồng thời ghi bước [Xem báo cáo] cho qua hay bị chặn (để đối chiếu `:79`).

**❌ FAIL nếu (bất kỳ điều nào):**

- Nhánh A bấm [Xuất Excel] mà **không có tệp nào được giao**, hoặc hiện thông báo mang nghĩa từ chối/thất bại
  (gồm nhưng không giới hạn ở đúng 2 câu đối tác chụp).
- Tệp giao ra **không mở được** bằng thư viện đọc xlsx (HTML/JSON/tệp hỏng đổi đuôi).
- Tên tệp **không** có phần ngày-giờ `_YYYYMMDD_HHmm` trước `.xlsx`, hoặc còn dấu tiếng Việt / khoảng trắng /
  dấu gạch nối / dấu câu trong phần tên báo cáo, hoặc xuất 2 lần cùng ngày ra **cùng một tên**.
- Tệp **thiếu** bất kỳ mảnh nào trong 5 mảnh phần đầu ở (d).
- Tệp **không có chiều đơn vị**, hoặc thiếu **một trong hai** cột *số CT* / *tổng ngân sách* ở (e1) — đây chính là
  vế (c) *"xuất toàn bộ"* mà đối tác nêu, chiếu theo hình hài cross-tab đặc tả đòi ở `:927` + `:948`.
- Bất kỳ số nào trong (e2) **lệch** so với màn, hoặc số hàng đơn vị của tệp khác số hàng trên màn.
- Đổi bộ lọc mà **nội dung tệp không đổi** (dạng ②/③ ra tệp giống hệt dạng ①) ⇒ vi phạm `:1280`.
- **Nhánh A xuất được nhưng nhánh B (QTHT) bị chặn bằng chuỗi tiếng Anh thô "Forbidden"** ⇒ vẫn là **Reopen**:
  đây là vế **(a) đối tác có nêu** (ô *TKM phản hồi lần 1*), và câu chữ đó trái yêu cầu của `:117` — hệ thống khi
  từ chối vì thiếu quyền phải cho người dùng biết **bằng tiếng Việt rằng họ không có quyền xem báo cáo**.
- Nhánh B bị chặn bằng **đúng khuôn tiếng Việt của `:117`** ⇒ **không** Fail vì câu chữ, nhưng khi đó còn tranh
  chấp *"QTHT có được xuất BC không"* mà đặc tả im lặng ⇒ **cần BA** (kèm mâu thuẫn hành vi: app cho QTHT **XEM**
  được báo cáo — ảnh đối tác có đủ số liệu 5 / 0 — nhưng cấm **XUẤT**; nếu QTHT thật sự không có quyền thì `:79`
  bước 1 phải chặn ngay từ bước Xem).

**KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):
tên sheet · thứ tự cột · đóng khung/tô màu/in đậm · có hay không dòng tổng cuối bảng · định dạng số tiền và ngày
trong ô · ghi đơn vị tiền tệ thế nào · biểu đồ có nhúng vào tệp hay không · số lượng sheet · thông báo hiện dạng
lớp nổi hay inline · mã lỗi có lộ ra giao diện hay không · **tên tệp khác literal `BaoCaoChuongTrinh_…` mà đối
tác ghi**, miễn vẫn đúng khuôn `:85` + `srs-v3.5.md:6716` (BA chốt 2026-08-04 / 2026-08-06 — xem khối trích ở
mục 2) · **`Tổng ngân sách` bằng 0** (`:945` không đòi > 0) · khổ giấy A4 và font Times New Roman cỡ 13 bên trong
tệp `.xlsx` **không** dùng để chặn Pass ở lượt này *(đặc tả `:85` có nêu, nhưng đó là thuộc tính trình bày khi in;
đo được thì ghi nhận, không đo được thì ghi rõ "chưa đo" chứ không suy ra Fail)*.

**Xử lý riêng — `don_vi_id` `:941` và `cap_don_vi` `:943`** (cả hai *Điều kiện* = "Luôn"): ghi nhận có/không trên
**cả 3 mặt** (màn · tệp xuất · phản hồi máy chủ của chính lời gọi báo cáo). Thiếu ở **cả 3** mặt ⇒ **không tự
chấm Fail case này**, mà xử theo §Ca biên của flow (*phát hiện mới đối tác không nêu* — đối tác chỉ nêu "xuất
toàn bộ", không nêu thiếu cột cấp đơn vị): ghi thành phát hiện riêng, **không kéo verdict**. Lý do pre-commit:
AC `:948` chỉ chốt cross-tab **2 cột** (số CT + ngân sách); `don_vi_id` là định danh nội bộ, không phải thứ người
dùng đọc trên tệp.

## 5. Dạng dữ liệu phải phủ — M = 3

Màn này **không có bộ lọc đặc thù** (`:931` — *"không bổ sung input"*; `:1084` cột *Bộ lọc đặc thù* = **"—"**),
nên chiều biến thiên nằm hết ở **Kỳ + Thời gian** và **Đơn vị**.

| # | Dạng | Cấu hình bộ lọc trên màn | Dùng để kiểm |
|---|---|---|---|
| ① | **Khớp khít cấu hình đối tác** | Kỳ = **Năm**, Từ **01/01/2026** → Đến **31/12/2026**, Đơn vị = **Toàn quốc** | tái hiện đúng điều kiện 2 ảnh bằng chứng; đo (a)(b)(c)(d)(e) |
| ② | **Đơn vị cụ thể** | như ① nhưng Đơn vị = **một đơn vị cụ thể có dữ liệu** (ưu tiên *Cục Bổ trợ tư pháp - Bộ Tư pháp*) | kiểm phạm vi 2-tier `:81` + `:1049`: cross-tab phải **rút gọn còn đúng đơn vị đó**, và bộ lọc đơn vị có vào tệp không (`:1280`) |
| ③ | **Kỳ hẹp hơn** | như ① nhưng Kỳ = **Quý / Tháng / Khoảng tùy chọn**, chọn khoảng con của 2026 sao cho **số CT khác** dạng ① | kiểm bộ lọc kỳ `:1048` có được áp vào tệp không (`:1280`); đối tác chưa từng thử đổi kỳ |

**Nguồn xác định M** (tra theo thứ tự flow §"Xác định M", dừng ở bước ②):

- Bước ① *(đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo)*: `:933` công thức — *"Đếm CT + tính tổng ngân
  sách **theo đơn vị**, **trong kỳ**"*; `:935` Dimensions — *"**Đơn vị (TW/BN/ĐP)**, Số CT, Ngân sách tổng"*
  ⇒ dữ liệu vào báo cáo biến thiên theo **2 chiều: đơn vị và kỳ**.
- Bước ② *(bộ lọc + giá trị enum ngay trên màn đó)*: `:1048` bộ lọc kỳ BC — *"Tuần / Tháng / Quý / Năm / Khoảng
  tùy chọn"* (**5 giá trị**) · `:1049` dropdown đơn vị — *"TW: 'Toàn quốc' + chọn BN/ĐP bất kỳ"* · `:931` + `:1084`
  xác nhận **không có** bộ lọc đặc thù nào khác.
- Ràng buộc quyết định: `:1280` đòi **"File xuất theo bộ lọc hiện tại"**. Một cấu hình bộ lọc duy nhất chỉ chứng
  minh *hệ thống xuất được một tệp*, **không** chứng minh được tệp có bám bộ lọc — muốn kết luận phải có **≥ 2
  cấu hình khác nhau** cho ra **≥ 2 nội dung khác nhau**. ⇒ **M = 1 không hợp lệ cho case này.** Chọn M = 3 để
  phủ **đúng 2 chiều lọc mà màn này có** (đơn vị `:81`/`:1049` và kỳ `:1048`) trên cùng một nền ①.

⚠️ **Bẫy suy biến đã lường trước cho mục 5** (ghi trước khi đo, không phải sửa sau):

- Nếu **mọi chương trình trên env đều thuộc một đơn vị** thì dạng ② ra số liệu **trùng** dạng ① và không phân biệt
  được *"bộ lọc có tác dụng"* với *"bộ lọc bị bỏ qua"*. Khi đó **bắt buộc thêm nhánh phụ ②b**: chọn **một đơn vị
  KHÁC** (không có chương trình) — nếu màn ra *"Không có dữ liệu…"* (`:113`) hoặc bảng cross-tab đổi hẳn thì bộ lọc
  đơn vị **thật sự lọc**, GAP đóng; phải ghi rõ đã dùng ②b.
- Nếu **mọi chương trình rơi vào cùng một kỳ con** thì dạng ③ trùng dạng ①. Khi đó thử **kỳ Khoảng tùy chọn** với
  khoảng cắt đôi tập dữ liệu; vẫn trùng thì ghi rõ **hạn chế** này vào mục 7 thay vì coi như đã đóng.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên / QTHT**, đơn vị **BTP · TW** (góc phải màn: `BTP · TW` + avatar `QV` + *Quản trị viên* + `QTHT`) — **cả 2 vòng giống hệt nhau** | Đo **cả 2 nhánh**. **A** `cbnv_tw_04` — `/auth/me` trả `hoTen "CB Nghiệp vụ - Trung ương #04"`, `vaiTro ["CB_NV_TW"]`, `capDonVi "TW"`, `donViId 00000000-0000-4000-8000-000000000001`; có `read_bao_cao` + `export_bao_cao` (đúng tác nhân `:62`/`:929`). **B** `admin` — `hoTen "Quản trị hệ thống"`, `vaiTro ["QTHT"]`, `capDonVi "TW"`, **cùng `donViId`** ⇒ **trùng khít vai trò + cấp + đơn vị `BTP · TW` của đối tác** (chỉ khác họ tên người dùng); `permissions` là **mảng rỗng**. Danh tính đo **TRƯỚC và SAU** mỗi phép đo quyết định đều **giống nhau** ⇒ không bị phiên QA song song đè | **Không** |
| Entity + trạng thái | **CHUONG_TRINH_HTPL**. Cả 2 ảnh chỉ lộ 2 thẻ tổng: **Tổng chương trình = 5**, **Tổng ngân sách = 0**; báo cáo tạo thành công (*Thời điểm tạo* 16/07/2026 16:48 và 31/07/2026 15:29) ⇒ dữ liệu **có**, không rơi nhánh `:113`. Ảnh không lộ bảng cross-tab theo đơn vị (bị cắt dưới biểu đồ) | Cùng entity **CHUONG_TRINH_HTPL**. Kỳ Năm 2026 đếm được **7** chương trình, **tổng ngân sách 350.000.000 ₫** (5 Đã duyệt + 1 Đang thực hiện + 1 Hoàn thành — khớp `:82`). Số bản ghi khác đối tác nhưng **cùng nhánh nghiệp vụ**: báo cáo CÓ dữ liệu (không rơi `:113`), cross-tab có đúng 1 hàng đơn vị như ảnh đối tác chỉ có 1 cột biểu đồ | **Không** — triệu chứng tái hiện nằm ở tầng quyền (403 trước khi sinh tệp), không phụ thuộc số bản ghi; đã kiểm chéo bằng dạng ③ (2 bản ghi) và ②b (0 bản ghi), kết quả nhất quán |
| Dữ liệu tiền đề | 5 chương trình trong kỳ 2026 trên env `htpldn-uat.ospgroup.vn`; ngân sách tổng = 0 ⇒ lỗi xuất tệp **không** do rỗng dữ liệu | Env verify có sẵn **14 chương trình** (`GET /api/v1/chuong-trinh-htpls`): DU_THAO 3 · CHO_PHE_DUYET 1 · HUY 1 · TAM_DUNG 1 · DA_DUYET 5 · DA_CONG_BO 1 · DANG_THUC_HIEN 1 · HOAN_THANH 1; ngày bắt đầu trải từ 01/01/2026 đến 31/08/2026 nên **cắt kỳ được** ⇒ **KHÔNG cần seed, KHÔNG tạo/sửa/xoá bản ghi nào** | **Không** |
| Input / filter / giá trị nhập | Kỳ **Năm** · **01/01/2026 → 31/12/2026** · Đơn vị **Toàn quốc**; **không có ô lọc đặc thù nào** trên màn (khớp `:931`); thao tác **[Xem báo cáo] rồi [Xuất Excel]** (đúng điều kiện hiển thị nút ở `:1052`) | **Giống hệt** ở dạng ①, cho **cả nhánh A và nhánh B** — URL sinh ra trùng khít ảnh đối tác: `/bao-cao?loai=ct-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Xác nhận màn **chỉ có 3 ô lọc** (Kỳ + Thời gian + Đơn vị), **không** có ô lọc đặc thù (khớp `:931` + `:1084`); dropdown Kỳ đúng **5 giá trị** *Tuần/Tháng/Quý/Năm/Khoảng tùy chọn* (`:1048`). Xác nhận `:1052`: nút [Xuất Excel] **bị khoá** cho tới khi bấm [Xem báo cáo], và khoá lại khi báo cáo rỗng | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | **M = 1** — 1 cấu hình bộ lọc duy nhất, lặp ở 2 vòng; đối tác **không** thử đổi đơn vị hay đổi kỳ ⇒ bằng chứng của họ không nói được gì về `:1280` | Nhánh A: **M = 3** (① Năm + Toàn quốc · ② Đơn vị BTP-TW · ③ Kỳ Khoảng 01/02→31/12/2026) **+ nhánh phụ ②b** (Đơn vị Bộ Công an — 0 bản ghi). Nhánh B: dạng ① (đủ tái hiện triệu chứng đối tác nêu). N = 7 chương trình ở dạng ①/②, 2 ở dạng ③, 0 ở dạng ②b | **Không** — dạng ② rơi đúng ca suy biến đã cảnh báo trước ở mục 5 (mọi CT cùng một đơn vị nên số trùng dạng ①); đã đóng bằng **②b** chứng minh bộ lọc đơn vị thật sự lọc, và bằng **③** chứng minh bộ lọc kỳ thật sự vào tệp |

**3 dữ kiện neo của đối tác:**

- URL/bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  (không có ID bản ghi đơn lẻ — đây là màn báo cáo tổng hợp, "bản ghi" chính là tập CT trong kỳ).
- Trạng thái entity: **5 chương trình** trong kỳ, **tổng ngân sách 0**; báo cáo đã tạo thành công, *Thời điểm tạo*
  **16/07/2026 16:48** (vòng 1) và **31/07/2026 15:29** (vòng 2).
- Vai trò + env + bản dựng: **Quản trị viên / QTHT**, `BTP · TW`, env **`htpldn-uat.ospgroup.vn`**, bản dựng
  **V1.0** (vòng 1, đồng hồ máy 16/07/2026 16:48) và **V1.0.3** (vòng 2, đồng hồ máy 31/07/2026 15:30).

**Giới hạn hiệu lực (KHÔNG phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`; lượt này đo trên
env nội bộ `18.143.165.120.nip.io` theo chỉ định. Mọi kết luận Pass ở đây là **Pass tạm**, chỉ có hiệu lực cho
env + bản dựng ghi ở đầu file, cho tới khi bản dựng đó lên env của đối tác.

---

## 7. Kết quả đo (giai đoạn B)

**Bộ bắt thông báo:** script dùng chung `tools/toast-capture.js` (không lọc trùng · đọc `innerText` · đếm
request). **Tự kiểm trước mỗi phép đo quyết định: `soObserverDangSong = 1`** ở CẢ 2 nhánh ⇒ số liệu hợp lệ.
Đếm thông báo theo **mốc giờ khác nhau**; mọi lượt đều **1 request ↔ 1 khung thông báo**, không double-toast.
Vì AntD cập nhật chữ **tại chỗ** trong cùng một khung (`message` dùng chung key) nên có cài thêm **1 observer
phụ mutation-driven** (không poll) đọc chuỗi chữ liên tiếp trong `.ant-message`. Số request đếm bằng
`list_network_requests` (bộ đếm của script chỉ ghi request khác GET).
**Bẫy cache máy chủ đã loại trừ:** trường *Thời điểm tạo* đổi theo từng lượt Xem báo cáo
(12:56 → 12:59 → 13:02 → 13:05), không phải số cũ.
**Tự vệ trước phiên QA song song:** tab riêng `isolatedContext="cttdvql04"`; danh tính `/auth/me` đo **trước
và sau** mỗi phép đo quyết định đều **trùng nhau** (nhánh A: `CB_NV_TW`/TW · nhánh B: `QTHT`/TW).

### Nhánh A — `cbnv_tw_04` (CB_NV_TW, cấp TW) — vai trò đặc tả, dùng để chấm

| Tiêu chí mục 4 | Đo được | Đạt? |
|---|---|:-:|
| (a) Giao được tệp, 0 thông báo lỗi | Dạng ①: **1** request `POST /api/v1/bao-cao/export`; **1** khung thông báo (1 mốc giờ), chữ **"Đang tạo file..." → "Tạo file thành công."**; **không** có *"Không thể tạo file xuất. Vui lòng thử lại."*, **không** có *"Forbidden"*. Tệp được giao thật: trang tự bấm `<a download="BaoCaoCtTheoDonVi_20260806_1257.xlsx">` kèm blob **6.693 byte**, MIME `…spreadsheetml.sheet` | ✅ |
| (b) Là .xlsx thật | Magic `PK\x03\x04`, giải nén có `xl/workbook.xml` + `xl/worksheets/sheet1.xml`, **mở được bằng `openpyxl`** (sheet *"Chương trình theo đơn vị"*) | ✅ |
| (c) Tên tệp đúng khuôn `:85`+`:1092`+`srs-v3.5.md:6716` | `BaoCaoCtTheoDonVi_20260806_1257.xlsx` — khớp `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`, PascalCase không dấu, không khoảng trắng/gạch nối/dấu câu, dài 39 ký tự (≤255); `20260806_1257` đúng ngày giờ bấm nút. Lượt sau ra `_1300`, `_1303` ⇒ **xuất nhiều lần trong ngày không đè tệp**, đúng chủ đích H8 | ✅ |
| (d) Phần đầu tệp đủ 5 mảnh (`:1092` + `:94`–`:98`) | A1 *BC Chương trình theo đơn vị* · A2 *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · A3 *Đơn vị: Toàn quốc* · A4 *Ngày tạo: 06/08/2026* | ✅ |
| (e1) Cross-tab đủ chiều đơn vị + 2 cột (`:927`,`:942`,`:944`,`:945`,`:948`) | A15 header **`Đơn vị | Cấp đơn vị | Số chương trình | Tổng ngân sách (₫)`**; A16 hàng dữ liệu **`Cục Bổ trợ tư pháp - Bộ Tư pháp | TW | 7 | 350000000`** ⇒ có **cả** cột số CT lẫn cột ngân sách, kèm cả `cap_don_vi` (`:943`) | ✅ |
| (e2) Khớp số với màn | Màn 7 / 350.000.000 ↔ tệp B8 = 7, B12 = 350000000; hàng đơn vị của tệp = đúng hàng duy nhất trên màn (7 / 350.000.000 ₫); **1 hàng đơn vị ở tệp = 1 hàng trên màn** | ✅ |
| (e3) Cộng khớp | Cộng dọc cột *Số chương trình* của các hàng đơn vị = 7 = thẻ *Tổng chương trình*; cộng dọc cột ngân sách = 350.000.000 = thẻ *Tổng ngân sách* | ✅ |
| (f) Áp đúng bộ lọc hiện tại (`:1280`) | Dạng ② (Đơn vị BTP-TW): tệp `_1300` đổi A3 thành *"Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp"*. Dạng ③ (Kỳ Khoảng 01/02→31/12/2026): tệp `_1303` đổi A2 thành *"Kỳ báo cáo: KHOANG (từ 01/02/2026 đến 31/12/2026)"*, **B8 = 2**, **B12 = 150000000**, hàng đơn vị **2 / 150000000** — khớp đúng màn (2 / 150.000.000). Dạng ②b (Đơn vị Bộ Công an): màn báo *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* (đúng `:113`) + nút [Xuất Excel] **bị khoá** | ✅ |

⇒ **Nhánh A: đạt cả 8 điểm đo của mục 4.** Không tái hiện được câu *"Không thể tạo file xuất. Vui lòng thử lại."*
của vòng 1, cũng không gặp *"Forbidden"*.

### Nhánh B — `admin` (QTHT) — trùng khít vai trò đối tác, đối chứng

| Bước | Đo được |
|---|---|
| [Xem báo cáo] | `GET /api/v1/bao-cao/ct-theo-don-vi?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**. Màn hiện **đầy đủ**: Tổng chương trình **7** · Tổng ngân sách **350.000.000** + biểu đồ cột + bảng cross-tab (*Cục Bổ trợ tư pháp - Bộ Tư pháp · TW · 7 · 350.000.000 ₫*). **0 thông báo**, không bị chặn ⇒ **QTHT XEM ĐƯỢC báo cáo.** |
| [Xuất Excel] | **1** request `POST /api/v1/bao-cao/export` → **403**. **1** khung thông báo (1 mốc giờ), chuỗi chữ người dùng đọc được: **"Đang tạo file..." → "Forbidden"**. **Không có tệp nào được giao** (0 blob, 0 thẻ tải xuống). Thân phản hồi: `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","timestamp":"2026-08-06T06:06:15.027Z","requestId":"05ed4987-9bce-4a93-930d-1de2eb3326ad"}}`. Thân yêu cầu gửi lên **giống hệt nhánh A**, chỉ khác phiên đăng nhập: `{"loaiBaoCao":"BC_CT_THEO_DON_VI","kyBaoCao":"NAM","tuNgay":"2026-01-01","denNgay":"2026-12-31","formatXuat":"XLSX"}` |

⇒ **Tái hiện ĐÚNG triệu chứng vòng 2 của đối tác**, trên env verify + bản dựng V1.0.8, ở đúng vai trò họ dùng.
Rơi đúng nhánh `❌ FAIL nếu` áp chót của mục 4: chữ hiển thị là chuỗi tiếng Anh thô **"Forbidden"**, trong khi
`:117` đòi hệ thống khi từ chối vì thiếu quyền phải cho người dùng biết **bằng tiếng Việt rằng họ không có
quyền xem báo cáo**. Kèm **mâu thuẫn hành vi**: `:79` bước 1 đặt việc kiểm quyền truy cập báo cáo ở **đầu**
luồng, nhưng thực tế bước Xem cho qua (200) rồi mới chặn ở bước Xuất (403).

### Đường đo thứ hai

Giao diện ↔ máy chủ ↔ nội dung tệp — **3 nguồn không mâu thuẫn**: chữ đọc bằng `innerText` trên DOM ·
mã + thân phản hồi lấy từ `list_network_requests` + `get_network_request` · nội dung tệp mở bằng `openpyxl`.
Phản hồi `GET /bao-cao/ct-theo-don-vi` trả **đủ 5 trường Output đặc thù `:941`–`:945`**
(`donViId` · `tenDonVi` · `capDonVi` · `soCt` · `tongNganSach`) và `chartType: "BAR_CROSS_TAB"` (đúng `:1084`)
⇒ **dòng "Xử lý riêng" ở mục 4 khép lại: `don_vi_id` và `cap_don_vi` đều có mặt** (`cap_don_vi` có cả trên màn,
trong tệp và trong phản hồi; `don_vi_id` có trong phản hồi) — không phát sinh vấn đề nào ở điểm này.
Đối chiếu chéo thêm bằng lời gọi máy chủ cùng phiên (chỉ đọc): `NAM 2026` → 7/350tr · `KHOANG 01/02–31/12`
→ 2/150tr · `QUY Q1` → 7/350tr · `QUY Q2` → 0 · `THANG 03/2026` → 1/50tr.

### Hạn chế đã ghi nhận

- **Ảnh lớp thông báo:** đã thử **3 lượt** — ① bấm nút thật rồi chụp ngay (trượt) · ② hẹn giờ bấm sau 2.500 ms
  rồi mới chụp (trượt) · ③ bấm lặp 8 lượt cách nhau 1.500 ms để lớp thông báo luôn hiện trên màn rồi chụp
  (**BẮT ĐƯỢC** — ảnh `CTTDVQL_04-B4-…`). Ngoài ảnh còn có số đo chứng minh khung thông báo hiển thị **thật**
  với người dùng: chữ *"Forbidden"*, khung `x=0 y=8 w=1432 h=56`, `opacity 1`, vùng chứa `position: fixed`
  `z-index 2010`, sống **3.370 ms**. 8 lượt lặp chỉ sinh thêm 8 lời gọi xuất đều 403, **không** đổi dữ liệu.
- Thao tác quyết định của dạng ① (cả 2 nhánh) dùng **công cụ bấm chuột thật** của trình duyệt; các lượt biến
  thể (②/②b/③ và 2 lượt chụp bổ sung của nhánh B) bấm bằng lệnh `click()` **trên đúng phần tử nút thật** trong
  trang — vẫn là sự kiện chuột do trình duyệt phát, không gọi thẳng API. Khai ra để người đọc biết.
- Dạng ② suy biến về số liệu (trùng dạng ①) vì mọi chương trình trên env đều thuộc một đơn vị — đã đóng bằng
  ②b + ③, xem mục 6.
- **Không đo** khổ giấy A4 / font Times New Roman cỡ 13 bên trong tệp `.xlsx` (thuộc tính trình bày khi in).
  Theo mục 4, **không** dùng để chặn Pass; ghi rõ là *chưa đo*.

### Ghi nhận ngoài phạm vi (đối tác KHÔNG nêu — không kéo verdict)

Ở dạng ③, dòng A2 của tệp xuất ghi nhãn kỳ bằng **mã nội bộ**: *"Kỳ báo cáo: **KHOANG** (từ 01/02/2026 đến
31/12/2026)"*, trong khi màn cùng lúc ghi *"Kỳ: **Khoảng**"* và tệp dạng ① ghi *"Kỳ báo cáo: **Năm**"*.
Đặc tả **im lặng** (`:1092` chỉ đòi *"chèn… thông tin kỳ"*; `:95` ghi format *"Kỳ đã chọn"*, không quy định
nhãn kỳ trong tệp phải là nhãn tiếng Việt) ⇒ theo §Ca biên của flow: **không mở phiếu lỗi**, chuyển thành
1 mục trong [`cau-hoi-BA.md`](../cau-hoi-BA.md) (Mục 4). **Không** ảnh hưởng verdict — bộ lọc của đối tác là
kỳ **Năm**, chỗ đó tệp ghi đúng *"Năm"*.

### Dữ liệu đã seed / thay đổi trên env

**KHÔNG seed, KHÔNG tạo/sửa/xoá bất kỳ bản ghi nào.** Env đã sẵn 14 chương trình, đủ cho cả 3 dạng mục 5.
Toàn bộ thao tác là đọc (`GET` báo cáo) + xuất tệp (`POST /bao-cao/export`, chỉ sinh tệp, không đổi dữ liệu
nghiệp vụ — đúng Postconditions `:105`). Có đăng xuất `cbnv_tw_04` rồi đăng nhập `admin` để đo nhánh B.

### Ảnh chụp + tệp xuất

| Tệp | Thấy gì |
|---|---|
| [`image/CTTDVQL_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png`](../image/CTTDVQL_04-A1-dang1-man-hinh-truoc-khi-xuat-V108.png) | Nhánh A, ngay **trước** khi bấm xuất: vai trò *CB Nghiệp vụ - Trung ương #04*, `BTP · TW`, bản dựng `HTPLDN · V1.0.8`; bộ lọc trùng khít ảnh đối tác (BC Chương trình theo đơn vị · Năm · 01/01/2026–31/12/2026 · Toàn quốc, **không có ô lọc đặc thù**); kết quả *Tổng chương trình 7 · Tổng ngân sách 350,000,000*, Thời điểm tạo 06/08/2026 12:56 |
| [`image/CTTDVQL_04-A2-dang1-ngay-sau-bam-xuat-excel-V108.png`](../image/CTTDVQL_04-A2-dang1-ngay-sau-bam-xuat-excel-V108.png) | Nhánh A, **ngay sau** khi bấm [Xuất Excel] (nút đang ở trạng thái vừa được bấm, viền xanh): **không có thông báo đỏ nào** ở đúng vị trí đỉnh trang mà 2 ảnh đối tác hiện *"Không thể tạo file xuất. Vui lòng thử lại."* và *"Forbidden"* |
| [`image/CTTDVQL_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png`](../image/CTTDVQL_04-A4-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png) | Nhánh A dạng ②b: Đơn vị = **Bộ Công an (BCA)**, kết quả là ảnh "Trống" + chữ *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"*; hai nút **[Xuất Excel] và [Xuất PDF] xám / bị khoá** |
| [`image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png`](../image/CTTDVQL_04-A5-dang3-ky-Khoang-01.02-31.12-man-hinh-truoc-khi-xuat-V108.png) | Nhánh A dạng ③: Kỳ *Khoảng tùy chọn* **01/02/2026 → 31/12/2026**, kết quả đổi thành *Tổng chương trình **2** · Tổng ngân sách **150,000,000***, Thời điểm tạo 06/08/2026 13:02 |
| [`image/CTTDVQL_04-B1-qtht-xem-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](../image/CTTDVQL_04-B1-qtht-xem-bao-cao-day-du-truoc-khi-bam-xuat-V108.png) | Nhánh B: vai trò **Quản trị hệ thống** (avatar `QT`, `BTP · TW`) **XEM ĐƯỢC** báo cáo đầy đủ — 7 / 350,000,000, Thời điểm tạo 06/08/2026 13:05; đây là trạng thái ngay trước thao tác [Xuất Excel] bị từ chối |
| [`image/CTTDVQL_04-B2-qtht-luot-chup-thu-1-ngay-sau-bam-xuat-excel-V108.png`](../image/CTTDVQL_04-B2-qtht-luot-chup-thu-1-ngay-sau-bam-xuat-excel-V108.png) | Nhánh B, **lượt chụp thứ 1** (bấm rồi chụp ngay): màn giữ nguyên 7 / 350,000,000, nút [Xuất Excel] đang ở trạng thái vừa bấm — **không bắt được** lớp thông báo |
| [`image/CTTDVQL_04-B3-qtht-luot-chup-thu-2-hen-gio-bam-truoc-2500ms-V108.png`](../image/CTTDVQL_04-B3-qtht-luot-chup-thu-2-hen-gio-bam-truoc-2500ms-V108.png) | Nhánh B, **lượt chụp thứ 2** (hẹn giờ bấm sau 2.500 ms rồi mới chụp): vẫn màn 7 / 350,000,000 của vai trò QTHT — **không bắt được** lớp thông báo |
| [`image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png`](../image/CTTDVQL_04-B4-qtht-thong-bao-Forbidden-khi-bam-xuat-excel-V108.png) | Nhánh B, **lượt chụp thứ 3 — BẮT ĐƯỢC**: lớp thông báo đỏ ✗ **"Forbidden"** nổi giữa đỉnh trang, trên nền màn *BC Chương trình theo đơn vị* của vai trò **Quản trị hệ thống** (`BTP · TW`, `HTPLDN · V1.0.8`), bộ lọc Năm · 01/01/2026–31/12/2026 · Toàn quốc, kết quả 7 / 350,000,000 — **đúng chỗ và đúng chữ** như ảnh vòng 2 của đối tác |
| [`image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt`](../image/CTTDVQL_04-thong-bao-va-phan-hoi-may-chu.txt) | Nguyên văn thông báo trên màn + phản hồi máy chủ + nội dung đầy đủ 3 tệp xuất của cả 2 nhánh |
| `testfiles/BaoCaoCtTheoDonVi_20260806_1257.xlsx` · `_1300.xlsx` · `_1303.xlsx` | 3 tệp xuất THẬT do chính thao tác trên giao diện giao ra (dạng ① / ② / ③), đã mở đọc bằng `openpyxl` |

## 8. Verdict

### 🔁 **Reopen**

**Case gộp 3 vế** (mục 1) → theo §Ca biên của flow: *còn ≥1 vế lỗi → Reopen*.

| Vế | Kết quả |
|---|---|
| (a) Không xuất được tệp | **CÒN LỖI ở vai trò của đối tác.** Vai trò đặc tả (CB Nghiệp vụ TW) xuất tệp bình thường; nhưng chính vai trò **QTHT** mà đối tác dùng vẫn bị chặn ở bước xuất, và chữ hiện ra vẫn đúng chuỗi **"Forbidden"** của vòng 2 — trái yêu cầu `srs-fr-11-bao-cao.md:117`. Câu của vòng 1 (`:116`) thì **không** còn tái hiện |
| (b) Tên tệp | **Đạt.** `BaoCaoCtTheoDonVi_20260806_1257.xlsx` đúng khuôn `:85` + `srs-v3.5.md:6716` (áp quyết định BA 2026-08-04 / 2026-08-06); không chấm Fail vì khác literal `BaoCaoChuongTrinh_…` của đối tác. Xuất 3 lượt trong ngày ra 3 tên khác nhau (`_1257`, `_1300`, `_1303`) ⇒ không đè tệp |
| (c) Nội dung tệp | **Đạt.** Đủ 5 mảnh phần đầu `:1092`, đúng hình hài cross-tab `:927`/`:948` (hàng = đơn vị; cột = số CT **và** ngân sách), có cả `cap_don_vi` `:943`, số khớp màn, cộng dọc khớp tổng, áp đúng bộ lọc `:1280` |

0 GAP (đủ 5 dòng mục 6) · M = 3 + 1 nhánh phụ · chạy đủ luồng bằng thao tác giao diện thật · có đường đo
thứ hai. Đủ điều kiện ra verdict.

⚠️ **Giới hạn hiệu lực:** kết luận này chỉ có hiệu lực cho môi trường `18.143.165.120.nip.io` và bản dựng
**V1.0.8** (`assets/index-CNwX9JjX.js`). Đối tác báo lỗi trên `htpldn-uat.ospgroup.vn` — chưa đối chiếu bản
dựng của env đó. Phần đã hết lỗi (vế b, c và nhánh CB Nghiệp vụ của vế a) là **đạt tạm**, cho tới khi bản
dựng này lên env của đối tác.

⚠️ **Không kết luận "fix đã có tác dụng":** không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng trước khi
sửa, nên chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**.

---

## Mục sửa đổi

- **2026-08-06 13:10** — **KHÔNG sửa mục 4 và mục 5** (tiêu chí giữ nguyên như lúc viết trước khi mở màn).
  Chỉ **điền** cột "Mình test lần này" + "GAP?" của mục 6, điền **Bản dựng** ở đầu file (ô đó vốn để trống chờ
  giai đoạn B) và **bổ sung** mục 7 + 8 (phần kết quả).
- Ghi chú về dạng ③: mục 5 viết *"Kỳ = Quý / Tháng / Khoảng tùy chọn, chọn khoảng con của 2026 sao cho số CT
  khác dạng ①"* — khi đo mới thấy kỳ **Tháng/Quý** có ô *Thời gian* **chỉ đọc, tự tính theo kỳ hiện tại**
  (tháng 08/2026 → 0 bản ghi, không xuất được tệp để so). Vì vậy chọn nhánh **Khoảng tùy chọn** đã nêu sẵn
  trong chính ô đó. **Không** phải nới tiêu chí — vẫn đúng phương án đã viết trước khi mở màn.
