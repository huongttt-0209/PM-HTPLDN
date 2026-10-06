# Bảng đối chiếu điều kiện — NHSYC_01 (row 127, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Nhập hồ sơ yêu cầu HTPL thủ công — FR-V.I-04 (UC54), màn SCR-V.I-02
**Loại bug:** phụ thuộc input/validation + dữ liệu tiền đề → BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG)
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_03` (CB_NV_TW, đơn vị BTP · TW)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res `partner-evidence/NHSYC_01.jpg`) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — nhãn góc phải ảnh ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" | `cbnv_tw_03` — nhãn góc phải "CB Nghiệp vụ - Trung ương #03 · CB_NV_TW", đơn vị "BTP · TW" (ảnh `image/NHSYC_01-01-form-mac-dinh.png`) | Không |
| Entity + **trạng thái** (state machine) | VU_VIEC **chưa tồn tại** — đang ở màn tạo mới `/vu-viec/tao-moi`, chưa sinh mã, chưa có trạng thái | VU_VIEC chưa tồn tại — màn `/vu-viec/tao-moi`, bấm [Lưu & Tiếp nhận] để chuyển sang DA_TIEP_NHAN | Không |
| Dữ liệu tiền đề (doanh nghiệp + tệp đính kèm) | Có **tệp PDF đính kèm**: `2K15 T5 (23.7) & T7 (25.7).pdf` (256.4 KB), đã upload xong (hiện dòng file + nút Xem/Xóa) | Có **tệp PDF đính kèm**: `NHSYC_01-tep-kiem-thu.pdf` / `NHSYC_01-tep-kiem-thu-R2.pdf` (614 B), upload xong `POST /vu-viecs/upload` → 201, hiện dòng file + nút Xem/Xóa. DN chọn qua hộp thoại Tìm DN: `Cong ty TNHH QA UAT Kiem Thu` (DN-HNI-0001) | Không |
| Input / filter / giá trị nhập | Kênh tiếp nhận = **Trực tiếp** · Ngày tiếp nhận = **27/07/2026** (= ngày hiện tại của máy đối tác, đồng hồ trong ảnh 27/07/2026 01:59 PM, tức để nguyên giá trị mặc định) · Người tiếp nhận auto-fill | Kênh tiếp nhận = **Trực tiếp** · Ngày tiếp nhận = **03/08/2026** (= ngày hiện tại, giá trị mặc định form, không sửa tay — cùng bản chất "ngày hiện tại" như đối tác) · Người tiếp nhận auto-fill "CB Nghiệp vụ - Trung ương #03" | Không |
| Nút hành động bấm | **[Lưu & Tiếp nhận]** (nhãn thật trong ảnh; phiếu cột J ghi "Lưu&Gửi duyệt" nhưng nút trên màn nhập thủ công tên là "Lưu & Tiếp nhận") | **[Lưu & Tiếp nhận]** — cùng nút | Không |

## Ghi chú đóng GAP

- **Ngày tiếp nhận lệch giá trị tuyệt đối (27/07 vs 03/08) nhưng KHÔNG phải GAP:** cả hai đều là **giá trị mặc định = ngày hiện tại** do form tự điền (SRS `srs-fr-05-vu-viec.md:1698` — "ngay_tiep_nhan | C11 DatePicker | Bắt buộc. Mặc định: ngày hiện tại"). Không bên nào sửa tay. Đã kiểm thêm: payload FE gửi `"ngayTiepNhan":"2026-08-03"` — đúng dạng ISO, tức nhánh serialize ngày chạy y như nhau với mọi ngày hiện tại.
- **Tệp đính kèm là điều kiện quyết định** (phát hiện khi cô lập biến): giữ đúng điều kiện đối tác (**có** tệp) thì hệ thống trả lỗi và không tạo được hồ sơ; bỏ tệp đi thì tạo được. Đã test cả hai nhánh nên không còn ô nào chưa thử.
- Đã chạy trên **bản đã tải lại trang** (`navigate_page reload ignoreCache`) để loại trừ mã cũ còn trong tab.

**Kết luận: 0 GAP** — mọi điều kiện của đối tác đã được tái lập bằng test thật.
