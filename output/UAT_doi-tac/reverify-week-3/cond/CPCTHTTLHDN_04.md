# Bảng đối chiếu điều kiện — CPCTHTTLHDN_04

Loại bug: **hiển thị phụ thuộc dữ liệu + tranh chấp thành phần biểu đồ** → điền bảng, 0 GAP. (Verdict = BA confirm: SRS "Grouped bar" không định nghĩa series; "trục tung toàn bộ 0" KHÔNG tái hiện đúng.)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc** | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Chi phí theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Chi phí theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chi phí chi trả) | Nhiều loại hình (Nhỏ/Siêu nhỏ/Vừa) có số liệu tiền chục-trăm triệu | Env có 1 hồ sơ chi phí (Siêu nhỏ 8.000.000 ₫, Trần 30M, Chênh lệch -22M) → đủ render chart + bảng | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data → khu vực kết quả render. Cả 2 env đều hiện biểu đồ Grouped bar plot 6 metric (Chênh lệch / Mức hỗ trợ % / Số hồ sơ / Trần / hồ sơ / Trần chi phí / Tổng chi phí) nhóm theo loại hình — actual về **thành phần biểu đồ** trùng khớp giữa 2 env.

**Đo lường trực tiếp (env test), đối chiếu 2 ý đối tác báo:**

1. **"Biểu đồ cột theo nhiều nhóm mà tài liệu không yêu cầu (Chênh lệch, Số hồ sơ, Trần/hồ sơ, Trần chi phí, Tổng chi phí)"** — TÁI HIỆN ĐÚNG. Legend chart có đủ 6 series: `Chênh lệch · Mức hỗ trợ (%) · Số hồ sơ · Trần / hồ sơ · Trần chi phí · Tổng chi phí`. Đối tác kỳ vọng "nhóm theo loại hình và mức hỗ trợ" (1 chiều mức hỗ trợ), app nhóm theo loại hình với 6 metric số làm series.
2. **"Số liệu ở trục tung hiển thị toàn bộ giá trị 0"** — KHÔNG tái hiện đúng theo nghĩa đen. Trên chart env test (nhóm "Siêu nhỏ"): bar **Tổng chi phí ≈ 8M (xanh lá, dương)**, **Trần/hồ sơ ≈ 30M (đỏ, dương cao)**, **Trần chi phí ≈ 30M (tím, dương cao)**, **Chênh lệch ≈ -22M (teal, âm)** — CÓ giá trị, KHÔNG phải 0. Chỉ **Số hồ sơ (=1)** và **Mức hỗ trợ % (=100)** hiện ~0/vô hình vì bị vẽ chung trục tung scale tiền (hàng chục triệu) → giá trị 1 và 100 quá nhỏ so với scale. Ảnh đối tác cũng cho thấy tooltip "Nhỏ" có Chênh lệch -211.843.371đ / Số hồ sơ 11 / Trần chi phí 330M → tự phủ định "toàn bộ 0".

**Verdict:** BA confirm — SRS Mapping UC141 (`srs-fr-11-bao-cao.md:1077`) chỉ ghi "Grouped bar" + bộ lọc "Loại DN", KHÔNG quy định series là "mức hỗ trợ" (kỳ vọng đối tác) và KHÔNG cấm nhóm 6 metric (app). Điểm cần BA chốt: thành phần series của biểu đồ + có nên tách trục phụ cho Số hồ sơ/Mức hỗ trợ để đọc được không.

Chi tiết đối chiếu SRS + câu hỏi BA: xem [`../reverify-audit/CPCTHTTLHDN_04/audit.md`](../reverify-audit/CPCTHTTLHDN_04/audit.md) và [`../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`](../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md).
