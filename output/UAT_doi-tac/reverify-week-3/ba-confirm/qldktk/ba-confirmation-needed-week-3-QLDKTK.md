# BA confirmation needed — UAT tuần 3 — Lô QLDKTK (Đăng ký tài khoản doanh nghiệp)

Bản SRS chỉ định chấm UAT tuần 3: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5`. Tab đối tác: `UAT_TGPL Doanh Nghiệp-tuần 3`. Màn liên quan: **SCR-VIII-08 — Đăng ký Tài khoản Doanh nghiệp** (FR-VIII-22 / UC120), form công khai `/register/doanh-nghiep`. Verify trực tiếp trên môi trường được giao ngày 2026-07-21.

> Phạm vi file này: các điểm màn hình **lệch so với SRS v3.5 nhưng SRS không quy định rõ đúng/sai** → cần BA chốt (bổ sung/sửa SRS, hay yêu cầu Dev đổi form). Các lỗi đã chắc chắn sai SRS (Open) nằm ở `../../bug-reports/qldktk/Pass-bug-report-QLDKTK.md`.

---

## 1. QLDKTK_03 (ý b) — Mục "Thông tin tài khoản" của form Đăng ký DN có thêm 2 trường "Họ và tên người đăng ký" + "Số điện thoại" mà SRS v3.5 không liệt kê

**Bối cảnh testcase**

- Dòng Excel: 186, mã TC `QLDKTK_03`. Nội dung kiểm tra: các trường mục "Thông tin tài khoản" trên màn "Đăng ký tài khoản doanh nghiệp".
- Đối tác báo 2 ý: (a) thiếu trường "Tên đăng nhập"; (b) màn có trường "Họ và tên người đăng ký", "Số điện thoại" nhưng SRS không yêu cầu 2 trường này.
- Ý (a) — QA xác định là **bug** (thiếu trường SRS yêu cầu) → đã log `BUG-QLDKTK_03`, verdict `Open` (không thuộc file này).
- Ý (b) — nội dung cần BA quyết dưới đây. Vì vậy verdict sheet của QLDKTK_03 là **`Open, BA confirm`**.

**Điểm cần BA xác nhận (ý b)**

- SRS v3.5 `SCR-VIII-08` Nhóm 2 "Tài khoản đăng nhập" (dòng 1857-1861) chỉ liệt kê 4 mục: **Tên đăng nhập** (chỉ đọc = Mã số thuế) · **Mật khẩu** · **Xác nhận mật khẩu** · **Cam kết thông tin đúng sự thật**.
- Thực tế form hiện có thêm 2 trường ở mục Tài khoản: **"Họ và tên người đăng ký"** (bắt buộc) + **"Số điện thoại"** (bắt buộc) — SRS v3.5 **không** liệt kê 2 trường này (SRS chỉ có `nguoi_dai_dien`/Người đại diện và `so_dien_thoai`/Điện thoại DN nằm ở Nhóm 1 – Thông tin doanh nghiệp, không phải Nhóm 2 – Tài khoản).
- API đăng ký thực tế có nhận `hoTen` + `soDienThoaiTaiKhoan` (thông tin người đăng ký, tách khỏi người đại diện + điện thoại DN).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1857` → `:1861` (SCR-VIII-08 Nhóm 2 — chỉ 4 mục, không có Họ tên người đăng ký / Số điện thoại)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1048` (`nguoi_dai_dien` — thuộc Nhóm 1) · `:1051` (`so_dien_thoai` — thuộc Nhóm 1)

**Câu hỏi BA**

- Form có được phép bổ sung 2 trường "Họ và tên người đăng ký" + "Số điện thoại" (thông tin cá nhân người đăng ký, tách khỏi người đại diện DN) ở mục Tài khoản không? Nếu **có** → cập nhật SRS bổ sung 2 trường; nếu **không** → yêu cầu Dev bỏ khỏi form.
- Verdict QA đề xuất cho ý (b): `Cần BA xác nhận` (không tự Reject vì SRS không quy định cấm; cũng không tự Open vì SRS silent). Owner sau khi BA chốt: `Dev FE` (thêm/bớt trường) hoặc `BA` (cập nhật SRS).

---

## 2. Phát hiện thêm trên cùng màn Đăng ký DN (ngoài 5 case được giao) — đề nghị BA cân nhắc

> Các điểm dưới đây **không phải verdict trên sheet** (không nằm trong 5 case QLDKTK_02/03/04/08/09 được giao). QA nêu để BA có bức tranh đầy đủ mức độ lệch của form so với SRS SCR-VIII-08 và quyết định có chuẩn hóa hay không.

**2.1. Thứ tự 2 mục bị đảo so với SRS**

- Hiện tại form xếp **"Thông tin tài khoản" TRƯỚC "Thông tin doanh nghiệp"**.
- SRS `SCR-VIII-08` xếp **Nhóm 1 = Thông tin doanh nghiệp** trước, **Nhóm 2 = Tài khoản đăng nhập** sau (dòng 1838 vs 1857).
- Đối tác (cột TKM phản hồi của QLDKTK_02) cũng đã góp ý đổi thứ tự "Thông tin doanh nghiệp trước, Thông tin tài khoản sau".
- **Câu hỏi BA:** giữ thứ tự theo SRS (DN trước, TK sau) hay chấp nhận bố cục hiện tại?

**2.2. Một số trường thừa không có trong SRS SCR-VIII-08**

- Form có thêm các trường/điều khiển: **"Tên viết tắt"**, **"Ngày cấp ĐKKD"**, **"Fax"**, **"Cho phép công khai thông tin"** (toggle) — SRS SCR-VIII-08 không liệt kê.
- (Lưu ý: các trường "Số lao động nữ", "Số lao động khuyết tật", "Nữ làm chủ" tuy không nằm trong bảng 18 trường của FR-VIII-22 nhưng thuộc entity DOANH_NGHIEP/FR-V.III-01 mà FR-VIII-22 tham chiếu "giống Inputs FR-V.III-01" → xem như hợp lệ, không nêu.)
- **Câu hỏi BA:** các trường thừa này có được giữ (và bổ sung vào SRS) hay bỏ để form khớp SCR-VIII-08? Riêng "Cho phép công khai thông tin" là toggle mới cần BA xác nhận nghiệp vụ (công khai thông tin gì, cho ai).

**Citation**

- `srs-fr-10-quan-tri.md:1838` (Nhóm 1 – Thông tin doanh nghiệp, xếp trước) · `:1857` (Nhóm 2 – Tài khoản, xếp sau)
- `srs-fr-10-quan-tri.md:1839`–`:1864` (danh sách đầy đủ 24 thành phần SCR-VIII-08 — không có Tên viết tắt / Ngày cấp ĐKKD / Fax / Cho phép công khai thông tin)

---

*File tạo: 2026-07-21 | QA Automation via Claude Code | Tách riêng theo yêu cầu gửi BA.*
