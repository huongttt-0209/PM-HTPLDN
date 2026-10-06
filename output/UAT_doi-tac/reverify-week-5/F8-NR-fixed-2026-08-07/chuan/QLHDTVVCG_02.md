# QLHDTVVCG_02 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 308 · **Mô tả (G):** Điều kiện tìm kiếm / bộ lọc · **Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn"
**Trạng thái (N):** `N/R` — phiếu đối tác **chưa từng chạy**, `Kết quả thực tế` RỖNG, không ảnh
⇒ **expected đối tác = nguyên văn cột `Kết quả mong đợi` (K)**, không có triệu chứng cũ.

**Nguồn chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-14-hop-dong-tv.md` (536 dòng, tự mở đếm lượt này)
**Kiểm chéo:** `srs-fr-05-vu-viec.md` §3.A–G (quy ước UI chung, áp toàn hệ thống) · `srs-v3.5.md` Phụ lục E §H

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống hiển thị các trường thông tin giống với thiết kế" — hiểu ở mức **đủ các thành phần đặc tả khai cho phần danh sách** | `srs-fr-14-hop-dong-tv.md:278`, `:285`, `:286`, `:287`, `:288`, `:289` | **MATCH** | TEST | **UI:** mở màn danh sách HĐ tư vấn, đối chiếu 5 vùng đặc tả khai (breadcrumb / tiêu đề + 3 nút / thanh lọc 3 nhóm / bảng 10 cột / phân trang 20 mục). **Đối chứng:** `evaluate_script` đếm số `<th>` của bảng + đọc `innerText` từng tiêu đề cột, so với danh sách cột ở `:288` |
| **C2** | "…giống với **thiết kế**" ở mức chi tiết ngoài bảng thành phần (bố cục, thứ tự, khoảng cách, kiểu control cụ thể) | `srs-fr-14-hop-dong-tv.md:274` → trỏ ra `dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1`, **tài liệu này KHÔNG có trong nguồn chuẩn** ⇒ **IM LẶNG** | **GAP** | **BA** | Chỉ đo hiện trạng để mô tả cho BA (ảnh màn hình). **CẤM Pass/Reopen vế này** |
| **C3** | "Dữ liệu hiển thị đúng định dạng và trường thông tin" | `srs-fr-14-hop-dong-tv.md:288` + Outputs `:147`–`:155` + `srs-fr-05-vu-viec.md:1492` | **MATCH** | TEST | **UI:** trên ≥1 dòng có đủ dữ liệu, đọc `innerText` các ô: Giá trị = định dạng tiền VND, Thời hạn = `dd/mm/yyyy`, Số VV = badge số, Tiến độ TT = %, Thời hạn kết thúc ≤30 ngày phải đỏ. **Đối chứng:** gọi API danh sách HĐ đọc giá trị thô của chính bản ghi đó, so với chuỗi đang hiển thị |
| **C4** | "Dữ liệu hiển thị không bị tràn/đè lên nhau" | `srs-fr-05-vu-viec.md:1568`–`:1573` (§C cắt nội dung dài) + `:1603` (§F responsive CMS ≥1024×768) — đặc tả **chỉ quy định cắt chuỗi dài + độ phân giải tối thiểu**, **IM LẶNG** về tràn/đè bố cục | **GAP** | **BA** | Chỉ đo hiện trạng ở 1440×900 (viewport chuẩn của lô) để mô tả cho BA. **CẤM Pass/Reopen.** Nếu bắt gặp cột text dài **không** cắt + **không** tooltip → đó là quan sát độc lập vi phạm §C, xử theo gate "bug mới tự lộ", không đổi quan hệ vế này |
| **C5** | "…đồng nhất ngôn ngữ hiển thị" | `srs-fr-05-vu-viec.md:1492` + `:1484` | **MATCH** | TEST | **UI:** đọc `innerText` toàn bộ tiêu đề cột + nhãn bộ lọc + nội dung ô Trạng thái, khẳng định không có mã DB kiểu `DANG_THUC_HIEN` / `HOAN_THANH` / `HUY` / `TAM_DUNG` và không lẫn tiếng Anh. **Đối chứng:** so với giá trị thô trong response API (phải là mã DB) → chứng minh có lớp dịch nhãn |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:274`**
```
**UX-Spec ref:** dac-ta-man-hinh-chuc-nang-v2.md -- MH-14.1
```
> ⚠️ Đã `find` toàn repo lượt này: **không tồn tại** tệp `dac-ta-man-hinh-chuc-nang-v2.md`. Bản vẽ "thiết kế" mà đối tác nhắc **không nằm trong nguồn chuẩn prompt cấp** ⇒ không có căn cứ chấm.

**`srs-fr-14-hop-dong-tv.md:278`**
```
**Danh sách:** Breadcrumb > Tiêu đề + nút hành động > Thanh lọc (tìm kiếm UC159e) > Bảng hợp đồng > Phân trang.
```

**`srs-fr-14-hop-dong-tv.md:285`**
```
| 1 | toolbar | Breadcrumb | breadcrumb | "Trang chủ > Tư vấn > Hợp đồng tư vấn" | navigate | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:286`**
```
| 2 | toolbar | Tiêu đề + nút | label + button | "Quản lý Hợp đồng Tư vấn" + [+ Thêm hợp đồng] [Xuất Excel] [Làm mới] | click -> action | luôn hiển thị; **nút [+ Thêm hợp đồng] CHỈ hiển thị với CB NV — ẩn với TVV/CG** |
```

**`srs-fr-14-hop-dong-tv.md:287`**
```
| 3 | filter-bar | Thanh lọc (UC159e) | form | Full-text: tên HĐ, mã HĐ, bên B. TVV (searchable). Khoảng ngày | change -> filter | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:288`**
```
| 4 | content | Bảng hợp đồng | table | Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu <= 30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động (CB NV thấy Xem/Sửa/Xóa; TVV/CG CHỈ thấy nút Xem) | click -> action | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:289`**
```
| 5 | footer | Phân trang | pagination | 20 mục/trang | click -> chuyển trang | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:147`–`:155`** (bảng Outputs FR-X.3-01 — cột Format)
```
| 1 | ma_hop_dong | text | luôn | HDTV-{date}-{seq} |
| 2 | ten_hop_dong | text | luôn | — |
| 3 | ben_a | text | luôn | — |
| 4 | ben_b | text | luôn | — |
| 5 | gia_tri_hop_dong | money | luôn | format tiền VND |
| 6 | thoi_han_bat_dau | date | luôn | dd/mm/yyyy |
| 7 | thoi_han_ket_thuc | date | luôn | dd/mm/yyyy |
| 8 | so_vv_lien_ket | number | luôn | badge |
| 9 | tien_do_tt | number | luôn | progress bar % |
```

**`srs-fr-05-vu-viec.md:1484`** (§A — cách đọc bảng Thành phần màn hình)
```
| **Thành phần** | Tên thành phần (đặt theo nhãn hiển thị thực tế, không dùng mã DB hay viết tắt nội bộ) |
```

**`srs-fr-05-vu-viec.md:1492`** (§B — ánh xạ mã DB → nhãn tiếng Việt)
```
Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt theo bảng dưới. Mã DB **không bao giờ** xuất hiện trên giao diện người dùng.
```

**`srs-fr-05-vu-viec.md:1571`–`:1573`** (§C — quy ước cắt nội dung dài)
```
- Cột tên / tiêu đề > 30 ký tự: cắt + dấu `...` cuối + tooltip hover hiển thị nội dung đầy đủ
- Cột mô tả ngắn > 50 ký tự: cắt + tooltip
- Áp dụng nhất quán cho 5 SCR — không spec lại trong từng cột
```

**`srs-fr-05-vu-viec.md:1603`** (§F — responsive)
```
- **Phía cán bộ (CMS) — SCR-V.I-01, -02, -03 ở chế độ CMS:** tối thiểu hỗ trợ máy tính bảng 1024×768. Không bắt buộc mobile.
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)**. Cột `Tác nhân` (F) của phiếu **RỖNG** ⇒ suy từ đặc tả: `srs-fr-14-hop-dong-tv.md:68` (CB NV — quyền CRUD đầy đủ) và `:27` (Tác nhân chính: Cán bộ Nghiệp vụ TW/BN/ĐP). Vế C1 còn đòi thấy nút `[+ Thêm hợp đồng]` — `:286` nói nút này **chỉ** hiện với CB NV ⇒ **bắt buộc** đăng nhập CB NV, dùng TVV/CG sẽ Fail oan | `:27`, `:68`, `:286` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` (bộ `_03` theo brief §3). Cấp TW để thấy dữ liệu toàn quốc (`srs-v3.5.md:1375` — "**TW (Trung ương):** Nhìn thấy dữ liệu TẤT CẢ đơn vị (toàn quốc)"), tránh bảng rỗng làm không đo được C3/C4 | brief §3 |
| **Dữ liệu** | **≥1 hợp đồng** trong phạm vi đơn vị, và trong đó **≥1 hợp đồng có đủ**: giá trị HĐ > 0, thời hạn bắt đầu + kết thúc, ≥1 vụ việc liên kết (để Số VV ≠ 0), ≥1 giai đoạn thanh toán đã thanh toán (để Tiến độ TT ≠ 0%). Không có bản ghi "đủ chất" thì C3 chỉ đo được một phần → ghi Chưa chốt phần đó, **không** Pass suy đoán | `:288` (10 cột đều phải có nội dung để đối chiếu) |
| **Dữ liệu phụ (C4)** | Muốn đo tràn/đè có ý nghĩa cần ≥1 HĐ có **Tên HĐ > 30 ký tự** và **Bên B dài**. Nếu pool không có, được seed thêm 1 HĐ tên dài (khai rõ: bản ghi nào · đổi gì · env nào) | `srs-fr-05-vu-viec.md:1571` |
| **Viewport** | 1440×900 (cấu hình MCP của lô). Ghi rõ vào báo cáo — `srs-fr-05-vu-viec.md:1603` chỉ bảo đảm ≥1024×768 | brief §3 |

> 🔴 **Cảnh báo đường vào màn (áp cho cả 18 phiếu).** Bước J của phiếu ghi *"Chọn menu Hợp đồng Tư vấn"*, nhưng `srs-fr-14-hop-dong-tv.md:266`–`:268` nói nhóm X.3 **không còn là mục menu riêng** và route độc lập **không được coi là luồng chính**. Đây là **tiền đề/đường đi**, **không** phải vế chấm của phiếu này (cột K không nhắc menu) ⇒ **không tách thành vế, không tự log bug**. Ghi lại đường thực tế đã đi vào báo cáo và đưa vào câu hỏi BA gộp ở `00-TONG-HOP-QLHDTVVCG.md`.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bề mặt đủ cột là kết luận đạt.** `:288` đòi Thời hạn kết thúc **đỏ khi ≤30 ngày** và Tiến độ TT là **progress bar %** — nếu chỉ liếc thấy "có cột" mà cột luôn trắng/0% trên mọi dòng thì chưa đo được gì. Phải có bản ghi thật rơi vào ngưỡng ≤30 ngày mới kết luận được phần đỏ; không có thì ghi Chưa chốt phần đó.
- **Bảng rỗng vẫn "trông đúng thiết kế".** Bảng 0 dòng thì C3/C4 **không đo được** — không được Pass C3 bằng ảnh bảng rỗng.
- **Ngôn ngữ (C5) chỉ nhìn tiêu đề cột.** Mã DB thường lộ ở **ô Trạng thái** và ở **tooltip/`title`**, không ở tiêu đề. Phải đọc `innerText` nội dung ô, không chỉ header.
- **Đọc bằng `textContent`.** Gom cả node ẩn của AntD → thấy chuỗi không có thật trên màn (bug ma) hoặc ngược lại che mất mã DB đang hiện. Dùng `innerText`.

**Dễ Fail oan:**
- **Chấm C1/C2 theo bản vẽ Figma / ảnh đối tác.** Bản vẽ `MH-14.1` **không có trong nguồn chuẩn** — mọi khác biệt về màu, vị trí, icon, thứ tự nút **không phải căn cứ Fail**. Đó chính là lý do C2 bị khóa `GAP`.
- **Fail vì màn có thêm cột/nút ngoài `:288`.** Đặc tả liệt kê thành phần **bắt buộc có**, không tuyên bố "cấm có thêm". Thừa thành phần → ghi nhận cho BA, không Fail.
- **Fail vì nhãn nút lệch.** `:286` ghi `[+ Thêm hợp đồng]`, trong khi Phụ lục E §H4 (`srs-v3.5.md:6756`) bắt nút thêm mới luôn là **"Thêm mới"** — **hai dòng của chính đặc tả đã lệch nhau**. Phiếu này không chấm nhãn nút ⇒ không Fail vì lý do đó; đưa vào câu hỏi BA gộp.
- **Fail vì phân trang không đúng 20.** `:289` ghi 20 mục/trang; nhưng `BR-DATA-07` (`:530`) cho phép tới max 100 rows/page. Chỉ Fail khi **không có phân trang**, không Fail vì con số mặc định khác 20 — nêu cho BA.
- **Fail vì cột Hành động thiếu chữ.** Phụ lục E §H6 (`srs-v3.5.md:6758`) quy định cột Hành động dùng **icon + tooltip**, không dùng nhãn text. Thấy icon thay vì chữ "Xem/Sửa/Xóa" là **đúng** đặc tả.
