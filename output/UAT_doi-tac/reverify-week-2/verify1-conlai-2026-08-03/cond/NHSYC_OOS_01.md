# Bảng đối chiếu điều kiện — NHSYC_OOS_01 (row 131, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Nhập hồ sơ yêu cầu HTPL thủ công — FR-V.I-04 (UC54), màn SCR-V.I-02
**Nội dung TC:** một lần bấm nút lưu rơi vào nhánh lỗi sinh HAI khung thông báo hiện cùng lúc với hai câu chữ khác nhau (1 lần gửi dữ liệu → 2 khung).
**Loại bug:** hiển thị thông báo phụ thuộc **thao tác + dữ liệu tiền đề** (chỉ quan sát được khi thao tác lưu rơi vào nhánh lỗi) → KHÔNG phải bug tĩnh, BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG).
**Ngày verify lại:** 2026-08-04 · **Tài khoản QA dùng:** `cbnv_tw_01` (CB_NV_TW, đơn vị BTP · TW, `donViId = 00000000-0000-4000-8000-000000000001`)

> **Nguồn gốc dòng TC:** lỗi do QA tự phát hiện khi verify NHSYC_01 (row 127), nằm ngoài tiêu chí của phiếu nên mở dòng mới. **Không có evidence đối tác cho riêng lỗi này** — cột giữa dưới đây ghi điều kiện của **BUG GỐC do QA dựng ngày 03/08/2026**, không suy diễn điều kiện đối tác.

| Điều kiện có thể đổi kết quả | Bug gốc (QA dựng 03/08/2026) | Mình test lại (04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `cbnv_tw_03` — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #03"), đơn vị `BTP · TW` | `cbnv_tw_01` — vai trò `CB_NV_TW` ("CB Nghiệp vụ - Trung ương #01"), đơn vị `BTP · TW`, `donViId = 00000000-0000-4000-8000-000000000001` **trùng đúng** đơn vị của tài khoản bug gốc (đọc từ phiên đăng nhập thực) | Không |
| Màn hình + trạng thái entity | Màn "Thêm mới Hồ sơ Vụ việc" (`/vu-viec/tao-moi`), VU_VIEC **chưa tồn tại** (chưa sinh mã, chưa có trạng thái); sau khi bấm nút màn hình vẫn đứng nguyên tại đây | **Đúng cùng màn** "Thêm mới Hồ sơ Vụ việc" (`/vu-viec/tao-moi`), VU_VIEC chưa tồn tại; ở lượt đo nhánh lỗi, sau khi bấm nút màn hình cũng đứng nguyên tại đây, không sinh mã | Không |
| Dữ liệu tiền đề (hồ sơ + tệp đính kèm) | Hồ sơ điền đủ trường bắt buộc, DN `Cong ty TNHH QA UAT Kiem Thu` (MST 0109998887, mã DN-HNI-0001); **có 1 tệp PDF đính kèm** 614 B đã upload xong — điều kiện đưa thao tác lưu vào nhánh lỗi | Hồ sơ điền đủ trường bắt buộc, **cùng DN** `Cong ty TNHH QA UAT Kiem Thu` (MST 0109998887, mã DN-HNI-0001); **cũng có 1 tệp PDF đính kèm** (`NHSYC_OOS_01-tep-dinh-kem-retest0804.pdf`, 605 B, tải lên xong — máy chủ nhận tệp trả mã thành công 201) | Không |
| Thao tác / nút bấm + nhánh lỗi được đo | Bấm **[Lưu & Tiếp nhận]** đúng 1 lần; nhánh lỗi kích hoạt bằng **tệp đính kèm** (máy chủ trả lỗi hệ thống — `BUG-NHSYC_01`) | Bấm **[Lưu & Tiếp nhận]** đúng 1 lần, đếm được đúng 1 lần gửi dữ liệu. Nhánh lỗi cũ (tệp đính kèm) **đã hết** — cùng dữ liệu nay tạo được hồ sơ `VV-BTP-TW-20260804-001`. Nên đo trên **nhánh lỗi khác của CHÍNH màn đó**: giữ nguyên ngày tiếp nhận mặc định của biểu mẫu (04/08/2026) → máy chủ từ chối "Ngày tiếp nhận không được ở tương lai" | Không |

## Ghi chú đóng GAP

- **Không có ô GAP nào vì không có điều kiện đối tác để lệch:** dòng TC này do QA mở, toàn bộ điều kiện là do QA tự dựng và đã ghi lại đầy đủ ở cột "Mình test lại". Cột giữa là điều kiện của bug gốc do chính QA dựng ngày 03/08/2026.
- **🔴 Đổi nhánh lỗi — khai báo minh bạch, KHÔNG giấu:** tiêu chí của dòng TC này là "một sự kiện lỗi → bao nhiêu khung thông báo", chứ không phải "lỗi nào". Nhánh lỗi của bug gốc (hồ sơ **có tệp đính kèm** → máy chủ báo lỗi hệ thống) nay **không kích hoạt được nữa**: chạy lại đúng luồng, đúng vai trò, đúng doanh nghiệp, đúng kiểu tệp thì hồ sơ **tạo được** (mã `VV-BTP-TW-20260804-001`, trạng thái "Đã tiếp nhận", tệp đính kèm lưu cùng hồ sơ). *Không có lỗi* ≠ *đã sửa lỗi lặp thông báo*, nên bắt buộc phải tìm nhánh lỗi khác trên cùng màn hình để đo — đã chọn nhánh máy chủ từ chối ngày tiếp nhận. Mọi điều kiện khác (vai trò, đơn vị, màn hình, doanh nghiệp, có tệp đính kèm) giữ y nguyên như bug gốc.
- **Đã loại trừ lỗi phép đo:** trước **mỗi** lượt bấm đều tự kiểm chỉ có **1** bộ đo đang chạy (chèn node giả, đếm phải = 1); bộ đo **không lọc trùng** và đọc bằng `innerText` (chỉ chữ người dùng nhìn thấy); mỗi khung thông báo đo được **diện tích chiếm chỗ thật** 1432×40 px nên không phải node ẩn.
- **Đếm số lệnh gửi lên máy chủ cho mỗi lượt bấm = 1** ⇒ không phải người dùng bấm hai lần.
- **Lặp lại nhiều lần:** 4 lượt bấm rời rạc (mỗi lượt 1 lệnh gửi → 1 khung thông báo) + 1 loạt 8 lượt bấm cách nhau 3,5 giây (8 lệnh gửi → **đúng 8** khung thông báo, khoảng cách nhỏ nhất giữa 2 khung là 3.475 ms = đúng nhịp bấm) ⇒ không có cặp khung nào sinh ra từ cùng một lượt bấm.
- **Đã tải lại trang bỏ bộ nhớ đệm** trước khi bắt đầu lượt kiểm tra này; gói giao diện đang chạy `index-BrKDNUvo.js` (bản `HTPLDN · V1.0.5`).

**Kết luận: 0 GAP** — mọi điều kiện của bug gốc đã tái lập bằng test thật; riêng nhánh kích hoạt lỗi phải đổi vì nhánh cũ đã hết lỗi, và việc đổi đã khai báo rõ ở trên.
