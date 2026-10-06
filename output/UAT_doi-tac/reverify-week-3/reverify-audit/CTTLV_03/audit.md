# Audit — CTTLV_03 (row 271) · BC Chương trình theo lĩnh vực — "KPI thừa"

**Verdict:** BA confirm. App có thẻ chỉ số tổng hợp mà §Output đặc thù không liệt kê → tranh chấp đặc tả (specific vs template chung).

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CTTLV_03.jpg` — BC Chương trình theo lĩnh vực (FR-IX-22 / UC145), đối tác cho là thẻ chỉ số (KPI card) thừa so với đặc tả.
- Env test: `cttlv-report-thuongmai-kpi.png` — env `18.143.165.120.nip.io`, `cbnv_tw_01` (Toàn quốc), 21/07/2026, kỳ Năm 2026.

### 3 dữ kiện neo

| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | Xem BC Chương trình theo lĩnh vực |
| (b) | Hiện tượng đối tác báo | Báo cáo hiển thị thẻ chỉ số tổng hợp ("KPI thừa") |
| (c) | Kỳ vọng đối tác | Không có thẻ chỉ số tổng hợp riêng cho báo cáo này |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh CTTLV_03 — báo cáo có khối thẻ chỉ số phía trên biểu đồ/bảng.
2. **Đối tác phản ánh CỤ THỂ:** thẻ chỉ số tổng hợp không có trong đặc tả của báo cáo này.
3. **Data + bước tái hiện:** login CB NV TW → BC theo lĩnh vực → kỳ Năm 2026, Toàn quốc → quan sát khối thẻ chỉ số.

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

- FR-IX-22 §Output đặc thù (`srs-fr-11-bao-cao.md:979-984`): chỉ liệt kê cột bảng (`linh_vuc_id`, `ten_linh_vuc`, `so_ct`, `so_dn_tham_gia`), KHÔNG liệt kê thẻ chỉ số tổng hợp riêng.
- Template chung TPL-REPORT-FULL (`srs-fr-11-bao-cao.md:100`) CÓ trường `tong_ban_ghi` ("Tổng số bản ghi") — có thể được FE hiện thực hoá thành thẻ chỉ số.
- SRS không cấm rõ ràng thẻ chỉ số → cần BA chốt source truth.

## Kết quả verify trên env được giao

- Báo cáo hiển thị **2 thẻ chỉ số**: "Tổng chương trình" + "Tổng DN tham gia" phía trên biểu đồ Bar + bảng theo lĩnh vực. Hiện tượng tái hiện đúng như đối tác phản ánh.
- Ảnh: `cttlv-report-thuongmai-kpi.png`.

## Verdict

**`BA confirm`** — App hiển thị thẻ chỉ số tổng hợp mà §Output đặc thù FR-IX-22 không liệt kê, nhưng Template chung TPL-REPORT-FULL có trường tổng hợp. SRS mâu thuẫn (specific vs template) → BA chốt: giữ (theo template chung) hay bỏ (theo output đặc thù). Chi tiết: [`../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch4.md`](../../ba-confirm/bctk/ba-confirmation-needed-bctk-batch4.md).
