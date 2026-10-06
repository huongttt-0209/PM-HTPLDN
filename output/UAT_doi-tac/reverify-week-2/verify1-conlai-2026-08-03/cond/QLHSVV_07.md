# Bảng đối chiếu điều kiện — QLHSVV_07 (row 128, tab `UAT_TGPL Doanh Nghiệp-tuần 2`)

**Chức năng:** Tải tệp đính kèm của hồ sơ vụ việc HTPL — FR-V.I-07 (UC57), màn SCR-V.I-03 (Accordion 3 — Tài liệu Đính kèm)
**Loại bug:** phụ thuộc dữ liệu tiền đề (hồ sơ phải CÓ tệp đính kèm) + vai trò + trạng thái → BẮT BUỘC có bảng này (QA_VERIFY_PROTOCOL §Quy tắc VÀNG)
**Ngày verify:** 2026-08-03 · **Tài khoản QA dùng:** `cbnv_tw_03` (CB_NV_TW, đơn vị BTP · TW)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res `frames/QLHSVV_07/`) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — nhãn góc phải khung hình ghi "Cán bộ NV Trung ương · CB_NV_TW", đơn vị "BTP · TW" (`t000.00s.jpg`) | `cbnv_tw_03` — nhãn góc phải "CB Nghiệp vụ - Trung ương #03 · CB_NV_TW", đơn vị "BTP · TW"; `donViId = 00000000-0000-4000-8000-000000000001` **trùng đúng** mã đơn vị nằm trong đường dẫn tệp của đối tác (`t003.38s.jpg`) | Không |
| Entity + **trạng thái** (state machine) | Vụ việc đứng ở màn **Chi tiết** (`/vu-viec/ab08db14-…`), dòng thời gian có "Tiếp nhận 29/07/2026 17:29" + "Bổ sung hồ sơ 29/07/2026 17:31" → hồ sơ đã tiếp nhận và đã bổ sung tài liệu | `VV-BTP-TW-20260803-002` ở màn **Chi tiết** (`/vu-viec/4f340b58-…`), badge trạng thái "Đã tiếp nhận", dòng thời gian có "Bổ sung hồ sơ 03/08/2026 16:13" → cùng trạng thái, cùng loại sự kiện | Không |
| Dữ liệu tiền đề (tệp đính kèm) | Hồ sơ có **1 tệp**: `QLHSVV_04.jpg` — Loại `BO_SUNG`, Định dạng **JPG**, 193.5 KB, Trạng thái quét **Sạch** | **QA tự tạo tiền đề** (đường 2 — đính kèm vào hồ sơ đã tồn tại): `QLHSVV_07_qa.jpg` — Loại `BO_SUNG`, Định dạng **JPG**, 38.8 KB, Trạng thái quét **Sạch**. Cùng định dạng tệp, cùng loại tài liệu, cùng kết quả quét | Không |
| Input / phần tử bấm | Bấm **biểu tượng mũi tên tải xuống** (⤓ xanh) ở cột cuối hàng tệp trong nhóm "Tài liệu đính kèm" — trên bản của đối tác đây là **phần tử hành động DUY NHẤT** của hàng, di chuột hiện đường dẫn tệp ở thanh trạng thái (`t001.42s.jpg`) | Bấm **nút [Tải]** (biểu tượng mũi tên tải xuống + chữ "Tải") ở cột "Thao tác" cùng hàng tệp. Bản hiện tại có **2 nút riêng** [Xem] và [Tải] — đã bấm **cả hai** để phân biệt chức năng | Không |

## Ghi chú đóng GAP

- **Tiền đề "hồ sơ có tệp đính kèm" đã TỰ TẠO, không phải blocker** (§Nguyên tắc 4). Đã thử theo thứ tự:
  1. Rà **toàn bộ 37 vụ việc** trong danh sách bằng dữ liệu trả về của màn hình (`/vu-viecs` + `/vu-viecs/{id}/ho-so`) → **0 hồ sơ có tệp** ⇒ không có sẵn để dùng.
  2. **Đính kèm tệp vào hồ sơ đã tồn tại** qua màn Chi tiết → nhóm "Tài liệu đính kèm" → [+ Thêm tài liệu] → **THÀNH CÔNG** (ảnh `BUG-QLHSVV_07-seed-01-modal-them-tai-lieu.png`, `…-seed-02-bang-tai-lieu-sau-upload.png`). Dừng ở đường này, không cần đến đường 3.
  - Đường "tạo hồ sơ mới KÈM tệp" **không dùng** vì đang hỏng (đã chứng minh ở case NHSYC_01 cùng đợt — máy chủ trả lỗi hệ thống khi tạo mới có tệp).
- **Chênh lệch bản dựng KHÔNG phải GAP mà chính là thứ cần kiểm:** đối tác quay trên bản `HTPLDN · V1.0.2` (môi trường `htpldn-uat.ospgroup.vn`), QA verify trên bản `HTPLDN · V1.0.5` (`18.143.165.120.nip.io`) — đây là verify vòng 1 **sau khi dev báo đã sửa**, nên phải đo trên bản mới.
- **Đã tải lại trang bỏ cache** (`navigate_page reload ignoreCache`) trước lần đo quyết định, để loại trừ mã cũ còn sống trong tab (bài học "Reopen oan 01/08").
- **Đo lại bằng phương pháp thứ hai:** lặp thao tác **3 lần** (1 lần trước khi tải lại trang, 2 lần sau khi tải lại trang), mỗi lần **xóa sạch tệp trong thư mục Tải xuống trước khi bấm**; cả 3 lần tệp đều về máy với **mã băm MD5 y hệt tệp gốc** (`091531a081d38cc9ddda5614f25bd154`, đúng bằng `etag` máy chủ trả về). Không có mâu thuẫn giữa 2 phép đo.

**Kết luận: 0 GAP** — mọi điều kiện của đối tác đã được tái lập bằng test thật trên tiền đề do QA tự dựng.
