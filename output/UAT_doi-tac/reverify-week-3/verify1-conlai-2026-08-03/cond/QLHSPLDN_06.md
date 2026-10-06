# QLHSPLDN_06 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLHSPLDN_06 · **Dòng sheet:** 324 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 20:53 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** TRỐNG tại thời điểm QA verify
**Phản ánh đối tác (cột L):** *"Màn hình không có nút chức năng xem chi tiết"* — thẻ **Hồ sơ pháp lý** trong màn Chi tiết Doanh nghiệp.
**Kết quả mong đợi đối tác (cột K):** *"Hệ thống mở cửa sổ chi tiết hiển thị toàn bộ thông tin của hồ sơ và danh sách tệp đính kèm (nếu có) ở chế độ chỉ đọc."*

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown pipe trong file này).
> Phần Cổng 3 trình bày dạng gạch đầu dòng; lập luận đầy đủ + danh sách khả năng đã loại trừ đặt ở `reverify-audit/QLHSPLDN_06.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File: `partner-evidence/QLHSPLDN_06.jpg` — mở đọc bằng tool Read ở độ phân giải gốc 1904×1031, đọc trực tiếp chữ trên ảnh, KHÔNG kết luận từ ảnh thu nhỏ.
- **3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết):**
  - (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — đúng màn **Chi tiết DN #DN-XX-0005**, đang mở thẻ **Hồ sơ pháp lý**. Đồng hồ máy đối tác 2026-08-03 10:03.
  - (b) Trạng thái entity: **2 hồ sơ pháp lý**, cả hai đều mang nhãn xanh **"Hiệu lực"** (cột Trạng thái bị cắt còn chữ "Trạng…" nhưng nhãn đọc được). Mã: `HSPL-20260803-0001` (Khác · Thuế · Thủ công · cấp 03/08/2026 · hết hạn 03/08/2026) và `HSPL-20260731-0002` (Giấy chứng nhận · Đất đai · Thủ công · cấp 01/07/2026 · hết hạn "–").
  - (c) Dữ liệu tiền đề: góc phải trên ghi **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**. Nguồn cả 2 hồ sơ là **Thủ công**.
- **Khoảnh khắc lỗi trong ảnh:** chính khung hình này — cột **Hành động** của cả 2 hàng chỉ có đúng **2 nút: [Sửa] [Xoá]**, KHÔNG có nút mở chi tiết. Cột "Hành động" là cột ghim bên phải nên hiện đủ, không bị cuộn khuất.
- Ghi nhận thêm ở ảnh đối tác: bảng của họ có **9 cột** (Mã hồ sơ / Tên hồ sơ / Loại / Lĩnh vực pháp lý / Nguồn / Ngày cấp / Ngày hết hạn / Trạng thái / Hành động) — **không có** cột "Có tệp đính kèm".
- ⇒ Kết luận Cổng 1: phản ánh của đối tác là **chính xác đối với bản dựng họ chụp**. Không có dấu hiệu họ thao tác sai hay bỏ sót do cuộn.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ: trên bảng "Hồ sơ pháp lý DN" của màn Chi tiết Doanh nghiệp, cột Hành động **thiếu hẳn nút mở chi tiết hồ sơ**; chỉ có Sửa và Xoá. Hệ quả: không thực hiện được bước 4 của kịch bản ("Nhấn Xem") nên không xem được toàn bộ thông tin hồ sơ + danh sách tệp đính kèm ở chế độ chỉ đọc.
- Dữ liệu + bước tái hiện (theo cột J của chính phiếu): đăng nhập vai trò Cán bộ Nghiệp vụ → menu **Doanh nghiệp** → bấm **Xem chi tiết** một DN → chọn thẻ **Hồ sơ pháp lý** → tìm nút **Xem** trên từng hàng. Tiền đề: DN phải có ≥1 hồ sơ pháp lý.

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — vai trò `CB_NV_TW`, phạm vi `BTP · TW` (đọc được ở góc phải trên ảnh) | `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp) — **trùng khớp tuyệt đối vai trò + cấp + đơn vị của đối tác**, chạy trong phiên trình duyệt cách ly riêng nên không dính phiên cũ. Đo thêm vai trò **Doanh nghiệp** (`0109998887`) trong phiên cách ly thứ hai để loại trừ khả năng "nút chỉ hiện với vai trò khác" | Không |
| Entity + trạng thái (state machine) | `HO_SO_PHAP_LY_DN` — 2 bản ghi, cả hai ở trạng thái **Hiệu lực**, nguồn **Thủ công** | Đo đủ **cả 3 trạng thái** hệ thống cho phép: **Hiệu lực** (4 bản ghi có sẵn), **Hết hạn** và **Thu hồi** (2 bản ghi do đội kiểm thử **tự tạo** ngay trong phiên vì môi trường chưa có). Tất cả đều nguồn Thủ công, trùng nguồn của đối tác | Không |
| Dữ liệu tiền đề (DN phải có sẵn hồ sơ pháp lý để bảng có hàng) | DN `#DN-XX-0005` có sẵn 2 hồ sơ pháp lý | DN `#DN-HNI-0001` (`Cong ty TNHH QA UAT Kiem Thu`, MST 0109998887) có sẵn 4 hồ sơ; đội kiểm thử **seed thêm 2 hồ sơ** để phủ 2 trạng thái còn thiếu → tổng **6 hồ sơ**. Có kiểm cả hồ sơ **có tệp đính kèm** và hồ sơ **không có tệp** | Không |
| Input / filter / giá trị nhập | Không nhập gì — ảnh chụp bảng ở trạng thái vừa mở thẻ, chưa lọc, chưa cuộn ngang | Đo ở đúng trạng thái vừa mở thẻ, chưa lọc. Sau đó **cuộn hết chiều ngang bảng** và đo lại bằng toạ độ thật; có **tải lại trang** trước khi chốt để chắc không đọc phải mã cũ còn giữ trong tab | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — bản chốt duy nhất. Đã **grep toàn bộ 18 file** cho khái niệm "Hồ sơ pháp lý" trước khi chốt, không đọc một dòng rồi kết luận.

### Thứ tự đo

- **Đo web TRƯỚC, đọc SRS SAU.** Toàn bộ số đo ở mục dưới được ghi ra trước khi mở bất kỳ file SRS nào.

### SRS quy định gì

- `srs-fr-12-tv-chuyen-sau.md:541` — `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)`; **dòng 543** ghi `**UC Reference:** UC 150`.
- `srs-fr-12-tv-chuyen-sau.md:550` — Mô tả FR: *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, **xem chi tiết**, thêm mới, chỉnh sửa, xóa mềm, tìm kiếm."*
- `srs-fr-12-tv-chuyen-sau.md:634` — khối `**Processing — Xem chi tiết** [GAP-X.1-05]`, bước 3 *"Trả full record: thông tin hồ sơ + thông tin DN liên kết"*, bước 4–5 *"Truy vấn danh sách file đính kèm (FILE_DINH_KEM)… Trả kết quả bao gồm file đính kèm (tên, loại, dung lượng, URL preview)"*.
- `srs-fr-12-tv-chuyen-sau.md:693` — Acceptance Criteria: *"**Given** CB NV xem chi tiết hồ sơ **When** chọn bản ghi **Then** hiển thị đầy đủ thông tin + file đính kèm"*.
- `srs-fr-07-doanh-nghiep.md:455` — `### SCR-V.III-02: Chi tiết / Chỉnh sửa Doanh nghiệp`, chính là màn đối tác đứng; **dòng 468** mô tả thành phần số 2: *"Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) … **CRUD hồ sơ pháp lý DN**: GIAY_PHEP / HOP_DONG / GIAY_CN / QUYET_DINH / KHAC. Trạng thái: HIEU_LUC / HET_HAN / THU_HOI"*.
- `srs-fr-12-tv-chuyen-sau.md:547` — màn hình riêng cũ `SCR-X1-03` đã **DEPRECATED v2.1**, chức năng chuyển thành tab trong màn chi tiết DN ⇒ tab này chính là nơi duy nhất còn thực thi FR-X.1-04.
- **Kiểm mâu thuẫn nội tại SRS:** chỗ duy nhất trong toàn bộ SRS gọi danh sách hồ sơ pháp lý là *"Read-only"* là `srs-fr-07-doanh-nghiep.md:523` — nhưng dòng đó thuộc **SCR-V.III-04 "Hồ sơ doanh nghiệp của tôi"** (`srs-fr-07-doanh-nghiep.md:508`), là **chuyên trang của vai trò Doanh nghiệp**, KHÔNG phải màn của cán bộ. ⇒ **Không có mâu thuẫn** giữa các nguồn cho màn đang xét; yêu cầu "xem chi tiết" là rõ ràng, không phải suy diễn.

### Thực tế web hiện tại (số đo, không phải cảm nhận)

- **6/6 hàng** trong bảng "Hồ sơ pháp lý DN" đều có **3 nút** ở cột Hành động: **[👁 Xem] [Sửa] [Xoá]** — tổng 18 nút. Đếm bằng **3 cách độc lập** cho cùng kết quả: đếm nút trong ô cuối mỗi hàng (18), đếm nút có chữ đúng "Xem" (6), đếm biểu tượng con mắt (6).
- Nút Xem **hoạt động được**: không có thuộc tính vô hiệu hoá, không bị chắn sự kiện chuột, độ mờ 1, kích thước thật 68×24 điểm ảnh.
- Bấm Xem → mở cửa sổ **"Chi tiết hồ sơ pháp lý"** hiển thị: Mã hồ sơ, Tên hồ sơ, Loại hồ sơ, Lĩnh vực pháp lý, Nguồn, Cơ quan cấp, Ngày cấp, Ngày hết hạn, Trạng thái, Mô tả, và mục **Tệp đính kèm** kèm tên tệp + dung lượng + 2 nút Xem/Tải, cùng nút Đóng.
- Cửa sổ chi tiết **đúng chế độ chỉ đọc**: đếm được **0 ô nhập liệu** trong cửa sổ (0 input / 0 textarea / 0 ô chọn).
- ⇒ Đối chiếu từng vế của SRS dòng 634 và 693: "thông tin hồ sơ đầy đủ" ✅ · "file đính kèm kèm tên + dung lượng + xem trước" ✅ · "chọn bản ghi thì mở được chi tiết" ✅. Yêu cầu **kết quả mong đợi của chính đối tác** (cột K) cũng được đáp ứng trọn vẹn.

---

## Kết luận

- Phản ánh của đối tác **KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, kiểm ở đúng vai trò `CB_NV_TW` + đúng cấp `BTP · TW` như ảnh đối tác.
- Nút mở chi tiết **đã có ở cả 6/6 hàng, thuộc cả 3 trạng thái hồ sơ**, và mở ra đúng cửa sổ chi tiết chỉ đọc kèm danh sách tệp đính kèm như đặc tả đòi.
- Xác nhận thêm: đối tác **không hề thao tác sai** — ảnh của họ cho thấy bản dựng cũ thật sự chỉ có 2 nút Sửa/Xoá, và cột Hành động là cột ghim phải nên không thể bị cuộn khuất. Vì vậy **KHÔNG dùng `Reject`**.
- Mỗi kết luận dựa trên ≥2 phương pháp độc lập cho kết quả trùng nhau (đọc cây DOM · ảnh chụp đã mở đọc · gọi trực tiếp dịch vụ máy chủ).
- **⇒ Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.
