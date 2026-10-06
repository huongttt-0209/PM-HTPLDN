# Bảng đối chiếu điều kiện — THDG_02

Loại bug: **Màn Chấm điểm (FR-VI-06 / SCR item 41-42) — đối tác báo thiếu "Nhận xét từng tiêu chí"; "Nhận xét tổng thể" hiện thành "Ghi chú".** Verdict phụ thuộc: (1) tái hiện đúng role/state, (2) SRS có prescribe số ô nhận xét + nhãn không.

| Điều kiện có thể đổi kết quả | Đối tác | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò | CB Nghiệp vụ | `cbnv_hn` (CB_NV_DP), người được phân công | Không |
| Trạng thái đợt | Tab Thực hiện / Chấm điểm | Đợt DGHQ-B1 đã qua chấm điểm (bảng cột đầy đủ) | Không |
| Màn đối chiếu | Bảng chấm điểm | Cùng bảng | Không |
| Đối tượng so sánh | App: mỗi tiêu chí 1 ô điểm, cột nhận xét chung nhãn "Ghi chú", không có ô nhận xét từng tiêu chí | App tôi test: y hệt | Không |

**Kết luận: 0 GAP role/state.** Tái hiện đúng. Đối chiếu SRS: FR-VI-06 Inputs #4 `nhan_xet` (từng tiêu chí, Max 1000) + #5 `nhan_xet_tong_the` (Max 2000); nhưng SCR item 42 chỉ mô tả 1 cột "Nhận xét (textarea inline)". Hai phần SRS không khớp về số ô nhận xét; không quy định nhãn "Ghi chú"/"Nhận xét tổng thể". → **BA confirm**.
