# QLHDTVVCG_21 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 327 · **Mô tả (G):** Sửa thành công
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "Sửa" · 3. Nhập thông tin hợp lệ và nhấn Lưu
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — FR-X.3-01 Processing + Error Handling + AC + §3

> 🔴 **Phiếu này có 1 vế `DIFF` + 1 vế `GAP` → CẤM Pass toàn phiếu, kết luận Cần BA.**

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "**Giữ nguyên mã hợp đồng**" (sau khi lưu bản sửa) | `srs-fr-14-hop-dong-tv.md:119` (sinh mã **chỉ ở Thêm mới**) + `:81` + `:384` (`UNIQUE`) | **MATCH** | TEST | **UI:** ghi mã trước khi sửa → sửa 1 trường → Lưu → mở lại bản ghi, mã phải **y nguyên**. **Đối chứng:** đọc `ma_hop_dong` qua API trước và sau khi lưu, hai giá trị phải trùng |
| **C2** | "…**cập nhật các trường thay đổi**" | `srs-fr-14-hop-dong-tv.md:122` ("Tạo hoặc **cập nhật** bản ghi hợp đồng…") + `:159` | **MATCH** | TEST | **UI:** đổi **hai** trường có thể quan sát (vd Tên hợp đồng + Giá trị) → Lưu → mở lại, hai giá trị mới phải hiện đúng. **Đối chứng:** đọc lại bản ghi qua API, so `ten_hop_dong` + `gia_tri_hop_dong` với giá trị vừa nhập |
| **C3** | "…**thay thế** danh sách mốc tiến độ / thanh toán / vụ việc liên kết / tệp đính kèm **theo dữ liệu mới**" | **IM LẶNG về ngữ nghĩa thay-thế-toàn-bộ.** `:122` chỉ nói "Tạo hoặc **cập nhật**", `:123` nói "**tạo** liên kết many-to-many" — đặc tả **không phát biểu** rằng danh sách cũ bị xoá sạch rồi ghi lại theo dữ liệu mới, cũng không nói là cộng dồn. Không có mục nào khai hành vi gỡ bỏ phần tử cũ khi lưu bản sửa | **GAP** | **BA** | Chỉ đo hiện trạng để mô tả cho BA: trước khi lưu, xoá 1 mốc cũ + thêm 1 mốc mới; sau khi lưu đếm lại. **CẤM Pass/Reopen vế này** |
| **C4** | "Hệ thống hiển thị thông báo **"Đã lưu hợp đồng"**" — chấm theo **hành vi**: có báo lưu thành công | `srs-fr-14-hop-dong-tv.md:173` (`INF-HDTV-01`, nguyên văn đúng chuỗi) + `:187` (AC nêu **đích danh** chế độ Chỉnh sửa) + `:175` | **MATCH** | TEST | **UI:** cài `MutationObserver` trên `document.body` **trước** khi bấm Lưu (CẤM lọc trùng) → bắt chữ hiện ra. **Đối chứng:** mã phản hồi của chính request lưu, gắn cùng mốc thời gian |
| **C5** | "…và **quay về danh sách**" | `srs-fr-14-hop-dong-tv.md:175` — **BA chốt 2026-08-06 nói NGƯỢC LẠI**: nhóm X.3 **không có màn danh sách độc lập**, sau khi lưu **trả người dùng về ngữ cảnh đã mở biểu mẫu**; `:187` cũng ghi "quay về ngữ cảnh đã mở nó" | **DIFF** | **BA** | Chỉ đo hiện trạng để ghi dev đang theo phía nào (sau khi lưu màn dừng ở đâu). **CẤM Pass kể cả khi web quay về danh sách đúng như đối tác mong đợi** |

### Câu bắt buộc cho vế `DIFF` (soạn sẵn)

> **CẦN BA CONFIRM:** đối tác kỳ vọng sau khi lưu bản sửa thì hệ thống **quay về màn danh sách hợp đồng**; SRS quy định nhóm X.3 **không có màn danh sách độc lập**, sau khi lưu hệ thống **đóng biểu mẫu và trả người dùng về ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên) — `srs-fr-14-hop-dong-tv.md:175` (`[BA chốt 2026-08-06]`) và `:187`; web/dev hiện tại **&lt;điền sau khi đo&gt;**.

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:119`** (Processing bước 2 — chỉ Thêm mới sinh mã)
```
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
```

**`srs-fr-14-hop-dong-tv.md:122`**–**`:123`** (Processing bước 5, 6 — **nguồn của `GAP` C3**)
```
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
| 6 | Liên kết vụ việc: tạo liên kết many-to-many | — |
```
> Bước 5 dùng chữ "**cập nhật**", bước 6 dùng chữ "**tạo**" — **không** dòng nào phát biểu việc **gỡ bỏ** phần tử cũ không còn trong dữ liệu mới. Tệp đính kèm (`:92`) thậm chí không xuất hiện trong bảng Processing. ⇒ ngữ nghĩa "thay thế" mà đối tác kỳ vọng **chưa có trong đặc tả**.

**`srs-fr-14-hop-dong-tv.md:159`**–**`:162`** (Postconditions — cũng không nói "thay thế")
```
- HĐ được tạo/cập nhật/xóa mềm
- Mốc tiến độ và thanh toán giai đoạn được quản lý
- Liên kết vụ việc many-to-many
- AUDIT_LOG ghi nhận
```

**`srs-fr-14-hop-dong-tv.md:173`** (Error Handling — dòng thông tin I1)
```
| I1 | Lưu HĐ thành công (thêm mới hoặc chỉnh sửa) | INF-HDTV-01 | "Đã lưu hợp đồng" | INFO |
```

**`srs-fr-14-hop-dong-tv.md:175`** (ghi chú BA — **nguồn của `DIFF` C5**)
```
> **Câu thông báo sau khi lưu + điều hướng** `[BA chốt 2026-08-06]`: dùng chung một câu `INF-HDTV-01` cho cả chế độ Thêm mới lẫn Chỉnh sửa. Nhóm X.3 **không có màn danh sách độc lập** (xem §3 — quyết định BA 11/05/2026), nên sau khi lưu hệ thống đóng biểu mẫu và trả người dùng về **ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên) — đây là biến thể hợp lệ của Phụ lục E §H7 "Sau khi thêm mới quay về danh sách".
```

**`srs-fr-14-hop-dong-tv.md:187`** (Acceptance Criteria — nêu đích danh chế độ Chỉnh sửa)
```
- **Given** CB NV lưu hợp đồng hợp lệ **When** ở chế độ Thêm mới hoặc Chỉnh sửa **Then** hiện thông báo `INF-HDTV-01` "Đã lưu hợp đồng" + đóng biểu mẫu, quay về ngữ cảnh đã mở nó
```

**`srs-fr-14-hop-dong-tv.md:81`** + **`:384`** (mã hợp đồng do hệ thống quản, UNIQUE)
```
| 1 | ma_hop_dong | text | Y (auto) | Format: HDTV-{YYYYMMDD}-{SEQ} | auto-gen | hệ thống |
| ma_hop_dong | text | Y | UNIQUE | Auto-gen | Mã HĐ |
```

**`srs-fr-14-hop-dong-tv.md:120`**–**`:121`** (hai kiểm tra để "nhập thông tin hợp lệ")
```
| 3 | Kiểm tra: ngày bắt đầu <= ngày kết thúc | — |
| 4 | Kiểm tra: tổng thanh toán giai đoạn <= giá trị HĐ | — |
```

**`srs-fr-14-hop-dong-tv.md:394`**–**`:395`** (cách lưu hai nhóm con — dữ liệu bối cảnh cho C3)
```
| moc_tien_do | text (long) | N | | | Mốc tiến độ (JSON array) |
| thanh_toan_giai_doan | text (long) | N | | | Thanh toán theo giai đoạn (JSON array) |
```
> Hai nhóm này lưu dạng mảng ngay trên bản ghi hợp đồng ⇒ ghi đè cả mảng là **cách làm khả dĩ**, nhưng đặc tả **không phát biểu** điều đó, và **vụ việc liên kết** (bảng nối N:N) cùng **tệp đính kèm** thì không lưu theo cách này ⇒ vẫn `GAP`.

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68`, `:118` (TVV/CG chặn mọi thao tác Update), `:288`, `:290` | `:68`, `:118`, `:288`, `:290` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu — quyết định** | **1 hợp đồng đã có sẵn ≥1 mốc tiến độ + ≥1 giai đoạn thanh toán + ≥1 vụ việc liên kết + ≥1 tệp đính kèm.** Không có đủ 4 nhóm thì C3 **không đo được** (không có "danh sách cũ" để xem có bị thay thế hay không). Ưu tiên dùng lại hợp đồng đã dựng ở `_15` | `:122`, `:123`, `:92` |
| **Ghi mốc so trước khi sửa** | Trước khi bấm Lưu, ghi lại: mã hợp đồng · giá trị hai trường sắp đổi · **số phần tử từng nhóm con**. Không có mốc so thì C1/C2/C3 chỉ là quan sát tĩnh | `:122` |
| **Kịch bản đo C3** | Trong cùng một lần sửa: **xoá 1 phần tử cũ** và **thêm 1 phần tử mới** ở nhóm Mốc tiến độ → Lưu → đếm lại. Nếu sau khi lưu còn cả cũ lẫn mới = cộng dồn; chỉ còn dữ liệu mới = thay thế. Ghi lại kết quả cho BA, **không** kết luận đúng/sai | `:122` |
| **Giá trị nhập phải hợp lệ** | Ngày bắt đầu ≤ kết thúc (`:120`); tổng thanh toán ≤ giá trị hợp đồng (`:121`). Vi phạm sẽ bị chặn lưu và phiếu không đo được | `:120`, `:121` |
| **Khai báo thay đổi** | Sửa hợp đồng **là mutate môi trường chung** ⇒ báo cáo khai: hợp đồng nào · đổi trường gì · env nội bộ | brief §4.5 |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Thấy thông báo lưu là kết luận đạt.** C2 chấm **dữ liệu đã đổi thật**. Phải mở lại bản ghi sau khi lưu và đối chứng qua API — giao diện có thể vẫn giữ giá trị vừa gõ trong bộ nhớ trình duyệt dù máy chủ chưa nhận.
- **Đếm nhóm con trên biểu mẫu chưa tải lại.** Giống bẫy ở `_15`: tải lại rồi mới đếm.
- **Đổi một trường rồi suy ra "mọi trường đều cập nhật được".** Đổi **hai** trường khác kiểu (chữ + số) để giảm rủi ro; nhưng **không** mở rộng thành ma trận đủ 12 trường — cột K không đòi, flow 04 luật khóa 4 cấm.
- **Kết luận C3 "đạt" vì danh sách sau khi lưu đúng y dữ liệu mới.** C3 đã khóa `GAP` — **kết quả đo không đổi được quan hệ**. Trong tóm tắt phải nói rõ "web hiện tại đúng kỳ vọng đối tác" để không bị đọc nhầm thành lỗi; câu hỏi BA là **bổ sung điều này vào đặc tả**.
- **Kết luận C5 "đạt" vì web quay về danh sách.** C5 đã khóa `DIFF` — CẤM Pass.
- **Thông báo tự tắt đã trượt** → kết luận sai "im lặng". Cài `MutationObserver` **trước** khi bấm Lưu.

**Dễ Fail oan:**
- **Fail C5 vì sau khi lưu không quay về danh sách.** Đó chính là `DIFF`: `:175` và `:187` nói phải trả về **ngữ cảnh đã mở biểu mẫu**. Không Fail, chuyển BA.
- **Fail C3 vì phần tử cũ vẫn còn sau khi lưu (cộng dồn thay vì thay thế).** Đặc tả im lặng ⇒ không Fail, chuyển BA.
- **Fail vì câu chữ thông báo lệch, hoặc vì thông báo giống hệt lúc Thêm mới.** `:173` và `:175` quy định **dùng chung một câu** cho cả hai chế độ ⇒ giống nhau là **đúng**.
- **Fail vì mã hợp đồng không đổi.** Đó là **yêu cầu** của C1 — `:119` chỉ sinh mã ở Thêm mới.
- **Fail vì tệp đính kèm cũ không bị gỡ.** Tệp đính kèm thậm chí **không xuất hiện** trong bảng Processing (`:118`–`:125`) ⇒ thuộc `GAP` C3.
- **Fail vì phải qua bước phê duyệt.** `:302` và `:462`: nhóm X.3 **KHÔNG cần phê duyệt, chỉ CRUD thuần**.
