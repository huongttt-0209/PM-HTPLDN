# FLOW 01 — Verify bug đối tác gửi (vòng đầu)

**Dùng khi:** đối tác gửi danh sách bug (Google Sheet), QA soát lần đầu: **có phải bug thật không?**
**Không dùng khi:** BA đã trả lời (→ [FLOW 02](02-ap-quyet-dinh-ba.md)) · dev báo đã fix
(→ [FLOW 03](03-reverify-sau-dev-fix.md) nếu bug đã qua flow này, [FLOW 04](04-verify-bug-dev-fix-khong-ho-so.md) nếu chưa).

> Flow chỉ nói **quy trình + cách check**. Thông tin dự án do **prompt truyền vào**.
> Thiếu tham số bắt buộc → **DỪNG hỏi user, cấm đoán**.

---

## PROMPT MẪU

```
Áp dụng @flows/01-verify-bug-doi-tac.md
- Sheet: <link>   | Tab: <tên tab>
- Ô mã case: "<...>" | Ô trạng thái dev: "<...>" | Ô kết quả QA: "<...>" | Ô note: "<...>"
- Từ vựng ô kết quả QA: là bug="<...>" · không phải bug="<...>" · cần BA="<...>" · không tái hiện="<...>"
- Từ vựng ô trạng thái dev: đã fix="<...>" · chờ BA="<...>"
- Đặc tả (SRS): <đường dẫn>        | Môi trường + tài khoản: <đường dẫn>
- Bug report: <file gộp>           | Ảnh: <thư mục image/>
- File gửi BA confirm: <đường dẫn>
- Công cụ: ghi kết quả=<...> · tải bằng chứng=<...> · bắt thông báo=<...>
- Phạm vi: <danh sách mã case | "toàn bộ dòng chưa có kết quả QA">
```

**Bắt buộc:** sheet + tên tab · tên 4 ô · đặc tả · môi trường/tài khoản · bug report + thư mục ảnh ·
file gửi BA. **Tuỳ chọn:** từ vựng (không khai → mặc định bảng dưới) · công cụ · phạm vi.

- Prompt có cả `gid=...` lẫn tên tab bằng chữ → **resolve gid ra tên tab rồi so sánh; lệch → DỪNG**.
- Định vị ô bằng **TÊN HEADER**, CẤM dùng chữ cái cột (thứ tự cột đổi được).

## Vai trò 4 ô

| Vai trò | Ai ghi | Ghi chú |
|---|---|---|
| **ô mã case** | không sửa | Khoá map bug ↔ dòng, Bug ID = `BUG-<mã case>`. Mở **dòng mới** thì được cấp mã; chỉ cấm sửa mã dòng có sẵn |
| **ô trạng thái dev** | dev | QA chỉ ghi khi ô **đang trống**; đã có giá trị của dev → **không đè**. *(Ngoại lệ: FLOW 02 gỡ nhãn "chờ BA", FLOW 03/04 ghi Reopen)* |
| **ô kết quả QA** | QA | Verdict |
| **ô note** | QA | **Người đọc đổi theo verdict** — §Note |

Hai ô mâu thuẫn nhau là **hợp lệ** (dev bảo không phải bug + QA soát lại thấy đúng là bug).

## Từ vựng verdict

Chỉ được ghi giá trị **có trong dropdown** của ô đó. Không có → **DỪNG báo user**, cấm bịa.

| Khái niệm | Mặc định |
|---|---|
| Đúng là bug | `Open` |
| Không phải bug (chứng minh được đối tác sai) | `Reject` |
| Bất đồng đặc tả, cần BA quyết | `BA confirm` |
| Không tái hiện **nhưng đối tác có bằng chứng** | `Resolved` |
| Chưa đủ điều kiện verify | **ô trống** |

---

## BƯỚC 0 — chốt phạm vi (1 lần)

Liệt kê **số dòng + danh sách mã case** thuộc phạm vi → báo user → mới chạy. Prompt khai phạm vi mà số
đếm lệch → **DỪNG hỏi**.

**Mặc định = dòng chưa có kết quả QA, TRỪ dòng ô trạng thái dev đang là "đã fix"** — dòng đó thuộc
FLOW 03/04, verify ở đây là chấm sai câu hỏi. Gặp trong phạm vi user khai → báo user.

## Vòng lặp MỖI CASE — **hồ sơ trước, bảng sau**

**CẤM gom cuối lô.**

1. Xem bằng chứng đối tác (**3 CỔNG**).
2. Verify trên web — **UI thật**, đúng vai trò của bug. API/DB chỉ để điều tra.
3. Chốt verdict → **là bug: tạo entry bug-report + ảnh + khối CÁCH VERIFY NGAY** (§Đầu ra).
4. **Rồi mới** ghi verdict + note vào bảng → **đọc lại xác nhận**.
5. Báo user 1 đoạn → case kế.
6. *"Ngoài điều đối tác báo, có thấy gì bất thường không?"* — dựa trên **ảnh đã đọc**. Có → **log thành
   dòng case mới trên bảng**. Không → ghi "không phát hiện thêm" **kèm danh sách ảnh đã đọc**.

> Thứ tự này để lúc dừng giữa chừng, tệ nhất là *có entry mà bảng chưa có verdict* — vô hại. Ngược lại
> đẻ ra *bảng có verdict, bug-report thiếu entry*, đúng nguyên nhân lệch số mà FLOW 03 phải đi bắt.

**Bug candidate ≠ bug.** Thấy dấu hiệu lỗi → **đo lại bằng phương pháp thứ hai** trước khi log (UI fail →
gọi API cùng hành động; API fail → tải lại trang test lại). **Hai phương pháp mâu thuẫn = CHƯA được log** —
ghi cả hai, hỏi user.

## 3 CỔNG — đủ 3 mới được chốt verdict

1. **Bằng chứng.** Phải **mở XEM được** file đối tác rồi mới verify. Video → trích frame tới **khoảnh khắc
   lỗi**; đọc **full-res**. *"Không thấy file"* ≠ *"đối tác không gắn"* — công cụ tải báo **rỗng** mới là
   không có. Chưa xem được = **CẤM verify bằng chữ trong sheet**.
   Trích **3 dữ kiện neo**: URL/ID bản ghi · trạng thái entity · dữ liệu tiền đề.
2. **Hiểu bug.** Viết 3 dòng: *bằng chứng đã xem (file + frame + 1 câu tả lỗi trong frame đó)* · *đối tác
   phản ánh CỤ THỂ gì* · *data + bước tái hiện*. Chưa thấy frame lỗi → **ô trống + hỏi user**.
3. **Đối chiếu.** Bảng *đặc tả yêu cầu gì (dẫn line)* vs *web thực tế*. Cấm kết luận cảm tính.

**Checklist cổng 3 theo loại bug:** Hiển thị→cột/field · Validation→input sai→rule→thông báo ·
Permission→role×hành động (role thật) · Workflow→state trước→sự kiện→state sau · Filter→điều kiện→số bản
ghi kỳ vọng vs thực · Màn rỗng→điều kiện no-data→thông báo · Import→file mẫu→rule→kết quả từng dòng ·
Tìm kiếm/Sắp xếp/Phân trang→query→kỳ vọng vs thực · **File xuất ra→ mở file đọc nội dung**.

**File xuất ra (Excel/PDF/CSV):** tạo được file ≠ file đúng. Mã trả về 200 + có bytes chỉ chứng minh hệ
thống *sinh ra* file. Phải **mở đọc**: đủ cột/mục theo đặc tả · dữ liệu khớp màn hình · nhãn/kỳ báo cáo
đúng. Không mở đọc được → **ô trống**.

**Đối tác THẬT SỰ không gắn bằng chứng** (công cụ tải báo rỗng):

| Tình huống | Verdict cho phép |
|---|---|
| Tự tái hiện được | *là bug* |
| Không tái hiện được, mô tả đủ rõ | hỏi đối tác bổ sung → chưa có thì **ô trống** |
| Mô tả mơ hồ | **ô trống + câu hỏi cụ thể cho đối tác** |

🔴 **CẤM verdict *không phải bug* trong nhánh này** — verdict đó đòi **chứng minh đối tác sai**, mà
*"tôi không tái hiện được"* không phải là chứng minh.

## 🔴 Quy tắc VÀNG — kết luận theo điều kiện của ĐỐI TÁC

> Tái hiện ở điều kiện **khác** rồi thấy "chạy được" = **CHƯA verify**, không phải "không phải bug".

Điền bảng dưới **và lưu thành file/mục có đường dẫn** (bảng trong đầu = không tồn tại):

| Điều kiện có thể đổi kết quả | Đối tác (từ bằng chứng full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | | | |
| Entity + **trạng thái** | | | |
| Dữ liệu tiền đề | | | |
| Input / filter / giá trị nhập | | | |

- **Điền đủ 4 dòng.** Dòng cho là không ảnh hưởng → vẫn ghi `Không — <căn cứ>`. Bỏ trống = **còn GAP**.
- **Còn ≥1 GAP → CẤM verdict *là bug* / *không phải bug* / *không tái hiện*.**
- **Ngoại lệ — GAP không thể đóng** (blocker khách quan, hoặc tiền đề không thể tạo): được để **ô trống**,
  và **phải ghi rõ GAP nào chưa đóng + vì sao**. Ô trống không nêu GAP tồn đọng là **không hợp lệ**.
- GAP **tạo được** (tài khoản, dữ liệu, trạng thái) chỉ đóng bằng **test thật**, cấm đóng bằng lập luận.

**Bằng chứng đối tác không lộ điều kiện** (gần như luôn xảy ra) — không tự động là GAP chết:
① suy từ bằng chứng (tên góc màn, menu, dữ liệu trên màn) → ② suy không ra thì **test đủ mọi nhánh khả dĩ**,
mọi nhánh cùng kết quả ⇒ GAP đóng, ghi rõ đã thử nhánh nào → ③ quá nhiều nhánh thì **hỏi đối tác**, chưa
có trả lời thì **ô trống**. Đừng đoán một nhánh rồi kết luận.

## Nguyên tắc

1. **Đặc tả/BA là chuẩn, không phải kỳ vọng đối tác.** Thứ bậc: *đặc tả & BA duyệt > thiết kế nội bộ duyệt
   > kỳ vọng đối tác*. Nhưng kỳ vọng khác đặc tả → **cần BA quyết**, KHÔNG tự bác.
2. **Verify qua UI thật** — không lấy API/DB ra *bênh* cho UI sai (*"API trả đúng, chắc UI chỉ hiển thị"*
   → vẫn là bug). ⚠️ Khác với ca **hai phép đo cùng một sự kiện cho kết quả trái ngược** (UI báo lỗi ↔ API
   thành công): ca đó **hoãn verdict**, ghi cả hai, hỏi user — đừng dùng luật "UI thắng" để chốt nhanh.
3. **Login đúng vai trò của bug.** Tài khoản quản trị chỉ để chuẩn bị dữ liệu/điều tra, **không ra verdict**.
   **Ghi rõ tài khoản đã dùng.**
4. 🔴 **Thiếu tiền đề thì TỰ TẠO — không phải blocker** (tài khoản/vai trò · dữ liệu · trạng thái).
   Tiền đề *tạo được* mà không tạo → **CẤM mọi verdict, kể cả ô trống**. Tiền đề **không thể tạo** → ô
   trống hợp lệ, nêu rõ cần ai seed gì.
5. Tài khoản mới tạo → **ghi vào file môi trường** để lần sau dùng lại.

## Verdict

| Verdict | Khi nào |
|---|---|
| **Đúng là bug** | Web sai rule đặc tả (dẫn line), HOẶC chặn luồng hợp lệ dù đủ điều kiện |
| **Không phải bug** | **CHỈ khi chứng minh được** đối tác thao tác/hiểu sai. ⚠️ Không tái hiện mà đối tác **có** bằng chứng → KHÔNG dùng. Đối tác **không** gắn bằng chứng → cũng không dùng |
| **Không tái hiện** | Đối tác có bằng chứng, bản hiện tại chạy OK. Bắt buộc **re-verify LIVE** |
| **Cần BA quyết** | Kỳ vọng đối tác **khác** đặc tả · đặc tả im lặng · các nguồn mâu thuẫn |
| **ô trống** | Không mở được bằng chứng · chưa thấy frame lỗi · blocker khách quan · GAP không đóng được. **KHÔNG** dùng cho tiền đề tạo được |

**Ca biên:**
- *Là bug* vs *cần BA quyết*: đặc tả nêu **rõ** cột/vị trí/thông báo mà web sai → là bug; đặc tả chỉ nêu
  nghiệp vụ chung, web đáp ứng cách khác → cần BA quyết.
- Đã đóng GAP mà **không tái hiện**: đối tác **có** bằng chứng → *không tái hiện* · **chứng minh được**
  đối tác sai → *không phải bug* · web **mâu thuẫn** bằng chứng, hoặc chỉ tranh chấp kỳ vọng → *cần BA quyết*.
- **1 case gộp nhiều lỗi con:** verdict từng ý. Tổng: ≥1 ý là bug → **là bug**; không có ý bug mà còn ý
  cần-BA/ô-trống → lấy theo ý đó; **chỉ** kết luận không-phải-bug khi **mọi** ý đều vậy.

**Tự vấn trước khi ghi** (bác nhầm nguy hơn báo nhầm): *là bug* → sai clause nào, dẫn line? · *không phải
bug* → đã **chứng minh** đối tác sai chưa? · *không tái hiện* → đã re-verify **LIVE** chưa? · còn GAP hoặc
đặc tả im lặng → **chưa được chốt**.

## 🔴 GATE bằng chứng real-data

**Cơ chế lách mà gate này chặn:** gặp khó → thay bằng chứng **rẻ** ("đọc đặc tả", "xem video đối tác") cho
bước **đắt** (tạo data + tự tay chạy). Khó khăn là tín hiệu đi tìm **màn tương đương + tạo data**.

Mỗi verdict phải kèm **1 trong 2**:

**① Artifact QUAN SÁT** — chạy trên data tự tạo:

| Loại claim | Artifact hợp lệ |
|---|---|
| Hiển thị/render | Ảnh full-res đúng phần tử tranh chấp, không cắt cụt |
| Thao tác/trạng thái | Thông báo bắt được / network status của **chính thao tác đó** |
| Absence ("phải báo lỗi X nhưng không") | Tự chạy đúng thao tác + chứng minh mọi kênh báo lỗi **rỗng** |
| Filter/search/đếm | Baseline + query phân biệt + số bản ghi thực |
| File xuất ra | **Nội dung đọc được từ file**, không phải mã trả về |

**② Artifact BLOCKER** — bảng chứng minh đã thử **cạn kiệt**: *vai trò × màn × URL/menu × tài khoản × kết
quả × đường dẫn ảnh*. Tối thiểu ≥1 dòng cho **mỗi vai trò khả dĩ** và ≥1 dòng cho **mỗi đường vào** màn
(menu, URL trực tiếp, link từ màn khác). Trước đó phải đóng mọi tiền đề tạo được.

**Artifact phải truy được THỜI ĐIỂM** — ít nhất một trong: thời điểm trong tên file · thời điểm trên màn ·
URL/ID bản ghi vừa tạo. Không biết chụp lúc nào = không chứng minh được thuộc lần test này.

**Cấm** ghi verdict khi chưa có 1 trong 2. *"Đọc đặc tả thấy sai"* / *"video đối tác cho thấy"* **không
thay được** artifact real-data.

**Ngoài hệ thống vs trong hệ thống** — quyết TRƯỚC khi gán "cần BA quyết". Chỉ coi là *ngoài hệ thống* sau
khi **loại trừ mọi tín hiệu trong hệ thống**:
- *Ngoài*: thao tác **chỉ** quan sát được trên cổng bên thứ ba QA không truy cập được, hoặc phụ thuộc đồng
  bộ do hệ thống khác chủ động gọi sang.
- *Trong* → **PHẢI verify được**: thao tác của người dùng nội bộ, thông báo do hành động nội bộ sinh ra,
  cập nhật trạng thái, CRUD màn quản trị, nhật ký. Đối tác quay màn hình ở cổng ngoài **không** làm bug
  thành *ngoài hệ thống* nếu nguyên nhân nằm ở hành động nội bộ.

**Bắt thông báo tự tắt:** dùng **script dùng chung của dự án**, **cấm tự viết observer mới**. **CẤM lọc
trùng** (che double-toast → Pass oan) · **CẤM `textContent`** (gom node ẩn → bug ma) · luôn **đếm request
kèm số thông báo**. Lệch thì phải xử lý, không chỉ ghi lại:

| Quan sát | Làm gì |
|---|---|
| 1 request + 2 thông báo | Lỗi hiển thị → **log bug riêng** mức nhẹ, không gộp vào case đang chạy |
| 2 request + 2 thông báo | **Nặng** → kiểm ngay có bản ghi trùng không; có → log bug riêng mức cao |
| 1 request + 0 thông báo | Đối chiếu đặc tả có yêu cầu thông báo không → có thì là bug |

**Ảnh phải kèm chú thích.** Chụp ở mọi thao tác đổi trạng thái (kể cả bước tạo dữ liệu), mỗi ảnh kèm 1 dòng
*tên file + thấy gì trong ảnh* (vd `toast-loi.png` — *toast đỏ "Không có quyền", danh sách còn 0 dòng*).
Viết không nổi chú thích = **chưa mở ảnh ra đọc** → chưa được dùng làm bằng chứng.

## Ghi kết quả

Có công cụ ghi → **bắt buộc dùng**, cấm ghi tay. Chạy thử → ghi thật → **đọc lại xác nhận**. Công cụ chặn
→ **DỪNG báo user**; cấm ghi tay để lách, cấm viết script ad-hoc mới.

Công cụ tối thiểu phải guard: khớp **mã case** · giá trị trong **dropdown** · in **old→new** · **đọc lại**
sau ghi · **log giá trị cũ** · đòi **đường dẫn bảng điều kiện + artifact**.

> ⚠️ **Chưa có công cụ ghi** → mọi dòng "BẮT BUỘC/CẤM" chỉ còn là lời dặn. Phải làm bù 3 việc:
> ① báo user rõ độ tin cậy thấp hơn ngay đầu đợt · ② sau mỗi lần ghi, **đọc lại đúng dòng đó và dán lại
> 3 ô** vào báo cáo · ③ ghi nhật ký *giá trị cũ → mới* vào file audit để khôi phục được.

## Note — người đọc đổi theo verdict

Tiếng Việt **có dấu**, **gạch đầu dòng**, dẫn chứng cụ thể.

| Verdict | Dòng đầu | Bắt buộc có | Đọc chính | Reference |
|---|---|---|---|---|
| Là bug | `📌 KẾT QUẢ CHUNG: XÁC NHẬN LÀ LỖI — CHUYỂN DEV` | `❌ CÒN LỖI — <hành vi sai cụ thể>` · kết quả mong đợi · kết quả thực tế · dev cần sửa · Bug ID | dev/BA | **giữ** mã + số dòng |
| Không phải bug | `📌 KẾT QUẢ CHUNG: KHÔNG PHẢI LỖI` | `✅ KHÔNG PHẢI LỖI — <lý do>` · kết quả mong đợi đúng · kết quả thực tế | đối tác | **bỏ** mã/số dòng |
| Chưa thể kết luận | `📌 KẾT QUẢ CHUNG: CHƯA THỂ KẾT LUẬN` | `⏸ CHƯA CHỐT — <phần chưa kết luận>` · kết quả cần kiểm tra · kết quả thực tế/điều kiện còn thiếu · dữ kiện cần bổ sung | đối tác | **bỏ** mã/số dòng |
| Cần BA quyết | `📌 KẾT QUẢ CHUNG: CẦN BA XÁC NHẬN` | `❓ CẦN BA XÁC NHẬN — <điểm chưa chốt>` · expected ↔ SRS · kết quả thực tế · **một câu hỏi cụ thể cho BA** | dev/BA | **giữ** mã + số dòng |

`📌` chỉ đánh dấu dòng tổng kết, không mang nghĩa đạt hay lỗi. Các icon chi tiết có nghĩa cố định trong mọi
flow: `❌` còn lỗi/xác nhận là bug · `❓` cần BA · `✅` đạt/không phải lỗi · `⏸` chưa đủ căn cứ · `🔎` phạm vi
đã kiểm tra. `⚠️` chỉ dùng cho caveat/cảnh báo, không dùng làm verdict.

Với verdict có phép đo web, luôn ghi:
`🔎 PHẠM VI ĐÃ ĐO: <URL môi trường> · <thời gian/bản dựng> · <vai trò> · <dữ liệu/biến thể quyết định>.`

Mẫu chung, không viết thành đoạn văn:

```text
📌 KẾT QUẢ CHUNG: <verdict>
<icon> <MỤC KẾT QUẢ> — <hành vi>
- Kết quả mong đợi: <hành vi cần đạt>.
- Kết quả thực tế: <hành vi đo được + số liệu quyết định>.
🔎 PHẠM VI ĐÃ ĐO: <URL môi trường> · <thời gian/bản dựng> · <vai trò>.
```

Mục còn lỗi dùng đúng ba ý, không viết thành lịch sử điều tra:

```text
❌ CÒN LỖI — <nêu chính xác hành vi đang sai>
- Kết quả mong đợi: <expected và SRS file:dòng quy định gì>.
- Kết quả thực tế: <đúng tiền đề · output sai · số đo/ví dụ quyết định · phạm vi tái hiện>.
- Dev cần sửa: <kết quả quan sát được phải đạt; không đoán nguyên nhân, không ép cách triển khai>.
```

Tên lỗi phải nói rõ cái gì sai. Số liệu quyết định ghi thẳng trong `Kết quả thực tế`; lịch sử điều tra và
artifact chi tiết để trong hồ sơ audit/cột ảnh.

Ô note là **ô dùng chung**, người đọc chính đổi theo verdict — luật *bỏ jargon* chỉ áp cho 2 verdict hướng
đối tác. Nhưng đối tác **vẫn xem được** ô này, nên mọi verdict đều cấm những thứ dưới.

**Cấm (mọi verdict):** viết không dấu · mô tả mơ hồ ("không giống thiết kế" mà không nói thiếu gì) · câu
đệm rỗng không kèm bằng chứng · **chi tiết nội bộ** (video đối tác quay, lịch sử BA chốt, so sánh 2 môi
trường) — đẩy vào hồ sơ audit.

## Đầu ra

**Là bug** → Bug ID = `BUG-<mã case>` + entry vào **file bug-report gộp** + **≥1 ảnh** + **khối CÁCH VERIFY**.

Entry tối thiểu (FLOW 03 đọc đúng những mục này): *mô tả · bước tái hiện · kết quả mong đợi · kết quả thực
tế · đường dẫn ảnh · vai trò + trạng thái + dữ liệu tiền đề đã dùng*. Dự án có template riêng → theo template.

🔴 **Khối CÁCH VERIFY bắt buộc cho MỌI bug log ở flow này**, không chỉ bug qua BA — ghi vào **ô note** và
vào bug entry:

```
── CÁCH VERIFY sau Dev fix ──
Phạm vi: <chỉ vế còn lỗi + expected/SRS file:dòng>.
Precondition:
- <URL môi trường · vai trò · màn · trạng thái/input bắt buộc>.
- <dữ liệu phân biệt được hành vi lỗi cũ với hành vi cần đạt>.
1) <đường UI ngắn nhất tới hành vi lỗi>
2) <thao tác và output cần quan sát>
Đối chứng độc lập: <đọc lại đúng bản ghi/giao dịch/request/tệp của lượt trên và nối được với UI>.
✅ PASS khi: <mọi điều kiện/biến thể bắt buộc đều đạt và bằng chứng phân biệt được hành vi mới với lỗi cũ>.
❌ FAIL nếu: <ít nhất một yêu cầu bắt buộc sai trên đúng tiền đề, có đối chứng độc lập>.
⏸ CHƯA CHỐT khi: <thiếu tiền đề/dữ liệu phân biệt; không nối được UI với đối chứng; hoặc hai phép đo mâu thuẫn>.
⚠️ Caveat: <bẫy có bằng chứng dễ gây Pass oan/Fail oan; không có thì bỏ>.
Ảnh lỗi cũ: <đường dẫn ảnh>
```

Rule chất lượng: mỗi bước phải trả lời trực tiếp một phần của vế lỗi. Không Pass bằng dữ liệu mà hành vi cũ và
mới đều có thể cho cùng kết quả, khi mới đo một phần hoặc thiếu biến thể bắt buộc. Không Fail khi sai tiền đề,
thiếu dữ liệu hoặc chưa nối được bằng chứng. Lặp lại cùng tín hiệu không phải đối chứng; trường hợp biên chưa
được expected/SRS quy định → Cần BA, không tự đặt tiêu chí.

> **Vì sao bắt buộc:** đa số bug đi thẳng sang dev, **không** qua BA. Không viết ở đây thì FLOW 03 sẽ **tự
> chế tiêu chí sau khi đã nhìn thấy kết quả** — đúng cơ chế đẻ ra Pass oan.

**Cần BA quyết** → 1 mục trong file gửi BA: web đang thế nào · đối tác kỳ vọng gì · đặc tả nói gì (dẫn
line) · **câu hỏi cần BA trả lời** · **đường dẫn ảnh lỗi** (FLOW 02 dẫn lại ảnh này trong khối CÁCH VERIFY).

**Không phải bug / không tái hiện / ô trống** → không vào bug-report, nhưng **lưu vết audit**: file bằng
chứng đã xem + frame + ảnh web + line đặc tả + thời điểm test.
