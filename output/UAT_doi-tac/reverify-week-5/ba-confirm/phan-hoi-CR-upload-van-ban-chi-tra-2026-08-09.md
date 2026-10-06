# Phiếu chốt — Bổ sung tải lên văn bản kết quả, nhóm Chi trả chi phí

**Ngày:** 09/08/2026 · **Nhóm chức năng:** V.II — Chi trả chi phí tư vấn pháp luật (UC 68–80)
**Nguồn:** đề nghị của đối tác qua bình luận trên tài liệu bàn giao — **ngoài luồng UAT**, không có mã test case, không cập nhật sổ theo dõi.
**Bản chấm chuẩn:** `srs-fr-06-chi-tra.md` · `srs-v3.5.md` · bản bàn giao `HTPLDN-PTYC-CT-v3.5.docx`
**Trạng thái:** ✅ **Đã chốt toàn bộ** (16 mục) · đặc tả **đã sửa xong** 10/08/2026, commit `b067649`, qua 5 vòng nghiệm thu · còn Dev action và Doc action chưa làm · câu (1) còn `[CHỜ BẰNG CHỨNG]`.

---

> **Ghi chú phương pháp:**
> - Căn cứ pháp luật đọc tận bản PDF ký số của Chính phủ, không qua kết quả tìm kiếm.
> - Đặc tả đã sửa được nghiệm thu theo danh sách tiêu chí cố định, giữ nguyên qua cả 5 vòng.

---

## Bổ sung tải lên văn bản kết quả ở luồng Đạt/Không đạt

**Vấn đề:** Khi cán bộ ghi kết quả Đạt / Không đạt trên màn hình chi tiết hồ sơ chi trả, phần mềm chỉ cho chọn kết quả và gõ lý do — không có chỗ tải lên bản văn bản đã ký. Theo quy định hiện hành, kết quả xử lý phải được ban hành thành văn bản của cơ quan có thẩm quyền, có số và ngày. Hồ sơ điện tử không lưu văn bản đó ở đâu, nên khi doanh nghiệp hoặc đoàn kiểm tra hỏi lại thì không tra ra bản đã ban hành.

**Bóc ý con trong yêu cầu:**

| Ý con | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Tải lên văn bản kèm theo ở bước ra kết quả | Không | Phương án xử lý, mục chốt 1 |
| Ghi số và ngày văn bản thành ô riêng | Không | BA chốt **không làm** (mục chốt 3) — số và ngày nằm sẵn trên mặt văn bản |
| Gửi kèm văn bản sang Cổng Dịch vụ công cho doanh nghiệp | Không | BA chốt **Có** (mục chốt 4) |

**(1) Phần mềm đúng bản gốc chưa? — `[CHỜ BẰNG CHỨNG]`.** Bản gốc **không có ô tải tệp nào cho cán bộ** ở nhóm chi trả, nên màn hình thiếu ô tải **không phải sai lệch so với đặc tả**. Hiện trạng phần mềm mới lấy từ lời đối tác — chưa mở môi trường, chưa có ảnh chụp.

**(1b) Bản `.docx` đối tác cầm có nói khác không? — KHÔNG.** Ba bước ra kết quả đều không mô tả trường tệp, ở **cả bản v3.5 lẫn v2.0** → **không phải lệch tài liệu bàn giao**, đây là yêu cầu mới thật.

**(2) Đối tác yêu cầu khác gì?** Thêm chức năng tải văn bản kèm theo tại luồng Đạt/Không đạt. Căn cứ họ dẫn — Văn bản hợp nhất 573/VBHN-BTP — là bản hợp nhất Nghị định 55/2019 với Nghị định 18/2026; **văn bản hợp nhất không sinh nghĩa vụ mới**, nhưng nghĩa vụ trong đó **khác hẳn** bản 2019 mà đặc tả đang dựa vào.

**(3) Có bắt buộc cho luồng nghiệp vụ không? — CÓ.** Điều 9 khoản 1 bản đang có hiệu lực buộc kết quả phải thành **quyết định** của Chủ tịch UBND cấp tỉnh khi đồng ý, hoặc **văn bản thông báo nêu rõ lý do** khi từ chối; thể thức bắt buộc có số, ngày, chữ ký, dấu theo Nghị định 30/2020.

#### Căn cứ chi tiết

**Pháp luật.** Nghị định 18/2026/NĐ-CP Điều 12 thay toàn bộ Điều 9 Nghị định 55/2019, hiệu lực 15/01/2026. Khoản 1:

> *"…Trong thời hạn 10 ngày làm việc kể từ ngày nhận được hồ sơ hợp lệ, Sở Tư pháp thẩm định, trình Chủ tịch Ủy ban nhân dân cấp tỉnh xem xét, **quyết định** hỗ trợ chi phí tư vấn pháp luật… Trường hợp xét thấy… thì Chủ tịch Ủy ban nhân dân cấp tỉnh từ chối hỗ trợ chi phí tư vấn, **có văn bản thông báo và nêu rõ lý do**."*

Thể thức bắt buộc của văn bản hành chính — Nghị định 30/2020 Điều 8 khoản 2: *"c) **Số, ký hiệu của văn bản**; d) **Địa danh và thời gian ban hành văn bản**; g) Chức vụ, họ tên và **chữ ký** của người có thẩm quyền; h) **Dấu, chữ ký số** của cơ quan, tổ chức"*.

Quyết định 523/QĐ-BTP (30/01/2026) công bố thủ tục hành chính: kết quả giải quyết là **quyết định hỗ trợ** hoặc **văn bản trả lời trường hợp không hỗ trợ**.

**Đặc tả hiện tại không có chức năng này.**

- `srs-fr-06-chi-tra.md:1136` — thành phần tệp duy nhất của màn hình chi tiết là #37: *"File đính kèm | C15 readonly | … | Xem / Tải"*.
- `:327-330` · `:688-691` · `:841-844` — Inputs của bước Kiểm tra, Thẩm định, Phê duyệt: mỗi mục 4 trường, không trường nào là tệp.
- `:1082` và `:1158` — *"Nguồn duy nhất: DVC qua LGSP — CB NV KHÔNG nhập tay hồ sơ chi trả"*.
- Mọi tệp trong nhóm đều do doanh nghiệp nộp qua Cổng Dịch vụ công, hoặc chỉ đọc.
- `PHE_DUYET_CHI_TRA` (`:1369-1379`) không có trường lưu văn bản.

**Tài liệu bàn giao cũng không có** — mục 4.6.4.2.2, 4.6.10.2.2, 4.6.13.2.2 đều không mô tả trường tệp, ở cả bản v3.5 lẫn v2.0. Đây là yêu cầu mới, **không phải lệch tài liệu bàn giao**.

**Ngược chiều cần lưu ý.** Ma trận phân quyền `srs-v3.5.md:1324` cho cán bộ nghiệp vụ quyền `CRUD*` trên hồ sơ chi trả, và ghi chú `◇` (`:1398`) nói tệp đính kèm kế thừa quyền thực thể cha — tức tầng phân quyền **đã cho phép** cán bộ tạo tệp, chỉ tầng đặc tả chức năng và màn hình cấm.

⚠️ **Chưa kiểm chứng hiện trạng phần mềm.** Việc "trên hệ thống chưa có" hiện lấy từ lời đối tác, chưa mở môi trường, chưa có ảnh chụp — xem điểm treo 5.

**→ Kết luận: đề nghị chính đáng, phải làm — đặc tả thiếu so với quy định pháp luật. Bổ sung chỗ tải lên văn bản kết quả tại bước Kiểm tra (nhánh Không đạt) và bước Phê duyệt (nhánh Duyệt). Việc thiếu chức năng này KHÔNG phải sai lệch so với đặc tả — cả hai bản tài liệu đều không quy định, Dev làm đúng thứ được giao. Dev action: Có (chưa làm) · Sửa đặc tả: Có (XONG 10/08, commit `b067649`) · Doc action: Có (chưa làm) · Sheet: không áp dụng — ngoài luồng UAT.**

⚠️ Câu (1) còn `[CHỜ BẰNG CHỨNG]` — cần ảnh chụp môi trường.

> **Phản hồi gửi đối tác:** BA tự gửi.

### Phương án xử lý (cập nhật SRS) — **ĐÃ CHỐT**

Bổ sung chức năng cho cán bộ **tải lên văn bản kết quả** trên màn hình chi tiết hồ sơ chi trả.

| # | Nội dung | Chốt |
|---|---|---|
| 1 | Vị trí đặt ô tải | **Hai chỗ:** bước Kiểm tra khi kết quả **Không đạt**, và bước **Phê duyệt**. Bước Thẩm định và bước Từ chối thanh toán giữ nguyên |
| 2 | Tệp bắt buộc hay tuỳ chọn | **Bắt buộc** — chặn nút xác nhận khi chưa đính kèm. Áp cho hồ sơ phát sinh từ ngày triển khai, không áp ngược hồ sơ cũ |
| 3 | Ô số và ngày văn bản | **Không thêm** — số và ngày đã nằm trên mặt văn bản |
| 4 | Gửi văn bản kèm sang Cổng Dịch vụ công cho doanh nghiệp | **Có** |
| 5 | Kiểm chữ ký số của tệp tải lên | **Không** — chỉ quét mã độc |
| 6 | Nhánh hệ thống tự từ chối khi quá hạn bổ sung | **Không cần văn bản.** Ghi một câu giải thích vào đặc tả |
| 7 | Câu quy tắc *"cán bộ không nhập tay hồ sơ chi trả"* | **Sửa** thành *"cấm nhập tay giấy tờ của doanh nghiệp; văn bản do cơ quan ban hành thì cán bộ được tải lên"* |
| 8 | Gửi kèm văn bản cho tư vấn viên | **Không** — bên thụ hưởng là doanh nghiệp; không có quy định phải giao quyết định cho tư vấn viên, và thủ tục cũ có tư vấn viên ký xác nhận đã bị bãi bỏ |
| 9 | Ô tải ở bước từ chối thanh toán sau khi đã duyệt | **Không** — bước này thuộc phần thủ tục đã bãi bỏ; xem lại cùng lượt rà nhóm. Ghi rõ lý do bỏ qua vào đặc tả |
| 10 | Xem và tải văn bản đã tải lên | **Có** — dùng lại vùng "File đính kèm" sẵn có của màn hình chi tiết. Cán bộ nghiệp vụ và cán bộ phê duyệt xem/tải được; doanh nghiệp xem tại Cổng Dịch vụ công; tư vấn viên không. **Tách nhóm hiển thị:** văn bản của cơ quan để riêng, không trộn với giấy tờ doanh nghiệp nộp |
| 11 | Sửa hoặc xoá tệp sau khi đã gửi | **Khoá** — không cho xoá, không cho thay. Tải nhầm thì ban hành văn bản mới, không sửa bản cũ |
| 12 | Rà lại nhóm chi trả theo Điều 9 hiện hành | **Treo lại**, mở việc riêng — xem điểm treo 1 |

#### Bốn điểm phát sinh sau lượt kiểm định — đã chốt 09/08/2026

| # | Điểm | Chốt |
|---|---|---|
| 13 | **Ràng buộc tệp** | **1 tệp · PDF, DOC, DOCX, JPG, PNG · tối đa 20MB.** Định dạng lấy nguyên bộ đang dùng trong chính nhóm chi trả (`:565`, `:975`) — bỏ bảng tính vì vô nghĩa với văn bản hành chính, giữ ảnh vì cán bộ hay chụp lại bản giấy. Dung lượng theo mức áp đảo toàn hệ thống, đã chốt cứng ở tầng dữ liệu bằng `CHECK kich_thuoc ≤ 20MB` (`srs-v3.5.md:3402`). Một tệp vì một quyết định là một văn bản. ⚠️ **Ghi rõ vào đặc tả:** mức 20MB **khác** mức 10MB của tệp đến qua Cổng Dịch vụ công trên cùng màn hình — 10MB là ràng buộc của kênh Cổng, 20MB là ràng buộc của phần mềm; không viết ra thì lượt kiểm thử sau sẽ log là lỗi |
| 14 | **Nhánh "Từ chối — trả về thẩm định"** của bước Phê duyệt | **Không bắt buộc tệp.** FR-V.II-12 bước 4 (`:851`) là **trả về nội bộ** cho cán bộ nghiệp vụ sửa, không phải từ chối cuối, không có văn bản nào của cơ quan. Tệp chỉ bắt buộc ở nhánh **Duyệt** |
| 15 | **Nhánh "Cần bổ sung"** của bước Kiểm tra | **Không bắt buộc tệp** — hồ sơ chưa kết thúc, chỉ yêu cầu doanh nghiệp bổ sung |
| 16 | **Nhánh "bổ sung 3 lần không đạt"** (BR-EC-15) — hệ thống lật thẳng sang Từ chối ngay trong thao tác của cán bộ | **Miễn tệp**, xử như nhánh quá hạn. Ghi rõ lý do vào đặc tả: cán bộ chọn "Yêu cầu bổ sung" nên không lường trước hồ sơ bị chấm dứt, không thể chuẩn bị văn bản tại chỗ |

#### Bên nào phải làm gì

| Trường | Giá trị | Tình trạng |
|---|---|---|
| **Dev action** | **Có** — bổ sung ô tải văn bản ở bước Kiểm tra (nhánh Không đạt) và bước Phê duyệt (nhánh Duyệt); chặn nút xác nhận khi thiếu tệp; quét mã độc; khoá sửa/xoá sau khi hồ sơ chuyển trạng thái; gửi tệp kèm sang Cổng Dịch vụ công ở cả hai bước | ⏳ **Chưa làm** — chờ Dev, làm theo đặc tả đã cập nhật |
| **Sửa đặc tả** | **Có** — `srs-fr-06-chi-tra.md` và `srs-v3.5.md` | ✅ **XONG 10/08/2026** — commit `b067649`, đã qua 5 vòng nghiệm thu (30/30 Phần I · 6/6 Phần II) |
| **Doc action** | **Có** — bản bàn giao `HTPLDN-PTYC-CT-v3.5.docx`: mục 4.6.4.2.2 (3→4 trường) · 4.6.4.2.3 trường hợp 3 · 4.6.13.2.2 (2→3 trường) · 4.6.13.2.3 · 4.6.5.2 nội dung gửi đi · 4.6.2.2.2 dòng Tài liệu đính kèm · §4.6.15.1 câu quy tắc · §3.6.2 bước 4 và bước 8. **Chưa có mục tương ứng, phải thêm mới:** quy tắc quét mã độc cho tệp cán bộ, và quy tắc khoá sửa/xoá | ⏳ **Chưa làm** — bên soạn tài liệu bàn giao, ở bản kế tiếp |
| **Sheet theo dõi** | **Không áp dụng** — đề nghị đến ngoài luồng UAT, không có mã test case. Nhóm chi trả cũng chưa có test case nào trong sổ | — |
| **Phản hồi đối tác** | BA tự gửi | ⏳ Chưa gửi |

---

#### Chỗ đã sửa — commit `b067649`, 10/08/2026

**Đặc tả chức năng** (`srs-fr-06-chi-tra.md`)

| Chỗ | Đã làm gì |
|---|---|
| FR-V.II-03 — chỉ nhánh Không đạt | Inputs 4 → **5** trường · Processing 8 → **9** bước (thêm bước kiểm tệp, quét mã độc, lưu kho) · Error Handling 2 → **4** mã (`ERR-CT-KT-03` + dùng lại `ERR-FILE-02`) · điều kiện chấp nhận 3 → **5**, nêu rõ thiếu tệp thì không chuyển trạng thái · ghi chú miễn tệp cho nhánh Cần bổ sung và hai nhánh tự động |
| FR-V.II-12 — chỉ nhánh Duyệt | Inputs 4 → **5** · Processing 7 → **8** · Error Handling 3 → **6** mã (`ERR-CT-PD-04`, `ERR-CT-LGSP-03`, `ERR-FILE-02`) · điều kiện chấp nhận nêu rõ nhánh trả về thẩm định không đòi tệp |
| Kênh gửi ở bước Phê duyệt | **Mở luồng gửi ra mới** tại FR-V.II-12 bước 7, đối xứng FR-V.II-04 — vì FR-V.II-04 chỉ chạy sau bước Kiểm tra nên không phủ được bước Phê duyệt |
| FR-V.II-04 | Processing 6 → **7** bước · Outputs 2 → **3** trường · ghi rõ tệp chỉ đi kèm ở nhánh Không đạt |
| Xử lý khi gửi thất bại | **Giữ nguyên bản gốc** — ghi log + cảnh báo CB NV. Không thêm thao tác gửi lại `[BA chốt 10/08: không có trong phiếu thì không đưa vào]` |
| Ràng buộc tệp | 1 tệp · PDF/DOC/DOCX/JPG/PNG · ≤ 20MB, kèm câu giải thích vì sao khác mức 10MB của kênh Cổng Dịch vụ công |

**Màn hình và máy trạng thái**

| Chỗ | Đã làm gì |
|---|---|
| Màn hình chi tiết hồ sơ | 37 → **39 thành phần**, đánh số lại từ #13; thêm ô tải ở section-3 và section-6 |
| Vùng File đính kèm (nay #39) | **Chia 2 nhóm** — giấy tờ doanh nghiệp nộp giữ chú thích mã tham chiếu Cổng; văn bản của cơ quan không có mã đó nên chú thích hiện người tải và thời điểm tải |
| Máy trạng thái — **4 bản** | Siết điều kiện 2 cạnh ở cả bản tệp nhóm và bản tệp nền; đồng bộ thêm khối chữ ở phần Tổng quan và bảng chuyển trạng thái trên màn hình |
| Tham chiếu chéo | `SCR-V.II-02 #34` → **`#36`** ở **cả hai** tệp |

**Quy ước dùng chung — viết thành ngoại lệ tường minh**

| Chỗ | Đã làm gì |
|---|---|
| Quét mã độc | Tách **hai vế**: tệp qua Cổng Dịch vụ công giữ cơ chế cũ (Cổng quét, phần mềm không quét lại); tệp cán bộ tải lên áp đủ quy ước chung, dùng lại `ERR-FILE-02` và câu chuẩn, nêu rõ hành vi chờ |
| Khoá sửa/xoá | Viết thành ngoại lệ của DG-09; neo BR-FLOW-03 và **mở rộng sang trạng thái Từ chối** |
| Xoá theo dây chuyền | Chặn ở **tầng thao tác**, không cascade với văn bản kết quả |
| Câu quy tắc nguồn dữ liệu | Nới ở **3 chỗ nguyên văn**; viết lại lập luận ở chỗ viện dẫn tại FR-V.II-14 để không hụt vế |
| Quyết định A′ | **Giữ kết luận**, đổi căn cứ sang vế còn hiệu lực; sửa kèm ở FR-V.II-10 và bảng truy vết tệp nền |

**Dữ liệu và phân quyền** (`srs-v3.5.md`)

| Chỗ | Đã làm gì |
|---|---|
| Tệp đính kèm | `loai_file` thêm giá trị cho văn bản kết quả **kèm ràng buộc kiểm tra giá trị**; ghi rõ mã tham chiếu Cổng và mã băm để trống với tệp tải trực tiếp |
| Bảng tổng quan thực thể | 2 → **4 FR** ghi bản ghi tệp cho hồ sơ chi trả |
| Ma trận phân quyền | Cán bộ phê duyệt thêm quyền tạo (ký hiệu `⌂` mới, có chú thích); quyền xoá kèm điều kiện trạng thái |
| Mốc "đã gửi" | **Không cần trường mới** — điều kiện khoá neo vào trạng thái hồ sơ |

**Không đụng bảng thuộc tính `HO_SO_CHI_TRA`.**

**Tài liệu bàn giao — chưa làm, thuộc bên soạn tài liệu:** §4.6.4.2.2 (3 → 4 trường) · §4.6.4.2.3 trường hợp 3 · §4.6.13.2.2 (2 → 3 trường) · §4.6.13.2.3 · §4.6.5.2 nội dung gửi đi · §4.6.2.2.2 dòng Tài liệu đính kèm · §4.6.15.1 câu quy tắc · §3.6.2 bước 4 và bước 8. **Chưa có mục tương ứng, phải thêm mới:** quy tắc quét mã độc cho tệp cán bộ và quy tắc khoá sửa/xoá.


## Điểm treo chuyển đợt sau

| # | Nội dung | Bên chịu | Trạng thái |
|---|---|---|---|
| 1 | 🔴 **Đặc tả nhóm chi trả đang dựng trên bản Điều 9 đã hết hiệu lực.** Quy định hiện hành chỉ còn **một** thủ tục (đã bãi bỏ hồ sơ đề nghị thanh toán), nộp tại Trung tâm phục vụ hành chính công tỉnh hoặc Cổng Dịch vụ công quốc gia, do **Sở Tư pháp thẩm định — Chủ tịch UBND cấp tỉnh quyết định**. Đặc tả đang mô hình hoá hai bước và cơ quan cấp bộ; FR-V.II-07 và điều kiện tiền đề `:557` dựa trên khoản đã bãi bỏ. Có điều khoản chuyển tiếp: hồ sơ tiếp nhận trước 15/01/2026 vẫn theo quy định cũ | BA + CĐT | Treo lại, mở việc riêng |
| 2 | Thẩm quyền ký văn bản: 4 trong 5 đường đóng hồ sơ do cán bộ nghiệp vụ một mình quyết, trong khi luật giao quyền quyết định cho Chủ tịch UBND cấp tỉnh | BA | Treo cùng điểm 1 |
| 3 | Danh mục kiểm tra hồ sơ vẫn tick Giấy chứng nhận đăng ký kinh doanh · Tờ khai quy mô · Hợp đồng tư vấn — hồ sơ hiện hành chỉ còn **2 giấy tờ**; việc tự xác định quy mô nay nằm trong Mẫu 01 mục I.8 | BA | Chờ chốt |
| 4 | Mốc 10 ngày làm việc nay tính từ *"ngày nhận được hồ sơ hợp lệ"*, đặc tả tính từ ngày nộp | BA | Chờ chốt |
| 5 | Chưa kiểm chứng hiện trạng phần mềm — cần đường dẫn môi trường đối tác đang dùng và tài khoản cán bộ nghiệp vụ, cán bộ phê duyệt | Bên dựng môi trường | Chờ cấp truy cập |
| 5b | ✅ **ĐÃ ĐÓNG `[BA chốt 2026-08-10]`.** Trong lúc sửa đặc tả, người soạn đã tự thêm thao tác **Gửi lại** khi gửi văn bản sang Cổng Dịch vụ công thất bại — **việc này không nằm trong 16 mục chốt của phiếu**, đến từ một phát hiện của lớp soi chứ không phải quyết định của BA. BA chốt **gỡ bỏ**: giữ nguyên hành vi có sẵn là ghi log + cảnh báo cán bộ. Gỡ xong thì nhu cầu lưu mốc "đã gửi" cũng không còn — điều kiện khoá sửa/xoá vốn đã neo vào trạng thái hồ sơ | — | Đã đóng |
| 6 | Hạn xử lý lệch hai bản: tệp nhóm ghi 10 ngày làm việc (`:1310`), tệp nền ghi 15 ngày (§3.4.3.5 + seed `:2346`). Luật là 10 ngày làm việc cho toàn bộ thủ tục | BA | Chờ chốt |
| 7 | Hai tệp trỏ nguồn vòng tròn cho thực thể `HO_SO_CHI_TRA`: tệp nền ghi nguồn là tệp nhóm (`:1965`), tệp nhóm ghi nguồn là tệp nền (`:1170`) | BA | Chờ chốt |
| 8 | Tệp nền có `ket_qua_danh_gia` và `ket_qua_tham_dinh`, tệp nhóm thiếu — mà `ket_qua_tham_dinh` là điều kiện chuyển sang Chờ phê duyệt | BA | Chờ chốt |
| 9 | `FR-V.II-CROSS-01` (job tự từ chối khi quá hạn bổ sung) chưa có mục đặc tả nào. Nhánh "bổ sung 3 lần không đạt" không có bước xử lý trong Processing FR-V.II-03 | BA | Chờ chốt |
| 10 | `SCR-V.II-02 #22` cho kết quả thẩm định chỉ 2 lựa chọn, trong khi FR-V.II-09 và `.docx` §4.6.10.2.2 đều 3 lựa chọn | BA | Chờ chốt |
| 11 | FR-V.II-01 khai `file_dinh_kem` ở Inputs nhưng Processing 9 bước không có bước nào lưu tệp | BA | Chờ chốt |
| 12 | Khoản 4 Điều 9 hiện hành: trong 15 ngày làm việc kể từ ngày thanh toán, Sở Tư pháp gửi văn bản tư vấn đã bỏ bí mật kinh doanh cho Bộ Tư pháp và Bộ Tài chính. Chưa rà đặc tả có nghĩa vụ này chưa | BA | Cần rà |
| 13 | `.docx` mâu thuẫn nội tại: bảng quy trình bước 5b ghi doanh nghiệp gửi đề nghị thanh toán khi hồ sơ ở *"Đang thẩm định"*, §4.6.8.1 ghi *"Đã duyệt"* | Bên soạn tài liệu | Chờ xử |
| 14 | Hai tham chiếu chết: **F-36** được viện dẫn 3 nơi và **EC-FILE-01** 5 nơi, không nơi nào định nghĩa | BA | Chờ chốt |
| 15 | Hai mã lỗi mỗi mã mang **hai nghĩa**: `ERR-FILE-01` (hết hạn mức lưu trữ ‖ vượt dung lượng tệp), `ERR-FILE-03` (timeout tải lên ‖ vượt số tệp) | BA | Chờ chốt |
| 16 | **9 biến thể câu thông báo mã độc / 8 mã lỗi** cho cùng một tình huống; `ERR-BM-07` chưa có câu thông báo | BA | Chờ chốt |
| 17 | **5 ô tải tệp không có ràng buộc nào** (nhóm Quản trị 2 · Hợp đồng tư vấn 2 · Chương trình HTPLDN 1); độ dài tên tệp, tên trùng, tệp rỗng chỉ được quy định ở nhóm Hỏi đáp | BA | Chờ chốt |
| 18 | `loai_file` **trùng tên khác nghĩa**: bản nền dùng làm phân loại nghiệp vụ, nhóm Tư vấn chuyên sâu dùng làm kiểu MIME — trong khi thực thể đã có cột riêng cho MIME | BA | Chờ chốt |
| 19 | **DG-07** (*"giữ nguyên tên tệp gốc, không tự sinh tên khác"*) chọi thiết kế dữ liệu có cột tên lưu trữ dạng mã định danh, và chọi nhóm Hỏi đáp vốn tự đổi tên khi trùng | BA | Chờ chốt |
| 20 | Màu nhãn trạng thái **lệch 6/10** giữa bảng máy trạng thái và bảng trên màn hình; riêng Đã duyệt và Đã thanh toán bị **đảo màu** cho nhau | BA | Chờ chốt |
| 21 | Thời gian thử lại khi gửi sang Cổng Dịch vụ công lệch: nhóm chi trả ghi *"3 lần, mỗi lần 30 giây"*, quy ước chung ghi *"3 lần, lùi dần 1s → 2s → 4s"* | BA | Chờ chốt |
| 21b | **Hành vi sau khi thử lại thất bại cũng lệch** (có sẵn từ trước, lượt sửa 09/08 không đụng): quy ước chung BR-RETRY-01 buộc *"ghi audit `LGSP_RETRY_FAILED` + đẩy vào hàng đợi `manual_review_queue` cho QTHT + gửi thông báo QTHT"*, trong khi nhóm chi trả chỉ ghi *"ghi log + cảnh báo CB NV"*. Hai bên khác cả **người nhận** lẫn **cơ chế xử lý tiếp** | BA | Chờ chốt |
| 22 | Cấu hình hạn bổ sung mang **hai tên khác nhau** ở hai bản máy trạng thái, trỏ hai bản ghi cấu hình khác nhau | BA | Chờ chốt |
| 22b | Hai bản máy trạng thái lệch **9 ô ở cột tham chiếu** (có sẵn từ trước lượt sửa 09/08): `BR-FLOW-04` có ở bản nền, trống ở bản tệp nhóm tại 3 cạnh từ chối · `BR-EC-15` tương tự tại cạnh yêu cầu bổ sung · nhãn `[GAP-V.II-01/02/03]` chỉ có ở bản tệp nhóm · `BR-CALC-03` chỉ có ở bản nền. Lượt sửa 09/08 **không tạo thêm lệch nào** — lệch duy nhất phát sinh (`BR-RETRY-01`) đã gỡ trong cùng lượt | BA | Chờ chốt |
| 23 | Tệp chỉ gắn được vào hồ sơ, **không gắn được vào lượt phê duyệt** — thực thể lịch sử phê duyệt là quan hệ nhiều-một nên khi ban hành văn bản mới sẽ có nhiều tệp cùng nhóm mà không chỉ ra được bản đang hiệu lực | BA | Chờ chốt |
