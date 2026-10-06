# Câu hỏi cần BA confirm — Verify Bug 2026-06-02

| Thông tin | Giá trị |
|-----------|---------|
| **Dự án** | PM HTPLDN |
| **Môi trường** | http://103.172.236.130:3000/ |
| **Người verify** | QA Automation (Claude Code) |
| **Ngày** | 2026-06-02 22:46:00 |
| **Nguồn** | [`verify-report-2026-06-02.md`](./verify-report-2026-06-02.md) · [`tasks/srs-contradictions.md`](../../../../tasks/srs-contradictions.md) |
| **Số câu chờ BA** | 1 (SRS-C-006) |

> Mỗi câu: lý do + SRS quote (mở file verify line số) + hiện trạng phần mềm + câu hỏi cụ thể cần BA chốt.

---

## STT 49 (CT HTPLDN) — SRS-C-006 — Chương trình HTPLDN có hỗ trợ file đính kèm không?

- **Lý do:** Bug #49 — upload file ở màn CT (Dự thảo) rồi Lưu → BE trả 500. Khi kiểm chứng SRS phát hiện **mâu thuẫn nội bộ**: màn hình hứa upload nhưng data-model không có chỗ lưu file cho CT.
- **SRS quote:**
  - Tầng màn hình: `srs-update-2026-5-5/srs-fr-15-ct-htpldn.md:1132` — "| 19 | form | File dinh kem | file-upload (C15) | -- | upload | **khi DU_THAO** |".
  - Tầng Inputs: `srs-fr-15-ct-htpldn.md:127-137` — FR-XI-01 chỉ 9 trường, KHÔNG có `file_dinh_kem`.
  - Tầng ràng buộc: `srs-v3.5.md:3238` — FILE_DINH_KEM CHECK 8 `entity_type`, **KHÔNG có CHUONG_TRINH_HTPL**.
  - Entity: `srs-v3.5.md:2070-2083` — CHUONG_TRINH_HTPL không có cột file.
- **Hiện trạng phần mềm:** Màn CT Dự thảo hiện nút "Tải lên" (C15). Upload file → `POST /chuong-trinh-htpls/upload` = **201** OK; nhưng Lưu (`PATCH` có `fileDinhKemIds`) = **500 `ERR-SYS-00-00-01`**; cùng PATCH không kèm file = 200.
- **Câu hỏi BA:** CT HTPLDN (FR-XI-01) **có** hỗ trợ đính kèm file (C15 line 1132) hay không?
  - Nếu **CÓ** → bổ sung định nghĩa lưu trữ (Inputs + entity + `FILE_DINH_KEM` thêm `entity_type=CHUONG_TRINH_HTPL`). Khi đó bug #49 nâng Major (Data).
  - Nếu **KHÔNG** → gỡ C15 khỏi `srs-fr-15:1132` + FE ẩn nút upload.
  - **Độc lập với 2 hướng trên:** BE phải sửa trả lỗi nghiệp vụ 4xx rõ ràng thay vì 500 `ERR-SYS` (lỗi xử lý ngoại lệ — bug #49).
- **Tham chiếu:** `tasks/srs-contradictions.md` SRS-C-006 (Open).

---

## STT 22 (dao-tao) — Mô tả bài giảng: ĐÃ CHỐT PASS theo bug gốc (user quyết 2026-06-02)

> **Trạng thái:** Đã chốt — **PASS** theo bug gốc. KHÔNG còn chờ BA để đóng STT 22. Phần dưới giữ lại làm khuyến nghị align SRS (tùy BA).

- **Quyết định:** User chốt làm theo bug gốc → Mô tả bài giảng **tùy chọn** = đúng nghiệp vụ (đã có record thật tạo không mô tả). STT 22 = ✅ Đạt / PASS.
- **Lưu ý spec (khuyến nghị, không block đóng):** SRS hiện vẫn ghi `mo_ta` = **bắt buộc (Y)** ở 3 nguồn:
  - `srs-update-2026-5-5/srs-fr-03-dao-tao.md:705` — "| 2 | mo_ta | text (long) | **Y** | — |" (FR-III-07 Inputs).
  - `srs-update-2026-5-5/srs-v3.5.md:2402` — Entity BAI_GIANG §3.4.3.20: "| 5 | mo_ta | text | **Y** |".
  - v3 legacy `srs-fr-03-dao-tao.md:576` — cũng = Y (không deprecate trong CHANGELOG).
- **Đề xuất BA:** Để UI khớp SRS, cập nhật SRS field `mo_ta` (FR-III-07 Inputs line 705 + entity BAI_GIANG line 2402) từ **Y → N**. Đây là khuyến nghị cập nhật tài liệu, không ảnh hưởng việc đóng STT 22.

---

*File generated: 2026-06-02 21:00:00 | Cập nhật: 2026-06-02 22:46:00 | QA Automation via Claude Code*
