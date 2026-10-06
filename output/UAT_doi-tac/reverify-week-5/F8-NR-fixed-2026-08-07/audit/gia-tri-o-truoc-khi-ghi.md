# Giá trị 2 ô sẽ ghi — CHỤP TRƯỚC KHI GHI (lô F8)

> Đọc tab `bug` lúc 2026-08-07 ~11:3x giờ VN. Dùng làm `--expect` khi ghi, và để khôi phục nếu ghi nhầm.
> Nội dung ô `Kết quả verify` dài được tách ra `audit/o-truoc-khi-ghi/<MÃ>-T-cu.txt`.

| dòng | Mã TC | `Trạng thái dev fix` (R) | `Kết quả verify` (T) |
|---|---|---|---|
| 10 | `KTDGKQHT_05` | `Fixed` | CÓ NỘI DUNG (6790 ký tự) → `audit/o-truoc-khi-ghi/KTDGKQHT_05-T-cu.txt` |
| 308 | `QLHDTVVCG_02` | `Fixed` | (RỖNG) |
| 309 | `QLHDTVVCG_03` | `Fixed` | (RỖNG) |
| 310 | `QLHDTVVCG_04` | `Fixed` | (RỖNG) |
| 311 | `QLHDTVVCG_05` | `Fixed` | (RỖNG) |
| 314 | `QLHDTVVCG_08` | `Fixed` | (RỖNG) |
| 315 | `QLHDTVVCG_09` | `Fixed` | (RỖNG) |
| 319 | `QLHDTVVCG_13` | `Fixed` | (RỖNG) |
| 321 | `QLHDTVVCG_15` | `Fixed` | (RỖNG) |
| 322 | `QLHDTVVCG_16` | `Fixed` | (RỖNG) |
| 323 | `QLHDTVVCG_17` | `Fixed` | (RỖNG) |
| 324 | `QLHDTVVCG_18` | `Fixed` | (RỖNG) |
| 325 | `QLHDTVVCG_19` | `Fixed` | (RỖNG) |
| 327 | `QLHDTVVCG_21` | `Fixed` | (RỖNG) |
| 328 | `QLHDTVVCG_22` | `Fixed` | (RỖNG) |
| 329 | `QLHDTVVCG_23` | `Fixed` | (RỖNG) |
| 330 | `QLHDTVVCG_24` | `Fixed` | (RỖNG) |
| 332 | `QLHDTVVCG_26` | `Fixed` | (RỖNG) |
| 333 | `QLHDTVVCG_27` | `Fixed` | (RỖNG) |
| 341 | `TPDBCKQTHCT_02` | `Fixed` | (RỖNG) |
| 343 | `THBCTHCT_01` | `Fixed` | (RỖNG) |
| 344 | `THBCTHCT_02` | `Fixed` | (RỖNG) |
| 345 | `THBCTHCT_05` | `Fixed` | (RỖNG) |

## Ô CHỈ ĐỌC — cấm ghi đè, chụp lại để đối chiếu sau lô

| dòng | Mã TC | `Trạng thái` (N) | `Kết quả thực tế` (L) | `TKM phản hồi lần 1` (Q) | `DEV phản hồi lần 1` (S) |
|---|---|---|---|---|---|
| 10 | `KTDGKQHT_05` | Fail | (RỖNG) | Màn hình danh sách không hiển thị mã học viên nhưng khi nhập… | (RỖNG) |
| 308 | `QLHDTVVCG_02` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 309 | `QLHDTVVCG_03` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 310 | `QLHDTVVCG_04` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 311 | `QLHDTVVCG_05` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 314 | `QLHDTVVCG_08` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 315 | `QLHDTVVCG_09` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 319 | `QLHDTVVCG_13` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 321 | `QLHDTVVCG_15` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 322 | `QLHDTVVCG_16` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 323 | `QLHDTVVCG_17` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 324 | `QLHDTVVCG_18` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 325 | `QLHDTVVCG_19` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 327 | `QLHDTVVCG_21` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 328 | `QLHDTVVCG_22` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 329 | `QLHDTVVCG_23` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 330 | `QLHDTVVCG_24` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 332 | `QLHDTVVCG_26` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 333 | `QLHDTVVCG_27` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 341 | `TPDBCKQTHCT_02` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 343 | `THBCTHCT_01` | N/R | (RỖNG) | Chưa thực hiện được do uc GKQTHCTHTPL_01 lỗi | (RỖNG) |
| 344 | `THBCTHCT_02` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |
| 345 | `THBCTHCT_05` | N/R | (RỖNG) | (RỖNG) | (RỖNG) |