# Chuẩn chấm đã khóa — TPDBCKQTHCT_01 (dòng 340) — "Trình phê duyệt báo cáo kết quả thực hiện chương trình"

> **Đặc tả — nguồn DUY NHẤT của phiếu này:**
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md` (1.610 dòng).
> Mọi số dòng dưới đây do agent này **tự mở file đếm lại ngày 2026-08-07**.
>
> **Không có bug entry QA nội bộ nào cho case này** ở tuần 4 (`bug-report-UAT-tuan-4.md` chỉ có 2 entry gắn
> `LBCKQTHCT_01`) ⇒ **không có khối `── CÁCH VERIFY sau Dev fix ──`** để chép. Chuẩn dưới đây dựng thẳng từ SRS.
>
> **Trạng thái phiếu:** vòng 1. Ô `Kết quả verify` (T340) đang **rỗng**; `Trạng thái dev fix = Fixed`
> (xem `../audit/gia-tri-o-truoc-khi-ghi.md`).

---

## 1. BẢNG SCOPE LOCK — 4 vế của "Kết quả mong đợi"

| Vế | Expected đối tác (nguyên văn phiếu) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | "Chuyển trạng thái **đợt báo cáo**: Đang lập báo cáo → **Chờ duyệt kết quả**" | **`:803`** (chính) · `:814` · `:818` · `:829` · `:1513` · nhãn `:1195`,`:1196` | `:803` = `\| 3 \| Chuyển trạng thái BC sang CHO_PHE_DUYET, đợt BC sang CHO_DUYET_KQ \| SM-DOT-BC \|` | **MATCH** | **TEST** | Sau khi bấm [Trình duyệt KQ], màn chi tiết đợt đọc được trạng thái "Chờ duyệt kết quả" cho chính đơn vị vừa trình, và **giữ sau khi tải lại trang bằng địa chỉ** |
| **C2** | "Gửi thông báo cho **cán bộ phê duyệt cùng đơn vị**" | **`:804`** (chính) · `:819` · `:829` · phần "cùng đơn vị": `:852` · `:1552` · `:1171` | `:804` = `\| 4 \| Gửi thông báo CB PD \| — \|`  ·  `:852` = `- CB PD cùng đơn vị với CB NV trình (BR-AUTH-05)` | **MATCH** (chiều thuận) | **TEST** | Đăng nhập CB PD **cùng đơn vị** → có thông báo về báo cáo vừa trình (chuông trong hệ thống và/hoặc thư ở MailHog) |
| **C3** | "Lưu vết thao tác theo quy định" | **`:805`** (chính) · `:1532` · `:1568` | `:805` = `\| 5 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` | **MATCH** | **TEST** | Màn Nhật ký hệ thống (vai trò QTHT) lọc theo mốc giờ vừa trình → có mục ứng với thao tác của đúng tài khoản |
| **C4** | "Trình thành công, hệ thống hiển thị **«Đã trình phê duyệt báo cáo»**" | **IM LẶNG** — gần nhất: `:1170` (dòng #40 SCR-XI-01) · đối chiếu `:1032` · `:1173` | `:1170` = `\| 40 \| action-bar \| [DANG_LAP_BC] Hanh dong lap BC (gop tu MH-15.6) \| button-group (C22) \| [Huy] [Luu nhap] [Trinh duyet KQ] -> validate -> SET CHO_DUYET_KQ + SET bc CHO_PHE_DUYET -> TB CB PD \|` | **GAP** | **BA** | **CẤM Pass/Reopen vế này.** Chỉ ghi nhận nguyên văn thông báo quan sát được |

**Căn cứ khẳng định C4 là IM LẶNG (không phải grep rỗng):** đã đọc trọn FR-XI-07 (`:773`–`:831`) — Outputs
`:812`–`:814` chỉ khai "Trạng thái đợt BC mới", Postconditions `:816`–`:819` chỉ khai chuyển trạng thái +
gửi TB CB PD, Error Handling `:823`–`:825` chỉ có `ERR-XI-07-01`, AC `:829`–`:830` không nhắc thông báo
thành công; đọc trọn khối SCR-XI-01 dòng #35–#45 (`:1165`–`:1175`) — chỉ `:1173` (Gửi TW) khai "Toast success".
SRS **có** khai thông báo thành công khi muốn (`:1032` `INF-XI-09-01`) ⇒ im lặng có ý nghĩa.

**Về phần "cùng đơn vị" của C2:** SRS `:804` chỉ ghi "Gửi thông báo CB PD" (không kèm phạm vi). Ràng buộc
"cùng đơn vị" đứng ở `:852` (điều kiện tiên quyết FR-XI-07a) + `:1552` (BR-AUTH-05: *"CB NV cấp nào tạo →
CB PD cùng đơn vị duyệt. KHÔNG xuyên cấp phê duyệt"*) + `:1171` (điều kiện hiển thị nút Phê duyệt:
*"user la CB PD cung cap"*). ⇒ **Chiều thuận** (CB PD cùng đơn vị phải nhận được) = MATCH, chấm được.
**Chiều nghịch** (không được gửi cho CB PD đơn vị khác) = **GAP — SRS không cấm**, ⇒ **CẤM chấm FAIL** vì
thấy tài khoản khác cũng nhận thông báo; nếu cần chấm chiều đó phải hỏi BA (§7).

---

## 2. Vế quyết định verdict vòng này

🔴 **C1 — trạng thái đợt báo cáo chuyển sang "Chờ duyệt kết quả" và đọc lại vẫn giữ.**

Kết quả thực tế của phiếu: *"Hệ thống không cập nhật trạng thái mặc dù có thông báo trình duyệt thành công."*
⇒ Đây đúng là mẫu **giao diện báo thành công nhưng máy chủ không đổi trạng thái**. C4 (thông báo) theo phiếu
**đã hiện** ⇒ C4 không phải điểm tranh chấp, và dù sao cũng là GAP không chấm được.

- C2, C3 đo đủ nhưng không lật verdict nếu C1 đạt.
- Nếu C1 đạt mà C2 **không** đạt (CB PD cùng đơn vị không nhận được gì) ⇒ vẫn **Reopen**, ghi rõ điểm hỏng
  đã dịch sang vế thông báo.

> ⚠️ **Bẫy trục trạng thái — đọc trước khi đo.** SRS có **HAI** trục:
> - **Trục ĐỢT** — `DOT_BAO_CAO.trang_thai`, enum `:1368` =
>   `CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP')`;
>   bảng nhãn `:1195` = `\| DANG_LAP_BC \| Dang lap BC \| Vang \|`, `:1196` = `\| CHO_DUYET_KQ \| Cho duyet KQ \| Vang dam \|`.
>   **C1 nằm ở trục này.**
> - **Trục ĐƠN VỊ** — `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop`, enum `:1389` cũng có giá trị `CHO_DUYET`.
>
> Ngoài ra `:803` còn khai **trục thứ ba**: bản thân **báo cáo** (`BAO_CAO_CT_HTPL.trang_thai`, enum `:1418` =
> `CHECK IN ('DU_THAO','CHO_PHE_DUYET','DA_DUYET','TU_CHOI')`) chuyển sang `CHO_PHE_DUYET`. Phiếu **chỉ nhắc
> trục ĐỢT** ⇒ chỉ chấm trục đợt; hai trục kia ghi nhận làm bằng chứng bổ trợ, **không** tách thành vế mới.

---

## 3. Precondition + công thức dựng tiền đề

### 3.1 Vai trò / tài khoản (env `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025/`)

| Vai trò | Tài khoản | Mật khẩu | Dùng để |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ đơn vị nộp | `cbnv_dp_01` (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | **Bấm [Trình duyệt KQ] + đọc lại trạng thái** — tài khoản chốt PASS/FAIL |
| **CB Phê duyệt CÙNG ĐƠN VỊ** | `cbpd_dp_01` — **BẮT BUỘC xác minh `donViId` trùng với `cbnv_dp_01` trước khi dùng** | `Test@1234` | Đo vế C2 + làm đối chứng độc lập cho C1 |
| CB Nghiệp vụ cấp TW | `cbnv_tw_01` | `Test@1234` | **CHỈ dựng tiền đề** (tạo đợt mới nếu cần — `:625`) |
| Đối chứng đọc lại không qua API | `cbnv_dp_02` (phải cùng `donViId`) | `Test@1234` | Đường đo thứ hai phương án B |
| Đọc nhật ký cho vế C3 | tài khoản QTHT | — | **Chỉ đọc log**, khai rõ |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che lỗi phạm vi/vai trò |

> ⚠️ `cbnv_dp` (không hậu tố) **login FAIL** từ 03/08/2026 → dùng `cbnv_dp_01` (fallback Rule 7 đúng vai trò
> + đúng cấp). `cbpd_tw` cũng FAIL từ 30/07 → `cbpd_tw_01`; **nhưng case này KHÔNG dùng CB PD cấp TW** —
> `:852` + `:1552` đòi CB PD **cùng đơn vị** với người trình.

### 3.2 Màn / đường dẫn

- Menu **"Đợt báo cáo"** → [Xem] dòng đợt → **chi tiết đợt** (tuần 4 quan sát dạng `/ct-htpldn/dot-bao-cao/{id}`).
- Khi đợt/đơn vị đang lập: khối biểu mẫu hiện **[Làm mới] [Lưu nháp] [Trình duyệt KQ]** (`:1170` khai
  button-group `[Huy] [Luu nhap] [Trinh duyet KQ]`).
- **Không FAIL vì tiền tố địa chỉ `/ct-htpldn/`** — BA-23 (`:1090`, `:1103`, `:1147`–`:1149`) chỉ đòi màn
  "Đợt báo cáo định kỳ" **độc lập**, đã đạt vì có mục menu riêng; SRS không đặc tả chuỗi địa chỉ.

### 3.3 Tiền đề bắt buộc + công thức dựng

**Nguyên văn `:786`–`:789` (Preconditions FR-XI-07):**
```
:788  - BC đã được lập và lưu
:789  - Đợt BC ở trạng thái DANG_LAP_BC
```

**🔴 Tiền đề quan trọng nhất, dễ bị bỏ sót nhất — `:802` (BA chốt 2026-08-06):**
```
| 2 | **Kiểm tra BC hoàn chỉnh** `[BA chốt 2026-08-06]`: đủ toàn bộ chỉ tiêu của biểu mẫu tại
`bieu_mau_su_dung` — `MAU_21A` → 13 chỉ tiêu biểu 21a; `MAU_21B` → theo biểu 21b; `CA_HAI` → cả hai biểu.
Ô để trống là **chưa điền**; giá trị **0 là đã điền** (đơn vị không phát sinh hoạt động trong kỳ vẫn phải
nộp). `nhan_xet` **không** tính vào điều kiện này | — |
```
⇒ **Phải điền ĐỦ mọi chỉ tiêu của biểu mẫu đang áp dụng trước khi bấm [Trình duyệt KQ]** (điền `0` là hợp lệ).
Bấm khi còn ô trống → bị chặn với `ERR-XI-07-01` *"Vui lòng hoàn chỉnh báo cáo trước khi trình"* (`:825`) —
**đó là ĐÚNG SPEC, cấm log thành bug** (`:830` = AC: *"Given báo cáo còn chỉ tiêu bỏ trống When CB NV nhấn
«Trình phê duyệt» Then chặn + báo `ERR-XI-07-01`"*).

**Công thức A — TÁI SỬ DỤNG (ưu tiên).** Case này nối tiếp `LBCKQTHCT_01`. Nếu lô đo đã dựng xong Case 1
trên một cặp (đợt, đơn vị) → **dùng lại chính cặp đó**, không tạo mới:
```
Đăng nhập cbnv_dp_01 → menu "Đợt báo cáo" → mở chi tiết đợt vừa lập BC
  → xác minh: đơn vị mình đang "Đang lập" và biểu mẫu ở chế độ nhập liệu
  → điền ĐỦ mọi chỉ tiêu của biểu mẫu (dùng 0 cho chỉ tiêu không phát sinh)
  → nhận xét: QA-TPD-<YYYYMMDD-HHmm>-trinh-phe-duyet   (ghi lại nguyên văn)
  → [Lưu nháp] → tải lại trang → xác minh số liệu còn nguyên
  → GHI LẠI trạng thái đợt TRƯỚC KHI BẤM (phải là "Đang lập BC") + mốc giờ
  → [Trình duyệt KQ] → xác nhận
```

**Công thức B — DỰNG MỚI (khi A không có).** Chạy trọn công thức B của `LBCKQTHCT_01.md` §3.3 (TW
`cbnv_tw_01` tạo đợt kỳ `TRON_NAM` 2026 — hai kỳ còn lại đã có đợt, `:656`/`:688` chặn trùng kỳ+năm) rồi
quay lại công thức A.

**Chốt định danh TRƯỚC khi bấm (bắt buộc ghi vào báo cáo):** `username thực dùng` · `capDonVi` · `mã đơn vị` ·
`mã đợt` · `biểu mẫu đang áp dụng` · `số chỉ tiêu đã điền / tổng chỉ tiêu` · `trạng thái đợt trước khi bấm` ·
`mốc giờ bấm`. **`cbpd_dp_01` phải được xác minh cùng `donViId`** — nếu khác đơn vị thì C2 không đo được bằng
tài khoản đó (đổi sang `cbpd_dp_02`/`_03` **cùng cấp ĐP**, hoặc khai 🚫 không đo được).

---

## 4. Các bước đo (UI thật)

0. **Ghi dấu vân tay bản dựng** (bó mã FE · `last-modified` · `etag`) + **tải lại trang bằng địa chỉ**;
   đối chiếu `../../BAN-DUNG.md`, ghi rõ nếu lệch.
1. Đăng nhập **`cbnv_dp_01`**. Ghi account thực dùng.
2. Dựng tiền đề theo §3.3 công thức A/B. **Chụp màn hình trạng thái đợt TRƯỚC khi bấm** (phải là
   "Đang lập BC") + ghi số chỉ tiêu đã điền.
3. Cài bộ bắt thông báo (**CẤM lọc trùng**, đếm kèm số yêu cầu gửi đi) → bấm **[Trình duyệt KQ]** → xác nhận.
   Chép **nguyên văn** thông báo hiện ra (phục vụ C4 — chỉ ghi nhận).
4. **Đo C1 (2 nhịp, bắt buộc cả hai):**
   - nhịp 1: đọc trạng thái ngay sau thao tác;
   - nhịp 2: **tải lại trang bằng địa chỉ** rồi đọc lại.
   Cả 2 nhịp phải là **"Chờ duyệt kết quả"**. Ghi nhận bổ trợ (không phải vế chấm): trạng thái nộp của đơn vị
   và trạng thái của bản báo cáo.
5. **Đo C2:** đăng nhập **`cbpd_dp_01`** (đã xác minh cùng đơn vị) → kiểm chuông thông báo trong hệ thống +
   hộp thư MailHog `http://18.143.165.120:8025/` → phải có thông báo về báo cáo vừa trình, trỏ đúng đợt/đơn vị.
   **Đồng thời** đây là đối chứng độc lập cho C1: màn của CB PD phải thấy báo cáo đang chờ duyệt.
6. **Đo C3:** QTHT → Nhật ký hệ thống → lọc quanh mốc giờ bước 3 → có mục ứng với thao tác trình của
   `cbnv_dp_01`. Không truy cập được ⇒ **🚫 không đo được**, **KHÔNG** chấm FAIL.
7. **Đường đo thứ hai** — §5.
8. Ghi bảng: `mã đợt | đơn vị | chỉ tiêu đã điền/tổng | trạng thái trước | ngay sau bấm | sau tải lại | CB PD nhận TB? | mục nhật ký?`.

---

## 5. Đường đo thứ hai (đối chứng độc lập)

**Phương án A — đọc lại bản ghi từ máy chủ bằng chính phiên của `cbnv_dp_01`** (cookie-auth, KHÔNG dùng `admin`).
- 🔴 **Phải tra `/api/docs-json` để lấy đúng đường dẫn — CẤM đoán endpoint.** (`/api/docs-json` đọc được
  không cần đăng nhập.)
- **Manh mối** từ tuần 4 (chỉ để biết tra ở nhóm nào, **không phải căn cứ**): nhóm `.../dot-bao-caos/…`
  (tuần 4 đã thấy `POST …/dot-bao-caos/{id}/start`).
- Đối chiếu: bản ghi của **đúng cặp (đợt, đơn vị)** mang trạng thái tương ứng "Chờ duyệt kết quả".

**Phương án B — bằng tài khoản khác, không cần API (khuyến nghị chạy CẢ HAI).**
`cbpd_dp_01` (bước 5) thấy báo cáo ở danh sách chờ duyệt, **hoặc** `cbnv_dp_02` cùng đơn vị mở cùng đợt thấy
cùng trạng thái ⇒ chứng minh trạng thái nằm ở máy chủ chứ không phải chỉ đổi trên phiên đang mở.

**Mâu thuẫn 2 đường** ⇒ ghi **cả hai** vào bug entry, đề xuất BA/dev xem, **không** tự chọn đường có lợi.

---

## 6. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ CẢ 3 điều, trên ≥1 lần trình THỰC HIỆN MỚI sau bản fix):
   (C1) Sau khi CB NV của đơn vị nộp trình báo cáo đã điền đủ chỉ tiêu, trạng thái đợt báo cáo đọc được cho
        chính đơn vị đó là "Chờ duyệt kết quả", và GIỮ NGUYÊN sau khi tải lại trang bằng địa chỉ.
   (C2) CB Phê duyệt cùng đơn vị nhận được thông báo về báo cáo vừa trình.
   (C3) Có mục nhật ký ứng với thao tác trình, đúng tài khoản, đúng mốc giờ.
   VÀ đúng ở cả hai đường đo (§5).

❌ FAIL nếu:
   - Trạng thái không đổi, hoặc đổi trên màn rồi quay về "Đang lập BC" sau khi tải lại trang
     (đây chính là triệu chứng phiếu mô tả: có thông báo thành công nhưng trạng thái không cập nhật);
   - HOẶC thao tác bị từ chối trong khi báo cáo ĐÃ điền đủ mọi chỉ tiêu của biểu mẫu đang áp dụng
     (chốt bằng ảnh chụp số ô đã điền, không phải suy đoán);
   - HOẶC CB PD cùng đơn vị không nhận được thông báo nào;
   - HOẶC hai đường đo mâu thuẫn nhau.

⚠️ KHÔNG chấm bằng vế C4: SRS im lặng về việc có/không có và câu chữ thông báo thành công (§1).
```

### 6.1 ⚠️ Bẫy chống **FAIL oan**

1. **Bấm khi báo cáo còn ô trống.** `:802` định nghĩa "hoàn chỉnh" = **đủ toàn bộ chỉ tiêu**; `:825` +
   `:830` khai rõ hệ thống **phải chặn**. Bị chặn vì thiếu chỉ tiêu = **đúng spec**, cấm log. Phải chụp bằng
   chứng đã điền đủ (kể cả các ô `0`) trước khi kết luận bị chặn sai.
2. **Nhầm `nhan_xet` là chỉ tiêu bắt buộc.** `:802` ghi rõ *"`nhan_xet` **không** tính vào điều kiện này"* —
   bỏ trống nhận xét mà vẫn trình được là **đúng spec**.
3. **Đo nhầm trục trạng thái.** Xem hộp cảnh báo §2. Đọc nhãn trạng thái nộp của đơn vị (trục `:1389`) hoặc
   nhãn của bản báo cáo (trục `:1418`) rồi kết luận "đợt không chuyển" = **FAIL oan**.
4. **Đo bằng tài khoản sai vai trò.** `:784` khai Tác nhân FR-XI-07 là **Cán bộ Nghiệp vụ**. Bấm bằng tài
   khoản CB Phê duyệt rồi bị chặn = đúng spec.
5. **CB PD khác đơn vị không thấy báo cáo.** `:852` + `:1552` (BR-AUTH-05) đòi **cùng đơn vị**. Dùng
   `cbpd_tw_01` (TW) rồi không thấy gì ⇒ **đúng spec**, cấm log — và cũng **không** dùng để chấm C2.
6. **Câu chữ thông báo lệch** so với *"Đã trình phê duyệt báo cáo"* ⇒ vế C4 là GAP, **cấm FAIL vì câu chữ**.
7. **Địa chỉ trang có tiền tố `/ct-htpldn/`** — xem §3.2.

### 6.2 ⚠️ Bẫy chống **PASS oan**

1. **Tin vào thông báo thành công.** Đây là **đúng triệu chứng phiếu báo**: *"có thông báo trình duyệt thành
   công"* nhưng trạng thái không đổi. **Thông báo KHÔNG phải bằng chứng của C1.** Bắt buộc nhịp 2 (tải lại
   trang) + đường đo thứ hai.
2. **Đọc trạng thái từ tab mở lâu.** Giao diện có thể giữ dữ liệu cũ trong bộ nhớ; **tải lại bằng địa chỉ**,
   không chỉ bấm qua lại giữa các mục menu.
3. **Thấy nút [Trình duyệt KQ] biến mất rồi kết luận đạt.** Nút ẩn/hiện là hệ quả giao diện; C1 hỏi
   **trạng thái đọc lại được**.
4. **Đếm thông báo của CB PD mà không kiểm nội dung.** Thông báo phải trỏ đúng đợt + đúng đơn vị vừa trình,
   không phải thông báo tồn từ đợt cũ. Dùng chuỗi mốc-giờ + đối chiếu thời điểm.
5. **Dùng `admin` để đọc trạng thái.** Quyền rộng che lỗi phạm vi — `admin` chỉ tra định danh, phải khai rõ
   và đối chứng lại bằng `cbnv_dp_01`.
6. **Bản ghi cũ (dữ liệu đóng băng).** Báo cáo trình **trước** bản fix mang trạng thái của bản cũ. **Phép thử
   quyết định = lần trình THỰC HIỆN MỚI sau bản fix.**
7. **Kết luận trên env sai.** Đối tác quay trên `htpldn-uat.ospgroup.vn`; đợt này đo trên env nội bộ
   `18.143.165.120.nip.io` ⇒ Pass là **Pass tạm** cho bản dựng đo được; bắt buộc ghi câu giới hạn.

### 6.3 ⚠️ Bẫy kỹ thuật khi bắt thông báo

Thông báo tự tắt ~3 giây. Cài bộ bắt **TRƯỚC** khi bấm, **CẤM lọc trùng**, luôn **đếm số yêu cầu gửi đi kèm
theo**. Nếu 1 thao tác sinh 2 thông báo ⇒ **hồi quy** của `BUG-BC-TOAST-LOI-HIEN-2-LAN` (đóng 28/07): log
mục RIÊNG, ghi rõ "hồi quy so với bản 28/07", **không** trộn vào 4 vế phiếu.

---

## 7. CẦN BA CONFIRM (vế GAP + mâu thuẫn nội bộ)

**(1) Vế C4 — thông báo khi trình phê duyệt:**

> **CẦN BA CONFIRM:** đối tác kỳ vọng *khi trình thành công, hệ thống hiển thị **"Đã trình phê duyệt báo
> cáo"***; SRS quy định **IM LẶNG** — FR-XI-07 (`srs-fr-15-ct-htpldn.md:773`–`:831`) không có mã `INF-XI-07-*`,
> Outputs `:814` chỉ khai trạng thái đợt mới, AC `:829`–`:830` không nhắc thông báo; dòng SCR `:1170` chỉ khai
> `[Trinh duyet KQ] -> validate -> SET CHO_DUYET_KQ + SET bc CHO_PHE_DUYET -> TB CB PD`; trong khi SRS **có**
> khai thông báo thành công ở chỗ khác (`:1032` `INF-XI-09-01`; `:1173` "Toast success"); web/dev hiện tại
> **chờ đo** (phiếu ghi nhận đã có thông báo thành công).
>
> **Câu hỏi BA:** (a) Thao tác Trình phê duyệt có bắt buộc phản hồi thành công cho người dùng không?
> (b) Nếu có, câu chữ có bị ràng buộc đúng chuỗi *"Đã trình phê duyệt báo cáo"* không? (c) Nếu bắt buộc, xin
> bổ sung mã `INF-XI-07-*` vào FR-XI-07.

**(2) Chiều nghịch của C2 — phạm vi người nhận thông báo (chỉ hỏi nếu phép đo lộ ra CB PD ngoài đơn vị cũng nhận):**

> **CẦN BA CONFIRM:** đối tác kỳ vọng thông báo gửi cho **cán bộ phê duyệt cùng đơn vị**; SRS quy định
> `:804` chỉ ghi *"Gửi thông báo CB PD"* **không kèm phạm vi**, ràng buộc "cùng đơn vị" chỉ xuất hiện ở
> `:852` (điều kiện được phê duyệt) và `:1552` (BR-AUTH-05); web/dev hiện tại **chờ đo**.
> **Câu hỏi BA:** thông báo trình duyệt có **bị giới hạn** chỉ CB PD cùng đơn vị, hay được phép gửi rộng hơn
> (vd cả CB PD cấp trên) miễn là CB PD cùng đơn vị chắc chắn nhận được?

**(3) Mâu thuẫn mô hình — trạng thái ĐỢT là một giá trị dùng chung cho ~83 đơn vị
(chỉ gửi BA nếu phép đo lộ ra hành vi nhập nhằng, vd đơn vị A trình xong thì đơn vị B cũng đổi nhãn):**

> **CẦN BA CONFIRM:** SRS `:621` + `:646` + `:1398` khai một đợt báo cáo do TW phát hành có phạm vi **~70–83
> đơn vị nộp**, nhưng `DOT_BAO_CAO.trang_thai` (`:1368`) chỉ có **một** giá trị cho cả đợt, trong khi `:803`
> (FR-XI-07) và `:937` (FR-XI-08) lại chuyển chính trạng thái đó theo **thao tác của từng đơn vị**. Hai điều
> này không thể cùng đúng khi hai đơn vị ở hai bước khác nhau. `:1389` có sẵn trục theo đơn vị
> (`trang_thai_nop` gồm cả `CHO_DUYET`, `DA_DUYET`) nhưng **không FR nào khai bước cập nhật hai giá trị này**.
> **Câu hỏi BA:** trạng thái mà cán bộ nhìn thấy ở chi tiết đợt phải là trạng thái **của đơn vị mình** hay
> trạng thái chung của đợt? Nếu là của đơn vị, xin bổ sung bước cập nhật `trang_thai_nop → CHO_DUYET` vào
> FR-XI-07 Processing (hiện `:803` chỉ nhắc trục đợt + trục báo cáo).
>
> ⚠️ **Hệ quả cho phép đo:** **KHÔNG** chấm FAIL chỉ vì trạng thái nộp của đơn vị vẫn là "Đang lập" sau khi
> trình — **không dòng SRS nào** đòi trục đơn vị đổi ở bước này.

---

## 8. Độ phủ biến thể

**Sàn: N ≥ 1 lần trình, dạng ① (CB NV cấp ĐP) — đúng cấu hình đối tác mô tả.**

| # | Dạng | Cách dựng | Bắt buộc? |
|---|---|---|---|
| **①** | CB NV **ĐP** trình, CB PD **ĐP cùng đơn vị** nhận | `cbnv_dp_01` + `cbpd_dp_01` | **BẮT BUỘC** |
| **②** | CB NV **BN** trình, CB PD **BN cùng đơn vị** nhận | `cbnv_bn_01` + `cbpd_bn_01` | Chỉ khi ① không dựng được, hoặc để tăng độ tin |

**KHÔNG mở rộng:** nhánh **từ chối** của CB PD (FR-XI-07a `:834`, `:870`, `:902`) là chức năng KHÁC, phiếu
không nhắc ⇒ **không đo, không kéo verdict**. Biểu mẫu 21a vs 21b: phiếu không nhắc ⇒ đo 1 biểu mẫu là đủ.

---

## 9. Cảnh báo cho agent đo

1. 🔴 **Điền ĐỦ mọi chỉ tiêu trước khi bấm (điền `0` là hợp lệ).** Bỏ qua bước này thì kết quả bị chặn là
   đúng spec ⇒ **verdict vô hiệu**. Chụp bằng chứng số ô đã điền.
2. 🔴 **Đọc và ghi trạng thái đợt TRƯỚC khi bấm.** Không có mốc "trước" thì không chứng minh được "đã chuyển".
3. 🔴 **Hai nhịp đo C1: ngay sau thao tác + sau khi tải lại trang bằng địa chỉ.** Bỏ nhịp 2 = Pass oan đúng
   kiểu phiếu đang báo.
4. **Xác minh `cbpd_dp_01` cùng `donViId` với `cbnv_dp_01`** trước khi dùng để đo C2; khác đơn vị ⇒ đổi
   `cbpd_dp_02`/`_03` **cùng cấp ĐP**, hoặc khai 🚫 không đo được C2.
5. **Ghi dấu vân tay bản dựng + tải lại trang bằng địa chỉ** trước khi đo (đối chiếu `../../BAN-DUNG.md`).
6. **Không dùng `admin` ra verdict.**
7. Login fail → **Rule 7**: fallback **cùng vai trò + cùng cấp**, khai account thực dùng; **không** đổi
   ĐP ↔ BN ↔ TW để "cho chạy được".
8. **Ảnh chụp lưu đúng** `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`.
