# Tiêu chí verify — QLHSDNHTCP_03

Mã case: **QLHSDNHTCP_03** (dòng 72, tab `bug`)  ·  Thời điểm viết: **2026-08-06 00:13**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: **HTPLDN · V1.0.8** (chuỗi phiên bản chân
thanh điều hướng) · gói mã `assets/index-DThrFe1_.js` · đo lúc **2026-08-06 00:18–00:40** · khung nhìn 1440×741

> Viết TRƯỚC khi mở màn "Chi trả chi phí" trên env verify. Nguồn lúc viết: 2 dòng phản ánh trên bảng đối tác,
> 2 ảnh bằng chứng, đặc tả SRS v3.5, và **quyết định BA ngày 2026-07-24**.

---

## 1. Đối tác phản ánh — tách theo vòng

| Vế | Vòng | Nội dung đối tác ghi |
|---|---|---|
| **a** | 1 (10/07) | "Cột thông tin **Mức cảnh báo thời hạn** không giống với thiết kế" |
| **b** | 2 (30/07) | "Dữ liệu cột *Mức cảnh báo thời hạn* **bị tràn sang cột Ngày nộp**" |

"Kết quả mong đợi" trên dòng bảng còn nêu 4 ý chung của case: đủ trường theo thiết kế · đúng định dạng ·
**không tràn/đè lên nhau, đồng nhất ngôn ngữ** · mặc định 20 bản ghi/trang.

**Bằng chứng đã mở xem (full-res):**
- `partner-evidence/QLHSDNHTCP_03.jpg` (288.741 bytes) — vòng 1. Bảng có cột tiêu đề **"SLA"**, giá trị dạng
  đếm ngược *"Quá hạn 58 / 60 / 61 / 62 / 64 ngày LV"*. 5 dòng HSCT000066→000070, "Hiển thị 1-5 / 5 kết quả".
- `partner-evidence/QLHSDNHTCP_03_v2.png` (267.652 bytes) — vòng 2. Khung đỏ do đối tác khoanh quanh 2 dòng
  `HSCT000051` + `HSCT000052`: ô cột SLA hiện thẻ nền đen **"Quá hạn nghiêm trọng · 52 ngày LV"** /
  **"· 54 ngày LV"**, thẻ **kéo dài đè lên cột "Ngày nộp"** — chỉ còn đọc được 3 ký tự cuối `026` của ngày.
  3 dòng còn lại (HSCT000053/54/55) hiện thẻ ngắn "Đã hoàn thành" nằm gọn trong ô, cột Ngày nộp đọc được đủ.

⚠️ **Hai vòng bằng chứng KHÔNG cùng điều kiện** — ghi rõ theo yêu cầu Cổng bằng chứng:
vòng 1 vai trò **CB_NV_TW**, bản dựng **V1.0**, hồ sơ HSCT000066-70; vòng 2 vai trò **CB_PD_BN**, bản dựng
**V1.0.2**, hồ sơ HSCT000051-55. Khác cả vai trò, bản dựng lẫn bản ghi ⇒ không coi vòng 2 là "vòng 1 chụp lại".

## 2. Đặc tả nói gì

- **SCR-V.II-01 thành phần #16 (`srs-fr-06-chi-tra.md:1058`)** —
  *"| 16 | table | **SLA** | C07 | 4 mức cảnh báo theo **BR-SLA-02**: Bình thường / Sắp hết hạn / Quá hạn /
  Quá hạn nghiêm trọng (80px) | — | Luôn |"*
- **SCR-V.II-01 thành phần #17 (`srs-fr-06-chi-tra.md:1059`)** —
  *"| 17 | table | **Ngày nộp** | date | dd/mm/yyyy (110px) | — | **Luôn** |"*
- **BR-SLA-02 cho hồ sơ chi trả (`srs-fr-06-chi-tra.md:1514-1523`)** — 4 mức + nhãn tiếng Việt:
  `BINH_THUONG` "Bình thường" (còn >50%) · `SAP_HET` "Sắp hết hạn" (còn <50%) · `QUA_HAN` "Quá hạn" (trễ >100%) ·
  `QUA_HAN_NGHIEM_TRONG` "Quá hạn nghiêm trọng" (trễ >200%). Ghi rõ *"BA điều chỉnh 2026-07-24 — bỏ mô hình
  70/85 riêng của Chi trả"*. Trường entity: `muc_do_canh_bao` (`:1311`).

**🔴 BA ĐÃ CHỐT ĐÚNG ĐIỂM TRANH CHẤP NÀY — dẫn nguồn + ngày:**
`reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-week-3.md:56-63`,
mục "QLHSDNHTCP_03", **ngày 2026-07-24**:
1. *"Tên cột **"SLA"** của app **khớp đặc tả**"* → kỳ vọng đối tác về tên cột "Mức cảnh báo thời hạn"
   **đã được BA bác** ⇒ vế (a) phần **tên cột** = **không phải lỗi**, không hỏi BA lại.
2. *"Dev sửa lại hiển thị theo BR-SLA-02 … app hiện **4 nhãn rời** "Bình thường / Sắp hết hạn / Quá hạn /
   Quá hạn nghiêm trọng" + **giữ số ngày** còn lại"* → phần **định dạng giá trị** thì BA **chốt là bắt buộc**
   ⇒ chấm được, xem mục 4.

**IM LẶNG về:** không có dòng nào quy định bề rộng thực tế phải là đúng 80px, hay ô được phép/không được phép
dùng tooltip. Nên mục 4 **không** chấm theo px của cột mà chấm theo **hệ quả nghiệp vụ**: giá trị Ngày nộp
(thành phần #17, điều kiện hiển thị "Luôn") có còn đọc được đủ hay không.

## 3. Precondition

- Tài khoản: **`cbnv_tw`** (CB Nghiệp vụ TW — cùng vai trò vòng 1) `Test@1234`. Đo lại lần 2 bằng
  **`cbpd_bn`** (CB Phê duyệt Bộ ngành — vai trò vòng 2) để đóng GAP vai trò. Không dùng `admin` ra verdict.
- Màn: **Chi trả chi phí → Danh sách**, URL `/chi-tra/danh-sach`, tab **"Tất cả"**.
- Dữ liệu tiền đề: phải có hồ sơ ở mức **`QUA_HAN_NGHIEM_TRONG`** — đây là mức có **chuỗi nhãn dài nhất**
  ("Quá hạn nghiêm trọng" = 20 ký tự) nên là dạng dễ tràn nhất; thiếu mức này thì phép đo tràn **không kết luận
  được**. Không có sẵn → seed (khai vào báo cáo: đổi bản ghi nào, đổi gì, env nào).

## 4. Tiêu chí chấm

**✅ PASS khi** — thoả **cả 3**:
1. **Nhãn mức rời (BA chốt 2026-07-24):** với mọi dòng, ô cột cảnh báo thời hạn chứa **nguyên văn một trong 4
   chuỗi** `Bình thường` / `Sắp hết hạn` / `Quá hạn nghiêm trọng` / `Quá hạn` (khớp mức đúng theo `muc_do_canh_bao`
   của dòng đó), **kèm** số ngày. Ô chỉ có đếm ngày trần kiểu *"Quá hạn 58 ngày LV"* mà không mang nhãn mức
   ⇒ chưa đạt.
2. **Không tràn:** với mọi dòng, hộp bao nội dung ô cảnh báo **nằm trọn trong** hộp bao ô của chính cột đó —
   phần chồng lấn theo trục ngang với ô cột "Ngày nộp" **= 0 px**.
3. **Ngày nộp vẫn đọc được:** với mọi dòng, giá trị Ngày nộp hiện **đủ 10 ký tự** dd/mm/yyyy, không bị phần tử
   nào phủ lên (kiểm bằng phép chạm điểm giữa ô: phần tử trên cùng tại toạ độ đó phải thuộc chính ô Ngày nộp).

**❌ FAIL nếu** — bất kỳ điều nào: ≥1 dòng có ô cảnh báo chồng lấn > 0 px sang ô Ngày nộp · ≥1 dòng có Ngày nộp
bị che một phần · ≥1 dòng vẫn hiện đếm ngày trần không kèm nhãn mức BR-SLA-02.

**KHÔNG được chấm Fail vì:**
- Tiêu đề cột là **"SLA"** chứ không phải "Mức cảnh báo thời hạn" → **BA đã chốt 2026-07-24** tên "SLA" khớp
  đặc tả. Đây là **áp quyết định có sẵn**, không phải QA tự bác đối tác.
- Cột "Mức HT %" xuất hiện trên app mà không có trong danh sách thành phần SCR-V.II-01, hay tiêu đề cột Tên DN
  để trống — **ngoài phạm vi 2 vế đối tác phản ánh ở case này**; nếu quan sát thấy thì ghi vào mục "lỗi phát
  hiện thêm" của báo cáo, không dùng để chấm case này.

**Phép thử mục 4:** người chưa biết bug, đọc mục 4 xong có chấm được không? → Có: đọc nhãn ô, đo 2 hộp bao,
chạm điểm giữa ô Ngày nộp.

## 5. Dạng dữ liệu phải phủ — M = 4

1. `BINH_THUONG` → nhãn "Bình thường"
2. `SAP_HET` → nhãn "Sắp hết hạn"
3. `QUA_HAN` → nhãn "Quá hạn"
4. `QUA_HAN_NGHIEM_TRONG` → nhãn "Quá hạn nghiêm trọng"  ← **dạng bắt buộc phải có** (chuỗi dài nhất)

**Nguồn xác định M:** cách ① của §Xác định M — đặc tả nói thẳng về nguồn giá trị: BR-SLA-02
(`srs-fr-06-chi-tra.md:1514-1523`) + ràng buộc CHECK của trường `muc_do_canh_bao` (`:1311`) liệt kê **đúng 4**
giá trị. Không cần tra tiếp cách ②/③.

Vì đây là bug về **cột hiển thị dữ liệu**, M **không được** để = 1.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | V1: **CB_NV_TW** "CB Nghiệp vụ TW 01", đơn vị `BTP · TW` · V2: **CB_PD_BN** "Cán bộ PD Bộ ngành", đơn vị `BTP · BN` | Đo **2 lượt, 2 vai trò**: (a) `cbnv_tw` — CB_NV_TW, `BTP · TW` = **trùng khít V1**. (b) `cbpd_tw_01` — **CB_PD**, `BTP · TW`. Đã thử `cbpd_bn` (trùng khít V2) nhưng đơn vị BN có **0 hồ sơ chi trả** → không đo được, phải đổi sang CB_PD cấp TW để giữ đúng **vai trò** V2 mà vẫn có dữ liệu | Không |
| Entity + trạng thái | V1: HSCT000066-70 (Yêu cầu bổ sung / Từ chối / Đã thanh toán ×3) · V2: HSCT000051-55 (Đang thẩm định / Yêu cầu bổ sung / Đã thanh toán ×2 / Từ chối) | 14 hồ sơ `CT-*`, phủ 8 trạng thái gồm **đủ cả 5 trạng thái đối tác gặp**: Đang kiểm tra 4 · Yêu cầu bổ sung 1 · Đang đánh giá 1 · **Đang thẩm định 2** · Đã duyệt 1 · Đã thanh toán 2 · Từ chối 1 · Hủy 1. Bản ghi HSCT-* của đối tác nằm ở env khác | Không |
| Dữ liệu tiền đề | 5 hồ sơ/trang, đều quy mô "Nhỏ", Mức HT 30%. V2 có 2 hồ sơ mức **Quá hạn nghiêm trọng** (52 & 54 ngày LV) | **6 hồ sơ mức "Quá hạn nghiêm trọng"** (11/14/14/16/20/53 ngày LV) — nhiều hơn V2, gồm cả chuỗi dài nhất "53 ngày LV". Quy mô phủ Siêu nhỏ/Nhỏ/Vừa. **Không seed gì cho case này** | Không |
| Input / filter / giá trị nhập | Tab **"Tất cả"**, không nhập từ khoá, không lọc trạng thái/quy mô/ngày. V2 URL `?tab=TAT_CA&page=1` | Tab **"Tất cả"**, không từ khoá, không lọc — `?tab=TAT_CA&page=1`, **trùng khít V2**. Đo ở **2 vị trí cuộn ngang** (mặc định + cuộn hết sang phải) vì cột "Hành động" dán cố định che phần bên phải khi chưa cuộn | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | V1: N=5, chỉ thấy 1 dạng cảnh báo (đếm ngày). V2: N=5, thấy 2 dạng ("Quá hạn nghiêm trọng" ×2, "Đã hoàn thành" ×3) | **N = 14 × 2 vai trò = 28 lượt đo dòng.** M = **4/4** mức BR-SLA-02 đều có mặt: Bình thường 1 · Sắp hết hạn 1 · Quá hạn 2 · Quá hạn nghiêm trọng 6. (+ 4 dòng hiện nhãn thứ 5 "Đã hoàn thành" — xem mục sửa đổi) | Không |

**GAP còn lại: 0.** Riêng dòng "Vai trò": không đóng được bằng đúng `cbpd_bn` (0 dữ liệu ở cấp BN — blocker
khách quan, không phải tiền đề tự tạo được), nên đóng bằng cách **thử đủ nhánh vai trò khả dĩ có dữ liệu**
(CB NV và CB PD), **hai nhánh cho cùng kết quả** ⇒ điều kiện vai trò không đổi được kết luận.

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** V1 `https://htpldn-uat.ospgroup.vn/chi-tra/danh-sach` (HSCT000066-70) ·
  V2 `https://htpldn-uat.ospgroup.vn/chi-tra/danh-sach?tab=TAT_CA&page=1` (HSCT000051-55)
- **Trạng thái entity:** V2 hai dòng lỗi ở `DANG_THAM_DINH` và `YEU_CAU_BO_SUNG`, cảnh báo `QUA_HAN_NGHIEM_TRONG`
- **Vai trò + bản dựng:** V1 CB_NV_TW · **HTPLDN · V1.0** · 2026-07-10 10:09 —
  V2 CB_PD_BN · **HTPLDN · V1.0.2** · 2026-07-30 10:53

> ⚠️ **Lệch env:** cả 2 vòng quay trên env nghiệm thu `ospgroup.vn`; đợt này verify trên env dev
> `18.143.165.120.nip.io`. Verdict Pass (nếu có) chỉ có hiệu lực cho env + bản dựng ghi ở đầu file.

---

## 7. SỬA ĐỔI TIÊU CHÍ — 2026-08-06 00:45 (sau khi đo, TRƯỚC khi chốt verdict)

**Sửa gì:** thu hẹp phạm vi ý 1 của mục 4.

- **Bản gốc (viết 00:13):** *"với **mọi dòng**, ô cột cảnh báo thời hạn chứa nguyên văn một trong 4 chuỗi…"*
- **Bản sửa:** *"với mọi dòng có hồ sơ **còn đang xử lý** (trạng thái chưa kết thúc), ô cột cảnh báo thời hạn
  chứa nguyên văn một trong 4 chuỗi…"*

**Vì sao sửa:** lúc viết tiêu chí tôi không lường trước nhóm hồ sơ **đã kết thúc**. Khi đo mới thấy 4 dòng ở
trạng thái kết thúc (`DA_THANH_TOAN` ×2, `TU_CHOI`, `HUY`) hiện **nhãn thứ 5 "Đã hoàn thành"** — nhãn này
không nằm trong 4 mức BR-SLA-02, và **lệch cả dữ liệu**: gọi `GET /api/v1/ho-so-chi-tras` thì đúng 4 bản ghi
đó trả `mucDoCanhBao = "BINH_THUONG"`. Đặc tả **không có dòng nào** nói cột này phải hiển thị gì khi hồ sơ đã
kết thúc; BR-SLA-02 chỉ có câu *"Nếu không thỏa điều kiện nào thì hiển thị 'Bình thường'"* — đọc thẳng thì
4 dòng đó phải ghi "Bình thường", nhưng ghi "Bình thường" cho hồ sơ đã Từ chối / Hủy thì vô nghĩa về nghiệp vụ.

**Hệ quả — KHÔNG tự chấm:** đây là **đặc tả im lặng**, nên tôi **không** dùng nó để chấm Fail, cũng **không**
lờ đi để chấm Pass. Chuyển thành **câu hỏi cho BA** (`../cau-hoi-BA.md` §1) và ghi rõ hiện trạng đo được.
Verdict của case vì thế là **cần BA**, không phải Pass — dù **cả 2 vế đối tác phản ánh đều đã hết lỗi**.

**Không sửa mục 5** (M vẫn = 4 mức BR-SLA-02, cả 4 đều đã phủ). Không sửa ý 2 và ý 3 của mục 4.
