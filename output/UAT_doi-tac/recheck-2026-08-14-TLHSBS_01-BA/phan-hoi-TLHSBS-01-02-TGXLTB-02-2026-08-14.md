# Phiếu phản hồi — `TLHSBS_01` · `TLHSBS_02` · `TGXLTB_02`: hai thẻ chỉ số tổng hợp trên Trang Tổng quan

*Ngày soạn: 14/08/2026 · Nhóm I — Trang Tổng quan (Dashboard) · Sổ theo dõi tab `bug`, dòng **39**, **40**, **44**, Tuần 1*

**Ghi chú phương pháp:**

- Đã đọc trọn các mục liên quan của bản gốc: khuôn chung TPL-DASH-KPI (`srs-fr-01-dashboard.md:169–226`), KPI-S-01 và KPI-S-02 (`:556–631`), màn hình SCR-I-01 (`:675–901`) gồm cả bảng 9 thẻ, Trạng thái đặc biệt và ma trận phân quyền.
- Bản `.docx` đối tác cầm ở Tuần 1 xác định được là **v2.0**: phiếu kiểm thử gọi thẻ là *"Tỷ lệ hố sơ bổ sung"*, khớp nhãn *"Tỷ lệ **hồ sơ** phải bổ sung"* của v2.0 §4.1.10 — bản v3.5 và bản gốc `.md` đã đổi thành *"Tỷ lệ **vụ việc** phải bổ sung"*. Vẫn tra chéo cả hai bản `.docx`; kết luận không phụ thuộc bản nào.
- `TLHSBS_01` đã đo lại trên môi trường kiểm thử chiều 14/08 (tài khoản Cán bộ Nghiệp vụ Trung ương, bộ lọc Năm 2026 · Cả năm · Toàn quốc); ảnh chụp, bản ghi cấu trúc màn hình và phản hồi máy chủ lưu tại `docs/Reference/recheck-2026-08-14-TLHSBS_01-BA/`, phần đối soát ở `BA-doi-soat-ket-qua-do-lai.md` cùng thư mục. Minh chứng của hai mã còn lại chưa có trong kho nội bộ: `TGXLTB_02` dùng ảnh tên `TGXLTB_01.jpg`, `TLHSBS_02` dùng chung ảnh với `TLHSBS_01` — ảnh có thể không ghi lại đúng thao tác bấm thẻ.

## Thay đổi kể từ lượt duyệt gần nhất

| Mục | Đổi gì | Kết luận có đổi không | Mức đọc lại |
|---|---|---|---|
| `TLHSBS_01` | Đã có kết quả đo lại chiều 14/08 — nhánh treo được khép | **Có đổi:** từ *"chờ đo lại, chưa gán Loại"* → **case lai: Loại 3 ở vế công thức + Loại 1 ở vế hiển thị**. Vế Loại 1 chốt được nhờ mẫu số đo được ≥ 11 | (a) đọc kỹ |
| `TLHSBS_02` · `TGXLTB_02` | — (lượt đầu) | — | Đọc đầy đủ |

## Bối cảnh nghiệp vụ

Trang Tổng quan có 9 thẻ chỉ số. Bảy thẻ đầu là **đếm số lượng** bản ghi — hỏi đáp mới, vụ việc tiếp nhận, vụ việc đang hỗ trợ, vụ việc hoàn thành, khóa đào tạo đang diễn ra, khóa đào tạo đã hoàn thành, chuyên gia/tư vấn viên đang hoạt động — nên mỗi thẻ ứng với một danh sách bản ghi có thật, bấm vào thẻ thì mở danh sách đó. Hai thẻ còn lại là **chỉ số đo chất lượng quy trình**: *Tỷ lệ vụ việc phải bổ sung* (một tỷ lệ phần trăm) và *Thời gian xử lý trung bình* (số ngày làm việc bình quân). Hai thẻ này không đếm bản ghi mà tính ra một con số từ nhiều bản ghi, nên không có danh sách nào tương ứng để mở.

---

## `TLHSBS_01` — Thẻ Tỷ lệ vụ việc phải bổ sung báo "Chưa có dữ liệu" trong kỳ đang có 23 vụ hoàn thành

**Vấn đề:** Đơn vị kiểm thử mở Trang Tổng quan, thấy thẻ *Tỷ lệ hồ sơ bổ sung* hiện số 0 dù trong hệ thống đang có hồ sơ ở trạng thái chờ doanh nghiệp bổ sung, nên kết luận số liệu sai. Thực chất thẻ này không đếm hồ sơ đang chờ bổ sung: nó đo **chất lượng hồ sơ đầu vào trên nhóm vụ việc đã xử lý xong** — trong số vụ đã hoàn thành trong kỳ, bao nhiêu phần trăm từng phải yêu cầu doanh nghiệp bổ sung. Hồ sơ còn đang chờ bổ sung chưa hoàn thành nên chưa được tính, và điều đó là đúng thiết kế. Nhưng đo lại chiều 14/08 lộ ra một lỗi khác nằm ngay cạnh: kỳ được xem có tới 23 vụ việc hoàn thành, mà thẻ vẫn kèm dòng **"Chưa có dữ liệu"** — tức phần mềm đang báo không có gì để tính trong khi rõ ràng có. Người đọc vì thế không phân biệt được "kỳ này không hồ sơ nào phải bổ sung" với "chưa tính được", hai câu dẫn tới hai đánh giá trái ngược về chất lượng hồ sơ đầu vào.

| Tình huống trong kỳ đã chọn | Vụ đã hoàn thành | Trong đó từng bị yêu cầu bổ sung | Hồ sơ đang chờ bổ sung (chưa hoàn thành) | Thẻ phải hiện |
|---|---|---|---|---|
| Kỳ có nhiều vụ đóng | 100 | 30 | 5 | **30,0%** |
| Kỳ có vụ đóng, hồ sơ đều sạch | 10 | 0 | 8 | **0,0%** — không kèm dòng "Chưa có dữ liệu" |
| Kỳ chưa có vụ nào đóng | 0 | — | 12 | **"—"** (không phải 0) |
| **Hiện trạng đo ngày 14/08** | **23** | chưa đếm được | — | thẻ đang hiện **"0" + "Chưa có dữ liệu"** ⇒ sai ở cả hai cách đọc |

**(1) Phần mềm đúng SRS chưa? → Hai vế khác nhau.**

- **Vế công thức: phần mềm không sai.** `srs-fr-01-dashboard.md:580` — *"Tập mẫu số = số vụ việc trạng thái "Hoàn thành" có ngày hoàn thành nằm trong khoảng đầu kỳ–cuối kỳ… Tập tử số = số vụ việc **trong mẫu số** đã từng đi qua trạng thái "Yêu cầu bổ sung" ít nhất 1 lần"*. Hồ sơ đang ở trạng thái *Yêu cầu bổ sung* mà chưa hoàn thành **không** nằm trong mẫu số lẫn tử số.
- **Vế hiển thị: phần mềm SAI — đã đo lại chiều 14/08 và khép được.** Thẻ đang chạy nhánh **không có dữ liệu** trong khi mẫu số lớn hơn 0: thẻ hiện *"0"* + *"%"* + dòng *"Chưa có dữ liệu"* + xu hướng *"—"*, mà cùng bộ lọc đó danh sách trả về **23 vụ** có ngày hoàn thành trong kỳ (đếm 20 bản ghi trang đầu: **11 vụ "Hoàn thành" + 9 vụ "Đã đánh giá"**), và thẻ *Thời gian xử lý trung bình* dùng **cùng tập mẫu** (`:609`) vẫn tính ra **11,7 ngày**. Theo bản gốc, mẫu số > 0 thì thẻ phải hiện tỷ lệ một chữ số thập phân (`:780`) và **không** kèm dòng trạng thái trống (`:841`); chỉ khi mẫu số = 0 mới hiện *"—"* (`:580`, `:591`). Bằng chứng: `docs/Reference/recheck-2026-08-14-TLHSBS_01-BA/`.
- **Vế tử số: chưa kết luận được, và đừng dùng bằng chứng của lượt đo lại.** Lượt đo lấy vụ `VV-BTP-TW-20260712-005` làm chứng cho tử số vì dòng thời gian có sự kiện *"Bổ sung hồ sơ"*. Đó là **thao tác thêm tài liệu vào hồ sơ**, không phải **trạng thái *Yêu cầu bổ sung*** mà `:580` yêu cầu — đọc trọn 20 bản ghi lịch sử của vụ đó, các trạng thái đi qua là Đã tiếp nhận → Đang kiểm tra → Đang xử lý → Chờ phê duyệt → Đã duyệt → Hoàn thành, riêng bản ghi *Bổ sung hồ sơ* không kèm trạng thái nào. Vụ này **không thuộc tử số**, nên chưa có căn cứ nói giá trị đúng phải lớn hơn 0.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không, và bản v3.5 còn nói rõ hơn.**

- `HTPLDN-PTYC-CT-v2.0.docx` §4.1.10: *"Số vụ việc từng qua trạng thái "Yêu cầu bổ sung" chia cho **tổng số vụ việc đã hoàn thành trong kỳ**, nhân 100"*.
- `HTPLDN-PTYC-CT-v3.5.docx` §4.1.10.2.2: *"Mẫu số là số vụ việc ở trạng thái "Hoàn thành" có ngày hoàn thành trong kỳ đã chọn… **Khi mẫu số bằng 0 thì hiển thị "—" và không tính xu hướng**"*.

⇒ Kỳ vọng *"số liệu phải khác 0 vì đang có hồ sơ chờ bổ sung"* không có gốc ở bản nào.

**(2) Đối tác yêu cầu có khác SRS không? → Có, ở cách hiểu chỉ số.** Phiếu đo thẻ như thể nó đếm hồ sơ đang chờ bổ sung tại thời điểm xem; bản gốc định nghĩa nó là tỷ lệ trên nhóm vụ đã hoàn thành trong kỳ. Muốn theo dõi lượng hồ sơ đang chờ bổ sung thì đó là một chỉ số khác, hiện không có trên Trang Tổng quan.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → Không, ở vế công thức** — đổi định nghĩa chỉ số không phục vụ luồng xử lý nào, chỉ là mong muốn xem thêm thông tin. **Có, ở vế hiển thị** — thẻ vừa hiện số 0 vừa báo "Chưa có dữ liệu" thì người đọc không biết đang ở tình huống nào: "kỳ này không hồ sơ nào phải bổ sung" hay "hệ thống chưa tính được". Hai câu dẫn tới hai đánh giá trái ngược về chất lượng hồ sơ đầu vào, mà đây lại chính là chỉ số dùng để đánh giá điều đó.

**→ Kết luận: case lai. Vế công thức — Loại 3: không sửa, phần mềm đúng bản gốc; kỳ vọng "thẻ phải khác 0 vì đang có hồ sơ chờ bổ sung" là hiểu sai chỉ số, đề nghị đối tác cập nhật Kết quả mong đợi. Vế hiển thị — Loại 1: lỗi phần mềm, Dev sửa theo bản gốc: khi trong kỳ có ít nhất một vụ việc hoàn thành thì thẻ phải hiện tỷ lệ một chữ số thập phân kèm dấu phần trăm và bỏ dòng "Chưa có dữ liệu"; chỉ khi không có vụ nào hoàn thành mới hiện "—" và bỏ chỉ dấu xu hướng. Dev action: Có · Sửa đặc tả: Không → Sheet: cột *Trạng thái dev fix* ghi `InProcess` cho dòng 39 (còn phần Dev phải sửa nên chưa đóng).**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Thẻ *Tỷ lệ vụ việc phải bổ sung* trên Trang Tổng quan đo chất lượng hồ sơ đầu vào của nhóm vụ việc **đã xử lý xong trong kỳ**: mẫu số là số vụ việc đã hoàn thành, tử số là số vụ trong đó từng phải yêu cầu doanh nghiệp bổ sung (một vụ bổ sung nhiều lần vẫn tính một lần). Hồ sơ còn đang chờ doanh nghiệp bổ sung chưa hoàn thành nên chưa tham gia phép tính — đây là thiết kế nêu tại mục 4.1.10 của tài liệu phân tích yêu cầu chi tiết. Vì vậy việc thẻ hiện giá trị 0 trong khi hệ thống đang có hồ sơ chờ bổ sung không phải là biểu hiện sai số liệu.
> **[Nhận định]** Kính đề nghị Quý đơn vị cập nhật Kết quả mong đợi của trường hợp kiểm thử này theo đúng định nghĩa nêu trên. Qua đo lại ngày 14/08 chúng tôi ghi nhận thẻ đang hiển thị dòng "Chưa có dữ liệu" trong khi kỳ được chọn có vụ việc hoàn thành — phần này là lỗi của phần mềm và sẽ được chỉnh sửa. Khi kiểm thử lại, kính đề nghị Quý đơn vị ghi kèm số vụ việc đã hoàn thành trong kỳ và số vụ trong đó từng bị yêu cầu bổ sung, để đối chiếu trực tiếp với tỷ lệ hiển thị trên thẻ.

**Việc Dev:** Sửa nhánh tính của thẻ theo đúng kết luận trên; tử số đếm theo **trạng thái *Yêu cầu bổ sung*** mà vụ việc đã từng đi qua, **không** đếm thao tác *Bổ sung hồ sơ* trên dòng thời gian (hai thứ khác nhau — xem phần đối soát tại `docs/Reference/recheck-2026-08-14-TLHSBS_01-BA/BA-doi-soat-ket-qua-do-lai.md`); một vụ đi qua nhiều lần vẫn chỉ tính một lần. *Nghiệm thu:* trên bộ lọc Năm 2026 · Cả năm · Toàn quốc, thẻ hiện tỷ lệ dạng "x,x%" và không còn dòng "Chưa có dữ liệu"; đưa một vụ việc qua kết luận kiểm tra *Yêu cầu bổ sung* rồi cho hoàn thành trong kỳ thì tỷ lệ tăng tương ứng.

---

## `TLHSBS_02` · `TGXLTB_02` — Bấm hai thẻ chỉ số tổng hợp không mở danh sách chi tiết

*Hai mã cùng một lỗi gốc nên phân tích chung; phản hồi ghi vào cả hai dòng 40 và 44.*

**Vấn đề:** Đơn vị kiểm thử bấm vào thẻ *Tỷ lệ hồ sơ bổ sung* và thẻ *Thời gian xử lý trung bình*, chờ hệ thống mở danh sách chi tiết như bảy thẻ còn lại, nhưng không có gì xảy ra. Hai thẻ này theo thiết kế **không có thao tác bấm**: chúng không đếm bản ghi mà tính ra một tỷ lệ và một số ngày bình quân, nên không có danh sách bản ghi nào tương ứng để mở. Bảy thẻ đếm số lượng đều mở được danh sách và đã được chấm Pass, cho thấy phần mềm đang làm đúng đúng chỗ cần làm.

**(1) Phần mềm đúng SRS chưa? → ĐÚNG.** Bản gốc nói bốn chỗ độc lập:

- `srs-fr-01-dashboard.md:586` (KPI-S-01) và `:615` (KPI-S-02) — *"**Drill-down: không có** (chỉ số tổng hợp, không có danh sách chi tiết tương ứng)"*.
- `:629–630` — bảng tóm tắt, cột *Xem chi tiết* của cả hai KPI = *"không"*.
- `:809–810` — bảng 9 thẻ của màn hình SCR-I-01, cột *Xem chi tiết*: *"❌ (chỉ số tổng hợp)"*. Đếm cả bảng `:805–813`: **7 thẻ ✅ / 2 thẻ ❌**.
- `:849` — quy tắc tương tác: *"Nhấn thẻ KPI **có xem chi tiết** → chuyển đến module chi tiết"*; ma trận phân quyền `:881–884` chỉ có bốn dòng điều hướng cho hỏi đáp, vụ việc, khóa học, tư vấn viên — **không có dòng nào** cho hai thẻ tổng hợp.

Sổ theo dõi cũng khớp: bảy trường hợp bấm thẻ ở các dòng **18 · 21 · 24 · 27 · 30 · 33 · 36** đều Pass, chỉ hai thẻ tổng hợp không mở danh sách (đếm các dòng có mô tả *"Click …"* trong nhóm Dashboard). Bản ghi cấu trúc màn hình thu được khi đo lại ngày 14/08 (`recheck-2026-08-14-TLHSBS_01-BA/audit/dashboard-a11y.txt`) cho thấy phần mềm cố ý dựng như vậy: bảy thẻ kia là **nút** kèm nhãn *"…, xem chi tiết"*, còn hai thẻ tổng hợp chỉ là **văn bản tĩnh**, không phải nút.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không — cả hai bản đều nói y hệt, và v2.0 còn nói rõ hơn.**

- `HTPLDN-PTYC-CT-v2.0.docx`, quy trình xem chi tiết: *"Người dùng bấm vào thẻ chỉ số có hỗ trợ xem chi tiết (7 thẻ chỉ số chính). **Các thẻ chỉ số tổng hợp (Tỷ lệ vụ việc phải bổ sung, Thời gian xử lý trung bình) không có liên kết xem chi tiết**"*. Bảng mô tả màn hình dòng 14 và 15 ghi kiểu thành phần là *"Thẻ chỉ số (**không drill-down**)"* kèm câu *"Thẻ chỉ hiển thị, không có tương tác"*; §4.1.10 và §4.1.11 nhắc lại: *"không có màn hình chi tiết để điều hướng tới"*. Bản này thậm chí ghi nhận cách phần mềm thể hiện điều đó: *"prototype phân biệt hai thẻ này bằng kiểu hiển thị phẳng (không nổi bật khi di chuột), không có điều hướng"*.
- `HTPLDN-PTYC-CT-v3.5.docx` §4.1.10.2.3: *"Thẻ chỉ số này là chỉ số tổng hợp, không có màn hình danh sách chi tiết tương ứng nên **không có thao tác bấm để xem chi tiết**"*.

⇒ Không phải Loại 4: kỳ vọng trong phiếu ngược lại chính tài liệu đối tác được giao.

**(2) Đối tác yêu cầu có khác SRS không? → Có.** Phiếu đòi bấm thẻ phải mở danh sách; bản gốc và cả hai bản bàn giao đều nói hai thẻ này không có thao tác bấm.

**(3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? → KHÔNG.** Hai chỉ số này là con số tổng hợp xuyên nhiều quy trình, không có tập bản ghi tương ứng để liệt kê. Không có thao tác bấm thì không luồng xử lý nào bị tắc, không mất chứng cứ, không sai phân vai. Nhu cầu xem danh sách vụ việc từng phải bổ sung hoặc bảng thời gian xử lý từng vụ thuộc phạm vi **báo cáo thống kê (Nhóm IX)**, nơi có màn hình và tệp xuất riêng.

**→ Kết luận: Loại 3 — Không sửa, phần mềm đúng bản gốc và đúng cả tài liệu bàn giao; đề nghị đối tác cập nhật Kết quả mong đợi của hai trường hợp này thành "thẻ chỉ hiển thị, không có thao tác bấm", và nếu vẫn cần xem danh sách chi tiết thì ghi nhận vào danh sách yêu cầu cải tiến để xem xét ở phạm vi báo cáo thống kê. Dev action: Không · Sửa đặc tả: Không → Sheet: cột *Trạng thái dev fix* ghi `Reject` cho cả dòng 40 và 44.**

> **Phản hồi gửi đối tác:**
> **[Lý do]** Trang Tổng quan có chín thẻ chỉ số, trong đó bảy thẻ đếm số lượng bản ghi nên bấm vào mở được danh sách tương ứng, còn hai thẻ *Tỷ lệ vụ việc phải bổ sung* và *Thời gian xử lý trung bình* là chỉ số tổng hợp — một tỷ lệ phần trăm và một số ngày làm việc bình quân tính từ nhiều bản ghi, không ứng với danh sách nào. Tài liệu phân tích yêu cầu chi tiết mà Quý đơn vị đang sử dụng nêu rõ điều này ở phần quy trình xem chi tiết của nhóm Trang Tổng quan, ở bảng mô tả thông tin màn hình (hai thẻ được ghi là thẻ chỉ số không có xem chi tiết, chỉ hiển thị, không có tương tác) và ở hai mục đặc tả riêng của từng thẻ. Việc hệ thống không mở danh sách khi bấm hai thẻ này là đúng thiết kế.
> **[Nhận định]** Kính đề nghị Quý đơn vị cập nhật Kết quả mong đợi của hai trường hợp kiểm thử thành "thẻ chỉ hiển thị số liệu, không phát sinh thao tác bấm". Trường hợp Quý đơn vị thấy cần có danh sách vụ việc từng phải bổ sung hoặc bảng thời gian xử lý của từng vụ việc, kính đề nghị ghi nhận thành yêu cầu cải tiến để xem xét bổ sung ở nhóm chức năng báo cáo thống kê — nơi có màn hình danh sách và tệp xuất phục vụ mục đích tra cứu chi tiết.

---

## Điểm treo chuyển đợt sau

| Nội dung | Phát hiện ở mục nào | Thuộc bên nào | Trạng thái |
|---|---|---|---|
| Khuôn chung của nhóm Dashboard `:222` quy định không có dữ liệu thì *"hiển thị "0" cho KPI"*, trong khi mục riêng của hai thẻ tổng hợp buộc hiển thị *"—"* (`:580` và điều kiện chấp nhận `:591` cho thẻ tỷ lệ; `:609` *"tập rỗng → giá trị trống"* cùng điều kiện chấp nhận `:620` cho thẻ thời gian trung bình; bản `.docx` v3.5 §4.1.10.2.2 · §4.1.11.2.2 nói thẳng *"hiển thị "—""*). Hai câu chọi nhau ở đúng tình huống đang tranh chấp; đề nghị dọn khuôn chung theo hướng nêu ngoại lệ cho thẻ tỷ lệ và thẻ giá trị trung bình | `TLHSBS_01`, câu (1) | BA | Chờ chốt |
| Dòng **41** (`TLHSBS_03`) đang Pass với kỳ vọng *"Hiển thị 0/Không có dữ liệu"* — ngược quy định *"—"* của bản gốc, và trùng đúng biểu hiện vừa bị kết luận là lỗi ở dòng 39. Sau khi Dev sửa, dòng này phải đo lại trên một kỳ thật sự không có vụ hoàn thành, không giữ Pass | `TLHSBS_01`, câu (1) | QA | Chờ đo lại |
| Mẫu số có gồm vụ ở trạng thái *Đã đánh giá* hay không: bản gốc ghi mẫu số là vụ *"trạng thái Hoàn thành"*, còn phần mềm gộp *Hoàn thành* + *Đã đánh giá* vào một tab (đo ngày 14/08: 20 bản ghi trang đầu gồm 11 vụ *Hoàn thành* + 9 vụ *Đã đánh giá*). Hai cách đọc ra hai mẫu số khác nhau nên ra hai tỷ lệ khác nhau — chốt trước, nếu không bản sửa vẫn lệch kỳ vọng khi nghiệm thu | `TLHSBS_01`, câu (1) | BA | Chờ chốt |
| Nhãn thẻ trên phần mềm là *"Tỷ lệ hồ sơ bổ sung"* (ảnh đo lại ngày 14/08), trong khi bản gốc và bản bàn giao v3.5 ghi *"Tỷ lệ vụ việc phải bổ sung"* — bản v2.0 ghi *"Tỷ lệ hồ sơ phải bổ sung"*. Chính chữ "hồ sơ" khiến phiếu đọc chỉ số thành "hồ sơ đang chờ bổ sung" và đo sai hướng ngay từ đầu; đề nghị sửa nhãn cùng đợt Dev sửa `TLHSBS_01` | Ghi chú phương pháp | Dev · Bên soạn tài liệu bàn giao | Chờ sửa |
| Hai dòng **38** và **42** của sổ không có mã trường hợp kiểm thử lẫn nội dung nhưng cột *Final Status* vẫn mang giá trị Fail — làm sai số đếm khi lọc | Pha gom bằng chứng | QA | Chờ dọn |
| Chưa đếm được tử số thật — trong 23 vụ hoàn thành có bao nhiêu vụ từng đi qua trạng thái *Yêu cầu bổ sung*. Lượt đo ngày 14/08 chỉ mở lịch sử một vụ. Số này cần để nghiệm thu bản sửa | `TLHSBS_01`, câu (1) | QA | Chờ đo bổ sung |
| Minh chứng của `TLHSBS_02` và `TGXLTB_02` chưa có bản sao trong kho nội bộ; `TGXLTB_02` dùng ảnh tên `TGXLTB_01.jpg`, `TLHSBS_01` và `TLHSBS_02` dùng chung một ảnh. Riêng `TLHSBS_01` đã có bộ bằng chứng đo lại tại `docs/Reference/recheck-2026-08-14-TLHSBS_01-BA/` | Ghi chú phương pháp | QA | Chờ tải về |
