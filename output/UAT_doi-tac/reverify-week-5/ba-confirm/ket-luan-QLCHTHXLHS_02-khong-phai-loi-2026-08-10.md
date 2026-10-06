# `QLCHTHXLHS_02` (dòng 151) — Số thẻ ở màn Cấu hình hệ thống — **Không phải lỗi** — 2026-08-10

> **File này để làm gì:** dòng 151 đang treo `Trạng thái dev fix = BA confirm` nhưng **không có điểm nào cần BA quyết** — BA đã chốt từ **07/05/2026** và đặc tả hiện hành đã ghi đúng. File này là căn cứ để chuyển dòng sang `reject` và là nội dung đề nghị BA phản hồi lại đơn vị kiểm thử.
>
> **Tách khỏi** `ba-confirmation-needed-6-dong-con-treo-2026-08-10.md` để dòng này không phải nằm chờ cùng 6 dòng thực sự cần BA quyết.

**Dạng:** A — QA đã có kết luận, chỉ cần BA phản hồi đối tác.

**Vân tay bản dựng của phép đo**

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-LoDAkSbB.js` |
| `last-modified` / `etag` | `Fri, 07 Aug 2026 15:26:56 GMT` · `W/"6a75f940-428"` |
| Chuỗi chân thanh bên | `HTPLDN · V1.0.10` — **không dùng làm vân tay**, chỉ ghi kèm |
| Thời điểm đo | 10/08/2026 (giờ VN) |
| Tài khoản | `cbnv_tw` / `Test@1234` → `CB_NV_TW`, đơn vị `00000000-0000-4000-8000-000000000001` |

---

## `QLCHTHXLHS_02` (dòng 151) — Số thẻ ở màn Cấu hình hệ thống

**Bối cảnh testcase**

- Dòng Excel: 151, mã TC `QLCHTHXLHS_02`.
- Nội dung kiểm tra: *Quản trị hệ thống → Cấu hình hệ thống*, kiểm thanh thẻ ở đầu trang.
- Expected trong file UAT: *"hiển thị các trường thông tin giống với thiết kế · đúng định dạng · không tràn/đè lên nhau, đồng nhất ngôn ngữ"*.
- Actual đối tác ghi: *"**SRS yêu cầu 4 thẻ**: 'Thời hạn xử lý / SLA', 'Phân công mặc định', 'Mẫu phản hồi', 'Quy trình hỗ trợ' nhưng hiện tại hệ thống hiển thị **3 thẻ**: 'Thời hạn xử lý / SLA', 'Mẫu phản hồi', 'Quản lý ngày lễ'."*

**Đối chiếu SRS v3.5**

- Đặc tả hiện hành quy định màn Cấu hình hệ thống có **đúng 3 thẻ**: *Thời hạn xử lý / SLA* — *Mẫu phản hồi* — *Quản lý ngày lễ*. **Trùng khít** 3 thẻ đối tác quan sát được.
- Hai thẻ đối tác kỳ vọng đã bị **bỏ có chủ đích**, mỗi thẻ theo một quyết định riêng của BA ngày **07/05/2026** — tức trước cả đợt UAT này:
  - *Quy trình hỗ trợ* — bỏ theo Hướng A, vì luồng vụ việc chạy cứng theo máy trạng thái trong mã nguồn, không cấu hình động;
  - *Phân công mặc định* — bỏ theo Q11, vì chức năng phân công đã dùng bộ lọc tự động 4 tiêu chí thay cho cấu hình tĩnh.
- Đặc tả còn đặt thêm **luật ẩn thẻ theo quyền**: cán bộ nghiệp vụ không phải quản trị hệ thống chỉ thấy thẻ *Mẫu phản hồi*; thẻ *Quản lý ngày lễ* chỉ hiện với quản trị hệ thống hoặc cán bộ nghiệp vụ cấp Trung ương.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1808` (bảng thành phần — *"Tab navigation (3 tabs)"* + luật ẩn thẻ theo quyền)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1793` (ghi chú v2.1 — *"Đã bỏ: Tab 4 Quy trình hỗ trợ … Tab 2 Phân công mặc định"*)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:20` (nhật ký sửa đổi 2026-05-07 — *"Hướng A — Bỏ Tab 4 Quy trình hỗ trợ khỏi SCR-VIII-06 (4 → 3 tab)"*)

**Kết quả verify UI hiện tại**

- Đo 10/08/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw` (`CB_NV_TW`), màn `/quan-tri/cau-hinh`.
- Tiêu đề trang đúng *"Cấu hình hệ thống"*; thanh thẻ hiện **2 thẻ**: *Mẫu phản hồi* · *Quản lý ngày lễ*.
- Đúng luật ẩn thẻ ở `:1808`: vai trò đang đo là cán bộ nghiệp vụ Trung ương, **không phải** quản trị hệ thống, nên không thấy thẻ *Thời hạn xử lý / SLA*. Bộ **3 thẻ** mà đối tác quan sát được là góc nhìn của tài khoản quản trị hệ thống — cũng đúng đặc tả.
- ⇒ Cả hai góc nhìn đều khớp đặc tả hiện hành; không có thẻ nào thiếu, không có thẻ nào thừa.

**Kết luận QA**

- `QLCHTHXLHS_02` **không phải bug theo SRS v3.5**.
- Phần mềm đúng đặc tả ở cả số thẻ lẫn luật ẩn thẻ theo quyền.
- Điểm sai nằm ở **ô "Kết quả thực tế" của phiếu**, không phải ở phần mềm:
  - câu *"SRS yêu cầu 4 thẻ"* trích từ một bản đặc tả **đã lỗi thời** — bản hiện hành quy định 3 thẻ từ 07/05/2026;
  - hai thẻ *Phân công mặc định* và *Quy trình hỗ trợ* đã được BA bỏ có chủ đích, mỗi thẻ có quyết định riêng, nên việc không thấy chúng là **đúng thiết kế**;
  - thẻ *Quản lý ngày lễ* mà đối tác coi là "lạ" chính là thẻ hợp lệ trong đặc tả hiện hành.
- Dòng này **đang treo `BA confirm` oan** — BA đã trả lời từ trước khi đợt UAT bắt đầu.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị cập nhật lại `QLCHTHXLHS_02` theo SRS v3.5:

- Xác nhận với đơn vị kiểm thử rằng màn Cấu hình hệ thống có **3 thẻ** — *Thời hạn xử lý / SLA*, *Mẫu phản hồi*, *Quản lý ngày lễ* — theo quyết định BA ngày **07/05/2026**; hai thẻ *Phân công mặc định* và *Quy trình hỗ trợ* đã được bỏ có chủ đích.
- Lưu ý thêm giúp đơn vị kiểm thử: số thẻ nhìn thấy **thay đổi theo quyền của tài khoản đo**, nên khi đo lại xin ghi rõ tài khoản đã dùng.
- Đề nghị đơn vị kiểm thử cập nhật ô "Kết quả thực tế" cho khớp đặc tả hiện hành.
- Verdict QA đề xuất: **`Không phải bug theo SRS`** — chuyển `Trạng thái dev fix` từ `BA confirm` sang `reject`, **không** gửi Dev.

---

## Việc tiếp theo

| Việc | Ai | Chặn bởi |
|---|---|---|
| Đổi `Trạng thái dev fix`: `BA confirm` → `reject`, ghi "DEV phản hồi lần 1" + "Kết quả verify" | QA | không chặn — làm được ngay |
| Gửi nội dung phản hồi ở mục trên cho đơn vị kiểm thử | BA | không chặn — không cần BA quyết, chỉ cần BA duyệt câu chữ |
