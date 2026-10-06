# Audit — QLDMTCDGHQ_06 (row 157) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMTCDGHQ_06.jpg` (full-res). Form "Thêm mới danh mục" tab **Tiêu chí đánh giá hiệu quả** — có trường **"Danh mục cha"**.

**Cổng 2 — Bug đối tác:** "Danh mục cha" thừa trong form Thêm mới.

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83) + FR-VIII-11/UC109 (dòng 531): không có "Danh mục cha" | Form Thêm mới có "Danh mục cha" (tùy chọn, không chặn lưu) | Thừa → BA confirm |
| SCR-VIII-01 §Thành phần đặc biệt TCDGHQ (dòng 1594): Trọng số / Thang điểm min / max bắt buộc | Các trường này có dấu * = ĐÚNG spec | Không phải lỗi |

**Artifact real-data:** `web-them-moi-form.png` (form + Danh mục cha; các trường Trọng số/Thang điểm bắt buộc đúng spec).

**Ghi chú env:** tab TCDGHQ trống ("Không có dữ liệu") trên env test — form Thêm mới vẫn mở & render đủ trường để verify.

**Verdict:** `BA confirm`. Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1.
