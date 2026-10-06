# Bảng đối chiếu điều kiện — VVTLV_03

Loại bug: **hiển thị phụ thuộc dữ liệu** (bảng cross-tab + biểu đồ nhóm chỉ render đúng khi kỳ/đơn vị có ≥2 đơn vị có dữ liệu) → điền bảng, chỉ kết luận khi 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh: "Quản trị viên · QTHT" (admin), nhưng dropdown Đơn vị = **Toàn quốc** (phạm vi rộng nhất) | `cbnv_tw` (CB Nghiệp vụ - Trung ương, CB_NV_TW) — phạm vi **Toàn quốc**, đúng vai trò verdict, quét cùng scope Toàn quốc | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | URL: `loai=vu-viec-theo-linh-vuc&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`, Đơn vị Toàn quốc | Chọn đúng "BC Vụ việc theo lĩnh vực", Kỳ Năm 01/01/2026 → 31/12/2026, Đơn vị Toàn quốc (URL trùng khớp) | Không |
| Dữ liệu tiền đề (nhiều đơn vị/lĩnh vực) | Bảng đối tác có nhiều lĩnh vực (Dân sự 2, Đất đai 5, Đầu tư 2, Doanh nghiệp 20…), chart legend chỉ 1 đơn vị "Sở Tư pháp Bắc Giang" | Env có 17 vụ việc / 2 lĩnh vực; riêng "Thương mại" tổng 16 phân bổ **4 đơn vị** (Cục Bổ trợ 7, Bộ KH&ĐT 4, STP Hà Nội 2, STP An Giang 3) — API trả đủ `theoDonVi[]` | Không |

**Kết luận: 0 GAP.** Điều kiện đối tác được tái lập bằng test thật đúng phạm vi Toàn quốc + đúng filter. Env test còn có ưu thế: dữ liệu "Thương mại" trải trên 4 đơn vị nên nếu FE dựng đúng cross-tab thì bảng phải có ≥4 cột đơn vị + chart phải có ≥4 chuỗi — thực tế UI chỉ render 1 cột "Tổng số" và 1 chuỗi đơn vị → lỗi hiển thị, không phải thiếu seed.

**Đo lường trực tiếp (env test):**
- DOM bảng: `tableHeaders = ["Lĩnh vực PL","Tổng số"]` (2 cột, thiếu breakdown đơn vị).
- DOM chart legend: `["Cục Bổ trợ tư pháp - Bộ Tư pháp"]` (1 chuỗi); 3 đơn vị còn lại **không xuất hiện** trong trang (`inPage=false`).
- API `GET /api/v1/bao-cao/vu-viec-theo-linh-vuc` (200): trả `chartType:"GROUPED_BAR"` + đủ `theoDonVi[]` cho từng lĩnh vực (Thương mại: 4 đơn vị) → BE có data, FE bỏ render.

Chi tiết đối chiếu §Output FR-IX-12 + Mapping SCR-IX-01: xem [`../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`](../bug-reports/bctk/Pass-bug-report-bctk-batch3.md) §BUG-VVTLV_03.
