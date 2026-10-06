# BA confirmation needed — 6 dòng còn treo `BA confirm` sau đợt duyệt 08–09/08 — 2026-08-10

> **File này để làm gì:** gom các dòng tab `bug` vẫn ở `Trạng thái dev fix = BA confirm` **sau khi** đã áp xong mọi quyết định của phiếu 34 điểm (BA duyệt 08–09/08) và phiếu phản hồi DEV 05/08. Mỗi dòng kèm đối chiếu SRS + số đo lại trên bản dựng hiện hành để BA quyết nhanh.

**Đã loại trừ trước khi đưa vào đây.** Đối chiếu cả 4 phiếu BA — `phan-hoi-ba-34-diem-tuan-5-2026-08-07.md`, `phan-hoi-TONG-HOP-reject-2026-08-05.md`, `phan-hoi-ba-7-diem-can-chot-2026-08-06.md`, `phan-hoi-ba-QLNDTVVCG-OOS-02-04-2026-08-06.md` — **không phiếu nào quyết 6 điểm dưới đây**. Bản SRS giao 10/08 có **91 dấu `[BA duyệt 2026-08-08]` / `[BA duyệt 2026-08-09]` nằm trong 12 file**, nhưng đã soi từng dấu: đều thuộc các mục khác của phiếu 34 điểm, **không dấu nào chạm 6 câu hỏi này**.

**Vân tay bản dựng của mọi phép đo trong file.**

| Mục | Giá trị |
|---|---|
| Env | `https://18.143.165.120.nip.io` (nội bộ) |
| Bó mã FE | `assets/index-LoDAkSbB.js` |
| `last-modified` / `etag` | `Fri, 07 Aug 2026 15:26:56 GMT` · `W/"6a75f940-428"` |
| Chuỗi chân thanh bên | `HTPLDN · V1.0.10` — **không dùng làm vân tay**, chỉ ghi kèm |
| Thời điểm đo | 10/08/2026 (giờ VN) |
| Tài khoản cán bộ | `cbnv_tw` / `Test@1234` → `CB_NV_TW`, đơn vị `00000000-0000-4000-8000-000000000001` |
| Tài khoản doanh nghiệp | `0209888006` / `Test@1234` → vai trò `DN`, `doanhNghiepId c03a66bc-f584-437d-89c8-1371f6a69772`, đơn vị quản lý `00000000-0000-4000-8002-000000000006` (Sở Tư pháp An Giang) |

> ⚠️ **Bản dựng đã đổi so với gói hỏi ngày 07/08.** Các lượt đo gửi BA hôm 07/08 chạy trên `index-D4Buvu4S.js` / `index-DsMHK7Dp.js` / `index-B2W2Krcs.js`; tối 07/08 có bản mới lên và vẫn là bản đang chạy. **Ba câu hỏi đã đổi dữ kiện, không còn giống nội dung gói 07/08** — đánh dấu 🔄 ở bảng dẫn.

---

## Bảng dẫn — 5 điểm cần BA, phủ 6 dòng

| # | Dòng | Mã TC | Dạng | Điểm cần BA | Đổi so với gói 07/08 |
|---|---|---|---|---|---|
| 1 | 20 | `QLLKHDTBD_09` | B | Tệp Xuất Excel Kế hoạch đào tạo **gồm những cột nào** — có "Người tạo"/"Ngày tạo" không | — |
| 2 | 64 | `DGKQHTVV_01` | B | DN có được thấy vụ việc **mình sở hữu nhưng đơn vị khác xử lý** không | 🔄 điểm này **chưa từng** nằm trong gói 13 dòng |
| 3 | 65 | `DGKQHTVV_02` | B | 4 câu về nhóm Đánh giá: nhãn · 2 trường Người/Ngày đánh giá · tiêu chí không bẻ vỡ giá trị · số thập phân | 🔄 vế "bẻ vỡ giá trị" nay **đã tái hiện được, có ảnh** |
| 4 | 338 + 339 | `LBCKQTHCT_05` · `_06` | B | Điều kiện hiển thị 2 khối ở màn Chi tiết đợt neo vào **trạng thái đợt** hay **có dữ liệu** | 🔄 bản mới **đã hiện đủ 2 khối**, ngược hẳn lượt đo 07/08 |
| 5 | 342 | `GKQTHCTHTPL_01` | B | Trạng thái ở màn Chi tiết đợt là của **ĐỢT** hay của **ĐƠN VỊ** | — |

> **Ưu tiên trả lời:** điểm **2** (chặn hẳn một nhánh nghiệp vụ của DN, đang là Reopen) và điểm **4** (bản mới đã đổi hành vi, để lâu thì lượt đo lại lệch tiếp).

> **Dòng thứ 7 đang treo `BA confirm` — `QLCHTHXLHS_02` (dòng 151) — KHÔNG nằm trong file này.** BA đã chốt việc đó từ **07/05/2026** và đặc tả hiện hành đã ghi đúng, nên không có gì để quyết; đưa vào đây chỉ khiến một dòng đóng được ngay phải nằm chờ cùng 5 điểm trên. Kết luận + căn cứ + nội dung đề nghị BA phản hồi đối tác tách sang [`ket-luan-QLCHTHXLHS_02-khong-phai-loi-2026-08-10.md`](ket-luan-QLCHTHXLHS_02-khong-phai-loi-2026-08-10.md).

---

<!-- ===================== 1 ===================== -->

## `QLLKHDTBD_09` (dòng 20) — Tệp Xuất Excel Kế hoạch đào tạo gồm những cột nào

**Bối cảnh testcase**

- Dòng Excel: 20, mã TC `QLLKHDTBD_09`.
- Nội dung kiểm tra: CB Nghiệp vụ mở *Đào tạo, tập huấn → Kế hoạch đào tạo*, nhập tiêu chí lọc rồi bấm **Xuất Excel**.
- Expected trong file UAT: *"Hệ thống xuất danh sách theo điều kiện lọc hiện tại ra tệp Excel."*
- Actual đối tác ghi: *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách."*
- Ô `TKM phản hồi lần 1`: *"File excel được xuất **thiếu trường thông tin Người tạo, Ngày tạo**."*

**Kết quả verify UI hiện tại**

- Đo 10/08/2026 bằng Chrome DevTools MCP, tài khoản `cbnv_tw`, màn `/dao-tao/ke-hoach/danh-sach`.
- **Vế "xuất theo bộ lọc" — ĐÃ HẾT LỖI.** Gọi đúng nút Xuất Excel của màn (`POST /api/v1/ke-hoach-dao-taos/export`), giải nén tệp trả về rồi đếm dòng thực:
  - không đặt bộ lọc → danh sách 14 bản ghi → tệp **đúng 14 dòng**;
  - lọc `Trạng thái = Đã duyệt` → tệp **đúng 4 dòng**.
  - Nếu chức năng bỏ qua bộ lọc thì cả hai tệp đã phải cùng 14 dòng ⇒ triệu chứng đối tác nêu **không tái hiện**.
- **Vế danh mục cột — vẫn nguyên.** Hàng tiêu đề tệp xuất có đúng **7 cột**: `Mã KH | Tên kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái`. Không có cột nào mang nghĩa người lập hay ngày lập bản ghi.
- Đối chiếu: bảng **trên màn** thì có đủ 12 cột, trong đó **có** "Người tạo" và "Ngày tạo". Khoảng trống chỉ nằm ở tệp Excel.

**Điểm mâu thuẫn trong SRS v3.5**

1. Bảng thành phần màn hình của Kế hoạch đào tạo **CÓ** hai cột này:
   - "Người tạo | Họ tên cán bộ tạo"
   - "Ngày tạo | dd/mm/yyyy"

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1795`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1796`

2. Nhưng §Outputs của chính FR-III-14 (Lập kế hoạch đào tạo năm) **KHÔNG** có hai trường này — chỉ 8 trường `id · ten_ke_hoach · nam · thoi_gian · ngan_sach_du_kien · so_ctdt · trang_thai · total_count`. Và §Processing của nút Xuất Excel chỉ nói *"Lấy danh sách theo filter, tối đa 10.000 dòng"*, **không** khai danh mục cột của tệp.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1090` (FR-III-14)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1189` (§Outputs — Danh sách)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1175` (§Processing — Xuất Excel)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1775` (nút Xuất Excel — *"xuất danh sách KH theo bộ lọc"*)

⇒ Chữ **"danh sách"** trong câu *"xuất danh sách KH theo bộ lọc"* đang có hai nghĩa: danh sách **trên màn** (12 cột) hay §Outputs của FR (8 trường). Phần mềm đang hiểu theo nghĩa thứ hai.

**Câu hỏi cần BA xác nhận**

Tệp Excel xuất từ màn Kế hoạch đào tạo phải gồm những cột nào — theo bảng trên màn hay theo §Outputs của FR-III-14?

1. **Hướng 1 — theo bảng trên màn:** tệp phải có thêm "Người tạo" và "Ngày tạo" ⇒ **là lỗi**, Dev BE bổ sung cột; đề nghị BA bổ sung bảng "Outputs — Tệp Xuất Excel" vào FR-III-14 để lần sau không phải hỏi lại.
2. **Hướng 2 — theo §Outputs của FR:** 7 cột hiện tại là đủ ⇒ **không phải lỗi**; đề nghị BA vẫn khai bảng danh mục cột vào FR-III-14 và đề nghị đối tác cập nhật lại ô "Kết quả thực tế".

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt danh mục cột.
- Tạm verdict `QLLKHDTBD_09`: `Cần BA xác nhận` cho vế cột; vế "xuất theo bộ lọc" thì **đã hết lỗi**, đề nghị ghi nhận riêng để không kéo cả dòng.
- Nếu BA chọn hướng 1: owner `Dev BE`. Nếu chọn hướng 2: `Không phải bug theo SRS`, đối tác cập nhật "Kết quả thực tế".

---

<!-- ===================== 2 ===================== -->

## `DGKQHTVV_01` (dòng 64) — Doanh nghiệp có thấy vụ việc mình sở hữu nhưng đơn vị khác xử lý không

**Bối cảnh testcase**

- Dòng Excel: 64, mã TC `DGKQHTVV_01`.
- Nội dung kiểm tra: CB Nghiệp vụ **hoặc DNNVV** mở *Vụ việc HTPL → Xem chi tiết → Nhóm 8 – Đánh giá* để đánh giá chất lượng hỗ trợ.
- Actual đối tác ghi: *"Hệ thống không hiển thị nút chức năng mặc dù bản ghi ở trạng thái phù hợp."*
- Ô `DEV phản hồi lần 1` đang ghi `⏸ CHỜ BA CONFIRM — Dev chưa sửa code`, kèm nguyên nhân gốc: **doanh nghiệp bị lọc theo ĐƠN VỊ XỬ LÝ trước khi lọc theo CHỦ SỞ HỮU**.

> **Vì sao gửi lại điểm này.** Quyết định BA 09/08 mục 25 (Hướng A — hai bên đánh giá độc lập) **đã vào SRS** và chính phiếu đó ghi *"verdict `DGKQHTVV_01` giữ **Reopen** (đang Reopen vì nhánh doanh nghiệp, mục này không đổi verdict đó)"*. Tức mục 25 **không** trả lời câu hỏi phạm vi mà Dev đang chặn. Câu hỏi phạm vi cũng **không** nằm trong gói 13 dòng gửi BA hôm 07/08 — đây là lần đầu nó được đặt thành một điểm riêng.
>
> Citation phần đã duyệt: `srs-fr-05-vu-viec.md:1753` · `:2302` · `:1234` (đều mang dấu `[DGKQHTVV_01 … BA duyệt 2026-08-09]`).

**Kết quả verify UI hiện tại**

- Đo 10/08/2026, đăng nhập bằng **chính tài khoản doanh nghiệp** `0209888006` (không dùng tài khoản cán bộ để ra kết luận).
- **Nhánh cùng đơn vị — ĐÃ CHẠY.** Mở vụ việc `VV-STP-AG-20260806-005` (trạng thái *Đã đánh giá*, do Sở Tư pháp An Giang xử lý): DN vào được chi tiết, có nhóm **"Đánh giá"**, có nút **[Đánh giá]**, không dính 403.
- **Nhánh khác đơn vị — VẪN HỎNG.** Đối chiếu số:

  | Đo bằng | Số vụ việc của DN `c03a66bc…` |
  |---|---|
  | Chính tài khoản DN | **8** |
  | Tài khoản cán bộ, lọc theo `doanhNghiepId` của DN đó | **9** |

  Bản ghi chênh là `VV-QA-NR-KTH13-20260805` — `doanhNghiepId` đúng của DN này, nhưng đơn vị xử lý là `00000000-0000-4000-8000-000000000001` (Trung ương). Mở thẳng bản ghi đó bằng phiên DN → **404 `ERR-VAL-VI-03-02`**.
- ⇒ Hiện trạng khớp đúng nguyên nhân gốc Dev nêu: DN bị lọc theo đơn vị xử lý, nên vụ việc của chính mình do đơn vị khác xử lý thì **không nhìn thấy, không mở được, không có đường vào nhóm Đánh giá**.

**Điểm mâu thuẫn trong SRS v3.5**

1. Tiền điều kiện của chính chức năng đánh giá (UC67) chỉ kiểm **quyền sở hữu**, không nhắc đơn vị:
   - *"DN truy cập là chủ sở hữu của VU_VIEC (`VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id`)"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1274`

2. Nhưng quy tắc phân quyền dữ liệu cho DN lại đặt **lọc kép** — đơn vị **và** định danh DN:
   - *"Hệ thống lọc theo đơn vị quản lý DN + định danh DN (lấy từ token VNeID)"*
   - *"API lọc theo `don_vi_id` (Sở TP quản lý DN) + `doanh_nghiep_id`"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:842` (khối *DN — lọc tầng dữ liệu (BR-AUTH-11)*)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5542` (bảng BR-AUTH-11)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:506`

⇒ Ngay cả khi đọc BR-AUTH-11 theo nghĩa có lợi nhất — "đơn vị **quản lý DN**" là thuộc tính của doanh nghiệp chứ không phải của vụ việc — thì đặc tả vẫn **không nói** phải làm gì khi vụ việc của DN được một đơn vị khác thụ lý. Đây đúng là chỗ im lặng khiến QA không tự chốt được.

**Câu hỏi cần BA xác nhận**

Doanh nghiệp có được xem — và đánh giá — vụ việc **do chính mình sở hữu** nhưng **đơn vị khác thụ lý** (ví dụ Trung ương xử lý vụ việc của DN thuộc Sở Tư pháp An Giang) hay không?

1. **Hướng 1 — theo tiền điều kiện UC67:** DN thấy **mọi** vụ việc mình sở hữu, bất kể đơn vị nào xử lý; đơn vị chỉ dùng để phân luồng nghiệp vụ, không dùng để che dữ liệu khỏi chủ sở hữu ⇒ hiện trạng **là lỗi**, owner `Dev BE`.
2. **Hướng 2 — theo BR-AUTH-11:** DN chỉ thấy vụ việc do đơn vị quản lý mình thụ lý ⇒ hiện trạng **đúng**, nhưng khi đó cần BA nói rõ ai đánh giá thay DN với những vụ việc do đơn vị khác xử lý, vì UC67 vẫn ghi DN là một trong hai bên đánh giá.

**Kèm theo, nếu BA chọn Hướng 1 — xin chốt luôn phạm vi đọc.** Để DN thực sự đánh giá được thì ngoài bảng vụ việc còn phải mở quyền đọc có điều kiện cho hồ sơ/tài liệu, kết quả hỗ trợ và bản đánh giá. Đây là thay đổi phân quyền nhiều bảng nên xin BA xác nhận cả ba điểm:

1. DN thấy mọi vụ việc mình sở hữu, bất kể đơn vị xử lý;
2. DN đọc đủ dữ liệu con mà SRS cho phép để tải tài liệu, xem kết quả và đánh giá; vẫn **chặn tuyệt đối** dữ liệu của DN khác;
3. Giữ nguyên đơn vị xử lý theo cán bộ lập, **không** sửa/backfill dữ liệu cũ.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt phạm vi — vì fix đúng gốc là đổi phân quyền nhiều bảng, không phải sửa một nút giao diện.
- Tạm verdict `DGKQHTVV_01`: giữ **`Reopen`** đúng như phiếu 34 điểm đã ghi.
- Nếu BA chọn hướng 1: owner `Dev BE`, mức Major. Nếu chọn hướng 2: cần BA cấp thêm câu trả lời về ai đánh giá thay DN.

---

<!-- ===================== 3 ===================== -->

## `DGKQHTVV_02` (dòng 65) — Nhóm Đánh giá: nhãn, 2 trường, tiêu chí bẻ vỡ giá trị, số thập phân

**Bối cảnh testcase**

- Dòng Excel: 65, mã TC `DGKQHTVV_02`.
- Nội dung kiểm tra: mở *Vụ việc HTPL → Xem chi tiết → Nhóm 8 – Đánh giá*, kiểm hiển thị các trường.
- Expected trong file UAT: *"hiển thị các trường thông tin giống với thiết kế · đúng định dạng và trường thông tin · **không bị tràn/đè lên nhau**, đồng nhất ngôn ngữ hiển thị"*.
- Ô "Kết quả thực tế" của đối tác **để trống** và **không có ảnh** ⇒ tiền đề tái hiện suy từ "Điều kiện" + "Các bước" ghi trên phiếu.

**Kết quả verify UI hiện tại**

- Đo 10/08/2026, tài khoản `cbnv_tw`, vụ việc `VV-BTP-TW-20260806-003` (trạng thái *Đã đánh giá*, đã có 1 bản đánh giá của CB Nghiệp vụ).
- Nhóm "Đánh giá" hiển thị 7 ô, nhãn **tiếng Việt** đầy đủ: `Điểm chất lượng tư vấn 9/10` · `Điểm đúng thời hạn 8/10` · `Điểm thái độ phục vụ 10/10` · `Điểm tổng (trung bình 3 điểm)` · `Người đánh giá` · `Ngày đánh giá 06/08/2026 16:34` · `Nhận xét`.
- 🔴 Ô **"Điểm tổng (trung bình 3 điểm)"** bị **bẻ giá trị giữa chừng**: cột hẹp nên `9/10` xuống dòng thành **`9/1`** ở dòng trên và **`0`** ở dòng dưới. Ba ô điểm thành phần cùng khuôn `x/10` thì không bị.
- Ba ô còn lại không tràn, không đè; trang không cuộn ngang.
- Evidence: `image/DGKQHTVV_02-diem-tong-be-dong-2026-08-10.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Bảng thành phần màn hình của nhóm Đánh giá chỉ liệt **mã kỹ thuật**, đúng 5 mục, **không có** "Người đánh giá" và "Ngày đánh giá":
   - *"diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:1735`

2. Nhưng thực thể dữ liệu của bản đánh giá **CÓ** hai trường đó, và giao diện đang hiển thị chúng:

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2118` (`nguoi_danh_gia_id`)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2125` (`ngay_danh_gia`)

3. Về tiêu chí "không tràn / không bẻ vỡ giá trị": **đã quét toàn bộ SRS v3.5**, cả bộ đặc tả chỉ có **một** chỗ duy nhất đặt luật này, và là luật riêng cho **một** chip trên màn Tổng quan chứ không phải luật chung:
   - *"Khi text > 25 ký tự → truncate với ellipsis '…' + tooltip hiển thị full name khi hover"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-01-dashboard.md:718`

   ⇒ Đặc tả có tiền lệ đặt luật hiển thị **theo từng thành phần**, nhưng **không có** luật chung cho mọi màn — nên không có căn cứ để chấm ô "Điểm tổng".

4. Về số thập phân: `diem_tong` được định nghĩa là trung bình cộng 3 điểm (`AVG`), thang 0–10, **không kèm quy tắc làm tròn**. Quy tắc làm tròn 1 chữ số duy nhất trong SRS là của **điểm trung bình tư vấn viên**, thang 1–5, thuộc chức năng khác.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2123` (`diem_tong` = AVG, không có quy tắc làm tròn)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md:2467` (làm tròn 1 chữ số — thang 1–5, của FR-IV-CROSS-01, **không áp cho UC67**)

**Câu hỏi cần BA xác nhận** — 4 câu, xin trả lời rời từng câu

1. **Bộ nhãn nhóm Đánh giá.** Bộ nhãn tiếng Việt đang chạy (*Điểm chất lượng tư vấn / Điểm đúng thời hạn / Điểm thái độ phục vụ / Điểm tổng (trung bình 3 điểm) / Nhận xét*) có được chốt làm nhãn chính thức để BA ghi vào bảng thành phần màn hình không, hay BA cấp bộ nhãn khác?
2. **Hai trường "Người đánh giá" / "Ngày đánh giá".** Bổ sung vào bảng thành phần màn hình (giao diện đã có, dữ liệu đã có) — hay gỡ khỏi giao diện?
3. 🔴 **Tiêu chí bẻ vỡ giá trị.** SRS **có** đặt yêu cầu "giá trị hiển thị không bị bẻ giữa chừng" cho vùng nhóm chi tiết vụ việc không?
   - **Có** ⇒ ô "Điểm tổng" đang bẻ `9/10` thành `9/1` + `0` là **lỗi thật**, owner `Dev FE`, mức Minor.
   - **Không** ⇒ **không phải lỗi**; đề nghị BA nói rõ để đối tác chỉnh lại vế "không bị tràn" trong ô Kết quả mong đợi, tránh mỗi đợt lại treo.
4. **Số thập phân của Điểm tổng.** Hiển thị mấy chữ số và làm tròn ra sao? Lượt đo này rơi đúng trường hợp trung bình ra số nguyên (`(9+8+10)/3 = 9`) nên chưa lộ được quy tắc.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA trả lời **câu 3** — đây là câu duy nhất có thể biến thành lỗi dev thật.
- Tạm verdict `DGKQHTVV_02`: `Cần BA xác nhận`.
- Nếu BA trả lời câu 3 là **Có**: owner `Dev FE`, mức Minor, gộp cùng lần sửa giao diện nhóm Đánh giá. Nếu **Không**: `Không phải bug theo SRS`, đối tác cập nhật Kết quả mong đợi.

---

<!-- ===================== 4 ===================== -->

## `LBCKQTHCT_05` (dòng 338) + `LBCKQTHCT_06` (dòng 339) — Điều kiện hiển thị 2 khối ở màn Chi tiết đợt báo cáo

**Bối cảnh testcase**

- Dòng Excel: 338, mã TC `LBCKQTHCT_05` — khối **Nhận xét, kiến nghị**.
- Dòng Excel: 339, mã TC `LBCKQTHCT_06` — khối **truy vết Chương trình HTPL liên quan**.
- Nội dung kiểm tra: mở *Đợt báo cáo → Trang Chi tiết đợt báo cáo* (đúng 2 bước, **không** bấm [Lập báo cáo]).
- Actual đối tác ghi: *"Màn hình Chi tiết không có Khối nhận xét, kiến nghị"* · *"Màn hình Chi tiết không có Khối truy vết chương trình liên quan"*.

> 🔄 **Dữ kiện đã đổi so với gói hỏi 07/08.** Lượt đo 07/08 (bản dựng cũ) tái hiện đúng quan sát của đối tác — hai khối **không** hiện. Lượt đo 10/08 trên bản dựng hiện hành thì **hiện đủ cả hai**. Câu hỏi vì thế đổi trọng tâm: không còn là "có phải hiện chỉ-đọc không", mà là **điều kiện hiển thị neo vào cái gì**.

**Kết quả verify UI hiện tại**

- Đo 10/08/2026, tài khoản `cbnv_tw`, màn `/ct-htpldn/dot-bao-cao/<id>`.
- Đợt `DOT-THBC01-UAT` — trạng thái **`Tạo đợt`** (bước 1/6 trên thanh tiến trình), tức **chưa** vào bước lập báo cáo.
- Màn Chi tiết hiển thị đủ, theo thứ tự: *Thông tin đợt* → *Tiến độ nộp theo đơn vị* → *Biểu mẫu 21a/TP/HTPLDN* (13 chỉ tiêu có số liệu) → **"Nhận xét, kiến nghị"** (nội dung *"Đơn vị hoàn thành các chỉ tiêu đề ra trong kỳ."*) → **"Chương trình HTPL liên quan trong kỳ"** (*"Tùy chọn — dùng để truy vết các chương trình đơn vị đã triển khai trong kỳ báo cáo."*, giá trị hiện `—`).
- Kiểm chéo 2 đợt còn lại (`DOT-SO_BO_NAM-2026-1`, `DOT-SO_BO_6_THANG-2026-1`, đều *Đã tổng hợp*): dữ liệu trả về đều mang cả `nhanXet` lẫn `ctHtplIdsLienQuan`.
- ⚠️ **Chưa loại trừ được một khả năng:** đợt đang đo **đã có sẵn dữ liệu báo cáo** (2 đơn vị đã nộp, biểu mẫu đã có số). Nên chưa phân biệt được hai khối hiện **vì đợt đã có báo cáo** hay **vì trạng thái đợt**. Đây đúng là chỗ cần BA chốt — QA cố ý không suy đoán.
- Evidence: `image/LBCKQTHCT_05-06-chi-tiet-dot-tao-dot-2026-08-10.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. Bảng thành phần màn hình neo điều kiện hiển thị vào **trạng thái đợt**, và chỉ nêu ô ở dạng **nhập liệu**:
   - *"| 39 | form | Nhan xet kien nghi | textarea | Max 5000 ky tu | input | **khi dot o DANG_LAP_BC** |"*
   - Hai ô biểu mẫu 21a/21b cùng khuôn: *"khi bieu mau ap dung va dot o DANG_LAP_BC"*.
   - ⇒ Đọc theo bảng này thì ở trạng thái `TAO_DOT` **không** có ô nào — trái với cái đang chạy.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1169` (khối Nhận xét, kiến nghị)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1167` · `:1168` (biểu mẫu 21a/21b, cùng khuôn điều kiện)

2. Còn khối **Chương trình HTPL liên quan** thì **bảng thành phần màn hình không khai dòng nào cả** — nó chỉ tồn tại ở phần dữ liệu và bước xử lý:
   - *"CB NV nhập/chỉnh sửa số liệu + nhận xét, kiến nghị; có thể chọn `ct_htpl_ids_lien_quan[]` để truy vết"*
   - *"`ct_htpl_ids_lien_quan[]` … truy vết các CT đơn vị đã triển khai trong kỳ (tham khảo, không bắt buộc)"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:744` (§Processing bước 6)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:732` (§Inputs)
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1417` (thực thể)

   ⇒ Đây đúng khuôn **UI-12** mà BA đã dùng cho `QLTLPLCVV_22`: mục **có** căn cứ ở §Processing nhưng **bị sót** ở bảng thành phần màn hình ⇒ bảng sót, phần mềm đúng. Xin BA xác nhận có áp cùng khuôn ở đây không.

**Câu hỏi cần BA xác nhận**

Ở màn **Chi tiết đợt báo cáo**, hai khối "Nhận xét, kiến nghị" và "Chương trình HTPL liên quan" hiển thị theo điều kiện nào?

1. **Hướng 1 — neo vào trạng thái đợt (đúng chữ bảng thành phần màn hình):** chỉ hiện khi đợt ở `DANG_LAP_BC`. ⇒ Bản đang chạy hiện chúng ở `TAO_DOT` là **sai**, owner `Dev FE`; và quan sát của đối tác ở bản cũ là đúng.
2. **Hướng 2 — neo vào việc đã có dữ liệu báo cáo:** hễ đợt đã có báo cáo thì hiện ở dạng **chỉ đọc** tại mọi trạng thái, chỉ cho sửa khi ở `DANG_LAP_BC`. ⇒ Bản đang chạy **đúng**, đề nghị BA bổ sung điều kiện hiển thị chỉ-đọc vào bảng thành phần màn hình và khai thêm dòng cho khối Chương trình liên quan (đang bị sót hẳn).

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt điều kiện hiển thị — vì hai hướng cho verdict ngược nhau hoàn toàn.
- Tạm verdict `LBCKQTHCT_05` và `LBCKQTHCT_06`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1: owner `Dev FE`, hai dòng thành lỗi. Nếu chọn hướng 2: `Không phải bug`, hai dòng đóng được sau khi BA bổ sung đặc tả; đối tác đo lại trên bản mới.
- **Dù BA chọn hướng nào**, xin bổ sung dòng cho khối "Chương trình HTPL liên quan" vào bảng thành phần màn hình — hiện tại nó không được khai ở đâu trong bảng.

---

<!-- ===================== 5 ===================== -->

## `GKQTHCTHTPL_01` (dòng 342) — Trạng thái ở màn Chi tiết đợt là của ĐỢT hay của ĐƠN VỊ

**Bối cảnh testcase**

- Dòng Excel: 342, mã TC `GKQTHCTHTPL_01`.
- Nội dung kiểm tra: *Đợt báo cáo → Chi tiết → bấm **"Gửi Trung ương"** → Xác nhận*.
- Expected trong file UAT: *"chuyển trạng thái đợt báo cáo: Đã duyệt kết quả → Đã gửi Trung ương"* + ghi nhận thời điểm gửi + đánh dấu vào danh sách tổng hợp của TW + thông báo cho CB NV TW + lưu vết + thông báo nhanh *"Đã gửi báo cáo lên Trung ương"*.
- Actual đối tác ghi: *"Hệ thống hiển thị thông báo **Forbidden**"*.

> **BA đã biết dòng này nhưng chưa quyết.** Phiếu phản hồi DEV 05/08 ghi rõ lỗi *"Forbidden"* của `GKQTHCTHTPL_01` **không phiếu Dev nào nhắc tới**, đề nghị đưa vào lô xử lý kế tiếp. Đây là lần đặt lại thành câu hỏi có thể trả lời được.

**Kết quả verify UI hiện tại**

- ⚠️ **Vế "Forbidden" chưa đo lại được trên bản dựng hiện hành — khai rõ, không suy từ lượt cũ.** Môi trường hiện chỉ có 4 đợt: 1 đợt ở `Tạo đợt`, 3 đợt ở `Đã tổng hợp` — **không đợt nào ở `Đã duyệt KQ`** để có nút [Gửi Trung ương] mà bấm. Dựng lại tiền đề phải chạy trọn vòng đời đợt qua nhiều vai trò.
- Lượt đo 07/08 (bản dựng cũ `index-D4Buvu4S.js`, tài khoản `cbnv_hn` — CB NV cấp ĐP) ghi nhận: **"Forbidden" đã hết**, thao tác chạy trót lọt, 4/5 vế đo được đều đạt. Ghi lại để BA có ngữ cảnh, **không** dùng làm kết luận cho bản hiện hành.
- **Vế trục trạng thái thì vẫn quan sát được trên bản hiện hành, và vẫn nhập nhằng.** Đợt `DOT-THBC01-UAT` đọc bằng tài khoản TW: ô *Trạng thái* của đợt ghi **`Tạo đợt`**, thanh tiến trình dừng ở bước 1/6 — trong khi bảng *Tiến độ nộp theo đơn vị* ngay bên dưới đã ghi **2 đơn vị "Đã nộp"** (Bộ Kế hoạch và Đầu tư 20/07, Sở Tư pháp An Giang 22/07).
- Lượt 07/08 còn bắt được biểu hiện rõ hơn của cùng một chỗ: **cùng một đợt**, màn của cán bộ ĐP đọc *"Đã gửi TW"* còn màn của cán bộ TW đọc *"Tạo đợt"*.

**Điểm mâu thuẫn trong SRS v3.5**

1. Bước xử lý của chính chức năng Gửi TW đổi **trạng thái của ĐỢT**:
   - *"| 3 | Chuyển trạng thái đợt BC sang DA_GUI_TW, đánh dấu da_gui_tw, ghi thời điểm gửi | SM-DOT-BC |"*
   - Và bước ngay trước đó chặn theo **trạng thái đợt**: *"| 2 | Kiểm tra đợt BC ở trạng thái DA_DUYET_KQ |"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:937`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:936`

2. Nhưng bước kế tiếp — thêm vào theo STT 52 — lại đổi **trạng thái nộp của ĐƠN VỊ**, và nói chính cái đó mới là thứ hiển thị:
   - *"| 3a | **Sửa theo STT 52 UAT 2026-05-26:** Cập nhật `DOT_BAO_CAO_DON_VI_NOP[dot_id, don_vi_nop_id].trang_thai_nop = DA_NOP` + `ngay_nop = NOW()`. **Tiến độ nộp hiển thị trực tiếp ở chi tiết Đợt BC.** |"*
   - Trong khi thực thể đợt vẫn giữ nguyên vòng đời 6 trạng thái dùng chung: *"`trang_thai` … CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP')"*

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:938`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md:1368`

⇒ Một đợt có **83 đơn vị** trong phạm vi nộp. Nếu đợt chỉ có **một** trạng thái dùng chung mà mỗi đơn vị lại gửi vào lúc khác nhau, thì "Đã gửi TW" của đợt có nghĩa gì khi mới 2/83 đơn vị nộp? Đây là chỗ đặc tả chưa phát biểu.

**Câu hỏi cần BA xác nhận**

Ô *Trạng thái* và thanh tiến trình ở màn **Chi tiết đợt báo cáo** phản ánh trạng thái của **ĐỢT** hay của **ĐƠN VỊ đang đăng nhập**?

1. **Hướng 1 — trục ĐƠN VỊ:** mỗi đơn vị nộp có tiến trình riêng; màn Chi tiết hiển thị tiến trình của đơn vị người dùng, trạng thái đợt chỉ là tổng hợp. ⇒ Đề nghị BA phát biểu lại bước 3 (`:937`) cho khớp, và nói rõ khi nào đợt mới được coi là "Đã gửi TW". Phần mềm về cơ bản **đúng**.
2. **Hướng 2 — trục ĐỢT:** trạng thái là của đợt, dùng chung cho mọi vai trò. ⇒ Việc cùng một đợt hiện hai trạng thái khác nhau ở màn ĐP và màn TW **là lỗi**, owner `Dev BE`.

**Kèm theo — 1 câu phụ, nếu BA chọn Hướng 2.** Với một đợt phủ 83 đơn vị, trạng thái đợt chuyển sang `DA_GUI_TW` khi **đơn vị đầu tiên** gửi hay khi **đơn vị cuối cùng** gửi? Bước 3 hiện không phân biệt.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt trục trạng thái.
- Tạm verdict `GKQTHCTHTPL_01`: `Cần BA xác nhận`.
- Song song, đề nghị cho phép QA **dựng lại tiền đề đợt ở `Đã duyệt KQ`** để đo lại vế "Forbidden" trên bản dựng hiện hành — hiện chưa kết luận được vế này.

## Cách trả lời nhanh

Với mỗi điểm, BA chỉ cần ghi **`Hướng 1`** hoặc **`Hướng 2`** (kèm 1–2 dòng lý do nếu cần). Riêng `DGKQHTVV_02` xin trả lời rời **4 câu**, và ưu tiên **câu 3** vì đó là câu duy nhất có thể biến thành lỗi dev thật.

QA sẽ tự cập nhật verdict trên sổ theo dõi và mở phiếu cho Dev nếu có.

**Đính kèm:** `image/DGKQHTVV_02-diem-tong-be-dong-2026-08-10.png` · `image/LBCKQTHCT_05-06-chi-tiet-dot-tao-dot-2026-08-10.png`
