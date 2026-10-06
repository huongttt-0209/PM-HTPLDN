# Phiếu phân tích — GHSYCHTPL_02 · GHSYCHTPL_06

**Ngày soạn:** 13/08/2026 · **Khối:** Tuần 2 · **Chức năng:** Gửi hồ sơ yêu cầu hỗ trợ pháp lý (UC52)

**Sổ theo dõi:** `docs.google.com/spreadsheets/d/1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` — tab **UAT_TGPL Doanh Nghiệp** (`gid=799081340`). Mã lấy theo bản tải **13/08/2026**; dòng 499 (GHSYCHTPL_02) và 503 (GHSYCHTPL_06), khớp lại bằng cột Mô tả + Kết quả mong đợi.

**Môi trường đối tác kiểm thử** (lấy từ ảnh và video minh chứng, không lấy từ phiếu Dev):
- Phía doanh nghiệp: `uat.phapluat.gov.vn` — Cổng Pháp luật Quốc gia, mục Tư vấn pháp luật › Vụ việc điển hình.
- Phía cán bộ: `htpldn-uat.ospgroup.vn` — bản HTPLDN V1.0.12, đăng nhập Cán bộ NV Trung ương.
- Thời điểm ghi nhận trong minh chứng: 12/08/2026.

**Ghi chú phương pháp:**
- Hai mã cùng một màn hình gửi hồ sơ nhưng **không gộp cụm**: _02 là lỗi ô nhập trên biểu mẫu, _06 là lỗi bước xử lý sau khi gửi — hai phần việc khác nhau của Dev.
- Bản bàn giao đối chiếu: **`HTPLDN-PTYC-CT-v3.5.docx`** (bản hiện hành, `docs/Reference/`), mục **4.5.2 — PM05.QLVV.GHS. Doanh nghiệp gửi hồ sơ yêu cầu hỗ trợ pháp lý**, dòng 5692–5764 của bản chuyển sang dạng chữ giữ nguyên bảng và số mục. Bản bàn giao nói **cùng một điều** với bản gốc ở cả hai mã — không có tranh chấp tài liệu.
- Minh chứng đã mở xem trực tiếp: 2 ảnh và 13 khung hình trích từ video (`ffmpeg`, 1 khung/3 giây).
- **Số dòng trích dẫn chốt theo bản đọc 13/08/2026.** Tệp nền `srs-v3.5.md` bị sửa ngay trong ngày (lúc 11:20) làm số dòng dịch 2 dòng — 4 trích dẫn của phiếu đã phải chỉnh lại. Trước khi thi hành phải mở lại từng dòng để xác nhận, đừng tin số dòng suông; định danh bền là **tên mục và tên trường**, không phải số dòng.

**Bối cảnh nghiệp vụ (nêu một lần, dùng chung cả phiếu):** Doanh nghiệp đăng nhập chuyên trang rồi gửi hồ sơ đề nghị hỗ trợ pháp lý. Hồ sơ chạy sang phần mềm của cán bộ thành một vụ việc mới, cán bộ nghiệp vụ tiếp nhận và xử lý trong 15 ngày làm việc theo Nghị định 55/2019/NĐ-CP Điều 8 Khoản 1. Mức ưu tiên xử lý là **diện chính sách** của doanh nghiệp theo Nghị định 55/2019/NĐ-CP Điều 4 Khoản 4 (do phụ nữ làm chủ, sử dụng nhiều lao động nữ, sử dụng từ 30% lao động là người khuyết tật), không phải nguyện vọng của người nộp hồ sơ.

## Thay đổi kể từ lượt duyệt gần nhất

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| Mục 3 — Kênh tiếp nhận | **(a) Kết luận đã ĐẢO — đọc kỹ.** Tra Danh sách UC/Transaction: nhóm V không có tác nhân Cổng Pháp luật Quốc gia. **Bỏ toàn bộ phương án bổ sung kênh** (12 chỗ sửa bản gốc + 3 dòng cập nhật tài liệu bàn giao + rào chắn) — phần mềm đang làm đúng, không sửa gì | Có — từ Loại 2 (Dev action Có · Sửa đặc tả Có) thành **phần mềm đúng** (Dev action Không · Sửa đặc tả Không) |
| Mục 1 — Phương án | **(b) Kết luận giữ, phần việc đổi hình — đọc phần phương án.** Lượt phản biện chỉ ra cách sửa cũ nặng hơn cần thiết: **bỏ việc thêm khối "Chế độ doanh nghiệp"**, thay bằng sửa thẳng cột Hành vi và Điều kiện hiển thị trong bảng thành phần có sẵn. Thêm việc 7 — bổ sung SCR-V.I-02 vào dòng quy ước giao diện di động (`:1613`), chỗ này trước đó bị sót | Không — vẫn Loại 1, Dev action Có · Sửa đặc tả Có |
| Mục 1 — Việc thêm khi thi hành | **(b) Kết luận giữ, phần việc phình ra — đọc phần phương án.** Phát sinh **sau** lượt BA duyệt, đã báo ngay: thêm **việc 8** — dòng `:1484` là danh sách thứ hai cùng liệt kê màn hình phía doanh nghiệp. Chỉ sửa việc 7 (`:1613`) thì hai danh sách nói ngược nhau. Thuần kỹ thuật văn bản, nhãn `[VIỆC THÊM BẮT BUỘC]` | Không — vẫn Loại 1 |
| Mục 1 và 2 | **(c) Chỉ sửa câu chữ — đọc lướt.** Phần đối chiếu bản bàn giao rút về chỉ dùng `HTPLDN-PTYC-CT-v3.5.docx`, bỏ trích dẫn các bản cũ | Không |

---

## 1. GHSYCHTPL_02 — Biểu mẫu gửi hồ sơ hỏi thông tin người gửi và bắt doanh nghiệp tự chọn mức ưu tiên

**Vấn đề:** Doanh nghiệp đã đăng nhập rồi mà biểu mẫu gửi hồ sơ vẫn bắt khai lại họ tên, thư điện tử và số điện thoại người gửi, trong khi không hiển thị tên doanh nghiệp và mã số thuế để người gửi biết hồ sơ đang gắn vào pháp nhân nào. Biểu mẫu còn bắt buộc doanh nghiệp tự chọn mức độ ưu tiên xử lý — thứ mà pháp luật giao cho hệ thống tự xác định theo diện chính sách, không để bên nộp hồ sơ tự đặt. Hệ quả: doanh nghiệp không xác nhận được hồ sơ gắn đúng pháp nhân, và thứ tự xử lý của toàn bộ vụ việc bị chi phối bởi lựa chọn của người nộp thay vì bởi diện ưu tiên theo Nghị định.

**Bóc ý con trong Kết quả mong đợi:**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Tên doanh nghiệp, mã số thuế chỉ đọc, không sửa được | Có — `srs-fr-05-vu-viec.md:179` + `:187` | (1) và Phương án, việc 1 |
| Doanh nghiệp nhập tiêu đề, loại hình hỗ trợ, lĩnh vực pháp luật, nội dung yêu cầu, tải tài liệu | Có — `srs-fr-05-vu-viec.md:180–185` | (1) — phần này phần mềm làm đúng |
| *(ý con lấy thêm từ minh chứng, đối tác chưa nêu)* Ô "Ghi chú" trên biểu mẫu doanh nghiệp | Không có trong bản gốc | (1) và Phương án, việc 2 |

**(1) Phần mềm đúng bản gốc chưa? → SAI.**
- `srs-fr-05-vu-viec.md:179` — "doanh_nghiep_id … *lấy từ session DN đã auth VNeID (không nhập thủ công)*"; bảng Inputs của FR-V.I-02 gồm **đúng 7 trường** (đếm dòng bảng `:179–185`), không có họ tên / thư điện tử / số điện thoại người gửi, không có mức ưu tiên, không có ghi chú.
- `srs-fr-05-vu-viec.md:187` — "*Thông tin DN được đọc từ DOANH_NGHIEP theo `doanh_nghiep_id`*".
- `srs-fr-05-vu-viec.md:196` — bước 4: "*Auto-calc `uu_tien` theo BR-CALC-07*".
- `srs-fr-05-vu-viec.md:2432` (BR-CALC-07) — "***4** và **5** — chỉ do CB NV nâng mức, bắt buộc nhập `ly_do_uu_tien`*"; `:2050` — "*Lý do nâng mức ưu tiên — bắt buộc khi CB NV nâng lên mức 4 hoặc 5*".
- Minh chứng (`GHSYCHTPL_02.jpg`, `GHSYCHTPL_02(2).jpg`): biểu mẫu có **12 ô nhập**, trong đó **6 ô thừa** so với bản gốc — Họ và tên người gửi (bắt buộc), Email liên hệ (bắt buộc), Số điện thoại (bắt buộc), Độ ưu tiên (bắt buộc), Lý do ưu tiên, Ghi chú — và **thiếu 2 ô chỉ đọc** Tên doanh nghiệp, Mã số thuế.

**(1b) Bản `.docx` đối tác cầm có nói khác không? → Không, `.docx` cùng phía với bản gốc.** Xem *Căn cứ chi tiết*.

**(2) Đối tác yêu cầu có khác bản gốc không? → Không khác.** Kết quả mong đợi trùng khớp cả bản gốc lẫn bản bàn giao; đối tác ghi nhận đúng.

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Ba ô người gửi bắt buộc dựng thêm rào chắn không có căn cứ trên hồ sơ đã định danh bằng đăng nhập. Ô mức ưu tiên bắt buộc vừa chặn gửi hồ sơ, vừa để bên nộp tự đặt thứ tự xử lý — trái Nghị định 55/2019/NĐ-CP Điều 4 Khoản 4, nơi ưu tiên là diện chính sách do hệ thống xét.

#### Căn cứ chi tiết

**(1b) Trích bản bàn giao `HTPLDN-PTYC-CT-v3.5.docx`:**
- §4.5.2.1 Phân quyền — "*Thông tin doanh nghiệp lấy theo tài khoản đang đăng nhập, **không nhập tay***".
- §4.5.2.2.2 Mô tả thông tin trên màn hình — bảng đúng **8 dòng**; "*Tên doanh nghiệp … **Chỉ đọc.** Hệ thống lấy theo hồ sơ doanh nghiệp của tài khoản đang đăng nhập*"; "*Mã số thuế … **Chỉ đọc.** Là định danh của doanh nghiệp trong hệ thống*".
- Quét toàn mục 4.5.2 (dòng 5692–5764) với các từ "kênh", "ưu tiên", "người gửi", "ghi chú" — **chỉ 1 chỗ khớp**, là gạch đầu dòng "*Tự xác định mức độ ưu tiên xử lý theo các tiêu chí ưu tiên có sẵn của doanh nghiệp*" ở §4.5.2.2.3. Bản bàn giao **không có** ô mức độ ưu tiên, ô lý do ưu tiên, ô thông tin người gửi và ô ghi chú trên biểu mẫu doanh nghiệp.

**(1) Chứng minh ngược khẳng định "bản gốc không có ô thông tin người gửi":** đã tra `srs-fr-05-vu-viec.md` với các biến thể `nguoi_gui`, `ten_nguoi`, `ho_ten`, `email_lien_he`, `sdt_lien_he`, "người liên hệ", "người gửi" — 10 chỗ khớp (`grep -cEi` trên tệp, chạy lại 13/08), **không chỗ nào** là ô nhập của vụ việc (đều là họ tên cán bộ/người xử lý, hoặc điểm liên hệ tổ chức tư vấn). Nhóm trường `nguoi_gui_id` / `ten_nguoi_gui` / `email_nguoi_gui` / `sdt_nguoi_gui` thuộc thực thể HOI_DAP của nhóm Hỏi đáp (`srs-v3.5.md:1524–1527`), không thuộc VU_VIEC. Đã đọc trọn mục FR-V.I-02 (`:160–224`) gồm cả Error Handling, Acceptance Criteria, Postconditions.

**→ Kết luận: Loại 1 — Lỗi phần mềm. Biểu mẫu gửi hồ sơ của doanh nghiệp phải bỏ 6 ô thừa (ba ô thông tin người gửi, mức ưu tiên, lý do ưu tiên, ghi chú) và hiển thị tên doanh nghiệp + mã số thuế ở dạng chỉ đọc lấy theo tài khoản đăng nhập. Dev action: Có · Sửa đặc tả: Có (tách chế độ doanh nghiệp ngay trong bảng thành phần SCR-V.I-02) → Sheet: Giữ xử lý.**  **✅ BA duyệt 13/08/2026.**

### Phương án xử lý (cập nhật SRS)

Bản gốc **đã đủ căn cứ để chốt đúng/sai** ở phần đặc tả chức năng (`:179`, `:187`, `:196`). Chỗ còn hở là phần Màn hình: `SCR-V.I-02` (`srs-fr-05-vu-viec.md:1679`) dùng chung cho hai chức năng — doanh nghiệp gửi hồ sơ (FR-V.I-02) và cán bộ nhập thủ công (FR-V.I-04) — nhưng **không dòng thành phần nào phân biệt theo chế độ người dùng**. Bảng có 23 dòng: 20 dòng ghi Điều kiện hiển thị "Luôn", 3 dòng còn lại có điều kiện nhưng đều là điều kiện **theo dữ liệu**, không phải theo chế độ — dòng 16 "Khi có file", dòng 21 "Khi hồ sơ có kênh = DVC", dòng 22 "Khi hồ sơ có kênh = HE_THONG_KHAC" (đọc cột cuối của cả 23 dòng bảng `:1687–1712`). Đây đúng là chỗ để lọt biểu mẫu hiện tại.

**Sửa thẳng trong bảng thành phần có sẵn, KHÔNG thêm khối mô tả mới.** Bảng đã có sẵn hai cột đủ sức diễn đạt khác biệt giữa hai chế độ — cột "Hành vi" và cột "Điều kiện hiển thị". Thêm một khối riêng kiểu `SCR-V.I-03 — Chế độ doanh nghiệp` là nặng hơn mức cần: khối đó tồn tại vì chế độ doanh nghiệp của màn chi tiết khác nhau ở cả bố cục và tập thao tác, còn ở đây khác biệt chỉ nằm ở mức từng ô. Thêm khối sẽ chép lại nội dung đã có ở Inputs FR-V.I-02 `:179–187`, và tạo thêm một bản sao phải giữ đồng bộ.

**8 việc** (7 việc BA duyệt 13/08 + 1 việc thêm bắt buộc phát sinh khi thi hành):

| # | Chỗ sửa | Sửa thành |
|---|---|---|
| 1 | dòng 4 bảng — nút [Tìm DN] (`:1692`) | Điều kiện hiển thị: chỉ chế độ cán bộ |
| 2 | dòng 5 — `ten_doanh_nghiep` (`:1693`) | Cột Hành vi ghi rõ hai chế độ: chế độ doanh nghiệp **chỉ đọc**, giá trị lấy theo tài khoản đăng nhập; chế độ cán bộ điền từ hộp thoại tìm/tạo DN |
| 3 | dòng 6 — `ma_so_thue` (`:1694`) | Như việc 2 |
| 4 | dòng 13 — `ghi_chu` (`:1701`) | Điều kiện hiển thị: chỉ chế độ cán bộ. **Không xoá trường khỏi thực thể** — `ghi_chu` là trường dùng chung của vụ việc (`srs-v3.5.md:975`), chỉ ẩn khỏi biểu mẫu doanh nghiệp |
| 5 | dòng 17–20 — cả nhóm "Thông tin Tiếp nhận" (`:1705–1708`) | Điều kiện hiển thị: chỉ chế độ cán bộ |
| 6 | mục Quy tắc tương tác của SCR-V.I-02 (`:1713`) | Thêm một dòng chốt **đúng 8 thành phần** của chế độ doanh nghiệp: **2 ô chỉ đọc** — tên doanh nghiệp, mã số thuế (lấy theo tài khoản đăng nhập) — và **6 ô nhập** — tiêu đề, loại hình hỗ trợ, lĩnh vực pháp luật, nội dung yêu cầu, vụ việc vướng mắc, tài liệu đính kèm. Nói rõ mức ưu tiên do hệ thống tự xác định, doanh nghiệp không nhập. **Đừng viết "7 trường theo Inputs"** — bảng Inputs có 7 dòng nhưng dòng đầu là định danh doanh nghiệp lấy từ phiên đăng nhập, không phải ô trên màn; đếm theo Inputs sẽ khiến người thi hành phân vân màn hình có 7 hay 8 thành phần. Con số 8 khớp đúng bảng 8 dòng ở `HTPLDN-PTYC-CT-v3.5.docx` §4.5.2.2.2 |
| 7 | dòng quy ước giao diện di động (`:1613`) | Danh sách màn hình phía doanh nghiệp hiện chỉ có SCR-V.I-03 chế độ DN, SCR-V.I-04, SCR-V.I-05 — **thiếu SCR-V.I-02**, dù đây chính là biểu mẫu doanh nghiệp gửi hồ sơ trên điện thoại. Bổ sung vào |
| 8 | dòng liệt kê màn hình phía doanh nghiệp ở đầu Mục 3 (`:1484`) | `[VIỆC THÊM BẮT BUỘC — phát sinh khi thi hành, sau lượt BA duyệt]` Đây là **danh sách thứ hai** cùng nội dung với việc 7. Sửa mỗi việc 7 thì hai danh sách nói ngược nhau — một bên có SCR-V.I-02, một bên không. Bổ sung SCR-V.I-02 chế độ doanh nghiệp vào đây cho khớp. Thuần kỹ thuật văn bản, không đổi nghiệp vụ |

**Doc action:** `HTPLDN-PTYC-CT-v3.5.docx` §4.5.2.2.2 hiện đã mô tả đúng chế độ doanh nghiệp — **không phát sinh việc gỡ hay thêm**. Chỉ rà lại ở lượt bàn giao kế tiếp để bảo đảm còn khớp.

*Rà phạm vi ảnh hưởng:* đã quét `srs-fr-05-vu-viec.md` theo các định danh — `SCR-V.I-02` 6 chỗ khớp, `uu_tien` 18 chỗ (gồm cả `ly_do_uu_tien` và `diem_uu_tien` do khớp chuỗi con), `ly_do_uu_tien` 7 chỗ, "chế độ doanh nghiệp / chế độ DN" 12 chỗ (`grep -c` từng định danh trên tệp, chạy lại 13/08). Không có bản sao của bảng thành phần SCR-V.I-02 ở `srs-v3.5.md`. Không phát sinh mã quy tắc mới, không đổi nhãn số đếm nào. Việc thêm ở đây là **ngoại lệ hiển thị theo chế độ**, cùng khuôn với SCR-V.I-03 đang dùng — không chọi dòng quy định chung nào.

---

## 2. GHSYCHTPL_06 — Vụ việc tạo xong nhưng không ghi dòng thời gian và không báo cho cán bộ

**Vấn đề:** Doanh nghiệp gửi hồ sơ thành công, vụ việc đã vào danh sách bên phần mềm của cán bộ, nhưng phần lịch sử xử lý của vụ việc để trống hoàn toàn và cán bộ nghiệp vụ không nhận được thông báo có hồ sơ mới. Hệ quả: hồ sơ nằm im chờ cán bộ tình cờ mở danh sách mới thấy, trong khi thời hạn trả lời 15 ngày làm việc vẫn chạy; đồng thời mất dấu vết ai tạo vụ việc — thứ cần có khi đối chiếu trách nhiệm về sau.

**Bóc ý con trong Kết quả mong đợi:**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Tự sinh mã vụ việc | Có — `:195` | Không tranh chấp — minh chứng cho thấy đã sinh `VV-BTP-TW-20260812-002` |
| Tự xác định mức ưu tiên; thiếu thông tin thì áp mức thấp nhất theo thứ tự tiếp nhận | Có — `:196` + BR-CALC-07 `:2424–2443` | Không tranh chấp — minh chứng hiển thị "1 — Mức thường — xét theo thứ tự nộp hồ sơ" |
| Tạo hồ sơ ở trạng thái "Mới tạo" và lưu tài liệu đính kèm | Có — `:197` và `:198` | Không tranh chấp, chờ chạy để đo — minh chứng xác nhận tệp đính kèm đã tải lên; badge trạng thái không lọt vào khung hình |
| Ghi lịch sử vụ việc với hành động tạo vụ việc, vai trò doanh nghiệp | Có — `:199` | (1) — **hỏng** |
| Gửi thông báo cho cán bộ nghiệp vụ | Có — `:200` | (1) — **hỏng** |

**(1) Phần mềm đúng bản gốc chưa? → SAI, ở hai bước cuối.**
- `srs-fr-05-vu-viec.md:199` — bước 7: "*Ghi LICH_SU_VU_VIEC: hanh_dong='TAO_VV', vai_tro='DN'*", quy tắc BR-DATA-05.
- `srs-fr-05-vu-viec.md:200` — bước 8: "*Gửi thông báo cho CB NV đơn vị theo `DOANH_NGHIEP.tinh_thanh_id`*… *Nếu vẫn không xác định được … → gửi cho TW (Bộ Tư pháp) phân loại lại*", quy tắc BR-NOTIF-01. Nhánh dự phòng đã phủ mọi trường hợp thiếu dữ liệu, nên không có cớ bỏ qua bước này.
- Minh chứng `GHSYCHTPL_06.webm`: khung 00:19 — màn chi tiết vụ việc vừa tạo, mục **Dòng thời gian rỗng** (hiển thị trạng thái trống). Khung 00:13 — chuông thông báo của Cán bộ NV Trung ương, 5 mục gần nhất đều là việc khác (đăng nhập nơi khác, phê duyệt vụ việc cũ, hồ sơ tư vấn viên, nộp báo cáo đợt), **không có mục nào báo hồ sơ mới**.

**(1b) Bản bàn giao có nói khác không? → Không.** `HTPLDN-PTYC-CT-v3.5.docx` §4.5.2.2.3 dòng 1 liệt kê đủ hai gạch đầu dòng "*Ghi lịch sử vụ việc với hành động tạo vụ việc, vai trò doanh nghiệp*" và "*Gửi thông báo cho cán bộ nghiệp vụ của đơn vị tiếp nhận theo tỉnh, thành phố của doanh nghiệp*". Kết quả mong đợi của đối tác chép gần nguyên văn từ đây.

**(2) Đối tác yêu cầu có khác bản gốc không? → Không khác.**

**(3) Có bắt buộc cho luồng nghiệp vụ không? → CÓ.** Thiếu thông báo thì hồ sơ không được tiếp nhận đúng lúc, trong khi thời hạn 15 ngày làm việc theo Nghị định 55/2019/NĐ-CP Điều 8 Khoản 1 đã bắt đầu. Thiếu lịch sử vụ việc thì mất dấu vết hành chính bắt buộc theo BR-DATA-05, và Dòng thời gian ở màn chi tiết vụ việc (`srs-fr-05-vu-viec.md:1744`) không có gì để hiển thị.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo bản gốc: khi doanh nghiệp gửi hồ sơ thành công phải ghi lịch sử vụ việc (hành động tạo vụ việc, vai trò doanh nghiệp) và gửi thông báo cho cán bộ nghiệp vụ đơn vị tiếp nhận, có nhánh dự phòng về Trung ương khi chưa xác định được đơn vị. Dev action: Có · Sửa đặc tả: Không → Sheet: Giữ xử lý.**

*Không có phản hồi gửi đối tác — Dev sửa toàn bộ, ghi nhận của đối tác đúng.*

---

## 3. Phát hiện nội bộ — Kênh tiếp nhận của hồ sơ do doanh nghiệp tự gửi

> **Đây KHÔNG phải lỗi đơn vị kiểm thử nêu, và kết luận là phần mềm ĐÚNG.** Không mã test case nào báo điểm này. Chính bước thực hiện của GHSYCHTPL_06 hướng dẫn *"Áp dụng bộ lọc «Kênh tiếp nhận = Hệ thống khác»"* — đơn vị kiểm thử dùng đúng bộ lọc đó và không than phiền. Mục này ghi lại để lưu vết một điểm đã tra và đã khép, **không sinh việc cho ai**.

**Nội dung phát hiện:** Hồ sơ doanh nghiệp tự nộp trên chuyên trang đang được xếp vào kênh "Hệ thống khác". Ban đầu tôi ngờ đây là chỗ hở của bản gốc và đề xuất mở thêm một kênh riêng. Tra Danh sách UC/Transaction thì thấy ngược lại — bản gốc không hở, và phần mềm đang làm đúng.

**(1) Phần mềm đúng bản gốc chưa? → ĐÚNG.**
- `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv` — nhóm **V. Quản lý vụ việc trợ giúp pháp lý** (dòng 248–393, 32 chức năng) có **8 loại tác nhân**, **không có Cổng Pháp luật Quốc gia** (đếm cột Tác nhân của 32 dòng chức năng): Cán bộ nghiệp vụ 18 lần · Doanh nghiệp 3 · Hệ thống giải quyết thủ tục hành chính BTP 3 · Cán bộ nghiệp vụ hoặc Cán bộ phê duyệt 2 · Người hỗ trợ 2 · Cán bộ phê duyệt 2 · Cán bộ nghiệp vụ hoặc Doanh nghiệp 1 · Tư vấn viên 1.
- Cổng Pháp luật Quốc gia **chỉ làm tác nhân ở nhóm X** (Tư vấn chuyên sâu với chuyên gia) — STT 149, 151, 153, 158, đều là Cổng chuyển dữ liệu sang. Danh sách UC không giao cho Cổng vai trò nào trong luồng vụ việc.
- Vì vậy vụ việc **không có kênh tiếp nhận mang tên Cổng**. Hồ sơ doanh nghiệp nộp trên chuyên trang đi vào phần mềm cán bộ theo đúng đường "hệ thống khác chuyển sang", và tập 5 giá trị hiện có (`srs-fr-05-vu-viec.md:2030`) đã đủ.
- Minh chứng `GHSYCHTPL_06.webm` khung 00:19 hiển thị "Kênh tiếp nhận: Hệ thống khác" — khớp.

**(1b) Bản bàn giao có nói khác không? → Không.** Quét toàn mục 4.5.2 của `HTPLDN-PTYC-CT-v3.5.docx` (dòng 5692–5764) với từ "kênh" — 0 chỗ khớp. Bản bàn giao không gán kênh nào cho luồng này, không mâu thuẫn với bản gốc.

**(2) Đối tác yêu cầu có khác bản gốc không? → Đối tác không nêu điểm này.** Bước thực hiện của họ còn dùng đúng kênh "Hệ thống khác".

**(3) Có bắt buộc cho luồng nghiệp vụ không? → Không đặt ra.** Không có sai lệch nào để xử.

**→ Kết luận: Phần mềm ĐÚNG. Danh sách UC/Transaction không đặt Cổng Pháp luật Quốc gia làm tác nhân của vụ việc, nên không mở thêm kênh tiếp nhận nào; tập 5 giá trị hiện có giữ nguyên. Dev action: Không · Sửa đặc tả: Không · Doc action: Không → Sheet: không đụng (điểm này không thuộc mã test case nào).**  **✅ BA chốt 13/08/2026.**

*Không có phản hồi gửi đối tác — đối tác không nêu điểm này và ghi nhận của họ không có gì sai.*

*Lịch sử: mục này bị đảo kết luận 1 lần — ban đầu đề xuất bổ sung kênh Cổng Pháp luật Quốc gia, sau khi tra Danh sách UC/Transaction thì bỏ hẳn phương án đó.*

## Cập nhật sổ theo dõi

Chưa ghi gì lên sổ. Cả hai mã đều còn việc của Dev nên **không đổi trạng thái** — người đổi là QA hoặc Dev sau khi làm xong (Pha 5, vế 1 là "có").

| Mã | Dòng sổ (bản tải 13/08) | Trạng thái dev fix | DEV phản hồi lần 1 |
|---|---|---|---|
| GHSYCHTPL_02 | 499 | Để nguyên | Để trống |
| GHSYCHTPL_06 | 503 | Để nguyên | Để trống |

> Trước khi ghi (nếu về sau có ghi): tải lại sổ, khớp dòng bằng cột Mô tả + Kết quả mong đợi, và tra tập giá trị đang dùng ở cột trạng thái — sổ hiện dùng chuỗi `Resoved` (thiếu chữ `l`), phải ghi đúng chuỗi đó chứ không ghi theo chính tả đúng.

## Điểm treo chuyển đợt sau

| Nội dung | Phát hiện ở mục nào | Thuộc bên nào | Trạng thái |
|---|---|---|---|
| Tách chế độ doanh nghiệp trong bảng thành phần SCR-V.I-02 — 7 việc | Mục 1, Phương án xử lý | Người sửa đặc tả (thi hành ở đợt riêng) | Đã chốt 13/08/2026, chờ mở đợt sửa đặc tả |
| Trạng thái "Mới tạo" của vụ việc vừa tạo chưa lọt vào khung hình minh chứng | Mục 2, bảng bóc ý con | QA | Chờ chạy để đo |
