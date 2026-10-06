# Bảng đối chiếu điều kiện — IBMHD_02

Loại bug: **Màn Import thiếu trường "Tệp Excel mô tả dữ liệu" + nút "Tải mẫu Excel".** Verdict phụ thuộc: (1) tái hiện đúng màn/role, (2) SRS có yêu cầu thành phần này không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 1 "Chọn file" | Cùng màn | Không |
| Thao tác | Mở màn Nhập hàng loạt | Cùng | Không |
| Giá trị quan sát | Màn chỉ có "Thư mục đích" + "Tải lên file biểu mẫu" (.doc/.docx/.xls/.xlsx); KHÔNG có trường Excel metadata + nút "Tải mẫu Excel" | Y hệt — ảnh partner `IBMHD_02.jpg` khớp 100% màn hiện tại (`BUG-IBMHD_02-03-import-screen-step1.png`) | Không |

**Kết luận: 0 GAP.** Tái hiện đúng — màn thực sự thiếu trường Excel metadata + nút Tải mẫu Excel. Nhưng **SRS tự mâu thuẫn**: SCR-VII-03 mục #2 (`srs-fr-09-bieu-mau.md:673`) yêu cầu "Tải file Excel metadata | .xlsx (max 5MB), Template: [Tải mẫu Excel] | luôn hiển thị"; trong khi FR-VII-06 §Inputs (`:458–461`) chỉ có `thu_muc_id` + `files`, không có metadata Excel, và không bước Processing nào (`:463–472`) tiêu thụ metadata. App hiện theo FR-VII-06. → **BA confirm (Dạng B — SRS tự mâu thuẫn)**.

> Ghi chú vai trò (nội bộ): case chỉ định vai trò "CB Nghiệp vụ" (không phân cấp). Test bằng `cbnv_bn` (CB Nghiệp vụ - Bộ ngành) do `cbnv_tw` đang bị session khác chiếm liên tục (MailHog ~10 login 15:43–16:00). Bug này là thành phần render UI của màn Import — không phụ thuộc đơn vị (TW/BN chỉ khác data scope thư mục, không đổi cấu trúc màn). Ảnh đối tác chụp trên TW khớp 100% màn `cbnv_bn` → xác nhận render giống nhau ở cả 2 cấp.
