# Tiêu chí verify — CTTLV_05 (tab `bug`, dòng 277)

Mã case: CTTLV_05          Thời điểm viết: 2026-08-06 13:26 (viết XONG trước khi mở màn Báo cáo thống kê
trên env verify)
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** (chuỗi phiên bản in
ở chân logo sidebar; **dấu vân tay bó mã giao diện `assets/index-CNwX9JjX.js`**) — đo lúc 2026-08-06
13:30–13:46. Tab được **mở MỚI trong phiên này** bằng ngữ cảnh trình duyệt riêng (`isolatedContext`) nên
chắc chắn chạy bản dựng hiện hành và **không dùng chung phiên đăng nhập với phiên QA khác**. Không có
endpoint công bố phiên bản (`/api/v1/health` đã tra ở đợt trước — 404) và header phản hồi không mang số
hiệu bản dựng.

**Màn thật của case:** *Báo cáo thống kê* → *Loại báo cáo* = **BC Chương trình theo lĩnh vực**
(URL mang `?loai=ct-theo-linh-vuc`), đặc tả **FR-IX-22 (UC145)**.
⚠️ Tiền tố `CT` trong mã case = **Chương trình**, KHÔNG phải "chi trả" — nhãn batch cũ ghi sai loại BC.

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A của flow):
`thu-QLTLPLCVV_15-2026-08-06/tieuchi/SLCTHT_06.md` (case cùng lô, cùng màn Báo cáo thống kê nhưng **khác
loại BC**) · brief chung của lô §9c (ghi nhận env verify có sẵn 14 chương trình, bản dựng V1.0.8, và kết
quả Reopen của `SLCTHT_06`) · `bug-report.md` Phần 2 (entry BUG-SLCTHT-006).
⚠️ Các hồ sơ trên chứa **số đo cũ của MỘT LOẠI BC KHÁC** (vd "7 chương trình", "xuất Excel 200"). Theo
flow §BƯỚC 0 — *cùng chữ không có nghĩa cùng nguyên nhân* — mỗi loại báo cáo là một đường xử lý riêng.
Mục 4 và mục 5 dưới đây suy từ **đặc tả** `srs-fr-11-bao-cao.md` (đã mở file đọc từng dòng được quote),
**không** lấy số đo cũ làm ngưỡng: tiêu chí (e) đòi tệp khớp **số hiện trên màn tại thời điểm đo**, không
chốt cứng con số nào.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** (tách theo ô `Mô tả` + `Các bước thực hiện` + `Kết quả mong đợi` + `Kết quả thực tế` +
`TKM phản hồi lần 1`):

- **(a) Không xuất được tệp.** Bấm **[Xuất Excel]** trên màn *Báo cáo thống kê* (loại BC = *BC Chương trình
  theo lĩnh vực*) thì hệ thống **không giao tệp nào**, chỉ hiện thông báo lỗi.
  - Vòng 1 (16/07/2026, bản dựng **V1.0**): thông báo đỏ ✗ **"Không thể tạo file xuất. Vui lòng thử lại."**
  - Vòng 2 (31/07/2026, bản dựng **V1.0.3**): thông báo đỏ ✗ **"Forbidden"** — **đổi hẳn câu chữ**, sang một
    chuỗi tiếng Anh thô.
- **(b) Tên tệp.** Kỳ vọng của đối tác: tệp tải về tên `BaoCaoChuongTrinh_{YYYYMMDD_HHmm}.xlsx`.
- **(c) Nội dung tệp + tự động tải về.** Kỳ vọng của đối tác: *"Hệ thống xuất **toàn bộ** và **tự động tải
  tệp về máy** người dùng"* — tệp chứa trọn dữ liệu báo cáo đang xem, không phải một phần.

**Lệch giữa 2 vòng bằng chứng** (bắt buộc ghi theo §Cổng bằng chứng của flow):

| | vòng 1 `CTTLV_05.jpg` | vòng 2 `CTTLV_05_v2.jpg` |
|---|---|---|
| Loại BC + kỳ + khoảng thời gian | BC Chương trình theo lĩnh vực · Năm · 01/01/2026 → 31/12/2026 | **giống hệt** |
| Vai trò | Quản trị viên / **QTHT**, `BTP · TW` | **giống hệt** |
| **Đơn vị** | **Toàn quốc** | **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** ← **KHÁC** (URL thêm `&donViId=00000000-0000-4000-8000-000000000001`) |
| Lĩnh vực | để trống (placeholder *"Chọn Lĩnh vực"*) | để trống |
| Bản dựng | **V1.0** | **V1.0.3** ← KHÁC |
| Số liệu trên màn | Tổng chương trình **5** + thẻ **Tổng DN tham gia 0** | Tổng chương trình **3**, **không còn** thẻ DN |
| Thông báo sau [Xuất Excel] | ✗ "Không thể tạo file xuất. Vui lòng thử lại." | ✗ "Forbidden" |

⇒ Hai vòng **không cùng điều kiện**: khác **đơn vị lọc**, khác **bản dựng**, khác **số liệu**, khác **câu
thông báo**. Không được coi là cùng một triệu chứng ⇒ vế (a) phải đo cho **cả hai** cấu hình đơn vị và **cả
hai** câu thông báo. (Đây là lý do mục 5 chốt dạng ① = Toàn quốc và dạng ② = BTP-TW, xem mục 5.)

**Bằng chứng đã mở đọc full-res:**

- `partner-evidence/CTTLV_05.jpg` (vòng 1). Thấy: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-linh-vuc&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`;
  chân logo sidebar `HTPLDN · V1.0`; góc phải `BTP · TW` + chuông 99+ + avatar `QV` + **Quản trị viên QTHT**;
  breadcrumb *Trang chủ / Báo cáo thống kê*; **thông báo đỏ ✗ "Không thể tạo file xuất. Vui lòng thử lại."**
  nổi giữa đỉnh trang; form lọc: *Loại báo cáo* = **BC Chương trình theo lĩnh vực**, *Kỳ báo cáo* = **Năm**,
  *Thời gian* **Từ 01/01/2026 — Đến 31/12/2026**, *Đơn vị* = **Toàn quốc**, *Lĩnh vực* = **để trống**
  (placeholder xám *"Chọn Lĩnh vực"*); hàng nút **[Xem báo cáo] [Xuất Excel] [Xuất PDF]**; khối kết quả
  **"BC Chương trình theo lĩnh vực"** — *Kỳ: Năm · 01/01/2026 → 31/12/2026 · Đơn vị: Toàn quốc*,
  **Thời điểm tạo: 16/07/2026 16:50**, hai thẻ **Tổng chương trình = 5** và **Tổng DN tham gia = 0**;
  đồng hồ máy **04:53 PM 2026-07-16**. Ảnh bị cắt dưới hàng thẻ ⇒ **không thấy bảng dữ liệu theo lĩnh vực**.
- `partner-evidence/CTTLV_05_v2.jpg` (vòng 2). Thấy: **cùng URL nhưng có thêm**
  `&donViId=00000000-0000-4000-8000-000000000001`; chân logo `HTPLDN · V1.0.3`; **thông báo đỏ ✗
  "Forbidden"** ở đúng vị trí đó; vẫn **Quản trị viên QTHT / BTP · TW**; *Đơn vị* = **Cục Bổ trợ tư pháp -
  Bộ Tư pháp (BTP-TW)**, *Lĩnh vực* để trống; khối kết quả **Thời điểm tạo: 31/07/2026 15:32**, **chỉ còn
  MỘT thẻ: Tổng chương trình = 3** (thẻ *Tổng DN tham gia* đã biến mất); trên thanh trình duyệt có **biểu
  tượng tải xuống** (dấu vết các lượt tải trước, **không** chứng minh lượt này có tệp — ảnh không mở khay
  tải); đồng hồ máy **03:34 PM 2026-07-31**. Ảnh cũng bị cắt dưới hàng thẻ ⇒ **không thấy bảng dữ liệu**.

## 2. Đặc tả nói gì

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`
(đã mở file đọc trực tiếp từng dòng dưới đây, không lấy số dòng từ trí nhớ).

**Vế (a) — quyền + luồng xuất (template chung TPL-REPORT-FULL):**

- `:62` — Preconditions chung: *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"*.
- `:79` — Processing chung bước 1: `| 1 | Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01 |`
- `:81` — bước 3: *"Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc, BN chỉ thấy BN mình, ĐP chỉ thấy ĐP
  mình (BN và ĐP ngang cấp song song, không thấy nhau)"* (BR-AUTH-03, BR-AUTH-04, BR-AUTH-08).
- `:82` — bước 4: *"Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh
  toán)"* (BR-RPT-01).
- `:1052` — SCR-IX-01 thành phần 8: `| 8 | action-bar | Nút Xuất Excel | button | "Xuất Excel (.xlsx)" → xuất
  theo format TT17/2025 | click → auto-download | Sau khi đã "Xem báo cáo" |`
- `:1058` — thành phần 14: `| 14 | content | Toast xuất file | toast | "Đang tạo file..." → "Xuất thành công"
  + auto-download | — | Khi nhấn xuất |`
- `:116` — E6: `| E6 | Lỗi xuất file | ERR-RPT-04 | "Không thể tạo file xuất. Vui lòng thử lại" | ERROR |`
  ← **đúng nguyên văn câu đối tác chụp ở vòng 1** ⇒ vòng 1 là **nhánh lỗi**, không phải nhánh thành công.
- `:117` — E7: `| E7 | Không có quyền | ERR-RPT-05 | "Bạn không có quyền xem báo cáo này" | ERROR |`
  ← đối chiếu với chuỗi **"Forbidden"** ở vòng 2.
- `:1268` — BR-AUTH-08: *"chính sách phân quyền áp dụng cho MỌI bảng có cột `don_vi_id`. TW thấy toàn quốc,
  BN thấy BN, ĐP thấy ĐP"*, cột **Ngoại lệ = "QTHT bypass"**, Áp dụng = *Toàn bộ FR-IX*.

**Vế (b) — tên tệp:**

- `:85` — Processing chung bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp
  `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo
  `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]`"*.
- `:86` — định nghĩa token (nêu trong bước 8 nhưng dùng chung cho cả 2 định dạng): *"`{TenBaoCao}` là tên
  loại báo cáo viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số (dấu `/`,
  khoảng trắng, dấu câu)"* `[BA chốt 2026-08-04]`.
- `:123` — AC chung: *"**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times New
  Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (Phụ lục E §H8)"*.
- `:1092` — Quy tắc tương tác SCR-IX-01: *"Tên tệp cả hai định dạng theo **Phụ lục E §H8** —
  `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"*.

> 🔴 **Kỳ vọng (b) của đối tác lệch đặc tả — nhưng BA ĐÃ chốt đúng điểm này.** Đối tác đòi literal
> `BaoCaoChuongTrinh_…`; quy tắc `:85`+`:86` suy tên tệp từ **tên loại báo cáo** (ở đây là *"BC Chương trình
> theo lĩnh vực"*), không phải một chuỗi cố định. Cả `:85`, `:86`, `:1092` đều mang nhãn nguồn + ngày
> **`[BA chốt 2026-08-04]`**, tức **sau** cả 2 vòng test của đối tác (16/07 và 31/07). Theo §Rẽ nhánh của
> flow (*"Ngoại lệ duy nhất — BA ĐÃ chốt trước đúng điểm tranh chấp này, dẫn được nguồn kèm ngày → áp quyết
> định có sẵn"*), vế (b) **áp khuôn của đặc tả**, KHÔNG đẩy sang cần-BA và KHÔNG chấm Fail vì tên khác
> literal của đối tác. Phần `_{YYYYMMDD_HHmm}` thì đối tác và đặc tả **trùng khớp** ⇒ vẫn là tiêu chí bắt buộc.

**Vế (c) — nội dung tệp:**

- `:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file."*
- `:1280` — BR-DATA-06: *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không
  vượt quá 10,000 rows/file"*, Áp dụng = *Toàn bộ FR-IX*.
- `:87` — bước 9: *"Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo"* (BR-DATA-06).
- `:88` — bước 10: *"Ghi nhật ký thao tác (xem/xuất báo cáo)"* (BR-DATA-05, xem thêm `:1274`).
- `:113` — E3: `| E3 | Không có dữ liệu | INF-RPT-01 | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | INFO |`

**Đặc thù màn của case — FR-IX-22 (UC145) `:952`–`:991`:**

- `:961` Mô tả: *"Báo cáo chương trình theo lĩnh vực: hàng = lĩnh vực, cột = số CT.
  `[CTTLV_04 chốt 2026-07-24: bỏ cột "Số DN tham gia" — CSV UC145 chỉ yêu cầu "thống kê số lượng chương
  trình theo lĩnh vực"; không có mô hình dữ liệu CT↔DN và không có định nghĩa nghiệp vụ "DN tham gia chương
  trình"…]`"*
- `:963` Tác nhân: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*
- `:965` Template: *"Kế thừa TPL-REPORT-FULL"*
- `:971` Input đặc thù: `| 1 | linh_vuc_id | identifier | N | FK → DANH_MUC | — | Chọn |`
  ⇒ bộ lọc **Lĩnh vực**, **không bắt buộc**.
- `:973` Công thức: *"Đếm số CT theo lĩnh vực, trong kỳ"* · `:975` Dimensions: *"Lĩnh vực, Số CT"*
- `:981`–`:983` Output đặc thù, cột *Điều kiện* của cả 3 dòng đều là **"Luôn"**:
  `linh_vuc_id` (ID lĩnh vực) · `ten_linh_vuc` (Tên lĩnh vực) · `so_ct` (Số CT)
- `:986` *"Cột "Lĩnh vực" gom theo `CHUONG_TRINH_HTPL.linh_vuc_id` — trường bắt buộc, chọn một lĩnh vực
  chính… Mỗi CT thuộc đúng một lĩnh vực nên báo cáo gom trọn vẹn theo lĩnh vực."*
- `:987` *"Vì lĩnh vực là bắt buộc từ khi tạo CT, báo cáo không phát sinh nhóm "Không xác định". CT dữ liệu
  cũ chưa gán lĩnh vực (nếu có) gom tạm vào nhóm **"Chưa phân loại"** kèm yêu cầu cán bộ cập nhật."*
- `:990` AC bổ sung: *"**Given** CB tạo BC **When** hiển thị **Then** bảng: hàng = lĩnh vực, cột = số CT"*
- `:991` AC bổ sung: *"**Given** mọi CT đã có lĩnh vực bắt buộc **When** hiển thị BC **Then** không xuất hiện
  nhóm "Không xác định""*
- `:1085` Mapping dropdown SCR-IX-01: `| | UC145 | BC CT theo lĩnh vực | Lĩnh vực | Bar |` ⇒ bộ lọc đặc thù
  của loại BC này **chỉ có Lĩnh vực**, biểu đồ dạng Bar.
- Output chung `:94`–`:101` (áp qua `:965`): `ten_bao_cao` · `ky_bao_cao` · `tu_ngay/den_ngay` ·
  `don_vi_ten` · `ngay_tao_bc` · `nguoi_tao` · `tong_ban_ghi` · `data[]` — cột *Điều kiện* đều **"Luôn"**.

**IM LẶNG về** (⇒ CẤM chấm Fail vì mấy thứ này):
tên sheet trong workbook · thứ tự cột trong tệp · có đóng khung / tô màu / in đậm không · có dòng tổng cuối
bảng không · định dạng số và định dạng ngày cụ thể trong ô · biểu đồ có được nhúng vào tệp `.xlsx` không ·
tệp xuất có mấy sheet · **vai trò QTHT có được XEM/XUẤT báo cáo hay không** (`:62` và `:963` chỉ **liệt kê**
CB NV / CB PD, **không** viết câu cấm QTHT; `:1268` lại cho QTHT **bypass** phạm vi đơn vị — hai chỗ này
không đủ để kết luận QTHT bị cấm) · thông báo lỗi hiển thị ở dạng lớp nổi hay inline · mã lỗi có lộ ra giao
diện hay không · thứ tự sắp xếp các lĩnh vực trong bảng · lĩnh vực có 0 chương trình thì có hiện hàng với
số 0 hay bị ẩn đi.

## 3. Precondition

- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → menu **Báo cáo thống kê** → *Loại báo cáo* =
  **BC Chương trình theo lĩnh vực** (URL mang `?loai=ct-theo-linh-vuc`).
- **Tài khoản — đo CẢ 2 nhánh, cùng bộ tiêu chí:**

  | Nhánh | Tài khoản | Vai trò | Dùng để |
  |---|---|---|---|
  | **A — ra verdict** | `cbnv_tw_04` / `Test@1234` | CB_NV_TW, cấp TW ⇒ phạm vi *Toàn quốc*, khớp `BTP · TW` của đối tác; đúng tác nhân `:62` + `:963` | quyết Pass / Reopen |
  | **B — đối chứng** | `admin` / `Secret@123` | QTHT — **trùng khít vai trò trên cả 2 ảnh đối tác** | giải thích triệu chứng **"Forbidden"** vòng 2; đóng dòng GAP *Vai trò / tài khoản* |

  Tài khoản quản trị **không** được dùng để ra verdict (quyền rộng che lỗi phân quyền) — nhánh B chỉ đối
  chứng. Rule 7 nếu khoá: fallback **cùng vai trò + cùng cấp** `cbnv_tw_04` → `cbnv_tw_05` → `cbnv_tw_03`…,
  tuyệt đối không đổi vai trò/cấp; ghi rõ tài khoản THỰC đã dùng.
- **Xác nhận danh tính NGAY TRƯỚC và NGAY SAU mỗi phép đo quyết định** (có phiên QA khác chạy song song trên
  cùng trình duyệt + cùng env): đọc `tenDangNhap` / `vaiTro` / `donViId` / `capDonVi` từ phiên đăng nhập và
  ghi vào mục 7. Trước ≠ sau ⇒ **phép đo VÔ HIỆU**, đăng nhập lại và đo lại. Tab đo phải là tab **tự mở**.
- **Dữ liệu tiền đề:** ≥ 1 chương trình HTPL trong khoảng **01/01/2026 – 31/12/2026** ở trạng thái được
  `:82` cho phép đếm (đã duyệt / hoàn thành / đã thanh toán), thuộc phạm vi TW. Muốn đo được **cả 3 dạng ở
  mục 5** thì cần thêm: **≥ 1 CT thuộc *Cục Bổ trợ tư pháp - Bộ Tư pháp*** (dạng ②) và **CT trải trên ≥ 2
  lĩnh vực khác nhau** (dạng ③ — nếu mọi CT cùng một lĩnh vực thì lọc lĩnh vực không phân biệt được
  "bộ lọc có tác dụng" với "bộ lọc bị bỏ qua"). Kiểm trước bằng màn **CT HTPLDN** hoặc
  `GET /api/v1/chuong-trinh-htpls`.
  Thiếu → **được seed** qua BE API (`create → submit → approve bằng tài khoản KHÁC → publish/activate/
  complete bằng người tạo`, mỗi bước cần `version`) và **bắt buộc khai** bản ghi nào · đổi gì · env nào vào
  mục 7 + bug entry. Tiền đề **tạo được mà không tạo → CẤM mọi verdict, kể cả ô trống.**
- **Bẫy cache máy chủ:** báo cáo thống kê có cache phía máy chủ. Sau khi seed mà số không đổi → đọc trường
  **"Thời điểm tạo"** trên màn; ép khoá cache mới bằng cách **đổi `denNgay` 1 ngày**. `cache:'reload'` chỉ
  bust cache trình duyệt ⇒ không dùng làm căn cứ.

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 6 điều dưới đây (đo được):**

- **(a) Nhánh A giao được tệp, không có thông báo lỗi.** Với `cbnv_tw_04`, ở dạng dữ liệu ① mục 5: bấm
  **[Xem báo cáo]** → chờ khối kết quả hiện → bấm **[Xuất Excel]**. Đo bằng bộ bắt thông báo cài **trước**
  khi bấm: **0** thông báo mang nội dung lỗi/từ chối (đếm theo **mốc giờ khác nhau**, không theo số phần
  tử), và hệ thống **giao ra một tệp** (tệp về máy, hoặc phản hồi máy chủ của chính thao tác đó có thân nhị
  phân tải về được). Số request của thao tác đếm bằng `list_network_requests` (nút có thể là GET nên
  `window.__qa.net` không ghi).
- **(b) Tệp là .xlsx thật.** Mở được bằng thư viện đọc xlsx (`openpyxl`) hoặc giải nén zip đọc được
  `xl/workbook.xml` — **không** phải HTML/JSON đổi đuôi. (Mã 200 + có bytes **không** đủ để đạt (b).)
- **(c) Tên tệp đúng khuôn `:85`+`:86`+`:1092`:** dạng `<Tên>_<8 chữ số>_<4 chữ số>.xlsx`, trong đó `<Tên>`
  là **tên loại báo cáo viết liền, không dấu tiếng Việt, không khoảng trắng, không dấu câu**, và
  `<8 chữ số>_<4 chữ số>` là **ngày `YYYYMMDD` + gạch dưới + giờ phút `HHmm`** khớp thời điểm xuất (sai lệch
  ≤ 5 phút so với đồng hồ lúc bấm nút). Kiểm bằng biểu thức: `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`.
- **(d) Trong tệp có đủ phần đầu theo `:1092`:** đọc nội dung ô của tệp phải tìm thấy **tiêu đề báo cáo**,
  **kỳ báo cáo**, **khoảng thời gian tu_ngay–den_ngay**, **tên đơn vị** (hoặc "Toàn quốc"), **ngày tạo báo
  cáo**. Đủ 5 mảnh ⇒ đạt; thiếu bất kỳ mảnh nào ⇒ không đạt.
- **(e) Tệp có đúng cấu trúc bảng của FR-IX-22 và số liệu KHỚP màn** — phép đo quyết định, không được bỏ:
  - **Cấu trúc `:990` + `:981`–`:983`:** trong tệp có một bảng mà **mỗi hàng là một lĩnh vực** và có **cột
    số chương trình** của lĩnh vực đó (tối thiểu đủ 2 mảnh `ten_linh_vuc` và `so_ct`; `linh_vuc_id` nếu
    không lộ ra ô thì ghi nhận chứ không chặn Pass, vì nó là mã kỹ thuật).
  - **Khớp thẻ tổng:** số *Tổng chương trình* trong tệp = số trên màn ở **cùng một lần "Xem báo cáo"**.
  - **Khớp từng hàng:** tập tên lĩnh vực trong tệp = tập tên lĩnh vực trên bảng của màn, và **mỗi lĩnh vực
    có cùng số CT** ở hai nơi; **số hàng lĩnh vực của tệp = số hàng trên màn** (không thiếu, không thừa).
  - **Cộng dọc:** tổng cột số CT của các hàng lĩnh vực = số *Tổng chương trình*. Lệch ⇒ theo §"phép đo đang
    nói dối" là số sai, phải đo lại, **chưa được kết luận**.
- **(f) Áp đúng bộ lọc hiện tại (`:1280`)** — chứng minh bằng **so sánh giữa các dạng ở mục 5**: nội dung
  tệp của dạng ② (đơn vị BTP-TW) và dạng ③ (có chọn Lĩnh vực) **khác** nội dung tệp dạng ①, và mỗi tệp khớp
  đúng màn của chính bộ lọc đó theo tiêu chí (e). Riêng dạng ③: tệp **chỉ chứa hàng của lĩnh vực đã chọn**,
  không còn hàng của lĩnh vực khác.

**Nhánh B (đối chứng, `admin`/QTHT) — không quyết Pass/Fail của case, nhưng bắt buộc đo và ghi:**
lặp lại đúng dạng ① rồi ghi nhận: xuất được tệp, **hay** bị từ chối. Nếu bị từ chối thì đọc **nguyên văn**
chữ hiện ra và đối chiếu `:117`.

**❌ FAIL nếu (bất kỳ điều nào):**

- Nhánh A bấm [Xuất Excel] mà **không có tệp nào được giao**, hoặc hiện thông báo mang nghĩa từ chối/thất
  bại (gồm nhưng không giới hạn ở đúng 2 câu đối tác chụp).
- Tệp giao ra **không mở được** bằng thư viện đọc xlsx (HTML/JSON/tệp hỏng đổi đuôi).
- Tên tệp **không** có phần ngày-giờ `_YYYYMMDD_HHmm` trước `.xlsx`, hoặc còn dấu tiếng Việt / khoảng trắng
  / dấu câu trong phần tên báo cáo.
- Tệp **thiếu** bất kỳ mảnh nào trong 5 mảnh phần đầu ở (d).
- Tệp **không có bảng hàng-là-lĩnh-vực kèm số CT** (`:990`), hoặc tập lĩnh vực / số CT từng lĩnh vực **lệch**
  so với màn, hoặc cộng dọc không bằng tổng.
- Đổi bộ lọc mà **nội dung tệp không đổi** (dạng ②/③ ra tệp giống hệt dạng ①) ⇒ vi phạm `:1280`.
- **Nhánh A xuất được nhưng nhánh B (QTHT) bị chặn bằng chuỗi tiếng Anh thô "Forbidden"** ⇒ vẫn là
  **Reopen**: đây là vế **(a) đối tác có nêu** (ô *TKM phản hồi lần 1*), và câu chữ đó trái yêu cầu của
  `:117` — hệ thống khi từ chối vì thiếu quyền phải nói bằng thông báo tiếng Việt cho biết người dùng không
  có quyền xem báo cáo.
- Nhánh B bị chặn bằng **đúng khuôn tiếng Việt của `:117`** ⇒ **không** Fail vì câu chữ, nhưng khi đó còn
  tranh chấp *"QTHT có được xuất BC không"* mà đặc tả im lặng ⇒ **cần BA** (kèm mâu thuẫn hành vi: app cho
  QTHT **XEM** được báo cáo — ảnh đối tác có đủ số liệu — nhưng cấm **XUẤT**; nếu QTHT thật sự không có
  quyền thì `:79` bước 1 phải chặn ngay từ bước Xem).

**KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):
tên sheet · thứ tự cột · đóng khung/tô màu/in đậm · có hay không dòng tổng cuối bảng · định dạng số và ngày
trong ô · biểu đồ có nhúng vào tệp hay không · số lượng sheet · thứ tự sắp xếp lĩnh vực · lĩnh vực 0 chương
trình bị ẩn hay hiện · thông báo hiện dạng lớp nổi hay inline · mã lỗi có lộ ra giao diện hay không ·
**tên tệp khác literal `BaoCaoChuongTrinh_…` mà đối tác ghi**, miễn vẫn đúng khuôn `:85`+`:86` (BA chốt
2026-08-04 — xem khối trích ở mục 2) · khổ giấy A4 và font Times New Roman cỡ 13 bên trong tệp `.xlsx`
**không** dùng để chặn Pass ở lượt này *(đặc tả `:85` có nêu, nhưng đó là thuộc tính trình bày khi in; đo
được thì ghi nhận, không đo được thì ghi rõ "chưa đo" chứ không suy ra Fail)*.

**🔴 Hai điểm ghi nhận RIÊNG — không kéo verdict của case** (flow §Ca biên: phát hiện nằm trong đúng màn
đang tranh chấp nhưng **đối tác không nêu** ⇒ xử riêng):

1. **Thẻ "Tổng DN tham gia"** — `:961` chốt ngày **2026-07-24** *bỏ cột "Số DN tham gia"*. Ảnh vòng 1 của
   đối tác (16/07, **trước** quyết định này) **có** thẻ đó; ảnh vòng 2 (31/07, **sau**) **không còn**. Ở
   lượt đo này: bản dựng còn thẻ/cột đó ⇒ **trái `:961`** (đặc tả nói rõ) → log lỗi mới; không còn ⇒ chỉ
   ghi nhận là đã đúng.
2. **Nhóm "Không xác định" / "Chưa phân loại"** — `:987` + AC `:991`: lĩnh vực là trường bắt buộc nên báo
   cáo **không được** phát sinh nhóm *"Không xác định"*; CT dữ liệu cũ chưa gán lĩnh vực thì gom vào nhóm
   *"Chưa phân loại"*. Ở lượt đo này: nếu bảng (trên màn hoặc trong tệp) xuất hiện nhãn *"Không xác định"*
   ⇒ **trái `:991`** → log lỗi mới; nhãn *"Chưa phân loại"* là **hợp lệ**, không phải lỗi.

## 5. Dạng dữ liệu phải phủ — M = 3

| # | Dạng | Cấu hình bộ lọc trên màn | Dùng để kiểm |
|---|---|---|---|
| ① | **Khớp khít cấu hình vòng 1 của đối tác** | Kỳ = **Năm**, Từ **01/01/2026** → Đến **31/12/2026**, Đơn vị = **Toàn quốc**, Lĩnh vực = **để trống** | tái hiện đúng điều kiện ảnh vòng 1; đo (a)(b)(c)(d)(e) |
| ② | **Khớp khít cấu hình vòng 2 của đối tác — đơn vị cụ thể** | như ① nhưng Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** (đúng `donViId=00000000-0000-4000-8000-000000000001` trên URL ảnh vòng 2) | tái hiện đúng điều kiện ảnh vòng 2; kiểm phạm vi đơn vị `:81`/`:1268` + bộ lọc đơn vị có vào tệp không (`:1280`) |
| ③ | **Có chọn Lĩnh vực** (bộ lọc đặc thù của chính FR-IX-22) | như ① nhưng *Lĩnh vực* = **một giá trị cụ thể đang có chương trình** (chọn từ dropdown tại thời điểm đo, ghi rõ đã chọn lĩnh vực nào) | kiểm bộ lọc đặc thù `:971` có được áp vào tệp không (`:1280`); và kiểm bảng vẫn đúng khuôn hàng = lĩnh vực (`:990`) |

**Nguồn xác định M** (tra theo thứ tự flow §"Xác định M", dừng ở bước ②):

- Bước ① *(đặc tả nói về nguồn dữ liệu / cách bản ghi được tạo)*: `:973` — báo cáo *"Đếm số CT theo lĩnh
  vực, trong kỳ"*; `:986` — dữ liệu gom theo `CHUONG_TRINH_HTPL.linh_vuc_id`, **mỗi CT thuộc đúng một lĩnh
  vực** ⇒ bản ghi vào báo cáo phân thành **nhiều nhóm lĩnh vực**; `:82` giới hạn ở bản ghi **đã duyệt**.
- Bước ② *(bộ lọc + giá trị enum ngay trên màn đó)*: `:971` cho `linh_vuc_id` (FK → DANH_MUC, **không bắt
  buộc** ⇒ có 2 trạng thái: để trống / có chọn) · `:1049` dropdown đơn vị (*"TW: 'Toàn quốc' + chọn BN/ĐP
  bất kỳ"*) · `:1048` bộ lọc kỳ BC · `:1085` xác nhận loại BC này **chỉ có 1 bộ lọc đặc thù = Lĩnh vực**.
- Ràng buộc quyết định: `:1280` đòi **"File xuất theo bộ lọc hiện tại"**. Một cấu hình bộ lọc duy nhất chỉ
  chứng minh *hệ thống xuất được một tệp*, **không** chứng minh được tệp có bám bộ lọc — muốn kết luận phải
  có **≥ 2 cấu hình khác nhau** cho ra **≥ 2 nội dung khác nhau**. ⇒ **M = 1 không hợp lệ cho case này.**
  Chọn M = 3 để phủ **2 chiều lọc độc lập** (đơn vị `:81`/`:1049` và lĩnh vực `:971`) trên cùng một nền ①,
  đồng thời **① và ② lần lượt trùng khít 2 vòng bằng chứng** của đối tác (2 vòng khác nhau ở đúng chiều đơn vị).

⚠️ Bẫy đã biết cho mục 5: nếu mọi CT trên env đều thuộc **một** lĩnh vực thì dạng ③ trùng dạng ① và **không
phân biệt được** "bộ lọc có tác dụng" với "bộ lọc bị bỏ qua" → phải seed cho đủ **≥ 2 lĩnh vực** trước khi
đo (xem mục 3), hoặc thêm nhánh phụ **③b** chọn một lĩnh vực **không có chương trình nào** để chứng minh bộ
lọc thật sự lọc (kết quả mong đợi khi đó là nhánh `:113`). Tương tự, nếu mọi CT đều thuộc **một** đơn vị thì
dạng ② trùng dạng ① — khi đó phải ghi rõ hạn chế này vào mục 7 và đóng bằng nhánh phụ **②b** (chọn một đơn
vị khác, không có dữ liệu), thay vì coi như đã đóng.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên / QTHT**, đơn vị **BTP · TW** (góc phải màn, avatar `QV`) — **cả 2 vòng giống nhau** | Đo **cả 2 nhánh**. **A** `cbnv_tw_04` — `/auth/me` trả `hoTen="CB Nghiệp vụ - Trung ương #04"`, `vaiTro=["CB_NV_TW"]`, `capDonVi="TW"`, `donViId=00000000-0000-4000-8000-000000000001`, màn hiện `BTP · TW`, phạm vi Toàn quốc (đúng tác nhân `:62`/`:963`). **B** `admin` — `hoTen="Quản trị hệ thống"`, `vaiTro=["QTHT"]`, `capDonVi="TW"`, cùng `donViId` ⇒ **trùng khít vai trò + cấp + đơn vị của đối tác** (chỉ khác họ tên người dùng: env đối tác là *"Quản trị viên"*, env này là *"Quản trị hệ thống"*). Danh tính kiểm **trước và sau** mỗi phép đo quyết định — trước = sau ở cả 2 nhánh | **Không** |
| Entity + trạng thái | **CHUONG_TRINH_HTPL** (`:986`). Vòng 1: *Tổng chương trình = 5* (Toàn quốc); vòng 2: *Tổng chương trình = 3* (riêng BTP-TW). Ảnh **không lộ** bảng theo lĩnh vực (bị cắt dưới hàng thẻ) ⇒ không biết 5/3 CT đó rải trên mấy lĩnh vực | Cùng entity **CHUONG_TRINH_HTPL**. Trong kỳ 2026 báo cáo đếm **7** chương trình, rải trên **5 nhóm**: *Chưa phân loại 3 · Lao động 1 · Đất đai 1 · Thuế 1 · Thương mại 1* (cộng dọc = 7). Số bản ghi khác đối tác nhưng **cùng nhánh nghiệp vụ**: báo cáo CÓ dữ liệu (không rơi `:113`) và có **≥2 lĩnh vực** như mục 5 đòi | **Không** — triệu chứng tái hiện nằm ở tầng quyền (403 trước khi sinh tệp), không phụ thuộc số lượng bản ghi; đã kiểm chéo bằng dạng ③ (1 bản ghi) và ②b (0 bản ghi), kết quả nhất quán |
| Dữ liệu tiền đề | Có dữ liệu thật trên env nghiệm thu: báo cáo tạo được, hiện số liệu (không rơi nhánh `:113`) ⇒ lỗi xuất tệp **không** do rỗng dữ liệu | Env verify có sẵn **14 chương trình** (`GET /api/v1/chuong-trinh-htpls`): DU_THAO 3 · CHO_PHE_DUYET 1 · HUY 1 · TAM_DUNG 1 · DA_DUYET 5 · DA_CONG_BO 1 · DANG_THUC_HIEN 1 · HOAN_THANH 1; lĩnh vực: Lao động 6 · Thuế 2 · Thương mại 2 · Đất đai 1 · **chưa gán 3**. Đã đủ **≥2 lĩnh vực** và đủ đơn vị để đo ⇒ **KHÔNG cần seed, KHÔNG tạo/sửa/xoá bản ghi nào** | **Không** |
| Input / filter / giá trị nhập | Kỳ **Năm** · **01/01/2026 → 31/12/2026** · Lĩnh vực **để trống** ở cả 2 vòng; Đơn vị **Toàn quốc** (vòng 1) và **BTP-TW** (vòng 2); thao tác **[Xem báo cáo] rồi [Xuất Excel]** (đúng điều kiện hiển thị nút ở `:1052`) | **Giống hệt** ở dạng ① (khớp vòng 1) và dạng ② (khớp vòng 2), cho **cả nhánh A và nhánh B**. URL sinh ra trùng khít ảnh đối tác: `/bao-cao?loai=ct-theo-linh-vuc&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` và bản có `&donViId=00000000-0000-4000-8000-000000000001`. Xác nhận thêm `:1052`: nút [Xuất Excel] **bị khoá** cho tới khi bấm [Xem báo cáo], và khoá lại khi báo cáo rỗng (dạng ②b) | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | **M = 2** theo chiều đơn vị (Toàn quốc, BTP-TW), nhưng **chưa bao giờ chọn Lĩnh vực** ⇒ bằng chứng của họ không nói được gì về bộ lọc đặc thù `:971` và về `:1280` | Nhánh A: **M = 3** (① Toàn quốc không lọc lĩnh vực · ② đơn vị BTP-TW · ③ lĩnh vực = Lao động) **+ 2 nhánh phụ**: ②b đơn vị Bộ Công an (0 bản ghi) và ③b lĩnh vực Đất đai. Nhánh B: dạng ① (đủ để tái hiện triệu chứng đối tác nêu). N = 7 chương trình ở dạng ①/②, 1 ở ③ và ③b, 0 ở ②b | **Không** — dạng ② rơi đúng ca suy biến đã cảnh báo ở mục 5 (mọi CT thuộc cùng 1 đơn vị nên số liệu trùng dạng ①); đã đóng bằng **②b** chứng minh bộ lọc đơn vị thật sự lọc dữ liệu |

**3 dữ kiện neo của đối tác:**

- URL/bản ghi: vòng 1 `htpldn-uat.ospgroup.vn/bao-cao?loai=ct-theo-linh-vuc&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  · vòng 2 **cùng URL + `&donViId=00000000-0000-4000-8000-000000000001`**. Không có ID bản ghi đơn lẻ —
  đây là màn báo cáo tổng hợp, "bản ghi" chính là tập CT trong kỳ.
- Trạng thái entity: vòng 1 **5 chương trình** toàn quốc (+ thẻ *Tổng DN tham gia 0*), vòng 2 **3 chương
  trình** riêng BTP-TW (không còn thẻ DN); báo cáo đã tạo thành công, *Thời điểm tạo* 16/07/2026 16:50
  (vòng 1) và 31/07/2026 15:32 (vòng 2).
- Vai trò + env + bản dựng: **Quản trị viên / QTHT**, `BTP · TW`, env **`htpldn-uat.ospgroup.vn`**,
  bản dựng **V1.0** (vòng 1, đồng hồ máy 16/07/2026 16:53) và **V1.0.3** (vòng 2, 31/07/2026 15:34).

**Giới hạn hiệu lực (KHÔNG phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`; lượt này đo
trên env nội bộ `18.143.165.120.nip.io` theo chỉ định. Mọi kết luận Pass ở đây là **Pass tạm**, chỉ có hiệu
lực cho env + bản dựng ghi ở đầu file, cho tới khi bản dựng đó lên env của đối tác.

---

## 7. Kết quả đo (giai đoạn B)

**Bộ bắt thông báo:** script dùng chung `tools/toast-capture.js` (không lọc trùng · đọc `innerText` · đếm
request). **Tự kiểm trước mỗi lượt: `soObserverDangSong = 1`** ⇒ số liệu hợp lệ (4 lượt đều = 1). Đếm
thông báo theo **mốc giờ khác nhau**; mọi lượt đều **1 request ↔ 1 khung thông báo**, không có
double-toast. Số request đếm bằng `list_network_requests` (đối chiếu với `window.__qa.net`).
**Bổ sung một bộ ghi chữ theo thời gian** (đọc `innerText` của khung thông báo mỗi 100 ms) vì thư viện
giao diện **dùng lại một khung** và **đổi chữ tại chỗ** — chỉ nghe `addedNodes` thì bắt được chữ đầu
(*"Đang tạo file..."*) mà mất chữ cuối (*"Tạo file thành công."* / *"Forbidden"*).
**Bẫy cache máy chủ đã loại trừ:** trường *Thời điểm tạo* đổi theo từng lượt Xem báo cáo
(13:32 → 13:35 → 13:37 → 13:38 → 13:39 → 13:40 → 13:41 → 13:44), không phải số cũ.

### Nhánh A — `cbnv_tw_04` (CB_NV_TW, cấp TW) — vai trò đặc tả, dùng để chấm

| Tiêu chí mục 4 | Đo được | Đạt? |
|---|---|:-:|
| (a) Giao được tệp, 0 thông báo lỗi | Dạng ①: 1 request `POST /api/v1/bao-cao/export` → **200**; 1 khung thông báo, chữ **"Đang tạo file..." → "Tạo file thành công."** (bắt trọn ở lượt ③b); **không** có "Không thể tạo file xuất. Vui lòng thử lại." và **không** có "Forbidden"; tệp về máy | ✅ |
| (b) Tệp là .xlsx thật | 6.674 byte, magic `PK\x03\x04`, giải nén có `xl/workbook.xml`, **mở được bằng `openpyxl`** | ✅ |
| (c) Tên tệp đúng khuôn `:85`+`:86` | `BaoCaoCtTheoLinhVuc_20260806_1333.xlsx` — khớp `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`, không dấu/khoảng trắng/dấu câu; `20260806_1333` = đúng ngày giờ bấm nút. Các lượt sau ra `_1335`, `_1337`, `_1341` ⇒ **xuất nhiều lần trong ngày không đè tệp** | ✅ |
| (d) Phần đầu tệp đủ 5 mảnh (`:1092`) | A1 *BC Chương trình theo lĩnh vực* · A2 *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · A3 *Đơn vị: Toàn quốc* · A4 *Ngày tạo: 06/08/2026* | ✅ |
| (e) Cấu trúc `:990` + số liệu khớp màn | Tệp có bảng **hàng = lĩnh vực, cột = số chương trình** (A11/B11 *Lĩnh vực PL \| Số chương trình*). Màn 7 ↔ tệp B8 = 7. Từng hàng khớp tuyệt đối: *Chưa phân loại 3 · Lao động 1 · Đất đai 1 · Thuế 1 · Thương mại 1* — **5 hàng ở tệp = 5 hàng trên màn**. **Cộng dọc** 3+1+1+1+1 = **7** = thẻ tổng | ✅ |
| (f) Áp đúng bộ lọc hiện tại (`:1280`) | Dạng ③ (Lĩnh vực = Lao động): tệp `_1337` ra B8 = **1**, bảng **chỉ còn "Lao động \| 1"** (mất hẳn 4 hàng của dạng ①) — khớp màn. Dạng ③b (Đất đai): tệp `_1341` ra B8 = 1, bảng chỉ còn *"Đất đai \| 1"*. Dạng ② (đơn vị BTP-TW): A3 đổi thành *"Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp"*. Dạng ②b (đơn vị Bộ Công an): màn báo *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* (đúng `:113`) + nút [Xuất Excel] bị khoá | ✅ |

⇒ **Nhánh A: đạt cả 6 tiêu chí.** Không tái hiện được câu *"Không thể tạo file xuất. Vui lòng thử lại."*
của vòng 1.
Ghi chú về `linh_vuc_id` (`:981`): tệp và màn **không in cột mã lĩnh vực**, chỉ in **tên lĩnh vực** +
**số CT**. Theo mục 4 (e) điều này **không chặn Pass** — mã là định danh kỹ thuật, hai mảnh bắt buộc để
đọc được báo cáo (`ten_linh_vuc`, `so_ct`) đều có đủ. Ghi lại để BA biết nếu muốn siết.

### Nhánh B — `admin` (QTHT) — trùng khít vai trò đối tác, đối chứng

| Bước | Đo được |
|---|---|
| [Xem báo cáo] | `GET /api/v1/bao-cao/ct-theo-linh-vuc?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → **200**. Màn hiện **đầy đủ**: Tổng chương trình 7 + bảng 5 hàng lĩnh vực + biểu đồ. **0 thông báo**, không bị chặn ⇒ **QTHT XEM ĐƯỢC báo cáo.** |
| [Xuất Excel] | 1 request `POST /api/v1/bao-cao/export` → **403**. 1 khung thông báo (1 mốc giờ), chữ người dùng thấy: **"Đang tạo file..." → "Forbidden"**. **Không có tệp nào được giao** (thư mục tải về không có tệp mới sau 13:41). Thân phản hồi: `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","timestamp":"2026-08-06T06:45:02.556Z","requestId":"d2432a2b-8188-4174-90e7-260149c6dfba"}}` |

⇒ **Tái hiện ĐÚNG triệu chứng vòng 2 của đối tác**, trên env verify + bản dựng V1.0.8.
Rơi đúng nhánh `❌ FAIL nếu` áp chót của mục 4: chữ hiển thị là chuỗi tiếng Anh thô **"Forbidden"**, trong
khi `:117` đòi hệ thống khi từ chối vì thiếu quyền phải cho người dùng biết **bằng tiếng Việt rằng họ
không có quyền xem báo cáo**. Kèm **mâu thuẫn hành vi**: `:79` bước 1 đặt việc kiểm quyền truy cập báo
cáo ở đầu luồng, nhưng thực tế bước Xem cho qua (200) rồi mới chặn ở bước Xuất (403).

### Đường đo thứ hai

Giao diện ↔ máy chủ **không mâu thuẫn**: mọi kết luận đều có đủ 2 nguồn — chữ đọc bằng `innerText` trên
DOM **và** mã/thân phản hồi lấy từ `list_network_requests` + `get_network_request` (A: 4 lượt
`POST /bao-cao/export` đều **200** kèm tệp thật đã mở đọc bằng `openpyxl` · B: **403** kèm thân JSON
`Forbidden`, không tệp). Thân yêu cầu của 2 nhánh **giống hệt nhau**
(`{"loaiBaoCao":"BC_CT_THEO_LINH_VUC",...,"formatXuat":"XLSX"}`), chỉ khác phiên đăng nhập.

### Hạn chế đã ghi nhận

- **Không chụp được ảnh lớp thông báo** (cả 2 nhánh; đã thử **3 lượt**: chụp ngay sau khi bấm · hẹn giờ
  bấm sau 2500 ms rồi mới chụp ở nhánh A · hẹn giờ 2500 ms ở nhánh B). Ảnh "ngay sau khi bấm" và ảnh
  "hẹn giờ" ra **byte giống hệt nhau** (đối chiếu md5) ⇒ công cụ chụp không bắt được lớp nổi do thư viện
  giao diện dựng qua portal — **tiền lệ đã có** ở BUG-QLTLPLCVV-015 và BUG-SLCTHT-006 trong chính đợt
  này. Bằng chứng thay thế = chữ đọc bằng `innerText` + số đo chứng minh khung hiển thị **thật** với
  người dùng (`position: fixed`, khung rộng **1432 px**, cao 40–45 px) + nguyên văn phản hồi máy chủ.
  Lưu ở [`image/CTTLV_05-thong-bao-va-phan-hoi-may-chu.txt`](../image/CTTLV_05-thong-bao-va-phan-hoi-may-chu.txt).
  *(Ảnh trùng byte đã xoá bớt 1 bản để không có 2 tệp cùng nội dung mà chú thích khác nhau.)*
- Thao tác quyết định của dạng ① ở **cả 2 nhánh** dùng **công cụ bấm chuột thật** của trình duyệt; các
  lượt biến thể (②/②b/③/③b và 2 lượt hẹn giờ) bấm bằng lệnh `click()` **trên đúng phần tử nút thật**
  trong trang — vẫn là sự kiện chuột do trình duyệt phát, không gọi thẳng API. Khai ra để người đọc biết.
- Dạng ② suy biến (số liệu trùng dạng ①) vì mọi chương trình trên env đều thuộc cùng một đơn vị — đã
  đóng bằng ②b, xem mục 6.

### Dữ liệu đã seed / thay đổi trên env

**KHÔNG seed, KHÔNG tạo/sửa/xoá bất kỳ bản ghi nào.** Env đã sẵn 14 chương trình đủ ≥2 lĩnh vực mà mục 5
đòi. Toàn bộ thao tác là đọc (`GET` báo cáo) + xuất tệp (`POST /bao-cao/export`, chỉ sinh tệp, không đổi
dữ liệu nghiệp vụ — đúng Postconditions `:105`). Có đăng xuất `cbnv_tw_04` rồi đăng nhập `admin` để đo
nhánh B. Tab đo dùng **ngữ cảnh trình duyệt riêng** nên không đụng phiên đăng nhập của phiên QA khác.

### Hai điểm ghi nhận riêng (mục 4) — kết quả

1. **Thẻ "Tổng DN tham gia" (`:961`, BA chốt 2026-07-24 bỏ cột "Số DN tham gia").** Bản dựng V1.0.8:
   màn **chỉ còn 1 thẻ "Tổng chương trình"**, tệp xuất cũng **không** có dòng/cột nào về doanh nghiệp
   ⇒ **đã đúng `:961`**, không phải lỗi. (Ảnh vòng 1 của đối tác còn thẻ đó vì chụp 16/07, trước quyết
   định ngày 24/07.)
2. **Nhóm "Không xác định" / "Chưa phân loại" (`:987` + AC `:991`).** Bản dựng V1.0.8: nhãn hiện ra là
   **"Chưa phân loại"** (3 chương trình) trên cả màn lẫn tệp xuất; **không** có nhãn *"Không xác định"*
   ⇒ **đã đúng `:987`/`:991`**, không phải lỗi. Đối chiếu dữ liệu gốc: `GET /api/v1/chuong-trinh-htpls`
   cho đúng **3** chương trình có `linhVucId = null` ở trạng thái được đếm (`CT-20260721-0004` DA_DUYET ·
   `CT-20260721-0003` HOAN_THANH · `CT-20260721-0002` DANG_THUC_HIEN) ⇒ con số 3 là đúng.

### 🔴 Phát hiện mới ngoài vế đối tác nêu — CHƯA mở phiếu

> **Đã đo lại bằng đường thứ hai lúc 14:52–15:01 (cửa ③) và ĐÃ SỬA mô tả.** Mô tả đầu tiên lúc 13:38
> ("khoá do **xoá bộ lọc Lĩnh vực**") **KHÔNG tái hiện** khi tải lại trang và là **quy kết sai nguyên
> nhân** — bộ lọc Lĩnh vực không liên quan. Nguyên nhân thật ghi ở dưới.

**Sau khi xuất tệp thành công một lần, lần bấm [Xem báo cáo] kế tiếp làm [Xuất Excel] / [Xuất PDF] bị
khoá, và khoá dính cho tới khi tải lại trang — dù báo cáo trên màn vẫn đang có dữ liệu.**

Phép đo lại ngày 2026-08-06, cùng bản dựng **V1.0.8**, cùng tài khoản `cbnv_tw_04` (CB_NV_TW, cấp TW),
**tải lại trang `/bao-cao` từ đầu** trước mỗi nhánh để loại trừ trạng thái cũ của ứng dụng một trang:

| Nhánh | Chuỗi thao tác (đều bằng chuột thật) | Nút xuất |
|---|---|---|
| ① | Tải lại trang → chọn Lĩnh vực *Lao động* → [Xem báo cáo] → **xoá** Lĩnh vực → [Xem báo cáo] (Tổng 7, tạo lúc 14:54) | **VẪN BẬT** |
| ② | Tải lại trang → **chưa từng chạm** ô Lĩnh vực → [Xem báo cáo] (Tổng 7, tạo lúc 14:56) | **VẪN BẬT** |
| ③ | Tải lại trang → [Xem báo cáo] (Tổng 7, nút bật) → **[Xuất Excel] chạy xong, có tệp về** → bấm [Xem báo cáo] lần 2, **không đổi một bộ lọc nào** (Tổng 7 vẫn hiện, tạo lúc 15:00) | **BỊ KHOÁ** |

Nhánh ③ tái hiện **2 lần** trong phiên (lượt 1 lúc 14:57→14:58 có kèm xoá bộ lọc, lượt 2 lúc 15:00 **không
đụng bộ lọc nào**) ⇒ yếu tố quyết định là **lần xuất tệp trước đó**, không phải thao tác với bộ lọc.
Sau khi đã khoá: bấm [Xem báo cáo] thêm lần nữa, hoặc đổi sang lọc Lĩnh vực khác (báo cáo vẫn trả dữ
liệu, *Thời điểm tạo* đổi 14:58 → 14:59) — **vẫn khoá**; chỉ **tải lại trang** mới mở lại được.

**Đường đo thứ hai — gọi thẳng máy chủ đúng lúc nút đang khoá** (cùng phiên `cbnv_tw_04`, cùng tiêu chí
Năm 2026 · Toàn quốc · **không** truyền lĩnh vực):
`POST /api/v1/bao-cao/export` `{loaiBaoCao: BC_CT_THEO_LINH_VUC, kyBaoCao: NAM, tuNgay 2026-01-01,
denNgay 2026-12-31, filterDacThu {}, formatXuat XLSX}` → **200**,
`content-type: …spreadsheetml.sheet`, `content-disposition: attachment; filename="BaoCaoCtTheoLinhVuc_20260806_1501.xlsx"`,
**6 673 byte**, magic `PK` — **tệp hợp lệ**. Mở tệp ra đọc: đủ phần đầu (tiêu đề · kỳ · khoảng thời gian ·
đơn vị · ngày tạo), *Tổng số chương trình = 7*, bảng *Chưa phân loại 3 · Lao động 1 · Đất đai 1 · Thuế 1 ·
Thương mại 1* — **khớp đúng từng hàng với màn** đang bị khoá nút.

**Danh tính phiên trước/sau phép đo quyết định** (§9b): `userId 9101c6bb-6b1d-4f00-8c3c-2247f5b22e07` ·
*CB Nghiệp vụ - Trung ương #04* · `["CB_NV_TW"]` — **không đổi**, không lẫn phiên song song.

⇒ **Kết luận: lỗi trạng thái nút phía giao diện (FE).** Máy chủ **không** từ chối: đúng thời điểm giao
diện khoá nút, cùng bộ tiêu chí đó vẫn xuất ra tệp đầy đủ và đúng số. Đối chiếu đặc tả: `:1052` đặt điều
kiện của nút Xuất Excel là *"Sau khi đã 'Xem báo cáo'"* — ở đây người dùng **đã** Xem báo cáo, màn **đang**
có dữ liệu, mà nút vẫn khoá. Tác động thực tế: người dùng chỉ xuất được **1 tệp mỗi lần tải trang**.

Ảnh: [`C1`](../image/CTTLV_05-C1-nhanh1-tai-lai-trang-chon-roi-xoa-linhvuc-nut-xuat-VAN-BAT-V108.png) ·
[`C2`](../image/CTTLV_05-C2-nhanh2-chua-tung-chon-linhvuc-nut-xuat-VAN-BAT-V108.png) ·
[`C3`](../image/CTTLV_05-C3-nhanh3-sau-khi-xuat-excel-thanh-cong-bam-xem-bao-cao-lan-2-nut-xuat-bi-KHOA-V108.png).
Nhật ký đo đầy đủ: [`image/CTTLV_05-cua3-do-lai-nut-xuat-bi-khoa.txt`](../image/CTTLV_05-cua3-do-lai-nut-xuat-bi-khoa.txt).
Ảnh cũ [`A5`](../image/CTTLV_05-A5-nut-xuat-bi-khoa-sau-khi-xoa-bo-loc-linhvuc-V108.png) vẫn là bằng chứng
hợp lệ của **hiện tượng** (nút khoá khi màn có dữ liệu), chỉ **chú thích nguyên nhân** của nó là sai.

Đã tra cửa ② (grep toàn bộ `bug-report*.md` kể cả file `Pass-`, tra theo **triệu chứng**): **chưa có
phiếu nào** cho triệu chứng này. Theo quy tắc của đợt, bug ngoài phạm vi cần **mở dòng mới trên bảng
theo dõi** phải được **phiên chính duyệt mã trước** ⇒ **đã DỪNG và báo về phiên chính**, không tự ghi.
**Không kéo verdict của case** (flow §Ca biên): phép đo quyết định của vế đối tác nêu chạy ở dạng ① ngay
sau khi tải trang, với nút xuất đang bật, không bị phát hiện này làm sai lệch.

### Ảnh đã chụp (mỗi ảnh 1 dòng: tên tệp + thấy gì)

| Ảnh | Thấy gì |
|---|---|
| [`image/CTTLV_05-A2-dang1-ngay-sau-bam-xuat-excel-V108.png`](../image/CTTLV_05-A2-dang1-ngay-sau-bam-xuat-excel-V108.png) | Nhánh A, vai trò *CB Nghiệp vụ - Trung ương #04* (`BTP · TW`, avatar CƯ), bản dựng `HTPLDN · V1.0.8`; bộ lọc trùng khít ảnh vòng 1 của đối tác (BC Chương trình theo lĩnh vực · Năm · 01/01/2026–31/12/2026 · Toàn quốc · *Chọn Lĩnh vực* để trống); báo cáo *Thời điểm tạo 06/08/2026 13:32*, **Tổng chương trình 7**, **chỉ có 1 thẻ** (không còn *Tổng DN tham gia*); ngay sau khi bấm [Xuất Excel] **không có thông báo đỏ nào** ở đúng vị trí mà 2 ảnh đối tác hiện lỗi |
| [`image/CTTLV_05-A3-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png`](../image/CTTLV_05-A3-dang2b-donvi-BoCongAn-khong-co-du-lieu-nut-xuat-bi-khoa-V108.png) | Nhánh A dạng ②b: Đơn vị = **Bộ Công an (BCA)** → chữ *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"*, hai nút **[Xuất Excel] và [Xuất PDF] xám / bị khoá** |
| [`image/CTTLV_05-A4-dang3-loc-linhvuc-LaoDong-man-hinh-truoc-khi-xuat-V108.png`](../image/CTTLV_05-A4-dang3-loc-linhvuc-LaoDong-man-hinh-truoc-khi-xuat-V108.png) | Nhánh A dạng ③: ô *Lĩnh vực* = **Lao động**, báo cáo *Thời điểm tạo 13:37*, **Tổng chương trình 1**, bảng chỉ còn hàng *Lao động* — trạng thái màn ngay trước khi bấm [Xuất Excel] |
| [`image/CTTLV_05-A5-nut-xuat-bi-khoa-sau-khi-xoa-bo-loc-linhvuc-V108.png`](../image/CTTLV_05-A5-nut-xuat-bi-khoa-sau-khi-xoa-bo-loc-linhvuc-V108.png) | **Phát hiện mới (chú thích đã sửa 15:05):** báo cáo hiện đủ (*Thời điểm tạo 13:38*, Tổng 7) nhưng **[Xuất Excel] và [Xuất PDF] xám / bị khoá**. Lúc chụp mình quy cho việc *xoá bộ lọc Lĩnh vực*; đo lại lúc 14:52–15:01 cho thấy nguyên nhân thật là **đã xuất tệp thành công trước đó rồi bấm [Xem báo cáo] lần nữa** — ảnh vẫn đúng về hiện tượng, sai về nguyên nhân |
| [`image/CTTLV_05-A6-dang3b-locDatDai-luot-chup-thu-3-hen-gio-bam-truoc-2500ms-V108.png`](../image/CTTLV_05-A6-dang3b-locDatDai-luot-chup-thu-3-hen-gio-bam-truoc-2500ms-V108.png) | Nhánh A dạng ③b: *Lĩnh vực* = **Đất đai**, *Thời điểm tạo 13:41*, **Tổng chương trình 1**; lượt chụp thứ 3 (hẹn giờ bấm trước 2500 ms) — **vẫn không bắt được lớp thông báo**, màn không có thông báo lỗi nào |
| [`image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png`](../image/CTTLV_05-B1-qtht-xem-duoc-bao-cao-day-du-truoc-khi-bam-xuat-V108.png) | Nhánh B: vai trò **Quản trị hệ thống** (avatar QT, `BTP · TW`), bộ lọc dạng ① trùng khít ảnh đối tác; **báo cáo XEM ĐƯỢC đầy đủ** — *Thời điểm tạo 13:44*, Tổng chương trình 7 + biểu đồ; nút [Xuất Excel] đang bật |
| [`image/CTTLV_05-B2-qtht-ngay-sau-bam-xuat-excel-V108.png`](../image/CTTLV_05-B2-qtht-ngay-sau-bam-xuat-excel-V108.png) | Nhánh B, **ngay sau khi bấm [Xuất Excel]**: nút [Xuất Excel] đang được chọn (viền xanh), màn giữ nguyên báo cáo 7; **ảnh không bắt được lớp thông báo "Forbidden"** — chữ và phản hồi 403 ghi ở tệp `.txt` kèm theo |
| [`image/CTTLV_05-C1-nhanh1-tai-lai-trang-chon-roi-xoa-linhvuc-nut-xuat-VAN-BAT-V108.png`](../image/CTTLV_05-C1-nhanh1-tai-lai-trang-chon-roi-xoa-linhvuc-nut-xuat-VAN-BAT-V108.png) | Đo lại cửa ③ nhánh ①: tải lại trang → chọn rồi **xoá** bộ lọc *Lĩnh vực* → [Xem báo cáo]; báo cáo *Thời điểm tạo 14:54*, Tổng 7, và **[Xuất Excel] + [Xuất PDF] vẫn sáng / bấm được** ⇒ mô tả "khoá do xoá bộ lọc" **không tái hiện** |
| [`image/CTTLV_05-C2-nhanh2-chua-tung-chon-linhvuc-nut-xuat-VAN-BAT-V108.png`](../image/CTTLV_05-C2-nhanh2-chua-tung-chon-linhvuc-nut-xuat-VAN-BAT-V108.png) | Đo lại cửa ③ nhánh ②: tải lại trang, **chưa từng chạm** ô *Lĩnh vực* → [Xem báo cáo]; *Thời điểm tạo 14:56*, Tổng 7, **hai nút xuất sáng** |
| [`image/CTTLV_05-C3-nhanh3-sau-khi-xuat-excel-thanh-cong-bam-xem-bao-cao-lan-2-nut-xuat-bi-KHOA-V108.png`](../image/CTTLV_05-C3-nhanh3-sau-khi-xuat-excel-thanh-cong-bam-xem-bao-cao-lan-2-nut-xuat-bi-KHOA-V108.png) | Đo lại cửa ③ nhánh ③ (**nguyên nhân thật**): tải lại trang → [Xem báo cáo] → **[Xuất Excel] chạy xong có tệp** → bấm [Xem báo cáo] lần 2 **không đổi bộ lọc nào**; màn vẫn đủ dữ liệu (*Thời điểm tạo 15:00*, Tổng 7, bảng 5 hàng) nhưng **[Xuất Excel] và [Xuất PDF] xám / bị khoá** |

## 8. Verdict

### 🔁 **Reopen**

**Case gộp 3 vế** (mục 1) → theo §Ca biên của flow: *còn ≥1 vế lỗi → Reopen*.

| Vế | Kết quả |
|---|---|
| (a) Không xuất được tệp | **CÒN LỖI ở vai trò của đối tác.** Vai trò đặc tả (CB Nghiệp vụ TW) xuất được bình thường; nhưng chính vai trò **QTHT** mà đối tác dùng vẫn bị chặn ở bước xuất, và chữ hiện ra vẫn đúng chuỗi **"Forbidden"** của vòng 2 — trái yêu cầu `srs-fr-11-bao-cao.md:117`. Câu của vòng 1 (`:116`) thì không còn tái hiện |
| (b) Tên tệp | **Đạt.** `BaoCaoCtTheoLinhVuc_20260806_1333.xlsx` đúng khuôn `:85`+`:86` (áp quyết định BA ngày 2026-08-04), không chấm Fail vì khác literal `BaoCaoChuongTrinh_…` của đối tác |
| (c) Nội dung tệp + tự động tải về | **Đạt.** Tệp tự về máy khi bấm nút; đủ phần đầu `:1092`; đúng khuôn bảng *hàng = lĩnh vực, cột = số CT* (`:990` + `:981`–`:983`); số khớp màn từng hàng và cộng dọc = tổng; áp đúng bộ lọc `:1280` |

0 GAP (đủ 5 dòng mục 6) · M = 3 + 2 nhánh phụ · chạy đủ luồng bằng thao tác giao diện thật · có đường đo
thứ hai. Đủ điều kiện ra verdict.

⚠️ **Giới hạn hiệu lực:** kết luận này chỉ có hiệu lực cho môi trường `18.143.165.120.nip.io` và bản dựng
**V1.0.8** (`assets/index-CNwX9JjX.js`). Đối tác báo lỗi trên `htpldn-uat.ospgroup.vn` — chưa đối chiếu
bản dựng của env đó. Phần đã hết lỗi (vế b, c và nhánh CB Nghiệp vụ của vế a) là **đạt tạm**, cho tới khi
bản dựng này lên env của đối tác.

⚠️ **Không kết luận "fix đã có tác dụng":** không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng trước
khi sửa, nên chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**.

---

## Mục sửa đổi

- **2026-08-06 13:50** — **KHÔNG sửa mục 4 và mục 5** (tiêu chí giữ nguyên như lúc viết lúc 13:26, trước
  khi mở màn Báo cáo thống kê trên env verify). Chỉ **điền** cột "Mình test lần này" + "GAP?" của mục 6,
  điền **bản dựng** ở đầu file (ô đó vốn để trống chờ giai đoạn B) và **bổ sung** mục 7 + 8.
  Hai nhánh phụ ②b và ③b là **phương án dự phòng đã viết sẵn trong mục 5** (đoạn ⚠️ Bẫy), không phải
  tiêu chí mới thêm sau khi thấy kết quả.
- **2026-08-06 15:05** — **Chỉ sửa mục 7**, phần *🔴 Phát hiện mới* + bảng ảnh; **không** đụng mục 4, 5, 6
  và **không** đổi verdict (vẫn 🔁 Reopen — phát hiện này chưa bao giờ tham gia quyết verdict). Lý do sửa:
  phiên chính yêu cầu đóng **cửa ③ (đo lại bằng đường thứ hai)**; kết quả đo lại 14:52–15:01 **bác bỏ**
  nguyên nhân đã ghi lúc 13:38 ("khoá do xoá bộ lọc Lĩnh vực") và xác định nguyên nhân thật là **đã xuất
  tệp thành công rồi bấm [Xem báo cáo] lần kế tiếp**, kèm kết luận **lỗi phía giao diện** dựa trên phép
  gọi thẳng máy chủ trả 200 + tệp hợp lệ đúng lúc nút bị khoá. Thêm 3 ảnh C1/C2/C3 + tệp nhật ký đo.
