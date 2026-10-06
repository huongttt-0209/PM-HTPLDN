# BA confirmation needed — TVCS Batch B (Form Thêm/Sửa SCR-X1-02) — 2026-07-21

> **File này để làm gì:** gom các testcase mà QA không tự chốt verdict được hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh.

> **Citation:** SRS v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`.

---

## QLNDTVVCG_06 — Form Thêm TVCS: "Ngày tư vấn" không mặc định hôm nay + thiếu trường "Cơ quan tiếp nhận" (web khớp SRS, kỳ vọng đối tác khác đặc tả)

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

## QLNDTVVCG_08 (mục phụ) — Form Thêm TVCS có trường "Vụ việc liên kết (tùy chọn)" không nằm trong danh sách Inputs của form (SRS mâu thuẫn nội bộ: form spec im lặng, ERD có FK)

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
