# QLHDTVVCG_24 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 330 · **Mô tả (G):** Thêm mốc
**Điều kiện (H):** 1. Điều kiện hiển thị: trong Nhóm 3 (Mốc tiến độ) của biểu mẫu chi tiết
**Bước (J):** 1. Mở Nhóm 3 (Mốc tiến độ) của biểu mẫu chi tiết · 2. Bấm nút "Thêm mốc"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01) + Inputs — Mốc tiến độ

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **thêm một dòng trống vào bảng mốc tiến độ**; NSD **nhập trực tiếp trên dòng**" | `srs-fr-14-hop-dong-tv.md:292` ("**editable-table** … **Inline-edit** … **[+ Thêm mốc]**") | **MATCH** | TEST | **UI:** ghi số dòng trước → bấm nút thêm mốc → bảng tăng đúng 1 dòng, các ô trên dòng đó **rỗng** và **gõ được ngay tại chỗ** (gõ thử vào ô Tên mốc, ký tự phải nhận). **Đối chứng:** `evaluate_script` đếm số dòng của bảng trước/sau và đọc `value` các ô của dòng mới |
| **C2** | "…nhập trên dòng: **Tên mốc, Ngày dự kiến, Ngày thực tế (tùy chọn), Trạng thái mốc**" | `srs-fr-14-hop-dong-tv.md:292` (liệt kê đúng 4 mục) + bảng Inputs `:98`–`:102` (cột **Bắt buộc**: Tên mốc `Y`, Ngày dự kiến `Y`, Ngày thực tế `N`, Trạng thái mốc `Y`) | **MATCH** | TEST | **UI:** trên dòng vừa thêm, đọc `innerText` nhãn/tiêu đề cột và đếm số ô nhập — phải có đủ 4 mục, trong đó **Ngày thực tế không bắt buộc**. **Đối chứng:** nhập đủ 3 trường bắt buộc, bỏ trống Ngày thực tế → dòng phải được chấp nhận (không báo thiếu) |

> Cột K **không nhắc** tới lưu, tới xoá mốc, tới thứ tự dòng hay tới kiểm tra ngày ⇒ **không tách thành vế**.

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:292`** (thành phần Nhóm 3 — neo chính của cả hai vế)
```
| 8 | content (form) | Accordion: Mốc tiến độ | editable-table | Inline-edit: Tên mốc / Ngày dự kiến / Ngày thực tế / Trạng thái mốc (CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH). [+ Thêm mốc] | inline-edit | trang thêm/sửa — chỉ CB NV |
```
> Dòng này khai đủ ba thứ cột K hỏi: nút `[+ Thêm mốc]`, kiểu bảng **sửa tại chỗ**, và **đúng 4 trường** trên dòng.

**`srs-fr-14-hop-dong-tv.md:96`**–**`:102`** (Inputs — Mốc tiến độ, **trọn bảng**)
```
| # | Tên field | Kiểu logic | Bắt buộc | Ràng buộc | Mặc định | Nguồn |
|---|----------|-----------|----------|-----------|----------|-------|
| 1 | hop_dong_id | identifier | Y | FK -> HOP_DONG_TU_VAN | — | hệ thống |
| 2 | ten_moc | text | Y | — | — | người dùng nhập |
| 3 | ngay_du_kien | date | Y | — | — | người dùng chọn |
| 4 | ngay_thuc_te | date | N | — | — | người dùng chọn |
| 5 | trang_thai_moc | text | Y | CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH | CHUA_BAT_DAU | người dùng chọn |
```
> `ngay_thuc_te` cột **Bắt buộc = N** ⇒ khớp đúng chữ "(tùy chọn)" của đối tác. `hop_dong_id` là trường hệ thống, **không** hiện trên dòng nhập ⇒ 4 mục người dùng nhập, đúng như cột K liệt kê.

**`srs-fr-14-hop-dong-tv.md:279`** (bố cục — nguồn của cách đánh "Nhóm 3")
```
**Form thêm/sửa:** Trang mới với Accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký.
```

**`srs-fr-14-hop-dong-tv.md:122`** (Processing — mốc tiến độ được lưu cùng hợp đồng)
```
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
```

**`srs-fr-14-hop-dong-tv.md:181`** (Acceptance Criteria)
```
- **Given** CB NV thêm mốc tiến độ **When** nhập thông tin **Then** lưu mốc + ngày dự kiến
```

**`srs-fr-14-hop-dong-tv.md:394`** (cách lưu — bối cảnh)
```
| moc_tien_do | text (long) | N | | | Mốc tiến độ (JSON array) |
```

**`srs-fr-05-vu-viec.md:1492`** (nhãn trạng thái mốc phải là tiếng Việt, không phải mã DB)
```
Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt theo bảng dưới. Mã DB **không bao giờ** xuất hiện trên giao diện người dùng.
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:292` ("trang thêm/sửa — **chỉ CB NV**"), `:68`, `:118` (TVV/CG chặn mọi thao tác Create/Update) | `:68`, `:118`, `:292` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Màn đo** | **Biểu mẫu thêm/sửa hợp đồng**, Nhóm 3 — `:292` chỉ khai nút `[+ Thêm mốc]` cho **trang thêm/sửa**. Trên trang chỉ-xem sẽ không có nút; ghi rõ đã đo trên màn nào | `:292` |
| **Dữ liệu** | **1 hợp đồng bất kỳ đang mở được ở chế độ sửa.** Bảng mốc có thể đang rỗng — vẫn đo được (số dòng 0 → 1). Ưu tiên dùng lại hợp đồng đã dựng ở `_15`, **không tạo mới** | `:292` |
| **Không cần lưu** | Cột K dừng ở "thêm một dòng trống … nhập trực tiếp trên dòng" ⇒ **không bắt buộc bấm Lưu**. Nếu đã gõ thử, bấm Hủy để không đổi dữ liệu; nếu buộc phải lưu để đo được thì khai rõ vào báo cáo | bước J của phiếu |
| **Ghi mốc so trước khi bấm** | Ghi **số dòng bảng mốc trước khi bấm** — mốc so cho C1 | `:292` |

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bấm nút, bảng có thêm dòng → kết luận đạt.** C1 còn đòi **dòng trống** và **nhập trực tiếp trên dòng**. Nếu bấm nút mở ra một hộp thoại nhập riêng thay vì thêm dòng vào bảng, thì **không** đúng "editable-table / inline-edit" ở `:292` ⇒ C1 **Fail**. Đây là điểm dễ bỏ qua nhất.
- **Dòng mới có sẵn dữ liệu (sao chép dòng trước).** Cột K nói "dòng **trống**". Phải đọc `value` từng ô, không nhìn lướt.
- **Không gõ thử.** Thấy ô có viền nhập chưa chứng minh sửa được tại chỗ — flow 04 cấm Pass bằng quan sát tĩnh khi vế là hành động. Phải gõ thử vào ô Tên mốc.
- **Đếm gộp thẻ bọc ngoài với thẻ con** → số dòng nhân đôi, không phát hiện được tăng đúng 1.
- **Trạng thái mốc hiển thị mã DB.** Cột này có enum `CHUA_BAT_DAU / DANG_THUC_HIEN / HOAN_THANH` (`:102`, `:292`). Nếu ô chọn hiện thẳng mã DB thì vi phạm `srs-fr-05-vu-viec.md:1492` — nhưng cột K của phiếu này **không** chấm nhãn; ghi nhận theo gate "bug mới tự lộ", **không** đổi verdict vế C2.

**Dễ Fail oan:**
- **Fail vì dòng mới không có sẵn giá trị Trạng thái mốc.** `:102` ghi Mặc định `CHUA_BAT_DAU` — nhưng cột K đòi **dòng trống**. Hai điều này lệch nhau; ô Trạng thái có sẵn giá trị mặc định là **đúng** đặc tả ⇒ **không Fail** C1 vì lý do đó.
- **Fail vì thiếu trường `hop_dong_id`.** `:98` ghi Nguồn = **hệ thống** ⇒ không hiện trên dòng nhập.
- **Fail vì bảng mốc không có nút xoá dòng.** Cột K không nhắc ⇒ không thành tiêu chí chấm (và đặc tả cũng không khai).
- **Fail vì bấm Thêm mốc mà chưa lưu thì mất dòng khi rời màn.** Đặc tả không khai thời điểm ghi xuống; `:122` cho biết mốc được lưu **cùng** bản ghi hợp đồng ⇒ mất khi chưa lưu là hợp lý.
- **Fail vì nhãn nút không phải "Thêm mốc".** `:292` ghi `[+ Thêm mốc]`; Phụ lục E §H4 (`srs-v3.5.md:6756`) lại bắt nút thêm mới luôn là "Thêm mới". Cột K chấm **hành vi thêm dòng**, không chấm nhãn nút.
- **Fail vì không kiểm tra Ngày dự kiến ≤ Ngày thực tế.** Đặc tả **không** khai ràng buộc nào giữa hai ngày này (`:100`, `:101` đều để trống cột Ràng buộc).
