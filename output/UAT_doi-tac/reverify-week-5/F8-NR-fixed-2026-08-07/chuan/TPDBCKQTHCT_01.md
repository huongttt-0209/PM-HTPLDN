# Chuẩn chấm đã khóa — TPDBCKQTHCT_01 (dòng 340) — "Trình phê duyệt báo cáo kết quả thực hiện chương trình"

> **Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` —
> chính là `srs-fr-15-ct-htpldn.md` (1.610 dòng), có dùng thêm **một cross-ref trong cùng thư mục nguồn
> chuẩn**: `srs-v3.5.md` §D.1.2 + §D.2.1 (bảng 13 cột Biểu 21a).
> **Mọi số dòng dưới đây do agent này tự mở file đếm lại ngày 2026-08-07 (lượt hiện tại).**
> Không lấy số dòng từ `input/srs-update-2026-5-5/`, từ thư BA, từ ô verify cũ, từ hồ sơ lô F5.
>
> **Trạng thái phiếu:** `Trạng thái` (N) = **`Fail`** · `Dopai` (O) = **`Open`** · `Trạng thái dev fix` (R) =
> **`Fixed`** · `Ảnh/vieo 1` (M) = `TPDBCKQTHCT_01.webm` (có bằng chứng đối tác) ·
> `Kết quả verify` (T) **ĐÃ CÓ NỘI DUNG** — QA ghi lúc **03:07 ngày 07/08/2026**, kết luận **Reopen**.
> ⇒ **Phiếu này KHÁC 4 phiếu còn lại của lô F8**: đối tác **ĐÃ chạy** và QA **ĐÃ verify một lượt**.
>
> 🔴 **Vì sao phải đo lại:** bản dựng lúc đo lượt trước là `index-D4Buvu4S.js` (07/08 02:23 giờ VN);
> lượt trinh sát 11:33 đọc được `index-eWHwDgt2.js` (07/08 09:11); prompt lượt này báo bản đang chạy là
> `index-BbPPdate.js` (07/08 13:47) ⇒ **đã qua ≥2 lần triển khai kể từ phép đo cũ**. Dev cũng đã **lật ô
> `Trạng thái dev fix` về `Fixed`** sau khi QA ghi Reopen. **Cấm suy verdict từ số cũ.**
>
> **Cổng bằng chứng (flow 04):** có video đối tác + có phép đo cũ của chính QA ⇒ đủ neo tái hiện
> (vai trò CB NV cấp ĐP · đợt `MAU_21A` · màn Chi tiết đợt). **Cấm kết luận "không phải lỗi" chỉ vì
> không tái hiện được.**

**Expected đối tác (nguyên văn K340, giữ nguyên xuống dòng):**
```
- Chuyển trạng thái đợt báo cáo: Đang lập báo cáo → Chờ duyệt kết quả.
+ Gửi thông báo cho cán bộ phê duyệt cùng đơn vị.
+ Lưu vết thao tác theo quy định.
- Trình thành công, hệ thống hiển thị "Đã trình phê duyệt báo cáo".
```

**Kết quả thực tế của đối tác (nguyên văn L340):**
```
Hệ thống không cập nhật trạng thái mặc dù có thông báo trình duyệt thành công
```

---

## 0. Ô `Kết quả verify` cũ (03:07 · 07/08) — rút ba nhóm, KHÔNG dùng làm chuẩn chấm

Ô verify cũ là **manh mối chỉ chỗ cần đo**, không phải căn cứ verdict lượt này.

| Nhóm | Nội dung rút được | Hệ quả cho lượt này |
|---|---|---|
| **(a) Triệu chứng gốc của đối tác đã HẾT** | Ở lượt trình **đi lọt được**: màn Chi tiết đợt đọc "Chờ duyệt kết quả", thanh tiến trình sang bước 3, giữ nguyên sau khi tải lại trang bằng địa chỉ; báo cáo sang Chờ phê duyệt; `cbpd_hn` **cùng đơn vị** nhận đúng thông báo trùng mốc giờ; nhật ký có mục thao tác trình | ⚠️ **Nhưng lượt trình đó chỉ đi lọt SAU KHI QA đã ép tiền đề bằng đường dữ liệu** (ô verify cũ tự khai). ⇒ (a) **chưa từng được chứng minh trên đường UI thuần**. Phải đo lại theo §5 |
| **(b) Điểm hỏng MỚI, lý do Reopen** | Trên báo cáo mà **13/13 chỉ tiêu đều đang hiện giá trị** (1→11 hiện sẵn `0 (HT)` **không có ô nhập**; 12, 13 có ô nhập, đã nhập `1207`/`1308`), bấm [Trình duyệt KQ] → [Đồng ý] → bị chặn `"Vui lòng hoàn chỉnh báo cáo trước khi trình"` + liệt kê **đúng 11 chỉ tiêu "còn thiếu" trùng khít 11 chỉ tiêu không có ô nhập**. Lặp 3 lần như nhau. Trạng thái đứng nguyên. Đợt thứ hai (`DOT-TRON_NAM-2026-1`, `CA_HAI`) cũng bị chặn cùng cách | Đây là **cổng chặn của C1a** lượt này (§5.1). Nhưng 🔴 **wording cũ SAI HƯỚNG** — xem §1.2 |
| **(c) QA đã tự ghi là KHÔNG thuộc phạm vi phiếu** | ① Mã lỗi trả về `ERR-VAL-XI-07-02` ≠ `:825` khai `ERR-XI-07-01` (câu chữ thì khớp) · ② Trường `trang_thai` của bản ghi **ĐỢT** vẫn đứng `TAO_DOT` kể cả sau khi trình thành công (đặc tả tự mâu thuẫn) · ③ Dữ liệu đã lưu có 3 khóa (`soVuViec`, `soDnDuocHoTro`, `tongChiPhi`) không dòng nào trên bảng 13 chỉ tiêu hiển thị | ① giữ nguyên **ghi nhận, không chấm** (§9). ② lượt này **nâng thành vế `C1b` GAP có route BA** vì expected nói thẳng "trạng thái **đợt** báo cáo" (§1.1). ③ ghi nhận, không chấm |

---

## 1. BẢNG SCOPE LOCK — 5 vế

| Vế | Expected đối tác (nguyên văn) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS then chốt | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|---|
| **C1a** | *"Chuyển trạng thái … Đang lập báo cáo → Chờ duyệt kết quả"* — **phần chấm được**: thao tác **đi lọt** và trạng thái **người dùng thấy** + bản ghi **BÁO CÁO** chuyển đúng | **`:803`** (vế BC) · `:829` · `:802` · `:1170` · `:1418` · `:1389` · `:1195`/`:1196` | `:803` = `\| 3 \| Chuyển trạng thái BC sang CHO_PHE_DUYET, đợt BC sang CHO_DUYET_KQ \| SM-DOT-BC \|` · `:829` = `- **Given** CB NV chọn BC hoàn chỉnh theo định nghĩa ở Processing bước 2 **When** nhấn "Trình phê duyệt" **Then** BC → CHO_PHE_DUYET, đợt BC → CHO_DUYET_KQ, gửi thông báo CB PD` | **MATCH** | **TEST** | **UI:** trên báo cáo đã hoàn chỉnh theo `:802` **dựng bằng giao diện** (§5.1 cổng TĐ-UI), bấm [Trình duyệt KQ] → [Đồng ý] → thao tác **không bị chặn**, nhãn trên màn của đơn vị chuyển sang "Chờ duyệt kết quả". **Đối chứng:** đọc lại bản ghi (`GET /api/v1/dot-bao-caos/{id}`) → `trang_thai` của **BÁO CÁO** = `CHO_PHE_DUYET` và `trangThaiNop` của **đơn vị mình** = `CHO_DUYET` |
| **C1b** | cùng câu trên — **phần "trạng thái ĐỢT báo cáo"** hiểu theo nghĩa đen: trường `trang_thai` của bản ghi **`DOT_BAO_CAO`** đi `DANG_LAP_BC → CHO_DUYET_KQ` | `:789` · `:803` · `:814` · `:818` · `:1512` · `:739`–`:747` (`:746`) · `:1368` · `:1367` · `:1398` · `:1389` | `:789` = `- Đợt BC ở trạng thái DANG_LAP_BC` · `:1512` = `\| TAO_DOT \| DANG_LAP_BC \| CB NV bắt đầu lập BC \| Đợt đã hoàn chỉnh thông tin \| Tạo BAO_CAO_CT_HTPL record \| FR-XI-06 \| — \|` · `:746` = `\| 8 \| Cập nhật DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop = DANG_LAP + bao_cao_id = <bao_cao mới> \| — \|` | **GAP** (đặc tả **tự mâu thuẫn**) | **BA** | Chỉ **ghi nhận hiện trạng**, không chấm: đọc `trang_thai` cấp ĐỢT trước/sau thao tác. **CẤM** lấy nó làm lý do FAIL, **CẤM** ép giá trị này bằng bất kỳ đường nào |
| **C2** | *"Gửi thông báo cho cán bộ phê duyệt cùng đơn vị"* | **`:804`** (chính) · `:819` · `:1170` · `:1513` + `:1552` (cùng đơn vị) · `:897` | `:804` = `\| 4 \| Gửi thông báo CB PD \| — \|` · `:819` = `- Thông báo gửi CB PD` · `:1552` = `\| **Phát biểu** \| CB NV cấp nào tạo → CB PD cùng đơn vị duyệt. KHÔNG xuyên cấp phê duyệt \|` | **MATCH** | **TEST** | **UI:** đăng nhập `cbpd_dp_04` (**đã xác minh cùng `donViId`**) → chuông/màn Thông báo → có mục về báo cáo vừa trình, mốc giờ khớp. **Đối chứng:** `GET /api/v1/thong-baos` bằng token riêng của **chính tài khoản đó** (lược đồ: *"Chỉ trả về thông báo có nguoiNhanId trùng người đăng nhập"*), so `createdAt` với mốc bấm |
| **C3** | *"Lưu vết thao tác theo quy định"* | **`:805`** (chính) · `:1532` · `:1568` | `:805` = `\| 5 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` · `:1568` = `\| **Phát biểu** \| Mọi thao tác CUD + phê duyệt đều ghi vào AUDIT_LOG. Log là immutable \|` | **MATCH** | **TEST** | **Đường 1:** `GET /api/v1/audit-logs?hanhDong=SUBMIT&tuNgay=…&denNgay=…` bằng **chính phiên `cbnv_dp_04`** (lược đồ: *"ngoài TW chỉ xem bản ghi của chính mình"*) → **đọc** `entityType`/`entityId`/`thoiGian` từ phản hồi, **cấm đoán trước**. **Đối chứng:** màn Nhật ký hệ thống của QTHT hiển thị đúng dòng đó (khai rõ tài khoản đọc log; **không** dùng để ra verdict vế khác) |
| **C4** | *"Trình thành công, hệ thống hiển thị **«Đã trình phê duyệt báo cáo»**"* | **IM LẶNG** — đã rà `:810`–`:814` (Outputs), `:816`–`:819` (Postconditions), `:821`–`:825` (Error Handling, **chỉ có E1 lỗi**), `:1170` (button-group **không** ghi toast), đối chiếu `:1173` của FR-XI-08 **có** ghi `Toast success` | `:825` = `\| E1 \| BC chưa hoàn chỉnh \| ERR-XI-07-01 \| "Vui lòng hoàn chỉnh báo cáo trước khi trình" \| ERROR \|` — **đây là dòng thông báo DUY NHẤT của FR-XI-07, và là dòng LỖI, không phải dòng thành công** | **GAP** (SRS im lặng) | **BA** | Vẫn **đo hiện trạng** vì cùng một cú bấm với C1a: cài `toast-capture.js` **TRƯỚC** khi bấm, đọc `innerText`, **CẤM lọc trùng**. **Đối chứng:** chuỗi `message` trong phản hồi máy chủ của chính lượt bấm. 🔴 **Đo xong vẫn KHÔNG được Pass vế này** (luật khóa 5) |

**Tổng: 5 vế — 3 MATCH (C1a · C2 · C3) · 0 DIFF · 2 GAP (C1b · C4).** Route **TEST ×3 + BA ×2**.

🔴 **Verdict logic sớm nhất có thể = `Cần BA`** (khi C1a/C2/C3 đều đạt), hoặc **`Reopen + Cần BA`**
(khi còn ≥1 vế MATCH sai). **Phiếu này KHÔNG có đường Pass thuần** — vì C1b và C4 là GAP.

### 1.1 Vì sao tách `C1a` / `C1b` — và vì sao không được gộp

Expected viết *"Chuyển trạng thái **đợt báo cáo**: Đang lập báo cáo → Chờ duyệt kết quả"*. Đặc tả có **hai
trục trạng thái khác nhau** cho cùng một sự việc, và **tự mâu thuẫn** ở trục ĐỢT:

| Trục | Trường | Enum | Dòng | Chấm được? |
|---|---|---|---|---|
| **BÁO CÁO** | `BAO_CAO_CT_HTPL.trang_thai` | `DU_THAO` · `CHO_PHE_DUYET` · `DA_DUYET` · `TU_CHOI` | `:1418` | ✅ `:803` khai rõ `→ CHO_PHE_DUYET` |
| **ĐƠN VỊ NỘP** | `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` | `CHUA_NOP` · `DANG_LAP` · `CHO_DUYET` · `DA_DUYET` · `DA_NOP` · `QUA_HAN` | `:1389` | ✅ đây là trục **một-đơn-vị-một-giá-trị**, khớp nhãn màn |
| **ĐỢT** | `DOT_BAO_CAO.trang_thai` | `TAO_DOT` · `DANG_LAP_BC` · `CHO_DUYET_KQ` · `DA_DUYET_KQ` · `DA_GUI_TW` · `DA_TONG_HOP` | `:1368` | ❌ **mâu thuẫn** — xem 3 điểm dưới |

**Ba điểm mâu thuẫn, đã đọc trọn để khẳng định (không phải grep rỗng):**

1. **Tiền đề `:789` không có chức năng nào tạo ra được.** `:789` = *"Đợt BC ở trạng thái DANG_LAP_BC"*.
   `:1512` khai bước `TAO_DOT → DANG_LAP_BC` do **FR-XI-06** thực hiện. Nhưng đã đọc **trọn** Processing
   FR-XI-06 `:737`–`:747` (9 bước): bước `:746` **chỉ** đặt `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop =
   DANG_LAP`; **không bước nào** đụng `DOT_BAO_CAO.trang_thai`. Đọc thêm `:749`–`:758` (Outputs +
   Postconditions FR-XI-06): cũng không nhắc trạng thái đợt.
2. **Một đợt chỉ có MỘT giá trị trạng thái, nhưng phục vụ ~70–83 đơn vị.** `:1368` cho `DOT_BAO_CAO.trang_thai`
   một giá trị; `:1367` khai `pham_vi_don_vi_nop_ids[]` = *"63 ĐP + BN"*; `:1398` = *"~3 đợt/năm × ~70 đơn vị
   = ~210 records/năm"*; `:646` cho TW chỉnh phạm vi thủ công. Một đơn vị trình duyệt thì đợt của 82 đơn vị
   còn lại chuyển theo — đặc tả không giải quyết.
3. **Đợt thực tế đứng yên `TAO_DOT`** (ghi nhận (c)② ở §0) trong khi nhãn người dùng thấy suy từ trục ĐƠN VỊ.

⇒ **`C1b` = `GAP`, route `BA`.** Kết quả đo **không** biến nó thành `MATCH` (luật khóa 5 flow 04).
⇒ **`C1a` = phần chấm được**, neo vào vế **BÁO CÁO** của `:803` + AC `:829` + nhãn màn.

> 🔴 **Câu hỏi BA của `C1b` CÙNG GỐC với câu Q1 đã mở** (phiếu 343 · C2, và bàn giao lô F5 §3 Nhóm 2)
> ⇒ **liên kết, KHÔNG mở câu hỏi trùng**; chỉ bổ sung đúng nhánh FR-XI-07 (xem §8).

### 1.2 🔴 PHÁT HIỆN LƯỢT NÀY — "11 chỉ tiêu không có ô nhập" là **ĐÚNG ĐẶC TẢ**, không phải lỗi

Ô verify cũ mô tả điểm hỏng theo hướng *"cán bộ **không sửa được** 11 chỉ tiêu đó"* và đề nghị theo hướng đó.
**Hướng này va vào đặc tả.** Đã mở `srs-v3.5.md` §D.2.1 (`:6674`–`:6690`) — bảng ánh xạ **13 cột Biểu 21a**:

```
:6676  | Cột 21a | Tên cột | Entity nguồn | Công thức |
:6678  | -1  | Số TVV kiện toàn   | TU_VAN_VIEN    | Đếm số TVV có trạng thái = 'HOAT_DONG' thuộc đơn vị báo cáo |
 …      (cột -2 → -11 đều có Entity nguồn + Công thức đếm/tổng từ dữ liệu hệ thống)
:6688  | -11 | KP HT TVPL (NSNN)  | HO_SO_CHI_TRA  | Tổng số tiền thực trả của hồ sơ đã thanh toán |
:6689  | -12 | KP chi HĐ khác     | —              | Nhập thủ công |
:6690  | -13 | KP xã hội hóa      | —              | Nhập thủ công |
```

⇒ **Đặc tả quy định đúng hình thái mà màn đang làm: cột -1 → -11 do hệ thống tính, chỉ cột -12 và -13 là
"Nhập thủ công".** Giao diện hiện `0 (HT)` cho 11 cột và chỉ mở ô nhập cho 2 cột **là khớp `:6678`–`:6690`**.

*(Ghi chú: `:731` cho `so_lieu` nguồn *"Nhập tay / Auto"* và `:744` viết *"CB NV nhập/chỉnh sửa số liệu"* —
căng với §D.2.1. Đây là mâu thuẫn phụ, **không** phải vế của phiếu ⇒ ghi nhận ở §9, không chấm, không hỏi BA
riêng.)*

**Hệ quả bắt buộc cho lượt này — 2 điều:**

1. ❌ **CẤM FAIL vì "11 chỉ tiêu không có ô nhập".** Đó là đúng `:6678`–`:6688`. FAIL vì lý do này = **Fail oan**
   và ép dev làm ngược đặc tả.
2. ✅ **Điều thật sự phải chấm ở `C1a`:** một báo cáo mà **mọi chỉ tiêu bắt buộc đều đã có giá trị (kể cả 0)**
   thì **phải trình được**. Neo: `:802` — *"giá trị **0 là đã điền** (đơn vị không phát sinh hoạt động trong
   kỳ vẫn phải nộp)"* — cộng AC `:829`. Nếu hệ thống vẫn báo "còn thiếu" đúng 11 cột mà chính nó tính ra
   thì **không đơn vị nào trình được bằng giao diện** ⇒ AC `:829` không thể đạt ⇒ **FAIL `C1a`**.

🔴 **Wording bắt buộc khi ghi kết quả (describe, KHÔNG prescribe):**
> ✅ *"Theo `:802` + `:829`, đơn vị có báo cáo mà toàn bộ chỉ tiêu bắt buộc của biểu mẫu đang áp dụng đều đã
> có giá trị (kể cả toàn bộ bằng 0) phải trình phê duyệt được; hiện tại thao tác bị chặn với thông báo còn
> thiếu N chỉ tiêu."*
> ❌ *"Phải cho cán bộ nhập tay 11 chỉ tiêu"* · ❌ *"Phải sửa endpoint `submit-bc` bỏ kiểm 13 khóa"*.

### 1.3 Căn cứ khẳng định đã đọc trọn mục (không phải grep rỗng)

- **FR-XI-07 `:773`–`:831`, đọc trọn:** Mô tả `:782`, Tác nhân `:784`, Preconditions `:786`–`:789`,
  Inputs `:791`–`:795`, Processing `:797`–`:805` (5 bước), BR áp dụng `:807`–`:808`, Outputs `:810`–`:814`,
  Postconditions `:816`–`:819`, Error Handling `:821`–`:825` (**chỉ một dòng E1, là dòng LỖI**),
  AC `:827`–`:830`.
- **FR-XI-06 `:701`–`:770`, đọc trọn** (để khóa `C1b` + tiền đề): Tác nhân `:712`, Preconditions `:714`–`:718`,
  Inputs `:720`–`:733`, Processing `:735`–`:747`, Outputs/Postconditions `:749`–`:758`, Error `:760`–`:764`,
  AC `:766`–`:769`.
- **FR-XI-05a `:612`–`:698`, đọc trọn** (để khóa phương án đợt dự phòng): `:625` · `:646` · `:654` · `:656` ·
  `:657` · `:660` · `:688`.
- **Màn `:1161`–`:1175`** (Chi tiết Đợt BC, dòng #35–#45) + **bảng nhãn SM-DOT-BC `:1190`–`:1199`** +
  **Quy tắc tương tác `:1217`–`:1232`** (`:1228` = *"Trinh duyet KQ -> validate -> SET CHO_DUYET_KQ -> TB CB PD"*).
- **Entity `:1350`–`:1422`** (DOT_BAO_CAO · DOT_BAO_CAO_DON_VI_NOP · BAO_CAO_CT_HTPL) + **SM-DOT-BC
  `:1491`–`:1517`** (đọc trọn bảng 7 dòng chuyển) + **BR `:1521`–`:1606`**.
- **Rà chuỗi thành công toàn thư mục nguồn chuẩn:** không có mã `INF-XI-07-*` ở bất kỳ file nào; chuỗi
  *"Đã trình phê duyệt báo cáo"* không xuất hiện ở bất kỳ file nào trong `srs-v3.5/`.
- Không có dấu `[STT…]` / `[CR-…]` / `[BA chốt …]` nào khác đụng vào 5 vế này, ngoài `[BA chốt 2026-08-06]`
  ở `:802` và `[STT 52 UAT 2026-05-26]` ở tiêu đề FR-XI-05a/06 + các entity.

---

## 2. Định nghĩa "BC hoàn chỉnh" — nguyên văn đặc tả, và 13 chỉ tiêu là gì

```
:802  | 2 | **Kiểm tra BC hoàn chỉnh** `[BA chốt 2026-08-06]`: đủ toàn bộ chỉ tiêu của biểu mẫu tại
      `bieu_mau_su_dung` — `MAU_21A` → 13 chỉ tiêu biểu 21a; `MAU_21B` → theo biểu 21b; `CA_HAI` → cả
      hai biểu. Ô để trống là **chưa điền**; giá trị **0 là đã điền** (đơn vị không phát sinh hoạt động
      trong kỳ vẫn phải nộp). `nhan_xet` **không** tính vào điều kiện này | — |
```

**Bộ 13 chỉ tiêu Biểu 21a** — khung biểu ở `srs-v3.5.md:6589`–`:6596` (§D.1.2), tên cột + nguồn ở
`:6678`–`:6690` (§D.2.1):

| Cột | Tên cột (`:6678`–`:6690`) | Nguồn theo §D.2.1 | Khóa quan sát được trong dữ liệu *(manh mối lô F5/kiểm kê — KHÔNG phải chuẩn chấm)* |
|---|---|---|---|
| -1 | Số TVV kiện toàn | `TU_VAN_VIEN` — hệ thống đếm | `soTvvKienToan` |
| -2 | Cuộc tập huấn | `KHOA_HOC` — hệ thống đếm | `soCuocTapHuan` |
| -3 | Hội nghị đối thoại | `KHOA_HOC` — hệ thống đếm | `soHoiNghiDoiThoai` |
| -4 | VB TL UBND | `VU_VIEC` — hệ thống đếm | `soVBTraLoiUBND` |
| -5 | VB TV mạng lưới | `VU_VIEC` — hệ thống đếm | `soVBTvMangLuoiTVV` |
| -6 | HS tiếp nhận | `HO_SO_CHI_TRA` — hệ thống đếm | `soHsTiepNhan` |
| -7 | HS giải quyết tổng | `HO_SO_CHI_TRA` — hệ thống đếm | `soHsGiaiQuyetTong` |
| -8 | DN vừa | `HO_SO_CHI_TRA` — hệ thống đếm | `hsDoanhNghiepVua` |
| -9 | DN nhỏ | `HO_SO_CHI_TRA` — hệ thống đếm | `hsDoanhNghiepNho` |
| -10 | DN siêu nhỏ | `HO_SO_CHI_TRA` — hệ thống đếm | `hsDoanhNghiepSieuNho` |
| -11 | KP HT TVPL (NSNN) | `HO_SO_CHI_TRA` — hệ thống tổng | `kpHoTroTvpl` |
| **-12** | **KP chi HĐ khác** | **`—` · Nhập thủ công** | `kpHoatDongKhac` |
| **-13** | **KP xã hội hóa** | **`—` · Nhập thủ công** | `kpXaHoiHoa` |

⇒ **Chỉ tiêu người dùng phải tự điền = đúng 2 cột (-12, -13).** 11 cột còn lại là **đầu ra của hệ thống**.
⇒ `nhan_xet` bỏ trống **KHÔNG** phải "chưa đầy đủ" (`:802`). Giá trị `0` **KHÔNG** phải "chưa đầy đủ" (`:802`).

---

## 3. Vai trò / tác nhân — dẫn dòng SRS + bộ tài khoản `_04`

**Prompt lượt này chỉ định bộ `_04`** (khác brief lô F8 §3 vốn ghi `_03`) ⇒ dùng `_04`, và **khai rõ tài
khoản thực dùng** trong báo cáo đo.

| Vai trò trong phiếu | Dòng SRS neo | Tài khoản `_04` đề xuất | Dùng để |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ của **đơn vị nộp** (cấp **ĐP** hoặc **BN**) | `:784` *"Cán bộ Nghiệp vụ"*; hẹp lại ở khâu lập BC `:712` = *"**CB Nghiệp vụ cấp ĐP/BN** (đơn vị thuộc phạm vi đợt BC)"*; `:716`–`:718` | **`cbnv_dp_04`** · `Test@1234` (ưu tiên) — dự phòng **`cbnv_bn_04`** | 🔴 **Bấm [Trình duyệt KQ] bằng giao diện thật** — tài khoản chốt C1a/C3/C4 |
| **CB Phê duyệt CÙNG ĐƠN VỊ** — người nhận thông báo | `:804` · `:819` · `:1171` (*"user la CB PD cung cap"*) · `:1513` BR Ref `BR-AUTH-05` · `:1552` · `:897` (`ERR-XI-07a-03` *"Bạn chỉ được phê duyệt BC cùng đơn vị"*) | **`cbpd_dp_04`** · `Test@1234` | **CHỈ ĐỌC thông báo** để đo C2. 🔴 **KHÔNG bấm [Phê duyệt]/[Từ chối]** — ngoài vế, và sẽ tiêu hủy trạng thái vừa đo |
| Dựng đợt dự phòng (chỉ khi không còn cặp (đợt, đơn vị) dùng được) | `:625` = *"**Chỉ CB Nghiệp vụ cấp TW (Bộ Tư pháp)**"* | `cbnv_tw_04` · `Test@1234` | **CHỈ dựng tiền đề**, không ra verdict |
| Đọc nhật ký (đối chứng C3, nếu vai trò CB NV không có màn nhật ký) | — | QTHT / `admin` · `Secret@123` | **CHỈ đọc log**, khai rõ. **CẤM dùng ra verdict bất kỳ vế nào** |

### 3.1 🔴 Hai điều BẮT BUỘC xác minh trước khi đo (chưa ai đọc được, KHÔNG được đoán)

1. **`cbnv_dp_04` thuộc đơn vị nào?** — `input/input.md:49` **không ghi đơn vị**. Toàn repo chỉ có một
   ghi chép về bộ `_04`: `reverify-week-3/dev-fix-reverify-round-7-2026-07-25/measurements.md:411` khai
   `cbnv_bn_04` ở đơn vị `…-8001-…0001` (= **Bộ Kế hoạch và Đầu tư**, trùng `cbnv_bn_03`).
   **Không có dòng nào về `cbnv_dp_04`.** ⇒ Bước đầu tiên: `GET /api/v1/auth/me` cho `cbnv_dp_04` **và**
   `cbpd_dp_04`, ghi `capDonVi` + `donViId` + tên đơn vị vào báo cáo.
2. **Cặp CB NV ↔ CB PD phải TRÙNG `donViId`.** Lệch ⇒ **không đo được C2**. Xử lý theo **Rule 7** —
   fallback **cùng vai trò + cùng cấp** (`_05`, rồi `_03`), **khai rõ tài khoản thực dùng và lý do lệch
   prompt**. 🔴 **CẤM đổi ĐP ↔ BN ↔ TW để "cho chạy được"**. *(Cặp đã xác minh sẵn nếu cần rơi về:
   `cbnv_dp_03` + `cbpd_dp_03` = **Sở Tư pháp An Giang** `…-8002-…0006`, nguồn `01-KIEM-KE-TIEN-DE.md` §2.)*

### 3.2 Cấp của đợt/báo cáo phải khớp cấp tài khoản

Đợt do TW phát hành cho cả nước (`:621`, `:1370` *"don_vi_id … **luôn = TW**"*); cái phải khớp là
**đơn vị của `cbnv_dp_04` nằm trong `pham_vi_don_vi_nop_ids[]` của đợt** (`:717` · `:1367` · `:646`).
Ngoài phạm vi ⇒ máy chủ trả **404** — **đây là phân quyền đúng thiết kế, KHÔNG phải "mất bản ghi"**.

---

## 4. Kiểm kê tiền đề — có sẵn gì · phải dựng gì · dựng thì mutate gì

### 4.1 Ảnh chụp dữ liệu 11:33–11:50 ngày 07/08 *(manh mối — BẮT BUỘC đọc lại trước khi đo)*

Nguồn: [`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2. **4 đợt, cả 4 đều `trang_thai = TAO_DOT`.**

| # | `maDot` | Kỳ | Biểu mẫu | Phạm vi | `id` |
|---|---|---|---|---|---|
| 1 | `DOT-TRON_NAM-2026-1` | `TRON_NAM` | `CA_HAI` | **2 đơn vị** | `a63a3214-d1d3-421b-8c0c-cec5db419413` |
| 2 | `DOT-THBC01-UAT` | `SO_BO_6_THANG` | `MAU_21A` | **2 đơn vị** (cả 2 đã `DA_NOP`) | `d7a62f6e-a119-4582-8b08-f935d25c534b` |
| **3** | **`DOT-SO_BO_NAM-2026-1`** | `SO_BO_NAM` | **`MAU_21A`** | **83 đơn vị** — `CHUA_NOP` **80** · `CHO_DUYET` 1 · `DANG_LAP` 1 · `DA_NOP` 1 | `e9909d96-1391-463b-8072-b1b56c319f8e` |
| **4** | **`DOT-SO_BO_6_THANG-2026-1`** | `SO_BO_6_THANG` | **`MAU_21A`** | **83 đơn vị** — `CHUA_NOP` **81** · `CHO_DUYET` 1 · `DANG_LAP` 1 | `a61e07f1-e205-4948-ad7d-a3ccac49830a` |

### 4.2 🟢 Đính chính giả định trong prompt: đợt `DOT-SO_BO_NAM-2026-1` **VẪN DÙNG ĐƯỢC**

Prompt lưu ý *"lượt trước đã đẩy `DOT-SO_BO_NAM-2026-1` sang «Chờ duyệt kết quả» bằng đường dữ liệu ⇒ đợt đó
có thể KHÔNG còn ở tiền đề đúng"*. **Kiểm kê 11:33 cho thấy khác:**

- Bản ghi **ĐỢT** vẫn `TAO_DOT` (không có chức năng nào đổi nó — chính là GAP `C1b`).
- Cái bị tiêu là **ô của Sở Tư pháp Hà Nội** trong đợt đó: đã đi hết vòng tới `DA_NOP` / báo cáo
  `4db99158-5bc4-4069-9d52-cfc756aadc2e` = `DA_GUI_TW`, mốc 2026-08-06 20:11. Đó là đơn vị của `cbnv_hn`
  (tài khoản lượt trước), **không phải** đơn vị của bộ `_04`.
- **80 đơn vị còn `CHUA_NOP`** trong đợt #3 và **81 đơn vị còn `CHUA_NOP`** trong đợt #4.

⇒ **Nếu đơn vị của `cbnv_dp_04` nằm trong 83 đơn vị và đang `CHUA_NOP`, tiền đề gần như chắc chắn dựng được,
và có 2 đợt độc lập (#3 và #4) ⇒ đo được 2 lượt.**
⚠️ Vẫn là **manh mối**: môi trường dùng chung, phải đọc lại ngay trước khi đo.

### 4.3 Bảng "phải dựng gì" — và mutate cái gì

| Việc | Có sẵn? | Đường được phép | Mutate cái gì (BẮT BUỘC khai vào báo cáo) |
|---|---|---|---|
| Đợt BC `MAU_21A` còn hiệu lực, có đơn vị `_04` trong phạm vi | ✅ **Có** (đợt #3 hoặc #4) | — | — |
| Bản ghi nộp của đơn vị `_04` ở `DANG_LAP` | ⚠️ **Phải kiểm** — nếu đang `CHUA_NOP` thì **phải dựng** | **[Lập báo cáo] trên GIAO DIỆN** (ưu tiên). API `POST /dot-bao-caos/{id}/start` được phép **CHỈ KHI** body **không** kèm `soLieuTongHop` — xem §4.4 | `DOT_BAO_CAO_DON_VI_NOP(đợt, đơn vị _04).trang_thai_nop`: `CHUA_NOP → DANG_LAP` · **tạo mới 1 bản ghi `BAO_CAO_CT_HTPL`** |
| Số liệu: 13 chỉ tiêu Biểu 21a có giá trị | ❌ **Phải dựng — và CHỈ BẰNG GIAO DIỆN** | 🔴 **UI ONLY** (§4.4) | `BAO_CAO_CT_HTPL.so_lieu_tong_hop` của chính bản ghi trên |
| Dấu nhận dạng lượt đo | — | Ô **Nhận xét, kiến nghị** (`:733` `nhan_xet`, max 5000; `:802` ghi rõ nó **không** tính vào điều kiện hoàn chỉnh) | Ghi chuỗi `QA-F8-340-<YYYYMMDD-HHmm>` |
| CB PD cùng đơn vị để đo C2 | ⚠️ **Phải xác minh** `donViId` (§3.1) | `GET /api/v1/auth/me` | — |
| Bấm [Trình duyệt KQ] | — | 🔴 **GIAO DIỆN THẬT** | Nếu đi lọt: BC `DU_THAO → CHO_PHE_DUYET`, đơn vị `DANG_LAP → CHO_DUYET`. **CB NV không tự hoàn tác được** — muốn quay lại phải để `cbpd_dp_04` [Từ chối] (`:1172` · `:1515`). **Không làm việc đó trong lô này** |

### 4.4 🔴 Ranh giới API / UI — **NGHIÊM NGẶT HƠN các phiếu khác của lô**

| Việc | Đường bắt buộc | Lý do |
|---|---|---|
| Đọc `/auth/me`, đọc danh sách đợt, đọc lại bản ghi, đọc `thong-baos`, đọc `audit-logs` | **API hoặc UI** | Đối chứng / kiểm kê, không phải hành vi tranh chấp |
| [Lập báo cáo] (đưa đơn vị về `DANG_LAP`) | **UI ưu tiên**; API `POST /{id}/start` được phép | Tiền đề (FR-XI-06) |
| 🔴 **Điền / lưu 13 chỉ tiêu số liệu** | 🔴 **CHỈ GIAO DIỆN** — **CẤM `PATCH /dot-bao-caos/{id}/bao-cao`, CẤM truyền `soLieuTongHop` trong `POST /{id}/start`** | **Đây chính là điểm hỏng đang mở (§0(b))**: câu hỏi của lượt này là *cán bộ có tự làm báo cáo hoàn chỉnh được bằng màn hình không*. Bơm 13 khóa bằng đường dữ liệu = **xóa sạch phép thử** ⇒ Pass oan. Lượt trước rơi đúng bẫy này (ô verify cũ tự khai đã "ép qua tiền đề bằng đường dữ liệu") |
| 🔴 **Bấm [Trình duyệt KQ] + [Đồng ý]** | 🔴 **GIAO DIỆN THẬT** | Hành động đang tranh chấp. Gọi thẳng `POST /{id}/submit-bc` ⇒ **verdict vô hiệu** |
| 🔴 **Bắt câu chữ thông báo** | Bộ bắt DOM cài **trước** thao tác, đọc `innerText` | C4 hỏi *"hệ thống **hiển thị**"* |
| 🔴 **`DOT_BAO_CAO.trang_thai`** | **KHÔNG ép bằng bất kỳ đường nào** | Chính là vế `C1b` GAP; không có chức năng hợp lệ nào sinh ra nó |

- Cấm đoán endpoint (`/api/docs-json` đọc được **không cần đăng nhập**), **cấm ghi thẳng DB**, cấm đụng dữ
  liệu đối tác. Mọi hành động chuyển trạng thái đòi `version` hiện tại ⇒ `GET` chi tiết ngay trước mỗi bước;
  **409 khóa lạc quan là xung đột kỹ thuật, KHÔNG phải bug nghiệp vụ**.

### 4.5 Đợt thay thế — theo thứ tự

| Ưu tiên | Phương án | Điều kiện dùng |
|---|---|---|
| **1** | `DOT-SO_BO_NAM-2026-1` (`e9909d96…`, `MAU_21A`, 83 đơn vị) | Đơn vị `_04` trong phạm vi **và** đang `CHUA_NOP`/`DANG_LAP` |
| **2** | `DOT-SO_BO_6_THANG-2026-1` (`a61e07f1…`, `MAU_21A`, 83 đơn vị) | Như trên — **đợt độc lập, cho lượt đo thứ hai** |
| 3 | Đổi cấp trong cùng vai trò: `cbnv_bn_04` (Bộ KH&ĐT) | ⚠️ Bộ KH&ĐT đang `CHO_DUYET` ở **cả hai** đợt 83-đơn-vị ⇒ **không ở `DANG_LAP`**, phải để `cbpd_bn_04` [Từ chối] trước — **thêm mutate, cân nhắc kỹ**. Khai rõ đây là biến thể §10 |
| 4 | `cbnv_tw_04` tạo đợt mới | `:625` chỉ TW tạo được · `:646` giữ phạm vi mặc định + **xác minh có đơn vị của `cbnv_dp_04`** · `:657` auto-sinh bản ghi `CHUA_NOP`. ⚠️ **Trùng kỳ + năm bị chặn là ĐÚNG SPEC** (`:656` · `:688` `ERR-XI-05a-02` *"Đã tồn tại đợt báo cáo cho kỳ '{ky}' năm {YYYY}"*) — **cả 3 kỳ của 2026 đã dùng** ⇒ phải chọn **năm khác** (đặt `tu_ngay`/`den_ngay` sang 2027). **Đừng log việc bị chặn thành bug** |

---

## 5. Đường đo từng vế

### 5.1 🔴 CỔNG TĐ-UI — làm báo cáo hoàn chỉnh **chỉ bằng giao diện** (quyết định verdict C1a)

```
[0] Vân tay bản dựng ĐẦU phiên: GET / → đọc assets/index-*.js + last-modified.  Ghi vào báo cáo.
[1] cbnv_dp_04 đăng nhập bằng GIAO DIỆN (mã 6 số ở MailHog).  GET /auth/me → ghi capDonVi + donViId + tên đơn vị.
[2] Menu "Đợt báo cáo" → mở chi tiết đợt ưu tiên 1 (§4.5) → đọc: trạng thái nộp của ĐƠN VỊ MÌNH, biểu mẫu
    đang áp dụng, đã có báo cáo chưa.  Lập bảng ghi lại TRƯỚC KHI ĐỘNG VÀO.
[3] Nếu đơn vị còn "Chưa nộp": bấm [Lập báo cáo] → [Đồng ý]  (đưa về "Đang lập").
[4] Trên biểu mẫu 21a: điền HAI ô nhập tay (cột -12 KP chi HĐ khác, cột -13 KP xã hội hóa) bằng số khác 0,
    khác nhau, dễ nhận (vd 1207 và 1308).  Ghi QA-F8-340-<YYYYMMDD-HHmm> vào ô Nhận xét, kiến nghị.
[5] Bấm [Lưu nháp].  TẢI LẠI TRANG BẰNG ĐỊA CHỈ.  Đọc lại màn: 13/13 dòng chỉ tiêu có giá trị nào?
[6] Nếu màn có nút [Làm mới]: bấm + xác nhận, quan sát 11 cột hệ thống có được nạp/ lưu không.
[7] CHỤP MÀN bảng 13 chỉ tiêu + ghi trạng thái đợt/đơn vị NGAY TRƯỚC KHI BẤM.
```

**Phán quyết của cổng — quyết cả C1a:**

| Quan sát ở [5]–[7] | Nghĩa | Đi tiếp thế nào |
|---|---|---|
| 13/13 chỉ tiêu có giá trị trong **dữ liệu đã lưu** (đọc lại bản ghi thấy đủ 13 khóa) | Tiền đề đạt bằng giao diện | Sang §5.2 đo C1a bình thường |
| Màn hiện đủ 13 giá trị nhưng **dữ liệu đã lưu thiếu** (như lượt trước: chỉ 3 khóa lạ / thiếu 11 khóa) | ⚠️ Chưa kết luận — vẫn **phải bấm** [Trình duyệt KQ] để xem máy chủ xử thế nào | Sang §5.2; nếu bị chặn ⇒ **FAIL C1a** theo `:802` + `:829` |
| Không có ô nhập nào cả / không lưu được gì | Chưa đủ dữ kiện | **⏸ Chưa chốt**, nêu rõ thiếu gì |

🔴 **CẤM tuyệt đối tại cổng này:** dùng `PATCH …/bao-cao` (hoặc `start` kèm `soLieuTongHop`) để bơm 13 khóa
rồi mới bấm giao diện. Làm thế là đo một hệ thống khác với hệ thống mà cán bộ dùng ⇒ **Pass oan** (§7.2 mục 1).

### 5.2 C1a — thao tác đi lọt + trạng thái chuyển

| | Nội dung |
|---|---|
| **Cài trước** | `toast-capture.js` (§5.5) — vì cùng một cú bấm còn phải thu C4 |
| **UI ngắn nhất** | [Trình duyệt KQ] → [Đồng ý]. Quan sát: thao tác có bị chặn không · nhãn trạng thái của **đơn vị mình** trên màn · thanh tiến trình. Tải lại trang bằng địa chỉ, đọc lại nhãn |
| **Đối chứng độc lập** | `GET /api/v1/dot-bao-caos/{id}` bằng phiên `cbnv_dp_04` **ngay sau** thao tác → `trang_thai` của **BÁO CÁO** = `CHO_PHE_DUYET` (`:1418`) **và** `trangThaiNop` của **đơn vị mình** = `CHO_DUYET` (`:1389`) |
| **Ghi kèm (không chấm)** | `trang_thai` cấp **ĐỢT** trước/sau — dữ liệu cho `C1b` |
| **Số liệu quyết định** | mốc giờ bấm · `baoCaoId` · `dotId` · 3 trục trạng thái trước/sau · mã lỗi + thông điệp nếu bị chặn · danh sách `chiTieuConThieu` nếu có |

**Bấm lại cùng nút KHÔNG tính là đường thứ hai.** Hai đường khớp ⇒ **DỪNG**. Mâu thuẫn ⇒ **⏸ Chưa chốt**.

### 5.3 C2 — thông báo tới CB PD cùng đơn vị

| | Nội dung |
|---|---|
| **Điều kiện** | `cbpd_dp_04` **đã xác minh trùng `donViId`** với `cbnv_dp_04` (§3.1). Lệch ⇒ đổi cặp theo Rule 7, khai rõ |
| **UI ngắn nhất** | Đăng nhập `cbpd_dp_04` → chuông / màn Thông báo → có mục về báo cáo vừa trình, mốc giờ khớp lượt bấm ở §5.2 |
| **Đối chứng độc lập** | `GET /api/v1/thong-baos` bằng **token riêng của chính `cbpd_dp_04`** (lược đồ: *"Chỉ trả về thông báo có `nguoiNhanId` trùng người đăng nhập"*; lọc `tuNgay`/`denNgay` quanh mốc bấm) → so `createdAt` |
| **Thứ tự** | Đo **SAU CÙNG** — đổi tài khoản trên trình duyệt dùng chung sẽ giết phiên `cbnv_dp_04`. Gọn hơn: lấy token API riêng cho `cbpd_dp_04`, giữ nguyên phiên giao diện |
| **Không chấm** | Hệ thống có gửi thêm cho ai khác không — `:804` chỉ ghi *"Gửi thông báo CB PD"*, **im lặng về việc giới hạn người nhận** ⇒ ngoài vế |

### 5.4 C3 — lưu vết thao tác

| | Nội dung |
|---|---|
| **Đường 1** | `GET /api/v1/audit-logs?hanhDong=SUBMIT&tuNgay=<mốc-5phút>&denNgay=<mốc+5phút>&sort=thoiGian&order=desc` bằng **chính phiên `cbnv_dp_04`** (lược đồ: *"TW xem tất cả, ngoài TW chỉ xem bản ghi của chính mình"*). 🔴 **Đọc** `entityType` / `entityId` / `thoiGian` / `nguoiThucHien` **từ phản hồi** — **cấm đoán trước** giá trị `entityType` |
| **Đối chứng độc lập** | Màn **Nhật ký hệ thống** của QTHT hiển thị đúng dòng đó (khai rõ tài khoản đọc log; **không** dùng ra verdict vế khác). Nếu CB NV vào được màn nhật ký thì đảo lại: UI trước, API sau |
| **Nối được với UI** | `entityId` phải khớp `baoCaoId`/`dotId` của lượt bấm, `thoiGian` khớp mốc giờ. Không nối được ⇒ **⏸ Chưa chốt**, không FAIL |
| **Nếu tài khoản thiếu quyền đọc log** | Đó là **blocker vận hành**, không phải bug: ghi ⏸ cho riêng C3, nêu cần cấp quyền đọc `AuditLog` hoặc cấp tài khoản QTHT |

### 5.5 C4 — câu chữ thông báo thành công *(đo để ghi nhận, KHÔNG chấm)*

- **Bộ bắt thông báo:** [`../../../tools/toast-capture.js`](../../../tools/toast-capture.js) — **file có thật**,
  đã kiểm. Dán nguyên khối vào `evaluate_script` **TRƯỚC** khi bấm.
- Ràng buộc của chính file đó: **CẤM lọc trùng** · đọc bằng **`innerText`** (không `textContent` — gom node
  ẩn AntD ⇒ **bug ma**) · cài lại phải **idempotent** · **`soObserverDangSong` PHẢI = 1**, khác 1 ⇒ **số liệu
  vô hiệu** · đếm kèm **số yêu cầu gửi đi** để phân biệt "gửi 2 lần" với "1 lần hiện 2 thông báo".
- **Đối chứng:** chuỗi `message` trong phản hồi máy chủ của **chính lượt bấm đó**.
- **Đếm theo mốc giờ KHÁC NHAU, không theo độ dài mảng.** *(Tiền lệ lô F5: 1 thông báo sinh 2 nút DOM
  `ant-message` khung + `ant-message-notice-wrapper` con, lệch ~1 ms ⇒ vẫn là **1**.)*
- 🔴 Đo xong ghi `WEB HIỆN TẠI: …` — **không viết PASS/FAIL cho C4** (GAP, luật khóa 5).

### 5.6 Kết phiên

Đo lại **vân tay bản dựng CUỐI phiên** (`GET /` → `assets/index-*.js` + `last-modified`). Lệch với đầu phiên
⇒ nói rõ quan sát nào rơi trước/sau mốc triển khai. **Nhãn `V1.0.x` ở chân thanh bên KHÔNG phải định danh.**

---

## 6. ✅ PASS khi / ❌ FAIL nếu / ⏸ CHƯA CHỐT khi

```
✅ ĐẠT (mức cao nhất của phiếu này = "Cần BA", KHÔNG phải Pass) khi đủ cả 3 vế MATCH,
   trên ≥1 lượt bấm THỰC HIỆN MỚI bằng giao diện, tiền đề dựng UI-ONLY theo §5.1:
   (C1a) Báo cáo đã hoàn chỉnh theo :802 → bấm [Trình duyệt KQ] → thao tác KHÔNG bị chặn;
         nhãn trạng thái của ĐƠN VỊ MÌNH chuyển sang "Chờ duyệt kết quả" và GIỮ NGUYÊN sau khi
         tải lại trang bằng địa chỉ; đọc lại bản ghi thấy BC = CHO_PHE_DUYET và trangThaiNop = CHO_DUYET.
   (C2)  cbpd_dp_04 (ĐÃ xác minh cùng donViId) nhận được thông báo về chính báo cáo đó, mốc giờ khớp;
         xác nhận bằng cả màn Thông báo lẫn danh sách thông báo cá nhân của chính tài khoản đó.
   (C3)  Có bản ghi nhật ký ứng với thao tác trình, nối được với baoCaoId/dotId + mốc giờ của lượt bấm.
   ⇒ Kết quả logic: 📌 CẦN BA XÁC NHẬN  (vì C1b + C4 vẫn là GAP — xem §8).

❌ FAIL (⇒ 📌 CÒN LỖI (REOPEN) + CẦN BA XÁC NHẬN) nếu bất kỳ điều nào:
   - Báo cáo đã có giá trị ở TOÀN BỘ chỉ tiêu bắt buộc (kể cả toàn bộ bằng 0) mà thao tác vẫn BỊ CHẶN
     với thông báo "còn thiếu"  → AC :829 không đạt được bằng thao tác trên màn;
   - HOẶC thao tác đi lọt nhưng đọc lại bản ghi thấy BÁO CÁO vẫn DU_THAO / đơn vị vẫn DANG_LAP
     (đúng triệu chứng gốc của đối tác);
   - HOẶC trình thành công nhưng CB PD cùng đơn vị KHÔNG nhận được thông báo nào (cả 2 đường đều rỗng);
   - HOẶC trình thành công nhưng KHÔNG có bản ghi nhật ký nào nối được với thao tác;
   - HOẶC hai đường đo mâu thuẫn nhau ở cùng một vế → xem ⏸ bên dưới.

⏸ CHƯA CHỐT khi:
   - Không xác minh được cặp cbnv_dp_04 ↔ cbpd_dp_04 cùng đơn vị, và không có cặp thay thế cùng vai trò+cấp;
   - HOẶC đơn vị của _04 không nằm trong phạm vi bất kỳ đợt MAU_21A nào và không dựng nổi đợt mới;
   - HOẶC không có quyền/không có màn đọc nhật ký (riêng C3 ⏸, các vế khác vẫn chốt được);
   - HOẶC hai phép đo mâu thuẫn (màn báo thành công nhưng bản ghi không đổi, hoặc ngược lại) → ghi CẢ HAI, hỏi user.
```

**Ca gộp nhiều vế (flow 04 §Ca biên):** còn ≥1 vế `MATCH` sai **và** có vế `GAP` ⇒ kết quả logic là
**`Reopen + cần BA`**, nêu riêng vế lỗi và câu hỏi BA. Không vế nào Reopen mà còn `GAP` ⇒ **`Cần BA`**.

---

## 7. Cạm bẫy — rút thẳng từ ô verify cũ

### 7.1 ⚠️ Bẫy chống **FAIL oan**

1. 🔴 **FAIL vì "11 chỉ tiêu không có ô nhập".** §1.2 — `srs-v3.5.md:6678`–`:6688` quy định cột -1→-11 do hệ
   thống tính; **chỉ -12, -13 (`:6689`, `:6690`) là "Nhập thủ công"**. Màn làm đúng. **Đây là bẫy nguy hiểm
   nhất chiều FAIL, và lượt trước đã suýt rơi vào** (wording cũ đề nghị theo hướng cho cán bộ nhập tay 11 cột).
2. 🔴 **FAIL vì trạng thái ĐỢT vẫn `TAO_DOT`.** Đây là vế `C1b` **GAP** (§1.1) — đặc tả tự mâu thuẫn
   (`:1512` vs `:739`–`:747`; `:1368` một giá trị vs `:1367`/`:1398` ~70–83 đơn vị). **CẤM lấy làm lý do FAIL.**
3. **Nhãn nút khác phiếu.** Phiếu ghi *"Trình phê duyệt"*, giao diện hiện **[Trình duyệt KQ]** — `:1170` khai
   đúng chữ giao diện. Phiếu **không nhắc nhãn nút** ⇒ **cấm FAIL vì nhãn**.
4. **Nhãn trạng thái khác chữ trong phiếu.** Bảng nhãn `:1195` = `Dang lap BC`, `:1196` = `Cho duyet KQ`;
   phiếu viết "Đang lập báo cáo" / "Chờ duyệt kết quả". Phiếu **không đòi chuỗi nhãn** ⇒ **cấm FAIL vì câu chữ nhãn**.
5. **Mã lỗi lệch `ERR-XI-07-01`.** Phiếu 340 **không nhắc mã lỗi, cũng không nhắc câu chữ lỗi** ⇒ ngoài vế.
   Ghi nhận ở §9, **không kéo verdict**.
6. **`nhan_xet` bỏ trống · giá trị `0`.** `:802` ghi rõ `nhan_xet` **không** tính, và `0` **là đã điền**.
7. **404 khi mở đợt / bảng `tienDo` rỗng với tài khoản ĐP.** Là **phân quyền đúng thiết kế** (phạm vi đơn vị
   nộp `:717`/`:1367`), **không phải "mất bản ghi"**.
8. **409 khóa lạc quan** do `version` cũ · **429 rate-limit đăng nhập** (5 lượt/60 giây) — **xung đột kỹ thuật**,
   không phải bug nghiệp vụ.
9. **Bấm bằng CB Phê duyệt hoặc tài khoản cấp TW rồi bị chặn** = đúng `:784` + `:712` ⇒ cấm log.

### 7.2 ⚠️ Bẫy chống **PASS oan** *(mục 1 là bẫy nguy hiểm nhất của phiếu này)*

1. 🔴 **Bơm 13 chỉ tiêu bằng đường dữ liệu rồi bấm giao diện → PASS.** Chính lượt trước đã làm việc này để đo
   được C2/C3 ("QA đã ép qua tiền đề bằng đường dữ liệu"). Nếu lượt này lặp lại rồi chấm đạt, ta **chứng minh
   một thứ khác** với thứ cán bộ gặp: cán bộ không có đường dữ liệu. ⇒ **Tiền đề PHẢI dựng UI-ONLY (§4.4, §5.1).**
   *Nếu cổng §5.1 vẫn chặn:* được phép đo tiếp C2/C3/C4 trên bản ghi đã ép qua bằng đường dữ liệu, **nhưng
   bắt buộc ghi câu giới hạn**: *"chỉ chứng minh hành vi SAU KHI thao tác trình đã đi lọt; KHÔNG chứng minh
   cán bộ tự trình được bằng giao diện"* — và **C1a vẫn FAIL**.
2. 🔴 **Chấm bằng quan sát tĩnh.** *"Thấy nút [Trình duyệt KQ] đã bấm được"*, *"màn trông đúng"* — flow 04
   **CẤM Pass bằng quan sát tĩnh** khi vế bug là hành động.
3. 🔴 **Không đọc lại bản ghi sau thao tác.** Triệu chứng gốc của đối tác **chính là** "báo thành công nhưng
   trạng thái không đổi" ⇒ **bắt buộc** đọc lại 3 trục trạng thái. Bỏ bước này là bỏ đúng vế của phiếu.
4. **Chấm bằng phản hồi máy chủ thay cho màn hình (C4).** C4 hỏi *"hiển thị"*; có 200 mà không thông báo gì
   hiện lên ⇒ ghi đúng như vậy, không suy ra "đã hiển thị".
5. **Đọc chữ bằng `textContent`** → gom node ẩn AntD ⇒ pass ma / bug ma. Dùng `innerText`.
6. **Bộ bắt thông báo lọc trùng · cài chồng nhiều lần.** `soObserverDangSong ≠ 1` ⇒ **số liệu vô hiệu**
   (tiền lệ Reopen oan `BUG-FE-TOAST-LAP`). Đếm theo **mốc giờ khác nhau**, không theo độ dài mảng.
7. **Đếm thông báo của C2 bằng tài khoản khác.** `/thong-baos` chỉ trả thông báo của **người đăng nhập** ⇒
   đọc bằng `admin`/`cbnv` sẽ **không thấy** thông báo của CB PD — dễ kết luận nhầm "không gửi".
   Ngược lại: chưa xác minh `donViId` mà thấy có thông báo ⇒ chưa chứng minh được **"cùng đơn vị"**.
8. **Dùng lại bản ghi mà lượt trước đã tác động** (Sở Tư pháp Hà Nội trong `DOT-SO_BO_NAM-2026-1`, đã
   `DA_NOP`/`DA_GUI_TW`): dữ liệu đóng băng trước lần triển khai mới ⇒ **không phân biệt được** hành vi cũ
   với hành vi cần đạt. **Dùng bản ghi MỚI của đơn vị `_04`.**
9. **Tab mở lâu chạy bó mã cũ.** Tải lại trang **bằng địa chỉ** + đọc tên bó mã `assets/index-*.js` ở **đầu VÀ
   cuối** phiên. Prompt báo bản mới `index-BbPPdate.js` (07/08 13:47) — **phải tự xác minh, không bê nguyên**.
10. **Kết luận trên env khác.** Đo trên env **nội bộ** `https://18.143.165.120.nip.io`; đối tác nghiệm thu
    trên `htpldn-uat.ospgroup.vn` ⇒ **bắt buộc câu giới hạn hiệu lực** trong kết quả.
11. **Viết *"fix đã có tác dụng"*.** Ta có triệu chứng cũ của đối tác + phép đo cũ của QA, nhưng **không có
    ảnh lỗi gốc của chính mình trên bản dựng cũ cho đúng bản ghi mới** ⇒ chỉ được kết luận **hiện trạng
    đúng/sai so với đặc tả** (flow 04 §Ca biên).

---

## 8. Câu hỏi BA — 2 vế GAP, mỗi câu chốt đúng một quyết định

| # | Vế | Expected đối tác ↔ SRS `file:dòng` | Câu hỏi (một quyết định) | Trạng thái |
|---|---|---|---|---|
| **Q-A** | **C1b** | Đối tác kỳ vọng *"Chuyển trạng thái **đợt báo cáo**: Đang lập báo cáo → Chờ duyệt kết quả"*. SRS: `:803`/`:814`/`:818`/`:1513` bắt **`DOT_BAO_CAO`** đổi trạng thái, `:789` còn đòi đợt **đã ở** `DANG_LAP_BC`; **nhưng** `:1512` giao bước `TAO_DOT → DANG_LAP_BC` cho FR-XI-06, mà Processing FR-XI-06 `:739`–`:747` (`:746`) **chỉ** đổi `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop`; và `:1368` cho đợt **một** giá trị trong khi phạm vi đợt là ~70–83 đơn vị (`:1367` · `:1398` · `:646`) | **Vòng đời SM-DOT-BC gắn vào bản ghi ĐỢT hay bản ghi NỘP CỦA TỪNG ĐƠN VỊ?** (Nếu là ĐỢT: chức năng nào đưa đợt từ `TAO_DOT` sang `DANG_LAP_BC`, và đợt xử lý ra sao khi 83 đơn vị đang ở các bước khác nhau?) | 🔗 **CÙNG GỐC với Q1 đã mở** (phiếu 343 · C2; bàn giao lô F5 §3 Nhóm 2) ⇒ **liên kết, KHÔNG mở câu trùng**. Phần mới cần bổ sung vào Q1: nhánh **FR-XI-07** và mâu thuẫn `:789` ↔ `:1512`/`:746` |
| **Q-B** | **C4** | Đối tác kỳ vọng *"Trình thành công, hệ thống hiển thị **«Đã trình phê duyệt báo cáo»**"*. SRS **IM LẶNG**: FR-XI-07 Outputs `:810`–`:814` không có thông báo · Postconditions `:816`–`:819` chỉ có trạng thái + TB cho CB PD · Error Handling `:821`–`:825` **chỉ có E1 lỗi** · `:1170` **không** ghi toast (đối chiếu `:1173` của FR-XI-08 **có** ghi `Toast success`) · không có mã `INF-XI-07-*` trong toàn thư mục `srs-v3.5/` | **Khi trình phê duyệt thành công, hệ thống có phải hiển thị thông báo cho người trình không — và nếu có thì câu chữ chốt là gì** (đề nghị bổ sung một dòng `INF-XI-07-…` vào bảng thông báo của FR-XI-07)? | **Mới**. 🔴 Mục đích là **bổ sung đặc tả**, KHÔNG phải chặn bàn giao. Nếu đo được web hiển thị đúng chuỗi đối tác chờ ⇒ ghi rõ *"web hiện tại đúng kỳ vọng đối tác"* trong tóm tắt |

**Cổng hỏi BA đã qua:** đã mở đúng SRS trong chính case, đã đọc trọn FR-XI-07 + FR-XI-06 + FR-XI-05a + khối
màn + entity + SM + BR (§1.3), và vẫn còn GAP. Không hỏi từ mô tả/web/note cũ.

---

## 9. Ghi nhận (KHÔNG chấm) — gửi dev/BA, không mở dòng bug mới

1. **Mã lỗi lệch đặc tả** — `:825` khai `ERR-XI-07-01`, hệ thống trả `ERR-VAL-XI-07-02` (câu chữ thì khớp
   nguyên văn `:825`). Phiếu 340 không nhắc mã lỗi ⇒ **ngoài vế**. 🔗 **Đã có ở bàn giao lô F5 §4 mục 2 —
   liên kết, không mở mục trùng.**
2. **Đặc tả tự căng về ai điền 11 cột hệ thống** — `:731` cho `so_lieu` nguồn *"Nhập tay / Auto"*, `:744`
   viết *"CB NV nhập/chỉnh sửa số liệu"*; trong khi `srs-v3.5.md:6678`–`:6688` giao cột -1→-11 cho hệ thống
   tính và chỉ `:6689`/`:6690` là *"Nhập thủ công"*. **Không phải vế của phiếu** ⇒ ghi nhận, **không hỏi BA
   riêng, không chấm**. *(Nếu BA trả lời Q-A/Q-B thì tiện thể nêu.)*
3. **Ba khóa lạ trong dữ liệu đã lưu** — `soVuViec` · `tongChiPhi` · `soDnDuocHoTro` không thuộc bộ 13 cột
   Biểu 21a (`:6678`–`:6690`) và không dòng nào trên bảng 13 chỉ tiêu hiển thị chúng. Ghi nhận, **không điều tra**.
4. **Bản ghi `c19b1bc2…` (Bộ KH&ĐT) đã ở `CHO_PHE_DUYET` với chỉ 3 khóa** — tức đã qua `submit-bc` trước khi
   luật kiểm 13 chỉ tiêu có hiệu lực. Manh mối, **không điều tra trong lô này**.

---

## 10. Độ phủ biến thể — **sàn N = 1**

| # | Dạng | Cách dựng | Bắt buộc? |
|---|---|---|---|
| **①** | CB NV **ĐP** trên đợt `MAU_21A` (đợt ưu tiên 1 §4.5) | `cbnv_dp_04` + `cbpd_dp_04` | **BẮT BUỘC** |
| ② | CB NV **ĐP** trên đợt `MAU_21A` thứ hai (đợt ưu tiên 2) | như trên | Chỉ khi ① rơi ⏸ vì lý do riêng của bản ghi |
| ③ | CB NV **BN** | `cbnv_bn_04` + `cbpd_bn_04` | Chỉ khi ①/② không dựng được; **khai rõ là biến thể** (`:712` cho phép cả ĐP lẫn BN) |

**KHÔNG mở rộng:** không đo nhánh "báo cáo **chưa** đầy đủ → bị chặn" (đó là **dòng 341**, phiếu khác — file
[`TPDBCKQTHCT_02.md`](TPDBCKQTHCT_02.md)) · không đo nhánh [Phê duyệt]/[Từ chối] của CB PD (FR-XI-07a
`:834`–`:903`) · không đo `MAU_21B`/`CA_HAI` nếu đợt đang dùng `MAU_21A` — **phiếu không nhắc biểu mẫu** ·
không đo [Gửi TW] (FR-XI-08).

---

## 11. Rủi ro verdict **Chưa chốt**

| Rủi ro | Xác suất | Cần bổ sung gì mới chốt được |
|---|---|---|
| `cbnv_dp_04` ↔ `cbpd_dp_04` **khác đơn vị** ⇒ không đo được C2 | **Trung bình** — chưa ai đọc được danh tính bộ `_04` cấp ĐP | Rule 7: đổi sang cặp cùng vai trò + cùng cấp (`_05`, rồi `_03` = An Giang đã xác minh), **khai rõ lý do lệch prompt** |
| Đơn vị của `_04` **ngoài phạm vi** mọi đợt `MAU_21A` | Thấp — 2 đợt phủ **83 đơn vị**, còn 80/81 ô `CHUA_NOP` | Đợt mới bằng `cbnv_tw_04`, **năm khác 2026** để né `:656`/`:688` |
| Giao diện **không cho lưu** hai ô -12/-13, hoặc không có ô nhập nào | Thấp (lượt trước nhập được `1207`/`1308`) | Ghi ⏸ + nêu rõ; **không** vá bằng đường dữ liệu (§4.4) |
| Không có quyền/không có màn đọc **nhật ký** ⇒ riêng C3 | Trung bình | Blocker vận hành: xin quyền đọc `AuditLog` hoặc tài khoản QTHT. Các vế khác vẫn chốt được |
| Máy chủ vẫn chặn dù 13/13 chỉ tiêu có giá trị | **Trung bình–cao** (điểm hỏng lượt trước) | **Không phải ⏸ — đây là FAIL C1a**, đủ căn cứ Reopen kèm khối `CÁCH VERIFY` |

> **Kết luận rủi ro:** tiền đề rẻ và **đo lại được nhiều lượt nếu bị chặn** (bị chặn ⇒ dữ liệu không đổi).
> Nhưng **nếu trình đi lọt thì tiền đề bị tiêu** (BC sang `CHO_PHE_DUYET`, CB NV không tự hoàn tác được)
> ⇒ **thu đủ bằng chứng C1a/C3/C4 trong CHÍNH lượt bấm đầu tiên**; C2 đo ngay sau, bằng token riêng.
> Muốn lượt hai: dùng đợt ưu tiên 2 (§4.5) với **cùng** đơn vị `_04`.
