# Kế hoạch verify module "Quản trị hệ thống" (Danh mục dùng chung + Tài khoản/Phân quyền/Cấu hình) — tuần 3

> **Vì sao chia batch:** module Quản trị hệ thống có **57 case** đối tác báo (rows **122–178**, tab `UAT_TGPL Doanh Nghiệp-tuần 3`).
> Chạy 57 case trong 1 session → vỡ context → chất lượng verify tụt (đúng bài học postmortem 16/07: "mù" khi chạy nhiều case một lúc).
> → Chia **9 batch** theo **cụm lỗi (pattern) + màn hình + tiền đề seed dùng chung** để mỗi session học 1 rule SRS, seed 1 lần, verify nhất quán nhiều case cùng bản chất.
> Mỗi batch **mở 1 cửa sổ Claude Code MỚI**, dán nguyên khối file `qtht/SESSION-qtht-batch{N}-prompt.md` tương ứng.
> **Chỉ có file prompt** nằm phẳng trong `qtht/`. **Bug + BA + cond + audit ghi vào FOLDER BUG TỔNG của round** (`reverify-week-3/bug-reports|cond|reverify-audit/`), đặt tên file theo batch (`bug-report-qtht-batch{N}.md`) để không đụng nhau khi chạy song song.

## SRS gốc của module
`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md` (Nhóm VIII — Quản trị Hệ thống, UC99–UC123).

🔴 **Điểm mấu chốt — SHARED TEMPLATE `TPL-DM-CRUD` (dòng 65–171).** 15 màn danh mục (FR-VIII-01…09, 11…13, 18, 19) dùng CHUNG 1 spec CRUD. Gần như mọi cụm lỗi danh mục quy về đúng 1 clause của template này:

| Clause template | Dòng SRS | Liên quan cụm lỗi |
|---|---|---|
| **Inputs chung** = `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường "Danh mục cha"** | 77–83 | Cụm "Danh mục cha thừa" (B1–B3) |
| `thu_tu` (Thứ tự) = **N — không bắt buộc**, default 0 | 82 | Required-field mismatch (B1 TTVV, B2 LDN/HSDNTT) |
| Sort mặc định: `thu_tu` tăng → `ten` tăng | 93 | Sắp xếp theo cột (B6) |
| Output ngày = **`dd/mm/yyyy HH:mm`** | 148 | Định dạng ngày yyyy-mm-dd (B1 CTHT) |
| `ERR-DM-03` = "Không thể xóa. Danh mục đang được sử dụng bởi {N} bản ghi {entity}" | 160 | Xóa tham chiếu → duplicate toast (B5) |
| SCR-VIII-01 §Quy tắc tương tác | 1607 | Xác nhận bỏ thay đổi chưa lưu (B4), click-to-sort (B6) |

Map sub-module (prefix mã TC) → FR / UC / màn hình SCR:

| Prefix | FR / UC | Chức năng | Màn hình SCR | Batch |
|---|---|---|---|:-:|
| QLDMLVPL | FR-VIII-01 / UC99 | DM lĩnh vực pháp lý | SCR-VIII-01 | 1·4·5·6 |
| QLDMLHHT | FR-VIII-02 / UC100 | DM loại hình hỗ trợ | SCR-VIII-01 | 1·4·5·6 |
| QLDMCTHT | FR-VIII-03 / UC101 | DM chương trình hỗ trợ | SCR-VIII-01 | 1·4 |
| QLDMTTVV | FR-VIII-04 / UC102 | DM tình trạng vụ việc | SCR-VIII-01 | 1·4 |
| QLDMCQDVQL | FR-VIII-05 / UC103 | DM cơ quan đơn vị QL (**Tree View**, dòng 1585) | SCR-VIII-01 | 4·5 |
| QLDMTCTV | FR-VIII-06 / UC104 | DM tổ chức tư vấn | SCR-VIII-01 | 5 |
| QLDMLDN | FR-VIII-07 / UC105 | DM loại doanh nghiệp | SCR-VIII-01 | 2·4·5 |
| QLDMHSDNHT | FR-VIII-08 / UC106 | DM hồ sơ đề nghị hỗ trợ | SCR-VIII-01 | 2·4 |
| QLDMHSDNTT | FR-VIII-09 / UC107 | DM hồ sơ đề nghị thanh toán | SCR-VIII-01 | 2·4 |
| QLCHTHXLHS | FR-VIII-10 / UC108 | Cấu hình SLA / thời hạn xử lý HS | **SCR-VIII-06** (Cấu hình HT, dòng 1723) | 7 |
| QLDMTCDGHQ | FR-VIII-11 / UC109 | DM tiêu chí ĐG hiệu quả (special, dòng 1594) | SCR-VIII-01 | 2·6 |
| QLDMTCDGHTCP | FR-VIII-12 / UC110 | DM tiêu chí ĐG hỗ trợ chi phí (special, dòng 1601) | SCR-VIII-01 | 3 |
| QLDMLTK | FR-VIII-13 / UC111 | Quản lý loại tài khoản | SCR-VIII-01 | 3 |
| QLVT | FR-VIII-14 / UC112 | Quản lý vai trò | **SCR-VIII-02** (dòng 1613) | 6 |
| QLTKND | FR-VIII-15 / UC113 | Quản lý tài khoản người dùng | **SCR-VIII-03** (dòng 1636) | 8 |
| QLPQTCDL | FR-VIII-16 / UC114 | Phân quyền truy cập dữ liệu | **SCR-VIII-05** (dòng 1705) | 9 |
| QLPQCN | FR-VIII-17 / UC115 | Phân quyền chức năng | **SCR-VIII-04** (dòng 1678) | 9 |
| QLLHTNHS | FR-VIII-18 / UC116 | DM loại hình tiếp nhận | SCR-VIII-01 | 3 |
| QLDMKTNHS | FR-VIII-19 / UC117 | DM kênh tiếp nhận | SCR-VIII-01 | 3 |

## 9 batch (tổng 57 case)

| Batch | Chủ đề / cụm lỗi | # | Mã TC (rows) | Màn hình / tiền đề seed chung | File prompt |
|:-:|---|:-:|---|---|---|
| **1** | DM — Form Thêm/Sửa: "Danh mục cha" thừa + ngày + Thứ tự bắt buộc — **nhóm A** | 8 | QLDMLVPL_09·16, QLDMLHHT_06·13, QLDMCTHT_06·13, QLDMTTVV_06·13 (r123,125,128,130,133,135,136,138) | Màn Danh mục (4 tab: LVPL/LHHT/CTHT/TTVV). Seed: ≥1 record mỗi tab | `SESSION-qtht-batch1-prompt.md` |
| **2** | DM — Form Thêm/Sửa: "Danh mục cha" + trường bắt buộc (Doanh thu, Thành phần HS) — **nhóm B** | 8 | QLDMLDN_06·13, QLDMHSDNHT_06·13, QLDMHSDNTT_06·13, QLDMTCDGHQ_06·12 (r142,144,146,148,149,151,157,158) | Màn Danh mục (4 tab: LDN/HSDNHT/HSDNTT/TCDGHQ) | `SESSION-qtht-batch2-prompt.md` |
| **3** | DM — Form Thêm/Sửa: "Danh mục cha" + tên trường — **nhóm C** | 8 | QLDMTCDGHTCP_06·12, QLDMLTK_06·12, QLLHTNHS_06·12, QLDMKTNHS_06·12 (r160,161,162,163,175,176,177,178) | Màn Danh mục (4 tab: TCDGHTCP/LTK/LHTNHS/KTNHS) | `SESSION-qtht-batch3-prompt.md` |
| **4** | DM — "Xác nhận bỏ thay đổi chưa lưu" không hiện (8 tab) | 8 | QLDMLVPL_14, QLDMLHHT_11, QLDMCTHT_11, QLDMTTVV_11, QLDMCQDVQL_12, QLDMLDN_11, QLDMHSDNHT_11, QLDMHSDNTT_11 (r124,129,134,137,140,143,147,150) | Màn Danh mục. Seed: ≥1 record mỗi tab để mở form sửa | `SESSION-qtht-batch4-prompt.md` |
| **5** | DM — List-level: xóa mục tham chiếu (duplicate toast) + empty-state + hiển thị 15 loại + thiếu tab "Tổ chức tư vấn" | 6 | QLDMLVPL_19, QLDMLHHT_16, QLDMLDN_16, QLDMCQDVQL_05, QLDMLVPL_02, QLDMTCTV_01 (r126,131,145,139,122,141) | Màn Danh mục. Seed: record **đang được tham chiếu** (không xóa được) cho 19/16 | `SESSION-qtht-batch5-prompt.md` |
| **6** | Sắp xếp theo cột + Phân trang (Danh mục + Vai trò) | 4 | QLDMLVPL_21, QLDMLHHT_18, QLDMTCDGHQ_17, QLVT_14 (r127,132,159,164) | Màn Danh mục + màn Vai trò. Seed: >20 record cho phân trang (TCDGHQ_17) | `SESSION-qtht-batch6-prompt.md` |
| **7** | Cấu hình xử lý hồ sơ / SLA (SCR-VIII-06) | 5 | QLCHTHXLHS_02·03·05·06·07 (r152–156) | Màn Cấu hình hệ thống (SLA). ⚠️ Spec churn nặng — bắt buộc 3-Step Verify version | `SESSION-qtht-batch7-prompt.md` |
| **8** | Tài khoản người dùng (SCR-VIII-03) | 7 | QLTKND_02·03·06·15·17·25·27 (r165–171) | Màn Quản lý tài khoản NSD. Seed: TK trùng tên/email (15/17), TK Đang hoạt động (27) | `SESSION-qtht-batch8-prompt.md` |
| **9** | Phân quyền dữ liệu + chức năng (SCR-VIII-04/05) | 3 | QLPQTCDL_06, QLPQCN_02, QLPQCN_03 (r172,173,174) | Màn Phân quyền (cây chức năng + ma trận). Seed: ≥1 vai trò có quyền | `SESSION-qtht-batch9-prompt.md` |

**Kích thước 8/8/8/8/6/4/5/7/3 — mỗi batch ≤8 case** → 1 session verify trọn không vỡ context.

## 🔴 Vai trò dùng verdict — dùng `admin` (QTHT) là ĐÚNG cho module này
Toàn bộ 57 case là chức năng **CHỈ QTHT truy cập** (TPL-DM-CRUD precondition dòng 72: "User có vai trò QTHT"). Không có case nào là bug phân quyền kiểu "role X làm/không làm được Y". → **Login `admin` / `Secret@123`** (vai trò QTHT — xem `input/input.md`) để verdict.
- Quy tắc protocol "admin không ra verdict" chỉ chặn **bug phân quyền** (quyền rộng che lỗi). Ở đây là bug hiển thị/validation/sort/form trên màn QTHT-độc-quyền → dùng QTHT là đúng vai trò của bug, KHÔNG vi phạm.
- Nếu phát sinh case cần role khác (không có trong danh sách này) → theo §Nguyên tắc 4 (tự tạo account, ghi vào `input/input.md`).

## 🔴 Cụm lỗi xuyên batch — verify chéo, nghi 1 bug gốc chung (đừng log rời)

1. **Cụm "Trường 'Danh mục cha' thừa trong popup Thêm/Sửa"** — **24 case xuyên B1·B2·B3** (mọi tab danh mục dạng phẳng). TPL-DM-CRUD Inputs (dòng 77–83) KHÔNG có trường cha. Nghi **1 bug FE gốc** (component form danh mục dùng chung render nhầm trường cha cho mọi loại).
   - ⚠️ **Ngoại lệ hợp lệ có cha:** DM Cơ quan đơn vị (UC103, Tree View dòng 1585) + DM Lĩnh vực kinh doanh (FR-VIII-31) **thực sự có** `danh_muc_cha_id`. Với các tab PHẲNG (LVPL, LHHT, CTHT, TTVV, LDN, HSDNHT, HSDNTT, TCDGHQ, TCDGHTCP, LTK, LHTNHS, KTNHS) → trường cha là **thừa so với SRS**.
   - **Verdict nuance (§Open vs BA confirm):** trường app **thêm** mà SRS Inputs không liệt kê + không phá validation → thiên về **`BA confirm`** (bổ sung thiết kế, để BA chốt có đưa vào spec không). Nếu trường cha **đánh dấu bắt buộc** hoặc chặn lưu record hợp lệ → **`Open`** (phá luồng). Mở đúng dòng SRS + chụp full-res trường tranh chấp trước khi chốt.
   - Verify KỸ 1–2 tab đại diện, các tab còn lại tham chiếu nhưng **vẫn chụp ảnh + ghi verdict riêng từng case** (GATE real-data).

2. **Cụm "Xác nhận bỏ thay đổi chưa lưu" không hiện** — **8 case B4**. Nghi **1 bug** (form không cảnh báo khi đóng). SCR-VIII-01 §Quy tắc tương tác (dòng 1607): nếu SRS **có** quy định dialog này → `Open`; SRS **silent** → `BA confirm` (đối tác kỳ vọng, SRS không nêu). Mở dòng 1607 xác nhận TRƯỚC khi chốt cả 8 case.

3. **Cụm "Xóa mục tham chiếu → toast duplicate"** — **B5** (LVPL_19, LHHT_16, LDN_16) + validation duplicate **B8** (QLTKND_15/17). ⚠️ **Vùng nóng postmortem 16/07.** BẮT BUỘC đo bằng `tools/toast-capture.js` (KHÔNG lọc trùng, đọc `innerText`, **đếm số request song song số khung toast**). `1 request + 2 toast` = lỗi FE hiển thị; đừng kết luận từ observer tự viết. Nội dung message đối chiếu `ERR-DM-03` (dòng 160).

4. **Cụm "Sắp xếp theo cột không chạy"** — **B6** (LVPL_21, LHHT_18, QLVT_14) + **B8** (QLTKND_25). Nghi **1 bug** (click header không sort). Template dòng 93 (sort mặc định) + SCR §Quy tắc tương tác (click-to-sort). Cross-ref B6↔B8.

5. **Cụm "Empty-state hiện 'Trống' thay vì message ngữ cảnh"** — **B5** (CQDVQL_05: thiếu "Không tìm thấy mục danh mục phù hợp") + **B8** (QLTKND_06: hiện "Trống" thay vì "Không tìm thấy tài khoản phù hợp"). Nghi **1 component empty-state dùng chung**. Cross-ref B5↔B8. Lưu ý phân loại tab trống (CLAUDE.md §"tab trống"): "Trống" = empty-state hợp lệ **hay** thiếu message chuẩn? → so SRS + chụp ảnh.

6. **Cụm "Trường bắt buộc sai"** — **B1** (TTVV_06: Thứ tự), **B2** (LDN_06/13: Doanh thu; HSDNTT_06/13: Thành phần HS). Template dòng 82: `thu_tu` = N. Doanh thu/Thành phần → mở FR riêng của tab đó (FR-VIII-07 dòng 389 / FR-VIII-09 dòng 429) xác nhận "N" trước khi chốt `Open`.

## Verdict wording — mẹo nhanh (theo protocol, KHÔNG thay bảng Verdict)
- Trường/cột SRS §Inputs/§Thành phần màn hình quy định RÕ mà app sai (thiếu/thừa/sai định dạng/sai bắt buộc) → thường **`Open`** (dẫn line template hoặc FR/SCR).
- App làm KHÁC nhưng SRS chỉ nêu chung / không quy định (message empty-state, dialog xác nhận SRS silent, trường thiết kế thêm) → **`BA confirm`**.
- Đối tác báo lỗi cụ thể mà verify **KHÔNG tái hiện** (web chạy đúng) → **`Reject`** + "→ Đối tác kiểm tra lại."
- **CẤM** kết luận từ SRS suông — mọi verdict phải kèm **artifact real-data** (ảnh full-res trường tranh chấp / toast+network của chính thao tác) chạy trên data đã seed (§GATE protocol).

## Output — tất cả ghi vào FOLDER BUG TỔNG của round (không tạo folder riêng batch)
> Folder bug tổng = `output/UAT_doi-tac/reverify-week-3/bug-reports|cond|reverify-audit/` (dùng chung mọi module round 3; file đặt tên có tiền tố `qtht` + số batch → không clobber khi song song).

- **Verdict → Google Sheet NGAY** sau mỗi case:
  `python3 tools/sheet_write.py --mode verify1 --row N --ma-tc <MÃ> --status <Open|Reject|BA confirm|""> --evidence <path> --condition-table <file.md> --note-file <note.txt>`
  (bug tĩnh: thêm `--static-bug "<lý do ≥10 ký tự>"`; ô TRỐNG: `--blocker-category A-F`). Lệnh chạy từ thư mục `output/UAT_doi-tac/`.
- **Bug Open** → `output/UAT_doi-tac/reverify-week-3/bug-reports/bug-report-qtht-batch{N}.md` (template `output/template/bug-report-template.md`, 6 sections; Bug ID = `BUG-<mã TC>`) + ≥1 screenshot `output/UAT_doi-tac/reverify-week-3/bug-reports/image/` (tên theo Bug ID).
- **BA confirm** → `output/UAT_doi-tac/reverify-week-3/ba-confirmation-needed-qtht-batch{N}.md`.
- **Reject / BA confirm** → evidence audit vào `output/UAT_doi-tac/reverify-week-3/reverify-audit/<mã TC>/`.
- **Bảng đối chiếu điều kiện** từng case (bug phụ thuộc role/state/data) → `output/UAT_doi-tac/reverify-week-3/cond/<mã TC>.md`. Bug tĩnh (typo/label/cột cố định) không cần bảng — dùng `--static-bug`.
- **Cuối cùng (1 session, tuần tự):** merge 9 file `bug-report-qtht-batch{N}.md` → `bug-reports/bug-report-qtht.md`; merge BA → `ba-confirmation-needed-qtht.md`.

## 🔴 Chạy song song được không?
- **B1·B2·B3·B4** đều thao tác trên **màn Danh mục** nhưng khác **tab** → an toàn chạy song song NẾU mỗi batch chỉ seed/sửa record trong **tab của mình** + đặt tiền tố tên phân biệt (vd `QTHT-B1-<ngày>`). B4 chỉ mở form sửa rồi đóng (không lưu) → gần như read-only, an toàn.
- **B5** có thao tác **xóa** (dù bị chặn) + cần record **đang tham chiếu** → seed record riêng, đừng đụng record batch khác.
- **B6** click sort/phân trang = read-only → an toàn song song bất kỳ lúc nào.
- **B7·B8·B9** ở **màn khác nhau** (Cấu hình / Tài khoản / Phân quyền) → độc lập hoàn toàn, song song thoải mái.
- An toàn nhất: chạy **tuần tự B1→B9**, hoặc song song 2–3 batch khác màn/khác tab.

## Tài khoản dùng chung (login đúng vai trò bug = QTHT)
- **Chính: `admin` / `Secret@123`** (vai trò QTHT) — xem `output/UAT_doi-tac/input/input.md`.
- Thiếu account/data/state tạo được mà không tạo → **CẤM** ghi verdict (§Nguyên tắc 4). Tạo xong ghi lại vào `input/input.md`.

## Môi trường
- Web: `https://18.143.165.120.nip.io/login` · MailHog: `http://18.143.165.120:8025/` (xem `input/input.md`).
- Tool QA mặc định: **Chrome DevTools MCP** (`mcp__chrome-devtools__*`).
