# BA confirmation needed — QTHT Batch 4 (màn Quản lý danh mục dùng chung) — 2026-07-21

> **File này để làm gì:** gom 8 testcase QTHT batch 4 (đối tác báo tuần 3) cùng 1 vấn đề gốc: **đóng form Thêm/Sửa danh mục khi đang nhập/sửa dở KHÔNG hiện hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?"**. QA đã verify tái hiện đúng trên web, nhưng SRS v3.5 **im lặng** về clause này cho màn danh mục → cần BA chốt có bổ sung yêu cầu hay không. Verdict sheet cả 8 case: `BA confirm`.

> **Quy tắc citation:** mọi khẳng định SRS trỏ `path:LINE`, mở file verify số dòng thực. SRS dùng: v3.5 (`input/srs-update-2026-5-5/`).

---

## Tóm tắt cụm — 8 TC, 1 bug gốc

Cả 8 TC đều test cùng 1 hành vi trên màn **Quản lý danh mục dùng chung** (SCR-VIII-01), khác nhau chỉ ở tab danh mục con. Đối tác báo giống hệt nhau: đóng form (nút X / Hủy) khi form đang có dữ liệu chưa lưu → không hỏi xác nhận, đóng thẳng, dữ liệu bị hủy.

| Dòng Excel | Mã TC | Tab danh mục | FR / UC | Verdict |
|---|---|---|---|---|
| 124 | `QLDMLVPL_14` | Lĩnh vực pháp lý | FR-VIII-01 / UC99 | BA confirm |
| 129 | `QLDMLHHT_11` | Loại hình hỗ trợ | FR-VIII-02 / UC100 | BA confirm |
| 137 | `QLDMCTHT_11` | Chương trình hỗ trợ | FR-VIII-03 / UC101 | BA confirm |
| 140 | `QLDMTTVV_11` | Tình trạng vụ việc | FR-VIII-04 / UC102 | BA confirm |
| 134 | `QLDMCQDVQL_12` | Cơ quan đơn vị (tree-view) | FR-VIII-05 / UC103 | BA confirm |
| 143 | `QLDMLDN_11` | Loại doanh nghiệp | FR-VIII-07 / UC105 | BA confirm |
| 147 | `QLDMHSDNHT_11` | Hồ sơ đề nghị hỗ trợ | FR-VIII-08 / UC106 | BA confirm |
| 150 | `QLDMHSDNTT_11` | Hồ sơ đề nghị thanh toán | FR-VIII-09 / UC107 | BA confirm |

---

## [QLDMLVPL_14 · QLDMLHHT_11 · QLDMCTHT_11 · QLDMTTVV_11 · QLDMCQDVQL_12 · QLDMLDN_11 · QLDMHSDNHT_11 · QLDMHSDNTT_11] — Thiếu hộp thoại xác nhận "bỏ thay đổi chưa lưu" khi đóng form danh mục

**Bối cảnh testcase**

- Dòng Excel: 124, 129, 137, 140, 134, 143, 147, 150 — mã TC như bảng trên.
- Nội dung kiểm tra: role QTHT mở form Thêm mới / Sửa một danh mục con, nhập hoặc sửa dở, rồi bấm đóng form (nút X góc phải hoặc nút Hủy).
- Expected trong file UAT (đối tác):
  - Khi đóng form đang có thay đổi chưa lưu, hệ thống phải hỏi xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?" trước khi đóng.
- Actual đối tác ghi: hệ thống đóng thẳng form, không hỏi, thay đổi bị mất.

**Đối chiếu SRS v3.5**

- Màn Quản lý danh mục dùng chung (SCR-VIII-01) mô tả bố cục + thao tác CRUD danh mục qua template dùng chung TPL-DM-CRUD. Phần mô tả form và nút đóng KHÔNG nêu yêu cầu hộp thoại xác nhận khi đóng form đang chỉnh sửa dở.
- §Quy tắc tương tác của màn danh mục chỉ quy định phân trang và sắp xếp, KHÔNG có clause "cảnh báo mất dữ liệu chưa lưu".
- Hộp thoại xác nhận "bỏ thay đổi chưa lưu" LẠI được quy định rõ ở các màn khác (Hỏi đáp pháp lý; Chuyên gia / Tư vấn viên) → cho thấy SRS có khái niệm này nhưng cố ý (hoặc bỏ sót) không áp cho màn danh mục.

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:1606` → `:1608` (SCR-VIII-01 §Quy tắc tương tác — chỉ phân trang + sắp xếp)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:65` → `:171` (TPL-DM-CRUD — mẫu form CRUD danh mục, không có clause dirty-state)
- Đối chiếu ngược (clause CÓ ở màn khác): `input/srs-update-2026-5-5/srs-fr-02-*.md:1070`; `input/srs-update-2026-5-5/srs-fr-04-*.md:1512`, `:1562`, `:1685`, `:1808`

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `admin` (role QTHT).
- URL gốc: `https://18.143.165.120.nip.io/quan-tri/danh-muc/*` (mỗi tab 1 loại danh mục).
- Với mỗi tab: mở form Thêm mới → nhập Mã/Tên/Mô tả (state dirty) → bấm Đóng (X).
- Quan sát đồng nhất cả 8 tab: form đóng thẳng về danh sách, **KHÔNG** hộp thoại xác nhận, **KHÔNG** toast, **0 request** ghi dữ liệu (observer toast-capture.js self-check=1, query `.ant-modal-confirm,[role="dialog"]` rỗng, text "chưa lưu"/"bỏ thay đổi" không xuất hiện). Dữ liệu nhập dở bị hủy im lặng.
- Riêng tab Cơ quan đơn vị (`QLDMCQDVQL_12`) là tree-view (panel phải), hành vi đóng vẫn giống: panel reset về "Chọn một đơn vị từ cây bên trái", không cảnh báo.
- Evidence: `../../reverify-audit/<TC>/BUG-<TC>-add-close-noconfirm.png` (8 ảnh, mỗi TC 1 ảnh).

**Kết luận QA**

- Web tái hiện ĐÚNG như đối tác báo: đóng form dirty không có hộp thoại xác nhận.
- Nhưng đối chiếu SRS v3.5: màn Quản lý danh mục **không quy định** yêu cầu hộp thoại này → web hiện tại **không vi phạm điều khoản nào của SRS cho màn danh mục**.
- Vì clause này CÓ ở màn khác nhưng SILENT ở màn danh mục, QA không tự chốt được đây là "bug thiếu tính năng" hay "đúng đặc tả" → cần BA quyết. Đây là 1 vấn đề gốc chung ở component form danh mục dùng chung (sửa 1 chỗ, cả 8 tab hết).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận yêu cầu nghiệp vụ cho màn Quản lý danh mục dùng chung (SCR-VIII-01):

- **Câu hỏi:** Có bổ sung yêu cầu hệ thống hiển thị hộp thoại xác nhận "Bạn có muốn bỏ các thay đổi chưa lưu?" khi người dùng đóng form Thêm/Sửa danh mục đang có thay đổi chưa lưu không?
- Nếu **CÓ** (đồng bộ với màn Hỏi đáp / Chuyên gia): chuyển Dev FE bổ sung dirty-check + hộp thoại xác nhận cho component form danh mục dùng chung; áp 1 lần cho cả 8 tab. Verdict cập nhật → `Open` (owner Dev FE).
- Nếu **KHÔNG**: web hiện tại đã đúng đặc tả cho màn danh mục; cập nhật lại kỳ vọng của đối tác cho cả 8 TC (không phải bug).
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận` (BA confirm) — chưa gửi Dev cho tới khi BA chốt.
