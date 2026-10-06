# Condition table — BUG-EM-HDD-002 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Đúng vai trò/trạng thái | CBPD từ chối hồ sơ `CHO_PHE_DUYET` | `cbpd_tw_01`, hồ sơ `HD-20260824-003` ở Chờ phê duyệt | Không |
| Giới hạn trường | Tối đa 1000 ký tự | DOM `maxlength = 1000`; UI khởi tạo `0 / 1000` | Không |
| Nhập trên 500 | Không được cắt ở 500 | Nhập được 574 ký tự; DOM `value.length = 574` | Không |
| Bộ đếm | Phản ánh đúng độ dài | Hiển thị `574 / 1000` | Không |
| Không đổi nghiệp vụ | Chỉ kiểm giới hạn, không từ chối thật | Đã hủy dialog, hồ sơ giữ nguyên | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — trường Lý do từ chối cho phép nhập tới 1000 ký tự, không còn bị cắt ở 500.
