# Bảng đối chiếu điều kiện — IBMHD_03

Loại bug: **Màn Import không có nút chức năng "Tải mẫu Excel".** Verdict phụ thuộc: (1) tái hiện đúng màn, (2) SRS có yêu cầu nút này không. Cùng gốc IBMHD_02.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 1 | Cùng màn | Không |
| Thao tác | Tìm nút "Tải mẫu Excel" | Cùng | Không |
| Giá trị quan sát | Không có nút "Tải mẫu Excel" | Y hệt — không có nút; ảnh partner `IBMHD_03.jpg` khớp màn hiện tại | Không |

**Kết luận: 0 GAP.** Tái hiện đúng — không có nút Tải mẫu Excel. Nút này là thành phần của trường "Tải file Excel metadata" trong SCR-VII-03 mục #2 (`srs-fr-09-bieu-mau.md:673`, "Template: [Tải mẫu Excel]"). FR-VII-06 §Inputs (`:458–461`) không có phần Excel metadata → không có Tải mẫu Excel. SRS tự mâu thuẫn giống IBMHD_02. → **BA confirm (Dạng B)**.

> Ghi chú vai trò (nội bộ): giống IBMHD_02 — case chỉ định vai trò "CB Nghiệp vụ"; test bằng `cbnv_bn` do `cbnv_tw` bị chiếm session. Thành phần render UI, không phụ thuộc đơn vị; ảnh đối tác (TW) khớp màn `cbnv_bn`.
