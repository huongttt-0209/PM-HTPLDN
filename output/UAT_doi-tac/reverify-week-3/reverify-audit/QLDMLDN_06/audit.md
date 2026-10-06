# Audit — QLDMLDN_06 (row 142) — Verdict: BA confirm

**Cổng 1 — Bằng chứng đối tác:** `partner-evidence/QLDMLDN_06.jpg` (đã mở full-res).
- URL đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/LOAI_DOANH_NGHIEP` (env khác env được giao).
- Frame lỗi: form "Thêm mới danh mục" tab Loại doanh nghiệp — có trường **"Danh mục cha"** (tùy chọn) + `* Tiêu chí doanh thu` (dấu * đỏ = bắt buộc).

**Cổng 2 — Bug đối tác phản ánh:** (1) "Danh mục cha" thừa; (2) "Tiêu chí doanh thu" bị đánh bắt buộc (SRS: không bắt buộc).

**Cổng 3 — Đối chiếu SRS vs web:**
| SRS yêu cầu | Web hiện tại (21/07) | Kết luận |
|---|---|---|
| TPL-DM-CRUD Inputs (dòng 77-83): 5 trường, KHÔNG có "Danh mục cha" | Form có "Danh mục cha" (tùy chọn, không chặn lưu) | Thừa vs SRS → BA confirm |
| FR-VIII-07 dòng 402: `tieu_chi_doanh_thu` = N (không bắt buộc) | Không có dấu *, POST lưu thành công khi để trống | Đúng SRS → không tái hiện |

**Artifact real-data:** `web-them-moi-form.png` (form + Danh mục cha), `web-sau-luu-doanh-thu-trong.png` (record QTHTB2LDN0721 lưu OK với Doanh thu trống — 1 POST `/api/v1/danh-muc` → toast "Thêm mới thành công").

**Verdict:** `BA confirm` (Danh mục cha cần BA chốt đặc tả; Doanh thu không còn là lỗi). Chi tiết: `../../ba-confirm/qtht/ba-confirmation-needed-qtht-batch2.md` Cụm 1 + Ghi chú.
