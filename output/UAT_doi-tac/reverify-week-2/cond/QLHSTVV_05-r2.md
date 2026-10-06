# Bảng đối chiếu điều kiện — QLHSTVV_05 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** "Khi nhấn xem chi tiết hệ thống điều hướng đến màn hình thông báo **'403-Forbidden'**".

**Bối cảnh ca kiểm thử:** kiểm tra thẻ **"Thẩm định"** có bị ẩn hoàn toàn khi người dùng là Người hỗ trợ pháp lý hay Doanh nghiệp. Vòng 1 đối tác báo thẻ này **vẫn hiện** với vai trò Người hỗ trợ; vòng 2 họ không đánh giá được tiêu chí đó nữa vì màn chi tiết bị chặn.

**Evidence:** `QLHSTVV_04_v2.webm` — video ~11 giây (trích khung bằng `tools/extract_frames.py`, thêm dải 0,5 s/khung đoạn 4–7 s).
Diễn biến đọc được:
- t≈4,0–5,1 s — danh sách `/chuyen-gia-tvv/danh-sach?trangThai=MOI_DANG_KY`, tab **"Mới đăng ký" (3)**, 3 bản ghi `TVV-STP-HN-0002/0003/0004`, tổ chức "Test thêm mới tổ chức địa phương". Cột **Hành động** hiển thị **Xem · Sửa · Xóa**.
- t≈5,1 s — con trỏ nằm trên liên kết **"Xem"** của dòng `NHT TKM` (`TVV-STP-HN-0004`, trạng thái **Mới đăng ký**).
- t≈5,6–8,1 s — trang chuyển sang **`/403`**: "403 — Forbidden — Mã lỗi: **ERR-PERM-SYS-00-01** — Vai trò hiện tại: **NHT**".

Header trong video: **"BTP · DP"**, tài khoản **"hương 3 NHT"**, vai trò **NHT**; đồng hồ máy 25/07/2026 16:47, trình duyệt Cốc Cốc trên Windows.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | **NHT** (Người hỗ trợ pháp lý) — trang 403 tự khai báo "Vai trò hiện tại: NHT" | `nht_qa_01` — dữ liệu tài khoản trả về `vaiTro = ["NHT"]`, chỉ một vai trò duy nhất | Không |
| Cấp đơn vị | Cấp **địa phương** (badge "BTP · DP"), bản ghi mã `TVV-STP-…` (Sở Tư pháp) | Cấp **địa phương** — `nht_qa_01` thuộc Sở Tư pháp An Giang, bản ghi mã `TVV-STP-AG-…` | Không |
| Quan hệ đơn vị người xem ↔ tư vấn viên | Bản ghi hiện trong danh sách của chính tài khoản NHT ⇒ trong phạm vi đơn vị của họ | **Cùng đơn vị** — đã đối chiếu mã đơn vị của tài khoản và của cả 3 bản ghi: trùng khít `…8002-000000000006` | Không |
| Màn hình + đường vào | Danh sách Tư vấn viên → cột Hành động → liên kết **"Xem"** → `/chuyen-gia-tvv/{id}` | Cùng đường vào: danh sách → cột Hành động → liên kết **"Xem"** (đọc đúng nhãn "Xem" trong dòng rồi mới bấm) | Không |
| Tab danh sách + trạng thái bản ghi | Tab **"Mới đăng ký"**, bản ghi trạng thái **Mới đăng ký** | Tab **"Mới đăng ký"**, bản ghi `TVV-STP-AG-0003` trạng thái **Mới đăng ký** — đơn vị này chưa có bản ghi nào ở trạng thái đó nên QA **tạo mới một bản ghi** bằng chính tài khoản NHT để khớp điều kiện | Không |
| Loại bản ghi | Tư vấn viên (TVV) | Tư vấn viên (TVV) | Không |
| Trình duyệt / kích thước cửa sổ | Cốc Cốc trên Windows, cửa sổ tối đa | Chrome 1440×900 — kết luận dựa trên mã trả về của lời gọi máy chủ + đường dẫn trang nên không phụ thuộc kích thước cửa sổ | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng cấp, cùng quan hệ đơn vị, cùng đường vào, cùng tab và cùng trạng thái bản ghi.

**Kết quả tái hiện: tái hiện MỘT PHẦN, đúng bản chất.**
- Bấm "Xem" mở chi tiết: **không** còn tự chuyển `/403` như video đối tác — màn chi tiết hiện đầy đủ.
- Nhưng chỉ cần bấm thêm **một** thẻ trên chính màn đó — thẻ **"Lịch sử hỗ trợ"**, thẻ mà đặc tả ghi điều kiện hiển thị là **"Luôn"** — thì cả trang bị đẩy sang **đúng trang `/403` — `ERR-PERM-SYS-00-01` — "Vai trò hiện tại: NHT"** mà đối tác chụp được.

Toàn bộ phép đo + 2 sai lệch khác QA phát hiện trên cùng màn: [`../reverify-audit/QLHSTVV_05/audit.md`](../reverify-audit/QLHSTVV_05/audit.md).
