# CHUẨN CHẤM — KTHSYCHTPL_11 (Lô G3 · khoá TRƯỚC khi đo)

> File này khoá chuẩn chấm **TRƯỚC** khi mở màn trên env nghiệm thu. Sau khi đo, **CẤM** sửa quan hệ
> `MATCH / DIFF / GAP` hoặc đổi ngưỡng Pass/Reopen cho khớp kết quả đo được.

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** · **dòng 45** |
| Mã TC | **KTHSYCHTPL_11** |
| Mô tả (đối tác) | "Kiểm tra nút chức năng Hoàn tất kiểm tra khi chọn kết luận Đạt" |
| Trạng thái nguồn (vòng 1) | `Trạng thái` = **Fail** · `Trạng thái dev fix` = **Test done** |
| Trạng thái nguồn (vòng 2) | `Trạng thái 2` = **Fail** · `Trạng thái dev fix 2` = **Bỏ qua** · `DEV phản hồi lần 2` = *"Reject / không phải lỗi theo BA-SRS; … kết luận Đạt giữ DANG_KIEM_TRA; chưa chọn người phân công thì không cho gửi; thao tác Phân công riêng mới chuyển DA_PHAN_CONG"* — **ngữ cảnh, KHÔNG phải căn cứ verdict**. Lô G3 **không đụng** 4 cột vòng 2 (BRIEF §5) |
| Kết quả thực tế (đối tác, nguyên văn) | *"Màn hình không hiển thị nút chức năng \"Hoàn tất kiểm tra\" mà hiển thị nút chức năng Kiểm tra lại"* |
| Env đo | `https://htpldn-uat.ospgroup.vn` (env NGHIỆM THU của đối tác) |
| Bản dựng | **đọc trên UI khi đo** (chân sidebar `HTPLDN · Vx.y.z`) — bắt buộc **tải lại trang** rồi mới ghi |
| Tài khoản dự kiến | `cbnv_tw` / `Test@1234` — vai trò **CB_NV_TW**, `donViId …8000-000000000001`, cấp TW (`output/UAT_doi-tac/input/input.md` §"Môi trường NGHIỆM THU của đối tác"). OTP ở `https://htpldn-uat.ospgroup.vn/mailhog/` |
| Vai trò theo đặc tả | **CB NV** — `srs-fr-05-vu-viec.md:1744` (cột "Tác nhân" của dòng trạng thái `DANG_KIEM_TRA` ghi **CB NV**); FR-V.I-06 `:513–514` (PRE-01 đã đăng nhập, PRE-02 VV ở `DA_TIEP_NHAN` hoặc `DANG_KIEM_TRA`); phạm vi đơn vị `:2452` (BR-AUTH-03/04) |
| Màn | **SCR-V.I-03 — Chi tiết Vụ việc**, **Accordion 4 — Kết quả Kiểm tra** + **thanh hành động cố định** (`:1730`, `:1736`) |
| URL dự kiến | `https://htpldn-uat.ospgroup.vn/vu-viec/{id}` — theo đúng luồng phiếu: menu **Vụ việc HTPL** → tìm kiếm → **Xem chi tiết** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-05-vu-viec.md` — **2506 dòng** |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` — **7012 dòng** |

---

## 2. Nguồn đã đọc (tự mở trong lượt này)

**SRS nguồn chuẩn DUY NHẤT — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`:**

| File | Đoạn đã đọc trọn | Nội dung |
|---|---|---|
| `srs-fr-05-vu-viec.md` | `:502–566` | **FR-V.I-06 Kiểm tra hồ sơ yêu cầu (UC56)** — trọn mục: Preconditions `:511–514` · Inputs `:518–523` · **6 hạng mục kiểm tra `:525–531`** · Processing 9 bước `:535–545` (**bước 5 = `:541`**) · Postconditions `:549–552` · **Error Handling `:556–559` (chỉ E1, E2)** · **AC `:562–564`** |
| `srs-fr-05-vu-viec.md` | `:704–791` | FR-V.I-09 Lựa chọn người hỗ trợ (UC59) — PRE-02 `:716`, Processing (Phân công) bước 6 `:749`, AC `:785–789`. Đây là FR sở hữu bước chuyển sang `DA_PHAN_CONG` |
| `srs-fr-05-vu-viec.md` | `:1715–1786` | **SCR-V.I-03** trọn mục: Thành phần `:1722–1736` (**Accordion 4 = `:1730`**, thanh hành động = `:1736`) · **Bảng nút theo trạng thái `:1740–1754` (dòng `DANG_KIEM_TRA` = `:1744`, dòng `DANG_KIEM_TRA (kết luận Đạt)` = `:1745`)** · **Quy ước hiển thị nút `:1756–1760`** · Thông báo riêng `:1771–1786` |
| `srs-fr-05-vu-viec.md` | `:1575–1599` | Quy ước chung mục 3 §D Trạng thái dữ liệu + §E Thông báo chung (đối chiếu câu chữ toast) |
| `srs-fr-05-vu-viec.md` | `:2229–2306` | **SM-VUVIEC** trọn mục: sơ đồ `:2238–2258` · Bảng trạng thái `:2262–2277` · **Bảng chuyển trạng thái `:2279–2303` (dòng quyết định = `:2288`)** |
| `srs-fr-05-vu-viec.md` | `:2309–2341`, `:2448–2452` | §6 Tổng quan BR + BR-AUTH-03/04 (phạm vi đơn vị) |
| `srs-fr-05-vu-viec.md` | `:12–26` | **Lịch sử thay đổi** — **dòng `:22`** ghi quyết định BA ngày **2026-07-16** nêu đích danh mã case này |

**Quét từ đồng nghĩa đã chạy trên toàn thư mục `srs-v3.5/`:** `Hoàn tất kiểm tra` · `Hoàn tất Kiểm tra` ·
`Kiểm tra lại` · `Kiểm tra Hồ sơ` · `Kiểm tra hồ sơ` · `danh sách kiểm tra` · `checklist` · `hạng mục` ·
`Đang kiểm tra` · `DANG_KIEM_TRA` · `Đã phân công` · `DA_PHAN_CONG` · `người kiểm tra` ·
`thời điểm kiểm tra` · `ngày kiểm tra` · `ket_luan` · `DAT` · `UC106`.

**Ngữ cảnh (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict, KHÔNG mượn số dòng):**
`output/UAT_doi-tac/flowtest-2026-08-05/tieuchi/KTHSYCHTPL_11.md` ·
`output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/batch-B6-vuviec-htpl/ketqua-KTHSYCHTPL_11.txt`
(lô đo cũ ở **env NỘI BỘ**, bản `V1.0.8`). **Lời DEV + ghi chú verify cũ = ngữ cảnh.**

---

## 3. Cổng bằng chứng

**CÓ 2 bằng chứng đối tác — đã MỞ XEM / trích khung hình:**

### 3.1. `KTHSYCHTPL_11.jpg` (vòng 1)
[`output/UAT_doi-tac/flowtest-2026-08-05/partner-evidence/KTHSYCHTPL_11.jpg`](../../../flowtest-2026-08-05/partner-evidence/KTHSYCHTPL_11.jpg)

| Vị trí trên ảnh | Nội dung đọc được |
|---|---|
| Thanh địa chỉ | `htpldn-uat.ospgroup.vn/vu-viec/aadd0022-0000-4000-8000-000000000004` |
| Đường dẫn điều hướng | `Trang chủ / Vụ việc hỗ trợ pháp lý / Chi tiết` |
| Góc phải trên | `BTP · DP` · chuông 52 · **`CB NV DP 01 (AG)`** · huy hiệu **`CB_NV_DP`** |
| Chân sidebar | **`HTPLDN · V1.0`** |
| Tiêu đề | **`VV-QA-R7-SLA-QHNT`** — *"QA R7 — Vụ việc SLA QUA_HAN_NGHIEM_TRONG"* + badge **`Đang kiểm tra`** + badge SLA mờ *"Quá hạn 47 ngày LV"* |
| **Thanh hành động (góc phải, đã phóng to đọc pixel)** | **ĐÚNG 2 nút: `[Phân công]` (nút chính, nền xanh) và `[Kiểm tra lại]` (nút phụ, viền)** — **KHÔNG thấy nút mang chữ "Hoàn tất kiểm tra"** |
| Thanh tiến trình | Mới tạo → Chờ tiếp nhận → Đã tiếp nhận → **Đang kiểm tra** (bước hiện tại) → Đã phân công → … |
| Accordion `Kết quả kiểm tra` (đang mở) | Bảng 5 cột `Mã / Hạng mục / Đạt / Không đạt / Ghi chú`; dòng `C01 — Văn bản đề nghị hỗ trợ (Mẫu 01 NĐ55)` có dấu `—` ở cột **Ghi chú**; **2 cột Đạt / Không đạt của C01 để trống** trong khung hình |
| Đồng hồ máy | `03:34 PM · 2026-07-09` |

### 3.2. `KTHSYCHTPL_11_v2.webm` (vòng 2) — đã trích khung hình
[`output/UAT_doi-tac/flowtest-2026-08-05/frames/KTHSYCHTPL_11_v2/`](../../../flowtest-2026-08-05/frames/KTHSYCHTPL_11_v2/)

| Khung | Nội dung đọc được |
|---|---|
| `t021.12s.jpg` | **Hộp thoại kiểm tra đang mở**: các hạng mục `3. Tờ khai xác định quy mô DN (NĐ39/2018)`, `4. Hợp đồng dịch vụ TVPL`, `5. Văn bản TVPL (bản đầy đủ)`, `6. Văn bản TVPL (bản loại bỏ bí mật KD)` — mỗi hạng mục 2 lựa chọn `Đạt` / `Không đạt` (đang chọn **Đạt**) + ô `Ghi chú cho hạng mục (không bắt buộc)`. Cuối hộp thoại: `* Kết luận` = **"Đạt — chuyển sang phân công"**, 2 nút `[Hủy]` `[Xác nhận]` |
| `t036.19s.jpg` | Sau khi xác nhận: `VV-BTP-TW-20260514-002` — *"R23v3 Seed VV2 LV Dat dai"*, badge **`Đang kiểm tra`** + badge `Quá hạn nghiêm trọng · 40 ngày LV`, thanh hành động vẫn **`[Phân công]` + `[Kiểm tra lại]`**; thanh tiến trình dừng ở bước 4 **Đang kiểm tra**; tài khoản `CB Nghiệp vụ TW 01 · CB_NV_TW`, `BTP · TW`, bản dựng **`HTPLDN · V1.0.4`**, ngày `2026-08-03` |

**Neo lấy được từ bằng chứng:**

1. Hai khung hình là **hai vụ việc khác nhau**, **hai vai trò khác nhau** (`CB_NV_DP` vs `CB_NV_TW`),
   **hai bản dựng khác nhau** (`V1.0` vs `V1.0.4`) ⇒ **không suy chéo**, phải tự dựng lại điều kiện.
2. Cả hai vụ việc đều mang dấu vết **do QA seed** (tên chứa `QA R7`, `R23v3 Seed`) — QA **không** được
   dùng lại chính 2 bản ghi đó nếu chúng đã bị thao tác; phải seed bản ghi mới (xem §5 T3).
3. Trên env nghiệm thu QA chỉ có tài khoản CB NV cấp **TW** (`cbnv_tw`) ⇒ đo ở **cùng vai trò CB NV**,
   khác cấp so với khung hình vòng 1. **Phải khai rõ** trong báo cáo.

---

## 4. BUG SCOPE LOCK — tách 3 vế

Phiếu gộp **2 vế trong ô "Kết quả mong đợi"** + **1 vế ẩn trong ô "Kết quả thực tế"**:

| Vế | Nguồn câu chữ | Quan hệ với SRS | Route |
|---|---|---|---|
| **V1 — nhãn/sự tồn tại của chức năng hoàn tất kiểm tra** | Ẩn trong *Kết quả thực tế*: *"Màn hình không hiển thị nút chức năng \"Hoàn tất kiểm tra\" mà hiển thị nút chức năng Kiểm tra lại"* | **MATCH** — `:1744` liệt kê đúng 2 nút cho trạng thái `DANG_KIEM_TRA` | **TEST** |
| **V2 — chuyển trạng thái sau khi kết luận Đạt** | *KQ mong đợi* dòng 1: *"Hệ thống chuyển trạng thái hồ sơ: \"Đang kiểm tra\" → \"Đã phân công\""* | **DIFF** — đặc tả nói **NGƯỢC LẠI** ở 4 chỗ độc lập (`:541`, `:564`, `:1744`, `:2288`); đã có quyết định BA **2026-07-16** nêu đích danh mã case này (`:22`) | **BA** (đo hiện trạng để trả lời, **CẤM Reopen riêng vế này**) |
| **V3 — ghi người kiểm tra + thời điểm kiểm tra** | *KQ mong đợi* dòng 2: *"Ghi người kiểm tra và thời điểm kiểm tra"* | **MATCH** — `:1730` (Accordion 4 chứa *"người kiểm tra + ngày"*) + `:550` | **TEST** |
| **V4 — đối chứng bắt buộc: đường chuyển sang "Đã phân công"** | Không có trên phiếu; là **vế đối chứng** để chứng minh V2 không phải "hệ thống kẹt" | **MATCH** — `:2288` + `:1745` + `:749` | **TEST** |

### Trích nguyên văn SRS dưới từng vế

**V1 — `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-05-vu-viec.md:1744`** (bảng "Bảng nút hành động theo trạng thái",
header cột ở `:1740` = `| Trạng thái hiện tại | Nút hiển thị | Tác nhân | Hành động |`):

```
| DANG_KIEM_TRA | [Hoàn tất Kiểm tra] · [Kiểm tra lại] | CB NV | Kết luận: **Đạt → vụ việc sẵn sàng phân công, VẪN giữ trạng thái DANG_KIEM_TRA** (chưa chuyển DA_PHAN_CONG) — khớp bảng chuyển trạng thái "DANG_KIEM_TRA → DA_PHAN_CONG: Đạt + chọn người/tổ chức xử lý" / YCBS → YEU_CAU_BO_SUNG (counter++) / Không đạt → TU_CHOI. Nút [Kiểm tra lại] dùng khi cần sửa lại kết quả kiểm tra đã lưu |
```

**V1 — `srs-fr-05-vu-viec.md:1758–1760`** (Quy ước hiển thị nút — dùng để phân biệt "ẩn" với "mờ"):

```
- Nếu user **không thuộc vai trò yêu cầu** → nút **không hiển thị** (không phải mờ đi)
- Nếu vai trò đúng nhưng **trạng thái / phạm vi không khớp** → nút **hiển thị nhưng mờ đi + tooltip** giải thích điều kiện chưa đạt (ví dụ: "Cần ở trạng thái 'Đã duyệt' để công khai")
- Nút context-sensitive theo bảng trên — KHÔNG hiển thị tất cả nút cùng lúc
```

**V2 — `srs-fr-05-vu-viec.md:541`** (FR-V.I-06 §Processing, bước 5):

```
| 5 | Nếu DAT: vụ việc sẵn sàng phân công, **giữ trạng thái DANG_KIEM_TRA** — chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức xử lý qua FR-V.I-09 (khớp điều kiện bảng chuyển trạng thái "Đạt + chọn người/tổ chức xử lý") | SM-VUVIEC |
```

**V2 — `srs-fr-05-vu-viec.md:564`** (FR-V.I-06 §Acceptance Criteria):

```
- **Given** CB NV kiểm tra xong **When** kết luận Đạt **Then** vụ việc sẵn sàng phân công, vẫn ở trạng thái DANG_KIEM_TRA; chỉ chuyển DA_PHAN_CONG khi CB NV phân công người/tổ chức xử lý (FR-V.I-09)
```

**V2 + V4 — `srs-fr-05-vu-viec.md:2288`** (SM-VUVIEC §Bảng chuyển trạng thái; header cột `:2281` =
`| Từ | Đến | Trigger | Guard | Action | FR Ref | BR Ref |`):

```
| DANG_KIEM_TRA | DA_PHAN_CONG | Đạt + chọn người/tổ chức xử lý | Đối tượng xử lý hợp lệ, đang hoạt động | Gửi TB người được phân công | FR-V.I-09 | BR-CALC-07 |
```

**V4 — `srs-fr-05-vu-viec.md:1745`** (bảng nút, dòng kế tiếp):

```
| DANG_KIEM_TRA (kết luận Đạt) / DA_TIEP_NHAN (phân công lại sau khi bị từ chối) | [Phân công] (modal 2 thẻ, gộp MH-05.5) | CB NV | … **Chỉ khi CB NV chọn được người/tổ chức xử lý và xác nhận thì vụ việc mới chuyển sang DA_PHAN_CONG.** …
```

**V3 — `srs-fr-05-vu-viec.md:1730`** (SCR-V.I-03 §Thành phần màn hình, dòng 7):

```
| 7 | content | Accordion 4 — Kết quả Kiểm tra (gộp MH-05.4) | C23 | Checklist 6 hạng mục (ĐẠT/KHÔNG_ĐẠT) từ UC106 + kết luận + lý do + người kiểm tra + ngày. "Lần bổ sung: {n}/3" (highlight đỏ khi n>=2) | CB NV nhập trực tiếp khi kiểm tra | Khi VV đã qua DANG_KIEM_TRA |
```

**V3 — `srs-fr-05-vu-viec.md:549–552`** (FR-V.I-06 §Postconditions):

```
**Postconditions:**
- Kết quả kiểm tra được ghi nhận
- Trạng thái VV chuyển theo SM-VUVIEC
- DN nhận thông báo nếu cần bổ sung hoặc từ chối
```

**6 hạng mục của danh sách kiểm tra — `srs-fr-05-vu-viec.md:525–531`** (để dựng tiền đề "đã đánh dấu đủ
6 hạng mục"):

```
**Hạng mục kiểm tra (UC106):**
1. Văn bản đề nghị hỗ trợ (Mẫu 01 (Phụ lục NĐ18/2026))
2. Bản chụp Giấy CNĐKKD
3. Tờ khai xác định quy mô DN (NĐ80/2021)
4. Hợp đồng dịch vụ TVPL
5. Văn bản TVPL (bản đầy đủ)
6. Văn bản TVPL (bản loại bỏ bí mật KD)
```

---

## 4b. 🔴 Trả lời câu hỏi then chốt — CÓ tìm thấy văn bản BA chốt ngày 16/07/2026 hay không?

**CÓ — nhưng nó nằm TRONG chính SRS nguồn chuẩn, KHÔNG phải một thư/biên bản BA riêng.**

**Căn cứ 1 — `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-05-vu-viec.md:22`** (bảng "Lịch sử thay đổi", cột 1 =
`Ngày` = `2026-07-16`, cột 2 = `Tác giả` = `BA + Claude`), trích đúng đoạn liên quan:

```
| 2026-07-16 | BA + Claude | **Apply chốt UAT tuần 2:** … sửa nút "Đạt" khớp bảng chuyển trạng thái — Đạt giữ DANG_KIEM_TRA, chỉ chuyển DA_PHAN_CONG khi phân công người xử lý (KTHSYCHTPL_11, đồng bộ FR-V.I-06); …
```

→ Dòng này **nêu đích danh mã case `KTHSYCHTPL_11`**.

**Căn cứ 2 (quan trọng hơn) — quyết định đã được áp vào THÂN đặc tả, không chỉ nằm ở changelog.**
Đã tự mở kiểm 4 vị trí normative, tất cả đều nhất quán: `:541` (Processing bước 5) · `:564` (AC) ·
**`:1744` (đặc tả cấp màn hình SCR-V.I-03)** · `:2288` (bảng chuyển trạng thái SM-VUVIEC).
⇒ Không rơi vào bẫy *"ghi chú phạm vi / CHANGELOG không thay được đặc tả màn hình"* — **phần màn hình
SCR đã mang dấu thay đổi**.

**KHÔNG tìm thấy:** một văn bản BA riêng (thư trả lời / biên bản / phiếu `ba-confirm`) đề ngày
**16/07/2026** cho case này. Đã quét: `output/UAT_doi-tac/**/ba-confirm/` (4 thư mục,
`reverify-week-5/ba-confirm/`, `reverify-bug-devfix-2026-08-06/ba-confirm/`, `reverify-week-3/ba-confirm/`,
`reverify-week-2/verify1-conlai-2026-08-03/ba-confirm/`) và `tasks/srs-contradictions.md`
(10 entry SRS-C-001…010) — **không có entry nào về `KTHSYCHTPL_11` / "Hoàn tất kiểm tra" / `DANG_KIEM_TRA`**.

**Hệ quả cho cách chấm:** vế **V2** là **DIFF giữa kỳ vọng của đối tác và đặc tả**, không phải lỗi phần
mềm. Vẫn **đề xuất BA xác nhận lại** với đối tác (đối tác đã Fail vế này 2 vòng ⇒ chưa được thông báo
hoặc chưa đồng thuận), **CẤM tự chốt "đối tác sai"** trong ô partner-facing.

**Câu hỏi BA soạn sẵn (dùng nguyên văn khi cần):**

> **CẦN BA XÁC NHẬN:** đối tác kỳ vọng — khi kết luận kiểm tra là *Đạt*, hồ sơ chuyển *"Đang kiểm tra" →
> "Đã phân công"*; đặc tả quy định **ngược lại** — kết luận Đạt **giữ nguyên "Đang kiểm tra"**, chỉ chuyển
> "Đã phân công" khi cán bộ chọn được người/tổ chức xử lý (`srs-fr-05-vu-viec.md:541`, `:564`, `:1744`,
> `:2288`; quyết định BA ghi tại `:22` ngày 2026-07-16 có nêu đích danh mã case này). Web hiện tại —
> *(điền sau khi đo)*. **Đề nghị BA xác nhận lại nội dung này với đối tác** để đóng dứt điểm, vì đối tác
> vẫn ghi Fail ở vòng 2. **Mục đích: thống nhất kỳ vọng, KHÔNG chặn bàn giao.**

---

## 5. Tiền đề phải dựng

| # | Tiền đề | Cách thoả (env đối tác **cho phép seed qua API cookie-auth**) |
|---|---|---|
| T1 | Đăng nhập đúng vai trò **CB NV** | `cbnv_tw` / `Test@1234` → mã 6 số ở `https://htpldn-uat.ospgroup.vn/mailhog/api/v2/messages?limit=5`. **5 lượt / 60 giây**. Lock → Rule 7 fallback **cùng vai trò + cùng cấp**, ghi account thực dùng |
| T2 | Xác nhận vai trò + đơn vị của phiên | `/api/v1/auth/me` → `vaiTro` chứa `CB_NV_TW`, ghi `donViId` + `capDonVi`. VV phải **cùng đơn vị** (`:2452` BR-AUTH-03/04) |
| T3 | **VV ở trạng thái `Đang kiểm tra` và CHƯA lưu kết luận kiểm tra** ← đây là tiền đề **quyết định** cho V1 | Không dùng lại 2 bản ghi trong bằng chứng. **Seed mới** theo đúng luồng: tạo VV *Nhập thủ công* (`:1707` — nhập tay vào thẳng `DA_TIEP_NHAN`) → mở chi tiết → bấm **[Kiểm tra Hồ sơ]** (`:1743`) để đưa về `DANG_KIEM_TRA`. **Dừng lại ở đây, chưa lưu kết luận.** Endpoint tra ở `GET /api/docs-json` (mở được không cần auth) — **CẤM đoán đường dẫn** |
| T4 | **VV thứ hai ở `Đang kiểm tra` ĐÃ lưu kết luận Đạt** — để đo V3 + V4 và để tách "sau khi kết luận" khỏi "trước khi kết luận" | Lặp T3 với 1 VV khác, sau đó hoàn tất kiểm tra với kết luận **Đạt**, đánh dấu **đủ 6 hạng mục** theo `:525–531` |
| T5 | Có ≥1 đối tượng xử lý hợp lệ để đo V4 | Trước khi bấm Phân công, kiểm hộp thoại có ít nhất 1 lựa chọn (cá nhân hoặc tổ chức) đang hoạt động, **cùng lĩnh vực** với VV (`:734`, `:747`). Không có → V4 **Chưa chốt**, không được ghi Reopen |
| T6 | **Bộ bắt thông báo cài TRƯỚC mỗi lần bấm** | `output/UAT_doi-tac/tools/toast-capture.js`; cài lại sau mỗi lần tải lại trang / chuyển màn; tự kiểm `soObserverDangSong = 1`; **CẤM lọc trùng**, **CẤM `textContent`**; đếm kèm số lời gọi mạng |
| T7 | Ghi **env + bản dựng** sau khi tải lại trang | `HTPLDN · Vx.y.z` ở chân sidebar + bó mã FE |
| T8 | Kế hoạch hoàn nguyên | VV do QA seed → **giữ lại** để dev tra cứu, ghi mã VV vào nhật ký đo. **Không** đụng VV của đối tác. Nếu buộc phải thao tác trên VV có sẵn: khai đủ **bản ghi nào · đổi gì · env nào** |

**Không dựng được T3 → V1 KHÔNG đo được → CẤM Pass** (BRIEF §4 luật 7).

---

## 6. Bảng chuẩn chấm

| # | Điều kiện BUG GỐC | Đặc tả (`file:dòng` nguyên văn) | Phép đo quyết định | Pass khi | Reopen khi |
|---|---|---|---|---|---|
| **V1** | *"Màn hình không hiển thị nút chức năng \"Hoàn tất kiểm tra\" mà hiển thị nút chức năng Kiểm tra lại"* — đo trên VV `Đang kiểm tra` **chưa lưu kết luận** (T3) | `srs-fr-05-vu-viec.md:1744` — *"\| DANG_KIEM_TRA \| **[Hoàn tất Kiểm tra] · [Kiểm tra lại]** \| CB NV \| …"*; quy ước ẩn/mờ `:1758–1760` | Liệt kê DOM thanh hành động: `innerText` **cộng** `title`/`aria-label`/`className` của **mọi** `button` / `a` / `[role=button]` trong vùng tiêu đề + thanh hành động, **kể cả** menu phụ (kebab `…`, "Thao tác khác"). Sau đó **mở chức năng đó** và xác nhận nó dẫn tới danh sách 6 hạng mục + ô kết luận có lựa chọn **Đạt** | Ở trạng thái `Đang kiểm tra` chưa có kết luận, CB NV **có** chức năng hoàn tất kiểm tra khả dụng (mở được phiếu 6 hạng mục + chọn được kết luận Đạt) **và** có chức năng kiểm tra lại | **Không có** chức năng nào cho phép hoàn tất kiểm tra ở trạng thái `Đang kiểm tra` (sau khi đã liệt kê DOM + mở menu phụ) — tức CB NV không thể ghi kết luận Đạt |
| **V1-b** *(Minor, gộp vào V1 khi báo cáo)* | Nhãn hiển thị của chức năng đó | `:1744` ghi nhãn **"[Hoàn tất Kiểm tra]"** | Đọc `innerText` của chính nút mở phiếu, đối chiếu từng chữ | Nhãn trùng đặc tả | Nhãn khác đặc tả → **ghi Minor trong ô diễn giải**, **KHÔNG** tự nó làm Reopen nếu V1 đạt |
| **V2** | *KQ mong đợi*: *"Hệ thống chuyển trạng thái hồ sơ: \"Đang kiểm tra\" → \"Đã phân công\""* | `:541` · `:564` · `:1744` · `:2288` — **đặc tả nói NGƯỢC**: Đạt **giữ** `DANG_KIEM_TRA`; quyết định BA `:22` (2026-07-16) nêu đích danh case này | Sau khi lưu kết luận **Đạt**: **tải lại trang** rồi đọc badge trạng thái + bước sáng trên thanh tiến trình; đối chứng bằng dữ liệu VV trả về từ máy chủ | **Chỉ ghi hiện trạng, KHÔNG Pass/Reopen riêng vế này.** Nếu hệ thống giữ `Đang kiểm tra` ⇒ **đúng đặc tả** → ghi *"web đúng đặc tả, kỳ vọng của phiếu lệch đặc tả"* + kèm câu hỏi BA §4b | Nếu hệ thống **tự nhảy sang `Đã phân công`** ngay khi kết luận Đạt (chưa chọn người xử lý) ⇒ **Reopen** — vi phạm `:541` và guard `:2288` |
| **V3** | *KQ mong đợi*: *"Ghi người kiểm tra và thời điểm kiểm tra"* | `:1730` — Accordion 4 gồm *"… + kết luận + lý do + **người kiểm tra + ngày**"*; `:550` — *"Kết quả kiểm tra được ghi nhận"* | Sau khi lưu kết luận Đạt + **tải lại trang**: đọc Accordion "Kết quả kiểm tra" — phải có **tên người vừa thao tác** và **thời điểm** khớp lượt bấm (lệch trong vài giây). Đối chứng: dữ liệu VV trả về từ máy chủ | Cả 2 thông tin hiển thị đúng người + đúng thời điểm **và** còn nguyên sau khi tải lại | Thiếu 1 trong 2 / ghi sai người (không phải tài khoản vừa thao tác) / mất sau khi tải lại |
| **V4** *(đối chứng)* | Không có trên phiếu — chứng minh đường sang `Đã phân công` vẫn thông | `:2288` — *"\| DANG_KIEM_TRA \| DA_PHAN_CONG \| Đạt + chọn người/tổ chức xử lý \| …"*; `:1745` — *"**Chỉ khi CB NV chọn được người/tổ chức xử lý và xác nhận thì vụ việc mới chuyển sang DA_PHAN_CONG**"* | Trên VV T4 (đã kết luận Đạt): mở chức năng **Phân công** → chọn 1 đối tượng xử lý hợp lệ → xác nhận → **tải lại trang** → đọc badge trạng thái | Sau khi chọn người/tổ chức và xác nhận, VV chuyển sang **`Đã phân công`** | Đã chọn được đối tượng hợp lệ và xác nhận thành công nhưng VV **vẫn không** chuyển `Đã phân công` ⇒ **Reopen** (lúc này lời phàn nàn "không chuyển trạng thái" của đối tác là đúng, chỉ khác điểm kích hoạt) |

**Quy tắc gộp:** **fix một phần = Reopen**. Verdict tổng tính trên **V1 · V3 · V4** (route TEST);
**V2 route BA** — chỉ dùng để mô tả hiện trạng và đặt câu hỏi, trừ khi rơi vào ô "Reopen khi" của chính V2.

---

## 7. Bẫy đã biết

**Chặn FAIL oan / Reopen oan:**

- **(a) 🔴 Đo nhầm thời điểm — bẫy đã làm case này kẹt 2 vòng.** Bảng `:1744` áp cho trạng thái
  `DANG_KIEM_TRA`; bảng `:1745` áp cho `DANG_KIEM_TRA (kết luận Đạt)` với nút **[Phân công]**. Cả 2
  khung hình của đối tác đều chụp **sau khi đã có kết luận** (thanh hành động là `[Phân công]` +
  `[Kiểm tra lại]`). ⇒ **CẤM kết luận "thiếu nút" từ ảnh chụp trạng thái đã kết luận.** V1 **bắt buộc**
  đo trên VV **chưa lưu kết luận** (T3).
- **(b) Nút có thể nằm trong menu phụ hoặc là biểu tượng không nhãn.** CẤM kết luận "không có nút" bằng
  mắt qua ảnh. Phải liệt kê DOM (`innerText` + `title` + `aria-label` + `className`) và mở thử menu phụ.
- **(c) Nhãn khác đặc tả ≠ thiếu chức năng.** Nếu chức năng hoàn tất kiểm tra tồn tại nhưng mang nhãn
  khác (ví dụ *"Kiểm tra hồ sơ"* / *"Kiểm tra lại"*), V1 **đạt** — chênh nhãn ghi **Minor** (V1-b).
  Đây là mô tả yêu cầu nghiệp vụ, không kê đơn cách hiện thực.
- **(d) `:1759` — nút mờ vẫn là "có hiển thị".** Nếu nút hiện nhưng mờ + tooltip do trạng thái chưa
  khớp thì đó là **đúng quy ước**, không phải "mất nút". Phải đọc `disabled` / `aria-disabled` +
  tooltip, không chỉ nhìn màu.
- **(e) Kỳ vọng "→ Đã phân công" của phiếu trái đặc tả.** CẤM chấm Reopen chỉ vì hệ thống **không**
  nhảy `Đã phân công` — `:541`/`:564`/`:1744`/`:2288` nói rõ điều ngược lại. Xử theo §4b: ghi hiện trạng
  + câu hỏi BA.
- **(f) Chữ trong hộp thoại có thể gây hiểu nhầm.** Khung `t021.12s.jpg` cho thấy ô kết luận ghi
  **"Đạt — chuyển sang phân công"**. Câu chữ này có thể là nguồn gốc kỳ vọng của đối tác. Đặc tả
  **không** quy định câu chữ cho lựa chọn kết luận ⇒ nếu quan sát lại thấy câu này, **ghi 1 dòng
  candidate câu chữ giao diện** trong `note/`, **không** dùng làm căn cứ Pass/Reopen.
- **(g) Phạm vi đơn vị.** VV không thuộc đơn vị của tài khoản đo → hệ thống chặn là **đúng**
  (`:2452` BR-AUTH-03/04). Chọn VV cùng đơn vị trước khi kết luận thiếu chức năng.
- **(h) `:558` E1 `ERR-KT-01`.** Nếu VV không ở `DA_TIEP_NHAN`/`DANG_KIEM_TRA` (`:514`) mà bấm kiểm tra
  → thông báo *"Vụ việc không ở trạng thái cho phép kiểm tra"* là **đúng đặc tả**, không phải bug.

**Chặn PASS oan:**

- **(i) "Thấy nút đã có" ≠ Pass.** BRIEF §4 luật 2 — phải bấm và chạy tới bước sinh ra kết quả: mở phiếu,
  đánh dấu đủ 6 hạng mục (`:525–531`), chọn kết luận **Đạt**, xác nhận, rồi mới đọc kết quả.
- **(j) Không tải lại trang.** Badge trạng thái và Accordion 4 có thể là dữ liệu cũ trong bộ nhớ trang.
  V2 + V3 **bắt buộc tải lại trang** rồi mới đọc.
- **(k) Không đo V3 trên nhánh khác Đạt là đủ.** Vế V3 của phiếu gắn với **kết luận Đạt** — đo ở nhánh
  *Yêu cầu bổ sung* không thay thế được.
- **(l) Bỏ V4.** Nếu chỉ đo V1 + V3 rồi kết luận Pass thì chưa loại được khả năng **đường sang "Đã phân
  công" thật sự hỏng** — đúng câu phàn nàn vòng 2 của đối tác (*"Hệ thống không chuyển trạng thái hồ sơ"*).
- **(m) Trang cũ / bản dựng cũ.** Bằng chứng là `V1.0` và `V1.0.4`; bản trên env hiện tại khác ⇒ tải lại
  trang + ghi tên bản dựng trước khi đo.

---

## 8. Bảng quyết định đã cam kết TRƯỚC khi đo

| Quan sát ở lượt đo | Verdict logic |
|---|---|
| V1 đạt (có chức năng hoàn tất kiểm tra, chọn được Đạt) · V3 đạt (ghi đủ người + thời điểm) · V4 đạt (Phân công → `Đã phân công`) · trạng thái sau khi Đạt **giữ** `Đang kiểm tra` | **Pass** — ô diễn giải mở đầu **"❌ Không phải lỗi"**, nêu căn cứ `:541`/`:564`/`:1744`/`:2288` + quyết định BA `:22` (2026-07-16), kèm đề nghị BA xác nhận lại với đối tác (§4b). Ghi rõ env + bản dựng đã đo |
| V1 đạt nhưng **nhãn** khác đặc tả | vẫn thuộc nhóm trên, **thêm 1 dòng Minor** về nhãn |
| Không tìm thấy chức năng hoàn tất kiểm tra ở `Đang kiểm tra` **chưa kết luận** (đã liệt kê DOM + menu phụ) | **Reopen** (V1 không đạt) |
| Chọn Đạt bị lỗi / không lưu được kết luận | **Reopen** (V1 không đạt) |
| Sau khi Đạt: **thiếu người kiểm tra hoặc thiếu thời điểm kiểm tra**, hoặc mất sau khi tải lại | **Reopen** (V3 không đạt) |
| Kết luận Đạt **tự nhảy** `Đã phân công` khi chưa chọn người xử lý | **Reopen** (vi phạm `:541` + guard `:2288`) |
| Đã chọn đối tượng xử lý hợp lệ + xác nhận thành công nhưng VV **không** chuyển `Đã phân công` | **Reopen** (V4 không đạt) |
| Không seed được VV ở `Đang kiểm tra` chưa kết luận (T3), hoặc không có đối tượng xử lý hợp lệ (T5) | **Chưa chốt** — nêu rõ dữ kiện còn thiếu, **CẤM Pass** |
| Giao diện và máy chủ mâu thuẫn (badge nói một đằng, dữ liệu trả về một nẻo) | **Chưa chốt** — ghi cả hai, hỏi lead |
