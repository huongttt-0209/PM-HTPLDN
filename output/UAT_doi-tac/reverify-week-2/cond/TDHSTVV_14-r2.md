# Bảng đối chiếu điều kiện — TDHSTVV_14 (verify phản ánh vòng 2)

**Claim vòng 2 của đối tác:** "**Người hỗ trợ không nhận được thông báo kèm lý do**".

**Bối cảnh ca kiểm thử:** Cán bộ Nghiệp vụ cùng đơn vị gửi kết quả thẩm định với kết luận **"Không đạt"**.
Kết quả mong đợi ghi trong phiếu: hồ sơ sang **"Từ chối"**, ghi thời điểm + người từ chối, **gửi thông báo kèm lý do đến Người hỗ trợ**, lưu vết, hiện thông báo "Đã từ chối hồ sơ".

**Evidence:** `TDHSTVV_13_v2.webm` — video ~46 giây (trích khung bằng `tools/extract_frames.py`, thêm dải 1 s/khung đoạn 26–32 s).
Diễn biến đọc được:
- t≈0–24 s — vai trò **CB_NV_TW** (badge "BTP · TW", "Cán bộ NV Trung ương") ở màn chi tiết `/chuyen-gia-tvv/cb345570-…`, thẻ **Thẩm định**: điền nhận xét 4 nhóm, tích "Có tham gia mạng lưới tư vấn pháp luật".
- t≈24 s — chọn **KHÔNG ĐẠT**, ô **Lý do** nhập "tkm kiểm thử chức năng không đạt" (32/1000 ký tự); thanh nút: Hủy · Lưu nháp · **Gửi KQ** · Trình duyệt (mờ).
- t≈28 s — hộp thông báo xanh **"Đã lưu kết quả thẩm định"**.
- t≈32–36 s — trang tải lại, về thẻ Hồ sơ.
- t≈44 s — chuyển sang tài khoản **NHT BTP TW 02 Audit R30** (vai trò NHT, badge "BTP · TW"), mở màn **Thông báo**: danh sách chỉ có **1** mục duy nhất *"Kích hoạt tài khoản Người hỗ trợ pháp lý — PM-HTPLDN"* ngày 11/05/2026 — **không có** thông báo từ chối hồ sơ.

Đồng hồ máy 25/07/2026 17:16–17:17.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò người thẩm định | **CB_NV_TW** — badge "BTP · TW", "Cán bộ NV Trung ương" | `cbnv_tw` — vai trò CB_NV_TW, badge "BTP · TW" (trùng khít) | Không |
| Quan hệ đơn vị người thẩm định ↔ hồ sơ | Hồ sơ mã `TVV-BTP-TW-…`, cùng Cục Bổ trợ tư pháp – Bộ Tư pháp | Hồ sơ `TVV-BTP-TW-0021`, mã đơn vị `…8000-000000000001` — trùng đơn vị của `cbnv_tw` | Không |
| Người tạo hồ sơ (Người hỗ trợ) | Tài khoản NHT ở **cùng cấp Trung ương**, badge "BTP · TW" | Hồ sơ do chính tài khoản **NHT `nht_qa_tw`** (cấp Trung ương, cùng Cục Bổ trợ tư pháp) tạo ⇒ quan hệ "Người hỗ trợ ↔ hồ sơ" là **chắc chắn** (video của đối tác không chứng minh được quan hệ này, QA dựng lại để loại bỏ nghi ngờ) | Không |
| Màn hình + thẻ | Màn chi tiết tư vấn viên, thẻ **Thẩm định** | Cùng màn, cùng thẻ Thẩm định | Không |
| Trạng thái hồ sơ trước thao tác | Hồ sơ đang thẩm định (thẻ Thẩm định mở, có nút "Gửi KQ") | **Đang thẩm định** — đọc dữ liệu hồ sơ ngay trước khi bấm: `DANG_THAM_DINH`, phiên bản 2 | Không |
| Kết luận + lý do nhập vào | **KHÔNG ĐẠT** + ô Lý do có nội dung (32 ký tự) | **KHÔNG ĐẠT** + Lý do 61 ký tự ("… ho so khong dat, thieu chung chi hanh nghe") | Không |
| Nút được bấm | **"Gửi KQ"** | **"Gửi KQ"** — chọn phần tử theo đúng nhãn "Gửi KQ" rồi mới bấm | Không |
| Nơi kiểm tra thông báo | Màn **Thông báo** trong ứng dụng, đăng nhập tài khoản NHT | Màn **Thông báo** trong ứng dụng, đăng nhập `nht_qa_tw`; **kèm thêm** kiểm hộp thư của hệ thống để biết thông báo có đi đường email hay không | Không |
| Trình duyệt / kích thước cửa sổ | Chrome trên Windows, cửa sổ tối đa | Chrome 1440×900 — kết luận dựa trên dữ liệu hồ sơ + danh sách thông báo + hộp thư nên không phụ thuộc kích thước cửa sổ | Không |

**Kết luận:** 0 GAP — cùng vai trò, cùng đơn vị, cùng màn/thẻ, cùng trạng thái đầu vào, cùng kết luận + lý do, cùng nút bấm; và QA còn **siết chặt hơn** ở chỗ bảo đảm hồ sơ do chính tài khoản NHT đang kiểm tạo ra.

**Kết quả tái hiện: TÁI HIỆN 100% phần quan sát — nhưng hệ thống KHÔNG sai đặc tả ở điểm này.**
- Người hỗ trợ pháp lý **không** nhận được thông báo nào trong ứng dụng (danh sách vẫn đúng 1 mục kích hoạt tài khoản cũ) — **giống hệt** video đối tác.
- Nhưng thông báo **có được gửi kèm lý do**, đi bằng **email tới địa chỉ khai trên hồ sơ ứng viên**, đúng đối tượng mà đặc tả chỉ định là **chủ hồ sơ**.

Chi tiết phép đo + câu hỏi cho BA + 1 lỗi phụ phát hiện kèm: [`../reverify-audit/TDHSTVV_14/audit.md`](../reverify-audit/TDHSTVV_14/audit.md).
