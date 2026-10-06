# Postmortem — QA chạy 16 case mà không thấy lỗi hiện ngay trên màn hình (16/07/2026)

**Người viết:** QA Automation (Claude Code) · **Người phát hiện:** user · **Phạm vi ảnh hưởng:** đợt verify 16 case dev-fix, tab `UAT_TGPL Doanh Nghiệp-tuần 2`.

> **Mục đích file này:** trả lời câu hỏi *"tại sao thấy bug mà không báo cho dev?"* — và chốt phương án để lần sau không lặp.
> **Đọc kèm:** [QA_VERIFY_PROTOCOL.md](QA_VERIFY_PROTOCOL.md) · công cụ [tools/toast-capture.js](tools/toast-capture.js)

---

## 1. Chuyện gì đã xảy ra

Sau khi QA báo verify xong 16 case, user mở chính cửa sổ trình duyệt của phiên QA và **nhìn thấy ngay** hai thông báo "Tạo khóa học thành công" chồng lên nhau. QA chạy suốt 16 case, tạo khóa học nhiều lần, **không hề phát hiện**.

Rà lại theo phản ánh của user thì ra 3 kết quả:

| Việc | Kết luận sau khi rà | Trạng thái |
|---|---|---|
| Thông báo lặp khi tạo khóa học | **Lỗi thật**, tái hiện 3/3. 1 request → 2 khung thông báo, cách nhau 2ms, chỉ tạo 1 bản ghi | Đã log → sheet dòng 113, `QLKH_02` |
| Xóa khóa học báo "Lỗi hệ thống" | **Lỗi thật**, tái hiện 2/2. `DELETE /api/v1/khoa-hocs/{id}` → HTTP 500, `ERR-SYS-00-00-01` | Đã log → sheet dòng 112, `QLKH_01` |
| "Chữ lặp" trong hộp thoại Trình phê duyệt | **KHÔNG phải lỗi** — do chính công cụ đo của QA đọc sai | Không log (đã chứng minh 4 cách) |

---

## 2. Nguyên nhân THẬT — và một đính chính

**Đính chính trước, vì nó đổi bản chất vấn đề:** QA **không** thấy rồi bỏ qua. QA **mù** trước nó. Điều này **không nhẹ hơn** — nó **nặng hơn**, vì "thấy mà bỏ qua" là một lần lười, còn "mù" là **sai có hệ thống**: nó tự tin, im lặng, và lặp lại ở mọi case.

Với **lỗi xóa khóa học** thì thậm chí không có chuyện "thấy": QA chưa từng bấm xóa khóa học trong 16 case — chỉ chạm tới nó khi đi dọn dữ liệu test.

Với **lỗi thông báo lặp** — nó **đã hiện trên màn hình trong phiên của QA**. Ảnh user gửi chụp từ chính cửa sổ đó. Bốn tầng nguyên nhân, từ ngọn xuống gốc:

### Tầng 1 — Trực tiếp: một dòng lọc trùng

```js
if (t && !window.__t.includes(t)) { window.__t.push(t); window.__pin(t); }
```

Hai thông báo giống hệt nhau bị gộp thành một. Viết dòng này để các thẻ ghim không đè nhau. **Đây chỉ là triệu chứng.**

### Tầng 2 — Gốc: đo để KHẲNG ĐỊNH điều mình đi tìm, không phải để QUAN SÁT điều đang xảy ra

Bộ đo được viết chỉ nhằm trả lời *"có hiện đúng câu chữ X không?"*. Với câu hỏi đó, lọc trùng nghe rất hợp lý — có/không thì cần gì đếm.

Nhưng **QA phải quan sát cái đang xảy ra, không chỉ cái mình đi tìm.** Phép đo được thiết kế quanh câu trả lời mong đợi sẽ **bóp méo dữ liệu trong im lặng**: không cảnh báo, không dấu vết, và cho ra đúng kết quả mình muốn thấy.

Cùng một gốc bệnh sinh ra lỗi ngược lại — **suýt log bug ma**: dùng `textContent` để đọc chữ, nó gom cả node ẩn dành cho trình đọc màn hình (`.ant-modal-title` ẩn + `.ant-modal-confirm-title` hiện) → tưởng chữ bị lặp. Một phép đo sai vừa **giấu lỗi thật**, vừa **đẻ ra lỗi giả**.

### Tầng 3 — Gốc: coi bước seed là "không phải test"

Thao tác bị lỗi (**tạo khóa học**) là bước **seed** để dựng dữ liệu cho `KTDGKQHT_03`, không thuộc case nào. Nó được chạy như thủ tục hành chính để có dữ liệu, không soi.

⇒ **Kể cả không có dòng lọc trùng ở Tầng 1, lỗi này vẫn có thể bị bỏ qua** vì "không thuộc phạm vi". Đây là lỗi tư duy, không phải lỗi code:

> **Mọi thao tác chạy trên phần mềm đều là bề mặt quan sát được — seed hay không seed.**
> Phần mềm không biết đâu là "bước chuẩn bị" của QA. Nó lỗi ở mọi nơi như nhau.

### Tầng 4 — Gốc: toàn bộ nhận thức về phần mềm đi qua `evaluate_script`, gần như không qua mắt

Ở các bước seed hầu như không chụp và không nhìn màn hình. Script sai một chỗ là mù chỗ đó.

**Bằng chứng đắt nhất của postmortem này:** user liếc màn hình **một giây** là thấy 2 cái toast. QA chạy **16 case** thì không. Khác biệt không nằm ở năng lực — nằm ở chỗ **một bên nhìn màn hình, một bên chỉ đọc số liệu do chính mình sinh ra.**

### Vì sao không có lưới an toàn nào bắt lại

Quy trình hiện có **rất chặt** về việc chấm verdict: 3 cổng, bảng đối chiếu điều kiện, gate bằng chứng, guard ghi sheet. Nhưng **không có một dòng nào** yêu cầu:

> "Gặp gì bất thường ngoài phạm vi case thì phải ghi lại."

Nên khi phạm vi = 16 case, **mọi thứ ngoài đó rơi khỏi tầm nhìn một cách có hệ thống** — không phải sơ suất một lần. Quy trình tối ưu cho "chấm đúng case được giao", không tối ưu cho "phát hiện phần mềm đang hỏng chỗ nào".

---

## 3. Phương án xử lý — xếp theo MỨC CƯỠNG CHẾ

> 🔴 **Nói thẳng: viết thêm quy tắc KHÔNG phải là xử lý triệt để.** Thứ vừa hỏng chính là "có quy tắc chặt chỗ này, không có quy tắc chỗ kia". Thêm một tài liệu nữa mà không đổi **hành vi mặc định** thì lần sau lặp lại y hệt.
> Vì vậy phương án chia 3 mức. **Mức A mới là thật.** Mức C là yếu nhất và được ghi ra chỉ để làm mốc tham chiếu chung.

### Mức A — Đổi hành vi MẶC ĐỊNH (mạnh nhất: làm đúng mà không cần nhớ)

| # | Việc | Trạng thái |
|:-:|---|---|
| **A1** | **Bộ bắt thông báo dùng chung** [tools/toast-capture.js](tools/toast-capture.js): **bỏ lọc trùng** · đọc bằng `innerText` (chỉ chữ nhìn thấy) · **đếm số request song song với số thông báo**. Cấm tự viết observer mới. | ✅ Đã làm 16/07 |
| **A2** | **Chụp màn hình ở MỌI thao tác đổi trạng thái — kể cả bước seed — và PHẢI mở ảnh ra đọc.** Lưu ảnh mà không đọc = vô nghĩa: chính "đọc ảnh" mới là thứ bắt được lỗi này. | ⬜ Áp dụng từ đợt sau |
| **A3** | **Đếm request kèm mọi thao tác ghi dữ liệu.** Bảng đọc kết quả: `1 request + 2 thông báo` = lỗi hiển thị (dữ liệu an toàn) · `2 request + 2 thông báo` = **nặng**, phải kiểm tạo trùng bản ghi ngay. | ✅ Có sẵn trong A1 |

### Mức B — Bắt KHAI CÓ Ý THỨC (máy chặn, không cho im lặng bỏ qua)

Theo đúng triết lý đã có trong quy trình (*"miễn bảng phải CỐ Ý khai, không được im lặng bỏ qua"* — cờ `--static-bug`):

| # | Đề xuất | Đánh giá thật |
|:-:|---|---|
| **B1** | Thêm cờ **bắt buộc** cho `sheet_write.py` khi ghi verdict: `--observed "<thấy gì bất thường ngoài tiêu chí BA, hoặc 'không có gì'>"`. Không khai → script DỪNG. Buộc QA **có ý thức** trả lời câu hỏi "ngoài case ra, có gì lạ không?" ở **mỗi** case. | ⚠️ **Rủi ro thật: dễ thoái hoá thành gõ máy móc "không có gì".** Chỉ có tác dụng nếu đi kèm A2 (đã thực sự nhìn ảnh). Cần user duyệt trước khi thêm — nó làm mọi lệnh ghi sheet dài thêm. |
| **B2** | Công cụ mở dòng bug mới [tools/sheet_add_bug_row.py](tools/sheet_add_bug_row.py) — để bug ngoài phạm vi **luôn có chỗ đi vào sheet**, không mắc kẹt trong file .md mà dev không đọc. | ✅ Đã làm 16/07 (dòng 112–113) |

### Mức C — Quy tắc trên giấy (yếu nhất — chính là thứ đã hỏng)

| # | Quy tắc | Ghi chú |
|:-:|---|---|
| **C1** | **Verify thấy bug ngoài phạm vi case cũng PHẢI log** — vào phụ lục "Lỗi phát hiện thêm" của report **và** mở dòng TC mới trên sheet (B2). Không được lờ vì "không thuộc tiêu chí BA của case này". | Đã ghi vào bộ nhớ dự án |
| **C2** | **Bug candidate ≠ bug.** Trước khi log, **đo lại bằng phương pháp thứ hai**. Cụ thể: `innerText` vs `textContent` · cây trợ năng · mã nguồn giao diện. Nếu 2 phương pháp mâu thuẫn → **chưa được log**. | Chính C2 đã chặn được bug ma ở mục 1 |
| **C3** | **Không kết luận "không tái hiện được" từ một phép đo của chính mình** khi chưa kiểm phép đo đó đúng chưa. | Xem §4 |

---

## 4. Dấu hiệu nhận biết PHÉP ĐO ĐANG NÓI DỐI

Rút từ 2 lần suýt/đã sai trong cùng một ngày — dùng làm checklist nhanh:

| Dấu hiệu | Nghĩa là gì | Làm gì |
|---|---|---|
| Phép đo **lọc/gộp/`unique`/`includes`** dữ liệu trước khi mình nhìn | Đang vứt bỏ chính thứ cần đếm | Bỏ lọc, đếm thô rồi mới đọc |
| Dùng `textContent` để đọc "chữ người dùng thấy" | Gom cả node ẩn (a11y, sr-only) → tưởng lặp | Dùng `innerText` |
| Kết quả **khớp y hệt** điều mình mong đợi, không có gì thừa | Có thể phép đo chỉ trả lời câu hỏi mình hỏi | Chụp màn hình, nhìn bằng mắt |
| Kết luận dựa **100%** vào `evaluate_script`, không có ảnh nào | Mù toàn tập nếu selector sai | Bắt buộc A2 |
| Selector không khớp → kết luận ngay "chức năng hỏng" | **Đã xảy ra thật:** dùng nhầm `.ant-radio-wrapper` thay vì `.ant-radio-button-wrapper` → suýt báo "điểm danh không được nạp lại" (dữ liệu thực ra vẫn đúng) | Đọc thẳng HTML thô của ô đó trước khi kết luận |

---

## 5. Cái CHƯA đóng được — rủi ro còn lại, để user quyết

1. **Không thể khẳng định 16 case đã verify có bị thông báo lặp hay không.** Bộ đo cũ lọc trùng, và dữ liệu tiền đề của các luồng đó đã tiêu thụ hết → không đo lại được. **Đây là lỗ hổng đã biết, không phải đã đóng.**
2. **Không biết còn bao nhiêu thứ khác đã hiện trên màn hình mà QA chạy qua không nhìn** — hệ quả trực tiếp của Tầng 3 và Tầng 4. **Đây không phải con số ước lượng được**, và không nên giả vờ là có.
3. **Phạm vi lỗi thông báo lặp mới đo được 4 thao tác** (chỉ tạo khóa học bị lặp; trình duyệt kết quả / lưu điểm danh / xóa khóa học đều bình thường). **Chưa quét toàn hệ thống.**

**Đề xuất đóng, rẻ nhất trước:**

| Cách | Chi phí | Nhận xét |
|---|---|---|
| **Dev rà một lượt toàn bộ chỗ hiện thông báo trên mã nguồn** | Thấp cho dev | **Khuyến nghị.** Dev có mã gốc + source map, tìm bằng grep nhanh hơn QA đo từng luồng nhiều lần |
| QA quét lại bằng `toast-capture.js` trên các luồng chính | Cao | Phải dựng lại tiền đề từng luồng; chỉ nên làm nếu dev không rà được |
| Bỏ qua | 0 | **Không khuyến nghị** — lỗi đã chứng minh là có thật, chỉ chưa rõ rộng tới đâu |

---

## 6. Làm sao biết phương án này có hiệu lực (chứ không phải hứa suông)

Tiêu chí kiểm ở đợt verify kế tiếp — **kiểm được, không phải cảm tính**:

1. Mọi thao tác đổi trạng thái (**kể cả seed**) đều **có ảnh** trong `image/` và ảnh đó **đã được mở đọc**, không chỉ lưu.
2. Không còn observer tự viết trong phiên — chỉ dùng `toast-capture.js`. Grep phiên làm việc: **không được xuất hiện** `includes(` trong bộ bắt thông báo, **không được xuất hiện** `textContent` để đọc chữ hiển thị.
3. Mỗi report có mục **"Lỗi phát hiện thêm ngoài phạm vi"** — kể cả khi mục đó ghi *"không phát hiện thêm"*, và câu đó phải dựa trên ảnh đã đọc (điểm 1), không phải suy đoán.
4. Bug ngoài phạm vi **đi tới dev**, tức là **có mặt trên sheet** (dòng TC mới qua `sheet_add_bug_row.py`), không nằm im trong file .md.

**Thước đo cuối cùng, thẳng thắn:** lần tới user nhìn màn hình mà thấy thứ QA đã chạy qua nhưng không báo → phương án này **đã thất bại**, và phải quay lại Tầng 3–4 chứ không phải viết thêm quy tắc.
