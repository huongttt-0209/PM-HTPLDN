# Row 173 — QLPQCN_02 — re-verify 2026-07-25 R5

Kết quả: **PASS** (đủ 5 điều kiện a–e). Tài khoản `admin` (QTHT). Vai trò thử: **CB_PD_BN — Cán bộ Phê duyệt Bộ/Ngành** (chọn vai trò không session nào đang dùng, theo đúng yêu cầu "vai trò KHÔNG dùng cho test khác").

## Đối chiếu từng điều kiện

| | Điều kiện | Kết quả | Số liệu đo |
|---|---|---|---|
| (a) | Mở phân quyền từ danh sách vai trò tải đúng quyền của vai trò được chọn; màn cho biết rõ đang thao tác trên vai trò nào | ✅ | Tiêu đề: "**Phân quyền vai trò: Cán bộ Phê duyệt Bộ/Ngành**". Mở 2 vai trò khác nhau cho 2 tập quyền khác nhau: CB_NV_DP = 235 quyền, CB_PD_TW = 102 quyền (153 mã chỉ có ở CB_NV_DP, 20 mã chỉ có ở CB_PD_TW) → không dính dữ liệu vai trò mở trước |
| (b) | Có chức năng đưa quyền về mặc định kèm bước xác nhận | ✅ | Nút "Reset về mặc định" + hộp xác nhận: "Reset về mặc định (SEED gốc) — Khôi phục bộ quyền của vai trò về đúng bộ mặc định gốc theo cấu hình hệ thống? Thao tác này ghi đè bộ quyền hiện tại." (Hủy / Reset) |
| (c) | Chọn Hủy → không đổi | ✅ | Sau khi Hủy: tập quyền trùng khớp hoàn toàn ảnh A |
| (d) | Chọn Đồng ý → tập quyền KHÁC ảnh A; lưu/tải lại vẫn giữ | ✅ | Reset trả lại đúng 3 quyền đã bị bỏ (`approve_bao_cao`, `export_bao_cao`, `read_dashboard`) và gỡ đúng 3 quyền đã thêm (`read_audit_log`, `delete_thong_bao`, `import_ngan_hang_cau_hoi`). Lưu + tải lại → giữ nguyên 102 quyền |
| (e) | Làm 2 lần cho ra cùng một kết quả | ✅ | Lần 2 sửa bộ quyền KHÁC hẳn (thêm `create_bao_cao`, `update_bao_cao`, `delete_bai_giang`, `create_giang_vien`; bỏ `read_bao_cao`, `read_thong_bao` → 104 quyền) rồi reset. **Kết quả reset lần 1 và lần 2 giống nhau từng mã quyền** (102/102), và trùng đúng bộ quyền gốc trước khi test |

## Phép thử quyết định (bước 3 — bắt buộc, đã làm)

Trước khi reset, đã **tạo khác biệt rồi LƯU**, tải lại trang xác nhận đã lưu thật (`read_audit_log` = tích, `approve_bao_cao` = bỏ tích sau khi reload). Nhờ vậy phân biệt được "đưa về mặc định" với "chỉ tải lại dữ liệu đã lưu": nếu chỉ tải lại thì kết quả sau reset phải trùng ảnh A — thực tế nó KHÁC ảnh A và quay về bộ SEED gốc.

## So với lượt kiểm trước (sáng 25/07)

Cả 3 điểm bị báo lỗi trước đó đều đã sửa:

- **Màn không cho biết đang thao tác trên vai trò nào** → nay tiêu đề ghi rõ tên vai trò.
- **Reset chỉ bỏ thay đổi chưa lưu, không khôi phục bộ mặc định** → nay reset trả về đúng bộ SEED gốc, khác với tập vừa lưu.
- **Nút Reset bị làm mờ khi màn chưa có thay đổi** → nay nút luôn bấm được (đo ngay sau khi tải lại trang, chưa thao tác gì: `disabled = false`).

## Giới hạn của lần kiểm này

Theo đúng ghi chú trong tiêu chí: đặc tả chỉ có một dòng về nút reset và **không định nghĩa "mặc định" gồm những quyền gì** ở mức mã quyền. Vì vậy 6 bước trên chứng minh được chức năng CÓ chạy, có xác nhận, và cho kết quả ỔN ĐỊNH (2 lần giống hệt nhau) — nhưng **chưa kiểm được nội dung bộ mặc định có đúng nghiệp vụ hay không**. Cần BA cung cấp bảng quyền mặc định theo từng vai trò ở mức mã quyền mới bổ sung được bước đối chiếu từng quyền.

## Ảnh hưởng dữ liệu

Vai trò CB_PD_BN kết thúc ở đúng **102 quyền như trước khi test** (chính thao tác reset đã đưa về bộ gốc). Đối chiếu: `quyen-goc-CB_PD_BN.json` == `sau-reset-lan-1.json` == `sau-reset-lan-2.json`. Không vai trò nào khác bị sửa; các vai trò CB_NV_DP và CB_PD_TW chỉ mở ra đọc.
