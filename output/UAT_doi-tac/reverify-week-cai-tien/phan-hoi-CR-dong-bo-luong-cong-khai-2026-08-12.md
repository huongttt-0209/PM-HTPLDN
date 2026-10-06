# Phiếu phân tích — Đồng bộ luồng Công khai lên Cổng và bổ sung Ảnh đại diện cho Chương trình HTPLDN

**Ngày:** 12/08/2026 · **Nhóm chức năng:** liên nhóm (II Hỏi đáp · III Đào tạo · IV Mạng lưới TVV · V.I Vụ việc · VII Biểu mẫu · X.1 Tư vấn chuyên sâu · X.2 Tư vấn nhanh · XI CT HTPLDN · XII API)
**Nguồn:** hai đề nghị của đối tác qua bình luận trên tài liệu bàn giao (Nguyễn Quốc Bảo, 05/08/2026) — **ngoài luồng UAT**, không có mã test case, không cập nhật sổ theo dõi.
**Bản chấm chuẩn:** `srs-v3.5.md` · `srs-fr-02` · `srs-fr-03` · `srs-fr-04` · `srs-fr-05` · `srs-fr-09` · `srs-fr-12` · `srs-fr-13` · `srs-fr-15` · `srs-fr-16` · bản bàn giao `HTPLDN-PTYC-CT-v3.5.docx`
**Trạng thái:** Mục 1 và Mục 2 **✅ BA duyệt 12/08/2026**; toàn bộ phần bổ sung sinh ra từ ba lượt kiểm định **✅ BA duyệt lại 13/08/2026**. Phiếu đã khép, trừ **một điểm treo còn CHỜ BA CHỐT** — chỗ đặt ô công khai của Tư vấn viên (điểm treo 1). **Đặc tả đã sửa xong 13/08/2026** — 10 tệp trong `_bmad-output/planning-artifacts/srs-v3.5/`, ghi tại `CHANGELOG-v3-to-v3.5.md` mục `CR-CK`, nghiệm thu **HỘI TỤ vòng 6** theo danh sách tiêu chí cố định `nghiem-thu-tieu-chi-cong-khai-2026-08-13.md`. Còn **Dev action** và **Doc action** chưa làm.

---

## Thay đổi kể từ lượt duyệt gần nhất

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| Mục 1 | **(a) Kết luận đã đổi — đọc kỹ.** Phạm vi nhóm ô chốt lại còn 9 đối tượng nhập ở form, 3 đối tượng nhập ở nhóm ô trên màn chi tiết. Tư vấn viên và Tổ chức tư vấn chuyển từ nhóm chi tiết sang nhóm form | Có — đã duyệt 12/08 |
| Mục 1 | **(b) Kết luận giữ, phần việc phình ra.** Bổ sung việc vá cho Tổ chức tư vấn: đặc tả nghiệp vụ Quản lý Tổ chức tư vấn thiếu hẳn bước Chỉnh sửa | Không |
| Mục 1 | **(b) Kết luận giữ, phần việc phình ra — **✅ đã duyệt lại 13/08/2026**.** Vòng soi 1 thêm việc 7 (hủy công khai không xoá nội dung công khai) và việc 8 (Ảnh đại diện sửa được ở mọi trạng thái trừ Hủy) | Không |
| Mục 1 | **(a) Có một điểm đổi — đọc kỹ · ✅ đã duyệt lại 13/08/2026.** Vòng soi 2 **thu hẹp việc 1**: Ảnh đại diện chỉ đặt ở form với 9 đối tượng nhóm form và Chương trình HTPLDN; ba đối tượng nhóm chi tiết thì ảnh nằm luôn trong nhóm ô Nội dung công khai, để bộ thông tin công khai của một hồ sơ không bị tách hai chỗ | Không đổi kết luận, đổi phạm vi việc 1 và việc 3 |
| Mục 1 | **(b) Phần việc phình ra — **✅ đã duyệt lại 13/08/2026**.** Vòng soi 2 thêm việc 9 (nâng quyền cán bộ phê duyệt trên Hỏi đáp), việc 10 (chỉ rõ form đặt ô của Tư vấn viên), việc 11 (bỏ trường khỏi §Inputs của 4 nghiệp vụ Công khai), việc 12 (chốt ràng buộc độ dài và số tệp) | Không |
| Mục 2 | **(a) Kết luận đã đổi — đọc kỹ · ✅ đã duyệt lại 13/08/2026.** Phương án viết lại theo khuôn đã chốt ở Mục 1: Chương trình HTPLDN xếp vào nhóm nhập ở form; số chỗ sửa 8 → **10**; thêm hai chỗ cố ý không làm kèm lý do | Không đổi phần "phải làm", chỉ mở rộng phạm vi |
| Mục 1 | **(b) Phần việc phình ra — **✅ đã duyệt lại 13/08/2026**.** Lượt soi 4 tầng bổ sung danh sách chỗ sửa đã định vị (9 chỗ ở đặc tả màn và quy tắc tương tác), khoanh Doc action còn **19 mục**, và chốt hai điều phải giữ khi bỏ ô nhập khỏi hộp thoại công khai | Không |
| Mục 2 | **(b) Phần việc phình ra — **✅ đã duyệt lại 13/08/2026**.** Soi lại vòng 1 trên bản mới: thêm việc 10 (bổ sung ngoại lệ vào Quy tắc tương tác của màn, nếu không thì mở quyền sửa ảnh mà màn hình không có chỗ bấm); việc 6 và 7 nói rõ hơn; sửa lại một dòng trong bảng rà vốn kết luận sai là "không chọi". Số chỗ sửa 10 → **11** | Không |

---

> **Ghi chú phương pháp:**
> - Yêu cầu 1 rơi đúng vào **điểm treo đã ghi sổ** tại `srs-v3.5.md:1031` — *"chuẩn hoá chỗ đặt ô nhập cho cả 12 entity. Cần BA quyết ở đợt sau"*. Đây là "đợt sau" đó, không phải đảo chốt 31/07.
> - Hiện trạng phần mềm chỉ lấy từ bình luận của đối tác — chưa mở môi trường, chưa có ảnh chụp. Mọi câu về hiện trạng đều đánh dấu `[CHỜ BẰNG CHỨNG]`.

**Bối cảnh nghiệp vụ (nêu một lần, dùng chung hai mục):** Cổng Pháp luật Quốc gia hiển thị cho doanh nghiệp ngoài hệ thống 12 nhóm dữ liệu do cán bộ đăng lên. Mỗi bản ghi đăng lên mang thêm một bộ **thông tin chuyên trang** — ảnh đại diện, mô tả công khai, tệp đính kèm công khai, thời gian đăng tải, công tắc công khai — theo yêu cầu thay đổi của đối tác ngày 16/04/2026. Cổng **tự kéo** dữ liệu định kỳ; phần mềm chỉ đặt cờ, không gọi sang Cổng.

---

## Mục 1 — Đồng bộ luồng Công khai: nhấn Công khai chỉ còn hộp thoại xác nhận

**Vấn đề:** Cùng một thao tác "Công khai lên Cổng", mỗi màn hình lại làm một kiểu: có màn bấm xong hiện ngay hộp thoại đòi nhập thêm mô tả, ảnh, tệp; có màn mở lại thông tin bản ghi và vẫn cho sửa; có màn chỉ hỏi xác nhận rồi đăng. Cán bộ phải học từng màn một, và đến bước công khai mới biết mình còn thiếu nội dung phải soạn. Đối tác đề nghị thống nhất: bấm Công khai chỉ hỏi xác nhận, còn mọi thông tin cần đăng thì nhập ngay từ lúc lập hồ sơ.

**Bóc ý con trong yêu cầu:**

| Ý con | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| a. Bấm Công khai chỉ hiện hộp thoại xác nhận, không nhập nội dung tại đó | Không đồng nhất — **6/12** đối tượng vẫn nhập tại bước công khai | Phương án xử lý, việc 4 |
| b. Không sinh bộ thông tin công khai riêng, chỉ công khai đúng thông tin bản ghi | Bản gốc **có** trường mô tả công khai riêng ở cả 12 đối tượng, do Chủ đầu tư chốt | Kết luận — **không làm**, căn cứ ở (3) |
| c. Chuyển các trường đang chỉ có ở bước Công khai về form Thông tin ban đầu | Không — 6 đối tượng đang đặt ở bước công khai | Phương án xử lý, việc 1–3 |
| d. Biểu mẫu hợp đồng: form tạo mới phải có Ảnh đại diện và Tệp đính kèm công khai, không được bỏ | Bản gốc **có**, đặt ở form nhưng ẩn cho tới khi bật công tắc Công khai | Phương án xử lý, việc 1 và 2 |

**(1) Phần mềm đúng bản gốc chưa? — Bản gốc tự nó không đồng nhất; hiện trạng phần mềm `[CHỜ BẰNG CHỨNG]`.** `srs-v3.5.md:1025` xếp 12 đối tượng công khai thành **bốn kiểu** theo chỗ đặt ô nhập, và `:1031` ghi nhận việc chuẩn hoá là điểm lệch còn tồn. Riêng Biểu mẫu, bản gốc đặt ba ô công khai ở form thêm/sửa với điều kiện hiển thị *"khi Switch ON"* (`srs-fr-09-bieu-mau.md:668-671`) — đúng cái đối tác mô tả là *"chỉ khi nhấn Công khai mới hiện"*.

**(1b) Bản `.docx` đối tác cầm có nói khác không? — KHÔNG.** `HTPLDN-PTYC-CT-v3.5.docx` §4.9.4.2.2 liệt kê Ảnh đại diện, Mô tả công khai, Tệp đính kèm công khai ngay trong bảng *"Mô tả thông tin trên màn hình"* của màn Quản lý Biểu mẫu, không đặt ở hộp thoại riêng — trùng bản gốc. **Không phải lệch tài liệu bàn giao.**

**(2) Đối tác yêu cầu khác gì?** Một khuôn duy nhất cho cả 12 đối tượng: mọi ô nội dung chuyên trang nằm ở form thêm/sửa, nút Công khai chỉ còn hộp thoại xác nhận. Thêm ý b — bỏ hẳn bộ thông tin công khai riêng.

**(3) Có bắt buộc cho luồng nghiệp vụ không? — Một phần CÓ.** Bắt buộc ở **Khóa học**: bốn trường công khai của khoá hiện **không có ô nhập trên màn nào** (`srs-v3.5.md:1031`), nên trường vĩnh viễn rỗng. Phần còn lại là thống nhất trải nghiệm, không chặn luồng. Riêng ý b **không được làm**: mô tả công khai của Vụ việc do cán bộ phê duyệt soạn riêng để ẩn danh doanh nghiệp theo Nghị định 13/2023 — gộp vào mô tả nội bộ là đẩy dữ liệu cá nhân ra Cổng.

#### Căn cứ chi tiết

**(1) Bốn kiểu bố trí hiện hành** — `srs-v3.5.md:1025`, đếm theo chính bảng đó: 5 + 4 + 2 + 1 = 12 đối tượng.

| Kiểu | Số đối tượng | Đối tượng | Đang nhập ở đâu |
|---|---|---|---|
| (1) Nhập ở form thêm/sửa | 5 | Biểu mẫu · Chương trình đào tạo · Tư liệu pháp lý vụ việc · Bài giảng · Kho câu hỏi | Form — **đã đúng khuôn đối tác muốn** |
| (2) Nhập ở hộp thoại / accordion công khai | 4 | Tổ chức tư vấn · Vụ việc · Hỏi đáp · Tư vấn chuyên sâu | Bước công khai |
| (3) Tách đôi | 2 | Tư vấn viên (ảnh ở form đăng ký, mô tả + tệp ở hộp thoại) · Kế hoạch đào tạo năm (ảnh ở form lập, bốn trường còn lại ở hộp thoại) | Cả hai nơi |
| (4) Nhập một phần | 1 | Khóa học — mới có ô Ảnh đại diện; bốn trường còn lại **không có ô nhập ở đâu** | Thiếu hẳn |

Số đối tượng còn nhập tại bước công khai = 4 + 2 = **6/12**.

**(1) Đúng chỗ đối tác nêu.**

- `srs-fr-09-bieu-mau.md:668` — *"| 16 | form | Switch \"Công khai trên Cổng PLQG\" | switch | Mặc định OFF. **Bật → hiện 3 trường bên dưới** |"*; `:669-671` là ba ô Ảnh đại diện công khai / Mô tả công khai / File đính kèm công khai, điều kiện hiển thị *"khi Switch ON"*.
- `srs-fr-02-hoi-dap.md:1119` — nút "Công khai" của Hỏi đáp mở **modal nhập** ảnh + mô tả + tệp + bản xem trước.
- `srs-fr-05-vu-viec.md:1346-1352` — Inputs bước Công khai vụ việc gồm `mo_ta_cong_khai` **bắt buộc**, tối đa 2000 ký tự.
- `srs-fr-04-chuyen-gia-tvv.md:1407` — hộp thoại `MD-CONG-KHAI` của Tư vấn viên là **form nhập** mô tả (bắt buộc) + tệp.
- `srs-fr-12-tv-chuyen-sau.md:1177` — accordion "Công khai chuyên trang" nằm trong màn chi tiết, chỉ hiện khi hồ sơ Đã duyệt.
- `srs-fr-15-ct-htpldn.md:1144` — nút "Công bố" của Chương trình HTPLDN **đã chỉ là hộp thoại xác nhận**, đúng khuôn đối tác muốn.

**(3) Vì sao ý b không làm được.** Mô tả công khai không phải bản sao của mô tả nội bộ, mà là một nội dung khác về bản chất, do một vai khác soạn ở một thời điểm khác:

- `srs-fr-05-vu-viec.md:2503` (BR-PUBLIC-04, Chủ đầu tư chốt Q-NEW-02 ngày 16/04/2026) — khi đăng vụ việc lên Cổng chỉ gửi **10 trường** trong danh sách trắng, **không gửi 6 trường nhạy cảm** gồm tên doanh nghiệp, người đại diện, CCCD/MST, mô tả nội bộ, hồ sơ nghiệp vụ, nội dung tư vấn, số điện thoại/thư điện tử/địa chỉ; *"CB Phê duyệt soạn `mo_ta_cong_khai` riêng (không auto-extract từ `mo_ta` nội bộ) — chỉ nội dung đã review mới lên chuyên trang"*. Căn cứ pháp luật ghi tại `:1418`: Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.
- `srs-fr-13-tv-nhanh.md:106` (BA chốt 30/07/2026) — *"Hệ thống KHÔNG tự điền giá trị mặc định; để trống thì lưu trống"* cho mô tả công khai của Kho câu hỏi.
- Hai trường nằm trên **cùng một bản ghi**, Cổng kéo thẳng từ bản ghi đó. Không có bản sao thứ hai, nên cũng không có chuyện dữ liệu lệch nhau giữa phần mềm quản lý và Cổng.

**→ Kết luận: đề nghị chính đáng ở ba ý a, c, d — nhận, áp một khuôn chung cho cả 12 đối tượng công khai. Riêng ý b (bỏ bộ thông tin công khai riêng) KHÔNG làm: mô tả công khai là nội dung đã ẩn danh và đã qua rà soát, do Chủ đầu tư chốt và có căn cứ Nghị định 13/2023; bỏ nó là đẩy dữ liệu cá nhân doanh nghiệp ra Cổng. Dev action: Có (chưa làm) · Sửa đặc tả: Có (chưa làm) · Doc action: Có — **19 mục** trong bản bàn giao (chưa làm) · Sheet: không áp dụng — ngoài luồng UAT.**  **✅ BA duyệt 12/08/2026.**

> *Lịch sử: phạm vi nhóm ô đã đổi hai lần trước khi duyệt — ban đầu chia theo màn (7 form / 5 chi tiết), sau chia theo trường, cuối cùng chuyển Tư vấn viên và Tổ chức tư vấn sang nhóm form (9 form / 3 chi tiết).*

⚠️ Hiện trạng phần mềm ở mọi màn nêu trên còn `[CHỜ BẰNG CHỨNG]` — xem điểm treo 1.

> **Phản hồi gửi đối tác — đã duyệt, gửi được:**
> **[Lý do]** Chúng tôi thống nhất với đề nghị của Quý đơn vị: các ô nội dung đăng tải sẽ nằm ngay trên hồ sơ và nhìn thấy từ đầu, thao tác Công khai chỉ còn bước xác nhận. Riêng ô Mô tả công khai, kính đề nghị Quý đơn vị cho giữ lại như một ô riêng: với nhóm Vụ việc và Hỏi đáp, nội dung đăng lên Cổng phải được ẩn danh doanh nghiệp và người đại diện theo Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân, nên không thể lấy nguyên nội dung hồ sơ nội bộ. Ô này nằm trên cùng một bản ghi với hồ sơ, Cổng lấy dữ liệu trực tiếp từ bản ghi đó nên không phát sinh bản thứ hai và không có tình trạng dữ liệu khác nhau giữa hai bên.
> **[Nhận định]** Chúng tôi sẽ gửi lại danh sách màn hình điều chỉnh kèm ước lượng khối lượng trong lần bàn giao gần nhất.

### Phương án xử lý (cập nhật SRS) — **✅ BA duyệt 12/08/2026, phần bổ sung duyệt lại 13/08/2026**

**Một khuôn duy nhất cho cả 12 đối tượng: ô nội dung công khai nằm trên chính hồ sơ và nhìn thấy ngay; nút Công khai chỉ còn hộp thoại xác nhận.** Chỗ đặt ô chia theo **từng trường**, không chia theo màn: trường nào biết trước lúc lập hồ sơ thì đưa lên form thêm mới; trường nào phải chờ hồ sơ xử lý xong mới nhập được thì đặt trên màn chi tiết.

| # | Việc | Áp cho |
|---|---|---|
| 1 | **Ảnh đại diện** đặt ở **form thêm/sửa**, hiện ngay khi mở form, **không ẩn theo công tắc**, không bắt buộc, để trống hoặc tải lỗi thì dùng ảnh mặc định hệ thống | **9 đối tượng nhóm form + Chương trình HTPLDN**. Trong đó 8 đã đặt sẵn ở form, chỉ phải bổ sung cho **Tổ chức tư vấn** và **Chương trình HTPLDN**. Ba đối tượng nhóm chi tiết không áp — xem việc 3 `[sửa 12/08 sau vòng soi 2]` |
| 2 | **Mô tả công khai** và **Tệp đính kèm công khai** đặt ở **form thêm/sửa**, cùng chỗ với Ảnh đại diện | **9** đối tượng biết trước nội dung đăng ngay lúc lập hồ sơ: Biểu mẫu · Chương trình đào tạo · Tư liệu pháp lý vụ việc · Bài giảng · Kho câu hỏi · Kế hoạch đào tạo năm · Khóa học · **Tư vấn viên** · **Tổ chức tư vấn** |
| 3 | **Cả ba ô — Ảnh đại diện · Mô tả công khai · Tệp đính kèm công khai** — gom thành nhóm **"Nội dung công khai" trên màn chi tiết hồ sơ** `[sửa 12/08 sau vòng soi 2: trước đó ảnh để ở form, làm bộ thông tin công khai của một hồ sơ nằm ở hai chỗ — đúng thứ đối tác phàn nàn]`, hiện ngay, nhập và sửa được bất cứ lúc nào trước khi đăng; quyền sửa nhóm ô này thuộc đúng vai có quyền đăng | **3** đối tượng mà nội dung đăng lên Cổng là tóm tắt kết quả xử lý: Vụ việc · Hỏi đáp · Tư vấn chuyên sâu |
| 4 | Nút **Công khai / Công bố** chỉ còn **hộp thoại xác nhận** — không ô nhập, không mở lại form cho sửa | 12/12 |
| 5 | Đối tượng bắt buộc có Mô tả công khai mà ô còn trống: hộp thoại xác nhận **chặn**, báo rõ ô cần điền và mở về đúng ô đó. Điều kiện trạng thái được công khai giữ nguyên (BR-PUBLIC-01) | Vụ việc · Tư vấn viên · Tổ chức tư vấn |
| 6 | **Giữ** ô Mô tả công khai tách khỏi mô tả nội bộ (ý b không làm) | 12/12 |
| 7 | **Hủy công khai không xoá nội dung công khai** — chỉ đặt cờ về 0 và xoá Thời gian đăng tải; giữ nguyên Ảnh đại diện, Mô tả công khai, Tệp đính kèm công khai để tái công khai không phải nhập lại. **Đây là đưa về khuôn chung, không phải đặt ngoại lệ mới**: Tư vấn viên (`srs-fr-04-chuyen-gia-tvv.md:666`) và Kế hoạch đào tạo năm (`srs-fr-03-dao-tao.md:1298`) đều đã ghi sẵn *"giữ nguyên giá trị đã lưu để tái công khai không phải nhập lại"*; Vụ việc là chỗ duy nhất xoá `[bổ sung 12/08 sau vòng soi 1; đối chiếu tiền lệ 12/08 sau lượt soi hẹp]` | 12/12 |
| 8 | **Ảnh đại diện sửa được ở mọi trạng thái trừ Hủy / Vô hiệu hoá** — không chịu quy tắc khoá sửa sau duyệt. **Phải ghi ngoại lệ vào từng màn**, không chỉ nêu làm nguyên tắc chung: nhóm Đào tạo không có dòng quy tắc tương tác nào cấm hiện nút Sửa ngoài trạng thái nháp, nên không sinh chọi như Chương trình HTPLDN — nhưng nếu không ghi vào chính đặc tả màn thì bên phát triển vẫn áp khoá `[bổ sung 12/08 sau vòng soi 1; siết 12/08 sau lượt soi hẹp]` | 9 đối tượng nhóm form + Chương trình HTPLDN. Ba đối tượng nhóm chi tiết đã được miễn khoá sẵn qua nhóm ô ở việc 3 |
| 9 | **Ma trận phân quyền** — nâng quyền của cán bộ phê duyệt trên Hỏi đáp từ chỉ đọc lên **đọc + cập nhật giới hạn**. Phải dùng **một ký hiệu chú thích mới** kèm giải thích *"chỉ sửa được nhóm ô Nội dung công khai và cờ công khai"*, theo đúng cách bảng này đang làm với các quyền có điều kiện (`†`, `‡`, `‖`, `¤`, `◊` — `srs-v3.5.md:1391-1400`). Ghi trơn `RU*` sẽ hàm ý sửa được cả bản ghi, chọi với `srs-fr-02-hoi-dap.md:1046`. Vụ việc đã có sẵn quyền cập nhật, không phải sửa `[bổ sung 12/08; siết cách ghi 12/08 sau lượt soi hẹp]` | Hỏi đáp |
| 10 | **Chỗ đặt ô công khai của Tư vấn viên — CHỜ BA CHỐT.** Ảnh chân dung đang nằm ở §Inputs của nghiệp vụ Đăng ký tham gia mạng lưới, tác nhân là Người hỗ trợ pháp lý (`srs-fr-04-chuyen-gia-tvv.md:313`); nếu đặt Mô tả công khai ở nghiệp vụ Quản lý tư vấn viên, tác nhân là cán bộ nghiệp vụ, thì hai ô của **cùng một hồ sơ nằm ở hai form, hai vai** — lặp đúng lỗi vừa sửa ở việc 3. Vướng thêm: ma trận cho Người hỗ trợ dấu `—` trên thực thể tư vấn viên (`srs-v3.5.md:1321`) trong khi nghiệp vụ đăng ký lại cho vai đó tạo bản ghi — hai nguồn chọi nhau từ trước. Phải chốt: gom cả ba ô về một form nào, và ai được sửa `[bổ sung 12/08; nâng thành điểm treo 12/08 sau lượt soi hẹp]` | Tư vấn viên |
| 11 | **Bỏ các trường nội dung công khai khỏi §Inputs của nghiệp vụ Công khai**, vì chúng không còn được nhập ở bước đó nữa — đọc từ hồ sơ. **Riêng FR-III-16: đây là đảo một chốt vừa áp** — ba trường đó mới được bổ sung vào §Inputs ngày 01/08/2026 theo phiếu `AI_TIEN-002` (`srs-fr-03-dao-tao.md:12`); ghi rõ lý do đảo để lượt rà sau không báo là hồi quy | 4 nghiệp vụ: FR-II-08 (Hỏi đáp) · FR-V.I-NEW-05 (Vụ việc) · FR-IV-08 (Tư vấn viên, Tổ chức tư vấn) · FR-III-16 (Kế hoạch đào tạo năm). FR-X.2-06 đã nằm ở nhóm chỗ vá kèm `[bổ sung 12/08 sau vòng soi 2]` |
| 12 | **Chốt ràng buộc của hai trường khi gom về một khuôn** — độ dài Mô tả công khai và số tệp tối đa của Tệp đính kèm công khai `[bổ sung 12/08 sau vòng soi 2 — xem ghi chú bên dưới]` | 12/12 |

**Danh sách chỗ sửa đã định vị** `[bổ sung 12/08 sau lượt soi 4 tầng]` — phương án trước đó mới nêu nguyên tắc, chưa khoanh phạm vi. Soi đủ bốn tầng (§Processing · đặc tả màn · quy tắc tương tác · bản bàn giao) cho ra:

| Tầng | Chỗ phải sửa |
|---|---|
| Đặc tả màn | `srs-fr-02-hoi-dap.md:1119` (nút Công khai mở modal nhập) · `srs-fr-05-vu-viec.md:1754` (bảng hành động) và `:1414` (điều kiện chấp nhận *"mở modal Công khai với form ảnh + mô tả + file"*) · `srs-fr-12-tv-chuyen-sau.md:1177` (accordion) · `srs-fr-04-chuyen-gia-tvv.md:1407` (định nghĩa `MD-CONG-KHAI`) và `:1560` (nút header) · `srs-fr-03-dao-tao.md:1839-1846` (Hộp thoại công khai Kế hoạch năm) · `srs-fr-09-bieu-mau.md:668-671` |
| Quy tắc tương tác | `srs-fr-12-tv-chuyen-sau.md:1202` · `srs-fr-04-chuyen-gia-tvv.md:1466` và `:1467` (công khai / hủy công khai **hàng loạt** cũng mở hộp thoại nhập) · `srs-fr-02-hoi-dap.md:1148` (quy tắc chống mã độc đang trỏ vào *"modal Công khai"* — đổi tham chiếu sang nhóm ô mới, nếu không thành tham chiếu chết). **`srs-fr-03-dao-tao.md` không có mục Quy tắc tương tác nào** — với nhóm Đào tạo, ngoại lệ ở việc 8 phải ghi thẳng vào bảng thành phần màn |
| §Processing / §Inputs | Việc 11 |
| Bản bàn giao | **19 mục** có ô Mô tả công khai: 4.2.8.2.2 · 4.2.8.2.3 · 4.3.1.2.2 · 4.3.4.2.3 · 4.3.7.2.2 · 4.3.7.2.3 · 4.4.5.2.2 · 4.4.8.2.2 · 4.4.8.2.3 · 4.5.19.2.2 · 4.5.19.2.3 · 4.9.4.2.2 · 4.9.4.2.3 · 4.12.1.3.2 · 4.12.1.3.3 · 4.12.6.2.2 · 4.12.6.2.3 · 4.13.1.2.2 · 4.13.6.2.3 (đếm bằng cách quét mọi bảng của tệp bàn giao). Nhóm 4.16 là mô tả giao diện liên thông ra — chỉ trả dữ liệu, **không** phải ô nhập, giữ nguyên |

**Hai điều phải giữ khi bỏ ô nhập khỏi hộp thoại công khai** `[bổ sung 12/08 sau lượt soi 4 tầng]`:

- **Câu cảnh báo chia sẻ dữ liệu của Tư vấn chuyên sâu.** `srs-fr-12-tv-chuyen-sau.md:1202` gắn vào hộp thoại một cảnh báo đã chốt ở đợt UAT trước: *"Khi công khai, Tiêu đề, Nội dung yêu cầu và Kết quả tư vấn sẽ được chia sẻ qua Cổng PLQG"* `[STT11]`. Bỏ ô nhập mà bỏ luôn cảnh báo là gỡ mất một chốt đã duyệt — **chuyển câu này sang hộp thoại xác nhận**.
- **Điều kiện hiện nhóm ô.** Cùng dòng `:1202` quy định accordion công khai *"chỉ hiển thị khi `trang_thai = DA_DUYET`"*. Việc 3 nói nhóm ô hiện ngay — hai câu chọi nhau. Chốt: **nhóm ô hiện ngay từ khi mở hồ sơ**, còn điều kiện trạng thái chỉ gate **nút Công khai** (BR-PUBLIC-01 giữ nguyên). Đây đúng điều đối tác cần: thấy ô từ đầu.

**Ghi chú cho việc 12 — hai ràng buộc đang lệch giữa các nhóm.** Định nghĩa Common Public Fields ở tệp nền (`srs-v3.5.md:990-996`) **không nêu** giới hạn ký tự của Mô tả công khai lẫn số tệp tối đa của Tệp đính kèm công khai, nên mỗi nhóm tự đặt: mô tả **2000 ký tự** ở Hỏi đáp và Vụ việc, **5000 ký tự** ở Tư vấn viên và Tổ chức tư vấn; tệp thì bốn chỗ ghi trần **10 tệp**, các chỗ còn lại chỉ ghi "nhiều tệp" không nêu trần. Gom về một khuôn mà không chốt thì bên phát triển sẽ lấy một mức áp cho tất cả. Đề nghị: **giữ nguyên mức của từng nhóm** và ghi rõ vào định nghĩa nền là mức do từng nhóm quy định; riêng số tệp thì **chốt trần 10** cho mọi nhóm vì bốn chỗ đã dùng mức đó và không chỗ nào dùng mức khác.

**Bốn chỗ phải vá kèm khi áp:**

- **Tổ chức tư vấn** — hai chỗ. Một: §Inputs của nghiệp vụ Quản lý Tổ chức tư vấn có 17 trường (`srs-fr-04-chuyen-gia-tvv.md:1047-1063`), **không có Ảnh đại diện lẫn Mô tả công khai**; ảnh của tổ chức hiện **không có ô nhập trên bất kỳ màn nào** — cùng loại lỗi với Khóa học. Bổ sung cả ba ô vào form quản lý tổ chức. Hai: §Processing của chính nghiệp vụ đó chỉ có Thêm mới, Xóa, Công khai, Xuất danh sách — **thiếu hẳn bước Chỉnh sửa**, dù phần Mô tả ghi là có sửa; phải bổ sung thì mới có chỗ mô tả việc sửa ba ô này `[VIỆC THÊM BẮT BUỘC — phát hiện 12/08 khi rà lại Tổ chức tư vấn]`.
- **Khóa học** — bốn ô công khai còn thiếu (công tắc Công khai · Mô tả công khai · Tệp đính kèm công khai · Thời gian đăng tải chỉ đọc) hiện không có trên màn nào; bổ sung vào SCR-III-02 Tab "Thông tin".
- **Biểu mẫu** — bỏ điều kiện hiển thị *"khi Switch ON"* của ba ô tại `srs-fr-09-bieu-mau.md:669-671`.
- **Kho câu hỏi** — FR-X.2-06 §Processing bước 3 ghi lưu ba trường mà §Inputs của chính nghiệp vụ đó không có; sửa thành đọc giá trị đã nhập ở form, không nhận nhập mới.

**Vì sao đúng ba đối tượng đó phải giữ ô trên màn chi tiết.**

Nói gọn trong bốn bước:

1. Phần mềm có một quy tắc chung: **hồ sơ đã được duyệt thì khoá lại, không cho sửa nữa** — để không ai sửa nội dung sau khi cấp trên đã ký duyệt.
2. Mà **chỉ hồ sơ đã duyệt mới được đăng lên Cổng.**
3. Ghép hai điều đó: nếu ô Mô tả công khai nằm trong form hồ sơ thì **đến lúc được phép đăng, form đã khoá — không ai điền vào ô đó được nữa.**
4. Với hầu hết hồ sơ, chuyện này không sao. Biểu mẫu, khoá học, tư vấn viên… nội dung giới thiệu viết được ngay từ lúc lập hồ sơ, viết xong rồi mới trình duyệt; đến lúc khoá thì ô đã có chữ.

**Riêng Vụ việc, Hỏi đáp, Tư vấn chuyên sâu thì không viết trước được.** Thứ đăng lên Cổng là tóm tắt **kết quả giải quyết**. Lúc mới mở hồ sơ thì chưa giải quyết gì, chưa có kết quả nào để tóm tắt; phải đợi xử lý xong — mà xử lý xong cũng là lúc hồ sơ đã duyệt, tức đã khoá. Thành ra kẹt: ô nằm trong form thì lúc cần điền không điền được, mà không điền thì không đăng được.

Cách gỡ: với ba loại này, ô tách ra thành một khối riêng trên màn chi tiết, không bị khoá theo hồ sơ. Cán bộ mở hồ sơ ra vẫn thấy ô ngay, điền sau khi đã có kết quả, rồi bấm Công khai để xác nhận — vẫn đúng ý đối tác. Thêm một lẽ nữa, riêng Vụ việc và Hỏi đáp: người bấm đăng là **cán bộ phê duyệt**, không phải người lập hồ sơ; ô nằm trong form thì người lập là người viết, còn người chịu trách nhiệm về nội dung hiển thị ra ngoài lại không có chỗ sửa.

Ảnh đại diện nằm ngoài toàn bộ câu chuyện trên — chỉ là hình minh hoạ, chọn lúc nào cũng được, không phụ thuộc kết quả xử lý, không chứa thông tin nhạy cảm. Vì vậy đưa lên form thêm mới cho cả 12 đối tượng; 8/12 vốn đã đặt ở form từ trước.

---

Phần dưới là căn cứ tra được trong đặc tả, để Dev và BA đối chiếu khi cần.

**Căn cứ 1 — quy tắc khoá sửa.** BR-FLOW-03 (`srs-fr-05-vu-viec.md:2405`): *"Bản ghi đã ở trạng thái 'Đã duyệt' hoặc 'Hoàn thành' không thể chỉnh sửa hoặc xóa. QTHT có thể force-edit (audit đặc biệt)."*

**Căn cứ 2 — với ba đối tượng này, trạng thái được phép công khai rơi đúng vào vùng bị khoá.** Giao của "trạng thái công khai được" và "trạng thái còn sửa được form" là **tập rỗng**:

| Đối tượng | Trạng thái được công khai | Trạng thái form còn sửa được |
|---|---|---|
| Vụ việc | `DA_DUYET`, `HOAN_THANH` — `srs-fr-05-vu-viec.md:1342` (PRE-02) | BR-FLOW-03 cấm sửa đúng hai trạng thái đó — `:2405` |
| Hỏi đáp | `DA_DUYET` — `srs-fr-02-hoi-dap.md:1119` (điều kiện hiển thị nút Công khai) | *"Sửa (chỉ khi trang_thai NOT IN (DA_DUYET, CONG_KHAI, HOAN_THANH))"* — `:1046` |
| Tư vấn chuyên sâu | `DA_DUYET` — `srs-fr-12-tv-chuyen-sau.md:1177`, `:1202` (accordion chỉ hiện khi DA_DUYET) | CB NV *"thao tác được ở trạng thái TIEP_NHAN hoặc DANG_TU_VAN"* — `:140` |

Đặt ô nội dung công khai ở form thêm/sửa của ba đối tượng này thì **đúng lúc được phép đăng, form đã khoá** — ô có mà không ai điền được.

**Căn cứ 3 — nội dung chỉ hình thành ở hoặc sau bước duyệt.** Vụ việc: danh sách trắng gửi ra Cổng gồm `ket_qua` và `thoi_gian_xu_ly` (`srs-fr-05-vu-viec.md:2503`) — chưa có lúc lập hồ sơ. Hỏi đáp: chỉ đăng sau khi phản hồi được duyệt. Tư vấn chuyên sâu: mô tả công khai *"khác `noi_dung_tu_van` nội bộ"* (`srs-fr-12-tv-chuyen-sau.md:122`).

**Căn cứ 4 — người viết khác người lập (riêng Vụ việc, Hỏi đáp).** `srs-v3.5.md:1434` — *"HOI_DAP_PUBLISH … **Chỉ CB_PD_{cap}** (siết — không cho CB_NV)"*; Vụ việc do CB Phê duyệt cùng cấp công khai (`srs-fr-05-vu-viec.md:1333`). Hồ sơ do cán bộ nghiệp vụ lập. Đặt ô ở form thì cán bộ nghiệp vụ là người viết, còn cán bộ phê duyệt không có chỗ sửa — vì căn cứ 1.

**Căn cứ 5 — pháp luật, riêng Vụ việc.** BR-PUBLIC-04 (`:2503`) buộc mô tả công khai phải do cán bộ phê duyệt soạn riêng, ẩn danh doanh nghiệp, *"không auto-extract từ `mo_ta` nội bộ"*; căn cứ Nghị định 13/2023/NĐ-CP ghi tại `:1418`.

**Đối chiếu ngược — vì sao 9 đối tượng kia không vướng.** Điểm dễ hiểu nhầm: nhóm Đào tạo **cũng bị khoá sửa sau duyệt**, nhưng vẫn đặt ô ở form được.

| Đối tượng | Có khoá sửa sau duyệt? | Nội dung công khai có trước khi khoá? |
|---|---|---|
| Biểu mẫu | Không có bước duyệt — *"KHÔNG cần phê duyệt, CB NV tự chịu trách nhiệm"* (`srs-fr-09-bieu-mau.md:528`) | Có |
| Tư liệu pháp lý vụ việc | Không — trạng thái chỉ `NHAP` / `CONG_KHAI` (`srs-fr-12-tv-chuyen-sau.md:851`) | Có |
| Tư vấn viên | Không — cập nhật hồ sơ chỉ *"kiểm trạng thái không phải Vô hiệu hóa"* (`srs-fr-04-chuyen-gia-tvv.md:1530`) | Có |
| Tổ chức tư vấn | Không — §Processing FR-IV-NEW-01 không có bước khoá theo trạng thái | Có |
| Chương trình đào tạo · Khóa học · Kế hoạch đào tạo năm | **Có** — sửa chỉ khi `NHAP` / `TU_CHOI` (`srs-fr-03-dao-tao.md:1155`) | **Có** — là bài giới thiệu, viết được trước khi trình duyệt |
| Bài giảng · Kho câu hỏi | Kho câu hỏi có bước duyệt, Bài giảng không | Có |

Với nhóm Đào tạo, nội dung công khai viết xong **trước** khi trình duyệt nên khoá không cản — và còn lợi: phần hiển thị ra Cổng được duyệt cùng hồ sơ. Ba đối tượng Vụ việc, Hỏi đáp, Tư vấn chuyên sâu không có cửa đó.

**Hệ quả bắt buộc ghi vào đặc tả.** Hai thứ phải là **ngoại lệ có tên của BR-FLOW-03**, nếu không ghi rõ thì bên phát triển sẽ áp khoá lên cả hai và luồng lại tắc đúng chỗ cũ:

- **Nhóm ô "Nội dung công khai" trên màn chi tiết** (ba đối tượng nhóm chi tiết): quy tắc khoá áp cho phần thân hồ sơ, không áp cho nhóm ô này; quyền sửa thuộc vai có quyền đăng — cán bộ phê duyệt với Vụ việc và Hỏi đáp, cán bộ nghiệp vụ với Tư vấn chuyên sâu.
- **Ô Ảnh đại diện** (mọi đối tượng): sửa được ở mọi trạng thái trừ Hủy / Vô hiệu hoá. Lý do ở việc 8 — xem phần kiểm định bên dưới.

**Một lỗi lộ ra khi rà lại Tư vấn viên.** Nghiệp vụ công khai hàng loạt (`srs-fr-04-chuyen-gia-tvv.md:1466`) cho chọn nhiều tư vấn viên rồi mở **một** hộp thoại nhập **một** mô tả công khai, sau đó đặt cờ công khai cho tất cả các dòng đã chọn — tức nhiều người khác nhau dùng chung một bài giới thiệu, hoặc mô tả nhập vào không biết ghi cho ai. Đưa ô mô tả về hồ sơ từng tư vấn viên thì thao tác hàng loạt trở lại đúng nghĩa: chỉ xác nhận, mỗi bản ghi mang mô tả của chính nó, bản ghi nào chưa có mô tả thì bị chặn và liệt kê ra.

**Phạm vi ảnh hưởng đã rà:**

| Câu hỏi rà | Kết quả |
|---|---|
| Chỗ khác cùng vi phạm | Đã tìm bằng hai mẫu khác hình dạng: `anh_dai_dien` và `ảnh đại diện` trên toàn thư mục SRS. Ngoài 12 đối tượng của bản đồ, còn **2** đối tượng có cờ công khai mà không có bộ trường chuyên trang: `CHUONG_TRINH_HTPL` (xử ở Mục 2) và `THU_MUC_BIEU_MAU` (`srs-fr-09-bieu-mau.md:816`) — thư mục biểu mẫu đã được ghi nhận là **cố ý không thêm** tại `CHANGELOG-v3-to-v3.5.md:1172`, giữ nguyên |
| Bản sao | Mỗi đối tượng có hai nơi mô tả: bảng nền `srs-v3.5.md` §3.4.3.x và tệp FR của nhóm. Riêng Kế hoạch đào tạo năm còn thêm bản đồ CPF `srs-v3.5.md:1025`. Cặp thứ ba là bản gốc ↔ bản bàn giao `.docx` |
| Nhãn và số đếm | `srs-v3.5.md:1025` ghi *"5 entity / 4 entity / 2 entity / 1 entity"* và `:1027` ghi *"10 entity khác giữ nguyên"* — viết lại theo trường: Ảnh đại diện ở form với cả 12; Mô tả công khai và Tệp đính kèm công khai ở form với 9, ở nhóm ô trên màn chi tiết với 3. Câu `:1031` *"Điểm lệch còn tồn"* xoá vì lượt này khép |
| Dòng chung bị chọi | Bỏ điều kiện *"khi Switch ON"* của Biểu mẫu không đụng BR-PUBLIC-01/02/03 — ba quy tắc đó nói về **điều kiện được bật cờ công khai**, không nói về chỗ đặt ô nhập. Việc 4 giữ nguyên hiệu lực của mã lỗi `ERR-CK-02` (`srs-fr-04-chuyen-gia-tvv.md:683`), chỉ đổi chỗ phát sinh lỗi từ hộp thoại nhập sang hộp thoại xác nhận |
| Chiều ngược sang `.docx` | Mỗi màn sửa sinh một dòng Doc action tương ứng. Với Biểu mẫu, §4.9.4.2.2 vốn **không** nêu điều kiện ẩn/hiện theo công tắc nên không phải sửa |

---

## Mục 2 — Bổ sung ô Ảnh đại diện cho Chương trình HTPLDN

**Vấn đề:** Màn thêm mới và chỉnh sửa Chương trình hỗ trợ pháp lý doanh nghiệp không có chỗ tải ảnh đại diện, trong khi kế hoạch chương trình sau khi công bố sẽ hiển thị trên Cổng Pháp luật Quốc gia cho doanh nghiệp tra cứu. Các nhóm dữ liệu khác cùng lên Cổng đều đã có ảnh; riêng nhóm này hiển thị không có hình minh hoạ.

**(1) Phần mềm đúng bản gốc chưa? — ĐÚNG.** Bản gốc không có trường ảnh cho chương trình, nên phần mềm thiếu ô nhập **không phải sai lệch so với đặc tả**. Đã tra hai biến thể `anh_dai_dien` và `ảnh đại diện` trên `srs-fr-15-ct-htpldn.md` (toàn tệp, 0 kết quả), trên bảng nền `srs-v3.5.md:2187-2201` (thực thể `CHUONG_TRINH_HTPL` — 13 thuộc tính, chỉ có `la_cong_bo` tại `:2200` và `ngay_cong_bo` tại `:2201`), trên sơ đồ quan hệ `srs-v3.5.md:4073-4079`, và trên `srs-fr-16-api.md:1596-1604`. Chương trình HTPLDN cũng **không nằm trong 12 đối tượng** của bảng Common Public Fields (`srs-v3.5.md:1006`, 12 dòng thân bảng `:1010-1021`).

**(1b) Bản `.docx` đối tác cầm có nói khác không? — KHÔNG.** `HTPLDN-PTYC-CT-v3.5.docx` §4.15.1.3.2 (bảng *"Mô tả thông tin trên màn hình"* của màn Chi tiết Chương trình hỗ trợ pháp lý) liệt kê 17 dòng trường thông tin, **không có Ảnh đại diện**. Trùng bản gốc → **không phải lệch tài liệu bàn giao**, đây là yêu cầu bổ sung thật.

**(2) Đối tác yêu cầu khác gì?** Thêm một trường Ảnh đại diện, **không bắt buộc**, cho màn Chương trình HTPLDN. Đối tác nói rõ đây là mục còn sót của đợt yêu cầu trước.

**(3) Có bắt buộc cho luồng nghiệp vụ không? — KHÔNG bắt buộc, nhưng nên làm.** Thiếu ảnh thì chương trình vẫn công bố và Cổng vẫn kéo được. Lý do nên làm: đây là mục thứ ba trong chính yêu cầu gốc của đợt trước, và là đối tượng công bố duy nhất còn thiếu ảnh mà chưa có quyết định bỏ.

#### Căn cứ chi tiết

**(2) Đây là mục sót của đợt trước, không phải yêu cầu mới.** Yêu cầu gốc STT 112 nêu ba màn: *"Màn thêm mới/chỉnh sửa **kế hoạch đào tạo** và **khóa học**/ **Chương trình kế hoạch**: Bổ sung trường Ảnh đại diện: Không bắt buộc, cho phép tải lên các định dạng ảnh"* (`Week4/Phản hồi/phan-hoi-ba-danh-sach-toi-uu-task-STT110-112.md:69` và `:86`). Hai màn đầu đã xử lý và BA duyệt ngày 31/07/2026; cụm **"Chương trình kế hoạch"** khi đó được hiểu là màn Chương trình đào tạo (`Week4/Phản hồi/phan-hoi-AI_TIEN-002-anh-dai-dien-va-hop-thoai-cong-khai.md:17`). Ảnh chụp đối tác gửi kèm lần này khoanh đỏ mục **Chương trình HTPLDN** trên thanh điều hướng, xác định đó mới là màn thứ ba.

Kết luận cũ về Chương trình đào tạo **vẫn đứng** và không phải đảo: bản gốc đã quy định ô ảnh ở form chương trình đào tạo từ đợt 06/05/2026, độc lập với đợt STT 112.

**(3) Chương trình HTPLDN công bố ra Cổng qua nghiệp vụ riêng.** `srs-fr-15-ct-htpldn.md:1611-1615` (BR-FLOW-05) — công bố = đặt cờ `la_cong_bo = 1` + chuyển trạng thái Đã công bố; Cổng chủ động kéo qua giao diện liên thông ra. Bản ghi được kéo qua `srs-fr-16-api.md` FR-XII-15, §Outputs hiện có **10 trường**, không có trường ảnh.

**→ Kết luận: đề nghị chính đáng, phải làm — bổ sung trường Ảnh đại diện cho Chương trình HTPLDN, không bắt buộc, JPG/PNG/GIF tối đa 5MB, để trống hoặc tải lỗi thì tự dùng ảnh mặc định hệ thống, theo đúng chuẩn đang áp cho toàn hệ thống. Việc phần mềm chưa có ô này KHÔNG phải sai lệch so với đặc tả — cả bản gốc lẫn bản bàn giao đều không quy định. Dev action: Có (chưa làm) · Sửa đặc tả: Có (chưa làm) · Doc action: Có (chưa làm) · Sheet: không áp dụng — ngoài luồng UAT.**  **✅ BA duyệt 12/08/2026.**

### Phương án xử lý (cập nhật SRS) — **✅ BA duyệt 12/08/2026, phần bổ sung duyệt lại 13/08/2026**

**Áp đúng khuôn đã chốt ở Mục 1.** Chương trình HTPLDN là đối tượng công bố thứ 13, ngoài 12 đối tượng của bản đồ Common Public Fields. Xếp nhóm theo tiêu chí của Mục 1: người lập chương trình và người công bố **cùng là cán bộ nghiệp vụ** (`srs-fr-15-ct-htpldn.md:121` và `:549`), nội dung hiển thị biết trước ngay lúc lập ⇒ thuộc **nhóm nhập ở form**. Nút Công bố vốn đã chỉ là hộp thoại xác nhận (`:1144`) nên không phải sửa. Nếu về sau bổ sung Mô tả công khai hoặc Tệp đính kèm công khai cho chương trình thì cũng đặt ở form, không đặt ở hộp thoại công bố.

| # | Chỗ sửa | Nội dung |
|---|---|---|
| 1 | `srs-fr-15-ct-htpldn.md` — thực thể `CHUONG_TRINH_HTPL` (`:1338-1357`) | Thêm thuộc tính `anh_dai_dien`: kiểu tệp ảnh, không bắt buộc, JPG/PNG/GIF ≤ 5MB, mặc định ảnh hệ thống |
| 2 | `srs-fr-15-ct-htpldn.md` — sơ đồ quan hệ nhóm (`:1264-1277`) | Thêm dòng `anh_dai_dien`. Sơ đồ này liệt kê gần đủ thuộc tính, có cả `la_cong_bo`, nên bỏ sót sẽ tạo lệch mới `[bổ sung 12/08 sau lượt kiểm định]` |
| 3 | `srs-v3.5.md` — bảng nền §3.4.3.10 (`:2187-2201`) | Thêm cùng thuộc tính, giữ khớp với tệp FR |
| 4 | `srs-fr-15-ct-htpldn.md` — FR-XI-01 §Inputs | Thêm **trường thứ 11** (§Inputs hiện có đúng 10 trường), không bắt buộc |
| 5 | `srs-fr-15-ct-htpldn.md` — FR-XI-01 §Processing bước 4 (`:151`) | Hiện ghi *"Chỉnh sửa: chỉ cho phép khi trạng thái DU_THAO"*. Bổ sung ngoại lệ: **riêng Ảnh đại diện sửa được ở mọi trạng thái trừ Hủy** — theo việc 8 của phương án Mục 1 `[bổ sung 12/08 sau lượt kiểm định]` |
| 6 | `srs-fr-15-ct-htpldn.md` — SCR-XI-01, Trang Chi tiết CT Tab "Thông tin" (`:1123`, dòng thành phần `:1127-1149`) | Thêm một dòng thành phần **Ảnh đại diện**, loại tải ảnh, đặt sau dòng 19 "Tệp đính kèm" (`:1140`). Điều kiện hiển thị **luôn hiển thị**, và ô có **thao tác đổi ảnh ngay tại chỗ**, không đi qua chế độ Sửa của toàn form — bắt buộc phải vậy thì việc 5 mới thi hành được, xem việc 10. Nhân đây ghi rõ nghĩa của *"khi DU_THAO"* ở các dòng 11–19 cùng bảng là **chỉ đọc ngoài trạng thái Dự thảo**, không phải ẩn hẳn `[sửa 12/08 sau lượt soi lại vòng 1]` |
| 7 | `srs-fr-16-api.md` — FR-XII-15 §Outputs (`:977-990`, 10 dòng thân bảng `:981-990`) | Thêm trường trả về thứ 11, **đặt tên `anh_dai_dien`, kiểu structured** cho khớp các API công khai khác (`:1559`), điều kiện *"nếu có"*. Không thêm thì ảnh nhập vào mà Cổng không nhận được — đúng loại lỗi "trường có dữ liệu, không có chỗ dùng" |
| 8 | `srs-fr-16-api.md` — thực thể tham chiếu `CHUONG_TRINH_HTPL` (`:1596-1604`) | Thêm thuộc tính cho khớp |
| 9 | `srs-v3.5.md` — ghi chú §3.2.0.9 (`:1025-1031`) | Ghi rõ Chương trình HTPLDN **chỉ bổ sung một trường ảnh**, không phải đủ bộ năm trường chuyên trang, và thuộc nhóm nhập ở form — để lượt rà sau không báo thiếu bốn trường và không đặt nhầm chỗ |
| 10 | `srs-fr-15-ct-htpldn.md` — Quy tắc tương tác SCR-XI-01 (`:1229`) | Dòng hiện hành: *"Sửa/Xóa CT: chỉ khi DU_THAO … các trạng thái khác không hiện cả hai"*. Bổ sung một câu ngoại lệ: **thao tác đổi Ảnh đại diện không thuộc diện này, hiện ở mọi trạng thái trừ Hủy**. Không bổ sung thì việc 5 mâu thuẫn với dòng này — mở quyền sửa ảnh mà màn hình không có chỗ bấm `[bổ sung 12/08 sau lượt soi lại vòng 1]` |
| 11 | Bản bàn giao `HTPLDN-PTYC-CT-v3.5.docx` §4.15.1.3.2 | Thêm một dòng **Ảnh đại diện · Tệp · Không bắt buộc · Ảnh mặc định của hệ thống · JPG, PNG hoặc GIF, tối đa 5 MB** — Doc action, thuộc bên soạn tài liệu bàn giao |

**Bốn chỗ đã kiểm, không phải sửa** — ghi ra để lượt soi sau khỏi báo lại: (a) **FR-XII-16** (API tìm kiếm chương trình) §Outputs ghi *"Giống FR-XII-15"* nên tự kế thừa trường mới; (b) **Hủy công bố** (`srs-fr-15-ct-htpldn.md:1146` và FR-XI-05 §Processing nhánh Hủy) chỉ đặt cờ về 0 và chuyển trạng thái, **không xoá trường nào** — đã khớp sẵn việc 7 của Mục 1; (c) bảng **Tổng quan entity** của fr-15 (`:1250-1256`) chỉ liệt kê tên và vai trò, không đếm thuộc tính; (d) bảng **danh sách entity** ở tệp nền (`srs-v3.5.md:1278`) chỉ ghi khối lượng bản ghi.

**Hai chỗ cố ý không làm:** (a) **sơ đồ quan hệ ở tệp nền** (`srs-v3.5.md:4073-4079`) — sơ đồ này chỉ liệt kê khoá và vài trường định danh, ngay cả Biểu mẫu cũng không có trường công khai nào trong đó, thêm vào sẽ lệch khuôn chung; (b) **cột Ảnh đại diện trên bảng danh sách chương trình** — đối tác không nêu, và bảng danh sách hiện đã 10 cột.

**Phạm vi ảnh hưởng đã rà:**

| Câu hỏi rà | Kết quả |
|---|---|
| Chỗ khác cùng vi phạm | Xem bảng rà ở Mục 1 — ngoài Chương trình HTPLDN chỉ còn Thư mục biểu mẫu, đã có quyết định cố ý không thêm. **Nói chính xác:** Chương trình HTPLDN là đối tượng công bố duy nhất thiếu hẳn **trường** ảnh; Tổ chức tư vấn thì có trường nhưng thiếu **ô nhập** — hai loại thiếu khác nhau, đừng gộp |
| Bản sao | **Năm** nơi mô tả thực thể, không phải bốn: bảng thuộc tính tệp FR (`srs-fr-15:1338`) · sơ đồ quan hệ tệp FR (`:1264`) · bảng nền (`srs-v3.5.md:2187`) · sơ đồ quan hệ nền (`:4073`) · bảng thực thể tệp API (`srs-fr-16:1596`). Bốn nơi vào bảng phương án, nơi thứ năm cố ý bỏ kèm lý do |
| Nhãn và số đếm | Bảng Common Public Fields giữ nguyên **12** đối tượng — Chương trình HTPLDN không gia nhập nhóm này vì chỉ thêm một trường. FR-XI-01 §Inputs từ **10** lên **11** trường |
| Dòng chung bị chọi | **Có chọi thật, đã xử.** Ngoại lệ ở việc 5 cùng loại với việc 8 của Mục 1 nên không sinh quy tắc mới ở tầng xử lý; nhưng ở tầng màn hình thì chọi với Quy tắc tương tác `:1229` — dòng đó cấm hiện nút Sửa ngoài trạng thái Dự thảo, tức mở quyền sửa ảnh mà không có chỗ bấm. Xử bằng việc 10 (thao tác đổi ảnh tại chỗ, không qua nút Sửa của form). Phần thân chương trình vẫn khoá sau duyệt như cũ `[sửa 12/08 — lượt rà trước chỉ kiểm §Processing, bỏ sót Quy tắc tương tác của màn]` |
| Chiều ngược sang `.docx` | **Hai** dòng Doc action, không phải một. Ngoài việc 11 (thêm dòng trường ở §4.15.1.3.2), còn §4.15.1.3.3 dòng 1 *"Ghi nhận, cập nhật chương trình"* ghi **"Điều kiện hiển thị: chế độ nhập mới, hoặc chương trình ở trạng thái Dự thảo"** — đúng quy tắc mà việc 10 mở ngoại lệ, nên bản bàn giao phải thêm cùng câu ngoại lệ đó `[sửa 12/08 — lượt rà trước kết luận sai là "không nêu điều kiện sửa"]` |

---

## Điểm treo chuyển đợt sau

| # | Nội dung | Phát hiện ở mục nào | Thuộc bên nào | Trạng thái |
|---|---|---|---|---|
| 1 | ~~Chỗ đặt ô công khai của Tư vấn viên, và phân quyền của Người hỗ trợ pháp lý trên hồ sơ tư vấn viên~~ | Mục 1, phương án việc 10 | BA | ✅ **Đã khép 13/08/2026** — hồ sơ tư vấn viên chỉ có một biểu mẫu `SCR-IV-02` nên ba ô đặt thẳng ở đó; ma trận §3.4.2 sửa ô Người hỗ trợ trên `TU_VAN_VIEN` từ `—` sang `CRU*◈` cho khớp FR-IV-03/04 |
| 2 | Hiện trạng phần mềm ở các màn Công khai chưa kiểm chứng — cần ảnh chụp hoặc quay màn hình cho ít nhất màn Biểu mẫu, Hỏi đáp, Vụ việc, Khóa học | Mục 1, câu (1) | Bên dựng môi trường / QA | `[CHỜ BẰNG CHỨNG]` |
| 3 | Ước lượng khối lượng đối tác đề nghị — không rút ra được từ phiếu nghiệp vụ, phải do bên phát triển đưa sau khi BA duyệt phương án | Mục 1 | Dev / PM | Chưa làm |
| 4 | Ma trận phân quyền `srs-v3.5.md:1434` — rà lại khi áp việc 2, để cán bộ phê duyệt của Vụ việc và Hỏi đáp có quyền sửa nhóm ô Nội dung công khai trên màn chi tiết | Mục 1, phương án việc 2 | BA | Làm cùng đợt sửa đặc tả |
| 5 | Chuẩn hoá chỗ đặt ô nhập của bản đồ Common Public Fields (`srs-v3.5.md:1031`) — điểm treo cũ từ 31/07/2026 | Mục 1 | BA | Khép tại phiếu này |
| 6 | Thư mục biểu mẫu không có bộ trường chuyên trang — đã ghi nhận cố ý tại `CHANGELOG-v3-to-v3.5.md:1172`, giữ nguyên trừ khi đối tác nêu lại | Mục 1, bảng rà | BA | Không xử lượt này |
