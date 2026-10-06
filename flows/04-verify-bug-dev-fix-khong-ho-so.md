# FLOW 04 — Verify bug dev đã fix, KHÔNG có hồ sơ nội bộ

**Dùng khi:** dev báo đã fix, nhưng bug **chưa từng qua** vòng soát nội bộ — không có bug entry, không có
khối CÁCH VERIFY. Chỉ có dòng trên bảng của đối tác + bằng chứng của họ.
**Không dùng khi:** bug đã có bug entry **và** khối CÁCH VERIFY sẵn — ca đó chỉ cần chạy lại đúng khối đó.

**File này tự chứa về quy trình verify** — không cần mở flow/quy tắc khác; vẫn phải mở đúng SRS, nguồn case
và bằng chứng do prompt cấp.

> Thông tin dự án do **prompt truyền vào**. Thiếu tham số bắt buộc → **DỪNG, hỏi user; cấm tự đoán**.

---

## ĐẦU VÀO TỪ PROMPT

Đọc trực tiếp từ prompt của session; flow không yêu cầu user điền lại một mẫu riêng.

**Bắt buộc để verify:** nguồn chứa đầy đủ case + expected đối tác · **đúng đường dẫn SRS dùng làm nguồn
chuẩn** · tài khoản · môi trường · phạm vi. Thiếu dữ kiện nào làm thay đổi chuẩn chấm hoặc không thể tái hiện
→ dừng đúng case đó và hỏi user; cấm tự đoán.

**Tùy chọn:** bằng chứng đối tác · mẫu đầu ra · công cụ bắt thông báo/tải bằng chứng/seed. Thiếu tùy chọn →
tiếp tục nếu vẫn tái hiện và kết luận được.

**Mọi cập nhật ra ngoài phép đo** — Sheet/Drive/file nào, trường nào, giá trị nào, dùng phương tiện nào — do
prompt của session quyết định. Prompt không yêu cầu thì không cập nhật. Flow này chỉ trả ra verdict logic và
nội dung căn cứ; không định nghĩa mapping, cột, dropdown, đường dẫn hay quyền ghi.

**Ảnh/video trên Sheet bug:** chỉ tạo, tải lên và gắn ảnh/video mới khi kết luận **Reopen** hoặc xác nhận **bug
mới**. Với Pass/Hiện tại đạt/Không phải lỗi/Cần BA/Chưa chốt/candidate, không tạo ảnh chỉ để làm bằng chứng
verify và không điền cột ảnh; giữ nguyên nội dung cũ nếu có. Yêu cầu “cập nhật Sheet” chung không đồng nghĩa
phải gắn ảnh. Luật này không bỏ phép đo, đối chứng độc lập hoặc việc mở đọc output/tệp bắt buộc.

---

## BƯỚC 0 — chốt phạm vi (1 lần)

1. **Phạm vi lấy từ prompt của session, không tự suy ra từ bảng.**
   - Prompt cho **danh sách mã case** → chạy đúng danh sách, không thêm không bớt. Case trong danh sách mà ô
     trạng thái dev không phải "đã fix" → **vẫn chạy**, chỉ ghi chú lại; đừng tự loại.
   - Prompt cho **tiêu chí lọc** (vd *"mọi dòng dev báo đã fix"*) → lọc đúng tiêu chí đó.
2. Mỗi mã case, kiểm bug-report có **entry tương ứng** không:
   - Có entry **và** có khối CÁCH VERIFY → **tách ra, không chạy flow này** (chỉ cần chạy lại đúng khối đó).
   - Không có entry, hoặc entry **không kèm** khối CÁCH VERIFY → chạy flow này.
3. In **vị trí nguồn + danh sách mã case** từng nhóm, kèm case nào không tải được bằng chứng. Không cần chờ phản hồi;
   chỉ dừng riêng case không có bằng chứng **và** không tự tái hiện được.

🔴 **Nhiều case cùng một câu triệu chứng** (mô tả giống hệt nhau, khác màn/khác module): **đo từng case trên
đúng màn của nó**. Cấm đo 1 case rồi suy cho các case còn lại — **cùng chữ không có nghĩa cùng nguyên nhân**.

Nếu nguồn case có thể thay đổi trong lúc chạy, **đọc lại đầy đủ case trước khi chốt verdict**; không dựa vào
bản cắt ngắn hoặc bản chụp đầu phiên.

---

# GIAI ĐOẠN A — chốt chuẩn chấm, CHƯA MỞ MÀN ĐANG TRANH CHẤP

## Nguồn chuẩn duy nhất

🔴 **Chỉ SRS tại đúng đường dẫn prompt cung cấp được đại diện phía đặc tả.** Expected đối tác là phía yêu cầu
đang được reverify. QA chỉ tự chấm Pass/Reopen khi hai phía **không mâu thuẫn**; nếu SRS nói khác expected thì
phải kết luận Cần BA, dù dev hiện đang làm đúng SRS. Bằng chứng đối tác chỉ dùng để lấy tiền đề tái hiện.
Phản hồi DEV/TKM, thư BA, ảnh đối tác, báo cáo tuần cũ và SRS ở đường dẫn khác chỉ là **manh mối tìm chỗ cần
đọc**, không được thêm yêu cầu, thay SRS hoặc quyết định verdict. Quyết định BA chỉ có hiệu lực trong flow này
khi đã được nhập vào chính bản SRS prompt cung cấp.

- Mọi trích dẫn phải tự mở lại từ đúng bản SRS trong lượt hiện tại, ghi `file.md:dòng`; cấm mượn số dòng từ
  thư BA, phiếu UAT hoặc hồ sơ cũ. Với `GAP` do SRS im lặng, ghi `IM LẶNG` nhưng vẫn dẫn dòng tiêu đề/bảng gần
  nhất đã đọc để truy được phạm vi kết luận; không biến dòng đó thành yêu cầu mà nó không hề ghi.
- Trước khi kết luận SRS im lặng/mâu thuẫn/khác expected, phải đọc **trọn bảng hoặc đoạn liên quan**, tìm cả
  thuật ngữ đồng nghĩa và dấu thay đổi (`[STT…]`, `[CR-…]`) nếu bản SRS có dùng. Một lệnh grep ra rỗng
  **không đủ** để kết luận SRS không quy định.
- SRS khác expected → bắt buộc ghi nguyên hai phía và tạo câu hỏi BA confirm. Nếu đã đo được dev đúng SRS thì note
  `DEV ĐANG ĐÚNG SRS HIỆN HÀNH · EXPECTED ĐỐI TÁC KHÁC SRS: …`; đây là hiện trạng kỹ thuật, **không phải Pass**.

## BUG SCOPE LOCK — cổng cứng trước khi đo, không tạo file

**Không tạo file tiêu chí/Scope Lock riêng.** Trong ngữ cảnh làm việc, mỗi vế chỉ chốt đúng một dòng:

`C1 · expected đối tác · SRS file:dòng (hoặc IM LẶNG/MÂU THUẪN) · MATCH/DIFF/GAP · route TEST/BA · đường đo`

Luật khóa:

1. Tách **đúng các vế trong expected đối tác**, không thêm chức năng kế bên. Mỗi vế phải khóa quan hệ:
   `MATCH` → được chấm; `DIFF` → bắt buộc BA confirm và cấm Pass; `GAP` (SRS im lặng/mâu thuẫn) → BA confirm.
   Kết quả web không được biến `DIFF/GAP` thành `MATCH`.
   **Dòng SRS dẫn cho một vế chỉ dùng để chấm đúng điều expected có nhắc.** Vai trò, trạng thái hoặc dữ liệu mà
   SRS quy định để vế đó có hiệu lực phải được dùng làm **tiền đề**, không tách thành bug mới. Hành vi/biến thể
   kế bên mà expected không nhắc thì không thành tiêu chí chấm và không được mở thêm phép đo.
2. Mỗi thao tác, seed, ảnh và phép đo phải trả lời được `đang kiểm Cn nào?`. Không ánh xạ được về vế bug thì
   **CẤM chạy** trong Flow 04.
3. Mặc định mỗi vế chỉ có **một đường UI ngắn nhất + một đối chứng độc lập**. Nhiều bước liên tiếp của cùng
   đường UI vẫn là một phép đo; không lặp lại trên trường/role/trạng thái khác chỉ để “chắc”.
4. Chỉ thêm biến thể khi **chính vế expected** áp dụng cho nhiều biến thể và SRS quy định kết quả khác nhau,
   hoặc bằng chứng của case cho thấy claim phụ thuộc biến thể đó; phải dẫn căn cứ tương ứng. SRS chỉ liệt kê
   enum và câu “về lý thuyết có thể lỗi” không phải căn cứ. Chỉ đo toàn bộ tập khi vế expected là mệnh đề toàn
   tập và có thể trả lời bằng một truy vấn gọn; cấm mở từng hàng/tệp để biến nó thành regression.
5. Sau khi mở màn, cấm đổi PASS/FAIL **hoặc đổi quan hệ MATCH/DIFF/GAP** để khớp kết quả. Đổi relation chỉ
   hợp lệ khi dẫn được **dòng SRS mới đọc được**; lý do kiểu *“kỳ vọng coi như đã được đáp ứng bằng cách
   khác”*, *“web đã làm đúng expected”* hoặc *“BA có cơ hội sửa mà không sửa”* không thay được quan hệ đã
   khóa. Hành động mới không qua luật 2–4 thì không chạy.

**Chưa được** vào màn đang tranh chấp để “xem thử nó thế nào rồi” trước khi khóa xong các dòng Cn.

## Cổng bằng chứng

Nếu prompt có file đối tác thì phải **mở xem nội dung**, không chỉ tin tên tệp. Video → tới đúng khoảnh khắc
lỗi; ảnh → đọc full-res; kiểm đúng case và đúng màn.

Từ bằng chứng, chỉ lấy các neo cần để tái hiện: `URL/ID bản ghi · trạng thái · vai trò · env/bản dựng`.
Thiếu bằng chứng nhưng tự tái hiện được → chạy tiếp và ghi điều kiện đã tái hiện. Không tái hiện được → kết
luận **Chưa chốt**, hỏi đúng dữ kiện còn thiếu. **Cấm kết luận “không phải lỗi” chỉ vì không tái hiện được.**

## Đối chiếu đặc tả

| Đặc tả về đúng phần đang tranh chấp | Xử lý |
|---|---|
| Nói rõ, khớp kỳ vọng đối tác | Route `TEST`; sang giai đoạn B và chốt Pass/Reopen bằng kết quả đo |
| Nói rõ, ngược kỳ vọng đối tác | Đo hiện trạng tối thiểu nếu cần biết dev đang theo phía nào; **cấm Pass**, kết luận Cần BA và tạo câu hỏi xác nhận. Chỉ Reopen phần độc lập mà cả SRS lẫn expected cùng yêu cầu nhưng web đều không đạt |
| Im lặng hoặc tự mâu thuẫn | Chỉ đo hiện trạng nếu cần làm rõ câu hỏi; **không Pass/Reopen vế này**; kết luận Cần BA và tạo câu hỏi xác nhận |

Case nhiều vế → đối chiếu từng vế. Đoạn SRS có nội dung nhưng vẫn mơ hồ/tự mâu thuẫn đến mức không xác định
được chuẩn chấm → route `GAP` và gửi BA, không test rồi lấy kết quả làm chuẩn. Chỉ phủ đúng kế hoạch đã qua
BUG SCOPE LOCK; cấm tự mở rộng thành regression, CRUD matrix, mọi vai trò, mọi bộ lọc, mọi trạng thái hoặc
mọi dạng dữ liệu.

Nếu mọi vế đều `DIFF/GAP` và câu hỏi BA đã rõ từ nguồn case + SRS thì **được chốt cần BA ngay ở Giai đoạn A**.
Chỉ sang Giai đoạn B khi cần đo web hiện tại để làm rõ câu hỏi, prompt yêu cầu ghi dev đang theo phía nào,
hoặc case còn vế `MATCH` phải verify.

---

# GIAI ĐOẠN B — đo

## Chuẩn bị

1. **Đăng nhập đúng vai trò** theo đặc tả và bằng chứng đối tác. Tài khoản quản trị chỉ được dùng để ra verdict
   khi quản trị chính là vai trò của vế Cn; nếu không, chỉ dùng để chuẩn bị dữ liệu/điều tra. Ghi tài khoản đã dùng.
2. **Tải lại trang** trước lô đo. Ghi môi trường và định danh bản dựng/deploy mà dự án đang công bố; nếu không
   có thì ghi thời điểm đo. Với các case liên tiếp trên cùng env và phiên, dùng chung thông tin này; chỉ kiểm
   lại khi phiên bị thay, có deploy giữa lượt hoặc hành vi cho thấy có thể đang chạy bản khác.
3. **Chuẩn bị tiền đề tối thiểu**, không chạy lại FLOW 01 và không mặc định tạo mới toàn bộ vòng đời.
   - Ưu tiên **dùng lại dữ liệu QA có sẵn** nếu truy được ID, đúng vai trò · trạng thái · env và chưa bị thay đổi.
   - Chỉ tạo phần còn thiếu. Chỉ tạo bản ghi mới khi **chính vế bug** nằm ở bước tạo/chuyển trạng thái, SRS
     phân biệt dữ liệu cũ/mới, có bằng chứng fix chỉ hiệu lực với dữ liệu sau deploy, hoặc không còn dữ liệu QA
     tương đương. Không có một trong các lý do này → dùng bản ghi sẵn có.
   - Chỉ seed qua cách đã được prompt cho phép và khi phần seed không phải hành vi đang tranh chấp; seed xong
     phải mở UI kiểm trạng thái cuối. **Cấm tự đoán endpoint, cấm ghi thẳng DB.**
   - Tệp seed phải là fixture thật, đọc được đúng định dạng. **Cấm tạo chuỗi chữ rồi đổi đuôi
     `.png/.xlsx/.docx`**; tái dùng fixture đã kiểm tra khi các case cần cùng loại dữ liệu.
   - Tiền đề tạo được mà không chuẩn bị → **CẤM chốt**. Không thể tạo → **Chưa chốt**, nêu rõ cần bổ sung dữ liệu gì.
   - Không đụng dữ liệu đối tác; bằng chứng không cho biết bản ghi nào thì dùng/tạo dữ liệu QA tương đương.
4. **Biến thể bắt buộc chưa tồn tại → được seed.** Bắt buộc khai vào báo cáo: **đổi bản ghi nào · đổi gì ·
   trên env nào** (seed là mutate môi trường của người khác).

**Chống dò mò:** không đoán khóa JSON/ID/endpoint — đọc keys/schema và endpoint danh sách trước khi dùng;
không dump toàn bộ DOM — script chỉ trả count/text/ID cần cho vế đang đo; tái dùng phiên đăng nhập khi còn
hợp lệ và cùng role. Đủ đường UI + đối chứng của vế thì dừng, không tiện tay kiểm thêm field/module khác.

## Chạy

5. Từ tiền đề đã kiểm tra, **chạy đủ phần luồng đang verify tới bước sinh ra lỗi cũ**. Hành động đang tranh
   chấp phải thực hiện bằng **UI thật**; API/DB/log chỉ dùng để đối chứng ở bước 8, không thay thao tác đó.
   🔴 **CẤM Pass bằng quan sát tĩnh** (*"thấy field đã có rồi"*) nếu vế bug là hành động. Không bấm lặp lại chỉ
   để dò double-submit/double-toast, trừ khi vế Cn hoặc SRS yêu cầu hành vi khi bấm lặp.
6. **Chỉ cài bộ bắt thông báo/lớp nổi khi nó thuộc vế Cn hoặc là output bắt buộc của hành động đang đo**, và
   cài trước thao tác. Ghi đúng nội dung người dùng nhìn thấy và gắn với thao tác vừa chạy. Chỉ đối chiếu các
   thuộc tính mà vế Cn/SRS yêu cầu; thông báo ngoài Cn chỉ đi qua gate bug mới, không đổi verdict bug gốc.

7. **Chỉ chụp khi quan sát cho thấy FAIL cần chứng minh**; setup và case Pass chỉ ghi ID + trạng thái/số liệu quyết định.
   Mỗi artifact lỗi phải nêu điều nó chứng minh và mốc thời gian/ID bản ghi; mở lại để xác nhận nội dung khớp
   mô tả. Không lặp thao tác chỉ để chụp lại output thoáng qua; dùng chữ đã bắt + phản hồi máy chủ.

8. **Đo bằng con số, rồi đối chứng bằng đúng một phương pháp độc lập phù hợp với claim.** Trạng thái lưu → đọc
   lại API/bản ghi; hiển thị → đối chiếu DOM/dữ liệu nguồn; file xuất → mở nội dung và chỉ kiểm các thuộc tính
   vế Cn/SRS yêu cầu. Chỉ kiểm cache, người nhận hoặc kênh thông báo khi chính vế Cn/SRS yêu cầu. Bấm lại cùng
   một nút không tính là phương pháp thứ hai. Hai đường đã khớp thì không thêm đường thứ ba. **Hai phép mâu
   thuẫn = CHƯA được chốt** — ghi cả hai, hỏi user. Verdict phụ thuộc file thì phải giữ lại chính file hoặc
   manifest có thể truy lại nội dung; screenshot/toast không thay được việc mở file.

   **Dấu hiệu phép đo đang nói dối** — gặp thì đo lại, chưa được chốt: đếm gộp thẻ bọc ngoài với thẻ con →
   số nhân đôi · một thông báo ra hai bản ghi cùng mốc giờ → đếm theo **mốc giờ khác nhau**, không theo độ
   dài mảng · chữ người dùng nhìn thấy phải đọc bằng `innerText` (`textContent` gom cả node ẩn → **bug ma**)
   · ảnh chụp toàn trang làm trang vẽ lại → luôn mở ảnh xem lại · các chiều số liệu **không cộng khớp tổng**
   → số đang sai, chưa được dùng. Xem số thô trước, đừng lọc/gộp rồi mới nhìn.

Trước khi chốt, chỉ so các điều kiện **có thể đổi kết quả** với case đối tác: vai trò, trạng thái bản ghi, dữ
liệu tiền đề và input/bộ lọc. Chênh lệch liên quan mà chưa giải quyết được → chưa chốt và nêu đúng dữ kiện còn
thiếu; không mở rộng sang mọi nhánh có thể tưởng tượng. Chuẩn chấm chỉ được đổi khi tìm thấy căn cứ SRS mới,
phải ghi lý do và đo lại phần bị ảnh hưởng.

---

# Chốt

## Verdict

| Verdict logic | Khi nào |
|---|---|
| **Pass** | Mọi vế đều `MATCH`, phép đo đạt chuẩn rút từ SRS và không còn vế `DIFF/GAP` |
| **Reopen** | Ít nhất một vế `MATCH` vẫn sai hoặc mới đúng một phần; với vế `DIFF`, chỉ Reopen phần độc lập mà SRS và expected cùng yêu cầu nhưng web đều không đạt |
| **Không phải lỗi** | Chỉ dùng cho `MATCH`: đối tác sai vai trò/tiền đề/bước và SRS quy định rõ điều kiện đúng; phải có phép đo xác nhận |
| **Cần BA** | Có `DIFF` giữa SRS và expected đối tác, hoặc `GAP` do SRS im lặng/tự mâu thuẫn; dev đúng SRS hiện tại vẫn thuộc nhóm này |
| **Chưa chốt** | Thiếu tiền đề/bằng chứng quyết định, hai phép đo mâu thuẫn hoặc blocker khách quan khiến chưa thể đo đúng vế |

Verdict chỉ có hiệu lực cho môi trường và bản dựng/thời điểm đã đo. Khác môi trường không tự động đổi Pass
thành Chưa chốt hay Reopen; chỉ ghi rõ giới hạn hiệu lực và quan sát thực tế ở từng môi trường nếu có.

## Ca biên

- **Case gộp nhiều vế:** mọi vế `MATCH` và hết lỗi mới Pass · còn ≥1 vế `MATCH` vẫn lỗi → **Reopen**; nếu đồng
  thời có vế `DIFF/GAP` thì kết quả logic là **Reopen + cần BA**, nêu riêng vế lỗi và câu hỏi BA. Không vế nào
  Reopen mà còn `DIFF/GAP` → **Cần BA**.
- **Quan sát ngoài vế đối tác nêu:** xử theo gate “Bug mới phát sinh trong lúc verify” bên dưới; không tự mở rộng
  sang màn, vai trò hoặc bộ lọc không cần cho case.
- **Không biết trước khi fix nó thế nào.** Không có ảnh "lỗi cũ" của mình ⇒ **không suy ra được fix có tác
  dụng hay không**, chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**. Ghi đúng như vậy, đừng viết
  *"fix đã có tác dụng"*.
- **Bug về trường lưu trong DB:** dùng bản ghi đúng tiền đề đối tác. Chỉ đo thêm bản ghi mới/cũ khi qua điều
  kiện tạo dữ liệu ở Giai đoạn B; bản chất “có lưu DB” không tự động cho phép mở rộng old × new matrix.
- Dev mô tả fix ở chỗ khác với triệu chứng → vẫn **chạy đủ luồng**, đừng tin mô tả.

## Nội dung kết quả tối thiểu

Trình bày theo mẫu prompt nếu có; flow chỉ yêu cầu nội dung đủ để kiểm toán lại. Dòng đầu luôn dùng icon trung
tính `📌`, không dùng lại icon của mục chi tiết:

- `📌 KẾT QUẢ CHUNG: HIỆN TẠI ĐẠT` — hoặc `ĐÃ HẾT LỖI` khi có bằng chứng lỗi cũ
- `📌 KẾT QUẢ CHUNG: CÒN LỖI (REOPEN)`
- `📌 KẾT QUẢ CHUNG: KHÔNG PHẢI LỖI`
- `📌 KẾT QUẢ CHUNG: CẦN BA XÁC NHẬN`
- `📌 KẾT QUẢ CHUNG: CÒN LỖI (REOPEN) + CẦN BA XÁC NHẬN`
- `📌 KẾT QUẢ CHUNG: CHƯA THỂ KẾT LUẬN`

Sau đó chỉ ghi các mục thực sự có nội dung:

| Mục | Phải trả lời rõ |
|---|---|
| `❌ CÒN LỖI — <hành vi sai cụ thể>` | Kết quả mong đợi · kết quả thực tế + số liệu quyết định · dev cần sửa |
| `❓ CẦN BA XÁC NHẬN — <điểm chưa chốt>` | Expected ↔ SRS · kết quả thực tế · một câu hỏi BA trả lời trực tiếp · ghi rõ chưa chấm đạt/lỗi |
| `✅ ĐÃ HẾT LỖI — <lỗi gốc>` | Kết quả mong đợi · kết quả thực tế + số liệu quyết định; chỉ dùng khi có bằng chứng lỗi cũ |
| `✅ HIỆN TẠI ĐẠT — <hành vi>` | Kết quả mong đợi · kết quả thực tế; dùng khi phép đo đạt nhưng không có bằng chứng tin cậy về lỗi trước đó |
| `✅ KHÔNG PHẢI LỖI — <lý do>` | Kết quả mong đợi đúng theo SRS/BA · kết quả thực tế xác nhận |
| `⏸ CHƯA CHỐT — <phần chưa kết luận>` | Kết quả cần kiểm tra · kết quả thực tế/điều kiện còn thiếu · dữ kiện cần bổ sung |
| `🔎 PHẠM VI ĐÃ ĐO` | URL môi trường · bản dựng/thời điểm · role · dữ liệu/biến thể quyết định |

Nghĩa icon cố định: `📌` tổng kết · `❌` còn lỗi/xác nhận là bug · `❓` cần BA · `✅` đạt/không phải lỗi ·
`⏸` chưa đủ căn cứ · `🔎` phạm vi đã kiểm tra. `⚠️` chỉ dùng cho caveat/cảnh báo, không dùng làm verdict.
Cấm đảo nghĩa icon theo cách diễn đạt của verdict.

Mỗi mục có phép đo web chỉ ghi ngắn gọn `Kết quả mong đợi` và `Kết quả thực tế`; số liệu quyết định đặt ngay
trong kết quả thực tế. `CÒN LỖI` thêm `Dev cần sửa`; `CẦN BA` thêm câu hỏi; `CHƯA CHỐT` thêm dữ kiện cần bổ
sung. Lịch sử điều tra để trong hồ sơ audit; cột ảnh chỉ nhận artifact lỗi theo luật ở đầu flow, không dùng
cho Pass.

```text
📌 KẾT QUẢ CHUNG: <verdict>
<icon> <MỤC KẾT QUẢ> — <hành vi>
- Kết quả mong đợi: <hành vi cần đạt>.
- Kết quả thực tế: <hành vi đo được + số liệu quyết định>.
🔎 PHẠM VI ĐÃ ĐO: <URL môi trường> · <thời gian/bản dựng> · <vai trò>.
```

```text
❌ CÒN LỖI — <nêu chính xác hành vi đang sai>
- Kết quả mong đợi: <expected và SRS file:dòng quy định gì>.
- Kết quả thực tế: <đúng tiền đề · output sai · số đo/ví dụ quyết định · phạm vi tái hiện>.
- Dev cần sửa: <kết quả quan sát được phải đạt; không đoán nguyên nhân, không ép cách triển khai>.
```

**Với vế `DIFF`:** mục kết quả phải có câu
`❓ CẦN BA XÁC NHẬN: đối tác kỳ vọng <…>; SRS quy định <…> (file:dòng); web/dev hiện tại <…>.`
Nếu case gộp phải Reopen vì vế khác, câu này và câu hỏi BA vẫn bắt buộc trong kết quả logic.

**Với vế `GAP` mà web đang làm đúng y nguyên kỳ vọng đối tác:** vẫn **không** được Pass (luật khóa 5) — nhưng
tóm tắt phải nói rõ để người ngoài không đọc nhầm thành lỗi chưa xử lý. `WEB HIỆN TẠI` ghi *"đúng kỳ vọng đối
tác"*, và `CÂU HỎI BA` phải nêu đúng mục đích: **bổ sung điều này vào đặc tả**, không phải chặn bàn giao.

---

## Hồ sơ tái hiện chỉ khi cần

Pass / Không phải lỗi / Cần BA / Chưa chốt chỉ cần kết quả tối thiểu ở trên, trừ khi prompt yêu cầu thêm.
**Chỉ Reopen và bug mới đã xác nhận** cần khối `CÁCH VERIFY`, vì đây là bản giao việc cho dev + QA vòng sau.
Tạo một bản chuẩn đủ để người chưa từng chạm case tự chạy lại; nếu cần đưa tới nhiều nơi, tái dùng cùng nội dung.

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
Artifact lỗi lần này: <đường dẫn ảnh/file/response>
```

Rule chất lượng: khối này phải sao lại phép thử đã khóa từ expected + SRS **trước khi đo**. Mỗi bước phải trả
lời trực tiếp một phần của vế lỗi. Không Pass bằng dữ liệu mà hành vi cũ và mới đều có thể cho cùng kết quả,
khi mới đo một phần hoặc thiếu biến thể bắt buộc. Không Fail khi sai tiền đề, thiếu dữ liệu hoặc chưa nối được
bằng chứng. Lặp lại cùng tín hiệu không phải đối chứng; trường hợp biên chưa được expected/SRS quy định → Cần
BA. `DIFF/GAP` không viết thành PASS/FAIL.

## Bug mới tự lộ — không exploratory

Trong lúc chạy tiền đề, thao tác hoặc đọc output bắt buộc của case, không được bỏ qua sai lệch rõ ràng trong
chính màn/phản hồi/tệp đang quan sát. Được đọc một lượt phần đang hiển thị, nhưng không bấm thử từng field/nút,
không chạy checklist regression và không mở chức năng khác chỉ để tìm bug.

1. Mở SRS thật, dẫn `file:dòng`. SRS im lặng → candidate; SRS mâu thuẫn → candidate + câu hỏi BA. Cả hai:
   không log như bug đã xác nhận.
2. Tra phiếu trùng trước khi đo thêm. Đã có phiếu → liên kết và dừng xử lý hiện tượng này; tiếp tục hoàn tất
   case gốc.
3. Artifact sẵn có chưa đủ → ngoài các phép đo bắt buộc của case, cả case chỉ được thêm tối đa **1 phép xác nhận**
   cho bug mới. Phép xác nhận giữ nguyên role/dữ liệu/bộ lọc; chỉ được replay đúng thao tác, hoặc đọc một kết quả/
   side effect trực tiếp đã phát sinh từ cùng bản ghi/giao dịch. Thao tác có thể làm thay đổi dữ liệu/trạng thái
   nghiệp vụ hoặc tạo thêm đầu ra nghiệp vụ mới — như gửi mail/thông báo, tạo hoặc sửa bản ghi, giao dịch hay tệp —
   thì **KHÔNG replay**; chỉ đọc lại kết quả/side effect đã có. Không seed, không thực hiện chức năng hoặc luồng
   nghiệp vụ khác.
4. Đủ SRS + artifact + đối chứng độc lập → log bug mới và tạo `CÁCH VERIFY`. Chưa đủ sau phép xác nhận → candidate,
   không điều tra tiếp.
5. Nhiều hiện tượng cùng lộ: hiện tượng đủ bằng chứng sẵn có thì log; hiện tượng cần thêm thao tác ghi candidate,
   không cộng thêm lượt xác nhận.
6. Bug mới chỉ đổi verdict case gốc khi làm điều kiện PASS không đạt hoặc chặn chính phép đo bắt buộc; trường hợp
   khác log riêng.

Candidate: `<hiện tượng> · xuất hiện tại <bước> · artifact <...> · còn thiếu <...> để xác nhận`.
Nơi lưu, mã bug và cách cập nhật theo prompt; không có chỉ dẫn thì đưa vào bàn giao cuối, cấm tự suy đích/mã.

**Cổng hỏi BA:** Chỉ hỏi khi đã mở đúng SRS trong chính case, đọc trọn đoạn/bảng liên quan và vẫn còn `DIFF/GAP`;
không hỏi chỉ từ mô tả, web, note cũ hoặc suy đoán. Câu hỏi phải kèm expected ↔ SRS `file:dòng`, hoặc `IM LẶNG`
kèm vị trí đã rà, và chỉ cần BA chốt một quyết định. Dùng lại trích dẫn đã có trong case, không quét toàn module;
thiếu dữ liệu, tài khoản, môi trường hoặc quyền truy cập là blocker vận hành, không hỏi BA.

## Cổng chốt verdict

Trước khi chốt mỗi case, trả lời đủ:

1. Mỗi vế chấm được neo vào dòng nào của đúng SRS prompt cung cấp?
2. Mọi thao tác đã chạy có trả lời một vế Cn hoặc là đối chứng độc lập của vế đó không?
3. Mọi vế `DIFF/GAP` đã bị chặn Pass và có câu hỏi BA đúng phần mâu thuẫn/thiếu chưa?
4. Đã đọc đầy đủ expected và các phản hồi liên quan của case, không dựa trên bản cắt ngắn chưa?
5. Điều kiện đo có khớp các tiền đề liên quan của case; nếu khác thì ảnh hưởng đã được xử lý chưa?

Flow kết thúc ở verdict + nội dung căn cứ. Nơi lưu, trường cần cập nhật, giá trị và cách cập nhật hoàn toàn theo
prompt; chúng không được làm thay đổi verdict hoặc buộc mở thêm phép đo. Có thể xử lý Giai đoạn A theo lô cho
các case cùng module; Giai đoạn B giữ cùng phiên khi còn hợp lệ và cùng vai trò.

## Bàn giao cuối

Theo format của prompt. Nếu prompt không quy định format, tóm tắt: kết quả từng case + bằng chứng; bug mới
hoặc candidate; dữ liệu đã seed/thay đổi; case Chưa chốt và dữ kiện cần bổ sung.

Nếu trong đợt chạy có bằng chứng chính flow làm giảm chất lượng kết quả hoặc gây thao tác thừa lặp lại, thêm
`CẢI TIẾN FLOW: <vấn đề> · <ảnh hưởng> · <rule/chỗ cần xem lại>`. Không có thì bỏ mục; không đo thêm chỉ để
đánh giá flow và không tự sửa flow trong phiên verify.
