# Audit — CTTDVQL_03 (row 267) · BC Chương trình theo đơn vị — "bảng thiếu cột Cấp đơn vị"

**Verdict:** Open (bug thật). Bảng thiếu cột "Cấp đơn vị" dù §Output đặc thù yêu cầu và BE đã trả `capDonVi`.

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CTTDVQL_03.jpg` — BC Chương trình theo đơn vị (FR-IX-21 / UC144), đối tác báo bảng dữ liệu thiếu cột "Cấp đơn vị".
- Env test: `cttdvql-table-missing-capdonvi.png` — env `18.143.165.120.nip.io`, `cbnv_tw_01` (Toàn quốc), 21/07/2026, kỳ Năm 2026.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | Xem BC Chương trình theo đơn vị, bảng tổng hợp |
| (b) | Hiện tượng đối tác báo | Bảng thiếu cột "Cấp đơn vị" |
| (c) | Kỳ vọng đối tác | Bảng có cột "Cấp đơn vị" (TW/BN/ĐP) theo đặc tả |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh CTTDVQL_03 — bảng chỉ có 3 cột (Đơn vị / Số CT / Tổng ngân sách).
2. **Đối tác phản ánh CỤ THỂ:** thiếu cột "Cấp đơn vị".
3. **Data + bước tái hiện:** login CB NV TW → BC theo đơn vị → kỳ Năm 2026, Toàn quốc → quan sát các cột của bảng tổng hợp.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

- FR-IX-21 §Output đặc thù (`srs-fr-11-bao-cao.md:943`): trường `cap_don_vi` ("Cấp đơn vị", TW/BN/ĐP) là cột bắt buộc của bảng → App SAI (thiếu cột).

## Kết quả verify trên env được giao

- Bảng chỉ hiển thị 3 cột: **Đơn vị · Số chương trình · Tổng ngân sách**. Cột "Cấp đơn vị" bị thiếu — tái hiện đúng như đối tác.
- API `GET /api/v1/bao-cao/ct-theo-don-vi` ĐÃ trả trường `capDonVi` ("TW") cho từng đơn vị, nhưng FE không render thành cột → lỗi phía FE.
  `{"donViId":"...0001","tenDonVi":"Cục Bổ trợ tư pháp - Bộ Tư pháp","capDonVi":"TW","soCt":1,"tongNganSach":100000000}`
- Ảnh: `cttdvql-table-missing-capdonvi.png`.

## Verdict

**`Open`** — Bug thật, owner `Dev FE`. Bảng thiếu cột "Cấp đơn vị" dù §Output đặc thù FR-IX-21 (`:943`) yêu cầu và BE đã trả `capDonVi`. Đã log: [`../../bug-reports/bctk/Pass-bug-report-bctk-batch4.md`](../../bug-reports/bctk/Pass-bug-report-bctk-batch4.md) (`BUG-CTTDVQL_03`).
