# Audit — CTTLV_04 (row 272) · BC Chương trình theo lĩnh vực — "Dữ liệu hiển thị 'Không xác định'"

**Verdict: BA confirm.** Hiện tượng "Không xác định" **tái hiện đúng** (chương trình chưa gán lĩnh vực) — đối tác quan sát chính xác, KHÔNG phải bất đồng về thực tế. Tranh chấp nằm ở ĐẶC TẢ: SRS mâu thuẫn nội bộ (báo cáo gom theo lĩnh vực nhưng entity chương trình không có trường lĩnh vực) + SRS im lặng về cách xử lý CT chưa gán lĩnh vực → cần BA chốt.

> ⚠️ **Đính chính so với audit round trước:** Bản cũ verdict `Reject` với lý do "'Không xác định' là nhãn đúng, đề nghị đối tác gán lĩnh vực". Sai ở chỗ: (1) hiện tượng TÁI HIỆN nên không thuộc định nghĩa Reject (Reject = lỗi cụ thể KHÔNG tái hiện); (2) "đề nghị đối tác gán lĩnh vực" bất khả thi — form tạo chương trình theo SRS KHÔNG có trường lĩnh vực. Đây là tranh chấp đặc tả → BA confirm.

## Cổng 1 — Bằng chứng (ĐÓNG)

- File đối tác: `partner-evidence/CTTLV_04.jpg` — full-res. Env đối tác, tài khoản admin (QTHT), báo cáo **BC Chương trình theo lĩnh vực** (FR-IX-22 / UC145). Đối tác thấy biểu đồ + bảng chỉ có nhóm **"Không xác định"** và cho là dữ liệu hiển thị sai.

### 3 dữ kiện neo
| # | Dữ kiện | Giá trị |
|---|---|---|
| (a) | Điều kiện đối tác | Xem BC Chương trình theo lĩnh vực; chương trình trong kỳ chưa gán lĩnh vực |
| (b) | Trạng thái entity | Báo cáo hiển thị nhóm lĩnh vực trên biểu đồ + bảng |
| (c) | Hiện tượng đối tác báo | Biểu đồ/bảng hiển thị nhóm **"Không xác định"**, đối tác cho là sai |

## Cổng 2 — Hiểu bug (3 dòng)

1. **Evidence đã xem:** ảnh CTTLV_04 — biểu đồ + bảng CT theo lĩnh vực chỉ có nhóm "Không xác định".
2. **Đối tác phản ánh CỤ THỂ:** cho rằng "Không xác định" là dữ liệu hiển thị SAI của phần mềm (kỳ vọng thấy tên lĩnh vực thật, không có nhóm "Không xác định").
3. **Data + bước tái hiện:** login CB NV TW → BC theo lĩnh vực → kỳ Năm 2026, Toàn quốc → test cả 2 nhánh: chương trình CÓ lĩnh vực và KHÔNG lĩnh vực → quan sát nhóm + đọc API.

## Bảng đối chiếu điều kiện

→ [`../../cond/CTTLV_04.md`](../../cond/CTTLV_04.md) — **0 GAP** (role nghiệp vụ Toàn quốc, kỳ Năm 2026, test cả 2 nhánh có/không lĩnh vực).

## Cổng 3 — Đối chiếu SRS (bản được giao: v3.5)

**Mâu thuẫn nội bộ SRS (nguồn gốc tranh chấp):**
- FR-IX-22 §Mô tả + §Output (`srs-fr-11-bao-cao.md:961`, `:981-982`): báo cáo gom **theo lĩnh vực** (hàng = lĩnh vực; Output `linh_vuc_id` + `ten_linh_vuc`, điều kiện "Luôn").
- NHƯNG entity **CHUONG_TRINH_HTPL** (data model `srs-fr-15-ct-htpldn.md:1323-1334`) **KHÔNG có attribute `linh_vuc_id`**. Form tạo chương trình FR-XI-01 (`srs-fr-15-ct-htpldn.md:129-137`) cũng **KHÔNG có trường lĩnh vực** (chỉ: mã, tên, mục tiêu, thời gian, ngân sách, đối tượng, đơn vị, ghi chú).
- → Theo SRS, chương trình **không có cách nào gán lĩnh vực** → mọi CT sẽ rơi vào "Không xác định". Báo cáo "theo lĩnh vực" gom theo một trường mà entity nguồn không định nghĩa.

**SRS im lặng:** FR-IX-22 không quy định cách xử lý chương trình có lĩnh vực = null (tạo nhóm "Không xác định" / ẩn / gộp khác). Không có clause nào cấm cũng như bắt buộc nhãn "Không xác định".

→ Đây KHÔNG phải app sai một clause SRS rõ ràng (không phải Open) và cũng KHÔNG phải lỗi không tái hiện (không phải Reject). Là **mâu thuẫn + khoảng trống đặc tả** → BA confirm.

## Kết quả verify trên env được giao (https://18.143.165.120.nip.io)

- Seed 1 chương trình gán lĩnh vực "Thương mại" (đã duyệt) + 3 chương trình không gán lĩnh vực (đã duyệt), kỳ Năm 2026.
- Báo cáo hiển thị đúng 2 nhóm: **"Không xác định" = 3** (biểu đồ cột xanh) + **"Thương mại" = 1** (cột xanh lá); bảng "Lĩnh vực PL / Số chương trình / Số DN tham gia": Không xác định = 3/0, Thương mại = 1/0. Tổng chương trình = 4.
- API `GET /api/v1/bao-cao/ct-theo-linh-vuc?kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31` → 200: `data:[{"linhVucId":null,"tenLinhVuc":"Không xác định","soCt":3},{"linhVucId":"bbbbbbbb-...","tenLinhVuc":"Thương mại","soCt":1}]`.
- → Hiện tượng đối tác báo **TÁI HIỆN**: nhóm "Không xác định" đúng là do CT chưa gán lĩnh vực; khi CT có lĩnh vực thì tên hiển thị đúng. FE map trung thực dữ liệu BE (không phải lỗi render/mapping).
- Ảnh: `cttlv-report-live-chart-table-2buckets.png`, `cttlv-report-live-2buckets-2026-07-22.png`.

## Verdict

**`BA confirm`** — Hiện tượng "Không xác định" tái hiện đúng (phản ánh CT chưa gán lĩnh vực), không phải lỗi render. Nhưng có mâu thuẫn nội bộ SRS (báo cáo gom theo lĩnh vực nhưng entity/form chương trình không có trường lĩnh vực) + SRS im lặng về cách xử lý CT chưa gán lĩnh vực. QA không tự chốt — đề xuất BA quyết (xem `../../ba-confirm/bctk/ba-confirm-CTTLV_04.md`).

## Evidence
- `cttlv-report-live-chart-table-2buckets.png` — biểu đồ + bảng 2 nhóm (Không xác định=3, Thương mại=1).
- `cttlv-report-live-2buckets-2026-07-22.png` — header báo cáo + Tổng chương trình=4.
- API response ct-theo-linh-vuc (linhVucId=null → "Không xác định").
- Bảng điều kiện: [`../../cond/CTTLV_04.md`](../../cond/CTTLV_04.md).
