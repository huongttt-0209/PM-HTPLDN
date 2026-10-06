# Condition table — BUG-EM-DT-002 (R3)

| Điều kiện | Điều kiện gốc | Thực tế reverify 2026-08-25 | GAP |
|---|---|---|---|
| Trạng thái đầu | CTĐT `TU_CHOI` | `CTDT-BTP-TW-2026-0012` ở `TU_CHOI` | Không |
| Đã sửa sau từ chối | Guard `updated_at > thoi_gian_tu_choi` | Hồ sơ đã có nội dung bổ sung và `ngayCapNhat = 2026-08-22T09:40:05.231Z`, sau mốc từ chối | Không |
| Hành động UI | Có đường gửi lại | Màn chi tiết hiện nút “Gửi phê duyệt lại” | Không |
| Chuyển trạng thái | `TU_CHOI → CHO_DUYET` | Thao tác UI thành công lúc 10:37; lịch sử ghi “Từ chối → Chờ duyệt” | Không |
| Thông báo CBPD | Phát thông báo/email sau gửi lại | MailHog CBPD tăng 50→51; thư CTĐT `0012` đến `2026-08-25T03:37:33.426Z` | Không |
| Môi trường | DEV | `https://18.143.165.120.nip.io`, UI v1.0.16 | Không |

**Kết luận:** PASS — CTĐT bị từ chối đã có thể gửi phê duyệt lại và chuyển đúng sang Chờ duyệt.
