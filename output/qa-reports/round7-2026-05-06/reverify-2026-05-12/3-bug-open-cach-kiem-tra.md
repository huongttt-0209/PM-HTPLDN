# Hướng dẫn kiểm tra 3 bug đang Open — R23-reverify

**Ngày:** 2026-05-14 02:15:00
**Mục đích:** Hướng dẫn người dùng cuối kiểm tra lại 3 bug trên web không cần thao tác kỹ thuật.

**Thông tin chung:**
- URL: http://103.172.236.130:3000/
- OTP login: gõ `666666` (dev bypass)
- File bug-report gốc nằm trong `bug-reports/danh-gia/` và `bug-reports/vu-viec/`

---

## Bug 1 — BUG-FUNC-DG-013

### Thông tin nhanh

| Trường | Giá trị |
|---|---|
| Module | **Đánh giá hiệu quả HTPL** |
| Màn hình | Danh sách kế hoạch đánh giá → Detail kế hoạch + tab Báo cáo + tab Kết quả |
| Severity hiện tại | **Minor P3** (đã downgrade từ Major P1) |
| Trạng thái | Open — chỉ còn lỗi nhỏ về **mã lỗi sai** (error code wording) |

### Bug là gì (dễ hiểu)

- Cán bộ thuộc cơ quan KHÁC cơ quan được đánh giá → mở kế hoạch đánh giá → web báo "Đơn vị không nằm trong phạm vi truy cập".
- Spec yêu cầu báo: "Bạn không có quyền xem kết quả đánh giá này" (mã `ERR-DG-10`).
- Cán bộ vẫn bị chặn đúng (không xem được), chỉ là **câu thông báo sai**. Không ảnh hưởng nghiệp vụ.

### Cách kiểm tra trên web

**Account cần dùng:** `cb_nv_dp_02` / `Secret@123` (cán bộ Sở Tư pháp Bắc Giang — KHÁC cơ quan được đánh giá An Giang).

1. Mở `http://103.172.236.130:3000/login` → đăng nhập `cb_nv_dp_02` + OTP `666666`.
2. Vào menu **"Đánh giá hiệu quả HTPL"** → **"Quản lý kế hoạch đánh giá"**.
3. Trên thanh URL gõ trực tiếp: `http://103.172.236.130:3000/danh-gia/ke-hoach/440b6dd1-d086-41d6-a842-45d2a323c94a` (kế hoạch DG-20260513-0001 của Sở Tư pháp An Giang).
4. **Quan sát thông báo lỗi popup hiện ra**.

### Kết quả thấy được

- ❌ Web hiện: **"Đơn vị không nằm trong phạm vi truy cập của bạn"** → SAI spec
- ✅ Spec yêu cầu: **"Bạn không có quyền xem kết quả đánh giá này"** (mã `ERR-DG-10`)

### Khi nào coi là FIXED

- Cán bộ Sở khác mở kế hoạch của Sở An Giang → web hiện đúng câu **"Bạn không có quyền xem kết quả đánh giá này"** (mã ERR-DG-10).

---

## Bug 2 — BUG-VV-PC-WRN-01

### Thông tin nhanh

| Trường | Giá trị |
|---|---|
| Module | **Quản lý Vụ việc HTPL** |
| Màn hình | Detail vụ việc → Modal **"Phân công tư vấn viên"** |
| Severity | **Minor P2** |
| Trạng thái | Open — chờ dev quyết cách cho phép tìm TVV ngoài lĩnh vực |

### Bug là gì (dễ hiểu)

- Cán bộ nghiệp vụ tạo 1 vụ việc thuộc lĩnh vực **"Doanh nghiệp"** → bấm Phân công → tìm tư vấn viên.
- Hệ thống chỉ hiện TVV có lĩnh vực **"Doanh nghiệp"** (5 người).
- Nếu không có TVV nào phù hợp, web hiện popup **"Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT"** → cán bộ bị kẹt.
- Spec yêu cầu cho cán bộ một **cách để tìm tư vấn viên thuộc lĩnh vực khác** (vd nút "Tìm thủ công", hoặc bỏ filter lĩnh vực).
- Hiện tại web không có nút nào để vượt qua tình huống này → vụ việc đó không phân công được.

### Cách kiểm tra trên web

**Account cần dùng:** `cb_nv_tw_01` / `Secret@123` (cán bộ Trung ương — có quyền phân công).

1. Login `cb_nv_tw_01` + OTP `666666`.
2. Sidebar → **"Quản lý vụ việc HTPL"** → danh sách vụ việc.
3. Tìm 1 vụ việc thuộc lĩnh vực **"Doanh nghiệp"** state **"Đang kiểm tra"** (vd `VV-QA-R7-PRIVACY-DNAG002`). Nếu không có, dùng cách dưới đây tạo mới:
   - Click **[Tạo vụ việc mới]** → fill: Doanh nghiệp = bất kỳ, Lĩnh vực = **Doanh nghiệp**, Loại hình = Tư vấn pháp luật → Lưu.
   - Mở detail vụ việc vừa tạo → click **[Kiểm tra hồ sơ]** → **[Xác nhận]** (state chuyển sang "Đang kiểm tra").
4. Click nút **[Phân công]** ở thanh action bar → modal "Phân công tư vấn viên" mở.
5. Click dropdown **"Chọn tư vấn viên"** → quan sát danh sách.
6. Gõ vào ô search trong dropdown: `XXKHONGMATCH99` (chuỗi bừa để force empty).

### Kết quả thấy được

- Empty state hiện text: **"Trống / Không tìm thấy đối tượng phù hợp lĩnh vực / Liên hệ QTHT để mở rộng lĩnh vực TVV/NHT, hoặc chọn vụ việc khác"**.
- ❌ **KHÔNG có nút [Tìm thủ công]** hoặc nút bỏ filter lĩnh vực.
- ❌ Gõ tên TVV thật ở lĩnh vực khác (vd `hương`) → vẫn 0 kết quả (dù TVV "hương tvv1" tồn tại trong hệ thống).

### Khi nào coi là FIXED

- Modal phân công có thêm 1 trong các cơ chế: nút **[Tìm thủ công]**, hoặc **toggle bỏ filter lĩnh vực**, hoặc **dropdown thứ 2 không lọc lĩnh vực**.
- Cán bộ chọn được TVV thuộc lĩnh vực khác.

---

## Bug 3 — BUG-VV-FN-LICHSU-01

### Thông tin nhanh

| Trường | Giá trị |
|---|---|
| Module | **Quản lý Vụ việc HTPL** |
| Màn hình | Detail vụ việc → tab **"Dòng thời gian"** (hoặc accordion "Lịch sử hành động") |
| Severity | **Minor P3** (đã downgrade) |
| Trạng thái | Open — chờ dev BE bổ sung 5 enum hành động còn thiếu |

### Bug là gì (dễ hiểu)

- Mỗi vụ việc có 1 tab "Dòng thời gian" hiện lịch sử các hành động (ai làm gì, lúc nào).
- Spec yêu cầu hệ thống ghi **18 loại hành động** riêng biệt (Tạo mới, Tiếp nhận, Kiểm tra, Yêu cầu bổ sung, Phân công, Phê duyệt, Hoàn thành, Đánh giá, …).
- Hiện tại hệ thống **chỉ ghi 13/18 loại**. 5 loại bị bỏ qua: Yêu cầu bổ sung, Bổ sung hồ sơ, Từ chối phê duyệt, Mở lại, Tự động từ chối quá hạn.
- Ngoài ra 4 vụ việc cũ vẫn dùng tên hành động cũ (`CREATE` thay vì `TAO_VV`, `UPDATE` thay vì `KIEM_TRA`, …).
- Hậu quả: người dùng xem timeline 1 vụ việc đã "Yêu cầu bổ sung" → không thấy entry "Yêu cầu bổ sung" trong lịch sử → không biết ai/khi nào yêu cầu.

### Cách kiểm tra trên web

**Account cần dùng:** `cb_nv_tw_03` / `Secret@123`.

1. Login `cb_nv_tw_03` + OTP `666666`.
2. Sidebar → **"Quản lý vụ việc HTPL"**.
3. Tìm 1 vụ việc state **"Yêu cầu bổ sung"** trong danh sách (filter cột trạng thái). Nếu không có, mở `VV-002` (trạng thái Yêu cầu bổ sung — UUID `aad90003-0000-4000-8000-000000000001`).
4. Click row → mở detail vụ việc.
5. Click tab **"Dòng thời gian"** (cuối trang, dạng accordion hoặc tab).
6. Quan sát danh sách hành động trong timeline.

### Kết quả thấy được

- Timeline chỉ hiện các loại hành động: **"Tạo mới"**, **"Cập nhật"** (hoặc "Kiểm tra" cho vụ việc mới).
- ❌ **KHÔNG có entry "Yêu cầu bổ sung"** dù trạng thái vụ việc đã là "Yêu cầu bổ sung".
- Vụ việc trạng thái "Từ chối" → không có entry "Từ chối".
- Vụ việc cũ vẫn hiện "Tạo mới" / "Cập nhật" generic thay vì tên hành động cụ thể.

### Khi nào coi là FIXED

- Mở vụ việc trạng thái "Yêu cầu bổ sung" → timeline có entry **"Yêu cầu bổ sung"** kèm tên người + thời gian.
- Test 5 loại hành động còn thiếu: Yêu cầu bổ sung / Bổ sung hồ sơ / Từ chối phê duyệt / Mở lại / Tự động từ chối quá hạn → đều có entry riêng.

---

## Tóm tắt

| Bug | Module | Màn hình | Account | Bước nhanh |
|---|---|---|---|---|
| BUG-FUNC-DG-013 | Đánh giá HQ | Detail kế hoạch đánh giá | `cb_nv_dp_02` | Mở URL kế hoạch của Sở khác → đọc câu lỗi |
| BUG-VV-PC-WRN-01 | Vụ việc | Modal Phân công TVV | `cb_nv_tw_01` | Mở VV LV Doanh nghiệp → Phân công → search bừa → xem có nút override không |
| BUG-VV-FN-LICHSU-01 | Vụ việc | Tab Dòng thời gian | `cb_nv_tw_03` | Mở VV trạng thái "Yêu cầu bổ sung" → xem timeline thiếu entry |

**Tất cả 3 bug đều là Minor**, không block nghiệp vụ chính — chỉ là chi tiết wording / UX / audit log thiếu. Dev fix xong sẽ retest.
