# Bảng đối chiếu điều kiện — CPCTHTTLHDN_03

Loại bug: **hiển thị phụ thuộc dữ liệu** (thẻ Chỉ số tổng hợp chỉ hiện khi có ≥1 hồ sơ chi phí) → điền bảng, 0 GAP. (Verdict = BA confirm: actual không tranh chấp, tranh chấp đặc tả.)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc**, đúng vai trò verdict | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Chi phí theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Chi phí theo loại hình DN", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chi phí chi trả) | Tổng hồ sơ 25, Tổng chi phí 226.308.268 (nhiều loại hình) | Env có 1 hồ sơ chi phí (Siêu nhỏ 8.000.000 ₫) → đủ để KPI + bảng render | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data → khu vực kết quả render. Cả 2 env đều hiện 2 thẻ Chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí) — actual trùng khớp, không tranh chấp. Điểm cần BA quyết: SRS §Output FR-IX-18 có yêu cầu thẻ Chỉ số tổng hợp này không.

**Đo lường trực tiếp (env test):**
- UI hiển thị 2 thẻ KPI: "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000"; chart Grouped bar 6 metric; bảng "Quy mô DN / Số hồ sơ / Tổng chi phí / Mức hỗ trợ (%) / Trần/hồ sơ / Trần chi phí / Chênh lệch".
- API `GET /api/v1/bao-cao/chi-phi-theo-loai-dn` (200): trả `tongHoSo:1` + `tongChiPhi:8000000` ở top-level (ngoài `data[]` theo loại hình) → aggregate do BE chủ đích tính.

Chi tiết đối chiếu SRS + câu hỏi BA: xem [`../reverify-audit/CPCTHTTLHDN_03/audit.md`](../reverify-audit/CPCTHTTLHDN_03/audit.md) và [`../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`](../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md).
