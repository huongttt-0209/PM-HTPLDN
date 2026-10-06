# CHUẨN CHẤM — KTDGKQHT_05 · "Tải lên tệp Excel điểm danh"

> **FLOW 04 · GIAI ĐOẠN A — khoá chuẩn chấm. CHƯA mở màn đang tranh chấp.**
> File này KHÔNG chấm verdict. Mọi quan hệ `MATCH/DIFF/GAP` dưới đây đã khoá; Giai đoạn B **cấm đổi** để khớp kết quả đo (Flow 04 §BUG SCOPE LOCK luật 5).

---

## 1. Bảng đầu

| Hạng mục | Giá trị |
|---|---|
| **Bảng · tab · dòng** | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219) · **dòng 10** |
| **Mã TC** | `KTDGKQHT_05` — "Tải lên tệp Excel điểm danh" |
| **Trạng thái trên bảng** | `Trạng thái` = Fail · `Dopai` = `N/R` · `Trạng thái dev fix` = **Fixed** · `DEV phản hồi lần 1` = trống · `Kết quả verify` = trống |
| **Env đo** | `https://18.143.165.120.nip.io` (env NỘI BỘ) · API `https://18.143.165.120.nip.io/api/v1` |
| **MailHog (OTP)** | `http://18.143.165.120:8025` |
| **Tài khoản dự kiến** | `cbnv_tw_02` / `Test@1234` — CB Nghiệp vụ Trung ương (`CB_NV_TW`). Lock → fallback **cùng role + cùng cấp** (`cbnv_tw_03`, `cbnv_tw_05`…), **cấm** đổi role/cấp; ghi account thực dùng vào báo cáo |
| **Vai trò theo đặc tả** | CB NV / CB PD — `srs-fr-03-dao-tao.md:526` (Tác nhân FR-III-05) · quyền "Quản lý kết quả ĐT" `:534` (PRE-01) |
| **Màn đo** | SCR-III-02 — Chi tiết Khóa học → **Tab "Điểm danh"** (`srs-fr-03-dao-tao.md:522`, `:1919`) |
| **URL màn (mẫu)** | `https://18.143.165.120.nip.io/dao-tao/khoa-hoc/{khoa_hoc_id}` → tab Điểm danh. ⚠️ Ảnh đối tác dùng `?tab=lich-hoc-diem-danh` trên env **khác** (`htpldn-uat.ospgroup.vn`); **phải đọc lại param tab live trên env nội bộ**, không bê nguyên. Điều hướng bằng **click sidebar** (MCP Rule 3), không `navigate_page` sau login |
| **SRS nguồn chuẩn (prompt chỉ định)** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **cấm** `input/srs-update-2026-5-5/`, `input/srs-v3/` |
| **File SRS đã tự mở trong lượt này** | `srs-fr-03-dao-tao.md` — **tổng 2296 dòng** (mtime 2026-08-04 17:17, md5 `63f378eab606497c51f0c38c74420c89`)<br>`srs-v3.5.md` — **tổng 7012 dòng** (mtime 2026-08-06 22:52) |
| **Cảnh báo drift số dòng** | BA đã chèn khối "Sửa đổi 2026-08-04 (KTDGKQHT_05)" vào **đầu** `srs-fr-03-dao-tao.md` (`:14`) → mọi mục bên dưới trôi ~18 dòng so với phiếu BA cùng ngày. **Mọi số dòng dưới đây là số tự đếm lại 2026-08-07 trên bản 2296 dòng.** Nếu tổng số dòng ≠ 2296 khi Giai đoạn B mở lại → **đếm lại**, không dùng số trong file này |

---

## 2. Nguồn đã đọc (và vì sao đọc)

| # | Nguồn | Vì sao đọc |
|---|---|---|
| 1 | `flows/04-verify-bug-dev-fix-khong-ho-so.md` (299 dòng, đọc trọn) | Quy trình bắt buộc: §Nguồn chuẩn duy nhất · §BUG SCOPE LOCK · §Cổng bằng chứng · §Đối chiếu đặc tả |
| 2 | **`srs-fr-03-dao-tao.md:14`** | Khối "Sửa đổi 2026-08-04 (KTDGKQHT_05)" — BA chèn cho **chính case này** ⇒ là đặc tả hiện hành, không phải ghi chú |
| 3 | **`srs-fr-03-dao-tao.md:519–670`** (FR-III-05 trọn mục) | Nguồn chuẩn của cả 3 vế: §Preconditions · §Inputs · §Processing Tải mẫu · §Processing Import Excel · §Error Handling · §Acceptance Criteria |
| 4 | **`srs-fr-03-dao-tao.md:1912–1932`** (SCR-III-02 trọn 8 tab) | Bộ cột Tab 4 "Điểm danh" + nút "Tải mẫu điểm danh" + trạng thái rỗng — trả lời trực tiếp manh mối TKM |
| 5 | `srs-fr-03-dao-tao.md:444–459` (FR-III-04) | Đường tạo học viên duy nhất ⇒ quyết định cách seed tiền đề |
| 6 | `srs-v3.5.md:75` (lịch sử 3.5.8) · `srs-v3.5.md:3543–3566` (entity HOC_VIEN) | Xác nhận BA **KHÔNG** thêm `ma_hoc_vien`; khoá đối chiếu vẫn là `id` |
| 7 | `srs-v3.5.md:6760` (quy ước H8 tên tệp) | Loại trừ tường minh "tệp mẫu nhập liệu tải sẵn (vd *Tải mẫu điểm danh*)" ⇒ bẫy chặn FAIL oan |
| 8 | Grep đồng nghĩa nhiều vòng (xem §7 bẫy 15) | Flow 04 §Nguồn chuẩn: một lệnh grep rỗng KHÔNG đủ để kết luận SRS im lặng |
| 9 | `partner-evidence/KTDGKQHT_05.jpg` (mở full-res + phóng to 4 vùng) | Cổng bằng chứng — lấy neo tái hiện |
| 10 | *(ngữ cảnh, CẤM làm căn cứ verdict)* `reverify-week-4/.../phieu-ban-giao-KTDGKQHT_05-dev-qa.md` | Biết BA đã chốt hướng nào để **tra đúng chỗ trong SRS**; mọi yêu cầu vẫn tự mở SRS xác minh lại |
| 11 | *(ngữ cảnh)* `reverify-week-2/.../bug-report-dao-tao.md:644, :707–723` | Cảnh báo drift số dòng + dữ liệu QA cũ trên **cùng env nội bộ** (`KH-20260730-001`) |
| 12 | `F5-flow04-2026-08-07/TIEN-DO.md` | Vân tay bản dựng V1.0.10 + ánh xạ ghi bảng + giới hạn hiệu lực verdict |

---

## 3. Đọc bằng chứng đối tác

**Tệp:** `partner-evidence/KTDGKQHT_05.jpg` — 1906×1032 px, đã mở full-res + crop phóng to 4 vùng (thanh URL · thanh bước trạng thái · dòng chú thích trong hộp thoại · vùng tab + đầu bảng).

**Thực sự nhìn thấy gì:**

| Vùng | Nội dung đọc được |
|---|---|
| Thanh URL | `htpldn-uat.ospgroup.vn/dao-tao/khoa-hoc/**0aad5545-9361-4fe4-854a-18e3fdce5862**?tab=**lich-hoc-diem-danh**` |
| Góc trên phải | `BTP · TW` · avatar `CB` · **"Cán bộ NV Trung ương"** · mã vai trò **`CB_NV_TW`** |
| Nhánh điều hướng | Trang chủ / Đào tạo, tập huấn / Khóa học / **Chi tiết** |
| Hộp thoại | Tiêu đề **"Import điểm danh từ Excel"**. Dòng chú thích: *"File **.xlsx**, tối đa 5MB. Cột bắt buộc: `Ma hoc vien,Co mat` (1/0)."* — đoạn `Ma hoc vien,Co mat` đang **được bôi đen** (tester tự chọn để chỉ vào) |
| Vùng thả tệp | "Kéo thả hoặc click để chọn file" · "Chỉ nhận .xlsx, tối đa 5MB" |
| Nút trong hộp thoại | Chỉ **một** nút **"Bắt đầu Import"** (đang mờ/disabled vì chưa chọn tệp). **Không thấy** khu vực xem trước, **không thấy** nút "Tải mẫu" nào |
| Sau lưng hộp thoại | Ô chọn **"Chọn buổi học để điểm danh"** đang ở trạng thái **placeholder xám (chưa chọn buổi)**; bảng bên dưới vẫn render đầu cột **STT · Họ tên · … · Trạng thái · Ghi chú** với thân bảng rỗng |
| Thanh bước trạng thái | Chỉ đọc được `✓ Dự thảo` (bước 1) và phần đuôi `…thúc` · `6 Chờ duyệt KQ` · `7 Hoàn thành`. **Bước hiện hành bị hộp thoại che — KHÔNG đọc được trạng thái khóa** |
| Nút hành động dưới | `Công khai` và `Kết thúc` (cả hai màu xanh đậm) |
| Đồng hồ hệ điều hành | **17:18 · 2026-07-24** |

**Neo tái hiện rút ra:**

| Neo | Giá trị | Ghi chú dùng ở Giai đoạn B |
|---|---|---|
| Vai trò | `CB_NV_TW`, đơn vị `BTP · TW` | Khớp tài khoản dự kiến `cbnv_tw_02` |
| Màn | Chi tiết Khóa học → tab điểm danh | Env nội bộ có thể đặt tên/param tab khác → đọc lại live |
| Bản ghi | `khoa_hoc_id = 0aad5545-9361-4fe4-854a-18e3fdce5862` | **Của env đối tác — KHÔNG tồn tại trên env nội bộ.** Cấm đụng dữ liệu đối tác ⇒ dùng khóa QA tương đương |
| Trạng thái khóa | **KHÔNG đọc được** (bị che) | ⇒ tiền đề trạng thái phải tự dựng theo PRE-03, không suy từ ảnh |
| Buổi học | **Chưa chọn buổi** khi mở hộp thoại import | Ghi nhận; Giai đoạn B **phải chọn buổi trước** (`:1920`) |
| Định dạng tệp hệ thống đòi (thời điểm 24/07) | Cột `Ma hoc vien`, `Co mat` (**1/0** — nhị phân) | Manh mối: bản 24/07 chưa theo cơ chế tệp mẫu và chưa theo enum 3 giá trị. **Là manh mối, không phải verdict** |
| Env + thời điểm | `htpldn-uat.ospgroup.vn` · 24/07/2026 17:18 | **Khác env đo.** Verdict chỉ có hiệu lực cho env + bản dựng đã đo |

---

## 4. BUG SCOPE LOCK

> Vế **C1, C2** tách từ ô **"Kết quả mong đợi"** của đối tác (nguồn tách vế theo Flow 04).
> Vế **C3** đến từ **manh mối `TKM phản hồi lần 1` + `Loại vấn đề`**, và chỉ được đưa vào chuẩn chấm vì **SRS có quy định thật** về tệp mẫu nhập liệu (BA chèn cho chính case này ngày 04/08). **C3 KHÔNG đến từ "Kết quả mong đợi".**
> **D1** là đối chiếu đề xuất của TKM — ghi để trả lời TKM, **không** phải tiêu chí chấm.

| Vế | Expected đối tác (nguyên văn) | SRS `file:dòng` | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C1** | "Hiển thị bản xem trước kết quả (số dòng hợp lệ, số dòng lỗi và lý do từng dòng)." | `srs-fr-03-dao-tao.md:593` (+ `:594`, `:650`) | **MATCH** | **TEST** | UI: chọn buổi → mở hộp thoại import → chọn tệp fixture → đọc khối xem trước bằng `innerText`. Đối chứng: đọc **response body** của request upload/preview |
| **C2** | "Nạp thành công, hệ thống hiển thị thông báo *Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ*." | `srs-fr-03-dao-tao.md:595` (+ `:594`, `:650`) | **MATCH** *(theo nội dung, KHÔNG theo câu chữ)* | **TEST** | UI: cài `MutationObserver` **trước** khi bấm xác nhận nạp → bắt thông báo bằng `innerText`. Đối chứng: đọc lại bảng điểm danh của **đúng buổi** đó |
| **C3** | *(không có trong "Kết quả mong đợi" — từ manh mối TKM)* Cán bộ phải có nguồn lấy định danh học viên do **hệ thống cấp**: nút "Tải mẫu điểm danh" sinh tệp điền sẵn `hoc_vien_id` + đúng bộ cột + metadata buổi | `srs-fr-03-dao-tao.md:571–583` · `:590` · `:1919` · `:651` | **MATCH** | **TEST** | UI: sau khi chọn buổi → tìm & bấm nút "Tải mẫu điểm danh". Đối chứng: **mở tệp .xlsx tải về bằng openpyxl**, đọc hàng tiêu đề + 1 hàng dữ liệu |
| **D1** | *(không phải expected — là đề xuất trong ô `Loại vấn đề`)* "nếu thêm cột MHV có đc ko" / "Màn hình danh sách không hiển thị mã học viên" | `srs-fr-03-dao-tao.md:1919` · `srs-v3.5.md:75` · `srs-v3.5.md:3543–3562` | **DIFF — nhưng BA ĐÃ TRẢ LỜI trong chính SRS hiện hành** | **KHÔNG mở câu hỏi BA mới**; ghi lại để trả lời TKM | **Không đo.** Chỉ trích SRS |

---

### C1 — trích nguyên văn SRS

`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:593`
```
| 5 | Hiển thị bản review (thành công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng | — |
```
`…:594`
```
| 6 | Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua | BR-KQ-01, BR-KQ-02 |
```
`…:650`
```
- **Given** CB NV import Excel **When** upload file **Then** validate + import + báo cáo lỗi
```

**Chốt chuẩn chấm C1 — ĐẠT khi đủ cả 3:**
1. Có **khối xem trước hiện ra TRƯỚC khi dữ liệu được ghi** (`:594` "Nếu xác nhận: merge" ⇒ xem trước là cổng xác nhận, không phải báo cáo hậu kiểm).
2. Khối đó **phân tách rõ dòng hợp lệ vs dòng lỗi** (đếm được cả hai nhóm).
3. **Mỗi dòng lỗi** có **lý do/mã lỗi + số dòng** — và 2 dòng lỗi khác lý do phải ra **2 lý do khác nhau**, không gộp một câu chung.

**Ranh giới C1 (chặn FAIL oan):** SRS `:593` **không quy định** phải in ra con số tổng dạng "N hợp lệ / M lỗi". ⇒ Nếu khối xem trước liệt kê đủ dòng để **đếm ra được** hai nhóm thì **không chấm Fail chỉ vì thiếu con số tổng**. Ngược lại, nếu khối xem trước **không cho biết dòng nào hợp lệ / dòng nào lỗi bằng bất kỳ cách nào** thì đó **không phải** "bản review (thành công / lỗi)" ⇒ **Fail C1**.

---

### C2 — trích nguyên văn SRS

`…srs-fr-03-dao-tao.md:595`
```
| 7 | Trả về báo cáo import | — |
```

**Chốt chuẩn chấm C2 — ĐẠT khi đủ cả 3:**
1. Sau khi xác nhận nạp, hệ thống **trả về/hiển thị báo cáo kết quả import** (không im lặng).
2. Báo cáo cho biết được **số bản ghi nạp thành công** và **số bản ghi không hợp lệ**.
3. Hai con số đó **đúng** so với tệp đã nạp (fixture 3 hợp lệ / 2 lỗi) và **cộng khớp** tổng dòng dữ liệu = 5.

**Ranh giới C2 (chặn FAIL oan):** SRS `:595` **không quy định câu chữ** của báo cáo — bảng Error Handling `:633–643` chỉ định nghĩa **thông báo lỗi** ERR-KQ-01…09, **không có** thông báo thành công nào. ⇒ **CẤM chấm Fail vì câu chữ khác chuỗi "Đã nạp {…} bản ghi thành công, {…} bản ghi không hợp lệ"** (quy tắc describe-not-prescribe). Chấm bằng **2 con số + tính đúng**, không bằng so chuỗi.

**Ranh giới C2 (chặn PASS oan):** thông báo có 2 con số nhưng **sai** so với dữ liệu thực ghi ⇒ Fail. Bắt buộc đối chứng bằng đường thứ hai (đọc lại bảng điểm danh của đúng buổi): phải đúng **3** học viên đổi trạng thái, **2** dòng lỗi **KHÔNG** được ghi (`:594` "chỉ merge dòng hợp lệ").

---

### C3 — trích nguyên văn SRS

`…srs-fr-03-dao-tao.md:571`
```
**Processing — Tải mẫu (điểm danh / điểm kiểm tra) `[KTDGKQHT_05 chốt 2026-08-04]`:**
```
`…:573`
```
Nhập liệu qua Excel theo cơ chế "Tải mẫu → điền → tải lên": cán bộ không tự gõ định danh học viên. Hệ thống sinh **hai loại tệp mẫu** theo ngữ cảnh đang thao tác:
```
`…:577` (hàng bảng — điều kiện bật nút)
```
| Mẫu điểm danh | "Tải mẫu điểm danh" (Tab 4) | Buổi học đang chọn (`lich_hoc_id`) | Đã chọn buổi + khóa `DANG_DIEN_RA` + khóa có ≥1 buổi học + có quyền nhập điểm danh |
```
`…:581` (bộ cột bắt buộc của tệp mẫu điểm danh)
```
  - **Mẫu điểm danh:** `hoc_vien_id` (điền sẵn, khoá/ẩn — ID nội bộ opaque, cán bộ không sửa) · Họ tên · Email · Đơn vị · **Trạng thái điểm danh** (trống — điền: Có mặt / Vắng có phép / Vắng không phép) · Ghi chú.
```
`…:583`
```
- `lich_hoc_id` (mẫu điểm danh) / `de_kiem_tra_id` (mẫu điểm kiểm tra) được **nhúng ở vùng metadata/tiêu đề tệp** (không phải cột từng dòng), để khi tải lên hệ thống biết tệp thuộc buổi/đề nào — cán bộ không phải nhập.
```
`…:590` (import phải khớp bộ cột tệp mẫu)
```
| 2 | Xác nhận tệp theo **đúng bộ cột của tệp mẫu** (mục "Tải mẫu"); thiếu/sai cột → ERR-KQ-02. Xác định **loại bản ghi theo loại tệp mẫu** (mẫu điểm danh → điểm danh; mẫu điểm kiểm tra → điểm kiểm tra); đọc `lich_hoc_id` / `de_kiem_tra_id` từ **metadata tệp** và bắt buộc **khớp buổi / đề đang chọn** trên màn; lệch → ERR-KQ-09 |
```
`…:651` (Acceptance Criteria)
```
- **Given** CB NV đã chọn buổi (Tab 4) hoặc đề kiểm tra (Tab 5) **When** nhấn "Tải mẫu" **Then** tải tệp Excel điền sẵn danh sách học viên + định danh, cột điểm danh/điểm kiểm tra để trống
```
`…:1919` (SCR-III-02 Tab 4 — nút + bộ cột màn hình)
```
4. **Tab 4 — Điểm danh** …: Cột STT · **Họ tên** · **Email** · **Số điện thoại** · **Đơn vị** · Buổi học (FK lich_hoc_id) · Trạng thái điểm danh (**Có mặt** / **Vắng có phép** / **Vắng không phép** — enum 3 trạng thái) · Ghi chú. Hỗ trợ Import Excel hàng loạt qua tệp mẫu — nút **"Tải mẫu điểm danh"** (bật sau khi chọn buổi, khóa `DANG_DIEN_RA`, khóa có ≥1 buổi học, có quyền; xem Processing "Tải mẫu" tại FR-III-05). `[KTDGKQHT_05 chốt 2026-08-04]`
```

**Chốt chuẩn chấm C3 — ĐẠT khi đủ cả 3:**
1. Tab Điểm danh **có nút "Tải mẫu điểm danh"** và nút **bật** đúng điều kiện `:577` (đã chọn buổi + khóa `DANG_DIEN_RA` + khóa có ≥1 buổi + có quyền).
2. Tệp tải về mở được bằng openpyxl và có **đúng bộ cột `:581`**: `hoc_vien_id` · Họ tên · Email · Đơn vị · Trạng thái điểm danh · Ghi chú — trong đó `hoc_vien_id` **đã điền sẵn** và cột Trạng thái điểm danh **để trống**.
3. Định danh buổi học nằm ở **metadata/tiêu đề tệp**, **không** phải cột từng dòng (`:583`).

**Ranh giới C3 (chặn FAIL oan):** `:583` cho phép **metadata HOẶC tiêu đề tệp** ⇒ không chấm Fail vì dev chọn cách nhúng nào; chỉ cần đọc ra được. Tên tệp mẫu **không** chịu khuôn H8 (`srs-v3.5.md:6760` loại trừ tường minh) ⇒ không chấm Fail vì tên tệp.

**Ranh giới C3 (chặn PASS oan):** thấy nút "Tải mẫu điểm danh" trên màn **chưa đủ** — Flow 04 §Chạy bước 5 cấm Pass bằng quan sát tĩnh. Phải **bấm thật, tải thật, mở tệp thật**.

**Quan sát bắt buộc ghi nhận khi đo C3** (không mở thêm phép đo): giá trị hợp lệ của cột Trạng thái điểm danh phải là **3 giá trị** Có mặt / Vắng có phép / Vắng không phép (`:549`, `:581`, `:638` ERR-KQ-04, `:1919`). Ảnh đối tác 24/07 cho thấy hệ thống lúc đó dùng **`Co mat` (1/0) nhị phân** — nếu env đo **vẫn** nhị phân thì đó là **một phần của C3 không đạt** (sai bộ cột tệp mẫu), ghi vào chính vế C3, **không** tách thành phép đo/bug riêng.

---

### D1 — trích nguyên văn SRS (trả lời TKM, không chấm)

`…srs-fr-03-dao-tao.md:1919` — bộ cột Tab 4 **không có** cột "Mã học viên" (xem trích ở C3).

`…srs-fr-03-dao-tao.md:14`
```
**Sửa đổi 2026-08-04 — chuẩn hoá nghiệp vụ nhập kết quả qua Excel bằng cơ chế "Tải mẫu → điền → tải lên" (KTDGKQHT_05):** … **Giữ `hoc_vien_id` làm khoá đối chiếu, KHÔNG thêm trường vào entity HOC_VIEN.**
```

`…srs-v3.5.md:75`
```
| **3.5.8** | **2026-08-04** | … **Entity HOC_VIEN §3.4.3.53 giữ nguyên — KHÔNG thêm `ma_hoc_vien`, khoá đối chiếu vẫn là `id`.** …
```

`…srs-v3.5.md:3550–3562` — bảng trường HOC_VIEN đã đọc trọn 11 trường: `id · ho_ten · don_vi · chuc_vu · email · so_dien_thoai · khoa_hoc_id · trang_thai_tham_gia · ket_qua · ngay_dang_ky · tai_khoan_id` — **không có** trường mã học viên.

**Kết luận D1:** đề xuất của TKM ("thêm cột MHV") **đã được BA xem xét và chốt theo hướng khác** ngay trong bản SRS mà prompt chỉ định: khe hở "không có nguồn lấy định danh" được vá bằng **cơ chế tệp mẫu (C3)**, **không** bằng cách phơi mã học viên ra màn danh sách. ⇒ **KHÔNG mở câu hỏi BA mới cho D1**, và **CẤM chấm Fail** vì Tab Điểm danh không có cột Mã học viên.

---

## 5. Đường đo tối thiểu cho từng vế

> Mặc định mỗi vế: **một đường UI ngắn nhất + một đối chứng độc lập** (Flow 04 §BUG SCOPE LOCK luật 3). Hai đường khớp thì **dừng**, không thêm đường thứ ba.

### C3 — cơ chế tệp mẫu *(đo TRƯỚC C1/C2 vì tệp mẫu là đầu vào của C1/C2)*

| | Nội dung |
|---|---|
| **Đường UI** | Đăng nhập `cbnv_tw_02` → click sidebar Đào tạo, tập huấn → Khóa học → mở khóa tiền đề → tab **Điểm danh** → **chọn buổi học** → tìm nút "Tải mẫu điểm danh" → **bấm tải** |
| **Đối chứng độc lập** | **Mở nội dung tệp .xlsx** bằng `openpyxl`: đọc hàng tiêu đề + 1 hàng dữ liệu + vùng metadata/tiêu đề. ⚠️ MCP chạy Chrome `--isolated` có thể **không** đổ tệp về `~/Downloads` → thử `~/Downloads` trước; không có thì parse zip **trong trang** (EOCD + `DecompressionStream`), **chỉ trả** hàng tiêu đề + 1 hàng mẫu + chuỗi metadata (cấm dump base64 cả tệp) |
| **Số đo quyết định** | (a) nút có / không · trạng thái bật đúng `:577`; (b) **danh sách tên cột đọc được** so với 6 cột `:581`; (c) số ô `hoc_vien_id` đã điền sẵn = số học viên của khóa; (d) cột Trạng thái điểm danh rỗng 100%; (e) chuỗi định danh buổi tìm thấy trong metadata/tiêu đề (có/không) |

### C1 — bản xem trước

| | Nội dung |
|---|---|
| **Đường UI** | Cùng phiên, cùng buổi đã chọn → mở hộp thoại **Import điểm danh từ Excel** → `upload_file` tệp fixture (5 dòng: 3 hợp lệ + 2 lỗi khác lý do) → **dừng lại trước khi bấm xác nhận nạp** → đọc khối xem trước bằng `evaluate_script` trả về `innerText` (**không** `textContent`) |
| **Đối chứng độc lập** | `list_network_requests` → `get_network_request` lấy **response body** của chính request upload/preview → đối chiếu số dòng hợp lệ / số dòng lỗi / mã lỗi từng dòng trong payload với chữ trên màn |
| **Số đo quyết định** | Bộ ba **(số dòng hợp lệ, số dòng lỗi, tập lý do)** = **(3, 2, {2 lý do KHÁC NHAU gắn đúng số dòng})**. Cộng khớp: 3 + 2 = **5** = tổng dòng dữ liệu trong tệp |

### C2 — báo cáo sau khi nạp

| | Nội dung |
|---|---|
| **Đường UI** | Cài `MutationObserver` trên `document.body` **TRƯỚC** khi bấm → bấm nút xác nhận nạp → thu `addedNodes` trong 2–5 s → lọc theo lớp thông báo AntD, đọc **`innerText`**, **CẤM lọc trùng** |
| **Đối chứng độc lập** | **Đọc lại bảng điểm danh của đúng buổi vừa nạp** (reload tab, đọc DOM hoặc gọi lại endpoint danh sách kết quả của buổi đó — **đọc endpoint từ `list_network_requests` của chính màn, cấm đoán đường dẫn**) |
| **Số đo quyết định** | (a) 2 con số trong thông báo; (b) **số học viên thực sự đổi trạng thái = 3**; (c) **2 học viên ở dòng lỗi KHÔNG bị ghi** (`:594`); (d) (a) ≡ (b),(c) |

---

## 6. Tiền đề tối thiểu phải có

| # | Tiền đề | Căn cứ SRS | Cách có |
|---|---|---|---|
| T1 | **Khóa học ở `DANG_DIEN_RA`** | `:536` PRE-03 · `:640` ERR-KQ-06 · `:659`, `:1923` (DA_KET_THUC ⇒ chỉ đọc) | Ưu tiên **dùng lại khóa QA sẵn có** trên chính env nội bộ. Ứng viên đã ghi nhận: **`KH-20260730-001`** (3 buổi 10/08 08:00 · 11/08 08:00 · 11/08 13:00, **đã Khai giảng**, đã có học viên, đã điểm danh 1 buổi) — **phải kiểm lại trạng thái live**, có thể đã bị đẩy tiếp. Nếu khóa đã `DA_KET_THUC` → chọn khóa khác; **không** ép lùi trạng thái |
| T2 | **Khóa có ≥1 buổi học và đã chọn buổi** | `:538` PRE-05 · `:1920` (bộ chọn buổi bắt buộc) | Thiếu buổi → thêm buổi ở Tab Lịch học (FR-III-22) — **khai báo mutate env** |
| T3 | **≥5 học viên thuộc khóa** (3 hợp lệ + 2 dòng lỗi) | `:592` ERR-KQ-03 cần học viên **thuộc** khóa | ⚠️ **Cán bộ KHÔNG tạo được học viên từ bên trong** — `:449` ghi rõ đăng ký của DN/NHT trên chuyên trang là **"đường tạo đăng ký duy nhất"**. ⇒ (a) **dùng lại khóa đã có sẵn học viên**; (b) nếu buộc phải seed: đăng ký qua chuyên trang bằng tài khoản DN vào khóa ở `DA_CONG_KHAI`/`DANG_DIEN_RA` (`:458` PRE-02) rồi CB NV duyệt — **khai báo đầy đủ: khóa nào · thêm mấy HV · env nào**; (c) không làm được cả (a) và (b) → **Chưa chốt**, nêu rõ thiếu dữ liệu gì. **Cấm đụng dữ liệu đối tác** |
| T4 | **1 `hoc_vien_id` của khóa KHÁC** (làm dòng lỗi ERR-KQ-03) | `:592`, `:637`, `:654` | Đọc từ danh sách học viên của một khóa khác qua UI/endpoint danh sách đã lộ trên màn — **cấm đoán endpoint/khóa JSON**, đọc schema trước |
| T5 | **Quyền + phạm vi đơn vị** | `:534` PRE-01 · BR-AUTH-08 | Khóa tiền đề phải thuộc đơn vị của `cbnv_tw_02`. Không thấy khóa → fallback sibling **cùng role + cùng cấp**; ghi account thực dùng |
| T6 | **Vân tay bản dựng** | Flow 04 §Chuẩn bị bước 2 | Ghi `Last-Modified`/etag `GET /` + tên bó mã đầu phiên. Kỳ vọng **V1.0.10**; khác ⇒ báo điều phối trước khi chốt |

### Tệp Excel fixture — bắt buộc

🔴 **Fixture phải là .xlsx THẬT tạo bằng `openpyxl`. CẤM tạo chuỗi chữ rồi đổi đuôi `.xlsx`** (Flow 04 §Chuẩn bị bước 3).
Lưu tại `output/UAT_doi-tac/reverify-week-5/F5-flow04-2026-08-07/seed-files/`.

**Quy tắc chọn nguồn tệp — quyết định theo kết quả C3:**

| Kết quả đo C3 | Tệp dùng cho C1/C2 |
|---|---|
| **Có** nút "Tải mẫu điểm danh" và tải được | 🔴 **BẮT BUỘC dùng chính tệp mẫu hệ thống sinh**, chỉ điền thêm cột Trạng thái điểm danh. Tự dựng tệp tay sẽ thiếu metadata buổi → vướng ERR-KQ-09 (`:590`, `:643`) → **FAIL oan C1/C2** |
| **Không** có nút "Tải mẫu" | Dựng tệp bằng `openpyxl` theo **đúng bộ cột mà hộp thoại đang công bố trên màn** (đọc chữ trên hộp thoại tại thời điểm đo, không bê "Ma hoc vien,Co mat" từ ảnh 24/07). C3 ghi không đạt; C1/C2 **vẫn đo tiếp** — không được tuyên bố chặn |

**Cấu trúc dữ liệu fixture — 5 dòng dữ liệu, cố định:**

| Dòng | Nội dung | Kỳ vọng | Vì sao chọn |
|---:|---|---|---|
| 1–3 | 3 học viên **thuộc** khóa, trạng thái điểm danh **hợp lệ** | **hợp lệ** | ≥2 dòng để phát hiện đếm cứng "1" |
| 4 | `hoc_vien_id` của **khóa khác** (T4), trạng thái hợp lệ | **lỗi — ERR-KQ-03** (`:637`, `:654`) | Sai dưới **mọi** cách hiểu định dạng (cũ hay mới) ⇒ không phụ thuộc dev đã fix tới đâu |
| 5 | Học viên **thuộc** khóa, ô trạng thái điểm danh = **`XYZ`** | **lỗi — ERR-KQ-04** (`:638`) | Ngoài enum dưới **mọi** cách hiểu |

**Vì sao 3 hợp lệ / 2 lỗi (KHÔNG phải 1/1, KHÔNG phải 2/2):** hai con số **khác nhau** ⇒ phát hiện được lỗi hoán vị (in số lỗi vào ô số thành công); mỗi nhóm **≥2** ⇒ phát hiện được số đếm cứng; tổng **5** ⇒ kiểm được phép cộng khớp.

🔴 **CẤM dùng "Vắng có phép" làm dòng lỗi cố ý.** Nếu dev đã làm đúng enum 3 giá trị (`:549`) thì đó là dòng **hợp lệ** → phá vỡ thiết kế đếm 3/2 → đọc sai kết quả cả C1 lẫn C2.

---

## 7. Bẫy đã biết — chặn FAIL oan / PASS oan

### Chặn FAIL oan

1. **CẤM chấm Fail vì Tab Điểm danh không có cột "Mã học viên".** SRS `:1919` chốt bộ cột không có nó; `srs-v3.5.md:75` + `:3550–3562` chốt **KHÔNG** thêm `ma_hoc_vien`. Đây chính là đề xuất TKM **đã bị BA thay bằng cơ chế tệp mẫu**.
2. **CẤM chấm Fail vì câu chữ thông báo khác chuỗi đối tác viết.** SRS `:595` chỉ ghi "Trả về báo cáo import"; bảng Error Handling `:633–643` **không** có thông báo thành công nào. Chấm bằng **con số**, không bằng so chuỗi.
3. **CẤM chấm Fail vì khối xem trước không in con số tổng**, nếu vẫn đếm được hai nhóm từ danh sách dòng (`:593` không quy định con số tổng).
4. **CẤM chấm Fail khi khóa ở `DA_KET_THUC` mà import điểm danh bị chặn** — SRS `:536` PRE-03 + `:640` ERR-KQ-06 + `:659` + `:1923` **bắt buộc** chặn. ⚠️ Ô "Điều kiện" của phiếu đối tác ghi *"Đang diễn ra **hoặc Đã kết thúc**"* — vế "Đã kết thúc" **lệch SRS**. ⇒ **phải đo trên `DANG_DIEN_RA`**; nếu vô tình đo trên khóa đã kết thúc rồi kết luận Fail thì đó là FAIL oan.
5. **CẤM chấm Fail vì tên tệp mẫu không theo khuôn H8** — `srs-v3.5.md:6760` loại trừ tường minh tệp mẫu nhập liệu tải sẵn.
6. **CẤM chấm Fail vì `hoc_vien_id` trong tệp mẫu là chuỗi UUID khó đọc** — `:581` quy định đúng là **"ID nội bộ opaque, cán bộ không sửa"**, khoá/ẩn là **đúng** đặc tả.
7. **CẤM chấm Fail vì nhãn/số thứ tự tab lệch** (env đối tác gộp `?tab=lich-hoc-diem-danh`). SRS `:1919` ràng buộc **nội dung** tab Điểm danh, không ràng buộc slug URL. Cấu trúc tab lệch ⇒ ghi **candidate một dòng**, không mở phép đo.

### Chặn PASS oan

8. **CẤM Pass bằng quan sát tĩnh** (Flow 04 §Chạy bước 5). Thấy nút "Tải mẫu", thấy chữ "xem trước" trong hộp thoại, thấy hộp thoại có vùng thả tệp — **không** kết luận được gì. Phải **bấm thật · nạp tệp thật · mở tệp thật · đọc con số thật**.
9. **Chữ người dùng nhìn thấy phải đọc bằng `innerText`.** `textContent` gom cả node ẩn của AntD (thông báo cũ đã đóng, template chưa render) → **bug ma** / số ma.
10. **Bộ bắt thông báo CẤM lọc trùng.** Lọc trùng che double-toast → Pass oan. Cài observer **TRƯỚC** khi bấm; luôn **đếm kèm số request** phát sinh.
11. **Một thông báo ra hai bản ghi ⇒ đếm theo MỐC GIỜ khác nhau**, không theo độ dài mảng `addedNodes`.
12. **Đếm gộp thẻ bọc ngoài với thẻ con → số nhân đôi.** Đọc **số thô trước**, đừng lọc/gộp rồi mới nhìn (vd đếm `.ant-table-row` lồng trong wrapper).
13. **Các chiều số phải cộng khớp:** (số hợp lệ) + (số lỗi) = **5** = tổng dòng dữ liệu fixture. Không khớp ⇒ **số đang sai, chưa được chốt** — đo lại, không chốt verdict.
14. **Hai phép đo mâu thuẫn (màn nói 3, response body nói 4) ⇒ CHƯA được chốt.** Ghi cả hai, hỏi điều phối.
15. **Đã grep nhiều vòng từ đồng nghĩa trước khi khoá quan hệ** — `điểm danh · học viên · mã học viên · nhập tệp · tải lên · Excel · import · xem trước · preview · bản review · báo cáo import · dòng hợp lệ · dòng lỗi · bản ghi không hợp lệ · đã nạp · tệp mẫu · tải mẫu · template` trên **cả** `srs-fr-03-dao-tao.md` và `srs-v3.5.md`, cộng dấu thay đổi `[KTDGKQHT_05 chốt 2026-08-04]` / `[STT…]`. **Không** kết luận "SRS im lặng" từ một lệnh grep rỗng.
16. **Ảnh chụp toàn trang lúc trang đang vẽ lại ⇒ luôn mở lại ảnh xem.** Thông báo tự tắt <5 s: hẹn giờ bấm rồi mới chụp; trượt ảnh thì **response body là bằng chứng mạnh hơn**.
17. **Tab MCP mở lâu vẫn chạy mã cũ ⇒ tải lại trang trước lô đo** và ghi vân tay bản dựng (T6). Env này deploy liên tục (V1.0.8 → V1.0.10 trong ~10 giờ).
18. **Giới hạn hiệu lực verdict:** đối tác đo trên `htpldn-uat.ospgroup.vn` (V1.0, 24/07); lô này đo trên `18.143.165.120.nip.io` (V1.0.10). Verdict **chỉ** có hiệu lực cho env + bản dựng đã đo — câu này bắt buộc vào ô `Kết quả verify`.
19. **CẤM mở rộng** thành hồi quy nhập tay, ma trận CRUD, mọi vai trò, mọi bộ lọc, Tab 5 "Kết quả kiểm tra", hay 9 kịch bản QA của phiếu bàn giao tuần 4. Phiếu đó là **ngữ cảnh**, không phải phạm vi đo của case này.

### Ghi nhận, không mở phép đo (candidate một dòng)

20. Ảnh đối tác cho thấy **bảng điểm danh render đầu cột với thân rỗng khi CHƯA chọn buổi**, trong khi SRS `:1921` bắt buộc hiện dòng *"Vui lòng chọn buổi học để bắt đầu điểm danh"*. Đây là vế của **KTDGKQHT_03**, **không** thuộc case này ⇒ nếu tái xuất hiện trên env đo thì ghi **candidate một dòng**, không điều tra, không đổi verdict KTDGKQHT_05.

---

## 8. Điều còn thiếu / câu hỏi cho điều phối

| # | Vấn đề | Ảnh hưởng | Đề xuất |
|---|---|---|---|
| 1 | **Trạng thái khóa trong ảnh đối tác không đọc được** (thanh bước bị hộp thoại che) | Không biết đối tác đo ở `DANG_DIEN_RA` hay `DA_KET_THUC`; ô "Điều kiện" của phiếu ghi cả hai, trong khi SRS `:536` chỉ cho `DANG_DIEN_RA` | Giai đoạn B **đo trên `DANG_DIEN_RA`** và ghi rõ chênh lệch tiền đề này vào kết quả. Không hỏi lại đối tác |
| 2 | **Tiền đề T3 (≥5 học viên) có thể không dựng được** | `:449` chốt cán bộ không tạo được học viên từ bên trong | Nếu không tìm được khóa `DANG_DIEN_RA` có ≥5 học viên **và** không seed được qua chuyên trang → **Chưa chốt**, nêu đúng dữ liệu còn thiếu. **Không** kết luận "không phải lỗi" vì không tái hiện được |
| 3 | **Rủi ro lớn nhất — C1 có thể không tồn tại ở dạng 2 bước.** Hộp thoại trong ảnh chỉ có **một** nút "Bắt đầu Import", không thấy vùng xem trước | Nếu web nạp thẳng rồi báo kết quả (1 bước), C1 **Fail** (`:594` "Nếu xác nhận: merge" ⇒ xem trước là cổng xác nhận) trong khi C2 vẫn có thể đạt ⇒ case ra **Reopen** vì một vế | **Không phán trước.** Ảnh là bản 24/07 env khác; khối xem trước có thể render **sau** khi chọn tệp. Bắt buộc chọn tệp thật rồi mới đọc |
| 4 | **Câu chữ báo cáo import chưa có trong SRS** (`:595` chỉ ghi "Trả về báo cáo import"; Error Handling `:633–643` không có thông báo thành công) | Không chặn verdict — đã khoá C2 chấm theo **nội dung**, không theo chuỗi | Nếu web đạt C2 về nội dung: ghi **ghi chú mềm** đề nghị BA bổ sung câu chữ chuẩn cho thông báo import vào Error Handling FR-III-05. **Không** biến thành câu hỏi chặn bàn giao, **không** đổi quan hệ đã khoá |
| 5 | **Ánh xạ ghi bảng** | `TIEN-DO.md` chỉ cấp `Trạng thái dev fix` + `Kết quả verify`; **không** cấp ô ảnh bằng chứng | Link ảnh xem được nhúng **trong chính ô `Kết quả verify`**. Ô `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1` là **chỉ đọc** |

---

## 9. Cổng chốt Giai đoạn A — tự kiểm

| # | Câu hỏi (Flow 04 §Cổng chốt verdict) | Trả lời |
|---|---|---|
| 1 | Mỗi vế chấm được neo vào dòng nào của đúng SRS prompt cung cấp? | C1 → `:593`(+`:594`,`:650`) · C2 → `:595`(+`:594`,`:650`) · C3 → `:571–583`,`:590`,`:651`,`:1919` · D1 → `:1919`, `srs-v3.5.md:75`,`:3550–3562`. **Tất cả tự mở file đọc ngày 2026-08-07 trên bản 2296 dòng** |
| 2 | Mọi thao tác dự kiến có trả lời một vế Cn hoặc là đối chứng độc lập không? | Có — §5, mỗi vế đúng 1 đường UI + 1 đối chứng. Không có thao tác nào ngoài 3 vế |
| 3 | Mọi vế `DIFF/GAP` đã bị chặn Pass và có câu hỏi BA đúng phần thiếu chưa? | **Không có vế nào ở `DIFF/GAP` trong chuẩn chấm.** D1 là `DIFF` so với **đề xuất TKM** nhưng BA **đã trả lời trong chính SRS hiện hành** ⇒ không mở câu hỏi BA mới, và D1 **không** dùng để chấm |
| 4 | Đã đọc đầy đủ expected và các phản hồi liên quan, không dựa trên bản cắt ngắn chưa? | Có — 2 gạch đầu dòng "Kết quả mong đợi", ô "Điều kiện", "Các bước thực hiện", "Loại vấn đề", "TKM phản hồi lần 1". `DEV phản hồi lần 1` trống. **Đọc lại bảng live trước khi chốt verdict** |
| 5 | Điều kiện đo có khớp tiền đề của case; nếu khác thì đã xử lý chưa? | Hai chênh lệch đã khai: (a) **env khác** (§7 bẫy 18 — ghi giới hạn hiệu lực); (b) **trạng thái khóa** — phiếu ghi "Đang diễn ra hoặc Đã kết thúc", SRS `:536` chỉ cho `DANG_DIEN_RA` ⇒ đo trên `DANG_DIEN_RA` (§7 bẫy 4, §8 mục 1) |

---

*Giai đoạn A khoá lúc 2026-08-07 · SRS đọc trực tiếp `srs-fr-03-dao-tao.md` (2296 dòng) + `srs-v3.5.md` (7012 dòng) · KHÔNG mở web, KHÔNG gọi chrome-devtools, KHÔNG curl app.*
