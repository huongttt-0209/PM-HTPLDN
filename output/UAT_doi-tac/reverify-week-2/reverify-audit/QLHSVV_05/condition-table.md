# QLHSVV_05 — Bảng đối chiếu điều kiện

**Case:** Thêm tài liệu vào vụ việc đang ở trạng thái cho phép sửa (SCR-V.I-03 Accordion 3 · FR-V.I-07 UC57).

**Evidence đối tác:** `partner-evidence/QLHSVV_05.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/d72ca300-...**?mode=edit**`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"** (cùng vụ việc với QLHSVV_03).
Nhóm **"Tài liệu đính kèm"** đã mở: chỉ có bảng (Tên tài liệu · Loại · Định dạng · Kích thước · Trạng thái quét · Ngày tải) + trạng thái rỗng "Chưa có tài liệu".
**KHÔNG có nút [+ Thêm tài liệu]**, không có vùng kéo-thả / chọn tệp.

**Đối tác phản ánh:** không có nút chức năng thêm tệp → không thực hiện được bước "Tệp hợp lệ" của case.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Entity + trạng thái (state machine) | VV mở được `?mode=edit` ⇒ đang ở trạng thái **cho phép sửa** | `VV-BTP-TW-20260712-005` (cf90a65c) — trạng thái **"Đã tiếp nhận"** = cho phép sửa (khớp state bug gốc; VV-006 gốc nay đã sang "Yêu cầu bổ sung") | Không |
| Dữ liệu tiền đề (danh sách tài liệu) | Bảng tài liệu **rỗng** ("Chưa có tài liệu") | Bảng tài liệu **rỗng** ("Chưa có tài liệu") — cùng điều kiện | Không |
| Chế độ quan sát (edit vs view) | Chế độ **sửa** (`?mode=edit`), nhóm "Tài liệu đính kèm" đã mở | Đã kiểm tra **CẢ 2 chế độ**: `?mode=edit` (nhóm mở) **và** chế độ xem thường — cả hai đều không có nút thêm tệp | Không |

## Quan sát (real-data)

**Vòng 1 (bug gốc):**
```json
{"che_do_edit": {"hasAddBtn": false, "fileInputs": 0, "uploadAreas": 0},
 "che_do_xem":  {"hasAddBtn": false, "fileInputs": 0, "uploadAreas": 0}}
```

**Re-test 2026-07-15 (sau dev fix) — cbnv_tw, VV-BTP-TW-20260712-005 `?mode=edit`:**
```json
{"hasAddBtn": true,
 "addBtnLabel": "Thêm tài liệu",
 "dialog": "Thêm tài liệu bổ sung — có file input + vùng kéo-thả; rule: Tối đa 10 tệp, .pdf/.doc/.docx/.xls/.xlsx/.png/.jpg/.jpeg, ≤20MB/tệp",
 "full_flow": "Chọn tệp PNG (244.9 KB) → Tải lên → toast 'Đã tải lên 1 tệp' → tệp vào bảng Tài liệu đính kèm (Loại BO_SUNG, PNG, quét virus 'Sạch', ngày 15/07/2026) — BE persist OK"}
```
→ **PASS:** nút [+ Thêm tài liệu] có mặt, upload chạy hết luồng và lưu thật (đúng thông báo "Đã tải lên {n} tệp" mà Kết quả mong đợi của case yêu cầu).

Ảnh: `../../bug-reports/image/BUG-QLHSVV_05-retest-upload-tailieu-thanhcong.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu 1** — `srs-fr-05-vu-viec.md:1721` (SCR-V.I-03 §Thành phần #6, Accordion 3 "Tài liệu Đính kèm"): *"Danh sách file: tên file, loại, kích thước, ngày upload, nút [Xem] [Tải]. **Nút [+ Thêm tài liệu]**"* — Điều kiện hiển thị: *"Luôn. **[+ Thêm] chỉ khi trạng thái cho phép sửa**"*.
  VV đang ở "Đã tiếp nhận" = trạng thái cho phép sửa (theo dòng 593: chỉ cấm HOAN_THANH + DA_DANH_GIA) ⇒ nút **[+ Thêm tài liệu] PHẢI hiển thị**.
  **Thực tế web:** không có nút, không có vùng upload, không có `input[type=file]` → **THIẾU**.
- **SRS yêu cầu 2** — `srs-fr-05-vu-viec.md:585` (FR-V.I-07 / UC57 §Inputs, dòng 3): trường **`file_bo_sung` (FILE[])** — *"Upload tài liệu bổ sung"* là input hợp lệ của chức năng.
  `srs-fr-05-vu-viec.md:595` (§Processing bước 4): *"Lưu tài liệu bổ sung"*. `:625` (§AC): *"Given CB NV chỉnh sửa When upload tài liệu bổ sung Then validate + lưu, ghi audit"*.
  **Thực tế web:** không có đường nào để upload từ màn chi tiết → chức năng **chưa được hiện thực** → **THIẾU**.

**Kết luận:** SRS quy định rõ nút [+ Thêm tài liệu] phải hiển thị ở trạng thái cho phép sửa, web không có → **Open**.
Vì không có nút, bước "chọn tệp hợp lệ" và thông báo *"Đã tải lên {số tệp} tệp"* trong Kết quả mong đợi của case **không thể kiểm tra được** — dev cần bổ sung chức năng trước.
