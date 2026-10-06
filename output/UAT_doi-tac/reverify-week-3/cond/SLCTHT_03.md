# Bảng đối chiếu điều kiện — SLCTHT_03

Loại bug: **hiển thị phụ thuộc dữ liệu** (khu Chỉ số tổng hợp chỉ render khi có ≥1 chương trình) → điền bảng, 0 GAP. Verdict = **Open** (thiếu 2 chỉ số so §Output FR-IX-20 dòng 908-909).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc** (vai trò verdict theo SESSION); cấu trúc khu Chỉ số độc lập role | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Số lượng chương trình hỗ trợ", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Số lượng chương trình hỗ trợ", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chương trình HTPLDN) | 5 CT (4 Đang thực hiện + 1 Hoàn thành) | Đã **seed qua API** 1 CT `DANG_THUC_HIEN` + 1 CT `HOAN_THANH` (+ CT có sẵn `DA_DUYET`) → tongCt=4, đủ render khu Chỉ số | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data (≥1 CT mọi trạng thái) → khu Chỉ số tổng hợp render. Cả 2 env đều chỉ hiện **1 thẻ "Tổng chương trình"**, thiếu thẻ "Đang thực hiện" + "Hoàn thành".

**Đo lường trực tiếp (env test, verify UI role cbnv_tw):**
- Khu Chỉ số tổng hợp: chỉ 1 thẻ "Tổng chương trình = 4". Không có thẻ Đang thực hiện / Hoàn thành.
- SRS §Output FR-IX-20 (`srs-fr-11-bao-cao.md:907-909`): `tong_ct` + `dang_thuc_hien` + `hoan_thanh`, cả 3 điều kiện **"Luôn"** → app thiếu 2 → vi phạm rõ → **Open**.
- Dữ liệu seed qua API (`/api/v1/chuong-trinh-htpls` + chuỗi transition); verdict lấy từ **màn hình UI** đã render, không từ API.

Chi tiết bug: [`../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`](../bug-reports/bctk/Pass-bug-report-bctk-batch3.md) §BUG-SLCTHT_03.
