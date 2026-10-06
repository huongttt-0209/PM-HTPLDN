# BA confirmation needed — UAT đối tác tuần 2, **vòng 2** — 2026-07-27

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | Phần mềm Hỗ trợ pháp lý doanh nghiệp (PM HTPLDN) |
| **Đợt** | UAT đối tác tuần 2 · **vòng 2** (verify lại các case `Trạng thái 2 = Fail`) |
| **Môi trường verify** | https://18.143.165.120.nip.io |
| **Nguồn đặc tả đối chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25) |
| **Sheet** | tab `UAT_TGPL Doanh Nghiệp-tuần 2` — cột W `Trạng thái dev fix 2` / X `DEV phản hồi lần 2` |
| **Ngày lập** | 2026-07-27 |
| **Vòng 1 của cùng tab** | [`ba-confirmation-needed-week-2.md`](ba-confirmation-needed-week-2.md) |

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác.
> Các case đã có căn cứ SRS rõ ràng đã log ở `bug-reports/` và **không** nằm trong file này.

> **Quy ước citation:** mọi dẫn chiếu dạng `srs-fr-NN-x.md:LINE` đều thuộc thư mục
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Mục **Citation** của từng case ghi đường dẫn đầy đủ.
> Số dòng đã mở file kiểm lại, không lấy từ trí nhớ.

---

## Phạm vi — 4 case, khớp đúng 4 dòng mang `BA confirm` trên sheet

| Mã | Row | Dạng | Case | Verdict cột W | Số câu hỏi con |
|----|----:|:----:|------|---------------|:--------------:|
| **BA-V2-1** | 8 | B | QLKTLBG_02 — bộ cột màn Kho tài liệu / Bài giảng (SCR-III-03) | `BA confirm` | 1 |
| **BA-V2-2** | 53 | B | DKTGMLTVV_03 — bộ trường nhóm "Nghề nghiệp" form Thêm/Sửa TVV (SCR-IV-02) | `Open, BA confirm` | 3 (a·b·c) |
| **BA-V2-3** | 58 | B | QLHSTVV_03 — thành phần thẻ "Hồ sơ" màn chi tiết TVV (SCR-IV-03) | `Open, BA confirm` | 4 (a₁·a₂·b·c) |
| **BA-V2-4** | 68 | A | TDHSTVV_14 — người nhận thông báo khi thẩm định "Không đạt" (FR-IV-06) | `BA confirm, Open` | 4 |

> **Dạng A** = QA đã kết luận được, cần BA phản hồi lại đối tác. **Dạng B** = SRS tự mâu thuẫn / im lặng, QA không tự chốt.

> **3 case mang 2 trạng thái** (`Open, BA confirm`) vì phần đối tác phản ánh cần BA chốt, còn phần QA phát hiện thêm trên
> cùng màn là lỗi thật đã chuyển dev (`BUG-DKTGMLTVV_03`, `BUG-QLHSTVV_03`, `BUG-TDHSTVV_14`).
> Phần đã chuyển dev **không** nằm trong file này.

> **Lưu ý nguồn:** các câu hỏi này cũng đã ghi vào cột **X** sheet tuần 2 (dòng 8, 53, 58, 68) cho đối tác đọc.
> File này là bản đầy đủ cho BA (có dẫn số dòng SRS). BA chốt xong phải cập nhật **cả hai** để không lệch nguồn.

---

## ⚑ Câu hỏi xuyên suốt — trả lời 1 lần là gỡ được 3 case dạng B

*(Mục thêm ngoài template — gom 3 case về một quyết định để BA không phải trả lời rời rạc.)*

**Dữ kiện quyết định:** cột "Kết quả mong đợi" của **cả 3 phiếu** (row 8, 53, 58) đều viết nguyên văn
*"hiển thị … **giống với thiết kế**"* — tức chuẩn đối chiếu mà đối tác dùng là **bản thiết kế màn hình**, còn QA đối chiếu **SRS v3.5**.
Đây là bất đồng **nguồn đặc tả**, QA không có thẩm quyền chọn nguồn.

Cả 3 màn đều lệch so với bảng "Thành phần màn hình" của SRS, nhưng phần lệch **đều có căn cứ ở chỗ khác của chính SRS**:

| Màn | Bảng thành phần SRS | Web thực tế | Căn cứ của phần lệch |
|---|---|---|---|
| SCR-III-03 — Kho tài liệu / Bài giảng | 6 cột | 6 cột (đối tác đòi thêm 3 cột) | FR-III-07 §Outputs `:765` có `khoa_hoc` mà bảng cũng không hiển thị |
| SCR-IV-02 — Thêm/Sửa Tư vấn viên | 9 mục nhóm 2, 5 nhóm | 11 trường nhóm 2, 6 nhóm | FR-IV-03 §Inputs `:304`, `:305`; entity `:155-156`; Phụ lục 1 `:2212-2213` |
| SCR-IV-03 — Chi tiết TVV, thẻ Hồ sơ | 6 nhóm, mô tả gọn `:1556` | thêm 6 mục (phiếu đếm 5 nhóm) | FR-IV-07 `:583`; Phụ lục 1 `:2027` |

**Xin BA chọn 1 trong 2:**

- **(A) Danh sách ĐÓNG** — màn hình chỉ được hiển thị đúng các mục có tên trong bảng thành phần. Mọi trường dôi ra là **lỗi**,
  và SRS phải bổ sung cách người dùng tra dữ liệu bị ẩn đi (xem BA-V2-3b).
- **(B) MÔ TẢ TÓM TẮT** — bảng thành phần chỉ nêu các mục chính; màn hình được hiển thị thêm trường đã có căn cứ ở
  §Inputs/§Outputs/entity/Phụ lục. Phần dôi ra là **đúng**, và các case đối tác báo "thừa trường" phải sửa lại kết quả mong đợi.

---

## BA-V2-1 — QLKTLBG_02 (row 8): bộ cột chuẩn của màn Kho tài liệu / Bài giảng

**Dạng B** · **Verdict:** `BA confirm`

### Bối cảnh testcase

- Dòng Excel: **8**, mã TC `QLKTLBG_02`.
- Nội dung kiểm tra: vai trò **CB_NV_TW** mở màn danh sách Kho tài liệu / Bài giảng, kiểm tra hiển thị bảng danh sách.
- Expected trong file UAT (nguyên văn):
  - "Hệ thống hiển thị bảng danh sách **giống với thiết kế** thành công";
  - "Dữ liệu hiển thị đúng định dạng và trường thông tin";
  - "Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị";
  - "Mặc định: 20 bản ghi/trang."
- Actual đối tác ghi (vòng 2): "Hệ thống hiển thị **thiếu các trường thông tin: Ảnh xem trước, Lĩnh vực, Người tạo**".

### Kết quả verify UI hiện tại

- Verify lại ngày **27/07/2026** qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / vai trò **CB_NV_TW**, đơn vị BTP·TW
  (trùng khít vai trò + đơn vị trong ảnh đối tác).
- Mở URL `https://18.143.165.120.nip.io/dao-tao/bai-giang/danh-sach`.
- Đọc trực tiếp tiêu đề bảng: có **đúng 6 cột** — `Tên bài giảng · Loại tài liệu · Dung lượng · Ngày tạo · Công khai · Thao tác`.
  ⇒ **Quan sát của đối tác là ĐÚNG**: 3 trường họ nêu thật sự không có trong bảng danh sách.
- Mở panel "Xem trước" của một bài giảng: panel có **Công khai · Ngày công khai · Ảnh đại diện · Mô tả công khai** + khung xem trước tệp.
  ⇒ "Ảnh xem trước" **có tồn tại**, chỉ nằm ở panel chứ không phải cột bảng — đúng vị trí SRS quy định.
- Chụp lại ở khung 1440 (đúng khung hình đối tác): bảng bị cuộn ngang, 2 cột "Ngày tạo" + "Công khai" bị đẩy khỏi vùng nhìn
  ⇒ giải thích vì sao ảnh đối tác thấy cột ngày bị cắt.
- Evidence:
  - [`reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-bang-danh-sach-full.png`](reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-bang-danh-sach-full.png) — đủ 6 cột ở khung 1920
  - [`reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-panel-xem-truoc.png`](reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-panel-xem-truoc.png) — panel có Ảnh đại diện
  - [`reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-bang-danh-sach-6-cot.png`](reverify-audit/QLKTLBG_02/QLKTLBG_02-r2-bang-danh-sach-6-cot.png) — khung 1440, bảng cuộn ngang

### Điểm mâu thuẫn trong SRS v3.5

1. Theo **SCR-III-03** và **FR-III-07 §Inputs/§Outputs**, cả 3 trường đối tác đòi đều **không phải cột danh sách**:

   | Trường đối tác đòi | SRS nói gì | Kết luận |
   |---|---|---|
   | Ảnh xem trước | `srs-fr-03-dao-tao.md:1906` — "**Panel chi tiết/preview** hiển thị thêm **Ảnh đại diện** (`anh_dai_dien`)" | SRS đặt ở panel xem trước; web **đã làm đúng** |
   | Lĩnh vực | `srs-fr-03-dao-tao.md:739` — `linh_vuc_ids` chỉ là **Input** khi thêm/sửa; không có ở §Outputs `:760-768`, không được SCR-III-03 nêu là cột | **SRS im lặng.** Web có bộ lọc "Lĩnh vực pháp lý" nhưng không có cột |
   | Người tạo | Không có ở §Inputs `:735-746`, §Outputs `:760-768`, hay SCR-III-03 `:1900-1906` | **SRS im lặng hoàn toàn** |

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1906`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:739`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:760-768`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1900-1906`

2. Nhưng **chính SRS lại không tự nhất quán**, và chuẩn đối chiếu của phiếu thì nằm ngoài SRS:
   - FR-III-07 §Outputs `:765` có trường `khoa_hoc` ("Khóa học liên kết") mà bảng danh sách **cũng không hiển thị**
     ⇒ bộ cột hiện tại không khớp trọn vẹn với §Outputs của chính FR đó.
   - SCR-III-03 `:1904` trỏ sang bản thiết kế `dac-ta-man-hinh-chuc-nang-v2.md — MH-03.3`; **file này không có trong repo**
     (đã tìm toàn bộ, 0 kết quả) → không đối chiếu được kỳ vọng "giống với thiết kế" của phiếu với bản thiết kế đã duyệt.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:765`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1904`

### Câu hỏi cần BA xác nhận

Bộ cột chuẩn của màn danh sách Kho tài liệu / Bài giảng (SCR-III-03) gồm những cột nào?

1. **Hướng 1 — theo SRS hiện hành:** giữ 6 cột, "Ảnh đại diện" nằm ở panel xem trước như `:1906` quy định.
   Xin BA bổ sung câu chữ vào SCR-III-03 để lần sau không tranh luận lại.
2. **Hướng 2 — theo kỳ vọng của phiếu:** bổ sung **Ảnh xem trước / Lĩnh vực / Người tạo** vào bảng danh sách.
   Nếu chọn hướng này, xin chốt luôn trường **"Khóa học liên kết"** (`khoa_hoc`, `:765`) có phải thành cột không.

### Đề xuất QA tạm thời

- Chưa gửi bug này cho Dev cho tới khi BA chốt bộ cột.
- Tạm verdict cho `QLKTLBG_02`: `BA confirm`.
- Nếu BA chọn hướng 1: UI hiện tại **Đúng** → owner `QA cập nhật expected` (sửa kết quả mong đợi của phiếu) + `BA cập nhật SRS`.
- Nếu BA chọn hướng 2: UI hiện tại **Vẫn lỗi** → owner `Dev FE` (bổ sung cột) + `Dev BE` nếu §Outputs phải trả thêm trường.

---

## BA-V2-2 — DKTGMLTVV_03 (row 53): bộ trường nhóm "Nghề nghiệp" form Thêm/Sửa Tư vấn viên

**Dạng B** · **Verdict:** `Open, BA confirm`

> Phần `Open` là một lỗi **khác** trên cùng form — `BUG-DKTGMLTVV_03`: trường "Tổ chức hành nghề chính" bị đặt bắt buộc,
> chặn hẳn luồng đăng ký tư vấn viên tự do (SRS `:1506` + `:307` đều nói tùy chọn). Lỗi này **đã chuyển dev**, không thuộc file này.

### Bối cảnh testcase

- Dòng Excel: **53**, mã TC `DKTGMLTVV_03`.
- Nội dung kiểm tra: vai trò **NHT** (Người hỗ trợ pháp lý) mở form Thêm mới Tư vấn viên, kiểm tra hiển thị **Nhóm 2 — Thông tin nghề nghiệp**.
- Expected trong file UAT (nguyên văn):
  - "Hệ thống hiển thị các trường thông tin **giống với thiết kế**";
  - "Dữ liệu hiển thị đúng định dạng và trường thông tin";
  - "Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị".
- Actual đối tác ghi (vòng 2): "Nhóm 2 — Thông tin chuyên môn: **SRS quy định chỉ hiển thị các trường Trình độ chuyên môn,
  Chuyên ngành đào tạo, Số năm kinh nghiệm. Nhưng hệ thống hiển thị nhiều hơn**".
- **Mâu thuẫn nội tại của chính phiếu:** ở **vòng 1** đối tác báo nhóm 2 **THIẾU** "Chứng chỉ hành nghề" và "Mô tả kinh nghiệm"
  (cột `Kết quả thực tế lần 1`) → dev đã bổ sung theo SRS → Verify Pass. **Vòng 2** lại báo **THỪA** trường.

### Kết quả verify UI hiện tại

- Verify lại ngày **27/07/2026** qua Chrome DevTools MCP, tài khoản UAT `nht_qa_01` / vai trò **NHT**, badge "BTP · DP"
  (trùng khít badge trong ảnh đối tác).
- Mở URL `https://18.143.165.120.nip.io/chuyen-gia-tvv/tao-moi`, mở hết các nhóm thu gọn, đọc toàn bộ nhãn theo nhóm.
- Form có **6 nhóm**. Nhóm 2 "Nghề nghiệp" có **11 trường**: Trình độ học vấn * · Chuyên ngành · Chức vụ · Nơi công tác ·
  Số năm kinh nghiệm · Mô tả kinh nghiệm · Chứng chỉ hành nghề · Số thẻ hành nghề · File thẻ hành nghề (PDF) ·
  Bằng cấp chi tiết · Chứng chỉ chi tiết.
  ⇒ **Quan sát của đối tác là ĐÚNG**: web hiện nhiều trường hơn tài liệu họ cầm.
- Nhóm dôi ra so với SRS `:1476` là nhóm **"Quyết định công bố"** (Số QĐ công bố · Ngày QĐ công bố).
- Bấm Lưu trên form **trống** (không tạo bản ghi nào) để đọc đúng bộ ràng buộc bắt buộc web đang áp:
  **Chuyên ngành** và **Số năm kinh nghiệm** **không** báo lỗi ⇒ web coi là **tùy chọn**, trong khi FR-IV-03 ghi **bắt buộc (Y)**.
- Evidence:
  - [`reverify-audit/DKTGMLTVV_03/DKTGMLTVV_03-r2-nhom2-nghe-nghiep-phan-duoi.png`](reverify-audit/DKTGMLTVV_03/DKTGMLTVV_03-r2-nhom2-nghe-nghiep-phan-duoi.png) — 11 trường nhóm 2
  - [`bug-reports/mang-luoi-tvv/image/BUG-DKTGMLTVV_03-to-chuc-chinh-bat-buoc.png`](bug-reports/mang-luoi-tvv/image/BUG-DKTGMLTVV_03-to-chuc-chinh-bat-buoc.png) — bộ trường bắt buộc khi bấm Lưu trên form trống

### BA-V2-2a — Bộ trường nhóm "Nghề nghiệp" lấy theo SRS hay bản thiết kế?

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-IV-02** và **FR-IV-03**, **không có chỗ nào** giới hạn nhóm 2 còn 3 trường:
   - SCR-IV-02 nhóm 2 liệt kê **9 mục**: Chức vụ (3.0a) · Nơi công tác (3.0b) · Trình độ * (3.1) · Chứng chỉ hành nghề (3.2) ·
     Bằng cấp chi tiết (3.3) · Chứng chỉ chi tiết (3.4) · Số thẻ hành nghề (3.5) · File thẻ hành nghề (3.6) · Mô tả kinh nghiệm (3.7).
   - FR-IV-03 (UC41) §Inputs còn quy định thêm `chuyen_nganh` và `so_nam_kinh_nghiem` là trường **NHT nhập**.
   ⇒ 11 trường trên web **đều có căn cứ trong SRS**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1495-1504`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:296-310`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:323`

2. Nhưng phiếu kiểm thử lấy chuẩn là **bản thiết kế màn hình** ("giống với thiết kế"), và bản thiết kế đó nêu 3 trường.
   Đây là bất đồng **nguồn đặc tả**, không phải bất đồng về sản phẩm.

   **Tiền lệ:** vòng 1 case `DKTGMLTVV_02` đã ghi nhận bản thiết kế **HTPLDN-041** lệch SRS và BA chốt **15/07/2026**
   theo hướng **"SRS > bản thiết kế"**.

**Câu hỏi cần BA xác nhận**

Bộ trường chuẩn của nhóm "Nghề nghiệp" trên form Thêm/Sửa Tư vấn viên lấy theo nguồn nào?

1. **Hướng 1 — theo SRS v3.5:** giữ 11 trường như hiện tại; sửa lại kết quả mong đợi của phiếu.
2. **Hướng 2 — theo bản thiết kế màn hình:** rút còn 3 trường; khi đó phải gỡ lại chính 2 trường dev vừa bổ sung ở vòng 1.

⚠️ **Rủi ro đã xảy ra thật:** không chốt một nguồn duy nhất thì dev còn sửa qua sửa lại — vòng 1 bổ sung, vòng 2 gỡ đi.
Nếu vẫn giữ nguyên tắc "SRS > bản thiết kế" đã chốt 15/07, xin BA xác nhận lại **bằng văn bản** để QA đóng dứt điểm cả vòng 1 lẫn vòng 2.

### BA-V2-2b — "Chuyên ngành" và "Số năm kinh nghiệm": bắt buộc hay tùy chọn?

Đây là **mâu thuẫn nội bộ SRS**, không phải bất đồng với đối tác.

**Điểm mâu thuẫn trong SRS v3.5**

1. FR-IV-03 §Inputs ghi cả hai trường là **bắt buộc (Y)**:
   - `chuyen_nganh | text | **Y** | NHT nhập`
   - `so_nam_kinh_nghiem | number | **Y** | NHT nhập`

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:304`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:305`

2. Nhưng bảng thành phần màn hình SCR-IV-02 nhóm 2 **không liệt kê** hai trường này.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1495-1504`

**Thực tế web:** cả 2 trường hiển thị nhưng để **tùy chọn** — bấm Lưu trên form trống không báo thiếu 2 trường này.

**Câu hỏi cần BA xác nhận**

Hai trường này **bắt buộc** (theo FR-IV-03 `:304`/`:305`) hay **tùy chọn** (theo hành vi hiện tại của web)?
Chốt xong xin sửa cho khớp một trong hai chỗ trong SRS.

### BA-V2-2c — Form Thêm/Sửa Tư vấn viên có 5 nhóm hay 6 nhóm?

**Điểm mâu thuẫn trong SRS v3.5**

1. SCR-IV-02 mô tả biểu mẫu chia **5 nhóm** thu gọn được: Thông tin cá nhân, Thông tin nghề nghiệp, Tổ chức & Mạng lưới,
   File đính kèm, Ghi chú.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1476`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1467`

2. Nhưng 2 trường của nhóm thứ 6 ("Quyết định công bố") lại **có căn cứ** ở entity và mẫu xuất:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:155-156` (entity TU_VAN_VIEN)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2212-2213` (Phụ lục 1 — mẫu xuất)

⇒ Nhiều khả năng SRS thiếu cập nhật chứ không phải web sai, nhưng QA không tự kết luận.

**Câu hỏi cần BA xác nhận**

Nhóm **"Quyết định công bố"** có thuộc form Thêm/Sửa Tư vấn viên không? Nếu có, xin bổ sung vào `:1476`.

### Đề xuất QA tạm thời (cho cả 2a·2b·2c)

- Chưa gửi phần này cho Dev cho tới khi BA chốt nguồn đặc tả. (Phần `Open` — "Tổ chức hành nghề chính" bắt buộc — **đã** gửi dev, độc lập.)
- Tạm verdict cho `DKTGMLTVV_03`: `Open, BA confirm`.
- Nếu BA chọn **SRS**: UI hiện tại **Đúng** ở bộ trường → owner `QA cập nhật expected`; riêng 2b nếu chốt "bắt buộc" thì
  owner `Dev FE` (thêm ràng buộc), nếu chốt "tùy chọn" thì owner `BA cập nhật SRS`.
- Nếu BA chọn **bản thiết kế**: UI hiện tại **Vẫn lỗi** → owner `Dev FE` (gỡ trường) + `BA cập nhật SRS` cho khớp,
  và phải thông báo rằng thay đổi này **đảo ngược** phần dev đã làm ở vòng 1.

---

## BA-V2-3 — QLHSTVV_03 (row 58): thành phần thẻ "Hồ sơ" màn chi tiết Tư vấn viên

**Dạng B** · **Verdict:** `Open, BA confirm`

> Phần `Open` là mục **"Địa bàn"** — `BUG-QLHSTVV_03`. SRS đã **khai tử** field này (`:46`, `:153`), ảnh đối tác cho thấy
> nó vẫn hiển thị ⇒ lỗi thật, **đã chuyển dev**, không thuộc file này.

### Bối cảnh testcase

- Dòng Excel: **58**, mã TC `QLHSTVV_03`.
- Nội dung kiểm tra: vai trò **CB_NV_TW** mở màn chi tiết Tư vấn viên, kiểm tra thẻ "Hồ sơ" (chỉ xem, tổ chức thành 5 nhóm thu gọn).
- Expected trong file UAT (nguyên văn):
  - "Hệ thống hiển thị 5 nhóm **giống với thiết kế**";
  - "Các trường thông tin **giống với thiết kế**, không được chỉnh sửa";
  - "Dữ liệu hiển thị Giá trị hiện tại và đúng định dạng";
  - "Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị".
- Actual đối tác ghi (vòng 2):
  - "Nhóm 2 thông tin nghề nghiệp **thừa trường Số quyết định (công nhận)**";
  - "Nhóm 3 — Tổ chức **thừa trường Địa bàn**".
- Ghi chú bằng chứng: trong ảnh đối tác **cả 2 mục đều rỗng** (`—`) ⇒ chúng hiện ra **không phụ thuộc dữ liệu**,
  tức do bố cục màn hình chứ không do bản ghi.

### Kết quả verify UI hiện tại

- Verify lại ngày **27/07/2026** qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` / vai trò **CB_NV_TW**, badge "BTP · TW"
  (trùng khít vai trò trong ảnh đối tác); có đối chứng thêm bằng `cbnv_dp`.
- Mở URL `https://18.143.165.120.nip.io/chuyen-gia-tvv/<id hồ sơ>`, thẻ "Hồ sơ", đọc toàn bộ nhãn bằng DOM.
- Bản ghi `TVV-BTP-TW-0016` (Chờ kích hoạt tài khoản, **đã phê duyệt**): nhóm Nghề nghiệp **11 mục**, **không có**
  "Số quyết định (công nhận)"; nhóm Tổ chức & Mạng lưới đúng **2 mục** (Tổ chức chính + Đối tác), **không có** "Địa bàn".
- Loại trừ giả thuyết "ẩn vì rỗng": bản ghi này **có** số quyết định công nhận thật (`soQuyetDinh = QĐ-8017/QĐ-BTP`)
  mà màn vẫn không dựng mục nào cho nó.
- Lặp với bản ghi khác trạng thái + khác đơn vị (`TVV-STP-AG-0001`, Đang hoạt động, Sở Tư pháp An Giang), xem bằng cả
  `cbnv_dp` và `cbnv_tw`: kết quả **giống hệt**.
- ⇒ **Chênh lệch quan sát:** ảnh đối tác có 2 mục dôi ra, bản QA kiểm không có. Đã chuyển dev kèm **cả hai ảnh** để dev
  đối chiếu trên bản build của mình.
- Evidence:
  - [`reverify-audit/QLHSTVV_03/QLHSTVV_03-r2-the-ho-so-QA-kiem-lai.png`](reverify-audit/QLHSTVV_03/QLHSTVV_03-r2-the-ho-so-QA-kiem-lai.png) — bản QA kiểm
  - [`bug-reports/mang-luoi-tvv/image/BUG-QLHSTVV_03-the-ho-so-co-muc-dia-ban.jpg`](bug-reports/mang-luoi-tvv/image/BUG-QLHSTVV_03-the-ho-so-co-muc-dia-ban.jpg) — ảnh đối tác

### BA-V2-3a — Bảng thành phần thẻ "Hồ sơ" là danh sách đóng hay tóm tắt?

**Điểm mâu thuẫn trong SRS v3.5**

1. SCR-IV-03 mô tả thẻ "Hồ sơ" nhóm (b) Nghề nghiệp = "(**chức vụ + nơi công tác** + trình độ, chứng chỉ, số thẻ, kinh nghiệm)".
   Danh sách này **không nhắc** "Số quyết định (công nhận)".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1556`

2. Nhưng danh sách đó **cũng không nhắc** Chuyên ngành, Số QĐ công bố, Ngày QĐ công bố, Mô tả kinh nghiệm, Số năm kinh nghiệm,
   Chứng chỉ chi tiết — trong khi **6 mục đó vẫn đang hiển thị** và không ai coi là thừa.
   ⇒ `:1556` **viết tóm tắt chứ không phải danh sách đóng** — nhưng đó là suy đoán của QA, cần BA chốt.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:155-156`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:304-305`

3. **Lệch ngay ở SỐ NHÓM — điểm này chưa ai nêu, QA phát hiện khi kiểm lại số dòng.**
   Kết quả mong đợi của phiếu ghi *"hiển thị **5 nhóm** giống với thiết kế"*, và vòng 1 đối tác cũng ghi actual là
   *"**5 nhóm** thông tin không giống với thiết kế"*. Nhưng `:1556` viết rõ **"6 nhóm thu gọn được, chỉ đọc"**,
   liệt kê (a) Thông tin cá nhân · (b) Nghề nghiệp · (c) Tổ chức · (d) Lĩnh vực · (e) File đính kèm ·
   **(f) Thông tin công khai — "chỉ hiển thị khi `cong_khai=1`"**.

   ⇒ Nhóm (f) là **nhóm có điều kiện**: hồ sơ **chưa công khai** sẽ chỉ thấy **5 nhóm**. Rất có thể "5 nhóm" trong phiếu
   chính là trường hợp chưa công khai, tức **không bên nào sai** — nhưng cần BA xác nhận thay vì để hai bên đếm lệch nhau qua từng vòng.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1556`

**Câu hỏi cần BA xác nhận**

1. Bảng thành phần thẻ "Hồ sơ" (`:1556`) là **danh sách đóng** (chỉ được hiển thị đúng các mục liệt kê) hay **mô tả tóm tắt**
   (được hiển thị thêm các trường khác của hồ sơ)? Hiện web hiển thị thêm 6 mục ngoài danh sách.
2. Số nhóm chuẩn của thẻ "Hồ sơ" là **6** (theo `:1556`, trong đó nhóm "Thông tin công khai" chỉ hiện khi hồ sơ đã công khai)
   hay **5** như kết quả mong đợi của phiếu? Nếu là 6-có-điều-kiện, xin sửa lại kết quả mong đợi để hai bên không đếm lệch tiếp.

### BA-V2-3b — "Số quyết định (công nhận)" có hiển thị trên thẻ Hồ sơ không? Nếu không thì tra ở đâu?

**Điểm mâu thuẫn trong SRS v3.5**

1. Trường này **hợp lệ và bắt buộc**, không phải trường lạ:

   | Nội dung | Dẫn chiếu |
   |---|---|
   | FR-IV-07 — `so_quyet_dinh` là trường **bắt buộc nhập** khi Cán bộ Phê duyệt duyệt hồ sơ | `:583` + `:604` |
   | Mã lỗi `ERR-PD-05` khi thiếu số quyết định | `:616` |
   | Phụ lục 1 — `so_quyet_dinh_cong_nhan` "Số QĐ công nhận (FR-IV-07)" | `:2027` |

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:583`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:604`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:616`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2027`

2. Nhưng bảng thành phần thẻ Hồ sơ `:1556` không nêu tên nó, **và bản QA kiểm cũng không hiển thị nó ở bất kỳ nhóm nào**
   dù dữ liệu có thật ⇒ hiện không có đường nào tra trường này trên màn chi tiết.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1556`

**Câu hỏi cần BA xác nhận**

Nếu `:1556` là danh sách đóng và trường này **không** được hiển thị trên thẻ Hồ sơ — người dùng tra số quyết định công nhận
của một tư vấn viên **ở đâu**? Đây là dữ liệu pháp lý bắt buộc nhập khi phê duyệt.

### BA-V2-3c — Xác nhận lại nguyên tắc "bỏ địa bàn của Tư vấn viên" ở v3.5

Mục này **không tranh cãi** — chỉ xin xác nhận để dev gỡ dứt điểm.

| Nội dung | Dẫn chiếu |
|---|---|
| "Ghi chú v3.1 — bỏ TVV_DIA_BAN: Theo NĐ 77/2008 Điều 19, Thẻ TVV có hiệu lực **toàn quốc** — pháp luật không giới hạn TVV theo địa bàn. Hệ thống **bỏ field `dia_ban_ids[]`** và bảng junction TVV_DIA_BAN" | `:46` |
| Entity dòng 19: `~~dia_ban_ids~~` — "**Bỏ field này**" | `:153` |
| Bộ lọc "địa bàn" ở màn danh sách phải hiểu là lọc theo **đơn vị công nhận**, không phải địa bàn của TVV | `:233` |

Citation:
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:46`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:153`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:233`

**Câu hỏi cần BA xác nhận**

Nguyên tắc bỏ địa bàn của Tư vấn viên còn giữ nguyên ở v3.5 chứ?

### Đề xuất QA tạm thời (cho cả 3a·3b·3c)

- Chưa gửi phần 3a/3b cho Dev cho tới khi BA chốt. (Phần `Open` — mục "Địa bàn" — **đã** gửi dev, độc lập.)
- Tạm verdict cho `QLHSTVV_03`: `Open, BA confirm`.
- Nếu BA chọn **danh sách đóng**: UI hiện tại **Vẫn lỗi** → owner `Dev FE` (gỡ mục dôi ra) + `BA cập nhật SRS` bổ sung
  đường tra "Số quyết định (công nhận)".
- Nếu BA chọn **mô tả tóm tắt**: UI hiện tại **Đúng** ở phần "Số quyết định" → owner `QA cập nhật expected`;
  riêng mục "Địa bàn" vẫn là lỗi độc lập, giữ nguyên với `Dev FE`.
- Câu 3c: câu trả lời "còn giữ nguyên" chỉ để dev đóng `BUG-QLHSTVV_03` dứt điểm, không đổi verdict.

---

## BA-V2-4 — TDHSTVV_14 (row 68): ai nhận thông báo khi thẩm định kết luận "Không đạt"

**Dạng A** · **Verdict:** `BA confirm, Open`

> Phần `Open` là lỗi phụ QA phát hiện kèm — `BUG-TDHSTVV_14` (Minor): thư báo **từ chối** lại mang tiêu đề trong thân thư là
> "✅ Phê duyệt: Hồ sơ bị từ chối". Lỗi này **đã chuyển dev**, không thuộc phạm vi câu hỏi BA bên dưới.

### Bối cảnh testcase

- Dòng Excel: **68**, mã TC `TDHSTVV_14`.
- Nội dung kiểm tra: vai trò **CB_NV_TW** gửi kết quả thẩm định với kết luận **"Không đạt"** trên màn chi tiết Tư vấn viên, thẻ Thẩm định.
- Expected trong file UAT (nguyên văn): "Hệ thống chuyển hồ sơ sang trạng thái **"Từ chối"**, ghi nhận thời điểm và người từ chối,
  **gửi thông báo kèm lý do đến Người hỗ trợ**, lưu vết thao tác, hiển thị thông báo "Đã từ chối hồ sơ"."
- Actual đối tác ghi (vòng 2): "**Người hỗ trợ không nhận được thông báo kèm lý do**".
- Bằng chứng: `TDHSTVV_13_v2.webm` (số hiệu tệp lệch một bậc — đối chiếu theo nội dung).
  **Khoảng trống của bằng chứng:** video không chứng minh tài khoản NHT được kiểm là người đã gửi chính hồ sơ đó, và không kiểm hộp thư.
  QA đã bịt cả hai khoảng trống này.

### Đối chiếu SRS v3.5

- Khi kết luận KHÔNG ĐẠT, đặc tả chỉ định người nhận thông báo là **TVV/CG (chủ hồ sơ)** — **không** nêu tên Người hỗ trợ
  ở bất kỳ dòng nào của luồng này (`:522` §Processing bước 6, `:548` §Postconditions, `:2325` bảng chuyển trạng thái SM-TVV).
- Kênh gửi được đặc tả xác định là **email đã khai trên hồ sơ** (`:595`).
- Đặc tả yêu cầu chuyển trạng thái **TU_CHOI** và **ghi lý do** (`:522`, `:2325`).
- Ứng viên bị từ chối ở bước thẩm định **chưa có tài khoản** trong hệ thống: tài khoản chỉ được cấp khi Cán bộ Phê duyệt
  duyệt hồ sơ (CHO_PHE_DUYET → CHO_KICH_HOAT, `:2326`).
- Đặc tả **không** quy định câu chữ của thông báo hiện ra sau khi bấm "Gửi KQ".

### Citation

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:522`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:548`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:595`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2325`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2326`

### Kết quả verify UI hiện tại

- Verify lại ngày **27/07/2026** (15:28–15:40) qua Chrome DevTools MCP, tài khoản UAT `nht_qa_tw` (**NHT**, Cục Bổ trợ tư pháp)
  + `cbnv_tw` (**CB_NV_TW**, cùng đơn vị).
- Mở URL `https://18.143.165.120.nip.io/chuyen-gia-tvv/<id hồ sơ>` (thẻ Thẩm định) và `https://18.143.165.120.nip.io/thong-baos`.
- **Bịt khoảng trống của video:** cho **chính tài khoản NHT** tạo hồ sơ `TVV-BTP-TW-0021` ⇒ quan hệ "Người hỗ trợ ↔ hồ sơ"
  là chắc chắn, không còn nghi ngờ như trong video đối tác.
- Bấm "Gửi KQ" với kết luận KHÔNG ĐẠT + lý do: trạng thái **DANG_THAM_DINH → TU_CHOI** (phiên bản 2 → 3);
  dữ liệu hồ sơ lưu đúng nguyên văn lý do + thời điểm thẩm định; hộp thông báo hiện **"Đã lưu kết quả thẩm định"**
  (số hộp cùng tồn tại tối đa = 1 ⇒ không phải lỗi hiện thông báo trùng).
- Màn **Thông báo** của `nht_qa_tw` sau thao tác: vẫn đúng **1** mục cũ ("Kích hoạt tài khoản…" 12/07/2026), **không** có
  thông báo từ chối ⇒ **giống hệt màn hình đối tác quay được**.
- Hộp thư hệ thống: **có** một thư mới đúng thời điểm bấm "Gửi KQ", người nhận là **email khai trên hồ sơ ứng viên**
  (`qa.tvv.tdhstvv14.r2@htpldn.gov.vn`), tiêu đề "Hồ sơ bị từ chối", nội dung **kèm nguyên văn lý do**.
  ⇒ Thông báo kèm lý do **có được gửi**, chỉ là gửi cho **chủ hồ sơ qua email**, không phải cho Người hỗ trợ trong ứng dụng.
- Lỗi phụ đọc được từ chính thư đó: tiêu đề trong thân thư là **"✅ Phê duyệt: Hồ sơ bị từ chối"** — chữ "Phê duyệt" + dấu tích xanh
  trên một thư báo **từ chối**.
- Evidence:
  - [`bug-reports/mang-luoi-tvv/image/TDHSTVV_14-r2-nht-thong-bao-khong-co-tu-choi.png`](bug-reports/mang-luoi-tvv/image/TDHSTVV_14-r2-nht-thong-bao-khong-co-tu-choi.png) — màn Thông báo của NHT sau thao tác
  - [`bug-reports/mang-luoi-tvv/image/TDHSTVV_14-r2-doi-tac-man-thong-bao-nht.jpg`](bug-reports/mang-luoi-tvv/image/TDHSTVV_14-r2-doi-tac-man-thong-bao-nht.jpg) — khung hình t≈44s trong video đối tác

### Kết luận QA

- `TDHSTVV_14`: **quan sát của đối tác ĐÚNG SỰ THẬT**, nhưng **không vi phạm dòng đặc tả nào** ⇒ không phải `Open`,
  và cũng **không** được `Reject` (họ không thao tác sai, không hiểu sai luồng).
- Web hiện tại **đúng SRS** ở cả 4 điểm kiểm được: người nhận (chủ hồ sơ), kênh (email đã khai), trạng thái (TU_CHOI), ghi lý do.
- Điểm đối tác kỳ vọng — "gửi thông báo đến **Người hỗ trợ**" — là kỳ vọng **nằm ngoài đặc tả**: `:522`, `:548`, `:2325`
  đều chỉ nêu chủ hồ sơ.
- Hệ quả thực tế cần BA để mắt: ứng viên bị từ chối chưa có tài khoản (`:2326`), nên **trong ứng dụng không vai trò nào**
  nhìn thấy kết quả từ chối — kể cả Người hỗ trợ đã nộp hồ sơ thay. Đặc tả chưa nói về điểm này.
- Lỗi thật duy nhất tìm được ở luồng này là **nội dung thư** (`BUG-TDHSTVV_14`, Minor) — đã chuyển dev.

### Nội dung đề xuất BA phản hồi đối tác

Đề nghị cập nhật kết quả mong đợi của `TDHSTVV_14` theo SRS v3.5, sau khi BA chốt 4 điểm sau:

1. Khi Cán bộ Nghiệp vụ kết luận **Không đạt**, **Người hỗ trợ pháp lý đã nộp hồ sơ** có phải nhận thông báo kèm lý do không?
   Đặc tả (`:522`, `:548`, `:2325`) chỉ nêu **chủ hồ sơ**.
2. Nếu **có**, thông báo cho Người hỗ trợ đi kênh nào — thông báo trong ứng dụng, email, hay cả hai?
3. Ứng viên bị từ chối ở bước thẩm định **chưa có tài khoản** (`:2326`). Vậy kết quả từ chối có cần hiện ở **thông báo trong ứng dụng**
   cho một vai trò nào đó (Người hỗ trợ / Cán bộ Nghiệp vụ) để còn theo dõi được không?
4. Thông báo hiện sau khi bấm "Gửi KQ" với kết luận Không đạt đang là **"Đã lưu kết quả thẩm định"**, trong khi phiếu mong đợi
   câu phản ánh đúng việc hồ sơ đã bị từ chối. Đặc tả không quy định câu chữ này — BA chốt theo hướng nào?

- Verdict QA đề xuất: `Cần BA xác nhận` cho ý chính (**không** gửi Dev); riêng lỗi nội dung thư đã gửi Dev — owner `Dev BE`.
- Nếu BA chốt "chỉ chủ hồ sơ" (giữ nguyên đặc tả): sửa kết quả mong đợi của phiếu → owner `QA cập nhật expected`.
- Nếu BA chốt "phải báo cả Người hỗ trợ": UI hiện tại **Vẫn lỗi** → owner `Dev BE` (thêm người nhận) + `BA cập nhật SRS` `:522`/`:548`/`:2325`.
- Dữ liệu để lại đối chiếu: `TVV-BTP-TW-0021 — QA TVV TDHSTVV14 R2` (Cục Bổ trợ tư pháp, trạng thái **Từ chối**, lý do đã ghi).

---

## Việc QA sẽ làm sau khi BA chốt

1. Cập nhật **kết quả mong đợi** của 4 test case (row 8, 53, 58, 68) cho khớp kết luận của BA.
2. Cập nhật cột **W / X** sheet tuần 2 — đổi `BA confirm` sang `Open` hoặc `Reject` theo hướng đã chốt.
3. Nếu BA chốt theo hướng web sai → log bug bổ sung, chuyển dev.
4. Nếu BA chốt theo hướng SRS thiếu/sai → mở entry ở [`tasks/srs-contradictions.md`](../../../tasks/srs-contradictions.md).

## Tài liệu chi tiết từng case

| Case | Audit đầy đủ (phép đo + đối chiếu SRS) | Bảng đối chiếu điều kiện (0 GAP) |
|---|---|---|
| QLKTLBG_02 | [`audit.md`](reverify-audit/QLKTLBG_02/audit.md) | [`cond`](cond/QLKTLBG_02-r2.md) |
| DKTGMLTVV_03 | [`audit.md`](reverify-audit/DKTGMLTVV_03/audit.md) | [`cond`](cond/DKTGMLTVV_03-r2.md) |
| QLHSTVV_03 | [`audit.md`](reverify-audit/QLHSTVV_03/audit.md) | [`cond`](cond/QLHSTVV_03-r2.md) |
| TDHSTVV_14 | [`audit.md`](reverify-audit/TDHSTVV_14/audit.md) | [`cond`](cond/TDHSTVV_14-r2.md) |

---

## Phụ lục — 2 ghi nhận KHÔNG thuộc 4 case trên (không tính vào phạm vi BA confirm)

Hai điểm dưới đây QA gặp khi soi, **không chặn verdict case nào** và **không được đánh `BA confirm`** trên sheet.
Ghi lại để BA để mắt khi rà soát tài liệu.

| # | Nội dung | Case (verdict) |
|---|---|---|
| P1 | **Mâu thuẫn SRS về luồng Import Excel:** `srs-fr-03-dao-tao.md:443` + `:475` mô tả import Excel là 1 trong 3 cách đăng ký, nhưng `:1683` (CSV UC22/UC23 v1.1) ghi Cán bộ Nghiệp vụ **không** có luồng này. Web **đang cho** CB NV nút Import Excel. Chốt hướng nào cũng không đổi verdict (lỗi đọc sai ô Email vẫn là lỗi), chỉ đổi phạm vi fix | DKTGKH_12 (row 3) — `Open` |
| P2 | **Nhãn "Đơn vị quản lý":** `srs-fr-04-chuyen-gia-tvv.md:1494` ghi nhãn có dấu sao bắt buộc, web hiển thị không có dấu sao. Trường này chỉ đọc + tự điền nên không ảnh hưởng nghiệp vụ — nên chốt một quy ước chung cho toàn hệ thống thay vì xử lý từng màn | DKTGMLTVV_02 (row 52) — `Reject` |
