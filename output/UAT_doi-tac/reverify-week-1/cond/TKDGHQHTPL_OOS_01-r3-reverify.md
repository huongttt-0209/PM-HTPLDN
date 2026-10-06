# Bảng đối chiếu điều kiện — TKDGHQHTPL_OOS_01 (re-verify sau khi dev báo fix, 27/07/2026)

**Mode:** `reverify` — cột tham chiếu là **điều kiện của BUG GỐC** (`BUG-TKDGHQ-KPI-LOC`, file [`bug-report-dashboard-r2.md`](../bug-reports/dashboard/bug-report-dashboard-r2.md)), không phải evidence đối tác (bug này do QA phát hiện ngoài phạm vi).

**Bug gốc:** thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" hiển thị `29.5/100` kèm "Dựa trên **14** đánh giá", trong khi chỉ có **11** kết quả ở trạng thái "Đã đánh giá" — thẻ gộp cả bản ghi chưa chấm và bản ghi của kế hoạch đã hủy.

| Điều kiện có thể đổi kết quả | Bug gốc (bug-report §Bước tái hiện) | Mình test (27/07/2026 17:22) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw_02` — Cán bộ NV Trung ương (`CB_NV_TW`), đơn vị Cục Bổ trợ tư pháp — BTP · TW | `cbnv_tw` — cùng vai trò `CB_NV_TW`, cùng đơn vị BTP · TW (fallback cùng role + cùng đơn vị theo Rule 7; bug-report §Phụ lục liệt kê cả 2 tài khoản này). Đo lặp thêm bằng `cbpd_tw` (`CB_PD_TW`) — thẻ trả **cùng con số 8.2/100 · 10 đánh giá** ⇒ kết quả không phụ thuộc vai trò, đã chứng minh bằng test thật chứ không phải lập luận | Không |
| Môi trường | Env được giao `18.143.165.120.nip.io` — bug gốc chỉ đo được ở đây | Đúng `18.143.165.120.nip.io` | Không |
| Màn hình + thẻ | Màn "Tổng quan hệ thống", thẻ "Điểm đánh giá hiệu quả hỗ trợ pháp lý" | Đúng màn đó, đúng thẻ đó | Không |
| Bộ lọc | Năm 2026, Tháng "Cả năm" (mặc định khi mở màn) | Đúng bộ lọc mặc định: Năm 2026 · Tháng "Cả năm" · Cấp đơn vị "Toàn quốc" · Đơn vị "Tất cả" | Không |
| Tiền đề dữ liệu (quyết định lỗi có lộ ra hay không) | Cần đồng thời: (a) ≥1 kết quả đánh giá còn ở "Chưa đánh giá" nhưng đã có sẵn điểm tổng, và (b) ≥1 kế hoạch đánh giá trạng thái "Hủy" mà kết quả của nó đã có điểm | Cả hai tiền đề **VẪN CÒN NGUYÊN** trên env tại thời điểm re-verify: (a) 3 kết quả "Chưa đánh giá" mang điểm 80,00 / 60,00 / 90,00 thuộc kế hoạch `KHDG-SEED-0001`; (b) kế hoạch `DG-20260727-0001` trạng thái "Hủy" có kết quả `diemTong = 100,00`. Đã đọc lại trực tiếp qua danh sách kế hoạch + kết quả đánh giá | Không |

**Kết luận:** 0 GAP. Quan trọng nhất là dòng cuối — **dữ liệu gây lỗi chưa hề bị dọn đi**, nên việc thẻ không còn đếm chúng là bằng chứng đã sửa logic, không phải do dữ liệu thay đổi.

## Kết quả đo (bug gốc → re-verify 27/07 17:22)

- **Con số trên thẻ:** `29.5/100` → **`8.2/100`**. Kỳ vọng 8,24 — bug-report đã tính sẵn ✅
- **Cỡ mẫu:** "Dựa trên **14** đánh giá" → **"Dựa trên 10 đánh giá"**. Kỳ vọng 10 = 11 kết quả "Đã đánh giá" − 1 của kế hoạch đã hủy ✅
- **Cột biểu đồ:** 02/2026 = 90.0 · 04/2026 = 80.0 · 05/2026 = 60.0 · 07/2026 = 16.6 → chỉ còn **07/2026 = 8.2**. 3 cột đầu đến từ bản ghi chưa chấm nên phải biến mất ✅

**Đối chiếu số học:** 10 kết quả "Đã đánh giá" thuộc kế hoạch không bị hủy = 8,40 + 8,00 + 8,00 + 8,60 + 7,90 + 7,70 + 8,90 + 8,00 + 8,90 + 8,00 = **82,40**; chia 10 = **8,24** → khớp con số **8.2** hiển thị. Đúng bằng giá trị mà bug-report đã dự đoán cho trường hợp loại bỏ bản ghi của kế hoạch đã hủy.

**Bằng chứng:** [`BUG-TKDGHQ-KPI-LOC-r3-nipio-PASS-8.2-dua-tren-10-danh-gia.png`](../bug-reports/dashboard/image/BUG-TKDGHQ-KPI-LOC-r3-nipio-PASS-8.2-dua-tren-10-danh-gia.png)
