# Bảng đối chiếu điều kiện — LBCKQTHCT_01 (row 34) — Lập báo cáo kết quả thực hiện chương trình

**Kết luận:** Open (Major).

Phiếu báo lỗi **403** *"Đơn vị không nằm trong phạm vi truy cập của bạn"* (`ERR-AUTH-VPD-00-02`, vai trò `CB_NV_DP`) khi mở màn chi tiết đợt báo cáo — tức tắc ở **bước 2** của phiếu.

Khi QA kiểm lại bằng đúng vai trò CB NV Địa phương: **bước 2 mở được bình thường**, không có màn 403. Nhưng đi tiếp đúng kịch bản thì **tắc ở bước 3**: bấm [Lập báo cáo] bị từ chối với *"Bản ghi đã tồn tại"*, trong khi chính hệ thống báo đơn vị **chưa nộp** và **chưa có báo cáo nào**.

⇒ Kết quả mong đợi của phiếu (lưu nháp thành công, trạng thái chuyển "Đang lập") **vẫn KHÔNG đạt** nên giữ **Open**, chỉ mô tả lại đúng điểm hỏng. → lỗi `BUG-BC-KHONG-LAP-DUOC-BAO-CAO`, kèm lỗi phụ `BUG-BC-TOAST-LOI-HIEN-2-LAN`.

| Điều kiện có thể đổi kết quả | Đối tác (evidence `partner-evidence/LBCKQTHCT_01.webm`) | Mình test (env nip.io, 27/07/2026 14:40–14:52) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Video cho thấy `CB_NV_DP` ("Cán bộ NV Địa phương"), badge đơn vị "BTP · DP". Màn 403 tự ghi rõ *"Vai trò hiện tại: CB_NV_DP"* | `cbnv_dp` — CB Nghiệp vụ - Địa phương, cấp đơn vị `DP`, badge "BTP · DP". Trùng khít. Đúng tác nhân đặc tả yêu cầu cho chức năng này (CB NV cấp ĐP/BN) | Không |
| Entity + trạng thái (state machine) | Video: màn `/ct-htpldn/dot-bao-cao`, thẻ "Tất cả", **1 đợt** `DOT-SO_BO_NAM-2026-1`, kỳ "Sơ bộ năm", phạm vi **86 đơn vị**, trạng thái hàng cuối "Tạo đợt" | Màn `/ct-htpldn/dot-bao-cao`, thẻ "Tất cả", **2 đợt** cùng dạng — `DOT-SO_BO_NAM-2026-1` (Sơ bộ năm) và `DOT-SO_BO_6_THANG-2026-1` (Sơ bộ 6 tháng), phạm vi **83 đơn vị**, cùng trạng thái **TAO_DOT**. Khác số lượng đợt và số đơn vị trong phạm vi, **nhưng cùng loại đợt và cùng trạng thái**; đã chạy phép đo trên CẢ HAI đợt để kết luận không phụ thuộc một bản ghi cá biệt | Không |
| Dữ liệu tiền đề | Phiếu chỉ ghi "Đăng nhập hệ thống thành công". Nhưng đặc tả đòi thêm 2 điều kiện: đơn vị nằm trong phạm vi đợt, và bản ghi nộp ở trạng thái chưa nộp / đang lập | Đã **chủ động kiểm và xác nhận đủ cả 3 điều kiện tiên quyết** trước khi chấm: vai trò CB NV cấp ĐP ✔; mã đơn vị của tài khoản **có mặt** trong danh sách đơn vị thuộc phạm vi của cả 2 đợt ✔; trạng thái nộp của đơn vị = *chưa nộp*, mã báo cáo *rỗng* ✔. Nhờ vậy loại được khả năng "lỗi do thiếu dữ liệu tiền đề" | Không |
| Input / filter / giá trị nhập | Video: mở danh sách → bấm biểu tượng Xem trên dòng đợt → chuyển sang màn 403. Không thấy nhập số liệu (chưa tới bước đó) | Mở danh sách → bấm Xem (vào được) → bấm [Lập báo cáo] → xác nhận [Đồng ý] trên hộp thoại. Đi xa hơn đối tác đúng 1 bước, tới đúng thao tác mà phiếu mô tả ở bước 3 | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Chặn thao tác / phân quyền)

- `partner-evidence/LBCKQTHCT_01.webm` (12,9 MB, ~57 giây) — **đã trích 15 khung hình và mở xem tới khoảnh khắc lỗi**, lưu ở `reverify-audit/LBCKQTHCT_01/frames/`:
  - `t000.00s` → `t052.67s`: xuyên suốt ở màn `/ct-htpldn/dot-bao-cao`, thẻ "Tất cả", đúng 1 dòng đợt `DOT-SO_BO_NAM-2026-1` — cột Phạm vi ghi "86 đơn vị", cột Trạng thái "Tạo đợt". Đọc được thanh trạng thái trình duyệt ở khung `t052.67s`: đích đến là `/ct-htpldn/dot-bao-cao/b9a98ab1-ec3d-458b-8b73-908a779…`
  - `t056.69s`: **khoảnh khắc lỗi** — trang `/403`, chữ lớn "403", dòng *"Đơn vị không nằm trong phạm vi truy cập của bạn"*, *"Mã lỗi: ERR-AUTH-VPD-00-02"*, *"Vai trò hiện tại: CB_NV_DP"*, hai nút [Về trang chủ] [Quay lại].
- `bug-reports/image/BUG-BC-chi-tiet-dot-bao-cao-mo-duoc.png` — đã mở đọc: màn chi tiết đợt báo cáo mở được bằng tài khoản CB NV Địa phương, có thanh tiến trình 6 bước và biểu mẫu 21a.
- `bug-reports/image/BUG-BC-hop-thoai-bat-dau-lap-bao-cao.png` — đã mở đọc: hộp thoại *"Bắt đầu lập báo cáo? — Hệ thống sẽ tạo báo cáo nháp để bạn nhập số liệu."* ngay trước khi xác nhận, phía sau là biểu mẫu 21a đủ 13 chỉ tiêu.

## Phương pháp thứ hai (bắt buộc)

- **Kiểm 3 điều kiện tiên quyết TRƯỚC khi kết luận — bước quan trọng nhất của case này.** Thông báo lỗi của đối tác nói "đơn vị không nằm trong phạm vi", nên giả thuyết cạnh tranh hiển nhiên là *hệ thống chặn đúng, chỉ là dữ liệu tài khoản chưa được đưa vào phạm vi*. Nếu đúng vậy thì đây không phải lỗi. Vì vậy QA đọc thẳng danh sách đơn vị thuộc phạm vi của từng đợt rồi đối chiếu với mã đơn vị của tài khoản: **có mặt ở cả 2 đợt**. Giả thuyết đó bị loại, và mọi kết luận sau đó mới có giá trị.
- **Phép thử quyết định — hệ thống tự mâu thuẫn.** Cùng một lần đọc dữ liệu màn chi tiết trả về: trạng thái nộp = *chưa nộp*, mã báo cáo = *rỗng*, không có báo cáo đính kèm, **và** liệt kê "bắt đầu lập" là thao tác đang mở cho người dùng. Nhưng thực hiện đúng thao tác đó thì bị từ chối với *"Bản ghi đã tồn tại"*. Hai phát biểu này không thể cùng đúng ⇒ đây là lỗi thật, không phải người dùng thao tác sai.
- **Lặp trên bản ghi thứ hai để loại "dữ liệu hỏng cá biệt".** Chạy lại toàn bộ trên đợt còn lại (`DOT-SO_BO_6_THANG-2026-1`, kỳ khác, cùng trạng thái): kết quả **giống hệt** — cùng bị từ chối, cùng mã lỗi. ⇒ Lỗi thuộc về luồng xử lý, không phải một bản ghi lỗi.
- **Đo bằng hai đường khác nhau cho cùng thao tác.** Bấm qua giao diện và gọi thẳng dịch vụ dữ liệu đều cho cùng một kết quả từ chối với cùng mã lỗi ⇒ không phải lỗi dựng giao diện, mà nằm ở tầng xử lý nghiệp vụ.
- **Đối chiếu đặc tả — trích nguyên văn 3 điều kiện tiên quyết:** `srs-fr-15-ct-htpldn.md:716` — *"User đã đăng nhập là CB NV cấp ĐP/BN"*; `:717` — *"Đợt BC định kỳ đã tạo (FR-XI-05a) và đơn vị user nằm trong `pham_vi_don_vi_nop_ids[]`"*; `:718` — *"`DOT_BAO_CAO_DON_VI_NOP` của (đợt, đơn vị) ở trạng thái CHUA_NOP hoặc DANG_LAP"*. Cả ba đều thoả nên hệ thống phải cho lập báo cáo. `:741` mô tả bước xác minh trạng thái nộp, `:746` mô tả việc chuyển trạng thái nộp sang *đang lập* sau khi lưu.
- **Đối chiếu quyền của vai trò để chắc không phải chặn đúng:** `:712` ghi tác nhân của chức năng này là *"**CB Nghiệp vụ cấp ĐP/BN** (đơn vị thuộc phạm vi đợt BC)"*, và `:621` mô tả *"CB NV cấp ĐP/BN của các đơn vị nộp được thông báo, vào tab "Đợt báo cáo" của đơn vị mình để lập + nộp báo cáo"*. ⇒ Vai trò đang dùng đúng là vai trò được giao nghiệp vụ này.
- **Về mã lỗi trong video của đối tác:** đã rà toàn bộ bộ SRS v3.5, **không có** mã `ERR-AUTH-VPD-00-02`. QA không lấy việc thiếu mã trong đặc tả làm căn cứ chấm lỗi (đặc tả không liệt kê hết mã hệ thống), chỉ ghi nhận để dev đối chiếu khi truy nguyên.
- **Ghi nhận lỗi phụ phát hiện khi đo:** một lần bấm chỉ gửi **1** yêu cầu nhưng giao diện hiện **2** thông báo lỗi chồng nhau (bộ bắt thông báo không lọc trùng, đếm được 2 thẻ báo cùng mốc thời gian). Tách riêng thành `BUG-BC-TOAST-LOI-HIEN-2-LAN` vì hướng sửa khác: lỗi chính ở tầng xử lý, lỗi này ở chỗ gắn thông báo vào giao diện.
