# Bảng đối chiếu điều kiện — QLDMTCTV_OOS_10 (dòng 336) — 5 nhãn trường khác đặc tả

**Kết luận:** Pass — cả 5 nhãn đã đổi đúng đặc tả, giống nhau ở chế độ Thêm mới và Chỉnh sửa.

**Case thuần tĩnh.** Nhãn ô nhập là chuỗi cố định của biểu mẫu SCR-IV-NEW-02, dùng chung cho Thêm mới và Chỉnh sửa; đặc tả không có nhánh đổi nhãn theo vai trò hay theo trạng thái hồ sơ. Màn này chỉ mở được với Cán bộ Nghiệp vụ cùng đơn vị (dòng 1667) — đúng vai trò đã dùng để đo. Phép đo là đọc nguyên văn chữ nhìn thấy của từng nhãn rồi so từng chữ với đặc tả.

| # | Nhãn vòng 1 (sai) | Đặc tả yêu cầu | Nhãn đọc được 04/08/2026 (Thêm mới **và** Sửa) | Hết lỗi? |
|---|---|---|---|:-:|
| 1 | Chức vụ đại diện | Chức vụ người đại diện (dòng 1680) | **Chức vụ người đại diện** | ✔ |
| 2 | Ngày cấp | Ngày cấp Giấy đăng ký hành nghề (dòng 1682) | **Ngày cấp Giấy đăng ký hành nghề** | ✔ |
| 3 | Lĩnh vực pháp lý | Lĩnh vực pháp luật (dòng 1684) | **Lĩnh vực pháp luật** | ✔ |
| 4 | Địa chỉ | Địa chỉ trụ sở (dòng 1687) | **Địa chỉ trụ sở** | ✔ |
| 5 | Điện thoại | Số điện thoại (dòng 1688) | **Số điện thoại** | ✔ |

*(Phiếu gốc dẫn các dòng 1679/1682/1685/1687/1688; mở file đặc tả đối chiếu thì 2 mục lệch 1 dòng — nội dung nhãn vẫn đúng như bảng.)*

Không tính vào phiếu này: nhãn "Số Giấy ĐKHĐ Sở TP" (đã tách sang phiếu QLDMTCTV_OOS_13 chờ BA chốt, đúng như ghi chú vòng 1).

**Bằng chứng:**
- `image/QLDMTCTV_OOS_08-v2-02-them-moi-mo-het-6-nhom-phan-tren.png` — Thêm mới: đọc rõ "Chức vụ người đại diện", "Ngày cấp Giấy đăng ký hành nghề", "Lĩnh vực pháp luật".
- `image/QLDMTCTV_OOS_10-v2-01-them-moi-nhan-lien-he-va-cong-bo.png` — Thêm mới: "Địa chỉ trụ sở", "Số điện thoại", "Email", "Website".
- `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` — chế độ Sửa: cùng bộ nhãn.
- `image/QLDMTCTV_09-v2-02-sua-nhom-lien-he-cong-bo-tep-dinh-kem-du-3-truong.png` — chế độ Sửa: "Địa chỉ trụ sở", "Số điện thoại".
