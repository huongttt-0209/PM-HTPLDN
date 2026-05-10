# Seed report — Set 09 + Set 10 (14 tài khoản, R7)

**Ngày:** 2026-05-10 10:30:00 → 10:53:00 (UTC+7)
**Thực hiện:** QA tự động qua Chrome DevTools MCP
**Account QTHT seed:** `qtht_01` / `Secret@123` + OTP `666666`
**Endpoint app:** http://103.172.236.130:3000
**MailHog inbox:** http://103.172.236.130:8025
**Verdict:** ✅ Đạt 14/14 tài khoản — toàn bộ create + activate + đổi MK Secret@123 thành công.

---

## 1. Phạm vi

Tạo 2 bộ tài khoản (mỗi bộ 7 role) phục vụ test multi-role isolation.

| # | Username | Vai trò | Đơn vị | Họ tên |
|---|---|---|---|---|
| 1 | qtht_09 | QTHT | BTP-TW (Cục Bổ trợ tư pháp - Bộ Tư pháp) | QTHT Test 09 |
| 2 | cb_nv_tw_09 | CB_NV_TW | BTP-TW | CB Nghiệp vụ TW 09 |
| 3 | cb_nv_bn_09 | CB_NV_BN | BCT (Bộ Công Thương) | CB NV BN 09 (BCT) |
| 4 | cb_nv_dp_09 | CB_NV_DP | STP-BNI (Sở Tư pháp Bắc Ninh) | CB NV DP 09 (BNI) |
| 5 | cb_pd_tw_09 | CB_PD_TW | BTP-TW | CB Phê duyệt TW 09 |
| 6 | cb_pd_bn_09 | CB_PD_BN | BCT | CB Phê duyệt BN 09 (BCT) |
| 7 | cb_pd_dp_09 | CB_PD_DP | STP-BNI | CB Phê duyệt DP 09 (BNI) |
| 8 | qtht_10 | QTHT | BTP-TW | QTHT Test 10 |
| 9 | cb_nv_tw_10 | CB_NV_TW | BTP-TW | CB Nghiệp vụ TW 10 |
| 10 | cb_nv_bn_10 | CB_NV_BN | BKH (Bộ Kế hoạch và Đầu tư) | CB NV BN 10 (BKH) |
| 11 | cb_nv_dp_10 | CB_NV_DP | STP-AG (Sở Tư pháp An Giang) | CB NV DP 10 (AG) |
| 12 | cb_pd_tw_10 | CB_PD_TW | BTP-TW | CB Phê duyệt TW 10 |
| 13 | cb_pd_bn_10 | CB_PD_BN | BKH | CB Phê duyệt BN 10 (BKH) |
| 14 | cb_pd_dp_10 | CB_PD_DP | STP-AG | CB Phê duyệt DP 10 (AG) |

**Email:** `<username>@htpldn.test` (đi vào MailHog).
**Mật khẩu cuối:** `Secret@123` (đã đổi từ temp pw qua API `/api/v1/auth/change-password`).

---

## 2. Quy trình thực hiện (per account)

```
[QTHT login] → [Tài khoản → Thêm mới] → [Fill 6 trường]
   → [Submit → toast "tài khoản đã được tạo, MK tạm gửi tới email"]
   → [Tab "Chờ kích hoạt" → click "Kích hoạt" → status flip HOAT_DONG]
   → [Logout QTHT]
   → [Login bằng temp pw từ MailHog + OTP 666666 → dashboard render]
   → [POST /api/v1/auth/change-password {currentPassword: tempPw, newPassword: Secret@123, newPasswordConfirm: Secret@123}]
   → [Logout]
```

**Endpoint xác nhận:**
- `POST /api/v1/auth/login` (200) — temp pw work
- `POST /api/v1/auth/verify-otp` (200) — OTP 666666 bypass
- `POST /api/v1/auth/change-password` (200) — body `{currentPassword, newPassword, newPasswordConfirm}` (note field thứ 3 là `newPasswordConfirm`, không phải `confirmPassword`)
- Toast text response: `"Mật khẩu đã được thay đổi thành công"`

**Verify smoke (qtht_09):** logout → login `qtht_09 / Secret@123 / OTP 666666` → dashboard load OK với label "QTHT Test 09 / QTHT". ✅ chứng minh end-to-end flow.

---

## 3. Account UUID (capture từ form-create response)

| Username | UUID |
|---|---|
| qtht_09 | 4e38790c-c984-474e-933e-206fb2f9f0cb |
| cb_nv_tw_09 | aa95ec96-57b9-4dea-9b5a-0ee19627419c |
| cb_nv_bn_09 | 1985d45d-9501-463f-936d-cb34a6502498 |
| cb_nv_dp_09 | 3b5f0b84-fc9a-446d-822c-304bbfaf9e51 |
| cb_pd_tw_09 | 238d5685-fe16-4f23-ac5a-e84cfbdc93ce |
| cb_pd_bn_09 | d2383db4-fbf4-4eab-8046-2977e316e21d |
| cb_pd_dp_09 | 4b795ebd-3a70-45d4-8f07-823d7a2ce8d2 |
| qtht_10 | fa6a7ffe-3bc4-4d41-ba02-f35c8fe19cb5 |
| cb_nv_tw_10 | 5dc9ae8f-3c71-4837-a6ea-eaeb9da3b6b9 |
| cb_nv_bn_10 | d94f8331-15f5-4664-936c-fabbf594c963 |
| cb_nv_dp_10 | f7cb0df0-6841-41f7-9ae5-72e34cc8288c |
| cb_pd_tw_10 | f3641884-6ec7-4c05-9144-34f68f59eec7 |
| cb_pd_bn_10 | 872a82d7-b7c8-4ed5-a1cd-a44522f904b9 |
| cb_pd_dp_10 | e6805ac6-f739-46d6-9653-51cbe78d86d1 |

---

## 4. Quan sát đáng note

1. **"Kích hoạt" là direct-activation, không có confirm modal.** Click button trực tiếp flip status `CHO_KICH_HOAT → HOAT_DONG` trong tab "Chờ kích hoạt". Tab counter cập nhật real-time. Spec SCR-VIII-08 không tả modal xác nhận → đúng spec.

2. **Temp password gửi qua MailHog là MK login được luôn (không bắt buộc đổi MK lần đầu).** Email subject: `Tài khoản hệ thống PM-HTPLDN đã được tạo`, body chứa dòng `Mật khẩu tạm: <pw>`. Login với temp pw → dashboard render bình thường, KHÔNG có forced-change-password page như email mô tả `"hệ thống sẽ yêu cầu bạn đổi mật khẩu ngay trong lần đăng nhập đầu tiên"`.
   - **Đã log bug:** [BUG-MAIL-FL-001](../../bug-reports/qtht-tai-khoan/Pass-bug-report-mail-first-login-promise-not-enforced.md) Severity Minor — email promise force-change-MK nhưng SRS + BE + FE không enforce. Cần BA review chọn hướng fix (sửa email vs thêm logic force-change).

3. **BE JWT revoke aggressive (~2 phút).** Khi tạo nhiều account liên tiếp trong 1 session QTHT, sau vài account bounce login. Workaround: re-login khi bị bounce, không cản trở tiến độ.

4. **API change-password tự động revoke session sau đổi MK** — mô tả "Sau khi đổi mật khẩu thành công, các phiên đăng nhập trên thiết bị khác sẽ bị đăng xuất tự động" trong UI Settings ✅ đúng.

5. **Field name response:** API yêu cầu `newPasswordConfirm` (không phải `confirmPassword`). Test nhanh body sai → trả error `ERR-VAL-SYS-00-01 newPasswordConfirm should not be empty`.

---

## 5. Cập nhật file

- `input/users.csv` — thêm 14 dòng mới (line 127-153 sau seed). Tất cả `mat_khau=Secret@123`, `trang_thai=HOAT_DONG`, `is_deleted=f`.

---

## 6. Verify state cuối (Tài khoản page snapshot)

Kiểm tra qua DOM scrape `qtht_01` ở /quan-tri/tai-khoan: 14/14 username có status `Hoạt động`, đơn vị + vai trò khớp bảng §1.

```
qtht_09 → Hoạt động, BTP-TW, QTHT
cb_nv_tw_09 → Hoạt động, BTP-TW, CB_NV_TW
cb_nv_bn_09 → Hoạt động, BCT, CB_NV_BN
cb_nv_dp_09 → Hoạt động, STP-BNI, CB_NV_DP
cb_pd_tw_09 → Hoạt động, BTP-TW, CB_PD_TW
cb_pd_bn_09 → Hoạt động, BCT, CB_PD_BN
cb_pd_dp_09 → Hoạt động, STP-BNI, CB_PD_DP
qtht_10 → Hoạt động, BTP-TW, QTHT
cb_nv_tw_10 → Hoạt động, BTP-TW, CB_NV_TW
cb_nv_bn_10 → Hoạt động, BKH, CB_NV_BN
cb_nv_dp_10 → Hoạt động, STP-AG, CB_NV_DP
cb_pd_tw_10 → Hoạt động, BTP-TW, CB_PD_TW
cb_pd_bn_10 → Hoạt động, BKH, CB_PD_BN
cb_pd_dp_10 → Hoạt động, STP-AG, CB_PD_DP
```

Total: 14/14 ✅
