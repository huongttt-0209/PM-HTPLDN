# Bảng đối chiếu điều kiện — QLKCHTV_22 (row 11) — Cột dữ liệu trong bảng kết quả Tư vấn nhanh

**Kết luận:** Open, BA confirm.
- **Open:** bảng thiếu **2 cột đặc tả yêu cầu** (`CB xử lý`, `Ngày trả lời`) và **thừa 1 cột** (`Số gợi ý`) — căn cứ `srs-fr-13-tv-nhanh.md:569`.
- **BA confirm:** ý đối tác nêu (Ngày gửi thiếu giờ HH:mm) **tái hiện đúng** nhưng đặc tả v3.5 KHÔNG quy định định dạng giờ cho cột này ⇒ cần BA chốt.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/QLKCHTV_22.jpg`) | Mình test (env nip.io, 27/07/2026 11:54) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — "Cán bộ NV Trung ương", badge "BTP · TW" (đọc rõ ở góc phải ảnh) | `cbnv_tw` — CB Nghiệp vụ - Trung ương, BTP · TW — TRÙNG KHỚP. Đặc tả giao màn này cho Cán bộ Nghiệp vụ: `srs-fr-13-tv-nhanh.md:178` *"**Tác nhân:** Cán bộ Nghiệp vụ"* | Không |
| Entity + trạng thái (state machine) | Bảng Tư vấn nhanh, thẻ "Tất cả"; các dòng ở nhiều trạng thái: Hoàn thành / CB trả lời / Hết hạn / Đang tìm kiếm | Bảng Tư vấn nhanh, thẻ "Tất cả"; 3 dòng ở trạng thái **CB trả lời** + (sau khi dựng thêm) 1 dòng **Hoàn thành** | Không |
| Dữ liệu tiền đề | Môi trường đối tác có sẵn phiên tư vấn nhanh | Môi trường nip.io **ban đầu 0 phiên** → QA **tự dựng 4 phiên** qua `POST /api/v1/tu-van-nhanhs/cms-create` (kênh TV Nhanh, gắn DN "Công ty TNHH QA Reverify R5" có MST 0198877665) rồi mới đo. Cột bảng là thành phần giao diện tĩnh, không phụ thuộc số lượng bản ghi | Không |
| Input / filter / giá trị nhập | Không lọc — mở thẳng menu Tư vấn → Tư vấn nhanh | Không lọc — mở thẳng menu Tư vấn → Tư vấn nhanh. **Bổ sung** đo thêm ở thẻ "Hoàn thành" để chắc bộ cột không đổi theo thẻ | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hiển thị/render)

- `bug-reports/image/BUG-TVN-danh-sach-cot-va-hanh-dong.png` — đã mở đọc: bảng đúng 8 cột, cột "Ngày gửi" hiện `27/07/2026`, cột "Ngày cập nhật" hiện `27/07/2026 11:54`.
- Đọc thẳng tiêu đề bảng bằng mã lệnh: `["Mã phiên","Câu hỏi DN","Kênh","Số gợi ý","Trạng thái","Ngày gửi","Ngày cập nhật","Hành động"]` — đo lại ở cả thẻ "Tất cả" và thẻ "Hoàn thành", **kết quả giống nhau**.
- Đọc nội dung 3 dòng: `Ngày gửi = "27/07/2026"` (không giờ) · `Ngày cập nhật = "27/07/2026 11:54"` (có giờ) ⇒ **không nhất quán ngay trong cùng một bảng**.

## Phương pháp thứ hai (bắt buộc)

- **Đối chiếu tầng dữ liệu để loại trừ "máy chủ không có giờ":** `GET /api/v1/tu-van-nhanhs/{id}` trả `"ngayGui":"2026-07-27T04:54:02.624Z"` — **có đầy đủ giờ phút giây**. Vậy phần giờ bị mất ở khâu hiển thị, không phải thiếu ở dữ liệu.
- **Đối chiếu đặc tả từng cột** (`srs-fr-13-tv-nhanh.md:569`, §3 SCR-X2-03 dòng 5): *"Bang TV nhanh | table | Ma phien / Cau hoi DN (cat 100 ky tu) / Kenh (TV_NHANH xanh / TV_THU_CONG vang) / **CB xu ly** / Trang thai SM-TVNHANH (C06) / Ngay gui / **Ngay tra loi** / Ngay cap nhat / Hanh dong (Xem / Tra loi)"*

  Đối chiếu từng cột đặc tả `:569` với hệ thống thực tế:
  - Mã phiên → ✅ có
  - Câu hỏi DN → ✅ có
  - Kênh → ✅ có
  - **CB xử lý → ❌ THIẾU**
  - Trạng thái → ✅ có
  - Ngày gửi → ✅ có
  - **Ngày trả lời → ❌ THIẾU**
  - Ngày cập nhật → ✅ có
  - Hành động → ✅ có (nhưng chỉ 1 hành động — xem QLKCHTV_24)
  - *Số gợi ý* → ⚠️ **THỪA**, không có trong đặc tả

  Dữ liệu cho 2 cột thiếu **đã có sẵn ở máy chủ**: `nguoiTraLoi: {hoTen: "CB Nghiệp vụ - Trung ương"}` và `ngayTraLoi: "2026-07-27T05:00:22.095Z"` ⇒ chỉ cần bổ sung cột hiển thị.
- **Tra định dạng ngày trong đặc tả:** quy ước UI-06 (`srs-v3.5.md:576`) chỉ ghi *"Định dạng ngày: dd/MM/yyyy"*, không nói tới giờ. Các module khác **có** quy định rõ định dạng có giờ cho cột kiểu ngày-giờ (vd `srs-fr-02-hoi-dap.md:1043` *"Cột Ngày tạo | table-column | dd/mm/yyyy HH:mm"*), nhưng §3 SCR-X2-03 của Tư vấn nhanh **không có bảng định dạng đầu ra** nào ⇒ không có câu chữ để đối chiếu ⇒ phần "thiếu giờ" phải để BA chốt (BA-10).
- **Ghi chú cột thừa:** cột "Số gợi ý" luôn hiện `0` và trường `goiYTraLoi` của máy chủ luôn `null`. Đặc tả FR-X.2-02 bước 2 (`srs-fr-13-tv-nhanh.md:196`) còn nói rõ *"khu vực 'Tra cứu Kho câu hỏi' hiển thị ô tìm kiếm rỗng, **không tự động tìm kiếm và không prefill** từ câu hỏi DN"* ⇒ hệ thống không sinh gợi ý tự động, nên cột này vừa thừa vừa luôn rỗng nghĩa.
