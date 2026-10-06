# Tiêu chí verify — QLTLPLCVV_15 (tab `bug`, dòng 299)

Mã case: QLTLPLCVV_15          Thời điểm viết: 2026-08-06 11:17
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN V1.0.8** (chuỗi phiên bản
in ở chân logo trong trang; bó mã giao diện `assets/index-CNwX9JjX.js`) — đo lúc 2026-08-06 11:19–11:32.
Đã tra `/api/v1/health` (404, không có endpoint công bố phiên bản) và các header phản hồi (không có).

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A):
`reverify-week-3/cond/QLTLPLCVV_15.md` (đo 21/07/2026) · `reverify-week-3/reverify-audit/QLTLPLCVV_15/note-sheet.txt` ·
`reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-tvcs.md` (BA duyệt 24/07/2026) ·
khối "CÁCH VERIFY sau Dev fix" trong `reverify-week-3/dev-fix-reverify-round-3-2026-07-25/queue.json`.
Mục 4 dưới đây suy từ **đặc tả** (SRS v3.5 dòng 871–872 + 966–969), **không** lấy số đo cũ làm ngưỡng.

---

1. **Đối tác phản ánh** (1 vế duy nhất — về câu chữ thông báo, không phải về việc chặn):
   - (a) Tải tệp đính kèm **chứa mã độc** trong cửa sổ chỉnh sửa tư liệu → hệ thống chỉ báo **"Tải file thất bại"**
     (thông báo chung chung), thay vì thông báo nêu rõ **tệp chứa mã độc + tên tệp**.
   - Đối tác **không** phản ánh việc mã độc lọt qua — ảnh cho thấy tệp bị chặn, tranh chấp nằm ở nội dung thông báo.

   Bằng chứng: `partner-evidence/QLTLPLCVV_15.jpg` (đã mở full-res). Thấy: modal sửa tư liệu "TKM kiểm thử chức năng"
   (Loại tư liệu = Tài liệu, Lĩnh vực = Doanh nghiệp), toast đỏ ✗ **"Tải file thất bại"** góc trên, widget
   "File đính kèm" ghi hạn mức *"Tối đa 10 tệp. Định dạng: .doc, .docx, .xls, .xlsx, .pdf, .jpg, .png, .gif.
   Dung lượng tối đa: 20MB"*, dòng tệp `2K15 T5 (16.7) & T7 (18.7).pdf`, nút [Hủy] [Cập nhật].

2. **Đặc tả nói gì** (mở file đọc trực tiếp — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`):
   - `srs-fr-12-tv-chuyen-sau.md:871` — Tải lên file, bước 2: `| 2 | Kiểm tra file: max 20MB, định dạng cho phép | EC-FILE-01 |`
   - `srs-fr-12-tv-chuyen-sau.md:872` — Tải lên file, bước 3: `| 3 | Quét virus | — |`
   - `srs-fr-12-tv-chuyen-sau.md:968` — `| E3 | File vượt 20MB | ERR-TLPL-03 | "File tối đa 20MB" | ERROR |`
   - `srs-fr-12-tv-chuyen-sau.md:969` — `| E4 | File chứa mã độc | ERR-TLPL-04 | "File '{ten_file}' chứa mã độc" | ERROR |`
   - `srs-fr-12-tv-chuyen-sau.md:978` — AC: *"**Given** CB NV tải lên file **When** chọn file hợp lệ **Then** upload + quét virus + lưu"*
   ⇒ Đặc tả **nói rõ** và **khớp** kỳ vọng đối tác: quét virus là một bước riêng, và khi bắt được mã độc phải phản hồi
   một thông báo **riêng biệt** nêu tệp chứa mã độc + tên tệp — không dùng chung câu lỗi tải tệp thất bại.
   Có thêm **quyết định BA ngày 24/07/2026** (`reverify-week-3/ba-confirm/phan-hoi/phan-hoi-ba/phan-hoi-ba-confirmation-needed-tvcs.md`
   dòng 141–144): *Loại 1 — Lỗi phần mềm, Dev sửa theo SRS* + yêu cầu Dev **xác nhận việc chặn đúng do quét virus**.

   **IM LẶNG về:** ký tự bao tên tệp (`'…'` hay `«…»`); có kèm cụm *"không thể tải lên"* hay không; vị trí hiển thị
   (toast / inline / modal); mã lỗi có lộ ra giao diện hay không; hành vi khi tệp mã độc **không** phải định dạng cho phép.

3. **Precondition:**
   - Tài khoản: `cbnv_tw` / `Test@1234` (vai trò CB_NV_TW — trùng vai trò trên ảnh đối tác "Cán bộ NV Trung ương").
     Fallback theo Rule 7 nếu khoá: `cbnv_tw_01` → `cbnv_tw_02` (giữ nguyên vai trò + cấp TW).
   - Màn: `https://18.143.165.120.nip.io/tv-chuyen-sau/{id}` → nhóm **"Tư liệu pháp luật liên kết"** → form Thêm/Sửa
     tư liệu → widget **File đính kèm**.
   - Dữ liệu tiền đề: 1 TVCS thuộc phạm vi đơn vị TW + 1 tư liệu trạng thái **NHAP** (tư liệu CONG_KHAI bị chặn sửa
     theo `srs-fr-12-tv-chuyen-sau.md:902` → không dùng được làm bàn thử). Chưa có → **tự tạo** bằng luồng chuẩn
     (nút [Thêm tư liệu]).

4. **✅ PASS khi (đủ cả 4, đo được):**
   - (a) Tệp **A** (PDF hợp lệ có nhúng chữ ký thử mã độc chuẩn EICAR) **bị từ chối** — sau khi đóng và mở lại tư liệu,
     tệp A **không** nằm trong danh sách đính kèm (đếm số tệp trước/sau bằng nhau).
   - (b) Thông báo hệ thống trả về khi từ chối tệp A **nêu rõ nguyên nhân là tệp chứa mã độc** VÀ **nêu tên tệp**.
   - (c) Thông báo của tệp A **khác hẳn** thông báo của tệp **C** (PDF sạch > 20MB, bị chặn vì dung lượng) — đây là
     phép đối chứng chứng minh tệp A bị chặn ở **bước quét virus** chứ không phải ở bước kiểm dung lượng/định dạng.
   - (d) Tệp **B** (PDF sạch, hợp lệ, < 20MB) **đính kèm thành công** — không bị chặn oan.

   **❌ FAIL nếu:** tệp A vẫn đính kèm thành công (mã độc lọt qua → nâng thành lỗ hổng bảo mật, báo ngay) ·
   tệp A bị chặn nhưng thông báo vẫn chung chung kiểu *"Tải file thất bại"* / không nêu mã độc / không nêu tên tệp ·
   thông báo của A trùng y hệt thông báo của C · tệp B bị chặn oan.

   **KHÔNG được chấm Fail vì:** dùng `'…'` thay vì `«…»`; thiếu/thừa cụm *"không thể tải lên"*; hiển thị dạng toast
   thay vì inline; không lộ mã `ERR-TLPL-04` ra giao diện — đặc tả im lặng về 4 điểm này (xem mục 2).

5. **Dạng dữ liệu phải phủ — M = 3:**
   - **A** — PDF hợp lệ (`%PDF-` header thật) có **nhúng nguyên chuỗi EICAR 68 byte**, < 20MB, đuôi `.pdf`.
   - **B** — PDF sạch bình thường, < 20MB, đuôi `.pdf`.
   - **C** — PDF sạch **> 20MB**, đuôi `.pdf`.

   **Nguồn xác định M:** đặc tả tách luồng "Tải lên file" thành 2 cổng liên tiếp — bước 2 kiểm dung lượng/định dạng
   (`:871`) và bước 3 quét virus (`:872`) — và gán **2 mã lỗi khác nhau** cho 2 cổng đó (E3 `:968` vs E4 `:969`).
   Muốn khẳng định tệp A bị chặn bởi **bước 3** chứ không phải bước 2 thì bắt buộc phải có mẫu đối chứng cho
   **cả hai cổng** (C cho bước 2) và một mẫu **đi lọt cả hai** (B). M = 1 không đủ để phân biệt.

   ⚠️ Bẫy đã biết: tệp EICAR **thô** đổi đuôi `.pdf` bị chặn ở **bước 2** (nội dung không khớp định dạng) → cho ra
   thông báo về định dạng, rất dễ kết luận nhầm là đã PASS. Bắt buộc dùng PDF **hợp lệ** nhúng EICAR.

6. **Bảng điều kiện:**

   | Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
   |---|---|---|:-:|
   | Vai trò / tài khoản | CB_NV_TW ("Cán bộ NV Trung ương", BTP · TW) | `cbnv_tw` — CB_NV_TW, `capDonVi = TW`, `donViId = 00000000-0000-4000-8000-000000000001` (trùng khít vai trò + cấp, không phải nới) | Không |
   | Entity + trạng thái | Tư liệu pháp luật "TKM kiểm thử chức năng" của 1 TVCS; đang mở form **Sửa** (nút [Cập nhật]); tư liệu chưa công khai (dòng bảng còn nút [Công khai]) | Tư liệu "QA QLTLPLCVV_15 - kiem thu tep chua ma doc 06/08/2026" (id `18183dfb-…`) trạng thái **Nháp**, thuộc TVCS-20260805-0001 (đơn vị TW); mở đúng cửa sổ **Sửa tư liệu pháp luật**, cùng widget "File đính kèm" | Không |
   | Dữ liệu tiền đề | Tệp `2K15 T5 (16.7) & T7 (18.7).pdf` — đối tác khai là tệp chứa mã độc; nội dung thật không rõ | 3 tệp tự dựng: **A** PDF hợp lệ 732 B nhúng EICAR chuẩn (đã mở đọc được bằng PyMuPDF ⇒ chắc chắn qua cổng định dạng) · **B** PDF sạch 594 B · **C** PDF sạch 23.069.772 B. Đối tác không cho biết nội dung tệp thật ⇒ đã đóng bằng cách **thử đủ mọi nhánh khả dĩ** (mã độc / sạch / vượt dung lượng, và thêm nhánh EICAR thô đổi đuôi qua đường máy chủ) — mọi nhánh đều cho kết quả nhất quán | Không |
   | Input / filter / giá trị nhập | Thao tác "Tải tệp" trong cửa sổ chỉnh sửa hồ sơ, định dạng `.pdf` (nằm trong danh sách cho phép) | Cùng thao tác, cùng widget, cùng đuôi `.pdf` cho cả A/B/C; đo thêm bằng đường thứ hai (gọi thẳng máy chủ) cho A'/B'/C'/D' | Không |
   | Độ phủ biến thể (N bản ghi, M dạng) | 1 lần thử, 1 tệp (M = 1) — không có mẫu đối chứng để biết chặn do quét virus hay do cổng khác | N = 1 tư liệu, **M = 3** dạng tệp (A mã độc · B sạch · C vượt dung lượng) + 1 nhánh phụ D (EICAR thô) — đủ phân biệt 2 cổng | Không |

   **3 dữ kiện neo của đối tác:** `htpldn-uat.ospgroup.vn/tv-chuyen-sau/287c1cd1-ea2e-4d17-8f2d-9be79d617167` ·
   tư liệu "TKM kiểm thử chức năng" chưa công khai, đang mở form Sửa · CB_NV_TW, env **`htpldn-uat.ospgroup.vn`**,
   thời điểm 17/07/2026 20:24.

   **Giới hạn hiệu lực (không phải GAP):** đối tác đo trên env `htpldn-uat.ospgroup.vn`; lượt này đo trên env
   `18.143.165.120.nip.io` theo chỉ định của prompt. Verdict chỉ có hiệu lực cho env + bản dựng ghi ở đầu file.

---

## 7. Kết quả đo (giai đoạn B) — đối chiếu từng tiêu chí mục 4

| Tiêu chí | Đo được | Đạt? |
|---|---|:-:|
| (a) Tệp A bị từ chối, không nằm trong danh sách đính kèm | Widget sau thao tác chỉ còn `B-pdf-sach.pdf`; sau [Lưu] cột File = **1**; đọc lại bản ghi `files = [B-pdf-sach.pdf]`; **tải lại trang** rồi mở lại cửa sổ Sửa vẫn chỉ có B | ✅ |
| (b) Thông báo nêu rõ tệp chứa mã độc + tên tệp | `Tệp «A-eicar-nhung-trong-pdf-hop-le.pdf» chứa mã độc, không thể tải lên` (bắt bằng innerText; máy chủ trả HTTP 400 `ERR-TLPL-04` cùng nguyên văn câu đó) | ✅ |
| (c) Thông báo của A khác hẳn thông báo của C | C: `C-pdf-sach-vuot-20mb.pdf: Kích thước vượt quá giới hạn 20MB.` (0 request — giao diện chặn trước). Hai câu khác hẳn nhau ⇒ A bị chặn ở **bước quét virus**, không phải bước dung lượng/định dạng | ✅ |
| (d) Tệp B đính kèm thành công | 1 request, **0** thông báo lỗi, widget hiện `B-pdf-sach.pdf (594 B)`; máy chủ trả 201 `trangThaiQuet = "SACH"` | ✅ |

**Bộ bắt thông báo:** dùng script dùng chung `tools/toast-capture.js` (không lọc trùng · đọc `innerText` ·
đếm request song song). Đã chạy tự kiểm trước khi tin số liệu: `soObserverDangSong = 1`.
Mọi lượt đo đều **1 request ↔ 1 khung thông báo**, không có double-toast.

**Đường đo thứ hai (gọi thẳng máy chủ, cùng hành động):** A' EICAR-trong-PDF → 400 `ERR-TLPL-04` ·
B' PDF sạch → 201 `SACH` · D' EICAR thô đổi đuôi `.pdf` → 400 `ERR-TLPL-04` · C' > 20MB → 413
`ERR-SYS-00-00-01`. Giao diện và máy chủ **không mâu thuẫn**.

**Hạn chế đã ghi nhận:** ảnh chụp qua công cụ KHÔNG bắt được lớp thông báo của thư viện giao diện
(thử 4 lượt, gồm cả hẹn giờ thao tác trước rồi mới chụp và lặp thao tác 25 lượt × 2s). Đã đo trực tiếp
trên DOM để chứng minh khung thông báo có hiển thị thật với người dùng: `position: fixed`, `top: 8px`,
khung `x=0 y=8 w=1440 h=56`, `opacity: 1`, `z-index: 2010`, sống **3,34 giây**. Bằng chứng thay thế =
chữ bắt bằng `innerText` + nguyên văn phản hồi máy chủ, lưu ở
`image/A-02-thong-bao-va-phan-hoi-may-chu.txt`.

**Dữ liệu đã dựng trên env verify** (khai theo yêu cầu): tạo mới 1 tư liệu pháp luật
`QA QLTLPLCVV_15 - kiem thu tep chua ma doc 06/08/2026` (id `18183dfb-d95d-4b65-9cbf-a370357dea72`,
trạng thái Nháp, 1 tệp sạch đính kèm) trong TVCS-20260805-0001, trên `18.143.165.120.nip.io`.
Không đụng dữ liệu nào có sẵn.

## 8. Verdict

**Pass** — đủ 4 tiêu chí mục 4, 0 GAP, đủ M = 3 dạng, chạy đủ luồng tới đúng bước sinh ra lỗi cũ bằng
thao tác giao diện thật, có đường đo thứ hai xác nhận.

⚠️ **Giới hạn hiệu lực:** Pass này chỉ có hiệu lực cho môi trường `18.143.165.120.nip.io` và bản dựng
**V1.0.8**. Đối tác báo lỗi trên `htpldn-uat.ospgroup.vn` — chưa đối chiếu bản dựng của env đó.

⚠️ **Không kết luận "fix đã có tác dụng":** không có ảnh "lỗi cũ" do chính mình chụp trên bản dựng
trước khi sửa, nên chỉ kết luận được **hiện trạng đúng đặc tả**, không kết luận được về tác dụng của
bản sửa.

---

## Mục sửa đổi

- **2026-08-06 11:32** — không sửa mục 4 và mục 5. Chỉ **bổ sung** vào mục 6 (cột "Mình test lần này"):
  id bản ghi thật, kích thước 3 tệp, và ghi rõ cách đóng GAP "nội dung tệp thật của đối tác không rõ"
  (thử đủ mọi nhánh khả dĩ). Bổ sung mục 7 + 8 là phần kết quả, không phải đổi tiêu chí.
