# Chuẩn chấm đã khóa — LBCKQTHCT_01 (dòng 335) — "Lập báo cáo kết quả thực hiện chương trình"

> **Đặc tả — nguồn DUY NHẤT của phiếu này:**
> `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md` (1.610 dòng).
> Mọi số dòng dưới đây do agent này **tự mở file đếm lại ngày 2026-08-07**. Không quote từ trí nhớ,
> không quote từ `input/srs-update-2026-5-5/`, không quote từ báo cáo đợt cũ.
>
> **Không có khối `── CÁCH VERIFY sau Dev fix ──`** trong 2 bug entry tuần 4 của case này
> (`../../../reverify-week-4/bug-reports/bug-report-UAT-tuan-4.md` — `BUG-BC-KHONG-LAP-DUOC-BAO-CAO` dòng
> 2457, `BUG-BC-TOAST-LOI-HIEN-2-LAN` dòng 2581; đã grep `CÁCH VERIFY` → **0 kết quả** trên toàn file).
> ⇒ Chuẩn chấm dưới đây dựng thẳng từ SRS, không có chuẩn mạnh hơn để chép lại.
>
> **Trạng thái phiếu:** đã qua **vòng 2**. Ô `Kết quả verify` (T335) đang giữ nguyên văn kết luận vòng 2
> của đối tác: *"Hệ thống không chuyển trạng thái thành «Đang lập»"* · `Trạng thái 2 = Fail` ·
> `Trạng thái dev fix 2 = dev done` (xem `../audit/gia-tri-o-truoc-khi-ghi.md`).

---

## 1. BẢNG SCOPE LOCK — 4 vế của "Kết quả mong đợi"

| Vế | Expected đối tác (nguyên văn phiếu) | SRS `srs-fr-15-ct-htpldn.md:` | Nguyên văn dòng SRS (≤200 ký tự) | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|---|
| **C1** | "Cập nhật trạng thái nộp của **đơn vị** thành **'Đang lập'**" | **`:746`** (chính) · `:718` · `:1389` | `:746` = `\| 8 \| Cập nhật `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop = DANG_LAP` + `bao_cao_id = <bao_cao mới>` \| — \|` | **MATCH** | **TEST** | Màn chi tiết đợt BC: nhãn trạng thái nộp **của chính đơn vị đang đăng nhập** đổi sang "Đang lập" và **giữ sau khi tải lại trang bằng địa chỉ** |
| **C2** | "Lưu nội dung báo cáo chi tiết" | **`:745`** (chính) · `:731` · `:733` · `:757` | `:745` = `\| 7 \| Lưu bản ghi `BAO_CAO_CT_HTPL` (giữ tên entity theo BA chốt 2026-05-30) với `dot_id` + `don_vi_nop_id` + `ct_htpl_ids_lien_quan[]` \| — \|` | **MATCH** | **TEST** | Nhập số liệu + nhận xét → [Lưu nháp] → **tải lại trang** → đọc lại đúng từng giá trị vừa nhập |
| **C3** | "Lưu vết thao tác theo quy định" | **`:747`** (chính) · `:758` · `:1568` | `:747` = `\| 9 \| Ghi nhật ký thao tác \| BR-DATA-05 \|` | **MATCH** | **TEST** | Màn Nhật ký hệ thống (vai trò QTHT) lọc theo mốc giờ vừa thao tác → có mục ứng với thao tác lập/lưu BC của đúng tài khoản |
| **C4** | "Lưu thành công, hệ thống hiển thị thông báo nhanh **«Đã lưu nháp»**" | **IM LẶNG** — gần nhất: `:1170` (dòng #40 SCR-XI-01) · đối chiếu `:1032` · `:1173` | `:1170` = `\| 40 \| action-bar \| [DANG_LAP_BC] Hanh dong lap BC (gop tu MH-15.6) \| button-group (C22) \| [Huy] [Luu nhap] [Trinh duyet KQ] -> validate -> SET CHO_DUYET_KQ + SET bc CHO_PHE_DUYET -> TB CB PD \|` | **GAP** | **BA** | **CẤM Pass/Reopen vế này.** Chỉ ghi nhận nguyên văn thông báo quan sát được, không chấm |

**Căn cứ khẳng định C4 là IM LẶNG (không phải grep rỗng):** đã đọc trọn FR-XI-06 (`:701`–`:770`) — bảng
Outputs `:751`–`:753` chỉ có "Báo cáo CT", bảng Error Handling `:762`–`:764` chỉ có `ERR-XI-06-01`, AC
`:768`–`:769` không nhắc thông báo; đọc trọn khối SCR-XI-01 dòng #35–#45 (`:1165`–`:1175`) — chỉ dòng
`:1173` (Gửi TW) khai chữ "Toast success". SRS **có khai thông báo thành công khi muốn** (`:1032` =
`\| I1 \| Tổng hợp thành công \| INF-XI-09-01 \| "Đã tổng hợp báo cáo toàn quốc" \| INFO \|`) ⇒ việc
FR-XI-06 không có mã `INF-XI-06-*` là im lặng có ý nghĩa, không phải sót grep.

---

## 2. Vế quyết định verdict vòng này

🔴 **C1 — trạng thái nộp của đơn vị chuyển sang "Đang lập".**

Vòng 1 đối tác báo 403 (`ERR-AUTH-VPD-00-02`, vai trò `CB_NV_DP`) ở bước **mở màn chi tiết đợt**; vòng 2
đối tác đổi triệu chứng sang **"Hệ thống không chuyển trạng thái thành «Đang lập»"**. ⇒ Vế 403 **không
còn là vế tranh chấp**; nó lùi về hàng **tiền đề** (đơn vị phải nằm trong phạm vi nộp — `:717`).

- C2, C3 vẫn phải đo đủ (cùng route TEST) nhưng **không** dùng để lật verdict nếu C1 đạt và C2/C3 đạt.
- C4 **không được** dùng để lật verdict theo bất kỳ hướng nào (GAP).
- Nếu C1 đạt mà C2 **không** đạt (số liệu không đọc lại được sau tải lại trang) ⇒ vẫn **Reopen**, ghi rõ
  điểm hỏng đã dịch sang vế lưu nội dung.

> ⚠️ **Bẫy trục trạng thái — đọc trước khi đo.** SRS có **HAI** trục trạng thái khác nhau, đừng đo nhầm:
> - **Trục ĐƠN VỊ** — `DOT_BAO_CAO_DON_VI_NOP.trang_thai_nop`, enum tại `:1389` =
>   `CHECK IN ('CHUA_NOP','DANG_LAP','CHO_DUYET','DA_DUYET','DA_NOP','QUA_HAN')`. **C1 nằm ở trục này**
>   (phiếu ghi rõ "trạng thái nộp **của đơn vị**"; SRS `:746` ghi rõ `trang_thai_nop = DANG_LAP`).
> - **Trục ĐỢT** — `DOT_BAO_CAO.trang_thai`, enum tại `:1368` =
>   `CHECK IN ('TAO_DOT','DANG_LAP_BC','CHO_DUYET_KQ','DA_DUYET_KQ','DA_GUI_TW','DA_TONG_HOP')`, nhãn
>   hiển thị ở bảng `:1194`–`:1199` (`DANG_LAP_BC` → nhãn "Dang lap BC").
>
> Hai trục có nhãn **na ná nhau** ("Đang lập" vs "Đang lập BC"). Chấm C1 bằng nhãn trục ĐỢT = **sai vế**.

---

## 3. Precondition + công thức dựng tiền đề

### 3.1 Vai trò / tài khoản (env `https://18.143.165.120.nip.io` · MailHog `http://18.143.165.120:8025/`)

| Vai trò | Tài khoản | Mật khẩu | Dùng để |
|---|---|---|---|
| **Người ra verdict** — CB Nghiệp vụ cấp **ĐP** (đơn vị thuộc phạm vi nộp) | `cbnv_dp_01` (`donViId 00000000-0000-4000-8002-000000000006`, `capDonVi = DP`) | `Test@1234` | **Thao tác lập BC + đọc trạng thái nộp** — tài khoản chốt PASS/FAIL |
| CB Nghiệp vụ cấp **BN** (biến thể thứ 2, xem §7) | `cbnv_bn_01` | `Test@1234` | Phủ nhánh Bộ ngành của `:712` |
| CB Nghiệp vụ cấp **TW** — dựng đợt mới | `cbnv_tw_01` | `Test@1234` | **CHỈ dựng tiền đề** (tạo đợt BC — `:625`). **KHÔNG** dùng ra verdict cho case này |
| Đối chứng đọc lại không qua API | `cbnv_dp_02` (phải xác minh cùng `donViId` với `cbnv_dp_01`) | `Test@1234` | Đường đo thứ hai (xem §5 phương án B) |
| Đọc nhật ký cho vế C3 | tài khoản QTHT | — | **Chỉ đọc log**, khai rõ trong báo cáo |
| **CẤM ra verdict** | `admin` / `Secret@123` | — | Quyền rộng che lỗi phạm vi đơn vị |

> ⚠️ `cbnv_dp` (không hậu tố) **login FAIL** từ 03/08/2026 (401, `Test@1234`) — đã fallback đúng Rule 7
> sang `cbnv_dp_01` **cùng vai trò `CB_NV_DP` + cùng cấp ĐP**. Ghi rõ account thực dùng trong báo cáo.

### 3.2 Màn / đường dẫn

- Menu sidebar **"Đợt báo cáo"** → danh sách đợt → biểu tượng **[Xem]** trên dòng đợt → **chi tiết đợt**
  (tuần 4 quan sát địa chỉ dạng `/ct-htpldn/dot-bao-cao/{id}`).
- Nút **[Lập báo cáo]** ở cuối trang chi tiết → hộp thoại *"Bắt đầu lập báo cáo?"* → **[Đồng ý]** →
  biểu mẫu 21a chuyển sang chế độ nhập liệu, hiện **[Làm mới] [Lưu nháp] [Trình duyệt KQ]**.
- ⚠️ **Không FAIL vì tiền tố địa chỉ `/ct-htpldn/`.** SRS `:1090` + `:1103` + `:1147`–`:1149` (BA-23 tuần 4,
  chốt 2026-07-30) chỉ yêu cầu màn "Đợt báo cáo định kỳ" **độc lập, không còn là thẻ con trong chi tiết CT**
  — đã đạt vì có mục menu riêng. SRS **không** đặc tả chuỗi địa chỉ.

### 3.3 Trạng thái dữ liệu + công thức dựng

**Tiền đề bắt buộc theo `:716`–`:718` (đọc nguyên văn):**
```
:716  - User đã đăng nhập là CB NV cấp ĐP/BN
:717  - Đợt BC định kỳ đã tạo (FR-XI-05a) và đơn vị user nằm trong `pham_vi_don_vi_nop_ids[]`
:718  - `DOT_BAO_CAO_DON_VI_NOP` của (đợt, đơn vị) ở trạng thái CHUA_NOP hoặc DANG_LAP
```

**🔴 Kho tiền đề nhiều khả năng ĐÃ CẠN cho vế C1.** Tuần 4 R2 (28/07) đã bấm [Lập báo cáo] thành công
trên **cả 2 đợt đang có** (`DOT-SO_BO_NAM-2026-1`, `DOT-SO_BO_6_THANG-2026-1`) bằng chính `cbnv_dp_01`
⇒ cặp (đợt, đơn vị ...8002-000000000006) nhiều khả năng đang ở **`DANG_LAP`**. `:718` vẫn cho phép vào
form ở `DANG_LAP`, **nhưng không quan sát được phép chuyển `CHUA_NOP → DANG_LAP`** ⇒ **không chấm được C1**.

**Bước 0 — ĐỌC TRƯỚC KHI DỰNG (bắt buộc, không được bỏ):** đăng nhập `cbnv_dp_01`, mở từng đợt, ghi lại
bảng `mã đợt | trạng thái nộp của đơn vị mình | đã có báo cáo chưa`. Chỉ khi có **≥1 cặp ở `CHUA_NOP`**
thì mới TÁI SỬ DỤNG được.

**Công thức A — TÁI SỬ DỤNG (ưu tiên, rẻ nhất).** Nếu bước 0 tìm được đợt mà đơn vị còn **"Chưa nộp"** →
đo thẳng trên đợt đó, không tạo gì mới.

**Công thức B — DỰNG MỚI (khi A không có).** Vế bug nằm đúng ở **bước chuyển trạng thái** ⇒ được phép tạo mới:
```
Đăng nhập cbnv_tw_01 (CB NV cấp TW — chỉ TW được tạo đợt, :625)
  → menu "Đợt báo cáo" → [+ Tạo đợt mới]
  → Kỳ báo cáo: TRON_NAM      ← BẮT BUỘC chọn kỳ CHƯA dùng trong năm 2026
  → Tên đợt: QA-BCCT-<YYYYMMDD-HHmm>-tron-nam   (ghi lại nguyên văn)
  → Hạn nộp / Từ ngày / Đến ngày: hợp lệ · Biểu mẫu: CA_HAI
  → Phạm vi đơn vị nộp: GIỮ mặc định toàn bộ ĐP + BN, xác minh có đơn vị của cbnv_dp_01 (:646)
  → Tạo đợt
Kỳ vọng theo :657 — hệ thống tự sinh bản ghi nộp cho từng đơn vị ở trạng thái CHUA_NOP
  → xác minh: mở chi tiết đợt mới, đơn vị của cbnv_dp_01 phải ở "Chưa nộp"
```
> ⚠️ **Chọn nhầm kỳ sẽ bị chặn ĐÚNG SPEC, đừng log thành bug.** `:656` = `\| 5 \| Kiểm tra không trùng đợt
> (cùng `ky_bao_cao` + năm) \| — \|`; `:688` = `\| E2 \| Đợt BC trùng kỳ + năm \| ERR-XI-05a-02 \| "Đã tồn
> tại đợt báo cáo cho kỳ '{ky}' năm {YYYY}" \| ERROR \|`. Hai kỳ `SO_BO_NAM` và `SO_BO_6_THANG` của 2026
> **đã có đợt** ⇒ chỉ còn `TRON_NAM` 2026 (hoặc đổi năm).

> ⚠️ **Mâu thuẫn nội bộ SRS có thể chặn công thức B — ghi nhận, KHÔNG log thành bug của phiếu này.**
> `:631` = *"**Bỏ điều kiện** «CT HTPL ở DANG_THUC_HIEN/HOAN_THANH» — đợt BC không gắn CT nên không kiểm
> tra trạng thái CT"* và `:655` = `\| 4 \| **BỎ kiểm tra trạng thái CT (STT 52 UAT 2026-05-26)** …`, NHƯNG
> `:1227` = `- CT phai o DANG_THUC_HIEN hoac HOAN_THANH moi tao dot BC` và `:1511` (bảng SM-DOT-BC) vẫn ghi
> Guard `CT ở DANG_THUC_HIEN/HOAN_THANH`. Nếu giao diện chặn tạo đợt vì lý do CT ⇒ đó là **mâu thuẫn spec**,
> ghi vào phần BA confirm §7, và chuyển sang công thức C.

**Công thức C — ĐỔI ĐƠN VỊ (khi A và B đều hỏng).** `:712` cho phép **cả BN lẫn ĐP**. Đăng nhập `cbnv_bn_01`
(cấp BN) trên chính 2 đợt cũ — đơn vị BN này chưa từng lập BC ở tuần 4 ⇒ nhiều khả năng còn `CHUA_NOP`.
**Đây là đổi ĐƠN VỊ trong cùng nhóm tác nhân mà `:712` cho phép, KHÔNG phải đổi cấp trái phép.**

**Chốt định danh TRƯỚC khi bấm (bắt buộc ghi vào báo cáo):** `username thực dùng` · `vai trò` · `capDonVi` ·
`mã đơn vị` · `mã đợt` · `trạng thái nộp trước khi bấm`. Không chốt được ⇒ **chưa được đo**, vì cả 4 vế đều
gắn với đúng cặp (đợt, đơn vị).

---

## 4. Các bước đo (UI thật)

0. **Ghi dấu vân tay bản dựng TRƯỚC khi đo** (bó mã FE · `last-modified` · `etag`) và **tải lại trang bằng
   địa chỉ** — tab mở lâu vẫn chạy bó mã cũ. Đối chiếu với `../../BAN-DUNG.md`; nếu lệch ⇒ FE đã deploy lại,
   ghi rõ số đo mới.
1. Đăng nhập **`cbnv_dp_01`** (mã xác thực 6 số lấy ở MailHog). Ghi lại account thực dùng.
2. Menu **"Đợt báo cáo"** → mở chi tiết đợt đã chốt ở §3.3. **Chụp màn hình trạng thái nộp TRƯỚC khi bấm**
   (phải là "Chưa nộp").
3. Bấm **[Lập báo cáo]** → **[Đồng ý]**. **Chụp/bắt thông báo** hiện ra (xem bẫy §6.3 — thông báo tự tắt).
4. **Đo C1:** đọc nhãn trạng thái nộp **của đơn vị mình** ngay sau thao tác → **tải lại trang bằng địa chỉ**
   → đọc lại lần nữa. Cả 2 lần phải là **"Đang lập"**.
5. **Đo C2:** nhập số liệu vào **toàn bộ chỉ tiêu** của biểu mẫu đang áp dụng + nhập **nhận xét** bằng chuỗi
   mốc-giờ duy nhất `QA-BCCT-<YYYYMMDD-HHmm>-nhan-xet` (ghi lại nguyên văn) → bấm **[Lưu nháp]** →
   **tải lại trang** → đọc lại từng ô: số liệu và nhận xét phải khớp **từng chữ**.
6. **Đo C4 (chỉ GHI NHẬN, không chấm):** chép nguyên văn thông báo quan sát được.
7. **Đo C3:** đăng nhập QTHT → màn Nhật ký hệ thống → lọc quanh mốc giờ bước 3 và bước 5 → phải có mục ứng
   với thao tác của đúng tài khoản `cbnv_dp_01`. Không truy cập được màn này ⇒ ghi **🚫 không đo được**,
   **KHÔNG** chấm FAIL.
8. **Đo bằng đường thứ hai** — §5.
9. Ghi bảng kết quả: `mã đợt | đơn vị | trạng thái trước | trạng thái sau bấm | sau tải lại | nhận xét đã nhập | nhận xét đọc lại | khớp?`.

---

## 5. Đường đo thứ hai (đối chứng độc lập) — chọn **A**, dùng **B** khi A không khả thi

**Phương án A — đọc lại bản ghi từ máy chủ bằng chính phiên của `cbnv_dp_01`** (cookie-auth, KHÔNG dùng `admin`).
- 🔴 **Phải tra `/api/docs-json` để lấy đúng đường dẫn — CẤM đoán endpoint.** (`/api/docs-json` đọc được
  không cần đăng nhập.)
- **Manh mối** từ tuần 4 (chỉ để biết tra ở nhóm nào, **không phải căn cứ**): nhóm `.../dot-bao-caos/…`;
  tuần 4 đã quan sát `POST …/dot-bao-caos/{id}/start` trả 409 trước khi dev fix.
- Đối chiếu: bản ghi nộp của **đúng cặp (đợt, đơn vị)** phải mang trạng thái tương ứng "Đang lập" và có
  liên kết tới bản báo cáo vừa tạo; nội dung số liệu + nhận xét khớp từng chữ chuỗi đã nhập.

**Phương án B — đối chứng bằng tài khoản thứ hai cùng đơn vị (không cần API).**
Đăng nhập `cbnv_dp_02` (**phải xác minh cùng `donViId` với `cbnv_dp_01` trước**), mở đúng đợt đó → phải thấy
cùng trạng thái "Đang lập" + cùng nội dung nháp. Chứng minh dữ liệu nằm ở máy chủ chứ không phải chỉ đổi
trên màn của phiên đang mở.

**Mâu thuẫn 2 đường** (một đường đạt, đường kia không) ⇒ ghi **cả hai** vào bug entry, đề xuất BA/dev xem,
**không** tự chọn đường có lợi.

---

## 6. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ CẢ 3 điều, trên ≥1 cặp (đợt, đơn vị) mới thao tác sau bản fix):
   (C1) Sau khi cán bộ nghiệp vụ ĐP/BN thuộc phạm vi nộp thực hiện thao tác lập báo cáo, trạng thái nộp
        của CHÍNH ĐƠN VỊ đó đọc được là "Đang lập", và GIỮ NGUYÊN sau khi tải lại trang bằng địa chỉ.
   (C2) Số liệu và nhận xét vừa nhập được lưu lại: sau khi tải lại trang đọc lại đúng từng chữ.
   (C3) Có mục nhật ký ứng với thao tác đó, đúng tài khoản, đúng mốc giờ.
   VÀ đúng ở cả hai đường đo (§5).

❌ FAIL nếu:
   - Trạng thái nộp của đơn vị không đổi, hoặc đổi trên màn rồi quay lại "Chưa nộp" sau khi tải lại trang;
   - HOẶC thao tác bị hệ thống từ chối trong khi cả 3 tiền đề :716–:718 đều đang thoả (chốt bằng bằng chứng
     đọc được, không phải suy đoán);
   - HOẶC số liệu/nhận xét không đọc lại được sau khi tải lại trang;
   - HOẶC hai đường đo mâu thuẫn nhau.

⚠️ KHÔNG chấm bằng vế C4: SRS im lặng về việc có/không có và câu chữ của thông báo nhanh (§1).
⚠️ KHÔNG chấm FAIL vì nhãn hiển thị viết hoa/thường/dấu khác ("Đang lập" vs "đang lập") — SRS chỉ khai giá
   trị trạng thái (:1389), bảng nhãn :1194–:1199 là của TRỤC ĐỢT, không phải trục đơn vị.
```

### 6.1 ⚠️ Bẫy chống **FAIL oan**

1. **Đo nhầm trục trạng thái.** Xem hộp cảnh báo §2. Màn chi tiết đợt hiển thị **cả hai**: nhãn trạng thái
   của đợt (thanh tiến trình 6 bước `TAO_DOT → … → DA_TONG_HOP`, `:1166`) và trạng thái nộp của từng đơn vị.
   Đọc thanh tiến trình rồi kết luận "không chuyển sang Đang lập" = **FAIL oan**. C1 chỉ hỏi trục ĐƠN VỊ.
2. **Đo bằng tài khoản cấp TW.** `:712` = *"**CB Nghiệp vụ cấp ĐP/BN** (đơn vị thuộc phạm vi đợt BC). Thu hẹp
   từ «CB NV TW/BN/ĐP» — TW không tự lập BC…"*. Phiếu ghi Tác nhân "Cán bộ TW, BN, ĐP" nhưng đó là ô Tác nhân
   của phiếu, **không phải một vế Kết quả mong đợi** ⇒ **tiền đề**, không tách thành bug. Dùng `cbnv_tw_01`
   rồi bị chặn = **đúng spec**, cấm log.
3. **Đo trên đơn vị ngoài phạm vi nộp.** `:717` đòi đơn vị nằm trong `pham_vi_don_vi_nop_ids[]`. Bị chặn khi
   ngoài phạm vi = đúng spec. **Phải chốt bằng chứng đơn vị CÓ trong phạm vi trước khi bấm.**
4. **Đo lại trên cặp đã ở "Đang lập" từ tuần 4.** Không quan sát được phép chuyển ⇒ đó là **thiếu tiền đề**,
   không phải "hệ thống không chuyển trạng thái". Bắt buộc bước 0 §3.3.
5. **Câu chữ thông báo lệch.** Tuần 4 quan sát *"Đã bắt đầu lập báo cáo"* và *"Đã lưu nháp thành công"*,
   phiếu kỳ vọng *"Đã lưu nháp"*. SRS im lặng ⇒ **cấm FAIL vì câu chữ** (vế C4, GAP).
6. **Địa chỉ trang có tiền tố `/ct-htpldn/`.** Xem §3.2 — không phải vi phạm BA-23.

### 6.2 ⚠️ Bẫy chống **PASS oan**

1. **Nhãn đổi trên màn nhưng chưa lưu ở máy chủ.** Bắt buộc **tải lại trang bằng địa chỉ** + đường đo thứ hai.
   Vòng 2 đối tác báo đúng triệu chứng nhóm này ⇒ đây là chỗ dễ Pass oan nhất.
2. **Thấy form 21a chuyển sang chế độ nhập liệu rồi kết luận đạt.** Form mở là hệ quả giao diện; C1 hỏi
   **trạng thái nộp**, C2 hỏi **nội dung đọc lại được**. Form mở mà tải lại trang mất sạch = **FAIL**.
3. **Nhận xét/số liệu "có vẻ" khớp.** Bắt buộc chuỗi mốc-giờ duy nhất `QA-BCCT-<YYYYMMDD-HHmm>-…` ghi lại
   **trước** khi bấm; không có chuỗi gốc thì không chấm được "khớp từng chữ".
4. **Dùng `admin` đọc dữ liệu rồi kết luận.** Quyền rộng che đúng loại lỗi mà vòng 1 báo (phạm vi đơn vị).
   `admin` chỉ để tra định danh, phải khai rõ, và phải đối chứng lại bằng `cbnv_dp_01`.
5. **Bản ghi cũ (dữ liệu đóng băng).** Báo cáo nháp tạo **trước** bản fix mang dữ liệu của bản cũ. **Phép thử
   quyết định = thao tác lập/lưu THỰC HIỆN MỚI sau bản fix.**
6. **Kết luận trên env sai.** Đối tác quay bằng chứng trên `htpldn-uat.ospgroup.vn`; đợt này đo trên env nội
   bộ `18.143.165.120.nip.io`. Mọi verdict Pass là **Pass tạm** cho bản dựng đo được — bắt buộc ghi câu giới
   hạn này vào kết quả.

### 6.3 ⚠️ Bẫy kỹ thuật khi bắt thông báo

Thông báo tự tắt sau ~3 giây (tuần 4 đã trượt ảnh chụp). Cài bộ bắt thông báo **TRƯỚC** khi bấm, **CẤM lọc
trùng** (che mất lỗi hiện 2 thông báo — đúng bug `BUG-BC-TOAST-LOI-HIEN-2-LAN` tuần 4), và luôn **đếm số yêu
cầu gửi đi kèm theo**. Nếu 1 thao tác lại sinh 2 thông báo ⇒ đó là **hồi quy** của bug tuần 4 đã đóng: log
thành mục RIÊNG, ghi rõ "hồi quy so với bản 28/07", **không** trộn vào 4 vế của phiếu.

---

## 7. CẦN BA CONFIRM (vế GAP + mâu thuẫn nội bộ)

**(1) Vế C4 — thông báo nhanh khi lưu nháp:**

> **CẦN BA CONFIRM:** đối tác kỳ vọng *khi lưu nháp thành công, hệ thống hiển thị thông báo nhanh
> **"Đã lưu nháp"***; SRS quy định **IM LẶNG** — FR-XI-06 (`srs-fr-15-ct-htpldn.md:701`–`:770`) không có mã
> `INF-XI-06-*` nào, bảng Outputs `:751`–`:753` chỉ khai bản ghi báo cáo, dòng SCR `:1170` chỉ liệt kê nút
> [Lưu nháp] mà không đặc tả thông báo — trong khi SRS **có** khai thông báo thành công ở chỗ khác
> (`:1032` `INF-XI-09-01` "Đã tổng hợp báo cáo toàn quốc"; `:1173` "Toast success" cho thao tác Gửi TW);
> web/dev hiện tại **chờ đo**.
>
> **Câu hỏi BA:** (a) Thao tác Lưu nháp ở FR-XI-06 **có bắt buộc** phản hồi thành công cho người dùng không?
> (b) Nếu có, câu chữ có bị ràng buộc đúng chuỗi *"Đã lưu nháp"* như phiếu UAT, hay chỉ cần một thông báo
> thành công bất kỳ (hiện hệ thống trả *"Đã lưu nháp thành công"*)? (c) Nếu BA chốt bắt buộc câu chữ, xin bổ
> sung mã `INF-XI-06-*` vào bảng Error/Info Handling của FR-XI-06 để lần sau chấm được.

**(2) Mâu thuẫn nội bộ SRS ảnh hưởng TIỀN ĐỀ (chỉ gửi BA nếu công thức B bị chặn thật):**

> **CẦN BA CONFIRM:** FR-XI-05a `:631` và Processing bước 4 `:655` đã **BỎ** điều kiện "CT HTPL ở
> DANG_THUC_HIEN/HOAN_THANH" khi tạo đợt báo cáo (đợt độc lập với CT theo STT 52 UAT 2026-05-26), nhưng
> mục Quy tắc tương tác `:1227` và bảng chuyển trạng thái SM-DOT-BC `:1511` **vẫn giữ** điều kiện đó.
> **Câu hỏi BA:** dòng nào còn hiệu lực? Đề nghị gỡ `:1227` + sửa Guard `:1511` cho khớp `:631`/`:655`.

*(Ghi nhận, KHÔNG hỏi BA vòng này vì không chạm vế nào của phiếu: `:1151` `[CAN BA CHOT]` — định dạng mã đợt
`DOT-{CT_ID}-{SEQ}` ở dòng #32 còn gắn đợt vào một CT, trái mô hình độc lập; BA đã tự treo sẵn.)*

---

## 8. Độ phủ biến thể

| # | Dạng | Cách dựng | Bắt buộc? |
|---|---|---|---|
| **①** | CB NV cấp **ĐP** | `cbnv_dp_01` trên đợt có đơn vị mình ở "Chưa nộp" | **BẮT BUỘC** — đúng vai trò đối tác báo lỗi (`CB_NV_DP` trong thông báo 403 vòng 1) |
| **②** | CB NV cấp **BN** | `cbnv_bn_01`, cùng cách | **Khuyến nghị** — `:712` khai cả BN; nếu công thức C phải dùng thì dạng này thành bắt buộc |

**Sàn tối thiểu: N ≥ 1 cặp (đợt, đơn vị) dạng ①.** Chỉ dựng được ② mà không dựng được ① ⇒ vẫn đo, nhưng
**khai rõ trong báo cáo** là chưa phủ đúng cấp mà đối tác báo lỗi.

**KHÔNG mở rộng** (ghi để agent đo không tự nới): 2 biểu mẫu 21a/21b (`:730` cho đơn vị tự chọn) là chiều
biến thể của FR-XI-06 nhưng **không** vế nào của phiếu nhắc tới ⇒ đo 1 biểu mẫu là đủ; gặp lỗi ở biểu mẫu
còn lại thì ghi candidate riêng, **không** kéo verdict phiếu này.

---

## 9. Cảnh báo cho agent đo

1. 🔴 **Bước 0 §3.3 là bắt buộc.** Không đọc trạng thái nộp trước khi bấm ⇒ không chấm được C1 ⇒ **cấm mọi
   verdict, kể cả ô trống**.
2. 🔴 **Chỉ chấm trên thao tác THỰC HIỆN MỚI sau bản fix**, không đọc lại kết quả tuần 4.
3. 🔴 **Ghi nguyên văn chuỗi nhận xét + mốc giờ TRƯỚC khi bấm.**
4. **Ghi dấu vân tay bản dựng + tải lại trang bằng địa chỉ** trước khi đo (`../../BAN-DUNG.md` để đối chiếu).
5. **Không dùng `admin` ra verdict**; dùng để tra định danh thì phải khai và đối chứng lại.
6. Login fail → **Rule 7**: fallback **cùng vai trò + cùng cấp** (`cbnv_dp_01` → `_02` → `_03`), khai account
   thực dùng; **tuyệt đối không** đổi ĐP ↔ BN ↔ TW để "cho chạy được" (đổi phạm vi dữ liệu ⇒ verdict vô hiệu).
   *(Ngoại lệ duy nhất: công thức C §3.3 đổi sang BN là chuyển sang nhánh tác nhân mà `:712` cho phép — phải
   khai rõ là dạng ②, không phải fallback.)*
7. **Ảnh chụp lưu đúng** `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`.
8. **Khi ghi ô `Kết quả verify` (T335): phải nhắc lại triệu chứng vòng 2 của đối tác** (*"không chuyển trạng
   thái thành «Đang lập»"*) để dev không mất dấu vết — ô này đang chứa kết luận vòng 2, ghi đè là xóa mất.
