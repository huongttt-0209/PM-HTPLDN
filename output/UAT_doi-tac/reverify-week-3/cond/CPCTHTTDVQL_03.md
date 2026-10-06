# Bảng đối chiếu điều kiện — CPCTHTTDVQL_03

Loại bug: **hiển thị phụ thuộc dữ liệu** (thẻ Chỉ số tổng hợp chỉ hiện khi kỳ/đơn vị có ≥1 hồ sơ chi phí) → điền bảng, chỉ kết luận khi 0 GAP. (Verdict = BA confirm: actual không tranh chấp — cả 2 env đều hiện KPI; tranh chấp là đặc tả.)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc**, đúng vai trò verdict | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Chi phí theo đơn vị", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Chi phí theo đơn vị", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chi phí chi trả) | Đối tác có nhiều đơn vị chi phí (Tổng hồ sơ 25, Tổng chi phí 226.308.268) | Env có 1 hồ sơ chi phí (Cục Bổ trợ 8.000.000 ₫) → đủ để KPI + bảng render | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data chi phí → khu vực kết quả render. Cả 2 env đều hiển thị 2 thẻ Chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí) — actual trùng khớp, không tranh chấp. Điểm cần BA quyết: SRS §Output FR-IX-16 có yêu cầu thẻ Chỉ số tổng hợp này không.

**Đo lường trực tiếp (env test):**
- UI hiển thị 2 thẻ KPI: "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000"; chart Bar theo đơn vị; bảng "Đơn vị / Số hồ sơ / Tổng chi phí / TB chi phí".
- API `GET /api/v1/bao-cao/chi-phi-theo-don-vi` (200): trả `tongHoSo:1` + `tongChiPhi:8000000` ở top-level (ngoài `rows[]` theo đơn vị) + `chartType:"BAR_CROSS_TAB"` → aggregate do BE chủ đích tính, không phải FE bịa.

Chi tiết đối chiếu SRS + câu hỏi BA: xem [`../reverify-audit/CPCTHTTDVQL_03/audit.md`](../reverify-audit/CPCTHTTDVQL_03/audit.md) và [`../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`](../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md).
