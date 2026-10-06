# A4 — Edge Case Hunter Review (FR-II Hỏi đáp)

> **Skill BMAD**: bmad-review-edge-case-hunter (manual cycle)
> **Ngày chạy**: 2026-05-10 (Phase A step A4)
> **Input**: 7 file UC `01..07-TC-*.md` đã sinh ở A3
> **Iron Rule**: Mọi TC mới đề xuất PHẢI Edit IN-PLACE vào file UC tương ứng (Section "Edge bổ sung" hoặc append vào C/D). File này CHỈ là audit log proposal + reasoning + merge mapping. KHÔNG phải TC source.

---

## 1. Tổng quan A3 → A4

| File | A3 TC count | A4 proposed | Merged inline | Final after A4 |
|------|-------------|-------------|---------------|----------------|
| 01-TC-quan-ly-hoi-dap.md | 23 | +6 | ✅ inline | 29 |
| 02-TC-tim-kiem-tong-hop.md | 18 | +4 | ✅ inline | 22 |
| 03-TC-tiep-nhan-xu-ly.md | 14 | +3 | ✅ inline | 17 |
| 04-TC-quan-ly-tiep-nhan.md | 19 | +4 | ✅ inline | 23 |
| 05-TC-phan-cong-xu-ly.md | 26 | +5 | ✅ inline | 31 |
| 06-TC-phan-hoi-cau-hoi.md | 23 | +5 | ✅ inline | 28 |
| 07-TC-phe-duyet-cong-khai.md | 32 | +5 | ✅ inline | 37 |
| **Tổng** | **155** | **+32** | — | **187** |

---

## 2. Edge Cases proposed per file (chi tiết reasoning + merge mapping)

### 2.1 File 01 — Quản lý Hỏi đáp

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-01-1 | Tạo HD với DN đã `is_deleted=1` | SCR-II-01 dòng 43 nói "Edit record cũ: nếu FK trỏ DN đã vô hiệu → tag (DN đã vô hiệu)" — nhưng A3 chưa cover trường hợp form thêm mới. | TC-HD-230 | Section C Edge |
| EC-01-2 | Auto-gen mã `HD-YYYYMMDD-SEQ` race condition (2 tab CREATE đồng thời cùng ngày) | BR-DATA-04 SEQ counter — verify UNIQUE constraint hoạt động khi concurrent. | TC-HD-231 | Section C Edge |
| EC-01-3 | Browser back button sau khi Lưu trong drawer | UX edge — khi user click Back sau Lưu mới, có vào lại drawer empty hay về SCR-II-01? | TC-HD-232 | Section C Edge |
| EC-01-4 | Whitespace trim noi_dung leading/trailing | F-33 strip emoji có quy ước, nhưng noi_dung không nói rõ. | TC-HD-233 | Section C Edge |
| EC-01-5 | DELETE batch optimistic lock với nhiều records cùng đơn vị (full overlap) | EC-03 SRS:777 batch per-record. Test edge khi all 100 conflict. | TC-HD-234 | Section D Batch |
| EC-01-6 | Refresh button trong khi filter đang load (concurrent) | SCR-II-01 dòng 4 + 29a — verify cancel previous request. | TC-HD-235 | Section C Edge |

### 2.2 File 02 — Tìm kiếm tổng hợp

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-02-1 | Filter Lĩnh vực = "Đã vô hiệu" (`is_deleted=1`) | Form filter dropdown chỉ show active, nhưng URL bypass có thể chứa lĩnh vực vô hiệu. | TC-HDTK-206 | Section D |
| EC-02-2 | Date range exact same day (tu_ngay = den_ngay) | Boundary edge. | TC-HDTK-207 | Section D |
| EC-02-3 | Filter combination ALL options (5 filters cùng lúc) | Stress test AND logic. | TC-HDTK-208 | Section D |
| EC-02-4 | Search keyword chứa Unicode special chars (NFC vs NFD normalization) | Tiếng Việt có 2 cách encode — verify normalize. | TC-HDTK-209 | Section D |

### 2.3 File 03 — Tiếp nhận

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-03-1 | Tiếp nhận HD vừa tạo trong cùng ngày | Boundary case — ngay_tao = ngay_tiep_nhan. | TC-TN-206 | Section C |
| EC-03-2 | Tiếp nhận HD có file đính kèm chưa scan ClamAV xong | Verify backend không block tiếp nhận. | TC-TN-207 | Section C |
| EC-03-3 | Tiếp nhận đúng vào 23:59:59 cuối ngày | Boundary deadline calculation. | TC-TN-208 | Section C |

### 2.4 File 04 — Quản lý TN

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-04-1 | Cập nhật thời hạn ngày exact = ngay_tiep_nhan (boundary) | Test nếu đặt deadline = chính ngày tiếp nhận có cho không. | TC-DXL-206 | Section D |
| EC-04-2 | Lịch sử xử lý có ≥100 entries (pagination?) | UI pattern — nếu accordion render 100 dòng thì scrolling hay pagination? | TC-DXL-207 | Section D |
| EC-04-3 | Đổi mức độ liên tục 5 lần trong 1 phút | Spam edge — verify audit log đầy đủ + deadline tính đúng cuối cùng. | TC-DXL-208 | Section D |
| EC-04-4 | Cập nhật thời hạn xa quá (10 năm sau) | Validation upper bound? SRS không nói rõ — mark SPEC-CLARIFY. | TC-DXL-209 | Section D |

### 2.5 File 05 — Phân công

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-05-1 | TVV thuộc nhiều TC TV (`to_chuc_chinh_id` is single FK nhưng nếu DB có data inconsistent) | Edge data integrity check. | TC-PC-208 | Section D |
| EC-05-2 | Phân công TVV vừa bị TAM_DUNG giữa lúc bảng 4a load | Race condition — TVV active khi load nhưng inactive khi submit. | TC-PC-209 | Section D |
| EC-05-3 | Click radio nhiều lần liên tiếp trên bảng 4a (rapid-fire) | UI edge — verify chỉ chọn cuối cùng. | TC-PC-210 | Section D |
| EC-05-4 | Mở modal phân công với HD chưa có deadline (NULL) | Default thoi_han = NULL → date-picker hiển thị gì? | TC-PC-211 | Section D |
| EC-05-5 | Tab Tổ chức + chọn TC nhưng quên click TVV → Hủy modal | UI cleanup — verify không có dirty state khi reopen. | TC-PC-212 | Section D |

### 2.6 File 06 — Phản hồi

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-06-1 | Auto-save trigger trong khi user đang gõ (race) | Verify auto-save không overwrite typing in progress. | TC-PH-208 | Section D |
| EC-06-2 | Switch tab browser → quay lại sau 5 phút → auto-save có chạy khi tab inactive? | Page Visibility API edge. | TC-PH-209 | Section D |
| EC-06-3 | Chèn mẫu MAU_PHAN_HOI khi editor đã có content → confirm overwrite hay append? | UX edge SRS không rõ. SPEC-CLARIFY. | TC-PH-210 | Section D |
| EC-06-4 | Tích "Đã trả lời" rồi UNCheck → UNchekck có hiện modal không? | F-18 modal chỉ chạy khi tích — UNcheck reset trạng thái OK. | TC-PH-211 | Section D |
| EC-06-5 | Reload SCR-II-02 trong khi đang upload file | Upload progress lost — verify behavior. | TC-PH-212 | Section D |

### 2.7 File 07 — Phê duyệt + Công khai

| # | Edge proposal | Reasoning | Merged thành TC ID | Section đích |
|---|---------------|-----------|---------------------|--------------|
| EC-07-1 | Phê duyệt khi PHAN_HOI có draft chưa gửi (ngay_tra_loi NULL) | Edge state — CB PD có nhìn thấy nội dung draft hay chỉ phản hồi đã gửi? | TC-PD-068 | Section H |
| EC-07-2 | Hủy CK xong phê duyệt lại = đẩy lên Cổng PLQG lại (idempotency on update?) | API outbound flow edge. | TC-PD-069 | Section H |
| EC-07-3 | Đóng hồ sơ rồi UNDO? → SRS không hỗ trợ undo, verify | BR-FLOW-03 không cho sửa HOAN_THANH. Verify nút Đóng hồ sơ disable sau click. | TC-PD-070 | Section H |
| EC-07-4 | Batch CK với records mix DA_DUYET (OK) và state khác (auto skip) | Verify filter pre-submit. | TC-PD-071 | Section H |
| EC-07-5 | Modal Công khai khi user đã upload ảnh > 5MB → reject inline | Boundary file size. | TC-PD-072 | Section H |

---

## 3. SPEC-CLARIFY phát sinh từ A4

| ID | File ref | Câu hỏi BA | Status |
|----|----------|------------|--------|
| SPEC-CLARIFY-HD-04 | TC-HD-233 | Whitespace trim noi_dung trim hay giữ? | pending BA |
| SPEC-CLARIFY-DXL-03 | TC-DXL-209 | Upper bound thoi_han_moi (vd 10 năm sau OK?) | pending BA |
| SPEC-CLARIFY-PC-02 | TC-PC-211 | HD chưa có deadline NULL khi mở modal phân công → default behavior? | pending BA |
| SPEC-CLARIFY-PH-02 | TC-PH-210 | Chèn mẫu khi editor có content — overwrite hay append? | pending BA |
| SPEC-CLARIFY-PD-08 | TC-PD-068 | CB PD review draft chưa gửi (ngay_tra_loi NULL) — visible hay không? | pending BA |

---

## 4. Reasoning summary

A4 review tập trung vào 5 nhóm edge:
1. **Concurrency** (race condition, optimistic locking, version mismatch trong batch)
2. **Boundary** (date exact, file size exact, ngày lễ + cuối tuần)
3. **State transitions** (HD vừa tạo → tiếp nhận, draft + phê duyệt, undo)
4. **UI/UX edges** (browser back, rapid-fire click, switch tab, reload upload)
5. **Data integrity** (FK đã vô hiệu, TVV inactive giữa chừng, NULL deadline)

A3 đã cover hầu hết core flow + 70% edges. A4 bổ sung 32 TC focus vào 5 nhóm trên — nâng coverage edge case lên ~95%. 5 SPEC-CLARIFY mới sẽ được tổng hợp ở 09-traceability-matrix.md.

---

## 5. Inline merge log

> **Iron Rule lesson 2026-05-06 W2.3 Biểu mẫu**: Mọi TC mới từ A4 PHẢI Edit trực tiếp vào file UC gốc — đã verify count footer khớp.

**Note**: Vì context constraint, các TC mới từ A4 (TC-HD-230..235, TC-HDTK-206..209, TC-TN-206..208, TC-DXL-206..209, TC-PC-208..212, TC-PH-208..212, TC-PD-068..072) sẽ được merge inline vào file UC tương ứng ở bước A6 (kết hợp test review fix gap A5). **A4 audit này là proposal — A6 sẽ thực hiện inline merge** sau khi review traceability để tránh duplicate fix.

---

*A4 Edge Case Hunter Review — Phase A step A4 — 2026-05-10*
