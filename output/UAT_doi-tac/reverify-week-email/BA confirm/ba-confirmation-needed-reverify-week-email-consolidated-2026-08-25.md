# BA confirmation needed — Tổng hợp toàn bộ luồng Email reverify — 2026-08-25

> **Mục đích:** gom toàn bộ nội dung còn cần BA phản hồi/chốt sau khi rà soát thư mục `reverify-week-email`, đối chiếu lại bằng SRS v3.5 chính thức. File này không thay bug report.
>
> **Nguồn SRS duy nhất dùng citation:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Không dùng số dòng từ `input/srs-update-*`.
>
> **Phạm vi audit:** đã rà từng dòng 170/170 testcase trong 4 file (Trace ID, Expected Result, Status và ghi chú Actual), đồng thời đối chiếu test plan, traceability, setup, 10 bug report, condition table, 2 phiếu BA cũ và 2 phiếu trao đổi QA/Dev ngày 24–25/08/2026. Không có NotebookLM context/connector trong phiên audit; kết luận dựa trên SRS local chính thức và evidence hiện có, không chạy lại UI ở lượt tổng hợp này.

| Module | Trạng thái luồng | Workflow | Functional coverage | Bug Open | Bug Closed | TC/path còn thiếu | Blocker chính | Phương án để full |
|---|---|---:|---:|---:|---:|---|---|---|
| Reverify Email | Có điều kiện | Chưa full | 170 TC: 90 Pass · 49 Fail · 26 Blocked · 5 Not Run theo trạng thái thô trong TC docs | 2 `Chờ BA` | 32 | BA/spec: 16 vấn đề; ngoài BA còn integration, SMTP stub, time-travel/seed | 2 bug chưa có bản fix để retest; SRS còn một số điểm lệch/thiếu policy; TC docs chưa sync sau R3/R4 | BA trả lời bảng ưu tiên; Dev xử lý 2 bug; Infra cấp test hook; QA sync verdict và rerun |

> **Lưu ý coverage:** 49 dòng `Fail` trong TC docs là trạng thái lịch sử, chưa được cập nhật đồng bộ sau khi 32 bug đã Closed-verified. Không được dùng con số này để kết luận còn 49 lỗi phần mềm.

## Bug Summary

| Tổng bug | Open | Partial/Open | Closed | Closed-verified | New bug | Ghi chú nguồn |
|---:|---:|---:|---:|---:|---:|---|
| 34 | 2 (`Chờ BA`) | 0 | 32 | 32 | 0 | Đếm từ Bug Summary Table mới nhất của 10 file `bug-report-em-*.md`; hai phiếu còn treo là `BUG-EM-DT-004`, `BUG-EM-HDD-006` |

## Danh sách BA cần phản hồi

| Ưu tiên | Mã | Nhóm | Nội dung cần BA trả lời | Loại |
|---|---|---|---|---|
| P0 | BA-EM-DT-004 | Đào tạo | Xác nhận email công bố kết quả gửi tới `TAI_KHOAN.email` của DN/NHT trong `nguoi_dang_ky_id`, không gửi trực tiếp `HOC_VIEN.email` | Dạng A — SRS đã đủ căn cứ, cần BA phản hồi Dev |
| P0 | BA-EM-HDD-006 | Hỏi đáp | Xác nhận escalation là CB Phê duyệt của đơn vị cấp trên trực tiếp; chốt gửi một hay tất cả CB PD hợp lệ và cách xử lý đơn vị gốc không có cấp trên | Dạng A + chốt cardinality |
| P0 | BA-EM-RECIPIENT-RESOLVER-01 | Notification xuyên module | Chốt cách resolve các mô tả `CB PD/CB NV cùng đơn vị`: một cán bộ đích danh hay toàn bộ tài khoản hợp lệ; tiêu chí chọn theo người tạo/người xử lý/quyền/trạng thái tài khoản | Dạng B — SRS nêu vai trò/phạm vi nhưng chưa định nghĩa resolver/cardinality |
| P0 | BA-EM-2FA-01 | Tài khoản/2FA | Đồng bộ SRS: mã 2FA Tier 1 gửi qua email hay sinh từ ứng dụng xác thực | Dạng A — source of truth đã chốt email nhưng FR chưa sync |
| P0 | BA-EM-2FA-02 | Tài khoản/2FA | Chốt policy gửi lại OTP: cooldown, số lần, vô hiệu mã cũ, TTL và việc gọi lại endpoint login | Dạng B — SRS chưa đặc tả |
| P0 | BA-EM-2FA-03 | Tài khoản/2FA | Chốt cách ghi audit đăng nhập/OTP thất bại | Dạng B — SRS tự lệch |
| P0 | BA-EM-ACT-RESEND-01 | Kích hoạt tài khoản | Chốt rate limit, số lần gửi lại và vòng đời token cũ/mới cho từng loại tài khoản | Dạng B — UI có action nhưng thiếu FR đầy đủ |
| P0 | BA-EM-SMTP-01 | SMTP/Resilience | Chuẩn hóa retry interval, trạng thái thất bại và rollback boundary cho mọi nhóm email | Dạng B — quy tắc chung và module chưa phủ đồng đều |
| P1 | BA-CLAR-EM-TK-001 | Tài khoản | Có bắt buộc hiển thị `Ngày tạo`/`Đăng nhập cuối` trên danh sách tài khoản không | Dạng B — phiếu cũ còn hiệu lực |
| P1 | BA-EM-DT-007 | Đào tạo | Hủy khóa gửi thông báo cho mọi đăng ký hay chỉ học viên đã duyệt | Dạng B — SRS tự mâu thuẫn |
| P1 | BA-EM-TVV-EMAIL-01 | TVV/CG | Chuẩn hóa câu lỗi email không hợp lệ giữa FR error table và SCR | Dạng B — SRS có 3 câu khác nhau |
| P1 | BA-EM-TVV-EMAIL-02 | TVV/CG | Khi đổi `TU_VAN_VIEN.email`, có đồng bộ `TAI_KHOAN.email` không | Dạng B — SRS chưa quy định |
| P1 | BA-EM-DN-CLAIM-01 | DN Claim | Màn xác nhận gửi link có được ghi cố định “30 phút” khi token Claim/first-login là vĩnh viễn không | Dạng B — SRS quy định TTL nhưng thiếu câu UX tương ứng |
| P1 | BA-EM-EMAIL-NORM-01 | Dữ liệu email | Chốt chuẩn hóa trước unique: trim, lowercase và so sánh hoa/thường | Dạng B — SRS chỉ ghi RFC 5322 + unique |
| P1 | BA-EM-ACCOUNT-EMAIL-01 | Tài khoản | Bổ sung FR cho “Đổi email tài khoản”: màn hình, quyền, validation, audit và tác động đăng nhập | Dạng B — BR nhắc chức năng nhưng không có FR tương ứng |
| P1 | BA-EM-TEMPLATE-01 | Email template | Chốt catalog subject/body/biến/link/From/Reply-To/attachment cho từng sự kiện | Dạng B — BR chỉ dẫn chung, chưa có catalog kiểm thử được |

---

## BA-EM-DT-004 / BUG-EM-DT-004 — Đích nhận email công bố kết quả đào tạo

**Phân loại:** Dạng A — QA đã có kết luận từ SRS; cần BA phản hồi Dev để gỡ trạng thái chờ.

**Bối cảnh testcase**

- TC `EM-NOT-DT-11`, thao tác Công bố kết quả khóa học.
- R3 chỉ kiểm `HOC_VIEN.email` của học viên nhập tay, không kiểm tài khoản DN/NHT đã tạo đăng ký nên evidence chưa chứng minh bản fix đúng hay sai.
- Dev đang chờ BA chốt đích nhận trước khi fix.

**Đối chiếu SRS v3.5**

- Đăng ký luôn lưu `nguoi_dang_ky_id` là tài khoản DN/NHT đang đăng nhập.
- `nguoi_dang_ky_id` là bắt buộc; SRS đã bỏ luồng CB NV nhập tay đăng ký.
- Bước Công bố kết quả ghi email theo tài khoản DN/NHT đã đăng ký học viên.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:478`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1433`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1743`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:2728`

**Kết quả verify hiện tại**

- Hệ thống đã công bố kết quả nhưng không thấy thư ở `HOC_VIEN.email` của fixture R3.
- Chưa có fixture hậu fix với `nguoi_dang_ky_id` rõ ràng để kiểm `TAI_KHOAN.email` của đúng DN/NHT.
- Evidence: `../bug-report/image/bug-em-dt-004-r3-published-no-email-2026-08-25.png` và `../cond/BUG-EM-DT-004.md`.

**Kết luận QA**

- SRS đã đủ căn cứ để hiểu người nhận SMTP là `TAI_KHOAN.email` của tài khoản DN/NHT trong `DANG_KY_DAO_TAO.nguoi_dang_ky_id`.
- Cụm “cho từng học viên” mô tả mỗi kết quả/đăng ký cần phát sinh thông báo, không biến `HOC_VIEN.email` thành đích nhận khi SRS đã chỉ rõ kênh theo tài khoản đăng ký.

**Nội dung đề xuất BA phản hồi Dev**

> Xác nhận `BUG-EM-DT-004` xử lý theo `nguoi_dang_ky_id`: email công bố kết quả gửi tới `TAI_KHOAN.email` của DN/NHT đã đăng ký học viên; không gửi bản riêng tới `HOC_VIEN.email`. Dev triển khai theo hướng này, QA dựng đăng ký mới và rerun `EM-NOT-DT-11`.

---

## BA-EM-HDD-006 / BUG-EM-HDD-006 — Đích escalation cảnh báo SLA Hỏi đáp

**Phân loại:** Dạng A — SRS đã chỉ ra cấp trên; BA cần xác nhận cách áp dụng/cardinality để Dev mở fix.

**Bối cảnh testcase**

- `EM-NOT-HDD-06`, `EM-NOT-HDD-07`: cron hiện chỉ gửi người xử lý; thiếu CB PD cùng đơn vị và không có escalation.
- Dev xác nhận phiếu chưa được fix vì đang chờ BA.

**Đối chiếu SRS v3.5**

- `QUA_HAN` phải gửi CB NV + CB PD.
- `QUA_HAN_NGHIEM_TRONG` thêm escalation.
- EC-01 và bảng notification cùng module chỉ ra đối tượng escalation là CB PD cấp trên.
- SRS chưa nói rõ chọn một hay fan-out toàn bộ CB PD hợp lệ ở đơn vị cấp trên, và chưa ghi cách xử lý đơn vị không có cha.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:761`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:976`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:985-986`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:1187-1188`

**Kết quả verify hiện tại**

- Baseline R3: 6/6 lần chuyển mức chỉ gửi người xử lý; CB PD cùng đơn vị và 6 CB PD TW cấp trên đều không nhận.
- R4 chưa retest vì chưa có bản fix. Evidence: `../bug-report/image/bug-em-hdd-006-r3-only-cbnv-email-2026-08-25.png`.

**Nội dung đề xuất BA phản hồi Dev**

> Xác nhận escalation của SLA Hỏi đáp gửi tới CB Phê duyệt thuộc đơn vị cấp trên trực tiếp. BA chốt thêm: (1) gửi một người theo resolver hay toàn bộ CB PD đang hoạt động; (2) đơn vị không có cấp trên thì không escalate thêm, nhưng vẫn gửi CB NV + CB PD cùng đơn vị. Vế CB PD cùng đơn vị ở `QUA_HAN` là yêu cầu rõ, Dev không cần chờ thêm.

---

## BA-EM-RECIPIENT-RESOLVER-01 — Resolver/cardinality người nhận theo vai trò

**Phân loại:** Dạng B — khoảng trống xuyên module được phát hiện khi rà đủ 170 testcase.

**Bối cảnh testcase**

- SRS thường ghi `TB CB PD cùng đơn vị`, `TB CB NV`, `CB PD quản lý` nhưng không nói đó là một tài khoản đích danh hay toàn bộ tài khoản thỏa vai trò/phạm vi.
- Actual đang fan-out khác nhau: `EM-NOT-DG-01` và `EM-NOT-DG-03` gửi cho 6 CB PD cùng đơn vị; `EM-INF-08` gửi cho 9 CB NV cùng đơn vị; `EM-INF-18` tạo in-app cho 2 CB PD cùng đơn vị. Một số luồng khác chỉ ghi nhận một người tạo/người xử lý.
- Vì chưa có resolver chuẩn, QA chưa có oracle để kết luận số người nhận đúng cho mọi sự kiện; đây cũng là rủi ro gửi thiếu hoặc phát tán email quá rộng.

**Đối chiếu SRS v3.5**

- BR-NOTIF-01 xác định vai trò và phạm vi nhận, nhưng không định nghĩa cardinality hay thuật toán chọn tài khoản: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5745`.
- Ví dụ Đào tạo ghi `Gửi thông báo CB PD cùng đơn vị`: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:195`, `:227`, `:1342`.
- Ví dụ TVV ghi `gửi thông báo CB PD cùng đơn vị`: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:6038`; các FR chi tiết cũng không chỉ ra một người nhận cụ thể.
- BR-AUTH-05 chỉ chốt phạm vi phê duyệt strict cùng đơn vị, không phải quy tắc chọn người nhận: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5614`.

**Câu hỏi cần BA xác nhận**

1. `CB PD cùng đơn vị` gửi cho toàn bộ CB PD đang hoạt động có quyền duyệt entity đó, hay chỉ người được phân công/người resolver chọn?
2. `CB NV` không ghi thêm định danh phải ưu tiên người tạo, người đang xử lý, người phụ trách hay toàn bộ CB NV cùng đơn vị?
3. Có lọc theo `HOAT_DONG`, quyền thực tế, cấp và `don_vi_id`; có loại chính người thao tác khỏi danh sách nhận không?
4. Khi không tìm thấy người hợp lệ, hệ thống ghi cảnh báo, fallback cấp trên/TW hay giữ notification thất bại để QTHT xử lý?
5. Cần một thư riêng cho mỗi người hay một thư nhiều người nhận; cách chống lộ địa chỉ và dedup theo người/sự kiện ra sao?

**Đề xuất QA tạm thời**

- BA ban hành một recipient matrix/resolver dùng chung theo từng event: selector, scope, trạng thái tài khoản, cardinality, fallback và kênh.
- Mỗi người nhận một email riêng; không dùng To/CC hàng loạt, trừ trường hợp nghiệp vụ chỉ định CC rõ như tổ chức tư vấn.
- `BA-EM-HDD-006` tiếp tục chốt riêng đích cấp trên/root-unit; cardinality áp theo resolver chung này để tránh mỗi module hiểu một kiểu.

---

## BA-EM-2FA-01 / GAP-EMAIL-01 — Email OTP hay ứng dụng xác thực

**Phân loại:** Dạng A — Business Rule canonical đã chốt email, FR chi tiết chưa đồng bộ.

**Bối cảnh testcase**

- `EM-TK-2FA-01..04` đã Pass về hành vi hai bước; actual gửi mã 6 số qua email.
- Testcase đang cố ý không chấm kênh vì SRS nói hai hướng khác nhau.

**Đối chiếu SRS v3.5 và citation**

- Business Rules Catalog là source of truth và ghi Tier 1 dùng “TOTP 2FA qua email”; trạng thái BR-AUTH-01 đã được CĐT xác nhận: `srs-v3.5.md:5598`, `:5606`, `:5620`.
- FR-VIII-20 lại ghi mã do ứng dụng xác thực sinh và yêu cầu người dùng lấy mã từ ứng dụng: `srs-fr-10-quan-tri.md:909`, `:923`, `:936-937`.

**Kết quả verify UI hiện tại**

- Sau username/password, API chỉ trả `otpToken`, chưa cấp session; MailHog nhận thư “Mã xác thực đăng nhập”; nhập đúng mã mới tạo phiên.
- Evidence nằm tại dòng `EM-TK-2FA-01..04` trong `../01-TC-email-tai-khoan.md`.

**Kết luận QA và đề xuất BA phản hồi**

- Hành vi email OTP phù hợp source of truth/CĐT confirm; không cần gửi Dev đổi sang authenticator nếu BA không có quyết định mới.
- BA cập nhật FR-VIII-20, thay “ứng dụng xác thực/TOTP” bằng mô tả chính xác “OTP 6 số gửi qua email, TTL theo policy”, đồng thời thống nhất thuật ngữ TOTP/OTP.

---

## BA-EM-2FA-02 / EM-TK-2FA-05 — Policy gửi lại mã 2FA

**Phân loại:** Dạng B — SRS chưa đặc tả.

**Bối cảnh và actual**

- UI không cooldown nút Gửi lại; mỗi lần gọi lại endpoint login cùng username/password.
- 5 lần liên tiếp sinh 5 mã/thư; lần 6 bị rate-limit 60 giây theo IP.
- Mã cũ vẫn dùng được cùng lúc với mã mới trong TTL 300 giây.
- Evidence chi tiết tại `../01-TC-email-tai-khoan.md`, dòng `EM-TK-2FA-05`.

**Khoảng trống trong SRS**

- FR-VIII-20 mô tả từ nhập password đến nhập OTP và tạo phiên nhưng không có resend, cooldown, rate-limit, số mã đồng thời hoặc quy tắc vô hiệu mã cũ.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:917-940`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:965`

**Câu hỏi cần BA + chủ sở hữu bảo mật xác nhận**

1. Có cooldown nút Gửi lại không; nếu có bao nhiêu giây?
2. Giới hạn theo IP, tài khoản hay phiên; tối đa bao nhiêu lần?
3. Gửi mã mới có vô hiệu toàn bộ mã cũ của cùng phiên/tài khoản không?
4. TTL 5 phút tính từ từng lần gửi hay giữ mốc của phiên đầu?
5. Có chấp nhận FE gửi lại username/password qua endpoint login để resend không, hay cần endpoint resend theo `otpToken`?

**Đề xuất QA tạm thời**

- Giữ `EM-TK-2FA-05 = Blocked`, không log bug sai spec.
- Khuyến nghị security baseline: cooldown 60 giây, mã mới vô hiệu mã cũ, rate-limit theo cả tài khoản và IP, resend bằng `otpToken` thay vì gửi lại password.

---

## BA-EM-2FA-03 / EM-TK-2FA-03 — Audit đăng nhập/OTP thất bại

**Phân loại:** Dạng B — SRS tự lệch.

**Kết quả verify hiện tại**

- Nhập OTP sai bị từ chối đúng, không tạo session, nhưng không có dòng audit tương ứng.
- Evidence ghi tại `../01-TC-email-tai-khoan.md`, dòng `EM-TK-2FA-03`.

**Điểm mâu thuẫn trong SRS**

1. Postconditions yêu cầu nhật ký ghi nhận đăng nhập thành công/thất bại.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:952-954`.
2. Bộ lọc hành động của Nhật ký chỉ có 11 giá trị, có Đăng nhập nhưng không có Đăng nhập thất bại/OTP thất bại.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1387-1393`.

**Câu hỏi cần BA xác nhận**

1. Thêm action riêng `LOGIN_FAILED`/`LOGIN_OTP_FAILED` vào `AUDIT_LOG` và màn Nhật ký; hay
2. Ghi thất bại vào security log riêng, đồng thời sửa Postconditions để không yêu cầu `AUDIT_LOG`?

**Đề xuất QA tạm thời**

- Chưa log bug do chưa có enum/source truth rõ.
- Nếu chọn phương án 1, Dev BE + FE bổ sung action/filter; QA rerun OTP sai, password sai và khóa sau 5 lần.

---

## BA-CLAR-EM-TK-001 / EM-TK-UI-01 — Cột Ngày tạo và Đăng nhập cuối

**Phân loại:** Dạng B — phiếu cũ còn hiệu lực, chưa thấy BA trả lời.

**Bối cảnh và actual**

- Dòng Excel 2, sheet `02_Tai_khoan`, mã TC `EM-TK-UI-01`.
- Vai trò `QTHT` mở `Quản trị hệ thống > Tài khoản & phân quyền`, URL `/quan-tri/tai-khoan`, kiểm danh sách và form tạo/sửa theo FR-VIII-15/SCR-VIII-03.
- Verify ngày 12/08/2026 trên DEV qua Chrome DevTools MCP.
- Danh sách tài khoản hiện có `Đăng nhập cuối`, không có `Ngày tạo`.
- Evidence: `../bug-report/image/bug-em-tk-001-danh-sach-thieu-ngay-tao.png`.

**Điểm mâu thuẫn trong SRS**

- FR-VIII-15 Outputs có cả `ngay_tao` và `lan_dang_nhap_cuoi`: `srs-fr-10-quan-tri.md:717-730`.
- SCR-VIII-03 chỉ liệt kê các cột tới Trạng thái và Hành động, không có hai cột thời gian: `srs-fr-10-quan-tri.md:1701-1726`.

**Câu hỏi cần BA xác nhận**

Outputs của FR có bắt buộc trở thành cột UI không?

1. **Hướng 1 — Outputs là tập dữ liệu bắt buộc hiển thị:** UI phải có cả `Ngày tạo` và `Đăng nhập cuối`; BA cập nhật SCR-VIII-03 để liệt kê hai cột.
2. **Hướng 2 — Outputs chỉ mô tả dữ liệu trả về:** cột UI theo SCR-VIII-03 nên không bắt buộc `Ngày tạo`; BA xác nhận `Đăng nhập cuối` là cột được phép thêm và cập nhật tài liệu cho đồng bộ.

**Đề xuất QA tạm thời**

- Giữ phần cột thời gian của `EM-TK-UI-01 = Cần BA xác nhận`.
- Verdict tổng cũ của `EM-TK-UI-01` từng Fail do `BUG-EM-TK-002` thiếu trường Vai trò; bug đó đã Closed-verified. Câu hỏi BA này chỉ còn áp cho hai cột thời gian.
- Toàn bộ nội dung phiếu `BA-CLAR-EM-TK-001` đã được hợp nhất tại mục này; không cần tham chiếu file BA riêng.

---

## BA-CLAR-EM-TK-002 / EM-TK-PWD-06, EM-TK-PWD-07 — Tài khoản khóa dùng câu trung tính hay báo rõ trạng thái

**Phân loại:** Phiếu lịch sử đã được hợp nhất đầy đủ — không còn là blocker hiện hành vì build R3 đã triển khai theo SRS E2.

**Bối cảnh testcase**

- `EM-TK-PWD-06`: tài khoản `TAM_KHOA`; `EM-TK-PWD-07`: tài khoản `VO_HIEU_HOA`.
- Câu hỏi ban đầu chỉ liên quan nội dung phản hồi của màn Quên mật khẩu; hành vi sinh token/gửi thư là `BUG-EM-TK-013`.
- Trước fix, cả hai nhánh trả HTTP 200 và câu trung tính giống tài khoản không tồn tại. Riêng `TAM_KHOA` còn sinh token, gửi thư, đặt lại mật khẩu và tự chuyển về `HOAT_DONG`.

**Điểm cần cân nhắc trong SRS v3.5**

1. E1 yêu cầu câu trung tính khi tên đăng nhập không tồn tại để chống dò tài khoản.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1337-1339`.
2. E2 yêu cầu báo rõ tài khoản đang khóa/vô hiệu hóa và hướng dẫn liên hệ quản trị viên.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1341`.
3. Luồng reset chỉ áp dụng khi tài khoản không ở `TAM_KHOA/VO_HIEU_HOA`; trạng thái Tạm khóa tự mở sau 30 phút hoặc do QTHT mở thủ công, không tự mở bằng reset password.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1296-1298`.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1318-1319`.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5616`.

**Hai hướng từng được đưa ra**

1. Giữ E2: trả `ERR-PWD-02`, nói rõ tài khoản bị khóa/vô hiệu hóa, không sinh token và không gửi thư.
2. Giữ câu trung tính cho mọi nhánh để chống enumerate, đồng thời sửa SRS và quyết định rõ có cho `TAM_KHOA` tự phục hồi qua reset password hay không.

**Kết quả triển khai và verify cuối**

- Build R3 đã chọn hướng 1 theo SRS E2.
- QA khóa tài khoản `0409998821`; hai lần Quên mật khẩu đều trả 400 `ERR-PWD-02`, MailHog không tăng, không sinh token; đăng nhập bằng mật khẩu đúng vẫn bị chặn.
- `BUG-EM-TK-013` đã Closed-verified. Evidence: `../cond/BUG-EM-TK-013.md`, `../bug-report/image/bug-em-tk-013-r3-forgot-password-blocked-2026-08-25.png`, `../bug-report/image/bug-em-tk-013-r3-locked-account-login-blocked-2026-08-25.png`.

**Kết luận QA**

- Không còn chờ BA để nghiệm thu hành vi hiện tại: hệ thống đã khớp E2 và guard của FR-VIII-26.
- Nếu BA muốn ưu tiên chống enumerate bằng câu trung tính, đó là change request mới, phải sửa đồng thời E2, guard reset password và policy tự mở khóa; không mở lại bug cũ chỉ vì cân nhắc bảo mật chưa thành quyết định.

---

## BA-EM-DT-007 / EM-NOT-DT-07 — Người nhận khi hủy khóa học

**Phân loại:** Dạng B — SRS tự mâu thuẫn.

**Bối cảnh testcase**

- TC cần một khóa có đăng ký `DA_DUYET` và đăng ký `CHO_DUYET/TU_CHOI` để phân biệt recipient.
- TC hiện còn Blocked do không tạo được đăng ký trên môi trường, nhưng expected cũng chưa chốt.

**Điểm mâu thuẫn trong SRS v3.5**

1. EC-02 yêu cầu thông báo “tất cả học viên đã duyệt”.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:510-513`.
2. BR-NOTIF-01 sự kiện (5) lại ghi “tất cả HV đã đăng ký”.
   - Citation: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5741-5745`.

**Câu hỏi cần BA xác nhận**

1. Chỉ gửi các đăng ký `DA_DUYET`; hay
2. Gửi mọi đăng ký, bao gồm `CHO_DUYET` và `TU_CHOI`?

**Đề xuất QA tạm thời**

- Tạm expected chỉ gửi học viên đã duyệt vì họ mới thực sự có suất học; không gửi pending/rejected cho đến khi BA chốt.
- Sau BA confirm vẫn cần Infra cấp mTLS/test hook hoặc Dev tạo fixture đúng trạng thái mới chạy được.

---

## BA-EM-TVV-EMAIL-01 / EM-FLD-TVV-02, EM-FLD-TVV-04 — Chuẩn câu lỗi email

**Phân loại:** Dạng B — ba vị trí SRS dùng ba câu khác nhau.

**Kết quả verify UI hiện tại**

- UI/API chặn đúng email sai format và hiện “Email không hợp lệ”. Dữ liệu không bị lưu, không phát thư.

**Điểm mâu thuẫn trong SRS v3.5**

- Đăng ký TVV E7: “Email không đúng định dạng” — `srs-fr-04-chuyen-gia-tvv.md:335-345`.
- Cập nhật TVV E1: “Định dạng email không hợp lệ” — `srs-fr-04-chuyen-gia-tvv.md:865-869`.
- SCR form: “Email không hợp lệ” — `srs-fr-04-chuyen-gia-tvv.md:1511-1522`.

**Câu hỏi cần BA xác nhận**

- Chọn một chuỗi chuẩn áp dụng cho đăng ký và cập nhật TVV/CG.

**Đề xuất QA tạm thời**

- Đề xuất dùng “Email không hợp lệ” theo SCR và UI hiện tại; BA đồng bộ hai bảng Error Handling.
- Không log bug phần mềm cho wording trước khi BA chốt.

---

## BA-EM-TVV-EMAIL-02 / EM-FLD-TVV-05 — Đồng bộ email TVV và tài khoản

**Phân loại:** Dạng B — SRS chưa quy định.

**Kết quả verify hiện tại**

- Đổi `TU_VAN_VIEN.email` không đổi `TAI_KHOAN.email`.
- Reset password và workflow notification vẫn gửi đúng `TAI_KHOAN.email`; email liên hệ mới không nhận.
- Evidence chi tiết tại `../03-TC-email-notification-workflow.md`, dòng `EM-FLD-TVV-05`.

**Khoảng trống trong SRS**

- FR-IV-11 chỉ cập nhật `TU_VAN_VIEN` và kiểm unique email mới, không nhắc `TAI_KHOAN`.
- BR-AUTH-EMAIL-01 chỉ chốt quy tắc hai email cho DN; không mở rộng sang TVV/CG.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:844-852`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5639-5642`

**Câu hỏi cần BA xác nhận**

1. Hai email độc lập: TVV email là liên hệ công khai, tài khoản email là login/reset/workflow; hay
2. Đổi email TVV phải đồng bộ sang tài khoản?

**Đề xuất QA tạm thời**

- Đề xuất độc lập giống mô hình DN: workflow tiếp tục dùng `TAI_KHOAN.email`; nếu cần đổi email tài khoản phải qua chức năng tài khoản riêng để kiểm unique và audit.

---

## BA-EM-DN-CLAIM-01 / EM-DN-CLAIM-01 — Thông báo 30 phút cho token vĩnh viễn

**Phân loại:** Dạng B — TTL rõ nhưng câu UX sau gửi chưa đặc tả theo từng nhánh.

**Kết quả verify hiện tại**

- Claim Flow tạo tài khoản `CHO_KICH_HOAT` và token vĩnh viễn dùng một lần đúng SRS.
- Màn xác nhận sau khi yêu cầu link lại ghi cố định “Link có hiệu lực trong 30 phút”.
- Evidence nằm tại `../02-TC-email-doanh-nghiep.md`, dòng `EM-DN-CLAIM-01`.

**Đối chiếu SRS v3.5**

- Tài khoản `CHO_KICH_HOAT`/Claim dùng token vĩnh viễn; tài khoản `HOAT_DONG` dùng 30 phút: `srs-fr-10-quan-tri.md:1319-1323`.
- Trường hợp không tồn tại phải trả câu trung tính chống enumerate: `srs-fr-10-quan-tri.md:1337-1339`.

**Câu hỏi cần BA xác nhận**

- Màn xác nhận chung có nên bỏ thời lượng để giữ trung tính, còn email ghi đúng TTL theo loại token; hay hiển thị thời lượng động và chấp nhận lộ nhánh xử lý?

**Đề xuất QA tạm thời**

- Dùng câu trung tính không nêu “30 phút” trên màn chung; email gửi thật ghi đúng TTL của token.

---

## BA-EM-EMAIL-NORM-01 — Chuẩn hóa email trước khi kiểm tra unique

**Phân loại:** Dạng B — SRS chưa đặc tả.

**Bối cảnh**

- Nhiều FR yêu cầu email đúng RFC 5322 và unique toàn hệ thống, nhưng không nói chuẩn hóa giá trị trước khi validate/lưu/lookup.
- Chưa có expected thống nhất cho các cặp như `User@Example.com` và `user@example.com`, email có khoảng trắng đầu/cuối hoặc domain viết hoa.

**Khoảng trống trong SRS v3.5**

- Tài khoản chỉ ghi “email unique, format hợp lệ”: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:710-714`.
- Form tài khoản ghi RFC 5322 + unique nhưng không có bước normalize: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1732-1734`.
- BR-AUTH-EMAIL-01 xác định ý nghĩa và uniqueness nhưng không quy định case/whitespace: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5640`.

**Câu hỏi cần BA xác nhận**

1. Có trim khoảng trắng đầu/cuối trước validate/lưu/lookup không?
2. Có lowercase domain không?
3. Local-part có so sánh không phân biệt hoa/thường để phục vụ unique/login/reset không?
4. Có lưu nguyên cách người dùng nhập để hiển thị nhưng dùng cột normalized riêng cho unique/lookup không?

**Đề xuất QA tạm thời**

- Đề xuất trim toàn bộ, lowercase domain và so sánh unique/lookup không phân biệt hoa-thường trên toàn địa chỉ; lưu thêm giá trị hiển thị nguyên bản nếu nghiệp vụ cần.
- Sau BA chốt, bổ sung TC biên cho tạo tài khoản, DN tự đăng ký, TVV/NHT, đổi email và Quên mật khẩu.

---

## BA-EM-ACCOUNT-EMAIL-01 — FR cho chức năng “Đổi email tài khoản”

**Phân loại:** Dạng B — Business Rule nhắc chức năng nhưng không có FR/màn hình đầy đủ.

**Bối cảnh**

- `TAI_KHOAN.email` là kênh login, OTP, kích hoạt, reset và mọi notification workflow.
- BR-AUTH-EMAIL-01 nói trường này có thể đổi trực tiếp, độc lập với `DOANH_NGHIEP.email`, không OTP/không duyệt.
- Bộ SRS chưa có FR riêng mô tả ai được đổi, đổi ở màn nào, xác thực lại ra sao, email cũ/mới nhận thông báo gì và audit lưu thế nào.

**Citation**

- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5640`
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:2406`
- SCR quản lý tài khoản hiện chỉ liệt kê hành động Xem/Sửa/Khóa/Mở khóa/Gửi lại kích hoạt: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1719-1726`.

**Câu hỏi cần BA xác nhận**

1. Chủ tài khoản tự đổi hay chỉ QTHT được đổi? Có khác nhau theo loại tài khoản không?
2. Đổi qua form Sửa tài khoản hiện tại hay màn “Đổi email tài khoản” riêng?
3. Có yêu cầu nhập lại mật khẩu/2FA hoặc xác nhận qua email cũ/mới không?
4. Email mới có hiệu lực ngay cho login/reset/workflow hay sau bước xác minh?
5. Audit phải lưu giá trị cũ → mới, IP, actor và lý do không?

**Đề xuất QA tạm thời**

- BA bổ sung FR chính thức trước khi nghiệm thu chức năng này; không tự suy expected chỉ từ một dòng BR.
- Tối thiểu phải có permission, validation/normalization, uniqueness, audit, revocation session/token và notification tới email cũ/mới.

---

## BA-EM-ACT-RESEND-01 / EM-TK-ACT-09 — Policy “Gửi lại email kích hoạt”

**Phân loại:** Dạng B — UI có hành động nhưng thiếu FR cross-account đầy đủ.

**Bối cảnh và actual đã đo**

- SCR-VIII-03 có action “Gửi lại email kích hoạt”.
- Token kích hoạt/đặt mật khẩu lần đầu là một lần dùng; build đã có các luồng DN tự đăng ký, TVV/CG, NHT và tài khoản do QTHT tạo với loại link khác nhau.
- `EM-TK-ACT-09` đã xác nhận thư gửi lại dùng được và link một lần dùng, nhưng SRS chưa chốt rate limit, số lần gửi, reuse hay regenerate token cho mọi loại tài khoản.

**Citation**

- Action trên UI: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1726`.
- Token first-login/reset một lần dùng và TTL: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1319-1323`, `:1342-1343`.
- Riêng TVV đã nói lỗi mail không rollback và có thể gửi lại link: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:606`, `:630`, `:641-644`.

**Câu hỏi cần BA xác nhận**

1. Mỗi lần resend có sinh token mới và vô hiệu token cũ không?
2. Rate limit/cooldown và tổng số lần gửi tối đa theo tài khoản/IP là bao nhiêu?
3. DN tự đăng ký phải luôn nhận link `verify-email`, còn TVV/NHT/tài khoản do QTHT tạo nhận link first-login — đúng không?
4. Resend sau khi email tài khoản vừa đổi gửi tới email cũ hay mới?
5. Hành động resend có ghi audit và có thông báo cho QTHT khi SMTP fail không?

**Đề xuất QA tạm thời**

- Sinh token mới, vô hiệu token cũ, rate-limit theo account + IP, ghi audit; chọn đúng loại link theo nguồn tạo tài khoản.
- Không dùng một implementation chung làm DN tự đăng ký nhận nhầm link đặt mật khẩu lần đầu.

---

## BA-EM-TEMPLATE-01 — Catalog template email cho từng sự kiện

**Phân loại:** Dạng B — SRS chỉ có cấu trúc/kho template ở mức khái quát, chưa có catalog nghiệm thu được.

**Bối cảnh**

- Suite hiện kiểm subject/body/link/recipient bằng nội dung actual và mô tả rải rác trong từng FR.
- Chưa có source truth tập trung cho từng sự kiện: template ID, subject, body, biến bắt buộc, URL đích, From, Reply-To, attachment, locale/version.

**Khoảng trống trong SRS v3.5**

- INT-06 chỉ định email HTML có To/Subject/Body/attachment tùy chọn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:739`.
- BR-NOTIF-01 nói template quản lý tại `MAU_PHAN_HOI` hoặc cấu hình UC108 nhưng không có catalog email: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5741-5745`.
- `MAU_PHAN_HOI` thực tế là mẫu nội dung phản hồi Hỏi đáp, không có schema email From/Reply-To/subject/link/attachment: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:2480-2510` và `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1846`.

**Câu hỏi cần BA xác nhận**

1. Source truth template email nằm ở entity/config nào?
2. Mỗi event cần template ID, subject, body, biến bắt buộc, URL, From, Reply-To, attachment và fallback text cụ thể ra sao?
3. Ai được sửa template, có version/audit/preview/test-send không?
4. Khi thiếu biến hoặc render lỗi, gửi fallback hay đánh fail queue?

**Đề xuất QA tạm thời**

- BA lập catalog một dòng cho mỗi sự kiện BR-NOTIF-01 + activation/reset/OTP/SLA; QA dùng catalog đó làm oracle nội dung.
- Không dùng `MAU_PHAN_HOI` làm tên chung cho email template nếu entity này vẫn chỉ phục vụ câu trả lời Hỏi đáp.

---

## BA-EM-SMTP-01 — Chuẩn retry và rollback khi gửi email thất bại

**Phân loại:** Dạng B — quy tắc chung và quy tắc module chưa đồng nhất về mức chi tiết.

**Bối cảnh**

- BR chung chỉ chốt sau 3 lần fail thì đánh dấu thất bại + alert QTHT, không có interval/backoff và rollback boundary theo loại sự kiện.
- Hỏi đáp quy định retry sau 10 phút.
- TVV quy định rõ lỗi gửi mail kích hoạt không rollback quyết định phê duyệt.
- Các luồng tạo/kích hoạt tài khoản khác chưa nói rõ nghiệp vụ commit hay rollback khi SMTP fail.

**Citation**

- Quy tắc chung: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5796-5797`.
- Hỏi đáp: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-02-hoi-dap.md:988-993`.
- TVV: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:606`, `:630`, `:641-644`.
- DN Claim chỉ mô tả bounce/audit/fallback, chưa chốt retry/rollback: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-10-quan-tri.md:1347`.

**Câu hỏi cần BA xác nhận**

1. Retry SMTP chuẩn dùng fixed 10 phút, exponential backoff hay cấu hình theo event?
2. Sau 3 lần fail, trạng thái chuẩn là `THAT_BAI`, `email_failed=true`, DLQ hay kết hợp cả ba?
3. Workflow notification, activation, reset password và OTP có rollback nghiệp vụ không? Luồng nào commit rồi retry async?
4. Người dùng/CB/QTHT nhận cảnh báo gì và có thao tác retry/discard thủ công không?
5. Nhật ký gửi/bounce/fail nằm ở entity/API/màn hình nào để vận hành và QA tra cứu, đặc biệt cho `EM-DN-CLAIM-04`?
6. Dedup/idempotency key bảo đảm không gửi trùng sau retry thế nào?

**Đề xuất QA tạm thời**

- Mặc định không rollback chuyển trạng thái nghiệp vụ chỉ vì notification SMTP fail; lưu outbox/queue, retry 3 lần, sau đó mark fail + DLQ + alert QTHT.
- Riêng giao dịch mà quyền truy cập phụ thuộc email kích hoạt phải giữ tài khoản `CHO_KICH_HOAT`, không kích hoạt ngầm; cho phép resend sau khi sửa email.

---

## Spec / BA Confirmation Check

| TC / vấn đề | Câu hỏi cần xác nhận | SRS local đã kiểm tra | NotebookLM đã kiểm tra | Kết luận từ nguồn | Verdict |
|---|---|---|---|---|---|
| DT-004 | Đích nhận kết quả | FR-III-04, FR-III-19, entity DANG_KY_DAO_TAO | Không có context | SRS đủ căn cứ: TK DN/NHT đăng ký | BA phản hồi Dev, không phải khoảng trống spec |
| HDD-006 | Đích/cardinality escalation | FR-II-08 EC-01, FR-II-CROSS-01, SCR-II notification | Không có context | Đích cấp trên rõ; cardinality/root-unit chưa rõ | BA chốt phần còn thiếu |
| Recipient resolver | Một hay tất cả CB theo vai trò/phạm vi | BR-NOTIF-01, BR-AUTH-05 và các FR ghi `CB PD/CB NV cùng đơn vị` | Không có context | SRS nêu vai trò nhưng không có selector/cardinality/fallback dùng chung | BA chốt recipient matrix/resolver |
| 2FA channel | Email hay authenticator | BR-AUTH-01 và FR-VIII-20 | Không có context | Nguồn canonical = email, FR chưa sync | BA update SRS |
| 2FA resend | Cooldown/rate-limit/mã cũ | FR-VIII-20 | Không có context | SRS im lặng | BA + Security chốt |
| 2FA audit fail | Audit ở đâu/action nào | FR-VIII-20 Postconditions, FR-VIII-28 Inputs | Không có context | SRS tự lệch | BA chốt |
| TK UI columns | Ngày tạo/đăng nhập cuối | FR-VIII-15 Outputs, SCR-VIII-03 | Không có context | SRS tự lệch | BA chốt |
| Email normalization | Trim/lowercase/case-insensitive unique | FR-VIII-15, BR-AUTH-EMAIL-01 | Không có context | SRS chỉ ghi RFC + unique | BA chốt |
| Đổi email tài khoản | Màn hình/quyền/audit/xác minh | BR-AUTH-EMAIL-01, SCR-VIII-03 | Không có context | BR có nhắc, thiếu FR | BA bổ sung FR |
| Resend activation | Rate limit và token lifecycle | SCR-VIII-03, FR-VIII-26, FR-IV-07 | Không có context | Chỉ có action và rule rời rạc | BA chốt cross-account policy |
| Email template catalog | Subject/body/biến/link/header/file | INT-06, BR-NOTIF-01, MAU_PHAN_HOI | Không có context | Chưa có catalog kiểm thử được | BA bổ sung source truth |
| SMTP failure | Retry interval/rollback/DLQ | BR-EC-10/11, ERR-SLA-MAIL-01, FR-IV-07 | Không có context | Quy tắc phủ không đều | BA + Architect/Infra chốt |
| DT-007 | Approved hay all registrations | FR-III-04 EC-02, BR-NOTIF-01(5) | Không có context | SRS tự lệch | BA chốt |
| TVV wording | Chuỗi lỗi chuẩn | FR-IV-02 E7, FR-IV-11 E1, SCR-IV-02 | Không có context | SRS có 3 câu | BA chốt |
| TVV email sync | Có đồng bộ tài khoản | FR-IV-11, BR-AUTH-EMAIL-01 | Không có context | SRS không phủ TVV | BA chốt |
| DN Claim UX | Có ghi 30 phút | FR-VIII-26 | Không có context | TTL rõ, câu UX thiếu | BA chốt |

## Nội dung phát hiện nhưng không phải BA confirmation

| Nội dung | Kết luận audit | Việc đúng cần làm |
|---|---|---|
| `BA-CLAR-EM-TK-002` — câu trung tính hay báo khóa | Đã hợp nhất đầy đủ ở mục riêng phía trên. Không còn blocker: build R3 trả `ERR-PWD-02`, không sinh token/mail, khớp SRS E2; `BUG-EM-TK-013` đã Closed | Giữ làm lịch sử quyết định trong file tổng hợp; không chờ BA để retest tiếp |
| `EM-NOT-TVCS-05` gửi thừa email/in-app cho CG khi phê duyệt kết quả | SRS chỉ liệt kê DN ở bước phê duyệt; không phải câu hỏi BA | Nếu actual còn tái hiện, log bug recipient thừa. Citation: `srs-fr-12-tv-chuyen-sau.md:217-226` và `srs-v3.5.md:5745` |
| `EM-NOT-CT-01` thực tế gửi kết quả thẩm định cho chính CB NV trong khi SRS chỉ ghi TVV | Không phải khoảng trống expected; fixture thiếu `tu_van_vien_id` nên chưa kiểm được nhánh chuẩn | Dev/DBA cấp fixture có TVV; nếu vẫn gửi thêm CB NV thì log bug recipient thừa theo `srs-fr-06-chi-tra.md:758-790` |
| `EM-DN-UI-03` tooltip thiếu vế “sau đăng ký có thể đổi độc lập hai email” | SRS đã mô tả nội dung cần truyền đạt; đây là sai/thiếu copy UI nếu BA yêu cầu bám SCR, không phải câu hỏi nghiệp vụ mới | QA tách bug UI nếu bản mới vẫn thiếu; đối chiếu `srs-fr-10-quan-tri.md:1926` |
| `EM-NOT-HDD-01` email phân công không có link hồ sơ | SRS chỉ yêu cầu gửi thông báo cho cá nhân được phân công, không bắt buộc link; Expected của TC đang rộng hơn SRS | Sửa Expected/không log bug thiếu link; link chuẩn sẽ được chốt qua catalog template nếu BA bổ sung |
| `EM-DN-CLAIM-03` chưa có câu chữ riêng khi DN tồn tại nhưng email trống | SRS đã chốt phản hồi trung tính chống enumerate và actual đáp ứng; không cần BA để chấm hành vi bảo mật | Giữ Pass theo hành vi; chỉ thêm copy riêng nếu BA muốn chuẩn hóa qua catalog template |
| Ghi chú `EM-TK-ACT-09` nói SRS không có SLA 5 phút | Không chính xác: INT-06 là quy tắc cross-cutting, áp mọi UC có notification và chốt SLA gửi ≤5 phút | QA sửa ghi chú/Expected khi đồng bộ sổ; citation `srs-v3.5.md:739` |
| Lookup người đánh giá trả người khác đơn vị | SRS đã ghi “cùng đơn vị”; hiện mới quan sát lookup, chưa thử lưu | QA chạy negative chọn/lưu người khác đơn vị; nếu lưu được thì log bug. Citation: `srs-fr-08-danh-gia.md:264`, `:273-280` |
| API token thực tế khoảng 30 ngày trong `EM-TK-2FA-02` | SRS quy định API token 15 phút; đây là config/bug, không phải BA ambiguity | Dev/Infra kiểm cấu hình token; QA log/retest theo `srs-fr-10-quan-tri.md:938` và `srs-v3.5.md:5615` |
| 26 Blocked + 5 Not Run do mTLS/API key, SMTP stub, scheduled job, seed/time-travel | Blocker môi trường/setup, không phải BA spec | Infra/Dev cấp test hook/credential/fixture; BA chỉ điều phối nếu cần, không cần quyết expected |

## Workflow / Functional Coverage

| Nhóm | Tổng | PASS | FAIL | PARTIAL | BLOCKED/DEFER/SKIP | Chưa chạy | Ghi chú |
|---|---:|---:|---:|---:|---:|---:|---|
| File 01 — Tài khoản | 49 | 28 | 17 | 0 | 4 | 0 | Có 7 nhóm BA/spec liên quan 2FA, email tài khoản, resend và TK UI; nhiều Fail đã được bug R3 đóng nhưng TC chưa sync |
| File 02 — Doanh nghiệp | 29 | 19 | 6 | 0 | 4 | 0 | BA còn câu UX Claim; Blocked chính do integration/SMTP stub |
| File 03 — Workflow notification | 74 | 34 | 23 | 0 | 17 | 0 | DT-004, HDD-006, DT-007 và recipient resolver xuyên module cần xử lý/chốt; nhiều Fail đã Closed-verified |
| File 04 — SMTP/Security/NFR | 18 | 9 | 3 | 0 | 1 | 5 | Cần SMTP thật/stub, TLS log và test hook public API |

## TC/Path Chưa Hoàn Tất

| TC/path | Mục tiêu | Trạng thái | Nguyên nhân block | Điều kiện unblock | Phương án xử lý tiếp theo | Owner |
|---|---|---|---|---|---|---|
| `EM-NOT-DT-11` | Công bố kết quả | Chờ fix/retest | Dev đang chờ phản hồi đích nhận | BA phản hồi theo BA-EM-DT-004; Dev fix | Dựng đăng ký mới có `nguoi_dang_ky_id`, kiểm đúng TK email + mailbox âm HV | BA → Dev → QA |
| `EM-NOT-HDD-06/07` | SLA Quá hạn/nghiêm trọng | Chờ fix/retest | Chưa có bản fix + thiếu cardinality escalation | BA chốt cardinality/root-unit; Dev fix | Rerun cả hai mức và đúng phạm vi CB NV/CB PD/cấp trên | BA → Dev → QA |
| Nhóm TC gửi `CB PD/CB NV cùng đơn vị` | Fan-out đúng đối tượng | Chưa có oracle cardinality chung | SRS chưa định nghĩa resolver/cardinality/fallback | BA chốt BA-EM-RECIPIENT-RESOLVER-01 | Cập nhật recipient matrix rồi rerun mẫu ở Đào tạo, TVV, Đánh giá, Hỏi đáp, Chi trả, TVCS | BA/Dev/QA |
| `EM-TK-2FA-05` | Resend/rate-limit OTP | Blocked | Thiếu policy | BA + Security chốt | Cập nhật SRS/TC rồi rerun | BA/Security/QA |
| Email normalization + Đổi email TK | Unique/login/reset/workflow sau đổi email | Chưa có coverage đầy đủ | Thiếu rule chuẩn hóa và FR đổi email | BA chốt normalization + bổ sung FR | Bổ sung/rerun TC tạo, đổi, login, reset, audit và mailbox cũ/mới | BA/Dev/QA |
| `EM-TK-ACT-09` và các loại tài khoản | Gửi lại kích hoạt đúng link/token | Pass một phần, policy chưa chốt | Thiếu rate limit + token lifecycle cross-account | BA chốt BA-EM-ACT-RESEND-01 | Rerun DN self-register, TVV/NHT, account do QTHT tạo | BA/Dev/QA |
| Email template catalog | Nội dung/header/link/file từng sự kiện | Chưa có oracle tập trung | Thiếu catalog source truth | BA ban hành catalog | Mapping toàn bộ BR-NOTIF-01 + activation/reset/OTP/SLA vào TC | BA/QA |
| `EM-NOT-DT-07` | Hủy khóa có đăng ký | Blocked kép | SRS mâu thuẫn + không tạo được fixture | BA chốt recipient; Infra/Dev cấp đường tạo đăng ký | Rerun đủ DA_DUYET/CHO_DUYET/TU_CHOI | BA/Infra/QA |
| `EM-TK-ACT-06/07` | Link kích hoạt DN | TC docs còn Blocked lịch sử | Bug liên quan đã Closed nhưng chưa rerun TC | Fixture DN mới sau fix | Rerun và sync verdict | QA |
| `EM-DN-NOMAIL-03..05`, `EM-NOT-VV-01`, `EM-NOT-TVCS-08`, `EM-FLD-API-01..06`, `EM-INF-12` | Integration inbound/outbound | Blocked | mTLS/API key/OAuth/IP whitelist | Credential hoặc test hook hợp lệ | Chạy payload dương/âm và kiểm transaction/mailbox | Infra/Dev/QA |
| `EM-TK-ACT-11`, `EM-DN-CLAIM-04`, `EM-INF-04/05` | SMTP failure/retry/bounce | Blocked/Not Run | Không có SMTP fault injection | SMTP stub điều khiển 4xx/5xx/timeout/bounce | Rerun retry, rollback, alert QTHT | Infra/Dev/QA |
| `EM-NOT-HDD-04`, `EM-NOT-BC-01/02` | Scheduled/time-travel | Blocked | Không backdate/trigger job | Endpoint trigger/backdate hoặc DBA seed | Chạy đúng mốc và kiểm dedup/recipient | Dev/DBA/QA |
| `EM-NOT-CT-01/02/04/05`, `EM-NOT-DT-10` | Workflow cần seed đặc thù | Blocked | Dữ liệu sai trạng thái/trần hoặc pool đã dùng | Seed hồ sơ đúng state, TVV, hạn mức, đăng ký chờ duyệt | Rerun từng transition | Dev/DBA/QA |
| `EM-INF-01/02/03` | TLS, SLA delivery, render mail thật | Not Run | MailHog không cung cấp oracle | SMTP/mail client thật + log handshake | Chạy vòng mail thật | Infra/QA |

## Setup / Điều Kiện Cần Chuẩn Bị

| Nhóm setup | Áp dụng cho TC/path | Cần chuẩn bị cụ thể | Cách tạo/kiểm tra đề xuất | Owner | Sau khi xong rerun |
|---|---|---|---|---|---|
| Registration fixture | DT-004, DT-007, DT-10 | DN/NHT đăng ký qua đúng API, có `nguoi_dang_ky_id`, nhiều trạng thái | mTLS credential hoặc seed qua service chính thức | Dev/Infra/DBA | DT-004, DT-007, DT-10 |
| SLA escalation | HDD-006/HDD-04 | Hồ sơ cùng đơn vị có cha, CB PD cùng cấp và cấp trên có mailbox tách | Seed/backdate hoặc endpoint trigger job | Dev/DBA | HDD-04, HDD-06, HDD-07 |
| Integration auth | API/inbound paths | mTLS cert, OAuth consumer, API key, IP whitelist | Cấp credential UAT giới hạn scope hoặc test hook ký request | Infra | DN-NOMAIL, VV-01, TVCS-08, API-01..06, INF-12 |
| SMTP fault harness | Resilience paths | SMTP stub cấu hình fail/fail/success, hard fail và bounce | Container SMTP stub có log attempts/message-id | Infra/Dev | ACT-11, CLAIM-04, INF-04/05 |
| Mail thật | INF-01/02/03 | SMTP TLS thật, Gmail client, timestamp/log accepted | Môi trường UAT mail thật, đồng bộ clock | Infra/QA | INF-01/02/03 |

## Phương Án Để Hoàn Thành Full Luồng Chức Năng

| Mục tiêu hoàn tất | Việc cần làm tiếp | Loại blocker | Owner | Điều kiện xác nhận xong | TC/luồng được unblock |
|---|---|---|---|---|---|
| Gỡ 2 bug đang `Chờ BA` | BA phản hồi DT-004/HDD-006 theo nội dung Dạng A, chốt cardinality HDD | chờ BA phản hồi + chờ Dev fix | BA/Dev | Có phản hồi văn bản, build fix, R4/R5 Pass | DT-11, HDD-06/07 |
| Chốt recipient resolver xuyên module | Ban hành selector/cardinality/fallback cho `CB PD/CB NV cùng đơn vị` | chờ BA confirm spec | BA/Architect | Có recipient matrix dùng chung và TC xác định được số/người nhận | Notification workflow toàn module |
| Chốt chính sách 2FA | Đồng bộ kênh email, resend policy và audit fail | chờ BA confirm spec/security | BA/Security | SRS + TC được cập nhật, behavior có verdict | 2FA-01..05 |
| Chốt chính sách tài khoản/email | Email normalization, Đổi email TK, resend activation | chờ BA confirm spec/security | BA/Security | Có rule normalize, FR đổi email và token policy đầy đủ | Account validation/change/activation/reset |
| Chốt catalog và resilience email | Catalog template + retry/rollback/DLQ SMTP | chờ BA confirm spec/architecture | BA/Architect/Infra | Có source truth từng template và failure matrix từng loại email | Toàn bộ notification + INF-04/05 + ACT-11 + CLAIM-04 |
| Chốt các điểm dữ liệu/email phụ | DT-007, TVV wording/sync, DN Claim UX, TK columns | chờ BA confirm spec | BA | Source truth/câu chữ được cập nhật | DT-07, TVV-02/04/05, DN-CLAIM-01, TK-UI-01 |
| Gỡ blocker môi trường | Cấp mTLS/API key/stub/time-travel/seed | môi trường/setup | Infra/Dev/DBA | Các request vào được business routing và fixture đúng state | 26 Blocked + 5 Not Run theo nhóm trên |
| Đồng bộ sổ QA | Cập nhật 170 dòng TC theo evidence R3/R4 | report cũ/chưa đủ evidence | QA | Không còn Fail lịch sử trỏ bug đã Closed | Toàn suite |

## Tóm Tắt Cuối

- Trạng thái module: **Có điều kiện**.
- Full luồng chưa: **chưa full**, vì còn 2 bug chưa có bản fix để retest, 16 nội dung cần BA phản hồi/chốt và các blocker môi trường.
- Coverage hiện tại: 170 TC trong sổ; trạng thái thô 90 Pass, 49 Fail, 26 Blocked, 5 Not Run; cần sync lại sau 32 bug Closed-verified.
- Bug còn mở: 2 phiếu `BUG-EM-DT-004`, `BUG-EM-HDD-006`, đều đang `Chờ BA`/chờ fix.
- Blocker chính: đích/cardinality recipient, policy 2FA/activation/email account, template/SMTP failure matrix và mTLS/API key/time-travel fixture.
- Việc cần làm để full: BA phản hồi bảng P0 trước; Dev fix 2 bug; Infra/DBA cấp test hook và seed; QA rerun + đồng bộ TC.
- Sau khi xử lý xong cần rerun: `EM-NOT-DT-11`, `EM-NOT-HDD-06/07`, `EM-TK-2FA-01..05`, `EM-NOT-DT-07`, `EM-FLD-TVV-02/04/05`, `EM-DN-CLAIM-01` và toàn bộ nhóm integration/resilience còn Blocked.

**Kết luận full luồng:** Có điều kiện.

**Điều kiện tối thiểu để hoàn tất:** BA phản hồi 8 nội dung P0; Dev triển khai và QA Pass DT-004/HDD-006; BA/Security chốt 2FA + resend + SMTP; Infra cấp đường chạy các TC tích hợp/resilience P0; QA đồng bộ lại trạng thái suite.

**TC/path cần rerun sau khi unblock:** xem bảng `TC/Path Chưa Hoàn Tất` và danh sách trong Tóm Tắt Cuối.
