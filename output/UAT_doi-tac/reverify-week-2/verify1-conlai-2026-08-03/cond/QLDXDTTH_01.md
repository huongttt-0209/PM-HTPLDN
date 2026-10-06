# QLDXDTTH_01 — Bảng đối chiếu điều kiện (verify vòng 1, 2026-08-03)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 118 · Cột P (dev) = `dev done` · Verdict QA = `Pass`
> Đối tác báo: *"Hệ thống hiển thị thông báo thành công nhưng đề xuất không hiển thị trên màn hình"*.
> Bug phụ thuộc **vai trò + đơn vị + trạng thái** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản **người gửi** | Tài khoản đã đăng nhập trên chuyên trang, chỉ hiện ảnh đại diện (không mở menu tài khoản trong suốt video nên không đọc được tên). Cột "Tác nhân" của sheet ghi **`Doanh nghiệp/Người hỗ trợ`** | Đăng nhập **`0109998887`** — header web hiện đúng `QA UAT Kiem Thu DN` · vai trò **`DN`** · `BTP · DP`. Đúng nhóm tác nhân DN mà sheet ghi | **Không** |
| Vai trò / tài khoản **người phải thấy đề xuất** | Không quan sát được trong video (đối tác không đăng nhập vai trò cán bộ) | Đăng nhập **`cbnv_hn`** — `QA CB Nghiep vu Ha Noi` · vai trò **`CB_NV_DP`**. Đã đối chiếu mã đơn vị của tài khoản này **trùng khít** mã đơn vị tiếp nhận của chính bản ghi vừa tạo (`00000000-0000-4000-8002-000000000001`) ⇒ đúng cán bộ của đơn vị tiếp nhận | **Không** |
| Entity + **trạng thái** (state machine) | Đề xuất vừa được gửi xong; trạng thái **không đọc được** (popup thành công không trả mã, đối tác không mở màn nào khác) | Đề xuất **mới tạo** `b69a9545-59e4-4121-9760-91be29b65c19`, trạng thái hiển thị **"Mới gửi"** (badge trên cả danh sách lẫn màn chi tiết), lọc tab "Mới gửi" ra đúng 1 kết quả. Đây đúng là trạng thái khởi tạo mà phiếu UAT yêu cầu | **Không** |
| Dữ liệu tiền đề — **đơn vị của người gửi vs đơn vị của cán bộ** | Đối tác chọn tay ô "ĐƠN VỊ TIẾP NHẬN" = **`Cục Bổ trợ tư pháp – Bộ Tư pháp`** (đọc từ frame `dense/t029.25s.jpg`) | Màn gửi đề xuất trên môi trường được giao **không có ô chọn đơn vị tiếp nhận** — hệ thống tự gán đơn vị tiếp nhận = đơn vị của người gửi. Vì vậy KHÔNG suy luận, mà **đọc mã đơn vị thực tế của bản ghi** rồi đăng nhập đúng cán bộ của đơn vị đó (`cbnv_hn`) để kiểm. Cả 2 mã đơn vị khớp nhau ⇒ đã test đúng cặp "đơn vị gửi ↔ đơn vị nhận" | **Không** |
| Input / giá trị nhập | Lĩnh vực `Dân sự` · Nội dung `TKM gửi đề xuất đào tạo cán bộ nghiệp vụ quý 3/2026` · Thời gian `quý 3/2026` · Địa điểm `Hà Nội` · Số lượng `10` | Lĩnh vực `Dân sự` · Nội dung `QA-VERIFY-0803 - Kiem thu QLDXDTTH_01: de xuat dao tao can bo nghiep vu quy 3/2026` · Thời gian `quy 3/2026` · Địa điểm `Ha Noi` · Số lượng `10`. Trùng cấu trúc, chỉ đổi phần nhận diện bản ghi | **Không** |
| Thao tác quan sát sau khi gửi | Đóng popup → nhìn danh sách; sau đó **tải lại trang** rồi nhìn lại | Nhìn danh sách ngay khi popup đóng (không tải lại) → **rồi tải lại trang có bỏ qua bộ nhớ đệm** → nhìn lại. Làm đủ **cả 2 lượt** như đối tác | **Không** |

## Chênh lệch bề mặt (màn hình) — đã đóng bằng chứng minh, không bỏ qua

- **Địa chỉ** — Đối tác: `uat.phapluat.gov.vn` (chuyên trang công khai). Mình test: `18.143.165.120.nip.io` (môi trường được giao cho đợt verify này).
- **Màn đang đứng** — Đối tác: **"Kế hoạch đào tạo"** (`/danh-sach-ke-hoach-dao-tao`). Mình test: tab **"Đề xuất đào tạo"** của màn Chương trình đào tạo.

**Vì sao chênh lệch này KHÔNG đổi kết quả** — chứng minh bằng chính bằng chứng của đối tác + đặc tả, không phải bằng lập luận suông:

1. **Màn đối tác đứng không phải nơi chứa đề xuất.** Frame `t000.00s.jpg` (đồng hồ trang `16:18:41`, tức **TRƯỚC** khi bấm gửi lúc `16:19:14`) cho thấy danh sách "Kế hoạch đào tạo" **đã rỗng sẵn** — *"Không tìm thấy kế hoạch đào tạo nào phù hợp."*. Một danh sách rỗng từ trước khi thao tác thì việc nó rỗng sau thao tác **không chứng minh** được bản ghi có được lưu hay không.
2. **Đặc tả chỉ định nơi hiển thị là một màn khác.** `srs-fr-03-dao-tao.md:1043` — *"**Màn hình:** SCR-III-01 (tab "De xuat")"* và `:1875` — *"**Thành phần 8 — Tab "Đề xuất đào tạo":** Tab phụ tiếp nhận đề xuất từ DN/NHT…"*. Không mục nào của SRS v3.5 quy định đề xuất phải xuất hiện trong danh sách **kế hoạch đào tạo**. Đây là 2 thực thể khác nhau.
3. **Chính phần mềm cũng nói vậy** — phụ đề popup thành công trong video: *"…sẽ nghiên cứu tổng hợp và **đưa vào kế hoạch đào tạo** sớm nhất"*, tức đề xuất **chưa** phải là kế hoạch đào tạo tại thời điểm gửi.
4. Chuyên trang là **một bản triển khai khác** (máy chủ khác, địa chỉ mạng khác `124.197.21.116` vs `18.143.165.120`), QA không được cấp tài khoản đăng nhập chuyên trang. Bản vá dev khai báo nằm trên môi trường được giao. Kiểm trên chuyên trang sẽ là kiểm một bản triển khai khác ⇒ không trả lời được câu hỏi "bản vá có chạy không".
5. Thao tác tranh chấp là **thao tác nội bộ** (tạo bản ghi · sinh thông báo cho cán bộ · hiển thị trên danh sách) ⇒ theo §External vs Internal của quy trình thì **bắt buộc verify trên môi trường được giao**, không được bỏ qua. Đã làm đúng như vậy.

⇒ **0 GAP.** Mọi tiền đề tạo được (tài khoản người gửi · tài khoản cán bộ đúng đơn vị · dữ liệu · trạng thái) đều đã tự tạo và test thật, không đóng bằng lập luận.
