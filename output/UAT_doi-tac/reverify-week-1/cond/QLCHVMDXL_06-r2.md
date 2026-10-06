# Bảng đối chiếu điều kiện — QLCHVMDXL_06 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** Các tab "Đã duyệt", "Công khai", "Hoàn thành" hiển thị bảng danh sách thiếu cột "Nội dung".

**Evidence:** `QLCHVMDXL_07_v2.jpg` — chụp 21/07/2026 17:27, thanh địa chỉ `htpldn-uat.ospgroup.vn/hoi-dap?tab=DA_DUYET&page=1`, header **Cán bộ PD Trung ương · CB_PD_TW · BTP·TW**, thẻ **"Đã duyệt 6"** đang active, tiêu đề bảng đi thẳng từ "Mã HD" sang "Lĩnh vực PL" (không có cột "Nội dung"), chân bảng "Hiển thị 1-6 / 6 kết quả".

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ PD Trung ương (`CB_PD_TW`), đơn vị BTP · TW — đọc ở header ảnh | `cbpd_tw` / `CB_PD_TW`, đơn vị BTP · TW — **đúng vai trò, đúng cấp, đúng đơn vị** (đã đăng nhập lại đúng vai trò để đóng chênh lệch, không dùng lập luận thay thế) | Không |
| Môi trường | `htpldn-uat.ospgroup.vn` (thanh địa chỉ ảnh, chụp 21/07/2026 17:27) | Đúng `htpldn-uat.ospgroup.vn` — đăng nhập trực tiếp env đối tác ngày 27/07/2026 | Không |
| Màn hình + thẻ (tab) đang đứng | Màn "Quản lý hỏi đáp, vướng mắc pháp lý", thẻ **"Đã duyệt"** active (badge 6) | Đúng màn đó; kiểm cả 7 thẻ, trong đó có **"Đã duyệt"** (badge 6), "Công khai" (badge 4), "Hoàn thành" (badge 10) | Không |
| Tập dữ liệu nền | 6 bản ghi thẻ "Đã duyệt": HD-20260702-013, HD-20260702-002, HD-QA-R7-064, HD-20260510-006, HD-20260510-002, HD-20260509-010 | **Trùng khít 6 mã đó**, cùng thứ tự — xác nhận cùng tập dữ liệu, chưa bị đụng vào | Không |
| Bộ lọc | Không đặt bộ lọc nào (chỉ `tab=DA_DUYET&page=1`) | Không đặt bộ lọc nào — chỉ bấm chuyển thẻ | Không |

**Kết luận:** 0 GAP — tái hiện trên **chính môi trường đối tác**, **đúng vai trò `CB_PD_TW`**, đúng thẻ, đúng tập dữ liệu.

Ghi nhận thêm: đã đo trước bằng vai trò `CB_NV_TW` rồi đăng nhập lại bằng `CB_PD_TW` để đóng chênh vai trò. **Hai vai trò cho kết quả y hệt** (cột "Nội dung" bề rộng 0 px ở đúng 3 thẻ 13 cột, 268 px ở 4 thẻ 11 cột) — lỗi không phụ thuộc quyền.

Phép đo đầy đủ (bề rộng từng cột × 7 thẻ) + đối chiếu SRS: xem [`../bug-reports/hoi-dap/Pass-bug-report-hoi-dap-r2.md`](../bug-reports/hoi-dap/Pass-bug-report-hoi-dap-r2.md) §BUG-QLCHVMDXL-COT-NOIDUNG.
