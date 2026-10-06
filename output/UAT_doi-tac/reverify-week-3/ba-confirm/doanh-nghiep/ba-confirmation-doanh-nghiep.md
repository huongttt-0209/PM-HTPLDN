# BA confirmation needed — Module Doanh nghiệp (Quản lý DN được Hỗ trợ) — Tuần 3 — 2026-07-20

> **File này để làm gì:** gom các testcase module Doanh nghiệp mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đối chiếu SRS + evidence UI để BA quyết nhanh. Các case là lỗi thật có SRS reference rõ (`Open`) nằm ở [../../bug-reports/doanh-nghiep/Pass-bug-report-doanh-nghiep.md) — KHÔNG đưa vào file này.

> **SRS dùng để chấm:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md` (v3.5 — bản được chỉ định cho UAT tuần 3). Mọi citation trỏ file này + số dòng thực (đã mở file verify).

> **Môi trường verify:** `https://18.143.165.120.nip.io` — Chrome DevTools MCP — tài khoản `cbnv_tw`/CB_NV_TW (và `cbnv_hn`/CB_NV_DP Hà Nội cho case _13). Ngày verify: 20/07/2026.

| Case | Dòng Excel | Dạng | Verdict | Câu hỏi gốc |
|------|:---------:|:---:|:-------:|-------------|
| QLDNDHTPL_05 | 26 | A | BA confirm | Nhóm A — Định danh cơ bản: bố cục nhóm trường không giống thiết kế |
| QLDNDHTPL_06 | 27 | A | BA confirm | Nhóm B — Địa lý + Phân loại: bố cục nhóm trường không giống thiết kế |
| QLDNDHTPL_13 | 30 | B | BA confirm | Tỉnh/TP không điền sẵn mặc định — SRS mâu thuẫn (UI vs backend) |
| QLDNDHTPL_17 | 32 | A | BA confirm | Danh sách không sắp xếp khi click tiêu đề cột |
| TKDNHTPL_02 | 41 | A | BA confirm | Thiết kế filter-bar khác SRS (nhãn, default, field Đơn vị) |
| TKDNHTPL_03 | 42 | A | BA confirm | Empty-state hiển thị "Trống" thay vì thông báo cụ thể |

> Các case `Open` (không thuộc file này): QLDNDHTPL_02, _04, _07 (thiếu Nhóm C), _10 (Hủy modal không tô đỏ MST), _14 (Hủy không xác nhận) — xem bug-report.

---

## QLDNDHTPL_05 (và QLDNDHTPL_06) — Form Thêm mới DN nhóm trường theo "Thông tin chung / Thông tin liên hệ" thay vì Nhóm A/B/C

*(Dạng A — QA đã kết luận: không thiếu trường, chỉ khác cách gom; mockup chi tiết SRS chưa chốt.)*

**Bối cảnh testcase**

- Dòng Excel 26, mã TC `QLDNDHTPL_05`. Nội dung kiểm tra: CB Nghiệp vụ mở form Thêm mới DN, kiểm Nhóm A — Định danh cơ bản (Tên DN, MST, Người đại diện, Email, SĐT).
- Dòng Excel 27, mã TC `QLDNDHTPL_06` — cùng vấn đề: kiểm Nhóm B — Địa lý + Phân loại (Tỉnh/TP, Địa chỉ, Loại DN, Quy mô, Ngành nghề).
- Expected trong file UAT:
  - Form nhóm trường đúng theo cấu trúc Nhóm A / Nhóm B / Nhóm C như SRS.
- Actual đối tác ghi: "Bố cục không giống với thiết kế".

**Đối chiếu SRS v3.5**

- SCR-V.III-03 §Bố cục form mô tả form 3 nhóm: Nhóm A — Định danh cơ bản, Nhóm B — Địa lý + Phân loại, Nhóm C — Thông tin bổ sung; liệt kê trường từng nhóm.
- Form chỉ bắt buộc **2 trường tối thiểu**: `ten_doanh_nghiep` + `ma_so_thue`; các trường khác tùy chọn.
- Bản đặc tả **màn hình chi tiết (mockup MH-VII-03)** ghi rõ **"sẽ bổ sung"** → thiết kế UI chi tiết cho màn này **chưa được chốt**; SRS không ràng buộc cứng nhãn/cách gom nhóm.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:550` (§Bố cục form — 3 nhóm A/B/C)
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:588` (2 trường bắt buộc tối thiểu; mockup MH-VII-03 "sẽ bổ sung")

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`/CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/them-moi`.
- Form chia **2 nhóm**: "Thông tin chung" + "Thông tin liên hệ" (tổng 10 trường).
- **Toàn bộ trường Nhóm A đều có mặt và render đúng**: Tên DN (bắt buộc), MST (bắt buộc), Người đại diện, Email, Số điện thoại — không tràn/đè.
- **Toàn bộ trường Nhóm B đều có mặt và render đúng**: Tỉnh/TP, Địa chỉ, Loại DN, Quy mô, Ngành nghề.
- Khác biệt duy nhất so với SRS: **cách gom nhóm/nhãn nhóm** (Thông tin chung/liên hệ thay vì A/B/C). Không thiếu trường Nhóm A hoặc B nào.
- Evidence: `bug-reports/image/BUG-QLDNDHTPL_04-form-them-moi-2-nhom.png`

**Kết luận QA**

- `QLDNDHTPL_05` và `QLDNDHTPL_06` **không phải lỗi thiếu trường** theo SRS v3.5 — mọi trường Nhóm A/B đều hiện đủ và đúng.
- Điểm khác SRS: form gom theo "Thông tin chung"/"Thông tin liên hệ" thay vì tách A/B/C. Nhưng mockup chi tiết MH-VII-03 SRS ghi "sẽ bổ sung" → chưa có cơ sở khẳng định web sai.
- Không để `Reject`: hành vi đối tác báo ("bố cục không giống thiết kế") **có tái hiện**. Không để `Open`: không trường nào bị thiếu + thiết kế chi tiết SRS còn để ngỏ.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý bố cục form Thêm mới DN:

- Form Thêm mới **có bắt buộc gom trường đúng theo Nhóm A / B / C** như §Bố cục form không, hay **chấp nhận cách gom hiện tại** ("Thông tin chung" + "Thông tin liên hệ") vì mockup MH-VII-03 chưa chốt?
- Nếu BA yêu cầu đúng A/B/C → mở lỗi UI-UX "form gom nhóm sai thiết kế" (chỉ đổi cách nhóm/nhãn, trường đã đủ), verdict chuyển `Open`.
- Nếu BA chấp nhận cách gom hiện tại → 2 case khép lại (không phải lỗi).
- Phân biệt với Nhóm C: khác hẳn — Nhóm C thiếu **toàn bộ 11 trường** → đó là `Open` (BUG-QLDNDHTPL_04), không thuộc diện này.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev cho tới khi BA chốt cách gom.

---

## QLDNDHTPL_17 — Danh sách DN không sắp xếp khi click tiêu đề cột

*(Dạng A — QA đã kết luận: SRS không yêu cầu sắp xếp tương tác, expected đối tác vượt SRS.)*

**Bối cảnh testcase**

- Dòng Excel 32, mã TC `QLDNDHTPL_17`. Nội dung kiểm tra: CB Nghiệp vụ vào danh sách DN, bấm vào tiêu đề cột cần sắp xếp.
- Expected trong file UAT:
  - "Hệ thống sắp xếp danh sách theo cột đó, luân phiên tăng dần / giảm dần qua mỗi lần bấm."
- Actual đối tác ghi: "Hệ thống không thực hiện sắp xếp khi nhấn vào tên cột."

**Đối chiếu SRS v3.5**

- SCR-V.III-01 §Quy tắc tương tác **chỉ** quy định: "Sắp xếp mặc định: ngày cập nhật mới nhất trước".
- Bảng thành phần cột danh sách (Mã DN, Tên DN, MST, Quy mô, Ngành nghề, Địa chỉ, Số lần hỗ trợ, Tổng chi phí, Hành động) **không** định nghĩa hành vi click-to-sort cho cột nào.
- → SRS **không yêu cầu** sắp xếp tương tác theo cột; app đáp ứng đúng phần "sắp xếp mặc định".

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:448` (chỉ "Sắp xếp mặc định: ngày cập nhật mới nhất trước")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:436-443` (bảng cột — không cột nào có hành vi sort)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`/CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/danh-sach`.
- Click tiêu đề cột (Tên DN, MST...) **không sắp xếp** — tái hiện đúng đối tác.
- Kiểm DOM: **không cột nào** có class `ant-table-column-has-sorters`, không có sort-icon (`.ant-table-column-sorter`), không có `aria-sort` → bảng không cấu hình sort tương tác.
- Evidence: `bug-reports/image/QLDNDHTPL_17-bang-khong-sort.png`

**Kết luận QA**

- `QLDNDHTPL_17` **không vi phạm SRS v3.5** — SRS không yêu cầu sắp xếp tương tác theo cột, chỉ yêu cầu sort mặc định (web đã đáp ứng).
- Hành vi đối tác báo (không sort khi click cột) **có tái hiện**, nhưng đó là do SRS không định nghĩa tính năng này — expected đối tác là kỳ vọng UX vượt phạm vi SRS.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Danh sách DN **có cần bổ sung** click tiêu đề cột để sắp xếp tăng/giảm (đối tác kỳ vọng) không, hay chỉ cần sắp xếp mặc định như SRS?
- Nếu BA yêu cầu bổ sung → tạo enhancement/lỗi "thiếu sắp xếp theo cột", owner `Dev FE`, verdict chuyển `Open`.
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev (SRS chưa yêu cầu — cần BA quyết có bổ sung feature).

---

## TKDNHTPL_02 — Bộ lọc / tìm kiếm danh sách DN khác thiết kế SRS (5 ý con)

*(Dạng A — QA đã kết luận từng ý: 1 ý bác hẳn, 4 ý là câu hỏi thiết kế filter-bar.)*

**Bối cảnh testcase**

- Dòng Excel 41, mã TC `TKDNHTPL_02`. Nội dung kiểm tra: CB Nghiệp vụ vào danh sách DN, kiểm các trường điều kiện tìm kiếm / bộ lọc.
- Expected trong file UAT: các trường filter hiển thị giống thiết kế, đúng định dạng, không tràn/đè.
- Actual đối tác ghi 5 ý: (1) placeholder "Lĩnh vực kinh doanh" đang là "Ngành nghề"; (2) không đặt default "tất cả" cho Quy mô/Tỉnh/TP/Lĩnh vực KD; (3) Lĩnh vực KD chỉ chọn 1 giá trị; (4) không hiển thị field "Đơn vị" cho cấp Trung ương; (5) hiển thị 1 field tìm kiếm "không có ý nghĩa".

**Đối chiếu SRS v3.5**

- SCR-V.III-01 filter-bar định nghĩa **6 field**: Từ khóa (tên DN/MST), Quy mô, Tỉnh thành, Lĩnh vực KD (multi-select có search, VSIC cấp 4), Từ ngày, Đến ngày + nút Tìm kiếm / Xóa bộ lọc.
- Field Lĩnh vực KD được đặc tả rõ là **multi-select** — "chọn 1 hoặc nhiều ngành VSIC cấp 4".
- Filter-bar SRS **không có** field "Ngành nghề" (nganh_nghe là cột bảng, không phải field lọc) và **không có** field "Đơn vị"; cột "Mặc định" của các select = "—" (không quy định default "Tất cả").

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:427-434` (filter-bar 6 field; không có Đơn vị/Ngành nghề; không default "Tất cả")
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:430` (Lĩnh vực KD = multi-select có search)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`/CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/danh-sach`.
- Filter-bar thực tế: Từ khóa (tên/MST), Tỉnh/TP, Quy mô, **Ngành nghề** (single-select), **Lĩnh vực KD "Chọn ngành VSIC cấp 4"** (multi-select) + "Bộ lọc nâng cao (2)" = Từ ngày / Đến ngày.
- Đối chiếu từng ý đối tác:

| # | Ý đối tác | Quan sát live | Nhận định |
|---|---|---|---|
| 1 | Placeholder "Lĩnh vực KD" đang là "Ngành nghề" | App có field **riêng** "Ngành nghề" + field Lĩnh vực KD placeholder "Chọn ngành VSIC cấp 4"; không có nhãn "Lĩnh vực kinh doanh" | Nhãn/placeholder khác SRS ("Lĩnh vực KD") — cần BA chốt nhãn |
| 2 | Không default "tất cả" cho Quy mô/Tỉnh/Lĩnh vực | Các select trống (placeholder), không default | SRS cột Mặc định = "—" (không quy định "Tất cả") — cần BA chốt |
| 3 | Lĩnh vực KD **chỉ chọn 1 giá trị** | Field Lĩnh vực KD (VSIC) là **multi-select** (`ant-select-multiple`) — chọn được nhiều | **KHÔNG tái hiện** — app đúng SRS dòng 430 |
| 4 | Không có field "Đơn vị" cho cấp TW | Filter-bar không có field Đơn vị | SRS filter-bar **không định nghĩa** field Đơn vị — cần BA chốt có cần cho TW không |
| 5 | 1 field tìm kiếm "không có ý nghĩa" | App có thêm field "Ngành nghề" ngoài danh sách SRS | Field thừa vs SRS — cần BA chốt giữ/bỏ |

- Evidence: `bug-reports/image/TKDNHTPL_02-filter-bar.png`

**Kết luận QA**

- Ý (3) "Lĩnh vực KD chỉ chọn 1 giá trị" — **QA bác**: field Lĩnh vực KD là multi-select đúng SRS dòng 430, không phải lỗi.
- 4 ý còn lại (1, 2, 4, 5) — QA **không tự chốt Open được**: SRS filter-bar không đủ ràng buộc về nhãn / default "Tất cả" / field Đơn vị, và app thêm field "Ngành nghề" ngoài SRS. Đây là các điểm thiết kế cần BA quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt thiết kế filter-bar chuẩn:

- Danh sách + nhãn field filter-bar (có giữ "Ngành nghề" không? nhãn "Lĩnh vực KD" vs "Chọn ngành VSIC cấp 4"?).
- Các select có cần **default "Tất cả"** không?
- Cấp Trung ương có cần **field Đơn vị** để lọc không (SRS chưa có)?
- Verdict QA đề xuất: `Cần BA xác nhận` (ý 3 đã bác — không gửi Dev; 4 ý còn lại chờ BA chốt thiết kế rồi mới quyết Open/không).

---

## TKDNHTPL_03 — Tìm kiếm không kết quả: hiển thị "Trống" thay vì thông báo cụ thể

*(Dạng A — QA đã kết luận: empty-state hợp lệ, SRS không quy định câu chữ.)*

**Bối cảnh testcase**

- Dòng Excel 42, mã TC `TKDNHTPL_03`. Nội dung kiểm tra: CB Nghiệp vụ nhập tiêu chí tìm kiếm không khớp bản ghi nào.
- Expected trong file UAT:
  - "Hệ thống để trống vùng kết quả và hiển thị thông báo **'Không tìm thấy doanh nghiệp phù hợp'**."
- Actual đối tác ghi: "Hệ thống hiển thị 'Trống'."

**Đối chiếu SRS v3.5**

- SCR-V.III-01 mô tả màn danh sách hỗ trợ tìm kiếm/lọc đa tiêu chí, nhưng **không quy định câu chữ empty-state cụ thể** khi tìm kiếm không ra kết quả.
- "Trống" là mô tả mặc định của component empty (`.ant-empty`) — thuộc nhóm empty-state hợp lệ theo phân loại QA, nhưng ít thông tin hơn thông báo đối tác kỳ vọng.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:414` (mô tả màn hỗ trợ tìm kiếm/lọc — không nêu câu chữ empty-state)

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, tài khoản `cbnv_tw`/CB_NV_TW.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/danh-sach?search=ZZZKHONGTONTAI999XYZ`.
- Vùng kết quả 0 dòng, hiển thị **"Trống"** (mô tả của `.ant-empty`). Tái hiện đúng đối tác.
- Evidence: `bug-reports/image/TKDNHTPL_03-empty-trong.png`

**Kết luận QA**

- `TKDNHTPL_03` **không vi phạm SRS v3.5** — SRS không quy định câu chữ empty-state, "Trống" là empty-state hợp lệ.
- Quan sát đối tác ("hiển thị Trống") **đúng**, nhưng đây là kỳ vọng UX về câu chữ, chưa đủ căn cứ SRS để kết luận Open.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận:

- Empty-state khi tìm không ra có **bắt buộc thông báo cụ thể** "Không tìm thấy doanh nghiệp phù hợp" không, hay chấp nhận empty component "Trống" hiện tại?
- Nếu BA yêu cầu message cụ thể → mở lỗi copy (owner `Dev FE`), verdict chuyển `Open` (Minor).
- Verdict QA đề xuất: `Cần BA xác nhận`, chưa gửi Dev (SRS chưa quy định message — cần BA quyết).

---

## QLDNDHTPL_13 — Form Thêm mới không điền sẵn Tỉnh/TP theo đơn vị CB đăng nhập

*(Dạng B — SRS tự mâu thuẫn: UI default vs backend-set-lúc-lưu.)*

**Bối cảnh testcase**

- Dòng Excel 30, mã TC `QLDNDHTPL_13`. Nội dung kiểm tra: CB Nghiệp vụ mở form Thêm mới DN, kiểm mặc định trường Tỉnh/Thành phố khi chưa nhập.
- Expected trong file UAT: "Hệ thống đặt mặc định [Tỉnh/TP] theo đơn vị của cán bộ đăng nhập." Đối tác báo: "Hệ thống không đặt mặc định theo đơn vị."

**Kết quả verify UI hiện tại**

- Verify lại ngày 20/07/2026 qua Chrome DevTools MCP, 2 tài khoản.
- Mở URL `https://18.143.165.120.nip.io/doanh-nghiep/them-moi`.
- **CB_NV_TW (Trung ương):** field Tỉnh/TP **trống** ("Vui lòng chọn"). Hợp lý — TW xem toàn quốc (BR-AUTH-08), không có 1 tỉnh cụ thể để mặc định.
- **CB_NV_DP Hà Nội (địa phương, `cbnv_hn`):** field Tỉnh/TP **cũng trống** ("Vui lòng chọn") — trong khi đơn vị là Hà Nội, đáng lẽ mặc định "Hà Nội".
- → UI **không** điền sẵn Tỉnh theo đơn vị, kể cả với cán bộ địa phương.
- Evidence: `bug-reports/image/QLDNDHTPL_13-tinh-khong-default-hanoi.png` (form CB_NV_DP Hà Nội, Tỉnh trống)

**Điểm mâu thuẫn trong SRS v3.5**

1. Theo **SCR-V.III-03 §Bố cục form (Nhóm B)**, Tỉnh/TP phải điền sẵn ở UI:
   - "Tỉnh/Thành phố | dropdown searchable | ... **Default tự suy diễn**: theo đơn vị CB NV đăng nhập (BR-AUTH-08). CB NV có thể chỉnh nếu DN ở tỉnh khác."
   - → UI **nên điền sẵn** để CB thấy và chỉnh.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:566`

2. Nhưng **FR-V.III-NEW-03 §Xử lý (bước validate/lưu)** lại đặt default ở backend lúc lưu:
   - "Validate 2 trường bắt buộc... Nếu `tinh_thanh_id` chưa nhập → **set default = tinh_thanh_id của đơn vị CB NV** đăng nhập".
   - → Backend **gán mặc định lúc lưu** nếu trống → UI trống vẫn ra data đúng, không cần prefill.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-07-doanh-nghiep.md:292`

**Câu hỏi cần BA xác nhận**

Form Thêm mới DN có bắt buộc **điền sẵn Tỉnh/TP theo đơn vị CB ngay trên UI** không? Cần hiểu theo hướng nào?

1. **Hướng 1 — theo SCR-V.III-03 dòng 566 (UI prefill):** form phải hiển thị sẵn Tỉnh = tỉnh của đơn vị CB (với ĐP), CB có thể chỉnh.
2. **Hướng 2 — theo FR-V.III-NEW-03 dòng 292 (backend-lúc-lưu):** UI để trống là chấp nhận được, hệ thống tự gán tỉnh của đơn vị khi lưu nếu để trống.

**Đề xuất QA tạm thời**

- Chưa gửi bug này cho Dev cho tới khi BA chốt source truth.
- Tạm verdict cho `QLDNDHTPL_13`: `Cần BA xác nhận`.
- Nếu BA chọn hướng 1 (UI prefill): UI hiện tại là `Vẫn lỗi` (không prefill kể cả cán bộ ĐP Hà Nội), owner `Dev FE`.
- Nếu BA chọn hướng 2 (backend-lúc-lưu): UI hiện tại **có thể không phải lỗi** — cần verify thêm hành vi backend khi lưu DN không nhập Tỉnh (chưa verify để tránh tạo data rác); nếu backend gán đúng thì khép case, cập nhật lại expected testcase cho khớp.
