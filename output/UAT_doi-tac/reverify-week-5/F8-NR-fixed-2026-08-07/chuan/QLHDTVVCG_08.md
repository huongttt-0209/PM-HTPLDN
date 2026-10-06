# QLHDTVVCG_08 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 314 · **Mô tả (G):** Biểu mẫu chi tiết — **Nhóm 1: Thông tin chung**
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn Xem chi tiết
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01) + §2 Inputs/Outputs FR-X.3-01
**Kiểm chéo:** `srs-fr-05-vu-viec.md` §3.A–G · `srs-v3.5.md` Phụ lục E §H

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống hiển thị các trường thông tin giống với thiết kế" — hiểu ở mức **đủ các trường đặc tả khai cho Nhóm 1 (Thông tin chung)** | `srs-fr-14-hop-dong-tv.md:279`, `:290` + bảng Inputs `:81`–`:92` | **MATCH** | TEST | **UI:** mở chi tiết 1 hợp đồng → nhóm "Thông tin chung", đọc `innerText` nhãn từng trường, đối chiếu 10 mục ở `:290` (Mã / Tên / Bên A / Bên B / Giá trị / Thời hạn bắt đầu / Thời hạn kết thúc / Nội dung / Ghi chú / File đính kèm). **Đối chứng:** gọi API đọc chính bản ghi đó, so từng giá trị trả về với chuỗi đang hiển thị |
| **C2** | "…giống với **thiết kế**" ở mức chi tiết ngoài danh sách trường (bố cục, thứ tự, khoảng cách, kiểu control) | `srs-fr-14-hop-dong-tv.md:274` → trỏ ra `dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1`, **tài liệu này KHÔNG có trong nguồn chuẩn** ⇒ **IM LẶNG** | **GAP** | **BA** | Chỉ chụp hiện trạng để mô tả cho BA. **CẤM Pass/Reopen vế này** |
| **C3** | "Dữ liệu hiển thị đúng định dạng và trường thông tin" | `srs-fr-14-hop-dong-tv.md:290` (ràng buộc bắt buộc / `>= bắt đầu`) + `:151`–`:153` (định dạng tiền VND, `dd/mm/yyyy`) + `srs-fr-05-vu-viec.md:1492` | **MATCH** | TEST | **UI:** trên bản ghi có đủ dữ liệu, đọc `innerText`: Giá trị = định dạng tiền VND, hai mốc Thời hạn = `dd/mm/yyyy`, không có mã DB. **Đối chứng:** so với giá trị thô trong response API của cùng bản ghi |
| **C4** | "Dữ liệu hiển thị không bị tràn/đè lên nhau" | `srs-v3.5.md:6755` (§H3 — khoảng cách dòng trang chi tiết) + `srs-fr-05-vu-viec.md:1603` (§F ≥1024×768). Đặc tả **IM LẶNG** về tràn/đè bố cục biểu mẫu | **GAP** | **BA** | Chỉ chụp hiện trạng ở 1440×900. **CẤM Pass/Reopen** |
| **C5** | "…đồng nhất ngôn ngữ hiển thị" | `srs-fr-05-vu-viec.md:1492` + `:1484` | **MATCH** | TEST | **UI:** đọc `innerText` toàn bộ nhãn trường + giá trị Trạng thái trong nhóm này, khẳng định không có mã DB (`DANG_THUC_HIEN`…) và không lẫn tiếng Anh. **Đối chứng:** giá trị thô trong API phải là mã DB → chứng minh có lớp dịch nhãn |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:272`** (loại màn hình SCR-X3-01)
```
**Loai man hinh:** Danh sach + Form (trang moi/modal/drawer) + Accordion
```

**`srs-fr-14-hop-dong-tv.md:274`**
```
**UX-Spec ref:** dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1
```
> ⚠️ Đã `find` toàn repo lượt này: **không tồn tại** tệp này ⇒ "thiết kế" không có trong nguồn chuẩn ⇒ C2 khóa `GAP`.

**`srs-fr-14-hop-dong-tv.md:279`** (bố cục biểu mẫu — nguồn của cách đánh "Nhóm 1..4" trong phiếu)
```
**Form thêm/sửa:** Trang mới với Accordion: Thông tin chung / Vụ việc liên kết / Mốc tiến độ / Thanh toán giai đoạn / Nhật ký.
```

**`srs-fr-14-hop-dong-tv.md:290`** (thành phần Nhóm 1 — **danh sách trường duy nhất đặc tả khai**)
```
| 6 | content (form) | Thông tin chung | form | Mã (auto) / Tên (bắt buộc) / Bên A (auto đơn vị) / Bên B (bắt buộc + TVV dropdown) / Giá trị (bắt buộc) / Thời hạn bắt đầu (bắt buộc) / Thời hạn kết thúc (bắt buộc, >= bắt đầu) / Nội dung / Ghi chú / File đính kèm | input -> validate | trang thêm/sửa — **CHỈ vai trò CB NV; TVV/CG không truy cập trang form** |
```

**`srs-fr-14-hop-dong-tv.md:81`–`:92`** (Inputs FR-X.3-01 — trọn bảng Thêm mới/Chỉnh sửa, 12 dòng)
```
| 1 | ma_hop_dong | text | Y (auto) | Format: HDTV-{YYYYMMDD}-{SEQ} | auto-gen | hệ thống |
| 2 | ten_hop_dong | text | Y | — | — | người dùng nhập |
| 3 | ben_a | text | Y | Bên A (đơn vị quản lý) | auto đơn vị | hệ thống |
| 4 | ben_b | text | Y | Bên B (TVV/Tổ chức tư vấn/Chuyên gia) | — | người dùng nhập |
| 5 | tvv_id | identifier | N | FK -> TU_VAN_VIEN (liên kết nếu có; có thể trỏ đến TVV hoặc CG, xác định qua TU_VAN_VIEN.loai_tvv) | — | người dùng chọn |
| 6 | gia_tri_hop_dong | money | Y | Giá trị HĐ | — | người dùng nhập |
| 7 | thoi_han_bat_dau | date | Y | — | — | người dùng chọn |
| 8 | thoi_han_ket_thuc | date | Y | >= thoi_han_bat_dau | — | người dùng chọn |
| 9 | noi_dung | text (long) | N | Nội dung tóm tắt HĐ | — | người dùng nhập |
| 10 | vu_viec_ids | identifier[] | N | FK[] -> VU_VIEC (many-to-many) | — | người dùng chọn |
| 11 | ghi_chu | text (long) | N | — | — | người dùng nhập |
| 12 | file_dinh_kem | file[] | N | Upload nhiều file | — | người dùng upload |
```

**`srs-fr-14-hop-dong-tv.md:151`–`:153`** (Outputs FR-X.3-01 — định dạng)
```
| 5 | gia_tri_hop_dong | money | luôn | format tiền VND |
| 6 | thoi_han_bat_dau | date | luôn | dd/mm/yyyy |
| 7 | thoi_han_ket_thuc | date | luôn | dd/mm/yyyy |
```

**`srs-fr-14-hop-dong-tv.md:294`**–**`:295`** (hai dòng duy nhất nhắc tới **trang xem chi tiết**)
```
| 10 | content (form) | Accordion: Nhật ký | timeline | Lịch sử CUD, mốc, thanh toán, liên kết VV | — | trang thêm/sửa (CB NV) hoặc xem chi tiết (TVV/CG xem được lịch sử của HĐ thuộc về mình) |
| 11 | action-bar | Thanh hành động | button-group | [Hủy] [Lưu] -- KHÔNG cần phê duyệt | click -> action | trang thêm/sửa — chỉ CB NV; TVV/CG ở trang xem chi tiết chỉ thấy nút [Đóng] |
```
> ⚠️ Đặc tả **không có bảng thành phần riêng cho trang "xem chi tiết"** — chỉ khai bảng cho **trang thêm/sửa**. Xem mục (d).

**`srs-v3.5.md:6755`** (Phụ lục E §H3)
```
| **H3** | Style trang chi tiết theo phong cách "Hỏi đáp pháp lý" | Trang Chi tiết bản ghi (SCR-XX-02) áp khoảng cách dòng compact giống mục "Thông tin kế hoạch" trong "Đánh giá hiệu quả". Tránh khoảng cách dòng rộng kiểu form. | BẮT BUỘC |
```

**`srs-fr-05-vu-viec.md:1492`**
```
Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt theo bảng dưới. Mã DB **không bao giờ** xuất hiện trên giao diện người dùng.
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)**. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `srs-fr-14-hop-dong-tv.md:68` (CB NV — CRUD đầy đủ) và `:290` ("**CHỈ vai trò CB NV; TVV/CG không truy cập trang form**"). Đo bằng TVV/CG sẽ không vào được nhóm này ⇒ Fail oan | `:68`, `:290` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu** | **≥1 hợp đồng có ĐỦ dữ liệu ở cả 10 trường** của `:290` — đặc biệt các trường **không bắt buộc** (Nội dung, Ghi chú, File đính kèm) phải có giá trị, nếu không thì C3 chỉ đo được phần bắt buộc. Không có bản ghi đủ chất ⇒ được seed 1 hợp đồng "đầy đủ trường" (khai rõ: bản ghi nào · đổi gì · env nào) | `:290`, `:81`–`:92` |
| **Màn đo** | Mở đúng màn mà bước J dẫn tới ("Xem chi tiết"). Ghi rõ vào báo cáo đây là **trang xem chi tiết** hay **trang thêm/sửa** — đặc tả chỉ khai bảng thành phần cho trang thêm/sửa (`:290`), nên phải nói rõ đã đo trên màn nào | `:290`, `:294`, `:295` |
| **Viewport** | 1440×900 | brief §3 |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bản ghi nghèo dữ liệu.** Các trường Nội dung / Ghi chú / File đính kèm là **không bắt buộc** (`:89`, `:91`, `:92`). Bản ghi để trống ba trường này thì màn trông "đủ" nhưng **chưa chứng minh** trường hiển thị đúng dữ liệu. Đây là lý do tiền đề đòi bản ghi đầy đủ.
- **Nhìn nhãn trường, không nhìn giá trị.** C1 chấm **có trường**, C3 chấm **giá trị đúng định dạng** — hai vế khác nhau. Có nhãn "Giá trị" mà ô trống hoặc in số thô `50000000` không có định dạng tiền thì C1 đạt nhưng C3 **Fail**.
- **Đo trên trang Sửa rồi kết luận cho trang Xem chi tiết.** Bước J của phiếu là "Xem chi tiết". Nếu thực tế bấm vào Sửa để xem cho tiện thì đang đo màn khác — ghi rõ đã đo màn nào; đặc tả có phân biệt hai màn ở `:294`–`:295`.
- **Đọc bằng `textContent`** → gom node ẩn của AntD, thấy nhãn không thật sự hiển thị. Dùng `innerText`.

**Dễ Fail oan:**
- **Fail vì màn thiếu trường mà đặc tả không khai cho màn đó.** Đặc tả **chỉ có bảng thành phần cho trang thêm/sửa** (`:290`); **không** có bảng nào khai trang "xem chi tiết". Nếu trang xem chi tiết hiển thị ít trường hơn trang sửa, đó là chỗ đặc tả im lặng ⇒ **không Fail**, đưa vào câu hỏi BA gộp.
- **Fail vì màn có thêm trường ngoài `:290`.** Chính đặc tả còn khai thêm `so_hop_dong` và `ngay_ky` ở phần thực thể (`:385`, `:390`) mà **không** liệt kê ở `:290`; bản chính `srs-v3.5.md:2306` còn có `to_chuc_tu_van_id` mà `srs-fr-14` không có. Thừa trường ⇒ ghi nhận cho BA, **không Fail**.
- **Fail vì chấm theo bản vẽ Figma / ảnh đối tác.** Bản vẽ `MH-14.1` không có trong nguồn chuẩn — đây chính là lý do C2 khóa `GAP`.
- **Fail vì Bên A / Mã hợp đồng không sửa được.** `:81` và `:83` ghi Nguồn = **hệ thống** ⇒ hai trường này vốn không do người dùng nhập; khoá chúng là **đúng** đặc tả.
- **Fail vì nút không phải [Lưu]/[Hủy].** `:295` khai `[Hủy] [Lưu]` cho trang thêm/sửa, `[Đóng]` cho trang xem chi tiết của TVV/CG. Phiếu này không chấm nút ⇒ không Fail vì nút.
