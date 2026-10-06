# QLHDTVVCG_19 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 325 · **Mô tả (G):** Kiểm tra khi nhấn nút chức năng Sửa
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "Sửa"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — §3 SCR-X3-01 + Inputs/Processing FR-X.3-01

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống mở màn hình biểu mẫu ở chế độ "Chi tiết" **cho phép chỉnh sửa**" | `srs-fr-14-hop-dong-tv.md:288` (hành động Sửa), `:279`, `:290`, `:295` (`[Hủy] [Lưu]`) | **MATCH** | TEST | **UI:** bấm Sửa trên 1 hợp đồng → biểu mẫu mở ra **đã nạp sẵn dữ liệu bản ghi đó** và các ô nhập **không bị khoá** (thử gõ vào ô Tên, ký tự phải nhận). **Đối chứng:** `list_network_requests` — có request đọc **đúng định danh** bản ghi vừa bấm |
| **C2** | "…**giữ nguyên mã hợp đồng**" | `srs-fr-14-hop-dong-tv.md:119` (sinh mã **chỉ ở Thêm mới**) + `:81` (Nguồn `hệ thống`) + `:384` (`UNIQUE`) | **MATCH** | TEST | **UI:** so mã hợp đồng hiển thị trên biểu mẫu Sửa với mã trên dòng danh sách vừa bấm — phải trùng khớp; ô Mã không cho sửa. **Đối chứng:** đọc `ma_hop_dong` của bản ghi qua API, so với chuỗi đang hiển thị |
| **C3** | "…và **Bên A**" (giữ nguyên) | `srs-fr-14-hop-dong-tv.md:83` (Mặc định `auto đơn vị`, Nguồn `hệ thống`) + `:290` ("Bên A (auto đơn vị)") | **MATCH** | TEST | **UI:** so Bên A trên biểu mẫu Sửa với Bên A trên dòng danh sách — phải trùng; ô không do người dùng nhập. **Đối chứng:** đọc `ben_a` của bản ghi qua API, so với chuỗi đang hiển thị |

> Cột K **không nhắc** tới việc lưu, tới các nhóm 2/3/4, hay tới thông báo ⇒ **không tách thành vế** ở phiếu này (hành vi lưu thuộc `_21`).

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:288`** (nút Sửa nằm ở cột Hành động)
```
| 4 | content | Bảng hợp đồng | table | Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu <= 30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động (CB NV thấy Xem/Sửa/Xóa; TVV/CG CHỈ thấy nút Xem) | click -> action | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:279`**
```
**Form thêm/sửa:** Trang mới với Accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký.
```

**`srs-fr-14-hop-dong-tv.md:290`**
```
| 6 | content (form) | Thông tin chung | form | Mã (auto) / Tên (bắt buộc) / Bên A (auto đơn vị) / Bên B (bắt buộc + TVV dropdown) / Giá trị (bắt buộc) / Thời hạn bắt đầu (bắt buộc) / Thời hạn kết thúc (bắt buộc, >= bắt đầu) / Nội dung / Ghi chú / File đính kèm | input -> validate | trang thêm/sửa — **CHỈ vai trò CB NV; TVV/CG không truy cập trang form** |
```

**`srs-fr-14-hop-dong-tv.md:295`** (thanh hành động của biểu mẫu — bằng chứng "cho phép chỉnh sửa")
```
| 11 | action-bar | Thanh hành động | button-group | [Hủy] [Lưu] -- KHÔNG cần phê duyệt | click -> action | trang thêm/sửa — chỉ CB NV; TVV/CG ở trang xem chi tiết chỉ thấy nút [Đóng] |
```

**`srs-fr-14-hop-dong-tv.md:119`** (Processing bước 2 — **chỉ Thêm mới mới sinh mã** ⇒ Sửa giữ nguyên mã)
```
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
```

**`srs-fr-14-hop-dong-tv.md:81`** + **`:83`** (Inputs — hai trường do hệ thống quản)
```
| 1 | ma_hop_dong | text | Y (auto) | Format: HDTV-{YYYYMMDD}-{SEQ} | auto-gen | hệ thống |
| 3 | ben_a | text | Y | Bên A (đơn vị quản lý) | auto đơn vị | hệ thống |
```

**`srs-fr-14-hop-dong-tv.md:384`** (thực thể — ràng buộc mã)
```
| ma_hop_dong | text | Y | UNIQUE | Auto-gen | Mã HĐ |
```

**`srs-fr-14-hop-dong-tv.md:118`** (ai được sửa)
```
| 1 | Kiểm tra quyền. CB NV: áp phân quyền đơn vị (BR-AUTH-08). TVV/CG: chỉ trả HĐ có `tu_van_vien_id` thuộc về user đang đăng nhập; chặn mọi thao tác Create/Update/Delete | BR-AUTH-01, BR-AUTH-08 |
```

**`srs-fr-14-hop-dong-tv.md:272`** (hình thức biểu mẫu — cho phép nhiều dạng)
```
**Loai man hinh:** Danh sach + Form (trang moi/modal/drawer) + Accordion
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68` (CB NV — CRUD đầy đủ), `:118` (TVV/CG **chặn mọi thao tác Update**), `:288` (chỉ CB NV thấy nút Sửa), `:290` (chỉ CB NV vào trang biểu mẫu) | `:68`, `:118`, `:288`, `:290` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu** | **≥1 hợp đồng** trong phạm vi đơn vị. Nên chọn bản ghi **có dữ liệu ở nhiều trường** để thấy rõ biểu mẫu đã nạp đúng bản ghi (C1) | `:290` |
| **Ghi lại đối chứng trước khi bấm** | Ghi **mã hợp đồng** và **Bên A** đọc từ dòng danh sách **trước khi** bấm Sửa — đây là mốc so cho C2/C3. Không có mốc so thì hai vế này chỉ còn là quan sát tĩnh | `:288` |
| **Không được lưu** | Phiếu này **dừng ở bước mở biểu mẫu**. **KHÔNG bấm Lưu** — hành vi lưu thuộc `_21`. Nếu đã gõ thử vào ô Tên để kiểm C1 thì **bấm Hủy** để không đổi dữ liệu | bước J của phiếu |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Biểu mẫu mở ra nhưng nạp sai bản ghi.** Nếu biểu mẫu hiện dữ liệu của hợp đồng khác (hoặc dữ liệu còn sót của lần mở trước), C1 vẫn "trông đạt". Bắt buộc đối chứng: request đọc phải trỏ **đúng định danh** của dòng vừa bấm.
- **"Cho phép chỉnh sửa" chấm bằng mắt.** Thấy ô có viền nhập không đủ — ô có thể ở trạng thái chỉ đọc. Phải **gõ thử** vào một ô (rồi Hủy) để chứng minh nhận ký tự. Đây là điểm flow 04 cấm Pass bằng quan sát tĩnh.
- **Mã hợp đồng "giữ nguyên" vì màn hiển thị lại chuỗi cũ trong khi dữ liệu đã đổi.** Ở phiếu này chưa lưu nên rủi ro thấp, nhưng vẫn phải đối chứng `ma_hop_dong` qua API.
- **Bên A trùng vì cả hai màn đều lấy từ đơn vị của tài khoản đăng nhập, chứ không phải từ bản ghi.** Nếu hợp đồng thuộc đơn vị khác với tài khoản đang dùng thì mới phân biệt được — nhưng chỉ dựng được ca này ở tài khoản TW. Nếu không phân biệt được, ghi rõ giới hạn của phép đo.

**Dễ Fail oan:**
- **Fail vì màn không mang nhãn "Chi tiết".** Đặc tả gọi màn này là **"trang thêm/sửa"** (`:290`, `:295`), không dùng chữ "Chi tiết". Cột K chấm **hành vi** (mở biểu mẫu cho phép chỉnh sửa), không chấm tên chế độ ⇒ không Fail vì nhãn.
- **Fail vì mở ra ngăn kéo/hộp thoại chứ không phải trang mới.** `:272` cho phép cả ba dạng.
- **Fail vì ô Mã hợp đồng và Bên A bị khoá không sửa được.** Đó chính là **yêu cầu**: `:81` và `:83` ghi Nguồn = **hệ thống**. Khoá là đúng.
- **Fail vì thiếu trường `so_hop_dong` / `ngay_ky`.** Hai trường có ở phần thực thể (`:385`, `:390`) nhưng không nằm trong danh sách `:290` ⇒ ghi nhận cho BA, không Fail.
- **Fail vì biểu mẫu Sửa không có bước phê duyệt.** `:302` và `:462` ghi rõ nhóm X.3 **KHÔNG cần phê duyệt, chỉ CRUD thuần**.
