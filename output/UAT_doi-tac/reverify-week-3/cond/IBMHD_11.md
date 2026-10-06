# Bảng đối chiếu điều kiện — IBMHD_11

Loại bug: **Nút "Hủy" trên màn Import không hiện cửa sổ xác nhận.** Verdict phụ thuộc: (1) tái hiện đúng, (2) SRS có yêu cầu confirm khi hủy không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (case chỉ định vai trò "CB Nghiệp vụ") | CB Nghiệp vụ (`cbnv_bn`) — cùng vai trò case yêu cầu | Không |
| Màn hình | `/bieu-mau/nhap-hang-loat` bước 1 | Cùng | Không |
| Thao tác | Chọn thư mục + upload tệp → bấm "Hủy" | Chọn thư mục + upload 1 tệp (có thay đổi chưa lưu) → bấm "Hủy" | Không |
| Giá trị quan sát | "Không hiển thị cửa sổ xác nhận" | Y hệt — bấm "Hủy" → điều hướng NGAY sang `/bieu-mau/danh-sach`, KHÔNG có modal xác nhận (điều hướng tức thì = không có modal chặn) | Không |

**Kết luận: 0 GAP — tái hiện đúng.** Bấm "Hủy" rời màn Import ngay, không hiện hộp xác nhận, kể cả khi đã tải tệp lên (chưa import). **Tuy nhiên SRS không có cơ sở**: FR-VII-06 (`srs-fr-09-bieu-mau.md:444–508`) và màn SCR-VII-03 §Thành phần màn hình (`:670–677`) KHÔNG liệt kê nút "Hủy" lẫn yêu cầu xác nhận khi hủy. Kỳ vọng của đối tác (Hủy phải confirm) không được SRS quy định. → **BA confirm** (BA chốt có cần hộp xác nhận trước khi hủy — tránh mất tệp đã tải — hay không). Bằng chứng: `BUG-IBMHD_11-huy-navigated-no-confirm.png`.

> Ghi chú vai trò (nội bộ): case chỉ định vai trò "CB Nghiệp vụ"; test bằng `cbnv_bn` do `cbnv_tw` bị chiếm session. Hành vi nút Hủy (điều hướng client-side) không phụ thuộc đơn vị.
