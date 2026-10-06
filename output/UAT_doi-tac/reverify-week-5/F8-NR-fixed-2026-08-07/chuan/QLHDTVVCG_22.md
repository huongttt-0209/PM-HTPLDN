# QLHDTVVCG_22 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 328 · **Mô tả (G):** Liên kết vụ việc
**Điều kiện (H):** 1. Điều kiện hiển thị: trong Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết
**Bước (J):** 1. Mở Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết · 2. Bấm nút "+ Liên kết vụ việc"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01) + Inputs/Processing FR-X.3-01
**Kiểm chéo:** `srs-fr-05-vu-viec.md:2036` + `srs-v3.5.md:4406` (quan hệ Vụ việc ↔ Hợp đồng)

> 🔴 **Phiếu này có 2 vế `GAP` (một trong đó do đặc tả TỰ MÂU THUẪN) → CẤM Pass toàn phiếu, kết luận Cần BA.**

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **mở cửa sổ chọn vụ việc**" | `srs-fr-14-hop-dong-tv.md:291` ("Nút [+ Liên kết VV] -> **modal multi-select**") | **MATCH** | TEST | **UI:** trong Nhóm 2, bấm nút liên kết vụ việc → một cửa sổ chọn phải mở ra và liệt kê vụ việc. **Đối chứng:** `list_network_requests` — có request lấy danh sách vụ việc gửi đi khi cửa sổ mở |
| **C2** | "…với **ô tìm kiếm theo mã vụ việc, tên doanh nghiệp hoặc lĩnh vực**" | **IM LẶNG** — `:291` chỉ khai "modal multi-select" và liệt kê cột của **bảng kết quả liên kết**, **không** khai tiêu chí tìm kiếm bên trong cửa sổ. Inputs FR-X.3-01 `:90` cũng chỉ khai trường `vu_viec_ids`, không khai bộ lọc | **GAP** | **BA** | Chỉ đo hiện trạng: ghi lại cửa sổ có ô tìm kiếm nào, tìm theo tiêu chí gì. **CẤM Pass/Reopen vế này** |
| **C3** | "…cho phép **chọn nhiều vụ việc cùng lúc**" | `srs-fr-14-hop-dong-tv.md:291` ("modal **multi-select**") | **MATCH** | TEST | **UI:** chọn **≥2** vụ việc trong cùng một lần mở cửa sổ — cả hai phải giữ được trạng thái đã chọn. **Đối chứng:** sau khi xác nhận, đếm số dòng tăng thêm trong bảng Nhóm 2 phải bằng số đã chọn |
| **C4** | "NSD chọn vụ việc và bấm "Xác nhận", hệ thống **thêm các vụ việc đã chọn vào bảng liên kết của hợp đồng**" | `srs-fr-14-hop-dong-tv.md:291` + `:123` ("Liên kết vụ việc: tạo liên kết many-to-many") + `:161` | **MATCH** | TEST | **UI:** xác nhận → bảng Nhóm 2 xuất hiện đúng các vụ việc vừa chọn (đúng mã). **Đối chứng:** đọc lại bản ghi hợp đồng qua API, danh sách vụ việc liên kết phải chứa đúng các mã đó |
| **C5** | "…**bản ghi liên kết nhiều-nhiều**" | **MÂU THUẪN**: `:90`, `:123`, `:291` khai **many-to-many**; nhưng sơ đồ thực thể `:352` và `:373` đặt khoá ngoại `hop_dong_tv_id` **trên bảng VU_VIEC** (một vụ việc trỏ tới **một** hợp đồng), `:424` lặp lại, và `srs-v3.5.md:4406` vẽ `HOP_DONG_TU_VAN ||--o{ VU_VIEC` (một-nhiều) | **GAP** | **BA** | Chỉ đo hiện trạng: thử liên kết **cùng một vụ việc** vào **hợp đồng thứ hai** rồi xem hợp đồng thứ nhất còn giữ liên kết không. **CẤM Pass/Reopen vế này** |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:291`** (thành phần Nhóm 2 — neo chính của C1/C3/C4, và là dòng gần nhất cho `GAP` C2)
```
| 7 | content (form) | Accordion: Vụ việc liên kết | table + modal | Bảng VV liên kết: Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. Nút [+ Liên kết VV] -> modal multi-select. N:N | click -> action | trang thêm/sửa — chỉ CB NV |
```
> Ba chữ "Mã VV / Tên DN / Lĩnh vực" ở đây là **cột của bảng kết quả**, **không phải** tiêu chí tìm kiếm trong cửa sổ chọn. Đây là chỗ rất dễ đọc nhầm thành `MATCH` cho C2.

**`srs-fr-14-hop-dong-tv.md:90`** (Inputs FR-X.3-01)
```
| 10 | vu_viec_ids | identifier[] | N | FK[] -> VU_VIEC (many-to-many) | — | người dùng chọn |
```

**`srs-fr-14-hop-dong-tv.md:123`** (Processing bước 6)
```
| 6 | Liên kết vụ việc: tạo liên kết many-to-many | — |
```

**`srs-fr-14-hop-dong-tv.md:161`** (Postconditions)
```
- Liên kết vụ việc many-to-many
```

**`srs-fr-14-hop-dong-tv.md:351`**–**`:352`** (sơ đồ thực thể, khối `VU_VIEC` — **phía mâu thuẫn**, khoá ngoại nằm trên VU_VIEC)
```
        text trang_thai
        identifier hop_dong_tv_id FK
```

**`srs-fr-14-hop-dong-tv.md:373`** (quan hệ trong sơ đồ — một vụ việc trỏ tới **một** hợp đồng)
```
    VU_VIEC }o--o| HOP_DONG_TU_VAN : "hop_dong_tv_id"
```

**`srs-fr-14-hop-dong-tv.md:424`** (bảng thuộc tính VU_VIEC — lặp lại khoá ngoại đơn)
```
| hop_dong_tv_id | identifier | N | FK → HOP_DONG_TU_VAN(id) | | HĐ tư vấn liên quan |
```

**`srs-v3.5.md:4406`** (sơ đồ thực thể tổng — cũng là **một-nhiều**)
```
    HOP_DONG_TU_VAN ||--o{ VU_VIEC : "lien_ket"
```

**`srs-fr-05-vu-viec.md:2036`** (bảng thuộc tính VU_VIEC ở nhóm Vụ việc — khẳng định lại khoá ngoại đơn)
```
| hop_dong_tv_id | identifier | N | FK → HOP_DONG_TU_VAN(id) | | HĐ tư vấn liên quan |
```
> **Tổng kết mâu thuẫn C5:** 4 chỗ khai `many-to-many` bằng lời (`:90`, `:123`, `:161`, `:291`) đối chọi 4 chỗ khai cấu trúc **một-nhiều** (`:352`, `:373`, `:424`, `srs-v3.5.md:4406`) — cùng được chốt trong **cùng một bản** SRS. Không xác định được chuẩn chấm ⇒ `GAP`, gửi BA (flow 04 §Đối chiếu đặc tả, dòng "Im lặng hoặc tự mâu thuẫn").

**`srs-fr-14-hop-dong-tv.md:29`** (mô tả quan hệ ở phần tổng quan — cũng nói 1 HĐ → nhiều VV, **không** nói ngược lại)
```
**Liên kết:** 1 HĐ -> nhiều vụ việc (V.I). HĐ <-> Vụ việc (V.I) <-> Chi trả (V.II).
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:291` ("trang thêm/sửa — **chỉ CB NV**"), `:68` (CB NV — CRUD đầy đủ), `:118` (TVV/CG chặn mọi thao tác Create/Update) | `:68`, `:118`, `:291` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Màn đo** | **Biểu mẫu thêm/sửa hợp đồng**, Nhóm 2 — `:291` chỉ khai nút `[+ Liên kết VV]` cho **trang thêm/sửa**. Nếu bước J dẫn vào trang chỉ-xem thì sẽ không có nút; ghi rõ đã đo trên màn nào | `:291` |
| **Dữ liệu — quyết định** | **≥2 vụ việc** trong phạm vi đơn vị và **chưa** liên kết với hợp đồng đang mở (để đo C3 "chọn nhiều"). Chỉ có 1 vụ việc thì C3 **không đo được** | `:291` |
| **Dữ liệu cho C5** | Thêm **1 hợp đồng thứ hai** để thử gắn **cùng một vụ việc** vào cả hai — đây là phép đo duy nhất phân biệt được nhiều-nhiều với một-nhiều | `:373` vs `:123` |
| **Hợp đồng chủ thể** | 1 hợp đồng đang ở trạng thái sửa được. Ưu tiên dùng lại hợp đồng đã dựng ở `_15` thay vì tạo mới | brief §4.5 |
| **Khai báo thay đổi** | Liên kết vụ việc **là mutate môi trường chung** ⇒ báo cáo khai: hợp đồng nào · gắn vụ việc nào · env nội bộ. **Không đụng dữ liệu đối tác** | brief §4.5 |

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Đọc nhầm `:291` thành chuẩn cho ô tìm kiếm.** Dòng này có đúng ba chữ "Mã VV / Tên DN / Lĩnh vực" — trùng khớp với ba tiêu chí đối tác nêu, nên rất dễ chấm C2 thành `MATCH`. Nhưng đó là **cột của bảng kết quả liên kết**, không phải bộ lọc trong cửa sổ chọn. C2 đã khóa `GAP`, **kết quả đo không đổi được quan hệ**.
- **Chọn nhiều nhưng chỉ một cái được thêm.** C3 chấm **chọn được nhiều**, C4 chấm **thêm đúng vào bảng**. Chọn 2 mà bảng chỉ tăng 1 dòng ⇒ C4 **Fail**. Phải đếm, không nhìn lướt.
- **Bảng Nhóm 2 hiện dòng mới nhưng chưa lưu xuống máy chủ.** Giao diện có thể chỉ thêm dòng trong bộ nhớ. Bắt buộc đọc lại bản ghi hợp đồng qua API sau khi xác nhận.
- **Đếm gộp thẻ bọc ngoài với thẻ con** của bảng → số nhân đôi. Đếm bằng selector dòng cụ thể.
- **Kết luận C5 "đạt" vì gắn được vụ việc vào hợp đồng thứ hai.** C5 đã khóa `GAP` do đặc tả tự mâu thuẫn — dù đo ra kết quả nào cũng **CẤM Pass**; ghi cả hiện trạng và câu hỏi BA.

**Dễ Fail oan:**
- **Fail C2 vì cửa sổ chỉ có một ô tìm kiếm chung, hoặc chỉ tìm theo mã.** Đặc tả im lặng về tiêu chí tìm ⇒ không Fail, chuyển BA.
- **Fail C5 vì gắn vụ việc vào hợp đồng thứ hai làm mất liên kết ở hợp đồng thứ nhất.** Hành vi này **khớp với sơ đồ thực thể** (`:373`, `srs-v3.5.md:4406`) dù ngược với chữ "many-to-many". Đặc tả tự mâu thuẫn ⇒ không Fail, chuyển BA.
- **Fail vì nút không tên "+ Liên kết vụ việc".** `:291` ghi `[+ Liên kết VV]`; đối tác ghi "+ Liên kết vụ việc". Cột K chấm **hành vi mở cửa sổ chọn**, không chấm nhãn nút.
- **Fail vì nút xác nhận không tên "Xác nhận".** Đặc tả **không** khai nhãn nút trong cửa sổ này; Phụ lục E §H4 (`srs-v3.5.md:6756`) chỉ chuẩn hóa "Thêm mới" và "Lưu". Không Fail vì nhãn.
- **Fail vì cửa sổ chọn là ngăn kéo chứ không phải hộp thoại.** `:272` cho phép cả `modal/drawer`.
- **Fail vì danh sách vụ việc trong cửa sổ ít hơn mong đợi.** Phân quyền dữ liệu theo đơn vị (BR-AUTH-08, `:496`) giới hạn tập nhìn thấy — đó là **đúng** đặc tả.
