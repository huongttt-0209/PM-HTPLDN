Mã case: VVDHT_06 (tab `bug` dòng 185)          Thời điểm viết: 2026-08-06 12:38
Môi trường verify: https://18.143.165.120.nip.io          Bản dựng: **V1.0.8** (`HTPLDN · V1.0.8`) — đo 06/08/2026 14:16–14:21

Hồ sơ QA nội bộ đã đọc trước khi viết file này: KHÔNG có (chưa từng qua vòng soát nội bộ).

---

## 1. Đối tác phản ánh

Màn: **BC Vụ việc đang hỗ trợ** (SCR-IX-01, `loai=vu-viec-dang-ho-tro`). **1 vế duy nhất:** bấm
**Xuất Excel** thì không nhận được tệp, hệ thống báo lỗi.

**Bằng chứng đã mở xem:**

| Tệp | Vòng | Thấy gì |
|---|---|---|
| `../partner-evidence/VVDHT_06.jpg` | Vòng 1 — 15/07/2026 | Bản dựng **V1.0**, vai trò **Quản trị viên QTHT**. Thông báo **"Không thể tạo file xuất. Vui lòng thử lại."** |
| `../partner-evidence/VVDHT_06_v2.jpg` | Vòng 2 — 31/07/2026 14:21 | Bản dựng **V1.0.2**, vẫn **QTHT** (BTP·TW). Loại BC `BC Vụ việc đang hỗ trợ`, Kỳ **Năm** 01/01/2026–31/12/2026, Đơn vị **BTP-TW**, NHT phụ trách + Mức SLA để trống. Màn **đã ra dữ liệu**: `Tổng vụ việc = 22`, `Thời điểm tạo: 31/07/2026 14:21`. Thông báo đổi thành **"Forbidden"**. Nút `Xuất Excel` / `Xuất PDF` hiện bình thường, không bị làm mờ. |

**Lệch giữa 2 vòng:** cùng vai trò (QTHT), cùng bộ lọc, **khác bản dựng** (V1.0 → V1.0.2), **khác triệu
chứng** (`ERR-RPT-04` → `Forbidden`) — giống hệt diễn biến của VVDTN_06 và VVTTG_05.

**Ghi chú dev:** cột "DEV phản hồi lần 1" dòng 185 ghi *"Đã kiểm tra trên môi trường DEV nhưng chưa tái
hiện được lỗi; chức năng hiện hoạt động đúng theo thiết kế."* — không khớp triệu chứng vòng 2. Vẫn chạy
đủ luồng, không tin mô tả.

> 🔴 Case này **cùng câu triệu chứng** với VVDTN_06 và VVTTG_05 nhưng **khác màn** ⇒ phải đo riêng trên
> màn BC Vụ việc đang hỗ trợ. Cấm suy kết quả từ case anh em.

---

## 2. Đặc tả nói gì

→ Xem [`_chung-xuat-excel.md` §2](_chung-xuat-excel.md). Riêng màn này: **FR-IX-03 (UC126)**, tác nhân
`srs-fr-11-bao-cao.md:236` = `CB Nghiệp vụ / CB Phê duyệt (TW/BN/ĐP)`; tên báo cáo hiển thị
`:1066` = `BC Vụ việc đang hỗ trợ`. Báo cáo này là **snapshot tại thời điểm query** (`:247`), không phải
tổng hợp theo kỳ như 2 màn kia — nên khi so số liệu tệp ↔ màn phải xuất **ngay sau** khi Xem báo cáo,
tránh dữ liệu đổi giữa 2 thao tác.

---

## 3. Precondition

- Tài khoản ra verdict: **`cbnv_tw` / `Test@1234`** (`CB_NV_TW`, cấp TW).
- Tài khoản đối chứng GAP vai trò: **`admin` / `Secret@123`** (QTHT) — trùng khít vai trò đối tác.
- Màn: `https://18.143.165.120.nip.io/bao-cao` → Loại báo cáo **"BC Vụ việc đang hỗ trợ"**.
- Bộ lọc khớp đối tác: Kỳ **Năm**, 01/01/2026 → 31/12/2026, Đơn vị **BTP-TW**, NHT + Mức SLA để trống.
- Dữ liệu tiền đề: phải có **≥1 vụ việc đang xử lý** trong phạm vi để "Xem báo cáo" ra dữ liệu (nút Xuất
  chỉ dùng được sau đó, `:1052`). Không có thì nới đơn vị / seed vụ việc qua luồng chuẩn rồi khai vào
  báo cáo.

---

## 4. Tiêu chí chấm

→ Dùng nguyên [`_chung-xuat-excel.md` §4](_chung-xuat-excel.md), đo trên **màn BC Vụ việc đang hỗ trợ**.
Cụ thể hoá 2 chỗ:

- Tiêu chí 3 (số khớp màn): tổng phải khớp là ô **`Tổng vụ việc`** của màn này; ngoài ra nếu màn có phân
  rã theo **mức SLA** và theo **người hỗ trợ** (`:257`–`:262`) thì các con số đó cũng phải có trong tệp.
- Tiêu chí 5 (tên tệp): khuôn `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` với `{TenBaoCao}` suy theo `:86` từ tên
  `BC Vụ việc đang hỗ trợ`. Chấm theo **khuôn**, không theo chuỗi tự nghĩ.

---

## 5. Dạng dữ liệu phải phủ

→ Dùng nguyên [`_chung-xuat-excel.md` §5](_chung-xuat-excel.md) — **M = 3**:
① `cbnv_tw` + kỳ có dữ liệu · ② `admin` (QTHT) + kỳ có dữ liệu · ③ `cbnv_tw` + đổi bộ lọc.
Dạng ③ trên màn này = đặt thêm bộ lọc **Mức SLA** (hoặc **NHT phụ trách**) rồi xuất lại, so nội dung 2
tệp — đây cũng là phép thử tiêu chí 4 (tệp áp đúng bộ lọc hiện tại).

---

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **Quản trị viên QTHT** (`BTP · TW`) ở cả 2 vòng — KHÔNG thuộc tác nhân FR-IX-03 (`:236`) | Đo **cả hai**: ① `cbnv_tw` → giữa chừng bị đá phiên (phiên khác đăng nhập cùng tài khoản, xem mục "Sửa đổi giữa chừng"), tiếp bằng **`cbnv_tw_03`** — cùng `CB_NV_TW`, cùng `donViId=…0001` (BTP-TW), xác nhận qua `auth/me` ⇒ scope y hệt · ② **`admin` (QTHT)** — **trùng khít vai trò đối tác**, đo trên chính giao diện, bấm nút Xuất thật | **Không** |
| Entity + trạng thái | VU_VIEC **đang xử lý** — snapshot tại thời điểm query (`:247`). Báo cáo đã render xong rồi mới bấm Xuất | Cùng loại + cùng thứ tự thao tác: Xem báo cáo ra dữ liệu (`Thời điểm tạo 06/08/2026 14:16` cho CB NV, `14:21` cho QTHT) **rồi mới** bấm Xuất | **Không** |
| Dữ liệu tiền đề | Kỳ CÓ dữ liệu: `Tổng vụ việc = 22` (31/07 14:21) | Kỳ CÓ dữ liệu: `Tổng vụ việc = **14**` (BTP-TW, cả 2 vai trò ra cùng con số) — ít hơn 22 của đối tác vì khác env/thời điểm, nhưng **cùng bản chất** (≥1 vụ việc ⇒ nút Xuất dùng được) | **Không** |
| Input / filter / giá trị nhập | Kỳ `NAM`, `tuNgay=2026-01-01`, `denNgay=2026-12-31`, `donViId=00000000-0000-4000-8000-000000000001` (BTP-TW); NHT phụ trách + Mức SLA để trống. Định dạng xuất: **Excel** | Giữ nguyên toàn bộ bộ lọc của đối tác cho dạng ① và ②; dạng ③ thêm **Mức SLA = Quá hạn** (`fd_mucSla=QUA_HAN`). Định dạng xuất: **Excel** | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 22 vụ việc · đối tác chỉ đo **1 dạng** (QTHT + 1 bộ lọc), không đổi vai trò, không đặt bộ lọc đặc thù | Phủ đủ **M = 3**: ① `cbnv_tw` BTP-TW → HTTP 200, tệp `BaoCaoVuViecDangHoTro_20260806_1417.xlsx` **mở đọc được**, đủ 4 dòng tiêu đề, số khớp màn từng con số (14 · SLA 12/0/2/0 · NHT `QA TVV Seed28 Active` 4/2) · ② `admin` QTHT → Xem báo cáo **200** (14) nhưng `POST /bao-cao/export` **403 `ERR-PERM-SYS-00-01` "Forbidden"**, `auth/me` ngay sau đó **200** ⇒ chặn quyền thật, không phải hết phiên · ③ `cbnv_tw_03` + Mức SLA=Quá hạn → 200, tệp `…_20260806_1419.xlsx` **bám đúng bộ lọc mới** (tổng 2, SLA 0/0/2/0, NHT 2/2) | **Không** |

**Sửa đổi giữa chừng (14:19):** đang đo dạng ③ bằng `cbnv_tw` thì bị đá về `/login` với thông báo
"Phiên làm việc hết hạn". Nguyên nhân khách quan: MailHog cho thấy **phiên QA khác đăng nhập cùng tài
khoản `cbnv_tw`** lúc 07:17:51 và 07:18:22 UTC (mã OTP không phải của mình), hệ thống chỉ cho 1 phiên/tài
khoản. Theo Rule 7 (fallback **giữ nguyên vai trò**, chỉ đổi tài khoản anh em cùng cấp + cùng đơn vị) đã
chuyển sang **`cbnv_tw_03`**; xác nhận `auth/me` trả `vaiTro=["CB_NV_TW"]`, `donViId=…0001`, `capDonVi=TW`
⇒ **cùng scope dữ liệu**, không phải nới cấp/đơn vị. Dạng ① đã đo xong bằng `cbnv_tw` trước khi bị đá.

**Đóng GAP:** 5/5 dòng đã điền, không còn GAP ⇒ được ra verdict.

**Phát hiện mới trên chính màn này, KHÔNG kéo verdict case** (xử riêng theo §Phát hiện mới):
① Trong tệp Excel, mục **"Theo đơn vị"** chỉ có dòng tiêu đề, **không có dữ liệu** — API trả `theoDonVi: []`
trong khi `:262` quy định `theo_don_vi[]` điều kiện **"Luôn"**.
> **Thu hẹp phạm vi 14:42 (đo lại):** lỗi này **chỉ xảy ra khi lọc đúng một đơn vị**. Ở phạm vi **Toàn quốc**
> API trả đủ 4 đơn vị (16/3/2/1) và màn hiện đủ bảng. Vậy mô tả đúng phải là "chọn 1 đơn vị thì mục Theo đơn vị
> bị rỗng", không phải "luôn rỗng" như tôi ghi lúc đầu.

**3 dữ kiện neo của đối tác:**
- URL/ID bản ghi: `htpldn-uat.ospgroup.vn/bao-cao?loai=vu-viec-dang-ho-tro&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31&donViId=00000000-0000-4000-8000-000000000001`
- Trạng thái entity: BC đã render, `Tổng vụ việc = 22`; `Thời điểm tạo` 31/07/2026 14:21 (vòng 2)
- Vai trò + env + bản dựng: **QTHT** · `htpldn-uat.ospgroup.vn` · **V1.0** (vòng 1) → **V1.0.2** (vòng 2)

**Giới hạn hiệu lực (không phải GAP):** đối tác đo trên `htpldn-uat.ospgroup.vn` V1.0/V1.0.2; đợt này đo
trên `18.143.165.120.nip.io` bản ghi ở đầu file ⇒ Pass ở đây là **Pass tạm** cho tới khi bản dựng này lên
env đối tác.
