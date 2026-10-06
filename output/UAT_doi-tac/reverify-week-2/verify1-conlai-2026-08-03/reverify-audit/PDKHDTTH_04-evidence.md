# PDKHDTTH_04 — Cổng 1 + Cổng 2 (AGENT-EVIDENCE, 2026-08-03)

> Sheet: `UAT_TGPL Doanh Nghiệp-tuần 2` row **120** · `fetch_evidence.py` **exit 0** (1 link Drive, tải được `PDKHDTTH_04.jpg`, 243.878 bytes, 1859×1036).
> Ô "Ảnh/video 2" (cột T) **trống**.
>
> 🔴 **CẢNH BÁO CỔNG 2 CHƯA ĐÓNG TRỌN:** evidence là **ảnh tĩnh chụp SAU sự việc**, **KHÔNG bắt được thao tác bấm "Phê duyệt"** và **KHÔNG bắt được (sự vắng mặt của) thông báo**. Chi tiết ở mục Cổng 2 (1).

## Cổng 1 — 3 dữ kiện neo

**(a) URL / mã bản ghi đối tác đang đứng**
- **`htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/14fb293e-ae76-49e5-9e42-a6dee7f98400`**
- Màn: `Đào tạo, tập huấn → Kế hoạch đào tạo → Chi tiết`.
- Bản ghi: **`KH-20260725-0002`** — tên **"Test phê duyệt không cùng cấp"**.

**(b) Trạng thái entity**
- Badge góc phải tiêu đề: **`Chờ duyệt`** (nền xanh nhạt).
- Stepper: `✓ Nháp — **(2) Chờ duyệt** — 3 Đã duyệt — 4 Đã công khai` → đang đứng **bước 2 · Chờ duyệt**.
- Trong bảng "Thông tin kế hoạch": `Trạng thái = Chờ duyệt`.

**(c) Dữ liệu tiền đề**
Bảng "Thông tin kế hoạch" đọc được đầy đủ:
| Trường | Giá trị |
|---|---|
| Mã kế hoạch | `KH-20260725-0002` |
| Tên kế hoạch | `Test phê duyệt không cùng cấp` |
| Năm | `2026` |
| Thời gian bắt đầu | `01/07/2026` |
| Thời gian kết thúc | `31/08/2026` |
| Ngân sách dự kiến | `0 VNĐ` |
| Trạng thái | `Chờ duyệt` |
| Nguồn lực | `—` |
| Ghi chú | `—` |

- 🔴 **`Đơn vị lập` / `Người lập` / `Cấp` của kế hoạch: KHÔNG ĐỌC ĐƯỢC** — bảng "Thông tin kế hoạch" **không có** trường nào cho biết kế hoạch thuộc đơn vị/cấp nào. Vì vậy **không thể xác nhận từ ảnh** rằng đây đúng là tình huống "khác cấp với người lập"; chỉ có **tên kế hoạch** ("Test phê duyệt không cùng cấp") gợi ý ý đồ test đó.
- **Phần thân trang bên dưới card thông tin là một dải trắng RỖNG HOÀN TOÀN** — đã crop phóng to ×2 (`crop-bottom-panel.png`): **không có nút `Phê duyệt`, không có nút `Từ chối`, không có dòng chữ / cảnh báo / banner nào**.

## Cổng 2 — 3 dòng

**(1) Evidence đã xem + frame chứa LỖI**
`partner-evidence/PDKHDTTH_04.jpg` — ảnh tĩnh full-res 1859×1036, chụp **10:41 AM 2026-07-25**. Đã đọc bản gốc + 3 vùng crop phóng to.

**Ảnh này KHÔNG phải "frame chứa thao tác lỗi".** Nó chỉ chứng minh **trạng thái màn hình**:
> ở vai trò `CB_PD_TW`, trên kế hoạch `KH-20260725-0002` đang `Chờ duyệt`, màn Chi tiết **không render bất kỳ nút hành động nào (Phê duyệt/Từ chối)** và **không có thông báo/giải thích nào** trên trang.

Ảnh **KHÔNG** chứa: (i) khoảnh khắc bấm nút "Phê duyệt", (ii) toast/dialog/response của thao tác đó, (iii) trường cho biết kế hoạch thuộc đơn vị/cấp nào. **Đây là claim dạng "absence" (phải báo lỗi X nhưng không báo") — theo §GATE của protocol, artifact hợp lệ bắt buộc là *tự chạy đúng thao tác + chứng minh observer/network/explainErrors đều RỖNG*, thứ mà ảnh tĩnh này không cung cấp.** Người verify **phải tự chạy lại thao tác** mới đóng được Cổng 2; nếu không dựng lại được điều kiện "khác cấp" thì để **verdict TRỐNG**.

**(2) Đối tác phản ánh CỤ THỂ gì**
Khi **Cán bộ phê duyệt KHÁC CẤP với người lập** bấm **`Phê duyệt`**, hệ thống **không hiển thị thông báo cho người dùng biết lý do không phê duyệt được**. Kết quả mong đợi ghi ở sheet là hệ thống **từ chối kèm thông báo** *"Không có quyền phê duyệt kế hoạch này"*. Vậy tranh chấp nằm ở **có/không có phản hồi giải thích**, không phải ở nội dung chuỗi cụ thể.

**(3) Data + bước tái hiện chính xác**
1. Dựng 1 kế hoạch đào tạo do **người lập ở CẤP KHÁC** với cán bộ phê duyệt sẽ dùng (đối tác đặt tên `Test phê duyệt không cùng cấp`, mã `KH-20260725-0002`, năm 2026, 01/07/2026 → 31/08/2026, ngân sách 0 VNĐ, nguồn lực & ghi chú để trống).
2. Đưa kế hoạch về state **`Chờ duyệt`** (stepper bước 2).
3. Đăng nhập **`CB_PD_TW` — Cán bộ PD Trung ương, đơn vị `BTP · TW`** (nhóm tài khoản sheet `cbpd_tw`).
4. `Đào tạo, tập huấn` → `Kế hoạch đào tạo` → mở chi tiết kế hoạch đó (URL dạng `/dao-tao/ke-hoach/<uuid>`).
5. Tìm nút **`Phê duyệt`** (sheet ghi bấm từ màn danh sách; ảnh đối tác cho thấy màn **chi tiết** không có nút) → bấm → **cài `tools/toast-capture.js` TRƯỚC khi bấm**, đếm **số request kèm số thông báo**.
6. Nếu không tìm thấy nút ở cả danh sách lẫn chi tiết → đó chính là quan sát cần ghi (hệ thống ẩn nút mà không giải thích).

## Vai trò / tài khoản đối tác dùng

**`Cán bộ PD Trung ương` — mã `CB_PD_TW`, đơn vị `BTP · TW`** (đọc rõ ở header phải, đã crop ×2: `crop-header-right.png`). Badge thông báo `56`. Nhóm tài khoản sheet: **`cbpd_tw`**.

## Ghi chú cho người verify

- 🔴 **Tiền đề khó nhất & bắt buộc: "khác cấp với người lập".** Ảnh **không** cho biết kế hoạch `KH-20260725-0002` do đơn vị/cấp nào lập. Muốn đóng GAP: dựng kế hoạch bằng tài khoản **`cbnv_bn`** (cấp Bộ ngành) hoặc **`cbnv_dp`** (cấp Địa phương), trình duyệt lên `Chờ duyệt`, rồi mới đăng nhập **`cbpd_tw`** để bấm duyệt. **Không được** dùng kế hoạch do `cbnv_tw` lập — cùng cấp thì mất điều kiện đối tác.
- 🔴 **Đây là claim dạng "absence"** → theo protocol phải **tự chạy đúng thao tác** rồi chứng minh observer/network rỗng. **CẤM** dùng `tools/toast-capture.js` bản tự chế có lọc trùng, **CẤM** đọc chữ bằng `textContent`.
- **Chú ý 2 bề mặt khác nhau:** sheet ghi bước *"Bấm nút Phê duyệt"* ở màn **Kế hoạch đào tạo (danh sách)**; ảnh đối tác lại là màn **Chi tiết** và ở đó **không có nút nào**. Phải kiểm **cả hai**: cột `Hành động` ngoài danh sách **và** thân màn chi tiết. Nếu nút chỉ ẩn ở chi tiết mà vẫn có ngoài danh sách thì bản chất sự việc khác hẳn mô tả.
- Phản hồi dev ở sheet (cột P=`Reject`, cột R): *"BE đã chặn phê duyệt khác đơn vị + trả message VN rõ 'Người duyệt phải cùng đơn vị với kế hoạch'; FE hiển thị toast đúng end-to-end. SRS không ép chuỗi message cụ thể."* → **Lưu ý dev nói "khác ĐƠN VỊ" còn TC nói "khác CẤP" — hai khái niệm không đồng nhất.** Nếu người verify chỉ dựng "khác đơn vị cùng cấp" thì chưa chắc trúng điều kiện đối tác. Nên hỏi rõ hoặc test cả 2 biến thể.
- Ảnh chụp trên **trình duyệt khác** với 4 case còn lại (thanh bookmark tiếng Hàn, nút "Hỏi AI" — Microsoft Edge), tức máy/profile khác. Không ảnh hưởng nghiệp vụ, chỉ ghi nhận.

## File evidence + vùng crop đã dùng

| Loại | Đường dẫn tuyệt đối |
|---|---|
| Ảnh gốc (duy nhất) | `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/partner-evidence/PDKHDTTH_04.jpg` |
| Crop dải trắng dưới card (chứng minh **không có nút / không có thông báo**) | `…/verify1-conlai-2026-08-03/frames/PDKHDTTH_04/crop-bottom-panel.png` |
| Crop header phải (vai trò `CB_PD_TW`, đơn vị `BTP · TW`, badge `Chờ duyệt`) | `…/verify1-conlai-2026-08-03/frames/PDKHDTTH_04/crop-header-right.png` |
| Crop tiêu đề + stepper | `…/verify1-conlai-2026-08-03/frames/PDKHDTTH_04/crop-title-stepper.png` |

## Ngoài lỗi đối tác nêu, trong ảnh còn thấy gì bất thường? (dựa trên ảnh ĐÃ ĐỌC)

1. **Bảng "Thông tin kế hoạch" thiếu hẳn thông tin chủ thể**: không có `Đơn vị lập`, `Người lập`, `Cấp`, `Ngày trình duyệt`. Với một màn phê duyệt, người duyệt **không có cách nào biết kế hoạch của ai** để quyết định — đây là thiếu sót hiển thị độc lập với lỗi đối tác nêu, và cũng chính là thứ khiến ảnh không kiểm chứng được điều kiện "khác cấp".
2. **Màn chi tiết ở state `Chờ duyệt` mà vai trò phê duyệt không có BẤT KỲ nút hành động nào** — không `Phê duyệt`, không `Từ chối`, không `Quay lại`/`In`. Dải trắng dưới card là một khối rỗng (đã crop ×2 xác nhận). So sánh: màn Chi tiết khoá học (case KTDGKQHT_02) vẫn có `Công khai`/`Kết thúc`.
3. **`Ngân sách dự kiến = 0 VNĐ`** trong khi các kế hoạch khác cùng môi trường đều có ngân sách hàng trăm triệu → nhiều khả năng là data test, nhưng cũng cho thấy hệ thống cho phép trình duyệt kế hoạch ngân sách 0.
4. **Stepper màn kế hoạch chỉ có 4 bước** (`Nháp → Chờ duyệt → Đã duyệt → Đã công khai`) — **không có bước `Từ chối`**, dù danh sách ở case QLLKHDTBD_09 có tab trạng thái `Từ chối`. Trạng thái `Từ chối` không được biểu diễn trên stepper.

*(Tất cả đọc trực tiếp từ pixel ảnh + crop phóng to, không suy đoán. Chưa log bug — thuộc quyền người verify.)*
