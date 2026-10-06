# Seed data — env UAT nip.io (18.143.165.120)

> Tách khỏi `input.md` ngày 27/07/2026 theo yêu cầu: `input.md` chỉ giữ **môi trường test + tài khoản**.
> Đây là các bản ghi QA tự tạo/sửa trên env để dựng tiền đề verify. Nội dung giữ nguyên văn, không sửa.
> Quy tắc tạo: `QA_VERIFY_PROTOCOL.md` §Nguyên tắc 4.

  --- SEED DATA (batch BCTK-4, 21/07/2026) — Chương trình HTPLDN để verify báo cáo CT ---
  > Env nip.io ban đầu có 1 CT seed (CTHTPL-SEED-0001, DA_CONG_BO, donVi RỖNG, ngayCongBo=null)
  > → KHÔNG được báo cáo đếm (activate trả 403 vì donVi null). Báo cáo CT chỉ đếm CT ≥ DA_DUYET.
  > Đã tạo mới bằng luồng chuẩn (cbnv_tw_01 tạo → cbpd_tw_01 phê duyệt → DA_DUYET → được đếm):
  >  - CT-20260721-0001: lĩnh vực Thương mại, đơn vị Cục Bổ trợ tư pháp (TW), ngân sách 100.000.000, DA_DUYET.
  >  - CT-20260721-0004: KHÔNG gán lĩnh vực (→ nhóm "Không xác định"), TW, ngân sách 50.000.000, DA_DUYET.
  >  - (CT-0002/0003 no-lĩnh-vực cũng tồn tại — dùng để có nhóm "Không xác định" ≥1).
  > Dùng data này để đối chiếu KPI card / cột bảng / nhãn biểu đồ của báo cáo CT theo đơn vị & theo lĩnh vực.

  --- SEED DATA (TVCS Batch D, 21/07/2026) — record Tư vấn chuyên sâu để verify workflow ---
  > Đơn vị: Cục Bổ trợ tư pháp - Bộ Tư pháp (donViId 00000000-0000-4000-8000-000000000001). DN: Công ty TNHH
  > Seed Publishable. CG phân công: qa_tvvseed28. Tạo bởi cbnv_tw_04, luồng: tạo → phân công → CG xác nhận.
  >  - TVCS-20260721-0003 (id ab63d0a6-8629-48a6-8715-531e9aa0b1e2): case 27 — nay ở **CHO_PHE_DUYET**
  >    (CG đã hoàn thành, có kết quả). Sẵn sàng nếu cần test tiếp luồng CB PD duyệt/từ chối.
  >  - TVCS-20260721-0004 (id 318a5e57-c949-4ea3-90e2-dd647e6da4bf): case 36 — nay ở **HUY** (đã hủy từ
  >    DANG_TU_VAN). Record cuối luồng, không dùng lại được.
  >  - TVCS-20260721-0002: record của batch B (Đang tư vấn), KHÔNG phải của batch D.

  --- SEED DATA (DG Batch, 27/07/2026) — kế hoạch đánh giá dùng để dò thang điểm Dashboard ---
  > Env: nip.io (18.143.165.120). KHÔNG seed gì lên env đối tác ospgroup.
  >  - DG-20260727-0001 (id b217202c-de53-4f6b-a3f9-6ec911f2dfe0): trạng thái **HUY** — KHÔNG XÓA ĐƯỢC.
  >    1 tiêu chí `diemToiDa=200` (cố ý lệch mặc định 10) + 1 kết quả `diemTong=100.00`, xepLoai `DAT`.
  >    Mục đích: chứng minh BE xếp loại theo % trên trần riêng từng kế hoạch (100/200 = 50% → Đạt).
  >  ⚠️ CẬP NHẬT 27/07/2026 17:22 — dev ĐÃ sửa bộ lọc của thẻ Dashboard "Điểm đánh giá hiệu quả"
  >    (BUG-TKDGHQ-KPI-LOC → Closed). Thẻ nay LOẠI kết quả của kế hoạch HUY và kết quả CHUA_DANH_GIA:
  >    hiển thị **8.2/100 · "Dựa trên 10 đánh giá"** thay vì 29.5/100 · 14 như trước. Hai bản ghi gây lệch
  >    (DG-20260727-0001 HUY + 3 bản ghi KHDG-SEED-0001) VẪN CÒN trong env — giữ nguyên, đừng xóa: chúng
  >    chính là tiền đề để re-verify lần sau chứng minh bộ lọc còn hoạt động. Số 29.5/16.6 nêu ở các báo
  >    cáo trước ngày 27/07 là số TRƯỚC khi sửa, không dùng để đối chiếu nữa.
  >  ⚠️ Ngoài ra env có 3 bản ghi cũ KHDG-SEED-0001 (0 tiêu chí, trạng thái kết quả CHUA_DANH_GIA nhưng
  >    đã có sẵn điểm 80/60/90 thang 0-100) — chính là 3 cột 02/2026, 04/2026, 05/2026 trên biểu đồ.
  > Chi tiết + số liệu đối chiếu: reverify-week-4/reverify-audit/TKDGHQHTPL_02/audit.md

  --- SEED DATA (Hỏi đáp, 27/07/2026) — bản ghi TIEP_NHAN để re-verify bộ lọc trạng thái ---
  > Env: nip.io (18.143.165.120). KHÔNG seed gì lên env đối tác ospgroup.
  >  - HD-20260727-001 (id 9ebc16dd-1e33-416e-b5fc-5c99b5f68da2): trạng thái **TIEP_NHAN**, lĩnh vực Thuế,
  >    tạo bằng luồng chuẩn (tạo hỏi đáp → POST /api/v1/hoi-daps/{id}/tiep-nhan) bởi cbnv_tw.
  >  Vì sao phải tạo: thẻ "Đang xử lý" gộp 2 trạng thái TIEP_NHAN + DANG_XU_LY, nhưng env chỉ có 1 bản ghi
  >    DANG_XU_LY → thẻ chỉ chứa 1 trạng thái, lọc kiểu gì cũng "đúng" tình cờ và che mất lỗi. Bản ghi này
  >    làm thẻ có đủ 2 trạng thái, đúng tiền đề của BUG-TKHDVMTH_07 (§Nguyên tắc 4).
  >  ⚠️ GIỮ LẠI, đừng chuyển trạng thái: chuyển đi là thẻ "Đang xử lý" lại còn 1 trạng thái và lần re-verify
  >    sau sẽ không đo được gì. Thẻ "Hoàn thành" đã sẵn đủ 2 trạng thái (HD-20260707-005 HOAN_THANH +
  >    HD-20260708-002 HUY), không cần seed thêm.
  > Chi tiết phép đo: reverify-week-1/cond/TKHDVMTH_07-r3-reverify2.md
