# BA confirmation needed — Tổ chức tư vấn (tab UAT tuần 3, verify vòng 1) — 2026-08-03

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được**, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report.

> **Phạm vi:** **3 mục** cần BA quyết, thuộc rows **339, 332, 331** của tab `UAT_TGPL Doanh Nghiệp-tuần 3` (gid `387857822`), sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`.
> **Cả 3 đều thuộc DẠNG B** (SRS tự mâu thuẫn hoặc lệch bản đã duyệt → cần BA chốt source truth). **Không có TC dạng A.**
> Cả 3 đều là **dòng QA tự mở thêm** (`_OOS_`), phát sinh khi kiểm 4 phiếu `QLDMTCTV_02 / _05 / _06 / _09` ngày 03/08/2026 — không nằm trong phạm vi phiếu gốc của đối tác.
> **Chức năng:** Quản lý Tổ chức tư vấn (FR-IV-NEW-01) — màn `SCR-IV-NEW-01` (danh sách) và `SCR-IV-NEW-02` (biểu mẫu thêm/sửa).
> **Môi trường:** `https://18.143.165.120.nip.io` · bản dựng **HTPLDN V1.0.5** · ngày 03/08/2026 · tài khoản `cbnv_tw_04` (`CB_NV_TW`) và `cbpd_tw_04` (`CB_PD_TW`), đơn vị Cục Bổ trợ tư pháp — Bộ Tư pháp.
> **Nguồn SRS quote số dòng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` (2543 dòng).

## Thứ tự ưu tiên

| # | Row | Mã TC | Cần BA quyết điều gì | Ảnh hưởng |
|:-:|:-:|---|---|---|
| 1 | 339 | `QLDMTCTV_OOS_13` | Giấy ĐKHĐ: chốt **một tên gọi** + **một mức bắt buộc** | **Chạm chức năng** — nếu chốt bắt buộc, hồ sơ cũ thiếu dữ liệu sẽ không lưu lại được |
| 2 | 332 | `QLDMTCTV_OOS_06` | Số lượng thẻ trạng thái: **6** hay **3** | Tài liệu — chưa chốt thì mọi lượt kiểm sau vẫn báo lệch |
| 3 | 331 | `QLDMTCTV_OOS_05` | Cột "Đơn vị quản lý": giữ và bổ sung vào đặc tả, hay bỏ | Hiển thị — mức Minor |

> **Mục 1 và 2 là lỗi của TÀI LIỆU, không phải lỗi phần mềm** — BA sửa đặc tả là xong, Dev không phải đụng gì (trừ khi mục 1 chốt theo hướng đổi tên nhãn / đổi tính bắt buộc). Chỉ mục 3 mới có thể dẫn tới việc sửa giao diện.

> **⚠️ Ghi chú phạm vi — đã lược bớt so với bản đầu:** trước khi rà lại, tab tuần 3 có **4** dòng mang trạng thái `BA confirm` (330, 331, 332, 339). QA rà lại và **loại 1 dòng cùng 2 ý con** vì đánh giá là **không phải lỗi, không cần BA quyết**:
> - Row **330 `QLDMTCTV_OOS_04`** (thẻ 0 hồ sơ không hiện số đếm) — ẩn huy hiệu khi bằng 0 là hành vi mặc định của thư viện giao diện, và đặc tả không quy định trường hợp bằng 0.
> - Ý "thứ tự thẻ trạng thái" của row **332**, và ý "thứ tự trường trên biểu mẫu" của row **339** — bảng thành phần màn hình là bảng liệt kê thành phần, không phải bản vẽ bố cục.
>
> **Sheet đã được đồng bộ theo file này ngày 03/08/2026:** row 330 đổi `BA confirm` → **`Reject`** (cả cột P và Verify) kèm note giải thích; note cột "DEV phản hồi lần 1" của row 332 và 339 đã gỡ 2 ý rút lại và ghi rõ lý do rút. Bản sao nguyên văn P/Q/R trước khi sửa: `reverify-audit/BACKUP-sheet-tuan3-rows-330-331-332-339-truoc-khi-sua-2026-08-03.json`. Sau đồng bộ, tab tuần 3 còn **3** dòng `BA confirm` — đúng bằng 3 mục của file này.

> **⚠️ Nguồn gốc số liệu — đọc trước khi dùng file:** các case này do **tổ verify Luồng 4 (Tổ chức tư vấn)** đo trên giao diện, QA lập file này **không tự chạy lại UI**. Phần QA lập file đã tự làm để bảo chứng:
> - Mở `srs-fr-04-chuyen-gia-tvv.md` kiểm **từng số dòng** được trích — **đúng 100%**, không dòng nào lệch hay rỗng.
> - Mở **cả 3 ảnh bằng chứng** đọc pixel, đối chiếu với lời mô tả — **khớp**; chi tiết đọc được ghi trong từng mục.
> - Chỗ nào ảnh **không đủ** để tự xác nhận (vd tổng số cột của bảng khi có cuộn ngang) đều ghi rõ là "theo ghi nhận của tổ verify", không nhận là quan sát của người lập file.

> **⚠️ Ghi chú tham chiếu chung:** chức năng "Quản lý Tổ chức tư vấn" (FR-IV-NEW-01) trong đặc tả **không được cấp mã UC** — dòng `1029` ghi nguyên văn `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])`. Vì vậy mọi mục dưới đây chỉ dẫn tên chức năng + số dòng, không có mã UC để trích.

---

## 1. QLDMTCTV_OOS_13 — Giấy đăng ký hoạt động: đặc tả dùng 3 tên gọi khác nhau và 2 mức bắt buộc trái ngược nhau

> **Ghi chú:** dòng này **tách ra từ `QLDMTCTV_OOS_10`**. Phần "thứ tự trường trên biểu mẫu" của dòng gốc đã được QA loại khỏi file (xem §Ghi chú phạm vi) — mục này chỉ còn phần Giấy đăng ký hoạt động.

**Bối cảnh testcase**

- Dòng Excel: **339**, mã TC `QLDMTCTV_OOS_13` (dòng QA tự mở thêm).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`) bấm "Thêm mới" mở biểu mẫu Thêm mới Tổ chức tư vấn, đọc nhãn và tính bắt buộc của trường Giấy đăng ký hoạt động, rồi đối chiếu với đặc tả.
- Tiền đề: không cần dữ liệu — chỉ đọc nhãn trường trên biểu mẫu.

**Kết quả verify UI hiện tại**

- **Đọc trực tiếp từ ảnh bằng chứng (người lập file tự mở, không đọc lại từ mô tả):** nhãn trường trên biểu mẫu là **"Số Giấy ĐKHĐ Sở TP"**, kèm trường **"Ngày cấp"**.
- Cả hai trường **đều có dấu `*` đỏ ⇒ phần mềm đang đặt là bắt buộc**.
- Tức phần mềm đang theo cách gọi của `:1073` + `:2216` ("Giấy ĐKHĐ Sở TP") và theo hướng **bắt buộc**.
- Evidence: `image/QLDMTCTV_OOS_10-nhan-truong-bieu-mau-them-moi.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. **TÊN GỌI — chính đặc tả gọi cùng một giấy tờ bằng BA cách khác nhau:**
   - `:1681` / `:1682` — "Số **Giấy đăng ký hành nghề**" / "Ngày cấp **Giấy đăng ký hành nghề**"
   - `:1073` — "**Giấy đăng ký hoạt động Sở TP**"
   - `:2216` / `:2217` — "**Giấy ĐKHĐ Sở TP**", nhãn hiển thị "Số giấy ĐKHĐ" / "Ngày cấp giấy ĐKHĐ"

   **Lưu ý nghiệp vụ:** "đăng ký **hoạt động**" và "đăng ký **hành nghề**" là **hai loại giấy tờ khác nhau** theo NĐ 77/2008, không phải hai cách viết tắt của cùng một giấy. Chốt sai tên sẽ dẫn tới thu thập sai giấy tờ.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1681`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1682`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1073`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2216`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2217`

2. **TÍNH BẮT BUỘC — hai bảng dữ liệu trong đặc tả ghi ngược nhau:**
   - `:1052` / `:1053` — bảng Inputs khai `so_giay_dkhd` và `ngay_cap_dkhd` cột Bắt buộc = **"N"** (không bắt buộc).
   - `:1073` / `:1681` / `:1682` / `:2216` / `:2217` — đều ghi **bắt buộc**, dẫn NĐ 77/2008 Đ.13 làm căn cứ.

   Phần mềm đang đặt **bắt buộc**, tức theo hướng đa số. **Hệ quả thực tế nếu chốt bắt buộc:** hồ sơ tổ chức đã có sẵn mà thiếu hai thông tin này sẽ **không lưu lại được** nếu không bổ sung — đây là rủi ro cần BA cân nhắc trước khi chốt.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1052`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1053`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1073`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:2216`

**Câu hỏi cần BA xác nhận**

Đề nghị BA chốt **một tên gọi chuẩn** và **một mức bắt buộc duy nhất**, rồi sửa đặc tả cho khớp ở **cả bốn chỗ** (`:1052`–`:1053`, `:1073`, `:1681`–`:1682`, `:2216`–`:2217`).

1. **Tên chuẩn** là "Giấy đăng ký **hoạt động**" hay "Giấy đăng ký **hành nghề**"?
2. **Bắt buộc hay không bắt buộc?** Nếu chốt **bắt buộc**, BA cần chốt thêm cách xử lý hồ sơ cũ đang thiếu dữ liệu:
   - (a) cho lưu tiếp, chỉ bắt buộc với hồ sơ tạo mới; hoặc
   - (b) bắt bổ sung, chấp nhận hồ sơ cũ không sửa được cho tới khi có đủ giấy tờ.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt.
- Tạm verdict cho `QLDMTCTV_OOS_13`: **`Cần BA xác nhận`** (đã ghi `BA confirm` ở cột `Verify` row 339).
- Đây là **mâu thuẫn nội bộ đặc tả, không phải lỗi phần mềm** — owner chính là **BA**. Sau khi chốt mới xác định được phần mềm có phải sửa nhãn hoặc sửa tính bắt buộc hay không.
- **Ưu tiên trả lời ý bắt buộc trước:** đây là nội dung duy nhất trong cả nhóm có thể **chặn người dùng lưu hồ sơ**; các mục còn lại chỉ ảnh hưởng hiển thị.

---

## 2. QLDMTCTV_OOS_06 — Đặc tả tự mâu thuẫn về SỐ LƯỢNG thẻ trạng thái: 6 tab (phần màn hình) vs 3 tab (Tiêu chí chấp nhận)

> **Ghi chú:** phần "thứ tự thẻ trạng thái" của dòng gốc đã được QA loại khỏi file (xem §Ghi chú phạm vi) — mục này chỉ còn phần số lượng thẻ.

**Bối cảnh testcase**

- Dòng Excel: **332**, mã TC `QLDMTCTV_OOS_06` (dòng QA tự mở thêm).
- Nội dung kiểm tra: Cán bộ Phê duyệt cấp Trung ương (`cbpd_tw_04`) mở màn "Tổ chức tư vấn", đếm số thẻ trạng thái rồi đối chiếu với đặc tả.
- Tiền đề: tài khoản Cán bộ Phê duyệt thấy đủ 6 thẻ (thẻ "Chờ phê duyệt" chỉ hiện với vai trò này).

**Kết quả verify UI hiện tại**

- **Đọc trực tiếp từ ảnh bằng chứng:** thanh thẻ của `cbpd_tw_04` có đúng **6 thẻ**: Đang hoạt động (3) · Chờ phê duyệt (1) · Mới đăng ký (1) · Đã từ chối · Tạm dừng · Vô hiệu hóa.
- Ảnh của `cbnv_tw_04` cho thấy vai trò Cán bộ Nghiệp vụ chỉ có **5 thẻ** (không có "Chờ phê duyệt") — đúng như đặc tả quy định thẻ này chỉ hiện với Cán bộ Phê duyệt.
- ⇒ Phần mềm hiển thị **5 thẻ với CB Nghiệp vụ / 6 thẻ với CB Phê duyệt**, không có vai trò nào thấy 3 thẻ.
- Evidence: `image/QLDMTCTV_05-cbpd-tw-04-thanh-the-co-cho-phe-duyet.png` · `image/QLDMTCTV_05-cbnv-tw-04-thanh-the-truoc-khi-seed.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. **Phần màn hình `SCR-IV-NEW-01` khẳng định 6 thẻ ở 3 chỗ độc lập:**
   - `:1610` — "Danh sách **6 tab** + thao tác hàng loạt + nhanh hành động cập nhật trạng thái"
   - `:1617` — "…Hiển thị **6 tab**…"
   - `:1625`–`:1630` — bảng thành phần liệt kê đủ 6 thẻ (Đang hoạt động · Tạm dừng · Mới đăng ký · Chờ phê duyệt · Đã từ chối · Vô hiệu hóa)

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1610`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1617`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1625`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1630`

2. **Nhưng Tiêu chí chấp nhận của chính chức năng lại ghi 3 thẻ:**
   - `:1129` — "**Given** CB NV truy cập "Quản lý tổ chức tư vấn" **When** hiển thị **Then** danh sách TC TV thuộc đơn vị, **3 tab trạng thái**"

   ⇒ Hai chỗ này dẫn tới **hai kết luận kiểm thử trái ngược nhau**: theo `:1129` thì phần mềm đang hiển thị **thừa thẻ**; theo `:1610`/`:1617` thì đúng. Con số 3 không khớp với bất kỳ vai trò nào trên phần mềm (5 hoặc 6), nên nhiều khả năng là **sót lại từ bản đặc tả cũ chưa cập nhật**.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1129`

**Câu hỏi cần BA xác nhận**

Số lượng thẻ trạng thái đúng của màn danh sách Tổ chức tư vấn là bao nhiêu?

1. **Hướng 1 — 6 thẻ** (theo phần màn hình `:1610` / `:1617` / `:1625`–`:1630`): phần mềm đang **đúng**; đề nghị sửa Tiêu chí chấp nhận `:1129` cho khớp, và ghi rõ thẻ "Chờ phê duyệt" chỉ hiện với Cán bộ Phê duyệt nên Cán bộ Nghiệp vụ thấy 5 thẻ.
2. **Hướng 2 — 3 thẻ** (theo `:1129`): phần mềm đang hiển thị thừa; BA cần chỉ rõ **3 thẻ nào** được giữ và sửa lại bảng thành phần `:1625`–`:1630` cho khớp.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt.
- Tạm verdict cho `QLDMTCTV_OOS_06`: **`Cần BA xác nhận`** (đã ghi `BA confirm` ở cột `Verify` row 332).
- QA nghiêng về **hướng 1** — phần màn hình mô tả chi tiết hơn, nhất quán ở 3 chỗ, và khớp với hành vi phần mềm; `:1129` nhiều khả năng là dòng cũ chưa cập nhật. Nhưng QA **không tự chốt** vì đây là hai phần của cùng một tài liệu đã duyệt.
- Chừng nào `:1129` còn ghi "3 tab" thì **mọi lượt kiểm sau vẫn sẽ báo lệch**. Owner: **BA sửa đặc tả**.

---

## 3. QLDMTCTV_OOS_05 — Bảng danh sách có thêm cột "Đơn vị quản lý" không nằm trong danh sách cột của đặc tả

> **Ưu tiên thấp** — mức Minor, chỉ ảnh hưởng hiển thị. Đưa vào file vì đây là **lệch so với bảng thành phần màn hình đã duyệt**, việc giữ hay bỏ thuộc thẩm quyền BA, không phải QA tự quyết.

**Bối cảnh testcase**

- Dòng Excel: **331**, mã TC `QLDMTCTV_OOS_05` (dòng QA tự mở thêm).
- Nội dung kiểm tra: Cán bộ Nghiệp vụ cấp Trung ương (`cbnv_tw_04`) mở màn "Tổ chức tư vấn", đọc lần lượt toàn bộ tiêu đề cột của bảng từ trái sang phải rồi đối chiếu với bảng thành phần màn hình.
- Tiền đề: 3 tổ chức ở thẻ "Đang hoạt động".

**Kết quả verify UI hiện tại**

- **Đọc trực tiếp từ ảnh bằng chứng:** các cột nhìn thấy trong khung hình, theo thứ tự trái→phải, là *ô chọn · STT · Mã tổ chức · Tên tổ chức · Loại hình · Lĩnh vực · **Đơn vị quản lý** · Hành động*. Cột "Đơn vị quản lý" có dữ liệu thật ("Sở Tư pháp An Giang", "Cục Bổ trợ tư pháp - Bộ Tư pháp").
- Ảnh cho thấy **thanh cuộn ngang** dưới bảng và cột "Hành động" bị ghim bên phải ⇒ còn cột nằm ngoài khung. Chân bảng ghi "Hiển thị 1-3 / 3 kết quả".
- **Theo ghi nhận của tổ verify** (phần này ảnh không đủ để người lập file tự xác nhận vì có cột khuất): bảng có **11 cột**, cột "Đơn vị quản lý" đặt giữa "Lĩnh vực" và "Người đại diện"; không thiếu thông tin nào, nhưng bảng rộng thêm nên phải cuộn ngang mới thấy 3 cột cuối (Trạng thái, Công khai, Hành động).
- Evidence: `image/QLDMTCTV_05-cbnv-tw-04-thanh-the-truoc-khi-seed.png`

**Điểm mâu thuẫn trong SRS v3.5**

1. **Đặc tả liệt kê đúng 10 cột cho bảng danh sách**, và "Đơn vị quản lý" **không nằm trong đó**: *Ô chọn · Số thứ tự · Mã tổ chức · Tên tổ chức · Loại hình · Người đại diện · Lĩnh vực · Trạng thái · Công khai · Hành động*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1637`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1646`

2. **"Đơn vị quản lý" được đặc tả gán vai trò khác — bộ lọc, không phải cột bảng:** khai là thành phần vùng "bộ lọc", loại UI "dropdown có tìm kiếm", hành vi "Lọc theo đơn vị quản lý Tổ chức tư vấn". Ảnh cho thấy phần mềm **đã có** bộ lọc này ở thanh lọc **và đồng thời** thêm nó làm cột.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1634`

3. **Khoảng trống khiến QA không tự chốt được:** đặc tả liệt kê danh sách cột nhưng **không có câu nào cấm thêm cột**, cũng không ghi danh sách này là đóng. Thêm cột "Đơn vị quản lý" có thể là **cải tiến hợp lý** với tài khoản cấp Trung ương (nhìn được tổ chức của nhiều Sở), nên không kết luận được là lỗi.

**Câu hỏi cần BA xác nhận**

Cột **"Đơn vị quản lý"** trên bảng danh sách Tổ chức tư vấn cần xử lý thế nào?

1. **Hướng 1 — giữ cột.** Công nhận đây là cải tiến cần thiết cho tài khoản cấp Trung ương, và **bổ sung cột này vào danh sách cột trong đặc tả** (`:1637`–`:1646`) để lần kiểm sau không báo lệch nữa.
2. **Hướng 2 — bỏ cột.** "Đơn vị quản lý" chỉ giữ vai trò bộ lọc như `:1634`; bảng trở về đúng 10 cột, hết phải cuộn ngang để xem Trạng thái / Công khai / Hành động.

**Đề xuất QA tạm thời**

- Chưa gửi Dev cho tới khi BA chốt.
- Tạm verdict cho `QLDMTCTV_OOS_05`: **`Cần BA xác nhận`** (đã ghi `BA confirm` ở cột `Verify` row 331).
- Nếu BA chọn **hướng 1**: phần mềm **không phải lỗi**, owner là **BA cập nhật đặc tả**; QA đóng dòng này.
- Nếu BA chọn **hướng 2**: phần mềm `Vẫn lỗi`, owner dự kiến **Dev FE** — mức Minor.
- **Không phụ thuộc hướng nào — đề nghị BA cân nhắc thêm:** dù giữ hay bỏ cột, việc 3 cột cuối (Trạng thái, Công khai, Hành động) chỉ thấy được sau khi cuộn ngang là điểm bất lợi về sử dụng, vì Trạng thái và Công khai là 2 thông tin người dùng cần nhìn ngay.
