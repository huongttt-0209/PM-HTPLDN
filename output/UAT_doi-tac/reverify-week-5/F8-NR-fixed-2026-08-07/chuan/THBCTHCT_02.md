# Chuẩn chấm đã khóa — THBCTHCT_02 (dòng 344) — "Kiểm tra khi bấm nút «Tổng hợp»"

> **Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> (1.610 dòng). **Mọi số dòng dưới đây do agent này tự mở file đếm lại ngày 2026-08-07.**
>
> **Trạng thái phiếu:** đối tác **CHƯA TỪNG CHẠY** — `Trạng thái` (N) = `N/R`, `Kết quả thực tế` (L) RỖNG,
> không ảnh ⇒ **`expected đối tác` = nguyên văn cột `Kết quả mong đợi` (K)**.
>
> **Điều kiện (H344):** *"NSD là cán bộ nghiệp vụ cấp Trung ương và có ít nhất một báo cáo từ Bộ/Ngành hoặc
> Địa phương đã gửi lên."* **Các bước (J344):** *"1. Chọn menu «Đợt báo cáo» · 2. Chọn các báo cáo cần tổng
> hợp trong bảng danh sách (ô chọn) và bấm nút «Tổng hợp»"* — **dừng ở đây, KHÔNG bấm [Lưu]** (bấm Lưu là
> phiếu 343).

**Expected đối tác (nguyên văn K344):**
```
- Hệ thống:
+ Gợi ý số liệu tổng hợp: tính tổng các chỉ tiêu tương ứng theo Biểu 21a và Biểu 21b từ các báo cáo đã chọn.
+ Hiển thị biểu mẫu tổng hợp Biểu 21a, 21b toàn quốc cho phép cán bộ nghiệp vụ cấp Trung ương chỉnh sửa, bổ sung.
```

---

## 1. BẢNG SCOPE LOCK — 3 vế (vế 2 của phiếu là câu ghép ⇒ tách C2a/C2b)

| Vế | Expected đối tác (nguyên văn) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|---|
| **C1** | "**Gợi ý số liệu tổng hợp: tính tổng các chỉ tiêu tương ứng** theo Biểu 21a và Biểu 21b **từ các báo cáo đã chọn**" | **`:1002`** (chính) · `:1037` · `:1175` · `:1231` | `:1002` = `\| 4 \| Hệ thống gợi ý số liệu: tính tổng các cột tương ứng 21a/21b \| — \|` · `:1037` = `- **Given** CB NV TW chọn các BC **When** nhấn "Tổng hợp" **Then** gợi ý số liệu + form tổng hợp theo TT17` | **MATCH** | **TEST** | **UI:** `cbnv_tw_03` tick ≥2 báo cáo → [Tổng hợp] → đọc từng ô số của form tổng hợp. **Đối chứng độc lập:** đọc lại số liệu của **từng báo cáo nguồn** (bằng chính phiên `cbnv_tw_03`) rồi tự cộng tay → so từng chỉ tiêu |
| **C2a** | "**Hiển thị biểu mẫu tổng hợp … toàn quốc cho phép cán bộ nghiệp vụ cấp Trung ương chỉnh sửa, bổ sung**" | **`:1003`** (chính) · `:1175` · `:1038` | `:1003` = `\| 5 \| CB NV TW chỉnh sửa/bổ sung trên form tổng hợp \| — \|` · `:1175` (trích) = `Chon BC (checkbox) -> [Tong hop] -> tu tinh tong hop mau 21a/21b -> form editable -> [Luu] …` | **MATCH** | **TEST** | **UI:** form tổng hợp hiện ra và **thực sự sửa được** — gõ một giá trị mốc-giờ vào một ô, giá trị nhận vào ô (đọc lại bằng `innerText`/`value`). **Đối chứng độc lập:** đọc thuộc tính chỉ-đọc/vô-hiệu của ô đó trong DOM |
| **C2b** | "biểu mẫu tổng hợp **Biểu 21a, 21b**" — tức **đủ CẢ HAI biểu** | **IM LẶNG** — gần nhất: `:1002` (*"21a/21b"*), `:1175` (*"mau 21a/21b"*), `:1167`/`:1168` (điều kiện hiển thị 2 biểu **ở form của ĐƠN VỊ**, không phải form tổng hợp TW) | `:1167` = `\| 37 \| form \| Bieu mau 21a (TT17/2025) \| form (editable table, C23) \| Chi tieu / So lieu ky truoc / Ky nay / Ghi chu… \| input \| **khi bieu mau ap dung va dot o DANG_LAP_BC** \|` | **GAP** | **BA** | **CẤM Pass/Reopen vế này.** Chỉ ghi nhận: form tổng hợp đang hiện những biểu nào, và `bieu_mau_su_dung` của từng báo cáo nguồn là gì |

### 1.1 Vì sao C2b là `GAP` (không phải grep rỗng)

Đã đọc trọn FR-XI-09 `:971`–`:1038` và trọn bảng thành phần màn hình `:1163`–`:1175`.
- SRS **không có dòng nào** nói form tổng hợp của TW phải hiện **cả hai** biểu 21a **và** 21b, hay hiện theo
  `bieu_mau_su_dung` của các báo cáo được chọn. Chuỗi `21a/21b` ở `:1002`, `:1006`, `:1175`, `:1231` là cách
  viết gộp, **không** phát biểu điều kiện hiển thị.
- Điều kiện hiển thị **duy nhất** SRS khai cho hai biểu (`:1167` cho 21a, `:1168` cho 21b) là
  *"khi bieu mau ap dung va dot o DANG_LAP_BC"* — đó là **form lập BC của ĐƠN VỊ**, không phải form tổng hợp
  của TW (khối #45, `:1175`).
- Mặt khác `:730` (FR-XI-06 input `bieu_mau_su_dung`) + `:1366` (entity `DOT_BAO_CAO`) cho phép mỗi đơn vị
  chọn `MAU_21A` / `MAU_21B` / `CA_HAI` ⇒ tập hợp báo cáo nguồn có thể **chỉ có 21a**. SRS im lặng về việc
  khi đó biểu 21b có phải hiện (rỗng) hay không.
⇒ Không xác định được chuẩn chấm ⇒ `GAP`, route BA.

**Câu hỏi BA cho C2b (bắt buộc có trong kết quả nếu form không hiện đủ 2 biểu):**
> **CẦN BA CONFIRM:** đối tác kỳ vọng *"hiển thị biểu mẫu tổng hợp **Biểu 21a, 21b** toàn quốc"* (đủ cả hai);
> SRS **im lặng** — FR-XI-09 (`srs-fr-15-ct-htpldn.md:971`–`:1038`) chỉ viết gộp *"21a/21b"* (`:1002`) và
> khối màn hình `:1175` chỉ ghi *"tu tinh tong hop mau 21a/21b … form editable"*, **không** khai điều kiện
> hiển thị; điều kiện hiển thị duy nhất cho hai biểu (`:1167`, `:1168`) lại thuộc **form lập BC của đơn vị**
> (*"khi bieu mau ap dung va dot o DANG_LAP_BC"*), trong khi mỗi đơn vị được tự chọn mẫu (`:730`, `:1366`);
> web/dev hiện tại **<điền sau khi đo: form tổng hợp đang hiện biểu nào · báo cáo nguồn dùng mẫu nào>**.
>
> **Câu hỏi BA:** form tổng hợp của TW phải hiện **cả hai** biểu 21a và 21b trong mọi trường hợp, hay chỉ
> hiện những biểu mà các báo cáo được chọn thực sự sử dụng? Nếu là vế thứ nhất, xin bổ sung điều kiện hiển
> thị cho khối tổng hợp (`:1175`).

### 1.2 Ranh giới với phiếu 343 — CẤM lấn

Phiếu 344 **dừng ở bước bấm [Tổng hợp]** (chưa lưu). Các vế *"lưu bản ghi"*, *"chuyển trạng thái đợt"*,
*"lưu vết"*, *"thông báo «Đã tổng hợp báo cáo toàn quốc»"* thuộc **phiếu 343** ⇒ **không chấm ở đây**,
không mở thêm phép đo. Nếu vì thứ tự chạy mà đã bấm [Lưu] ở phiếu 343 trước, **vẫn phải bấm lại [Tổng hợp]
để đo phiếu này** — quan sát tĩnh trên form còn sót lại **không** được dùng để Pass (flow 04 §Chạy mục 5:
*"CẤM Pass bằng quan sát tĩnh"*).

---

## 2. Tiền đề tối thiểu

### 2.1 Tài khoản

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| 🔴 **Người ra verdict** — CB Nghiệp vụ cấp **TW** | **`cbnv_tw_03`** · `Test@1234` | **Tick ô chọn + bấm [Tổng hợp] bằng giao diện thật**. `:982` Tác nhân *"Cán bộ Nghiệp vụ TW"*; `:986` *"User thuộc cấp TW"*; `:1175` điều kiện hiển thị *"user TW"* |
| Dựng tiền đề đơn vị #1 / #2 | `cbnv_dp_03` + `cbpd_dp_03` · `cbnv_bn_03` + `cbpd_bn_03` (**mỗi cặp phải cùng `donViId`** — `:852`, `:1552`) | Lập → trình → duyệt → gửi TW |
| **CẤM ra verdict** | `admin` | Quyền rộng che lỗi phạm vi/vai trò |

### 2.2 Trạng thái dữ liệu bắt buộc

`:986` *"User thuộc cấp TW"* · `:987` *"Có BC từ BN/ĐP đã gửi"*.

🔴 **Yêu cầu chặt hơn của phiếu này — đây là điểm quyết định chấm được hay không:**

> **≥2 báo cáo của 2 ĐƠN VỊ KHÁC NHAU, ở trạng thái "Đã gửi Trung ương", và có ÍT NHẤT MỘT CHỈ TIÊU mà hai
> đơn vị nhập GIÁ TRỊ KHÁC NHAU, KHÁC 0.**

Vì vế C1 hỏi **phép cộng**. Với 1 báo cáo, "tổng" trùng chính nó ⇒ không phân biệt được hệ thống có cộng hay
chỉ chép lại. Với 2 báo cáo mà mọi chỉ tiêu đều `0` ⇒ tổng cũng là `0` ⇒ vẫn không phân biệt được.
**Lô F5 đo được: 11/13 chỉ tiêu của biểu 21a là do hệ thống tự tính và luôn hiện `0`; chỉ 2 chỉ tiêu cuối có
ô nhập tay.** ⇒ phép đo cộng dồn **phải đặt vào đúng các chỉ tiêu có ô nhập**.

**Giá trị đề nghị (ghi nguyên vào báo cáo đo):**

| Đơn vị | Chỉ tiêu có ô nhập #1 | Chỉ tiêu có ô nhập #2 |
|---|---|---|
| Đơn vị #1 (ĐP) | `1207` | `1308` |
| Đơn vị #2 (BN) | `2100` | `3400` |
| **Tổng kỳ vọng** | **`3307`** | **`4708`** |

*(Nếu tái dùng bản ghi Sở Tư pháp Hà Nội mà lô F5 để lại — đợt `DOT-SO_BO_NAM-2026-1`, đã "Đã nộp" — thì
đọc lại giá trị thực của bản ghi đó trước, rồi chọn giá trị cho đơn vị #2 sao cho tổng là con số duy nhất,
không trùng bất kỳ số hạng nào.)*

> 🟢 **CẶP BÁO CÁO ĐÃ CÓ SẴN — nhưng phải ĐỌC SỐ LIỆU CỦA CHÚNG TRƯỚC KHI ĐO.** Trinh sát chỉ-đọc
> 11:33–11:50 ngày 2026-08-07 ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2) đọc được cặp cùng
> đợt/kỳ/biểu mẫu, đúng 1 BN + 1 ĐP:
> **`c4801d2d-dedc-4ffe-b5d2-44e9245fbedc`** (Bộ KH&ĐT) + **`df6498aa-4ae4-4d59-ba3e-7c322e1f9a59`**
> (Sở TP An Giang), cùng đợt `DOT-THBC01-UAT`, kỳ `SO_BO_6_THANG`, biểu `MAU_21A`.
> Bản của Bộ KH&ĐT có **đủ 13 khóa chỉ tiêu**; **số liệu cụ thể của cả hai thì CHƯA đọc được** —
> trinh sát chỉ đếm khóa, không ghi giá trị.
>
> ⇒ **Bước bắt buộc trước khi bấm [Tổng hợp]:** mở **từng báo cáo nguồn** (nút *Xem* ở bảng BC từ BN/ĐP) và
> **chép nguyên giá trị từng chỉ tiêu của cả hai bản** vào báo cáo đo. Đó vừa là số hạng để tự cộng tay,
> vừa là **đối chứng độc lập** ở §4. **Không được lấy bảng "Giá trị đề nghị" ở trên làm kỳ vọng nếu không
> tự tay nhập** — dữ liệu này là dữ liệu seed sẵn, ta **không** chọn giá trị cho nó.
>
> 🔴 **Kiểm khả năng phân biệt NGAY sau khi đọc.** Nếu hai bản trùng nhau ở mọi chỉ tiêu, hoặc mọi chỉ tiêu
> đều `0`, thì **phép cộng không phân biệt được** ⇒ **không được chấm C1 là Đạt**. Khi đó chọn 1 trong 2:
> (a) sửa số liệu một bản nguồn nếu bản dựng còn cho sửa **trước khi gửi TW** — nhưng cặp này **đã** gửi rồi
> nên nhiều khả năng bị khóa; (b) **dựng thêm một báo cáo nguồn thứ ba với giá trị khác hẳn** theo đường
> ngắn nhất: Bộ KH&ĐT còn 2 báo cáo `CHO_PHE_DUYET` (`c19b1bc2…` ở `DOT-SO_BO_NAM-2026-1`, `a63bf70c…` ở
> `DOT-SO_BO_6_THANG-2026-1`) — bù số liệu → `cbpd_bn_03` duyệt → `cbnv_bn_03` gửi TW.
> Không làm được cả (a) lẫn (b) ⇒ **C1 ghi `Chưa chốt`**, nêu rõ thiếu dữ kiện gì.
>
> ⚠️ **MANH MỐI, KHÔNG PHẢI CHUẨN CHẤM** — môi trường dùng chung, **xác minh lại ngay trước khi đo**.
>
> 🔴 **Bấm [Tổng hợp] (bước gợi ý số liệu) là thao tác CHỈ ĐỌC ⇒ không tiêu hủy tiền đề.** Nhưng bấm
> [Lưu tổng hợp] của phiếu 343 thì có. **Phiếu 344 này phải đo TRƯỚC phiếu 343.**

### 2.3 Công thức dựng + phương án dự phòng

Dùng **chung** với phiếu 343 — bản đầy đủ ở [`00-TONG-HOP-BCCT.md` §3](00-TONG-HOP-BCCT.md);
tóm tắt + phương án ép qua bước [Trình duyệt KQ] bằng đường dữ liệu: xem [`THBCTHCT_01.md` §3.3–§3.4](THBCTHCT_01.md).

### 2.4 Cái gì bằng API — cái gì BẮT BUỘC bằng giao diện

| Việc | Đường được phép |
|---|---|
| Tạo đợt · lập BC · nhập số liệu · trình duyệt · phê duyệt · gửi TW · đọc lại số liệu báo cáo nguồn để đối chứng | **API hoặc UI đều được** — tiền đề |
| 🔴 **Tick ô chọn các báo cáo + bấm [Tổng hợp]** | **BẮT BUỘC GIAO DIỆN THẬT** — hành vi đang tranh chấp |
| 🔴 **Kiểm "sửa được"** (C2a) | **BẮT BUỘC gõ thật vào ô trên giao diện**, không suy từ thuộc tính DOM đơn thuần |

Seed = mutate môi trường chung ⇒ khai: **đổi bản ghi nào · đổi gì · trên env nào**.
Cấm đoán endpoint (đọc `/api/docs-json` trước), cấm ghi thẳng DB, cấm đụng dữ liệu đối tác.

---

## 3. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ cả C1 + C2a, trên ≥1 lượt bấm [Tổng hợp] THỰC HIỆN MỚI bằng giao diện):
   (C1)  Với ≥2 báo cáo của 2 đơn vị khác nhau có số liệu khác nhau, form tổng hợp hiện sẵn giá trị bằng
         ĐÚNG TỔNG của các báo cáo đã chọn, ở TỪNG chỉ tiêu (không chỉ ở một ô);
         và tổng đó khớp với phép cộng tay từ số liệu đọc lại của chính các báo cáo nguồn.
   (C2a) Form tổng hợp cho cán bộ cấp TW sửa được và bổ sung được (gõ giá trị vào ô → ô nhận giá trị).
   ⚠️ Còn vế C2b = GAP ⇒ theo flow 04 §Ca biên "Không vế nào Reopen mà còn DIFF/GAP → Cần BA":
      verdict logic của phiếu là **Cần BA** ngay cả khi C1 + C2a đều đạt, TRỪ KHI phép đo cho thấy form
      hiện đủ cả hai biểu đúng như phiếu mong đợi — khi đó vẫn KHÔNG Pass vế C2b (luật khóa 5), nhưng
      tóm tắt phải ghi rõ "web hiện tại đúng kỳ vọng đối tác", câu hỏi BA nhằm BỔ SUNG ĐẶC TẢ.

❌ REOPEN nếu:
   - Bấm [Tổng hợp] mà form tổng hợp không hiện ra;
   - HOẶC form hiện ra nhưng mọi ô đều rỗng / bằng 0 trong khi báo cáo nguồn có số khác 0;
   - HOẶC giá trị hiện ra KHÔNG bằng tổng (vd chỉ lấy báo cáo đầu tiên, hoặc nhân đôi, hoặc lệch một số hạng);
   - HOẶC form hiện ra nhưng cán bộ cấp TW không sửa/bổ sung được (ô chỉ đọc, vô hiệu);
   - HOẶC hai đường đo mâu thuẫn nhau.

⏸ CHƯA CHỐT nếu: không dựng nổi ≥2 báo cáo "Đã gửi TW" có số liệu phân biệt được, hoặc [Tổng hợp] bị máy
   chủ chặn vì điều kiện trạng thái ĐỢT (xem [`THBCTHCT_01.md` §6 R1](THBCTHCT_01.md)) — ghi nguyên văn mã
   lỗi + thông điệp, nêu dữ kiện còn thiếu.
```

### 3.1 ⚠️ Bẫy chống **FAIL oan**

1. **Chấm C2b (thiếu biểu 21b) thành lỗi.** Đã khóa `GAP` ở §1.1 — **cấm FAIL**, kể cả khi form chỉ hiện 21a
   vì mọi báo cáo nguồn đều dùng `MAU_21A`.
2. **11 chỉ tiêu đầu đều `0` nên "tổng sai".** Lô F5 đo được 11 chỉ tiêu đầu là do hệ thống tự tính và đang
   trả `0` ở tầng đơn vị. `0 + 0 = 0` là **đúng phép cộng**. Chỉ chấm sai khi tổng của các chỉ tiêu **có số
   liệu phân biệt được** không khớp.
3. **Nhãn nút / nhãn cột khác phiếu.** Phiếu ghi "Tổng hợp"; `:1175` khai `[Tong hop]`. Không nhắc nhãn ⇒
   cấm FAIL vì nhãn.
4. **Không chọn báo cáo nào rồi bấm và bị chặn** = ĐÚNG SPEC (`:1029` `ERR-XI-09-01` *"Vui lòng chọn ít nhất
   1 BC để tổng hợp"*).
5. **Tài khoản không phải cấp TW bị chặn** = ĐÚNG SPEC (`:986`, `:1030` `ERR-XI-09-02`, `:1175` *"user TW"*).
6. **Báo cáo dùng mẫu cũ bị cảnh báo** = ĐÚNG SPEC (`:1031` `WRN-XI-09-01`). Không phải vế phiếu.
7. **Form tổng hợp không hiện cột "Số liệu kỳ trước"/"Ghi chú".** Bốn cột đó (`:1167`) là của **form lập BC
   của đơn vị**; phiếu 344 không nhắc cột ⇒ không chấm.
8. **Địa chỉ trang có tiền tố `/ct-htpldn/`** — xem BA-23 (`:1090`, `:1103`, `:1147`–`:1149`).

### 3.2 ⚠️ Bẫy chống **PASS oan** *(mục 1–2 là bẫy nguy hiểm nhất của phiếu này)*

1. 🔴 **Tổng hợp 1 báo cáo rồi chấm Pass.** "Tổng" của một số hạng trùng chính nó ⇒ **không chứng minh được
   hệ thống cộng**. Sàn cứng: **≥2 đơn vị**.
2. 🔴 **Mọi chỉ tiêu đều `0` rồi chấm Pass.** `0` ở mọi ô không phân biệt được "cộng đúng" với "không cộng gì".
   Bắt buộc có ≥1 chỉ tiêu mà hai đơn vị nhập số **khác nhau, khác 0**, và tổng là **con số duy nhất** không
   trùng bất kỳ số hạng nào.
3. **Chỉ kiểm một ô rồi suy ra cả bảng.** Vế C1 nói *"tính tổng các chỉ tiêu tương ứng"* ⇒ đọc **từng** chỉ
   tiêu của biểu đang hiện, lập bảng `chỉ tiêu | BC#1 | BC#2 | tổng kỳ vọng | form hiện`.
4. **Kết luận "sửa được" từ vẻ ngoài của ô.** Phải **gõ thật** một giá trị mốc-giờ và đọc lại.
5. **Nhìn nhầm số của lượt tổng hợp trước.** Đổi bộ chọn (bỏ tick 1 báo cáo, bấm lại [Tổng hợp]) → tổng phải
   đổi theo. *(Đây vẫn thuộc **cùng một đường đo** của C1, không phải phép đo mới.)*
6. **Đọc chữ/số bằng `textContent`** (gom node ẩn AntD → số ma). Dùng `innerText` / `value` của ô nhập.
7. **Tab mở lâu chạy bó mã cũ** ⇒ tải lại bằng địa chỉ, đọc tên bó mã `assets/index-*.js` đầu và cuối phiên.
8. **Kết luận trên env khác** ⇒ ghi câu giới hạn hiệu lực (đo trên env nội bộ).

---

## 4. Đường đo thứ hai (đối chứng độc lập — đúng 1 đường)

Đọc lại **số liệu của từng báo cáo nguồn** bằng **chính phiên `cbnv_tw_03`** (cookie-auth, không dùng
`admin`) → tự cộng tay → so với bảng số trên form tổng hợp.
🔴 Tra `/api/docs-json` lấy đúng đường dẫn — **CẤM đoán endpoint**.
Bấm lại cùng nút [Tổng hợp] với **cùng bộ chọn** không tính là đường thứ hai.
**Hai đường mâu thuẫn ⇒ CHƯA được chốt** — ghi cả hai, hỏi user.

---

## 5. Rủi ro verdict **Chưa chốt** — TRUNG BÌNH–CAO

| # | Rủi ro | Cần bổ sung gì mới chốt được |
|---|---|---|
| R1 | Chỉ dựng nổi **1** báo cáo "Đã gửi TW" | ~~Rủi ro chính~~ → **đã hạ mức**: kiểm kê 11:50 thấy **3 báo cáo `DA_GUI_TW`**, có sẵn cặp cùng đợt/kỳ (§2.2). Chỉ còn rủi ro dữ liệu bị tác nhân khác tiêu thụ ⇒ xác minh lại trước khi đo |
| R2 | **Hai báo cáo nguồn trùng số liệu / toàn `0`** ⇒ phép cộng không phân biệt được | **Đây mới là rủi ro số 1 của phiếu này** sau khi có kiểm kê: ta **không** chọn được giá trị cho dữ liệu seed sẵn. Xử theo §2.2 phương án (a)/(b); không được cả hai ⇒ **C1 Chưa chốt** |
| R3 | [Tổng hợp] bị máy chủ chặn vì trạng thái ĐỢT chưa `DA_GUI_TW` | Ghi nguyên văn mã lỗi + thông điệp ⇒ chuyển thành **bằng chứng GAP** của phiếu 343 §2, verdict **Cần BA + Chưa chốt** |
| R4 | Không có khối [Tổng hợp] trên màn của `cbnv_tw_03` | Chụp màn + xác minh `capDonVi = TW`. Đúng TW mà không có khối ⇒ **Reopen vế C2a** kèm khối `CÁCH VERIFY` |

---

## 6. Độ phủ biến thể — **sàn: 1 lượt bấm [Tổng hợp], bộ chọn ≥2 báo cáo**

| # | Dạng | Bắt buộc? |
|---|---|---|
| **①** | Chọn 2 báo cáo của 2 đơn vị khác nhau (ưu tiên 1 ĐP + 1 BN), **cùng một đợt** | **BẮT BUỘC** |
| ② | Đổi bộ chọn (bỏ 1 báo cáo) để xác nhận tổng đổi theo | Nằm trong **cùng đường đo C1**, không phải biến thể mới |

**KHÔNG mở rộng:** không bấm [Lưu] (phiếu 343) · không xuất tệp (phiếu 345) · không đo lại gửi TW (dòng 342)
· không đo `WRN-XI-09-01` · không chạy mọi tổ hợp biểu mẫu.
