# Audit — QLDMHSDNHT_13 (row 148) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMHSDNHT_13.jpg` (full-res). Form "Chỉnh sửa danh mục" tab **Hồ sơ đề nghị hỗ trợ** — có trường **"Danh mục cha"**.

**Cổng 2 — Bug đối tác:** "Danh mục cha" thừa trong form Sửa.

**Cổng 3 — SRS vs web:**
| SRS | Web (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (77-83) + FR-VIII-08/HSDNHT (dòng 410): không có "Danh mục cha" | Form Sửa có "Danh mục cha" (tùy chọn, không chặn lưu) | Thừa → BA confirm |

**Artifact real-data:** `web-sua-form.png` (form Sửa + trường Danh mục cha tùy chọn).

**Verdict:** `BA confirm`. Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1.
