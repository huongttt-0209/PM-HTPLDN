# BA confirmation needed — QTHT Batch 5 (DM List-level) — 2026-07-21

> Gom testcase QTHT Batch 5 mà QA cần BA phản hồi lại đối tác. Citation trỏ `srs-update-2026-5-5/` (v3.5) / `srs-v3.5/` — đã mở file verify số dòng thực.

---

## QLDMCQDVQL_05 — Tìm kiếm cây "Cơ quan đơn vị" không ra kết quả, không hiện thông báo "Không tìm thấy"

**Bối cảnh testcase**

- Dòng Excel: 139, mã TC `QLDMCQDVQL_05`.
- Nội dung kiểm tra: QTHT vào **Quản trị hệ thống → Danh mục dùng chung → Cơ quan đơn vị** (giao diện cây đơn vị — Tree View), gõ từ khóa tìm kiếm không khớp bản ghi nào.
- Expected trong file UAT:
  - Khi tìm kiếm không ra kết quả, hệ thống phải hiển thị thông báo **"Không tìm thấy mục danh mục phù hợp"**.
- Actual đối tác ghi: gõ "tư pháp HCM" → vùng cây đơn vị **trắng hoàn toàn**, không có thông báo nào.

**Đối chiếu SRS v3.5**

- TPL-DM-CRUD §Processing chung — Tìm kiếm (SEARCH) chỉ quy định: nhận từ khóa → tìm theo mã/tên (bản ghi chưa xóa) → phân trang + trả kết quả. **Không quy định thông báo chuẩn khi kết quả rỗng.**
- Acceptance Criteria chung về tìm kiếm chỉ nêu: "Given QTHT tìm kiếm When nhập từ khóa Then hiển thị kết quả matching" — không mô tả trạng thái khi 0 kết quả.
- Toàn bộ template TPL-DM-CRUD (áp cho 15 màn danh mục, gồm Cơ quan đơn vị UC103) không có mã lỗi / message cho "search rỗng".

**Citation**

- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:130` (SEARCH — bước 1-3, không có empty message)
- `input/srs-update-2026-5-5/srs-fr-10-quan-tri.md:170` (AC tìm kiếm — chỉ hiển thị kết quả matching)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản `admin` (QTHT).
- Mở `https://18.143.165.120.nip.io/quan-tri/danh-muc/CO_QUAN_DON_VI`, gõ đúng từ khóa "tư pháp HCM" (không khớp) vào ô tìm "Cây đơn vị".
- Vùng cây `.ant-tree` innerText length = 0 (trắng, không node). Không có `.ant-empty` trong panel cây → **không hiện message nào** (kể cả "Trống").
- → **Tái hiện đúng** quan sát của đối tác. Actual đối tác chính xác.
- Evidence: `../../reverify-audit/QLDMCQDVQL_05/search-empty-tree.png`

**Kết luận QA**

- `QLDMCQDVQL_05` **không phải bug theo SRS v3.5**: SRS không quy định thông báo cho tìm kiếm rỗng, nên app để trống không vi phạm clause SRS nào.
- Tuy nhiên, actual đối tác quan sát là ĐÚNG (vùng cây trắng, không feedback). Đây là bất đồng về **kỳ vọng UX** vs **đặc tả** (SRS silent) → cần BA quyết, QA không tự Reject.
- Cross-ref cụm empty-state: `QLTKND_06` (Batch 8 — màn Tài khoản hiện "Trống" thay vì "Không tìm thấy tài khoản phù hợp"). Nghi thiếu empty-state chuẩn dùng chung cho các màn tìm kiếm.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA xác nhận hướng xử lý:

- Có bổ sung yêu cầu **empty-state message** cho tìm kiếm không ra kết quả (ít nhất "Không tìm thấy dữ liệu phù hợp") vào SRS TPL-DM-CRUD §SEARCH cho các màn danh mục (gồm cả cây Cơ quan đơn vị) hay không?
- Nếu **CÓ** → chuyển Dev bổ sung empty-state (owner: Dev FE), đồng bộ cả cụm (QLTKND_06). Verdict khi đó: `Vẫn lỗi`.
- Nếu **KHÔNG** → giữ nguyên, cập nhật expected của `QLDMCQDVQL_05` (bỏ yêu cầu message). Verdict: `Không phải bug theo SRS`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev.
