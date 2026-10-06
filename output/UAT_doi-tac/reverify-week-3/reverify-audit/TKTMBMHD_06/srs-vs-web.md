# Audit — TKTMBMHD_06 (Cổng 3: SRS vs Web)

**Verdict:** Open (bug tĩnh — wording thông báo empty-state, không phụ thuộc role/state/data)

## Cổng 1 — evidence đối tác
- `partner-evidence/TKTMBMHD_06.jpg`. Đối tác báo KQ thực: "Hệ thống hiển thị thông báo không giống với thiết kế". KQ mong đợi: "Không tìm thấy thư mục phù hợp".

## Cổng 2 — hiểu bug
- Đối tác phản ánh: thông báo màn tìm-0-kết-quả không đúng thiết kế.
- Bước tái hiện: login CB_NV_TW → thu-muc → tìm "zzzqa123khongtontai" → 0 kết quả.

## Cổng 3 — SRS vs Web

| Tiêu chí | SRS yêu cầu (dẫn line) | Thực tế web | Đủ/Thiếu |
|---|---|---|---|
| Thông báo khi tìm 0 kết quả | "Không tìm thấy thư mục phù hợp" — FR-VII-02 §Error Handling E2 `srs-fr-09:199` (INF-TM-TK-01) | Hiển thị **"Trống"** (empty description AntD mặc định) | ❌ SAI |

## Kết luận
- SRS quy định message CỤ THỂ (INF-TM-TK-01) → app hiển thị "Trống" ≠ → **Open** (describe-not-prescribe: SRS quy định nội dung thông báo, app phải hiển thị đúng thông báo đó).
- Artifact: `bug-reports/image/BUG-TKTMBMHD_06.png` (full-res, role CB_NV_TW, "Trống").
