# Tiêu chí verify — SLCTHT_06 (tab `bug`, dòng 267)

Mã case: SLCTHT_06          Thời điểm viết: 2026-08-06 12:20 (viết XONG trước khi mở màn Báo cáo thống kê)
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** (chuỗi phiên bản in
ở chân logo trong trang; **dấu vân tay bó mã giao diện `assets/index-CNwX9JjX.js`**) — đo lúc
2026-08-06 12:24–12:33. Trang được mở MỚI trong phiên này (không dùng tab cũ) nên chắc chắn chạy bản dựng
hiện hành. Đã tra `/api/v1/health` ở đợt trước (404, không có endpoint công bố phiên bản) và header phản
hồi (không mang số hiệu bản dựng).

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A của flow):
`reverify-week-4/reverify-round-2026-08-03/KET-QUA-REVERIFY-VONG-2.md` dòng 82 (SLCTHT_06 — ghi ✅ Pass
ngày 03/08/2026) và dòng 83 (SLCTHT_07 — ⚠️ BA confirm) · `reverify-week-4/DANH-SACH-53-BUG-REOPEN-KET-QUA-QA.md`
dòng 70 · `reverify-round-2026-08-05/cond/SLCTHT_07.md` + `SLCTHT_07-uat.md` (đo bản PDF cùng loại BC) ·
`bug-con-fail-doi-tac-2026-07-31.csv` dòng 182 (nguyên văn ô của đối tác).
⚠️ Các hồ sơ trên chứa **số đo cũ** (vd "5 chương trình", "xuất Excel OK, số liệu khớp"). Mục 4 và mục 5
dưới đây suy từ **đặc tả** `srs-fr-11-bao-cao.md` (đã mở file đọc từng dòng), **không** lấy số đo cũ làm
ngưỡng — cụ thể: tiêu chí (d) đòi tệp khớp **số hiện trên màn tại thời điểm đo**, không chốt cứng con số 5.

---

## 1. Đối tác phản ánh

Case gộp **3 vế** (tách theo ô `Kết quả mong đợi` + `Kết quả thực tế` + `TKM phản hồi lần 1`):

- **(a) Không xuất được tệp.** Bấm **[Xuất Excel]** trên màn *Báo cáo thống kê* (loại BC = *BC Số lượng
  chương trình hỗ trợ*) thì hệ thống **không giao tệp nào**, chỉ hiện thông báo lỗi.
  - Vòng 1 (16/07/2026, bản dựng **V1.0**): thông báo đỏ ✗ **"Không thể tạo file xuất. Vui lòng thử lại."**
  - Vòng 2 (31/07/2026, bản dựng **V1.0.3**): thông báo đỏ ✗ **"Forbidden"** — **đổi hẳn câu chữ**, sang
    một chuỗi tiếng Anh thô.
- **(b) Tên tệp.** Kỳ vọng của đối tác: tệp tải về tên `BaoCaoChuongTrinh_{YYYYMMDD_HHmm}.xlsx`.
- **(c) Nội dung tệp.** Kỳ vọng của đối tác: *"Hệ thống xuất **toàn bộ**"* — tệp chứa trọn dữ liệu báo cáo
  đang xem, không phải một phần.

**Lệch giữa 2 vòng bằng chứng** (bắt buộc ghi theo §Cổng bằng chứng): cùng URL, cùng vai trò, cùng bộ lọc,
**khác bản dựng** (V1.0 → V1.0.3) và **khác câu thông báo**. Ảnh vòng 2 hiện thêm 2 thẻ *Đang thực hiện = 4*
và *Hoàn thành = 1* mà ảnh vòng 1 chưa chụp tới (ảnh vòng 1 bị cắt dưới thẻ *Tổng chương trình*).
⇒ Không được coi 2 vòng là cùng một triệu chứng; vế (a) phải đo cho **cả hai** câu thông báo.

**Bằng chứng đã mở đọc full-res:**
- `partner-evidence/SLCTHT_06.jpg` (vòng 1). Thấy: thanh địa chỉ
  `htpldn-uat.ospgroup.vn/bao-cao?loai=so-luong-ct-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`;
  chân logo sidebar `HTPLDN · V1.0`; góc phải `BTP · TW` + avatar `QV` + **Quản trị viên QTHT**;
  breadcrumb *Trang chủ / Báo cáo thống kê*; **thông báo đỏ ✗ "Không thể tạo file xuất. Vui lòng thử lại."**
  nổi giữa đỉnh trang; form lọc: *Loại báo cáo* = **BC Số lượng chương trình hỗ trợ**, *Kỳ báo cáo* = **Năm**,
  *Thời gian* **Từ 01/01/2026 — Đến 31/12/2026**, *Đơn vị* = **Toàn quốc**, *Trạng thái chương trình* = **để
  trống** (placeholder xám *"Chọn Trạng thái chương trình"*); hàng nút **[Xem báo cáo] [Xuất Excel] [Xuất PDF]**;
  khối kết quả **"BC Số lượng chương trình hỗ trợ"** — *Kỳ: Năm · 01/01/2026 → 31/12/2026 · Đơn vị: Toàn quốc*,
  **Thời điểm tạo: 16/07/2026 16:39**, thẻ **Tổng chương trình = 5**; đồng hồ máy **04:42 PM 2026-07-16**.
- `partner-evidence/SLCTHT_06_v2.jpg` (vòng 2). Thấy: **cùng URL, cùng bộ lọc, cùng vai trò Quản trị viên
  QTHT / BTP · TW**; chân logo `HTPLDN · V1.0.3`; **thông báo đỏ ✗ "Forbidden"** ở đúng vị trí đó; khối kết
  quả **Thời điểm tạo: 31/07/2026 15:26**, ba thẻ **Tổng chương trình 5 · Đang thực hiện 4 · Hoàn thành 1**;
  đồng hồ máy **03:28 PM 2026-07-31**; trên thanh trình duyệt có **biểu tượng tải xuống** (dấu vết của các
  lượt tải trước, không chứng minh lượt này có tệp — ảnh không mở khay tải).

## 2. Đặc tả nói gì

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (đã mở file
đọc trực tiếp từng dòng dưới đây, không lấy số dòng từ trí nhớ).

**Vế (a) — quyền + luồng xuất:**
- `:62` — Preconditions chung TPL-REPORT-FULL: *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt
  (TW/BN/ĐP)"*.
- `:79` — Processing chung bước 1: `| 1 | Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01 |`
- `:81` — bước 3: *"Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc, BN chỉ thấy BN mình, ĐP chỉ thấy ĐP
  mình…"*
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
- `:1268` — BR-AUTH-08: *"…TW thấy toàn quốc, BN thấy BN, ĐP thấy ĐP"*, cột **Ngoại lệ = "QTHT bypass"**,
  Áp dụng = *Toàn bộ FR-IX*.

**Vế (b) — tên tệp:**
- `:85` — Processing chung bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp
  `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp
  `[BA chốt 2026-08-04]`"*.
- `:86` — định nghĩa token: *"`{TenBaoCao}` là tên loại báo cáo viết liền kiểu PascalCase, bỏ dấu tiếng Việt
  và bỏ mọi ký tự không phải chữ/số (dấu `/`, khoảng trắng, dấu câu)"* `[BA chốt 2026-08-04]`.
- `:123` — AC chung: *"**Given** CB nhấn "Xuất Excel" **When** click **Then** tải file .xlsx khổ A4 Times New
  Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"*.
- `:1092` — Quy tắc tương tác SCR-IX-01: *"Tên tệp cả hai định dạng theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`
  `[BA chốt 2026-08-04]`"*.

> 🔴 **Kỳ vọng (b) của đối tác lệch đặc tả — nhưng BA ĐÃ chốt đúng điểm này.** Đối tác đòi literal
> `BaoCaoChuongTrinh_…`; quy tắc `:86` suy ra tên từ **tên loại báo cáo** (*"BC Số lượng chương trình hỗ trợ"*),
> không phải chuỗi cố định "BaoCaoChuongTrinh". Cả `:85`, `:86`, `:1092` đều gắn nhãn nguồn + ngày
> **`[BA chốt 2026-08-04]`**, tức **sau** cả 2 vòng test của đối tác (16/07 và 31/07). Theo §Rẽ nhánh của flow
> (*"Ngoại lệ duy nhất — BA ĐÃ chốt trước đúng điểm tranh chấp này, dẫn được nguồn kèm ngày → áp quyết định
> có sẵn"*), vế (b) **áp khuôn của đặc tả**, KHÔNG đẩy sang cần-BA và KHÔNG chấm Fail vì tên khác literal
> của đối tác. Phần `_{YYYYMMDD_HHmm}` thì đối tác và đặc tả **trùng khớp** ⇒ vẫn là tiêu chí bắt buộc.

**Vế (c) — nội dung tệp:**
- `:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file."*
- `:1280` — BR-DATA-06: *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không
  vượt quá 10,000 rows/file"*, Áp dụng = *Toàn bộ FR-IX*.
- `:87` — bước 9: *"Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo"*.
- `:88` — bước 10: *"Ghi nhật ký thao tác (xem/xuất báo cáo)"* (BR-DATA-05, xem thêm `:1274`).
- **FR-IX-20 (UC143) `:878`–`:914`** — *BC Số lượng CT hỗ trợ*:
  - `:889` Tác nhân: *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*
  - `:897` Input đặc thù: `| 1 | trang_thai_ct | text | N | DANG_THUC_HIEN / HOAN_THANH | — | Chọn |`
  - `:899` Công thức: *"Đếm CT HTPL đang thực hiện / hoàn thành, theo phạm vi đơn vị"*
  - `:907`–`:911` Output đặc thù, cột *Điều kiện* của cả 5 dòng đều là **"Luôn"**:
    `tong_ct` · `dang_thuc_hien` · `hoan_thanh` ·
    `theo_don_vi[]` = `{don_vi, ten, so_ct, dang_thuc_hien, hoan_thanh}` · `theo_ky[]` = `{ky, so_ct}`
  - `:914` AC bổ sung: *"**Given** CB tạo BC **When** hiển thị **Then** tổng CT phân theo đơn vị + trạng thái"*
- `:113` — E3: `| E3 | Không có dữ liệu | INF-RPT-01 | "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn" | INFO |`

**IM LẶNG về** (⇒ CẤM chấm Fail vì mấy thứ này):
tên sheet trong workbook · thứ tự cột trong tệp · có đóng khung / tô màu / in đậm không · có dòng tổng cuối
bảng không · định dạng số và định dạng ngày cụ thể trong ô · biểu đồ có được nhúng vào tệp `.xlsx` không ·
tệp xuất có mấy sheet · **vai trò QTHT có được XEM/XUẤT báo cáo hay không** (`:62` và `:889` chỉ **liệt kê**
CB NV / CB PD, **không** viết câu cấm QTHT; `:1268` lại cho QTHT **bypass** phạm vi đơn vị — hai chỗ này
không đủ để kết luận QTHT bị cấm) · thông báo lỗi hiển thị ở dạng lớp nổi hay inline · mã lỗi có lộ ra giao
diện hay không.

## 3. Precondition

- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → menu **Báo cáo thống kê** → *Loại báo cáo* =
  **BC Số lượng chương trình hỗ trợ** (URL mang `?loai=so-luong-ct-ho-tro`).
- **Tài khoản — đo CẢ 2 nhánh, cùng bộ tiêu chí:**

  | Nhánh | Tài khoản | Vai trò | Dùng để |
  |---|---|---|---|
  | **A — ra verdict** | `cbnv_tw_04` / `Test@1234` | CB_NV_TW, cấp TW ⇒ phạm vi *Toàn quốc*, khớp `BTP · TW` của đối tác; đúng tác nhân `:62` + `:889` | quyết Pass / Reopen |
  | **B — đối chứng** | `admin` / `Secret@123` | QTHT — **trùng khít vai trò trên cả 2 ảnh đối tác** | giải thích triệu chứng **"Forbidden"** vòng 2; đóng dòng GAP *Vai trò / tài khoản* |

  Tài khoản quản trị **không** được dùng để ra verdict (quyền rộng che lỗi phân quyền) — nhánh B chỉ đối chứng.
  Rule 7 nếu khoá: fallback **cùng vai trò + cùng cấp** `cbnv_tw_04` → `cbnv_tw_05` → `cbnv_tw_03`…, tuyệt
  đối không đổi vai trò/cấp; ghi rõ tài khoản THỰC đã dùng.
- **Dữ liệu tiền đề:** ≥ 1 chương trình HTPL trong khoảng **01/01/2026 – 31/12/2026** ở trạng thái được `:82`
  cho phép đếm (đã duyệt / đang thực hiện / hoàn thành), thuộc phạm vi TW. Muốn đo được **cả 3 dạng ở mục 5**
  thì cần **≥ 1 CT `Đang thực hiện`** và **≥ 1 CT `Hoàn thành`**, trong đó **≥ 1 CT thuộc *Cục Bổ trợ tư pháp
  - Bộ Tư pháp*.** Kiểm trước bằng màn **CT HTPLDN** hoặc `GET /api/v1/chuong-trinh-htpls`.
  Thiếu → **được seed** qua BE API (`create → submit → approve bằng tài khoản KHÁC → publish/activate/complete
  bằng người tạo`, mỗi bước cần `version`) và **bắt buộc khai** bản ghi nào · đổi gì · env nào vào mục 7 + bug entry.
  Tiền đề **tạo được mà không tạo → CẤM mọi verdict, kể cả ô trống.**
- **Bẫy cache máy chủ:** báo cáo thống kê có cache phía máy chủ. Sau khi seed mà số không đổi → đọc trường
  **"Thời điểm tạo"** trên màn; ép khoá cache mới bằng cách **đổi `denNgay` 1 ngày**. `cache:'reload'` chỉ bust
  cache trình duyệt ⇒ không dùng làm căn cứ.

## 4. Tiêu chí chấm

**✅ PASS khi — đủ CẢ 6 điều dưới đây (đo được):**

- **(a) Nhánh A giao được tệp, không có thông báo lỗi.** Với `cbnv_tw_04`, ở dạng dữ liệu ① mục 5: bấm
  **[Xem báo cáo]** → chờ khối kết quả hiện → bấm **[Xuất Excel]**. Đo bằng bộ bắt thông báo cài **trước**
  khi bấm: **0** thông báo mang nội dung lỗi/từ chối (đếm theo **mốc giờ khác nhau**, không theo số phần tử),
  và hệ thống **giao ra một tệp** (tệp về máy, hoặc phản hồi máy chủ của chính thao tác đó có thân nhị phân
  tải về được). Số request của thao tác đếm bằng `list_network_requests` (nút có thể là GET nên
  `window.__qa.net` không ghi).
- **(b) Tệp là .xlsx thật.** Mở được bằng thư viện đọc xlsx (`openpyxl`) hoặc giải nén zip đọc được
  `xl/workbook.xml` — **không** phải HTML/JSON đổi đuôi. (Mã 200 + có bytes **không** đủ để đạt (b).)
- **(c) Tên tệp đúng khuôn `:85`+`:86`+`:1092`:** dạng `<Tên>_<8 chữ số>_<4 chữ số>.xlsx`, trong đó
  `<Tên>` là **tên loại báo cáo viết liền, không dấu tiếng Việt, không khoảng trắng, không dấu câu**, và
  `<8 chữ số>_<4 chữ số>` là **ngày `YYYYMMDD` + gạch dưới + giờ phút `HHmm`** khớp thời điểm xuất (sai lệch
  ≤ 5 phút so với đồng hồ lúc bấm nút). Kiểm bằng biểu thức: `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`.
- **(d) Trong tệp có đủ phần đầu theo `:1092`:** đọc nội dung ô của tệp phải tìm thấy **tiêu đề báo cáo**,
  **kỳ báo cáo**, **khoảng thời gian tu_ngay–den_ngay**, **tên đơn vị** (hoặc "Toàn quốc"), **ngày tạo báo cáo**.
  Đủ 5 mảnh ⇒ đạt; thiếu bất kỳ mảnh nào ⇒ không đạt.
- **(e) Số liệu trong tệp KHỚP số liệu đang hiển thị trên màn** — phép đo quyết định, không được bỏ:
  - 3 thẻ tổng của FR-IX-20 `:907`–`:909`: **Tổng chương trình**, **Đang thực hiện**, **Hoàn thành** —
    3 số trong tệp bằng đúng 3 số trên màn ở **cùng một lần "Xem báo cáo"**.
  - Bảng theo đơn vị `:910`: mỗi hàng đơn vị trong tệp có mặt trên màn với **cùng số CT / đang thực hiện /
    hoàn thành**; số hàng đơn vị của tệp = số hàng trên màn.
  - Cộng dọc các hàng đơn vị = số thẻ tổng (nếu lệch ⇒ theo §"phép đo đang nói dối" là số sai, phải đo lại,
    chưa được kết luận).
  - Có phần theo kỳ `:911` (`{ky, so_ct}`) trong tệp.
- **(f) Áp đúng bộ lọc hiện tại (`:1280`)** — chứng minh bằng **so sánh giữa các dạng ở mục 5**:
  nội dung tệp của dạng ② (đơn vị cụ thể) và dạng ③ (có lọc trạng thái CT) **khác** nội dung tệp dạng ①, và
  mỗi tệp khớp đúng màn của chính bộ lọc đó theo tiêu chí (e). Riêng dạng ③ lọc `Hoàn thành`: tệp **không**
  chứa hàng dữ liệu của chương trình đang thực hiện.

**Nhánh B (đối chứng, `admin`/QTHT) — không quyết Pass/Fail của case, nhưng bắt buộc đo và ghi:**
lặp lại đúng dạng ① rồi ghi nhận: xuất được tệp, **hay** bị từ chối. Nếu bị từ chối thì đọc **nguyên văn**
chữ hiện ra và đối chiếu `:117`.

**❌ FAIL nếu (bất kỳ điều nào):**
- Nhánh A bấm [Xuất Excel] mà **không có tệp nào được giao**, hoặc hiện thông báo mang nghĩa từ chối/thất bại
  (gồm nhưng không giới hạn ở đúng 2 câu đối tác chụp).
- Tệp giao ra **không mở được** bằng thư viện đọc xlsx (HTML/JSON/tệp hỏng đổi đuôi).
- Tên tệp **không** có phần ngày-giờ `_YYYYMMDD_HHmm` trước `.xlsx`, hoặc còn dấu tiếng Việt / khoảng trắng /
  dấu câu trong phần tên báo cáo.
- Tệp **thiếu** bất kỳ mảnh nào trong 5 mảnh phần đầu ở (d).
- Bất kỳ số nào trong (e) **lệch** so với màn, hoặc thiếu hẳn bảng theo đơn vị / phần theo kỳ.
- Đổi bộ lọc mà **nội dung tệp không đổi** (dạng ②/③ ra tệp giống hệt dạng ①) ⇒ vi phạm `:1280`.
- **Nhánh A xuất được nhưng nhánh B (QTHT) bị chặn bằng chuỗi tiếng Anh thô "Forbidden"** ⇒ vẫn là **Reopen**:
  đây là vế **(a) đối tác có nêu** (ô *TKM phản hồi lần 1*), và câu chữ đó trái yêu cầu của `:117` — hệ thống
  khi từ chối vì thiếu quyền phải nói bằng thông báo tiếng Việt cho biết người dùng không có quyền xem báo cáo.
- Nhánh B bị chặn bằng **đúng khuôn tiếng Việt của `:117`** ⇒ **không** Fail vì câu chữ, nhưng khi đó còn tranh
  chấp *"QTHT có được xuất BC không"* mà đặc tả im lặng ⇒ **cần BA** (kèm mâu thuẫn hành vi: app cho QTHT **XEM**
  được báo cáo — ảnh đối tác có đủ số liệu — nhưng cấm **XUẤT**; nếu QTHT thật sự không có quyền thì `:79` bước 1
  phải chặn ngay từ bước Xem).

**KHÔNG được chấm Fail vì** (đặc tả im lặng — xem mục 2):
tên sheet · thứ tự cột · đóng khung/tô màu/in đậm · có hay không dòng tổng cuối bảng · định dạng số và ngày
trong ô · biểu đồ có nhúng vào tệp hay không · số lượng sheet · thông báo hiện dạng lớp nổi hay inline · mã
lỗi có lộ ra giao diện hay không · **tên tệp khác literal `BaoCaoChuongTrinh_…` mà đối tác ghi**, miễn vẫn
đúng khuôn `:85`+`:86` (BA chốt 2026-08-04 — xem khối trích ở mục 2) · khổ giấy A4 và font Times New Roman
cỡ 13 bên trong tệp `.xlsx` **không** dùng để chặn Pass ở lượt này *(đặc tả `:85` có nêu, nhưng đó là thuộc
tính trình bày khi in; nếu đo được thì ghi nhận, nếu không đo được thì ghi rõ "chưa đo" chứ không suy ra Fail)*.

## 5. Dạng dữ liệu phải phủ — M = 3

| # | Dạng | Cấu hình bộ lọc trên màn | Dùng để kiểm |
|---|---|---|---|
| ① | **Khớp khít cấu hình đối tác** | Kỳ = **Năm**, Từ **01/01/2026** → Đến **31/12/2026**, Đơn vị = **Toàn quốc**, Trạng thái chương trình = **để trống** | tái hiện đúng điều kiện 2 ảnh bằng chứng; đo (a)(b)(c)(d)(e) |
| ② | **Đơn vị cụ thể** | như ① nhưng Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)** | kiểm phạm vi đơn vị `:81` + bộ lọc đơn vị có vào tệp không (`:1280`) |
| ③ | **Có lọc trạng thái CT** | như ① nhưng Trạng thái chương trình = **Hoàn thành** | kiểm bộ lọc đặc thù `:897` (enum `DANG_THUC_HIEN`/`HOAN_THANH`) có được áp vào tệp không (`:1280`) |

**Nguồn xác định M** (tra theo thứ tự flow §"Xác định M", dừng ở bước ②):
- Bước ① *(đặc tả nói về nguồn dữ liệu)*: `:899` — báo cáo đếm CT HTPL **đang thực hiện / hoàn thành** theo
  **phạm vi đơn vị** ⇒ bản ghi vào báo cáo đến từ **2 trạng thái** và **nhiều đơn vị**.
- Bước ② *(bộ lọc + giá trị enum ngay trên màn đó)*: `:897` cho `trang_thai_ct` **2 enum** ·
  `:1049` dropdown đơn vị (*"TW: 'Toàn quốc' + chọn BN/ĐP bất kỳ"*) · `:1048` bộ lọc kỳ BC.
- Ràng buộc quyết định: `:1280` đòi **"File xuất theo bộ lọc hiện tại"**. Một cấu hình bộ lọc duy nhất chỉ
  chứng minh *hệ thống xuất được một tệp*, **không** chứng minh được tệp có bám bộ lọc — muốn kết luận phải
  có **≥ 2 cấu hình khác nhau** cho ra **≥ 2 nội dung khác nhau**. ⇒ **M = 1 không hợp lệ cho case này.**
  Chọn M = 3 để phủ **2 chiều lọc độc lập** (đơn vị `:81`/`:1049` và trạng thái CT `:897`) trên cùng một nền ①.

⚠️ Bẫy đã biết cho mục 5: nếu env chỉ có CT ở **một** trạng thái thì dạng ③ sẽ trùng dạng ① và **không phân
biệt được** "bộ lọc có tác dụng" với "bộ lọc bị bỏ qua" → bắt buộc seed cho đủ **cả 2 trạng thái** trước khi đo
(xem mục 3). Tương tự, nếu mọi CT đều thuộc **một** đơn vị thì dạng ② trùng dạng ① — khi đó phải ghi rõ hạn
chế này vào mục 7 thay vì coi như đã đóng.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên / QTHT**, đơn vị **BTP · TW** (góc phải màn, avatar `QV`) — **cả 2 vòng giống nhau** | Đo **cả 2 nhánh**. **A** `cbnv_tw_04` — hiển thị *"CB Nghiệp vụ - Trung ương #04 / Cán bộ Nghiệp vụ Trung ương"*, `BTP · TW`, phạm vi Toàn quốc (đúng tác nhân `:62`/`:889`). **B** `admin` — hiển thị *"Quản trị hệ thống"*, `BTP · TW`; giải mã access_token: `vaiTro=["QTHT"]`, `capDonVi="TW"`, `donViId=00000000-0000-4000-8000-000000000001` ⇒ **trùng khít vai trò + cấp + đơn vị của đối tác** (chỉ khác họ tên người dùng: env đối tác là *"Quản trị viên"*, env này là *"Quản trị hệ thống"* — cùng vai trò QTHT) | **Không** |
| Entity + trạng thái | **CHUONG_TRINH_HTPL**. Vòng 1 ảnh chỉ lộ *Tổng chương trình = 5*; vòng 2 lộ đủ **5 = 4 Đang thực hiện + 1 Hoàn thành** | Cùng entity **CHUONG_TRINH_HTPL**. Trong kỳ 2026, báo cáo đếm **7 = 5 Đã phê duyệt + 1 Đang thực hiện + 1 Hoàn thành** (khớp `:82`). Số bản ghi khác đối tác nhưng **cùng nhánh nghiệp vụ**: báo cáo CÓ dữ liệu (không rơi `:113`), có **cả** trạng thái Đang thực hiện và Hoàn thành như ảnh vòng 2 | **Không** — triệu chứng tái hiện nằm ở tầng quyền (HTTP 403 trước khi sinh tệp), không phụ thuộc số lượng bản ghi; đã kiểm chéo bằng dạng ③ (1 bản ghi) và ②b (0 bản ghi) đều cho kết quả nhất quán |
| Dữ liệu tiền đề | 5 chương trình trong kỳ 2026 trên env `htpldn-uat.ospgroup.vn`; báo cáo **có dữ liệu** (không rơi vào nhánh `:113`) ⇒ lỗi xuất tệp **không** do rỗng dữ liệu | Env verify có sẵn **14 chương trình** (`GET /api/v1/chuong-trinh-htpls`): DU_THAO 3 · CHO_PHE_DUYET 1 · HUY 1 · TAM_DUNG 1 · DA_DUYET 5 · DA_CONG_BO 1 · DANG_THUC_HIEN 1 · HOAN_THANH 1. Đã đủ **cả 2 trạng thái** mà mục 5 đòi ⇒ **KHÔNG cần seed, KHÔNG tạo/sửa/xoá bản ghi nào** | **Không** |
| Input / filter / giá trị nhập | Kỳ **Năm** · **01/01/2026 → 31/12/2026** · Đơn vị **Toàn quốc** · Trạng thái chương trình **để trống**; thao tác **[Xem báo cáo] rồi [Xuất Excel]** (đúng điều kiện hiển thị nút ở `:1052`) | **Giống hệt** ở dạng ①, cho **cả nhánh A và nhánh B** — URL sinh ra trùng khít ảnh đối tác: `/bao-cao?loai=so-luong-ct-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`. Xác nhận thêm `:1052`: nút [Xuất Excel] **bị khoá** cho tới khi bấm [Xem báo cáo] | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | **M = 1** — 1 cấu hình bộ lọc duy nhất, lặp ở 2 vòng; đối tác **không** thử đổi đơn vị hay lọc trạng thái ⇒ bằng chứng của họ không nói được gì về `:1280` | Nhánh A: **M = 3** (① Toàn quốc không lọc trạng thái · ② đơn vị BTP-TW · ③ trạng thái = Hoàn thành) **+ nhánh phụ ②b** (đơn vị Bộ Công an — 0 bản ghi). Nhánh B: dạng ① (đủ để tái hiện triệu chứng đối tác nêu). N = 7 chương trình ở dạng ①, 1 ở dạng ③, 0 ở dạng ②b | **Không** — riêng dạng ② rơi vào ca suy biến đã cảnh báo ở mục 5 (mọi CT thuộc cùng 1 đơn vị nên số liệu trùng dạng ①); đã đóng bằng **②b** chứng minh bộ lọc đơn vị thật sự lọc dữ liệu |

**3 dữ kiện neo của đối tác:**
- URL/bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=so-luong-ct-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
  (không có ID bản ghi đơn lẻ — đây là màn báo cáo tổng hợp, "bản ghi" chính là tập CT trong kỳ).
- Trạng thái entity: 5 chương trình trong kỳ — **4 Đang thực hiện + 1 Hoàn thành** (đọc từ ảnh vòng 2);
  báo cáo đã tạo thành công, *Thời điểm tạo* 16/07/2026 16:39 (vòng 1) và 31/07/2026 15:26 (vòng 2).
- Vai trò + env + bản dựng: **Quản trị viên / QTHT**, `BTP · TW`, env **`htpldn-uat.ospgroup.vn`**,
  bản dựng **V1.0** (vòng 1, 16/07/2026 16:42) và **V1.0.3** (vòng 2, 31/07/2026 15:28).

**Giới hạn hiệu lực (KHÔNG phải GAP):** đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn`; lượt này đo
trên env nội bộ `18.143.165.120.nip.io` theo chỉ định. Mọi kết luận Pass ở đây là **Pass tạm**, chỉ có hiệu
lực cho env + bản dựng ghi ở đầu file, cho tới khi bản dựng đó lên env của đối tác.

---

## 7. Kết quả đo (giai đoạn B)

**Bộ bắt thông báo:** script dùng chung `tools/toast-capture.js` (không lọc trùng · đọc `innerText` · đếm
request). **Tự kiểm trước mỗi lượt: `soObserverDangSong = 1`** ⇒ số liệu hợp lệ. Đếm thông báo theo **mốc
giờ khác nhau**; mọi lượt đều **1 request ↔ 1 khung thông báo**, không có double-toast.
Số request đếm bằng `list_network_requests` (nút xuất đi qua `POST`, nhưng vẫn đối chiếu cả 2 nguồn).
**Bẫy cache máy chủ đã loại trừ:** trường *Thời điểm tạo* đổi theo từng lượt Xem báo cáo
(12:24 → 12:26 → 12:28 → 12:29 → 12:32), không phải số cũ.

### Nhánh A — `cbnv_tw_04` (CB_NV_TW, cấp TW) — vai trò đặc tả, dùng để chấm

| Tiêu chí mục 4 | Đo được | Đạt? |
|---|---|:-:|
| (a) Giao được tệp, 0 thông báo lỗi | Dạng ①: 1 request `POST /api/v1/bao-cao/export` → **200**; 1 khung thông báo, chữ **"Đang tạo file..." → "Tạo file thành công."**; **không** có "Không thể tạo file xuất. Vui lòng thử lại." và **không** có "Forbidden" | ✅ |
| (b) Là .xlsx thật | 6.959 byte, magic `PK\x03\x04`, MIME `…spreadsheetml.sheet`, **mở được bằng `openpyxl`** | ✅ |
| (c) Tên tệp đúng khuôn `:85`+`:86` | `BaoCaoSoLuongCtHoTro_20260806_1224.xlsx` — khớp `^[A-Za-z0-9]+_\d{8}_\d{4}\.xlsx$`, không dấu/khoảng trắng/dấu câu; `20260806_1224` = đúng ngày giờ bấm nút. Lượt sau ra `_1227`, `_1228`, `_1229` ⇒ **xuất nhiều lần trong ngày không đè tệp**, đúng chủ đích `[BA chốt 2026-08-04]` | ✅ |
| (d) Phần đầu tệp đủ 5 mảnh (`:1092`) | A1 *BC Số lượng chương trình hỗ trợ* · A2 *Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)* · A3 *Đơn vị: Toàn quốc* · A4 *Ngày tạo: 06/08/2026* | ✅ |
| (e) Số liệu tệp khớp màn | Màn 7/1/1 ↔ tệp A8=7, A12=1, A16=1. Bảng *Theo đơn vị* tệp: `Cục Bổ trợ tư pháp - Bộ Tư pháp | 7 | 1 | 1` = đúng hàng duy nhất trên màn. Có *Theo kỳ* `Năm 2026 | 7` (`:911`). **Cộng khớp:** *Theo trạng thái* 5+1+1 = 7 = tổng | ✅ |
| (f) Áp đúng bộ lọc hiện tại (`:1280`) | Dạng ③ (trạng thái = Hoàn thành): tệp `_1227` ra 1/0/1, mục *Theo trạng thái* **chỉ còn dòng "Hoàn thành 1"** (mất hẳn 2 dòng của dạng ①) — khớp màn 1/0/1. Dạng ② (đơn vị BTP-TW): A3 đổi thành *"Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp"*. Dạng ②b (đơn vị Bộ Công an): màn báo *"Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn"* (đúng `:113`) + nút [Xuất Excel] bị khoá | ✅ |

⇒ **Nhánh A: đạt cả 6 tiêu chí.** Không tái hiện được câu *"Không thể tạo file xuất. Vui lòng thử lại."* của vòng 1.

### Nhánh B — `admin` (QTHT) — trùng khít vai trò đối tác, đối chứng

| Bước | Đo được |
|---|---|
| [Xem báo cáo] | `GET /api/v1/bao-cao/so-luong-ct-ho-tro?...` → **200**. Màn hiện **đầy đủ** báo cáo: 7 · 1 · 1 + bảng theo đơn vị + 2 biểu đồ. **0 thông báo**, không bị chặn ⇒ **QTHT XEM ĐƯỢC báo cáo.** |
| [Xuất Excel] | 1 request `POST /api/v1/bao-cao/export` → **403**. 1 khung thông báo (1 mốc giờ), chữ người dùng thấy: **"Forbidden"**. **Không có tệp nào được giao** (0 blob, 0 thẻ tải xuống). Thân phản hồi: `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden","requestId":"08e57ea9-1b56-4c28-9fe0-70a05ad37850"}}` |

⇒ **Tái hiện ĐÚNG triệu chứng vòng 2 của đối tác**, trên env verify + bản dựng V1.0.8.
Rơi đúng nhánh `❌ FAIL nếu` cuối cùng của mục 4: chữ hiển thị là chuỗi tiếng Anh thô **"Forbidden"**,
trong khi `:117` đòi hệ thống khi từ chối vì thiếu quyền phải cho người dùng biết **bằng tiếng Việt rằng
họ không có quyền xem báo cáo**. Kèm **mâu thuẫn hành vi**: `:79` bước 1 đặt việc kiểm quyền truy cập báo
cáo ở đầu luồng, nhưng thực tế bước Xem cho qua (200) rồi mới chặn ở bước Xuất (403).

### Đường đo thứ hai

Giao diện ↔ máy chủ **không mâu thuẫn**: mọi kết luận trên đều có đủ 2 nguồn — chữ đọc bằng `innerText`
trên DOM **và** mã/thân phản hồi lấy từ `list_network_requests` + `get_network_request`
(A: 4 lượt `POST /bao-cao/export` đều **200** kèm tệp · B: **403** kèm thân JSON `Forbidden`, không tệp).

### Hạn chế đã ghi nhận

- **Không chụp được ảnh lớp thông báo** (đã thử **4 lượt**: chụp ngay sau khi bấm · hẹn giờ bấm sau 2500ms
  rồi mới chụp · hẹn giờ 1500ms · bấm bằng JS rồi chụp ngay). Công cụ chụp không bắt được lớp nổi do thư
  viện giao diện dựng qua portal — **tiền lệ đã có** trong chính đợt này (bug entry QLTLPLCVV_15).
  Bằng chứng thay thế = chữ đọc bằng `innerText` + số đo chứng minh khung thông báo hiển thị **thật** với
  người dùng (nhánh A: `position: fixed`, khung `x=0 y=8 w=1432 h=42`, sống ≥ **2,279 s**; nhánh B: khung
  `w=1432 h=41`, sống ≥ **3,241 s**) + nguyên văn phản hồi máy chủ. Lưu ở
  [`image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt`](../image/SLCTHT_06-thong-bao-va-phan-hoi-may-chu.txt).
- Thao tác quyết định của dạng ① nhánh A dùng **công cụ bấm chuột thật** của trình duyệt; các lượt biến thể
  (②/③/②b và nhánh B) bấm bằng lệnh `click()` **trên đúng phần tử nút thật** trong trang — vẫn là sự kiện
  chuột thật do trình duyệt phát, không gọi thẳng API. Khai ra để người đọc biết.
- Dạng ② suy biến (số liệu trùng dạng ①) vì mọi chương trình trên env đều thuộc cùng một đơn vị — đã đóng
  bằng ②b, xem mục 6.

### Dữ liệu đã seed / thay đổi trên env

**KHÔNG seed, KHÔNG tạo/sửa/xoá bất kỳ bản ghi nào.** Env đã sẵn 14 chương trình đủ 2 trạng thái mục 5 đòi.
Toàn bộ thao tác là đọc (`GET` báo cáo) + xuất tệp (`POST /bao-cao/export`, chỉ sinh tệp, không đổi dữ liệu
nghiệp vụ — đúng Postconditions `:105`). Có đăng xuất `cbnv_tw_04` rồi đăng nhập `admin` để đo nhánh B.

## 8. Verdict

### 🔁 **Reopen**

**Case gộp 3 vế** (mục 1) → theo §Ca biên của flow: *còn ≥1 vế lỗi → Reopen*.

| Vế | Kết quả |
|---|---|
| (a) Không xuất được tệp | **CÒN LỖI ở vai trò của đối tác.** Vai trò đặc tả (CB NV TW) xuất được bình thường; nhưng chính vai trò **QTHT** mà đối tác dùng vẫn bị chặn, và chữ hiện ra vẫn đúng chuỗi **"Forbidden"** của vòng 2 — trái yêu cầu `srs-fr-11-bao-cao.md:117`. Câu của vòng 1 (`:116`) thì không còn tái hiện |
| (b) Tên tệp | **Đạt.** `BaoCaoSoLuongCtHoTro_20260806_1224.xlsx` đúng khuôn `:85`+`:86` (áp quyết định BA ngày 2026-08-04), không chấm Fail vì khác literal `BaoCaoChuongTrinh_…` của đối tác |
| (c) Nội dung tệp | **Đạt.** Đủ phần đầu `:1092`, đủ 5 nhóm output `:907`–`:911`, số khớp màn, áp đúng bộ lọc `:1280` |

0 GAP (đủ 5 dòng mục 6) · M = 3 + 1 nhánh phụ · chạy đủ luồng bằng thao tác giao diện thật · có đường đo
thứ hai. Đủ điều kiện ra verdict.

⚠️ **Giới hạn hiệu lực:** kết luận này chỉ có hiệu lực cho môi trường `18.143.165.120.nip.io` và bản dựng
**V1.0.8** (`assets/index-CNwX9JjX.js`). Đối tác báo lỗi trên `htpldn-uat.ospgroup.vn` — chưa đối chiếu bản
dựng của env đó. Phần đã hết lỗi (vế b, c và nhánh CB Nghiệp vụ của vế a) là **đạt tạm**, cho tới khi bản
dựng này lên env của đối tác.

⚠️ **Không kết luận "fix đã có tác dụng":** không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng trước
khi sửa, nên chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**.

---

## Mục sửa đổi

- **2026-08-06 12:40** — **KHÔNG sửa mục 4 và mục 5** (tiêu chí giữ nguyên như lúc viết trước khi mở màn).
  Chỉ **điền** cột "Mình test lần này" + "GAP?" của mục 6 và **bổ sung** mục 7 + 8 (phần kết quả).
  Bản dựng ở đầu file được điền đúng như thiết kế (ô đó vốn để trống chờ giai đoạn B).
