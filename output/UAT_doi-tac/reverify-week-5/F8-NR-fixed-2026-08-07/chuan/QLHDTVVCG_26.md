# QLHDTVVCG_26 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 332 · **Mô tả (G):** Thêm giai đoạn thanh toán
**Điều kiện (H):** 1. Điều kiện hiển thị: trong Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết
**Bước (J):** 1. Mở Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết · 2. Bấm nút "Thêm giai đoạn thanh toán"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01) + Inputs — Thanh toán giai đoạn + Processing + Error Handling

> 🔴 **Phiếu này có 1 vế `DIFF` → CẤM Pass toàn phiếu, kết luận Cần BA.**

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **thêm một dòng trống vào bảng**; NSD nhập trực tiếp trên dòng: **Giai đoạn, Số tiền, Ngày thanh toán (tùy chọn), Trạng thái thanh toán**" | `srs-fr-14-hop-dong-tv.md:293` ("**editable-table** … **Inline-edit**: Giai đoạn / Số tiền / Ngày TT / Trạng thái") + Inputs `:108`–`:112` (cột **Bắt buộc**: Giai đoạn `Y`, Số tiền `Y`, Ngày TT `N`, Trạng thái `Y`) | **MATCH** | TEST | **UI:** ghi số dòng trước → bấm nút thêm giai đoạn → bảng tăng đúng 1 dòng, ô rỗng, gõ được ngay tại chỗ, đủ 4 mục và **Ngày thanh toán không bắt buộc**. **Đối chứng:** `evaluate_script` đếm số dòng trước/sau + đọc `value` các ô của dòng mới |
| **C2** | "**Khi NSD nhập Số tiền, hệ thống tự cộng dồn và cập nhật thanh tiến trình tổng** phía trên bảng" | `srs-fr-14-hop-dong-tv.md:301` định nghĩa thanh tiến trình = **SUM(đã thanh toán) / giá trị HĐ**, tức **chỉ cộng phần ĐÃ thanh toán**; dòng mới mặc định `CHUA_THANH_TOAN` (`:112`) ⇒ theo đặc tả, nhập Số tiền vào dòng chưa thanh toán **KHÔNG** làm thanh tiến trình nhúc nhích. Đối tác kỳ vọng cộng dồn ngay khi nhập ⇒ **ngược nhau** | **DIFF** | **BA** | Chỉ đo hiện trạng: nhập Số tiền vào dòng mới (giữ trạng thái mặc định), đọc % thanh tiến trình trước/sau. **CẤM Pass kể cả khi thanh tiến trình nhảy đúng như đối tác mong đợi** |
| **C3** | "Nếu **tổng số tiền các giai đoạn vượt Giá trị hợp đồng**, hệ thống **đánh dấu cảnh báo**" | `srs-fr-14-hop-dong-tv.md:121` (bước kiểm tra), `:293` ("Validate: SUM <= giá trị HĐ"), `:170` (`ERR-HDTV-03` "Tổng thanh toán vượt giá trị hợp đồng") | **MATCH** | TEST | **UI:** nhập một giai đoạn có Số tiền lớn hơn Giá trị hợp đồng → hệ thống phải báo cho người dùng biết tổng đã vượt. **Đối chứng:** cài `MutationObserver` **trước** thao tác (CẤM lọc trùng) để bắt cả thông báo tự tắt; hoặc đọc `innerText` vùng lỗi cạnh ô Số tiền |

### Câu bắt buộc cho vế `DIFF` (soạn sẵn)

> **CẦN BA CONFIRM:** đối tác kỳ vọng **ngay khi nhập Số tiền của một giai đoạn**, hệ thống **tự cộng dồn và cập nhật thanh tiến trình tổng**; SRS quy định thanh tiến trình thanh toán = **SUM(đã thanh toán) / giá trị hợp đồng × 100%** — `srs-fr-14-hop-dong-tv.md:301` — tức chỉ tính phần **đã thanh toán**, trong khi giai đoạn mới mặc định là **chưa thanh toán** (`:112`), nên theo SRS thanh tiến trình **không** đổi khi mới nhập số tiền; web/dev hiện tại **&lt;điền sau khi đo&gt;**.

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:293`** (thành phần Nhóm 4 — neo của C1 và C3)
```
| 9 | content (form) | Accordion: Thanh toán giai đoạn | editable-table | Inline-edit: Giai đoạn / Số tiền / Ngày TT / Trạng thái (CHUA_THANH_TOAN / DA_THANH_TOAN). Validate: SUM <= giá trị HĐ. Thanh tiến độ TT phía trên | inline-edit | trang thêm/sửa — chỉ CB NV |
```
> ⚠️ Dòng này **không** khai nút `[+ Thêm giai đoạn thanh toán]` (khác với `:292` có khai `[+ Thêm mốc]`). Việc thêm dòng vẫn suy được từ kiểu **editable-table / inline-edit** cộng với bảng Inputs `:106`–`:112` và bước xử lý `:122`, nên C1 giữ `MATCH`; nhưng nếu web **không có nút nào để thêm dòng** thì phải ghi rõ và hỏi BA thay vì Fail thẳng.

**`srs-fr-14-hop-dong-tv.md:104`**–**`:112`** (Inputs — Thanh toán giai đoạn, **trọn bảng**)
```
**Inputs -- Thanh toán giai đoạn:**

| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | hop_dong_id | identifier | Y | FK -> HOP_DONG_TU_VAN | — | hệ thống |
| 2 | giai_doan | text | Y | — | — | người dùng nhập |
| 3 | so_tien | money | Y | — | — | người dùng nhập |
| 4 | ngay_thanh_toan | date | N | — | — | người dùng chọn |
| 5 | trang_thai_tt | text | Y | CHUA_THANH_TOAN / DA_THANH_TOAN | CHUA_THANH_TOAN | người dùng chọn |
```
> `ngay_thanh_toan` **Bắt buộc = N** ⇒ khớp chữ "(tùy chọn)". `trang_thai_tt` **Mặc định = `CHUA_THANH_TOAN`** ⇒ đây là mắt xích của vế `DIFF` C2.

**`srs-fr-14-hop-dong-tv.md:301`** (Quy tắc tương tác — **nguồn của vế `DIFF`**)
```
- Progress bar thanh toán = SUM(đã thanh toán) / giá trị HĐ * 100%
```
> Công thức nói rõ tử số là **SUM(đã thanh toán)**, không phải tổng số tiền các giai đoạn.

**`srs-fr-14-hop-dong-tv.md:121`** (Processing bước 4 — neo của C3)
```
| 4 | Kiểm tra: tổng thanh toán giai đoạn <= giá trị HĐ | — |
```

**`srs-fr-14-hop-dong-tv.md:170`** (Error Handling — dòng E3, neo của C3)
```
| E3 | Tổng thanh toán > giá trị HĐ | ERR-HDTV-03 | "Tổng thanh toán vượt giá trị hợp đồng" | ERROR |
```
> ⚠️ Đặc tả xếp mức **ERROR** (chặn), đối tác chỉ nói "**đánh dấu cảnh báo**". Cả hai đều đòi hệ thống **báo cho người dùng biết** ⇒ C3 giữ `MATCH` ở mức hành vi. Xem mục (d) về ca web chỉ cảnh báo mà vẫn lưu được.

**`srs-fr-14-hop-dong-tv.md:86`** (Giá trị hợp đồng — mẫu số của công thức)
```
| 6 | gia_tri_hop_dong | money | Y | Giá trị HĐ | — | người dùng nhập |
```

**`srs-fr-14-hop-dong-tv.md:155`** (Outputs — tiến độ thanh toán là một cột đầu ra)
```
| 9 | tien_do_tt | number | luôn | progress bar % |
```

**`srs-fr-14-hop-dong-tv.md:122`** (Processing — giai đoạn thanh toán được lưu cùng hợp đồng)
```
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
```

**`srs-fr-14-hop-dong-tv.md:395`** (cách lưu — bối cảnh)
```
| thanh_toan_giai_doan | text (long) | N | | | Thanh toán theo giai đoạn (JSON array) |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:293` ("trang thêm/sửa — **chỉ CB NV**"), `:68`, `:118` | `:68`, `:118`, `:293` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Màn đo** | **Biểu mẫu thêm/sửa hợp đồng**, Nhóm 4 | `:293` |
| **Dữ liệu — quyết định** | **1 hợp đồng có Giá trị hợp đồng > 0 và biết trước con số đó.** Không biết mẫu số thì **không tính được** thanh tiến trình (C2) và **không dựng được** ca vượt ngưỡng (C3). Ghi lại giá trị hợp đồng trước khi đo | `:86`, `:301` |
| **Dữ liệu cho C2** | Ghi **% thanh tiến trình trước khi nhập** làm mốc so. Nên có sẵn **≥1 giai đoạn đã thanh toán** để thanh tiến trình khác 0 — nếu đang 0% thì khó phân biệt "không đổi vì đúng công thức" với "không đổi vì hỏng" | `:301` |
| **Giá trị nhập cho C3** | Một giai đoạn có Số tiền **lớn hơn hẳn** Giá trị hợp đồng (vd gấp đôi) để chắc chắn vượt ngưỡng ngay ở một dòng, không phụ thuộc các dòng cũ | `:121`, `:170` |
| **Không cần lưu** | Cột K dừng ở hành vi trên biểu mẫu ⇒ **không bắt buộc bấm Lưu**. Nếu đã nhập số tiền vượt ngưỡng thì bấm Hủy để không ghi dữ liệu sai vào môi trường chung | bước J của phiếu |

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Kết luận C2 "đạt" vì thanh tiến trình nhảy ngay khi nhập số tiền.** C2 đã khóa `DIFF` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Web làm đúng ý đối tác nghĩa là **lệch công thức `:301`**; vẫn CẤM Pass, ghi hiện trạng + câu hỏi BA.
- **Đo C2 mà không ghi mốc % trước khi nhập.** Không có mốc so thì mọi kết luận về "có cộng dồn hay không" đều là suy đoán.
- **Nhầm hai loại tổng.** `:301` dùng **SUM(đã thanh toán)**; cột K dùng **tổng số tiền các giai đoạn**. Hai con số này khác nhau khi có giai đoạn chưa thanh toán. Phải ghi rõ đang đo con số nào.
- **Bấm nút thêm giai đoạn nhưng mở hộp thoại nhập riêng.** `:293` khai **editable-table / inline-edit** ⇒ nhập phải diễn ra **trên dòng**. Hộp thoại riêng ⇒ C1 **Fail**.
- **Không gõ thử vào ô** → Pass bằng quan sát tĩnh, flow 04 cấm khi vế là hành động.
- **Thông báo vượt ngưỡng tự tắt đã trượt** → kết luận sai "im lặng" ở C3. Cài `MutationObserver` **trước** thao tác.
- **Đếm gộp thẻ bọc ngoài với thẻ con** → số dòng nhân đôi ở C1.

**Dễ Fail oan:**
- **Fail C2 vì thanh tiến trình đứng yên khi nhập số tiền.** Đó chính là điểm `DIFF` — đứng yên **có thể là đúng** công thức `:301` (dòng mới mặc định chưa thanh toán). Không Fail, chuyển BA.
- **Fail C3 vì hệ thống chặn lưu thay vì chỉ tô cảnh báo.** `:170` xếp mức **ERROR** ⇒ chặn là **chặt hơn** và đúng đặc tả. C3 chấm "có báo cho người dùng biết đã vượt", chặn vẫn thoả.
- **Ngược lại — nếu web chỉ tô cảnh báo mà VẪN lưu được:** vế C3 vẫn đạt (có đánh dấu cảnh báo đúng ý đối tác), nhưng đó là **lệch đặc tả `:121`/`:170`** theo hướng lỏng hơn. Ghi nhận theo gate "bug mới tự lộ" **và** nêu trong phần cần BA chốt; **không** dùng để đổi quan hệ vế C3.
- **Fail vì câu chữ cảnh báo không phải "Tổng thanh toán vượt giá trị hợp đồng".** Chấm theo **hành vi**; chữ khác nhỏ ⇒ ghi chênh lệch cho BA.
- **Fail vì dòng mới có sẵn Trạng thái "Chưa thanh toán".** `:112` ghi Mặc định `CHUA_THANH_TOAN` ⇒ có sẵn là **đúng**, dù cột K nói "dòng trống".
- **Fail vì thiếu trường `hop_dong_id`.** `:108` ghi Nguồn = **hệ thống** ⇒ không hiện trên dòng nhập.
- **Fail vì không có nút "Thêm giai đoạn thanh toán".** `:293` **không khai nút này** (khác `:292` có `[+ Thêm mốc]`). Nếu web thêm dòng bằng cách khác (bấm vào dòng cuối, biểu tượng dấu cộng…) thì vẫn thoả `inline-edit`; chỉ khi **không có cách nào thêm dòng** mới ghi Chưa chốt + hỏi BA.
