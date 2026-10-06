# QLDKTK_01 — Bảng đối chiếu điều kiện (re-verify vòng 2 lần 2, 04/08/2026)

> Sheet `UAT_TGPL Doanh Nghiệp-tuần 3` dòng 321. Vòng trước (04/08 16:00) QA chấm `Reopen` vì
> **ý 2 còn lỗi**: nhập dữ liệu hoàn toàn mới nhưng chọn Tỉnh/Thành phố = **Hà Nội** thì bị chặn bằng câu
> "Mã số thuế đã tồn tại trong hệ thống". Sau đó dev đặt lại `Trạng thái dev fix 2` = `dev done`
> ⇒ verify lại **cả 4 ý** của phiếu.

**Môi trường đo:** `https://18.143.165.120.nip.io` (đúng môi trường ghi trong `input/input.md`) ·
nhãn bản dựng **HTPLDN · V1.0.6** — mới hơn bản `V1.0.5` của vòng trước.
**Vai trò:** khách vãng lai (màn hình đăng ký không cần đăng nhập); đối chiếu dữ liệu bằng `admin` và `cbnv_tw_02`.

| Điều kiện có thể đổi kết quả | Điều kiện bug gốc (vòng 2) | Mình test (04/08/2026 lần 2) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Khách vãng lai, chưa đăng nhập, vào màn hình Đăng ký tài khoản doanh nghiệp | Giống hệt — mở `/register/doanh-nghiep` trong ngữ cảnh trình duyệt sạch (browser context riêng), không đăng nhập | Không |
| Màn hình / thực thể + trạng thái | Màn hình đăng ký doanh nghiệp; mã số thuế chưa có bản ghi nào trong hệ thống | Giống hệt — kiểm bằng tài khoản có quyền: 3 mã số thuế thử nghiệm đều **không có** trong danh sách doanh nghiệp lẫn danh sách tài khoản trước khi chạy | Không |
| Dữ liệu nhập — ô Tỉnh/Thành phố (biến gây lỗi ở vòng trước) | Tỉnh/Thành phố = **Hà Nội** | Giống hệt — cả 3 lượt đăng ký đều chọn **Hà Nội** | Không |
| Dữ liệu tiền đề — dãy mã doanh nghiệp của Hà Nội vẫn còn "thủng số" | Vòng trước lỗi vì số thứ tự cấp cho Hà Nội đâm vào mã đã tồn tại | Dãy Hà Nội trước khi test: `DN-HNI-0001 · 0002 · 0003 · 0005 · 0006` — **vẫn thủng số 0004**, tức điều kiện sinh lỗi cũ CHƯA bị dọn đi | Không |
| Thao tác | Điền đủ trường bắt buộc rồi bấm Đăng ký | Giống hệt — điền đủ, bấm Đăng ký, bắt thông báo bằng bộ đo chuẩn (không lọc trùng) + đếm số request | Không |

**Kết luận: 0 GAP** — quan trọng nhất là **dãy mã Hà Nội vẫn còn lỗ hổng số**, nên đây là phép thử thật
chứ không phải "hết lỗi vì dữ liệu đã sạch".

## Kết quả từng ý của phiếu

- **Ý 1 — các trường trên biểu mẫu khớp tài liệu (lỗi gốc vòng 1):** ✅ **Đạt.** Biểu mẫu có đúng **28 mục nhập liệu + 2 nút Hủy / Đăng ký**, khớp bảng thành phần màn hình. Ô "Tên đăng nhập" chỉ đọc và tự điền theo Mã số thuế (hiện `0455667788` ngay khi nhập). Ba danh sách chọn cố định đúng: Quy mô (Siêu nhỏ / Nhỏ / Vừa), Ngành nghề chính (Nông lâm thủy sản / Công nghiệp xây dựng / Thương mại dịch vụ), Lĩnh vực kinh doanh chọn nhiều ngành cấp 4. Chênh duy nhất vẫn là "Doanh nghiệp do nữ làm chủ" được vẽ bằng công tắc thay vì ô tích — đã ghi nhận từ vòng 1, không cản trở nhập liệu.
- **Ý 2 — nhập thông tin hợp lệ rồi bấm Đăng ký thì đăng ký được:** ✅ **Đạt.** Chọn Tỉnh/Thành phố = Hà Nội, mã số thuế mới → đăng ký chạy trọn. **2/2 lượt thành công**, không lượt nào bị chặn.
- **Ý 3 — sau khi đăng ký hiện thông báo thành công + gửi thư kích hoạt:** ✅ **Đạt.** Hiện đúng 1 thông báo "Đăng ký thành công, vui lòng kiểm tra email kích hoạt" (đúng 1 request gửi đi), tạo tài khoản trạng thái Chờ kích hoạt với tên đăng nhập = mã số thuế, thư "Kích hoạt tài khoản doanh nghiệp" về đúng hòm thư đã khai. Bấm liên kết trong thư → tài khoản chuyển sang Đang hoạt động và đăng nhập được ngay bằng mã số thuế.
- **Ý 4 — khi mã số thuế trùng THẬT thì báo đúng cách:** ✅ **Đạt.** Đăng ký lại bằng chính mã số thuế vừa tạo (cùng tỉnh Hà Nội) → hiện đúng câu "Mã số thuế này đã có trong hệ thống. Vui lòng dùng chức năng Quên mật khẩu…" kèm nút "Quên mật khẩu", đồng thời báo đỏ ngay dưới ô Mã số thuế. Khác hẳn câu báo sai bản chất của vòng trước.

⇒ **4/4 ý đã hết lỗi** ⇒ verdict `Pass` (cột `Verify 2`).

## Bằng chứng đo được

- Lượt 1: mã số thuế `0455667788`, Hà Nội → thành công, cấp mã doanh nghiệp `DN-HNI-0007`.
- Lượt 2: mã số thuế `0455667799`, Hà Nội → thành công, cấp mã `DN-HNI-0008`.
- Số thứ tự cấp ra là **số lớn nhất + 1** (0006 → 0007 → 0008), **không** đâm vào mã đã tồn tại dù dãy vẫn thủng số 0004 ⇒ đúng chỗ vòng trước bị lỗi.
- Lượt 3 (mã số thuế trùng thật `0455667788`): bị từ chối bằng đúng câu dành cho trùng mã số thuế + nút "Quên mật khẩu".

## Đã cố BÁC BỎ kết luận Pass

1. Nghi "hết lỗi vì dữ liệu đã được dọn" → kiểm dãy mã Hà Nội trước khi test, **vẫn còn thủng số 0004** ⇒ điều kiện sinh lỗi cũ vẫn nguyên.
2. Nghi "may mắn 1 lần" → chạy **2 lượt** liên tiếp cùng tỉnh Hà Nội, cả 2 đều thành công.
3. Nghi "chặn đúng nhưng câu báo vẫn sai" → thử riêng nhánh mã số thuế trùng thật, câu báo và nút đi kèm đều đúng loại lỗi.
4. Nghi "đăng ký được nhưng không thật sự dùng được" → chạy tiếp tới bước kích hoạt bằng thư và đăng nhập thành công bằng mã số thuế.

## Phát hiện thêm NGOÀI 4 ý của phiếu (không ảnh hưởng verdict trên)

Tài khoản doanh nghiệp **chưa bấm liên kết kích hoạt trong thư** vẫn đăng nhập vào được hệ thống:
đăng nhập bằng mã số thuế + mật khẩu tự đặt lúc đăng ký → hiện hộp thoại "Đặt mật khẩu mới" ghi
"bạn cần đổi mật khẩu **tạm đã gửi tới** …" (thực tế không có mật khẩu tạm nào được gửi) → đặt mật khẩu mới
→ vào thẳng hệ thống, không hỏi mã xác thực, và tài khoản tự chuyển từ Chờ kích hoạt sang Đang hoạt động.
Đã dựng riêng 1 tài khoản để chứng minh: sau khi đăng ký, đọc trạng thái ra đúng `CHO_KICH_HOAT`; chưa đụng
vào thư, đăng nhập xong đọc lại thành `HOAT_DONG`. Lặp lại 2/2 lần. → cần log thành phiếu riêng.
