# Bảng đối chiếu điều kiện — CPHTCT_06 (row 250) — Xuất Excel BC Chi phí chi trả hỗ trợ

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng chuẩn TT17.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res CPHTCT_06.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict). Xuất thành công với vai trò nghiệp vụ đã bao phủ; QTHT quyền rộng hơn nên không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Chi phí chi trả hỗ trợ | BC Chi phí chi trả hỗ trợ | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — KPI Tổng chi phí 226.308.268đ / 25 hồ sơ (data env đối tác) | Có data — Tổng chi phí 8.000.000đ / 1 hồ sơ (env QA), đã Xem báo cáo trước khi Xuất. Số lượng data khác env nhưng đều CÓ data → nút Xuất bật, không đổi verdict export | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** `POST /api/v1/bao-cao/export` (formatXuat=XLSX, reqid=126) trả **200** + `content-disposition: attachment; filename="bao-cao-chi-phi-chi-tra-2026-07-21.xlsx"`. Toast = "Đang tạo file...", KHÔNG phải ERR-RPT-04.

**Kiểm nội dung file (openpyxl):** header TT17 ĐỦ 4/4 (tiêu đề + Kỳ + Đơn vị: Toàn quốc + Ngày tạo: 21/07/2026) + số liệu khớp màn hình (Cục Bổ trợ tư pháp: 1 hồ sơ, 8.000.000₫ tổng, 8.000.000₫ TB). File gốc: `reverify-audit/_export-check/CPHTCT_06.xlsx`.

**Lưu ý env:** đối tác test `htpldn-uat.ospgroup.vn` (data 25 HS/226 triệu); QA verify `18.143.165.120.nip.io` (1 HS/8 triệu). Khác data nhưng đều CÓ data; lỗi tạo file không tái hiện → đề nghị đối tác kiểm tra lại.
