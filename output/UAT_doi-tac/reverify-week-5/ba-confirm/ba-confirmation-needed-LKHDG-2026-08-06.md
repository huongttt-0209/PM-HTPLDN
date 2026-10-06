# BA confirmation needed — LKHDG (Đánh giá hiệu quả · Kế hoạch đánh giá) — 2026-08-06

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `bug-report-*.md`).

> **Phạm vi file này:** đợt re-verify FLOW 04 các bug đối tác đã đánh `Dopai=dev done` + `Trạng thái dev fix=Fixed`,
> bảng `1OKBN2otlmdZ44…` tab `bug`. Đo trên **env dev `https://18.143.165.120.nip.io`**, bản dựng **HTPLDN · V1.0.8**
> (`assets/index-DThrFe1_.js`), tài khoản `cbnv_tw` (CB_NV_TW · `BTP · TW`).
>
> **Lưu ý hiệu lực:** đối tác quay bằng chứng trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản V1.0 / V1.0.2.
> Mọi quan sát dưới đây là của bản V1.0.8 trên env dev.

---

## LKHDG_16 — Form Sửa kế hoạch đang hiển thị "Tài liệu đính kèm" nhưng đặc tả màn hình không liệt kê thành phần này

**Bối cảnh testcase**

- Dòng Excel: **127**, mã TC `LKHDG_16`, tab `bug`.
- Nội dung kiểm tra: *Cán bộ Nghiệp vụ Trung ương* bấm **[Sửa]** một đợt đánh giá từ màn
  **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**.
- Expected trong file UAT (cột "Kết quả mong đợi" của đối tác):
  - *"Chỉ hiển thị khi đợt đang ở trạng thái 'Lập kế hoạch' hoặc 'Phân công', và Cán bộ nghiệp vụ thuộc đơn vị
    sở hữu đợt."*
  - *"Hệ thống mở màn hình chi tiết đợt đánh giá ở chế độ chỉnh sửa."*
- Actual đối tác ghi (vòng 2, cột "Kết quả verify"): *"Không hiển thị danh sách các tệp đính kèm mặc dù tồn tại
  dữ liệu"* → đối tác chấm `Fail`.

**Kết quả verify UI hiện tại**

- Verify lại ngày **06/08/2026** qua **Chrome DevTools MCP**, tài khoản UAT `cbnv_tw` / *CB Nghiệp vụ Trung ương*.
- Mở `https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach` → bấm **[Sửa]**.
- Khung Sửa mở ra dưới dạng bảng nhập bên phải, tiêu đề **"Sửa kế hoạch đánh giá"**, gồm **9** mục:
  Tên đợt đánh giá · Mục tiêu · Tần suất · Đối tượng · **Cơ quan được đánh giá** · Thời gian bắt đầu ·
  Thời gian kết thúc · Ghi chú · **Tài liệu đính kèm**.
- Mục **"Tài liệu đính kèm"** hiện **có** liệt kê đủ tệp của đợt kèm kích thước và thao tác [Xem] [Xóa] —
  đo trên 2 đợt: đợt có **1** tệp (`.pdf`) và đợt có **2** tệp khác định dạng (`.docx` + `.pdf`).
  ⇒ **Triệu chứng đối tác nêu không còn tái hiện trên bản V1.0.8.**
- Lưu form mà không đụng vùng đính kèm **không làm mất tệp** đã có (đọc lại bản ghi: vẫn đủ 2 tệp,
  `trangThaiQuet = SACH`).
- Evidence: `../../reverify-bug-devfix-2026-08-06/bug-reports/image/LKHDG_16-C-drawer-sua-dot-1-tep-ghichu-da-luu-V108.png` ·
  `../../reverify-bug-devfix-2026-08-06/bug-reports/image/LKHDG_16-A-man-chitiet-co-2-tep-dinh-kem-V108.png`

**Điểm cần BA chốt**

1. **Đặc tả thực thể CÓ trường tệp đính kèm.**
   `KE_HOACH_DANH_GIA` khai trường `file_dinh_kem`, kiểu `file[]`, định dạng `PDF/DOC/DOCX/XLS/XLSX`,
   tối đa 20MB/tệp `[CR-07]`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1043`

2. **Nhưng bảng thành phần của form tạo/sửa lại là danh sách ĐÓNG 7 dòng và KHÔNG có dòng nào tên
   "Tài liệu đính kèm".** Bảy dòng đó là: `#21` Tên đợt · `#22` Mục tiêu · `#23` Tần suất · `#24` Từ ngày/Đến ngày ·
   `#25` Đối tượng · `#26` Ghi chú · `#27` thanh hành động `[Hủy] [Lưu nháp] [Lưu & Chuyển tiêu chí]`.
   Cũng không có dòng nào cho mục **"Cơ quan được đánh giá"** mà giao diện đang hiển thị.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:843-851`

⇒ Giao diện hiện **nhiều hơn** đặc tả màn hình 2 mục. Đối tác **mong đợi** phần hơn đó (chính là lý do họ chấm
Fail ở vòng 2 khi nó chưa có). Đặc tả không cấm, nhưng cũng không ghi nhận.

**Câu hỏi cần BA xác nhận**

Bảng thành phần form tạo/sửa đợt đánh giá (`srs-fr-08-danh-gia.md:843-851`) nên được hiểu theo hướng nào?

1. **Hướng 1 — danh sách MỞ (giao diện được phép có thêm thành phần phục vụ trường của thực thể).**
   Việc form Sửa hiển thị "Tài liệu đính kèm" và "Cơ quan được đánh giá" là **đúng**; đề nghị BA bổ sung 2 dòng
   này vào bảng để đặc tả khớp hiện trạng, tránh lượt dọn dẹp sau lại gỡ mất.
2. **Hướng 2 — danh sách ĐÓNG (form chỉ được có đúng 7 thành phần).**
   Thì phần "Tài liệu đính kèm" đang hiển thị là **thừa so với đặc tả**, và kỳ vọng của đối tác ở `LKHDG_16`
   vòng 2 là **sai so với đặc tả** — cần BA phản hồi lại đối tác thay vì để dev gỡ đi.

**Đề xuất QA tạm thời**

- **Không** gửi điểm này cho Dev — hiện trạng đang **thoả** kỳ vọng đối tác, gỡ đi sẽ tái sinh đúng bug cũ.
- Verdict của `LKHDG_16` trong đợt này **không** treo vào câu hỏi trên. Case được chấm **Reopen** vì một lý do
  khác, độc lập và đã có căn cứ đặc tả rõ ràng: đợt ở trạng thái **Phân công** không vào được chế độ sửa, trái
  `srs-fr-08-danh-gia.md:837` + `:159` và trái chính cột "Kết quả mong đợi" của phiếu.
  → đã log `BUG-LKHDG-SUA-PHANCONG` tại `../../reverify-bug-devfix-2026-08-06/bug-reports/bug-report-LKHDG.md`.
- Nếu BA chọn **Hướng 1**: QA cập nhật tiêu chí verify để coi "Tài liệu đính kèm" là thành phần bắt buộc của form
  Sửa; owner `BA update SRS`.
- Nếu BA chọn **Hướng 2**: QA hạ kỳ vọng của `LKHDG_16` vế (c) xuống "không áp dụng", và BA phản hồi đối tác;
  owner `BA phản hồi đối tác`. **Vẫn không đề nghị Dev gỡ tính năng** khi chưa có quyết định bằng văn bản.

---

## Phụ lục — vì sao điểm dưới đây KHÔNG nằm trong file này

| Điểm phát hiện | Xử lý | Lý do |
|---|---|---|
| Đợt ở trạng thái *Phân công* không sửa được (giao diện giấu thao tác Sửa + máy chủ trả 409 `ERR-BIZ-XI-01-02`) | **Log bug** `BUG-LKHDG-SUA-PHANCONG` | Đặc tả **không tự mâu thuẫn**: chỉ có 2 dòng nói về việc sửa kế hoạch (`:837`, `:159`) và cả hai đều cho phép sửa ở *Phân công*. Có SRS reference rõ ⇒ thuộc bug-report, không phải câu hỏi BA |
| Xuất Excel không áp bộ lọc đang bật | **Log bug** `BUG-LKHDG-EXPORT-FILTER` | `BR-DATA-06` (`srs-v3.5.md:5525`) ràng buộc rõ *"File xuất theo bộ lọc hiện tại"*, áp dụng *"Toàn bộ CRUD list"* |
| Tệp xuất Excel thiếu/thừa cột, nhãn ghi mã enum thô | **Không log, chỉ ghi nhận** | Đặc tả **im lặng** về tập cột và định dạng nhãn của *tệp xuất*; bảng `:829-837` là đặc tả **màn hình**. Đòi tệp sao đúng cột của bảng là QA tự đặt luật |
