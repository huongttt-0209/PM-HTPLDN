# Bảng đối chiếu điều kiện — PDHSVV_03

Loại bug: **Cán bộ Phê duyệt khác đơn vị bấm Phê duyệt vụ việc ở "Chờ phê duyệt" — đối tác báo (1) thông báo hiển thị lặp (duplicate) và (2) sai wording.** Cả 2 ý phụ thuộc role (CB PD **khác** đơn vị) + state (Chờ phê duyệt) → điền bảng, xác nhận app thực tế đúng điều kiện đối tác trước khi kết luận.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence + cột Điều kiện/Bước) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác | **Cán bộ phê duyệt KHÁC đơn vị** với đơn vị của vụ việc | `cbpd_tw` — CB_PD_TW, đơn vị BTP·TW (Trung ương). Vụ việc thuộc Sở Tư pháp An Giang (địa phương) → **khác đơn vị + khác cấp**, đúng tình huống E2 "CB PD không cùng cấp" | Không |
| Trạng thái vụ việc khi phê duyệt | Hồ sơ vụ việc ở **"Chờ phê duyệt"** (có nút [Phê duyệt] [Từ chối]) | VV-STP-AG-20260712-003 ở **CHO_PHE_DUYET** (có nút [Phê duyệt] [Từ chối]) | Không |
| Thao tác thực hiện | Bấm [Phê duyệt] → hộp thoại xác nhận → Xác nhận | Bấm [Phê duyệt] → hộp thoại "Bạn xác nhận phê duyệt kết quả xử lý vụ việc?" → bấm [Phê duyệt] | Không |
| Ý (1) — hiện tượng lặp cần đo | "Hệ thống hiển thị **thông báo lặp** (2 thông báo giống nhau)" | Đo bằng `tools/toast-capture.js` (tự kiểm observer = 1, KHÔNG lọc trùng, đọc `innerText`, đếm request) qua **3 lần** bấm | Không |
| Ý (2) — nội dung wording cần đọc | "Nội dung thông báo **sai** so với đặc tả" | Đọc nội dung khung thông báo hiển thị (bằng observer + ảnh chụp) | Không |

**Kết luận: 0 GAP về role/state/data.** Đã test đúng điều kiện đối tác nêu (CB PD khác đơn vị, vụ việc "Chờ phê duyệt"). Kết quả:

- **Chặn nghiệp vụ ĐẠT:** máy chủ trả HTTP 403, vụ việc giữ nguyên "Chờ phê duyệt" — không cho phê duyệt chéo đơn vị (đúng SRS E2 ERR-PD-02).
- **Ý (1) — thông báo lặp KHÔNG tái hiện:** 3 lần bấm Phê duyệt (2 lần đo qua observer bọc fetch + 1 lần đo qua ảnh pin), mỗi lần **1 request** `POST .../phe-duyet` (403) và **đúng 1 khung thông báo**, không lặp (`SO_KHUNG = 1`, `BI_LAP = false`); network log CDP cũng chỉ có 1 POST /phe-duyet. Ảnh chụp chỉ có 1 thông báo. → Không log bug cho ý này (không tái hiện, tránh false bug).
- **Ý (2) — sai wording XÁC NHẬN:** thông báo hiển thị **"Đơn vị của người phê duyệt khác đơn vị của bản ghi"** — dùng từ kỹ thuật "bản ghi" và khác nội dung SRS quy định ("Bạn không có quyền phê duyệt vụ việc này", `srs-fr-05-vu-viec.md:1002`). → Log **BUG-PDHSVV_03** (Minor, wording).

**Ghi chú tiền đề (seed):** VV-STP-AG-20260712-003 gốc ở DANG_XU_LY (seed tuần 2). Để dựng đúng điều kiện "Chờ phê duyệt", đã: (a) `nht_ag_uat2` (người xử lý/nguoiXuLy của vụ việc, cùng đơn vị An Giang) cập nhật kết quả xử lý qua `cap-nhat-ket-qua`; (b) trình phê duyệt qua `trinh-phe-duyet` → CHO_PHE_DUYET. Không đổi role/đơn vị của người phê duyệt (vẫn là cbpd_tw khác đơn vị) → không phát sinh GAP.

Chi tiết: xem [`../reverify-audit/PDHSVV_03/audit.md`](../reverify-audit/PDHSVV_03/audit.md).
