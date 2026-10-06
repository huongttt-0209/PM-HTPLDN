# BA confirmation needed — Báo cáo thống kê vụ việc (B1: 6 case / 3 màn) — 2026-08-06

> **⚠️ File này là bản ghi gốc của lô, KHÔNG phải bản gửi BA.**
> Bản gửi BA là [`cau-hoi-BA-tong-hop-2026-08-06.md`](../../reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md) — `VVDTN_04` → **Mục 1**.
> **Đã xoá khỏi bản gộp vì trùng câu đã gửi:** `VVDTN_06` · `VVDHT_06` · `VVTTG_05` (cùng câu hỏi quyền xuất tệp của vai trò QTHT) — BA trả lời một lần ở [`cau-hoi-BA.md`](../../reverify-week-5/ba-confirm/cau-hoi-BA.md).

> Đợt verify bug đối tác báo dev đã fix, tab `bug` bảng làm việc. Môi trường verify
> `https://18.143.165.120.nip.io` bản dựng **V1.0.8** (đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0 → V1.0.3).
> Hồ sơ tiêu chí từng case: [`../tieuchi/`](../tieuchi). Ảnh: [`../bug-reports/image/`](../bug-reports/image).

---

## VVDTN_04 — Biểu đồ tròn theo lĩnh vực trên "BC Vụ việc đã tiếp nhận"

**Bối cảnh testcase**

- Dòng Excel: 178, mã TC `VVDTN_04`.
- Nội dung kiểm tra: vai trò **Quản trị viên QTHT** mở màn Báo cáo thống kê → loại BC **"BC Vụ việc đã tiếp nhận"**,
  Kỳ `Năm` 01/01/2026–31/12/2026, Đơn vị `Cục Bổ trợ tư pháp – BTP·TW`.
- Expected trong file UAT — đối tác nêu **2 vế**:
  - **(a)** phải hiển thị **biểu đồ tròn** theo lĩnh vực;
  - **(b)** bảng tổng hợp **thiếu các cột: Theo kênh, Theo lĩnh vực**.
- Actual đối tác ghi: chỉ thấy biểu đồ cột theo kênh + biểu đồ đường theo thời gian, không có vùng nào theo lĩnh vực.

**Đối chiếu SRS v3.5**

- Về **dữ liệu**: FR-IX-02 (UC125) khai `theo_kenh[]` và `theo_linh_vuc[]` là output điều kiện **"Luôn"** — tức
  hai chiều này bắt buộc phải có trong mọi lần tạo báo cáo. Vế (b) của đối tác **có cơ sở đặc tả**.
- Về **dạng biểu đồ**: bảng "Mapping 23 loại BC" của SCR-IX-01 gán cho UC125 dạng **"Bar + Trend"**. Cùng bảng đó
  gán `Donut + Trend` cho UC124 và `Bar + Donut` cho UC127 ⇒ đặc tả **có** khái niệm biểu đồ tròn và **cố ý không**
  gán cho UC125. Đây không phải chỗ đặc tả im lặng.
- Đặc tả **im lặng** về: chiều lĩnh vực phải trình bày bằng *biểu đồ* hay bằng *bảng* — chỉ đòi có dữ liệu.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:214` — `| 2 | theo_kenh[] | structured | Luôn | {kenh, so_luong} |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:215` — `| 3 | theo_linh_vuc[] | structured | Luôn | {linh_vuc, ten, so_luong} |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1065` — `| **Vụ việc** | UC125 | BC Vụ việc đã tiếp nhận | Kênh tiếp nhận, Lĩnh vực PL | **Bar + Trend** |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1064` / `:1067` — UC124 `Donut + Trend`, UC127 `Bar + Donut` (đối chứng: Donut được gán có chủ đích cho UC khác)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:203` — công thức FR-IX-02 "Đếm số vụ việc đã tiếp nhận (trừ từ chối)"

**Kết quả verify UI hiện tại**

- Verify 06/08/2026 12:51–13:12 qua Chrome DevTools MCP, bản dựng **V1.0.8**, tài khoản `cbnv_tw` (`CB_NV_TW` — đúng
  tác nhân `:192`); đối chứng thêm chính vai trò đối tác `admin`/**QTHT** qua API.
- URL: `https://18.143.165.120.nip.io/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`
- **Vế (b) — không còn tái hiện.** Màn hiện đủ cả hai chiều:
  - Bảng **"Kênh tiếp nhận / Số lượng"**: Trực tiếp 41 · Doanh nghiệp 3 (lọc Toàn quốc).
  - Bảng **"Thống kê theo lĩnh vực pháp luật"**: Thương mại 16 · Dân sự 13 · Lao động 12 · Thuế 3, kèm cột Tỷ lệ.
  - Cả hai chiều **cộng khớp** tổng 44; đối chiếu đường thứ hai `GET /api/v1/vu-viecs` (45 bản ghi − 1 `TU_CHOI`
    = 44, đúng công thức `:203`) ra **y hệt** từng con số ⇒ số liệu đúng, không phải trùng/thiếu.
  - Vai trò QTHT của đối tác gọi `GET /api/v1/bao-cao/vu-viec-tiep-nhan` cũng nhận đủ `theoKenh` + `theoLinhVuc`.
- **Vế (a) — hiện trạng: không có biểu đồ tròn.** Màn render đúng 2 biểu đồ: **cột** theo kênh tiếp nhận và
  **đường xu hướng** theo kỳ — khớp `Bar + Trend` của `:1065`. Chiều lĩnh vực được trình bày bằng **bảng**, không
  phải biểu đồ tròn.
- **Đo lại 06/08/2026 13:36 bằng CHÍNH vai trò đối tác (`admin` / Quản trị hệ thống, BTP·TW), đúng bộ lọc đối tác** —
  kết quả **không khác**: `Tổng vụ việc = 34`; bảng "Kênh tiếp nhận" (Trực tiếp 34); bảng "Thống kê theo lĩnh vực
  pháp luật" (Dân sự 13 · Lao động 9 · Thương mại 9 · Thuế 3 = 34, có cột Tỷ lệ); hai biểu đồ là **cột** theo kênh
  và **đường** theo kỳ, **không có biểu đồ tròn**. Vai trò không làm đổi kết luận của cả hai vế.
- Evidence:
  - `../bug-reports/image/VVDTN_04-04-QTHT-bieu-do-cot-va-duong-khong-co-tron.png` — **vai trò QTHT**, tổng 34, biểu đồ cột + đường
  - `../bug-reports/image/VVDTN_04-05-QTHT-bang-kenh-va-bang-linh-vuc.png` — **vai trò QTHT**, bảng kênh + bảng lĩnh vực
  - `../bug-reports/image/VVDTN_04-01-btptw-bang-kenh-va-linhvuc.png` — bảng theo kênh + bảng theo lĩnh vực (CB Nghiệp vụ)
  - `../bug-reports/image/VVDTN_04-02-btptw-tong-va-bieu-do-cot-theo-kenh.png` — tổng, thời điểm tạo, biểu đồ cột theo kênh
  - `../bug-reports/image/VVDTN_04-03-toanquoc-2kenh-4linhvuc-4donvi.png` — đủ 2 kênh có dữ liệu

**Kết luận QA**

- **Vế (b) không còn là lỗi trên bản V1.0.8**: hai chiều "theo kênh" và "theo lĩnh vực" đều hiển thị được và số
  liệu khớp hai đường đo độc lập. (Đặc tả không quy định nhãn cột phải đúng chữ "Theo kênh"/"Theo lĩnh vực", nên
  không chấm lỗi vì tên cột.)
- **Vế (a) QA không tự chốt được — kỳ vọng đối tác ngược với đặc tả nói rõ.** Đối tác đòi biểu đồ tròn; `:1065`
  chốt UC125 = Bar + Trend. QA không tự bác đối tác nên không chấm Pass/Fail vế này.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt 1 trong 2 hướng cho `VVDTN_04`:

- **Hướng 1 — giữ đặc tả:** trả lời đối tác rằng UC125 theo thiết kế chỉ có **Bar + Trend**; chiều lĩnh vực đã
  được trình bày bằng **bảng có cột Tỷ lệ**, đủ thông tin. Khi đó cập nhật lại expected của `VVDTN_04` và đóng case.
- **Hướng 2 — đổi đặc tả:** nếu nghiệp vụ thực sự cần biểu đồ tròn theo lĩnh vực, cần sửa `:1065` (UC125 →
  `Bar + Donut + Trend` hoặc tương đương) rồi mới giao Dev FE bổ sung.
- Verdict QA đề xuất: **Cần BA xác nhận** (vế a), **không gửi Dev** cho tới khi có hướng chốt. Vế (b) không gửi Dev.

---

## VVDTN_06 — Vai trò QTHT **xem được** báo cáo nhưng **không xuất được** tệp

**Bối cảnh testcase**

- Dòng Excel: 179, mã TC `VVDTN_06`.
- Nội dung kiểm tra: vai trò **Quản trị viên QTHT** mở "BC Vụ việc đã tiếp nhận", Kỳ `Năm` 01/01/2026–31/12/2026,
  Đơn vị `Cục Bổ trợ tư pháp – BTP·TW`, bấm **Xuất Excel**.
- Expected trong file UAT: tải được tệp .xlsx.
- Actual đối tác ghi: vòng 1 (15/07, V1.0) báo *"Không thể tạo file xuất. Vui lòng thử lại."*; vòng 2 (31/07, V1.0.2)
  báo **"Forbidden"**. Ghi chú của Dev: *"Đã kiểm tra trên môi trường DEV nhưng chưa tái hiện được lỗi; chức năng
  hiện hoạt động đúng theo thiết kế."*

**Kết quả verify UI hiện tại**

- Verify 06/08/2026 qua Chrome DevTools MCP + gọi API trực tiếp, bản dựng **V1.0.8**.
- **Với `cbnv_tw` (CB Nghiệp vụ TW — đúng tác nhân `:192`): xuất được bình thường.** Bấm nút thật trên UI →
  `POST /api/v1/bao-cao/export` **200**, tệp `BaoCaoVuViecTiepNhan_20260806_1254.xlsx` tải về, **mở đọc được**,
  nội dung khớp màn từng con số và bám đúng bộ lọc khi đổi bộ lọc.
- **Với `admin` (QTHT — đúng vai trò đối tác dùng): tái hiện y hệt triệu chứng vòng 2.**
  Đo bằng **đúng đường người dùng đi**: đăng nhập giao diện bằng `admin`, mở màn Báo cáo thống kê, đặt đúng bộ lọc
  đối tác, bấm **Xem báo cáo** rồi bấm chính nút **Xuất Excel** (13:39 ngày 06/08/2026).
  - Xem báo cáo → **200/304**, `Tổng vụ việc = 34`, `Thời điểm tạo 06/08/2026 13:39`.
  - Bấm nút Xuất Excel → `POST /api/v1/bao-cao/export` **403**; token gửi kèm giải mã ra `vaiTro: ["QTHT"]`,
    `hoTen: "Quản trị hệ thống"`. Thân phản hồi: `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}`.
  - `GET /api/v1/auth/me` **ngay sau** cú 403 → **304** ⇒ **chặn quyền thật**, không phải phiên hết hạn.
  - Nút **Xuất Excel / Xuất PDF hiện bình thường và bấm được** với vai trò QTHT — hệ thống mời thao tác rồi mới chặn;
    thông báo đầu tiên người dùng thấy là **"Đang tạo file..."** (bắt được lúc 06:39:23.182 và .183).
  - *Hạn chế đã biết của lượt đo:* câu thông báo **lỗi cuối cùng** chưa tự chụp được — mã FE dùng cùng `key: "export"`
    nên AntD thay nội dung tại chỗ, và lượt đo lại bị **phiên khác chiếm tài khoản `admin`** nên phải dừng. Không ảnh
    hưởng kết luận: mã phía máy chủ và ảnh vòng 2 của đối tác đều là chữ **"Forbidden"**.
- Evidence: `../bug-reports/image/VVDTN_06-QTHT-bam-nut-that-403.json` (bằng chứng của chính lượt bấm nút),
  `../bug-reports/image/VVDTN_06-01-btptw-co-du-lieu-nhung-nut-xuat-bi-vo-hieu.png`,
  `../bug-reports/image/VVDTN_06-toanquoc-BaoCaoVuViecTiepNhan_20260806_1254.xlsx`,
  `../bug-reports/image/VVDTN_06-loc-truc-tiep-BaoCaoVuViecTiepNhan_20260806_1311.xlsx`.

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo FR-IX-02, **QTHT không phải tác nhân** của báo cáo này:
   - dòng "Tác nhân" chỉ liệt kê CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP).

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:192`

2. Nhưng phần quy tắc nghiệp vụ lại **có tính đến QTHT trong chính nhóm FR-IX**, và tính theo hướng **nới quyền**:
   - `BR-AUTH-08` — chính sách phân quyền dữ liệu, cột "Áp dụng FR" ghi **Toàn bộ FR-IX**, cột "Ngoại lệ" ghi
     **"QTHT bypass"** (QTHT vượt qua giới hạn phạm vi đơn vị, chứ không phải bị cấm).
   - Luồng xử lý chung chỉ có **một** bước kiểm quyền cho cả báo cáo ("Kiểm tra quyền truy cập báo cáo + phạm vi
     theo đơn vị"), không tách quyền *xem* với quyền *xuất*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1268`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:79`

3. Hiện trạng hệ thống **không khớp cả hai cách hiểu**: cho QTHT *xem* (200) nhưng chặn *xuất* (403) cùng một tập
   dữ liệu, và vẫn hiện nút Xuất cho vai trò bị chặn.

**Câu hỏi cần BA xác nhận**

Vai trò **QTHT** có được dùng chức năng Báo cáo thống kê (xem **và** xuất tệp) hay không?

1. **Hướng 1 — QTHT được dùng đầy đủ** (theo `:1268` "QTHT bypass"): Dev BE mở quyền `POST /bao-cao/export` cho
   QTHT. `VVDTN_06` khi đó là **lỗi còn tồn tại**, chuyển lại Dev.
2. **Hướng 2 — QTHT không được dùng** (theo `:192`): phải chặn **nhất quán** — chặn luôn cả `GET` xem báo cáo, ẩn
   hoặc vô hiệu nút Xuất, và trả đúng thông báo `ERR-RPT-05` "Bạn không có quyền xem báo cáo này" thay vì
   "Forbidden". `VVDTN_06` khi đó **không phải lỗi**, nhưng cần trả lời đối tác rằng phải test bằng vai trò
   CB Nghiệp vụ / CB Phê duyệt.

**Đề xuất QA tạm thời**

- Chưa có kết luận của BA thì **không** chuyển `VVDTN_06` cho Dev, tránh đôi bên hiểu khác nhau về phạm vi vai trò.
- **Độc lập với hướng nào được chọn**, thông báo chặn quyền đang trả `ERR-PERM-SYS-00-01` / "Forbidden" (tiếng Anh,
  mã ngoài bộ mã báo cáo) là trái `srs-fr-11-bao-cao.md:117` — đã tách thành dòng lỗi riêng `VVDTN_QA01`.
- Cần nói rõ với đối tác: các case xuất tệp còn lại (`VVDHT_06`, `VVTTG_05`) cũng được đo bằng **cùng** vai trò
  QTHT nên nhiều khả năng cùng bản chất; kết luận của BA nên áp cho cả nhóm.

---

## VVDHT_06 — cùng câu hỏi vai trò QTHT, đo độc lập trên màn "BC Vụ việc đang hỗ trợ"

**Bối cảnh testcase**

- Dòng Excel: 185, mã TC `VVDHT_06`. Màn **BC Vụ việc đang hỗ trợ** (FR-IX-03 / UC126) — **khác màn** với `VVDTN_06`,
  nên đã đo lại từ đầu chứ không suy kết quả từ case anh em.
- Actual đối tác ghi: vòng 1 (15/07, V1.0) *"Không thể tạo file xuất. Vui lòng thử lại."*; vòng 2 (31/07 14:21, V1.0.2)
  **"Forbidden"**, màn đã ra dữ liệu `Tổng vụ việc = 22`. Ghi chú Dev: *"…chưa tái hiện được lỗi; chức năng hiện hoạt
  động đúng theo thiết kế."*

**Kết quả verify UI hiện tại** (06/08/2026, bản dựng **V1.0.8**)

- **`cbnv_tw` (CB Nghiệp vụ TW — đúng tác nhân `:236`): xuất được bình thường.** Bấm nút thật trên UI →
  `POST /api/v1/bao-cao/export` **200**, `content-disposition` = `BaoCaoVuViecDangHoTro_20260806_1417.xlsx`
  (đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`), tệp **mở đọc được**, đủ 4 dòng tiêu đề (tên BC · kỳ + khoảng
  thời gian · đơn vị · ngày tạo) và số khớp màn **từng con số**: tổng 14 · SLA 12 / 0 / 2 / 0 · NHT
  `QA TVV Seed28 Active` 4 vụ, 2 quá hạn.
- **Đổi bộ lọc rồi xuất lại** (`cbnv_tw_03`, thêm Mức SLA = *Quá hạn*): tệp `…_20260806_1419.xlsx` **bám đúng bộ lọc
  mới** — tổng 2, SLA 0/0/2/0, NHT 2/2. Tức phần thân chức năng xuất chạy đúng.
- **`admin` (QTHT — đúng vai trò đối tác dùng): tái hiện y hệt triệu chứng vòng 2.** Cùng một phiên, cùng bộ lọc:
  - Xem báo cáo → **200**, `Tổng vụ việc = 14`, `Thời điểm tạo 06/08/2026 14:21` — **xem được**.
  - Bấm chính nút **Xuất Excel** → `POST /api/v1/bao-cao/export` **403**,
    thân phản hồi `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}`; token gửi kèm giải mã ra `vaiTro: ["QTHT"]`.
  - `GET /api/v1/auth/me` **ngay sau** cú 403 → **200** ⇒ **chặn quyền thật**, không phải phiên hết hạn.
  - Lần này **bắt được trọn chuỗi thông báo** trên giao diện: *"Đang tạo file..."* → **"Forbidden"**
    (ảnh `../bug-reports/image/VVDHT_06-02-QTHT-xuat-excel-bao-Forbidden.png` chụp đúng lúc toast còn hiện,
    trên nền màn đã có dữ liệu 14). Đây là bằng chứng UI mà lượt đo `VVDTN_06` còn thiếu.
  - Nút Xuất Excel / Xuất PDF **hiện bình thường và bấm được** với vai trò QTHT.
- Evidence: `../bug-reports/image/VVDHT_06-QTHT-export-403.json`,
  `../bug-reports/image/VVDHT_06-02-QTHT-xuat-excel-bao-Forbidden.png`,
  `../bug-reports/image/VVDHT_06-01-cbnv_tw-man-bao-cao-truoc-khi-xuat.png`,
  `../bug-reports/image/VVDHT_06-cbnv_tw-BaoCaoVuViecDangHoTro_20260806_1417.xlsx`,
  `../bug-reports/image/VVDHT_06-loc-quahan-BaoCaoVuViecDangHoTro_20260806_1419.xlsx`.

**Điểm mâu thuẫn trong SRS v3.5** — **giống hệt** `VVDTN_06`, chỉ đổi số dòng "Tác nhân":

- FR-IX-03 dòng "Tác nhân" chỉ liệt kê CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP), **không có QTHT** —
  `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:236`.
- `BR-AUTH-08` áp **Toàn bộ FR-IX** với ngoại lệ **"QTHT bypass"** — `…srs-fr-11-bao-cao.md:1268`.
- Luồng xử lý chỉ có **một** bước kiểm quyền chung cho cả xem lẫn xuất — `…srs-fr-11-bao-cao.md:79`.
- Hiện trạng cho *xem* (200) mà chặn *xuất* (403) trên cùng tập dữ liệu ⇒ **không khớp cách hiểu nào**.

**Câu hỏi cần BA xác nhận**

Giống câu hỏi ở mục `VVDTN_06` — đây là **một** quyết định phạm vi vai trò áp cho **cả nhóm báo cáo**, không phải
2 quyết định riêng. Hai hướng xử lý và hệ quả với testcase y như mục trên.

**Đề xuất QA tạm thời**

- Chưa có kết luận BA thì **không** chuyển `VVDHT_06` cho Dev.
- Lượt đo này **loại trừ được** giả thuyết "chức năng xuất của màn này hỏng": cùng màn, cùng bộ lọc, chỉ đổi vai trò
  thì kết quả đảo chiều 200 ↔ 403 ⇒ vấn đề nằm ở **phạm vi vai trò**, không phải ở luồng tạo tệp.
- Vì sao Dev không tái hiện được: nhiều khả năng Dev test bằng vai trò CB Nghiệp vụ (luồng đó chạy tốt), còn đối tác
  test bằng QTHT.

---

## VVTTG_05 — cùng câu hỏi vai trò QTHT, đo độc lập trên màn "BC Vụ việc theo thời gian"

**Bối cảnh testcase**

- Dòng Excel: 195, mã TC `VVTTG_05`. Màn **BC Vụ việc theo thời gian** (FR-IX-05 / UC128) — màn thứ ba, đã đo lại
  từ đầu chứ không suy từ `VVDTN_06` / `VVDHT_06`.
- Actual đối tác ghi: vòng 1 (15/07, V1.0) *"Không thể tạo file xuất. Vui lòng thử lại."*; vòng 2 (31/07 14:50,
  **V1.0.3**) **"Forbidden"**, màn đã ra dữ liệu `Tổng vụ việc toàn kỳ = 51`.

**Kết quả verify UI hiện tại** (06/08/2026, bản dựng **V1.0.8**)

- **`cbpd_tw_01` (CB Phê duyệt TW — thuộc tác nhân `:325`): xuất được bình thường.** `POST /bao-cao/export` **200**,
  `content-disposition` = `BaoCaoVuViecTheoThoiGian_20260806_1432.xlsx` (đúng khuôn), tệp **mở đọc được**, có đủ
  bảng **"Theo kỳ"** (`Năm 2026 | 01/01/2026 | 31/12/2026 | Tiếp nhận 50 | Hoàn thành 18`) — tức tệp giữ được
  **từng mốc thời gian** đúng yêu cầu `:337` — và bảng **"Theo đơn vị"** (6+5+36+3 = 50), khớp màn từng con số.
- **Đổi Kỳ Năm → Tháng rồi xuất lại**: tệp `…_20260806_1433.xlsx` **đổi mốc trend theo kỳ mới**
  (`Tháng 8/2026 | 01/08 | 31/08 | 20 | 0`, đơn vị 13+4+3 = 20). Phần thân chức năng xuất chạy đúng.
- **`admin` (QTHT — đúng vai trò đối tác dùng): tái hiện y hệt triệu chứng vòng 2.** Cùng phiên, cùng bộ lọc:
  - Xem báo cáo → **200**, `Tổng vụ việc toàn kỳ = 50`, `Thời điểm tạo 06/08/2026 14:34`.
  - Bấm chính nút **Xuất Excel** → `POST /bao-cao/export` **403**,
    `{"code":"ERR-PERM-SYS-00-01","message":"Forbidden"}`.
  - `GET /auth/me` **200 cả trước lẫn sau** cú 403 ⇒ chặn quyền thật, không phải phiên hết hạn.
  - Bắt được trọn chuỗi thông báo trên giao diện: *"Đang tạo file..."* → **"Forbidden"**
    (ảnh `../bug-reports/image/VVTTG_05-01-QTHT-xuat-excel-bao-Forbidden.png`, nền màn đang có dữ liệu 50).
- Evidence: `../bug-reports/image/VVTTG_05-QTHT-export-403.json`,
  `../bug-reports/image/VVTTG_05-01-QTHT-xuat-excel-bao-Forbidden.png`,
  `../bug-reports/image/VVTTG_05-nam-BaoCaoVuViecTheoThoiGian_20260806_1432.xlsx`,
  `../bug-reports/image/VVTTG_05-thang8-BaoCaoVuViecTheoThoiGian_20260806_1433.xlsx`.

**Điểm mâu thuẫn trong SRS v3.5** — giống hai mục trên, chỉ đổi số dòng "Tác nhân":
`…srs-fr-11-bao-cao.md:325` (không có QTHT) vs `:1268` BR-AUTH-08 "QTHT bypass" áp **Toàn bộ FR-IX** vs `:79`
(một bước kiểm quyền chung cho cả xem lẫn xuất).

**Câu hỏi cần BA xác nhận**

Giống mục `VVDTN_06`. **Ba case xuất tệp (`VVDTN_06`, `VVDHT_06`, `VVTTG_05`) đã được đo độc lập trên ba màn
khác nhau và cho kết quả GIỐNG HỆT nhau** — cùng vai trò đúng tác nhân thì xuất được, cùng vai trò QTHT thì
403 "Forbidden". Đây là **một** quyết định phạm vi vai trò, không phải ba.

**Đề xuất QA tạm thời**

- Chưa có kết luận BA thì **không** chuyển 3 case này cho Dev.
- Nếu BA chọn Hướng 1 (QTHT được dùng đầy đủ) → cả 3 case là lỗi còn tồn tại, sửa **một** chỗ ở tầng phân quyền
  `POST /bao-cao/export` là đóng cả 3.
- Nếu BA chọn Hướng 2 (QTHT không được dùng) → cả 3 case không phải lỗi, nhưng phải chặn **nhất quán** (chặn cả
  `GET`, ẩn/vô hiệu nút Xuất, đổi thông báo theo `:117`) và trả lời đối tác rằng phải test bằng CB Nghiệp vụ /
  CB Phê duyệt.
