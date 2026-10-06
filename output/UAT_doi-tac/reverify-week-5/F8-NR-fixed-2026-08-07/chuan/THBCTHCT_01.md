# Chuẩn chấm đã khóa — THBCTHCT_01 (dòng 343) — "Tổng hợp báo cáo từ nhiều đơn vị → Lưu tổng hợp"

> **Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> (1.610 dòng). **Mọi số dòng dưới đây do agent này tự mở file đếm lại ngày 2026-08-07.**
>
> **Trạng thái phiếu:** đối tác **CHƯA TỪNG CHẠY** — `Trạng thái` (N) = `N/R`, `Kết quả thực tế` (L) RỖNG,
> không ảnh ⇒ **`expected đối tác` = nguyên văn cột `Kết quả mong đợi` (K)**.
> Ô `TKM phản hồi lần 1` (Q343) ghi: *"Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi"* — tức bên nghiệm thu
> **bị chặn ở luồng thượng nguồn**, chưa từng đo được phiếu này. Lô F5 đã đo `GKQTHCTHTPL_01` (dòng 342):
> lỗi "Forbidden" **đã hết**, gửi TW chạy trót lọt ⇒ **luồng thượng nguồn nay đi được**, tiền đề dựng được.
>
> **Tác nhân (F343):** Cán bộ nghiệp vụ TW. **Điều kiện (H343):** *"NSD là cán bộ nghiệp vụ cấp Trung ương
> và có ít nhất một báo cáo từ Bộ/Ngành hoặc Địa phương đã gửi lên."*

**Expected đối tác (nguyên văn K343):**
```
- Lưu bản ghi báo cáo tổng hợp toàn quốc.
+ Chuyển trạng thái các đợt báo cáo đã chọn: Đã gửi Trung ương → Đã tổng hợp.
+ Lưu vết thao tác theo quy định.
- Tổng hợp thành công, hệ thống hiển thị thông báo "Đã tổng hợp báo cáo toàn quốc".
```

---

## 1. BẢNG SCOPE LOCK — 4 vế

| Vế | Expected đối tác (nguyên văn) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|---|
| **C1** | "Lưu bản ghi **báo cáo tổng hợp toàn quốc**" | **`:1004`** (chính) · `:1016` · `:1021` · `:1038` · `:1175` | `:1004` = `\| 6 \| Lưu bản ghi BC tổng hợp toàn quốc (loại TONG_HOP_TW) \| — \|` | **MATCH** | **TEST** | **UI:** `cbnv_tw_03` bấm [Lưu] của khối Tổng hợp → thao tác đi lọt. **Đối chứng độc lập:** mở lại màn tổng hợp **sau khi tải lại trang bằng địa chỉ** → bản ghi tổng hợp đọc lại được với đúng số liệu vừa lưu (bản ghi tồn tại ở máy chủ, không chỉ trong phiên) |
| **C2** | "Chuyển trạng thái **các đợt báo cáo đã chọn: Đã gửi Trung ương → Đã tổng hợp**" | `:1005` · `:1022` · `:1010` · `:1517` · `:993` · `:1368` · `:1389` · `:1398` · `:646` · nhãn `:1198`,`:1199` | `:1005` = `\| 7 \| Chuyển các đợt BC đã chọn sang DA_TONG_HOP \| SM-DOT-BC \|` · `:993` = `\| 1 \| bao_cao_ids \| identifier[] \| Y \| FK → BAO_CAO_CT_HTPL, da_gui_tw = true \| — \| Checkbox chọn \|` | **GAP** — đặc tả **tự mâu thuẫn** (§2) | **BA** | **CẤM Pass/Reopen vế này.** Chỉ **ghi nhận hiện trạng**: nhãn trạng thái trên màn của **cả TW lẫn đơn vị đã nộp**, + giá trị đọc lại được ở **cả hai trục** (đợt / đơn vị) trước và sau thao tác |
| **C3** | "**Lưu vết thao tác** theo quy định" | **`:1007`** (chính) · `:1532` · `:1568` | `:1007` = `\| 9 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` | **MATCH** | **TEST** | Màn Nhật ký hệ thống (vai trò QTHT) lọc quanh mốc giờ bấm [Lưu] → có mục ứng với thao tác của đúng tài khoản `cbnv_tw_03`, đúng mốc giờ |
| **C4** | "hệ thống hiển thị thông báo **«Đã tổng hợp báo cáo toàn quốc»**" | **`:1032`** (chính) | `:1032` = `\| I1 \| Tổng hợp thành công \| INF-XI-09-01 \| "Đã tổng hợp báo cáo toàn quốc" \| INFO \|` | **MATCH** (kể cả câu chữ) | **TEST** | Bộ bắt thông báo cài **TRƯỚC** khi bấm, **CẤM lọc trùng**, đọc `innerText`. **Đối chứng độc lập:** phản hồi máy chủ của chính lượt bấm đó |

> **C4 là ca hiếm:** SRS **có** khai nguyên văn câu chữ (`:1032`, mã `INF-XI-09-01`) ⇒ **chấm được cả chuỗi**.
> Khác hẳn FR-XI-07 (im lặng về thông báo thành công) và FR-XI-08 (chỉ khai *"Toast success"* ở `:1173`,
> im lặng về câu chữ) — hai chỗ đó lô F5 phải để GAP.

### 1.1 Căn cứ khẳng định đã đọc trọn mục (không phải grep rỗng)

Đã đọc trọn FR-XI-09 `:971`–`:1038`: Mô tả `:980`, Tác nhân `:982`, Preconditions `:984`–`:987`,
Inputs `:989`–`:993`, Processing `:995`–`:1007` (9 bước), Business Rules `:1009`–`:1010`,
Outputs `:1012`–`:1017`, Postconditions `:1019`–`:1023`, Error Handling `:1025`–`:1032`, AC `:1034`–`:1038`.
Đọc trọn khối SCR "Chi tiet Dot BC" `:1161`–`:1175` (dòng #35–#45), bảng nhãn SM-DOT-BC `:1190`–`:1199`,
entity `DOT_BAO_CAO` `:1350`–`:1377`, `DOT_BAO_CAO_DON_VI_NOP` `:1379`–`:1398`, `BAO_CAO_CT_HTPL`
`:1400`–`:1422`, máy trạng thái SM-DOT-BC `:1491`–`:1517`, BR-FLOW-08 `:1600`–`:1606`.
Đã soát dấu thay đổi `[STT 52 UAT 2026-05-26]` (`:612`, `:701`, `:938`, `:1350`, `:1379`, `:1400`) và
`[BA-23 tuan 4]` (`:1103`, `:1149`, `:1155`).

---

## 2. 🔴 Vì sao C2 là `GAP` — bằng chứng tự mâu thuẫn trong chính bản SRS này

**Yêu cầu bị khóa hai bậc, hai bậc chọi nhau:**

| # | Dòng SRS | Nội dung | Nói lên điều gì |
|---|---|---|---|
| a | `:1005` | `\| 7 \| Chuyển các đợt BC đã chọn sang DA_TONG_HOP \| SM-DOT-BC \|` | Đổi trạng thái ở **trục ĐỢT** |
| b | `:1517` | `\| DA_GUI_TW \| DA_TONG_HOP \| TW tổng hợp \| CB NV TW xác nhận \| Tạo BC tổng hợp \| FR-XI-09 \| — \|` | Chuyển tiếp hợp lệ **chỉ có ở trục ĐỢT** |
| c | `:1368` | `\| 11 \| trang_thai \| text \| Y \| CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP') \| 'TAO_DOT' \| Trạng thái lifecycle (SM-DOT-BC: 6 states) \|` | Đợt chỉ có **MỘT** giá trị trạng thái |
| d | `:1367` · `:646` · `:1398` | `:1367` = phạm vi `pham_vi_don_vi_nop_ids[]` mặc định *"Toàn bộ ĐP + BN"* (63 ĐP + BN); `:1398` = `**Volume:** ~3 đợt/năm × ~70 đơn vị (63 ĐP + ~7 BN) = ~210 records/năm` | Một đợt dùng chung cho **~70–83 đơn vị** |
| e | `:993` | Đầu vào của FR-XI-09 là `bao_cao_ids[]` — **chọn BÁO CÁO** (mỗi báo cáo thuộc 1 đơn vị), **không** chọn đợt | Cụm chữ *"các đợt BC đã chọn"* ở `:1005` **không khớp** với thứ người dùng thực sự chọn |
| f | `:1389` | `\| 3 \| trang_thai_nop \| text \| Y \| CHECK IN ('CHUA_NOP','DANG_LAP','CHO_DUYET','DA_DUYET','DA_NOP','QUA_HAN') \| 'CHUA_NOP' \| …` | Trục ĐƠN VỊ **KHÔNG có** giá trị `DA_TONG_HOP` |
| g | `:937` vs `:938` | `:937` bắt đổi trạng thái **ĐỢT** khi gửi TW; `:938` (`[STT 52 UAT 2026-05-26]`) quy định chính việc đó ở cấp **ĐƠN VỊ** (`trang_thai_nop = DA_NOP` + `ngay_nop`) | Cùng một hành vi được khai ở hai bậc |

**Hệ quả:** không xác định được chuẩn chấm.
- Đọc theo bậc **ĐỢT** (a+b+c): tổng hợp 2 đơn vị trong một đợt 83 đơn vị sẽ đánh dấu **cả đợt** là "Đã tổng
  hợp" trong khi 81 đơn vị chưa nộp — và tiền trạng thái `DA_GUI_TW` của đợt, theo phép đo lô F5, **không
  bao giờ đạt được** (đợt đứng yên `TAO_DOT`, `daGuiTw = false`, nhãn người dùng thấy suy từ trục đơn vị).
- Đọc theo bậc **ĐƠN VỊ** (f+g): **không tồn tại** giá trị `DA_TONG_HOP` để chuyển sang.

⇒ Flow 04, bảng "Đối chiếu đặc tả", dòng *"Im lặng hoặc tự mâu thuẫn"*: **không Pass/Reopen vế này; kết luận
Cần BA**. Kết quả đo trên web **không** biến `GAP` thành `MATCH` (luật khóa 5).

> ⚠️ **Kể cả khi web làm ĐÚNG Y NGUYÊN kỳ vọng đối tác** (đợt đã chọn nhảy sang "Đã tổng hợp") ⇒ vẫn **KHÔNG
> Pass** vế C2. Nhưng phần tóm tắt phải nói rõ *"web hiện tại đúng kỳ vọng đối tác"* để người ngoài không đọc
> nhầm thành lỗi chưa xử lý; câu hỏi BA khi đó nhằm **bổ sung/đính chính đặc tả**, không phải chặn bàn giao.

### 2.1 Câu hỏi BA cho vế C2 (bắt buộc có trong kết quả)

> **CẦN BA CONFIRM:** đối tác kỳ vọng *"chuyển trạng thái **các đợt báo cáo đã chọn**: Đã gửi Trung ương →
> Đã tổng hợp"*; SRS quy định điều đó ở **trục ĐỢT** (`srs-fr-15-ct-htpldn.md:1005`, `:1022`, `:1517`) nhưng
> **tự mâu thuẫn**: đầu vào của chính chức năng là **danh sách BÁO CÁO theo đơn vị** (`:993`), một đợt chỉ có
> **một** giá trị trạng thái (`:1368`) trong khi phạm vi đợt là **~70–83 đơn vị** (`:1367`, `:1398`), còn trục
> đơn vị (`:1389`) **không có** giá trị `DA_TONG_HOP`; đồng thời `:937` và `:938` khai cùng một hành vi ở hai
> bậc khác nhau. Web/dev hiện tại **<điền sau khi đo: nhãn TW thấy · nhãn đơn vị thấy · giá trị đọc lại được
> ở cả hai trục>**.
>
> **Câu hỏi BA:** sau khi TW lưu tổng hợp, **cái gì** phải chuyển sang "Đã tổng hợp" — (a) **cả đợt** (kể cả
> khi mới tổng hợp một phần số đơn vị), (b) **từng bản ghi nộp của đơn vị đã được chọn** (khi đó xin bổ sung
> giá trị `DA_TONG_HOP` vào `:1389`), hay (c) **bản ghi báo cáo tổng hợp TW** là nơi duy nhất mang trạng thái
> này? Và trạng thái cán bộ nhìn thấy ở chi tiết đợt là của **đơn vị mình** hay của **đợt**?
>
> *(Cùng gốc với câu hỏi đã gửi ở bàn giao lô F5 §3 Nhóm 2 — **liên kết, không mở câu hỏi trùng**; phần bổ
> sung mới của phiếu này là bước `DA_GUI_TW → DA_TONG_HOP` và mâu thuẫn "chọn báo cáo nhưng đổi trạng thái
> đợt".)*

---

## 3. Tiền đề tối thiểu — phần khó nhất của phiếu

### 3.1 Tài khoản

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| 🔴 **Người ra verdict** — CB Nghiệp vụ cấp **TW** | **`cbnv_tw_03`** · `Test@1234` | **Bấm [Tổng hợp] + [Lưu] bằng giao diện thật** — tài khoản chốt PASS/FAIL. `:982` Tác nhân = *"Cán bộ Nghiệp vụ TW"*; `:986` *"User thuộc cấp TW"* |
| Dựng tiền đề đơn vị #1 | `cbnv_dp_03` + `cbpd_dp_03` (**phải cùng `donViId`**) · `Test@1234` | Lập → trình → duyệt → gửi TW cho một đơn vị ĐP |
| Dựng tiền đề đơn vị #2 | `cbnv_bn_03` + `cbpd_bn_03` (**phải cùng `donViId`**) · `Test@1234` | Nhánh Bộ/Ngành — `:1604` BR-FLOW-08 *"ĐP/BN gửi BC đã duyệt lên TW"* |
| Đọc nhật ký (C3) | tài khoản QTHT (hoặc `admin` **chỉ để đọc log**, khai rõ) | Không dùng ra verdict |
| **CẤM ra verdict** | `admin` | Quyền rộng che đúng loại lỗi phạm vi/vai trò |

> 🔴 **Kiểm TRƯỚC khi dựng:** `cbnv_dp_03` ↔ `cbpd_dp_03` và `cbnv_bn_03` ↔ `cbpd_bn_03` **phải cùng
> `donViId`** — `:852` + `:1552` (BR-AUTH-05: *"CB NV cấp nào tạo → CB PD cùng đơn vị duyệt. KHÔNG xuyên cấp
> phê duyệt"*). Khác đơn vị ⇒ bước phê duyệt **không thể chạy** ⇒ đổi sang cặp `_04`/`_05` **cùng vai trò +
> cùng cấp**, ghi rõ tài khoản thực dùng. **CẤM** dùng CB PD cấp TW để duyệt báo cáo của ĐP/BN.

### 3.2 Trạng thái dữ liệu bắt buộc — nguyên văn `:986`–`:987`

```
:986  - User thuộc cấp TW
:987  - Có BC từ BN/ĐP đã gửi
```

**Yêu cầu của lô này (chặt hơn `:987`): ≥2 báo cáo của 2 ĐƠN VỊ KHÁC NHAU ở trạng thái "Đã gửi Trung ương",
ưu tiên NẰM TRONG CÙNG MỘT ĐỢT.** Lý do:
- Phiếu 343 mô tả *"Tổng hợp báo cáo thực hiện chương trình **từ nhiều đơn vị**"* và các bước J343 nói *"Chọn
  **các** báo cáo cần tổng hợp"*.
- Phiếu 344 (`THBCTHCT_02`) đòi kiểm **phép cộng** chỉ tiêu — với 1 báo cáo thì "tổng" trùng chính nó,
  **không phân biệt được** có cộng hay không (bẫy PASS oan, xem `THBCTHCT_02.md` §4.2).
- Cùng một đợt = đúng nghĩa "tổng hợp toàn quốc theo kỳ". SRS **không cấm** chọn chéo đợt (`:993` chỉ ràng
  buộc `da_gui_tw = true`) ⇒ nếu hệ thống cho chọn chéo đợt thì **ghi nhận, không chấm**.

**Bước 0 — KIỂM KÊ TRƯỚC KHI DỰNG (bắt buộc).** Đăng nhập `cbnv_tw_03` → mở khối *"Bảng BC từ BN/ĐP"*
(`:1174` khai cột `Checkbox / Don vi / Cap / Ma dot / Ky / Ngay gui / Trang thai / Hanh dong (Xem)`,
`Filter: da_gui_tw = 1`) → ghi bảng: `mã đợt | đơn vị | cấp | ngày gửi | trạng thái`.

> 🟢 **KHÔNG CẦN DỰNG — cặp tiền đề đã có sẵn.** Trinh sát chỉ-đọc 11:33–11:50 ngày 2026-08-07
> ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2) đọc được **3 báo cáo ở `DA_GUI_TW`**, trong đó
> **một cặp hoàn hảo cùng đợt / cùng kỳ / cùng biểu mẫu, đúng 1 Bộ ngành + 1 Địa phương:**
>
> | # | `baoCaoId` | Đơn vị | Cấp | Đợt | Kỳ · Biểu mẫu | `ngayGuiTw` |
> |---|---|---|---|---|---|---|
> | 1 | `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | Bộ Kế hoạch và Đầu tư | BN | `DOT-THBC01-UAT` | `SO_BO_6_THANG` · `MAU_21A` | 2026-07-20 02:00 |
> | 2 | `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` | Sở Tư pháp An Giang | DP | `DOT-THBC01-UAT` | `SO_BO_6_THANG` · `MAU_21A` | 2026-07-22 07:30 |
>
> Đợt `DOT-THBC01-UAT` = `d7a62f6e-a119-4582-8b08-f935d25c534b`, **phạm vi đúng 2 đơn vị và cả hai đã nộp**
> ⇒ hợp cấu hình `1 BN + 1 ĐP` của `:1604`. Báo cáo thứ 3 (Sở Tư pháp Hà Nội,
> `4db99158-5bc4-4069-9d52-cfc756aadc2e`, đợt `DOT-SO_BO_NAM-2026-1`, kỳ `SO_BO_NAM`) **khác đợt khác kỳ**
> ⇒ **đừng gộp chung** trừ khi cố ý thử chọn chéo đợt (khi đó chỉ **ghi nhận**, không chấm — xem gạch đầu
> dòng thứ 4 ở trên).
>
> ⇒ **Chuỗi [1]→[6] ở §3.3 và cả phương án dự phòng §3.4 nhiều khả năng KHÔNG phải chạy.** Giữ nguyên
> chúng làm đường lùi.
>
> ⚠️ **MANH MỐI, KHÔNG PHẢI CHUẨN CHẤM.** Môi trường dùng chung, tác nhân khác đang chạy ⇒ **bắt buộc mở
> lại bảng BC từ BN/ĐP và xác minh cặp này còn ở "Đã nộp" ngay trước khi bấm.**
>
> 🔴 **CHỈ CÓ MỘT LƯỢT ĐO SẠCH.** Tổng hợp làm các báo cáo đã chọn rời `DA_GUI_TW` ⇒ chạy xong là cặp này
> **hết dùng lại được**. Bắt buộc: đo phiếu **344 (bấm [Tổng hợp] — chỉ đọc, không tiêu hủy) TRƯỚC**, rồi
> mới đến phiếu 343 này, rồi 345. Muốn có tiền đề lượt hai: Bộ KH&ĐT còn 2 báo cáo đang `CHO_PHE_DUYET`
> (`c19b1bc2…` ở `DOT-SO_BO_NAM-2026-1` và `a63bf70c…` ở `DOT-SO_BO_6_THANG-2026-1`) — `cbpd_bn_03` duyệt
> rồi `cbnv_bn_03` gửi TW là thành 2 bản dự phòng, **không cần chạy lại từ bước [1]**.

Lô F5 cũng để lại một bản ghi dùng lại được (đợt `DOT-SO_BO_NAM-2026-1`, **Sở Tư pháp Hà Nội**
`…8002-000000000001`, `ngayGuiTw` 07/08/2026) — chính là báo cáo #3 ở khung trên. Chỉ dựng **phần còn thiếu**.

### 3.3 🔴 Công thức dựng một báo cáo "Đã gửi Trung ương" (chạy cho MỖI đơn vị còn thiếu)

> **Chi tiết dùng chung cho cả 3 phiếu THBCTHCT — bản đầy đủ ở [`00-TONG-HOP-BCCT.md` §3](00-TONG-HOP-BCCT.md).**
> Tóm tắt chuỗi + đường đi (API/UI) ở đây để tự chứa.

```
[1] Đợt BC tồn tại + đơn vị nằm trong phạm vi nộp                    (:717 · :646 · :657)
      chưa có → cbnv_tw_03 tạo đợt mới (chỉ TW được tạo, :625);
      trùng kỳ+năm bị chặn là ĐÚNG SPEC (:656 · :688)                     [UI hoặc API — tiền đề]
[2] cbnv_<đv>_03 mở chi tiết đợt → [Lập báo cáo]  → đơn vị "Đang lập"  (:746)   [UI hoặc API — tiền đề]
[3] cbnv_<đv>_03 nhập số liệu chỉ tiêu + [Lưu nháp]                            [UI hoặc API — tiền đề]
      🔴 BẮT BUỘC: mỗi đơn vị nhập GIÁ TRỊ KHÁC NHAU, KHÁC 0, ở các chỉ tiêu CÓ ô nhập
         (vd đơn vị #1: 1207 / 1308 · đơn vị #2: 2100 / 3400) — cần cho phép đo cộng dồn của phiếu 344
[4] cbnv_<đv>_03 [Trình duyệt KQ] → đợt/đơn vị "Chờ duyệt kết quả"     (:802 · :803)     [UI — tiền đề]
      ⚠️ ĐIỂM ĐỨT ĐÃ BIẾT — xem §3.4 phương án dự phòng
[5] cbpd_<đv>_03 (CÙNG ĐƠN VỊ) mở đợt → [Phê duyệt] → "Đã duyệt kết quả"
      (:869 = `| 3 | Nếu DUYỆT: chuyển đợt BC → DA_DUYET_KQ, BC → DA_DUYET | SM-DOT-BC |` · :1171)  [UI — tiền đề]
[6] cbnv_<đv>_03 [Gửi lên TW] → Xác nhận → đơn vị "Đã nộp"/`DA_GUI_TW`, lọt vào bảng BC của TW
      (:937 · :938 · :939 · :1173 · :1174)                                              [UI — tiền đề]
```

**Ghi bắt buộc cho mỗi đơn vị đã dựng:** `username thực dùng` · `capDonVi` · `donViId` · `mã đợt` ·
`biểu mẫu đang áp dụng` · `giá trị đã nhập ở từng chỉ tiêu` · `mốc giờ gửi TW`.

### 3.4 🔴 Phương án dự phòng khi bước [4] Trình duyệt vẫn hỏng

**Điểm đứt đã biết (lô F5, dòng 340 — verdict Reopen):** trên bản dựng nội bộ, 11/13 chỉ tiêu của biểu 21a
hiển thị sẵn `0 (HT)` và **không có ô nhập**; giao diện **không gửi** 11 khóa đó khi lưu, còn máy chủ lại đòi
chúng có mặt ⇒ bấm [Trình duyệt KQ] trả **422** kèm danh sách đúng 11 chỉ tiêu ấy. Cán bộ **không có đường
nào** hoàn tất bằng giao diện.

**Công thức ép qua bằng đường dữ liệu (đúng cách lô F5 đã làm, và PHẢI khai rõ):**
```
(a) Đọc đúng TÊN KHÓA của 13 chỉ tiêu — KHÔNG ĐOÁN. Hai nguồn hợp lệ:
      · bảng khai 13 chỉ tiêu trong bó mã giao diện đang chạy (mỗi phần tử có thuộc tính `key` + `auto`)
      · hoặc lược đồ ở /api/docs-json  (đọc được, không cần đăng nhập)
(b) Ghi bổ sung các khóa còn thiếu với giá trị 0 vào chính bản báo cáo đang lập
      (lô F5: PATCH …/bao-cao → 200, máy chủ nhận đủ 13 khóa)
(c) Gọi đúng chức năng trình duyệt của bản ghi đó, kèm `version` HIỆN TẠI (GET trước mỗi bước —
      sai `version` là lỗi xung đột, KHÔNG phải bug nghiệp vụ)
(d) Mở UI kiểm trạng thái cuối: đơn vị phải đọc được "Chờ duyệt kết quả"
```

**Ràng buộc bắt buộc khi dùng dự phòng:**
1. Đây là **tiền đề**, hợp lệ vì hành vi đang tranh chấp của **phiếu 343** là [Tổng hợp]/[Lưu tổng hợp],
   **không phải** [Trình duyệt KQ].
2. 🔴 **TUYỆT ĐỐI KHÔNG dùng đường này cho phiếu 341 (`TPDBCKQTHCT_02`)** — ở phiếu đó [Trình phê duyệt]
   **chính là** hành vi đang tranh chấp, ép bằng API ⇒ verdict vô hiệu.
3. **Khai vào báo cáo:** đổi bản ghi nào · đổi khóa nào · giá trị gì · trên env nào · lúc mấy giờ.
4. **CẤM ghi thẳng DB. CẤM đoán endpoint. CẤM đụng dữ liệu đối tác.**
5. Nếu bước [4] **đã tự chạy được** bằng giao diện (dev đã fix dòng 340) ⇒ **không dùng dự phòng**, và ghi
   nhận điều đó cho người đo dòng 340.

### 3.5 Cái gì bằng API — cái gì BẮT BUỘC bằng giao diện

| Việc | Đường được phép |
|---|---|
| Tạo đợt · lập BC · nhập số liệu · trình duyệt · phê duyệt · gửi TW · đọc lại bản ghi để đối chứng | **API hoặc UI đều được** (đây là tiền đề của phiếu 343) |
| 🔴 **Chọn ô chọn các báo cáo + bấm [Tổng hợp]** | **BẮT BUỘC GIAO DIỆN THẬT** |
| 🔴 **Bấm [Lưu] / [Lưu tổng hợp]** | **BẮT BUỘC GIAO DIỆN THẬT** — đây là hành vi đang tranh chấp của phiếu này |
| 🔴 **Bắt câu chữ thông báo C4** | Bộ bắt DOM cài **trước** thao tác, đọc `innerText` |

---

## 4. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ CẢ 3 vế MATCH, trên ≥1 lượt tổng hợp THỰC HIỆN MỚI bằng giao diện):
   (C1) Sau khi CB NV cấp TW chọn ≥2 báo cáo đã gửi TW và lưu tổng hợp, bản ghi báo cáo tổng hợp toàn quốc
        tồn tại ở máy chủ — đọc lại được sau khi TẢI LẠI TRANG BẰNG ĐỊA CHỈ, với đúng số liệu vừa lưu.
   (C3) Có mục nhật ký ứng với thao tác lưu tổng hợp, đúng tài khoản cbnv_tw_03, đúng mốc giờ.
   (C4) Người dùng nhìn thấy đúng chuỗi "Đã tổng hợp báo cáo toàn quốc" (đọc bằng innerText),
        khớp thông điệp trong phản hồi máy chủ của chính lượt bấm đó.
   VÀ vế C2 đã được ghi nhận hiện trạng đầy đủ (không chấm).

   ⚠️ Còn vế C2 = GAP ⇒ theo flow 04 §Ca biên: "Không vế nào Reopen mà còn DIFF/GAP → Cần BA".
      NGHĨA LÀ: kể cả C1+C3+C4 đều đạt, verdict logic của phiếu vẫn là **Cần BA**, KHÔNG phải Pass.

❌ REOPEN nếu (ít nhất một vế MATCH sai / mới đúng một phần):
   - Bấm [Lưu] báo thành công nhưng bản ghi tổng hợp KHÔNG đọc lại được sau khi tải lại trang;
   - HOẶC số liệu lưu xuống khác số liệu trên form (đã trừ phần CB NV TW chủ động sửa);
   - HOẶC không có mục nhật ký nào cho thao tác lưu tổng hợp;
   - HOẶC không hiển thị thông báo nào cho người dùng, hoặc câu chữ khác nghĩa chuỗi :1032;
   - HOẶC hai đường đo mâu thuẫn nhau.
   ⇒ Khi đó verdict logic = **Reopen + cần BA** (nêu riêng vế lỗi và câu hỏi BA của C2).

⏸ CHƯA CHỐT nếu: không dựng nổi ≥2 báo cáo "Đã gửi TW", hoặc thao tác [Tổng hợp]/[Lưu] bị máy chủ chặn vì
   điều kiện trạng thái ĐỢT (xem §6) — ghi rõ mã lỗi + nguyên văn thông điệp, nêu dữ kiện còn thiếu.
```

### 4.1 ⚠️ Bẫy chống **FAIL oan**

1. 🔴 **Chấm C2 bằng nhãn trên màn.** Đây là bẫy lớn nhất của phiếu. **Hai bậc trạng thái:** trục **ĐỢT**
   (`DOT_BAO_CAO.trang_thai`, `:1368`, nhãn `:1198` `DA_GUI_TW → "Da gui TW"`, `:1199` `DA_TONG_HOP → "Da
   tong hop"`) và trục **ĐƠN VỊ** (`DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop`, `:1389`, **không có**
   `DA_TONG_HOP`). Lô F5 đo được cùng một đợt cho **hai câu trả lời khác nhau** tùy vai trò đăng nhập.
   ⇒ **C2 đã khóa GAP, cấm chấm** — dù thấy nhãn đúng hay sai.
2. **Nhãn nút khác phiếu.** Phiếu ghi *"Lưu tổng hợp"*; `:1175` khai **[Luu]**. Phiếu không nhắc nhãn nút
   ⇒ cấm FAIL vì nhãn.
3. **Không tìm thấy trường `loai = TONG_HOP_TW` trong bản ghi.** `:1016`/`:1021` khai `BAO_CAO_CT
   (loai = TONG_HOP_TW)` **nhưng entity `BAO_CAO_CT_HTPL` (`:1400`–`:1418`) KHÔNG khai trường `loai`**, và
   `don_vi_nop_id` (`:1410`) lại **bắt buộc** và mô tả là *"Đơn vị nộp BC (ĐP/BN)"* — không có chỗ cho bản
   ghi cấp TW. ⇒ **Cấm FAIL vì bản ghi không mang nhãn `TONG_HOP_TW`.** C1 chỉ hỏi *"có lưu được bản ghi báo
   cáo tổng hợp toàn quốc không"*. Ghi nhận mâu thuẫn này cho BA (§7).
4. **`da_gui_tw` không thấy trong entity.** `:937`, `:993`, `:1174` đều dùng cờ `da_gui_tw`, nhưng **không
   entity nào khai trường này** (`DOT_BAO_CAO` `:1356`–`:1375`, `BAO_CAO_CT_HTPL` `:1405`–`:1418`).
   ⇒ ghi nhận, **không** biến thành lý do FAIL.
5. **Thông báo hiện ở bước [Tổng hợp] thay vì bước [Lưu].** `:1032` khai mã `INF-XI-09-01` cho *"Tổng hợp
   thành công"* **không nói bấm nút nào**. Miễn là chuỗi hiện ra ở bước hoàn tất tổng hợp ⇒ đạt C4; ghi nhận
   nếu lệch bước.
6. **Hệ thống cho chọn báo cáo chéo nhiều đợt.** `:993` chỉ ràng buộc `da_gui_tw = true` ⇒ SRS im lặng,
   ghi nhận, không chấm.
7. **Địa chỉ trang có tiền tố `/ct-htpldn/`** — BA-23 (`:1090`, `:1103`, `:1147`–`:1149`) chỉ đòi màn độc
   lập, SRS không đặc tả chuỗi địa chỉ.
8. **Bấm bằng tài khoản không phải cấp TW rồi bị chặn** = **ĐÚNG SPEC** (`:986`, `:1030` `ERR-XI-09-02`
   *"Chỉ cấp TW mới tổng hợp BC"*, `:1175` điều kiện hiển thị *"user TW"*). Cấm log.
9. **Không chọn báo cáo nào rồi bấm [Tổng hợp] và bị chặn** = ĐÚNG SPEC (`:1029` `ERR-XI-09-01`).
10. 🔴 **Đợt chưa sang "Đã tổng hợp" ngay sau khi bấm [Lưu] — CÓ THỂ do còn một bước "chốt" nữa.** Manh mối
    từ trinh sát ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §3.2): bản dựng có **hai** thao tác tách
    rời — `POST /api/v1/dot-bao-caos/tong-hop` (lưu bản tổng hợp) và
    `POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop`, mà mô tả của thao tác **sau** mới nói đưa đợt
    liên quan sang `DA_TONG_HOP`. ⇒ Nếu bấm [Lưu] xong đợt chưa đổi nhãn, **phải rà màn xem còn nút
    "Hoàn thành/Chốt tổng hợp" hay không rồi mới kết luận**. Dù sao **C2 đã khóa `GAP` ⇒ cấm chấm**; đây chỉ
    là dữ kiện mô tả cho BA (§7) và cho tiền đề của phiếu 345.
11. 🔴 **Bẫy tên gọi — cùng một báo cáo, hai cái tên.** Ở bảng tiến độ theo đơn vị, giá trị đọc được là
    `tienDo[].trangThaiNop = DA_NOP` (trục **ĐƠN VỊ**, `:1389`); cũng chính báo cáo đó trong danh sách tổng
    hợp của TW lại mang `trangThai = DA_GUI_TW` (trục **BÁO CÁO**, `:1418`). **Thấy `DA_NOP` không có nghĩa
    là chưa gửi TW.** Đối chiếu bằng `ngayGuiTw` + `baoCaoId`, đừng đối chiếu bằng tên trạng thái.

### 4.2 ⚠️ Bẫy chống **PASS oan**

1. **Tin vào thông báo thành công.** Đúng mẫu đã dính ở dòng 340/342: báo thành công mà máy chủ không đổi gì.
   **Bắt buộc:** đọc lại bản ghi tổng hợp **sau khi tải lại trang bằng địa chỉ**.
2. **Tổng hợp chỉ 1 báo cáo rồi chấm Pass.** Phiếu nói *"từ nhiều đơn vị"* ⇒ sàn là **≥2 đơn vị khác nhau**.
3. **Nhìn nhầm bản ghi cũ.** Phải khớp **đủ ba**: mã đợt + danh sách đơn vị đã chọn + mốc giờ lưu.
   Dùng chuỗi mốc-giờ `QA-F8-343-<YYYYMMDD-HHmm>` đặt vào một ô cho phép nhập trên form tổng hợp.
4. **Đọc bản ghi bằng `admin`.** Quyền rộng che lỗi phạm vi ⇒ đọc bằng chính phiên `cbnv_tw_03`.
5. **Đọc chữ bằng `textContent`** (gom node ẩn AntD → thông báo ma). Dùng `innerText`.
6. **Bộ bắt thông báo lọc trùng.** CẤM lọc trùng; đếm kèm **số yêu cầu gửi đi**; đếm theo **mốc giờ khác
   nhau**, không theo độ dài mảng. *(Lô F5: 1 thông báo sinh 2 nút DOM `ant-message` + `ant-message-notice-
   wrapper` lệch ~1–2 ms ⇒ vẫn là 1 thông báo.)*
7. **Tab mở lâu chạy bó mã cũ.** Tải lại bằng địa chỉ + đọc tên bó mã `assets/index-*.js` **đầu và cuối** phiên.
8. **Kết luận trên env khác.** Đo trên env **nội bộ**; đối tác nghiệm thu trên `htpldn-uat.ospgroup.vn`
   ⇒ ghi câu giới hạn hiệu lực.

---

## 5. Đường đo thứ hai (đối chứng độc lập — đúng 1 đường)

**Phương án A (khuyến nghị):** sau khi lưu, **tải lại trang bằng địa chỉ** rồi đọc lại bản ghi tổng hợp bằng
**chính phiên `cbnv_tw_03`** (cookie-auth, không dùng `admin`) — so số liệu đọc lại với số liệu trên form
lúc bấm [Lưu]. 🔴 Tra `/api/docs-json` lấy đúng đường dẫn, **CẤM đoán endpoint**.

**Phương án B (khi A không khả thi):** đăng nhập một tài khoản cấp TW khác (`cbnv_tw_04`, **cùng vai trò +
cùng cấp**) mở lại màn tổng hợp → thấy cùng bản ghi ⇒ chứng minh dữ liệu nằm ở máy chủ.

Bấm lại cùng một nút **không** tính là đường thứ hai. **Hai đường mâu thuẫn ⇒ CHƯA được chốt.**

---

## 6. 🔴 Rủi ro verdict **Chưa chốt** — CAO. Cảnh báo trước cho điều phối

| # | Rủi ro | Vì sao | Nếu xảy ra thì làm gì |
|---|---|---|---|
| **R1** | **Máy chủ chặn [Tổng hợp]/[Lưu] vì đợt chưa ở `DA_GUI_TW`** | `:1517` đặt tiền trạng thái `DA_GUI_TW` cho bước tổng hợp, nhưng lô F5 đo được trục ĐỢT **đứng yên `TAO_DOT`** sau khi gửi TW (`daGuiTw = false`, `ngayGuiTw = null`), và tab lọc "Đã gửi TW" của TW **rỗng** | Ghi **nguyên văn mã lỗi + thông điệp**, chụp màn. Đây là **bằng chứng mạnh cho GAP §2** ⇒ verdict **Cần BA + Chưa chốt phần C1/C3/C4**. 🔴 **CẤM ép trạng thái đợt bằng đường dữ liệu để "cho chạy được"** — trạng thái đợt **chính là** vế C2 đang tranh chấp, và không có chức năng hợp lệ nào sinh ra nó (SRS giao việc đó cho `:937` mà `:937` không chạy) |
| **R2** | Không dựng nổi đơn vị thứ hai (cặp `cbnv_bn_03`/`cbpd_bn_03` khác đơn vị, hoặc bước [4] hỏng và không đọc được tên khóa chỉ tiêu) | §3.1 + §3.4 | Đo với số đơn vị dựng được, **khai rõ**; nếu chỉ 1 đơn vị ⇒ C1/C3/C4 vẫn chấm được nhưng phải ghi giới hạn; **phiếu 344 thì Chưa chốt** (không kiểm được phép cộng) |
| **R3** | Không tìm thấy khối [Tổng hợp] trên giao diện của `cbnv_tw_03` | `:1175` khai khối #45 điều kiện hiển thị *"user TW"* | Chụp màn + đọc lại vai trò/cấp của tài khoản (`capDonVi = TW`). Nếu đúng TW mà **không có** khối này ⇒ đây là **lỗi thật của vế C1** (không có đường nào lưu tổng hợp) ⇒ **Reopen**, kèm khối `CÁCH VERIFY` |
| **R4** | Lưu tổng hợp **đổi trạng thái cả đợt** ⇒ hỏng tiền đề của các phiếu/lô khác dùng chung đợt | `:1005` | Chạy **sau** phiếu 341 và **sau** phiếu 344 (thứ tự ở `00-TONG-HOP-BCCT.md` §4); khai rõ bản ghi đã đổi để lô sau biết |
| **R5** | **Chỉ có MỘT lượt đo sạch** — tổng hợp xong là cặp `c4801d2d…` + `df6498aa…` rời `DA_GUI_TW` | Trinh sát §5.3(b) | Đo **344 trước** (chỉ đọc), rồi 343, rồi 345. Cần lượt hai: `cbpd_bn_03` duyệt + `cbnv_bn_03` gửi TW 2 báo cáo `CHO_PHE_DUYET` của Bộ KH&ĐT (`c19b1bc2…`, `a63bf70c…`) |

> 🟢 **R1 và R2 đã hạ mức sau kiểm kê 11:50** (xem §3.2): tiền đề **≥2 báo cáo "Đã gửi TW" đã tồn tại**
> ⇒ R2 gần như loại bỏ. Với R1, đợt `DOT-THBC01-UAT` đọc được vẫn ở `trangThai = TAO_DOT` **trong khi hai
> báo cáo con đã ở `DA_GUI_TW`** — tức hiện tượng "trục ĐỢT đứng yên" của lô F5 **vẫn còn**, nhưng bản dựng
> **có vẻ chặn theo trục BÁO CÁO** (danh sách tổng hợp lọc `da_gui_tw`, không lọc trạng thái đợt) nên khả
> năng bị chặn thấp hơn dự phòng ban đầu. **Đây là suy đoán từ manh mối, không phải kết luận** — nếu vẫn bị
> chặn thì xử đúng như ô R1. **Lệnh cấm ép trạng thái đợt giữ nguyên hiệu lực.**

---

## 7. Ghi nhận (KHÔNG chấm) — gửi BA/dev

1. **`:1016`/`:1021` khai `BAO_CAO_CT (loai = TONG_HOP_TW)` nhưng entity `BAO_CAO_CT_HTPL` (`:1400`–`:1418`)
   không có trường `loai`**, còn `don_vi_nop_id` (`:1410`) bắt buộc và mô tả là đơn vị **ĐP/BN** ⇒ chưa có
   chỗ khai bản ghi tổng hợp cấp TW. Đề nghị BA bổ sung trường + enum, hoặc chỉ rõ entity khác.
2. **Cờ `da_gui_tw` dùng ở `:937`, `:993`, `:1174` nhưng không entity nào khai** (`:1356`–`:1375`,
   `:1405`–`:1418`).
3. **`:1005` viết "các đợt BC đã chọn" trong khi đầu vào `:993` là "bao_cao_ids"** — nên phát biểu lại cho
   khớp thứ người dùng thực sự chọn.

*(Cả 3 mục đều là **đặc tả**, không mở dòng bug `_QA<n>` — chốt sẵn một phía khi chưa biết phía nào đúng là
sai quy trình. Đề nghị BA trả lời §2.1 trước.)*

---

## 8. Độ phủ biến thể — **sàn: 1 lượt tổng hợp, ≥2 đơn vị, cùng 1 đợt**

| # | Dạng | Bắt buộc? |
|---|---|---|
| **①** | 1 đơn vị **ĐP** + 1 đơn vị **BN** trong cùng đợt | **BẮT BUỘC** (đúng `:1604` BR-FLOW-08 *"ĐP/BN gửi BC đã duyệt lên TW"*) |
| ② | 2 đơn vị cùng cấp | Chấp nhận khi ① không dựng được — **khai rõ** |

**KHÔNG mở rộng:** không đo lại FR-XI-08 (gửi TW — dòng 342, lô F5 đã đo); không đo nhánh từ chối của CB PD;
không đo `WRN-XI-09-01` (`:1031`, BC dùng mẫu cũ) — phiếu không nhắc; không đo xuất tệp (đó là **phiếu 345**).
