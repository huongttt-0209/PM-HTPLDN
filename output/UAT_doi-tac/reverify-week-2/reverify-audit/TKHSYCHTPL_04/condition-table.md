# TKHSYCHTPL_04 — Bảng đối chiếu điều kiện

**Case:** Tìm kiếm vụ việc theo khoảng thời gian hợp lệ (SCR-V.I-01 · FR-V.I-08 UC58).

**Evidence đối tác:** `partner-evidence/TKHSYCHTPL_04.jpg` — **CÓ khoảnh khắc thao tác**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?tab=TAT_CA&**tuNgay=2026-05-08&denNgay=2026-05-18**&page=1`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**.
Ô lọc: **08/05/2026 – 18/05/2026**. Kết quả: "Tất cả **30**" (giảm từ 53 khi không lọc ⇒ bộ lọc CÓ tác dụng).
Các dòng nhìn thấy trong ảnh và **Ngày tiếp nhận** của chúng: 14/05 · 14/05 · 10/05 · 12/05 · 12/05 · 08/05 → **TẤT CẢ đều nằm trong khoảng 08/05–18/05**.
Chi tiết đáng chú ý: đối tác **bôi đen (select) 2 ô** ở dòng đầu — `14/05/2026` (Ngày tiếp nhận) và **`08/06/2026` (cột Deadline thời hạn)**. `08/06/2026` nằm NGOÀI khoảng lọc, nhưng đó là cột **Deadline**, không phải cột được lọc.

**Đối tác phản ánh:** *"Hệ thống hiển thị các bản ghi không đúng với tiêu chí tìm kiếm."*

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" (thấy VV toàn quốc) | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp, thấy 17 VV toàn quốc) | Không |
| Input / giá trị lọc (khoảng ngày) | Lọc khoảng ngày **08/05/2026 – 18/05/2026** trên thanh tìm kiếm, có bấm Tìm kiếm | Lọc khoảng ngày trên **cùng thanh tìm kiếm**, chạy **3 khoảng khác nhau** (rộng / hẹp / 1 ngày) để phân biệt kết quả — xem bảng truy vấn dưới | Không |
| Dữ liệu tiền đề (phải có VV trong VÀ ngoài khoảng lọc) | Dữ liệu đối tác có VV trải nhiều tháng (05/2026, 06/2026...) | Dữ liệu có VV trải **2024-03 → 2026-07** (17 VV: 01/03/2024, 01/06/2024, 15/01/2026, 01/02/2026 ×2, 01/03/2026 ×2, 01/04/2026, 12/07/2026 ×9) ⇒ **có cả VV trong khoảng lẫn ngoài khoảng** để lộ lỗi nếu có | Không |
| Đường thao tác (UI form vs URL) | Thao tác trên UI (URL sinh ra `tuNgay`/`denNgay`) | Test **cả 2 đường**: (a) điền 2 ô ngày trên UI + bấm [Tìm kiếm]; (b) mở thẳng URL có `tuNgay`/`denNgay` — kết quả **giống hệt nhau** | Không |

## Quan sát (real-data) — cbnv_tw, baseline + 3 truy vấn phân biệt

```
BASELINE (không lọc)          → 17 kết quả  (VV từ 01/03/2024 đến 12/07/2026)

[Q1] 01/02/2026 → 31/03/2026  → 4 kết quả:
       DDD-VV-003  (Ngày tiếp nhận 01/02/2026)  ✔ trong khoảng
       EEE-VH-011  (01/02/2026)                 ✔ trong khoảng
       EEE-VH-012  (01/03/2026)                 ✔ trong khoảng
       EEE-VH-013  (01/03/2026)                 ✔ trong khoảng
     → 4/4 đúng tiêu chí. 13 VV ngoài khoảng (15/01/2026, 01/04/2026, 12/07/2026×9, 2024×2) ĐỀU bị loại đúng.
     → Số đếm trên các thẻ tab cũng cập nhật theo bộ lọc: Tất cả 4 · Đang xử lý 1 · Hoàn thành 3.

[Q2] 01/03/2026 → 01/03/2026  → 2 kết quả:  EEE-VH-012 (01/03/2026) · EEE-VH-013 (01/03/2026)
     → lọc 1 ngày duy nhất vẫn chính xác, không lọt VV ngày khác.

[Q3] Đường UI form (điền 2 ô ngày + bấm [Tìm kiếm], khoảng 01/02–31/03/2026)
     → 17 → 4, đúng y hệt Q1 ⇒ đường UI form KHÔNG bị bỏ qua bộ lọc.
```

**Kiểm tra biên:** ngày đầu khoảng (01/02/2026) và ngày cuối khoảng (31/03/2026) đều **bao gồm** (inclusive) — VV ngày 01/02/2026 vẫn được trả về.

Ảnh: `web-loc-khoang-ngay-4-4-ban-ghi-dung-tieu-chi.png`

## Đối chiếu SRS (Cổng 3)

- `srs-fr-05-vu-viec.md:650-651` — FR-V.I-08 (UC58) §Inputs: `tu_ngay` = *"**Từ ngày tiếp nhận**"*, `den_ngay` = *"Đến ngày"* ⇒ bộ lọc khoảng thời gian áp lên cột **Ngày tiếp nhận**, **KHÔNG áp lên cột Deadline / thời hạn**.
- `srs-fr-05-vu-viec.md:658` — §Processing bước 2: *"Kết hợp tất cả điều kiện lọc (AND)"*; bước 4: *"Phân trang (20/trang)"*.
- **Thực tế web:** mọi bản ghi trả về đều có **Ngày tiếp nhận nằm trong khoảng lọc** (4/4 ở Q1, 2/2 ở Q2), phân trang 20/trang → **ĐÚNG SRS**.

**Kết luận:** Lỗi đối tác báo (*"hiển thị bản ghi không đúng tiêu chí tìm kiếm"*) **KHÔNG tái hiện** trên cả 3 truy vấn, cả 2 đường thao tác, với đúng vai trò CB_NV_TW và bộ dữ liệu có cả VV trong lẫn ngoài khoảng → **Reject**.

> **Nguyên nhân có thể gây hiểu nhầm:** trong ảnh đối tác, các dòng nhìn thấy đều có **Ngày tiếp nhận đúng khoảng** (08/05–14/05); ô bị bôi đen `08/06/2026` là cột **"Deadline thời hạn"** — cột này **không phải** đối tượng của bộ lọc khoảng ngày (SRS chỉ lọc theo Ngày tiếp nhận). Nếu đối tác vẫn thấy bản ghi sai, đề nghị gửi **mã VV cụ thể** kèm Ngày tiếp nhận của nó để QA kiểm tra lại.
