# Bảng đối chiếu điều kiện — QLHSTVV_03 (re-verify sau dev fix, 2026-07-15)

| Điều kiện | Bug gốc (Bước tái hiện) | Mình test (re-verify 2026-07-15) | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB_NV_TW — `cbnv_tw` | CB_NV_TW — `cbnv_tw`, banner BTP·TW | Không |
| Entity + trạng thái | TVV cùng đơn vị: 1 chưa công khai (TVV-BTP-TW-0002) + 1 đã công khai (TVV-SEED-0001) | TVV-BTP-TW-0002 (Đang hoạt động, Chưa công khai) + TVV-SEED-0001 (Đang hoạt động, đã công khai — có nút "Hủy công khai") | Không |
| Màn hình | Màn Chi tiết TVV → thẻ "Hồ sơ", đếm/đối chiếu các nhóm | Đúng màn, thẻ "Hồ sơ" | Không |
| Thao tác kiểm | Kiểm: Lĩnh vực là nhóm riêng? thừa "Ghi chú"? có "Thông tin công khai"? | TVV chưa công khai: 5 nhóm (Thông tin cá nhân / Nghề nghiệp / Tổ chức & Mạng lưới / **Lĩnh vực pháp luật (riêng)** / File đính kèm) — KHÔNG có "Ghi chú". TVV công khai: thêm nhóm **"Thông tin công khai"** (Mô tả công khai / File đính kèm công khai / Thời gian đăng tải) = 6 nhóm | Không |

Kết luận: 0 GAP. Kết quả re-verify: **Đã fix cả 3 ý** — (1) "Lĩnh vực pháp luật" là nhóm riêng (không còn gộp vào Tổ chức), (2) không còn nhóm "Ghi chú" thừa, (3) nhóm "Thông tin công khai" hiển thị đúng khi hồ sơ đã công khai.
