# Bảng đối chiếu điều kiện — CVVDG_02

Loại bug: **Danh sách "Chọn vụ việc đánh giá" (FR-VI-05 / SCR item 41) — đối tác báo thiếu cột Tên doanh nghiệp, Ngày hoàn thành, Cảnh báo trùng đợt.** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS có prescribe danh sách cột cho bảng chọn VV không.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence CVVDG_02.jpg) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **CB Nghiệp vụ** (CB_NV_TW trong ảnh) | `cbnv_hn` — CB_NV_DP, CB NV được phân công | Không |
| Trạng thái đợt | THUC_HIEN (Tab Thực hiện, section Chọn VV) | Đợt DGHQ-B1 ở THUC_HIEN | Không |
| Màn hình đối chiếu | Bảng "Chọn vụ việc đánh giá" ở Tab Thực hiện | Cùng bảng đó | Không |
| Đối tượng so sánh (cột) | App có 5 cột: Mã VV / Tên VV / Lĩnh vực / Trạng thái / Đã chọn? — thiếu **Tên DN, Ngày hoàn thành, Cảnh báo trùng đợt** | App tôi test: **cùng 5 cột** Mã VV / Tên VV / Lĩnh vực / Trạng thái / Đã chọn? — thiếu đúng 3 cột đối tác nêu | Không |

**Kết luận: 0 GAP về role/state.** Tái hiện đúng: bảng chọn VV có 5 cột, thiếu đúng 3 cột đối tác nêu. Đối chiếu SRS:

- **SCR-VI-01 Tab 3 item 41** (`srs-fr-08-danh-gia.md:872`): "Chọn VV đánh giá | **C10 Multi-select** | Chọn VV hoàn thành trong kỳ... Lọc: trạng thái HOAN_THANH, trong kỳ, thuộc đơn vị". SRS mô tả đây là **multi-select**, KHÔNG liệt kê danh sách cột bắt buộc.
- **Cột "Tên DN"** chỉ được SRS quy định ở **bảng CHẤM ĐIỂM** (item 42, `:873`: "Cột: Mã VV / Tên DN / Lĩnh vực / ...") và **bảng báo cáo** (item 47, `:883`), KHÔNG phải bảng chọn VV.
- **"Ngày hoàn thành"** không xuất hiện như cột bắt buộc ở bất kỳ bảng nào trong SCR.
- **"Cảnh báo trùng đợt"** là **hành vi bắt buộc** (AC line 449 + Mô tả 393: cảnh báo khi VV thuộc đợt khác) nhưng SRS không quy định phải là 1 **cột** — hành vi cảnh báo được kiểm riêng ở **CVVDG_03**.
- SRS silent về danh sách cột của bảng chọn VV; app render bảng 5 cột (giàu hơn 1 multi-select). Không xác định app SAI hay bản thiết kế mới đúng → **BA confirm**.

Chi tiết: xem [`../reverify-audit/CVVDG_02/audit.md`](../reverify-audit/CVVDG_02/audit.md).
