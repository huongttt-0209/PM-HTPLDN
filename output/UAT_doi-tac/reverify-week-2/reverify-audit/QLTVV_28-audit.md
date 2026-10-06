# QLTVV_28 — Audit verify (internal)

**Verdict:** `Reject` (❌ Không phải bug — không tái hiện).
**Ngày verify:** 2026-07-12 · **Account verdict:** `cbnv_tw` (CB_NV_TW) trên env được giao `http://18.143.165.120`.

## Đối tác phản ánh
Xóa 1 TVV đang có vụ việc chưa hoàn thành → hệ thống báo **chung chung** "Không thể xóa tư vấn viên. Vui lòng thử lại." thay vì thông báo nghiệp vụ cụ thể (ERR-TVV-05 "Tư vấn viên đang có vụ việc chưa hoàn thành").
- Evidence: `partner-evidence/QLTVV_28.webm` → frame `QLTVV_28-partner-frame-delete-generic-message.jpg`.

## Bảng đối chiếu điều kiện (Quy tắc VÀNG) — 0 GAP
| Điều kiện | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | Cán bộ Nghiệp vụ | CB_NV_TW (`cbnv_tw`) | Không |
| Entity + state | TVV có vụ việc **chưa hoàn thành** | TVV `QA TVV Seed28 Active` (HOAT_DONG) có vụ việc `VV-BTP-TW-20260712-001` state **DA_PHAN_CONG** (chưa hoàn thành) | Không |
| Data tiền đề | TVV được phân công vụ việc đang xử lý | Đã phân công 1:1 (API 201, vụ việc → DA_PHAN_CONG) | Không |

## Seed đã thực hiện (env được giao) — để đóng GAP
Dữ liệu mẫu ban đầu KHÔNG có TVV nào vừa hoạt động vừa được phân công vụ việc (3 TVV seed đều `taiKhoanId=null` → phân công trả ERR-PC-02). Đã seed đủ vòng đời để tái hiện nhánh bị chặn:
1. Tạo TVV `TVV-BTP-TW-0002` (`98cfd963-…`) qua API → MOI_DANG_KY.
2. Thẩm định (Nhóm 1–4) + Trình duyệt qua tab "Thẩm định" → CHO_PHE_DUYET.
3. Phê duyệt (soQuyetDinh) → CHO_KICH_HOAT (BE tự tạo tài khoản `5432719c-…`).
4. Kích hoạt tài khoản qua email first-login-password (MailHog env này) → **HOAT_DONG** (đủ điều kiện phân công).
5. Tạo vụ việc `VV-BTP-TW-20260712-001` (`8e259653-…`, lĩnh vực Thương mại) → đưa về DANG_KIEM_TRA.
6. Phân công vụ việc cho TVV → **201, vụ việc DA_PHAN_CONG** (TVV giờ có vụ việc chưa hoàn thành).

## Quan sát thao tác bị báo lỗi (real-data artifact)
Bấm **Xóa** TVV `QA TVV Seed28 Active` (đang có vụ việc DA_PHAN_CONG) → xác nhận:
- **UI toast** (bắt bằng MutationObserver + chụp màn): **"Không thể xóa: TVV còn vụ việc đang xử lý"** — thông báo nghiệp vụ **CỤ THỂ**, KHÔNG phải "Vui lòng thử lại".
  - Ảnh: `QLTVV_28-web-delete-toast-thongbao-cu-the.png`.
- **API** `DELETE /api/v1/tu-van-viens/{id}` → **HTTP 409**, `code: ERR-TVV-05`, `message: "Không thể xóa: TVV còn vụ việc đang xử lý"`.

## Kết luận
Nhánh chặn xóa đã tái hiện đúng điều kiện đối tác (0 GAP). Trên env được giao, hệ thống hiển thị **đúng** thông báo nghiệp vụ cụ thể (cả UI lẫn API mang mã ERR-TVV-05) — không xảy ra thông báo chung chung "Vui lòng thử lại" như đối tác báo. Bất đồng thuộc về **thực tế** (không tái hiện được hành vi lỗi) → `Reject`.

**Đối chiếu SRS:** ERR-TVV-05 (srs-fr-04 dòng 200) yêu cầu từ chối xóa kèm thông báo nghiệp vụ khi TVV còn vụ việc chưa hoàn thành. Thông báo thực tế "Không thể xóa: TVV còn vụ việc đang xử lý" thoả yêu cầu (nêu rõ lý do nghiệp vụ). Không còn defect về wording.

*(Ghi chú env: đối tác log trên môi trường khác; hành vi generic có thể là build cũ/khác của đối tác. Không đưa nội dung 2 môi trường vào note gửi đối tác.)*
