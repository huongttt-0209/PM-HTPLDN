# CHUẨN CHẤM — KTDGKQHT_05 · "Tải lên tệp Excel điểm danh" (lô F8, dòng 10 tab `bug`)

> **Nhánh xử lý:** phiếu này **KHÔNG chạy FLOW 04 từ đầu**. Theo
> [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md) **BƯỚC 0 mục 2** —
> *"Có entry **và** có khối CÁCH VERIFY → tách ra, không chạy flow này (chỉ cần chạy lại đúng khối đó)"* —
> ô `Kết quả verify` của dòng 10 đã có sẵn khối `── CÁCH VERIFY sau Dev fix ──` do QA viết lúc **02:20 ngày 07/08/2026**
> ([`KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt`](KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt)).
> ⇒ Việc của lượt này là **chạy lại đúng khối đó** theo
> [`KTDGKQHT_05-KICH-BAN-CHAY.md`](KTDGKQHT_05-KICH-BAN-CHAY.md).
>
> 🔴 **File này KHÔNG chấm verdict và KHÔNG mang theo kết luận cũ.** Nó chỉ khóa lại (a) quan hệ
> `MATCH/DIFF/GAP` từng vế + dòng SRS, (b) kết quả tự kiểm số dòng SRS trong lượt hôm nay.
> Verdict do lần đo mới quyết. Sau khi mở màn **cấm đổi quan hệ** để khớp kết quả đo (Flow 04 §BUG SCOPE LOCK luật 5).

---

## 1. Bảng đầu

| Hạng mục | Giá trị |
|---|---|
| **Bảng · tab · dòng** | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219) · **dòng 10** |
| **Mã TC** | `KTDGKQHT_05` — "Tải lên tệp Excel điểm danh" (Tuần 2) |
| **Trạng thái trên bảng** (chụp 07/08 ~11:3x) | `Trạng thái` (N) = **Fail** · `Dopai` (O) = `N/R` · `Trạng thái dev fix` (R) = **`Fixed`** · `Ảnh/vieo 1` = `KTDGKQHT_05.jpg` · `Kết quả verify` (T) = **ĐÃ CÓ nội dung + khối CÁCH VERIFY** |
| **🔴 Mâu thuẫn dữ liệu phải ghi nhận** | Xem §4 — ô R đang là `Fixed` trong khi QA đã kết luận **Reopen** lúc 02:20 cùng ngày |
| **Env đo** | `https://18.143.165.120.nip.io` (env **NỘI BỘ**) · API `.../api/v1` · MailHog `http://18.143.165.120:8025` |
| **Tài khoản lượt này** | **`cbnv_tw_03`** / `Test@1234` — CB Nghiệp vụ Trung ương (`CB_NV_TW`). **Đổi so với lần đo trước (`cbnv_tw_02`)** theo bộ `_03` của lô F8. Lock → fallback **cùng vai trò + cùng cấp** `cbnv_tw_04` → `cbnv_tw_05`; **cấm** đổi vai trò/cấp; ghi tài khoản thực dùng vào báo cáo |
| **Vai trò theo đặc tả** | CB NV / CB PD — `srs-fr-03-dao-tao.md:526` · quyền "Quản lý kết quả ĐT" `:534` (PRE-01) |
| **Màn đo** | SCR-III-02 — Chi tiết Khóa học → **Tab 4 "Điểm danh"** (`srs-fr-03-dao-tao.md:522`, `:1919`) |
| **SRS nguồn chuẩn (prompt chỉ định)** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **cấm** `input/srs-update-2026-5-5/`, `input/srs-v3/` |
| **Hồ sơ lần đo trước** | [`../../F5-flow04-2026-08-07/chuan/KTDGKQHT_05.md`](../../F5-flow04-2026-08-07/chuan/KTDGKQHT_05.md) (khóa chuẩn chấm) · [`../../F5-flow04-2026-08-07/do/KTDGKQHT_05.md`](../../F5-flow04-2026-08-07/do/KTDGKQHT_05.md) (nhật ký đo) · [`../../F5-flow04-2026-08-07/note/KTDGKQHT_05.md`](../../F5-flow04-2026-08-07/note/KTDGKQHT_05.md) (nội dung ô T) · ảnh `../../F5-flow04-2026-08-07/image/KTDGKQHT_05-0*.png` · tệp `../../F5-flow04-2026-08-07/seed-files/*KTDGKQHT_05*.xlsx` |

---

## 2. BẢNG KIỂM SỐ DÒNG SRS — tự mở file đếm lại 2026-08-07

**Đã tự mở:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`
— **2 296 dòng**, md5 `63f378eab606497c51f0c38c74420c89`, mtime `2026-08-04 17:17`.
Bản chốt Giai đoạn A hôm 07/08 cũng ghi 2 296 dòng + đúng md5 này ⇒ **file chưa bị sửa từ lần đo trước.**

> 🔴 Nếu lượt chạy sau thấy tổng số dòng ≠ 2 296 hoặc md5 khác → **đếm lại từ đầu**, không dùng bảng này.

| Số dòng khối cũ trích | Nội dung dòng đó **HIỆN TẠI** (trích rút gọn, đã tự đọc) | Còn đúng? |
|---|---|---|
| `:536` | `PRE-03` — *"**Nhập điểm danh:** khóa học ở `DANG_DIEN_RA`. Khi khóa chuyển `DA_KET_THUC` thì **điểm danh đóng**…"* | ✅ đúng |
| `:571` | *"**Processing — Tải mẫu (điểm danh / điểm kiểm tra)** `[KTDGKQHT_05 chốt 2026-08-04]`:"* | ✅ đúng |
| `:573` | *"Nhập liệu qua Excel theo cơ chế "Tải mẫu → điền → tải lên": cán bộ không tự gõ định danh học viên…"* | ✅ đúng |
| `:577` | Hàng bảng — *"Mẫu điểm danh \| "Tải mẫu điểm danh" (Tab 4) \| Buổi học đang chọn (`lich_hoc_id`) \| Đã chọn buổi + khóa `DANG_DIEN_RA` + khóa có ≥1 buổi học + có quyền nhập điểm danh"* | ✅ đúng |
| `:581` | Bộ cột mẫu điểm danh — *"`hoc_vien_id` (điền sẵn, khoá/ẩn — ID nội bộ opaque…) · Họ tên · Email · Đơn vị · **Trạng thái điểm danh** (trống — điền: Có mặt / Vắng có phép / Vắng không phép) · Ghi chú."* | ✅ đúng |
| `:583` | *"`lich_hoc_id` … được **nhúng ở vùng metadata/tiêu đề tệp** (không phải cột từng dòng)…"* | ✅ đúng |
| `:593` | Bước 5 Import — *"Hiển thị bản review (thành công / lỗi) — dòng lỗi ghi rõ mã lỗi + số dòng"* | ✅ đúng |
| `:594` | Bước 6 Import — *"Nếu xác nhận: merge kết quả — **chỉ merge dòng hợp lệ**, dòng lỗi bỏ qua"* | ✅ đúng |
| `:595` | Bước 7 Import — *"Trả về báo cáo import"* | ✅ đúng |
| `:640` | `E6` — *"Nhập điểm danh khi khóa không ở `DANG_DIEN_RA`… → `ERR-KQ-06` "Chỉ điểm danh được khi khóa học đang diễn ra""* | ✅ đúng |
| `:651` | AC — *"**Given** CB NV đã chọn buổi (Tab 4) hoặc đề kiểm tra (Tab 5) **When** nhấn "Tải mẫu" **Then** tải tệp Excel điền sẵn danh sách học viên + định danh, cột điểm danh/điểm kiểm tra để trống"* | ✅ đúng |
| `:652` | AC — *"**Given** CB NV tải lên tệp mẫu đúng buổi/đề đang chọn **When** import **Then** đối chiếu học viên theo định danh sẵn trong tệp, **merge dòng hợp lệ**"* | ✅ đúng |
| `:1919` | SCR-III-02 Tab 4 Điểm danh — bộ cột + *"nút **"Tải mẫu điểm danh"** (bật sau khi chọn buổi, khóa `DANG_DIEN_RA`, khóa có ≥1 buổi học, có quyền…)"* | ✅ đúng |

**⇒ 13/13 số dòng khối cũ trích đều CÒN ĐÚNG. Không có số dòng nào phải sửa.**

### Dòng bổ trợ đã tự đọc thêm trong lượt này (dùng cho bẫy chấm oan, không phải neo chấm mới)

| Dòng | Nội dung | Dùng để |
|---|---|---|
| `srs-fr-03-dao-tao.md:14` | Khối *"Sửa đổi 2026-08-04 … (KTDGKQHT_05)"* — chốt **giữ `hoc_vien_id` làm khoá đối chiếu, KHÔNG thêm trường vào entity HOC_VIEN** | Chặn FAIL oan "thiếu cột Mã học viên" |
| `:549` | `diem_danh` enum `CO_MAT / VANG_PHEP / VANG_KHONG_PHEP` | Chuẩn 3 giá trị của cột trạng thái |
| `:590` | Bước 2 Import — đọc `lich_hoc_id` từ **metadata tệp**, **bắt buộc khớp buổi đang chọn**; lệch → `ERR-KQ-09` | Vì sao cấm tự dựng tệp |
| `:592` | Bước 4 Import — *"**ERR-KQ-03: học viên phải TỒN TẠI VÀ THUỘC khóa đang thao tác**"* | Thiết kế dòng lỗi 1 |
| `:637` | `E3` `ERR-KQ-03` — *"Không tìm thấy học viên ở dòng {N} (định danh không hợp lệ hoặc không thuộc khóa học này)"* | Câu chữ kỳ vọng dòng lỗi 1 |
| `:638` | `E4` `ERR-KQ-04` — *"Giá trị điểm danh không hợp lệ"* | Câu chữ kỳ vọng dòng lỗi 2 |
| `:633–643` | Trọn bảng Error Handling `ERR-KQ-01…09` — **không có thông báo THÀNH CÔNG nào** | Căn cứ của `G1` §3 |
| `:659` | AC — khóa `DA_KET_THUC` → Tab 4 chỉ đọc | Bẫy chặn FAIL oan |
| `:660` | AC — chưa chọn buổi → *"Vui lòng chọn buổi học để bắt đầu điểm danh"* | Bẫy candidate (vế của KTDGKQHT_03) |
| `:1920–1923` | Bộ chọn buổi bắt buộc · trạng thái rỗng · chỉ đọc khi `DA_KET_THUC` | Tiền đề + bẫy |
| `srs-v3.5.md:75` (file 7 012 dòng) | Lịch sử 3.5.8 — *"Entity HOC_VIEN … **KHÔNG thêm `ma_hoc_vien`, khoá đối chiếu vẫn là `id`**"* | Trả lời TKM (`D1`) |
| `srs-v3.5.md:6760` | Quy ước H8 — *"**Không áp** cho tệp mẫu nhập liệu tải sẵn (vd "Tải mẫu điểm danh")"* | Chặn FAIL oan vì tên tệp mẫu |

---

## 3. BẢNG VẾ (BUG SCOPE LOCK) — quan hệ + dòng SRS, KHÔNG kèm verdict

> Nguồn tách vế: **C1, C2** từ ô `Kết quả mong đợi` (K) của đối tác. **C3** từ manh mối ô `TKM phản hồi lần 1` +
> `Loại vấn đề`, được nhận vào chuẩn chấm vì SRS có quy định thật (BA chèn cho chính case này ngày 04/08).
> **D1** là đề xuất của TKM — ghi để trả lời TKM, **không** phải tiêu chí chấm. **G1** là điểm đặc tả im lặng.
>
> Expected đối tác nguyên văn (ô K):
> - *"Hiển thị bản xem trước kết quả (số dòng hợp lệ, số dòng lỗi và lý do từng dòng)."*
> - *"Nạp thành công, hệ thống hiển thị thông báo "Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ"."*

| Vế | expected | SRS `file:dòng` | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C3** | Cán bộ có nguồn lấy định danh học viên **do hệ thống cấp**: nút "Tải mẫu điểm danh" sinh tệp điền sẵn `hoc_vien_id` + đúng bộ cột + metadata buổi *(đo TRƯỚC vì tệp mẫu là đầu vào của C1/C2)* | `srs-fr-03-dao-tao.md:571–583` · `:590` · `:651` · `:1919` | **MATCH** | **TEST** | **UI:** chọn buổi → bấm "Tải mẫu điểm danh" (bấm thật, tải thật). **Đối chứng:** mở tệp `.xlsx` bằng `openpyxl` — đọc bộ cột + số ô `hoc_vien_id` điền sẵn + cột trạng thái rỗng + metadata buổi |
| **C1** | "Hiển thị bản xem trước kết quả (số dòng hợp lệ, số dòng lỗi và **lý do từng dòng**)." | `srs-fr-03-dao-tao.md:593` (+ `:594`, `:650`) | **MATCH** | **TEST** | **UI:** nạp fixture → bấm "Kiểm tra tệp" → **dừng trước khi xác nhận** → đọc khối xem trước bằng `innerText`. **Đối chứng:** response body của chính request xem trước |
| **C2** | "Nạp thành công, hệ thống hiển thị thông báo …" — chấm theo **nội dung** (có báo cáo, có số nạp thành công + số không hợp lệ, số đúng), **KHÔNG** theo câu chữ | `srs-fr-03-dao-tao.md:595` (+ `:594`, `:652`) | **MATCH** | **TEST** | **UI:** cài `MutationObserver` **trước** khi bấm "Xác nhận import" → bắt thông báo bằng `innerText`, **cấm lọc trùng**. **Đối chứng:** đọc lại dữ liệu điểm danh của **đúng buổi** đó |
| **G1** | Đối tác kỳ vọng **đúng câu chữ** *"Đã nạp {số thành công} bản ghi thành công, {số lỗi} bản ghi không hợp lệ"* | `:595` chỉ ghi *"Trả về báo cáo import"*; bảng Error Handling `:633–643` **không có thông báo thành công nào** ⇒ **IM LẶNG về câu chữ** | **GAP** | **BA** | **Không đo.** Chỉ ghi lại câu chữ thực tế quan sát được ở C2 để BA có mốc |
| **D1** | *(không phải expected — ô `Loại vấn đề` + `TKM phản hồi lần 1`)*: "nếu thêm cột MHV có đc ko" / "Màn hình danh sách không hiển thị mã học viên" | `:1919` (bộ cột Tab 4 không có cột Mã học viên) · `:14` · `srs-v3.5.md:75` | **DIFF — nhưng BA ĐÃ trả lời ngay trong SRS hiện hành** (vá bằng cơ chế tệp mẫu C3, không phơi mã HV ra màn) | **KHÔNG mở câu hỏi BA mới**; chỉ trích SRS để trả lời TKM | **Không đo** |

### Chuẩn chấm từng vế (điều kiện ĐẠT — chốt trước khi mở màn)

**C3 ĐẠT khi đủ 3:** (1) Tab Điểm danh **có** nút "Tải mẫu điểm danh", **tắt** khi chưa chọn buổi và **bật** đúng điều kiện `:577`;
(2) tệp tải về mở được bằng `openpyxl`, đúng 6 cột `:581` đúng thứ tự, `hoc_vien_id` **điền sẵn** đủ học viên của khóa, cột "Trạng thái điểm danh" **rỗng 100%**;
(3) định danh buổi nằm ở **metadata/tiêu đề tệp**, không phải cột từng dòng (`:583`).

**C1 ĐẠT khi đủ 3:** (1) khối xem trước hiện ra **TRƯỚC** khi ghi dữ liệu (`:594` "Nếu xác nhận: merge" ⇒ xem trước là cổng xác nhận);
(2) **phân tách rõ** nhóm hợp lệ vs nhóm lỗi (đếm được cả hai);
(3) **mỗi dòng lỗi** có mã lỗi/lý do **+ số dòng**, và 2 dòng lỗi khác nguyên nhân phải ra **2 lý do KHÁC NHAU**.
Bộ ba số quyết định = **(3 hợp lệ, 2 lỗi, {2 lý do khác nhau gắn đúng số dòng})**, cộng khớp **3+0+2 = 5** = tổng dòng fixture.

**C2 ĐẠT khi đủ 3:** (1) sau khi xác nhận nạp, hệ thống **trả về/hiển thị báo cáo kết quả import**, không im lặng và không lỗi hệ thống;
(2) báo cáo cho biết **số bản ghi nạp thành công** + **số bản ghi không hợp lệ**;
(3) hai con số **đúng** với fixture (3/2) **và** khớp đối chứng: đúng **3** học viên đổi trạng thái đúng 3 giá trị đã điền, **2** học viên ở dòng lỗi **KHÔNG** được ghi (`:594`).

### 🔴 Hệ quả của `G1` đối với verdict — điểm phải hỏi điều phối TRƯỚC khi ghi ô R

Flow 04 §Verdict: **Pass** chỉ khi *"mọi vế đều `MATCH` … và **không còn vế `DIFF/GAP`**"*; **Cần BA** khi *"có `GAP` do SRS im lặng"*.
`G1` là `GAP` thật (đối tác kỳ vọng một câu chữ cụ thể mà SRS không quy định).
⇒ **Kể cả khi C1+C2+C3 đo ra đạt hết**, verdict logic **không phải Pass sạch** mà là *"phần đo được đạt + còn `G1` cần BA"*.
Lần đo 02:20 xếp `G1` là **"ghi chú mềm, không chặn bàn giao"** và ra verdict `Reopen` vì C2 hỏng, nên điểm này chưa phải quyết.
Lần này nếu C2 đạt thì **buộc phải quyết**, mà ô `R` chỉ nhận **một** giá trị (`Test done` \| `Reopen` \| `BA confirm`).
**⇒ Báo điều phối chọn trước khi ghi:** `Test done` + nêu `G1` trong ô `T`, hay `BA confirm`.
**Cấm** tự hạ `G1` từ `GAP` xuống `MATCH` để lấy `Test done` (Flow 04 §BUG SCOPE LOCK luật 5).

---

## 4. 🔴 MÂU THUẪN DỮ LIỆU PHẢI GHI NHẬN — ô `Trạng thái dev fix` = `Fixed`

| Mốc | Sự kiện |
|---|---|
| **07/08 02:08–02:20** | QA đo trên env nội bộ, bản dựng `assets/index-DsMHK7Dp.js` / nhãn `V1.0.9`, tài khoản `cbnv_tw_02` → kết luận **Reopen** (bước xác nhận nạp trả HTTP 500 `ERR-SYS-00-00-01`, 0/3 dòng hợp lệ được ghi), và ghi khối `CÁCH VERIFY` vào ô `Kết quả verify` |
| **07/08 ~11:3x** | Chụp phạm vi lô F8: ô `Trạng thái dev fix` (R) của dòng 10 đang là **`Fixed`**, không phải `Reopen` |

**Hai cách giải thích, không suy đoán được từ dữ liệu đang có:**
1. Dev đã sửa tiếp sau 02:20 và tự đặt lại ô R = `Fixed` (rất có thể — env này deploy liên tục, V1.0.8 → V1.0.10 trong ~10 giờ);
2. Ô R bị đặt lại/ghi đè do thao tác khác trên bảng.

**Hệ quả bắt buộc:** đây chính là lý do **phải chạy lại thật**, **cấm** suy verdict từ kết quả 02:20.
Mặt khác cũng **cấm** mặc định "dev đã fix" — Flow 04 §Ca biên: *"Dev mô tả fix ở chỗ khác với triệu chứng → vẫn chạy đủ luồng, đừng tin mô tả."*
Ô `DEV phản hồi lần 1` (S) **trống** ⇒ không có mô tả fix nào để đối chiếu.

**Việc phải làm khi bắt đầu lượt đo:** đọc lại **live** dòng 10 (ô `R`, `S`, `T`) ngay trước khi ghi verdict —
nguồn có thể đã đổi lần nữa. Nếu ô `T` đã bị người khác ghi đè thì **lưu bản cũ vào `audit/` trước**, không đè mất.

---

## 5. Tiền đề — phải kiểm lại, không mặc định còn dùng được

| # | Tiền đề | Căn cứ SRS | Trạng thái ghi nhận 02:20 07/08 | Phải kiểm lại gì |
|---|---|---|---|---|
| T1 | Khóa ở `DANG_DIEN_RA` | `:536` PRE-03 · `:640` · `:659` · `:1923` | `KH-QAW7-HOINGHI` — `a7480002-0000-4000-8000-000000000002` — "QAW7 — Hội nghị đối thoại DN 2026", thanh bước ở "Đang diễn ra" | **Còn `DANG_DIEN_RA` không?** Đã sang `DA_KET_THUC` → đổi khóa khác, **không** ép lùi trạng thái |
| T2 | Khóa có ≥1 buổi + đã chọn buổi | `:538` PRE-05 · `:1920` | 4 buổi; đo trên **Buổi 4** `bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2` (11/05/2026 14:00–16:00) | Buổi 4 còn tồn tại không |
| T3 | ≥4 học viên `Đã duyệt` **thuộc khóa** | `:592` (ERR-KQ-03 cần HV thuộc khóa) | 4 HV: `dbf62f06…b660` · `cd17f1b7…3458b` · `6feead91…27f53` · `56640d49…01162` | **Còn đủ 4 không?** Thiếu → duyệt thêm ở tab "Học viên" (còn 2 đăng ký `Chờ duyệt`: "Nguyễn Văn Ngọc", "QA Probe Email") và **khai mutate** |
| T4 | 1 `hoc_vien_id` của **khóa KHÁC** (ép ERR-KQ-03) | `:592`, `:637`, `:654` | `cccccccc-0000-4000-8000-000000000001` — "Nguyễn Văn Học Viên", khóa `DDD-KH-011`, `DA_DUYET` | Còn tồn tại + vẫn thuộc khóa khác? Không còn → lấy id khác từ danh sách HV của một khóa khác (đọc endpoint **đã lộ trên màn**, cấm đoán) |
| **T5** | **🔴 Buổi đo phải SẠCH (chưa có bản ghi điểm danh)** | `:594` (chỉ merge dòng hợp lệ) — phép đo "3 học viên đổi trạng thái" chỉ đọc được nếu biết mốc gốc | Mốc gốc 02:20: cả 4 HV `trangThai = null`, `id = ""` ⇒ buổi 4 **sạch**; và lần đó **0 bản ghi được ghi** (lỗi 500) ⇒ **về lý thuyết vẫn sạch** | **Phải đọc lại mốc gốc trước khi nạp.** Nếu có bản ghi rồi → xem §6 |
| T6 | Quyền + phạm vi đơn vị | `:534` PRE-01 · BR-AUTH-08 | Khóa thuộc phạm vi `CB_NV_TW`, đơn vị `BTP · TW` | `cbnv_tw_03` cùng vai trò + cấp ⇒ dự kiến thấy khóa; không thấy → kiểm đơn vị của tài khoản trước khi kết luận |
| T7 | Vân tay bản dựng | Flow 04 §Chuẩn bị bước 2 | `Last-Modified` `Thu, 06 Aug 2026 18:51:25 GMT` · etag `W/"6a74d7ad-428"` · bó mã `assets/index-DsMHK7Dp.js` · nhãn chân sidebar `V1.0.9` | Đo vân tay **đầu VÀ cuối** phiên; khác ⇒ nói rõ quan sát nào rơi trước/sau mốc deploy. Nhãn `V1.0.x` **không** phải định danh |

---

## 6. Rủi ro dữ liệu bẩn — tiền đề T5

Lần đo trước bấm "Xác nhận import" và **máy chủ trả 500 ⇒ 0 bản ghi được ghi** (đã đối chứng bằng
`GET …/diem-danhs?lichHocId=…`: cả 4 HV `trangThai = null`). Nên **Buổi 4 nhiều khả năng vẫn sạch**.
Nhưng **không được mặc định**: giữa 02:20 và bây giờ có deploy + có thể có tác nhân khác chạy thử.

**Quy tắc:** đọc mốc gốc **trước khi nạp**, rồi chọn nhánh:

| Mốc gốc đọc được | Xử lý |
|---|---|
| **0 học viên có `trangThai`** | ✅ Buổi sạch — dùng Buổi 4 như kịch bản |
| **Có ≥1 học viên đã mang `trangThai`** | ⚠️ Dữ liệu **không còn sạch**. Ưu tiên: (a) đổi sang **buổi khác của cùng khóa** (Buổi 1/2/3) đang sạch — tệp mẫu tải ở buổi nào thì mang `lich_hoc_id` buổi đó, không phải sửa gì; (b) hết buổi sạch → **khóa khác** đang `DANG_DIEN_RA`, có ≥1 buổi, ≥4 HV `Đã duyệt`; (c) hết cả hai → **vẫn đo được** nhưng phải chấm bằng **delta**: ghi mốc gốc từng học viên, sau khi nạp so từng người, chỉ tính "3 học viên đổi trạng thái **mới**". 🔴 Ghi mốc gốc vào `do/` trước khi bấm, nếu không thì **cấm chốt** |

**Cách kiểm bằng API (endpoint đã quan sát live lượt trước, không phải đoán):**

```bash
TOKEN=$(/tmp/login.sh cbnv_tw_03)     # in ra accessToken; idleTtl 30 phút
KH=a7480002-0000-4000-8000-000000000002
LH=bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2

# (1) mốc gốc điểm danh của đúng buổi — đếm bản ghi đã có trạng thái
curl -sk -H "Authorization: Bearer $TOKEN" \
  "https://18.143.165.120.nip.io/api/v1/khoa-hocs/$KH/diem-danhs?lichHocId=$LH" | python3 -m json.tool

# (2) danh sách đăng ký/học viên của khóa — đếm học viên Đã duyệt (T3) + soi HV khóa khác (T4)
curl -sk -H "Authorization: Bearer $TOKEN" \
  "https://18.143.165.120.nip.io/api/v1/khoa-hocs/$KH/dang-ky-dao-taos" | python3 -m json.tool
```

- `/tmp/login.sh` là tệp tạm, có thể đã bị dọn → nếu không còn, xem lại brief lô F8 §3 để dựng lại
  (login → lấy `otpToken` → lấy mã 6 số ở MailHog → `verify-otp` → `accessToken`).
- Bearer trả 401 → token của env này nằm ở cookie; đối chứng bằng `fetch(..., {credentials:'include'})`
  chạy trong chính tab đang đăng nhập.
- **Trạng thái khóa (T1) và danh sách buổi (T2):** endpoint **chưa quan sát trực tiếp** ở lượt trước ⇒
  **cấm đoán đường dẫn**. Đọc bằng UI (thanh bước + tab Lịch học) và/hoặc lấy đúng request mà chính màn gọi
  qua `list_network_requests`; cần tra thì đọc `/api/docs-json`.

---

## 7. Bẫy đã biết (giữ nguyên từ chuẩn chấm đã khóa — không phát minh thêm)

### Chặn FAIL oan
1. **Không** chấm Fail vì Tab Điểm danh thiếu cột "Mã học viên" — `:1919` chốt bộ cột không có nó; `:14` + `srs-v3.5.md:75` chốt **không** thêm `ma_hoc_vien`.
2. **Không** chấm Fail vì **câu chữ** thông báo khác chuỗi đối tác viết — `:595` chỉ ghi "Trả về báo cáo import"; chấm bằng **con số**. (Điểm câu chữ đi vào `G1` → BA, **không** thành Fail.)
3. **Không** chấm Fail vì khối xem trước thiếu con số tổng, nếu vẫn đếm được hai nhóm từ danh sách dòng (`:593` không đòi con số tổng).
4. **Không** chấm Fail khi thao tác bị chặn vì khóa đã `DA_KET_THUC` — `:536` + `:640` + `:659` + `:1923` **bắt buộc** chặn. Ô `Điều kiện` của phiếu ghi *"Đang diễn ra **hoặc Đã kết thúc**"* — **vế "Đã kết thúc" lệch SRS** ⇒ **phải đo trên `DANG_DIEN_RA`**.
5. **Không** chấm Fail vì tên tệp mẫu không theo khuôn H8 — `srs-v3.5.md:6760` loại trừ tường minh.
6. **Không** chấm Fail vì `hoc_vien_id` là UUID khó đọc — `:581` quy định đúng là "ID nội bộ opaque, cán bộ không sửa".
7. **Không** chấm Fail vì nhãn/slug tab lệch (`?tab=lich-hoc-diem-danh` của env đối tác). `:1919` ràng buộc **nội dung** tab, không ràng buộc slug.

### Chặn PASS oan
8. **Cấm Pass bằng quan sát tĩnh** — thấy nút "Tải mẫu", thấy khối xem trước 3/2 **không** kết luận được gì về C2. Phải **bấm xác nhận thật** rồi **đọc lại dữ liệu buổi học**.
9. Chữ người dùng nhìn thấy đọc bằng **`innerText`** (`textContent` gom node ẩn AntD → bug ma).
10. Bộ bắt thông báo **cấm lọc trùng**; cài **trước** khi bấm; **đếm kèm số request** phát sinh.
11. Một thông báo ra hai node (thẻ bọc + thẻ con) ⇒ **đếm theo mốc giờ khác nhau**, không theo độ dài mảng.
12. Các chiều số phải **cộng khớp**: hợp lệ + bỏ qua + lỗi = **5** = tổng dòng fixture. Không khớp ⇒ số đang sai, **chưa được chốt**.
13. **Hai phép đo mâu thuẫn** (màn nói 3, response nói 4; hoặc báo cáo nói 3 mà đọc lại chỉ 2) ⇒ **chưa chốt**, ghi cả hai, hỏi điều phối.
14. **Tab mở lâu vẫn chạy mã cũ** ⇒ tải lại trang trước lô đo + ghi vân tay bản dựng (T7).
15. **Giới hạn hiệu lực verdict:** đối tác đo trên `htpldn-uat.ospgroup.vn` (V1.0, 24/07); lô này đo trên `18.143.165.120.nip.io`. Câu giới hạn hiệu lực **bắt buộc** có trong ô `Kết quả verify`.
16. **Cấm mở rộng** thành hồi quy nhập tay, ma trận CRUD, mọi vai trò, Tab 5 "Kết quả kiểm tra".

### Ghi nhận, không mở phép đo (candidate một dòng)
17. Bảng điểm danh render đầu cột với thân rỗng khi **chưa chọn buổi** (SRS `:660`, `:1921` đòi dòng *"Vui lòng chọn buổi học để bắt đầu điểm danh"*) là vế của **KTDGKQHT_03**, **không** thuộc phiếu này ⇒ tái xuất hiện thì ghi **candidate một dòng**, không điều tra, không đổi verdict.

---

*Khóa lúc 2026-08-07 · SRS tự mở đọc `srs-fr-03-dao-tao.md` (2 296 dòng, md5 `63f378eab606497c51f0c38c74420c89`) + `srs-v3.5.md` (7 012 dòng) · KHÔNG mở trình duyệt, KHÔNG gọi chrome-devtools, KHÔNG gọi API ứng dụng trong lượt soạn này.*
