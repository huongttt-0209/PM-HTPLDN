# Bảng đối chiếu điều kiện — QLTMBMHD_07

Loại bug: **Thêm thư mục trùng tên → đối tác báo thông báo lỗi bị NHÂN ĐÔI (duplicate toast).** Verdict phụ thuộc: tái hiện đúng role + đúng điều kiện tiền đề (đã có thư mục trùng tên trong đơn vị) rồi ĐO số khung thông báo vs số request.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence QLTMBMHD_07.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **CB Nghiệp vụ** thêm thư mục | `cbnv_tw` — CB Nghiệp vụ, Trung ương (BTP·TW) | Không |
| Dữ liệu tiền đề | Đơn vị đã có thư mục cùng tên | Đã seed thư mục "BM-B1-0720 Trung" (Nháp, Thương mại, BTP·TW) tồn tại sẵn | Không |
| Thao tác đối chiếu | Thêm thư mục nhập lại đúng tên trùng → Lưu → xem thông báo | Modal "Thêm thư mục biểu mẫu" → nhập "BM-B1-0720 Trung" + Lĩnh vực Thương mại → Lưu → đo qua `tools/toast-capture.js` (2 lần) | Không |
| Đối tượng so sánh (số khung thông báo) | App đối tác hiện **2 toast xếp chồng** cùng nội dung "Tên thư mục đã tồn tại trong đơn vị" | App test: **1 request → 1 khung thông báo** (cả 2 lần đo, `BI_LAP=false`, observer KHÔNG lọc trùng) | Không |

**Kết luận: 0 GAP về role/data/thao tác.** Tái hiện đúng điều kiện đối tác (CB NV, đơn vị đã có thư mục trùng, nhập trùng tên). Kết quả:

- **KHÔNG tái hiện nhân đôi:** 2 lần đo độc lập đều cho 1 POST `/api/v1/thu-muc-bieu-maus` → 1 khung thông báo "Tên thư mục đã tồn tại trong đơn vị". Cả tầng network (1 request) lẫn tầng hiển thị (1 toast frame) đều nhất quán — nếu nhân đôi ở tầng hiển thị, observer (không dedup) sẽ đếm 2.
- Triệu chứng cụ thể đối tác phản ánh (thông báo nhân đôi) **không xảy ra** trên build hiện tại → **Reject**.
- Ghi nhận phụ (ngoài phạm vi case, KHÔNG đổi verdict): wording toast "Tên thư mục đã tồn tại trong đơn vị" khác SRS ERR-TM-01 "Thư mục '{tên}' đã tồn tại trong đơn vị" (thiếu tên thư mục cụ thể). Nêu ở mục "bất thường ngoài tiêu chí".

Chi tiết đo: [`../reverify-audit/QLTMBMHD_07/toast-measurement.md`](../reverify-audit/QLTMBMHD_07/toast-measurement.md).
