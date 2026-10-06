# Bảng đối chiếu điều kiện — QLNDTVVCG_07 (row 280) — REVERIFY sau dev fix

**Kết luận:** Pass — Sau khi chọn Doanh nghiệp + Chuyên gia trên form Thêm TVCS, hệ thống **đã hiển thị đủ 2 panel thông tin đi kèm**: DN → Mã số thuế / Địa chỉ / Người đại diện; CG → Chuyên môn / Số điện thoại / Email. Đúng "KQ mong đợi" của bug gốc.

- **Mã TC:** QLNDTVVCG_07 (row 280) · **Màn:** SCR-X1-02 form Thêm (`/tv-chuyen-sau/tao-moi`).
- **Loại bug:** hiển thị-sau-khi-chọn (phụ thuộc **input/data**: phải chọn DN + CG) → lập bảng đối chiếu.

## Bảng đối chiếu điều kiện (re-test đúng điều kiện bug gốc)

| Điều kiện có thể đổi kết quả | Bug gốc (Pass-bug-report-tvcs-batchB.md) | Mình test (cbnv_tw_01 / CB_NV_TW, BTP·TW, 23/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW (cbnv_tw_02), đơn vị BTP·TW | CB_NV_TW (cbnv_tw_01), đơn vị BTP·TW — cùng role + cùng đơn vị | Không |
| Màn hình | Form Thêm yêu cầu TVCS `/tv-chuyen-sau/tao-moi` (SCR-X1-02) | Form Thêm yêu cầu TVCS `/tv-chuyen-sau/tao-moi` (SCR-X1-02) | Không |
| Input: chọn DN | Công ty TNHH Seed Publishable | DN-SEED-0001 — Công ty TNHH Seed Publishable | Không |
| Input: chọn CG | QA TVV Seed28 Active | TVV-BTP-TW-0002 — QA TVV Seed28 Active | Không |
| Kết quả render sau chọn | KHÔNG hiện panel (đo DOM: showsMST/diaChi/nguoiDaiDien/chuyenMon = false) | **CÓ hiện đủ** panel DN + CG (đo DOM: tất cả label + value = true) | Không |

**0 GAP** — re-test đúng vai trò/màn/DN/CG như bug gốc; chỉ khác instance tài khoản (`_01` vs `_02`, cùng role CB_NV_TW + cùng đơn vị BTP·TW nên scope/state không đổi).

**Artifact real-data (chạy trên form thật, đo bằng snapshot a11y + `evaluate_script` đọc DOM hiển thị):**
- Sau chọn DN: panel hiện **Mã số thuế: 0100000001** · **Địa chỉ: So 10 Pho Test, Quan Ba Dinh, Ha Noi** · **Người đại diện: Nguyen Van Seed** — cả 3 label + value đều có trong `document.body.innerText`.
- Sau chọn CG: panel hiện **Chuyên môn: —** (CG này không có dữ liệu chuyên môn — mức data, label vẫn render đúng) · **Số điện thoại: 0912280028** · **Email: qa.tvvseed28@htpldn-uat.local**.
- `evaluate_script` trả `dn_panel` + `cg_panel` = tất cả `true`. So bug gốc đo `false` toàn bộ → nay render đủ.
- Ảnh: `bug-reports/tvcs/image/bug-qlndtvvcg_07-retest-pass-dn-cg-info-shown.png`.

## Kết luận

- SRS SCR-X1-02 §Thành phần màn hình yêu cầu: chọn DN → hiện MST, địa chỉ, người đại diện; chọn CG → hiện chuyên môn, SĐT, email.
- Web hiện tại **đã hiển thị đủ** các thông tin này sau khi chọn DN + CG → khớp KQ mong đợi → **Pass (Closed)**.
