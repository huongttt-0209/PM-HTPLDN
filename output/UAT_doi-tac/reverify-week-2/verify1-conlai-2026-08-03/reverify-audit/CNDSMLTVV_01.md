# CNDSMLTVV_01 — evidence audit (verify vòng 1, 2026-08-03)

## 0. Note CŨ của dev ở cột R (backup TRƯỚC khi đè)

> **R124 (DEV phản hồi lần 1) — giá trị cũ:** (TRỐNG — dev không để lại note)
> **P124 (Trạng thái dev fix 1) — giá trị hiện tại:** `dev done` (KHÔNG đụng vào cột P)

---

## 1. Verdict

**`Pass`** — ghi vào cột `Verify` (Q124). Giữ nguyên P124 = `dev done`.

Dev claim `dev done` mà không giải trình (R124 trống) → theo nguyên tắc **KHÔNG TIN DEV**, đã tự test lại toàn bộ luồng. Kết quả: chức năng chạy đúng SRS, lỗi đối tác báo không tái hiện, và dấu vết trên bản dựng cho thấy đây là fix có thật (modal đầy đủ, kèm đúng câu xác nhận mà đối tác kỳ vọng) chứ không phải "may mà không tái hiện".

Vì sao **không** phải `Resolved`: `Resolved` dành cho ca P=`Reject` (dev phủ nhận bug) mà QA không tái hiện được. Ở đây dev nhận đã sửa (`dev done`) và QA xác nhận bản hiện tại chạy đúng → đúng định nghĩa `Pass`. (Ghi chú kỹ thuật: dropdown cột Q của tab tuần 2 cũng không có option `Resolved`.)

---

## 2. Cổng 1 — bằng chứng đối tác

- **File:** `partner-evidence/CNDSMLTVV_01.jpg` (md5 `e8ddedb37f62ddad54239ad15c4b6c83`, 304.540 bytes — **không** trùng md5 với ảnh nào khác trong đợt). Đã mở full-res bằng Read tool.
- **3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**
  - (a) **URL/bản ghi:** `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach` — màn danh sách TVV (SCR-IV-01), tab "Đang hoạt động", phân trang "1-10 / 10 mục".
  - (b) **Trạng thái entity:** mọi dòng nhìn thấy đều badge xanh "Đang hoạt động" — `TVV-BTP-TW-0030` (huongcg), `TVV-BTP-TW-0029` (hương tvv1), `TVV-BTP-TW-0006`, `TVV-BTP-TW-0004`, `TVV-BTP-TW-0002`.
  - (c) **Tiền đề / vai trò:** góc phải "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW". Cột "Công khai" nằm ngoài vùng cuộn ngang nên ảnh không hiển thị — tiền đề "chưa công khai" lấy từ cột H của phiếu.

## 3. Cổng 2 — hiểu bug (3 dòng)

1. **Evidence đã xem:** `CNDSMLTVV_01.jpg`, vùng chứa LỖI = dải toast đỏ phía trên đầu trang danh sách. Lỗi thấy trong ảnh: thông báo *"Mô tả công khai là bắt buộc trước khi đẩy lên Cổng pháp luật quốc gia"* bắn ra **trên nền màn danh sách, không có hộp thoại nào đang mở**.
2. **Đối tác phản ánh CỤ THỂ:** bấm "Công khai hàng loạt" → hệ thống **không mở cửa sổ nhập mô tả**, mà bắn thẳng thông báo lỗi thiếu mô tả. Kỳ vọng: mở cửa sổ nhập mô tả (bắt buộc) + câu xác nhận "Công khai {N} tư vấn viên đã chọn lên Cổng pháp luật quốc gia?".
3. **Data + bước tái hiện:** TVV trạng thái "Đang hoạt động" và chưa công khai → tab "Đang hoạt động" → tích chọn nhiều dòng → "Công khai hàng loạt" → Xác nhận.

> **Nhận xét về tính hợp lý của báo cáo:** claim của đối tác tự nhất quán. `ERR-CK-02` (SRS :682) là lỗi *thiếu mô tả công khai*, mà mô tả theo SRS :656 **chỉ nhập được trong modal MD-CONG-KHAI**. Nếu modal không mở thì người dùng không có đường nào cung cấp mô tả ⇒ nếu tái hiện được thì đây đúng là lỗi chặn luồng hợp lệ. Đây là lý do phải test tới cùng chứ không dừng ở "dev bảo xong rồi".

## 4. Cổng 3 — đối chiếu SRS vs web (đo LIVE)

Môi trường: `https://18.143.165.120.nip.io`, bản dựng **HTPLDN · V1.0.5**, ngày 03/08/2026.
Tài khoản: **`cbnv_tw_02`** (CB Nghiệp vụ - Trung ương #02, `CB_NV_TW`, BTP·TW, có quyền `publish_tu_van_vien`). Không dùng admin.

| # | SRS yêu cầu (dẫn dòng) | Thực tế web | Đạt? |
|---|---|---|:-:|
| 1 | `:1464` SCR-IV-01 — "Công khai hàng loạt" (tab Đang hoạt động): chọn nhiều dòng → nút "Công khai lên Cổng pháp luật quốc gia" → **mở MD-CONG-KHAI** | Tích 2 dòng → thanh hành động hiện "Công khai lên Cổng PLQG" → bấm → **modal "Công khai hàng loạt lên Cổng PLQG" mở ra** | ✅ |
| 2 | `:1406` MD-CONG-KHAI (a) — **Form nhập**: "Mô tả công khai", text dài, **bắt buộc**, max 5000 ký tự | Modal có ô "Mô tả công khai" gắn dấu `*` đỏ, `textarea maxLength=5000`, bộ đếm "0 / 5000" | ✅ |
| 3 | `:656` FR-IV-08 Input #4 — `mo_ta_cong_khai` bắt buộc khi CONG_KHAI, nguồn = **CB Nghiệp vụ nhập trong modal MD-CONG-KHAI** | Bỏ trống → chặn ngay trong modal: viền đỏ + lỗi inline, **0 request · 0 khung thông báo**, modal không đóng | ✅ |
| 4 | `:1406` MD-CONG-KHAI (c) — cảnh báo về hiển thị trên Cổng pháp luật quốc gia | Modal ghi: "Sau khi công khai, các hồ sơ được đánh dấu công khai ngay. Cổng PLQG sẽ tự động kéo dữ liệu công khai định kỳ để hiển thị." (khớp mô hình KÉO, BR-PUBLIC-01 `:664`) | ✅ |
| 5 | `:664` Processing bước 2 — lưu mô tả, đặt `cong_khai = 1`, chuyển trạng thái Công khai | `POST /api/v1/tu-van-viens/batch-cong-khai` → **200**, body `{"success":true,"data":{"results":[{...,"laCongKhai":true},{...,"laCongKhai":true}]}}`; cột Công khai của cả 2 dòng đổi "Chưa công khai" → **"Công khai"** | ✅ |
| 6 | `:666` Processing bước 4 — hỗ trợ thao tác hàng loạt | 1 request duy nhất xử lý cả 2 `ids`, request body `{"ids":[...2 id...],"hanh_dong":"CONG_KHAI","publishDto":{"moTaCongKhai":"..."}}` | ✅ |
| 7 | Kỳ vọng đối tác (cột K) — câu xác nhận "Công khai **{N}** tư vấn viên đã chọn lên Cổng pháp luật quốc gia?" *(SRS silent, chỉ là kỳ vọng)* | Modal hiển thị **nguyên văn**: "Công khai **2** tư vấn viên đã chọn lên Cổng pháp luật quốc gia?" | ✅ |
| 8 | `:1558` SCR-IV-03 — nút "Công khai" ở header màn chi tiết cũng mở MD-CONG-KHAI (form mô tả + file đính kèm) | Màn chi tiết `TVV-SEED-0001` → nút "Công khai lên Cổng PLQG" → modal `Công khai TVV "Nguyễn Văn Seed" lên Cổng PLQG`, có ô mô tả **và** vùng "Tệp đính kèm (tùy chọn)" | ✅ |
| 9 | `:1465` — hủy công khai vẫn **giữ lại** `mo_ta_cong_khai` để tái công khai không phải nhập lại | Sau khi hủy công khai rồi mở lại modal, ô mô tả **tự điền sẵn** đúng nội dung đã nhập trước đó (95 ký tự) | ✅ |

**Kết luận Cổng 3: 9/9 đạt.** Lỗi đối tác phản ánh **không tái hiện** — modal mở đúng, đúng thứ tự luồng, và chính câu xác nhận đối tác mong đợi cũng đã có.

## 5. Phép đo (bộ bắt thông báo dùng chung `tools/toast-capture.js`, KHÔNG tự viết observer)

Tự kiểm trước mỗi lô đo: `soObserverDangSong = 1` (hợp lệ) — đo 2 lần, một lần ở màn danh sách, một lần sau SPA-navigate sang màn chi tiết.

| Thao tác | SO_REQUEST | SO_KHUNG_THONG_BAO | Chữ hiển thị | Lặp? |
|---|:-:|:-:|---|:-:|
| Bấm "Công khai" khi **bỏ trống** mô tả | **0** | **0** | — (chặn bằng lỗi inline trong modal) | Không |
| Bấm "Công khai" sau khi **nhập** mô tả | **1** | **1** | "Đã công khai tư vấn viên thành công" | Không |
| Bấm "Hủy công khai" (bước seed) | **1** | **1** | "Đã hủy công khai tư vấn viên thành công" | Không |

Không có hiện tượng thông báo lặp trong toàn phiên. `list_console_messages` (error+warn): **rỗng**.

Lỗi inline khi bỏ trống mô tả: `["Vui lòng nhập mô tả công khai", "Mô tả công khai không được để trống"]`.

## 6. Ảnh — đã lưu VÀ đã mở đọc (postmortem A2)

| Ảnh | Nội dung đã đọc được |
|---|---|
| `image/CNDSMLTVV_01-01-truoc-khi-bam.png` | "Đã chọn 2 mục"; 2 checkbox tích xanh ở `TVV-STP-AG-0001` và `TVV-SEED-0001`; cả 2 cột Trạng thái "Đang hoạt động"; nút "Công khai lên Cổng PLQG" hiện trên thanh hành động; góc phải "CB Nghiệp vụ - Trung ương #02 · CB_NV_TW", "BTP · TW" |
| `image/CNDSMLTVV_01-02-ngay-sau-khi-bam.png` | **Modal MD-CONG-KHAI đã mở**: tiêu đề "Công khai hàng loạt lên Cổng PLQG"; dòng xanh "Công khai 2 tư vấn viên đã chọn lên Cổng pháp luật quốc gia?"; ô "* Mô tả công khai" rỗng, bộ đếm "0 / 5000"; 2 nút "Hủy" / "Công khai" |
| `image/CNDSMLTVV_01-03-bam-cong-khai-de-trong-mo-ta.png` | Ô mô tả viền **đỏ**, 2 dòng lỗi đỏ "Vui lòng nhập mô tả công khai" + "Mô tả công khai không được để trống"; modal **vẫn mở**, không có toast |
| `image/CNDSMLTVV_01-04-sau-khi-cong-khai-thanh-cong.png` | Modal đã đóng, danh sách được nạp lại, bỏ chọn hết; 5 dòng đều "Đang hoạt động" |
| `image/CNDSMLTVV_01-05-seed-modal-huy-cong-khai.png` | Bước seed — sau khi bấm "Hủy công khai": **không có hộp thoại xác nhận nào**, danh sách nạp lại luôn |
| `image/CNDSMLTVV_01-06-loi-vao-2-man-chi-tiet.png` | Modal ở màn chi tiết: `Công khai TVV "Nguyễn Văn Seed" lên Cổng PLQG`; ô mô tả **tự điền sẵn** 95/5000; vùng "Tệp đính kèm (tùy chọn)" — "Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp" |

## 7. Dữ liệu — đã khôi phục nguyên trạng

| Bản ghi | Trước test | Sau các bước test | Sau khi khôi phục |
|---|---|---|---|
| `TVV-STP-AG-0001` (`4c1d3aab-…`) | Chưa công khai | Công khai | **Chưa công khai** ✅ (gọi `HUY_CONG_KHAI`, HTTP 200, `laCongKhai:false`) |
| `TVV-SEED-0001` (`5eed0003-…`) | Chưa công khai | Công khai → hủy công khai (bước seed cho lối vào 2) | **Chưa công khai** ✅ |

Không để lại bản ghi rác, không tạo mới bản ghi nào.

## 8. Lỗi phát hiện thêm NGOÀI phạm vi case (postmortem C1 — phải log, không được lờ)

### 8.1 🔴 "Hủy công khai hàng loạt" thực thi ngay, KHÔNG có bước xác nhận

- **SRS `:1465`** (SCR-IV-01): *"**Hủy công khai hàng loạt** (tab "Đang hoạt động"): chọn dòng đã công khai → nút "Hủy công khai" → **MD-HUY-CONG-KHAI** → đặt `cong_khai = 0` + chuyển trạng thái Hủy công khai"*.
- **SRS `:1407`** định nghĩa MD-HUY-CONG-KHAI: tiêu đề *"Xác nhận hủy công khai?"*, nội dung *"Thông tin **{tên}** sẽ bị gỡ khỏi Cổng pháp luật quốc gia…"*, nút primary *"Hủy công khai"*.
- **Thực tế đo được:** tích 1 dòng → bấm "Hủy công khai" → **không hộp thoại nào mở** (`coModal: false`), đi thẳng `POST /api/v1/tu-van-viens/batch-cong-khai` → 1 toast "Đã hủy công khai tư vấn viên thành công", cột Công khai đổi ngay sang "Chưa công khai". Bằng chứng: `image/CNDSMLTVV_01-05-seed-modal-huy-cong-khai.png`.
- **Vì sao đáng lo hơn bug gốc:** đây là thao tác **gỡ dữ liệu khỏi Cổng pháp luật quốc gia**, tác động ra ngoài phạm vi hệ thống và áp hàng loạt, lại không có bước xác nhận nào — bấm nhầm là mất công khai ngay. Trong khi chiều ngược lại (công khai) thì có tới 2 lớp: modal + trường bắt buộc.
- Phát hiện trong lúc **seed**, đúng loại lỗi mà postmortem Tầng 3 chỉ ra là hay bị bỏ qua vì "không thuộc case nào".

### 8.2 ⚠️ Modal công khai HÀNG LOẠT thiếu vùng "Tệp đính kèm", modal ở màn CHI TIẾT lại có

- **SRS `:1406`** MD-CONG-KHAI mục (b): *"**File đính kèm** — PDF/DOC/DOCX/XLS/XLSX, max 20MB/file, nhiều file, tùy chọn"*; **SRS `:657`** liệt kê `file_dinh_kem_cong_khai` là Input #5 của FR-IV-08.
- **Đo được:** modal hàng loạt → `soVungUploadFile: 0`, `soInputFile: 0`. Modal màn chi tiết → `soVungUpload: 2`, `soInputFile: 1`, `accept = ".pdf,.doc,.docx,.xls,.xlsx"`.
- Có thể là chủ đích (file là "giới thiệu **cá nhân**" nên không áp hàng loạt được), nhưng SRS không tách 2 trường hợp ⇒ nếu log thì thuộc nhánh cần BA chốt, không phải lỗi hiển nhiên.

### 8.3 ⚠️ Một trường sinh 2 thông báo lỗi trùng nghĩa cùng lúc

Bỏ trống "Mô tả công khai" → hiện đồng thời "Vui lòng nhập mô tả công khai" **và** "Mô tả công khai không được để trống". Hai lớp kiểm tra cùng bắn. Mức độ nhẹ (giao diện), nhưng là dấu hiệu quy tắc kiểm tra bị khai báo trùng.

> Cả 3 mục trên **chưa** mở dòng TC mới trên sheet — đang chờ quyết định, vì mở dòng TC là ghi thêm dữ liệu vào sheet làm việc.
