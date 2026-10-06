# BA confirmation needed — TVCS Batch A (Màn danh sách SCR-X1-01) — 2026-07-21

> **File này để làm gì:** gom các testcase mà QA không tự chốt verdict được hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh.

> **Citation:** SRS v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`.

---

## QLNDTVVCG_40 — Xuất Excel danh sách TVCS: tên tệp + tập cột đối tác kỳ vọng khác với SRS (SRS silent về export)

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
