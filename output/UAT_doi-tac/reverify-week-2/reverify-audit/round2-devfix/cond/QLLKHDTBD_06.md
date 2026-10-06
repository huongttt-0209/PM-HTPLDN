# Bảng đối chiếu điều kiện — QLLKHDTBD_06 (reverify R2 sau dev fix) — REOPEN

| Điều kiện | Bug gốc (bug-report) | Mình test (reverify R2) | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ (cbnv_tw — CB_NV_TW) | cbnv_tw (CB_NV_TW) | Không |
| Thao tác | Tạo mới KH đào tạo, nhập đủ trường bắt buộc (Tên, Năm, Thời gian) | Tạo KH: Tên + Năm 2026 + Thời gian 01/04–30/11/2026, KHÔNG nhập Ngân sách (trường không bắt buộc) | Không |
| Kết quả bug gốc | POST tạo KH trả 500 (ERR-SYS), không tạo được | POST /ke-hoach-dao-taos trả **500** (reqid 186 + 196), toast "Lỗi hệ thống"; khi CÓ Ngân sách → 201 OK | Không |
