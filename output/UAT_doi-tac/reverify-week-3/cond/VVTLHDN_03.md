# Bảng đối chiếu điều kiện — VVTLHDN_03

Loại bug: **hiển thị phụ thuộc dữ liệu** (bảng cross-tab + biểu đồ nhóm cần kỳ/đơn vị có ≥2 đơn vị có dữ liệu) → điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc**, đúng vai trò verdict | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Vụ việc theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Vụ việc theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (nhiều đơn vị) | Chart đối tác grouped bar 5 đơn vị × 3 loại hình (Nhỏ/Siêu nhỏ/Vừa); bảng Nhỏ 21, Siêu nhỏ 21, Vừa 5 | Env có 17 vụ việc / 2 loại hình; "Siêu nhỏ" tổng 14 phân bổ **3 đơn vị** (Cục Bổ trợ 8, Bộ KH&ĐT 4, STP Hà Nội 2) — API trả đủ `theoDonVi[]` | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter. Env test có "Siêu nhỏ" trải 3 đơn vị → nếu FE dựng đúng cross-tab thì bảng phải có cột đơn vị + chart phải có ≥3 chuỗi cho Siêu nhỏ. Thực tế bảng chỉ 1 cột "Tổng số" và chart chỉ 1 chuỗi (Sở Tư pháp An Giang) → lỗi hiển thị, không phải thiếu seed.

**Đo lường trực tiếp (env test):**
- DOM bảng: `tableHeaders = ["Quy mô DN","Tổng số"]` (2 cột, thiếu breakdown đơn vị).
- DOM chart legend: `["Sở Tư pháp An Giang"]` (1 chuỗi); chart chỉ có 1 cột "Nhỏ"=3, cột "Siêu nhỏ" trống dù bảng Siêu nhỏ=14 (vì chỉ vẽ dữ liệu đơn vị An Giang).
- API `GET /api/v1/bao-cao/vu-viec-theo-loai-dn` (200): trả `chartType:"GROUPED_BAR"` + `theoDonVi[]` (Siêu nhỏ 3 đơn vị) → BE có data, FE bỏ render.

Chi tiết đối chiếu §Output FR-IX-13 + Mapping: xem [`../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`](../bug-reports/bctk/Pass-bug-report-bctk-batch3.md) §BUG-VVTLHDN_03.
