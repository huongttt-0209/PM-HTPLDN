# Bảng đối chiếu điều kiện — RE-VERIFY TMHDVMPL_OOS_01 (row 279) — sau khi dev báo đã sửa

**Kết luận:** Pass. Tệp đính kèm **trùng tên nay được tự động đổi tên** đúng dạng đặc tả quy định: nạp **cùng một tệp** `QA-trung-ten.docx` vào ô File đính kèm **3 lần liên tiếp** thì danh sách hiện `QA-trung-ten.docx` · `QA-trung-ten_1.docx` · `QA-trung-ten_2.docx` — mỗi tệp một tên riêng, đánh số tăng dần. Bấm **[Lưu]** rồi mở lại hồ sơ mới `HD-20260730-007`: đúng **3 tên khác nhau** như trên, không còn tệp trùng tên.

Đo ngày 30/07/2026 23:26–23:30, bản **HTPLDN · V1.0.3**, tài khoản `cbnv_tw_03`.

| Điều kiện có thể đổi kết quả | Phiếu gốc (TMHDVMPL_OOS_01, dòng QA tự mở) | Mình test lại (env nip.io, 30/07/2026 23:26–23:30) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw` — **CB Nghiệp vụ - Trung ương (CB_NV_TW)**, phạm vi **BTP · TW** | `cbnv_tw_03` — **CB Nghiệp vụ - Trung ương #03 (CB_NV_TW)**, phạm vi **BTP · TW**, đơn vị *Bộ Tư Pháp · Cục Bổ trợ tư pháp* | Không |
| Màn hình + thao tác kích hoạt | **Hỏi đáp pháp lý** → **[Thêm mới]** → mục **File đính kèm** (bước 1–5 của phiếu) | Đúng màn, đúng nút **[Thêm mới]**, đúng mục **File đính kèm** | Không |
| Tệp đem thử | `QA-trung-ten.docx` — **201 489 byte ≈ 196,8 KB**, docx hợp lệ, cỡ nhỏ để loại biến dung lượng | Dựng lại tệp **cùng tên, cùng cỡ 201 489 byte (196,8 KB)**, docx hợp lệ | Không |
| Cách gây trùng tên | Đưa **đúng một tệp** đó vào ô File đính kèm **2 lần** | Đưa **đúng một tệp** đó vào **3 lần** — 2 lần đầu **trùng khít** điều kiện phiếu gốc, lần thứ 3 là phần đo **thêm** để xem số thứ tự có tăng tiếp không | Không |
| Tên hiển thị trên danh sách tệp | 2 dòng **cùng tên** `QA-trung-ten.docx (196.8 KB)`, không dòng nào thành `_1` | `QA-trung-ten.docx` · `QA-trung-ten_1.docx` · `QA-trung-ten_2.docx` — mỗi dòng một tên, đánh số tăng dần đúng dạng `{tên}_{n}.{phần mở rộng}` | Không |
| Tên lưu xuống hồ sơ (đọc lại sau khi lưu) | Hồ sơ `HD-20260730-003` lưu **2 bản ghi cùng tên** `QA-trung-ten.docx`, cùng 201 489 byte | Hồ sơ mới `HD-20260730-007` lưu **3 tên khác nhau**: `QA-trung-ten.docx` · `QA-trung-ten_1.docx` · `QA-trung-ten_2.docx`, mỗi tệp *(196.8 KB)* | Không |
| Tên tệp lúc **tải về** (hệ quả mà phiếu gốc nêu) | Phiếu gốc nêu ảnh hưởng *"khi tải về sẽ có 2 tệp cùng tên trong cùng thư mục"* nhưng **không đo** | Bấm **[Tải]** trên tệp thứ hai của hồ sơ `HD-20260730-007` → tệp trả về mang đúng tên **`QA-trung-ten_1.docx`**, dung lượng 201 489 byte ⇒ tên đã đổi **đi theo tới lúc tải xuống**, không còn cảnh 2 tệp trùng tên trong cùng thư mục | Không |
| Bề mặt thứ hai — màn Chỉnh sửa | Không có trong phiếu gốc (phiếu gốc chỉ đo form Thêm mới) | Mở **[Sửa]** hồ sơ `HD-20260730-007` (đang có 3 tệp) rồi nạp lại **cùng tệp đó** → thành `QA-trung-ten_3.docx`. Quy tắc đổi tên chạy nhất quán trên cả hai màn | Không |

## Bằng chứng đã mở đọc

- `bug-reports/image/BUG-TMHDVMPL_OOS_01-r5-PASS-tu-doi-ten-_1-_2.png` — form *Thêm mới hỏi đáp* sau khi nạp cùng một tệp 3 lần: danh sách hiện **3 tên khác nhau** `QA-trung-ten.docx` / `QA-trung-ten_1.docx` / `QA-trung-ten_2.docx`, mỗi tệp *(196.8 KB)*, dòng tổng *"Tổng dung lượng 590.3 KB / 100MB"*.
- `bug-reports/image/BUG-TMHDVMPL_OOS_01-r5-PASS-ban-ghi-moi-luu-3-ten-khac-nhau.png` — hồ sơ `HD-20260730-007` sau khi lưu: mục **File đính kèm** đúng 3 tên khác nhau kèm nút *Xem / Tải*; góc phải **CB Nghiệp vụ - Trung ương #03 · CB_NV_TW · BTP · TW**; thanh bên **HTPLDN · V1.0.3**.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại hồ sơ sau khi lưu** (đúng bước 8 của phiếu, là phép thử quyết định vì bug gốc là *"lưu 2 tệp cùng tên y nguyên"*): `HD-20260730-007` có 3 tên khác nhau ⇒ đổi tên xảy ra thật ở dữ liệu lưu, không phải chỉ đổi nhãn trên giao diện.
- **Nạp thêm lần thứ 3** thay vì dừng ở 2 lần như phiếu gốc: số thứ tự tăng đúng `_1` → `_2`, chứng minh đây là **quy tắc đánh số**, không phải một chỗ vá cứng cho đúng trường hợp 2 tệp.
- **Đo nốt bước tải về** (bổ sung 31/07 00:16): bấm **[Tải]** → tên tệp nhận được là `QA-trung-ten_1.docx`. Đây là bước quyết định cho phần *ảnh hưởng* mà phiếu gốc nêu, trước đó mới chỉ suy ra từ tên đã lưu.
- **Đo trên bề mặt thứ hai** (màn Chỉnh sửa): tệp thứ 4 thành `_3` ⇒ quy tắc nhất quán, không chỉ có ở form Thêm mới.
- **Đối chiếu đặc tả** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md`):
  - `:1070` (SCR-II-01, thành phần 45 *File đính kèm*) — *"Trùng tên: tự động đổi tên `{name}_1.{ext}`"* ⇒ khớp đúng dạng tên đang thấy.
  - Bảng Error Handling của FR-II-01 không có mã lỗi cho tình huống trùng tên ⇒ đặc tả chọn xử lý im lặng bằng đổi tên; đúng như quan sát: **không** có thông báo lỗi nào khi nạp tệp trùng tên.

## Pass đối kháng (tự bác trước khi ghi sheet)

1. *"Có thể giao diện đổi nhãn cho đẹp, còn dữ liệu vẫn lưu trùng tên."* — Bác: mở lại hồ sơ sau khi lưu, đọc mục File đính kèm — 3 tên khác nhau. Đây là dữ liệu đã lưu, không phải danh sách tạm lúc soạn.
2. *"Có thể hệ thống chặn tệp trùng tên thay vì đổi tên (sửa quá tay)."* — Bác: cả 3 tệp **đều vào danh sách** và **đều được lưu**; không có thông báo từ chối nào. Đúng cách xử lý mà đặc tả chọn.
3. *"Có thể chỉ đúng khi trùng 2 tệp."* — Bác: thử tới tệp thứ 3 (`_2`) và tệp thứ 4 ở màn Chỉnh sửa (`_3`) — đánh số tăng đều.
4. *"Có thể đo trên bản cũ."* — Bác: đo trên **hồ sơ tạo mới hoàn toàn** `HD-20260730-007` (23:27 ngày 30/07/2026), bản **V1.0.3** hiện hành, cùng phiên đã xác nhận 2 chốt kiểm khác của cùng ô File đính kèm đều đã đổi hành vi.

## Giới hạn còn lại (khai báo minh bạch — không giấu)

- **Chỉ thử trùng tên bằng cùng một tệp.** Chưa thử trường hợp 2 tệp **khác nội dung nhưng trùng tên** — phiếu gốc cũng dựng bằng cùng một tệp nên điều kiện đã khớp, nhưng ghi lại để ai cần thì mở lượt kiểm riêng.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Màn *Chỉnh sửa hỏi đáp* vẫn in dòng gợi ý cũ và thiếu chỉ số tổng dung lượng** — trùng với ghi nhận ở [TMHDVMPL_12-r5-reverify.md](TMHDVMPL_12-r5-reverify.md) và [TMHDVMPL_16-r5-reverify.md](TMHDVMPL_16-r5-reverify.md). Hành vi (đổi tên, chặn định dạng, chặn tổng dung lượng) đều đúng; chỉ còn phần **chữ hiển thị**. Đề xuất gộp 1 phiếu riêng cho màn Chỉnh sửa.
- 🔴 **Phát hiện thêm ngoài phiếu (kiểm chứng lại 31/07/2026 00:35) — bấm [Hủy] ở màn Chỉnh sửa nhưng tệp vừa nạp VẪN được lưu vào hồ sơ.** Trong lượt đo trước tôi đã ghi nhầm rằng lần nạp thứ 4 *"đã hủy, không lưu"*; khi mở lại hồ sơ để đo bước tải về thì thấy `HD-20260730-007` **có 4 tệp** (có cả `QA-trung-ten_3.docx`) ⇒ ghi nhận cũ là **sai**. Đã dựng lại phép thử có chủ đích để chốt: mở **[Sửa]** hồ sơ → nạp `QA-r5-hople.docx` (934 B) → bấm **[Hủy]** (KHÔNG bấm [Đồng ý]) → panel đóng **không hề hỏi lại về thay đổi chưa lưu** → thoát ra danh sách, mở lại hồ sơ: **5 tệp**, tệp vừa nạp đã nằm trong hồ sơ. Tức tệp được ghi vào hồ sơ **ngay lúc nạp**, nút [Đồng ý] không còn là điểm quyết định lưu — trong khi `srs-fr-02-hoi-dap.md:1070` (thành phần 47 *Nút Lưu*) đặt hành vi *"Sửa: UPDATE"* ở nút Lưu. Ảnh: `../bug-reports/image/BUG-TMHDVMPL_OOS_01-r6-ngoai-pham-vi-huy-chinh-sua-van-luu-tep.png`. **Không dùng để mở lại phiếu này** (phiếu chỉ nói về việc đặt tên khi trùng, và việc đó đã đúng) — đề xuất mở phiếu riêng, gộp chung với phần chữ hiển thị còn sót ở màn Chỉnh sửa.
- **Bản ghi tạo trong phiên này:** `HD-20260730-007` (*Mới*). Sau các phép đo ở trên hiện có **5 tệp**: `QA-trung-ten.docx` / `_1` / `_2` / `_3` (4 tệp cùng nội dung, dùng để đo quy tắc đánh số) và `QA-r5-hople.docx` (nạp trong phép thử [Hủy] nói trên). Giữ nguyên làm vết kiểm chứng, không xóa.
