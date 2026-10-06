# Số liệu đo — Reverify round 9 (2026-07-25)

Môi trường: `https://18.143.165.120.nip.io` · Tài khoản `cbnv_tw_04` (CB Nghiệp vụ - Trung ương #04, CB_NV_TW).
Công cụ: Chrome DevTools MCP. Bộ bắt thông báo: `output/UAT_doi-tac/tools/toast-capture.js` — mọi lượt đo đều tự kiểm `soObserverDangSong = 1` trước khi tin số liệu.

---

## QLBMHD_OOS_01 (dòng 309) — Biểu mẫu → Danh sách biểu mẫu → form Chỉnh sửa

### Dữ liệu MỚI dựng trong phiên (25/07/2026 ~15:58)

| Mã BM | Tên lúc tạo | Tệp đính kèm | Thư mục |
|---|---|---|---|
| BM-20260725-009 | R9-QLBMHD-THU-A | `r9-ok-1.docx` (922 B, bản sao mới của `qa-ok-1.docx`) | QA-R7-A-CO-BM |
| BM-20260725-010 | R9-QLBMHD-THU-B | `r9-ok-2.docx` (922 B, bản sao mới của `qa-ok-2.docx`) | QA-R7-A-CO-BM |

Ảnh: `QLBMHD_OOS_01/image/seed-2-bieu-mau-moi-009-010.png`

### (A) Bản ghi MỚI — phép thử quyết định

| Lần đo | Bản ghi | Thao tác | Quan sát | Đạt |
|---|---|---|---|---|
| A0 (đối chứng) | BM-009 | Mở Sửa, **KHÔNG** bấm tải → đổi tên → [Lưu] | Lưu được. Tên → `R9-THU-A DOICHUNG`. phiên bản 1→2, lượt tải 0 | ✅ |
| A1 | BM-009 | Bấm "Tải tập tin" **1 lần** → đổi tên → [Lưu] | Sau khi tải: phiên bản **giữ nguyên 2**, lượt tải 0→1. Lưu được: 1 khung thông báo *"Cập nhật biểu mẫu thành công"*, 1 request ghi. Tên → `R9-THU-A SAU-TAI-LAN1`. phiên bản 2→3 | ✅ |
| A2 | BM-009 | Bấm tải **1 lần** → đổi tên → [Lưu] | Sau khi tải: phiên bản **giữ 3**, lượt tải 1→2. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-THU-A SAU-TAI-LAN2`. phiên bản 3→4 | ✅ |
| A3 | BM-009 | Bấm tải **1 lần** → đổi tên → [Lưu] | Sau khi tải: phiên bản **giữ 4**, lượt tải 2→3. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-THU-A SAU-TAI-LAN3`. phiên bản 4→5. **Ảnh chụp được khung thông báo** | ✅ |
| A4 | BM-010 | Bấm tải **1 lần** → đổi tên → [Lưu] | Sau khi tải: phiên bản **giữ 1**, lượt tải 0→1. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-THU-B SAU-TAI-LAN1`. phiên bản 1→2 | ✅ |
| A5 (biến thể) | BM-010 | Bấm tải **2 lần liên tiếp** → đổi tên → [Lưu] | Sau 2 lần tải: phiên bản **giữ 2**, lượt tải 1→3. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-THU-B TAI-2-LAN`. phiên bản 2→3 | ✅ |

**Kết quả (A): 4/4 lần bấm tải rồi Lưu đều thành công (A1, A2, A3, A4) + biến thể tải 2 lần (A5) cũng thành công. Đối chứng A0 đạt.**

### (B) Bản ghi CŨ (đã tồn tại từ round 7)

| Lần đo | Bản ghi | Tên cũ | Quan sát | Đạt |
|---|---|---|---|---|
| B1 | BM-20260725-006 | R7-KC-S6-RecordA TESTA-khong-tai | Bấm tải 1 lần: phiên bản **giữ 4**, lượt tải 2→3. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-CU-006 SAU-TAI`. phiên bản 4→5 | ✅ |
| B2 | BM-20260725-007 | R7-KC-S6-RecordB | Bấm tải 1 lần: phiên bản **giữ 2**, lượt tải 1→2. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-CU-007 SAU-TAI`. phiên bản 2→3 | ✅ |
| B3 | BM-20260725-008 | R7-EVID-S6-BM01 CTRL-khong-tai | Bấm tải 1 lần: phiên bản **giữ 4**, lượt tải 2→3. Lưu được: 1 khung *"Cập nhật biểu mẫu thành công"*, 1 request. Tên → `R9-CU-008 SAU-TAI`. phiên bản 4→5 | ✅ |

**Kết quả (B): 3/3 bản ghi cũ đều lưu được sau khi bấm tải.**

Ảnh danh sách xác nhận 5 tên đã đổi thật: `QLBMHD_OOS_01/image/danh-sach-ten-da-doi-sau-khi-tai-va-luu.png`

### (C) Chẩn đoán — 4 con số trước/sau cú bấm tải (chỉ để hiểu, không dùng chốt verdict)

| Bản ghi | phiên bản TRƯỚC | lượt tải TRƯỚC | phiên bản SAU | lượt tải SAU |
|---|---|---|---|---|
| BM-009 (A1) | 2 | 0 | **2 (không đổi)** | 1 |
| BM-010 (A4) | 1 | 0 | **1 (không đổi)** | 1 |

→ Trước fix (round 7): cú bấm tải đẩy phiên bản 2→3. Nay phiên bản **không đổi**, chỉ lượt tải tăng. Đúng bản chất "tải là thao tác chỉ đọc".

### ⚠️ Kiểm bẫy fix sai hướng — dev có bỏ luôn cơ chế chống ghi đè không?

| Thao tác | Kết quả | Kết luận |
|---|---|---|
| Gửi lệnh cập nhật BM-009 với số phiên bản cố tình cũ (gửi 2, phiên bản thật là 5) | **HTTP 409**, mã `ERR-STATE-LOCK-409`, thông báo *"Dữ liệu đã bị thay đổi bởi người dùng khác"*. Bản ghi **không** bị đổi (tên vẫn `R9-THU-A SAU-TAI-LAN3`, phiên bản vẫn 5) | ✅ Cơ chế chống ghi đè **VẪN CÒN hiệu lực**. Dev KHÔNG bỏ kiểm tra phiên bản — chỉ ngừng tăng phiên bản khi tải tệp |

### VERDICT QLBMHD_OOS_01: **Pass**
(A) 4/4 · (B) 3/3 · (C) cơ chế chống ghi đè còn nguyên → đủ cả 3 điều kiện Pass.

---

## IBMHD_OOS_01 (dòng 310) — Biểu mẫu → Nhập hàng loạt → bước 1 "Chọn file"

### Tệp dùng để đo — bản sao MỚI, đặt tên mới trong phiên này

`r9-ok-1.docx` (922 B) · `r9-ok-2.docx` (922 B) · `r9-loi.txt` (48 B, sai định dạng) · `r9-hong.docx` (3010 B, đúng đuôi nhưng nội dung hỏng).
Cả 4 tệp được đưa vào ô chọn tệp trong **một lần** (đúng kịch bản "chọn cùng lúc 4 tệp").
Bộ bắt thông báo cài **trước** khi chọn tệp; `soObserverDangSong = 1` ở mọi lượt.

### Lượt 1 & Lượt 2 — chọn cùng lúc cả 4 tệp

| Chỉ số | Lượt 1 | Lượt 2 | Giống nhau |
|---|---|---|---|
| Số dòng hiện trong danh sách tải lên | 3 (`r9-ok-1.docx`, `r9-ok-2.docx`, `r9-hong.docx` chữ đỏ) | 3 (y hệt) | ✅ |
| Nguyên văn dòng đếm | `Đã tải lên thành công: 2/4 · Có file lỗi` | y hệt | ✅ |
| Khu vực báo tệp bị loại | `1 tệp bị loại (không được tải lên)` → `r9-loi.txt — Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx)` | y hệt | ✅ |
| SO_KHUNG_THONG_BAO | 1 — *"Tệp không hợp lệ hoặc bị hỏng"* (của `r9-hong.docx`) | 1 — y hệt | ✅ |
| SO_REQUEST | 3 (3 lần gửi tệp lên) | 3 | ✅ |

**Điểm mấu chốt:** `r9-loi.txt` **không** có dòng trong danh sách tải lên, nhưng **có** khu vực riêng "1 tệp bị loại (không được tải lên)" nêu **đúng tên tệp + đúng lý do**. Mẫu số dòng đếm là **4** — bằng số tệp người dùng vừa chọn.

Ảnh: `IBMHD_OOS_01/image/luot1-buoc1-chon-4-tep-dem-2-tren-4-va-panel-r9-loi-txt-bi-loai.png`

### Đo tách bạch (thêm từng nhóm tệp một)

| Bước | Thao tác | Số dòng | Dòng đếm | Khu vực tệp bị loại | Số khung thông báo | Số request |
|---|---|---|---|---|---|---|
| a | Chọn 2 tệp hợp lệ | 2 | `Đã tải lên thành công: 2/2` | không có | 0 | 2 |
| b | Thêm riêng `r9-loi.txt` | 2 (không thêm dòng) | `Đã tải lên thành công: 2/3` ← **mẫu số tăng 2→3** | `1 tệp bị loại (không được tải lên)` · `r9-loi.txt — Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx)` | 0 | 0 |
| c | Thêm riêng `r9-hong.docx` | 3 (thêm dòng đỏ) | `Đã tải lên thành công: 2/4 · Có file lỗi` | giữ nguyên (vẫn chỉ `r9-loi.txt`) | 1 — *"Tệp không hợp lệ hoặc bị hỏng"* | 1 |

→ Tách bạch xác nhận: tệp sai định dạng bị loại **ngay tại máy người dùng** (0 request), nhưng vẫn **được đếm vào mẫu số** và **được nêu tên + lý do** ở khu vực riêng. Tệp hỏng thì đi lên máy chủ rồi mới báo lỗi, hiện dòng đỏ + 1 khung thông báo.

### Bước 2 "Kiểm tra" và bước 3 "Hoàn thành" (đo 2 lần, kết quả giống nhau)

| Màn | Số liệu đọc được |
|---|---|
| Bước 2 | `Tổng số file 4` · `Hợp lệ 2` · `Lỗi 2` · cảnh báo *"Có 2 tệp lỗi sẽ bị bỏ qua khi nhập"*. Bảng "Chi tiết file" liệt kê **đủ 4 dòng**, trong đó dòng 3 `r9-loi.txt · TXT · 48 B · Lỗi · Định dạng không hỗ trợ (chỉ chấp nhận .doc, .docx, .xls, .xlsx)` và dòng 4 `r9-hong.docx · DOCX · 2.9 KB · Lỗi · Tệp không hợp lệ hoặc bị hỏng` |
| Bước 3 | `Nhập biểu mẫu hoàn tất: 2 thành công / 2 lỗi`. Bảng "Chi tiết 2 tệp lỗi" nêu `r9-loi.txt · Chọn tệp · Định dạng không hỗ trợ...` và `r9-hong.docx · Tải lên · Tệp không hợp lệ hoặc bị hỏng` |

Ảnh: `IBMHD_OOS_01/image/buoc2-tong-4-hop-le-2-loi-2-bang-du-4-dong.png` · `IBMHD_OOS_01/image/buoc3-hoan-tat-2-thanh-cong-2-loi-neu-ten-tep.png` · `IBMHD_OOS_01/image/them-rieng-r9-loi-txt-dem-2-tren-3-panel-neu-ten-va-ly-do.png`

### VERDICT IBMHD_OOS_01: **Pass**
- Người dùng biết `r9-loi.txt` bị loại và vì sao → ✅ (khu vực "1 tệp bị loại (không được tải lên)" nêu đúng tên tệp + đúng lý do).
- Mẫu số dòng đếm bằng số tệp vừa chọn (4) → ✅ (trước đây là 3).
- Bước 2 / Kết quả vẫn đếm đúng (Tổng 4 · Hợp lệ 2 · Lỗi 2) → ✅.

> **Lưu ý cách đo — suýt chấm sai:** truy vấn DOM chỉ đếm dòng trong danh sách tải lên cho ra "3 dòng, `r9-loi.txt` biến mất" y như mô tả bug gốc. Chỉ khi **mở ảnh chụp ra đọc pixel** mới thấy khu vực "1 tệp bị loại" nằm **bên dưới dòng đếm**, ngoài danh sách tải lên. Đây là phần dev đã bổ sung.

