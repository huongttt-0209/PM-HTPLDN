# Bảng đối chiếu điều kiện — RE-VERIFY TMHDVMPL_12 (row 277) — sau khi dev báo đã sửa

**Kết luận:** Pass. Ô **File đính kèm** của form **Thêm mới hỏi đáp** nay **từ chối** tệp `.jpg`: hiện thông báo nêu rõ lý do và danh sách định dạng được chấp nhận, tệp **không** vào danh sách, **không** có request tải tệp nào phát sinh, và bản ghi lưu xuống **không** chứa tệp ảnh. Dòng gợi ý dưới ô tải tệp cũng đã sửa đúng 5 định dạng tài liệu. Đã đo trên **bản ghi tạo mới** `HD-20260730-005` đi trọn luồng: nạp `.jpg` (bị chặn) → nạp `.docx` hợp lệ → bấm **[Lưu]** → mở lại bản ghi đọc kết quả.

Đo ngày 30/07/2026 23:05–23:12, bản **HTPLDN · V1.0.3**, tài khoản `cbnv_tw_03`.

| Điều kiện có thể đổi kết quả | Bug gốc (BUG-TMHDVMPL_12, Pass-bug-report-tuan-1-vong-dau.md) | Mình test lại (env nip.io, 30/07/2026 23:05–23:12) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, phạm vi **BTP · TW** | `cbnv_tw_03` — **CB Nghiệp vụ - Trung ương #03 (CB_NV_TW)**, phạm vi **BTP · TW**, đơn vị *Bộ Tư Pháp · Cục Bổ trợ tư pháp* | Không |
| Màn hình + thao tác kích hoạt | **Hỏi đáp pháp lý** → **[Thêm mới]** → mục **File đính kèm** (bước 2–4 của phiếu) | Đúng màn, đúng nút **[Thêm mới]**, đúng mục **File đính kèm** | Không |
| Tệp đem thử | **Duy nhất 1 tệp `.jpg`** — ảnh JPEG thật 400×300, 2,5 KB (đã kiểm bằng `file(1)`) | **Cùng đúng tệp đó** (`QA-r5-TMHDVMPL_12.jpg`, JPEG thật 400×300, 2 529 byte), nạp một mình để cô lập biến | Không |
| Cách nạp tệp | Chọn tệp qua hộp thoại của trình duyệt | Nạp thẳng vào ô chọn tệp, **cố ý đi vòng qua bộ lọc `accept`** của hộp thoại — tức là ép hệ thống phải tự kiểm chứ không dựa vào việc hộp thoại giấu tệp đi. Đây là điều kiện **chặt hơn** bug gốc: nếu hệ thống còn hở, cách này chắc chắn bắt được | Không |
| Dòng gợi ý hiển thị dưới ô tải tệp | *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx, **.jpg, .png**. Dung lượng tối đa: 20MB/tệp."* — sai so với đặc tả | *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp, **tổng 100MB**."* — khớp đặc tả, đã bỏ `.jpg/.png` và bổ sung mức tổng | Không |
| Định dạng ảnh còn lại (`.png`) — dòng gợi ý cũ liệt kê cả 2 | Phiếu gốc chỉ thử `.jpg`; dòng gợi ý sai thì liệt kê cả `.jpg` **và** `.png` | Thử nốt `.png` (PNG thật 40×30, 170 byte) trên cùng form *Thêm mới*: **cũng bị từ chối**, thông báo *"QA-r5-TMHDVMPL_12.png: Định dạng không được hỗ trợ. Chấp nhận: .pdf, .doc, .docx, .xls, .xlsx"*, danh sách rỗng, *Tổng dung lượng 0 B / 100MB* ⇒ chặn **cả hai** định dạng ảnh, không chỉ đúng cái phiếu nêu | Không |
| Đối chứng ngược — tệp hợp lệ vẫn phải lưu được | Không có trong bug gốc (bug gốc chỉ đo nhánh sai) | Nạp `QA-r5-hople.docx` (934 B) → vào danh sách bình thường, *Tổng dung lượng 934 B / 100MB*, bấm **[Lưu]** → tạo bản ghi thành công. Chứng minh chốt kiểm **lọc theo định dạng**, không phải chặn mù mọi tệp | Không |
| Đi hết luồng đến khi lưu + đọc lại bản ghi | Bug gốc: lưu xong bản ghi `HD-20260730-001` vẫn chứa tệp `.jpg` (`loai: image/jpeg`) kèm nút *Xem / Tải* | Bản ghi mới `HD-20260730-005`: mục **File đính kèm** chỉ có **`QA-r5-hople.docx` (0.9 KB)** — **không** có tệp ảnh nào | Không |

## Bằng chứng đã mở đọc

- `bug-reports/image/BUG-TMHDVMPL_12-r5-PASS-jpg-bi-tu-choi-dinh-dang.png` — **khoảnh khắc bị chặn** trên form *Thêm mới hỏi đáp*: sau khi nạp tệp `.jpg`, danh sách tệp **rỗng**, dòng tổng ghi *"Tổng dung lượng 0 B / 100MB"*, và dòng gợi ý đã sửa còn *".pdf, .doc, .docx, .xls, .xlsx … tổng 100MB"* (không còn `.jpg, .png`).
- `bug-reports/image/BUG-TMHDVMPL_12-r5-PASS-ban-ghi-moi-chi-luu-docx.png` — **kết quả sau khi đi hết luồng**: bản ghi `HD-20260730-005` (*Mới*), mục **File đính kèm** chỉ có `QA-r5-hople.docx (0.9 KB)`; góc phải là **CB Nghiệp vụ - Trung ương #03 · CB_NV_TW · BTP · TW**; thanh bên ghi **HTPLDN · V1.0.3**.
- `bug-reports/image/BUG-TMHDVMPL_12-r5-ngoai-pham-vi-form-chinh-sua-goi-y-con-jpg-png.png` — ảnh cho mục *Ngoài tiêu chí phiếu* bên dưới: form **Chỉnh sửa** vẫn in dòng gợi ý cũ có `.jpg, .png`, dù tệp `.jpg` nạp vào đó cũng đã bị từ chối.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại bản ghi sau khi lưu** (không chỉ nhìn giao diện lúc nạp tệp): mở `HD-20260730-005` → chỉ thấy `QA-r5-hople.docx`. Đây là phép thử quyết định, vì bug gốc chính là *"lưu được xuống hồ sơ thật"*.
- **Đếm request tải tệp**: cả phiên chỉ có **1** request tải tệp lên (`.../files` → **201**) ứng với tệp `.docx`; **không có** request nào cho tệp `.jpg` ⇒ tệp ảnh bị chặn **trước khi** rời trình duyệt, không phải bị máy chủ nhận rồi ẩn đi.
- **Bắt thông báo hiển thị** (bộ bắt cài trước thao tác, không lọc trùng): nạp `.jpg` → thông báo *"QA-r5-TMHDVMPL_12.jpg: Định dạng không được hỗ trợ. Chấp nhận: .pdf, .doc, .docx, .xls, .xlsx"*. Nghĩa là hệ thống **nêu rõ lý do từ chối**, đúng yêu cầu của phiếu.
- **Thử nốt định dạng còn lại**: không dừng ở `.jpg` của phiếu, mà nạp thêm `.png` — cũng bị từ chối cùng thông báo. Nếu dev chỉ vá riêng `.jpg` thì bước này đã bắt được.
- **Đối chứng ngược** (mục trong bảng trên): `.docx` hợp lệ vẫn nạp và lưu được ⇒ loại giả thuyết "dev chặn hết mọi tệp cho xong".
- **Đối chiếu đặc tả** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md`):
  - `:1070` (SCR-II-01, thành phần 45 *File đính kèm*) — *"Tối đa 10 file/lần, tổng tối đa 100MB, mỗi file tối đa 20MB. **Định dạng: doc/docx/xls/xlsx/pdf.**"* ⇒ cả hành vi lẫn dòng gợi ý trên form Thêm mới nay đều khớp.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Có thể chỉ hộp thoại chọn tệp giấu tệp `.jpg` đi, còn hệ thống vẫn nhận nếu kéo thả."* — Bác: đã **cố ý đi vòng qua bộ lọc của hộp thoại**, đưa thẳng tệp `.jpg` vào ô tải lên. Hệ thống vẫn tự kiểm và từ chối kèm thông báo.
2. *"Có thể chỉ giao diện không hiện tệp, nhưng máy chủ vẫn lưu."* — Bác: **0 request tải tệp** cho tệp `.jpg`, và bản ghi đọc lại sau khi lưu chỉ có `.docx`.
3. *"Có thể dev chặn mù mọi tệp."* — Bác bằng **đối chứng ngược**: `.docx` hợp lệ nạp và lưu bình thường.
4. *"Có thể chỉ đúng trên bản ghi cũ."* — Bác: đo trên **bản ghi tạo mới hoàn toàn** `HD-20260730-005` (23:09 ngày 30/07/2026), đi trọn luồng từ mở form đến lưu và đọc lại.

## Giới hạn còn lại (khai báo minh bạch — không giấu)

- **Chưa chụp được ảnh khung thông báo từ chối.** Thông báo này tự tắt rất nhanh và không lọt vào ảnh chụp màn hình dù đã thử 6 cách khác nhau (hẹn giờ, bắn lặp, chụp ngay sau thao tác). Bù lại đã có: **nguyên văn câu thông báo** do bộ bắt sự kiện ghi lại tại thời điểm nó xuất hiện, **danh sách tệp rỗng**, **dòng tổng 0 B**, **0 request tải tệp** và **bản ghi lưu xuống không có ảnh** — 4 bằng chứng độc lập cho cùng một kết luận.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Form *Chỉnh sửa hỏi đáp* vẫn in dòng gợi ý cũ.** Mở bản ghi → **[Sửa]**, mục **File đính kèm** vẫn ghi *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx, **.jpg, .png**. Dung lượng tối đa: 20MB/tệp."* (thiếu luôn mức tổng 100MB), và bộ lọc tệp của ô này vẫn liệt kê `.jpg,.png`. **Hành vi thì đã đúng**: nạp tệp `.jpg` vào đó cũng bị từ chối, thông báo *"File đính kèm chỉ chấp nhận định dạng: .doc, .docx, .xls, .xlsx, .pdf"*, tệp không vào danh sách. Nên đây là **lỗi chữ hiển thị còn sót ở màn Chỉnh sửa**, không phải lỗi cho lưu tệp sai định dạng.
  - **Vì sao vẫn để phiếu TMHDVMPL_12 là Pass:** phiếu gốc ghi rõ phạm vi là ô File đính kèm của **form Thêm mới**, và cả 3 gạch đầu dòng "Kết quả mong đợi" của phiếu đều đã thỏa trên form đó. Phần còn sót nằm ở **màn khác**, hành vi lại đã đúng ⇒ ghi lại ở đây để đề xuất mở phiếu riêng, không dùng để mở lại phiếu này.
  - Đặc tả liên quan: `srs-fr-02-hoi-dap.md:1070` (thành phần 45) mô tả cùng một ô File đính kèm cho cả hai chế độ Thêm mới và Sửa (thành phần 47 *Nút Lưu* gộp cả *"Thêm mới: INSERT"* và *"Sửa: UPDATE"*).
- **Bản ghi tạo trong phiên này:** `HD-20260730-005` (*Mới*, đính kèm 1 tệp `.docx` 934 B). Tạo có chủ đích để verify trên dữ liệu mới, không xóa để giữ vết kiểm chứng.
