# Tiêu chí chấm — TKTMBMHD_04 (dòng 89)

> Round 7 · 2026-07-25. **CẤM tự đặt tiêu chí khác.** Chấm theo đúng 2 khối dưới:
> (A) bar gốc dev đặt ở round trước, (B) các lỗi CÒN LẠI mình đã ghi cho đối tác ở lượt Reopen gần nhất.
> PASS = (A) đủ điều kiện PASS **và** (B) không còn gạch đầu dòng nào tái hiện.

## Case gốc (đối tác)
- **Mô tả:** Kiểm tra Điều kiện tìm kiếm / bộ lọc
- **Điều kiện:** 1. Đăng nhập tài khoản
- **Các bước:** 1. Chọn menu "Biểu mẫu" -> "Thư mục biểu mẫu"
- **KQ mong đợi:** - Hệ thống hiển thị các trường thông tin giống với thiết kế
- Dữ liệu hiển thị đúng định dạng và trường thông tin
- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị
- Giá trị mặc định của các trường thông tin có kiểu dữ liệu Danh sách chọn là Tất cả
- **KQ thực tế (đối tác báo):** - Giá trị mặc định của các trường thông tin có kiểu dữ liệu Danh sách chọn là rỗng

## (A) Bar gốc của DEV — bộ "CÁCH VERIFY" đã chốt

✅ Bug đúng (BA duyệt 24/07/2026). Loại 2 — SRS đã được chốt sửa, Dev FE làm theo bản mới.
Yêu cầu nghiệp vụ: hai ô lọc dạng danh sách chọn trên màn Thư viện biểu mẫu > Thư mục (Lĩnh vực và Trạng thái) phải có sẵn một mục "Tất cả", và mục đó được chọn sẵn làm giá trị mặc định khi mở màn — thay vì để ô trắng chỉ có chữ gợi ý mờ. Người dùng phải đọc được trên ô rằng hiện đang không lọc, và xóa nhanh lựa chọn lẻ bằng cách chọn lại "Tất cả".
Căn cứ SRS: srs-v3.5/srs-fr-09-bieu-mau.md:619 (SCR-VII-01 #4 Lọc lĩnh vực — "Lĩnh vực PL (từ UC99). Mặc định: "Tất cả""), :620 (#5 Lọc trạng thái — "Tất cả / NHAP / CONG_KHAI / AN"), và §Inputs FR-VII-02 đã được sửa cho khớp: :168 (linh_vuc_id, cột Mặc định = "Tất cả (không lọc)"), :171 (trang_thai, Mặc định = "Tất cả (không lọc)"). Quy ước dùng chung srs-v3.5/srs-v3.5.md:580 (UI-11) cũng yêu cầu ô lọc chọn có một mục "Tất cả". (BA trích :163/:166 theo bản SRS trước khi cập nhật; số dòng hiện hành là :168/:171.) Mức Minor.

── CÁCH VERIFY sau Dev fix ──
Precondition: cbnv_tw / Test@1234 (CB Nghiệp vụ Trung ương) · https://18.143.165.120.nip.io/bieu-mau/thu-muc · mở URL sạch, KHÔNG kèm tham số tab / keyword / bộ lọc trên URL.
1) Mở URL trên, chưa bấm gì cả, đọc chữ đang hiển thị trong ô lọc "Lĩnh vực" và ô lọc "Trạng thái".
2) Mở dropdown ô "Trạng thái", đếm số mục và đọc mục đầu tiên.
3) Mở dropdown ô "Lĩnh vực", đọc mục đầu tiên (trước nhóm các lĩnh vực Thuế / Lao động / Đất đai...).
4) Ở ô "Trạng thái" chọn "Nháp" (danh sách co lại), rồi chọn lại "Tất cả".
✅ PASS khi ĐỦ 4 điều: (i) bước 1 cả hai ô hiển thị chữ "Tất cả" ở dạng giá trị đã chọn (chữ đậm như khi có lựa chọn), không phải chữ mờ gợi ý "Lĩnh vực" / "Trạng thái"; (ii) bước 2 dropdown Trạng thái có đúng 4 mục — Tất cả, Nháp, Đã công khai, Đã ẩn — và "Tất cả" đứng đầu; (iii) bước 3 dropdown Lĩnh vực có mục "Tất cả" đứng trước toàn bộ lĩnh vực; (iv) bước 4 chọn lại "Tất cả" thì danh sách trở về đủ số thư mục như lúc mới mở màn.
❌ FAIL nếu: ô lọc chỉ hiện chữ mờ gợi ý khi mới mở màn; HOẶC dropdown không có mục "Tất cả"; HOẶC có mục "Tất cả" nhưng khi mở màn nó không được chọn sẵn.
⚠️ Đừng lấy "danh sách vẫn ra đủ thư mục" làm bằng chứng PASS — để ô trắng cũng ra đủ thư mục. Case này chấm giá trị hiển thị trên ô lọc và sự tồn tại của mục "Tất cả" trong dropdown.
⚠️ Không nhầm hai ô lọc này với dãy tab phân loại phía trên bảng (Tất cả / Đã công khai / Nháp / Đã ẩn, srs-v3.5/srs-fr-09-bieu-mau.md:623). Tab là control khác và thuộc case TKTMBMHD_07.

## (B) Lỗi CÒN LẠI sau lượt Reopen gần nhất (nội dung đang nằm ở cột R của sheet)

- Mở màn Thư viện biểu mẫu > Thư mục lần đầu: hai ô lọc "Lĩnh vực" và "Trạng thái" đã đổi chữ hiển thị thành "Tất cả", nhưng vẫn là chữ gợi ý mờ (xám nhạt) chứ chưa phải giá trị đang được chọn. Khi người dùng thực sự chọn một mục thì chữ mới đậm lên — nên nhìn vào ô lọc lúc mới mở màn vẫn không biết đang để "Tất cả" hay đang bỏ trống.
- Mở danh sách chọn của ô "Lĩnh vực": chỉ có 10 lĩnh vực (Thuế, Lao động, Đất đai, Dân sự, Thương mại, Hình sự, Hành chính, Sở hữu trí tuệ, Doanh nghiệp, Đầu tư), KHÔNG có mục "Tất cả".
- Ô "Trạng thái" đã có đủ 4 mục (Tất cả / Nháp / Đã công khai / Đã ẩn) và "Tất cả" đứng đầu — phần này đạt; nhưng lúc mới mở màn mục "Tất cả" không được đánh dấu là đang chọn.
- Chọn Trạng thái = Nháp rồi chọn lại "Tất cả" thì danh sách trở về đủ 4 thư mục — phần này đạt.
- Kiểm tra ngày 25/07/2026, tài khoản CB Nghiệp vụ Trung ương.
