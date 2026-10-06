# Kiểm kê tiền đề lô F8 — đọc trước khi đo

> Đo **2026-08-07, 11:33 → 11:50 giờ VN**, env nội bộ `https://18.143.165.120.nip.io`.
> Chỉ dùng `curl` / Python — **không mở giao diện**, không gọi Chrome DevTools MCP.
> Chỉ gọi `GET` (trừ ba lượt `POST /auth/login` + `/auth/verify-otp` để lấy phiên).
> **KHÔNG có `POST` / `PATCH` / `DELETE` nghiệp vụ nào được thực hiện — môi trường KHÔNG bị thay đổi.**
>
> 🔴 **Đây là KIỂM KÊ (đang có sẵn dữ liệu gì), KHÔNG phải phép đo hành vi.** Mọi dòng đánh dấu
> **`manh mối`** dưới đây là thứ tình cờ đọc được trong lược đồ/bản ghi, **chưa đối chiếu SRS, chưa
> kết luận đúng/sai**. Quan hệ `MATCH/DIFF/GAP` và verdict thuộc về tác nhân đo, sau khi khóa chuẩn chấm.

---

## 1. Vân tay bản dựng

Gọi `GET /` **3 lượt liên tiếp** (11:33:55 · 11:33:57 · 11:34:00 giờ VN) — **3/3 lượt trả GIỐNG HỆT nhau**
⇒ đã loại trừ khả năng nhiều máy chủ phục vụ bản khác nhau.

| Hạng mục | Giá trị đo được |
|---|---|
| Môi trường | `https://18.143.165.120.nip.io` — env **NỘI BỘ** (không phải `htpldn-uat.ospgroup.vn` của đối tác) |
| **Bó mã FE (định danh bản dựng)** | **`assets/index-eWHwDgt2.js`** · **`assets/index-DVlgOkLg.css`** |
| `GET /` `last-modified` | `Fri, 07 Aug 2026 02:11:03 GMT` = **07/08 09:11:03 giờ VN** |
| `GET /` `etag` | `W/"6a753eb7-428"` |
| Máy chủ web | `nginx/1.27.5` sau `Caddy` (`via: 1.1 Caddy`) |
| BE (`/api/docs-json` → `info`) | `HTPLDN API` · `version 1.0.0` — chuỗi này KHÔNG đổi theo lần deploy ⇒ **không dùng làm vân tay** |
| Đo đầu phiên trinh sát | 11:33:55 → bó mã `index-eWHwDgt2.js` |
| Đo cuối phiên trinh sát | 11:49:54 → **y nguyên** `index-eWHwDgt2.js`, cùng etag, cùng last-modified |

**Đối chiếu với [`BAN-DUNG.md`](../../BAN-DUNG.md):** đây là **bản thứ 6** kể từ chiều 06/08, mới hơn bản #5
(`index-D4Buvu4S.js`, 07/08 02:23 giờ VN) và mới hơn bản #4 (`index-DsMHK7Dp.js`) mà lượt đo
`KTDGKQHT_05` lúc 02:08–02:20 đã dùng.

| # | Bó mã FE | `last-modified` (GMT) | Giờ VN | Ghi chú |
|---|---|---|---|---|
| 4 | `index-DsMHK7Dp.js` | 06 Aug 18:51:25 | 07/08 01:51 | bản mà `KTDGKQHT_05` được đo lần trước |
| 5 | `index-D4Buvu4S.js` | 06 Aug 19:23:01 | 07/08 02:23 | — |
| **6** | **`index-eWHwDgt2.js`** | **07 Aug 02:11:03** | **07/08 09:11** | **bản đang phục vụ lúc trinh sát** |

⚠️ Nhãn `V1.0.x` ở chân thanh bên **không dùng làm định danh** (bản #4 có bó mã mới hơn #3 nhưng nhãn lùi
V1.0.10 → V1.0.9). Mỗi tác nhân đo vẫn phải tự lấy vân tay **đầu và cuối phiên của mình** — nhịp deploy
của env này là vài giờ một bản.

---

## 2. Bộ tài khoản `_03`

Cách lấy phiên (đã kiểm chứng chạy được, giữ nguyên từ lô F5):

```
POST /api/v1/auth/login      {"username":"<u>","password":"Test@1234"}  -> data.otpToken (hạn 300s)
   lấy mã 6 số ở MailHog:  http://18.143.165.120:8025/api/v2/messages?limit=25
POST /api/v1/auth/verify-otp {"otpToken":"…","otpCode":"######"}        -> data.accessToken (Bearer)
```
Script: `/tmp/login.sh <username> [Test@1234]`. Danh tính đọc bằng **`GET /api/v1/auth/me`**
(phản hồi của `verify-otp` **không** kèm khối người dùng).

### ✅ 6/6 tài khoản đăng nhập được — KHÔNG phải fallback sang `_04` / `_05`

| Tài khoản | `hoTen` | `vaiTro` | `capDonVi` | `donViId` | Tên đơn vị |
|---|---|---|---|---|---|
| `cbnv_tw_03` | CB Nghiệp vụ - Trung ương #03 | `CB_NV_TW` | `TW` | `00000000-0000-4000-8000-000000000001` | Cục Bổ trợ tư pháp - Bộ Tư pháp |
| `cbnv_bn_03` | CB Nghiệp vụ - Bộ ngành #03 | `CB_NV_BN` | `BN` | `00000000-0000-4000-8001-000000000001` | Bộ Kế hoạch và Đầu tư |
| `cbnv_dp_03` | CB Nghiệp vụ - Địa phương #03 | `CB_NV_DP` | `DP` | `00000000-0000-4000-8002-000000000006` | Sở Tư pháp An Giang |
| `cbpd_tw_03` | CB Phê duyệt - Trung ương #03 | `CB_PD_TW` | `TW` | `00000000-0000-4000-8000-000000000001` | Cục Bổ trợ tư pháp - Bộ Tư pháp |
| `cbpd_bn_03` | CB Phê duyệt - Bộ ngành #03 | `CB_PD_BN` | `BN` | `00000000-0000-4000-8001-000000000001` | Bộ Kế hoạch và Đầu tư |
| `cbpd_dp_03` | CB Phê duyệt - Địa phương #03 | `CB_PD_DP` | `DP` | `00000000-0000-4000-8002-000000000006` | Sở Tư pháp An Giang |

⚠️ **Giới hạn đăng nhập 5 lượt / 60 giây** — đã chờ ~25s giữa các lượt, 6/6 thành công không lần nào 429.

### Quyền theo vai trò (đọc từ `permissions` của `/auth/me`) — dùng để chọn đúng tác nhân

| Vai trò | Hợp đồng tư vấn | Đợt báo cáo | Điểm danh / khóa học |
|---|---|---|---|
| `CB_NV_TW` (237 quyền) | create · read · update · delete · export | create · read · update · delete · submit · **`tong-hop`** | `read_diem_danh` · `update_diem_danh` · `create_lich_hoc` · `read_khoa_hoc` |
| `CB_NV_BN` (232) | create · read · update · delete · export | read · update · delete · submit · **`gui-tw`** (KHÔNG có `tong-hop`) | `read_diem_danh` · `update_diem_danh` |
| `CB_NV_DP` (232) | create · read · update · delete · export | read · update · delete · submit · **`gui-tw`** (KHÔNG có `tong-hop`) | `read_diem_danh` · `update_diem_danh` |
| `CB_PD_*` (102) | **chỉ** read · export | **chỉ** read · **`approve`** | chỉ `read_diem_danh` · `read_khoa_hoc` · `approve_*` |

⇒ Tác nhân đúng cho từng nhóm phiếu: `QLHDTVVCG_*` → **`cbnv_*_03`** (CB PD không tạo/sửa/xóa được) ·
`THBCTHCT_*` → **`cbnv_tw_03`** (chỉ TW có `tong-hop`) · `TPDBCKQTHCT_02` → **`cbnv_dp_03`** hoặc
`cbnv_bn_03` (cần `submit`) · `KTDGKQHT_05` → **`cbnv_tw_03`** (cần `update_diem_danh` + khóa thuộc TW).

---

## 3. Lược đồ API — `GET /api/docs-json` (không cần xác thực)

549 đường dẫn · 486 lược đồ. Trích 3 nhóm liên quan lô F8.

### 3.1 Hợp đồng tư vấn — tên tài nguyên thật là `hop-dong-tu-vans` (số nhiều)

| Việc | Endpoint | Ghi chú |
|---|---|---|
| Danh sách | `GET /api/v1/hop-dong-tu-vans` | 🔴 xem ràng buộc dưới bảng |
| Chi tiết | `GET /api/v1/hop-dong-tu-vans/{id}` | |
| Tạo | `POST /api/v1/hop-dong-tu-vans` | 201 |
| Sửa | `PATCH /api/v1/hop-dong-tu-vans/{id}` | |
| Xóa | `DELETE /api/v1/hop-dong-tu-vans/{id}` | 204 · có mã 409 |
| Xuất tệp | `POST /api/v1/hop-dong-tu-vans/export` | trả nhị phân, không bọc envelope |
| Sinh mã | `GET /api/v1/hop-dong-tu-vans/ma-preview` | không tham số |
| Mốc tiến độ (hàng loạt) | `POST /api/v1/hop-dong-tu-vans/{id}/moc-tien-dos` | |
| Thanh toán giai đoạn (hàng loạt) | `POST /api/v1/hop-dong-tu-vans/{id}/thanh-toans` | |
| Tệp đính kèm | `POST /{id}/files` · `DELETE /{id}/files/{fileId}` · `GET /{id}/files/{fileId}/download` | |
| Nhật ký thay đổi | `GET /api/v1/hop-dong-tu-vans/{id}/audit-logs` | |

🔴 **Ràng buộc quan trọng nhất của cả nhóm — chép nguyên văn mô tả trong lược đồ:**

> "Trả về danh sách hợp đồng tư vấn theo bộ lọc phân trang. **Bắt buộc truyền ít nhất một trong các tham số
> ngữ cảnh `vuViecId`, `tuVanVienId` hoặc `toChucTuVanId`; nếu thiếu sẽ trả 403** vì hợp đồng chỉ được
> truy cập trong ngữ cảnh vụ việc/tư vấn viên/tổ chức tư vấn."

Đã kiểm bằng `curl` với `cbnv_dp_03`:
```
GET /api/v1/hop-dong-tu-vans   (không tham số)
→ HTTP 403  {"code":"ERR-PERM-SYS-00-01",
             "message":"Hợp đồng tư vấn chỉ truy cập trong ngữ cảnh vụ việc/tư vấn viên/tổ chức."}
```

**Tham số tìm kiếm thật sự tồn tại** (giống hệt cho `GET` danh sách và `POST /export`):

| Tham số | Kiểu | Ghi chú |
|---|---|---|
| `trangThai` | enum | `NHAP` · `DANG_THUC_HIEN` · `TAM_DUNG` · `HOAN_THANH` · `HET_HAN` · `HUY` |
| `tuVanVienId` | uuid | 1 trong 3 tham số ngữ cảnh bắt buộc |
| `toChucTuVanId` | uuid | 1 trong 3 tham số ngữ cảnh bắt buộc |
| `vuViecId` | uuid | 1 trong 3 tham số ngữ cảnh bắt buộc |
| `tuNgay` / `denNgay` | chuỗi | khoảng ngày |
| phân trang | `page` · **`pageSize`** | ⚠️ `limit` / `size` / `perPage` **bị bỏ qua** (đã thử, vẫn trả pageSize 20) |

- **manh mối** — **lược đồ KHÔNG có tham số từ khóa** (`tuKhoa` / `q` / `keyword` / `search`) ở cả danh sách
  lẫn xuất tệp, trong khi phiếu `_03` / `_04` / `_16` nói tới "từ khóa". Chưa đối chiếu SRS ⇒ chưa kết luận;
  cũng có thể FE lọc phía màn hình. Tác nhân đo phải kiểm bằng giao diện thật.

**Tên trường thật của bản ghi hợp đồng** (`CreateHopDongTuVanDto`):

| Nhóm | Trường |
|---|---|
| Thông tin chung | `tenHopDong`* · `soHopDong` · `benA`* · `benB`* · `giaTriHopDong`* · `ngayKy` · `ngayBatDau`* · `ngayKetThuc`* · `noiDung` · `ghiChu` · `trangThai` (enum 6 giá trị ở trên) |
| Bên thực hiện | `tuVanVienId` · `toChucTuVanId` |
| Vụ việc liên kết | **`vuViecIds`** — mảng uuid |
| Mốc tiến độ | **`mocTienDos[]`** = `tenMoc`* · `thuTu`* · `ngayDuKien`* · `ngayThucTe` · `trangThaiMoc` (`CHUA_BAT_DAU` · `DANG_THUC_HIEN` · `HOAN_THANH` · `TRE_HAN`) · `ghiChu` |
| Thanh toán giai đoạn | **`thanhToans[]`** = `giaiDoan`* · `thuTu`* · `soTien`* · `ngayThanhToan` · `trangThaiTt` (`CHUA_THANH_TOAN` · `DA_THANH_TOAN` · `HUY`) · `ghiChu` |
| Tệp đính kèm | không nằm trong DTO tạo — nạp riêng qua `POST /{id}/files` (multipart, trường `file`) |

(*) = bắt buộc. **Không có trường `maHopDong` trong DTO tạo** ⇒ mã do hệ thống sinh (`ma-preview` trả
`{"maHopDong":"HDTV-20260807-0001"}`).

- **manh mối** — mô tả `POST /export` trong lược đồ ghi tên tệp là **`HdtvDanhSach_{YYYYMMDD_HHmm}.xlsx`**
  ("theo giờ Việt Nam (Phụ lục E §H8, BA chốt 2026-08-06)"), còn phiếu `_16` kỳ vọng
  `HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx`. **Hai chuỗi khác nhau.** Đây là chỗ phải khóa `MATCH/DIFF/GAP`
  bằng SRS trước khi mở màn — không được kết luận từ dòng này.
- Mô tả `POST /{id}/files` ghi: chặn nạp tệp khi hợp đồng đã `HOAN_THANH` / `HET_HAN` / `HUY`.

### 3.2 Đợt báo cáo / báo cáo kết quả CT

| Việc | Endpoint | Vai trò / ghi chú |
|---|---|---|
| Danh sách đợt | `GET /api/v1/dot-bao-caos` | lọc `trangThai`, `kyBaoCao`; phân trang `page`/`pageSize` |
| Chi tiết đợt | `GET /api/v1/dot-bao-caos/{id}` | đơn vị trong phạm vi đợt cũng mở được |
| Tạo đợt | `POST /api/v1/dot-bao-caos` | chỉ `CB_NV_TW` có `create_dot_bao_cao` |
| Sửa / Xóa đợt | `PATCH` · `DELETE /{id}` | đòi `version` |
| Bắt đầu lập BC | `POST /{id}/start` | body `version`* + `soLieuTongHop` + `nhanXet` |
| Cập nhật số liệu | `PATCH /{id}/bao-cao` | body `soLieuTongHop`* + `nhanXet` + `ctHtplIdsLienQuan` (**không** đòi `version`) |
| Trình duyệt nội bộ | `POST /{id}/submit-bc` | body `ghiChu` + `version`* |
| Phê duyệt nội bộ | `POST /{id}/approve-bc` | body `quyetDinh`* (`DUYET`/`TU_CHOI`) + `lyDoTuChoi` + `ghiChuPheDuyet` + `version`* — **CB PD cùng đơn vị**, có ràng buộc phân tách nhiệm vụ (BR-SOD) |
| **Gửi TW** | `POST /{id}/gui-tw` | body `ghiChu` + `version`* — quyền `gui-tw_dot_bao_cao` (BN/DP) |
| **Danh sách số liệu tổng hợp** | **`GET /api/v1/dot-bao-caos/tong-hop`** | lọc `kyBaoCao`, `donViId`, `tuNgay`, `denNgay` — **chỉ cấp TW** |
| **Gợi ý số liệu tổng hợp** | **`POST /api/v1/dot-bao-caos/tong-hop/goi-y`** | body `baoCaoIds`* — **CHỈ ĐỌC**, không tạo bản ghi, không đổi trạng thái |
| **Tổng hợp toàn quốc (theo lô)** | **`POST /api/v1/dot-bao-caos/tong-hop`** | body `baoCaoIds`* + `soLieuTongHop` + `nhanXet` — quyền `TongHop`, chỉ TW |
| Tổng hợp một đợt | `POST /api/v1/dot-bao-caos/{id}/tong-hop` | body `version`* + `soLieuTongHop` + `nhanXet` |
| **Xuất tệp tổng hợp** | **`POST /api/v1/dot-bao-caos/tong-hop/export`** | body `baoCaoIds`* + `format`* (`xlsx`/`docx`) + `bieuMau` |
| Sửa báo cáo tổng hợp TW | `PATCH /api/v1/bao-cao-ct-htpl/{id}/chinh-sua-tong-hop` | body `soLieuTongHop` + `nhanXet` + `version`* |
| **Chốt báo cáo tổng hợp TW** | `POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop` | body **chỉ** `version`* |

✅ **CÓ endpoint tổng hợp toàn quốc.** Tên: **`POST /api/v1/dot-bao-caos/tong-hop`** (theo lô `baoCaoIds`),
đi kèm bộ 3: `…/tong-hop/goi-y` (gợi ý số liệu, chỉ đọc) và `…/tong-hop/export` (xuất tệp).
Bước chốt cuối là `POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop`.

Mô tả trong lược đồ (chép nguyên văn, dùng để chọn đường đo — **không** dùng làm chuẩn chấm thay SRS):

- `…/tong-hop/goi-y`: "cộng các chỉ tiêu tương ứng của **Biểu 21a/21b** từ những báo cáo được chọn, **luôn
  phủ đủ 13 chỉ tiêu** (chỉ tiêu thiếu trả 0) kèm ngữ cảnh đợt (tên đợt, kỳ báo cáo, biểu mẫu, số đơn vị).
  **Chỉ ĐỌC** — không tạo bản ghi, không đổi trạng thái đợt, không ghi nhật ký."
- `…/{id}/submit-bc`: "…kiểm tra báo cáo đã hoàn chỉnh — phải có **đủ 13 chỉ tiêu Biểu 21a/21b theo
  TT 17/2025** (giá trị 0 vẫn hợp lệ); nếu thiếu thì trả **422** kèm thông điệp **'Vui lòng hoàn chỉnh báo
  cáo trước khi trình'** và danh sách chỉ tiêu còn thiếu tại `error.details.chiTieuConThieu`."
- `…/hoan-thanh-tong-hop`: "chuyển trạng thái báo cáo sang `DA_DUYET` và đồng thời cập nhật đợt báo cáo
  liên quan sang **`DA_TONG_HOP`**."
- `…/tong-hop/export`: "…theo khung **Thông tư 17/2025/TT-BTP**: khổ A4, phông Times New Roman 13, đầu
  trang có quốc hiệu - tiêu ngữ và tên cơ quan ban hành, cuối trang có ngày ký, họ tên cán bộ xuất báo cáo
  và chỗ trống đóng dấu (**không in dòng chức danh do hồ sơ tài khoản không lưu chức vụ**). Tên tệp theo
  khuôn **`BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}`**."

- **manh mối** — phiếu `THBCTHCT_05` kỳ vọng tên tệp `BaoCaoTongHop_CTHTPL_{…}`, lược đồ ghi
  `BaoCaoTongHopCTHTPL_{…}` (thiếu một dấu gạch dưới); phiếu cũng kỳ vọng "chức danh người ký" trong khi
  lược đồ nói rõ **không in dòng chức danh**. Hai điểm này phải khóa `MATCH/DIFF/GAP` bằng SRS trước khi đo.

**Enum trạng thái** không nằm trong `components.schemas` (mô tả OpenAPI để `trangThai`/`trangThaiNop` là
`string` trần) — các giá trị dưới đây là **quan sát thực từ dữ liệu**, không phải từ lược đồ:
`trangThai` cấp ĐỢT: `TAO_DOT` (đang thấy) · `DA_TONG_HOP` (theo mô tả `hoan-thanh-tong-hop`).
`trangThaiNop` cấp ĐƠN VỊ: `CHUA_NOP` · `DANG_LAP` · `CHO_DUYET` · `DA_NOP`.
`trangThai` cấp BÁO CÁO: `DU_THAO` · `NHAP` · `CHO_PHE_DUYET` · `DA_DUYET` · **`DA_GUI_TW`**.

### 3.3 Điểm danh khóa học (phục vụ `KTDGKQHT_05`)

| Việc | Endpoint | Tham số / body |
|---|---|---|
| **Tải mẫu** | `GET /api/v1/khoa-hocs/{khoaHocId}/diem-danhs/template` | `lichHocId` (query, **bắt buộc**) |
| **Kiểm tệp / xem trước** | `POST /api/v1/khoa-hocs/{khoaHocId}/diem-danhs/import/preview` | multipart: `file`* + `lichHocId`* — "chưa ghi dữ liệu" |
| **Xác nhận nạp** | `POST /api/v1/khoa-hocs/{khoaHocId}/diem-danhs/import/confirm` | JSON: `sessionId`* + `lichHocId`* |
| **Đọc điểm danh theo buổi** | `GET /api/v1/khoa-hocs/{khoaHocId}/diem-danhs` | `ngayDiemDanh` (**bắt buộc**) + `lichHocId` (**bắt buộc**) |
| Ghi tay hàng loạt | `POST /{khoaHocId}/diem-danhs/batch-update` | `diemDanhs[]` = `hocVienId`* + `trangThai` (`CO_MAT`/`VANG_PHEP`/`VANG_KHONG_PHEP`) + `coMat` + `ghiChu` |
| Xuất bảng điểm danh | `POST /{khoaHocId}/diem-danhs/export` | `lichHocId` (query, tùy chọn) |
| Danh sách buổi học | `GET /{khoaHocId}/lich-hocs` · thêm buổi `POST` cùng đường dẫn | `CreateLichHocDto`: `ngayHoc`* · `gioBatDau`* · `gioKetThuc`* · `hinhThucBuoi`* |
| Danh sách đăng ký | `GET /{khoaHocId}/dang-ky-dao-taos` | `keyword` · `trangThai` (`CHO_DUYET`/`DA_DUYET`/`TU_CHOI`/`DA_HUY`) |

Đã kiểm endpoint mẫu gọi được (chỉ đọc mã trả về + tiêu đề, **không mở nội dung tệp** — nội dung tệp mẫu
thuộc phần đang tranh chấp, để tác nhân đo mở):
```
GET /khoa-hocs/a7480002…0002/diem-danhs/template?lichHocId=bd1cdf35…c8c2
→ HTTP 200 · content-type xlsx · content-disposition: filename="mau-diem-danh-KH-QAW7-HOINGHI.xlsx" · 8189 byte
```

### 3.4 🔴 Endpoint KHÔNG tồn tại trong lược đồ (thông tin quan trọng cho tác nhân đo)

| Thứ hay bị đoán nhầm | Sự thật trong lược đồ |
|---|---|
| `hop-dong-tu-van` (số ít) | **không có** — chỉ có `hop-dong-tu-vans` |
| `GET /hop-dong-tu-vans/{id}/vu-viecs` (bảng vụ việc liên kết riêng) | **không có** — vụ việc liên kết đi trong `vuViecIds` của DTO tạo/sửa |
| `POST /hop-dong-tu-vans/{id}/vu-viecs` · `DELETE /{id}/vu-viecs/{vuViecId}` (liên kết / bỏ liên kết) | **không có** — `_22` / `_23` phải đi qua `PATCH /{id}` với `vuViecIds` |
| `GET /hop-dong-tu-vans/search` | **không có** (khác `vu-viec/search`, `tu-van-vien/search` là có) |
| tham số từ khóa cho hợp đồng (`tuKhoa` / `q` / `keyword`) | **không có** ở cả `GET` danh sách lẫn `POST /export` |
| `GET /dot-bao-caos/{id}/export` | **không có** — chỉ có `POST /dot-bao-caos/tong-hop/export` (cấp TW) |
| `POST /dot-bao-caos/{id}/tong-hop-toan-quoc` | **không có** — tên thật là `POST /dot-bao-caos/tong-hop` |
| endpoint xóa mốc / xóa giai đoạn thanh toán riêng lẻ | **không có** — dùng `POST /{id}/moc-tien-dos` và `POST /{id}/thanh-toans` kiểu "thêm/cập nhật/xóa hàng loạt" |
| `GET /khoa-hocs/{id}/diem-danhs` không truyền tham số | **không chạy** — `ngayDiemDanh` **và** `lichHocId` đều bắt buộc |

---

## 4. Kiểm kê tiền đề đang có

### 4.1 Hợp đồng tư vấn — 🔴 **0 (KHÔNG) bản ghi**

Vì `GET` danh sách bắt buộc tham số ngữ cảnh, đã **quét vét cạn** toàn bộ không gian ngữ cảnh mà tài khoản
`cbnv_tw_03` (cấp TW, phạm vi rộng nhất trong bộ `_03`) nhìn thấy:

| Trục ngữ cảnh | Số bản ghi quét | Số hợp đồng tìm thấy |
|---|---|---|
| `tuVanVienId` — toàn bộ tư vấn viên | **44 / 44** (`pageSize=200`) | **0** |
| `toChucTuVanId` — toàn bộ tổ chức tư vấn | **7 / 7** | **0** |
| `vuViecId` — toàn bộ vụ việc | **60 / 60** | **0** |
| | **Tổng 111 lượt gọi, 0 lỗi HTTP** | **0** |

Đối chứng độc lập: `GET /hop-dong-tu-vans/ma-preview` trả **`HDTV-20260807-0001`** cho cả `cbnv_tw_03` lẫn
`cbnv_dp_03` ⇒ số thứ tự của ngày 07/08 **chưa được cấp phát lần nào**.

⇒ **Không có bản ghi nào có vụ việc liên kết, cũng không có bản ghi nào không có vụ việc liên kết.**
Phiếu `_17` (xóa khi KHÔNG có vụ việc liên kết) và `_18` (xóa khi CÓ vụ việc liên kết) **đều thiếu tiền đề**.

**Nguyên liệu sẵn có để dựng** (khi tác nhân đo cần seed):

| Nguyên liệu | Số lượng nhìn thấy bởi `cbnv_tw_03` | Bởi `cbnv_bn_03` | Bởi `cbnv_dp_03` |
|---|---|---|---|
| Tư vấn viên | 44 | 1 | 4 |
| Tổ chức tư vấn | 7 (3 `HOAT_DONG`, 2 `MOI_DANG_KY`, 2 `CHO_PHE_DUYET`) | 0 | 1 (`HOAT_DONG`) |
| Vụ việc | 60 (28 `DANG_XU_LY`, 25 `HOAN_THANH`, 3 `CHO_TIEP_NHAN`, 1 `CHO_PHE_DUYET`, 1 `TU_CHOI`) | 4 | 8 |

### 4.2 Đợt báo cáo — 4 đợt, tất cả đều `trangThai = TAO_DOT`

`GET /api/v1/dot-bao-caos?pageSize=200`. Cột `trangThaiNop` **phụ thuộc tài khoản đang gọi**
(là trạng thái nộp của ĐƠN VỊ người gọi trong đợt đó) — bảng dưới ghi cả 3 góc nhìn.

| # | `maDot` | `tenDot` | `kyBaoCao` | `trangThai` (ĐỢT) | `version` | `bieuMauSuDung` | `hanNop` | phạm vi | `id` |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `DOT-TRON_NAM-2026-1` | QA F5 reverify 21b - CA_HAI (LBCKQTHCT_04) | `TRON_NAM` | `TAO_DOT` | 1 | `CA_HAI` | 2026-12-31 | **2 đơn vị** | `a63a3214-d1d3-421b-8c0c-cec5db419413` |
| 2 | `DOT-THBC01-UAT` | THBCTHCT_01 - Đợt báo cáo sơ bộ 6 tháng 2026 (seed UAT) | `SO_BO_6_THANG` | `TAO_DOT` | 2 | `MAU_21A` | 2026-07-31 | **2 đơn vị** | `d7a62f6e-a119-4582-8b08-f935d25c534b` |
| 3 | `DOT-SO_BO_NAM-2026-1` | QA Reverify CTBC 715 v2 fresh | `SO_BO_NAM` | `TAO_DOT` | 1 | `MAU_21A` | 2026-12-31 | **83 đơn vị** | `e9909d96-1391-463b-8072-b1b56c319f8e` |
| 4 | `DOT-SO_BO_6_THANG-2026-1` | QA Reverify CTBC 715 BN | `SO_BO_6_THANG` | `TAO_DOT` | 1 | `MAU_21A` | 2026-12-31 | **83 đơn vị** | `a61e07f1-e205-4948-ad7d-a3ccac49830a` |

`trangThaiNop` cấp ĐƠN VỊ + `baoCaoId` tương ứng:

| Đợt | `cbnv_bn_03` (Bộ KH&ĐT) | `cbnv_dp_03` (Sở TP An Giang) |
|---|---|---|
| `DOT-TRON_NAM-2026-1` | **404 — ngoài phạm vi** | `CHUA_NOP` · `baoCaoId = null` |
| `DOT-THBC01-UAT` | `DA_NOP` · `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | `DA_NOP` · `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` |
| `DOT-SO_BO_NAM-2026-1` | `CHO_DUYET` · `c19b1bc2-f6d9-484c-9d47-ada2b351456e` | `DANG_LAP` · `c1b1045d-007c-4104-a169-e267010557a0` |
| `DOT-SO_BO_6_THANG-2026-1` | `CHO_DUYET` · `a63bf70c-9ed0-4587-b5e2-9b9689dfa94c` | `DANG_LAP` · `f445b699-04bd-4c94-ab77-9ca118c78dd0` |

Bảng `tienDo` (tiến độ nộp theo đơn vị) trong chi tiết đợt — **chỉ tài khoản TW đọc được**
(`cbnv_bn_03` / `cbnv_dp_03` đều nhận `tienDo = []`):

| Đợt | số dòng `tienDo` | phân bố `trangThaiNop` | đơn vị đã động vào |
|---|---|---|---|
| `DOT-TRON_NAM-2026-1` | 2 | `CHUA_NOP` 1 · `DANG_LAP` 1 | Sở Tư pháp Hà Nội (`DANG_LAP`, bc `1b3085b8…`) |
| `DOT-THBC01-UAT` | 2 | **`DA_NOP` 2** | Bộ KH&ĐT (nộp 2026-07-20) · Sở TP An Giang (nộp 2026-07-22) |
| `DOT-SO_BO_NAM-2026-1` | 83 | `CHUA_NOP` 80 · `CHO_DUYET` 1 · `DANG_LAP` 1 · **`DA_NOP` 1** | Bộ KH&ĐT (`CHO_DUYET`) · Sở TP An Giang (`DANG_LAP`) · **Sở TP Hà Nội (`DA_NOP`, nộp 2026-08-06 20:11)** |
| `DOT-SO_BO_6_THANG-2026-1` | 83 | `CHUA_NOP` 81 · `CHO_DUYET` 1 · `DANG_LAP` 1 | Bộ KH&ĐT (`CHO_DUYET`) · Sở TP An Giang (`DANG_LAP`) |

#### 🔴 Có báo cáo "Đã gửi Trung ương" không? — **CÓ, 3 báo cáo**

`GET /api/v1/dot-bao-caos/tong-hop?pageSize=200` với `cbnv_tw_03` (và `cbpd_tw_03` cho ra y hệt):

| # | `baoCaoId` | Đợt | `kyBaoCao` | `bieuMauSuDung` | Đơn vị | `trangThai` | `ngayGuiTw` |
|---|---|---|---|---|---|---|---|
| 1 | `c4801d2d-dedc-4ffe-b5d2-44e9245fbedc` | `DOT-THBC01-UAT` | `SO_BO_6_THANG` | `MAU_21A` | Bộ Kế hoạch và Đầu tư (BN) | **`DA_GUI_TW`** | 2026-07-20 02:00 |
| 2 | `df6498aa-4ae4-4d59-ba3e-7c322e1f9a59` | `DOT-THBC01-UAT` | `SO_BO_6_THANG` | `MAU_21A` | Sở Tư pháp An Giang (DP) | **`DA_GUI_TW`** | 2026-07-22 07:30 |
| 3 | `4db99158-5bc4-4069-9d52-cfc756aadc2e` | `DOT-SO_BO_NAM-2026-1` | `SO_BO_NAM` | `MAU_21A` | Sở Tư pháp Hà Nội (DP) | **`DA_GUI_TW`** | 2026-08-06 20:11 |

✅ **Đủ ≥2 báo cáo `DA_GUI_TW` ⇒ 3 phiếu `THBCTHCT_*` có tiền đề.**
⚠️ Nhưng chỉ **#1 và #2 cùng một đợt / cùng kỳ / cùng biểu mẫu** (`DOT-THBC01-UAT`, `SO_BO_6_THANG`,
`MAU_21A`). #3 khác đợt và khác kỳ (`SO_BO_NAM`). **Cặp sạch để tổng hợp là {#1, #2}.**
`cbnv_bn_03` và `cbnv_dp_03` gọi endpoint này đều nhận `403 ERR-PERM-XI-09-02` — "Chỉ cấp TW mới có quyền
tổng hợp báo cáo".

⚠️ **Hai bậc tên trạng thái khác nhau cho cùng một sự việc** (chỗ dễ chấm oan):
`tienDo[].trangThaiNop = DA_NOP` (bậc ĐƠN VỊ trong đợt) ứng với `…/tong-hop → trangThai = DA_GUI_TW`
(bậc BÁO CÁO). Cùng một báo cáo, hai tên. Khi phiếu nói "Đã gửi Trung ương", **phải xác định màn đang hiện
bậc nào** trước khi kết luận — không tự quy đổi.

#### Nội dung báo cáo (chỉ đếm số chỉ tiêu, không đánh giá) — phục vụ `TPDBCKQTHCT_02`

| `baoCaoId` | Đơn vị | `trangThai` BC | số khóa trong `soLieuTongHop` | danh sách khóa |
|---|---|---|---|---|
| `c4801d2d…` | Bộ KH&ĐT (`DOT-THBC01-UAT`) | `DA_DUYET` | **13** | `kpXaHoiHoa` · `kpHoTroTvpl` · `soHsTiepNhan` · `soCuocTapHuan` · `soTvvKienToan` · `kpHoatDongKhac` · `soVBTraLoiUBND` · `hsDoanhNghiepNho` · `hsDoanhNghiepVua` · `soHoiNghiDoiThoai` · `soHsGiaiQuyetTong` · `soVBTvMangLuoiTVV` · `hsDoanhNghiepSieuNho` |
| `c1b1045d…` | Sở TP An Giang (`DOT-SO_BO_NAM-2026-1`) | `DU_THAO` | **3** | `soVuViec` · `tongChiPhi` · `soDnDuocHoTro` |
| `f445b699…` | Sở TP An Giang (`DOT-SO_BO_6_THANG-2026-1`) | `DU_THAO` | **3** | `soVuViec` · `tongChiPhi` · `soDnDuocHoTro` |
| `c19b1bc2…` | Bộ KH&ĐT (`DOT-SO_BO_NAM-2026-1`) | `CHO_PHE_DUYET` | **3** | `soVuViec` · `tongChiPhi` · `soDnDuocHoTro` |

⇒ Hai báo cáo `DU_THAO` của `cbnv_dp_03` có **3 chỉ tiêu**, mà `submit-bc` đòi **13 chỉ tiêu Biểu 21a/21b**
⇒ **tiền đề "Báo cáo chưa đầy đủ" của `TPDBCKQTHCT_02` ĐÃ CÓ SẴN, không cần dựng gì.**
Cả 2 đợt đều có `_links.submit-bc` cho `cbnv_dp_03`.

- **manh mối** — báo cáo `c19b1bc2…` của Bộ KH&ĐT đã ở `CHO_PHE_DUYET` (tức đã qua `submit-bc`) nhưng
  cũng chỉ có 3 chỉ tiêu. Có thể bản ghi này được nộp trước khi luật kiểm 13 chỉ tiêu được thêm. Ghi nhận
  làm manh mối, **KHÔNG điều tra trong lô này**.
- Trường **`soLieuKyTruoc`** và **`soLieuGoiY`** tồn tại ở cấp cao nhất của phản hồi chi tiết đợt, hiện
  **đều `null`** ở cả 4 đợt.

### 4.3 Khóa học `KH-QAW7-HOINGHI` (phục vụ `KTDGKQHT_05`)

`GET /api/v1/khoa-hocs/a7480002-0000-4000-8000-000000000002` — **chỉ `cbnv_tw_03` đọc được**
(`cbnv_dp_03` nhận 404 `ERR-VAL-VII-02-01`; khóa thuộc `donViId = 00000000-0000-4000-8000-000000000001`
= Cục Bổ trợ tư pháp - Bộ Tư pháp, cấp TW).

| Thuộc tính | Giá trị |
|---|---|
| `maKhoaHoc` / `tenKhoaHoc` | `KH-QAW7-HOINGHI` / QAW7 — Hội nghị đối thoại DN 2026 |
| **`trangThai`** | ✅ **`DANG_DIEN_RA`** (đúng điều kiện phiếu) |
| `version` | **6** |
| `ngayBatDau` – `ngayKetThuc` | 2026-05-10 – 2026-05-11 |
| `hinhThuc` | `TRUC_TIEP` |
| `soHocVienDaDangKy` | 4 · `soLuongToiDa` 100 · `tyLeChuyenCanToiThieu` 80 |
| `soBuoiHoc` (trường trong bản ghi khóa) | **1** — **manh mối**: lệch với số buổi thực trong `lich-hocs` (4). Ghi nhận, không điều tra. |
| `_links` | `self` · `finish` · `publish` |

**Buổi học — `GET /{id}/lich-hocs` → 4 buổi:**

| # | `lichHocId` | `ngayHoc` | Giờ | Nội dung |
|---|---|---|---|---|
| 1 | `16ccd447-2c50-4d2f-8c8e-f97eb46a9de3` | 2026-05-10 | 08:00–10:00 | Buổi 1 - QA seed KTDGKQHT_02 |
| 2 | `7b5cd560-74ab-4631-b362-3b70f6da646d` | 2026-05-10 | 14:00–16:00 | Buổi 2 - QA seed KTDGKQHT_02 |
| 3 | `cde385a9-7dd7-4513-a3f9-fa1999dd0edf` | 2026-05-11 | 08:00–10:00 | Buổi 3 - QA seed KTDGKQHT_02 |
| 4 | `bd1cdf35-8ab7-41f6-ae85-d21fdec2c8c2` | 2026-05-11 | 14:00–16:00 | Buổi 4 - QA seed KTDGKQHT_23 |

**Học viên — `GET /{id}/dang-ky-dao-taos` → 6 đăng ký:** ✅ **4 `DA_DUYET`** + 2 `CHO_DUYET`.

**🔴 Buổi nào đã có dữ liệu điểm danh** (`GET /{id}/diem-danhs?lichHocId=…&ngayDiemDanh=…`, mỗi buổi trả
4 dòng ứng 4 học viên đã duyệt):

| Buổi | Phân bố `trangThai` | Còn sạch? |
|---|---|---|
| Buổi 1 (`16ccd447…`) | `CO_MAT` 2 · chưa ghi 2 | ❌ **đã bẩn** |
| Buổi 2 (`7b5cd560…`) | `CO_MAT` 1 · `VANG_PHEP` 1 · chưa ghi 2 | ❌ **đã bẩn** |
| Buổi 3 (`cde385a9…`) | `CO_MAT` 1 · `VANG_KHONG_PHEP` 1 · chưa ghi 2 | ❌ **đã bẩn** |
| **Buổi 4 (`bd1cdf35…`)** | **chưa ghi 4/4** | ✅ **CÒN SẠCH — duy nhất** |

⇒ Đúng buổi mà khối `CÁCH VERIFY` chỉ định (Buổi 4) **vẫn còn sạch**: lượt đo 02:18 ngày 07/08 trả lỗi
máy chủ nên không ghi được dòng nào, khớp với ghi chép cũ ("0/3 dòng hợp lệ được ghi").

**Trường trong bản ghi điểm danh:** `id` · `hocVienId` · `hoTen` · `donVi` · `email` · `soDienThoai` ·
`ngayDiemDanh` · `trangThai` · `coMat` · `ghiChu`.
- **manh mối** — **không có trường mã học viên** trong phản hồi danh sách điểm danh, trong khi ô
  `TKM phản hồi lần 1` của phiếu viết "Màn hình danh sách không hiển thị mã học viên nhưng khi nhập file
  excel điểm danh hệ thống bắt buộc có mã học viên". Ghi nhận làm manh mối chỉ chỗ cần đọc SRS —
  **chưa mở tệp mẫu, chưa kết luận**.

**Khóa học khác đang diễn ra** (dự phòng): `DDD-KH-011` "Khóa học pháp luật doanh nghiệp seed"
(`dddddddd-0000-4000-8000-000000000011`) — chỉ **1** học viên đã đăng ký. Tổng 16 khóa học ở phạm vi TW
(7 `HOAN_THANH`, 2 `DU_THAO`, 2 `DANG_DIEN_RA`, 2 `DA_KET_THUC`, 1 mỗi loại `DA_DUYET`/`CHO_DUYET`/`CHO_DUYET_KQ`).

---

## 5. Hệ quả cho việc lập kế hoạch đo

### 5.1 ✅ Đã có sẵn tiền đề — vào đo được ngay (5 phiếu)

| Phiếu | Tiền đề sẵn có | Tác nhân |
|---|---|---|
| `KTDGKQHT_05` | Khóa `KH-QAW7-HOINGHI` `DANG_DIEN_RA` · 4 buổi · 4 học viên `DA_DUYET` · **Buổi 4 `bd1cdf35…` còn sạch** | `cbnv_tw_03` |
| `TPDBCKQTHCT_02` | 2 đợt của Sở TP An Giang ở `DANG_LAP` với báo cáo chỉ **3/13 chỉ tiêu** (`c1b1045d…`, `f445b699…`), đều có `_links.submit-bc` | `cbnv_dp_03` |
| `THBCTHCT_02` (bấm "Tổng hợp" → gợi ý số liệu) | 3 báo cáo `DA_GUI_TW`; cặp cùng đợt/kỳ/biểu mẫu = `c4801d2d…` + `df6498aa…`. Bước gợi ý là **chỉ đọc**, không tiêu hủy tiền đề | `cbnv_tw_03` |
| `THBCTHCT_01` (Lưu tổng hợp) | như trên — **nhưng chỉ chạy sạch được 1 lượt**, xem §5.3 | `cbnv_tw_03` |
| `QLHDTVVCG_04` (tìm kiếm KHÔNG có kết quả) | 0 hợp đồng ⇒ mọi tiêu chí tìm kiếm đều cho tập rỗng | `cbnv_*_03` |

### 5.2 🟡 Phải dựng thêm trước khi đo (16 phiếu — toàn bộ phần còn lại của `QLHDTVVCG_*`)

Cả module hợp đồng tư vấn đang **rỗng tuyệt đối (0 bản ghi)**. Cần dựng:

| Cần dựng | Phục vụ phiếu | Ghi chú dựng |
|---|---|---|
| **HĐ-A: 1 hợp đồng KHÔNG có vụ việc liên kết** (`vuViecIds: []`), có ≥2 `mocTienDos` và ≥2 `thanhToans` | `_03` `_08` `_16` **`_17`** `_19` `_21` `_24` `_26` `_27` | `POST /api/v1/hop-dong-tu-vans` |
| **HĐ-B: 1 hợp đồng CÓ ≥1 vụ việc liên kết** | `_09` **`_18`** `_22` `_23` | cùng endpoint, thêm `vuViecIds` |
| (không cần bản ghi, chỉ cần vào được màn) | `_02` `_05` `_13` `_15` | `_15` chính là hành vi tạo — đo bằng giao diện, đừng seed trước |

Nguyên liệu để gán: 44 tư vấn viên · 7 tổ chức tư vấn · 60 vụ việc (số của `cbnv_tw_03`).
Nếu đo bằng `cbnv_dp_03` thì phải chọn trong 4 TVV / 1 TCTV / 8 VV thuộc Sở TP An Giang.

⚠️ **Khai báo seed bắt buộc** (flow 04 §4.5): ghi rõ đã tạo hợp đồng nào (mã + ID), gắn vụ việc nào, trên
env nội bộ. Seed = làm thay đổi môi trường chung.

### 5.3 🔴 Có nguy cơ không dựng nổi / chỉ đo được một lượt — CẢNH BÁO SỚM

**(a) `QLHDTVVCG_02` — "Chọn menu Hợp đồng Tư vấn" rồi xem bộ lọc.**
Endpoint danh sách **trả 403 khi không có tham số ngữ cảnh** (`ERR-PERM-SYS-00-01`, đã kiểm bằng `curl`).
Nếu màn danh sách của FE gọi thẳng `GET /hop-dong-tu-vans` khi vừa mở menu thì màn sẽ không có dữ liệu để
hiển thị — **nhưng đây mới là manh mối**, chưa đo bằng giao diện, và cũng chưa biết SRS quy định màn này
vào bằng đường nào (có thể vào từ trong chi tiết vụ việc / tư vấn viên). **Tác nhân đo phải xác định trước
tiên: màn "Hợp đồng Tư vấn" vào bằng đường nào**, vì cả 18 phiếu `QLHDTVVCG_*` đều bắt đầu bằng bước
"Chọn menu Hợp đồng Tư vấn". Nếu không vào được màn thì 18 phiếu kẹt cùng lúc → ghi `Chưa chốt`, báo điều phối.

**(b) `THBCTHCT_01` — chỉ có MỘT lượt đo sạch.**
`POST /dot-bao-caos/tong-hop` chuyển các báo cáo đã chọn khỏi `DA_GUI_TW`, và `hoan-thanh-tong-hop` đẩy đợt
sang `DA_TONG_HOP`. Sau lượt đầu, cặp `c4801d2d…` + `df6498aa…` **không còn dùng lại được**.
⇒ **Thứ tự đo bắt buộc:** `THBCTHCT_02` (gợi ý — chỉ đọc) **trước**, rồi `THBCTHCT_01` (lưu tổng hợp),
rồi `THBCTHCT_05` (xuất tệp trên bản tổng hợp vừa chốt). Đảo thứ tự = mất tiền đề.
Muốn đo lại, phải dựng thêm báo cáo `DA_GUI_TW` mới — đường ngắn nhất:
```
Bộ KH&ĐT đang CHO_DUYET ở DOT-SO_BO_NAM-2026-1 và DOT-SO_BO_6_THANG-2026-1
  → cbpd_bn_03: POST /{id}/approve-bc {quyetDinh:"DUYET", version}
  → cbnv_bn_03: POST /{id}/gui-tw    {version}
```
(2 báo cáo dự phòng). Xa hơn: Sở TP An Giang `DANG_LAP` → cần bù đủ 13 chỉ tiêu rồi `submit-bc` →
`cbpd_dp_03` `approve-bc` → `gui-tw`.

**(c) `THBCTHCT_05` — phụ thuộc (b).** Điều kiện phiếu là "Đã hoàn thành tổng hợp báo cáo toàn quốc"
⇒ chỉ đo được **sau** khi `THBCTHCT_01` chạy xong. Nếu `_01` hỏng thì `_05` kẹt theo.

**(d) `KTDGKQHT_05` — chỉ còn MỘT buổi sạch.**
Buổi 4 là buổi duy nhất chưa có dữ liệu điểm danh. Chạy `import/confirm` một lần là buổi 4 hết sạch.
Muốn đo lại phải **thêm buổi mới** (`POST /{khoaHocId}/lich-hocs`, `cbnv_tw_03` có `create_lich_hoc`) —
và phải khai vào báo cáo. Đừng dùng buổi 1/2/3 (đã có sẵn trạng thái → không đếm được "đúng 3 dòng mới ghi").

**(e) `KTDGKQHT_05` — khối `CÁCH VERIFY` ghi tài khoản `cbnv_tw_02`, prompt lô F8 chỉ định bộ `_03`.**
Cùng `vai_tro` `CB_NV_TW` + cùng cấp `TW` + cùng `donViId` ⇒ thay `cbnv_tw_03` là hợp lệ theo Rule 7,
nhưng **phải ghi rõ tài khoản thực dùng** trong báo cáo. Đã kiểm: `cbnv_tw_03` có `read_diem_danh` +
`update_diem_danh` và đọc được khóa `KH-QAW7-HOINGHI`.

**(f) `KTDGKQHT_05` được đo lần trước trên bản dựng `index-DsMHK7Dp.js` (07/08 01:51).**
Bản đang phục vụ là `index-eWHwDgt2.js` (07/08 09:11) — **đã qua 2 lần deploy**. Lỗi cũ là lỗi máy chủ
(HTTP 500 `ERR-SYS-00-00-01` ở bước xác nhận nạp), không phải lỗi màn hình ⇒ phải đo lại thật, không suy từ
số cũ.

### 5.4 Bảng gọn — 23 phiếu

| Nhóm | Phiếu | Trạng thái tiền đề |
|---|---|---|
| Đã có sẵn | `KTDGKQHT_05` · `TPDBCKQTHCT_02` · `THBCTHCT_02` · `QLHDTVVCG_04` | vào đo được ngay |
| Có sẵn nhưng **một lượt duy nhất** | `THBCTHCT_01` (→ kéo theo `THBCTHCT_05`) | phải đo đúng thứ tự `_02` → `_01` → `_05` |
| Phải dựng **HĐ-A** (không vụ việc liên kết) | `QLHDTVVCG_03` `_08` `_16` `_17` `_19` `_21` `_24` `_26` `_27` | 9 phiếu |
| Phải dựng **HĐ-B** (có vụ việc liên kết) | `QLHDTVVCG_09` `_18` `_22` `_23` | 4 phiếu |
| Không cần bản ghi, nhưng cần vào được màn | `QLHDTVVCG_02` `_05` `_13` `_15` | 4 phiếu |
| 🔴 Rủi ro chặn cả nhóm | **toàn bộ 18 phiếu `QLHDTVVCG_*`** nếu màn danh sách không vào được | xem §5.3(a) |

---

## 6. Ràng buộc kỹ thuật khi dựng tiền đề

1. **Mọi hành động chuyển trạng thái đòi `version` hiện tại ⇒ `GET` chi tiết ngay trước MỖI bước.**
   Sai `version` → **409 khóa lạc quan**, đây là **xung đột kỹ thuật, KHÔNG phải bug nghiệp vụ** — đừng log nhầm.
   Danh sách hành động đòi `version`: `PATCH /dot-bao-caos/{id}` · `DELETE /dot-bao-caos/{id}` ·
   `POST /{id}/start` · `/submit-bc` · `/approve-bc` · `/gui-tw` · `/{id}/tong-hop` ·
   `PATCH /bao-cao-ct-htpl/{id}/chinh-sua-tong-hop` · `POST /bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop`.
   **Ngoại lệ:** `PATCH /dot-bao-caos/{id}/bao-cao` (cập nhật số liệu) **không** đòi `version`.
2. **Phân trang: dùng `page` + `pageSize`.** `limit` / `size` / `perPage` **bị bỏ qua âm thầm** (vẫn trả 20
   dòng nhưng `meta.total` đúng) — dễ đếm hụt và kết luận sai "không có dữ liệu".
3. **Danh sách hợp đồng bắt buộc 1 trong 3 tham số ngữ cảnh** (`vuViecId` / `tuVanVienId` / `toChucTuVanId`),
   thiếu → 403 `ERR-PERM-SYS-00-01`. Không có tham số từ khóa. Muốn quét toàn bộ phải lặp qua từng ngữ cảnh.
4. **Quyền theo vai trò** (đã kiểm bằng `/auth/me`, xem bảng §2):
   - Tạo/sửa/xóa hợp đồng: **chỉ `CB_NV_*`**. `CB_PD_*` chỉ đọc + xuất tệp.
   - Tạo đợt báo cáo: **chỉ `CB_NV_TW`**.
   - `approve-bc`: **chỉ `CB_PD_*` cùng đơn vị nộp**, có ràng buộc phân tách nhiệm vụ (BR-SOD) ⇒ người
     trình và người duyệt phải khác nhau.
   - `gui-tw`: `CB_NV_BN` / `CB_NV_DP` (TW **không** có quyền này).
   - `tong-hop` + `chinh-sua-tong-hop` + `hoan-thanh-tong-hop`: **chỉ cấp TW** (`403 ERR-PERM-XI-09-02` cho
     BN/DP, đã kiểm thật).
   - Điểm danh: `read_diem_danh` + `update_diem_danh` có ở `CB_NV_*`; `CB_PD_*` **chỉ đọc**.
5. **Phạm vi dữ liệu theo đơn vị (RLS)** rất chặt: `cbnv_bn_03` nhận **404** khi mở
   `DOT-TRON_NAM-2026-1` (ngoài phạm vi); `cbnv_dp_03` nhận **404** khi mở khóa `KH-QAW7-HOINGHI` (khóa TW).
   Bảng `tienDo` chỉ TW đọc được, BN/DP nhận `[]`. **404 ở đây là phân quyền đúng thiết kế, không phải "mất
   bản ghi"** — đừng log nhầm.
6. **Đọc điểm danh bắt buộc cả `lichHocId` và `ngayDiemDanh`**; `ngayDiemDanh` phải khớp `ngayHoc` của buổi.
7. **Chuỗi dựng báo cáo `DA_GUI_TW`** (mỗi bước `GET` lại lấy `version` mới):
   `start` → `PATCH /{id}/bao-cao` (đủ **13** chỉ tiêu Biểu 21a/21b, giá trị 0 vẫn hợp lệ) →
   `submit-bc` (CB NV) → `approve-bc` (CB PD **cùng đơn vị**) → `gui-tw` (CB NV).
8. **Tệp seed phải là fixture thật** (`.xlsx` đúng định dạng). Với `KTDGKQHT_05`, khối `CÁCH VERIFY` yêu cầu
   giữ nguyên sheet metadata của tệp mẫu tải từ hệ thống — **không tạo tệp mới từ đầu, không đổi đuôi**.
   Đã có sẵn `chuan/KTDGKQHT_05-dien-file-mau.py` từ lượt trước.
9. **Hành động đang tranh chấp phải bấm bằng giao diện thật.** API chỉ để **dựng tiền đề** và **đối chứng**.
10. **Trình duyệt dùng chung — chỉ MỘT tác nhân đo tại một thời điểm.** Việc trinh sát này không đụng trình duyệt.

---

## 7. Những gì lượt trinh sát này CỐ Ý KHÔNG làm

- Không mở nội dung tệp mẫu điểm danh (cột nào, có `hoc_vien_id` không) — thuộc vế đang tranh chấp của `KTDGKQHT_05`.
- Không gọi `POST /tong-hop/goi-y` dù nó chỉ đọc — kết quả gợi ý số liệu là **phép đo** của `THBCTHCT_02`.
- Không gọi `POST /export` của bất kỳ nhóm nào — tên tệp và nội dung tệp là vế đo của `_16` / `THBCTHCT_05`.
- Không đánh giá màn hình, câu chữ thông báo, định dạng hiển thị, hay luồng nghiệp vụ.
- Không dùng `admin` (đúng chỉ đạo prompt) ⇒ mọi con số ở §4 là **số nhìn thấy bởi tài khoản đúng vai trò**.
  Riêng câu "0 hợp đồng" đã được củng cố bằng đối chứng độc lập `ma-preview` (§4.1).
