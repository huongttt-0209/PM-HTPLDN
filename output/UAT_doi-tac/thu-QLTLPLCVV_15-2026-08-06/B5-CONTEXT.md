# B5 — Bối cảnh dùng chung cho 6 case (đọc TRƯỚC khi chạy)

> File này do phiên chính lập 2026-08-06 12:15. Mỗi agent con đọc file này + `flows/04-verify-bug-dev-fix-khong-ho-so.md`
> rồi chạy ĐÚNG 1 case được giao. **Không** chạy case của người khác, **không** suy kết quả case này sang case kia.

---

## 1. Nguồn + phạm vi

- Bảng: `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** (gid 1714340219) · ô mã case = cột `Mã TC`.
- 6 case B5, **6 màn báo cáo khác nhau**, cùng một câu triệu chứng:

| row | Mã TC | Màn (loại báo cáo) | FR | Kết quả mong đợi của đối tác có đòi tên tệp? |
|---|---|---|---|---|
| 174 | SLHDVM_06 | BC Số lượng hỏi đáp/vướng mắc pháp luật | FR-IX-01 (`srs-fr-11-bao-cao.md:129`) | **Không** — chỉ "xuất toàn bộ + tự tải về máy" |
| 200 | CLDTBDDDR_06 | BC Lớp đào tạo đang diễn ra | FR-IX-06 (`:346`) | Có — `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx` hoặc `.pdf` |
| 205 | LDTBDDDR_06 | BC Lớp đào tạo đã diễn ra | FR-IX-07 (`:389`) | Có — `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx` hoặc `.pdf` |
| 210 | CGTVPL_06 | BC Số lượng CG/TVV | FR-IX-08 (`:429`) | Có — `BaoCaoDanhGia_{YYYYMMDD_HHmm}.xlsx / .pdf` |
| 214 | DGHQHTPL_06 | BC Đánh giá hiệu quả HTPL | FR-IX-09 (`:474`) | Có — `BaoCaoDanhGia_{YYYYMMDD_HHmm}.xlsx / .pdf` |
| 218 | CLDTBDPL_06 | BC Chất lượng đào tạo | FR-IX-10 (`:515`) | Có — `BaoCaoDaoTao_{YYYYMMDD_HHmm}.xlsx` |

- Triệu chứng gốc (`Kết quả thực tế`, cả 6 dòng): *Hệ thống hiển thị thông báo "Không thể tạo file xuất. Vui lòng thử lại."*
- `TKM phản hồi lần 1` (cả 6 dòng, retest 31/07/2026): *Hệ thống hiển thị thông báo "Forbidden"* + ảnh `<Mã TC>_v2.jpg`.
- `DEV phản hồi lần 1` (cả 6 dòng): *"Đã kiểm tra trên môi trường DEV nhưng chưa tái hiện được lỗi..."* → **đừng tin mô tả, chạy đủ luồng**.
- Trạng thái hiện tại của cả 6 dòng: `Trạng thái` = `Fail` · `Dopai` = `dev done` · `Trạng thái dev fix` = `Fixed` · `Kết quả verify` = **rỗng**.

## 2. Bằng chứng đối tác — đã tải sẵn

Thư mục: `output/UAT_doi-tac/thu-QLTLPLCVV_15-2026-08-06/partner-evidence/`

| Mã TC | Vòng 1 (cột `Ảnh/vieo 1`) | Vòng 2 (cột `TKM phản hồi lần 1`) |
|---|---|---|
| SLHDVM_06 | `SLHDVM_06.webm` (video 3.2MB → trích frame tới khoảnh khắc lỗi) | `SLHDVM_06_v2.jpg` |
| CLDTBDDDR_06 | `CLDTBDDDR_06.jpg` | `CLDTBDDDR_06_v2.jpg` |
| LDTBDDDR_06 | ⚠️ **ô M205 trỏ ĐÚNG CÙNG file Drive với row 200** (`CLDTBDDDR_06.jpg`, id `1b-8svUeew_…`) | `LDTBDDDR_06_v2.jpg` |
| CGTVPL_06 | `CGTVPL_06.jpg` | `CGTVPL_06_v2.jpg` |
| DGHQHTPL_06 | `DGHQHTPL_06.jpg` | `DGHQHTPL_06_v2.jpg` |
| CLDTBDPL_06 | `CLDTBDPL_06.jpg` | `CLDTBDPL_06_v2.jpg` |

🔴 **LDTBDDDR_06:** mở ảnh vòng 1 ra đọc; nếu nội dung là màn "Lớp đào tạo **đang** diễn ra" thì đó là bằng chứng của
case khác → ghi trong mục 1 file tiêu chí là "vòng 1 không có bằng chứng riêng", dùng ảnh vòng 2 `LDTBDDDR_06_v2.jpg`
làm bằng chứng của case này. **Không** vì thế mà bỏ case.

Trích frame video: `python3 output/UAT_doi-tac/tools/extract_frames.py` (xem `--help`); đích `.../thu-QLTLPLCVV_15-2026-08-06/frames/<Mã TC>/`.

## 3. Môi trường + tài khoản

- **MÔI TRƯỜNG VERIFY (bắt buộc): `https://18.143.165.120.nip.io`** — env kiểm thử NỘI BỘ, không phải env nghiệm thu
  của đối tác (`htpldn-uat.ospgroup.vn`). ⇒ Mọi verdict Pass là **Pass tạm**, phải ghi rõ câu
  *"chưa có hiệu lực cho tới khi bản dựng này lên môi trường nghiệm thu"* trong note.
- **Dấu vân tay bản dựng** (phiên chính đo 2026-08-06 12:10): bó mã `assets/index-CNwX9JjX.js` ·
  `last-modified: Thu, 06 Aug 2026 02:51:16 GMT` · `etag: "6a73f6a4-428"` · nhãn hiển thị trong app: **V1.0.8**.
  Agent **tự đo lại** và ghi vào mục "Bản dựng" của file tiêu chí (đừng chép mù — bản dựng có thể đổi giữa đợt).
- **Tài khoản — dùng BỘ 05** (user chỉ định; các phiên khác đang chạy batch B1–B4 song song trên cùng env với bộ 01–04):
  - Chính: **`cbnv_tw_05`** / `Test@1234` (CB Nghiệp vụ Trung ương — phạm vi Toàn quốc; đã kiểm chứng bước 1 đăng nhập
    trả `otpToken` OK lúc 12:12).
  - Fallback đúng Rule 7 **cùng vai trò + cùng cấp**: `cbnv_tw_04` → `_03` → `_02` → `_01`. **Cấm** đổi sang cấp BN/ĐP
    hay vai trò khác (đổi cấp = đổi phạm vi dữ liệu = phép đo vô nghĩa). Có fallback thì **khai trong báo cáo**.
  - OTP: MailHog `http://18.143.165.120:8025` (API `/api/v2/messages?limit=5`). Đăng nhập API:
    `POST /api/v1/auth/login {username, password}` → `POST /api/v1/auth/verify-otp {otpToken, otpCode}`.
    ⚠️ Trường JSON là `username`/`password`, **không** phải `tenDangNhap`/`matKhau`.
  - Giới hạn đăng nhập 5 lượt/60s — sai mật khẩu nhiều lần sẽ bị chặn.
- Công cụ browse: **Chrome DevTools MCP** (`mcp__chrome-devtools__*`). Bộ bắt thông báo dùng chung:
  `output/UAT_doi-tac/tools/toast-capture.js` — cài **TRƯỚC** khi bấm, không lọc trùng, đọc `innerText`,
  đếm theo **mốc giờ khác nhau** chứ không theo số phần tử.

## 4. Đặc tả — BA ĐÃ CHỐT 2026-08-04, KHÔNG hỏi lại BA về tên tệp

Bản chuẩn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`.
**Mở file đọc lại đúng dòng trước khi quote** — số dòng dưới đây phiên chính đã mở kiểm 2026-08-06, nhưng vẫn phải tự xác nhận.

| Dòng | Nguyên văn (rút gọn) |
|---|---|
| `:85` | Bước 7 Processing chung — *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp `[BA chốt 2026-08-04]`"* |
| `:86` | Bước 8 — quy định PDF + *"`{TenBaoCao}` là tên loại báo cáo viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ/số"* `[BA chốt 2026-08-04]` |
| `:112` | E6 — *"Lỗi xuất file · ERR-RPT-04 · 'Không thể tạo file xuất. Vui lòng thử lại'"* ⇒ đúng câu đối tác gặp |
| `:113` | E7 — *"Không có quyền · ERR-RPT-05 · 'Bạn không có quyền xem báo cáo này'"* ⇒ liên quan triệu chứng "Forbidden" vòng 2 |
| `:123` | Tiêu chí chấp nhận — *"nhấn 'Xuất Excel' → tải file .xlsx khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"* |
| `:1052` | SCR — nút *"Xuất Excel (.xlsx)"*, điều kiện hiển thị *"Sau khi đã 'Xem báo cáo'"*, hành vi *click → auto-download* |
| `:1092` | *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file … Tên tệp cả hai định dạng theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}`"* `[BA chốt 2026-08-04]` |
| `:1280` | BR-DATA-06 — *"File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file"*, áp *"Toàn bộ FR-IX"* |

🔴 **Vì sao đây KHÔNG còn là ca cần BA:** vòng verify 03/08/2026 đã gửi BA câu hỏi *"nhóm IX có quy ước tên tệp không"*
(hồ sơ: `output/UAT_doi-tac/reverify-week-4/reverify-round-2026-08-03/GUI-BA-2026-08-03/ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md`).
**BA đã chốt ngày 2026-08-04** và đặc tả đã được sửa theo — dấu `[BA chốt 2026-08-04]` nằm ngay trong 3 dòng `:85` `:86` `:1092`.
⇒ Đây là **áp quyết định có sẵn**, QA chấm được, **cấm** đẩy vế tên tệp sang file hỏi BA lần nữa.
(`tasks/srs-contradictions.md` §SRS-C-010 vẫn ghi "Open" — đó là **tracker chưa cập nhật**, không phải chưa có quyết định.
Phiên chính đã ghi nhận; agent con **không** sửa file tracker đó.)

**Số đo cũ (03/08/2026, build V1.0.4, env đối tác) — CHỈ để biết, CẤM lấy làm ngưỡng:** tệp xuất khi đó tên
`bao-cao-<slug>-YYYY-MM-DD.xlsx` (vd `bao-cao-lop-dao-tao-dang-dien-ra-2026-08-03.xlsx`) — thiếu hẳn giờ-phút.
Mục 4 file tiêu chí phải suy từ đặc tả ở trên, không được suy từ số đo này. Có đọc thì **khai trong file tiêu chí**.

## 5. Bar Pass của nhóm này (đừng hạ thấp)

1. **Chạy luồng thật trên giao diện**: menu **Báo cáo thống kê** → chọn đúng loại báo cáo của case → nhập kỳ +
   khoảng thời gian + đơn vị → **[Xem báo cáo]** → **[Xuất Excel]**. Không kết luận chỉ từ API.
2. **Mở tệp .xlsx ra đọc nội dung** — `openpyxl`. Mã 200 + có bytes chỉ chứng minh *sinh ra* tệp.
   Phải đo: ① số liệu trong tệp khớp số liệu đang hiện trên màn ② header tệp có tiêu đề BC + kỳ + đơn vị + ngày tạo
   (`:1092`) ③ **tên tệp** đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`:85`, `:123`).
3. Chrome của MCP chạy `--isolated` **có thể không đổ tệp về `~/Downloads`**. Hai đường dự phòng, dùng đường nào cũng phải
   ghi rõ: (a) kiểm `~/Downloads` trước/sau khi bấm; (b) giải nén zip xlsx **ngay trong trang** bằng `evaluate_script`
   (parse EOCD + `DecompressionStream`, chỉ trả về thứ cần đo — đừng dump base64 cả tệp).
   **Tên tệp** phải lấy từ nguồn người dùng thật thấy: tên file rơi về máy, hoặc `content-disposition` của phản hồi.
4. **Báo cáo thống kê có cache phía máy chủ** — nếu số liệu trông cũ, kiểm trường "Thời điểm tạo"/`ngayTaoBc` và đổi
   `denNgay` 1 ngày để lấy khoá cache mới. Đừng chấm Fail oan vì cache.
5. **Đo bằng đường thứ hai**: gọi thẳng endpoint xuất với cùng tham số, so mã HTTP + `content-disposition` + kích thước.
   Hai đường mâu thuẫn ⇒ **chưa chốt được**, ghi cả hai + hỏi user.
6. Triệu chứng vòng 2 là **"Forbidden"** ⇒ phải khẳng định được nút xuất chạy được **với đúng vai trò CB nghiệp vụ**,
   không phải chỉ chạy được với quản trị. Tài khoản quản trị chỉ dùng để dựng dữ liệu, **không ra verdict**.
7. **Không có dữ liệu trong kỳ** → đó là `INF-RPT-01` hợp lệ, **không phải** lỗi xuất tệp. Đổi kỳ/đơn vị để có dữ liệu
   rồi mới đo nút xuất. Nếu mọi kỳ đều rỗng → GAP chưa đóng → verdict **ô trống**, nêu rõ cần seed gì.

## 6. Nơi lưu hồ sơ (user chỉ định — dùng đúng, không tự đổi)

| Loại | Đường dẫn |
|---|---|
| File tiêu chí | `output/UAT_doi-tac/thu-QLTLPLCVV_15-2026-08-06/tieuchi/<Mã TC>.md` |
| Bug report | `output/UAT_doi-tac/thu-QLTLPLCVV_15-2026-08-06/bug-report.md` (**append**, xem §7) |
| Ảnh | `output/UAT_doi-tac/thu-QLTLPLCVV_15-2026-08-06/image/` — đặt tên `<Mã TC>-<thứ tự>-<mô tả>-V108.png` |
| File gửi BA | `output/UAT_doi-tac/thu-QLTLPLCVV_15-2026-08-06/cau-hoi-BA.md` (**append**) |
| Mẫu bug | `output/template/bug-report-template.md` · Mẫu BA: `output/template/ba-confirmation-needed-template.md` |

⚠️ **Thư mục này đang có sẵn hồ sơ của case `QLTLPLCVV_15`** (bug report 1 case, đã Pass) và **các phiên khác cũng đang
đổ `partner-evidence/` vào đây**. Khi sửa `bug-report.md` / `cau-hoi-BA.md`: **đọc lại file ngay trước khi ghi**,
chỉ **thêm** mục mới ở cuối, **không** xoá/sửa nội dung của case khác. Nếu file đã đổi so với lúc đọc → đọc lại rồi ghi tiếp.

## 7. Quy ước ghi `bug-report.md` (file dùng chung nhiều case)

- Mỗi case = **1 mục mới ở cuối file**, tiêu đề `## BUG-<MÃ TC không dấu>-… — <tiêu đề>` hoặc mục ghi nhận Pass.
- Bảng **Severity breakdown** + **Bug Summary Table** ở đầu file: **cập nhật đồng thời** với mục mới (cộng thêm dòng,
  cộng thêm số). Trường **Ngày** ở header: bump lên mốc giờ của lần đo mới nhất.
- Cả 3 việc trên làm **nguyên tử trong 1 lần ghi** (một lần Bash/Python hoặc một chuỗi Edit liền mạch) — sửa lệch
  giữa bảng và entry là hồ sơ mâu thuẫn.
- **Chỉ verdict Reopen mới có khối `── CÁCH VERIFY sau Dev fix ──`**. Pass / cần BA / ô trống → không viết khối này.
- Ảnh gắn bằng đường dẫn tương đối `image/<tên>.png`, **không** base64. Mỗi ảnh 1 dòng chú thích *tên file + thấy gì*.

## 8. Ghi bảng — công cụ bắt buộc

```bash
cd "output/UAT_doi-tac"
python3 tools/sheet_bug_verify_write.py \
  --row <N> --ma-tc <MÃ TC> --verdict <pass|reopen|ba|trong> \
  --ketqua-file <file .txt chứa note> \
  --evidence <artifact QUAN SÁT của chính lượt đo này> \
  --tieuchi thu-QLTLPLCVV_15-2026-08-06/tieuchi/<Mã TC>.md \
  --dry-run          # chạy thử trước, xem CŨ→MỚI, rồi bỏ --dry-run để ghi thật
```

- Ánh xạ verdict (do prompt user quy định, **cấm tự chế giá trị**):
  `pass` → `Trạng thái dev fix` = `Test done` · `reopen` → `Trạng thái dev fix` = `Reopen` · `ba` → `Dopai` = `BA`
  · mọi verdict đều ghi cột `Kết quả verify` (diễn giải).
- **Ô CHỈ ĐỌC, cấm ghi đè:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.
- Dropdown thật đã kiểm 2026-08-06 12:05: `Trạng thái dev fix` = `[In Progress, Fixed, UAT done, Bug, Test done, reject, Reopen]`
  · `Dopai` = `[InProcess, Resoved, dev done, OSP, Bỏ qua, Open, bug, BA]` ⇒ 3 giá trị cần ghi đều hợp lệ.
- `--evidence` **không được** là file trong `partner-evidence/` (script chặn tên chứa `partner`) — phải là artifact
  của chính lượt đo này (ảnh mình chụp / tệp .xlsx tải về / file .txt chứa nguyên văn thông báo + phản hồi máy chủ).
- Ghi xong: script tự đọc lại. **Dán lại dòng đọc-lại** vào phần báo cáo cho phiên chính.
- Script chặn → **DỪNG, báo phiên chính**. Cấm ghi tay, cấm viết script dùng-một-lần để lách.

## 9. Bug ngoài phạm vi

Gặp lệch ngoài vế đối tác nêu → **không** kéo verdict của case. Qua đủ 4 cửa (đặc tả có đòi? đã có phiếu chưa?
đo lại đường thứ hai? hoàn nguyên dữ liệu?) rồi mới mở dòng mới trên bảng, theo quy tắc mã `<tiền tố module>_QA<số>`
và bộ ô: `Mã TC` · `Tên chức năng` · `Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` · `Kết quả thực tế` ·
`Trạng thái`=`Fail` · `Dopai`=`bug` · `Ảnh/vieo 1`=link xem được. Công cụ: `tools/sheet_add_bug_row.py`.
**Chưa mở dòng mới thì báo phiên chính trước** — phiên chính quyết, tránh 6 agent cùng mở trùng một lỗi gốc.

## 10. Báo về phiên chính (kết thúc agent)

Trả về đúng các mục: ① verdict + 1 câu lý do · ② đường dẫn file tiêu chí · ③ đường dẫn ảnh đã chụp (kèm chú thích)
· ④ nguyên văn dòng đọc-lại của công cụ ghi bảng · ⑤ dữ liệu đã seed/thay đổi trên env (nếu có) · ⑥ điều gì chưa đo được.
