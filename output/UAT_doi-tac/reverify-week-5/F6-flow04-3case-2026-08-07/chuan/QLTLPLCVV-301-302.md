# GIAI ĐOẠN A — chuẩn chấm 2 case QLTLPLCVV (dòng 301 · 302)

**Lô:** `F6-flow04-3case-2026-08-07` · **Flow:** 04 (verify bug dev fix, không hồ sơ nội bộ)
**Bảng nguồn:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `bug` — dòng 301 (`QLTLPLCVV_22`), dòng 302 (`QLTLPLCVV_23`)
**Nguồn chuẩn DUY NHẤT (prompt chỉ định):** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Người chốt chuẩn:** CHUẨN-TVCS · **Ngày:** 2026-08-07 · **Chưa mở trình duyệt, chưa đo web** (đúng ràng buộc Giai đoạn A)

> **Đã đọc trọn, không dừng ở grep:** FR-X.1-06 toàn bộ (`srs-fr-12-tv-chuyen-sau.md:822–998`, gồm cả 4 khối Processing gắn
> `[GAP-X.1-02]` và toàn bộ Acceptance Criteria) · SCR-X1-02 toàn bộ (`:1150–1201`) · SCR-X1-01 để đối chiếu cách khai
> control tìm kiếm (`:1102–1148`) · 5 SCR DEPRECATED (`:1203–1230`) · §6 Business Rules toàn bộ (`:1562–1678`) ·
> BR-DATA-08 bản gốc trong file chính (`srs-v3.5.md:5572`) · Phụ lục E §H quy ước UI toàn hệ thống (`srs-v3.5.md:6747–6762`) ·
> entity `TU_LIEU_PHAP_LY_VV` (`:1448–1475`) · CHANGELOG mục 8 giải thích vì sao khối "Tìm kiếm tư liệu" xuất hiện ở v3.5
> (`CHANGELOG-v3-to-v3.5.md:1574–1582`).
>
> **Đã quét đồng nghĩa:** `unaccent` · `không dấu` · `bỏ dấu` · `phân biệt dấu` · `accent-insensitive` · `ILIKE` trên
> **toàn bộ** thư mục `srs-v3.5/` — chỉ 2 lần trúng cho nhóm X.1 (`srs-fr-12:948`, `srs-fr-12:1635`), ngoài ra là
> `srs-v3.5.md:6757` (H5, quy ước dropdown) và 3 chỗ thuộc nhóm khác (DN/quản trị/báo cáo).
>
> **Đã quét dấu thay đổi** `[STT…]` `[CR-…]` `[GAP-…]` `[BA chốt …]` trong toàn file FR-12: **không có dấu nào thêm/bớt
> ô tìm kiếm hoặc bộ lọc cho section tư liệu**. Dấu duy nhất chạm khối tìm kiếm tư liệu là `[GAP-X.1-02]` (`:942`) và
> `[STT63 UAT 2026-06-02]` (`:946`, `:949` — chỉ về phân quyền CG, không về ô tìm kiếm).

---

## Trả lời 5 câu hỏi bắt buộc trước khi khóa vế

| # | Câu hỏi | Trả lời (dẫn dòng thực đọc) |
|---|---|---|
| a | SRS đặc tả màn chi tiết TVCS có section tư liệu không? Quy định thành phần gì? | **CÓ.** `SCR-X1-02` (`srs-fr-12-tv-chuyen-sau.md:1150`) có "Accordion: Tư liệu PL liên kết (UC152)" là thành phần #6 (`:1171`). SRS quy định cho section này **đúng 2 thứ**: (1) một **bảng** 9 cột "Tên / Loại / Lĩnh vực / Số file / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động"; (2) **nút `[+ Thêm tư liệu]`** inline. **KHÔNG khai ô nhập từ khóa, KHÔNG khai bộ lọc nào.** §Quy tắc tương tác cũng chỉ nói "CRUD tư liệu inline. Nút [Công khai lên Cổng PLQG] khi NHAP + >= 1 file" (`:1198`). |
| b | SRS có yêu cầu tìm kiếm keyword/bộ lọc **ngay trong** section đó không? Hay chỉ ở màn danh sách tư liệu độc lập? | **Chức năng tìm kiếm tư liệu CÓ được đặc tả** — `FR-X.1-06 §Processing — Tìm kiếm tư liệu` (`:942–951`): nhận keyword (tên tư liệu, mô tả) + lĩnh vực + loại + trạng thái, AND logic, phân trang. **Không còn màn độc lập nào:** `SCR-X1-07 Tư liệu Pháp lý Vụ việc` đã **DEPRECATED v2.1** và "Gộp vào: Tab 'Tư liệu PL liên kết' trong SCR-X1-02" (`:1227–1229`); §Màn hình của chính FR-X.1-06 ghi y hệt (`:828`); `SCR-X1-02 §FR sử dụng` có liệt kê FR-X.1-06 (`:1153`). Đã grep toàn bộ 15 file FR khác trong `srs-v3.5/`: **không file nào** có màn/section tư liệu pháp lý khác. ⇒ Chức năng bắt buộc phải nằm ở section này, **nhưng SRS im lặng về control UI để dùng nó**. |
| c | SRS có quy định tìm kiếm tiếng Việt **không dấu** áp cho chức năng này không? | **CÓ, một chỗ duy nhất:** `:948` — "Full-text search trên ten_tu_lieu + mo_ta **(hỗ trợ tiếng Việt unaccent)**". ⚠️ Nhưng 3 chỗ khác **thu hẹp BR-DATA-08 ra ngoài FR-X.1-06**: bảng tổng quan BR (`:1579` → chỉ FR-X.1-02), bản trích BR-DATA-08 (`:1635` → "cho nội dung tư vấn", cột Áp dụng FR = FR-X.1-02), và **bản gốc BR-DATA-08 trong file chính** (`srs-v3.5.md:5572` → phạm vi FR-II-02/FR-X.1-02/FR-X.2-04, **không hề nhắc chữ unaccent**, cột Ngoại lệ ghi "Các entity khác: search by tìm kiếm theo từ khóa"). Chuẩn chấm lấy `:948` (câu đặc tả **trực tiếp cho đúng 2 trường `ten_tu_lieu` + `mo_ta` của chính FR này**), độ lệch của 3 bảng tham chiếu ghi làm ghi chú — xem §5 câu hỏi BA phụ. |
| d | Dấu thay đổi trong vùng liên quan | `[GAP-X.1-02]` gắn trên 4 khối Processing của FR-X.1-06, trong đó có "Tìm kiếm tư liệu" (`:909`, `:920`, `:931`, `:942`). CHANGELOG mục 8 (`CHANGELOG-v3-to-v3.5.md:1574–1582`) nói rõ 4 khối này là **"Sửa lỗi nội bộ SRS" bổ sung ở v3.5** vì v3 thiếu — và mục "Vị trí đã sửa" **chỉ liệt kê §2 phần Xử lý, KHÔNG có dòng nào sửa §3 Màn hình**. Đây chính là nguồn gốc của khoảng trống ở câu (a)/(b). Ngoài ra: `[STT63 UAT 2026-06-02]` (`:833`, `:839`, `:866–867`, `:946`, `:949`, `:992–993`) và `[GAP-X.1-03]` (`:1448` entity) — đều **không** đụng tới ô tìm kiếm. |
| e | Ràng buộc vai trò | `:833` Tác nhân: **Cán bộ Nghiệp vụ (TW/BN/ĐP) — CRUD đầy đủ**; Chuyên gia — chỉ ĐỌC (BR-AUTH-14). `:946` bước 1 của chính khối tìm kiếm: CB NV theo đơn vị (BR-AUTH-08). `:39` ghi rõ **NHT KHÔNG tham gia UC152**. Bằng chứng đối tác dùng `CB_NV_TW` ⇒ **đúng vai trò tác nhân chính** ⇒ ghi làm **tiền đề**, KHÔNG tách thành vế/bug mới, KHÔNG mở phép đo cho CG/NHT. |

---

## 1. Case dòng 301 — `QLTLPLCVV_22` "Tìm kiếm tư liệu hỗ trợ tiếng Việt có dấu"

### 1.1 Expected đối tác — tách vế

Nguyên văn KQ mong đợi: *"Có kết quả, hệ thống hiển thị danh sách kết quả."*
Nguyên văn bước 4: *"NSD nhập từ khóa và/hoặc chọn bộ lọc"* — sau bước 3 *"Mở Nhóm 3 — Tư liệu pháp lý liên kết"*.

| Vế | Nội dung expected (chỉ những gì đối tác nhắc) |
|---|---|
| **C1** | Trong section "Tư liệu pháp lý liên kết" của màn **chi tiết TVCS**, NSD **có phương tiện để nhập từ khóa và/hoặc chọn bộ lọc** (điểm tranh chấp chính — TKM phản hồi *"Màn hình không có chức năng"*) |
| **C2** | Nhập **từ khóa tiếng Việt CÓ DẤU** khớp tư liệu đang tồn tại ⇒ hệ thống **hiển thị danh sách kết quả** (không rỗng, chỉ chứa bản ghi khớp) |

### 1.2 BUG SCOPE LOCK — dòng 301

```
C1 · Section "Tư liệu pháp lý liên kết" trên màn chi tiết TVCS có ô nhập từ khóa và/hoặc bộ lọc để NSD dùng ·
     srs-fr-12-tv-chuyen-sau.md:942-951 (SRS quy định CHỨC NĂNG tìm kiếm tư liệu) + :828/:1153/:1227-1229
     (màn duy nhất chứa FR-X.1-06 = accordion này) NHƯNG :1171 + :1198 IM LẶNG về control tìm kiếm/bộ lọc
     và :986-996 không có AC tìm kiếm · GAP · route BA · đường đo: [UI] cbnv_tw_05 → Tư vấn → Tư vấn chuyên sâu
     → chi tiết TVCS tiền đề → mở accordion tư liệu → đếm control nhập/chọn NẰM TRONG container section
     (trả count + placeholder/label, cấm dump DOM); [đối chứng] list_network_requests lúc mở section, lấy đúng
     request danh sách tư liệu của TVCS đó (KHÔNG đoán endpoint), đọc query string thực tế xem có nhận
     keyword/loại/lĩnh vực/trạng thái, đối chiếu schema tại /api/docs-json

C2 · Nhập từ khóa tiếng Việt CÓ DẤU khớp tư liệu đang tồn tại → hiển thị danh sách kết quả khớp ·
     srs-fr-12-tv-chuyen-sau.md:947 (nhận keyword tên tư liệu + mô tả) + :950 (AND logic) + :951 (phân trang,
     trả kết quả) + :946 (phạm vi đơn vị CB NV) · MATCH · route TEST · đường đo: [UI] gõ đúng cụm CÓ DẤU
     "Nghị định" vào ô tìm kiếm của section → đếm số dòng .ant-table-tbody tr.ant-table-row trước/sau + đọc
     innerText cột Tên của các dòng còn lại; [đối chứng] get_network_request của CHÍNH request tìm kiếm vừa
     phát sinh → so total/độ dài mảng data với số dòng UI
```

### 1.3 Route dòng 301

| Vế | Relation | Route | Được chấm Pass? |
|---|---|---|---|
| C1 | **GAP** | **BA** | ❌ Cấm Pass (luật khóa 5). Kể cả khi web đã có ô tìm kiếm chạy đúng → ghi `WEB HIỆN TẠI: đúng kỳ vọng đối tác`, câu hỏi BA nhằm **bổ sung vào đặc tả**, không phải chặn bàn giao |
| C2 | **MATCH** | **TEST** | ✅ Chấm bằng đo — **nhưng chỉ đo được khi C1 có control**; không có control ⇒ C2 = **Chưa chốt**, CẤM thay thao tác UI bằng curl API (Flow 04 §Giai đoạn B bước 5) |

**Verdict logic dự kiến dòng 301:** còn ≥1 vế `GAP` ⇒ **Cần BA** (nếu C2 đo được và đạt) hoặc **Reopen + cần BA** (nếu C2 đo được và sai).

---

## 2. Case dòng 302 — `QLTLPLCVV_23` "Tìm kiếm hỗ trợ tiếng Việt không dấu."

### 2.1 Expected đối tác — tách vế

KQ mong đợi + bước 1–4 **giống hệt dòng 301**; điểm phân biệt duy nhất nằm ở Mô tả: từ khóa **KHÔNG DẤU**.

> 🔴 Hai dòng dùng **chung một ảnh** (md5 `3d926926a8bbdfd3352f9328d55c1c39`) ⇒ ảnh chỉ chứng minh *trạng thái màn*,
> **không** phân biệt vế "có dấu" với "không dấu" ⇒ theo Flow 04 §Bước 0 phải **đo riêng từng vế**, cấm suy case này
> ra case kia. C1 quan sát trên cùng một màn nhưng **phải ghi kết quả riêng cho từng dòng**; C2 là **hai phép gõ khác nhau**.

| Vế | Nội dung expected |
|---|---|
| **C1** | Như C1 dòng 301 — section tư liệu của màn chi tiết TVCS có phương tiện nhập từ khóa và/hoặc bộ lọc |
| **C2** | Nhập **từ khóa tiếng Việt KHÔNG DẤU (bỏ dấu)** của tư liệu có tên/mô tả viết **có dấu** ⇒ vẫn **hiển thị danh sách kết quả** khớp |

### 2.2 BUG SCOPE LOCK — dòng 302

```
C1 · Section "Tư liệu pháp lý liên kết" trên màn chi tiết TVCS có ô nhập từ khóa và/hoặc bộ lọc để NSD dùng ·
     srs-fr-12-tv-chuyen-sau.md:942-951 + :828/:1153/:1227-1229 (chức năng có, màn duy nhất là accordion này)
     NHƯNG :1171 + :1198 IM LẶNG về control tìm kiếm/bộ lọc, :986-996 không có AC tìm kiếm · GAP · route BA ·
     đường đo: dùng CHUNG quan sát với C1 dòng 301 (cùng màn, cùng bản ghi tiền đề) nhưng GHI KẾT QUẢ RIÊNG
     cho dòng 302; không lặp lại thao tác chỉ để "chắc"

C2 · Nhập từ khóa tiếng Việt KHÔNG DẤU của tư liệu có tên/mô tả viết CÓ DẤU → vẫn hiển thị danh sách kết quả ·
     srs-fr-12-tv-chuyen-sau.md:948 nguyên văn "Full-text search trên ten_tu_lieu + mo_ta (hỗ trợ tiếng Việt
     unaccent)" · MATCH · route TEST · đường đo: [UI] cùng ô tìm kiếm, thay chuỗi thành "Nghi dinh" (bỏ dấu của
     đúng cụm đã dùng ở C2 dòng 301) → đếm số dòng + đọc innerText cột Tên; [đối chứng] response của CHÍNH
     request tìm kiếm đó → so tập ID trả về với tập ID thu được ở C2 dòng 301 (phải trùng, không được rỗng)
```

### 2.3 Route dòng 302

| Vế | Relation | Route | Được chấm Pass? |
|---|---|---|---|
| C1 | **GAP** | **BA** | ❌ Cấm Pass — như dòng 301 |
| C2 | **MATCH** | **TEST** | ✅ Chấm bằng đo. Chuẩn chấm = `:948`. Độ lệch phạm vi BR-DATA-08 (`:1579`, `:1635`, `srs-v3.5.md:5572`) **không** đổi relation — chỉ ghi kèm câu hỏi BA phụ ở §5 |

**Verdict logic dự kiến dòng 302:** còn ≥1 vế `GAP` ⇒ **Cần BA**, hoặc **Reopen + cần BA** nếu C2 đo được mà không dấu trả rỗng trong khi có dấu ra kết quả.

---

## 3. Trích dẫn SRS nguyên văn (tự mở file trong lượt này, dán đủ để kiểm lại)

### 3.1 `srs-fr-12-tv-chuyen-sau.md` — FR-X.1-06 (UC152)

```
:822  ### FR-X.1-06: Quản lý tư liệu pháp lý của vụ việc (UC152)
:828  **Màn hình:** ~~SCR-X1-07~~ (DEPRECATED v2.1 — gộp thành tab "Tư liệu PL" trong SCR-X1-02 / MH-12.2)
:833  **Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP) — CRUD đầy đủ. **Chuyên gia (CG)** — `[STT63 UAT 2026-06-02]`
      chỉ ĐỌC (R-only), scope đích danh theo TVCS được phân công (BR-AUTH-14).
:839  - **Phân quyền theo vai trò:** CB NV → phân quyền theo đơn vị (BR-AUTH-08, CRUD). **CG → BR-AUTH-14**
      `[STT63 UAT 2026-06-02]`: chỉ đọc/tải tư liệu của TVCS có `chuyen_gia_id = CG đang đăng nhập` và trạng
      thái ≥ PHAN_CONG; chặn mọi thao tác CUD + công khai
```

Inputs (để biết trường nào tìm được / lọc được):

```
:846  | 2 | ten_tu_lieu | text | Y | Tối đa 500 ký tự | — | người dùng nhập |
:847  | 3 | loai_tu_lieu | text | Y | VAN_BAN_PL / TAI_LIEU / NGHIEN_CUU / TIEN_LE / KHAC | — | người dùng chọn |
:848  | 4 | linh_vuc_id | identifier | N | FK -> DANH_MUC | — | người dùng chọn |
:849  | 5 | mo_ta | text (long) | N | — | — | người dùng nhập |
:850  | 6 | trang_thai | text | Y | NHAP / CONG_KHAI | NHAP | hệ thống |
```

**Khối quyết định — Processing tìm kiếm (nguyên văn cả bảng):**

```
:942  **Processing — Tìm kiếm tư liệu** `[GAP-X.1-02]`
:943
:944  | Bước | Mô tả xử lý | BR áp dụng |
:945  |------|-------------|-----------|
:946  | 1 | Kiểm tra quyền: CB NV theo đơn vị (BR-AUTH-08); **CG đích danh TVCS được phân công (BR-AUTH-14)**
        `[STT63 UAT 2026-06-02]` | BR-AUTH-01, BR-AUTH-08, BR-AUTH-14 |
:947  | 2 | Nhận tiêu chí: keyword (tên tư liệu, mô tả), lĩnh vực, loại tư liệu, trạng thái | — |
:948  | 3 | Full-text search trên ten_tu_lieu + mo_ta (hỗ trợ tiếng Việt unaccent) | BR-DATA-08 |
:949  | 4 | Lọc bản ghi chưa xóa: CB NV theo đơn vị (BR-AUTH-08); **CG chỉ tư liệu của TVCS có
        `chuyen_gia_id=CG` và trạng thái ≥ PHAN_CONG (BR-AUTH-14)** `[STT63 UAT 2026-06-02]` |
        BR-DATA-01, BR-AUTH-14 |
:950  | 5 | AND logic cho tất cả điều kiện | — |
:951  | 6 | Phân trang (mặc định 20/trang) và trả về kết quả | BR-DATA-07 |
```

**Acceptance Criteria của FR-X.1-06 — đọc trọn 11 dòng `:986–996`, KHÔNG có dòng nào về tìm kiếm:**

```
:986  **Acceptance Criteria:**
:988  - **Given** CB NV truy cập "Tư liệu pháp lý" **When** hệ thống hiển thị **Then** danh sách tư liệu thuộc
        đơn vị, phân trang
:989  - **Given** CB NV xem chi tiết **When** chọn tư liệu **Then** hiển thị thông tin + danh sách file
:990  - **Given** CB NV thêm mới tư liệu **When** nhập thông tin + nhấn Lưu **Then** validate + lưu
:991  - **Given** CB NV tải lên file **When** chọn file hợp lệ **Then** upload + quét virus + lưu
:992  - **[STT63 UAT 2026-06-02] Given** Chuyên gia được phân công mở section "Tư liệu pháp lý" của TVCS mình
        phụ trách (trạng thái ≥ PHAN_CONG) **When** xem/tải tư liệu **Then** hiển thị chế độ chỉ đọc (xem +
        tải/preview), ẩn nút Thêm/Sửa/Xóa/Công khai (BR-AUTH-14); ghi AUDIT_LOG hành vi đọc/tải (BR-DATA-05)
:993  - **[STT63 UAT 2026-06-02] Given** Chuyên gia truy cập tư liệu của TVCS KHÔNG phải mình phụ trách **When**
        mở section **Then** từ chối (không hiển thị / 403 xử lý ở tầng quyền), không phải lỗi hệ thống
:994  - **Given** CB NV xem file trực tuyến **When** chọn file **Then** hiển thị preview
:995  - **Given** CB NV công khai tư liệu **When** nhấn "Công khai" **Then** đặt cờ công khai (`cong_khai = 1`)
        trên CSDL CMS; Cổng PLQG tự kéo qua API outbound Nhóm XII
:996  - **Given** CB NV hủy công khai **When** xác nhận **Then** đặt cờ `cong_khai = 0` trên CSDL CMS; Cổng PLQG
        tự ẩn qua kéo định kỳ
```

### 3.2 `srs-fr-12-tv-chuyen-sau.md` — SCR-X1-02 (màn duy nhất chứa FR-X.1-06)

```
:1150 ### SCR-X1-02: Thêm mới / Chi tiết Tư vấn pháp luật chuyên sâu
:1152 **Loại màn hình:** Form nhập liệu / Chi tiết (tabs: Thông tin, Tư liệu PL, Đánh giá CL + action buttons
      phân công/phê duyệt)
:1153 **FR sử dụng:** FR-X.1-01, FR-X.1-03, FR-X.1-04, FR-X.1-05, FR-X.1-06
:1156 > **v2.1:** Gộp MH-12.4 (Phân công CG), MH-12.5 (Xác nhận CG), MH-12.6 (Phê duyệt TVCS) thành action
      buttons. MH-12.7 (Tư liệu PL) thành tab trong màn hình này.
:1160 Breadcrumb > Tiêu đề + nhãn trạng thái > Thanh tiến trình SM-TVCS (stepper) > Accordion sections (Thông
      tin cơ bản / Nội dung TV / Tư liệu PL / Đánh giá CL / Nhật ký) > Thanh hành động cố định
```

**Dòng quyết định — thành phần #6, toàn bộ nội dung SRS gán cho section tư liệu:**

```
:1171 | 6 | content | Accordion: Tư liệu PL liên kết (UC152) | table | Bảng tư liệu: Tên / Loại / Lĩnh vực /
      Số file / Trạng thái / Công khai lúc / Người tạo / Ngày tạo / Hành động. Nút [+ Thêm tư liệu] (inline
      trong tab này) | click -> modal/inline | luôn hiển thị |
```

```
:1198 - Tư liệu PL (gộp từ MH-12.7): tab "Tư liệu PL" trong accordion. CRUD tư liệu inline. Nút [Công khai lên
      Cổng PLQG] khi NHAP + >= 1 file
:1227 ### ~~SCR-X1-07: Tư liệu Pháp lý Vụ việc~~ (DEPRECATED v2.1)
:1229 > **Gộp vào:** Tab "Tư liệu PL liên kết" trong SCR-X1-02 (MH-12.2).
```

**Đối chiếu — cùng file, SRS KHAI RẤT RÕ control tìm kiếm khi muốn có (SCR-X1-01):**

```
:1119 | 4 | filter-bar | Ô tìm kiếm | search-box | Full-text (tìm kiếm toàn văn trên tieu_de + noi_dung_tu_van
      + ma_noi_dung + ten DN) | change -> filter | luôn hiển thị |
:1122 | 7 | filter-bar | Dropdown Lĩnh vực | select | Từ DANH_MUC | change -> filter | luôn hiển thị |
:1123 | 8 | filter-bar | Dropdown Trạng thái | select | TIEP_NHAN / PHAN_CONG / DANG_TU_VAN / HOAN_THANH /
      CHO_PHE_DUYET / DA_DUYET / HUY | change -> filter | luôn hiển thị |
```

> ⇒ Cùng một file dùng loại `search-box` / `select` cho filter-bar của SCR-X1-01, nhưng section tư liệu của
> SCR-X1-02 chỉ có loại `table`. **Đây là căn cứ để kết luận `IM LẶNG` chứ không phải "SRS mặc nhiên có".**

### 3.3 BR-DATA-08 — 3 bản, lệch nhau (căn cứ cho ghi chú vế C2 dòng 302)

```
srs-fr-12-tv-chuyen-sau.md:1564  > **Source of truth:** `srs-v3.md` Phụ lục B.
srs-fr-12-tv-chuyen-sau.md:1565  > Đây là bản trích BR liên quan đến Nhóm X.1...

srs-fr-12-tv-chuyen-sau.md:1579 | BR-DATA-08 | Tìm kiếm toàn văn | FR-X.1-02 |
srs-fr-12-tv-chuyen-sau.md:1635 | BR-DATA-08 | Tìm kiếm toàn văn (full-text search) cho nội dung tư vấn.
      Hỗ trợ tiếng Việt unaccent | Architecture AD-09 | FR-X.1-02 | — | Test FTS với nội dung tiếng Việt |

srs-v3.5.md:5572 | BR-DATA-08 | **Full-text search:** Hỏi đáp (noi_dung) và Kho câu hỏi
      (cau_hoi/cau_tra_loi/tu_khoa) hỗ trợ tìm kiếm toàn văn | FR-II-02, FR-X.1-02, FR-X.2-04 |
      FR-II-02, FR-X.1-02, FR-X.2-04 | Các entity khác: search by tìm kiếm theo từ khóa |
      Verify chỉ mục tìm kiếm toàn văn |
```

> Bản gốc trong file chính **không có chữ "unaccent"** và **không liệt kê FR-X.1-06**; bản trích ở FR-12 thì
> có chữ "unaccent" nhưng cột Áp dụng FR vẫn chỉ ghi FR-X.1-02. Câu duy nhất buộc unaccent cho **đúng
> `ten_tu_lieu` + `mo_ta`** là `srs-fr-12:948` ⇒ dùng làm chuẩn chấm C2 dòng 302, độ lệch đưa vào câu hỏi BA phụ.

### 3.4 Quy ước UI toàn hệ thống (Phụ lục E §H) — chỉ liên quan phần bộ lọc dropdown

```
srs-v3.5.md:6749 Áp dụng cho **mọi màn hình** trong hệ thống (Dashboard, Hỏi đáp, ... TVCS, TV nhanh, HĐ TV,
      CT HTPLDN, API).
srs-v3.5.md:6757 | **H5** | Dropdown có tìm kiếm tương đối | Mọi dropdown có ≥10 lựa chọn phải hỗ trợ tìm kiếm
      bằng cách gõ (autocomplete) với so khớp **tương đối** (chứa chuỗi, không phân biệt hoa thường, hỗ trợ bỏ
      dấu tiếng Việt). Dropdown <10 lựa chọn cho phép native select. | BẮT BUỘC |
srs-v3.5.md:6762 **Tham chiếu chéo:** Các FR/SCR có quy ước UI riêng phải cross-ref về Phụ lục E §H thay vì
      viết lại; nếu lệch quy ước H1–H8 phải ghi rõ lý do nghiệp vụ tại FR đó.
```

> H5 **không** tạo ra ô tìm kiếm cho section; nó chỉ ràng buộc **hành vi gõ trong dropdown ≥10 lựa chọn**
> (vd dropdown Lĩnh vực nếu có). Ghi để người đo không nhầm H5 thành căn cứ cho C1.

### 3.5 CHANGELOG — vì sao khối "Tìm kiếm tư liệu" có mặt mà màn hình không có control

```
CHANGELOG-v3-to-v3.5.md:1574 #### 8. Bổ sung 6 khối Xử lý còn thiếu cho FR-X.1-04 ... và FR-X.1-06 (Tư liệu
      pháp luật vụ việc)
CHANGELOG-v3-to-v3.5.md:1577 ...với tư liệu pháp luật thì thiếu "Chỉnh sửa / Xóa mềm / Xóa file đính kèm /
      Tìm kiếm" mặc dù Tiêu chí chấp nhận có đề cập...
CHANGELOG-v3-to-v3.5.md:1579 **Vị trí đã sửa trong srs-v3.5/srs-fr-12-tv-chuyen-sau.md:**
CHANGELOG-v3-to-v3.5.md:1581 - §2 FR-X.1-06 phần Xử lý — Chỉnh sửa tư liệu (line 865), Xóa mềm tư liệu
      (line 876), Xóa file đính kèm (line 887), Tìm kiếm tư liệu (line 898)
```

> Mục "Vị trí đã sửa" **chỉ có §2 phần Xử lý**, **không có dòng §3 Màn hình** ⇒ khối tìm kiếm được thêm ở tầng
> nghiệp vụ mà **không kèm thành phần màn hình**. Đây là bằng chứng tài liệu cho relation `GAP` của C1.

### 3.6 Entity (để thiết kế tiền đề đúng trường)

```
:1458 | 3 | ten_tu_lieu | text | Y | Max 500 ký tự | — | Tên tư liệu |
:1461 | 6 | mo_ta | text (long) | N | | — | Mô tả |
:1462 | 7 | trang_thai | text | Y | CHECK IN ('NHAP','CONG_KHAI') | 'NHAP' | Trạng thái công khai |
:1463 | 8 | don_vi_id | identifier | Y | FK → DON_VI(id) | — | Đơn vị sở hữu |
```

---

## 4. Tiền đề cần chuẩn bị cho Giai đoạn B

### 4.1 Môi trường · vai trò · bản dựng

| Hạng mục | Giá trị chốt |
|---|---|
| Env đo | `https://18.143.165.120.nip.io` (env nội bộ) — bản dựng đã vân tay đầu lô: **V1.0.10**, bó mã `assets/index-B2W2Krcs.js` |
| Tài khoản | **`cbnv_tw_05` / `Test@1234`** (vai trò `CB_NV_TW`) — khớp vai trò trên ảnh đối tác (`Cán bộ NV Trung ương`) và khớp Tác nhân SRS `:833`. Fallback trong CÙNG vai trò + cấp: `cbnv_tw_04` → `cbnv_tw_03` (chỉ khi lock; phải ghi account thực dùng) |
| Vai trò KHÔNG đo | CG (`:839` R-only) và NHT (`:39` không tham gia UC152) — **tiền đề, không mở phép đo** |
| Giới hạn hiệu lực | Đối tác đo trên `htpldn-uat.ospgroup.vn` bản `HTPLDN · V1.0`; verdict lô này chỉ có hiệu lực cho bản dựng nội bộ ghi ở trên |

### 4.2 Dữ liệu tiền đề — ưu tiên DÙNG LẠI dữ liệu QA sẵn có

**Cần đúng 1 bản ghi TVCS** thuộc đơn vị TW của `cbnv_tw_05`, có **≥3 tư liệu** trong section, thoả:

| Nhãn | `ten_tu_lieu` gợi ý | Vai trò trong phép đo |
|---|---|---|
| TL-A | `Nghị định 55/2019 hỗ trợ pháp lý cho doanh nghiệp nhỏ và vừa` | Bản ghi **phải khớp** với cả "Nghị định" (C2/301) lẫn "Nghi dinh" (C2/302) |
| TL-B | `Thông tư 09 hướng dẫn nghiệp vụ` | Bản ghi **phải bị loại** — chứng minh tìm kiếm thật sự thu hẹp, không trả nguyên bảng |
| TL-C | `Biên bản làm việc 2026` | Bản ghi **phải bị loại** — như trên |

**Ràng buộc chọn từ khóa (bắt buộc, tránh false PASS/FAIL):**

- Dùng **cụm 2 từ** `Nghị định` / `Nghi dinh`. **CẤM** dùng cụm 1 từ `nghị` / `nghi` — bỏ dấu của `nghị` là `nghi`,
  trùng tiền tố của `nghiệp` (`nghiep`) ⇒ tìm kiếm chuỗi con sẽ vô tình khớp TL-B và làm mất khả năng phân biệt.
- Bảo đảm **TL-B và TL-C không chứa** chuỗi `nghi dinh` sau khi bỏ dấu.
- Nếu dữ liệu QA sẵn có đã thoả (đủ 3 bản ghi + có bản ghi tên chứa dấu tiếng Việt phân biệt được) ⇒ **dùng lại,
  không tạo mới** (Flow 04 §Giai đoạn B bước 3).

**Nếu thiếu — cách bổ sung (chỉ tạo phần còn thiếu):**

1. Dùng chính nút **`[+ Thêm tư liệu]`** trong section (đường chính thức của SRS `:1171`), **cấm đoán endpoint, cấm ghi thẳng DB**.
2. Chọn TVCS ở trạng thái **TIEP_NHAN** hoặc **DANG_TU_VAN** để tránh chế độ read-only của màn (`:1179`).
3. `trang_thai` để mặc định **NHAP** (`:850`) — không cần công khai, vì công khai đòi ≥1 file (`:983` ERR-TLPL-05) và
   không thuộc vế nào đang chấm.
4. Nếu form bắt buộc file: tái dùng **fixture PDF thật** đã có trong `seed-files/`; **cấm** đổi đuôi file giả.
5. **Khai vào báo cáo:** đổi bản ghi TVCS nào (mã + id) · thêm mấy tư liệu · tên gì · trên env nào.

### 4.3 Bẫy phải tránh khi đo (chốt trước, không sửa sau khi mở màn)

- ⚠️ **CẤM dùng ô tìm kiếm ở màn DANH SÁCH TVCS** (`:1119`, thuộc FR-X.1-02) để thay cho ô tìm kiếm trong section
  tư liệu — khác vế, khác FR, sẽ Pass oan.
- ⚠️ **CẤM thay thao tác UI bằng curl/API khi section không có ô tìm kiếm.** API chỉ là **đối chứng** (Flow 04 bước 5/8).
  Không có control ⇒ C2 = **Chưa chốt**, C1 = dữ kiện trả lời câu hỏi BA.
- ⚠️ **CẤM kết luận "0 kết quả = lỗi"** nếu bản ghi tiền đề nằm ngoài đơn vị của tài khoản đo (`:946` BR-AUTH-08) —
  kiểm đơn vị trước khi chốt.
- ⚠️ **CẤM đổi relation `GAP` → `MATCH`** vì web đã có ô tìm kiếm chạy tốt (luật khóa 5). Chỉ đổi được khi dẫn ra
  **dòng SRS mới đọc được**.
- ⚠️ Tải lại trang trước lô đo (tab MCP mở lâu vẫn chạy JS bản cũ) và ghi lại bản dựng thực tế.
- ℹ️ **Ghi nhận, KHÔNG thành vế chấm, KHÔNG mở phép đo:** bảng trong ảnh đối tác có 7 cột (Tên tư liệu · Loại ·
  Lĩnh vực · File · Trạng thái · Công khai lúc · Hành động) trong khi `:1171` khai 9 cột (thiếu **Người tạo**,
  **Ngày tạo**); tiêu đề section trên web là *"Tư liệu pháp luật"* còn SRS gọi *"Tư liệu PL liên kết"*. Cả hai nằm
  ngoài expected của 2 dòng ⇒ chỉ là **candidate một dòng**, không điều tra trong case này.

---

## 5. Câu hỏi BA dự thảo (vế `GAP` — bắt buộc; phần "web/dev hiện tại" người đo điền)

### 5.1 Câu hỏi chính — áp cho **cả dòng 301 và 302** (vế C1)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **section "Tư liệu pháp lý liên kết" trong màn chi tiết Tư vấn chuyên sâu có ô
> nhập từ khóa và/hoặc bộ lọc để người dùng tìm tư liệu ngay tại đó**; SRS quy định **chức năng tìm kiếm tư liệu là
> yêu cầu bắt buộc của FR-X.1-06 (nhận keyword theo tên tư liệu + mô tả, lĩnh vực, loại tư liệu, trạng thái, AND
> logic, phân trang — `srs-fr-12-tv-chuyen-sau.md:942–951`) và màn duy nhất chứa FR-X.1-06 là chính accordion này
> (`:828`, `:1153`, `:1227–1229` — SCR-X1-07 đã bị gộp vào), NHƯNG phần Thành phần màn hình của SCR-X1-02 chỉ khai
> cho section này một bảng dữ liệu và nút [+ Thêm tư liệu], không khai ô tìm kiếm hay bộ lọc nào (`:1171`, `:1198`),
> và FR-X.1-06 không có tiêu chí chấp nhận nào cho tìm kiếm (`:986–996`)**; web/dev hiện tại **<người đo điền>**.
>
> **Đề nghị BA chốt:** section tư liệu trong màn chi tiết TVCS **có phải hiển thị phương tiện tìm kiếm/lọc cho người
> dùng hay không**. Nếu **có** → xin bổ sung thành phần đó vào SCR-X1-02 §Thành phần màn hình (nêu rõ tìm theo trường
> nào, có mấy bộ lọc) và bổ sung tiêu chí chấp nhận tương ứng cho FR-X.1-06. Nếu **không** (khối Processing tìm kiếm
> chỉ phục vụ tầng API/nội bộ) → xin ghi rõ điều đó tại FR-X.1-06 để dev và QA không hiểu lệch.
>
> *(Mục đích: bổ sung điều này vào đặc tả — không phải chặn bàn giao.)*

### 5.2 Câu hỏi phụ — chỉ áp cho **dòng 302** (độ lệch phạm vi BR-DATA-08)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **tìm kiếm tư liệu bằng từ khóa tiếng Việt không dấu vẫn ra kết quả của bản ghi
> có tên/mô tả viết có dấu**; SRS quy định **hai chỗ lệch nhau: bước xử lý của chính FR-X.1-06 ghi "Full-text search
> trên ten_tu_lieu + mo_ta (hỗ trợ tiếng Việt unaccent)" (`srs-fr-12-tv-chuyen-sau.md:948`), trong khi quy tắc
> BR-DATA-08 ở bản gốc file chính không nhắc unaccent và chỉ áp cho FR-II-02 / FR-X.1-02 / FR-X.2-04, phần Ngoại lệ
> ghi "Các entity khác: search by tìm kiếm theo từ khóa" (`srs-v3.5.md:5572`); hai bảng tham chiếu trong FR-12 cũng
> chỉ gán BR-DATA-08 cho FR-X.1-02 (`:1579`, `:1635`)**; web/dev hiện tại **<người đo điền>**.
>
> **Đề nghị BA chốt:** tìm kiếm tư liệu pháp lý (FR-X.1-06) **có bắt buộc hỗ trợ tiếng Việt không dấu hay không**, và
> đồng bộ lại phạm vi BR-DATA-08 giữa file chính và bản trích ở FR-12.
>
> *(Chuẩn chấm của vòng verify này vẫn lấy `:948` — câu đặc tả trực tiếp cho đúng hai trường `ten_tu_lieu` + `mo_ta`
> của chính FR-X.1-06. Câu hỏi này chỉ nhằm dọn mâu thuẫn tài liệu, không đổi relation đã khóa.)*

---

## 6. Cổng chốt Giai đoạn A

| # | Câu hỏi cổng | Trả lời |
|---|---|---|
| 1 | Mỗi vế neo vào dòng SRS nào? | C1 → `:942–951` + `:828`/`:1153`/`:1227–1229` (chức năng) đối chiếu `:1171`/`:1198`/`:986–996` (im lặng UI). C2/301 → `:947`, `:950`, `:951`, `:946`. C2/302 → `:948`. |
| 2 | Mọi thao tác dự kiến có ánh xạ về vế Cn không? | Có — 3 phép đo (quan sát control · gõ có dấu · gõ không dấu) + 1 đối chứng network dùng chung. Không thao tác nào ngoài vế. |
| 3 | Vế `GAP` đã bị chặn Pass và có câu hỏi BA chưa? | Rồi — C1 (cả 2 dòng) route BA, câu hỏi §5.1. Vế `MATCH` C2/302 kèm câu hỏi phụ §5.2 nhưng **không** đổi relation. |
| 4 | Đã đọc đầy đủ expected + phản hồi của case chưa? | Rồi — Mô tả, Điều kiện, 4 bước, KQ mong đợi, Trạng thái `Fail`, `TKM phản hồi lần 1` = *"Màn hình không có chức năng"*, `Trạng thái dev fix` = `Fixed`, `DEV phản hồi lần 1` trống. |
| 5 | Điều kiện đo có khớp tiền đề case không? | Khớp vai trò (`CB_NV_TW`) và màn (chi tiết TVCS → section tư liệu). Khác: env nội bộ V1.0.10 vs env đối tác V1.0, và bản ghi TVCS là dữ liệu QA (ảnh đối tác không cho biết nội dung tư liệu của họ) ⇒ đã ghi giới hạn hiệu lực + thiết kế tiền đề riêng ở §4.2. |
