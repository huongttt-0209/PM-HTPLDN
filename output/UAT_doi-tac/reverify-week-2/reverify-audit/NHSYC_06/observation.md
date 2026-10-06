# Quan sát real-data — NHSYC_06 (Tệp đính kèm vi phạm quy định)

## Ràng buộc SRS

- **FR-V.I-04 (UC54) §Inputs #9** (`srs-fr-05-vu-viec.md` dòng 320): `file_scan` — PDF/DOC/DOCX/JPG/PNG, **max 20MB/file, tổng 100MB, max 10 file** (quét virus).
- **FR-V.I-04 §Error Handling E3** (dòng 355): `ERR-NH-03` — *"File vượt quá dung lượng/số lượng cho phép hoặc sai định dạng"* | severity ERROR.
- Kết quả mong đợi của test case: *"Hệ thống dừng gửi và hiển thị thông báo 'Tệp vượt quá dung lượng/số lượng cho phép hoặc sai định dạng'."*

## Kết quả tự chạy 4 nhánh vi phạm (tải tệp thật, bắt toast bằng MutationObserver)

| # | Nhánh vi phạm | Tệp dùng | Hệ thống có chặn? | Thông báo hiển thị | Kết luận |
|:-:|---|---|:-:|---|:-:|
| 1 | **Sai định dạng** | `sai-dinh-dang.txt` | ✅ Có — không thêm vào danh sách | *"sai-dinh-dang.txt: Định dạng không được hỗ trợ. Chấp nhận: .doc, .docx, .xls, .xlsx, .pdf, .jpg, .png, .gif"* | ✅ **ĐẠT** |
| 2 | **Vượt 20MB/tệp** | `qua-dung-luong-25mb.pdf` (25MB) | ✅ Có — không thêm vào danh sách | *"qua-dung-luong-25mb.pdf: Kích thước vượt quá giới hạn 20MB."* | ✅ **ĐẠT** |
| 3 | **Vượt 10 tệp** | tải tệp thứ **11** (`hople-11.pdf`, PDF hợp lệ) sau khi đã có 10 tệp | ⚠️ Có chặn (danh sách giữ nguyên 10) | **KHÔNG CÓ thông báo nào** — observer bắt được **0 toast**; tệp thứ 11 biến mất im lặng | ❌ **LỖI** |
| 4 | **Vượt tổng 100MB** | 6 tệp × 18MB = **108MB** (mỗi tệp <20MB nên không phạm rule/tệp) | ❌ **KHÔNG chặn** — nhận đủ 6/6 tệp | **KHÔNG CÓ thông báo nào** | ❌ **LỖI** |

⇒ **2/4 ràng buộc SRS không được thực thi đúng.** Cả 2 nhánh lỗi đều **im lặng** — vi phạm ERR-NH-03 (SRS bắt buộc hiển thị thông báo).

## Ghi chú trung thực (không log thành bug)

1. **Lần tải đầu của `tong-18mb-2.pdf` báo "Tải file thất bại"** rồi tải lại lần 2 thì thành công. Đây là lỗi **không tái hiện ổn định** (4 tệp 18MB khác cùng lúc vẫn lên bình thường) → **không log bug**, chỉ ghi nhận để dev biết có khả năng chập chờn khi tải tệp lớn.
2. **Danh sách tệp đã tải chỉ hiển thị tên tệp**, không có Kích thước / Ngày upload như SCR-V.I-02 row 27 (dòng 1688) yêu cầu. **Nằm ngoài phạm vi phản ánh của đối tác ở case này** → không log vào case này, nêu riêng cho user quyết.
3. **Định dạng `.gif` được chấp nhận** nhưng không nằm trong danh sách SRS nào: FR-V.I-04 #9 ghi PDF/DOC/DOCX/JPG/PNG (không có XLS/XLSX/GIF); SCR-V.I-02 row 26 (dòng 1687) ghi doc/docx/xls/xlsx/pdf (không có JPG/PNG/GIF). **SRS tự mâu thuẫn về danh sách định dạng** → tách sang BA confirm.

**Verdict: Open** (nhánh 3 + 4).
