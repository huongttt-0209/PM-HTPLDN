# Audit — QLDMHSDNHT_06 (row 146) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMHSDNHT_06.jpg` (full-res). Form "Thêm mới danh mục" tab **Hồ sơ đề nghị hỗ trợ** — có trường **"Danh mục cha"**.

**Cổng 2 — Bug đối tác:** "Danh mục cha" thừa trong form Thêm mới.

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83) + FR-VIII-08/HSDNHT (dòng 410): không có "Danh mục cha" | Form Thêm mới có "Danh mục cha" (tùy chọn, không chặn lưu) | Thừa → BA confirm |

**Artifact real-data:** `web-them-moi-form.png` (form + trường Danh mục cha, placeholder "Chọn danh mục cha (tùy chọn)", `::before`=none → không có dấu *).

**Verdict:** `BA confirm`. Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1.
