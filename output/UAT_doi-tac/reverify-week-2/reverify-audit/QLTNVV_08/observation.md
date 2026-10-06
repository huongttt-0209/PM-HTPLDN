# Quan sát real-data — QLTNVV_08 (Sắp xếp theo cột)

Claim đối tác thuộc dạng **"absence"** ("không thực hiện sắp xếp khi nhấn vào tên cột") → phải tự chạy đúng thao tác và chứng minh **không có gì xảy ra** bằng nhiều đường độc lập, không chỉ nhìn ảnh.

## Cách 1 — Rà DOM toàn bộ 10 cột: không cột nào có cơ chế sắp xếp

Không cột nào có class `ant-table-column-has-sorters`, không có icon `.ant-table-column-sorter`, không có thuộc tính `aria-sort`:

- "Mã VV" → sorter: KHÔNG
- "Tên DN" → sorter: KHÔNG
- "Lĩnh vực PL" → sorter: KHÔNG
- "Kênh tiếp nhận" → sorter: KHÔNG
- "Trạng thái" → sorter: KHÔNG
- "Người xử lý / Tổ chức" → sorter: KHÔNG
- "Ngày tiếp nhận" → sorter: KHÔNG
- "Deadline thời hạn" → sorter: KHÔNG
- "Cảnh báo thời hạn" → sorter: KHÔNG
- "Hành động" → sorter: KHÔNG

## Cách 2 — Tự bấm tiêu đề cột: thứ tự KHÔNG đổi

Bấm lần lượt tiêu đề "Mã VV" → "Ngày tiếp nhận" → "Deadline thời hạn" (mỗi lần chờ ~1s):

Thứ tự TRƯỚC khi bấm:
`VV-BTP-TW-20260712-001, DDD-VV-001, DDD-VV-002, DDD-VV-003, VV-SEED-0001, EEE-VH-012, EEE-VH-013, EEE-VH-014, EEE-VH-011`

Thứ tự SAU khi bấm cả 3 cột:
`VV-BTP-TW-20260712-001, DDD-VV-001, DDD-VV-002, DDD-VV-003, VV-SEED-0001, EEE-VH-012, EEE-VH-013, EEE-VH-014, EEE-VH-011`

⇒ **Giống hệt nhau — thứ tự không đổi.** Nếu có sắp xếp tăng/giảm dần thì "Mã VV" phải đảo về `DDD-VV-001 … VV-SEED-0001` (A→Z) hoặc ngược lại.

## Cách 3 — Rà network: không có tham số sắp xếp nào được gửi

Toàn bộ lời gọi API danh sách vụ việc trong phiên:

- `/api/v1/vu-viecs?page=1&pageSize=20`
- `/api/v1/vu-viecs?keyword=EEE&page=1&pageSize=20`
- `/api/v1/vu-viecs/export`

Không có `sort` / `order` / `sortBy` / `orderBy` trong bất kỳ request nào (kiểm bằng regex trên `performance.getEntriesByType('resource')` → `anySortParam: false`). Bấm tiêu đề cột **không phát sinh request mới**.

## Đối chiếu SRS

`srs-fr-05-vu-viec.md` dòng **1647** — SCR-V.I-01 §Quy tắc tương tác, nguyên văn:

> "Sắp xếp mặc định: ngày cập nhật DESC. **Hỗ trợ sort theo từng cột**"

⇒ SRS yêu cầu rõ ràng danh sách phải hỗ trợ sắp xếp theo từng cột. Web **không có cơ chế sắp xếp trên bất kỳ cột nào**.

Đối chiếu thêm với bản thiết kế (prototype nội bộ `pages/vu-viec/danh-sach.tsx`): có gắn `sorter` cho 3 cột "Mã vụ việc", "Ngày tiếp nhận", "Deadline SLA" → thiết kế cũng có sắp xếp, bản dựng thật thì không.

**Verdict: Open** — lỗi đối tác báo tái hiện đúng, và vi phạm rõ clause SRS dòng 1647.
