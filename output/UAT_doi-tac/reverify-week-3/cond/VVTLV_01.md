# Bảng đối chiếu điều kiện — VVTLV_01 (row 241) — BC Vụ việc theo lĩnh vực (FR-IX-12)

**Đối tác phản ánh:** "Biểu đồ ≠ bảng tổng hợp" — số trên biểu đồ không khớp số trên bảng tổng hợp.

**Loại bug:** Data accuracy / hiển thị (biểu đồ vs bảng, phụ thuộc data + FE render) → BẮT BUỘC bảng đối chiếu, 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ (xem báo cáo thống kê) | `cbnv_tw_04` (CB_NV_TW, Toàn quốc) — cùng vai trò | Không |
| Loại báo cáo | BC "Vụ việc theo lĩnh vực" (FR-IX-12 / UC135) | BC "Vụ việc theo lĩnh vực", Năm 2026, Toàn quốc | Không |
| Phạm vi đơn vị | Toàn hệ thống | Toàn quốc (TW nhìn toàn hệ thống — có 4 đơn vị trong data) | Không |
| Dữ liệu tiền đề | Có ≥2 đơn vị cùng 1 lĩnh vực (mới thấy chênh biểu đồ vs bảng) | Lĩnh vực "Thương mại" có **4 đơn vị**: Cục Bổ trợ 7, Bộ KH&ĐT 4, STP HN 2, STP AG 3 = tổng 16 | Không |
| Thành phần so sánh | Biểu đồ vs bảng tổng hợp | Đọc **cả biểu đồ (tooltip)** và **bảng** trên cùng 1 lần xem báo cáo | Không |

**Kết luận:** 0 GAP. Cùng vai trò, cùng báo cáo, cùng phạm vi; data có 1 lĩnh vực nhiều đơn vị (điều kiện cần để lộ chênh lệch). So trực tiếp biểu đồ vs bảng.

**Đo 2 phương pháp (bug candidate ≠ bug):**

- **UI — biểu đồ (tooltip):** biểu đồ cột chỉ có **1 chuỗi legend** = "Cục Bổ trợ tư pháp - Bộ Tư pháp". Hover cột "Thương mại" → tooltip **"Thương mại — Cục Bổ trợ tư pháp - Bộ Tư pháp : 7"**. DOM: `.recharts-bar` = 1 series, 2 cột (Thuế h≈30px, Thương mại h≈210px). → biểu đồ chỉ vẽ dữ liệu **1 đơn vị (Cục Bổ trợ)**, Thương mại = **7**.
- **UI — bảng tổng hợp:** 2 cột `["Lĩnh vực PL","Tổng số"]` → Thuế = 1, **Thương mại = 16** (tổng toàn bộ đơn vị).
- **API** `GET /api/v1/bao-cao/vu-viec-theo-linh-vuc` (cùng kỳ/phạm vi): `theoLinhVuc[].theoDonVi[]` cho "Thương mại" = 4 đơn vị (Cục Bổ trợ 7 + Bộ KH&ĐT 4 + STP HN 2 + STP AG 3 = 16), `tongSo:16`, `tongBanGhi:17`, `chartType:"GROUPED_BAR"`. → BE **có đủ** 4 đơn vị.
- → Biểu đồ (Thương mại = 7, 1 đơn vị) **KHÔNG khớp** bảng (Thương mại = 16). Data BE đủ 4 đơn vị nhưng FE dựng biểu đồ chỉ 1 chuỗi đơn vị (Cục Bổ trợ) → chênh 7 vs 16, đúng như đối tác phản ánh. Đây là lỗi FE render biểu đồ, không phải bug candidate.

**SRS:**
- `srs-fr-11-bao-cao.md:619` — §Output FR-IX-12: `theo_don_vi[] = {don_vi, ten, so_luong}` (trường **Luôn**).
- `srs-fr-11-bao-cao.md:622` — AC: "cross-tab: hàng = lĩnh vực, cột = đơn vị".
- `srs-fr-11-bao-cao.md:1071` — Mapping SCR-IX-01: biểu đồ **Grouped bar** (nhóm lĩnh vực × nhiều đơn vị, mỗi đơn vị 1 chuỗi).

**Verdict: Open** — biểu đồ chỉ vẽ 1 đơn vị (Cục Bổ trợ, Thương mại = 7) trong khi bảng tổng hợp là 16 (toàn bộ 4 đơn vị) → biểu đồ ≠ bảng, không dựng đúng Grouped bar cross-tab theo §Output/AC FR-IX-12.

> **Lưu ý trùng lặp:** Đây là **cùng gốc lỗi** với **BUG-VVTLV_03** đã log ở `bug-reports/bctk/Pass-bug-report-bctk-batch3.md` (row 242 — "thiếu breakdown theo đơn vị ở cả bảng và biểu đồ; biểu đồ chỉ 1 chuỗi, cột Thương mại ~7 ≠ tổng 16"). VVTLV_01 (biểu đồ ≠ bảng) là **triệu chứng** của cùng defect đó. → Verdict Open, **tham chiếu BUG-VVTLV_03, KHÔNG log bug mới trùng.**
