# BA confirmation needed — QTHT Batch 1 (Form Thêm/Sửa danh mục nhóm A) — 2026-07-21

> **File này để làm gì:** gom các testcase QTHT Batch 1 mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh.
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md` — mẫu dùng chung **TPL-DM-CRUD** (dòng 65–171), các FR riêng FR-VIII-01…04.
> **Verify:** 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin` (vai trò QTHT — đúng vai trò của chức năng QTHT-độc-quyền). Env `https://18.143.165.120.nip.io`.

---

## Cụm gốc chung — "Danh mục cha" thừa trong form Thêm/Sửa (8/8 case Batch 1)

Cả 8 case Batch 1 đều tái hiện: form Thêm mới / Sửa danh mục của 4 tab **phẳng** (Lĩnh vực pháp lý, Loại hình hỗ trợ, Chương trình hỗ trợ, Tình trạng vụ việc) đều render thêm trường **"Danh mục cha"** (combobox, placeholder "Chọn danh mục cha (tùy chọn)"). Trường này **không bắt buộc** (không có dấu `*`), **để trống vẫn lưu được**, không phá luồng nhập.

- Mẫu **TPL-DM-CRUD §Inputs chung** (dòng 77–83) chỉ liệt kê: `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có "Danh mục cha"**.
- Các FR riêng của 4 tab này (FR-VIII-01 dòng 188–195, FR-VIII-02 dòng 229–235, FR-VIII-03 dòng 252–261, FR-VIII-04 dòng 278–286) **cũng không** có `danh_muc_cha_id` — đây là danh mục phẳng.
- ⚠️ Ngoại lệ có cha hợp lệ (KHÔNG thuộc batch này): DM Cơ quan đơn vị (UC103, Tree View, dòng 300) + DM Lĩnh vực kinh doanh — 2 loại này thật sự có cấp cha.
- Nghi **1 bug FE gốc chung**: component form danh mục dùng chung render trường cha cho MỌI loại, kể cả loại phẳng.

**Vì sao BA confirm (không tự Open):** trường app **thêm** mà SRS §Inputs không liệt kê + **không** đánh dấu bắt buộc + **không** chặn lưu record hợp lệ → thuộc diện "bổ sung thiết kế", để BA chốt có đưa vào spec / hay yêu cầu ẩn. (Nếu trường cha bị đánh bắt buộc hoặc chặn lưu → sẽ là `Open`; thực tế verify không phải vậy.)

**Câu hỏi BA (chung cả cụm):** Với các danh mục **phẳng** (không phân cấp), có:
1. **Bổ sung** trường "Danh mục cha" vào đặc tả TPL-DM-CRUD (chấp nhận UI hiện tại), hay
2. **Yêu cầu ẩn** trường "Danh mục cha" ở các loại phẳng (chỉ hiện cho DM có cấp cha thật)?

> ⚠️ **Bổ sung quan trọng (ngoài phản ánh đối tác):** trường "Danh mục cha" KHÔNG chỉ hiển thị thừa — dropdown của nó **có dữ liệu**: khi mở ở tab Tình trạng vụ việc, nó liệt kê **chính các record cùng loại** (Mới tạo, Chờ tiếp nhận, Đã tiếp nhận, Đang kiểm tra, Yêu cầu bổ sung, Đã phân công, Đang xử lý, Chờ phê duyệt, Đã duyệt…) làm "cha" chọn được. Tức là user CÓ THỂ gán 1 record danh mục phẳng làm con của record khác cùng loại → tạo phân cấp trong mô hình SRS quy định là **phẳng** (không `danh_muc_cha_id`). Đây là rủi ro toàn vẹn dữ liệu, không chỉ lỗi hiển thị → nghiêng về **ẩn trường** (phương án 2). Evidence: `../../reverify-audit/QLDMTTVV_13/QLDMTTVV_13-danhmuccha-dropdown-empty.png`. (Chưa test lưu thực tế để xác nhận BE có persist `danh_muc_cha_id` hay không — đề nghị Dev/BA kiểm tra thêm.)

---

## QLDMLVPL_09 (row 123) — Lĩnh vực pháp lý · Thêm mới · "Danh mục cha" thừa

**Bối cảnh testcase**

- Dòng Excel: 123, mã TC `QLDMLVPL_09`.
- Nội dung kiểm tra: QTHT mở form **Thêm mới** danh mục tab "Lĩnh vực pháp lý".
- Actual đối tác ghi: popup Thêm mới có trường "Danh mục cha" nhưng SRS không có.

**Đối chiếu SRS v3.5**

- FR-VIII-01 (UC99) dùng mẫu TPL-DM-CRUD. §Inputs chung (dòng 77–83) = `ma, ten, mo_ta, thu_tu, trang_thai`, không có "Danh mục cha".
- FR-VIII-01 §Inputs trường riêng (dòng 190–195) chỉ thêm `loai_danh_muc` = 'LINH_VUC_PL' (system), không có `danh_muc_cha_id`.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:190-195`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin`/QTHT.
- URL `https://18.143.165.120.nip.io/quan-tri/danh-muc/LINH_VUC_PL` → nút "Thêm mới".
- Form hiển thị: `* Mã`, `* Tên`, `Mô tả`, `Thứ tự` (=0, không bắt buộc), **`Danh mục cha` — "Chọn danh mục cha (tùy chọn)"** (không bắt buộc), `Trạng thái` (Kích hoạt/Vô hiệu hóa).
- Bỏ trống "Danh mục cha" vẫn cho lưu → không chặn luồng.
- Evidence: `../../reverify-audit/QLDMLVPL_09/QLDMLVPL_09-add-form.png`

**Kết luận QA**

- `QLDMLVPL_09`: đối tác quan sát **đúng thực tế** (trường "Danh mục cha" có trong form) — không phải Reject.
- Web thừa trường so với SRS §Inputs, nhưng trường optional + không chặn lưu → QA không tự Open, cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận hướng: bổ sung "Danh mục cha" vào đặc tả danh mục phẳng, hay yêu cầu Dev FE ẩn trường này ở các loại phẳng.
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chọn ẩn trường → owner `Dev FE` (gốc chung, tái hiện toàn bộ 4 tab batch này + nghi B2/B3).

---

## QLDMLVPL_16 (row 125) — Lĩnh vực pháp lý · Sửa · "Danh mục cha" thừa

**Bối cảnh testcase**

- Dòng Excel: 125, mã TC `QLDMLVPL_16`.
- Nội dung kiểm tra: QTHT mở form **Sửa** danh mục tab "Lĩnh vực pháp lý".
- Actual đối tác ghi: popup sửa có trường "Danh mục cha" nhưng SRS không có (evidence sửa record "Khác").

**Đối chiếu SRS v3.5** — như cụm gốc chung ở trên (FR-VIII-01 dùng TPL-DM-CRUD, §Inputs dòng 77–83 không có "Danh mục cha").

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:190-195`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, mở form Sửa record `THUE` tại `.../danh-muc/LINH_VUC_PL`.
- Form "Chỉnh sửa danh mục" hiển thị: `* Mã`=THUE, `* Tên`=Thuế, `Mô tả`, `Thứ tự`=1, **`Danh mục cha` — "Chọn danh mục cha (tùy chọn)"** (trống, không bắt buộc), `Trạng thái`.
- Evidence: `../../reverify-audit/QLDMLVPL_16/QLDMLVPL_16-edit-form.png`

**Kết luận QA**

- `QLDMLVPL_16`: đối tác quan sát đúng thực tế; web thừa trường so SRS nhưng optional + không chặn lưu → cần BA quyết (giống QLDMLVPL_09).

**Nội dung đề xuất BA phản hồi đối tác** — như câu hỏi chung cụm gốc. Verdict QA đề xuất: `Cần BA xác nhận`.

---

## QLDMLHHT_06 (row 128) — Loại hình hỗ trợ · Thêm mới · "Danh mục cha" thừa

**Bối cảnh testcase**

- Dòng Excel: 128, mã TC `QLDMLHHT_06`. QTHT mở form **Thêm mới** danh mục tab "Loại hình hỗ trợ".
- Actual đối tác ghi: popup thêm mới có trường "Danh mục cha" nhưng SRS không có.

**Đối chiếu SRS v3.5** — FR-VIII-02 (UC100) dùng TPL-DM-CRUD, §Inputs dòng 77–83 không có "Danh mục cha"; §Inputs trường riêng (dòng 231–235) chỉ thêm `loai_danh_muc`.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:231-235`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, `.../danh-muc/LOAI_HINH_HO_TRO` → "Thêm mới".
- Form hiển thị `* Mã`, `* Tên`, `Mô tả`, `Thứ tự`=0, **`Danh mục cha` — "Chọn danh mục cha (tùy chọn)"** (không bắt buộc), `Trạng thái`. Bỏ trống vẫn lưu.
- Evidence: `../../reverify-audit/QLDMLHHT_06/QLDMLHHT_06-add-form.png`

**Kết luận QA** — đối tác quan sát đúng; trường thừa vs SRS nhưng optional + không chặn lưu → `Cần BA xác nhận` (cùng cụm gốc, cùng câu hỏi BA).

---

## QLDMLHHT_13 (row 130) — Loại hình hỗ trợ · Sửa · "Danh mục cha" thừa

**Bối cảnh testcase**

- Dòng Excel: 130, mã TC `QLDMLHHT_13`. QTHT mở form **Sửa** danh mục tab "Loại hình hỗ trợ".
- Actual đối tác ghi: popup sửa có trường "Danh mục cha" nhưng SRS không có (evidence sửa record "TKM test").

**Đối chiếu SRS v3.5** — FR-VIII-02 (UC100) dùng TPL-DM-CRUD, §Inputs dòng 77–83 không có "Danh mục cha".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:231-235`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, mở form Sửa record `TU_VAN` tại `.../danh-muc/LOAI_HINH_HO_TRO`.
- Form "Chỉnh sửa danh mục" hiển thị `* Mã`=TU_VAN, `* Tên`=Tư vấn pháp luật, `Mô tả`, `Thứ tự`=1, **`Danh mục cha` — "Chọn danh mục cha (tùy chọn)"** (trống, không bắt buộc), `Trạng thái`.
- Evidence: `../../reverify-audit/QLDMLHHT_13/QLDMLHHT_13-edit-form.png`

**Kết luận QA** — đối tác quan sát đúng; trường thừa vs SRS nhưng optional + không chặn lưu → `Cần BA xác nhận` (cùng cụm gốc).

---

## QLDMCTHT_06 (row 133) — Chương trình hỗ trợ · Thêm mới · "Danh mục cha" thừa + định dạng ngày yyyy-mm-dd (gộp 2 ý)

**Bối cảnh testcase**

- Dòng Excel: 133, mã TC `QLDMCTHT_06`. QTHT mở form **Thêm mới** danh mục tab "Chương trình hỗ trợ".
- Actual đối tác ghi: (1) popup có trường "Danh mục cha" thừa; (2) ô ngày hiển thị `yyyy-mm-dd` (SRS yêu cầu `dd/mm/yyyy`).

**Đối chiếu SRS v3.5**

- **Ý 1 (Danh mục cha):** FR-VIII-03 (UC101) dùng TPL-DM-CRUD §Inputs (dòng 77–83) không có "Danh mục cha"; §Inputs trường riêng (dòng 254–261) chỉ thêm `thoi_gian_bat_dau/ket_thuc`, `don_vi_chu_tri`, `loai_danh_muc` — không có `danh_muc_cha_id`.
- **Ý 2 (định dạng ngày):** §Outputs TPL-DM-CRUD (dòng 148) quy định datetime `dd/mm/yyyy HH:mm` (cho `created_at/updated_at`). §Inputs FR-VIII-03 (dòng 258–259) chỉ ghi kiểu `date`, **không nêu rõ định dạng của ô nhập**. Danh sách CTHT KHÔNG hiển thị cột ngày nào → dòng 148 (output) không áp trực tiếp cho ô nhập tranh chấp.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:254-261`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:148`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, `.../danh-muc/CHUONG_TRINH_HT` → "Thêm mới".
- Form hiển thị: `* Mã`, `* Tên`, `Mô tả`, `Thứ tự`=0, **`Danh mục cha` (tùy chọn)**, `Trạng thái`, **`* Thời gian bắt đầu` placeholder "YYYY-MM-DD"**, **`Thời gian kết thúc` placeholder "YYYY-MM-DD (tùy chọn — chương trình open-ended)"**, `* Đơn vị chủ trì`.
- DOM inspect: placeholder ô ngày = `YYYY-MM-DD` (xác nhận định dạng ISO). Danh sách CTHT chỉ 6 cột (Mã/Tên/Mô tả/Thứ tự/Trạng thái/Hành động), không cột ngày.
- Evidence: `../../reverify-audit/QLDMCTHT_06/QLDMCTHT_06-add-form-dates.png`

**Kết luận QA**

- **Ý 1:** đối tác đúng thực tế; trường thừa nhưng optional + không chặn lưu → `Cần BA xác nhận` (cùng cụm gốc).
- **Ý 2:** đối tác đúng thực tế (ô ngày là `yyyy-mm-dd`). SRS quy định `dd/mm/yyyy` cho ngày/giờ output (dòng 148) nhưng silent về định dạng ô **nhập** → QA không tự Open. Đây là **bug candidate về định dạng** cần BA chốt chuẩn.
- Verdict tổng: `Cần BA xác nhận` (case vừa là bug định dạng ngày vừa cần BA chốt spec → ghi sheet `BA confirm`).

**Nội dung đề xuất BA phản hồi đối tác**

- (a) Bổ sung/ẩn "Danh mục cha" cho danh mục phẳng?
- (b) Chuẩn hoá ô nhập ngày về `dd/mm/yyyy` cho đồng bộ định dạng ngày hệ thống (dòng 148)? Nếu BA chốt `dd/mm/yyyy` → owner `Dev FE` sửa định dạng ô ngày (áp cả QLDMCTHT_13).

---

## QLDMCTHT_13 (row 135) — Chương trình hỗ trợ · Sửa · "Danh mục cha" thừa + định dạng ngày yyyy-mm-dd (gộp 2 ý)

**Bối cảnh testcase**

- Dòng Excel: 135, mã TC `QLDMCTHT_13`. QTHT mở form **Sửa** danh mục tab "Chương trình hỗ trợ".
- Actual đối tác ghi: (1) "Danh mục cha" thừa; (2) ô ngày dạng `yyyy-mm-dd` (evidence: record "TKM test", ngày `2026-07-13`/`2026-07-14`).

**Đối chiếu SRS v3.5** — như QLDMCTHT_06: FR-VIII-03 (UC101) §Inputs không có "Danh mục cha" (dòng 77–83); định dạng ngày output dd/mm/yyyy (dòng 148), input SRS silent (dòng 258–259).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:254-261`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:148`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, mở form Sửa record `CT_NGUOI_NGHEO` tại `.../danh-muc/CHUONG_TRINH_HT`.
- Form "Chỉnh sửa danh mục" hiển thị: `* Mã`=CT_NGUOI_NGHEO, `* Tên`, `Mô tả`, `Thứ tự`=1, **`Danh mục cha` (tùy chọn, trống)**, `Trạng thái`, **`* Thời gian bắt đầu` = "2020-01-01"** (giá trị thực dạng yyyy-mm-dd), `Thời gian kết thúc` (placeholder "YYYY-MM-DD"), `* Đơn vị chủ trì`="Cục Bổ trợ tư pháp".
- Evidence: `../../reverify-audit/QLDMCTHT_13/QLDMCTHT_13-edit-form-dates.png`

**Kết luận QA**

- **Ý 1:** đối tác đúng; trường optional + không chặn lưu → `Cần BA xác nhận`.
- **Ý 2:** đối tác đúng (giá trị ngày render `yyyy-mm-dd`). SRS silent về format ô nhập → `Cần BA xác nhận` (bug candidate định dạng, chờ BA chốt chuẩn).
- Verdict tổng: `Cần BA xác nhận` → ghi sheet `BA confirm`.

**Nội dung đề xuất BA phản hồi đối tác** — như QLDMCTHT_06 (áp chung 2 case CTHT). Nếu BA chốt `dd/mm/yyyy` → `Dev FE` sửa định dạng ô ngày.

---

## QLDMTTVV_06 (row 136) — Tình trạng vụ việc · Thêm mới · "Danh mục cha" thừa + "Thứ tự" bắt buộc (gộp 2 ý; ý 2 là SRS TỰ MÂU THUẪN)

**Bối cảnh testcase**

- Dòng Excel: 136, mã TC `QLDMTTVV_06`. QTHT mở form **Thêm mới** danh mục tab "Tình trạng vụ việc".
- Actual đối tác ghi: (1) "Danh mục cha" thừa; (2) trường "Thứ tự" bị đánh dấu **bắt buộc** (đối tác cho rằng SRS: không bắt buộc).

**Ý 1 (Danh mục cha) — Dạng A: QA đã kết luận**

- FR-VIII-04 (UC102) dùng TPL-DM-CRUD §Inputs (dòng 77–83) không có "Danh mục cha".
- Web: form có trường "Danh mục cha" (tùy chọn, không chặn lưu) → thừa vs SRS nhưng optional → `Cần BA xác nhận` (cùng cụm gốc).

**Ý 2 (Thứ tự bắt buộc) — Dạng B: SRS tự mâu thuẫn**

Điểm mâu thuẫn trong SRS v3.5:

1. Mẫu chung **TPL-DM-CRUD §Inputs** (dòng 82): `thu_tu` = **N (không bắt buộc)**, default 0.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:82`
2. Nhưng **FR-VIII-04 §Inputs trường riêng** (dòng 284): `thu_tu` = **Y (bắt buộc)** — "Thứ tự hiển thị trong workflow".
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:284`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, `.../danh-muc/TINH_TRANG_VU_VIEC` → "Thêm mới".
- Form hiển thị: `* Mã`, `* Tên`, `Mô tả`, **`* Thứ tự`** (có dấu `*` = **bắt buộc**, spinbutton min=1), **`Danh mục cha` (tùy chọn)**, `Trạng thái`, `Màu hiển thị` (ColorWell — khớp `mau_hien_thi` dòng 285).
- Web đang theo **FR-VIII-04 (bắt buộc)**, KHÔNG theo mẫu chung dòng 82.
- Evidence: `../../reverify-audit/QLDMTTVV_06/QLDMTTVV_06-add-form.png`

**Câu hỏi cần BA xác nhận**

Ô "Thứ tự" của Tình trạng vụ việc cần hiểu theo hướng nào?
1. **Theo FR-VIII-04 (dòng 284):** bắt buộc — UI hiện tại ĐÚNG (thứ tự quan trọng cho workflow trạng thái). → cập nhật mẫu chung dòng 82 cho khớp / ghi chú ngoại lệ.
2. **Theo mẫu chung TPL-DM-CRUD (dòng 82):** không bắt buộc — UI hiện tại cần bỏ dấu `*`. → sửa FR-VIII-04.

**Đề xuất QA tạm thời**

- Chưa gửi bug cho Dev tới khi BA chốt nguồn chuẩn (dòng 82 vs 284).
- Tạm verdict cả case: `Cần BA xác nhận` (ghi sheet `BA confirm`).
- ⚠️ **Lưu ý cho BA:** prompt/kỳ vọng đối tác chỉ dẫn mẫu chung dòng 82 (không bắt buộc), bỏ sót override FR-VIII-04 dòng 284 (bắt buộc). QA đã đối chiếu cả 2 dòng — đây KHÔNG phải bug đơn thuần mà là mâu thuẫn spec.

---

## QLDMTTVV_13 (row 138) — Tình trạng vụ việc · Sửa · "Danh mục cha" thừa

**Bối cảnh testcase**

- Dòng Excel: 138, mã TC `QLDMTTVV_13`. QTHT mở form **Sửa** danh mục tab "Tình trạng vụ việc".
- Actual đối tác ghi: popup sửa có trường "Danh mục cha" nhưng SRS không có (evidence sửa record "TKM test").

**Đối chiếu SRS v3.5** — FR-VIII-04 (UC102) dùng TPL-DM-CRUD, §Inputs dòng 77–83 không có "Danh mục cha".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:278-286`

**Kết quả verify UI hiện tại**

- Verify 2026-07-21, `admin`/QTHT, mở form Sửa record `MOI_TAO` tại `.../danh-muc/TINH_TRANG_VU_VIEC`.
- Form "Chỉnh sửa danh mục" hiển thị: `* Mã`=MOI_TAO, `* Tên`=Mới tạo, `Mô tả`, `* Thứ tự`=1 (bắt buộc), **`Danh mục cha` — "Chọn danh mục cha (tùy chọn)"** (trống, không bắt buộc), `Trạng thái`, `Màu hiển thị`.
- Evidence: `../../reverify-audit/QLDMTTVV_13/QLDMTTVV_13-edit-form.png`

**Kết luận QA** — đối tác quan sát đúng; trường "Danh mục cha" thừa vs SRS nhưng optional + không chặn lưu → `Cần BA xác nhận` (cùng cụm gốc).
- Ghi chú: form Sửa TTVV cũng đánh dấu `* Thứ tự` bắt buộc (giống QLDMTTVV_06) — mâu thuẫn dòng 82 vs 284 đã nêu ở mục QLDMTTVV_06, KHÔNG lặp verdict.

---
