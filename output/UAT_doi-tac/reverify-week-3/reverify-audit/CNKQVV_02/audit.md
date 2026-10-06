# Audit — CNKQVV_02 (row 13) · Cập nhật kết quả cuối / Hoàn thành vụ việc — "tên nút + trường thông tin không giống thiết kế"

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CNKQVV_02.jpg` (`fetch_evidence.py --row 13`). Ảnh (env đối tác `htpldn-uat.ospgroup.vn`): modal **"Hoàn thành vụ việc"** với 2 trường **"Kết luận cuối cùng"** (0/5000) + **"Kết quả xử lý"** (radio Thành công/Không thành công), nút trigger **"Hoàn thành"**, nút gửi trong modal.
- Frame chứa vấn đề đối tác báo: modal hoàn thành có tên nút + các trường mà đối tác cho là "không giống với thiết kế".

### 3 dữ kiện neo (từ evidence + cột sheet)

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | CB nghiệp vụ mở chức năng cập nhật kết quả cuối / hoàn thành vụ việc (vụ việc "Đã duyệt") |
| (b) | Hiện tượng đối tác báo (cột "Kết quả thực tế") | **Tên nút chức năng và các trường thông tin không giống với thiết kế** |
| (c) | Kỳ vọng đối tác (cột "Kết quả mong đợi") | Hiển thị đúng tên nút + các trường theo thiết kế, đồng nhất ngôn ngữ, không tràn/đè |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh CNKQVV_02 — modal "Hoàn thành vụ việc" (Kết luận cuối cùng + Kết quả xử lý), nút "Hoàn thành".
2. **Đối tác phản ánh CỤ THỂ:** tên nút + tập trường của modal khác so với thiết kế (không nêu rõ thiết kế là bản nào).
3. **Data + bước tái hiện:** vụ việc ở "Đã duyệt" → login CB NV được giao → bấm nút hành động mở modal → đọc tên nút, tiêu đề modal, danh sách trường → đối chiếu FR-V.I-16 (SCR-V.I-03 Accordion 6 + bảng nút hành động).

## Bảng đối chiếu điều kiện

→ [`../../cond/CNKQVV_02.md`](../../cond/CNKQVV_02.md) — **0 GAP** về role/state/data. Đã test đúng vai trò (CB NV được giao) + đúng state ("Đã duyệt") + đúng modal đối tác chụp.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

### Nút hành động ("tên nút")

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-16 AC | "**When** nhấn **'Cập nhật kết quả cuối'** **Then** VV → HOAN_THANH" | `srs-fr-05-vu-viec.md:1167` |
| SCR-V.I-03 bảng nút hành động | `DA_DUYET → [Cập nhật KQ cuối] (CB NV) → HOAN_THANH` | `srs-fr-05-vu-viec.md:1739` |

→ App test: nút hành động = **"Hoàn thành"**, tiêu đề modal = **"Hoàn thành vụ việc"**, nút gửi = **"Xác nhận"**, endpoint `POST /api/v1/vu-viecs/{id}/hoan-thanh` [201]. **Lệch tên** so với đặc tả ("Cập nhật kết quả cuối"). Nhưng "Hoàn thành" khớp đúng transition state (→ HOAN_THANH) và rõ nghĩa — **có thể là quyết định thiết kế cố ý**, không chắc là lỗi.

### Trường thông tin ("các trường")

| Nguồn SRS v3.5 | Yêu cầu | Vị trí |
|---|---|---|
| FR-V.I-16 Inputs | Chỉ 1 trường người dùng nhập: **`ket_luan_cuoi`** (text long, bắt buộc) | `srs-fr-05-vu-viec.md:1136-1140` |
| SCR-V.I-03 Accordion 6 (Kết quả Hỗ trợ) | noi_dung_ket_qua, file_ket_qua, **ket_luan_cuoi**, ngay_hoan_thanh | `srs-fr-05-vu-viec.md:1721` |

→ App test: modal có **"Kết luận cuối cùng"** (= `ket_luan_cuoi` ✅ khớp) + **"Kết quả xử lý (Thành công/Không thành công)"** (KHÔNG có trong Inputs FR-V.I-16). Trường "Kết quả xử lý" ánh xạ field `ketQuaXuLy` có sẵn trong mô hình dữ liệu VU_VIEC → **hợp lý về nghiệp vụ** (ghi nhận kết quả xử lý), có thể là bổ sung thiết kế cố ý.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- VV-BTP-TW-20260712-001 (id `8e259653-...`, đơn vị BTP·TW, DA_DUYET). `cbnv_tw` (CB NV được giao) bấm nút **"Hoàn thành"** → modal **"Hoàn thành vụ việc"**: trường **"Kết luận cuối cùng"** (bắt buộc, 0/5000) + **"Kết quả xử lý"** (radio Thành công/Không thành công) + nút **"Hủy"/"Xác nhận"**.
- Điền kết luận + chọn "Thành công" → Xác nhận → `POST .../hoan-thanh` [201], vụ việc → **"Hoàn thành"**. Chức năng chạy đúng.
- Modal app **giống hệt** frame đối tác chụp (CNKQVV_02.jpg) → đối tác so sánh chính modal này với "thiết kế".
- Ảnh: `image/CNKQVV_02-modal-hoan-thanh.png`.

## Verdict

**`BA confirm`** — cập nhật 2026-07-20 (mới nhất): gộp về **1 trạng thái `BA confirm`** (bỏ dual `Open, BA confirm`) theo yêu cầu — case bản chất là câu hỏi thiết kế chờ BA; nếu BA chốt sửa app → dev fix theo `BUG-CNKQVV_02`.

- **Lệch đặc tả (đối tác phản ánh đúng):** App **lệch** so với đặc tả v3.5 (FR-V.I-16) — bản đặc tả được chỉ định làm chuẩn chấm — ở 2 điểm: (1) tên nút "Hoàn thành" / modal "Hoàn thành vụ việc" vs đặc tả "Cập nhật kết quả cuối" (`:1167`, `:1739`); (2) trường "Kết quả xử lý (Thành công/Không thành công)" không nằm trong Inputs FR-V.I-16 (`:1136-1140`). Đối tác phản ánh ĐÚNG là "khác thiết kế" → ghi nhận lệch đặc tả = `BUG-CNKQVV_02` (describe lệch, KHÔNG prescribe hướng sửa).
- **⚠️ CẦN BA CONFIRM:** cả 2 điểm đều nhẹ + hợp lý (tên rõ nghĩa theo transition → HOAN_THANH; trường ánh xạ field `ketQuaXuLy` có sẵn trong mô hình dữ liệu) → có thể là quyết định thiết kế cố ý; không có nguồn thiết kế uy tín (Figma) để khẳng định app SAI. → BA chốt hướng: giữ theo app (cập nhật đặc tả) hay sửa app theo đặc tả. Chi tiết: mục CNKQVV_02 trong [`../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md`](../../ba-confirm/vu-viec/ba-confirmation-needed-vu-viec.md).
