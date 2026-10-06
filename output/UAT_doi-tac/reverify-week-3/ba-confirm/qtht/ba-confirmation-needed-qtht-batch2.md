# BA confirmation needed — QTHT Batch 2 (Form Thêm/Sửa danh mục nhóm B) — 2026-07-21

> Gom các testcase QTHT Batch 2 (rows 142–158) cần BA phản hồi lại đối tác. Tool verify: Chrome DevTools MCP, tài khoản `admin` (vai trò QTHT), env `https://18.143.165.120.nip.io`. SRS: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md`.
>
> **Kết luận nhanh:** cả 8 case đều verdict `BA confirm`. Cụm gốc chung = trường **"Danh mục cha"** thừa trong form của mọi tab danh mục phẳng (nghi 1 bug FE component dùng chung). Riêng HSDNTT có thêm ràng buộc **"Thành phần hồ sơ bắt buộc ≥1"** trái SRS. Ý "Tiêu chí doanh thu bắt buộc" (LDN) đã KHÔNG còn tái hiện.

---

## Cụm 1 — Trường "Danh mục cha" thừa trong form Thêm/Sửa (8 case: 142·144·146·148·149·151·157·158)

**Bối cảnh testcase**

- Đối tác phản ánh: form Thêm/Sửa các tab danh mục phẳng (Loại doanh nghiệp, Hồ sơ đề nghị hỗ trợ, Hồ sơ đề nghị thanh toán, Tiêu chí đánh giá hiệu quả) hiển thị thừa trường **"Danh mục cha"**.
- Vai trò kiểm tra: QTHT (đúng vai trò — TPL-DM-CRUD precondition dòng 72: "User có vai trò QTHT").

**Đối chiếu SRS v3.5**

- SHARED TEMPLATE **TPL-DM-CRUD** §Inputs chung (dòng 77–83) chỉ có 5 trường: `ma, ten, mo_ta, thu_tu, trang_thai` — **KHÔNG có trường "Danh mục cha"** (`danh_muc_cha_id`).
- Màn **SCR-VIII-01** §Thành phần màn hình (dòng 1578–1583): modal CRUD gồm Mã / Tên / Mô tả / Thứ tự / Trạng thái / Hủy-Lưu — **không liệt kê "Danh mục cha"**.
- Trường "Đơn vị cha" (danh mục cha) CHỈ tồn tại hợp lệ ở **DM Cơ quan Đơn vị (UC103, Tree View, dòng 1585–1590)** — không áp cho các tab phẳng đang xét.
- Các FR riêng của 4 tab đều dùng TPL-DM-CRUD + trường riêng, KHÔNG khai báo "Danh mục cha": FR-VIII-07/LDN (dòng 389), FR-VIII-08/HSDNHT (dòng 410), FR-VIII-09/HSDNTT (dòng 429), FR-VIII-11/TCDGHQ (dòng 531).

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:77-83` (Inputs chung TPL-DM-CRUD)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1578-1583` (SCR-VIII-01 modal)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1585-1590` (Tree View DM Cơ quan ĐV — trường hợp DUY NHẤT có cha)

**Kết quả verify UI hiện tại (21/07/2026, Chrome DevTools MCP, tài khoản `admin`/QTHT)**

- Cả 4 tab, cả form Thêm mới lẫn Sửa: trường **"Danh mục cha"** đều hiển thị, placeholder "Chọn danh mục cha (tùy chọn)".
- Trường ở dạng **tùy chọn** (không có dấu `*`, `reqClass=false`, CSS `::before` = none). Lưu bản ghi KHÔNG chọn cha vẫn thành công (đã test POST tạo record Loại DN không cha → toast "Thêm mới thành công").
- Evidence: `../../reverify-audit/QLDMLDN_06/web-them-moi-form.png`, `QLDMLDN_13/web-sua-form.png`, `QLDMHSDNHT_06/web-them-moi-form.png`, `QLDMHSDNHT_13/web-sua-form.png`, `QLDMHSDNTT_06/web-luu-thanh-phan-trong.png`, `QLDMHSDNTT_13/web-sua-form.png`, `QLDMTCDGHQ_06/web-them-moi-form.png`, `QLDMTCDGHQ_12/web-sua-form.png`.

**Kết luận QA**

- Trường "Danh mục cha" là **thiết kế thêm ngoài đặc tả** cho các danh mục phẳng: SRS Inputs (dòng 77–83) và SCR-VIII-01 (dòng 1578–1583) không liệt kê.
- Trường ở dạng tùy chọn, KHÔNG chặn luồng lưu hợp lệ → không phải lỗi phá validation, nên để **BA chốt đặc tả** thay vì đẩy dev sửa ngay.

**Nội dung đề xuất BA phản hồi đối tác**

- Xác nhận 1 trong 2 hướng cho các danh mục **phẳng** (LDN, HSDNHT, HSDNTT, TCDGHQ — và các tab phẳng khác cùng component: LVPL, LHHT, CTHT, TTVV...):
  1. **Bổ sung "Danh mục cha" vào đặc tả** (nếu nghiệp vụ muốn hỗ trợ phân cấp cho các danh mục này) — cập nhật TPL-DM-CRUD Inputs;
  2. **Ẩn/bỏ trường "Danh mục cha"** khỏi form các tab phẳng, chỉ giữ cho DM Cơ quan Đơn vị (UC103) — để khớp SRS hiện hành.
- Verdict QA đề xuất: `BA confirm` (bổ sung/điều chỉnh đặc tả — chưa gửi Dev tới khi BA chốt hướng).

---

## Cụm 2 — HSDNTT buộc nhập ≥1 "Thành phần hồ sơ" (149 QLDMHSDNTT_06, 151 QLDMHSDNTT_13)

**Bối cảnh testcase**

- Đối tác phản ánh: form Thêm/Sửa "Hồ sơ đề nghị thanh toán" đánh **"Thành phần hồ sơ" bắt buộc ≥1** (SRS: không bắt buộc).

**Đối chiếu SRS v3.5**

- FR-VIII-09 (UC107) §Inputs — trường riêng: `thanh_phan_ho_so` kiểu `structured`, cột **Bắt buộc = N** (không bắt buộc).
- Nghĩa là: một danh mục "Hồ sơ đề nghị thanh toán" được phép tạo mà KHÔNG cần khai thành phần nào.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:442` (`thanh_phan_ho_so | structured | N`)

**Kết quả verify UI hiện tại (21/07/2026, MCP, `admin`/QTHT)**

- Form luôn dựng sẵn khối "Thành phần hồ sơ" → "Thành phần 1" với `* Mã thành phần` + `* Tên thành phần` (bắt buộc) và **nút xóa của Thành phần 1 bị vô hiệu** → không bỏ được component đầu.
- Test thật: điền Mã + Tên danh mục, để trống thành phần, bấm **Đồng ý** → **0 request gửi máy chủ, không có toast, form bị chặn**, hiện lỗi inline "Mã thành phần là bắt buộc" + "Tên thành phần là bắt buộc".
- Evidence: `../../reverify-audit/QLDMHSDNTT_06/web-loi-thanh-phan-bat-buoc.png` (ảnh lỗi inline), `web-luu-thanh-phan-trong.png`.

**Kết luận QA**

- App **ép ≥1 thành phần hồ sơ** (chặn lưu danh mục không có thành phần), TRÁI với SRS FR-VIII-09 dòng 442 (`thanh_phan_ho_so` = N/không bắt buộc). Đây là bất đồng về **đặc tả/ràng buộc nghiệp vụ**.

**Nội dung đề xuất BA phản hồi đối tác**

- BA chốt source truth cho ràng buộc "thành phần hồ sơ thanh toán":
  1. **Giữ ràng buộc ≥1 thành phần** (nếu nghiệp vụ yêu cầu mọi loại hồ sơ TT phải có tối thiểu 1 thành phần) → cập nhật SRS FR-VIII-09 thành Y + ghi rõ min 1; đối tác/QA cập nhật expected.
  2. **Bỏ ràng buộc, cho phép 0 thành phần** để khớp SRS hiện hành (N) → gửi Dev FE nới validation (cho xóa hết thành phần, không ép Thành phần 1).
- Verdict QA đề xuất: `BA confirm` (SRS ghi N nhưng app enforce ≥1 — cần BA quyết giữ hay bỏ; theo chỉ đạo ghi cột trạng thái = BA confirm vì case vừa là lỗi-vs-SRS vừa cần BA chốt spec).

---

## Ghi chú — ý "Tiêu chí doanh thu bắt buộc" (LDN 142/144) đã KHÔNG tái hiện

- Đối tác (vòng đầu, env `htpldn-uat.ospgroup.vn`) chụp form Loại doanh nghiệp có `* Tiêu chí doanh thu` (dấu * đỏ → bắt buộc).
- Verify lại 21/07 trên env được giao: trường **"Tiêu chí doanh thu" KHÔNG còn bắt buộc** — không có dấu `*` (`::before`=none), placeholder ghi "(tùy chọn)", đã tạo (POST) và cập nhật (PATCH) record thành công khi để trống trường này. Khớp SRS FR-VIII-07 dòng 402 (`tieu_chi_doanh_thu` = N).
- → Ý này KHÔNG phải lỗi ở build hiện tại (không đưa vào câu hỏi BA). Verdict tổng của LDN vẫn `BA confirm` do còn cụm "Danh mục cha".
