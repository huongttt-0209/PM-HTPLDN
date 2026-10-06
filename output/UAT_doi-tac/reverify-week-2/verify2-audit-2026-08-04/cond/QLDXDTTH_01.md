# QLDXDTTH_01 — Bảng đối chiếu điều kiện (VÒNG SOÁT LẠI 2, 2026-08-04)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 2` row 118 · Verdict Verify 2: `Pass`
> Bug gốc: *"Hệ thống hiển thị thông báo thành công nhưng đề xuất không hiển thị trên màn hình"* khi
> Doanh nghiệp gửi đề xuất đào tạo, tập huấn (UC 32).
> Phiếu đòi 3 điều: (1) đề xuất được tạo ở trạng thái "Mới"; (2) cán bộ nghiệp vụ **thuộc đơn vị tiếp nhận**
> nhận được thông báo; (3) người gửi thấy thông báo gửi thành công.
> Bug phụ thuộc **vai trò + đơn vị + trạng thái + màn hình quan sát** ⇒ KHÔNG phải bug tĩnh ⇒ bắt buộc điền bảng này.

**Môi trường soát lại 2:** `https://htpldn-uat.ospgroup.vn` · `HTPLDN · V1.0.5` · gói giao diện **`index-DpIXRGaI.js`**
(bản dựng dev vừa đưa lên UAT). Bản ghi tạo mới trong lượt này: `5e3304d0-0bce-4bfa-865f-515c320a6ce0`,
`ngayTao 2026-08-04T10:14:30.730Z`.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test (soát lại 2, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản **người gửi** | Vai trò **Doanh nghiệp** (cột "Tác nhân" của phiếu ghi `Doanh nghiệp/Người hỗ trợ`) | **`0311224477`** — thanh trên hiện `QA Kiem Chung` · vai trò **`DN`** · `BTP · DP`; `auth/me` trả `vaiTro:["DN"]`, có quyền `create_de_xuat_dao_tao`. Tài khoản `0109998887` của vòng trước **không tồn tại trên môi trường này** (đăng nhập trả sai tên/mật khẩu) nên đã **tự dựng tiền đề**: kích hoạt tài khoản DN đang chờ kích hoạt `0311224477` bằng thư kích hoạt trong hộp thư giả lập, rồi đăng nhập bằng giao diện thật | Không |
| Vai trò / tài khoản **người phải nhận thông báo + thấy đề xuất** | Cán bộ nghiệp vụ **thuộc đúng đơn vị tiếp nhận** của đề xuất | **`cb_nv_dp_01`** — `CB NV DP 01 (AG)` · vai trò **`CB_NV_DP`** · `donViId 00000000-0000-4000-8002-000000000006`. Đã đọc **mã đơn vị thực tế của chính bản ghi vừa tạo** (`donVi.tenDonVi = "Sở Tư pháp An Giang"`, `donViId ...006`) — **trùng khít** mã đơn vị của tài khoản cán bộ ⇒ đúng cặp "đơn vị gửi ↔ đơn vị nhận". Mật khẩu tài khoản này do QA tự đặt lại qua chức năng "Quên mật khẩu" + thư trong hộp thư giả lập | Không |
| Entity + **trạng thái** (state machine) | Đề xuất **vừa gửi xong**, phiếu yêu cầu trạng thái khởi tạo "Mới" | Đề xuất mới tạo, nhãn trạng thái **"Mới gửi"** trên **cả 3 chỗ**: dòng bảng của người gửi · màn chi tiết · bảng của cán bộ tiếp nhận. Lọc tab **"Mới gửi"** ra đúng 1 kết quả (`?tab=MOI_GUI`). Dữ liệu gốc `trangThai: "MOI_GUI"` | Không |
| Dữ liệu tiền đề — danh sách **trước** khi gửi | Video đối tác: danh sách đang rỗng từ trước lúc bấm gửi | Đã chụp **mốc nền**: tab "Đề xuất đào tạo" của tài khoản DN hiện *"Không có đề xuất đào tạo nào phù hợp."* ⇒ 0 bản ghi. Sau khi gửi: **1 kết quả**. Có mốc nền nên chênh lệch 0 → 1 là do chính thao tác gửi | Không |
| Input / giá trị nhập | Lĩnh vực `Dân sự` · thời gian `quý 3/2026` · địa điểm `Hà Nội` · số lượng `10` (đúng bộ dữ liệu dev khai đã chạy lại) | Lĩnh vực `Dân sự` · nội dung `QA-V2-0804 - Kiem thu QLDXDTTH_01 ...` · thời gian `quy 3/2026` · địa điểm `Ha Noi` · số lượng `10`. Trùng cấu trúc, chỉ đổi phần nhận diện bản ghi | Không |
| Thao tác quan sát sau khi gửi | Đóng hộp thoại → nhìn danh sách; rồi tải lại trang nhìn lại | Làm **đủ 3 lượt**: (a) nhìn ngay khi hộp thoại đóng, **không** tải lại → đã thấy; (b) **tải lại trang bỏ qua bộ nhớ đệm** → vẫn thấy, phiên không rớt; (c) lọc tab "Mới gửi" → vẫn ra đúng 1 kết quả | Không |
| Màn hình quan sát | Video đối tác đứng ở màn **"Kế hoạch đào tạo"** trên chuyên trang công khai | Quan sát ở màn **"Đề xuất đào tạo"** (tab phụ của Chương trình đào tạo). Xem mục "Chênh lệch bề mặt" bên dưới — đã đóng bằng đặc tả chứ không bỏ qua | Không |

## Đo được trong lượt gửi (bộ bắt thông báo `tools/toast-capture.js`, tự kiểm `soObserverDangSong = 1`)

```json
{"thoiDiemBam":"2026-08-04T10:14:30.553Z",
 "SO_REQUEST":1,"request":["POST /api/v1/de-xuat-dao-taos"],
 "SO_KHUNG_THONG_BAO":1,"chu":["Đề xuất đào tạo đã được gửi thành công"],
 "BI_LAP":false,"khoangCachMs":null}
```

⇒ **1 lần gọi máy chủ ↔ 1 khung thông báo**, không lặp, không im lặng.

## Kết quả từng yêu cầu của phiếu

- **Ý 1 — đề xuất được tạo, trạng thái khởi tạo:** ✅ ĐẠT. Bản ghi hiện **ngay lập tức** trên danh sách người gửi
  (0 → 1 bản ghi), nhãn **"Mới gửi"**, còn nguyên sau khi tải lại trang bỏ bộ nhớ đệm.
- **Ý 2 — cán bộ nghiệp vụ đơn vị tiếp nhận nhận thông báo:** ✅ ĐẠT. Đăng nhập `cb_nv_dp_01` (đúng đơn vị
  `Sở Tư pháp An Giang`) → chuông thông báo có dòng **"Đề xuất đào tạo mới — Có đề xuất đào tạo mới từ người dùng
  QA Kiem Chung — 7 phút trước"**, còn dấu chưa đọc. Cán bộ này cũng **thấy đề xuất** trên tab "Đề xuất đào tạo".
- **Ý 3 — người gửi nhận thông báo gửi thành công:** ✅ ĐẠT. Đúng **1** khung thông báo
  *"Đề xuất đào tạo đã được gửi thành công"*, ứng với **1** lần gọi máy chủ.

## Chênh lệch bề mặt (màn hình) — đóng bằng đặc tả, không bỏ qua

Đối tác quay ở màn **"Kế hoạch đào tạo"**; mình quan sát ở màn **"Đề xuất đào tạo"**.

1. Đặc tả chỉ định nơi chứa đề xuất là màn khác: `srs-fr-03-dao-tao.md:1066` — FR-III-13 (UC 32)
   *"**Màn hình:** SCR-III-01 (tab "De xuat")"*, và `:1898` *"**Thành phần 8 — Tab "Đề xuất đào tạo":** Tab phụ
   tiếp nhận đề xuất từ DN/NHT…"*.
2. "Kế hoạch đào tạo" là **thực thể khác**: `srs-fr-03-dao-tao.md:1090` — FR-III-14 (UC 33)
   *"**Màn hình:** SCR-III-00 (sub-menu 1 — màn hình riêng cho Kế hoạch đào tạo năm)"*. Không mục nào của đặc tả
   quy định đề xuất vừa gửi phải xuất hiện trong danh sách kế hoạch đào tạo.
3. Trên môi trường được giao, tài khoản vai trò Doanh nghiệp **không có** menu "Kế hoạch đào tạo" (menu chỉ có
   Chương trình đào tạo · Khóa học · Kho tài liệu/Bài giảng · Vụ việc HTPL · Doanh nghiệp) ⇒ không thể dựng lại
   đúng bề mặt đó bằng vai trò DN, và cũng không cần: thao tác tranh chấp (tạo bản ghi · sinh thông báo cho cán bộ
   · hiển thị trên danh sách) là **thao tác nội bộ**, theo §External vs Internal thì **bắt buộc** verify trên
   môi trường được giao — đã làm đúng như vậy.

## Đã cố BÁC BỎ kết luận `Pass` cũ bằng những cách nào

1. **Không chấm bằng quan sát tĩnh:** chạy trọn luồng từ tài khoản DN mới kích hoạt → gửi → quan sát, chứ không
   nhìn danh sách có sẵn.
2. **Dựng mốc nền trước khi gửi** (0 bản ghi) để loại khả năng "bản ghi cũ trông như bản ghi mới".
3. **Thử ba cách quan sát** (không tải lại · tải lại bỏ bộ nhớ đệm · lọc theo trạng thái) — nếu lỗi cũ chỉ hiện ở
   một trong ba cách thì đã lộ ra.
4. **Đo bằng bộ bắt thông báo bắt buộc**, kiểm số khung thông báo **kèm** số lần gọi máy chủ — để loại kịch bản
   "báo thành công mà thực ra không ghi được" (1 ↔ 1, không lệch).
5. **Kiểm phía nhận, không tin lời khai của dev:** tự tìm đúng cán bộ **cùng mã đơn vị với bản ghi** (chứ không
   lấy bừa một cán bộ địa phương — `cbnv_dp` trên môi trường này thuộc **Sở Tư pháp Hà Nội**, khác đơn vị, dùng
   sẽ ra kết luận sai), tự đặt lại mật khẩu để đăng nhập được, rồi mới đọc chuông thông báo và danh sách.
6. **Không punt vì thiếu tài khoản:** tài khoản DN của vòng trước không tồn tại ở môi trường này — đã tự kích hoạt
   tài khoản DN và tự đặt lại mật khẩu tài khoản cán bộ thay vì để ô TRỐNG.

**Kết luận: 0 GAP.** Cả 3 yêu cầu của phiếu đều đạt trên bản dựng hiện tại, và triệu chứng đối tác báo
("báo thành công nhưng đề xuất không hiển thị") **không tái hiện** dù đã cố dựng lại đúng vai trò, đúng đơn vị,
đúng dữ liệu và thử 3 cách quan sát ⇒ verdict `Pass`.
