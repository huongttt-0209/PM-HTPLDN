# Bảng đối chiếu điều kiện — QLTKND_17 (row 169)

**Case:** Thêm tài khoản với **email trùng** → đối tác báo thông báo lỗi bị lặp (2 toast "Email đã tồn tại trong hệ thống").
**Verdict:** `Reject` — trên env được giao chỉ hiện **1 toast** (đo bằng tools/toast-capture.js, 2 lần sạch, self-check=1); hành vi 2 toast không tái hiện.

> Env được giao (`18.143.165.120.nip.io`) luôn khác env đối tác log (QA_VERIFY_PROTOCOL §Nguyên tắc — dòng 80). Chi tiết so sánh build/env đẩy vào `reverify-audit/QLTKND_17/toast-capture-measurement.md` (nội bộ). Bảng dưới chỉ đối chiếu **điều kiện tái hiện** (role/state/input).

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLTKND_17.jpg, full-res) | Mình test (18.143.165.120.nip.io, 21/07) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | QTHT ("Quản trị viên QTHT") | admin / QTHT | Không |
| Entity + trạng thái | Form "Thêm tài khoản mới", có email đã tồn tại để nhập trùng | Form "Thêm tài khoản mới", email `nht_qa_01@htpldn.test` đã tồn tại | Không |
| Input / giá trị nhập | Email trùng (`aibox@gmail.com`), tên đăng nhập mới | Email trùng (`nht_qa_01@htpldn.test`), tên đăng nhập mới (unique) | Không |

**0 GAP.** Cùng thao tác (thêm TK email trùng), cùng vai trò QTHT, cùng điều kiện (email đã tồn tại). Khác email cụ thể không đổi bản chất — cả 2 đều là email đã tồn tại → cùng nhánh validation trùng email.

## Kết quả test (real-data, artifact — mandated tool)
- Đo bằng `tools/toast-capture.js` (observer=1 self-check hợp lệ mỗi lần, KHÔNG lọc trùng, đọc innerText, đếm request song song toast).
- **Lần #1 & #2 (sạch):** `1 request POST /api/v1/tai-khoan` → **1 toast** "Email đã tồn tại trong hệ thống". Không lặp.
- **Lần #3:** observer bắt 0 toast (trang điều hướng đi + AntD reuse node); network xác nhận POST trả **409 Conflict** (email trùng). Không kết luận từ run này.
- **Không lần nào bắt được 2 toast** trên env được giao. Session prompt map: `1 request + 1 toast = Reject`.
- Log đầy đủ: `reverify-audit/QLTKND_17/toast-capture-measurement.md`.

## Đối chiếu SRS
- FR-VIII-15 §Error Handling E2 (`ERR-TK-02`, `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:728`): email trùng → **1** thông báo lỗi. Env được giao (1 toast) = ĐÚNG đặc tả.

## Kết luận
`Reject` — Trên env được giao, thêm tài khoản email trùng chỉ hiện **1 thông báo lỗi** (đúng đặc tả); hành vi lặp 2 toast đối tác báo KHÔNG tái hiện. → Đối tác kiểm tra lại. Cross-ref: case chị em **QLTKND_15** (trùng **tên đăng nhập**) VẪN sinh 2 toast trên env được giao → đã log Open riêng; hai nhánh (email vs username) hiện hành xử KHÁC nhau.
