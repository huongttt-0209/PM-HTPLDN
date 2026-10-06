# BA confirmation needed — TVCS Batch C (Màn Chi tiết SCR-X1-02) — 2026-07-21

> **File này để làm gì:** gom các testcase Batch C mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI. Bug có SRS reference rõ → `../../bug-reports/tvcs/Pass-bug-report-tvcs-batchC.md`.
>
> **Môi trường verify:** https://18.143.165.120.nip.io · **Tài khoản:** `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, đơn vị BTP·TW) · **Tool:** Chrome DevTools MCP.
> **SRS:** `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md` (v3.5, bản đồng nhất với `srs-v3.5/`).

---

## QLNDTVVCG_15 (row 283) — Số nhóm accordion (5/6/7) + nhãn nhóm màn Chi tiết TVCS (SRS tự mâu thuẫn)

**Dạng B — SRS tự mâu thuẫn về nhãn nhóm, QA không tự chốt được.**

**Bối cảnh testcase**

- Dòng Excel: 283, mã TC `QLNDTVVCG_15`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn **Chi tiết TVCS** (SCR-X1-02, chế độ xem) → quan sát số nhóm accordion + tên từng nhóm.
- Expected/Actual đối tác (ảnh `QLNDTVVCG_15.jpg`, env `htpldn-uat.ospgroup.vn`, bản **TVCS-20260527-0001 Đã duyệt**):
  - Đối tác thấy **7 nhóm**: Thông tin cơ bản / Nội dung tư vấn / **Vụ việc liên kết** / **Tư liệu pháp luật** / **Trạng thái công khai** / Đánh giá chất lượng / **Nhật ký**.
  - Đối tác kỳ vọng: **5 nhóm**; nhãn "Tư liệu pháp lý liên kết" (không phải "Tư liệu pháp luật"); "Nhật ký thao tác" (không phải "Nhật ký").

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW).
- Mở `https://18.143.165.120.nip.io/tv-chuyen-sau/5eed0008-0000-4000-8000-000000000001` — bản **TVCS-SEED-0001**, trạng thái **Đã duyệt** (khớp đúng trạng thái bản đối tác đang đứng).
- Đếm bằng `evaluate_script` (đọc `.ant-collapse-header`) → **đúng 6 nhóm**, nhãn chính xác:
  `["Thông tin cơ bản", "Nội dung tư vấn", "Tư liệu pháp luật", "Trạng thái công khai", "Đánh giá chất lượng", "Nhật ký"]`
- **KHÔNG có nhóm "Vụ việc liên kết"** → phần "7 nhóm" của đối tác **không tái hiện** trên env này.
- 6 nhóm này = **đúng SRS cho trạng thái Đã duyệt**: 5 nhóm cơ bản (Thông tin cơ bản / Nội dung TV / Tư liệu PL / Đánh giá CL / Nhật ký) + nhóm **Công khai** (chỉ hiển thị khi `trang_thai = DA_DUYET`, BR-PUBLIC-01).
- Evidence: `../../reverify-audit/QLNDTVVCG_15/qlndtvvcg_15-accordion-6nhom-nip.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **§Bố cục tổng quan** của SCR-X1-02, các nhóm accordion dùng **nhãn NGẮN**:
   - "Accordion sections (Thông tin cơ bản / Nội dung TV / **Tư liệu PL** / Đánh giá CL / **Nhật ký**)"

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1133`

2. Nhưng **§Thành phần màn hình** (bảng) lại dùng **nhãn DÀI**:
   - #6 "**Tư liệu PL liên kết** (UC152)" · #8 "**Nhật ký thao tác**" · #8b "**Công khai chuyên trang**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144` (Tư liệu PL liên kết)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1146` (Nhật ký thao tác)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1147` (Công khai chuyên trang)

3. Thêm: chữ **"PL"** trong SRS (dòng 1133/1144) không rõ là "pháp **lý**" hay "pháp **luật**". Tên chức năng FR-X.1-06 = "Quản lý **tư liệu pháp lý** của vụ việc" và §Xử lý dòng 151 "Truy vấn **tư liệu pháp lý** liên quan" → nghiêng về "**pháp lý**". Web đang hiện "Tư liệu pháp **luật**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:151`

**Câu hỏi cần BA xác nhận**

Nhãn chuẩn của các nhóm accordion màn **Chi tiết TVCS** (SCR-X1-02) là gì? Cần thống nhất giữa 2 chỗ SRS đang khác nhau:

1. **Hướng 1 — theo §Bố cục dòng 1133 (nhãn ngắn):** "Tư liệu PL", "Nhật ký". → Web hiện "Nhật ký" **khớp**; "Tư liệu pháp luật" vẫn cần chốt "pháp lý/pháp luật".
2. **Hướng 2 — theo §Thành phần dòng 1144/1146/1147 (nhãn dài):** "Tư liệu pháp lý liên kết", "Nhật ký thao tác", "Công khai chuyên trang" (khớp kỳ vọng đối tác). → Web hiện "Tư liệu pháp luật"/"Nhật ký"/"Trạng thái công khai" **đều lệch**, cần Dev sửa nhãn.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt nhãn chuẩn + số nhóm chuẩn.
- Tạm verdict `QLNDTVVCG_15`: **Cần BA xác nhận**.
- Phần "7 nhóm / nhóm Vụ việc liên kết": **không tái hiện** trên nip.io (web đúng 6 nhóm cho bản Đã duyệt) → không phải lỗi trên env hiện tại; nếu BA cần, đề nghị đối tác kiểm tra lại trên bản build mới.
- Nếu BA chọn Hướng 2 (nhãn dài): các nhãn "Tư liệu pháp luật"/"Nhật ký"/"Trạng thái công khai" trên web là `Vẫn lỗi` (nhãn), owner `Dev FE`.
- Nếu BA chọn Hướng 1 (nhãn ngắn): web cơ bản đúng, chỉ cần chốt "pháp lý" vs "pháp luật".

---

## QLNDTVVCG_17 (row 284) — Nhóm 1 "Cơ quan tiếp nhận" + Nhóm 2 "Tiêu đề/Tóm tắt" màn Chi tiết TVCS

**Dạng A — QA đã kết luận, cần BA phản hồi đối tác.**

**Bối cảnh testcase**

- Dòng Excel: 284, mã TC `QLNDTVVCG_17`.
- Nội dung kiểm tra: CB Nghiệp vụ mở màn **Chi tiết TVCS** (SCR-X1-02, chế độ xem) → đọc trường của Nhóm 1 (Thông tin cơ bản) + Nhóm 2 (Nội dung tư vấn).
- Expected/Actual đối tác (ảnh `QLNDTVVCG_17.jpg`, env `htpldn-uat.ospgroup.vn`, bản TVCS-20260527-0001 Đã duyệt):
  - Nhóm 1 **thiếu "Cơ quan tiếp nhận"** (đối tác kỳ vọng có).
  - Nhóm 2 **thiếu "Tiêu đề" + thừa "Tóm tắt"**: field đầu Nhóm 2 của đối tác ghi nhãn **"Tóm tắt"** (value "Tư vấn").

**Đối chiếu SRS v3.5**

- Nhóm 1 "Thông tin cơ bản" (§Thành phần dòng 1142) gồm: Mã (auto) / DN / Chuyên gia / Lĩnh vực PL / Ngày tư vấn / Ghi chú. **KHÔNG liệt kê trường "Cơ quan tiếp nhận"** cho CB nhập/xem — `don_vi_id` (đơn vị tiếp nhận) là trường tự gán = đơn vị của CB đăng nhập (dòng 118), không phải field trên form/màn chi tiết.
- Nhóm 2 "Nội dung tư vấn" (§Thành phần dòng 1143) gồm: **Tiêu đề** (bắt buộc, max 255) / Nội dung TV chi tiết (Rich Text). Trường chính thức là `tieu_de` — "chính thức hóa từ `tom_tat`" (dòng 114). "Tóm tắt" là tên trường CŨ đã bị thay.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1142` (Nhóm 1 — không có "Cơ quan tiếp nhận")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:118` (don_vi_id auto = đơn vị CB đăng nhập)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1143` (Nhóm 2 — trường "Tiêu đề")
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:114` (`tieu_de` chính thức hóa từ `tom_tat`)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW), bản TVCS-SEED-0001 (Đã duyệt).
- `evaluate_script` trên `<main>`: `hasTieuDe = true`, `hasTomTat = false`, `hasCoQuanTiepNhan = false`.
- Nhóm 1 các trường đọc được: Mã tư vấn / Doanh nghiệp / Lĩnh vực / Chuyên gia / Trạng thái / Ngày bắt đầu / Ngày hoàn thành / Ngày tạo — **không có "Cơ quan tiếp nhận"**.
- Nhóm 2: nhãn field đầu là **"Tiêu đề"** (= "Tư vấn chuyên sâu về hợp đồng thương mại seed"), tiếp theo "Nội dung chi tiết" / "Kết quả" — **KHÔNG có "Tóm tắt"**.
- Evidence: `../../reverify-audit/QLNDTVVCG_17/qlndtvvcg_17-nhom1-nhom2-clean-nip.png`

**Kết luận QA**

- **Ý "Nhóm 2 thiếu Tiêu đề + thừa Tóm tắt": KHÔNG tái hiện** trên nip.io — web hiện đúng nhãn "Tiêu đề" (SRS dòng 114/1143), không còn "Tóm tắt". Bản đối tác quay là build cũ dùng nhãn `tom_tat`. → Phần này web ĐÚNG.
- **Ý "Nhóm 1 thiếu Cơ quan tiếp nhận":** web đúng SRS — SRS §Thành phần dòng 1142 không quy định trường này (don_vi_id auto). Đây là **kỳ vọng đối tác khác SRS** → cần BA chốt.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận cho `QLNDTVVCG_17`: phần "Tiêu đề/Tóm tắt" đã đúng trên bản hiện tại (không phải bug) — đề nghị đối tác kiểm tra lại trên build mới.
- Với "Cơ quan tiếp nhận": BA quyết có bổ sung hiển thị **đơn vị tiếp nhận** ở Nhóm 1 màn Chi tiết hay không.
  - Nếu **CÓ** → cập nhật SRS dòng 1142 + Dev FE bổ sung trường (owner: Dev FE).
  - Nếu **KHÔNG** → cập nhật lại kỳ vọng testcase cho khớp SRS.
- Verdict QA đề xuất: `Cần BA xác nhận` (không gửi Dev cho tới khi BA chốt "Cơ quan tiếp nhận").

---

## QLNDTVVCG_22 (row 286) — Modal Phân công CG: ô "Chuyên môn" trống (—) + chú thích SLA

**Dạng A — QA đã kết luận (reproduce + root cause), cần BA chốt nghĩa trường dữ liệu.**

**Bối cảnh testcase**

- Dòng Excel: 286, mã TC `QLNDTVVCG_22`.
- Nội dung kiểm tra: CB Nghiệp vụ mở bản TVCS trạng thái Tiếp nhận → bấm **Phân công Chuyên gia** → quan sát modal gợi ý CG.
- Expected/Actual đối tác (ảnh `QLNDTVVCG_22.jpg`, env `htpldn-uat.ospgroup.vn`):
  - Modal hiện CG "huongcg" (dropdown ghi lĩnh vực: Đất đai, Hình sự, Lao động, Thuế) nhưng ô **"Chuyên môn" để trống (—)** "dù CG có data".
  - Đối tác kỳ vọng thêm chú thích **"Chuyên gia sẽ được gửi thông báo..."**.

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_03` (CB_NV_TW, BTP·TW), bản **TVCS-20260721-0001 · Tiếp nhận** → mở modal Phân công.
- `evaluate_script` đọc modal: **"Chuyên môn: —"** (tái hiện), **SĐT = 0912280028**, **Email = qa.tvvseed28@htpldn-uat.local** (populate đúng), banner **"SLA: Chuyên gia có 2 ngày làm việc để xác nhận tham gia."** hiển thị.
- API modal load CG (`GET /tu-van-viens?...&loaiTvv=CG&linhVucIds=<record.linhVuc>`) trả 1 CG:
  `hoTen:"QA TVV Seed28 Active"`, **`chuyenNganh: null`**, **`linhVucText: "Thương mại"`**, `dienThoai:"0912280028"`, `email:"qa.tvvseed28@..."`.
- Đối chiếu: nhãn dropdown "QA TVV Seed28 Active — Thương mại" lấy từ **`linhVucText`** (Lĩnh vực). Ô "Chuyên môn" trong bảng chi tiết map vào **`chuyenNganh`** — giá trị `null` → render "—". Vậy app hiển thị **đúng theo dữ liệu**; thứ đối tác tưởng là "data chuyên môn" thực chất là **Lĩnh vực** (trường khác).

**Đối chiếu SRS v3.5**

- Modal Phân công (§Thành phần dòng 1153): "gợi ý TOP 5 CG theo lĩnh vực khớp + tìm CG + ghi chú + **info SLA (2 ngày LV xác nhận)**". → banner SLA **đã có** → thỏa yêu cầu; câu "sẽ được gửi thông báo" không nằm trong SRS.
- "chuyên môn phù hợp lĩnh vực" (dòng 160) + pattern hiển thị chuyên môn khi chọn CG (dòng 1142) — **không định nghĩa** ô "Chuyên môn" đọc từ trường dữ liệu nào (`chuyenNganh` hay `linhVucText`).

**Citation**

- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1153` (modal Phân công — info SLA 2 ngày LV)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:160` (chuyên môn phù hợp lĩnh vực)
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1142` (hiển thị chuyên môn khi chọn CG)

**Câu hỏi cần BA xác nhận**

1. Ô **"Chuyên môn"** trong modal Phân công CG lấy dữ liệu từ trường nào?
   - Nếu là **Lĩnh vực CG** (`linhVucText`, đang có "Thương mại") → hiện đang map sai trường → Dev FE sửa (owner: Dev FE).
   - Nếu là **trường chuyên ngành riêng** (`chuyenNganh`, đang `null`) → app hiển thị "—" là đúng → cần **seed/nhập chuyên ngành cho CG** thì mới có dữ liệu (owner: QA seed / dữ liệu CG), **không phải bug FE**.
2. Có bổ sung câu chú thích **"Chuyên gia sẽ được gửi thông báo..."** vào modal không? (SRS chỉ yêu cầu info SLA — đã có.)

**Đề xuất QA tạm thời**

- Verdict `QLNDTVVCG_22`: **Cần BA xác nhận** — không gửi Dev/không log bug FE cho tới khi BA chốt nghĩa trường "Chuyên môn" (tránh talk-past kiểu prescribe implementation).
- Phần chú thích SLA: web đã thỏa SRS (có banner 2 ngày LV) → không phải thiếu; wording bổ sung tùy BA.
- Evidence: `../../reverify-audit/QLNDTVVCG_22/qlndtvvcg_22-modal-chuyenmon-rong-nip.png`
