# LCNHTCVV_02 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị cửa sổ "Phân công xử lý vụ việc" — thẻ "Cá nhân" (SCR-V.I-03 modal Phân công · FR-V.I-09 UC59).

**Evidence đối tác:** `partner-evidence/LCNHTCVV_02.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/71cb2ab1-...`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**, VV đang ở trạng thái cho phép phân công (thanh hành động có [Phân công] + [Kiểm tra lại]).
Cửa sổ **"Phân công tư vấn viên"** đã mở, thẻ **"Cá nhân"** đang chọn. Phần gợi ý là **1 ô danh sách xổ xuống (dropdown)**, mỗi dòng là **một chuỗi chữ gộp**:
`[TVV] Chuyên gia Nguyễn Văn A (TVV-MOCK-999) — 0 VV đang xử lý` · `[NHT] hương 2 nht (NHT-BTP-TW-0011) — 0 VV đang xử lý` · `[TVV] TVV R11 Verify Mail Fix (TVV-BTP-TW-0032) — 4 VV đang xử lý — ĐG: 8.3` …
⇒ **KHÔNG phải bảng có cột**; mỗi dòng chỉ có: loại · họ tên · mã · số VV đang xử lý · (đôi khi) điểm ĐG.

**Đối tác phản ánh:** **Bảng gợi ý ở thẻ "Cá nhân" không giống với thiết kế.**

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Entity + trạng thái (state machine) | VV có nút [Phân công] + [Kiểm tra lại] ⇒ đang ở **"Đang kiểm tra"** (đã kết luận kiểm tra Đạt) | `VV-BTP-TW-20260712-005` (cùng đơn vị TW) — seed sang **"Đang kiểm tra"** (Kiểm tra hồ sơ 6/6 Đạt), thanh hành động có [Phân công] + [Kiểm tra lại] (VV-003 gốc nay đã "Đã phân công") | Không |
| Dữ liệu tiền đề (pool gợi ý phải CÓ người) | Danh sách gợi ý có **≥8 người** (TVV + NHT) → đủ dữ liệu để bảng hiển thị các cột | Pool gợi ý có **2 TVV** (`QA TVV Seed28 Active`, `Nguyễn Văn Seed`) — **có dữ liệu**, trong đó 1 người có điểm ĐG (4.2) và cả 2 đều có lĩnh vực + đơn vị quản lý trong DB ⇒ đủ điều kiện để các cột SRS hiển thị nếu chúng tồn tại | Không |
| Thẻ đang chọn trong cửa sổ | Thẻ **"Cá nhân"** | Thẻ **"Cá nhân"** (mặc định được chọn) | Không |

## Quan sát (real-data) — cbnv_tw, cửa sổ "Phân công tư vấn viên", thẻ "Cá nhân"

**Vòng 1 (bug gốc):**
```json
{"truong_thieu": ["Lĩnh vực chuyên môn", "Đơn vị quản lý", "Điểm ưu tiên"]}
```

**Re-test 2026-07-15 (sau dev fix):**
```json
{"cac_dong_goi_y": [
   "[TVV] QA TVV Seed28 Active (TVV-BTP-TW-0002) · LV: Thương mại · ĐVQL: Cục Bổ trợ tư pháp - Bộ Tư pháp · Ưu tiên: 2 · 0 VV đang xử lý · ĐG: 4.2",
   "[TVV] Nguyễn Văn Seed (TVV-SEED-0001) · LV: Thương mại · ĐVQL: Cục Bổ trợ tư pháp - Bộ Tư pháp · Ưu tiên: 2 · 0 VV đang xử lý"],
 "truong_da_bo_sung": {"LV (Lĩnh vực chuyên môn)": "có", "ĐVQL (Đơn vị quản lý)": "có", "Ưu tiên (Điểm ưu tiên)": "có"}}
```
→ **PASS:** mỗi dòng gợi ý nay có đủ 3 trường trước thiếu — LV (Lĩnh vực), ĐVQL (Đơn vị quản lý), Ưu tiên (Điểm ưu tiên) — kèm workload + ĐG.

Ảnh: `../../bug-reports/image/BUG-LCNHTCVV_02-retest-pool-co-linhvuc-donvi-uutien.png`

## Đối chiếu SRS (Cổng 3)

**SRS yêu cầu** — `srs-fr-05-vu-viec.md:750-758` (FR-V.I-09 / UC59 §Outputs): danh sách gợi ý người xử lý phải xuất **9 trường**, trong đó các trường hiển thị cho cán bộ chọn người gồm:

- dòng **752** `ho_ten_nguoi_xu_ly` (Họ tên) → web **CÓ** ✔
- dòng **754** `linh_vuc` — *"Lĩnh vực chuyên môn"* → web **THIẾU** ✘
- dòng **755** `don_vi_quan_ly` — *"Đơn vị quản lý (Sở TP/Bộ ngành công nhận)"* → web **THIẾU** ✘
- dòng **756** `workload` — *"Số VV đang xử lý"* → web **CÓ** ✔
- dòng **757** `diem_danh_gia` — *"Điểm đánh giá TB (thang 1.0–5.0)"* → web **CÓ (một phần)** — chỉ hiện khi TVV có điểm, người chưa có điểm thì không hiển thị gì
- dòng **758** `diem_uu_tien` — *"Điểm ưu tiên tính toán"* → web **THIẾU** ✘

**Hệ quả nghiệp vụ:** `srs-fr-05-vu-viec.md:735-741` (§Processing — Gợi ý người xử lý, BR-CALC-07) quy định danh sách được **sắp xếp theo điểm ưu tiên DN (NĐ55 Điều 4) giảm dần → workload tăng dần → điểm ĐG giảm dần**. Do web **không hiển thị Điểm ưu tiên và Lĩnh vực chuyên môn**, cán bộ **không có căn cứ nào để đối chiếu** vì sao người này được gợi ý trước người kia, cũng không biết người được gợi ý có đúng lĩnh vực của vụ việc hay không.

**Kết luận:** Vùng gợi ý ở thẻ "Cá nhân" **thiếu 3/6 trường thông tin SRS quy định** (Lĩnh vực chuyên môn · Đơn vị quản lý · Điểm ưu tiên) và trình bày dạng chuỗi chữ gộp trong dropdown thay vì bảng có cột → **Open**.

> Ghi chú: chi tiết "ĐG: 8.3" trong ảnh đối tác (vượt thang 1.0–5.0 mà SRS dòng 757 quy định) **KHÔNG tái hiện** trên env được giao — env này hiển thị "ĐG: 4.2" (đúng thang). Không log thành lỗi ở lượt này.
