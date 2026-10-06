# Audit verify vòng 1 — NHSYC_01 (row 127, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Nhập hồ sơ yêu cầu HTPL thủ công (Vụ việc HTPL → "Nhập thủ công") · FR-V.I-04 (UC54) · SCR-V.I-02
**Ngày verify:** 2026-08-03 · **Người verify:** QA (Claude Code, Chrome DevTools MCP)

## Note dev trước khi QA đè (2026-08-03)

Cột P (`Trạng thái dev fix 1`): `dev done`

Cột R (`DEV phản hồi lần 1`) — NGUYÊN VĂN:

```
Đã fix: FE trước serialize ngày sai định dạng → nay gửi ISO "YYYY-MM-DD" (hết lỗi 422 ngayTiepNhan). Commit 6eb4a3661 (VVHT_001), đã deploy 120.
```

Cột Q (`Verify`) trước khi QA ghi: **RỖNG** (không có verdict cũ mâu thuẫn).

---

## Cổng 1 — Bằng chứng đối tác (đã mở full-res bằng Read tool)

**File:** `partner-evidence/NHSYC_01.jpg` (JPEG 1914×1031, đã xem bằng mắt, không đọc từ mô tả text).

**3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết):**

| # | Dữ kiện | Giá trị đọc được từ ảnh |
|---|---|---|
| (a) | URL / ID bản ghi | `htpldn-uat.ospgroup.vn/vu-viec/tao-moi` — màn **tạo mới**, CHƯA có ID vụ việc (bản ghi chưa được tạo) |
| (b) | Trạng thái entity / màn đối tác đang đứng | Form "Nhập thủ công" chưa submit được. Accordion **"Thông tin Tiếp nhận"** đang mở. Toast đỏ góc trên: `ngayTiepNhan must be a valid ISO 8601 date string` + inline error đỏ **ngay dưới ô "Ngày tiếp nhận"** cùng nội dung. Ô "Ngày tiếp nhận" viền đỏ. Vai trò góc phải: **`CB_NV_TW` — "Cán bộ NV Trung ương"**, đơn vị **`BTP · TW`** |
| (c) | Dữ liệu tiền đề đối tác nhập | Tệp đính kèm `2K15 T5 (23.7) & T7 (25.7).pdf` (256.4 KB) · Kênh tiếp nhận = **Trực tiếp** · Ngày tiếp nhận = **27/07/2026** · Người tiếp nhận = "Cán bộ NV Trung ương" (auto, disabled). Đồng hồ máy trong ảnh: **27/07/2026 01:59 PM** |

**Ghi chú tên nút:** action-bar trong ảnh đối tác là **[Hủy] [Lưu nháp] [Lưu & Tiếp nhận]** — KHÔNG phải "Lưu & Gửi duyệt" như mô tả cột J của phiếu. Nút "Lưu & Tiếp nhận" chính là nút submit của chế độ nhập thủ công.

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** `partner-evidence/NHSYC_01.jpg`, vùng chứa LỖI = toast đỏ đỉnh màn + dòng chữ đỏ dưới ô "Ngày tiếp nhận" — hệ thống từ chối lưu hồ sơ, báo `ngayTiepNhan must be a valid ISO 8601 date string` dù ô ngày đã có giá trị hợp lệ `27/07/2026`.
2. **Đối tác phản ánh CỤ THỂ:** bấm nút lưu ở form nhập thủ công thì KHÔNG tạo được hồ sơ, thay vào đó hiện thông báo lỗi định dạng ngày tiếp nhận (lỗi kỹ thuật tiếng Anh, không phải message nghiệp vụ).
3. **Data + bước tái hiện:** login CB Nghiệp vụ cấp TW → menu "Vụ việc HTPL" → nút "Nhập thủ công" → điền đủ trường bắt buộc (DN, tiêu đề, nội dung, lĩnh vực, loại hình HT) + Kênh tiếp nhận "Trực tiếp" + Ngày tiếp nhận để mặc định/chọn hôm nay → bấm **[Lưu & Tiếp nhận]**.

## Cổng 3 — Đối chiếu SRS vs thực tế web

| # | SRS yêu cầu (trích nguyên văn + dòng) | Thực tế web (QA đo 2026-08-03) | Đạt? |
|:-:|---|---|:-:|
| 1 | `:1706` — "Mã VV auto-gen: VV-{TINH}-{YYYYMMDD}-{SEQ} (BR-DATA-04)" | Tạo được (khi bỏ tệp): **`VV-BTP-TW-20260803-002`** — `VV` + mã đơn vị `BTP-TW` + `20260803` + `002`. Bản ghi đơn vị địa phương trong danh sách có dạng `VV-STP-AG-20260712-003` | ✅ |
| 2 | `:1707` — "Nhập thủ công (UC54): trang_thai mặc định = DA_TIEP_NHAN (bỏ qua MOI_TAO và CHO_TIEP_NHAN)"; `:342` — "Tạo VU_VIEC, trạng thái = DA_TIEP_NHAN" | Badge trên màn Chi tiết: **"Đã tiếp nhận"**; stepper nhảy thẳng tới bước 3 "Đã tiếp nhận" (bước 1 "Mới tạo" + bước 2 "Chờ tiếp nhận" đánh dấu ✓ bỏ qua). Payload trả `"trangThai":"DA_TIEP_NHAN"` — UI khớp API | ✅ |
| 3 | `:341` — "Auto-calc `uu_tien` theo BR-CALC-07..."; `:2412` — "(1) DN phụ nữ làm chủ +3, (2) DN nhiều LĐ nữ +2, (3) DN ≥30% LĐ khuyết tật +2, (4) FIFO +1"; `:1709` — "Thiếu các trường ưu tiên → BR-CALC-07 trả `uu_tien = 1` (FIFO)" | DN dùng test có `laNuLamChu=false`, `soLaoDongNu=null`, `soLaoDongKhuyetTat=null` → kỳ vọng **1**. Thực tế UI hiện "Ưu tiên: **Trung bình**", payload `"uuTien":3`. Gọi API **không gửi** `uuTien` → BE vẫn trả **3** ⇒ hằng số mặc định, không auto-calc. Nhãn form còn lộ mã BR nội bộ lỗi thời "mặc định **BR-CALC-04**" (mã này đã đổi thành BR-CALC-07 tại v3.5 rev.3 — `CHANGELOG-v3-to-v3.5.md:2667`) | ❌ |
| 4 | `:343` — "Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc"; `:2418` — "SLA mặc định = 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1)" | UI "Thời hạn xử lý **24/08/2026**", badge "Bình thường · **còn 15 ngày LV**". Kiểm lại: 03/08/2026 (thứ Hai) + 15 ngày làm việc (trừ T7/CN; `/api/v1/ngay-le?nam=2026` không có ngày lễ nào trong 04–24/08) = **24/08/2026** — khớp chính xác | ✅ |
| 5 | `:342` + `:344` (§Processing bước 7 + bước 9) + `:1694` (SCR-V.I-02 row 15 — tệp PDF ≤20MB/tệp, tổng ≤100MB, ≤10 tệp là dữ liệu hợp lệ) | **Với tệp đính kèm (đúng điều kiện đối tác): KHÔNG tạo được hồ sơ.** `POST /api/v1/vu-viecs/manual` → **HTTP 500** `ERR-SYS-00-00-01`; màn hình đứng ở "Thêm mới Hồ sơ Vụ việc"; 2 thông báo lỗi hiện cùng lúc. Tái hiện 3/3 lần trên UI + 1/1 lần qua API | ❌ |

> **Hệ quả:** 4 tiêu chí Output của phiếu chỉ quan sát được khi **bỏ tệp đính kèm**. Giữ đúng điều kiện đối tác (**có** tệp) thì không có hồ sơ nào được tạo ⇒ cả 4 tiêu chí đều không đạt được trên luồng thực của đối tác.

## SRS đã mở đọc xác nhận (nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md`)

| Dòng | Trích nguyên văn |
|---|---|
| `:300` | `### FR-V.I-04: Nhập hồ sơ yêu cầu thủ công (UC54)` |
| `:302` | `**UC Reference:** UC 54 \| **Priority:** Essential \| **Stability:** High` |
| `:305` | `**Mô tả:** CB NV nhập hồ sơ thủ công (trực tiếp/điện thoại). Trạng thái bắt đầu = DA_TIEP_NHAN (bỏ qua MOI_TAO, CHO_TIEP_NHAN).` |
| `:341` | `\| 6 \| Auto-calc \`uu_tien\` theo BR-CALC-07 (FIFO +1 + các trường ưu tiên nếu có); nếu CB NV override phải có \`ly_do_uu_tien\` \| BR-CALC-07 \|` |
| `:342` | `\| 7 \| Tạo VU_VIEC, trạng thái = DA_TIEP_NHAN \| SM-VUVIEC \|` |
| `:343` | `\| 8 \| Tính deadline SLA: ngày tiếp nhận + 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1) \| BR-SLA-01 \|` |
| `:1670` | `### SCR-V.I-02: Thêm mới / Nhập thủ công Hồ sơ` |
| `:1698` | `\| 19 \| accordion-4 \| ngay_tiep_nhan \| C11 DatePicker \| Bắt buộc. Mặc định: ngày hiện tại. Common Approval Fields §3.2.0.8 \| — \| Luôn \|` |
| `:1702` | `\| 23 \| action-bar \| Thanh hành động cố định \| C22 \| [Hủy] [Lưu nháp] (→ MOI_TAO) [Lưu & Gửi duyệt] (→ CHO_TIEP_NHAN) \| click → tương ứng \| Luôn \|` |
| `:1706` | `- Mã VV auto-gen: VV-{TINH}-{YYYYMMDD}-{SEQ} (BR-DATA-04)` |
| `:1707` | `- Nhập thủ công (UC54): trang_thai mặc định = DA_TIEP_NHAN (bỏ qua MOI_TAO và CHO_TIEP_NHAN)` |
| `:2412` | `(1) DN phụ nữ làm chủ +3, (2) DN nhiều LĐ nữ +2, (3) DN ≥30% LĐ khuyết tật +2, (4) FIFO +1. CB NV có quyền override gợi ý.` (BR-CALC-07) |
| `:2418` | `SLA mặc định = 15 ngày làm việc (NĐ55/2019 Điều 8 Khoản 1 — trả lời vướng mắc pháp lý cho DNNVV). Có thể cấu hình khác tại UC108.` (BR-SLA-01) |

**Lưu ý mâu thuẫn nội bộ SRS:** dòng `:1702` (bảng thành phần màn dùng chung cho cả FR-V.I-02 UC52 và FR-V.I-04 UC54) ghi `[Lưu & Gửi duyệt] (→ CHO_TIEP_NHAN)`, nhưng **quy tắc tương tác `:1707` + mô tả FR `:305` + Processing `:342` đều chốt riêng cho UC54 (nhập thủ công) là `DA_TIEP_NHAN`**. Quy tắc riêng cho UC54 thắng → tiêu chí chấm dùng `DA_TIEP_NHAN`. Đây cũng là lý do app đặt tên nút chế độ nhập thủ công là **[Lưu & Tiếp nhận]** thay vì "Lưu & Gửi duyệt".

## Tài khoản dùng verify

- **Account THỰC dùng: `cbnv_tw_03` / `Test@1234`** — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #03"), đơn vị `BTP · TW`. Login OK ngay lần đầu, **không phải fallback Rule 7**.
- Khớp đúng vai trò + cấp của đối tác trong ảnh (`CB_NV_TW`, `BTP · TW`). **Không dùng `admin` để ra verdict**; `admin` không được dùng trong case này.
- OTP lấy từ MailHog `http://18.143.165.120:8025` (hộp thư `cbnv_tw_03@htpldn.test`).

## Kết quả đo

### Bằng chứng QUAN SÁT do QA tự chạy (GATE real-data)

| # | Artifact | Đường dẫn | Nội dung pixel/log đã mở đọc |
|:-:|---|---|---|
| 1 | Ảnh form đã điền đủ + **có tệp PDF**, ngay trước khi bấm | `bug-reports/vu-viec/image/BUG-NHSYC_01-form-co-tep-truoc-khi-bam.png` | DN đã chọn, tiêu đề/nội dung/lĩnh vực/loại hình đủ, dòng tệp `NHSYC_01-tep-kiem-thu.pdf (614 B)`, Kênh "Trực tiếp", Ngày tiếp nhận `03/08/2026`, nút `[Lưu & Tiếp nhận]` |
| 2 | Ảnh **2 thông báo lỗi** hiện trên màn | `bug-reports/vu-viec/image/BUG-NHSYC_01-toast-loi-he-thong.png` | 2 khung đỏ: "Lỗi hệ thống, vui lòng thử lại sau." + "Có lỗi xảy ra. Vui lòng thử lại sau."; nền vẫn là màn "Thêm mới Hồ sơ Vụ việc" (không chuyển màn Chi tiết) |
| 3 | Ảnh màn Chi tiết khi **bỏ tệp** → tạo được | `bug-reports/vu-viec/image/BUG-NHSYC_01-tao-duoc-khi-bo-tep.png` | `VV-BTP-TW-20260803-002`, badge "Đã tiếp nhận", stepper bước 3, "Ưu tiên: Trung bình", "Ngày tiếp nhận 03/08/2026 07:00", "Thời hạn xử lý 24/08/2026", badge "Bình thường · còn 15 ngày LV" |
| 4 | Ảnh form mặc định (ghi nhận nhãn ô Độ ưu tiên) | `image/NHSYC_01-01-form-mac-dinh.png` | Ngày tiếp nhận mặc định `03/08/2026`; ô Độ ưu tiên `3 — Trung bình (mặc định BR-CALC-04)` |
| 5 | Ảnh chẩn đoán màn OTP (Rule 9 step 1 khi `wait_for` timeout) | `image/NHSYC_01-00-login-diag.png` | Màn "Nhập mã xác thực" — không phải lỗi đăng nhập, chỉ là từ khoá chờ không khớp |

### Bộ bắt thông báo (`tools/toast-capture.js` — KHÔNG tự viết observer)

Tự kiểm trước mỗi lượt đo: `soObserverDangSong = 1` ⇒ số liệu hợp lệ.

| Lượt | Điều kiện | SỐ REQUEST ghi dữ liệu | SỐ KHUNG THÔNG BÁO | Nội dung | Kết quả |
|:-:|---|:-:|:-:|---|---|
| 1 | Có tệp đính kèm (trước reload) | 1 · `POST /api/v1/vu-viecs/manual` | **2** | "Lỗi hệ thống, vui lòng thử lại sau." · "Có lỗi xảy ra. Vui lòng thử lại sau." | Không tạo được, vẫn ở `/vu-viec/tao-moi` |
| 2 | Có tệp đính kèm (**sau reload bỏ cache**, tệp MỚI) | 1 · `POST /api/v1/vu-viecs/manual` | **2** | y hệt lượt 1 | Không tạo được |
| 3 | Có tệp đính kèm (lượt chụp ảnh) | 1/lượt | **2**/lượt | y hệt | Không tạo được |
| 4 | **Bỏ tệp đính kèm** | 1 · `POST /api/v1/vu-viecs/manual` | **1** | "Đã tiếp nhận — VV-BTP-TW-20260803-002" | Tạo được, chuyển `/vu-viec/{id}` |

**Chú ý về `khoangCachMs` 0.9–1.3 ms:** file `toast-capture.js` xem `<1ms` là cờ đỏ "observer bị nhân bản". Đã loại trừ: (a) tự kiểm cho đúng **1** observer trước mỗi lượt; (b) **nội dung 2 khung KHÁC NHAU** — observer nhân bản sẽ ghi 2 dòng chữ giống hệt; (c) đọc DOM sống ngay sau khi bấm cho `soKhungDangHienTrenMan = 2`; (d) **ảnh chụp bắt được đúng 2 khung trên màn hình**. ⇒ 2 thông báo là thật, không phải lỗi phép đo.

### Phương pháp thứ hai (bug candidate ≠ bug) — gọi thẳng dịch vụ, cùng tài khoản

| Phép thử | Payload | HTTP | Kết quả |
|---|---|:-:|---|
| A | Y như UI nhưng **bỏ** `fileDinhKemIds` | **201** | `VV-BTP-TW-20260803-001` · `trangThai: DA_TIEP_NHAN` · `deadline: 2026-08-24` · `uuTien: 3` |
| B | Y hệt UI, **có** `fileDinhKemIds` | **500** | `ERR-SYS-00-00-01` "Lỗi hệ thống, vui lòng thử lại sau" |
| C | Bỏ `fileDinhKemIds` **và** không gửi `uuTien` | **201** | `VV-BTP-TW-20260803-003` · `uuTien: 3` ⇒ BE **không** auto-calc BR-CALC-07 |

⇒ **2 phương pháp KHỚP nhau** (UI 500 ↔ API 500; UI tạo được khi bỏ tệp ↔ API 201 khi bỏ tệp). Không có mâu thuẫn cần dừng hỏi user. Biến quyết định đã cô lập được: **tệp đính kèm**.

### Đối chiếu UI vs payload (Nguyên tắc 2 — verdict theo UI + SRS)

Không có mâu thuẫn: UI "Đã tiếp nhận" ↔ `trangThai: DA_TIEP_NHAN`; UI "Thời hạn xử lý 24/08/2026" ↔ `deadline: 2026-08-24T00:00:00.000Z`; UI "Ưu tiên: Trung bình" ↔ `uuTien: 3`; UI mã `VV-BTP-TW-20260803-002` ↔ `maVuViec` cùng giá trị.

## Bản ghi QA tạo ra trên môi trường (để dọn/theo dõi)

| Mã vụ việc | Cách tạo | Trạng thái | Ghi chú |
|---|---|---|---|
| `VV-BTP-TW-20260803-001` | API (phép thử A — cô lập biến tệp đính kèm) | Đã tiếp nhận | dữ liệu điều tra, có thể xoá |
| `VV-BTP-TW-20260803-002` | **UI** (luồng chuẩn, bỏ tệp) | Đã tiếp nhận | **giữ làm bằng chứng** cho 3 tiêu chí Output đạt |
| `VV-BTP-TW-20260803-003` | API (phép thử C — kiểm auto-calc ưu tiên) | Đã tiếp nhận | dữ liệu điều tra, có thể xoá |

Bản ghi ở trạng thái "Đã tiếp nhận" không có nút Xoá trên giao diện (chỉ trạng thái "Mới tạo" mới có) nên QA để nguyên, không tự xoá bằng đường vòng.

## Verdict

**`Reopen`** (ghi cột Q `Verify`, mode `qaverdict`, **không đụng cột P**).

Lý do: dev báo `dev done`. Phần dev claim **đúng một nửa** — lỗi định dạng ngày (`ngayTiepNhan must be a valid ISO 8601 date string`, 422) đã hết thật, FE gửi `"ngayTiepNhan":"2026-08-03"`. Nhưng chính thao tác trong phiếu (bước 3–4 cột J: "Nhập thông tin hợp lệ" → bấm lưu) **vẫn không tạo được hồ sơ** ở đúng điều kiện đối tác (có tệp đính kèm): lỗi chỉ đổi dạng từ 422 sang 500. Ngoài ra tiêu chí Output "tự tính điểm ưu tiên theo NĐ 55/2019 Điều 4" cũng chưa đạt.

Tổng kết 4 tiêu chí Output: mã hồ sơ ✅ · trạng thái "Đã tiếp nhận" ✅ · điểm ưu tiên ❌ · thời hạn 15 ngày làm việc ✅ — **nhưng cả 4 chỉ đạt được khi bỏ tệp đính kèm**; trên luồng thật của đối tác không hồ sơ nào được tạo.

## Ngoài tiêu chí của case — quan sát thêm (dựa trên ảnh đã mở đọc)

1. **Một thao tác lưu sinh HAI thông báo lỗi cùng lúc** với hai câu chữ khác nhau (ảnh #2, đo 3/3 lượt, 1 request). Đây là lỗi hiển thị nằm ngoài phạm vi tiêu chí của phiếu → đã mở dòng TC mới trên sheet.
2. **Giao diện lộ mã quy tắc nội bộ đã lỗi thời** — ô "Độ ưu tiên" hiển thị `3 — Trung bình (mặc định BR-CALC-04)` (ảnh #4). Mã này đã đổi thành BR-CALC-07 ở SRS v3.5 và hiện `BR-CALC-04` đang thuộc nghiệp vụ khác (trọng số tiêu chí đánh giá, `srs-fr-08`/`srs-fr-10`). Đã gộp vào `BUG-NHSYC_01-B`.
3. Không phát hiện thêm bất thường nào khác trong 5 ảnh đã mở đọc.
