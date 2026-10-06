# Bảng đối chiếu điều kiện — QLTLPLCVV_08 (row 297) — Bấm "Sửa" tư liệu không hiển thị tệp đính kèm dù có file

**Kết luận:** Open — Tái hiện đúng: tư liệu có **2 file** (cột "File" = 2 ở bảng danh sách, `soFile=2`) nhưng khi bấm **[Sửa]** vùng "File đính kèm" trong modal **trống** (không liệt kê file nào). Nguyên nhân gốc là BE: `GET /api/v1/tu-lieu-phap-ly-vvs/{id}` (detail) trả `files: []` dù danh sách báo 2 file → FE không có data để render. Vi phạm AC dòng 962 ("chọn tư liệu → hiển thị thông tin + **danh sách file**") và Output `so_file` dòng 936.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test (cbnv_tw_05 / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB NV | cbnv_tw_05 (CB_NV_TW — CRUD đầy đủ, SRS dòng 806) | Không |
| Tư liệu có ≥1 file đính kèm | Có file | Tư liệu `90268a74` "TL-BE-0721 Tu lieu 2 file - case 08", cột File = **2**, `soFile=2` | Không |
| Trạng thái tư liệu | — | Kiểm khi CONG_KHAI (cùng record case 07). Bug độc lập trạng thái: detail luôn trả `files:[]` | Không |
| Thao tác | Bấm Sửa → xem vùng file | Bấm Sửa → modal "Sửa tư liệu pháp luật", vùng "File đính kèm" **trống** (`ant-upload-list` rỗng) | Không |
| API có data không (FE vs BE) | — | `GET /tu-lieu-phap-ly-vvs/{id}` trả `files:[]` (BE thiếu data, không phải FE ẩn) | Không |

**Artifact real-data (2 method — UI + API):**
- Method 1 (UI): modal Sửa → `fileListInModal = []` (không hiển thị file dù danh sách báo 2).
- Method 2 (API detail): `GET /api/v1/tu-lieu-phap-ly-vvs/90268a74-9213-43bb-947f-d6ea6c0b0b9f` → `{"trangThai":"CONG_KHAI","files":[]}` (mảng file RỖNG). Trong khi danh sách `GET /tu-lieu-phap-ly-vvs?...` cùng record trả `soFile=2`.
- Đối chứng lúc tạo: POST create gửi `fileDinhKemIds:[<id1>,<id2>]` (2 file upload trước đó đều 201, `trangThaiQuet:SACH`) → 2 file có thật, chỉ endpoint detail không join/trả.
- Ảnh: `bug-reports/tvcs/image/bug-qltlplcvv_08-sua-khong-hien-file.png`.

**SRS:**
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:962` — AC: "Given CB NV xem chi tiết When chọn tư liệu Then hiển thị thông tin + **danh sách file**".
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:936` — Output #7 `so_file | number | luôn` (danh sách đếm đúng 2, chứng tỏ file tồn tại).
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:890` — Processing Chỉnh sửa step 5 (cập nhật fields) — không sửa/quản lý được file khi modal không hiển thị file hiện có.

→ File tồn tại (danh sách đếm 2, tạo bằng 2 fileDinhKemIds hợp lệ) nhưng detail API trả rỗng → modal Sửa không render file. BE bug (endpoint detail thiếu join files). Owner: Dev BE.
