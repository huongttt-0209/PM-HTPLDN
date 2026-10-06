# Chuẩn bị chung cho cả 7 case — đọc TRƯỚC khi đo

> Lấy ngày **2026-08-07**, trước khi mở màn đang tranh chấp (Flow 04 cấm "xem thử" trước khi khóa chuẩn chấm).
> Mục đích: chống 2 lỗi kinh điển — **đoán endpoint** và **đo nhầm bản dựng cũ**.

## 1. Môi trường + dấu vân tay bản dựng

| Mục | Giá trị |
|---|---|
| Env verify | `https://18.143.165.120.nip.io` (HTTP 200, 0.22s) |
| MailHog | `http://18.143.165.120:8025/` (IP thô, KHÔNG qua nip.io) |
| Bó mã FE | `assets/index-DsMHK7Dp.js` — `1.124.347` bytes |
| ETag JS | `"6a74d7ad-1127fb"` |
| ETag index.html | `"6a74d7ad-428"` |
| Last-Modified | `Thu, 06 Aug 2026 18:51:25 GMT` = **07/08/2026 01:51 giờ VN** |
| Máy chủ web | `nginx/1.27.5` |
| Ổn định? | Đo 2 lượt liên tiếp — **giống hệt nhau**, không có deploy đang chạy dở |

> ⚠️ **Bản dựng vừa lên rất gần giờ đo.** Vòng F3 ngày 06/08 đo trên bó mã `assets/index-DIABnbIr.js`;
> nay là `index-DsMHK7Dp.js` ⇒ **đã có bản triển khai mới**. Đây là bản mang các fix mà dev báo.
> **BẮT BUỘC** với mọi agent đo: tải lại trang bằng địa chỉ (không dùng tab đang mở sẵn) và
> **kiểm lại tên bó mã** trước khi chốt verdict. Tab MCP mở lâu vẫn chạy mã cũ → đã gây Reopen oan trước đây.

**Câu ghi vào kết quả:** *"Đo trên môi trường nội bộ `18.143.165.120.nip.io`, bó mã giao diện
`index-DsMHK7Dp.js` (07/08/2026 01:51). Bằng chứng gốc của đối tác quay trên môi trường khác."*

## 2. Endpoint THẬT (đọc từ `/api/docs-json` — 549 đường dẫn — KHÔNG đoán)

| Endpoint | Tóm tắt của chính hệ thống | Dùng cho case |
|---|---|---|
| `GET /api/v1/dot-bao-caos` | Danh sách đợt báo cáo — tham số `trangThai`, `kyBaoCao` | Tìm tiền đề mọi case |
| `GET /api/v1/dot-bao-caos/{id}` | Chi tiết đợt báo cáo | Đường đo thứ hai mọi case |
| `POST /api/v1/dot-bao-caos/{id}/start` | **Bắt đầu lập báo cáo** | LBCKQTHCT_01 |
| `PATCH /api/v1/dot-bao-caos/{id}/bao-cao` | **Cập nhật số liệu báo cáo** | LBCKQTHCT_01 (lưu nháp) |
| `POST /api/v1/dot-bao-caos/{id}/submit-bc` | **Trình duyệt nội bộ báo cáo** | TPDBCKQTHCT_01 |
| `POST /api/v1/dot-bao-caos/{id}/approve-bc` | **Phê duyệt nội bộ báo cáo** | Dựng tiền đề GKQTHCTHTPL_01 |
| `POST /api/v1/dot-bao-caos/{id}/gui-tw` | **Gửi báo cáo lên Trung ương** | GKQTHCTHTPL_01 |
| `POST /api/v1/dot-bao-caos/{id}/tong-hop` · `/tong-hop/goi-y` · `/tong-hop/export` | TW tổng hợp | Ngoài phạm vi 7 case |
| `PATCH /api/v1/bao-cao-ct-htpl/{id}/chinh-sua-tong-hop` · `POST .../hoan-thanh-tong-hop` | Tổng hợp cấp TW | Ngoài phạm vi |

> 🔴 **`/api/v1/bao-cao/...` (số ít) là nhóm BÁO CÁO THỐNG KÊ — KHÔNG liên quan 7 case này.**
> Nhóm đúng là **`/api/v1/dot-bao-caos/...`** (số nhiều, có `dot-`). Nhầm nhóm = đo sai màn.

## 3. Hình dạng dữ liệu gửi lên (schema thật, không suy đoán)

```
LapBaoCaoDto      required: [version]           { soLieuTongHop: object, nhanXet: string, version: number }
UpdateSoLieuDto   required: [soLieuTongHop]     { soLieuTongHop: object, nhanXet: string, ctHtplIdsLienQuan: string[] }
TrinhDuyetBcDto   required: [version]           { ghiChu: string, version: number }
PheDuyetBcDto     required: [quyetDinh, version]{ quyetDinh: string, lyDoTuChoi: string, ghiChuPheDuyet: string, version: number }
GuiTwDto          required: [version]           { ghiChu: string, version: number }
```

### 3 manh mối quan trọng rút ra từ schema

1. **`nhanXet: string` tồn tại** trong cả `LapBaoCaoDto` lẫn `UpdateSoLieuDto` ⇒ tầng dữ liệu **có** chỗ chứa
   nhận xét. Liên quan trực tiếp **LBCKQTHCT_05** ("thiếu Khối nhận xét, kiến nghị").
   ⚠️ Nhưng *có trường trong DTO* **KHÔNG** tự động = *đặc tả yêu cầu hiển thị khối đó trên màn Chi tiết*.
   Quan hệ MATCH/DIFF/GAP vẫn phải khóa bằng **dòng SRS**, không bằng schema. Schema chỉ là manh mối tìm chỗ đọc.
2. **`ctHtplIdsLienQuan: string[]` tồn tại** ⇒ tầng dữ liệu **có** liên kết sang chương trình HTPL liên quan.
   Liên quan trực tiếp **LBCKQTHCT_06** ("thiếu Khối truy vết chương trình liên quan"). Cùng cảnh báo như trên.
3. **`soLieuTongHop` là `object` tự do** ⇒ các cột "Số liệu kỳ trước" / "Ghi chú" (**LBCKQTHCT_03/04**)
   nếu có sẽ nằm **bên trong** object này, không phải trường riêng. ⇒ Đường đo thứ hai cho 03/04 là
   **đọc khóa thật bên trong `soLieuTongHop`** của một bản ghi đã có số liệu — **CẤM đoán tên khóa**,
   phải `GET /api/v1/dot-bao-caos/{id}` rồi in danh sách khóa ra xem.
4. **Mọi hành động chuyển trạng thái đều đòi `version`** ⇒ khi dựng tiền đề bằng API phải `GET` lấy `version`
   hiện tại trước mỗi bước. Sai `version` sẽ trả lỗi xung đột chứ không phải lỗi nghiệp vụ — **đừng log nhầm thành bug**.

## 4. Tài khoản (chi tiết: `output/UAT_doi-tac/input/input.md`)

| Vai trò cần | Tài khoản | Ghi chú |
|---|---|---|
| CB NV Trung ương | `cbnv_tw` / `cbnv_tw_01` | `Test@1234` |
| CB NV Địa phương | **`cbnv_dp_01`** | ⚠️ `cbnv_dp` login **FAIL** (401) — đã fallback đúng Rule 7 |
| CB NV Địa phương (Hà Nội) | `cbnv_hn` | Sở Tư pháp Hà Nội |
| CB PD Trung ương | **`cbpd_tw_01`** | ⚠️ `cbpd_tw` login **FAIL** (401) |
| CB PD Địa phương | `cbpd_dp` / `cbpd_dp_01` | Duyệt BC nội bộ |
| CB PD Địa phương (Hà Nội) | `cbpd_hn` | Cặp với `cbnv_hn` |
| Quản trị | `admin` / `Secret@123` | **CẤM ra verdict** — chỉ tra định danh, phải khai rõ |

Rule 7 khi login fail: fallback **cùng vai trò + cùng cấp** (`_01` → `_02` → `_03`), **khai account thực dùng**.
Tuyệt đối không đổi cấp TW↔BN↔ĐP (đổi phạm vi dữ liệu ⇒ verdict vô hiệu). Giới hạn đăng nhập **5 lượt / 60 giây**.

## 5. Quy tắc chung khi đo (Flow 04)

- Hành động đang tranh chấp phải làm bằng **giao diện thật**. API/log chỉ để **đối chứng**, không thay thao tác.
- **CẤM Pass bằng quan sát tĩnh** ("thấy nút có rồi") nếu vế bug là một hành động.
- Mỗi vế: **1 đường giao diện + 1 đối chứng độc lập**. Hai đường khớp thì **dừng**, không thêm đường thứ ba.
  **Hai đường mâu thuẫn = CHƯA ĐƯỢC CHỐT** — ghi cả hai, hỏi lại.
- Chữ người dùng nhìn thấy đọc bằng **`innerText`**, KHÔNG `textContent` (gom cả node ẩn → **bug ma**).
- Thông báo nổi (toast): cài bộ bắt **TRƯỚC** khi bấm; **CẤM lọc trùng** (che double-toast → Pass oan);
  đếm số yêu cầu mạng kèm theo. Chỉ cài khi thông báo thuộc vế đang đo.
- Ảnh lưu tại `output/UAT_doi-tac/reverify-week-5/F5-devfix-BCCT-2026-08-07/image/`.
- **7 case này soi 3 luồng + 4 phần khác nhau của cùng 1 màn** ⇒ **CẤM đo 1 case rồi suy cho case khác**.
  Cùng chữ không có nghĩa cùng nguyên nhân.
