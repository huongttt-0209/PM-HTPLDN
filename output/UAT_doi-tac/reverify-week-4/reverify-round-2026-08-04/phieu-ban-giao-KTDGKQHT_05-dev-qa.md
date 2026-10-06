# Phiếu bàn giao thay đổi SRS — Nhập kết quả học tập qua Excel (KTDGKQHT_05)

| | |
|---|---|
| **Mã** | KTDGKQHT_05 |
| **Ngày** | 2026-08-04 |
| **Người gửi** | BA |
| **Nơi nhận** | DEV, QA |
| **Phạm vi** | FR-III-05 (Quản lý kiểm tra, đánh giá kết quả — UC24) + SCR-III-02 Tab 4/5 |
| **Tài liệu chuẩn** | `srs-fr-03-dao-tao.md` (commit `475ef02`) |
| **Thời điểm bàn giao** | Sau khi hoàn tất fix bug tuần 5 |

## 1. Bối cảnh

Kiểm thử độc lập phản ánh (KTDGKQHT_05): màn hình danh sách không hiển thị mã học viên, nhưng khi nhập tệp Excel điểm danh hệ thống lại bắt buộc có mã học viên — người dùng không có nguồn để biết mã mà điền.

Rà soát cho thấy đây là khe hở nghiệp vụ: import bắt buộc định danh học viên mỗi dòng nhưng không nơi nào trên giao diện cho người dùng lấy định danh đó, và SRS chưa định nghĩa tệp mẫu nhập. Đã cập nhật SRS theo hướng "Tải mẫu → điền → tải lên".

## 2. Tóm tắt thay đổi SRS

- Giữ `hoc_vien_id` làm khoá đối chiếu; **KHÔNG thêm trường vào entity HOC_VIEN**.
- Bổ sung cơ chế tệp mẫu: cán bộ không tự gõ định danh; hệ thống sinh tệp đã điền sẵn danh sách học viên.
- Áp cho **cả điểm danh và điểm kiểm tra** (luồng import dùng chung).

## 3. Việc DEV cần làm

### 3.1 Hai nút "Tải mẫu"
- **Tab 4 (Điểm danh):** nút **"Tải mẫu điểm danh"** — bật khi: đã chọn buổi học + khóa ở `DANG_DIEN_RA` + khóa có ≥1 buổi học + có quyền nhập điểm danh.
- **Tab 5 (Kết quả kiểm tra):** nút **"Tải mẫu điểm kiểm tra"** — bật khi: đã chọn đề kiểm tra thuộc khóa + khóa ở `DANG_DIEN_RA`/`DA_KET_THUC` + có quyền.

### 3.2 Sinh tệp mẫu
- Điền sẵn danh sách học viên của khóa.
- **Mẫu điểm danh — cột (thứ tự cố định):** `hoc_vien_id` (điền sẵn, **khoá/ẩn** — ID nội bộ, không cho sửa) · Họ tên · Email · Đơn vị · **Trạng thái điểm danh** (trống: Có mặt / Vắng có phép / Vắng không phép) · Ghi chú.
- **Mẫu điểm kiểm tra — cột:** `hoc_vien_id` (điền sẵn, khoá/ẩn) · Họ tên · Email · Đơn vị · **Điểm kiểm tra** (trống, 0–10) · Ghi chú.
- Nhúng `lich_hoc_id` (mẫu điểm danh) / `de_kiem_tra_id` (mẫu điểm kiểm tra) vào **metadata/tiêu đề tệp** — không phải cột từng dòng.

### 3.3 Import
- Xác định **loại bản ghi theo loại tệp mẫu** (không dựa vào có/không cột `lich_hoc_id` từng dòng nữa).
- Đọc `lich_hoc_id`/`de_kiem_tra_id` từ **metadata tệp**, bắt buộc **khớp buổi/đề đang chọn** trên màn; lệch → **ERR-KQ-09**.
- Validate `hoc_vien_id` phải **tồn tại VÀ thuộc khóa đang thao tác** (`HOC_VIEN.khoa_hoc_id` = khóa hiện tại); sai → **ERR-KQ-03**.
- Giữ nguyên các ràng buộc hiện có: trạng thái khóa (PRE-03/PRE-04, ERR-KQ-06), enum điểm danh (ERR-KQ-04), điểm 0–10 từ chối không kéo về biên (ERR-KQ-01), đề thuộc khóa (ERR-KQ-08); chỉ merge dòng hợp lệ.
- **Backend không tin dữ liệu định danh trong tệp** — luôn tự validate quyền + khóa + buổi/đề.

### 3.4 Thông báo lỗi
- **ERR-KQ-03** (đổi câu chữ): "Không tìm thấy học viên ở dòng {N} (định danh không hợp lệ hoặc không thuộc khóa học này)".
- **ERR-KQ-09** (mới): "Tệp mẫu không khớp buổi học / đề kiểm tra đang chọn. Vui lòng tải mẫu đúng và thử lại".

### 3.5 Phân biệt 2 tệp
- **Tệp mẫu nhập** (Tải mẫu) ≠ **tệp Xuất Excel kết quả** (báo cáo tổng hợp). Tệp Xuất kết quả KHÔNG dùng để nhập liệu.

## 4. Việc QA cần kiểm thử

| # | Kịch bản | Kết quả mong đợi |
|---|----------|------------------|
| 1 | Chọn buổi (Tab 4) → "Tải mẫu điểm danh" | Tải tệp điền sẵn danh sách HV, cột định danh khoá/ẩn, cột Trạng thái điểm danh để trống |
| 2 | Chọn đề (Tab 5) → "Tải mẫu điểm kiểm tra" | Tải tệp điền sẵn HV, cột Điểm kiểm tra để trống |
| 3 | Điền mẫu đúng buổi/đề đang chọn → tải lên | Import thành công, đối chiếu theo định danh sẵn trong tệp, merge dòng hợp lệ |
| 4 | Tải lên mẫu của **buổi/đề khác** với ngữ cảnh đang chọn | Từ chối kèm **ERR-KQ-09** |
| 5 | Tệp có dòng `hoc_vien_id` **không thuộc khóa** | Dòng đó báo **ERR-KQ-03**, bị bỏ qua |
| 6 | Điều kiện bật nút (chưa chọn buổi/đề; khóa `DA_KET_THUC` ở Tab 4; thiếu quyền; khóa chưa có buổi học) | Nút "Tải mẫu" **không bật** đúng theo điều kiện |
| 7 | Dùng tệp **Xuất Excel kết quả** để tải lên nhập | Bị từ chối (không đúng định dạng mẫu — ERR-KQ-02) |
| 8 | Hồi quy: nhập điểm danh/điểm thủ công trên bảng | Vẫn hoạt động bình thường, không cần gõ định danh |
| 9 | Hồi quy: import điểm ngoài 0–10 | Từ chối kèm ERR-KQ-01, **không tự kéo về biên 0/10** |

## 5. Tham chiếu
- SRS: `srs-fr-03-dao-tao.md` — FR-III-05 (§Processing "Tải mẫu", §Processing Import Excel, §Error Handling, §Acceptance Criteria) + SCR-III-02 Tab 4/5.
- Baseline: `srs-v3.5.md` dòng lịch sử 3.5.8; chi tiết tại `CHANGELOG-v3-to-v3.5.md`.
- Commit: `475ef02` "Chuẩn hoá nhập kết quả học tập qua Excel (KTDGKQHT_05)".
