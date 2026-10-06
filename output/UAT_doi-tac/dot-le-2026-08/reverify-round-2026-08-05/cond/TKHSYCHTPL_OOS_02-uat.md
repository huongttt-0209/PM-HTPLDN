# TKHSYCHTPL_OOS_02 — đo lại trên môi trường nghiệm thu đối tác (05/08/2026)

Tiêu chí lấy nguyên khối ở cột `DEV phản hồi lần 1`, dòng 155 (tab `UAT_TGPL Doanh Nghiệp-tuần 2`).

| Điều kiện | Bug gốc (khối tiêu chí) | Mình test | GAP? |
|---|---|---|---|
| Môi trường | Môi trường nghiệm thu của đối tác | `https://htpldn-uat.ospgroup.vn` — nhãn `HTPLDN · V1.0.7` | Không |
| Vai trò | `cbnv_tw` + màn Vụ việc HTPL | `cbnv_tw` · CB_NV_TW · cấp TW cho phần cán bộ; thêm tài khoản doanh nghiệp `0151554887` (TKM Company) cho luồng DN | Không |
| Luồng 1 — cán bộ nhập thủ công | Tạo mới 1 hồ sơ đi vào luồng xử lý | Tạo `VV-BTP-TW-20260805-004` bằng [Lưu nháp] (ra "Mới tạo") rồi bấm [Tiếp nhận] để đẩy vào luồng; thêm `VV-BTP-TW-20260805-003` tạo thẳng bằng [Lưu & Tiếp nhận] | Không |
| Luồng 2 — doanh nghiệp gửi yêu cầu | Tạo mới 1 hồ sơ đi vào "Chờ tiếp nhận" | Đăng nhập tài khoản DN, bấm [Gửi yêu cầu hỗ trợ pháp lý] → `VV-STP-HN-20260805-003`, trạng thái "Chờ tiếp nhận" | Không |
| Màn đọc kết quả | Danh sách vụ việc, cột "Thời hạn xử lý" + "Cảnh báo thời hạn" | Đúng hai cột đó trên màn danh sách | Không |
| Phạm vi rà lại | Toàn bộ danh sách, đếm hồ sơ đã qua tiếp nhận mà trống thời hạn | Rà **72/72** hồ sơ ở cả 10 trạng thái (đối chiếu dữ liệu máy chủ) + rà 71/71 dòng trên 4 trang giao diện | Không |
| Nhóm loại trừ | Hồ sơ "Mới tạo" trống thời hạn là hợp lệ | Có kiểm chứng riêng: bản nháp `VV-BTP-TW-20260805-004` lúc còn "Mới tạo" đúng là chưa có thời hạn — không tính vào phạm vi | Không |
| Cách đo thứ 2 | Đọc trên giao diện | Đối chiếu thêm giá trị thời hạn + mức cảnh báo đang lưu ở phía máy chủ cho từng hồ sơ | Không |

**Kết luận: 0 GAP → PASS.**

## Đối chiếu từng ý của khối tiêu chí

- **Hồ sơ MỚI ở luồng doanh nghiệp gửi yêu cầu có thời hạn ngay**: gửi yêu cầu bằng tài khoản DN →
  `VV-STP-HN-20260805-003`, trạng thái **"Chờ tiếp nhận"**, cột Ngày tiếp nhận `05/08/2026`, cột **Thời hạn
  xử lý `20/08/2026`**, cột **Cảnh báo thời hạn "Bình thường · còn 11 ngày LV"**. Giá trị lưu ở máy chủ:
  `deadline = 2026-08-20T08:59:17Z`, `mucDoCanhBao = BINH_THUONG`. Đây chính là luồng mà phản ánh gốc dùng
  làm bằng chứng loại trừ giả thiết "chỉ là hồ sơ cũ" — nay luồng đó ra đủ thời hạn.
- **Hồ sơ MỚI ở luồng cán bộ nhập thủ công cũng có thời hạn**: `VV-BTP-TW-20260805-004` lưu nháp trước
  (trạng thái "Mới tạo", chưa có ngày tiếp nhận, chưa có thời hạn — **đúng như phần loại trừ của phiếu**),
  sau đó bấm [Tiếp nhận] → thông báo "Tiếp nhận vụ việc thành công", hồ sơ chuyển "Đã tiếp nhận" và **ngay
  lập tức** có Ngày tiếp nhận `05/08/2026 15:56` + Thời hạn xử lý `20/08/2026` + cảnh báo
  "Bình thường · còn 11 ngày LV". Tức bước tính thời hạn khi hồ sơ rời trạng thái "Mới tạo" đã chạy.
  Hồ sơ `VV-BTP-TW-20260805-003` tạo thẳng bằng [Lưu & Tiếp nhận] cũng có đủ thời hạn.
- **Không còn hồ sơ nào từ "Chờ tiếp nhận" trở đi mà trống thời hạn**: rà toàn bộ **72 hồ sơ** đang có,
  chia theo trạng thái — Chờ tiếp nhận 5 · Đã tiếp nhận 12 · Đang kiểm tra 3 · Đã phân công 23 ·
  Đang xử lý 4 · Chờ phê duyệt 3 · Đã duyệt 4 · Hoàn thành 8 · Đã đánh giá 4 · Từ chối 6 — **cả 10 nhóm đều
  0 hồ sơ trống thời hạn và 0 hồ sơ trống mức cảnh báo**. Phản ánh gốc đếm được 22/47 hồ sơ trống (20 hồ sơ
  đã vào luồng); con số đó nay về **0**. Nhóm hồ sơ cũ mà phản ánh gốc đề nghị rà lại và bổ sung đã được xử
  lý: các hồ sơ trạng thái Hoàn thành / Đã đánh giá / Đã duyệt / Đang xử lý đều đã có thời hạn.
- **Đọc trên giao diện cũng khớp**: rà 4 trang danh sách (71 dòng hiển thị lúc rà), **không dòng nào** để
  trống cột "Thời hạn xử lý"; cột "Cảnh báo thời hạn" chỉ ra 4 nhãn hợp lệ
  `Bình thường · Sắp hết hạn · Quá hạn · Quá hạn nghiêm trọng`.
- **Phần phiếu nói KHÔNG được chấm sai đã tôn trọng**: bản nháp lúc còn "Mới tạo" trống thời hạn — không
  dùng làm căn cứ trượt. Việc cột "Cảnh báo thời hạn" hiện dấu gạch khi chưa có thời hạn cũng không bị tính
  là lỗi.

Ảnh: `../image/TKHSYCHTPL_OOS_02-uat-moi-ho-so-deu-co-thoi-han.png` (danh sách phía cán bộ) ·
`../image/TKHSYCHTPL_OOS_02-uat-luong-dn-gui-yeu-cau-co-thoi-han.png` (hồ sơ mới của luồng DN)

## Ghi nhận thêm

- **Trùng mã với phản ánh gốc — đừng nhầm hai hồ sơ.** Phản ánh gốc nêu 3 hồ sơ
  `VV-STP-HN-20260805-001/002/003`. Lúc bắt đầu đo, trên môi trường chỉ còn `-001` và `-002` (cả hai **đã
  có** thời hạn `20/08/2026`); mã `-003` được cấp lại cho chính hồ sơ mình vừa gửi trong lượt đo này. Khi
  đối chiếu về sau cần phân biệt: `VV-STP-HN-20260805-003` hiện tại là hồ sơ kiểm thử tạo 05/08/2026 15:59,
  tiêu đề mở đầu "QA UAT 05-08".
- Mốc hạn vẫn cộng **+15 ngày lịch** (05/08 → 20/08) thay vì +15 ngày làm việc như đặc tả — điểm này đã ghi
  ở `cond/NHSYC_OOS_02-uat.md`, không thuộc phạm vi phiếu này.
- Dữ liệu phát sinh khi đo (là bước bắt buộc của chính kịch bản): 2 hồ sơ vụ việc mới —
  `VV-BTP-TW-20260805-004` (cán bộ nhập thủ công, nay "Đã tiếp nhận") và `VV-STP-HN-20260805-003`
  (doanh nghiệp gửi, "Chờ tiếp nhận"). Không sửa, không xóa hồ sơ nào có sẵn.
- Tài khoản doanh nghiệp dùng cho luồng DN trên môi trường này: `0151554887` (TKM Company, tên đăng nhập
  chính là mã số thuế) — đã bổ sung vào `input/input.md`.
