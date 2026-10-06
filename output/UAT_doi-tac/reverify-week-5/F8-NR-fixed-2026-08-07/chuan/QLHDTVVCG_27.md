# QLHDTVVCG_27 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 333 · **Mô tả (G):** Xóa giai đoạn thanh toán
**Điều kiện (H):** 1. Điều kiện hiển thị: trên mỗi dòng của bảng thanh toán giai đoạn (Nhóm 4)
**Bước (J):** 1. Mở Nhóm 4 (Thanh toán giai đoạn) của biểu mẫu chi tiết · 2. Bấm nút "Xóa giai đoạn thanh toán"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01) + Processing FR-X.3-01

> 🔴 **Phiếu này có 1 vế `GAP` → CẤM Pass toàn phiếu, kết luận Cần BA.**

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **bỏ dòng khỏi bảng**" (xoá một giai đoạn thanh toán) | **IM LẶNG** — `:293` khai bảng Nhóm 4 là `editable-table` với 4 trường sửa tại chỗ, kiểm tra tổng và thanh tiến trình, **nhưng không khai nút xoá dòng nào**; bảng Processing `:118`–`:125` (đã đọc trọn) chỉ có bước 7 xoá **hợp đồng**, không có bước xoá **giai đoạn thanh toán**. So sánh: `:291` có khai `[Bỏ liên kết]`, `:292` có khai `[+ Thêm mốc]` — riêng `:293` không khai nút nào | **GAP** | **BA** | Chỉ đo hiện trạng: ghi lại trên dòng có nút/biểu tượng xoá không, bấm thì dòng có biến mất không. **CẤM Pass/Reopen vế này** |
| **C2** | "…và **cập nhật lại thanh tiến trình tổng**" | `srs-fr-14-hop-dong-tv.md:301` (công thức thanh tiến trình) + `:155` | **MATCH** | TEST | **UI:** ghi % thanh tiến trình và danh sách giai đoạn trước khi xoá → xoá **một dòng đã ở trạng thái "đã thanh toán"** → % phải giảm đúng theo công thức `SUM(đã thanh toán) / giá trị HĐ`. **Đối chứng:** tự tính lại % từ các dòng còn lại và giá trị hợp đồng, so với số hiển thị |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:293`** (dòng duy nhất khai bảng Nhóm 4 — **bằng chứng `GAP` C1**)
```
| 9 | content (form) | Accordion: Thanh toán giai đoạn | editable-table | Inline-edit: Giai đoạn / Số tiền / Ngày TT / Trạng thái (CHUA_THANH_TOAN / DA_THANH_TOAN). Validate: SUM <= giá trị HĐ. Thanh tiến độ TT phía trên | inline-edit | trang thêm/sửa — chỉ CB NV |
```

**`srs-fr-14-hop-dong-tv.md:291`**–**`:292`** (hai nhóm kề bên — **có** khai nút, để đối chiếu cho thấy `:293` thiếu)
```
| 7 | content (form) | Accordion: Vụ việc liên kết | table + modal | Bảng VV liên kết: Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. Nút [+ Liên kết VV] -> modal multi-select. N:N | click -> action | trang thêm/sửa — chỉ CB NV |
| 8 | content (form) | Accordion: Mốc tiến độ | editable-table | Inline-edit: Tên mốc / Ngày dự kiến / Ngày thực tế / Trạng thái mốc (CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH). [+ Thêm mốc] | inline-edit | trang thêm/sửa — chỉ CB NV |
```
> Nhóm 2 khai `[Bỏ liên kết]`, Nhóm 3 khai `[+ Thêm mốc]` — **Nhóm 4 không khai nút nào**. Đây là căn cứ cho `GAP` chứ không phải suy đoán từ một lệnh tìm rỗng.

**`srs-fr-14-hop-dong-tv.md:118`**–**`:125`** (Processing FR-X.3-01 — **trọn bảng**, không có bước xoá giai đoạn thanh toán)
```
| 1 | Kiểm tra quyền. CB NV: áp phân quyền đơn vị (BR-AUTH-08). TVV/CG: chỉ trả HĐ có `tu_van_vien_id` thuộc về user đang đăng nhập; chặn mọi thao tác Create/Update/Delete | BR-AUTH-01, BR-AUTH-08 |
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
| 3 | Kiểm tra: ngày bắt đầu <= ngày kết thúc | — |
| 4 | Kiểm tra: tổng thanh toán giai đoạn <= giá trị HĐ | — |
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
| 6 | Liên kết vụ việc: tạo liên kết many-to-many | — |
| 7 | Xóa: chỉ khi KHÔNG có vụ việc liên kết, xóa mềm | BR-DATA-01 |
| 8 | Ghi nhật ký thao tác | BR-DATA-05 |
```
> Bước 7 nói về xoá **hợp đồng** (điều kiện là vụ việc liên kết, hệ quả là xoá mềm) — **không** phải xoá một dòng thanh toán.

**`srs-fr-14-hop-dong-tv.md:301`** (Quy tắc tương tác — neo của C2)
```
- Progress bar thanh toán = SUM(đã thanh toán) / giá trị HĐ * 100%
```

**`srs-fr-14-hop-dong-tv.md:155`** (Outputs — tiến độ thanh toán)
```
| 9 | tien_do_tt | number | luôn | progress bar % |
```

**`srs-fr-14-hop-dong-tv.md:112`** (trạng thái thanh toán — quyết định dòng nào ảnh hưởng thanh tiến trình)
```
| 5 | trang_thai_tt | text | Y | CHUA_THANH_TOAN / DA_THANH_TOAN | CHUA_THANH_TOAN | người dùng chọn |
```

**`srs-fr-14-hop-dong-tv.md:395`** (cách lưu — bối cảnh)
```
| thanh_toan_giai_doan | text (long) | N | | | Thanh toán theo giai đoạn (JSON array) |
```

**`srs-fr-14-hop-dong-tv.md:160`** (Postconditions — chỉ nói "được quản lý", không nói xoá)
```
- Mốc tiến độ và thanh toán giai đoạn được quản lý
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:293` ("trang thêm/sửa — **chỉ CB NV**"), `:68`, `:118` (TVV/CG chặn mọi thao tác Update/Delete) | `:68`, `:118`, `:293` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Màn đo** | **Biểu mẫu thêm/sửa hợp đồng**, Nhóm 4 | `:293` |
| **Dữ liệu — quyết định** | **1 hợp đồng có ≥2 giai đoạn thanh toán**, trong đó **≥1 dòng ở trạng thái "đã thanh toán"**. Cần ≥2 để sau khi xoá còn bảng mà đếm; cần dòng "đã thanh toán" vì theo `:301` **chỉ dòng đã thanh toán mới ảnh hưởng thanh tiến trình** — xoá dòng chưa thanh toán thì % **không đổi** và C2 không đo được gì | `:301`, `:112` |
| **Ghi mốc so trước khi bấm** | Ghi: **số dòng**, **giai đoạn của dòng sắp xoá**, **số tiền + trạng thái từng dòng**, **giá trị hợp đồng**, **% thanh tiến trình hiện tại**. Thiếu bộ số này thì C2 không tự tính lại để đối chứng được | `:301` |
| **Cách dựng** | Chạy `_26` trước để có giai đoạn, hoặc dùng lại hợp đồng đã dựng ở `_15`. Đặt ≥1 dòng sang trạng thái "đã thanh toán" | thứ tự chạy ở `00-TONG-HOP-QLHDTVVCG.md` |
| **Khai báo thay đổi** | Xoá giai đoạn **là mutate môi trường chung** ⇒ báo cáo khai: hợp đồng nào · xoá giai đoạn nào · env nội bộ | brief §4.5 |

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Kết luận C1 "đạt" vì có nút xoá và bấm thì dòng biến mất.** C1 đã khóa `GAP` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Trong tóm tắt phải nói rõ "web hiện tại **đúng kỳ vọng đối tác**" để không bị đọc nhầm thành lỗi; câu hỏi BA là **bổ sung điều này vào đặc tả**, không phải chặn bàn giao.
- **Xoá dòng "chưa thanh toán" rồi thấy % không đổi và chấm C2 đạt.** Theo `:301` thì % **đương nhiên** không đổi — phép đo này **không chứng minh được gì**. Bắt buộc xoá một dòng **đã thanh toán**.
- **Ngược lại: xoá dòng "chưa thanh toán" mà % lại đổi** ⇒ web đang tính theo tổng tất cả giai đoạn, **lệch công thức `:301`** — cùng bản chất với vế `DIFF` ở phiếu `_26`. Ghi vào cùng câu hỏi BA, không tự chấm.
- **Dòng biến khỏi bảng nhưng chưa gỡ ở máy chủ.** Giao diện có thể chỉ gỡ trong bộ nhớ, chờ bấm Lưu. Ghi rõ hành vi quan sát được.
- **Đọc % bằng mắt thay vì tự tính lại.** Đối chứng độc lập của C2 là **tự tính** `SUM(đã thanh toán) / giá trị HĐ` từ các dòng còn lại rồi so — không phải bấm lại nút.
- **Đếm gộp thẻ bọc ngoài với thẻ con** → số dòng nhân đôi.

**Dễ Fail oan:**
- **Fail C1 vì trên dòng không có nút xoá.** `:293` **không khai** nút xoá cho bảng Nhóm 4 (trong khi `:291` và `:292` có khai nút cho nhóm của mình) ⇒ thiếu nút **có thể là đúng** đặc tả. Không Fail, chuyển BA.
- **Fail vì phải bấm Lưu mới có hiệu lực.** Đặc tả không khai thời điểm ghi xuống; `:122` cho biết giai đoạn thanh toán được lưu **cùng** bản ghi hợp đồng.
- **Fail vì % không về 0 sau khi xoá.** Công thức `:301` chỉ trừ phần của dòng bị xoá; các dòng đã thanh toán còn lại vẫn tính.
- **Fail vì nút xoá là biểu tượng thùng rác chứ không phải chữ.** Phụ lục E §H6 (`srs-v3.5.md:6758`) bắt cột Hành động dùng **icon + tooltip** ⇒ icon là **đúng**.
- **Fail vì không có hộp xác nhận trước khi xoá dòng.** Cột K **không nhắc** hộp xác nhận ⇒ không thành tiêu chí chấm (khác `_23`, nơi đối tác có nhắc).
