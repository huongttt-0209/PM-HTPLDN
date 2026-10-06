Mã case: VVTTG_05 (tab `bug` dòng 195)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (`HTPLDN · V1.0.8`) — đo 06/08/2026 14:32–14:35

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có (chưa từng qua vòng soát nội bộ).

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc theo thời gian** (SCR-IX-01, `loai=vu-viec-theo-thoi-gian`). **1 vế duy nhất:** bấm
**Xuất Excel** thì không nhận được tệp, hệ thống báo lỗi.

**Bằng chứng đã mở xem:**

| Tệp | Vòng | Thấy gì |
|---|---|---|
| `../partner-evidence/VVTTG_05.jpg` | Vòng 1 — 15/07/2026 | Vai trò **Quản trị viên QTHT**. Thông báo **"Không thể tạo file xuất. Vui lòng thử lại."** |
| `../partner-evidence/VVTTG_05_v2.jpg` | Vòng 2 — 31/07/2026 14:50 | Bản dựng **V1.0.3**, vẫn **QTHT** (BTP·TW). Loại BC `BC Vụ việc theo thời gian`, Kỳ **Năm** 01/01/2026–31/12/2026, Đơn vị **Toàn quốc**, Lĩnh vực PL để trống. Màn **đã ra dữ liệu**: `Tổng vụ việc toàn kỳ = 51`, `Thời điểm tạo: 31/07/2026 14:50`. Thông báo đổi thành **"Forbidden"**. Nút `Xuất Excel` / `Xuất PDF` hiện bình thường. Thanh địa chỉ có **biểu tượng tải xuống** — dấu hiệu trình duyệt từng nhận tệp nào đó trong phiên, cần đo lại chứ không suy đoán. |

**Lệch giữa 2 vòng:** cùng vai trò (QTHT), **khác bản dựng** (V1.0 → V1.0.3 — lưu ý V1.0.3 **cao hơn**
bản V1.0.2 ở 2 case xuất tệp kia, tức đối tác chụp sau khi env đã deploy tiếp), **khác triệu chứng**
(`ERR-RPT-04` → `Forbidden`).

**Ghi chú dev:** cột "DEV phản hồi lần 1" dòng 195 ghi *"Đã kiểm tra trên môi trường DEV nhưng chưa tái
hiện được lỗi; chức năng hiện hoạt động đúng theo thiết kế."* — không khớp triệu chứng vòng 2. Vẫn chạy
đủ luồng, không tin mô tả.

> 🔴 Case này **cùng câu triệu chứng** với VVDTN_06 và VVDHT_06 nhưng **khác màn** ⇒ phải đo riêng trên
> màn BC Vụ việc theo thời gian. Cấm suy kết quả từ case anh em.
>
> ⚠️ Màn này còn có case **VVTTG_01** (số liệu) chạy cùng phiên. Verdict của VVTTG_05 chỉ do vế **xuất
> tệp** quyết định; nếu số liệu trong tệp sai vì bản thân báo cáo sai thì đó là chuyện của VVTTG_01 —
> ghi chéo, không trộn verdict. Ngoại lệ: nếu báo cáo không ra nổi dữ liệu thì không xuất được và
> VVTTG_05 thành **ô trống** vì thiếu tiền đề.

---

## 2. Đặc tả nói gì

→ Xem [`_chung-xuat-excel.md` §2](_chung-xuat-excel.md). Riêng màn này: **FR-IX-05 (UC128)**, tác nhân
`srs-fr-11-bao-cao.md:325` = `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`; tên báo cáo hiển thị
`:1068` = `BC Vụ việc theo thời gian`; output `:337` = `trend_data[] {ky_label, tiep_nhan, hoan_thanh}` —
đây là báo cáo dạng **trend nhiều mốc**, nên tệp xuất phải chứa được **từng mốc thời gian**, không chỉ
mỗi con số tổng.

---

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw` / `Test@1234`** (`CB_NV_TW`, cấp TW — mới thấy được "Toàn quốc" như
  đối tác, `:81`/`:1049`).
- Tài khoản đối chứng GAP vai trò: **`admin` / `Secret@123`** (QTHT) — trùng khít vai trò đối tác.
- Màn: `https://18.143.165.120.nip.io/bao-cao` → Loại báo cáo **"BC Vụ việc theo thời gian"**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Toàn quốc**, Lĩnh vực PL để trống.
- Dữ liệu tiền đề: kỳ đã chọn phải **có** dữ liệu (Xem báo cáo ra `Tổng vụ việc toàn kỳ` > 0) — nút Xuất
  chỉ dùng được sau khi Xem báo cáo (`:1052`).

---

## 4. Tiêu chí chấm

→ Dùng nguyên [`_chung-xuat-excel.md` §4](_chung-xuat-excel.md), đo trên **màn BC Vụ việc theo thời gian**.
Cụ thể hoá 3 chỗ:

- Tiêu chí 3 (số khớp màn): tổng phải khớp là ô **`Tổng vụ việc toàn kỳ`**; ngoài ra tệp phải đọc ra được
  **từng mốc thời gian kèm số vụ việc** khớp đúng các điểm trên biểu đồ/bảng của màn (`:337`).
- Tiêu chí 4 (áp đúng bộ lọc): phép thử là **đổi Kỳ báo cáo** (Năm → Tháng) rồi xuất lại — số mốc trong
  tệp phải đổi theo, vì đây là báo cáo trend.
- Tiêu chí 5 (tên tệp): khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` với `{TenBaoCao}` suy theo `:86` từ tên
  `BC Vụ việc theo thời gian`. Chấm theo **khuôn**, không theo chuỗi tự nghĩ.

---

## 5. Dạng dữ liệu phải phủ

→ Dùng nguyên [`_chung-xuat-excel.md` §5](_chung-xuat-excel.md) — **M = 3**:
① `cbnv_tw` + kỳ có dữ liệu · ② `admin` (QTHT) + kỳ có dữ liệu · ③ `cbnv_tw` + đổi bộ lọc.
Dạng ③ trên màn này = **đổi Kỳ báo cáo Năm → Tháng** rồi xuất lại và so nội dung 2 tệp (số mốc trend phải
khác nhau) — đây là phép thử mạnh nhất cho tiêu chí 4 trên màn trend.

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên QTHT** (`BTP · TW`) ở cả 2 vòng — KHÔNG thuộc tác nhân FR-IX-05 (`:325`) | Đo **cả hai**: ① **`cbpd_tw_01`** (`CB_PD_TW`, `donViId=…0001`, `capDonVi=TW`) — **nới đã khai**, xem "Sửa đổi giữa chừng"; vẫn nằm **trong** danh sách tác nhân `:325` (`CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`) và cùng cấp TW ⇒ cùng phạm vi Toàn quốc như đối tác · ② **`admin` (QTHT)** — **trùng khít vai trò đối tác**, đo trên chính giao diện, bấm nút Xuất thật | **Không** |
| Entity + trạng thái | VU_VIEC, chỉ bản ghi đã duyệt (`:82`). Báo cáo đã render xong rồi mới bấm Xuất | Cùng loại + cùng thứ tự: Xem báo cáo ra dữ liệu (`Thời điểm tạo 06/08/2026 14:32` cho CB Phê duyệt, `14:34` cho QTHT) **rồi mới** bấm Xuất | **Không** |
| Dữ liệu tiền đề | Kỳ CÓ dữ liệu: `Tổng vụ việc toàn kỳ = 51` (31/07 14:50) | Kỳ CÓ dữ liệu: `Tổng vụ việc toàn kỳ = **50**` (Toàn quốc, cả 2 vai trò ra cùng con số) — sát con số 51 của đối tác, **cùng bản chất** (kỳ có dữ liệu ⇒ nút Xuất dùng được) | **Không** |
| Input / filter / giá trị nhập | Kỳ `NAM`, `tuNgay=2026-01-01`, `denNgay=2026-12-31`, **không có `donViId`** ⇒ Đơn vị `Toàn quốc`; Lĩnh vực PL để trống. Định dạng xuất: **Excel** | Giữ nguyên toàn bộ bộ lọc đối tác cho dạng ① và ②; dạng ③ **đổi Kỳ Năm → Tháng** (giao diện tự thu khoảng về 01/08–31/08/2026). Định dạng xuất: **Excel** | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 51 vụ việc · đối tác chỉ đo **1 dạng** (QTHT + kỳ Năm + Toàn quốc), không đổi vai trò, không đổi kỳ | Phủ đủ **M = 3**: ① `cbpd_tw_01` kỳ Năm Toàn quốc → HTTP 200, tệp `BaoCaoVuViecTheoThoiGian_20260806_1432.xlsx` **mở đọc được**, đủ 4 dòng tiêu đề, có bảng **"Theo kỳ"** (`Năm 2026 · 01/01/2026 · 31/12/2026 · Tiếp nhận 50 · Hoàn thành 18`) và bảng **"Theo đơn vị"** (6+5+36+3 = 50) — khớp màn từng con số · ② `admin` QTHT → Xem báo cáo **200** (50) nhưng `POST /bao-cao/export` **403 `ERR-PERM-SYS-00-01` "Forbidden"**, `auth/me` **200** cả trước lẫn sau cú 403 ⇒ chặn quyền thật · ③ đổi Kỳ → Tháng → 200, tệp `…_20260806_1433.xlsx` **đổi mốc trend theo kỳ mới** (`Tháng 8/2026 · 01/08 · 31/08 · 20 · 0`, đơn vị 13+4+3 = 20) | **Không** |

**Sửa đổi giữa chừng (14:32) — nới vai trò, khai rõ:** toàn bộ tài khoản `CB_NV_TW` (`cbnv_tw`, `_01`,
`_02`, `_03`, `_05`) đều bị một phiên QA khác chiếm liên tục trong ~15 phút (đối chiếu MailHog, chi tiết ở
`VVTTG_01.md`), hệ thống chỉ cho 1 phiên/tài khoản nên mỗi lần bị thu hồi token là mất giữa chừng phép đo.
Vì phép đo này cần **giữ được phiên đủ lâu để bấm nút Xuất và đọc tệp**, đã chuyển sang **`cbpd_tw_01`**.
- Đây là **nới vai trò** (CB Nghiệp vụ → CB Phê duyệt), **không** phải nới cấp/đơn vị: cùng `capDonVi=TW`,
  cùng `donViId=…0001` ⇒ **phạm vi dữ liệu y hệt** (Toàn quốc, đúng như đối tác).
- Nới này **không phá trục chấm**: `:325` liệt kê **cả hai** vai trò là tác nhân hợp lệ của FR-IX-05, nên
  cả hai đều là "vai trò được phép xuất". Vai trò gây tranh cãi (QTHT) vẫn được đo riêng ở dạng ②.
- `cbpd_tw` (không hậu tố) **không đăng nhập được** với `Test@1234` — đây là hiện trạng đã ghi sẵn trong
  `input/input.md` từ 30/07, không phải phát hiện mới của lượt này.

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict.

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- Trạng thái entity: BC đã render, `Tổng vụ việc toàn kỳ = 51`; `Thời điểm tạo: 31/07/2026 14:50`
- Vai trò + env + bản dựng: **QTHT** · `htpldn-uat.ospgroup.vn` · **V1.0** (vòng 1) → **V1.0.3** (vòng 2)

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0/V1.0.3; đợt này đo
trên `18.143.165.120.nip.io` bản ghi ở đầu file ⇒ Pass ở đây là **Pass tạm** cho tới khi bản dựng này lên
env đối tác.
