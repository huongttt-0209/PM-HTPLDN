# Phiếu chốt BA — 7 điểm treo tuần 5 (LKHDG · QLNDTVVCG · BC thống kê vụ việc)

**Ngày:** 06/08/2026 · Gom từ 4 phiếu hỏi: `ba-confirmation-needed-LKHDG`, `ba-confirmation-needed-QLNDTVVCG`, `cau-hoi-BA` (nhóm B2), `phan-hoi-ba-QLNDTVVCG-OOS-02-04`.

## Thay đổi kể từ lượt duyệt gần nhất

Lượt đầu của phiếu này. Bảng dưới ghi **kết luận có khác đề xuất của bên hỏi hay không**, để người duyệt biết chỗ nào phải đọc kỹ.

| Mục | Bên hỏi đề xuất gì | Kết luận phiếu này | Mức đọc |
|---|---|---|---|
| 1. Hai ô nhập của form kế hoạch đánh giá | QA để mở 2 hướng | ✅ Không hướng nào — bảng vẫn ĐÓNG, nhưng **thiếu 2 dòng**; và bản bàn giao mới vừa gỡ mất chúng | (a) đọc kỹ |
| 2. Kênh gửi thông báo tư vấn chuyên sâu | QA chấm Pass, ngả về "chỉ trong ứng dụng" | ✅ **BA chốt 06/08: trong ứng dụng + thư điện tử** → `QLNDTVVCG_24` đảo Pass thành còn lỗi | (a) đọc kỹ |
| 3. Điều hướng sau khi chuyên gia từ chối | QA ngả về giữ nguyên màn chi tiết | ✅ **BA chốt 06/08: quay về danh sách** — đối tác ghi đúng | (a) đọc kỹ |
| 4. Giao việc cho ai | QA ngả về "chỉ Chuyên gia" | ✅ **BA chốt 06/08: chỉ Chuyên gia** — phần mềm đúng, chỉ dọn đặc tả | (a) đọc kỹ |
| 5. Quản trị hệ thống xuất tệp báo cáo | QA để mở 2 hướng, giữ quyền xem | ✅ **Không được xuất, và cũng không vào màn báo cáo** | (a) đọc kỹ |
| 6. Nhật ký không hiện lý do từ chối | Dev đề xuất cách B | ✅ **BA chốt 06/08: hiện lý do có kiểm soát** — cải tiến, không phải bug | (b) đọc phần phương án |
| 7. Chuyên gia sửa/tạo nội dung tư vấn | Dev để mở "giữ nguyên / siết hết" | ✅ **Siết theo phạm vi**, không siết phẳng | (a) đọc kỹ |

**Tình trạng: cả 7 mục ĐÃ CHỐT — 3 mục tự khép theo cây trọng tài (1 · 5 · 7), 4 mục BA duyệt ngày 06/08/2026 (2 · 3 · 4 · 6).** Không còn điểm treo nào chờ quyết; phần còn lại là thi hành.

### Lịch sử đảo kết luận — đọc trước khi duyệt

Phiếu này đã qua một vòng soi độc lập hỏi mù (bốn lượt tra song song, không lượt nào được đọc kết luận của người soạn). Vòng đó **lật hai kết luận** vốn được ghi là tự chốt:

| Mục | Ban đầu chốt gì | Vì sao đảo |
|---|---|---|
| 2. Kênh thông báo | Tự chốt "phải có thư điện tử", coi danh sách phạm vi của quy tắc chung là lỗi thời | Quy tắc chung **liệt kê đích danh** các nhóm áp dụng và **không có nhóm này**; bản trích trong tệp module lại là **một quy tắc khác hẳn** trùng mã số. Sáu bước gửi thông báo của chức năng đang trỏ tới một mã mà **không bản định nghĩa nào nhận**. Không thể tự khép bằng cách tuyên bố danh sách kia lỗi thời → **BA đã chốt 06/08**, và việc sửa danh sách phạm vi nay là một phần của phương án |
| 4. Giao việc cho ai | Tự chốt "cả Chuyên gia lẫn Tư vấn viên", dựa trên 13 lần đặc tả viết "CG/TVV" | Đếm lại theo từng mục thì tỉ lệ là **14 lần "CG/TVV" so với 107 lần chỉ "CG"**, và mục Màn hình có **0 lần** "CG/TVV". Ngay trong cùng mục Máy trạng thái, sơ đồ viết "CG/TVV" còn bảng viết "CG". Bản bàn giao mới nhất đã **chủ động sửa** ô chọn thành "chỉ liệt kê chuyên gia đang hoạt động" |

Mục 3 cũng từng được chốt rồi hạ xuống ở lượt trước, khi phát hiện bản bàn giao mới đã gỡ mất khuôn mà tôi viện. Vòng soi độc lập xác nhận lại: *"đây là khoảng trống thật, không phải chỗ tôi đọc sót"*.

Ba mục còn lại (1 · 5 · 7) được vòng soi **xác nhận và củng cố thêm** — chi tiết ghi trong từng mục.

## Bối cảnh chung

Đợt đo lại tuần 5 trên bản dựng V1.0.8, môi trường `18.143.165.120.nip.io`. Đối tác quay bằng chứng trên môi trường nghiệm thu bản V1.0–V1.0.3 nên số liệu tuyệt đối khác nhau; mọi kết luận dưới đây đo trên chính lượt này.

**Bản bàn giao đối chiếu: `HTPLDN-PTYC-CT-v3.5.docx`** (tệp ngày 01/08/2026) — bản mới nhất và là **mốc đối chiếu duy nhất** của phiếu này `[BA chốt 2026-08-06]`. Các bản trước không dùng làm căn cứ.

Chưa ghi nhận được ngày bàn giao và kênh gửi của bản này.

---

# 1. Form lập / sửa kế hoạch đánh giá thiếu hai ô nhập trong đặc tả

**Vấn đề:** Khi cán bộ bấm Sửa một đợt đánh giá, màn hình đang hiện thêm ô chọn cơ quan được đánh giá và khu vực tài liệu đính kèm. Bảng mô tả form trong đặc tả gốc chỉ liệt kê 7 thành phần, không có hai mục này — nên đối tác từng chấm Fail khi chúng chưa xuất hiện, còn đợt dọn dẹp sau lại có nguy cơ gỡ đi.

**Bảng bóc ý con — Kết quả mong đợi `LKHDG_16`**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Chỉ hiện nút Sửa khi đợt ở Lập kế hoạch hoặc Phân công | Có (`srs-fr-08-danh-gia.md:837`) | Không thuộc phiếu này — đã log `BUG-LKHDG-SUA-PHANCONG` |
| Cán bộ phải thuộc đơn vị sở hữu đợt | Có (BR-AUTH-08) | Không tranh chấp |
| Hiện danh sách tệp đính kèm của đợt | Bảng form không có; bảng dữ liệu **có** | Mục này |

**(1) Phần mềm đúng bản gốc chưa?** ĐÚNG, và bản gốc mới là chỗ thiếu. Bảng dữ liệu của thực thể khai đủ hai trường, trong đó `co_quan_duoc_danh_gia_id` là **bắt buộc**:

- `_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md:1043` — *"`file_dinh_kem` | file[] | N | PDF/DOC/DOCX/XLS/XLSX, max 20MB/file | — | File đính kèm kế hoạch đánh giá `[CR-07]`"*
- `srs-fr-08-danh-gia.md:1044` — *"`co_quan_duoc_danh_gia_id` | identifier | **Y** | FK → DON_VI(id) | — | Cơ quan được đánh giá (1:1, Q-07)"*
- `srs-fr-08-danh-gia.md:859` — ở Tab Tiêu chí trường này chỉ **read-only**: *"Mã đợt, Tên đợt, Tần suất, Kỳ đánh giá, Đối tượng, Cơ quan được đánh giá (read-only)"*

Đã quét toàn tệp `srs-fr-08`: ngoài dòng read-only trên, **không có ô nhập nào** cho hai trường này. Một trường bắt buộc mà không màn hình nào cho nhập thì không tạo nổi bản ghi — bảng form ở `:843-851` là bảng **chưa cập nhật**, không phải bảng đóng.

**Thiếu ở hai chỗ chứ không phải một.** Bảng dữ liệu đầu vào của chính chức năng (`srs-fr-08-danh-gia.md:105-113`) cũng chỉ có **7 trường**, cũng không có hai trường này. Nên chỗ phải vá là **cả §Inputs lẫn §Màn hình**.

**Nhật ký sửa đổi chứng minh đây là lượt áp thay đổi làm dở, không phải quên một dòng.** `CHANGELOG-v3-to-v3.5.md` liệt kê **vị trí đã sửa** của hai yêu cầu thay đổi, và cả hai đều chỉ đụng đúng mục Thực thể:
- CR-07 (`:988-989`) — *"**Vị trí đã sửa:** - §4 Bảng entity KE_HOACH_DANH_GIA — thêm field 15 `file_dinh_kem` file[]"*
- CR-10 / Q-07 (`:965-968`) — *"**Vị trí đã sửa:** - §4 Mermaid ERD … - §4 Bảng entity KE_HOACH_DANH_GIA — thêm field 16"*

**Và tệp nền còn chưa được áp gì cả.** Bảng thực thể `KE_HOACH_DANH_GIA` ở `srs-v3.5.md:2904-2926` **thiếu cả hai trường**, còn giữ bộ trạng thái cũ 6 giá trị (tệp nhóm đã 8), khai `muc_tieu` là không bắt buộc (tệp nhóm ghi bắt buộc), và thừa một trường `ct_htpl_id` mà tệp nhóm không có. Sơ đồ quan hệ tổng `:3911-3916` cũng chỉ 4 trường. ⇒ Việc sửa phải đồng bộ **tệp nền + tệp nhóm**, không chỉ tệp nhóm.

**Một mâu thuẫn khác lộ ra khi rà, nên xử luôn cùng lượt:** ba trường `tan_suat` / `thoi_gian_bat_dau` / `thoi_gian_ket_thuc` khai **không bắt buộc** ở bảng thực thể (`:1033-1035`) nhưng **bắt buộc** ở cả §Inputs (`:109-111`) lẫn form màn hình (`:847-848`); riêng `tan_suat` ở thực thể có **3** giá trị (thêm `DOT_XUAT`) còn chức năng và màn hình chỉ **2**.

**(1b) Bản bàn giao nói gì? — CŨNG THIẾU cả hai mục, y như bản gốc.**

Bảng trường thông tin của biểu mẫu (mục 4.8.1.2.2) có 9 dòng: Mã đợt · Tên đợt · Mục tiêu · Tần suất · Từ ngày · Đến ngày · Đối tượng · Ghi chú · Trạng thái đợt. Mô tả thao tác thêm mới cũng chỉ liệt kê 5 nhóm: *"Người sử dụng bấm 'Thêm mới', nhập tên đợt, mục tiêu, tần suất, khoảng thời gian, đối tượng đánh giá rồi lưu"*. **Không có dòng nào cho Cơ quan được đánh giá, cũng không có Tệp đính kèm.**

⚠️ **Đây là chỗ nguy hiểm nhất của phiếu này: cả bản gốc lẫn bản bàn giao đều không có ô nhập cho một trường BẮT BUỘC.** Không phải một bên sai một bên đúng — cả hai cùng thiếu. Nếu không sửa trước đợt kiểm thử sau, đối tác chấm theo v3.5 sẽ báo phần mềm **thừa** hai ô, tức ngược hẳn với lần trước.

*(Bản mềm hiện đang hiển thị hai ô đó, tức đúng theo bảng dữ liệu và đúng nhu cầu nghiệp vụ — nhưng vượt cả hai tài liệu. Cách xử là bổ sung vào tài liệu, không phải gỡ khỏi phần mềm; lý do ở (3).)*

**(2) Đối tác yêu cầu khác bản gốc chỗ nào?** Không khác. Kỳ vọng của đối tác trùng bảng dữ liệu và trùng bản bàn giao.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ. Không có ô chọn cơ quan được đánh giá thì không tạo được đợt; và chính trường này là điều kiện của chức năng Nhận kết quả đánh giá (`srs-fr-08-danh-gia.md:773` — *"Tác nhân: CB NV (thuộc `co_quan_duoc_danh_gia_id`)"*).

**→ Kết luận: bảng thành phần form vẫn là danh sách ĐÓNG — nhưng đang thiếu 2 dòng, phải bổ sung vào bản gốc. Phần mềm ĐÚNG, không gỡ gì. Dev action: Không · Sửa đặc tả: Có · Sheet: giữ nguyên trạng thái đang xử lý (LKHDG_16 vẫn Reopen vì lỗi độc lập `BUG-LKHDG-SUA-PHANCONG`).** ✅ Tự chốt theo cây trọng tài — tầng "mô hình dữ liệu đè đặc tả form".

### Phương án xử lý (cập nhật SRS)

Bổ sung 2 dòng vào bảng `srs-fr-08-danh-gia.md:843-851`, đặt trước dòng thanh hành động:

| Vị trí | Thành phần | Nội dung đặc tả |
|---|---|---|
| chèn sau `#25` Đối tượng | Cơ quan được đánh giá | Danh sách chọn từ danh mục Đơn vị, **bắt buộc**, chọn 1 đơn vị; được phép khác đơn vị của người tạo (đơn vị thực hiện đánh giá) |
| chèn sau `#26` Ghi chú | Tài liệu đính kèm | Tải lên nhiều tệp PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB mỗi tệp, không bắt buộc; hiện danh sách tệp đã có kèm thao tác Xem / Xóa |

Rà kèm 3 chỗ:

(a) **§Inputs của FR-VI-01 phải liệt kê đủ 2 trường** — bảng đó (`srs-fr-08-danh-gia.md:105-113`) cũng chỉ có 7 trường như bảng màn hình.

(b) **Số tệp tối đa: áp khuôn đã dùng nhất quán trong chính bản gốc**, không đẻ quy ước mới — *"Tối đa 10 file/upload, tổng max 100MB, mỗi file max 20MB"* (`srs-fr-02-hoi-dap.md:108`, `srs-fr-05-vu-viec.md:185 · :325 · :483 · :1280`).

(c) Nhãn số đếm nếu có chỗ ghi "form 7 thành phần" — **đã quét, không có chuỗi đó**, nên không phải sửa.

> **Không cần thêm mã lỗi cho ô Cơ quan được đánh giá.** Bảng lỗi của chức năng đã có dòng phủ chung: `srs-fr-08-danh-gia.md:151` — *"| E1 | Thiếu trường bắt buộc | `ERR-DG-KH-01` | \"Vui lòng nhập đầy đủ thông tin bắt buộc\" |"*. Trường mới là trường bắt buộc nên tự rơi vào mã này. *(Lượt soạn trước ghi đây là việc phải làm — sai, chưa chứng minh ngược.)*

**Doc action — hai chiều, đừng chỉ làm một chiều:** bản `.docx` v3.5 phải **bổ sung** hai dòng này, và bản gốc cũng vậy. Đây là ca hiếm mà cả hai tài liệu cùng thiếu một chỗ, nên nếu chỉ sửa một bên thì bên còn lại thành căn cứ để mở lại phiếu.

⚠️ **Một câu chữ dễ bị hiểu ngược, phải làm rõ khi sửa.** `srs-fr-08-danh-gia.md:1044` ghi *"**Khác** `don_vi_id` (= cơ quan thực hiện ĐG)"*. Đây là **ghi chú phân biệt hai trường**, không phải ràng buộc "hai giá trị bắt buộc phải khác nhau" — ba căn cứ: (a) cụm đó nằm ở cột **Mô tả**, còn cột **Ràng buộc nghiệp vụ** của chính dòng chỉ có `FK → DON_VI(id)`; (b) không bước xử lý nào, không mã lỗi nào, không quy tắc nào so sánh hai đơn vị; (c) nhật ký sửa đổi ghi mục đích là **phân biệt hai vai trò** — *"cơ quan thực hiện đánh giá … và cơ quan được đánh giá … v3 chỉ có một ô nên cán bộ không phân biệt được hai vai trò"*.

Để nguyên chữ "Khác" thì đơn vị phát triển dễ cài kiểm tra chặn. **Sửa `:1044` thành *"được phép trùng hoặc khác `don_vi_id`"*.** ✅ **BA duyệt 06/08/2026 — cho phép một cơ quan tự đánh giá chính mình.**

Ba căn cứ:

1. **Mục đích của trường là phân biệt hai vai, không phải cấm trùng.** Nhật ký sửa đổi ghi lý do bổ sung: *"v3 chỉ có một ô để ghi đơn vị nên cán bộ nghiệp vụ **không phân biệt được hai vai trò, dễ chấm điểm sai đối tượng** và không thể gửi kết quả"*.
2. **Không có quy tắc phân cấp nào nói ai đánh giá ai.** Đã quét biến thể *TW đánh giá · đánh giá cấp dưới · đánh giá trực thuộc · Bộ TP đánh giá* trên toàn bộ tệp đặc tả — không dòng nào. Danh mục Đơn vị lại cho mọi vai trò đọc toàn bộ (`srs-v3.5.md:1333`, tất cả cột `R`).
3. **Chặn trùng sẽ vô hiệu hoá chức năng ở cấp Bộ ngành và Địa phương.** Quy tắc phạm vi dữ liệu ghi *"BN chỉ nhìn thấy dữ liệu đơn vị BN của mình; ĐP chỉ nhìn thấy dữ liệu đơn vị ĐP của mình; **Ngang cấp KHÔNG thấy nhau**"* (`srs-v3.5.md:1369-1372`). Một Sở Tư pháp đánh giá hoạt động hỗ trợ pháp lý của chính mình là tình huống bình thường, và cũng là tình huống duy nhất họ làm được — chặn trùng thì chỉ Trung ương tạo được đợt đánh giá.

> **Hệ quả nhỏ, ghi để lượt sau khỏi báo là lỗi:** khi hai đơn vị trùng nhau thì FR-VI-10 *Nhận kết quả đánh giá* thành **thừa** — cán bộ tạo đợt cũng là người nhận kết quả, mà họ đã xem được với quyền đầy đủ. Không hỏng gì. Chức năng đó sinh ra cho ca hai đơn vị khác nhau, khi *"hoàn toàn không có cách nào để cán bộ tại cơ quan được đánh giá xem lại kết quả của đơn vị mình"*.

> **Phản hồi gửi đối tác** (điền cột "DEV phản hồi lần 1" tại dòng `LKHDG_16`):
>
> *"Xác nhận bản SRS docx đang thiếu thành phần. Sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần."*

---

# 2. Sự kiện tư vấn chuyên sâu chỉ báo trong phần mềm, không gửi thư điện tử

**Vấn đề:** Khi chuyên gia bấm chấp nhận hoặc từ chối một yêu cầu tư vấn, doanh nghiệp và cán bộ phụ trách chỉ nhận được thông báo hiển thị trong phần mềm, không có thư điện tử. Riêng ở mảng tư vấn chuyên sâu, doanh nghiệp chưa có chỗ đăng nhập để đọc thông báo đó — nên nếu không gửi thư thì họ không biết yêu cầu của mình đã được nhận hay bị trả lại.

**(1) Phần mềm đúng bản gốc chưa?** **KHÔNG kết luận được.** Hai bước xử lý không ghi kênh mà viện dẫn quy tắc thông báo; quy tắc đó có chốt kênh, nhưng lại không tuyên bố áp cho nhóm này (xem phần dưới):

- `srs-fr-12-tv-chuyen-sau.md:186` — *"Gửi thông báo DN + CB NV: CG đã xác nhận | BR-NOTIF-01"*
- `srs-fr-12-tv-chuyen-sau.md:197` — *"Gửi thông báo CB NV: CG từ chối, cần phân công lại | BR-NOTIF-01"*
- `srs-v3.5.md:5613` — *"hệ thống PHẢI gửi thông báo in-app + email cho các đối tượng tương ứng … **Kênh:** in-app + email; SMS chỉ với case khẩn"*

**Đã đếm, không phát biểu cảm tính.** Trong các bảng bước xử lý của toàn bộ 17 tệp đặc tả có **64** bước "Gửi thông báo"; chỉ **12** bước viết kênh ra chữ — **19%**. Nghĩa là **không ghi kênh mới là khuôn chung**, ghi kênh mới là ngoại lệ. Riêng FR-X.1-01 có **8** bước gửi thông báo (`:174 · :186 · :197 · :208 · :219 · :220 · :231 · :243`) và chỉ **2** bước ghi kênh — `:174` (in-app + email) và `:219` (qua Cổng PLQG hoặc email, là kênh riêng của luồng trả kết quả). ⇒ **Đọc chỗ thiếu ở `:186`/`:197` thành "cố ý chỉ trong ứng dụng" là suy ngược khuôn** — im lặng ở đây là thói quen viết, không phải quyết định.

*(Con số này đã sửa: lượt soạn đầu ghi "4/56" vì chỉ dò đúng một cách viết `in-app + email`, bỏ sót các cách viết khác như `trong hệ thống + email`, `qua email đã khai`.)*

**Nhưng chỗ đáng lẽ lấp khoảng im lặng đó lại không nhận nhóm này — đây là lý do mục này không tự khép được.**

Mã `BR-NOTIF-01` hiện trỏ tới **hai quy tắc khác hẳn nhau**:

- `srs-v3.5.md:5613` — quy tắc **sự kiện workflow**: *"Khi entity workflow chuyển trạng thái có ý nghĩa với bên liên quan, hệ thống PHẢI gửi thông báo in-app + email … **Kênh:** in-app + email"*. Cột Áp dụng liệt kê: *"FR-II-08, FR-III-01/13/14/15/17/18, FR-IV-06/07, FR-V.I, FR-V.II, FR-VI, FR-XI"* — **không có FR-X.1**.
- `srs-fr-12-tv-chuyen-sau.md:1626` — quy tắc **dữ liệu từ Cổng**: *"Hệ thống tự động gửi thông báo in-app + email **khi có dữ liệu mới từ API inbound (Cổng PLQG)**"*, phạm vi FR-X.1-03, FR-X.1-05.

Hai phát biểu này không phải một quy tắc. Bản trong tệp module đúng phạm vi của nó (FR-X.1-03/05 chính là hai chức năng nhận dữ liệu từ Cổng), và bảng ánh xạ `:1555` cũng nhất quán với nó. Vấn đề là **FR-X.1-01 viện mã này ở 6 bước** (`:174 · :186 · :197 · :219 · :231 · :243`) và liệt kê ở danh sách quy tắc áp dụng `:287` — nhưng không bản nào tuyên bố phủ nó.

⇒ Không thể tự khép bằng cách coi danh sách phạm vi ở `:5613` là lỗi thời. Phải để BA chốt kênh, rồi mới sửa đặc tả cho khớp.

**Một mâu thuẫn nhỏ hơn, sửa kèm:** bảng chuyển trạng thái `srs-fr-12-tv-chuyen-sau.md:1521` cho bước chuyên gia từ chối **không nhắc gửi thông báo** và để trống cột quy tắc, trong khi bảng bước xử lý `:197` thì có. Hai bảng cùng tệp chọi nhau.

**(1b) Bản bàn giao nói gì? — LẶP LẠI ĐÚNG khoảng im lặng của bản gốc.**

Bản `.docx` v3.5 ghi kênh ở hai bước đầu, rồi bỏ trống ở đúng hai bước đang xét:

| Bước | Bản `.docx` v3.5 ghi gì | Có kênh? |
|---|---|---|
| Tiếp nhận yêu cầu | *"Cán bộ nghiệp vụ phụ trách đơn vị nhận thông báo **trong hệ thống và qua thư điện tử**"* | **Có** |
| Phân công chuyên gia | *"hệ thống gửi thông báo **trong hệ thống và qua thư điện tử** tới chuyên gia được chọn kèm thời hạn 2 ngày làm việc"* | **Có** |
| **Chuyên gia xác nhận** | *"+ Gửi thông báo cho doanh nghiệp và CB NV."* | **Không** |
| **Chuyên gia từ chối** | *"gửi thông báo cho CB NV để phân công lại và lưu vết thao tác kèm lý do từ chối"* | **Không** |

⇒ **Không phải tranh chấp tài liệu.** Bản bàn giao lặp lại y hệt kiểu viết của bản gốc: nêu kênh ở hai bước đầu rồi im ở hai bước sau. Đối tác đọc v3.5 cũng không suy ra được kênh cho hai mốc này, nên kỳ vọng *"Doanh nghiệp và CBNV không nhận được thông báo"* của họ không đối chiếu được với văn bản.

Điều này khép một khả năng: đây **không** phải ca "phần mềm đúng bản gốc nhưng bản bàn giao đòi thêm". Cả hai tài liệu cùng thiếu một chỗ — nên phải bổ sung vào cả hai, và chốt kênh là việc của BA chứ không phải việc dọn tài liệu.

**(2) Đối tác yêu cầu khác bản gốc không?** Không khác. Kết quả mong đợi *"Gửi thông báo cho doanh nghiệp và cán bộ nghiệp vụ phụ trách"* đúng với `:186`.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ với doanh nghiệp — đây là lý do tôi nghiêng về hướng có thư điện tử. Doanh nghiệp có màn hình riêng trong phần mềm ở nhóm Vụ việc, nhưng **nhóm tư vấn chuyên sâu thì bản gốc ghi rõ là không có cổng cho doanh nghiệp** (`srs-fr-12-tv-chuyen-sau.md:244`), và họ phải tự đăng ký tài khoản mới theo dõi được (`:486`). Với cán bộ phụ trách thì mức bắt buộc thấp hơn nhưng vẫn thuộc cùng một quy tắc, không tách được.

**→ Kết luận: kênh chuẩn cho các mốc thông báo của nhóm Tư vấn chuyên sâu là TRONG ỨNG DỤNG + THƯ ĐIỆN TỬ. Hiện thiếu thư điện tử ⇒ là lỗi phần mềm. Dev action: Có · Sửa đặc tả: Có · Sheet: giữ xử lý.** ✅ **BA duyệt 06/08/2026.**

**Ba căn cứ của quyết định:**
1. **Riêng nhóm tư vấn chuyên sâu thì doanh nghiệp không có cửa vào để đọc thông báo trong ứng dụng.** Doanh nghiệp có màn hình riêng trong phần mềm — `SCR-V.I-04` (danh sách vụ việc của tôi), `SCR-V.I-05` (thông báo của tôi) — nhưng cả hai thuộc nhóm **Vụ việc**. Nhóm tư vấn chuyên sâu thì bản gốc nói thẳng là không có: `srs-fr-12-tv-chuyen-sau.md:244` — *"**TVCS không có cổng cho DN**"*; `:486` — *"**Khi DN muốn theo dõi nội dung tư vấn chuyên sâu → DN tự đăng ký TK**"*. Doanh nghiệp chưa tự đăng ký thì thông báo trong ứng dụng không tới được.
2. **Không nhất quán ngay trong cùng một luồng.** Bước phân công gửi cho **chuyên gia** — người *có* tài khoản — lại ghi rõ hai kênh (`:174`), còn bước xác nhận gửi cho **doanh nghiệp** — người *không có* tài khoản — thì bỏ trống. Người trong hệ thống được gửi thư, người ngoài hệ thống thì không: đó là ngược.
3. **Cả hai tài liệu cùng im lặng ở đúng hai bước này**, tức đây là khoảng sót của cách viết, không phải quyết định loại thư điện tử.

⚠️ **Hệ quả về verdict — Dev có việc phải làm:**
- `QLNDTVVCG_24` đảo từ **Pass** sang **còn lỗi**. Sheet: **giữ xử lý**, không Reject.
- Bước từ chối `:197` (ghi chú gộp ở `QLNDTVVCG_26`) đi theo cùng kết luận. Riêng verdict của `QLNDTVVCG_26` còn phụ thuộc mục 3.
- **Không cần phản hồi đối tác** — đây là bug thật, Dev sửa toàn bộ; đối tác ghi nhận đúng.

> **Ghi lịch sử (mục này đã đảo 2 lần):** lượt đầu tự chốt "phải có thư điện tử", coi danh sách phạm vi thiếu FR-X.1 là lỗi thời → vòng soi độc lập chỉ ra không bản định nghĩa nào nhận nhóm này nên hạ xuống chờ BA → BA chốt 06/08 theo hướng có thư điện tử, kèm yêu cầu sửa danh sách phạm vi cho khớp.

### Phương án xử lý (cập nhật SRS)

1. `srs-v3.5.md:5613` — cột "Áp dụng FR" bổ sung **FR-X.1** vào danh sách; đồng thời bổ sung nhóm sự kiện của luồng tư vấn chuyên sâu (phân công / chuyên gia xác nhận / chuyên gia từ chối / hoàn thành / phê duyệt / từ chối phê duyệt / hủy) vào danh sách sự kiện kích hoạt.
2. `srs-fr-12-tv-chuyen-sau.md:1626` — thay bản trích sai bằng đúng bản gốc; giữ câu về dữ liệu từ Cổng thành **một sự kiện** trong danh sách, không phải toàn bộ quy tắc.
3. `srs-fr-12-tv-chuyen-sau.md:1555` — sửa ánh xạ từ "FR-X.1-03, FR-X.1-05" thành **FR-X.1-01, FR-X.1-03, FR-X.1-05**.
4. **Hai bước không viện quy tắc nào — bổ sung phạm vi thôi không chạm tới chúng:**
   - `srs-fr-12-tv-chuyen-sau.md:208` — *"Auto chuyển → CHO_PHE_DUYET, gửi thông báo CB Phê duyệt cùng đơn vị | **BR-FLOW-01**"* (viện quy tắc khác)
   - `srs-fr-12-tv-chuyen-sau.md:220` — *"Gửi thông báo DN đánh giá chất lượng | **—**"* (bỏ trống)

   Danh sách 7 sự kiện ở mục 1 trên **không có** "thông báo DN đánh giá chất lượng". Phải bổ sung sự kiện này, nếu không `:220` vẫn là bước gửi thông báo không quy tắc, không kênh.
5. Rà chiều ngược: bản bàn giao cũng phải nêu đủ kênh ở các mốc này, đúng như đã nêu ở bước phân công.

**Rà phạm vi ảnh hưởng — 2 chỗ:**

(a) Không nâng thành quy ước toàn hệ thống. Các bước "Gửi thông báo" ở nhóm FR khác vẫn để nguyên — chúng đã nằm trong phạm vi bản gốc theo nhóm của mình. Ở đây chỉ vá đúng chỗ danh sách phạm vi bỏ sót nhóm X.1.

(b) **Hệ quả ngược — một bước phải loại trừ rõ.** `srs-fr-12-tv-chuyen-sau.md:219` gửi **kết quả tư vấn** cho doanh nghiệp *"qua Cổng PLQG hoặc email"* — đây là kênh riêng đã chốt của luồng trả kết quả, **không** áp quy tắc hai kênh vào. Phải ghi rõ ngoại lệ này khi sửa, nếu không Dev sẽ hiểu là phải bắn thêm thông báo trong ứng dụng cho một bên vốn không thao tác trên phần mềm quản trị.

---

# 3. Sau khi chuyên gia từ chối, màn hình ở lại hồ sơ mà chuyên gia không còn quyền xem

**Vấn đề:** Chuyên gia nhập lý do rồi bấm từ chối; hệ thống trả hồ sơ về hàng chờ và gỡ tên chuyên gia khỏi hồ sơ, nhưng vẫn giữ người dùng ở nguyên trang chi tiết. Từ giây đó hồ sơ không còn thuộc chuyên gia nữa — họ đang nhìn một trang mà tải lại là mất quyền.

**Bảng bóc ý con — Kết quả mong đợi `QLNDTVVCG_26`**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Hiển thị thông báo "Đã từ chối yêu cầu" | Không quy định câu chữ | Mục này (thống nhất câu chữ) |
| Quay về danh sách | Không quy định | Mục này |
| Gửi thông báo cán bộ phụ trách kèm lý do | Có (`srs-fr-12-tv-chuyen-sau.md:197`) | Đã đạt về nội dung; thiếu kênh thư — mục 2 |

**(1) Phần mềm đúng bản gốc chưa?** Bản gốc **im lặng** về điều hướng sau thao tác. Đã chứng minh ngược: quét toàn bộ quy ước giao diện dùng chung ở `srs-v3.5.md` Phụ lục E §H (H1–H8) — chỉ có **H7** nói về điều hướng, và nó chỉ phủ thao tác Thêm mới:

- `srs-v3.5.md:6715` — *"Sau khi thực hiện thành công thao tác **Thêm mới** một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông báo"*

Bảng bước xử lý (`srs-fr-12-tv-chuyen-sau.md:189-198`) và mục màn hình (`:1162`, `:1169`) đều chỉ nói tới sự tồn tại của hai nút, không nói màn hình đi đâu.

**(1b) Bản bàn giao nói gì? — CŨNG IM LẶNG, y như bản gốc.**

Mô tả nút Từ chối của chính chức năng này chỉ có hai dòng, dừng ở nghiệp vụ: *"Người sử dụng bấm 'Từ chối' và nhập lý do bắt buộc, hệ thống gỡ liên kết chuyên gia, chuyển trạng thái về Tiếp nhận, gửi thông báo cho CB NV để phân công lại và lưu vết thao tác kèm lý do từ chối."* — **không câu nào nói màn hình đi đâu**, cũng không có câu chữ thông báo.

Đã tra thêm luồng tương đương ở nhóm vụ việc (người được phân công từ chối tham gia): cũng chỉ có *"ghi nhận việc từ chối kèm lý do, đưa vụ việc trở lại trạng thái chờ phân công lại, gửi thông báo…"* — không có vế điều hướng. Trong toàn bản v3.5, các cụm *về màn hình danh sách · quay lại danh sách · trở về danh sách* chỉ còn ở nút "Quay lại danh sách" bấm tay và ở tình huống hồ sơ đã bị xoá.

⇒ **Cả bản gốc lẫn bản bàn giao đều im lặng.** Không có quy ước nào để viện, hai hướng đều chỉ dựa trên suy luận.

**(2) Đối tác yêu cầu khác bản gốc không?** Có. Vế *"quay về danh sách"* là kỳ vọng riêng của đối tác, không có gốc ở bản gốc lẫn bản v3.5. Lưu ý đối tác **không** phản ánh gì về vế này ở cột Kết quả thực tế — nó chỉ nằm ở cột Kết quả mong đợi.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Có một lý do thật, độc lập với tài liệu: chuyên gia chỉ thấy hồ sơ mình được giao, mà từ chối xong thì tên bị gỡ khỏi hồ sơ (`srs-fr-12-tv-chuyen-sau.md:196`). Ở lại trang chi tiết là để người dùng trước một trang mà tải lại sẽ mất quyền. Nhưng đây là suy luận về hệ quả, không phải điều khoản.

**→ Kết luận: sau khi chuyên gia từ chối, hệ thống hiển thị thông báo rồi QUAY VỀ MÀN DANH SÁCH. Đối tác ghi ĐÚNG. Dev action: Có (giao diện) · Sửa đặc tả: Có · Sheet: giữ xử lý.** ✅ **BA duyệt 06/08/2026.**

**Căn cứ:** chuyên gia không còn quyền trên hồ sơ vừa từ chối — bước `srs-fr-12-tv-chuyen-sau.md:196` gỡ tên họ khỏi hồ sơ. Giữ họ ở trang đó là giữ trước một trang mà tải lại sẽ mất quyền. Hướng này cũng trùng kỳ vọng đối tác nên đóng luôn tranh chấp, không phải giải trình.

> **Ghi lịch sử (mục này đã đảo 2 lần):** lượt đầu tự chốt "quay về danh sách" dựa trên một khuôn ở bản bàn giao cũ → đối chiếu bản v3.5 thì khuôn đó không còn, hạ xuống chờ BA → BA chốt 06/08 vẫn theo hướng quay về danh sách, nhưng nay căn cứ là **phạm vi quyền**, không phải khuôn tài liệu.

⚠️ **Hệ quả về verdict:** `QLNDTVVCG_26` giữ **xử lý** — có hai việc Dev phải làm: điều hướng (mục này) và bổ sung thư điện tử (mục 2). **Không phản hồi đối tác** — cả hai vế đều sửa toàn bộ.

### Phương án xử lý (cập nhật SRS)

Bổ sung vào mục Quy tắc tương tác `srs-fr-12-tv-chuyen-sau.md:1169`, viết theo **tiêu chí chung** để lần sau không phải hỏi lại từng nút:

> Thao tác làm bản ghi **rời khỏi phạm vi của người thao tác** → hiển thị thông báo thành công rồi **quay về màn danh sách**. Thao tác mà người thao tác **vẫn giữ bản ghi** → **ở lại màn chi tiết và làm mới dữ liệu**.

**Câu chữ thông báo:** đổi *"Đã từ chối nhiệm vụ"* thành **"Đã từ chối yêu cầu tư vấn"** — bám vốn từ của chính bản gốc (`:1317-1322` gọi bản ghi là *"Mã yêu cầu TV"*, *"Nội dung yêu cầu TV"*) và bám khuôn *"Đã từ chối tham gia vụ việc"* của nhóm vụ việc. Đây cũng gần đúng câu đối tác ghi trong Kết quả mong đợi.

**Hai chỗ phải quyết kèm, nếu không tiêu chí chung để lại vùng tự suy:**

1. **Nút Hoàn thành rơi vào đúng vế đầu của tiêu chí.** Khi chuyên gia bấm hoàn thành, hồ sơ rời khỏi trạng thái họ sửa được (`:1166` — *"Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)"*). Theo tiêu chí thì cũng phải quay về danh sách. Hoặc ghi rõ áp cho nút này, hoặc thu hẹp tiêu chí về đúng nút Từ chối — **đừng để đơn vị phát triển tự suy**. Hai nút còn lại của nhóm (cán bộ phê duyệt từ chối `:231`, hủy yêu cầu `:243`) cũng vậy.

2. **Chỗ đặt câu chữ thông báo — nên theo khuôn, nhưng không bắt buộc.** Quy ước viết màn hình liệt kê *"8. **Thông báo riêng** **(nếu có)** — UI message đặc thù SCR"* (`srs-fr-05-vu-viec.md:1616`) — tức khối này **tuỳ chọn**, và hiện toàn hệ thống mới có đúng một màn dùng nó (`SCR-V.I-03`). Đặt câu thông báo vào Quy tắc tương tác **không sai quy ước**. Nhưng nếu mục 6 cũng thêm câu chữ cho cùng màn này thì nên gom thành một khối "Thông báo riêng" cho gọn. *(Lượt soạn trước ghi "phải tạo khối đó" — nói quá, quy ước dùng chữ "nếu có".)*

> **Không chọi mục 6.** Hai mục nói về hai người khác nhau: mục này đưa **chuyên gia** về danh sách sau khi họ từ chối (đúng, vì `:196` gỡ tên họ khỏi hồ sơ); mục 6 hiện lý do cho **cán bộ nghiệp vụ** khi họ mở lại hồ sơ để phân công lại. Người bị đưa về danh sách không phải người cần đọc khối nhật ký.

**Đề nghị nâng lên quy ước chung — điểm treo, không làm trong đợt này.** Tiêu chí trên đúng cho mọi nhóm chức năng, không riêng tư vấn chuyên sâu; toàn hệ thống hiện **không có** quy ước điều hướng sau thao tác (Phụ lục E §H chỉ có H7 cho thao tác Thêm mới). Nếu để rải rác thì mỗi nhóm lại phát sinh một tranh chấp cùng kiểu.

---

# 4. Hệ thống chỉ nhận người loại Chuyên gia khi giao việc, trong khi đặc tả cho cả Tư vấn viên

**Vấn đề:** Cán bộ giao một yêu cầu tư vấn cho người thuộc mạng lưới; nếu người đó được ghi loại Tư vấn viên thì máy chủ từ chối, chỉ loại Chuyên gia mới giao được. Hệ quả là nửa mạng lưới không nhận được việc, và mọi kịch bản kiểm thử của luồng này chỉ phủ được một loại người.

**(1) Phần mềm đúng bản gốc chưa?** **Không kết luận được — bản gốc viết theo cả hai kiểu, và không kiểu nào áp đảo.**

**Đã đếm theo từng mục** (tệp `srs-fr-12-tv-chuyen-sau.md`, 1654 dòng, tách theo ranh giới mục):

| Mục | "CG/TVV" — ghi cả hai loại | "CG" / "Chuyên gia" đứng riêng |
|---|---|---|
| §1–2 Yêu cầu chức năng | 2 | 59 |
| §3 Màn hình | **0** | 23 |
| §4 Thực thể | 3 | 5 |
| §5 Máy trạng thái | 9 | 12 |
| §6 Quy tắc | 0 | 8 |
| **Tổng** | **14** | **107** |

**Bên nói CẢ HAI loại** — nằm ở chỗ chịu lực về dữ liệu:
- `:1324` trường lưu người nhận việc: *"`chuyen_gia_id` … FK → TU_VAN_VIEN(id) | | **CG/TVV** được phân công"*
- `:1490-1493` sơ đồ máy trạng thái: *"CB NV phân công **CG/TVV**"*, *"**CG/TVV** xác nhận tham gia"*, *"**CG/TVV** từ chối"*, *"**CG/TVV** tích Hoàn thành"*
- `:172` bước phân công: *"Kiểm tra **CG/TVV** được chọn"*
- `srs-v3.5.md:907` thuật toán gợi ý AG-01: *"**CG/TVV** phù hợp theo lĩnh vực PL"*
- **Không có ràng buộc loại ở bất kỳ đâu.** Công cụ để siết đã sẵn — `srs-v3.5.md:1725` khai *"`loai_tvv` … CHECK IN ('TVV','CG')"* — nhưng `chuyen_gia_id` chỉ ràng buộc *"phải đang hoạt động"*, không ràng buộc loại.

**Bên nói CHỈ Chuyên gia** — nằm ở chỗ chịu lực về phạm vi và giao diện:
- **Danh sách UC/Transaction, STT 147:** tên chức năng *"Quản lý nội dung tư vấn với **chuyên gia**"*, mô tả *"các nội dung tư vấn chuyên sâu từ DNNVV với cho **chuyên gia**"* — không nhắc tư vấn viên. STT 148 và 152 cũng vậy.
- **Toàn bộ §3 Màn hình: 0 lần "CG/TVV".** Ô chọn người được phân công `:1156` ghi *"Chuyên gia (dropdown searchable WHERE hoạt động)"*; gợi ý `:1167` *"TOP 5 CG"*.
- **Ba khối xử lý xác nhận / từ chối / hoàn thành** (`:181 · :193 · :204`) đều ghi *"user là **CG** được phân công"*. Riêng khối *Processing — CG từ chối* có 3 lần "CG", 0 lần TVV.
- **Mâu thuẫn ngay trong cùng một mục:** sơ đồ máy trạng thái `:1492` viết *"CG/TVV từ chối"*, bảng chuyển trạng thái ngay dưới `:1521` viết *"**CG** từ chối … Quay lại chọn **CG** khác"*.

**(1b) Bản bàn giao nói gì? — TỰ MÂU THUẪN giữa hai mục của chính nó.**

- **Mục đặc tả chức năng (4.12)** nói **chỉ Chuyên gia**: ô chọn người được phân công ghi *"Chuyên gia | Ô chọn có tìm kiếm | Có | … Bắt buộc chọn, **chỉ liệt kê chuyên gia đang hoạt động**"*. Toàn mục này không chỗ nào nhắc tư vấn viên.
- **Mục quy trình nghiệp vụ (3.12)** của cùng bản lại nói **cả hai**: cột Đối tượng thực hiện ghi *"**Chuyên gia / Tư vấn viên**"* ở 3 bước liên tiếp (xác nhận tham gia · tư vấn · hoàn thành nộp văn bản), và bước phân công ghi *"Chọn và gán **chuyên gia (hoặc tư vấn viên)** phù hợp với lĩnh vực yêu cầu"*.

⇒ Tỉ lệ trong bản gốc không áp đảo, và bản bàn giao tự chọi chính nó. **Không đủ căn cứ để tự khép.**

**(2) Đối tác yêu cầu khác bản gốc không?** Điểm này không do đối tác nêu — QA phát hiện khi phủ dạng dữ liệu thứ hai.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Có ảnh hưởng thật, theo cả hai chiều. Mở cho cả hai loại thì mạng lưới rộng hơn — Điều 10 Nghị định 55/2019 dựng mạng lưới gồm cá nhân tư vấn viên, tổ chức hành nghề luật sư và trung tâm tư vấn pháp luật, không tách riêng một hạng "chuyên gia" độc quyền. Siết về một loại thì đúng tên gọi của chính nhóm chức năng (*"tư vấn với chuyên gia"*) và đúng Danh sách UC.

**→ Kết luận: nội dung tư vấn chuyên sâu CHỈ giao cho Chuyên gia. Hiện trạng phần mềm ĐÚNG. Dev action: Không · Sửa đặc tả: Có (1 chỗ thêm ràng buộc + 6 chỗ dọn cách viết, đụng cả tệp nền) · Sheet: không có phiếu nào treo vào điểm này.** ✅ **BA duyệt 06/08/2026.**

**Căn cứ của quyết định:**
1. **Danh sách UC gọi bên tư vấn là "chuyên gia", không nhắc tư vấn viên ở đâu.** UC147 *"Quản lý nội dung tư vấn **với chuyên gia**"* và UC148 *"Tìm kiếm nội dung tư vấn **với chuyên gia**"* có chữ này ngay ở tên; UC152 có ở mô tả — *"các văn bản, tài liệu, nghiên cứu được **chuyên gia** sử dụng để tư vấn"*. Lưu ý cho chặt: đây là **tên nghiệp vụ gọi bên tư vấn**, không phải cột Tác nhân — Danh sách UC không phân biệt loại CG với loại TVV ở bất cứ đâu.
2. **Toàn bộ mục Màn hình: 0 lần "CG/TVV"** — ô chọn người được phân công ghi *"Chuyên gia (dropdown searchable WHERE hoạt động)"*, gợi ý ghi *"TOP 5 CG"*.
3. **Bản bàn giao, ở mục đặc tả chức năng, ghi thẳng** *"Bắt buộc chọn, **chỉ liệt kê chuyên gia đang hoạt động**"* — đây là mục đối tác dùng để chấm giao diện.

⇒ **Việc máy chủ chặn theo loại người là ĐÚNG, không phải lỗi.** Cụm "CG/TVV" rải trong bản gốc là cách viết lệch, phải dọn.

> **Ghi lịch sử (mục này đã đảo 2 lần):** lượt đầu tự chốt "cả hai loại" dựa trên 13 lần đặc tả viết "CG/TVV" → vòng soi độc lập đếm lại theo từng mục ra tỉ lệ **14 so với 107**, mục Màn hình **0 lần**, nên hạ xuống chờ BA → **BA chốt 06/08 theo hướng chỉ Chuyên gia**, ngược đề xuất của người soạn.

⚠️ **Hệ quả:** không log bug, không gửi Dev. Điểm này QA nêu là "giới hạn phạm vi kiểm thử" — nay đã rõ: kịch bản chỉ phủ dạng "người được giao là Chuyên gia" là **đúng và đủ**, không phải thiếu.

### Phương án xử lý (cập nhật SRS)

Đặc tả đang viết hai kiểu ở 5 mục, **cả tệp nhóm lẫn tệp nền**. Bảng dưới: 1 dòng đầu là thêm ràng buộc, 6 dòng sau là dọn câu chữ.

| Chỗ | Việc |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:111` trường lưu người nhận việc | thêm ràng buộc **`loai_tvv` = 'CG'** vào cột Ràng buộc (hiện chỉ có *"phải đang hoạt động"*) |
| `:1324` mô tả trường `chuyen_gia_id` | *"CG/TVV được phân công"* → **"CG được phân công"** |
| `:172` · `:174` hai bước phân công | *"CG/TVV"* → **"CG"** |
| `:1490-1493` sơ đồ máy trạng thái (4 chuyển tiếp) · `:1507-1509` bảng trạng thái · `:1519` bảng chuyển tiếp | *"CG/TVV"* → **"CG"**, cho khớp bảng `:1521` vốn đã ghi "CG" |
| `:1217` · `:1370` mô tả LICH_SU_TRAO_DOI_TV | *"giữa DN và CG/TVV"* → **"giữa DN và CG"** |
| `srs-v3.5.md:907` thuật toán gợi ý AG-01 | *"CG/TVV phù hợp theo lĩnh vực PL"* → **"CG phù hợp…"** |
| **`srs-fr-12-tv-chuyen-sau.md:1221`** — chỗ vi phạm viết bằng chữ đầy đủ nên vô hình với mẫu tìm "CG/TVV" | *"| 7 | TU_VAN_VIEN | referenced | **Chuyên gia/TVV được phân công tư vấn** |"* → bỏ "/TVV" |
| **Tệp nền — 11 chỗ cùng nội dung, phải sửa song song** | `srs-v3.5.md:1262` · `:2125` (bản gốc của `:1324`) · `:3237` · `:6231-6234` (sơ đồ SM-TVCS, 4 nhánh) · `:6248-6250` (bảng trạng thái) · `:6260` (bảng chuyển tiếp). **Không đụng** 10 chỗ "CG/TVV" còn lại ở tệp nền — đó là **tên nhóm chức năng IV**, không liên quan |

Giữ nguyên: nhãn ô chọn `:1156`, gợi ý `:1167`, mã lỗi E2 `:320`, ma trận `srs-v3.5.md:1336` cột TVV = `R*` — tất cả đã đúng theo hướng đã chốt.

**Bốn việc bắt buộc kèm theo — thiếu một trong số này là áp không được:**

1. ⚠️ **Sửa cột "Bắt buộc" của `:111` từ Y thành N, cùng lượt.** Bảng dữ liệu đầu vào ghi `chuyen_gia_id … **Y**`, còn bảng thực thể `:1324` ghi **N**; hồ sơ lại được tạo ở trạng thái *Tiếp nhận* trước khi có người nhận (`:1518`). Chèn ràng buộc loại mà giữ nguyên "Y" thì **mọi hồ sơ tạo mới đều vướng**, kể cả hồ sơ từ Cổng.

2. **Ghi rõ cách xử ở bước liên kết của luồng nhận dữ liệu từ Cổng — dùng đúng đường đã có, không đẻ mã lỗi mới.** `:487` hiện ghi *"Liên kết chuyên gia nếu có thông tin (match theo mã chuyên gia)"*; mã này dò vào `TU_VAN_VIEN.ma_tvv` là mã dùng chung cho cả hai loại. Sửa thành: **chỉ nối khi người đó loại Chuyên gia; ngược lại bỏ nối và ghi cảnh báo vào nhật ký**, hồ sơ vẫn vào ở trạng thái *Tiếp nhận* để cán bộ phân công.

   **Không cần mã lỗi mới, không cần sửa hợp đồng API** — hai lý do:
   - Trường thông tin chuyên gia trong payload vốn **không bắt buộc** (`:454` — `chuyen_gia_info | structured | **N**`), nên đường "hồ sơ vào mà không gắn ai" đã tồn tại sẵn và là đường bình thường. Ca gặp mã tư vấn viên chỉ việc đi vào đúng đường đó.
   - API chiều ra chia sẻ danh bạ cho Cổng (`srs-fr-16-api.md` FR-XII-05) **đã có trường `loai`** ở cả đầu vào lẫn đầu ra — *"`loai` | text | luôn | **TVV / CG** `[STT14]`"* — nên Cổng đã đủ dữ liệu để tự lọc ô chọn. Ca này là **lỗi dữ liệu phía Cổng**, không phải lỗ hổng thiết kế.

   Thêm trường `loai` vào payload chiều vào là **thừa và có hại**: hệ thống dò mã vào danh bạ của chính mình nên đã biết loại; lấy bản sao bên ngoài phán về dữ liệu gốc của mình chỉ tạo thêm tranh chấp "Cổng nói CG, danh bạ nói TVV thì tin ai".

   Kèm một dòng cho bên tích hợp: Cổng lọc ô chọn người tư vấn theo trường `loai` sẵn có.

3. **Điều khoản cho hồ sơ cũ: DUNG NẠP như ngoại lệ lịch sử, có đánh dấu.** ✅ **BA duyệt 06/08/2026.** Ràng buộc loại chỉ áp ở **thời điểm gán mới**, **không hồi tố**. Hồ sơ đang chạy dở với tư vấn viên thì chạy tiếp cho xong; hệ thống đánh dấu để cán bộ xử khi phù hợp.

   Ba căn cứ:
   - **Tiền lệ khớp nhất trong bản gốc là dung nạp, không phải ép.** `srs-fr-11-bao-cao.md:987` — *"dữ liệu cũ chưa gán lĩnh vực (nếu có) gom tạm vào nhóm 'Chưa phân loại' **kèm yêu cầu bổ sung**"*. Tiền lệ ép điền (`srs-fr-12:1318`, tiêu đề) áp được vì tiêu đề **sinh máy móc được**; ở đây thì không — hệ thống không tự chọn thay người cho một hồ sơ đang tư vấn dở.
   - **Chính bản gốc còn chưa biết có dữ liệu cũ hay không:** `srs-v3.5.md:4683` — *"| INS-06 | Data migration | 🟡 **Chờ khảo sát: có dữ liệu cũ cần migrate không**, format nào, volume bao nhiêu | 🟡 Chờ CĐT |"*.
   - Chặn giữa chừng là cắt việc đang làm của doanh nghiệp vì một chuyện phân loại nội bộ.

4. **Siết luôn `ma_chuyen_gia` ở bảng đánh giá chất lượng.** `:1463` — *"`ma_chuyen_gia` | text | N | Liên kết `TU_VAN_VIEN.ma_tvv` | — | CG được đánh giá"* — mô tả nói "CG" nhưng không có ràng buộc. Bỏ qua thì hệ thống vẫn cộng điểm tư vấn chuyên sâu vào hồ sơ một tư vấn viên.

**Doc action:** bản `.docx` v3.5 phải sửa 4 chỗ — bước phân công (*"gán chuyên gia (hoặc tư vấn viên)"*) và cột Đối tượng thực hiện ở 3 bước liên tiếp (*"Chuyên gia / Tư vấn viên"*).

⚠️ **Nên ghi một câu lý do nghiệp vụ vào đặc tả.** Nhóm này **không viện dẫn căn cứ pháp lý nào** (đã tra: 0 lần nhắc NĐ 55/2019 và NĐ 77/2008). Mà theo cách chính đặc tả đọc NĐ 55/2019 Điều 10, mạng lưới gồm ba thành phần — tư vấn viên cá nhân, tổ chức hành nghề luật sư, trung tâm tư vấn pháp luật — **không có hạng "Chuyên gia"**; hạng này do hệ thống tự đặt trong danh sách giá trị. Tức quyết định đang giữ hạng không có tên trong văn bản và loại hạng có tên (tư vấn viên, có Thẻ theo NĐ 77/2008 Đ.19). Không sai luật vì đặc tả không viện dẫn, nhưng một câu lý do nghiệp vụ sẽ chặn được chất vấn khi nghiệm thu.

**Rà phạm vi ảnh hưởng — 3 chỗ, đều là KHÔNG phải sửa (ghi ra để lượt sau khỏi mở lại):**

(a) `srs-v3.5.md:1337` PHIEN_TU_VAN cột TVV `R*` và `:1338` LICH_SU_TRAO_DOI_TV cột TVV `—` — **giữ nguyên**, đúng với việc tư vấn viên không nhận việc ở nhóm này.

(b) `srs-v3.5.md:5503` BR-AUTH-14 viết đích danh *"Chuyên gia (CG)"* — **giữ nguyên**, nay khớp tuyệt đối với quyết định này.

(c) Bảng `TU_VAN_VIEN` vẫn giữ cả hai giá trị `CHECK IN ('TVV','CG')` — quyết định này **không** đụng cấu trúc mạng lưới, chỉ giới hạn ai được nhận việc ở nhóm tư vấn chuyên sâu.

---

# 5. Quản trị viên vào được màn báo cáo, bấm xuất tệp thì bị máy chủ từ chối

**Vấn đề:** Tài khoản quản trị hệ thống mở được màn báo cáo thống kê, xem được số liệu, nút xuất tệp vẫn sáng — nhưng bấm vào thì bị từ chối. Người dùng bị mời làm một việc rồi mới bị chặn, và câu từ chối hiện ra không phải câu của phần mềm.

**Bảng bóc ý con — Kết quả mong đợi 5 phiếu B2**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Xuất và tự động tải tệp về máy | Có (`srs-fr-11-bao-cao.md:123`) | Mục này — đã đạt với vai trò có quyền |
| Tên tệp theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` | Có (Phụ lục E §H8) | Đã đo đạt ở vai trò cán bộ nghiệp vụ, không tranh chấp |

**(1) Phần mềm đúng bản gốc chưa?** Phần chặn **ĐÚNG**. Vai trò quản trị hệ thống không phải tác nhân của bất kỳ chức năng báo cáo nào:

- `srs-fr-11-bao-cao.md:62` — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"*
- `srs-fr-11-bao-cao.md:51` — *"Tác nhân chính: Cán bộ Nghiệp vụ (TW/BN/ĐP), Cán bộ Phê duyệt (TW/BN/ĐP)"*

**Đã đếm:** tệp nhóm báo cáo có **23** mục FR, cả **23/23** đều ghi Tác nhân là *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"* — không mục nào nhắc quản trị hệ thống.

**Đối chiếu Danh sách UC/Transaction — trọng tài cho phạm vi tác nhân:** đúng **23** giao dịch báo cáo thống kê (STT 124–146), khớp một-một với 23 mục FR, đều ghi tác nhân *"Cán bộ nghiệp vụ TW,BN,ĐP/Cán bộ phê duyệt TW,BN,ĐP"*. **23/23 không có quản trị hệ thống.**

**Về lập luận "xuất là một dạng đọc":** không đứng được, nhưng lý do không phải như phiếu QA nêu. Bản gốc tự khai luồng báo cáo là chỉ đọc (`srs-fr-11-bao-cao.md:105` — *"Không thay đổi dữ liệu nghiệp vụ (read-only)"*), nên lập luận "xuất tệp là quyền Tạo" bị chính bản gốc bác. Chỗ quyết định nằm khác: **Xem và Xuất là MỘT chức năng, không phải hai.** Định dạng xuất là **trường nhập bắt buộc** của chính yêu cầu báo cáo (`srs-fr-11-bao-cao.md` §Input chung, `format_xuat | text | Y | XLSX / PDF`). Đã không phải tác nhân của chức năng thì không có phần nào của chức năng.

Ô `R` của quản trị hệ thống ở `srs-v3.5.md:1335` là **quyền mức dữ liệu phục vụ quản trị**, không phải quyền thực hiện chức năng nghiệp vụ. Đã đếm cột này trên toàn ma trận: **60 dòng `R` / 10 dòng `CRUD`**, và cả 10 dòng `CRUD` đều là thực thể cấu hình - quản trị (danh mục, tài khoản, vai trò, quyền hạn, đơn vị, cấu hình thời hạn, ngày lễ, tiêu chí đánh giá và 2 bảng liên kết). Không dòng nghiệp vụ nào cho quản trị viên quyền ghi.

**Và việc quản trị viên vào được màn báo cáo là TRÁI một quy ước đã có sẵn** — `srs-v3.5.md:684`: *"| M-05 | **Hiển thị theo quyền** — menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó. **Ẩn (không disable) nếu không có quyền** |"*. Quy ước này áp toàn hệ thống. Vậy đây không phải chỗ đặc tả im lặng — đặc tả đã quy định, phần mềm làm chưa đúng.

**Căn cứ nghiệp vụ dứt điểm:** tệp xuất là **văn bản hành chính**, không phải bản trích dữ liệu:

- `srs-fr-11-bao-cao.md:86` — *"tạo file .pdf theo khung văn bản hành chính Thông tư 17/2025 … **đầu trang** có quốc hiệu, tiêu ngữ và tên cơ quan ban hành; **cuối trang** có ngày ký, **họ tên cán bộ xuất báo cáo** và chỗ trống cho con dấu khi in chính thức"*

Cho quản trị viên xuất tệp là để tên một người không phải cán bộ nghiệp vụ đứng dưới một văn bản có quốc hiệu và chỗ đóng dấu. Đó là lý do đủ để chốt, độc lập với mọi tranh luận về chữ `R` hay `C`.

**(1b) Bản bàn giao nói gì? — chốt thẳng, còn rõ hơn cả bản gốc.**

Mở đầu toàn bộ nhóm báo cáo là một dòng dứt khoát, **áp cho cả 23 báo cáo**: *"**Quy tắc chung của các báo cáo thống kê** (áp dụng cho toàn bộ các mục 4.11.1 đến 4.11.23): • **Người thực hiện là cán bộ nghiệp vụ hoặc cán bộ phê duyệt** ở Trung ương, bộ ngành, địa phương."* Nút xuất chỉ đặt thêm một điều kiện trạng thái: *"đã xem báo cáo và có dữ liệu"*.

⇒ Chính tài liệu đối tác được giao đã loại vai trò quản trị viên khỏi chức năng này. Đối tác đo bằng tài khoản quản trị viên là **thao tác sai vai trò so với văn bản họ đang cầm**, không phải phần mềm sai.

**(2) Đối tác yêu cầu khác bản gốc không?** Khác ở chỗ họ thao tác bằng vai trò không có quyền — cả 10/10 ảnh hai vòng đều hiện "Quản trị viên · QTHT". Kỳ vọng *"xuất và tải tệp về máy"* của họ đúng, chỉ là đo bằng vai trò sai.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Việc nới quyền: KHÔNG. Việc sửa giao diện mời-rồi-chặn: CÓ — người dùng phải biết trước là không dùng được.

**→ Kết luận: vai trò Quản trị hệ thống KHÔNG phải tác nhân của chức năng báo cáo thống kê — không xuất tệp, và cũng không vào màn báo cáo. Máy chủ chặn xuất là ĐÚNG, không nới quyền. Giao diện sai ở chỗ vẫn mở màn và vẫn mời bấm nút xuất. Dev action: Có (giao diện) · Sửa đặc tả: Có (ghi rõ điều kiện vai trò + bổ sung mã lỗi cho thao tác xuất) · Sheet: giữ xử lý cho cả 5 phiếu (189 · 222 · 226 · 230 · 234).** ✅ Tự chốt theo cây trọng tài — tầng "CSV UC/Transaction".

> **Lưu ý phạm vi — rộng hơn câu QA hỏi.** QA chỉ hỏi "có được xuất không" và đề xuất giữ quyền xem. Nhưng đã lấy tiền đề `:62` làm căn cứ thì không dừng nửa chừng được: tiền đề đó chặn ở mức **truy cập chức năng**, không phải ở mức thao tác xuất. Giữ quyền xem mà chặn quyền xuất là tự mâu thuẫn với chính căn cứ vừa dùng. Nếu chị muốn giữ quyền xem cho quản trị viên (phục vụ vận hành, hỗ trợ người dùng) thì đó phải là **ngoại lệ được ghi thành văn** ở `srs-fr-11-bao-cao.md:62`, không phải suy ra từ ô `R` của ma trận.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-11-bao-cao.md:79` — bước 1 ghi rõ kiểm **vai trò** trước khi kiểm phạm vi đơn vị; chặn ngay ở cửa vào chức năng, không để tới lúc bấm xuất.
2. `srs-fr-11-bao-cao.md:1052` và `:1053` — cột Điều kiện hiển thị của hai nút xuất: thêm *"và người dùng có vai trò Cán bộ nghiệp vụ hoặc Cán bộ phê duyệt"*.
3. **Ghi ngoại lệ ở khối chú thích ký hiệu, KHÔNG ghi vào một dòng.** Đặt ở `srs-v3.5.md:1294` (chú giải ký hiệu) hoặc khối chú thích chung `:1382-1388`: ô `R` của quản trị hệ thống là quyền đọc dữ liệu mức quản trị, **không kèm quyền thực hiện chức năng nghiệp vụ**. Ghi vào riêng dòng `:1335` thì ngầm khẳng định 59 dòng `R` còn lại **có** kèm quyền chức năng — đúng điều mục này vừa bác.
4. **Nút Xem báo cáo và ô chọn loại báo cáo cũng phải theo cùng điều kiện.** `srs-fr-11-bao-cao.md:1051` hiện ghi nút Xem báo cáo *"**Luôn hiển thị**"*; `:1047` ô chọn loại báo cáo cũng vậy. Kết luận là quản trị viên không vào màn, nên sửa cả hai — nếu không thì vẫn "mời rồi chặn", chỉ lùi một bước.
5. **Gỡ ba mã quyền báo cáo khỏi vai trò quản trị viên ở dữ liệu khởi tạo.** Quy ước M-05 ẩn menu theo **quyền truy cập chức năng**, không theo vai trò viết tay. Không gỡ ở tầng quyền thì đơn vị phát triển sẽ ẩn bằng cách kiểm vai trò trực tiếp, không đi qua cơ chế phân quyền.
6. **Bổ sung mã lỗi cho thao tác xuất — chỗ này sửa cả bug QA đã log.** Nhóm báo cáo chỉ có **một** dòng lỗi quyền: `srs-fr-11-bao-cao.md:117` — *"Bạn không có quyền **xem** báo cáo này"* (`ERR-RPT-05`). Dùng nó cho tình huống chặn **xuất** thì sai bản chất — người dùng đang xem được mà hệ thống lại báo không được xem. Câu đúng đã có ở quy ước chung mục E (`srs-fr-05-vu-viec.md:1594`): *"Bạn không có quyền thực hiện thao tác này"*. Chèn thành dòng **E10 / `ERR-RPT-08`** (bảng lỗi `:109-119` hiện chạy E1–E9). **Cần báo lại QA chỉnh phiếu `BUG-BCTK-QA01`** — phiếu đó đang yêu cầu Dev hiện đúng câu `:117`.
7. ⚠️ **Gỡ dòng "QTHT bypass" nằm ngay trong tệp làm căn cứ.** `srs-fr-11-bao-cao.md:1268` — *"| BR-AUTH-08 | … | **Toàn bộ FR-IX** | **QTHT bypass** | Verify phân quyền |"*. Câu này giả định quản trị viên **có** chạy nhóm báo cáo (không chạy thì không có gì để bỏ qua) — trái thẳng kết luận vừa chốt. Bỏ sót dòng này là đủ để đối tác mở lại phiếu.

**Chạm tệp nền `srs-v3.5.md` đúng MỘT chỗ — việc số 3.** Sáu việc còn lại nằm trong `srs-fr-11-bao-cao.md` và dữ liệu khởi tạo.

*Bốn dòng khác ở tệp nền chỉ là **căn cứ trích dẫn, KHÔNG sửa**: `:1335` dòng BAO_CAO giữ nguyên `R` · `:684` quy ước M-05 · `:834`, `:5476` (BR-AUTH-03), `:5485` (BR-AUTH-08) — ba dòng cuối là ngoại lệ về **phạm vi dữ liệu**, không phải quyền chạy chức năng. Ghi ra để lượt sau khỏi sửa nhầm.*

> **Điểm treo phát hiện khi rà, không làm trong đợt này:** `srs-v3.5.md:3150` khẳng định module báo cáo có **3 mã quyền** và trỏ danh sách về `srs-fr-10-quan-tri.md` §3.4.3.41 — nhưng mục đó **không có danh sách nào**. Nên hiện không tra được ba mã quyền đó là gì. Nhóm Hỏi đáp thì có bảng quyền mức thao tác (`srs-v3.5.md:1416` — `HOI_DAP_EXPORT`), nhóm báo cáo không có bảng tương ứng.

> **Phản hồi gửi đối tác** (ghi vào một dòng đại diện cho cả cụm 5 phiếu, các dòng còn lại để trống):
>
> **[Lý do]** Chức năng báo cáo thống kê được thiết kế cho cán bộ nghiệp vụ và cán bộ phê duyệt, vì tệp kết xuất là văn bản hành chính có quốc hiệu, tiêu ngữ, tên cơ quan và họ tên cán bộ lập báo cáo. Tài khoản quản trị hệ thống không thuộc nhóm này nên không thực hiện được thao tác xuất tệp. Kịch bản kiểm thử vừa qua được thực hiện bằng tài khoản quản trị viên nên bị từ chối.
>
> **[Nhận định]** Kính đề nghị Quý đơn vị kiểm thử lại bằng tài khoản cán bộ nghiệp vụ hoặc cán bộ phê duyệt. Phần giao diện còn hiển thị nút xuất cho tài khoản quản trị viên là điểm chưa đúng của phần mềm, đơn vị phát triển sẽ chỉnh sửa.

---

# 6. Cán bộ phải phân công lại nhưng không tra lại được lý do chuyên gia từ chối

**Vấn đề:** Chuyên gia từ chối kèm lý do; cán bộ phụ trách nhận được lý do đó ngay lúc bị từ chối. Nhưng khi mở lại hồ sơ để giao cho người khác — có thể vài ngày sau — khối nhật ký trên hồ sơ chỉ hiện đã có thao tác, không hiện vì sao. Muốn xem thì phải nhờ quản trị viên mở nhật ký hệ thống.

**(1) Phần mềm đúng bản gốc chưa?** ĐÚNG, theo đúng chữ. Cả hai vế bản gốc đòi đều đã đạt:

- `srs-fr-12-tv-chuyen-sau.md:198` — *"Ghi nhật ký thao tác (kèm lý do từ chối)"* → Dev đo lại: lý do **có** được lưu, không bị lượt sau ghi đè.
- Đặc tả **cố ý** không tạo cột lý do trên bảng dữ liệu — tiền lệ đã chốt cho thao tác hủy tại `:244`: *"…**KHÔNG lưu thành cột riêng trên entity**"*. Lý do sống ở nhật ký, đúng thiết kế.
- `srs-fr-12-tv-chuyen-sau.md:1160` — khuôn hiển thị của khối nhật ký trên hồ sơ chỉ gồm ba phần: *"dd/mm/yyyy HH:mm -- {User} -- {Hành động}"* — **không có chỗ cho lý do**. Phần mềm đang hiện đúng khuôn này.
- Bản `.docx` v3.5 ghi y hệt, nên không có tranh chấp tài liệu ở điểm này: *"Nhật ký thao tác | Danh sách theo thời gian | Chỉ đọc. **Mỗi dòng gồm ngày giờ, người thực hiện và hành động.**"*

Đã chứng minh ngược khẳng định "bản gốc không đòi hiển thị lý do": quét biến thể *lý do từ chối · ly_do · lý do* trong toàn tệp nhóm; bảng thực thể `:1310-1338` **không có cột lý do từ chối** — bản gốc cố ý để lý do nằm ở nhật ký, đúng tiền lệ đã chốt cho thao tác hủy tại `:244` (*"KHÔNG lưu thành cột riêng trên entity"*).

**Và không có quy tắc dùng chung nào phủ ca này.** BR-FLOW-04 (`srs-fr-12-tv-chuyen-sau.md:1614`) trông giống nhưng là chuyện khác: nguyên văn *"**Mọi hành động từ chối phê duyệt** PHẢI có lý do…"*, cột Áp dụng ghi *"FR-X.1-01 (**CB PD từ chối TVCS**)"* — tức cán bộ phê duyệt từ chối phê duyệt, không phải chuyên gia từ chối nhận việc. Việc không có quy tắc nào phủ lại củng cố cho quyết định cải tiến.

⇒ Mô tả của QA (*"không thấy lý do trong nhật ký"*) chưa chính xác như Dev đã đo lại. **Đây không phải lỗi.**

**(1b) Bản bàn giao nói gì? — GIỐNG HỆT bản gốc, không có tranh chấp tài liệu.**

- Khuôn hiển thị khối nhật ký: *"Nhật ký thao tác | Danh sách theo thời gian | Chỉ đọc. **Mỗi dòng gồm ngày giờ, người thực hiện và hành động.**"* — đúng ba thành phần như `srs-fr-12-tv-chuyen-sau.md:1160`, **không có ô lý do**.
- Bước từ chối: *"gửi thông báo cho CB NV để phân công lại và **lưu vết thao tác kèm lý do từ chối**"* — lý do gắn với lưu vết, không gắn với thông báo, cũng không gắn với khối nhật ký trên hồ sơ.

⇒ Hai tài liệu nói giống nhau. Đây thuần là **quyết định cải tiến**, không phải chỗ tài liệu lệch nhau.

**(2) Đối tác yêu cầu khác bản gốc không?** Điểm này không do đối tác nêu.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** Đây là chỗ **BA phải cân**, không tự khép được. Lý do từ chối quyết định cách phân công lại: *"không đúng chuyên môn"* thì phải đổi người, *"đang quá tải"* thì vẫn người đó nhưng lùi lịch.

⚠️ **Một dữ kiện làm nhu cầu này nặng hơn tôi tưởng ban đầu.** Tôi từng lập luận "cán bộ đã nhận được lý do qua thông báo rồi". Lập luận đó **không có gốc đặc tả**:
- Bước `:197` chỉ ghi *"Gửi thông báo CB NV: CG từ chối, cần phân công lại"* — **không** yêu cầu đính lý do. Việc thông báo hiện có kèm dòng "Lý do: …" là đơn vị phát triển làm thêm.
- Bản bàn giao cũng vậy: *"gửi thông báo cho CB NV để phân công lại và **lưu vết thao tác kèm lý do từ chối**"* — lý do gắn với **lưu vết**, không gắn với thông báo.

⇒ Theo văn bản, lý do từ chối **chỉ sống trong nhật ký hệ thống mà chỉ quản trị viên đọc được**. Cán bộ phải phân công lại không có đường nào chính thức để xem. Ngược lại, mở toàn bộ nội dung nhật ký ra hồ sơ thì lộ mọi trường của bản ghi cho bất kỳ ai xem được hồ sơ.

**→ Kết luận: yêu cầu "ghi nhật ký kèm lý do từ chối" là ĐẠT — không phải lỗi. Nhưng chốt cải tiến: HIỆN LÝ DO CÓ KIỂM SOÁT trên khối nhật ký của hồ sơ. Dev action: Có · Sửa đặc tả: Có · Sheet: giữ xử lý.** ✅ **BA duyệt 06/08/2026.**

⚠️ **Ghi rõ để Dev và QA không hiểu nhầm:** đây **không phải bug** — dữ liệu đã ghi đúng đặc tả. Đây là **cải tiến đã được duyệt**, làm vì cán bộ phải phân công lại cần tra lại lý do. Phiếu `QLNDTVVCG_OOS_04` để **giữ xử lý**, không Reject.

### Phương án xử lý (cập nhật SRS + Dev)

**Cách làm** — theo đúng phương án đơn vị phát triển đề xuất (*tách nhãn riêng cho thao tác Từ chối và hiển thị đúng phần lý do trên hồ sơ*, thay vì hiện toàn bộ bản chụp hồ sơ), thêm ràng buộc phạm vi:

1. **Tách nhãn riêng cho thao tác Từ chối** — hiện đang gộp vào nhãn "Cập nhật".
2. **Hiển thị duy nhất phần lý do** trên khối nhật ký của hồ sơ. **Không** mở các trường khác của bản chụp hồ sơ — đây là điểm đơn vị phát triển cảnh báo đúng: khối này là bản chụp toàn bộ hồ sơ tại từng thời điểm, hiện hết sẽ lộ mọi trường cho bất kỳ ai xem được hồ sơ.
3. **Phạm vi xem:** mở cho **vai trò nội bộ xem được hồ sơ** — cán bộ nghiệp vụ, cán bộ phê duyệt, và người hỗ trợ theo phạm vi đơn vị (`srs-fr-12-tv-chuyen-sau.md:37`). **KHÔNG** mở cho chính người trong mạng lưới tư vấn.

   *(Câu này ở lượt soạn trước viết là "không mở cho vai trò ngoài mạng lưới" — sai ngược: cán bộ nghiệp vụ chính là vai trò ngoài mạng lưới, tức câu cũ chặn đúng người mà mục này phục vụ.)*

4. **Nguồn của nhãn hiển thị — khuôn đã có sẵn, chỉ là nhóm này chưa dựng bảng của mình.** Bảng nhật ký đã có giá trị `REJECT` trong danh sách hành động (`srs-v3.5.md:2204`). Và bản gốc đã **bắt buộc** mỗi thực thể có vòng đời phải khai bảng quyền mức thao tác kèm tên hành động tiếng Việt: `srs-v3.5.md:1392` — *"Mỗi entity có vòng đời workflow **SHALL** định nghĩa **permission codes action-level** theo format `{ENTITY}_{ACTION}` … Dưới đây là bảng cho HOI_DAP — **template cho các entity workflow khác**"*, ví dụ `:1411` — *"| `HOI_DAP_REJECT` | **Từ chối phản hồi** | CB_PD_{cap} | … |"*.

   ⇒ Việc phải làm **không phải** dựng một bảng ánh xạ mới, mà là **dựng bảng quyền mức thao tác cho `TU_VAN_CHUYEN_SAU` theo đúng khuôn đã bắt buộc** — nhãn "Từ chối" lấy từ đó. Rẻ hơn nhiều và đúng khuôn sẵn có. *(Lượt soạn trước ghi "toàn hệ thống không có bảng ánh xạ" — sai, chưa chứng minh ngược.)*

**Sửa đặc tả — 2 chỗ:**

| Chỗ | Việc |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1160` khuôn khối nhật ký | giữ *"{thời điểm} — {người thao tác} — {hành động}"*; riêng hành động **Từ chối** thêm dòng phụ *"Lý do: {nội dung}"*. Các hành động khác giữ nguyên ba phần |
| `srs-fr-12-tv-chuyen-sau.md:197` bước gửi thông báo | bổ sung: thông báo gửi cán bộ **phải đính lý do từ chối** — để việc đơn vị phát triển đang làm thêm trở thành yêu cầu có văn bản |

**Hai ca cùng bệnh trong chính tệp này — chốt luôn phạm vi để lượt sau khỏi mở phiếu:**
- `:232` cán bộ phê duyệt từ chối phê duyệt — *"Ghi nhật ký thao tác (kèm lý do từ chối)"*; hồ sơ quay về *Đang tư vấn*, **chuyên gia phải bổ sung nội dung nhưng cũng không có đường chính thức xem lý do**. Đề nghị áp cùng cách.
- `:244` hủy yêu cầu — lý do hủy cũng chỉ sống ở nhật ký, *"KHÔNG lưu thành cột riêng trên entity"*. Đề nghị áp cùng cách.

**Rà chiều ngược:** bản bàn giao cũng phải sửa hai chỗ tương ứng — khuôn khối nhật ký (hiện ghi *"Mỗi dòng gồm ngày giờ, người thực hiện và hành động"*) và bước từ chối.

---

# 7. Chuyên gia sửa được nội dung của bất kỳ hồ sơ tư vấn nào trong đơn vị mình

**Vấn đề:** Tài khoản chỉ mang vai trò mạng lưới tư vấn hiện sửa được nội dung tư vấn của mọi hồ sơ trong đơn vị — kể cả hồ sơ không giao cho mình — và gọi được thao tác tạo mới. Người trong mạng lưới là bên ngoài cơ quan, không phải cán bộ, nên đây là chỗ hở về phạm vi dữ liệu chứ không chỉ là chuyện nhãn quyền.

**(1) Phần mềm đúng bản gốc chưa?** SAI ở **phạm vi**, không sai ở **bản chất**. Phải tách làm hai vế — Dev đang trình bày như một câu hỏi nhị phân "giữ nguyên hay siết hết", nhưng bản gốc trả lời khác nhau cho hai vế.

**Vế Tạo mới — bản gốc không cho:**

- `srs-fr-12-tv-chuyen-sau.md:97` — *"Tác nhân: Cán bộ Nghiệp vụ (TW/BN/ĐP)"*
- `srs-fr-12-tv-chuyen-sau.md:329-335` — **7/7** điều kiện chấp nhận đều mở đầu bằng *"Given **CB NV**…"*, gồm cả *"CB NV ghi nhận nội dung tư vấn"* và *"CB NV cập nhật nội dung"*
- Danh sách UC/Transaction, STT 147 — tác nhân *"Cán bộ nghiệp vụ TW,BN,ĐP"*. Đã quét toàn bộ **188 UC / 722 dòng giao dịch**: **không UC nào** có "Chuyên gia" ở cột Tác nhân.
- `srs-fr-12-tv-chuyen-sau.md:37` — chính bản gốc đã dùng lập luận này để loại Người hỗ trợ: *"NHT KHÔNG có CRUD (UC147 actor = chỉ CB NV)"*

**Vế Sửa — bản gốc CÓ cho, nhưng chỉ trong một cửa sổ hẹp.** Đây là chỗ nếu siết phẳng theo hướng "chỉ cán bộ được sửa" thì **làm tắc luồng**:

- `srs-fr-12-tv-chuyen-sau.md:231` — khi cán bộ phê duyệt từ chối, hồ sơ quay về *Đang tư vấn* và *"Gửi thông báo CG: **cần bổ sung nội dung**"*
- `srs-fr-12-tv-chuyen-sau.md:1166` — *"Mode sửa chỉ khi trạng thái IN (TIEP_NHAN, DANG_TU_VAN)"*; `:1162` — ở trạng thái *Đang tư vấn* thanh hành động có nút **[Lưu]**
- Bản `.docx` v3.5 nói thẳng hơn — bước *Tư vấn pháp luật chuyên sâu*, đối tượng thực hiện là Chuyên gia / Tư vấn viên: *"**soạn thảo văn bản tư vấn pháp luật trên trình soạn thảo của hệ thống** (tự động lưu bản nháp mỗi 30 giây); đính kèm tư liệu pháp lý liên quan"*

Người làm việc ở trạng thái *Đang tư vấn* chính là người được giao. Vậy quyền `U` của họ là có thật — cái sai là **phạm vi**: hiện áp theo đơn vị (thấy hồ sơ nào sửa hồ sơ đó), đáng lẽ phải **đích danh theo bản ghi được giao**, và chỉ ở đúng trạng thái đang tư vấn.

**Khuôn để bám đã có sẵn, do chính BA chốt cho cùng nhóm chức năng này:**

- `srs-v3.5.md:5503` — BR-AUTH-14, BA chốt 2026-06-03: *"Chuyên gia (CG) chỉ được ĐỌC/tải tư liệu pháp lý (UC152) của TVCS mà mình là `chuyen_gia_id` … (**đích danh theo bản ghi, KHÔNG theo `don_vi_id`**)"*

**Về ma trận phân quyền — không dùng làm căn cứ được, và có mốc thời gian chứng minh.** `srs-v3.5.md:1336` ghi cột CG là `CRU*` cho nội dung tư vấn. Nhưng dòng `:1363` cũng ghi cột CG là `CRU*` cho **tư liệu pháp lý** — trong khi BR-AUTH-14 đã chốt chuyên gia **chỉ đọc** tư liệu và *"Chặn mọi thao tác Thêm/Sửa/Xóa/Công khai"*.

Mốc thời gian: dòng ma trận đó được đặt ngày **2026-05-07** (`CHANGELOG-v3-to-v3.5.md:3162` — *"TU_LIEU_PHAP_LY_VV (CRUD CB; **CG soạn**)"*), còn BR-AUTH-14 là **BA chốt 2026-06-03**. Tức ô ma trận có **trước** quyết định của chị gần một tháng và **chưa ai sửa lại**. Ở điểm tư liệu, tỉ lệ là **5 nguồn chọi 1**: quy tắc BR, tệp nhóm, điều kiện chấp nhận, Danh sách UC, và **bản bàn giao** — tất cả đều nói chỉ đọc; chỉ ma trận nói khác. Bản bàn giao ghi nguyên văn: *"Chuyên gia chỉ được xem và tải tư liệu của chính nội dung tư vấn được phân công cho mình… **Chuyên gia không được thêm, sửa, xóa và không được công khai**."*

> **Vì sao mục này giữ quyền Sửa cho chuyên gia, còn mục 5 cắt cả quyền Xem của quản trị viên — dù cùng dùng một tiền đề "không phải tác nhân thì không có phần nào của chức năng"?** Vì ở đây có **bằng chứng dương** trong chính luồng nghiệp vụ: `:231` cán bộ phê duyệt từ chối → *"Gửi thông báo CG: cần bổ sung nội dung"*; `:1162` trạng thái *Đang tư vấn* có nút [Lưu]; `:1166` cho sửa ở trạng thái đó. Nhóm báo cáo không có bằng chứng dương nào tương đương cho quản trị viên.

⇒ Ô `CRU*` của cột CG là **ô chưa được bảo trì**, không phải tuyên bố thiết kế. Ghi chú *"UC147: nội dung tư vấn với CG"* trong mã nguồn bám đúng ô đã lỗi thời này. Riêng chữ `C` (tạo mới) trên nội dung tư vấn thì **không có chức năng nào chống lưng** — không Danh sách UC, không tệp nhóm, không màn hình.

**(1b) Bản bàn giao nói gì? — CÙNG CHIỀU với kết luận, và tự mâu thuẫn ở đúng chỗ đáng chú ý.**

Mục phân quyền của bản `.docx` v3.5 phân vai rành mạch, **không cho chuyên gia tạo hay sửa**:

> *"• Người sử dụng là **CB NV** ở Trung ương, bộ ngành hoặc địa phương được **thêm, sửa**, phân công, hủy và công khai; phạm vi dữ liệu giới hạn theo đơn vị của người sử dụng.*
> *• **Chuyên gia được phân công thực hiện xác nhận nhận việc, từ chối và hoàn thành tư vấn trên chính bản ghi được giao.**"*

Hai điều đáng lưu ý:
- Câu về chuyên gia đã ghi sẵn ràng buộc **"trên chính bản ghi được giao"** — tức đúng cái phạm vi mà phần mềm đang thiếu. Bản bàn giao không sai; phần mềm làm rộng hơn văn bản.
- Nhưng mục quy trình nghiệp vụ của **chính bản v3.5** lại ghi chuyên gia *"soạn thảo văn bản tư vấn pháp luật trên trình soạn thảo của hệ thống"* — tức vẫn có việc soạn nội dung. Hai mục của cùng một bản chọi nhau, đúng như bản gốc.

⇒ Đây là ca **cả hai tài liệu cùng chỉ ra hướng siết theo phạm vi**, chỉ khác là chưa tài liệu nào viết ra ranh giới giữa "soạn nội dung khi đang tư vấn" và "sửa hồ sơ bất kỳ". Đó chính là chỗ phương án dưới đây lấp.

**(2) Đối tác yêu cầu khác bản gốc không?** Điểm này không do đối tác nêu — Dev phát hiện khi rà các chỗ hở cùng kiểu.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** CÓ. Mạng lưới tư vấn là bên ngoài cơ quan; hồ sơ tư vấn chuyên sâu chứa nội dung vướng mắc pháp lý của doanh nghiệp cụ thể. Để một người trong mạng lưới sửa được hồ sơ của doanh nghiệp mà mình không phụ trách là hở dữ liệu giữa các doanh nghiệp qua trung gian là người tư vấn.

**→ Kết luận: siết theo PHẠM VI, không siết phẳng. Chuyên gia được giao KHÔNG được tạo mới; chỉ được sửa bản ghi mà mình là người được giao, và chỉ khi hồ sơ ở trạng thái Đang tư vấn. Dev action: Có · Sửa đặc tả: Có · Sheet: không có phiếu QA nào treo vào điểm này.** ✅ Tự chốt theo cây trọng tài — tầng CSV UC, dùng khuôn BR-AUTH-14 đã chốt.

> Khớp với mục 4 đã chốt: người được giao chỉ có thể là **Chuyên gia**, nên chủ ngữ của quy tắc mới là "Chuyên gia được phân công".

### Phương án xử lý (cập nhật SRS)

Đặt một quy tắc mới cùng họ với BR-AUTH-14, để không phải vá rải rác:

> **Chuyên gia chỉ GHI trên hồ sơ của mình.** Chuyên gia chỉ được **sửa nội dung** của hồ sơ tư vấn chuyên sâu mà mình là người được phân công, và **chỉ khi hồ sơ ở trạng thái Đang tư vấn**. Chặn thao tác Tạo mới và Xóa ở mọi trạng thái. Các thao tác còn lại của họ đi qua nút của luồng (nhận việc, từ chối, hoàn thành).
>
> **Ràng buộc đích danh này CHỈ áp cho thao tác ghi. Quyền XEM giữ nguyên theo đơn vị.**

⚠️ **Vế thứ hai là bắt buộc, không phải chú thích.** Bản gốc đã chốt quyền xem tư vấn chuyên sâu là theo đơn vị, không lọc đích danh:

- `srs-v3.5.md:5490` BR-AUTH-10, cột Ngoại lệ — *"Dữ liệu chung (UC21, UC27, **UC147, UC148**): chỉ Lớp 1"*
- `srs-fr-12-tv-chuyen-sau.md:37` — *"**KHÔNG áp lọc kép BR-AUTH-10** vì TVCS là tài liệu kiến thức nghiệp vụ chia sẻ trong đơn vị, không phải task gán đích danh"* `[BA chốt 2026-05-10]`

Viết quy tắc mới mà không tách rõ hai tầng thì thành **đảo một quyết định BA cũ mà không ai để ý**. Ba bảng bước xử lý *Xem danh sách* `:132`, *Xem chi tiết* `:150`, *Xuất Excel danh sách* `:159` đang lọc theo đơn vị — **giữ nguyên cả ba**, đúng quyết định 2026-05-10.

Áp kèm 4 chỗ:

| Chỗ | Việc |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:140` | bước "Ghi nhận hoặc cập nhật nội dung", bước 1 hiện ghi *"Kiểm tra quyền và phạm vi đơn vị"* — nêu đích danh vai trò như bước phân công ở `:170` đã làm, và tách rõ hai nhánh cán bộ / người được giao |
| `srs-fr-12-tv-chuyen-sau.md:1166` | mục Quy tắc tương tác: ghi rõ ở *Tiếp nhận* người sửa là cán bộ nghiệp vụ, ở *Đang tư vấn* là cán bộ nghiệp vụ **hoặc** người được giao |
| `srs-v3.5.md:1336` | dòng TU_VAN_CHUYEN_SAU: **chỉ sửa cột CG** `CRU*` → `RU*‡` (bỏ quyền Tạo; giữ đọc theo đơn vị; `‡` trỏ quy tắc mới). **Cột TVV giữ `R*`** — mục 4 đã chốt tư vấn viên không nhận việc ở nhóm này nên không có căn cứ cấp thêm quyền ghi |
| `srs-v3.5.md:1363` | dòng TU_LIEU_PHAP_LY_VV: cột CG sửa `CRU*` → `R‡` cho khớp BR-AUTH-14 đã chốt 2026-06-03 — chỗ này đang mâu thuẫn sẵn, không phải phát sinh mới |

**Sáu chỗ nữa phải sửa, nếu không đặc tả tự chọi:**

| Chỗ | Việc |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:97` §Tác nhân · `:34` §Tác nhân chính · `:103` §Điều kiện tiên quyết | ba dòng này hiện chỉ có Cán bộ Nghiệp vụ; chốt cho chuyên gia quyền sửa mà để nguyên là tự chọi |
| `:312` §Postconditions — *"phân quyền dữ liệu theo đơn vị (chỉ xem dữ liệu đơn vị mình)"* | thêm vế ngoại lệ cho thao tác ghi của chuyên gia |
| `:329-335` Điều kiện chấp nhận — 7/7 dòng mở đầu *"Given CB NV…"* | thêm dòng cho chuyên gia sửa nội dung ở trạng thái Đang tư vấn, và dòng phủ định cho hồ sơ không được giao |
| `:317-325` bảng mã lỗi `ERR-TVCS-01`…`07` | thêm mã cho *"chuyên gia sửa hồ sơ không được giao"* và *"chuyên gia bấm tạo mới"* — chặn mà không có câu trả lời là chỗ đơn vị phát triển tự đặt |
| **Dựng bảng quyền mức thao tác cho `TU_VAN_CHUYEN_SAU` — khuôn đã bắt buộc sẵn, đừng đẻ quy tắc rời** | `srs-v3.5.md:1392` ghi *"Mỗi entity có vòng đời workflow **SHALL** định nghĩa permission codes action-level … template cho các entity workflow khác"*, và nhóm Hỏi đáp đã có bảng mẫu (`:1396-1416`). Ràng buộc của mục này (`TVCS_UPDATE`: chỉ Chuyên gia là `chuyen_gia_id`, chỉ ở trạng thái Đang tư vấn) là **đúng loại "Scope constraint"** của bảng đó. Dựng bảng này là đủ; ký hiệu `‡` ở ma trận trỏ về nó. **Không cần cấp mã BR mới, không cần khai ở 4 chỗ** như lượt soạn trước ghi |
| **Doc action** | `.docx` v3.5 hiện ghi chuyên gia *"thực hiện xác nhận nhận việc, từ chối và hoàn thành tư vấn"* — hẹp hơn bản gốc mới, phải bổ sung vế sửa nội dung |

**Rà phạm vi ảnh hưởng — 3 chỗ:**

(a) `srs-v3.5.md:1337` PHIEN_TU_VAN cột CG = `RU*` và `:1338` LICH_SU_TRAO_DOI_TV cột CG = `CRU*` — đây là chỗ làm việc thật của chuyên gia, **giữ quyền ghi** nhưng đổi dấu `*` → `‡` cho khớp ràng buộc theo bản ghi. (Hai cột TVV ở hai dòng này là `R*` và `—`, **không có `C`/`U` nào để giữ** — mục 4 đã chốt.)

(b) Không đụng bảng thao tác mức hành động của nhóm Hỏi đáp — quy tắc mới chỉ áp cho nhóm X.1.

(c) **Ngoại lệ thứ ba của BR-AUTH-08 phải ghi vào chính quy tắc đó.** `srs-v3.5.md:5485` hiện liệt kê hai ngoại lệ — *"Exception: (1) QTHT — không scoped theo đơn vị; (2) MAU_PHAN_HOI — phân quyền kép"*. Không thêm quy tắc mới vào đây thì hai dòng chọi nhau.

### Ba lỗ hổng lộ ra khi rà mục này — nên vá cùng lượt

1. **Trường `ket_qua` — thứ chặn luồng — không có ô nhập nào trong toàn bộ đặc tả.** Bước Hoàn thành `:206` kiểm *"đã có văn bản tư vấn pháp luật (`ket_qua` không rỗng)"*, máy trạng thái `:1522` cũng ghi điều kiện *"Có VB TVPL"*. Nhưng bảng dữ liệu đầu vào của chức năng (16 trường, `:109-124`) **không có `ket_qua`**, và khối "Nội dung tư vấn" trên màn hình `:1157` chỉ có Tiêu đề + Nội dung yêu cầu — đó là **nội dung doanh nghiệp hỏi**, không phải kết quả tư vấn. Trường này chỉ tồn tại ở bảng thực thể `:1327`. **Đây đúng cùng một bệnh với mục 1.**

2. **Bản v3.5 tự mâu thuẫn ở đúng điểm này.** Mục phân quyền chỉ cho Chuyên gia *"xác nhận nhận việc, từ chối và hoàn thành tư vấn trên chính bản ghi được giao"* — không nhắc soạn nội dung. Nhưng mục quy trình nghiệp vụ của **chính bản đó** lại ghi: *"Chuyên gia … **soạn thảo văn bản tư vấn pháp luật trên trình soạn thảo của hệ thống** (tự động lưu bản nháp mỗi 30 giây)"*.

3. **Hai tên gọi sai trong bản gốc, sửa luôn:**
   - `srs-fr-12-tv-chuyen-sau.md:1531` nhắc thực thể `TRAO_DOI_NHAP` — **không có thực thể nào tên vậy**; thực thể thật là `LICH_SU_TRAO_DOI_TV` (`:1368`).
   - `srs-v3.5.md:5490` (BR-AUTH-10) viết *"`YEU_CAU_TU_VAN.chuyen_gia_id`"* — **sai tên bảng**, bảng thật là `TU_VAN_CHUYEN_SAU`.

---

## Ba bổ sung ngoài phương án — BA duyệt giữ lại

✅ **BA chốt 06/08/2026: GIỮ.** Ba việc dưới đây **không nằm trong phương án 7 mục**, phát sinh trong lúc sửa đặc tả vì thiếu chúng thì quyết định đã chốt **không cài đặt được**. Cả ba đụng thực thể dùng chung toàn hệ thống nên ghi riêng ở đây để có dấu vết.

| Bổ sung | Vì sao bắt buộc | Rào để không áp ngược lên nhóm khác |
|---|---|---|
| `THONG_BAO`: `nguoi_nhan_id` Y→N, thêm `email_nguoi_nhan` và `hien_trong_ung_dung`, kèm ràng buộc phải có ít nhất một đường liên hệ | Mục 2 chốt gửi thư cho doanh nghiệp, nhưng bảng này bắt buộc phải có tài khoản — mà doanh nghiệp nhóm X.1 **không có** (*"TVCS không có cổng cho DN"*) | `hien_trong_ung_dung` mặc định `1` nên hành vi các nhóm khác **không đổi** |
| `AUDIT_LOG`: thêm trường `ly_do`, bổ sung `'CANCEL'` và `'ASSIGN'` vào tập giá trị `hanh_dong` | Mục 6 chốt hiện lý do trên khối nhật ký, nhưng bảng này **không có chỗ chứa lý do**, và không có giá trị cho thao tác Hủy | `ly_do` **không bắt buộc**, ghi rõ *"KHÔNG đặt ràng buộc cứng ở đây để tránh áp ngược lên các nhóm đã chốt khác"*. Enum chỉ **nới**, không bỏ giá trị nào |
| `srs-fr-10-quan-tri.md`: bộ lọc "Hành động" ở màn Nhật ký hệ thống liệt đủ 11 giá trị | Hệ quả trực tiếp của việc nới enum — không đồng bộ thì quản trị viên không lọc được hai loại thao tác vừa tách | Chỉ thêm lựa chọn vào bộ lọc, không đổi quyền hay luồng |

**Điểm treo kèm theo:** ba bổ sung này chưa được rà chéo sang **các nhóm FR khác** đang dùng hai thực thể trên. Rà chéo thuộc đợt sau, đã ghi ở bảng Điểm treo.

---

## Việc phải thi hành sau khi chốt

Bảy mục đã chốt sinh ra việc cho bốn bên. **Sửa đặc tả là một đợt riêng, làm sau khi phiếu này được đóng dấu.**

| Bên | Việc | Thuộc mục |
|---|---|---|
| **Dev** | Bổ sung thư điện tử cho các mốc thông báo nhóm tư vấn chuyên sâu | 2 |
| **Dev** | Sau khi chuyên gia từ chối → quay về màn danh sách; đổi câu thông báo thành *"Đã từ chối yêu cầu tư vấn"* | 3 |
| **Dev** | Ẩn màn báo cáo thống kê với vai trò quản trị viên (ẩn, không làm mờ — theo quy ước M-05) | 5 |
| **Dev** | Tách nhãn thao tác Từ chối + hiện dòng lý do trên khối nhật ký hồ sơ | 6 |
| **Dev** | Siết phạm vi sửa nội dung tư vấn: chỉ hồ sơ được giao, chỉ ở trạng thái Đang tư vấn; chặn tạo mới | 7 |
| **BA** | Sửa đặc tả 7 mục (đụng cả tệp nền lẫn tệp nhóm) | tất cả |
| **Bên soạn tài liệu** | Cập nhật bản `.docx` v3.5 theo từng chỗ sửa bản gốc | tất cả |
| **QA** | Chỉnh phiếu `BUG-BCTK-QA01` — câu từ chối phải là câu cho *thao tác*, không phải câu cho *xem* | 5 |

**Trạng thái sheet — người phân tích KHÔNG tự đổi mục nào.** Cả bảy mục đều còn việc ở phía Dev hoặc phía đặc tả, nên để QA/Dev đổi sau khi làm xong:

| Phiếu | Trạng thái | Vì sao |
|---|---|---|
| `QLNDTVVCG_24` | giữ xử lý (đảo từ Pass) | Dev bổ sung thư điện tử |
| `QLNDTVVCG_26` | giữ xử lý | Dev sửa điều hướng + thư điện tử |
| `QLNDTVVCG_OOS_04` | giữ xử lý | Dev làm cải tiến đã duyệt |
| `LKHDG_16` | giữ nguyên (đang Reopen) | Reopen vì lỗi độc lập `BUG-LKHDG-SUA-PHANCONG` |
| 189 · 222 · 226 · 230 · 234 | giữ xử lý | Dev sửa giao diện + câu từ chối |

**Chỉ một ô phản hồi cần điền ngay** — dòng `LKHDG_16`, cột "DEV phản hồi lần 1": *"Xác nhận bản SRS docx đang thiếu thành phần. Sẽ gửi lại bản cập nhật mới nhất khi bàn giao fix bug tuần."* Các mục còn lại là bug thật Dev sửa toàn bộ nên không phản hồi.

---

## Điểm treo chuyển đợt sau

| Nội dung | Phát hiện ở mục | Thuộc bên nào | Trạng thái |
|---|---|---|---|
| Bản trích quy tắc thông báo trong tệp module viết ra một quy tắc khác bản gốc (`srs-fr-12:1626`) — cần rà xem còn tệp module nào trích lệch tương tự | 2 | BA | Mới, chưa rà |
| Ô cột CG trong ma trận phân quyền chưa được bảo trì sau quyết định BR-AUTH-14 (2026-06-03) — cần rà toàn bộ ma trận tìm ô lệch cùng kiểu. **Đã có 2 ca thật:** `TU_LIEU_PHAP_LY_VV` và `TU_VAN_CHUYEN_SAU` cột CG cùng ghi `CRU*` trong khi quy tắc và Danh sách UC đều nói hẹp hơn | 7 | BA | Mới, chưa rà |
| Bảng thành phần màn hình có thể còn chỗ khác chưa cập nhật sau lượt cherry-pick v3.5 (nhóm 08 vừa lộ 2 dòng) — nên quét cả các nhóm cùng lượt | 1 | BA | Mới, chưa rà |
| Chưa xác định được ngày bàn giao và kênh gửi của bản `v3.5` | Bối cảnh chung | Bên soạn tài liệu bàn giao | Đã hỏi, chưa có |
| Toàn bộ chỗ sửa bản gốc ở 7 mục đều sinh một việc tương ứng bên bản bàn giao | tất cả | Bên soạn tài liệu bàn giao | Chờ đợt bàn giao kế tiếp |
| **Bảng thực thể ở tệp nền đang tụt lại so với tệp nhóm — đã thấy ở 2 thực thể, nhiều khả năng còn.** `KE_HOACH_DANH_GIA` (thiếu 2 trường CR, trạng thái 6 vs 8, thừa 1 trường) và `TU_VAN_CHUYEN_SAU` (16 thuộc tính vs 22, thiếu cả `don_vi_id`). Cần rà toàn bộ, vì mọi kết luận dựa trên "bảng dữ liệu nói X" đều phụ thuộc việc đọc đúng bản nào | 1 · 7 | BA | **Mới — ưu tiên cao** |
| **Bản `v3.5` thiếu nhiều thứ so với bản gốc, ở đúng những chỗ đang tranh chấp.** Đã đếm được: 2 ô nhập form kế hoạch đánh giá · điều hướng và câu thông báo sau khi từ chối · nhánh lỗi thiếu lý do · kênh gửi ở các mốc thông báo · cụm "CG/TVV" ở mục phân quyền (trong khi mục quy trình của chính nó vẫn ghi) · **và toàn bộ Phụ lục A (ma trận truy vết) + Phụ lục B (danh mục quy tắc nghiệp vụ)**. Cần rà ngược một lượt bản `v3.5` so với bản gốc trước đợt bàn giao kế tiếp, mỗi mục thiếu khép bằng một trong hai kết luận: bổ sung vào `.docx` hoặc xác nhận cố ý bỏ | 1·2·3·4·6·7 | Bên soạn tài liệu bàn giao | **Mới — ưu tiên cao nhất** |
| Do v3.5 gỡ Phụ lục B, **đối tác đọc bản mới không còn thấy nguyên văn quy tắc phân quyền nào** — mọi giải trình về quyền quản trị viên hay quyền chuyên gia đều không dẫn được trong chính tài liệu đã giao cho họ | 4 · 5 · 7 | Bên soạn tài liệu bàn giao | Mới |
| Trường `ket_qua` (văn bản tư vấn) chặn bước Hoàn thành nhưng **không có ô nhập nào** trong đặc tả — cùng bệnh với mục 1 | 7 | BA | Mới |
| ~~Đặc tả im lặng về việc một cơ quan tự đánh giá chính mình~~ — **BA chốt 06/08: cho phép trùng**, đã ghi vào phương án mục 1 | 1 | — | Khép 06/08 |
| Toàn hệ thống **không có quy ước câu chữ thông báo cho hành vi Từ chối** — chỉ 2 nhóm tự đặt câu riêng. Nên cân nhắc bổ sung vào bảng thông báo dùng chung | 3 | BA | Mới |
| **Lỗi phạm vi của quy tắc thông báo không riêng nhóm X.1 — còn 3 ca cùng hình dạng.** `srs-fr-07-doanh-nghiep.md:386` viện `BR-NOTIF-01` nhưng **FR-V.III không có** trong danh sách phạm vi; `srs-fr-03-dao-tao.md:2248` bảng nhóm ghi **FR-III-19** mà tệp nền không có, ngược lại tệp nền có **FR-III-13** mà bảng nhóm không có. Vá riêng nhóm X.1 là để lại 3 ca | 2 | BA | **Mới — nên gộp một lượt** |
| **Bản trích quy tắc lệch không phải 2 mà ít nhất 4.** Ngoài `srs-v3.5.md:5613` và `srs-fr-12:1626`, còn `srs-fr-08-danh-gia.md:1269` và `srs-fr-05-vu-viec.md:2480` | 2 | BA | Mới |
| **Tệp nền tự chọi về bộ trạng thái kế hoạch đánh giá** — bảng thực thể `srs-v3.5.md:2911` giữ bộ 6 giá trị cũ, còn máy trạng thái C.6 ngay trong cùng tệp (`:6089-6090`) đã là bộ mới. Sửa `:2911` phải đối chiếu C.6 cùng tệp, không phải đối chiếu sang tệp nhóm | 1 | BA | Mới |
| Sơ đồ quan hệ ở tệp nhóm (`srs-fr-08-danh-gia.md:938-947`) đã có `co_quan_duoc_danh_gia_id` nhưng **chưa có `file_dinh_kem`** — áp CR-10 mà chưa áp CR-07 | 1 | BA | Mới |
| Đường quan hệ `srs-v3.5.md:4349` trỏ khóa ngoại `ct_htpl_id` — nếu gỡ trường thừa đó thì phải gỡ cả dòng quan hệ | 1 | BA | Mới |
| Bảng danh sách và bộ lọc đợt đánh giá không có **Cơ quan được đánh giá**, dù đó là chiều tra cứu chính của chức năng Nhận kết quả đánh giá | 1 | BA | Mới |
| **Ba mục 2 · 3 · 6 thi hành trên nền `[GAP-X.1-01]`** — luồng chuyên gia chấp nhận/từ chối vốn không có giao dịch nào trong Danh sách UC (0/188 UC có "Chuyên gia" ở cột Tác nhân). Không phải lỗi, nhưng phiếu dùng Danh sách UC làm trọng tài dứt điểm ở mục 4 · 5 · 7 nên cần nói rõ cho nhất quán | 2 · 3 · 6 | BA | Ghi nhận |
| Phiếu `BUG-BCTK-QA01` đang yêu cầu Dev hiện câu *"Bạn không có quyền xem báo cáo này"* cho tình huống chặn **xuất** — sai bản chất, cần chỉnh phiếu | 5 | QA | Mới, phải báo lại |
| ~~Bản gốc chưa giới hạn số lượng tệp đính kèm mỗi đợt đánh giá~~ — **đã tự khép**: áp khuôn dùng chung đã có sẵn trong bản gốc (*"tối đa 10 file, tổng 100MB, mỗi file 20MB"*), không phải quyết định mới | 1 | — | Khép 06/08 |
| Bản gốc im lặng về **tập cột của tệp xuất** ở nhóm đánh giá, trong khi quyết định 06/08 vừa chốt khuôn tên tệp thành quy ước chung và đã đặc tả tập cột cho nhóm tư vấn chuyên sâu — nên thống nhất một lượt | Phụ lục phiếu LKHDG | BA | Mới, chưa quyết |
| Toàn bộ lượt đo lại tuần 5 chạy trên môi trường phát triển `18.143.165.120.nip.io`, còn đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`. Hai điểm sửa của `QLNDTVVCG_OOS_02/03` cũng chỉ verify ở máy cá nhân và môi trường 120 | Bối cảnh chung | Bên dựng môi trường | Phải xác nhận bản sửa đã lên đúng môi trường đối tác đo |
