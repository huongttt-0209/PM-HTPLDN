# BA confirmation needed — Biểu mẫu Batch 2 (Tìm kiếm thư mục & biểu mẫu) — 2026-07-20

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `Pass-bug-report-bieu-mau-batch2.md`).

> **Phạm vi:** tab đối tác `UAT_TGPL Doanh Nghiệp-tuần 3`, sub-module TKTMBMHD (FR-VII-02/UC93) + TKBMHD (FR-VII-05/UC96). Verify env `https://18.143.165.120.nip.io`, login `cbnv_tw` (CB_NV_TW) / Test@1234, tool Chrome DevTools MCP.
>
> **SRS chấm:** `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md` (v3.5). Mọi citation dưới đây đã mở file verify số dòng thực.

---

## TKTMBMHD_04 (row 89) — Giá trị mặc định bộ lọc Danh sách chọn: "Tất cả" hay rỗng?

> **Dạng B — SRS tự mâu thuẫn, cần BA chốt source truth.**

**Bối cảnh testcase**

- Dòng Excel: 89, mã TC `TKTMBMHD_04`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) kiểm giá trị mặc định các trường Danh sách chọn của bộ lọc màn "Thư viện biểu mẫu → Thư mục" (SCR-VII-01).
- Expected trong file UAT: giá trị mặc định của các trường kiểu Danh sách chọn là **"Tất cả"**.
- Actual đối tác ghi: giá trị mặc định là **rỗng**.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/thu-muc`.
- Bộ lọc **Lĩnh vực**: chỉ hiện placeholder "Lĩnh vực"; danh sách chọn = `[Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư]` — **không có mục "Tất cả"**, không chọn sẵn.
- Bộ lọc **Trạng thái**: placeholder "Trạng thái"; danh sách chọn = `[Nháp, Đã công khai, Đã ẩn]` — **không có mục "Tất cả"**.
- Cơ chế app: placeholder rỗng = không áp bộ lọc = hiển thị toàn bộ (tab "Tất cả 4", list đủ record). → Web khớp §Inputs (default "—") nhưng lệch §Thành phần màn hình (default "Tất cả").
- Evidence: `../../reverify-audit/TKTMBMHD_04/web-default-filters.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-VII-01 §Thành phần màn hình**, bộ lọc để mặc định "Tất cả":
   - #4 Lọc lĩnh vực: "Mặc định: 'Tất cả'".
   - #5 Lọc trạng thái: liệt kê "Tất cả / NHAP / CONG_KHAI / AN" ("Tất cả" là option đầu).

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:606`
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:607`

2. Nhưng **FR-VII-02 §Inputs** lại đặt mặc định "—" (rỗng):
   - `linh_vuc_id`: Mặc định "—".
   - `trang_thai`: Mặc định "—".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:163`
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:166`

**Câu hỏi cần BA xác nhận**

Bộ lọc Danh sách chọn (Lĩnh vực, Trạng thái) trên màn tìm kiếm thư mục cần hiểu theo hướng nào?

1. **Hướng 1 — theo §Thành phần màn hình (SCR-VII-01:606–607):** thêm mục "Tất cả" vào danh sách chọn và đặt sẵn làm mặc định.
2. **Hướng 2 — theo §Inputs (FR-VII-02:163/166):** để mặc định rỗng (placeholder = không lọc) như hiện tại.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict `TKTMBMHD_04`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: UI hiện tại `Vẫn lỗi`, owner dự kiến `Dev FE` (thêm option "Tất cả" + set default).
- Nếu BA chọn hướng 2: UI hiện tại **không phải lỗi** (đang đúng §Inputs); cập nhật lại expected testcase cho khớp SRS.
- Đồng bộ tiền lệ tuần 3 `LKHDG_03` (batch A) — cùng vấn đề placeholder vs mục "Tất cả".

---

## TKTMBMHD_07 (row 91) — Nút "Xóa bộ lọc" không đưa tab phân loại về "Tất cả"

> **Dạng A — QA đã kết luận (SRS không quy định), cần BA phản hồi đối tác.**

**Bối cảnh testcase**

- Dòng Excel: 91, mã TC `TKTMBMHD_07`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) bấm nút "Xóa bộ lọc" trên màn "Thư viện biểu mẫu → Thư mục" (SCR-VII-01).
- Expected trong file UAT:
  - Xoá toàn bộ giá trị đã nhập tại điều kiện tìm kiếm và bộ lọc (Tìm kiếm, Lọc lĩnh vực, Lọc trạng thái, Khoảng ngày tạo).
  - Đưa tab phân loại về "Tất cả".
  - Hiển thị lại danh sách mặc định (toàn bộ thư mục trong phạm vi phân quyền, sắp xếp ngày tạo giảm dần).
- Actual đối tác ghi: không đưa về tab "Tất cả".

**Đối chiếu SRS v3.5**

- FR-VII-02 (UC93) và SCR-VII-01 §Thành phần màn hình **không mô tả nút "Xóa bộ lọc"**; không có clause nào quy định nút này phải reset tab phân loại về "Tất cả".
- Thanh lọc (SCR-VII-01 #3–6) gồm ô tìm kiếm / lọc lĩnh vực / lọc trạng thái / khoảng ngày; tab phân loại (#7) là control riêng ở vùng content — SRS không ràng buộc quan hệ giữa nút "Xóa bộ lọc" và tab.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:605` (thanh lọc: ô tìm kiếm)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:609` (tab phân loại: Tất cả / Đã công khai / Nháp / Đã ẩn)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Tiền đề: đang ở tab "Nháp" + có từ khóa `zzzqa123` trong ô tìm kiếm (URL `.../bieu-mau/thu-muc?tab=NHAP&keyword=zzzqa123`).
- Bấm **Xóa bộ lọc** → URL đổi thành `.../bieu-mau/thu-muc?tab=NHAP`: từ khóa + bộ lọc bị xoá, **nhưng tab vẫn là "Nháp"** (không về "Tất cả"); danh sách vẫn lọc theo tab Nháp (3 thư mục), không hiển thị lại toàn bộ.
- Evidence: `../../reverify-audit/TKTMBMHD_07/web-after-xoa-boloc.png`

**Kết luận QA**

- `TKTMBMHD_07` **không vi phạm clause SRS nào** — SRS im lặng về hành vi "Xóa bộ lọc" ↔ tab phân loại. Web xoá đúng các trường trong thanh lọc.
- Điểm khác biệt: đối tác kỳ vọng nút cũng reset tab về "Tất cả" — đây là kỳ vọng UX **vượt ngoài đặc tả** hiện có, không phải lỗi tái hiện được clause nào.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý cho `TKTMBMHD_07`:

- Nếu chuẩn hoá "Xóa bộ lọc" = đưa về trạng thái mặc định hoàn toàn → **bổ sung yêu cầu**: nút reset cả tab phân loại về "Tất cả" + hiển thị lại danh sách mặc định.
- Nếu giữ nguyên (nút chỉ xoá các trường trong thanh lọc, tab do người dùng chủ động đổi) → cập nhật expected testcase cho khớp hành vi.
- Verdict QA đề xuất: `Cần BA xác nhận`; **không gửi Dev** cho tới khi BA chốt (nếu BA đồng ý bổ sung thì owner `Dev FE`).

---

## TKBMHD_03 (row 113) — Bộ lọc màn Danh sách biểu mẫu: mặc định "Tất cả" + Định dạng có "PDF"

> **Dạng B — SRS tự mâu thuẫn / im lặng, cần BA chốt source truth.**

**Bối cảnh testcase**

- Dòng Excel: 113, mã TC `TKBMHD_03`.
- Nội dung kiểm tra: CB Nghiệp vụ (CB_NV_TW) kiểm điều kiện tìm kiếm / bộ lọc màn "Biểu mẫu → Danh sách biểu mẫu" (SCR-VII-02). Đối tác nêu 2 ý.
- Expected trong file UAT: các trường thông tin hiển thị giống thiết kế, đúng định dạng.
- Actual đối tác ghi: (1) các trường Danh sách chọn giá trị mặc định **không phải "Tất cả"**; (2) trường Định dạng **thừa giá trị "PDF"**.

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/bieu-mau/danh-sach`.
- (1) 4 bộ lọc Danh sách chọn (Thư mục, Lĩnh vực, Loại hình, Định dạng) đều chỉ hiện placeholder, **không có mục "Tất cả"**, không chọn sẵn — placeholder = không lọc.
- (2) Dropdown **Định dạng** = `[DOC, DOCX, XLS, XLSX, PDF]` — **có "PDF"**.
- Evidence: `../../reverify-audit/TKBMHD_03/web-dinhdang-pdf.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Về **giá trị mặc định "Tất cả"**:
   - FR-VII-05 §Inputs (keyword, linh_vuc_id, loai_hinh, thu_muc_id) đều "Mặc định —" (rỗng); SCR-VII-02 §Thành phần chỉ ghi "select | Các bộ lọc", **không** nêu default "Tất cả".
   - Nhưng màn chị em SCR-VII-01 (tìm kiếm thư mục) lại quy định lọc lĩnh vực "Mặc định: 'Tất cả'" → 2 màn cùng chức năng lệch chuẩn.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:400` (FR-VII-05 §Inputs linh_vuc_id, Mặc định "—")
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:640` (SCR-VII-02: "các bộ lọc", không nêu default)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:606` (SCR-VII-01 lọc lĩnh vực "Mặc định: Tất cả")

2. Về **giá trị "PDF" trong bộ lọc Định dạng**:
   - File biểu mẫu (chính) chỉ nhận **doc/docx/xls/xlsx** → biểu mẫu không thể có định dạng PDF → lọc PDF luôn 0 kết quả.
   - Nhưng **file đính kèm công khai** trong cùng module lại cho phép **PDF**/DOC/DOCX/XLS/XLSX → "PDF" là định dạng hợp lệ ở một phần của module.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:50` (module: file chấp nhận doc/docx/xls/xlsx)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:652` (form File đính kèm: doc/docx/xls/xlsx)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:779` (file_dinh_kem_cong_khai: PDF/DOC/DOCX/XLS/XLSX)

**Câu hỏi cần BA xác nhận**

Bộ lọc màn Danh sách biểu mẫu cần hiểu theo hướng nào?

1. **Giá trị mặc định:** thêm mục "Tất cả" + chọn sẵn (đồng bộ SCR-VII-01) hay giữ placeholder rỗng (đồng bộ §Inputs FR-VII-05)?
2. **Trường Định dạng:** lọc theo **định dạng file biểu mẫu chính** (chỉ doc/docx/xls/xlsx → **bỏ "PDF"**) hay bao gồm cả **định dạng file đính kèm công khai** (**giữ "PDF"**)?

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict `TKBMHD_03`: `Cần BA xác nhận`.
- Nếu BA: default phải "Tất cả" → UI `Vẫn lỗi`, owner `Dev FE` (thêm option + set default). Nếu giữ placeholder → cập nhật expected testcase.
- Nếu BA: bỏ "PDF" → UI `Vẫn lỗi`, owner `Dev FE` (loại PDF khỏi dropdown Định dạng). Nếu giữ "PDF" (lọc gồm cả file công khai) → **không phải bug**, cập nhật expected testcase.
