# Bảng đối chiếu điều kiện — QLDX_03 (re-verify vòng 2, 03/08/2026)

| Điều kiện | Bug gốc (vòng 2) | Mình test | GAP? |
|---|---|---|---|
| Trạng thái phiên | Đã đăng nhập thành công | Đã đăng nhập thành công (cbnv_tw, build V1.0.4) | Không |
| Thời gian không thao tác | ~25-30 phút không thao tác | Đo 2 lượt: lượt 1 đồng hồ thật 14.8 phút liên tục; lượt 2 đặt mốc hoạt động cuối rồi để đồng hồ thật vượt ngưỡng 25 và 30 phút | Không |
| Tình trạng mạng | Không nêu trong phiếu | Canh song song bằng curl 25s/lần, 20/20 lần HTTP 200 trong khoảng đo | Không |
