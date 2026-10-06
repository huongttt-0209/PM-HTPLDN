# BA confirmation needed (bổ sung) — Cập nhật cải tiến CR-GY-2026-09-13 — 2026-09-14

> **File này để làm gì:** gom các câu **BA chưa trả lời** của đợt `[CR-GY-2026-09-13]` — chỗ QA không tự chốt được kết quả mong đợi khi viết testcase. Câu nào BA đã trả lời (bằng thư phản hồi hoặc đã sửa vào SRS) không còn ở đây; testcase đã viết lại theo SRS. File đi kèm, **không thay** file gửi trước `ba-confirmation-needed-cr-gy-2026-09-14.md` (Q01–Q08, G1–G3 — BA đã trả lời hết). Q09–Q22 phát hiện khi viết bộ testcase đầy đủ; **Q23–Q25 thêm tối 14/09** khi rà biên (Edge Case Hunter) toàn bộ 11 file testcase — mỗi câu gắn với một TC mới không chấm được nếu thiếu câu trả lời. Ba mục **hỏi thêm** (Q03, Q06, Q07) sinh ra từ chính lần BA sửa SRS. Đây **không phải bug-report** — chức năng chưa có bản dựng để kiểm.

> **Nguồn đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` commit `aaee63b` — bản BA đã áp phần giải đáp phiếu QA (Q01–Q08) và phiếu Dev (BA-R1, BA-R2). Mọi số dòng trong file đọc trên bản này. Trong câu chữ, vài chỗ viết gọn `fr-NN:dòng` = tệp `srs-fr-NN-….md` trong cùng thư mục (ví dụ `fr-02:1036` = `srs-fr-02-hoi-dap.md` dòng 1036).

> **Chưa có mục "Kết quả verify UI":** chức năng chưa có giao diện. Các điểm thuần giao diện **không** đưa vào file này.

> **Cách trả lời:** mỗi câu chọn Hướng 1 hoặc Hướng 2, hoặc ghi hướng khác. Testcase liên quan đang gắn nhãn `chờ BA – Qxx` trong `output/Update_cai-tien/Testcase/`. Mục "Sửa tài liệu" ở cuối không cần quyết định.

**Tóm tắt**

| Mã | Chức năng | Loại vấn đề | Ảnh hưởng |
|---|---|---|---|
| CR-GY-Q03 (hỏi thêm) | Xóa vụ việc cầu nối còn Chờ tiếp nhận (FR-V.I-05 bước 5a) | Danh sách của màn xóa chỉ lấy kênh `HE_THONG_KHAC`; nút Xóa hàng loạt không có phần xử lý | Vụ việc cầu nối kênh khác xóa ở đâu; lô xóa lẫn vụ việc cầu nối; `TC-VVCL-024` chờ |
| CR-GY-Q06 (hỏi thêm) | Quy mô doanh nghiệp (FR-V.III-01, FR-VIII-22) | Một cột lưu nhưng còn hai ô nhập | Hai ô gửi lệch nhau thì từ chối hay lấy ô nào |
| CR-GY-Q07 (hỏi thêm) | Thẻ hành nghề — người hỗ trợ cập nhật TVV (FR-IV-11) | Ràng buộc thẻ chỉ nêu FR-IV-01, FR-IV-04 | Lần lưu FR-IV-11 trên TVV thiếu thẻ có bị chặn không |
| CR-GY-Q09 | Kiểm tra hồ sơ 7 hạng mục (FR-V.I-06) | Loại lý do từ chối không có chỗ lưu, không báo cáo nào đọc | Không thống kê được theo loại lý do; quy tắc nhóm "Không xác định" không có chỗ áp |
| CR-GY-Q10 | Chuyển Hỏi đáp → Vụ việc sang **đơn vị khác** | Không nêu tập đơn vị được chọn | CB NV chọn được đơn vị nào (quyền đọc hai bên đã chốt) |
| CR-GY-Q11 | Vụ việc cầu nối mang kênh `DVC` | Kế thừa kênh nhưng không có mã hồ sơ DVC | Đồng bộ trạng thái về LGSP sai hoặc lỗi |
| CR-GY-Q12 | KPI-S-03 Thời gian xử lý toàn trình | Thiếu quy ước chung của thẻ KPI; tập "vụ việc đóng trong kỳ" | Số trên thẻ; vụ việc đã đánh giá, vụ việc từ chối có tính không |
| CR-GY-Q13 | Trạng thái `DA_CHUYEN_LUONG` | Chưa nói mức cảnh báo thời hạn trong lúc hồ sơ ở trạng thái đã chuyển | Mức cảnh báo: để trống, đứng yên hay lên tiếp; tra cứu "câu hỏi đã xử lý" |
| CR-GY-Q14 | Báo cáo hỏi đáp FR-IX-01 | Chưa có bảng trạng thái → nhóm | Tổng, ba nhóm và tỷ lệ trả lời |
| CR-GY-Q15 | KPI-S-03 — vụ việc tiếp nhận trực tiếp | Ghi chú trái quy tắc tính: mốc ngày tạo hay ngày tiếp nhận | Số trên thẻ; `TC-KPI3-002` (P0) chờ |
| CR-GY-Q16 | Báo cáo FR-IX-02, FR-IX-13 | Công thức riêng trái bước 4 TPL-REPORT-FULL | Có đếm vụ việc đang xử lý không; mốc "trong kỳ" của FR-IX-13 |
| CR-GY-Q17 | Thẩm định hồ sơ TVV FR-IV-06 | Phần xử lý và màn hình SCR-IV-03 khác nhau | Nhóm Pháp lý Không đạt có được "Yêu cầu bổ sung" không |
| CR-GY-Q18 | Báo cáo chi phí FR-IX-18 | Ba cột tiền chưa có công thức; "NĐ55" trái BR-CALC-01 | `tong_chi_phi`, `tran_chi_phi`, `chenh_lech` |
| CR-GY-Q19 | Đăng ký DN FR-VIII-22; CB NV thêm DN FR-V.III-NEW-03 | Dẫn chiếu FR-V.III-01 nhưng thiếu trường 7a (D9 cũ) | Có nhận hình thức tổ chức không |
| CR-GY-Q20 | Đăng ký TVV FR-IV-03 | `ERR-DK-05` tổng 50 MB không gắn ô nào | Lần gửi nhiều tệp minh chứng bị chặn hay không |
| CR-GY-Q21 | Gợi ý câu hỏi tương tự FR-II-12 | Phạm vi toàn quốc trái quyền đọc kho theo đơn vị | Gợi ý có bản ghi đơn vị khác không; mở được không |
| CR-GY-Q22 | Tiếp nhận FR-II-03 trường 3 | Không có đường tạo hồ sơ thiếu lĩnh vực | Ba TC (hai P0) chỉ chạy trên dữ liệu DBA sửa tay |
| CR-GY-Q23 | Chỉnh sửa hỏi đáp FR-II-01 — gắn doanh nghiệp vào hồ sơ ẩn danh **sau khi đã tiếp nhận** | Ba trường ảnh chụp 12–14: điền theo doanh nghiệp hay giữ trống | Hồ sơ vào nhóm "Không xác định" hay nhóm của doanh nghiệp ở FR-IX-01; `TC-PL-021` chờ |
| CR-GY-Q24 | Số thẻ hành nghề FR-IV-03 / FR-IV-01 / FR-IV-04 | Không có UNIQUE trong khi CCCD, email UNIQUE toàn hệ thống; không mã lỗi trùng | Hai tư vấn viên cùng số thẻ lưu được hay bị chặn; `TC-THN-027` chờ |
| CR-GY-Q25 | Báo cáo hỏi đáp FR-IX-01 — kỳ | Không nói mốc ngày xếp hồ sơ vào kỳ; nhóm theo trạng thái lúc chạy hay tại cuối kỳ | Số của hai kỳ khi hồ sơ tạo và chuyển khác tháng; `TC-BC01-025` một phần |

---

## CR-GY-Q03 (hỏi thêm) — Xóa vụ việc cầu nối: vụ việc không thuộc kênh `HE_THONG_KHAC` xóa ở đâu, xóa hàng loạt xử lý thế nào

**Bối cảnh testcase**

- Q03 đã chốt trong SRS `aaee63b`: vụ việc sinh từ cầu nối còn Chờ tiếp nhận xóa được và kéo theo mở lại hồ sơ hỏi đáp gốc (FR-II-11 §Hoàn tác); đã tiếp nhận thì chặn `ERR-INTG-06`. Hai điểm dưới sinh ra từ chính lần sửa.
- Nội dung kiểm tra: (a) xóa vụ việc cầu nối kênh `TRUC_TIEP` còn Chờ tiếp nhận; (b) xóa hàng loạt một lô lẫn vụ việc thường, vụ việc cầu nối còn Chờ tiếp nhận và vụ việc cầu nối đã tiếp nhận.
- Testcase bị ảnh hưởng: `TC-VVCL-024` (cả TC chờ); `TC-HQHD-026` (phần thông báo, bảng lỗi từng dòng — viết sẵn hai hướng). `TC-HQHD-014` (vụ việc kênh `HE_THONG_KHAC`) chấm ngay.

**Điểm SRS chưa nói**

1. Bước 5a / 5b nhận biết vụ việc cầu nối theo `hoi_dap_goc_id`, **không** theo kênh — mọi vụ việc cầu nối còn Chờ tiếp nhận đều xóa được:
   - "| 5a | **Vụ việc sinh từ cầu nối Hỏi đáp** (`hoi_dap_goc_id` có giá trị): chỉ xóa được khi còn `CHO_TIEP_NHAN`. Đã tiếp nhận → chặn, trả `ERR-INTG-06`. Khi xóa, **kéo theo mở lại hồ sơ hỏi đáp gốc** …"
   - "| 5b | Nhận biết vụ việc từ cầu nối căn theo **`hoi_dap_goc_id` có giá trị**, KHÔNG căn theo kênh tiếp nhận …"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:431`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:432`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:471`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1036`

2. Nhưng 5a / 5b nằm trong FR-V.I-05 (hồ sơ từ hệ thống khác), mà danh sách của chức năng này chỉ lấy vụ việc kênh `HE_THONG_KHAC`. Vụ việc cầu nối mang kênh kế thừa của hồ sơ gốc (ví dụ `TRUC_TIEP`) không có trong danh sách đó. Hậu điều kiện xóa cũng chưa nêu việc mở lại hồ sơ gốc:
   - "| 2 | Xem danh sách: lấy VV kênh HE_THONG_KHAC chưa xóa, áp dụng filter + phân trang |"
   - "| CMS Xóa | VU_VIEC.is_deleted = 1 (chỉ khi trang_thai = 'CHO_TIEP_NHAN'), AUDIT_LOG ghi nhận |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:427`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:462`

3. Màn danh sách vụ việc chung (SCR-V.I-01) có nút Xóa từng dòng và Xóa hàng loạt, nhưng không phần xử lý nào nêu điều kiện xóa hay dẫn tới bước 5a. Xóa hàng loạt chỉ có hộp xác nhận, không có bảng lỗi từng dòng. Nếu lô xóa mềm vụ việc cầu nối mà không mở lại hồ sơ gốc, hồ sơ gốc kẹt ở `DA_CHUYEN_LUONG` — không sửa, không xóa (BR-FLOW-03), không chuyển lại được:
   - "| 22 | table | Hành động | icon buttons | 👁 Xem → MH-05.3 / ✏ Sửa → MH-05.2 / 🗑 Xóa (C12 confirm) …"
   - "| 23 | action-bar | Thanh hành động hàng loạt | buttons | ☐ Chọn tất cả + [Xóa hàng loạt] …"
   - "| Xóa hàng loạt | Confirm modal | "Bạn sắp xóa {N} vụ việc. Tiếp tục?" |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1797`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1798`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1735`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1912`

**Câu hỏi cần BA xác nhận**

(a) Vụ việc cầu nối không thuộc kênh `HE_THONG_KHAC`, còn Chờ tiếp nhận, xóa được ở đâu?

1. **Hướng 1 — xóa từ danh sách vụ việc chung** (SCR-V.I-01 dòng 22, 23): bổ sung phần xử lý cho nút Xóa ở đó — cùng điều kiện 5a (chỉ `CHO_TIEP_NHAN`, đã tiếp nhận trả `ERR-INTG-06`) và kéo theo hoàn tác.
2. **Hướng 2 — chỉ FR-V.I-05 xóa được**, tức chỉ vụ việc cầu nối kênh `HE_THONG_KHAC`. Vụ việc cầu nối kênh khác không xóa được — muốn dừng thì tiếp nhận rồi từ chối, hồ sơ gốc không mở lại (`fr-02:1036`). Khi đó sửa 5b cho khớp.

(b) Xóa hàng loạt một lô có vụ việc cầu nối: mỗi vụ việc cầu nối còn Chờ tiếp nhận có kéo theo hoàn tác cho hồ sơ gốc không; vụ việc cầu nối đã tiếp nhận bị loại khỏi lô (báo `ERR-INTG-06` cho dòng đó) hay chặn cả lô?

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 cho (a) — bước 5b cố ý không căn theo kênh, và lý do hoàn tác ("hồ sơ tạo nhầm và chưa ai xem xét") đúng với mọi kênh. Với (b), QA nghiêng về xử lý từng vụ việc trong lô như xóa đơn lẻ (hoàn tác, hoặc loại khỏi lô kèm mã lỗi), để không hồ sơ gốc nào kẹt.
- `TC-VVCL-024` gắn `chờ BA – Q03 (hỏi thêm)`, ghi sẵn hai hướng. `TC-HQHD-026` chấm ngay bất biến "vụ việc cầu nối bị xóa mềm ⇔ hồ sơ gốc mở lại" — đúng ở mọi hướng; phần thông báo và bảng lỗi từng dòng chấm theo hướng BA chốt.

---

## CR-GY-Q06 (hỏi thêm) — Quy mô doanh nghiệp còn hai ô nhập: gửi hai giá trị lệch nhau thì sao

**Bối cảnh testcase**

- Q06 đã chốt trong SRS `aaee63b`: `loai_dn_id` là cột lưu duy nhất của quy mô doanh nghiệp; FR-IX-13, FR-IX-18 gom theo cột này.
- Nội dung kiểm tra: thêm / sửa doanh nghiệp khi hai ô quy mô gửi lên hai giá trị khác nhau.
- Testcase bị ảnh hưởng: `TC-PL-006`, `TC-HQBC-007` — chỉ dòng Ghi lại (kết quả chính chấm ngay).

**Điểm SRS chưa nói**

1. SRS chốt một cột lưu:
   - "`loai_dn_id` … **Quy mô doanh nghiệp**: siêu nhỏ / nhỏ / vừa. Nhãn hiển thị đổi thành "Quy mô doanh nghiệp" …"
   - "gom theo `DOANH_NGHIEP.loai_dn_id` — **cột lưu duy nhất** của quy mô doanh nghiệp"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:695`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1746`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:666`

2. Nhưng đầu vào vẫn có hai ô, bước xử lý vẫn tự tính và cho sửa ô thứ hai, sơ đồ thực thể còn cột `quy_mo`, và form doanh nghiệp tự đăng ký bắt buộc cả hai:
   - FR-V.III-01: "| 7 | loai_dn_id | identifier | **N** | … **Tùy chọn** cho 5 kênh CB NV/API; bắt buộc khi DN tự đăng ký." và "| 8 | quy_mo | text | **N** | SIEU_NHO / NHO / VUA. …"
   - "| 5 | Auto-calc `quy_mo` theo BR-CALC-05 … CB NV có thể override |"
   - Sơ đồ thực thể: "text quy_mo"
   - FR-VIII-22: "| 6 | loai_doanh_nghiep_id | identifier | Y |" và "| 7 | quy_mo | text | Y | SIEU_NHO / NHO / VUA (theo NĐ 80/2021) |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:106`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:108`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:296`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:641`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1064`–`:1065`

**Câu hỏi cần BA xác nhận**

Hai ô gửi lên lệch nhau thì hệ thống xử lý thế nào?

1. **Hướng 1 — bỏ ô `quy_mo` khỏi đầu vào:** bỏ trường 8 của FR-V.III-01 và trường 7 của FR-VIII-22; bước 5 tự tính ghi thẳng vào `loai_dn_id`; bỏ `quy_mo` khỏi sơ đồ thực thể.
2. **Hướng 2 — giữ hai ô, thêm quy tắc:** lệch nhau thì từ chối (nêu mã lỗi), hoặc nêu ô nào thắng.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — khớp quyết định "một cột lưu" của Q06.
- `TC-PL-006`, `TC-HQBC-007` chấm theo `loai_dn_id`; cách hệ thống xử lý hai ô lệch nhau chỉ ghi lại.

---

## CR-GY-Q07 (hỏi thêm) — Người hỗ trợ cập nhật tư vấn viên thiếu thẻ (FR-IV-11): có bị chặn không

**Bối cảnh testcase**

- Q07 đã chốt trong SRS `aaee63b`: FR-IV-01 chặn hồ sơ tư vấn viên thiếu số thẻ hoặc tệp thẻ (`ERR-TVV-10`), kể cả khi sửa hồ sơ đã duyệt; không hồi tố lên hồ sơ không ai mở.
- Nội dung kiểm tra: người hỗ trợ pháp lý cập nhật địa chỉ của tư vấn viên đã duyệt còn thiếu thẻ, qua FR-IV-11.
- Testcase bị ảnh hưởng: `TC-THN-025` — chỉ ý này chờ.

**Điểm SRS chưa nói**

1. Ràng buộc thẻ nay nêu ở FR-IV-01 và FR-IV-04:
   - "| E10 | `loai_tvv = 'TVV'` mà thiếu số thẻ hoặc tệp thẻ hành nghề … | ERR-TVV-10 | …"
   - "**Given** CB NV mở hồ sơ tư vấn viên đã duyệt còn thiếu số thẻ **When** sửa bất kỳ nội dung nào và lưu **Then** hệ thống yêu cầu bổ sung số thẻ — quy tắc chặn nhẹ, **không hồi tố** …"
   - "Ràng buộc chỉ chặn **tại thời điểm lưu** của FR-IV-04 …"; "Hồ sơ không ai mở ra sửa thì không bị đụng tới."

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:211`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:218`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:418`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:419`

2. FR-IV-11 cũng lưu bản ghi TU_VAN_VIEN, nhưng đầu vào chỉ có bốn trường — địa chỉ, số điện thoại, email, lĩnh vực — không có ô thẻ; bảy bước xử lý (kiểm quyền, kiểm trạng thái vô hiệu hóa, kiểm định dạng, kiểm email trùng, cập nhật, cập nhật lĩnh vực, ghi nhật ký) không bước nào kiểm thẻ.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:861`–`:864`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:870`–`:876`

**Câu hỏi cần BA xác nhận**

Lần lưu FR-IV-11 trên tư vấn viên còn thiếu thẻ có bị chặn không?

1. **Hướng 1 — không chặn:** FR-IV-11 chỉ đổi thông tin liên hệ, lĩnh vực và không có ô thẻ; ghi rõ ngoại lệ này cạnh quy tắc chặn nhẹ (`fr-04:418`).
2. **Hướng 2 — chặn:** thêm bước kiểm thẻ và mã lỗi vào FR-IV-11 (dùng `ERR-TVV-10` hay `ERR-NL-06`); người hỗ trợ bổ sung thẻ qua FR-IV-04 trước rồi mới cập nhật liên hệ.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — FR-IV-11 không có ô thẻ; chặn thì một lần sửa số điện thoại cũng không lưu được cho tới khi có người mở FR-IV-04.
- `TC-THN-025` chấm theo SRS hiện hành (lưu được, có nhật ký); ý "có bị chặn không" gắn `chờ BA – Q07 (hỏi thêm)`.

---

## CR-GY-Q09 — Loại lý do từ chối lưu ở đâu, ai dùng

**Bối cảnh testcase**

- Nhóm thay đổi T2 — FR-V.I-06, trường mới `loai_ly_do_tu_choi` (Ngoài phạm vi hỗ trợ / Thiếu thành phần hồ sơ / Lý do khác).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ kết luận Không đạt; sau đó đọc lại vụ việc và xem thống kê theo loại lý do.
- Testcase bị ảnh hưởng: ý đọc lại loại lý do và kết quả từng hạng mục của `TC-KT-003`, `TC-KT-004`, `TC-KT-005`, `TC-KT-012`, `TC-KT-014`, `TC-KT-018`, `TC-KT-019`, `TC-VVCL-012` (kết quả chính chấm ngay).

**Điểm mâu thuẫn trong SRS v3.5**

1. SRS đưa trường này vào với mục đích **thống kê**, hệ thống tự xác định giá trị, và bản `aaee63b` còn thêm quy tắc cho số liệu gom theo lý do từ chối:
   - Hạng mục 1 đặt trước "để tách bạch lý do từ chối 'ngoài phạm vi hỗ trợ' với lý do 'thiếu tài liệu' khi thống kê".
   - Thứ tự ưu tiên: hạng mục 1 không đạt → `NGOAI_PHAM_VI`; hạng mục 1 đạt nhưng có hạng mục 2–7 không đạt → `THIEU_TAI_LIEU`; cả bảy đạt mà kết luận Không đạt → `KHAC`.
   - "Hồ sơ kiểm tra theo danh mục trước đây (lưu ít hơn 7 hạng mục) không có giá trị cho trường này; mọi chiều gom số liệu theo lý do từ chối xếp nhóm "Không xác định", KHÔNG suy đoán ngược".
   - Thông báo từ chối cho doanh nghiệp nêu đúng loại lý do.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:527`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:542`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:570`–`:572`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:575`

2. Nhưng **không bảng thuộc tính nào có cột này**, và không báo cáo / chỉ số nào đọc nó:
   - Bảng VU_VIEC (tệp nền và tệp nhóm) không có `loai_ly_do_tu_choi`, cũng không có cột lưu kết quả checklist (`checklist` dạng JSON ở đầu vào).
   - Tệp Báo cáo không có báo cáo nào gom theo loại lý do từ chối — nhóm "Không xác định" ở điểm 1 không có chỗ áp. Bản phản hồi phiếu Dev (bảng "Sửa gì trong SRS", dòng 4) ghi sẽ thêm "Báo cáo lý do từ chối: nhóm "Không xác định"" vào `srs-fr-11-bao-cao.md`, nhưng SRS `aaee63b` không có thay đổi đó.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1585`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2151`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:524`

**Câu hỏi cần BA xác nhận**

Loại lý do từ chối (và kết quả 7 hạng mục) có phải lưu lại để tra cứu / thống kê không?

1. **Hướng 1 — lưu:** bổ sung cột `loai_ly_do_tu_choi` (và nơi lưu kết quả checklist) vào VU_VIEC hoặc bảng kết quả kiểm tra; nói rõ báo cáo nào gom theo loại lý do — nhóm "Không xác định" của `fr-05:527` nằm ở báo cáo đó.
2. **Hướng 2 — không lưu:** loại lý do chỉ dùng tức thời để soạn thông báo cho doanh nghiệp. Khi đó bỏ câu "khi thống kê" ở `fr-05:542` và câu về nhóm "Không xác định" ở `fr-05:527`.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — mục đích ghi trong SRS là thống kê, và `aaee63b` còn đặt quy tắc gom số liệu; không lưu thì cả hai không đạt được.
- Kết quả chính (trạng thái `TU_CHOI`, loại lý do nêu trong thông báo) chấm ngay. Ý đọc lại loại lý do ghi `chờ BA – Q09`.
- Nếu Hướng 1: thêm kiểm đọc lại vụ việc thấy đúng loại lý do và kiểm báo cáo gom theo loại lý do (kể cả nhóm "Không xác định"). Nếu Hướng 2: chỉ kiểm nội dung thông báo.

---

## CR-GY-Q10 — Chuyển sang vụ việc do đơn vị khác thụ lý: được chọn đơn vị nào

**Bối cảnh testcase**

- Nhóm thay đổi T1 — FR-II-11 cho Cán bộ Nghiệp vụ **chọn lại đơn vị thụ lý** trước khi chuyển.
- Phần quyền đọc hai bên khi khác đơn vị đã chốt trong SRS `aaee63b` (mỗi bên chỉ thấy thông tin về thao tác chuyển; Cán bộ Trung ương, QTHT mở được cả hai hồ sơ) — không hỏi lại. Còn một điểm.
- Testcase bị ảnh hưởng: không TC nào treo. `TC-CL-005` chọn Sở Tư pháp cùng cấp địa phương — nằm trong tập được chọn ở mọi hướng dưới đây.

**Điểm SRS chưa nói**

1. Trường đơn vị thụ lý chỉ ghi "chọn lại được", không nêu tập đơn vị:
   - "| 4 | don_vi_id | identifier | Y | FK → DON_VI. **Chép nguyên đơn vị của hồ sơ hỏi đáp gốc**; CB NV chọn lại được trước khi xác nhận |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:956`

2. Chức năng có sẵn cho chọn lại đơn vị thì ghi rõ tập — FR-II-01 bước 5a: "CB được phép chọn lại trên dropdown (toàn bộ DON_VI TW+BN+ĐP)". Phần quyền đọc sau khi chuyển đã chốt, không phụ thuộc tập đơn vị.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:140`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1014`–`:1022`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1340`–`:1342`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1376`

**Câu hỏi cần BA xác nhận**

CB NV được chọn đơn vị thụ lý trong tập nào?

1. **Hướng 1 — toàn bộ đơn vị** (Trung ương, Bộ ngành, Địa phương), như FR-II-01 bước 5a.
2. **Hướng 2 — giới hạn:** chỉ đơn vị cùng cấp, hoặc cùng cấp và cấp trên — nêu rõ tập, và mã lỗi khi gửi đơn vị ngoài tập.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — khớp tiền lệ FR-II-01 bước 5a; SRS đã chấp nhận hệ quả đơn vị nguồn không tra được tiến độ sau khi chuyển (`fr-02:1020`).
- Không TC nào treo. BA chốt Hướng 2 thì QA thêm TC chọn đơn vị ngoài tập.

---

## CR-GY-Q11 — Vụ việc cầu nối kế thừa kênh `DVC`: có đồng bộ LGSP không

**Bối cảnh testcase**

- Nhóm thay đổi T1 — quy đổi kênh: hồ sơ hỏi đáp kênh `DVC` → vụ việc **giữ nguyên** `DVC`.
- Nội dung kiểm tra: vụ việc cầu nối kênh DVC được tiếp nhận, rồi bị từ chối.
- Testcase bị ảnh hưởng: `TC-VVCL-016`, `TC-HQHD-017`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Nhóm Vụ việc **nhận biết hồ sơ DVC theo kênh** và đồng bộ trạng thái về Hệ thống TTHC Bộ Tư pháp qua LGSP:
   - Tiếp nhận: "gửi TB DN (nếu DVC)".
   - Từ chối (FR-V.I-12): "Nếu HS qua DVC: gửi trạng thái về LGSP".
   - Việc đồng bộ dùng mã hồ sơ DVC `ma_ho_so_dvc`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2435`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:999`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1007`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1611`

2. Nhưng vụ việc cầu nối **không có mã hồ sơ DVC nào** để đồng bộ:
   - Kênh DVC được giữ nguyên khi chuyển.
   - Các bước của FR-II-11 không chép mã hồ sơ DVC; bảng HOI_DAP không có cột `ma_ho_so_dvc`.
   - BR-FLOW-11 (g) nói nhận biết hồ sơ chuyển luồng theo liên kết truy nguồn, không theo kênh — nhưng logic LGSP vẫn theo kênh.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:982`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:994`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1546`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5732`

**Câu hỏi cần BA xác nhận**

Vụ việc cầu nối mang kênh DVC có đồng bộ trạng thái về LGSP không?

1. **Hướng 1 — không đồng bộ:** điều kiện đồng bộ LGSP đổi thành "kênh DVC **và** có `ma_ho_so_dvc`" (hoặc "không có `hoi_dap_goc_id`"). Doanh nghiệp chỉ nhận thông báo trong hệ thống + email.
2. **Hướng 2 — có đồng bộ:** FR-II-11 phải chép mã hồ sơ DVC từ hồ sơ hỏi đáp sang vụ việc; khi đó HOI_DAP cần có cột lưu mã này.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1: hồ sơ hỏi đáp chưa từng là thủ tục DVC có mã, nên không có gì để đồng bộ.
- Testcase liên quan gắn `chờ BA – Q11`. Kênh `DVC` giữ nguyên trên vụ việc (bước quy đổi) viết ngay.

---

## CR-GY-Q12 — KPI-S-03: quy ước chung của thẻ KPI; tập "vụ việc đóng trong kỳ"

**Bối cảnh testcase**

- Nhóm thay đổi T5 — chỉ số mới Thời gian xử lý toàn trình, đặt cạnh KPI-S-02 trên Dashboard.
- Nội dung kiểm tra: tính giá trị thẻ cho một kỳ có / không có vụ việc đóng; vụ việc hoàn thành rồi được đánh giá; vụ việc bị từ chối.
- Testcase bị ảnh hưởng: `TC-KPI3-004`, `TC-KPI3-006`, `TC-KPI3-008` (cả TC chờ, ý a); `TC-KPI3-007` (cả TC chờ, ý b); `TC-HQBC-015` (một ý, ý b). `TC-KPI3-013` (vụ việc từ chối) chấm ngay — liên quan ý c.

**Điểm mâu thuẫn trong SRS v3.5**

1. KPI-S-02 (thẻ đứng cạnh) theo đủ quy ước chung:
   - Khai "Template: TPL-DASH-KPI"; nằm trong danh sách "KPI phát sinh trong kỳ" của bước lọc.
   - Làm tròn 1 chữ số thập phân; tập rỗng → giá trị trống, hiển thị "—".
   - Tập vụ việc: trạng thái "Hoàn thành" có ngày hoàn thành trong kỳ.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:607`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:615`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:626`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:194`

2. Nhưng KPI-S-03 **không khai template**, không có trong danh sách KPI phát sinh trong kỳ, không nói làm tròn, không nói kỳ rỗng, không nói xu hướng so kỳ trước. Còn tập "vụ việc đóng trong kỳ":
   - KPI-S-03: "Lấy tập vụ việc đóng trong kỳ"; "Lấy trung bình trên tập vụ việc trong kỳ".
   - BA đã trả lời giả định G2 ở file trước: KPI-S-03 dùng đúng tập của KPI-S-02. Câu này chưa vào SRS.
   - Tập của KPI-S-02 chỉ ghi trạng thái "Hoàn thành", trong khi FR-I-04 coi "đã hoàn thành" gồm **`HOAN_THANH` và `DA_DANH_GIA`**. Vụ việc sau khi được đánh giá chuyển `DA_DANH_GIA` — nếu chỉ lấy `HOAN_THANH` thì vụ việc đã đánh giá rơi khỏi cả hai thẻ. Bước 4 TPL-REPORT-FULL và BR-RPT-01 cũng không nêu `DA_DANH_GIA`, nên các báo cáo vụ việc vướng cùng chỗ.
   - "Đóng" có gồm vụ việc `TU_CHOI` không cũng chưa nói. Nếu gồm, vụ việc từ chối không có `ngay_hoan_thanh`, mà mốc kết thúc của KPI-S-03 là ngày hoàn thành.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:655`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:658`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:321`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:649`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:82`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5834`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2181`

**Câu hỏi cần BA xác nhận**

(a) KPI-S-03 có theo TPL-DASH-KPI và cùng quy ước với KPI-S-02 không (lọc Năm/Tháng/đơn vị, KPI phát sinh trong kỳ, xu hướng so kỳ trước, làm tròn 1 chữ số, kỳ rỗng → "—")?

1. **Hướng 1 — có:** ghi "Template: TPL-DASH-KPI", thêm KPI-S-03 vào danh sách KPI phát sinh trong kỳ (`fr-01:194`), ghi làm tròn và kỳ rỗng như KPI-S-02.
2. **Hướng 2 — không:** nêu quy ước riêng.

(b) Vụ việc đã được đánh giá (`DA_DANH_GIA`) có thuộc tập "vụ việc đóng trong kỳ" của KPI-S-02, KPI-S-03 không?

1. **Hướng 1 — có**, như FR-I-04: tập gồm `HOAN_THANH` và `DA_DANH_GIA`, ngày hoàn thành trong kỳ. Sửa chữ ở KPI-S-02, ghi tập vào `fr-01:655`, và nói rõ các báo cáo vụ việc (FR-IX-02, FR-IX-13) có tính `DA_DANH_GIA` không.
2. **Hướng 2 — không**, chỉ `HOAN_THANH`: vụ việc rời khỏi hai thẻ khi doanh nghiệp đánh giá — ghi rõ ở KPI-S-02 và KPI-S-03.

(c) "Vụ việc đóng" của KPI-S-03 có gồm `TU_CHOI` không? Nếu có, mốc kết thúc lấy trường nào?

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 cho (a) và (b) — với Hướng 2 của (b), vụ việc biến khỏi hai thẻ ngay khi doanh nghiệp đánh giá. Với (c), testcase chấm theo chữ hiện hành: vụ việc từ chối không có mốc kết thúc nên không vào chỉ số.
- Ba tiêu chí chấp nhận có sẵn của KPI-S-03 (mốc bắt đầu, không dự phần tỷ lệ tuân thủ) viết ngay. `TC-KPI3-007` gắn `chờ BA – Q12(b)`; `TC-KPI3-013` chấm số không đổi khi có vụ việc từ chối; `TC-HQBC-015` chấm KPI-04, phần KPI-S-02 và báo cáo ghi lại.

---

## CR-GY-Q13 — Mức cảnh báo thời hạn của hồ sơ đã chuyển (`DA_CHUYEN_LUONG`)

**Bối cảnh testcase**

- Nhóm thay đổi T1 — hồ sơ hỏi đáp đã chuyển đóng ở trạng thái riêng.
- Nội dung kiểm tra: hồ sơ đã chuyển quá thời hạn cũ — hệ thống có tiếp tục nâng mức cảnh báo và gửi thông báo không; tra cứu "câu hỏi đã xử lý" có ra hồ sơ này không.
- Testcase bị ảnh hưởng: `TC-HQHD-007`, `TC-HQHD-008` (cả TC chờ); `TC-CL-011`, `TC-CL-036` (một ý).

**Điểm mâu thuẫn trong SRS v3.5**

1. SRS coi hồ sơ đã chuyển là **đã đóng**:
   - "Hồ sơ chuyển sang chỉ đọc, không sửa, không soạn phản hồi, không chuyển tiếp lần nữa"; BR-FLOW-11 (d) "đóng hồ sơ nguồn".
   - Mức cảnh báo thời hạn "chỉ tính khi hồ sơ đã có thời hạn xử lý và **chưa kết thúc**; ngoài khoảng đó để trống". Xóa mức khi hồ sơ đã kết thúc không gửi thông báo.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1826`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5732`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1553`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5770`

2. Nhưng SRS **không liệt kê** trạng thái nào là "kết thúc" của hỏi đáp, và các tập trạng thái cố định có sẵn không có `DA_CHUYEN_LUONG`:
   - Tìm kiếm câu hỏi đã xử lý (FR-II-10): lọc cứng `HOAN_THANH`, `HUY`.
   - Tìm kiếm hỏi đáp đã tiếp nhận (FR-II-05): lọc cứng `TIEP_NHAN`, `DANG_XU_LY`.
   - Tác vụ tự động tính mức cảnh báo thời hạn chỉ quét hồ sơ `TIEP_NHAN`, `DANG_XU_LY`.
   - Hệ quả: theo văn bản hiện hành, tác vụ không quét hồ sơ đã chuyển, nên mức cảnh báo **đứng yên ở giá trị lúc chuyển**: không lên Quá hạn, không gửi thông báo, nhưng cũng không để trống như điểm 1 đòi khi hồ sơ đã kết thúc.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:887`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:489`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1245`

3. Bản `aaee63b` thêm lối **Hoàn tác** `DA_CHUYEN_LUONG → TIEP_NHAN` khi vụ việc đích bị xóa lúc còn Chờ tiếp nhận: khôi phục `deadline` và `muc_do_canh_bao` từ hai trường ảnh chụp, "KHÔNG tính lại từ đầu". Như vậy `DA_CHUYEN_LUONG` không còn là trạng thái cuối tuyệt đối, và SRS vẫn không nói hai trường `deadline`, `muc_do_canh_bao` của hồ sơ **trong khoảng** nằm ở `DA_CHUYEN_LUONG` được xóa, đứng yên hay chạy tiếp. Nếu đứng yên thì bước khôi phục là thừa.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:997`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1044`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1778`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1819`

**Câu hỏi cần BA xác nhận**

Trong thời gian hồ sơ ở `DA_CHUYEN_LUONG`, mức cảnh báo thời hạn xử lý thế nào; hồ sơ có vào tập tra cứu "câu hỏi đã xử lý" không?

1. **Hướng 1 — coi như đã kết thúc về thời hạn:** khi chuyển, xóa mức cảnh báo (không gửi thông báo, như BR-SLA-03), bộ đếm thời hạn dừng; nếu hoàn tác, khôi phục từ ảnh chụp như `fr-02:1044`. FR-II-10 thêm `DA_CHUYEN_LUONG` vào tập tra cứu.
2. **Hướng 2 — không phải trạng thái kết thúc:** nói rõ mức cảnh báo giữ nguyên giá trị lúc chuyển (tác vụ không quét, như văn bản hiện hành), hay tác vụ quét thêm `DA_CHUYEN_LUONG` để mức lên tiếp — khi đó ai nhận thông báo. FR-II-10 giữ bộ lọc hiện tại.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — khớp "đóng hồ sơ nguồn" của BR-FLOW-11 (d), và lối Hoàn tác khôi phục từ ảnh chụp chỉ có nghĩa khi hai trường gốc không còn giữ giá trị lúc chuyển.
- Testcase liên quan gắn `chờ BA – Q13`. Phần "tab / bộ lọc trạng thái trên màn danh sách" là giao diện, để lại tới khi có UI.

---

## CR-GY-Q14 — Báo cáo hỏi đáp FR-IX-01: trạng thái nào vào nhóm nào

**Bối cảnh testcase**

- Nhóm thay đổi T1 + T4 — FR-IX-01 thêm nhóm thứ ba "đã chuyển sang Vụ việc" và đổi mẫu số tỷ lệ trả lời.
- Nội dung kiểm tra: dựng một kỳ có hồ sơ ở nhiều trạng thái, đối chiếu tổng, ba nhóm và tỷ lệ.
- Testcase bị ảnh hưởng: `TC-BC01-003`, `TC-BC01-004` (cả TC chờ); `TC-BC01-001`, `TC-BC01-002` (một phần); `TC-BC01-017` (một ý). Số đã trả lời / chờ trả lời của `TC-BC01-006`, `-007`, `-009`, `-012`, `-013`, `-015`, `-018`, `-019`, `-021`, `-022`, `-023` tính theo bảng đề xuất dưới đây — BA chốt khác thì tính lại.

**Điểm mâu thuẫn trong SRS v3.5**

1. FR-IX-01 kế thừa TPL-REPORT-FULL, mà bước 4 của template chỉ lấy **bản ghi đã duyệt**, đồng thời đòi tập giá trị ô lọc trạng thái phủ đúng tập trạng thái thống kê để tổng các nhóm bằng tổng chung:
   - "CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán)."

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:145`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:82`

2. Nhưng FR-IX-01 đếm cả hồ sơ **chưa duyệt** (chờ trả lời, đã chuyển), và **không có bảng** trạng thái → nhóm. Hỏi đáp có 10 trạng thái; ô lọc chỉ có 3 giá trị:
   - Ô lọc: `DA_TRA_LOI / CHO_TRA_LOI / DA_CHUYEN_LUONG` — trong đó `DA_TRA_LOI` còn trùng tên một trạng thái thật của hỏi đáp.
   - Trạng thái hỏi đáp: `MOI`, `TIEP_NHAN`, `DANG_XU_LY`, `DA_TRA_LOI`, `CHO_PHE_DUYET`, `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH`, `HUY`, `DA_CHUYEN_LUONG`.
   - Không nói `HUY` và `MOI` có vào `tong_hoi_dap` không. Nếu `HUY` vào tổng mà không thuộc nhóm nào thì tổng ba nhóm ≠ tổng, trái bước 4 của template; mẫu số mới `tong_hoi_dap − da_chuyen_luong` cũng đổi theo.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:152`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:157`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:198`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1544`

**Câu hỏi cần BA xác nhận**

Đề nghị BA chốt bảng trạng thái → nhóm cho FR-IX-01. QA đề xuất bản dưới để BA sửa trực tiếp:

| Trạng thái hỏi đáp | Nhóm đề xuất | Vào `tong_hoi_dap`? |
|---|---|---|
| `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH` | đã trả lời | có |
| `MOI`, `TIEP_NHAN`, `DANG_XU_LY`, `DA_TRA_LOI`, `CHO_PHE_DUYET` | chờ trả lời | có |
| `DA_CHUYEN_LUONG` | đã chuyển sang Vụ việc | có (BR-RPT-02 b) |
| `HUY` | — | **cần BA chốt** |

Kèm theo: FR-IX-01 là **ngoại lệ** của bước 4 TPL-REPORT-FULL (đếm cả hồ sơ chưa duyệt) — đề nghị ghi tường minh ngoại lệ đó.

**Đề xuất QA tạm thời**

- Phần đã chốt viết ngay: hồ sơ `DA_CHUYEN_LUONG` vào tổng, nằm ở nhóm thứ ba, không vào đã trả lời, bị loại khỏi mẫu số (BR-RPT-02 a–d).
- Con số cụ thể của hai nhóm đã trả lời / chờ trả lời gắn `chờ BA – Q14`. Dữ liệu thử tạm chỉ dùng `HOAN_THANH` (đã trả lời) và `DANG_XU_LY` (chờ trả lời) — hai trạng thái ít khả năng bị xếp khác.

---

## CR-GY-Q15 — KPI-S-03: vụ việc tiếp nhận trực tiếp lấy mốc ngày tạo hay ngày tiếp nhận

**Bối cảnh testcase**

- Nhóm thay đổi T5 — chỉ số Thời gian xử lý toàn trình, phần vụ việc **không** qua cầu nối.
- Nội dung kiểm tra: dựng kỳ có vụ việc trực tiếp tạo trước ngày tiếp nhận vài ngày (VV-K2 tạo 07/09, tiếp nhận 09/09), đối chiếu số trên thẻ với số tính tay.
- Testcase bị ảnh hưởng: `TC-KPI3-002` (P0, cả TC chờ); `TC-KPI3-004`, `TC-KPI3-007` (thêm Q15 vào nhãn Q12 sẵn có); `TC-KPI3-005`, `TC-KPI3-010` ghi hai giá trị, chấm theo hướng BA chốt.

**Điểm mâu thuẫn trong SRS v3.5**

1. Mô tả, bảng mốc, quy tắc tính và tiêu chí chấp nhận của KPI-S-03 đều lấy **ngày tạo bản ghi vụ việc** làm mốc cho vụ việc tiếp nhận trực tiếp:
   - "Đo thời gian doanh nghiệp thực tế phải chờ — tính từ **ngày yêu cầu vào hệ thống**…"
   - "| Vụ việc tiếp nhận trực tiếp | Ngày tạo bản ghi vụ việc |"
   - "…nếu có `hoi_dap_goc_id` → mốc bắt đầu = ngày tạo bản ghi hỏi đáp gốc; ngược lại = ngày tạo bản ghi vụ việc"
   - "**Given** vụ việc tiếp nhận trực tiếp **When** tính chỉ số **Then** mốc bắt đầu là ngày tạo bản ghi vụ việc"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:634`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:645`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:656`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:668`

2. Ghi chú ngay dưới quy tắc tính lại nói với hồ sơ không qua chuyển luồng chỉ số này **bằng đúng thời gian xử lý thường** — mà thời gian xử lý thường (KPI-S-02) tính từ **ngày tiếp nhận**:
   - "Với hồ sơ **không** qua chuyển luồng, chỉ số này bằng đúng thời gian xử lý thường — vẫn có nghĩa, không phải trường hợp ngoại lệ."
   - KPI-S-02: "Trung bình số ngày làm việc giữa ngày tiếp nhận và ngày hoàn thành (cho vụ hoàn thành trong kỳ)"
   - Hai câu chỉ cho cùng một số khi vụ việc được tiếp nhận đúng ngày tạo. Vụ việc cán bộ nhập tay nằm ở `CHO_TIEP_NHAN` vài ngày rồi mới tiếp nhận là chuyện thường. Dữ liệu `TC-KPI3-002`: hai vụ đóng trong kỳ cho **18** ngày theo ngày tạo, **17** theo ngày tiếp nhận.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:664`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:678`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:602`

**Câu hỏi cần BA xác nhận**

Vụ việc tiếp nhận trực tiếp: mốc bắt đầu của KPI-S-03 là ngày nào?

1. **Hướng 1 — ngày tạo bản ghi vụ việc** (theo mô tả, bảng mốc, quy tắc tính, tiêu chí chấp nhận): sửa ghi chú thành "bằng thời gian xử lý thường **cộng** thời gian chờ tiếp nhận", hoặc bỏ câu đó.
2. **Hướng 2 — ngày tiếp nhận** (theo ghi chú): sửa bốn chỗ ở điểm 1; khi đó với vụ trực tiếp KPI-S-03 trùng KPI-S-02, hai thẻ chỉ khác nhau ở vụ cầu nối.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — mục đích ghi ở mô tả là "thời gian doanh nghiệp thực tế phải chờ", và bốn chỗ nhất quán với nhau; ghi chú là câu giải thích viết thiếu.
- `TC-KPI3-002` gắn `chờ BA – Q15`, hai hướng ghi sẵn hai số. Các TC khác của file 09 ghi cả hai giá trị, chấm sau khi BA chốt. Q15 độc lập với Q12 (làm tròn, tập vụ việc) — BA có thể trả lời riêng.

---

## CR-GY-Q16 — FR-IX-02 và FR-IX-13 kế thừa TPL-REPORT-FULL: đếm mọi vụ việc đã tiếp nhận hay chỉ bản ghi đã duyệt

**Bối cảnh testcase**

- Nhóm thay đổi T4 — FR-IX-13 đổi chiều thống kê sang quy mô DN; FR-IX-02 là báo cáo cũ dùng chung mẫu, vướng cùng một chỗ.
- Nội dung kiểm tra: dựng kỳ có vụ việc hoàn thành và vụ việc mới tiếp nhận, chưa xử lý xong; chạy báo cáo trước và sau khi tiếp nhận thêm một vụ, so số đếm.
- Testcase bị ảnh hưởng: `TC-HQBC-005` (lần chạy 3), `TC-HQBC-006` (số của dòng quy mô Nhỏ).

**Điểm mâu thuẫn trong SRS v3.5**

1. Bước 4 của TPL-REPORT-FULL chỉ lấy bản ghi đã duyệt, và cả hai báo cáo đều ghi kế thừa mẫu này:
   - "| 4 | Truy vấn dữ liệu: CHỈ bản ghi đã duyệt (trạng thái đã duyệt / hoàn thành / đã thanh toán). …"
   - FR-IX-02, FR-IX-13: "**Template:** Kế thừa TPL-REPORT-FULL"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:82`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:232`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:683`

2. Công thức riêng của FR-IX-02 lại đếm **mọi vụ việc đã tiếp nhận** (trừ từ chối) — gồm vụ đang xử lý, chưa thuộc "đã duyệt / hoàn thành"; FR-IX-13 chỉ ghi "trong kỳ", không nói tập trạng thái, cũng không nói "trong kỳ" tính theo ngày tạo, ngày tiếp nhận hay ngày hoàn thành:
   - FR-IX-02: "**Công thức:** Đếm số vụ việc đã tiếp nhận (trừ từ chối) trong kỳ, theo phạm vi đơn vị"
   - FR-IX-13: "**Công thức:** Đếm vụ việc **theo quy mô DN** (siêu nhỏ / nhỏ / vừa) `[CR-GY-2026-09-13]`, trong kỳ, theo phạm vi"
   - Không nơi nào ghi hai báo cáo này là ngoại lệ của bước 4 (FR-IX-01 vướng cùng chỗ — đã hỏi ở Q14). Một vụ việc vừa tiếp nhận được đếm theo công thức FR-IX-02 nhưng bị loại theo mẫu.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:241`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:691`

**Câu hỏi cần BA xác nhận**

Với FR-IX-02 và FR-IX-13, vụ việc đã tiếp nhận nhưng chưa hoàn thành có được đếm không?

1. **Hướng 1 — có** (theo công thức FR-IX-02): ghi rõ hai báo cáo là ngoại lệ của bước 4 mẫu; FR-IX-13 dùng cùng tập với FR-IX-02, mốc "trong kỳ" = ngày tiếp nhận.
2. **Hướng 2 — không** (theo mẫu): sửa công thức FR-IX-02 thành "đếm vụ việc hoàn thành trong kỳ"; FR-IX-13 ghi tập trạng thái và mốc ngày.

Dù chọn hướng nào, đề nghị ghi cho FR-IX-13 mốc ngày của "trong kỳ" (ngày tạo / ngày tiếp nhận / ngày hoàn thành).

**Đề xuất QA tạm thời**

- `TC-HQBC-005` lần chạy 3 gắn `chờ BA – Q16`: Hướng 1 → `tong_vu_viec` = 4 (thêm vụ vừa tiếp nhận, kênh DVC); Hướng 2 → vẫn 3. Hai lần chạy đầu chỉ có vụ hoàn thành nên chấm ngay.
- `TC-HQBC-006` dòng Nhỏ gắn `chờ BA – Q16`: cặp số (lần 1, lần 3) cho biết cách hệ thống dùng — (2, 2) chỉ đếm vụ hoàn thành; (2, 3) đếm theo ngày tiếp nhận; (3, 3) đếm theo ngày tạo. Cặp khác → không đạt ở mọi hướng.

---

## CR-GY-Q17 — Thẩm định hồ sơ TVV: nhóm Pháp lý Không đạt thì chỉ chặn "Đạt" hay ép cả kết luận thành "Không đạt"

**Bối cảnh testcase**

- Nhóm thay đổi T6 — hồi quy thẩm định FR-IV-06 sau khi nhóm Pháp lý thêm ô đối chiếu số thẻ và bản chụp thẻ hành nghề.
- Nội dung kiểm tra: hồ sơ tư vấn viên thiếu thẻ, cán bộ chấm nhóm Pháp lý = Không đạt rồi chọn kết luận "Yêu cầu bổ sung" kèm lý do.
- Testcase bị ảnh hưởng: `TC-HQBC-012` (bộ b).

**Điểm mâu thuẫn trong SRS v3.5**

1. Phần xử lý của FR-IV-06 chỉ có **một** ràng buộc — không được kết luận Đạt khi nhóm Pháp lý chưa đạt; "Yêu cầu bổ sung" là kết luận hợp lệ, có bước xử lý và thông báo riêng:
   - "| 3 | Kiểm tra: DAT chỉ khi nhóm Pháp lý = Đạt |"
   - "| 5 | Nếu YEU_CAU_BO_SUNG: chuyển trạng thái, gửi thông báo kèm lý do cho **TVV/CG (chủ hồ sơ) qua email đã khai** VÀ **Người hỗ trợ đã nộp hồ sơ (thông báo trong phần mềm + email)** …"
   - `ERR-TD-02`: "Không thể kết luận ĐẠT khi nhóm Pháp lý chưa đạt"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:551`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:553`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:577`

2. Màn hình SCR-IV-03 ghi hai quy tắc khác nhau ở hai dòng — dòng 14 ép toàn bộ kết luận, dòng 18 chỉ chặn "Đạt" (khớp phần xử lý):
   - Dòng 14: "Kết luận: "Đạt" / "Không đạt" — nếu "Không đạt" thì toàn bộ kết luận = "Không đạt""
   - Dòng 18: ""Đạt" / "Không đạt" / "Yêu cầu bổ sung". Quy tắc: "Đạt" chỉ chọn được khi Nhóm 1 = Đạt"
   - Theo dòng 14, hồ sơ thiếu thẻ hành nghề (nhóm Pháp lý Không đạt) không bao giờ được "Yêu cầu bổ sung" — trong khi thiếu giấy tờ là đúng tình huống của trạng thái này.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1625`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1629`

**Câu hỏi cần BA xác nhận**

Nhóm Pháp lý = Không đạt, cán bộ chọn "Yêu cầu bổ sung" — hệ thống nhận hay chặn?

1. **Hướng 1 — nhận** (theo phần xử lý và dòng 18): hồ sơ sang `YEU_CAU_BO_SUNG`, gửi thông báo theo bước 5; sửa dòng 14 thành "không được kết luận Đạt".
2. **Hướng 2 — chặn** (theo dòng 14): chỉ còn "Không đạt"; bổ sung quy tắc và mã lỗi vào phần xử lý, ghi rõ "Yêu cầu bổ sung" không chọn được khi Nhóm 1 = Không đạt.

**Đề xuất QA tạm thời**

- QA nghiêng về Hướng 1 — phần xử lý và dòng 18 nhất quán với nhau, dòng 14 là câu viết quá tay.
- `TC-HQBC-012` bộ (b) gắn `chờ BA – Q17`: Hướng 1 → hồ sơ `YEU_CAU_BO_SUNG`, người hỗ trợ và chủ hồ sơ nhận thông báo kèm lý do; Hướng 2 → bị từ chối hoặc ra `TU_CHOI`, ghi lại. Bộ (a) (chọn Đạt → `ERR-TD-02`) và bộ (c) chấm ngay.

---

## CR-GY-Q18 — FR-IX-18 Báo cáo chi phí theo quy mô DN: ba cột tiền tính thế nào

**Bối cảnh testcase**

- Nhóm thay đổi T4 — FR-IX-18 đổi chiều sang "theo quy mô DN".
- Nội dung kiểm tra: dựng ba hồ sơ chi trả đã thanh toán (hai DN quy mô Nhỏ, một DN Vừa) trong một kỳ, đối chiếu từng cột của dòng báo cáo với số tính tay.
- Testcase bị ảnh hưởng: `TC-HQBC-008` (ba cột tiền).

**Điểm mâu thuẫn trong SRS v3.5**

1. Công thức và cột `tong_chi_phi` chỉ ghi "Tổng chi phí" — không nói cộng cột nào của hồ sơ chi trả (phí tư vấn `phi_tu_van`, số được duyệt `so_tien_duoc_duyet` hay số thực trả `so_tien_thuc_tra`), và "+ mức hỗ trợ" trong công thức nghĩa là cộng thêm hay chỉ hiển thị cạnh:
   - "**Công thức:** Tính tổng chi phí **theo quy mô DN** `[CR-GY-2026-09-13]` + mức hỗ trợ, so sánh với trần chi phí theo NĐ55/2019"
   - "| 5 | tong_chi_phi | money | Luôn | Tổng chi phí |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:873`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:885`

2. Trần chi phí ghi "theo NĐ55", trong khi quy tắc tính và cấu hình đang dùng theo NĐ18/2026, còn UBND tỉnh có thể đặt trần riêng — không rõ báo cáo lấy trần từ đâu:
   - "Báo cáo chi phí **theo quy mô DN** (siêu nhỏ/nhỏ/vừa) `[CR-GY-2026-09-13]`, kèm mức hỗ trợ và so sánh trần chi phí theo NĐ55."
   - "| 6 | tran_chi_phi | money | Luôn | Trần chi phí theo NĐ55 |"
   - BR-CALC-01: "**Mức hỗ trợ chi phí theo quy mô DN (NĐ18/2026):** DN siêu nhỏ = 100% (trần 3 triệu/năm), DN nhỏ = tối đa 30% (trần 5 triệu/năm), DN vừa = tối đa 10% (trần 10 triệu/năm) … Địa phương (UBND tỉnh) có thể quyết định mức phí trần riêng"
   - "Nếu NĐ18/2026 không ban hành hoặc ban hành với mức khác, hệ thống fallback về NĐ55/2019 … FR-VIII-12 seed data sẽ được điều chỉnh theo văn bản chính thức."
   - Seed FR-VIII-12: "**Seed Data (NĐ18/2026):** Siêu nhỏ: 100%, 3.000.000 VNĐ | Nhỏ: <=30%, 5.000.000 VNĐ | Vừa: <=10%, 10.000.000 VNĐ"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:861`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:886`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5740`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5742`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:605`

3. Trần là mức "/năm" của **một** doanh nghiệp, còn một dòng báo cáo gộp nhiều hồ sơ của nhiều DN — `tran_chi_phi` của dòng là trần một DN, trần × số DN, hay trần × số hồ sơ; `chenh_lech` ("Tổng CP - Trần") đổi theo:
   - "| 7 | chenh_lech | money | Luôn | Tổng CP - Trần |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:887`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5740`

**Câu hỏi cần BA xác nhận**

Đề nghị BA ghi công thức cho ba cột. QA đề xuất bản dưới để BA sửa trực tiếp:

| Cột | Đề xuất QA |
|---|---|
| `tong_chi_phi` | Tổng `so_tien_thuc_tra` của các hồ sơ đã thanh toán trong dòng (cùng cột FR-IX-15 đang dùng) |
| `tran_chi_phi` | Trần theo cấu hình FR-VIII-12 đang áp dụng (NĐ18/2026 hoặc trần địa phương) × số DN khác nhau trong dòng; sửa chữ "NĐ55" ở mô tả, công thức, cột 6 |
| `chenh_lech` | `tong_chi_phi` − `tran_chi_phi` |

**Đề xuất QA tạm thời**

- `TC-HQBC-008` chấm ngay `loai_dn`, `muc_ho_tro`, `so_ho_so` và quan hệ `chenh_lech` = `tong_chi_phi` − `tran_chi_phi` trong cùng dòng. Ba cột tiền gắn `chờ BA – Q18`: TC ghi sẵn số theo bốn cách (tiền hỗ trợ / phí tư vấn × trần một DN / trần cộng), chấm sau khi BA chốt; số không thuộc cách nào → không đạt.

---

## CR-GY-Q19 — Doanh nghiệp tự đăng ký (FR-VIII-22) và CB NV thêm DN (FR-V.III-NEW-03): có nhận trường Hình thức tổ chức không

**Bối cảnh testcase**

- Nhóm thay đổi T3 — FR-V.III-01 thêm trường 7a `hinh_thuc_to_chuc_id` (tùy chọn).
- Nội dung kiểm tra: đăng ký tài khoản doanh nghiệp gửi kèm hình thức tổ chức; CB NV thêm doanh nghiệp kèm hình thức.
- Testcase bị ảnh hưởng: `TC-HQBC-010` (bước 8). `TC-HTTC-013` kiểm qua FR-V.III-01 nên không phụ thuộc.
- Trước đây QA ghi điểm này ở mục Sửa tài liệu (D9) và viết testcase "đăng ký không khai hình thức vẫn thành công; gửi kèm thì ghi SRS Gap". Soát lại: bước 8 của `TC-HQBC-010` phải chọn một cách hiểu mới chấm được → chuyển thành câu hỏi.

**Điểm mâu thuẫn trong SRS v3.5**

1. FR-V.III-01 có trường 7a, tùy chọn:
   - "| 7a | hinh_thuc_to_chuc_id | identifier | N | FK → DANH_MUC … **Tùy chọn.** …"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:107`

2. Hai chức năng khác dẫn chiếu bảng FR-V.III-01, nhưng danh sách trường riêng của chúng không có 7a:
   - FR-VIII-22: "Form đăng ký full thông tin entity DOANH_NGHIEP (giống Inputs FR-V.III-01) + 3 trường tài khoản" — khối "| **Thông tin doanh nghiệp (giống Inputs FR-V.III-01)** |" liệt kê tới trường 24 `la_nu_lam_chu`, không có 7a.
   - FR-V.III-NEW-03: "**Inputs:** 18 trường DN như bảng FR-V.III-01 (mục 95–117) … 15 trường còn lại tùy chọn…" — không nhắc 7a.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1046`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1058`–`:1082`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:286`

**Câu hỏi cần BA xác nhận**

Hai form này có nhận `hinh_thuc_to_chuc_id` không?

1. **Hướng 1 — có:** "giống Inputs FR-V.III-01" hiểu là gồm cả 7a; bổ sung dòng 7a vào danh sách trường của FR-VIII-22 và câu Inputs của FR-V.III-NEW-03.
2. **Hướng 2 — không:** hai form giữ danh sách hiện có; ghi rõ giá trị gửi kèm bị bỏ qua hay bị từ chối (mã lỗi); hình thức tổ chức chỉ vào được qua sửa hồ sơ doanh nghiệp.

**Đề xuất QA tạm thời**

- `TC-HQBC-010` bước 8 gắn `chờ BA – Q19`: Hướng 1 → tạo được DN kèm `hinh_thuc_to_chuc_id`; Hướng 2 → bị từ chối hoặc tạo được mà bỏ hình thức, ghi lại. Các bước khác (đăng ký không khai hình thức, tài khoản `CHO_KICH_HOAT`, thư kích hoạt, nhật ký) chấm ngay.

---

## CR-GY-Q20 — Giới hạn tổng 50 MB khi đăng ký TVV: tính trên mọi tệp của một lần gửi hay trên từng ô

**Bối cảnh testcase**

- Nhóm thay đổi T6 — FR-IV-03 thêm tệp thẻ hành nghề và hai ô minh chứng (trường 21, 23), mỗi ô tối đa 10 tệp × 10 MB.
- Nội dung kiểm tra: một lần gửi có 6 tệp, tổng 54 MB, không tệp nào quá 10 MB, không ô nào quá 10 tệp (riêng ô 21 = 36 MB).
- Testcase bị ảnh hưởng: `TC-THN-008` (lần gửi 3).

**Điểm mâu thuẫn trong SRS v3.5**

1. Giới hạn tổng 50 MB có từ trước và gắn với **ô bằng cấp** ở FR-IV-01, FR-IV-04:
   - FR-IV-01: "| 20 | file_bang_cap | structured | Cond | Max 10MB/file, **tổng 50MB**, **max 10 files**, PDF only. …"
   - FR-IV-04: "PDF, max 10MB/file, tổng 50MB, max 10 files"; `ERR-NL-03` cùng câu "Tổng dung lượng file tối đa 50MB".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:158`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:403`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:455`

2. Ở FR-IV-03, ô bằng cấp (17) chỉ ghi 10 MB/tệp; hai ô minh chứng 21, 23 mỗi ô "tối đa 10 tệp" × 10 MB (tới 100 MB một ô); tệp thẻ 10 MB — còn dòng lỗi E5 không nói tổng của ô nào:
   - "| 17 | file_bang_cap | binary[] | Y | PDF, max 10MB/file"
   - Trường 21, 23: "PDF/DOC/DOCX, max 10MB/tệp, tối đa 10 tệp"
   - "| E5 | File vượt tổng 50MB | ERR-DK-05 | "Tổng dung lượng file tối đa 50MB""
   - Cộng mọi ô thì một ô minh chứng đầy đã vượt 50 MB — giới hạn "10 tệp × 10 MB" của ô 21, 23 không bao giờ đạt tới; tính riêng từng ô thì ô 21, 23 hợp lệ tới 100 MB mà không chạm E5.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:319`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:320`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:324`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:326`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:352`

**Câu hỏi cần BA xác nhận**

`ERR-DK-05` tính tổng 50 MB trên tập tệp nào?

1. **Hướng 1 — tổng mọi tệp của một lần gửi** (bằng cấp + thẻ + hai ô minh chứng) ≤ 50 MB: sửa giới hạn từng ô 21, 23 cho khớp (không thể tới 10 tệp × 10 MB).
2. **Hướng 2 — chỉ tính trên ô bằng cấp** (như FR-IV-01, FR-IV-04): ghi rõ ở E5 và ở trường 17; ô 21, 23 và tệp thẻ chỉ theo giới hạn riêng.

**Đề xuất QA tạm thời**

- `TC-THN-008` lần gửi 3 gắn `chờ BA – Q20`: Hướng 1 → `ERR-DK-05`, không sinh hồ sơ; Hướng 2 → đăng ký thành công, hồ sơ có đủ 6 tệp. Hai lần gửi đầu (11 tệp; tệp sai định dạng) chấm ngay.

---

## CR-GY-Q21 — Gợi ý câu hỏi tương tự lấy kho toàn quốc, nhưng quyền đọc kho của cán bộ chỉ trong đơn vị

**Bối cảnh testcase**

- Nhóm thay đổi T7 — FR-II-12 Gợi ý câu hỏi đã xử lý tương tự.
- Nội dung kiểm tra: kho có bản ghi đã duyệt, cùng lĩnh vực, thuộc đơn vị khác và thuộc cấp TW; cán bộ tiếp nhận ở đơn vị thứ ba đọc gợi ý — có thấy hai bản ghi đó không, mở được không.
- Testcase bị ảnh hưởng: `TC-GY-004` (cả TC chờ); `TC-GY-018` (một ý — nội dung gợi ý cán bộ Trung ương nhận được).

**Điểm mâu thuẫn trong SRS v3.5**

1. FR-II-12 lấy phạm vi toàn quốc:
   - "| Phạm vi so khớp | Kho câu hỏi ở trạng thái đã duyệt hoặc đã công khai, còn hiệu lực. Phạm vi **toàn quốc**. …"
   - Bước 1 chỉ ghi "Kiểm tra quyền | BR-AUTH-01", bước 4 "Lọc cứng theo lĩnh vực pháp luật; chỉ lấy bản ghi đã duyệt hoặc đã công khai, còn hiệu lực" — không lọc đơn vị.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1092`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1103`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1106`

2. Ma trận quyền dữ liệu chỉ cho vai trò cán bộ nghiệp vụ đọc KHO_CAU_HOI **trong đơn vị mình** (dấu `*`), và đường tra kho hiện có của cán bộ (tư vấn nhanh) áp phân quyền theo đơn vị:
   - "| KHO_CAU_HOI | R | CRUD* | CRUD* | CRUD* | RU* | RU* | RU* | R | — | — | — |"
   - "R*=Read scoped (chỉ đơn vị mình)"; bảng là "quyền ở MỨC DỮ LIỆU".
   - FR-XI (tư vấn nhanh) bước 4: "… áp phân quyền dữ liệu theo `don_vi_id` nếu có"
   - Hệ quả: cán bộ thấy gợi ý từ đơn vị khác nhưng theo ma trận không được đọc bản ghi đó — mở chi tiết, chép câu trả lời có được không; hoặc nếu gợi ý bị lọc theo đơn vị thì trái dòng "toàn quốc".

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1375`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1325`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1327`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-13-tv-nhanh.md:202`

**Câu hỏi cần BA xác nhận**

Gợi ý FR-II-12 đưa kết quả toàn quốc hay chỉ trong đơn vị của cán bộ?

1. **Hướng 1 — toàn quốc** (theo FR-II-12): bổ sung ngoại lệ vào ma trận / BR-DATA-08 — cán bộ được đọc bản ghi kho đã duyệt của đơn vị khác khi nó nằm trong gợi ý (hoặc chỉ đọc qua khối gợi ý, không mở chi tiết).
2. **Hướng 2 — theo đơn vị** (theo ma trận): sửa dòng "Phạm vi toàn quốc" và bước 4 của FR-II-12 thành lọc theo `don_vi_id` như tư vấn nhanh.

**Đề xuất QA tạm thời**

- `TC-GY-004` gắn `chờ BA – Q21`, hai hướng ghi sẵn: Hướng 1 → danh sách gợi ý có cả hai bản ghi của đơn vị khác; Hướng 2 → không có. Việc mở chi tiết bản ghi đơn vị khác chỉ ghi lại, không chấm.

---

## CR-GY-Q22 — Ô "Lĩnh vực pháp luật" ở bước tiếp nhận (FR-II-03 trường 3): có đường nào tạo được hồ sơ thiếu lĩnh vực không

**Bối cảnh testcase**

- Nhóm thay đổi T3 — FR-II-03 thêm trường 3, bắt buộc khi hồ sơ chưa có lĩnh vực, ẩn khi đã có.
- Nội dung kiểm tra: tiếp nhận hồ sơ thiếu lĩnh vực (phải chọn mới tiếp nhận được); hồ sơ đã có lĩnh vực (ẩn ô, không đổi được ở bước này).
- Testcase bị ảnh hưởng: `TC-PL-001`, `TC-PL-002` (P0), `TC-PL-004`; `TC-GY-012`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Lý do bổ sung trường 3 là dữ liệu Cổng đẩy sang có thể thiếu lĩnh vực:
   - "| 3 | linh_vuc_id | identifier | Cond | … **Bắt buộc nhập khi hồ sơ chưa có lĩnh vực pháp luật**; ẩn khi hồ sơ đã có"
   - "… nếu dữ liệu Cổng Pháp luật quốc gia đẩy sang thiếu thì **CB NV không có đường nào bổ sung**…"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:325`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:330`

2. Nhưng mọi đường tạo hồ sơ hỏi đáp trong SRS đều bắt buộc lĩnh vực, kể cả API nhận từ Cổng — API còn kiểm tra `linh_vuc_id` tồn tại trước khi tạo:
   - FR-II-01: "| 3 | linh_vuc_id | identifier | Y | Lĩnh vực PL (từ UC99) |"
   - API nhận hồ sơ: "| 3 | linh_vuc_id | identifier | Y | FK → DANH_MUC | Lĩnh vực pháp luật DN chọn trên Cổng. |"
   - "| 3 | Validate payload: `external_id` không trống, `noi_dung` ≤ 5000 ký tự, `linh_vuc_id` tồn tại, `don_vi_id` tồn tại |"
   - Theo văn bản, trường 3 không bao giờ hiện. Ba testcase (hai P0) chỉ chạy được trên hồ sơ DBA sửa tay bỏ lĩnh vực.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:102`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:1168`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-16-api.md:1183`

**Câu hỏi cần BA xác nhận**

Có đường nào (Cổng, tích hợp khác, nhập tay) tạo hồ sơ hỏi đáp thiếu lĩnh vực không?

1. **Hướng 1 — có:** ghi rõ đường đó và nới `linh_vuc_id` ở FR-II-01 / API tương ứng thành tùy chọn; trường 3 của FR-II-03 giữ như hiện nay.
2. **Hướng 2 — không:** bỏ trường 3 và ghi chú ở FR-II-03, hoặc giữ như phương án dự phòng cho dữ liệu lỗi nhưng ghi rõ; testcase hạ ưu tiên.

**Đề xuất QA tạm thời**

- `TC-PL-001`, `TC-PL-002`, `TC-PL-004`, `TC-GY-012` vẫn chạy trên hồ sơ DBA dựng, có ghi chú Q22 ở tiền đề. BA chốt Hướng 2 thì hạ ưu tiên ba TC đầu (không còn P0).

---

## CR-GY-Q23 — Gắn doanh nghiệp vào hồ sơ ẩn danh **sau khi đã tiếp nhận** (FR-II-01 Chỉnh sửa): ba trường phân loại có tự điền theo doanh nghiệp không

**Bối cảnh testcase**

- Nhóm thay đổi T3 — FR-II-01 thêm ba trường 12–14 (quy mô, hình thức tổ chức, tỉnh/thành của doanh nghiệp), là ảnh chụp tại thời điểm tiếp nhận; FR-II-11 bước 7 điền ba trường này khi chuyển luồng hồ sơ ẩn danh.
- Nội dung kiểm tra: hồ sơ ẩn danh đã tiếp nhận (ba trường trống), cán bộ dùng **Chỉnh sửa** (FR-II-01) gắn doanh nghiệp — sau khi lưu, ba trường có giá trị theo doanh nghiệp hay vẫn trống.
- Testcase bị ảnh hưởng: `TC-PL-021` (⏸, thêm ngày 14/09 khi rà biên).

**Điểm mâu thuẫn trong SRS v3.5**

1. Trường 12 (và 13, 14 cùng khuôn) viết quy tắc điền theo điều kiện `doanh_nghiep_id` có giá trị — đọc theo nghĩa rộng thì gắn doanh nghiệp lúc nào cũng điền:
   - "**Ảnh chụp tại thời điểm tiếp nhận.** Hệ thống điền sẵn theo hồ sơ doanh nghiệp khi `doanh_nghiep_id` có giá trị; CB NV sửa lại được. Câu hỏi ẩn danh → để trống"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:111`

2. Ghi chú ngay dưới bảng và tên trường lại giới hạn vào một thời điểm; phần Chỉnh sửa (bước 1–4: kiểm trạng thái, kiểm dữ liệu vào, cập nhật bản ghi, ghi nhật ký) không nói gì về ba trường khi `doanh_nghiep_id` đổi từ trống sang có giá trị:
   - "**Ba trường 12–14 là ảnh chụp tại thời điểm tiếp nhận, KHÔNG đọc động sang hồ sơ doanh nghiệp**"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:115`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:151`–`:154`

3. BA đã phải viết riêng quy tắc điền ba trường cho đường chuyển luồng (FR-II-11 bước 7), cho thấy đường Chỉnh sửa chưa có quy tắc:
   - "**Nếu hồ sơ hỏi đáp gốc chưa gắn doanh nghiệp** (câu hỏi ẩn danh): ghi `doanh_nghiep_id` vừa xác định **vào chính hồ sơ hỏi đáp gốc**, và điền ba trường phân loại `quy_mo_dn_id`, `hinh_thuc_to_chuc_id`, `tinh_thanh_dn_id` theo doanh nghiệp đó — **trước khi đóng hồ sơ**"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:996`

**Vì sao testcase không tự chọn được**: hai cách đọc cho hai kết quả trái nhau trên cùng bản ghi, và kéo theo hai số liệu báo cáo FR-IX-01 khác nhau (hồ sơ nằm ở nhóm "Không xác định" của cả ba chiều, hay nằm ở nhóm địa bàn / quy mô / hình thức của doanh nghiệp).

**Câu hỏi cần BA xác nhận**

Khi gắn doanh nghiệp vào hồ sơ ẩn danh bằng Chỉnh sửa sau khi đã tiếp nhận, ba trường 12–14 xử lý thế nào?

1. **Hướng 1 — tự điền theo hồ sơ doanh nghiệp tại lúc gắn** (thống nhất với FR-II-11 bước 7; báo cáo có địa bàn / quy mô / hình thức). Nếu chọn, đề nghị ghi thêm một bước ở phần Chỉnh sửa của FR-II-01.
2. **Hướng 2 — giữ trống** (ảnh chụp chỉ lấy một lần ở bước tiếp nhận). Nếu cần, cán bộ nhập tay ba trường ở bước sửa — phần thao tác thuộc H1, không hỏi thêm ở đây.

**Đề xuất QA tạm thời**

- `TC-PL-021` chạy được ngay: phần chắc chắn ở cả hai hướng (doanh nghiệp được ghi, các trường khác và hạn xử lý không đổi, nhật ký giá trị cũ → mới) vẫn kiểm; phần ba trường gắn nhãn `⏸ chờ BA – Q23`, không chấm. File 08 (FR-IX-01) không dựng hồ sơ kiểu này để Bảng A không lệch.

---

## CR-GY-Q24 — Số thẻ hành nghề có phải duy nhất toàn hệ thống không

**Bối cảnh testcase**

- Nhóm thay đổi T6 — số thẻ hành nghề `so_the_hanh_nghe` (bắt buộc khi `loai_tvv = 'TVV'`) ở FR-IV-03 trường 18a, FR-IV-01 trường 12, FR-IV-04 trường 7 và Entity HO_SO_TU_VAN_VIEN trường 6.
- Nội dung kiểm tra: đăng ký tư vấn viên mới với số thẻ trùng từng ký tự số thẻ của tư vấn viên đang hoạt động — được lưu hay bị chặn.
- Testcase bị ảnh hưởng: `TC-THN-027` (⏸, thêm ngày 14/09 khi rà biên). **Khác Q07**: Q07 hỏi ràng buộc thẻ có áp cho đường FR-IV-01 không; Q24 hỏi tính duy nhất của số thẻ.

**Điểm mâu thuẫn trong SRS v3.5**

1. Cột số thẻ chỉ có ràng buộc độ dài và điều kiện bắt buộc, không có "unique"; trong cùng bảng chỉ `tu_van_vien_id` là UNIQUE:
   - "| 6 | so_the_hanh_nghe | text | **Cond** | Max 50 ký tự. **Bắt buộc khi `TU_VAN_VIEN.loai_tvv = 'TVV'`** (NĐ 77/2008 Đ.20); không áp cho Chuyên gia"
   - "| 2 | tu_van_vien_id | identifier | Y | FK → TU_VAN_VIEN(id), UNIQUE |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2180`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2176`

2. Cùng biểu mẫu đăng ký, hai định danh cá nhân khác lại ghi rõ duy nhất toàn hệ thống — số thẻ là định danh cấp theo từng người nhưng không được đối xử như vậy:
   - "| 2 | cmnd_cccd | text | Y | Max 12, unique toàn hệ thống |"
   - "| 5 | email | text | Y | RFC 5322, unique toàn hệ thống |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:304`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:307`

3. Bảng lỗi của FR-IV-03, FR-IV-01, FR-IV-04 không có mã cho "số thẻ đã tồn tại" (chỉ có mã thiếu số thẻ `ERR-DK-10`, `ERR-TVV-10`, `ERR-NL-06`):
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:321`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:149`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:404`

**Vì sao testcase không tự chọn được**: theo đúng chữ SRS thì hệ thống phải lưu; theo lẽ thường (thẻ cấp theo từng người) thì hai hồ sơ cùng số thẻ là dữ liệu sai. Chấm theo SRS mà bản dựng chặn → phải log bug rồi BA có thể nói "chặn là đúng"; chấm theo lẽ thường mà bản dựng lưu → không có dòng SRS nào làm căn cứ.

**Câu hỏi cần BA xác nhận**

1. **Hướng 1 — không cần duy nhất** (giữ SRS hiện hành): đăng ký / thêm / sửa với số thẻ trùng vẫn lưu; chỉ CCCD, email chặn trùng.
2. **Hướng 2 — phải duy nhất toàn hệ thống**: bổ sung UNIQUE cho `so_the_hanh_nghe` và mã lỗi mới ở FR-IV-03, FR-IV-01, FR-IV-04. Đề nghị nói rõ so trùng có xét hồ sơ `TU_CHOI`, `VO_HIEU_HOA` hay không.

**Đề xuất QA tạm thời**

- `TC-THN-027` giữ nhãn chờ, ghi cả hai hướng. BA chọn Hướng 2 thì thêm TC tương ứng ở FR-IV-04 (bổ sung số thẻ trùng) và FR-IV-01 (sửa thành số thẻ trùng).

---

## CR-GY-Q25 — Báo cáo hỏi đáp FR-IX-01: hồ sơ xếp vào kỳ theo mốc ngày nào, và nhóm lấy theo trạng thái lúc chạy báo cáo hay tại cuối kỳ

**Bối cảnh testcase**

- Nhóm thay đổi T4 + BR-RPT-02 — FR-IX-01 thêm nhóm thứ ba "đã chuyển sang Vụ việc" và đổi mẫu số tỷ lệ trả lời.
- Nội dung kiểm tra: hồ sơ tiếp nhận cuối tháng, chuyển sang Vụ việc đầu tháng sau — cùng một hồ sơ có ngày tạo ở kỳ P và `ngay_chuyen_luong` ở kỳ P+1. Báo cáo kỳ P và kỳ P+1 mỗi kỳ ra số nào.
- Testcase bị ảnh hưởng: `TC-BC01-025` (⏸ một phần, thêm ngày 14/09 khi rà biên). Ghi chú "báo cáo đọc trạng thái hiện tại" ở `TC-BC01-017` là cách hiểu chưa có dòng SRS. **Liên quan Q14** (trạng thái nào vào nhóm nào) — BA có thể trả lời chung, nhưng đây là câu khác: Q14 hỏi nhóm, Q25 hỏi kỳ.

**Điểm mâu thuẫn trong SRS v3.5**

1. Công thức chỉ ghi "trong kỳ", không nói mốc ngày (ngày tạo, ngày tiếp nhận, hay ngày của sự kiện) dùng để xếp hồ sơ vào kỳ; hai ô `tu_ngay`, `den_ngay` là `datetime` nhưng không nói so với cột nào:
   - "**Công thức:** Đếm số hỏi đáp trong kỳ, theo phạm vi đơn vị, chia **ba nhóm**: đã trả lời / chờ trả lời / **đã chuyển sang Vụ việc**"
   - "| 2 | tu_ngay | datetime | Y | <= den_ngay |" · "| 3 | den_ngay | datetime | Y | >= tu_ngay |"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:157`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:70`–`:71`

2. BR-RPT-01 quy định cache hằng đêm và "đối chiếu lại real-time khi CB NV/PD mở từng báo cáo cụ thể" — tức số của một kỳ đã khép có thể đổi khi trạng thái hồ sơ đổi sau kỳ; không nói kỳ đã khép có được khóa số hay không:
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5834`

3. BR-RPT-02 (b), (d) chỉ nói hồ sơ đã chuyển vẫn trong tổng và tách thành nhóm thứ ba, không nói ở kỳ nào khi ngày tạo và ngày chuyển khác kỳ; FR-II-11 bước 8 ghi `ngay_chuyen_luong = NOW()` nhưng không báo cáo nào dùng cột này:
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5835`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:997`

**Vì sao testcase không tự chọn được**: với hồ sơ tạo 05/10 và chuyển 05/11, Hướng 1 cho kỳ 10 tăng "đã chuyển" và kỳ 11 không đổi; Hướng 2 cho kỳ 10 không đổi và kỳ 11 tăng "đã chuyển". Hai hướng cho hai bộ số khác nhau ở cả hai kỳ, và đổi tỷ lệ trả lời của từng kỳ.

**Câu hỏi cần BA xác nhận**

1. **Hướng 1 — kỳ theo ngày tạo (hoặc ngày tiếp nhận — BA chọn một) của hồ sơ; nhóm theo trạng thái tại lúc chạy báo cáo.** Kỳ đã khép có thể đổi số khi hồ sơ đổi trạng thái sau đó.
2. **Hướng 2 — sự kiện chuyển luồng tính vào kỳ có `ngay_chuyen_luong`** (nhóm "đã chuyển" của kỳ P+1), hoặc kỳ đã khép giữ số theo trạng thái tại cuối kỳ. Cần nói rõ tổng của kỳ P+1 có gồm hồ sơ đó không.

**Đề xuất QA tạm thời**

- `TC-BC01-025` chấm phần chắc chắn (hồ sơ chỉ đếm là "đã chuyển" ở đúng một kỳ; ở mỗi kỳ ba nhóm cộng bằng tổng; hồ sơ không nằm ở nhóm "đã trả lời" của kỳ nào); phần kỳ nào gắn nhãn `⏸ chờ BA – Q25`. Bộ dữ liệu chính của file 08 đặt mọi mốc của một hồ sơ trong cùng kỳ, nên các TC khác không phụ thuộc câu này; Bảng B15 của file 08 viết theo Hướng 1.

---

## Sửa tài liệu — không cần quyết định (BA sửa khi rảnh)

> Số D giữ nguyên để khớp testcase. D9 đã thành Q19, D27 là Q10 — không có dòng riêng. D13–D29 phát sinh khi BA đưa phản hồi vào SRS `aaee63b`.

| # | Chỗ cần sửa | Citation |
|---|---|---|
| D1 | Tiêu chí chấp nhận của FR-VIII-33 **chép nhầm từ FR-VIII-32** (nói tab "Loại sự kiện đào tạo", 2 bản ghi `TAP_HUAN`, dropdown Khóa học). FR-VIII-33 hiện không có tiêu chí chấp nhận đúng. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1651`–`:1656` |
| D2 | Bảng thuộc tính HOI_DAP ở tệp nhóm Hỏi đáp **thiếu ba cột** `quy_mo_dn_id`, `hinh_thuc_to_chuc_id`, `tinh_thanh_dn_id` (tệp nền đã có). | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1614`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1541` |
| D3 | FR-II-01 trường 7 và FR-II-11 trường 2 gọi `doanh_nghiep_id`, nhưng bảng HOI_DAP dùng tên cột `nguoi_gui_id` (FK DOANH_NGHIEP). | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:106`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:954`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1537` |
| D4 | Bảng chuyển trạng thái vụ việc, dòng khởi tạo `[*] → CHO_TIEP_NHAN`: nguồn chỉ liệt kê "DVC/HT khác/Trực tiếp" (thiếu FR-II-11) và ghi "tính deadline" lúc tạo — trái EC-V.I-05-09 và FR-V.I-18 (thời hạn tính từ lúc tiếp nhận). QA viết testcase theo FR-V.I-18. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2434`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:489`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1343` |
| D5 | FR-IV-03 bước 7 liệt kê các trường tạo bản ghi nhưng **thiếu năm trường mới** (số thẻ, tệp thẻ, hai loại minh chứng, số vụ việc tự kê khai); tiêu chí chấp nhận vẫn ghi "form đăng ký mở với 21 trường". | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:340`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:375` |
| D6 | FR-IX-13 đã đổi tên "theo quy mô DN" nhưng phần Mô tả và tiêu chí chấp nhận vẫn ghi "loại doanh nghiệp". | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:679`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:705` |
| D7 | Thiếu mã lỗi / câu thông báo cho: xóa trắng `tieu_de` / `mo_ta` khi chuyển; `ghi_chu_chuyen` quá 2.000 ký tự; loại hình hỗ trợ ngoài danh mục; chuyển thành công; không tích ô đối chiếu địa bàn. Testcase đang ghi "SRS Gap". | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1028`–`:1032`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:358`–`:359` |
| D8 | FR-V.I-18 phần Inputs và bước 4 ghi "tiếp nhận (FR-V.I-02)", nhưng FR-V.I-02 là "Gửi hồ sơ yêu cầu HTPL (UC52)" của doanh nghiệp. Bảng chuyển trạng thái gán `CHO_TIEP_NHAN → DA_TIEP_NHAN` cho FR-V.I-01. QA viết testcase theo bảng chuyển trạng thái. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1332`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1343`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:160`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2435` |
| D10 | Nối tiếp D7 — thiếu mã lỗi / câu thông báo ở các chức năng khác của đợt này. **(a) Dữ liệu sai:** lĩnh vực không thuộc `LINH_VUC_PL` khi tiếp nhận; ba trường phân loại hoặc hình thức tổ chức trên hồ sơ DN trỏ sai loại danh mục; lý do kiểm tra hồ sơ dưới 10 hoặc trên 5.000 ký tự (`ERR-KT-02` chỉ nói bỏ trống); phía gửi tự đặt loại lý do từ chối; số thẻ hành nghề quá 50 ký tự; tệp thẻ không phải PDF; quá 10 tệp minh chứng; số vụ việc tự kê khai âm; cán bộ nhập tay kênh `CONG_PLQG` hoặc tự gắn `hoi_dap_goc_id` khi lập vụ việc. **(b) Bị từ chối do phân quyền:** vai trò không phải CB NV chuyển hồ sơ; vai trò không phải CB NV đọc gợi ý; tư vấn viên tự sửa hồ sơ năng lực. Testcase đang ghi "SRS Gap" (14 TC). | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:325`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:111`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:107`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:526`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:527`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:320`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:321`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:324`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:325`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:324`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1600`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:929`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1067`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:388` |
| D11 | Hai dòng 2a (khối "Nguồn gốc hồ sơ") và 2b (dòng "Thời gian xử lý toàn trình") nằm trong bảng của SCR-V.I-02 (Thêm mới / Nhập thủ công), trong khi FR-V.I-18 đặt khối truy nguồn ở SCR-V.I-03 (chi tiết) và KPI-S-03 đặt dòng toàn trình ở SCR-V.I-03. Lệch thêm một điểm: dòng 2b chỉ hiện khi có `hoi_dap_goc_id`, còn KPI-S-03 tính mốc bắt đầu cho cả vụ việc tiếp nhận trực tiếp và không nêu điều kiện hiển thị — vụ việc không đến từ cầu nối có dòng này không. QA viết testcase theo FR-V.I-18 bước 3 kèm nội dung dòng 2a (TC-VVCL-003); dòng toàn trình trên màn chi tiết để phần hoãn giao diện. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1822`–`:1823`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1810`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1859`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1318`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1340`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:645`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:660` |
| D12 | FR-II-01 (doanh nghiệp gửi câu hỏi) không có ô nhập tiêu đề, trong khi bảng HOI_DAP có cột `tieu_de` bắt buộc và FR-II-11 trường 5 chép `HOI_DAP.tieu_de` sang vụ việc; không nói tiêu đề sinh từ đâu. QA: testcase file 01 ghi lại tiêu đề hệ thống lưu; trống thì nhập trong hộp thoại chuyển. *(phát hiện 14/09)* | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:100`–`:113`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1534`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:957` |
| D13 | Bảng "Thông báo khi chuyển luồng" (ba nhóm người nhận, chống gửi trùng) nằm trong FR-II-01, ngay trước Outputs của FR-II-01, trong khi FR-II-11 bước 11 dẫn "theo bảng dưới" — người đọc FR-II-11 không thấy bảng. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:188`–`:198`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1000` |
| D14 | Cùng một dòng người nhận "Cán bộ Nghiệp vụ của đơn vị thụ lý" ghi hai cách xác định tập: "dùng đúng tập người nhận mà `FR-V.I-02` đang xác định" và "theo `don_vi_id` của vụ việc mới" — FR-V.I-02 chọn đơn vị theo tỉnh/thành doanh nghiệp. Hai cách cho kết quả khác nhau khi doanh nghiệp ở tỉnh khác đơn vị thụ lý. QA chấm theo cột "Cách xác định tập" (`don_vi_id` của vụ việc). | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:193`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:200` |
| D15 | Nhóm người nhận thứ ba ghi "Người hỗ trợ pháp lý hoặc Tư vấn viên", nhưng hỏi đáp chỉ phân công cho CB NV hoặc người hỗ trợ pháp lý; bảng thuộc tính HOI_DAP ở tệp nền còn mô tả phân công tư vấn viên / tổ chức. QA xác định nhóm theo `nguoi_phan_cong_id`. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:194`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:553`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1639`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1550` |
| D16 | Chỉnh sửa hỏi đáp bước 1 chỉ kiểm "không phải DA_DUYET hoặc HOAN_THANH", chưa có `DA_CHUYEN_LUONG` (bước Xóa, BR-FLOW-03, nút Sửa và ma trận quyền đã có). Câu của `ERR-HD-04` vẫn là "Không thể sửa/xóa bản ghi đã phê duyệt" dù nay dùng cho cả hồ sơ đã chuyển. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:151`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:160`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:223`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1324`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1912`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:1451` |
| D17 | SCR-V.I-01 dòng 16a: bấm huy hiệu "Từ Hỏi đáp" mở hồ sơ hỏi đáp gốc, không có điều kiện cùng đơn vị như FR-V.I-18 bước 3a / 3b. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1791`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1341`–`:1342` |
| D18 | FR-V.I-18 bước 3a / 3b và dòng 2a khối "Nguồn gốc hồ sơ" chỉ xét `user.don_vi_id = HOI_DAP.don_vi_id`; ngoại lệ Cán bộ Trung ương / QTHT chỉ nằm ở ghi chú bên dưới — đọc riêng bước 3b thì cán bộ Trung ương cũng bị ẩn đường dẫn. QA chấm theo ghi chú. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1341`–`:1342`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1353`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1822`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1022` |
| D19 | Lặp chữ "(§Processing bước 6) (bước 6)". | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1351` |
| D20 | FR-V.I-12 trường 2 liệt kê hai nhãn loại lý do ("Ngoài phạm vi hỗ trợ" hoặc "Thiếu thành phần hồ sơ"), thiếu "Lý do khác" (`KHAC`) mới thêm ở FR-V.I-06. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:988`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:527`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:572` |
| D21 | "Hạng mục 2–7", "cả bảy hạng mục" viết cứng, trong khi UC106 cho QTHT thêm / bớt thành phần hồ sơ — số hạng mục thực tế có thể khác 7. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:527`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:567`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:572`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:433`–`:434`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:439` |
| D22 | Bước 4b chỉ khóa Đạt / Yêu cầu bổ sung khi hạng mục 1 không đạt; không nói hạng mục 1 đạt, có hạng mục 2–7 không đạt mà chọn Đạt thì sao. Tiêu chí chấp nhận chưa có ca 4a / 4b / 4c. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:571`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:573`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:619`–`:622` |
| D23 | Cùng một ràng buộc thẻ hành nghề, ba mã lỗi cùng câu: `ERR-TVV-10` (FR-IV-01), `ERR-DK-10` (FR-IV-03), `ERR-NL-06` (FR-IV-04). SCR-IV-02 mục 3.5 chỉ ghi `ERR-DK-10` / `ERR-NL-06`; tiêu chí chấp nhận ở `fr-04:218` không nêu mã. QA chấm `ERR-TVV-10` cho FR-IV-01. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:211`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:218`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:357`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:458`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1559`–`:1560` |
| D24 | FR-IX-18 gom theo `DOANH_NGHIEP.loai_dn_id` (hồ sơ doanh nghiệp hiện tại), trong khi hồ sơ chi trả có cột `quy_mo_dn` (quy mô dùng để xác định mức hỗ trợ) — SRS không nói cột này dùng cho báo cáo nào; hai giá trị có thể khác nhau. QA theo `fr-11:852`. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:852`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:2038` |
| D25 | FR-IX-01 ghi báo cáo dùng "ảnh chụp tại thời điểm tiếp nhận", nhưng câu hỏi ẩn danh được điền ba trường lúc chuyển luồng (FR-II-11 bước 7). QA chấm theo bước 7. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:183`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:185`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:996` |
| D26 | Bảng chuyển trạng thái vụ việc thiếu dòng `DA_TIEP_NHAN → DA_PHAN_CONG` (phân công lại sau khi người được phân công từ chối), dù FR-V.I-09 cho phép và quy tắc chuyển tiếp danh mục dựa vào. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2436`–`:2441`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:774`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:591` |
| D28 | Dòng mở lại `TU_CHOI → DA_TIEP_NHAN` dẫn "FR-V.I-xx" — chưa có chức năng; quy tắc chuyển tiếp danh mục dựa vào lối này. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2449`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:592` |
| D29 | Bước 3a "giữ nguyên các hạng mục đã tích": với `dat` 0 / 1, hạng mục cũ đã đánh "không đạt" có tính là "đã tích" không. | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:524`, `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:568` |

## Không đưa vào file này

- **Đang chờ CĐT:** H1, V1, V3, A5, T8 — như file trước. Testcase gắn `chờ CĐT`.
- **Điểm thuần giao diện:** các chỗ đếm số widget / số thẻ trên Dashboard chưa cộng thẻ KPI-S-03; nhãn "Quy mô doanh nghiệp" (còn sót ở SCR-VIII-08 ô 6 "Loại hình doanh nghiệp" — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1968`); danh sách tab dọc SCR-VIII-01 vẫn ghi 16 tab, chưa có tab Hình thức tổ chức (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1677` so với `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1622`); nút chép câu trả lời và hộp xác nhận ghi đè của khối gợi ý. Để lại tới khi có UI.
