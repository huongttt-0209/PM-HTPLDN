# CHUẨN CHẤM — `DKTGMLTVV_13` (bảng `bug` dòng 35) · GIAI ĐOẠN A

**Lô:** `F6-flow04-3case-2026-08-07` · Flow 04 (verify bug dev đã fix, không có hồ sơ nội bộ)
**Bảng nguồn:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `bug`, dòng 35
**Mô tả case:** Gửi đăng ký khi Dữ liệu hợp lệ · Trạng thái `Fail` · Dopai `N/R` · Trạng thái dev fix `Fixed`
**SRS nguồn chuẩn (prompt chỉ định):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
— trọng tâm `srs-fr-04-chuyen-gia-tvv.md`; có dẫn thêm `srs-v3.5.md` (quy ước UI chung) và
`srs-fr-10-quan-tri.md` (màn tra nhật ký) trong CÙNG thư mục v3.5.
**Bằng chứng đối tác đã mở xem:** `partner-evidence/DKTGMLTVV_13.jpg` — màn
`htpldn-uat.ospgroup.vn/chuyen-gia-tvv/tao-moi`, breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Thêm mới",
vai trò `hương 3 NHT` (`NHT`), đơn vị `BTP · DP`, cuối form là cặp nút `Hủy` + `Lưu` (không có `Gửi đăng ký`),
khối `File đính kèm (Bằng cấp / Chứng chỉ)` đã đính 3 tệp pdf, mốc 08/07/2026 14:54, bản `HTPLDN · V1.0`.

> **Trạng thái:** Giai đoạn A đã khóa. **CHƯA mở màn đang tranh chấp, chưa đo web** (khâu đo do người khác
> trong team thực hiện ở Giai đoạn B). Mọi ô "web/dev hiện tại" trong tài liệu này để TRỐNG cho người đo điền.

---

## 1. Tách vế expected

Nguyên văn ô **Kết quả mong đợi** (nguồn duy nhất để tách vế):

> Hệ thống tạo hồ sơ tư vấn viên với loại "Người hỗ trợ" ở trạng thái "Mới đăng ký"; tạo liên kết đến các
> lĩnh vực pháp luật đã chọn và tổ chức chủ quản (nếu có); gửi thông báo đến Cán bộ nghiệp vụ cùng đơn vị;
> lưu vết thao tác; hiển thị thông báo "Đăng ký thành công, chờ thẩm định" cùng mã hồ sơ đã tạo và chuyển
> sang trang theo dõi tiến độ.

Tách thành **10 vế** (mỗi vế khóa quan hệ riêng — cùng một câu nhưng SRS trả lời khác nhau cho từng vế):

| Vế | Trích đúng chữ trong expected |
|---|---|
| C1 | "Hệ thống tạo hồ sơ tư vấn viên" — bản ghi được tạo và lưu lại khi dữ liệu hợp lệ |
| C2 | "…với loại **Người hỗ trợ**" — giá trị trường Loại của hồ sơ vừa tạo |
| C3 | "…ở trạng thái **Mới đăng ký**" — trạng thái khởi tạo |
| C4 | "tạo liên kết đến các **lĩnh vực pháp luật đã chọn**" |
| C5 | "…và **tổ chức chủ quản (nếu có)**" |
| C6 | "gửi thông báo đến **Cán bộ nghiệp vụ cùng đơn vị**" |
| C7 | "**lưu vết thao tác**" |
| C8 | "hiển thị thông báo **"Đăng ký thành công, chờ thẩm định"**" — đúng câu chữ |
| C9 | "…**cùng mã hồ sơ đã tạo**" — thông báo có kèm mã hồ sơ |
| C10 | "**chuyển sang trang theo dõi tiến độ**" — điều hướng sau khi gửi |

**Không nằm trong expected ⇒ KHÔNG thành tiêu chí chấm** (Flow 04 §BUG SCOPE LOCK luật 1):

- **Nhãn nút submit** (`Gửi đăng ký` vs `Lưu`). Ô "Các bước thực hiện" của chính case ghi *"Dữ liệu hợp lệ và
  nhấn **Lưu**"* ⇒ nút `Lưu` là **tiền đề thao tác**, không phải kết quả mong đợi. Ô TKM nêu chuyện tên nút chỉ
  là **manh mối**. Xem §3.G để biết SRS v3.5 hiện quy định nhãn nào và vì sao câu "BA xác nhận tên button sai"
  chưa có hiệu lực trong flow này.
- **"Các trường thông tin đang không đúng với thiết kế"** (ý thứ 2 ô TKM, ghi ngày 25/7): manh mối, KHÔNG có
  trong expected ⇒ không thành tiêu chí chấm, không mở phép đo đối chiếu từng trường. Bảng trường bắt buộc của
  form vẫn được trích ở §4 để người đo **nhập liệu đúng tiền đề**, không phải để chấm.
- **Vai trò tác nhân** (NHT tự đăng ký hộ ứng viên): SRS quy định rõ (xem §3.H) nhưng expected không nhắc
  ⇒ dùng làm **tiền đề bắt buộc**, cấm tách thành bug mới.

---

## 2. Bảng BUG SCOPE LOCK

Định dạng: `Cn · expected đối tác · SRS file:dòng · MATCH/DIFF/GAP · route · đường đo`.
`MATCH` = được chấm bằng đo · `DIFF` = CẤM Pass, bắt buộc BA confirm · `GAP` = SRS im lặng/mâu thuẫn, BA confirm.

| Vế | Expected đối tác | SRS (file:dòng) | Quan hệ | Route | Đường đo (UI ngắn nhất + 1 đối chứng độc lập) |
|---|---|---|---|---|---|
| **C1** | Hệ thống tạo hồ sơ tư vấn viên | `srs-fr-04-chuyen-gia-tvv.md:326` (Processing b7 "Tạo bản ghi TU_VAN_VIEN…"), `:354` (Postcondition), `:361` (AC), `:2329` (SM-TVV `[*] → MOI_DANG_KY`) | **MATCH** | TEST | **UI:** NHT nhập đủ form `/chuyen-gia-tvv/tao-moi` → bấm `Lưu` → hồ sơ mới xuất hiện ở danh sách TVV cùng đơn vị. **Đối chứng:** đọc lại bản ghi qua API danh sách/chi tiết TVV (xác nhận endpoint ở `/api/docs-json` TRƯỚC khi gọi; endpoint đã dùng ở đợt trước: `/api/v1/tu-van-viens`) — có bản ghi đúng họ tên + `donViId` = đơn vị của NHT |
| **C2** | Loại hồ sơ = **"Người hỗ trợ"** | `:296` (Inputs #0 `loai_tvv` CHECK IN ('TVV','CG')), `:1490` (SCR-IV-02 mục 2.2 dropdown 2 lựa chọn), `:1381`–`:1386` (§3.0 ánh xạ `loai_tvv`: chỉ TVV/CG), `:2019` (entity TU_VAN_VIEN — "NHT lưu ở entity riêng NGUOI_HO_TRO"), `:137` (FR-IV-01 Inputs 1b) | **DIFF** | **BA** | **CẤM Pass.** Chỉ đo hiện trạng tối thiểu để biết dev theo phía nào: đọc danh sách lựa chọn của ô "Loại" trên chính form (đếm + đọc nhãn từng option bằng `innerText`), KHÔNG bấm gì thêm. Ghi vào §5 câu hỏi BA-1 |
| **C3** | Trạng thái = "Mới đăng ký" | `:349` (Outputs #2 `trang_thai` = MOI_DANG_KY), `:326` (Processing b7 "…trạng thái = MOI_DANG_KY"), `:1350` (§3.0: MOI_DANG_KY → "Mới đăng ký"), `:2314` + `:2329` (SM-TVV) | **MATCH** | TEST | **UI:** badge trạng thái của hồ sơ vừa tạo (danh sách hoặc màn chi tiết) hiển thị "Mới đăng ký". **Đối chứng:** trường trạng thái trong phản hồi API của đúng bản ghi đó = `MOI_DANG_KY`. *(Ghi chú phụ thuộc: vế này chấm trên bản ghi tạo từ SCR-IV-02 — đúng màn trong bằng chứng đối tác. Nếu BA trả lời C2 theo hướng khác, quan hệ C3 phải suy lại từ dòng SRS mới, không tự đổi.)* |
| **C4** | Tạo liên kết đến các lĩnh vực pháp luật đã chọn | `:309` (Inputs #13 `linh_vuc_ids` bắt buộc ≥1), `:326` (Processing b7 ghi `linh_vuc_ids`), `:1517` (SCR-IV-02 mục 4.3), `:172` (FR-IV-01 Processing b5 "…+ TVV_LINH_VUC") | **MATCH** | TEST | **UI:** mở chi tiết hồ sơ vừa tạo → tab "Hồ sơ" nhóm Lĩnh vực hiển thị **đúng cả 2 lĩnh vực đã chọn** (chọn 2 để phép đo có nghĩa). **Đối chứng:** mảng lĩnh vực trong phản hồi API chi tiết của bản ghi = đúng 2 id đã chọn (đọc key thật trong schema, không đoán tên khóa) |
| **C5** | Tạo liên kết tổ chức chủ quản (nếu có) | `:310` (Inputs #14 `to_chuc_id`, không bắt buộc, FK → TO_CHUC_TU_VAN), `:1515` (SCR-IV-02 mục 4.1 "Tổ chức chính" — tùy chọn), `:326` (Processing b7 ghi `to_chuc_chinh_id`), `:2026` (entity `to_chuc_chinh_id`), `:2117`–`:2126` (bảng N:N TVV_TO_CHUC) | **MATCH** | TEST | **UI:** cùng lượt tạo ở C1, chọn 1 tổ chức ở ô "Tổ chức chính" → chi tiết hồ sơ hiển thị đúng tên tổ chức đó. **Đối chứng:** trường tổ chức chính trong phản hồi API chi tiết trỏ đúng tổ chức đã chọn. **Nếu dropdown rỗng** (đơn vị chưa có tổ chức tư vấn nào) → ghi **Chưa đo được** cho riêng C5 + nêu thiếu dữ kiện gì; KHÔNG Pass, KHÔNG Fail, KHÔNG tự mở màn Tổ chức tư vấn để tạo trừ khi khai báo seed theo §4.5 |
| **C6** | Gửi thông báo đến Cán bộ nghiệp vụ cùng đơn vị | `:327` (Processing b8 "Gửi thông báo cho Cán bộ Nghiệp vụ cùng đơn vị"), `:356` (Postcondition), `:361` (AC), `:1522` (SCR-IV-02 cell 7 — nội dung "Hồ sơ tư vấn viên mới đăng ký: [tên]") | **MATCH** | TEST | **CẦN TÀI KHOẢN THỨ HAI.** **UI:** đăng nhập tài khoản **Cán bộ Nghiệp vụ CÙNG ĐƠN VỊ với NHT vừa thao tác** → màn Thông báo → có thông báo về hồ sơ TVV mới, nội dung khớp tên ứng viên vừa tạo, **mốc giờ nằm sau** thời điểm bấm Lưu. **Đối chứng:** danh sách thông báo của chính tài khoản đó qua API (đọc schema trước). **Chống phép đo nói dối:** đối chiếu theo **mốc giờ + tên ứng viên**, KHÔNG kết luận bằng độ dài mảng/số badge |
| **C7** | Lưu vết thao tác | `:328` (Processing b9 "Ghi nhật ký thao tác" — BR-DATA-05), `:2514` (BR-DATA-05: mọi thao tác CUD ghi AUDIT_LOG, immutable) | **MATCH** | TEST | **UI:** tài khoản `admin` (QTHT) → Quản trị hệ thống → Nhật ký hệ thống (`srs-fr-10-quan-tri.md:1373` — chỉ QTHT truy cập) → lọc Người dùng = tài khoản NHT vừa thao tác, Module = `CG-TVV`, Loại thao tác = `Tạo`, ngày = hôm nay → có dòng khớp mốc giờ + mã bản ghi. **Đối chứng:** cột "Chi tiết thay đổi" của đúng dòng đó chứa bản ghi vừa tạo. *(Dùng `admin` chỉ để ĐỌC side-effect; hành động đang verify vẫn do NHT bấm trên UI thật)* |
| **C8** | Thông báo "Đăng ký thành công, chờ thẩm định" | `:351` (Outputs #4 `thong_bao` = "Đăng ký thành công, chờ thẩm định"), `srs-v3.5.md:576` (UI-04 — toast cho thao tác thành công), `srs-v3.5.md:6759` (H7 — "…kèm toast thông báo") | **MATCH** | TEST | **VẾ EPHEMERAL — bắt buộc cài bộ bắt thông báo TRƯỚC khi bấm `Lưu`.** `MutationObserver` trên `document.body`, đọc `innerText` (KHÔNG `textContent` — node ẩn AntD gây bug ma), **CẤM lọc trùng**, ghi lại đủ mọi toast xuất hiện + mốc giờ. **Đối chứng:** phản hồi máy chủ của chính request tạo hồ sơ (thân phản hồi là bằng chứng mạnh hơn ảnh nếu trượt toast) |
| **C9** | Thông báo kèm **mã hồ sơ đã tạo** | **IM LẶNG.** Đã đọc trọn §Outputs FR-IV-03 (`:344`–`:351`): `ma_tvv` là Output #1 (`:348`) còn `thong_bao` là Output #4 (`:351`) — SRS **không** ghi thông báo phải chứa mã. Đọc thêm SCR-IV-02 cell 7 (`:1522`) và §Postconditions (`:353`–`:357`): cũng không ghi. Đối chứng ngược: khi SRS muốn kèm mã thì viết rõ — FR-IV-07 Processing b2 (`:597`) "gửi mail link kích hoạt … **kèm mã số TVV**" | **GAP** | **BA** | Không thêm phép đo mới. Dùng **đúng chuỗi toast đã bắt ở C8**: ghi lại toast có/không chứa chuỗi dạng `TVV-…`. Ghi vào §5 câu hỏi BA-2 |
| **C10** | Chuyển sang **trang theo dõi tiến độ** | `srs-v3.5.md:6759` (Phụ lục E §H7, **BẮT BUỘC**: "Sau khi thực hiện thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang **Danh sách (SCR-XX-01)** kèm toast thông báo. Trừ trường hợp đối tác/CĐT yêu cầu giữ lại trang Chi tiết bản ghi vừa tạo — **phải có ghi chú riêng tại FR cụ thể**"). FR-IV-03 và SCR-IV-02 (`:1470`–`:1529`) KHÔNG có ghi chú ngoại lệ nào; grep toàn thư mục v3.5 cho "trang theo dõi tiến độ" chỉ ra 1 kết quả thuộc `srs-fr-15-ct-htpldn.md:621` (đợt báo cáo CT HTPLDN — khác nghiệp vụ) | **DIFF** | **BA** | **CẤM Pass.** Chỉ đo hiện trạng: sau khi bấm `Lưu`, đọc `location.href` + breadcrumb (không bấm thêm) và ghi lại. Ghi vào §5 câu hỏi BA-3 |

**Tổng kết quan hệ:** MATCH 7 (C1, C3, C4, C5, C6, C7, C8) · DIFF 2 (C2, C10) · GAP 1 (C9).

**Hệ quả logic đã khóa trước khi đo** (Flow 04 §Ca biên "Case gộp nhiều vế"):

- Vì đã có `DIFF` + `GAP`, case này **không thể ra Pass** dù mọi vế MATCH đều đạt.
- Mọi vế MATCH đạt hết → verdict logic = **Cần BA**.
- Có ≥1 vế MATCH không đạt → verdict logic = **Reopen + Cần BA** (nêu riêng phần lỗi và câu hỏi BA).
- Kết quả web **không được** biến `DIFF`/`GAP` thành `MATCH` (luật khóa 5). Chỉ được đổi quan hệ khi dẫn được
  **dòng SRS mới đọc được**, phải ghi lý do và đo lại phần bị ảnh hưởng.

---

## 3. Trích dẫn SRS nguyên văn

> Mọi dòng dưới đây đều **tự mở file trong lượt này** để đọc. Dán đủ để người khác kiểm lại.

### A. Ai được đăng ký, ở màn nào (tiền đề của toàn bộ case)

`srs-fr-04-chuyen-gia-tvv.md:280-284`
```
### FR-IV-03: Đăng ký tham gia mạng lưới (UC41)

**UC Reference:** UC 41
**Priority:** Essential | **Stability:** High
**Màn hình:** SCR-IV-02 (chức năng quản lý của Người hỗ trợ)
```

`srs-fr-04-chuyen-gia-tvv.md:286`
```
**Mô tả:** Người hỗ trợ pháp lý (NHT — cán bộ HTPL theo NĐ 55/2019 Đ.7) submit hồ sơ ứng viên TVV/CG vào mạng lưới tư vấn viên thuộc đơn vị mình.
```

`srs-fr-04-chuyen-gia-tvv.md:288`
```
**Tác nhân:** Người hỗ trợ pháp lý (NHT) — đã có tài khoản do quản trị/cán bộ cấp; đăng nhập bằng tên đăng nhập + mật khẩu
```

`srs-fr-04-chuyen-gia-tvv.md:1474-1479` (SCR-IV-02 — đúng URL trong ảnh đối tác)
```
**Đường dẫn:** `/chuyen-gia-tvv/tao-moi` hoặc `/chuyen-gia-tvv/:id/chinh-sua`
**Quyền truy cập:**
- Người hỗ trợ pháp lý (NHT): submit hồ sơ ứng viên TVV/CG vào mạng lưới + cập nhật thông tin TVV/CG cùng đơn vị
- Cán bộ Nghiệp vụ: **chỉ xem** hồ sơ TVV/CG cùng đơn vị (FR-IV-05 / UC43 — CSV chỉ có giao dịch xem danh sách, tìm kiếm, xem chi tiết, xuất file); sửa lĩnh vực chuyên môn thì qua FR-IV-06 §Processing trong lúc thẩm định `[sửa 2026-07-31 — TDHSTVV_13]`
- Tư vấn viên / Chuyên gia (chủ hồ sơ): chỉ xem hồ sơ của mình ở chế độ chỉ đọc qua chuyên trang — không có nút sửa; muốn thay đổi → liên hệ NHT
- Chỉ cho phép sửa khi trạng thái khác "Vô hiệu hóa"
```

### B. C2 — Loại hồ sơ: SRS chỉ có TVV / CG, KHÔNG có "Người hỗ trợ"

`srs-fr-04-chuyen-gia-tvv.md:296` (FR-IV-03 §Inputs, dòng đầu bảng)
```
| 0 | loai_tvv | text | Y | CHECK IN ('TVV','CG') | 'TVV' | NHT chọn (radio) |
```

`srs-fr-04-chuyen-gia-tvv.md:1490` (SCR-IV-02 §Thành phần màn hình, mục 2.2)
```
| 2.2 | nhóm 1 | Loại * | dropdown 2 lựa chọn | "Tư vấn viên" / "Chuyên gia" — mặc định "Tư vấn viên" | — |
```

`srs-fr-04-chuyen-gia-tvv.md:1381-1386` (§3.0 bảng ánh xạ — đóng tập giá trị)
```
**Loại tư vấn viên (loai_tvv):**

| Mã enum DB | Label hiển thị | Màu badge |
|-----------|----------------|-----------|
| TVV | Tư vấn viên | Xanh dương |
| CG | Chuyên gia | Tím |
```

`srs-fr-04-chuyen-gia-tvv.md:2019` (entity TU_VAN_VIEN)
```
| loai_tvv | text | Y | CHECK IN ('TVV','CG') | | Loại: TVV (có thẻ NĐ 77/2008 Đ.19) / CG (chuyên gia). NHT lưu ở entity riêng NGUOI_HO_TRO |
```

`srs-fr-04-chuyen-gia-tvv.md:137` (FR-IV-01 §Inputs 1b — nhắc lại cùng ràng buộc)
```
| 1b | loai_tvv | text | Y | CHECK IN ('TVV','CG') — chỉ cá nhân ngoài hành nghề tư vấn theo NĐ 77/2008. NHT (cán bộ HTPL theo NĐ 55/2019 Đ.7) lưu ở entity riêng NGUOI_HO_TRO | 'TVV' | Người dùng (dropdown) |
```

`srs-fr-04-chuyen-gia-tvv.md:18` (Lịch sử thay đổi — vì sao NHT bị gỡ khỏi `loai_tvv`)
```
| 2026-05-03 | BA + Claude | Apply 7 fix theo deep review per-module FR-04 v3: … F-FR04-NEW-02 phương án B+ (refactor NHT: bỏ NHT khỏi loai_tvv enum + tạo entity NGUOI_HO_TRO 1:1 với TAI_KHOAN) … |
```

`srs-fr-04-chuyen-gia-tvv.md:2087-2096` (bảng "Phân biệt với TU_VAN_VIEN" — NHT là entity + màn khác)
```
**Phân biệt với TU_VAN_VIEN:**

| Tiêu chí | TU_VAN_VIEN (TVV/CG) | NGUOI_HO_TRO (NHT) |
…
| Workflow | MOI_DANG_KY → CHO_THAM_DINH → DANG_THAM_DINH → CHO_PHE_DUYET → CHO_KICH_HOAT → HOAT_DONG (10 trạng thái) | CHO_KICH_HOAT → HOAT_DONG → TAM_DUNG → VO_HIEU_HOA (4 trạng thái) |
…
| Đường vào hệ thống | Người hỗ trợ đăng ký hộ hồ sơ ứng viên (FR-IV-03); tài khoản chỉ được cấp sau khi Cán bộ Phê duyệt duyệt | Tài khoản nội bộ do quản trị cấp (FR-X) |
```

`srs-fr-04-chuyen-gia-tvv.md:1799` (màn tạo NHT là màn KHÁC, URL KHÁC)
```
**Đường dẫn:** `/chuyen-gia-tvv/nguoi-ho-tro/tao-moi` hoặc `/chuyen-gia-tvv/nguoi-ho-tro/:id/chinh-sua`
```

`srs-fr-04-chuyen-gia-tvv.md:2073` (entity NGUOI_HO_TRO — trạng thái khởi tạo KHÔNG phải "Mới đăng ký")
```
| 8 | trang_thai | text | Y | CHECK IN ('CHO_KICH_HOAT','HOAT_DONG','TAM_DUNG','VO_HIEU_HOA') | 'CHO_KICH_HOAT' | Trạng thái (SM-NHT — 4 trạng thái). Mới tạo = CHO_KICH_HOAT (chờ NHT bấm link kích hoạt + đặt mật khẩu lần đầu); sau đó chuyển HOAT_DONG. Cán bộ không cần workflow thẩm định 4 tiêu chí như TVV cá nhân |
```

> **Đọc ra:** trên chính màn của bằng chứng (`/chuyen-gia-tvv/tao-moi` = SCR-IV-02), SRS v3.5 chỉ cho hồ sơ mang
> loại `TVV` hoặc `CG`. "Người hỗ trợ" trong SRS v3.5 là **vai trò người thao tác** (tác nhân của FR-IV-03) và là
> **một entity riêng** tạo ở màn khác với trạng thái khởi tạo khác. Expected đối tác đang gán "Người hỗ trợ" làm
> **giá trị trường Loại của hồ sơ** ⇒ ngược SRS ⇒ `DIFF`, cấm Pass, phải BA confirm.

### C. C1 + C3 — tạo bản ghi và trạng thái khởi tạo

`srs-fr-04-chuyen-gia-tvv.md:316-328` (§Processing đầy đủ)
```
**Processing:**

| Bước | Mô tả xử lý | BR áp dụng |
|------|-------------|-----------|
| 1 | Kiểm tra ứng viên chưa có hồ sơ đang chờ xử lý (theo CCCD, trạng thái ∈ {MOI_DANG_KY, CHO_THAM_DINH, DANG_THAM_DINH, YEU_CAU_BO_SUNG, CHO_PHE_DUYET}) | — |
| 2 | Kiểm tra nếu có hồ sơ trước TU_CHOI → cho phép sửa và chuyển lại CHO_THAM_DINH (KHÔNG có cooldown — BA chốt 2026-05-03) | — |
| 3 | Xác nhận dữ liệu đầu vào | — |
| 4 | Kiểm tra CMND/CCCD duy nhất toàn hệ thống | — |
| 5 | Kiểm tra email duy nhất toàn hệ thống | — |
| 6 | Quét virus cho tất cả file upload | — |
| 7 | Tạo bản ghi TU_VAN_VIEN với đầy đủ các trường nhập (loai_tvv, ho_ten, cccd, ngay_sinh, gioi_tinh, email, dien_thoai, dia_chi, chuc_vu, noi_cong_tac, trinh_do, chuyen_nganh, so_nam_kinh_nghiem, linh_vuc_ids, to_chuc_chinh_id, anh_dai_dien, **don_vi_id (auto từ NHT.don_vi_id)**), trạng thái = MOI_DANG_KY | SM-TVV |
| 8 | Gửi thông báo cho Cán bộ Nghiệp vụ cùng đơn vị | — |
| 9 | Ghi nhật ký thao tác | BR-DATA-05 |
```

`srs-fr-04-chuyen-gia-tvv.md:344-351` (§Outputs đầy đủ — nguồn của C3, C8, C9)
```
**Outputs:**

| # | Tên | Kiểu logic | Điều kiện | Format |
|---|-----|-----------|-----------|--------|
| 1 | ma_tvv | text | — | TVV-{CODE}-{SEQ} (auto-gen) |
| 2 | trang_thai | text | — | MOI_DANG_KY |
| 3 | ngay_dang_ky | datetime | — | dd/mm/yyyy HH:mm |
| 4 | thong_bao | text | — | "Đăng ký thành công, chờ thẩm định" |
```

`srs-fr-04-chuyen-gia-tvv.md:353-357` (§Postconditions đầy đủ — nguồn của C1, C6)
```
**Postconditions:**
- Hồ sơ TVV/CG được tạo với trạng thái MOI_DANG_KY, gắn đơn vị quản lý theo NHT đăng ký
- TVV/CG (chủ hồ sơ) chưa có tài khoản hệ thống. Liên lạc qua email/điện thoại đã khai
- Cán bộ Nghiệp vụ cùng đơn vị nhận thông báo hồ sơ mới
- Khi hồ sơ chuyển CHO_KICH_HOAT (sau khi Cán bộ Phê duyệt duyệt — xem FR-IV-07), hệ thống tự cấp tài khoản + gửi mail kích hoạt cho TVV/CG
```

`srs-fr-04-chuyen-gia-tvv.md:359-363` (§Acceptance Criteria)
```
**Acceptance Criteria:**
- **Given** NHT đã đăng nhập **When** chọn "Đăng ký TVV vào mạng lưới" **Then** form đăng ký mở với 19 trường, trường "Đơn vị quản lý" hiển thị tên đơn vị NHT (chỉ xem)
- **Given** NHT nhập đủ + upload file **When** gửi **Then** tạo hồ sơ TVV với don_vi_id = NHT.don_vi_id, trạng thái = MOI_DANG_KY, Cán bộ Nghiệp vụ cùng đơn vị nhận thông báo
- **Given** ứng viên (theo CCCD) đã có hồ sơ chờ **When** NHT đăng ký lại **Then** hệ thống từ chối với ERR-DK-01
- **Given** email đã tồn tại trong hệ thống **When** NHT submit **Then** hệ thống từ chối với ERR-DK-09
```

`srs-fr-04-chuyen-gia-tvv.md:1350` (§3.0 ánh xạ trạng thái)
```
| MOI_DANG_KY | Mới đăng ký | Xanh dương nhạt |
```

`srs-fr-04-chuyen-gia-tvv.md:2314` + `:2329` (SM-TVV)
```
| Mới đăng ký | MOI_DANG_KY | Người hỗ trợ vừa submit hồ sơ ứng viên TVV/CG | Xanh dương |
…
| [*] | MOI_DANG_KY | Người hỗ trợ submit hồ sơ ứng viên TVV/CG | — | Tạo hồ sơ TVV | FR-IV-03 | — |
```

### D. C4 + C5 — lĩnh vực pháp luật và tổ chức chủ quản

`srs-fr-04-chuyen-gia-tvv.md:309-311` (FR-IV-03 §Inputs)
```
| 13 | linh_vuc_ids | identifier[] | Y | ≥ 1 lĩnh vực PL đăng ký | — | NHT chọn (multi) |
| 14 | to_chuc_id | identifier | N | FK → TO_CHUC_TU_VAN | — | NHT chọn |
| 15 | don_vi_id | identifier | Y | FK → DON_VI; auto-set theo đơn vị NHT đang đăng nhập (chỉ xem, không sửa) | NHT.don_vi_id | system |
```

`srs-fr-04-chuyen-gia-tvv.md:1514-1517` (SCR-IV-02 nhóm 3)
```
| 4 | nhóm 3 | Tổ chức & Mạng lưới | nhóm thu gọn | — | — |
| 4.1 | nhóm 3 | Tổ chức chính | dropdown có tìm kiếm | Tùy chọn — tư vấn viên tự do để trống | Lỗi nếu chọn tổ chức không tồn tại |
| 4.2 | nhóm 3 | Tổ chức đối tác | dropdown chọn nhiều | Tùy chọn — N:N | — |
| 4.3 | nhóm 3 | Lĩnh vực pháp luật * | dropdown chọn nhiều | Bắt buộc ≥ 1 | Lỗi rỗng: "Vui lòng chọn ít nhất 1 lĩnh vực pháp luật" |
```

`srs-fr-04-chuyen-gia-tvv.md:172` (FR-IV-01 §Processing — SRS gọi tên 2 bảng liên kết)
```
| 5 | Tạo bản ghi TU_VAN_VIEN + TVV_TO_CHUC + TVV_LINH_VUC | BR-DATA-03 |
```

`srs-fr-04-chuyen-gia-tvv.md:2026` (entity TU_VAN_VIEN — trường tổ chức chính)
```
| to_chuc_chinh_id | identifier | N | FK → TO_CHUC_TU_VAN(id) | | Tổ chức hành nghề chính `[CR-02]` |
```

> **Đọc ra:** "tổ chức chủ quản (nếu có)" của đối tác khớp trường SRS gọi là **"Tổ chức chính"** /
> `to_chuc_chinh_id`, và khớp cả tính **tùy chọn** ("nếu có" ↔ Bắt buộc = N). Khác chữ, không khác yêu cầu
> ⇒ `MATCH`, không tách thành DIFF về từ ngữ.

### E. C6 — thông báo tới Cán bộ Nghiệp vụ cùng đơn vị

`srs-fr-04-chuyen-gia-tvv.md:327` (Processing bước 8 — cột BR để trống, tức SRS không gắn mã BR nào)
```
| 8 | Gửi thông báo cho Cán bộ Nghiệp vụ cùng đơn vị | — |
```

`srs-fr-04-chuyen-gia-tvv.md:1522` (SCR-IV-02 cell 7 — nội dung thông báo, đọc nguyên văn cả ô)
```
| 7 | thanh hành động | 2 nút Hủy / Lưu | nhóm nút | "Hủy" (phụ) / "Lưu" (chính) | Hủy: nếu có thay đổi chưa lưu → MD-XOA xác nhận. Lưu: tạo mới hoặc cập nhật; nếu tạo mới → đặt trạng thái Mới đăng ký + thông báo Cán bộ Nghiệp vụ cùng đơn vị "Hồ sơ tư vấn viên mới đăng ký: [tên]" |
```

> **Đọc ra — giới hạn của C6:** SRS chốt **người nhận** ("Cán bộ Nghiệp vụ cùng đơn vị") và **nội dung**
> ("Hồ sơ tư vấn viên mới đăng ký: [tên]"), nhưng **KHÔNG chốt mã thông báo và KHÔNG chốt kênh** cho sự kiện
> này: bước 8 để trống cột BR, và danh mục sự kiện của `BR-NOTIF-01` (`srs-v3.5.md:5657`, đã đọc trọn 9 nhóm
> sự kiện) **không liệt kê sự kiện đăng ký hồ sơ TVV mới**. Vì vậy chỉ chấm **đúng người nhận + đúng bản ghi**;
> **không** được chấm Fail vì thiếu email, thiếu mã thông báo hay sai kênh — những thứ SRS không quy định.

### F. C7 — lưu vết thao tác

`srs-fr-04-chuyen-gia-tvv.md:328`
```
| 9 | Ghi nhật ký thao tác | BR-DATA-05 |
```

`srs-fr-04-chuyen-gia-tvv.md:2510-2514`
```
### BR-DATA-05: Audit trail

| ID | Phát biểu quy tắc | Nguồn | Áp dụng FR (nhóm IV) | Ngoại lệ | Kiểm chứng |
|----|-------------------|-------|---------------------|---------|------------|
| BR-DATA-05 | Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Log là immutable, không sửa/xóa | NFR-06 | Toàn bộ FR nhóm IV | — | Verify INSERT-only trên AUDIT_LOG |
```

`srs-fr-10-quan-tri.md:1373` (nơi đọc được nhật ký)
```
**Mô tả:** Tra cứu, lọc và xuất nhật ký thao tác toàn hệ thống (audit log). Chỉ QTHT truy cập. Dữ liệu read-only, không sửa/xóa.
```

`srs-fr-10-quan-tri.md:1388` (giá trị bộ lọc — dùng để tra đúng dòng)
```
| 5 | hanh_dong | select | N | Tạo / Sửa / Xóa / Phê duyệt / Từ chối / **Hủy** / **Phân công** / **Công khai** / **Hủy công khai** / Đăng nhập / Đăng xuất `[đồng bộ 2026-08-06 — đủ 11 giá trị của `AUDIT_LOG.hanh_dong`]` | — | user input |
```

### G. Nhãn nút submit — SRS v3.5 hiện ghi gì (KHÔNG phải tiêu chí chấm)

`srs-fr-04-chuyen-gia-tvv.md:1522` (đã dán ở §E): `"Hủy" (phụ) / "Lưu" (chính)`.

`srs-v3.5.md:6756` (Phụ lục E §H4 — quy ước UI chung, BẮT BUỘC, áp cho **mọi màn hình**)
```
| **H4** | Nhãn nút thống nhất | Nút thêm mới luôn đặt nhãn **"Thêm mới"** (không "Tạo mới", "Tạo", "Thêm", "Mới"…). Nút lưu luôn **"Lưu"** (không "Lưu lại", "Cập nhật", "Hoàn tất"…). Trường hợp đặc thù (vd. "Phê duyệt", "Gửi") giữ nguyên — không nhầm với Lưu. | BẮT BUỘC |
```

Kiểm dấu thay đổi (đúng yêu cầu "không kết luận bằng một lệnh grep rỗng"):

- Chuỗi `Gửi đăng ký`: **0 kết quả** trên toàn thư mục `srs-v3.5/` (đã grep cả 18 tệp).
- Dấu thay đổi `[STT…]` trong `srs-fr-04-chuyen-gia-tvv.md`: **0 kết quả**.
- Dấu `[CR-…]` / `[BA chốt …]` gần vùng nút SCR-IV-02: đã đọc trọn `:1483`–`:1529`. Các dấu có mặt đều thuộc
  trường dữ liệu (`:1499` DKTGMLTVV_02 P2 — bỏ dấu sao "Đơn vị quản lý"; `:1510`/`:1511` DKTGMLTVV_03a/b/c —
  Chuyên ngành, Số năm kinh nghiệm; `:1528` TDHSTVV_13 — chủ thể thao tác). **Không dấu nào chạm nhãn nút.**
- 3 đợt áp UAT gần nhất vào FR-04 (`:24` ngày 2026-07-16, `:26` ngày 2026-07-30, `:27` ngày 2026-07-31) liệt kê
  chi tiết từng vị trí sửa — **không đợt nào đổi nhãn nút của SCR-IV-02**, dù đợt 2026-07-30 có xử đúng nhóm mã
  `DKTGMLTVV_02` / `DKTGMLTVV_03`.

> **Đọc ra:** tới bản SRS chốt hiện hành, nhãn nút submit của màn này là **"Lưu"** — trùng đúng cái đối tác nhìn
> thấy trên web và trùng đúng bước thao tác của chính case ("nhấn Lưu"). Câu *"BA xác nhận tên button sai"* trong
> ô TKM **chưa được nhập vào bản SRS này**, nên theo Flow 04 §Nguồn chuẩn duy nhất, quyết định đó **chưa có hiệu
> lực** trong lượt verify này. Đây là **ghi nhận ngoài phạm vi chấm**, KHÔNG phải bug, KHÔNG phải vế Cn, và
> KHÔNG mở phép đo riêng: nếu đội muốn đổi nhãn nút thì phải đi đường sửa đặc tả (BA cập nhật SCR-IV-02 + §H4),
> không đi đường verify case này.

### H. Vai trò tác nhân (tiền đề, không tách bug)

`srs-fr-04-chuyen-gia-tvv.md:288` + `:1476`–`:1477` (đã dán ở §A) + `:290`:
```
**Preconditions:** NHT đã đăng nhập, có quyền "Đăng ký TVV vào mạng lưới" theo phân công vai trò + đơn vị.
```

`srs-fr-04-chuyen-gia-tvv.md:2482` (BR-AUTH-08 — phạm vi đơn vị)
```
| BR-AUTH-08 | Cán bộ Nghiệp vụ (NHT) / Cán bộ Phê duyệt chỉ CRUD được bản ghi có `don_vi_id = current_user.don_vi_id`. … **NHT** (cán bộ HTPL theo NĐ 55/2019 Đ.7) có quyền theo phân công VAI_TRO + đơn vị, KHÔNG sở hữu hồ sơ TVV. | PRD A4 | Toàn bộ FR nhóm IV có CRUD | … |
```

> **Đọc ra:** vai trò trong ảnh đối tác (`NHT`, cấp DP) **đúng** với SRS ⇒ dùng nguyên làm tiền đề; không có gì
> để tách thành bug ở vế vai trò.

---

## 4. Tiền đề + dữ liệu nhập cần chuẩn bị cho Giai đoạn B

### 4.1 Môi trường và vai trò

| Mục | Giá trị |
|---|---|
| Env đo | `https://18.143.165.120.nip.io` (env NỘI BỘ) · MailHog `http://18.143.165.120:8025` |
| Màn đo | `/chuyen-gia-tvv/tao-moi` (SCR-IV-02) — vào bằng **click menu**: Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia → nút "+ Thêm tư vấn viên" |
| Vai trò bắt buộc | **NHT** (Người hỗ trợ pháp lý). Bộ `_05` mà prompt chỉ định **không có tài khoản NHT** ⇒ phải mượn NHT sẵn có, giữ nguyên vai trò/cấp của bằng chứng đối tác (NHT cấp ĐP) |
| Tài khoản NHT đề xuất (ưu tiên 1, khớp cấp ĐP như ảnh đối tác) | `nht_ag_uat2` / `Test@1234` (Sở Tư pháp An Giang — NHT-STP-AG-0001, Đang hoạt động). Dự phòng cùng vai trò + cùng đơn vị: `nht_qa_01` / `Test@1234` |
| Tài khoản thứ hai (chỉ cho C6) | **Cán bộ Nghiệp vụ CÙNG ĐƠN VỊ với NHT ở trên** — thử `cbnv_dp_05` / `Test@1234` trước (đúng bộ `_05` prompt chỉ định); nếu login fail thì fallback đúng Rule 7 (cùng vai trò CB_NV_DP + cùng cấp ĐP): `cbnv_dp_01` |
| Tài khoản đọc nhật ký (chỉ cho C7) | `admin` / `Secret@123` (QTHT) — chỉ ĐỌC side-effect, không thao tác nghiệp vụ |
| Phương án dự phòng nếu cặp ĐP không cùng đơn vị | Chuyển sang cặp TW: NHT = `nht_qa_tw`, CB NV = `cbnv_tw_05`. Ghi rõ đã đổi cấp trong báo cáo |

> **BẮT BUỘC TRƯỚC KHI CHẤM C6:** xác nhận NHT và CB NV **cùng `donViId`** (đọc từ phản hồi đăng nhập / endpoint
> thông tin phiên — đọc schema trước, cấm đoán tên khóa). `don_vi_id` của hồ sơ được auto-set theo NHT
> (`srs-fr-04-chuyen-gia-tvv.md:311`), nên CB NV khác đơn vị sẽ **không** nhận thông báo và sẽ tạo Fail oan.
> Không xác minh được đơn vị ⇒ C6 ghi **Chưa chốt**, không ghi Fail.

### 4.2 Trường bắt buộc của form (dùng để nhập đúng, KHÔNG dùng để chấm)

Từ `srs-fr-04-chuyen-gia-tvv.md:292`–`:314` (FR-IV-03 §Inputs) và `:1485`–`:1522` (SCR-IV-02):

| Nhóm | Trường bắt buộc | Ràng buộc phải tuân |
|---|---|---|
| 1 — Thông tin cá nhân | Loại, Họ tên, Ngày sinh, Giới tính, Số CCCD, Email, Số điện thoại, Địa chỉ | CCCD ≤12 ký tự **duy nhất toàn hệ thống**; Email đúng định dạng **duy nhất toàn hệ thống**; SĐT `^0\d{9,10}$`; Giới tính chỉ Nam/Nữ; Ngày sinh ≤ hôm nay |
| 1 | Đơn vị quản lý | Chỉ đọc, hệ thống tự gán = đơn vị NHT (`:1499`) — **không nhập** |
| 2 — Nghề nghiệp | Trình độ, **Chuyên ngành**, **Số năm kinh nghiệm** | Chuyên ngành + Số năm kinh nghiệm **bắt buộc khi NHT đăng ký mới** (`:1510`, `:1511`) |
| 2 | Số thẻ hành nghề + File thẻ hành nghề | **Bắt buộc nếu Loại = "Tư vấn viên"** (`:1507`, `:1508`, `:314`) |
| 3 — Tổ chức & Mạng lưới | Lĩnh vực pháp luật (≥1) | Chọn **2 lĩnh vực** để C4 có sức chứng minh |
| 3 | Tổ chức chính | Tùy chọn — nhưng **phải chọn 1** thì mới đo được C5 |
| 4 — File đính kèm | Bằng cấp / Chứng chỉ | Bắt buộc; PDF, ≤10MB/file, tổng ≤50MB, ≤10 file |
| 5 — Ghi chú | — | Tùy chọn |

### 4.3 Bộ dữ liệu nhập đề xuất (mỗi lần chạy phải đổi CCCD + Email để không đụng ERR-DK-04 / ERR-DK-09)

| Trường | Giá trị đề xuất |
|---|---|
| Loại | **Tư vấn viên** (mặc định SRS `'TVV'`, sát tên case "…mạng lưới tư vấn viên"). Chọn giá trị này thì **bắt buộc** có Số thẻ + File thẻ hành nghề |
| Họ tên | `QA F6 DKTGMLTVV13 <HHmm>` |
| Ngày sinh | `01/01/1990` |
| Giới tính | Nam |
| Số CCCD | 12 số sinh theo dấu thời gian chạy (vd `0868` + `HHmmss` + 2 số ngẫu nhiên) — **không tái dùng** |
| Email | `qa.f6.dktgmltvv13.<HHmmss>@htpldn.test` — **không tái dùng** |
| Số điện thoại | `0912345678` |
| Địa chỉ | `Số 1 QA Test, An Giang` |
| Trình độ | Cử nhân |
| Chuyên ngành | `Luật kinh tế` |
| Số năm kinh nghiệm | `5` |
| Số thẻ hành nghề | `TVV-QA-F6-001` |
| Lĩnh vực pháp luật | **2 lĩnh vực** (vd `Thương mại` + `Lao động`) — ghi lại đúng 2 tên đã chọn |
| Tổ chức chính | 1 tổ chức bất kỳ đang có trong dropdown — **ghi lại tên**; dropdown rỗng thì xử theo §4.5 |
| Ghi chú | `Seed Flow04 F6 DKTGMLTVV_13` |

### 4.4 Tệp đính kèm — fixture PDF THẬT, đã kiểm tra, dùng lại

| Tệp | Đường dẫn | Kiểm chứng |
|---|---|---|
| Bằng cấp / Chứng chỉ | `output/UAT_doi-tac/reverify-week-5/F6-flow04-3case-2026-08-07/seed-files/QA-F6-bangcap-chungchi.pdf` | `file` → `PDF document, version 1.4, 1 pages`; PyMuPDF mở được, 1 trang, nội dung `QA LKHDG_16 seed 2026-08-06`. **Là PDF thật, không phải đổi đuôi** |
| File thẻ hành nghề (khi Loại = Tư vấn viên) | dùng lại **chính tệp trên** | Cùng lý do; SRS chỉ đòi PDF ≤10MB |

Đã rà cả `reverify-week-5/seed-files/`: chỉ có 5 tệp `.png` cỡ 73–99 byte và 1 `.xlsx` — **không dùng** cho case
này (không phải PDF; các `.png` nhỏ bất thường, chưa kiểm chứng là ảnh thật). **Cấm** tạo tệp văn bản rồi đổi
đuôi `.pdf`.

### 4.5 Nếu dropdown "Tổ chức chính" rỗng

1. Ưu tiên: ghi C5 = **Chưa đo được**, nêu rõ "đơn vị của NHT chưa có Tổ chức tư vấn nào trong dropdown".
   Không Pass, không Fail cho riêng C5; các vế còn lại vẫn chấm bình thường.
2. Chỉ khi cần khép kín C5 mới seed 1 Tổ chức tư vấn qua UI (`cbnv_dp_05` → màn Tổ chức tư vấn, SCR-IV-NEW-02).
   Đây là **mutate môi trường** ⇒ bắt buộc khai vào báo cáo: **đổi/tạo bản ghi nào · đổi gì · trên env nào**.
   Cấm ghi thẳng DB, cấm đoán endpoint.

### 4.6 Thứ tự phép đo (một lượt tạo hồ sơ trả lời được C1, C3, C4, C5, C8, C9, C10)

| Bước | Việc | Trả lời vế |
|---|---|---|
| 0 | Tải lại trang, ghi mốc giờ + bản dựng (lô này đã ghi `V1.0.10` ở `TIEN-DO.md`; kiểm lại nếu có deploy giữa lượt) | — |
| 1 | Đăng nhập NHT → vào `/chuyen-gia-tvv/tao-moi` bằng click menu | tiền đề |
| 2 | **Đọc danh sách lựa chọn ô "Loại"** (đếm + đọc nhãn bằng `innerText`), chưa bấm gì | C2 (đo hiện trạng) |
| 3 | Nhập trọn bộ dữ liệu §4.3 + đính tệp §4.4 | tiền đề |
| 4 | **Cài `MutationObserver` bắt toast TRƯỚC khi bấm** (không dedupe, đọc `innerText`) | chuẩn bị C8, C9 |
| 5 | Bấm `Lưu` một lần duy nhất (không bấm lặp) | C1 |
| 6 | Ngay sau đó: đọc chuỗi toast đã bắt + `location.href` + breadcrumb; lưu thân phản hồi của request tạo hồ sơ | C8, C9, C10 |
| 7 | Mở lại hồ sơ vừa tạo: badge trạng thái + nhóm Lĩnh vực + Tổ chức chính | C3, C4, C5 |
| 8 | Đối chứng độc lập bằng API: đọc lại đúng bản ghi (trạng thái, mảng lĩnh vực, tổ chức chính, đơn vị) | C1, C3, C4, C5 |
| 9 | Đăng nhập CB NV cùng đơn vị → màn Thông báo → tìm thông báo khớp tên ứng viên + mốc giờ; đối chứng bằng API danh sách thông báo của chính tài khoản đó | C6 |
| 10 | Đăng nhập `admin` → Nhật ký hệ thống → lọc Người dùng = NHT, Module `CG-TVV`, Loại thao tác `Tạo`, ngày hôm nay | C7 |

**Vế phải cài bộ bắt toast trước thao tác:** **C8** (và C9 dùng ké cùng chuỗi bắt được). Bắt trượt toast thì
**không** bấm lại để chụp lại — dùng thân phản hồi máy chủ làm bằng chứng.
**Vế cần tài khoản thứ hai:** **C6** (Cán bộ Nghiệp vụ cùng đơn vị). **C7** cần `admin` để đọc nhật ký.

### 4.7 Giới hạn hiệu lực và cấm mở rộng

- Verdict chỉ có hiệu lực cho env nội bộ + bản dựng đã ghi. Đối tác đo trên `htpldn-uat.ospgroup.vn` bản
  `HTPLDN · V1.0`; khác môi trường thì ghi rõ giới hạn, không tự quy ra Reopen/Chưa chốt.
- Cấm mở rộng sang: màn Người hỗ trợ pháp lý, màn Tổ chức tư vấn (trừ seed §4.5), luồng thẩm định/phê duyệt,
  các vai trò khác, bộ lọc/tìm kiếm, thử nhiều biến thể `loai_tvv`, dò validate từng trường.
- Hiện tượng lạ ngoài vế Cn: chỉ ghi **candidate một dòng**, không điều tra trong case này.

---

## 5. Câu hỏi BA dự thảo (cho mọi vế DIFF/GAP)

> Phần `web/dev hiện tại` để **TRỐNG** — người đo điền sau khi chạy Giai đoạn B.

**BA-1 (vế C2 — DIFF, chặn Pass):**

```
CẦN BA CONFIRM: đối tác kỳ vọng hồ sơ tạo ở màn Thêm mới Tư vấn viên (/chuyen-gia-tvv/tao-moi) mang loại
"Người hỗ trợ";
SRS quy định trường Loại của hồ sơ này chỉ nhận 'TVV' hoặc 'CG' và "Người hỗ trợ" là entity + màn riêng
(srs-fr-04-chuyen-gia-tvv.md:296 Inputs #0 CHECK IN ('TVV','CG'); :1490 dropdown 2 lựa chọn "Tư vấn viên"/
"Chuyên gia"; :1381-1386 bảng ánh xạ loai_tvv chỉ TVV/CG; :2019 entity TU_VAN_VIEN "NHT lưu ở entity riêng
NGUOI_HO_TRO"; :1799 màn tạo Người hỗ trợ ở /chuyen-gia-tvv/nguoi-ho-tro/tao-moi; :2073 NHT khởi tạo ở
CHO_KICH_HOAT chứ không phải MOI_DANG_KY; :18 lịch sử thay đổi 2026-05-03 gỡ NHT khỏi enum loai_tvv);
web/dev hiện tại <để trống — người đo điền>.
Đề nghị BA chốt 1 trong 2 hướng: (a) expected của đối tác đang nhầm giữa "vai trò người thao tác (NHT)" với
"loại hồ sơ" ⇒ sửa expected về loại "Tư vấn viên"/"Chuyên gia"; hoặc (b) nghiệp vụ thật sự cần thêm giá trị
"Người hỗ trợ" vào trường Loại của hồ sơ TVV ⇒ BA nhập thay đổi vào SRS (Inputs #0 + SCR-IV-02 mục 2.2 +
§3.0 + entity TU_VAN_VIEN) rồi mới verify lại.
```

**BA-2 (vế C9 — GAP, SRS im lặng):**

```
CẦN BA CONFIRM: đối tác kỳ vọng thông báo thành công hiển thị KÈM mã hồ sơ vừa tạo;
SRS im lặng về việc này — §Outputs của FR-IV-03 tách riêng ma_tvv (srs-fr-04-chuyen-gia-tvv.md:348) và
thong_bao "Đăng ký thành công, chờ thẩm định" (:351), không dòng nào yêu cầu ghép mã vào câu thông báo;
SCR-IV-02 cell 7 (:1522) và §Postconditions (:353-357) cũng không nhắc. Đối chứng cho thấy khi SRS muốn kèm mã
thì viết rõ: FR-IV-07 Processing bước 2 (:597) "gửi mail link kích hoạt … kèm mã số TVV";
web/dev hiện tại <để trống — người đo điền>.
Đề nghị BA chốt: câu thông báo sau khi đăng ký có bắt buộc kèm mã hồ sơ không? Nếu có, bổ sung câu chuẩn vào
§Outputs FR-IV-03 để dev và QA cùng một chuẩn.
```

**BA-3 (vế C10 — DIFF, chặn Pass):**

```
CẦN BA CONFIRM: đối tác kỳ vọng sau khi gửi đăng ký thành công, hệ thống chuyển sang "trang theo dõi tiến độ";
SRS quy định ngược lại và ở mức BẮT BUỘC: Phụ lục E §H7 (srs-v3.5.md:6759) "Sau khi thực hiện thành công thao
tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông báo", ngoại lệ
giữ lại trang Chi tiết chỉ hợp lệ khi "có ghi chú riêng tại FR cụ thể" — FR-IV-03 và SCR-IV-02
(srs-fr-04-chuyen-gia-tvv.md:280-363 và :1470-1529) KHÔNG có ghi chú ngoại lệ nào; toàn bộ thư mục srs-v3.5/
cũng không có màn nào tên "trang theo dõi tiến độ" cho luồng này (chuỗi này chỉ xuất hiện 1 lần ở
srs-fr-15-ct-htpldn.md:621, thuộc nghiệp vụ đợt báo cáo CT HTPLDN);
web/dev hiện tại <để trống — người đo điền>.
Đề nghị BA chốt 1 trong 2 hướng: (a) giữ §H7 ⇒ sửa expected của đối tác về "quay lại trang Danh sách tư vấn
viên"; hoặc (b) nghiệp vụ cần một màn theo dõi tiến độ hồ sơ cho Người hỗ trợ ⇒ BA định nghĩa màn đó và ghi
ngoại lệ §H7 ngay tại FR-IV-03 trước khi verify lại.
```

**Ghi nhận ngoài Cn (không phải bug, không phải câu hỏi BA của case này):** ô TKM ghi *"BA xác nhận tên button
sai"*, nhưng SRS v3.5 hiện hành vẫn quy định nhãn nút submit của SCR-IV-02 là **"Lưu"**
(`srs-fr-04-chuyen-gia-tvv.md:1522` + quy ước chung BẮT BUỘC `srs-v3.5.md:6756` §H4), và không có dấu thay đổi
nào (`[STT…]`/`[CR-…]`/`[BA chốt …]`) chạm tới nhãn nút; chuỗi "Gửi đăng ký" không tồn tại trong toàn bộ SRS
v3.5. Theo Flow 04, quyết định BA chỉ có hiệu lực khi đã nhập vào chính bản SRS này ⇒ **web đang đúng SRS hiện
hành ở điểm nhãn nút**; nếu đội muốn đổi tên nút thì đi đường cập nhật đặc tả, không đi đường verify case này.
