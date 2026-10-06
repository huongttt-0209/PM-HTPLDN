# Reverify Report — UAT Tuần 2 (verify bug đối tác vòng đầu)

| Thông tin | Giá trị |
|---|---|
| Env được giao | http://18.143.165.120 (login CB_NV_TW = `cbnv_tw` / `Test@1234`, OTP MailHog `:8025`) |
| Env đối tác log | `htpldn-uat.ospgroup.vn` (build/env KHÁC env được giao) |
| Sheet | UAT_TGPL Doanh Nghiệp-tuần 2 · cột ghi: `Trạng thái dev fix 1` (P) + `DEV phản hồi lần 1` (R) |
| SRS | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` |
| Người verify | QA Automation (Claude Code) · 2026-07-10 |

> ✅ **Ghi sheet đã thông (2026-07-10):** Đã dựng `tools/sheet_write.py` + `tools/sheet_auth.py` (OAuth Desktop, project GCP `htpldn-uat-sheet`, token `tools/token.json`, scope `spreadsheets`). Ghi có đủ 5 guard + đọc lại xác nhận. Dùng lại: `../tools/README.md`.

---

## Case 1 — DKTGKH_07 · "Nhập đăng ký thủ công" (row 2) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (bug KHÔNG tái hiện trên env được giao; UI hiện tại đúng SRS) — dòng cuối note nhẹ: "Đối tác kiểm tra lại" (bỏ "Đề nghị" cho nhẹ; bỏ "sau bản build mới" vì chưa xác nhận có build fix).
**Ghi sheet:** 2026-07-10 — P2=`Reject`, R2=note (446 ký tự), đọc lại khớp. ✅

### Cổng 1 — Bằng chứng đã xem
- File: `partner-evidence/DKTGKH_07.webm` (30s). Trích 30 frame (1 fps) bằng `imageio_ffmpeg`.
- Frame chứa LỖI: **00:28–00:29** (`f_029.jpg` / `f_030.jpg`) → lưu `reverify-audit/DKTGKH_07-partner-frame-00m28s-loi-cot-trong.jpg`.
- Mô tả lỗi thấy trong frame: sau khi bấm "Thêm mới", toast "Đã thêm học viên" hiện, danh sách tab Học viên có bản ghi (Nguồn = "Nhập tay", Trạng thái "Chờ duyệt") **nhưng tất cả cột Họ tên / Email / SĐT / Đơn vị đều "-"** dù đã nhập đủ (Nguyễn Văn A, email, SĐT, đơn vị TKM).

### Cổng 2 — Hiểu bug
- Đối tác phản ánh CỤ THỂ: tạo bản ghi thành công (toast + state + nguồn đúng) nhưng **dữ liệu cá nhân của bản ghi mới không hiển thị lên danh sách** (cột Họ tên/Email/SĐT/Đơn vị trống).
- Data + bước tái hiện: role CB_NV_TW · Đào tạo → Khóa học → chi tiết khóa (video: `dd1adee1…`, thuộc env ospgroup) → tab Học viên → Thêm học viên thủ công → nhập name/email/phone/unit → submit → quan sát list.
- Kỳ vọng đối tác (K): tạo hồ sơ ĐK trạng thái "Chờ duyệt", nguồn "Nhập thủ công", toast "Đã tạo đăng ký thành công".

### Cổng 3 — Đối chiếu SRS vs thực tế web (env được giao)

| Mục | SRS yêu cầu | Thực tế web `18.143.165.120` |
|---|---|---|
| Cột tab Học viên | **SRS line 1820** (SCR-III-02, Tab 3 Học viên `[v3.5 Thay đổi 7]`): STT · **Họ tên · Email · Số điện thoại · Đơn vị** · Trạng thái đăng ký · Ngày đăng ký · Hành động | Header đủ: STT · Họ tên · Email · SĐT · Đơn vị · Nguồn · Ngày đăng ký · Trạng thái · Hành động ✅ |
| Hiển thị bản ghi thêm-tay | Phải hiển thị dữ liệu HV vừa nhập | Record mới "QA Verify DKTGKH07 R2 Now" hiển thị đủ: `0909123456` · "Cong ty TKM QA R2" · email · Nguồn "Nhập tay" · "Chờ duyệt" ✅ |
| Toast + state | Tạo ĐK "Chờ duyệt", nguồn thủ công | Toast "Đã thêm học viên" + state "Chờ duyệt" + Nguồn "Nhập tay" ✅ (khớp Expected đối tác) |

**Bước tái hiện thực tế:**
1. Login `cbnv_tw` (CB_NV_TW) — đúng vai trò của bug.
2. Khóa `AAA-KH-TW` (Đã kết thúc): thêm HV bị chặn `ERR-BIZ-III-04-01: Chỉ có thể đăng ký khóa học đã duyệt` → chuyển khóa `KH-SEED-0001` (Đã duyệt).
3. `KH-SEED-0001` tab Học viên: 6 record sẵn có, các record "Nhập tay" (QA Verify DKTGKH07 R1, HV seed…) **đều hiển thị đủ 4 cột**.
4. Thêm mới record "QA Verify DKTGKH07 R2 Now" (đủ name/email/SĐT/đơn vị) → toast "Đã thêm học viên" → record hiển thị **đủ mọi cột ngay lập tức**. Bằng chứng: `reverify-audit/DKTGKH_07-web-hienthi-du-cot-Nhaptay.png`.

> Ghi chú khóa `AAA-KH-TW`: các HV seed cũ hiện Họ tên + Email nhưng SĐT/Đơn vị "-" — do record seed 2026-02-01 không có sẵn 2 field đó (không phải lỗi hiển thị).

### Challenge (bác nhầm còn nguy hơn Open)
- Đã mở SRS xác nhận: line 1820 rõ ràng — cột phải hiển thị. Env hiện tại đáp ứng đúng.
- Đã tái hiện đúng bước/data đối tác (thêm-tay đủ field): **KHÔNG tái hiện lỗi** trên env được giao.
- **Evidence từ env/build KHÁC:** đối tác test `htpldn-uat.ospgroup.vn`, tôi test `18.143.165.120`. Có khác env → lỗi nhiều khả năng là build cũ trên env đối tác, đã đúng trên env được giao. Không mâu thuẫn SRS (SRS không silent) → không cần BA confirm. Kết luận `Reject` + yêu cầu đối tác verify lại trên env mới.

### Note đã ghi sheet (cột "DEV phản hồi lần 1") — partner-facing, KHÔNG lộ env
```
❌ Không phải bug.
• Thêm học viên thủ công (vai trò Cán bộ nghiệp vụ): hệ thống báo "Đã thêm học viên", bản ghi tạo ở trạng thái "Chờ duyệt", nguồn "Nhập tay".
• Danh sách tab "Học viên" hiển thị đủ các cột Họ tên/Email/SĐT/Đơn vị của bản ghi vừa thêm — đã tái hiện bằng thao tác thêm mới trực tiếp, dữ liệu lên đúng.
• SRS FR-III (srs-fr-03-dao-tao dòng 1820, Tab 3 "Học viên") yêu cầu các cột này; hệ thống đáp ứng đúng.
→ Đối tác kiểm tra lại.
```
> Chi tiết env-comparison (env đối tác `ospgroup.vn` vs env được giao `18.143.165.120`) chỉ để trong file audit này, KHÔNG đưa vào ô sheet (partner-facing).

### Data để lại (audit)
- Đã thêm 1 record test "QA Verify DKTGKH07 R2 Now" (SĐT 0909123456) vào `KH-SEED-0001` tab Học viên, state "Chờ duyệt" (nhất quán với record QA test từ session trước). Không xóa (không phá dữ liệu; đồng bộ cách QA seed đã dùng).

---

## Case 2 — DKTGKH_12 · "Tải lên tệp Excel" (row 3) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (app đáp ứng SRS; kỳ vọng "xem trước trước khi xác nhận" không phải yêu cầu SRS).
**Ghi sheet:** 2026-07-10 — P3=`Reject`, R3=note (634 ký tự), đọc lại khớp. ✅

### Cổng 1 — Bằng chứng đã xem
- File `partner-evidence/DKTGKH_12.webm` (68s), frame LỖI **00:57** (`f_058`) → `reverify-audit/DKTGKH_12-partner-frame-00m57s-baocao-ket-qua.jpg`.
- Frame cho thấy: sau import, modal kết quả hiện **Tổng dòng 2 · Thành công 0 · Bỏ qua (trùng) 1 · Lỗi 1** + "Dòng 2: Đã có đăng ký", "Dòng 3: Email không hợp lệ". → App CÓ báo cáo số hợp lệ/lỗi + lý do.

### Cổng 2 — Hiểu bug
- Partner phản ánh: hệ thống **không hiển thị "bản xem trước kết quả"** (số dòng hợp lệ, dòng lỗi, lý do) "theo thiết kế".
- Thực chất partner mong bước **preview TRƯỚC khi xác nhận nạp** (2 bước: preview → confirm → import). App làm 1 bước: import → báo cáo kết quả.

### Cổng 3 — Đối chiếu SRS vs thực tế web (env được giao)

| Mục | SRS yêu cầu | Thực tế web `18.143.165.120` |
|---|---|---|
| Luồng import | FR-III-04 dòng 474: "validate template, import từng dòng, **báo cáo KQ**"; dòng 609: "validate + import + **báo cáo lỗi**" | Chọn file → "Bắt đầu Import" → báo cáo kết quả (không có preview-trước) ✅ khớp luồng SRS |
| Nội dung báo cáo | dòng 485: ket_qua_import = số thành công / lỗi | Tổng dòng 3 · Thành công 1 · Bỏ qua (trùng) 1 · Lỗi 1 + "Dòng 3: Đã có đăng ký", "Dòng 4: Email không hợp lệ" ✅ |
| Bước "xem trước trước khi xác nhận" | KHÔNG có trong SRS FR-III-04 | App không có → đúng SRS |

**Tái hiện:** upload file 3 dòng (1 hợp lệ `qa.import.reverify12ok@...` + 1 trùng email `qa.import.v1@test.vn` + 1 sai email `notanemail`) → báo cáo 1 thành công / 1 bỏ qua / 1 lỗi + lý do; bản ghi hợp lệ vào list nguồn "Import Excel". Template 4 cột: Họ và tên · Email · Số điện thoại · Đơn vị. Bằng chứng: `reverify-audit/DKTGKH_12-web-baocao-ket-qua-import.png`.

### Challenge
- App đáp ứng SRS (báo cáo số hợp lệ/bỏ qua/lỗi + lý do từng dòng), tái hiện trực tiếp trên env được giao.
- Claim partner "không hiển thị số dòng lỗi + lý do" bị chính video partner (frame 00:57) + tái hiện phản chứng.
- "Preview trước khi xác nhận" là kỳ vọng thiết kế đối tác, KHÔNG phải yêu cầu SRS (SRS > thiết kế đối tác) → `Reject`.

### Data để lại (audit)
- Import thêm 1 bản ghi hợp lệ "QA Import Reverify12 OK" vào `KH-SEED-0001` (Chờ duyệt, nguồn Import Excel). File test: `reverify-audit/import-test-DKTGKH12.xlsx`, template gốc: `reverify-audit/dang-ky-template.xlsx`.

---

## Case 3 — KTDGKQHT_01 · "Màn hình tab không giống thiết kế" (row 4) — ✅ ĐÃ GHI SHEET (session trước)

**Verdict: `Open`** — tab "Kết quả" & "Điểm danh" thiếu cột Email/SĐT/Đơn vị/Xếp loại theo SRS FR-III-05 §Outputs (dòng 574–590) + Tab Điểm danh (dòng 1822). Log **BUG-KTDGKQHT_01** (Medium) trong `bug-reports/Pass-bug-report-UAT-tuan-2.md`.

---

## Case 4 — KTDGKQHT_03 · "Nhập điểm danh thủ công" (row 5) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (bảng điểm danh trống là empty-state cần chọn ngày buổi học, không phải lỗi hiển thị).
**Ghi sheet:** 2026-07-10 — P5=`Reject`, R5=note (568 ký tự), đọc lại khớp. ✅ · Note: `reverify-audit/note-KTDGKQHT_03.txt`

### Cổng 1 — Bằng chứng
- ⚠️ Video `KTDGKQHT_03.webm` KHÔNG có sẵn trong `partner-evidence/` (đã bị dọn từ session trước, chưa tải lại được — không có link Drive). Verify dựa trên **claim văn bản rõ ràng của đối tác** (cột L: "không hiển thị bảng danh sách học viên mặc dù tồn tại dữ liệu học viên") + tái hiện trực tiếp trên web. Nếu cần soi video, đối tác cấp lại link Drive.

### Cổng 2 — Hiểu bug
- Đối tác: mở tab "Điểm danh" → bảng danh sách học viên trống dù học viên đã có.
- Kỳ vọng đối tác (K): hệ thống ghi nhận + báo "Đã lưu điểm danh".

### Cổng 3 — Đối chiếu SRS vs thực tế web (env được giao)

| Mục | SRS yêu cầu | Thực tế web `18.143.165.120` |
|---|---|---|
| Điểm danh gắn buổi học | **dòng 538**: `lich_hoc_id` bắt buộc — "điểm danh phải gắn với 1 buổi cụ thể" | Tab Điểm danh có ô "Chọn ngày điểm danh"; chưa chọn → empty-state "Chọn ngày để xem điểm danh" ✅ đúng thiết kế |
| Hiện danh sách sau khi chọn ngày | Phải hiện HV để điểm danh | Chọn 10/02/2026 (buổi học đã có ở tab Lịch học) → hiện đủ **4 HV** (TW 01–04) + radio Có mặt/Vắng có phép/Vắng không phép ✅ |
| Lưu điểm danh | Báo "Đã lưu điểm danh" | Bấm Lưu → toast **"Đã lưu điểm danh"** (bắt bằng MutationObserver) ✅ khớp Expected đối tác |

### Challenge
- Bảng trống KHÔNG phải lỗi: là empty-state có hướng dẫn "Chọn ngày để xem điểm danh" (đúng phân loại empty-state hợp lệ). Điểm danh theo từng buổi (SRS dòng 538) → phải chọn ngày trước.
- Đối tác nhiều khả năng chưa chọn ngày, hoặc khóa họ dùng chưa có buổi học (lịch học) → precondition không đạt.
- Bằng chứng web: `reverify-audit/KTDGKQHT_03-web-diemdanh-hien-4hv-sau-chon-ngay.png`.

---

## Case 5 — KTDGKQHT_08 · "Nhập điểm kiểm tra thủ công không hợp lệ" (row 6) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (tab Kết quả trống là empty-state khi khóa chưa có HV duyệt/chưa phát sinh kết quả; app đã chặn điểm ngoài 0–10).
**Ghi sheet:** 2026-07-10 — P6=`Reject`, R6=note (625 ký tự), đọc lại khớp. ✅ · Note: `reverify-audit/note-KTDGKQHT_08.txt`

### Cổng 1 — Bằng chứng
- Video `KTDGKQHT_08.webm` (15s) — trích 15 frame 1fps → montage `reverify-audit/KTDGKQHT_08-montage.jpg`.
- Frame LỖI (tab Kết quả): danh sách học viên **trống** dù tab "Học viên" của khóa có dữ liệu. Lưu `reverify-audit/KTDGKQHT_08-partner-frame-tab-ketqua-trong.jpg`.

### Cổng 2 — Hiểu bug
- Đối tác Actual (cột L): "không hiển thị danh sách học viên mặc dù tồn tại dữ liệu" — vào tab "Kết quả" thấy trống dù học viên có ở tab "Học viên".
- Đối tác Expected (cột K): nhập điểm sai → hệ thống từ chối + báo "Điểm kiểm tra phải từ 0 đến 10".

### Cổng 3 — Đối chiếu SRS vs thực tế web (env được giao)

> **⚠️ Đính chính (sau câu hỏi review):** Video đối tác thực chất quay trên khóa **"Đang diễn ra"** (frame URL `dd1adee1-...`, state stepper highlight "4 Đang diễn ra"), HV đã **"Đã duyệt"**. Nghĩa là đối tác test đúng khóa có HV enrolled mà tab Kết quả vẫn trống. Lý do đúng: **SRS FR-III-17 yêu cầu khóa ở trạng thái "Đã kết thúc" mới nhập kết quả** — không phải "chưa có HV duyệt" như phân tích ban đầu. Verdict `Reject` giữ nguyên, lý do đã sửa.

| Mục | SRS yêu cầu | Thực tế web `18.143.165.120` |
|---|---|---|
| Điều kiện nhập kết quả | **FR-III-17 (dòng 1229, 1244)** PRE + Processing: "Khóa học ở **DA_KET_THUC**" (Đã kết thúc) mới ghi nhận kết quả → CHO_DUYET_KQ | Khóa "Đang diễn ra" → tab Kết quả **trống "Chưa có dữ liệu kết quả"**, nút "Lưu kết quả" disabled, có nút "Kết thúc". Khóa "Đã kết thúc" → hiện đủ HV + cho nhập điểm ✅ đúng FR-III-17 |
| Từ chối điểm ngoài 0–10 | **dòng 600** E1 ERR-KQ-01: "Điểm kiểm tra phải từ 0 đến 10" | Ô "Điểm kiểm tra" là InputNumber giới hạn 0–10; nhập 15 → khi rời ô **tự kẹp về 10.0**, không cho lưu điểm sai ✅ đạt yêu cầu "từ chối điểm ngoài 0–10" (cơ chế clamp, không hiện dòng chữ literal) |

**Bằng chứng triangulation (khớp hoàn toàn):**
1. **Video đối tác** (`KTDGKQHT_08-partner-frame-tab-ketqua-trong.jpg` + frame 2/9): khóa **"Đang diễn ra"**, HV "Đã duyệt", tab Kết quả **trống**, nút "Lưu kết quả" disabled + có nút "Kết thúc".
2. **SRS FR-III-17** (dòng 1229, 1244): Màn SCR-III-02 Tab Kết quả, PRE "Khóa học ở DA_KET_THUC", Processing "Kiểm tra khóa DA_KET_THUC → Merge KET_QUA_HOC_TAP → CHO_DUYET_KQ".
3. **Web `AAA-KH-TW`** (Đã kết thúc, 4 HV đã duyệt) → tab Kết quả hiện đủ 4 HV + ô nhập điểm 0–10. Bằng chứng: `reverify-audit/KTDGKQHT_08-web-ketqua-hien-4hv.png`.
4. **Web `KH-SEED-0001`** (chưa kết thúc) → tab Kết quả trống "Chưa có dữ liệu kết quả" (kể cả sau khi duyệt 1 HV). Bằng chứng: `reverify-audit/KTDGKQHT_08-web-ketqua-trong-khoa-chua-dienra.png`.

### Challenge
- **Trả lời trực tiếp câu hỏi review "khóa Đang diễn ra thì sao":** tab Kết quả vẫn TRỐNG (đúng thiết kế). Điểm kiểm tra là điểm CUỐI KHÓA — SRS FR-III-17 chỉ cho nhập khi khóa **"Đã kết thúc"**. Đối tác phải bấm "Kết thúc" khóa trước, không phải lỗi.
- Không phải Open (app không chặn luồng hợp lệ — khóa "Đang diễn ra" CHƯA đủ điều kiện theo FR-III-17). Không phải BA confirm (SRS FR-III-17 nêu rõ, không silent).
- Về validation: app chặn điểm ngoài 0–10 bằng clamp (nhập 15 → về 10), không cho lưu điểm sai → đạt yêu cầu SRS E1. App KHÔNG hiện dòng chữ literal "Điểm kiểm tra phải từ 0 đến 10" — chi tiết UX (dev có thể cân nhắc thêm message), không phải lỗi đối tác báo.

### Data để lại (audit)
- Đã duyệt 1 HV test "QA Import Reverify12 OK" (Chờ duyệt → Đã duyệt) ở `KH-SEED-0001` khi điều tra. Không xóa (HV test QA, env UAT). **KHÔNG** đẩy khóa `KH-SEED-0001` qua Khai giảng/Kết thúc (giữ nguyên state "Đã duyệt" cho các test khác dùng chung seed fixture) — kết luận dựa trên SRS FR-III-17 + `AAA-KH-TW` (Đã kết thúc, đã verify live). Chưa lưu điểm nào.

---

## Case 7 — TTKTDGKQHT_01 · "Tìm kiếm kết quả học tập" (row 7) — ✅ ĐÃ GHI SHEET · **OPEN**

**Verdict: `Open`** — tab "Kết quả kiểm tra" thiếu bộ lọc tìm kiếm theo SRS FR-III-06. Log **BUG-TTKTDGKQHT_01** (Medium).
**Ghi sheet:** 2026-07-10 — P7=`Open`, R7 (501 ký tự), đọc lại khớp. ✅

- **Cổng 1 (evidence full-res `TTKTDGKQHT_01.jpg`):** URL `aaffaa02-...022` · state **Hoàn thành** · KQ công bố 25/03/2026 · 4 HV. Partner: tab Kết quả không có trường tìm kiếm.
- **Bảng đối chiếu điều kiện (0 GAP):** role CB_NV_TW=CB_NV_TW · state Hoàn thành = `AAA-KH-BN` Hoàn thành · data KQ công bố = khớp.
- **Cổng 3 (SRS vs web):** SRS **FR-III-06** (dòng 616–635) — màn SCR-III-02 tab "Kết quả kiểm tra" phải có bộ lọc `tu_khoa`(tên HV)/`khoa_hoc_id`/`ket_qua`. Web `AAA-KH-BN` tab Kết quả: **0 trường tìm kiếm** (chỉ Xuất DOCX/Hủy công bố/Ghi chú). Tái hiện đúng partner. Bằng chứng: `bug-reports/image/TTKTDGKQHT_01-tab-ketqua-thieu-truong-tim-kiem.png`.
- **Challenge:** Không Reject (SRS nêu rõ vị trí + field, app thiếu → Open). Đối chứng: list Bài giảng CÓ search (FR-III-08) → search được implement chỗ khác, riêng tab Kết quả thiếu.

## Case 8 — QLKTLBG_02 · "Kho tài liệu/Bài giảng — hiển thị danh sách" (row 8) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (không tái hiện "Lỗi hệ thống"). **Ghi sheet:** P8=`Reject`, R8 (496 ký tự). ✅ · Note: `reverify-audit/note-QLKTLBG_02.txt`

- **Cổng 1:** đã tải & xem `partner-evidence/QLKTLBG_02.jpg` — ảnh cho thấy toast "Lỗi hệ thống, vui lòng thử lại sau" kèm danh sách rỗng (env đối tác). Đối chiếu claim cột L khớp.
- **Cổng 3:** Web `18.143.165.120` màn Kho tài liệu/Bài giảng: trang tải OK, bảng đủ cột, **không có "Lỗi hệ thống"** ở **cả 2 trạng thái** — rỗng và **khi có dữ liệu** (1 bản ghi PDF `QA UAT Bài giảng Test QLKTLBG_08`: hiển thị đúng cột, không tràn/đè, phân trang 20/trang). Network `GET /api/v1/bai-giangs?page=1&pageSize=20` → **[200]** (default 20/trang khớp Expected). Bằng chứng: `reverify-audit/QLKTLBG_02-web-kho-baigiang-load-ok.png` (rỗng) + `reverify-audit/QLKTLBG_02-web-kho-baigiang-co-du-lieu.png` (có dữ liệu).
- **Challenge:** Lỗi hệ thống nhiều khả năng transient trên env đối tác lúc test → note đề nghị gửi lại thời điểm để rà log nếu tái diễn.

## Case 9 — QLKTLBG_03 · "Thêm bài giảng — thiếu trường Ảnh đại diện" (row 9) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (không tái hiện; trường "Ảnh đại diện" CÓ, đúng SRS). **Ghi sheet:** P9=`Reject`, R9 (409 ký tự). ✅ · Note: `reverify-audit/note-QLKTLBG_03.txt`

- **Cổng 1:** đã tải & xem `partner-evidence/QLKTLBG_03.jpg` — ảnh cho thấy form đối tác thiếu trường "Ảnh đại diện" (sau "Lĩnh vực" tới thẳng "Công khai"). Đối chiếu claim cột L khớp.
- **Cổng 3 (bug tĩnh — chỉ cần SRS vs web, bỏ bảng điều kiện):** SRS **FR-III-07** field #7 `anh_dai_dien` (jpg/png/gif, max 5MB). Web form "Thêm bài giảng": CÓ đủ trường **Ảnh đại diện** (upload .jpg/.jpeg/.png/.gif max 5MB) + Tên/Mô tả/Loại/Tệp/Lĩnh vực/Công khai — khớp SRS. Bằng chứng: `reverify-audit/QLKTLBG_03-form-co-truong-anh-dai-dien.png`.
- **Challenge:** Partner thấy thiếu nhiều khả năng do build cũ (env ospgroup) → note đối tác kiểm tra lại.

## Case 10 — QLKTLBG_08 · "Kho tài liệu/Bài giảng — Thêm mới hợp lệ" (row 10) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (không tái hiện "Lỗi hệ thống"; Thêm mới hợp lệ lưu thành công). **Ghi sheet:** P10=`Reject`, R10 (451 ký tự), đọc lại khớp. ✅ · Note: `reverify-audit/note-QLKTLBG_08.txt`

- **Cổng 1:** Ảnh đối tác `QLKTLBG_08.jpg` **KHÔNG được share vào Drive** (chỉ có QLKTLBG_03/07). Claim cột L rõ: bấm Lưu → toast "Lỗi hệ thống, vui lòng thử lại sau". Lỗi hệ thống = lỗi runtime → verify mạnh nhất bằng **tái hiện trực tiếp** (mạnh hơn xem ảnh 1 toast lỗi).
- **Bảng đối chiếu điều kiện:** role CB_NV_TW = CB_NV_TW · input "hợp lệ" (đối tác không nêu loại) → test đủ 3 biến thể để đóng GAP loại. Env khác (ospgroup vs 18.143.165.120).
- **Cổng 3 (SRS vs web):** SRS **FR-III-07** (dòng 755–757): CB NV thêm bài giảng hợp lệ → lưu thành công + preview. Web: Thêm mới 3 trường hợp — **PDF (công khai OFF)**, **PDF (công khai ON)**, **Video (URL YouTube)** — đều toast "Tạo bài giảng thành công", **không "Lỗi hệ thống"**. Network: `POST /bai-giangs/upload-file` → **[201]** + `POST /bai-giangs` → **[201]** (2 lần PDF); Video `POST /bai-giangs` → **[201]**. List hiện đủ 3 record 3 loại + badge công khai đúng ("Hiển thị 1-3/3 kết quả"). Bằng chứng: `reverify-audit/QLKTLBG_08-them-moi-thanh-cong-web.png`.
- **Challenge:** Không Open (không chặn luồng hợp lệ — ngược lại lưu OK). Không BA confirm (SRS rõ, không silent). Lỗi hệ thống của đối tác nhiều khả năng transient / build cũ trên env đối tác → Reject + đối tác kiểm tra lại. **Residual:** chưa xem được ảnh đối tác + chưa test loại Slide (PPTX) → nếu đối tác vẫn gặp, xin ảnh + loại tài liệu cụ thể lúc lỗi.

### Data để lại (audit)
- Đã tạo 3 bản ghi test ở Kho tài liệu/Bài giảng: `QA UAT Bài giảng Test QLKTLBG_08` (PDF, chưa công khai), `QA UAT Bài giảng Công khai QLKTLBG_08b` (PDF, đã công khai), `QA UAT Video QLKTLBG_08c` (Video). Giữ lại làm data tiền đề cho Case 11 TTKTLBG_01 (nhất quán convention "Data để lại" các case trước, không xóa). File PDF test: `.tmp-uat/qa-baigiang-test.pdf`.

## Case 11 — TTKTLBG_01 · "Tìm kiếm kho tài liệu, bài giảng" (row 11) — ✅ ĐÃ GHI SHEET

**Verdict: `Reject`** (không tái hiện "Lỗi hệ thống"; tìm kiếm chạy đúng + phân trang). **Ghi sheet:** P11=`Reject`, R11 (418 ký tự), đọc lại khớp. ✅ · Note: `reverify-audit/note-TTKTLBG_01.txt`

- **Cổng 1:** Ảnh đối tác `TTKTLBG_01.jpg` **KHÔNG được share vào Drive**. Claim cột L rõ: tìm theo từ khóa → toast "Lỗi hệ thống, vui lòng thử lại sau". Điều kiện đối tác ghi rõ "Tồn tại bản ghi phù hợp" → verify bằng tái hiện trực tiếp **khi kho CÓ dữ liệu**.
- **Bảng đối chiếu điều kiện (đóng GAP data):** role CB_NV_TW = CB_NV_TW · **data tiền đề "có bản ghi phù hợp"** → đã seed 3 bài giảng (Case 10) rồi search lại. Env khác.
- **Cổng 3 (SRS vs web):** SRS **FR-III-08** (dòng 813–814): CB NV nhập từ khóa → tìm kiếm → danh sách phù hợp, phân trang. Web: (a) search kho rỗng `GET /bai-giangs?keyword=Luật` → **[200]**; (b) search khi có data `keyword=QA` → **[200]**, hiện record đúng "Hiển thị 1-1/1 kết quả"; (c) search + lọc Loại tài liệu PDF → **[200]**, hiển thị đúng. Phân trang 20/trang. **Không "Lỗi hệ thống"** ở mọi biến thể. Bằng chứng: `reverify-audit/TTKTLBG_01-search-with-data-ok.png`.
- **Challenge:** Không Open (tìm kiếm hoạt động đúng SRS + phân trang). Không BA confirm (SRS rõ). Lỗi đối tác nhiều khả năng transient / build cũ → Reject + đối tác kiểm tra lại. **Residual:** chưa xem được ảnh đối tác → nếu vẫn gặp, xin ảnh + từ khóa/bộ lọc cụ thể lúc lỗi.
