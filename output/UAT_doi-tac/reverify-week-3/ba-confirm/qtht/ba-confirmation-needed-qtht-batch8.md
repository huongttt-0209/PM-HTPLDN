# BA confirmation needed — QTHT Batch 8 (Quản lý tài khoản người dùng — SCR-VIII-03) — 2026-07-21

> Gom các testcase Batch 8 QA verdict **BA confirm** (đối chiếu SRS xong nhưng cần BA phản hồi lại đối tác). Đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. Bug có SRS reference rõ (Open) → `bug-report-qtht-batch8.md`; case không tái hiện (Reject) → `../../reverify-audit/`.

> Citation trỏ `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:LINE` (SRS v3.5, đã mở file verify số dòng thực).

---

## QLTKND_06 — Empty-state khi tìm kiếm không ra: "Trống" vs thông báo ngữ cảnh

**Bối cảnh testcase**

- Dòng Excel: 167, mã TC `QLTKND_06`.
- Nội dung kiểm tra: QTHT tìm kiếm chuỗi không tồn tại trên màn Quản lý tài khoản người dùng (SCR-VIII-03).
- Expected trong file UAT: hiển thị thông báo ngữ cảnh "Không tìm thấy tài khoản phù hợp".
- Actual đối tác ghi: hệ thống hiển thị "Trống" (component empty mặc định).

**Đối chiếu SRS v3.5**

- SCR-VIII-03 (bảng Thành phần màn hình + hành vi, dòng 1642–1673) KHÔNG quy định nội dung thông báo khi tìm kiếm không có kết quả trên màn này (im lặng về copy empty-state).
- Không có BR/AC nào chốt chuỗi thông báo empty-state cho danh sách tài khoản.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1635` (heading SCR-VIII-03 Quản lý Tài khoản NSD)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1647` (Ô tìm kiếm — có search, KHÔNG spec copy empty-state khi 0 kết quả)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT.
- Tìm chuỗi random không có kết quả → khung danh sách hiển thị "Trống" (component empty mặc định) — tái hiện đúng như đối tác phản ánh.
- Evidence: `../../reverify-audit/QLTKND_06/empty-trong.png`.

**Kết luận QA**

- `QLTKND_06` KHÔNG đủ căn cứ Open: SRS im lặng về nội dung thông báo empty-state màn Tài khoản → app hiển thị "Trống" không vi phạm clause SRS nào.
- Cùng bản chất với **QLDMCQDVQL_05** (B5) — nghi dùng chung 1 component empty-state gốc; cần thống nhất copy toàn hệ thống.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý copy empty-state:

- Có đổi "Trống" thành thông báo ngữ cảnh "Không tìm thấy tài khoản phù hợp" cho màn Tài khoản (và các màn dùng chung component) không?
- Verdict QA đề xuất: `Cần BA xác nhận` (SRS silent), chưa gửi Dev tới khi BA chốt chuẩn copy empty-state chung.

---

## QLTKND_25 — Sắp xếp theo cột: màn Tài khoản không có click-sort

**Bối cảnh testcase**

- Dòng Excel: 170, mã TC `QLTKND_25`.
- Nội dung kiểm tra: QTHT bấm tên cột trên danh sách tài khoản để sắp xếp.
- Expected trong file UAT: bấm tên cột → danh sách sắp xếp theo cột đó, luân phiên tăng/giảm.
- Actual đối tác ghi: KHÔNG sắp xếp được (mặc định "Lần đăng nhập cuối" giảm dần).

**Đối chiếu SRS v3.5**

- SCR-VIII-03 bảng Thành phần màn hình (cột 10–16): hành vi cột Username = "click → chi tiết"; các cột Họ tên / Email / Đơn vị / Vai trò / Trạng thái = "—" (không mô tả tương tác click-sort) → màn Tài khoản KHÔNG yêu cầu click-sort cột.
- Ngược lại, các màn sibling CÓ click-sort theo đặc tả: danh mục dùng chung cùng module (SCR-VIII-01, chỉ cột Tên — [STT69]); Vụ việc HTPL; Hỏi đáp pháp lý → hệ thống không đồng nhất.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1654` (cột Username "click → chi tiết"; cột Họ tên/Email/Đơn vị/Vai trò/Trạng thái dòng 1655–1659 hành vi = "—", không click-sort)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1572` (SCR-VIII-01 cột Tên có sort — [STT69])

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT, URL `/quan-tri/tai-khoan`.
- DOM: 10 header cột, KHÔNG cột nào có mũi tên sắp xếp / `aria-sort` / marker sort.
- Behavioral: bấm header "Tên đăng nhập" → thứ tự dòng giữ nguyên, không có request `?sortBy=` gửi lên máy chủ.
- Evidence: `../../reverify-audit/QLTKND_25/web-cot-khong-sort.png`, audit `../../reverify-audit/QLTKND_25/audit.md`.

**Kết luận QA**

- `QLTKND_25` KHÔNG đủ căn cứ Open: xét riêng SCR-VIII-03, SRS không mô tả click-sort → app đúng spec màn này.
- KHÔNG thể Reject: sibling screens có click-sort → không đồng nhất cấp cross-screen.
- Cùng bản chất với **QLHSDNHTCP_19** (row 23, đã BA confirm).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA quyết phạm vi yêu cầu click-sort:

- Click-sort theo cột là yêu cầu chung cho MỌI màn danh sách (khi đó màn Tài khoản thiếu → bổ sung, owner Dev FE)? Hay chỉ áp cho màn có "Hành vi = sắp xếp" trong SRS (khi đó màn Tài khoản đúng spec)?
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt phạm vi (đồng bộ QLHSDNHTCP_19).

---

## QLTKND_27 — Nút "Đặt lại mật khẩu" đã bị bỏ theo STT80

**Bối cảnh testcase**

- Dòng Excel: 171, mã TC `QLTKND_27`.
- Nội dung kiểm tra: QTHT tìm nút "Đặt lại mật khẩu" trên màn Quản lý tài khoản (cột Hành động).
- Expected trong file UAT: nút "Đặt lại mật khẩu" hiển thị khi TK Đang hoạt động / Tạm khóa.
- Actual đối tác ghi: màn hình KHÔNG hiển thị nút chức năng này.

**Đối chiếu SRS v3.5**

- SCR-VIII-03 cột Hành động (row 16): **[STT80 UAT 2026-06-02] Bỏ "Đổi MK"** — quản trị viên KHÔNG đặt/đổi mật khẩu người dùng; reset MK qua "Gửi lại email kích hoạt".
- FR-VIII-15 §Inputs [STT80]: admin không đặt mật khẩu khi tạo TK; user tự đặt qua link kích hoạt.
- FR-VIII-26: reset/đặt lại mật khẩu là luồng tự phục vụ "Quên mật khẩu" của user, không phải nút admin trên list.
- → App KHÔNG hiện nút = ĐÚNG SRS v3.5. Kỳ vọng đối tác theo spec CŨ (trước STT80).

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1660` (cột Hành động — [STT80] bỏ "Đổi MK")
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:695` (§Inputs — [STT80] bỏ field mật khẩu)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1260` (FR-VIII-26 — Quên mật khẩu / kích hoạt)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin`/QTHT, URL `/quan-tri/tai-khoan`.
- Kiểm cả 2 trạng thái đối tác nêu: **Hoạt động** (nút Sửa/Phân quyền/Khóa TK/Vô hiệu hóa) và **Tạm khóa** (cbpd_bn — nút Sửa/Phân quyền/Mở khóa) — cả 2 đều KHÔNG có "Đặt lại mật khẩu".
- `anyResetButtonAnywhere = false` (không nút reset ở bất kỳ trạng thái nào).
- Evidence: `../../reverify-audit/QLTKND_27/web-hanh-dong-active-no-reset.png`, audit `../../reverify-audit/QLTKND_27/audit.md`.

**Kết luận QA**

- `QLTKND_27` KHÔNG phải bug theo SRS v3.5: nút "Đặt lại mật khẩu" đã bị bỏ có chủ đích [STT80 UAT 2026-06-02].
- KHÔNG thể Reject: quan sát "không có nút" của đối tác tái hiện đúng, chỉ tranh chấp expected/spec.
- Điểm expected đối tác lệch spec: kỳ vọng nút hiện khi Active/Tạm khóa là theo đặc tả trước STT80.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận expected của `QLTKND_27` theo SRS v3.5:

- Nút "Đặt lại mật khẩu"/"Đổi MK" đã được BA bỏ 2026-06-02 (STT80). Reset MK nay qua "Gửi lại email kích hoạt" (TK chờ kích hoạt) + tự phục vụ "Quên mật khẩu" (FR-VIII-26).
- Đề nghị cập nhật expected testcase bỏ yêu cầu nút "Đặt lại mật khẩu" — trừ khi BA có yêu cầu khôi phục nút cho admin.
- Verdict QA đề xuất: `Không phải bug theo SRS v3.5` (chờ BA xác nhận với đối tác), không gửi Dev.
