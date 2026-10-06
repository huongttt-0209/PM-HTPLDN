# Re-verify vòng 2 — QLDMTCTV_09 (dòng 320, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

**Ngày:** 2026-08-04 · **Môi trường:** https://htpldn-uat.ospgroup.vn (bản dựng UAT mới)
**Bản dựng đo được:** `assets/index-DpIXRGaI.js` · nhãn sidebar `HTPLDN · V1.0.5`
**Tài khoản:** `cbnv_tw` / `Test@1234` (`CB_NV_TW`, Cục Bổ trợ tư pháp – Bộ Tư pháp)
**Verdict:** ✅ Pass

---

## Triệu chứng gốc cần kiểm

"Biểu mẫu **Sửa** thiếu Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm" + yêu cầu "mở ở chế độ chỉnh sửa, **điền sẵn thông tin hiện có**, đúng định dạng, không tràn/đè, đồng nhất tiếng Việt".

## Nhật ký đo

### 13:49 — Mở chế độ Sửa (bản ghi 1): TC-BTP-TW-0001
Danh sách Tổ chức tư vấn → thẻ "Đang hoạt động" → biểu tượng bút chì trên dòng **TC-BTP-TW-0001 "Công ty Luật TNHH Alpha Hà Nội"** → `/chuyen-gia-tvv/to-chuc/beb25e6f-…/chinh-sua`, tiêu đề "Chỉnh sửa Tổ chức tư vấn".

Biểu mẫu Sửa dùng chung bố cục 6 nhóm với Thêm mới, đủ 15 nhãn — trong đó có **"Số quyết định công bố"**, **"Ngày quyết định công bố"** và nhóm **"File đính kèm"** (vùng kéo thả).

### 13:50 — So từng ô với dữ liệu thật của bản ghi
Lấy dữ liệu gốc bằng `GET /api/v1/to-chuc-tu-vans/beb25e6f-…` ngay trong phiên, rồi đọc giá trị từng ô trên biểu mẫu:

| Trường trên biểu mẫu | Giá trị hiển thị | Dữ liệu bản ghi (API) | Khớp |
|---|---|---|:-:|
| Tên tổ chức | Công ty Luật TNHH Alpha Hà Nội | `tenToChuc` như vậy | ✔ |
| Loại hình | Công ty Luật | `loaiHinh = CONG_TY_LUAT` | ✔ |
| Người đại diện | Nguyễn Văn A | như vậy | ✔ |
| Chức vụ người đại diện | Giám đốc | `chucVuDaiDien = Giám đốc` | ✔ |
| Số Giấy ĐKHĐ Sở TP | DKHD-HN-001/2024 | `soGiayDkhd` như vậy | ✔ |
| Ngày cấp Giấy đăng ký hành nghề | 15/03/2024 | `ngayCapDkhd = 2024-03-15` (hiện đúng dạng ngày/tháng/năm) | ✔ |
| Lĩnh vực pháp luật | Lao động · Doanh nghiệp · Thương mại | `linhVucText = Doanh nghiệp, Lao động, Thương mại` | ✔ |
| Số lao động | 25 | `soLaoDong = 25` | ✔ |
| Địa chỉ trụ sở | Số 5 Trần Hưng Đạo, Hoàn Kiếm, Hà Nội | như vậy | ✔ |
| Số điện thoại | 0241000101 | như vậy | ✔ |
| Email | alpha-law@test.htpldn.vn | như vậy | ✔ |
| Website | https://alpha-law.vn | như vậy | ✔ |
| **Số quyết định công bố** | **QD-TW-0001/2026** | `soQdCongBo = QD-TW-0001/2026` | ✔ |
| **Ngày quyết định công bố** | **06/05/2026** | `ngayQdCongBo = 2026-05-06` | ✔ |
| Ghi chú | (trống) | `ghiChu = null` — hồ sơ thật sự chưa có | ✔ |
| **Tệp đính kèm** | danh sách trống, vùng kéo thả sẵn sàng | `fileDinhKem = []` | ✔ |

15/15 ô điền sẵn đúng. Nhãn danh mục hiển thị tiếng Việt (không lộ mã enum), ngày đúng dạng dd/mm/yyyy, bố cục 2–3 cột không tràn/đè.

Ảnh: `image/QLDMTCTV_09-v2-01-sua-TC-BTP-TW-0001-duong-dan-co-ten-to-chuc-va-du-lieu-dien-san.png` và `image/QLDMTCTV_09-v2-02-sua-nhom-lien-he-cong-bo-tep-dinh-kem-du-3-truong.png` (đã mở đọc cả hai).

### 13:52 — Phép thử quyết định: đính kèm tệp rồi lưu
Trên chính bản ghi đang mở (vốn có `fileDinhKem = []`), đính kèm `qd-cong-bo-alpha-reverify-v2.pdf` → danh sách tệp hiện **tên + (237 B) + nút Xem + nút Xóa**.
Bấm **Lưu** (bộ bắt thông báo dùng chung, tự kiểm `soObserverDangSong = 1`):
- **1 request** `PATCH /api/v1/to-chuc-tu-vans/beb25e6f-…` · **1 thông báo** "Cập nhật thành công". Không lặp.
- Sau khi lưu, hệ thống chuyển sang màn Chi tiết; mục "Tệp đính kèm" hiển thị đúng tệp vừa gắn.

⇒ Ba trường ở chế độ Sửa không chỉ hiện mà **ghi xuống thật**.

### 14:00 — Bản ghi thứ 2 để loại trừ "chỉ đúng với 1 hồ sơ": TC-BTP-TW-0003
Mở Sửa **TC-BTP-TW-0003 "Trung tâm TVPL Gamma Đà Nẵng"**. Cũng đủ 6 nhóm + 15 nhãn, và điền sẵn khớp dữ liệu bản ghi:
Loại hình `Trung tâm Tư vấn Pháp luật` · Người đại diện `Lê Văn C` · Chức vụ `Giám đốc TT` · Số Giấy ĐKHĐ `DKHD-DN-003/2024` · Ngày cấp `10/01/2024` · Lĩnh vực `Sở hữu trí tuệ, Đất đai` · Số lao động `15` · Địa chỉ `Số 88 Bạch Đằng, Hải Châu, Đà Nẵng` · Điện thoại `0241000103` · Email `gamma-tvpl@test.htpldn.vn` · Website `https://gamma-tvpl.vn` · **Số QĐ công bố `QD-TW-0003/2026`** · **Ngày QĐ công bố `06/05/2026`**.
Đối chiếu API `GET /api/v1/to-chuc-tu-vans/9bf97472-…`: khớp hoàn toàn. Rời màn bằng nút **Hủy**, không đổi dữ liệu.

Ảnh: `image/QLDMTCTV_OOS_09-v2-01-duong-dan-Chinh-sua-kem-ten-to-chuc-khong-co-cap-Chi-tiet.png` (đã mở đọc — cùng lúc là bằng chứng cho phiếu OOS_09).

### Đối chiếu đặc tả
`srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` dòng 1666 (đường dẫn `/…/:id/chinh-sua`), dòng 1692–1694 (Số QĐ công bố / Ngày QĐ công bố / File đính kèm). Biểu mẫu Sửa dùng chung SCR-IV-NEW-02 với Thêm mới, đúng thiết kế.

### Kết luận
Biểu mẫu Sửa đã có đủ 3 trường, dữ liệu điền sẵn đúng trên cả 2 hồ sơ kiểm, và lưu được ⇒ **Pass**.
