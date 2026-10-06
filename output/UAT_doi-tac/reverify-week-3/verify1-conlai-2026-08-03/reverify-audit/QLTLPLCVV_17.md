# QLTLPLCVV_17 — Reverify audit (verify vòng 1, 2026-08-03)

Row 326 · tab `UAT_TGPL Doanh Nghiệp-tuần 3` · Mã TC `QLTLPLCVV_17`
Đối tác phản ánh: **Nhóm 3 "Tư liệu pháp lý" — nút "Xem" tệp bị VÔ HIỆU HÓA (bấm không được).**

**VERDICT: `Pass`** — dev khai đã fix, QA test lại trên bản đang chạy thì nút [Xem] dùng được ở cả 2 vai trò, mở đúng nội dung tệp.

---

## Note dev trước khi QA đè (đọc ô R326 lúc 2026-08-03 21:45 bằng gspread)

> Nguyên văn, không tóm tắt:

```
Đã fix (BUG thật, SRS FR-12 dòng 979/981): nút "Xem" tệp trong FileUpload bị vô hiệu do kế thừa DisabledContext của Form chỉ-đọc → set disabled tường minh (chỉ chặn khi đang quét virus). Fix chung mọi nhóm tệp. Commit 92b956d. Verify e2e: Xem PDF online GET download 200.
```

**Các ô khác của row 326 (để đối chiếu, không bị đè):**

| Cột | Header | Giá trị |
|---|---|---|
| C | Tuần | Tuần 3 |
| D | Mã TC | QLTLPLCVV_17 |
| G | Mô tả | Xem tệp trực tuyến |
| H | Điều kiện | 1. Đăng nhập hệ thống thành công |
| J | Các bước thực hiện | 1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu" / 2. Nhấn "Xem chi tiết" tại bản ghi / 3. Mở Nhóm 3 — Tư liệu pháp lý liên kết / 4. Bấm vào tên tệp đính kèm |
| K | Kết quả mong đợi | Hệ thống mở trình xem trực tuyến cho định dạng hỗ trợ (PDF, hình ảnh). Định dạng không hỗ trợ xem trực tuyến, hệ thống tải tệp về máy người dùng. |
| L | Kết quả thực tế | Hệ thống disable nút chức năng Xem |
| M | Ảnh/vieo 1 | QLTLPLCVV_17_v2.jpg |
| N | Trạng thái 1 | Fail |
| P | Trạng thái dev fix 1 | dev done |
| Q | Verify | (TRỐNG → QA ghi `Pass`) |
| R | DEV phản hồi lần 1 | (nguyên văn ở trên — QA đè bằng note partner-facing) |

---

## CỔNG 1 — Bằng chứng đối tác (đã mở full-res)

File: `partner-evidence/QLTLPLCVV_17_v2.jpg` (214.164 bytes) — ảnh tĩnh, mở bằng Read tool ở độ phân giải gốc 1920×1041.

**3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**

| # | Dữ kiện | Giá trị đọc được trên ảnh |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/tv-chuyen-sau/07e06acc-bdfc-43af-9e62-d600bdc4c258` — màn chi tiết Tư vấn chuyên sâu (env của đối tác, khác env QA được giao) |
| (b) | Vai trò + trạng thái | Badge góc phải: **"Cán bộ NV Trung ương · CB_NV_TW"**, đơn vị **BTP · TW**. **KHÔNG phải chuyên gia.** Hàng tư liệu phía sau hộp thoại có hành động `Xem tệp / Hủy công khai / Xóa` ⇒ tư liệu đang ở trạng thái **Đã công khai** |
| (c) | Dữ liệu tiền đề | 1 tư liệu tên "tài liệu kiểm thử", Loại tư liệu = **Tài liệu**, Lĩnh vực = Sở hữu trí tuệ, Mô tả = "tkm", **1 tệp đính kèm `Báo cáo mẫu.docx`** (định dạng .docx — KHÔNG thuộc nhóm xem trực tuyến được). Ngày trên máy đối tác: 03/08/2026 10:31 |

> Lưu ý quan trọng rút ra từ ảnh: đối tác đo ở vai trò **Cán bộ nghiệp vụ**, không phải chuyên gia — dù dev dẫn dòng SRS nói về chuyên gia. Vì vậy QA đo **cả hai** vai trò.

## CỔNG 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem + chỗ chứa LỖI:** ảnh `QLTLPLCVV_17_v2.jpg`, vùng dưới cùng hộp thoại "File đính kèm": dòng `📎 Báo cáo mẫu.docx` kèm chữ `👁 Xem` **màu xám nhạt**, trong khi nút `Xem tệp` của bảng phía sau vẫn màu xanh → nút [Xem] trong hộp thoại bị vô hiệu hoá.
2. **Đối tác phản ánh CỤ THỂ:** trong hộp thoại xem tư liệu (chỉ có nút [Đóng]), nút [Xem] cạnh tên tệp bấm không được, nên không mở/tải được tệp.
3. **Data + bước tái hiện:** mở TVCS → Nhóm 3 "Tư liệu pháp lý liên kết" → bấm [Xem tệp] ở hàng tư liệu đã công khai có tệp đính kèm → trong hộp thoại bấm [Xem] cạnh tên tệp.

## CỔNG 3 — Đối chiếu SRS vs web

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md`
Chức năng: **FR-X.1-06 — Quản lý tư liệu pháp lý của vụ việc**, `**UC Reference:** UC 152` (dòng 811).

- `srs-fr-12-tv-chuyen-sau.md:981` — *"**Given** CB NV xem file trực tuyến **When** chọn file **Then** hiển thị preview"* → **web ĐÁP ỨNG**: CB_NV_TW bấm [Xem] trên .pdf mở trình xem trực tuyến render đúng nội dung; trên .png mở khung xem ảnh render đúng ảnh.
- `srs-fr-12-tv-chuyen-sau.md:979` — *"[STT63 UAT 2026-06-02] **Given** Chuyên gia được phân công mở section "Tư liệu pháp lý" của TVCS mình phụ trách (trạng thái ≥ PHAN_CONG) **When** xem/tải tư liệu **Then** hiển thị chế độ chỉ đọc (xem + tải/preview), ẩn nút Thêm/Sửa/Xóa/Công khai (BR-AUTH-14); ghi AUDIT_LOG hành vi đọc/tải (BR-DATA-05)"* → **web ĐÁP ỨNG**: chuyên gia được phân công thấy tư liệu ở chế độ chỉ đọc (mất nút "Thêm tư liệu", hàng chỉ còn [Xem tệp], không có Sửa/Công khai/Xóa) và [Xem] vẫn dùng được cho cả 3 định dạng.
- `srs-fr-12-tv-chuyen-sau.md:815` — màn `SCR-X1-07` **DEPRECATED v2.1**, gộp thành tab "Tư liệu PL" trong `SCR-X1-02 / MH-12.2` → surface QA đo (accordion "Tư liệu pháp lý liên kết" trong màn chi tiết TVCS) là **đúng surface còn hiệu lực**, không đo nhầm màn đã bỏ.
- `srs-fr-12-tv-chuyen-sau.md:820, :826, :853, :936` — CB NV = CRUD theo đơn vị (BR-AUTH-08); CG = chỉ đọc/tải đích danh TVCS `chuyen_gia_id` = mình và trạng thái ≥ PHAN_CONG (BR-AUTH-14). Khớp quan sát.
- **Kiểm nhãn `[GAP-...]`:** các nhãn `[GAP-X.1-02]` trong nhóm này nằm ở phần Processing *Chỉnh sửa / Xóa mềm / Xóa file / Tìm kiếm* (dòng 896, 907, 918, 929) — **KHÔNG** dán lên hai tiêu chí 979/981 mà case này đo. ⇒ yêu cầu đang đo là yêu cầu đã chốt, **không** rơi vào diện "SRS chưa chốt → BA confirm".

### Nhận xét: dev dẫn SRS dòng 979/981 có ĐÚNG không?

**ĐÚNG — đã mở file đọc lại đúng 2 dòng đó, không dùng trí nhớ.** Dòng 979 đúng là quy định chuyên gia được phân công xem/tải ở chế độ chỉ đọc (BR-AUTH-14); dòng 981 đúng là quy định CB NV xem file trực tuyến thì hiển thị preview. Cả hai đều nằm trong khối Acceptance Criteria của FR-X.1-06 và đều là căn cứ hợp lệ cho lỗi mà đối tác báo. Dev ghi "FR-12" là nói theo số nhóm/tên file (`srs-fr-12-...`), còn mã FR bên trong là `FR-X.1-06` — cách gọi tắt, không sai lệch nội dung.

Tuy vậy **claim của dev vẫn không được dùng làm căn cứ verdict** — verdict dưới đây dựa trên số đo QA tự chạy.

---

## Điều kiện QA đã dựng (Nguyên tắc 4 — thiếu tiền đề thì TỰ SEED)

Ban đầu Nhóm 3 của mọi TVCS trên env đều rỗng — hiện đúng chữ **"Chưa có tư liệu pháp luật đính kèm."** (empty state hợp lệ, KHÔNG phải "Chức năng đang phát triển") ⇒ phải seed, không phải blocker.

- TVCS dùng: **`TVCS-20260803-0002`** (id `73178d48-44d9-4198-87a9-5df4340c0736`), `trangThai = DANG_TU_VAN` (≥ PHAN_CONG ✓), `chuyenGiaId = 98cfd963-3cd3-4c8a-bfa9-625460824d6d` (= `qa_tvvseed28`).
- Tư liệu seed: **`QLTLPLCVV_17 - tu lieu kiem thu xem tep`** (id `69436ab9-170e-4ab7-910d-c52f5311ce5f`), loại **Tài liệu** (đúng loại đối tác dùng), đính **3 tệp THẬT** (`seed-files/`):
  - `Bao cao mau QLTLPLCVV17.docx` — 949 B — **khớp đúng định dạng .docx của đối tác**
  - `Tai lieu PDF QLTLPLCVV17.pdf` — 412 B — định dạng SRS bắt phải xem trực tuyến
  - `Anh minh hoa QLTLPLCVV17.png` — 33.533 B — định dạng ảnh
- Seed đo bằng `tools/toast-capture.js` (tự kiểm `soObserverDangSong = 1`): **1 request** `POST /api/v1/tu-lieu-phap-ly-vvs`, **1 khung thông báo** "Đã thêm tư liệu pháp luật", không lặp.
- Sau đó **công khai** tư liệu để khớp đúng trạng thái của đối tác: **1 request** `POST .../cong-khai`, **1 thông báo** "Đã công khai tư liệu" → hàng đổi thành `Đã công khai` + hành động `Xem tệp / Hủy công khai / Xóa` — **trùng khít hàng trong ảnh đối tác**.

---

## BẢNG ĐO CHÍNH — vai trò × trạng thái × (nút tồn tại / bị vô hiệu / bấm ra gì / nội dung tệp có hiện)

Đo bằng `evaluate_script` (đọc `disabled`, `pointer-events`, `opacity`, `color`, kích thước) **VÀ** bấm thật rồi quan sát. Mọi số dưới đây là số đo thực.

| Vai trò (tài khoản) | Trạng thái TVCS / tư liệu | Tệp | Nút [Xem] **có tồn tại**? | **Có bị vô hiệu**? (`disabled` · `pointer-events` · `opacity` · màu chữ · kích thước) | Bấm ra gì | **Nội dung tệp có hiện**? |
|---|---|---|---|---|---|---|
| **CB Nghiệp vụ TW** `cbnv_tw_04` (CB_NV_TW, BTP·TW) — *đúng vai trò đối tác* | TVCS `DANG_TU_VAN` · tư liệu **Nháp** | `.pdf` | Có (68×24 px) | **KHÔNG** — `disabled=false` · `auto` · `1` · `rgb(9,88,217)` xanh | Mở tab trình xem trực tuyến (URL ký sẵn) | **CÓ** — render trang 1/1, đọc được chữ "QA UAT QLTLPLCVV_17 - PDF xem truc tuyen" (ảnh `-04`) |
| ↑ | ↑ | `.png` | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · xanh | Mở khung xem ảnh (có thanh xoay/phóng) | **CÓ** — ảnh render đúng, `naturalWidth×Height = 200×80` khớp tệp gốc, `complete=true` (ảnh `-05`) |
| ↑ | ↑ | `.docx` | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · xanh | **Tải tệp về máy** (`<a download="Bao cao mau QLTLPLCVV17.docx">`) | **CÓ** — tệp thực 949 B, chữ ký `PK..` (OOXML hợp lệ), **≠ 0 byte** |
| **CB Nghiệp vụ TW** `cbnv_tw_04` | TVCS `DANG_TU_VAN` · tư liệu **Đã công khai** — *khớp khít trạng thái đối tác* | cả 3 | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · `rgb(9,88,217)` xanh | như trên | **CÓ** (ảnh `-06`: hàng `Xem tệp / Hủy công khai / Xóa` giống hệt ảnh đối tác, nhưng [Xem] **xanh** chứ không xám) |
| **Chuyên gia ĐƯỢC phân công** `qa_tvvseed28` (TVV · CG, BTP·TW) — *vai trò trọng tâm SRS:979* | TVCS `DANG_TU_VAN` (≥ PHAN_CONG) · tư liệu **Đã công khai** | `.pdf` | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · xanh · `cursor:pointer` | Mở tab trình xem trực tuyến | **CÓ** |
| ↑ | ↑ | `.png` | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · xanh | Mở khung xem ảnh | **CÓ** — `200×80`, `complete=true` |
| ↑ | ↑ | `.docx` | Có (68×24) | **KHÔNG** — `false` · `auto` · `1` · xanh | Tải tệp về máy | **CÓ** — blob kèm đúng tên tệp |
| **Chuyên gia KHÔNG được phân công** `qa_tvvseed28` trên TVCS `chuyen_gia_id = null` | `TVCS-20260725-0001` (TIEP_NHAN) · tư liệu **Nháp** | `.pdf` | — (không đo nút, đo tầng quyền) | — | Gọi thẳng API tải tệp | **CÓ — VẪN TẢI ĐƯỢC** (200, 604 B, `%PDF-`) ⇒ **không khớp** `srs-...:980`. Xem §Quan sát ngoài phạm vi |

**Phân biệt 3 khả năng mà đề bài yêu cầu tách bạch — kết quả trên bản đang chạy:**
- Nút **không tồn tại trong DOM**: KHÔNG xảy ra ở vai trò/trạng thái nào (luôn có, 68×24 px, `getClientRects()` khác rỗng).
- Nút tồn tại nhưng **bị vô hiệu** (`disabled` / `pointer-events:none` / mờ): KHÔNG xảy ra — cả 3 chỉ số đều ở trạng thái bật, màu chữ `rgb(9,88,217)` (xanh) chứ không phải xám.
- Nút bấm được nhưng **không mở được gì / cửa sổ trống / tệp 0 byte**: KHÔNG xảy ra — PDF render chữ, PNG render ảnh đúng kích thước gốc, DOCX tải về đủ 949 B đúng chữ ký OOXML.

## Phép thử thứ hai (đo lại bằng phương pháp KHÁC, theo 3-step verify)

UI cho kết quả "chạy được" → kiểm chứng lại bằng **gọi thẳng API** trong phiên của chính vai trò đang xét, để loại khả năng UI mở cửa sổ rỗng:

`GET /api/v1/tu-lieu-phap-ly-vvs/69436ab9-170e-4ab7-910d-c52f5311ce5f/files/{fileId}/download` → 200, trả liên kết tải ký sẵn; tải tiếp liên kết đó:

| Tệp | HTTP | Content-Type trả về | Số byte thực | Chữ ký đầu tệp | Khớp tệp gốc? |
|---|---|---|---|---|---|
| `.pdf` | 200 | `application/pdf` | **412** | `%PDF-1` | ✔ đúng 412 B |
| `.png` | 200 | `image/png` | **33.533** | `\x89PNG` | ✔ đúng 33.533 B |
| `.docx` | 200 | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` | **949** | `PK\x03\x04` | ✔ đúng 949 B |

⇒ **Hai phương pháp KHỚP nhau** (UI mở được + API trả đúng tệp thật, không tệp rỗng, không hỏng). Không có mâu thuẫn nào phải đẩy sang BA.

**Chống "JS cũ trong tab mở lâu":** đã **tải lại trang** (`reload`, bỏ qua cache) rồi đo lại lần cuối trên bản dựng hiển thị **HTPLDN · V1.0.5** — cả 3 nút [Xem] vẫn `disabled=false` · `pointer-events:auto` · `opacity:1` · màu xanh.

## Ảnh bằng chứng (đều đã mở đọc lại pixel, tên tệp khớp nội dung)

| Ảnh | Nội dung |
|---|---|
| `image/QLTLPLCVV_17-01-seed-baseline-empty.png` | Nhóm 3 rỗng trước khi seed ("Chưa có tư liệu pháp luật đính kèm.") |
| `image/QLTLPLCVV_17-02-seed-modal-3file.png` | Hộp thoại Thêm tư liệu đã điền + 3 tệp thật |
| `image/QLTLPLCVV_17-03-cbnv-modal-xem-tep-nut-Xem-xanh.png` | CB NV — hộp thoại "Xem tư liệu pháp luật", 3 nút [Xem] **xanh** |
| `image/QLTLPLCVV_17-04-cbnv-pdf-render-online.png` | PDF render trực tuyến, đọc được chữ trong tệp |
| `image/QLTLPLCVV_17-05-cbnv-png-preview-render.png` | Ảnh PNG render trong khung xem ảnh |
| `image/QLTLPLCVV_17-06-cbnv-dacongkhai-nut-Xem-van-dung-duoc.png` | Trạng thái **trùng khít** ảnh đối tác (`Xem tệp / Hủy công khai / Xóa`) mà [Xem] vẫn xanh |
| `image/QLTLPLCVV_17-07-chuyengia-duocphancong-nut-Xem-dung-duoc.png` | Chuyên gia được phân công (badge `TVV · CG`) — chế độ chỉ đọc, [Xem] xanh |

---

## Kết luận

Lỗi đối tác báo là **có thật tại thời điểm họ kiểm thử** (dev cũng tự nhận là BUG thật và đã sửa). Trên bản đang chạy, QA dựng lại **đúng vai trò (CB_NV_TW), đúng trạng thái (tư liệu đã công khai), đúng định dạng tệp (.docx)** của đối tác và **không còn tái hiện**: nút [Xem] tồn tại, không bị vô hiệu, bấm ra đúng hành vi mà đặc tả yêu cầu, và nội dung tệp thực sự hiện ra. Vai trò chuyên gia được phân công — vai trò mà `:979` bảo vệ — cũng xem/tải được bình thường trong chế độ chỉ đọc.

⇒ **`Pass`** (theo bảng §5.1 của PROMPT: *dev báo đã fix, QA test lại chạy đúng → `Pass`*).

## Quan sát NGOÀI tiêu chí của case (không ghi lên sheet, chỉ báo lại người phụ trách)

Khi đo nhánh "chuyên gia KHÔNG được phân công" phát hiện: tài khoản chuyên gia `qa_tvvseed28` **liệt kê được toàn bộ 9 tư liệu của mọi TVCS trong đơn vị** (`GET /api/v1/tu-lieu-phap-ly-vvs?pageSize=100` → 200, 9 bản ghi) và **tải được tệp của TVCS mà mình KHÔNG phụ trách** — cụ thể tư liệu `c30663cd-...` (trạng thái **Nháp**, chưa công khai) thuộc `TVCS-20260725-0001` có `chuyen_gia_id = null`: `GET .../files/e2ca26b2-.../download` → 200, tải về 604 B `%PDF-`.

Đối chiếu `srs-fr-12-tv-chuyen-sau.md:980` — *"**Given** Chuyên gia truy cập tư liệu của TVCS KHÔNG phải mình phụ trách **When** mở section **Then** từ chối (không hiển thị / 403 xử lý ở tầng quyền), không phải lỗi hệ thống"* — và `:936` (*CG chỉ tư liệu của TVCS có `chuyen_gia_id=CG` và trạng thái ≥ PHAN_CONG*) thì hành vi này **rộng hơn quyền mà đặc tả cho phép**.

Sắc thái cần nói rõ: **giao diện danh sách đã lọc đúng** (tab "Chờ xử lý" của chuyên gia hiện 0 bản ghi, chuyên gia không thấy các TVCS không phải của mình trên màn) — chỗ nới lỏng nằm ở **tầng API**. Đây là hướng **ngược lại** với lỗi của case này (case này là chặn nhầm người có quyền; cái này là chưa chặn người không có quyền), nên KHÔNG gộp vào verdict của `QLTLPLCVV_17`.
