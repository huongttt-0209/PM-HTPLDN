# Phát hiện thêm — ngoài tiêu chí (reverify round 7, 2026-07-25)

Ghi theo BRIEF §3 bước 6. Chỉ ghi những gì quan sát được trên ảnh đã mở đọc + đo lại bằng DOM, KHÔNG suy đoán. **Không mở dòng TC mới trên sheet.**

Người kiểm: QA · tài khoản `cbnv_tw_04` (CB Nghiệp vụ Trung ương) · Chrome DevTools MCP.

---

## 🔴 KẾT QUẢ KIỂM CHỨNG ĐỐI KHÁNG (25/07/2026, sau khi lập §1–§9) — ĐỌC TRƯỚC CÁC MỤC DƯỚI

5 mục §4–§9 đã được kiểm chứng lại theo hướng **cố bác bỏ**. Kết quả: **3/5 mục ban đầu quy kết SAI**. Các mục dưới giữ nguyên văn bản gốc để đối chiếu, nhưng phải đọc kèm bảng này:

| Mục | Nhãn sau kiểm chứng | Đính chính |
|---|---|---|
| §4 | **REWORD — sai phạm vi** | KHÔNG phải lỗi module Biểu mẫu. Hỏng ở **mọi module có tệp lưu trong kho đối tượng** (đã tái hiện ở Đào tạo → Kho tài liệu/Bài giảng: khung xem trước trắng, cùng lỗi Mixed Content). Ngược lại tệp do ứng dụng tự sinh vẫn tải bình thường (Xuất Excel Chi trả 7.579 B, Xuất Excel Báo cáo 6.541 B, đều qua https). → **Lỗi cấu hình triển khai**, chuyển đội hạ tầng. Không mở dòng bug UAT chức năng. |
| §5 | **REWORD — ngược hướng** | Dropdown **KHÔNG sai**. SRS `BR-AUTH-04` (`srs-v3.5.md:5439`): *"TW thấy toàn bộ dữ liệu TW + BN + ĐP… TW query toàn quốc; BN/ĐP query chỉ đơn vị mình"*. Đối chiếu thực tế: TW thấy 13 thư mục, BN chỉ thấy 3 của đơn vị mình → dropdown đang lọc ĐÚNG theo vai trò. Điểm chưa rõ là **phạm vi GHI** — SRS im lặng. Ghi chú thêm: `ERR-BM-05` trong SRS `srs-fr-09-bieu-mau.md:357` = "Thư mục đích không tồn tại", app lại nói "…hoặc không thuộc đơn vị". → Tester quyết **bỏ qua**, không mở dòng bug, không mở phiếu BA. |
| §6 | **CONFIRMED** | Đã chứng minh nhân quả trên 3 biểu mẫu mới, 5/5 lần. → **đã mở dòng `QLBMHD_OOS_01` (dòng 309)** trên tab "UAT_TGPL Doanh Nghiệp-tuần 3" ngày 25/07/2026. |
| §8 | **CONFIRMED** | Đo cô lập: thêm riêng `qa-loi.txt` → số dòng không đổi, `SO_KHUNG_THONG_BAO = 0`. → **đã mở dòng `IBMHD_OOS_01` (dòng 310)** ngày 25/07/2026. |
| §9 | **REWORD — sai điều kiện kích hoạt** | Thu hẹp bình thường (1440→1400) **không mất gì**. Chỉ mất khi bề ngang **tụt dưới 1024px**: app tự hiện màn *"Màn hình không được hỗ trợ — vui lòng dùng màn hình ≥ 1024px"* và gỡ toàn bộ trình nhập; mở rộng lại thì dựng mới ở bước 1 trắng. Ngưỡng chốt 1024px bình thường / 1023px hiện màn chặn. → Tester quyết **không log**. |

Ảnh kiểm chứng: [`kiem-chung/`](kiem-chung/).

**Bài học:** §4 nếu ghi nguyên như bản nháp sẽ đẩy dev đi sửa nhầm module; §5 sẽ khiến dev lọc dropdown và phá quyền toàn quốc của cán bộ TW; §9 sẽ bị đóng nhầm "không tái hiện" vì dev thử 1440→1400. Phát hiện tình cờ phải qua kiểm chứng đối kháng trước khi ghi sheet.

---

## 1. Bộ lọc không tự áp dụng khi chọn — phải bấm [Tìm kiếm]

**Màn:** cả `/bieu-mau/danh-sach` và `/bieu-mau/thu-muc`.

**Quan sát:** chọn xong giá trị trong ô lọc (vd Định dạng = DOCX) thì danh sách **giữ nguyên** — đo sau 2,5 s và sau 5,5 s đều vẫn `Hiển thị 1-14 / 14 kết quả`. Chỉ khi bấm nút **[Tìm kiếm]** thì URL mới đổi thành `?dinhDang=DOCX&page=1` và danh sách rút về `1-12 / 12`.

**Kết luận: KHÔNG phải lỗi.** Màn có sẵn nút [Tìm kiếm] và nút [Xóa bộ lọc] ngay cạnh bộ lọc, nên đây là cách vận hành có chủ đích chứ không phải bộ lọc chết.

**Vì sao vẫn ghi lại:** người kiểm ở lượt sau nếu chỉ chọn giá trị rồi đọc số bản ghi ngay sẽ thấy số không đổi và dễ kết luận nhầm là "bộ lọc không chạy". Cần bấm [Tìm kiếm] rồi mới đọc số.

---

## 2. Cột "Hành động" che 3 cột bên trái khi mới mở màn (đã kiểm — không phải lỗi)

**Màn:** `/bieu-mau/thu-muc` (và cùng kiểu ở `/bieu-mau/danh-sach`), cửa sổ rộng 1440.

**Quan sát ban đầu trên ảnh:** cột "Trạng thái" bị cắt còn "Trạ...", phần dữ liệu trạng thái chỉ thấy một chấm màu rồi bị khối "Hành động" đè lên.

**Đo lại bằng DOM:** bảng rộng `scrollWidth = 1600` trong khung `clientWidth = 1128` nên có thanh cuộn ngang. Cột "Hành động" là cột ghim phải (`ant-table-cell-fix-end-sticky`, x 1079→1408). Lúc `scrollLeft = 0`, ba cột Trạng thái (1056→1221), Đồng bộ (1221→1386), Ngày tạo (1386→1551) nằm dưới vùng cột ghim.

**Kiểm tiếp:** cuộn ngang hết cỡ (`scrollLeft = 472`) thì cả ba cột hiện đầy đủ, không còn chồng lấn — Trạng thái 584→749, Đồng bộ 749→914, Ngày tạo 914→1079, Hành động 1079→1408.

**Kết luận: KHÔNG phải lỗi.** Dữ liệu không mất, chỉ cần cuộn ngang là đọc được. Đây là cách bảng có cột ghim phải hoạt động bình thường.

---

## 3. Không có bất thường nào khác — trong phạm vi 2 case TKBMHD_03 · TKTMBMHD_04

Ngoài 2 mục trên, không quan sát thấy chữ lạ, chữ tiếng Anh lẫn vào, giá trị `null` / `undefined`, thông báo lỗi, hay dữ liệu tràn/đè trong toàn bộ 11 ảnh đã chụp và mở đọc của 2 case đó.

*(Các mục 4–7 dưới đây phát hiện ở lô sau: QLTMBMHD_20 · QLBMHD_13 · QLBMHD_08.)*

---

## 4. 🔴 Không tải được tệp biểu mẫu về máy — hỏng ở CẢ 3 chỗ bấm tải (phát hiện khi làm QLBMHD_13)

**Màn:** `/bieu-mau/danh-sach` (dòng), `/bieu-mau/{id}` (Chi tiết), `/bieu-mau/{id}/sua` (form Sửa). Bản ghi đo: `BM-20260725-003`, tệp `qa-edit-src.docx` 931 B.

**Quan sát:** bấm nút tải ở bất kỳ chỗ nào trong 3 chỗ trên thì **yêu cầu CÓ tới máy chủ** (trường "Số lượt tải" của bản ghi tăng đều 1 → 2 → 3 → 4) nhưng **tệp không bao giờ về máy**. Đã rà toàn bộ thư mục Tải về, Màn hình, thư mục tạm — không có tệp nào.

| Chỗ bấm tải | Máy chủ có được gọi? | Tệp về máy? |
|---|---|---|
| Nút "Tải tập tin" trên form Sửa | ✅ số lượt tải 1 → 2 | ❌ |
| [Tải về] màn Chi tiết | ✅ 2 → 3 | ❌ |
| [Tải về] trên dòng Danh sách | ✅ 3 → 4 | ❌ |

**Nguyên nhân đo được (console trình duyệt):** trang chạy `https://18.143.165.120.nip.io`, nhưng máy chủ chuyển hướng lệnh tải sang địa chỉ kho tệp dùng **`http://18.143.165.120:9000/...`**. Trình duyệt chặn vì trang an toàn không được phép lấy tài nguyên qua kênh không an toàn:

> `Mixed Content: The page at 'https://18.143.165.120.nip.io/bieu-mau/…/sua' was loaded over HTTPS, but requested an insecure resource 'http://18.143.165.120:9000/htpldn/…/qa-edit-src.docx?...'. This request has been blocked; the content must be served over HTTPS.`

**Kiểm chứng tệp KHÔNG hỏng:** tải thẳng địa chỉ kho tệp (không qua trình duyệt) → `HTTP 200`, `931 byte`, đúng kiểu .docx, **SHA-256 trùng 100%** tệp gốc `qa-edit-src.docx`. Vậy tệp lưu trong hệ thống hoàn toàn nguyên vẹn; vấn đề nằm ở **cấu hình địa chỉ kho tệp (http) lệch với địa chỉ ứng dụng (https)**.

**Vì sao KHÔNG tính vào QLBMHD_13:** lỗi giống hệt nhau ở cả 3 chỗ tải, kể cả những chỗ chưa từng nằm trong phạm vi phiếu này ⇒ là vấn đề chung của môi trường triển khai, không phải lỗi của form Sửa. Bar chấm QLBMHD_13 yêu cầu form Sửa "có lối tải tệp ngay trên form" — điều đó đã có (tên tệp bấm được + nút tải riêng). Ghi ở đây để đội dự án xử lý riêng; **không tự mở dòng TC mới trên sheet**.

**Đề nghị:** đội triển khai cấu hình kho tệp phát địa chỉ `https` (hoặc cho ứng dụng phát tệp trực tiếp thay vì chuyển hướng sang cổng 9000), rồi kiểm lại 3 chỗ tải trên.

---

## 5. Danh sách chọn Thư mục ở form Thêm biểu mẫu có cả thư mục của đơn vị khác

**Màn:** `/bieu-mau/them-moi`, ô **Thư mục**. Tài khoản `cbnv_tw_04` (Trung ương).

**Quan sát:** ô Thư mục liệt kê cả `QA-IMPORT-KQ` và `BM-B6-BN-Import-20260720` — hai thư mục thuộc **đơn vị khác** (Bộ ngành). Chọn `QA-IMPORT-KQ`, điền đủ thông tin rồi bấm [Thêm mới] thì máy chủ từ chối:

> `ERR-BM-05` — **"Thư mục biểu mẫu không tồn tại hoặc không thuộc đơn vị"**

**Đánh giá:** máy chủ chặn ĐÚNG (không cho tạo biểu mẫu vào thư mục đơn vị khác). Vấn đề là **giao diện vẫn mời người dùng chọn** thư mục mà chắc chắn sẽ bị từ chối — người dùng điền xong cả form mới biết mình chọn sai, và câu thông báo cũng không chỉ ra thư mục nào sai.

**Đề nghị:** lọc danh sách thư mục theo đúng đơn vị của người đang đăng nhập (hoặc hiển thị mờ/kèm tên đơn vị) để tránh chọn nhầm.

---

## 6. Bấm tải tệp làm tăng "phiên bản" bản ghi → form Sửa đang mở bị từ chối lưu

**Màn:** `/bieu-mau/{id}/sua`. Bản ghi `BM-20260725-003`.

**Quan sát:** mở form Sửa → bấm nút tải tệp ngay trên form → sửa Tên biểu mẫu → bấm [Lưu] thì bị từ chối với thông báo:

> **"Bản ghi đã được người khác cập nhật trong lúc bạn thao tác."**

Thực tế **không có người nào khác** thao tác. Nguyên nhân: mỗi lần bấm tải, hệ thống tăng "Số lượt tải" của bản ghi, kéo theo **số phiên bản của bản ghi tăng** (1 → 2 → 3). Form Sửa đang giữ số phiên bản lúc mở nên bị coi là cũ.

**Kiểm chứng:** tải lại form Sửa (lấy phiên bản mới) rồi sửa tên và lưu **không** bấm tải → **"Cập nhật biểu mẫu thành công"** ngay.

**Đánh giá:** thao tác chỉ ĐỌC (tải tệp về) không nên làm người dùng mất công sửa. Câu thông báo cũng dễ gây hiểu nhầm là có người khác đang sửa cùng bản ghi.

**Đề nghị:** không tính lượt tải vào phiên bản dùng để kiểm tra tranh chấp khi lưu; hoặc form tự cập nhật lại phiên bản sau khi người dùng bấm tải.

**Dựng lại trên bản ghi mới (25/07/2026 14:40–14:48, tài khoản CB Nghiệp vụ - Trung ương):** bản ghi `BM-20260725-008 · R7-EVID-S6-BM01`, thư mục `QA-R7-A-CO-BM`, tệp `qa-ok-1.docx`.

| Bước | Thao tác | Phiên bản trước → sau | Số lượt tải trước → sau | Kết quả bấm [Lưu] |
|---|---|---|---|---|
| Đối chứng | Mở Sửa → **KHÔNG** bấm tải → đổi Tên → [Lưu] | 1 → 2 | 0 → 0 | ✅ Lưu được (Tên đổi thành `… CTRL-khong-tai`) |
| Phép thử | Mở Sửa → bấm tải **1 lần** → đổi Tên → [Lưu] | 2 → 3 (chỉ do bấm tải) | 0 → 1 | ❌ Bị từ chối |
| Lặp lại | Mở Sửa → bấm tải **1 lần** → đổi Tên → [Lưu] | 3 → 4 (chỉ do bấm tải) | 1 → 2 | ❌ Bị từ chối |

Số khung thông báo = 1, số yêu cầu gửi đi = 1, nguyên văn: **"Bản ghi đã được người khác cập nhật trong lúc bạn thao tác."** Tên biểu mẫu sau khi bị từ chối vẫn là `R7-EVID-S6-BM01 CTRL-khong-tai` — sửa đổi bị mất.

**Bằng chứng:**
- [Khung thông báo từ chối lưu](kiem-chung/s6-EVID-01-khung-thong-bao-tu-choi-luu.png)
- [Màn Chi tiết: Số lượt tải = 2, tên chưa lưu](kiem-chung/s6-EVID-02-chi-tiet-so-luot-tai-2-ten-chua-luu.png)

---

## 7. Tồn dư từ lượt đo trước: biểu mẫu chứa chuỗi thử mã độc vẫn còn trong hệ thống

**Màn:** `/bieu-mau/danh-sach`, tìm từ khóa `eicar`.

**Quan sát:** còn 1 bản ghi **`BM-20260720-006 · QA-eicar-malware-test-row101`** (tệp `QA-eicar-malware-test-row101.docx`, 1028 B, **ngày tạo 20/07/2026**) nằm trong "Thư mục biểu mẫu seed". Đây là bản ghi sinh ra ở lượt đo 20/07 — thời điểm bộ quét CHƯA chặn nên tệp chứa chuỗi thử diệt virus (EICAR) được lưu vào kho.

**Đánh giá:** không phải lỗi mới — nay hệ thống đã chặn đúng (xem QLBMHD_08). Nhưng tệp cũ **vẫn nằm trong kho** và vẫn tải được, tức bản vá chỉ chặn từ thời điểm sửa trở đi, không rà soát dữ liệu đã lưu trước đó.

**Đề nghị:** đội dự án rà quét lại các tệp đã lưu trước khi bật bộ quét và gỡ bản ghi thử này khỏi môi trường.

---

## 8. Bước "Chọn file" giấu tệp sai định dạng, mẫu số dòng đếm không khớp số tệp người dùng đã chọn

**Màn:** `/bieu-mau/nhap-hang-loat`, bước 1 (phát hiện khi làm IBMHD_07).

**Quan sát:** chọn 4 tệp trong 1 lượt (`qa-ok-1.docx`, `qa-ok-2.docx`, `qa-loi.txt`, `qa-hong.docx`):

- Danh sách tệp ở bước 1 chỉ hiện **3** dòng — `qa-loi.txt` bị bỏ hẳn, **không có dòng nào, không có thông báo nào**.
- Dòng đếm ghi **"Đã tải lên thành công: 2/3 · Có file lỗi"** — mẫu số là 3, trong khi người dùng đã chọn 4 tệp.
- Sang bước 2 thì hệ thống lại đếm đủ: **"Tổng số file 4 · Hợp lệ 2 · Lỗi 2"**, và `qa-loi.txt` có mặt kèm lý do. Màn Kết quả cũng đếm đủ 2 tệp lỗi.

**Đánh giá:** không ảnh hưởng kết quả chấm IBMHD_07 (bước Kiểm tra và màn Kết quả đều đúng). Nhưng ở bước 1 người dùng chọn 4 tệp mà chỉ thấy 3, lại không được báo tệp thứ tư đi đâu — dễ tưởng bấm hụt. Mẫu số "2/3" cũng lệch với số tệp thực đã chọn.

**Đề nghị:** ngay ở bước chọn tệp, hiện luôn dòng cho tệp sai định dạng kèm lý do (như bước Kiểm tra đang làm), và tính nó vào mẫu số dòng đếm.

---

## 9. Đổi kích thước cửa sổ khi đang nhập hàng loạt làm mất sạch tệp đã chọn, quay về bước 1

**Màn:** `/bieu-mau/nhap-hang-loat` (phát hiện khi làm IBMHD_07).

**Quan sát:** đang ở **bước 2 (Kiểm tra)** với thư mục đích `QA-IMPORT-R7` và 4 tệp đã nạp xong, chỉ cần đổi kích thước khung nhìn trình duyệt là toàn bộ trình nhập **nhảy về bước 1 ở trạng thái trắng**: ô Thư mục đích trở lại "Chọn thư mục", danh sách tệp rỗng, dòng đếm về "Đã tải lên thành công: 0/0". Không có cảnh báo, không hỏi xác nhận. Trang **không** tải lại (đối tượng theo dõi cài trong trang vẫn còn sống) — tức là dữ liệu bị xóa ở phía giao diện chứ không phải do mất phiên.

**Đánh giá:** người dùng phải chọn lại thư mục và tải lại từ đầu toàn bộ tệp. Với lô nhiều tệp (hệ thống cho tới 50 tệp/lần) thì mất khá nhiều công. Việc phóng to/thu nhỏ cửa sổ, xoay màn hình máy tính bảng, hay mở thêm thanh công cụ đều là thao tác bình thường.

**Đề nghị:** giữ nguyên thư mục đích và danh sách tệp đã tải khi cửa sổ đổi kích thước; nếu buộc phải làm lại thì báo trước cho người dùng.
