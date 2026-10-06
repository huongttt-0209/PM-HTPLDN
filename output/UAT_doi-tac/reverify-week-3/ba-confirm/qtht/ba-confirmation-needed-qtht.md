# BA confirmation needed — Quản trị hệ thống — 2026-07-21

> File tổng hợp các nội dung QA cần BA xác nhận sau khi reverify UAT đối tác tuần 3. Nội dung phân tích, citation và evidence của từng testcase được giữ nguyên từ các báo cáo nguồn.

---

## Tổng hợp nhanh

Có **43 testcase** cần BA xác nhận, quy về các nhóm quyết định chính dưới đây:

| Nhóm cần BA chốt | Số TC | Nội dung quyết định |
|---|---:|---|
| Form danh mục dùng chung | 24 | “Danh mục cha” trên danh mục phẳng; định dạng ngày; bắt buộc “Thứ tự”; thành phần hồ sơ; tên trường chi phí |
| Cảnh báo mất thay đổi chưa lưu | 8 | Có bổ sung dirty-check và hộp thoại xác nhận khi đóng form danh mục hay không |
| Empty-state khi tìm kiếm không có kết quả | 2 | Chuẩn hóa thông báo ngữ cảnh hay giữ component rỗng mặc định |
| Sắp xếp bằng tiêu đề cột | 2 | Áp dụng click-sort cho màn Vai trò và Tài khoản hay chỉ cho màn được SRS chỉ định |
| Cấu hình hệ thống / SLA | 4 | Số tab, cấu trúc bảng, inline-edit hay modal-edit |
| Đặt lại mật khẩu | 1 | Giữ quyết định bỏ nút theo STT80 hay khôi phục cho quản trị viên |
| Phân quyền chức năng | 2 | Dùng ma trận 6 cột cũ hay bản redesign panel theo module |

> Các mục bên dưới giữ nguyên kết quả verify, đối chiếu SRS, citation, kết luận QA và nội dung đề xuất BA phản hồi đối tác.

---

<!-- group-1-start -->
## Form Thêm/Sửa danh mục nhóm A

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
<!-- group-1-end -->

---

<!-- group-2-start -->
## Form Thêm/Sửa danh mục nhóm B

> Gom các testcase QTHT Batch 2 (rows 142–158) cần BA phản hồi lại đối tác. Tool verify: Chrome DevTools MCP, tài khoản `admin` (vai trò QTHT), env `https://18.143.165.120.nip.io`. SRS: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md`.
>
> **Kết luận nhanh:** cả 8 case đều verdict `BA confirm`. Cụm gốc chung = trường **"Danh mục cha"** thừa trong form của mọi tab danh mục phẳng (nghi 1 bug FE component dùng chung). Riêng HSDNTT có thêm ràng buộc **"Thành phần hồ sơ bắt buộc ≥1"** trái SRS. Ý "Tiêu chí doanh thu bắt buộc" (LDN) đã KHÔNG còn tái hiện.

---

## Cụm 1 — Trường "Danh mục cha" thừa trong form Thêm/Sửa (8 case: 142·144·146·148·149·151·157·158)

**Bối cảnh testcase**

- Đối tác phản ánh: form Thêm/Sửa các tab danh mục phẳng (Loại doanh nghiệp, Hồ sơ đề nghị hỗ trợ, Hồ sơ đề nghị thanh toán, Tiêu chí đánh giá hiệu quả) hiển thị thừa trường **"Danh mục cha"**.
- Vai trò kiểm tra: QTHT (đúng vai trò — TPL-DM-CRUD precondition dòng 72: "User có vai trò QTHT").

**Đối chiếu SRS v3.5**

- SHARED TEMPLATE **TPL-DM-CRUD** §Inputs chung (dòng 77–83) chỉ có 5 trường: `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường "Danh mục cha"** (`danh_muc_cha_id`).
- Màn **SCR-VIII-01** §Thành phần màn hình (dòng 1578–1583): modal CRUD gồm Mã / Tên / Mô tả / Thứ tự / Trạng thái / Hủy-Lưu — **không liệt kê "Danh mục cha"**.
- Trường "Đơn vị cha" (danh mục cha) CHỈ tồn tại hợp lệ ở **DM Cơ quan Đơn vị (UC103, Tree View, dòng 1585–1590)** — không áp cho các tab phẳng đang xét.
- Các FR riêng của 4 tab đều dùng TPL-DM-CRUD + trường riêng, KHÔNG khai báo "Danh mục cha": FR-VIII-07/LDN (dòng 389), FR-VIII-08/HSDNHT (dòng 410), FR-VIII-09/HSDNTT (dòng 429), FR-VIII-11/TCDGHQ (dòng 531).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83` (Inputs chung TPL-DM-CRUD)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1578-1583` (SCR-VIII-01 modal)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1585-1590` (Tree View DM Cơ quan ĐV — trường hợp DUY NHẤT có cha)

**Kết quả verify UI hiện tại (21/07/2026, Chrome DevTools MCP, tài khoản `admin`/QTHT)**

- Cả 4 tab, cả form Thêm mới lẫn Sửa: trường **"Danh mục cha"** đều hiển thị, placeholder "Chọn danh mục cha (tùy chọn)".
- Trường ở dạng **tùy chọn** (không có dấu `*`, `reqClass=false`, CSS `::before` = none). Lưu bản ghi KHÔNG chọn cha vẫn thành công (đã test POST tạo record Loại DN không cha → toast "Thêm mới thành công").
- Evidence: `../../reverify-audit/QLDMLDN_06/web-them-moi-form.png`, `QLDMLDN_13/web-sua-form.png`, `QLDMHSDNHT_06/web-them-moi-form.png`, `QLDMHSDNHT_13/web-sua-form.png`, `QLDMHSDNTT_06/web-luu-thanh-phan-trong.png`, `QLDMHSDNTT_13/web-sua-form.png`, `QLDMTCDGHQ_06/web-them-moi-form.png`, `QLDMTCDGHQ_12/web-sua-form.png`.

**Kết luận QA**

- Trường "Danh mục cha" là **thiết kế thêm ngoài đặc tả** cho các danh mục phẳng: SRS Inputs (dòng 77–83) và SCR-VIII-01 (dòng 1578–1583) không liệt kê.
- Trường ở dạng tùy chọn, KHÔNG chặn luồng lưu hợp lệ → không phải lỗi phá validation, nên để **BA chốt đặc tả** thay vì đẩy dev sửa ngay.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận 1 trong 2 hướng cho các danh mục **phẳng** (LDN, HSDNHT, HSDNTT, TCDGHQ — và các tab phẳng khác cùng component: LVPL, LHHT, CTHT, TTVV...):
  1. **Bổ sung "Danh mục cha" vào đặc tả** (nếu nghiệp vụ muốn hỗ trợ phân cấp cho các danh mục này) — cập nhật TPL-DM-CRUD Inputs;
  2. **Ẩn/bỏ trường "Danh mục cha"** khỏi form các tab phẳng, chỉ giữ cho DM Cơ quan Đơn vị (UC103) — để khớp SRS hiện hành.
- Verdict QA đề xuất: `BA confirm` (bổ sung/điều chỉnh đặc tả — chưa gửi Dev tới khi BA chốt hướng).

---

## Cụm 2 — HSDNTT buộc nhập ≥1 "Thành phần hồ sơ" (149 QLDMHSDNTT_06, 151 QLDMHSDNTT_13)

**Bối cảnh testcase**

- Đối tác phản ánh: form Thêm/Sửa "Hồ sơ đề nghị thanh toán" đánh **"Thành phần hồ sơ" bắt buộc ≥1** (SRS: không bắt buộc).

**Đối chiếu SRS v3.5**

- FR-VIII-09 (UC107) §Inputs — trường riêng: `thanh_phan_ho_so` kiểu `structured`, cột **Bắt buộc = N** (không bắt buộc).
- Nghĩa là: một danh mục "Hồ sơ đề nghị thanh toán" được phép tạo mà KHÔNG cần khai thành phần nào.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:442` (`thanh_phan_ho_so | structured | N`)

**Kết quả verify UI hiện tại (21/07/2026, MCP, `admin`/QTHT)**

- Form luôn dựng sẵn khối "Thành phần hồ sơ" → "Thành phần 1" với `* Mã thành phần` + `* Tên thành phần` (bắt buộc) và **nút xóa của Thành phần 1 bị vô hiệu** → không bỏ được component đầu.
- Test thật: điền Mã + Tên danh mục, để trống thành phần, bấm **Đồng ý** → **0 request gửi máy chủ, không có toast, form bị chặn**, hiện lỗi inline "Mã thành phần là bắt buộc" + "Tên thành phần là bắt buộc".
- Evidence: `../../reverify-audit/QLDMHSDNTT_06/web-loi-thanh-phan-bat-buoc.png` (ảnh lỗi inline), `web-luu-thanh-phan-trong.png`.

**Kết luận QA**

- App **ép ≥1 thành phần hồ sơ** (chặn lưu danh mục không có thành phần), TRÁI với SRS FR-VIII-09 dòng 442 (`thanh_phan_ho_so` = N/không bắt buộc). Đây là bất đồng về **đặc tả/ràng buộc nghiệp vụ**.

**Nội dung đề xuất BA phản hồi đối tác**

- BA chốt source truth cho ràng buộc "thành phần hồ sơ thanh toán":
  1. **Giữ ràng buộc ≥1 thành phần** (nếu nghiệp vụ yêu cầu mọi loại hồ sơ TT phải có tối thiểu 1 thành phần) → cập nhật SRS FR-VIII-09 thành Y + ghi rõ min 1; đối tác/QA cập nhật expected.
  2. **Bỏ ràng buộc, cho phép 0 thành phần** để khớp SRS hiện hành (N) → gửi Dev FE nới validation (cho xóa hết thành phần, không ép Thành phần 1).
- Verdict QA đề xuất: `BA confirm` (SRS ghi N nhưng app enforce ≥1 — cần BA quyết giữ hay bỏ; theo chỉ đạo ghi cột trạng thái = BA confirm vì case vừa là lỗi-vs-SRS vừa cần BA chốt spec).

---

## Ghi chú — ý "Tiêu chí doanh thu bắt buộc" (LDN 142/144) đã KHÔNG tái hiện

- Đối tác (vòng đầu, env `htpldn-uat.ospgroup.vn`) chụp form Loại doanh nghiệp có `* Tiêu chí doanh thu` (dấu * đỏ → bắt buộc).
- Verify lại 21/07 trên env được giao: trường **"Tiêu chí doanh thu" KHÔNG còn bắt buộc** — không có dấu `*` (`::before`=none), placeholder ghi "(tùy chọn)", đã tạo (POST) và cập nhật (PATCH) record thành công khi để trống trường này. Khớp SRS FR-VIII-07 dòng 402 (`tieu_chi_doanh_thu` = N).
- → Ý này KHÔNG phải lỗi ở build hiện tại (không đưa vào câu hỏi BA). Verdict tổng của LDN vẫn `BA confirm` do còn cụm "Danh mục cha".
<!-- group-2-end -->

---

<!-- group-3-start -->
## Form Thêm/Sửa danh mục nhóm C

> **File này để làm gì:** gom các testcase QA không tự chốt Open được (đối tác kỳ vọng khác SRS hoặc SRS im lặng về chi tiết tranh chấp), kèm đối chiếu SRS + evidence UI để BA quyết. Bug có SRS reference rõ ràng → log vào `bug-reports/bug-report-qtht-batch3.md`.

> **SRS dùng:** v3.5 — `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md`. Template chung: TPL-DM-CRUD (dòng 64–171). Màn: SCR-VIII-01 (dòng 1558).

> **Cụm gốc chung Batch 3:** 8/8 case đều nằm trên form Thêm/Sửa của các tab danh mục **dạng phẳng** (Tiêu chí ĐG chi phí, Loại tài khoản, Loại hình tiếp nhận, Kênh tiếp nhận). Cả 8 form đều render thêm trường **"Danh mục cha"** (tùy chọn) mà SRS TPL-DM-CRUD §Inputs (dòng 78–82) + SCR-VIII-01 modal (rows 11–16, dòng 1577–1582) KHÔNG liệt kê → nghi **1 bug FE gốc chung** (component form danh mục dùng chung render nhầm trường cha cho mọi loại). Riêng 2 case TCDGHTCP (160/161) thêm ý "tên trường bổ sung khác SRS". Vì trường thừa để **tùy chọn, không chặn lưu** và tên field form không được SRS quy định cứng → chuyển **BA confirm** thay vì Open (tránh quote sai clause / prescribe implementation).

---

## QLDMTCDGHTCP_06 & QLDMTCDGHTCP_12 — Form Thêm/Sửa "Tiêu chí đánh giá chi phí": trường "Danh mục cha" thừa + tên 2 trường bổ sung khác SRS

**Bối cảnh testcase**

- Dòng Excel: 160 (`QLDMTCDGHTCP_06` — Thêm mới) và 161 (`QLDMTCDGHTCP_12` — Sửa).
- Nội dung kiểm tra: QTHT mở form Thêm mới / Sửa danh mục ở tab **Tiêu chí đánh giá chi phí** (Quản trị hệ thống → Danh mục dùng chung).
- Expected trong file UAT (đối tác):
  - Form không có trường "Danh mục cha" (danh mục phẳng, không phân cấp).
  - Tên trường bổ sung phải giống thiết kế: không phải "Tỷ lệ phần trăm" / "Mức chi phí tối đa".
- Actual đối tác ghi: form hiển thị thêm "Danh mục cha" và 2 trường tên "Tỷ lệ phần trăm", "Mức chi phí tối đa" (đối tác tô vàng 2 label này).

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Inputs chung (áp dụng cho FR-VIII-12) chỉ có 5 trường: `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường cha**.
- SCR-VIII-01 §Thành phần màn hình, modal CRUD (rows 11–16): Mã, Tên, Mô tả, Thứ tự, Trạng thái, nút Hủy/Lưu — **KHÔNG có trường cha**.
- FR-VIII-12 §Inputs — trường riêng: `quy_mo_dn`, `muc_ho_tro_phan_tram` (VD 100/30/10), `tran_ho_tro_nam` (money, VNĐ/năm) — tên logic, không có "danh_muc_cha".
- SCR-VIII-01 §Thành phần đặc biệt — DM Tiêu chí ĐG Chi phí (row 23): cột bổ sung được đặt tên **"Quy mô DN, Mức hỗ trợ (%), Trần hỗ trợ/năm (VNĐ)"** — khác với label form app ("Tỷ lệ phần trăm", "Mức chi phí tối đa"). Đây là label **cột danh sách**, SRS không quy định riêng label **trường trên form**.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:78-82` (TPL-DM-CRUD §Inputs chung — 5 trường, không có cha)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1577-1582` (SCR-VIII-01 modal CRUD — không có trường cha)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:575-579` (FR-VIII-12 §Inputs trường riêng)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1604` (SCR-VIII-01 §Thành phần đặc biệt UC110 — "Mức hỗ trợ (%)", "Trần hỗ trợ/năm (VNĐ)")

**Kết quả verify UI hiện tại**

- Verify lại 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin` / vai trò QTHT, env `https://18.143.165.120.nip.io`.
- Mở `/quan-tri/danh-muc/TIEU_CHI_DG_CHI_PHI` → nút "Thêm mới" → drawer "Thêm mới danh mục".
- Form (đọc DOM `innerText` + ảnh full-res) có 9 trường: Mã*, Tên*, Mô tả, Thứ tự, **Danh mục cha (không bắt buộc)**, Trạng thái, Quy mô doanh nghiệp*, **Tỷ lệ phần trăm* (%)**, **Mức chi phí tối đa* (VNĐ)**.
- "Danh mục cha" là dropdown "Chọn danh mục cha (tùy chọn)" — **không có dấu `*`, không chặn lưu**. Tab này dạng phẳng, không phân cấp cha-con.
- Tái hiện đúng cả 2 ý đối tác phản ánh. Cùng form dùng cho Thêm (160) và Sửa (161).
- Evidence: `../../reverify-audit/QLDMTCDGHTCP_06/form-them-moi-tcdghtcp.png`, `../../reverify-audit/QLDMTCDGHTCP_06/form-them-moi-tcdghtcp-fields.png`; evidence đối tác `../../partner-evidence/QLDMTCDGHTCP_06.jpg`.

**Kết luận QA**

- Cả 2 ý tái hiện đúng trên web hiện tại — không phải "không tái hiện" (không Reject).
- Ý (1) "Danh mục cha" thừa: SRS §Inputs/modal không liệt kê trường cha cho danh mục phẳng → app thêm là **lệch SRS**, nhưng để **tùy chọn + không chặn lưu** → không phá luồng → chưa đủ mức Open, cần BA chốt có bỏ trường này khỏi danh mục phẳng không.
- Ý (2) tên trường: SRS chỉ đặt tên **cột danh sách** ("Mức hỗ trợ (%)", "Trần hỗ trợ/năm (VNĐ)") + tên **field logic** (snake_case); **không quy định cứng label trường trên form**. App dùng "Tỷ lệ phần trăm"/"Mức chi phí tối đa" — khác cách gọi SRS nhưng SRS không prescribe label form → cần BA chốt có chuẩn hóa theo SRS không.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận cho cụm form danh mục dạng phẳng (áp dụng chung cả Batch 3):

- Trường "Danh mục cha" (tùy chọn) hiện xuất hiện trên form của mọi danh mục phẳng: BA có yêu cầu ẩn/bỏ trường này ở các danh mục không phân cấp (chỉ giữ ở DM Cơ quan đơn vị / Lĩnh vực kinh doanh vốn có cấu trúc cây) hay chấp nhận giữ dạng tùy chọn?
- Với TCDGHTCP: BA có yêu cầu đổi tên 2 trường form về đúng SRS SCR-VIII-01 ("Mức hỗ trợ (%)", "Trần hỗ trợ/năm") hay chấp nhận label hiện tại ("Tỷ lệ phần trăm", "Mức chi phí tối đa")?
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA chốt theo SRS → chuyển **Dev FE**; nếu chấp nhận hiện trạng → cập nhật lại expected của đối tác.

---

## QLDMLTK_06/_12 · QLLHTNHS_06/_12 · QLDMKTNHS_06/_12 — Trường "Danh mục cha" thừa trong form Thêm/Sửa các danh mục phẳng (Loại tài khoản · Loại hình tiếp nhận · Kênh tiếp nhận)

**Bối cảnh testcase**

- Dòng Excel: 162 (`QLDMLTK_06` — Thêm), 163 (`QLDMLTK_12` — Sửa), 175 (`QLLHTNHS_06` — Thêm), 176 (`QLLHTNHS_12` — Sửa), 177 (`QLDMKTNHS_06` — Thêm), 178 (`QLDMKTNHS_12` — Sửa).
- Nội dung kiểm tra: QTHT mở form Thêm mới / Sửa danh mục ở 3 tab **Loại tài khoản**, **Loại hình tiếp nhận**, **Kênh tiếp nhận** (Quản trị hệ thống → Danh mục dùng chung).
- Expected đối tác: form không có trường "Danh mục cha" (các danh mục này dạng phẳng).
- Actual đối tác ghi: form hiển thị thêm trường "Danh mục cha".

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Inputs chung: 5 trường `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường cha**.
- SCR-VIII-01 §Thành phần màn hình modal CRUD (rows 11–16): Mã, Tên, Mô tả, Thứ tự, Trạng thái, nút Hủy/Lưu — **KHÔNG có trường cha**.
- FR-VIII-13 (LTK, UC111), FR-VIII-18 (LHTNHS, UC116), FR-VIII-19 (KTNHS, UC117) §Inputs trường riêng: chỉ thêm `loai_danh_muc` (system) — KHÔNG có "danh_muc_cha". Cả 3 đều là danh mục **phẳng** (không phân cấp cha-con). SRS ghi rõ chỉ DM Cơ quan đơn vị (UC103, Tree View) mới có cấu trúc cây.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:78-82` (TPL-DM-CRUD §Inputs chung)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1577-1582` (SCR-VIII-01 modal CRUD)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:595-599` (FR-VIII-13 LTK)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:863-869` (FR-VIII-18 LHTNHS)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:882-888` (FR-VIII-19 KTNHS)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1584-1590` (SCR-VIII-01 — Tree View chỉ áp cho DM Cơ quan đơn vị)

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, tài khoản `admin` / QTHT, env `https://18.143.165.120.nip.io`.
- 3 tab đều có sẵn record chuẩn (LTK: CB/NHT/TVV/CG/DN/QTHT; LHTNHS: TRUC_TUYEN…; KTNHS: CONG_DVC…) → mở được cả Thêm và Sửa.
- Cả 6 form (đọc DOM `innerText` + ảnh full-res): trường gồm Mã*, Tên*, Mô tả, Thứ tự, **Danh mục cha (không bắt buộc)**, Trạng thái — không có trường đặc biệt khác. "Danh mục cha" = dropdown "Chọn danh mục cha (tùy chọn)", **không có `*`, không chặn lưu**.
- Tái hiện đúng phản ánh đối tác trên cả 6 case (3 tab × Thêm/Sửa).
- Evidence: `../../reverify-audit/QLDMLTK_06/form-them-moi-ltk.png`, `../../reverify-audit/QLDMLTK_12/form-sua-ltk.png`, `../../reverify-audit/QLLHTNHS_06/form-them-moi-lhtnhs.png`, `../../reverify-audit/QLLHTNHS_12/form-sua-lhtnhs.png`, `../../reverify-audit/QLDMKTNHS_06/form-them-moi-ktnhs.png`, `../../reverify-audit/QLDMKTNHS_12/form-sua-ktnhs.png`; evidence đối tác `../../partner-evidence/QLDMLTK_06.jpg`, `QLDMLTK_11.jpg`, `QLLHTNHS_06.jpg`, `QLLHTNHS_12.jpg`, `QLDMKTNHS_06.jpg`, `QLDMKTNHS_12.jpg`.

**Kết luận QA**

- 6 case tái hiện đúng — không phải "không tái hiện" (không Reject).
- Trường "Danh mục cha" lệch SRS (SRS §Inputs/modal không liệt kê cho danh mục phẳng) nhưng để **tùy chọn + không chặn lưu** → không phá luồng → chưa đủ mức Open. Đây là **1 bug FE gốc chung** (component form danh mục dùng chung render trường cha cho mọi loại), cùng bản chất với cụm TCDGHTCP ở trên.

**Nội dung đề xuất BA phản hồi đối tác**

- Cùng câu hỏi với cụm TCDGHTCP: BA có yêu cầu ẩn/bỏ trường "Danh mục cha" khỏi form của các danh mục phẳng (LTK, LHTNHS, KTNHS và các tab phẳng khác), chỉ giữ ở danh mục cấu trúc cây (Cơ quan đơn vị / Lĩnh vực kinh doanh) hay chấp nhận giữ dạng tùy chọn?
- Verdict QA đề xuất: `Cần BA xác nhận`. Vì nghi 1 bug FE gốc chung xuyên Batch 1·2·3 → nếu BA chốt bỏ, đề nghị **Dev FE** sửa 1 lần ở component form danh mục dùng chung (áp cho mọi tab phẳng).

---
<!-- group-3-end -->

---

<!-- group-4-start -->
## Cảnh báo khi đóng form Quản lý danh mục dùng chung

> **File này để làm gì:** gom 8 testcase QTHT batch 4 (đối tác báo tuần 3) cùng 1 vấn đề gốc: **đóng form Thêm/Sửa danh mục khi đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?"**. QA đã verify tái hiện đúng trên web, nhưng SRS v3.5 **im lặng** về clause này cho màn danh mục → cần BA chốt có bổ sung yêu cầu hay không. Verdict sheet cả 8 case: `BA confirm`.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE`, mở file verify số dòng thực. SRS dùng: v3.5 (`input/srs-update-2026-5-5/`).

---

## Tóm tắt cụm — 8 TC, 1 bug gốc

Cả 8 TC đều test cùng 1 hành vi trên màn **Quản lý danh mục dùng chung** (SCR-VIII-01), khác nhau chỉ ở tab danh mục con. Đối tác báo giống hệt nhau: đóng form (nút X / Hủy) khi form đang có dữ liệu chưa lưu → không hỏi xác nhận, đóng thẳng, dữ liệu bị hủy.

| Dòng Excel | Mã TC | Tab danh mục | FR / UC | Verdict |
|---|---|---|---|---|
| 124 | `QLDMLVPL_14` | Lĩnh vực pháp lý | FR-VIII-01 / UC99 | BA confirm |
| 129 | `QLDMLHHT_11` | Loại hình hỗ trợ | FR-VIII-02 / UC100 | BA confirm |
| 137 | `QLDMCTHT_11` | Chương trình hỗ trợ | FR-VIII-03 / UC101 | BA confirm |
| 140 | `QLDMTTVV_11` | Tình trạng vụ việc | FR-VIII-04 / UC102 | BA confirm |
| 134 | `QLDMCQDVQL_12` | Cơ quan đơn vị (tree-view) | FR-VIII-05 / UC103 | BA confirm |
| 143 | `QLDMLDN_11` | Loại doanh nghiệp | FR-VIII-07 / UC105 | BA confirm |
| 147 | `QLDMHSDNHT_11` | Hồ sơ đề nghị hỗ trợ | FR-VIII-08 / UC106 | BA confirm |
| 150 | `QLDMHSDNTT_11` | Hồ sơ đề nghị thanh toán | FR-VIII-09 / UC107 | BA confirm |

---

## [QLDMLVPL_14 · QLDMLHHT_11 · QLDMCTHT_11 · QLDMTTVV_11 · QLDMCQDVQL_12 · QLDMLDN_11 · QLDMHSDNHT_11 · QLDMHSDNTT_11] — Thiếu hộp thoại xác nhận "bỏ thay đổi chưa lưu" khi đóng form danh mục

**Bối cảnh testcase**

- Dòng Excel: 124, 129, 137, 140, 134, 143, 147, 150 — mã TC như bảng trên.
- Nội dung kiểm tra: role QTHT mở form Thêm mới / Sửa một danh mục con, nhập hoặc sửa dở, rồi bấm đóng form (nút X góc phải hoặc nút Hủy).
- Expected trong file UAT (đối tác):
  - Khi đóng form đang có thay đổi chưa lưu, hệ thống phải hỏi xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?" trước khi đóng.
- Actual đối tác ghi: hệ thống đóng thẳng form, không hỏi, thay đổi bị mất.

**Đối chiếu SRS v3.5**

- Màn Quản lý danh mục dùng chung (SCR-VIII-01) mô tả bố cục + thao tác CRUD danh mục qua template dùng chung TPL-DM-CRUD. Phần mô tả form và nút đóng KHÔNG nêu yêu cầu hộp thoại xác nhận khi đóng form đang chỉnh sửa dở.
- §Quy tắc tương tác của màn danh mục chỉ quy định phân trang và sắp xếp, KHÔNG có clause "cảnh báo mất dữ liệu chưa lưu".
- Hộp thoại xác nhận "bỏ thay đổi chưa lưu" LẠI được quy định rõ ở các màn khác (Hỏi đáp pháp lý; Chuyên gia / Tư vấn viên) → cho thấy SRS có khái niệm này nhưng cố ý (hoặc bỏ sót) không áp cho màn danh mục.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1606` → `:1608` (SCR-VIII-01 §Quy tắc tương tác — chỉ phân trang + sắp xếp)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:65` → `:171` (TPL-DM-CRUD — mẫu form CRUD danh mục, không có clause dirty-state)
- Đối chiếu ngược (clause CÓ ở màn khác): `input/srs-update-2026-5-5/srs-fr-02-*.md:1070`; `input/srs-update-2026-5-5/srs-fr-04-*.md:1512`, `:1562`, `:1685`, `:1808`

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `admin` (role QTHT).
- URL gốc: `https://18.143.165.120.nip.io/quan-tri/danh-muc/*` (mỗi tab 1 loại danh mục).
- Với mỗi tab: mở form Thêm mới → nhập Mã/Tên/Mô tả (state dirty) → bấm Đóng (X).
- Quan sát đồng nhất cả 8 tab: form đóng thẳng về danh sách, **KHÔNG** hộp thoại xác nhận, **KHÔNG** toast, **0 request** ghi dữ liệu (observer toast-capture.js self-check=1, query `.ant-modal-confirm,[role="dialog"]` rỗng, text "chưa lưu"/"bỏ thay đổi" không xuất hiện). Dữ liệu nhập dở bị hủy im lặng.
- Riêng tab Cơ quan đơn vị (`QLDMCQDVQL_12`) là tree-view (panel phải), hành vi đóng vẫn giống: panel reset về "Chọn một đơn vị từ cây bên trái", không cảnh báo.
- Evidence: `../../reverify-audit/<TC>/BUG-<TC>-add-close-noconfirm.png` (8 ảnh, mỗi TC 1 ảnh).

**Kết luận QA**

- Web tái hiện ĐÚNG như đối tác báo: đóng form dirty không có hộp thoại xác nhận.
- Nhưng đối chiếu SRS v3.5: màn Quản lý danh mục **không quy định** yêu cầu hộp thoại này → web hiện tại **không vi phạm điều khoản nào của SRS cho màn danh mục**.
- Vì clause này CÓ ở màn khác nhưng SILENT ở màn danh mục, QA không tự chốt được đây là "bug thiếu tính năng" hay "đúng đặc tả" → cần BA quyết. Đây là 1 vấn đề gốc chung ở component form danh mục dùng chung (sửa 1 chỗ, cả 8 tab hết).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận yêu cầu nghiệp vụ cho màn Quản lý danh mục dùng chung (SCR-VIII-01):

- **Câu hỏi:** Có bổ sung yêu cầu hệ thống hiển thị hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?" khi người dùng đóng form Thêm/Sửa danh mục đang có thay đổi chưa lưu không?
- Nếu **CÓ** (đồng bộ với màn Hỏi đáp / Chuyên gia): chuyển Dev FE bổ sung dirty-check + hộp thoại xác nhận cho component form danh mục dùng chung; áp 1 lần cho cả 8 tab. Verdict cập nhật → `Open` (owner Dev FE).
- Nếu **KHÔNG**: web hiện tại đã đúng đặc tả cho màn danh mục; cập nhật lại kỳ vọng của đối tác cho cả 8 TC (không phải bug).
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận` (BA confirm) — chưa gửi Dev cho tới khi BA chốt.
<!-- group-4-end -->

---

<!-- group-5-start -->
## Trạng thái rỗng khi tìm kiếm Cơ quan đơn vị

> Gom testcase QTHT Batch 5 mà QA cần BA phản hồi lại đối tác. Citation trỏ `srs-update-2026-5-5/` (v3.5) / `srs-v3.5/` — đã mở file verify số dòng thực.

---

## QLDMCQDVQL_05 — Tìm kiếm cây "Cơ quan đơn vị" không ra kết quả, không hiện thông báo "Không tìm thấy"

**Bối cảnh testcase**

- Dòng Excel: 139, mã TC `QLDMCQDVQL_05`.
- Nội dung kiểm tra: QTHT vào **Quản trị hệ thống → Danh mục dùng chung → Cơ quan đơn vị** (giao diện cây đơn vị — Tree View), gõ từ khóa tìm kiếm không khớp bản ghi nào.
- Expected trong file UAT:
  - Khi tìm kiếm không ra kết quả, hệ thống phải hiển thị thông báo **"Không tìm thấy mục danh mục phù hợp"**.
- Actual đối tác ghi: gõ "tư pháp HCM" → vùng cây đơn vị **trắng hoàn toàn**, không có thông báo nào.

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Processing chung — Tìm kiếm (SEARCH) chỉ quy định: nhận từ khóa → tìm theo mã/tên (bản ghi chưa xóa) → phân trang + trả kết quả. **Không quy định thông báo chuẩn khi kết quả rỗng.**
- Acceptance Criteria chung về tìm kiếm chỉ nêu: "Given QTHT tìm kiếm When nhập từ khóa Then hiển thị kết quả matching" — không mô tả trạng thái khi 0 kết quả.
- Toàn bộ template TPL-DM-CRUD (áp cho 15 màn danh mục, gồm Cơ quan đơn vị UC103) không có mã lỗi / message cho "search rỗng".

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:130` (SEARCH — bước 1-3, không có empty message)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:170` (AC tìm kiếm — chỉ hiển thị kết quả matching)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin` (QTHT).
- Mở `https://18.143.165.120.nip.io/quan-tri/danh-muc/CO_QUAN_DON_VI`, gõ đúng từ khóa "tư pháp HCM" (không khớp) vào ô tìm "Cây đơn vị".
- Vùng cây `.ant-tree` innerText length = 0 (trắng, không node). Không có `.ant-empty` trong panel cây → **không hiện message nào** (kể cả "Trống").
- → **Tái hiện đúng** quan sát của đối tác. Actual đối tác chính xác.
- Evidence: `../../reverify-audit/QLDMCQDVQL_05/search-empty-tree.png`

**Kết luận QA**

- `QLDMCQDVQL_05` **không phải bug theo SRS v3.5**: SRS không quy định thông báo cho tìm kiếm rỗng, nên app để trống không vi phạm clause SRS nào.
- Tuy nhiên, actual đối tác quan sát là ĐÚNG (vùng cây trắng, không feedback). Đây là bất đồng về **kỳ vọng UX** vs **đặc tả** (SRS silent) → cần BA quyết, QA không tự Reject.
- Cross-ref cụm empty-state: `QLTKND_06` (Batch 8 — màn Tài khoản hiện "Trống" thay vì "Không tìm thấy tài khoản phù hợp"). Nghi thiếu empty-state chuẩn dùng chung cho các màn tìm kiếm.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Có bổ sung yêu cầu **empty-state message** cho tìm kiếm không ra kết quả (ít nhất "Không tìm thấy dữ liệu phù hợp") vào SRS TPL-DM-CRUD §SEARCH cho các màn danh mục (gồm cả cây Cơ quan đơn vị) hay không?
- Nếu **CÓ** → chuyển Dev bổ sung empty-state (owner: Dev FE), đồng bộ cả cụm (QLTKND_06). Verdict khi đó: `Vẫn lỗi`.
- Nếu **KHÔNG** → giữ nguyên, cập nhật expected của `QLDMCQDVQL_05` (bỏ yêu cầu message). Verdict: `Không phải bug theo SRS`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev.
<!-- group-5-end -->

---

<!-- group-6-start -->
## Sắp xếp trên màn Vai trò

> Gom testcase QA không tự chốt verdict được (SRS silent / kỳ vọng đối tác vượt spec). Kèm đối chiếu SRS + evidence UI để BA quyết nhanh.

---

## QLVT_14 (row 164) — Màn Vai trò không có sắp xếp bằng bấm tiêu đề cột

**Bối cảnh testcase**

- Dòng Excel: 164, mã TC `QLVT_14`.
- Nội dung kiểm tra: QTHT mở màn Vai trò (`/quan-tri/vai-tro`), bấm tiêu đề cột để sắp xếp danh sách.
- Expected trong file UAT:
  - Bấm tên cột thì danh sách sắp xếp lại (luân phiên tăng/giảm).
  - Mặc định sắp theo "Tên vai trò" tăng dần.
- Actual đối tác ghi: không sắp xếp được theo cột.

**Đối chiếu SRS v3.5**

- SCR-VIII-02 (Quản lý Vai trò): cột "Tên vai trò" có cột Hành vi = "—" (không quy định sắp xếp tương tác). Màn này KHÔNG có mục "Quy tắc tương tác" — khác SCR-VIII-01 (Danh mục dùng chung) đã bổ sung click-to-sort cho cột "Tên" theo STT69 UAT 2026-06-02.
- FR-VIII-14 (UC112 — Quản lý vai trò): Acceptance Criteria chỉ nêu "danh sách vai trò, phân trang" — không quy định sắp xếp bằng bấm tiêu đề cột, cũng không nêu rõ tiêu chí sắp mặc định.
- → SRS **silent** về sắp xếp tương tác (click cột) trên màn Vai trò.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1625` (SCR-VIII-02, cột Tên vai trò — Hành vi "—")
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1612` (SCR-VIII-02 — không có §Quy tắc tương tác)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:660` (FR-VIII-14 AC — chỉ "danh sách vai trò, phân trang")
- So sánh: `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1608` (SCR-VIII-01 Danh mục — CÓ click-to-sort cột Tên [STT69])

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin` / QTHT, URL `https://18.143.165.120.nip.io/quan-tri/vai-tro`.
- Danh sách 11 vai trò (CB_NV_BN, CB_NV_DP, CB_NV_TW, CB_PD_BN, CB_PD_DP, CB_PD_TW, CG, DN, NHT, QTHT, TVV).
- Kiểm DOM 8 tiêu đề cột: tất cả không có class sortable, không `aria-sort`, không sorter icon, con trỏ `auto` (không click được). Bấm "Tên vai trò" → URL không đổi, thứ tự không đổi.
- Thứ tự mặc định hiện tại = theo Tên vai trò tăng dần (trùng Mã vai trò tăng dần) → phần "mặc định Tên vai trò↑" của đối tác ĐANG được đáp ứng.
- Evidence: `../../reverify-audit/QLVT_14/vaitro-baseline.png` (web) + `../../partner-evidence/QLVT_14.jpg` (đối tác).

**Kết luận QA**

- `QLVT_14`: đối tác quan sát ĐÚNG thực tế (màn Vai trò không sắp xếp được bằng bấm tiêu đề cột — vì màn này không có chức năng sort tương tác).
- Web hiện tại phù hợp SRS (SRS không quy định click-to-sort cho màn Vai trò). Không phải bug (không vi phạm rule SRS) và cũng không phải điều đối tác báo sai.
- Điểm cần BA: kỳ vọng "click cột để sắp xếp" của đối tác là bổ sung so với SRS — SRS chưa quy định cho màn Vai trò.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận hướng xử lý cho `QLVT_14`:
  - Có bổ sung chức năng bấm tiêu đề cột để sắp xếp cho màn Vai trò (tương tự cột "Tên" ở màn Danh mục dùng chung theo STT69) không?
  - Hay giữ nguyên: màn Vai trò chỉ sắp mặc định (Tên vai trò tăng dần), không có sort tương tác?
- Verdict QA đề xuất: `Cần BA xác nhận`. Nếu BA quyết bổ sung → chuyển Dev FE làm click-to-sort; nếu giữ nguyên → cập nhật expected testcase `QLVT_14` cho khớp SRS (không có click-to-sort).
<!-- group-6-end -->

---

<!-- group-7-start -->
## Cấu hình hệ thống / SLA

> Gom các testcase QA không tự chốt verdict được (bất đồng ĐẶC TẢ giữa SRS v3.5 / thực tế web / kỳ vọng đối tác) trên màn **Cấu hình hệ thống** Tab 1 "Thời hạn xử lý (SLA)". Màn này là **MÀN HÌNH MỚI v2.1** với spec churn nặng (4→3→2 tab qua 2 lần BA chốt 2026-05-07).
>
> - Account verify: `admin` / QTHT (Tab 1 SLA chỉ QTHT truy cập — SRS dòng 1731). URL: `/quan-tri/cau-hinh`.
> - Tool: Chrome DevTools MCP. Env verify `18.143.165.120.nip.io` hiển thị **giống hệt** env đối tác `htpldn-uat.ospgroup.vn` (cùng 6 dòng SLA, cùng cột, cùng toggle disabled).
> - Citation: `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:LINE` (đã mở file verify số dòng thực).

**Tóm tắt verdict batch 7:** 4 case BA confirm (152, 153, 154, 155) + 1 case Open (156 — xem `../../bug-reports/qtht/Pass-bug-report-qtht-batch7.md`).

| Row | Mã TC | Vấn đề | Verdict |
|---|---|---|---|
| 152 | QLCHTHXLHS_02 | Số thẻ tab (3 app vs 2 SRS vs 4 đối tác) | BA confirm |
| 153 | QLCHTHXLHS_03 | Cấu trúc cột bảng SLA (redesign + 2 vi phạm) | BA confirm |
| 154 | QLCHTHXLHS_05 | Toggle "Gửi email" không bật/tắt inline | BA confirm |
| 155 | QLCHTHXLHS_06 | Toggle "Gửi TB app" không bật/tắt inline | BA confirm |

---

## QLCHTHXLHS_02 — Số thẻ tab màn Cấu hình hệ thống (bất đồng 3 chiều: SRS 2 · web 3 · đối tác 4)

**Bối cảnh testcase**

- Dòng Excel: 152, mã TC `QLCHTHXLHS_02`.
- Nội dung kiểm tra: QTHT mở màn Cấu hình hệ thống (`/quan-tri/cau-hinh`), đếm số thẻ tab.
- Expected trong file UAT: đối tác kỳ vọng **4 thẻ** — SLA / Phân công / Mẫu phản hồi / Quy trình.
- Actual đối tác ghi: hệ thống hiển thị **3 thẻ** — SLA / Mẫu phản hồi / **Quản lý ngày lễ**.

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT). URL `/quan-tri/cau-hinh`.
- Web hiển thị đúng **3 tab**: "Thời hạn xử lý (SLA)" · "Mẫu phản hồi" · "Quản lý ngày lễ" (khớp actual đối tác).
- Evidence: `../../reverify-audit/QLCHTHXLHS_02/QLCHTHXLHS_02-tabs-table.png`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo SCR-VIII-06, màn = **2 tab**: Tab 1 "Thời hạn xử lý / SLA", Tab 2 "Mẫu phản hồi". Đã **bỏ** Tab "Phân công mặc định" (Q11) + Tab "Quy trình hỗ trợ" (Hướng A) — BA chốt 2026-05-07.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1724` — "Loại màn hình: Tab Page (2 tabs)"
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1728` — "Đã bỏ: Tab 4 Quy trình hỗ trợ ... Tab 2 Phân công mặc định"
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1742` — "Tab 1: Thời hạn xử lý / SLA — Tab 2: Mẫu phản hồi"

2. Nhưng web thực tế có **tab thứ 3 "Quản lý ngày lễ"** — SCR-VIII-06 (2 tab) **không liệt kê** tab này (chức năng quản lý ngày nghỉ lễ nằm ở FR riêng, không thuộc 2 tab của màn Cấu hình theo spec hiện hành).

**Câu hỏi cần BA xác nhận**

Màn Cấu hình hệ thống phải có **bao nhiêu tab** và **tab nào**?

1. **Theo SRS v3.5 (2 tab):** SLA + Mẫu phản hồi. → tab "Quản lý ngày lễ" là **thừa** so với spec.
2. **Theo thực tế web (3 tab):** SLA + Mẫu phản hồi + Quản lý ngày lễ → cần BA bổ sung "Quản lý ngày lễ" vào SCR-VIII-06 nếu đây là thiết kế mới.
3. **Kỳ vọng đối tác (4 tab, gồm Phân công + Quy trình):** là **spec CŨ đã bị bỏ** (BA chốt 2026-05-07) → không còn hiệu lực.

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_02`: **BA confirm**. Chưa gửi Dev tới khi BA chốt số tab chuẩn.
- Kỳ vọng "4 thẻ" của đối tác dựa trên spec cũ (Phân công/Quy trình đã bỏ) → **đề nghị cập nhật expected testcase** theo spec hiện hành.
- Nếu BA giữ SRS 2 tab: tab "Quản lý ngày lễ" cần gỡ khỏi màn (owner Dev FE) hoặc bổ sung vào SCR-VIII-06.
- Nếu BA chấp nhận 3 tab: cập nhật SCR-VIII-06 thành 3 tab.

---

## QLCHTHXLHS_03 — Cấu trúc cột bảng Tab SLA (redesign inline→modal + 2 điểm vi phạm SRS)

**Bối cảnh testcase**

- Dòng Excel: 153, mã TC `QLCHTHXLHS_03`.
- Nội dung kiểm tra: QTHT xem bảng Tab 1 "Thời hạn xử lý (SLA)", đối chiếu các cột.
- Expected/actual đối tác: bảng SLA khác spec — Loại yêu cầu tách 2 cột · 6 giá trị (spec 4) · Cảnh báo mức 1&2 gộp "Vùng cảnh báo" · thiếu cột Quá hạn(%)/Số ngày BS tối đa · thừa "Hệ số quá hạn".

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT).
- Bảng thực tế có **8 cột**: `Loại yêu cầu` (mã enum) · `Tên loại` · `Thời hạn (ngày LV)` · `Vùng cảnh báo` (1 thanh gộp) · `Hệ số quá hạn` (=2) · `Email` (toggle) · `Thông báo app` (toggle) · `Hành động` (nút Sửa).
- **6 dòng** loại YC: HOI_DAP · HOI_DAP_PHUC_TAP · HO_SO_CHI_TRA · HO_SO_HT · HO_SO_TT · VU_VIEC.
- Giá trị CB mức 1/mức 2 vẫn sửa được trong modal "Sửa" (Ngưỡng cảnh báo 1=50, Ngưỡng cảnh báo 2=100).
- Evidence: `../../reverify-audit/QLCHTHXLHS_03/QLCHTHXLHS_03-cols-right-clean.png`.

**Đối chiếu SRS v3.5 — tách từng ý con**

| # | Đối tác phản ánh | SRS v3.5 | Web thực tế | Đánh giá QA |
|---|---|---|---|---|
| a | Loại yêu cầu tách 2 cột | SCR dòng 1749: 1 cột "Loại yêu cầu". Nhưng FR Inputs có cả `loai_yeu_cau` + `ten_loai` (dòng 465–466) | 2 cột (mã + tên loại) | Thiết kế thêm hợp lý (đủ hơn) — **cần BA chốt** |
| b | 6 giá trị (spec 4) | SCR 1749 + FR 465: 4 giá trị (HOI_DAP/VU_VIEC/HO_SO_HT/HO_SO_TT) | 6 giá trị (thêm HOI_DAP_PHUC_TAP, HO_SO_CHI_TRA) | Thêm 2 loại SLA ngoài enum SRS — **cần BA chốt** có bổ sung vào spec |
| c | Gộp "Vùng cảnh báo" | SCR dòng 1751–1752: 2 cột riêng "CB mức 1 (%)" + "CB mức 2 (%)" | 1 thanh "Vùng cảnh báo" (hiển thị); giá trị vẫn sửa trong modal | Khác cách hiển thị, giá trị vẫn cấu hình được — **cần BA chốt** |
| d | Thiếu cột Quá hạn(%) | SCR dòng 1753: cột readonly "Quá hạn (%)" = 100% | Giá trị 100% nhúng trong thanh Vùng cảnh báo, không có cột riêng | Khác cách hiển thị — **cần BA chốt** |
| e | **Thiếu cột Số ngày BS tối đa** | SCR 11a dòng 1756 + FR Inputs #10 dòng 474 + AC dòng 515: bắt buộc cho loại ≠ HOI_DAP (default 5) | **Không có** ở cả bảng lẫn modal | **QA khẳng định vi phạm** — thiếu trường cấu hình bắt buộc |
| f | **Thừa "Hệ số quá hạn"** | SCR dòng 1759 + FR dòng 471 (BA chốt 2026-05-07 Q5): `qua_han_he_so` **ngầm, KHÔNG hiển thị UI** | Hiện cột "Hệ số quá hạn" = 2 (và cả trong modal) | **QA khẳng định vi phạm** — hiện field mà BA đã chốt phải ẩn |

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1749` (4 giá trị, 1 cột loại)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1751` · `:1752` (CB mức 1 / mức 2 = 2 cột riêng)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1753` (cột Quá hạn %)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1756` (cột Số ngày BS tối đa)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1759` + `:471` (Hệ số quá hạn ngầm, không UI — BA Q5)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:474` (so_ngay_bo_sung_toi_da — BA chốt 2026-05-13) + `:515` (AC cột Số ngày BS tối đa)

**Câu hỏi cần BA xác nhận**

Bảng Tab SLA đã được **redesign** so với SRS (bảng read-only + nút "Sửa" mở modal, thay vì inline-edit + 1 nút [Lưu cấu hình]). BA chốt hướng nào cho các điểm a–d (cấu trúc cột)?
- 2 điểm **e** (thiếu Số ngày BS tối đa) và **f** (thừa Hệ số quá hạn) là **vi phạm rõ SRS + BA đã chốt trước** → QA đề xuất **chuyển Dev fix** (đã ghi chi tiết ở `Pass-bug-report-qtht-batch7.md` BUG-QLCHTHXLHS_07).

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_03`: **BA confirm** (vừa có điểm cần BA chốt thiết kế a–d, vừa có 2 vi phạm rõ e–f).
- Nếu BA giữ SRS: e (thêm cột/trường Số ngày BS) + f (ẩn Hệ số quá hạn) → owner Dev FE. a–d tùy BA chốt giữ SRS hay chấp nhận redesign.

---

## QLCHTHXLHS_05 & QLCHTHXLHS_06 — Toggle "Gửi email" / "Gửi TB app" không bật/tắt được trên dòng (redesign inline → modal-edit)

**Bối cảnh testcase**

- Dòng Excel: 154 (`QLCHTHXLHS_05` — Email) · 155 (`QLCHTHXLHS_06` — Thông báo app).
- Nội dung kiểm tra: QTHT thử bật/tắt toggle "Gửi email" / "Gửi TB app" **trực tiếp trên dòng** bảng SLA.
- Actual đối tác ghi: hệ thống **KHÔNG cho bật/tắt trên dòng** (video hiện con trỏ 🚫 khi hover toggle).

**Kết quả verify UI hiện tại**

- Verify 2026-07-21 qua Chrome DevTools MCP, account `admin` (QTHT).
- Cả 12 toggle (6 dòng × 2 cột Email/Thông báo app) đều ở trạng thái `disabled` (đo DOM: `disabled=true` toàn bộ) → **không bật/tắt được inline** (khớp phản ánh đối tác + con trỏ 🚫 trong video).
- **Tuy nhiên**, giá trị Email/Thông báo app **sửa được** trong modal "Sửa cấu hình SLA" (2 switch "Gửi email cảnh báo" / "Gửi thông báo in-app" ở trạng thái enabled, bật/tắt được, lưu qua [Đồng ý]).
- Evidence: `../../reverify-audit/QLCHTHXLHS_05/QLCHTHXLHS_05-toggle-disabled-inline.png` (disabled inline) + `...-modal-editable.png` (sửa được trong modal). Tương tự `../../reverify-audit/QLCHTHXLHS_06/`.

**Đối chiếu SRS v3.5**

- SCR-VIII-06 dòng 1754 (Gửi email) + 1755 (Gửi TB app): mô tả là **cột toggle** (hành vi = toggle) trong bảng SLA → thiết kế gốc là **inline toggle**.
- SCR dòng 1757: có nút [Lưu cấu hình] chung → thiết kế gốc: sửa inline nhiều dòng rồi Lưu 1 lần.
- Web đã **redesign**: bảng read-only + nút "Sửa" từng dòng mở modal; toggle Email/app chỉ sửa trong modal.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1754` (Cột Gửi email — toggle)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1755` (Cột Gửi TB app — toggle)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1757` (nút [Lưu cấu hình])

**Câu hỏi cần BA xác nhận**

SRS thiết kế Tab SLA dạng **inline-edit** (toggle + input trực tiếp trên bảng). Web đã đổi sang **read-only table + modal-edit** (bật/tắt Email/Thông báo app trong modal "Sửa", không sửa được trên dòng). Chức năng cấu hình **KHÔNG bị chặn** (vẫn đổi được qua modal), chỉ khác cách tương tác. BA chốt:
1. **Bắt buộc inline toggle** theo SRS → hiện web là lỗi, owner Dev FE.
2. **Chấp nhận modal-edit** (sửa qua nút Sửa) → cập nhật SCR-VIII-06 + cập nhật expected testcase 154/155.

**Đề xuất QA tạm thời**

- Tạm verdict `QLCHTHXLHS_05` + `QLCHTHXLHS_06`: **BA confirm**. Chưa gửi Dev tới khi BA chốt inline vs modal.
- Actual đối tác (không bật/tắt inline) là **đúng thực tế** → không Reject; nhưng chức năng cấu hình Email/app không mất (sửa qua modal) → không phải bug chặn luồng, để BA chốt thiết kế.
<!-- group-7-end -->

---

<!-- group-8-start -->
## Quản lý tài khoản người dùng

> Gom các testcase Batch 8 QA verdict **BA confirm** (đối chiếu SRS xong nhưng cần BA phản hồi lại đối tác). Đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. Bug có SRS reference rõ (Open) → `bug-report-qtht-batch8.md`; case không tái hiện (Reject) → `../../reverify-audit/`.

> Citation trỏ `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:LINE` (SRS v3.5, đã mở file verify số dòng thực).

---

## QLTKND_06 — Empty-state khi tìm kiếm không ra: "Trống" vs thông báo ngữ cảnh

**Bối cảnh testcase**

- Dòng Excel: 167, mã TC `QLTKND_06`.
- Nội dung kiểm tra: QTHT tìm kiếm chuỗi không tồn tại trên màn Quản lý tài khoản người dùng (SCR-VIII-03).
- Expected trong file UAT: hiển thị thông báo ngữ cảnh "Không tìm thấy tài khoản phù hợp".
- Actual đối tác ghi: hệ thống hiển thị "Trống" (component empty mặc định).

**Đối chiếu SRS v3.5**

- SCR-VIII-03 (bảng Thành phần màn hình + hành vi, dòng 1642–1673) KHÔNG quy định nội dung thông báo khi tìm kiếm không có kết quả trên màn này (im lặng về copy empty-state).
- Không có BR/AC nào chốt chuỗi thông báo empty-state cho danh sách tài khoản.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1635` (heading SCR-VIII-03 Quản lý Tài khoản NSD)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1647` (Ô tìm kiếm — có search, KHÔNG spec copy empty-state khi 0 kết quả)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT.
- Tìm chuỗi random không có kết quả → khung danh sách hiển thị "Trống" (component empty mặc định) — tái hiện đúng như đối tác phản ánh.
- Evidence: `../../reverify-audit/QLTKND_06/empty-trong.png`.

**Kết luận QA**

- `QLTKND_06` KHÔNG đủ căn cứ Open: SRS im lặng về nội dung thông báo empty-state màn Tài khoản → app hiển thị "Trống" không vi phạm clause SRS nào.
- Cùng bản chất với **QLDMCQDVQL_05** (B5) — nghi dùng chung 1 component empty-state gốc; cần thống nhất copy toàn hệ thống.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý copy empty-state:

- Có đổi "Trống" thành thông báo ngữ cảnh "Không tìm thấy tài khoản phù hợp" cho màn Tài khoản (và các màn dùng chung component) không?
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS silent), chưa gửi Dev tới khi BA chốt chuẩn copy empty-state chung.

---

## QLTKND_25 — Sắp xếp theo cột: màn Tài khoản không có click-sort

**Bối cảnh testcase**

- Dòng Excel: 170, mã TC `QLTKND_25`.
- Nội dung kiểm tra: QTHT bấm tên cột trên danh sách tài khoản để sắp xếp.
- Expected trong file UAT: bấm tên cột → danh sách sắp xếp theo cột đó, luân phiên tăng/giảm.
- Actual đối tác ghi: KHÔNG sắp xếp được (mặc định "Lần đăng nhập cuối" giảm dần).

**Đối chiếu SRS v3.5**

- SCR-VIII-03 bảng Thành phần màn hình (cột 10–16): hành vi cột Username = "click → chi tiết"; các cột Họ tên / Email / Đơn vị / Vai trò / Trạng thái = "—" (không mô tả tương tác click-sort) → màn Tài khoản KHÔNG yêu cầu click-sort cột.
- Ngược lại, các màn sibling CÓ click-sort theo đặc tả: danh mục dùng chung cùng module (SCR-VIII-01, chỉ cột Tên — [STT69]); Vụ việc HTPL; Hỏi đáp pháp lý → hệ thống không đồng nhất.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1654` (cột Username "click → chi tiết"; cột Họ tên/Email/Đơn vị/Vai trò/Trạng thái dòng 1655–1659 hành vi = "—", không click-sort)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` (SCR-VIII-01 cột Tên có sort — [STT69])

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT, URL `/quan-tri/tai-khoan`.
- DOM: 10 header cột, KHÔNG cột nào có mũi tên sắp xếp / `aria-sort` / marker sort.
- Behavioral: bấm header "Tên đăng nhập" → thứ tự dòng giữ nguyên, không có request `?sortBy=` gửi lên máy chủ.
- Evidence: `../../reverify-audit/QLTKND_25/web-cot-khong-sort.png`, audit `../../reverify-audit/QLTKND_25/audit.md`.

**Kết luận QA**

- `QLTKND_25` KHÔNG đủ căn cứ Open: xét riêng SCR-VIII-03, SRS không mô tả click-sort → app đúng spec màn này.
- KHÔNG thể Reject: sibling screens có click-sort → không đồng nhất cấp cross-screen.
- Cùng bản chất với **QLHSDNHTCP_19** (row 23, đã BA confirm).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA quyết phạm vi yêu cầu click-sort:

- Click-sort theo cột là yêu cầu chung cho MỌI màn danh sách (khi đó màn Tài khoản thiếu → bổ sung, owner Dev FE)? Hay chỉ áp cho màn có "Hành vi = sắp xếp" trong SRS (khi đó màn Tài khoản đúng spec)?
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt phạm vi (đồng bộ QLHSDNHTCP_19).

---

## QLTKND_27 — Nút "Đặt lại mật khẩu" đã bị bỏ theo STT80

**Bối cảnh testcase**

- Dòng Excel: 171, mã TC `QLTKND_27`.
- Nội dung kiểm tra: QTHT tìm nút "Đặt lại mật khẩu" trên màn Quản lý tài khoản (cột Hành động).
- Expected trong file UAT: nút "Đặt lại mật khẩu" hiển thị khi TK Đang hoạt động / Tạm khóa.
- Actual đối tác ghi: màn hình KHÔNG hiển thị nút chức năng này.

**Đối chiếu SRS v3.5**

- SCR-VIII-03 cột Hành động (row 16): **[STT80 UAT 2026-06-02] Bỏ "Đổi MK"** — quản trị viên KHÔNG đặt/đổi mật khẩu người dùng; reset MK qua "Gửi lại email kích hoạt".
- FR-VIII-15 §Inputs [STT80]: admin không đặt mật khẩu khi tạo TK; user tự đặt qua link kích hoạt.
- FR-VIII-26: reset/đặt lại mật khẩu là luồng tự phục vụ "Quên mật khẩu" của user, không phải nút admin trên list.
- → App KHÔNG hiện nút = ĐÚNG SRS v3.5. Kỳ vọng đối tác theo spec CŨ (trước STT80).

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1660` (cột Hành động — [STT80] bỏ "Đổi MK")
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:695` (§Inputs — [STT80] bỏ field mật khẩu)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1260` (FR-VIII-26 — Quên mật khẩu / kích hoạt)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT, URL `/quan-tri/tai-khoan`.
- Kiểm cả 2 trạng thái đối tác nêu: **Hoạt động** (nút Sửa/Phân quyền/Khóa TK/Vô hiệu hóa) và **Tạm khóa** (cbpd_bn — nút Sửa/Phân quyền/Mở khóa) — cả 2 đều KHÔNG có "Đặt lại mật khẩu".
- `anyResetButtonAnywhere = false` (không nút reset ở bất kỳ trạng thái nào).
- Evidence: `../../reverify-audit/QLTKND_27/web-hanh-dong-active-no-reset.png`, audit `../../reverify-audit/QLTKND_27/audit.md`.

**Kết luận QA**

- `QLTKND_27` KHÔNG phải bug theo SRS v3.5: nút "Đặt lại mật khẩu" đã bị bỏ có chủ đích [STT80 UAT 2026-06-02].
- KHÔNG thể Reject: quan sát "không có nút" của đối tác tái hiện đúng, chỉ tranh chấp expected/spec.
- Điểm expected đối tác lệch spec: kỳ vọng nút hiện khi Active/Tạm khóa là theo đặc tả trước STT80.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận expected của `QLTKND_27` theo SRS v3.5:

- Nút "Đặt lại mật khẩu"/"Đổi MK" đã được BA bỏ 2026-06-02 (STT80). Reset MK nay qua "Gửi lại email kích hoạt" (TK chờ kích hoạt) + tự phục vụ "Quên mật khẩu" (FR-VIII-26).
- Đề nghị cập nhật expected testcase bỏ yêu cầu nút "Đặt lại mật khẩu" — trừ khi BA có yêu cầu khôi phục nút cho admin.
- Verdict QA đề xuất: `Không phải bug theo SRS v3.5` (chờ BA xác nhận với đối tác), không gửi Dev.
<!-- group-8-end -->

---

<!-- group-9-start -->
## Phân quyền chức năng

> **File này để làm gì:** gom testcase QA không tự chốt verdict được vì **SRS tự mâu thuẫn** (body SCR-VIII-04 vs CHANGELOG Pha 5 redesign), kèm đối chiếu + evidence để BA quyết + phản hồi đối tác.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` — đã mở file verify số dòng thực. SRS v3.5 (`input/srs-update-2026-5-5/`).

---

## QLPQCN_02 (và QLPQCN_03) — Màn "Phân quyền chức năng" (SCR-VIII-04): app theo bản redesign panel-theo-module, còn body SRS + kỳ vọng đối tác theo ma trận 6 cột cũ

**Bối cảnh testcase**

- Dòng Excel: 173, mã TC `QLPQCN_02` — đối tác phản ánh màn KHÔNG hiển thị **Bộ chọn vai trò** (kỳ vọng: chọn vai trò → tải ma trận quyền).
- Dòng Excel: 174, mã TC `QLPQCN_03` — đối tác phản ánh ma trận phân quyền KHÔNG hiển thị theo **Cây chức năng** (danh sách cây).
- Nội dung kiểm tra: QTHT mở màn Phân quyền chức năng của 1 vai trò (`/quan-tri/vai-tro/{id}/quyen-han`).
- Expected trong file UAT (đối tác): màn có dropdown "Bộ chọn vai trò" + ma trận quyền tổ chức theo cây chức năng phân cấp với các cột hành động. Đối tác dẫn chứng spec doc `HTPLDN-PTYC-CT-v2.0` §4.10.4.2 (ma trận Phân quyền Chức năng theo Vai trò: Bộ chọn vai trò = Danh sách chọn; Cây chức năng cột trái = Danh sách cây).

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `admin` (vai trò QTHT). Mở `https://18.143.165.120.nip.io/quan-tri/vai-tro/aaaaaaaa-0000-4000-8000-000000000010/quyen-han` (vai trò "Cán bộ Nghiệp vụ Địa phương").
- Màn tiêu đề "Phân quyền vai trò". Quyền hiển thị dạng **collapse panel theo module**: "Báo cáo (11 quyền)", "BIEU_MAU (10 quyền)", "Chi trả (16 quyền)"… — mỗi panel có checkbox nhóm + expand ra danh sách **quyền chi tiết có tên** (Cập nhật báo cáo `update_bao_cao`, Duyệt báo cáo `approve_bao_cao`, Xem bảng điều khiển `read_dashboard`, Công khai thư mục biểu mẫu `publish_thu_muc_bieu_mau`…), mỗi quyền 1 checkbox.
- Đo DOM: `selects: []` → **không có dropdown/bộ chọn vai trò** nào trên màn (vai trò chọn qua điều hướng từ danh sách Vai trò). Không có cột `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất` (`hasActionColumns` = false toàn bộ). 612 checkbox, nút "Quay lại" + "Lưu".
- Env đối tác (`ospgroup.vn`, video QLPQCN_02/03.webm) render **giống hệt**: cùng panel-theo-module, cùng không có dropdown vai trò.
- Evidence: `../../reverify-audit/QLPQCN_02/quyen-han-screen.png`, `../../reverify-audit/QLPQCN_03/quyen-han-grouped-list.png`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-VIII-04 §Thành phần màn hình (body SRS)** — màn là **ma trận 6 cột**:
   - Toolbar có "Dropdown vai trò" (select) — luôn hiển thị.
   - Content "Cây menu (cột trái)" (tree) + 6 cột checkbox `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất`.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1688` (Dropdown vai trò | select | luôn hiển thị)
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1689` (Cây menu cột trái | tree | Phân cấp module)
   - `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1690-1694` (6 cột hành động)

2. Nhưng **CHANGELOG-v3-to-v3.5 §Pha 5 "Tái thiết kế Phân quyền chức năng" (2026-05-08, ✅ BA + PM chốt)** đã **redesign** SCR-VIII-04 sang **1 vùng panel theo module** (bỏ ma trận 6 cột):
   - "SCR-VIII-04 dùng **1 vùng duy nhất** — danh sách collapse panel theo module. Mỗi panel chứa block CRUD compact (6 checkbox) + block đặc thù dọc (các quyền workflow theo 9 nhóm verb)."
   - QUYEN_HAN thêm `module_code`/`module_name` → "UI render panel theo `module_code`, không parse prefix `ma_quyen`". 218 quyền chia **12 module** (BAO_CAO, BIEU_MAU, CHI_TRA, HOI_DAP, DAO_TAO, VU_VIEC, DANH_GIA, QUAN_TRI, TVCS, TV_NHANH, CT_HTPL, TVV_CG).
   - Tổng kết: "1 SCR redesign hoàn chỉnh (SCR-VIII-04: **ma trận 6 cột → 1 vùng panel theo module**)".

   Citation:
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3246` (1 vùng collapse panel theo module)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3262` (UI render panel theo module_code)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3270` (218 quyền / 12 module)
   - `input/srs-update-2026-5-5/CHANGELOG-v3-to-v3.5.md:3304` (ma trận 6 cột → 1 vùng panel theo module)

   → **Body SCR-VIII-04 §Thành phần chưa được đồng bộ với bản redesign đã chốt trong changelog** (cả 3 bản srs-fr-10: input v3.5, Docs v3.5, Docs v4 đều còn giữ ma trận 6 cột). Web hiện tại render **đúng bản redesign panel-theo-module** (khớp `module_code` + 12 module + quyền chi tiết), KHÔNG khớp ma trận 6 cột.

**Câu hỏi cần BA xác nhận**

Màn "Phân quyền chức năng" (SCR-VIII-04) cần theo bản nào?

1. **Hướng 1 — theo body SCR-VIII-04 (ma trận 6 cột cũ):** cần dropdown "Bộ chọn vai trò" trên màn + ma trận cây chức năng × 6 cột `Xem/Thêm/Sửa/Xóa/Phê duyệt/Xuất`. → Web hiện tại **sai thiết kế**, kỳ vọng đối tác **đúng**.
2. **Hướng 2 — theo CHANGELOG Pha 5 redesign (panel theo module, đã BA+PM chốt 2026-05-08):** 1 vùng collapse panel theo module với quyền chi tiết; chọn vai trò qua điều hướng danh sách. → Web hiện tại **đúng bản redesign**, kỳ vọng đối tác (ma trận 6 cột) **dựa trên thiết kế cũ đã bị thay**, cần cập nhật body SRS + báo đối tác.

- Riêng `QLPQCN_02` (không có dropdown vai trò): kể cả theo Hướng 2, changelog chỉ mô tả lại vùng hiển thị quyền, chưa nêu rõ có bỏ dropdown vai trò hay không → BA xác nhận màn redesign có cần dropdown chọn vai trò không, hay chọn vai trò qua điều hướng danh sách là chấp nhận được.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `QLPQCN_02` và `QLPQCN_03`: `BA confirm`.
- **QA nghiêng Hướng 2:** CHANGELOG Pha 5 là quyết định BA+PM sau cùng (2026-05-08, trạng thái "✅ chốt"), thứ bậc `BA duyệt > expected đối tác`. Web đang khớp bản redesign này (panel theo `module_code`, 12 module, quyền chi tiết) → nhiều khả năng web ĐÚNG, kỳ vọng đối tác dựa trên ma trận 6 cột đã bị thay. Nếu BA chọn Hướng 2: cần (a) cập nhật body SCR-VIII-04 §Thành phần cho khớp changelog, (b) phản hồi đối tác rằng thiết kế màn đã đổi sang panel-theo-module, cập nhật lại expected của QLPQCN_02/03.
- Nếu BA chọn Hướng 1: web `Vẫn lỗi`, owner `Dev FE` (dựng lại dropdown vai trò + ma trận 6 cột).

**Quan sát thêm (cùng cụm SCR-VIII-04, để BA cân nhắc chung — QA chưa mở dòng bug riêng vì phụ thuộc cùng 1 quyết định source-truth):**
- Màn `/quyen-han` chỉ có nút "Quay lại" + "Lưu", **không có nút "Reset về mặc định"** (body SCR-VIII-04 comp 10 `srs-fr-10-quan-tri.md:1696`; spec doc đối tác cũng có "Khôi phục về mặc định"). Nếu BA chốt Hướng 1 → thiếu nút này là lỗi; nếu Hướng 2 → cần xác nhận bản redesign có giữ nút Reset không.

<!-- group-9-end -->

