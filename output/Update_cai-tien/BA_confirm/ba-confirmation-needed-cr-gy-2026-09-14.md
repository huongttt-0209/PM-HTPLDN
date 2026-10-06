# BA confirmation needed — Cập nhật cải tiến CR-GY-2026-09-13 (phiếu góp ý 08/09/2026) — 2026-09-14

> **File này để làm gì:** gom các điểm QA **không tự chốt được kết quả mong đợi** khi viết testcase cho đợt cập nhật SRS `[CR-GY-2026-09-13]`. Mỗi câu kèm đối chiếu SRS để BA quyết nhanh. Đây **không phải bug-report** — chức năng chưa có bản dựng để kiểm.

> **Nguồn đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` bản đang có trong repo (commit `01b0116`, 14/09/2026). Mọi số dòng đã mở file kiểm lại ngày 14/09/2026.

> **Chưa có mục "Kết quả verify UI":** tại 14/09/2026 chức năng của đợt này chưa có giao diện. Tất cả câu hỏi dựa trên SRS. Các điểm thuần giao diện (nhãn, tab, bước tiến trình, huy hiệu, vị trí ô) **không** đưa vào file này.

> **Cách trả lời:** mỗi câu chọn Hướng 1 hoặc Hướng 2, hoặc ghi hướng khác. Testcase liên quan đang gắn nhãn `chờ BA – Q0x`.

**Tóm tắt**

| Mã | Chức năng | Loại vấn đề | Ảnh hưởng |
|---|---|---|---|
| CR-GY-Q01 | Chuyển Hỏi đáp → Vụ việc (FR-II-11) | Quy tắc chép dữ liệu vào chỗ không có | Kết quả mong đợi của vụ việc sau khi chuyển |
| CR-GY-Q02 | Hồ sơ hỏi đáp đã chuyển | Hai nơi trong SRS nói ngược nhau | Có sửa / xóa được hồ sơ đã chuyển không |
| CR-GY-Q03 | Xóa vụ việc sinh từ cầu nối | SRS chưa tính trường hợp | Mất yêu cầu của doanh nghiệp |
| CR-GY-Q04 | Kết luận kiểm tra hồ sơ 7 hạng mục (FR-V.I-06) | Quy tắc thiếu nhánh | Trạng thái sau kiểm tra + loại lý do từ chối |
| CR-GY-Q05 | Hạng mục "thuộc phạm vi hỗ trợ" | SRS chưa nói lưu ở đâu | QTHT sửa danh mục có làm hỏng quy tắc không |
| CR-GY-Q06 | Quy mô doanh nghiệp | Hai cột cùng nghĩa | Giá trị điền sẵn + số liệu báo cáo |
| CR-GY-Q07 | Số thẻ tư vấn viên (FR-IV-01) | Ràng buộc mới chưa áp đủ | Cán bộ thêm / sửa TVV thiếu thẻ |
| CR-GY-Q08 *(phụ)* | Thông báo khi chuyển luồng | SRS chưa định nghĩa | Ai nhận, nhận gì |

---

## CR-GY-Q01 — Vụ việc sau khi chuyển luồng: ba trường phân loại lưu ở đâu

**Bối cảnh testcase**

- Nhóm thay đổi T1 — Chuyển hồ sơ hỏi đáp sang vụ việc (FR-II-11).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ chuyển hồ sơ hỏi đáp sang vụ việc, sau đó kiểm tra dữ liệu của vụ việc vừa lập.
- Testcase dự kiến bị ảnh hưởng: bước 7 của FR-II-11 và trường hợp câu hỏi ẩn danh.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-II-11 và BR-FLOW-11, khi chuyển luồng hệ thống **chép ba trường phân loại** (quy mô, hình thức tổ chức, địa bàn doanh nghiệp) sang vụ việc theo nguyên tắc ảnh chụp:
   - Bước 7: chép `quy_mo_dn_id`, `hinh_thuc_to_chuc_id`, `tinh_thanh_dn_id` sang vụ việc.
   - BR-FLOW-11 (a): bản ghi đích mang theo nội dung, tệp đính kèm và các trường phân loại của hồ sơ nguồn.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:978`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5732`

2. Nhưng bảng thuộc tính VU_VIEC **không có ba cột này**, ở cả tệp nền lẫn tệp nhóm Vụ việc. Đợt này chỉ thêm đúng một cột là liên kết truy nguồn `hoi_dap_goc_id`:
   - Bảng VU_VIEC tệp nền: không có `quy_mo_dn_id` / `hinh_thuc_to_chuc_id` / `tinh_thanh_dn_id`.
   - Tệp nhóm Vụ việc: không có chỗ nào nhắc ba tên cột này.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1585`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1600`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2121`

3. Thêm một chỗ chưa rõ: câu hỏi ẩn danh để trống ba trường phân loại. Khi chuyển, cán bộ phải tìm hoặc lập hồ sơ doanh nghiệp trước. SRS không nói ba trường có được điền theo doanh nghiệp vừa gắn không, và hồ sơ hỏi đáp gốc có được ghi nhận doanh nghiệp đó không.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:111`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:942`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:974`

**Câu hỏi cần BA xác nhận**

Vụ việc sinh ra từ cầu nối có giữ riêng ba trường phân loại của hồ sơ hỏi đáp không?

1. **Hướng 1 — vụ việc không giữ riêng:** bỏ bước 7. Vụ việc tra quy mô, hình thức, địa bàn qua hồ sơ doanh nghiệp như mọi vụ việc khác. Ba trường ảnh chụp chỉ nằm trên hồ sơ hỏi đáp.
2. **Hướng 2 — vụ việc giữ ảnh chụp:** vụ việc lưu ba trường tại thời điểm chuyển. SRS cần bổ sung vào bảng thuộc tính VU_VIEC và nói rõ báo cáo nào đọc chúng. Với câu hỏi ẩn danh vừa gắn doanh nghiệp lúc chuyển, BA chốt thêm: ba trường lấy theo doanh nghiệp vừa gắn hay để trống.

**Đề xuất QA tạm thời**

- Chưa có bug. Testcase của bước 7 và trường hợp ẩn danh gắn nhãn `chờ BA – Q01`.
- Phần còn lại của FR-II-11 (trạng thái, liên kết truy nguồn, kênh, 5 mã lỗi `ERR-CL`) viết ngay, không phụ thuộc câu này.
- Nếu BA chọn Hướng 1: bỏ testcase kiểm ba trường trên vụ việc, chỉ kiểm hồ sơ hỏi đáp gốc giữ nguyên ba trường.
- Nếu BA chọn Hướng 2: thêm testcase kiểm ba trường trên vụ việc bằng đúng giá trị của hồ sơ hỏi đáp tại lúc chuyển, không đổi khi hồ sơ doanh nghiệp đổi sau đó.

---

## CR-GY-Q02 — Hồ sơ hỏi đáp đã chuyển luồng còn sửa, xóa được không

**Bối cảnh testcase**

- Nhóm thay đổi T1 — trạng thái mới `DA_CHUYEN_LUONG` ("Đã chuyển sang Vụ việc").
- Nội dung kiểm tra: Cán bộ Nghiệp vụ cùng đơn vị thử sửa và thử xóa mềm một hồ sơ hỏi đáp đã chuyển.
- Testcase dự kiến bị ảnh hưởng: phân quyền thao tác trên hồ sơ `DA_CHUYEN_LUONG`, kiểm được qua API không cần giao diện.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo ghi chú máy trạng thái Hỏi đáp và BR-FLOW-11, hồ sơ đã chuyển là **hồ sơ đã đóng, chỉ đọc**:
   - "Hồ sơ chuyển sang chỉ đọc, không sửa, không soạn phản hồi, không chuyển tiếp lần nữa."
   - BR-FLOW-11 (d): đóng hồ sơ nguồn ở trạng thái riêng mang nghĩa đã chuyển luồng.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1779`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5732`

2. Nhưng ma trận phân quyền thao tác **vẫn cho sửa và xóa mềm**, vì chỉ chặn ba trạng thái Đã duyệt / Công khai / Hoàn thành. Mô tả màn danh sách dùng cùng điều kiện. Ngoài ra, mã `ERR-CL-VV-01` lại tính sẵn trường hợp hồ sơ hỏi đáp gốc "đã xóa mềm":
   - Quyền sửa hỏi đáp: `trang_thai NOT IN (DA_DUYET, CONG_KHAI, HOAN_THANH)`.
   - Quyền xóa mềm hỏi đáp: cùng điều kiện.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1451`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1452`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1279`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1327`

**Câu hỏi cần BA xác nhận**

Hồ sơ hỏi đáp ở trạng thái "Đã chuyển sang Vụ việc" có được sửa hoặc xóa mềm không?

1. **Hướng 1 — theo ghi chú máy trạng thái:** chặn cả sửa lẫn xóa, hồ sơ chỉ đọc. Ma trận phân quyền cần thêm `DA_CHUYEN_LUONG` vào danh sách trạng thái bị chặn. `ERR-CL-VV-01` chỉ còn phục vụ trường hợp dữ liệu hỏng.
2. **Hướng 2 — theo ma trận phân quyền:** cho sửa và xóa như hiện ghi. Khi đó cần nói rõ vụ việc đích xử lý thế nào khi hồ sơ gốc bị xóa (hiện chỉ có cảnh báo `ERR-CL-VV-01`).

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1, vì khớp BR-FLOW-11 (d) và ghi chú máy trạng thái. Hai chỗ đó mới là phần viết cho đợt này; ma trận phân quyền có từ trước và chưa được cập nhật.
- Testcase sửa / xóa hồ sơ `DA_CHUYEN_LUONG` gắn nhãn `chờ BA – Q02`.
- Nếu BA chọn Hướng 1: kỳ vọng hệ thống từ chối sửa và xóa, hồ sơ giữ nguyên.
- Nếu BA chọn Hướng 2: kỳ vọng sửa / xóa thành công; thêm testcase mở vụ việc đích sau khi hồ sơ gốc bị xóa → cảnh báo `ERR-CL-VV-01`.

---

## CR-GY-Q03 — Xóa vụ việc sinh từ cầu nối thì hồ sơ hỏi đáp gốc ra sao

**Bối cảnh testcase**

- Nhóm thay đổi T1 — vụ việc đích của cầu nối (FR-V.I-18).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ xóa mềm một vụ việc vừa sinh từ cầu nối khi vụ việc còn ở trạng thái Chờ tiếp nhận.
- Testcase dự kiến bị ảnh hưởng: trường hợp biên của cầu nối.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-V.I-05 (hồ sơ từ hệ thống khác), cán bộ **xóa mềm được** vụ việc kênh `HE_THONG_KHAC` khi còn Chờ tiếp nhận. Vụ việc từ cầu nối **lọt vào đúng nhóm này** khi hồ sơ hỏi đáp gốc có kênh `HE_THONG_KHAC`, vì kênh được giữ nguyên:
   - Hồ sơ hỏi đáp kênh `DVC` / `HE_THONG_KHAC` / `TRUC_TIEP` → vụ việc giữ nguyên kênh.
   - Vụ việc từ cầu nối khởi tạo ở `CHO_TIEP_NHAN`.
   - Màn quản lý hồ sơ từ hệ thống khác lấy vụ việc **theo kênh** `HE_THONG_KHAC` và cho xóa mềm khi còn `CHO_TIEP_NHAN`.
   - Bảng CRUD cho Cán bộ Nghiệp vụ quyền xóa trên VU_VIEC.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:964`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:976`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:427`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:430`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:460`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1351`

2. Nhưng xóa xong thì **hồ sơ hỏi đáp gốc kẹt lại**. Nó vẫn đóng ở trạng thái đã chuyển và không chuyển lại được, vì mỗi hồ sơ chỉ chuyển một lần. SRS chỉ nói trường hợp vụ việc **bị từ chối** thì không mở lại hồ sơ gốc; trường hợp vụ việc **bị xóa** chưa được tính. Ngoài ra, BR-FLOW-11 (g) quy định nhận biết hồ sơ chuyển luồng qua liên kết truy nguồn, không qua kênh, trong khi FR-V.I-05 vẫn lọc theo kênh:
   - Điều kiện chuyển: `vu_viec_dich_id` còn trống; cột này có ràng buộc duy nhất.
   - Vụ việc bị từ chối: không mở lại hồ sơ gốc.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:935`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1564`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1311`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5732`

**Câu hỏi cần BA xác nhận**

Vụ việc có liên kết về hồ sơ hỏi đáp gốc có được xóa mềm không?

1. **Hướng 1 — chặn xóa:** vụ việc sinh từ cầu nối không xóa được, kể cả khi còn Chờ tiếp nhận. Muốn dừng thì đi đường từ chối, và doanh nghiệp nhận hướng dẫn gửi lại theo đường hỏi đáp.
2. **Hướng 2 — cho xóa, mở lại hồ sơ gốc:** xóa vụ việc thì hồ sơ hỏi đáp gốc quay về trạng thái trước khi chuyển và bỏ liên kết, để xử lý tiếp hoặc chuyển lại.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1, vì nhất quán với quyết định "không mở lại hồ sơ gốc" của trường hợp từ chối.
- Testcase xóa vụ việc từ cầu nối gắn nhãn `chờ BA – Q03`.
- Nếu BA chọn Hướng 1: kỳ vọng hệ thống từ chối xóa; màn hồ sơ từ hệ thống khác cũng không cho xóa vụ việc có liên kết.
- Nếu BA chọn Hướng 2: kỳ vọng xóa xong, hồ sơ gốc trở lại trạng thái cũ và chuyển lại được lần nữa.

---

## CR-GY-Q04 — Kết luận kiểm tra hồ sơ khi dùng checklist 7 hạng mục

**Bối cảnh testcase**

- Nhóm thay đổi T2 — thêm hạng mục "thuộc phạm vi hỗ trợ" và loại lý do từ chối (FR-V.I-06).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ tích checklist rồi chọn kết luận Đạt / Không đạt / Yêu cầu bổ sung.
- Testcase dự kiến bị ảnh hưởng: các tổ hợp giữa kết quả checklist và kết luận.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-V.I-06, **kết luận do cán bộ chọn**, còn loại lý do từ chối do hệ thống tự suy ra từ checklist:
   - Kết luận: Đạt / Không đạt / Yêu cầu bổ sung.
   - Loại lý do bắt buộc khi Không đạt, chỉ có hai nhánh: hạng mục 1 không đạt → Ngoài phạm vi; hạng mục 1 đạt nhưng có hạng mục 2–7 không đạt → Thiếu thành phần hồ sơ.
   - Hạng mục 1 không đạt: hệ thống đặt loại lý do Ngoài phạm vi, không bắt tích tiếp hạng mục 2–7. SRS **không nói** hệ thống có ép kết luận Không đạt không.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:522`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:524`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:566`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:569`

2. Nhưng FR-V.I-18 viết cho vụ việc từ cầu nối lại coi như **ngoài phạm vi thì từ chối**. Bảng lỗi của FR-V.I-06 không có lỗi nào cho tổ hợp sai:
   - "Thiếu giấy tờ → Yêu cầu bổ sung; ngoài phạm vi → Từ chối."
   - Lỗi hiện có: chỉ `ERR-KT-01` (sai trạng thái) và `ERR-KT-02` (thiếu lý do).

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1310`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:584`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:585`

**Câu hỏi cần BA xác nhận**

(a) Khi hạng mục 1 không đạt, cán bộ còn chọn được kết luận Đạt hoặc Yêu cầu bổ sung không?

1. **Hướng 1 — ép từ chối:** hạng mục 1 không đạt thì chỉ cho kết luận Không đạt, và hồ sơ chuyển Từ chối với lý do Ngoài phạm vi.
2. **Hướng 2 — cán bộ tự quyết:** hạng mục 1 chỉ gợi ý loại lý do; cán bộ vẫn chọn kết luận bất kỳ.

(b) Khi cả 7 hạng mục đều đạt mà cán bộ chọn Không đạt, loại lý do bắt buộc nhưng không có quy tắc nào suy ra giá trị. Xử lý thế nào?

1. **Hướng 1 — không cho chọn:** 7 hạng mục đạt thì không cho kết luận Không đạt.
2. **Hướng 2 — thêm loại lý do thứ ba** (vd "Lý do khác") để cán bộ tự ghi.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 cho cả (a) và (b), để loại lý do luôn suy ra được và số liệu thống kê "ngoài phạm vi / thiếu tài liệu" không lẫn.
- Hai tổ hợp này gắn nhãn `chờ BA – Q04`. Các tổ hợp đã rõ (hạng mục 1 đạt + thiếu giấy → bổ sung hoặc từ chối "Thiếu thành phần hồ sơ") viết ngay.

---

## CR-GY-Q05 — Hạng mục "thuộc phạm vi hỗ trợ" là cố định hay nằm trong danh mục cấu hình

**Bối cảnh testcase**

- Nhóm thay đổi T2 — checklist kiểm tra hồ sơ từ 6 lên 7 hạng mục.
- Nội dung kiểm tra: Quản trị hệ thống sửa danh mục hồ sơ đề nghị hỗ trợ; Cán bộ Nghiệp vụ kiểm tra hồ sơ sau khi danh mục đổi.
- Testcase dự kiến bị ảnh hưởng: dữ liệu mồi của checklist và testcase hồi quy danh mục UC106.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-V.I-06, checklist có 7 hạng mục; **hạng mục 1 là kết luận về phạm vi, không phải thành phần hồ sơ**, và có quy tắc riêng (không đạt → Ngoài phạm vi):
   - 7 hạng mục chia 2 nhóm; hạng mục 1 thuộc nhóm Phạm vi hỗ trợ.
   - Bước 3: tải checklist "từ cấu hình UC106 (7 hạng mục)".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:526`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:529`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:564`

2. Nhưng "cấu hình UC106" là danh mục FR-VIII-08, **Quản trị hệ thống thêm, sửa, xóa được**. Danh mục này chỉ có thành phần hồ sơ bắt buộc / tùy chọn, không có chỗ cho hạng mục phạm vi, và chưa có dữ liệu mồi:
   - FR-VIII-08: trường `thanh_phan_bat_buoc`, `thanh_phan_tuy_chon`, theo mẫu CRUD danh mục.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:420`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:433`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:434`

**Câu hỏi cần BA xác nhận**

Hạng mục 1 "Vụ việc thuộc phạm vi hỗ trợ" nằm ở đâu?

1. **Hướng 1 — cố định trong hệ thống:** hạng mục 1 luôn đứng đầu checklist, Quản trị hệ thống không sửa hay xóa được. Danh mục UC106 chỉ quản lý 6 thành phần hồ sơ (hạng mục 2–7).
2. **Hướng 2 — là một bản ghi trong danh mục UC106:** khi đó cần nói hệ thống nhận ra "hạng mục phạm vi" bằng cách nào, và chuyện gì xảy ra khi Quản trị hệ thống xóa hoặc đổi thứ tự bản ghi đó.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1, vì hạng mục 1 mang quy tắc nghiệp vụ riêng, không phải giấy tờ.
- Testcase "Quản trị hệ thống sửa danh mục → checklist đổi theo" gắn nhãn `chờ BA – Q05`.

---

## CR-GY-Q06 — Quy mô doanh nghiệp lấy từ cột nào

**Bối cảnh testcase**

- Nhóm thay đổi T3 và T4 — trường quy mô trên hồ sơ hỏi đáp, chiều quy mô trên báo cáo hỏi đáp, đổi nhãn hai báo cáo "theo quy mô DN".
- Nội dung kiểm tra: Cán bộ Nghiệp vụ chọn doanh nghiệp khi tạo / tiếp nhận câu hỏi → hệ thống điền sẵn quy mô; báo cáo gom theo quy mô.
- Testcase dự kiến bị ảnh hưởng: giá trị điền sẵn, báo cáo FR-IX-01, FR-IX-13, FR-IX-18.

**Điểm mâu thuẫn trong SRS v3.5**

1. Hồ sơ doanh nghiệp đang có **hai cột cùng mô tả quy mô**:
   - `loai_dn_id`: chọn từ danh mục Quy mô doanh nghiệp (UC105). FR-V.III-01 ghi **không bắt buộc** khi cán bộ nhập, nhưng bảng thuộc tính tệp nền ghi **bắt buộc**.
   - `quy_mo`: SIEU_NHO / NHO / VUA, hệ thống tự tính theo BR-CALC-05 và dùng tính mức hỗ trợ chi phí. Cột này có ở FR-V.III-01 nhưng **không có** trong bảng thuộc tính DOANH_NGHIEP tệp nền.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:106`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:108`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1734`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1746`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5746`

2. Các chức năng của đợt này **đọc hai cột khác nhau**:
   - Hồ sơ hỏi đáp điền sẵn quy mô theo **danh mục** (tức `loai_dn_id`); báo cáo hỏi đáp FR-IX-01 lọc theo đó.
   - Báo cáo FR-IX-13 và FR-IX-18 lọc theo **SIEU_NHO / NHO / VUA**, đúng dạng giá trị của `quy_mo`.
   - Hệ quả: nếu hai cột lệch, hoặc doanh nghiệp chỉ có `quy_mo`, hồ sơ hỏi đáp điền sẵn trống và báo cáo quy mô của Hỏi đáp và Vụ việc ra số khác nhau cho cùng một doanh nghiệp.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:111`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:154`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:683`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:863`

**Câu hỏi cần BA xác nhận**

Cột nào là nguồn chuẩn của "Quy mô doanh nghiệp"?

1. **Hướng 1 — `loai_dn_id` (danh mục):** hồ sơ hỏi đáp điền sẵn và mọi báo cáo quy mô đọc cột này. Cần nói rõ cột này bắt buộc hay tùy chọn, và cách đồng bộ với `quy_mo` đang dùng tính mức hỗ trợ.
2. **Hướng 2 — `quy_mo` (tự tính theo BR-CALC-05):** hồ sơ hỏi đáp điền sẵn từ cột này; danh mục chỉ để hiển thị nhãn. Cần bổ sung `quy_mo` vào bảng thuộc tính DOANH_NGHIEP tệp nền.

**Đề xuất QA tạm thời**

- Không nghiêng hướng nào — đây là quyết định dữ liệu, cần BA và Dev cùng chốt.
- Testcase điền sẵn quy mô và đối chiếu số liệu giữa báo cáo hỏi đáp và báo cáo vụ việc gắn nhãn `chờ BA – Q06`.
- Seed dữ liệu thử tạm dùng doanh nghiệp có **cả hai cột cùng giá trị**, để các testcase khác không bị kẹt.

---

## CR-GY-Q07 — Số thẻ tư vấn viên khi cán bộ thêm hoặc sửa trực tiếp (FR-IV-01)

**Bối cảnh testcase**

- Nhóm thay đổi T6 — số thẻ và tệp thẻ hành nghề bắt buộc khi loại là Tư vấn viên, không hồi tố.
- Nội dung kiểm tra: Cán bộ Nghiệp vụ thêm mới hoặc sửa tư vấn viên loại "Tư vấn viên" mà không có số thẻ.
- Testcase dự kiến bị ảnh hưởng: luồng cán bộ nhập tay TVV (FR-IV-01).

**Điểm mâu thuẫn trong SRS v3.5**

1. Đợt này **siết bắt buộc** số thẻ và tệp thẻ với loại Tư vấn viên, kèm hai mã lỗi chặn — nhưng chỉ gắn với hai chức năng:
   - Đăng ký tham gia mạng lưới (FR-IV-03): thiếu → `ERR-DK-10`.
   - Cập nhật năng lực (FR-IV-04): thiếu → `ERR-NL-06`; ràng buộc chỉ chặn tại thời điểm lưu của FR-IV-04.
   - Màn nhập hồ sơ SCR-IV-02 ghi bắt buộc khi loại là Tư vấn viên (đăng ký mới → `ERR-DK-10`, cập nhật → `ERR-NL-06`).

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:352`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:413`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:453`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1554`

2. Nhưng FR-IV-01 (Quản lý TVV — cán bộ thêm, sửa, xóa) **dùng chung màn SCR-IV-02** mà vẫn để số thẻ **không bắt buộc** và không có mã lỗi. Trường đó còn trỏ tới cột `so_the` đã bỏ khỏi bảng TU_VAN_VIEN:
   - FR-IV-01 trường 12 `so_the`: không bắt buộc.
   - Tiêu chí chấp nhận: cán bộ thêm TVV, nhập đủ trường bắt buộc → tạo TVV mới ở trạng thái Mới đăng ký.
   - Bảng TU_VAN_VIEN: `the_hanh_nghe` đã bỏ, chuyển sang hồ sơ tư vấn viên.
   - Bước thẩm định vẫn có mục "Thẻ hành nghề còn hiệu lực" cán bộ tích tay, nhưng đó là kiểm thủ công, không phải chặn khi lưu.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:122`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:149`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:213`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1838`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1620`

**Câu hỏi cần BA xác nhận**

Ràng buộc số thẻ có áp cho thao tác thêm và sửa của cán bộ ở FR-IV-01 không?

1. **Hướng 1 — áp như đăng ký / cập nhật:** cán bộ thêm TVV loại Tư vấn viên thiếu số thẻ hoặc tệp thẻ thì bị chặn (mã lỗi của đăng ký mới). Cán bộ sửa hồ sơ đã duyệt thiếu thẻ cũng bị chặn khi lưu, như FR-IV-04. Trường 12 của FR-IV-01 sửa lại cho khớp.
2. **Hướng 2 — không áp cho cán bộ:** cán bộ vẫn thêm / sửa được khi thiếu thẻ; việc kiểm thẻ dồn về bước thẩm định. Khi đó cần ghi rõ ngoại lệ này để không bị coi là lỗ hổng.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1, vì SCR-IV-02 là màn dùng chung và đã ghi bắt buộc.
- Testcase thêm / sửa TVV qua FR-IV-01 khi thiếu thẻ gắn nhãn `chờ BA – Q07`. Testcase đăng ký (FR-IV-03) và cập nhật năng lực (FR-IV-04) viết ngay.

---

## CR-GY-Q08 *(phụ, không gấp)* — Thông báo khi chuyển hồ sơ hỏi đáp sang vụ việc

**Bối cảnh testcase**

- Nhóm thay đổi T1 — FR-II-11 bước 11.
- Nội dung kiểm tra: sau khi chuyển, doanh nghiệp và cán bộ nhóm Vụ việc của đơn vị thụ lý nhận thông báo.

**Điểm SRS chưa định nghĩa**

1. FR-II-11 bước 11 gửi thông báo cho doanh nghiệp và cán bộ nhóm Vụ việc, dẫn chiếu BR-NOTIF-01. Nhưng danh sách sự kiện kích hoạt của BR-NOTIF-01 **không có sự kiện chuyển luồng**, và SRS không có nội dung thông báo.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:982`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5800`

2. Hồ sơ ở trạng thái Đang xử lý **luôn đã được phân công** cho người hỗ trợ / tư vấn viên, và người đó đang xem được hồ sơ. SRS không nói người này có được báo khi hồ sơ bị chuyển đi không.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1733`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1457`

**Câu hỏi cần BA xác nhận**

- Nội dung thông báo gửi doanh nghiệp và gửi cán bộ nhóm Vụ việc là gì?
- Doanh nghiệp gắn vào lúc chuyển (câu hỏi ẩn danh) có thể chưa có tài khoản: thông báo gửi qua đâu?
- Người hỗ trợ / tư vấn viên đang được phân công hồ sơ hỏi đáp có nhận thông báo không?

**Đề xuất QA tạm thời**

- Testcase chỉ kiểm **có thông báo tới đúng hai nhóm người nhận**, chưa kiểm nội dung. Phần nội dung và người hỗ trợ gắn nhãn `chờ BA – Q08`.

---

## Giả định QA tự áp khi viết testcase (BA không cần trả lời — chỉ phản hồi nếu thấy sai)

| # | Giả định | Căn cứ |
|---|---|---|
| G1 | Tiếp nhận hồ sơ chưa có lĩnh vực mà không chọn lĩnh vực → hệ thống chặn và báo cần chọn lĩnh vực. SRS không có mã lỗi riêng nên testcase không kiểm mã. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:336`, `:346`, `:347` |
| G2 | KPI-S-03 "vụ việc đóng trong kỳ" hiểu giống KPI-S-02: vụ việc trạng thái Hoàn thành có ngày hoàn thành trong kỳ. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:655`, `:615` |
| G3 | Gợi ý câu hỏi tương tự (FR-II-12) chỉ chạy ở màn tiếp nhận và màn soạn phản hồi, và chỉ khi hồ sơ đã có lĩnh vực. Mở màn tiếp nhận của hồ sơ chưa có lĩnh vực → không có gợi ý. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1033`, `:1059` |

## Không đưa vào file này

- **Đang chờ CĐT — BA không trả lời được:** H1 (ai nhập ba trường phân loại), V1 (màn chưa bắt chọn lĩnh vực), V3 (mở chiều sang Tư vấn chuyên sâu), A5 (hai chiều Quy mô / Hình thức tổ chức ở báo cáo hỏi đáp), T8 (hộ kinh doanh, hợp tác xã). SRS đã ghi treo tại `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:131`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:117`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:185`. Testcase vẫn viết, gắn nhãn `chờ CĐT`.
- **Điểm thuần giao diện:** số tab và nhãn ở màn Quản trị danh mục, bước tiến trình, huy hiệu, bộ lọc trạng thái, vị trí khối gợi ý, vị trí các ô trên màn Tiếp nhận và màn Doanh nghiệp, nhãn kênh `CONG_PLQG` của vụ việc. Để lại tới khi có giao diện.
