# BA confirmation needed — TVCS Batch D (Workflow SM-TVCS) — 2026-07-21

> **File này để làm gì:** gom testcase mà QA cần BA phản hồi. Riêng `QLNDTVVCG_36` đã có **bug log song song** (`../../bug-reports/tvcs/Pass-bug-report-tvcs-batchD.md` — BUG-QLNDTVVCG_36): defect "hủy trực tiếp bỏ qua guard" đã rõ theo SRS. Phần cần BA ở đây là **cơ chế duyệt hủy chưa có state/sub-flow riêng trong SM** — dev cần BA chốt cách mô hình hóa trước khi implement đúng.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE` mở file verify thực. Dùng SRS v3.5 (`input/srs-update-2026-5-5/`).

---

## QLNDTVVCG_36 — Cơ chế "duyệt hủy" record DANG_TU_VAN chưa có state/sub-flow riêng trong SM-TVCS

**Bối cảnh testcase**

- Dòng Excel: 289, mã TC `QLNDTVVCG_36`.
- Nội dung kiểm tra: CB Nghiệp vụ hủy một record TVCS đang ở trạng thái "Đang tư vấn" (DANG_TU_VAN).
- Expected đối tác: hủy từ "Đang tư vấn" phải qua bước **"chờ duyệt hủy"**, không được chuyển thẳng "Đã hủy".
- Actual đối tác ghi: hủy → chuyển thẳng "Đã hủy" + báo "Đã hủy yêu cầu".

**Kết quả verify UI hiện tại**

- Verify 21/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw_04` / CB_NV_TW (đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp, cùng đơn vị record).
- Record TVCS-20260721-0004 ở DANG_TU_VAN → bấm [Hủy yêu cầu] → hộp thoại "Hủy nội dung tư vấn" **chỉ có 1 trường "Lý do hủy"** (bắt buộc), không có bước DN đồng ý / CB PD duyệt.
- Nhập lý do → [Xác nhận hủy]: **1 request** `POST .../huy` → record `trangThai=HUY` ngay lập tức (không qua trạng thái trung gian).
- Evidence: `../bug-reports/tvcs/image/BD-case36-R2-dahuy.png`, `../bug-reports/tvcs/image/BD-case36-R2-dangtuvan.png`.

**Điểm cần BA chốt trong SRS v3.5**

1. SRS **có yêu cầu** điều kiện duyệt hủy cho record DANG_TU_VAN:
   - Processing Hủy yêu cầu bước 4: "Nếu DANG_TU_VAN: **yêu cầu DN đồng ý hủy + CB Phê duyệt duyệt hủy**".
   - SM-TVCS bảng chuyển trạng thái: `DANG_TU_VAN → HUY` có guard "**DN yêu cầu hủy + CB PD duyệt**".

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:229`
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1512`

2. Nhưng SM-TVCS **không có trạng thái riêng** cho bước duyệt hủy, và **không có Processing sub-flow / màn hình** mô tả cơ chế:
   - Bảng trạng thái SM chỉ có 7 state: TIEP_NHAN, PHAN_CONG, DANG_TU_VAN, HOAN_THANH, CHO_PHE_DUYET, DA_DUYET, HUY — không có "CHO_DUYET_HUY" hay tương đương.
   - Điều kiện "DN đồng ý hủy + CB PD duyệt hủy" chỉ tồn tại dạng guard, không nêu ai khởi tạo yêu cầu hủy (DN hay CB NV), DN nêu đồng ý qua kênh nào, CB PD duyệt hủy ở màn hình nào.

   Citation:
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1489-1497` (bảng 7 trạng thái, không có state duyệt hủy)
   - `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:222-232` (Processing Hủy — không có sub-flow cho bước duyệt hủy)

**Câu hỏi cần BA xác nhận**

Cơ chế hủy record DANG_TU_VAN cần được mô hình hóa thế nào để dev implement đúng guard SRS dòng 229/1512?

1. **Hướng 1 — thêm trạng thái/luồng duyệt hủy:** hủy từ DANG_TU_VAN không chuyển thẳng HUY mà vào một bước chờ (DN đồng ý + CB PD duyệt hủy) trước; cần bổ sung state/sub-flow + màn hình duyệt hủy.
2. **Hướng 2 — giữ hủy trực tiếp nhưng ràng buộc điều kiện:** không thêm state, nhưng nút hủy chỉ khả dụng/hoàn tất khi đã có xác nhận DN + phê duyệt CB PD (điều kiện enable), nếu chưa đủ thì chặn.

**Đề xuất QA tạm thời**

- Verdict TC: `Open, BA confirm` — **Open** vì hành vi hiện tại (CB NV hủy trực tiếp, bỏ qua cả DN đồng ý lẫn CB PD duyệt) vi phạm guard SRS dòng 229/1512 (đã log BUG-QLNDTVVCG_36); **BA confirm** vì cơ chế duyệt hủy chưa được đặc tả (chọn Hướng 1 hay Hướng 2).
- Bug BUG-QLNDTVVCG_36 gửi Dev BE để chặn hủy trực tiếp; phần thiết kế cơ chế chờ BA chốt hướng trước khi dev làm chi tiết.
- Nếu BA chọn Hướng 1: cần cập nhật SM-TVCS (thêm state duyệt hủy) + expected testcase khớp "chờ duyệt hủy" như đối tác mong đợi.
- Nếu BA chọn Hướng 2: giữ SM 7 state, dev thêm ràng buộc điều kiện enable nút hủy; expected testcase đối tác ("chờ duyệt hủy" là 1 state) cần điều chỉnh lại.
