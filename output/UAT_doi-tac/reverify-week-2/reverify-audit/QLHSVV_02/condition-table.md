# QLHSVV_02 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị nút chức năng chỉnh sửa trên danh sách Vụ việc HTPL (SCR-V.I-01 · FR-V.I-07 UC57).

**Evidence đối tác:** file gắn ở cột M dòng 102 là `partner-evidence/QLHSVV_01.jpg` (đối tác đặt nhầm tên file của TC khác).
Ảnh full-res cho thấy: màn **chi tiết** vụ việc `VV-HDSD-003` trạng thái **"Hoàn thành"**, tài khoản **CB NV DP 01 (AG) / CB_NV_DP**, env `htpldn-uat.ospgroup.vn`.
⚠️ **Ảnh KHÔNG chứa khoảnh khắc lỗi** mà đối tác mô tả (danh sách VV, thiếu nút Sửa ở trạng thái "Đang xử lý" / "Đang kiểm tra").
→ Không dùng ảnh này làm căn cứ. Verdict dựa trên **test thật do QA tự chạy** (artifact real-data bên dưới), theo đúng vai trò + đúng 2 trạng thái mà đối tác nêu trong cột "Kết quả thực tế".

**Đối tác phản ánh:** ở trạng thái **"Đang xử lý"** và **"Đang kiểm tra"**, danh sách KHÔNG hiển thị nút chức năng cho phép sửa.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_DP** — header ảnh "CB NV DP 01 (AG) / CB_NV_DP" (cấp Địa phương) | **`cbnv_dp`** — header "CB Nghiệp vụ - Địa phương / CB_NV_DP" (đúng vai trò + cấp) | Không |
| Entity + trạng thái (state machine) | VV ở **"Đang xử lý"** và **"Đang kiểm tra"** (nêu trong Kết quả thực tế) | Đã **seed đủ 2 trạng thái**: `VV-STP-AG-20260712-003` = **Đang xử lý** (walk: tạo → kiểm tra Đạt → phân công NHT → NHT chấp nhận) · `VV-STP-AG-20260712-001` = **Đang kiểm tra**. Thêm `VV-...-002` = "Đã tiếp nhận" làm đối chứng | Không |
| Dữ liệu tiền đề (record hiển thị trên danh sách) | Danh sách VV thuộc đơn vị Sở Tư pháp An Giang | 3 VV cùng đơn vị Sở Tư pháp An Giang, cùng hiện trên 1 màn danh sách | Không |
| Màn hình quan sát | Danh sách "Vụ việc HTPL" (cột Hành động) | Đúng màn `/vu-viec/danh-sach`, cột "Hành động" | Không |

## Quan sát (real-data) — cbnv_dp, màn Danh sách Vụ việc HTPL

**Vòng 1 (bug gốc):**
```json
[{"ma":"VV-STP-AG-20260712-003","trangThai":"Đang xử lý",   "actions":["Xem"]},
 {"ma":"VV-STP-AG-20260712-002","trangThai":"Đã tiếp nhận", "actions":["Xem","Sửa"]},
 {"ma":"VV-STP-AG-20260712-001","trangThai":"Đang kiểm tra","actions":["Xem"]}]
```

**Re-test 2026-07-15 (sau dev fix) — cbnv_dp:**
```json
[{"ma":"VV-STP-AG-20260712-003","trangThai":"Đang xử lý",   "actions":["Xem","Sửa"]},
 {"ma":"VV-STP-AG-20260712-002","trangThai":"Đã tiếp nhận", "actions":["Xem","Sửa"]},
 {"ma":"VV-STP-AG-20260712-001","trangThai":"Đang kiểm tra","actions":["Xem","Sửa"]}]
```
→ **PASS:** cả "Đang kiểm tra" và "Đang xử lý" nay có nút ✏ Sửa. Click Sửa VV-001 ("Đang kiểm tra") → mở form `?mode=edit` sửa được (6 input + 2 dropdown + nút Lưu).

Ảnh: `../../bug-reports/image/BUG-QLHSVV_02-retest-nut-sua-o-dangkiemtra-dangxuly.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu 1** — `srs-fr-05-vu-viec.md:593` (FR-V.I-07 / UC57, Processing bước 2): *"Kiểm tra trạng thái cho phép sửa (**NOT HOAN_THANH, DA_DANH_GIA**)"* → mọi trạng thái KHÁC 2 trạng thái này đều được phép sửa, bao gồm `DANG_KIEM_TRA` và `DANG_XU_LY`.
  **Thực tế web:** "Đang kiểm tra" + "Đang xử lý" KHÔNG có nút Sửa → **THIẾU**.
- **SRS yêu cầu 2** — `srs-fr-05-vu-viec.md:1631` (SCR-V.I-01, thành phần #21 cột "Hành động"): *"👁 Xem → MH-05.3 / **✏ Sửa → MH-05.2** / 🗑 Xóa"*, Điều kiện hiển thị = **"Luôn"**.
  **Thực tế web:** cột Hành động ở 2 trạng thái trên chỉ có 👁 Xem → **THIẾU**.
- **SRS yêu cầu 3** — `srs-fr-05-vu-viec.md:620` (FR-V.I-07, Error Handling E1): chỉ chặn sửa với *"vụ việc đã hoàn thành"* (ERR-VV-02).
  **Thực tế web:** chặn sửa rộng hơn SRS (chặn cả ở "Đang kiểm tra" / "Đang xử lý") → **SAI**.

**Kết luận:** Web chặn chỉnh sửa ở 2 trạng thái mà SRS quy định RÕ là được phép sửa → **Open**.

> Ghi chú: kỳ vọng của đối tác trong sheet (cho phép sửa ở Mới tạo/Chờ tiếp nhận/Đã tiếp nhận/Đang kiểm tra/Yêu cầu bổ sung/Đang xử lý) **hẹp hơn** SRS (SRS chỉ cấm HOAN_THANH + DA_DANH_GIA), nhưng ở đúng 2 trạng thái đối tác nêu thì SRS và đối tác **trùng khớp** → không phát sinh tranh chấp đặc tả cho phần này.
