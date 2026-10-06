# Kế hoạch verify module "Tư vấn pháp luật chuyên sâu" (TVCS) — tuần 3

> **Vì sao chia batch:** cụm TVCS có **23 case** đối tác báo (rows **277–301**, tab `UAT_TGPL Doanh Nghiệp-tuần 3`), trải 3 chức năng con trên cùng nhóm màn hình.
> Chạy 23 case trong 1 session → vỡ context → chất lượng verify tụt (đúng bài học postmortem 16/07: "mù" khi chạy nhiều case một lúc).
> → Chia **6 batch** theo **màn hình + cụm lỗi (pattern) + tiền đề seed dùng chung** để mỗi session học 1 nhóm rule SRS, seed 1 lần, verify nhất quán.
> Mỗi batch **mở 1 cửa sổ Claude Code MỚI**, dán nguyên khối file `tvcs/SESSION-tvcs-batch{A..F}-prompt.md` tương ứng.
> **Chỉ có file prompt** nằm phẳng trong `tvcs/`. **Bug + BA + cond + audit ghi vào FOLDER BUG TỔNG của round** (`reverify-week-3/bug-reports|cond|reverify-audit/`), đặt tên file theo batch (`bug-report-tvcs-batch{X}.md`) để không đụng nhau khi chạy song song.
>
> **QLHSPLDN (2 case, rows 292–293) KHÔNG thuộc kế hoạch này** — đã tách folder riêng `reverify-week-3/session-prompts/qlhspldn/` vì truy cập qua menu **Doanh nghiệp** (màn khác). Xem `session-prompts/qlhspldn/SESSION-qlhspldn-PLAN.md`.

## SRS gốc của module — TẤT CẢ trong 1 file
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md` (Nhóm X.1 — Quản lý Tư vấn pháp luật chuyên sâu, UC147–UC153).

🔴 **v2.1 gộp màn hình (dòng 1073):** chỉ còn **2 màn hình menu chính** — MH-12.1 (SCR-X1-01 danh sách) + MH-12.2 (SCR-X1-02 chi tiết, dạng accordion + action buttons). Các màn cũ (Phân công CG, Xác nhận CG, Phê duyệt, Tư liệu PL) **gộp thành tab/action button trong SCR-X1-02** — KHÔNG còn màn riêng (SCR-X1-03..07 DEPRECATED, dòng 1161–1187).

Map prefix mã TC → FR / UC / màn hình SCR:

| Prefix | FR / UC | Chức năng | Màn hình SCR | Batch |
|---|---|---|---|:-:|
| QLNDTVVCG | FR-X.1-01 / UC147 (dòng 86) | Quản lý nội dung TV với chuyên gia | SCR-X1-01 (list) + SCR-X1-02 (chi tiết) | A·B·C·D |
| TKNDTVVCG | FR-X.1-02 / UC148 (dòng 327) | Tìm kiếm nội dung TV với chuyên gia | SCR-X1-01 (list) | A |
| QLTLPLCVV | FR-X.1-06 / UC152 (dòng 795) | Quản lý tư liệu pháp lý của vụ việc | SCR-X1-02 tab "Tư liệu PL" | E·F |

🔴 **Điểm neo SRS quan trọng (mở file verify TRƯỚC khi chốt — CẤM kết luận từ trí nhớ):**

| Chủ đề | Dòng SRS | Nội dung |
|---|---|---|
| Cột bảng danh sách TVCS | **1098** | Checkbox / Mã / **Tiêu đề** / Tên DN / Tên CG / Lĩnh vực PL / Trạng thái (badge) / Ngày tư vấn / Ngày tạo / Hành động (Xem/Sửa/Phân công CG/Hủy) |
| 3 tab phân loại + số đếm | **1091** | "Chờ xử lý" (TIEP_NHAN+PHAN_CONG) / "Đang tư vấn" (DANG_TU_VAN+HOAN_THANH+CHO_PHE_DUYET) / "Hoàn thành" (DA_DUYET+HUY) — **có số đếm** |
| Form Nhóm 1 Thông tin cơ bản | **1142** | Mã (auto, read-only) / DN (bắt buộc — **chọn → hiện MST, địa chỉ, người đại diện**) / CG (bắt buộc — **chọn → hiện chuyên môn, SĐT, email**) / Lĩnh vực (bắt buộc) / Ngày tư vấn (bắt buộc) / Ghi chú. **KHÔNG có field "Cơ quan tiếp nhận"** (don_vi_id auto = đơn vị CB login, dòng 118) |
| Form Nhóm 2 Nội dung tư vấn | **1143** | **Tiêu đề** (bắt buộc, max 255) / Nội dung TV chi tiết (**Rich Text Editor**, bắt buộc, max 50KB) |
| 5 nhóm accordion màn chi tiết | **1133, 1141–1148** | Thông tin cơ bản / Nội dung TV / **Tư liệu PL liên kết** / Đánh giá CL / **Nhật ký thao tác** (+ Công khai chỉ khi DA_DUYET) = **5 nhóm** |
| Điều kiện hiện nút Sửa (mode sửa) | **1152** | "Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)" |
| Modal Phân công CG | **1153** | gợi ý TOP 5 CG (lĩnh vực khớp, điểm TB DESC, workload ASC) + tìm CG + ghi chú + **info SLA (2 ngày LV xác nhận)** |
| Nhật ký thao tác | **1146** + BR-DATA-05 | timeline "dd/mm/yyyy HH:mm -- {User} -- {Hành động}", lịch sử chuyển trạng thái + CUD |
| SM-TVCS (7 trạng thái) | **1467–1513** | TIEP_NHAN→PHAN_CONG→DANG_TU_VAN→HOAN_THANH→CHO_PHE_DUYET→DA_DUYET (+HUY). Hủy từ DANG_TU_VAN: **guard "DN yêu cầu hủy + CB PD duyệt"** (dòng 1484, 1512) |
| Auto notif khi Hoàn thành | **196** + SM dòng 1508 | HOAN_THANH → CHO_PHE_DUYET (Auto), **gửi TB CB Phê duyệt cùng đơn vị** (BR-FLOW-01, BR-NOTIF-01) |
| Tư liệu PL — cột danh sách | **928–939** | id / ten_tu_lieu / loai_tu_lieu / ten_vu_viec / ten_linh_vuc / trang_thai / so_file / **nguoi_tao** / **ngay_tao** (dd/mm/yyyy HH:mm) |
| Tư liệu PL — sửa khi CONG_KHAI | **888** | "nếu CONG_KHAI → **từ chối sửa** (phải hủy công khai trước)" |
| Tư liệu PL — xóa khi CONG_KHAI | **893–902** (step 899) | Xóa được: nếu CONG_KHAI → auto set cong_khai=0 trước rồi soft-delete. **KHÔNG disable nút Xóa** |
| Tư liệu PL — upload mã độc | **955, 956** | ERR-TLPL-04 "File '{ten_file}' chứa mã độc" (E4); ERR-TLPL-05 công khai thiếu file (E5) |

## 6 batch (tổng 23 case)

| Batch | Chủ đề / cụm lỗi | # | Mã TC (rows) | Màn hình / tiền đề seed chung | File prompt |
|:-:|---|:-:|---|---|---|
| **A** | Màn **danh sách** TVCS: cột / tab phân loại / xuất Excel / tìm kiếm (SCR-X1-01) | 4 | QLNDTVVCG_03·04·40, TKNDTVVCG_03 (r277,278,290,291) | SCR-X1-01. Seed: ≥1 TVCS record có Tiêu đề + DN (để search ra) | `SESSION-tvcs-batchA-prompt.md` |
| **B** | Màn **Thêm/Sửa** TVCS: form Nhóm 1+2, autofill DN/CG, nút Sửa theo state (SCR-X1-02) | 4 | QLNDTVVCG_06·07·08·11 (r279,280,281,282) | SCR-X1-02 form. Seed: record TIEP_NHAN + record DANG_TU_VAN (test nút Sửa) | `SESSION-tvcs-batchB-prompt.md` |
| **C** | Màn **Chi tiết** (read): 5 vs 7 nhóm, tên nhóm, trường chi tiết, Nhật ký, modal Phân công (SCR-X1-02) | 4 | QLNDTVVCG_15·17·20·22 (r283,284,285,286) | SCR-X1-02 chi tiết. Seed: 1 record đã chạy hết vòng đời (để Nhật ký có lịch sử) + 1 record TIEP_NHAN (mở modal Phân công) | `SESSION-tvcs-batchC-prompt.md` |
| **D** | **Workflow / chuyển trạng thái** (multi-role): phân công, hoàn thành→thông báo, hủy từ Đang tư vấn | 3 | QLNDTVVCG_23·27·36 (r287,288,289) | SCR-X1-02 action buttons + SM-TVCS. ⚠️ Cần CG + CB PD **cùng đơn vị**. Seed: record TIEP_NHAN (phân công), DANG_TU_VAN (hoàn thành + hủy) | `SESSION-tvcs-batchD-prompt.md` |
| **E** | **Tư liệu PL** — danh sách + hiển thị + điều kiện nút Thêm/Sửa (tab trong SCR-X1-02) | 4 | QLTLPLCVV_02·03·07·08 (r294,295,296,297) | Tab "Tư liệu PL". Seed: 1 TVCS + tư liệu ở NHAP **và** CONG_KHAI + tư liệu có file đính kèm | `SESSION-tvcs-batchE-prompt.md` |
| **F** | **Tư liệu PL** — sửa/xóa/upload validation (message + confirm) | 4 | QLTLPLCVV_09·11·15·16 (r298,299,300,301) | Tab "Tư liệu PL". Seed: tư liệu CONG_KHAI + file đính kèm + **file EICAR test mã độc** | `SESSION-tvcs-batchF-prompt.md` |

**Kích thước 4/4/4/3/4/4 — mỗi batch ≤4 case** → 1 session verify trọn không vỡ context. (TVCS case nặng hơn danh mục QTHT vì có workflow/state/multi-role → chia nhỏ hơn.)

## 🔴 Vai trò dùng verdict — login CB NV, KHÔNG dùng admin
Tác nhân của UC147/148/152 là **Cán bộ Nghiệp vụ (CB NV)** (SRS dòng 97, 338, 806). → **Login `cbnv_*` / `Test@1234`** để verdict, KHÔNG dùng admin.
- ⚠️ Khác QTHT: ở đây admin (QTHT) KHÔNG phải vai trò của bug → dùng admin ra verdict = **vi phạm** protocol §Nguyên tắc 3 (quyền rộng che lỗi phân quyền/scope). Admin chỉ dùng **prep/seed data** nếu cần (vd tạo account, gán vai trò CG).
- **Multi-tenant scope (BR-AUTH-08, dòng 1530):** CB NV chỉ thấy TVCS thuộc **đơn vị mình**. → Seed record bằng đúng account `cbnv_*` sẽ dùng verdict, để record hiện trong scope. Đề xuất nhất quán 1 đơn vị/batch.
- **Batch D (workflow)** cần thêm: **CG được phân công** (`qa_tvvseed28` — TVV+CG, Cục Bổ trợ tư pháp TW) + **CB Phê duyệt cùng đơn vị** (`cbpd_*`). Ràng buộc cứng: CG + CB NV + CB PD phải **cùng đơn vị** thì luồng mới chạy. Xác định đơn vị chung (hoặc seed account theo §Nguyên tắc 4) TRƯỚC khi test.

## 🔴 Cụm lỗi xuyên batch — verify chéo, nghi bug gốc chung (đừng log rời)

1. **Cụm "Trường Tiêu đề bị thiếu / trường Mô tả thừa"** — xuyên **A (03)** (cột danh sách), **B (08)** (form nhập), **C (17)** (chi tiết). SRS: Tiêu đề bắt buộc (dòng 114, 1098, 1143, 312 ERR-TVCS-06); "Mô tả" KHÔNG có trong SRS Inputs/Output. Nghi **1 bug gốc**: FE dùng field `mo_ta`/`tom_tat` cũ thay cho `tieu_de` (SRS dòng 114 ghi rõ "chính thức hóa từ `tom_tat`"). Verify cả 3 điểm, log rõ "gốc chung".

2. **Cụm "Trường Cơ quan tiếp nhận"** — **B (06)** (form thiếu) vs **C (17)** (chi tiết thiếu). ⚠️ **Cẩn thận:** SRS form (dòng 1142) **KHÔNG liệt kê** field "Cơ quan tiếp nhận" cho CB nhập tay (don_vi_id auto = đơn vị CB login, dòng 118). → đối tác kỳ vọng field này = **`BA confirm`** (kỳ vọng khác SRS), KHÔNG auto-Open. Đọc dòng 118 + 1142 xác nhận trước khi chốt.

3. **Cụm "Điều kiện hiển thị nút theo trạng thái"** — **B (11)** (nút Sửa TVCS theo state, dòng 1152), **E (03)** (nút Thêm tư liệu theo state TVCS), **E (07)** (nút Sửa tư liệu theo state NHAP/CONG_KHAI, dòng 888). Nghi cùng nhóm bug "gating nút không đúng state". Cần record ở **nhiều trạng thái** để phân biệt. Verify từng nút riêng, đừng gộp verdict.

4. **Cụm "Tên nhóm / label hiển thị sai so SRS"** — **C (15)**: "Tư liệu pháp lý liên kết"→"Tư liệu pháp luật", "Nhật ký thao tác"→"Nhật ký"; 5 nhóm→7 nhóm. Bug tĩnh (label cố định) → dùng `--static-bug`, không cần bảng đối chiếu điều kiện. Đối chiếu dòng 1133/1141–1148.

5. **Cụm "Thông báo lỗi generic thay message chuẩn SRS"** — **F (09)** (sửa CK: message kỹ thuật lộ field `moTa, fileDinhKemIds`), **F (15)** (upload mã độc: "Tải file thất bại" thay ERR-TLPL-04). ⚠️ **Vùng nóng postmortem 16/07** — đo message bằng `tools/toast-capture.js` (KHÔNG lọc trùng, đọc `innerText`, đếm số request kèm số toast). Đối chiếu message chuẩn dòng 888/955/956.

## 🔴 Phân loại Internal vs External TRƯỚC khi punt (protocol §GATE)
- **QLNDTVVCG_27 (thông báo CB phê duyệt)**: thông báo do **hành động nội bộ** (CG tích Hoàn thành) sinh ra → **INTERNAL**, PHẢI verify trên CMS (kiểm chuông thông báo/`list_network_requests` của CB PD sau khi CG hoàn thành). **CẤM** punt "external". SRS dòng 196 + 1508 + BR-NOTIF-01.
- **QLTLPLCVV_11 (xóa tư liệu công khai)**: SRS dòng 899 — thao tác **set cờ trên CSDL CMS** (nội bộ), Cổng PLQG tự pull. → INTERNAL, verify nút Xóa + xác nhận + set trạng thái trên CMS. KHÔNG cần chờ Cổng PLQG.

## Verdict wording — mẹo nhanh (theo protocol, KHÔNG thay bảng Verdict)
- Cột/trường/message SRS §Inputs/§Output/§Thành phần màn hình/§Error Handling quy định RÕ mà app sai (thiếu/thừa/sai định dạng/sai message) → thường **`Open`** (dẫn dòng cụ thể).
- App làm KHÁC nhưng SRS chỉ nêu chung / không quy định (field thiết kế thêm, default không nêu, confirm-dialog SRS silent, filename export không quy định) → **`BA confirm`**.
- Đối tác báo lỗi cụ thể mà verify **KHÔNG tái hiện** (web chạy đúng) → **`Reject`** + "→ Đối tác kiểm tra lại."
- **CẤM** kết luận từ SRS suông — mọi verdict phải kèm **artifact real-data** (ảnh full-res trường tranh chấp / toast+network của chính thao tác) chạy trên data đã seed (§GATE protocol). Bug workflow/state/permission/filter → **bắt buộc Bảng đối chiếu điều kiện** (`cond/<mã TC>.md`), chỉ chốt khi 0 GAP.

## Output — tất cả ghi vào FOLDER BUG TỔNG của round (không tạo folder riêng batch)
> Folder bug tổng = `output/UAT_doi-tac/reverify-week-3/bug-reports|cond|reverify-audit/` (dùng chung mọi module round 3; file đặt tên tiền tố `tvcs` + chữ batch → không clobber khi song song).

- **Verdict → Google Sheet NGAY** sau mỗi case (chạy từ thư mục `output/UAT_doi-tac/`):
  `python3 tools/sheet_write.py --mode verify1 --row N --ma-tc <MÃ> --status <Open|Reject|BA confirm|""> --evidence <path> --condition-table <file.md> --note-file <note.txt>`
  (bug tĩnh: thêm `--static-bug "<lý do ≥10 ký tự>"` thay `--condition-table`; ô TRỐNG: `--blocker-category A-F`).
- **Bug Open** → `reverify-week-3/bug-reports/bug-report-tvcs-batch{X}.md` (template `output/template/bug-report-template.md`, 6 sections; Bug ID = `BUG-<mã TC>`) + ≥1 screenshot `reverify-week-3/bug-reports/image/` (tên theo Bug ID).
- **BA confirm** → `reverify-week-3/ba-confirmation-needed-tvcs-batch{X}.md`.
- **Reject / BA confirm** → evidence audit vào `reverify-week-3/reverify-audit/<mã TC>/`.
- **Bảng đối chiếu điều kiện** (bug phụ thuộc role/state/data) → `reverify-week-3/cond/<mã TC>.md`. Bug tĩnh (label/cột cố định) → `--static-bug`, miễn bảng.
- **Cuối cùng (1 session, tuần tự):** merge 6 file `bug-report-tvcs-batch{X}.md` → `bug-reports/Pass-bug-report-tvcs.md`; merge BA → `ba-confirmation-needed-tvcs.md`.

## 🔴 Chạy song song được không?
- **A** (list, gần read-only trừ export/search) + **B** (mở form, không lưu/lưu record test riêng) + **C** (chi tiết read) → an toàn song song NẾU mỗi batch seed record tiền tố phân biệt (vd `TVCS-B{X}-<ngày>`) và không sửa record của batch khác.
- **D** (workflow) **thay đổi state thật** record (phân công/hoàn thành/hủy) → seed record RIÊNG, đừng đụng record batch khác. Chạy sau A/B/C an toàn hơn.
- **E·F** (tư liệu) thao tác trên tư liệu con của 1 TVCS → seed TVCS + tư liệu riêng. E gần read-only, F có sửa/xóa/upload → F seed riêng.
- An toàn nhất: chạy **tuần tự A→F**, hoặc song song A+B+C (đọc), rồi D, rồi E+F.

## Tài khoản dùng chung (login đúng vai trò bug = CB NV)
- **Chính: `cbnv_*` / `Test@1234`** (CB Nghiệp vụ) — chọn 1 đơn vị nhất quán, seed record trong đơn vị đó. Xem `output/UAT_doi-tac/input/input.md`.
- **Batch D** thêm: `qa_tvvseed28` (CG, Cục Bổ trợ tư pháp TW) + `cbpd_*` (CB Phê duyệt cùng đơn vị). ⚠️ Lưu ý data note trong input.md: sau case XNTGHTVV_03, một số VV DA_PHAN_CONG đã bị từ chối → cần phân công lại.
- Thiếu account/data/state tạo được mà không tạo → **CẤM** ghi verdict (§Nguyên tắc 4). Tạo xong ghi lại vào `input/input.md`.

## Môi trường
- Web: `https://18.143.165.120.nip.io/login` · MailHog: `http://18.143.165.120:8025/` (xem `input/input.md`).
- Tool QA mặc định: **Chrome DevTools MCP** (`mcp__chrome-devtools__*`).
- Lấy evidence đối tác: `python3 tools/fetch_evidence.py --row N` **TRƯỚC mỗi case** (đóng Cổng 1). Video → trích frame tới khoảnh khắc lỗi.
