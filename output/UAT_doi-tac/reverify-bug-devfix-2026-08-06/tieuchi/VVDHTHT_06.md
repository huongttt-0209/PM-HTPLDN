# Tiêu chí verify — VVDHTHT_06 (tab `bug`, dòng 189)

Mã case: VVDHTHT_06          Thời điểm viết: 2026-08-06 12:45
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** (`assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (khai theo §Giai đoạn A):
`reverify-week-4/reverify-round-2026-08-03/cond/VVDHTHT_06.md` (đo 03/08 trên env đối tác, build V1.0.4) ·
`reverify-week-4/reverify-round-2026-08-03/KET-QUA-REVERIFY-VONG-2.md` §7 ·
`reverify-week-4/reverify-round-2026-08-03/GUI-BA-2026-08-03/ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md` ·
`reverify-week-4/reverify-round-2026-08-04/phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md` (Vấn đề 16–18, BA duyệt 04/08) ·
`tasks/srs-contradictions.md` §SRS-C-010 (Open — chỉ nói về tệp **PDF**, không nói tệp .xlsx).
Mục 4 dưới đây suy từ **đặc tả** (SRS v3.5), **không** lấy số đo cũ làm ngưỡng. Số liệu cũ (Tổng vụ việc = 4/5)
chỉ dùng làm mốc so sánh env, không dùng làm tiêu chí.

---

## 1. Đối tác phản ánh

- **(a)** Bấm **[Xuất Excel]** trên màn Báo cáo thống kê (sau khi đã [Xem báo cáo] thành công) → hệ thống
  **không tải được tệp về máy**, thay vào đó hiện thông báo lỗi.
  - Vòng 1 (15/07/2026 17:20, bản dựng **V1.0**): thông báo `Không thể tạo file xuất. Vui lòng thử lại.`
  - Vòng 2 (retest TKM 31/07/2026 14:35, bản dựng **V1.0.3**): thông báo `Forbidden`
- Ô *Kết quả mong đợi* của phiếu này: *"Hệ thống xuất toàn bộ và tự động tải tệp về máy người dùng."*
  → **KHÔNG có chữ nào về tên tệp** (khác 4 phiếu cùng nhóm 222/226/230/234). Vì vậy tên tệp **không phải**
  một vế của case này; nếu tên tệp sai khuôn thì xử theo nhánh *phát hiện ngoài phạm vi*, không kéo verdict.

**Bằng chứng đã mở xem full-res:**
- `../partner-evidence/VVDHTHT_06.jpg` — thanh địa chỉ `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-dang-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-00000000...`;
  góc phải trên **"Quản trị viên · QTHT"**, nhãn đơn vị **BTP · TW**; dropdown *Loại báo cáo* = **BC Vụ việc đã hoàn thành**;
  Kỳ = **Năm**, 01/01/2026–31/12/2026; Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**; khối kết quả đã render
  (*Thời điểm tạo: 15/07/2026 17:20*, **Tổng vụ việc = 4**); toast đỏ **"Không thể tạo file xuất. Vui lòng thử lại."**;
  chân sidebar ghi **HTPLDN · V1.0**; đồng hồ máy 15/07/2026 17:20.
- `../partner-evidence/VVDHTHT_06_v2.jpg` — cùng màn, URL `...?loai=vu-viec-hoan-thanh&...&donViId=00000000-0000-4000-8000-000000000001`;
  vẫn **"Quản trị viên · QTHT"**; *Thời điểm tạo: 31/07/2026 14:35*, **Tổng vụ việc = 5 · Thành công 5 · Không thành công 0 · Tỷ lệ 100.0%**;
  toast đỏ **"Forbidden"**; chân sidebar **HTPLDN · V1.0.3**; đồng hồ máy 31/07/2026 14:35.

> **Hai vòng bằng chứng KHÔNG cùng bản dựng** (V1.0 vs V1.0.3) và **không cùng số liệu** (4 vs 5 vụ việc) —
> nhưng **cùng vai trò (QTHT), cùng màn, cùng loại BC, cùng kỳ**. Câu chữ thông báo đổi giữa 2 vòng
> (`Không thể tạo file xuất` → `Forbidden`) ⇒ dev có đụng vào chỗ này giữa 2 bản dựng.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chuẩn, đã mở file đọc từng dòng).

- `srs-fr-11-bao-cao.md:62` — Preconditions chung TPL-REPORT-FULL: *"User đã đăng nhập, có role CB Nghiệp vụ
  hoặc CB Phê duyệt (TW/BN/ĐP)"*
- `srs-fr-11-bao-cao.md:79` — Processing bước 1: *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01"*
- `srs-fr-11-bao-cao.md:81` — bước 3: *"Áp dụng phạm vi dữ liệu 2-tier: TW thấy toàn quốc..."*
- `srs-fr-11-bao-cao.md:85` — bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13).
  Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc để xuất hai lần trong ngày không đè tệp `[BA chốt 2026-08-04]`"*
- `srs-fr-11-bao-cao.md:87` — bước 9: *"Giới hạn tối đa 10.000 dòng xuất; nếu vượt thì cắt + cảnh báo | BR-DATA-06"*
- `srs-fr-11-bao-cao.md:116` — E6: *"Lỗi xuất file | ERR-RPT-04 | \"Không thể tạo file xuất. Vui lòng thử lại\" | ERROR"*
- `srs-fr-11-bao-cao.md:117` — E7: *"Không có quyền | ERR-RPT-05 | \"Bạn không có quyền xem báo cáo này\" | ERROR"*
- `srs-fr-11-bao-cao.md:123` — AC chung: *"**Given** CB nhấn \"Xuất Excel\" **When** click **Then** tải file .xlsx
  khổ A4 Times New Roman 13, tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"*
- `srs-fr-11-bao-cao.md:1052` — SCR-IX-01 thành phần 8: *"Nút Xuất Excel | button | \"Xuất Excel (.xlsx)\" →
  xuất theo format TT17/2025 | **click → auto-download** | Sau khi đã \"Xem báo cáo\""*
- `srs-fr-11-bao-cao.md:1058` — thành phần 14: *"Toast xuất file | toast | \"Đang tạo file...\" → \"Xuất thành công\"
  + auto-download | — | Khi nhấn xuất"*
- `srs-fr-11-bao-cao.md:1092` — Quy tắc tương tác: *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị +
  ngày tạo vào header file... Tên tệp cả hai định dạng theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"*
- `srs-fr-11-bao-cao.md:1094` — *"Max 10.000 rows xuất; nếu vượt: cảnh báo + xuất 10.000 dòng đầu"*
- `srs-fr-11-bao-cao.md:1280` — BR-DATA-06: *"File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file"*
- **Riêng loại BC này** — `srs-fr-11-bao-cao.md:270-306` FR-IX-04 *BC Vụ việc đã hoàn thành (UC127)*:
  Tác nhân (`:281`) *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*; Output đặc thù (`:300-306`) gồm
  `tong_hoan_thanh` · `thanh_cong` · `khong_thanh_cong` · `ty_le_thanh_cong` · `theo_linh_vuc[]` ·
  `theo_don_vi[]` · `theo_ky[]`.
- **Ma trận quyền entity** — `srs-v3.5.md:1335`: `| BAO_CAO | R | CRU* | CRU* | CRU* | RU* | RU* | RU* | — | — | — | — |`
  (thứ tự cột QTHT · CB_NV_TW · CB_NV_BN · CB_NV_DP · CB_PD_TW · CB_PD_BN · CB_PD_DP · DN · NHT · TVV · CG)
  ⇒ **QTHT = R (chỉ xem)**, CB_NV_TW = CRU*.

**IM LẶNG về:**
- **Vai trò QTHT có được XUẤT tệp báo cáo hay không.** Đặc tả cho QTHT quyền `R` trên `BAO_CAO` (`srs-v3.5.md:1335`)
  nhưng không nói thao tác "Xuất Excel" thuộc `R` (đọc) hay `C` (tạo bản ghi `BAO_CAO` mới, entity có trường
  `duong_dan_file` — `srs-fr-11-bao-cao.md:1221`). Tiền đề `:62` lại chỉ liệt kê CB NV / CB PD, trong khi phần mềm
  vẫn cho QTHT **xem** được báo cáo.
- Câu chữ cụ thể của thông báo thành công ngoài cụm *"Xuất thành công"* (`:1058`).
- Số cột / thứ tự cột / tên sheet bên trong tệp `.xlsx`.
- Khổ giấy + phông chữ áp thế nào cho một tệp `.xlsx` (`:85` chép khuôn của tệp PDF sang Excel; `.xlsx` không có
  khái niệm khổ giấy bắt buộc trừ khi đặt vùng in).

**Rẽ nhánh:** đặc tả **nói rõ** và **khớp** kỳ vọng đối tác ở vế (a) — bấm Xuất Excel phải tải được tệp
(`:1052` *auto-download*, `:123` AC) → viết mục 4, sang giai đoạn B. Vế phụ về **quyền của QTHT** thì đặc tả
im lặng → chỉ chuyển sang nhánh *cần BA* **nếu** đo ra QTHT bị chặn.

## 3. Precondition

- **Tài khoản (2 vai trò, đo cả hai):**
  1. `admin` / `Secret@123` — vai trò **QTHT**, đúng vai trò đối tác dùng trên cả 2 vòng bằng chứng.
     Đây là **vai trò đang bị tranh chấp**, không phải dùng admin để "mở quyền cho dễ" — nên vẫn ra verdict được.
     `admin` là tài khoản gốc, không có sibling → khoá thì DỪNG, báo user (Rule 7).
  2. `cbnv_tw_02` / `Test@1234` — vai trò **CB_NV_TW**, cấp TW, đúng vai trò đặc tả `:62`. Fallback cùng vai trò +
     cùng cấp: `cbnv_tw_01` → `cbnv_tw`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → *Loại báo cáo* = **BC Vụ việc đã hoàn thành**.
- **Dữ liệu tiền đề:** kỳ đang chọn phải có ≥1 vụ việc hoàn thành (nếu 0 thì màn hiện empty state `:1057` và nút
  Xuất không đo được → phải nới kỳ / đổi đơn vị cho tới khi có dữ liệu, ghi rõ đã nới gì).

## 4. ✅ PASS khi (đủ cả 4, đo được) — ❌ FAIL nếu

**✅ PASS khi:**
- **(a) Vai trò QTHT** (đúng điều kiện đối tác): [Xem báo cáo] → [Xuất Excel] → có **tệp .xlsx về máy** và
  **0 thông báo lỗi** (không có `Không thể tạo file xuất...`, không có `Forbidden`, không có câu lỗi nào khác).
- **(b) Vai trò CB_NV_TW** (vai trò đặc tả): cùng thao tác → có tệp .xlsx về máy, 0 thông báo lỗi.
- **(c) Mở đọc nội dung tệp** (không chỉ kiểm tệp tạo được):
  - Đầu tệp có đủ **4 mục** theo `:1092`: tên báo cáo · kỳ/khoảng thời gian · đơn vị · ngày tạo.
  - Số liệu trong tệp **khớp số liệu trên màn hình**: đối chiếu **≥3 con số cụ thể** trong nhóm
    `tong_hoan_thanh` / `thanh_cong` / `khong_thanh_cong` / `ty_le_thanh_cong` (`:300-303`).
  - Tệp **áp đúng bộ lọc đang chọn**: đổi bộ lọc (dạng D3 mục 5) rồi xuất lại → số liệu trong tệp đổi theo
    (BR-DATA-06 `:1280` *"File xuất theo bộ lọc hiện tại"*).
- **(d) Không phát sinh lỗi mới cùng luồng:** mỗi lần bấm Xuất chỉ sinh **1 yêu cầu tải tệp**, không đẻ thông báo
  trùng lặp, không kẹt trạng thái "Đang tạo file..." vô hạn.

**❌ FAIL nếu:** vẫn hiện thông báo lỗi khi bấm Xuất Excel (bất kể câu chữ) · không có tệp nào về máy ·
tệp về nhưng mở không được / rỗng / 0 dòng dữ liệu trong khi màn hình có số liệu · số liệu trong tệp lệch
số liệu trên màn · tệp không đổi khi đổi bộ lọc · hoặc **fix một phần** (vai trò này chạy được, vai trò kia
vẫn lỗi) — trường hợp cuối vẫn là Reopen theo §Ca biên, trừ khi rơi đúng vào ca *cần BA* dưới đây.

**⚠️ Chuyển sang *cần BA*, KHÔNG tự chấm Fail, nếu:** vai trò **CB_NV_TW xuất được bình thường** nhưng
**QTHT bị chặn quyền** — vì đặc tả im lặng về việc QTHT có được xuất hay không (xem mục 2). Khi đó vẫn phải
ghi nhận hiện trạng + chụp ảnh + nêu câu hỏi cho BA.

**KHÔNG được chấm Fail vì:** thứ tự / tên cột trong tệp `.xlsx` · tên sheet · phông chữ và khổ giấy của tệp
`.xlsx` · câu chữ thông báo thành công khác cụm *"Xuất thành công"* · thiếu quốc hiệu / khối ký (đó là yêu cầu
của tệp **PDF** tại `:86`, không áp cho `.xlsx`) · **tên tệp không theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`**
— phiếu này không nêu tên tệp trong *Kết quả mong đợi*, nên tên tệp là phát hiện ngoài phạm vi (log riêng),
không kéo verdict.

## 5. Dạng dữ liệu phải phủ — M = 3

- **D1 — đúng điều kiện đối tác:** vai trò **QTHT**, BC Vụ việc đã hoàn thành, Kỳ = **Năm** 01/01/2026–31/12/2026,
  Đơn vị = **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**, bộ lọc đặc thù để trống.
- **D2 — vai trò đặc tả:** vai trò **CB_NV_TW** (`cbnv_tw_02`), **cùng** bộ lọc như D1.
- **D3 — đổi bộ lọc:** cùng vai trò D2, đổi **bộ lọc đặc thù** của FR-IX-04 (`:289-290` — *Lĩnh vực PL* hoặc
  *Kết quả* = Thành công / Không thành công) hoặc đổi kỳ → dùng để chứng minh tệp xuất **bám bộ lọc hiện tại**.

**Nguồn xác định M:** ② bộ lọc + giá trị enum ngay trên màn SCR-IX-01 (`:1047-1050` — loại BC · kỳ · đơn vị ·
bộ lọc đặc thù) kết hợp ma trận quyền `srs-v3.5.md:1335` (QTHT `R` vs CB_NV_TW `CRU*` → hai vai trò có thể cho
kết quả khác nhau, nên vai trò là một chiều bắt buộc phủ). M = 1 không phân biệt được "lỗi xuất tệp" với
"chặn quyền", mà bằng chứng vòng 2 (`Forbidden`) đúng là dấu hiệu chặn quyền.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên · QTHT**, nhãn đơn vị BTP · TW (cả 2 vòng bằng chứng) | **Cả hai**: `admin` (QTHT, BTP · TW) + `cbnv_tw_02` (CB_NV_TW, BTP · TW) | Không |
| Entity + trạng thái | Báo cáo **BC Vụ việc đã hoàn thành** đã [Xem báo cáo] xong (khối kết quả đã render; nút Xuất mới bật theo `:1052`). Vòng 1: Tổng 4 · Vòng 2: Tổng 5 / TC 5 / KTC 0 / 100.0% | Cùng loại BC, đã [Xem báo cáo] xong, nút Xuất đã bật. Số liệu env này: Tổng 15 / TC 3 / KTC 0 / 20.0% | Không (khác **số liệu** vì khác env — đã nêu ở Giới hạn hiệu lực) |
| Dữ liệu tiền đề | Kỳ **Năm** 01/01/2026–31/12/2026, đơn vị **BTP-TW**; có dữ liệu (4 rồi 5 vụ việc hoàn thành) | Kỳ **Năm** 01/01/2026–31/12/2026, đơn vị **Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW)**; có dữ liệu (15 vụ việc) | Không |
| Input / filter / giá trị nhập | Bộ lọc đặc thù (*Lĩnh vực PL*, *Kết quả*) để **trống**; thao tác = bấm nút **[Xuất Excel]** | D1/D2: cả 2 ô lọc để **trống**, bấm **[Xuất Excel]**. D3: *Kết quả* = **Thành công** | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 2 lượt thử, 1 vai trò, 1 bộ lọc (M = 1) — không có mẫu đối chứng để tách "lỗi tạo tệp" khỏi "chặn quyền" | **M = 3** (D1 QTHT · D2 CB_NV_TW cùng lọc · D3 CB_NV_TW đổi lọc) — đủ mẫu đối chứng | Không |

**3 dữ kiện neo của đối tác:**
`htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-hoan-thanh&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001` ·
báo cáo đã render xong, nút Xuất đã bật, *Thời điểm tạo* 15/07/2026 17:20 (vòng 1) và 31/07/2026 14:35 (vòng 2) ·
vai trò **QTHT**, env **`htpldn-uat.ospgroup.vn`**, bản dựng **V1.0** (vòng 1) → **V1.0.3** (vòng 2).

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên env `htpldn-uat.ospgroup.vn`; lượt này đo trên
`18.143.165.120.nip.io` theo chỉ định của prompt. Hai env **khác bộ dữ liệu** (đã có tiền lệ: env nip.io
23.000.000/2 hồ sơ vs ospgroup 226.308.268/25 hồ sơ ở case CPCTHTTTG_03) nên **con số tuyệt đối sẽ khác** —
tiêu chí mục 4 vì vậy chỉ đối chiếu *tệp khớp màn hình của chính lượt đo này*, không đối chiếu với số của đối tác.
Verdict chỉ có hiệu lực cho env + bản dựng ghi ở đầu file.

## 7. Kết quả đo (giai đoạn B — 2026-08-06, bản dựng V1.0.8)

**D1 — vai trò QTHT (`admin`), đúng điều kiện đối tác — ❌ KHÔNG xuất được**

| Đo gì | Kết quả |
|---|---|
| Màn hình trước khi bấm | `/bao-cao?loai=vu-viec-hoan-thanh&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001` — đã render, *Thời điểm tạo 06/08/2026 12:55*, Tổng 15 · TC 3 · KTC 0 · 20.0% |
| Số lần gọi máy chủ | **1** — `POST /api/v1/bao-cao/export` |
| Máy chủ trả về | **HTTP 403** · `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}}` (reqid 104, 06:56:38Z) |
| Chữ trên thông báo | **`Forbidden`** (ảnh `../bug-reports/image/VVDHTHT_06-D1-qtht-toast.png`) — trước đó hiện `Đang tạo file...` rồi bị thay bằng câu lỗi |
| Tệp về máy | **KHÔNG** (0 blob, 0 thẻ `<a download>`) |
| Vai trò trong thẻ đăng nhập | `vaiTro:["QTHT"]`, `donViId:...0001`, `capDonVi:"TW"` (giải mã từ cookie `access_token` của chính request 403) |

**D2 — vai trò CB_NV_TW (`cbnv_tw_02`), cùng bộ lọc — ✅ xuất bình thường**

| Đo gì | Kết quả |
|---|---|
| Số lần gọi máy chủ | **1** — `POST /api/v1/bao-cao/export` |
| Tệp về máy | **CÓ** — `BaoCaoVuViecHoanThanh_20260806_1301.xlsx`, 6 990 byte, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Thông báo lỗi | **0** (chỉ có `Đang tạo file...`, không có câu lỗi nào) |
| 4 mục đầu tệp (`:1092`) | ✔ đủ — dòng 1 `BC Vụ việc đã hoàn thành` · dòng 2 `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · dòng 3 `Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp` · dòng 4 `Ngày tạo: 06/08/2026` |
| Số liệu tệp vs màn hình | ✔ khớp **7/7 con số**: Tổng 15 · Thành công 3 · Không thành công 0 · Tỷ lệ 20 · Dân sự 11 · Thương mại 4 · Chưa xác định 12 |
| Tên trang tính | `BC Vụ việc đã hoàn thành` |

**D3 — CB_NV_TW, đổi bộ lọc *Kết quả* = Thành công — ✅ tệp bám bộ lọc**

Màn hình đổi thành Tổng 3 · Tỷ lệ 100.0% · chỉ còn Thương mại 3. Tệp `BaoCaoVuViecHoanThanh_20260806_1303.xlsx` (6 918 byte) đổi theo đúng như vậy: `Tổng số vụ việc = 3`, `Tỷ lệ thành công (%) = 100`, mục *Theo lĩnh vực* chỉ còn `Thương mại 3`. ⇒ thoả BR-DATA-06 (`:1280` *"File xuất theo bộ lọc hiện tại"*).

**Kiểm chéo bằng phương pháp thứ hai:** kết luận D1 không chỉ dựa vào chữ trên thông báo mà đối chiếu với **mã lỗi + mã HTTP ở tầng mạng** (`list_network_requests` → `get_network_request` reqid 104). Hai nguồn khớp nhau: giao diện báo `Forbidden`, máy chủ trả 403 `ERR-PERM-SYS-00-01`.

**Tự kiểm bộ đo:** `soObserverDangSong = 1` ở cả hai phiên (QTHT và CB_NV_TW) trước khi tin số liệu.

## 8. Kết luận

**Verdict: cần BA** — rơi đúng nhánh đã ghi sẵn ở mục 4 trước khi đo: *CB_NV_TW xuất được bình thường nhưng QTHT bị chặn quyền*.

- Triệu chứng đối tác phản ánh **vẫn còn nguyên** ở bản dựng V1.0.8 với **đúng vai trò đối tác đã dùng** (QTHT): bấm [Xuất Excel] → `Forbidden`, không có tệp về máy. Không thể chấm Pass.
- Nhưng cũng **không chấm Fail**, vì với vai trò mà đặc tả nêu đích danh (`:62` CB Nghiệp vụ / CB Phê duyệt) thì chức năng chạy đúng và đủ: tệp về máy, 4 mục đầu tệp đủ, số liệu khớp màn hình, tệp bám bộ lọc. Cái đang tranh chấp là **QTHT có được xuất báo cáo hay không** — đặc tả im lặng (mục 2).
- Câu hỏi gửi BA + phát hiện phụ về câu chữ thông báo: xem `../../reverify-week-5/ba-confirm/cau-hoi-BA.md` và `../bug-reports/bug-report-BCTK.md`.

**Phát hiện ngoài phạm vi phiếu này (không kéo verdict):** tên tệp `BaoCaoVuViecHoanThanh_20260806_1301.xlsx` **đúng khuôn** `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`:85`, `:1092` `[BA chốt 2026-08-04]`) — phiếu này không nêu tên tệp trong *Kết quả mong đợi* nên chỉ ghi nhận, không tính điểm.
