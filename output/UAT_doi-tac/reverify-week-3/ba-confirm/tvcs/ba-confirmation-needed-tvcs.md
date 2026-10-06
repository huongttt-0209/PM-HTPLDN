# BA confirmation needed — TVCS — UAT tuần 3 — 2026-07-21

> Tài liệu tổng hợp các nội dung cần BA xác nhận của module TVCS từ 6 nhóm kiểm thử UAT tuần 3. Nội dung chi tiết, citation, evidence và đề xuất QA được giữ nguyên từ các file nguồn.

---

## Nhóm A — Màn danh sách SCR-X1-01

> **File này để làm gì:** gom các testcase mà QA không tự chốt verdict được hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh.

> **Citation:** SRS v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`.

---

### QLNDTVVCG_40 — Xuất Excel danh sách TVCS: tên tệp + tập cột đối tác kỳ vọng khác với SRS (SRS silent về export)

**Bối cảnh testcase**

- Dòng Excel: 290, mã TC `QLNDTVVCG_40`.
- Nội dung kiểm tra: Cán bộ Nghiệp vụ bấm nút **[Xuất Excel]** trên màn Danh sách Tư vấn pháp luật chuyên sâu (SCR-X1-01).
- Expected trong file UAT (kỳ vọng đối tác):
  - Tệp tải về theo điều kiện lọc hiện tại, gồm **toàn bộ cột đang hiển thị** trên màn cộng thêm cột **"Nội dung tư vấn (đầy đủ)"** và **"Ngày hoàn thành"**.
  - Tên tệp dạng **`TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx`**.
- Actual đối tác ghi: tên tệp không giống thiết kế; tệp Excel thiếu các cột **Doanh nghiệp, Chuyên gia, Lĩnh vực** so với màn danh sách.

**Đối chiếu SRS v3.5**

- FR-X.1-01 (UC147) — màn SCR-X1-01: khu tiêu đề trang có nút **[Xuất Excel]** (đặc tả xác nhận nút tồn tại), nhưng **KHÔNG có mục Processing/Outputs nào quy định tên tệp hay danh sách cột export** cho danh sách TVCS.
- Phần **"Processing — Xuất Excel"** duy nhất trong file SRS này (columns = mã hồ sơ, tên, DN, loại, ngày cấp, hết hạn, trạng thái, cơ quan cấp; format `HSPL-{date}-{seq}`) nằm trong **FR-X.1-04 (UC150) — Quản lý hồ sơ pháp lý doanh nghiệp**, KHÔNG áp cho màn danh sách TVCS.
- Kết luận: **SRS im lặng (silent)** về định dạng tên tệp và tập cột export của danh sách TVCS → không có clause để khẳng định app sai.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1090` (nút [Xuất Excel] trên SCR-X1-01)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:632`–`640` (Processing — Xuất Excel thuộc FR-X.1-04/UC150 Hồ sơ pháp lý DN, không phải TVCS)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:529` (mốc bắt đầu FR-X.1-04)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw_01` / `CB_NV_TW` (đơn vị BTP·TW).
- Mở `/tv-chuyen-sau/danh-sach`, bấm **[Xuất Excel]** khi danh sách có 1 bản ghi (TVCS-SEED-0001).
- Endpoint export `GET /api/v1/noi-dung-tu-van-cs/export?page=1&pageSize=20` trả **200**, tải về tệp `.xlsx` hợp lệ (6.798 bytes) có dữ liệu → **chức năng export hoạt động, không bị chặn**.
- **Tên tệp thực tế:** `noi-dung-tu-van-cs-20260721.xlsx` (không có phần giờ-phút, prefix khác kỳ vọng đối tác).
- **Cột trong tệp thực tế:** `Mã tư vấn | Nội dung | Trạng thái | Ngày tạo | Ngày bắt đầu | Ngày hoàn thành | Điểm đánh giá` (7 cột).
- So với màn danh sách (Mã tư vấn / Doanh nghiệp / Chuyên gia / Lĩnh vực / Tiêu đề / Trạng thái / Ngày bắt đầu / Ngày tạo): tệp export **thiếu** Doanh nghiệp, Chuyên gia, Lĩnh vực, Tiêu đề; **thêm** các cột Nội dung, Ngày hoàn thành, Điểm đánh giá không có trên màn.
- Evidence: `../../reverify-audit/QLNDTVVCG_40/export-actual.xlsx` · `../../reverify-audit/QLNDTVVCG_40/export-headers.txt`

**Kết luận QA**

- `QLNDTVVCG_40` **không kết luận được là bug theo SRS v3.5** vì SRS không quy định tên tệp và tập cột export cho danh sách TVCS.
- Quan sát của đối tác về thực tế là **đúng** (tên tệp khác, tệp thiếu cột Doanh nghiệp/Chuyên gia/Lĩnh vực) — đây là **tranh chấp đặc tả (UX design)**, không phải bất đồng về thực tế.
- Chức năng export **không lỗi** (tải file được, có dữ liệu) → không phải Open kiểu chặn chức năng.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt đặc tả export danh sách TVCS (SRS đang silent):

- (1) Tên tệp export danh sách TVCS phải theo định dạng nào? (đối tác đề xuất `TVCS-danh-sach-{YYYYMMDD-HHmm}.xlsx`; hiện app dùng `noi-dung-tu-van-cs-{YYYYMMDD}.xlsx`).
- (2) Tệp export phải gồm những cột nào — có bắt buộc thêm **Doanh nghiệp / Chuyên gia / Lĩnh vực / Tiêu đề** (đang hiển thị trên màn) không?
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt yêu cầu tên tệp + cột theo kỳ vọng đối tác → gửi Dev FE/BE bổ sung; nếu BA chấp nhận thiết kế hiện tại → cập nhật lại expected của testcase.

---

## Nhóm B — Form Thêm/Sửa SCR-X1-02

> **File này để làm gì:** gom các testcase mà QA không tự chốt verdict được hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh.

> **Citation:** SRS v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`.

---

### QLNDTVVCG_06 — Form Thêm TVCS: "Ngày tư vấn" không mặc định hôm nay + thiếu trường "Cơ quan tiếp nhận" (web khớp SRS, kỳ vọng đối tác khác đặc tả)

**Bối cảnh testcase**

- Dòng Excel: 279, mã TC `QLNDTVVCG_06`.
- Nội dung kiểm tra: Cán bộ Nghiệp vụ mở form **Thêm yêu cầu Tư vấn pháp luật chuyên sâu** (SCR-X1-02), kiểm tra giá trị mặc định và các trường của form.
- Expected trong file UAT (kỳ vọng đối tác):
  - Trường **"Ngày tư vấn"** phải tự điền mặc định = **ngày hôm nay**.
  - Form phải có trường **"Cơ quan tiếp nhận"** để nhập/hiển thị.
- Actual đối tác ghi: "Ngày tư vấn" để trống (không default); form không có trường "Cơ quan tiếp nhận".

**Đối chiếu SRS v3.5**

- Trường `ngay_tu_van` (Inputs): kiểu date, bắt buộc, **cột "Mặc định" = "—" (không quy định giá trị mặc định)** → SRS không yêu cầu default = hôm nay.
- Trường `don_vi_id` (đơn vị tiếp nhận): khi **CB nhập tay** thì `don_vi_id = đơn vị của CB đang đăng nhập` (gán TỰ ĐỘNG), không phải trường cán bộ nhập/chọn trên form.
- Danh sách thành phần form (Accordion "Thông tin cơ bản") gồm: Mã nội dung / DN / Chuyên gia / Lĩnh vực PL / Ngày tư vấn / Ghi chú — **KHÔNG liệt kê trường "Cơ quan tiếp nhận"** để cán bộ nhập tay.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:116` (`ngay_tu_van` — cột Mặc định = "—", không default)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:118` (`don_vi_id` — CB nhập tay ⇒ don_vi_id = đơn vị CB đang đăng nhập, auto)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1142` (Accordion "Thông tin cơ bản" — không có trường "Cơ quan tiếp nhận")

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw_02` / `CB_NV_TW` (đơn vị BTP·TW).
- Mở `/tv-chuyen-sau/tao-moi` (form Thêm mới).
- Trường **"Ngày tư vấn"** để trống (không tự điền hôm nay) — **đúng như đối tác quan sát**.
- Form **không có trường "Cơ quan tiếp nhận"** — **đúng như đối tác quan sát**.
- Đối chiếu SRS: cả 2 điểm này web hiện tại đang **khớp đặc tả** (SRS không yêu cầu default ngày, đơn vị tiếp nhận gán tự động ẩn khỏi form).
- Evidence: `../bug-reports/tvcs/image/tvcs-batchB-form-them-nhom1-2.png`

**Kết luận QA**

- `QLNDTVVCG_06` **không phải bug theo SRS v3.5**: web hiện tại khớp đặc tả ở cả 2 điểm.
- Quan sát của đối tác về thực tế là **đúng** (ngày để trống, không có ô Cơ quan tiếp nhận), nhưng **kỳ vọng** của đối tác (có default ngày + có ô Cơ quan tiếp nhận) **khác với SRS** — đây là tranh chấp đặc tả, không phải bất đồng về thực tế.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt 2 điểm (SRS hiện không yêu cầu, nhưng có thể là cải tiến UX hợp lý):

- (1) Trường **"Ngày tư vấn"** có cần mặc định = ngày hôm nay không? (SRS để "—"; đối tác muốn default hôm nay).
- (2) Form có cần **hiển thị "Cơ quan tiếp nhận"** (dạng chỉ đọc, = đơn vị của CB đang đăng nhập) để cán bộ thấy rõ không? (SRS gán tự động, không đưa lên form).
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt theo kỳ vọng đối tác → gửi Dev FE bổ sung (default ngày + field read-only); nếu BA giữ nguyên đặc tả → cập nhật lại expected của testcase theo SRS.

---

### QLNDTVVCG_08 (mục phụ) — Form Thêm TVCS có trường "Vụ việc liên kết (tùy chọn)" không nằm trong danh sách Inputs của form (SRS mâu thuẫn nội bộ: form spec im lặng, ERD có FK)

> Bug chính của `QLNDTVVCG_08` (Nội dung tư vấn là textarea không phải Rich Text Editor) đã log Open tại `../../bug-reports/tvcs/Pass-bug-report-tvcs-batchB.md`. Mục dưới đây **chỉ tách riêng** điểm cần BA xác nhận (trường "Vụ việc liên kết" thừa so với form spec), không thuộc phạm vi bug.

**Bối cảnh testcase**

- Dòng Excel: 281, mã TC `QLNDTVVCG_08`.
- Nội dung kiểm tra: Cán bộ Nghiệp vụ mở form **Thêm yêu cầu TVCS** (SCR-X1-02), rà soát các trường form so với đặc tả.
- Ghi nhận thực tế: form có thêm trường **"Vụ việc liên kết (tùy chọn)"**.

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw_02` / `CB_NV_TW` (đơn vị BTP·TW).
- Mở `/tv-chuyen-sau/tao-moi`.
- Form hiển thị trường **"Vụ việc liên kết (tùy chọn)"** — không nằm trong danh sách trường mà form spec (Accordion) liệt kê.
- Evidence: `../bug-reports/tvcs/image/tvcs-batchB-form-them-nhom1-2.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. **Form spec (Thành phần màn hình) + Inputs KHÔNG có trường "Vụ việc liên kết":** danh sách Inputs của FR-X.1-01 (UC147) chỉ gồm `ma_noi_dung / doanh_nghiep_id / chuyen_gia_id / linh_vuc_id / noi_dung_tu_van / tieu_de / trang_thai / ngay_tu_van / ghi_chu / don_vi_id / cong_khai / anh_dai_dien` — không có `vu_viec_id`. Accordion form cũng không liệt kê trường này.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:108`–`120` (bảng Inputs FR-X.1-01 — không có vu_viec_id)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1142`–`1143` (Accordion form — không liệt kê "Vụ việc liên kết")

2. **Nhưng ERD/mô hình dữ liệu LẠI có FK `vu_viec_id`** trên thực thể TVCS: nullable, mô tả "Vụ việc liên quan (nếu có)".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1316` (`vu_viec_id | identifier | N | FK → VU_VIEC(id) | Vụ việc liên quan (nếu có)`)

**Câu hỏi cần BA xác nhận**

Form Thêm/Sửa TVCS **có nên hiển thị trường "Vụ việc liên kết (tùy chọn)"** để cán bộ chọn không?

1. **Hướng 1 — theo ERD (giữ trường):** trường hợp lệ vì data model có `vu_viec_id` (optional). Cần bổ sung mô tả trường này vào §Inputs + §Thành phần màn hình của SRS cho khớp.
2. **Hướng 2 — theo form spec (bỏ trường):** form chỉ nên có các trường đã liệt kê; trường "Vụ việc liên kết" là thừa so với đặc tả màn hình → yêu cầu Dev FE gỡ.

**Đề xuất QA tạm thời**

- Chưa gửi điểm này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho mục phụ `QLNDTVVCG_08 (Vụ việc liên kết)`: `Cần BA xác nhận`.
- Nếu BA chọn Hướng 1: UI hiện tại **không lỗi** — chỉ cần cập nhật SRS §Inputs/§Màn hình để nhất quán.
- Nếu BA chọn Hướng 2: UI cần gỡ trường "Vụ việc liên kết", owner `Dev FE`; đồng thời cập nhật expected testcase.

---

## Nhóm C — Màn Chi tiết SCR-X1-02

> **File này để làm gì:** gom các testcase Batch C mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI. Bug có SRS reference rõ → `../../bug-reports/tvcs/Pass-bug-report-tvcs-batchC.md`.
>
> **Môi trường verify:** https://18.143.165.120.nip.io · **Tài khoản:** `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, đơn vị BTP·TW) · **Tool:** Chrome DevTools MCP.
> **SRS:** `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` (v3.5, bản đồng nhất với `srs-v3.5/`).

---

### QLNDTVVCG_15 (row 283) — Số nhóm accordion (5/6/7) + nhãn nhóm màn Chi tiết TVCS (SRS tự mâu thuẫn)

**Dạng B — SRS tự mâu thuẫn về nhãn nhóm, QA không tự chốt được.**

**Bối cảnh testcase**

- Dòng Excel: 283, mã TC `QLNDTVVCG_15`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn **Chi tiết TVCS** (SCR-X1-02, chế độ xem) → quan sát số nhóm accordion + tên từng nhóm.
- Expected/Actual đối tác (ảnh `QLNDTVVCG_15.jpg`, env `htpldn-uat.ospgroup.vn`, bản **TVCS-20260527-0001 Đã duyệt**):
  - Đối tác thấy **7 nhóm**: Thông tin cơ bản / Nội dung tư vấn / **Vụ việc liên kết** / **Tư liệu pháp luật** / **Trạng thái công khai** / Đánh giá chất lượng / **Nhật ký**.
  - Đối tác kỳ vọng: **5 nhóm**; nhãn "Tư liệu pháp lý liên kết" (không phải "Tư liệu pháp luật"); "Nhật ký thao tác" (không phải "Nhật ký").

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW).
- Mở `https://18.143.165.120.nip.io/tv-chuyen-sau/5eed0008-0000-4000-8000-000000000001` — bản **TVCS-SEED-0001**, trạng thái **Đã duyệt** (khớp đúng trạng thái bản đối tác đang đứng).
- Đếm bằng `evaluate_script` (đọc `.ant-collapse-header`) → **đúng 6 nhóm**, nhãn chính xác:
  `["Thông tin cơ bản", "Nội dung tư vấn", "Tư liệu pháp luật", "Trạng thái công khai", "Đánh giá chất lượng", "Nhật ký"]`
- **KHÔNG có nhóm "Vụ việc liên kết"** → phần "7 nhóm" của đối tác **không tái hiện** trên env này.
- 6 nhóm này = **đúng SRS cho trạng thái Đã duyệt**: 5 nhóm cơ bản (Thông tin cơ bản / Nội dung TV / Tư liệu PL / Đánh giá CL / Nhật ký) + nhóm **Công khai** (chỉ hiển thị khi `trang_thai = DA_DUYET`, BR-PUBLIC-01).
- Evidence: `../../reverify-audit/QLNDTVVCG_15/qlndtvvcg_15-accordion-6nhom-nip.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **§Bố cục tổng quan** của SCR-X1-02, các nhóm accordion dùng **nhãn NGẮN**:
   - "Accordion sections (Thông tin cơ bản / Nội dung TV / **Tư liệu PL** / Đánh giá CL / **Nhật ký**)"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1133`

2. Nhưng **§Thành phần màn hình** (bảng) lại dùng **nhãn DÀI**:
   - #6 "**Tư liệu PL liên kết** (UC152)" · #8 "**Nhật ký thao tác**" · #8b "**Công khai chuyên trang**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144` (Tư liệu PL liên kết)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1146` (Nhật ký thao tác)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1147` (Công khai chuyên trang)

3. Thêm: chữ **"PL"** trong SRS (dòng 1133/1144) không rõ là "pháp **lý**" hay "pháp **luật**". Tên chức năng FR-X.1-06 = "Quản lý **tư liệu pháp lý** của vụ việc" và §Xử lý dòng 151 "Truy vấn **tư liệu pháp lý** liên quan" → nghiêng về "**pháp lý**". Web đang hiện "Tư liệu pháp **luật**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:151`

**Câu hỏi cần BA xác nhận**

Nhãn chuẩn của các nhóm accordion màn **Chi tiết TVCS** (SCR-X1-02) là gì? Cần thống nhất giữa 2 chỗ SRS đang khác nhau:

1. **Hướng 1 — theo §Bố cục dòng 1133 (nhãn ngắn):** "Tư liệu PL", "Nhật ký". → Web hiện "Nhật ký" **khớp**; "Tư liệu pháp luật" vẫn cần chốt "pháp lý/pháp luật".
2. **Hướng 2 — theo §Thành phần dòng 1144/1146/1147 (nhãn dài):** "Tư liệu pháp lý liên kết", "Nhật ký thao tác", "Công khai chuyên trang" (khớp kỳ vọng đối tác). → Web hiện "Tư liệu pháp luật"/"Nhật ký"/"Trạng thái công khai" **đều lệch**, cần Dev sửa nhãn.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt nhãn chuẩn + số nhóm chuẩn.
- Tạm verdict `QLNDTVVCG_15`: **Cần BA xác nhận**.
- Phần "7 nhóm / nhóm Vụ việc liên kết": **không tái hiện** trên nip.io (web đúng 6 nhóm cho bản Đã duyệt) → không phải lỗi trên env hiện tại; nếu BA cần, đề nghị đối tác kiểm tra lại trên bản build mới.
- Nếu BA chọn Hướng 2 (nhãn dài): các nhãn "Tư liệu pháp luật"/"Nhật ký"/"Trạng thái công khai" trên web là `Vẫn lỗi` (nhãn), owner `Dev FE`.
- Nếu BA chọn Hướng 1 (nhãn ngắn): web cơ bản đúng, chỉ cần chốt "pháp lý" vs "pháp luật".

---

### QLNDTVVCG_17 (row 284) — Nhóm 1 "Cơ quan tiếp nhận" + Nhóm 2 "Tiêu đề/Tóm tắt" màn Chi tiết TVCS

**Dạng A — QA đã kết luận, cần BA phản hồi đối tác.**

**Bối cảnh testcase**

- Dòng Excel: 284, mã TC `QLNDTVVCG_17`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn **Chi tiết TVCS** (SCR-X1-02, chế độ xem) → đọc trường của Nhóm 1 (Thông tin cơ bản) + Nhóm 2 (Nội dung tư vấn).
- Expected/Actual đối tác (ảnh `QLNDTVVCG_17.jpg`, env `htpldn-uat.ospgroup.vn`, bản TVCS-20260527-0001 Đã duyệt):
  - Nhóm 1 **thiếu "Cơ quan tiếp nhận"** (đối tác kỳ vọng có).
  - Nhóm 2 **thiếu "Tiêu đề" + thừa "Tóm tắt"**: field đầu Nhóm 2 của đối tác ghi nhãn **"Tóm tắt"** (value "Tư vấn").

**Đối chiếu SRS v3.5**

- Nhóm 1 "Thông tin cơ bản" (§Thành phần dòng 1142) gồm: Mã (auto) / DN / Chuyên gia / Lĩnh vực PL / Ngày tư vấn / Ghi chú. **KHÔNG liệt kê trường "Cơ quan tiếp nhận"** cho CB nhập/xem — `don_vi_id` (đơn vị tiếp nhận) là trường tự gán = đơn vị của CB đăng nhập (dòng 118), không phải field trên form/màn chi tiết.
- Nhóm 2 "Nội dung tư vấn" (§Thành phần dòng 1143) gồm: **Tiêu đề** (bắt buộc, max 255) / Nội dung TV chi tiết (Rich Text). Trường chính thức là `tieu_de` — "chính thức hóa từ `tom_tat`" (dòng 114). "Tóm tắt" là tên trường CŨ đã bị thay.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1142` (Nhóm 1 — không có "Cơ quan tiếp nhận")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:118` (don_vi_id auto = đơn vị CB đăng nhập)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1143` (Nhóm 2 — trường "Tiêu đề")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:114` (`tieu_de` chính thức hóa từ `tom_tat`)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW), bản TVCS-SEED-0001 (Đã duyệt).
- `evaluate_script` trên `<main>`: `hasTieuDe = true`, `hasTomTat = false`, `hasCoQuanTiepNhan = false`.
- Nhóm 1 các trường đọc được: Mã tư vấn / Doanh nghiệp / Lĩnh vực / Chuyên gia / Trạng thái / Ngày bắt đầu / Ngày hoàn thành / Ngày tạo — **không có "Cơ quan tiếp nhận"**.
- Nhóm 2: nhãn field đầu là **"Tiêu đề"** (= "Tư vấn chuyên sâu về hợp đồng thương mại seed"), tiếp theo "Nội dung chi tiết" / "Kết quả" — **KHÔNG có "Tóm tắt"**.
- Evidence: `../../reverify-audit/QLNDTVVCG_17/qlndtvvcg_17-nhom1-nhom2-clean-nip.png`

**Kết luận QA**

- **Ý "Nhóm 2 thiếu Tiêu đề + thừa Tóm tắt": KHÔNG tái hiện** trên nip.io — web hiện đúng nhãn "Tiêu đề" (SRS dòng 114/1143), không còn "Tóm tắt". Bản đối tác quay là build cũ dùng nhãn `tom_tat`. → Phần này web ĐÚNG.
- **Ý "Nhóm 1 thiếu Cơ quan tiếp nhận":** web đúng SRS — SRS §Thành phần dòng 1142 không quy định trường này (don_vi_id auto). Đây là **kỳ vọng đối tác khác SRS** → cần BA chốt.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận cho `QLNDTVVCG_17`: phần "Tiêu đề/Tóm tắt" đã đúng trên bản hiện tại (không phải bug) — đề nghị đối tác kiểm tra lại trên build mới.
- Với "Cơ quan tiếp nhận": BA quyết có bổ sung hiển thị **đơn vị tiếp nhận** ở Nhóm 1 màn Chi tiết hay không.
  - Nếu **CÓ** → cập nhật SRS dòng 1142 + Dev FE bổ sung trường (owner: Dev FE).
  - Nếu **KHÔNG** → cập nhật lại kỳ vọng testcase cho khớp SRS.
- Verdict QA đề xuất: `Cần BA xác nhận` (không gửi Dev cho tới khi BA chốt "Cơ quan tiếp nhận").

---

### QLNDTVVCG_22 (row 286) — Modal Phân công CG: ô "Chuyên môn" trống (—) + chú thích SLA

**Dạng A — QA đã kết luận (reproduce + root cause), cần BA chốt nghĩa trường dữ liệu.**

**Bối cảnh testcase**

- Dòng Excel: 286, mã TC `QLNDTVVCG_22`.
- Nội dung kiểm tra: CB Nghiệp vụ mở bản TVCS trạng thái Tiếp nhận → bấm **Phân công Chuyên gia** → quan sát modal gợi ý CG.
- Expected/Actual đối tác (ảnh `QLNDTVVCG_22.jpg`, env `htpldn-uat.ospgroup.vn`):
  - Modal hiện CG "huongcg" (dropdown ghi lĩnh vực: Đất đai, Hình sự, Lao động, Thuế) nhưng ô **"Chuyên môn" để trống (—)** "dù CG có data".
  - Đối tác kỳ vọng thêm chú thích **"Chuyên gia sẽ được gửi thông báo..."**.

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW), bản **TVCS-20260721-0001 · Tiếp nhận** → mở modal Phân công.
- `evaluate_script` đọc modal: **"Chuyên môn: —"** (tái hiện), **SĐT = 0912280028**, **Email = qa.tvvseed28@htpldn-uat.local** (populate đúng), banner **"SLA: Chuyên gia có 2 ngày làm việc để xác nhận tham gia."** hiển thị.
- API modal load CG (`GET /tu-van-viens?...&loaiTvv=CG&linhVucIds=<record.linhVuc>`) trả 1 CG:
  `hoTen:"QA TVV Seed28 Active"`, **`chuyenNganh: null`**, **`linhVucText: "Thương mại"`**, `dienThoai:"0912280028"`, `email:"qa.tvvseed28@..."`.
- Đối chiếu: nhãn dropdown "QA TVV Seed28 Active — Thương mại" lấy từ **`linhVucText`** (Lĩnh vực). Ô "Chuyên môn" trong bảng chi tiết map vào **`chuyenNganh`** — giá trị `null` → render "—". Vậy app hiển thị **đúng theo dữ liệu**; thứ đối tác tưởng là "data chuyên môn" thực chất là **Lĩnh vực** (trường khác).

**Đối chiếu SRS v3.5**

- Modal Phân công (§Thành phần dòng 1153): "gợi ý TOP 5 CG theo lĩnh vực khớp + tìm CG + ghi chú + **info SLA (2 ngày LV xác nhận)**". → banner SLA **đã có** → thỏa yêu cầu; câu "sẽ được gửi thông báo" không nằm trong SRS.
- "chuyên môn phù hợp lĩnh vực" (dòng 160) + pattern hiển thị chuyên môn khi chọn CG (dòng 1142) — **không định nghĩa** ô "Chuyên môn" đọc từ trường dữ liệu nào (`chuyenNganh` hay `linhVucText`).

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1153` (modal Phân công — info SLA 2 ngày LV)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:160` (chuyên môn phù hợp lĩnh vực)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1142` (hiển thị chuyên môn khi chọn CG)

**Câu hỏi cần BA xác nhận**

1. Ô **"Chuyên môn"** trong modal Phân công CG lấy dữ liệu từ trường nào?
   - Nếu là **Lĩnh vực CG** (`linhVucText`, đang có "Thương mại") → hiện đang map sai trường → Dev FE sửa (owner: Dev FE).
   - Nếu là **trường chuyên ngành riêng** (`chuyenNganh`, đang `null`) → app hiển thị "—" là đúng → cần **seed/nhập chuyên ngành cho CG** thì mới có dữ liệu (owner: QA seed / dữ liệu CG), **không phải bug FE**.
2. Có bổ sung câu chú thích **"Chuyên gia sẽ được gửi thông báo..."** vào modal không? (SRS chỉ yêu cầu info SLA — đã có.)

**Đề xuất QA tạm thời**

- Verdict `QLNDTVVCG_22`: **Cần BA xác nhận** — không gửi Dev/không log bug FE cho tới khi BA chốt nghĩa trường "Chuyên môn" (tránh talk-past kiểu prescribe implementation).
- Phần chú thích SLA: web đã thỏa SRS (có banner 2 ngày LV) → không phải thiếu; wording bổ sung tùy BA.
- Evidence: `../../reverify-audit/QLNDTVVCG_22/qlndtvvcg_22-modal-chuyenmon-rong-nip.png`

---

## Nhóm D — Workflow SM-TVCS

> **File này để làm gì:** gom testcase mà QA cần BA phản hồi. Riêng `QLNDTVVCG_36` đã có **bug log song song** (`../../bug-reports/tvcs/Pass-bug-report-tvcs-batchD.md` — BUG-QLNDTVVCG_36): defect "hủy trực tiếp bỏ qua guard" đã rõ theo SRS. Phần cần BA ở đây là **cơ chế duyệt hủy chưa có state/sub-flow riêng trong SM** — dev cần BA chốt cách mô hình hóa trước khi implement đúng.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` mở file verify thực. Dùng SRS v3.5 (`input/srs-update-2026-5-5/`).

---

### QLNDTVVCG_36 — Cơ chế "duyệt hủy" record DANG_TU_VAN chưa có state/sub-flow riêng trong SM-TVCS

**Bối cảnh testcase**

- Dòng Excel: 289, mã TC `QLNDTVVCG_36`.
- Nội dung kiểm tra: CB Nghiệp vụ hủy một record TVCS đang ở trạng thái "Đang tư vấn" (DANG_TU_VAN).
- Expected đối tác: hủy từ "Đang tư vấn" phải qua bước **"chờ duyệt hủy"**, không được chuyển thẳng "Đã hủy".
- Actual đối tác ghi: hủy → chuyển thẳng "Đã hủy" + báo "Đã hủy yêu cầu".

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_04` / CB_NV_TW (đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cùng đơn vị record).
- Record TVCS-20260721-0004 ở DANG_TU_VAN → bấm [Hủy yêu cầu] → hộp thoại "Hủy nội dung tư vấn" **chỉ có 1 trường "Lý do hủy"** (bắt buộc), không có bước DN đồng ý / CB PD duyệt.
- Nhập lý do → [Xác nhận hủy]: **1 request** `POST .../huy` → record `trangThai=HUY` ngay lập tức (không qua trạng thái trung gian).
- Evidence: `../bug-reports/tvcs/image/BD-case36-R2-dahuy.png`, `../bug-reports/tvcs/image/BD-case36-R2-dangtuvan.png`.

**Điểm cần BA chốt trong SRS v3.5**

1. SRS **có yêu cầu** điều kiện duyệt hủy cho record DANG_TU_VAN:
   - Processing Hủy yêu cầu bước 4: "Nếu DANG_TU_VAN: **yêu cầu DN đồng ý hủy + CB Phê duyệt duyệt hủy**".
   - SM-TVCS bảng chuyển trạng thái: `DANG_TU_VAN → HUY` có guard "**DN yêu cầu hủy + CB PD duyệt**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:229`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1512`

2. Nhưng SM-TVCS **không có trạng thái riêng** cho bước duyệt hủy, và **không có Processing sub-flow / màn hình** mô tả cơ chế:
   - Bảng trạng thái SM chỉ có 7 state: TIEP_NHAN, PHAN_CONG, DANG_TU_VAN, HOAN_THANH, CHO_PHE_DUYET, DA_DUYET, HUY — không có "CHO_DUYET_HUY" hay tương đương.
   - Điều kiện "DN đồng ý hủy + CB PD duyệt hủy" chỉ tồn tại dạng guard, không nêu ai khởi tạo yêu cầu hủy (DN hay CB NV), DN nêu đồng ý qua kênh nào, CB PD duyệt hủy ở màn hình nào.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1489-1497` (bảng 7 trạng thái, không có state duyệt hủy)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:222-232` (Processing Hủy — không có sub-flow cho bước duyệt hủy)

**Câu hỏi cần BA xác nhận**

Cơ chế hủy record DANG_TU_VAN cần được mô hình hóa thế nào để dev implement đúng guard SRS dòng 229/1512?

1. **Hướng 1 — thêm trạng thái/luồng duyệt hủy:** hủy từ DANG_TU_VAN không chuyển thẳng HUY mà vào một bước chờ (DN đồng ý + CB PD duyệt hủy) trước; cần bổ sung state/sub-flow + màn hình duyệt hủy.
2. **Hướng 2 — giữ hủy trực tiếp nhưng ràng buộc điều kiện:** không thêm state, nhưng nút hủy chỉ khả dụng/hoàn tất khi đã có xác nhận DN + phê duyệt CB PD (điều kiện enable), nếu chưa đủ thì chặn.

**Đề xuất QA tạm thời**

- Verdict TC: `Open, BA confirm` — **Open** vì hành vi hiện tại (CB NV hủy trực tiếp, bỏ qua cả DN đồng ý lẫn CB PD duyệt) vi phạm guard SRS dòng 229/1512 (đã log BUG-QLNDTVVCG_36); **BA confirm** vì cơ chế duyệt hủy chưa được đặc tả (chọn Hướng 1 hay Hướng 2).
- Bug BUG-QLNDTVVCG_36 gửi Dev BE để chặn hủy trực tiếp; phần thiết kế cơ chế chờ BA chốt hướng trước khi dev làm chi tiết.
- Nếu BA chọn Hướng 1: cần cập nhật SM-TVCS (thêm state duyệt hủy) + expected testcase khớp "chờ duyệt hủy" như đối tác mong đợi.
- Nếu BA chọn Hướng 2: giữ SM 7 state, dev thêm ràng buộc điều kiện enable nút hủy; expected testcase đối tác ("chờ duyệt hủy" là 1 state) cần điều chỉnh lại.

---

## Nhóm E — Tư liệu pháp lý, tab SCR-X1-02

> Gom các testcase Batch E mà QA **không tự chốt verdict được** (SRS tự mâu thuẫn / không quy định) hoặc cần BA phản hồi đối tác. Case Open có SRS reference rõ (QLTLPLCVV_08) đã log riêng ở `../../bug-reports/tvcs/Pass-bug-report-tvcs-batchE.md`.
>
> Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_05` / `CB_NV_TW` (CB NV có CRUD đầy đủ tư liệu — SRS dòng 806/812). SRS trích từ `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` (v3.5), số dòng mở file verify trực tiếp.

---

### QLTLPLCVV_02 — Bảng tư liệu thiếu cột "Ngày tạo" / "Người tạo" (Dạng B — SRS tự mâu thuẫn)

**Bối cảnh testcase**

- Dòng Excel: 294, mã TC `QLTLPLCVV_02`.
- Nội dung kiểm tra: CB NV mở tab "Tư liệu PL liên kết" trong Chi tiết TVCS → xem cột bảng danh sách tư liệu.
- Expected trong file UAT (đối tác): bảng tư liệu **thiếu cột "Ngày tạo" và "Người tạo"**.

**Kết quả verify UI hiện tại**

- Mở accordion "Tư liệu pháp luật" trong Chi tiết TVCS (`/tv-chuyen-sau/{id}`).
- Bảng hiển thị **7 cột**: `Tên tư liệu | Loại | Lĩnh vực | File | Trạng thái | Công khai lúc | Hành động` (đọc `<thead>` trực tiếp, cố định trên cả record TIEP_NHAN và DA_DUYET).
- **Không có** cột "Ngày tạo", "Người tạo" → khớp phản ánh đối tác. Có cột "Công khai lúc" (thời gian công khai) thay vì "Ngày tạo".
- Evidence: `../../reverify-audit/QLTLPLCVV_02/tvcs-batchE-02-cot-bang-tu-lieu.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo mục **Outputs (FR-X.1-06)**, danh sách tư liệu phải có `nguoi_tao` + `ngay_tao` (đều "luôn"):
   - #8 `nguoi_tao | text | luôn`
   - #9 `ngay_tao | datetime | luôn | dd/mm/yyyy HH:mm`

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:937`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:938`

2. Nhưng mục **Thành phần màn hình SCR-X1-02** lại mô tả bảng tư liệu chỉ gồm `Tên / Loại / Trạng thái / Số file / Hành động` — KHÔNG có "Ngày tạo"/"Người tạo" (và cũng không có "Lĩnh vực"/"Công khai lúc" mà UI đang thêm):
   - "Bảng tư liệu: Tên / Loại / Trạng thái / Số file / Hành động. Nút [+ Thêm tư liệu]"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144`

**Câu hỏi cần BA xác nhận**

Bảng danh sách tư liệu (tab "Tư liệu PL liên kết") phải gồm những cột nào? Đang có 2 nguồn SRS mâu thuẫn:

1. **Hướng 1 — theo Outputs (937/938):** phải bổ sung cột "Người tạo" + "Ngày tạo (dd/mm/yyyy HH:mm)" → UI hiện **thiếu 2 cột** (là lỗi).
2. **Hướng 2 — theo Thành phần màn hình (1144):** bảng không cần 2 cột này → UI hiện **không phải lỗi** (thậm chí đã có thêm Lĩnh vực + Công khai lúc).

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth (Outputs vs Thành phần màn hình).
- Tạm verdict `QLTLPLCVV_02`: **Cần BA xác nhận**.
- Nếu BA chọn hướng 1: UI `Vẫn lỗi` (thiếu cột Người tạo/Ngày tạo), owner `Dev FE` (+ Dev BE nếu API chưa trả 2 field).
- Nếu BA chọn hướng 2: UI **không phải lỗi**, cập nhật lại expected của TC cho khớp; đối tác nên bỏ kỳ vọng 2 cột này.

---

### QLTLPLCVV_03 — Nút "Thêm tư liệu" hiện khi TVCS "Đã duyệt"/"Hủy" (Dạng B — SRS không quy định gating theo state)

**Bối cảnh testcase**

- Dòng Excel: 295, mã TC `QLTLPLCVV_03`.
- Nội dung kiểm tra: CB NV mở tab Tư liệu của TVCS ở các trạng thái khác nhau → nút **[+ Thêm tư liệu]** có hiện không.
- Expected trong file UAT (đối tác): nút "Thêm mới" **chỉ hiện khi TVCS ở Tiếp nhận / Đã phân công / Đang tư vấn / Hoàn thành / Chờ phê duyệt**; phải **ẩn khi TVCS "Đã duyệt" và "Hủy"**.

**Kết quả verify UI hiện tại**

- TVCS **TIEP_NHAN** (baseline): [+ Thêm tư liệu] hiện + enable.
- TVCS **DA_DUYET** (record `5eed0008`): nút **hiện, enable**; bấm vào **mở được form "Thêm tư liệu pháp luật"** đủ field enable + nút [Thêm mới] enable (không seed thêm).
- TVCS **HUY** (record `758383f6`, seed→huy): nút **hiện, enable**; banner record "Nội dung tư vấn đã bị hủy".
- → Nút [+ Thêm tư liệu] hiện ở **mọi state** (kể cả DA_DUYET + HUY) → khớp phản ánh đối tác.
- Evidence: `../../reverify-audit/QLTLPLCVV_03/tvcs-batchE-03-nut-them-tu-lieu-tren-TVCS-DADUYET.png` + `...-HUY.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **Thành phần màn hình SCR-X1-02**, nút [+ Thêm tư liệu] "**luôn hiển thị**" (không gate theo state TVCS):
   - "Nút [+ Thêm tư liệu] (inline trong tab này)" — cột điều kiện hiển thị = "luôn hiển thị".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1156` (Tư liệu PL: "CRUD tư liệu inline" — không nêu gate theo state TVCS)

2. Nhưng **Quy tắc tương tác** lại giới hạn mode sửa (nếu áp cho cả CRUD tư liệu) chỉ 2 state:
   - "Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1152`

**Câu hỏi cần BA xác nhận**

Thao tác **Thêm/CRUD tư liệu PL** có bị chặn theo trạng thái TVCS không, và nếu có thì cho phép ở những state nào?

1. **Hướng 1 — theo 1144 (luôn hiển thị):** nút Thêm hiện ở mọi state → UI hiện **đúng SRS**, kỳ vọng đối tác (ẩn ở DA_DUYET/HUY) **không có cơ sở SRS**.
2. **Hướng 2 — theo 1152 (chỉ TIEP_NHAN/DANG_TU_VAN):** nút Thêm chỉ nên hiện ở 2 state → UI hiện **sai** (thừa ở PHAN_CONG/HOAN_THANH/CHO_PHE_DUYET/DA_DUYET/HUY), đồng thời kỳ vọng đối tác (5 state) **cũng lệch** (thừa PHAN_CONG/HOAN_THANH/CHO_PHE_DUYET).

> Lưu ý: kỳ vọng đối tác (hiện 5 state, ẩn DA_DUYET+HUY) **không khớp** cả hướng 1 lẫn hướng 2. Về nghiệp vụ, thêm tư liệu vào TVCS đã **Hủy**/đã **Duyệt** (chốt) có thể không hợp lý — nhưng SRS 1144 lại nói "luôn hiển thị".

**Đề xuất QA tạm thời**

- Chưa gửi Dev tới khi BA chốt: CRUD tư liệu có gate theo state TVCS không + state nào được phép.
- Tạm verdict `QLTLPLCVV_03`: **Cần BA xác nhận**.
- Nếu BA chọn hướng 1: UI **không phải lỗi** (đúng 1144); cập nhật expected TC.
- Nếu BA chọn hướng 2 (hoặc rule mới theo đối tác): UI `Vẫn lỗi` (không gate), owner `Dev FE` (+ BE chặn API create khi state chốt); cần định nghĩa rõ danh sách state cho phép.

---

### QLTLPLCVV_07 — Nút "Sửa" hiện + cho sửa (mô tả/file) trên tư liệu "Đã công khai" (Dạng A — app diverge SRS 888 có chủ đích)

**Bối cảnh testcase**

- Dòng Excel: 296, mã TC `QLTLPLCVV_07`.
- Nội dung kiểm tra: CB NV xem tư liệu ở trạng thái **CONG_KHAI ("Đã công khai")** → nút **[Sửa]** có hiện + bấm được không.
- Expected trong file UAT (đối tác): nút "Sửa" **chỉ nên hiện khi tư liệu "Nháp"**; hiện trên "Công khai" là sai.
- Actual đối tác ghi: nút "Sửa" vẫn hiện với tư liệu "Công khai".

**Đối chiếu SRS v3.5**

- SRS quy định về **hành động sửa** (không nói ẩn nút): khi tư liệu CONG_KHAI → **từ chối sửa, phải hủy công khai trước** (chặn toàn bộ chỉnh sửa).
- Bước cập nhật field (ten/loai/linh_vuc/mo_ta) chỉ chạy khi KHÔNG bị từ chối ở bước kiểm trạng thái → SRS = chặn **mọi** field khi CONG_KHAI, không có carve-out cho mô tả/file.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:888` (step 3: CONG_KHAI → từ chối sửa, phải hủy công khai trước)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:890` (step 5: cập nhật ten_tu_lieu, loai_tu_lieu, linh_vuc_id, mo_ta — chỉ khi qua được step 3)

**Kết quả verify UI hiện tại**

- Tài khoản `cbnv_tw_05` / `CB_NV_TW`, tư liệu `90268a74` trạng thái **CONG_KHAI ("Đã công khai")**.
- Nút **[Sửa] hiện + enable** trên tư liệu CONG_KHAI (khớp đối tác). (Nút [Xóa] cùng hàng thì bị disable — xem mục "bất thường".)
- Bấm [Sửa] → modal "Sửa tư liệu pháp luật" mở, banner cam "Tư liệu đã công khai — chỉ được cập nhật mô tả và file đính kèm". Field Tên/Loại/Lĩnh vực **khóa (disabled)**; File đính kèm **enable**; [Lưu] **enable**. (Mô tả hiển thị disabled trong form dù banner nói được sửa — nhưng API vẫn nhận cập nhật mô tả, xem dưới.)
- **Điểm chốt — hệ thống CHO SỬA THẬT tư liệu công khai:**
  - FE bấm [Lưu] (payload gồm cả field khóa) → `PATCH /tu-lieu-phap-ly-vvs/90268a74` trả **400** `ERR-STATE-X1-06-01` "Tư liệu đã công khai, chỉ cho phép cập nhật: moTa, fileDinhKemIds".
  - Test chốt bằng API chỉ gửi field cho phép: `PATCH {"moTa":"...","version":3}` → **200 success**, `moTa` đổi thật, `version` 3→4, `trangThai` vẫn **CONG_KHAI**. (Đã khôi phục mô tả gốc sau test.)
- → App **không** "từ chối sửa hoàn toàn" như SRS 888; mà thực thi 1 rule khác **có chủ đích**: cho cập nhật `moTa` + `fileDinhKemIds` trên tư liệu CONG_KHAI, chỉ khóa các field lõi (có mã lỗi riêng `ERR-STATE-X1-06-01` liệt kê rõ field được phép).
- Evidence: `../../reverify-audit/QLTLPLCVV_07/tvcs-batchE-07-modal-sua-mo-tren-tu-lieu-cong-khai.png` (modal mở) + `...-luu-400-err-state.png` (toast 400 khi kèm field khóa).

**Kết luận QA**

- Về **nút hiện**: SRS 888 không yêu cầu ẩn nút [Sửa] khi CONG_KHAI (chỉ chặn hành động) → riêng việc nút hiện chưa đủ để kết luận lỗi; kỳ vọng "ẩn nút" của đối tác là ý muốn UX, không có trong SRS.
- Về **hành động**: đây là điểm quan trọng — app **cho sửa thật** (mô tả + file) tư liệu CONG_KHAI (đã verify 200, persist), trong khi SRS 888 nói phải **từ chối sửa, hủy công khai trước**. Đây là **xung đột spec-vs-implementation có chủ đích** (dev cố ý cho phép sửa mô tả/file khi công khai), không phải app quên enforce → QA không tự chốt "SRS 888 thắng" được, cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Quy tắc chuẩn cho tư liệu **đã công khai**: (a) chặn sửa **toàn bộ** (theo SRS 888, phải hủy công khai trước) hay (b) cho sửa **mô tả + file đính kèm**, chỉ khóa field lõi (theo hành vi app hiện tại `ERR-STATE-X1-06-01`)?
- Nút [Sửa] trên tư liệu công khai nên **ẩn** (ý đối tác) hay **hiện-nhưng-hạn-chế** (app hiện tại)?
- Verdict QA đề xuất: **Cần BA xác nhận**. Chưa gửi Dev tới khi chốt:
  - Nếu BA chọn (a) SRS 888: app `Vẫn lỗi` (đang cho sửa mô tả/file khi công khai), owner `Dev BE` (chặn PATCH khi CONG_KHAI) + `Dev FE` (ẩn/khóa nút Sửa).
  - Nếu BA chọn (b) rule app: **không phải lỗi**; cập nhật SRS 888 + expected TC (nút hiện-nhưng-hạn-chế là đúng), riêng nút [Sửa] có thể vẫn cân nhắc UX theo ý đối tác.

---

## Nhóm F — Quản lý tư liệu pháp lý của vụ việc

> **File này để làm gì:** gom testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng thay bug-report (bug có SRS reference rõ → `bug-report-tvcs-batchF.md`).

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` — SRS v3.5 `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md`.

---

### QLTLPLCVV_15 — Upload file mã độc: không tái hiện được message vì bước Quét virus chưa chặn file mã độc mẫu (EICAR)

**Bối cảnh testcase**

- Dòng Excel: **300**, mã TC `QLTLPLCVV_15`.
- Nội dung kiểm tra: CB Nghiệp vụ upload một tệp **chứa mã độc** vào tư liệu pháp lý của vụ việc (widget "File đính kèm").
- Expected trong file UAT (đối tác):
  - Khi upload tệp chứa mã độc, hệ thống chặn và báo thông báo chuẩn "File '{tên}' chứa mã độc".
- Actual đối tác ghi: hệ thống báo **"Tải file thất bại"** (thông báo chung chung, không phải message chuẩn).

**Đối chiếu SRS v3.5**

- Quy trình "Tải lên file" có bước **"Quét virus"** trước khi lưu file.
- Error Handling định nghĩa mã lỗi **ERR-TLPL-04**: khi file chứa mã độc → báo *"File '{ten_file}' chứa mã độc"* (mức ERROR).
- Tức SRS yêu cầu: (1) có bước quét virus; (2) nếu phát hiện mã độc → chặn + báo message chuẩn ERR-TLPL-04.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:858` (Processing "Tải lên file" — bước "Quét virus")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:955` (Error Handling E4 — ERR-TLPL-04 "File '{ten_file}' chứa mã độc")

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Dùng tệp test **EICAR chuẩn** (chuỗi 68 byte mà mọi phần mềm diệt virus được thiết kế để phát hiện; hoàn toàn vô hại, dùng đúng mục đích kiểm thử AV):
  - Biến thể chuỗi EICAR thô đặt đuôi `.pdf` → bị chặn ở **cổng kiểm tra định dạng** ("Nội dung file không khớp định dạng", HTTP 400) — chặn vì định dạng, KHÔNG phải vì mã độc.
  - Biến thể **PDF hợp lệ nhúng nguyên chuỗi EICAR** (đi qua được cổng định dạng) → **upload THÀNH CÔNG**: `POST /api/v1/tu-lieu-phap-ly-vvs/upload` trả **HTTP 201**, `trangThaiQuet="SACH"` (sạch), không có thông báo lỗi, file hiển thị bình thường.
- ⇒ Trên hệ thống hiện tại, **bước quét virus không phát hiện tệp chứa chữ ký mã độc mẫu**; không đạt được tình huống "tệp bị chặn vì mã độc" nên **không có message để đối chiếu** với "Tải file thất bại" đối tác báo.
- Evidence: `../../reverify-audit/QLTLPLCVV_15/eicar-accepted-modal.png`, `../../cond/QLTLPLCVV_15.md` (kèm log network).

**Kết luận QA**

- `QLTLPLCVV_15`: **không tự chốt được** verdict wording (Open/Reject) vì tình huống mã độc **không tái hiện được** — hệ thống hiện chưa chặn tệp mã độc mẫu, nên chưa hề hiển thị message nào để so với chuẩn ERR-TLPL-04.
- Nghi vấn: tính năng **quét virus chưa được bật/triển khai** trên môi trường này (khớp ghi nhận nội bộ rằng phần virus/mã độc trước đây được hoãn).
- Kèm **phát hiện bảo mật**: tệp chứa chữ ký mã độc chuẩn được hệ thống nhận là "sạch" và cho lưu → nếu quét virus lẽ ra phải hoạt động thì đây là lỗ hổng cần xử lý.

**Câu hỏi cần BA xác nhận**

1. Bước **Quét virus** (SRS dòng 858) có nằm trong **phạm vi bản phát hành hiện tại / được bật trên môi trường này** không, hay đang **được hoãn**?

**Nội dung đề xuất BA phản hồi đối tác (theo nhánh)**

- **Nếu quét virus đang được HOÃN / chưa trong phạm vi:** phản hồi đối tác rằng chức năng quét mã độc chưa được kích hoạt ở giai đoạn này, nên khiếu nại về nội dung thông báo khi chặn mã độc **tạm hoãn đánh giá**; sẽ kiểm thử lại wording (đối chiếu chuẩn "File '{tên}' chứa mã độc") khi tính năng được bật. Verdict QA: `Cần BA xác nhận` (chưa gửi Dev về phần wording).
- **Nếu quét virus PHẢI hoạt động ở bản này:** đây là **lỗ hổng bảo mật** — hệ thống hiện cho phép tải lên tệp chứa chữ ký mã độc mẫu (đánh dấu "sạch"). Ưu tiên chuyển **Dev BE** khắc phục bước quét virus TRƯỚC; phần nội dung thông báo (message chuẩn ERR-TLPL-04) đánh giá lại sau khi tệp mã độc đã bị chặn. Verdict QA: `Cần BA xác nhận` + cảnh báo bảo mật.

---

### QLTLPLCVV_16 — Xóa tệp đính kèm không hiển thị hộp xác nhận (SRS silent về confirm cho xóa file)

**Bối cảnh testcase**

- Dòng Excel: **301**, mã TC `QLTLPLCVV_16`.
- Nội dung kiểm tra: CB Nghiệp vụ mở form "Sửa tư liệu pháp luật" của 1 tư liệu có file đính kèm → bấm nút xóa cạnh 1 file.
- Expected trong file UAT (đối tác):
  - Khi xóa tệp đính kèm, hệ thống **phải hiển thị hộp xác nhận** trước khi xóa.
- Actual đối tác ghi: bấm xóa file → file bị xóa ngay, **không có hộp xác nhận** nào.

**Đối chiếu SRS v3.5**

- Quy trình "Xóa file đính kèm" gồm 6 bước nghiệp vụ (kiểm quyền & phạm vi đơn vị → kiểm file tồn tại và thuộc tư liệu → xóa file khỏi storage → cập nhật danh sách liên kết → cảnh báo CB NV nếu tư liệu đang công khai và không còn file nào → ghi nhật ký). **Trong 6 bước KHÔNG có bước "hiển thị xác nhận".**
- Ngược lại, quy trình "Xóa mềm **tư liệu**" **có** bước hiển thị xác nhận: *"Bạn có chắc chắn muốn xóa tư liệu '{tên}'?"*. Tức là spec CHỦ ĐÍCH phân biệt: xóa **tư liệu** có confirm, xóa **file** thì không mô tả confirm.
- Vì vậy hành vi "xóa file không confirm" mà đối tác quan sát **đang khớp với SRS hiện hành**; kỳ vọng "phải có confirm" của đối tác là thứ SRS **chưa quy định**.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:904` (đầu bảng "Processing — Xóa file đính kèm") → `:913` (bước 6, hết bảng — không có step confirm)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:900` (Processing "Xóa mềm tư liệu" step 4 — CÓ hiển thị xác nhận, để đối chiếu)

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Bằng chứng đối tác (video `../../partner-evidence/QLTLPLCVV_16.webm`): frame t002 form "Sửa" hiển thị file cũ `2K15 T5 (16.7) & T7 (18.7).pdf` kèm icon thùng rác; frame t003→t004 sau khi bấm thùng rác, file **biến mất ngay, không có hộp xác nhận** → khớp actual đối tác.
- Trên env verify `18.143.165.120.nip.io`: KHÔNG thao tác lại được đúng bước vì form "Sửa" **không hiển thị file đính kèm cũ** (endpoint chi tiết trả `files: []` dù `soFile: 1` — xem mục Ghi chú anomaly). Evidence: `../../reverify-audit/QLTLPLCVV_16/nipio-edit-form-no-existing-file.png` + `../../cond/QLTLPLCVV_16.md`.
- Đối chiếu: hành vi "không confirm khi xóa file" trên env đối tác **đúng với SRS 904–913**.

**Kết luận QA**

- `QLTLPLCVV_16`: theo SRS v3.5, **không confirm khi xóa file đính kèm là ĐÚNG spec hiện hành** — không phải bug so với SRS.
- Kỳ vọng "phải có hộp xác nhận" của đối tác **chưa được SRS quy định** cho thao tác xóa **file** (chỉ xóa **tư liệu** mới có confirm) → bất đồng về đặc tả, cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận **có bổ sung bước "hiển thị hộp xác nhận" cho thao tác Xóa file đính kèm hay không**:

- **Nếu GIỮ theo SRS hiện hành:** không cần confirm khi xóa file → cập nhật expected của `QLTLPLCVV_16` cho khớp SRS (chỉ xóa tư liệu mới confirm); phản hồi đối tác đây không phải lỗi.
- **Nếu BỔ SUNG confirm:** cập nhật SRS 904–913 thêm step "hiển thị xác nhận" → chuyển Dev FE bổ sung hộp xác nhận; khi đó UI hiện tại (không confirm) mới là lỗi.
- Verdict QA đề xuất: `Cần BA xác nhận` (chưa gửi Dev cho tới khi BA chốt spec confirm).

---

### Ghi chú anomaly (ngoài phạm vi TC — phát hiện khi verify QLTLPLCVV_16, cần dev/BA)

Trên env verify `18.143.165.120.nip.io`, **form "Sửa tư liệu pháp luật" không hiển thị file đính kèm hiện có** → CB NV không xem/xóa được file cũ qua form Sửa. Đo 2 phương pháp: (1) UI — quét `[role=dialog]` không thấy item file nào; (2) API — `GET /api/v1/tu-lieu-phap-ly-vvs/{id}` trả `files: []` dù `soFile: 1`, cho cả tư liệu NHAP mới tạo lẫn tư liệu CONG_KHAI (chắc chắn có file vì đã công khai — SRS 867). Đề nghị dev xác nhận: endpoint chi tiết có nên trả mảng `files` không, hoặc FE có nạp file qua endpoint khác không (env đối tác `ospgroup.vn` hiển thị được file). *Chưa log bug Open vì chưa loại trừ khả năng khác biệt build/endpoint — chờ dev confirm.*
