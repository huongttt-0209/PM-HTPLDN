# R7.2.4 — Luồng kích hoạt email DN (FR-VIII-22)

**Round:** R7 (2026-05-09 02:30:00)
**Tester:** huongttt + Claude (MCP chrome-devtools)
**Verdict:** ❌ **FAIL** — luồng kích hoạt qua email **không hoạt động cho user thực** vì host link = `localhost:3000` (deploy gap) + email body không có thẻ `<a>` clickable
**DN test:** Phú Cường BN (MST 5700000029) — token activation chưa consume

---

## 1. Yêu cầu user

> "thêm cho mình 1 doanh nghiệp nhỏ, chạy luồng kích hoạt email cho mình nhé, truy cập mailhog nhớ mở UI ra check nhé"

## 2. Verdict — FAIL với lý do rõ ràng

Round này đo theo đúng phương pháp UI thật (per memory `feedback_test_method_ui_only`): mô phỏng user copy-paste link y nguyên từ email vào browser, KHÔNG edit URL, KHÔNG dùng API direct. Kết quả:

| Bước E2E | Status | Bằng chứng |
|---|---|---|
| FR-VIII-22 self-reg DN qua UI | ✅ PASS | DN-BGG-0001 + Phú Cường BN saved (verify GET API) |
| Email "Kích hoạt..." gửi tới MailHog | ✅ PASS | MailHog inbox 83 msg |
| Email body có link kích hoạt | ⚠️ Có nhưng dạng plain text — KHÔNG có thẻ `<a>` | DOM `querySelectorAll('a')` = `[]` |
| User copy-paste link gốc → browser | ❌ **FAIL** | `ERR_CONNECTION_REFUSED` (host `localhost:3000`) |
| BE consume token → CHO_PHAN_QUYEN | ❌ N/A | Không tới được do bước trên fail |
| Login DN → dashboard | ❌ N/A | Không thể test khi luồng kích hoạt fail |

> **Lý do FAIL (per SRS FR-VIII-22 §Processing Bước 6 + AC):** Spec yêu cầu "Gửi email xác nhận (link kích hoạt)" + AC "user click link activation → TK chuyển CHO_PHAN_QUYEN". Hiện tại email gửi OK nhưng link **không click được trong môi trường user thực** — vi phạm AC.

## 3. Bug đã log

| Bug ID | Severity | Title | File |
|---|---|---|---|
| BUG-DEPLOY-MAIL-HOST-001 | Major | Email kích hoạt dùng host `localhost:3000` → user click `ERR_CONNECTION_REFUSED` | [bug-report-deploy-mail-host.md](../../bug-reports/doanh-nghiep/bug-report-deploy-mail-host.md) |
| BUG-DEPLOY-MAIL-LINK-002 | Major | Email body render link plain text — KHÔNG có thẻ `<a>` clickable | [bug-report-deploy-mail-host.md](../../bug-reports/doanh-nghiep/bug-report-deploy-mail-host.md) |

## 4. Bằng chứng phương pháp UI thật

### Phase 1 — Self-reg DN qua UI form FR-VIII-22 (PASS)
- `r7-2-4-dn1-form-filled.png` · `r7-2-4-dn2-form-filled.png` — 21 trường form fill đủ
- API verify: DN saved trạng thái `CHO_KICH_HOAT` (FR-VIII-22 §Processing Bước 5)

### Phase 2 — MailHog UI check email (PASS)
- `r7-2-4-mailhog-baseline-inbox.png` — inbox 83 message
- `r7-2-4-mailhog-email-format-sample.png` — From: `"PM-HTPLDN" <noreply@htpldn.gov.vn>`, Subject: "Kích hoạt tài khoản doanh nghiệp HTPLDN"
- `r7-2-4-mailhog-email-localhost-link.png` — body chứa link plain text host `localhost:3000`

### Phase 3 — Click link activation (FAIL)

**Cách test ĐÚNG (UI mô phỏng user thực):**
1. Mở email phucuong.bn trong MailHog UI HTML preview.
2. Inspect iframe DOM → `querySelectorAll('a')` = `[]` (không có thẻ `<a>`).
3. Copy nguyên text link `http://localhost:3000/auth/verify-email?token=9df67ce0-72aa-414b-9100-fec8e522805a`.
4. `new_page` với URL gốc (mô phỏng user paste vào browser).
5. **Kết quả:** `chrome-error://chromewebdata/` · title `localhost` · body "Không thể truy cập trang web này / localhost đã từ chối kết nối / ERR_CONNECTION_REFUSED".

**Bằng chứng:** `r7-2-4-activation-link-broken-real-user-click.png` (hoặc copy `deploy-mail-host-001-err-connection-refused.png` trong bug-reports).

### Phase 4 — Login + dashboard

**Không test** — luồng kích hoạt fail ở Phase 3 nên các bước tiếp theo (login với MK đã set, OTP, dashboard) không có ý nghĩa. Khi BE consume token thất bại, TK vẫn ở `CHO_KICH_HOAT` → login sẽ bị reject.

> **Note phương pháp:** Round trước (lần đầu) tôi tự edit `localhost` → `103.172.236.130` để workaround → record verdict PASS với note "Major workaround". Đây là sai phương pháp (vi phạm rule UI-only) — user đã correct ngay tại session. Round này test lại đúng cách: copy-paste y nguyên URL gốc → bug rõ ràng hơn nữa.

## 5. Issues phụ phát hiện đồng thời

### Issue #5 — Throttle 1h chặn self-reg DN Nhỏ thứ 3
- **Trigger:** Self-reg DN thứ 3 cùng IP/session trong 30 phút.
- **UI message:** "Vui lòng thử lại sau 1 giờ".
- **Memory match:** BUG-THROTTLE-001 verified Closed 2026-05-07. Có thể là rule hợp lệ (giới hạn 2 self-reg/h/IP) hoặc regression — cần BA xác nhận spec rate limit.
- **Action:** Document, retry sau 1h hoặc escalate BA.

### Issue #6 — Modal NĐ39/2018 guard quy mô (verified BR, không phải bug)
- **Trigger:** Form data: 50 LĐ + 25 tỷ DT + **30 tỷ vốn** + Quy mô = "Nhỏ" + Ngành = Nông lâm.
- **NĐ39/2018 nông lâm:** Nhỏ vốn ≤ 20 tỷ → 30 tỷ thuộc Vừa → BE đúng.
- **UX:** Modal cảnh báo + 2 nút "Dùng giá trị gợi ý" / "Giữ lựa chọn của tôi".
- **Action:** Không log bug, document như verified BR.

### Issue #7 — FR-VIII-26 reset MK form? (cần BA verify)
- **SRS FR-VIII-26 v3 §FR-VIII-22:** Processing Bước 7 chỉ ghi "User click link → chuyển trạng thái = CHO_PHAN_QUYEN" — KHÔNG yêu cầu form đặt MK mới.
- **Phân tích:** FR-VIII-22 §Inputs đã yêu cầu user nhập MK (validation BR-AUTH-01 + xác nhận MK) khi đăng ký. Nếu MK đã chuẩn từ FR-VIII-22, **không cần reset MK ở FR-VIII-26** — link chỉ confirm sở hữu email.
- **Action:** Note pending — escalate BA Q (chưa thể verify do luồng activation fail trước).

## 6. Pool DN sau seed

Pool vẫn 25 DN (DN Nhỏ × Nông lâm × Lạng Sơn KHÔNG seed thành công do throttle Issue #5). 9/9 combo cover từ phase 1 vẫn giữ.

**TODO retry sau throttle clear (~02:40 sáng):**
- Self-reg DN-LS với MST 5800000030, vốn 18 tỷ (≤ 20 tỷ ngưỡng Nhỏ nông lâm) → 50 LĐ + 25 tỷ DT + 18 tỷ vốn → Quy mô Nhỏ thoả NĐ39/2018.

## 7. Conclusion

Luồng kích hoạt email DN E2E **FAIL** — phát hiện 2 bug Major (BUG-DEPLOY-MAIL-HOST-001 + BUG-DEPLOY-MAIL-LINK-002). FR-VIII-22 self-reg + email gửi đều OK; điểm gãy ở **email link không click được trong môi trường user thực** vì host hardcode `localhost:3000` và body không có thẻ `<a>`.

**Next action:**
1. ✅ Log bug `bug-report-deploy-mail-host.md` (đã làm).
2. ⏰ Escalate dev set BE config `MAIL_BASE_URL=http://103.172.236.130:3000` per env deploy + đổi template email sang HTML có thẻ `<a>`.
3. ⏰ Re-test toàn bộ luồng kích hoạt sau khi dev fix BUG-DEPLOY-MAIL-HOST-001.
4. ⏰ Retry seed DN Nhỏ × Nông lâm sau throttle clear.
5. ⏰ Escalate BA Q về FR-VIII-26 reset MK spec (khi luồng kích hoạt thông thì test tiếp).
