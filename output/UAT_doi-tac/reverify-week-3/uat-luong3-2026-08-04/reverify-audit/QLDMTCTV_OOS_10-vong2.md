# Re-verify vòng 2 — QLDMTCTV_OOS_10 (dòng 336, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, Cục Bổ trợ tư pháp – Bộ Tư pháp)
**Verdict:** ✅ Pass — **case thuần tĩnh** (đọc nhãn chữ của các ô nhập)

---

## Triệu chứng gốc cần kiểm — 5 nhãn khác đặc tả

| # | Nhãn vòng 1 (sai) | Nhãn đặc tả yêu cầu |
|---|---|---|
| 1 | Chức vụ đại diện | Chức vụ người đại diện (dòng 1680) |
| 2 | Ngày cấp | Ngày cấp Giấy đăng ký hành nghề (dòng 1682) |
| 3 | Lĩnh vực pháp lý | Lĩnh vực pháp luật (dòng 1684) |
| 4 | Địa chỉ | Địa chỉ trụ sở (dòng 1687) |
| 5 | Điện thoại | Số điện thoại (dòng 1688) |

*(Phiếu gốc ghi các số dòng 1679/1682/1685/1687/1688; mở file đặc tả đối chiếu thì 2 mục lệch 1 dòng — nội dung nhãn vẫn đúng như bảng trên.)*

## Vì sao case này không phụ thuộc vai trò / trạng thái

Nhãn ô nhập là chuỗi tĩnh của biểu mẫu SCR-IV-NEW-02, dùng chung cho Thêm mới và Chỉnh sửa; đặc tả không có nhánh đổi nhãn theo vai trò hay theo trạng thái hồ sơ. Màn này chỉ mở được với Cán bộ Nghiệp vụ cùng đơn vị (dòng 1667) — đúng vai trò đã dùng để đo.

## Nhật ký đo

### 13:46 — Chế độ Thêm mới: đọc nguyên văn 15 nhãn
Đọc chữ NHÌN THẤY của `.ant-form-item-label label` trên `/chuyen-gia-tvv/to-chuc/tao-moi`:

> Tên tổ chức · Loại hình · Người đại diện · **Chức vụ người đại diện** · Số Giấy ĐKHĐ Sở TP · **Ngày cấp Giấy đăng ký hành nghề** · **Lĩnh vực pháp luật** · Số lao động · **Địa chỉ trụ sở** · **Số điện thoại** · Email · Website · Số quyết định công bố · Ngày quyết định công bố · Ghi chú

Đối chiếu từng chữ với bảng trên: **5/5 nhãn đã đổi đúng đặc tả.**

Ảnh: `image/QLDMTCTV_OOS_08-v2-02-them-moi-mo-het-6-nhom-phan-tren.png` (đã mở đọc: thấy "Chức vụ người đại diện", "Ngày cấp Giấy đăng ký hành nghề", "Lĩnh vực pháp luật") và `image/QLDMTCTV_OOS_10-v2-01-them-moi-nhan-lien-he-va-cong-bo.png` (đã mở đọc: thấy "Địa chỉ trụ sở", "Số điện thoại", "Email", "Website", "Số quyết định công bố", "Ngày quyết định công bố").

### 13:50 và 14:01 — Chế độ Chỉnh sửa (2 hồ sơ)
Mở Sửa TC-BTP-TW-0001 và TC-BTP-TW-0003: danh sách 15 nhãn **giống hệt** chế độ Thêm mới, 5 nhãn cần kiểm đều đúng.
Ảnh: `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` (đã mở đọc: "Chức vụ người đại diện", "Ngày cấp Giấy đăng ký hành nghề", "Lĩnh vực pháp luật" trên màn Chỉnh sửa) và `image/QLDMTCTV_09-v2-02-sua-nhom-lien-he-cong-bo-tep-dinh-kem-du-3-truong.png` ("Địa chỉ trụ sở", "Số điện thoại").

### Ngoài phạm vi phiếu này — nhãn "Số Giấy ĐKHĐ Sở TP"
Web vẫn ghi "Số Giấy ĐKHĐ Sở TP" trong khi dòng 1681 gọi là "Số Giấy đăng ký hành nghề". Đúng như ghi chú vòng 1: phần tên gọi giấy này đã tách sang phiếu **QLDMTCTV_OOS_13** để BA chốt, **không tính vào phiếu OOS_10**.

### Kết luận
5/5 nhãn đã đổi đúng đặc tả, giống nhau ở cả Thêm mới và Chỉnh sửa ⇒ **Pass**.
