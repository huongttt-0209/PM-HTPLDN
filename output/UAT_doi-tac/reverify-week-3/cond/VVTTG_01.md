# Bảng đối chiếu điều kiện — VVTTG_01 (row 213) — BC Vụ việc theo thời gian (FR-IX-05)

**Đối tác phản ánh:** "Số liệu thống kê không chính xác" — con số hiển thị trên BC Vụ việc theo thời gian không đúng.

**Loại bug:** Data accuracy (phụ thuộc data + công thức §Output) → BẮT BUỘC bảng đối chiếu, 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ (xem báo cáo thống kê) | `cbnv_tw_04` (CB_NV_TW, phạm vi Toàn quốc) — cùng vai trò xem báo cáo | Không |
| Entity + loại báo cáo | BC "Vụ việc theo thời gian" (FR-IX-05 / UC128) | BC "Vụ việc theo thời gian", Năm & Tháng, Toàn quốc | Không |
| Kỳ báo cáo | Trend theo thời gian | Đo cả kỳ **Năm** (1 điểm 2026) và **Tháng** (12 điểm T01–T12) cùng range 01/01→31/12/2026 | Không |
| Phạm vi đơn vị | Toàn hệ thống | Toàn quốc (TW nhìn toàn hệ thống) | Không |
| Dữ liệu tiền đề | Có vụ việc phát sinh trong kỳ | Có 14 VV tiếp nhận + 5 VV hoàn thành trong 2026 (data đủ để 2 chuỗi khác 0) | Không |

**Kết luận:** 0 GAP. Cùng vai trò, cùng báo cáo, cùng phạm vi, có dữ liệu. Đo được số liệu hiển thị và so với công thức §Output.

**Đo 2 phương pháp (bug candidate ≠ bug):**

- **UI:** Loại BC = "BC Vụ việc theo thời gian", Kỳ = Năm 2026, Đơn vị = Toàn quốc → thẻ "Tổng vụ việc toàn kỳ = **6**", biểu đồ đường **1 chuỗi duy nhất "Số vụ việc"**, không có nhãn tiếp nhận/hoàn thành, không có bảng chi tiết. (Evidence: `reverify-audit/VVTTG_01/vvttg-report-nam-kpi6.png`.)
- **API** `GET /api/v1/bao-cao/vu-viec-theo-thoi-gian` (cùng kỳ/phạm vi):
  - Năm: `tongVuViecToanKy: 6`, `data:[{kyLabel:"2026", soVuViec:6}]`, `chartType:"LINE"` — chỉ có trường `soVuViec`, **KHÔNG có `tiepNhan`/`hoanThanh`**.
  - Tháng: `data` 12 điểm, `soVuViec` T01=1, T02=1, T03=2, T04=1, T07=1, còn lại 0 → tổng = 6. (Nội bộ nhất quán KPI = biểu đồ = tổng cột.)
- → UI khớp API (đều là 1 con số `soVuViec` = 6). Không phải lỗi render tình cờ; là bản chất dữ liệu BE trả về.

**Đối chiếu công thức §Output — số 6 khớp với chỉ số nào?**

SRS FR-IX-05 §Output (dòng 337) yêu cầu `trend_data[] = {ky_label, tiep_nhan, hoan_thanh}` — mỗi kỳ phải có **2 chỉ số**: số vụ việc *tiếp nhận* và số *hoàn thành*. BE đang trả 1 chỉ số `soVuViec` không rõ định nghĩa. Đo trực tiếp 2 chỉ số SRS yêu cầu (cùng kỳ Năm 2026, Toàn quốc) — bảng đối chiếu chi tiết ở `reverify-audit/VVTTG_01/reconciliation.md`:

- **Tổng năm 2026:** `soVuViec` (VVTTG) = **6** · tiếp nhận (`vu-viec-tiep-nhan`) = **14** · hoàn thành (`vu-viec-hoan-thanh`) = **5**.
- **Breakdown tháng** — `soVuViec`: T01=1, T02=1, T03=2, T04=1, T07=1. Tiếp nhận: T01=1, T02=2, T03=2, T04=1, T07=8. Hoàn thành: T02=1, T03=2, T04=1, T07=1.
- Số hiển thị `soVuViec = 6` **KHÔNG khớp** tiếp nhận (14) cũng **KHÔNG khớp** hoàn thành (5). Lệch rõ nhất ở T07: báo cáo hiện 1 trong khi thực tế tiếp nhận 8.
- BE **có đủ dữ liệu** cả 2 chuỗi (2 endpoint `vu-viec-tiep-nhan` = 14 và `vu-viec-hoan-thanh` = 5 trả về bình thường) nhưng báo cáo "theo thời gian" lại gộp về 1 con số không thuộc chỉ số nào SRS định nghĩa → người xem không biết 6 là gì → đúng như đối tác cảm nhận "số liệu không chính xác".

**SRS:**
- `srs-fr-11-bao-cao.md:337` — §Output đặc thù FR-IX-05: `trend_data[] | structured | Luôn | {ky_label, tiep_nhan, hoan_thanh}`.
- `srs-fr-11-bao-cao.md:338` — `theo_don_vi[] | {don_vi, ten, trend_data[]}` (bảng chi tiết theo đơn vị — cũng thiếu).
- `srs-fr-11-bao-cao.md:342` — AC: "hiển thị biểu đồ trend + **bảng chi tiết**".

**Verdict: Open** — báo cáo lệch §Output FR-IX-05: trả 1 chỉ số `soVuViec` (=6, không khớp tiếp nhận 14 hay hoàn thành 5) thay vì 2 chuỗi `{tiep_nhan, hoan_thanh}` theo đặc tả.

> **Lưu ý trùng lặp:** Đây là **cùng gốc lỗi** với **BUG-VVTTG_03** đã log ở `bug-reports/bctk/Pass-bug-report-bctk-batch1.md` (row 215 — "biểu đồ trend chỉ 1 chuỗi, thiếu tiếp nhận/hoàn thành + không có bảng theo đơn vị"). VVTTG_01 (số liệu không chính xác) là **triệu chứng** của cùng defect cấu trúc đó. → Verdict Open, **tham chiếu BUG-VVTTG_03, KHÔNG log bug mới trùng.**
