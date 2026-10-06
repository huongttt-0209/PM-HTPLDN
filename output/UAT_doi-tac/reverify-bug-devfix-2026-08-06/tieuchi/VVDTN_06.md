Mã case: VVDTN_06 (tab `bug` dòng 179)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (`HTPLDN · V1.0.8`;
gói `assets/index-CNwX9JjX.js`) — đo 06/08/2026 12:54–13:12

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có (chưa từng qua vòng soát nội bộ).

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc đã tiếp nhận** (SCR-IX-01, `loai=vu-viec-tiep-nhan`). **1 vế duy nhất:** bấm
**Xuất Excel** thì không nhận được tệp, hệ thống báo lỗi.

**Bằng chứng đã mở xem:**

| Tệp | Vòng | Thấy gì |
|---|---|---|
| `../partner-evidence/VVDTN_06.jpg` | Vòng 1 — 15/07/2026 16:39 | Bản dựng **V1.0**, vai trò **Quản trị viên QTHT** (BTP·TW). Màn đã "Xem báo cáo" xong (`Tổng vụ việc = 27`, `Thời điểm tạo: 15/07/2026 16:39`). Lớp thông báo đỏ giữa đầu trang: **"Không thể tạo file xuất. Vui lòng thử lại."** Nút `Xuất Excel` + `Xuất PDF` đang hiện, không bị làm mờ. |
| `../partner-evidence/VVDTN_06_v2.jpg` | Vòng 2 — 31/07/2026 14:09 | Bản dựng **V1.0.2**, vẫn vai trò **QTHT**, cùng bộ lọc. Thông báo đổi thành **"Forbidden"** (chữ tiếng Anh, không dấu). Màn vẫn ra dữ liệu `Tổng vụ việc = 27`, `Thời điểm tạo: 31/07/2026 14:06`. |

**Lệch giữa 2 vòng:** cùng vai trò (QTHT), cùng bộ lọc, **khác bản dựng** (V1.0 → V1.0.2) và **khác hẳn
triệu chứng** (`ERR-RPT-04` "Không thể tạo file xuất" → `Forbidden`). ⇒ Dev có đụng vào luồng này; triệu
chứng mới nghiêng về **chặn quyền**, mà vai trò đối tác dùng (QTHT) vốn **không** thuộc tác nhân FR-IX-02.
Đây chính là lý do mục 5 bắt buộc đo **cả 2 vai trò**.

**Ghi chú dev:** cột "DEV phản hồi lần 1" dòng 179 ghi *"Đã kiểm tra trên môi trường DEV nhưng chưa tái
hiện được lỗi; chức năng hiện hoạt động đúng theo thiết kế."* — mô tả này **không** khớp triệu chứng vòng
2 (Forbidden). Vẫn chạy đủ luồng, không tin mô tả.

---

## 2. Đặc tả nói gì

→ Xem [`_chung-xuat-excel.md` §2](_chung-xuat-excel.md). Riêng màn này: **FR-IX-02 (UC125)**, tác nhân
`srs-fr-11-bao-cao.md:192` = `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`; tên báo cáo hiển thị
`:1065` = `BC Vụ việc đã tiếp nhận`.

---

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw` / `Test@1234`** (`CB_NV_TW`, cấp TW).
- Tài khoản đối chứng GAP vai trò: **`admin` / `Secret@123`** (QTHT) — trùng khít vai trò đối tác.
- Màn: `https://18.143.165.120.nip.io/bao-cao` → Loại báo cáo **"BC Vụ việc đã tiếp nhận"**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **Cục Bổ trợ tư pháp – BTP-TW**.
- Dữ liệu tiền đề: kỳ đã chọn phải **có** dữ liệu (đã bấm "Xem báo cáo" ra bảng/biểu đồ) — nút Xuất chỉ
  hiện sau khi Xem báo cáo (`:1052`). Không có dữ liệu thì đổi khoảng/đơn vị cho tới khi có, rồi mới đo.

---

## 4. Tiêu chí chấm

→ Dùng nguyên [`_chung-xuat-excel.md` §4](_chung-xuat-excel.md), đo trên **màn BC Vụ việc đã tiếp nhận**.
Cụ thể hoá 2 chỗ:

- Tiêu chí 3 (số khớp màn): tổng phải khớp là ô **`Tổng vụ việc`** của màn này.
- Tiêu chí 5 (tên tệp): `{TenBaoCao}` suy từ `:86` cho tên `BC Vụ việc đã tiếp nhận` → chuỗi PascalCase
  không dấu, không ký tự đặc biệt. **Chấm theo khuôn** `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx`, không chấm
  theo một chuỗi tự nghĩ ra.

---

## 5. Dạng dữ liệu phải phủ

→ Dùng nguyên [`_chung-xuat-excel.md` §5](_chung-xuat-excel.md) — **M = 3**:
① `cbnv_tw` + kỳ có dữ liệu · ② `admin` (QTHT) + kỳ có dữ liệu · ③ `cbnv_tw` + đổi bộ lọc.
Dạng ③ trên màn này = đổi **Đơn vị** (BTP-TW → Toàn quốc) hoặc đổi khoảng thời gian, rồi xuất lại và so
nội dung 2 tệp.

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên QTHT** (`BTP · TW`) ở cả 2 vòng — KHÔNG thuộc tác nhân FR-IX-02 (`:192`) | Đo **cả 2 vai trò**: ① `cbnv_tw` (đúng tác nhân) bấm nút thật trên UI → `POST /api/v1/bao-cao/export` **200**, tệp tải về và mở đọc được; ② `admin` (**QTHT**, trùng khít đối tác) — **đăng nhập UI và bấm chính nút "Xuất Excel"** (không phải chỉ gọi API): `POST /api/v1/bao-cao/export` **403**, token gửi kèm giải mã ra `vaiTro:["QTHT"]`; cùng phiên đó `GET /bao-cao/vu-viec-tiep-nhan` = 200/304 (tổng 34). Chốt kiểm `GET /auth/me` = 304 **ngay sau** cú 403 ⇒ chặn quyền thật, không phải bị đá phiên. Artifact `../bug-reports/image/VVDTN_06-QTHT-bam-nut-that-403.json` | **Không** — đã đo đúng vai trò đối tác, đúng đường người dùng đi |
| Entity + trạng thái | VU_VIEC đã tiếp nhận, chỉ bản ghi đã duyệt (`:82`). Báo cáo đã render xong rồi mới bấm Xuất | Giống đối tác: cả 2 vai trò đều "Xem báo cáo" ra dữ liệu xong mới xuất. Với `cbnv_tw` có ảnh màn kèm `Thời điểm tạo` trước lúc bấm | **Không** |
| Dữ liệu tiền đề | Kỳ CÓ dữ liệu: `Tổng vụ việc = 27` ở cả 2 vòng | Kỳ CÓ dữ liệu ở mọi lượt đo: **44** (Toàn quốc) · **34** (BTP-TW, đúng bộ lọc đối tác) · **41** (Toàn quốc + kênh Trực tiếp) | **Không** — khác con số nhưng đều thoả tiền đề "kỳ có dữ liệu" |
| Input / filter / giá trị nhập | Kỳ `NAM`, `tuNgay=2026-01-01`, `denNgay=2026-12-31`, `donViId=00000000-0000-4000-8000-000000000001` (BTP-TW); Kênh tiếp nhận + Lĩnh vực PL để trống. Định dạng xuất: **Excel** | Đo **3 bộ lọc**, đều `formatXuat=XLSX`: ① Toàn quốc · ② BTP-TW (trùng khít đối tác) · ③ Toàn quốc + `kenhTiepNhan=TRUC_TIEP`. **Không đo PDF** — đối tác chỉ nêu "Xuất Excel", ngoài vế đối tác nêu | **Không** — biến thể duy nhất đối tác dùng (XLSX) đã phủ, cộng 2 bộ lọc khác |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 27 vụ việc · đối tác chỉ đo **1 dạng** (QTHT + 1 bộ lọc), không đổi vai trò, không đổi bộ lọc | Đủ **M = 3** dạng của mục 5: ① `cbnv_tw` + kỳ có dữ liệu → xuất được, **mở đọc nội dung** khớp màn · ② QTHT + kỳ có dữ liệu → **403** · ③ `cbnv_tw` + đổi bộ lọc → tệp bám đúng bộ lọc mới | **Không** |

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict.

**Kết quả đo nội dung tệp (tiêu chí 1–5 của [`_chung-xuat-excel.md` §4](_chung-xuat-excel.md)) — vai trò `cbnv_tw`:**

| # | Tiêu chí | Kết quả |
|:-:|---|---|
| 1 | Tệp thật sự tải về | ✅ `POST /bao-cao/export` 200, `content-type` = `…spreadsheetml.sheet` |
| 2 | Mở đọc được + đủ tiêu đề/kỳ/khoảng/đơn vị/ngày tạo | ✅ 4 dòng đầu: `BC Vụ việc đã tiếp nhận` · `Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)` · `Đơn vị: Toàn quốc` · `Ngày tạo: 06/08/2026` |
| 3 | Số khớp màn | ✅ Tổng 44 = màn 44; theo kênh 41+3, theo lĩnh vực 16+13+12+3, theo đơn vị 34+3+4+3, theo kỳ 44 — mọi chiều cộng khớp tổng |
| 4 | Áp đúng bộ lọc hiện tại | ✅ Lọc `Trực tiếp` → tệp ra tổng **41**, bảng kênh chỉ còn 1 dòng `Trực tiếp 41`, lĩnh vực 16+13+9+3 = 41 |
| 5 | Tên tệp đúng khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` | ✅ `BaoCaoVuViecTiepNhan_20260806_1254.xlsx` và `…_20260806_1311.xlsx` |

Tệp lưu tại `../bug-reports/image/VVDTN_06-toanquoc-BaoCaoVuViecTiepNhan_20260806_1254.xlsx` và
`../bug-reports/image/VVDTN_06-loc-truc-tiep-BaoCaoVuViecTiepNhan_20260806_1311.xlsx`.

**Phát hiện mới, KHÔNG kéo verdict case này** (xử riêng theo §Phát hiện mới của flow):
`ERR-PERM-SYS-00-01` "Forbidden" trái `:117` (đòi `ERR-RPT-05` "Bạn không có quyền xem báo cáo này");
nút Xuất bị vô hiệu vĩnh viễn sau lần "Xem báo cáo" thứ 2; `theoDonVi: []` khi lọc 1 đơn vị dù `:216` ghi "Luôn".

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-tiep-nhan&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001`
- Trạng thái entity: BC đã render, `Tổng vụ việc = 27`; `Thời điểm tạo` 15/07/2026 16:39 (vòng 1) · 31/07/2026 14:06 (vòng 2)
- Vai trò + env + bản dựng: **QTHT** · `htpldn-uat.ospgroup.vn` · **V1.0** (vòng 1) → **V1.0.2** (vòng 2)

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0/V1.0.2; đợt này đo
trên `18.143.165.120.nip.io` bản ghi ở đầu file ⇒ Pass ở đây là **Pass tạm** cho tới khi bản dựng này lên
env đối tác.
