# Bảng đối chiếu điều kiện — TTCTDTTH_17 (row 237) — CTĐT không tự chuyển sang "Hoàn thành"

**Kết luận:** Open (Major). Tái hiện 1/1 bằng thao tác thật; cùng gốc lỗi với `BUG-TTCTDTTH_16`.

Phiếu ghi *"Chương trình ở trạng thái 'Đã duyệt' và có ít nhất 1 khóa học ở trạng thái 'Hoàn thành' nhưng hệ thống không tự động chuyển trạng thái của chương trình sang 'Hoàn thành'"* → **TÁI HIỆN ĐÚNG**.

Tôi đưa khóa học con cuối cùng của một chương trình về **Hoàn thành** bằng đúng luồng nghiệp vụ trên giao diện (Cán bộ nghiệp vụ *Gửi duyệt KQ* → Cán bộ phê duyệt *Duyệt KQ*), khiến **toàn bộ** khóa học của chương trình đều ở "Hoàn thành". Chương trình cha vẫn đứng ở bước **3 Đã duyệt**; mốc `ngayCapNhat` của chương trình không đổi.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/TTCTDTTH_18.webm`, full-res) | Mình test (env nip.io, 30/07/2026 10:05–10:20) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Frame `t000.00s` + `t006.05s` góc phải: **Cán bộ NV Trung ương · CB_NV_TW**, phạm vi **BTP · TW**. Lịch sử phê duyệt trong frame `t000.00s` cho thấy khâu duyệt do **Cán bộ PD Trung ương** thực hiện | Quan sát kết luận bằng `cbnv_tw` (CB Nghiệp vụ - Trung ương, BTP · TW) — đúng vai trò + cấp. Khâu duyệt kết quả dùng `cbpd_tw_01` (CB Phê duyệt - Trung ương, cùng cấp TW) — xem ghi chú tài khoản dưới | Không |
| Entity + **trạng thái** (state machine) | Chương trình `CTDT-BTP-TW-2026-0011 — TKM Test` ở bước **3 Đã duyệt**; bảng "Khóa học thuộc chương trình" có **1 khóa học duy nhất, trạng thái Hoàn thành** | Chương trình `CTDT-2026-001` ở bước **3 Đã duyệt**; bảng "Khóa học thuộc chương trình" có **2 khóa học, cả 2 đều Hoàn thành** (`KH-2026-001` sẵn Hoàn thành, `KH-2026-002` do tôi đưa từ *Đã kết thúc* → *Chờ duyệt KQ* → *Hoàn thành*) | Không |
| Dữ liệu tiền đề | Chương trình đã duyệt + **mọi** khóa học con đã Hoàn thành | Dựng đúng điều kiện "mọi khóa học con Hoàn thành" — không để sót khóa nào ở trạng thái khác (đã đọc lại từng khóa: `HOAN_THANH` / `HOAN_THANH`) | Không |
| Input / thao tác kích hoạt | Đối tác mở chi tiết chương trình để xem trạng thái sau khi khóa học đã hoàn thành | `cbnv_tw` bấm **[Gửi duyệt KQ]** (1 request `POST …/submit-result`, 1 thông báo) → `cbpd_tw_01` bấm **[Duyệt KQ]** (1 request `POST …/approve-result`, 1 thông báo) → mở lại chi tiết chương trình + đọc lại bản ghi | Không |

> **Ghi chú tài khoản (Rule 7 — fallback trong cùng vai trò + cấp):** `cbpd_tw` đăng nhập thất bại — `POST /api/v1/auth/login` trả **401** `ERR-AUTH-LOGIN-01` *"Tên đăng nhập hoặc mật khẩu không đúng."* (ảnh `reverify-audit/TTCTDTTH_17/02-account-cbpd_tw-login-401.png`). Đã tự động chuyển sang tài khoản cùng vai trò **CB_PD_TW** và **cùng cấp TW**: `cbpd_tw_01` (đăng nhập OK, giao diện hiển thị "CB Phê duyệt - Trung ương #01"). Không đổi vai trò, không đổi cấp ⇒ phạm vi dữ liệu không thay đổi.

## Artifact real-data (Gate bằng chứng — loại claim: Thao tác/state)

- `partner-evidence/TTCTDTTH_18.webm` — đã mở đọc frame full-res. `t000.00s`: chi tiết `CTDT-BTP-TW-2026-0011`, bảng "Khóa học thuộc chương trình" có 1 dòng **Hoàn thành** (03/07–04/07/2026, sĩ số 1/2); "Lịch sử phê duyệt" ghi *Gửi duyệt* 03/07 16:34 và *Phê duyệt* 03/07 16:35. `t006.05s` = **khoảnh khắc lỗi**: thanh tiến trình của chương trình vẫn ở bước **3 Đã duyệt**, bước **4 Đang thực hiện** và **5 Hoàn thành** đều xám.
- `reverify-audit/TTCTDTTH_17/01-seed-trinh-duyet-kq-KH-2026-002.png` — đã mở đọc: khóa học `KH-2026-002` sau [Gửi duyệt KQ] chuyển sang bước **6 Chờ duyệt KQ**.
- `reverify-audit/TTCTDTTH_17/03-seed-duyet-kq-KH-2026-002-hoan-thanh.png` — đã mở đọc: cùng khóa học sau [Duyệt KQ] của `cbpd_tw_01` chuyển sang bước **7 Hoàn thành** (góc phải xác nhận đang đăng nhập "CB Phê duyệt - Trung ương #01 · CB_PD_TW").
- `reverify-audit/TTCTDTTH_17/04-BUG-ctdt-van-da-duyet-du-moi-khoahoc-hoan-thanh.png` — đã mở đọc: chi tiết `CTDT-2026-001` (đăng nhập `cbnv_tw`) vẫn bước **3 Đã duyệt**; trên trang chỉ có [Quay lại danh sách], [Xuất DOCX], [Tạo khóa học] — **không có bất kỳ nút nào để đưa chương trình đi tiếp**.
- `reverify-audit/TTCTDTTH_17/05-BUG-2-khoahoc-hoan-thanh-ctdt-buoc-3.png` — đã mở đọc: bảng "Khóa học thuộc chương trình" cuộn sang cột **Trạng thái**, cả 2 khóa học đều **Hoàn thành**.
- Bộ bắt thông báo (`tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1` ở cả 2 phiên): mỗi thao tác đúng **1 request ↔ 1 khung thông báo** (*"Đã trình duyệt kết quả thành công"* · *"Đã phê duyệt kết quả thành công"*).

## Phương pháp thứ hai (bắt buộc)

- **Đọc lại bản ghi chương trình sau thao tác**: `CTDT-2026-001` trả `trangThai = "DA_DUYET"`, `ngayCapNhat = "2026-07-25T03:23:52.082Z"` — **y nguyên**, trong khi khóa học con `KH-2026-002` có `ngayCapNhat = "2026-07-30T03:11:51.907Z"` (đúng lúc tôi duyệt). ⇒ Hệ thống cập nhật khóa học nhưng **không chạm** tới chương trình. Không phải lỗi hiển thị.
- **Kiểm xem hệ thống có đường nào đưa chương trình đi tiếp hay không** (phép thử phân biệt "chưa kích hoạt tự động" vs "chưa làm chức năng"): danh sách thao tác mà máy chủ mở cho chương trình đào tạo chỉ có *gửi duyệt · phê duyệt · từ chối · hủy* — **không có thao tác nào ứng với "Đang thực hiện" hoặc "Hoàn thành"**. Thử cập nhật trực tiếp trạng thái cũng bị chặn: trả **409** `ERR-STATE-SYS-00-01` — *"ERR-BIZ-III-01-03: Chỉ được cập nhật chương trình ở trạng thái DU_THAO hoặc TU_CHOI (hiện tại: DA_DUYET)"*. ⇒ Hai trạng thái cuối của vòng đời chương trình **không có đường nào đi tới**, cả tự động lẫn thủ công.
- **Không thể dựng tiền đề "chương trình đang ở Đang thực hiện"** để đo riêng nhánh 2, vì chính nhánh 1 đã hỏng (xem `BUG-TTCTDTTH_16`) và hệ thống không có thao tác nào đặt được trạng thái đó. Vì vậy tôi **không tách** đây thành lỗi độc lập mà ghi rõ là **cùng một gốc**: vòng đời chương trình bị cắt ở "Đã duyệt". Dev sửa nhánh 1 xong phải kiểm lại nhánh 2 mới đóng được phiếu này.
- **Đối chiếu đặc tả — trích nguyên văn** (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`):
  - `:2129` — *"DANG_THUC_HIEN --> HOAN_THANH : Tất cả KHOA_HOC con HOAN_THANH / DA_HUY"*
  - `:2145` — *"| DANG_THUC_HIEN | HOAN_THANH | Auto khi tất cả KHOA_HOC con HOAN_THANH / DA_HUY | — | (auto) |"*
  - `:2119` — *"**Trạng thái:** 7 (DU_THAO, CHO_DUYET, TU_CHOI, DA_DUYET, DANG_THUC_HIEN, HOAN_THANH, DA_HUY)"* ⇒ 2 trong 7 trạng thái đang không thể đạt.
  - `:2118` — *"**Tham chiếu FR:** FR-III-01, FR-III-02"* · `:76` / `:78` — *"FR-III-01: Quản lý Chương trình đào tạo (UC20)"*, *"UC Reference: UC 20"*
- **Kiểm phần đã đúng để không quy kết quá phạm vi**: vòng đời **khóa học** chạy đủ 7 bước (Đã kết thúc → Chờ duyệt KQ → Hoàn thành), phân quyền đúng (cán bộ nghiệp vụ trình, cán bộ phê duyệt mới duyệt được), thông báo rõ ràng. Lỗi khoanh đúng vào **vòng đời của chương trình đào tạo**.

## Ngoài tiêu chí phiếu — có thấy gì bất thường không?

- **Đã soi 1 nghi vấn và LOẠI, không log:** trong ảnh `04-…` chụp ngay sau khi tải trang, 2 ô *Kế hoạch năm* và *Lĩnh vực pháp luật* của `CTDT-2026-001` hiển thị **mã định danh thô** (`f0aaaaaa-…`, `bbbbbbbb-…`) thay vì tên. Đo lại bằng phương pháp thứ hai (đọc chữ hiển thị thực của 2 ô đó sau khi trang tải xong) thì ra đúng tên: *"Kế hoạch đào tạo PL doanh nghiệp 2026 (2026)"* và *"Dân sự"*. ⇒ Đây là **trạng thái tạm trong lúc danh sách chọn chưa tải xong**, không phải lỗi hiển thị. Hai phương pháp mâu thuẫn ⇒ theo quy trình, **chưa được log**.
- Ngoài ra không phát hiện thêm: 2 thao tác đổi trạng thái đều 1 request ↔ 1 thông báo, không lặp.
