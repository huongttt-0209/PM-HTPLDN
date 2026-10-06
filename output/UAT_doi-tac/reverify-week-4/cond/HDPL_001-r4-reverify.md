# Bảng đối chiếu điều kiện — HDPL_001 (row 52) — re-verify R4 sau khi dev báo fix

**Kết luận:** Pass (đo lại đủ 3 ý trên dữ liệu MỚI tự dựng).
- Ý1 — nút công khai ở màn danh sách hỏi đáp, công khai được nhiều bản ghi: **ĐẠT**.
- Ý2 — cột nội dung câu hỏi ở 3 tab Đã duyệt / Công khai / Hoàn thành: **ĐẠT**.
- Ý3 — đồng bộ trạng thái 2 màn: **KHÔNG đồng bộ**, đo lại vẫn đúng như đối tác mô tả, nhưng khớp đặc tả hiện hành (2 bản ghi, 2 vòng đời, mỗi bên có đường công khai riêng) và đã có quyết định của BA từ vòng 1.

> ⚠️ **Phạm vi môi trường:** đo trên **env được giao `18.143.165.120.nip.io`** (bản dựng `V1.0.4`, tài nguyên `assets/index-C-Au2yTy.js`) theo đúng `input/input.md`. Env đối tác `htpldn-uat.ospgroup.vn` đang chạy bản dựng khác (`assets/index-B4L2Psgc.js`, nhãn `V1.0.3`) ⇒ kết luận chứng minh **mã nguồn đã sửa**, chưa chứng minh bản sửa đã được triển khai lên env đối tác; dev cần xác nhận việc triển khai.

| Điều kiện có thể đổi kết quả | Bug gốc (phiếu `HDPL_001` + kết luận vòng 1 ghi trên sheet) | Mình test lại (env nip.io, 31/07/2026 · V1.0.4) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản (ý1 — người bấm công khai) | Phiếu ghi `Tk: cb_nv_tw_03`; phần "Dữ liệu đầu vào" của phiếu lại ghi hành động thuộc **Cán bộ phê duyệt TW/BN/ĐP**. Vòng 1 kiểm bằng `cbpd_tw` | Đo **cả hai**: `cbnv_tw_03` (đúng tài khoản phiếu ghi) và `cbpd_tw_01` (đúng vai trò CB Phê duyệt TW, cùng đơn vị Cục Bổ trợ tư pháp). `cbpd_tw` đăng nhập FAIL nên fallback đúng Rule 7 sang `cbpd_tw_01` — cùng vai trò `CB_PD_TW`, cùng cấp TW, cùng đơn vị | Không |
| Vai trò / tài khoản (ý2 — người đọc bảng) | `cbnv_tw_03` — đúng tài khoản đối tác ghi trong phiếu | `cbnv_tw_03` — đọc header + ô dữ liệu của cả 3 tab bằng chính tài khoản này | Không |
| Vai trò / tài khoản (ý3 — người công khai ở Kho câu hỏi) | Đối tác công khai câu hỏi ở menu Kho câu hỏi rồi quay lại xem trạng thái ở menu Hỏi đáp pháp lý | `cbnv_tw_03` — đúng vai trò CB Nghiệp vụ mà đặc tả giao hành động công khai Kho câu hỏi | Không |
| Entity + trạng thái (state machine) | Bản ghi hỏi đáp ở trạng thái **Đã duyệt** (điều kiện để hiện nút công khai) + bản ghi kho câu hỏi tương ứng | Tự dựng **2 hồ sơ mới** đi trọn vòng đời: Thêm mới → Tiếp nhận → Phân công → Gửi phản hồi → Chờ phê duyệt → Phê duyệt (bằng `cbpd_tw_01`) → **Đã duyệt**: `HD-20260731-001` (A) và `HD-20260731-002` (B). Hệ thống tự sinh 2 bản ghi kho câu hỏi nguồn "Tự động": `QA-20260731-0001`, `QA-20260731-0002` | Không |
| Dữ liệu tiền đề | Câu hỏi đã duyệt thuộc đúng đơn vị của người công khai | Cả 2 hồ sơ có Đơn vị xử lý = Cục Bổ trợ tư pháp - Bộ Tư pháp (TW), trùng đơn vị của `cbpd_tw_01` ⇒ thoả điều kiện "CB PD cùng đơn vị" (`srs-fr-02-hoi-dap.md:1085`) | Không |
| Input / thao tác (ý1) | Vào màn danh sách hỏi đáp, tìm nút công khai cho bản ghi Đã duyệt; đối tác muốn công khai được **nhiều** bản ghi | Tab "Đã duyệt" → tích 1 dòng → đọc thanh hành động; tích thêm dòng thứ 2 → đọc lại; bỏ tích còn 1 → bấm công khai thật, đọc hộp thoại + thông báo + tab đích | Không |
| Input / thao tác (ý2) | Mở lần lượt 3 tab Đã duyệt / Công khai / Hoàn thành, tìm cột nội dung câu hỏi | Mở đúng 3 tab đó, đọc **danh sách tên cột** + **giá trị ô** ở cột nội dung của từng dòng (không kết luận bằng nhìn ảnh) | Không |
| Input / thao tác (ý3) | Công khai câu hỏi ở menu Kho câu hỏi → quay lại menu Hỏi đáp pháp lý đọc trạng thái bản ghi tương ứng | Công khai `QA-20260731-0001` ở Kho câu hỏi (hộp thoại công khai, chọn ảnh hệ thống mặc định) → quay lại màn Hỏi đáp tra `HD-20260731-001` đọc trạng thái | Không |

## Artifact real-data (Gate bằng chứng — loại claim: Hành vi luồng + Hiển thị/render)

- `bug-reports/image/R4-HDPL_001-01-nut-cong-khai-hang-loat-tab-da-duyet.png` — đã mở đọc: tab "Đã duyệt", thanh "Đã chọn 1 bản ghi" + nút **"Công khai hàng loạt"** + nút "Bỏ chọn".
- `bug-reports/image/R4-HDPL_001-02-sau-cong-khai-hd-002-sang-tab-cong-khai.png` — đã mở đọc: sau khi công khai, `HD-20260731-002` nằm ở tab **Công khai**, cột Trạng thái = "Công khai"; số đếm tab đổi từ "Công khai 1" → "Công khai 2", "Đã duyệt 9" → "Đã duyệt 8".
- `bug-reports/image/R4-HDPL_001-03-kho-cau-hoi-QA-0001-cong-khai.png` — đã mở đọc: `QA-20260731-0001` ở Kho câu hỏi, Trạng thái "Công khai", cột Công khai = "Công khai".
- `bug-reports/image/R4-HDPL_001-04-cot-noi-dung-tab-hoan-thanh.png` — đã mở đọc: tab "Hoàn thành", cột **"Nội dung"** là cột thứ 3, có chữ trong ô.
- `bug-reports/image/R4-HDPL_001-05-hoi-dap-HD-001-van-da-duyet-sau-khi-cong-khai-o-kho.png` — đã mở đọc: `HD-20260731-001` vẫn "Đã duyệt" sau khi bản ghi kho tương ứng đã công khai.
- `bug-reports/image/R4-HDPL_001-00-cbpd_tw-login-fail-fallback.png` — đã mở đọc: `cbpd_tw` đăng nhập trả *"Tên đăng nhập hoặc mật khẩu không đúng."* ⇒ căn cứ fallback Rule 7.
- Đọc thẳng dữ liệu bảng (không qua ảnh):
  - Ý1: `Đã chọn 1 bản ghi` → nút `["Công khai hàng loạt","Bỏ chọn"]`; `Đã chọn 2 bản ghi` → vẫn đủ 2 nút; hộp thoại `"Công khai 1 hồ sơ lên Cổng PLQG?"`; thông báo `"Đã công khai 1 hồ sơ lên Cổng PLQG"`.
  - Ý2: cả 3 tab đều có 13 cột, cột `"Nội dung"` ở **vị trí thứ 3**; ô dữ liệu có nội dung thật (vd `"QA R4 HDPL_001 (A): Doanh nghiep can chuan bi ho so gi …"`).
  - Ý3: `QA-20260731-0001` → Trạng thái `Công khai`; `HD-20260731-001` → Trạng thái `Đã duyệt`.

## Phương pháp thứ hai (bắt buộc)

- **Đo bằng 2 vai trò khác nhau để tách "thiếu chức năng" khỏi "không đủ quyền":** với `cbnv_tw_03` (CB Nghiệp vụ), tích 1 rồi 2 dòng ở tab Đã duyệt đều **không** hiện nút công khai hàng loạt; với `cbpd_tw_01` (CB Phê duyệt cùng đơn vị) thì nút hiện ngay khi tích 1 dòng. Chênh lệch này khớp `srs-fr-02-hoi-dap.md:1085` (*"Nút Công khai hàng loạt (dòng 35): chỉ CB PD cùng đơn vị với bản ghi chọn"*) ⇒ ảnh của đối tác chụp bằng tài khoản CB Nghiệp vụ nên không thấy nút là **đúng phân quyền**, không phải thiếu chức năng.
- **Đo cột bằng cấu trúc bảng, không bằng mắt:** đọc mảng tên cột của `thead` (13 cột, `"Nội dung"` ở chỉ số 2) và đọc giá trị từng ô ở cột đó cho cả 3 tab ⇒ loại hẳn khả năng "cột bị khuất do bảng cuộn ngang" mà vòng 1 nêu; cột nằm ở vị trí thứ 3, không cần cuộn.
- **Đo ý3 theo cả hai chiều, không chỉ chiều đối tác nêu:**
  - Chiều đối tác (Kho → Hỏi đáp): công khai `QA-20260731-0001` ⇒ `HD-20260731-001` vẫn `Đã duyệt`.
  - Chiều ngược (Hỏi đáp → Kho): công khai `HD-20260731-002` ⇒ bản ghi kho `QA-20260731-0002` vẫn `Đã duyệt`, cột Công khai = `Chưa`.
  Hai chiều đối xứng ⇒ đây là **thiết kế tách đôi vòng đời**, không phải lỗi một chiều.
- **Đối chiếu đặc tả (mở tệp lấy số dòng, không dẫn theo trí nhớ):**
  - `srs-fr-13-tv-nhanh.md:494-498` — khối **Postconditions** của hành động công khai/hủy công khai Kho câu hỏi liệt kê **đủ** hệ quả: cập nhật `KHO_CAU_HOI.cong_khai` + `trang_thai`; Cổng PLQG tự kéo; ghi nhật ký. **Không có** mục nào yêu cầu đổi trạng thái bản ghi hỏi đáp ⇒ không đồng bộ là khớp đặc tả.
  - `srs-fr-02-hoi-dap.md:1053` — hỏi đáp có **đường công khai riêng** (nút Công khai hàng loạt, tab Đã duyệt, đặt `cong_khai=1` + trạng thái `CONG_KHAI` per-record); `:1045` — bản ghi `CONG_KHAI` phải "Hủy công khai về DA_DUYET" ⇒ hỏi đáp có vòng đời công khai độc lập của riêng nó.
  - ⚠️ **Đính chính một trích dẫn của vòng 1:** ghi chú vòng 1 dẫn *"srs-fr-13:498: công khai bên này không đổi trạng thái bên kia — có chủ đích"*. Mở tệp đặc tả v3.5 chuẩn (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`) thì **dòng 498 là "AUDIT_LOG ghi nhận"**, không phải câu đó; câu trích cũng không tìm thấy ở chỗ nào khác trong tệp. Kết luận vẫn đứng vững nhưng dựa vào khối Postconditions 494-498 nêu trên, **không** dựa vào câu trích đó. Bản SRS "Phase 12" kèm dấu `[HDPL_001 chốt 2026-07-31]` mà ghi chú vòng 1 nhắc tới **không có trong kho tài liệu QA đang dùng**.
