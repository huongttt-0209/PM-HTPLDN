# Bảng đối chiếu điều kiện — SLCTHT_04

Loại bug: **hiển thị phụ thuộc dữ liệu** (biểu đồ + bảng chỉ render khi có ≥1 chương trình) → điền bảng, 0 GAP. Verdict = **Open** (biểu đồ/bảng theo trạng thái, thiếu chiều đơn vị + kỳ so §Output FR-IX-20 dòng 910-911 + Mapping 1079).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc**; cấu trúc biểu đồ/bảng độc lập role | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Số lượng chương trình hỗ trợ", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Số lượng chương trình hỗ trợ", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chương trình HTPLDN nhiều trạng thái) | 5 CT (4 Đang thực hiện + 1 Hoàn thành) | Đã **seed qua API** 1 CT `DANG_THUC_HIEN` + 1 CT `HOAN_THANH` (+ `DA_DUYET`) → 3 trạng thái hiện trên biểu đồ/bảng | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data nhiều trạng thái → biểu đồ + bảng render. Cả 2 env: biểu đồ + bảng đều theo **trạng thái**, không theo đơn vị/kỳ.

**Đo lường trực tiếp (env test, verify UI role cbnv_tw):**
- Biểu đồ cột: trục hoành = 3 trạng thái (Đã phê duyệt / Đang thực hiện / Hoàn thành) → theo trạng thái, KHÔNG theo đơn vị.
- Biểu đồ đường: trục hoành cũng = 3 trạng thái → theo trạng thái, KHÔNG theo kỳ thời gian.
- Bảng: chỉ 2 cột {Trạng thái, Số chương trình} (Đã phê duyệt 2, Đang thực hiện 1, Hoàn thành 1) → thiếu cột Đơn vị + Đang thực hiện/Hoàn thành theo đơn vị.
- SRS §Output FR-IX-20 (`srs-fr-11-bao-cao.md:910-911`): `theo_don_vi[]` + `theo_ky[]` (đều "Luôn"); Mapping (`:1079`) "Bar + Trend" (cột theo đơn vị + đường theo kỳ) → app sai chiều → **Open**.
- Network `so-luong-ct-ho-tro` trả `data[]` gom theo trạng thái, không có `theoDonVi/theoKy` → lỗi cả BE contract + FE. Verdict lấy từ **màn hình UI**.

Chi tiết bug: [`../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`](../bug-reports/bctk/Pass-bug-report-bctk-batch3.md) §BUG-SLCTHT_04.
