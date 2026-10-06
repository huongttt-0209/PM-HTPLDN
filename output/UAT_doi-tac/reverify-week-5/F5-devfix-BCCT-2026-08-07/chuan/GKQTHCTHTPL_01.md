# Chuẩn chấm đã khóa — GKQTHCTHTPL_01 (dòng 342) — "Gửi kết quả thực hiện chương trình hỗ trợ pháp lý"

> **Đặc tả — nguồn DUY NHẤT của phiếu này:**
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md` (1.610 dòng).
> Mọi số dòng dưới đây do agent này **tự mở file đếm lại ngày 2026-08-07**.
>
> **Không có bug entry QA nội bộ nào cho case này** ở tuần 4 ⇒ **không có khối `── CÁCH VERIFY sau Dev fix ──`**
> để chép. Chuẩn dưới đây dựng thẳng từ SRS.
>
> **Trạng thái phiếu:** vòng 1. Ô `Kết quả verify` (T342) **rỗng**; `Trạng thái dev fix = Fixed`
> (xem `../audit/gia-tri-o-truoc-khi-ghi.md`).

---

## 1. BẢNG SCOPE LOCK — 5 vế của "Kết quả mong đợi" (vế 2 của phiếu là câu ghép ⇒ tách C2a/C2b)

| Vế | Expected đối tác (nguyên văn phiếu) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | "Chuyển trạng thái **đợt báo cáo**: Đã duyệt kết quả → **Đã gửi Trung ương**" | **`:937`** (chính) · `:950` · `:954` · `:967` · `:1516` · nhãn `:1197`,`:1198` | `:937` = `\| 3 \| Chuyển trạng thái đợt BC sang DA_GUI_TW, đánh dấu da_gui_tw, ghi thời điểm gửi \| SM-DOT-BC \|` | **MATCH** | **TEST** | Sau khi bấm [Gửi Trung ương] + Xác nhận, màn chi tiết đợt đọc được "Đã gửi TW" cho chính đơn vị vừa gửi, **giữ sau khi tải lại trang bằng địa chỉ** |
| **C2a** | "**Ghi nhận thời điểm gửi**" | **`:937`** · `:938` · `:1173` | `:938` = `\| 3a \| **Sửa theo STT 52 UAT 2026-05-26:** Cập nhật `DOT_BAO_CAO_DON_VI_NOP[dot_id, don_vi_nop_id].trang_thai_nop = DA_NOP` + `ngay_nop = NOW()`. Tiến độ nộp hiển thị trực tiếp ở chi tiết Đợt BC. \| — \|` | **MATCH** | **TEST** | Màn chi tiết đợt (bảng tiến độ nộp) hiển thị mốc thời gian gửi/nộp của đơn vị, khớp mốc giờ thao tác (lệch ≤ vài phút) |
| **C2b** | "**đánh dấu báo cáo vào danh sách tổng hợp của cấp Trung ương**" | **`:939`** (chính) · `:955` · `:1174` | `:939` = `\| 4 \| BC hiển thị trong danh sách "Tổng hợp" của cấp TW \| — \|` | **MATCH** | **TEST** | Đăng nhập CB NV **cấp TW** → bảng báo cáo từ BN/ĐP đã gửi → có dòng của đúng đơn vị + đúng đợt vừa gửi |
| **C3** | "Gửi thông báo cho **cán bộ nghiệp vụ cấp Trung ương**" | **`:940`** (chính) · `:956` · `:1516` | `:940` = `\| 5 \| Gửi thông báo CB NV TW \| — \|` | **MATCH** | **TEST** | Đăng nhập CB NV cấp TW → chuông thông báo trong hệ thống và/hoặc thư ở MailHog, trỏ đúng đợt + đơn vị |
| **C4** | "Lưu vết thao tác theo quy định" | **`:941`** (chính) · `:1532` · `:1568` | `:941` = `\| 6 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` | **MATCH** | **TEST** | Màn Nhật ký hệ thống (vai trò QTHT) lọc theo mốc giờ gửi → có mục ứng với thao tác của đúng tài khoản |
| **C5** | "Gửi thành công, hệ thống hiển thị thông báo nhanh **«Đã gửi báo cáo lên Trung ương»**" | **`:1173`** (chỉ khai CÓ toast, không khai câu chữ) | `:1173` = `\| 43 \| action-bar \| [DA_DUYET_KQ] Gui len TW (gop tu MH-15.8, BN/DP) \| button + modal \| Modal xac nhan -> SET DA_GUI_TW, da_gui_tw = 1, ngay_gui = NOW. TB CB NV TW. Toast success \| click -> send \|` | **MATCH** (có thông báo thành công) · **GAP** (câu chữ cụ thể) | **TEST** phần "có thông báo" · **BA** phần câu chữ | Ghi nhận có/không có thông báo thành công. **CẤM** chấm Pass/Reopen dựa trên câu chữ |

**Căn cứ khẳng định phần câu chữ của C5 là IM LẶNG (không phải grep rỗng):** đã đọc trọn FR-XI-08
(`:907`–`:968`) — Outputs `:948`–`:950` chỉ khai "Trạng thái đợt BC mới", Postconditions `:952`–`:956`,
Error Handling `:958`–`:963` chỉ có `ERR-XI-08-01`/`-02`, AC `:967` không nhắc thông báo thành công; SRS
**có** khai câu chữ thông báo khi muốn (`:1032` = `\| I1 \| Tổng hợp thành công \| INF-XI-09-01 \| "Đã tổng
hợp báo cáo toàn quốc" \| INFO \|`) ⇒ FR-XI-08 không có mã `INF-XI-08-*` là im lặng có ý nghĩa. Riêng dòng
`:1173` khai chữ **"Toast success"** ⇒ **sự tồn tại** của thông báo thành công là có đặc tả, chấm được.

---

## 2. Vế quyết định verdict vòng này

🔴 **C1 — trạng thái đợt chuyển sang "Đã gửi Trung ương" và đọc lại vẫn giữ.**

Kết quả thực tế của phiếu: **"Forbidden"** ⇒ thao tác bị **chặn**, chưa tới được C2a/C2b/C3/C4/C5.

**🔴 Quy trình bắt buộc khi gặp lại "Forbidden" — phân 4 nhánh TRƯỚC khi kết luận:**

| Nhánh | Dấu hiệu phải chốt bằng bằng chứng | Kết luận |
|---|---|---|
| **(a) Sai cấp đơn vị** | tài khoản đo có `capDonVi = TW` | **ĐÚNG SPEC** — `:918` Tác nhân *"Cán bộ Nghiệp vụ BN/ĐP"*, `:922` *"User thuộc cấp BN hoặc ĐP"*, `:963` `ERR-XI-08-02` *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*. **Cấm log.** Đo lại bằng ĐP/BN |
| **(b) Đợt chưa ở "Đã duyệt kết quả"** | trạng thái trước khi bấm ≠ DA_DUYET_KQ | **ĐÚNG SPEC** — `:923` + `:936` + `:962` `ERR-XI-08-01`. **Thiếu tiền đề**, dựng lại theo §3.3 |
| **(c) Đơn vị ngoài phạm vi nộp** | đơn vị không có trong phạm vi đợt | **ĐÚNG SPEC** — `:717` (tiền đề của cả luồng). **Cấm log**, đổi đợt/đơn vị |
| **(d) Đúng cấp ĐP/BN + đúng đơn vị trong phạm vi + đợt đang ở "Đã duyệt kết quả" mà vẫn bị chặn** | cả 3 điều trên đã chốt bằng ảnh chụp/bản đọc | **BUG — Reopen.** Đây là nhánh duy nhất lật verdict |

> **Ghi nhận riêng (candidate, KHÔNG kéo verdict 5 vế):** nếu hệ thống chặn bằng chuỗi **"Forbidden"** thô
> (tiếng Anh) thay vì thông báo tiếng Việt mà SRS khai ở `:962`/`:963`, ghi thành **mục riêng** trong báo cáo
> — 4xx này tự lộ ngay trong bước bắt buộc của vế đang verify nên được phép ghi candidate; nhưng nó **không**
> phải một trong 5 vế của phiếu ⇒ **không** dùng để chấm Pass/Reopen phiếu này.

> ⚠️ **Bẫy trục trạng thái.** SRS có **HAI** trục: trục **ĐỢT** `DOT_BAO_CAO.trang_thai` (`:1368`, nhãn
> `:1197` = `\| DA_DUYET_KQ \| Da duyet KQ \| Xanh la \|`, `:1198` = `\| DA_GUI_TW \| Da gui TW \| Xanh duong \|`)
> — **C1 nằm ở trục này**; và trục **ĐƠN VỊ** `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop` (`:1389`, giá trị
> `DA_NOP`) — `:938` khai đây là nơi ghi `ngay_nop`, phục vụ **C2a**. Đừng đo lẫn hai trục.

---

## 3. Precondition + công thức dựng tiền đề

### 3.1 Vai trò / tài khoản (env `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025/`)

| Vai trò | Tài khoản | Mật khẩu | Dùng để |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ **ĐP** (đơn vị trong phạm vi nộp) | `cbnv_dp_01` (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | **Bấm [Gửi Trung ương] + đọc lại trạng thái** — tài khoản chốt PASS/FAIL |
| **CB Phê duyệt CÙNG ĐƠN VỊ** | `cbpd_dp_01` — **BẮT BUỘC xác minh `donViId` trùng `cbnv_dp_01`** | `Test@1234` | **CHỈ dựng tiền đề** (duyệt kết quả để đợt lên "Đã duyệt kết quả") |
| **CB Nghiệp vụ cấp TW** | `cbnv_tw_01` (`capDonVi = TW`) | `Test@1234` | Đo **C2b + C3** (danh sách tổng hợp TW + thông báo TW). **KHÔNG** dùng để bấm gửi |
| CB Nghiệp vụ cấp BN (biến thể ②) | `cbnv_bn_01` + `cbpd_bn_01` | `Test@1234` | Phủ nhánh BN của `:918` |
| Đọc nhật ký cho vế C4 | tài khoản QTHT | — | **Chỉ đọc log**, khai rõ |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che đúng loại lỗi mà phiếu đang báo (chặn quyền) |

> ⚠️ `cbnv_dp` **login FAIL** từ 03/08/2026 → `cbnv_dp_01`; `cbpd_tw` FAIL từ 30/07 → `cbpd_tw_01`
> (nhưng case này **không** dùng CB PD cấp TW — `:852`/`:1552` đòi CB PD **cùng đơn vị** với người trình).

### 3.2 Màn / đường dẫn

- Menu **"Đợt báo cáo"** → [Xem] dòng đợt → **chi tiết đợt** (tuần 4 quan sát dạng `/ct-htpldn/dot-bao-cao/{id}`).
- Nút **[Gửi Trung ương]** + hộp thoại xác nhận — điều kiện hiển thị theo `:1173`:
  *"khi dot o DA_DUYET_KQ, user BN/DP"*.
- Màn TW đọc C2b: bảng báo cáo từ BN/ĐP đã gửi — `:1174` = `\| 44 \| content \| [TW] Bang BC tu BN/DP …
  Filter: da_gui_tw = 1. Cot: Checkbox / Don vi / Cap / Ma dot / Ky / Ngay gui / Trang thai / Hanh dong (Xem) \| — \| user TW \|`.
- **Không FAIL vì tiền tố địa chỉ `/ct-htpldn/`** — BA-23 (`:1090`, `:1103`, `:1147`–`:1149`) chỉ đòi màn
  "Đợt báo cáo định kỳ" **độc lập** (đã đạt vì có mục menu riêng); SRS không đặc tả chuỗi địa chỉ.

### 3.3 Tiền đề bắt buộc + công thức dựng

**Nguyên văn `:920`–`:923` (Preconditions FR-XI-08):**
```
:922  - User thuộc cấp BN hoặc ĐP
:923  - BC đã được phê duyệt KQ (đợt BC ở DA_DUYET_KQ)
```

**Chuỗi tiền đề đầy đủ (case này nằm CUỐI chuỗi 3 phiếu — dựng theo đúng thứ tự):**
```
[1] Đợt BC tồn tại + đơn vị của cbnv_dp_01 trong phạm vi nộp        (:717 · :657)
      → nếu chưa có: cbnv_tw_01 tạo đợt kỳ TRON_NAM 2026 (:625, :656/:688 chặn trùng kỳ+năm;
        hai kỳ SO_BO_NAM và SO_BO_6_THANG của 2026 đã có đợt)
[2] cbnv_dp_01 lập báo cáo → trạng thái nộp "Đang lập"               (:746)  ← xem LBCKQTHCT_01.md
[3] cbnv_dp_01 điền ĐỦ mọi chỉ tiêu của biểu mẫu (0 là hợp lệ) → [Trình duyệt KQ]
      → đợt "Chờ duyệt kết quả"                                     (:802 · :803)  ← xem TPDBCKQTHCT_01.md
[4] cbpd_dp_01 (CÙNG ĐƠN VỊ) mở đợt → [Phê duyệt]
      → đợt "Đã duyệt kết quả"                                      (:869 · :901 · :1171)
[5] ĐO CASE NÀY: đăng nhập lại cbnv_dp_01 → [Gửi Trung ương] → Xác nhận
```
Dòng nền cho bước [4]: `:869` = `\| 3 \| Nếu DUYỆT: chuyển đợt BC → DA_DUYET_KQ, BC → DA_DUYET \| SM-DOT-BC \|`;
`:1171` = `\| 41 \| action-bar \| [CHO_DUYET_KQ] Phe duyet BC (gop tu MH-15.7) \| button (primary) + modal \|
[Phe duyet]: SET dot_bc = DA_DUYET_KQ, bc = DA_DUYET. TB CB NV: "Co the gui len TW" \| … \| khi dot o
CHO_DUYET_KQ, user la CB PD cung cap \|`.

**Công thức A — TÁI SỬ DỤNG (ưu tiên).** Nếu lô đo đã chạy xong `LBCKQTHCT_01` + `TPDBCKQTHCT_01` trên một
cặp (đợt, đơn vị) → chỉ cần làm bước [4] rồi [5]. **Không tạo đợt mới.**

**Công thức B — DỰNG TỪ ĐẦU.** Chạy trọn [1]→[5].

**Chốt định danh TRƯỚC khi bấm (bắt buộc ghi vào báo cáo):** `username thực dùng` · `vai trò` · `capDonVi` ·
`mã đơn vị` · `đơn vị CÓ trong phạm vi đợt (bằng chứng đọc được)` · `mã đợt` · `trạng thái đợt ngay trước khi
bấm (phải là "Đã duyệt kết quả")` · `mốc giờ bấm`. **Thiếu bất kỳ mục nào ⇒ không phân được 4 nhánh §2 ⇒
chưa được ra verdict.**

---

## 4. Các bước đo (UI thật)

0. **Ghi dấu vân tay bản dựng** (bó mã FE · `last-modified` · `etag`) + **tải lại trang bằng địa chỉ**;
   đối chiếu `../../BAN-DUNG.md`.
1. Đăng nhập **`cbnv_dp_01`**. Ghi account thực dùng + `capDonVi` + mã đơn vị.
2. Dựng tiền đề theo §3.3. **Chụp màn hình trạng thái đợt TRƯỚC khi bấm** (phải là "Đã duyệt kết quả") +
   bằng chứng đơn vị nằm trong phạm vi nộp.
3. Cài bộ bắt thông báo (**CẤM lọc trùng**, đếm kèm số yêu cầu gửi đi) → bấm **[Gửi Trung ương]** →
   **[Xác nhận]**. Chép **nguyên văn** thông báo/thông điệp lỗi hiện ra + mốc giờ chính xác.
4. **Đo C1 (2 nhịp, bắt buộc cả hai):** đọc trạng thái ngay sau thao tác; rồi **tải lại trang bằng địa chỉ**
   đọc lại. Cả 2 nhịp phải là **"Đã gửi TW"**.
   - Nếu bị chặn ⇒ **dừng, chạy bảng phân 4 nhánh §2**, thu đủ bằng chứng cho từng nhánh rồi mới kết luận.
5. **Đo C2a:** trên bảng tiến độ nộp ở chi tiết đợt, đọc mốc thời gian gửi/nộp của đơn vị mình → so với mốc
   giờ bước 3 (lệch ≤ vài phút).
6. **Đo C2b + C3:** đăng nhập **`cbnv_tw_01`** →
   - C2b: mở bảng báo cáo từ BN/ĐP đã gửi (`:1174`) → phải có dòng của **đúng đơn vị + đúng mã đợt**, kèm
     ngày gửi khớp;
   - C3: kiểm chuông thông báo trong hệ thống + hộp thư MailHog → có thông báo trỏ đúng đợt + đơn vị.
7. **Đo C4:** QTHT → Nhật ký hệ thống → lọc quanh mốc giờ bước 3 → có mục ứng với thao tác gửi của
   `cbnv_dp_01`. Không truy cập được ⇒ **🚫 không đo được**, **KHÔNG** chấm FAIL.
8. **Đường đo thứ hai** — §5.
9. Ghi bảng: `mã đợt | đơn vị | trạng thái trước | ngay sau bấm | sau tải lại | mốc giờ gửi ghi nhận | TW thấy trong DS tổng hợp? | TW nhận TB? | mục nhật ký? | nguyên văn thông báo`.

---

## 5. Đường đo thứ hai (đối chứng độc lập)

**Phương án A — đọc lại bản ghi từ máy chủ bằng chính phiên của `cbnv_dp_01`** (cookie-auth, KHÔNG dùng `admin`).
- 🔴 **Phải tra `/api/docs-json` để lấy đúng đường dẫn — CẤM đoán endpoint.** (`/api/docs-json` đọc được
  không cần đăng nhập.)
- **Manh mối** từ tuần 4 (chỉ để biết tra ở nhóm nào, **không phải căn cứ**): nhóm `.../dot-bao-caos/…`.
- Đối chiếu: bản ghi của **đúng cặp (đợt, đơn vị)** mang trạng thái tương ứng "Đã gửi TW" + có mốc thời gian
  gửi khác rỗng.
- **Nếu bị chặn:** ghi lại **mã lỗi + nguyên văn thông điệp máy chủ trả về** — đây là bằng chứng phân nhánh
  (a)/(b)/(c)/(d) ở §2 mạnh hơn ảnh chụp.

**Phương án B — bằng vai trò TW, không cần API (khuyến nghị chạy CẢ HAI).**
Bước 6 (`cbnv_tw_01` thấy báo cáo trong danh sách tổng hợp) vừa là vế C2b vừa là **đối chứng độc lập cho C1**:
báo cáo chỉ vào danh sách đó khi đã thực sự gửi (`:939` + `:1174` lọc theo cờ đã gửi TW).

**Mâu thuẫn 2 đường** ⇒ ghi **cả hai** vào bug entry, đề xuất BA/dev xem, **không** tự chọn đường có lợi.

---

## 6. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ CẢ 5 điều, trên ≥1 lần gửi THỰC HIỆN MỚI sau bản fix):
   (C1)  Sau khi CB NV cấp ĐP/BN thuộc phạm vi nộp gửi báo cáo đã được duyệt kết quả, trạng thái đợt đọc
         được cho chính đơn vị đó là "Đã gửi TW", và GIỮ NGUYÊN sau khi tải lại trang bằng địa chỉ.
   (C2a) Hệ thống ghi nhận được thời điểm gửi, khớp mốc giờ thao tác.
   (C2b) Cán bộ nghiệp vụ cấp Trung ương thấy báo cáo của đúng đơn vị + đúng đợt trong danh sách tổng hợp.
   (C3)  Cán bộ nghiệp vụ cấp Trung ương nhận được thông báo về báo cáo vừa gửi.
   (C4)  Có mục nhật ký ứng với thao tác gửi, đúng tài khoản, đúng mốc giờ.
   VÀ đúng ở cả hai đường đo (§5). Có thông báo thành công (phần MATCH của C5).

❌ FAIL nếu:
   - Thao tác bị chặn TRONG KHI đã chốt bằng chứng: tài khoản đúng cấp ĐP/BN, đơn vị nằm trong phạm vi nộp,
     đợt đang ở "Đã duyệt kết quả" (nhánh (d) §2);
   - HOẶC trạng thái đổi trên màn rồi quay về "Đã duyệt kết quả" sau khi tải lại trang;
   - HOẶC gửi xong mà cấp Trung ương không thấy báo cáo trong danh sách tổng hợp;
   - HOẶC không ghi nhận thời điểm gửi;
   - HOẶC hai đường đo mâu thuẫn nhau.

⚠️ KHÔNG chấm bằng CÂU CHỮ của C5: SRS chỉ khai CÓ thông báo thành công (:1173), không khai chuỗi
   "Đã gửi báo cáo lên Trung ương".
```

### 6.1 ⚠️ Bẫy chống **FAIL oan**

1. **Kết luận "Forbidden = bug" mà chưa phân 4 nhánh §2.** Đây là bẫy lớn nhất của phiếu này: ba trong bốn
   nhánh là **đúng spec** (`:922`/`:963` sai cấp · `:923`/`:962` sai trạng thái · `:717` ngoài phạm vi).
2. **Đo bằng tài khoản cấp TW.** `:918` Tác nhân = *"Cán bộ Nghiệp vụ BN/ĐP"*; `:1173` điều kiện hiển thị nút
   = *"user BN/DP"*. TW bị chặn = **đúng spec**, cấm log. (Phiếu ghi Tác nhân "Cán bộ nghiệp vụ BN, ĐP" —
   khớp SRS, không có xung đột.)
3. **Bỏ qua bước [4] phê duyệt.** Không có CB PD **cùng đơn vị** duyệt thì đợt không lên "Đã duyệt kết quả"
   ⇒ bị chặn là đúng `:962`. Dùng `cbpd_tw_01` (TW) để duyệt là **sai** — `:852` + `:1552` (BR-AUTH-05:
   *"CB NV cấp nào tạo → CB PD cùng đơn vị duyệt. KHÔNG xuyên cấp phê duyệt"*).
4. **Đo nhầm trục trạng thái** — xem hộp cảnh báo §2.
5. **Câu chữ thông báo lệch** so với *"Đã gửi báo cáo lên Trung ương"* ⇒ phần GAP của C5, **cấm FAIL vì câu chữ**.
6. **Trạng thái nộp của đơn vị không đổi sang "Đã nộp"** — nếu C1 đạt mà nhãn tiến độ nộp chưa đổi, đó là vế
   `:938`; phiếu chỉ nhắc "ghi nhận thời điểm gửi" (C2a) ⇒ chấm theo **mốc thời gian**, không chấm theo nhãn.
7. **Địa chỉ trang có tiền tố `/ct-htpldn/`** — xem §3.2.

### 6.2 ⚠️ Bẫy chống **PASS oan**

1. **Tin vào thông báo thành công.** Phiếu chị em `TPDBCKQTHCT_01` đã dính đúng mẫu "báo thành công nhưng
   trạng thái không đổi" ⇒ bắt buộc nhịp 2 (tải lại trang) + đường đo thứ hai.
2. **Thấy nút [Gửi Trung ương] biến mất rồi kết luận đạt.** Nút ẩn/hiện là hệ quả giao diện.
3. **Đọc danh sách tổng hợp TW bằng `admin`.** Quyền rộng che đúng loại lỗi phiếu đang báo. Bắt buộc dùng
   `cbnv_tw_01`; nếu buộc phải tra định danh bằng `admin` thì khai rõ và đối chứng lại.
4. **Nhìn nhầm dòng cũ trong danh sách TW.** Danh sách có thể còn dòng của các đợt/đơn vị khác. Phải khớp
   **đủ ba**: mã đợt + tên đơn vị + ngày gửi.
5. **Đếm thông báo TW mà không kiểm nội dung.** Thông báo phải trỏ đúng đợt + đơn vị vừa gửi, không phải
   thông báo tồn từ trước.
6. **Bản ghi cũ (dữ liệu đóng băng).** Bản ghi gửi **trước** bản fix mang dữ liệu của bản cũ. **Phép thử
   quyết định = lần gửi THỰC HIỆN MỚI sau bản fix.**
7. **Kết luận trên env sai.** Đối tác quay trên `htpldn-uat.ospgroup.vn`; đợt này đo trên env nội bộ
   `18.143.165.120.nip.io` ⇒ Pass là **Pass tạm** cho bản dựng đo được; bắt buộc ghi câu giới hạn.

### 6.3 ⚠️ Bẫy kỹ thuật khi bắt thông báo

Thông báo tự tắt ~3 giây. Cài bộ bắt **TRƯỚC** khi bấm, **CẤM lọc trùng**, **đếm số yêu cầu gửi đi kèm theo**.
1 thao tác sinh 2 thông báo ⇒ **hồi quy** của `BUG-BC-TOAST-LOI-HIEN-2-LAN` (đóng 28/07): log mục RIÊNG,
**không** trộn vào 5 vế phiếu.

---

## 7. CẦN BA CONFIRM (phần GAP + mâu thuẫn nội bộ)

**(1) Phần câu chữ của vế C5:**

> **CẦN BA CONFIRM:** đối tác kỳ vọng *khi gửi thành công, hệ thống hiển thị thông báo nhanh **"Đã gửi báo
> cáo lên Trung ương"***; SRS quy định **có** thông báo thành công (`srs-fr-15-ct-htpldn.md:1173` — dòng #43
> khai *"Toast success"*) nhưng **IM LẶNG về câu chữ** — FR-XI-08 (`:907`–`:968`) không có mã `INF-XI-08-*`,
> trong khi SRS **có** khai câu chữ ở chỗ khác (`:1032` `INF-XI-09-01` *"Đã tổng hợp báo cáo toàn quốc"*);
> web/dev hiện tại **chờ đo**.
>
> **Câu hỏi BA:** câu chữ thông báo gửi TW có bị ràng buộc đúng chuỗi *"Đã gửi báo cáo lên Trung ương"* như
> phiếu UAT, hay chỉ cần một thông báo thành công bất kỳ? Nếu ràng buộc, xin bổ sung mã `INF-XI-08-*` vào
> FR-XI-08.

**(2) Chỉ gửi nếu phép đo rơi vào nhánh (d) §2 mà thông điệp chặn là chuỗi "Forbidden" thô:**

> **CẦN BA CONFIRM / DEV:** SRS khai hai thông điệp chặn tiếng Việt cho FR-XI-08 — `:962` `ERR-XI-08-01`
> *"Đợt BC chưa được phê duyệt kết quả"* và `:963` `ERR-XI-08-02` *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*.
> Hệ thống trả chuỗi **"Forbidden"** không thuộc hai thông điệp trên ⇒ hoặc chặn sai chỗ, hoặc đúng chỗ
> nhưng chưa gắn thông điệp đã đặc tả. Ghi thành **mục riêng**, không kéo verdict 5 vế.

**(3) Mâu thuẫn mô hình — trạng thái ĐỢT là một giá trị dùng chung cho ~83 đơn vị
(chỉ gửi BA nếu phép đo lộ ra hành vi nhập nhằng, vd đơn vị A gửi TW xong thì đơn vị B cũng đổi nhãn):**

> **CẦN BA CONFIRM:** SRS `:621` + `:646` + `:1398` khai một đợt báo cáo có phạm vi **~70–83 đơn vị nộp**,
> nhưng `DOT_BAO_CAO.trang_thai` (`:1368`) chỉ có **một** giá trị cho cả đợt, trong khi `:937` (FR-XI-08) lại
> chuyển chính trạng thái đó theo thao tác của **từng đơn vị**; `:938` đồng thời khai một trục riêng theo đơn
> vị (`trang_thai_nop = DA_NOP`). **Câu hỏi BA:** trạng thái cán bộ nhìn thấy ở chi tiết đợt là trạng thái
> **của đơn vị mình** hay trạng thái chung của đợt? Nếu là của đơn vị, xin phát biểu lại `:937` cho khớp `:938`.

---

## 8. Độ phủ biến thể

**Sàn: N ≥ 1 lần gửi, dạng ① (CB NV cấp ĐP) — đúng cấu hình đối tác mô tả (`ERR-AUTH-VPD` vòng 1 của phiếu
chị em ghi vai trò `CB_NV_DP`).**

| # | Dạng | Cách dựng | Bắt buộc? |
|---|---|---|---|
| **①** | Đơn vị **ĐP** gửi TW | `cbnv_dp_01` gửi · `cbpd_dp_01` duyệt tiền đề | **BẮT BUỘC** |
| **②** | Đơn vị **BN** gửi TW | `cbnv_bn_01` gửi · `cbpd_bn_01` duyệt tiền đề | **Khuyến nghị** — `:918`/`:922` khai cả BN; bắt buộc nếu ① không dựng được |

**KHÔNG mở rộng:** bước TW tổng hợp (FR-XI-09 `:971`, `:1005`, `:1175`) là chức năng KHÁC, phiếu không nhắc
⇒ **không đo, không kéo verdict**. Nhánh CB PD **từ chối** (`:870`, `:902`) cũng ngoài phạm vi.

---

## 9. Cảnh báo cho agent đo

1. 🔴 **Phân 4 nhánh §2 trước mọi kết luận về "Forbidden".** Đây là điều kiện tiên quyết của verdict phiếu
   này; kết luận mà không có đủ 3 bằng chứng (cấp đơn vị · phạm vi · trạng thái đợt) ⇒ **verdict vô hiệu**.
2. 🔴 **Bước [4] phải do CB PD CÙNG ĐƠN VỊ thực hiện** (`:852`, `:1552`). Duyệt bằng CB PD cấp TW là dựng
   tiền đề sai ⇒ mọi kết quả sau đó vô nghĩa.
3. 🔴 **Đọc và ghi trạng thái đợt TRƯỚC khi bấm** (phải là "Đã duyệt kết quả") + **mốc giờ bấm** (cần cho C2a).
4. 🔴 **Hai nhịp đo C1: ngay sau thao tác + sau khi tải lại trang bằng địa chỉ.**
5. **Ghi dấu vân tay bản dựng + tải lại trang bằng địa chỉ** trước khi đo (đối chiếu `../../BAN-DUNG.md`).
6. **Không dùng `admin` ra verdict**; C2b/C3 phải đo bằng `cbnv_tw_01`.
7. Login fail → **Rule 7**: fallback **cùng vai trò + cùng cấp**, khai account thực dùng; **không** đổi
   ĐP ↔ BN ↔ TW để "cho chạy được" *(ngoại lệ: biến thể ② §8 là nhánh tác nhân mà `:918` cho phép — phải
   khai rõ là dạng ②)*.
8. **Ảnh chụp lưu đúng** `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`.
