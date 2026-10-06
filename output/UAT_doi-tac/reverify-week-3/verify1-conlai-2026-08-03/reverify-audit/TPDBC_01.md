# Audit verify vòng 1 — TPDBC_01 (row 316, tab `UAT_TGPL Doanh Nghiệp-tuần 3`)

- **Ngày verify:** 2026-08-03 (18:40–18:50 giờ máy, tương ứng 11:40–11:48 UTC)
- **Env:** https://18.143.165.120.nip.io — build hiển thị ở sidebar: **HTPLDN · V1.0.5**
- **Cột P (dev):** `dev done` · **Cột Q (Verify) trước khi ghi:** TRỐNG
- **Verdict QA:** **`Pass`** — dev báo đã fix, test lại chạy đúng.

---

## Note dev trước khi QA đè (2026-08-03 18:40)

**Cột R (`DEV phản hồi lần 1`) của row 316 đang TRỐNG — không có note dev nào để lưu lại.**
Đã đọc lại toàn bộ 25 cột của row 316 trước khi ghi (dump bên dưới, phần "Dữ liệu phiếu gốc"). Dev mới chỉ điền cột P = `dev done`, chưa viết giải trình. Vì vậy verify vòng 1 hoàn toàn độc lập, không có manh mối nào từ dev.

### Dữ liệu phiếu gốc (row 316)

| Cột | Giá trị |
|---|---|
| D — Mã TC | `TPDBC_01` |
| E — Tên chức năng | Trình phê duyệt báo cáo đánh giá |
| F — Tác nhân | Cán bộ TW, BN, ĐP |
| H — Điều kiện | 1. Đăng nhập tài khoản · 2. Đợt đánh giá ở trạng thái "Báo cáo" · 3. Báo cáo đã được lưu |
| J — Các bước | 1. Chọn menu "Đánh giá hiệu quả" · 2. Mở Chi tiết đợt đánh giá (tab Báo cáo) · 3. Nhấn "Trình phê duyệt báo cáo" |
| K — Kết quả mong đợi | Thông điệp "Đã trình phê duyệt báo cáo"; trạng thái "Báo cáo" → "Chờ phê duyệt"; **gửi thông báo cho Cán bộ phê duyệt cùng đơn vị**; lưu vết thao tác |
| L — Kết quả thực tế (đối tác) | "Cán bộ phê duyệt không nhận được thông báo" |
| M — Ảnh/video 1 | `TPDBC_01.webm` |
| N — Trạng thái 1 | Fail |
| P — Trạng thái dev fix 1 | `dev done` |
| Q — Verify | (TRỐNG) |
| R — DEV phản hồi lần 1 | (TRỐNG) |

---

## Cổng 1 — Bằng chứng đối tác (đã mở xem full-res)

- **File:** `partner-evidence/TPDBC_01.webm` (10.797.219 bytes, dài ~24s).
- **Frame đã trích:** `frames/TPDBC_01/` — 9 frame, mỗi 3s (`tools/extract_frames.py`), đã **mở đọc full-res bằng Read tool** toàn bộ 9 frame.
- Môi trường đối tác quay: `htpldn-uat.ospgroup.vn`, đồng hồ máy `2026-07-27 05:18–05:19 PM`.

### 3 dữ kiện neo (viết TRƯỚC khi hình thành giả thuyết)

| # | Dữ kiện | Nguồn frame |
|---|---|---|
| (a) | **URL/ID bản ghi:** `htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/244a13f2-2f7d-440f-94d0-28b62d72d72a`; ở màn danh sách bản ghi này là **DG-20260727-0001** | t000.00s · t021.11s |
| (b) | **Trạng thái entity đối tác đang đứng:** trước thao tác — màn chi tiết đợt đánh giá còn nút **"Trình phê duyệt"**; sau thao tác — toast **"Đã trình phê duyệt"**, và ở danh sách dòng DG-20260727-0001 mang badge **"Chờ phê duyệt"** | t000.00s · t003.03s · t021.11s |
| (c) | **Dữ liệu tiền đề:** đợt đã có số liệu tổng hợp — Tổng số vụ việc 1, Đã đánh giá 1, Điểm trung bình 10, Xếp loại "Xuất sắc: 1"; có biểu đồ radar + biểu đồ cột ⇒ báo cáo đã lập và lưu | t000.00s |

## Cổng 2 — Hiểu bug (3 dòng bắt buộc)

1. **Evidence đã xem — frame chứa LỖI:** `frames/TPDBC_01/t024.13s.jpg`. Trong frame này, tài khoản **Cán bộ PD Trung ương (CB_PD_TW, phạm vi BTP · TW)** vừa đăng nhập xong đã mở dropdown chuông "Thông báo": mục mới nhất là *"Tài khoản vừa đăng nhập ở nơi khác — 3 giờ trước"*, kế đó *"Hồ sơ TVV chờ phê duyệt — 2 ngày trước"*… **KHÔNG có mục nào về báo cáo đánh giá vừa được trình chưa đầy 1 phút trước đó.**
2. **Đối tác phản ánh CỤ THỂ:** sau khi Cán bộ nghiệp vụ bấm "Trình phê duyệt" báo cáo đánh giá, **Cán bộ phê duyệt cùng đơn vị không nhận được thông báo nào** trên chuông trong ứng dụng. Đối tác KHÔNG phản ánh về toast hay về việc đổi trạng thái (hai thứ này chạy đúng trong chính video).
3. **Data + bước tái hiện:** đợt đánh giá ở trạng thái "Lập báo cáo", báo cáo đã lưu → CB NV vào chi tiết đợt → tab Báo cáo → "Trình phê duyệt" → xác nhận → đăng xuất, đăng nhập CB PD cùng đơn vị → mở chuông thông báo.

**Chuỗi thao tác trong video (đọc từ 9 frame):** t000 CB_NV_TW ở màn chi tiết đợt, còn nút "Trình phê duyệt" → t003 toast "Đã trình phê duyệt", nút đổi thành "Xuất báo cáo" → t006 về màn đăng nhập → t009 nhập `cbpd_tw` → t012 lấy OTP trong MailHog (`cbpd_tw@htpldn.gov.vn`) → t015 nhập OTP → t018 vào dashboard với vai trò **CB Phê duyệt Trung ương (CB_PD_TW · BTP · TW)** → t021 danh sách Đánh giá hiệu quả, DG-20260727-0001 badge "Chờ phê duyệt" → **t024 mở chuông, không có thông báo mới**.

---

## Thứ tự làm — ĐO WEB TRƯỚC, ĐỌC SRS SAU

Toàn bộ số đo dưới đây được ghi xong **trước khi** mở file SRS (chống thiên kiến xác nhận).

## Số đo thực tế trên web (phương pháp 1 — UI thật, Chrome DevTools MCP)

**Tài khoản dùng (ghi rõ theo §Nguyên tắc 3):**

| Vai | Tài khoản | Vai trò | donViId | capDonVi |
|---|---|---|---|---|
| Người trình báo cáo | `cbnv_tw_04` | CB_NV_TW | `00000000-0000-4000-8000-000000000001` | TW |
| Người nhận thông báo (chính) | `cbpd_tw_04` | CB_PD_TW | `00000000-0000-4000-8000-000000000001` | TW |
| Người nhận thông báo (kiểm chứng thêm) | `cbpd_tw_01` | CB_PD_TW | `00000000-0000-4000-8000-000000000001` | TW |

⇒ **Người trình và cả hai người phê duyệt CÙNG một `donViId`** — phép thử hợp lệ với yêu cầu "cùng đơn vị".

> `cbpd_tw` (tài khoản đối tác dùng trong video) đăng nhập FAIL 401 trên env này từ 30/07/2026 — đã ghi sẵn trong `input/input.md`. Áp Rule 7: fallback CÙNG vai trò + CÙNG cấp sang `cbpd_tw_04`, và thêm `cbpd_tw_01` để loại trừ khả năng "chỉ một người nhận được".

**Bản ghi dùng để test:** `DG-20260725-0001` — "Kiem thu LKHDG_03 - R3 20260725", `id = fd7d05b9-4108-4244-9366-ddc719c0cf74`, `donViId = 00000000-0000-4000-8000-000000000001`, người tạo = `cbnv_tw_04`.
Tiền đề: trạng thái **BAO_CAO** ("Lập báo cáo", stepper bước 7) + báo cáo **BCDG-20260725-0001 đã lưu** (version 3, ngày cập nhật 2026-07-30). Không phải seed mới — bản ghi có sẵn đã ở đúng state tiền đề của phiếu.

**Mốc thời gian (giờ UTC do trình duyệt trả về):**

| Mốc | Giá trị |
|---|---|
| Baseline chuông `cbpd_tw_04` trước thao tác | **47 chưa đọc**; thông báo mới nhất `2026-08-03T11:42:59.615Z` — "Tài khoản vừa đăng nhập ở nơi khác" |
| Bấm nút xác nhận "Trình phê duyệt" | `2026-08-03T11:45:12.074Z` + hẹn giờ 2500 ms ⇒ thao tác thực ~`11:45:14.5Z` |
| Chuông `cbpd_tw_04` sau thao tác (tải lại trang) | **48 chưa đọc** (+1) |
| Chuông `cbpd_tw_01` sau thao tác | **52 chưa đọc**, thông báo mới nhất là thông báo của thao tác này |

**Bộ bắt thông báo:** dùng nguyên khối `tools/toast-capture.js` (không lọc trùng, `innerText`, đếm request). Tự kiểm trước khi tin số liệu: `soObserverDangSong = 1` → **hợp lệ**.

Kết quả đo quanh thao tác "Trình phê duyệt":

```
SO_REQUEST            = 1   → POST /api/v1/ke-hoach-danh-gias/fd7d05b9-4108-4244-9366-ddc719c0cf74/bao-cao/submit
SO_KHUNG_THONG_BAO    = 1   → "Đã trình phê duyệt"
khoangCachMs          = null (không có khung thứ 2)
```

⇒ 1 request + 1 khung thông báo: **không có hiện tượng thông báo lặp**, không gọi máy chủ 2 lần.

**Trạng thái sau thao tác (đọc từ ảnh):** badge đổi từ "Lập báo cáo" → **"Chờ phê duyệt"**, stepper nhảy từ bước 7 sang **bước 8 "Chờ phê duyệt"**.

**Thông báo nhận được ở phía Cán bộ phê duyệt (đọc từ ảnh chuông):**
> **Báo cáo đánh giá chờ phê duyệt - DG-20…** / "Có báo cáo đánh giá vừa được trình lên chờ phê duyệt: - Mã …" / "một phút trước"

## Phương pháp thứ hai (bắt buộc) — gọi thẳng API thông báo bằng phiên đăng nhập của chính người phê duyệt

Endpoint được khám phá qua `/api/docs-json` (không đoán): `/api/v1/thong-baos`, `/api/v1/thong-baos/unread-count`.
Gọi bằng `evaluate_script` + `credentials:'include'` (cookie-auth) trong đúng phiên của từng tài khoản phê duyệt:

| Tài khoản | `unread-count` sau thao tác | Bản ghi mới nhất |
|---|---|---|
| `cbpd_tw_04` | 48 (baseline 47) | `tieuDe` = "Báo cáo đánh giá chờ phê duyệt - DG-20260725-0001" · `loai` = `PHE_DUYET` · `ngayTao` = `2026-08-03T11:45:14.766Z` · `nguoiNhanId` = `44dcccb6-972a-4203-83fe-6fba8cdcb9e5` (chính là userId của `cbpd_tw_04`) |
| `cbpd_tw_01` | 52 | cùng `tieuDe` "Báo cáo đánh giá chờ phê duyệt - DG-20260725-0001" · `ngayTao` = `2026-08-03T11:45:14.729Z` |

`noiDung` đầy đủ của thông báo:
```
Có báo cáo đánh giá vừa được trình lên chờ phê duyệt:

- Mã kế hoạch: DG-20260725-0001
- Đợt đánh giá: Kiem thu LKHDG_03 - R3 20260725

Vui lòng đăng nhập hệ thống để xem xét phê duyệt.
```

**Hai phương pháp KHỚP nhau** (UI chuông + API thông báo), không mâu thuẫn ⇒ đủ điều kiện chốt verdict.

### Ba khả năng đã phân biệt được (không gộp làm một)

| Khả năng | Kết luận | Bằng chứng |
|---|---|---|
| (a) Hệ thống KHÔNG sinh thông báo | **Bị loại** | API trả bản ghi thông báo có `ngayTao` khớp đúng giây thao tác |
| (b) Sinh nhưng gửi SAI người | **Bị loại** | `nguoiNhanId` = userId của chính CB phê duyệt cùng đơn vị; kiểm chứng thêm ở tài khoản phê duyệt thứ hai cùng đơn vị cũng nhận được |
| (c) Sinh đúng nhưng giao diện không hiện | **Bị loại** | Chuông tăng 47 → 48 và dropdown hiển thị đúng mục, đã mở ảnh đọc |

---

## Cổng 3 — Đối chiếu SRS (đọc SAU khi đã có số đo)

**Bản SRS dùng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (nguồn duy nhất).

Đã grep toàn file module đánh giá cho khái niệm đang xét (`Trình phê duyệt`, `CHO_PHE_DUYET`, `Thông báo CB PD`) — **4 vị trí, tất cả nói CÙNG một điều**, không có chỗ nào nói ngược:

| Vị trí (mở file đọc đúng dòng) | Nguyên văn |
|---|---|
| `srs-fr-08-danh-gia.md:626` | `### FR-VI-08: Trình phê duyệt báo cáo (UC90)` |
| `srs-fr-08-danh-gia.md:628` | `**UC Reference:** UC 90` |
| `srs-fr-08-danh-gia.md:658` | `\| 5 \| Gửi thông báo CB PD \| — \|` (bước 5 của bảng Processing) |
| `srs-fr-08-danh-gia.md:669` | `\| 2 \| Thông báo CB PD \| text \| Luôn \| Gửi CB PD \|` (bảng Outputs) |
| `srs-fr-08-danh-gia.md:674` | `- Thông báo gửi CB PD` (Postconditions) |
| `srs-fr-08-danh-gia.md:685` | `- **Given** CB NV chọn BC hoàn chỉnh **When** nhấn "Trình phê duyệt" **Then** BC → CHO_PHE_DUYET, gửi thông báo CB PD` |
| `srs-fr-08-danh-gia.md:897` | `\| 50 \| action-bar \| Nút [Trình duyệt BC] \| C08 Primary \| SET CHO_PHE_DUYET + gửi TB CB PD \| click → transition \| Khi TT = BAO_CAO \|` (đặc tả màn hình SCR-VI-01) |
| `srs-fr-08-danh-gia.md:1191` | `\| BAO_CAO \| CHO_PHE_DUYET \| CB NV trình \| BC đủ dữ liệu \| TB CB PD \| FR-VI-08 \| — \|` (bảng transition SM-DANHGIA) |

**Đối chiếu SRS ↔ web:**

| SRS yêu cầu | Thực tế web (số đo) | Đạt? |
|---|---|---|
| Chuyển trạng thái BAO_CAO → CHO_PHE_DUYET (dòng 657, 685) | Badge "Lập báo cáo" → "Chờ phê duyệt", stepper 7 → 8 | ✅ |
| Gửi thông báo CB PD (dòng 658, 669, 674, 685, 897, 1191) | Bản ghi thông báo `PHE_DUYET` "Báo cáo đánh giá chờ phê duyệt - DG-20260725-0001" tới đúng CB PD cùng đơn vị; chuông 47 → 48 | ✅ |
| Hiển thị thông điệp xác nhận cho người trình | 1 khung thông báo "Đã trình phê duyệt" (1 request / 1 khung) | ✅ |

**Về khác biệt câu chữ:** phiếu đối tác viết kỳ vọng thông điệp là *"Đã trình phê duyệt báo cáo"*, web hiện *"Đã trình phê duyệt"*. SRS FR-VI-08 **không quy định câu chữ** của thông điệp này (chỉ quy định chuyển trạng thái + gửi thông báo CB PD). Đây là khác biệt câu chữ nhỏ, KHÔNG phải nội dung đối tác báo lỗi (đối tác báo về thông báo cho cán bộ phê duyệt, và trong chính video của họ thông điệp này đã hiện). Không ghi thành bug, chỉ ghi nhận ở đây.

---

## GATE bằng chứng real-data

Loại claim = **Thao tác/state + absence** ("phải gửi thông báo mà không có"). Artifact QUAN SÁT từ re-verify **LIVE**, chạy trên bản ghi thật:

| # | Ảnh (đã mở đọc lại pixel, tên khớp nội dung) | Nội dung |
|---|---|---|
| 1 | `image/TPDBC_01-01-baseline-chuong-cbpd_tw_04.png` | Chuông người phê duyệt TRƯỚC thao tác: 47, mục mới nhất là "Tài khoản vừa đăng nhập ở nơi khác" |
| 2 | `image/TPDBC_01-02-tab-baocao-truoc-khi-trinh.png` | DG-20260725-0001, stepper bước 7 "Lập báo cáo", badge "Lập báo cáo", tài khoản CB Nghiệp vụ - Trung ương #04 (BTP · TW) |
| 3 | `image/TPDBC_01-03-modal-xac-nhan-trinh-phe-duyet.png` | Hộp thoại "Trình phê duyệt báo cáo? — Báo cáo sẽ được gửi cho cán bộ phê duyệt." |
| 4 | `image/TPDBC_01-04-sau-khi-trinh-trang-thai-cho-phe-duyet.png` | Sau thao tác: badge "Chờ phê duyệt", stepper bước 8 |
| 5 | `image/TPDBC_01-05-chuong-cbpd_tw_04-sau-khi-trinh.png` | Chuông người phê duyệt SAU thao tác: 48, mục mới nhất "Báo cáo đánh giá chờ phê duyệt - DG-20…" · "một phút trước" |
| 6 | `image/TPDBC_01-06-chuong-cbpd_tw_01-cung-don-vi-cung-nhan.png` | Tài khoản phê duyệt thứ hai cùng đơn vị cũng có đúng thông báo đó, chuông 52 |

> Ảnh #4 ban đầu được đặt tên `...toast-da-trinh-phe-duyet.png` nhưng pixel thực tế bắt được **trạng thái sau khi trình** (toast tự tắt trước khi ảnh chụp xong) → đã **đổi tên cho khớp nội dung** theo GATE. Chữ của toast được ghi nhận bằng bộ bắt thông báo (`SO_KHUNG_THONG_BAO = 1`, chữ "Đã trình phê duyệt"), không suy đoán từ ảnh.

---

## Kết luận

- Lỗi đối tác báo (**Cán bộ phê duyệt cùng đơn vị không nhận được thông báo**) **KHÔNG tái hiện** trên bản hiện tại (V1.0.5): hệ thống sinh thông báo `PHE_DUYET` đúng nội dung, đúng người nhận, đúng thời điểm; hai tài khoản phê duyệt cùng đơn vị đều nhận.
- Cột P của dev = `dev done` và **kiểm chứng độc lập cho thấy claim này ĐÚNG** — nhưng kết luận dựa trên số đo của QA, không dựa vào lời dev (cột R trống, không có giải trình nào để dựa vào).
- Theo bảng verdict §5.1 của prompt ("Dev bảo đã fix, test lại chạy đúng → `Pass`") ⇒ **Verify = `Pass`**.

## Ngoài tiêu chí của case — có thấy gì bất thường không?

**Không phát hiện thêm** lỗi nào từ 6 ảnh đã mở đọc và các số đo đã chạy trong phiên này. Ba điểm quan sát được nhưng KHÔNG phải lỗi, ghi lại để khỏi mất dấu:

1. Thông điệp sau khi trình là *"Đã trình phê duyệt"* trong khi phiếu đối tác kỳ vọng *"Đã trình phê duyệt báo cáo"*. SRS không quy định câu chữ này ⇒ không log.
2. Số đo 1 request / 1 khung thông báo ⇒ **không** dính lỗi thông báo lặp (bài học 16/07).
3. Chuông của tài khoản phê duyệt có nhiều mục "Tài khoản vừa đăng nhập ở nơi khác" — do chính QA đăng nhập lại nhiều lần, là hành vi bảo mật bình thường của hệ thống, không phải lỗi.
