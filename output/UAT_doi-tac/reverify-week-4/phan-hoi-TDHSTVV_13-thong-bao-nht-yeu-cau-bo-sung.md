# Phiếu phân tích — `TDHSTVV_13`: thông báo Người hỗ trợ khi thẩm định kết luận "Yêu cầu bổ sung"

**Ngày lập:** 31/07/2026 · **Phạm vi:** một test case lẻ, ngoài lô
**Sheet:** `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c`, tab `UAT_TGPL Doanh Nghiệp` (`gid=799081340`), **dòng 449**
**Bản `.docx` đối chiếu:** `docs/Reference/HTPLDN-PTYC-CT-v2.0.docx`
**CSV trọng tài:** `docs/Input/Danh sách transaction_v1.1_2026-03-27.csv`
**Đầu ra:** phiếu phân tích + **đã áp SRS ngày 31/07** (xem mục Đã áp SRS). **Không cập nhật sheet** theo yêu cầu.

## Ghi chú phương pháp

- `TDHSTVV_13` là **ca song sinh của `TDHSTVV_14`** — cùng nút "Gửi kết quả thẩm định" (`SCR-IV-03` tab Thẩm định), chỉ khác nhánh kết luận: `_13` = "Yêu cầu bổ sung", `_14` = "Không đạt".
- `_14` đã chốt **Loại 4B** ngày 30/07 (`phan-hoi-ba-confirmation-week2-vong2-va-tkdghqhtpl-r2.md`), và đợt áp SRS cùng ngày sửa `.md` cho **cả hai nhánh** ⇒ pha bổ sung `.md` của `_13` đã xong sẵn, ca này rơi khỏi diện Loại 4.
- Minh chứng `TDHSTVV_13.webm` (57 giây) **đã tải và xem bằng khung hình** — liên kết Drive lấy từ bản xuất XLSX của sheet (bản CSV không giữ siêu liên kết).

---

## `TDHSTVV_13` (dòng 449, Tuần 2) — thông báo Người hỗ trợ khi kết luận "Yêu cầu bổ sung"

**Vấn đề:** Cán bộ Nghiệp vụ thẩm định hồ sơ ứng viên tư vấn viên, kết luận "Yêu cầu bổ sung" và gửi kết quả. Hệ thống không gửi thông báo cho Người hỗ trợ và không hiển thị câu xác nhận trên màn hình.

**Kết quả mong đợi (nguyên văn ô sheet):** *"Hệ thống chuyển hồ sơ sang trạng thái "Yêu cầu bổ sung", gửi thông báo kèm lý do đến Người hỗ trợ, lưu vết thao tác, hiển thị thông báo "Đã gửi yêu cầu bổ sung đến Người hỗ trợ"."*

**Kiểm kê ý con** — Kết quả mong đợi chứa 4 ý; evidence nêu 2 lỗi ở 2 thời điểm khác nhau:

| # | Ý con | Trạng thái | Nguồn ghi nhận |
|---|---|---|---|
| 1 | Chuyển trạng thái "Yêu cầu bổ sung" | **Đạt** | Video 00:36 — nhãn trạng thái trên hồ sơ đổi thành "Yêu cầu bổ sung" |
| 2 | **Gửi thông báo kèm lý do đến Người hỗ trợ** | **Fail** | TKM phản hồi lần 1: *"TKM retest 25/7: Người hỗ trợ không nhận được thông báo kèm lý do"* |
| 3 | Lưu vết thao tác | Chưa kiểm được | Video không mở màn nhật ký thao tác |
| 4 | **Hiển thị "Đã gửi yêu cầu bổ sung đến Người hỗ trợ"** | **Fail** | Kết quả thực tế *"- Hệ thống không hiển thị thông báo"*; video 00:36–00:38 không có câu thông báo nào hiện ra |

**Diễn biến video** — quay bằng tài khoản Cán bộ NV Trung ương (`CB_NV_TW`), hồ sơ *Lê Văn Chuyên Gia (R32 NHT edit)* mã `TVV-BTP-TW-0011`:

- 00:28–00:35 — tab Thẩm định, Kết luận thẩm định chọn "YÊU CẦU BỔ SUNG", ô Lý do nhập *"TKM test123"* (11/1000 ký tự, vượt ngưỡng tối thiểu 10).
- ~00:35 — bấm "Gửi KQ". Trang chuyển sang chế độ xem, **không có câu thông báo nào xuất hiện** trong suốt 00:36–00:38.
- 00:46 — mở chuông thông báo của chính Cán bộ Nghiệp vụ (86 chưa đọc): có 3 mục *"Hồ sơ TVV đã được bổ sung"*, không có mục nào ứng với yêu cầu bổ sung vừa gửi. Đây là hộp thông báo của Cán bộ Nghiệp vụ chứ không phải của Người hỗ trợ nên **không dùng để kết luận ý 2**; nhưng cho thấy khung thông báo của phần mềm vẫn chạy — thiếu sót nằm ở đúng chiều gửi ra Người hỗ trợ.

Trạng thái dev fix hiện tại `Reopent`; *DEV phản hồi lần 1* **trống** — Dev chưa từng phản hồi.

### (1) Phần mềm đúng SRS chưa? — **SAI, 2 trên 4 ý**

- `srs-fr-04-chuyen-gia-tvv.md:524` — *"Nếu YEU_CAU_BO_SUNG: chuyển trạng thái, gửi thông báo kèm lý do cho **TVV/CG (chủ hồ sơ) qua email đã khai** VÀ **Người hỗ trợ đã nộp hồ sơ (thông báo trong phần mềm + email)** `[BA chốt 2026-07-30 — TDHSTVV_14]`"* ⇒ ý 2 sai.
- `srs-fr-04-chuyen-gia-tvv.md:1575` (SCR-IV-03 mục 20c) — *"nếu "Yêu cầu bổ sung" → đặt trạng thái Yêu cầu bổ sung + thông báo **chủ hồ sơ và Người hỗ trợ đã nộp hồ sơ** kèm lý do + hiển thị thông báo **"Đã gửi yêu cầu bổ sung đến Người hỗ trợ"**"* ⇒ ý 4 sai.
- Ý 1 đạt (video 00:36); ý 3 có căn cứ ở `:528` bước 9 ghi nhật ký thao tác (BR-DATA-05) nhưng chưa kiểm được.
- CSV UC44 bản ghi 219 xác nhận độc lập — *"Cán bộ nghiệp vụ TW,BN,ĐP gửi yêu cầu bổ sung thông tin đối với hồ sơ chưa đầy đủ; Hệ thống kiểm tra điều kiện, cập nhật trạng thái hồ sơ và **thông báo yêu cầu bổ sung đến người đăng ký**."* Người đăng ký hồ sơ là Người hỗ trợ (CSV UC41 Tác nhân; `srs-fr-04-chuyen-gia-tvv.md:2330`).

**Mốc thời gian:** tại ngày test 07/07 và retest 25/07, `.md` **chưa có** ý 2 và ý 4 — cả hai bổ sung ngày 30/07 theo `srs-fr-04-chuyen-gia-tvv.md:26` mục (7) và (8). Ghi nhận của đơn vị kiểm thử đúng ở mọi mốc: đúng `.docx` khi test, đúng `.md` hiện tại.

### (1b) Bản `.docx` đối tác cầm có nói khác không? — **Không, trùng khít**

- `.docx` v2.0 mục **4.4.5.2.2**, chức năng #2 "Gửi kết quả thẩm định", Trường hợp 1 — *"Hệ thống chuyển hồ sơ sang trạng thái "Yêu cầu bổ sung", gửi thông báo kèm lý do đến Người hỗ trợ, lưu vết thao tác, hiển thị thông báo "Đã gửi yêu cầu bổ sung đến Người hỗ trợ"."*

Trùng **từng chữ** với ô Kết quả mong đợi, và đồng nhất với `.md` sau đợt áp 30/07 ⇒ không có chênh lệch tài liệu ⇒ **không phải Loại 4**.

### (2) Đối tác yêu cầu có khác SRS không? — **Không khác điểm nào**

Kết quả mong đợi không đòi thêm gì ngoài đặc tả. Không đề nghị sửa Expected.

### (3) Yêu cầu đó có bắt buộc cho luồng nghiệp vụ không? — **CÓ, thiếu thì đứt luồng**

- Ứng viên **chưa có tài khoản** ở bước thẩm định — `srs-fr-04-chuyen-gia-tvv.md:2337` cho thấy tài khoản chỉ cấp ở `CHO_PHE_DUYET → CHO_KICH_HOAT`, nên không nhận được thông báo trong phần mềm.
- Người hỗ trợ là **tác nhân duy nhất bổ sung được hồ sơ** — `srs-fr-04-chuyen-gia-tvv.md:373` *"TVV/CG có thể đăng nhập chuyên trang xem hồ sơ của mình ở chế độ chỉ đọc, không sửa được. Muốn thay đổi → liên hệ NHT."*
- Không báo thì hồ sơ nằm mãi ở `YEU_CAU_BO_SUNG`, không ai biết để bổ sung — đứt luồng, không phải bất tiện.

**→ Kết luận: Loại 1 — Lỗi phần mềm, Dev sửa theo SRS.** Khi gửi kết quả thẩm định với kết luận "Yêu cầu bổ sung", hệ thống phải (a) gửi thông báo kèm lý do cho Người hỗ trợ đã nộp hồ sơ — trong phần mềm và email — và cho chủ hồ sơ qua email đã khai; (b) hiển thị câu "Đã gửi yêu cầu bổ sung đến Người hỗ trợ". **Dev action: Có → Sheet: Giữ xử lý** (giá trị `InProcess`, xem mục Cập nhật sheet). Không phản hồi đối tác, không sửa Kết quả mong đợi.

### Phương án xử lý (cập nhật SRS)

Hai điểm `.md` tự mâu thuẫn nằm trên đúng đường đi của ca này. Là dọn đặc tả, BA làm, không phát sinh việc cho Dev ngoài phần đã nêu ở Kết luận.

**Điểm A — bảng SM-TVV dòng `DANG_THAM_DINH → YEU_CAU_BO_SUNG` bị sót Người hỗ trợ.** Đợt áp 30/07 sửa dòng `TU_CHOI` và dòng CB PĐ từ chối nhưng bỏ sót đúng dòng của ca này:

- `srs-fr-04-chuyen-gia-tvv.md:2333` (`DANG_THAM_DINH → YEU_CAU_BO_SUNG`) — cột Action: *"Thông báo TVV/CG (chủ hồ sơ)"* — **thiếu Người hỗ trợ**, cột BR Ref để trống.
- `srs-fr-04-chuyen-gia-tvv.md:2336` (`DANG_THAM_DINH → TU_CHOI`) — *"Thông báo TVV/CG (chủ hồ sơ) **+ Người hỗ trợ đã nộp hồ sơ** + ghi lý do"*, BR Ref có `BR-NOTIF-01`.

Ghi chú CHANGELOG `:26` mục (7) tuyên bố đã bổ sung Người hỗ trợ vào bảng SM-TVV, nhưng bảng mới được sửa một nửa. **Đặc tả phải thành:** dòng `:2333` ghi người nhận là chủ hồ sơ **và Người hỗ trợ đã nộp hồ sơ** kèm lý do; BR Ref bổ sung `BR-NOTIF-01`. Căn cứ theo cây trọng tài tầng 1 — quyết định BA 30/07 đè bảng cũ, không cần hỏi lại BA.

**Điểm B — "ai thao tác hồ sơ tư vấn viên" mâu thuẫn 5 chỗ.** Chủ thể đúng là **Người hỗ trợ**.

| Vị trí | Nội dung | |
|---|---|---|
| FR-IV-04 `:373`, `:375` | Tác nhân = **Người hỗ trợ**; TVV/CG chỉ đọc | ✓ |
| Sơ đồ SM-TVV `:2296` | *"Người hỗ trợ bổ sung xong"* | ✓ |
| Bảng SM-TVV `:2334` | *"**TVV/CG (chủ hồ sơ)** bổ sung xong"* | ✗ |
| SCR-IV-03 `:1591` | *"tự động kích hoạt khi **chủ hồ sơ** lưu thông tin năng lực mới qua chuyên trang"* | ✗ |
| SCR-IV-03 `:1577` (tab Năng lực) | *"Vai trò = **chủ hồ sơ** HOẶC **Cán bộ Nghiệp vụ**"* — cho chủ hồ sơ sửa và bỏ sót Người hỗ trợ | ✗ |

"Chủ hồ sơ tự bổ sung qua chuyên trang" còn **không thực hiện được** — ở `YEU_CAU_BO_SUNG` ứng viên chưa có tài khoản (`:2337`).

Riêng `:1577` thêm Cán bộ Nghiệp vụ vào quyền sửa: FR-IV-04 §Processing (`:399`–`:406`) không có bước nào cho vai này, và theo cây trọng tài tầng 3 màn hình phải bám §Processing. Cán bộ Nghiệp vụ vẫn sửa được lĩnh vực chuyên môn trong lúc thẩm định qua FR-IV-06 §Processing bước 8 (`:527`) — đó là đường riêng, không phải chức năng Cập nhật năng lực.

**Căn cứ CSV** (cây trọng tài tầng 4 — CSV UC/Transaction là trọng tài cho tách vai UC):

- **UC42 bản ghi 206** "Quản lý cập nhật hồ sơ năng lực của tư vấn viên" — Tác nhân **Người hỗ trợ**; cả 4 transaction (bản ghi 207–210) đều mở đầu *"Người hỗ trợ…"*.
- **UC41 bản ghi 201–205** và **UC49 bản ghi 240–243** — Tác nhân **Người hỗ trợ**, toàn bộ transaction đều *"Người hỗ trợ…"*. Không có transaction nào cho ứng viên tự đăng ký qua chuyên trang công khai.
- Trong toàn bộ 934 bản ghi CSV, "Tư vấn viên" xuất hiện ở cột Tác nhân **đúng một lần** — UC75 bản ghi 357 *"Nhận thông báo kết quả xử lý hồ sơ đề nghị thanh toán"*, là nhận thông báo thụ động, không liên quan hồ sơ năng lực.

Thêm một căn cứ nội tại: `:1592` ("Nộp lại sau từ chối") đã ghi Người hỗ trợ theo chốt BA 30/07, với lý lẽ *"ứng viên bị từ chối chưa có tài khoản, không thao tác được"* — cùng lý lẽ áp cho `YEU_CAU_BO_SUNG`.

**Đặc tả phải thành** — 5 vị trí đổi chủ thể sang Người hỗ trợ:

- `:2334` — trigger ghi *"Người hỗ trợ bổ sung xong"*, khớp sơ đồ `:2296`.
- `:1591` — *"tự động kích hoạt khi Người hỗ trợ lưu thông tin năng lực mới"*, bỏ "chủ hồ sơ … qua chuyên trang".
- `:1528` — bỏ "ứng viên đăng ký qua chuyên trang công khai", ghi Người hỗ trợ đăng ký hồ sơ ứng viên.
- `:1529` — bỏ "tự cập nhật qua chuyên trang" và điều kiện kiểm sở hữu theo Căn cước công dân; thay bằng kiểm quyền Người hỗ trợ theo vai trò và đơn vị, đúng FR-IV-04 §Processing bước 1 (`:399`).
- `:1577` — điều kiện hiển thị nút "Cập nhật năng lực" ghi **Vai trò = Người hỗ trợ**, bỏ chủ hồ sơ và Cán bộ Nghiệp vụ.

**Doc action:** `.docx` mục 4.4.8 §Phân quyền hiện có gạch đầu dòng cho Cán bộ Nghiệp vụ — bên soạn tài liệu bàn giao gỡ theo `.md` ở bản kế tiếp.

> ⚠ Ý 3 (lưu vết thao tác) chưa kiểm được — video không mở màn nhật ký thao tác. Không đổi kết luận.

---

## Đã áp SRS — 31/07/2026

Áp đủ Điểm A và Điểm B, kèm đồng bộ khối SM-TVV ở baseline. Chạm **2 tệp**; đợt áp 30/07 chỉ chạm tệp module nên baseline lệch theo. Liệt kê theo cụm thay vì đếm tổng — số vị trí đổi theo cách gộp ô bảng, không phải con số ổn định.

**`srs-fr-04-chuyen-gia-tvv.md`:**

- SM-TVV — dòng `DANG_THAM_DINH → YEU_CAU_BO_SUNG` (Điểm A), dòng `YEU_CAU_BO_SUNG → DANG_THAM_DINH`, dòng `TU_CHOI → CHO_THAM_DINH`.
- SCR-IV-03 — §Quy tắc tương tác mục "Bổ sung hồ sơ"; cell 21 điều kiện hiển thị tab Năng lực; cell 4 nút "Sửa hồ sơ"; cell 5 và cell 8 nhãn tab danh sách.
- SCR-IV-02 — §Quy tắc tương tác 2 dòng "ứng viên đăng ký / tự cập nhật"; §Quyền truy cập dòng Cán bộ Nghiệp vụ; cell 5.1 nhãn bắt buộc tải file.
- Khối Quy trình nghiệp vụ tổng quan; bảng so sánh TVV ↔ NHT dòng "Đăng ký qua chuyên trang". Thêm một dòng CHANGELOG.

**`srs-v3.5.md` (baseline):**

- C.3 SM-TVV — tiêu đề + §Tham chiếu FR + §Trạng thái; mermaid 4 nhánh; bảng chuyển trạng thái 7 dòng, thêm 2 dòng `CHO_KICH_HOAT`.
- Ngoài C.3 — ghi chú trường `ngay_tiep_nhan`; §Tham chiếu FR entity NGUOI_HO_TRO; bảng so sánh TVV ↔ NHT (2 dòng); ma trận truy vết dòng FR-IV-11. Thêm dòng lịch sử v3.5.6.

Các dòng `TU_CHOI` ở baseline vốn ngoài phạm vi ca này, nhưng thuộc đúng đợt chốt 30/07 (TDHSTVV_14) mà lúc đó chỉ áp vào tệp module — nên áp nốt cho hết lệch.

### Đồng bộ khối SM-TVV baseline — đã làm cùng đợt

Khối C.3 SM-TVV ở baseline là bản sao cũ hơn bản ở tệp module. Câu hỏi "baseline giữ bản sao hay trỏ về module" **không phải điểm treo** — quy ước đã ghi sẵn ở `srs-v3.5.md` C.13 SM-NHT: *"sync từ srs-fr-04 v3.5"*. Baseline giữ bản sao và đồng bộ từ module. Đã đồng bộ đủ:

- **Bổ sung trạng thái `CHO_KICH_HOAT`** + 3 chuyển tiếp (`CHO_PHE_DUYET → CHO_KICH_HOAT`, `CHO_KICH_HOAT → HOAT_DONG`, `CHO_KICH_HOAT → VO_HIEU_HOA`), sửa `CHO_PHE_DUYET → HOAT_DONG` thành `CHO_PHE_DUYET → CHO_KICH_HOAT`. Đây không phải quyết định thiết kế mà là vá mâu thuẫn nội tại: entity `TU_VAN_VIEN` `:1739` vốn đã khai đủ 10 trạng thái kể cả `CHO_KICH_HOAT`, chỉ riêng máy trạng thái C.3 dừng ở 9.
- **Gỡ 4 tham chiếu `FR-IV-13`** (đã xoá ở v3.5 theo `CHANGELOG-v3-to-v3.5.md:220`; `:230` yêu cầu đổi tham chiếu trong bảng SM-TVV nhưng chỉ áp cho tệp module): C.3 §Tham chiếu FR, nhánh mermaid + dòng bảng `MOI_DANG_KY → CHO_THAM_DINH` → **FR-IV-06**; ghi chú trường `ngay_tiep_nhan` `:1750` → **FR-IV-06**; §Tham chiếu FR entity NGUOI_HO_TRO `:1865` → **FR-IV-12**.
- Thêm dòng lịch sử **v3.5.6** vào baseline. Đợt áp 30/07 có chạm baseline (trường `chuyen_nganh`, `gioi_tinh`) nhưng không ghi dòng lịch sử nào — bảng lịch sử baseline dừng ở v3.5.5 ngày 16/07.

**Kết quả kiểm chứng:** C.3 baseline nay khớp tuyệt đối `srs-fr-04` — **17 chuyển tiếp · 10 trạng thái · 17 dòng bảng** ở cả hai tệp.

---

## Cập nhật sheet (Pha 5)

**Không thực hiện** theo yêu cầu. Giá trị đề nghị cho dòng 449 khi cần chạy:

| Cột | Giá trị |
|---|---|
| `Trạng thái dev fix` | **`InProcess`** (đang là `Reopent`) — ghi khi chuyển phiếu cho Dev |
| `DEV phản hồi lần 1` | Để trống — bug thật, Dev sửa, không giải trình |
| `Trạng thái dev fix 2` · `DEV phản hồi lần 2` | Để trống — chưa sang vòng hai |

**Vì sao `InProcess` chứ không giữ `Reopent`.** "Giữ xử lý" nghĩa là không đặt `Reject` / `Resolve`, không có nghĩa là không đụng ô. Cột này đang dùng 5 giá trị (`dev done` 306 · `Reopent` 82 · `Resoved` 63 · `Reject` 4 · `InProcess` 4), trong đó `Reopent` và `InProcess` đều thuộc nhóm đang xử lý:

- `Reopent` — kiểm lại vẫn lỗi, phiếu mở lại, **chưa ai nhận**; đơn vị kiểm thử đặt sau retest.
- `InProcess` — **đã có kết luận, Dev nhận việc và đang làm**; bên phát triển đặt khi bắt tay.

Phiếu này là mốc chuyển giao: đặc tả đã rõ, không còn tranh chấp, Dev có việc cụ thể. Khớp với `phan-hoi-27-bug-reopent-lo-2.md` (bảng tổng kết Nhóm I: *"Giữ `Reopent` / chuyển `InProcess` khi Dev bắt tay"*) và với 4 dòng Tuần 4 trên sheet đang để `InProcess` ở cột này.

**Ghi cột 1, không phải cột 2** — *DEV phản hồi lần 1* còn trống nên vòng một chưa khép. Cột *Trạng thái dev fix 2* chỉ dùng khi đã qua một lượt Dev phản hồi rồi bị bác (tiền lệ `TLCTCDG_11` dòng 753 và `CPCTHTTTG_03` dòng 1388: cột 1 `Reopent`, cột 2 `InProcess`, cả hai đều có nội dung ở *DEV phản hồi lần 1*).

---

## Kiểm định (Pha 4)

- **Lớp 1 — Codex review:** đã chạy chế độ chỉ đọc (`codex exec -s read-only`, reasoning `high`, 120.666 token). Ra 6 phát hiện `[P1]` + 3 `[P2]`. Kết quả xử lý ở bảng dưới.
- **Lớp 2 — tự kiểm:** đã mở đọc trực tiếp từng dòng `.md` được trích; trích `.docx` v2.0 bằng công cụ giữ nguyên bảng và số mục, không bóc thẻ XML thô; đối chiếu chéo CHANGELOG `:26` với nội dung thật của bảng SM-TVV và phát hiện đợt áp 30/07 mới hoàn tất một nửa; quét toàn bộ 934 bản ghi CSV để xác nhận không có giao dịch nào tư vấn viên tự thao tác hồ sơ; xem video minh chứng bằng khung hình 3 giây, dày lại thành 0,5 giây quanh thời điểm bấm "Gửi KQ" để chắc chắn không bỏ sót câu thông báo thoáng qua.
- **Còn hở:** ý 3 (lưu vết thao tác) chưa kiểm được.

### Xử lý phát hiện của Codex

| # | Codex nêu | Phán quyết sau khi tự kiểm | Đã làm |
|---|---|---|---|
| P1-1 | Nhãn phải là Loại 4B, không phải Loại 1 | **Nhận một phần.** Gốc ca đúng là 4B và phiếu đã ghi ở §Ghi chú phương pháp. Nhưng Loại 4 đòi tiền đề *"phần mềm đúng `.md`"* — sau đợt áp 30/07 phần mềm **sai** `.md`, nên Pha 1 không tới câu (1b). Giữ Loại 1, đã nói rõ gốc 4B | Giữ nguyên |
| P1-2 | 12 trích dẫn `file:dòng` lệch | **Nhận.** Lệch đúng +1 vì chính tôi chèn dòng CHANGELOG ở đầu tệp rồi vẫn cite số dòng trước khi sửa | Dò lại bằng script, dịch 36 trích dẫn |
| P1-3 | "dòng 201/206/216/240" của CSV là số bản ghi, không phải dòng tệp | **Nhận.** Dùng trình đọc bảng nên là chỉ số bản ghi | Đổi hết sang "bản ghi" |
| P1-4 | Còn 8 chỗ ghi chủ hồ sơ / ứng viên / CB NV thao tác hồ sơ | **Nhận.** Grep của tôi chỉ dò đúng chuỗi đã sửa, không quét không gian ngữ nghĩa | Sửa 9 chỗ ở cả 2 tệp |
| P1-5 | Baseline chưa "khớp tuyệt đối" — `srs-v3.5.md:1897` còn ghi 9 trạng thái | **Nhận.** Tôi chỉ đối chiếu khối C.3, không quét ngoài khối | Sửa thành 10 (TVV) và 4 (NHT) |
| P1-6 | Nói "không có phản chứng" là sai | **Nhận**, hệ quả của P1-4 | Đã sửa hết các dòng phản chứng |
| P2-1 | CSV UC42 ô Mô tả vẫn ghi "Tư vấn viên tự cập nhật" | **Nhận.** Bản rút gọn theo quy tắc trình bày đã cắt mất chi tiết này | Nêu lại ở §Căn cứ CSV |
| P2-2 | BR-AUTH-08 nên ghi rõ TVV/CG là quyền chỉ đọc | **Nhận.** Ban đầu tôi gán `CHỜ BA CHỐT` vì tưởng đụng quy tắc dùng chung — sai: bản BR-AUTH-08 toàn cục (`srs-v3.5.md:5482`) không hề nhắc TVV/CG, mệnh đề này chỉ nằm ở bản sao nhóm IV. Chữ "owner" còn chọi với **chính cột kiểm chứng cùng dòng** (*"TVV/CG chỉ thấy hồ sơ của mình"*) | Đổi thành "chỉ ĐỌC… không có quyền sửa" |
| P2-3 | Số vị trí trong phiếu tự mâu thuẫn (6/7/5/20) | **Nhận** | Bỏ số tổng, liệt kê theo cụm |

**Codex sai chỗ nào:** không có phát hiện nào sai hoàn toàn. Nhưng phần P1-4 nêu `:1510`/`:1511` ("tùy chọn khi **cán bộ** sửa hồ sơ đã có") là lỗi thì chưa chuẩn — FR-IV-04 §Mô tả định nghĩa Người hỗ trợ chính là *"cán bộ HTPL theo NĐ 55/2019 Đ.7"*, nên chữ "cán bộ" ở đây không sai, chỉ mơ hồ. Đây là câu do BA chốt ngày 30/07 nên giữ nguyên, không tự sửa.
