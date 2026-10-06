# BA confirmation needed — BCTK Batch 3 (DISPLAY: VV theo chiều + Chi phí + Số lượng CT) — 2026-07-21

> **File này để làm gì:** gom các testcase batch 3 mà QA verify xong nhưng cần BA phản hồi đối tác (chủ yếu: đối tác kỳ vọng "không có / có" một thành phần hiển thị mà SRS §Output không quy định rõ). Bug có SRS reference rõ ràng → đã log vào `../../bug-reports/bctk/Pass-bug-report-bctk-batch3.md`.

> **Quy tắc citation:** SRS v3.5 = `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-11-bao-cao.md`. Mọi khẳng định dẫn số dòng thực đã mở file kiểm.

---

## CPCTHTTDVQL_03 — Đối tác cho rằng báo cáo "Chi phí theo đơn vị" KHÔNG được có thẻ Chỉ số tổng hợp, nhưng app hiện 2 thẻ (Tổng hồ sơ + Tổng chi phí)

**Bối cảnh testcase**

- Dòng Excel: 252, mã TC `CPCTHTTDVQL_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo đơn vị" (UC139 / FR-IX-16), kiểm tra phần "Chỉ số tổng hợp".
- Expected trong file UAT: "Không có chỉ số tổng hợp riêng".
- Actual đối tác ghi: "Hệ thống hiển thị chỉ số tổng hợp" (2 thẻ: Tổng hồ sơ = 25, Tổng chi phí = 226.308.268).

**Đối chiếu SRS v3.5**

- FR-IX-16 §Output đặc thù chỉ liệt kê các trường **theo đơn vị** (cross-tab): `don_vi_id`, `ten_don_vi`, `tong_chi_phi`, `so_ho_so`, `trung_binh` — KHÔNG liệt kê thẻ chỉ số tổng hợp (aggregate Tổng hồ sơ / Tổng chi phí toàn quốc).
- Ngược lại, FR-IX-15 (BC Chi phí chi trả hỗ trợ) §Output có aggregate `tong_chi_phi`, `tong_ho_so`, `trung_binh_ho_so` là trường "Luôn" — tức thiết kế đặt phần chỉ số tổng hợp ở FR-IX-15, không ở FR-IX-16.
- SCR-IX-01 §Thành phần màn hình (dòng 1039–1054) KHÔNG có component "Chỉ số tổng hợp / KPI card" riêng — chỉ có biểu đồ (item 10) + bảng dữ liệu có hàng tổng cộng (item 11).
- SRS **không cấm rõ ràng** thẻ chỉ số tổng hợp ở FR-IX-16; chỉ là §Output không liệt kê. Aggregate hiển thị (Tổng hồ sơ, Tổng chi phí) là số đúng, suy ra trực tiếp từ bảng theo đơn vị.

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:752-758` (FR-IX-16 §Output — chỉ có trường theo đơn vị, không có aggregate KPI)
- `srs-v3.5/srs-fr-11-bao-cao.md:718-724` (FR-IX-15 §Output — aggregate tong_chi_phi/tong_ho_so/trung_binh ở đây)
- `srs-v3.5/srs-fr-11-bao-cao.md:1039-1054` (SCR-IX-01 thành phần màn hình — không có component KPI card)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (CB Nghiệp vụ - Trung ương, phạm vi Toàn quốc).
- Mở URL `.../bao-cao?loai=chi-phi-theo-don-vi&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- UI hiển thị 2 thẻ Chỉ số tổng hợp: "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000" (env test ít data hơn đối tác) → **tái hiện đúng** hiện tượng đối tác báo.
- Chart Bar theo đơn vị + bảng "Đơn vị / Số hồ sơ / Tổng chi phí / TB chi phí" — đúng §Output FR-IX-16.
- Network: `GET /api/v1/bao-cao/chi-phi-theo-don-vi` trả `tongHoSo` + `tongChiPhi` ở top-level (BE chủ đích tính aggregate) → thẻ KPI không phải FE tự bịa.
- Evidence: `../../reverify-audit/CPCTHTTDVQL_03/web-kpi.png`

**Kết luận QA**

- `CPCTHTTDVQL_03`: actual đối tác **đúng thực tế** (app có hiển thị thẻ chỉ số tổng hợp), nhưng đây là bất đồng về **đặc tả** — SRS §Output FR-IX-16 không liệt kê thẻ chỉ số tổng hợp, cũng không cấm.
- Thẻ KPI hiển thị số liệu đúng (aggregate của bảng theo đơn vị, do BE tính). Không phải lỗi dữ liệu.
- Chưa đủ căn cứ Reject (đối tác quan sát đúng) hay Open (SRS không quy định rõ cấm).

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: báo cáo "Chi phí theo đơn vị" (FR-IX-16) **có được phép** hiển thị thẻ chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí toàn phạm vi) không?

- Nếu BA đồng ý thẻ tổng hợp là hợp lệ/hữu ích → cập nhật expected của `CPCTHTTDVQL_03` (bỏ yêu cầu "không có chỉ số tổng hợp"); bổ sung §Output FR-IX-16 cho khớp implementation. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn giữ đúng thiết kế "FR-IX-16 không có KPI riêng" (chỉ FR-IX-15 mới có) → gửi Dev FE/BE bỏ thẻ chỉ số tổng hợp khỏi báo cáo này. Verdict: `Vẫn lỗi — owner: Dev FE/BE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

## CPCTHTTLHDN_03 — Đối tác cho rằng báo cáo "Chi phí theo loại hình DN" KHÔNG được có thẻ Chỉ số tổng hợp, nhưng app hiện 2 thẻ (Tổng hồ sơ + Tổng chi phí)

**Bối cảnh testcase**

- Dòng Excel: 255, mã TC `CPCTHTTLHDN_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo loại hình DN" (UC141 / FR-IX-18), kiểm tra phần "Chỉ số tổng hợp".
- Expected trong file UAT: "Không có chỉ số tổng hợp riêng".
- Actual đối tác ghi: "Hệ thống hiển thị chỉ số tổng hợp" (2 thẻ: Tổng hồ sơ = 25, Tổng chi phí = 226.308.268).

**Đối chiếu SRS v3.5**

- FR-IX-18 §Output đặc thù chỉ liệt kê các trường **theo loại hình DN**: `loai_dn`, `ten_loai_dn`, `muc_ho_tro`, `so_ho_so`, `tong_chi_phi`, `tran_chi_phi`, `chenh_lech` — KHÔNG liệt kê thẻ chỉ số tổng hợp (aggregate Tổng hồ sơ / Tổng chi phí).
- Aggregate KPI (Tổng hồ sơ / Tổng chi phí) thuộc §Output của FR-IX-15 (BC Chi phí chi trả hỗ trợ), không phải FR-IX-18.
- SCR-IX-01 §Thành phần màn hình (dòng 1039–1054) không có component "Chỉ số tổng hợp / KPI card" riêng.
- SRS **không cấm rõ ràng** thẻ chỉ số tổng hợp ở FR-IX-18. Số liệu 2 thẻ đúng (aggregate của bảng theo loại hình, do BE tính).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:831-839` (FR-IX-18 §Output — chỉ có trường theo loại hình, không có aggregate KPI)
- `srs-v3.5/srs-fr-11-bao-cao.md:718-724` (FR-IX-15 §Output — aggregate ở đây)
- `srs-v3.5/srs-fr-11-bao-cao.md:1039-1054` (SCR-IX-01 thành phần màn hình — không có component KPI card)

**Kết quả verify UI hiện tại**

- Verify lại ngày 21/07/2026 qua Chrome DevTools MCP, tài khoản UAT `cbnv_tw` (Toàn quốc).
- Mở URL `.../bao-cao?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- UI hiển thị 2 thẻ Chỉ số tổng hợp "Tổng hồ sơ = 1", "Tổng chi phí = 8,000,000" (env test ít data hơn) → **tái hiện đúng** hiện tượng đối tác báo.
- Chart Grouped bar 6 metric + bảng "Quy mô DN / Số hồ sơ / Tổng chi phí / Mức hỗ trợ (%) / Trần/hồ sơ / Trần chi phí / Chênh lệch" — đúng §Output FR-IX-18.
- Network: `GET /api/v1/bao-cao/chi-phi-theo-loai-dn` trả `tongHoSo` + `tongChiPhi` ở top-level → thẻ KPI do BE cấp.
- Evidence: `../../reverify-audit/CPCTHTTLHDN_03/web-kpi.png`

**Kết luận QA**

- `CPCTHTTLHDN_03`: actual đối tác **đúng thực tế** (app có thẻ chỉ số tổng hợp), bất đồng về **đặc tả** — SRS §Output FR-IX-18 không liệt kê thẻ này, cũng không cấm.
- Cùng bản chất với `CPCTHTTDVQL_03` (cùng cụm "Chi phí — thẻ chỉ số tổng hợp") → nên chốt chung 1 hướng.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt: các báo cáo Chi phí (FR-IX-16 / FR-IX-18) **có được phép** hiển thị thẻ chỉ số tổng hợp (Tổng hồ sơ + Tổng chi phí) không?

- Nếu đồng ý → cập nhật expected `CPCTHTTLHDN_03` + bổ sung §Output. Verdict: `Không phải bug theo SRS`.
- Nếu giữ thiết kế "chỉ FR-IX-15 có KPI tổng hợp" → gửi Dev bỏ thẻ. Verdict: `Vẫn lỗi — owner: Dev FE/BE`.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

## CPCTHTTLHDN_04 — Đối tác cho rằng biểu đồ "Chi phí theo loại hình DN" phải nhóm theo loại hình × mức hỗ trợ, nhưng app plot 6 metric số; đối tác còn báo "trục tung toàn bộ 0"

**Bối cảnh testcase**

- Dòng Excel: 256, mã TC `CPCTHTTLHDN_04`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo loại hình DN" (UC141 / FR-IX-18), kiểm tra hiển thị **biểu đồ + bảng tổng hợp**.
- Expected trong file UAT: "Biểu đồ cột nhóm theo loại hình và mức hỗ trợ" + "Bảng tổng hợp: Loại hình, Mức hỗ trợ, Số hồ sơ, Tổng chi phí, Trần chi phí, Chênh lệch".
- Actual đối tác ghi (2 ý): (1) "Biểu đồ cột theo nhiều nhóm mà tài liệu không yêu cầu: Chênh lệch, Số hồ sơ, Trần / hồ sơ, Trần chi phí, Tổng chi phí"; (2) "Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0".

**Đối chiếu SRS v3.5**

- Mapping 23 loại BC (dòng 1077): `UC141 | BC Chi phí theo loại hình DN | Bộ lọc: Loại DN | Biểu đồ: Grouped bar`. SRS **chỉ ghi loại biểu đồ "Grouped bar" + bộ lọc "Loại DN"**, KHÔNG định nghĩa các series của biểu đồ là gì (không nói "nhóm theo mức hỗ trợ" như đối tác kỳ vọng, cũng không nói phải plot 6 metric như app).
- FR-IX-18 §Output (dòng 831-839) mô tả các cột **bảng** (loai_dn, ten_loai_dn, muc_ho_tro, so_ho_so, tong_chi_phi, tran_chi_phi, chenh_lech) — bảng app khớp §Output (thêm cột "Trần / hồ sơ" = tranChiPhiMoiHoSo, ngoài spec nhưng hợp lý). §Output KHÔNG mô tả series biểu đồ.
- SRS không quy định trục tung/thứ nguyên biểu đồ, cũng không yêu cầu tách trục phụ cho metric khác đơn vị.

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1077` (Mapping UC141 — "Grouped bar", bộ lọc "Loại DN"; không định nghĩa series)
- `srs-v3.5/srs-fr-11-bao-cao.md:831-839` (FR-IX-18 §Output — cột bảng, không mô tả biểu đồ)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc), URL `.../bao-cao?loai=chi-phi-theo-loai-dn&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- **Ý (1) — thành phần biểu đồ: TÁI HIỆN ĐÚNG.** Legend chart đủ 6 series: `Chênh lệch · Mức hỗ trợ (%) · Số hồ sơ · Trần / hồ sơ · Trần chi phí · Tổng chi phí`, nhóm theo loại hình DN. Đối tác kỳ vọng "nhóm theo loại hình và mức hỗ trợ" (1 chiều mức hỗ trợ) — app không làm vậy.
- **Ý (2) — "trục tung toàn bộ 0": KHÔNG tái hiện đúng theo nghĩa đen.** Nhóm "Siêu nhỏ" trên chart env test: bar **Tổng chi phí ≈8M (dương)**, **Trần/hồ sơ ≈30M (dương cao)**, **Trần chi phí ≈30M (dương cao)**, **Chênh lệch ≈-22M (âm)** — có giá trị rõ. Chỉ **Số hồ sơ (=1)** và **Mức hỗ trợ % (=100)** hiện ~0/vô hình vì được vẽ chung trục tung scale tiền (hàng chục triệu) → 1 và 100 quá nhỏ. Ảnh chính đối tác cũng có tooltip giá trị khác 0 (Chênh lệch -211M, Số hồ sơ 11...) → tự phủ định "toàn bộ 0".
- Network: `GET /api/v1/bao-cao/chi-phi-theo-loai-dn` (200) trả đủ 6 metric số per loại hình (`soHoSo`, `mucHoTroPhanTram`, `tongChiPhi`, `tranChiPhiMoiHoSo`, `tranChiPhi`, `chenhLech`) → chart plot 6 series là chủ đích, data không lỗi.
- Evidence: `../../reverify-audit/CPCTHTTLHDN_04/web-chart.png`

**Kết luận QA**

- Ý (1): actual đối tác đúng thực tế (chart plot 6 metric), nhưng đây là **bất đồng đặc tả** — SRS "Grouped bar" không định nghĩa series; không có dòng SRS để khẳng định app sai hay đối tác đúng. → không đủ căn cứ Open/Reject.
- Ý (2): claim "toàn bộ 0" **không đúng theo nghĩa đen** — bar tiền có giá trị; chỉ count/% bị nén thành 0 do trộn scale. Đây là **vấn đề legibility/thiết kế biểu đồ** (2 series không đọc được), SRS không quy định → cần design/BA quyết, không phải data bug.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho biểu đồ "Chi phí theo loại hình DN" (FR-IX-18, Grouped bar):

1. **Thành phần series biểu đồ:** giữ nguyên plot 6 metric số (như app), hay đổi sang "nhóm theo loại hình × mức hỗ trợ" (như đối tác kỳ vọng)? SRS Mapping chỉ ghi "Grouped bar" nên cần BA/design chốt.
2. **Xử lý metric khác đơn vị:** Số hồ sơ (đếm) và Mức hỗ trợ (%) đang dùng chung trục tung với tiền → hiện thành ~0, không đọc được. Có nên tách **trục phụ (secondary axis)** hoặc bỏ 2 metric này khỏi biểu đồ (chỉ để trong bảng) không?

- Nếu BA chấp nhận biểu đồ hiện tại → cập nhật expected `CPCTHTTLHDN_04`; làm rõ Mapping/§Output về series. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn theo kỳ vọng đối tác (nhóm theo mức hỗ trợ + tách trục cho count/%) → gửi Dev FE. Verdict: `Vẫn lỗi — owner: Dev FE`.
- Lưu ý riêng: claim "trục tung toàn bộ 0" của đối tác **không chính xác** — chỉ 2 series count/% hiện ~0 do scale, phần tiền vẫn đúng.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

---

## CPCTHTTTG_03 — Đối tác báo biểu đồ "Chi phí theo thời gian" có "trục tung toàn bộ 0"; thực tế điểm Tổng chi phí khác 0, chỉ Số hồ sơ hiện ~0 do trộn scale

**Bối cảnh testcase**

- Dòng Excel: 259, mã TC `CPCTHTTTG_03`.
- Nội dung kiểm tra: Cán bộ nghiệp vụ TW xem báo cáo "BC Chi phí theo thời gian" (UC142 / FR-IX-19), kiểm tra hiển thị **biểu đồ + bảng tổng hợp**.
- Expected trong file UAT: "Biểu đồ đường thể hiện xu hướng chi phí" + "Bảng tổng hợp: Kỳ thời gian, Tổng chi phí, Số hồ sơ".
- Actual đối tác ghi: "Số liệu ở trục tung của biểu đồ hiển thị toàn bộ giá trị 0".

**Đối chiếu SRS v3.5**

- Mapping UC142 (dòng 1078): `BC Chi phí theo thời gian | Biểu đồ: Line chart trend`. SRS chỉ ghi loại biểu đồ, không định nghĩa trục/series.
- FR-IX-19 §Output (dòng 869): `trend_data[] = {ky_label, tong_chi_phi, so_ho_so}` (điều kiện "Luôn"), `chart_type = LINE`. → SRS §Output CÓ đưa cả `so_ho_so` + `tong_chi_phi` vào trend_data nên biểu đồ vẽ 2 series là khớp §Output. SRS **không quy định tách trục** cho metric đếm.
- AC (dòng 874): "12 tháng → line chart 12 điểm trend chi phí". Đối tác chọn Kỳ = Năm → chỉ 1 kỳ (2026) → 1 điểm là đúng filter (không phải lỗi).

**Citation**

- `srs-v3.5/srs-fr-11-bao-cao.md:1078` (Mapping UC142 — "Line chart trend")
- `srs-v3.5/srs-fr-11-bao-cao.md:869` (FR-IX-19 §Output — trend_data gồm cả so_ho_so + tong_chi_phi; không nêu tách trục)

**Kết quả verify UI hiện tại**

- Verify lại 21/07/2026 qua Chrome DevTools MCP, `cbnv_tw` (Toàn quốc), URL `.../bao-cao?loai=chi-phi-theo-thoi-gian&kyBaoCao=NAM&tuNgay=2026-01-01&denNgay=2026-12-31`.
- **"Trục tung toàn bộ 0": KHÔNG tái hiện đúng theo nghĩa đen.** Chart env test: trục tung auto-scale `0 / 2M / 4M / 6M / 8M`; điểm **Tổng chi phí (xanh lá) nằm ở đỉnh ≈8.000.000** (khác 0 rõ), điểm **Số hồ sơ (xanh dương, =1) ở đáy ≈0** vì bị vẽ chung trục tung scale tiền. Ảnh chính đối tác cũng cho thấy điểm Tổng chi phí ở đỉnh (~226M) → tự phủ định "toàn bộ 0".
- Network: `GET /api/v1/bao-cao/chi-phi-theo-thoi-gian` (200) trả `tongChiPhiToanKy:8000000, tongHoSoToanKy:1, data:[{kyLabel:"2026", soHoSo:1, tongChiPhi:8000000}], chartType:"LINE"` → BE trả số khác 0, data không lỗi.
- Evidence: `../../reverify-audit/CPCTHTTTG_03/web-chart.png`

**Kết luận QA**

- Claim "trục tung toàn bộ 0" **sai theo nghĩa đen** — series Tổng chi phí có giá trị, hiển thị ở đỉnh trục. Không phải data bug.
- Đây là **cùng bản chất với `CPCTHTTLHDN_04`**: biểu đồ trộn metric đếm (Số hồ sơ) và metric tiền (Tổng chi phí) trên cùng 1 trục tung → series đếm bị nén thành ~0, không đọc được. SRS không quy định trục phụ → vấn đề legibility/thiết kế, cần BA/design quyết.

**Nội dung đề xuất BA phản hồi đối tác**

Đề nghị BA chốt cho biểu đồ "Chi phí theo thời gian" (FR-IX-19, Line chart):

1. Series "Số hồ sơ" (đếm) dùng chung trục tung với "Tổng chi phí" (tiền) → hiện thành ~0, không đọc được. Có nên **tách trục phụ (secondary axis)** cho Số hồ sơ, hay chỉ vẽ trend chi phí (bỏ Số hồ sơ khỏi biểu đồ, giữ ở bảng) như expected đối tác ("biểu đồ đường thể hiện xu hướng chi phí")?

- Nếu BA chấp nhận biểu đồ hiện tại → cập nhật expected `CPCTHTTTG_03`. Verdict: `Không phải bug theo SRS`.
- Nếu BA muốn tách trục / bỏ Số hồ sơ khỏi biểu đồ → gửi Dev FE. Verdict: `Vẫn lỗi — owner: Dev FE`.
- Lưu ý riêng: claim "trục tung toàn bộ 0" của đối tác **không chính xác** — chỉ Số hồ sơ hiện ~0 do scale; Tổng chi phí đúng.
- Verdict QA đề xuất hiện tại: `Cần BA xác nhận`, chưa gửi Dev tới khi BA chốt.

> **Ghi chú cụm:** 3 case `CPCTHTTLHDN_04` + `CPCTHTTTG_03` (+ liên quan `CPCTHTTLHDN_03`/`CPCTHTTDVQL_03`) đều xoay quanh cùng 1 gốc: biểu đồ báo cáo Chi phí trộn nhiều metric khác đơn vị (tiền / đếm / %) trên 1 trục tung → metric đếm & % hiện ~0. Nên BA chốt CHUNG 1 nguyên tắc trục phụ cho toàn cụm báo cáo Chi phí.
