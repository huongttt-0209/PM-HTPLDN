# Audit — SLCTHT_04 (BC Số lượng CT hỗ trợ — Biểu đồ + bảng) — ✅ Open (confirmed)

**Verdict:** **Open** — cả 2 biểu đồ (cột + đường) + bảng đều theo TRẠNG THÁI; thiếu chiều đơn vị (cột) + kỳ (đường) + cột bảng theo §Output (vi phạm §Output FR-IX-20 dòng 910-911 + Mapping 1079).

> **Cập nhật:** Ban đầu định mark BLOCKED (env test tongCt=0). Nhưng **seed được qua BE API** (`/api/v1/chuong-trinh-htpls`) — đã seed CT nhiều trạng thái rồi verify qua UI role cbnv_tw → tái hiện đúng → **Open**. (Lưu ý: bug này ở màn **Báo cáo thống kê**, độc lập với màn quản lý CT `/ct-htpldn` — màn quản lý đầu session từng 404 nhưng re-verify cuối session đã chạy OK, không phải bug.)

## Evidence
- Đối tác: `partner-evidence/SLCTHT_04.jpg` — bar + line + bảng đều theo trạng thái; bảng "Trạng thái | Số chương trình".
- Env test: `../../bug-reports/bctk/image/BUG-SLCTHT-web-render.png` — role `cbnv_tw`, sau seed: biểu đồ cột trục hoành = 3 trạng thái; biểu đồ đường trục hoành cũng = 3 trạng thái (không theo kỳ); bảng 2 cột {Trạng thái, Số chương trình} (Đã phê duyệt 2, Đang thực hiện 1, Hoàn thành 1). Tái hiện đúng.

## Seed qua API
- Giống SLCTHT_03: tạo + submit + approve(cbpd_tw) + publish/activate/complete(admin) → có CT ở DA_DUYET/DANG_THUC_HIEN/HOAN_THANH.
- Report API: `data:[{trangThai:DA_DUYET,soCt:2},{DANG_THUC_HIEN,1},{HOAN_THANH,1}], chartType:BAR` — gom theo trạng thái, KHÔNG có `theoDonVi[]`/`theoKy[]`.

## Đối chiếu SRS
- `srs-fr-11-bao-cao.md:910` — `theo_don_vi[]` {don_vi, ten, so_ct, dang_thuc_hien, hoan_thanh} ("Luôn"). `:911` — `theo_ky[]` {ky, so_ct} ("Luôn"). `:1079` Mapping "Bar + Trend" (cột theo đơn vị + đường theo kỳ).
- App vẽ theo trạng thái, bảng thiếu cột đơn vị → sai chiều → **Open**. Lỗi cả BE contract (thiếu chiều đơn vị/kỳ) + FE.
- Chi tiết bug: `../../bug-reports/bctk/Pass-bug-report-bctk-batch3.md` §BUG-SLCTHT_04.
