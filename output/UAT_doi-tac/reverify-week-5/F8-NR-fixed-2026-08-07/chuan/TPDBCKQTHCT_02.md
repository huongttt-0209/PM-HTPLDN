# Chuẩn chấm đã khóa — TPDBCKQTHCT_02 (dòng 341) — "Báo cáo chưa đầy đủ → bấm Trình phê duyệt"

> **Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> (1.610 dòng). **Mọi số dòng dưới đây do agent này tự mở file đếm lại ngày 2026-08-07.**
> Không lấy số dòng từ `input/srs-update-2026-5-5/`, từ thư BA, từ hồ sơ lô F5.
>
> **Trạng thái phiếu:** đối tác **CHƯA TỪNG CHẠY** — `Trạng thái` (N) = `N/R`, `Kết quả thực tế` (L) RỖNG,
> `Ảnh/vieo 1` (M) RỖNG ⇒ **`expected đối tác` = nguyên văn cột `Kết quả mong đợi` (K)**, không có triệu
> chứng cũ để đối chiếu. Không có bug entry QA nội bộ ⇒ không có khối `CÁCH VERIFY` để chép.
>
> **Cổng bằng chứng (flow 04):** không có ảnh đối tác ⇒ rơi nhánh *"Thiếu bằng chứng nhưng tự tái hiện được
> → chạy tiếp và ghi điều kiện đã tái hiện"*. **CẤM kết luận "không phải lỗi" chỉ vì không có bằng chứng.**

**Expected đối tác (nguyên văn K341):**
```
Hệ thống hiển thị "Vui lòng hoàn chỉnh báo cáo trước khi trình".
```

---

## 1. BẢNG SCOPE LOCK — 2 vế

| Vế | Expected đối tác (nguyên văn) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|---|
| **C1** | "Hệ thống hiển thị…" ⇒ hàm ý **chặn thao tác** khi báo cáo chưa đầy đủ (điều kiện phiếu H341 = *"Báo cáo chưa đầy đủ"*) | **`:830`** (chính) · `:825` · `:802` · `:1170` | `:830` = `- **Given** báo cáo còn chỉ tiêu bỏ trống **When** CB NV nhấn "Trình phê duyệt" **Then** chặn + báo `ERR-XI-07-01`` | **MATCH** | **TEST** | **UI:** bấm [Trình duyệt KQ] trên báo cáo còn chỉ tiêu bỏ trống → thao tác không đi lọt. **Đối chứng độc lập:** đọc lại bản ghi (đợt + báo cáo + trạng thái nộp của đơn vị) sau thao tác — cả ba trục **không đổi** |
| **C2** | *"hiển thị **«Vui lòng hoàn chỉnh báo cáo trước khi trình»**"* | **`:825`** (chính) · `:830` | `:825` = `\| E1 \| BC chưa hoàn chỉnh \| ERR-XI-07-01 \| "Vui lòng hoàn chỉnh báo cáo trước khi trình" \| ERROR \|` | **MATCH** (kể cả câu chữ) | **TEST** | **UI:** bộ bắt thông báo cài **TRƯỚC** khi bấm, **CẤM lọc trùng**, đọc bằng `innerText` → chuỗi người dùng nhìn thấy. **Đối chứng độc lập:** nội dung `message` trong phản hồi máy chủ của chính lượt bấm đó |

### 1.1 🔴 Trả lời dứt điểm câu hỏi "chấm theo hành vi hay theo đúng chuỗi chữ?"

**Chấm được CẢ HAI — và ở phiếu này, chuỗi chữ CÓ đặc tả.**

Khác hẳn hai phiếu chị em ở lô F5:
- FR-XI-07 **thông báo THÀNH CÔNG**: SRS **im lặng** (không có mã `INF-XI-07-*`) ⇒ lô F5 phải để GAP.
- FR-XI-08 **thông báo THÀNH CÔNG**: SRS chỉ khai *"Toast success"* (`:1173`), im lặng về câu chữ ⇒ GAP.
- FR-XI-07 **thông báo LỖI khi BC chưa hoàn chỉnh**: SRS **khai nguyên văn chuỗi** ở `:825`, cột "Phản hồi
  hệ thống" = `"Vui lòng hoàn chỉnh báo cáo trước khi trình"` — **trùng khít từng chữ** với expected đối tác.

⇒ Quan hệ **MATCH cả hai vế**. Được chấm Pass/Reopen bằng phép đo.

### 1.2 🔴 Mã lỗi KHÔNG phải vế chấm — cấm biến thành lý do FAIL

`:825` khai mã `ERR-XI-07-01`. Lô F5 đo được hệ thống trả `ERR-VAL-XI-07-02` (câu chữ thì khớp).
**Phiếu 341 không nhắc mã lỗi** ⇒ theo BUG SCOPE LOCK luật 1 (*"tách đúng các vế trong expected đối tác,
không thêm chức năng kế bên"*), mã lỗi **không thành tiêu chí chấm**. Ghi nhận vào mục "gửi dev", không
kéo verdict. *(Mục này đã có ở bàn giao F5 §4 mục 2 — liên kết, không mở phiếu mới.)*

### 1.3 Căn cứ khẳng định đã đọc trọn mục (không phải grep rỗng)

Đã đọc trọn FR-XI-07 `:773`–`:831`: Mô tả `:782`, Tác nhân `:784`, Preconditions `:786`–`:789`,
Inputs `:791`–`:795`, Processing `:797`–`:805`, Outputs `:810`–`:814`, Postconditions `:816`–`:819`,
Error Handling `:821`–`:825` (**chỉ một dòng lỗi E1**), AC `:827`–`:830`. Đọc trọn khối SCR
"Chi tiet Dot BC" `:1161`–`:1175` (dòng #35–#45) và bảng nhãn trạng thái SM-DOT-BC `:1190`–`:1199`.
Không có dấu `[STT…]` / `[CR-…]` nào khác đụng vào câu chữ thông báo lỗi này ngoài `[BA chốt 2026-08-06]`
ở `:802`.

---

## 2. Định nghĩa "báo cáo chưa đầy đủ" — nguyên văn đặc tả

```
:802  | 2 | **Kiểm tra BC hoàn chỉnh** `[BA chốt 2026-08-06]`: đủ toàn bộ chỉ tiêu của biểu mẫu tại
      `bieu_mau_su_dung` — `MAU_21A` → 13 chỉ tiêu biểu 21a; `MAU_21B` → theo biểu 21b; `CA_HAI` → cả
      hai biểu. Ô để trống là **chưa điền**; giá trị **0 là đã điền** (đơn vị không phát sinh hoạt động
      trong kỳ vẫn phải nộp). `nhan_xet` **không** tính vào điều kiện này | — |
```

⇒ **"Chưa đầy đủ" = còn ≥1 chỉ tiêu của biểu mẫu đang áp dụng ở trạng thái Ô TRỐNG.**
- Giá trị `0` **KHÔNG** phải "chưa đầy đủ".
- Bỏ trống **Nhận xét, kiến nghị** **KHÔNG** phải "chưa đầy đủ".
- Với `MAU_21A` → mốc là **13 chỉ tiêu**; `MAU_21B` → theo biểu 21b; `CA_HAI` → cả hai biểu.

---

## 3. Tiền đề tối thiểu

### 3.1 Tài khoản (env `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025/`)

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ đơn vị nộp (ĐP **hoặc** BN) | **`cbnv_dp_03`** (ưu tiên) hoặc `cbnv_bn_03` · `Test@1234` | **Bấm [Trình duyệt KQ] bằng giao diện thật** — tài khoản chốt PASS/FAIL |
| Dựng đợt mới (chỉ khi không tái sử dụng được) | `cbnv_tw_03` · `Test@1234` | **CHỈ dựng tiền đề** — `:625` chỉ CB NV cấp TW được tạo đợt |
| **CẤM ra verdict** | `admin` | Quyền rộng che lỗi phạm vi/vai trò. Chỉ tra định danh, phải khai rõ |

- Tác nhân đúng theo `:784` = *"Cán bộ Nghiệp vụ"*; hẹp hơn ở khâu lập BC `:712` = **CB NV cấp ĐP/BN**
  ⇒ **KHÔNG** bấm bằng tài khoản cấp TW, **KHÔNG** bấm bằng CB Phê duyệt.
- Login fail → Rule 7: fallback **cùng vai trò + cùng cấp** (`_04`, `_05`), **khai account thực dùng**.
  CẤM đổi ĐP ↔ BN ↔ TW để "cho chạy được" *(đổi ĐP ↔ BN chỉ hợp lệ khi khai rõ là biến thể §7, vì `:712`
  cho phép cả hai — nhưng phải giữ nguyên một cặp (đợt, đơn vị) xuyên suốt phép đo)*.

### 3.2 Màn / đường đi

Menu **"Đợt báo cáo"** → [Xem] dòng đợt → **chi tiết đợt** (tuần 4 quan sát dạng `/ct-htpldn/dot-bao-cao/{id}`)
→ nút **[Lập báo cáo]** (nếu đơn vị còn "Chưa nộp") → biểu mẫu chuyển sang chế độ nhập, hiện nhóm nút
**[Làm mới] [Lưu nháp] [Trình duyệt KQ]** (`:1170` khai button-group `[Huy] [Luu nhap] [Trinh duyet KQ]`).

### 3.3 Trạng thái dữ liệu bắt buộc — nguyên văn `:788`–`:789`

```
:788  - BC đã được lập và lưu
:789  - Đợt BC ở trạng thái DANG_LAP_BC
```

**Bước 0 — KIỂM KÊ TRƯỚC KHI DỰNG (bắt buộc, không được bỏ).** Đăng nhập `cbnv_dp_03`, mở từng đợt trong
menu "Đợt báo cáo", ghi bảng: `mã đợt | biểu mẫu đang áp dụng | trạng thái nộp của đơn vị mình | đã có báo
cáo chưa | chỉ tiêu nào đang trống`. Chỉ dựng phần còn thiếu.

> 🟢 **TIỀN ĐỀ ĐANG SẴN SÀNG — nhiều khả năng KHÔNG phải dựng gì.** Lượt trinh sát chỉ-đọc 11:33–11:50
> ngày 2026-08-07 ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2) đọc được **2 báo cáo `DU_THAO`
> của chính `cbnv_dp_03`** (Sở Tư pháp An Giang), mỗi bản chỉ có **3 khóa số liệu**
> (`soVuViec` · `tongChiPhi` · `soDnDuocHoTro`) trong khi `submit-bc` đòi **13 chỉ tiêu Biểu 21a/21b**:
>
> | `baoCaoId` | Đợt | Trạng thái nộp của đơn vị | Có `_links.submit-bc` |
> |---|---|---|---|
> | `c1b1045d-007c-4104-a169-e267010557a0` | `DOT-SO_BO_NAM-2026-1` | `DANG_LAP` | có |
> | `f445b699-04bd-4c94-ab77-9ca118c78dd0` | `DOT-SO_BO_6_THANG-2026-1` | `DANG_LAP` | có |
>
> ⇒ Đây đúng là hình thái **TĐ-B** (báo cáo thiếu chỉ tiêu, chưa từng điền đủ), có sẵn **2 bản dự phòng**.
> Nghĩa là phiếu này gần như chắc chắn đo được, và **được đo lại nhiều lượt** (bấm bị chặn ⇒ dữ liệu không
> đổi ⇒ tiền đề không bị tiêu hủy).
>
> ⚠️ **MANH MỐI, KHÔNG PHẢI CHUẨN CHẤM** — và môi trường dùng chung **có thể đã đổi**. Bắt buộc mở lại màn
> và xác minh trạng thái ngay trước khi bấm; nếu đã khác, quay về TĐ-A/TĐ-C.
>
> ⚠️ **3 khóa này KHÔNG nằm trong 13 khóa Biểu 21a** (`kpXaHoiHoa` · `kpHoTroTvpl` · `soHsTiepNhan` ·
> `soCuocTapHuan` · `soTvvKienToan` · `kpHoatDongKhac` · `soVBTraLoiUBND` · `hsDoanhNghiepNho` ·
> `hsDoanhNghiepVua` · `soHoiNghiDoiThoai` · `soHsGiaiQuyetTong` · `soVBTvMangLuoiTVV` ·
> `hsDoanhNghiepSieuNho`) ⇒ báo cáo **thiếu cả 13**, tức "chưa đầy đủ" theo đúng nghĩa `:802`. Nhưng vì
> **không** phải "điền 12 thiếu 1", vẫn phải áp nguyên **lời khai bắt buộc của TĐ-B** ở đoạn dưới.

**Tiền đề TĐ-A — ƯU TIÊN, sạch nhất (chỉ tiêu CÓ ô nhập đang để trống).** Nếu 2 bản ghi ở khung trên còn
nguyên, hãy **áp TĐ-A lên chính một trong hai bản đó** (mở ra, điền các ô nhập hiện có nhưng chừa ≥1 ô
trống) — vừa được hình thái sạch nhất, vừa khỏi dựng đợt mới:
```
cbnv_dp_03 → menu "Đợt báo cáo" → mở chi tiết một đợt mà đơn vị mình ở "Chưa nộp" / "Đang lập"
  → nếu còn "Chưa nộp": bấm [Lập báo cáo] → [Đồng ý]  (đưa đơn vị về "Đang lập")
  → điền các chỉ tiêu CÓ ô nhập, NHƯNG CỐ Ý ĐỂ TRỐNG ít nhất 1 ô  (vd điền ô 12, xóa trắng ô 13)
  → ghi chuỗi mốc-giờ vào ô Ghi chú: QA-F8-341-<YYYYMMDD-HHmm>
  → [Lưu nháp] → TẢI LẠI TRANG BẰNG ĐỊA CHỈ → xác minh ô đó VẪN TRỐNG trong dữ liệu đã lưu
  → CHỤP MÀN bảng chỉ tiêu (bằng chứng "chưa đầy đủ") + ghi trạng thái đợt/đơn vị TRƯỚC KHI BẤM
  → [Trình duyệt KQ] → [Đồng ý]
```

**Tiền đề TĐ-B — DỰ PHÒNG (khi giao diện không cho lưu ô trống, vd tự điền `0`):** dùng báo cáo **vừa lập,
chưa nhập gì**. Bắt buộc **khai rõ trong báo cáo đo**: bao nhiêu khóa số liệu thực sự có trong dữ liệu đã
lưu (đọc lại bản ghi), và danh sách chỉ tiêu "còn thiếu" mà hệ thống liệt kê **bao gồm cả nhóm chỉ tiêu
không có ô nhập** — điểm hỏng này đang mở ở **dòng 340 (`TPDBCKQTHCT_01`, verdict Reopen của lô F5)**.
⇒ Verdict của phiếu 341 khi đó **chỉ nói về việc chặn + câu chữ thông báo**, **không** kết luận gì về tính
đúng của danh sách chỉ tiêu thiếu.

**Tiền đề TĐ-C — DỰNG ĐỢT MỚI (khi không còn cặp (đợt, đơn vị) nào dùng được):** `cbnv_tw_03` tạo đợt mới —
`:637` mã đợt auto, `:640` kỳ, `:641` hạn nộp, `:642`/`:643` khoảng thời gian, `:645` biểu mẫu, `:646` phạm
vi đơn vị nộp (giữ mặc định, **xác minh có đơn vị của `cbnv_dp_03`**). `:657` khai hệ thống auto-sinh bản
ghi nộp `CHUA_NOP` cho từng đơn vị.
> ⚠️ **Trùng kỳ + năm bị chặn là ĐÚNG SPEC, đừng log:** `:656` = `\| 5 \| Kiểm tra không trùng đợt (cùng
> `ky_bao_cao` + năm) \| — \|`; `:688` = `\| E2 \| Đợt BC trùng kỳ + năm \| ERR-XI-05a-02 \| "Đã tồn tại đợt
> báo cáo cho kỳ '{ky}' năm {YYYY}" \| ERROR \|`.

### 3.4 Cái gì được dựng bằng API — cái gì BẮT BUỘC bấm bằng giao diện

| Việc | Đường được phép | Lý do |
|---|---|---|
| Tạo đợt · lập BC · nhập/lưu số liệu · đọc lại bản ghi để đối chứng | **API hoặc giao diện đều được** (ưu tiên giao diện cho gọn) | Đây là **tiền đề**, không phải hành vi đang tranh chấp |
| 🔴 **Bấm [Trình duyệt KQ]** | **BẮT BUỘC GIAO DIỆN THẬT** | Đây **chính là hành động đang tranh chấp** của phiếu. Gọi thẳng `submit-bc` bằng API ⇒ **verdict vô hiệu** |
| 🔴 **Bắt câu chữ thông báo** | Bộ bắt DOM cài trước thao tác, đọc `innerText` | Vế C2 hỏi *"hệ thống **hiển thị**"* — chuỗi trong phản hồi máy chủ là **đối chứng**, không thay được chữ người dùng nhìn thấy |

- Cấm đoán endpoint (đọc `/api/docs-json` trước), **cấm ghi thẳng DB**, cấm đụng dữ liệu đối tác.
- Seed = mutate môi trường chung ⇒ khai vào báo cáo: **đổi bản ghi nào · đổi gì · trên env nào**.

---

## 4. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ cả 2, trên ≥1 lượt bấm THỰC HIỆN MỚI bằng giao diện sau bản dựng đang đo):
   (C1) Báo cáo đang ở tình trạng "chưa đầy đủ" theo :802 (có bằng chứng chụp màn + dữ liệu đã lưu)
        → bấm [Trình duyệt KQ] → thao tác KHÔNG đi lọt, và đọc lại bản ghi thấy trạng thái GIỮ NGUYÊN.
   (C2) Người dùng nhìn thấy đúng chuỗi "Vui lòng hoàn chỉnh báo cáo trước khi trình"
        (đọc bằng innerText), và chuỗi đó khớp thông điệp trong phản hồi máy chủ của chính lượt bấm đó.

❌ FAIL nếu:
   - Thao tác ĐI LỌT (trạng thái chuyển sang "Chờ duyệt kết quả") trong khi báo cáo còn ô trống;
   - HOẶC bị chặn nhưng KHÔNG hiển thị thông báo nào cho người dùng (chỉ im lặng / chỉ lỗi trong nhật ký
     trình duyệt);
   - HOẶC câu chữ hiển thị khác nghĩa chuỗi đã đặc tả ở :825 (vd chuỗi tiếng Anh thô, mã lỗi trần,
     "Có lỗi xảy ra");
   - HOẶC hai đường đo mâu thuẫn (màn báo chặn nhưng bản ghi đã đổi trạng thái, hoặc ngược lại).
```

### 4.1 ⚠️ Bẫy chống **FAIL oan**

1. **Nhãn nút khác phiếu.** Phiếu ghi *"Trình phê duyệt"*, giao diện hiện **[Trình duyệt KQ]** (`:1170`
   khai đúng chữ này). Phiếu **không nhắc nhãn nút** ⇒ **cấm FAIL vì nhãn**.
2. **Nhầm `nhan_xet` là chỉ tiêu bắt buộc.** `:802` ghi rõ *"`nhan_xet` **không** tính vào điều kiện này"*.
3. **Coi giá trị `0` là "chưa điền".** `:802`: *"giá trị **0 là đã điền**"*.
4. **Mã lỗi lệch `ERR-XI-07-01`.** Xem §1.2 — không phải vế chấm.
5. **Địa chỉ trang có tiền tố `/ct-htpldn/`.** BA-23 (`:1090`, `:1103`, `:1147`–`:1149`) chỉ đòi màn "Đợt báo
   cáo định kỳ" **độc lập** (đã đạt vì có mục menu riêng); SRS **không** đặc tả chuỗi địa chỉ.
6. **Trạng thái ĐỢT hiển thị không phải `DANG_LAP_BC`.** `:789` đòi đợt ở `DANG_LAP_BC`, nhưng lô F5 đo được
   trục ĐỢT (`DOT_BAO_CAO.trang_thai`, enum `:1368`) đứng yên ở `TAO_DOT` còn nhãn trên màn suy từ trục ĐƠN
   VỊ (`:1389`). **Đây là vùng đặc tả tự mâu thuẫn (§6), KHÔNG phải điều kiện để FAIL phiếu 341** — miễn là
   nút [Trình duyệt KQ] có mặt và bấm được thì tiền đề coi như đạt; ghi lại cả hai trục làm bằng chứng.
7. **Bấm bằng CB Phê duyệt hoặc tài khoản cấp TW rồi bị chặn** = đúng spec (`:784` + `:712`), cấm log.

### 4.2 ⚠️ Bẫy chống **PASS oan** *(mục 1 là bẫy nguy hiểm nhất của phiếu này)*

1. 🔴 **PASS "ăn ké" điểm hỏng của dòng 340.** Lô F5 đo được: 11/13 chỉ tiêu **không có ô nhập**, hệ thống
   tự hiện `0 (HT)` nhưng không lưu, nên **mọi** báo cáo đều bị máy chủ coi là chưa đầy đủ ⇒ bấm gì cũng bị
   chặn kèm đúng câu chữ. Nếu QA lấy một báo cáo **đã điền hết mọi ô có thể nhập** rồi thấy bị chặn và chấm
   Pass cho 341 ⇒ **đó là kịch bản của dòng 340 (đang Reopen), không phải của 341** — Pass oan.
   **Bắt buộc:** tiền đề phải là báo cáo **thực sự thiếu** theo `:802` (ưu tiên TĐ-A: có ô nhập bỏ trống),
   và phải chụp bằng chứng ô nào trống.
2. **Chấm bằng phản hồi máy chủ thay cho màn hình.** Vế C2 hỏi *"hiển thị"*. Có 422 mà không có thông báo
   nào hiện lên ⇒ **không đạt C2**.
3. **Đọc chữ bằng `textContent`.** Gom cả node ẩn của AntD ⇒ **bug ma** / pass ma. Dùng `innerText`.
4. **Bộ bắt thông báo lọc trùng.** CẤM lọc trùng (che double-toast). Cài **trước** thao tác, đếm kèm **số
   yêu cầu gửi đi**. 1 thao tác sinh 2 thông báo ⇒ ghi mục RIÊNG (hồi quy `BUG-BC-TOAST-LOI-HIEN-2-LAN`,
   đóng 28/07), **không** trộn vào 2 vế.
   > Lô F5 đã ghi nhận: mỗi lượt bấm bắt được **2 nút DOM** (`ant-message` khung + `ant-message-notice-wrapper`
   > con) của **CÙNG 1** thông báo, lệch ~1 ms ⇒ **1 thông báo**. Đếm theo **mốc giờ khác nhau**, không theo
   > độ dài mảng.
5. **Không đọc lại bản ghi sau khi bị chặn.** Phải xác minh trạng thái **giữ nguyên** — "báo chặn nhưng vẫn
   đổi trạng thái" là ca hỏng thật.
6. **Tab mở lâu chạy bó mã cũ.** Tải lại trang **bằng địa chỉ** + đọc lại tên bó mã `assets/index-*.js` ở
   **đầu và cuối** phiên (brief §3).
7. **Kết luận trên env khác.** Đo trên env **nội bộ** `18.143.165.120.nip.io`; đối tác nghiệm thu trên
   `htpldn-uat.ospgroup.vn` ⇒ bắt buộc ghi câu giới hạn hiệu lực.

---

## 5. Đường đo thứ hai (đối chứng độc lập — bắt buộc đúng 1 đường, không thêm đường thứ ba)

Đọc lại **chính bản ghi** bằng phiên của `cbnv_dp_03` (cookie-auth, **không** dùng `admin`) ngay sau lượt
bấm: trạng thái nộp của đơn vị · trạng thái bản báo cáo · trạng thái đợt — **cả ba phải không đổi**, và
`message` trong phản hồi của lượt bấm phải khớp chuỗi hiển thị.
🔴 **Tra `/api/docs-json` để lấy đúng đường dẫn — CẤM đoán endpoint** (`/api/docs-json` đọc được không cần
đăng nhập). Bấm lại cùng một nút **không** tính là đường thứ hai.

**Hai đường mâu thuẫn ⇒ CHƯA được chốt** — ghi cả hai, hỏi user.

---

## 6. Ghi nhận (KHÔNG chấm) — gửi BA/dev

1. **Mã lỗi lệch đặc tả** — `:825` khai `ERR-XI-07-01`, hệ thống trả `ERR-VAL-XI-07-02` (lô F5 đo được).
   Câu chữ khớp. Không phải vế phiếu ⇒ ghi nhận, **liên kết** mục đã có ở bàn giao F5 §4 mục 2.
2. **Trục trạng thái đợt vs đơn vị** — đặc tả tự mâu thuẫn (`:789` đòi đợt `DANG_LAP_BC`; `:1512` khai
   `TAO_DOT → DANG_LAP_BC` do FR-XI-06, nhưng Processing FR-XI-06 `:739`–`:747` **không có bước nào** đụng
   `DOT_BAO_CAO.trang_thai` — `:746` chỉ đặt `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop = DANG_LAP`; `:1368` chỉ
   cho đợt **một** giá trị trong khi phạm vi đợt là ~70–83 đơn vị `:1367`/`:1398`/`:646`).
   ⇒ **Đã có câu hỏi BA ở bàn giao lô F5 §3 Nhóm 2 — liên kết, KHÔNG mở câu hỏi trùng.**

---

## 7. Độ phủ biến thể — **sàn N = 1**

| # | Dạng | Cách dựng | Bắt buộc? |
|---|---|---|---|
| **①** | CB NV **ĐP** trên biểu mẫu đang áp dụng của đợt | `cbnv_dp_03` | **BẮT BUỘC** |
| ② | CB NV **BN** | `cbnv_bn_03` | Chỉ khi ① không dựng được |

**KHÔNG mở rộng:** không đo nhánh "báo cáo ĐÃ đầy đủ → trình đi lọt" (đó là **dòng 340**, phiếu khác, đang
Reopen); không đo nhánh từ chối của CB PD (FR-XI-07a `:834`–`:903`); không đo `MAU_21B`/`CA_HAI` nếu đợt đang
dùng `MAU_21A` — phiếu không nhắc biểu mẫu.

---

## 8. Rủi ro verdict **Chưa chốt** — thấp

| Rủi ro | Xác suất | Cần bổ sung gì mới chốt được |
|---|---|---|
| Không có cặp (đợt, đơn vị) nào để `cbnv_dp_03` lập/sửa báo cáo | Thấp — còn TĐ-C dựng đợt mới bằng `cbnv_tw_03` | Nếu `:656`/`:688` chặn hết 3 kỳ của 2026 → tạo đợt năm khác, hoặc đổi sang `cbnv_bn_03` |
| Giao diện tự điền `0` nên không tạo được ô trống | Trung bình | Dùng TĐ-B + khai rõ giới hạn kết luận (§3.3) |
| `cbnv_dp_03` không nằm trong phạm vi đơn vị nộp của mọi đợt | **Rất thấp** — trinh sát 11:50 đọc được 2 đợt đang có bản ghi nộp của đơn vị này ở `DANG_LAP` | Dựng đợt mới có phạm vi mặc định (`:646`) |

> **Kết luận rủi ro:** đây là phiếu **an toàn nhất trong 4 phiếu của lô**. Tiền đề có sẵn, có bản dự phòng,
> và thao tác bị chặn nên **không tiêu hủy tiền đề** ⇒ đo lại được nhiều lượt. Nên chạy **đầu tiên**.
