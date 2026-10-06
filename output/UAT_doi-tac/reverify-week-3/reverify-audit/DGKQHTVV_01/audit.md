# Audit — DGKQHTVV_01 (row 15) · Nhóm 8 Đánh giá — "không hiện nút chức năng đánh giá"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/DGKQHTVV_01-2.jpg` (ảnh) + `DGKQHTVV_01-1.jpg` (WebM video) (`fetch_evidence.py --row 15`).
- Ảnh (env đối tác `htpldn-uat.ospgroup.vn`): màn chi tiết vụ việc, góc phải hiển thị **"Cán bộ NV Trung ương / CB_NV_TW"**; mục **"Đánh giá"** (Nhóm 8) mở ra chỉ hiện ảnh "Trống" + chữ **"Chưa có thông tin"**; Dòng thời gian ghi **"Hoàn thành 10/07/2026 09:54 Cán bộ NV Trung ương"** → vụ việc ở HOAN_THANH. Không thấy nút chức năng đánh giá.
- Frame chứa vấn đề đối tác báo: mục "Đánh giá" trống + không có nút để thực hiện đánh giá.

### 3 dữ kiện neo (từ evidence + cột sheet)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | **CB NV Trung ương** (CB_NV_TW) mở mục "Đánh giá" của vụ việc **đã "Hoàn thành"** |
| (b) | Hiện tượng đối tác báo (cột "Kết quả thực tế") | Mục "Đánh giá" (Nhóm 8) **không hiện nút chức năng** — chỉ "Chưa có thông tin" |
| (c) | Kỳ vọng đối tác (cột "Kết quả mong đợi") | Có nút/biểu mẫu để đánh giá kết quả hỗ trợ khi vụ việc đã hoàn thành |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh DGKQHTVV_01-2 — CB_NV_TW, vụ việc "Hoàn thành", mục "Đánh giá" (Nhóm 8) trống, không có nút chức năng.
2. **Đối tác phản ánh CỤ THỂ:** không có nút để thực hiện chức năng đánh giá ở Nhóm 8 khi vụ việc đã hoàn thành.
3. **Data + bước tái hiện:** dùng vụ việc HOAN_THANH có CB NV được giao là `cbnv_tw` → mở chi tiết → kiểm thanh hành động (có [Đánh giá]?) + mở Nhóm 8 (có biểu mẫu chấm điểm?) → đối chiếu API đánh giá có tồn tại/cho phép không.

## Bảng đối chiếu điều kiện

→ [`../../cond/DGKQHTVV_01.md`](../../cond/DGKQHTVV_01.md) — **0 GAP**. Đối tác dùng **cùng vai trò CB_NV_TW** + **cùng state HOAN_THANH** + cùng màn "Đánh giá" như mình test → điều kiện trùng khớp hoàn toàn.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

### Yêu cầu: có nút [Đánh giá] + biểu mẫu chấm điểm khi HOAN_THANH cho CB NV

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-17 (UC67) §Preconditions | PRE-02: VV ở **HOAN_THANH** hoặc DA_DANH_GIA; PRE-03: role ∈ **{CB_NV, DN}** | `srs-fr-05-vu-viec.md:1186-1187` |
| FR-V.I-17 §Processing bước 1-2 | Kiểm quyền role ∈ {CB_NV, DN}; scope role='CB_NV' → `VU_VIEC.don_vi_id = current_user.don_vi_id` | `srs-fr-05-vu-viec.md:1204-1205` |
| SCR-V.I-03 §Bảng nút hành động | `HOAN_THANH → [Đánh giá] (CB NV/DN) → Mở Accordion 8. Gửi → DA_DANH_GIA` | `srs-fr-05-vu-viec.md:1740` |
| SCR-V.I-03 Accordion 8 (Đánh giá) | diem_chat_luong/thoi_gian/thai_do (0-10) + diem_tong (auto) + nhan_xet, **"CB NV/DN nhập trực tiếp"**, hiển thị **khi VV ở HOAN_THANH/DA_DANH_GIA** | `srs-fr-05-vu-viec.md:1723` |
| SCR-V.I-03 §Quy ước hiển thị nút | **Đúng vai trò → nút hiển thị**; đúng vai trò nhưng sai state/scope → mờ + tooltip (KHÔNG ẩn hẳn) | `srs-fr-05-vu-viec.md:1747` |

→ App test: `cbnv_tw` (đúng role CB_NV, đúng đơn vị) + vụ việc HOAN_THANH → theo SRS **phải** có nút [Đánh giá] + biểu mẫu Accordion 8. Thực tế **không có nút nào** + Accordion 8 chỉ đọc "Chưa có thông tin". ❌ **Vi phạm** `:1740` + `:1723` + `:1747`.

### Phân loại: lỗi FE (không phải thiếu data, không phải chặn quyền đúng)

- Gọi `POST /api/v1/vu-viecs/{id}/danh-gia` (thân rỗng) → **HTTP 422** `ERR-VAL-SYS-00-01` field `diemChatLuong` *"Điểm chất lượng phải từ 0-10"*. → Endpoint **tồn tại**, và trả **422 validation** (không phải **403 forbidden**) cho chính session `cbnv_tw` → máy chủ **cho phép** tài khoản này đánh giá, chỉ thiếu điểm hợp lệ.
- → Chức năng đánh giá đã có ở BE + BE authorize đúng CB NV; **giao diện thiếu nút + biểu mẫu để gọi** → lỗi phía FE, không phải empty-state thiếu data cũng không phải chặn quyền hợp lệ.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- VV-BTP-TW-20260712-001 (id `8e259653-...`, đơn vị BTP·TW) được đưa lên **HOAN_THANH** (điền kết luận cuối → Xác nhận, `POST .../hoan-thanh` [201]).
- `cbnv_tw` (vai trò `["CB_NV_TW"]`, cấp TW, đơn vị BTP·TW — là CB NV được giao) mở chi tiết:
  - Thanh hành động: **không có** nút [Đánh giá].
  - Mở mục "Đánh giá" (Nhóm 8): chỉ hiện ảnh "Trống" + "Chưa có thông tin", không có ô nhập/nút gửi.
- API probe: `POST .../danh-gia` thân rỗng → 422 "Điểm chất lượng phải từ 0-10" (endpoint tồn tại + authorize tài khoản này).
- Ảnh: `image/DGKQHTVV_01-nhom8-danhgia-trong.png`.

## Verdict

**`Open`** — Lỗi thật (FE). Vụ việc HOAN_THANH + tài khoản đúng vai trò CB NV cùng đơn vị nhưng **giao diện không cung cấp nút [Đánh giá] và biểu mẫu Accordion 8** để đánh giá kết quả hỗ trợ — trái `srs-fr-05-vu-viec.md:1740` (nút [Đánh giá] ở HOAN_THANH) + `:1723` (Accordion 8 CB NV/DN nhập trực tiếp) + `:1747` (đúng vai trò → nút phải hiển thị). Endpoint đánh giá phía máy chủ **tồn tại + cho phép** chính tài khoản này (422 validation, không 403) → xác nhận là lỗi FE thiếu nút/biểu mẫu chứ không phải empty-state thiếu data hay chặn quyền đúng. Điều kiện trùng khớp hoàn toàn với đối tác (cùng CB_NV_TW + HOAN_THANH). Đã log **BUG-DGKQHTVV_01** (Major).
