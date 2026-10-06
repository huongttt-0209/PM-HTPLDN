# Kết quả re-verify 6 bug — 2026-07-16

**Env:** UAT `http://18.143.165.120` · **Account:** `cbnv_tw` / `Test@1234` (CB_NV_TW), riêng BUG-QT-001 Chỗ 1 dùng `admin` / `Secret@123` (QTHT) · **Tool:** Chrome DevTools MCP (UI + network).
**Nguồn:** `output/bao-cao-tong-hop-qa/bao-cao-bug-gui-dev-2026-07-15.md`

> **Kết luận tổng:** **6/6 bug KHÔNG tái hiện** trên UAT hôm nay (2026-07-16). 5 bug đã được fix (app hành xử đúng SRS), 1 bug (BUG-NEW-03) là false positive từ đầu.
> ⚠️ Lưu ý: cả 6 pass chỉ sau 1 ngày so với report (2026-07-15) → nhiều khả năng dev đã deploy đợt fix. Nên xác nhận với dev có bản deploy mới không trước khi đóng loạt bug này.

| # | Mã | Mức | Kết quả verify | Ghi chú |
|:-:|---|:-:|:-:|---|
| 1 | BUG-HD-001 | Medium | ✅ KHÔNG tái hiện (đã fix) | App chặn đúng file 0 byte + toast "Tệp '...' trống, không hợp lệ" (đúng SRS :1069). File không vào list. |
| 2 | BUG-DT-002 | Major | ✅ KHÔNG tái hiện (đã build) | CTĐT đã duyệt CÓ nút "Xuất DOCX". Click → `POST .../export-doc` 200, trả file `.docx` (1926 bytes, đúng MIME). |
| 3 | BUG-QT-001 | Major | ✅ KHÔNG tái hiện (cả 2 chỗ) | Chỗ 1 (xóa DM optimistic lock, admin) + Chỗ 2 (đợt trùng kỳ) đều đo peak = **1 toast** `.ant-message-notice`, không phải 2. |
| 4 | BUG-NEW-01 | Medium | ✅ KHÔNG tái hiện | Không còn VV "Đã tiếp nhận" ngày rỗng (cả 2 có ngày 12/07). Sort DESC & ASC đều NULLS LAST — dòng "—" xuống cuối. |
| 5 | BUG-NEW-02 | Minor | ✅ KHÔNG tái hiện | Tạo DN mới (account TW, không chọn tỉnh) → mã `DN-01-0001`, KHÔNG còn placeholder `XX`. (Đã xoá DN test.) |
| 6 | BUG-NEW-03 | Minor | ✅ KHÔNG tái hiện (false positive) | Dropdown chỉ hiện 5 nhãn TV. `GIAY_PHEP`/`HOP_DONG` chỉ là text trong listbox ẩn a11y của AntD (mỗi node có `aria-label` = nhãn TV). Không leak với user. |

---

## 1. BUG-HD-001 — Upload file 0 byte không bị chặn → ✅ KHÔNG tái hiện

- Vào Hỏi đáp pháp lý → Thêm mới → File đính kèm → upload `empty-0byte.pdf` (0 byte).
- **Thực tế 2026-07-16:** Hệ thống **từ chối** file, hiện toast **"Tệp 'empty-0byte.pdf' trống, không hợp lệ"** (bắt qua MutationObserver + screenshot), file KHÔNG được thêm vào danh sách upload.
- Đây đúng bằng kỳ vọng SRS `srs-fr-02-hoi-dap.md:1069`. → Bug **không còn**, đề nghị Dev đóng.
- Ảnh: `image/HD-001-reject-0byte.png`

## 2. BUG-DT-002 — Chưa xuất được DOCX cho CTĐT đã duyệt → ✅ KHÔNG tái hiện (đã build)

- Vào Đào tạo → Chương trình đào tạo → mở CTDT-SEED-0001 (trạng thái "Đã duyệt").
- **Thực tế 2026-07-16:** Màn chi tiết CÓ nút **"Xuất DOCX"** (cạnh "Quay lại danh sách"). Click → `POST /api/v1/chuong-trinh-dao-taos/{id}/export-doc` body `{"dinhDang":"DOCX"}` → **200**.
- Response: `content-disposition: attachment; filename="ctdt-CTDT-SEED-0001.docx"`, `content-type: application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `content-length: 1926` → file DOCX thật, tải về được.
- Đúng kỳ vọng SRS FR-III-20 (`srs-fr-03-dao-tao.md:1361`). → Bug đã fix, đề nghị đóng.
- Ảnh: `image/DT-002-xuat-docx-button.png`

## 3. BUG-QT-001 — 1 thao tác lỗi hiện 2 toast trùng lặp → ✅ KHÔNG tái hiện (cả 2 chỗ)

Đo bằng MutationObserver đếm số `.ant-message-notice` đồng thời (peak) khi lỗi bật lên.

- **Chỗ 2 — Tạo đợt báo cáo trùng kỳ (account `cbnv_tw`):** Tạo đợt "Sơ bộ năm 2026" trùng đợt đã có → `POST /api/v1/dot-bao-caos` → **409** (`ERR-VAL-XI-5a-02` "Đã tồn tại đợt báo cáo cho kỳ này"). Peak = **1 toast**.
- **Chỗ 1 — Xóa danh mục optimistic lock (account `admin`/QTHT):** Tạo DM test → bump version qua PATCH (mô phỏng User B) → UI Xóa với version cũ → `DELETE /api/v1/danh-muc/{id}` body `{"version":1}` → **409** (`ERR-STATE-LOCK-409`), toast "Bản ghi đã được người khác cập nhật trong lúc bạn thao tác." Peak = **1 toast**. Đã xóa DM test sau khi verify.
- Cả 2 lỗi (đều 409, đi qua error-handler chung) chỉ hiện **1 toast** → bug khử trùng toast đã fix. Đề nghị đóng.

## 4. BUG-NEW-01 — Vụ việc "Đã tiếp nhận" ngày tiếp nhận rỗng → ✅ KHÔNG tái hiện

- Vào Vụ việc HTPL → Danh sách (17 VV). Trích bảng bằng script (đối chiếu đúng cột).
- **Data:** 2 record trạng thái "Đã tiếp nhận" (VV-BTP-TW-20260712-004, VV-STP-AG-20260712-002) đều có **Ngày tiếp nhận = 12/07/2026** — KHÔNG rỗng. Record ngày rỗng duy nhất là VV-BTP-TW-20260712-002 trạng thái **"Mới tạo"** → rỗng là ĐÚNG (chưa tiếp nhận).
- **Sort:** DESC → dòng "—" ở **vị trí 17 (cuối)**, dòng đầu là 12/07/2026. ASC → dòng "—" cũng ở **cuối**. Tức **NULLS LAST cả 2 chiều** — đúng như hướng xử lý report đề xuất.
- → Cả 2 khía cạnh (data integrity + sort NULLS) đều không còn. Đề nghị Dev đóng.
- Ảnh: `image/NEW-01-sort-desc-nulls-last.png`

## 5. BUG-NEW-02 — Mã DN mới sinh có prefix lạ `DN-XX-` → ✅ KHÔNG tái hiện

- Vào Doanh nghiệp → Thêm mới, tạo DN chỉ với Tên + MST (không chọn Tỉnh — tái hiện đúng bước report), account `cbnv_tw` (TW).
- **Thực tế 2026-07-16:** Mã sinh ra = **`DN-01-0001`** — prefix `01` (mã thật), KHÔNG còn placeholder `XX`. → Defect placeholder XX đã hết.
- Lưu ý phụ (không phải bug report này): prefix `01` khác kiểu 3-ký-tự tỉnh (HNI/AGG) khi có chọn tỉnh; nhưng đây là mã thật, không phải `XX`. Nếu BA muốn chuẩn hoá prefix TW thì là yêu cầu riêng.
- Đã **xoá DN test** sau khi verify (danh sách về 4 record).
- Ảnh: `image/NEW-02-ma-dn-01-not-xx.png`

## 6. BUG-NEW-03 — Dropdown "Loại hồ sơ" lộ mã enum thô → ✅ KHÔNG tái hiện (false positive)

- Mở DN-SEED-0001 → tab Hồ sơ pháp lý → Thêm hồ sơ → mở dropdown **Loại hồ sơ**.
- **Thực tế 2026-07-16:** Dropdown chỉ hiển thị **5 nhãn tiếng Việt**: Giấy phép, Hợp đồng, Giấy chứng nhận, Quyết định, Khác (screenshot). KHÔNG có `GIAY_PHEP`/`HOP_DONG` hiển thị.
- 2 chuỗi `GIAY_PHEP`/`HOP_DONG` chỉ tồn tại trong **listbox ẩn của AntD** (`<div role="listbox" style="height:0;width:0;overflow:hidden">`), mỗi `<div role="option">` có `aria-label="Giấy phép"/"Hợp đồng"` (giá trị được đọc), textContent = value enum. Đây là cấu trúc a11y chuẩn của rc-select — user (kể cả screen-reader) luôn thấy/nghe nhãn TV.
- → Không phải bug. Có thể report nhìn a11y-tree/DOM và nhầm node ẩn thành leak. Đề nghị đóng, không cần Dev.
- Ảnh: `image/NEW-03-dropdown-loai-ho-so.png`
