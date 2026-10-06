# Bảng đối chiếu điều kiện — QLTLPLCVV_02 (row 294) — Bảng tư liệu thiếu cột "Ngày tạo" / "Người tạo"

**Kết luận:** BA confirm (SRS tự mâu thuẫn) — Tái hiện đúng: bảng "Tư liệu PL liên kết" hiển thị **7 cột** `Tên tư liệu / Loại / Lĩnh vực / File / Trạng thái / Công khai lúc / Hành động`, **không có "Ngày tạo" và "Người tạo"** (khớp với đối tác). Nhưng SRS mâu thuẫn: mục **Outputs** liệt kê `nguoi_tao` (dòng 937) + `ngay_tao` (dòng 938) đều "luôn"; còn **Thành phần màn hình SCR-X1-02** (dòng 1144) mô tả bảng chỉ gồm `Tên / Loại / Trạng thái / Số file / Hành động` — không có 2 cột này. → không tự chốt Open được, cần BA chọn source truth.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test (cbnv_tw_05 / CB_NV_TW, 21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB NV | cbnv_tw_05 (CB_NV_TW — đúng tác nhân SRS dòng 806, CRUD đầy đủ tư liệu) | Không |
| Màn hình + tab | Bảng danh sách tư liệu | Tab "Tư liệu PL liên kết" (accordion) trong Chi tiết TVCS SCR-X1-02 | Không |
| Entity + trạng thái | Bảng tư liệu bất kỳ | Kiểm trên 2 record: TVCS-20260721-0001 (TIEP_NHAN, 1 tư liệu CONG_KHAI) + record DA_DUYET `5eed0008` | Không |
| Bug tĩnh (không phụ thuộc state/data) | Cột `<thead>` cố định | Đọc `<thead>` — 7 cột cố định mọi record, không có cột ẩn/tooltip Ngày tạo/Người tạo | Không |

**Artifact real-data (đọc DOM `<thead>` trực tiếp):**
- `evaluate_script` trả `tableCols = ["Tên tư liệu","Loại","Lĩnh vực","File","Trạng thái","Công khai lúc","Hành động"]` (7 cột) — trên cả record TIEP_NHAN và DA_DUYET.
- Có cột **"Công khai lúc"** (thời gian công khai) nhưng KHÔNG có **"Ngày tạo"** hay **"Người tạo"**.
- Ảnh: `reverify-audit/QLTLPLCVV_02/tvcs-batchE-02-cot-bang-tu-lieu.png`.

**SRS (mâu thuẫn nội bộ):**
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:937` — Outputs #8 `nguoi_tao | text | luôn`.
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:938` — Outputs #9 `ngay_tao | datetime | luôn | dd/mm/yyyy HH:mm`.
- `input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:1144` — Thành phần màn hình SCR-X1-02: bảng tư liệu = `Tên / Loại / Trạng thái / Số file / Hành động` (KHÔNG có Ngày tạo/Người tạo; cũng không có Lĩnh vực/Công khai lúc mà UI đang có).

→ Outputs (937/938) và Thành phần màn hình (1144) nói khác nhau về cột bảng. Web hiện theo hướng gần 1144 (không có Ngày tạo/Người tạo) + thêm Lĩnh vực & Công khai lúc. Cần BA chốt bảng tư liệu phải gồm những cột nào.
