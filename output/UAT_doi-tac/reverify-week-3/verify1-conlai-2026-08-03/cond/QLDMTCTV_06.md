# QLDMTCTV_06 — Bảng đối chiếu điều kiện + Cổng 3 (SRS vs web)

**Mã TC:** QLDMTCTV_06 · **Dòng sheet:** 319 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Môi trường:** https://18.143.165.120.nip.io (bản dựng ở chân menu: `HTPLDN · V1.0.5`)
**Cột P (`Trạng thái dev fix 1`):** `dev done` — dev tự điền, là CLAIM chứ không phải bằng chứng · **Cột R:** rỗng tại thời điểm QA verify
**Phản ánh đối tác:** "Kiểm tra các trường thông tin trên màn hình/popup thêm mới" — màn *Mạng lưới Tư vấn viên → Tổ chức tư vấn → Thêm mới*. Kết quả thực tế đối tác ghi: **"Thiếu trường thông tin Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm"**.

> Bảng dưới đây là **bảng đối chiếu điều kiện duy nhất** trong file (script `sheet_write.py` đọc mọi bảng markdown trong file này).
> Phần Cổng 3 trình bày dạng gạch đầu dòng; lập luận đầy đủ đặt ở `reverify-audit/QLDMTCTV_06.md`.

---

## Cổng 1 — Bằng chứng đối tác (đã mở FULL-RES)

- File: `partner-evidence/QLDMTCTV_06.jpg` — đã mở đọc bằng tool Read ở độ phân giải gốc 1904×1031, đọc trực tiếp chữ trên ảnh, không kết luận từ ảnh thu nhỏ.
- **3 dữ kiện neo (viết ra TRƯỚC khi hình thành giả thuyết):**
  - (a) URL/bản ghi: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/to-chuc/tao-moi` — đúng màn **Thêm mới Tổ chức tư vấn**, đường dẫn khớp đặc tả. Breadcrumb "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / **Thêm mới**". Đồng hồ máy đối tác 2026-07-28 09:05.
  - (b) Trạng thái entity: **chưa có bản ghi** — biểu mẫu ở chế độ nhập liệu mới, mọi ô đều trống ("nhập dữ liệu" / "Vui lòng chọn"). Đây là tiền đề đúng của case.
  - (c) Dữ liệu tiền đề: góc phải trên ghi **"Cán bộ NV Trung ương · CB_NV_TW"**, phạm vi **BTP · TW**.
- **🔴 Vai trò đọc được trong ảnh = Cán bộ Nghiệp vụ Trung ương (CB_NV_TW), phạm vi BTP · TW** — tự đọc lại từ ảnh của chính case 06, không suy ra từ case 05. Đây đúng là vai trò được cấp quyền tạo Tổ chức tư vấn, nên quan sát của đối tác là quan sát hợp lệ.
- **🔴 Tình trạng nhóm thu gọn trong ảnh đối tác — dữ kiện quyết định:** biểu mẫu của đối tác **KHÔNG có bất kỳ tiêu đề nhóm nào và KHÔNG có nhóm nào đang thu gọn**. Ảnh chụp từ **đầu biểu mẫu** (thấy breadcrumb + ô đầu tiên "Tên tổ chức") **xuống tới ô cuối "Ghi chú"** — tức gần như trọn chiều dài biểu mẫu. Thứ tự ô trong ảnh: Tên tổ chức → Loại hình → Người đại diện → Chức vụ đại diện → Số Giấy ĐKHĐ Sở TP → Ngày cấp → Số lao động → Địa chỉ → Điện thoại → Email → Website → Lĩnh vực pháp lý → **Ghi chú**. Giữa "Lĩnh vực pháp lý" và "Ghi chú" **không có** vùng "Công bố" lẫn vùng "Tệp đính kèm".
- ⇒ Kết luận Cổng 1: đối tác **không hề bỏ sót do chưa cuộn hoặc chưa mở nhóm thu gọn**. Tại bản dựng họ chụp, 3 trường đó **thực sự vắng mặt**. Phản ánh của đối tác là chính xác đối với bản dựng đó.
- **Khoảnh khắc lỗi trong ảnh:** chính khung hình này — vùng lẽ ra là "Công bố" + "Tệp đính kèm" bị thiếu hẳn, ô "Ghi chú" nối thẳng ngay sau "Lĩnh vực pháp lý".

## Cổng 2 — Hiểu bug

- Đối tác phản ánh CỤ THỂ 3 thành phần bị thiếu trên biểu mẫu Thêm mới: (1) ô nhập **Số quyết định công bố**, (2) bộ chọn ngày **Ngày quyết định công bố**, (3) vùng **Tệp đính kèm**.
- Dữ liệu + bước tái hiện: đăng nhập vai trò Cán bộ Nghiệp vụ → menu *Mạng lưới Tư vấn viên* → *Tổ chức tư vấn* → bấm *Thêm mới* → đọc toàn bộ biểu mẫu. Case **không cần dữ liệu tiền đề** vì chỉ mở biểu mẫu rỗng; tuy nhiên để chứng minh 3 trường **dùng được thật** chứ không chỉ hiển thị, đội kiểm thử có tạo 1 bản ghi thật (xem dòng "Dữ liệu tiền đề" trong bảng).

---

## 🔴 Bảng đối chiếu điều kiện (0 GAP mới được chốt verdict)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | Cán bộ Nghiệp vụ Trung ương — vai trò `CB_NV_TW`, phạm vi `BTP · TW` (đọc được ở góc phải trên ảnh) | `cbnv_tw_04` (CB Nghiệp vụ - Trung ương, `CB_NV_TW`, phạm vi `BTP · TW`, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp) — **trùng khớp tuyệt đối vai trò + cấp + đơn vị của đối tác**; đây cũng đúng vai trò được cấp quyền tạo Tổ chức tư vấn. Chạy trong phiên trình duyệt cách ly riêng nên không dính phiên cũ | Không |
| Entity + trạng thái (state machine) | `TO_CHUC_TU_VAN` — chế độ **Thêm mới**, chưa có bản ghi, mọi ô trống | Mở đúng chế độ **Thêm mới** (`/chuyen-gia-tvv/to-chuc/tao-moi`), biểu mẫu rỗng, đo ngay khi vừa mở và chưa thao tác gì. Sau đó đo thêm ở chế độ **Chỉnh sửa** của bản ghi vừa tạo để đối chiếu | Không |
| Dữ liệu tiền đề (case chỉ mở biểu mẫu nên KHÔNG cần seed trước) | Không cần — biểu mẫu nhập liệu mới | Không cần seed để đo hiển thị. Để chứng minh 3 trường **dùng được thật** (không chỉ vẽ ra), đội kiểm thử đã **tự tạo 1 bản ghi thật** `TC-BTP-TW-0003` qua chính giao diện bằng `cbnv_tw_04`: nhập Số QĐ + chọn Ngày QĐ + đính 1 tệp PDF hợp lệ rồi Lưu, sau đó mở lại đối chiếu | Không |
| Input / filter / giá trị nhập | Không nhập gì (ảnh chụp biểu mẫu rỗng lúc vừa mở) | Đo **2 lần**: (1) lúc vừa mở, chưa nhập gì, chưa cuộn — đúng điều kiện ảnh đối tác; (2) sau khi nhập đủ và lưu. Có **cuộn hết chiều dài biểu mẫu** và **rà mọi dấu hiệu nhóm thu gọn** trước khi kết luận. Có **tải lại trang bỏ qua bộ nhớ đệm (hard reload)** rồi đo lại để chắc không đọc phải mã cũ còn giữ trong tab | Không |

**Kết luận điều kiện: 0 GAP → đủ điều kiện chốt verdict.**

---

## Cổng 3 — SRS yêu cầu (dẫn dòng) vs thực tế web

**Nguồn SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md` — bản chốt duy nhất, đã mở file đọc từng dòng, không lấy số dòng từ trí nhớ.

- `SCR-IV-NEW-02: Thêm mới / Chỉnh sửa Tổ chức tư vấn` — **dòng 1662**; đường dẫn `/chuyen-gia-tvv/to-chuc/tao-moi` — **dòng 1666** (khớp web); Quyền truy cập "Cán bộ Nghiệp vụ" — **dòng 1667** (khớp vai trò đã test).
- FR gốc `FR-IV-NEW-01: Quản lý Tổ chức tư vấn` — **dòng 1027**; **dòng 1029** ghi `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])` → **FR này KHÔNG có mã UC trong SRS**, cấm bịa mã UC trong note gửi đối tác.

### Thứ tự đo (đo web TRƯỚC, đọc SRS SAU)

- Danh sách nhóm + trường quan sát được đã viết ra **TRƯỚC** khi mở SRS, bằng cách đọc thô cây DOM (`label innerText`, **không dùng `textContent`**) + ảnh chụp đã mở đọc. Sau đó mới đối chiếu SRS.

### 3 trường đối tác báo thiếu — kết quả đo trên web hiện tại

- **Số quyết định công bố** (SRS **dòng 1692**, nhóm 4 "Công bố", ô văn bản, *Tùy chọn*): ✅ **CÓ**. Ô nhập nằm dưới tiêu đề "Công bố", **hiện sẵn ngay khi vừa mở biểu mẫu**, không phải mở nhóm nào.
- **Ngày quyết định công bố** (SRS **dòng 1693**, nhóm 4 "Công bố", bộ chọn ngày, *Tùy chọn*): ✅ **CÓ**. Là bộ chọn ngày thật (có biểu tượng lịch), hiện sẵn cạnh ô trên.
- **Tệp đính kèm** (SRS **dòng 1694**, nhóm 5 "File đính kèm", tải nhiều file, PDF/DOC/DOCX/XLS/XLSX, tối đa 20MB/file): ✅ **CÓ**. Vùng kéo-thả dưới tiêu đề "Tệp đính kèm", chú thích trên web: *"Tối đa 10 tệp. Định dạng: .pdf, .doc, .docx, .xls, .xlsx. Dung lượng tối đa: 20MB/tệp."* — định dạng và giới hạn 20MB **khớp đúng** SRS.
- Tìm bằng **≥2 cách độc lập** đúng yêu cầu: (1) theo chữ trên nhãn, (2) theo **loại điều khiển** — đếm được `input[type=file]` = 1, `.ant-upload-drag` = 1, `.ant-picker` = 2 (Ngày cấp + Ngày QĐ công bố). Hai cách cho cùng kết quả.
- **Nguồn thứ 2 độc lập trong SRS** (mục Inputs của FR-IV-NEW-01) xác nhận cùng 3 trường: `so_qd_cong_bo` **dòng 1060** · `ngay_qd_cong_bo` **dòng 1061** · `file_dinh_kem` **dòng 1063**. Cả 3 được quy định ở **2 chỗ độc lập** → yêu cầu rõ ràng, không phải suy diễn.
- **Điều kiện ẩn/hiện:** đã đọc kỹ cột "Hành vi" của các dòng 1691–1694 và phần mô tả nhóm — **SRS KHÔNG đặt bất kỳ điều kiện ẩn/hiện nào** cho 3 trường này. ⇒ SRS đòi chúng **luôn hiện** ở biểu mẫu Thêm mới. Web đang đáp ứng.

### Đối chiếu ĐỦ/THIẾU **TỪNG** trường theo bảng Thành phần màn hình (dòng 1673–1696)

- Nhóm 1 — **dòng 1676–1682**: Tên tổ chức * ✅ · Loại hình * ✅ (đúng 4 lựa chọn "Công ty Luật / Văn phòng Luật sư / Trung tâm Tư vấn Pháp luật / Khác" như dòng 1678) · Người đại diện * ✅ · Chức vụ người đại diện ✅ · Số Giấy ĐKHĐ * ✅ · Ngày cấp * ✅.
- Nhóm 2 — **dòng 1683–1685**: Lĩnh vực pháp luật * ✅ (chọn nhiều) · Số lao động ✅ (ô số, nhập 25 nhận bình thường).
- Nhóm 3 — **dòng 1686–1690**: Địa chỉ trụ sở * ✅ · Số điện thoại ✅ · Email ✅ · Website ✅.
- Nhóm 4 — **dòng 1691–1693**: Số quyết định công bố ✅ · Ngày quyết định công bố ✅.
- Nhóm 5 — **dòng 1694**: File đính kèm ✅.
- Nhóm 6 — **dòng 1695**: Ghi chú ✅ (ô văn bản dài).
- **Dòng 1696**: 2 nút **Hủy / Lưu** ✅ — đúng 2 nút, đúng tên.
- ⇒ **Không thiếu trường nào** so với bảng Thành phần màn hình. Tổng cộng 16 ô nhập, khớp đủ 15 trường SRS liệt kê (+1 vùng tải tệp).

### 3 trường có dùng được thật không (không chỉ hiển thị)

- Đã nhập **Số QĐ công bố** = `QD-CB-QA-0803/2026`, chọn **Ngày QĐ công bố** = `15/07/2026`, đính **1 tệp PDF hợp lệ** (`QA-QD-cong-bo-QLDMTCTV06.pdf`, 613 B) rồi bấm **Lưu**.
- Kết quả: tạo thành công bản ghi **`TC-BTP-TW-0003`**, vào đúng trạng thái **"Mới đăng ký"** (khớp dòng 1696 và bước 5 phần Processing).
- **Dữ liệu 3 trường được lưu thật:** mở lại bản ghi ở **màn Chi tiết** thấy "Số QĐ công bố: QD-CB-QA-0803/2026" và "Ngày QĐ công bố: 15/07/2026"; mở tiếp ở **chế độ Chỉnh sửa** thấy đủ cả 3 — kể cả tệp đính kèm còn nguyên kèm nút "Xem"/"Xóa". Sau **tải lại trang bỏ qua bộ nhớ đệm** vẫn còn đủ ⇒ dữ liệu nằm ở máy chủ, không phải chỉ trên màn hình.
- Đo kèm số request: **1 request** `POST /api/v1/to-chuc-tu-vans` / **1 khung thông báo** "Tạo Tổ chức tư vấn thành công" → không có thông báo lặp, không tạo trùng bản ghi.

### 🔴 Sai lệch so với SRS vẫn còn (KHÔNG thuộc phản ánh của đối tác)

- **Dòng 1664** ghi "Loại màn hình: Biểu mẫu nhập liệu (**6 nhóm**)"; **dòng 1669** đặt tên 6 nhóm; các **dòng 1676 / 1683 / 1686 / 1691** đều ghi loại UI là "**nhóm thu gọn**" (riêng nhóm 1 dòng 1676 ghi "Mặc định mở").
- Thực tế web: **KHÔNG có nhóm thu gọn nào** (rà toàn bộ cây DOM: 0 `.ant-collapse`, 0 accordion, 0 fieldset). Chỉ có **2 tiêu đề phân cách** là "Công bố" và "Tệp đính kèm"; 4 nhóm còn lại (Thông tin cơ bản, Lĩnh vực & Nhân sự, Liên hệ, Ghi chú) **không có tiêu đề nhóm**. Toàn bộ trường hiện phẳng trên một trang.
- **Không làm đổi verdict của case này**: đối tác phản ánh **thiếu trường**, mà cả 15 trường + vùng tải tệp đều đã có và dùng được. Đây là sai lệch về **cách gom nhóm**, ghi ra để BA/dev biết (xem §Ngoài phạm vi).

---

## Kết luận

- Phản ánh của đối tác **KHÔNG còn tái hiện** trên bản dựng hiện tại `HTPLDN · V1.0.5`, kiểm ở đúng vai trò `CB_NV_TW` + đúng đơn vị `BTP · TW` như ảnh đối tác:
  - **Số quyết định công bố → đã có**, hiện sẵn khi vừa mở biểu mẫu.
  - **Ngày quyết định công bố → đã có**, là bộ chọn ngày thật.
  - **Tệp đính kèm → đã có**, kèm đúng ràng buộc định dạng và 20MB/tệp như đặc tả.
- Cả 3 **không chỉ hiển thị mà còn lưu được dữ liệu thật** — chứng minh bằng bản ghi `TC-BTP-TW-0003` do đội kiểm thử tự tạo, mở lại vẫn đủ dữ liệu sau khi tải lại trang.
- Xác nhận thêm: đối tác **không hề thao tác sai** — ảnh của họ cho thấy biểu mẫu bản cũ thật sự thiếu 3 trường, và biểu mẫu đó **không có nhóm thu gọn nào để mà bỏ sót**. Vì vậy **KHÔNG dùng `Reject`**.
- Mỗi kết luận dựa trên 2 phương pháp độc lập cho kết quả trùng nhau: đọc thô cây DOM và ảnh chụp full-res **đã mở ra đọc**.
- Không có lỗi trong bảng điều khiển trình duyệt; các lệnh gọi máy chủ đều 200/304.
- **⇒ Verdict: `Pass`** (cột Q — Verify). Cột P giữ nguyên `dev done`, KHÔNG đụng tới.

## Ngoài phạm vi case (chưa log — chờ user quyết)

1. **Biểu mẫu không chia 6 nhóm thu gọn như đặc tả.** SRS dòng 1664 / 1669 / 1676 / 1683 / 1686 / 1691 mô tả 6 nhóm dạng "nhóm thu gọn"; web để phẳng, chỉ có 2 tiêu đề phân cách "Công bố" và "Tệp đính kèm". Không ảnh hưởng việc nhập liệu.
2. **Thứ tự trường khác SRS.** SRS gom "Lĩnh vực pháp luật + Số lao động" vào nhóm 2 rồi mới tới nhóm Liên hệ; web đặt "Số lao động" cạnh "Địa chỉ" và đẩy "Lĩnh vực pháp lý" xuống sau "Website".
3. **Vài nhãn rút gọn so với SRS.** SRS "Số Giấy đăng ký hành nghề" → web "Số Giấy ĐKHĐ Sở TP"; SRS "Ngày cấp Giấy đăng ký hành nghề" → web "Ngày cấp"; SRS "Địa chỉ trụ sở" → web "Địa chỉ"; SRS "Lĩnh vực pháp luật" → web "Lĩnh vực pháp lý". Nghĩa không đổi.
4. **Mâu thuẫn nội tại của SRS (để BA chốt, không dùng chấm case).** Bảng màn hình dòng 1681–1682 đánh dấu "Số Giấy ĐKHĐ" và "Ngày cấp" là **bắt buộc (\*)**, nhưng bảng Inputs của FR dòng 1052–1053 lại ghi Bắt buộc = **N**. Web đang làm theo bảng màn hình (bắt buộc) — cũng khớp bước 3 phần Processing (dòng 1073).
5. **Màn Chi tiết chưa thấy vùng tệp đính kèm.** Bản ghi vừa tạo có tệp, nhưng màn Chi tiết chỉ liệt kê thông tin chữ, phải vào Chỉnh sửa mới thấy tệp. Đây là màn khác (SCR-IV-NEW-03) và có thể phụ thuộc trạng thái "Mới đăng ký" nên **chưa kết luận**, chỉ ghi nhận.

## Ghi chú đo lường (chống lặp lại lỗi 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js`, **không lọc trùng**, đọc bằng `innerText`; đã tự kiểm `soObserverDangSong = 1` **trước** khi tin số liệu.
- Thao tác đổi trạng thái (tạo bản ghi) đo kèm số request: **1 request / 1 khung thông báo** → không lặp.
- Mọi ảnh đều **đã được mở ra đọc**, không chỉ lưu. Một ảnh bị đặt tên nhắc tới "thông báo" trong khi điểm ảnh không có thông báo (thông báo đã tự tắt trước khi chụp) → **đã đổi tên cho khớp nội dung thật** thành `...-sau-khi-luu-danh-sach-moi-dang-ky-tang-len-2.png`.
- **Hai lần selector của QA sai, KHÔNG phải lỗi ứng dụng** (đã kiểm lại bằng mã HTML thô nên không log oan): (1) đếm tệp đã đính bằng `.ant-upload-list-item` ra 0 trong khi tệp vẫn đính đúng — ứng dụng dựng danh sách tệp bằng cách riêng; (2) dò chú thích trợ giúp bằng `.anticon-question-circle` toàn trang thì trúng biểu tượng ở menu bên trái thay vì biểu tượng trong biểu mẫu.
- **Cảnh báo về phép đo, không phải lỗi ứng dụng:** ảnh chụp chế độ "toàn trang" của công cụ kiểm thử **dựng hình không đáng tin** với phần vừa thay đổi — một lần cho ra biểu mẫu trắng trơn và một lần thiếu dòng tệp vừa đính, trong khi cây DOM đo ngay sau đó vẫn đủ dữ liệu. Đã kiểm chứng bằng phép thử phân biệt: **thu phóng khung nhìn thật (1440→1100) KHÔNG hề làm mất dữ liệu đang nhập** ⇒ đây là hiện tượng của công cụ chụp ảnh, không phải hành vi ứng dụng, nên **KHÔNG log**. Từ đó chuyển sang chụp theo khung nhìn + cuộn để lấy bằng chứng.
