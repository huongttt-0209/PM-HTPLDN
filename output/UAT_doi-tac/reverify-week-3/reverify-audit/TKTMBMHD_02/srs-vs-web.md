# Audit — TKTMBMHD_02 (Cổng 3: SRS vs Web)

**Verdict:** Open (bug tĩnh — mặc định phân trang, không phụ thuộc role/state/data)

## 3 dữ kiện neo (từ evidence đối tác full-res)
- (a) URL/ID: `htpldn-uat.ospgroup.vn/bieu-mau/thu-muc?linhVucId=...013&page=1`, role CB_NV_TW.
- (b) State: dropdown phân trang góc phải = **"100 / trang"**; tab "Tất cả 3"; "Hiển thị 1-3 / 3 kết quả".
- (c) Tiền đề: 3 thư mục (Nháp/Đã công khai/Đã ẩn), lọc lĩnh vực "Lao động".

## Cổng 2 — hiểu bug
- Evidence đã xem: `partner-evidence/TKTMBMHD_02.jpg` — frame chứa lỗi: dropdown "100 / trang" ở góc dưới phải.
- Đối tác phản ánh cụ thể: mặc định 100 mục/trang (kỳ vọng 20/trang + sort ngày tạo giảm dần).
- Data + bước: login CB_NV_TW → Biểu mẫu → Thư viện biểu mẫu → quan sát dropdown page-size + thứ tự Ngày tạo.

## Cổng 3 — Bảng đối chiếu SRS vs Web

| Tiêu chí | SRS yêu cầu (dẫn line) | Thực tế web (env test) | Đủ/Thiếu |
|---|---|---|---|
| Kích thước trang mặc định | 20 mục/trang, max 100 — BR-DATA-07 `srs-fr-09:917`; SCR-VII-01 §Quy tắc tương tác `srs-fr-09:623` | **100 / trang** (ngay khi tải, chưa thao tác) | ❌ THIẾU/SAI |
| Sắp xếp mặc định (ngày tạo giảm dần) | AC không nêu rõ thứ tự; kỳ vọng đối tác = ngày tạo giảm dần | 20/07 → 20/07 → 15/07 → 30/06 = **giảm dần** | ✅ Đúng |

## Kết luận
- Sub-claim page-size 100 ≠ 20 → **Open** (sai rõ clause SRS: BR-DATA-07 + SCR-VII-01:623).
- Sub-claim sort ngày tạo giảm dần → web ĐÚNG → không phải lỗi.
- Verdict tổng (1 case gộp nhiều ý): **Open** vì ≥1 ý Open.
- Bug tĩnh: mặc định page-size là cấu hình FE cố định, không phụ thuộc role/state/data → dùng `--static-bug`.

## Artifact real-data
- `bug-reports/image/BUG-TKTMBMHD_02.png` (full-res, env test, role CB_NV_TW, dropdown "100 / trang" rõ).
