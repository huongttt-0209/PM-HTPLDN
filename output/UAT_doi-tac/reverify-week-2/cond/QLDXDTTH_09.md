# Bảng đối chiếu điều kiện — re-verify QLDXDTTH_09 (row 30)

Bug gốc: khi tạo đề xuất đào tạo mới thì CB Nghiệp vụ của đơn vị quản lý KHÔNG nhận thông báo.
Re-test 2026-07-15: tạo đề xuất mới route An Giang → kiểm cbnv_dp (CB NV An Giang) có nhận thông báo không.

| Điều kiện | Bug gốc (bước tái hiện) | Mình test | GAP? |
|---|---|---|---|
| Vai trò/tài khoản nhận thông báo (recipient — đối tượng bug) | CB_NV_DP cùng đơn vị Sở Tư pháp An Giang | Đăng nhập `cbnv_dp` (CB_NV_DP, Sở Tư pháp An Giang) | Không |
| Vai trò/tài khoản tạo đề xuất (tác nhân trigger) | DN `0209888006` (Sở Tư pháp An Giang) qua chuyên trang VNeID | NHT `nht_ag_uat2` (Sở Tư pháp An Giang) — cùng là "người gửi đề xuất" theo SRS FR-III-13; đường DN cần VNeID Tier 2 không tạo được; thông báo sinh ra khi tạo đề xuất, không phụ thuộc loại người gửi | Không |
| Trạng thái/sự kiện trigger | Đề xuất đào tạo mới tạo (trạng thái "Mới gửi") | Đề xuất mới tạo 15/07/2026, trạng thái "Mới gửi", lĩnh vực Thương mại | Không |
| Đơn vị route đề xuất | Sở Tư pháp An Giang (đề xuất.donViId = donViId đơn vị) | Sở Tư pháp An Giang (NHT thuộc đơn vị này) → recipient cbnv_dp cùng đơn vị | Không |
