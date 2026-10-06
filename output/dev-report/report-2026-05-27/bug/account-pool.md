# Account Pool Ownership — Round 8

## 11 account pool

| Username | Pass | Role | Đơn vị | Owner agent | Status |
|---|---|---|---|---|---|
| admin | Secret@123 | root | TW | F (race) | ⏳ |
| qtht_01 | Secret@123 | QTHT | TW | B, E | ⏳ |
| qtht_02 | Secret@123 | QTHT | TW | B (fallback) | ⏳ |
| cb_nv_tw_01 | Secret@123 | CB_NV_TW | TW | C1 | ⏳ |
| cb_nv_tw_02 | Secret@123 | CB_NV_TW | TW | C2 | ⏳ |
| cb_nv_dp_01 | Secret@123 | CB_NV_DP | ĐP BKH | D (cross-tenant left) | ⏳ |
| cb_nv_dp_02 | Secret@123 | CB_NV_DP | ĐP BTC | D (cross-tenant right) | ⏳ |
| cb_nv_bn_01 | Secret@123 | CB_NV_BN | BKH | F (race) | ⏳ |
| cb_nv_bn_02 | Secret@123 | CB_NV_BN | BTC | F (race) | ⏳ |
| tvv_01 | Secret@123 | TVV | TVV | F + cross-role | ⏳ |
| tvv_02 | Secret@123 | TVV | TVV | F + cross-role | ⏳ |

## R8_ Read-only role (sẽ tạo ở A0.3)

| Role code | Permissions (target) | Bind account |
|---|---|---|
| R8_DG_NoDelete | Đánh giá full trừ DELETE | r8_dg_01 (tạo mới) |
| R8_CT_NoEdit | Câu trả lời full trừ UPDATE | r8_ct_01 |
| R8_GV_NoEdit | Giảng viên full trừ UPDATE | r8_gv_01 |
| R8_DN_NoEdit | Doanh nghiệp full trừ UPDATE | r8_dn_01 |
| R8_API_Consumer | API consumer scope (DVC) | r8_api_01 |

## Lock semantics

- Agent lock entity trước khi mutation (POST/PATCH/DELETE) bằng entry `record-locks.md`
- Read-only operation (GET) không cần lock
- Lock format: `<entity>:<id> => agent_<X> (HH:MM:SS)`
- Release: agent đóng task → xóa entry
