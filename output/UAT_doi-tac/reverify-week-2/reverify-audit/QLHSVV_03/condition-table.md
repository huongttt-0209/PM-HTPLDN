# QLHSVV_03 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra form chỉnh sửa vụ việc — Nhóm 2 "Nội dung yêu cầu" (SCR-V.I-01 #21 → MH-05.2 · FR-V.I-07 UC57).

**Evidence đối tác:** `partner-evidence/QLHSVV_03.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res cho thấy: URL `htpldn-uat.ospgroup.vn/vu-viec/d72ca300-...?mode=edit`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**, vụ việc "TKM nhập thủ công" (Lĩnh vực Thuế, Loại hình Đại diện ngoài tố tụng).
Nhóm 2 ở chế độ sửa: chỉ có 3 ô nhập — **Tiêu đề**, **Nội dung yêu cầu**, **Vướng mắc** (+ nút [Lưu] [Hủy]).
**Lĩnh vực / Loại hình** in ra dạng chữ tĩnh (không phải dropdown); **Ghi chú KHÔNG xuất hiện** trong biểu mẫu.

**Đối tác phản ánh:** hệ thống không cho phép chỉnh sửa **Lĩnh vực**, **Loại hình** và **Ghi chú**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Entity + trạng thái (state machine) | VV "TKM nhập thủ công" — đang mở được `?mode=edit` ⇒ ở trạng thái cho phép sửa (nhập thủ công → "Đã tiếp nhận") | `VV-BTP-TW-20260712-005` (cf90a65c) — trạng thái **"Đã tiếp nhận"** (khớp state bug gốc; VV-006 gốc nay đã sang "Yêu cầu bổ sung") | Không |
| Dữ liệu tiền đề (VV đã có Lĩnh vực + Loại hình) | VV có sẵn Lĩnh vực "Thuế" + Loại hình "Đại diện ngoài tố tụng" | VV có sẵn Lĩnh vực **"Thương mại"** + Loại hình **"Tư vấn pháp luật"** (giá trị hiện tại có dữ liệu, đủ điều kiện để form render dropdown nếu có) | Không |
| Màn hình / chế độ quan sát | Màn Chi tiết VV ở chế độ sửa (`?mode=edit`), Nhóm 2 "Nội dung Yêu cầu" | Đúng màn `/vu-viec/{id}?mode=edit`, Nhóm 2 "Nội dung Yêu cầu" | Không |

## Quan sát (real-data)

**Vòng 1 (bug gốc) — cbnv_tw, `?mode=edit`:**
```json
{"labels_co_o_nhap": ["Tiêu đề", "Nội dung yêu cầu", "Vướng mắc"],
 "linh_vuc":   "Thương mại — in chữ tĩnh, KHÔNG có dropdown",
 "loai_hinh":  "Tư vấn pháp luật — in chữ tĩnh, KHÔNG có dropdown",
 "ghi_chu":    "KHÔNG tồn tại trong biểu mẫu (hasGhiChu=false)"}
```

**Re-test 2026-07-15 (sau dev fix) — cbnv_tw, VV-BTP-TW-20260712-005 `?mode=edit`:**
```json
{"linh_vuc":  "combobox/dropdown (mở ra 13 option: Thuế/Lao động/Đất đai/Dân sự/Thương mại/Hình sự/...) — CHỌN được",
 "loai_hinh": "combobox/dropdown, giá trị 'Tư vấn pháp luật' — CHỌN được",
 "ghi_chu":   "textbox multiline có counter '0/2000' — nhập được",
 "full_flow": "Nhập Ghi chú 'QA reverify 2026-07-15...' → bấm Lưu → toast 'Cập nhật vụ việc thành công' → reload ?mode=edit → Ghi chú GIỮ nguyên giá trị (BE persist OK)"}
```
→ **PASS:** cả 3 trường (Lĩnh vực, Loại hình, Ghi chú) nay có mặt + sửa được + lưu persist qua BE.

Ảnh: `../../bug-reports/image/BUG-QLHSVV_03-retest-form-sua-co-linhvuc-loaihinh-ghichu.png`

## Đối chiếu SRS (Cổng 3)

- **Ý A — Ghi chú không sửa được → Open (rõ ràng).**
  `srs-fr-05-vu-viec.md:586` — FR-V.I-07 (UC57) §Inputs, dòng 4: trường **`ghi_chu`** (text long, bắt buộc = N) là **input hợp lệ của chức năng chỉnh sửa vụ việc**.
  **Thực tế web:** biểu mẫu sửa KHÔNG có trường Ghi chú → **THIẾU** (vi phạm trực tiếp Inputs của UC57).

- **Ý B — Lĩnh vực + Loại hình không sửa được → Open (theo SRS màn hình).**
  `srs-fr-05-vu-viec.md:1631` — SCR-V.I-01 §Thành phần #21: nút **"✏ Sửa → MH-05.2"** ⇒ thao tác Sửa phải mở **MH-05.2 = SCR-V.I-02**.
  `srs-fr-05-vu-viec.md:1673-1676` — SCR-V.I-02 §Thành phần #21/#22/#24: `linh_vuc_id` (C10 Dropdown, **Bắt buộc**), `loai_hinh_ht_id` (C10 Dropdown, **Bắt buộc**), `ghi_chu` (C09 Textarea) đều là **trường nhập của biểu mẫu**.
  **Thực tế web:** thao tác Sửa KHÔNG mở MH-05.2 mà bật chế độ sửa inline ngay trên màn Chi tiết, chỉ cho sửa 3/6 trường của Nhóm 2; Lĩnh vực + Loại hình bị khóa cứng thành chữ tĩnh → **THIẾU**.

**Kết luận:** cả 3 trường đối tác nêu (Lĩnh vực, Loại hình, Ghi chú) đều là trường được phép nhập theo SRS nhưng web không cho sửa → **Open**.

> Lưu ý gửi BA (đã ghi `ba-confirmation-needed-week-2.md`): FR-V.I-07 §Inputs (dòng 583-586) chỉ liệt kê `noi_dung_yeu_cau` + `file_bo_sung` + `ghi_chu`, KHÔNG liệt kê `linh_vuc_id` / `loai_hinh_ht_id`; trong khi SCR-V.I-01 #21 lại map Sửa → MH-05.2 (nơi 2 trường này là trường nhập bắt buộc). Hai chỗ này chưa thống nhất về phạm vi trường được sửa — dev nên fix theo màn MH-05.2 và BA chốt lại danh sách trường.
