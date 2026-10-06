# Đo lường — QLDX_02: Hộp thoại xác nhận trước khi đăng xuất

**Phương pháp:** MutationObserver (Rule 8), còn sống suốt thao tác đăng xuất, bắt cả node `ant-modal-root|ant-modal-confirm|ant-modal-wrap`; persist sang `sessionStorage` để tồn tại qua full-navigation.

**Tài khoản:** cbpd_tw (đã đăng nhập thành công) · env https://18.143.165.120.nip.io

**Các bước:**
1. Đăng nhập thành công → dashboard.
2. Cài MutationObserver bắt cả toast lẫn modal, persist sang `sessionStorage['__qa_logout_modals']`.
3. Mở menu avatar → nhấn "Đăng xuất".
4. Quan sát: có modal xác nhận ("Bạn có chắc muốn đăng xuất...?") hiện ra trước khi đăng xuất không.

**Kết quả đo:**
- Modal xác nhận bắt được trong suốt thao tác: **0**.
- Ngay khi nhấn "Đăng xuất", hệ thống đăng xuất & điều hướng thẳng về `/login` — KHÔNG có bước xác nhận trung gian.
- Lặp lại với tài khoản admin (Quản trị hệ thống): kết quả giống hệt (đăng xuất ngay, không modal) → xác nhận hành vi độc lập vai trò.

**Kết luận:** KHÔNG có hộp thoại xác nhận đăng xuất. Yêu cầu (SRS `srs-fr-10-quan-tri.md:1883`, SCR-VIII-09 — luồng đăng xuất chủ động: Avatar → dropdown → "Đăng xuất" → **Modal xác nhận** → Hủy JWT → Redirect) không được đáp ứng.

**Ảnh:** [BUG-QLDX_01-logout-no-toast.png](../bug-reports/dang-nhap-xuat/image/BUG-QLDX_01-logout-no-toast.png) (màn đăng nhập ngay sau khi nhấn "Đăng xuất" — không qua bước xác nhận).
