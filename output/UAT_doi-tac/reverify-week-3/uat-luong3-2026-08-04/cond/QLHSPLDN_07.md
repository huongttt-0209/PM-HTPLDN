# Bảng đối chiếu điều kiện — QLHSPLDN_07 (dòng 325) — Sửa hồ sơ pháp lý doanh nghiệp, dữ liệu phải lưu thật

**Kết luận:** Pass — sửa xong dữ liệu ghi thật vào bản ghi, kể cả tệp vừa đính kèm; kiểm trên bản ghi mới tạo lẫn bản ghi cũ.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:43–14:46, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương | `cb_nv_tw_01` — `CB_NV_TW`, cấp TW, đơn vị Cục Bổ trợ tư pháp | Không |
| Màn hình / entity | Doanh nghiệp → chi tiết → thẻ "Hồ sơ pháp lý" → Sửa | Đúng 4 bước của phiếu, doanh nghiệp "Công ty TNHH Mẫu Test" (DN-XX-0005) | Không |
| **Tuổi bản ghi** (lỗi trường lưu trong CSDL: bản ghi cũ có thể vẫn hỏng dù đã vá) | Không nêu | Kiểm **2 bản ghi**: (a) bản ghi **tạo mới ngay trong lượt này** qua luồng chuẩn — `HSPL-20260804-0001`; (b) bản ghi **cũ tạo 31/07** — `HSPL-20260731-0002`. Cả hai đều lưu đủ | Không |
| Kiểu ô nhập (lỗi loại này thường chỉ dính một nhóm) | "dữ liệu chưa được cập nhật vào bản ghi" | Sửa đủ 8 ô thuộc 4 kiểu: ô chữ (Tên hồ sơ, Cơ quan cấp) · ô chữ dài (Mô tả) · ô ngày (Ngày cấp, Ngày hết hạn) · ô chọn (Loại hồ sơ, Lĩnh vực pháp lý, Trạng thái) | Không |
| Tệp đính kèm (đúng thao tác trong video đối tác) | Tệp vừa thêm biến mất khi mở lại | Thêm tệp mới khi Sửa trên **cả hai** bản ghi; sau khi tải lại trang tệp vẫn còn, đúng tên đúng dung lượng | Không |

**Bằng chứng:**
- `image/QLHSPLDN_07-v2-01-sau-tai-lai-trang-du-lieu-sua-va-tep-them-con-nguyen.png` — sau khi **tải lại trang bỏ bộ nhớ đệm**, mở lại `HSPL-20260804-0001`: cả 8 giá trị đều là giá trị MỚI (Tên "QA-HSPL-V2-0408-742199 DA SUA vong 2", Loại "Quyết định", Lĩnh vực "Lao động", Cơ quan cấp "Co quan cap DA SUA v2", Ngày cấp 05/08/2026, Ngày hết hạn 30/11/2026, Trạng thái "Hết hạn", Mô tả mới); mục Tệp đính kèm có **cả 2 tệp** — `hspl-them-khi-sua-v2.png` (tệp thêm lúc Sửa) và `hspl-goc-v2.png` (tệp lúc tạo).
- `image/QLHSPLDN_07-v2-02-ho-so-cu-sua-va-them-tep-cung-luu-duoc.png` — bản ghi cũ `HSPL-20260731-0002` sau khi Sửa + tải lại trang: tên đổi thành "Ho so x - SUA CU v2 742199", tệp `hspl-cu-them-tep-v2.png` còn nguyên, cột "Có tệp đính kèm" đổi từ "Không" sang "Có".
- Đọc thẳng bản ghi từ máy chủ (`GET /api/v1/ho-so-phap-ly-dns/{id}`) khớp từng ô với màn hình; `fileDinhKem` trả về đủ 2 tệp, mỗi tệp có `dungLuong 70`, `trangThaiQuet: SACH`.
- Lưu vết thao tác đạt: `version` 1 → 2, `ngayCapNhat` = `07:44:24.601Z` (đúng thời điểm bấm `07:44:24.528Z`), `nguoiCapNhatId` = tài khoản đang thao tác.
- Bộ bắt thông báo (`soObserverDangSong = 1`): 1 request `PATCH /api/v1/ho-so-phap-ly-dns/{id}` ứng với 1 khung "Cập nhật hồ sơ thành công" — không gửi 2 lần, không thông báo lặp.
- Vế đầu của "Kết quả mong đợi" cũng đạt: cửa sổ Sửa mở lên **điền sẵn đủ 9/9 ô** đúng giá trị hiện có của bản ghi.
