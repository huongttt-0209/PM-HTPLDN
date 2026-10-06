# Test Cases — UC26/UC27: Quản lý kho bài giảng & Tìm kiếm bài giảng (FR-III-07 / FR-III-08)

> **SRS Ref:** FR-III-07 (UC26 — quote `srs-fr-03-dao-tao.md` dòng 556-628), FR-III-08 (UC27 — dòng 630-682), SCR-III-03 (dòng 1166-1170), Entity `BAI_GIANG` (`02-thu-tu-module.md` dòng 602 — quan hệ 1-N trực tiếp với KHOA_HOC qua `bai_giang.khoa_hoc_id`)
> **Phase:** A (BMAD A1-A7) — Phase A re-run 2026-05-09
> **Phạm vi:** SCR-III-03 (sub-menu 2). 4 loại tài liệu: SLIDE (PPTX), PDF, VIDEO (YouTube), TAI_LIEU_KHAC. Switch công khai per record.
> **Cross-module:** `linh_vuc_ids` ← FR-10 DM "Lĩnh vực PL"; `khoa_hoc_id` ← KHOA_HOC nội bộ FR-03.

---

## A. UI FIELD VERIFICATION (BẮT BUỘC chạy trước functional)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-UI-01 | FR-III-07 / SCR-III-03 / UI | Verify SCR-III-03 layout: list + preview panel + filter loại + switch công khai | CB_NV_TW (cb_nv_tw_01) đã đăng nhập. Seed ≥6 BAI_GIANG cover 4 loại (SLIDE/PDF/VIDEO/TAI_LIEU_KHAC) + 2 cong_khai=true, 4 cong_khai=false. | URL: `/dao-tao/bai-giang` (sub-menu 2 SCR-III-03) | 1. Đăng nhập CB_NV_TW. 2. Vào menu "Đào tạo, Tập huấn > Kho bài giảng". 3. Verify từng row vs SRS dòng 1168 + Outputs dòng 596-606. | **LAYOUT**: Breadcrumb "Trang chủ > Đào tạo > Kho bài giảng" + toolbar [+ Thêm bài giảng] [Tìm kiếm]. **FILTER-BAR**: Từ khóa (search), Loại tài liệu dropdown (4 giá trị: SLIDE/PDF/VIDEO/TAI_LIEU_KHAC), Khóa học (dropdown FK KHOA_HOC), Lĩnh vực PL (multi-select), Công khai (toggle/dropdown), Từ ngày/Đến ngày tạo. **SPLIT-PANEL**: Trái — danh sách bài giảng (Mã, Tên, Loại badge màu, Khóa học, Dung lượng, Công khai switch, Ngày tạo, Hành động). Phải — preview panel (PPTX render / PDF embed / YouTube iframe / placeholder TAI_LIEU_KHAC). **SWITCH cong_khai**: per row toggle on/off (per SRS dòng 561 "Switch công khai lên chuyên trang"). **PAGINATION** default 20/page (BR-DATA-07). **NEGATIVE — Phần tử KHÔNG có**: KHÔNG batch action (chưa thấy spec). | Happy 🔴 |
| TC-BG-UI-02 | FR-III-07 / SCR-III-03 / UI | Verify form Thêm/Sửa bài giảng với 4 loại tài liệu — file/url field conditional | CB_NV_TW đã đăng nhập. | — | 1. Click [+ Thêm bài giảng]. 2. Lần lượt chọn loại = SLIDE/PDF/VIDEO/TAI_LIEU_KHAC. 3. Quan sát field hiển thị conditional. | **LAYOUT**: Drawer/Modal form. Common fields: Tên bài giảng *, Mô tả *, Loại * (radio/select), Khóa học (dropdown FK), Lĩnh vực PL (multi-select), Thứ tự (number ≥1), Công khai (toggle, default off per SRS dòng 582), Ảnh đại diện (single image). **CONDITIONAL** (per SRS Inputs dòng 573-582): Loại=SLIDE → field "File PPTX *" (accept `.pptx` ≤20MB) + ẩn url_youtube. Loại=PDF → field "File PDF *" (accept `.pdf` ≤20MB) + ẩn url_youtube. Loại=VIDEO → field "URL YouTube *" + ẩn file. Loại=TAI_LIEU_KHAC → cả 2 optional. Action-bar [Hủy] [Đồng ý]/[Lưu]. **NEGATIVE — Phần tử KHÔNG có**: KHÔNG có lựa chọn loại nào ngoài 4 enum trên. | Happy 🔴 |

---

## B. READ / LIST / SEARCH (FR-III-08 — UC27)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-001 | FR-III-08 / BR-DATA-07 | Xem danh sách bài giảng — phân trang default 20/page | CB_NV_TW đăng nhập. Seed ≥25 BAI_GIANG. | — | 1. Vào SCR-III-03. 2. Quan sát pagination + count. 3. Click trang 2. | **STATE**: `GET /api/v1/bai-giang?page=1&size=20` → 20 record. Page 2 → 5 record. **UI**: Trang 1 hiển thị 20 dòng + tổng count. Trang 2 hiển thị 5 dòng. **PERSIST**: Reload trang 2 → vẫn ở trang 2 (URL state). | Happy |
| TC-BG-002 | FR-III-08 / SCR-III-03 | Filter loại tài liệu = VIDEO | CB_NV_TW đăng nhập. Seed 3 SLIDE + 2 PDF + 2 VIDEO + 1 TAI_LIEU_KHAC. | filter loai_tai_lieu=VIDEO | 1. SCR-III-03. 2. Filter dropdown Loại = VIDEO. 3. Click [Tìm kiếm]. | **STATE**: `GET /api/v1/bai-giang?loai_tai_lieu=VIDEO`. **UI**: Hiển thị đúng 2 record VIDEO. Loại badge "VIDEO" (màu phân biệt). KHÔNG hiển thị SLIDE/PDF/TAI_LIEU_KHAC. **PERSIST**: Reload giữ filter. | Happy |
| TC-BG-003 | FR-III-08 / SCR-III-03 | Filter Công khai = true | CB_NV_TW đăng nhập. Seed 4 cong_khai=true + 6 cong_khai=false. | filter cong_khai=true | 1. SCR-III-03. 2. Filter Công khai = "Đã công khai". 3. Tìm kiếm. | **STATE**: `GET /api/v1/bai-giang?cong_khai=true`. **UI**: Đúng 4 record. Switch hiển thị on (xanh). **PERSIST**: Reload giữ filter. | Happy |
| TC-BG-004 | FR-III-08 | Search by tu_khoa kết hợp filter Loại (AND) | CB_NV_TW đăng nhập. Seed: PDF "Luật DN 2020", VIDEO "Luật DN 2020", PDF "Hợp đồng". | tu_khoa="Luật DN", loai=PDF | 1. Nhập tu_khoa="Luật DN". 2. Loại=PDF. 3. Tìm kiếm. | **STATE**: Backend filter AND tu_khoa LIKE + loai=PDF. **UI**: Đúng 1 record (PDF "Luật DN 2020"). KHÔNG có VIDEO "Luật DN 2020". **PERSIST**: — | Happy |
| TC-BG-005 | FR-III-08 / SCR-III-03 | Click row hiển thị preview panel theo loại | CB_NV_TW đăng nhập. Seed 1 PDF + 1 VIDEO + 1 SLIDE. | — | 1. SCR-III-03. 2. Click lần lượt 3 row. | **STATE**: `GET /api/v1/bai-giang/{id}` mỗi click. **UI**: PDF → preview iframe `<embed>` với PDF content. VIDEO → YouTube iframe embed (`https://www.youtube.com/embed/...`). SLIDE → render PPTX hoặc download link (depend implementation; nếu chỉ download thì raise SPEC-CLARIFY-DT-09 cho phương thức render PPTX). **PERSIST**: Quay lại row khác → preview update. | Happy 🟡 |

---

## C. CREATE — Thêm bài giảng SLIDE (PPTX)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-006 | FR-III-07 / BR-DATA-03 / BR-DATA-05 | Thêm bài giảng SLIDE thành công, file 18MB.pptx | CB_NV_TW đăng nhập. KHOA_HOC "KH-20260601-001" DA_DUYET tồn tại. Lĩnh vực "DAN_SU" tồn tại (FR-10). | ten_bai_giang="Bài 1 - Luật DN 2020", mo_ta="Tổng quan luật DN", loai=SLIDE, file=`bai1.pptx` (18MB), khoa_hoc_id=KH-20260601-001, linh_vuc_ids=[DAN_SU], thu_tu=1, cong_khai=false | 1. Click [+ Thêm bài giảng]. 2. Điền Tên + Mô tả + chọn Loại=SLIDE. 3. Upload file `bai1.pptx` 18MB. 4. Chọn KHOA_HOC + Lĩnh vực. 5. Click [Đồng ý]. | **STATE**: INSERT BAI_GIANG với loai_tai_lieu=SLIDE, duong_dan_file=`storage/bai-giang/{uuid}.pptx`, dung_luong=18874368 (18MB bytes), cong_khai=false. AUDIT_LOG hanh_dong=CREATE entity=BAI_GIANG (BR-DATA-05). 7 common fields (BR-DATA-03). **UI**: Toast "Thêm bài giảng thành công" (SRS Gap message → SPEC-CLARIFY-DT-10). Form đóng, list refresh. **PERSIST**: Reload → record xuất hiện với loại SLIDE. | Happy 🔴 |

---

## C2. CREATE — Thêm bài giảng PDF

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-007 | FR-III-07 | Thêm bài giảng PDF thành công, file 19.5MB | CB_NV_TW đăng nhập. KHOA_HOC DA_DUYET tồn tại. | ten="Bài 2 - Hợp đồng", loai=PDF, file=`bai2.pdf` (19.5MB) | 1-5 như TC-BG-006 nhưng Loại=PDF + file PDF. | **STATE**: INSERT loai_tai_lieu=PDF, duong_dan_file=`*.pdf`, dung_luong=20447232. **UI**: Toast OK + preview PDF embed work. **PERSIST**: Detail → preview render PDF inline. | Happy 🔴 |
| TC-BG-008 | FR-III-07 / BR-DATA-04 | Thêm bài giảng PDF không gắn KHOA_HOC (orphan, dùng chung kho) | CB_NV_TW đăng nhập. | ten="Tài liệu chung 1", loai=PDF, file 5MB, khoa_hoc_id=null, linh_vuc_ids=[DAN_SU] | 1. Tạo bài giảng. 2. KHOA_HOC để trống. 3. Lưu. | **STATE**: INSERT với khoa_hoc_id=NULL (Inputs dòng 573-582 không mark khoa_hoc_id bắt buộc). **UI**: Toast OK. **PERSIST**: List filter "Không gắn KH" (nếu có) → record xuất hiện. **Note**: SPEC-CLARIFY-DT-11 — SRS không nói rõ khoa_hoc_id bắt buộc hay không trong UC26 (Inputs không list nó). 02-thu-tu-module dòng 602 ngụ ý 1-N trực tiếp → kho dùng chung không khả thi nếu khoa_hoc_id NOT NULL. | Edge 🟡 |

---

## C3. CREATE — Thêm bài giảng VIDEO (YouTube)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-009 | FR-III-07 | Thêm bài giảng VIDEO với YouTube link hợp lệ | CB_NV_TW đăng nhập. | ten="Video bài 3", loai=VIDEO, url_youtube="https://youtu.be/abc12345678", khoa_hoc_id=KH-20260601-001 | 1. Tạo bài giảng. 2. Loại=VIDEO. 3. Nhập URL `https://youtu.be/abc12345678`. 4. Lưu. | **STATE**: INSERT loai_tai_lieu=VIDEO, link_video=URL, duong_dan_file=NULL, dung_luong=NULL. **UI**: Toast OK. Preview iframe embed YouTube `https://www.youtube.com/embed/abc12345678`. **PERSIST**: Detail render YouTube player inline. | Happy 🔴 |
| TC-BG-010 | FR-III-07 | Thêm VIDEO với link YouTube full format `https://www.youtube.com/watch?v=...` | CB_NV_TW đăng nhập. | url_youtube="https://www.youtube.com/watch?v=xyz98765432" | 1-4 như TC-BG-009 với URL full format. | **STATE**: INSERT thành công, link_video lưu nguyên. **UI**: Preview iframe parse `v=xyz98765432`. **PERSIST**: BE phải parse được cả 2 format YouTube — nếu chỉ accept 1 format → log SPEC-CLARIFY-DT-12. | Happy |

---

## D. UPDATE — Sửa bài giảng

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-011 | FR-III-07 / BR-DATA-05 | Sửa metadata bài giảng (tên + mô tả + lĩnh vực), không đổi file | CB_NV_TW đăng nhập. BAI_GIANG "BG-001" loai=PDF tồn tại. | ten mới="Bài 1 - Luật DN 2020 (rev 2)", linh_vuc_ids=[DAN_SU, HINH_SU] | 1. Click [Sửa] row BG-001. 2. Đổi tên + thêm 1 lĩnh vực. 3. Lưu. | **STATE**: UPDATE BAI_GIANG SET ten_bai_giang, linh_vuc_ids JSON, updated_at=NOW(). AUDIT_LOG hanh_dong=UPDATE với du_lieu_cu/moi. **UI**: Toast OK. **PERSIST**: Reload list → tên mới hiển thị. | Happy |
| TC-BG-012 | FR-III-07 | Thay file PDF mới (replace storage), giữ metadata | CB_NV_TW đăng nhập. BAI_GIANG "BG-002" loai=PDF, file cũ 5MB. | file mới `bai2-v2.pdf` (8MB) | 1. Sửa BG-002. 2. Click [Thay file]. 3. Upload file mới 8MB. 4. Lưu. | **STATE**: UPDATE duong_dan_file mới, dung_luong=8388608. File cũ → archive hoặc xóa storage (SPEC-CLARIFY-DT-13: SRS không nói rõ replace strategy). **UI**: Preview update nội dung mới. **PERSIST**: Detail → file URL mới + size mới. | Happy 🟡 |

---

## E. DELETE — Xóa mềm

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-013 | FR-III-07 / BR-DATA-01 | Xóa mềm bài giảng chưa gắn KHOA_HOC nào | CB_NV_TW đăng nhập. BG-003 chưa có KH liên kết. | — | 1. Click [Xóa] row BG-003. 2. Confirm dialog. 3. [Xác nhận]. | **STATE**: UPDATE BAI_GIANG SET is_deleted=1, deleted_at, deleted_by (BR-DATA-01 soft delete). AUDIT_LOG hanh_dong=DELETE. **UI**: Toast "Xóa thành công". Record biến mất khỏi list. **PERSIST**: Reload → record không hiển thị. | Happy |
| TC-BG-014 | FR-III-07 / SPEC-CLARIFY-DT-14 | Xóa bài giảng đang gắn vào KHOA_HOC chưa duyệt → cảnh báo hay chặn? | CB_NV_TW đăng nhập. BG-004 đang được tham chiếu bởi KH-001 (DU_THAO). | — | 1. Click [Xóa] BG-004. 2. Quan sát phản hồi. | **STATE**: SRS không quote rõ — SPEC-CLARIFY-DT-14: SRS UC26 Processing-Xóa thiếu rule "BG đang dùng trong KH". Có thể cảnh báo "Bài giảng đang gắn vào N khóa học, vẫn xóa?" tương tự pattern UC28 NHCH (WRN-NHCH-01 dòng 751). **UI**: Toast/dialog cảnh báo. **PERSIST**: Tùy logic. Mark SPEC-CLARIFY-DT-14. | Edge 🟡 |

---

## F. TOGGLE Công khai

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-015 | FR-III-07 / SCR-III-03 | Toggle cong_khai từ false → true trên row | CB_NV_TW đăng nhập. BG-005 cong_khai=false. | — | 1. SCR-III-03. 2. Click switch on row BG-005. | **STATE**: UPDATE BAI_GIANG SET cong_khai=true, updated_at, updated_by. AUDIT_LOG. **UI**: Switch chuyển màu xanh, toast "Đã công khai". **PERSIST**: Reload → switch giữ on. Bài giảng xuất hiện trên Cổng PLQG (verify cross-module nếu có endpoint public list). | Happy |
| TC-BG-016 | FR-III-07 | Toggle cong_khai true → false (tắt công khai) | CB_NV_TW đăng nhập. BG-006 cong_khai=true. | — | 1. Click switch off. | **STATE**: UPDATE cong_khai=false. **UI**: Switch xám, toast "Đã tắt công khai". **PERSIST**: Reload giữ off. Cổng PLQG không còn list record này. | Happy |

---

## G. PREVIEW

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-017 | FR-III-07 / AC dòng 624 | Preview PDF inline (browser native) | CB_NV_TW đăng nhập. BG-007 loai=PDF. | — | 1. Click row BG-007. 2. Quan sát preview panel. | **STATE**: GET file URL (signed if storage private). **UI**: Iframe `<embed type="application/pdf" src="...">` render PDF với scroll/zoom. **PERSIST**: F5 reload giữ preview state. | Happy |
| TC-BG-018 | FR-III-07 | Preview YouTube embed video | CB_NV_TW đăng nhập. BG-008 loai=VIDEO link `https://youtu.be/abc12345678`. | — | 1. Click BG-008. | **STATE**: — **UI**: Iframe `<iframe src="https://www.youtube.com/embed/abc12345678" allowfullscreen>`. Play button work. **PERSIST**: — | Happy |

---

## H. NEGATIVE — Error Handling

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-019 | ERR-BG-01 | Upload file PDF > 20MB → ERR-BG-01 | CB_NV_TW đăng nhập. | file `big.pdf` 21MB, loai=PDF | 1. Tạo bài giảng. 2. Loại=PDF. 3. Upload file 21MB. 4. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline/toast "**File tối đa 20MB**" (NLM nguyên văn ERR-BG-01 srs-fr-03 dòng 616). Reject upload ở client OR backend reject 400. **PERSIST**: Count BAI_GIANG không đổi. | Negative 🔴 |
| TC-BG-020 | ERR-BG-02 | Upload file sai định dạng (.xlsx) khi loại=PDF → ERR-BG-02 | CB_NV_TW đăng nhập. | file `wrong.xlsx`, loai=PDF | 1. Tạo. 2. Loại=PDF. 3. Upload `.xlsx`. 4. Lưu. | **STATE**: KHÔNG INSERT. **UI**: "**Chỉ chấp nhận file Slide hoặc PDF**" (ERR-BG-02 dòng 617). Client side validation accept=`.pdf` chặn trước; nếu bypass → BE reject 400. **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-BG-021 | ERR-BG-03 | URL YouTube không hợp lệ (random text) → ERR-BG-03 | CB_NV_TW đăng nhập. | url_youtube="not-a-youtube-url" | 1. Tạo. 2. Loại=VIDEO. 3. Nhập URL invalid. 4. Lưu. | **STATE**: KHÔNG INSERT. **UI**: "**URL YouTube không hợp lệ**" (ERR-BG-03 dòng 618). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-BG-022 | FR-III-07 / Inputs Y | Tên bài giảng trống → reject | CB_NV_TW đăng nhập. | ten_bai_giang="" | 1. Tạo. 2. Bỏ trống Tên. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "Tên bài giảng là bắt buộc" (SRS Gap message — mark SPEC-CLARIFY-DT-15 cho ERR code). **PERSIST**: Count không đổi. | Negative 🔴 |
| TC-BG-023 | FR-III-07 / loai=SLIDE | Loại=SLIDE bỏ trống file → reject Cond field | CB_NV_TW đăng nhập. | loai=SLIDE, file=null | 1. Tạo. 2. Loại=SLIDE, không upload. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "File bài giảng là bắt buộc" (Inputs dòng 578 — Cond). **PERSIST**: Count không đổi. | Negative |
| TC-BG-024 | FR-III-07 / loai=VIDEO | Loại=VIDEO bỏ trống url_youtube → reject Cond | CB_NV_TW đăng nhập. | loai=VIDEO, url_youtube="" | 1. Tạo. 2. Loại=VIDEO, để trống URL. 3. Lưu. | **STATE**: KHÔNG INSERT. **UI**: Inline "URL YouTube là bắt buộc" (Inputs dòng 579 — Cond). **PERSIST**: Count không đổi. | Negative |

---

## I. PERMISSION (BR-AUTH-08 + Permission Matrix)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-025 | BR-AUTH-08 / Permission Matrix | CB_NV_DP chỉ thấy BG thuộc đơn vị ĐP của mình | CB_NV_DP_01 đăng nhập. Seed BG TW + BN + ĐP. | — | 1. Vào SCR-III-03. | **STATE**: `GET /api/v1/bai-giang` filter WHERE don_vi_id = cb_nv_dp_01.don_vi_id (BR-AUTH-08). **UI**: Chỉ hiển thị BG thuộc đơn vị ĐP. KHÔNG thấy BG TW/BN. **PERSIST**: Reload giữ scope. | Permission |
| TC-BG-026 | Permission Matrix | TVV không có quyền vào menu Kho bài giảng (CRUD) | TVV (tvv_01) đăng nhập. | URL trực tiếp `/dao-tao/bai-giang` | 1. Đăng nhập tvv_01. 2. Quan sát sidebar. 3. Cố navigate URL. | **STATE**: BE 403 nếu cố call. **UI**: Sidebar không có menu "Kho bài giảng" CRUD (TVV chỉ public_view qua Cổng). Direct URL → page lỗi/redirect. **PERSIST**: Reload vẫn bị chặn. | Permission |
| TC-BG-027 | Permission Matrix / BR-AUTH-08 | CB_PD không có quyền CREATE/UPDATE/DELETE BG (chỉ Read) | CB_PD_TW (cb_pd_tw_01) đăng nhập. | — | 1. Vào SCR-III-03. 2. Quan sát toolbar + cột Hành động. | **STATE**: — **UI**: Per Permission Matrix dòng 165 (BAI_GIANG CRUD chỉ CB_NV) → CB_PD button [+ Thêm bài giảng] và [Sửa]/[Xóa] ẨN/DISABLE. Read-only list. **PERSIST**: API direct PUT → 403. | Permission 🟡 |

---

## J. EDGE CASES (A4 added)

| ID | TraceID (Mã SRS) | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|-------------------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-BG-028 | ERR-BG-01 / Boundary | Upload file PDF chính xác 20MB (boundary max) và 20MB+1KB (over) | cb_nv_tw_01. | file_20MB.pdf (20×1024×1024 bytes); file_20MB_1KB.pdf (20×1024×1024+1024 bytes) | 2 lần test boundary. | **STATE**: 20MB INSERT OK; 20MB+1KB reject ERR-BG-01. **UI**: 20MB toast OK; 20MB+1KB inline "File tối đa 20MB". **PERSIST**: Count chỉ +1. SPEC-CLARIFY-DT-EC-09 cho convention "20MB" = 20 × 1024 × 1024 (binary) hay 20 × 1000 × 1000 (decimal). | Boundary 🔴 |
| TC-BG-029 | 🟠 DEFER (A7) FR-III-07 / Network / Upload đứt mạng | Upload PPTX 18MB đứt mạng giữa chừng → resume hay restart | cb_nv_tw_01. File 18MB. Cần Chrome DevTools "Throttling: Offline" toggle giữa upload (manual). | — | 1. Form upload. 2. Bật DevTools Network → Offline khi progress ~50%. 3. Reconnect. 4. Quan sát toast + list. | **STATE**: BE behavior tùy implement. SPEC-CLARIFY-DT-EC-10. **UI**: Toast error "Upload thất bại, vui lòng thử lại". **PERSIST**: List BAI_GIANG count không tăng. Reload form — không có draft. | Edge 🟡 (DEFER A7) |
| TC-BG-030 | FR-III-07 / Special character / File name Unicode | Upload file PPTX với tên file chứa Unicode + ký tự đặc biệt + spaces | cb_nv_tw_01. | filename="Bài 1 — Pháp luật DN 2020 (rev 2) 🎓.pptx" | 1. Upload file. 2. Lưu. 3. Verify storage path + download. | **STATE**: INSERT BAI_GIANG với duong_dan_file=`storage/{uuid}.pptx` (UUID rename) và `original_filename` lưu Unicode. **UI**: Cột tên hiển thị literal Unicode + emoji. Click [Tải xuống] → file tải về với tên gốc. **PERSIST**: SPEC-CLARIFY-DT-EC-11 — SRS không quote BE rename UUID hay giữ original. Default UUID + giữ original filename trong metadata. | Edge 🟡 |
| TC-BG-031 | ERR-BG-01 / Boundary lower | Upload file PDF 0 byte (file rỗng) — verify reject | cb_nv_tw_01. File `empty.pdf` size = 0 byte (header-only / corrupted). | loai=PDF, file=`empty.pdf` (0 byte) | 1. Form thêm bài giảng. 2. Loại=PDF. 3. Upload `empty.pdf`. 4. Lưu. | **STATE**: KHÔNG INSERT. BE check `dung_luong > 0` (per BR-DATA-03 + nghiệp vụ — file 0 byte không hợp lệ). **UI**: Inline error "File không hợp lệ hoặc rỗng" (SPEC-CLARIFY-DT-EC-12 nguyên văn — SRS gap với boundary lower). **PERSIST**: Count BAI_GIANG không đổi. Storage không có file. | Boundary 🟡 |

---

## SPEC-CLARIFY tickets (file này)

| Ticket | Issue | Đề xuất |
|--------|-------|---------|
| SPEC-CLARIFY-DT-09 | SRS không nói rõ phương thức render PPTX inline (Office Online / convert PDF / chỉ download) | BA xác nhận render strategy hoặc accept download fallback |
| SPEC-CLARIFY-DT-10 | SRS không có nguyên văn message thành công cho UC26 CREATE | BA confirm message text |
| SPEC-CLARIFY-DT-11 | SRS UC26 Inputs không mark `khoa_hoc_id` bắt buộc nhưng 02-thu-tu-module dòng 602 ngụ ý 1-N trực tiếp | BA confirm: BG có thể tồn tại không gắn KH? Nếu có → schema cần khoa_hoc_id NULL allowed |
| SPEC-CLARIFY-DT-12 | SRS không quote BE phải parse cả 2 format YouTube (`youtu.be/X` và `youtube.com/watch?v=X`) | BA confirm regex pattern URL accept |
| SPEC-CLARIFY-DT-13 | SRS không quote replace file strategy (xóa file cũ vs archive) | BA confirm |
| SPEC-CLARIFY-DT-14 | SRS UC26 Processing-Xóa thiếu rule khi BG đang gắn vào KHOA_HOC | Pattern WRN tương tự UC28 NHCH |
| SPEC-CLARIFY-DT-15 | SRS UC26 không có ERR code cho field "Tên bài giảng trống" | BA confirm ERR-BG-04 |
| SPEC-CLARIFY-DT-EC-09 | Convention "20MB" — binary (20×1024²) hay decimal (20×1000²) | BA confirm |
| SPEC-CLARIFY-DT-EC-10 | Multipart resume khi upload đứt mạng — SRS không quote support | BA confirm scope |
| SPEC-CLARIFY-DT-EC-11 | Storage convention — BE rename UUID hay giữ original filename + xử lý collision | BA confirm |
| SPEC-CLARIFY-DT-EC-12 | Boundary lower — file 0 byte: BE reject hay accept với warning? Nguyên văn message | BA confirm |

---

**Tổng TC file 9:** 28 TC active sau A7 (UI 2 + READ 5 + CREATE 5 + UPDATE 2 + DELETE 2 + TOGGLE 2 + PREVIEW 2 + NEGATIVE 6 + PERMISSION 3 + EDGE A4 4 = 31 raw → 28 sau A6 fill +1 TC-BG-031). A7 không LOẠI; DEFER 1 (TC-BG-029 cần DevTools Offline toggle manual).

---

## A7 Filter Notes

- **DEFER (A7):** TC-BG-029 — multipart resume cần Chrome DevTools Network "Offline" toggle giữa upload (manual operator + browser-controlled). Phase B chạy nếu QA có thời gian.
- **KEEP all others 27 TC:** Observable qua UI list + preview + network panel (file size validate, YouTube embed, toggle switch).
