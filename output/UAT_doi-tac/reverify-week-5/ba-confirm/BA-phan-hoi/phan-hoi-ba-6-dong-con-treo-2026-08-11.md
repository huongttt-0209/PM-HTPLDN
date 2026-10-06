# Phiếu phản hồi — 6 dòng còn treo `BA confirm` sau đợt duyệt 08–09/08 — 2026-08-11

**Nguồn vào:** `Week5/Yêu cầu/ba-confirmation-needed-6-dong-con-treo-2026-08-10.md` (giữ nguyên làm vết lượt đo 10/08) + `Week5/Yêu cầu/GUI-BA-tong-hop-13-dong-BA-confirm-2026-08-07.md` + `Week5/Yêu cầu/cau-hoi-ba-DGKQHTVV_01-pham-vi-nhin-cua-DN.md`.

| Mục | Giá trị |
|---|---|
| Bản chấm chuẩn (`.md`) | `_bmad-output/planning-artifacts/srs-v3.5/` |
| Bản bàn giao đối chiếu (`.docx`) | `docs/Reference/_backup_HTPLDN-PTYC-CT-v3.5_pre-sync-md_20260808-0903.docx` — ảnh chụp bản v3.5 **trước lượt sửa 08/08**, tức bản có hiệu lực khi đối tác ghi nhận lỗi (05–07/08). Bản v3.5 dựng lại toàn bộ mục 4 ngày 31/07–01/08 theo `_bmad-output/NGUON-CUA-BAN-BAN-GIAO.md` |
| ⚠️ Kênh gửi bản `.docx` | **Chưa ghi nhận được ngày bàn giao và kênh gửi.** Đã tra chéo với bản hiện hành (`HTPLDN-PTYC-CT-v3.5.docx`, 08/08 10:20) — mọi trích dẫn dùng trong phiếu này **giống nhau ở cả hai bản**, nên kết luận không phụ thuộc bản nào |
| Bản dựng đo | `https://18.143.165.120.nip.io` · bó mã `assets/index-LoDAkSbB.js` · `Fri, 07 Aug 2026 15:26:56 GMT` · đo 10/08/2026 |
| Sổ theo dõi | ⚠️ **Chưa hỏi đường dẫn + `gid` của đợt này.** Phải hỏi và thử ghi một ô nháp trước khi cập nhật (Pha 0) |

---

## Thay đổi kể từ lượt duyệt gần nhất

Hai lượt đã chạy trên phiếu này. **Lượt kiểm định 11/08** đọc lại `.md` trọn mục, tra thêm bản `.docx` (bước `(1b)` chưa chạy ở lượt 10/08) và đối chiếu ngược gói 07/08 — khép được 3 vấn đề rưỡi. **Lượt BA duyệt 11/08** chốt mục 1 và cả bốn ý của mục 3, trong đó **đảo một kết luận**.

**Lượt BA duyệt 11/08 đợt 4 — sau vòng soi thứ tư (Codex quét đủ 17 tệp + tự kiểm chéo). Đọc kỹ 2 dòng đầu**

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| Mục 5 việc 5a — **bảng Tiến độ nộp theo đơn vị** | **Lỗ của chính phiếu.** Bản trước viết *"người dùng Trung ương xem bảng Tiến độ nộp"* mà không kiểm bảng đó đã đặc tả chưa — bảng thành phần màn hình `:1163–1175` **không khai dòng nào**, trong khi `:621` `:938` `:1046` `:1080` đều nói nó hiển thị ở đúng màn đó | **(a) Đổi.** Thêm việc 5a. Phương án cũ trỏ vào một thành phần **không tồn tại trong đặc tả** |
| Mục 5 việc 6 — **ma trận phân quyền dòng `DOT_BAO_CAO`** | `srs-v3.5.md:1361` đang cho cán bộ Bộ ngành và Địa phương **tạo, sửa, xoá đợt**, trái `srs-fr-15:625` *"chỉ CB NV cấp TW"* | **(a) Đổi.** Dấu vết thứ tư của STT 52 áp một nửa, và là dấu **cho phép sai** chứ không phải thiếu |
| Mục 5 việc 6 — danh mục máy trạng thái | `srs-v3.5.md:6917` còn gắn máy trạng thái với thực thể đợt. Lượt trước tính `:6237` `:6241` nhưng bỏ dòng này | **(b) Phần việc phình ra 1 chỗ** |
| Mục 3 ý 3 — **số đếm sai** | Phiếu ghi *"7 chỗ – 0 chỗ"*, BA quyết trên con số đó. Đếm lại bằng 2 cách độc lập: **43 – 0**. Tỉ lệ vẫn áp đảo nên kết luận giữ, nhưng phạm vi nghiệm thu **rộng hơn 6 lần** so với lúc trình | **(c) Kết luận giữ, số đếm đính chính.** BA được báo lại và **giữ DG-12** |
| Mục 3 — DG-11 | Thu hẹp: bỏ cụm *"nhãn biểu đồ"* khỏi phạm vi áp, vì chưa đo giao diện biểu đồ lần nào | **(c) Câu chữ.** Mở rộng sau nếu đo được lỗi thật |

**Lượt BA duyệt 11/08 đợt 3 — sau vòng soi thứ ba (Codex soi độc lập + tự kiểm chéo). Đọc kỹ 2 dòng đầu**

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| Mục 3 ý 3 — làm tròn | **Cắt phạm vi rồi nâng cấp cách làm.** Bản trước áp cho 3 trường / 5 chỗ; quét 16 tệp thì 2 trường **không hiển thị ở màn nào** ⇒ bỏ. Đồng thời đếm được khuôn *"1 chữ số thập phân"* đã áp đảo **7–0** ⇒ BA chốt phát biểu thành quy ước dùng chung **DG-12** thay vì sửa từng trường | **(a) Đổi.** 5 chỗ → **1 quy ước + 2 chỗ dẫn chiếu**. Kèm cảnh báo **hai trường trùng tên `diem_tong`** ở hai thang (0–10 và 0–100) |
| Mục 3 ý 1, ý 2 | **Phát hiện bản sao thứ ba:** bản mô phỏng giao diện Phụ lục D.1.4 (`srs-v3.5.md:6638–6657`) vẽ đúng form đánh giá, dùng **bộ nhãn thứ tư**. Cùng 5 ô đang có **4 bộ nhãn** rải trong đặc tả | **(b) Kết luận giữ, phần việc phình ra.** Thêm 1 chỗ sửa; loại bản sao "bản mô phỏng giao diện" **chưa từng được tính** ở mọi lượt rà trước |
| Mục 2 việc 4 | Gỡ câu *"không sửa hay dựng lại dữ liệu cũ"* — chỉ dẫn chuyển đổi dữ liệu, vi phạm nguyên tắc chỉ mô tả hành vi nghiệp vụ | **(c) Câu chữ.** Giữ vế nghiệp vụ, bỏ vế triển khai |
| Mục 5 việc 3c — mã đợt | Bản trước chỉ sửa bảng màn hình. Tài liệu gốc `srs-v3.5.md:2213` cũng còn dạng cũ, và `:2215` còn trường gắn chương trình **ở mức bắt buộc** ⇒ đọc theo tài liệu gốc thì không tạo được đợt độc lập | **(b) Phần việc phình ra:** 1 chỗ → **3 chỗ**. Hạ xuống **DỌN KÈM** vì không sinh từ 6 dòng lỗi |
| Mục 1 | Bổ sung 2 quy ước dùng chung chưa trích: **H9** (`srs-v3.5.md:6772`) và Phụ lục D.2.3 *"Export format"* — cả hai cũng **không** khai danh mục cột | **(c) Câu chữ.** Củng cố kết luận "đặc tả im lặng về cột" |
| Mục 3 rà phạm vi — quy ước không-ngắt-giá-trị | Mẫu tìm cũ suy từ chính chỗ lỗi (`/10`) nên **bỏ sót 3 nơi**: `srs-fr-04-chuyen-gia-tvv.md:1454` (*"4.5/5"*, *"—/5"*), `srs-fr-08-danh-gia.md:889` · `:897` | **(b) Danh sách ứng viên 9 → 12 nơi.** Đúng lỗi mà quy trình đã cảnh báo: đừng dùng mẫu tìm suy ra từ chỗ đã biết |
| Mục 5 việc 6 — ma trận phân quyền · Mục 5 việc 3a — ngưỡng khoá | Hạ từ BẮT BUỘC xuống **DỌN KÈM**: quyền đã ngầm định ở bước xử lý `:746` `:938`; việc siết ngưỡng Chỉnh sửa là chính sách thêm, không phái sinh bắt buộc | **(c) Đổi mức, không đổi nội dung** |

**Lượt BA duyệt 11/08 đợt 2 — sau vòng soi thứ hai. Đọc kỹ 2 dòng đầu**

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| Mục 5 — ngưỡng khoá sửa/xoá đợt | **Sửa một chỗ tôi ghi sai.** Phiếu từng ghi *"đã có lời giải trong phương án"* — không đúng: hai điều kiện đã có sẵn vế thứ hai và **hai vế đó khác ngưỡng nhau**; câu tôi đề xuất sẽ âm thầm siết điều kiện Chỉnh sửa. BA chốt **dùng chung ngưỡng chặt** | **(a) Đổi.** Từ *"không cần quyết"* → thành việc 3a có nội dung. Kèm phát hiện: thông báo lỗi `:689` chỉ dẫn một chức năng **không tồn tại** |
| Mục 5 — "Quá hạn" | BA chốt là **nhãn cảnh báo**, không phải bước vòng đời. Bằng chứng: đặc tả đang **ghi đè** trạng thái thật, khiến đơn vị quá hạn không lập tiếp được (`:718` không nhận *Quá hạn*) trong khi thông báo lại bảo *"nộp ngay"* | **(a) Đổi.** Từ điểm treo → thành việc 3b, gỡ được một lỗi khoá có sẵn |
| Mục 5 — phạm vi đợt sửa đặc tả | **Phát hiện nặng nhất của vòng soi:** bảng theo dõi nộp của đơn vị **không có một dòng nào** ở tài liệu gốc; sơ đồ quan hệ còn trường đã bị STT 52 bỏ. BA chốt **gộp việc đồng bộ vào đợt này** | **(b) Kết luận giữ, phần việc phình ra đáng kể.** Thêm việc 6 — 5 chỗ ở tài liệu gốc. Rà phạm vi chạy lại: 8 thứ mới, 28 cặp, 6 Doc action |
| Mục 5 — mã đợt | BA chốt dạng theo kỳ và năm; sửa bảng mô tả màn hình dòng 32 | **(c) Câu chữ.** Gỡ luôn ghi chú `[CẦN BA CHỐT]` đặt sẵn tại `:1151` |
| Mục 3 ý 3 — làm tròn | BA chốt áp cho **cả ba** trường điểm thang 0–10 của nhóm vụ việc, không chỉ Điểm tổng | **(b) Kết luận giữ, phần việc rộng ra** từ 1 chỗ thành **5 chỗ** |

**Lượt BA duyệt 11/08 đợt 1 — đọc kỹ 2 dòng đầu**

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| `DGKQHTVV_02` ý 4 (bẻ vỡ giá trị) | BA **đảo**: giá trị không được tách làm đôi, phải ngắt dòng hợp lý. Cấp quy ước dùng chung mới **DG-11** | **(a) Đổi.** Từ *"không phải lỗi, route cải tiến"* → **là lỗi, `Dev FE` sửa**. Đã gỡ khối phản hồi đối tác của ý này |
| `QLLKHDTBD_09` | BA chốt **Theo bảng trên màn** | **(a) Đổi.** Từ *"CHỜ BA CHỐT"* → **là lỗi, `Dev BE` bổ sung 2 cột**, Sheet chuyển sang Giữ xử lý |
| `DGKQHTVV_02` ý 1, 2, 3 | BA chốt: nhãn theo bản đang chạy · bổ sung 2 trường vào đặc tả · làm tròn theo quy tắc sẵn có | **(b) Kết luận giữ hướng, phần việc thành hình.** Đã viết Phương án xử lý + rà phạm vi 6 câu |
| `GKQTHCTHTPL_01` + `LBCKQTHCT_05/06` vế trục trạng thái | BA chốt **Mỗi đơn vị một tiến trình riêng**, kèm cách hiển thị mới cho danh sách đợt (cột Tiến độ + lọc 3 mức). Trả lời câu hỏi phát sinh của BA về tầm nhìn của Trung ương làm lộ thêm: **dấu "đã gửi TW" vốn là thuộc tính của báo cáo, không phải của đợt** (`:993` vs bảng 18 trường `:1358–1375`) | **(a) Đổi.** Từ *"CHỜ BA CHỐT"* → đã chốt. Phương án 5 việc, đụng **3 bản sao** của máy trạng thái. Điều kiện hiển thị ở mục 4 gộp vào đây |

**Lượt kiểm định 11/08 — so với phiếu hỏi BA ngày 10/08**

| Mục | Đổi gì | Kết luận có đổi không |
|---|---|---|
| `DGKQHTVV_01` | Tìm ra `srs-fr-05-vu-viec.md:1217` — Processing bước 2 của chính UC67 định nghĩa phạm vi của DN **chỉ theo quyền sở hữu**. `.docx` §4.5.17.2.3 nói cùng nội dung | **(a) Đổi.** Từ *"cần BA chọn 1 trong 2 hướng"* → **Loại 1, lỗi phần mềm, tự khép** |
| `GKQTHCTHTPL_01` vế "Forbidden" | Khôi phục kết luận đã có ở gói 07/08 (chặn đúng đặc tả, chỉ sai câu thông báo) | **(a) Đổi.** Từ *"chưa đo lại được"* → **Loại 1, Dev BE**, có việc cụ thể |
| `DGKQHTVV_02` ý 4 (bẻ vỡ giá trị) | Đếm lại: đặc tả có **6 nơi** đặt luật hiển thị nội dung dài, trong đó 2 là quy ước dùng chung (DG-04, UI-07) — lượt 10/08 ghi "chỉ có một chỗ duy nhất" | **(a) Đổi** ở lượt này, **BA đảo lại** ở lượt sau — xem bảng trên |
| `LBCKQTHCT_05/06` | Bỏ khẳng định *"bản dựng đã đổi hành vi"* — hai lượt đo khác tiền đề và khác vai trò, không phải khác bản dựng. `.docx` §4.15.7.2.3 khai điều kiện hiển thị theo **đơn vị** | **(a) Đổi.** Vế "khối không hiện trước khi lập" → **không phải lỗi**; vế bảng thành phần thiếu dòng → **Loại 4B** |
| `LBCKQTHCT_05/06` + `GKQTHCTHTPL_01` vế trục trạng thái | Gộp lại thành **một** câu hỏi (gói 07/08 đã ghi "cùng gốc, nên chốt một lần"; lượt 10/08 tách đôi) | **(b) Kết luận giữ, phần việc gộp lại** |
| `QLLKHDTBD_09` | Bổ sung `(1b)`: `.docx` §4.3.14.2.3 cũng không khai danh mục cột. Đếm khuôn trong `.docx`: **6/15** mô tả Xuất Excel có khai cột, **9/15** không | **(c) Câu chữ.** Nay đã được BA chốt |
| `DGKQHTVV_02` ý 1, 2, 3 | Bổ sung bộ nhãn nguyên văn của `.docx` để BA so trực tiếp | **(c) Câu chữ.** Nay đã được BA chốt |

**Ghi chú phương pháp**

- `DGKQHTVV_01` từng được đặt thành phiếu riêng ngày **07/08** (`cau-hoi-ba-DGKQHTVV_01-pham-vi-nhin-cua-DN.md`); lượt 10/08 ghi *"lần đầu đặt thành một điểm riêng"* là không đúng. Phần "Dev sẽ làm gì sau khi chốt" của phiếu 07/08 vẫn còn hiệu lực, không viết lại ở đây.
- Số 83 đơn vị là **số đo trên môi trường thử** ngày 07/08 (đợt `DOT-SO_BO_NAM-2026-1`), không phải số của đặc tả — `.md:621` chỉ nói *"63 Sở Tư pháp ĐP + Bộ ngành đang có CT HTPLDN"*.
- `LBCKQTHCT_05.jpg` và `LBCKQTHCT_06.jpg` là **cùng một tệp ảnh** (trùng mã băm) và chỉ bắt phần dưới trang — không dùng làm căn cứ, mọi kết luận dựa vào lượt tự tái hiện.

---

## 1. Dòng 20 · `QLLKHDTBD_09` — tệp Excel Kế hoạch đào tạo gồm những cột nào

**Vấn đề:** Cán bộ lọc danh sách Kế hoạch đào tạo rồi bấm Xuất Excel. Bảng trên màn có 12 cột, trong đó có "Người tạo" và "Ngày tạo"; tệp tải về chỉ có 7 cột và thiếu đúng hai cột đó. Cán bộ mở tệp ra không biết bản ghi do ai lập và lập khi nào, phải quay lại phần mềm tra từng dòng.

**(1) Phần mềm đúng đặc tả chưa?** — **Đặc tả thiếu.** Đọc trọn FR-III-14 (`srs-fr-03-dao-tao.md:1090–1229`, gồm cả Error Handling `:1207`, Acceptance Criteria `:1218`, Postconditions `:1202`): không có bảng nào khai danh mục cột của tệp xuất.

- `srs-fr-03-dao-tao.md:1175` — *"Lấy danh sách theo filter, tối đa 10.000 dòng | BR-DATA-06"*
- `srs-fr-03-dao-tao.md:1224` — *"**Given** CB NV nhấn "Xuất Excel" **Then** tải file ≤ 10.000 dòng"*
- `srs-v3.5.md:5577` (BR-DATA-06, quy ước dùng chung) — *"**Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file"*
- `srs-v3.5.md:6772` (**H9**, quy ước giao diện dùng chung — lượt soi 3 bổ sung) — *"Mọi nút Xuất Excel: nếu bộ lọc hiện hành không ra bản ghi nào thì **chặn xuất, không tạo tệp rỗng**"* — cũng **không** khai danh mục cột
- `srs-v3.5.md:6712–6718` (Phụ lục D.2.3 *"Export format"*) — chỉ nói định dạng tệp và khuôn mẫu 21a/21b, **không** khai danh mục cột cho danh sách quản lý
- `srs-fr-03-dao-tao.md:1795` · `:1796` (bảng thành phần màn hình) — *"Người tạo | Họ tên cán bộ tạo"* · *"Ngày tạo | dd/mm/yyyy"*

**(1b) Bản `.docx` đối tác cầm có nói khác không?** — **Không.** §4.3.14.2.3, dòng STT 6: *"Người sử dụng bấm "Xuất Excel", hệ thống kết xuất danh sách kế hoạch năm theo bộ lọc hiện tại, tối đa 10.000 dòng, và trả tệp về máy người sử dụng."* Không khai cột ⇒ **không phải Loại 4**.

**(2) Đối tác yêu cầu khác gì?** — Ô `TKM phản hồi lần 1` đòi tệp có thêm "Người tạo", "Ngày tạo". Ô "Kết quả thực tế" còn ghi *"xuất toàn bộ danh sách"* — vế này **đã hết lỗi**, xem bảng bóc ý con.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** — Không chặn luồng, nhưng chạm quy ước dùng chung (BR-DATA-06 áp cho **mọi** danh sách toàn hệ thống) nên không tự khép được.

#### Căn cứ chi tiết

**(1b) Đếm khuôn mô tả Xuất Excel trong `.docx`** — 15 mô tả có câu *"bấm "Xuất Excel""* (`grep -c` trên bản trích `.docx`):

| Khuôn | Số | Ví dụ |
|---|---|---|
| **Có** khai danh mục cột | **6/15** | §4.4.1.2.3 danh sách tư vấn viên — *"gồm 10 cột: số thứ tự, họ tên, năm sinh…"* theo QĐ 1322/QĐ-BTP · §4.12.1.2.3 tư vấn chuyên sâu — *"tạo tệp bảng tính gồm **các cột đang hiển thị**: mã tư vấn, doanh nghiệp, chuyên gia, lĩnh vực…"* |
| **Không** khai | **9/15** | §4.3.14.2.3 Kế hoạch năm · và 8 màn khác (hồ sơ vụ việc, doanh nghiệp, thư mục tài liệu…) |

Tỉ lệ 6/15 – 9/15 **không áp đảo** ⇒ theo quy trình, không được dùng làm căn cứ tự khép. Nhưng khuôn *"các cột đang hiển thị"* đã có tiền lệ trong chính bản bàn giao, nên đây là câu BA trả lời được nhanh.

**→ Kết luận: Loại 2 — chốt phương án **Theo bảng trên màn**: tệp Xuất Excel lấy đúng các cột đang hiển thị trên bảng, gồm cả "Người tạo" và "Ngày tạo". Hiện trạng thiếu hai cột ⇒ **là lỗi**. Dev action: Có (`Dev BE`, mức Minor) · Sửa đặc tả: Có · Doc action: Có → Sheet: Giữ xử lý.** ✅ **BA duyệt 2026-08-11.**

**Bảng bóc ý con**

| Ý con trong Kết quả mong đợi / phản hồi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Xuất theo điều kiện lọc hiện tại | **Có** — BR-DATA-06 `:5577` + `.docx` §4.3.14.2.3 | **Không phải lỗi.** Đo 10/08: không lọc → 14 dòng; lọc *Đã duyệt* → 4 dòng. Có phản hồi riêng cho vế này |
| Tệp có cột "Người tạo", "Ngày tạo" | **Không** — cả `.md` lẫn `.docx` đều im lặng | Đã chốt: bổ sung, `Dev BE` |
| Giới hạn 10.000 dòng | Có — `:1175`, `:1216` (ERR-KH-06) | Không tranh chấp, chưa đo |

> **Phản hồi gửi đối tác** — cho riêng vế "xuất theo bộ lọc":
> **[Lý do]** Chức năng Xuất Excel của màn Kế hoạch đào tạo hiện đã lấy đúng danh sách theo điều kiện lọc đang áp: khi không đặt điều kiện, tệp có đủ 14 bản ghi; khi lọc theo trạng thái Đã duyệt, tệp còn 4 bản ghi. Nội dung Quý đơn vị ghi nhận là hệ thống xuất toàn bộ danh sách không tái hiện được trên bản phần mềm hiện hành.
> **[Nhận định]** Đề nghị Quý đơn vị cập nhật lại phần Kết quả thực tế cho riêng nội dung này. Phần thiếu cột "Người tạo" và "Ngày tạo" đã được ghi nhận là lỗi và sẽ được chỉnh sửa.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-03-dao-tao.md` FR-III-14 — **thêm một bảng mới "Outputs — Tệp Xuất Excel"** đặt ngay sau bảng `:1189` *"Outputs — Danh sách"*, liệt kê đúng 12 cột của bảng trên màn, giữ nguyên thứ tự hiển thị, có "Người tạo" và "Ngày tạo".
2. Cùng chỗ — thêm một câu phân biệt hai bảng, vì chúng gần nhau và dễ đọc nhầm: *"Outputs — Danh sách"* là dữ liệu trả về cho màn hình; *"Outputs — Tệp Xuất Excel"* là danh mục cột của tệp tải về. Hai bảng có thể khác nhau về số cột.
3. `srs-fr-03-dao-tao.md:1175` (§Processing — Xuất Excel bước 2) — bổ sung vế dẫn sang bảng mới, để bước xử lý không còn dừng ở *"lấy danh sách theo filter"*.
4. **Khoanh phạm vi: chỉ áp cho FR-III-14.** Không sửa BR-DATA-06 và không áp sang 8 màn còn lại chưa khai cột — việc đó cần một lượt chốt riêng, đã ghi vào Điểm treo.

**Rà phạm vi ảnh hưởng**

| Câu | Đầu ra |
|---|---|
| Chỗ khác cùng vi phạm | 15 màn có Xuất Excel, **9 màn chưa khai cột**. Cố ý **không** sửa lượt này — xem việc 4 và Điểm treo |
| Bản sao | `KE_HOACH_DAO_TAO` xuất hiện ở **2 tệp** (`srs-fr-03-dao-tao.md`, `srs-v3.5.md`); bảng thành phần màn hình có "Người tạo \| Họ tên cán bộ tạo" chỉ **1 nơi** (`srs-fr-03-dao-tao.md:1795`). Phải rà baseline khi thêm bảng Outputs mới |
| Cross-ref trong file | `:1227` Cross-ref của FR-III-14 dẫn *"Entity KE_HOACH_DAO_TAO §4 master"* — không nhắc danh mục cột, không phải sửa |
| Nhãn và số đếm | Không có nhãn đếm nào cho số bảng Outputs của FR-III-14 phải đổi |
| Dòng chung bị chọi | Cặp có ràng buộc thật: **"Outputs — Tệp Xuất Excel" × "Outputs — Danh sách"** — hai bảng cùng tên đầu, khác nội dung ⇒ đã xử bằng việc 2. BR-DATA-06 chỉ nói bộ lọc và giới hạn dòng, không chọi |
| Chiều ngược sang `.docx` | **1 Doc action:** §4.3.14.2.3 hiện chỉ ghi *"kết xuất danh sách kế hoạch năm theo bộ lọc hiện tại, tối đa 10.000 dòng"* — bổ sung danh mục 12 cột |

---

## 2. Dòng 64 · `DGKQHTVV_01` — doanh nghiệp không thấy vụ việc của chính mình do đơn vị khác thụ lý

**Vấn đề:** Doanh nghiệp đăng nhập bằng chính tài khoản của mình nhưng không nhìn thấy, không mở được một vụ việc do chính mình đứng tên — chỉ vì vụ việc đó được cán bộ Trung ương lập và thụ lý, còn doanh nghiệp thì thuộc Sở Tư pháp An Giang quản lý. Dán thẳng địa chỉ vụ việc thì báo không tìm thấy. Hệ quả: doanh nghiệp mất hẳn đường vào chức năng đánh giá kết quả hỗ trợ đối với vụ việc của mình, và mất luôn quyền theo dõi hồ sơ.

**(1) Phần mềm đúng đặc tả chưa?** — **Sai.** Đọc trọn FR-V.I-17 (`srs-fr-05-vu-viec.md:1186–1235`): phạm vi của doanh nghiệp được định nghĩa **chỉ theo quyền sở hữu**, đặt cạnh nhánh cán bộ để phân biệt rõ.

- `srs-fr-05-vu-viec.md:1217` — *"Validate scope theo role: nếu role='DN' → `VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id`; nếu role='CB_NV' → `VU_VIEC.don_vi_id = current_user.don_vi_id`"*
- `srs-v3.5.md:845` (khối BR-AUTH-11) — *"Chỉ cho phép DN xem hồ sơ của chính mình"*
- `srs-fr-05-vu-viec.md:1274` · `:1289` (FR-V.I-NEW-02 — DN bổ sung hồ sơ) — *"DN truy cập là chủ sở hữu của VU_VIEC"*

**(1b) Bản `.docx` đối tác cầm có nói khác không?** — **Không, nói cùng.** §4.5.17.2.3: *"Kiểm tra quyền và phạm vi: **doanh nghiệp chỉ đánh giá vụ việc của mình**, cán bộ nghiệp vụ chỉ đánh giá vụ việc thuộc đơn vị mình."*

**(2) Đối tác yêu cầu khác gì?** — Không khác. Đối tác ghi *"không hiển thị nút chức năng mặc dù bản ghi ở trạng thái phù hợp"* — đúng triệu chứng của cùng một nguyên nhân.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** — **Có.** Thiếu nó thì một trong hai bên đánh giá của UC67 không bao giờ vào được chức năng, và quyết định BA 09/08 (hai bên đánh giá độc lập) không cài đặt được.

#### Căn cứ chi tiết

**(1) Chứng minh ngược** — đã quét `srs-fr-05-vu-viec.md` và `srs-v3.5.md` tìm mọi chỗ ràng buộc phạm vi của doanh nghiệp đối với vụ việc (biến thể: `doanh_nghiep_id`, `chủ sở hữu`, `của mình`, `don_vi` + `DN`). **4 nơi nói theo quyền sở hữu** (`:1217` · `:1274` · `:1289` · `:845`), **0 nơi** đặt điều kiện theo đơn vị thụ lý vụ việc.

**(1) Vì sao BR-AUTH-11 không lật được kết luận** — hai lý do, độc lập nhau:

1. Câu mở đầu của BR-AUTH-11 đã lạc hậu. `srs-v3.5.md:5542` còn ghi *"DN **KHÔNG** đăng nhập CMS → không có phiên phân quyền dữ liệu. DN tương tác qua API chuyên trang"*, trong khi cùng bản gốc, giả định **A-01** (`:531`) ghi *"PM phát triển CMS (cho cán bộ) + **giao diện DN** (cho DN/người dân, đăng nhập VNeID Tier 2) … ✅ Cập nhật theo CSV (lượt 6)"* và `:843` ghi *"DN đăng nhập giao diện DN của phần mềm qua VNeID Tier 2"*. Chốt sau đè chốt trước.
2. Kể cả đọc nguyên văn, `:5542` lọc theo *"`don_vi_id` (**Sở TP quản lý DN**)"* — đây là thuộc tính định danh của doanh nghiệp, cố định theo doanh nghiệp, **không phải** đơn vị thụ lý vụ việc. Vụ việc do Trung ương thụ lý vẫn thuộc doanh nghiệp do Sở Tư pháp An Giang quản lý, nên bộ lọc này không loại nó ra.

**→ Kết luận: Loại 1 — lỗi phần mềm. Phạm vi nhìn của doanh nghiệp đang bị cắt theo đơn vị thụ lý, trái `srs-fr-05-vu-viec.md:1217`; phải mở theo quyền sở hữu cho cả danh sách, chi tiết và các dữ liệu con cần để tải tài liệu, xem kết quả và đánh giá. Dev action: Có (mức Major, `Dev BE`) · Sửa đặc tả: Có (chỉ để dọn BR-AUTH-11, không đổi nghiệp vụ) → Sheet: Giữ xử lý — verdict `Reopen` không đổi.**

### Phương án xử lý (cập nhật SRS)

1. `srs-v3.5.md:5542` — viết lại câu mở đầu BR-AUTH-11 cho khớp A-01 (`:531`) và `:843`: doanh nghiệp **có** đăng nhập giao diện DN qua VNeID Tier 2. Gỡ vế *"không có phiên phân quyền dữ liệu"*.
2. `srs-v3.5.md:844` — nói rõ "đơn vị quản lý DN" là thuộc tính của doanh nghiệp, **không** dùng để lọc theo đơn vị thụ lý bản ghi.
3. Bổ sung một dòng vào BR-AUTH-11: doanh nghiệp thấy **mọi** bản ghi mình đứng tên, bất kể đơn vị nào thụ lý; vẫn chặn tuyệt đối dữ liệu của doanh nghiệp khác.
4. Giữ nguyên quy tắc **đơn vị thụ lý đặt theo đơn vị của cán bộ lập hồ sơ** — đây là hành vi nghiệp vụ, không đổi.

> *Bản trước còn kèm câu "không sửa hay dựng lại dữ liệu cũ". Đã gỡ: đó là chỉ dẫn chuyển đổi dữ liệu khi triển khai, thuộc phần Dev tự quyết, không phải nội dung đặc tả nghiệp vụ.*

> Ba việc trên chỉ dọn câu chữ cho khớp nhau, không đổi nghiệp vụ. Nếu BA thấy đủ rõ thì Dev sửa được ngay, không phải chờ đợt sửa đặc tả.

---

## 3. Dòng 65 · `DGKQHTVV_02` — nhóm Đánh giá: nhãn, hai trường thừa, số thập phân, giá trị bị bẻ dòng

**Vấn đề:** Mở chi tiết một vụ việc đã đánh giá, phần Đánh giá hiện 7 ô trong khi tài liệu chỉ tả 5 ô; tên các ô trên màn cũng dài hơn tên trong tài liệu. Riêng ô "Điểm tổng" bị cắt giá trị làm đôi giữa hai dòng — người đọc thấy `9/1` ở dòng trên và `0` ở dòng dưới, dễ đọc nhầm thành điểm khác.

**(1) Phần mềm đúng đặc tả chưa?** — **Đặc tả thiếu ở ba ý, đủ ở một ý.**

- `srs-fr-05-vu-viec.md:1735` (bảng thành phần màn hình, Accordion 8) — *"diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet"* — đúng 5 mục, ghi bằng mã kỹ thuật, **không có** Người/Ngày đánh giá.
- `srs-fr-05-vu-viec.md:2118` · `:2125` (thực thể) — **có** `nguoi_danh_gia_id` và `ngay_danh_gia`, tức dữ liệu đã có sẵn.
- `srs-fr-05-vu-viec.md:2123` — `diem_tong` là trung bình cộng 3 điểm, thang 0–10, **không kèm quy tắc làm tròn**. Quy tắc làm tròn 1 chữ số duy nhất trong đặc tả (`:2467`) là của điểm trung bình tư vấn viên, thang 1–5, thuộc FR-IV-CROSS-01.
- Không quy ước nào cấm bẻ giá trị giữa chừng — xem Căn cứ chi tiết.

**(1b) Bản `.docx` đối tác cầm có nói khác không?** — **Không.** §4.5.17.2.2 khai đúng **5 trường**, không có Người/Ngày đánh giá, và cũng không có quy tắc làm tròn:

| Trường trong `.docx` §4.5.17.2.2 | Mô tả nguyên văn |
|---|---|
| Điểm chất lượng | *"Bắt buộc chấm theo thang từ 0 đến 10."* |
| Điểm thời gian | *"Bắt buộc chấm theo thang từ 0 đến 10."* |
| Điểm thái độ | *"Bắt buộc chấm theo thang từ 0 đến 10."* |
| Điểm tổng | *"Chỉ đọc. Hệ thống tự tính bằng trung bình cộng ba điểm thành phần."* |
| Nhận xét | *"Nhận xét thêm của người đánh giá về kết quả hỗ trợ."* |

⇒ `.md` và `.docx` khớp nhau ⇒ **không phải Loại 4** ở cả bốn ý.

**(2) Đối tác yêu cầu khác gì?** — Kết quả mong đợi đòi *"hiển thị các trường giống thiết kế · đúng định dạng · **không bị tràn/đè lên nhau**, đồng nhất ngôn ngữ hiển thị"*. Ô "Kết quả thực tế" của đối tác **để trống và không có ảnh**.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** — Ý 4 không chặn luồng và không mất chứng cứ, nhưng BA đánh giá là khiếm khuyết trình bày phải sửa. Ý 1, 2, 3 cần chốt vì đang có ba bộ nội dung khác nhau cùng tồn tại: bản gốc, bản bàn giao và bản đang chạy.

#### Căn cứ chi tiết

**(1) Chứng minh ngược cho ý 4** — đã quét toàn thư mục `srs-v3.5/` bằng các biến thể *tràn · ellipsis · truncate · xuống dòng · overflow · cắt chữ* (15 nơi khớp). Đặc tả **có 6 nơi** đặt luật hiển thị nội dung dài, trong đó **2 là quy ước dùng chung**:

| Nơi | Nội dung | Phạm vi |
|---|---|---|
| `srs-v3.5.md:958` (**DG-04**) | *"Thông tin dài >2 dòng \| Hiển thị `…` + mở rộng/thu gọn"* | quy ước dùng chung |
| `srs-v3.5.md:579` (**UI-07**) | *"Thiết kế tối ưu cho ≥ 1280px … Cuộn ngang cho bảng nhiều cột"* | quy ước dùng chung |
| `srs-fr-05-vu-viec.md:1569–1574` (**§C**) | *"Áp dụng cho mọi cột text trong bảng: cột tên/tiêu đề > 30 ký tự cắt + `...` + tooltip … Áp dụng nhất quán cho 5 SCR"* | riêng nhóm vụ việc |
| `srs-fr-01-dashboard.md:718` | truncate 25 ký tự + tooltip | riêng một chip |
| `srs-fr-02-hoi-dap.md:1037` · `srs-fr-10-quan-tri.md:1843` | truncate 200 / 100 ký tự + tooltip | riêng một cột |

Cả 6 nơi đều nói về **rút gọn chuỗi dài**, không nơi nào cấm **bẻ một giá trị ngắn ra làm hai dòng**. Ô "Điểm tổng" là giá trị 4 ký tự trong thẻ chi tiết, không phải cột bảng, nên §C và DG-04 không phủ. `.docx` cũng không có luật này.

**Đo được gì** — vụ việc `VV-BTP-TW-20260806-003`, tài khoản `cbnv_tw`, 10/08. Nhóm Đánh giá hiện 7 ô, nhãn tiếng Việt đầy đủ, không lộ mã kỹ thuật. Ba ô điểm thành phần cùng khuôn `x/10` không bị bẻ; riêng "Điểm tổng (trung bình 3 điểm)" cột hẹp nên `9/10` xuống dòng thành `9/1` + `0`. Trang không cuộn ngang. Ảnh: `image/DGKQHTVV_02-diem-tong-be-dong-2026-08-10.png`. Lượt đo rơi đúng trường hợp trung bình ra số nguyên (`(9+8+10)/3 = 9`) nên chưa lộ được quy tắc làm tròn.

**→ Kết luận: Loại 2 — bốn ý đều chốt, đặc tả phải bổ sung rồi Dev chỉnh giao diện. Bộ nhãn lấy theo bản đang chạy · hai trường "Người đánh giá" / "Ngày đánh giá" bổ sung vào đặc tả · Điểm tổng làm tròn 1 chữ số thập phân theo quy tắc sẵn có · giá trị hiển thị **không được ngắt giữa chừng**, ô "Điểm tổng" bẻ `9/10` thành `9/1` + `0` là **lỗi**. Dev action: Có (`Dev FE`, mức Minor) · Sửa đặc tả: Có · Doc action: Có → Sheet: Giữ xử lý.** ✅ **BA duyệt 2026-08-11.**

> *Lịch sử: ý "bẻ vỡ giá trị" đã đảo kết luận 2 lần — lượt 10/08 để ngỏ chờ BA, lượt 11/08 khép "không phải lỗi" vì đặc tả im lặng, BA 11/08 đảo lại thành lỗi và cấp quy ước mới. Bản đang có hiệu lực là quyết định của BA.*

**Bảng bóc ý con**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Hiển thị các trường giống thiết kế | Có — `:1735` (5 trường) | Ý 1 + ý 2, đã chốt: lấy nhãn bản đang chạy, bổ sung 2 trường |
| Đúng định dạng | Một phần — thang 0–10 có, làm tròn không | Ý 3, đã chốt: làm tròn 1 chữ số thập phân |
| Không bị tràn / đè lên nhau | **Không** — đã đếm 6 nơi, không nơi nào phủ | Ý 4, đã chốt: BA cấp quy ước mới **DG-11** |
| Đồng nhất ngôn ngữ hiển thị | Có — UI-06 `srs-v3.5.md:578` | **Không tranh chấp.** Đo 10/08: toàn tiếng Việt, không lộ mã kỹ thuật |

### Phương án xử lý (cập nhật SRS)

**Ý 1 — bộ nhãn.** Cùng 5 ô này đang có **4 bộ nhãn khác nhau** nằm rải trong đặc tả — đây mới là gốc của tranh chấp, không phải chuyện đặt tên:

| Nguồn | Bộ nhãn |
|---|---|
| Bảng thành phần màn hình `srs-fr-05-vu-viec.md:1735` | mã kỹ thuật trần (`diem_chat_luong`…) |
| Mô tả trường `srs-fr-05-vu-viec.md:2120–2122` + bản sao `srs-v3.5.md:1643–1645` | Điểm chất lượng tư vấn / Điểm đúng thời hạn / Điểm thái độ phục vụ |
| **Bản mô phỏng giao diện `srs-v3.5.md:6648–6652`** (Phụ lục D.1.4) | Chất lượng tư vấn / Đúng hạn xử lý / Thái độ phục vụ / Điểm tổng (TB) |
| Bản bàn giao §4.5.17.2.2 | Điểm chất lượng / Điểm thời gian / Điểm thái độ / Điểm tổng |

Chốt lấy **bộ nhãn đang chạy**, trùng với dòng thứ hai của bảng trên — tức đặc tả đã có sẵn bộ nhãn này ở phần mô tả trường, chỉ chưa đưa lên bảng màn hình. Sửa `srs-fr-05-vu-viec.md:1735`, thay đoạn liệt kê mã kỹ thuật bằng bộ nhãn tiếng Việt, giữ mã trường kèm theo như khuôn sẵn có của bảng này:

| Nhãn chính thức | Trường |
|---|---|
| Điểm chất lượng tư vấn | `diem_chat_luong` |
| Điểm đúng thời hạn | `diem_thoi_gian` |
| Điểm thái độ phục vụ | `diem_thai_do` |
| Điểm tổng (trung bình 3 điểm) | `diem_tong` |
| Nhận xét | `nhan_xet` |

**Ý 2 — hai trường.** Cùng dòng `:1735` — bổ sung **"Người đánh giá"** (`nguoi_danh_gia_id`) và **"Ngày đánh giá"** (`ngay_danh_gia`), ghi rõ **chỉ đọc, hệ thống tự gán**. Đây đúng khuôn **UI-12** (`srs-v3.5.md:584`): mục có căn cứ ở mô hình dữ liệu của chính FR đang xét (`:2118` · `:2125`) mà bảng Thành phần màn hình không khai ⇒ *"bảng bị sót — phần mềm đúng, BA bổ sung vào bảng"*. Theo **UI-13** (`:585`), hai trường này **không gắn dấu sao** vì người dùng không tự nhập.

**Ý 1 + ý 2 — sửa kèm bản mô phỏng giao diện.** Phụ lục D.1.4 (`srs-v3.5.md:6638–6657`) vẽ đúng form này: phải đổi sang bộ nhãn đã chốt, bổ sung hai ô Người/Ngày đánh giá, và sửa dòng `Điểm tổng (TB): _____ / 10` cho khớp DG-11 lẫn DG-12. Bỏ sót khối này thì đặc tả có hai chỗ vẽ cùng một màn mà khác nhau.

**Ý 3 — làm tròn: phát biểu thành quy ước dùng chung DG-12, không sửa từng trường** `[BA duyệt 2026-08-11 lượt 3]`.

Quét toàn thư mục cho thấy khuôn *"1 chữ số thập phân"* **đã áp đảo sẵn: 43 chỗ dùng, 0 chỗ dùng khuôn khác** — nên đây là việc *ghi lại một quy ước đang tồn tại*, không phải đặt luật mới. Đếm bằng **hai cách độc lập**, lệnh đếm ghi ngay tại chỗ:

| Cách đếm | Kết quả |
|---|---|
| Phát biểu bằng lời — `grep -rniE "1 chữ số thập phân\|một chữ số thập phân\|làm tròn 1 chữ số"`, bỏ CHANGELOG | **16 dòng** |
| Ràng buộc `DECIMAL(3,1)` — `grep -rn "DECIMAL(3,1)"`, bỏ CHANGELOG | **27 dòng** |
| Hợp lại (có dòng trùng) | **43 dòng** |
| Khuôn khác — `grep -rniE "2 chữ số thập phân\|DECIMAL\(3,2\)\|DECIMAL\(4,2\)\|không làm tròn"` | **0** |

> ⚠️ **Đính chính số đếm.** Lượt duyệt trước phiếu ghi *"7 chỗ – 0 chỗ"* và BA quyết định trên con số đó. Con số **sai**; đếm lại ở lượt soi 4 ra **43 – 0**. Tỉ lệ vẫn áp đảo nên kết luận không đổi, nhưng **phạm vi nghiệm thu rộng hơn 6 lần** so với lúc trình. BA đã được báo và **giữ nguyên quyết định thêm DG-12** `[BA duyệt 2026-08-11 lượt 4]`.

**Thêm dòng DG-12** vào bảng Quy tắc hiển thị dữ liệu (`srs-v3.5.md:955–964`), ngay sau DG-11:

> **DG-12 — Điểm đánh giá hiển thị 1 chữ số thập phân.** Mọi điểm đánh giá, ở mọi thang (0–10, 1–5, 0–100), hiển thị **1 chữ số thập phân**; giá trị do hệ thống tính thì **làm tròn nửa lên**. Ví dụ: `(9+8+10)/3` → `9,0`; `(9+8+8)/3` → `8,3`. Điểm do người dùng chấm bằng số nguyên vẫn hiển thị kèm phần thập phân (`8` → `8,0`) để hai ô điểm cạnh nhau không trông như hai kiểu dữ liệu khác nhau. Quy ước này chỉ nói **cách hiển thị**; công thức tính và bước cập nhật điểm trung bình của từng thang vẫn giữ nguyên tại FR sở hữu.

**Chỗ sửa kèm — 2 chỗ, không phải 5:** bổ sung dẫn chiếu DG-12 vào ràng buộc của `DANH_GIA_VU_VIEC.diem_tong` ở **cả hai bản** — `srs-fr-05-vu-viec.md:2123` và bản sao ở tài liệu gốc `srs-v3.5.md:1646`.

> **Đã cắt so với lượt trước.** Bản trước định áp cho 3 trường / 5 chỗ, gồm `VU_VIEC.diem_danh_gia` và `KET_QUA_VU_VIEC.diem_danh_gia`. Quét cả 16 tệp: **hai trường đó không xuất hiện trong bất kỳ bảng Thành phần màn hình nào**, chỉ tồn tại ở dòng mô tả thực thể ⇒ áp quy tắc hiển thị cho thứ không hiển thị là việc thừa. DG-12 tự phủ chúng khi nào chúng lên màn.
>
> ⚠️ **Cảnh báo khi thi hành:** có **hai trường cùng tên `diem_tong`** ở hai thực thể khác nhau — `DANH_GIA_VU_VIEC.diem_tong` (thang 0–10, UC67) và `KET_QUA_DANH_GIA.diem_tong` (**thang 0–100**, dùng cho biểu đồ màn Tổng quan — `srs-fr-01-dashboard.md:416`). Mọi chỗ sửa phải ghi kèm tên thực thể, không dùng tên trường trần.

**Ý 4 — quy ước hiển thị mới DG-11.** `srs-v3.5.md`, bảng Quy tắc hiển thị dữ liệu (`:955–964`) — **thêm dòng DG-11** ngay sau DG-10:

> **DG-11 — Giá trị nguyên khối không bị ngắt giữa chừng.** Giá trị mang tính nguyên khối — tỉ số (`9/10`), số có phần thập phân (`8,3`), ngày (`06/08/2026`), số tiền, mã định danh — phải nằm trọn trên một dòng **trong cùng một ô hiển thị**. Khi bề rộng ô không đủ, chỉ được ngắt dòng tại khoảng trắng của **nhãn**, không ngắt bên trong giá trị. Nếu vẫn không đủ chỗ thì rút gọn theo **DG-04** (`…` kèm nội dung đầy đủ khi rê chuột), **không** cắt đôi giá trị. **Áp cho:** thẻ chi tiết, ô bảng, thẻ chỉ số. **Không áp cho** đoạn văn bản tự do nhiều dòng (nhận xét, mô tả) — chỗ đó ngắt dòng theo từ như bình thường.
>
> *Đã thu hẹp ở lượt soi 4: bỏ cụm "nhãn biểu đồ" khỏi phạm vi áp. Lý do — chưa đo giao diện biểu đồ lần nào, mà nhãn biểu đồ do đội thiết kế quyết bố cục (xem `srs-fr-01-dashboard.md:443` · `:521`). Nếu đo được lỗi thật ở đó thì mở rộng sau, có bằng chứng.*

**Rà phạm vi ảnh hưởng — DG-11 là quy ước dùng chung nên rà đủ 6 câu**

| Câu | Đầu ra |
|---|---|
| Chỗ khác cùng vi phạm | Đã thử **4 mẫu khác hình dạng**: `[giá trị]/10` · `{tham số}/{tham số}` · `[số],[số]/[số]` · nhãn tiếng Việt *"Điểm…"*. **12 nơi khớp trong đặc tả** (không tính CHANGELOG). Chín nơi dạng `/10`: `srs-fr-01-dashboard.md:443` · `:521` · `:544` · `:548` · `:834` · `srs-fr-11-bao-cao.md:830` · `srs-fr-06-chi-tra.md:1217` · `srs-fr-16-api.md:1407` · `:1408`. **Ba nơi mẫu cũ không thấy** — bắt được ở lượt soi 3: `srs-fr-04-chuyen-gia-tvv.md:1454` (*"4.5/5"* và *"—/5"* trong ô bảng), `srs-fr-08-danh-gia.md:889` · `:897` (*"{n}/{total}"* trên thẻ chỉ số). Đây là **ứng viên trên đặc tả**; chỗ vi phạm thật nằm ở giao diện đang chạy nên không grep được — đã ghi thành một lượt rà giao diện ở Điểm treo |
| Bản sao | Bảng Quy tắc hiển thị dữ liệu **1 nơi** (`srs-v3.5.md:953–964`); bảng Đặc điểm giao diện **1 nơi** (`:571–585`) ⇒ DG-11 và DG-12 không sinh lệch. **Nhưng nội dung nhóm Đánh giá thì có 3 bản sao:** (1) bảng thành phần màn hình `srs-fr-05-vu-viec.md:1735`; (2) mô tả trường `:2120–2125` + bản sao tài liệu gốc `srs-v3.5.md:1643–1648`; (3) **bản mô phỏng giao diện `srs-v3.5.md:6638–6657`** — loại bản sao mà các lượt rà trước **chưa từng tính đến**. Trường `diem_tong` cũng có 2 bản (`srs-fr-05:2123` + `srs-v3.5.md:1646`) |
| Cross-ref trong file | DG-04 được viện ở **1 nơi duy nhất** (chính dòng định nghĩa `:958`); UI-07 cũng **1 nơi** (`:579`). Không có chỗ nào nhắc lại nội dung sắp sửa |
| Nhãn và số đếm | Bảng DG **10 dòng → 12 dòng** (thêm DG-11 và DG-12). Đã quét tìm nhãn đếm dạng *"N quy tắc hiển thị"* — **không có** nhãn nào phải đổi theo. Mã trống đã kiểm: `DG-11`, `DG-12`, `DG-13` đều chưa dùng (chuỗi `ERR-DG-11` ở `srs-fr-08-danh-gia.md:799` thuộc nhóm mã lỗi, khác nhóm). Nhóm giao diện đã dùng hết tới `UI-13` |
| Dòng chung bị chọi | 6 thứ mới lượt này (DG-11 · **DG-12** · bảng Outputs Excel · 2 trường bổ sung · 1 dòng CT liên quan · bộ nhãn mới) → **15 cặp**, dưới ngưỡng tách phương án. Đã đối chiếu đủ; **3 cặp có ràng buộc thật**: (a) DG-11 × DG-04 — không loại trừ nhau, DG-11 dẫn sang DG-04 làm cách xử lý khi thiếu chỗ; (b) hai trường mới × UI-13 — hệ thống tự gán nên không gắn dấu sao; (c) **DG-12 × ba chỗ đang phát biểu làm tròn rời rạc** (`srs-fr-05-vu-viec.md:2467` · `srs-fr-04-chuyen-gia-tvv.md:796` · `srs-fr-01-dashboard.md:518`) — DG-12 **không thay thế** chúng, chỉ nâng thành quy ước chung; ba chỗ đó giữ nguyên vì còn mang công thức tính riêng của từng thang. Ba quy ước còn lại (`§C` `srs-fr-05-vu-viec.md:1569`, UI-07 `:579`, chip 25 ký tự `srs-fr-01-dashboard.md:718`) nói về **rút gọn chuỗi dài**, khác lớp với DG-11 nói về **giá trị ngắn nguyên khối** ⇒ không chọi |
| Chiều ngược sang `.docx` | **5 Doc action** cho mục này: (1) bổ sung DG-11 vào mục quy ước hiển thị chung; (2) §4.5.17.2.2 đổi 5 nhãn sang bộ nhãn mới; (3) §4.5.17.2.2 thêm 2 dòng Người/Ngày đánh giá; (4) §4.5.17.2.2 ô Điểm tổng bổ sung quy tắc làm tròn; (5) hai ô điểm thang 0–10 ở mục mô tả vụ việc và mục kết quả vụ việc — bổ sung cùng quy tắc |

**Bốn thứ tự soi thêm cho quy ước mới**

- **Phạm vi áp / không áp:** đã ghi trong nội dung DG-11.
- **Tham số động:** không có — quy ước không mang ngưỡng hay tham số cấu hình.
- **Giới hạn độ dài:** cố ý **không** đặt ngưỡng ký tự. Ràng buộc là *"không ngắt bên trong giá trị"*; khi thiếu chỗ thì dẫn sang DG-04, tránh đẻ thêm một con số phải bảo trì.
- **Xử lý trùng:** khi một ô vừa dài vừa nguyên khối (ví dụ mã định danh 40 ký tự), **DG-11 thắng** — rút gọn kèm nội dung đầy đủ khi rê chuột, không bao giờ cắt đôi xuống dòng.

---

## 4. Dòng 338 + 339 · `LBCKQTHCT_05` · `LBCKQTHCT_06` — hai khối ở màn Chi tiết đợt báo cáo

**Vấn đề:** Cán bộ mở màn Chi tiết đợt báo cáo và không thấy ô nhập Nhận xét, kiến nghị lẫn ô chọn Chương trình liên quan. Thực ra hai ô này nằm trong phần lập báo cáo, chỉ hiện khi đơn vị của cán bộ đã bước vào việc lập; đo trước thời điểm đó thì không thấy. Riêng ô Chương trình liên quan thì bảng mô tả màn hình của bản gốc không khai ở đâu cả, nên không có căn cứ để chấm đúng sai.

**(1) Phần mềm đúng đặc tả chưa?** — **Hai vế khác nhau.**

- Vế hiển thị: `srs-fr-15-ct-htpldn.md:1169` (bảng thành phần *Chi tiết Đợt BC*, heading `:1161`) — *"| 39 | form | Nhan xet kien nghi | textarea | Max 5000 ky tu | input | **khi dot o DANG_LAP_BC** |"*. Hai ô biểu mẫu 21a/21b cùng khuôn (`:1167` · `:1168`).
- Vế khối Chương trình liên quan: bảng thành phần (dải `:1163–1175`, các dòng 35–45) **không khai dòng nào**. Yêu cầu chỉ tồn tại ở `:732` (Inputs), `:744` · `:745` (Processing), `:1417` (thực thể).

**(1b) Bản `.docx` đối tác cầm có nói khác không?** — **Có, ở cả hai vế.** §4.15.7.2.2 và §4.15.7.2.3:

- *"**Chương trình liên quan** | Ô chọn nhiều | Không | — | Chọn các chương trình hỗ trợ pháp lý đơn vị đã triển khai trong kỳ để truy vết; không bắt buộc."* ⇒ bản bàn giao **có** khai, bản gốc **sót**.
- *"Điều kiện hiển thị: **đơn vị của người sử dụng thuộc phạm vi nộp và bản ghi theo dõi nộp ở trạng thái Chưa nộp hoặc Đang lập**."* ⇒ bản bàn giao neo điều kiện vào **đơn vị**, bản gốc `:1169` neo vào **đợt**.

**(2) Đối tác yêu cầu khác gì?** — Đối tác ghi *"Màn hình Chi tiết không có Khối nhận xét, kiến nghị"* và *"…không có Khối truy vết chương trình liên quan"*. Đo đúng theo hai bước ghi trên phiếu, trên một đợt mà đơn vị chưa bắt đầu lập ⇒ **quan sát đúng**, và **khớp đúng** điều kiện hiển thị của `.docx`.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** — Vế hiển thị: không, phần mềm đang chạy đúng bản bàn giao. Vế bảng thành phần sót dòng: có, vì không có dòng nào thì mọi đợt kiểm thử sau đều treo lại đúng chỗ này.

#### Căn cứ chi tiết

**(1) Vì sao không kết luận "bản dựng đã đổi hành vi"** — hai lượt đo khác tiền đề, không so được với nhau:

| Lượt | Vai trò | Đợt | Tình trạng đợt | Kết quả |
|---|---|---|---|---|
| 07/08 | `cbnv_hn` (CB NV ĐP) | đợt mà đơn vị **chưa bắt đầu lập** | chưa có báo cáo | hai khối **không** hiện |
| 07/08 | `cbnv_hn` | sau khi bấm [Lập báo cáo] | đang lập | hai khối **có**, lưu và đọc lại đúng, kiểm trên 2 bản ghi |
| 10/08 | `cbnv_tw` (TW) | `DOT-THBC01-UAT`, **2 đơn vị đã nộp**, biểu mẫu đã có số | đã có báo cáo | hai khối **có** |

Khác vai trò và khác tiền đề ⇒ không suy ra được là bản dựng đổi hành vi. Áp điều kiện của `.docx` §4.15.7.2.3 thì **cả ba dòng đều nhất quán**: khối hiện khi bản ghi theo dõi nộp của đơn vị đã ở Chưa nộp/Đang lập và cán bộ đã vào việc lập.

**→ Kết luận: case lai.**
**(a) Vế "hai khối không hiện trước khi lập" — không phải lỗi.** Phần mềm chạy đúng điều kiện hiển thị của bản bàn giao §4.15.7.2.3; quan sát của đối tác cũng đúng, chỉ là đo trước thời điểm khối xuất hiện.
**(b) Vế bảng thành phần màn hình sót dòng "Chương trình liên quan" — Loại 4 hướng B:** bản bàn giao **có**, bản gốc **thiếu**; yêu cầu vẫn còn giá trị (`:732` · `:744` · `:1417` đều có) ⇒ bổ sung bản gốc.
**(c) Vế điều kiện hiển thị neo vào trục nào — đã chốt cùng mục 5:** neo vào **trạng thái nộp của đơn vị**, không neo vào trạng thái đợt. Việc sửa nằm ở phương án mục 5 việc 5.
**Dev action: Không · Sửa đặc tả: Có · Doc action: Không (bản bàn giao đang đúng, bản gốc mới phải theo) → Sheet: KHÔNG đổi trạng thái.**

> **Phản hồi gửi đối tác** — cho riêng vế (a), dùng chung cho cả hai mã `LBCKQTHCT_05` và `LBCKQTHCT_06`:
> **[Lý do]** Hai khối "Nhận xét, kiến nghị" và "Chương trình liên quan" thuộc phần lập báo cáo của đơn vị, chỉ hiển thị khi đơn vị của người sử dụng đã bước vào việc lập báo cáo cho đợt đó — đúng như điều kiện hiển thị mô tả trong tài liệu bàn giao. Các bước Quý đơn vị thực hiện dừng ở màn Chi tiết đợt báo cáo trước thời điểm này nên chưa thấy hai khối.
> **[Nhận định]** Chúng tôi đề nghị Quý đơn vị bổ sung bước mở phần lập báo cáo vào phần Các bước thực hiện của hai trường hợp kiểm thử, rồi đo lại.

### Phương án xử lý (cập nhật SRS)

1. `srs-fr-15-ct-htpldn.md`, bảng thành phần *Chi tiết Đợt BC* (`:1163–1175`) — **thêm một dòng** cho khối "Chương trình liên quan": ô chọn nhiều, không bắt buộc, đặt cùng vùng với ô Nhận xét, kiến nghị; nội dung lấy nguyên văn `.docx` §4.15.7.2.2. Số thứ tự tiếp sau dòng 45. Theo **UI-13** (`srs-v3.5.md:585`), ô này **không gắn dấu sao** vì không bắt buộc.
   > Đây đúng khuôn **UI-12** (`srs-v3.5.md:584`): *"nếu mục đó **có căn cứ** ở §Inputs / §Processing / §Outputs / mô hình dữ liệu của chính FR đang xét thì **bảng bị sót — phần mềm đúng**, BA bổ sung vào bảng"*. Khối này có căn cứ ở cả ba chỗ — `:732` (§Inputs), `:744` · `:745` (§Processing), `:1417` (mô hình dữ liệu) ⇒ áp thẳng UI-12, không cần hỏi lại BA.
2. `:1169` (và `:1167` · `:1168` cùng khuôn) — đổi điều kiện hiển thị từ *"khi đợt ở Đang lập BC"* sang **"khi trạng thái nộp của đơn vị người dùng ở Chưa nộp hoặc Đang lập"**, đúng nguyên văn bản bàn giao §4.15.7.2.3. Việc này **thuộc phương án mục 5 việc 5**, làm cùng một lượt để không sửa hai lần.
3. Nhãn số lượng: bảng thành phần *Chi tiết Đợt BC* hiện có 11 dòng (35–45), thêm 1 dòng thành 12 — rà mọi chỗ nhắc số này trước khi sửa.
4. Chiều ngược sang bản bàn giao: **không phát sinh Doc action** cho việc 1, vì `.docx` đã có sẵn dòng này.

---

## 5. Dòng 342 · `GKQTHCTHTPL_01` — trạng thái ở màn Chi tiết đợt là của đợt hay của đơn vị

**Vấn đề:** Cùng một đợt báo cáo, cán bộ địa phương vừa gửi xong thì màn của họ hiện "Đã gửi Trung ương", nhưng màn của cán bộ Trung ương vẫn hiện "Tạo đợt" và bộ lọc "Đã gửi TW" của Trung ương không có đợt đó. Hai bên đọc ra hai kết quả khác nhau cho cùng một đợt nên không ai biết đợt đang ở đâu. Đứng sau là một câu chưa được trả lời: một đợt do Trung ương phát hành cho hàng chục đơn vị nộp thì "đợt đã gửi Trung ương" nghĩa là gì khi mới vài đơn vị nộp.

Một đợt, ba đơn vị đang ở ba bước khác nhau — ô Trạng thái phải hiện gì:

| Tình huống | Đơn vị A | Đơn vị B | Đơn vị C | Ô Trạng thái đọc ra gì |
|---|---|---|---|---|
| Sau khi Trung ương phát hành đợt | chưa nộp | chưa nộp | chưa nộp | Tạo đợt — mọi vai trò đọc giống nhau, không tranh chấp |
| A đang lập, B và C chưa mở | đang lập | chưa nộp | chưa nộp | **chưa có lời giải** — đợt chỉ có một giá trị |
| A đã gửi Trung ương, B và C chưa xong | đã gửi TW | đang lập | chưa nộp | **chưa có lời giải.** Hiện A đọc "Đã gửi TW", Trung ương đọc "Tạo đợt" |
| A đã gửi rồi, B bấm gửi | đã gửi TW | đã duyệt KQ | chưa nộp | **B bị chặn** — điều kiện tiên quyết đòi đợt ở "Đã duyệt KQ", mà đợt đã sang "Đã gửi TW" vì A |
| Cả ba đã gửi | đã gửi TW | đã gửi TW | đã gửi TW | Đã gửi TW — không tranh chấp |

**(1) Phần mềm đúng đặc tả chưa?** — **Bản gốc tự mâu thuẫn.** FR-XI-08 (`srs-fr-15-ct-htpldn.md:907–968`, đọc trọn mục) chuyển trạng thái của **đợt** ở bốn chỗ, trong khi bước thêm theo STT 52 lại chuyển trạng thái nộp của **đơn vị**:

- `:937` (Processing bước 3) — *"Chuyển trạng thái **đợt BC** sang DA_GUI_TW, đánh dấu da_gui_tw, ghi thời điểm gửi | SM-DOT-BC"*; cùng nội dung ở `:950` (Outputs), `:954` (Postconditions), `:967` (Acceptance Criteria).
- `:938` (bước 3a) — *"**Sửa theo STT 52 UAT 2026-05-26:** Cập nhật `DOT_BAO_CAO_DON_VI_NOP[dot_id, don_vi_nop_id].trang_thai_nop = DA_NOP` + `ngay_nop = NOW()`. Tiến độ nộp hiển thị trực tiếp ở chi tiết Đợt BC."*
- `:1368` — đợt có **một** giá trị trạng thái: *"CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP')"*
- `:1389` — đơn vị có trục trạng thái riêng, đủ 6 giá trị: *"trang_thai_nop … CHECK IN ('CHUA_NOP','DANG_LAP','CHO_DUYET','DA_DUYET','DA_NOP','QUA_HAN') … Trạng thái nộp của đơn vị trong đợt"*
- `:1165` · `:1166` (bảng thành phần *Chi tiết Đợt BC*) — ô Trạng thái và thanh tiến trình đều gắn **SM-DOT-BC**, tức trục đợt, *"luon hien thi"*

**(1b) Bản `.docx` đối tác cầm có nói khác không?** — **Có, và rõ hơn bản gốc.** Bản bàn giao nói **"đợt báo cáo của đơn vị"** ở mọi bước chuyển trạng thái:

- §4.15.10.2.3 — *"Điều kiện hiển thị: **đợt báo cáo của đơn vị** ở trạng thái Đã duyệt kết quả"* · *"Chuyển **đợt báo cáo của đơn vị** sang trạng thái Đã gửi Trung ương, đánh dấu đã gửi và ghi thời điểm gửi"* · *"Cập nhật bản ghi theo dõi nộp của đơn vị sang trạng thái Đã nộp và ghi ngày nộp"*
- §4.15.9.2.3 — *"chuyển **đợt báo cáo của đơn vị** sang trạng thái Đã duyệt kết quả"* · *"chuyển **đợt báo cáo của đơn vị** về trạng thái Đang lập báo cáo"*
- §4.15.8 — *"**Đợt báo cáo của đơn vị** đang ở trạng thái Đang lập báo cáo."*

**(2) Đối tác yêu cầu khác gì?** — Kết quả mong đợi đòi *"chuyển trạng thái đợt báo cáo: Đã duyệt kết quả → Đã gửi Trung ương"* + 5 vế phụ. Kết quả thực tế ghi *"Hệ thống hiển thị thông báo Forbidden"*.

**(3) Có bắt buộc cho luồng nghiệp vụ không?** — **Có.** Nếu trạng thái là của đợt dùng chung thì đơn vị nộp đầu tiên đẩy đợt sang "Đã gửi Trung ương", và điều kiện tiên quyết `:923` (*"đợt BC ở DA_DUYET_KQ"*) chặn hết các đơn vị còn lại. Đợt phủ vài chục đơn vị thì chỉ đơn vị đầu tiên nộp được.

#### Căn cứ chi tiết

**(1) Vì sao đây là mâu thuẫn thật, không phải cách đọc** — STT 52 (26/05/2026) đảo mô hình sang *"đợt báo cáo định kỳ độc lập do TW phát hành, nhiều đơn vị nộp"* (`:612` · `:621`), nhưng máy trạng thái 6 bước và các bước chuyển trạng thái của FR-XI-06/07/07a/08 vẫn giữ nguyên cách viết của mô hình cũ (một đợt = một báo cáo của một đơn vị). Bản bàn giao đã được viết lại theo mô hình mới (thêm chữ *"của đơn vị"*), bản gốc thì chưa.

**Đo được gì** — đợt `DOT-THBC01-UAT` đọc bằng tài khoản Trung ương ngày 10/08: ô Trạng thái ghi "Tạo đợt", thanh tiến trình dừng bước 1/6, trong khi bảng *Tiến độ nộp theo đơn vị* ngay dưới đã ghi **2 đơn vị "Đã nộp"** (Bộ Kế hoạch và Đầu tư 20/07, Sở Tư pháp An Giang 22/07). Lượt 07/08 bắt được biểu hiện rõ hơn trên đợt `DOT-SO_BO_NAM-2026-1`: cùng một đợt, màn cán bộ địa phương đọc "Đã gửi TW", màn cán bộ Trung ương đọc "Tạo đợt", tab lọc "Đã gửi TW" của Trung ương rỗng. Ảnh: `image/LBCKQTHCT_05-06-chi-tiet-dot-tao-dot-2026-08-10.png`.

**→ Kết luận: case lai.**
**(a) Vế "Forbidden" — Loại 1, đã đủ căn cứ, không cần BA.** Việc chặn là **đúng đặc tả**: `:922` giới hạn tác nhân là CB NV cấp BN/ĐP, và `:963` đã khai sẵn mã lỗi `ERR-XI-08-02` với câu *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*. Phần mềm trả về chuỗi tiếng Anh thô kèm mã quyền chung thay vì câu đã đặc tả ⇒ **Dev BE gắn đúng `ERR-XI-08-02`**, mức Minor. (Nguồn được truy ở lượt đo 07/08: dùng tài khoản cấp Trung ương gọi chức năng gửi TW thì ra đúng chữ "Forbidden".)
**(b) Vế trục trạng thái — Loại 2, chốt phương án "Mỗi đơn vị một tiến trình riêng".** Vòng đời 6 bước chạy cho **từng đơn vị** trong đợt, không phải cho đợt dùng chung. Đợt không còn ô trạng thái vòng đời; thay bằng **tiến độ nộp**. Việc hai vai trò đọc ra hai giá trị khác nhau cho cùng một đợt, và việc đơn vị nộp sau bị chặn, đều là hệ quả của chỗ trộn cấp trong đặc tả.
**Dev action: Có cho vế (a) — `Dev BE` Minor, gắn đúng `ERR-XI-08-02`. Vế (b) Dev làm sau khi đặc tả sửa xong · Sửa đặc tả: Có · Doc action: Có → Sheet: Giữ xử lý.** ✅ **BA duyệt 2026-08-11.**

**Bảng bóc ý con**

| Ý con trong Kết quả mong đợi | Bản gốc có không | Phiếu xử ở đâu |
|---|---|---|
| Chuyển trạng thái Đã duyệt KQ → Đã gửi TW | Có nhưng mâu thuẫn — `:937` vs `:938` | Vế (b), đã chốt: trục **đơn vị** |
| Ghi nhận thời điểm gửi | Có — `:937` | **Không tranh chấp.** Đo 07/08: mốc lệch ~0,1 s so với lúc bấm |
| Đánh dấu vào danh sách tổng hợp của TW | Có — `:939` | **Không tranh chấp.** Đo 07/08: có dòng khớp mã đợt + tên đơn vị + ngày gửi |
| Thông báo cho CB NV TW | Có — `:940` | **Không tranh chấp.** Đo 07/08: có, trùng mốc giờ |
| Lưu vết | Có — `:941` | **Không tranh chấp.** Đo 07/08: đúng tài khoản, đúng mốc giờ |
| Thông báo nhanh "Đã gửi báo cáo lên Trung ương" | Không khai câu chữ | **Không tranh chấp.** Đo 07/08: đúng nguyên văn |
| Không hiện "Forbidden" | Có — `:963` khai `ERR-XI-08-02` | Vế (a), Loại 1, Dev BE |

> Sáu ý giữa đo trên bản dựng cũ `index-D4Buvu4S.js` ngày 07/08, **chưa đo lại** trên bản hiện hành — ghi rõ để không chấm nhầm là đã nghiệm thu.

### Phương án xử lý (cập nhật SRS)

> **Chốt chung cho cả mục 4 và mục 5** — điều kiện hiển thị hai khối ở mục 4 (`:1167` · `:1168` · `:1169`) neo vào cùng trục này, sửa một lượt.

**Điểm tựa của phương án: trục đơn vị đã có sẵn, chỉ chưa được dùng.** Bảng theo dõi nộp của từng đơn vị (`:1389`) đã khai đủ 6 giá trị, ánh xạ gần như một-một với 6 bước của đợt:

| Vòng đời đợt (đang dùng) | Trạng thái nộp của đơn vị (đã có sẵn) |
|---|---|
| Tạo đợt | Chưa nộp |
| Đang lập BC | Đang lập |
| Chờ duyệt KQ | Chờ duyệt |
| Đã duyệt KQ | Đã duyệt |
| Đã gửi TW | Đã nộp |
| Đã tổng hợp | **thiếu — bổ sung** |
| — | Quá hạn *(đợt không có, giữ)* |

⇒ Lần đảo mô hình STT 52 đã dựng sẵn trục đơn vị đúng bằng 6 bước nhưng **chưa gỡ trục đợt** và **chưa nối thanh tiến trình vào trục mới**. Phương án dưới đây hoàn tất việc bỏ dở đó, không phải thiết kế lại.

**Việc 1 — chuyển vòng đời xuống cấp đơn vị.** Máy trạng thái `SM-DOT-BC` giữ nguyên tên và 6 bước, nhưng **đổi chủ thể**: từ *đợt báo cáo* thành *bản ghi theo dõi nộp của một đơn vị trong đợt*. Bổ sung giá trị **"Đã tổng hợp"** vào trạng thái nộp (`:1389`) để bước tổng hợp của Trung ương có chỗ ghi.

**Việc 2 — gỡ vế "chuyển trạng thái đợt" ở 4 bước xử lý.** Bốn chức năng dưới đây đều nhận đầu vào là **báo cáo của một đơn vị** rồi lại chuyển trạng thái **đợt** — đúng chỗ trộn cấp:

| Chỗ | Đang ghi | Sửa thành |
|---|---|---|
| `:803` (Trình phê duyệt) | *"Chuyển trạng thái BC sang Chờ phê duyệt, **đợt BC** sang Chờ duyệt KQ"* | chỉ chuyển trạng thái nộp **của đơn vị** sang Chờ duyệt |
| `:869` · `:870` (Phê duyệt / Từ chối) | *"chuyển **đợt BC** → Đã duyệt KQ / Đang lập BC"* | chuyển trạng thái nộp **của đơn vị** |
| `:937` (Gửi lên TW) | *"Chuyển trạng thái **đợt BC** sang Đã gửi TW, đánh dấu đã gửi"* | chuyển trạng thái nộp **của đơn vị** sang Đã nộp; dấu đã-gửi vốn đã nằm ở **báo cáo** (xem việc 4) |
| `:1005` (TW tổng hợp) | *"Chuyển các **đợt BC** đã chọn sang Đã tổng hợp"* | chuyển **các báo cáo đã chọn** và trạng thái nộp của đơn vị tương ứng sang Đã tổng hợp |

Đồng bộ theo: Outputs · Postconditions · Điều kiện chấp nhận của cả bốn FR (`:814` · `:950` · `:954` · `:967` và các dòng tương ứng của FR-XI-07/07a), cùng Preconditions `:923` — điều kiện để gửi lên TW là **trạng thái nộp của đơn vị** ở Đã duyệt, không phải trạng thái đợt. Đây chính là chỗ đang khoá các đơn vị nộp sau.

**Việc 3 — đợt không còn ô trạng thái vòng đời.** Trường trạng thái của đợt (`:1368` và bản sao ở baseline `srs-v3.5.md:2221`) thôi vai trò vòng đời. Danh sách đợt của Trung ương thay bằng:

- **Cột Tiến độ** dạng *"đã nộp / tổng số đơn vị trong phạm vi"* (ví dụ `12/83`) — thay cột *"Trạng thái"* ở bảng thành phần màn hình **dòng 32** (`:1157`).
- **Bộ lọc theo tiến độ**, 3 mức: *Chưa có đơn vị nào nộp* · *Đang nộp dở* · *Đã đủ đơn vị*. Bỏ bộ lọc theo 6 trạng thái cũ — đó là bộ lọc đang luôn rỗng mà QA đo được.

**Việc 3a — ngưỡng khoá sửa/xoá đợt** `[BA duyệt 2026-08-11]`. Gồm hai phần khác mức: **gỡ vế "đợt ở Tạo đợt" là BẮT BUỘC** (trạng thái đó không còn tồn tại sau việc 3, để nguyên là câu chết); **thống nhất ngưỡng cho cả hai thao tác là DỌN KÈM** (chính sách thêm, không phái sinh từ việc 3). Sau khi gỡ, cả hai dùng chung ngưỡng *"khi chưa đơn vị nào bắt đầu lập báo cáo"*.

| Chỗ | Đang ghi | Sửa thành |
|---|---|---|
| `:658` bước 7 (Chỉnh sửa) | *"chỉ khi đợt ở Tạo đợt **và chưa có đơn vị nào nộp BC**"* | chỉ khi **chưa đơn vị nào bắt đầu lập báo cáo** |
| `:659` bước 8 (Xoá) | *"chỉ khi Tạo đợt **và chưa có bản ghi nộp nào ở trạng thái khác Chưa nộp**"* | như trên — nội dung vốn đã đúng ngưỡng này, chỉ bỏ vế trạng thái đợt |
| `:689` lỗi E3 | *"Xóa đợt không ở Tạo đợt **hoặc đã có đơn vị nộp BC**"* | phát biểu lại theo cùng ngưỡng |

> **Siết so với hiện tại — cố ý.** Điều kiện Chỉnh sửa đang lỏng hơn Xoá: sửa được cho tới khi có đơn vị *nộp*, trong khi xoá bị chặn ngay khi có đơn vị *bắt đầu lập*. Sửa hạn nộp, phạm vi đơn vị hay biểu mẫu khi đã có đơn vị soạn dở sẽ làm hỏng việc của họ, nên chốt dùng ngưỡng chặt cho cả hai.
>
> **Bỏ vế chỉ dẫn chức năng không tồn tại.** Câu thông báo `:689` hiện bảo *"Vui lòng huỷ riêng từng bản ghi nộp trước"* — đã quét toàn tệp nhóm chức năng, **không FR nào có chức năng huỷ bản ghi nộp**, kết quả duy nhất là chính câu thông báo đó. Viết lại thành câu nêu lý do, không chỉ dẫn thao tác không làm được.

**Việc 3b — "Quá hạn" thành nhãn cảnh báo, không phải bước vòng đời** `[BA duyệt 2026-08-11]`. Bỏ giá trị *Quá hạn* khỏi tập trạng thái nộp (`:1389`); thay bằng dấu cảnh báo suy ra từ hạn nộp của đợt, hiển thị kèm trạng thái thật của đơn vị.

Ba chỗ phải sửa theo, ở chức năng đôn đốc tự động (FR-XI-NEW-01):

- `:1054` (mốc *Sau hạn*) và `:1068` (bước 5) — bỏ vế *"cập nhật trạng thái nộp = Quá hạn"*; giữ nguyên việc gửi thông báo và tăng số lần nhắc.
- `:1058` (Điều kiện tiên quyết) và `:1065` (bước 2) — hai chỗ này lọc theo **trạng thái đợt** (*"đợt ở trạng thái khác Đã tổng hợp"*, *"lấy các đợt chưa kết thúc"*); phát biểu lại theo tiến độ nộp.

> **Vì sao phải bỏ.** Đặc tả đang ghi đè trạng thái thật của đơn vị: đơn vị đang soạn dở mà quá hạn thì bị chuyển thành *Quá hạn*, **mất dấu là đã soạn dở**. Mà điều kiện để lập/sửa báo cáo (`:718`) chỉ nhận *Chưa nộp* hoặc *Đang lập* ⇒ đơn vị quá hạn **không lập tiếp được**, khoá vĩnh viễn — trong khi chính thông báo quá hạn lại bảo họ *"nộp ngay"*. Đây là lỗi có sẵn, sẽ nặng hơn khi trạng thái nộp thành trục vòng đời chính.

**Việc 3c — chốt một định dạng mã đợt** `[BA duyệt 2026-08-11]` · **DỌN KÈM**. Dùng dạng **theo kỳ và năm** (`DOT-{kỳ}-{năm}-{số thứ tự}`) đúng như bảng thực thể `:1359` và đúng mã thật đang chạy (`DOT-SO_BO_NAM-2026-1`). Sửa **3 chỗ** đang ghi dạng cũ gắn với một chương trình:

- `srs-fr-15-ct-htpldn.md:1157` — bảng thành phần màn hình dòng 32; gỡ luôn ghi chú `[CẦN BA CHỐT]` đặt sẵn tại `:1151`.
- `srs-v3.5.md:2213` — **bảng thực thể ở tài liệu gốc**, còn ghi `DOT-{CT_ID}-{SEQ}` *(lượt soi 3 bổ sung — bản trước chỉ nói sửa bảng màn hình)*.
- `srs-v3.5.md:2215` — cùng bảng đó còn trường `chuong_trinh_id` **bắt buộc (Y)**, khoá ngoại tới chương trình. STT 52 đã bỏ trường này ở tệp nhóm chức năng (`srs-fr-15:1361`) nhưng tài liệu gốc vẫn giữ, lại còn để mức bắt buộc — đọc theo tài liệu gốc thì **không tạo được đợt độc lập**.

> Việc này **không sinh ra từ 6 dòng lỗi**; nó là mâu thuẫn có sẵn nằm đúng bảng đang sửa. Xếp DỌN KÈM để nếu cần thu hẹp phạm vi thì cắt được mà không ảnh hưởng phần bắt buộc.

**Việc 4 — làm rõ chỗ Trung ương nhìn thấy báo cáo đã gửi.** Dấu "đã gửi TW" **vốn là thuộc tính của báo cáo, không phải của đợt**: bảng thông tin đợt có 18 trường (`:1358–1375`) và không trường nào mang dấu này, trong khi đầu vào của chức năng TW tổng hợp lấy *"những báo cáo có dấu đã-gửi-TW"* (`:993`). Ghi rõ điều đó vào đặc tả, và giữ nguyên bảng *"Báo cáo từ Bộ ngành / Địa phương"* (bảng thành phần màn hình dòng 44, `:1174`) — bảng này đã khai sẵn các cột **Đơn vị · Cấp · Mã đợt · Kỳ · Ngày gửi · Trạng thái**, tức vốn liệt kê theo từng đơn vị. Trung ương không mất tầm nhìn nào.

**Việc 5 — bảng thành phần màn hình Chi tiết đợt.** Dòng 36 (`:1166`, thanh tiến trình) và dòng 35 (`:1165`, ô Trạng thái trong thẻ Thông tin đợt): đổi thành tiến trình **của đơn vị người dùng đang đăng nhập**. Dòng 37–39 (`:1167` · `:1168` · `:1169`) đổi điều kiện hiển thị sang trạng thái nộp của đơn vị, đúng nguyên văn bản bàn giao §4.15.7.2.3 — **đây là việc gộp từ mục 4**.

**Việc 5a — bổ sung dòng "Tiến độ nộp theo đơn vị" vào bảng thành phần màn hình** `[lượt soi 4 phát hiện]`. Bảng thành phần màn hình Chi tiết đợt (`:1163–1175`, dòng 35–45) **không khai dòng nào** cho bảng này, trong khi **bốn chỗ khác** của cùng đặc tả đều nói nó hiển thị ở đúng màn đó:

- `:621` — *"CB NV TW theo dõi tiến độ nộp ở chi tiết Đợt BC (bảng đơn vị + trạng thái nộp)"*
- `:938` — *"Tiến độ nộp hiển thị trực tiếp ở chi tiết Đợt BC"*
- `:1046` — nguồn STT 52 Q4: *"Tiến độ nộp hiển thị 2 nơi"*
- `:1080` — *"Tiến độ nộp xem trực tiếp ở chi tiết Đợt BC (bảng đơn vị + trạng thái nộp từ `DOT_BAO_CAO_DON_VI_NOP`, **đã có ở FR-XI-05a**)"*

Câu `:1080` tự nhận là "đã có" nhưng bảng thành phần thì không khai. QA đo 10/08 thấy bảng này **có thật trên phần mềm** (đọc ra 2 đơn vị Đã nộp). ⇒ Đúng khuôn **UI-12**: có căn cứ ở §Mô tả và §Processing của chính FR đang xét ⇒ **bảng bị sót, phần mềm đúng, BA bổ sung**. Thêm một dòng: bảng, cột *Đơn vị · Cấp · Trạng thái nộp · Ngày nộp*, luôn hiển thị; với người dùng Trung ương thì đây là chỗ thay cho thanh tiến trình.

> **Đây là lỗ của chính phiếu này, không phải của đặc tả gốc.** Bản trước viết *"người dùng Trung ương xem bảng Tiến độ nộp theo đơn vị"* mà không kiểm bảng đó đã được đặc tả chưa — tức phương án trỏ vào một thành phần màn hình không tồn tại trong đặc tả.

**Việc 6 — đồng bộ quyết định STT 52 sang tài liệu gốc** `[BA duyệt 2026-08-11 — gộp vào đợt này]`.

Quyết định đảo mô hình ngày 26/05/2026 mới được áp vào tệp nhóm chức năng, **chưa vào tài liệu gốc**. Bảng theo dõi nộp của từng đơn vị — thực thể trung tâm mà toàn bộ phương án này dựa vào — **không xuất hiện một lần nào** trong `srs-v3.5.md` (đã quét, 0 kết quả). Không đưa nó vào thì không thể chuyển vòng đời xuống cấp đơn vị, và **chưa ai xác định được ai đọc, ai ghi trạng thái nộp**.

| Chỗ phải bổ sung / sửa | Hiện trạng | Việc |
|---|---|---|
| Danh sách thực thể (`srs-v3.5.md:1278`) | có `50a DOT_BAO_CAO`, **không có** bảng theo dõi nộp | thêm mục `50b` cho bảng theo dõi nộp của đơn vị |
| Mục mô tả thực thể (`:2202` — §3.4.3.10a) | chỉ có đợt | thêm mục kế tiếp cho bảng theo dõi nộp, đủ 8 trường như `srs-fr-15:1385–1394` (trừ *Quá hạn*, xem việc 3b; thêm *Đã tổng hợp*, xem việc 1) |
| Ma trận phân quyền (`:1302` tiêu đề 11 vai trò · `:1361` dòng đợt) — **DỌN KÈM** | **không có dòng nào** cho bảng theo dõi nộp. Không chặn phương án vì quyền đã ngầm định ở bước xử lý `:746` · `:938`, nhưng để trống thì đợt kiểm thử sau lại tranh chấp | thêm một dòng. Đề xuất: Quản trị **R** · CB NV Trung ương **R** (theo dõi tiến độ, không lập báo cáo) · CB NV Bộ ngành / Địa phương **RU\*** (đơn vị mình) · CB PD Bộ ngành / Địa phương **RU\*** (duyệt) · các vai trò còn lại **—** |
| Sơ đồ quan hệ dữ liệu (`:4257–4269`) | khối đợt **còn trường gắn với một chương trình** (`:4261`) — trường mà STT 52 đã bỏ | gỡ trường đó; thêm khối cho bảng theo dõi nộp |
| Quan hệ trong sơ đồ (`:4482`) | còn *"chương trình có nhiều đợt báo cáo"* | gỡ; thêm *"đợt có nhiều bản ghi nộp"* và *"đơn vị có nhiều bản ghi nộp"* |
| **Danh mục máy trạng thái (`:6917`)** — *lượt soi 4 bổ sung* | ghi `SM-DOT-BC \| … \| **DOT_BAO_CAO** \| Appendix C.7a` | đổi chủ thể sang bảng theo dõi nộp của đơn vị. Lượt trước đã tính `:6237` và `:6241` nhưng **bỏ mất dòng danh mục này** |
| **Ma trận phân quyền, dòng `DOT_BAO_CAO` (`:1361`)** — *lượt soi 4 bổ sung* | `R \| CRUD* \| **CRUD*** \| **CRUD*** \| RU* \| RU* \| RU* \| …` — cán bộ nghiệp vụ **Bộ ngành và Địa phương đang được tạo, sửa, xoá đợt** | sửa xuống **R**: `srs-fr-15-ct-htpldn.md:625` ghi rõ *"**Chỉ CB Nghiệp vụ cấp TW (Bộ Tư pháp)**"* — thu hẹp theo STT 52 |

> **Dòng ma trận trên là dấu vết thứ tư của việc STT 52 mới áp một nửa — và là dấu nguy hiểm nhất.** Ba dấu trước đều là *thiếu* (entity không có ở gốc, sơ đồ còn trường cũ, mã đợt còn dạng cũ); dấu này là **cho phép sai**: tài liệu gốc đang trao quyền tạo và xoá đợt cho cấp Bộ ngành / Địa phương, trái hẳn đặc tả chức năng.

**Rà phạm vi ảnh hưởng — 6 câu** *(chạy lại sau khi gộp việc 6; phạm vi rộng hơn lượt trước)*

| Câu | Đầu ra |
|---|---|
| Chỗ khác cùng vi phạm | Đã thử 3 mẫu khác hình dạng: mã máy trạng thái `SM-DOT-BC` · cụm *"đợt BC"* trong bước xử lý · tên bảng theo dõi nộp. **11 nơi khớp** trong `srs-fr-15-ct-htpldn.md` (`:36` `:77` `:654` `:658` `:665` `:803` `:808` `:868–870` `:875` `:936–937` `:944` `:1005` `:1010` `:1491`), trong đó **4 nơi trộn cấp thật** — đã liệt ở việc 2; số còn lại là dòng dẫn chiếu, sửa theo. Mẫu thứ ba cho **0 kết quả ở tài liệu gốc** — chính là việc 6 |
| Bản sao | **Máy trạng thái 3 nơi:** `srs-v3.5.md:6237` (Phụ lục C.7a — bản chuẩn, có sơ đồ + bảng chuyển trạng thái, và dòng *"Entity: DOT_BAO_CAO"* ở `:6241` phải đổi chủ thể), `srs-fr-15:77`, `:1491`. **Thực thể đợt 2 nơi:** `srs-fr-15:1368` và `srs-v3.5.md:2221` — **cộng thêm** `srs-v3.5.md:2213` (mã đợt) và `:2215` (trường gắn chương trình), xem việc 3c. **Bảng theo dõi nộp hiện 1 nơi** (`srs-fr-15:1379–1394`) — sau việc 6 thành **2 nơi**, phải giữ đồng bộ từ đó về sau. **Bảng nhãn màu trạng thái 1 nơi:** `srs-fr-15:1190–1199`. **Sơ đồ quan hệ 1 nơi:** `srs-v3.5.md:4257`. **Bản mô phỏng giao diện:** Phụ lục D có 2 khối liên quan — D.1.2 mẫu 21a (`:6584`) và D.1.3 mẫu 21b (`:6612`); đã đọc, cả hai chỉ vẽ 13 chỉ tiêu của biểu mẫu, **không** vẽ ô Nhận xét hay ô Chương trình liên quan ⇒ không phải sửa. Ghi lại vì loại bản sao này bị bỏ quên ở các lượt rà trước |
| Cross-ref trong file | Dòng *"Business Rules áp dụng — SM-DOT-BC: Transition X → Y"* xuất hiện **5 chỗ** (`:665` `:808` `:875` `:944` `:1010`), mỗi FR một chỗ. Dòng *"Cross-ref"* của chức năng đôn đốc (`:1082`) dẫn 4 FR + thực thể — rà lại sau khi bỏ *Quá hạn* |
| Nhãn và số đếm | Trạng thái nộp: **6 → 6 giá trị** (thêm *Đã tổng hợp*, bỏ *Quá hạn* — bù trừ nhau, nhưng phải đổi cả hai đầu, không được chỉ thêm). Bảng nhãn màu `:1194–1199`: **6 dòng, giữ 6**, đổi tên trạng thái. Bảng đếm máy trạng thái `srs-v3.5.md:6967` ghi **17** — **giữ 17** (máy trạng thái đổi chủ thể, không bị bỏ). Bảng đếm thực thể `:6966` ghi **70 → 71**; con số này phải **đếm lại tại thời điểm sửa**, không chép từ đây |
| Dòng chung bị chọi | 8 thứ mới lượt này (trục đơn vị làm trục chính · giá trị *Đã tổng hợp* · bỏ giá trị *Quá hạn* · cách hiển thị danh sách đợt · bỏ vai trò vòng đời của trạng thái đợt · ngưỡng khoá sửa/xoá dùng chung · một định dạng mã đợt · thực thể mới ở tài liệu gốc) → **28 cặp**, dưới ngưỡng tách phương án. Đã đối chiếu đủ. **2 cặp có ràng buộc thật:** (a) bỏ vai trò vòng đời của trạng thái đợt × điều kiện sửa/xoá đợt — đã xử ở việc 3a; (b) bỏ giá trị *Quá hạn* × điều kiện lập báo cáo `:718` — sau khi bỏ, đơn vị quá hạn giữ nguyên *Chưa nộp / Đang lập* nên `:718` **không cần sửa**, đây là điều kiện tự khỏi. Các cặp còn lại độc lập |
| Chiều ngược sang `.docx` | **6 Doc action.** Ba chỗ đã nêu ở lượt trước (§4.15.5 câu *"đi qua sáu trạng thái"* · §4.15.6.2.2 ô *Nhãn trạng thái* · ô *Thanh tiến trình*), thêm ba chỗ mới: §4.15.6.2.3 điều kiện hiển thị nút Chỉnh sửa và nút Xoá (dòng STT 3–4, bản bàn giao đang lỏng hơn bản gốc) · §4.15.6.2.2 cột mã đợt và cột trạng thái ở bảng danh sách đợt · mục mô tả chức năng đôn đốc, bỏ vế chuyển sang *Quá hạn* |
| Chiều ngược sang `.docx` | **3 Doc action.** Phần lớn bản bàn giao **đã đúng** (mọi bước đều ghi *"đợt báo cáo của đơn vị"*), chỉ 3 chỗ còn nói chung chung: §4.15.5 (*"Đợt báo cáo định kỳ đi qua sáu trạng thái…"*) · §4.15.6.2.2 ô *"Nhãn trạng thái đợt báo cáo"* · §4.15.6.2.2 ô *"Thanh tiến trình đợt báo cáo"* — làm rõ đây là tiến trình của từng đơn vị, và bổ sung cột Tiến độ + bộ lọc mới cho danh sách đợt |

---

## Điểm treo chuyển đợt sau

| Nội dung | Phát hiện ở mục | Thuộc bên nào | Trạng thái |
|---|---|---|---|
| Ngày bàn giao + kênh gửi bản `.docx` v3.5 chưa ghi nhận được | Đầu phiếu | Bên soạn tài liệu bàn giao | Chưa xử. Kết luận phiếu này không phụ thuộc, đã tra chéo 2 bản |
| Đường dẫn + `gid` sổ theo dõi bug đợt này chưa hỏi; chưa thử ghi ô nháp | Đầu phiếu | QA | Chưa xử — **phải làm trước khi cập nhật sổ** |
| Sáu ý con của `GKQTHCTHTPL_01` mới đo trên bản dựng cũ 07/08 | Mục 5 | QA | Chưa xử. Cần đo lại trên `index-LoDAkSbB.js` |
| Chưa dựng được đợt ở trạng thái "Đã duyệt KQ" trên môi trường hiện hành để đo lại nút Gửi TW | Mục 5 | Bên dựng môi trường + QA | Chưa xử |
| Chưa đo được thao tác nhập điểm đánh giá trên một vụ việc "Hoàn thành" phía doanh nghiệp (chưa có tư vấn viên để phân công) | Mục 2 — kế thừa phiếu 07/08 mục 8 | Bên dựng môi trường | Chưa xử. Phải đo sau khi Dev sửa phạm vi nhìn |
| Danh sách chương trình đổ vào ô chọn không lọc theo trạng thái chương trình và không lọc theo kỳ báo cáo | Mục 4 — kế thừa phiếu 07/08 | BA | Chưa xử. Đặc tả không quy định, chỉ ghi nhận |
| Khối "Chương trình liên quan" đang đặt lồng trong thẻ "Nhận xét, kiến nghị" — đúng ý đồ thiết kế hay cần tách riêng | Mục 4 — kế thừa phiếu 07/08 | BA | Chưa xử. Gộp vào phương án mục 4 việc 1 nếu BA muốn siết |
| Một lần gửi lên Trung ương sinh 2 mục nhật ký cùng mốc giờ | Mục 5 — kế thừa phiếu 07/08 | BA | Chưa xử. Đặc tả không quy định số mục |
| Sơ đồ quan hệ dữ liệu còn quan hệ *"chương trình có nhiều đợt báo cáo"* và trường gắn đợt với một chương trình — cả hai đã bị STT 52 bỏ | Mục 5 — rà phạm vi câu 2 | BA | **Đã gộp vào phương án** (việc 6). Ghi lại vì đây là dấu hiệu quyết định STT 52 mới áp một nửa — nên rà xem còn quyết định nào khác cùng tình trạng |
| **Bản mô phỏng giao diện là một loại bản sao chưa từng được tính** trong rà phạm vi. Tài liệu gốc có **34 khối** như vậy; lượt này mới rà 3 khối liên quan (D.1.2, D.1.3, D.1.4) | Mục 3 · Mục 5 — rà phạm vi câu 2 | BA + người soạn đặc tả | Chưa xử. Đề nghị bổ sung "bản mô phỏng giao diện" vào danh mục bản sao bắt buộc rà của quy trình, nếu không lượt sau lại sót |
| **DG-12 phủ 43 dòng** — lượt nghiệm thu phải rà đủ 43, không phải 7 như con số trình lần đầu | Mục 3 ý 3 | QA | Chưa xử. BA đã biết số thật và giữ quyết định; ghi ở đây để lượt nghiệm thu không dùng con số cũ |
| Bốn thang điểm cùng tồn tại — 0–10 (vụ việc) · 1–5 (tư vấn viên, tư vấn nhanh, tư vấn chuyên sâu) · 0–100 (đánh giá hiệu quả) · điểm kiểm tra học viên. Hai trường khác thực thể **trùng tên `diem_tong`** | Mục 3 ý 3 | BA | Chưa xử. DG-12 phủ cách hiển thị; việc có nên thu về ít thang hơn là câu nghiệp vụ riêng |
| Chức năng huỷ bản ghi nộp của một đơn vị — thông báo lỗi `:689` chỉ dẫn tới nhưng **không FR nào có** | Mục 5 việc 3a | BA | Lượt này chỉ **bỏ vế chỉ dẫn** khỏi câu thông báo. Nếu nghiệp vụ thật sự cần cho đơn vị rút lại bản nộp thì phải bổ sung một chức năng mới — chưa có trong danh sách giao dịch |
| BR-DATA-06 chưa khai danh mục cột cho **8 màn còn lại** có Xuất Excel | Mục 1 | BA | Chưa xử. Quyết định 11/08 cố ý **chỉ áp cho FR-III-14**. Đề nghị chốt một quy ước dùng chung ở đợt riêng, tránh mỗi màn một lần hỏi |
| Rà giao diện đang chạy tìm mọi chỗ vi phạm **DG-11** | Mục 3 ý 4 | QA | Chưa xử. Không grep được từ đặc tả — cần một lượt soi giao diện. 9 nơi ứng viên trên đặc tả đã liệt ở phần rà phạm vi, tập trung ở màn Tổng quan (`{diem_tb}/10` trên thẻ chỉ số) |
| Quy tắc làm tròn 1 chữ số nay tồn tại ở **2 thang khác nhau** — 0–10 (UC67) và 1–5 (FR-IV-CROSS-01) | Mục 3 ý 3 | BA | Chưa xử. Cố ý **không gộp** ở lượt này. Nếu đợt sau có thang thứ ba thì nên nâng thành quy ước dùng chung |

---

## Cập nhật sổ theo dõi

**Chưa ghi ô nào.** Theo Pha 5, chỉ được tự đổi trạng thái khi **cả hai vế** đều "không" — phần mềm không phải sửa **và** đặc tả không phải sửa. Không mục nào của phiếu này đạt đủ hai vế.

| Mã | Dev action | Sửa đặc tả | Trạng thái sổ | Ai đổi |
|---|---|---|---|---|
| `QLLKHDTBD_09` | Có (Minor, `Dev BE`) | Có | Giữ xử lý | Dev, sau khi sửa xong |
| `DGKQHTVV_01` | Có (Major, `Dev BE`) | Có | Giữ xử lý — `Reopen` không đổi | Dev, sau khi sửa xong |
| `DGKQHTVV_02` | Có (Minor, `Dev FE`) | Có | Giữ xử lý | Dev, sau khi sửa xong |
| `LBCKQTHCT_05` · `LBCKQTHCT_06` | Có (`Dev FE`, sau khi đặc tả sửa) | Có | Giữ xử lý | Dev, sau khi sửa xong |
| `GKQTHCTHTPL_01` | Có (Minor `Dev BE` cho vế thông báo; `Dev BE` cho vế trục trạng thái, sau khi đặc tả sửa) | Có | Giữ xử lý | Dev, sau khi sửa xong |

**Trước khi ghi, bắt buộc làm đủ:** hỏi đường dẫn sổ + `gid` đúng tab · tra tập giá trị đang dùng trong cột `Trạng thái dev fix` và ghi đúng chuỗi **kể cả khi sai chính tả** · tra dòng theo **nội dung test case** (Mô tả + Kết quả mong đợi), không dùng số dòng chép từ phiếu · verify lại ngay sau khi ghi.

Cột `DEV phản hồi lần 1` chỉ điền cho hai chỗ: `QLLKHDTBD_09` (riêng vế "xuất theo bộ lọc") và **một dòng đại diện** của cụm `LBCKQTHCT_05`/`LBCKQTHCT_06` — nội dung lấy nguyên văn hai khối "Phản hồi gửi đối tác" ở mục 1 và mục 4, dòng còn lại của cụm để trống. `DGKQHTVV_02` **không** điền phản hồi nữa: sau khi BA đảo kết luận ý 4, cả bốn ý đều do Dev sửa nên không còn phần nào để giải trình với đối tác.

---

**Đính kèm:** `image/DGKQHTVV_02-diem-tong-be-dong-2026-08-10.png` · `image/LBCKQTHCT_05-06-chi-tiet-dot-tao-dot-2026-08-10.png`
