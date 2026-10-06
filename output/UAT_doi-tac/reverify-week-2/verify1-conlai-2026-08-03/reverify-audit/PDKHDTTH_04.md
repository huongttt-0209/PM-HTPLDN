# PDKHDTTH_04 — Audit verify vòng 1 (2026-08-03)

> Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · row **120**.
> Cổng 1 + Cổng 2 chi tiết: [`PDKHDTTH_04-evidence.md`](PDKHDTTH_04-evidence.md) · Cổng 3: [`../srs/PDKHDTTH_04-srs.md`](../srs/PDKHDTTH_04-srs.md)

## Note dev trước khi QA đè (2026-08-03)

Cột **P — `Trạng thái dev fix 1`** = `Reject`

Cột **R — `DEV phản hồi lần 1`** (nguyên văn):

```
KHÔNG phải bug: BE đã chặn phê duyệt khác đơn vị + trả message VN rõ "Người duyệt phải cùng đơn vị với kế hoạch"; FE hiển thị toast đúng end-to-end. SRS không ép chuỗi message cụ thể.
```

## Nội dung gốc của case (đọc lại từ sheet 2026-08-03)

| Cột | Giá trị |
|---|---|
| G — Mô tả | `Cán bộ phê duyệt khác cấp với người lập` |
| H — Điều kiện | `1. Đăng nhập tài khoản Cán bộ phê duyệt khác cấp với người lập` |
| J — Các bước thực hiện | `1. Chọn menu "Đào tạo, tập huấn" -> "Kế hoạch đào tạo"` / `2. Bấm nút "Phê duyệt"` |
| K — Kết quả mong đợi | `Hệ thống từ chối và hiển thị thông báo "Không có quyền phê duyệt kế hoạch này".` |
| L — Kết quả thực tế | `Hệ thống không hiển thị thông báo để người dùng dễ dàng nhận biết lý do không phê duyệt được kế hoạch` |
| M — Ảnh/video 1 | `PDKHDTTH_04.jpg` |
| N — Trạng thái 1 | `Fail` |
| Q — Verify | *(trống trước khi QA ghi)* |

---

## Verdict QA vòng 1: `BA confirm`

Tài khoản dùng ra verdict: **`cbpd_tw_01`** (`CB_PD_TW`, `BTP · TW`). `cbpd_tw` login FAIL `401` → fallback Rule 7 (cùng vai trò + cùng cấp), đúng ghi nhận sẵn có ở [`input/input.md`](../../../input/input.md).
Seed dựng bằng `cbnv_dp_01` (`cbnv_dp` cũng login FAIL `401` → fallback Rule 7). `admin` KHÔNG được dùng.

### Kết quả đo (2 lần + đối chứng + phương pháp thứ hai)

| Lần đo | Điều kiện | Nút "Phê duyệt" | Số request ghi | Số khung thông báo | Trạng thái sau |
|---|---|:-:|:-:|:-:|---|
| **1** | `cbpd_tw_01` (TW) × `KH-20260803-0004` (cấp ĐP), Chờ duyệt | Không có | **0** | **0** | Chờ duyệt (không đổi) |
| **2** (sau khi tải lại trang) | như trên | Không có | **0** | **0** | Chờ duyệt (không đổi) |
| Biến thể lệch cấp #2 | `cbpd_tw_01` (TW) × `KH-20260803-0002` (cấp Bộ ngành), Chờ duyệt | Không có | 0 | 0 | Chờ duyệt |
| **Đối chứng** cùng đơn vị | `cbpd_tw_01` (TW) × `KH-20260803-0001` (cấp TW), Chờ duyệt | **Có** (Phê duyệt + Từ chối) | **1** (`POST …/approve`) | **1** — "Đã phê duyệt" | **Đã duyệt** |
| Phương pháp thứ hai (tầng dữ liệu) | gọi thẳng thao tác duyệt trên `KH-20260803-0004` | — | 1 | 0 (giao diện không hiện gì) | Chờ duyệt — `HTTP 403`, mã `ERR-PERM-III-15-02`, message **"Người duyệt phải cùng đơn vị với kế hoạch"** |

- Bộ đo: **chỉ** `tools/toast-capture.js` (không lọc trùng, đọc bằng `innerText`). Tự kiểm `soObserverDangSong = 1` trước cả 2 lần đo.
- Đối chứng chứng minh **bộ đo không nói dối**: cùng màn, cùng tài khoản, cùng phiên — khi thao tác được phép thì observer bắt đúng **1** khung thông báo (`khoangCachMs = null`, không lặp).
- Bằng chứng DOM cho "absence": thanh hành động dưới cùng của màn Chi tiết là `<div style="position: sticky; bottom: 0…">` chứa **`ant-space` RỖNG** — 0 phần tử con. Quét toàn trang: **0** phần tử khớp `Phê duyệt|Từ chối` (kể cả node ẩn / `disabled`), **0** `ant-alert`, **0** `[role="alert"]`, **0** `ant-form-item-explain-error`, **0** `ant-modal`, **0** `ant-result`.
- `list_network_requests` xác nhận: trên màn đó FE **không phát bất kỳ request ghi nào**; `POST …/approve` duy nhất trong log là request do QA tự gọi ở phương pháp thứ hai.

### Cổng 3 — SRS yêu cầu vs thực tế web

> Nguồn SRS duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — đã tự mở đọc, xác nhận từng số dòng.

| SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|
| `srs-fr-03-dao-tao.md:1217` — *"Preconditions: CB PD đã đăng nhập, KH ở CHO_DUYET, CB PD cùng đơn vị."* + `:1221` — *"Processing: Kiểm tra quyền + cùng đơn vị → …"* | Không cùng đơn vị → không duyệt được (giao diện gỡ nút; tầng dữ liệu trả 403 `ERR-PERM-III-15-02`) | **Đủ** |
| `srs-v3.5.md:5480` BR-AUTH-05 — *"CB PD chỉ duyệt bản ghi do CB NV cùng đơn vị tạo… KHÔNG cho phép cấp trên duyệt cấp dưới…"*; Ngoại lệ = `—`; Cách kiểm thử nêu đúng ca *"CB PD Bộ Tư pháp (TW) KHÔNG duyệt được bản ghi của Sở TP HN (ĐP)"* | TW không duyệt được kế hoạch cấp ĐP và cấp BN | **Đủ** |
| `srs-v3.5.md:6380` SM-KH-DAO-TAO — guard `CHO_DUYET → DA_DUYET` là *"Cùng đơn vị (BR-AUTH-05)"* | Trạng thái giữ `CHO_DUYET` sau cả 2 lần đo + sau khi gọi thẳng tầng dữ liệu; `nguoiDuyet`/`thoiGianDuyet` vẫn `null` | **Đủ** |
| `srs-fr-03-dao-tao.md:1228`–`:1229` (AC, 2 dòng đều là ca thành công) + BR-AUTH-05 test (3) *"CB PD Sở TP HN duyệt được bản ghi của Sở TP HN"* | Cùng đơn vị → duyệt được, trạng thái → Đã duyệt, có thông báo "Đã phê duyệt" | **Đủ** |
| **Thông báo giải thích khi bị chặn** — FR-III-15 (`srs-fr-03-dao-tao.md:1208`–`:1229`) KHÔNG có mục Error Handling, không mã lỗi, không mẫu câu. Chuỗi đối tác kỳ vọng *"Không có quyền phê duyệt kế hoạch này"* KHÔNG tồn tại ở bất kỳ dòng nào của SRS v3.5 | Không hiển thị bất kỳ thông báo / cảnh báo / dòng giải thích nào (mọi kênh = 0) | **SRS SILENT → BA chốt** |
| `srs-v3.5.md:683` quy ước M-05 — *"Hiển thị theo quyền… Ẩn (không disable) nếu không có quyền"* | App ẩn hẳn nút Phê duyệt/Từ chối với CB PD khác đơn vị → khớp khuynh hướng M-05 | Đủ (theo M-05) |
| `srs-fr-03-dao-tao.md:1774` SCR-III-00 cột Hành động — *"… Phê duyệt + Từ chối (Chờ duyệt — CB PD) …"*: điều kiện hiển thị chỉ nêu **trạng thái + vai trò**, KHÔNG nêu điều kiện đơn vị | App ẩn nút dù đúng trạng thái + đúng vai trò | **Lệch `:1774`** — mâu thuẫn nội bộ SRS (`:1774` vs BR-AUTH-05 + M-05) → BA chốt |
| **Tiền lệ cùng file** cho đúng tình huống "phê duyệt khác đơn vị": `:277` `ERR-CTDT-PD-01` *"Không có quyền phê duyệt CTDT của đơn vị khác"* · `:283` `ERR-KH-PD-03` *"Không có quyền phê duyệt Khóa học của đơn vị khác"* | CTDT và Khóa học có câu thông báo trong SRS; Kế hoạch (FR-III-15) thì không, và app cũng không hiện gì | **Lệch tiền lệ** → BA chốt |

**Ghi nhận thêm:** hệ thống **đã có sẵn** mã lỗi + câu tiếng Việt riêng cho chính FR-III-15 ở tầng dữ liệu — `ERR-PERM-III-15-02` *"Người duyệt phải cùng đơn vị với kế hoạch"* — nhưng giao diện gỡ hẳn nút nên câu này **không bao giờ tới được người dùng**.

### Vì sao `BA confirm` chứ không phải `Open` / `Reject`

- **Không `Open`:** hai điều kiện của `Open` đều không thoả — (a) không có clause SRS nào bị app làm sai (việc chặn là **bắt buộc** theo BR-AUTH-05 `srs-v3.5.md:5480` + `srs-fr-03-dao-tao.md:1217`/`:1221`); (b) luồng bị chặn **không phải luồng hợp lệ** — phê duyệt xuyên cấp là thứ SRS cấm. Phần đối tác phản ánh (thiếu thông báo) rơi đúng vào chỗ **SRS không quy định**.
- **Không `Reject`:** quan sát của đối tác **ĐÚNG** và tái hiện được 2/2 lần — hệ thống thật sự không cho người dùng biết lý do. Không chứng minh được đối tác thao tác/hiểu sai. Đây là bất đồng về **ĐẶC TẢ**, protocol cấm `Reject` cho ca này.
- **`BA confirm`:** SRS silent về thông báo + 3 nguồn nội bộ mâu thuẫn nhau (M-05 "ẩn" vs `:1774` "hiện theo trạng thái + vai trò" vs tiền lệ `:277`/`:283` "có câu thông báo") + hệ thống đã tự có mã lỗi `ERR-PERM-III-15-02` cho FR-III-15 mà giao diện không dùng.

### Đối chiếu với phản hồi của dev

| Dev nói | QA đo được | Kết luận |
|---|---|---|
| *"BE đã chặn phê duyệt khác đơn vị"* | Đúng — `403`, trạng thái không đổi | ✅ đúng |
| *"trả message VN rõ 'Người duyệt phải cùng đơn vị với kế hoạch'"* | Đúng nguyên văn — `ERR-PERM-III-15-02` | ✅ đúng |
| *"FE hiển thị toast đúng end-to-end"* | **Sai** — FE gỡ hẳn nút Phê duyệt/Từ chối với CB PD khác đơn vị, **0 request ghi → 0 khung thông báo** ở cả 2 lần đo. Không tồn tại đường đi nào trên giao diện để câu message đó hiện ra | ❌ không đúng với tình huống này |
| *"SRS không ép chuỗi message cụ thể"* | Đúng về mặt chữ nghĩa (FR-III-15 không có Error Handling), nhưng **không** kết luận được là "không cần thông báo" — vì `:1774`, `:277`, `:283` kéo về hướng ngược lại | ⚠️ đúng một nửa → cần BA chốt |

### Artifact

| Loại | Đường dẫn |
|---|---|
| Bằng chứng đối tác (đã mở full-res) | `partner-evidence/PDKHDTTH_04.jpg` + `frames/PDKHDTTH_04/crop-{title-stepper,header-right,bottom-panel}.png` |
| Login `cbnv_dp` FAIL (Rule 7) | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-seed-00-login-cbnv_dp-fail.png` |
| Seed — form tạo kế hoạch (cấp ĐP) | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-seed-01-form-tao-ke-hoach-DP.png` |
| Seed — kế hoạch đã tạo (Nháp) | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-seed-02-da-tao-ke-hoach-nhap.png` |
| Seed — kế hoạch đã lên Chờ duyệt | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-seed-03-ke-hoach-DP-cho-duyet.png` |
| Danh sách dưới quyền CB PD TW — chỉ có "Xem" | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-01-danh-sach-CBPD-TW-chi-co-Xem.png` |
| Đối chứng — cùng đơn vị CÓ nút Phê duyệt | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-02-doi-chung-cung-don-vi-TW-co-nut-Phe-duyet.png` |
| **Điều kiện đối tác — khác cấp: không nút, không thông báo** | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-03-khac-cap-DP-khong-co-nut-khong-co-thong-bao.png` |
| Đối chứng — duyệt cùng đơn vị thành công | `bug-reports/dao-tao/image/BUG-PDKHDTTH_04-04-doi-chung-cung-don-vi-duyet-thanh-cong.png` |
| Bảng đối chiếu điều kiện (0 GAP) | `cond/PDKHDTTH_04.md` |
| Note ghi vào sheet | `notes/PDKHDTTH_04.txt` |

### Ngoài tiêu chí của case, có thấy gì bất thường không?

**CÓ — 1 phát hiện đã log thành dòng TC mới, 1 phát hiện gộp vào câu hỏi BA, 1 ghi nhận môi trường.**

1. **`QLLKHDTBD_50` — đã mở dòng TC mới trên sheet (tab tuần 2, row 144, `Verify='Open'`).**
   Bảng danh sách Kế hoạch đào tạo chỉ có **8 cột** (Mã kế hoạch · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Trạng thái · Hành động), trong khi SCR-III-00 Thành phần 3 (`srs-fr-03-dao-tao.md:1767`–`:1775`) quy định phải có thêm **ô tích chọn dòng**, **Số chương trình**, **Người tạo**, **Ngày tạo**. Cột ngân sách còn hiển thị số thô `100000000.00` thay vì định dạng dấu chấm (màn Chi tiết cùng bản ghi lại hiển thị đúng `100.000.000 VNĐ` → hai màn không nhất quán).
   Kiểm 2 cách đều khớp: liệt kê toàn bộ `th` trong DOM (đúng 8, không có cột ẩn) + ảnh chụp sau khi cuộn ngang hết sang phải. Ảnh: `bug-reports/dao-tao/image/BUG-QLLKHDTBD_50-danh-sach-KHDT-thieu-4-cot.png`.
   Liên quan trực tiếp tới case này: thiếu cột "Người tạo" là lý do **cả đối tác lẫn QA đều không đọc được kế hoạch thuộc đơn vị nào** từ màn hình.
   *(Không trùng row 31 `QLLKHDTBD_02` — dòng đó phản ánh lỗi "Lỗi hệ thống" khi tải danh sách, đã `Verify=Pass`, không đụng tới chuyện thiếu cột.)*

2. **Màn Danh sách không có hành động Phê duyệt/Từ chối cho CB PD** — kể cả với dòng **cùng đơn vị + đang Chờ duyệt** (`KH-20260803-0001` lúc còn Chờ duyệt chỉ có "Xem"), trái với `srs-fr-03-dao-tao.md:1774`. Phải mở màn Chi tiết mới thao tác được — đây đúng là lý do bước *"2. Bấm nút Phê duyệt"* trong phiếu không thực hiện được ngay ở màn danh sách.
   **KHÔNG mở dòng TC riêng** vì nó dựa trên chính dòng `:1774` mà QA đã đưa vào **câu hỏi BA số 3** của case này — nếu BA chốt `:1774` viết thiếu điều kiện đơn vị thì đây không phải lỗi. Chờ BA trả lời rồi mới quyết log hay không.

3. **Ghi nhận môi trường (không phải lỗi phần mềm):** `cbnv_dp` đăng nhập FAIL `401` với `Test@1234` — cùng triệu chứng đã ghi sẵn cho `cbpd_tw`. Đã fallback đúng Rule 7 sang `cbnv_dp_01`. Đã bổ sung vào `input/input.md`.

**Không phát hiện lỗi thông báo lặp:** mọi thao tác ghi trong phiên đều đo được **1 request → 1 khung thông báo** (tạo kế hoạch · gửi phê duyệt · phê duyệt), `khoangCachMs = null`.

### Dữ liệu QA tạo ra trong phiên (để phiên sau biết)

- `KH-20260803-0004` — "QA PDKHDTTH_04 - Test phe duyet khac cap (DP)", đơn vị cấp ĐP (`…8002-000000000006`), **vẫn ở Chờ duyệt** (dùng lại được cho re-test).
- `KH-20260803-0001` — seed sẵn có của phiên trước (đơn vị TW), đã bị **duyệt** trong lượt đối chứng → nay ở **Đã duyệt**. Cần kế hoạch TW ở Chờ duyệt cho lượt sau thì phải seed mới.
- `KH-20260803-0002` — đơn vị cấp BN, vẫn ở Chờ duyệt.
