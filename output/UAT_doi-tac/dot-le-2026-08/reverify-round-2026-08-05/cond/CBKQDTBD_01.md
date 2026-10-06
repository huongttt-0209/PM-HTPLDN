# Bảng đối chiếu điều kiện — CBKQDTBD_01 (re-verify vòng 2, 05/08/2026)

Loại bug: **không công bố kết quả cho một phần danh sách học viên được** (nút của từng học viên mờ, ô tích chọn không có tác dụng) → phụ thuộc trạng thái khóa học và trạng thái công bố của từng học viên ⇒ bắt buộc điền bảng đối chiếu, 0 GAP.
Ô note của dòng này (*DEV phản hồi lần 2*) KHÔNG có khối `── CÁCH VERIFY sau Dev fix ──`, nên lấy phần **"Phần còn lỗi"** của note (kèm 2 ý ghi nhận thêm cùng màn hình) làm điều kiện bắt buộc phải hết lỗi, và phần **"Phần đã hết lỗi"** làm mốc phải giữ được.

| Điều kiện | Bug gốc (phần còn lỗi + phần đã hết lỗi của note) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường bàn giao, bản dựng đang chạy | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.6** (đọc ở thanh bên trái) | Không |
| Vai trò | Cán bộ nghiệp vụ Trung ương | `cbnv_tw` · CB Nghiệp vụ - Trung ương · CB_NV_TW · đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp | Không |
| Màn hình | Đào tạo, tập huấn → Khóa học → chi tiết → thẻ "Công bố kết quả" | Đúng đường đó, đi bằng menu bên trái rồi bấm mã khóa học | Không |
| Tiền đề — khóa học | Khóa học trạng thái "Hoàn thành" có học viên đã được phê duyệt kết quả; note dùng khóa "test thêm mới khóa học" (KH-20260703-005) | Khóa học note dùng **không còn** trong kho, nên chọn khóa học khác cùng điều kiện: **AAA-KH-TW** "Tập huấn pháp lý cấp Trung ương 2026", trạng thái **Hoàn thành** (bước 7 trên thanh tiến trình), có **4 học viên đã có điểm và kết quả** | Không |
| Tiền đề — trạng thái công bố | Note đo ở cả hai trạng thái (chưa công bố và đã công bố) | Đo ở **cả hai trạng thái**: tự hủy công bố để có học viên "Chưa công bố", rồi công bố lại | Không |
| Nội dung 1 — bước 4 của phiếu | "Chọn danh sách học viên và bấm nút Công bố" chưa thực hiện được | Tích chọn **đúng 1 học viên** rồi bấm nút công bố cho phần đã chọn, kiểm xem **chỉ học viên đó** đổi trạng thái hay không | Không |
| Nội dung 2 — nút của từng học viên | Nút "Công bố"/"Hủy" ở cột Hành động luôn mờ, bấm không được; rê chuột hiện chú thích "sẽ khả dụng khi hệ thống hỗ trợ" | Bấm **thật** nút "Hủy" rồi nút "Công bố" ở cột Hành động của một học viên; **rê chuột** lên nút để xem còn chú thích đó không | Không |
| Nội dung 3 — ô tích chọn | Ô tích từng dòng và ô "chọn tất cả" không có tác dụng | Tích **từng dòng** và tích **ô chọn tất cả**, đếm số dòng được chọn và xem nút thao tác có nhận số lượng đã chọn không | Không |
| Nội dung 4 — thời điểm công bố sau khi hủy | Sau khi hủy công bố, cột "Thời điểm công bố" vẫn giữ mốc thời gian lần công bố trước | Hủy công bố rồi **đọc lại cột "Thời điểm công bố"** của đúng học viên đó | Không |
| Nội dung 5 — công bố lại sau khi hủy | Bấm "Công bố tất cả" lần nữa thì báo "Đang có yêu cầu PUBLISH đang chờ xử lý cho khóa học này", khóa học bị kẹt | Chạy trọn vòng **công bố cả khóa → hủy công bố cả khóa → công bố lại cả khóa**, xem có bị chặn không | Không |
| Mốc phải giữ — công bố / hủy cả khóa | Note ghi đã chạy được, hủy phải nhập lý do tối thiểu 10 ký tự | Kiểm lại cả hai nút cấp khóa và **thử nhập lý do 3 ký tự** xem còn bị chặn không | Không |
| Mốc phải giữ — chặn khi chưa Hoàn thành | Note ghi hệ thống chặn công bố và báo rõ lý do | Mở một khóa học **chưa Hoàn thành** (KH-20260803-001, Dự thảo) và đọc thẻ "Công bố kết quả" | Không |
| Cách đo | Note đo trên 3 khóa học, cả 2 trạng thái | Đo bằng **2 cách**: bấm thật từng nút và đọc lại bảng sau mỗi thao tác; kèm ảnh chụp màn ở trạng thái có cả học viên đã công bố lẫn chưa công bố | Không |
| Ràng buộc chấm | Không chấm bằng quan sát tĩnh, phải chạy tới bước sinh ra lỗi cũ | Thực hiện **7 lượt đổi trạng thái công bố thật** trong phiên đo, không chấm bằng cách nhìn nút | Không |

**Kết luận: 0 GAP** — đúng bản dựng đang chạy, đúng vai trò và màn hình, dựng lại tiền đề tương đương khi khóa học cũ không còn, đo đủ 5 nội dung còn lỗi và 2 mốc phải giữ, chạy trọn tới chỗ sinh ra lỗi cũ.

## Đo lường trực tiếp (05/08/2026, `18.143.165.120.nip.io`, bản dựng V1.0.6, tài khoản `cbnv_tw`)

### Nội dung 1 — bước 4 của phiếu: chọn danh sách học viên rồi bấm Công bố

- ✅ Thanh thao tác nay có thêm **hai nút theo lựa chọn**: "Công bố đã chọn (N)" và "Hủy công bố đã chọn (N)"; số N chạy đúng theo số dòng đang tích.
- ✅ Tích **đúng 1 học viên** (Học viên TW 01) rồi bấm "Công bố đã chọn (1)" → hệ thống hỏi xác nhận "Công bố kết quả 1 học viên đã chọn?" → đồng ý → **chỉ học viên đó** chuyển sang "Đã công bố" với mốc thời gian mới **05/08/2026 04:04**, ba học viên còn lại giữ nguyên mốc cũ 03/08/2026 17:55.
- ✅ Đúng thao tác mà phiếu mô tả ở bước 4 — **công bố cho một phần danh sách học viên** — nay thực hiện được.

### Nội dung 2 — nút "Công bố" / "Hủy" của từng học viên

- ✅ Nút ở cột **Hành động** của từng học viên nay **bấm được** (không còn mờ). Bấm "Hủy" ở học viên TW 02 → nhập lý do → học viên đó về "Chưa công bố"; bấm tiếp "Công bố" ở chính học viên đó → trở lại "Đã công bố" lúc **05/08/2026 04:05**, các học viên khác không đổi.
- ✅ **Rê chuột lên nút không còn chú thích** "Công bố/hủy theo từng học viên sẽ khả dụng khi hệ thống hỗ trợ (hiện chỉ công bố cấp khóa)".
  Ảnh (một học viên "Chưa công bố" với nút "Công bố", các học viên khác "Đã công bố" với nút "Hủy"): [`../image/CBKQDTBD_01-r2-cong-bo-theo-tung-hoc-vien.png`](../image/CBKQDTBD_01-r2-cong-bo-theo-tung-hoc-vien.png)

### Nội dung 3 — ô tích chọn từng dòng và ô chọn tất cả

- ✅ Tích **1 dòng** → nút thao tác nhận đúng "(1)"; tích **ô chọn tất cả** ở dòng tiêu đề → **4/4 dòng** được chọn và nút nhận đúng "(4)".
- ✅ Hai nút còn **tự bật/tắt theo trạng thái của các dòng đang chọn**: chọn học viên đã công bố thì chỉ nút "Hủy công bố đã chọn" sáng, chọn học viên chưa công bố thì chỉ nút "Công bố đã chọn" sáng — không còn cảnh tích xong vẫn không bấm được nút nào.

### Nội dung 4 — cột "Thời điểm công bố" sau khi hủy

- ✅ Sau khi hủy công bố một học viên, cột **"Thời điểm công bố" của học viên đó về dấu "—"**, không còn giữ mốc thời gian của lần công bố trước; cột trạng thái và cột thời điểm nay nói cùng một điều.

### Nội dung 5 — công bố lại sau khi đã hủy

- ✅ Chạy trọn vòng **công bố cả khóa → hủy công bố cả khóa (có lý do) → công bố lại cả khóa**: lần công bố lại **thành công**, cả 4 học viên về "Đã công bố" lúc 05/08/2026 04:06.
- ✅ **Không còn thông báo "Đang có yêu cầu PUBLISH đang chờ xử lý cho khóa học này"**, khóa học không bị kẹt.

### Phần note ghi đã hết lỗi — kiểm lại để chắc không hỏng ngược

- ✅ Hai nút cấp khóa **"Công bố tất cả"** và **"Hủy công bố tất cả"** vẫn chạy đúng.
- ✅ Hủy công bố vẫn **bắt nhập lý do tối thiểu 10 ký tự**: nhập 3 ký tự thì hệ thống báo "Lý do phải có tối thiểu 10 ký tự" và **không hủy** bản ghi nào.
- ✅ Khóa học **chưa ở trạng thái Hoàn thành** (KH-20260803-001, Dự thảo) vẫn bị chặn: thẻ hiện "Chưa thể công bố kết quả — Chỉ có thể công bố/hủy công bố kết quả khi khóa học đã ở trạng thái Hoàn thành", cả 4 nút đều mờ.

### Kết luận

Thực hiện 7 lượt đổi trạng thái công bố thật trong cùng một phiên: bước 4 của phiếu (chọn danh sách học viên rồi bấm Công bố) nay làm được, nút Công bố/Hủy của từng học viên bấm được và không còn chú thích "sẽ khả dụng khi hệ thống hỗ trợ", ô tích chọn từng dòng và chọn tất cả đều có tác dụng, thời điểm công bố được xóa đúng khi hủy, và công bố lại sau khi hủy không còn bị kẹt; hai mốc đang chạy tốt (thao tác cấp khóa, chặn khi chưa Hoàn thành) vẫn giữ nguyên → **Pass**.

### Ghi nhận thêm (ngoài phạm vi phiếu — không tự thêm dòng mới vào sheet)

- Thông báo sau khi công bố là **"Đã công bố kết quả. Cổng PLQG sẽ lấy dữ liệu ở lần đồng bộ kế tiếp."**, chưa kèm **số lượng học viên** như câu mô tả trong phiếu ("Đã công bố kết quả cho {số lượng} học viên"). Note vòng 2 không nêu ý này nên không dùng để chấm; ghi lại để đối tác/BA cân nhắc.
- Công tắc **"Công bố lên Cổng PLQG"** ở đầu thẻ phản ánh trạng thái của **toàn khóa**: chỉ cần một học viên chưa công bố thì công tắc về vị trí tắt. Hành vi này hợp lý, chỉ ghi lại để tránh hiểu nhầm khi đọc màn hình.
- Trạng thái dữ liệu sau phiên đo: khóa học **AAA-KH-TW** được trả về **đủ 4 học viên "Đã công bố"** như trước khi đo (mốc thời gian mới là 05/08/2026).
