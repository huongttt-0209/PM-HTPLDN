# Nhật ký đo — QLHSPLDN_07 (dòng 325) — vòng 2, 04/08/2026

**Bản dựng đang chạy:** `assets/index-DpIXRGaI.js` · `HTPLDN · V1.0.5`. **Tài khoản:** `cb_nv_tw_01` (`CB_NV_TW`, TW, Cục Bổ trợ tư pháp).
**Lỗi gốc cần kiểm:** bấm Lưu thì báo cập nhật thành công nhưng dữ liệu không vào bản ghi; video đối tác cho thấy tệp vừa đính kèm biến mất khi mở lại.

**Nguyên tắc áp dụng:** đây là lỗi về **trường lưu trong cơ sở dữ liệu**, nên phép thử quyết định là **tạo bản ghi MỚI qua luồng chuẩn rồi sửa ngay**, không chỉ sửa bản ghi cũ.

| Giờ (VN) | Thao tác | Số liệu đo được |
|---|---|---|
| 14:43 | **Tạo bản ghi mới** qua nút "Thêm hồ sơ" của DN-XX-0005: điền 8 ô + đính kèm `hspl-goc-v2.png` | Bộ bắt thông báo tự kiểm `soObserverDangSong = 1`. Bấm "Đồng ý" lúc `07:43:18.086Z` → 1 request `POST /api/v1/ho-so-phap-ly-dns`, 1 khung "Thêm hồ sơ thành công". Bản ghi `HSPL-20260804-0001`, `version 1`, `coFile true`. |
| 14:44 | Bấm "Sửa" trên bản ghi vừa tạo | Cửa sổ "Sửa hồ sơ pháp lý" **điền sẵn đủ 9/9 ô** đúng giá trị hiện có (kể cả tệp đã đính kèm) — đạt vế 1 của Kết quả mong đợi. |
| 14:44 | Sửa **8 ô thuộc 4 kiểu**: chữ (Tên hồ sơ, Cơ quan cấp) · chữ dài (Mô tả) · ngày (Ngày cấp 01/08→05/08, Ngày hết hạn 31/12→30/11) · chọn (Loại Giấy phép→Quyết định, Lĩnh vực Thuế→Lao động, Trạng thái Hiệu lực→Hết hạn); **thêm tệp** `hspl-them-khi-sua-v2.png` | Danh sách tệp trong biểu mẫu hiện đủ 2 tệp trước khi lưu. |
| 14:44:24 | Bấm "Đồng ý" | `soObserverDangSong = 1`; **1 request** `PATCH /api/v1/ho-so-phap-ly-dns/1eada753-…`, **1 khung** "Cập nhật hồ sơ thành công" — không gửi 2 lần, không thông báo lặp. |
| 14:44 | Đọc thẳng bản ghi từ máy chủ | Cả 8 ô đều là **giá trị MỚI**; `fileDinhKem` có **2 tệp** (`hspl-them-khi-sua-v2.png`, `hspl-goc-v2.png`, mỗi tệp 70 B, `trangThaiQuet: SACH`); `version 1 → 2`; `ngayCapNhat 07:44:24.601Z` (khớp giây bấm); `nguoiCapNhatId` = tài khoản đang thao tác → lưu vết đạt. |
| 14:45 | **Tải lại trang bỏ bộ nhớ đệm**, mở lại chính hồ sơ đó | Dòng trong bảng và cửa sổ chi tiết đều hiện giá trị mới; mục tệp có đủ 2 tệp. Ảnh `image/QLHSPLDN_07-v2-01-…png`. |
| 14:45 | **Kiểm thêm bản ghi CŨ** `HSPL-20260731-0002` (tạo 31/07, trước bản vá): đổi Tên hồ sơ + thêm tệp `hspl-cu-them-tep-v2.png` | Khung "Cập nhật hồ sơ thành công". Máy chủ: tên mới, `version 1 → 2`, `ngayCapNhat 07:45:32.395Z`, tệp mới có thật. |
| 14:46 | Tải lại trang, mở lại bản ghi cũ | Tên mới + tệp mới còn nguyên; cột "Có tệp đính kèm" đổi từ "Không" sang "Có". Ảnh `image/QLHSPLDN_07-v2-02-…png`. |

**Một ghi chú về dụng cụ đo (không phải lỗi phần mềm):** ở lượt sửa bản ghi cũ tôi chỉ bọc `fetch` mà quên bọc `XMLHttpRequest`, nên bộ đếm hiện `SO_REQUEST = 0` — đây là thiếu sót của bộ đo, không phải app không gọi máy chủ; đã đối chứng bằng cách đọc lại bản ghi từ máy chủ (`version` tăng, `ngayCapNhat` đúng giây bấm).

**Kết luận: Pass** — cả 3 vế đều đạt: mở cửa sổ với dữ liệu hiện có, dữ liệu sửa lưu thật (bản ghi mới lẫn bản ghi cũ, cả tệp đính kèm), và có lưu vết thao tác.
