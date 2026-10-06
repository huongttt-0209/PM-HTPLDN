# Bảng đối chiếu điều kiện — QLNDTVVCG_26 (dòng 323) — Chuyên gia từ chối phân công, thông báo cho CBNV kèm lý do

**Kết luận:** Pass — cán bộ nghiệp vụ phụ trách nhận được thông báo và thông báo có **nguyên văn lý do từ chối**.

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1 / phiếu đối tác) | Mình đo lại (04/08/2026 14:23, bản dựng index-DpIXRGaI.js · V1.0.5) | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | Chuyên gia **được phân công** cho yêu cầu | `huongcg` — đúng chuyên gia đang được phân công (`chuyenGiaId` khớp) | Không |
| Vai trò người nhận | Cán bộ nghiệp vụ phụ trách | `cb_nv_tw_10` — người tạo và phân công yêu cầu (`nguoiTaoId` khớp; đã tra ra tài khoản chứ không mở chuông tài khoản khác) | Không |
| Entity + trạng thái | Yêu cầu tư vấn chuyên sâu ở "Phân công" | `TVCS-20260804-0005`, trạng thái "Phân công" | Không |
| Thao tác / input | Bấm "Từ chối", nhập lý do, xác nhận | Bấm "Từ chối nhiệm vụ" → nhập lý do có chuỗi nhận dạng riêng `QA-LYDO-V2-0408-742199 chuyen gia ban lich khong nhan nhiem vu nay` → bấm "Từ chối" | Không |

**Bằng chứng:**
- `image/QLNDTVVCG_26-v2-01-tuchoi-ve-tiepnhan-go-chuyengia.png` — sau thao tác: trạng thái về "Tiếp nhận", trục tiến trình lùi về bước 1.
- `image/QLNDTVVCG_26-v2-02-cbnv-nhan-thongbao-kem-ly-do.png` — màn "Thông báo" mở bằng chính tài khoản `CB Nghiệp vụ TW 10 · CB_NV_TW`: mục "Chuyên gia từ chối phân công: TVCS-20260804-0005 · Phân công · 04/08/2026 14:23", nội dung đầy đủ **"Mã: TVCS-20260804-0005. Chuyên gia đã từ chối, cần phân công lại. Lý do: QA-LYDO-V2-0408-742199 chuyen gia ban lich khong nhan nhiem vu nay"** — chuỗi nhận dạng trùng khớp tuyệt đối với lý do đã nhập.
- Đếm hộp thông báo trước/sau: 83 → 85 mục; mục mới ghi nhận `07:23:02Z`, trùng đúng giây với thời điểm bấm `07:23:02.653Z`.
- Kết quả nghiệp vụ khác cũng đúng: trạng thái `PHAN_CONG` → `TIEP_NHAN`, `chuyenGiaId` được gỡ về `null`; ô nhập lý do là bắt buộc (`aria-required=true`, gợi ý "tối thiểu 10 ký tự").
- 1 request `POST /api/v1/noi-dung-tu-van-cs/{id}/xac-nhan`, 1 khung thông báo — không lặp.

**⚠️ Lệch nhỏ so với "Kết quả mong đợi" của phiếu, KHÔNG phải lỗi đối tác đã báo:** khung thông báo hiện chữ **"Đã xác nhận"** (giống hệt nhánh chấp nhận) thay vì "Đã từ chối yêu cầu", và sau khi từ chối màn hình **ở lại trang chi tiết** chứ không quay về danh sách. Ghi nhận ở mục "Phát hiện thêm", không đổi verdict vì lỗi đối tác báo là chuyện thông báo cho cán bộ.
