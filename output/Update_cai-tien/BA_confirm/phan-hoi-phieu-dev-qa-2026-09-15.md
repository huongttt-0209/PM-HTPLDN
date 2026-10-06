# Quyết định chốt — đợt rà T1–T7 sau bản `aaee63b`

| | |
|---|---|
| **Phạm vi** | 4 nội dung do bộ phận phát triển nêu · 20 nội dung do bộ phận kiểm thử nêu · 27 mục sửa tài liệu |
| **Đối chiếu** | SRS v3.5 commit `aaee63b` |
| **Ngày chốt** | 15/09/2026 |
| **Dấu mốc khi sửa SRS** | `[CR-DEV-2026-09-15]` cho phần A · `[CR-QA-2026-09-15]` cho phần B và C |
| **Khối lượng** | **72 chỗ sửa** trên 9 tệp; 4 chỗ chốt không thi hành |

Mỗi mục nêu **quyết định cuối** và **chỗ sửa trong SRS**. Chỗ sửa đánh số liên tục 1–76.

---

# Phần A — Bốn nội dung của bộ phận phát triển

## A1. Kênh DVC của hồ sơ hỏi đáp

### A1.1. Quyết định

Giá trị `DVC` trong danh sách kênh tiếp nhận của hồ sơ hỏi đáp là **nhãn nguồn do cán bộ chọn tay**. Hồ sơ mang nhãn này **không tương ứng hồ sơ nào** trên Hệ thống giải quyết thủ tục hành chính Bộ Tư pháp và **không có mã hồ sơ DVC**.

Hệ thống không có đầu nối nào nhận hồ sơ hỏi đáp từ Cổng dịch vụ công. Vụ việc sinh từ cầu nối chuyển luồng **không có và không cần** mã hồ sơ DVC.

### A1.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 1 | `srs-fr-02-hoi-dap.md` — bảng thuộc tính `HOI_DAP`, cột `kenh_tiep_nhan` | Ghi rõ: giá trị `DVC` là nhãn nguồn do cán bộ chọn; hệ thống không nhận hồ sơ hỏi đáp tự động từ Cổng dịch vụ công; hồ sơ mang nhãn này không có mã hồ sơ thủ tục hành chính |
| 2 | `srs-fr-02-hoi-dap.md` — bảng Quy đổi kênh của `FR-II-11` | Thêm ghi chú: kênh kế thừa là nhãn nguồn, không kéo theo nghĩa vụ đồng bộ với hệ thống ngoài |

---

## A2. Đồng bộ trạng thái với hệ thống ngoài cho hồ sơ đi qua cầu nối

### A2.1. Quyết định

**Không sự kiện nào của hồ sơ đi qua cầu nối cần đồng bộ ra ngoài:**

| Sự kiện | Quyết định |
|---|---|
| Chuyển hồ sơ hỏi đáp sang vụ việc | Không gửi |
| Hoàn tác do xóa mềm vụ việc còn Chờ tiếp nhận | Không gửi |
| Chuyển lại sau hoàn tác | Không gửi |
| Vụ việc sinh từ cầu nối bị kiểm tra Không đạt | Không gửi. Doanh nghiệp vẫn nhận thông báo trong phần mềm và thư điện tử |

**Điều kiện kích hoạt đồng bộ đổi từ nhãn kênh sang mã hồ sơ:** hệ thống gửi trạng thái ra ngoài **khi và chỉ khi hồ sơ có mã hồ sơ DVC**. Nghĩa vụ đồng bộ giữ nguyên cho vụ việc do đầu nối tiếp nhận qua LGSP tạo ra.

### A2.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 3 | `srs-fr-05-vu-viec.md` — `FR-V.I-12` phần Mô tả (`:967`), bước 3, Hậu điều kiện, Tiêu chí chấp nhận | Đổi điều kiện từ *"Nếu hồ sơ qua DVC"* thành *"Nếu hồ sơ có mã hồ sơ DVC"*. Thêm một tiêu chí chấp nhận: vụ việc sinh từ cầu nối mang nhãn kênh DVC nhưng không có mã hồ sơ thì không gửi trạng thái ra ngoài, doanh nghiệp vẫn nhận thông báo |
| 4 | `srs-fr-05-vu-viec.md` — bảng chuyển trạng thái, dòng `CHO_TIEP_NHAN → DA_TIEP_NHAN` | Mệnh đề *"gửi thông báo doanh nghiệp nếu DVC"* căn theo mã hồ sơ |
| 5 | `srs-v3.5.md` — `BR-FLOW-11` | Thêm một vế: hồ sơ sinh từ chuyển luồng không kế thừa nghĩa vụ đồng bộ với hệ thống ngoài của nhóm đích; nghĩa vụ đó chỉ áp cho hồ sơ do đầu nối tạo ra |

---

## A3. Thời hạn xử lý hỏi đáp

### A3.1. Quyết định

**15 ngày làm việc cho vướng mắc thường, 30 ngày làm việc cho vướng mắc phức tạp** — theo Nghị định 55/2019/NĐ-CP Điều 8 Khoản 1.

Hai nơi khai dữ liệu khởi tạo cho cùng một thực thể cấu hình thời hạn đang lệch nhau ở **bốn dòng**. Giá trị đúng:

| Loại | Tệp nền | Tệp nhóm Quản trị | **Chốt** |
|---|---|---|---|
| Hỏi đáp, mức thường | 15 ngày | 5 ngày | **15 ngày** |
| Hỏi đáp, mức phức tạp | 30 ngày | 10 ngày | **30 ngày** |
| Vụ việc | 15 ngày | 10 ngày | *(không sửa đợt này)* |
| Hồ sơ chi trả | 15 ngày | 10 ngày | *(không sửa đợt này)* |

**Đợt này chỉ sửa hai dòng Hỏi đáp.** Hai dòng Vụ việc và Hồ sơ chi trả nằm ngoài nội dung được hỏi nên giữ nguyên trạng lệch, ghi điểm treo trong đặc tả để lượt rà sau xử lý.

Trong lúc chưa sửa xong: giữ nguyên cấu hình và thời hạn của hồ sơ đang xử lý.

### A3.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 6 | `srs-fr-10-quan-tri.md` — dữ liệu khởi tạo cấu hình thời hạn | Sửa **hai dòng Hỏi đáp** thành 15 / 30 ngày làm việc. **Hai dòng Vụ việc và Hồ sơ chi trả giữ nguyên trạng lệch**, ghi điểm treo ngay tại chỗ |
| 7 | — | **Không thi hành** — giữ nguyên dòng Hồ sơ chi trả ở tệp nền |
| 8 | Cả hai nơi | Thêm một dòng: danh sách này là bản duy nhất, hai tệp phải giống nhau từng dòng |

---

## A4. Cách khai hai mức thời hạn của hỏi đáp

### A4.1. Quyết định

**Giữ một mã cấu hình `HOI_DAP`. Bỏ hai mã `HOI_DAP_THUONG` và `HOI_DAP_PHUC_TAP`.**

Hai mức thời hạn đặt thành **hai cột trên cùng một dòng cấu hình**. Khi tính hạn, hệ thống đọc dòng `HOI_DAP` rồi chọn cột theo trường `muc_do_phuc_tap` của chính hồ sơ.

Quản trị hệ thống thấy đúng **bốn dòng cấu hình** như hiện nay; riêng dòng Hỏi đáp có hai ô số ngày. Hai mốc cảnh báo là tỷ lệ phần trăm của thời hạn nên dùng chung cho cả hai mức.

Mã `HO_SO_CHI_TRA_BO_SUNG` cũng bỏ — thời hạn gửi bổ sung đã có cột riêng trên cùng dòng.

### A4.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 9 | `srs-v3.5.md` và `srs-fr-10-quan-tri.md` — bảng thuộc tính cấu hình thời hạn | Thêm một cột thời hạn cho mức phức tạp, để trống với loại yêu cầu không phân mức. Giữ mã loại yêu cầu là khóa duy nhất, đúng bốn giá trị |
| 10 | `srs-v3.5.md` và `srs-fr-10-quan-tri.md` — dữ liệu khởi tạo | Bỏ hai mã `HOI_DAP_THUONG`, `HOI_DAP_PHUC_TAP`; còn một dòng `HOI_DAP` mang hai thời hạn 15 / 30 ngày làm việc |
| 11 | `srs-v3.5.md` — dữ liệu khởi tạo | Bỏ mã `HO_SO_CHI_TRA_BO_SUNG` |
| 12 | `srs-fr-02-hoi-dap.md:1936` — `BR-CALC-03` · `:144` — `FR-II-01` bước 9 · `:351` — `FR-II-03` bước 4 | Lấy dòng cấu hình loại `HOI_DAP`, chọn cột thời hạn theo `muc_do_phuc_tap` của hồ sơ. `FR-II-03` bước 4 đang gọi đích danh hai mã cũ và ghi cứng số 15 / 30 trong lời văn — sửa cả hai vế, số ngày đọc từ cấu hình |
| 13 | `srs-fr-10-quan-tri.md` — `FR-VIII-10` đầu vào và màn hình | Thêm ô nhập thời hạn mức phức tạp, chỉ hiện với loại Hỏi đáp; ràng buộc kiểm tra như ô thời hạn hiện có |

---

# Phần B — Hai mươi nội dung của bộ phận kiểm thử

## Q03. Xóa vụ việc sinh từ cầu nối

### Q03.1. Quyết định

**Xóa từ màn danh sách vụ việc.** Quy tắc xóa áp cho mọi vụ việc sinh từ cầu nối, nhận biết theo liên kết truy nguồn chứ không theo kênh tiếp nhận: chỉ xóa được khi còn Chờ tiếp nhận, đã tiếp nhận thì chặn, khi xóa thì kéo theo mở lại hồ sơ hỏi đáp gốc.

**Xóa hàng loạt xử lý từng dòng, không chặn cả lô.** Mỗi vụ việc cầu nối bị xóa đều kéo theo mở lại hồ sơ gốc. Dòng không đủ điều kiện bị loại khỏi lô kèm mã lỗi của chính nó, các dòng còn lại vẫn xóa.

### Q03.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 14 | `srs-fr-05-vu-viec.md` — `FR-V.I-01` (UC51), màn `SCR-V.I-01` dòng 22 | Đặt quy tắc xóa tại đây: điều kiện Chờ tiếp nhận, chặn `ERR-INTG-06`, kéo theo hoàn tác. Không đặt ở `FR-V.I-07` — chức năng đó gắn với màn chi tiết `SCR-V.I-03`, còn nút Xóa nằm trên màn danh sách `SCR-V.I-01`, mà màn này khai dùng `FR-V.I-01` và `FR-V.I-08` |
| 15 | `srs-fr-05-vu-viec.md` — `FR-V.I-05` bước 5a, 5b | Đổi thành dẫn chiếu sang `FR-V.I-01`, không chép lại quy tắc |
| 16 | `srs-fr-05-vu-viec.md` — `SCR-V.I-01` dòng 23 | Thêm bảng kết quả từng dòng sau khi xóa hàng loạt: số xóa được, số bị loại, lý do từng dòng |

---

## Q06. Ô nhập quy mô doanh nghiệp

### Q06.1. Quyết định

**Một ô nhập duy nhất.** Biểu mẫu doanh nghiệp hiện có hai ô cùng nói về quy mô; giữ lại một ô mang nhãn **"Quy mô doanh nghiệp"**, chọn từ danh mục, lưu vào một cột duy nhất.

Hệ thống tự xác định quy mô theo số lao động, doanh thu và nguồn vốn rồi điền sẵn vào ô đó; cán bộ sửa lại được.

Cột `quy_mo` bỏ khỏi thực thể doanh nghiệp; mọi nơi đang đọc cột này chuyển sang đọc cột danh mục. Cột ảnh chụp quy mô trên hồ sơ chi trả **không đụng tới** — đó là giá trị ghi lại tại thời điểm xét mức hỗ trợ, khác mục đích.

Rà toàn kho: tên `quy_mo` xuất hiện ở **35 chỗ trên 8 tệp**, trong đó hai chỗ dùng sai tên cột chứ không chỉ sai nguồn đọc.

### Q06.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 17 | `srs-fr-07-doanh-nghiep.md` — `FR-V.III-01` trường 8 · `srs-fr-10-quan-tri.md` — `FR-VIII-22` trường 7 · `srs-fr-07-doanh-nghiep.md` — màn `SCR-V.III-03` nhóm B ô 8 và ô 9 kèm quy tắc gợi ý giá trị số 3 | Bỏ ô `quy_mo` khỏi hai chức năng và khỏi màn hình. Màn `SCR-V.III-03` hiện có cả hai ô — ô 8 "Loại doanh nghiệp" và ô 9 "Quy mô"; giữ một ô, đổi nhãn thành "Quy mô doanh nghiệp"; quy tắc gợi ý giá trị trỏ sang ô còn lại |
| 18 | `srs-fr-07-doanh-nghiep.md` — `FR-V.III-01` bước 5 | Quy tắc tự xác định quy mô ghi kết quả vào cột danh mục; cán bộ sửa lại trên cùng một ô |
| 19 | 8 tệp — 35 chỗ dùng tên `quy_mo` | Bỏ cột khỏi bảng thuộc tính và sơ đồ thực thể; mọi chỗ còn lại đọc cột danh mục. Hai chỗ phải đổi tên cột: `srs-fr-06-chi-tra.md:117` (bước 4 nhóm Chi trả — viết *"lưu hồ sơ chi trả với `quy_mo = NULL`"* trong khi cột thật tên `quy_mo_dn`; đọc từ cột danh mục, ghi vào `quy_mo_dn`) và `srs-fr-05-vu-viec.md:1681` (quy tắc chấm điểm ưu tiên) |

---

## Q07. Ràng buộc thẻ hành nghề khi người hỗ trợ cập nhật tư vấn viên

### Q07.1. Quyết định

**Không chặn.** Chức năng người hỗ trợ cập nhật thông tin tư vấn viên chỉ đổi địa chỉ, điện thoại, thư điện tử và lĩnh vực; không có ô thẻ nên không kiểm thẻ tại đây.

Ràng buộc thẻ là **chặn nhẹ** — chỉ chặn tại chỗ người dùng có thể bổ sung ngay, tức chức năng cập nhật năng lực.

### Q07.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 20 | `srs-fr-04-chuyen-gia-tvv.md:418` | Thêm một gạch đầu dòng: ràng buộc thẻ không áp cho `FR-IV-11`, vì chức năng này không nhận trường thẻ |

---

## Q09. Lưu loại lý do từ chối và kết quả kiểm tra

### Q09.1. Quyết định

**Lưu.** Vụ việc lưu lại **loại lý do từ chối** và **kết quả kiểm tra từng hạng mục** tại lần kiểm tra gần nhất; màn chi tiết hiển thị lại ở chế độ chỉ đọc.

**Đợt này không dựng báo cáo gom theo loại lý do.** Quy tắc nhóm "Không xác định" là **quy tắc dữ liệu**: mọi chiều gom theo trường này, ở bất kỳ báo cáo hay ô lọc nào, đều xếp hồ sơ không có giá trị vào nhóm "Không xác định", không suy đoán ngược.

### Q09.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 21 | `srs-v3.5.md` và `srs-fr-05-vu-viec.md` — bảng thuộc tính `VU_VIEC` | Thêm hai nội dung lưu: loại lý do từ chối và kết quả kiểm tra từng hạng mục |
| 22 | `srs-fr-05-vu-viec.md` — màn chi tiết vụ việc | Hiển thị lại hai nội dung này ở chế độ chỉ đọc |
| 23 | `srs-fr-05-vu-viec.md:527`, `:542` | Viết lại quy tắc nhóm "Không xác định" thành quy tắc dữ liệu; cụm *"khi thống kê"* đổi thành *"khi tra cứu và tổng hợp"* |

---

## Q10. Tập đơn vị được chọn khi chuyển luồng

### Q10.1. Quyết định

Cán bộ nghiệp vụ chọn đơn vị thụ lý trong **toàn bộ đơn vị: Trung ương, Bộ ngành, Địa phương** — cùng tập với thao tác chọn lại đơn vị ở chức năng quản lý hỏi đáp.

Hệ quả đã chấp nhận: sau khi chuyển sang đơn vị khác, đơn vị nguồn không tra được tiến độ xử lý.

### Q10.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 24 | `srs-fr-02-hoi-dap.md` — `FR-II-11` trường 4 | Ghi rõ tập chọn là toàn bộ đơn vị, dẫn `FR-II-01` bước 5a |

---

## Q11. Đồng bộ với hệ thống ngoài cho vụ việc cầu nối mang kênh DVC

### Q11.1. Quyết định

**Không đồng bộ.** Hồ sơ hỏi đáp mang nhãn `DVC` chưa từng là hồ sơ thủ tục hành chính nên không có mã hồ sơ để đồng bộ. Điều kiện đồng bộ căn theo **mã hồ sơ**, không theo nhãn kênh — chi tiết tại **A2**.

### Q11.2. Sửa trong SRS

Không phát sinh chỗ sửa riêng; đã nằm ở mục **3, 4, 5**.

---

## Q12. Quy ước của chỉ số thời gian xử lý toàn trình

### Q12.1. Quyết định

**Theo đúng mẫu thẻ chỉ số, cùng quy ước với chỉ số thời gian xử lý trung bình**: lọc theo năm, tháng, đơn vị; nằm trong nhóm chỉ số phát sinh trong kỳ; có xu hướng so kỳ trước; làm tròn một chữ số thập phân; kỳ rỗng hiển thị "—".

**Tập vụ việc gồm cả trạng thái Hoàn thành và Đã đánh giá**, ngày hoàn thành nằm trong kỳ. Áp cho cả hai thẻ chỉ số. Vụ việc không rơi khỏi thẻ khi doanh nghiệp gửi đánh giá.

**Không gồm vụ việc bị từ chối** — vụ việc từ chối không có ngày hoàn thành nên không có mốc kết thúc để đo. Chữ "đóng trong kỳ" đổi thành **"hoàn thành trong kỳ"**.

### Q12.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 25 | `srs-fr-01-dashboard.md` — `KPI-S-03` | Khai template, đưa vào danh sách chỉ số phát sinh trong kỳ, ghi làm tròn và kỳ rỗng, xu hướng so kỳ trước |
| 26 | `srs-fr-01-dashboard.md` — `KPI-S-02` và `KPI-S-03` | Tập vụ việc ghi rõ gồm `HOAN_THANH` và `DA_DANH_GIA` |
| 27 | `srs-fr-01-dashboard.md` — `KPI-S-03` bước 1 và bước 4 · `srs-v3.5.md` — `BR-RPT-01` | Chữ "đóng trong kỳ" đổi thành "hoàn thành trong kỳ"; `BR-RPT-01` bổ sung `DA_DANH_GIA` vào tập trạng thái cuối hợp lệ của vụ việc |

---

## Q13. Mức cảnh báo thời hạn của hồ sơ đã chuyển luồng

### Q13.1. Quyết định

Trạng thái **Đã chuyển luồng là trạng thái kết thúc** của hồ sơ hỏi đáp về mặt thời hạn.

Khi chuyển luồng, hệ thống **xóa mức cảnh báo** của hồ sơ nguồn — việc xóa này không gửi thông báo — và bộ đếm thời hạn dừng. Khi hoàn tác, khôi phục thời hạn và mức cảnh báo từ hai trường ảnh chụp lúc chuyển.

Hồ sơ đã chuyển **vào tập tra cứu "câu hỏi đã xử lý"**.

Tập trạng thái kết thúc của hồ sơ hỏi đáp: **Hoàn thành, Hủy, Đã chuyển luồng**.

### Q13.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 28 | `srs-fr-02-hoi-dap.md` — `FR-II-11` bước 8 | Xóa mức cảnh báo của hồ sơ nguồn sau khi chụp ảnh |
| 29 | `srs-v3.5.md` — cạnh quy tắc mức cảnh báo | Liệt kê tường minh tập trạng thái kết thúc của hỏi đáp: `HOAN_THANH`, `HUY`, `DA_CHUYEN_LUONG` |
| 30 | `srs-fr-02-hoi-dap.md:887` — `FR-II-10` | Thêm `DA_CHUYEN_LUONG` vào bộ lọc cứng của tra cứu câu hỏi đã xử lý |

Tác vụ tự động tính mức cảnh báo giữ nguyên phạm vi quét hai trạng thái đang xử lý, không sửa.

---

## Q14. Trạng thái nào vào nhóm nào của báo cáo hỏi đáp

### Q14.1. Quyết định

| Trạng thái hỏi đáp | Nhóm | Vào tổng |
|---|---|---|
| `DA_DUYET`, `CONG_KHAI`, `HOAN_THANH` | Đã trả lời | Có |
| `MOI`, `TIEP_NHAN`, `DANG_XU_LY`, `DA_TRA_LOI`, `CHO_PHE_DUYET` | Chờ trả lời | Có |
| `DA_CHUYEN_LUONG` | Đã chuyển sang Vụ việc | Có |
| `HUY` | — | **Không** |

Hồ sơ đã hủy không còn là yêu cầu cần xử lý nên không vào tổng. Nhờ vậy **tổng ba nhóm bằng tổng chung** và ô lọc giữ đúng ba giá trị hiện có.

### Q14.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 31 | `srs-fr-11-bao-cao.md` — `FR-IX-01` | Ghi bảng trạng thái → nhóm ở trên |
| 32 | `srs-fr-11-bao-cao.md` — `FR-IX-01` | Ghi rõ báo cáo này là ngoại lệ của bước 4 mẫu báo cáo — đếm cả hồ sơ chưa duyệt |

---

## Q15. Mốc bắt đầu của chỉ số toàn trình với vụ việc tiếp nhận trực tiếp

### Q15.1. Quyết định

**Ngày tạo bản ghi vụ việc.** Chỉ số đo thời gian doanh nghiệp thực tế phải chờ, mà doanh nghiệp bắt đầu chờ từ lúc yêu cầu vào hệ thống, không phải từ lúc cán bộ bấm tiếp nhận.

Với hồ sơ không qua chuyển luồng, chỉ số này bằng thời gian xử lý thường **cộng thời gian chờ tiếp nhận**.

### Q15.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 33 | `srs-fr-01-dashboard.md:664` | Sửa ghi chú thành *"bằng thời gian xử lý thường cộng thời gian chờ tiếp nhận"* |

---

## Q16. Tập vụ việc của hai báo cáo vụ việc

### Q16.1. Quyết định

**Đếm cả vụ việc đã tiếp nhận chưa hoàn thành.** Hai báo cáo này đo khối lượng tiếp nhận, không đo kết quả.

**Mốc "trong kỳ" của cả hai: ngày tiếp nhận.**

### Q16.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 34 | `srs-v3.5.md` — `BR-RPT-01` | Thêm mệnh đề ngoại lệ, liệt kê đích danh ba báo cáo đếm cả bản ghi chưa duyệt: `FR-IX-01`, `FR-IX-02`, `FR-IX-13` |
| 35 | `srs-fr-11-bao-cao.md` — `FR-IX-13` | Ghi tập trạng thái như `FR-IX-02` (trừ từ chối) và mốc ngày tiếp nhận |

---

## Q17. Kết luận thẩm định khi nhóm Pháp lý không đạt

### Q17.1. Quyết định

**Nhận kết luận "Yêu cầu bổ sung".** Nhóm Pháp lý không đạt chỉ khóa kết luận "Đạt", không khóa "Yêu cầu bổ sung" — thiếu giấy tờ đúng là tình huống của trạng thái này.

### Q17.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 36 | `srs-fr-04-chuyen-gia-tvv.md:1625` — `SCR-IV-03` dòng 14 | Sửa thành *"nếu Nhóm 1 Không đạt thì không được kết luận Đạt"* |

---

## Q18. Ba cột tiền của báo cáo chi phí theo quy mô doanh nghiệp

### Q18.1. Quyết định

| Cột | Công thức |
|---|---|
| Tổng chi phí | Tổng **số tiền thực trả** của các hồ sơ đã chi trả trong kỳ thuộc dòng |
| Trần chi phí | Tổng trần năm của **các doanh nghiệp khác nhau** trong dòng; mỗi doanh nghiệp lấy trần đang áp dụng cho địa bàn của mình |
| Chênh lệch | Tổng chi phí − Trần chi phí |

Trần lấy theo **cấu hình mức hỗ trợ đang áp dụng** — hiện là Nghị định 18/2026, địa phương có thể đặt trần riêng. Cụm *"cộng mức hỗ trợ"* trong công thức nghĩa là **hiển thị kèm**, không cộng vào tổng chi phí.

### Q18.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 37 | `srs-fr-11-bao-cao.md:885`–`:887` | Ghi công thức ba cột theo bảng trên |
| 38 | `srs-fr-11-bao-cao.md:861`, `:873`, `:886` | Đổi *"trần chi phí theo NĐ55"* thành *"trần theo cấu hình mức hỗ trợ đang áp dụng"*; làm rõ *"cộng mức hỗ trợ"* là hiển thị kèm. Giữ nguyên `BR-CALC-01`, không chép số vào báo cáo |

---

## Q19. Trường Hình thức tổ chức trên hai biểu mẫu tạo doanh nghiệp

### Q19.1. Quyết định

**Cả hai biểu mẫu nhận trường Hình thức tổ chức, tùy chọn** — biểu mẫu doanh nghiệp tự đăng ký và biểu mẫu cán bộ thêm doanh nghiệp. Trường đặt cạnh ô quy mô trong nhóm Địa lý và Phân loại.

### Q19.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 39 | `srs-fr-10-quan-tri.md` — `FR-VIII-22` · `srs-fr-07-doanh-nghiep.md` — `FR-V.III-NEW-03` và màn `SCR-V.III-03` nhóm B | Bổ sung trường `hinh_thuc_to_chuc_id` (tùy chọn) vào cả hai chức năng và màn hình. Cùng lúc bỏ ô `quy_mo` theo mục 17 |

---

## Q20. Giới hạn dung lượng tệp khi đăng ký tư vấn viên

### Q20.1. Quyết định

Giới hạn **tổng 50 MB tính trên từng ô tệp**, không phải trên cả lần gửi. Mỗi ô: tối đa 10 tệp, mỗi tệp không quá 10 MB, tổng của ô không quá 50 MB.

### Q20.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 40 | `srs-fr-04-chuyen-gia-tvv.md` — `FR-IV-03` ô 17, 21, 23 và dòng lỗi `ERR-DK-05` | Ghi đủ ba giới hạn cho từng ô, trong đó tổng 50 MB mỗi ô; câu lỗi nêu rõ tên ô vượt giới hạn |

---

## Q21. Phạm vi kho câu hỏi của khối gợi ý

### Q21.1. Quyết định

**Lọc theo đơn vị của cán bộ.** Khối gợi ý chỉ lấy bản ghi kho câu hỏi thuộc đơn vị của cán bộ đang xử lý, giống đường tra kho hiện có ở nhóm Tư vấn nhanh.

Quy tắc phân quyền dữ liệu theo đơn vị **giữ đúng ba ngoại lệ hiện có**, không thêm. Ma trận phân quyền và đường tra kho của nhóm Tư vấn nhanh **giữ nguyên**.

Chỗ phải sửa là dòng *"phạm vi toàn quốc"* của khối gợi ý — dòng này trái ma trận phân quyền nên phải bỏ.

> **Điểm treo, ghi nhận để quyết sau.** Gợi ý chỉ trong đơn vị thì cán bộ không thấy câu trả lời cùng nội dung của đơn vị khác, giá trị của chức năng giảm nhiều so với mục tiêu tránh trả lời lại. Mở phạm vi toàn quốc đòi đổi nguyên tắc phân quyền dữ liệu, nên để lại thành một nội dung quyết riêng.

### Q21.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 41 | `srs-fr-02-hoi-dap.md` — `FR-II-12` bảng tiêu chí và bước 4 | Bỏ *"Phạm vi toàn quốc"*; thêm lọc theo đơn vị của cán bộ đang xử lý. Ghi điểm treo về phạm vi ngay tại chỗ |
| 42 | — | **Không thi hành** — giữ nguyên ma trận phân quyền dữ liệu |
| 43 | — | **Không thi hành** — giữ nguyên đường tra kho của nhóm Tư vấn nhanh |

---

## Q22. Ô lĩnh vực pháp luật ở bước tiếp nhận

### Q22.1. Quyết định

**Giữ ô làm đường dự phòng.** Mọi đường tạo hồ sơ hỏi đáp trong hệ thống đều bắt buộc lĩnh vực, kể cả đầu nối từ Cổng — đầu nối còn kiểm tra giá trị tồn tại trước khi tạo. Ô này **chỉ hiện với hồ sơ ngoại lệ**: hồ sơ di trú từ hệ thống cũ và dữ liệu lỗi, nếu không có ô thì hồ sơ kẹt vĩnh viễn ở bước tiếp nhận.

Câu căn cứ hiện hành trong SRS — *"nếu dữ liệu Cổng đẩy sang thiếu thì cán bộ không có đường nào bổ sung"* — **là sai**, phải sửa.

### Q22.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 44 | `srs-fr-02-hoi-dap.md` — `FR-II-03` trường 3 và ghi chú | Sửa câu căn cứ sai; ghi rõ trường 3 chỉ hiện với hồ sơ ngoại lệ |

---

## Q23. Ba trường phân loại khi gắn doanh nghiệp vào hồ sơ ẩn danh

### Q23.1. Quyết định

**Tự điền theo hồ sơ doanh nghiệp tại lúc gắn.** Nguyên tắc: ảnh chụp lấy **tại thời điểm hồ sơ lần đầu xác định được doanh nghiệp**, không phải cứng ở bước tiếp nhận.

Ảnh chụp **chỉ lấy một lần**: hồ sơ đã có giá trị thì đổi doanh nghiệp về sau không ghi đè.

### Q23.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 45 | `srs-fr-02-hoi-dap.md` — `FR-II-01` phần Chỉnh sửa | Thêm một bước: khi trường doanh nghiệp đổi từ trống sang có giá trị, điền ba trường phân loại theo hồ sơ doanh nghiệp đó; đã có giá trị thì không ghi đè |
| 46 | `srs-v3.5.md`, `srs-fr-02-hoi-dap.md`, `srs-fr-11-bao-cao.md:183` | Ba chỗ dùng cụm *"tại thời điểm tiếp nhận"* sửa thành *"tại thời điểm lần đầu xác định được doanh nghiệp"*; giữ vế không đọc động sang hồ sơ doanh nghiệp về sau |

---

## Q24. Tính duy nhất của số thẻ hành nghề

### Q24.1. Quyết định

**Không ràng buộc duy nhất.** Hai hồ sơ tư vấn viên mang cùng số thẻ hành nghề vẫn lưu được. Chỉ số định danh cá nhân và thư điện tử chặn trùng như hiện nay.

Đây là **lệch có chủ đích**, ghi rõ trong đặc tả để bộ phận kiểm thử chấm đúng và để lượt rà sau không mở lại.

> **Điểm treo, ghi nhận để quyết sau.** Thẻ tư vấn viên pháp luật cấp cho từng người theo Điều 20 Nghị định 77/2008 và là căn cứ thẩm định, nên hai hồ sơ cùng số thẻ vẫn là dữ liệu đáng ngờ. Thêm ràng buộc duy nhất là đặt một ràng buộc mới lên dữ liệu đang có, phải rà dữ liệu hiện trạng trước — để lại thành một nội dung quyết riêng.

### Q24.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 47 | `srs-fr-04-chuyen-gia-tvv.md` — cột số thẻ của `HO_SO_TU_VAN_VIEN` | Ghi rõ: **không ràng buộc duy nhất**, hai hồ sơ cùng số thẻ lưu được; kèm điểm treo |
| 48 | — | **Không thi hành** — không thêm mã lỗi trùng số thẻ |

---

## Q25. Mốc xếp hồ sơ vào kỳ của báo cáo hỏi đáp

### Q25.1. Quyết định

**Kỳ theo ngày tạo bản ghi hỏi đáp. Nhóm theo trạng thái tại thời điểm chạy báo cáo.**

Một hồ sơ chỉ thuộc đúng một kỳ suốt vòng đời. Kỳ đã khép **có thể ra số khác khi in lại** nếu hồ sơ đổi trạng thái về sau — đúng cơ chế đối chiếu lại khi mở báo cáo.

### Q25.2. Sửa trong SRS

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 49 | `srs-fr-11-bao-cao.md` — `FR-IX-01` | Ghi mốc xếp kỳ và thời điểm đọc trạng thái; hai ô lọc ngày ghi rõ so với ngày tạo bản ghi. Ghi rõ kỳ đã khép có thể ra số khác khi in lại |

---

# Phần C — Hai mươi bảy mục sửa tài liệu

Toàn bộ tiếp nhận, không mục nào tranh chấp. Mỗi mục sửa đúng nội dung nêu ở cột Nội dung.

| # | Mã | Nội dung phải sửa | Tệp |
|---|---|---|---|
| 50 | D1 | Tiêu chí chấp nhận của `FR-VIII-33` đang là nội dung của danh mục Loại sự kiện đào tạo — chép nhầm nguyên khối. Viết lại hoàn toàn cho danh mục Hình thức tổ chức | `srs-fr-10-quan-tri.md` |
| 51 | D2 | Bảng thuộc tính `HOI_DAP` ở tệp nhóm thiếu ba cột `quy_mo_dn_id`, `hinh_thuc_to_chuc_id`, `tinh_thanh_dn_id`; tệp nền đã có | `srs-fr-02-hoi-dap.md` |
| 52 | D3 | `FR-II-01` trường 7 và `FR-II-11` trường 2 gọi `doanh_nghiep_id`, bảng `HOI_DAP` dùng tên cột `nguoi_gui_id`. Thống nhất theo tên cột ở tệp nền | `srs-fr-02-hoi-dap.md`, `srs-v3.5.md` |
| 53 | D4 | Dòng khởi tạo vụ việc `[*] → CHO_TIEP_NHAN` thiếu nguồn `FR-II-11` và ghi "tính deadline" lúc tạo — trái quy tắc tính thời hạn từ lúc tiếp nhận | `srs-fr-05-vu-viec.md` |
| 54 | D5 | `FR-IV-03` bước 7 thiếu năm trường mới (số thẻ, tệp thẻ, hai loại minh chứng, số vụ việc tự kê khai); tiêu chí chấp nhận vẫn ghi "form đăng ký mở với 21 trường" | `srs-fr-04-chuyen-gia-tvv.md` |
| 55 | D6 | `FR-IX-13` đã đổi tên "theo quy mô DN" nhưng Mô tả và tiêu chí chấp nhận vẫn ghi "loại doanh nghiệp" | `srs-fr-11-bao-cao.md` |
| 56 | D7 | Thiếu mã lỗi và câu thông báo cho: xóa trắng tiêu đề hoặc mô tả khi chuyển; ghi chú chuyển quá 2.000 ký tự; loại hình hỗ trợ ngoài danh mục; chuyển thành công; không tích ô đối chiếu địa bàn | `srs-fr-02-hoi-dap.md` |
| 57 | D8 | `FR-V.I-18` phần Inputs và bước 4 ghi "tiếp nhận (`FR-V.I-02`)", nhưng `FR-V.I-02` là chức năng doanh nghiệp gửi hồ sơ. Bảng chuyển trạng thái gán bước tiếp nhận cho `FR-V.I-01` — sửa theo bảng chuyển trạng thái | `srs-fr-05-vu-viec.md` |
| 58 | D10 | Thiếu mã lỗi và câu thông báo ở các chức năng khác của đợt này. **Dữ liệu sai:** lĩnh vực không thuộc danh mục khi tiếp nhận; ba trường phân loại hoặc hình thức tổ chức trỏ sai loại danh mục; lý do kiểm tra hồ sơ dưới 10 hoặc trên 5.000 ký tự; phía gửi tự đặt loại lý do từ chối; số thẻ quá 50 ký tự; tệp thẻ không phải PDF; quá 10 tệp minh chứng; số vụ việc tự kê khai âm; cán bộ nhập tay kênh `CONG_PLQG` hoặc tự gắn liên kết truy nguồn khi lập vụ việc. **Bị từ chối do phân quyền:** vai trò không phải cán bộ nghiệp vụ chuyển hồ sơ; vai trò không phải cán bộ nghiệp vụ đọc gợi ý; tư vấn viên tự sửa hồ sơ năng lực | `srs-fr-02-hoi-dap.md`, `srs-fr-05-vu-viec.md`, `srs-fr-04-chuyen-gia-tvv.md`, `srs-fr-07-doanh-nghiep.md` |
| 59 | D11 | Hai dòng khối "Nguồn gốc hồ sơ" và dòng "Thời gian xử lý toàn trình" nằm trong bảng của màn Thêm mới, trong khi hai nội dung này thuộc màn chi tiết. Nêu rõ dòng thời gian toàn trình có hiện với vụ việc tiếp nhận trực tiếp không | `srs-fr-05-vu-viec.md` |
| 60 | D12 | `FR-II-01` không có ô nhập tiêu đề, trong khi bảng `HOI_DAP` có cột tiêu đề bắt buộc và `FR-II-11` chép tiêu đề sang vụ việc. Nêu rõ tiêu đề sinh từ đâu | `srs-fr-02-hoi-dap.md` |
| 61 | D13 | Bảng "Thông báo khi chuyển luồng" nằm trong `FR-II-01`, trong khi `FR-II-11` bước 11 dẫn "theo bảng dưới" — người đọc `FR-II-11` không thấy bảng. Chuyển bảng về `FR-II-11` hoặc dẫn chiếu tường minh | `srs-fr-02-hoi-dap.md` |
| 62 | D14 | Dòng người nhận "Cán bộ Nghiệp vụ của đơn vị thụ lý" ghi hai cách xác định tập khác nhau. Thống nhất: theo đơn vị của vụ việc mới | `srs-fr-02-hoi-dap.md` |
| 63 | D15 | Nhóm người nhận thứ ba ghi "Người hỗ trợ pháp lý hoặc Tư vấn viên", nhưng hỏi đáp chỉ phân công cho cán bộ nghiệp vụ hoặc người hỗ trợ pháp lý. Thống nhất theo trường người được phân công | `srs-fr-02-hoi-dap.md`, `srs-v3.5.md` |
| 64 | D16 | Bước chỉnh sửa hỏi đáp chưa chặn trạng thái Đã chuyển luồng, dù bước Xóa, quy tắc chuyển luồng, nút Sửa và ma trận quyền đã chặn. Câu của `ERR-HD-04` vẫn là "Không thể sửa/xóa bản ghi đã phê duyệt" dù nay dùng cho cả hồ sơ đã chuyển | `srs-fr-02-hoi-dap.md` |
| 65 | D17 | Huy hiệu "Từ Hỏi đáp" trên màn danh sách vụ việc mở hồ sơ gốc mà không có điều kiện cùng đơn vị như quy tắc của `FR-V.I-18` | `srs-fr-05-vu-viec.md` |
| 66 | D18 | Điều kiện cùng đơn vị ở `FR-V.I-18` và khối "Nguồn gốc hồ sơ" không nêu ngoại lệ Cán bộ Trung ương và Quản trị hệ thống — ngoại lệ chỉ nằm ở ghi chú bên dưới. Đưa vào chính bước xử lý | `srs-fr-05-vu-viec.md` |
| 67 | D19 | Lặp chữ "(§Processing bước 6) (bước 6)" | `srs-fr-05-vu-viec.md` |
| 68 | D20 | `FR-V.I-12` trường 2 liệt hai nhãn loại lý do, thiếu "Lý do khác" mới thêm ở `FR-V.I-06` | `srs-fr-05-vu-viec.md` |
| 69 | D21 | Cụm "Hạng mục 2–7" và "cả bảy hạng mục" viết cứng, trong khi Quản trị hệ thống thêm bớt được thành phần hồ sơ. Viết lại theo cách không phụ thuộc số lượng | `srs-fr-05-vu-viec.md` |
| 70 | D22 | Bước 4b chỉ khóa kết luận khi hạng mục 1 không đạt; chưa nói trường hợp hạng mục 1 đạt nhưng có hạng mục khác không đạt mà chọn Đạt. Tiêu chí chấp nhận chưa có ba ca 4a, 4b, 4c | `srs-fr-05-vu-viec.md` |
| 71 | D23 | Cùng một ràng buộc thẻ hành nghề có ba mã lỗi cùng câu ở ba chức năng; màn `SCR-IV-02` chỉ ghi hai mã. Thống nhất cách dùng và ghi đủ mã ở tiêu chí chấp nhận | `srs-fr-04-chuyen-gia-tvv.md` |
| 72 | D24 | `FR-IX-18` gom theo quy mô trên hồ sơ doanh nghiệp hiện tại, trong khi hồ sơ chi trả có cột ảnh chụp quy mô dùng để xác định mức hỗ trợ; hai giá trị có thể khác nhau. Nêu rõ báo cáo dùng cột nào | `srs-fr-11-bao-cao.md` |
| 73 | D25 | `FR-IX-01` ghi báo cáo dùng "ảnh chụp tại thời điểm tiếp nhận", nhưng câu hỏi ẩn danh được điền ba trường lúc chuyển luồng. Sửa theo quyết định tại **Q23** | `srs-fr-11-bao-cao.md` |
| 74 | D26 | Bảng chuyển trạng thái vụ việc thiếu dòng phân công lại sau khi người được phân công từ chối, dù chức năng lựa chọn người hỗ trợ cho phép | `srs-fr-05-vu-viec.md` |
| 75 | D28 | Dòng mở lại vụ việc từ trạng thái Từ chối dẫn một mã chức năng chưa tồn tại | `srs-fr-05-vu-viec.md` |
| 76 | D29 | Bước 3a "giữ nguyên các hạng mục đã tích" chưa nói hạng mục đã đánh "không đạt" có tính là đã tích không | `srs-fr-05-vu-viec.md` |
