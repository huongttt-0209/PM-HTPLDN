# Bảng đối chiếu điều kiện — CPCTHTTTG_03

Loại bug: **hiển thị phụ thuộc dữ liệu (biểu đồ đường)** → điền bảng, 0 GAP. (Verdict = BA confirm: claim "trục tung toàn bộ 0" KHÔNG tái hiện đúng — điểm Tổng chi phí khác 0; chỉ Số hồ sơ hiện ~0 do trộn scale, giống CPCTHTTLHDN_04.)

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / phạm vi dữ liệu | Header ảnh "Quản trị viên · QTHT" (admin), Đơn vị = **Toàn quốc** | `cbnv_tw` (CB Nghiệp vụ - Trung ương) — phạm vi **Toàn quốc** | Không |
| Loại báo cáo + kỳ + đơn vị (filter) | "BC Chi phí theo thời gian", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Chọn đúng "BC Chi phí theo thời gian", Kỳ Năm 01/01/2026 → 31/12/2026, Toàn quốc | Không |
| Dữ liệu tiền đề (có chi phí chi trả) | Tổng chi phí toàn kỳ 226.308.268, Tổng hồ sơ 25 (1 kỳ = 2026) | Env có Tổng chi phí 8.000.000, Tổng hồ sơ 1 (1 kỳ = 2026) → đủ để chart + bảng render | Không |

**Kết luận: 0 GAP.** Đúng phạm vi Toàn quốc + đúng filter + có data → khu vực kết quả render. Cả 2 env đều hiện biểu đồ Line 2 series (Số hồ sơ + Tổng chi phí), 1 điểm kỳ "2026".

**Đo lường trực tiếp (env test), đối chiếu ý đối tác báo:**

- Đối tác báo: **"Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0"** — KHÔNG tái hiện đúng theo nghĩa đen.
- Trên chart env test: trục tung auto-scale `0 / 2.000.000 / 4.000.000 / 6.000.000 / 8.000.000`. Điểm **Tổng chi phí (xanh lá) nằm ở đỉnh ≈ 8.000.000** (khác 0 rõ ràng). Điểm **Số hồ sơ (xanh dương, = 1) nằm ở đáy ≈ 0** vì được vẽ chung trục tung scale tiền (giá trị 1 quá nhỏ so với 8 triệu).
- Ảnh đối tác cũng thể hiện y hệt: điểm **Tổng chi phí (xanh lá) ở đỉnh (~226M)**, điểm **Số hồ sơ (=25) ở đáy 0**. → chính ảnh đối tác tự phủ định "toàn bộ 0" (series tiền có giá trị cao).
- API `GET /api/v1/bao-cao/chi-phi-theo-thoi-gian` (200): `tongChiPhiToanKy:8000000, tongHoSoToanKy:1, data:[{kyLabel:"2026", soHoSo:1, tongChiPhi:8000000}], chartType:"LINE"` → BE trả số khác 0, data không lỗi.

**Verdict:** BA confirm — cùng bản chất với `CPCTHTTLHDN_04`: biểu đồ trộn 2 metric khác đơn vị (Số hồ sơ = đếm, Tổng chi phí = tiền) trên cùng 1 trục tung → series đếm hiện ~0. SRS Mapping UC142 (`srs-fr-11-bao-cao.md:1078`) chỉ ghi "Line chart trend"; §Output FR-IX-19 (`:869`) đưa cả `so_ho_so` + `tong_chi_phi` vào `trend_data[]` nhưng KHÔNG quy định tách trục. Điểm cần BA chốt: có tách trục phụ cho Số hồ sơ để đọc được không.

Chi tiết đối chiếu SRS + câu hỏi BA: xem [`../reverify-audit/CPCTHTTTG_03/audit.md`](../reverify-audit/CPCTHTTTG_03/audit.md) và [`../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md`](../ba-confirm/bctk/ba-confirmation-needed-bctk-batch3.md).
