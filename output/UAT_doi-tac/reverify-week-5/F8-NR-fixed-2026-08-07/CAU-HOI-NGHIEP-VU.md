# Câu hỏi gửi nghiệp vụ — cụm Quản lý Hợp đồng Tư vấn (18 phiếu)

**Lập:** 07/08/2026 · **Người lập:** đội kiểm thử · **Nguồn đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`

---

## Đọc cái này trước

Đợt rà 18 phiếu cụm Hợp đồng Tư vấn có **60 điểm kỳ vọng**. Trong đó:

| | Số điểm | Nghĩa là |
|---|---|---|
| Đối chiếu được với đặc tả | **41** | Đội kiểm thử tự chấm đạt / chưa đạt, **không cần nghiệp vụ** |
| **Cần nghiệp vụ chốt** | **19** | Đặc tả **nói ngược** phiếu (4 điểm), hoặc **im lặng / tự mâu thuẫn** (15 điểm) |

19 điểm đó gom lại thành **11 câu hỏi** dưới đây.

**🔴 Xin đọc kỹ chỗ này để tránh hiểu nhầm:** phần lớn các câu dưới đây **không phải là lỗi phần mềm chưa
sửa**. Nhiều chỗ phần mềm đang chạy **đúng như đặc tả**, chỉ khác câu chữ trong phiếu kiểm thử; một số chỗ
phần mềm đang chạy **đúng như phiếu mong đợi** nhưng đặc tả chưa ghi điều đó. Cả hai trường hợp đội kiểm thử
đều **không được chấm đạt cũng không được chấm lỗi** — nên mới hỏi. Chỗ nào thật sự cần sửa phần mềm sẽ được
ghi rõ là **cần sửa**.

**Cách trả lời nhanh nhất:** mỗi câu có sẵn mục *"Đề nghị chốt"* với các phương án. Nghiệp vụ chỉ cần
đánh dấu phương án chọn; nếu chọn "giữ như hiện nay" thì đội kiểm thử sẽ tự sửa lại câu chữ của phiếu.

---

## Phần I — 4 câu **gửi được ngay**, không phụ thuộc kết quả đo

Đây là các câu chỉ liên quan tới **nội dung tài liệu**, trả lời được mà không cần biết phần mềm đang chạy ra sao.

---

### Câu 1 — Đặc tả trỏ tới một tệp thiết kế **không tìm thấy** ⟨3 điểm: `_02` · `_08` · `_09`⟩

Ba phiếu có kỳ vọng *"màn hình hiển thị giống với thiết kế"*. Để chấm được, đội kiểm thử cần bản thiết kế đó.

Đặc tả `srs-fr-14-hop-dong-tv.md:274` trỏ sang tệp `dac-ta-man-hinh-chuc-nang-v2.md`, phần `MH-14.1`.
**Tệp này không có trong bộ tài liệu chuẩn** — đã tìm toàn bộ kho tài liệu, không thấy.

**Đề nghị chốt — chọn một:**
- ☐ **(a)** Cấp bản thiết kế `MH-14.1` ⇒ đội kiểm thử đối chiếu rồi chấm.
- ☐ **(b)** Xác nhận **bảng thành phần màn hình trong chính đặc tả là chuẩn duy nhất**, bỏ dòng trỏ sang tệp kia ⇒ đội kiểm thử chấm theo bảng đó.

---

### Câu 2 — Chưa có quy ước về **tràn / đè bố cục** ⟨3 điểm: `_02` · `_08` · `_09`⟩

Ba phiếu có kỳ vọng *"nội dung không bị tràn, không bị đè lên nhau"*.

Đặc tả **có** hai quy ước gần nhất nhưng **không phải** quy ước này:
- Chuỗi quá dài thì **cắt bớt kèm chú thích khi rê chuột** (`srs-fr-05-vu-viec.md:1571`–`:1573`)
- **Độ phân giải màn hình tối thiểu** phải hỗ trợ (`:1603`, `srs-v3.5.md:6755`)

Không dòng nào nói thế nào là "tràn", thế nào là "đè", và đo ở độ phân giải nào thì tính.

**Đề nghị chốt:** bổ sung một quy ước đo được, ví dụ *"ở độ phân giải tối thiểu đã quy định, không thành phần
nào bị cắt mất nội dung hoặc chồng lên thành phần khác"*. Nghiệp vụ cho biết độ phân giải chuẩn để chấm.

---

### Câu 3 — 🔴 **Mâu thuẫn nặng nhất:** Hợp đồng ↔ Vụ việc là **nhiều-nhiều** hay **một-nhiều**? ⟨1 điểm: `_22`⟩

Đặc tả nói **hai đằng**, mỗi bên 4 chỗ:

| Khai **nhiều-nhiều** (một hợp đồng gắn nhiều vụ việc) | Khai **một-nhiều** (mỗi vụ việc chỉ một hợp đồng) |
|---|---|
| `srs-fr-14-hop-dong-tv.md:90` `:123` `:161` `:291` | `srs-fr-14-hop-dong-tv.md:352` `:373` `:424` · `srs-v3.5.md:4406` |

**Vì sao câu này quan trọng hơn các câu khác:** nó không chỉ là câu chữ — nó quyết định **cấu trúc dữ liệu**.
Chốt sai chiều thì phải sửa cả phần lưu trữ, không chỉ sửa màn hình. Nó cũng chi phối cách xử lý của
phiếu `_18` (xóa hợp đồng đang có vụ việc) và `_23` (bỏ liên kết).

**Đề nghị chốt — chọn một:**
- ☐ **(a)** Nhiều-nhiều ⇒ sửa 4 dòng khai một-nhiều.
- ☐ **(b)** Một-nhiều ⇒ sửa 4 dòng khai nhiều-nhiều.

*(Đội kiểm thử sẽ đo phần mềm đang làm theo chiều nào và bổ sung vào câu này trước khi gửi — xem Phần III.)*

---

### Câu 4 — **Thời điểm** ô "Mã hợp đồng" được điền ⟨1 điểm: `_13`⟩ — ✅ đã đo

Đặc tả nói hai đằng: `:290` khai *"Mã (auto)"* như một **trường có sẵn trên biểu mẫu**; `:119` lại xếp việc
sinh mã vào **bước xử lý khi bấm lưu**. Không dòng nào nói mã phải hiện ngay lúc mở biểu mẫu.

**Phần mềm hiện tại: đúng như phiếu mong đợi.** Vừa mở biểu mẫu là ô Mã hợp đồng đã có sẵn
`HDTV-20260807-0006`, đúng khuôn. Bộ phận phát triển còn dựng riêng một điểm xem trước mã.

**Đề nghị chốt:** bổ sung vào đặc tả rằng mã hiện ngay khi mở biểu mẫu.
**Đây là câu hỏi hoàn thiện tài liệu, KHÔNG chặn bàn giao** — phần mềm đang làm đúng.

---

## Phần II — 7 câu **chờ đo xong** mới gửi

Các câu này cần biết **phần mềm hiện đang làm gì** thì nghiệp vụ mới quyết được — vì nếu phần mềm đã làm
đúng ý nghiệp vụ thì chỉ cần **bổ sung tài liệu** (rẻ), còn nếu làm khác thì mới là chuyện **sửa phần mềm** (đắt).

> Cột **"Phần mềm hiện tại"** sẽ được điền khi phiếu tương ứng được đo. Trạng thái hiện tại ghi ở Phần III.

---

### Câu 5 — Lưu xong thì màn hình đi đâu? ⟨3 điểm: `_15` · `_21` · `_17`⟩ — đã đo 1/3

**Phiếu mong đợi:** lưu xong → **quay về màn danh sách hợp đồng**. (`_17` cũng mong *"danh sách được làm mới"* sau khi xóa.)

**Đặc tả quy định ngược:** nhóm chức năng này **không có màn danh sách hợp đồng độc lập** — quyết định
nghiệp vụ ngày 11/05/2026, ghi tại `srs-fr-14-hop-dong-tv.md:266` và `:268`. Lưu xong thì **đóng biểu mẫu và
trả người dùng về nơi đã mở nó** (`:175`, có ghi chú *"BA chốt 06/08/2026"*, và `:187`).

**Phần mềm hiện tại (đo ở phiếu `_15`): làm theo phía đặc tả.** Đóng biểu mẫu, ở lại màn Chi tiết vụ việc và
tự nạp lại bảng "HĐ tư vấn liên kết" ngay trong màn đó; bảng đã hiện hợp đồng vừa tạo.

**Đề nghị chốt — chọn một:**
- ☐ **(a)** Giữ như hiện nay ⇒ đội kiểm thử **sửa lại câu chữ của 3 phiếu** cho khớp. *(không cần sửa phần mềm)*
- ☐ **(b)** Vẫn phải có màn danh sách riêng ⇒ **cần dựng thêm màn đó**, và cần xem lại quyết định ngày 11/05/2026.

---

### Câu 6 — Bảng thành phần `:285`–`:289` áp cho **màn nào**? ⟨liên quan `_02`⟩ — ✅ đã đo

Đặc tả mô tả một **màn danh sách hợp đồng độc lập** gồm 5 vùng: đường dẫn phụ đề riêng (`:285`), tiêu đề trang
kèm 3 nút (`:286`), thanh lọc (`:287`), bảng 10 cột (`:288`), phân trang (`:289`). **Nhưng chính đặc tả tại
`:266`/`:268` đã bỏ màn độc lập đó.**

⇒ Một mục nằm bên trong màn khác thì **về mặt kiến trúc không thể** có đường dẫn phụ đề riêng, tiêu đề trang
riêng, hay phân trang riêng của nó. **Ba vùng đó thiếu là hệ quả của chính quyết định bỏ màn, không phải bộ
phận phát triển làm thiếu.**

**Phần mềm hiện tại:** thanh lọc **khớp từng ý** với `:287`; bảng có **đủ 10 cột**, thừa thêm cột Trạng thái
(đặc tả liệt kê thành phần bắt buộc chứ không cấm thêm ⇒ không tính lỗi); phân trang có, mặc định 20 mục/trang;
có nút thêm hợp đồng và nút Xuất Excel; **không có** nút Làm mới, thay bằng nút Xóa bộ lọc.

**Đề nghị chốt:** xác nhận bảng `:285`–`:289` **chỉ áp cho phần hợp đồng nhúng trong màn Chi tiết vụ việc**,
và **bỏ 3 vùng không áp dụng được**. Nếu nghiệp vụ vẫn muốn đủ 5 vùng thì quay lại Câu 5 phương án (b).

---

### Câu 7 — Thiếu câu thông báo cho hai hành động ⟨2 điểm: `_17` · `_23`⟩

| Hành động | Đặc tả có gì | Thiếu gì |
|---|---|---|
| **Xóa hợp đồng thành công** | bảng mã thông báo có mã cho *xóa thất bại* và *lưu thành công* (`:166`–`:173`) | **không có** mã cho *xóa thành công* |
| **Bỏ liên kết vụ việc** | `:291` chỉ khai có nút `[Bỏ liên kết]` | **không khai** có hộp xác nhận hay không, và câu chữ ra sao |

*(Mẫu câu ở `srs-fr-05-vu-viec.md:1595` là câu **xóa vụ việc** — không được mượn sang, khác hành động.)*

**Đề nghị chốt:** bổ sung hai câu này vào bảng mã thông báo, và nói rõ **bỏ liên kết có cần hộp xác nhận không**
(đây là thao tác gỡ quan hệ, không xóa dữ liệu — nghiệp vụ quyết mức độ cảnh báo).

---

### Câu 8 — Tệp Excel xuất ra: **cột nào** và **tên tệp ra sao** ⟨2 điểm: `_16`⟩

**8a — Cấu trúc cột.** Chính đặc tả ghi *"**cần chủ đầu tư xác nhận template**"* và gắn cờ chưa chốt cho cả
khối (`:127`, `:134`). ⇒ Chưa có chuẩn để chấm. **Đề nghị cấp mẫu tệp Excel chuẩn.**

**8b — Tên tệp.** Đây là chỗ **đặc tả nói ngược phiếu**:

| | Nội dung |
|---|---|
| Phiếu mong đợi | `HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx` |
| Đặc tả **bắt buộc** (`srs-v3.5.md:6760`, Phụ lục E §H8) | khuôn `{TênTệp}[_{ĐịnhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`, viết hoa đầu từ, **bỏ mọi ký tự không phải chữ và số, kể cả dấu gạch nối** |

⇒ Tên trong phiếu **vi phạm khuôn chung** (có dấu gạch nối, không viết hoa đầu từ).

**Đề nghị chốt — chọn một:**
- ☐ **(a)** Theo khuôn chung `:6760` ⇒ đội kiểm thử sửa câu chữ của phiếu. *(khả năng cao phần mềm đã đúng)*
- ☐ **(b)** Cho chức năng này một ngoại lệ ⇒ ghi ngoại lệ đó vào đặc tả.

---

### Câu 9 — Lưu bản sửa: **thay toàn bộ** hay **gộp thêm** các danh sách con? ⟨1 điểm: `_21`⟩

Hợp đồng có 4 danh sách con (vụ việc liên kết · mốc tiến độ · giai đoạn thanh toán · tệp đính kèm).
Khi bấm lưu bản sửa, đặc tả **không nói rõ**: `:122` chỉ nói *"cập nhật"*, `:123` nói *"tạo"*, còn tệp đính kèm
**không xuất hiện** trong bảng xử lý (`:118`–`:125`, `:159`–`:162`).

**Vì sao phải hỏi:** hai cách hiểu cho ra kết quả **ngược nhau** — "thay toàn bộ" nghĩa là dòng nào không gửi
lên sẽ **bị xóa mất**; "gộp thêm" nghĩa là dòng cũ được giữ. Đây là rủi ro **mất dữ liệu người dùng**.

**Đề nghị chốt:** nói rõ với từng danh sách con, lưu bản sửa là thay toàn bộ hay gộp thêm.

---

### Câu 10 — Tìm kiếm **bên trong cửa sổ chọn vụ việc** theo tiêu chí gì? ⟨1 điểm: `_22`⟩

Phiếu mong đợi cửa sổ chọn vụ việc có tìm kiếm. Đặc tả `:291` chỉ khai *"cửa sổ chọn nhiều"* và các **cột của
bảng kết quả**, **không khai** ô tìm kiếm nào, tìm theo trường gì.

**Đề nghị chốt:** liệt kê tiêu chí tìm kiếm bắt buộc có trong cửa sổ này (ví dụ mã vụ việc, tên doanh nghiệp).

---

### Câu 11 — Hai điểm ở phần **thanh toán giai đoạn** ⟨2 điểm: `_26` · `_27`⟩

**11a — Thanh tiến trình.** Phiếu mong đợi: nhập Số tiền → **tự cộng dồn** vào thanh tiến trình.
Đặc tả quy định ngược: thanh tiến trình = **tổng các dòng ĐÃ THANH TOÁN** / giá trị hợp đồng (`:301`), và dòng
mới tạo mặc định là **chưa thanh toán** (`:112`). ⇒ Theo đặc tả, thêm dòng mới thì thanh tiến trình **đứng yên**
là **đúng**, phải đánh dấu đã trả nó mới nhích.
**Đề nghị chốt:** ☐ (a) theo đặc tả, sửa câu chữ phiếu · ☐ (b) đổi cách tính thành "tổng đã cam kết".

**11b — Nút xóa dòng.** Bảng Thanh toán giai đoạn `:293` **không khai nút nào**, trong khi bảng vụ việc `:291`
có khai `[Bỏ liên kết]` và bảng mốc tiến độ `:292` có khai `[+ Thêm mốc]`. Phần xử lý cũng không có bước xóa
giai đoạn thanh toán.
**Đề nghị chốt:** có cho xóa dòng giai đoạn thanh toán không? Nếu có, bổ sung vào bảng thành phần và phần xử lý.

---

## Phần III — Tình trạng đo (cập nhật khi có kết quả)

| Câu | Điểm liên quan | Cần kết quả đo? | Tình trạng |
|---|---|---|---|
| 1 | `_02` C2 · `_08` C2 · `_09` C2 | không | ✅ **gửi được ngay** |
| 2 | `_02` C4 · `_08` C4 · `_09` C4 | không | ✅ **gửi được ngay** |
| 3 | `_22` C5 | nên có, không bắt buộc | ✅ **gửi được ngay** (bổ sung sau khi đo `_22`) |
| 4 | `_13` C2 | có | ✅ **đã đo — gửi được ngay** |
| 5 | `_15` C5 · `_21` C5 · `_17` C4 | có | ⏳ đã đo 1/3 (`_15`), chờ `_21` `_17` |
| 6 | `_02` C2 | có | ✅ **đã đo — gửi được ngay** |
| 7 | `_17` C3 · `_23` C1 | có | ⏳ chờ đo `_17` `_23` |
| 8 | `_16` C2 · `_16` C4 | có | ⏳ chờ đo `_16` |
| 9 | `_21` C3 | có | ⏳ chờ đo `_21` |
| 10 | `_22` C2 | có | ⏳ chờ đo `_22` |
| 11 | `_26` C2 · `_27` C1 | có | ⏳ chờ đo `_26` `_27` |

**Gửi được ngay: 5 câu** (1, 2, 3, 4, 6) — phủ **8/19 điểm**.
**Chờ đo: 6 câu** (5, 7, 8, 9, 10, 11) — phủ **11/19 điểm**.

---

## Ghi chú về phạm vi

Bộ câu hỏi này **chỉ thuộc cụm Hợp đồng Tư vấn**. Các cụm khác trong đợt rà (`KTDGKQHT` · `TPDBCKQTHCT` ·
`THBCTHCT`) có câu hỏi nghiệp vụ riêng, đã ghi trong ô *Kết quả verify* của từng dòng trên bảng theo dõi.
