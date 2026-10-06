# Đo lường — QLDX_01: Toast "Đăng xuất thành công" khi đăng xuất

**Phương pháp:** MutationObserver (Rule 8 — bắt element hiệu ứng ngắn, KHÔNG poll DOM), còn sống suốt thao tác đăng xuất; đẩy mỗi toast bắt được sang `sessionStorage` để dữ liệu tồn tại qua lần full-navigation về trang đăng nhập.

**Tài khoản:** cbpd_tw (đã đăng nhập thành công) · env https://18.143.165.120.nip.io

**Các bước:**
1. Đăng nhập thành công → dashboard.
2. Cài MutationObserver trên `document.body` (regex `ant-message-notice-wrapper|ant-notification-notice-wrapper`, đọc `innerText`, KHÔNG lọc trùng), persist sang `sessionStorage['__qa_logout_toasts']`.
3. Mở menu avatar → nhấn "Đăng xuất".
4. Sau khi hệ thống chuyển về `/login`, đọc lại `sessionStorage` + kiểm tra DOM trang login.

**Kết quả đo:**
- Toast bắt được phía dashboard (trong lúc đăng xuất): **0**.
- Toast trên trang `/login` sau redirect (ảnh chụp ngay + kiểm DOM ~0.8s): **0**.
- Điều hướng về `/login` xảy ra ngay sau khi nhấn "Đăng xuất".

**Kết luận:** KHÔNG có toast "Đăng xuất thành công" ở bất kỳ thời điểm nào của luồng đăng xuất. Yêu cầu (SRS `srs-fr-10-quan-tri.md:1003`, FR-VIII-21 UC119 Output #2 — message "Đăng xuất thành công") không được đáp ứng.

**Ảnh:** [BUG-QLDX_01-logout-no-toast.png](../bug-reports/dang-nhap-xuat/image/BUG-QLDX_01-logout-no-toast.png)
