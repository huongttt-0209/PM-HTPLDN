# FLOW 04 · lô F5-flow04-2026-08-07 — 4 case

**Bảng:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219)
**Môi trường đo:** `https://18.143.165.120.nip.io` (env NỘI BỘ) · MailHog `http://18.143.165.120:8025`
**SRS nguồn chuẩn (prompt chỉ định):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Tài khoản:** bộ `_02` (`cbnv_tw_02` / `Test@1234`) — nguồn `output/UAT_doi-tac/input/input.md`

**Ánh xạ ghi bảng (prompt quyết định, flow không được tự mở rộng):**

| Verdict logic Flow 04 | Ô `Trạng thái dev fix` |
|---|---|
| Pass | `Test done` |
| Reopen | `Reopen` |
| Cần BA | `BA confirm` |

Diễn giải → ô `Kết quả verify`.
**Ô CHỈ ĐỌC, cấm ghi đè:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.

> ⚠️ Prompt KHÔNG cấp ô cho ảnh bằng chứng vòng verify (`Ảnh/video verify` không nằm trong ánh xạ).
> ⇒ Không ghi cột đó. Link ảnh xem được (Drive) nhúng **trong chính ô `Kết quả verify`**.

---

## BƯỚC 0 — chốt phạm vi (đọc live 2026-08-07)

### Trạng thái bảng lúc bắt đầu

| Dòng | Mã TC | Mô tả | Trạng thái | Dopai | Trạng thái dev fix | DEV phản hồi lần 1 | Kết quả verify | Ảnh/vieo 1 |
|---:|---|---|---|---|---|---|---|---|
| 10 | KTDGKQHT_05 | Tải lên tệp Excel điểm danh | Fail | `N/R` | `Fixed` | *(trống)* | *(trống)* | `KTDGKQHT_05.jpg` ✅ tải được |
| 13 | QLKTLBG_19 | Xuất excel không có điều kiện lọc | Fail | `N/R` | `Fixed` | *(trống)* | *(trống)* | **RỖNG** |
| 14 | QLKTLBG_20 | Xuất Excel với điều kiện lọc không có kết quả | Fail | `N/R` | `Fixed` | *(trống)* | *(trống)* | **RỖNG** |
| 20 | QLLKHDTBD_09 | Xuất Excel với điều kiện lọc | Fail | `dev done` | `Fixed` | *(trống)* | *(trống)* | `QLLKHDTBD_09.webm` ✅ + `QLLKHDTBD_09_v2.jpg` (gắn ở ô TKM) ✅ |

- Cột `Kết quả verify` **trống ở cả 4 dòng** ⇒ không có nội dung cũ để đè, không cần hồ sơ `audit/`.
- Cột `Tác nhân` trống ở cả 4 dòng ⇒ vai trò lấy theo ghi chú tiêu đề bảng (bộ `cbnv_*`), cấp TW.
- Dòng 20 có `Kết quả thực tế` = *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"*; 3 dòng còn lại trống.

### Phân nhánh Flow 03 vs Flow 04

Đã grep toàn bộ `output/` tìm bug entry + khối `CÁCH VERIFY` cho 4 mã:

| Mã TC | Có bug entry nội bộ? | Có khối `CÁCH VERIFY`? | Nhánh |
|---|---|---|---|
| KTDGKQHT_05 | không (chỉ 1 phiếu bàn giao tuần 4 + 1 ghi chú số dòng SRS) | ❌ | **Flow 04** |
| QLKTLBG_19 | không | ❌ | **Flow 04** |
| QLKTLBG_20 | không | ❌ | **Flow 04** |
| QLLKHDTBD_09 | có — `BUG-QLLKHDTBD_09` (**Closed** 2026-08-04, vế *bỏ qua bộ lọc*) | ❌ | **Flow 04** |

⇒ **4/4 đúng nhánh Flow 04.** Không case nào phải tách sang Flow 03.

🔴 **Cảnh báo riêng dòng 20 — vế đang tranh chấp KHÁC vế đã đóng.**
`BUG-QLLKHDTBD_09` (đóng 04/08) là vế *tệp xuất bỏ qua bộ lọc*. Ô `TKM phản hồi lần 1` vòng này nêu vế MỚI:
*"File excel được xuất thiếu trường thông tin Người tạo, Ngày tạo"*. Cấm chép verdict cũ sang; phải khoá lại
chuẩn chấm cho ĐÚNG vế đang tranh chấp.

### Cổng bằng chứng

| Dòng | Bằng chứng | Xử lý |
|---:|---|---|
| 10 | `partner-evidence/KTDGKQHT_05.jpg` (207 KB) | mở full-res trước khi đo |
| 13 | **không có** | Flow 04 §Cổng bằng chứng: thiếu bằng chứng **nhưng tự tái hiện được** (2 bước, không cần tiền đề riêng) ⇒ chạy tiếp, ghi rõ điều kiện đã tái hiện |
| 14 | **không có** | như trên |
| 20 | `partner-evidence/QLLKHDTBD_09.webm` (4.4 MB) + `partner-evidence/QLLKHDTBD_09_v2.jpg` (320 KB) | trích frame tới khoảnh khắc lỗi |

### Vân tay bản dựng phải đối chiếu ở đầu mỗi lượt đo

Đo lúc **2026-08-07 01:47 giờ VN** (`GET /` trên env nội bộ):

| Hạng mục | Giá trị |
|---|---|
| `GET /` last-modified | `Thu, 06 Aug 2026 17:39:54 GMT` (00:39 giờ VN 07/08) |
| `GET /` etag | `W/"6a74c6ea-428"` |
| Bản dựng suy ra | **V1.0.10** · bó mã `assets/index-B2W2Krcs.js` (theo `F3-devfix-2026-08-07/TIEN-DO.md`) |
| Máy chủ | `nginx/1.27.5` sau `Caddy` |

🔴 Env này **deploy liên tục** (V1.0.8 → V1.0.9 → V1.0.10 trong ~10 giờ). Mọi agent đo BẮT BUỘC ghi vân tay
đầu phiên; khác V1.0.10 ⇒ báo điều phối trước khi chốt.

### Giới hạn hiệu lực verdict

Đối tác đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` (bản `HTPLDN · V1.0`). Lô này đo trên env nội bộ
`18.143.165.120.nip.io` (V1.0.10) theo đúng chỉ định của prompt ⇒ mọi verdict chỉ có hiệu lực cho bản dựng
và env đã đo; phải ghi câu giới hạn này vào ô `Kết quả verify`.

---

## Lịch chạy (TUẦN TỰ — mỗi thời điểm chỉ MỘT agent gọi chrome-devtools)

| Lượt | Dòng | Mã TC | Giai đoạn A (chuẩn chấm) | Giai đoạn B (đo) | Ghi bảng + đọc lại |
|---|---:|---|---|---|---|
| 1 | 10 | KTDGKQHT_05 | ✅ | ✅ | ✅ |
| 2 | 13 | QLKTLBG_19 | ✅ | ✅ | ✅ |
| 3 | 14 | QLKTLBG_20 | ✅ | ✅ | ✅ |
| 4 | 20 | QLLKHDTBD_09 | ✅ | ✅ | ✅ |

**LÔ HOÀN TẤT 4/4** — mỗi case chạy trọn chu trình *đo → viết report → ghi bảng → đọc lại xác nhận* rồi mới sang case kế.

### Kết quả Giai đoạn A — quan hệ đã KHOÁ (cấm đổi sau khi mở màn)

| Dòng | Vế | Quan hệ | Dòng SRS quyết định |
|---:|---|---|---|
| 10 | C1 xem trước · C2 báo cáo sau nạp · C3 tệp mẫu | MATCH ×3 | `srs-fr-03-dao-tao.md:593` · `:595` · `:571-583` |
| 10 | D1 đề xuất thêm cột "Mã học viên" của TKM | DIFF — **BA đã trả lời sẵn trong SRS hiện hành** (`srs-v3.5.md:75` chốt KHÔNG thêm) ⇒ không mở câu hỏi BA mới, không dùng để chấm | |
| 13 | C1 có chức năng Xuất Excel · C2 tệp chứa toàn bộ danh sách | MATCH ×2 | `srs-fr-03-dao-tao.md:1952` + `srs-v3.5.md:5570` (BR-DATA-06, Áp dụng = "Toàn bộ CRUD list") |
| 14 | C1 có chức năng Xuất Excel · C2a tệp 0 dòng theo lọc | MATCH ×2 | như trên |
| 14 | C2b nhánh "hiển thị thông báo không có dữ liệu" | **GAP** — SRS Nhóm III im lặng ca 0 kết quả | đã đọc trọn FR-III-07 `:744-818`, FR-III-08 `:821-877`, SCR-III-03 `:1941-1984` |
| 20 | C1 tệp xuất theo đúng bộ lọc | MATCH | `srs-v3.5.md:5570` · `srs-fr-03-dao-tao.md:1775` · `:1175` · `:2243` |
| 20 | C2 tệp có trường Người tạo / Ngày tạo | **GAP** — `:1795-1796` là đặc tả BẢNG TRÊN MÀN, không phải tệp xuất; `Outputs` FR-III-14 `:1189-1200` KHÔNG có 2 trường đó | ⇒ **cấm Pass/Reopen vế này**, phải BA confirm |

### Quyết định điều phối

1. **Dropdown ô `Trạng thái dev fix` là strict one-of** — chỉ nhận: `In Progress · Fixed · UAT done · Bug · Test done · reject · Reopen · BA confirm`. **Không ghi được đa-trạng thái.** Case ra "Reopen + cần BA" ⇒ ghi `Reopen` (việc actionable cho dev), khối `CẦN BA CONFIRM:` đặt trọn trong ô `Kết quả verify`.
2. **Ô `Ảnh/video verify` KHÔNG nằm trong ánh xạ prompt ⇒ không ghi.** Link Drive xem được nhúng thẳng trong ô `Kết quả verify`.
3. **Dòng 14 — bảng quyết định vế C2 KHOÁ TRƯỚC KHI ĐO** (expected là mệnh đề HOẶC, phải chốt cách xử trước để không chấm theo kết quả):
   - Web **xuất tệp 0 dòng** → đạt nhánh (a), nhánh (a) có neo SRS `:5570` ⇒ vế C2 **đạt**, không phát sinh câu hỏi BA.
   - Web **chặn xuất + báo "không có dữ liệu"** → đạt expected qua nhánh (b), nhưng SRS im lặng ⇒ **GAP**, verdict `BA confirm`, không Reopen.
   - Web **xuất tệp chứa toàn bộ danh sách** (bỏ qua lọc) → **Reopen** (trái cả SRS lẫn expected).
   - **Không có nút Xuất Excel** → **Reopen** (vế C1, `:1952` nói rõ).
4. **Vân tay bản dựng đã ĐỔI lần nữa trong lúc chạy lô** — xem bảng dưới.

### Vân tay bản dựng thực đo

| Mốc | last-modified | etag | Bó mã FE | Chuỗi phiên bản |
|---|---|---|---|---|
| Điều phối, 01:47 giờ VN 07/08 | `Thu, 06 Aug 2026 17:39:54 GMT` | `W/"6a74c6ea-428"` | (suy ra `index-B2W2Krcs.js`) | V1.0.10 |
| **Lượt 1 đo, 02:08–02:20 giờ VN 07/08** | **`Thu, 06 Aug 2026 18:51:25 GMT`** | **`W/"6a74d7ad-428"`** | **`assets/index-DsMHK7Dp.js`** | **`V1.0.9`** |

🔴 Có deploy MỚI sau mốc V1.0.10, nhưng chuỗi phiên bản chân sidebar lại lùi về `V1.0.9` ⇒ **chuỗi phiên bản trên màn KHÔNG đáng tin làm vân tay**. Dùng `last-modified` + `etag` + bó mã FE. Mọi lượt sau đối chiếu với dòng "Lượt 1 đo".

## Kết quả

| Dòng | Mã TC | Verdict logic | Ô `Trạng thái dev fix` | Đọc lại khớp | Ô `Kết quả verify` |
|---:|---|---|---|---|---|
| 10 | KTDGKQHT_05 | 🔁 **Reopen** | `Reopen` | ✅ | 6790 ký tự · 3 link Drive · có khối CÁCH VERIFY |
| 13 | QLKTLBG_19 | ✅ **Pass** | `Test done` | ✅ | 5497 ký tự · 2 link Drive |
| 14 | QLKTLBG_20 | ✅ **Pass** | `Test done` | ✅ | 6237 ký tự · 1 link Drive |
| 20 | QLLKHDTBD_09 | ⚠️ **Cần BA** | `BA confirm` | ✅ | 7566 ký tự · 3 link Drive · có câu `CẦN BA CONFIRM` |

**Ô CHỈ ĐỌC — đã đọc lại kiểm chứng 4/4 dòng NGUYÊN VẸN:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.
**Ô `Ảnh/video verify`:** không ghi (ngoài ánh xạ prompt). Link ảnh nhúng trong `Kết quả verify`.
**Drive:** 10 ảnh, thư mục `UAT HTPLDN - bang chung QA - reverify Task-cai-tien 2026-07-31` (`1aUwKffPXhgx21D1e8EPHOygTlWOLYl_P`), chia sẻ *ai có link đều xem được*. Sổ link: `tools/evidence_drive_links_f5flow04.json`.

---

## Bàn giao cuối

### Bản dựng — env deploy 4 lần trong lúc chạy lô

| Mốc | last-modified | etag | Bó mã FE | Chuỗi phiên bản trên màn |
|---|---|---|---|---|
| Điều phối 01:47 | `06 Aug 17:39:54 GMT` | `W/"6a74c6ea-428"` | (`index-B2W2Krcs.js`) | V1.0.10 |
| **Dòng 10** đo 02:08–02:20 | `06 Aug 18:51:25 GMT` | `W/"6a74d7ad-428"` | `index-DsMHK7Dp.js` | V1.0.9 |
| **Dòng 13** đo 02:30–02:36 | `06 Aug 19:23:01 GMT` | `W/"6a74df15-428"` | `index-D4Buvu4S.js` | V1.0.9 |
| **Dòng 14** đo 02:44–02:49 | `06 Aug 19:23:01 GMT` | `W/"6a74df15-428"` | `index-D4Buvu4S.js` | V1.0.9 |
| **Dòng 20** đo 03:00–03:07 | `06 Aug 19:23:01 GMT` | `W/"6a74df15-428"` | `index-D4Buvu4S.js` | V1.0.9 |

🔴 **Chuỗi phiên bản trên màn KHÔNG dùng làm vân tay được** — lùi từ `V1.0.10` về `V1.0.9` trong khi bó mã lại mới hơn. Vân tay tin cậy = `last-modified` + `etag` + bó mã FE.
🔴 **Dòng 10 đo trên bản dựng KHÁC 3 dòng còn lại** (`index-DsMHK7Dp.js` vs `index-D4Buvu4S.js`) — verdict Reopen dòng 10 chỉ có hiệu lực cho bản dựng đó; nếu dev nói đã fix ở bản sau thì phải đo lại.

### Dữ liệu đã seed / mutate trên env `18.143.165.120.nip.io`

| Dòng | Mutate |
|---:|---|
| 10 | Duyệt 2 đăng ký học viên `Chờ duyệt → Đã duyệt` trên khóa `KH-QAW7-HOINGHI` (`a7480002-…-0002`): `2c87b577-…-9311e`, `b7745c2c-…-41858`. Không tạo khóa/buổi mới. |
| 13 · 14 · 20 | **KHÔNG mutate gì** — chỉ đọc, lọc, xuất tệp. |

Không đụng dữ liệu đối tác ở bất kỳ case nào.

### Bug mới / candidate

**Bug mới đã xác nhận: KHÔNG có.** Riêng dòng 20 đã chủ động kiểm điểm nghi ngờ nhất — **bảng trên màn CÓ đủ cột `Người tạo` + `Ngày tạo`** đúng `srs-fr-03-dao-tao.md:1795-1796` (đã cuộn bảng sang phải chụp lại để không kết luận nhầm do khuất tầm nhìn) ⇒ khoảng trống chỉ ở tệp xuất, đúng phạm vi vế C2 (GAP → BA), không tách bug mới.

**Candidate (chỉ ghi nhận, KHÔNG điều tra trong lô này — đúng gate Flow 04):**

1. **Tài liệu SRS:** bảng §6 `srs-fr-03-dao-tao.md:2243` liệt kê `BR-DATA-06` chỉ cho FR-III-01/05/06/14, **thiếu FR-III-07/08**, trong khi `:1952` lại dẫn thẳng BR-DATA-06 cho màn Kho tài liệu/Bài giảng. Đây là mục lục tham chiếu chéo (không phải mệnh đề ngoại lệ) — đề nghị BA bổ sung cho khớp. *(2 agent độc lập cùng ghi nhận.)*
2. **Phân quyền (dòng 13):** bộ quyền `cbnv_tw_02` có 18 quyền `export_*` nhưng **không có `export_bai_giang`**, thao tác xuất vẫn trả 200. Cần đổi vai trò mới xác nhận ⇒ ngoài phạm vi vế Cn.
3. **Độ phủ phép đo (dòng 20):** chưa tách bạch được "xuất toàn bộ tập sau lọc" với "xuất đúng dòng của trang đang xem", vì mọi `M` (4, 1) lẫn `N` (14) đều nhỏ hơn cỡ trang 20. Muốn xác nhận phải seed ≥7 bản ghi hoặc đổi cỡ trang — ngoài vế đối tác nêu. **Đã khai giới hạn này trong ô `Kết quả verify`** để không ai đọc kết quả rộng hơn thực tế.

### Câu hỏi BA đang mở — 1 case

**Dòng 20 `QLLKHDTBD_09`** — danh mục cột của tệp Excel xuất từ màn Kế hoạch đào tạo. Nội dung đầy đủ trong `note/QLLKHDTBD_09.md` (đã ghi lên ô `Kết quả verify`). Tóm tắt: đối tác kỳ vọng tệp có `Người tạo` + `Ngày tạo`; SRS `srs-fr-03-dao-tao.md:1189-1200` (`Outputs — Danh sách` của FR-III-14) **không liệt kê** 2 trường đó, và không có câu nào nói tệp xuất = cột của bảng trên màn; đối chứng FR-III-05 `:609-625` cho thấy SRS **biết cách** đặc tả bộ cột tệp xuất khi muốn. ⇒ **GAP, không phải lỗi dev.** Mục đích câu hỏi: **bổ sung vào đặc tả**, không chặn bàn giao.

### Case Chưa chốt: KHÔNG có (4/4 đều ra verdict).

---

### Chi tiết dòng 10 (Reopen)
- **Đạt:** C3 tệp mẫu (5/5) · C1 bản xem trước (3/3 — màn `Tổng 5 / Hợp lệ 3 / Bỏ qua 0 / Lỗi 2`, đối chứng response `total 5, success 3, errors 2`).
- **Không đạt:** C2 — `POST /diem-danhs/import/confirm` **HTTP 500 `ERR-SYS-00-00-01`** (requestId `6415303f-0248-42b0-b314-defb9492ce64`), đọc lại buổi học: **0/3 dòng hợp lệ được ghi**. Trái `:594` `:595` `:652`.
- **Không có vế DIFF/GAP** ⇒ không có câu `CẦN BA CONFIRM`.
- **Đã mutate env:** duyệt 2 đăng ký học viên `Chờ duyệt → Đã duyệt` trên khóa `KH-QAW7-HOINGHI` (`a7480002-…-0002`) — `2c87b577-…-9311e`, `b7745c2c-…-41858`. Không tạo khóa/buổi mới, không đụng dữ liệu đối tác.
- **Bug mới/candidate:** không có (lỗi 500 thuộc chính vế C2).
