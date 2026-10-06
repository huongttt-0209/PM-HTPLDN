# Chuẩn chấm đã khóa — DGKQHTVV_02 (dòng 65) — GIAI ĐOẠN A, CHƯA CÓ VERDICT

> **FLOW 04** — verify bug dev báo đã fix, **không có hồ sơ nội bộ** (không có bug entry, không có khối `CÁCH VERIFY` cũ cho mã này).
> **Nguồn chuẩn đặc tả — DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> Mọi số dòng dưới đây **tự mở file đọc lại ngày 2026-08-07 trong lượt này**. Không mượn số dòng từ phiếu UAT, thư BA hay báo cáo đợt cũ.
> Chức năng: **FR-V.I-17 — Đánh giá kết quả hỗ trợ vụ việc (UC67)**, heading tại `srs-fr-05-vu-viec.md:1185`.
> Màn: **SCR-V.I-03 — Chi tiết Vụ việc**, heading tại `srs-fr-05-vu-viec.md:1715`; thành phần Nhóm 8 tại `:1734`.
>
> 🔴 **Không có bằng chứng đối tác cho mã này** (đã tìm toàn bộ `reverify-week-5/**/partner-evidence/` — chỉ có QLBMHD_02, QLHSPLDN_06/07). ⇒ Tiền đề tái hiện phải suy từ **chính các bước + điều kiện ghi trên phiếu**, và phải khai rõ điều kiện đã tái hiện trong báo cáo.
>
> 🔴 **Cảnh báo lệch mã TC:** nguồn case đợt này có ghi chú đối tác **xóa và đánh lệch ID**, đã chuyển lại ID để map. ⇒ Khi ghi kết quả phải neo vào **đúng dòng 65 của nguồn case**, không neo vào mã `DGKQHTVV_02` một mình.

---

## 1. Lỗi gốc — nguyên văn phiếu

| | Nội dung |
|---|---|
| **Mã TC / dòng** | `DGKQHTVV_02` — dòng **65** |
| **Mô tả** | Kiểm tra hiển thị các trường thông tin Nhóm 8 – Đánh giá |
| **Điều kiện** | 1. Đăng nhập tài khoản; 2. Hồ sơ vụ việc ở trạng thái "Hoàn thành" hoặc "Đã đánh giá" |
| **Các bước** | 1. Chọn menu "Vụ việc HTPL"; 2. Tìm kiếm và nhấn Xem chi tiết; 3. Mở Nhóm 8 – Đánh giá |
| **Kết quả mong đợi (nguyên văn)** | - Hệ thống hiển thị các trường thông tin giống với thiết kế<br>- Dữ liệu hiển thị đúng định dạng và trường thông tin<br>- Dữ liệu hiển thị không bị tràn/đè lên nhau, đồng nhất ngôn ngữ hiển thị |
| **Trạng thái** | Fail · **Dopai:** Open · **Trạng thái dev fix:** Fixed |

**Vai trò suy ra từ bước 1:** bước "Chọn menu **Vụ việc HTPL**" là menu **CMS phía cán bộ** (`srs-v3.5.md:641` — `📋 Quản lý vụ việc hỗ trợ pháp lý [click thẳng] → FR-V.I (UC51-67)`; tiêu đề màn `srs-fr-05-vu-viec.md:1637` — `"Quản lý Vụ việc HTPL"`). Phía DN dùng menu/URL khác (`SCR-V.I-04`, `:1815`, `:1819`). ⇒ **Vế này đo ở chế độ CÁN BỘ (CB_NV)**, không phải chế độ doanh nghiệp. Nhánh doanh nghiệp là mã `DGKQHTVV_01`, không gộp vào đây.

---

## 2. Đặc tả đối chiếu — trích dẫn nguyên văn, tự mở file đếm lại

### 2.1 Bộ trường của Nhóm 8 — Đánh giá

| `file:dòng` | Nguyên văn (cắt ở ≤220 ký tự, đánh dấu `…`) |
|---|---|
| `srs-fr-05-vu-viec.md:1185` | `### FR-V.I-17: Đánh giá kết quả hỗ trợ vụ việc (UC67)` |
| `srs-fr-05-vu-viec.md:1188` | `**Màn hình:** SCR-V.I-03 (Accordion 8 — Đánh giá)` |
| `srs-fr-05-vu-viec.md:1190` | `**Mô tả:** CB NV hoặc DN đánh giá chất lượng hỗ trợ VV theo 3 tiêu chí thang 0-10 (theo CSV UC67). Mỗi loại người đánh giá chỉ chấm 1 lần/vụ việc.` |
| `srs-fr-05-vu-viec.md:1734` | `\| 11 \| content \| Accordion 8 — Đánh giá (gộp MH-05.9) \| C23 \| diem_chat_luong (0-10), diem_thoi_gian (0-10), diem_thai_do (0-10), diem_tong (AVG auto), nhan_xet \| CB NV/DN nhập trực tiếp \| Khi VV ở HOAN_THANH hoặc DA_DANH_GIA \|` |

**Inputs của FR-V.I-17 (`:1202`–`:1209`) — nguyên văn từng dòng:**

| `dòng` | Nguyên văn |
|---|---|
| `:1204` | `\| 1 \| vu_viec_id \| identifier \| Y \| Vụ việc được đánh giá (FK → VU_VIEC) \|` |
| `:1205` | `\| 2 \| diem_chat_luong \| number \| Y \| 0-10 \|` |
| `:1206` | `\| 3 \| diem_thoi_gian \| number \| Y \| 0-10 \|` |
| `:1207` | `\| 4 \| diem_thai_do \| number \| Y \| 0-10 \|` |
| `:1208` | `\| 5 \| diem_tong \| number \| Y (auto) \| AVG(3 điểm) \|` |
| `:1209` | `\| 6 \| nhan_xet \| text (long) \| N \| — \|` |

**Mô hình dữ liệu `DANH_GIA_VU_VIEC` (`:2106`–`:2123`) — nguyên văn dòng dùng để chấm:**

| `dòng` | Nguyên văn |
|---|---|
| `:2108` | `**Mô tả:** Đánh giá chất lượng hỗ trợ VV. Mỗi VV có tối đa 1 đánh giá từ CB NV và 1 từ DN — UNIQUE (vu_viec_id, loai_nguoi_danh_gia).` |
| `:2115` | `\| 3 \| nguoi_danh_gia_id \| identifier \| Y \| FK → TAI_KHOAN(id) \| — \| Người thực hiện đánh giá \|` |
| `:2116` | `\| 4 \| loai_nguoi_danh_gia \| text \| Y \| CHECK IN ('CB_NV','DN') \| — \| Loại người đánh giá (theo CSV UC67: chỉ CB Nghiệp vụ và Doanh nghiệp) \|` |
| `:2117` | `\| 5 \| diem_chat_luong \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm chất lượng tư vấn \|` |
| `:2118` | `\| 6 \| diem_thoi_gian \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm đúng thời hạn \|` |
| `:2119` | `\| 7 \| diem_thai_do \| number \| Y \| CHECK BETWEEN 0 AND 10 \| — \| Điểm thái độ phục vụ \|` |
| `:2120` | `\| 8 \| diem_tong \| number \| Y \| Auto = AVG(diem_chat_luong, diem_thoi_gian, diem_thai_do) \| — \| Điểm tổng hợp \|` |
| `:2121` | `\| 9 \| nhan_xet \| text \| N \| max 2000 \| — \| Nhận xét chi tiết \|` |
| `:2122` | `\| 10 \| ngay_danh_gia \| datetime \| Y \| DEFAULT NOW() \| — \| Thời điểm đánh giá \|` |
| `:2123` | `\| 11 \| don_vi_id \| identifier \| Y \| FK → DON_VI(id) \| — \| Đơn vị sở hữu \|` |

### 2.2 → BẢNG "TRƯỜNG BẮT BUỘC THEO SRS" của Nhóm 8

Chốt từ `:1734` (bảng Thành phần màn hình — danh sách đóng ở cấp đặc tả theo `srs-v3.5.md:584`) đối chiếu `:1204`–`:1209` và `:2117`–`:2121`:

| # | Trường (mã trong SRS) | Có ở `:1734`? | Thang / định dạng SRS ghi | Nhãn tiếng Việt SRS ghi ở đâu | Bắt buộc hiện? |
|---|---|---|---|---|---|
| 1 | `diem_chat_luong` | ✅ `:1734` | `0-10` (`:1205`, `:2117`) | **KHÔNG có nhãn UI.** Chỉ có mô tả entity `:2117` *"Điểm chất lượng tư vấn"* | **CÓ — bắt buộc** |
| 2 | `diem_thoi_gian` | ✅ `:1734` | `0-10` (`:1206`, `:2118`) | **KHÔNG có nhãn UI.** Mô tả entity `:2118` *"Điểm đúng thời hạn"* | **CÓ — bắt buộc** |
| 3 | `diem_thai_do` | ✅ `:1734` | `0-10` (`:1207`, `:2119`) | **KHÔNG có nhãn UI.** Mô tả entity `:2119` *"Điểm thái độ phục vụ"* | **CÓ — bắt buộc** |
| 4 | `diem_tong` | ✅ `:1734` | `AVG auto` (`:1208`, `:1220`, `:2120`); **số chữ số thập phân: IM LẶNG** | **KHÔNG có nhãn UI.** Mô tả entity `:2120` *"Điểm tổng hợp"* | **CÓ — bắt buộc** |
| 5 | `nhan_xet` | ✅ `:1734` | `text (long)`, không bắt buộc (`:1209`), `max 2000` (`:2121`) | **KHÔNG có nhãn UI.** Mô tả entity `:2121` *"Nhận xét chi tiết"* | **CÓ — ô phải hiện; giá trị được rỗng** |
| 6 | `nguoi_danh_gia_id` / `ngay_danh_gia` | ❌ **không có ở `:1734`** | `:2115` / `:2122` | — | **KHÔNG bắt buộc.** Nếu web CÓ hiện → xử theo `srs-v3.5.md:584` (xem §6 bẫy FAIL oan #1) |
| 7 | `loai_nguoi_danh_gia` / `don_vi_id` | ❌ không có ở `:1734` | `:2116` / `:2123` | — | **KHÔNG bắt buộc hiện** |

> ⇒ **Bộ trường bắt buộc = đúng 5: 3 điểm thành phần + điểm tổng + nhận xét.** Thiếu bất kỳ 1 trong 5 = không đạt. Có thêm trường ngoài 5 ⇒ **KHÔNG tự động là lỗi** — phải qua cổng `srs-v3.5.md:584`.

### 2.3 Quy ước UI có hiệu lực chấm

| `file:dòng` | Nguyên văn |
|---|---|
| `srs-fr-05-vu-viec.md:1484` | `\| **Thành phần** \| Tên thành phần (đặt theo nhãn hiển thị thực tế, không dùng mã DB hay viết tắt nội bộ) \|` |
| `srs-fr-05-vu-viec.md:1486` | `\| **Dữ liệu / Nội dung** \| Chữ chính xác user nhìn thấy trên màn hình + tooltip (nếu có) + ràng buộc validation \|` |
| `srs-fr-05-vu-viec.md:1492` | `Khi render UI, dev **phải dịch** mã DB (snake_case enum) sang nhãn tiếng Việt theo bảng dưới. Mã DB **không bao giờ** xuất hiện trên giao diện người dùng.` |
| `srs-fr-05-vu-viec.md:1622` | `- Mã DB / mã enum trong nhãn UI` *(nằm trong khối "**KHÔNG đưa vào description:**" bắt đầu ở `:1619`)* |
| `srs-v3.5.md:578` | `\| UI-06 \| Localization \| Tiếng Việt là ngôn ngữ duy nhất. Unicode UTF-8. Định dạng ngày: dd/MM/yyyy. Số: dấu chấm phân cách hàng nghìn \| UX-Spec Section 1 \|` |
| `srs-v3.5.md:584` | `\| UI-12 \| Bảng "Thành phần màn hình" là danh sách đóng ở cấp đặc tả \| … Khi màn hình có mục không nằm trong bảng: nếu mục đó **có căn cứ** ở §Inputs / §Processing / §Outputs / mô hình dữ liệu của chính FR đang xét thì **bảng bị sót — phần mềm đúng**, BA bổ sung vào bảng; nếu **không có căn cứ** ở bất kỳ đâu trong SRS thì **phần mềm thừa**, đội phát triển gỡ. …` |
| `srs-v3.5.md:585` | `\| UI-13 \| Dấu sao bắt buộc chỉ dùng cho trường người dùng tự nhập \| Nhãn trường gắn dấu sao (\*) khi và chỉ khi người dùng phải tự nhập giá trị. Trường **chỉ đọc / hệ thống tự gán** thì **không** gắn dấu sao dù dữ liệu bắt buộc phải có … \|` |
| `srs-fr-05-vu-viec.md:1809` | `\| Nhóm 8 — Đánh giá \| Cho phép nhập khi vụ việc ở "Hoàn thành" / "Đã đánh giá" + DN chưa đánh giá. Sau khi đánh giá → chuyển sang chế độ chỉ đọc \|` *(bảng **chế độ doanh nghiệp** — chỉ dùng làm ngữ cảnh, KHÔNG dùng chấm case này)* |

### 2.4 Chỗ SRS IM LẶNG hoặc TỰ MÂU THUẪN — đã đọc trọn đoạn, không phải grep rỗng

| Vấn đề của expected | Kết luận | Dòng gần nhất đã đọc (để truy phạm vi kết luận) |
|---|---|---|
| **Nhãn tiếng Việt cụ thể của 5 trường Nhóm 8** | **IM LẶNG + TỰ MÂU THUẪN.** `:1486` quy ước cột "Dữ liệu / Nội dung" là *"Chữ chính xác user nhìn thấy trên màn hình"*, nhưng ô thực tế ở `:1734` lại ghi **mã DB snake_case** (`diem_chat_luong`…), trong khi `:1492` + `:1622` cấm mã DB xuất hiện trên UI. ⇒ Từ SRS **không rút ra được chuỗi nhãn nào là đúng**. Cột "Mô tả" của bảng entity (`:2117`–`:2121`) là **mô tả entity, không phải nhãn UI** — cấm dùng làm chuẩn chữ | `:1484`, `:1486`, `:1492`, `:1622`, `:1734`, `:2117`–`:2121` |
| **"giống với thiết kế"** (bố cục, thứ tự, khoảng cách, màu, kiểu điều khiển) | **GAP — tài liệu thiết kế mà SRS trỏ tới KHÔNG có trong nguồn chuẩn.** `srs-v3.5.md:567`: `**Tài liệu chi tiết:** Xem \`ux-spec.md\` (toàn bộ design system, component library, screen specs)`. Đã kiểm `_bmad-output/planning-artifacts/` — chỉ có `srs-v3`, `srs-v3.5`, `srs-v4`; **không có `ux-spec.md`** | `srs-v3.5.md:567`, `:263`, `:589`, `:623` |
| **Số chữ số thập phân / cách làm tròn `diem_tong`** | **IM LẶNG cho UC67.** Quy tắc làm tròn duy nhất trong file loại trừ UC67 rõ ràng: `srs-fr-05-vu-viec.md:2462` — `Trigger cập nhật \`TU_VAN_VIEN.diem_danh_gia_tb = AVG(diem_trung_binh)\` từ DANH_GIA_SAU_VU_VIEC … Thang điểm 1–5, làm tròn 1 chữ số thập phân (round-half-up). UC67 chỉ tạo DANH_GIA_VU_VIEC (thang 0–10), trigger cập nhật điểm TVV nằm ở **FR-IV-CROSS-01**.` | `:1208`, `:2120`, `:2462` |
| **"không bị tràn / đè lên nhau"** | **IM LẶNG.** Không có dòng nào trong nguồn chuẩn đặt tiêu chí không-tràn/không-chồng-lấn cho vùng accordion. Quy ước cắt nội dung dài chỉ áp cho **bảng**: `srs-fr-05-vu-viec.md:1570` — `Áp dụng cho mọi cột text trong bảng:` (Nhóm 8 không phải bảng). **Thêm: hai dòng responsive MÂU THUẪN nhau** — `srs-v3.5.md:579` (`UI-07 … Desktop-only. Min width: 1024px … Không hỗ trợ mobile/tablet`) vs `srs-fr-05-vu-viec.md:1603` (`**Phía cán bộ (CMS) — SCR-V.I-01, -02, -03 ở chế độ CMS:** tối thiểu hỗ trợ máy tính bảng 1024×768. Không bắt buộc mobile.`) và `:1604` (`**Phía doanh nghiệp** … thiết kế ưu tiên di động (mobile-first). Bảng dài auto chuyển sang dạng card khi màn hình < 768px.`) | `srs-v3.5.md:577`, `:579`; `srs-fr-05-vu-viec.md:1568`–`:1573`, `:1601`–`:1604` |
| **Chữ tiêu đề của chính accordion** ("Nhóm 8" hay "Accordion 8") | **TỰ MÂU THUẪN trong cùng file:** `:1734` gọi `Accordion 8 — Đánh giá`, `:1809` gọi `Nhóm 8 — Đánh giá`. ⇒ **Không phải tiêu chí chấm** | `:1734`, `:1809` |

---

## 3. BUG SCOPE LOCK — các dòng `Cn`

> Tách **đúng 3 gạch đầu dòng của expected**, không thêm chức năng kế bên. Sau khi mở màn, **cấm đổi quan hệ** `MATCH/DIFF/GAP` để khớp kết quả (Flow 04, luật khóa 5).

```
C1 · "Hệ thống hiển thị các trường thông tin giống với thiết kế" — phần ĐO ĐƯỢC: Nhóm 8 hiện đủ 5 trường
     (3 điểm thành phần + điểm tổng + nhận xét)
   · srs-fr-05-vu-viec.md:1734 (+ :1204-:1209, :2117-:2121) · MATCH · route TEST
   · Đường đo: mở chi tiết 1 VV đã có đánh giá → mở Nhóm 8 → đếm bằng mắt trong khung nhìn đủ/thiếu 5 trường

C2 · "…giống với thiết kế" — phần nhãn tiếng Việt cụ thể / thứ tự / bố cục / kiểu điều khiển
   · IM LẶNG + MÂU THUẪN (:1486 nói cột là "chữ chính xác user nhìn thấy" nhưng :1734 ghi mã DB;
     :1492/:1622 lại cấm mã DB trên UI; ux-spec.md mà srs-v3.5.md:567 trỏ tới KHÔNG có trong nguồn chuẩn)
   · GAP · route BA · Đường đo: chỉ GHI NHẬN hiện trạng (chụp 1 ảnh Nhóm 8) làm dữ kiện cho câu hỏi BA — KHÔNG chấm

C3 · "Dữ liệu hiển thị đúng định dạng và trường thông tin" — phần ĐO ĐƯỢC: giá trị hiển thị ở Nhóm 8
     đúng bằng giá trị đã lưu của đúng bản ghi đó, mỗi điểm nằm trong 0-10, điểm tổng = trung bình 3 điểm
   · srs-fr-05-vu-viec.md:1205-:1208, :2117-:2120 · MATCH · route TEST
   · Đường đo: đọc giá trị trên màn ↔ đọc lại bản ghi đánh giá của đúng VV đó từ máy chủ, đối chiếu từng trường

C3b · "…đúng định dạng" — số chữ số thập phân / cách làm tròn của điểm tổng
   · IM LẶNG cho UC67 (:2462 loại trừ UC67 khỏi quy tắc làm tròn duy nhất) · GAP · route BA
   · Đường đo: chỉ GHI NHẬN chuỗi hiển thị thực tế (vd "9" / "9.0" / "9,0") — KHÔNG chấm đúng/sai

C4 · "…đồng nhất ngôn ngữ hiển thị" — nhãn + giá trị hiển thị là tiếng Việt, KHÔNG lộ mã DB snake_case,
     KHÔNG lộ chuỗi tiếng Anh / null / undefined
   · srs-fr-05-vu-viec.md:1492 + :1622 + srs-v3.5.md:578 (UI-06) · MATCH · route TEST
   · Đường đo: đọc innerText của vùng Nhóm 8, soi 3 mẫu: /[a-z]+_[a-z_]+/ (snake_case) · null|undefined ·
     từ tiếng Anh lộ ra

C5 · "Dữ liệu hiển thị không bị tràn/đè lên nhau"
   · IM LẶNG (dòng gần nhất đã đọc: srs-fr-05-vu-viec.md:1570 §C chỉ áp cho cột text TRONG BẢNG;
     srs-v3.5.md:579 UI-07 vs srs-fr-05-vu-viec.md:1603-:1604 MÂU THUẪN về khổ màn hỗ trợ) · GAP · route BA
   · Đường đo: chụp 1 ảnh Nhóm 8 ở khổ ≥1280px, GHI NHẬN hiện trạng — KHÔNG chấm
   · 🔴 NGOẠI LỆ ĐÃ KHÓA: nếu tràn/đè tới mức làm giá trị của MỘT trong 5 trường ở :1734 KHÔNG đọc được,
     thì đó là vi phạm C1 (trường không được hiển thị) → Reopen theo C1, KHÔNG cần BA.
     Tràn/đè mà vẫn đọc được đủ 5 giá trị → giữ nguyên GAP, không Reopen.
```

**Ánh xạ bắt buộc:** mọi thao tác / seed / ảnh phải trả lời được `đang kiểm Cn nào?`. Không ánh xạ được ⇒ **CẤM chạy**.

**Hệ quả logic đã thấy trước (Flow 04 §Ca biên):** vì tồn tại `C2`, `C3b`, `C5` là `GAP`, **case này không thể ra verdict "Pass" thuần**, kể cả khi web hoàn hảo. Kết quả logic tốt nhất = **Cần BA** với `WEB HIỆN TẠI` ghi *"đúng kỳ vọng đối tác"* và `CÂU HỎI BA` nêu rõ mục đích là **bổ sung điều này vào đặc tả, không phải chặn bàn giao**.

---

## 4. Tiền đề tối thiểu + tài khoản / vai trò

### 4.1 Môi trường

| Hạng mục | Giá trị |
|---|---|
| Env đo | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env nghiệm thu đối tác `htpldn-uat.ospgroup.vn` |
| Mã xác thực 6 số | MailHog `http://18.143.165.120:8025/` (env chưa tích hợp email thật — cấm log "không nhận được mã" thành bug) |
| Vân tay bản dựng | **Phải đo lại đầu phiên** (bó mã FE + `last-modified` + `etag`). Bản đo 2026-08-06 18:44: `HTPLDN · V1.0.8`, `assets/index-DIABnbIr.js`, `last-modified Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"` — nếu trùng nguyên ⇒ FE **chưa deploy lại**, phải ghi vào kết quả |
| Giới hạn hiệu lực | Verdict chỉ có giá trị cho env + bản dựng đã đo. Đối tác đo trên `htpldn-uat.ospgroup.vn` — phải ghi câu giới hạn này |

### 4.2 Vai trò được đánh giá theo SRS

`srs-fr-05-vu-viec.md:1198` — `| PRE-03 | Role ∈ {CB_NV, DN} (theo CSV UC67) |`
`srs-fr-05-vu-viec.md:1216` — `| 2 | Validate scope theo role: nếu role='DN' → VU_VIEC.doanh_nghiep_id = current_user.doanh_nghiep_id; nếu role='CB_NV' → VU_VIEC.don_vi_id = current_user.don_vi_id | BR-AUTH-03/04, BR-AUTH-08 |`

⇒ **Vai trò ra verdict cho mã này = CB Nghiệp vụ (CB_NV)**, và **vụ việc phải cùng `don_vi_id` với tài khoản đo**.

| Vai trò | Tài khoản | Mật khẩu | Ghi chú |
|---|---|---|---|
| **CB NV Trung ương — ưu tiên ra verdict** | `cbnv_tw` | `Test@1234` | Tài khoản đã dùng đo lô 06/08 (`BAN-DUNG.md:19`) |
| Dự phòng cùng vai trò + cùng cấp (Rule 7) | `cbnv_tw_01` → `cbnv_tw_02` → `cbnv_tw_03` | `Test@1234` | **Chỉ fallback trong CÙNG vai trò + CÙNG cấp**; phải khai account thực dùng |
| CB NV Địa phương (nếu bản ghi tiền đề thuộc An Giang) | `cbnv_dp_01` (`cbnv_dp` đang FAIL login từ 03/08) | `Test@1234` | Dùng khi VV tiền đề thuộc đơn vị ĐP — bắt buộc để thoả `:1216` |
| **CẤM ra verdict** | `admin` | — | Quyền rộng che lỗi phân quyền/scope |
| **KHÔNG dùng cho mã này** | tài khoản doanh nghiệp (tên đăng nhập = mã số thuế) | — | Nhánh DN là `DGKQHTVV_01`, màn khác (`SCR-V.I-04`/`:1815`), không gộp |

### 4.3 Dữ liệu tiền đề

**Cần: đúng 1 vụ việc thuộc đơn vị của tài khoản đo, ở `DA_DANH_GIA` và ĐÃ có bản ghi đánh giá loại `CB_NV`** — vì expected đòi *"Dữ liệu hiển thị đúng định dạng"*, tức Nhóm 8 phải **có dữ liệu để đọc**.

| Ứng viên tái dùng (ưu tiên — Flow 04 §Giai đoạn B bước 3) | Trạng thái ghi nhận 06/08 | Việc phải làm trước khi tính là tiền đề |
|---|---|---|
| `VV-BTP-TW-20260806-003` (`fbf936fb-…`) | "Đã đánh giá", đã có **1 đánh giá loại `CB_NV`** — 9·8·10, nhận xét `QA-DGKQ-20260806-1634` | **Xác minh lại** bằng phiên `cbnv_tw`: VV còn tồn tại, còn thuộc đơn vị của tài khoản đo, bản ghi đánh giá còn nguyên 3 điểm + nhận xét |
| `VV-BTP-TW-20260806-004` (`45501596-…`) | "Đã đánh giá", 1 đánh giá `CB_NV` — nhận xét `QA-DGKQ-20260806-1701` | Dự phòng |

**Nếu cả hai không dùng được** → dựng 1 bản ghi mới theo luồng chuẩn 8 bước (DN gửi hồ sơ → CB NV cùng địa bàn tiếp nhận → kiểm tra kết luận Đạt → phân công người xử lý → cập nhật kết quả → trình phê duyệt → CB PD duyệt → cập nhật kết quả cuối → "Hoàn thành"), rồi CB NV chấm 1 lần để đẩy sang "Đã đánh giá" (`:1222`). **Cấm ghi thẳng DB, cấm đoán endpoint seed.** Nếu có seed thì phải khai: **đổi bản ghi nào · đổi gì · trên env nào**.

> ⚠️ **Bản ghi tiền đề CHỈ CẦN 1.** `C1`–`C5` đều là vế hiển thị trên cùng một màn, một đường UI ⇒ theo luật khóa 3, **không lặp trên nhiều bản ghi / nhiều trạng thái chỉ để "chắc"**. Điều kiện phiếu ghi *"Hoàn thành **hoặc** Đã đánh giá"* là **hoặc**, không phải hai biến thể bắt buộc.

> ⚠️ **Tiền đề tạo được mà không chuẩn bị ⇒ CẤM chốt** (kể cả chốt bằng ô trống).

---

## 5. Đường đo + đối chứng độc lập

### 5.1 Đường UI ngắn nhất (1 đường duy nhất cho cả C1/C3/C4)

1. Tải lại trang bằng địa chỉ (không tái dùng tab cũ đang chạy bó mã cũ), ghi vân tay bản dựng.
2. Đăng nhập UI thật bằng `cbnv_tw` / `Test@1234` (mã 6 số lấy ở MailHog). Ghi account thực dùng.
3. Click menu **"Quản lý vụ việc hỗ trợ pháp lý"** (`srs-v3.5.md:641`) → màn danh sách `SCR-V.I-01` (`srs-fr-05-vu-viec.md:1626`).
4. Tìm theo **mã vụ việc** của bản ghi tiền đề → mở **Xem chi tiết** (`SCR-V.I-03`, `:1715`).
5. Mở **Nhóm 8 — Đánh giá**. Chụp `take_screenshot` toàn vùng Nhóm 8 ở khổ **≥1280px**.
6. **Đếm bằng mắt trong khung nhìn** đủ/thiếu 5 trường (C1). **Không** dùng querySelector moi phần tử ẩn rồi tính là "có".
7. Đọc chữ người dùng nhìn thấy bằng **`innerText`** (KHÔNG `textContent` — gom cả node ẩn → bug ma) để soi C4.

### 5.2 Đối chứng độc lập (bắt buộc — đúng 1 đường thứ hai)

- Bằng **chính phiên đăng nhập `cbnv_tw`** (JWT là cookie), đọc lại **bản ghi đánh giá của đúng vụ việc đó** từ máy chủ và đối chiếu **từng trường** với chữ trên màn ở bước 5.1: `diem_chat_luong` · `diem_thoi_gian` · `diem_thai_do` · `diem_tong` · `nhan_xet`.
- 🔴 **CHƯA BIẾT ĐƯỜNG DẪN API — phải tra danh sách endpoint TRƯỚC khi dùng.** Cấm tự đoán khóa JSON / ID / endpoint. Đọc bản mô tả API mà hệ thống công bố (`/api/docs-json`, đọc được không cần đăng nhập) để lấy **đúng** đường dẫn đọc chi tiết vụ việc / đọc đánh giá, rồi mới gọi.
- **Không** gọi bằng `admin`, **không** gọi bằng phiên vai trò khác.
- **Bấm lại cùng một nút KHÔNG tính là đường thứ hai.** Hai đường khớp thì **dừng**, không mở đường thứ ba.
- 🔴 **Hai đường mâu thuẫn ⇒ CHƯA ĐƯỢC CHỐT** — ghi cả hai, hỏi user.

### 5.3 Những gì CẤM chạy trong case này

- Không mở thêm màn / vai trò / bộ lọc / trạng thái khác để "kiểm cho chắc".
- Không đo nhánh doanh nghiệp (đó là `DGKQHTVV_01`).
- Không bấm nút Đánh giá / không gửi đánh giá mới (đó là `DGKQHTVV_04`) — trừ khi bản ghi tiền đề phải tự dựng.
- Không cài bộ bắt thông báo: case này **không có hành động sinh thông báo** ⇒ không thuộc vế `Cn` nào.

---

## 6. Bẫy chấm sai

### 6.1 Bẫy **FAIL oan** — dễ chấm sai thành lỗi

1. 🔴 **Thấy trường ngoài 5 trường của `:1734` (vd "Người đánh giá", "Thời điểm đánh giá") rồi log "thừa trường".** Theo `srs-v3.5.md:584` (UI-12): mục có **căn cứ** ở mô hình dữ liệu của chính FR đang xét ⇒ **bảng bị sót — phần mềm ĐÚNG**, BA bổ sung vào bảng. `nguoi_danh_gia_id` (`:2115`) và `ngay_danh_gia` (`:2122`) **có căn cứ** ⇒ **CẤM chấm Fail**; ghi câu hỏi BA bổ sung bảng. Chỉ trường **không có căn cứ ở bất kỳ đâu trong SRS** mới là "phần mềm thừa".
2. 🔴 **FAIL vì nhãn tiếng Việt khác chữ trong cột "Mô tả" của bảng entity** (`:2117`–`:2121`). Cột đó là **mô tả entity**, không phải nhãn UI. SRS **không quy định** chuỗi nhãn của 5 trường này (xem §2.4). ⇒ Thuộc `C2` = GAP.
3. 🔴 **FAIL vì điểm tổng hiện `9` thay vì `9.0` / `9,0`** (hoặc ngược lại). SRS **im lặng** về số chữ số thập phân cho UC67; `:2462` loại trừ UC67 khỏi quy tắc làm tròn duy nhất. ⇒ `C3b` = GAP.
4. 🔴 **FAIL vì nhận xét dài bị cắt + tooltip.** `:1570` (§C cắt nội dung dài) chỉ áp cho **cột text trong BẢNG**, Nhóm 8 không phải bảng. ⇒ SRS im lặng, ghi BA.
5. 🔴 **FAIL vì thu nhỏ cửa sổ rồi thấy tràn.** SRS **mâu thuẫn** về khổ hỗ trợ (`srs-v3.5.md:579` desktop-only ≥1024, không hỗ trợ tablet ↔ `srs-fr-05-vu-viec.md:1603` CMS tối thiểu tablet 1024×768). ⇒ **Đo ở khổ ≥1280px** (khổ SRS ghi là tối ưu) và không chấm ở khổ khác.
6. 🔴 **FAIL vì tiêu đề accordion ghi "Nhóm 8" (hay "Accordion 8") khác chữ mình mong đợi.** SRS dùng cả hai cách gọi cho cùng một thứ (`:1734` vs `:1809`) ⇒ không phải tiêu chí chấm.
7. ⚠️ **FAIL vì ô "Điểm tổng" không có dấu sao `*`.** `srs-v3.5.md:585` (UI-13): trường **hệ thống tự gán** thì **không** gắn dấu sao dù bắt buộc. `diem_tong` là `Y (auto)` (`:1208`) ⇒ **không được có dấu sao**.
8. ⚠️ **FAIL vì ô nhận xét trống.** `nhan_xet` là **không bắt buộc** (`:1209` — cột Bắt buộc = `N`). Ô phải **hiện**, giá trị được rỗng.
9. ⚠️ **FAIL vì không thấy Nhóm 4 / 5 / 7.** Đó là quy tắc **chế độ doanh nghiệp** (`:1805`, `:1806`, `:1808`) — không áp cho chế độ cán bộ. Ngược lại: ở chế độ cán bộ các nhóm này **phải** hiện, nhưng chúng **ngoài phạm vi** `Cn` của case này ⇒ chỉ ghi candidate nếu tự lộ, không mở phép đo.

### 6.2 Bẫy **PASS oan** — dễ chấm sai thành đạt

1. 🔴 **Thấy đủ 5 cái nhãn rồi Pass mà không đọc giá trị.** `C3` đòi **giá trị đúng bằng bản ghi đã lưu**. Nhãn có mà ô rỗng / hiện giá trị của bản ghi khác ⇒ **không đạt C3**.
2. 🔴 **Đo trên vụ việc CHƯA có đánh giá** (form Nhóm 8 rỗng) rồi kết luận "hiển thị đúng". Không có dữ liệu thì **không chấm được** vế *"Dữ liệu hiển thị đúng định dạng"* ⇒ tiền đề sai, kết quả vô hiệu.
3. 🔴 **Dùng `textContent` để đọc chữ.** Gom cả node ẩn của thư viện giao diện ⇒ vừa tạo bug ma, vừa che chuỗi thực sự hiển thị. **Bắt buộc `innerText`.**
4. 🔴 **Moi phần tử bằng querySelector rồi tính là "có hiển thị".** Trường ẩn (`display:none` / kích thước 0×0) **không** tính là hiển thị. Phải đếm bằng mắt trong khung nhìn + có ảnh chụp.
5. 🔴 **Tab mở lâu vẫn chạy bó mã FE cũ.** Đã gây báo Reopen oan trước đây. **Tải lại trang bằng địa chỉ + ghi vân tay bản dựng trước khi đo.**
6. ⚠️ **Pass vì "nhìn không thấy chữ tiếng Anh nào".** `C4` phải soi cả **mã DB snake_case** (`diem_chat_luong`…), `null`, `undefined` — không chỉ tiếng Anh.
7. ⚠️ **Pass vì `admin` xem được.** `admin` bị CẤM ra verdict; scope `:1216` chỉ đúng khi đo bằng `CB_NV` cùng đơn vị.

---

## 7. Kết luận sơ bộ — route (CHƯA CÓ VERDICT)

| Vế | Quan hệ | Route | Được chấm Pass/Reopen? |
|---|---|---|---|
| `C1` — đủ 5 trường Nhóm 8 | **MATCH** | **TEST** | ✅ Có |
| `C2` — nhãn / bố cục "giống thiết kế" | **GAP** (SRS im lặng + tự mâu thuẫn `:1486` ↔ `:1734` ↔ `:1492`; `ux-spec.md` không có trong nguồn) | **BA** | ❌ Cấm Pass, cấm Reopen |
| `C3` — giá trị đúng, mỗi điểm 0-10, điểm tổng = trung bình 3 điểm | **MATCH** | **TEST** | ✅ Có |
| `C3b` — số chữ số thập phân / làm tròn điểm tổng | **GAP** (`:2462` loại trừ UC67) | **BA** | ❌ |
| `C4` — tiếng Việt, không lộ mã DB | **MATCH** | **TEST** | ✅ Có |
| `C5` — không tràn / đè lên nhau | **GAP** (SRS im lặng; `srs-v3.5.md:579` ↔ `srs-fr-05-vu-viec.md:1603`–`:1604` mâu thuẫn) | **BA** | ❌, **trừ** ngoại lệ đã khóa: che mất giá trị 1 trong 5 trường ⇒ rơi về `C1` |

**⇒ Phải sang Giai đoạn B** (còn 3 vế `MATCH` phải verify), nhưng **verdict trần của case này là "Cần BA"**, không thể là "Pass" thuần (Flow 04 §Ca biên: *"Không vế nào Reopen mà còn `DIFF/GAP` → **Cần BA**"*).

**Câu hỏi BA phải nêu (soạn sẵn, chờ số đo điền vào chỗ `…`):**

1. **Nhãn hiển thị của 5 trường Nhóm 8 — Đánh giá là gì?** Bảng Thành phần màn hình (`srs-fr-05-vu-viec.md:1734`) ghi mã DB snake_case, trong khi quy ước của chính mục 3 (`:1486`) nói cột đó là *"Chữ chính xác user nhìn thấy trên màn hình"* và `:1492` + `:1622` cấm mã DB xuất hiện trên giao diện. Đề nghị BA chốt bộ nhãn tiếng Việt và **ghi vào chính bản SRS v3.5**. *(Web hiện tại: `…`)*
2. **Điểm tổng hiển thị mấy chữ số thập phân, làm tròn theo quy tắc nào?** `:2462` chỉ quy định cho thang TVV 1–5 và **loại trừ UC67**. *(Web hiện tại: `…`)*
3. **Có đưa "Người đánh giá" / "Thời điểm đánh giá" vào bảng Thành phần màn hình của Nhóm 8 không?** Hai trường này có căn cứ ở mô hình dữ liệu (`:2115`, `:2122`) nhưng không có trong bảng `:1734` — theo UI-12 (`srs-v3.5.md:584`) đây là **bảng bị sót**, cần BA bổ sung. *(Web hiện tại: `…`)*
4. **Khổ màn hình nào là chuẩn chấm hiển thị của màn CMS?** `srs-v3.5.md:579` ghi *desktop-only, không hỗ trợ mobile/tablet*; `srs-fr-05-vu-viec.md:1603` ghi *tối thiểu hỗ trợ máy tính bảng 1024×768*. Hai câu ngược nhau. Kèm câu hỏi: SRS có đặt tiêu chí "không tràn/đè lên nhau" cho vùng accordion không (hiện **im lặng**; `:1570` chỉ áp cho cột text trong bảng)?

> Nếu đo xong thấy web đạt hết `C1`/`C3`/`C4` và không có tràn/đè che giá trị: `WEB HIỆN TẠI` ghi **"đúng kỳ vọng đối tác"**, và câu hỏi BA nêu rõ mục đích là **bổ sung điều này vào đặc tả — KHÔNG phải chặn bàn giao** (Flow 04 §Nội dung kết quả tối thiểu, vế `GAP`).
