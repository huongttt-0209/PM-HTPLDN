# Audit — SLCTHT_03 (BC Số lượng CT hỗ trợ — Chỉ số tổng hợp) — ✅ Open (confirmed)

**Verdict:** **Open** — khu Chỉ số tổng hợp chỉ hiện "Tổng chương trình", thiếu 2 chỉ số "Đang thực hiện" + "Hoàn thành" (vi phạm §Output FR-IX-20 dòng 908-909, cả 3 điều kiện "Luôn").

> **Cập nhật:** Ban đầu định mark BLOCKED (env test tongCt=0). Nhưng **seed được qua BE API** (`/api/v1/chuong-trinh-htpls`, plural) — đã seed 1 CT DANG_THUC_HIEN + 1 HOAN_THANH rồi verify qua UI role cbnv_tw → tái hiện đúng → **Open**. (Lưu ý: bug này ở màn **Báo cáo thống kê**, độc lập với màn quản lý CT `/ct-htpldn` — màn quản lý đầu session từng 404 nhưng re-verify cuối session đã chạy OK, không phải bug.)

## Evidence
- Đối tác: `partner-evidence/SLCTHT_03.jpg` — chỉ 1 thẻ "Tổng chương trình = 5", thiếu 2 thẻ trạng thái.
- Env test: `../../bug-reports/bctk/image/BUG-SLCTHT-web-render.png` — role `cbnv_tw`, Toàn quốc, sau seed: chỉ 1 thẻ "Tổng chương trình = 4", KHÔNG có thẻ Đang thực hiện / Hoàn thành. Tái hiện đúng.

## Seed qua API (phục vụ render, verdict lấy từ UI)
- `POST /api/v1/chuong-trinh-htpls` tạo CT (DU_THAO) → `/submit` (CHO_PHE_DUYET) → `/approve` bằng **cbpd_tw** (người tạo không được duyệt chính mình, ERR-XI-04-04) → `/publish` + `/activate` bằng admin (creator; cbpd không có quyền publish) → DANG_THUC_HIEN; thêm `/complete` → HOAN_THANH. Mỗi transition cần field `version` (optimistic lock).
- Report API sau seed: `tongCt:4, data:[{DA_DUYET:2},{DANG_THUC_HIEN:1},{HOAN_THANH:1}], chartType:BAR`.

## Đối chiếu SRS
- `srs-fr-11-bao-cao.md:907-909` — `tong_ct` + `dang_thuc_hien` + `hoan_thanh`, cả 3 điều kiện **"Luôn"**. App chỉ render `tong_ct` → thiếu 2 → **Open**.
- Chi tiết bug: `../../bug-reports/bctk/Pass-bug-report-bctk-batch3.md` §BUG-SLCTHT_03.
