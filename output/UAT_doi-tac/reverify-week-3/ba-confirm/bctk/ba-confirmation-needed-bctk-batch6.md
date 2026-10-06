# BA confirmation needed — BCTK Batch 6 (BUTTON: nút "Xóa bộ lọc" không hiển thị) — 2026-07-21

> **File này để làm gì:** gom 6 testcase batch 6 (module Báo cáo Thống kê, cụm "nút Xóa bộ lọc không hiển thị") mà QA đối chiếu SRS xong nhưng khác biệt nằm ở **đặc tả** (kỳ vọng đối tác ≠ SRS) → cần BA chốt. Không phải bug app sai clause SRS nên KHÔNG log vào bug-report.
>
> **Vai trò verify:** `cbnv_tw_03` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc). Môi trường `https://18.143.165.120.nip.io/bao-cao`. Kỳ = Năm 2026, Đơn vị = Toàn quốc.
>
> **SRS:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md` (= `input/srs-update-2026-5-5/srs-fr-11-bao-cao.md`, cùng nội dung dòng 1042).

---

## SLHDVM_09, VVDTN_09, VVDHT_09, VVDHTHT_09, VVTTG_08, CLDTBDDDR_09 — Đối tác kỳ vọng nút "Xóa bộ lọc", SRS spec "Nút Làm mới" (cùng 1 màn dùng chung SCR-IX-01)

**Bối cảnh testcase**

- 6 dòng Excel cùng bản chất — chỉ khác dropdown loại báo cáo:

  | Row | Mã TC | Loại báo cáo (FR-IX) | Evidence đối tác | Evidence QA (real-data) |
  |---|---|---|---|---|
  | 194 | `SLHDVM_09` | BC Số lượng hỏi đáp/vướng mắc PL (FR-IX-01) | `../../partner-evidence/SLHDVM_09.jpg` | `../../reverify-audit/SLHDVM_09/SLHDVM_09-before-lammoi.png` + `-after-lammoi.png` |
  | 199 | `VVDTN_09` | BC Vụ việc đã tiếp nhận (FR-IX-02) | `../../partner-evidence/VVDTN_09.jpg` | `../../reverify-audit/VVDTN_09/VVDTN_09-toolbar.png` |
  | 206 | `VVDHT_09` | BC Vụ việc đang hỗ trợ (FR-IX-03) | `../../partner-evidence/VVDHT_09.jpg` | `../../reverify-audit/VVDHT_09/VVDHT_09-toolbar.png` |
  | 212 | `VVDHTHT_09` | BC Vụ việc đã hoàn thành (FR-IX-04) | `../../partner-evidence/VVDHTHT_09.jpg` | `../../reverify-audit/VVDHTHT_09/VVDHTHT_09-toolbar.png` |
  | 219 | `VVTTG_08` | BC Vụ việc theo thời gian (FR-IX-05) | `../../partner-evidence/VVTTG_08.jpg` | `../../reverify-audit/VVTTG_08/VVTTG_08-before-lammoi.png` + `-after-lammoi.png` |
  | 225 | `CLDTBDDDR_09` | BC Lớp đào tạo đang diễn ra (FR-IX-06) | `../../partner-evidence/CLDTBDDDR_09.jpg` | `../../reverify-audit/CLDTBDDDR_09/CLDTBDDDR_09-toolbar.png` |

- Nội dung kiểm tra (chung): Cán bộ nghiệp vụ mở Báo cáo thống kê → chọn loại BC → nhập tiêu chí lọc → Xem báo cáo → **bấm "Xóa bộ lọc"** để đặt bộ lọc về mặc định.
- Expected trong file UAT (đối tác, `KQ mong đợi _09/_08`): "Hệ thống xóa toàn bộ giá trị đã nhập trong các trường lọc và đặt lại về giá trị mặc định (Kỳ = Tháng, Từ ngày = ngày đầu tháng hiện tại, Đến ngày = ngày hiện tại, Đơn vị = đơn vị đăng nhập, các trường khác = 'Tất cả'); khu vực kết quả không tự tải lại cho đến khi NSD bấm 'Xem báo cáo'."
- Actual đối tác ghi (cả 6): **"Màn hình không hiển thị nút chức năng"** (đối tác tìm nút tên "Xóa bộ lọc" nhưng không thấy).

**Đối chiếu SRS v3.5**

- SCR-IX-01 (màn Báo cáo thống kê dùng chung cho cả 23 loại BC) — bảng "Thành phần màn hình" chỉ spec **4 nút** ở toolbar/action-bar: **"Nút Làm mới"** (item 2), "Xem báo cáo" (item 7), "Xuất Excel (.xlsx)" (item 8), "Xuất PDF (.pdf)" (item 9).
- SRS **KHÔNG** có nút tên **"Xóa bộ lọc"** và **KHÔNG** có nút "In báo cáo" trong SCR-IX-01 — chức năng "đặt lại bộ lọc" mà đối tác mong muốn được SRS đặt tên là **"Làm mới"** (item 2).
- SRS **không quy định** giá trị mặc định cụ thể mà thao tác reset phải khôi phục (Kỳ=Tháng, ngày đầu tháng...) — mốc mặc định đó chỉ có trong KQMĐ của đối tác, không có trong SCR-IX-01 §Thành phần màn hình.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1042` — `| 2 | toolbar | Tiêu đề trang | label | "Báo cáo Thống kê" + Nút Làm mới | — | Luôn hiển thị |`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md:1047-1049` — action-bar chỉ có "Xem báo cáo" / "Xuất Excel" / "Xuất PDF" (không có "Xóa bộ lọc").

**Kết quả verify UI hiện tại**

- Verify ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw_03` / CB_NV_TW (Toàn quốc). URL `https://18.143.165.120.nip.io/bao-cao`.
- Liệt kê toolbar bằng `evaluate_script` trên cả 6 loại BC → mỗi màn đúng **4 nút**: `["Làm mới","Xem báo cáo","Xuất Excel","Xuất PDF"]`. `hasXoaBoLoc=false` — **không có nút tên "Xóa bộ lọc"** (khớp evidence đối tác).
- **Test hành vi nút "Làm mới"** (test kỹ 2 đại diện: SLHDVM_09 + VVTTG_08):
  - Nhập bộ lọc khác mặc định (Kỳ=Năm, Lĩnh vực=Thuế) → Xem báo cáo (ra kết quả: SLHDVM Tổng hỏi đáp=11; VVTTG Tổng vụ việc toàn kỳ=6) → bấm **"Làm mới"**.
  - Kết quả: **xóa toàn bộ giá trị đã nhập** (Loại BC, Kỳ, Lĩnh vực, Thời gian về trống), Đơn vị về "Toàn quốc" (= đơn vị đăng nhập của TW); **khu vực kết quả bị xóa, KHÔNG tự tải lại** (nút "Xem báo cáo"/"Xuất" disabled trở lại). URL trả về `/bao-cao` (bỏ hết query params).
- Khác biệt duy nhất vs KQMĐ đối tác: sau reset, bộ lọc về **trống hoàn toàn** (Kỳ chưa chọn) — KHÔNG pre-fill Kỳ=Tháng + ngày đầu tháng như KQMĐ mô tả. Đây cũng là trạng thái mặc định khởi tạo của màn (khi mới mở, Loại BC + Kỳ đều trống).

**Kết luận QA**

- 6 case KHÔNG phải bug theo SRS v3.5: SRS SCR-IX-01 (dòng 1042) spec đúng **"Nút Làm mới"**, app hiển thị đúng nút này và nút này **thực hiện đúng chức năng reset bộ lọc** (xóa filter + xóa kết quả, không tự tải lại) — tức chức năng đối tác cần **CÓ tồn tại**, chỉ khác **TÊN** ("Làm mới" thay vì "Xóa bộ lọc") và khác **giá trị mặc định sau reset** (về trống thay vì Kỳ=Tháng).
- Đối tác quan sát ĐÚNG thực tế (không có nút tên "Xóa bộ lọc") nhưng kỳ vọng tên/hành vi khác SRS → bất đồng về **ĐẶC TẢ**, không phải app sai → `BA confirm` (QA không tự Reject).
- Ghi nhận thêm (không phải căn cứ verdict): màn danh sách khác trong app (vd Đào tạo → Chương trình đào tạo → Danh sách) dùng nút tên **"Xóa bộ lọc"**, trong khi màn Báo cáo thống kê dùng **"Làm mới"** → thiếu nhất quán đặt tên giữa các màn, có thể là lý do đối tác kỳ vọng "Xóa bộ lọc".

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt hướng xử lý cụm "nút Xóa bộ lọc" của màn Báo cáo thống kê (áp dụng chung cho cả 6 case):

- **Hướng 1 (giữ theo SRS):** màn dùng nút **"Làm mới"** (SCR-IX-01 item 2) để đặt lại bộ lọc → web hiện tại đúng SRS; cập nhật lại expected của 6 TC (đổi "Xóa bộ lọc" → "Làm mới", và mô tả reset về trạng thái khởi tạo trống).
- **Hướng 2 (chỉnh theo kỳ vọng đối tác):** (a) đổi tên nút "Làm mới" → "Xóa bộ lọc" cho nhất quán với các màn danh sách khác, và/hoặc (b) khi reset thì pre-fill giá trị mặc định (Kỳ=Tháng, Từ ngày=đầu tháng, Đến ngày=hôm nay) thay vì để trống → cần cập nhật SCR-IX-01 + gửi Dev FE bổ sung.
- Verdict QA đề xuất: **`Cần BA xác nhận`** (đặc tả kỳ vọng đối tác vs SRS lệch nhau về tên nút + giá trị mặc định sau reset). Chưa gửi Dev cho tới khi BA chốt source truth.
