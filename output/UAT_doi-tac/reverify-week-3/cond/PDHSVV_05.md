# Bảng đối chiếu điều kiện — PDHSVV_05

Loại bug: **Từ chối phê duyệt vụ việc thành công nhưng (1) không gửi thông báo cho CB Nghiệp vụ + người được phân công, (2) không hiển thị lý do từ chối ở màn chi tiết vụ việc.** Cả 2 ý phụ thuộc role (CB PD cùng đơn vị mới từ chối được) + state (Chờ phê duyệt) → điền bảng, xác nhận app thực tế đúng điều kiện đối tác trước khi kết luận.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence + cột Điều kiện/Bước) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thao tác (từ chối) | **Cán bộ phê duyệt cùng đơn vị với đơn vị tạo hồ sơ** | `cbpd_tw` — CB_PD_TW, đơn vị BTP·TW (cùng đơn vị với đơn vị tạo hồ sơ VV-BTP-TW-...). Cùng loại vai trò Cán bộ Phê duyệt cùng cấp | Không |
| Trạng thái vụ việc khi từ chối | Hồ sơ vụ việc ở **"Chờ phê duyệt"** (có nút [Phê duyệt] [Từ chối]) | VV-BTP-TW-20260712-001 ở **CHO_PHE_DUYET** (có nút [Phê duyệt] [Từ chối]) | Không |
| Thao tác thực hiện | Bấm [Từ chối] → nhập **thông tin hợp lệ** (lý do) → Xác nhận | Bấm [Từ chối] → nhập lý do hợp lệ (110 ký tự, ≥10) → Xác nhận → toast "Đã từ chối phê duyệt", VV → DANG_XU_LY | Không |
| Ý (1) — người nhận thông báo cần kiểm | "Gửi thông báo cho **cán bộ nghiệp vụ và người hỗ trợ** phụ trách hồ sơ kèm lý do" | Kiểm cả 2: `cbnv_tw` (CB NV phụ trách, CB_NV_TW) + `qa_tvvseed28` (người được phân công / TVV). Cả 2 đều là người nhận đúng theo SRS | Không |
| Ý (2) — nơi hiển thị lý do cần kiểm | "Chi tiết bản ghi **không hiển thị lý do từ chối**" | Kiểm màn chi tiết VV (Dòng thời gian + các accordion) ở cả 2 view (assignee + CB NV) | Không |

**Kết luận: 0 GAP về role/state/data.** Xác nhận app thực tế đúng như đối tác báo:

- **Trạng thái + toast ĐẠT:** bấm [Từ chối] + nhập lý do hợp lệ → toast "Đã từ chối phê duyệt", VV chuyển CHO_PHE_DUYET → DANG_XU_LY (quay về người được phân công sửa kết quả). Đúng SRS.
- **Ý (1) — thông báo THIẾU:** sau khi từ chối (06:03Z), cả CB NV phụ trách (`cbnv_tw`) lẫn người được phân công (`qa_tvvseed28`) đều **KHÔNG có thông báo** nào về việc vụ việc bị từ chối — cả in-app (số chưa đọc không tăng thêm mục từ chối; panel chỉ có HE_THONG/PHAN_CONG/PHE_DUYET cũ) lẫn email. Loại trừ nhiễu: cả 2 tài khoản VẪN nhận các thông báo khác (phân công, phê duyệt hồ sơ TVV, đăng nhập nơi khác) → chức năng thông báo còn sống, chỉ thiếu riêng thông báo **từ chối phê duyệt vụ việc**.
- **Ý (2) — lý do KHÔNG hiển thị:** lý do từ chối được lưu ở dữ liệu (`VU_VIEC.ghiChuPheDuyet` + `LICH_SU_VU_VIEC.duLieuMoi.lyDo`) nhưng màn chi tiết vụ việc **không surface ra UI ở bất kỳ đâu khi vụ việc bị từ chối quay về DANG_XU_LY**: Dòng thời gian chỉ hiện dòng "Từ chối duyệt" + giờ + người, KHÔNG kèm lý do; **nhóm "Phê duyệt" không hiển thị ở trạng thái DANG_XU_LY** (app chỉ hiện nhóm này khi vụ việc đang CHO_PHE_DUYET hoặc DA_DUYET — xác nhận thêm khi verify PDHSVV_02), nên còn 7 nhóm: Thông tin DN, Nội dung Yêu cầu, Tài liệu đính kèm, Kết quả kiểm tra, Phân công, Kết quả hỗ trợ, HĐ tư vấn liên kết. Kiểm cả 2 view (người được phân công + CB NV) đều không thấy chữ lý do (`hasReasonTextOnPage=false`).

Chi tiết: xem [`../reverify-audit/PDHSVV_05/audit.md`](../reverify-audit/PDHSVV_05/audit.md).
