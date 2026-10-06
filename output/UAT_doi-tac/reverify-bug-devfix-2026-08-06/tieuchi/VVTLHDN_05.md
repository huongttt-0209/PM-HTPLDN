# Tiêu chí verify — VVTLHDN_05 (tab `bug`, dòng 230)

Mã case: VVTLHDN_05          Thời điểm viết: 2026-08-06 12:51
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **HTPLDN · V1.0.8** (`assets/index-CNwX9JjX.js`)

**Hồ sơ QA nội bộ đã đọc trước khi viết mục 4:** `reverify-week-4/reverify-round-2026-08-03/cond/VVTLHDN_05.md` ·
`.../KET-QUA-REVERIFY-VONG-2.md` §25 · `.../GUI-BA-2026-08-03/ba-confirmation-needed-bao-cao-thong-ke-xuat-file-2026-08-03.md` ·
`reverify-week-4/reverify-round-2026-08-04/phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md` (Vấn đề 16–18, BA duyệt 04/08) ·
`reverify-week-3/bug-reports/bctk/Pass-bug-report-bctk-batch10-export.md` · `tasks/srs-contradictions.md` §SRS-C-010
(Open — chỉ nói về tệp **PDF**). Mục 4 suy từ **đặc tả**, không lấy số đo cũ làm ngưỡng.

---

## 1. Đối tác phản ánh

- **(a)** Bấm **[Xuất Excel]** sau khi đã [Xem báo cáo] → không tải được tệp, hiện thông báo lỗi.
  - Vòng 1 (16/07/2026 15:54, bản dựng **V1.0**): `Không thể tạo file xuất. Vui lòng thử lại.`
  - Vòng 2 (retest TKM 31/07/2026 15:09, bản dựng **V1.0.3**): `Forbidden`
- **(b)** Ô *Kết quả mong đợi* ghi thêm: *"Tên tệp xuất: `BaoCaoVuViec_{YYYYMMDD_HHmm}.xlsx`"*
  → **tên tệp LÀ một vế của case này**.

**Bằng chứng đã mở xem full-res:**
- `../partner-evidence/VVTLHDN_05.jpg` — góc phải **"Quản trị viên · QTHT"**, nhãn **BTP · TW**; tiêu đề khối kết quả
  **BC Vụ việc theo loại hình DN**; Kỳ = **Năm** 01/01/2026–31/12/2026; Đơn vị = **Toàn quốc**; ô lọc **Loại DN**
  để **trống** ("Chọn Loại DN"); *Thời điểm tạo 16/07/2026 15:54*; biểu đồ cột nhóm, trục tối đa 12;
  toast đỏ **"Không thể tạo file xuất. Vui lòng thử lại."**; sidebar **HTPLDN · V1.0**.
  (Thanh địa chỉ còn giữ `loai=vu-viec-theo-linh-vuc` của lần chọn trước — nhưng dropdown, tiêu đề khối kết quả,
  ô lọc *Loại DN* và biểu đồ đều là **BC Vụ việc theo loại hình DN**, nên đúng case.)
- `../partner-evidence/VVTLHDN_05_v2.jpg` — cùng loại BC (dropdown ghi rõ **BC Vụ việc theo loại hình DN**), cùng vai trò
  **QTHT**, Đơn vị **Toàn quốc**, ô lọc *Loại DN* vẫn trống; *Thời điểm tạo 31/07/2026 15:09*;
  toast đỏ **"Forbidden"**; sidebar **HTPLDN · V1.0.3**.

> Hai vòng **cùng vai trò (QTHT) · cùng loại BC · cùng kỳ · cùng đơn vị · cùng bộ lọc Loại DN (trống)**,
> khác bản dựng (V1.0 → V1.0.3) và khác câu chữ thông báo ⇒ dev có đụng vào chỗ này giữa 2 bản dựng.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (đã mở file đọc từng dòng).

- `srs-fr-11-bao-cao.md:62` — *"User đã đăng nhập, có role CB Nghiệp vụ hoặc CB Phê duyệt (TW/BN/ĐP)"*
- `srs-fr-11-bao-cao.md:79` — bước 1: *"Kiểm tra quyền truy cập báo cáo + phạm vi theo đơn vị | BR-AUTH-01"*
- `srs-fr-11-bao-cao.md:85` — bước 7: *"Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13).
  Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` — phần giờ-phút bắt buộc... `[BA chốt 2026-08-04]`"*
- `srs-fr-11-bao-cao.md:116` — E6: *"Lỗi xuất file | ERR-RPT-04 | \"Không thể tạo file xuất. Vui lòng thử lại\""*
- `srs-fr-11-bao-cao.md:117` — E7: *"Không có quyền | ERR-RPT-05 | \"Bạn không có quyền xem báo cáo này\""*
- `srs-fr-11-bao-cao.md:123` — AC chung: *"...**Then** tải file .xlsx ..., tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`"*
- `srs-fr-11-bao-cao.md:1052` — SCR-IX-01 thành phần 8: *"Nút Xuất Excel ... **click → auto-download** | Sau khi đã \"Xem báo cáo\""*
- `srs-fr-11-bao-cao.md:1058` — thành phần 14: *"Toast xuất file ... \"Đang tạo file...\" → \"Xuất thành công\" + auto-download"*
- `srs-fr-11-bao-cao.md:1092` — *"Export XLSX/PDF chèn tiêu đề BC + thông tin kỳ + đơn vị + ngày tạo vào header file...
  Tên tệp cả hai định dạng theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` `[BA chốt 2026-08-04]`"*
- `srs-fr-11-bao-cao.md:1280` — BR-DATA-06: *"File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file"*
- **Riêng loại BC này** — `srs-fr-11-bao-cao.md:626-661` FR-IX-13 *BC Vụ việc theo loại hình DN (UC136)*:
  mô tả (`:635`) *"cross-tab vụ việc theo loại doanh nghiệp (siêu nhỏ/nhỏ/vừa), phân theo đơn vị"*;
  Tác nhân (`:637`) *"CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)"*; **Input đặc thù** (`:645`) `loai_dn` —
  *"SIEU_NHO / NHO / VUA"*, không bắt buộc; Output đặc thù (`:655-658`) gồm `loai_dn` · `ten_loai_dn` ·
  `tong` · `theo_don_vi[]`; AC (`:661`) *"**Then** cross-tab: hàng = loại DN, cột = đơn vị"*.
- **Ma trận quyền entity** — `srs-v3.5.md:1335` (chép nguyên văn):
  `| BAO_CAO | R | CRU* | CRU* | CRU* | RU* | RU* | RU* | — | — | — | — |`
  (thứ tự cột QTHT · CB_NV_TW · CB_NV_BN · CB_NV_DP · CB_PD_TW · CB_PD_BN · CB_PD_DP · DN · NHT · TVV · CG)
  ⇒ **QTHT = R (chỉ xem)**, CB_NV_TW = `CRU*`.

**Về vế (b) — tên tệp:** BA chốt **04/08/2026** khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.{ext}` áp cho **mọi định dạng
xuất** của nhóm IX (nguồn: `phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md` Vấn đề 17; đã ghi vào đặc tả `:85` + `:1092`)
⇒ **đặc tả nói rõ và KHỚP kỳ vọng đối tác**. Câu *"26 phiếu Xuất Excel đã đóng — không mở lại"* trong phiếu BA
không áp cho dòng 230 vì dòng này **chưa đóng** (`Kết quả verify` trống, đang chờ verify lượt này).

**IM LẶNG về:** vai trò **QTHT có được XUẤT** tệp báo cáo hay không (matrix cho `R`, không nói "Xuất Excel" thuộc
`R` hay `C`; tiền đề `:62` không liệt kê QTHT nhưng phần mềm vẫn cho QTHT **xem** báo cáo) · phần `{TenBaoCao}`
cụ thể của từng loại BC · câu chữ thông báo thành công ngoài *"Xuất thành công"* · số cột / thứ tự cột / tên sheet
trong tệp · khổ giấy + phông chữ áp thế nào cho một tệp `.xlsx`.

**Rẽ nhánh:** cả 2 vế — đặc tả **nói rõ** và **khớp** kỳ vọng đối tác → viết mục 4, sang giai đoạn B.
Vế phụ về quyền QTHT im lặng → chỉ chuyển *cần BA* **nếu** đo ra QTHT bị chặn.

## 3. Precondition

- **Tài khoản (2 vai trò, đo cả hai):**
  1. `admin` / `Secret@123` — **QTHT**, đúng vai trò đối tác dùng; là vai trò **đang bị tranh chấp** nên vẫn ra
     verdict được. Không có sibling → khoá thì DỪNG, báo user (Rule 7).
  2. `cbnv_tw_02` / `Test@1234` — **CB_NV_TW** cấp TW (vai trò đặc tả `:62`). Fallback: `cbnv_tw_01` → `cbnv_tw`.
- **Màn:** `https://18.143.165.120.nip.io/bao-cao` → *Loại báo cáo* = **BC Vụ việc theo loại hình DN**,
  ô lọc **Loại DN để trống** (đúng như bằng chứng đối tác).
- **Dữ liệu tiền đề:** kỳ đang chọn phải có ≥1 vụ việc gắn DN ở phạm vi Toàn quốc (0 → empty state `:1057`,
  nút Xuất không đo được → nới kỳ, ghi rõ đã nới gì).

## 4. ✅ PASS khi (đủ cả 5, đo được) — ❌ FAIL nếu

**✅ PASS khi:**
- **(a) Vai trò QTHT:** [Xem báo cáo] → [Xuất Excel] → có **tệp .xlsx về máy**, **0 thông báo lỗi**.
- **(b) Vai trò CB_NV_TW:** cùng thao tác → có tệp .xlsx về máy, 0 thông báo lỗi.
- **(c) Tên tệp** theo khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`: có **phần giờ-phút** (không chỉ ngày),
  `{TenBaoCao}` viết liền không dấu. *(Không đòi đúng chữ `BaoCaoVuViec`.)*
- **(d) Mở đọc nội dung tệp:** đầu tệp đủ **4 mục** theo `:1092` (tên BC · kỳ/khoảng thời gian · đơn vị · ngày tạo);
  số liệu **khớp màn hình** — đối chiếu **≥3 con số**: `tong` của ít nhất 2 loại DN khác nhau + tổng cộng
  (`:655-658`); tệp **áp đúng bộ lọc hiện tại** (đặt ô lọc **Loại DN** = 1 giá trị cụ thể — dạng D3 — rồi xuất lại
  → tệp chỉ còn loại DN đó, `:1280`).
- **(e) Không phát sinh lỗi mới cùng luồng:** 1 lần bấm Xuất = **1 yêu cầu tải tệp**, không thông báo trùng lặp,
  không kẹt "Đang tạo file..." vô hạn.

**❌ FAIL nếu:** vẫn hiện thông báo lỗi khi bấm Xuất Excel (bất kể câu chữ) · không có tệp về máy · tệp mở không
được / rỗng / 0 dòng trong khi màn hình có số liệu · số liệu tệp lệch màn hình · **tệp không đổi khi đặt bộ lọc
Loại DN** · **tên tệp thiếu phần giờ-phút hoặc không theo khuôn đã chốt** · hoặc **fix một phần** → Reopen theo §Ca biên.

**⚠️ Chuyển sang *cần BA*, KHÔNG tự chấm Fail, nếu:** CB_NV_TW xuất bình thường nhưng **QTHT bị chặn quyền**.

**KHÔNG được chấm Fail vì:** `{TenBaoCao}` không đúng y chữ `BaoCaoVuViec` · thứ tự / tên cột · tên sheet ·
phông chữ và khổ giấy của `.xlsx` · câu chữ thông báo thành công · thiếu quốc hiệu / khối ký (yêu cầu của **PDF** `:86`).

## 5. Dạng dữ liệu phải phủ — M = 3

- **D1 — đúng điều kiện đối tác:** vai trò **QTHT**, BC Vụ việc theo loại hình DN, Kỳ = **Năm**
  01/01/2026–31/12/2026, Đơn vị = **Toàn quốc**, ô lọc **Loại DN để trống**.
- **D2 — vai trò đặc tả:** **CB_NV_TW** (`cbnv_tw_02`), **cùng** bộ lọc như D1.
- **D3 — đổi bộ lọc đặc thù:** cùng vai trò D2, đặt **Loại DN** = 1 giá trị (Siêu nhỏ / Nhỏ / Vừa — enum `:645`)
  → chứng minh tệp xuất **bám bộ lọc hiện tại**.

**Nguồn xác định M:** ② bộ lọc + giá trị enum ngay trên màn SCR-IX-01 (`:1047-1050`, bộ lọc đặc thù *Loại DN* tại
`:1076`) + enum `SIEU_NHO / NHO / VUA` (`:645`), kết hợp ma trận quyền `srs-v3.5.md:1335` (QTHT `R` vs CB_NV_TW
`CRU*` ⇒ vai trò là chiều bắt buộc phủ). M = 1 không tách được "lỗi tạo tệp" khỏi "chặn quyền", mà bằng chứng
vòng 2 (`Forbidden`) đúng là dấu hiệu chặn quyền.

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên · QTHT**, nhãn đơn vị BTP · TW (cả 2 vòng) | **Cả hai**: `admin` (QTHT, BTP · TW) + `cbnv_tw_02` (CB_NV_TW, BTP · TW) | Không |
| Entity + trạng thái | **BC Vụ việc theo loại hình DN** đã [Xem báo cáo] xong, biểu đồ cột nhóm đã render (nút Xuất mới bật theo `:1052`) | Cùng loại BC, đã [Xem báo cáo] xong, nút Xuất đã bật. Số liệu env này: 3 nhóm quy mô, Tổng 35 | Không (khác **số liệu** vì khác env — đã nêu ở Giới hạn hiệu lực) |
| Dữ liệu tiền đề | Kỳ **Năm** 01/01/2026–31/12/2026, Đơn vị = **Toàn quốc**; có dữ liệu (trục biểu đồ tối đa 12) | Kỳ **Năm** 01/01/2026–31/12/2026, Đơn vị = **Toàn quốc**; có dữ liệu (3 nhóm quy mô) | Không |
| Input / filter / giá trị nhập | Ô lọc đặc thù **Loại DN để trống**; thao tác = bấm nút **[Xuất Excel]** | D1/D2: ô lọc **Loại DN để trống**, bấm **[Xuất Excel]**. D3: **Loại DN** = Siêu nhỏ | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | 2 lượt thử, 1 vai trò, 1 bộ lọc (M = 1) — không có mẫu đối chứng tách "lỗi tạo tệp" khỏi "chặn quyền", và chưa bao giờ tải được tệp nên không đo được tên tệp lẫn nội dung | **M = 3** (D1 QTHT · D2 CB_NV_TW cùng lọc · D3 CB_NV_TW đổi lọc) — đủ mẫu đối chứng, và đã tải được tệp nên đo được cả tên tệp lẫn nội dung | Không |

**3 dữ kiện neo của đối tác:** màn `htpldn-uat.ospgroup.vn/bao-cao`, loại BC **Vụ việc theo loại hình DN**,
Kỳ Năm 2026, Đơn vị Toàn quốc, Loại DN trống · báo cáo đã render, nút Xuất đã bật, *Thời điểm tạo*
16/07/2026 15:54 (vòng 1) và 31/07/2026 15:09 (vòng 2) · vai trò **QTHT**, env **`htpldn-uat.ospgroup.vn`**,
bản dựng **V1.0** → **V1.0.3**.

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn`; lượt này đo trên
`18.143.165.120.nip.io` theo chỉ định của prompt. Hai env khác bộ dữ liệu ⇒ con số tuyệt đối sẽ khác; mục 4
chỉ đối chiếu *tệp khớp màn hình của chính lượt đo này*. Verdict chỉ có hiệu lực cho env + bản dựng ghi ở đầu file.


## 7. Kết quả đo (giai đoạn B — 2026-08-06, bản dựng V1.0.8)

**D1 — vai trò QTHT (`admin` (QTHT, BTP · TW)), đúng điều kiện đối tác — ❌ KHÔNG xuất được**

| Đo gì | Kết quả |
|---|---|
| Màn hình trước khi bấm | `/bao-cao?loai=vu-viec-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` — đã render, *Thời điểm tạo 06/08/2026 13:19*, 3 nhóm quy mô (Nhỏ 16 · Siêu nhỏ 18 · Không phân loại 1) |
| Số lần gọi máy chủ | **1** — `POST /api/v1/bao-cao/export` |
| Máy chủ trả về | **HTTP 403** · `{"success":false,"error":{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}}` (reqid 842, 06:20:00Z) |
| Chữ trên thông báo | **`Forbidden`** — đọc thẳng từ khung thông báo đang hiện trên màn (`.ant-message-notice-wrapper`), sau khi thay chữ `Đang tạo file...` |
| Tệp về máy | **KHÔNG** (0 blob, 0 thẻ `<a download>`) |
| Vai trò trong thẻ đăng nhập | `vaiTro:["QTHT"]`, `donViId:...0001`, `capDonVi:"TW"` (giải mã từ cookie `access_token` của chính request 403) |
| Ảnh | `../bug-reports/image/VVTLHDN_05-D1-qtht-man-hinh.png` |

**D2 — vai trò CB_NV_TW (`cbnv_tw_02`), cùng bộ lọc — ✅ xuất bình thường**

| Đo gì | Kết quả |
|---|---|
| Số lần gọi máy chủ | **1** — `POST /api/v1/bao-cao/export` |
| Tệp về máy | **CÓ** — `BaoCaoVuViecTheoLoaiDn_20260806_1306.xlsx`, 6 801 byte, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Thông báo lỗi | **0** (chỉ có `Đang tạo file...`) |
| 4 mục đầu tệp (`:1092`) | ✔ đủ — dòng 1 `BC Vụ việc theo loại hình DN` · dòng 2 `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · dòng 3 `Đơn vị: Toàn quốc` · dòng 4 `Ngày tạo: 06/08/2026` |
| Số liệu tệp vs màn hình | ✔ khớp **16/16 con số**: Tổng 35 · Nhỏ 10/3/3/0/16 · Siêu nhỏ 12/2/0/4/18 · (Không phân loại) 1/0/0/0/1 |
| Tên trang tính | `Vụ việc theo loại hình DN` |
| Ảnh | `../bug-reports/image/VVTLHDN_05-D2-cbnvtw.png` |

**Tên tệp:** `BaoCaoVuViecTheoLoaiDn_20260806_1306.xlsx` — **đúng khuôn** `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` (`srs-fr-11-bao-cao.md:85`, `:1092` `[BA chốt 2026-08-04]`, AC `:123`). Đây là một vế của *Kết quả mong đợi* phiếu này ⇒ tính vào tiêu chí, và **đạt**.

**D3 — CB_NV_TW, đặt **Loại DN** = Siêu nhỏ (enum `SIEU_NHO` — `:645`) — ✅ tệp bám bộ lọc**

Màn hình đổi còn đúng 1 dòng `Siêu nhỏ 12 / 4 / 2 / Tổng 18`. Tệp `BaoCaoVuViecTheoLoaiDn_20260806_1306.xlsx` (6 682 byte) đổi theo: `Tổng số vụ việc = 18`, mục *Theo loại hình doanh nghiệp* chỉ còn dòng `Siêu nhỏ | 12 | 4 | 2 | 18`. ⇒ thoả BR-DATA-06 (`:1280` *"File xuất theo bộ lọc hiện tại"*).

**Kiểm chéo bằng phương pháp thứ hai:** kết luận D1 không chỉ dựa vào chữ trên thông báo mà đối chiếu với **mã lỗi + mã HTTP ở tầng mạng** (`list_network_requests` → `get_network_request`). Hai nguồn khớp nhau: giao diện báo `Forbidden`, máy chủ trả 403 `ERR-PERM-SYS-00-01`.

**Tự kiểm bộ đo:** `soObserverDangSong = 1` ở cả hai phiên (QTHT và CB_NV_TW) trước khi tin số liệu.

## 8. Kết luận

**Verdict: cần BA** — rơi đúng nhánh đã ghi sẵn ở mục 4 trước khi đo: *CB_NV_TW xuất được bình thường nhưng QTHT bị chặn quyền*.

- Triệu chứng đối tác phản ánh **vẫn còn nguyên** ở bản dựng V1.0.8 với **đúng vai trò đối tác đã dùng** (QTHT): bấm [Xuất Excel] → `Forbidden`, không có tệp về máy. Không thể chấm Pass.
- Nhưng cũng **không chấm Fail**, vì với vai trò mà đặc tả nêu đích danh (`:62` CB Nghiệp vụ / CB Phê duyệt) thì chức năng chạy đúng và đủ: tệp về máy, **tên tệp đúng khuôn**, 4 mục đầu tệp đủ, số liệu khớp màn hình, tệp bám bộ lọc. Cái đang tranh chấp là **QTHT có được xuất báo cáo hay không** — đặc tả im lặng (mục 2).
- Câu hỏi gửi BA + phát hiện phụ về câu chữ thông báo: xem `../../reverify-week-5/ba-confirm/cau-hoi-BA.md` và `../bug-reports/bug-report-BCTK.md`.
