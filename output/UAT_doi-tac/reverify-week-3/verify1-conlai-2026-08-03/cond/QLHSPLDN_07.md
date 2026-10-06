# QLHSPLDN_07 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLHSPLDN_07 · **Dòng sheet:** 325 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 21:02 → 21:30 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** có giải trình dev, đã sao lưu nguyên văn vào `reverify-audit/QLHSPLDN_07.md` trước khi ghi đè
**Phản ánh đối tác (cột L):** *"Hệ thống hiển thị thông báo cập nhật thành công nhưng dữ liệu chưa được cập nhật vào bản ghi"*
**Kết quả mong đợi đối tác (cột K):** *"Hệ thống mở cửa sổ chỉnh sửa với dữ liệu hiện có. NSD cập nhật và bấm Lưu, hệ thống cập nhật bản ghi và lưu vết thao tác."*

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown pipe trong file này).
> Phần Cổng 1 / Cổng 2 / Cổng 3 trình bày dạng gạch đầu dòng; số đo đầy đủ theo từng trường đặt ở `reverify-audit/QLHSPLDN_07.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File đã mở: `partner-evidence/QLHSPLDN_07-1.jpg` (ảnh tĩnh 1904×1031) + **6 khung hình** trong `frames/QLHSPLDN_07/` trích từ `QLHSPLDN_07-2.webm`, mở đọc từng khung bằng tool Read, KHÔNG kết luận từ ảnh thu nhỏ.
- **3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết):**
  - (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/doanh-nghiep/1a715c55-bc31-46de-ae07-56dd4f403ce5?tab=ho-so-pl` — màn **Chi tiết DN #DN-XX-0005**, thẻ **Hồ sơ pháp lý**; bản ghi thao tác là **`HSPL-20260803-0001`**.
  - (b) Trạng thái entity: `HSPL-20260803-0001` — Loại **Khác**, LVPL **Thuế**, Nguồn **Thủ công**, Ngày cấp **03/08/2026**, Ngày hết hạn **03/08/2026**, Trạng thái **Hiệu lực**. DN có 2 hồ sơ, cả hai "Hiệu lực".
  - (c) Dữ liệu tiền đề: góc phải trên ghi **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**. Hồ sơ đang sửa **đã có sẵn 1 tệp đính kèm** `2K15 T3 (4.8) & CN (9.8).pdf` (258.2 KB); các ô Cơ quan cấp `TKM`, Trạng thái `Hiệu lực`, Mô tả `tkm kiểm thử chức năng` đã có dữ liệu. Đồng hồ máy đối tác 2026-08-03 10:04 → 10:06.
- **Khoảnh khắc lỗi:** khung **`t015.08s.jpg`** (mốc 00:15). Ở mốc 00:03 đối tác thêm tệp `QLHSPLDN_07.jpg` (213.3 KB) thành 2 tệp; mốc 00:12 bấm Đồng ý và hệ thống báo **"Cập nhật hồ sơ thành công"**; mốc 00:15 mở lại chính cửa sổ Sửa đó thì **chỉ còn 1 tệp cũ** — tệp vừa thêm đã biến mất.
- Cách đối tác kết luận "không lưu": **mở lại cửa sổ Sửa của chính bản ghi vừa lưu** rồi so sánh danh sách tệp đính kèm (không tải lại trang).
- ⇒ Kết luận Cổng 1: phản ánh của đối tác là **chính xác đối với bản dựng họ quay**; không có dấu hiệu thao tác nhầm hay bỏ sót do cuộn.

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ: khi **Sửa hồ sơ pháp lý DN**, hệ thống **báo cập nhật thành công** nhưng **thay đổi không được ghi vào bản ghi**. Thay đổi duy nhất quan sát được trong video là **thêm 1 tệp đính kèm**, và đó chính là thứ bị mất. Các ô khác giữ nguyên giá trị cũ giữa khung đầu và khung cuối nên video **không phân biệt được** các trường khác có bị mất hay không → bắt buộc phải tự đo đủ mọi KIỂU trường (chữ / ngày / ô chọn / trạng thái / tệp), không kết luận gộp.
- Dữ liệu + bước tái hiện (theo cột J của chính phiếu): cần 1 DN có ≥1 hồ sơ pháp lý. Đăng nhập vai trò Cán bộ Nghiệp vụ → menu **Doanh nghiệp** → **Xem chi tiết** một DN → thẻ **Hồ sơ pháp lý** → **Sửa** → đổi dữ liệu + thêm tệp → **Đồng ý** → mở lại bản ghi so sánh.

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — vai trò `CB_NV_TW`, phạm vi `BTP · TW` (đọc được ở góc phải trên ảnh và mọi khung video) | `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp) — **trùng khớp tuyệt đối vai trò + cấp của đối tác**, chạy trong phiên trình duyệt cách ly riêng nên không dính phiên cũ. Toàn bộ verdict dựa trên tài khoản này. Tài khoản `cbnv_hn` (`CB_NV_DP`, Sở Tư pháp Hà Nội) chỉ dùng cho **phép thử phụ A2** trên hồ sơ cũ 21/07 mà cấp TW không ghi được, không dùng ra verdict. KHÔNG dùng `admin` | Không |
| Entity + trạng thái (state machine) | `HO_SO_PHAP_LY_DN` — bản ghi bị lỗi ở trạng thái **Hiệu lực**, loại **Khác**, nguồn **Thủ công**, **đã có sẵn 1 tệp đính kèm** | Đã sửa và lưu hồ sơ ở **cả 3 trạng thái** hệ thống cho phép (**Hiệu lực**, **Hết hạn**, **Thu hồi**) và **4/5 loại hồ sơ** (Giấy phép, Quyết định, Khác, Hợp đồng), nguồn **Thủ công** trùng đối tác. Kiểm cả hồ sơ **đã có sẵn tệp** (giống tiền đề đối tác) lẫn hồ sơ **chưa có tệp**; mọi lần đều thêm tệp mới rồi mở lại kiểm | Không |
| Dữ liệu tiền đề (tuổi bản ghi — cũ trước bản vá vs mới tạo) | Bản ghi `HSPL-20260803-0001` được tạo cùng ngày quay (03/08/2026), thuộc đúng đơn vị của người thao tác | Chạy **3 kịch bản** để phủ cả hai phía: **(A)** hồ sơ **có sẵn từ trước** phiên đo (`HSPL-20260803-0001`, tạo 13:46, sửa lúc 21:16); **(A2)** hồ sơ **cũ thật tạo 21/07/2026** — trước bản vá của dev (`HSPL-20260721-0001`); **(B)** hồ sơ **mới tạo qua luồng chuẩn** ngay trong phiên rồi sửa (`HSPL-20260803-0003`). Cả ba cho kết quả **giống nhau: lưu đủ** ⇒ loại trừ hoàn toàn giả thuyết "dữ liệu cũ đóng băng theo lỗi cũ" | Không |
| Input / giá trị nhập (kiểu trường bị ảnh hưởng) | Video chỉ chứng minh được **1 kiểu**: tệp đính kèm (thêm 1 tệp vào hồ sơ đã có 1 tệp). Các ô chữ/ngày/ô chọn giữ nguyên giá trị nên không kết luận được | Sửa **đủ 5 kiểu trường** trong mỗi kịch bản, dùng giá trị dễ nhận dạng `QA-EDIT-*-20260803-*`: **chữ** (Tên hồ sơ, Cơ quan cấp), **chữ dài** (Mô tả), **ngày** (Ngày cấp, Ngày hết hạn), **ô chọn** (Loại hồ sơ, Lĩnh vực pháp lý), **trạng thái**, và **tệp đính kèm**. Form không có ô kiểu số nên không đo được kiểu này — SRS bảng Inputs cũng không quy định trường số nào cho chức năng này. Mỗi trường kiểm ở **3 nơi**: khung thông báo + số request · sau khi **tải lại trang thật** · **đọc lại bản ghi theo id từ dịch vụ máy chủ** | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

### Thứ tự đo

- **Đo web TRƯỚC, đọc SRS SAU.** Toàn bộ số đo được ghi ra trước khi mở bất kỳ file SRS nào.

### SRS quy định gì

**Nguồn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — bản chốt duy nhất. Đã grep **toàn bộ 18 file** cho "hồ sơ pháp lý" / `HO_SO_PHAP_LY_DN` / `HSPL` trước khi chốt.

- `srs-fr-12-tv-chuyen-sau.md:541` — `### FR-X.1-04: Quản lý hồ sơ pháp lý doanh nghiệp (UC150)`; dòng **543** ghi `**UC Reference:** UC 150`.
- `srs-fr-12-tv-chuyen-sau.md:550` — *"CRUD hồ sơ pháp lý doanh nghiệp: xem danh sách, xem chi tiết, thêm mới, **chỉnh sửa**, xóa mềm, tìm kiếm."*
- `srs-fr-12-tv-chuyen-sau.md:607-614` — khối Processing **"Chỉnh sửa"** 4 bước, trong đó bước 3 *"**Cập nhật bản ghi hồ sơ**"* và bước 4 *"**Ghi nhật ký thao tác**"* (`BR-DATA-05`).
- `srs-fr-12-tv-chuyen-sau.md:674` — Postconditions *"Hồ sơ được tạo/**cập nhật**/xóa mềm trong CSDL"*; dòng **676** *"AUDIT_LOG ghi nhận mọi thao tác CUD"*.
- `srs-fr-12-tv-chuyen-sau.md:695` — Acceptance Criteria *"**Given** CB NV chỉnh sửa hồ sơ **When** sửa thông tin + nhấn Lưu **Then** cập nhật bản ghi"*.
- `srs-fr-12-tv-chuyen-sau.md:560-574` — bảng Inputs "Thêm mới / Chỉnh sửa" 11 trường, gồm dòng **574** `file_dinh_kem | file | N | PDF/image, max 20MB`; dòng **567** 5 loại hồ sơ; dòng **573** 3 trạng thái.
- `srs-fr-07-doanh-nghiep.md:468` — màn `SCR-V.III-02` (chính màn đối tác đứng), thành phần số 2: *"Tab Hồ sơ PL doanh nghiệp (MỚI v2.1) … **CRUD hồ sơ pháp lý DN**"*.
- `srs-fr-12-tv-chuyen-sau.md:547` — màn riêng cũ `SCR-X1-03` **DEPRECATED v2.1**, chuyển thành tab trong màn chi tiết DN ⇒ không lấy dòng nào của SCR-X1-03 làm căn cứ.

### Kiểm nhãn GAP và mâu thuẫn nội tại SRS

- Trong FR-X.1-04 chỉ có **2 khối mang nhãn `[GAP-X.1-05]`**: *Processing — Xem chi tiết* (dòng 634) và *Processing — Xuất Excel* (dòng 644). Khối **"Chỉnh sửa" (dòng 607) và AC dòng 695 KHÔNG mang nhãn GAP** ⇒ yêu cầu áp cho case này là **đã chốt**, không thuộc vùng SRS còn treo.
- Chỗ duy nhất trong SRS gọi danh sách hồ sơ pháp lý là *"Read-only"* là `srs-fr-07-doanh-nghiep.md:523`, nhưng dòng đó thuộc **SCR-V.III-04 "Hồ sơ doanh nghiệp của tôi"** (`srs-fr-07-doanh-nghiep.md:508`) — chuyên trang của vai trò **Doanh nghiệp**, không phải màn của cán bộ ⇒ **không mâu thuẫn** cho màn đang xét.

### Thực tế web hiện tại (số đo, không phải cảm nhận)

- Chạy **3 kịch bản × 9 trường = 27 ô đo**, mỗi ô kiểm ở **3 nơi** (khung thông báo + số request · sau khi tải lại trang thật · đọc lại từ dịch vụ máy chủ). **27/27 ô đều lưu đúng.** Không nhóm trường nào bị bỏ sót.
- Mọi lần lưu đều đúng tỉ lệ **1 request ↔ 1 khung thông báo** `"Cập nhật hồ sơ thành công"`, **không có thông báo lặp**, không tạo trùng bản ghi. Bước tạo hồ sơ mới cũng vậy: 1 request ↔ 1 thông báo `"Thêm hồ sơ thành công"`.
- Đúng vế *"lưu vết thao tác"* của Kết quả mong đợi: `version` tăng 1→2, thời điểm cập nhật đổi đúng lúc bấm, và người cập nhật được ghi đúng là tài khoản đang thao tác — ở **cả 3 kịch bản**.
- Kịch bản **giống hệt video đối tác** (thêm tệp đính kèm vào hồ sơ rồi mở lại) chạy **3/3 lần đều giữ được tệp** đúng tên và đúng dung lượng sau khi tải lại trang.
- ⇒ Đối chiếu từng vế: SRS dòng 613 "cập nhật bản ghi" ✅ · dòng 695 "sửa + Lưu → cập nhật" ✅ · dòng 614/676 "ghi nhật ký thao tác" ✅ · dòng 574 "file đính kèm" ✅ · dòng 567/573 (5 loại × 3 trạng thái) ✅. **Kết quả mong đợi của chính đối tác (cột K) được đáp ứng trọn vẹn.**

### Phép thử thứ hai

- Mỗi kết luận dựa trên **≥2 phương pháp độc lập cho kết quả trùng nhau**: đọc cây DOM cửa sổ Sửa sau khi tải lại trang · gọi thẳng dịch vụ máy chủ đọc lại bản ghi theo id · ảnh chụp màn hình đã mở đọc bằng mắt · dòng trong bảng danh sách sau khi tải lại trang. **Không mâu thuẫn ở bất kỳ trường nào.**
- Trong quá trình đo đã phát hiện và sửa **3 lỗi của chính phép đo** (sai class đếm tệp, sai class đọc ô chọn, hàm điền bị nối chuỗi thay vì thay thế) — chi tiết ở `reverify-audit/QLHSPLDN_07.md`. Số liệu báo cáo là số đo **sau khi** đã sửa phép đo và tự kiểm bộ bắt thông báo (`soObserverDangSong = 1`).

---

## Kết luận

- Lỗi đối tác phản ánh **KHÔNG còn tái hiện** trên bản dựng `HTPLDN · V1.0.5`, kiểm ở đúng vai trò và phạm vi của đối tác.
- Đã loại trừ giả thuyết "dữ liệu cũ đóng băng": hồ sơ cũ (kể cả hồ sơ tạo 21/07, trước bản vá) và hồ sơ mới tạo đều lưu đủ như nhau ⇒ không cần `BA confirm`.
- Đối tác **không thao tác sai** — video của họ cho thấy bản dựng cũ thật sự làm mất tệp vừa đính kèm dù đã báo thành công ⇒ **KHÔNG dùng `Reject`**.
- Cột P đang là `dev done` và phép thử lại cho kết quả chạy đúng ⇒ **Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.
