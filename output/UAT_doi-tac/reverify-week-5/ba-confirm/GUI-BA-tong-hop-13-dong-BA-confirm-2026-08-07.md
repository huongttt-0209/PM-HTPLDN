# Gửi BA — tổng hợp nội dung cần xác nhận (13 dòng đang treo `BA confirm`) — 07/08/2026

> **File này để làm gì:** gom **nguyên văn** các điểm cần BA chốt của **13 dòng** trên bảng theo dõi
> `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab **`bug`** (gid 1714340219) đang để
> `Trạng thái dev fix = BA confirm` **và** ô `DEV phản hồi lần 1` **chưa có nội dung BA chốt**.
> Mục đích là BA đọc **một** file rồi trả lời một lượt, không phải mở 7 file rời.
> Nội dung gốc vẫn giữ nguyên ở các file nguồn (Phụ lục C) — file này **không thay thế** chúng.

> **Cách lọc ra 13 dòng này (đọc sheet ngày 07/08/2026):** tab `bug` có **20** dòng `Trạng thái dev fix =
> BA confirm`. Trừ **7** dòng ô `DEV phản hồi lần 1` **đã có nội dung BA chốt hoặc đã kết luận BA không phải
> quyết** — dòng **10** (`KTDGKQHT_05`, BA chốt 04/08) · **308** (`QLHDTVVCG_02`) · **319** (`QLHDTVVCG_13`) ·
> **321** (`QLHDTVVCG_15`) · **345** (`THBCTHCT_05`) đều "BA chốt 06/08"; **343** (`THBCTHCT_01`) và **344**
> (`THBCTHCT_02`) ghi *"Dev tự fix theo căn cứ SRS rõ ràng, BA không phải quyết"*. **Còn lại 13 dòng** trong
> file này. Riêng dòng **32** ô `DEV phản hồi lần 1` **có chữ nhưng là chữ của Dev nói "Vẫn chờ BA — chưa có
> kết luận"** kèm câu hỏi gửi BA ⇒ vẫn tính là chưa chốt.

> **Không điểm nào dưới đây đang chặn bàn giao.** Ở **cả 13 dòng**, phần mềm đang chạy **đúng đặc tả hiện hành
> hoặc đúng kỳ vọng đối tác**; việc cần chốt là **dọn đặc tả / sửa "Kết quả mong đợi" của phiếu**. Chỉ khi BA
> chọn **Hướng 2** ở một số câu thì mới phát sinh việc cho Dev — đã ghi rõ ở từng câu.

> **Nguồn đối chiếu duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt 2026-07-25).
> Mọi số dòng đều đã **mở file đọc trong chính lượt đo**, không lấy từ trí nhớ và không lấy từ
> `input/srs-update-2026-5-5/`.

> **Giới hạn hiệu lực:** QA đo trên env nội bộ `https://18.143.165.120.nip.io` (bản dựng `HTPLDN · V1.0.8` /
> `V1.0.9` tùy lô). Đối tác chụp bằng chứng trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản `V1.0`–`V1.0.3`.
> **Hai bản dựng khác nhau thật** — mọi kết luận dưới đây chỉ có hiệu lực cho bản đã ghi, cần đo lại khi bản
> này lên env nghiệm thu.

---

## Bảng dẫn — 13 dòng, 17 điểm cần chốt

| # | Dòng | Mã TC | Điểm cần BA chốt | Nếu chọn Hướng 1 | Nếu chọn Hướng 2 | Người quyết |
|--:|---:|---|---|---|---|---|
| 1 | 20 | `QLLKHDTBD_09` | Tệp Excel xuất từ màn Kế hoạch đào tạo gồm **những cột nào** (có "Người tạo"/"Ngày tạo" không) | Bổ sung bảng "Outputs — Tệp Xuất Excel" vào FR-III-14 | Thêm cột vào tệp → `Dev BE` | BA |
| 2 | 32 | `QLTVV_02` | Danh sách TVV/CG mặc định **sắp theo tiêu chí nào** | Giữ ngày tạo → ghi vào SRS + sửa phiếu | Đổi sang ngày công nhận → **lỗi**, `Dev BE` | BA **+ đối tác** |
| 3a | 35 | `DKTGMLTVV_13` | Hồ sơ tạo ở màn Thêm mới TVV có mang loại **"Người hỗ trợ"** không | Sửa "Kết quả mong đợi" của phiếu | BA sửa đặc tả ≥4 chỗ rồi mới đo lại | BA **+ đối tác** |
| 3b | 35 | `DKTGMLTVV_13` | Sau khi lưu thành công thì **chuyển sang màn nào** | Sửa phiếu (về Danh sách) | BA định nghĩa màn mới + ghi ngoại lệ §H7 | BA **+ đối tác** |
| 3c | 35 | `DKTGMLTVV_13` | Câu thông báo thành công có **bắt buộc kèm mã hồ sơ** không | Sửa phiếu (bỏ vế "cùng mã hồ sơ") | Bổ sung câu chuẩn vào SRS → `Dev FE` | BA **+ đối tác** |
| 4a | 65 | `DGKQHTVV_02` | **Bộ nhãn + bố cục** nhóm Đánh giá vụ việc là gì (đặc tả ghi mã kỹ thuật) | Chốt bộ nhãn đang chạy | Cấp bộ nhãn khác → `Dev FE` | BA |
| 4b | 65 | `DGKQHTVV_02` | Có bổ sung 2 trường **"Người đánh giá" / "Ngày đánh giá"** vào bảng thành phần màn hình không | Bổ sung (web đã có) | Gỡ khỏi giao diện → `Dev FE` | BA |
| 4c | 65 | `DGKQHTVV_02` | 🔴 SRS có đặt tiêu chí **"không tràn / không bẻ vỡ giá trị"** cho vùng nhóm chi tiết không | Có → **thành lỗi thật**, `Dev FE` | Không → không phải lỗi | BA |
| 4d | 65 | `DGKQHTVV_02` | Điểm tổng hiển thị **mấy chữ số thập phân**, làm tròn ra sao | Chốt quy tắc + ghi vào SRS | — | BA |
| 5 | 149 | `QLDMTCTV_12` | **Mốc tối đa** của ô "Lý do thay đổi trạng thái" Tổ chức tư vấn | Chốt 1.000 → sửa phiếu + ghi số vào SRS | Chốt 5.000 → **lỗi**, `Dev FE/BE` | BA |
| 6 | 288 | `QLNDTVVCG_38` | Phân công CG hàng loạt: **một** CG chung hay **riêng từng hồ sơ** | Bổ sung câu "một CG chung" vào SRS | Bổ sung khuôn nhập riêng → `Dev FE/BE` | BA |
| 7 | 297 | `QLHSPLDN_15` | Xuất Excel khi bộ lọc ra **0 bản ghi**: chặn xuất hay xuất tệp rỗng | Cấp mã lỗi + câu chữ chính thức | Xác nhận được phép trả tệp rỗng | BA |
| 8 | 301 + 302 | `QLTLPLCVV_22/23` | Nhóm "Tư liệu PL liên kết" **có** ô tìm kiếm / bộ lọc không | Bổ sung vào §Thành phần màn hình SCR-X1-02 | Bỏ khỏi giao diện → `Dev FE` | BA |
| 9 | 302 | `QLTLPLCVV_23` | Tìm kiếm tư liệu có **bắt buộc hỗ trợ tiếng Việt không dấu** không | Đồng bộ phạm vi BR-DATA-08 | Sửa `:948`, bỏ cụm "unaccent" | BA |
| 10 | 335 | `LBCKQTHCT_01` | Thao tác **Lưu nháp** có bắt buộc phản hồi thành công không, câu chữ ràng buộc tới đâu | Bổ sung mã `INF-XI-06-*` vào SRS | Không bắt buộc → đóng phiếu | BA |
| 11 | 338 + 339 | `LBCKQTHCT_05/06` | Trước khi bấm [Lập báo cáo], màn Chi tiết đợt có phải hiện khối **Nhận xét + Chương trình liên quan** ở dạng chỉ đọc không · điều kiện hiển thị neo vào **ĐỢT** hay **ĐƠN VỊ** | Chỉ hiện khi lập → bổ sung điều kiện vào SRS | Phải hiện chỉ-đọc → `Dev FE` | BA |
| 12 | 342 | `GKQTHCTHTPL_01` | 🔴 Trạng thái ở màn Chi tiết đợt là của **ĐƠN VỊ** hay của **ĐỢT** — `:937` vs `:938` vs `:1368` đang mâu thuẫn | Chốt trục ĐƠN VỊ → phát biểu lại `:937` | Chốt trục ĐỢT → `Dev BE` | BA |

> **Điểm 2 · 3a · 3b · 3c BA không quyết một mình được.** Nếu chốt theo Hướng 1 đều dẫn tới **sửa ô "Kết quả
> mong đợi" trong phiếu của đối tác** — cần đối tác xác nhận. Các điểm còn lại thuần nội bộ.

> **2 điểm có thể biến thành lỗi dev thật:** **4c** (nếu BA nói SRS *có* tiêu chí không-bẻ-vỡ thì ô "Điểm tổng"
> đang bẻ `9/10` → `9/1`+`0` là lỗi) và **12** (mô hình trạng thái đợt/đơn vị). Ưu tiên trả lời 2 điểm này trước.

**Cách trả lời nhanh:** với mỗi điểm, BA chỉ cần ghi **`Hướng 1`** hoặc **`Hướng 2`** (kèm 1–2 dòng lý do nếu
cần). QA sẽ tự cập nhật verdict 13 dòng + mở phiếu cho Dev nếu có.

---

# 1. Dòng 20 · `QLLKHDTBD_09` — Tệp Excel xuất từ màn Kế hoạch đào tạo gồm những cột nào

**Bối cảnh phiếu**

- Màn *Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách* (`/dao-tao/ke-hoach/danh-sach`), vai trò **CB_NV_TW**.
- *Kết quả mong đợi*: *"Hệ thống xuất danh sách theo điều kiện lọc hiện tại ra tệp Excel."*
- *Kết quả thực tế* đối tác: *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách."*
- Ô `TKM phản hồi lần 1`: *"File excel được xuất **thiếu trường thông tin Người tạo, Ngày tạo**."*
- QA đo lại **07/08/2026 03:00–03:07**, tài khoản `cbnv_tw_02`, bản dựng `index-D4Buvu4S.js`.

**Phần 1 — xuất theo bộ lọc: ĐÃ ĐẠT, không cần BA**

- Danh sách chưa lọc có **14** bản ghi (lấy từ tổng số máy chủ trả về, kiểm chéo bằng thẻ trạng thái
  7+2+4+1+0 = 14).
- Lọc `Trạng thái = "Đã duyệt"` → màn còn **4** kết quả → tệp tải về có **đúng 4 dòng**, 4 mã kế hoạch trùng khít
  màn hình.
- Lọc `01/07/2026 → 31/07/2026` (đúng bộ lọc trong tư liệu nghiệm thu) → màn còn **1** → tệp có **đúng 1 dòng**.
- Nếu chức năng xuất bỏ qua bộ lọc thì cả hai tệp đã phải có 14 dòng ⇒ triệu chứng đối tác nêu **không tái hiện**.
- Căn cứ: `srs-v3.5.md:5570` (*"File xuất theo bộ lọc hiện tại, không vượt quá 10.000 rows/file"*) ·
  `srs-fr-03-dao-tao.md:2243` · `srs-fr-03-dao-tao.md:1775` (*"Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ
  lọc, tối đa 10.000 dòng"*) · `srs-fr-03-dao-tao.md:1175`.

**Phần 2 — danh mục cột của tệp xuất: CẦN BA**

- Hàng tiêu đề tệp xuất (giống nhau ở cả 2 tệp) đúng **7 cột**:
  `Mã KH | Tên kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái`
- **Không có** cột "Người tạo", **không có** cột "Ngày tạo". QA không so tên cột theo chuỗi chữ cứng mà đối chiếu
  theo ý nghĩa (Người lập / Ngày lập / Thời điểm tạo / Cán bộ tạo): không cột nào chứa họ tên người; hai cột ngày
  duy nhất là **thời gian hiệu lực của kế hoạch**, không phải ngày lập bản ghi. Ví dụ quyết định: `KH-20260803-0003`
  trong tệp có Từ ngày 05/07/2026 · Đến ngày 25/07/2026, còn Ngày tạo trên màn là 03/08/2026 — **ba giá trị khác nhau**.
- ⚠️ **Tránh hiểu nhầm phạm vi:** **bảng trên màn ĐÃ có đủ** hai cột "Người tạo"/"Ngày tạo" kèm dữ liệu thật
  (vd *"CB Nghiệp vụ - Trung ương"* · *"03/08/2026"*), đúng đặc tả màn. Khoảng trống **chỉ nằm ở tệp Excel**.
- Đây **không phải lỗi mới phát sinh từ bản sửa lần này**: tư liệu nghiệm thu vòng đầu (25/07) cho thấy tệp xuất
  đã gồm đúng 7 cột như trên ngay từ thời điểm đó.

**Đặc tả đang có hai định nghĩa khác nhau cho chữ "danh sách"**

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-03-dao-tao.md:1795` · `:1796` | Bảng hiển thị trên màn **CÓ** *"Người tạo \| Họ tên cán bộ tạo"* và *"Ngày tạo \| dd/mm/yyyy"* |
| `srs-fr-03-dao-tao.md:1189–1200` | §Outputs — Danh sách của FR-III-14 **KHÔNG** có hai trường này |
| `srs-v3.5.md:5570` · `srs-fr-03-dao-tao.md:1775` · `:1175` | Phần xuất Excel **chỉ ràng buộc phạm vi dữ liệu** (theo bộ lọc, ≤10.000 dòng), **không** khai danh mục cột |

**Câu hỏi cần BA xác nhận — 3 ý**

1. Tệp Excel xuất từ màn Kế hoạch đào tạo năm phải gồm **đúng những cột nào** — theo **bảng hiển thị trên màn**
   (`:1786–1796`, có "Người tạo"/"Ngày tạo") hay theo **§Outputs — Danh sách** của FR-III-14 (`:1189–1200`, không
   có hai cột này)? **Đề nghị bổ sung một bảng "Outputs — Tệp Xuất Excel" vào FR-III-14**, theo đúng cách đặc tả
   đã làm ở FR-III-05 (`srs-fr-03-dao-tao.md:609–625`).
2. Nếu chốt theo bảng trên màn: cột **"Số chương trình"** (`:1793`) có phải nằm trong tệp xuất không? Hiện tệp
   cũng không có cột này ⇒ câu trả lời quyết định phạm vi cần chỉnh **rộng hơn** hai cột mà đối tác nêu.
3. Cột **"Mã KH"** có trong tệp xuất thực tế nhưng **không có trong cả hai bảng cột** nói trên của đặc tả — là
   cột được chấp nhận và cần bổ sung vào đặc tả, hay là cột thừa cần gỡ?

> **Giới hạn phép đo phần 1:** cả hai lần đo đều có số kết quả sau lọc (4 và 1) **nhỏ hơn cỡ trang** (20 dòng/trang)
> và tổng dữ liệu (14) cũng nhỏ hơn cỡ trang ⇒ khẳng định được tệp bám bộ lọc, **chưa** tách bạch được trường hợp
> số kết quả sau lọc lớn hơn một trang.

---

# 2. Dòng 32 · `QLTVV_02` — Danh sách Tư vấn viên/Chuyên gia mặc định sắp xếp theo tiêu chí nào

**Bối cảnh phiếu**

- Màn *Danh sách Tư vấn viên / Chuyên gia*, vai trò **CB_NV_TW**. Phiếu gộp **5 vế**.
- *Kết quả mong đợi* (vế đang treo): *"Mặc định: hệ thống sắp xếp **theo ngày công nhận mới nhất trước**, 20 bản
  ghi mỗi trang."*
- QA đo lại **06/08/2026**.

**4/5 vế ĐÃ HẾT LỖI — không cần BA**

- Cột Điểm ĐG **không còn tràn/đè** lên cột Trạng thái: đo **toạ độ thật 26 lượt hàng** ở 4 bề rộng màn hình
  1920/1440/1280/1024 — khoảng cách mép phải ô Điểm ĐG với mép trái ô Trạng thái đúng bằng 0, không hàng nào
  chồng lấn; chữ bên trong còn cách mép phải 27–36 px.
- Cột Điểm ĐG hiển thị **đồng nhất**: hàng chưa có điểm = 5 sao xám + `"—/5"`; hàng có điểm = 5 sao, tô vàng
  theo điểm + `"4.1/5"` · `"3.3/5"`. Cùng kiểu trình bày, chỉ khác dữ liệu.
- Nút thao tác **không còn xuống dòng**: 3 biểu tượng 24×24 nằm ngang cùng một dòng, chênh lệch chiều dọc = 0,
  chiều cao khung ô đúng bằng một biểu tượng đơn.
- Mặc định **20 bản ghi/trang**: đúng, ở cả 4 tab và cả 4 bề rộng.

**Vế còn lại — CẦN BA**

- Đọc hết cột "Ngày công nhận" của 6/6 hàng trang 1: thứ tự `"—"`, 17/07/2026, 12/07/2026, `"—"`, `"—"`, `"—"`
  — **không giảm dần**.
- Đối chiếu bằng đường thứ hai: thứ tự máy chủ trả về trùng khít thứ tự trên màn, và **ngày TẠO bản ghi** của dãy
  đó **giảm dần tuyệt đối** (05/08 → 12/07 09:55 → 12/07 00:11 → 30/06 → 01/03/2026 → 01/02/2024).
  ⇒ Danh sách đang sắp theo **ngày tạo bản ghi, mới nhất trước** — một tiêu chí **khác** ngày công nhận.

**Vì sao chuyển BA thay vì chuyển lại Dev**

- Đã rà toàn bộ `srs-fr-04-chuyen-gia-tvv.md`: **KHÔNG có dòng nào** quy định thứ tự sắp xếp mặc định của màn
  Danh sách TVV. Chỉ có `srs-fr-04-chuyen-gia-tvv.md:247` — *"Phân trang (mặc định 20/trang) | BR-DATA-07"*.
- Trong khi đó các màn danh sách khác (Vụ việc · Doanh nghiệp · Chi trả · Đánh giá) **đều có quy định rõ**.
  ⇒ Đây là chỗ **đặc tả bỏ sót**, không phải chỗ phần mềm làm sai điều đã quy định.

**Câu hỏi cần BA xác nhận — 2 ý**

1. Màn Danh sách Tư vấn viên / Chuyên gia mặc định sắp theo **ngày công nhận mới nhất trước** (như phiếu ghi),
   hay **giữ theo ngày tạo bản ghi** như hiện tại?
2. Nếu chọn ngày công nhận: hồ sơ **CHƯA có** ngày công nhận xếp **lên đầu** hay **xuống cuối**? (Hiện có 4/6 hàng
   trang 1 chưa có ngày công nhận ⇒ câu này quyết định phần lớn thứ tự thực tế.)

- **Hướng 1:** giữ ngày tạo → ghi tiêu chí sắp xếp vào đặc tả màn + sửa ô "Kết quả mong đợi" của phiếu.
  **Cần đối tác xác nhận.**
- **Hướng 2:** đổi sang ngày công nhận → **là lỗi cần dev sửa**, owner `Dev BE`; kèm quy tắc xử lý hồ sơ chưa có
  ngày công nhận.

---

# 3. Dòng 35 · `DKTGMLTVV_13` — Người hỗ trợ đăng ký hồ sơ Tư vấn viên

**Bối cảnh phiếu**

- Vai trò **Người hỗ trợ pháp lý (NHT)**, màn `Thêm mới Tư vấn viên` (`/chuyen-gia-tvv/tao-moi`), nhập dữ liệu
  hợp lệ rồi bấm `Lưu`.
- *Kết quả mong đợi* của đối tác (một ô, chứa **3 vế**): *"Hệ thống tạo hồ sơ tư vấn viên **với loại "Người hỗ
  trợ"** ở trạng thái "Mới đăng ký"… hiển thị thông báo "Đăng ký thành công, chờ thẩm định" **cùng mã hồ sơ đã
  tạo** và **chuyển sang trang theo dõi tiến độ**."*
- Đối tác chấm `Fail`. Ô `TKM phản hồi lần 1` nêu thêm ý nút submit tên `Lưu` chứ không phải `Gửi đăng ký`.
- QA đo lại **07/08/2026**, tài khoản `nht_ag_uat2` (NHT · cấp ĐP · Sở Tư pháp An Giang), bản dựng `V1.0.9`.
  Tạo được hồ sơ `TVV-STP-AG-0004`, trạng thái `Mới đăng ký`.

> **Ba vế phải trả lời cả ba thì dòng 35 mới đóng được.** Trả lời một vế vẫn để dòng treo.

---

## 3a. Trường "Loại" của hồ sơ có giá trị "Người hỗ trợ" không?

**Đặc tả nói gì**

- Trường `loai_tvv` chỉ nhận **hai** giá trị `TVV` / `CG`, ràng buộc dữ liệu ghi thẳng `CHECK IN ('TVV','CG')`.
- "Người hỗ trợ" **không phải giá trị của trường Loại** — nó là **vai trò của người thao tác** và là **đối tượng
  dữ liệu riêng** (`NGUOI_HO_TRO`), tạo ở **màn khác**, **trạng thái khởi tạo khác** (`CHO_KICH_HOAT`).
- Đây là thay đổi **có chủ đích**, ghi trong lịch sử sửa đổi của chính tài liệu (2026-05-03: gỡ NHT khỏi enum
  `loai_tvv`, tách thành entity riêng).

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:296` | `\| 0 \| loai_tvv \| text \| Y \| CHECK IN ('TVV','CG') \| 'TVV' \| NHT chọn (radio) \|` |
| `srs-fr-04-chuyen-gia-tvv.md:1490` | `\| 2.2 \| nhóm 1 \| Loại * \| dropdown 2 lựa chọn \| "Tư vấn viên" / "Chuyên gia" — mặc định "Tư vấn viên" \|` |
| `srs-fr-04-chuyen-gia-tvv.md:1381–1386` | Bảng ánh xạ `loai_tvv`: chỉ `TVV → Tư vấn viên`, `CG → Chuyên gia` |
| `srs-fr-04-chuyen-gia-tvv.md:137` · `:2019` | *"NHT … lưu ở entity riêng NGUOI_HO_TRO"* |
| `srs-fr-04-chuyen-gia-tvv.md:1799` | Màn tạo Người hỗ trợ: `/chuyen-gia-tvv/nguoi-ho-tro/tao-moi` |
| `srs-fr-04-chuyen-gia-tvv.md:2073` | `NGUOI_HO_TRO.trang_thai` mặc định `'CHO_KICH_HOAT'` |
| `srs-fr-04-chuyen-gia-tvv.md:18` | Lịch sử 2026-05-03 `F-FR04-NEW-02`: *"bỏ NHT khỏi loai_tvv enum + tạo entity NGUOI_HO_TRO"* |

**Web hiện tại làm gì**

- Mở ô "Loại" **trước khi nhập bất kỳ dữ liệu nào**: đúng **2** lựa chọn `Tư vấn viên (TVV)` và `Chuyên gia (CG)`.
  **Không có "Người hỗ trợ"**. Hồ sơ tạo ra mang `loaiTvv = TVV`.
- ⇒ **Khớp hoàn toàn** `:296` và `:1490`. **Không phải lỗi dev.**

**Câu hỏi**

Hồ sơ tạo ở màn Thêm mới Tư vấn viên **có** được phép mang loại "Người hỗ trợ" không?

1. **Hướng 1 (QA đề xuất):** không — giữ 2 giá trị `TVV`/`CG`. Sửa ô "Kết quả mong đợi" của phiếu thành *"với
   loại **Tư vấn viên** (hoặc **Chuyên gia**, theo lựa chọn khi nhập)"*. **Cần đối tác xác nhận.**
2. **Hướng 2:** có — thì BA nhập thay đổi vào đặc tả **trước**, tối thiểu 4 chỗ: `:296` · `:1490` · `:1381–1386`
   · `:2019`; kèm quyết định xử lý quan hệ với entity `NGUOI_HO_TRO` đang tồn tại song song. Sau đó QA đo lại.

---

## 3b. Sau khi lưu thành công thì chuyển sang màn nào?

**Đặc tả nói gì**

- Quy ước UI chung toàn hệ thống, mức **BẮT BUỘC**, quy định **ngược** với kỳ vọng của đối tác:
  `srs-v3.5.md:6759` §H7 — *"Sau khi thực hiện thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng
  về trang Danh sách (SCR-XX-01) kèm toast thông báo. Trừ trường hợp đối tác/CĐT yêu cầu giữ lại trang Chi tiết
  bản ghi vừa tạo (… **phải có ghi chú riêng tại FR cụ thể**)."*
- Đọc trọn FR-IV-03 (`srs-fr-04-chuyen-gia-tvv.md:280–363`) và SCR-IV-02 (`:1470–1529`): **không có ghi chú
  ngoại lệ nào** — tức điều kiện duy nhất để được làm khác §H7 không tồn tại.
- Trong toàn bộ đặc tả **không có màn nào tên "trang theo dõi tiến độ"** cho luồng đăng ký TVV. Cụm chữ này xuất
  hiện đúng **1** lần trong cả thư mục `srs-v3.5/`, thuộc **nghiệp vụ khác** — `srs-fr-15-ct-htpldn.md:621`
  (theo dõi tiến độ **nộp báo cáo** của các đơn vị).

**Web hiện tại làm gì**

- Ngay sau khi lưu: `location.href` = `/chuyen-gia-tvv/danh-sach`, breadcrumb *Trang chủ / Mạng lưới Tư vấn viên
  / Danh sách*. ⇒ **Khớp §H7.** **Không phải lỗi dev.**

**Câu hỏi**

Sau khi Người hỗ trợ đăng ký hồ sơ TVV thành công, màn hình **nên** đi đâu?

1. **Hướng 1 (QA đề xuất):** giữ §H7 — quay về trang Danh sách. Sửa ô "Kết quả mong đợi" của phiếu thành *"…và
   **quay lại trang Danh sách tư vấn viên**"*. **Cần đối tác xác nhận.**
2. **Hướng 2:** nếu nghiệp vụ thật sự cần một màn theo dõi tiến độ hồ sơ cho NHT → BA **định nghĩa màn đó**
   (đường dẫn · thành phần · quyền truy cập) và **ghi ngoại lệ §H7 ngay tại FR-IV-03** — đúng cơ chế ngoại lệ mà
   chính §H7 quy định — rồi QA mới đo lại.

---

## 3c. Câu thông báo thành công có bắt buộc kèm mã hồ sơ không?

**Đặc tả im lặng** *(không phải "hai chỗ nói ngược nhau" — đơn giản là không có dòng nào nói)*

- §Outputs của FR-IV-03 **tách riêng hai thứ**, không dòng nào yêu cầu ghép mã vào câu thông báo:
  - `srs-fr-04-chuyen-gia-tvv.md:348` — `\| 1 \| ma_tvv \| text \| — \| TVV-{CODE}-{SEQ} (auto-gen) \|`
  - `srs-fr-04-chuyen-gia-tvv.md:351` — `\| 4 \| thong_bao \| text \| — \| "Đăng ký thành công, chờ thẩm định" \|`
- Hai chỗ còn lại có thể quy định câu thông báo cũng không nhắc: mô tả nút `Lưu` của màn hình (`:1522`) và trọn
  §Postconditions (`:353–357`).
- **Đối chứng ngược:** khi đặc tả *muốn* kèm mã thì viết rõ — `:597` (FR-IV-07): *"gửi mail link kích hoạt vĩnh
  viễn (1 lần dùng) **kèm mã số TVV**"*. ⇒ sự im lặng ở trên khó coi là "ngầm hiểu".

**Web hiện tại làm gì**

- QA **cài sẵn bộ bắt thông báo trước khi bấm** `Lưu` (thông báo tự tắt sau vài giây), bấm **một lần duy nhất**.
- Chuỗi bắt được: **"Đăng ký thành công, chờ thẩm định"** — **trùng nguyên văn** câu chuẩn ở `:351`.
- Câu thông báo **không chứa mã hồ sơ**. Mã `TVV-STP-AG-0004` **có** được sinh, nhưng chỉ nằm trong dữ liệu máy
  chủ trả về.

**Câu hỏi**

Câu thông báo sau khi đăng ký thành công **có** bắt buộc kèm mã hồ sơ vừa tạo không?

1. **Hướng 1:** theo đúng chữ ở `:351` — câu thông báo là *"Đăng ký thành công, chờ thẩm định"*, hết; mã hồ sơ
   là output riêng, người dùng xem ở danh sách/chi tiết. Web hiện tại **đúng** → sửa phiếu, bỏ vế *"cùng mã hồ
   sơ đã tạo"*. **Cần đối tác xác nhận.**
2. **Hướng 2:** phải kèm mã, ví dụ *"Đăng ký thành công, chờ thẩm định. Mã hồ sơ: TVV-STP-AG-0004"*. Khi đó
   `:351` **thiếu** → BA bổ sung **câu chuẩn đầy đủ** kèm định dạng ghép mã, rồi giao `Dev FE`.

---

## 3d. Ghi nhận kèm theo — **KHÔNG cần BA quyết trong file này**

Ô `TKM phản hồi lần 1` của dòng 35 ghi *"…không có button Gửi đăng ký, chỉ có button Lưu … **BA xác nhận tên
button sai**"*. QA **không đưa điểm này thành tiêu chí chấm**, vì:

- Đặc tả chốt hiện hành vẫn quy định nhãn nút của màn này là **"Lưu"** — `srs-fr-04-chuyen-gia-tvv.md:1522`
  (*"Hủy" (phụ) / "Lưu" (chính)"*) và quy ước nhãn nút **BẮT BUỘC** `srs-v3.5.md:6756` §H4 (*"Nút lưu luôn Lưu"*).
- Chuỗi `"Gửi đăng ký"`: **0 kết quả** trên toàn bộ 18 tệp của thư mục `srs-v3.5/`.
- Không có dấu thay đổi nào (`[STT…]` / `[CR-…]` / `[BA chốt …]`) chạm tới nhãn nút của SCR-IV-02.
- Bước thao tác của **chính phiếu** cũng ghi *"Dữ liệu hợp lệ và nhấn **Lưu**"* ⇒ nút `Lưu` là **tiền đề thao
  tác**, không phải kết quả mong đợi.

⇒ Quyết định *"BA xác nhận tên button sai"* **chưa được nhập vào bản đặc tả này** nên chưa có hiệu lực để chấm.
Nếu vẫn muốn đổi tên nút, đề nghị BA **cập nhật `:1522` và §H4 (`srs-v3.5.md:6756`) trước** — đi đường sửa đặc
tả, không đi đường verify phiếu.

---

# 4. Dòng 65 · `DGKQHTVV_02` — Nhóm "Đánh giá" ở màn chi tiết Vụ việc

**Bối cảnh phiếu**

- Màn *Chi tiết vụ việc* → nhóm **Đánh giá** (Accordion 8), vai trò **CB_NV_TW**.
- *Kết quả mong đợi* của đối tác — 3 vế chung chung: *"hiển thị các trường thông tin **giống với thiết kế**"* ·
  *"dữ liệu đúng định dạng và trường thông tin"* · *"dữ liệu **không bị tràn/đè lên nhau**, đồng nhất ngôn ngữ"*.
- Ô *Kết quả thực tế* và *TKM phản hồi lần 1* của đối tác đều **TRỐNG** — phiếu không mô tả triệu chứng cụ thể.
- QA đo lại **07/08/2026 02:00–02:12**, tài khoản `cbnv_tw_04`, vụ việc `VV-BTP-TW-20260806-003` (đang *Đã đánh
  giá*, cùng đơn vị tài khoản đo), bản dựng `index-DsMHK7Dp.js`. Không seed, không sửa dữ liệu.

**3 vế đo được ĐÃ ĐẠT — không cần BA**

1. Nhóm Đánh giá hiện **đủ 5 trường** đặc tả yêu cầu: Điểm chất lượng tư vấn 9/10 · Điểm đúng thời hạn 8/10 ·
   Điểm thái độ phục vụ 10/10 · Điểm tổng 9/10 · Nhận xét. **14/14 ô** hiển thị thật, không ô nào ẩn.
   - `srs-fr-05-vu-viec.md:1734` — *"Accordion 8 — Đánh giá (gộp MH-05.9) … diem_chat_luong (0-10),
     diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet … Khi VV ở HOAN_THANH hoặc
     DA_DANH_GIA"*
2. Giá trị trên màn **khớp đúng bản ghi đã lưu**: đọc lại từ máy chủ được 9 – 8 – 10 – tổng 9, nhận xét
   `QA-DGKQ-20260806-1634`, ngày 06/08/2026 16:34. **Hai đường đo khớp nhau.**
3. Toàn bộ nhãn và giá trị là **tiếng Việt**, không lộ mã kỹ thuật, không `null`/`undefined`
   (`srs-fr-05-vu-viec.md:1492` · `:1622`).

**4 điểm CẦN BA CHỐT**

**(a) Bộ nhãn tiếng Việt + bố cục của nhóm Đánh giá là gì?**
Bảng thành phần màn hình `:1734` ghi **mã kỹ thuật** (`diem_chat_luong`, `diem_thoi_gian`…), trong khi quy ước
của chính mục đó (`:1486`) nói cột ấy phải là **chữ người dùng nhìn thấy**, còn `:1492` và `:1622` lại **cấm mã
kỹ thuật lên giao diện**. Tài liệu thiết kế mà `srs-v3.5.md:567` trỏ tới **không có trong bộ SRS**.
⇒ Không có chuẩn để chấm vế *"hiển thị giống với thiết kế"*. *(Web hiện tại đang dùng 7 nhãn tiếng Việt.)*

**(b) Có bổ sung 2 trường "Người đánh giá" và "Ngày đánh giá" vào bảng thành phần màn hình không?**
Hai trường này **không** nằm trong bảng `:1734` nhưng **có căn cứ ở mô hình dữ liệu** (`:2115`, `:2122`) ⇒ theo
quy ước **UI-12** (`srs-v3.5.md:584`) là **bảng đặc tả bị sót**, phần mềm không sai. *(Web hiện tại đã hiển thị
cả hai.)*

**(c) 🔴 SRS có đặt tiêu chí "không tràn / không bẻ vỡ giá trị" cho vùng nhóm chi tiết không?**
Hiện `srs-fr-05-vu-viec.md:1570` chỉ ghi *"Áp dụng cho **mọi cột text trong bảng**"* — tức chỉ áp cho **bảng danh
sách**, không nói gì về vùng nhóm chi tiết.
**Đây là điểm có thể biến thành lỗi dev thật, đề nghị BA ưu tiên trả lời:**
- Bảng của nhóm Đánh giá chia cột rất lệch: cột giá trị **thứ nhất chỉ rộng 64–65 px** (trừ đệm hai bên còn vùng
  chữ **31–32 px**), trong khi cột thứ hai rộng **238 px** và cột thứ ba **152 px**. Chuỗi dạng `"x/10"` cần đúng
  khoảng **31 px** ⇒ **sát ngưỡng**, chỉ cần chữ in đậm hoặc hụt 1 px là vỡ dòng.
- Đo trên `VV-BTP-TW-20260806-003`: ô **"Điểm tổng"** (in đậm) **bị bẻ làm hai dòng** — dòng trên `9/1`, dòng dưới `0`.
- Đo thêm trên `VV-QAW7-DG01` cùng màn: vùng chữ cột thứ nhất còn 31 px nên **CẢ** ô "Điểm chất lượng tư vấn"
  (chữ thường) **LẪN** ô "Điểm tổng" đều bị bẻ hai dòng — `4/1`+`0` và `7/1`+`0`.
  ⇒ Nguyên nhân là **bề rộng cột thứ nhất quá hẹp**, không phải riêng chuyện chữ in đậm.
- Giá trị vẫn đọc ra được nên **chưa mất dữ liệu**, nhưng vế *"dữ liệu hiển thị không bị tràn, đè lên nhau"* của
  phiếu **đang KHÔNG được đáp ứng trọn vẹn**. Ngoài hiện tượng bẻ dòng: không ô nào chồng lấn, không ô nào bị cắt
  mất chữ, trang không cuộn ngang.

**(d) Điểm tổng hiển thị mấy chữ số thập phân, làm tròn theo quy tắc nào?**
`srs-fr-05-vu-viec.md:2462` chỉ áp cho **thang tư vấn viên 1–5** (*"Thang điểm 1–5, làm tròn 1 chữ số thập phân
(round-half-up)"*) và **loại trừ bằng chữ** trường hợp đánh giá vụ việc này (*"UC67 chỉ tạo DANH_GIA_VU_VIEC
(thang 0–10)"*). *(Web hiện tại: `9/10`; lượt đo dùng bộ 9-8-10 chia hết cho 3 nên chưa lộ quy tắc làm tròn —
dữ kiện làm tròn thật sự nằm ở dòng 68.)*

**Hai hướng cho từng điểm**

- **(a) (b) (d) — Hướng 1:** chốt theo hiện trạng đang chạy → **BA bổ sung vào đặc tả** (bộ nhãn tiếng Việt ·
  2 trường Người/Ngày đánh giá · quy tắc số thập phân). **Hướng 2:** cấp bộ nhãn / bố cục khác → `Dev FE`.
- **(c) — Hướng 1:** SRS **có** tiêu chí không-bẻ-vỡ cho vùng nhóm chi tiết → hiện tượng bẻ dòng ô Điểm tổng là
  **lỗi cần dev sửa**, owner `Dev FE`, hướng sửa nằm ở cách chia bề rộng cột. **Hướng 2:** SRS không đặt tiêu chí
  này → không phải lỗi, và đề nghị BA **ghi rõ** để vòng sau không tranh chấp lại.

> **Giới hạn:** kết luận chỉ có hiệu lực cho env nội bộ + bó mã `index-DsMHK7Dp.js`. Bằng chứng gốc của đối tác
> quay trên môi trường nghiệm thu khác.

---

# 5. Dòng 149 · `QLDMTCTV_12` — Mốc tối đa của ô "Lý do thay đổi trạng thái" Tổ chức tư vấn

**Bối cảnh phiếu**

- Màn *Danh mục Tổ chức tư vấn* → cửa sổ **Cập nhật trạng thái hoạt động**, ô **Lý do**.
- *Kết quả mong đợi* của đối tác: ô Lý do **bắt buộc**, **tối thiểu 10** ký tự, **tối đa 5.000** ký tự.
- Đối tác báo *"Màn hình không có nút chức năng cần kiểm thử nên không thao tác được"* (env nghiệm thu) ⇒ chưa
  từng chạy tới bước này.
- QA đo lại **07/08/2026**, tài khoản `cbnv_tw_03`, bản dựng `V1.0.9` (`index-D4Buvu4S.js`). **5/5 vế còn lại
  đều PASS** — chỉ vướng đúng mốc tối đa.

**Đặc tả im lặng về mốc tối đa**

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-04-chuyen-gia-tvv.md:984` | `\| 3 \| ly_do \| text (long) \| Y \| **Min 10 ký tự** \|` — **không có mốc tối đa** |
| `srs-v3.5.md:805` | Không đặt mốc tối đa mặc định cho kiểu `text (long)` |
| `srs-fr-04-chuyen-gia-tvv.md:2232` | `ly_do_tu_choi` giới hạn 2.000 ký tự — **trường khác**, dùng cho luồng từ chối phê duyệt |
| `srs-fr-02-hoi-dap.md:421` | Tiền lệ nhóm Hỏi đáp đặt 10–500 ký tự |

**Web hiện tại làm gì**

- Ô Lý do có `maxlength="1000"`. Nhập 5.001 ký tự → ô **chỉ nhận 1.000 và cắt âm thầm**, **không câu nào** báo
  cho người dùng biết đã bị cắt.

**Câu hỏi**

Mốc **tối đa** của ô "Lý do thay đổi trạng thái" Tổ chức tư vấn là bao nhiêu?

1. **Hướng 1 — chốt 1.000** (theo hiện trạng): sửa mốc trong phiếu của đối tác và **bổ sung số vào `:984`**.
2. **Hướng 2 — chốt 5.000** (theo kỳ vọng đối tác): đây là **lỗi cần dev sửa**, owner `Dev FE` (nới `maxlength`)
   — kiểm tra kèm phía máy chủ.

> **Đề nghị áp cho cả hai hướng:** hiển thị **một câu nhắc khi người dùng nhập vượt mốc**, thay vì cắt âm thầm.
> Hiện người dùng không có cách nào biết nội dung mình gõ đã bị mất.

> **Ứng viên lỗi ghi kèm (KHÔNG kéo verdict dòng 149, chưa lập phiếu):** ở lượt **Khôi phục** (Tạm dừng → Đang
> hoạt động), lý do gửi lên là `"KhoiPhuc07080353 - hoan nguyen sau do QLDMTCTV_12"` nhưng dòng nhật ký tab
> "Lịch sử" lại hiện **giá trị trường mô tả công khai cũ**, không phải lý do vừa nhập (lượt **Tạm dừng** thì
> hiện đúng). Cột "Hành động" cũng ghi `Cập nhật` cho cả hai lượt, trong khi `:1731` có bộ nhãn riêng
> "Tạm dừng"/"Khôi phục".

---

# 6. Dòng 288 · `QLNDTVVCG_38` — Phân công chuyên gia hàng loạt

**Bối cảnh phiếu**

- Màn *Tư vấn chuyên sâu* → chọn nhiều hồ sơ ở trạng thái `Tiếp nhận` → **[Phân công CG hàng loạt]**.
- *Kết quả mong đợi* của đối tác: áp **CÙNG MỘT** chuyên gia đã chọn cho **TẤT CẢ** yêu cầu được chọn.
- Ảnh của đối tác (`QLNDTVVCG_38.jpg`, env nghiệm thu bản `V1.0`) cho thấy hộp thoại từ chối với nội dung
  *"Phân công hàng loạt chưa được hỗ trợ"*.
- QA đo lại **07/08/2026**, bản dựng `index-D4Buvu4S.js`, 2 hồ sơ `TVCS-QLND38-UAT-01/02` cùng lĩnh vực.

**Đính chính một giả định đang lưu hành**

> Có giả định rằng *"SRS chỉ quy định phân công từng bản ghi, không hề có hàng loạt"*. **Giả định đó KHÔNG đúng.**
> `srs-fr-12-tv-chuyen-sau.md:1127` quy định rõ nút `[Phân công CG hàng loạt]` cho bản ghi `TIEP_NHAN`, và yêu
> cầu này **có từ bản v3** (`srs-v3/srs-fr-12:886`). Tức hộp thoại từ chối trong ảnh đối tác đã **viện dẫn chính
> `srs-fr-12`** để biện minh cho việc không hỗ trợ — trong khi `srs-fr-12` yêu cầu điều ngược lại.

**Web hiện tại làm gì**

- **4/4 vế đo được đều ĐẠT** — triệu chứng *"chưa được hỗ trợ"* **không còn tái hiện**: chọn 2 dòng → thanh
  `Đã chọn 2 bản ghi` + nút `Phân công hàng loạt (2)` → cửa sổ "Phân công chuyên gia" mở ra → sau khi xác nhận,
  cả 2 hồ sơ đều có chuyên gia và đổi trạng thái.
- Cửa sổ chỉ có **1 ô chọn chuyên gia + 1 ô ghi chú**, không có bảng nhập riêng từng hồ sơ. Một lời gọi duy nhất
  `POST /api/v1/noi-dung-tu-van-cs/phan-cong-hang-loat`; `ngayPhanCong` của 2 hồ sơ cách nhau **2 mili-giây**
  ⇒ một thao tác duy nhất, không phải 2 lần phân công lẻ. **Đúng kỳ vọng đối tác.**

**Điểm đặc tả im lặng**

- `srs-fr-12-tv-chuyen-sau.md:1127` có nút hàng loạt nhưng **không nói** chọn chuyên gia **chung** hay **riêng
  từng bản ghi**.
- Khối Processing phân công `srs-fr-12-tv-chuyen-sau.md:166–181` **chỉ mô tả một bản ghi**.
- Module anh em `srs-fr-04-chuyen-gia-tvv.md:1462` lại dùng **khuôn nhập từng hồ sơ** ⇒ hai kiểu cùng tồn tại
  trong bộ tài liệu.

**Câu hỏi**

Với phân công chuyên gia **hàng loạt** của Tư vấn chuyên sâu, cán bộ chọn **một** chuyên gia áp cho mọi hồ sơ đã
chọn, hay chọn chuyên gia **riêng cho từng hồ sơ** trong cùng một cửa sổ?
**Và:** nếu là một chuyên gia chung thì xử lý thế nào khi các hồ sơ đã chọn thuộc **lĩnh vực khác nhau**, trong
khi bước 3 của khối Phân công (`srs-fr-12-tv-chuyen-sau.md:178`) buộc kiểm *"chuyên môn phù hợp lĩnh vực"*?

1. **Hướng 1 (khớp hiện trạng):** một chuyên gia chung → BA bổ sung câu này vào `:1127` + quy tắc xử lý khi lĩnh
   vực lệch nhau. **Không có gì để dev sửa.**
2. **Hướng 2:** chọn riêng từng hồ sơ → bổ sung khuôn nhập vào đặc tả màn hình rồi mới giao `Dev FE/BE`.

> Lượt đo **cố ý chọn 2 hồ sơ cùng lĩnh vực** để tránh bẫy FAIL oan, nên **chưa** có dữ kiện cho tình huống lĩnh
> vực khác nhau. Đó chính là phần BA cần chốt trước khi bổ sung đặc tả.

> **Lỗi mới phát sinh trong lúc đo (đã ghi riêng dòng 376 `QLNDTVVCG_QA01`, KHÔNG cần BA):** nhãn trạng thái màn
> danh sách lệch bảng nhãn `srs-fr-12:1130–1140` — `PHAN_CONG` hiện *"Phân công"* (đặc tả *"Đã phân công"*,
> `:1135`), `HUY` hiện *"Hủy"* (đặc tả *"Đã hủy"*, `:1140`). Đã chuyển Dev.

---

# 7. Dòng 297 · `QLHSPLDN_15` — Xuất Excel khi bộ lọc ra 0 bản ghi

**Bối cảnh phiếu**

- Màn *Chi tiết doanh nghiệp → tab **Hồ sơ pháp lý*** (`SCR-V.III-02`, `/doanh-nghiep/{id}?tab=ho-so-pl`),
  vai trò **CB_NV_TW**.
- *Kết quả mong đợi* của đối tác: hệ thống hiển thị thông báo **"Không có dữ liệu để xuất"**.
- Đối tác báo *"Màn hình không có nút chức năng"* (env nghiệm thu, 17/07/2026) ⇒ **chưa từng chạy tới bước này**.
- QA đo lại **07/08/2026 00:11**, bản dựng `V1.0.9` (`index-CxS5qW_0.js`), tài khoản `cbnv_tw_02`, DN `DN-HNI-0001`.

**Web hiện tại làm gì**

- Lọc từ khóa không khớp bản ghi nào → bảng **0 dòng** → bấm **Xuất Excel**.
- Bắt được **đúng 1 thông báo**, nguyên văn **"Không có dữ liệu để xuất"** — **trùng khít** câu chữ đối tác kỳ
  vọng. Bấm lặp lần 2: vẫn đúng 1 thông báo, không nhân đôi.
- Đối chứng độc lập: **0 lượt gọi máy chủ**, **không tệp nào được tạo** ⇒ hệ thống **chặn xuất**, không trả tệp rỗng.

> Vế còn lại của cùng phiếu — **lọc rồi xuất** — đã đo và **đạt**: lọc còn 2 dòng thì tệp xuất ra đúng 2 dòng,
> `GET /api/v1/ho-so-phap-ly-dns/export?…&keyword=QA-W5` mang theo bộ lọc. Vế đó **không** cần BA.

**Điểm đặc tả im lặng**

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:657–665` | `FR-X.1-04` §Processing — Xuất Excel đủ 5 bước (áp bộ lọc `:662` · giới hạn 10.000 dòng `:663` · 8 cột `:664` · trả tệp `:665`) — **không nói gì** về bộ lọc ra 0 bản ghi |
| `srs-fr-12-tv-chuyen-sau.md:693–701` | Bảng Error Handling của chính `FR-X.1-04` liệt kê đủ `E1→E7`; `E7 / INF-HSPL-01` là *"Không có kết quả tìm kiếm"* — **không có mã nào** cho tình huống **xuất Excel** khi bộ lọc rỗng |
| `srs-v3.5.md:5570` | `BR-DATA-06` chỉ quy định **giới hạn trên** (≤10.000 rows/file), không nói gì về tập rỗng |

**Module khác ĐÃ có quy định cho đúng tình huống này, nhưng câu chữ khác nhau:**

- `srs-fr-13-tv-nhanh.md:155` — `E5 / INF-KHO-XL-01`: *"Không có dữ liệu để xuất"* — **chặn xuất, không tạo tệp
  rỗng** `[BA-07 tuần 4]` (Kho câu hỏi).
- `srs-fr-15-ct-htpldn.md:403` — `E1 / INF-XI-02-XL-01`: *"Không có chương trình nào để xuất"* (CT HTPLDN).

**Câu hỏi**

Hồ sơ pháp lý DN (`FR-X.1-04`) có áp cùng hành vi **"chặn xuất, không tạo tệp rỗng"** như `INF-KHO-XL-01` không?

1. **Hướng 1 — có:** xin BA cấp **mã lỗi + câu chữ chính thức** cho `FR-X.1-04` — dùng lại đúng câu *"Không có
   dữ liệu để xuất"* (giống Kho câu hỏi), hay đặt câu riêng theo đối tượng như nhóm XI (*"Không có hồ sơ nào để
   xuất"*)? **Bản dựng hiện tại đang dùng đúng câu của Kho câu hỏi.**
2. **Hướng 2 — không áp:** xin BA xác nhận rõ hệ thống **được phép** trả tệp rỗng, để QA đóng vế này và ghi lại
   cho các lượt sau.

> **Đề nghị kèm:** nếu chọn Hướng 1 thì nên chốt luôn **quy ước dùng chung** cho mọi màn có nút Xuất Excel —
> hiện đã có **2 câu chữ khác nhau** ở 2 module, dễ tiếp tục lệch ở màn thứ ba.
>
> **Vì sao QA chưa tự chấm Pass:** đặc tả không có dòng nào để chấm, nên kết quả web dù trùng khít kỳ vọng đối
> tác cũng **không** đủ tư cách làm chuẩn chấm.

---

# 8. Dòng 301 + 302 · `QLTLPLCVV_22/23` — Nhóm "Tư liệu pháp lý liên kết" có được có ô tìm kiếm / bộ lọc không

**Bối cảnh phiếu**

- Vai trò **Cán bộ Nghiệp vụ**, nhóm *"Tư liệu pháp lý liên kết"* trong màn **chi tiết Tư vấn chuyên sâu**.
- Dòng **301** `QLTLPLCVV_22` — *"Tìm kiếm tư liệu hỗ trợ tiếng Việt có dấu"*.
- Dòng **302** `QLTLPLCVV_23` — *"Tìm kiếm hỗ trợ tiếng Việt không dấu"*.
- Ô `TKM phản hồi lần 1` của **cả 2** dòng: *"Màn hình không có chức năng"*.
- QA đo lại **07/08/2026**, tài khoản `cbnv_tw_05`, bản ghi `TVCS-20260806-0003`, bản dựng `V1.0.9`.

> ⚠️ **Lưu ý về bằng chứng:** hai dòng 301 và 302 đính **cùng một ảnh** (`QLTLPLCVV_23.jpg` và
> `QLTLPLCVV_24.jpg` trùng khít, md5 `3d926926a8bbdfd3352f9328d55c1c39`). Ảnh chỉ chứng minh *trạng thái màn*,
> không phân biệt được vế "có dấu" với vế "không dấu" ⇒ QA đã **đo riêng từng vế**, không suy case này ra case kia.

**Web hiện tại làm gì**

- Trong đúng khung của nhóm này có **4 ô nhập/chọn**: 1 ô từ khóa (chữ gợi ý *"Tìm theo tên hoặc mô tả tư liệu"*)
  + 3 bộ lọc `Loại tư liệu` / `Lĩnh vực` / `Trạng thái`; kèm nút `[Tìm kiếm]`, `[Xóa bộ lọc]`, `[Thêm tư liệu]`.
- Bảng tư liệu đủ **9 cột**. Tìm chạy đúng: nhóm có 2 tư liệu, gõ từ khóa → còn 1 dòng đúng bản ghi mong đợi.
- **Bảng 9 cột + nút `[+ Thêm tư liệu]` khớp đúng** thành phần đã khai ở `:1171`. Phần **ô tìm kiếm + 3 bộ lọc**
  thì **không có chỗ nào** trong bảng thành phần màn hình quy định — chính là điểm cần BA chốt.

> **So với bản đối tác đo:** ảnh của đối tác (bản `V1.0`) cho thấy nhóm này **chưa có** thanh lọc và bảng chỉ
> **7 cột**. Tức hiện tượng *"Màn hình không có chức năng"* **không còn tái hiện** trên `V1.0.9`. QA vẫn **không
> kết luận "fix đã có tác dụng"** vì không có ảnh "lỗi cũ" tự chụp trên cùng môi trường.

**Điểm mâu thuẫn trong đặc tả**

**(a) §Processing của FR-X.1-06 coi tìm kiếm tư liệu là yêu cầu chức năng BẮT BUỘC**, mô tả rất chi tiết — và
màn **duy nhất** chứa FR-X.1-06 chính là nhóm tư liệu trong màn chi tiết TVCS (màn riêng SCR-X1-07 **đã bị gộp
vào** SCR-X1-02):

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:942` | *"**Processing — Tìm kiếm tư liệu** `[GAP-X.1-02]`"* |
| `srs-fr-12-tv-chuyen-sau.md:947` | *"Nhận tiêu chí: keyword (tên tư liệu, mô tả), lĩnh vực, loại tư liệu, trạng thái"* |
| `srs-fr-12-tv-chuyen-sau.md:950` · `:951` | *"AND logic cho tất cả điều kiện"* · *"Phân trang (mặc định 20/trang)"* |
| `srs-fr-12-tv-chuyen-sau.md:828` | *"**Màn hình:** ~~SCR-X1-07~~ (DEPRECATED v2.1 — gộp thành tab "Tư liệu PL" trong SCR-X1-02 / MH-12.2)"* |
| `srs-fr-12-tv-chuyen-sau.md:1153` | *"**FR sử dụng:** FR-X.1-01, FR-X.1-03, FR-X.1-04, FR-X.1-05, **FR-X.1-06**"* |
| `srs-fr-12-tv-chuyen-sau.md:1227–1229` | *"### ~~SCR-X1-07~~ (DEPRECATED v2.1) > **Gộp vào:** Tab "Tư liệu PL liên kết" trong SCR-X1-02"* |

**(b) Nhưng §Thành phần màn hình của SCR-X1-02 KHÔNG khai bất kỳ ô tìm kiếm hay bộ lọc nào** cho nhóm này — chỉ
khai một bảng dữ liệu và nút `[+ Thêm tư liệu]`. Và **§Acceptance Criteria của FR-X.1-06 không có tiêu chí nào
cho tìm kiếm**:

| Trích dẫn | Nội dung |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1171` | *"Bảng tư liệu: Tên / Loại / Lĩnh vực / Số file / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động. Nút [+ Thêm tư liệu] (inline trong tab này)"* |
| `srs-fr-12-tv-chuyen-sau.md:1198` | *"Tư liệu PL (gộp từ MH-12.7) … CRUD tư liệu inline. Nút [Công khai lên Cổng PLQG] khi NHAP + >= 1 file"* |
| `srs-fr-12-tv-chuyen-sau.md:986–996` | Trọn §Acceptance Criteria của FR-X.1-06 — đếm số lần xuất hiện chuỗi "tìm kiếm"/"search": **0** |

**Câu hỏi**

Nhóm *"Tư liệu pháp lý liên kết"* trong màn chi tiết Tư vấn chuyên sâu (SCR-X1-02) **có** phải có ô nhập từ khóa
và bộ lọc để người dùng tìm tư liệu ngay tại đó không?

1. **Hướng 1 (QA nghiêng về hướng này) — theo §Processing FR-X.1-06 (`:942–951`):** tìm kiếm là bắt buộc, và vì
   màn riêng đã bị gộp vào SCR-X1-02 nên phương tiện tìm kiếm **phải** nằm ngay trong nhóm này. Phần dev đang làm
   là **đúng**, chỉ thiếu ở tài liệu → **BA bổ sung ô tìm kiếm + 3 bộ lọc vào `SCR-X1-02 §Thành phần màn hình`**
   (nêu rõ tìm theo trường nào, có mấy bộ lọc) + bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06.
2. **Hướng 2 — theo §Thành phần màn hình (`:1171`, `:1198`) + §AC (`:986–996`):** nhóm này chỉ gồm bảng dữ liệu
   và nút Thêm; ô tìm kiếm + 3 bộ lọc là **phần dev làm thêm ngoài đặc tả** → cần quyết **bỏ khỏi giao diện**
   (owner `Dev FE`) hay giữ và vẫn bổ sung vào đặc tả.
   ⚠️ Hướng này để lại một câu hỏi chưa có lời giải: **FR-X.1-06 sẽ được thực hiện ở màn nào**, khi màn riêng
   của nó (SCR-X1-07) đã bị khai tử ở `:828` và `:1227–1229`?

---

# 9. Dòng 302 · `QLTLPLCVV_23` — Tìm kiếm tư liệu có bắt buộc hỗ trợ tiếng Việt không dấu không

> Câu này **độc lập** với câu 8: câu 8 hỏi *"có ô tìm kiếm không"*, câu 9 hỏi *"ô đó có phải bỏ dấu được không"*.
> Dòng 302 cần **cả hai** câu trả lời mới đóng được.

**Bối cảnh phiếu**

- *Kết quả mong đợi* của đối tác: gõ từ khóa tiếng Việt **không dấu** vẫn ra bản ghi có tên viết **có dấu**.

**Web hiện tại làm gì**

- QA chọn cụm **2 từ** `Nghi dinh` chứ không dùng 1 từ: bỏ dấu của *"nghị"* là *"nghi"*, trùng tiền tố của
  *"nghiệp"* (*"nghiep"*) ⇒ tìm 1 từ sẽ mất khả năng phân biệt.
- Bấm `[Xóa bộ lọc]` để về mốc gốc: bảng **2** dòng. Gõ `Nghi dinh` (bỏ dấu hoàn toàn) → bảng còn **1** dòng,
  đúng bản ghi tên viết **CÓ DẤU** *"Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa"*.
- Đối chứng độc lập bằng phản hồi máy chủ của **chính lượt tìm đó**: `total = 1`, mã bản ghi trùng khít với tập
  mã của lượt gõ **có dấu** ở phiếu `QLTLPLCVV_22` ⇒ bỏ dấu và có dấu cho ra **cùng một kết quả**.

**Điểm mâu thuẫn trong đặc tả**

**(a) §Processing của chính FR-X.1-06 nói CÓ hỗ trợ không dấu:**

- `srs-fr-12-tv-chuyen-sau.md:948` — *"Full-text search trên ten_tu_lieu + mo_ta (**hỗ trợ tiếng Việt unaccent**)
  | BR-DATA-08"*

**(b) Nhưng quy tắc gốc BR-DATA-08 ở file chính KHÔNG nhắc chữ unaccent, và phạm vi áp dụng KHÔNG có FR-X.1-06:**

| Trích dẫn | Nội dung |
|---|---|
| `srs-v3.5.md:5572` | *"BR-DATA-08 — **Full-text search:** Hỏi đáp (noi_dung) và Kho câu hỏi (cau_hoi/cau_tra_loi/tu_khoa) … \| **FR-II-02, FR-X.1-02, FR-X.2-04** \| … Các entity khác: …"* — **không có FR-X.1-06** |
| `srs-fr-12-tv-chuyen-sau.md:1579` | *"BR-DATA-08 \| Tìm kiếm toàn văn \| **FR-X.1-02**"* |
| `srs-fr-12-tv-chuyen-sau.md:1635` | *"BR-DATA-08 \| … Hỗ trợ tiếng Việt unaccent \| Architecture AD-09 \| **FR-X.1-02**"* |

**Câu hỏi**

Tìm kiếm tư liệu pháp lý (**FR-X.1-06**) **có** bắt buộc hỗ trợ tiếng Việt không dấu không?

1. **Hướng 1 — theo `:948`** (bản trích nằm trong chính FR đang verify): có bắt buộc. Web hiện tại **đúng**
   → đề nghị **đồng bộ lại phạm vi BR-DATA-08** ở `srs-v3.5.md:5572` và hai bảng tham chiếu `:1579`, `:1635`
   để bổ sung FR-X.1-06 — hiện chúng đang nói khác với `:948`.
2. **Hướng 2 — theo BR-DATA-08 gốc:** FR-X.1-06 không thuộc phạm vi full-text/unaccent, chỉ cần tìm theo từ khóa
   thường. Web hiện tại **làm nhiều hơn yêu cầu** → đề nghị **sửa `:948`** bỏ cụm *"(hỗ trợ tiếng Việt unaccent)"*
   cho khỏi mâu thuẫn, và quyết xem có yêu cầu Dev gỡ khả năng không dấu hay giữ nguyên như phần dôi ra.

> **Chuẩn chấm vòng này QA lấy `:948`** (bản trích nằm trong chính FR đang verify) — nêu rõ để BA biết QA đã chọn
> mốc nào khi đo. Ở **cả hai hướng**, web hiện tại đều **không sai**: Hướng 1 là đúng yêu cầu, Hướng 2 là làm dôi ra.

---

# 10. Dòng 335 · `LBCKQTHCT_01` — Lưu nháp báo cáo kết quả thực hiện chương trình có phải báo "Đã lưu nháp" không

**Bối cảnh phiếu**

- Màn *Chi tiết đợt báo cáo* → lập báo cáo kết quả thực hiện chương trình, vai trò **CB_NV_DP**.
- *Kết quả mong đợi*: cập nhật trạng thái nộp của đơn vị thành *"Đang lập"* · lưu nội dung báo cáo chi tiết ·
  lưu vết thao tác · **hiển thị thông báo nhanh "Đã lưu nháp"**.
- *Kết quả thực tế* đối tác (vòng 1): `403 — Đơn vị không nằm trong phạm vi truy cập của bạn — ERR-AUTH-VPD-00-02`.
  Vòng 2 đối tác báo: *"Hệ thống không chuyển trạng thái thành «Đang lập»"* (không kèm bằng chứng nào).
- QA đo lại **07/08/2026**, tài khoản `cbnv_hn` (CB Nghiệp vụ Địa phương — Sở Tư pháp Hà Nội), đợt
  `DOT-SO_BO_NAM-2026-1`, biểu mẫu 21a, bản dựng `index-DsMHK7Dp.js`.

**3/3 điểm đặc tả CÓ quy định — ĐÃ ĐẠT, không cần BA**

1. Trạng thái nộp của đơn vị chuyển *"Chưa nộp"* → *"Đang lập báo cáo"* và **giữ nguyên sau khi tải lại trang
   bằng địa chỉ**; hệ thống đồng thời sinh bản ghi báo cáo gắn vào đơn vị.
   `srs-fr-15-ct-htpldn.md:746` — *"Cập nhật `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop = DANG_LAP` + `bao_cao_id =
   <bao_cao mới>`"*. ⇒ **Đây chính là điểm đối tác báo hỏng ở vòng 2 — KHÔNG tái hiện.**
2. Nội dung báo cáo chi tiết lưu và **đọc lại đúng từng chữ** sau khi tải lại trang: nhận xét, ghi chú chỉ tiêu và
   2 chỉ tiêu nhập tay đều khớp trên cả giao diện lẫn dữ liệu máy chủ (`:745`).
3. Nhật ký thao tác ghi đủ **3 lượt** (1 lượt bắt đầu lập + 2 lượt cập nhật số liệu), đúng tài khoản, vai trò,
   đơn vị và mốc giờ (`:747`).

Không có hiện tượng gửi trùng: mỗi lần bấm phát sinh **đúng 1** lượt gọi, **đúng 1** thông báo.

**Điểm đặc tả IM LẶNG — cần BA**

- **FR-XI-06** (`srs-fr-15-ct-htpldn.md:701–770`): §Đầu ra chỉ ghi *"Báo cáo CT"* · §Hậu điều kiện chỉ ghi tạo bản
  ghi + ghi nhật ký · §Xử lý lỗi chỉ có `ERR-XI-06-01` · **2 dòng Tiêu chí chấp nhận đều không nhắc thông báo**.
- `srs-fr-15-ct-htpldn.md:1170` (dòng thành phần màn hình #40) liệt kê nhóm nút `[Huy] [Luu nhap] [Trinh duyet KQ]`
  mà **không** đặc tả thông báo — trong khi `:1173` (Gửi lên TW) **lại ghi rõ** *"Toast success"*.
- Cả file chỉ có **3 mã thông báo `INF-`** (`:381`, `:403`, `:1032`), **không mã nào** thuộc FR-XI-06.

**Web hiện tại làm gì** — **ĐÚNG như kỳ vọng đối tác**: bấm `[Lưu nháp]` hiện đúng 1 thông báo *"Đã lưu nháp
thành công"*; bấm `[Lập báo cáo]` hiện *"Đã bắt đầu lập báo cáo"*.

**Câu hỏi cần BA xác nhận — 3 ý**

1. Thao tác **Lưu nháp** ở FR-XI-06 **có bắt buộc** phản hồi thành công cho người dùng không?
2. Nếu có, câu chữ có **bị ràng buộc đúng chuỗi "Đã lưu nháp"** hay chỉ cần một thông báo thành công bất kỳ?
   *(Web đang hiện "Đã lưu nháp **thành công**" — lệch chữ so với phiếu nếu ràng buộc chuỗi chính xác.)*
3. Nếu BA chốt là bắt buộc, đề nghị **bổ sung mã `INF-XI-06-*`** vào bảng thông báo của FR-XI-06 để các vòng sau
   có căn cứ chấm.

> **Ghi nhận thêm (không thuộc phạm vi phiếu, không ảnh hưởng kết luận):** thẻ "Biểu mẫu" và thẻ "Nhận xét, kiến
> nghị" có **2 nút [Lưu nháp] riêng biệt** và **không thấy nút [Hủy]**, trong khi `:1170` mô tả **một nhóm nút
> chung có [Hủy]**. Mỗi thao tác sinh **2 dòng nhật ký** cùng mốc giờ (1 cấp nghiệp vụ + 1 cấp giao tiếp). Đặc tả
> không quy định các điểm này nên chỉ ghi nhận.

---

# 11. Dòng 338 + 339 · `LBCKQTHCT_05/06` — Khối "Nhận xét, kiến nghị" và "Chương trình liên quan" hiện lúc nào

> **Hai dòng chung MỘT câu hỏi, BA chỉ cần trả lời một lần.**
> Dòng **338** `LBCKQTHCT_05` — *"Màn hình Chi tiết không có Khối nhận xét, kiến nghị"*.
> Dòng **339** `LBCKQTHCT_06` — *"Màn hình Chi tiết không có Khối truy vết chương trình liên quan"*.

**Bối cảnh phiếu**

- Màn *Chi tiết đợt báo cáo*, vai trò **CB_NV_DP**. QA đo lại **07/08/2026**, tài khoản `cbnv_hn`, bản dựng
  `index-D4Buvu4S.js`.
- ⚠️ **Về bằng chứng gốc:** `LBCKQTHCT_05.jpg` và `LBCKQTHCT_06.jpg` là **cùng một file ảnh** (trùng mã băm) —
  một ảnh đang dùng cho **hai** khiếu nại về **hai** khối khác nhau; ảnh lại **chỉ bắt phần dưới trang** nên không
  loại trừ được khả năng khối nằm phía trên. QA **không dựa vào ảnh** mà tự tái hiện đúng các bước phiếu mô tả.

**Cả hai khối ĐÃ CÓ và dùng được — không cần BA**

*Khối "Nhận xét, kiến nghị" (dòng 338):*
- Có thẻ *"Nhận xét, kiến nghị"* đặt ngay sau các thẻ biểu mẫu 21a/21b, trước nhóm nút hành động — đúng thứ tự
  đặc tả mô tả. Ô soạn nhiều dòng, giới hạn đúng **5.000 ký tự**, có bộ đếm ký tự trên màn —
  `srs-fr-15-ct-htpldn.md:1169` (*"Nhan xet kien nghi | textarea | Max 5000 ky tu"*).
- Nhập → Lưu nháp: đúng **1** lượt gọi, không gửi trùng. Sau khi **tải lại trang**, nội dung đọc lại đúng từng
  chữ trên cả giao diện lẫn dữ liệu nguồn ⇒ **không phải "khối chỉ có vỏ"**. Kiểm trên **2 bản ghi độc lập**.

*Khối "Chương trình HTPL liên quan trong kỳ" (dòng 339):*
- Có khối nhãn *"Chương trình HTPL liên quan trong kỳ"* kèm mô tả *"Tùy chọn — dùng để truy vết các chương trình
  đơn vị đã triển khai trong kỳ báo cáo"* — gần như nguyên văn `srs-fr-15-ct-htpldn.md:732` (*"Multi-select
  FK → CHUONG_TRINH_HTPL — truy vết các CT đơn vị đã triển khai trong kỳ (tham khảo, không bắt buộc) … Chọn"*).
- Chọn chương trình → Lưu nháp → **tải lại trang**: lựa chọn vẫn còn và dữ liệu nguồn lưu đúng mã chương trình.
- ⚠️ **Một chi tiết dễ hiểu nhầm thành lỗi:** lượt quét đầu, ô chọn mở ra hiện *"Trống"*. **KHÔNG phải lỗi** —
  giao diện gọi đúng địa chỉ và nhận phản hồi thành công với **0 bản ghi**, vì cả **14** chương trình đang có trên
  môi trường đều thuộc **Cục Bổ trợ tư pháp (TW)**, còn đơn vị đang đo (Sở Tư pháp Hà Nội) chưa sở hữu chương
  trình nào. Đúng `:732` thì khối chỉ liệt kê chương trình **của chính đơn vị** ⇒ danh sách rỗng là **phân quyền
  dữ liệu đúng**. QA đã tạo 1 chương trình thử `CT-20260807-0001` cho Sở Tư pháp Hà Nội để kiểm trọn vẹn.

**Vì sao chưa chấm hết lỗi được — CẦN BA**

Làm **đúng 2 bước ghi trong phiếu** (mở menu "Đợt báo cáo" → mở Chi tiết đợt báo cáo) trên một đợt mà **đơn vị
chưa bắt đầu lập báo cáo**, thì màn Chi tiết **CHỈ có thẻ Biểu mẫu 21a** — không có thẻ Nhận xét, kiến nghị,
không có ô soạn nào, không có chữ "Nhận xét" ở bất kỳ đâu trong vùng nội dung; khối truy vết nằm **bên trong** thẻ
đó nên cũng không hiện. **Cả hai khối chỉ xuất hiện sau khi bấm `[Lập báo cáo]`.**
⇒ **Quan sát của đối tác không sai** — chỉ là đo ở thời điểm trước khi bắt đầu lập.

Nhưng cũng **chưa đủ căn cứ kết luận là lỗi**:
- `srs-fr-15-ct-htpldn.md:1169` đặt điều kiện hiển thị khối Nhận xét là *"khi dot o DANG_LAP_BC"* — tức **chỉ yêu
  cầu khối trong pha đang lập**, và **im lặng** về việc màn phải hiển thị gì ở các trạng thái còn lại. Không dòng
  nào buộc phải hiện khối ở dạng **chỉ đọc** trước khi lập.
- Bảng thành phần màn hình của màn Chi tiết đợt báo cáo (`:1163–1175`, gồm 11 dòng) **KHÔNG có dòng nào** khai
  **khối truy vết chương trình liên quan** ⇒ đặc tả không quy định nó phải là khối riêng, đặt ở đâu, hay hiện ở
  trạng thái nào. Yêu cầu về khối này hiện chỉ nằm ở phần **dữ liệu đầu vào** của chức năng Lập báo cáo
  (`:732`, `:744`, `:745`, `:1417`).

**Câu hỏi cần BA xác nhận — 3 ý**

1. Khi đơn vị **chưa vào pha lập báo cáo**, màn Chi tiết đợt báo cáo **có phải** hiển thị phần lập báo cáo — gồm
   khối *"Nhận xét, kiến nghị"* và khối *"Chương trình HTPL liên quan"* — ở **dạng chỉ đọc** không, hay **đúng là
   chỉ hiện khi bắt đầu lập**? Đề nghị bổ sung điều kiện hiển thị cho **các trạng thái còn lại** vào dòng **#39**
   của bảng thành phần màn hình.
2. 🔴 Đặc tả tách **hai bậc trạng thái**: trạng thái của **ĐỢT** (`:1368`, có giá trị `DANG_LAP_BC`) và trạng thái
   nộp của **từng ĐƠN VỊ** (`:1389`, có giá trị *"Đang lập"*). Điều kiện hiển thị ở dòng #39 **chỉ nhắc trạng thái
   của ĐỢT**, trong khi **một đợt dùng chung cho nhiều chục đơn vị**. Đề nghị BA chốt điều kiện hiển thị nên neo
   vào **trạng thái nộp của ĐƠN VỊ** hay **trạng thái của ĐỢT**. *(Hiện phần mềm đang neo vào ĐƠN VỊ.)*
   → **Cùng gốc với câu 12 dưới đây, nên chốt một lần cho cả hai.**
3. Đề nghị bổ sung **một dòng cho khối truy vết chương trình liên quan** vào bảng thành phần màn hình Chi tiết đợt
   báo cáo (hiện dừng ở dòng #45), ghi rõ kiểu điều khiển · vị trí · điều kiện hiển thị. Kèm câu hỏi: khối này
   đang đặt **lồng trong** thẻ "Nhận xét, kiến nghị" — có đúng ý đồ thiết kế không, hay cần **tách thành khối riêng**?

> **Ghi nhận thêm, không thuộc phạm vi phiếu:** danh sách đổ vào ô chọn **không lọc theo trạng thái chương trình**
> (chương trình còn ở *Dự thảo* vẫn xuất hiện) và **không lọc theo kỳ báo cáo**. Đặc tả không quy định các bộ lọc
> này nên chỉ ghi nhận — có thể gộp vào câu 3 nếu BA muốn siết lại.

---

# 12. Dòng 342 · `GKQTHCTHTPL_01` — Trạng thái ở màn Chi tiết đợt là của ĐƠN VỊ hay của ĐỢT

**Bối cảnh phiếu**

- Chức năng *Gửi kết quả thực hiện chương trình hỗ trợ pháp lý lên Trung ương*, vai trò **CB_NV_DP**.
- *Kết quả mong đợi*: chuyển trạng thái đợt báo cáo *Đã duyệt kết quả → Đã gửi Trung ương* · ghi nhận thời điểm
  gửi + đánh dấu vào danh sách tổng hợp TW · gửi thông báo cho CB NV TW · lưu vết · thông báo nhanh *"Đã gửi báo
  cáo lên Trung ương"*.
- *Kết quả thực tế* đối tác: *"Hệ thống hiển thị thông báo **Forbidden**"*.
- QA đo lại **07/08/2026**, tài khoản bấm gửi `cbnv_hn` (CB NV Địa phương — Sở Tư pháp Hà Nội); tiền đề phê duyệt
  do `cbpd_hn` (CB Phê duyệt **cùng đơn vị**, đã đối chiếu trùng mã đơn vị); vế phía TW đo bằng `cbnv_tw` đăng
  nhập riêng, **không dùng tài khoản quản trị**. Đợt `DOT-SO_BO_NAM-2026-1`, phạm vi **83 đơn vị**.

**Lỗi "Forbidden" ĐÃ HẾT — 4/5 vế kỳ vọng đều ĐẠT, không cần BA**

- Trước khi bấm: màn Chi tiết đợt đọc được *"Đã duyệt kết quả"*, có nút `[Gửi lên TW]`. Bấm → hộp xác nhận →
  `[Đồng ý]`: thao tác **thành công**, **KHÔNG còn "Forbidden"**.
- Thông báo nhanh **đúng nguyên văn** câu đối tác kỳ vọng: *"Đã gửi báo cáo lên Trung ương"*. Đúng 1 thông báo
  cho 1 lần bấm, không trùng.
- **Ghi nhận thời điểm gửi:** mốc lưu là 07/08/2026 03:11:24 (giờ VN), lệch ~0,1 s so với lúc bấm. Bảng *"Tiến độ
  nộp theo đơn vị"* (vai trò TW): trong **83** dòng có **đúng một** dòng *"Đã nộp"* — Sở Tư pháp Hà Nội, cấp DP,
  ngày nộp 07/08/2026.
- **Danh sách tổng hợp TW:** đọc bằng chính phiên của CB NV TW — có dòng khớp đủ **ba** yếu tố mã đợt + tên đơn vị
  + ngày gửi.
- **Thông báo cho CB NV TW:** có, trùng mốc giờ, tiêu đề *"Đơn vị đã nộp BC đợt DOT-SO_BO_NAM-2026-1 lên TW"*.
- **Lưu vết:** nhật ký có mục ứng lần gửi, đúng tài khoản `cbnv_hn`, đúng mốc giờ; bước phê duyệt tiền đề cũng ghi
  đúng `cbpd_hn`.

**Vế còn lại — CẦN BA, vì đặc tả TỰ MÂU THUẪN**

Cùng một đợt `DOT-SO_BO_NAM-2026-1`, **sau khi gửi thành công**:
- Màn của cán bộ **Địa phương** (người vừa gửi) đọc: **"Đã gửi TW"**.
- Màn của cán bộ **Trung ương** (bên nhận) đọc: **"Tạo đợt"** — cả ở danh sách đợt lẫn ở Chi tiết đợt. Tab lọc
  *"Đã gửi TW"* trong danh sách đợt của TW **đang rỗng**, không có đợt vừa gửi.
- Dữ liệu nguồn: trạng thái, dấu đã-gửi và thời điểm gửi **đều ghi ở bản ghi THEO TỪNG ĐƠN VỊ**; bản ghi **ĐỢT
  không đổi**.

| Trích dẫn | Nội dung | Nói cấp nào |
|---|---|---|
| `srs-fr-15-ct-htpldn.md:937` | *"Chuyển trạng thái **đợt BC** sang DA_GUI_TW, đánh dấu da_gui_tw, ghi thời điểm gửi \| SM-DOT-BC"* | **ĐỢT** |
| `srs-fr-15-ct-htpldn.md:938` | *"**Sửa theo STT 52 UAT 2026-05-26:** Cập nhật `DOT_BAO_CAO_DON_VI_NOP[dot_id, don_vi_nop_id].trang_thai_nop = DA_NOP` + `ngay_nop = NOW()`"* | **ĐƠN VỊ** |
| `srs-fr-15-ct-htpldn.md:1368` | *"trang_thai … CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP') … Trạng thái lifecycle (SM-DOT-BC: 6 states)"* | mỗi đợt **MỘT** giá trị |
| `:621` · `:646` · `:1398` | Một đợt dùng chung cho **83 đơn vị** | — |

⇒ **Ba dòng này không thể cùng đúng** khi các đơn vị đang ở những bước khác nhau. Vì đặc tả mâu thuẫn, QA **không
được phép tự chọn bên nào là đúng** — không chốt Pass, cũng không mở lại lỗi cho vế này.

**Câu hỏi cần BA xác nhận — 3 ý**

1. Trạng thái mà người dùng nhìn thấy ở màn Chi tiết đợt phải là trạng thái **CỦA ĐƠN VỊ MÌNH** hay trạng thái
   chung **CỦA ĐỢT**? *(Hiện phần mềm cho cán bộ Địa phương thấy trạng thái của đơn vị, còn cán bộ Trung ương
   thấy trạng thái của đợt ⇒ hai vai trò đọc ra hai kết quả khác nhau cho cùng một đợt.)*
2. Nếu chốt theo trục **ĐƠN VỊ**: đề nghị **phát biểu lại `:937` cho khớp `:938`** (bỏ phần chuyển trạng thái đợt),
   đồng thời làm rõ **khi nào thì trạng thái chung của ĐỢT mới đổi** — vì hiện đợt đứng nguyên ở *"Tạo đợt"* suốt
   cả vòng đời, kể cả khi đã có đơn vị nộp xong.
3. Bộ lọc *"Đã gửi TW"* ở danh sách đợt của Trung ương nên hiểu thế nào: liệt kê đợt có **ít nhất một** đơn vị đã
   gửi, hay chỉ đợt mà **toàn bộ** đơn vị đã gửi?

> **Ghi nhận thêm, KHÔNG thuộc phạm vi phiếu và không ảnh hưởng kết luận:**
> - **Đã truy được nguồn của chữ "Forbidden"** mà phiếu mô tả: nếu dùng tài khoản **CẤP TRUNG ƯƠNG** để gọi chức
>   năng gửi lên TW thì hệ thống chặn với đúng chữ *"Forbidden"*. Việc chặn là **ĐÚNG đặc tả** (`:918`, `:922` —
>   chỉ CB NV Bộ/Ngành hoặc Địa phương mới được gửi) ⇒ **không phải lỗi**. Tuy nhiên thông điệp trả về là **chuỗi
>   tiếng Anh thô kèm mã quyền chung**, không phải thông điệp tiếng Việt mà đặc tả **đã khai sẵn** cho chức năng
>   này (`:962` *"Đợt BC chưa được phê duyệt kết quả"* · `:963` *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*).
>   **Đề nghị dev gắn đúng thông điệp đã đặc tả.**
> - Thông báo gửi cho CB NV TW **chỉ nêu mã đợt, không nêu tên đơn vị** đã nộp; đặc tả không quy định nội dung nên
>   chỉ nêu để BA cân nhắc — một đợt có tới 83 đơn vị.
> - Một lần gửi sinh **2 mục nhật ký** cùng mốc giờ; đặc tả không quy định số mục nên chỉ ghi nhận.

---

# Phụ lục A — Phần đã đo và ĐẠT, không cần BA quyết

Ghi ở đây để BA thấy phạm vi tranh chấp chỉ nằm ở 17 điểm trên, **không phiếu nào phải `Reopen`**.

| Dòng · Phiếu | Vế đã đo ĐẠT |
|---|---|
| 20 `QLLKHDTBD_09` | Xuất Excel **bám đúng bộ lọc**: lọc còn 4 → tệp 4 dòng, lọc còn 1 → tệp 1 dòng (danh sách chưa lọc có 14) ⇒ triệu chứng "xuất toàn bộ" không tái hiện |
| 32 `QLTVV_02` | 4/5 vế: cột Điểm ĐG không tràn/đè (26 lượt đo toạ độ × 4 bề rộng) · Điểm ĐG hiển thị đồng nhất · nút thao tác không xuống dòng · mặc định 20 bản ghi/trang |
| 35 `DKTGMLTVV_13` | Tạo được hồ sơ `TVV-STP-AG-0004` · đơn vị tự gán đúng theo NHT · trạng thái `Mới đăng ký` · đủ **cả 2** lĩnh vực đã chọn · đúng tổ chức chính · Cán bộ Nghiệp vụ **cùng đơn vị** nhận thông báo sau thao tác 52 ms, đúng tên ứng viên · Nhật ký hệ thống có dòng `Tạo mới` / `TU_VAN_VIEN` / mã bản ghi khớp · câu thông báo đúng nguyên văn |
| 65 `DGKQHTVV_02` | 3/6 vế: nhóm Đánh giá đủ 5 trường (14/14 ô hiển thị thật) · giá trị trên màn khớp bản ghi đã lưu (2 đường đo) · toàn tiếng Việt, không lộ mã kỹ thuật, không `null`/`undefined` |
| 149 `QLDMTCTV_12` | 5/5 vế còn lại PASS (chỉ vướng mốc tối đa ở vế C6) |
| 288 `QLNDTVVCG_38` | 4/4 vế `MATCH` (C1–C4) — chọn nhiều dòng · thanh hành động hàng loạt · cửa sổ phân công mở ra · sau tải lại cả 2 hồ sơ đều có chuyên gia |
| 297 `QLHSPLDN_15` | Vế **lọc rồi xuất**: lọc còn 2 dòng thì tệp xuất đúng 2 dòng, lời gọi mang theo bộ lọc |
| 301 `QLTLPLCVV_22` | Tìm bằng từ khóa **có dấu** → bảng từ 2 dòng còn đúng 1 dòng mong đợi, khớp phản hồi máy chủ (`total = 1`) |
| 302 `QLTLPLCVV_23` | Tìm bằng từ khóa **không dấu** → ra đúng bản ghi có dấu, tập mã trùng khít lượt có dấu |
| 335 `LBCKQTHCT_01` | 3/3 điểm đặc tả có quy định: trạng thái nộp đơn vị chuyển `DANG_LAP` và giữ sau tải lại · nội dung báo cáo đọc lại đúng từng chữ · nhật ký ghi đủ 3 lượt. Lỗi `403 ERR-AUTH-VPD-00-02` **đã hết** |
| 338 `LBCKQTHCT_05` | Khối "Nhận xét, kiến nghị" **có**, đúng vị trí, giới hạn đúng 5.000 ký tự + bộ đếm; lưu và đọc lại đúng từng chữ sau tải lại, kiểm trên 2 bản ghi độc lập |
| 339 `LBCKQTHCT_06` | Khối "Chương trình HTPL liên quan" **có**, đúng kiểu multi-select, mô tả gần nguyên văn `:732`; chọn → lưu → tải lại vẫn còn, dữ liệu nguồn đúng mã |
| 342 `GKQTHCTHTPL_01` | Lỗi **"Forbidden" đã hết**; 4/5 vế đạt — thông báo đúng nguyên văn · mốc gửi ghi đúng (83 đơn vị, đúng 1 dòng "Đã nộp") · có trong danh sách tổng hợp TW · CB NV TW nhận thông báo · nhật ký đúng tài khoản |

**Khai mutate môi trường:** các lượt đo có tạo/đổi dữ liệu trên **env nội bộ** — 1 tư liệu *"Nghị định 55/2019…"*
(Nháp) gắn vào `TVCS-20260806-0003` · 1 hồ sơ TVV `TVV-STP-AG-0004` (`MOI_DANG_KY`) kèm 2 tệp PDF ·
`TVCS-QLND38-UAT-01/02` chuyển `TIEP_NHAN → PHAN_CONG` · `TC-TW-DEMO-001` đổi trạng thái rồi đưa lại
`HOAT_DONG` · 1 chương trình thử `CT-20260807-0001` cho Sở Tư pháp Hà Nội (dòng 339) · đợt
`DOT-SO_BO_NAM-2026-1` được QA đưa qua bước phê duyệt rồi nộp lên TW để đo dòng 342 (**có thể đưa về trạng thái
cũ** sau khi đối tác đọc xong). **Không đụng dữ liệu của đối tác**, không sửa/xóa bản ghi có sẵn.

---

# Phụ lục B — 🔴 Câu hỏi BA khác đang treo trong hồ sơ QA nhưng **sheet CHƯA đánh `BA confirm`**

> **Vì sao tách riêng:** bộ 13 dòng ở trên lấy đúng theo bộ lọc *`Trạng thái dev fix = BA confirm`* trên tab `bug`.
> Các dòng dưới đây **đã có câu hỏi BA viết sẵn trong hồ sơ QA** nhưng ô `Trạng thái dev fix` trên sheet vẫn đang
> là `UAT done` / `Test done` ⇒ **không lọt bộ lọc**. Hoặc câu hỏi đã được giải quyết mà hồ sơ chưa dọn, hoặc sheet
> chưa được cập nhật. **Cần người điều phối chốt** trước khi gửi BA — QA không tự đổi ô sheet.

| Dòng | Mã TC | Ô `Trạng thái dev fix` hiện tại | Điểm cần BA (theo hồ sơ QA) | File nguồn |
|---:|---|---|---|---|
| **169** | `QLDKTK_10` | `UAT done` | 🔴 DN đặt mật khẩu ở **form đăng ký** (`srs-fr-10-quan-tri.md:1070-1071`) hay ở **màn kích hoạt** (`:1109`/`:1116`/`:2299`)? Đặc tả nói **cả hai hướng loại trừ nhau**; web làm theo form đăng ký | [`ba-confirm-lo-F5.md`](ba-confirm-lo-F5.md) §Q1 |
| **286** | `QLNDTVVCG_24` | `Test done` | Sự kiện "chuyên gia xác nhận nhận việc" gửi thông báo qua **kênh nào** — chỉ in-app (hiện trạng) hay in-app + email theo `BR-NOTIF-01`? Nếu chọn email → đổi từ Pass sang Còn lỗi, `Dev BE` | [`ba-confirmation-needed-QLNDTVVCG-2026-08-06.md`](ba-confirmation-needed-QLNDTVVCG-2026-08-06.md) |
| **286** (phụ) | `QLNDTVVCG_24` | `Test done` | Nội dung TVCS giao cho **chỉ CG** (hiện trạng) hay **cả CG lẫn TVV** (`srs-fr-12:172` viết *"CG/TVV"*)? | ⌐ nt |
| **287** | `QLNDTVVCG_26` | `UAT done` | Sau khi chuyên gia từ chối, màn hình ở nguyên Chi tiết (hiện trạng) hay tự quay về Danh sách như đối tác mong đợi? | ⌐ nt |
| **127** | `LKHDG_16` | `UAT done` | Form Sửa kế hoạch đang hiển thị "Tài liệu đính kèm" nhưng đặc tả màn hình không liệt kê thành phần này | [`ba-confirmation-needed-LKHDG-2026-08-06.md`](ba-confirmation-needed-LKHDG-2026-08-06.md) |
| **189 · 222 · 226 · 230 · 234** | `VVDHTHT_06` · `VVTDVQL_06` · `VVTLV_05` · `VVTLHDN_05` · `VVTTGCT_05` | `Test done` (ô DEV ghi *"chưa tái hiện được lỗi"*) | Vai trò **QTHT** có được **xuất tệp** báo cáo không? Hai hướng cho **hai owner khác nhau** (`Dev FE` vs `Dev BE`) | [`cau-hoi-BA.md`](cau-hoi-BA.md) |
| — | (housekeeping) | — | 5 câu dọn đặc tả phiên đăng nhập: mốc cảnh báo 25 hay 30 phút · câu chữ + nhãn nút hộp thoại · hành vi nút [Gia hạn phiên] + có giới hạn số lần gia hạn không · câu thông báo hết phiên đang có **4 dạng lệch nhau** · lọc trạng thái ở màn Tổ chức tư vấn | [`ba-confirm-lo-F5.md`](ba-confirm-lo-F5.md) §Q3–Q7 |

---

# Phụ lục C — File nguồn của 13 dòng trong bảng chính

| Dòng | Mã TC | File nguồn (nội dung đầy đủ + evidence) |
|---:|---|---|
| 20 | `QLLKHDTBD_09` | [`../F5-flow04-2026-08-07/do/QLLKHDTBD_09.md`](../F5-flow04-2026-08-07/do/QLLKHDTBD_09.md) · [`../F5-flow04-2026-08-07/chuan/QLLKHDTBD_09.md`](../F5-flow04-2026-08-07/chuan/QLLKHDTBD_09.md) |
| 32 | `QLTVV_02` | [`../../batch-B7-tuvan-mangluoi-2026-08-06/ketqua-QLTVV_02.txt`](../../batch-B7-tuvan-mangluoi-2026-08-06/ketqua-QLTVV_02.txt) · [`../../batch-B7-tuvan-mangluoi-2026-08-06/cau-hoi-BA.md`](../../batch-B7-tuvan-mangluoi-2026-08-06/cau-hoi-BA.md) |
| 35 · 301 · 302 | `DKTGMLTVV_13` · `QLTLPLCVV_22/23` | [`ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md`](ba-confirmation-needed-F6-QLTLPLCVV-DKTGMLTVV-2026-08-07.md) |
| 65 | `DGKQHTVV_02` | [`../F6-flow04-devfix-2026-08-07/do/DGKQHTVV_02.md`](../F6-flow04-devfix-2026-08-07/do/DGKQHTVV_02.md) §7 · [`../F6-flow04-devfix-2026-08-07/BAN-GIAO.md`](../F6-flow04-devfix-2026-08-07/BAN-GIAO.md) |
| 149 | `QLDMTCTV_12` | [`ba-confirm-lo-F5.md`](ba-confirm-lo-F5.md) §Q2 · [`../F5-devfix-2026-08-07/do/QLDMTCTV_12.md`](../F5-devfix-2026-08-07/do/QLDMTCTV_12.md) |
| 288 | `QLNDTVVCG_38` | [`../F6-flow04-devfix-2026-08-07/do/QLNDTVVCG_38.md`](../F6-flow04-devfix-2026-08-07/do/QLNDTVVCG_38.md) §8 · [`../F6-flow04-devfix-2026-08-07/BAN-GIAO.md`](../F6-flow04-devfix-2026-08-07/BAN-GIAO.md) |
| 297 | `QLHSPLDN_15` | [`ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md`](ba-confirmation-needed-QLHSPLDN_15-2026-08-07.md) |
| 335 | `LBCKQTHCT_01` | [`../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_01.md`](../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_01.md) |
| 338 | `LBCKQTHCT_05` | [`../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_05.md`](../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_05.md) |
| 339 | `LBCKQTHCT_06` | [`../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_06.md`](../F5-devfix-BCCT-2026-08-07/do/LBCKQTHCT_06.md) |
| 342 | `GKQTHCTHTPL_01` | [`../F5-devfix-BCCT-2026-08-07/do/GKQTHCTHTPL_01.md`](../F5-devfix-BCCT-2026-08-07/do/GKQTHCTHTPL_01.md) |

> ⚠️ **Đính chính một chỗ trỏ sai đang lưu hành:** dòng **288** `QLNDTVVCG_38` **KHÔNG** nằm trong
> `ba-confirmation-needed-QLNDTVVCG-2026-08-06.md` — file đó chứa câu hỏi của dòng **286** (`QLNDTVVCG_24`) và
> **287** (`QLNDTVVCG_26`). Câu hỏi của dòng 288 nằm ở `F6-flow04-devfix-2026-08-07/do/QLNDTVVCG_38.md §8`.

---

# Phụ lục D — 7 dòng `BA confirm` KHÔNG đưa vào file này (BA đã chốt hoặc không phải việc của BA)

Ghi lại để người đọc kiểm chứng được bộ lọc 20 → 13.

| Dòng | Mã TC | Nội dung ô `DEV phản hồi lần 1` (rút gọn) |
|---:|---|---|
| 10 | `KTDGKQHT_05` | *"BA chốt 04/08/2026 — phiếu bàn giao thay đổi SRS (FR-III-05 + SCR-III-02 Tab 4/5)… Dev đã làm theo đặc tả mới, đã lên bản v1.0.10."* |
| 308 | `QLHDTVVCG_02` | *"BA chốt 06/08/2026 — cụm Hợp đồng tư vấn (27 phiếu), Loại 4 hướng A: giữ quyết định BA 11/05/2026 bỏ menu riêng…"* |
| 319 | `QLHDTVVCG_13` | *"BA chốt 06/08/2026 — … test case mô tả lối vào đã hết hiệu lực. Không sửa phần mềm theo lối vào cũ."* |
| 321 | `QLHDTVVCG_15` | *"BA chốt 06/08/2026 — Loại 4 hướng B: lấy câu theo bản bàn giao .docx là "Đã lưu hợp đồng"… Dev đã dùng chung câu INF-HDTV-01."* |
| 343 | `THBCTHCT_01` | *"…thuộc nhóm Dev tự fix theo căn cứ SRS rõ ràng, **BA không phải quyết**. Căn cứ: INF-XI-09-01."* |
| 344 | `THBCTHCT_02` | *"…nhóm Dev tự fix theo căn cứ SRS rõ ràng, **BA không phải quyết**."* |
| 345 | `THBCTHCT_05` | *"BA chốt 06/08/2026, hai ý: (1) tên tệp nâng thành quy ước dùng chung, đưa vào Phụ lục E; (2) khối ký mở rộng ngoại lệ §D.2.4…"* |
