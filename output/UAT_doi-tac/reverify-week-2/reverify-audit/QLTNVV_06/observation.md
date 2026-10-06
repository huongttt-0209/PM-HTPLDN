# Quan sát real-data — QLTNVV_06 (Xuất Excel)

**Cách lấy bằng chứng:** file Excel do web tự sinh (export chạy client-side, không có API call). Đã hook `URL.createObjectURL` để bắt đúng blob web tạo ra → giải mã thành .xlsx thật → đọc bằng `openpyxl`. Không dựng lại file, không suy đoán.

## File thu được

- `vu-viec-export-web.xlsx` — không lọc, 9 dòng dữ liệu (7.427 bytes).
- `vu-viec-export-web-loc-EEE.xlsx` — lọc từ khóa "EEE" → **4 dòng dữ liệu**, khớp đúng 4 kết quả trên màn hình ⇒ **BR-DATA-06 (xuất theo bộ lọc hiện tại) ĐẠT**.

## Header 11 cột (giống hệt file trong video đối tác, khung t=24s)

A "Mã vụ việc" · B "Tiêu đề" · C "Doanh nghiệp" · D "Lĩnh vực" · E "Trạng thái" · F "Kênh tiếp nhận" · G "Ưu tiên" · H "Mức cảnh báo" · I "Deadline" · J "Ngày tiếp nhận" · K "Người hỗ trợ"

## Đối chiếu 9 cột đang hiển thị trên màn danh sách → file Excel

- "Mã VV" → A "Mã vụ việc" ✅
- "Tên DN" → C "Doanh nghiệp" ✅
- "Lĩnh vực PL" → D "Lĩnh vực" ✅
- "Kênh tiếp nhận" → F "Kênh tiếp nhận" ✅
- "Trạng thái" → E "Trạng thái" ✅
- "Người xử lý / Tổ chức" → K "Người hỗ trợ" ✅
- "Ngày tiếp nhận" → J "Ngày tiếp nhận" ✅
- "Deadline thời hạn" → I "Deadline" ✅
- **"Cảnh báo thời hạn" → H "Mức cảnh báo" ✅ CÓ — KHÔNG THIẾU** (giá trị thực: "Bình thường", "Quá hạn nghiêm trọng")
- 2 cột thừa so với màn hình: B "Tiêu đề", G "Ưu tiên"

## Kết luận từng ý

1. **"Thiếu cột thông tin Cảnh báo thời hạn" → KHÔNG tái hiện (Reject ý này).** Cột có thật (cột H "Mức cảnh báo") và có dữ liệu. Chính video đối tác khung t=24s cũng hiển thị cột H "Mức cảnh báo" = "Quá hạn nghiêm trọng" → đối tác nhìn nhầm/không nhận ra vì tên cột khác nhãn trên màn hình.
2. **"Tên cột không đúng thiết kế" → BA confirm.** Tên cột trong file Excel khác nhãn trên màn danh sách ("Deadline" vs "Deadline thời hạn"; "Mức cảnh báo" vs "Cảnh báo thời hạn"; "Doanh nghiệp" vs "Tên DN"; "Người hỗ trợ" vs "Người xử lý / Tổ chức"). Nhưng **SRS không quy định danh sách/tên cột file Excel** cho nhóm Vụ việc:
   - SCR-V.I-01 chỉ nêu toolbar có nút [Xuất Excel] (`srs-fr-05-vu-viec.md` dòng 1620).
   - BR-DATA-06 (`srs-v3.5.md` dòng 5434) chỉ ràng buộc: "xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows".
   - Đối chiếu: module TVV có FR-IV-02 §Processing bước 4 (`srs-fr-04` dòng 243) quy định rõ **10 cột cố định** → SRS CÓ quy định cột khi muốn; FR-V.I thì không.

**Verdict tổng:** không có ý nào Open; ý 2 là BA confirm ⇒ **BA confirm** (theo quy tắc: không Open mà còn BA confirm → lấy BA confirm, không Reject cả case).
