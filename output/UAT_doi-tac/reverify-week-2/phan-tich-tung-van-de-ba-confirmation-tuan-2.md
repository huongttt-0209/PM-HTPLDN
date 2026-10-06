# Phân tích từng vấn đề — Các điểm cần BA xác nhận (UAT Tuần 2)

**Nguồn câu hỏi:** `docs/Reference/Fix bug KTĐL/ba-confirmation-needed-week-2.md`
**Nguồn đối chiếu:** CSV baseline `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` (CSV là chuẩn cao nhất, trên SRS) và bộ SRS `_bmad-output/planning-artifacts/srs-v3.5/`.

**Cách đọc.** Giữ theo nhóm module. Mỗi vấn đề gồm 3 mục:
- **Vấn đề** — đối tác báo gì, hoặc câu hỏi nghiệp vụ.
- **Hiện trạng phần mềm — SRS** — tách 3 dòng: *Phần mềm đang làm gì* · *SRS/CSV nói gì* · *Ai đúng*.
- **Giải pháp** — nên làm gì, ai làm.

Case nào **phần mềm đã đúng SRS** thì có thêm **Phản hồi cho KTĐL** — câu trả lời gửi lại tổ kiểm thử.

**Bốn loại kết luận:**
- **Chuyển Dev** — có căn cứ SRS để coi là lỗi, giao Dev sửa.
- **Chờ BA quyết** — SRS chưa quy định, cần chị chốt có làm hay không.
- **Dọn SRS** — hai chỗ trong SRS nói ngược nhau, phải sửa cho khớp dù chị quyết thế nào.
- **Không phải lỗi** — phần mềm đúng đặc tả, chỉ cần sửa lại "Kết quả mong đợi" của test case.

---

## Nhóm 1 — Module Đào tạo, tập huấn (FR-III)

### QLDXDTTH_03 — DN có cần màn "Xem chi tiết" đề xuất riêng không?

**Vấn đề:** Trên giao diện DN, đối tác bấm "Xem" một đề xuất đào tạo để mở màn chi tiết, nhưng không có chức năng đó.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* mỗi đề xuất hiển thị dạng thẻ, đã có đủ thông tin ngay trên thẻ (nội dung, lĩnh vực, thời gian, địa điểm, số lượng, ngày gửi, trạng thái) và nút Chỉnh sửa / Xóa. Không có nút "Xem" riêng.
- *CSV (chuẩn):* dòng 287-288 tách "xem danh sách" và "xem chi tiết" thành **hai thao tác riêng của DN** — tức DN phải có một màn xem chi tiết.
- *SRS:* FR-III-13 và SCR-III-01 chỉ cho **cán bộ** được "Xem", bỏ mất thao tác "DN xem chi tiết" của CSV (`srs-fr-03:1017`, `:1800`). Đây là chỗ SRS ghi thiếu so với CSV, không dùng để bênh phần mềm được.
- *Ai đúng:* đối tác đúng — phần mềm thiếu màn xem chi tiết cho DN.

**Giải pháp:** **Chuyển Dev.** BA đã chốt 15/07/2026: cho DN/NHT xem đề xuất (cả danh sách lẫn chi tiết). Cách làm gọn: màn "Xem chi tiết" cho cán bộ đã có sẵn (SCR-III-01 Thành phần 8), chỉ **thêm DN/NHT vào làm người xem** (chỉ đọc, chỉ thấy đề xuất của mình), không dựng màn mới. Chi tiết ở `de-xuat-update-srs-QLDXDTTH_03-dn-xem-de-xuat.md`. BA sửa SRS + Dev FE làm giao diện.

### QLDXDTTH_06 — Xóa đề xuất xong không có thông báo thành công

**Vấn đề:** DN xóa một đề xuất, hệ thống không báo là đã xóa thành công.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* có hộp xác nhận, bấm Xóa thì danh sách cập nhật (đề xuất biến mất, tức xóa có chạy), nhưng suốt gần 2 giây không có thông báo nào. Trong khi đó luồng tạo đề xuất lại có thông báo "Đã gửi đề xuất thành công".
- *SRS:* quy ước chung UI-04 yêu cầu "thao tác thành công phải có thông báo" (`srs-v3.5.md:571`). Xóa thành công cũng là thao tác thành công.
- *Ai đúng:* đối tác đúng — thiếu thông báo là vi phạm UI-04.

**Giải pháp:** **Chuyển Dev FE.** Phạm vi giao diện DN đã được BA chốt từ 02/05/2026 nên không còn vướng câu hỏi phạm vi. (Verdict đổi từ "BA confirm" sang **Open**.)

### QLDXDTTH_09 — DN không nhận thông báo khi đề xuất được tiếp nhận

**Vấn đề:** DN gửi đề xuất đào tạo lên Sở/Bộ, gửi xong muốn biết cán bộ đã tiếp nhận chưa, nhưng không nhận được thông báo nào.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* trạng thái đề xuất phía DN **có** cập nhật đúng (chuyển sang "Đã tiếp nhận"), nhưng trung tâm thông báo của DN vẫn **rỗng**. Vậy phần "không nhận thông báo" là có thật; phần "trạng thái không cập nhật" thì không xảy ra.
- *SRS:* FR-III-13 **chỉ quy định thông báo một chiều** — khi DN gửi đề xuất thì báo cho cán bộ ("Thông báo CB NV" ở Processing, "CB NV nhận thông báo" ở Postconditions, `srs-fr-03:1019`, `:1023`). SRS **không** yêu cầu báo ngược lại cho DN khi cán bộ tiếp nhận / đánh dấu đã thực hiện. BR-NOTIF-01 tuy có ghi FR-III-13 ở cột "Áp dụng FR", nhưng trong 8 sự kiện cụ thể không có sự kiện nào cho vòng đời đề xuất đào tạo (`srs-v3.5.md:5520`).
- *Ai đúng:* phần mềm đúng SRS hiện hành — không báo chiều cán bộ→DN là đúng đặc tả. Kỳ vọng đối tác vượt phần SRS quy định.

**Giải pháp:** **Không phải lỗi.** Phần mềm làm đúng FR-III-13. Nếu muốn có thông báo cho DN khi đề xuất đổi trạng thái thì đây là **yêu cầu cải tiến** (thêm chức năng mới), cần liệt kê vào danh sách yêu cầu cải tiến; sau khi duyệt mới bổ sung SRS (thêm sự kiện (9) vào BR-NOTIF-01 + cập nhật FR-III-13 §Processing/§Postconditions) rồi giao Dev.
*(Phân biệt: chiều ngược lại — DN gửi đề xuất thì phải báo cán bộ — SRS đã yêu cầu rõ nhưng phần mềm không chạy → đó là lỗi Dev, đã log riêng `BUG-DEXUAT-NOTIF-CB-01`. Khác hẳn chiều cán bộ→DN ở đây vốn không được đặc tả.)*

**Phản hồi cho KTĐL:** Theo SRS hiện hành (FR-III-13), hệ thống chỉ báo cho cán bộ khi DN gửi đề xuất; SRS không quy định báo lại cho DN khi cán bộ tiếp nhận hoặc đánh dấu đã thực hiện. Vì vậy việc DN không nhận thông báo ở chiều này là **đúng đặc tả, không phải lỗi**. Nếu cần bổ sung thông báo cho DN, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### QLGVTG_05 — Số điện thoại giảng viên có cần kiểm tra định dạng không?

**Vấn đề:** Nhập số điện thoại giảng viên sai định dạng vẫn lưu được, không báo lỗi.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* cho lưu số điện thoại sai; các trường khác vẫn kiểm tra đúng (email sai thì báo, bỏ trống lĩnh vực thì báo).
- *SRS:* trường số điện thoại là tự do — không bắt buộc, không ràng buộc định dạng, không có mã lỗi (`srs-fr-03:965`, `:973`). Vậy theo SRS hiện tại, phần mềm không sai.
- *Ai đúng:* SRS chưa yêu cầu, nên chưa thể coi là lỗi.

**Giải pháp:** **BA đã đồng ý bổ sung kiểm tra định dạng (15/07/2026), vẫn để không bắt buộc.** Định dạng theo đúng chuẩn viễn thông VN hiện hành: **số phải bắt đầu bằng số 0, gồm 10 chữ số (di động) hoặc 11 chữ số (số cố định)** — quy tắc gợi ý cho Dev `^0\d{9,10}$`.
- *Vì sao không phải "đúng 10 số":* sau chuyển đổi 2018-2019, di động VN đúng 10 số (bắt đầu bằng 0); nhưng **số cố định là 11 số** (số 0 + mã vùng + thuê bao). Bắt "đúng 10 số" sẽ loại nhầm số cố định. Quy ước "10-11 chữ số" sẵn có trong SRS (TVV `srs-fr-04:297`, NHT, hỏi đáp) vốn **đã đúng độ dài** — điểm bổ sung mới chỉ là ràng buộc "bắt đầu bằng số 0" (hiện chưa field nào bắt).
- *Việc cần làm:* bổ sung ràng buộc + mã lỗi vào FR-III-11 §Đầu vào (`srs-fr-03:965`) và §Lỗi (`:973`); và thống nhất một quy ước SĐT chung cho cả hệ thống (xem Mục tổng hợp B.5, theo quyết định "siết cả hệ thống"). Dev FE (+ BE nếu kiểm ở máy chủ).

### QLGVTG_06 — Giảng viên mới thêm không lên đầu danh sách

**Vấn đề:** Cán bộ thêm một giảng viên, mong thấy bản ghi mới ở đầu danh sách để kiểm lại, nhưng nó không lên đầu.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* danh sách sắp theo tên A→Z, nên bản ghi mới về đúng vị trí bảng chữ cái chứ không lên đầu.
- *SRS:* quy ước chung DG-06 yêu cầu "sắp xếp mặc định theo thời gian cập nhật mới nhất" (`srs-v3.5.md:919`). Quy ước này nằm ở mục dùng chung nên phiếu QA đã bỏ sót.
- *Ai đúng:* đối tác đúng — sắp A→Z là vi phạm DG-06.

**Giải pháp:** **Chuyển Dev.** (Verdict đổi từ "BA confirm" sang **Open**.)

### QLGVTG_07 — Có cần nút "Xem" riêng ở cột thao tác không?

**Vấn đề:** Cột thao tác giảng viên chỉ có Sửa / Xóa, không có nút "Xem" riêng.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* màn chi tiết 2 tab (Thông tin + Lịch sử giảng dạy) **vẫn mở được** bằng cách bấm vào tên giảng viên.
- *SRS:* FR-III-11 yêu cầu có màn chi tiết 2 tab (đã có), nhưng không bắt buộc phải có nút "Xem" riêng ở cột thao tác (`srs-fr-03:959`, `:977`). Tuy nhiên, khảo sát toàn hệ thống cho thấy **hầu hết màn danh sách nghiệp vụ đều CÓ nút "Xem" (👁) riêng** ở cột Hành động: Hỏi đáp (`srs-fr-02:1044`), Doanh nghiệp (`srs-fr-07:442`), Vụ việc (`srs-fr-05:1639`), Đào tạo — Chương trình/Khóa/Đề xuất (`srs-fr-03:1700`, `:1775`, `:1800`), Quản trị user (`srs-fr-10:1660`), Mẫu phản hồi (`:1769`). Màn giảng viên (SCR-III-05, `:1852`) là **ngoại lệ** — chỉ Sửa/Xóa, mở chi tiết qua click tên.
- *Ai đúng:* yêu cầu nghiệp vụ (xem được chi tiết) đã được đáp ứng; nhưng kỳ vọng của đối tác **khớp với chuẩn chung** của hệ thống, giảng viên đang lệch chuẩn.

**Giải pháp:** **BA đã đồng ý bổ sung nút "Xem" (👁) — 15/07/2026.** Thêm nút 👁 Xem vào cột Hành động của màn Giảng viên (SCR-III-05, `srs-fr-03:1852`), mở màn chi tiết 2 tab sẵn có, cho nhất quán với các màn danh sách khác. Chỉ hiển thị, dữ liệu và màn chi tiết đã có. Owner Dev FE. *(BA không nâng thành quy ước chung — chỉ sửa riêng màn giảng viên.)*

### QLGVTG_08 — Bấm "Sửa" nhưng breadcrumb vẫn ghi "Chi tiết"

**Vấn đề:** Bấm nút Sửa giảng viên thì mở được form sửa, nhưng đường dẫn phía trên (breadcrumb) lại ghi "Chi tiết".

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* bấm Sửa và bấm tên giảng viên đều mở cùng một màn, breadcrumb luôn ghi "Chi tiết".
- *SRS:* FR-III-11 không quy định nhãn breadcrumb theo chế độ. Nhưng module Tư vấn viên đã có tiền lệ: bấm Sửa thì ghi "Chỉnh sửa [Họ tên]" (`srs-fr-04:1480`).
- *Ai đúng:* đối tác đúng; và chính SRS module khác đã làm phân biệt nhãn.

**Giải pháp:** **BA đã đồng ý — 15/07/2026.** Bấm "Sửa" thì breadcrumb/tiêu đề ghi **"Chỉnh sửa"**, phân biệt với "Chi tiết" (xem). Bổ sung một dòng quy ước chung về nhãn đường dẫn theo chế độ (Xem chi tiết / Chỉnh sửa / Thêm mới) để đồng bộ giữa các module — theo tiền lệ module TVV (`srs-fr-04:1480`). Owner Dev FE.

### QLGVTG_12 — Cán bộ Trung ương xóa giảng viên tỉnh khác bị chặn nhầm

**Vấn đề:** Cán bộ Trung ương xóa một giảng viên An Giang (đang dạy 3 khóa), mong hệ thống cảnh báo "đang dạy N khóa", nhưng lại báo "Đơn vị của bạn khác đơn vị của giảng viên".

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* so khớp đơn vị bằng nhau tuyệt đối, nên chặn cán bộ Trung ương xóa giảng viên tỉnh. Khi xóa giảng viên đang dạy cũng chưa hiện cảnh báo số khóa.
- *SRS:* giảng viên **có** phân quyền theo đơn vị (`srs-v3.5.md:2534`, `:1256`; `srs-fr-03:976`), NHƯNG cán bộ Trung ương là **ngoại lệ, được thao tác toàn quốc** (BR-AUTH-08, `srs-fr-05:2350`). SRS cũng đã có sẵn cảnh báo "đang dạy N khóa" (WRN-GV-01, `srs-fr-03:973`, `:967`).
- *Ai đúng:* đối tác đúng. Đáp án không nằm trong 2 phương án của phiếu hỏi, mà là phương án thứ 3: giảng viên có phân quyền đơn vị, nhưng Trung ương là ngoại lệ toàn quốc.

**Giải pháp:** **Chuyển Dev BE.** Bỏ so khớp đơn vị tuyệt đối, áp đúng quy tắc: Trung ương thao tác toàn quốc, Bộ ngành / Địa phương chỉ trong đơn vị mình. Khi giảng viên đang được phân công thì hiện cảnh báo WRN-GV-01 và bắt xác nhận trước khi xóa. (Verdict đổi sang **Open**.)
*Kèm dọn SRS (BA đã đồng ý 15/07/2026):* ghi chú "giữ giảng viên bản cũ 11 trường" (`CHANGELOG-v3-to-v3.5.md:2018`, `srs-fr-03:1876`) mâu thuẫn với entity thật 18 trường có `don_vi_id` → **xóa ghi chú, lấy entity 18 trường làm chuẩn.**

### TKGVTG_07 — Không sắp xếp được danh sách giảng viên bằng cách bấm tiêu đề cột

**Vấn đề:** Bấm tiêu đề cột "Họ tên" / "Ngày" không đổi thứ tự danh sách. *(Khác QLGVTG_06: case kia nói về thứ tự mặc định, case này nói về bấm cột để sắp xếp.)*

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* không hỗ trợ bấm cột để sắp xếp.
- *SRS:* mẫu danh sách chung P-01 không liệt kê sắp xếp theo cột (`srs-v3.5.md:681`).
- *Ai đúng:* phần mềm đúng SRS hiện hành (FR-III-12 và mẫu P-01 đều không quy định sắp xếp theo cột — chỉ lọc + phân trang).

**Giải pháp:** **Không phải lỗi (BA chốt 15/07/2026).** Phần mềm làm đúng SRS. Nếu thực sự có nhu cầu sắp xếp theo cột → liệt kê vào **danh sách yêu cầu cải tiến**. Sửa lại Expected của test case.

**Phản hồi cho KTĐL:** Theo SRS hiện hành, màn tìm kiếm giảng viên (FR-III-12) và mẫu danh sách chung P-01 không quy định sắp xếp theo cột — chỉ lọc + phân trang. Phần mềm làm đúng đặc tả, không phải lỗi. Nếu cần bổ sung sắp xếp theo cột, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### DKTGKH_12 — Import Excel đăng ký học viên: có cần bước "xem trước" không?

**Vấn đề:** Cán bộ nạp file Excel danh sách đăng ký học viên, không có bước xem trước trước khi nạp.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* chọn file rồi bấm "Bắt đầu Import" là nạp thẳng, sau đó mới hiện báo cáo kết quả (tổng / thành công / bỏ qua trùng / lỗi + lý do).
- *SRS:* FR-III-04 mô tả đúng luồng nạp-rồi-báo-cáo, không tách bước xem trước (`srs-fr-03:474`, `:485`).
- *Ai đúng:* phần mềm đúng SRS hiện hành (FR-III-04 mô tả nạp-rồi-báo-cáo, không có bước xem trước).

**Giải pháp:** **Không phải lỗi.** Phần mềm làm đúng FR-III-04. Nếu thực sự cần bước xem trước (nạp thẳng rồi mới báo lỗi thì dữ liệu hỏng đã vào hệ thống, phải dọn tay) → liệt kê vào **danh sách yêu cầu cải tiến**. Sửa lại Expected của test case.

**Phản hồi cho KTĐL:** Theo SRS hiện hành (FR-III-04, UC23), chức năng import là "validate → nạp từng dòng → báo cáo kết quả", không có bước xem trước tách riêng. Phần mềm làm đúng đặc tả, không phải lỗi. Nếu cần bổ sung màn xem trước, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### TTKTLBG_02 — Tìm kho tài liệu thiếu bộ lọc "Lĩnh vực pháp lý"

**Vấn đề:** Màn tìm kho tài liệu / bài giảng không có bộ lọc theo Lĩnh vực pháp lý.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* có 5 bộ lọc (Tên bài giảng, Loại tài liệu, Công khai, Từ ngày, Đến ngày).
- *SRS:* FR-III-08 đúng 5 tiêu chí này, không có lĩnh vực pháp lý (`srs-fr-03:782-788`).
- *Ai đúng:* phần mềm đúng SRS hiện hành; BA quyết định bổ sung.

**Giải pháp:** **BA đã đồng ý bổ sung bộ lọc "Lĩnh vực pháp lý" — 15/07/2026.** Bài giảng đã có sẵn trường lĩnh vực khi tạo; có dữ liệu mà không cho lọc là lãng phí. Bổ sung bộ lọc vào FR-III-08 §Đầu vào (`srs-fr-03:782-788`). Owner BA sửa SRS → Dev FE + BE.

### QLNHCH_02 — Màn Ngân hàng câu hỏi có cần "Thẻ thống kê tổng quan" không?

**Vấn đề:** Màn Ngân hàng câu hỏi không có thẻ thống kê tổng quan.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* có tiêu đề + 2 tab (Câu hỏi / Đề kiểm tra), mỗi tab có thanh lọc và bảng danh sách phân trang.
- *SRS:* FR-III-09 chỉ yêu cầu danh sách + phân trang, không nhắc thẻ thống kê (`srs-fr-03:868-877`, `:892`).
- *Ai đúng:* phần mềm đúng SRS.

**Giải pháp:** **Không phải lỗi.** Phần mềm làm đúng SRS. Nếu thực sự có nhu cầu thẻ thống kê tổng quan → liệt kê vào **danh sách yêu cầu cải tiến**. Sửa lại Expected của test case.

**Phản hồi cho KTĐL:** Theo SRS hiện hành (FR-III-09, UC28), màn Ngân hàng câu hỏi gồm danh sách + phân trang, không quy định thẻ thống kê tổng quan. Phần mềm làm đúng đặc tả, không phải lỗi. Nếu cần bổ sung, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### QLNHCH_04 — Trạng thái câu hỏi: 2 giá trị hay bộ 3?

**Vấn đề:** Đối tác mong bộ 3 trạng thái (Nháp / Công khai / Ẩn); phần mềm chỉ có 2 (Kích hoạt / Vô hiệu hóa).

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* trường Trạng thái có 2 giá trị Kích hoạt / Vô hiệu hóa.
- *SRS:* đúng 2 giá trị này, kèm ghi chú "BA chốt 2 trạng thái là chuẩn, bỏ bộ Nháp/Công khai/Ẩn cũ" (07/05/2026, `srs-fr-03:848`). Bộ 3 là bộ cũ đã bỏ.
- *Ai đúng:* phần mềm đúng quyết định BA hiện hành.

**Giải pháp:** **Không phải lỗi.** Sửa lại "Kết quả mong đợi" của test case về 2 giá trị.

**Phản hồi cho KTĐL:** Phần mềm làm đúng SRS — trường Trạng thái câu hỏi có 2 giá trị Kích hoạt / Vô hiệu hóa là chủ đích, không phải lỗi. Lý do: bộ 3 trạng thái Nháp / Công khai / Ẩn thực chất là mô hình **xuất bản ra ngoài**, chỉ phù hợp với nội dung được công khai lên Cổng Pháp luật Quốc gia (như biểu mẫu — vẫn giữ bộ 3). Còn **câu hỏi kiểm tra là tài nguyên nội bộ**, chỉ dùng để soạn đề kiểm tra, không công khai ra Cổng — nên không cần trạng thái "Công khai/Ẩn", chỉ cần **dùng được (Kích hoạt) / ngừng dùng (Vô hiệu hóa)**. BA đã chốt bộ 2 này từ 07/05/2026 (khớp định nghĩa entity gốc, đã có bước chuyển đổi dữ liệu cũ). Đề nghị cập nhật lại Expected của test case theo bộ 2 giá trị.

### CBKQDTBD_01 — Công bố kết quả đào tạo có cấp chứng nhận PDF ký số không?

**Vấn đề:** Đối tác mong bấm "Công bố và sinh chứng nhận" sẽ sinh số và file PDF ký số cho từng học viên; phần mềm không có.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* chức năng công bố kết quả **đã có** ở tab "Kết quả" (công bố / hủy công bố + xuất DOCX), nhưng không sinh chứng nhận PDF ký số.
- *SRS:* FR-III-19 chọn **Hướng B** — "không cấp chứng nhận PDF" (`srs-fr-03:1278`). Lý do pháp lý: NĐ55/2019 không trao thẩm quyền cấp chứng nhận đào tạo cho phần mềm; PDF tự sinh dễ bị hiểu nhầm là chứng nhận chính thức (`:1280`).
- *Ai đúng:* việc không sinh chứng nhận là **cố ý**, phần mềm đúng SRS.

**Giải pháp:** **Không phải lỗi.** Phần mềm làm đúng Hướng B (không cấp chứng nhận PDF). Nếu là yêu cầu thật (muốn khôi phục cấp chứng nhận) → liệt kê vào **danh sách yêu cầu cải tiến** — lưu ý đây là mở rộng phạm vi có **rủi ro pháp lý** (NĐ55/2019 không trao thẩm quyền cấp chứng nhận đào tạo cho phần mềm), cần quy chế nội bộ Bộ Tư pháp trước khi làm.

**Phản hồi cho KTĐL:** Không sinh chứng nhận PDF là chủ đích theo Hướng B (duyệt 06/05/2026), vì NĐ55/2019 không cho phần mềm thẩm quyền cấp chứng nhận đào tạo; PDF tự sinh có thể bị hiểu nhầm là chứng nhận chính thức. Phần mềm đã làm đúng phạm vi (công bố kết quả), không phải lỗi. Nếu thực sự có nhu cầu cấp chứng nhận, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

---

## Nhóm 2 — Module Mạng lưới Tư vấn viên (FR-IV)

### QLTVV_07 & TKTVV_08 — Không sắp xếp được danh sách TVV bằng cách bấm tiêu đề cột

**Vấn đề:** Bấm tiêu đề cột (Mã TVV, Họ tên, Ngày công nhận) không đổi thứ tự. *(Hai mã case, cùng một vấn đề.)*

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* cả 12 cột đều không cho bấm để sắp xếp.
- *SRS:* mẫu danh sách chung P-01 không liệt kê sắp xếp theo cột (`srs-v3.5.md:681`). Nhưng module Vụ việc thì lại yêu cầu (`srs-fr-05:1647`) — tức SRS quy định không đều giữa các module.
- *Ai đúng:* phần mềm đúng SRS hiện hành (FR-IV-02 và mẫu P-01 không quy định sắp xếp theo cột).

**Giải pháp:** **Không phải lỗi (BA chốt 15/07/2026, chung với TKGVTG_07).** Phần mềm đúng SRS. Nếu có nhu cầu sắp xếp theo cột → liệt kê vào **danh sách yêu cầu cải tiến**. Sửa lại Expected của test case.

**Phản hồi cho KTĐL:** Theo SRS hiện hành, màn danh sách TVV (FR-IV-02) và mẫu P-01 không quy định sắp xếp theo cột. Phần mềm làm đúng, không phải lỗi. Nếu cần, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### TKTVV_02 — Bộ lọc "Lĩnh vực" có cần hiện sẵn giá trị "Tất cả" không?

**Vấn đề:** Đối tác dẫn thiết kế đòi bộ lọc mặc định là "Tất cả"; thực tế ô lọc để trống.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* ô lọc mặc định trống (chữ mờ "Lĩnh vực"), là ô chọn nhiều.
- *SRS:* chỉ nói "ô chọn nhiều", không quy định giá trị mặc định (`srs-fr-04:1432`, `:230`). Về logic, để trống = không lọc = trả về tất cả — nhưng muốn quay về "tất cả" thì phải bỏ chọn từng option đã chọn, **tốn thao tác**.
- *Ai đúng:* thiết kế đòi "Tất cả" là hợp lý về thao tác; phần mềm để trống tuy cùng kết quả nhưng bất tiện khi muốn xóa lựa chọn.

**Giải pháp:** **BA đã chốt 15/07/2026 — thêm tùy chọn "Tất cả".** Bổ sung một mục **"Tất cả"** trong danh sách lọc. Với ô chọn nhiều: **chọn "Tất cả" → tự bỏ chọn mọi option lẻ; chọn một option lẻ → tự bỏ "Tất cả"**. Áp cho **mọi trường chọn nhiều trong bộ lọc toàn hệ thống** (xem Mục tổng hợp B.6). Gộp vào `BUG-TKTVV_02`. Owner Dev FE.

### DKTGMLTVV_02 — Trường "Loại" của TVV: 2 giá trị hay 3?

**Vấn đề:** Đối tác dẫn thiết kế đòi 3 giá trị (Tư vấn viên / Chuyên gia / Người hỗ trợ); phần mềm có 2 (Tư vấn viên / Chuyên gia).

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* trường "Loại" có 2 giá trị TVV / CG.
- *SRS:* đúng 2 giá trị này (`srs-fr-04:1483`, `:252`). "Người hỗ trợ pháp lý" là **đối tượng riêng**, đã có FR và màn hình riêng (FR-IV-NHT-01/02/03, `:1199`). BA đã chốt 03/05/2026.
- *Ai đúng:* theo thứ bậc SRS/BA duyệt cao hơn bản thiết kế, phần mềm đúng.

**Giải pháp:** **Không phải lỗi — BA chốt giữ 2 giá trị (15/07/2026).** Giữ 2 giá trị TVV / CG; đề nghị sửa lại bản thiết kế HTPLDN-041 cho khớp SRS.

**Phản hồi cho KTĐL:** "Người hỗ trợ pháp lý" không phải một giá trị của trường "Loại", mà là một đối tượng riêng đã có FR và màn hình riêng trong SRS (BA chốt 03/05/2026). Trường "Loại" đúng 2 giá trị TVV / CG.

### QLHSTVV_02 — Thẻ giới thiệu đầu trang TVV có thêm 3 trường không?

**Vấn đề:** Thẻ giới thiệu đầu trang màn Chi tiết TVV thiếu Loại / Tổ chức tư vấn / Lĩnh vực pháp luật.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* thẻ đầu trang có Ảnh, Họ tên, Mã TVV, Trạng thái, điểm đánh giá, Ngày công nhận; không có 3 trường kia (đã loại trừ khả năng thiếu dữ liệu).
- *SRS:* thẻ đầu trang đúng các trường trên, không nêu 3 trường này (`srs-fr-04:1541`). SRS đặt 3 trường đó ở thẻ "Hồ sơ" bên dưới (`:1554`).
- *Ai đúng:* phần mềm đúng SRS; đối tác kỳ vọng theo bố cục thiết kế.

**Giải pháp:** **Không phải lỗi — phần mềm đúng SRS (BA xác nhận 15/07/2026).** Thẻ đầu trang hiển thị đúng các trường SRS quy định; 3 trường Loại / Tổ chức tư vấn / Lĩnh vực pháp luật được SRS đặt ở thẻ "Hồ sơ" bên dưới. Nếu muốn đưa lên thẻ đầu trang, đề nghị liệt kê vào danh sách yêu cầu cải tiến. **Riêng một việc khác:** trường "Loại" vẫn phải hiện trong thẻ "Hồ sơ" theo `:1554` → giữ `BUG-QLTVV_04` (Open).

**Phản hồi cho KTĐL:** Theo SRS (SCR-IV-03), thẻ giới thiệu đầu trang gồm Ảnh, Họ tên, Mã TVV, Trạng thái, điểm đánh giá, Ngày công nhận; 3 trường Loại / Tổ chức tư vấn / Lĩnh vực pháp luật được đặt ở thẻ "Hồ sơ" bên dưới, không phải ở thẻ đầu trang. Phần mềm hiển thị đúng đặc tả, không phải lỗi. Nếu muốn đưa 3 trường lên thẻ đầu trang, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### QLHSTVV_04 — Bấm "Quay lại danh sách" bị mất bộ lọc đang áp

**Vấn đề:** Cán bộ lọc ra một hồ sơ, mở chi tiết rồi bấm "Quay lại", thì mất hết bộ lọc.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* bấm "Quay lại" là mất điều kiện lọc (thẻ về mặc định "Đang hoạt động", ô tìm kiếm rỗng, danh sách khác đi).
- *SRS:* nút Quay lại chỉ được quy định về điều hướng; không nơi nào yêu cầu ghi nhớ bộ lọc (`srs-fr-04:1540`, `:1452-1459`).
- *Ai đúng:* đối tác đúng, đây là khoảng trống của SRS.

**Giải pháp:** **BA đã đồng ý 15/07/2026 — giữ bộ lọc khi quay lại danh sách.** Phạm vi giữ: thẻ trạng thái + từ khóa + bộ lọc nâng cao + số trang. Áp chung cho mọi màn danh sách (TVV, Tổ chức tư vấn, Người hỗ trợ, Vụ việc) — quy ước chung tại Mục tổng hợp B.4. Owner Dev FE.

### QLHSTVV_06 — Thẻ "Lịch sử hỗ trợ" / "Đánh giá" có hiện số đếm cạnh tên thẻ không?

**Vấn đề:** Đối tác dẫn thiết kế muốn có số đếm cạnh tên thẻ (kiểu "Đánh giá (2)").

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* số liệu hiện **bên trong** thẻ (ví dụ "1 đánh giá"), không hiện cạnh tên thẻ.
- *SRS:* để số liệu bên trong thẻ, không nêu số đếm cạnh tên thẻ (`srs-fr-04:1567`, `:1570`).
- *Ai đúng:* phần mềm đúng SRS.

**Giải pháp:** **BA đã đồng ý bổ sung 15/07/2026 — sửa cho đồng nhất với hệ thống.** Bổ sung số đếm cạnh tên thẻ (kiểu "Đánh giá (2)"); dữ liệu đã có sẵn. Owner Dev FE.

### TDHSTVV_09 — Lưu nháp thẩm định lúc mất mạng không báo lỗi

**Vấn đề:** Cán bộ bấm "Lưu nháp" kết quả thẩm định khi mất mạng, không có thông báo lỗi.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* bấm "Lưu nháp" thì không báo gì, nút quay vòng (spinner) **mãi không dừng**, và việc lưu thực ra đã hỏng. Hệ thống **nuốt lỗi trong im lặng** — cán bộ tưởng đã lưu nhưng bản nháp hỏng.
- *SRS:* module TVV chỉ liệt kê 3 lỗi nghiệp vụ, không có lỗi mất kết nối (`srs-fr-04:539-541`). Nhưng module Vụ việc đã có quy ước cho tình huống này ("Lưu thất bại, vui lòng kiểm tra kết nối và thử lại" + nút Thử lại, `srs-fr-05:1567`, `:1574`).
- *Ai đúng:* đối tác đúng về thực tế; chỉ là đặc tả module IV còn thiếu.

**Giải pháp:** **BA đã đồng ý 15/07/2026 — sửa cho đồng nhất với hệ thống.** Nâng quy ước báo lỗi mất kết nối ở module Vụ việc (`srs-fr-05:1567`, `:1574`) thành **quy ước chung** áp cho mọi module (Mục tổng hợp B.2). Ngoài thêm thông báo lỗi, phải dừng spinner + có nút Thử lại (nút quay vòng mãi hiện nay gây nguy cơ mất trắng dữ liệu). Cùng gốc với `BUG-TDHSTVV_08`. Owner Dev FE.

### TDHSTVV_18 — Trình duyệt cấp Địa phương: hồ sơ có tự lên cấp Bộ/Ngành không?

**Vấn đề:** Cán bộ Địa phương thẩm định Đạt rồi "Trình duyệt"; đối tác mong hồ sơ tự chuyển lên cấp Bộ/Ngành.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* hồ sơ chuyển "Chờ phê duyệt" nhưng **giữ nguyên cấp Địa phương**; cán bộ Phê duyệt cùng đơn vị thấy trong hàng chờ.
- *SRS:* thẩm định và phê duyệt cùng cấp, **không xuyên cấp**, và đã **bỏ cơ chế tự chuyển lên cấp trên** từ v3.5 (`srs-fr-04:80`, `:518`, `:570`; căn cứ NĐ121/2025 Đ.39-40 và NĐ55/2019 Đ.9).
- *Ai đúng:* phần mềm đúng SRS; kỳ vọng đối tác viết theo bản SRS cũ.

**Giải pháp:** **Không phải lỗi.** Sửa "Kết quả mong đợi" (bỏ ý "tự lên cấp Bộ/Ngành").
*(Hai ý khác — không có thông báo thành công, và cán bộ Phê duyệt cùng đơn vị không nhận thông báo — đều có thật, đã log riêng `BUG-TDHSTVV_18`.)*

**Phản hồi cho KTĐL:** Việc hồ sơ không tự chuyển lên cấp Bộ/Ngành là **đúng thiết kế hiện hành**, không phải lỗi. Kỳ vọng "tự chuyển lên cấp trên" là theo bản SRS v3 cũ; từ v3.5, cơ chế chuyển cấp bắt buộc (ESCALATE) đã được bỏ theo NĐ121/2025 Đ.39-40 và NĐ55/2019 Đ.9. Cơ sở: mỗi cấp — Địa phương (UBND cấp tỉnh), Bộ ngành, Trung ương (Bộ Tư pháp) — tự công bố mạng lưới TVV trong phạm vi phân cấp của mình, không đẩy hồ sơ xuyên cấp. Do đó cán bộ Địa phương thẩm định Đạt thì hồ sơ ở lại cấp Địa phương để cán bộ Phê duyệt cùng cấp xử lý — đúng quy định.

### PDHSTVV_06 — Sau khi duyệt, hồ sơ TVV chuyển "Chờ kích hoạt" hay "Đang hoạt động"?

**Vấn đề:** Đối tác mong sau duyệt là "Đang hoạt động" + thông báo "Đã công nhận tư vấn viên"; phần mềm chuyển "Chờ kích hoạt tài khoản" + gửi mail kích hoạt.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* sau duyệt → "Chờ kích hoạt tài khoản", tự cấp tài khoản, gửi mail kích hoạt.
- *SRS tự mâu thuẫn:* phần đặc tả xử lý ghi "Chờ kích hoạt" (`srs-fr-04:591`, `:619-620`); nhưng phần mô tả màn hình lại ghi "Đang hoạt động" (`:1545`, `:1582`). Changelog xác nhận đã sửa sang cơ chế "Chờ kích hoạt" — vậy 2 dòng "Đang hoạt động" là câu chữ sót của bản cũ.
- *Ai đúng:* phần mềm đúng ý định mới; SRS có chỗ sót cần dọn.

**Giải pháp:** **Dọn SRS.**
- *Trạng thái:* giữ "Chờ kích hoạt tài khoản", **sửa 2 dòng SRS `:1545` và `:1582`** cho khớp.
- *Nội dung mail:* SRS chỉ yêu cầu gửi cho chủ hồ sơ (phần mềm đang đúng). Đề nghị **thêm mã số TVV** vào nội dung mail. Chỉ gửi chủ hồ sơ — PDHSTVV_08 đã chốt không thêm người nhận.
- *Câu chữ thông báo:* đề nghị dùng "Đã công nhận tư vấn viên" cho khớp tài liệu bàn giao.

**Phản hồi cho KTĐL:** Sau khi phê duyệt, hồ sơ chuyển "Chờ kích hoạt tài khoản" là **đúng cơ chế thiết kế**: hệ thống tự tạo tài khoản cho TVV và gửi mail kích hoạt; TVV kích hoạt xong mới sang "Đang hoạt động". Hai dòng mô tả màn hình trong SRS còn ghi "Đang hoạt động" là câu chữ sót của bản cũ, đang được dọn cho thống nhất (phần đặc tả xử lý đã ghi đúng "Chờ kích hoạt"). Vì vậy hành vi phần mềm là đúng về ý định thiết kế. Riêng câu chữ thông báo, hệ thống sẽ dùng "Đã công nhận tư vấn viên" cho khớp tài liệu bàn giao và bổ sung mã số TVV vào nội dung mail.

### PDHSTVV_08 — Cán bộ đã thẩm định có được báo kết quả duyệt/từ chối không?

**Vấn đề:** Hồ sơ TVV bị duyệt hoặc từ chối, cán bộ đã thẩm định không nhận được thông báo.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* cán bộ thẩm định không nhận thông báo khi hồ sơ bị từ chối.
- *SRS:* chỉ yêu cầu báo cho chủ hồ sơ, im lặng về cán bộ thẩm định (`srs-fr-04:593`, `:627`, `:1398`). (Chiều ngược lại thì SRS có: trình duyệt thì báo cán bộ phê duyệt, `:518`.)
- *Ai đúng:* phần mềm đúng SRS — SRS không yêu cầu báo cho cán bộ thẩm định ở chiều này. *(Ý chính — chủ hồ sơ không nhận thông báo từ chối — đã log riêng `BUG-PDHSTVV_08`.)*

**Giải pháp:** **Không phải lỗi — phần mềm đúng SRS.** SRS chỉ yêu cầu báo cho chủ hồ sơ khi duyệt/từ chối (`srs-fr-04:593`, `:627`), không quy định báo cho cán bộ nghiệp vụ đã thẩm định. Việc CB NV không nhận thông báo là đúng đặc tả. Nếu muốn bổ sung báo cho CB NV thì liệt kê vào danh sách yêu cầu cải tiến.

**Phản hồi cho KTĐL:** Theo SRS (FR-IV-07), khi hồ sơ TVV được duyệt hoặc từ chối, hệ thống báo cho **chủ hồ sơ** (ứng viên TVV); SRS không quy định báo cho cán bộ nghiệp vụ đã thẩm định. Vì vậy việc cán bộ thẩm định không nhận thông báo ở chiều này là **đúng đặc tả, không phải lỗi**. Nếu cần bổ sung báo cho cán bộ thẩm định, đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### PDHSTVV_09 — Số quyết định công nhận TVV có bắt buộc không được trùng không?

**Vấn đề:** Nhập trùng số quyết định vẫn duyệt được; đối tác mong báo lỗi trùng.

**Hiện trạng phần mềm — SRS:**
- *Thực tế nghiệp vụ:* một quyết định thường công nhận nhiều tư vấn viên cùng lúc (một QĐ kèm danh sách), nên trùng số QĐ là bình thường.
- *Phần mềm:* cho phép nhiều hồ sơ cùng một số QĐ.
- *SRS:* số QĐ chỉ ràng buộc định dạng, **cố ý không** bắt duy nhất (`srs-fr-04:2025`). Các trường cần duy nhất khác đều được ghi rõ kèm mã lỗi (CCCD, email), số QĐ thì không.
- *Ai đúng:* phần mềm đúng SRS.

**Giải pháp:** **Không phải lỗi.** Giữ nguyên, sửa test case. Nếu chị muốn kiểm soát trùng thì dùng cảnh báo mềm (không chặn), hoặc chỉ bắt duy nhất theo cụm (số QĐ + đơn vị + ngày ký).

**Phản hồi cho KTĐL:** Một quyết định công nhận thường kèm danh sách nhiều tư vấn viên, nên nhiều hồ sơ mang cùng một số QĐ là đúng nghiệp vụ. SRS cố ý không đặt ràng buộc "không trùng" cho trường này (khác các trường CCCD / email vốn có ràng buộc duy nhất và mã lỗi riêng). Phần mềm đúng, không phải lỗi. Nếu là nhu cầu thật (muốn kiểm soát trùng số QĐ), đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### CNDSMLTVV_05 — Công khai TVV lên Cổng PLQG theo mô hình ĐẨY hay KÉO? *(gấp nhất)*

**Vấn đề:** Bấm công khai một TVV lên Cổng PLQG thì báo "Không thể công khai, vui lòng thử lại" — chức năng công khai chết trên cả hai môi trường.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* khi công khai, backend gọi thẳng sang Cổng; lời gọi thất bại thì trả **502 mã `ERR-SYS-IV-CK-02` "Lỗi kết nối Cổng PLQG khi công khai"** → **hủy bỏ (rollback)**, không đặt được cờ công khai. Đây là mô hình ĐẨY.
- *SRS:* chốt mô hình **KÉO**, nhắc lại tới 4 chỗ — phần mềm chỉ đặt cờ và đổi trạng thái, Cổng tự kéo dữ liệu định kỳ, phần mềm **không** gọi sang Cổng (`srs-fr-04:638`, `:657`, `:682-683`, `:1457`).
- *Mã lỗi code trả KHÔNG có trong SRS:* §Error Handling của FR-IV-08 (`srs-fr-04:674-675`) chỉ có 2 mã lỗi nghiệp vụ — `ERR-CK-01` (trạng thái không hợp lệ) và `ERR-CK-02` (thiếu mô tả công khai). Mã `ERR-SYS-IV-CK-02` mà code đang trả **không tồn tại trong toàn bộ SRS**. Đây là logic sạch: SRS quy định KÉO → phần mềm không gọi ra Cổng → không thể có "lỗi kết nối Cổng khi công khai" → nên SRS cố ý không có mã lỗi đó. Việc code **tự sinh** mã lỗi này chính là **bằng chứng code đang làm ĐẨY**, lệch mô hình KÉO. *(Đối chiếu: module có gọi API thật như Biểu mẫu FR-IX / TV nhanh FR-XIII đều có mã `ERR-CK-API-01/02` — `srs-v3.5.md:6639`, `:6641`; riêng TVV FR-IV-08 cố ý không có.)*
- *Ai đúng:* SRS chốt KÉO; cả phần mềm lẫn kỳ vọng đối tác đều đang theo ĐẨY. Đây không chỉ là lỗi lẻ của màn TVV mà là **lệch chuẩn tích hợp chung** — BR-API-01 (`srs-v3.5.md:5544`) quy định toàn Nhóm XII dùng KÉO (Cổng/consumer chủ động pull), code TVV lại ĐẨY. Nghi vấn: quyết định KÉO chưa được truyền tới Dev, hoặc BA đã đổi lại ĐẨY mà chưa cập nhật SRS.

**Giải pháp:** **BA đã chốt mô hình KÉO — Chuyển Dev (16/07/2026).** Dev **bỏ lời gọi sang Cổng** khỏi thao tác công khai; công khai chỉ đặt cờ `cong_khai` + đổi trạng thái, **luôn thành công** khi đủ điều kiện (Cổng sập cũng không chặn); Cổng PLQG tự kéo dữ liệu định kỳ. Bỏ mã lỗi `ERR-SYS-IV-CK-02` (không có trong SRS). Đây là hướng fix `BUG-CNDSMLTVV_05`, đồng bộ với chuẩn KÉO chung của Nhóm XII (BR-API-01). Sửa Expected test case (bỏ "đẩy", bỏ "Cổng tiếp nhận trong lần gọi đầu tiên"). Owner Dev BE + FE.

### DGTVV_03 — Danh sách đánh giá có cần cột "Điểm tổng" không?

**Vấn đề:** Danh sách đánh giá TVV thiếu cột "Điểm tổng".

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* danh sách có 7 cột (Người đánh giá, Vụ việc, Ngày, 3 điểm thành phần, Nhận xét); form gửi đánh giá thì có hiện "Điểm tổng (tính tự động)".
- *SRS:* liệt kê đúng 7 thành phần, không có "Điểm tổng" (`srs-fr-04:1570`). Nhưng điểm tổng vẫn được tính và lưu sẵn (`:706`, `:726`).
- *Ai đúng:* phần mềm đúng SRS.

**Giải pháp:** **Không phải lỗi — phần mềm đúng SRS.** Danh sách hiển thị đúng 7 thành phần SRS quy định, không có cột "Điểm tổng". Nếu có nhu cầu thật (thêm cột Điểm tổng), đề nghị liệt kê vào danh sách yêu cầu cải tiến.

**Phản hồi cho KTĐL:** Theo SRS (SCR-IV-03, `srs-fr-04:1570`), danh sách đánh giá gồm 7 cột: Người đánh giá, Vụ việc, Ngày, 3 điểm thành phần, Nhận xét — không có cột "Điểm tổng". Phần mềm hiển thị đúng đặc tả, không phải lỗi. Nếu muốn thêm cột "Điểm tổng" (dữ liệu đã có sẵn), đề nghị liệt kê vào danh sách yêu cầu cải tiến.

### DGTVV_05 — Trường "Vụ việc liên kết" khi gửi đánh giá: bắt buộc hay tùy chọn?

**Vấn đề:** Bỏ trống "Vụ việc liên kết" không báo lỗi, đối tác cho rằng nó phải là trường bắt buộc.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* gửi form trống thì chặn và báo lỗi đúng 3 trường bắt buộc (3 điểm thành phần); "Vụ việc liên kết" không có dấu sao, không báo lỗi. Tức phần mềm **đã** đáp ứng Expected ("có báo lỗi").
- *SRS:* "Vụ việc liên kết" là **không bắt buộc** (`srs-fr-04:702`, `:1573`).
- *Ai đúng:* phần mềm đúng SRS.

**Giải pháp:** **Không phải lỗi.** Giữ tùy chọn (đánh giá TVV có thể phát sinh ngoài một vụ việc cụ thể — ví dụ đánh giá định kỳ). Sửa "Kết quả thực tế" của test case.

**Phản hồi cho KTĐL:** "Vụ việc liên kết" là trường tùy chọn theo SRS, vì đánh giá có thể là đánh giá định kỳ không gắn với vụ việc nào. Lưu ý thêm: dropdown này hiện đang rỗng với mọi TVV, nên nếu ép bắt buộc thì chức năng gửi đánh giá sẽ chết hoàn toàn. Phần mềm đúng, đề nghị cập nhật lại Expected.

---

## Nhóm 3 — Module Vụ việc HTPL (FR-V.I)

### QLTNVV_02 — Tên cột viết tắt và badge cảnh báo quá hạn khó nhìn

**Vấn đề:** Tên cột trên danh sách vụ việc bị viết tắt, và badge cảnh báo quá hạn nhấp nháy / chữ chìm vào nền khó đọc. *(Phần chính của case là Open — 2 cột thời hạn sai nhãn, đã log `BUG-QLTNVV_02`. Đây là 2 đề nghị thêm.)*

**Hiện trạng phần mềm — SRS:**
- *Ý 1 — tên cột viết tắt ("Mã VV", "Tên DN", "Lĩnh vực PL"):* SRS quy định đúng các nhãn viết tắt này (`srs-fr-05:1630-1632`), nên phần mềm làm đúng. Nếu muốn viết đầy đủ thì đây là yêu cầu mới.
- *Ý 2 — badge quá hạn:* video đối tác cho thấy badge mờ, tương phản kém (QA chưa quan sát trực tiếp vì môi trường chưa có bản ghi quá hạn). Quy ước UI-05 yêu cầu tương phản đủ theo chuẩn WCAG (`srs-v3.5.md:572`) → chữ chìm nền là vi phạm; riêng hiệu ứng nhấp nháy thì SRS chưa cấm.

**Giải pháp:**
- *Ý 1:* **BA đã đồng ý 16/07/2026 — viết đầy đủ tên cột, bỏ viết tắt.** Đổi "Mã VV" → "Mã vụ việc", "Tên DN" → "Tên doanh nghiệp", "Lĩnh vực PL" → "Lĩnh vực pháp luật"… Sửa SRS một lần cho cả 5 màn SCR-V.I-01…05 (`srs-fr-05:1630-1632`), làm cùng lúc với đổi nhãn "Deadline SLA" ở KTHSYCHTPL_04. Owner BA sửa SRS → Dev FE.
- *Ý 2:* **Chuyển Dev** (phần tương phản, verdict đổi sang **Open**) và bổ sung vào quy ước giao diện chung: "không dùng hiệu ứng nhấp nháy cho nhãn cảnh báo; badge quá hạn phải đạt tương phản tối thiểu WCAG AA 4.5:1".

### QLTNVV_06 — File Excel xuất ra sai tên cột và dư cột *(đã chốt 12/07/2026)*

**Vấn đề:** File Excel xuất từ danh sách vụ việc lệch tên cột so với màn hình và có cột thừa.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* file Excel dư 2 cột "Tiêu đề" và "Ưu tiên".
- *SRS:* tập cột đúng là 9 cột dữ liệu của SCR-V.I-01 (`srs-fr-05:1630-1638`).

**Giải pháp:** **Chuyển Dev (đã chốt).** Nguyên tắc: màn hình hiện cột nào thì Excel có đúng cột đó với đúng tên đó → **bỏ** 2 cột thừa; cột chọn (checkbox) và cột "Hành động" không xuất. Đã log `BUG-QLTNVV_06`. Thứ tự làm: sửa nhãn cột trên màn hình trước (`BUG-QLTNVV_02`), rồi mới đồng bộ Excel. *Kèm SRS:* bổ sung một mục quy định cột xuất Excel vào FR-V.I-01 (theo mẫu module TVV, `srs-fr-04:243`).

### NHSYC_02 — Form "Nhập thủ công" hồ sơ vụ việc: 8 ý

**Vấn đề:** Cán bộ nhập tay hồ sơ vụ việc mà DN gửi qua đường trực tiếp / điện thoại / bưu chính. *(Phần chính của case là Open — thiếu trường "Ngày tiếp nhận", đã log `BUG-NHSYC_02`. 8 ý dưới không phải lỗi Dev.)*

**Hiện trạng phần mềm — SRS — Giải pháp từng ý:**

- **Ý 1 — nhóm "Thông tin DN": nhập thẳng 13 trường hay mở hộp thoại 2 trường?** *SRS tự mâu thuẫn:* mô tả màn hình liệt kê 13 trường nhập thẳng (`srs-fr-05:1666-1678`), nhưng quyết định BA 30/05/2026 lại chốt mở hộp thoại tạo DN chỉ 2 trường bắt buộc (mã số thuế + tên DN), 15 trường còn lại tùy chọn (`:312`, `:1668`). Phần mềm làm đúng quyết định BA. → **Dọn SRS (BA đồng ý 16/07/2026):** xóa 13 dòng nhập thẳng `:1666-1678`.
- **Ý 2 — "Kênh tiếp nhận": 3 hay 5 giá trị?** *SRS tự mâu thuẫn:* phần đặc tả ghi 3 giá trị (`:319`), mô tả màn hình ghi 5 giá trị (`:1690`). Phần mềm làm 3. → **Dọn SRS (BA đồng ý 16/07/2026):** giữ 3 giá trị, sửa `:1690`. Lý do: "Dịch vụ công" và "Hệ thống khác" là kênh tự động (hệ thống đẩy sang), cán bộ không thể tự nhập tay một hồ sơ rồi khai nó đến từ Dịch vụ công.
- **Ý 3 — danh mục "Loại hình hỗ trợ" (thiết kế 4, web 6):** không phải lỗi Dev — đây là **danh mục cấu hình được** (FK → DANH_MUC, `:315`, `:1683`), giá trị hiển thị do cấu hình chứ không cứng trong code. → **Phản hồi KTĐL:** danh mục này cấu hình được qua chức năng quản trị danh mục; đơn vị vận hành tự cấu hình giá trị theo nhu cầu, không phải lỗi phần mềm. BA sẽ ban hành danh mục chuẩn để nạp.
- **Ý 4 — danh mục "Lĩnh vực pháp lý" (thiết kế 8, web 10, thiếu "Khác"):** như ý 3 — danh mục cấu hình được (`:316`, `:1682`). → **Phản hồi KTĐL:** tương tự ý 3 — tự cấu hình qua quản trị danh mục, không phải lỗi. BA ban hành danh mục chuẩn (và chốt có giá trị "Khác" hay không).
- **Ý 5 — gộp "Nội dung yêu cầu" và "Vướng mắc" thành 1?** Đây là 2 trường riêng, ý nghĩa khác nhau (`:317-318`, `:1681`, `:1684`) → **giữ nguyên SRS, không gộp — phần mềm đúng.** → **Phản hồi KTĐL:** "Nội dung yêu cầu" (yêu cầu DN đưa ra) và "Vướng mắc" (vướng mắc pháp lý cụ thể) là 2 trường riêng theo SRS, ý nghĩa khác nhau; phần mềm hiển thị đúng đặc tả, không phải lỗi.
- **Ý 6 — thêm trường "Thời điểm phát sinh"?** SRS chưa có → **nếu có nhu cầu thật thì liệt kê vào danh sách yêu cầu cải tiến, nêu rõ mục đích sử dụng** (dùng để làm gì — lưu ý không dùng để tính thời hạn, thời hạn tính từ ngày tiếp nhận `:338`).
- **Ý 7 — thêm trường "Hướng dẫn hồ sơ cần nộp"?** SRS chưa có, và **đối tác chưa nêu yêu cầu cụ thể** (chỉ ghi "thiếu", không rõ nội dung / tĩnh hay động / ai nhập). → Cần đối tác **làm rõ yêu cầu**; nếu có nhu cầu thật thì liệt kê vào danh sách yêu cầu cải tiến kèm mô tả cụ thể.
- **Ý 8 — thêm ô "Ghi chú tiếp nhận" riêng ở nhóm 4?** SRS đã có 1 ô ghi chú ở nhóm 2 (`:1685`) → **giữ nguyên SRS, không thêm — phần mềm đúng.** → **Phản hồi KTĐL:** form đã có ô "Ghi chú" (nhóm 2) dùng chung; thêm ô "Ghi chú tiếp nhận" riêng ở nhóm 4 là trùng lặp, không cần. Không phải lỗi.

### NHSYC_06 — Danh sách định dạng tệp đính kèm hợp lệ

**Vấn đề:** Danh sách định dạng tệp đính kèm không đúng thiết kế. *(Phần chính của case là Open — vượt 10 tệp và vượt 100MB không báo lỗi, đã log `BUG-NHSYC_06`. Đây là phần danh sách định dạng.)*

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* nhận .doc / .docx / .xls / .xlsx / .pdf / .jpg / .png / **.gif**.
- *SRS ghi 3 danh sách khác nhau ở 3 chỗ:* `:320` = PDF/DOC/DOCX/JPG/PNG; `:1687` = doc/docx/xls/xlsx/pdf; `:180` = PDF/DOC/DOCX/XLS/XLSX. Phần mềm lấy hợp của cả 3 rồi thêm cả `.gif` (không có ở dòng SRS nào).
- *Ai đúng:* không có "đáp án đúng" để chấm Dev, vì bản thân SRS đã lệch nhau 3 chỗ.

**Giải pháp:** **Dọn SRS (BA đồng ý 16/07/2026).** Chốt **một** danh sách: **PDF · DOC · DOCX · XLS · XLSX** (tài liệu) và **JPG · PNG** (ảnh chụp giấy tờ) — **bỏ `.gif`** (ảnh động không phải tài liệu pháp lý). Đồng bộ cả 3 dòng SRS (`:180`, `:320`, `:1687`). Ngoài ra: trần **tổng 100MB** hiện không hiện trên màn hình → phải hiển thị, vì người dùng không thể tuân theo giới hạn họ không được biết.

### NHSYC_07 — "Lưu nháp": có bắt nhập đủ trường không, và lưu xong ở lại form hay chuyển trang?

**Vấn đề:** Cán bộ đang nhập dở một vụ việc thì bấm "Lưu nháp".

**Hiện trạng phần mềm — SRS:**
- *Ý 1 — lưu nháp có bắt nhập đủ trường không:* phần mềm vẫn bắt đủ 5 trường bắt buộc như khi lưu chính thức. SRS chưa quy định lưu nháp có kiểm tra hay không.
- *Ý 2 — lưu xong ở lại form hay chuyển trang:* phần mềm hiện thông báo "Đã lưu nháp" rồi chuyển sang trang chi tiết. SRS yêu cầu đúng như vậy — chuyển sang trang chi tiết (`:342`). *(2/3 ý Expected đã đạt: sinh mã đúng quy tắc, lưu trạng thái "Mới tạo".)*

**Giải pháp:**
- *Ý 1:* **Giữ nguyên hành vi hiện tại — không phải lỗi.** SRS không quy định lưu nháp phải nới lỏng kiểm tra; phần mềm vẫn kiểm tra các trường bắt buộc là chấp nhận được. Nếu muốn lưu nháp chỉ cần vài trường định danh thì đề nghị liệt kê vào danh sách yêu cầu cải tiến.
- *Ý 2:* **Không phải lỗi — phần mềm đúng SRS** (chuyển trang chi tiết, `:342`).

**Phản hồi cho KTĐL (ý 1):** Khi bấm "Lưu nháp", phần mềm vẫn kiểm tra các trường bắt buộc — đây là thiết kế hiện hành, SRS không quy định khác, không phải lỗi. Nếu muốn nới lỏng để lưu nháp chỉ cần vài trường định danh, đề nghị liệt kê vào danh sách yêu cầu cải tiến.
**Phản hồi cho KTĐL (ý 2):** Sau khi lưu nháp, phần mềm chuyển sang trang chi tiết vụ việc — đúng SRS (`srs-fr-05:342`). Kỳ vọng "ở lại form" là trái đặc tả; phần mềm đúng ở ý này.

### NHSYC_08 — Bấm "Hủy" khi đang nhập dở có hỏi xác nhận không?

**Vấn đề:** Cán bộ nhập dở form vụ việc (dài 4 nhóm) rồi bấm "Hủy", hệ thống chuyển thẳng về danh sách, không hỏi gì, dữ liệu mất luôn.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* bấm "Hủy" là về danh sách ngay, không có hộp thoại xác nhận.
- *SRS:* im lặng ở module Vụ việc (`:1695`, `:1571-1580` chỉ hỏi xác nhận khi Xóa). Nhưng hai module đang làm khác nhau: module Tư vấn viên **có** hộp thoại xác nhận ("Ở lại"), module Vụ việc **không**.
- *Ai đúng:* đối tác đúng về rủi ro; điểm quan trọng là hai module cùng sản phẩm lại hành xử khác nhau ở cùng một thao tác.

**Giải pháp:** **BA đã đồng ý 16/07/2026 — sửa cho đồng nhất trong phần mềm.** Bổ sung hộp thoại xác nhận khi rời form còn dữ liệu chưa lưu; chuẩn hóa thành **quy ước chung** trong SRS (cạnh UI-04, Mục tổng hợp B.3), áp mọi module — xóa sự lệch giữa module Tư vấn viên (đã có) và Vụ việc (chưa có). Owner Dev FE.

### KTHSYCHTPL_04 — Nhãn trường thời hạn đang là tiếng Anh ("Deadline")

**Vấn đề:** Trên màn Chi tiết vụ việc, trường thời hạn xử lý đang hiển thị bằng tiếng Anh.

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* nhãn thật là "Deadline" — nhãn tiếng Anh duy nhất trong nhóm (6 nhãn còn lại đều tiếng Việt).
- *SRS:* quy ước UI-06 ghi "tiếng Việt là ngôn ngữ duy nhất", không ngoại lệ (`srs-v3.5.md:573`); cùng chiều với các chỗ khác dùng "Thời hạn xử lý".
- *Ai đúng:* đối tác đúng — "Deadline" vi phạm UI-06.

**Giải pháp:** **BA đã đồng ý 16/07/2026 — sửa SRS rồi chuyển Dev.** Đổi "Deadline" thành "Thời hạn xử lý". **Đồng thời sửa SRS `srs-fr-05:1637-1638`** ("Deadline SLA" → "Thời hạn xử lý", "Cảnh báo SLA" → "Cảnh báo thời hạn") để áp thống nhất cả màn danh sách lẫn màn chi tiết — nếu không, `BUG-QLTNVV_02` sẽ kéo Dev về hướng ngược lại làm 2 màn lệch nhau. (Verdict đổi sang **Open**.)

### KTHSYCHTPL_11 — Kết luận "Đạt" là chuyển ngay "Đã phân công", hay phải chọn người xử lý mới chuyển?

**Vấn đề:** Cán bộ kiểm tra hồ sơ vụ việc, kết luận Đạt. Câu hỏi: chuyển ngay sang "Đã phân công", hay phải chọn được người xử lý rồi mới chuyển? *(Phần chính của case — không ghi người/ngày kiểm tra — đã log `BUG-KTHSYCHTPL_11`.)*

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* kết luận Đạt thì vụ việc sang "Đang kiểm tra" và báo "sẵn sàng phân công"; phải bấm [Phân công] chọn người xử lý thì mới sang "Đã phân công".
- *SRS tự mâu thuẫn:* bảng nút ghi "Đạt → Đã phân công" ngay (`:1736`); bảng chuyển trạng thái lại ghi "Đạt + phải chọn người xử lý" mới chuyển (`:2280`). Phần mềm theo dòng `:2280`.
- *Ai đúng:* phần mềm đúng nghiệp vụ — không thể "Đã phân công" khi chưa có ai được phân công.

**Giải pháp:** **Dọn SRS (BA đồng ý 16/07/2026).** Giữ luồng phần mềm (Đạt + chọn người xử lý mới sang "Đã phân công"), **sửa SRS dòng 1736** cho khớp `:2280`. Gợi ý đổi nhãn nút thành [Kiểm tra lại] cho rõ nghĩa "sửa lại kết quả kiểm tra".

### TKHSYCHTPL_02 — Cán bộ Trung ương xem vụ việc toàn quốc nhưng không có bộ lọc "Đơn vị"

**Vấn đề:** Cán bộ Trung ương thấy lẫn lộn vụ việc của nhiều đơn vị trong một danh sách, nhưng không có bộ lọc theo "Đơn vị".

**Hiện trạng phần mềm — SRS:**
- *Phần mềm:* thanh tìm kiếm có 6 trường (từ khóa, Lĩnh vực PL, Kênh tiếp nhận, Mức SLA, Trạng thái, Từ–Đến ngày), không có "Đơn vị".
- *SRS:* đúng 6 trường này, không có trường lọc theo đơn vị (`srs-fr-05:1622-1628`, `:645-652`). SRS cho Trung ương xem toàn quốc nhưng không cho công cụ lọc theo đơn vị.
- *Ai đúng:* phần mềm không sai theo SRS, nhưng đây là khoảng trống đặc tả.

**Giải pháp:** **BA đã đồng ý 16/07/2026 — bổ sung bộ lọc "Đơn vị", chỉ hiện với cấp Trung ương.** Cho quyền xem toàn quốc mà không cho công cụ lọc là thiết kế chưa trọn; cán bộ Bộ ngành / Địa phương đã bị giới hạn 1 đơn vị nên với họ trường lọc này vô nghĩa. Bổ sung `don_vi_id` vào SCR-V.I-01 (`srs-fr-05:1622-1628`) và FR-V.I-08 §Đầu vào (`:645-652`), chỉ hiển thị cho cấp Trung ương. Owner BA sửa SRS → Dev FE + BE.

---

## Mục tổng hợp — Việc cần làm với SRS

### A. Bốn chỗ SRS tự mâu thuẫn — phải dọn dù BA quyết thế nào

1. `srs-fr-04:1545` và `:1582`: "đặt trạng thái Đang hoạt động" → sửa thành **"Chờ kích hoạt tài khoản"** (khớp phần xử lý `:591`/`:619-620` và Changelog). *(PDHSTVV_06)*
2. `srs-fr-05:1736`: "[Hoàn tất Kiểm tra] Đạt → Đã phân công" → sửa cho khớp `:2280` (Đạt + chọn người xử lý mới chuyển). *(KTHSYCHTPL_11)*
3. `srs-fr-05:1666-1678` (13 trường DN nhập thẳng) và `:1690` (kênh tiếp nhận 5 giá trị) → xóa 13 dòng; sửa `:1690` xuống 3 giá trị. *(NHSYC_02 ý 1-2)*
4. `CHANGELOG-v3-to-v3.5.md:2018` và `srs-fr-03:1876` ("giữ giảng viên bản cũ 11 trường") → xóa ghi chú, lấy entity thật 18 trường có `don_vi_id` làm chuẩn. *(QLGVTG_12 — BA đã đồng ý 15/07/2026)*

### B. Bốn chỗ nên nâng thành quy ước dùng chung

1. Bảng **DG-01…DG-07** (gồm DG-06 sắp xếp mặc định) → chuyển từ mục con lên mục quy ước giao diện chung, cạnh UI-01…UI-07.
2. Quy ước **báo lỗi mất kết nối** (`srs-fr-05:1567`, `:1574`) → nâng thành quy ước chung, áp mọi module. *(TDHSTVV_09)*
3. Quy ước **hỏi xác nhận trước khi rời form còn dữ liệu chưa lưu** → bổ sung cạnh UI-04, áp mọi form. *(NHSYC_08)*
4. Quy ước **giữ bộ lọc khi quay lại danh sách từ màn chi tiết** → bổ sung cạnh UI-04, áp mọi màn danh sách. *(QLHSTVV_04)*
5. Quy ước **định dạng số điện thoại chung** → "bắt đầu bằng số 0; 10 chữ số (di động) hoặc 11 chữ số (cố định)", quy tắc `^0\d{9,10}$`; áp cho mọi field SĐT: giảng viên (`srs-fr-03:965`), TVV/NHT (`srs-fr-04:297`…), hỏi đáp (`srs-fr-02:1064`), API (`srs-fr-16:1155`). Giữ độ dài "10-11" cũ (vốn đúng luật), **bổ sung ràng buộc "bắt đầu bằng số 0"**. *(QLGVTG_05 — BA chốt siết cả hệ thống 15/07/2026; căn cứ Quy hoạch kho số viễn thông, chuyển đổi 11→10 số di động hoàn tất 2018-2019)*
6. Quy ước **tùy chọn "Tất cả" cho ô lọc chọn nhiều** → mọi trường lọc dạng chọn nhiều (multi-select) có một mục **"Tất cả"**; chọn "Tất cả" → tự bỏ chọn các option lẻ, chọn một option lẻ → tự bỏ "Tất cả". Giúp người dùng xóa nhanh lựa chọn mà không phải bỏ chọn từng cái. Áp cho mọi bộ lọc chọn nhiều toàn hệ thống. *(TKTVV_02 — BA chốt 15/07/2026)*

### C. Bổ sung theo quyết định BA (chỉ làm sau khi chị chốt)

| Nếu BA chốt | Sửa ở đâu |
|---|---|
| Báo cho DN khi đề xuất đổi trạng thái | BR-NOTIF-01 `srs-v3.5.md:5520` (thêm 1 sự kiện) + FR-III-13 |
| Báo cho cán bộ thẩm định khi duyệt/từ chối | FR-IV-07 `srs-fr-04:593` + `:627` |
| Nhãn tiếng Việt cho trường thời hạn | `srs-fr-05:1637-1638` |
| Bộ lọc "Đơn vị" cho cán bộ Trung ương | `srs-fr-05:1622-1628` + `:645-652` |
| Danh sách định dạng tệp thống nhất | `srs-fr-05:180`, `:320`, `:1687` |
| Cột "Điểm tổng" ở danh sách đánh giá | `srs-fr-04:1570` |
| Bộ lọc "Lĩnh vực pháp lý" cho kho tài liệu | `srs-fr-03:782-788` |
| Bước xem trước khi import Excel đăng ký | `srs-fr-03:474`, `:485` |
| Nút "Xem" riêng / breadcrumb "Chỉnh sửa" / thẻ đầu trang / thẻ thống kê… | các mục "tùy chị" tương ứng |

### D. Hai danh mục BA cần ban hành (là dữ liệu cấu hình, không giao Dev)

1. Danh mục **"Loại hình hỗ trợ"** (NHSYC_02 ý 3).
2. Danh mục **"Lĩnh vực pháp lý"** — trả lời rõ có giá trị "Khác" hay không (NHSYC_02 ý 4).

### E. Thay đổi verdict so với phiếu hỏi

| Case | Verdict cũ | Verdict mới | Lý do |
|---|---|---|---|
| QLGVTG_06 | BA confirm | **Open** | Vi phạm DG-06 (sắp xếp mặc định dùng chung) |
| QLGVTG_12 | BA confirm | **Open** | Vi phạm BR-AUTH-08 (Trung ương là ngoại lệ toàn quốc) + thiếu cảnh báo WRN-GV-01 |
| KTHSYCHTPL_04 | BA confirm | **Open** | Vi phạm UI-06 (tiếng Việt là ngôn ngữ duy nhất) |
| QLTNVV_02 (ý 2) | BA confirm | **Open** (phần tương phản) | Vi phạm UI-05 (chuẩn tương phản WCAG) |
| QLDXDTTH_06 | BA confirm (chờ phạm vi) | **Open** | Phạm vi giao diện DN đã chốt 02/05/2026 → vi phạm UI-04 |
| CNDSMLTVV_05 | BA confirm | **Open** | SRS chốt mô hình KÉO (4 chỗ); phần mềm làm ĐẨY |
| QLDXDTTH_03 | BA confirm | **Open** | CSV chuẩn (dòng 287-288) có thao tác "DN xem chi tiết"; BA chốt 15/07/2026 bổ sung |
| QLDXDTTH_09 | BA confirm (chờ phạm vi) | **Không phải lỗi** (đúng SRS) | FR-III-13 chỉ quy định báo chiều DN→cán bộ; không báo lại DN là đúng đặc tả. Muốn thêm → yêu cầu cải tiến |

---

*Toàn bộ trích dẫn đối chiếu trực tiếp với file SRS gốc và CSV baseline. Nội dung kết luận đồng nhất với bản gộp nhóm `bao-cao-phan-tich-ba-confirmation-tuan-2.md`.*
