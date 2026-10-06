# Bảng đối chiếu điều kiện — VVTLV_05 (row 243) — Xuất Excel BC Vụ việc theo lĩnh vực

**Verdict:** Reject — lỗi "Không thể tạo file xuất" (ERR-RPT-04) KHÔNG tái hiện; hệ thống xuất file .xlsx thành công, nội dung đúng chuẩn TT17.

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res VVTLV_05.jpg) | Mình test (21/07/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Quản trị viên (QTHT) — góc phải màn hình | `cbnv_tw_01` (CB Nghiệp vụ TW — vai trò chuẩn ra verdict, có quyền xem + xuất BC). Xuất file là chức năng dùng chung; xuất thành công với vai trò nghiệp vụ đã bao phủ. QTHT quyền rộng hơn nên không thể là lý do đối tác lỗi mà mình pass | Không |
| Loại báo cáo | BC Vụ việc theo lĩnh vực | BC Vụ việc theo lĩnh vực | Không |
| Kỳ + khoảng thời gian | Năm — 01/01/2026 → 31/12/2026 | Năm — 01/01/2026 → 31/12/2026 | Không |
| Đơn vị (phạm vi) | Toàn quốc | Toàn quốc | Không |
| Dữ liệu tiền đề (phải có data mới bật nút Xuất) | Có data — đã Xem báo cáo ra biểu đồ | Có data — Thuế 1 + Thương mại 16 (Tổng 17), đã Xem báo cáo ra kết quả trước khi Xuất | Không |
| Thao tác | Xuất Excel (.xlsx) | Xuất Excel (.xlsx) | Không |

**0 GAP.** Đối tác báo lỗi cụ thể (ERR-RPT-04 khi Xuất Excel) — verify đúng điều kiện, lỗi KHÔNG tái hiện: `POST /api/v1/bao-cao/export` (formatXuat=XLSX, reqid=96) trả **200** + `content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` + `content-disposition: attachment; filename="bao-cao-vu-viec-theo-linh-vuc-2026-07-21.xlsx"`. Toast quan sát = "Đang tạo file..." (SRS item 14), KHÔNG phải ERR-RPT-04.

**Kiểm nội dung file (openpyxl):** header TT17 ĐỦ 4/4 — R1 "BC Vụ việc theo lĩnh vực" · R2 "Kỳ báo cáo: Năm (từ 01/01/2026 đến 31/12/2026)" · R3 "Đơn vị: Toàn quốc" · R4 "Ngày tạo: 21/07/2026" · số liệu khớp màn hình (Thuế 1, Thương mại 16). File gốc: `reverify-audit/_export-check/VVTLV_05.xlsx`.

**Lưu ý env:** đối tác test trên `htpldn-uat.ospgroup.vn`; QA verify trên env được giao `18.143.165.120.nip.io`. Lỗi không tái hiện trên env QA → khả năng lỗi transient/đã fix ở env đối tác → đề nghị đối tác kiểm tra lại.
