# BA confirmation needed — tab UAT tuần 2 (verify vòng 1) — 2026-08-03

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được**, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh.
> **Đây là file DUY NHẤT của tuần 2** — mọi luồng gộp về đây, không tách file theo luồng.

> **Phạm vi:** **8 TC** của tab `UAT_TGPL Doanh Nghiệp-tuần 2`, sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` — rows **116, 120, 122, 123, 125, 126, 135, 145**.
> Danh sách này lấy bằng cách **rà toàn bộ 146 dòng của tab** và lọc ra mọi dòng mang nhãn `BA confirm`, không phải gom tay theo trí nhớ.
> **Một ngoại lệ có chủ đích:** row **127 `NHSYC_01`** mang `BA confirm` ở cột **của dev** (`Trạng thái dev fix 1`) nhưng verdict QA là `Reopen` → tách xuống **Phụ lục A**, không tính vào 8 TC.
> **Phân dạng:** 7 TC **dạng B** (đặc tả tự mâu thuẫn / hai bản tài liệu chỏi nhau / đặc tả không quy định → BA chốt đâu là nguồn chuẩn) · 1 TC **vừa A vừa B** (`QLLSHTCTVV_04`). **Dạng A** = kỳ vọng của đối tác lệch SRS trong khi web bám đúng SRS.
> **Môi trường verify:** `https://18.143.165.120.nip.io` · bản dựng **HTPLDN V1.0.5** · verify ngày **03/08/2026** qua Chrome DevTools MCP.
> **Nguồn SRS quote số dòng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — đã mở file verify từng số dòng ngày 03/08/2026, không dùng số dòng từ trí nhớ.

> **⚠️ Cách đọc case hỗn hợp — xin BA lưu ý:** 4/8 TC là case gộp nhiều ý, trong đó **chỉ một phần** cần BA. Phần còn lại là **lỗi đã chứng minh tái hiện, đã log bug, dev sửa được ngay — KHÔNG phải chờ BA**. Mỗi mục như vậy có khối **"Phần KHÔNG chờ BA"** liệt kê rõ mã bug. Trên sheet, cả dòng mang nhãn `BA confirm`, nên nếu dev lọc theo nhãn sẽ bỏ sót các bug đó — khối này chính là chỗ bù lại.

---

## LUỒNG 1 — Đào tạo, tập huấn (3 TC)

### KTDGKQHT_02 — Tab "Kết quả kiểm tra" (chi tiết Khóa học): 4 trường số buổi thuộc Outputs UC24 nhưng không có trong đặc tả cột của tab nào

**Bối cảnh testcase**

- Dòng Excel: **116**, mã TC `KTDGKQHT_02`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ mở màn chi tiết Khóa học → tab "Kết quả kiểm tra", đọc tiêu đề các cột của bảng học viên.
- Expected trong file UAT: tab "Kết quả kiểm tra" hiển thị 4 cột **Số buổi có mặt** · **Số buổi vắng có phép** · **Số buổi vắng không phép** · **Tổng số buổi**.
- Actual đối tác ghi: tab không có 4 cột đó.

**Kết quả verify UI hiện tại**

- Verify lại ngày 03/08/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (vai trò CB_NV_TW, đơn vị Cục Bổ trợ tư pháp — trùng vai trò + cấp của đối tác).
- Tiền đề đã tự dựng cho khớp điều kiện đối tác: khóa học trạng thái **Đang diễn ra**, có học viên, lịch học **3 buổi**, đã điểm danh **1 buổi**.
- Tab "Kết quả" có đúng **10 cột**: STT · Họ tên · Email · Số điện thoại · Đơn vị · **Chuyên cần** · **Điểm kiểm tra** · Kết quả · Xếp loại · Ghi chú.
- Đã **cuộn hết thanh ngang** (phần khuất 187px, cột khuất duy nhất là "Ghi chú") ⇒ loại trừ khả năng 4 cột bị che.
- Bộ cột **bất biến** ở cả 3 trạng thái khóa học: Đang diễn ra · Đã kết thúc · Hoàn thành.
- Kiểm chéo tab "Điểm danh": chỉ có **7 cột** (STT · Họ tên · Email · Số điện thoại · Đơn vị · Trạng thái · Ghi chú) — **cũng không có** 4 trường đó.
- ⇒ **Quan sát của đối tác là ĐÚNG.** Lập luận trước đó cho rằng "4 cột thuộc tab Điểm danh" **không khớp thực tế đo được**.
- Evidence: `../image/KTDGKQHT_02-web-tab-ketqua-dangdienra.png` · `../image/KTDGKQHT_02-web-tab-ketqua-cuonhet-phai.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **đặc tả màn hình SCR-III-02**, 4 trường này **không thuộc tab nào**:
   - Tab 5 "Kết quả kiểm tra" liệt kê cột: *STT · Họ tên · Email · Số điện thoại · Đơn vị · Đề kiểm tra · Điểm · Xếp loại · Kết quả · Ghi chú* — không có 4 trường số buổi.
   - Tab 4 "Điểm danh" liệt kê cột: *STT · Họ tên · Email · Số điện thoại · Đơn vị · Buổi học · Trạng thái điểm danh · Ghi chú* — cũng không có.
   - Mục Acceptance Criteria của FR-III-05 không có tiêu chí nào đòi hiển thị 4 trường này.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1901`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1896`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:628`

2. Nhưng **§Outputs của chính FR-III-05 (UC24)** lại liệt kê đủ 4 trường, và §Màn hình gắn UC24 cho đúng 2 tab nói trên:
   - `so_buoi_co_mat` (Số buổi có mặt) · `so_buoi_vang_phep` (Số buổi vắng có phép) · `so_buoi_vang_khong_phep` (Số buổi vắng không phép) · `tong_buoi` (Tổng số buổi).
   - §Màn hình: *"SCR-III-02 (chi tiet Khoa hoc — Tab 3 'Lich hoc & Diem danh' + Tab 4 'Ket qua kiem tra')"* ⇒ UC24 phủ đúng 2 tab mà cả 2 đều không liệt kê 4 trường.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:600-603`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:520`

**Thực tế phần mềm đang làm gì với 4 trường này**

- "Số buổi có mặt" + "Tổng số buổi": **đã có** dữ liệu, được **gộp** hiển thị trong một ô "Chuyên cần" dạng `x/y (z%)`, và có trong file kết quả xuất ra.
- "Số buổi vắng có phép" + "Số buổi vắng không phép": **chưa có ở bất kỳ đâu** trên giao diện lẫn file xuất.

**Câu hỏi cần BA xác nhận**

Bốn trường số buổi tại §Outputs UC24 cần được hiểu theo hướng nào?

1. **Hướng 1 — theo §Outputs (`:600-603`) + §Màn hình (`:520`):** 4 trường là dữ liệu đầu ra bắt buộc của UC24, phải hiển thị thành **cột riêng** trên tab "Kết quả kiểm tra". ⇒ web hiện tại **thiếu 4 cột**.
2. **Hướng 2 — theo đặc tả cột (`:1901` / `:1896`) + AC (`:628`):** danh sách cột là **danh sách đóng**, §Outputs chỉ mô tả dữ liệu tầng nghiệp vụ chứ không ép hiển thị. ⇒ web hiện tại **đúng**, cần sửa lại expected của testcase.

Kèm 2 câu hỏi phụ, dù chọn hướng nào cũng cần trả lời:

- **(a)** Việc **gộp** Số buổi có mặt + Tổng số buổi + % chuyên cần vào một ô "Chuyên cần" có được chấp nhận thay cho các cột riêng không?
- **(b)** Hai trường "Số buổi vắng có phép" / "Số buổi vắng không phép" (`:601-602`) hiện **chưa có ở đâu** — **bổ sung vào app** hay **gỡ khỏi §Outputs** của UC24?

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `KTDGKQHT_02`: `Cần BA xác nhận` (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: UI hiện tại là `Vẫn lỗi` — owner `Dev FE` (bổ sung cột) và có thể cả `Dev BE` nếu 2 trường vắng phép/không phép chưa được tính.
- Nếu BA chọn **hướng 2**: UI hiện tại **không phải lỗi** — owner `QA update expected` cho `KTDGKQHT_02`; nhưng vẫn cần trả lời câu (b) vì §Outputs đang liệt kê 2 trường mà hệ thống không hề sinh ra.

---

### PDKHDTTH_04 — Phê duyệt kế hoạch đào tạo khác đơn vị: hệ thống chặn đúng nhưng không cho người dùng biết lý do

**Bối cảnh testcase**

- Dòng Excel: **120**, mã TC `PDKHDTTH_04`.
- Nội dung kiểm tra: Cán bộ phê duyệt **khác cấp/khác đơn vị** mở kế hoạch đào tạo đang "Chờ duyệt" và bấm Phê duyệt.
- Expected trong file UAT: hệ thống chặn **và hiển thị thông báo** cho biết lý do (đối tác mong đợi câu *"Không có quyền phê duyệt kế hoạch này"*).
- Actual đối tác ghi: bị chặn nhưng **không có thông báo nào** báo lý do.

**Kết quả verify UI hiện tại**

- Verify lại ngày 03/08/2026 qua Chrome DevTools MCP, tài khoản UAT `cbpd_tw_01` (vai trò CB_PD_TW, cấp Trung ương). *(`cbpd_tw` đăng nhập lỗi 401 → đã fallback đúng vai trò + đúng cấp.)*
- Tiền đề đã tự dựng: kế hoạch `KH-20260803-0004` do đơn vị **cấp Địa phương** lập, trạng thái **Chờ duyệt**. Kiểm thêm biến thể kế hoạch cấp **Bộ ngành** — kết quả như nhau.
- **Phần hệ thống làm ĐÚNG:** kế hoạch không bị duyệt, giữ nguyên "Chờ duyệt", không ghi nhận người duyệt.
- **Phần đúng như đối tác phản ánh:** màn hình **không hiện bất kỳ thông báo nào**. Đo **2 lần**, cả 2 đều **0 request → 0 thông báo**; mọi kênh hiển thị khác (`ant-alert`, `[role=alert]`, lỗi inline trong form, hộp thoại lỗi) đều rỗng.
- **Nguyên nhân quan sát được:** giao diện **ẩn hẳn** nút "Phê duyệt"/"Từ chối" với vai trò khác đơn vị — thanh hành động rỗng, không có phần tử nào khớp kể cả node ẩn. Nên thao tác không phát sinh, và thông báo của máy chủ không bao giờ tới người dùng.
- **Đối chứng loại trừ lỗi phép đo:** cùng tài khoản đó, với kế hoạch **cùng đơn vị**, nút vẫn hiện và duyệt được bình thường — **1 request → 1 thông báo "Đã phê duyệt"**.
- **Kiểm bằng phương pháp thứ hai (gọi thẳng máy chủ):** trả `HTTP 403`, mã `ERR-PERM-III-15-02`, message tiếng Việt rõ ràng *"Người duyệt phải cùng đơn vị với kế hoạch"* ⇒ **máy chủ CÓ sinh thông báo, giao diện không hiển thị**.
- Evidence: `../bug-reports/dao-tao/image/BUG-PDKHDTTH_04-03-khac-cap-DP-khong-co-nut-khong-co-thong-bao.png` · đối chứng `../bug-reports/dao-tao/image/BUG-PDKHDTTH_04-02-doi-chung-cung-don-vi-TW-co-nut-Phe-duyet.png` · `../bug-reports/dao-tao/image/BUG-PDKHDTTH_04-04-doi-chung-cung-don-vi-duyet-thanh-cong.png`

**Điểm mâu thuẫn trong SRS v3.5**

> Lưu ý: **việc chặn là ĐÚNG SRS** — phần này không tranh chấp, QA không log lỗi. Tranh chấp chỉ nằm ở chỗ **có phải báo cho người dùng biết lý do hay không**.

1. Theo **FR-III-15 + BR-AUTH-05**, chặn duyệt khác đơn vị là đúng, và FR-III-15 **không quy định** thông báo nào cho tình huống này:
   - §Preconditions: *"CB PD đã đăng nhập, KH ở CHO_DUYET, **CB PD cùng đơn vị**"*.
   - §Processing: *"Kiểm tra quyền + cùng đơn vị → Duyệt/Từ chối → Thông báo CB NV → Ghi nhật ký"*.
   - BR-AUTH-05: *"Phê duyệt cùng đơn vị (strict). CB PD chỉ duyệt bản ghi do CB NV cùng đơn vị tạo"*.
   - Toàn bộ FR-III-15 **không có mục Error Handling**, không có mã lỗi nào cho ca "duyệt khác đơn vị".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1217`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1221`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1208` (mở đầu FR-III-15 — đọc hết mục, không có Error Handling)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5480` (BR-AUTH-05)

2. Nhưng **hai chức năng anh em cùng file đều CÓ thông báo** cho đúng tình huống này, còn đặc tả màn hình Kế hoạch lại **không nêu điều kiện đơn vị**:
   - `ERR-CTDT-PD-01` — *"CB PD phê duyệt CTDT khác đơn vị"* → message *"Không có quyền phê duyệt CTDT của đơn vị khác"*.
   - `ERR-KH-PD-03` — *"CB PD phê duyệt Khóa học khác đơn vị"* → message *"Không có quyền phê duyệt Khóa học của đơn vị khác"*.
   - ⇒ Riêng **Kế hoạch đào tạo** không có mã lỗi tương ứng, dù cùng một tình huống nghiệp vụ.
   - Đặc tả màn hình SCR-III-00, dòng "Hành động": *"Phê duyệt + Từ chối (Chờ duyệt — CB PD)"* — điều kiện chỉ gồm **trạng thái + vai trò**, **không** nêu điều kiện cùng đơn vị ⇒ đọc theo dòng này thì nút **phải hiện** với mọi CB PD, và khi bấm mới báo lỗi.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:277`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:283`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1774`

3. Quy ước giao diện **M-05** thường được viện dẫn để bảo vệ cách "ẩn nút", nhưng **phạm vi của nó là menu, không phải nút thao tác**:
   - Nguyên văn: *"**Hiển thị theo quyền** — **menu item** chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. Ẩn (không disable) nếu không có quyền"*.
   - ⇒ M-05 nói về **menu item**. Áp nó cho nút "Phê duyệt" trong màn chi tiết là **suy rộng ngoài phạm vi câu chữ** — cần BA xác nhận có được suy rộng hay không.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:683`

**Câu hỏi cần BA xác nhận**

Khi cán bộ phê duyệt **khác đơn vị** mở kế hoạch đang "Chờ duyệt", hệ thống cần hành xử theo hướng nào?

1. **Hướng 1 — theo tiền lệ `:277` / `:283` + đặc tả màn hình `:1774`:** nút "Phê duyệt/Từ chối" **vẫn hiện** (điều kiện chỉ là trạng thái + vai trò), khi bấm thì **hiển thị thông báo** giải thích không có quyền do khác đơn vị. ⇒ web hiện tại **thiếu thông báo**, và cần bổ sung mã lỗi tương ứng cho FR-III-15.
2. **Hướng 2 — theo cách suy rộng M-05 (`srs-v3.5.md:683`):** không có quyền thì **ẩn hẳn** nút, không cần thông báo. ⇒ web hiện tại **đúng**, cần sửa lại expected của testcase và sửa `:1774` cho khớp BR-AUTH-05.

Kèm 2 câu hỏi phụ:

- **(a)** M-05 đang viết cho **menu item** — BA xác nhận có mở rộng phạm vi sang **nút thao tác trong màn chi tiết** không? Nếu có, đề nghị sửa câu chữ M-05 cho rõ.
- **(b)** `:1774` ghi nút hiện theo trạng thái + vai trò, **không** nêu điều kiện đơn vị — lệch với BR-AUTH-05. BA xác nhận **sửa `:1774` cho khớp** không?

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `PDKHDTTH_04`: `Cần BA xác nhận` (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: UI hiện tại là `Vẫn lỗi` — owner `Dev FE` (hiển thị thông báo máy chủ đã trả sẵn) + `BA` bổ sung mã lỗi cho FR-III-15. Chi phí sửa thấp vì máy chủ **đã** trả message tiếng Việt đúng nghĩa.
- Nếu BA chọn **hướng 2**: UI hiện tại **không phải lỗi** — owner `QA update expected`; đồng thời cần sửa `:1774` và làm rõ phạm vi M-05, nếu không mâu thuẫn này sẽ lặp lại ở mọi chức năng phê duyệt khác.

---

### QLDXDTTH_11 — Tab "Đề xuất đào tạo": Cán bộ nghiệp vụ không có thao tác Tiếp nhận, nhưng lại có nút Gửi đề xuất mới

> **TC này do QA tự phát hiện** khi verify `QLDXDTTH_01` ngày 03/08/2026, **không nằm trong phiếu gốc của đối tác** → đã mở dòng TC mới trên sheet.
> **🔴 Ưu tiên cao nhất trong 3 mục:** nếu không chốt, đề xuất đào tạo **đứng vĩnh viễn** ở trạng thái "Mới gửi" và toàn bộ phiếu kiểm thử phía sau của nhóm đề xuất đào tạo **không chạy tiếp được**.

**Bối cảnh testcase**

- Dòng Excel: **135**, mã TC `QLDXDTTH_11` (dòng do QA mở, phát sinh từ `QLDXDTTH_01` — dòng Excel 118).
- Nội dung kiểm tra: Cán bộ nghiệp vụ thuộc **đúng đơn vị tiếp nhận** mở tab "Đề xuất đào tạo", xem cột Hành động và màn chi tiết của đề xuất đang ở trạng thái "Mới gửi".
- Expected trong file UAT: **không có** — TC do QA mở, không có expected của đối tác. Kỳ vọng lấy trực tiếp từ SRS.

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_hn` (vai trò CB_NV_DP, Sở Tư pháp Hà Nội) — mã đơn vị **trùng khít** đơn vị tiếp nhận của bản ghi, đã đối chiếu để loại trừ khả năng "không thấy do khác đơn vị".
- Tiền đề: đề xuất `QA-VERIFY-0803` do tài khoản Doanh nghiệp cùng đơn vị gửi trong cùng phiên, trạng thái **"Mới gửi"**.
- Cột "Hành động" của **mọi dòng** trong bảng đều là **dấu gạch ngang**, không có nút nào.
- Mở màn chi tiết đề xuất: chỉ có nút **"Quay lại danh sách"**, không có thao tác nghiệp vụ nào.
- ⇒ Cán bộ **không tiếp nhận được** đề xuất, quy trình đứng tại "Mới gửi".
- Ngược lại, nút **"Gửi đề xuất mới" lại hiện** với vai trò cán bộ. *(Chưa bấm thử để tránh tạo dữ liệu rác.)*
- Evidence: `../bug-reports/dao-tao/image/BUG-QLDXDTTH_01-08-CBNV-man-chi-tiet-khong-co-nut-Tiep-nhan.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **FR-III-13 (UC32) + đặc tả màn hình SCR-III-01**, việc tiếp nhận là **của Cán bộ nghiệp vụ**, còn người gửi là DN/NHT:
   - §Mô tả: *"DN/NHT gửi đề xuất đào tạo. **CB NV tiếp nhận**. Sửa/xóa khi chưa tiếp nhận."*
   - §Tác nhân: *"**DN / NHT**"* — cán bộ không nằm trong danh sách tác nhân gửi.
   - SCR-III-01 Thành phần 8: *"Tab phụ tiếp nhận đề xuất từ DN/NHT. Bảng cột … · **Hành động (Xem · Tiếp nhận · Đánh dấu thực hiện)**."*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1045`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1047`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1875`

2. Nhưng **Ma trận phân quyền** lại **không cấp quyền sửa** cho bất kỳ vai trò cán bộ nào trên thực thể này:
   - Dòng `DE_XUAT_DAO_TAO`: các cột vai trò cán bộ chỉ có `R` / `R*` (**chỉ đọc**, `*` = trong phạm vi đơn vị); chỉ 2 cột cuối nhóm DN/NHT mới có `C†RU*` (tạo + đọc + sửa).
   - ⇒ Theo ma trận này, **không vai trò cán bộ nào** được phép thay đổi trạng thái đề xuất ⇒ hành vi hiện tại của web (không có nút Tiếp nhận) là **đúng ma trận quyền**, nhưng **sai §Mô tả và §Đặc tả màn hình**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1309`

**Câu hỏi cần BA xác nhận**

Quyền trên thực thể `DE_XUAT_DAO_TAO` cần được hiểu theo hướng nào?

1. **Hướng 1 — theo FR-III-13 (`:1045`) + SCR-III-01 (`:1875`):** Cán bộ nghiệp vụ **được phép** Tiếp nhận / Đánh dấu thực hiện. ⇒ web hiện tại **thiếu chức năng**, và **Ma trận phân quyền (`srs-v3.5.md:1309`) phải bổ sung quyền sửa** cho vai trò CB NV, nếu không dev sửa xong vẫn mâu thuẫn tài liệu.
2. **Hướng 2 — theo Ma trận phân quyền (`srs-v3.5.md:1309`):** cán bộ **chỉ được đọc**. ⇒ web hiện tại **đúng**, nhưng khi đó **phải chỉ rõ vai trò nào tiếp nhận đề xuất** — nếu không có vai trò nào, quy trình đề xuất đào tạo **không có lối đi tiếp** và cần thiết kế lại luồng.

Kèm 1 câu hỏi phụ, độc lập với việc chọn hướng nào:

- **(a)** Vai trò cán bộ **có được phép gửi** đề xuất đào tạo không? §Tác nhân (`:1047`) chỉ ghi DN / NHT, nhưng web đang hiện nút "Gửi đề xuất mới" cho cán bộ. Nếu không được phép → cần **ẩn nút** với vai trò cán bộ.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `QLDXDTTH_11`: `Cần BA xác nhận` (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: UI hiện tại là `Vẫn lỗi` — owner `Dev FE` + `Dev BE` (bổ sung thao tác Tiếp nhận / Đánh dấu thực hiện) và `BA` cập nhật ma trận quyền `:1309`.
- Nếu BA chọn **hướng 2**: UI hiện tại **không phải lỗi** về mặt quyền — nhưng owner `BA` vẫn phải thiết kế lại luồng, vì hiện **không vai trò nào** đưa được đề xuất ra khỏi trạng thái "Mới gửi".
- **Đề nghị BA ưu tiên trả lời mục này trước 2 mục còn lại** — hai mục kia ảnh hưởng hiển thị/trải nghiệm, mục này **chặn luồng** và làm kẹt các TC nhóm đề xuất đào tạo phía sau.

---

## LUỒNG 2 — Mạng lưới tư vấn viên (4 TC)

### DKTGMLTVV_04 — Nhóm 3 "Tổ chức & Mạng lưới" của form Thêm mới TVV: 3 trường theo v3.5, hay 2 trường theo bản bàn giao 10/7?

> **Toàn bộ case này là câu hỏi đặc tả — không có ý nào là lỗi phần mềm.** Web khớp SRS v3.5 100%.

**Bối cảnh testcase**

- Dòng Excel: **122**, mã TC `DKTGMLTVV_04`.
- Nội dung kiểm tra: Người hỗ trợ mở form **Thêm mới Tư vấn viên**, cuộn tới nhóm 3 "Tổ chức & Mạng lưới", đọc danh sách trường.
- Expected trong file UAT: nhóm 3 **chỉ gồm 2 trường** — "Lĩnh vực pháp luật đăng ký" và "Tổ chức tư vấn chủ quản".
- Actual đối tác ghi: *"hệ thống hiển thị nhiều hơn"* — tức web có thêm trường thứ 3.

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026 qua Chrome DevTools MCP, tài khoản UAT `nht_qa_tw` (vai trò **NHT**, cấp TW) — **trùng vai trò của đối tác** trong ảnh bằng chứng. *(Không dùng bộ tài khoản `_02` vì bộ đó chỉ có vai trò CB Nghiệp vụ / CB Phê duyệt, trong khi màn này bắt buộc vai trò NHT. Không dùng admin để ra verdict.)*
- Đường đi đúng 3 bước đối tác mô tả: sidebar → "Tư vấn viên / Chuyên gia" → tab "Mới đăng ký" → "Thêm mới".
- Nhóm 3 có **đúng 3 trường**, không có trường thứ 4:
  1. **Tổ chức hành nghề chính** — dropdown có tìm kiếm, không bắt buộc
  2. **Tổ chức đối tác** — dropdown chọn nhiều, không bắt buộc
  3. **Lĩnh vực pháp luật \*** — dropdown chọn nhiều, bắt buộc
- Đo lặp ở **cả 2 giá trị "Loại"** (Tư vấn viên / Chuyên gia): đều 3 trường, không đổi.
- ⇒ **Đối tác quan sát ĐÚNG thực tế** (web đang có 3 trường). Cái lệch nằm ở **kỳ vọng**, không phải ở quan sát.
- Console **0 lỗi / 0 cảnh báo**; network không có 4xx/5xx.
- Evidence: `../image/DKTGMLTVV_04-web-nhom3.png` (ảnh đã mở đọc: header "Tổ chức & Mạng lưới", 3 ô, ngay dưới là header nhóm kế tiếp "File đính kèm" ⇒ nhóm 3 kết thúc sau 3 trường, không có trường bị khuất).
- *Ghi chú về độ tin của phép đo:* lần đo đầu trả về "0 trường" cho mọi nhóm — **không** kết luận "form hỏng" mà đọc HTML thô trước, phát hiện bản dựng này render thân nhóm bằng lớp `.ant-collapse-body` (thư viện selector cũ ghi `.ant-collapse-content`). Sửa rồi đo lại mới lấy số.

**Điểm mâu thuẫn — nằm giữa HAI BẢN TÀI LIỆU, không phải trong một bản**

1. **SRS v3.5 quy định đúng 3 trường**, khớp 100% những gì web đang hiện:

   Citation:
   - `srs-fr-04-chuyen-gia-tvv.md:1514` — nhóm 3 tên "Tổ chức & Mạng lưới", nhóm thu gọn
   - `srs-fr-04-chuyen-gia-tvv.md:1515` — 4.1 Tổ chức chính, dropdown có tìm kiếm, tùy chọn
   - `srs-fr-04-chuyen-gia-tvv.md:1516` — 4.2 **Tổ chức đối tác**, dropdown chọn nhiều, tùy chọn (quan hệ N:N)
   - `srs-fr-04-chuyen-gia-tvv.md:1517` — 4.3 Lĩnh vực pháp luật \*, bắt buộc ≥ 1

2. **Đối tác đang bám một bản tài liệu khác.** Cột "TKM phản hồi lần 1" của chính dòng này ghi: *"Do tài liệu SRS được bàn giao lần 2 ngày 10/7 (v2.0) thay đổi nên log bug thay đổi theo"* ⇒ đối tác căn theo bản đánh số **v2.0 bàn giao 10/7** (2 trường), còn QA và dev căn theo **v3.5**. Đây là **mâu thuẫn giữa các nguồn**, không phải đối tác thao tác sai.

3. **Tiền lệ: BA đã trực tiếp soi chính nhóm 3 này ngày 30/07/2026.** CHANGELOG SRS v3.5 (mục "Apply chốt UAT tuần 2 vòng 2", dòng 26) ghi: *"(2) `to_chuc_chinh_id` Y→N cho khớp **SCR-IV-02 mục 4.1**, FR-IV-03 §Inputs #14 và baseline — tư vấn viên tự do được để trống (**DKTGMLTVV_03** phần Open)"*. Tức BA đã sửa **mục 4.1** của đúng nhóm này, **và giữ nguyên mục 4.2 "Tổ chức đối tác"**, đồng thời khẳng định *"form giữ đúng 5 nhóm, không tách nhóm thứ 6"*. Đây là tín hiệu mạnh rằng cấu trúc 3 trường là **có chủ đích**, nhưng QA **không tự suy ra kết luận thay BA**.

**Câu hỏi cần BA xác nhận**

Nhóm 3 của màn `SCR-IV-02` phải theo bản tài liệu nào?

1. **Hướng 1 — v3.5 (`:1514-1517`) là bản chuẩn:** nhóm 3 gồm 3 trường. ⇒ web hiện tại **đúng**, cần sửa lại expected của testcase và đồng bộ tài liệu phía đối tác.
2. **Hướng 2 — bản bàn giao 10/7 là bản chuẩn:** nhóm 3 chỉ 2 trường. ⇒ cần **gỡ "Tổ chức đối tác" khỏi form** và **cập nhật lại SRS v3.5** (xóa mục 4.2), đồng thời xử lý dữ liệu N:N đã phát sinh nếu có.

Kèm 1 câu hỏi phụ:

- **(a)** Trường **"Tổ chức đối tác"** (`:1516`, quan hệ N:N) có giữ lại trên form **Thêm mới** TVV không, hay chỉ xuất hiện ở màn Chỉnh sửa / Chi tiết? (Gợi ý: BA đã đụng mục 4.1 cùng nhóm ngày 30/07 mà **không** gỡ mục 4.2.)

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt bản tài liệu chuẩn.
- Tạm verdict cho `DKTGMLTVV_04`: `Cần BA xác nhận` (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: UI hiện tại **không phải lỗi** — owner `QA update expected` + `BA` gửi lại bản v3.5 cho đối tác để hai bên dùng chung một nguồn.
- Nếu BA chọn **hướng 2**: UI hiện tại là `Vẫn lỗi` — owner `Dev FE` (gỡ trường) + `BA` cập nhật SRS. Lưu ý đây là **đảo ngược một quyết định BA vừa ra ngày 30/07**, nên cần nêu rõ lý do đổi.
- **Rủi ro nếu không chốt:** cả nhóm TC `DKTGMLTVV_*` sẽ lặp lại đúng tranh chấp này ở mọi vòng verify sau, vì hai bên đang đọc hai bản tài liệu khác nhau.

---

### DKTGMLTVV_05 — "File thẻ hành nghề" thuộc nhóm 2 hay nhóm 4? SRS liệt kê CÙNG MỘT trường ở cả hai chỗ

> **Case hỗn hợp.** Chỉ ý 1 dưới đây cần BA. Hai lỗi còn lại trong cùng case đã chứng minh tái hiện và **không chờ BA** — xem khối cuối mục này.

**Bối cảnh testcase**

- Dòng Excel: **123**, mã TC `DKTGMLTVV_05`.
- Nội dung kiểm tra: Người hỗ trợ mở form Thêm mới TVV → nhóm 4 "File đính kèm", đọc các mục tải tệp.
- Expected trong file UAT: nhóm 4 gồm **2 tệp** — "Tệp bằng cấp / chứng chỉ" **và** "Tệp thẻ hành nghề".
- Actual đối tác ghi: nhóm 4 chỉ có tệp thứ nhất, thiếu "Tệp thẻ hành nghề".

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026, tài khoản `nht_qa_tw` (vai trò **NHT**, cấp TW — đúng vai trò được phép đăng ký ứng viên mới). Không dùng admin.
- Nhóm 4 có **đúng 1 mục**: "File đính kèm (Bằng cấp / Chứng chỉ)". Đo ở **cả 2 giá trị "Loại"** (Chuyên gia / Tư vấn viên) — đều 1 mục.
- Chức năng tải "File thẻ hành nghề" **có tồn tại**, nhưng nằm ở **nhóm 2 "Nghề nghiệp"** (nhãn "File thẻ hành nghề (PDF)", tối đa 1 tệp, 10MB).
- ⇒ **Đối tác quan sát ĐÚNG**: nhóm 4 thật sự không có trường này. Nhưng chức năng **không bị thiếu**, chỉ **khác vị trí nhóm**.
- *Về bằng chứng của đối tác:* ảnh bị **cắt ngay dưới khung kéo-thả** nên **tự nó không chứng minh được sự vắng mặt** ở phần dưới nhóm 4. Kết luận vắng mặt ở trên **lấy từ phép đo live của QA**, không lấy từ ảnh — nói rõ để BA không hiểu nhầm nguồn kết luận.
- Evidence: `../image/DKTGMLTVV_05-web-nhom4-truoc-upload.png` (ảnh đã mở đọc: nhóm "File đính kèm" chỉ 1 mục; ngay dưới là nhóm "Ghi chú" ⇒ không còn mục nào khác trong nhóm 4).

**Điểm mâu thuẫn trong SRS v3.5 — cùng một trường được liệt kê HAI LẦN, ở HAI NHÓM**

1. `srs-fr-04-chuyen-gia-tvv.md:1508` — mục **3.6, nhóm 2 "Nghề nghiệp"**: *"File thẻ hành nghề | tải file | PDF, tối đa 10MB; **bắt buộc nếu Loại = Tư vấn viên**"*.
2. `srs-fr-04-chuyen-gia-tvv.md:1520` — mục **5.2, nhóm 4 "File đính kèm"**: *"File thẻ hành nghề | tải 1 file | PDF, tối đa 10MB"* (ô Ràng buộc **không ghi điều kiện** nào).

Cùng một trường, hai nhóm khác nhau, và **không có câu nào trong SRS nói nó xuất hiện ở cả hai**. Đây là **lỗi đặc tả**, không phải lỗi phần mềm.

> **Đính chính giải trình của dev:** dev ghi ở cột phản hồi rằng *"tệp Thẻ hành nghề đặt ở Nhóm 2 đúng SRS (mục 3.6)"*. Phần đó **đúng sự thật** nhưng **đọc thiếu** — SRS còn liệt kê chính trường ấy ở mục 5.2 nhóm 4 (`:1520`). Nêu ra để BA thấy vì sao QA không đóng case theo hướng "không phải bug".

**Câu hỏi cần BA xác nhận**

Trường "File thẻ hành nghề" thuộc nhóm nào của màn `SCR-IV-02`?

1. **Hướng 1 — chỉ nhóm 2 (`:1508`):** web hiện tại **đúng**. ⇒ cần **xóa mục 5.2 khỏi `:1520`** để SRS hết mâu thuẫn, và sửa lại expected của testcase.
2. **Hướng 2 — chỉ nhóm 4 (`:1520`):** ⇒ cần **chuyển trường xuống nhóm 4** và xóa mục 3.6 ở `:1508`; lưu ý ràng buộc *"bắt buộc nếu Loại = Tư vấn viên"* hiện chỉ được ghi ở `:1508` nên phải mang theo.
3. **Hướng 3 — xuất hiện ở CẢ HAI nhóm** (một chỗ nhập, một chỗ xem lại): ⇒ web **thiếu** phần hiển thị ở nhóm 4, và SRS cần ghi rõ quan hệ giữa hai chỗ (cùng một tệp hay hai tệp khác nhau).

Kèm 1 câu hỏi phụ:

- **(a)** Nếu chọn hướng 1 hoặc 2, ràng buộc *"bắt buộc nếu Loại = Tư vấn viên"* (`:1508`) có được giữ nguyên không? Hiện web **có** áp ràng buộc này ở nhóm 2 (thử lưu hồ sơ TVV không đính kèm → bị chặn với thông báo *"File thẻ hành nghề là bắt buộc đối với Tư vấn viên"*), nên nếu chuyển nhóm mà quên mang ràng buộc thì sẽ thành lỗi mới.

**Đề xuất QA tạm thời**

- Tạm verdict cho `DKTGMLTVV_05`: `Cần BA xác nhận` cho ý này (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: owner `BA` (xóa `:1520`) + `QA update expected`. Chi phí gần như bằng 0, không cần dev.
- Nếu BA chọn **hướng 2 hoặc 3**: owner `Dev FE` + `BA` cập nhật SRS.

**Phần KHÔNG chờ BA — 2 lỗi đã chứng minh tái hiện trong cùng case này**

| Mã bug | Nội dung | Vì sao không cần BA |
|---|---|---|
| `BUG-DKTGMLTVV_05` | `:1519` ghi "Bằng cấp / Chứng chỉ **\***  — **bắt buộc khi Người hỗ trợ đăng ký ứng viên mới**", nhưng web **không đánh dấu bắt buộc và không chặn**: đã tạo thật hồ sơ `TVV-BTP-TW-0030` với nhóm 4 rỗng, hệ thống trả "Tạo hồ sơ TVV thành công" | Sai **một clause SRS cụ thể**, không có nguồn nào trong SRS mâu thuẫn với clause đó |
| `BUG-DKTGMLTVV_05-B` | `:1521` ghi *"Xóa: **xác nhận trước khi xóa**"*, nhưng nút "Xóa" trong danh sách file đã tải **gỡ tệp ngay**, không hỏi. Đo 2 lần bằng 2 cách (click chuột thật + script), kết quả giống nhau | Như trên — clause rõ ràng, không mâu thuẫn nội tại |

⇒ Hai bug này **dev xử lý được ngay**, không phụ thuộc câu trả lời của BA. Chi tiết + ảnh: `../bug-reports/mang-luoi-tvv/bug-report-mang-luoi-tvv.md`.

---

### QLLSHTCTVV_03 — Bảng "Lịch sử hỗ trợ" có phải bổ sung cột "Trạng thái vụ việc" không?

> **Case hỗn hợp.** Chỉ ý (2) dưới đây cần BA. Hai lỗi hiển thị còn lại **không chờ BA** — xem khối cuối mục này.

**Bối cảnh testcase**

- Dòng Excel: **125**, mã TC `QLLSHTCTVV_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ mở hồ sơ chi tiết một Tư vấn viên đang hoạt động → tab "Lịch sử hỗ trợ", đọc các cột của bảng.
- Đối tác phản ánh **2 ý**: (1) cột "Đánh giá" bị tràn; (2) **thiếu cột "Trạng thái"**.
- Ý cần BA ở đây là **ý (2)**.

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026, tài khoản `cbnv_tw_02` (vai trò `CB_NV_TW`, đơn vị Cục Bổ trợ tư pháp — Bộ Tư pháp, cấp TW) — trùng vai trò + cấp của đối tác. Không dùng admin.
- Bản ghi test: `TVV-BTP-TW-0002`, tab "Lịch sử hỗ trợ (6)".
- Bảng có **đúng 9 cột**, khớp **9/9** với danh sách cột mà `SCR-IV-03:1578` liệt kê: Mã vụ việc · Tên vụ việc · Doanh nghiệp · Lĩnh vực · Vai trò · Ngày phân công · Ngày hoàn thành · Kết quả · Đánh giá.
- **Không có cột "Trạng thái"** — và `:1578` **cũng không liệt kê** cột đó. ⇒ Xét riêng đặc tả màn hình, **web không thiếu cột nào**.
- Evidence: `../image/QLLSHTCTVV_03-web-cot-danhgia-vo-2-dong.png`

**Điểm mâu thuẫn trong SRS v3.5 — đặc tả MÀN HÌNH chỏi đặc tả CHỨC NĂNG của cùng một FR**

1. **Đặc tả màn hình** `srs-fr-04-chuyen-gia-tvv.md:1578` liệt kê **9 cột, không có "Trạng thái"** → web đúng.
2. Nhưng **đặc tả chức năng FR-IV-10 (UC48)** lại khai `trang_thai` là **dữ liệu đầu ra** và cho **lọc** theo nó:
   - `srs-fr-04-chuyen-gia-tvv.md:792` — §Outputs: `| 5 | trang_thai | text | — | Trạng thái vụ việc |`
   - `srs-fr-04-chuyen-gia-tvv.md:773` — §Inputs: `| 4 | trang_thai_vv | text | N | Lọc trạng thái vụ việc |`
   - `srs-fr-04-chuyen-gia-tvv.md:1578` mục (a) — bộ lọc "Trạng thái vụ việc" **có** trong đặc tả màn hình, và **đang hiện thật trên web**.
3. **Số liệu thực tế củng cố câu hỏi:** 6 vụ việc của `TVV-BTP-TW-0002` trải trên **5 trạng thái khác nhau** (`DA_DUYET`, `DA_DANH_GIA` ×2, `DA_PHAN_CONG`, `DANG_XU_LY`, `HOAN_THANH`). Dữ liệu **đã có sẵn**, **lọc được**, chỉ **không được trình bày thành cột** — người dùng lọc theo trạng thái nhưng không nhìn thấy trạng thái của từng dòng kết quả.
4. **Đối chứng trong cùng màn hình:** bảng "Hợp đồng tư vấn" nằm ngay dưới, cùng trang, **có** cột "Trạng thái" — cho thấy cột trạng thái là mẫu quen thuộc của hệ thống.

**Câu hỏi cần BA xác nhận**

Bảng "Lịch sử hỗ trợ" có phải bổ sung cột "Trạng thái vụ việc" không?

1. **Hướng 1 — theo §Outputs (`:792`) + §Inputs (`:773`):** `trang_thai` là dữ liệu đầu ra của UC48, phải hiển thị thành **cột**. ⇒ web hiện tại **thiếu 1 cột**, và `:1578` cần bổ sung cột đó vào danh sách.
2. **Hướng 2 — theo đặc tả màn hình (`:1578`):** danh sách 9 cột là **danh sách đóng**; `trang_thai` chỉ phục vụ **lọc**, không cần thành cột. ⇒ web hiện tại **đúng**, cần sửa lại expected của testcase.

Kèm 1 câu hỏi phụ:

- **(a)** Nếu chọn hướng 2 — giữ bộ lọc "Trạng thái vụ việc" mà không hiển thị cột tương ứng có gây khó hiểu cho người dùng không? Hiện người dùng lọc ra 1 dòng nhưng không có cách nào đọc được trạng thái của dòng đó ngay trên bảng.

**Đề xuất QA tạm thời**

- Tạm verdict cho `QLLSHTCTVV_03`: `Cần BA xác nhận` cho ý (2) (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA chọn **hướng 1**: owner `Dev FE` (thêm cột — dữ liệu đã có sẵn trong dữ liệu trả về, không cần đụng BE) + `BA` cập nhật `:1578`.
- Nếu BA chọn **hướng 2**: owner `QA update expected`; nên trả lời thêm câu (a) để tránh lặp lại tranh chấp ở màn tương tự.

**Phần KHÔNG chờ BA — 2 lỗi hiển thị đã chứng minh tái hiện trong cùng case này**

| Mã bug | Nội dung | Vì sao không cần BA |
|---|---|---|
| `BUG-QLLSHTCTVV_03` | Cột "Đánh giá" **vỡ 2 hàng** (4 sao trên, 1 sao dưới) ở **6/6 dòng** tại khung nhìn 1440×900 và 1600×900 (ở 1920 thì bình thường). Nguyên nhân đo được: dãy 5 sao cần 132px, ô rộng 140px trừ đệm còn 124px → **thiếu 8px**. Đây chính là chỗ đối tác khoanh đỏ (ý 1 của họ) | Vi phạm tiêu chí chung ghi ngay trong phiếu: *"Dữ liệu hiển thị không bị tràn/đè lên nhau"* — không cần BA diễn giải |
| `BUG-QLLSHTCTVV_03-B` | Ô "Điểm trung bình" hiện **8.9** trong khi cùng trang, đầu hồ sơ hiện **4.1/5**. `:1578` mục (c) quy định *"Điểm trung bình: {X}**/5**"* và `FR-IV-10:795` quy định `diem_danh_gia` định dạng **"1.0–5.0"**, nhưng dữ liệu đang là **thang 10** (`9.0`, `8.7`). Hệ quả: 2 vụ việc điểm khác nhau **đều hiện 5/5 sao đầy** → mất khả năng phân biệt | Sai **clause SRS cụ thể** về thang điểm; ngoài ra ảnh của **chính đối tác** cũng hiện "Điểm trung bình 8.3" ⇒ lỗi có trên cả môi trường của họ |

⇒ Hai bug này **dev xử lý được ngay**. Chi tiết + ảnh: `../bug-reports/mang-luoi-tvv/bug-report-mang-luoi-tvv.md`.

---

### QLLSHTCTVV_04 — Bộ lọc "Trạng thái vụ việc": tập giá trị rút gọn có đủ dùng không, và nhãn "Đã hủy" trong SRS là gì?

> **Case hỗn hợp và là TC duy nhất mang cả dạng A lẫn dạng B.** Ý A + ý B cần BA; lỗi "chọn đơn thay vì chọn nhiều" **không chờ BA** — xem khối cuối mục này.

**Bối cảnh testcase**

- Dòng Excel: **126**, mã TC `QLLSHTCTVV_04`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ mở hồ sơ chi tiết TVV → tab "Lịch sử hỗ trợ" → mở dropdown "Trạng thái vụ việc".
- Expected/Actual đối tác: *"Danh sách chọn Trạng thái chưa đủ giá trị theo định nghĩa của nhóm chức năng Quản lý vụ việc"* — tức họ chờ đủ tập trạng thái vụ việc (12 giá trị), web chỉ có 3.
- Ảnh bằng chứng của đối tác **bắt đúng khoảnh khắc lỗi** (dropdown đang mở), không phải ảnh chụp sau.

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026, tài khoản `cbnv_tw_02` (`CB_NV_TW`, BTP·TW). **Trang đã tải lại + bỏ cache trước khi đo** để không chạy nhầm mã cũ của tab mở lâu. Không dùng admin.
- Dropdown có **đúng 3 giá trị**: "Đang xử lý" · "Hoàn thành" · "Từ chối". Không có "Tất cả", không có "Đã hủy".
- Hành vi "xem tất cả" **vẫn đạt được** bằng nút xóa (⊗) của ô lọc → gửi yêu cầu không kèm tham số trạng thái → trả đủ 6/6 dòng. Tức thiếu option tên "Tất cả" nhưng **không mất chức năng**.
- Giao diện hiện **nhãn tiếng Việt**, mã enum chỉ nằm trong tham số yêu cầu — đúng `srs-fr-05-vu-viec.md:1492`.
- Console 0 lỗi / 0 cảnh báo; 26 yêu cầu mạng toàn 200/304; mỗi lần đổi bộ lọc phát **đúng 1 yêu cầu**, không gọi lặp.
- Evidence: `../image/QLLSHTCTVV_04-web-dropdown-3option.png`

**Ý A — tập giá trị rút gọn (dạng A: kỳ vọng đối tác lệch SRS)**

- Đối tác **quan sát đúng**: dropdown thật sự chỉ có 3 giá trị, ít hơn tập 12 trạng thái vụ việc (`srs-fr-05-vu-viec.md:1498-1509`).
- Nhưng `SCR-IV-03:1578` **cố ý** quy định tập **rút gọn** cho riêng tab này: `"Tất cả" / "Đang xử lý" / "Hoàn thành" / "Đã hủy"`. Web bám tập rút gọn ⇒ **không lệch đặc tả màn hình**.
- ⇒ Bất đồng nằm ở **kỳ vọng vs đặc tả**, không phải ở thực tế. Theo quy trình verify, ca này **cấm dùng `Reject`**, phải để BA chốt.

**Số liệu làm câu hỏi trở nên cụ thể — bộ lọc hiện chỉ chạm tới 2/6 bản ghi**

Đo thật trên `TVV-BTP-TW-0002` (nền 6 dòng):

| Giá trị chọn | Số dòng trả về |
|---|:-:|
| *(không lọc)* | **6** |
| Đang xử lý | 1 |
| Hoàn thành | 1 |
| Từ chối | **0** |

⇒ **4/6 vụ việc không giá trị nào lọc ra được**: `DA_DUYET` ×1, `DA_DANH_GIA` ×2, `DA_PHAN_CONG` ×1. Đây là **hệ quả của chính tập rút gọn mà SRS quy định** — không phải phần mềm làm sai — nhưng nó cho thấy tập rút gọn hiện **không phủ được 2/3 dữ liệu mà chính tab này đang hiển thị**.

**Ý B — nhãn "Đã hủy" trong SRS là nhãn mồ côi (dạng B: SRS tự mâu thuẫn)**

- `SCR-IV-03:1578` nguyên văn ghi giá trị thứ 4 là **"Đã hủy"** (đã mở file verify, không dựa trí nhớ).
- Bảng ánh xạ mã → nhãn `srs-fr-05-vu-viec.md:1498-1509` liệt kê **12 trạng thái, KHÔNG có "Đã hủy"**; giá trị gần nhất là `TU_CHOI` → nhãn **"Từ chối"**.
- Web hiển thị **"Từ chối"** và gửi `TU_CHOI` ⇒ **web khớp bảng ánh xạ `:1509`**, chỉ lệch nguyên văn `:1578`. Ở điểm này **web đúng hơn SRS**.

> **Đính chính giải trình của dev:** dev viết ở cột phản hồi rằng `:1578` ghi *"Tất cả/Đang xử lý/Hoàn thành/**Từ chối**"*. Nguyên văn `:1578` là **"Đã hủy"**, không phải "Từ chối" — dev đã mô tả **giao diện đang chạy** rồi gán cho SRS. Kết luận cuối của dev (tập rút gọn là chủ ý) vẫn đúng, nhưng nếu không kiểm lại thì chính mâu thuẫn ở ý B này sẽ bị bỏ qua.

**Câu hỏi cần BA xác nhận**

1. **Câu hỏi chính (ý A):** bộ lọc "Trạng thái vụ việc" của tab "Lịch sử hỗ trợ" giữ **tập rút gọn** theo `:1578`, hay dùng **đủ tập 12 trạng thái** theo `srs-fr-05-vu-viec.md:1498-1509` như đối tác kỳ vọng? Nếu giữ tập rút gọn, xin xác nhận rõ **việc 4/6 vụ việc không lọc được là chấp nhận được**.
2. **Câu hỏi chính (ý B):** nhãn thứ 4 đúng là **"Đã hủy"** (⇒ cần bổ sung trạng thái này vào bảng ánh xạ và vào phần mềm) hay **"Từ chối"** (⇒ cần sửa nguyên văn `:1578` cho khớp `:1509`)?

Kèm 1 câu hỏi phụ:

- **(a)** SRS yêu cầu có option **"Tất cả"** trong danh sách. Web không có option đó nhưng đạt cùng hành vi bằng nút xóa bộ lọc (⊗). BA chấp nhận cách thể hiện này hay yêu cầu đúng một mục tên "Tất cả"?

**Đề xuất QA tạm thời**

- Tạm verdict cho `QLLSHTCTVV_04`: `Cần BA xác nhận` cho ý A + ý B (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Nếu BA giữ **tập rút gọn**: owner `QA update expected`; `BA` vẫn phải trả lời ý B vì `:1578` đang chứa một nhãn không tồn tại trong hệ thống.
- Nếu BA chọn **đủ 12 trạng thái**: owner `Dev FE` + `BA` cập nhật `:1578`.
- **Lưu ý phạm vi ảnh hưởng:** cụm `(chọn nhiều: "Tất cả" / "Đang xử lý" / "Hoàn thành" / "Đã hủy")` được SRS lặp **nguyên văn** ở `:1856` cho tab "Vụ việc đã hỗ trợ" của màn Người hỗ trợ pháp lý ⇒ câu trả lời của BA sẽ áp cho **2 màn**, không chỉ màn này.

**Phần KHÔNG chờ BA — 1 lỗi đã chứng minh tái hiện trong cùng case này**

| Mã bug | Nội dung | Vì sao không cần BA |
|---|---|---|
| `BUG-QLLSHTCTVV_04` | `:1578` ghi rõ bộ lọc là **"chọn nhiều"**, web chỉ giữ **1 giá trị** tại một thời điểm. Xác minh bằng **3 phương pháp độc lập**: lớp CSS là `ant-select-single` (không có `ant-select-multiple`) · thao tác thật chọn "Đang xử lý" rồi "Hoàn thành" thì giá trị sau **đè** giá trị trước · thuộc tính trợ năng `aria-multiselectable` = `null`, 0 checkbox, 0 thẻ tag | Sai **clause SRS cụ thể**. Cụm "dropdown chọn nhiều" là **kiểu điều khiển chính thức** của SRS (dùng ở `:1516`, `:1517`) và lặp lại ở `:1856` ⇒ là quy định có chủ ý, không phải chữ thừa |

⇒ Bug này **dev xử lý được ngay**. Chi tiết + ảnh: `../bug-reports/mang-luoi-tvv/bug-report-mang-luoi-tvv.md`.

*Ghi chú kỹ thuật cho lần verify sau:* bản dựng này render ô select bằng `.ant-select-content`, **không** phải `.ant-select-selector` như thư viện selector cũ ghi — selector cũ trả `null`, dễ bị hiểu nhầm thành "không có điều khiển".

---

## LUỒNG 3 — Vụ việc hỗ trợ pháp lý (1 TC)

### TKHSYCHTPL_OOS_01 — Hồ sơ đã kết thúc vẫn lọt bộ lọc "Sắp hết hạn", còn cột "Cảnh báo thời hạn" hiện nhãn không có trong đặc tả

> **TC này do QA tự phát hiện** khi verify `TKHSYCHTPL_03` ngày 03/08/2026, **không nằm trong phiếu gốc của đối tác** → đã mở dòng TC mới trên sheet.
> **Không phải hồi quy:** cách hiển thị này đã có từ trước lần sửa bộ lọc "Mức SLA".

**Bối cảnh testcase**

- Dòng Excel: **145**, mã TC `TKHSYCHTPL_OOS_01` (phát sinh từ `TKHSYCHTPL_03` — phiếu đó chỉ nói về việc bộ lọc báo lỗi, không có dòng nào cho phần hiển thị cột "Cảnh báo thời hạn").
- Nội dung kiểm tra: màn "Vụ việc HTPL / Danh sách", chọn **Mức SLA = "Sắp hết hạn"**, đọc cột "Cảnh báo thời hạn" của các dòng trả về.
- Expected trong file UAT: **không có** — TC do QA mở. Kỳ vọng lấy trực tiếp từ SRS.

**Kết quả verify UI hiện tại**

- Verify ngày 03/08/2026, tài khoản `cbnv_tw_03` (`CB_NV_TW`, đơn vị BTP · TW), đăng nhập lần đầu OK. Không dùng admin.
- Lọc "Mức SLA = Sắp hết hạn" trả về **đúng 2 hồ sơ**: `VV-BTP-TW-20260712-006` và `VV-BTP-TW-20260712-005` (cùng tiếp nhận 12/07/2026, thời hạn xử lý 31/07/2026).
- **Cả 2 hồ sơ đều đã kết thúc**: một ở trạng thái **"Từ chối"**, một ở **"Hoàn thành"**.
- Ngay trên 2 dòng đó, cột **"Cảnh báo thời hạn"** lại hiện **"Đã hoàn thành"** — tức bộ lọc và cột hiển thị **nói hai điều khác nhau** trên cùng một màn, người dùng dễ hiểu nhầm bộ lọc trả sai bản ghi.
- Nguyên nhân đo được: mức cảnh báo của 2 hồ sơ **vẫn giữ nguyên "Sắp hết hạn"** kể từ lúc hồ sơ đóng (cập nhật cuối 29/07 và 24/07) và không đổi nữa, dù mốc 31/07/2026 đã trôi qua.
- Đo bằng **2 phương pháp độc lập, không mâu thuẫn**: ảnh full-res 1920×1080 (đã đọc pixel, cột "Mã vụ việc" và "Cảnh báo thời hạn" **cùng lọt một khung hình**, chân bảng ghi "Hiển thị 1-2 / 2 kết quả") + gọi lại chính dịch vụ danh sách bằng phiên đăng nhập đó (HTTP 200, `meta.total = 2`, cả 2 bản ghi mang mức cảnh báo `SAP_HET`, `trangThai` là `TU_CHOI` / `HOAN_THANH`).
- ⚠️ **Hai cột rất dễ nhầm** — đây là chỗ suýt kết luận sai ở lượt trước: cột **"Trạng thái"** hiện "Từ chối"/"Hoàn thành"; cột **"Cảnh báo thời hạn"** (đứng sau "Thời hạn xử lý") mới là cột hiện "Đã hoàn thành".
- Evidence: `../bug-reports/vu-viec/image/BUG-TKHSYCHTPL_OOS_01-cot-canh-bao-thoi-han-hien-da-hoan-thanh.png`

**Điểm mâu thuẫn trong SRS v3.5 — đặc tả IM LẶNG, không trích được điều khoản nào bị vi phạm**

1. `srs-fr-05-vu-viec.md:1436` (FR-V.I-CROSS-01) — công việc tự động **chỉ rà hồ sơ ĐANG hoạt động** (Đã tiếp nhận, Đang kiểm tra, Đã phân công, Đang xử lý, Chờ phê duyệt). Hồ sơ Hoàn thành / Từ chối **không nằm trong phạm vi rà** ⇒ việc mức cảnh báo cũ được giữ lại là **đúng phạm vi đã mô tả**.
2. `srs-fr-05-vu-viec.md:2442` (BR-CALC-03) — chỉ nêu **công thức tính** mức cảnh báo và chu kỳ chạy 30 phút, **không nói** phải xử lý ra sao với mức cảnh báo còn sót của hồ sơ đã đóng.
3. `srs-fr-05-vu-viec.md:1656` (SCR-V.I-01) — cột "Cảnh báo thời hạn" chỉ gồm **4 mức**: Bình thường / Sắp hết hạn / Quá hạn / Quá hạn nghiêm trọng. Nhãn **"Đã hoàn thành" không nằm trong 4 mức này** và không được định nghĩa ở bất kỳ chỗ nào khác.
4. `srs-fr-05-vu-viec.md:636` (FR-V.I-08, UC58) — mô tả chức năng tìm kiếm và lọc, **không nêu** bộ lọc mức cảnh báo có loại trừ hồ sơ đã kết thúc hay không.

> Đã `grep` toàn file cụm **"Đã hoàn thành"** → **0 kết quả**; `grep` các cụm về "đặt lại / xoá cảnh báo" → **0 kết quả**. Không trích được điều khoản nào bị vi phạm ⇒ verdict phải là `BA confirm`, **không phải `Open`**.

**Câu hỏi cần BA xác nhận**

1. Khi hồ sơ **đã kết thúc** (Hoàn thành / Từ chối), mức cảnh báo thời hạn có phải được **đặt lại hoặc xoá đi** không, hay **giữ nguyên** giá trị tại thời điểm đóng hồ sơ?
2. Hồ sơ đã kết thúc có được phép **xuất hiện trong kết quả lọc "Mức SLA = Sắp hết hạn"** không? Nếu không, bộ lọc cần loại trừ các trạng thái kết thúc.
3. Nhãn **"Đã hoàn thành"** ở cột "Cảnh báo thời hạn" có được bổ sung chính thức vào đặc tả như **một mức hiển thị riêng** (mức thứ 5) không, hay với hồ sơ đã kết thúc thì cột này phải **để trống / hiển thị dấu "—"**?

**Đề xuất QA tạm thời**

- Tạm verdict cho `TKHSYCHTPL_OOS_01`: `Cần BA xác nhận` (đã ghi `BA confirm` vào cả 2 cột trạng thái trên sheet).
- Ba câu hỏi trên **liên quan nhau** — trả lời câu 1 gần như quyết định luôn câu 2; câu 3 độc lập và có thể trả lời riêng.
- Nếu BA yêu cầu **đặt lại mức cảnh báo khi đóng hồ sơ**: owner `Dev BE` (xử lý tại bước chuyển trạng thái kết thúc) + rà dữ liệu cũ đang mang mức cảnh báo mồ côi.
- Nếu BA giữ **nguyên trạng**: owner `BA` bổ sung nhãn "Đã hoàn thành" vào `:1656` và ghi rõ ở `:636` rằng bộ lọc mức SLA **không** loại trừ hồ sơ đã kết thúc — nếu không, mỗi vòng verify sẽ lại có người báo đây là lỗi.


---

## Bảng tra nhanh

| # | Mã TC | Dòng Excel | Luồng | Dạng | Vấn đề cần BA chốt | Số câu hỏi | Mức ảnh hưởng |
|---|---|:-:|---|:-:|---|:-:|---|
| 1 | `KTDGKQHT_02` | 116 | Đào tạo | B | 4 trường §Outputs UC24 có phải hiển thị thành cột riêng không | 1 chính + 2 phụ | Hiển thị — không chặn luồng |
| 2 | `PDKHDTTH_04` | 120 | Đào tạo | B | Chặn duyệt khác đơn vị có bắt buộc kèm thông báo giải thích không | 1 chính + 2 phụ | Trải nghiệm — người dùng không biết vì sao bị chặn |
| 3 | `QLDXDTTH_11` | 135 | Đào tạo | B | Vai trò nào được tiếp nhận đề xuất đào tạo | 1 chính + 1 phụ | 🔴 **Chặn luồng** — đề xuất kẹt ở "Mới gửi" |
| 4 | `DKTGMLTVV_04` | 122 | Mạng lưới TVV | B | Nhóm 3 form Thêm mới TVV: 3 trường (v3.5) hay 2 trường (bản 10/7) | 1 chính + 1 phụ | Tài liệu — hai bên đang đọc hai bản SRS khác nhau |
| 5 | `DKTGMLTVV_05` | 123 | Mạng lưới TVV | B | "File thẻ hành nghề" thuộc nhóm 2 hay nhóm 4 (SRS ghi ở cả hai) | 1 chính (3 hướng) + 1 phụ | Bố cục biểu mẫu — chức năng vẫn dùng được |
| 6 | `QLLSHTCTVV_03` | 125 | Mạng lưới TVV | B | Bảng "Lịch sử hỗ trợ" có phải thêm cột "Trạng thái vụ việc" không | 1 chính + 1 phụ | Hiển thị — lọc được nhưng không thấy trạng thái |
| 7 | `QLLSHTCTVV_04` | 126 | Mạng lưới TVV | **A + B** | Bộ lọc trạng thái: giữ tập rút gọn hay đủ 12 giá trị · nhãn "Đã hủy" có thật không | 2 chính + 1 phụ | Sử dụng — bộ lọc chỉ chạm 2/6 bản ghi. Câu trả lời áp cho **2 màn** (`:1578` + `:1856`) |
| 8 | `TKHSYCHTPL_OOS_01` | 145 | Vụ việc HTPL | B | Hồ sơ đã đóng có được giữ mức cảnh báo cũ / lọt bộ lọc SLA không | 3 chính | Gây hiểu nhầm — bộ lọc và cột hiển thị nói hai điều khác nhau |

**Đề nghị thứ tự ưu tiên trả lời:** `QLDXDTTH_11` (chặn luồng) → `DKTGMLTVV_04` (đang làm hai bên đọc hai bản tài liệu khác nhau, sẽ lặp ở mọi vòng sau) → 6 mục còn lại.

---

## Phụ lục A — `NHSYC_01` (row 127): 3 điểm chờ BA do **DEV** nêu, QA chưa thẩm định

Row 127 mang nhãn `BA confirm` ở cột **`Trạng thái dev fix 1`** (cột của dev), nhưng verdict của QA ở cột `Verify` là **`Reopen`** — tức QA đo lại và lỗi **vẫn tái hiện**. Vì vậy mục này **không** nằm trong 8 TC ở trên.

Ghi lại ở đây để BA không bị sót, nguyên văn phần dev nêu:

> *"⚠️ B còn 3 điểm CHỜ BA: thang điểm SRS mâu thuẫn (1=Rất cao vs cộng dồn), ngưỡng LĐ nữ chưa định lượng, `createForDn` ngoài phạm vi — sẽ có phiếu BA riêng."*

**Trạng thái:** dev nói **sẽ có phiếu BA riêng**, tính đến 03/08/2026 **chưa thấy phiếu đó**. QA **chưa tự thẩm định** 3 điểm này (chưa mở SRS đối chiếu, chưa đo lại) nên **không** đưa vào phần chính — nếu BA cần, QA sẽ verify và bổ sung thành mục đầy đủ như 8 mục trên.

---

## Ghi chú vận hành

- Nội dung 8 mục chính **đã được ghi vào cột `DEV phản hồi lần 1` (R)** của đúng 8 dòng trên sheet; mỗi dòng thuộc phần cần BA quyết đều gắn **⚠️ đầu dòng**, còn dòng là **lỗi thật đã chứng minh** gắn **✅** để dev phân biệt ngay trong ô note.
- Ô trạng thái để `BA confirm` ở **cả 2 cột** `Trạng thái dev fix 1` và `Verify` — dropdown của sheet **không có** giá trị "chờ BA confirm", nên ý "đang chờ" được diễn đạt bằng dòng `⚠️ Trạng thái: ĐANG CHỜ BA XÁC NHẬN` trong note.
- 🔴 **Hệ quả cần biết của quy ước trên:** 4/8 TC là case hỗn hợp, bên trong có **6 bug đã chứng minh tái hiện** (`BUG-DKTGMLTVV_05`, `-05-B`, `BUG-QLLSHTCTVV_03`, `-03-B`, `BUG-QLLSHTCTVV_04`). Cả dòng mang nhãn `BA confirm` nên **dev lọc theo nhãn sẽ không thấy 6 bug này** — đó là lý do mỗi mục hỗn hợp đều có khối **"Phần KHÔNG chờ BA"**, và toàn bộ chi tiết nằm ở `../bug-reports/mang-luoi-tvv/bug-report-mang-luoi-tvv.md`.
- **File này là file DUY NHẤT cho tuần 2** (đổi tên từ `ba-confirmation-needed-luong1-dao-tao-2026-08-03.md` ngày 03/08/2026, gộp thêm luồng Mạng lưới TVV và luồng Vụ việc HTPL). Vòng verify nào của tuần 2 phát sinh thêm mục BA confirm thì **thêm vào đây**, không mở file mới.
- Các file `ba-confirmation-needed-week-2.md` và `ba-confirmation-needed-week-2-vong2.md` ở thư mục `reverify-week-2/` là **của các vòng verify trước** và đã có phiếu phản hồi tương ứng — không gộp vào đây để tránh trộn câu hỏi đã được trả lời với câu hỏi đang mở.
