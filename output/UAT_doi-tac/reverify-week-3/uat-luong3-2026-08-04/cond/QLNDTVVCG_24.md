# Bảng đối chiếu điều kiện — QLNDTVVCG_24 (dòng 322) — Chuyên gia chấp nhận phân công, gửi thông báo cho DN và CBNV

**Kết luận:** Pass — cả doanh nghiệp lẫn cán bộ nghiệp vụ phụ trách đều nhận được thông báo, kiểm riêng từng người.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:21, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Chuyên gia **được phân công** cho yêu cầu | `huongcg` — đúng chuyên gia đang được phân công của bản ghi (`chuyenGiaId` khớp) | Không |
| Người nhận 1 | Doanh nghiệp của yêu cầu | Tài khoản `0151554887` — "Tester TKM", vai trò DN, đúng doanh nghiệp TKM Company sở hữu yêu cầu | Không |
| Người nhận 2 | Cán bộ nghiệp vụ phụ trách | `cbnv_tw` — người tạo và phân công yêu cầu (`nguoiTaoId` khớp) | Không |
| Entity + trạng thái | Yêu cầu tư vấn chuyên sâu ở "Phân công" | `TVCS-20260803-0003`, trạng thái "Phân công" (bước 2) | Không |
| Thao tác | Bấm "Chấp nhận" | Bấm "Chấp nhận" → hộp xác nhận "Chấp nhận tư vấn?" → xác nhận | Không |

**Bằng chứng:**
- `image/QLNDTVVCG_24-v2-01-chapnhan-doi-trangthai-dang-tu-van.png` — sau thao tác: huy hiệu "Đang tư vấn", trục tiến trình nhảy sang bước 3, Ngày bắt đầu 04/08/2026.
- `image/QLNDTVVCG_24-v2-02-chuong-doanhnghiep-nhan-thongbao.png` — mở chuông bằng chính tài khoản doanh nghiệp `Tester TKM · DN`: mục "Chuyên gia đã xác nhận tư vấn: TVCS-20…" / "Mã: TVCS-20260803-0003. Chuyên gia đã nhận việc, nội dung đa…".
- Đếm hộp thông báo trước/sau:
  - Doanh nghiệp: 10 → 12 mục; mục mới `Chuyên gia đã xác nhận tư vấn: TVCS-20260803-0003`, nội dung "…nội dung đang được tư vấn", ghi nhận `07:21:44Z`.
  - Cán bộ nghiệp vụ `cbnv_tw`: 336 → 338 mục; mục mới cùng tiêu đề, nội dung "…nội dung chuyển sang trạng thái đang tư vấn", ghi nhận `07:21:44Z`.
  - Cả hai trùng đúng giây với thời điểm bấm `07:21:44.275Z`.
- Hai kết quả nghiệp vụ còn lại cũng đúng: trạng thái `PHAN_CONG` → `DANG_TU_VAN`, `ngayBatDau` ghi `07:21:44.370Z`, và hệ thống tạo **1 phiên tư vấn mới** (`ngayTao 07:21:44.362Z`).
- 1 request `POST /api/v1/noi-dung-tu-van-cs/{id}/xac-nhan`, 1 khung thông báo "Đã xác nhận" — không lặp.
