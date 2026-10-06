# Tiêu chí verify — SLHDVM_06

```
Mã case: SLHDVM_06 (tab `bug` dòng 174)      Thời điểm viết: 2026-08-06 12:20
Môi trường verify: https://18.143.165.120.nip.io       Thời điểm đo: 2026-08-06 12:23 → 12:41
Bản dựng (TỰ ĐO 2026-08-06 12:23, không chép từ B5-CONTEXT):
  · nhãn hiển thị trong app: HTPLDN · V1.0.8
  · bó mã: assets/index-CNwX9JjX.js · etag "6a73f6a4-1124fd" · 1 123 581 byte
  · index.html etag "6a73f6a4-428" · last-modified: Thu, 06 Aug 2026 02:51:16 GMT
  · DẤU VÂN TAY: md5 bó mã = e0e4f737b1fb7ab9409f459a4d0fa051
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow §Giai đoạn A):
> - `output/UAT_doi-tac/reverify-week-3/reverify-audit/SLHDVM_06/SLHDVM_06-network-evidence.md` — số đo cũ
>   21/07/2026 (`POST /api/v1/bao-cao/export` → 200, `content-disposition: attachment; filename="bao-cao-hoi-dap-2026-07-21.xlsx"`).
> - `output/UAT_doi-tac/reverify-week-3/cond/SLHDVM_06.md` và `.../reverify-week-4/reverify-round-2026-08-03/cond/SLHDVM_06.md` — bảng điều kiện cũ.
> - `B5-CONTEXT.md` §4 có nhắc số đo cũ 03/08/2026 (tên tệp `bao-cao-<slug>-YYYY-MM-DD.xlsx`).
>
> **Mục 4 và 5 dưới đây suy từ ĐẶC TẢ, không lấy số đo cũ làm ngưỡng.** Cụ thể: số đo cũ chỉ chứng minh
> "endpoint từng trả 200" — nó KHÔNG được dùng làm tiêu chí Pass, vì bar Pass của đợt này đòi **mở tệp ra đọc nội dung**.

---

## 1. Đối tác phản ánh

Case gộp **2 vòng**, cùng một thao tác (bấm **[Xuất Excel]** trên BC Số lượng hỏi đáp/vướng mắc pháp luật),
nhưng **triệu chứng khác nhau** ⇒ tách thành 2 vế:

- **Vế a (vòng 1, ô `Kết quả thực tế`)** — bấm [Xuất Excel] → hiện thông báo lỗi
  *"Không thể tạo file xuất. Vui lòng thử lại."* ⇒ **không có tệp nào được tải về**.
- **Vế b (vòng 2, ô `TKM phản hồi lần 1`, retest 31/07/2026)** — cùng thao tác → hiện thông báo *"Forbidden"*
  ⇒ vẫn không có tệp; triệu chứng đổi từ "lỗi tạo tệp" sang "bị chặn quyền".

`Kết quả mong đợi` của đối tác: *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng."*

🔴 **Case này KHÔNG đòi khuôn tên tệp** (khác 5 case còn lại của batch B5). Vế tên tệp **không** nằm trong
kỳ vọng đối tác ⇒ **không** được kéo verdict; nếu đo thấy tên tệp lệch đặc tả thì xử theo §Bug ngoài phạm vi
(báo phiên chính trước, không tự mở dòng mới).

### Bằng chứng — đã MỞ XEM full-res

| Vòng | Tệp | Frame/ảnh đã xem | Thấy gì |
|---|---|---|---|
| 1 | `partner-evidence/SLHDVM_06.webm` (3,2 MB, ~20 giây) | `frames/SLHDVM_06/t000.00s.jpg`, `t008.02s.jpg`, `t012.03s.jpg`, **`t016.05s.jpg` = khoảnh khắc lỗi** | Màn *Báo cáo thống kê*, loại BC *"BC Số lượng hỏi đáp/vướng mắc pháp luật"*, kỳ **Năm** 01/01/2026→31/12/2026, đơn vị **Toàn quốc**, **Lĩnh vực PL = Thuế**, Trạng thái HĐ trống. Báo cáo đã render: Tổng hỏi đáp **8** · Đã trả lời **3** · Chờ trả lời **5** · Tỷ lệ **37,5 %**, *Thời điểm tạo 15/07/2026 16:22*. Tại `t016.05s` hiện khung thông báo đỏ **"Không thể tạo file xuất. Vui lòng thử lại."** |
| 2 | `partner-evidence/SLHDVM_06_v2.jpg` | ảnh full-res | Cùng màn, cùng loại BC, kỳ **Năm** 01/01/2026→31/12/2026, **Toàn quốc**, **cả 2 bộ lọc đặc thù để trống**. Báo cáo: Tổng **60** · Đã trả lời **20** · Chờ **40** · **33,3 %**, *Thời điểm tạo 31/07/2026 14:03*. Khung thông báo đỏ **"Forbidden"** |

✅ **Kiểm bằng chứng có đúng case này không:** cả 2 tệp đều là màn *BC Số lượng hỏi đáp/vướng mắc pháp luật*
(FR-IX-01) — **đúng case**, không lệch mã.

⚠️ **Hai vòng KHÔNG cùng điều kiện** (bắt buộc ghi theo flow §Cổng bằng chứng):
- Bản dựng khác nhau: vòng 1 nhãn **HTPLDN · V1.0**, vòng 2 nhãn **HTPLDN · V1.0.2**.
- Bộ lọc khác nhau: vòng 1 có **Lĩnh vực PL = Thuế**, vòng 2 **không lọc**.
- Dữ liệu khác nhau: 8 hỏi đáp vs 60 hỏi đáp.
- Giống nhau: cùng env `htpldn-uat.ospgroup.vn`, cùng vai trò **Quản trị viên · QTHT**, cùng đơn vị **BTP · TW**.

---

## 2. Đặc tả nói gì

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` — **đã mở file đọc
đúng dòng 2026-08-06 12:20**, không lấy số dòng từ trí nhớ.

| Dòng | Nguyên văn (trích) |
|---|---|
| `:85` | *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp `[BA chốt 2026-08-04]`"* |
| `:113` | *"E3 · Không có dữ liệu · INF-RPT-01 · 'Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn' · INFO"* |
| `:116` | *"E6 · Lỗi xuất file · **ERR-RPT-04** · 'Không thể tạo file xuất. Vui lòng thử lại' · ERROR"* ⇒ đúng câu **vế a** |
| `:117` | *"E7 · Không có quyền · **ERR-RPT-05** · 'Bạn không có quyền xem báo cáo này' · ERROR"* ⇒ nhánh quyền của **vế b** |
| `:123` | *"**Given** CB nhấn 'Xuất Excel' **When** click **Then** tải file .xlsx khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"* |
| `:140` | FR-IX-01 — *"**Tác nhân:** CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* |
| `:1052` | SCR-IX-01 item 8 — *"Nút Xuất Excel · button · 'Xuất Excel (.xlsx)' → xuất theo format TT17/2025 · **click → auto-download** · Điều kiện hiển thị: Sau khi đã 'Xem báo cáo'"* |
| `:1058` | SCR-IX-01 item 14 — *"Toast xuất file · 'Đang tạo file…' → 'Xuất thành công' + auto-download · Khi nhấn xuất"* |
| `:1092` | *"Export XLSX/PDF **chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file**… Tên tệp cả hai định dạng theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"* |
| `:1280` | BR-DATA-06 — *"Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |

**Rẽ nhánh (quyết TRƯỚC khi viết mục 4):** đặc tả **nói rõ** và **khớp** kỳ vọng đối tác — `:1052` ghi thẳng
*click → auto-download*, `:123` ghi *tải file .xlsx*; đối tác mong *"xuất toàn bộ và tự động tải tệp về máy"*.
⇒ **Không** thuộc nhánh cần BA. Viết mục 4 + 5 rồi sang giai đoạn B.

**IM LẶNG về:**
- Chữ chính xác của thông báo **thành công** khi xuất được (`:1058` ghi *"Xuất thành công"* trong bảng thành
  phần màn hình, nhưng không có mã INF/WRN tương ứng ở bảng Error Handling) ⇒ **không** chấm Fail vì chữ thông
  báo thành công khác.
- Thứ tự / tên sheet, tên cột bên trong tệp .xlsx — đặc tả chỉ quy định **header file** phải có tiêu đề BC +
  kỳ + đơn vị + ngày tạo (`:1092`), không quy định bố cục chi tiết.
- Có bắt buộc hiện toast *"Đang tạo file…"* hay không (bảng thành phần màn hình mô tả, nhưng Error Handling
  không có mã) ⇒ thiếu toast loading **không** phải Fail.

---

## 3. Precondition

- **Tài khoản ra verdict:** `cbnv_tw_05` / `Test@1234` — **CB Nghiệp vụ - Trung ương** (`CB_NV_TW`), cấp **TW**,
  phạm vi dữ liệu **Toàn quốc**. Đây đúng **tác nhân đặc tả** của FR-IX-01 (`:140`).
  Fallback (Rule 7, cùng vai trò + cùng cấp): `cbnv_tw_04` → `_03` → `_02` → `_01`. Có fallback thì khai rõ.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` — menu **Báo cáo thống kê**.
- **Dữ liệu tiền đề:** ≥1 hỏi đáp/vướng mắc **đã duyệt** trong kỳ đo (đặc tả Processing chung bước 4 `:82`:
  *"CHỈ bản ghi đã duyệt"*). Nếu kỳ rỗng → đó là `INF-RPT-01` hợp lệ (`:113`), phải đổi kỳ/đơn vị để có dữ liệu
  rồi mới đo nút xuất.
- **Bộ lọc neo theo đối tác:** Loại BC = *BC Số lượng hỏi đáp/vướng mắc pháp luật* · Kỳ = **Năm** ·
  01/01/2026 → 31/12/2026 · Đơn vị = **Toàn quốc**.
- **Bộ bắt thông báo** `output/UAT_doi-tac/tools/toast-capture.js` cài **TRƯỚC** mỗi lần bấm; chỉ tin số liệu
  khi `soObserverDangSong = 1`; đếm thông báo theo **mốc giờ khác nhau**, không theo số phần tử.

---

## 4. Tiêu chí chấm

### ✅ PASS khi — **đủ cả 6 điều, trên đủ M = 3 dạng ở mục 5**

1. **Không bị chặn, không báo lỗi tạo tệp.** Vai trò CB Nghiệp vụ TW, sau khi Xem báo cáo ra dữ liệu, thao tác
   Xuất Excel **không** sinh thông báo mang nghĩa *từ chối quyền* (nhánh `:117`) và **không** sinh thông báo
   mang nghĩa *không tạo được tệp* (nhánh `:116`). Đo bằng bộ bắt thông báo: đọc **nguyên văn** chữ trên màn,
   đối chiếu với 2 câu ở `:116` / `:117` và với 2 câu đối tác gặp (*"Không thể tạo file xuất. Vui lòng thử lại."*,
   *"Forbidden"*).
2. **Trình duyệt thật sự nhận được một tệp tải về** (`:1052` *click → auto-download*): quan sát được ở phía
   người dùng — tệp rơi về thư mục tải xuống, **hoặc** phản hồi của chính thao tác đó là một tệp đính kèm
   (`content-disposition: attachment`) chứ không phải trang lỗi / JSON lỗi.
3. **Tệp mở được như một workbook .xlsx thật** — `openpyxl.load_workbook()` chạy được, đọc ra ≥1 sheet có ô
   không rỗng. (Mã 200 + có bytes **không** đủ.)
4. **Header tệp có đủ 4 thông tin đặc tả đòi ở `:1092`**: tiêu đề báo cáo · thông tin kỳ (kỳ + khoảng thời
   gian) · đơn vị · ngày tạo. Đo bằng cách đọc các ô đầu sheet và tìm đủ 4 mẩu thông tin đó.
5. **Số liệu trong tệp khớp số liệu đang hiện trên màn.** So từng cặp, tối thiểu 4 chỉ số của FR-IX-01
   (`:161`–`:164`): Tổng hỏi đáp · Đã trả lời · Chờ trả lời · Tỷ lệ trả lời. Có bảng phân theo lĩnh vực /
   đơn vị trong tệp thì tổng các dòng phải cộng khớp Tổng hỏi đáp.
6. **Tệp phản ánh đúng bộ lọc hiện tại** (`:1280`): khi đặt bộ lọc đặc thù khác nhau (3 dạng ở mục 5), số liệu
   trong tệp **đổi theo** và mỗi lần đều khớp số trên màn của chính lần đó — không phải luôn trả bản không lọc.

### ❌ FAIL nếu — bất kỳ điều nào, ở bất kỳ dạng nào trong M

- Bất kỳ lượt nào trong M dạng sinh thông báo từ chối quyền hoặc thông báo không tạo được tệp (tức tái hiện
  vế a hoặc vế b).
- Bấm xuất mà **không** có tệp nào đến tay người dùng (không có tệp tải về **và** phản hồi không phải tệp đính kèm).
- Có "tệp" nhưng `openpyxl` **không** mở được (thực chất là JSON/HTML lỗi đổi đuôi).
- Tệp mở được nhưng **thiếu** ≥1 trong 4 thông tin header ở `:1092`.
- Số liệu trong tệp **lệch** số liệu trên màn ở bất kỳ chỉ số nào trong 4 chỉ số bắt buộc.
- Tệp **bỏ qua** bộ lọc hiện tại (2 dạng lọc khác nhau cho ra tệp có số liệu giống hệt nhau trong khi số trên
  màn khác nhau).
- Fix **một phần**: xuất được ở dạng này nhưng vẫn lỗi ở dạng khác trong M ⇒ vẫn FAIL (flow §Verdict: *fix một phần → Reopen*).

### KHÔNG được chấm Fail vì (đặc tả im lặng, hoặc ngoài vế đối tác nêu)

- **Tên tệp không khớp khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`.** Case này đối tác **không** nêu vế tên tệp
  ⇒ đây là **phát hiện ngoài phạm vi**, ghi riêng, báo phiên chính, **không kéo verdict** (flow §Ca biên:
  *"Verdict của case chỉ do các vế đối tác nêu quyết định"*).
- **Khổ giấy A4 / font Times New Roman cỡ 13 bên trong tệp** (`:85`, `:123`) — cũng ngoài vế đối tác nêu; đo thì
  ghi nhận, không chấm.
- **Kỳ/đơn vị không có dữ liệu** → `INF-RPT-01` (`:113`) là hành vi **hợp lệ**, không phải lỗi xuất tệp.
- **Chữ của thông báo thành công** khác *"Xuất thành công"*, hoặc **thiếu** toast *"Đang tạo file…"* — đặc tả
  im lặng ở bảng Error Handling.
- **Số liệu trên màn khác số liệu đối tác chụp** (8 / 60 hỏi đáp) — khác env, khác thời điểm, dữ liệu QA đã đổi.
- **Báo cáo trả số trông cũ** — phải kiểm trường *"Thời điểm tạo"* trước khi kết luận (cache phía máy chủ).

> **Phép thử mục 4:** người không biết gì về bug này, đọc riêng mục 4, vẫn chấm được PASS/FAIL — 6 điều đều
> đếm được / so được / nhìn thấy được, không có chữ "hiển thị đúng" hay "hợp lý".

---

## 5. Dạng dữ liệu phải phủ — **M = 3**

**Nguồn xác định M:** tra theo thứ tự của flow — ① đặc tả nói về nguồn dữ liệu: `:151` *"Đếm số hỏi đáp (đã trả
lời / chờ trả lời) trong kỳ, theo phạm vi đơn vị"*, `:82` *"CHỈ bản ghi đã duyệt"* → chỉ có **một** nguồn bản
ghi, chưa đủ chia dạng. ② **bộ lọc + giá trị enum ngay trên màn**: `:1050` (bộ lọc đặc thù) + `:148`–`:149`
(`linh_vuc_id` optional; `trang_thai_hd` ∈ {`DA_TRA_LOI`, `CHO_TRA_LOI`}) + `:1064` (bộ lọc đặc thù của UC124 =
Lĩnh vực PL, Trạng thái HĐ). **Dừng ở ②** — bộ lọc là chiều duy nhất đổi được nội dung tệp xuất, và `:1280`
buộc *"file xuất theo bộ lọc hiện tại"* nên mỗi nhánh lọc là một dạng phải đo.

| # | Tên dạng | Vì sao phải có |
|---|---|---|
| 1 | **Không lọc đặc thù** (Lĩnh vực PL trống + Trạng thái HĐ trống) | Đúng điều kiện **vòng 2** của đối tác (ảnh `_v2.jpg`) — nhánh sinh ra *"Forbidden"* |
| 2 | **Lọc Lĩnh vực PL** (= *Thuế*, hoặc lĩnh vực khác nếu *Thuế* không có dữ liệu — khai rõ) | Đúng điều kiện **vòng 1** của đối tác (video) — nhánh sinh ra *"Không thể tạo file xuất"* |
| 3 | **Lọc Trạng thái HĐ** (một trong `DA_TRA_LOI` / `CHO_TRA_LOI`) | Nhánh enum còn lại của bộ lọc đặc thù `:149`; cần để chứng minh `:1280` (*"theo bộ lọc hiện tại"*) chứ không phải luôn xuất bản đầy đủ |

Kỳ báo cáo giữ cố định **Năm 2026** cho cả 3 dạng để phép so số liệu giữa các dạng có nghĩa (đúng kỳ đối tác dùng).

---

## 6. Bảng điều kiện

> Cột **"Đối tác"** điền NGAY từ bằng chứng (2026-08-06 12:20). 2 cột sau điền ở **giai đoạn B**.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên · QTHT**, đơn vị **BTP · TW** (đọc từ góc phải trên màn ở cả video vòng 1 và ảnh vòng 2) | **Đo cả 2 nhánh vai trò khả dĩ.** ① **Ra verdict:** `cbnv_tw_05` — *CB Nghiệp vụ - Trung ương #05*, `CB_NV_TW`, cấp TW, `donViId 00000000-0000-4000-8000-000000000001`, phạm vi **Toàn quốc** = đúng **tác nhân đặc tả** của FR-IX-01 (`:140`); không phải fallback, dùng đúng tài khoản được giao. ② **Đối chứng (chỉ điều tra, không ra verdict):** `admin` — *Quản trị hệ thống*, `QTHT`, cấp TW = **trùng khít vai trò đối tác dùng**, để trả lời câu "vì sao đối tác gặp Forbidden" | **Không** |
| Entity + trạng thái | Báo cáo *BC Số lượng hỏi đáp/vướng mắc pháp luật* đã ở trạng thái **đã render có dữ liệu** (nút Xuất Excel đang bật). Vòng 1: Tổng 8 / ĐTL 3 / CTL 5 / 37,5 %, *Thời điểm tạo 15/07/2026 16:22*. Vòng 2: Tổng 60 / ĐTL 20 / CTL 40 / 33,3 %, *Thời điểm tạo 31/07/2026 14:03* | Cùng trạng thái: báo cáo **đã render có dữ liệu**, nút Xuất Excel **bật** ở cả 2 vai trò. Dạng 1: Tổng 22 / 11 / 11 / 50,0 % (*tạo 06/08/2026 12:25*) · dạng 2: 8 / 6 / 2 / 75,0 % (*12:28*) · dạng 3: 11 / 11 / 0 / 100,0 % (*12:30*) · nhánh QTHT: 22 / 11 / 11 / 50,0 % (*12:37*). Mọi lượt đều kiểm trường *Thời điểm tạo* để loại trừ cache máy chủ | **Không** |
| Dữ liệu tiền đề | Có hỏi đáp đã duyệt trong kỳ Năm 2026, phạm vi Toàn quốc (đủ để báo cáo ra số > 0) | Có sẵn, **không cần seed**: 22 hỏi đáp đã duyệt trong kỳ Năm 2026 phạm vi Toàn quốc, trải **3 lĩnh vực** (Thương mại 13 · Thuế 8 · Lao động 1) và **2 đơn vị** (Cục Bổ trợ tư pháp 21 · Sở Tư pháp Hà Nội 1), có cả 2 trạng thái (11 đã trả lời / 11 chờ) ⇒ đủ để dựng cả 3 dạng ở mục 5 | **Không** |
| Input / filter / giá trị nhập | Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**. Vòng 1: **Lĩnh vực PL = Thuế**, Trạng thái HĐ trống. Vòng 2: **cả 2 bộ lọc đặc thù trống**. Thao tác: [Xem báo cáo] → [**Xuất Excel**] | Trùng khít: kỳ **Năm** 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, thao tác [Xem báo cáo] → [**Xuất Excel**] bằng chuột thật trên giao diện. Phủ **cả 2 bộ lọc đối tác dùng**: dạng 2 = **Lĩnh vực PL Thuế** (URL sinh ra `…&fd_linhVucId=bbbbbbbb-0000-4000-8000-000000000018` — **trùng đúng URL vòng 1** của đối tác) · dạng 1 = **không lọc** (URL trùng đúng vòng 2). Thêm dạng 3 = Trạng thái HĐ *Đã trả lời* | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 lượt xuất mỗi vòng (2 lượt tổng). M = 2 dạng lọc (có lọc lĩnh vực / không lọc). Không thấy đối tác thử lọc theo Trạng thái HĐ | **N = 5 lượt xuất** (3 lượt giao diện vai trò CB Nghiệp vụ + 1 lượt curl đường thứ hai + 1 lượt giao diện vai trò QTHT), **phủ đủ M = 3 dạng** ở mục 5. Mỗi tệp đều **mở bằng `openpyxl` đọc nội dung**; 3 tệp có **md5 khác nhau** ⇒ chứng minh tệp bám bộ lọc. Nhánh QTHT còn quét thêm **3 loại BC × 2 định dạng = 6 tổ hợp**, tất cả 403 | **Không** |

**3 dữ kiện neo của đối tác:**
- **URL/ID bản ghi:** vòng 1 — `htpldn-uat.ospgroup.vn/bao-cao?loai=hoi-dap&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&fd_linhVucId=bbbbbbbb-0000-4000-8000-000000000018`;
  vòng 2 — `htpldn-uat.ospgroup.vn/bao-cao?loai=hoi-dap&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` (không có `fd_linhVucId`).
- **Trạng thái entity:** báo cáo đã chạy xong, có dữ liệu; *Thời điểm tạo* 15/07/2026 16:22 (vòng 1) · 31/07/2026 14:03 (vòng 2).
- **Vai trò + env + bản dựng:** Quản trị viên QTHT (BTP · TW) · `htpldn-uat.ospgroup.vn` · nhãn **HTPLDN V1.0**
  (vòng 1, 15/07/2026) và **HTPLDN V1.0.2** (vòng 2, 31/07/2026).

**Giới hạn hiệu lực (không phải GAP):** mình đo trên `18.143.165.120.nip.io` — **env kiểm thử nội bộ**, khác
env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác, và bản dựng cũng mới hơn. ⇒ Mọi kết luận Pass chỉ là
**Pass tạm**, chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu.

---

## 7. Kết quả chấm (điền 2026-08-06 12:41)

| Vế đối tác nêu | Kết quả đo | Kết luận |
|---|---|---|
| **a** — *"Không thể tạo file xuất. Vui lòng thử lại."* (ERR-RPT-04, `:116`) | Vai trò CB Nghiệp vụ TW: **3/3 dạng xuất được**, 1 request ↔ 1 thông báo *"Đang tạo file..."*, HTTP 200, tệp .xlsx thật, mở bằng `openpyxl` đủ 4 mục header (`:1092`) và số liệu khớp màn từng con số. Vai trò QTHT: trả *"Forbidden"*, **không phải** câu ERR-RPT-04 | **HẾT LỖI** |
| **b** — *"Forbidden"* | Vai trò **QTHT — đúng vai trò đối tác dùng**: `POST /api/v1/bao-cao/export` → **HTTP 403** `ERR-PERM-SYS-00-01`, chữ trên màn đúng một chữ **"Forbidden"** (hiện 102 ms sau khi bấm, sống ~3,3 giây, x=8 y=16 w=1416 h=40, opacity 1). Đã chụp được ảnh. Quét rộng: QTHT **xem được** mọi báo cáo (200) nhưng **xuất 403 ở 3/3 loại BC × 2/2 định dạng** | **CÒN LỖI — TÁI HIỆN** |

**Verdict: REOPEN.** Theo flow §Ca biên (*case gộp nhiều vế: còn ≥1 vế lỗi → Reopen*).

**Vì sao KHÔNG chấm *"không phải lỗi"* dù `:140` chỉ liệt kê tác nhân là CB Nghiệp vụ / CB Phê duyệt:**
verdict đó đòi chứng minh **đối tác thao tác sai**, mà ở đây chính phần mềm đã (1) cho vai trò QTHT vào
màn báo cáo, (2) cho chạy báo cáo ra dữ liệu (HTTP 200), (3) **hiện nút [Xuất Excel] ở trạng thái bấm được**
— `:1052` ghi điều kiện hiển thị của nút là *"Sau khi đã 'Xem báo cáo'"*, **không kèm điều kiện vai trò**.
Người dùng bấm một nút mà phần mềm đang mời bấm thì không thể gọi là thao tác sai. Thêm nữa, dù sau này
BA chốt QTHT **không** được xuất, hành vi hiện tại vẫn lệch `:117` (từ chối vì thiếu quyền phải báo bằng
thông báo tiếng Việt đã định, không phải chữ *"Forbidden"* nguyên tiếng Anh).

**Vì sao KHÔNG chấm *"cần BA"*:** vế b có căn cứ đặc tả rõ ở `:117` (+ `:1052`) nên chấm được ngay.
Riêng câu hỏi *"QTHT rốt cuộc CÓ hay KHÔNG được xuất báo cáo"* là điểm đặc tả tự mâu thuẫn (`:140` vs `:1052`)
⇒ thuộc diện gửi BA để dev biết sửa theo hướng nào; mục đó **không** kéo verdict của case.
**Đã có sẵn** ở [`cau-hoi-BA.md`](../cau-hoi-BA.md) § *Mục 2 — Vai trò QTHT có được XUẤT báo cáo thống kê
không?* (do lượt verify `SLCTHT_06` mở lúc 12:40, cùng nguyên nhân gốc, nêu đúng câu hỏi này) ⇒ **không mở
mục trùng**, chỉ trỏ tới; phiếu `BUG-SLHDVM-006` đã dẫn chiếu mục đó.

**Giới hạn hiệu lực:** đo trên env kiểm thử nội bộ `18.143.165.120.nip.io`, bản dựng V1.0.8
(md5 bó mã `e0e4f737b1fb7ab9409f459a4d0fa051`) — khác env nghiệm thu `htpldn-uat.ospgroup.vn` của đối tác.

**Đối chiếu kết luận cũ của tổ QA:** hồ sơ `reverify-week-4/DANH-SACH-53-BUG-REOPEN-KET-QUA-QA.md` từng xếp
cụm 44 lỗi *"Forbidden"* màn Báo cáo thống kê là **"không phải bug code — env-drift, OSP chạy bản cũ"**.
Lượt đo này **bác kết luận đó**: nguyên nhân là **phân quyền theo vai trò** (QTHT bị chặn ở endpoint xuất),
tái hiện 100 % ngay trên bản dựng mới nhất. Vòng verify cũ không tái hiện được vì chỉ đo bằng vai trò
CB Nghiệp vụ — đúng vai trò được phép — chứ không đo bằng vai trò đối tác thật sự dùng.

---

## 8. Nhật ký sửa đổi tiêu chí

- **2026-08-06 12:56** — Chỉ sửa **câu chữ ở mục 7** cho khớp hồ sơ thật: câu hỏi gửi BA **không** mở mục mới
  mà trỏ vào mục đã có sẵn trong `cau-hoi-BA.md` (§ Mục 2, do lượt verify `SLCTHT_06` mở lúc 12:40 — cùng
  nguyên nhân gốc). **Không** đụng mục 4, 5, 6 và **không** đổi verdict.
- **2026-08-06 12:41** — Không sửa mục 4 và mục 5; hai mục này giữ **nguyên văn như lúc viết trước khi mở màn**.
  Chỉ điền thêm cột *"Mình test lần này"* + cột *GAP?* ở mục 6, điền **Bản dựng** ở đầu file, và thêm mục 7
  (kết quả chấm) + mục 8 này.
- **2026-08-06 12:35 — bổ sung phương pháp đo, không đổi tiêu chí:** phát hiện bộ bắt thông báo dùng chung
  (nghe *node mới được thêm*) **bỏ sót** chữ *"Forbidden"* vì thư viện giao diện thay chữ **trong node cũ**.
  Đã đo bù bằng cách theo dõi **nội dung** vùng thông báo theo thời gian (`innerText`) và ghi lại hình học để
  chứng minh người dùng nhìn thấy thật. Ghi lại ở đây vì nếu chỉ tin bộ đo cũ thì sẽ kết luận sai là
  *"bấm xuất không hiện thông báo nào"*.
