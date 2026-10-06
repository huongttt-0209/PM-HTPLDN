# Bảng đối chiếu điều kiện — TTCTDTTH_16 (row 236) — CTĐT không tự chuyển sang "Đang thực hiện"

**Kết luận:** Open (Major). Tái hiện 1/1 bằng thao tác thật, cộng 1 ca dữ liệu cũ củng cố.

Phiếu ghi *"Chương trình ở trạng thái 'Đã duyệt' và có ít nhất 1 khóa học ở trạng thái 'Đang diễn ra'/'Đã công khai' nhưng hệ thống không tự động chuyển trạng thái của chương trình sang 'Đang thực hiện'"* → **TÁI HIỆN ĐÚNG**.

Tôi tự tay đưa một khóa học từ *Đã duyệt* sang *Đang diễn ra* bằng nút **[Khai giảng]** trên giao diện (không sửa dữ liệu trực tiếp), rồi mở lại chương trình cha: chương trình vẫn đứng ở bước **3 Đã duyệt**, bước **4 Đang thực hiện** chưa được kích hoạt. Mốc `ngayCapNhat` của chương trình **không đổi** (`2026-07-25T03:23:52.370Z`) ⇒ hệ thống không hề chạm tới bản ghi chương trình khi khóa học con đổi trạng thái.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TTCTDTTH_17.webm`, full-res) | Mình test (env nip.io, 30/07/2026 09:58–10:12) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Frame `t000.00s` góc phải: **Cán bộ NV Trung ương · CB_NV_TW**, phạm vi **BTP · TW** | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW (đúng vai trò + đúng cấp) | Không |
| Entity + **trạng thái** (state machine) | Khóa học `KH-20260722-002` ở bước **4 Đang diễn ra** (frame `t000.00s`); chương trình cha `CTDT-BTP-TW-2026-0012 — test` ở bước **3 Đã duyệt** (frame `t028.09s`) | Khóa học `KH-QAW7-HOINGHI` được tôi bấm **[Khai giảng]** → bước **4 Đang diễn ra**; chương trình cha `CTDT-QAW7-01` vẫn bước **3 Đã duyệt** | Không |
| Dữ liệu tiền đề | Chương trình đã duyệt, có ≥1 khóa học con đã qua duyệt và đang diễn ra | Dựng đúng cặp cha–con: `CTDT-QAW7-01` (Đã duyệt) ← `KH-QAW7-HOINGHI` (Đang diễn ra sau khi khai giảng). Ngoài ra còn 1 cặp dữ liệu cũ cùng dạng: `CTDT-SEED-0001` (Đã duyệt từ 30/06) ← `DDD-KH-011` (Đang diễn ra, cập nhật 16/07) | Không |
| Input / thao tác kích hoạt | Đối tác quay lại danh sách chương trình rồi mở chi tiết để xem trạng thái (frame `t012.04s` → `t028.09s`) | Bấm **[Khai giảng]** trên chi tiết khóa học (1 request `POST …/start`, 1 thông báo *"Đã khai giảng khóa học"*), rồi mở chi tiết chương trình cha + đọc lại bản ghi chương trình | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Thao tác/state)

- `partner-evidence/TTCTDTTH_17.webm` — đã mở đọc frame full-res. `t000.00s`: khóa học `KH-20260722-002` (chương trình ĐT = `CTDT-BTP-TW-2026-0012 — test`) đứng ở bước **4 Đang diễn ra**. `t012.04s`: danh sách chương trình, thẻ **Đã duyệt 12**, thẻ **Đang thực hiện KHÔNG có số** (0). `t028.09s` = **khoảnh khắc lỗi**: chi tiết `CTDT-BTP-TW-2026-0012` vẫn ở bước **3 Đã duyệt**, bước 4 Đang thực hiện chưa sáng.
- `reverify-audit/TTCTDTTH_16/01-baseline-ctdt-list-3-da-duyet.png` — đã mở đọc: nền trước khi thao tác, 3 chương trình, thẻ **Đã duyệt 3**, thẻ **Đang thực hiện** và **Hoàn thành** đều không có số.
- `reverify-audit/TTCTDTTH_16/04-seed-khai-giang-toast.png` — đã mở đọc: sau khi bấm [Khai giảng], khóa học `KH-QAW7-HOINGHI` chuyển sang bước **4 Đang diễn ra** (chứng minh thao tác đổi trạng thái đã chạy thật).
- `reverify-audit/TTCTDTTH_16/05-BUG-ctdt-van-da-duyet-du-khoahoc-dang-dien-ra.png` — đã mở đọc: chi tiết `CTDT-QAW7-01` vẫn bước **3 Đã duyệt**, bước **4 Đang thực hiện** xám. **Trùng khít bố cục frame `t028.09s` của đối tác.**
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`): thao tác Khai giảng = **1 request** `POST /api/v1/khoa-hocs/{id}/start` + **1 khung thông báo** *"Đã khai giảng khóa học"* → không lặp thông báo, không gửi trùng.

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại bản ghi chương trình sau thao tác** (không chỉ nhìn giao diện): chương trình `CTDT-QAW7-01` trả về `trangThai = "DA_DUYET"`, `ngayCapNhat = "2026-07-25T03:23:52.370Z"` — **y nguyên mốc trước thao tác**. Nếu chỉ giao diện hiển thị sai thì mốc cập nhật phải đổi; ở đây không đổi ⇒ trạng thái chương trình thật sự chưa được xử lý, không phải lỗi hiển thị.
- **Loại giả thuyết "bộ lọc theo trạng thái bị hỏng nên không thấy"**: lọc chương trình theo từng trạng thái cho `Đã duyệt` = **3 bản ghi**, `Đang thực hiện` = **0**, `Hoàn thành` = **0**. Bộ lọc có tác dụng ⇒ danh sách rỗng ở thẻ *Đang thực hiện* là vì **không có chương trình nào ở trạng thái đó**, chứ không phải thẻ lọc lỗi.
- **Loại giả thuyết "việc chuyển trạng thái chạy theo lịch định kỳ nên cần chờ"**: cặp dữ liệu cũ `CTDT-SEED-0001` (Đã duyệt, `ngayCapNhat = 30/06/2026`) có khóa học con `DDD-KH-011` **Đang diễn ra** (`ngayCapNhat = 16/07/2026`) — sau **hai tuần** chương trình vẫn *Đã duyệt* và mốc cập nhật không nhích. Một tiến trình chạy theo giờ/ngày thì đã phải xử lý xong. Bên đối tác cũng vậy: khóa học của họ mở từ 22/07, video quay 24/07 — sau 2 ngày vẫn chưa chuyển.
- **Loại giả thuyết "phải là 'Đã công khai' mới tính, 'Đang diễn ra' thì không"**: đặc tả nêu **cả hai** trạng thái đều là điều kiện (`Đã công khai` / `Đang diễn ra`). Thêm nữa tôi đã thử **[Công khai]** trước: hệ thống từ chối với thông báo *"Khóa học phải có cửa sổ đăng ký hợp lệ trước khi công khai"* (khóa học seed không có ngày mở đăng ký) — đây là chốt kiểm hợp lệ, không phải lỗi; nên tôi chuyển sang **[Khai giảng]**, là nhánh còn lại của cùng điều kiện.
- **Đối chiếu đặc tả — trích nguyên văn** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`):
  - `:2128` — *"DA_DUYET --> DANG_THUC_HIEN : Có ≥1 KHOA_HOC con DA_CONG_KHAI / DANG_DIEN_RA"*
  - `:2144` — *"| DA_DUYET | DANG_THUC_HIEN | Auto khi có ≥1 KHOA_HOC con DA_CONG_KHAI / DANG_DIEN_RA | — | (auto) |"*
  - `:2118` — *"**Tham chiếu FR:** FR-III-01, FR-III-02"* · `:76` — *"### FR-III-01: Quản lý Chương trình đào tạo (UC20)"* · `:78` — *"**UC Reference:** UC 20"*
- **Kiểm phần đã đúng để không quy kết quá phạm vi**: nhánh khóa học chạy đúng (Đã duyệt → Đang diễn ra được, có thông báo, có chốt kiểm cửa sổ đăng ký khi công khai); danh sách + bộ lọc + thẻ đếm của màn chương trình đều hoạt động. Lỗi khoanh đúng vào **việc tự chuyển trạng thái của chương trình theo trạng thái khóa học con**.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

Không phát hiện thêm lỗi mới. Cụ thể, dựa trên các ảnh đã mở đọc ở trên: 2 thao tác đổi trạng thái (Công khai bị từ chối · Khai giảng thành công) đều **1 request ↔ 1 thông báo**, không lặp; thông báo từ chối công khai nêu đúng lý do thiếu cửa sổ đăng ký. Bảng điều khiển của trình duyệt chỉ có **đúng 1 dòng lỗi 422**, ứng với chính lần công khai bị từ chối ở trên (từ chối có kèm thông báo rõ ràng cho người dùng ⇒ không phải lỗi ngầm).
