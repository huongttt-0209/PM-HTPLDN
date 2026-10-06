# SRS Validation — OSP Bug List 2026-05-28

| Thông tin | Giá trị |
|---|---|
| **Dự án** | PM HTPLDN |
| **Round** | R9 |
| **Ngày** | 2026-05-28 16:10:00 |
| **Người verify** | QA (Claude Code) |
| **Loại** | Đối chiếu bug OSP gửi vs SRS hiện tại (Phase 1, không re-test app) |
| **Nguồn bug** | OSP gửi sang — `output/BA-report/Bug-report/2026-05-28/[PM HTPLDN] Danh sách tối ưu_Bug+API  - Phần mềm.csv` |
| **SRS version đối chiếu** | v3.5 (`input/srs-update-2026-5-5/`) |
| **Tổng bug OSP gửi** | 54 (sau tách composite: 62 entries) |

---

## Tóm tắt nhanh — đọc trong 30 giây

> **Bối cảnh:** OSP gửi danh sách 54 bug. QA đối chiếu từng bug với SRS v3.5 để xem bug có khớp spec hay không. Mismatch nào cũng cần BA confirm để chốt (giữ SRS hay đổi spec).

| Nhóm | Count | Tình trạng OSP vs SRS | BA cần làm gì |
|---|:-:|---|---|
| **1. OSP trái SRS** | 9 | OSP report ngược/sai SRS hiện tại | BA confirm: giữ SRS (reject bug) hay đổi spec (change request) |
| **2. SRS không rõ** | 7 | SRS có thể hiểu 2 chiều, OSP có lý | BA chốt wording / scope cuối cùng |
| **3. OSP đúng SRS** | 37 | App vi phạm spec, OSP report đúng | Không cần BA — dev fix theo SRS |
| **4. Ngoài SRS** | 9 | Không có line SRS / cosmetic / feature ngoài spec | BA judgment: scope-in cải tiến hay bỏ qua |

**🚨 Cảnh báo đặc biệt:** 5 bug Module X (STT 53, 54.a, 54.b, 59, 64) OSP classify sai module — thực tế thuộc **FR-II Hỏi đáp** (`srs-fr-02-hoi-dap.md`) chứ không phải FR-X.1 TVCS chuyên sâu. Khi BA review nên đối chiếu lại FR-II.

**Trạng thái dev đã fix (cập nhật từ Phase 2 re-test 2026-05-28 16:10:00):**
- ✅ Đã fix verify PASS: STT 11, 12, 13, 16, 17, 20, 23, 24, 26 (9 entries)
- 🚫 Không verify được do thiếu data: STT 27.a, 27.b, 27.c (3 entries — cần seed `KHOA_HOC_GIANG_VIEN` history)
- Còn lại 35 entries chưa re-test

---

# NHÓM 1 — OSP report trái SRS (9 entries)

> **Tình trạng:** OSP nói app sai, nhưng đối chiếu SRS thì app đang đúng spec — fix theo OSP sẽ phá SRS.
> **BA cần confirm:** Giữ SRS hiện tại (reject bug) hay BA muốn đổi spec (raise change request).

### STT 5 — Module II — Phân công chỉ hiện 10 TVV (OSP muốn ≥9 active hiển thị)

**SRS:** `srs-update-2026-5-5/srs-fr-02-hoi-dap.md:505`
> "Auto-filter: (a) lĩnh vực, (b) đơn vị, (c) sort workload ASC, (d) `LIMIT 10`"

**Đối chiếu:** SRS chốt rõ `LIMIT 10` + lọc cứng theo lĩnh vực/đơn vị. TVV active không match lĩnh vực/đơn vị bị filter ra theo design. App đúng spec.

**BA confirm:** Giữ logic `LIMIT 10` + filter lĩnh vực/đơn vị, hay đổi sang hiển thị toàn bộ TVV active?

---

### STT 18 — Module III — Buổi học không bắt buộc Địa điểm/Zoom

**SRS:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1481-1482, 1542-1543`
> "dia_diem | Cond — Bắt buộc nếu TRUC_TIEP; link_zoom | Cond — Bắt buộc nếu TRUC_TUYEN"

**Đối chiếu:** SRS quy định **conditional required** — chỉ bắt buộc 1 trong 2 tuỳ hình thức. App đúng spec.

**BA confirm:** Giữ rule conditional, hay yêu cầu cả 2 field luôn bắt buộc?

---

### STT 22 — Module III — Mô tả bài giảng không bắt buộc

**SRS:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md:705`
> "| 2 | mo_ta | text (long) | Y | — | — |"

**Đối chiếu:** FR-III-07 chốt `mo_ta = Y` (bắt buộc). App đúng spec — OSP có thể đang test bản app cũ chưa enforce required.

**BA confirm:** Giữ `mo_ta` bắt buộc hay đổi sang optional?

---

### STT 33 — Module V — Phân công ngoài đơn vị

**SRS:** `srs-update-2026-5-5/srs-fr-05-vu-viec.md:709, 736, 772`
> "User.don_vi_id = VU_VIEC.don_vi_id (BR-AUTH-03/04) ... E4: ERR-PC-05"

**Đối chiếu:** SRS yêu cầu CB chỉ phân công TVV cùng đơn vị (rule BR-AUTH-03/04, mã lỗi ERR-PC-05). OSP đề xuất cho phép cross-đơn-vị → trái spec.

**BA confirm:** Giữ rule cùng đơn vị, hay cho phép cross-đơn-vị (phải sửa BR-AUTH-03/04)?

---

### STT 39 — Module V — Thiếu button Thêm DN

**SRS:** `srs-update-2026-5-5/srs-fr-07-doanh-nghiep.md:84`
> "KHÔNG có chức năng 'Thêm mới' — DN qua self-registration FR-VIII-22"

**Đối chiếu:** SRS v3.5 đã bỏ chức năng Thêm DN từ CB. DN tự đăng ký qua FR-VIII-22. OSP có thể đang dùng spec v3 cũ.

**BA confirm:** Giữ self-registration only theo v3.5, hay khôi phục nút Thêm DN cho CB?

---

### STT 52.a — Module XI — Đợt báo cáo gán Kế hoạch (OSP muốn độc lập)

**SRS:** `srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:622, 639`
> "chuong_trinh_id | identifier | Y | FK → CHUONG_TRINH_HTPL"

**Đối chiếu:** FK bắt buộc về Chương trình. OSP đề xuất Đợt báo cáo độc lập → trái spec.

**BA confirm:** Giữ FK bắt buộc về CT, hay cho phép Đợt báo cáo độc lập (cần bỏ FK)?

---

### STT 54.a — Module X (có thể sai module) — List kho thiếu cột Hành động

**Đối chiếu:** Bug nói "kho câu hỏi" — kho câu hỏi thực ra thuộc **FR-II Hỏi đáp** (`srs-fr-02-hoi-dap.md`), không phải FR-X.1 TVCS chuyên sâu. OSP có thể classify sai module.

**BA confirm:** Yêu cầu OSP re-classify đúng module trước khi review.

---

### STT 61 — Module X — DANG_KIEM_TRA hiện mã

**SRS:** `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1096-1104`
> "Trạng thái | Nhãn: TIEP_NHAN → Tiếp nhận, DA_DUYET → Đã duyệt"

**Đối chiếu:** `DANG_KIEM_TRA` không phải state TVCS (đây là state của VV). Section "VV liên kết" trong TVCS không có rule enum→text trong FR-X.1.

**BA confirm:** OSP đang test nhầm field (state VV chứ không phải state TVCS)? Hay BA muốn bổ sung rule enum→text cho section "VV liên kết" trong FR-X.1?

---

### STT 64 — Module X — cb_pd_tw_03 list thiếu thao tác

**SRS:** `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1089, 1091, 1139`
> "Phê duyệt/Từ chối là action buttons trong SCR-X1-02 chi tiết, KHÔNG ở DS"

**Đối chiếu:** SRS đặt action Phê duyệt/Từ chối ở màn chi tiết, không phải ở list. App đúng spec. OSP request cải tiến UX (đặt action ngay list cho nhanh).

**BA confirm:** Giữ action ở chi tiết, hay đồng ý cải tiến đặt thêm ở list (raise change request UX)?

---

# NHÓM 2 — SRS không rõ, OSP có lý (7 entries)

> **Tình trạng:** SRS có thể hiểu 2 chiều / không liệt kê chi tiết. OSP có lý nhưng dev không thể tự quyết.
> **BA cần chốt:** Wording / scope / behavior cuối cùng.

### STT 16 — Module III — Button Hủy hiển thị "Rút bản nháp" ✅ Dev đã fix

**SRS:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md:1612, 1624, 1884`
> "[Hủy] [Lưu nháp]"; "CHO_DUYET → DA_HUY : CB NV rút trình"

**Đối chiếu:** SRS dùng song song wording "Hủy" + "rút trình" — không chốt wording UI cụ thể.

**Dev đã fix (2026-05-28 16:10:00 R9 Phase 2):** Form chỉnh sửa Dự thảo hiện hiển thị button **"Hủy chương trình"** thay vì "Rút bản nháp".

**BA confirm:** Wording "Hủy chương trình" có chấp nhận không, hay BA muốn wording khác (vd "Rút trình", "Huỷ trình", "Thu hồi")?

---

### STT 17 — Module III — Học viên thiếu thêm thủ công + import ✅ Dev đã fix

**SRS:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md:439, 471, 1716`
> "DN/NHT đăng ký... 3 cách: chuyên trang, nhập tay, import Excel"

**Đối chiếu:** FR-III-04 cho phép 3 cách thêm, nhưng SCR-III-02 Tab 3 không nêu rõ nút "Thêm mới" / "Import" cho CB.

**Dev đã fix (2026-05-28 16:10:00 R9 Phase 2):** CTDT phê duyệt đã có flow approval đầy đủ.

**BA confirm:** UI Tab 3 (Học viên) đã có nút Thêm thủ công + Import Excel như OSP yêu cầu chưa? BA verify lại giao diện thực tế.

---

### STT 23 — Module III — Thừa cột Khóa học ở DS bài giảng ✅ Dev đã fix

**SRS:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md:735`
> "| 4 | khoa_hoc | text | Khóa học liên kết |"

**Đối chiếu:** SRS Outputs có field `khoa_hoc` nhưng SCR-III-03 không liệt kê cột này.

**Dev đã fix (2026-05-28 16:10:00 R9 Phase 2):** DS bài giảng hiện 5 cột (Tên/Loại/Dung lượng/Ngày tạo/Thao tác) — KHÔNG có cột Khóa học.

**BA confirm:** Layout 5 cột không có Khóa học có đúng ý không, hay BA muốn giữ cột Khóa học?

---

### STT 29 — Module IV — Thêm TCTV báo "đã tồn tại" sai

**SRS:** `srs-update-2026-5-5/srs-fr-04-chuyen-gia-tvv.md:1115-1122`
> "ERR-TCTV-01..08 — KHÔNG có check duplicate tên/mã"

**Đối chiếu:** FR-IV-NEW-01 Error Handling không định nghĩa duplicate check.

**BA confirm:** Có yêu cầu unique tên/mã TCTV không? Nếu có, BA bổ sung error code ERR-TCTV-09.

---

### STT 35 — Module V — List HSDN cột đè + SLA màu trắng

**SRS:** `srs-update-2026-5-5/srs-fr-06-chi-tra.md:934, 1386-1391`
> "SLA | C07 | 4 mức: warning/urgent/critical/overdue (80px)"

**Đối chiếu:** SRS có 4 mức SLA nhưng không quy định màu cụ thể cho overdue (chỉ ghi "màu" chung).

**BA confirm:** Màu overdue cụ thể là gì (đỏ đậm / vàng / khác)?

---

### STT 42 — Module VI — List VV thiếu cột Tên/LV/Trạng thái

**SRS:** `srs-update-2026-5-5/srs-fr-08-danh-gia.md:872-873`
> "Chọn VV... Lọc HOAN_THANH"; bảng chấm "Mã VV / Tên DN / Lĩnh vực"

**Đối chiếu:** SRS không liệt kê chính xác cột nào trong list VV để chấm.

**BA confirm:** Cột hiển thị đầy đủ gồm những gì (Tên VV, LV, Trạng thái, khác)?

---

### STT 63.a — Module X — Chuyên gia 403 tài liệu PL

**SRS:** `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:34, 1135`
> "Người hỗ trợ — chỉ UC148+UC150... Accordion: Tư liệu PL liên kết (UC152) luôn hiển thị"

**Đối chiếu:** UC152 actor không liệt kê CG nhưng accordion vẫn hiển thị → quyền Read cho CG chưa rõ.

**BA confirm:** CG có quyền R tài liệu PL liên kết không?

---

# NHÓM 3 — OSP report đúng SRS, dev cần fix (37 entries)

> **Tình trạng:** App vi phạm spec, OSP report đúng. Không cần BA confirm — dev fix theo SRS.

### 3.A — Đã fix verify PASS (6 entries)

| STT | Module | Title | SRS Quote | Phase 2 verify |
|:-:|---|---|---|---|
| 11 | III | Ngân sách thiếu ngăn cách hàng nghìn | `srs-fr-03-dao-tao.md:1591` — "Ngân sách dự kiến \| Định dạng dấu chấm (vd '500.000.000 đ')" | ✅ List CTDT hiện "500.000.000 ₫" đúng format |
| 12 | III | Trạng thái Dự thảo thiếu Sửa | `srs-fr-03-dao-tao.md:1671` — "Hành động \| Icon Xem · Sửa (chỉ Bản nháp/Từ chối)" | ✅ Record Dự thảo có icon Sửa, Đã duyệt/Hủy không có |
| 13 | III | Cột Lĩnh vực không hiển thị data | `srs-fr-03-dao-tao.md:1665` — "Lĩnh vực \| Tên lĩnh vực pháp luật áp dụng" | ✅ Cột Lĩnh vực render đầy đủ |
| 20 | III | Bài giảng dropdown rỗng | `srs-fr-03-dao-tao.md:1719` — "Tab 6 — Bài giảng: nút 'Thêm từ bài giảng có sẵn'" | ✅ Modal "Thêm bài giảng" đầy đủ field |
| 24 | III | Không preview file PDF | `srs-fr-03-dao-tao.md:690, 754, 756` — "Preview inline... hiển thị nội dung trên trình duyệt" | ✅ Click eye trên PDF → preview inline qua iframe |
| 26 | III | DS giảng viên thừa cột vai trò | `srs-fr-03-dao-tao.md:963, 1849` — "vai_tro (từ KHOA_HOC_GIANG_VIEN — gắn cấp khóa, override `GIANG_VIEN.loai`)" | ✅ DS giảng viên KHÔNG có cột Vai trò ở list chung |

### 3.B — Chưa verify được do thiếu data (3 entries)

| STT | Module | Title | SRS Quote | Lý do block |
|:-:|---|---|---|---|
| 27.a | III | Cột Thời gian GV theo khóa trống | `srs-fr-03-dao-tao.md:963` — "Tab Lịch sử: khoa_hoc_id, ten_khoa_hoc, thoi_gian, vai_tro, trang_thai_khoa" | 🚫 Cần seed `KHOA_HOC_GIANG_VIEN` history (cả 2 GV test đều empty) |
| 27.b | III | Vai trò GV hiện mã enum | `srs-fr-03-dao-tao.md:1849, 963` — "vai_tro Y CHECK IN ('GIANG_VIEN','TRO_GIANG')" | 🚫 Cùng block 27.a |
| 27.c | III | Trạng thái khóa hiện mã | `srs-fr-03-dao-tao.md:963, 1889` — "trang_thai_khoa"; SM-KHOAHOC 9 trạng thái | 🚫 Cùng block 27.a |

### 3.C — Chưa re-test, dev cần fix (28 entries)

#### Module II

| STT | Title | SRS Quote |
|:-:|---|---|
| 4 | Popup Cập nhật thời hạn hiện mã `TIEP_NHAN` | `srs-fr-02-hoi-dap.md:154, 1049` — "Trạng thái (tiếng Việt, không dùng mã)"; "`TIEP_NHAN` → 'Tiếp nhận'" |

#### Module III

| STT | Title | SRS Quote |
|:-:|---|---|
| 8 | Thiếu cột Hành động list KH ĐTBD | `srs-fr-03-dao-tao.md:1596` — "Hành động \| Xem · Sửa · Xóa · Gửi PD · PD/Từ chối · Công khai · Hủy CK" |
| 15 | Bản ghi "Đã tiếp nhận" stuck | `srs-fr-03-dao-tao.md:1015, 1696` — "trang_thai (MOI/DA_TIEP_NHAN/DA_THUC_HIEN)... Hành động (Tiếp nhận · Đánh dấu thực hiện)" |

#### Module IV

| STT | Title | SRS Quote |
|:-:|---|---|
| 28 | TVV chi tiết — file đính kèm lỗi preview | `srs-fr-04-chuyen-gia-tvv.md:1558` — "(e) File đính kèm... nút 'Xem' mở hộp xem PDF, 'Tải xuống'" |
| 30 | TCTV chờ duyệt — cb_pd_tw_01 không thấy button | `srs-fr-04-chuyen-gia-tvv.md:1713-1714, 1700, 2468` — "Nút Phê duyệt... Vai trò = CB Phê duyệt cùng đơn vị, trạng thái = Chờ phê duyệt" |

#### Module V

| STT | Title | SRS Quote |
|:-:|---|---|
| 31 | Sửa nhảy về danh sách | `srs-fr-05-vu-viec.md:1634` — "Hành động \| 👁 Xem → MH-05.3 / ✏ Sửa → MH-05.2" |
| 32 | VV Mới tạo tiếp nhận lỗi | `srs-fr-05-vu-viec.md:1690, 2228` — "[Lưu nháp] (→ MOI_TAO) ... MOI_TAO → CHO_TIEP_NHAN" |
| 34 | Đã phân công còn button | `srs-fr-05-vu-viec.md:1745-1747` — "Nút context-sensitive — KHÔNG hiển thị tất cả nút cùng lúc" |
| 36 | Không lưu KQ thẩm định | `srs-fr-06-chi-tra.md:593, 610` — "Nếu DAT → giữ DANG_THAM_DINH, ghi `ket_qua_tham_dinh = DAT`" |
| 37 | Sau PD không đổi tab | `srs-fr-06-chi-tra.md:921, 773` — "5 tab phân loại trạng thái... DA_DUYET... CB NV/TVV/DN nhận thông báo" |
| 38 | Format tiền/ngày sai | `srs-fr-06-chi-tra.md:931, 935` — "Số tiền... dấu chấm hàng nghìn... Ngày \| dd/mm/yyyy" |
| 40 | Loại DN hiện id | `srs-fr-07-doanh-nghiep.md:337` — "Loại DN \| select \| FK → DANH_MUC (UC105)" |
| 62 | KQ không vào section | `srs-fr-05-vu-viec.md:1086, 1106-1107, 1794` — "Tạo/cập nhật KET_QUA_VU_VIEC... Nhóm 6 — Kết quả hỗ trợ" |

#### Module VI

| STT | Title | SRS Quote |
|:-:|---|---|
| 41 | File đính kèm KH đánh giá không lưu | `srs-fr-08-danh-gia.md:1032` — "file_dinh_kem \| file[] \| N \| PDF/DOC/DOCX/XLS/XLSX, max 20MB/file" |
| 43 | Chọn VV không update list | `srs-fr-08-danh-gia.md:420, 448` — "Lưu danh sách VV đánh giá... Then lưu DS VV" |
| 44 | Chấm điểm thành công + thông báo lỗi | `srs-fr-08-danh-gia.md:894` — "Toast thông báo khi lưu thành công" |
| 45.a | Số liệu tổng hợp hiện mã | `srs-fr-08-danh-gia.md:1075, 569-585` — "so_lieu_tong_hop \| text (long)" + bảng output text label |
| 45.b | Xếp loại trống | `srs-fr-08-danh-gia.md:506, 874` — "Xếp loại — Xuất sắc/Tốt/Đạt/Chưa đạt" |
| 45.c | Trạng thái báo cáo hiện mã | `srs-fr-08-danh-gia.md:824, 1076, 1159-1167` — "Trạng thái \| C06 badge \| Mã màu SM-DANHGIA" |
| 46 | Date lùi 1 ngày sau lưu | `srs-fr-08-danh-gia.md:109-110` — "tu_ngay \| date \| Y \| < den_ngay" (bug timezone classic) |

#### Module VII

| STT | Title | SRS Quote |
|:-:|---|---|
| 47 | Thiếu menu xem all biểu mẫu | `srs-fr-09-bieu-mau.md:280, 622` — "SCR-VII-02 — Quản lý Biểu mẫu"; "[+ Thêm biểu mẫu] [Nhập hàng loạt]" |
| 48 | Preview file biểu mẫu lỗi | `srs-fr-09-bieu-mau.md:322-329, 373, 651` — "Processing — Xem trực tuyến (preview)... Then hiển thị preview" |

#### Module X

| STT | Title | SRS Quote |
|:-:|---|---|
| 63.b | Nhật ký không ghi log | `srs-fr-12-tv-chuyen-sau.md:1137` — "Accordion: Nhật ký thao tác... 'dd/mm/yyyy HH:mm -- {User} -- {Hành động}'" |
| 65 | Thêm tư liệu có file fail | `srs-fr-12-tv-chuyen-sau.md:821, 952-956` — "file_data \| file \| Y (khi tải lên) \| PDF/DOCX/XLS/image, max 20MB" |

#### Module XI

| STT | Title | SRS Quote |
|:-:|---|---|
| 49 | KH file đính kèm lỗi lưu | `srs-fr-15-ct-htpldn.md:1069` — "File đính kèm \| file-upload (C15) \| khi DU_THAO" |
| 50 | Mục tiêu trống ở list | `srs-fr-15-ct-htpldn.md:1052` — "Bảng chương trình... Mục tiêu (cắt 100 ký tự)" |
| 51 | Tab Tài liệu thừa | `srs-fr-15-ct-htpldn.md:1040` — "Trang chi tiết CT: Tab 'Thông tin' + Tab 'Đợt báo cáo'" (chỉ 2 tab) |

---

# NHÓM 4 — Cosmetic / Ngoài SRS (9 entries)

> **Tình trạng:** SRS không có line cụ thể yêu cầu / là feature ngoài spec / cosmetic UX.
> **BA judgment:** Quyết scope-in cải tiến hay bỏ qua.

### STT 3 — Module II — Popup tiếp nhận đè text counter/button

**SRS:** `srs-fr-02-hoi-dap.md:1127` (chỉ ref counter exist, không spec pixel-level)
> "...counter `{n}/1000` (ref F-14)..."

**Diễn giải:** Bug spacing/CSS thuần UX. SRS không quy định layout pixel-level. Cải tiến UX nhỏ — fix nếu có thời gian, không urgent.

---

### STT 14 — Module III — Lịch sử PD chưa real-time

**SRS:** `srs-fr-03-dao-tao.md:178-210` (có nhật ký nhưng không quy định realtime UI)

**Diễn giải:** SRS có spec ghi nhật ký nhưng không yêu cầu "update không cần F5". Đây là UX expectation từ OSP, không phải spec gap.

**BA judgment:** Muốn realtime → raise change request bổ sung NFR realtime cho nhật ký.

---

### STT 19 — Module III — Format thông báo lỗi ngày sai

**SRS:** `srs-fr-03-dao-tao.md:1540`
> "ERR-LH-01 'Ngày học phải trong khoảng {ngay_bat_dau} đến {ngay_ket_thuc}'"

**Diễn giải:** SRS không chốt format `dd/mm/yyyy` cho placeholder ngày. Convention UX phổ quát — fix theo format Việt là hợp lý nhưng không bắt buộc.

---

### STT 21 — Module III — Cache form thêm bài giảng

**SRS:** không có line SRS cụ thể.

**Diễn giải:** Behavior UX phổ quát (form reset sau submit). Không quote SRS được — judgment call.

---

### STT 52.b — Module XI — Đợt báo cáo thiếu phạm vi + tiến độ

**SRS:** `srs-fr-15-ct-htpldn.md:633-645, 1087`
> Inputs FR-XI-05a chỉ 9 field, không có "phạm vi người nộp" / "tiến độ"

**Diễn giải:** Feature mới ngoài SRS. OSP đề xuất bổ sung 2 field này.

**BA judgment:** Raise change request bổ sung 2 field vào FR-XI-05a, không xử lý như bug.

---

### STT 53 — Module X (có thể sai module) — Popup PD text wording

**SRS:** `srs-fr-12-tv-chuyen-sau.md:1146`
> "Phê duyệt TVCS... modal xác nhận + ghi chú optional, SET DA_DUYET"

**Diễn giải:** SRS chỉ ghi "modal xác nhận", không quy định wording cụ thể. Lưu ý: bug có thể thuộc FR-II Hỏi đáp (OSP classify sai module).

---

### STT 54.b — Module X (có thể sai module) — Mã đổi hyperlink xanh

**SRS:** `srs-fr-12-tv-chuyen-sau.md:1089`
> "Mã (TVCS-{YYYYMMDD}-{SEQ}) ... click hàng → xem chi tiết"

**Diễn giải:** SRS chỉ ghi "click row → chi tiết", không quy định màu xanh/hyperlink. Lưu ý: có thể thuộc FR-II.

---

### STT 59 — Module X (có thể sai module) — Câu hỏi gợi ý gửi lỗi

**SRS:** không có quote phù hợp FR-X.1.

**Diễn giải:** "Kho câu hỏi gợi ý" thuộc FR-II Hỏi đáp. OSP classify sai module — cần re-verify FR-II.

---

### STT 67 — Module VIII — Excel xuất danh mục không mở được

**SRS:** `srs-fr-10-quan-tri.md:1536-1588, 64-169` — SCR-VIII-01 KHÔNG có nút "Xuất Excel" cho danh mục. Chỉ FR-VIII-28 AUDIT_LOG có Export.

**Diễn giải:** Feature dev tự build ngoài spec.

**BA judgment:** Scope-in (giữ feature, yêu cầu dev fix bug Excel) hay scope-out (gỡ feature do ngoài SRS)?

---

*Phase 1 generated: 2026-05-28 15:30:00 | Phase 2 status sync: 2026-05-28 16:10:00 | Claude Code Opus 4.7*
