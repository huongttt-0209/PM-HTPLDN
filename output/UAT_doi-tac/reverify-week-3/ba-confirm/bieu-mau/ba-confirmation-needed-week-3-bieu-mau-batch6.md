# BA confirmation needed — UAT đối tác tuần 3, Batch 6 (Biểu mẫu) — 2026-07-20

> **File này để làm gì:** gom các testcase re-verify Batch 6 mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh.
>
> **Phạm vi:** module Biểu mẫu — Nhập hàng loạt (FR-VII-06 / SCR-VII-03) + Công khai (FR-VII-07). 5/7 case của batch cần BA. 2 case còn lại (IBMHD_10, CKBMHDLCTT_01) đã Reject — không tái hiện trên bản hiện tại, không đưa vào file này.
>
> **SRS dùng:** v3.5 — `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md`. Tài khoản verify: `cbnv_bn` (CB Nghiệp vụ - Bộ ngành). Case chỉ định vai trò "CB Nghiệp vụ"; `cbnv_tw` đang bị session khác chiếm liên tục nên dùng `cbnv_bn` cùng vai trò — các case này là render UI / validate client / diễn giải SRS, không phụ thuộc đơn vị.

---

## IBMHD_02 (và IBMHD_03) — Màn Nhập hàng loạt: trường "Tải file Excel metadata" + nút "Tải mẫu Excel"

**Bối cảnh testcase**

- Dòng Excel: 116, mã TC `IBMHD_02` — "Màn Import thiếu trường Tệp Excel mô tả dữ liệu + nút Tải mẫu Excel".
- Dòng Excel: 117, mã TC `IBMHD_03` — "Chức năng Tải mẫu Excel bị thiếu" (cùng gốc: nút Tải mẫu Excel là thành phần của trường Excel metadata).
- Nội dung kiểm tra: CB Nghiệp vụ mở màn Nhập hàng loạt biểu mẫu (`/bieu-mau/nhap-hang-loat`).
- Expected trong file UAT: màn phải có trường "Tệp Excel mô tả dữ liệu" và nút "Tải mẫu Excel".

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_bn` / CB Nghiệp vụ. URL `/bieu-mau/nhap-hang-loat`.
- Màn bước 1 "Chọn file" chỉ có: **Thư mục đích** (select) + **Tải lên file biểu mẫu** (.doc/.docx/.xls/.xlsx, kéo-thả).
- KHÔNG có trường "Tải file Excel metadata", KHÔNG có nút "Tải mẫu Excel".
- Khớp 100% với ảnh đối tác chụp trên bản đối tác → hành vi giống nhau hai bản.
- Evidence: `bug-reports/image/BUG-IBMHD_02-03-import-screen-step1.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-VII-06 §Inputs**, luồng import chỉ nhận 2 field và KHÔNG có Excel metadata:
   - `thu_muc_id` (Thư mục đích, bắt buộc)
   - `files` (binary[], Max 50 file / 20MB / tổng 500MB)
   - Không bước Processing nào (kiểm quyền → validate → tạo bản ghi → tổng hợp → log) tiêu thụ file metadata.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:460` (thu_muc_id)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:461` (files)
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:463-472` (Processing — không có metadata)

2. Nhưng **SCR-VII-03 §Thành phần màn hình mục #2** lại yêu cầu trường Excel metadata + nút Tải mẫu, **luôn hiển thị**:
   - "Tải file Excel metadata | file-upload | .xlsx (max 5MB), Template: **[Tải mẫu Excel]** | luôn hiển thị"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:673`

**Câu hỏi cần BA xác nhận**

Màn Nhập hàng loạt biểu mẫu có bắt buộc trường "Tải file Excel metadata" + nút "Tải mẫu Excel" không? SRS đang mâu thuẫn giữa đặc tả nghiệp vụ (FR-VII-06 không dùng metadata) và đặc tả màn hình (SCR-VII-03 #2 yêu cầu hiển thị).

1. **Hướng 1 — theo SCR-VII-03 #2:** phải bổ sung trường Excel metadata + nút Tải mẫu Excel → app hiện tại **thiếu** → Dev FE bổ sung; đồng thời BA làm rõ metadata được xử lý ở bước Processing nào.
2. **Hướng 2 — theo FR-VII-06:** luồng import chỉ cần `thu_muc_id` + `files`, metadata không dùng → app hiện tại **đúng** → cập nhật SCR-VII-03 bỏ mục #2 + cập nhật expected của đối tác.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt source truth.
- Verdict tạm cho `IBMHD_02` + `IBMHD_03`: **Cần BA xác nhận** (đã ghi sheet `BA confirm`, dòng 116 + 117).
- Nếu BA chọn Hướng 1: UI hiện tại `Vẫn thiếu`, owner `Dev FE` (thêm trường + nút) + `BA` (định nghĩa cách dùng metadata).
- Nếu BA chọn Hướng 2: UI hiện tại `Đúng SRS nghiệp vụ`; owner `QA/BA` cập nhật SCR-VII-03 + expected đối tác.

---

## IBMHD_04 — Chọn tệp → bảng kiểm tra không liệt kê tệp lỗi (Hợp lệ/Lỗi)

**Bối cảnh testcase**

- Dòng Excel: 118, mã TC `IBMHD_04`.
- Nội dung kiểm tra: CB Nghiệp vụ upload tệp sai định dạng / vượt kích thước ở màn Nhập hàng loạt, xem bảng kiểm tra.
- Expected trong file UAT: tệp lỗi hiển thị trong bảng kiểm tra với trạng thái Hợp lệ/Lỗi kèm lý do.
- Actual đối tác ghi: tệp lỗi không xuất hiện trong bảng kiểm tra.

**Đối chiếu SRS v3.5**

- SCR-VII-03 #4 (Bảng kiểm tra) quy định bảng có cột **"Trạng thái (Hợp lệ/Lỗi)"**, hiển thị "sau upload" → hàm ý tệp lỗi phải xuất hiện thành dòng có trạng thái Lỗi. Bảng **không có cột "Lý do"** → kỳ vọng "kèm lý do" của đối tác vượt quá SRS.
- SCR-VII-03 #5 (Thống kê) quy định "Tổng: {N} file. Hợp lệ: {X}. **Lỗi: {Y}**" → SRS kỳ vọng có đếm số tệp lỗi.
- FR-VII-06 §Processing bước 2 "Kiểm tra từng file: định dạng + kích thước" — SRS không nói rõ kiểm ở bước chọn hay bước import.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:675` (Bảng kiểm tra — cột Trạng thái Hợp lệ/Lỗi)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:676` (Thống kê — Lỗi: {Y})
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:468` (Processing bước 2 — validate định dạng + kích thước)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ. Upload `.txt` (sai định dạng) + `.docx` 22MB (>20MB) + 2 tệp hợp lệ.
- Tệp lỗi bị **chặn NGAY tại bước Chọn file** kèm thông báo lý do ("Định dạng không hỗ trợ: ... Chỉ chấp nhận .doc,.docx,.xls,.xlsx" / "vượt quá 20MB (22.0 MB)").
- Bảng kiểm tra (STT / Tên / Định dạng / Kích thước / Trạng thái) + Thống kê (Tổng/Hợp lệ/Không hợp lệ) **chỉ liệt kê tệp hợp lệ**; tệp lỗi không thành dòng.
- Đối chiếu: app báo lỗi + lý do (đạt mục tiêu "người dùng biết tệp nào sai + vì sao"), nhưng KHÁC cách trình bày mà SCR-VII-03 #4/#5 mô tả (tệp lỗi thành dòng Lỗi trong bảng + đếm Lỗi:{Y}).
- Evidence: `bug-reports/image/BUG-IBMHD_04-step1-valid-2-reject-txt.png`, `bug-reports/image/BUG-IBMHD_04-step2-bang-kiem-tra.png`

**Kết luận QA**

- `IBMHD_04` tái hiện đúng phần "tệp lỗi không có trong bảng kiểm tra" — nhưng KHÔNG "im lặng": app báo lý do tại bước chọn.
- App đạt yêu cầu nghiệp vụ (thông báo tệp lỗi + lý do trước khi import) nhưng lệch đặc tả màn SCR-VII-03 #4/#5 (kỳ vọng Lỗi thành dòng + đếm trong bảng).
- Kỳ vọng "kèm lý do trong bảng" của đối tác vượt SRS (SCR-VII-03 #4 không có cột Lý do).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt mô hình kiểm tra tệp lỗi:

- **Hướng 1 (theo literal SCR-VII-03 #4/#5):** tệp lỗi phải hiện thành dòng "Lỗi" trong Bảng kiểm tra + đếm ở Thống kê "Lỗi: {Y}" → app hiện tại `Vẫn lỗi`, owner `Dev FE`.
- **Hướng 2 (chấp nhận early-validation):** app báo lỗi + lý do tại bước chọn là đủ (đạt mục tiêu nghiệp vụ) → app hiện tại `Đúng`, owner `QA/BA` cập nhật SCR-VII-03 + expected đối tác (bỏ kỳ vọng "kèm lý do").
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 118), chưa gửi Dev tới khi BA chốt.

---

## IBMHD_07 — Import lô có tệp lỗi → không hiện "{Y} tệp lỗi: xem chi tiết"

**Bối cảnh testcase**

- Dòng Excel: 119, mã TC `IBMHD_07`.
- Nội dung kiểm tra: CB Nghiệp vụ import một lô có cả tệp hợp lệ + tệp lỗi, xem kết quả import.
- Expected trong file UAT: kết quả import hiện "{Y} tệp lỗi: xem chi tiết" + bảng chi tiết lý do lỗi.
- Actual đối tác ghi: không hiện thông báo tệp lỗi + bảng chi tiết.

**Đối chiếu SRS v3.5**

- FR-VII-06 §Processing bước 4-5: "Với mỗi file lỗi: ghi vào báo cáo lỗi" → "Trả về tổng hợp: N thành công, M lỗi".
- Error Handling E2 (WRN-IMP-01): "Import thành công {N} file. **{M} file lỗi: xem chi tiết**".
- Outputs `chi_tiet_loi` structured `[{file_ten, ly_do}]` — "Khi có lỗi".
- Postcondition + AC: "File lỗi được ghi vào báo cáo chi tiết"; "Given 1+ file lỗi When import Then báo cáo lỗi chi tiết, import các file hợp lệ còn lại"; "hiển thị tổng hợp: N file thành công, M file lỗi".

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:479` (E2 WRN-IMP-01)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:489` (Outputs chi_tiet_loi)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:498-499` (AC — báo cáo lỗi chi tiết + tổng hợp N/M)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ.
- Vì app validate định dạng/kích thước SỚM ở bước chọn (xem IBMHD_04), **tệp lỗi không tới được bước Import** → tới bước import chỉ còn tệp hợp lệ → kết quả chỉ hiện "Đã nhập thành công 2 biểu mẫu" (không có nhánh "{M} tệp lỗi").
- Thử import trùng tên (duplicate): app **chấp nhận**, không coi là lỗi → cũng không sinh nhánh lỗi.
- Không tái hiện được lỗi phát sinh TẠI bước import trong luồng thường.
- **Giới hạn kiểm thử (honest):** chưa thử được loại lỗi chỉ phát sinh ở bước import (vd file .docx đúng đuôi nhưng nội dung hỏng / lỗi ghi DB). Nhánh "{M} tệp lỗi" có thể vẫn tồn tại cho các lỗi này — chưa reproduce.
- Evidence: `bug-reports/image/BUG-IBMHD_07-step3-ket-qua-import.png`

**Kết luận QA**

- `IBMHD_07`: nhánh "{M} tệp lỗi: xem chi tiết" (E2) không kích hoạt trong luồng nhập thường vì lỗi định dạng/kích thước đã bị chặn sớm; duplicate không bị coi là lỗi.
- Chưa khẳng định app THIẾU nhánh này (có thể vẫn có cho lỗi import-time chưa test được).

**Nội dung đề xuất BA phản hồi đối tác**

- **Hướng 1:** nếu SRS bắt buộc nhánh "{M} tệp lỗi" luôn có (vd cả với lỗi định dạng), thì mô hình kiểm-sớm hiện tại chưa đạt AC → cần Dev bổ sung / đổi điểm kiểm → `Cần Dev BE/FE`.
- **Hướng 2:** nếu chấp nhận app catch lỗi định dạng/kích thước ở bước chọn (chỉ giữ nhánh {M} lỗi cho lỗi import-time), thì cần một test-case tạo lỗi import-time để xác minh nhánh — QA sẽ seed file hỏng để verify tiếp.
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 119). Đề nghị BA xác nhận mô hình kiểm-sớm có đạt AC "báo cáo lỗi chi tiết" không.

---

## IBMHD_11 — Nút "Hủy" màn Import không hiện hộp xác nhận

**Bối cảnh testcase**

- Dòng Excel: 121, mã TC `IBMHD_11`.
- Nội dung kiểm tra: CB Nghiệp vụ đã chọn thư mục + tải tệp lên màn Nhập hàng loạt, bấm "Hủy".
- Expected trong file UAT: bấm "Hủy" hiện hộp xác nhận (tránh mất tệp đã tải).
- Actual đối tác ghi: không hiện hộp xác nhận.

**Đối chiếu SRS v3.5**

- FR-VII-06 (toàn UC, `:444-508`) đặc tả Inputs / Processing / Error / AC — KHÔNG đề cập nút "Hủy" lẫn hành vi xác nhận khi hủy.
- SCR-VII-03 §Thành phần màn hình (`:670-677`) liệt kê 6 thành phần (Thư mục đích, Excel metadata, Tải nhiều file, Bảng kiểm tra, Thống kê, Nút xác nhận) — **không có nút "Hủy"** và không có yêu cầu hộp xác nhận khi hủy.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:444-508` (FR-VII-06 — không có nút Hủy)
- `input/srs-update-2026-5-5/srs-fr-09-bieu-mau.md:670-677` (SCR-VII-03 Thành phần — không có nút Hủy / hộp xác nhận)

**Kết quả verify UI hiện tại**

- Verify 20/07/2026 qua Chrome DevTools MCP, `cbnv_bn` / CB Nghiệp vụ.
- Đã chọn thư mục + tải 1 tệp (có thay đổi chưa lưu) → bấm "Hủy" → **điều hướng NGAY** sang `/bieu-mau/danh-sach`, KHÔNG có modal xác nhận (điều hướng tức thì = không có modal chặn).
- Tái hiện đúng claim đối tác.
- Evidence: `bug-reports/image/BUG-IBMHD_11-huy-navigated-no-confirm.png`

**Kết luận QA**

- `IBMHD_11` tái hiện đúng: Hủy rời màn ngay, không xác nhận, kể cả khi đã tải tệp.
- Nhưng SRS **không quy định** nút Hủy phải có hộp xác nhận → kỳ vọng của đối tác chưa có cơ sở SRS. Đây là gap yêu cầu (SRS thiếu đặc tả), không phải app sai so với SRS hiện có.

**Nội dung đề xuất BA phản hồi đối tác**

- Đề nghị BA quyết có bổ sung yêu cầu "hộp xác nhận trước khi Hủy khi đã tải tệp" vào SRS không (UX chống mất dữ liệu vô ý).
- Nếu **có** → owner `Dev FE` thêm Popconfirm + `BA` bổ sung SRS. Nếu **không** → app hiện tại đúng, cập nhật expected đối tác.
- Verdict QA đề xuất: `Cần BA xác nhận` (đã ghi sheet dòng 121). Chưa gửi Dev tới khi BA chốt.
