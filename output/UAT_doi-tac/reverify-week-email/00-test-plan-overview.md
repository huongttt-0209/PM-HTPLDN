# Test Plan — Reverify luồng Email PM HTPLDN

> Nguồn: LOCAL SRS v3.5 — `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5`  
> Ngày tạo: 2026-08-12

## 1. Đánh giá template

Template `output/template/test-case-template.md` dùng được làm nền vì đã có TraceID, tiền đề, dữ liệu, bước và Expected theo STATE/UI/PERSIST. Bộ email bổ sung các cột: Priority, actor, điểm bắt đầu luồng, nguồn địa chỉ nhận, Expected To/CC, mailbox âm, oracle UI/API/queue/SMTP/audit, cleanup, evidence, trạng thái và Bug ID. Không yêu cầu quyền DB; không Pass chỉ vì nhìn thấy một email trong inbox.

## 2. Cấu trúc bộ test

- `01-TC-email-tai-khoan.md`: validation, cấp/kích hoạt TK, reset, đổi email, 2FA.
- `02-TC-email-doanh-nghiep.md`: email liên hệ, self-registration, các luồng không gửi mail, Claim Flow.
- `03-TC-email-notification-workflow.md`: trigger nghiệp vụ theo từng module/state transition.
- `04-TC-email-smtp-security-nfr.md`: SMTP/TLS, SLA, retry, dedupe, XSS, PII, bulk và isolation.
- `05-traceability-matrix.md`: ánh xạ requirement → testcase.
- `06-test-data-and-environment.md`: dữ liệu/mailbox/fault injection.
- `07-dev-email-account-setup.md`: mapping đã áp dụng trên DEV và đúng các mục còn cần dev xử lý.
- `08-prompt-run-email-test-new-session.md`: prompt master + cách chia batch để chạy ở session mới không vỡ context.
- `UAT-Email-Reverify-Test-Suite.xlsx`: workbook thực thi và ghi kết quả.

## 3. Entry criteria

1. UAT build/deployment version được ghi nhận.
2. Có quyền truy cập UI, API ứng dụng và Gmail thật. Email queue, SMTP log và audit chỉ là oracle bổ sung khi môi trường cho phép.
3. Clock ứng dụng/Gmail/SMTP đồng bộ; các testcase fault-injection chỉ chạy khi có khả năng giả lập thời gian/token và SMTP 4xx/5xx/timeout/bounce.
4. Mapping account/email trong file 07 đã được áp dụng và đọc lại trên DEV. Ba case escalation dùng hồ sơ Bộ/ngành và đối soát recipient theo role `CB_PD_TW` + `don_vi_cha_id`; trước khi chạy phải map mọi tài khoản có thể được resolver chọn sang alias Gmail thật.
5. Phải đăng nhập được hộp thư `diupt01@gmail.com`; mọi OTP và email thông báo DEV được kiểm trực tiếp trong Gmail bằng query `to:<alias>`. Mỗi TC tạo TK/đăng ký/token/claim dùng `PATTERN_TC`, MST riêng hoặc cleanup rõ ràng.

## 4. Quy tắc Pass/Fail/Blocked

- **Pass**: mọi Expected theo bước đều đạt qua UI/API/Gmail; đúng người nhận, đúng chuông nếu SRS yêu cầu in-app, mailbox/tài khoản âm không nhận hoặc không nhìn thấy; không có side effect ngoài dự kiến. Queue/SMTP/audit chỉ đối chiếu khi có quyền.
- **Fail**: ít nhất một expected có căn cứ SRS không đạt, kể cả email đã tới inbox nhưng state, nội dung, recipient, count, audit hoặc SLA sai.
- **Blocked**: SRS chưa chốt tiêu chí hoặc môi trường không cung cấp oracle bắt buộc; tuyệt đối không đổi thành Pass.
- **Not Run**: chưa thực hiện.

## 5. Exit criteria

1. 100% P0 đã Run và Pass; không còn P0 Fail/Blocked, trừ blocker BA được chấp nhận bằng văn bản.
2. 100% requirement trong ma trận có ít nhất một TC và đã Run.
3. Không còn lỗi gửi nhầm, gửi chéo đơn vị, gửi trùng, token dùng lại, PII/XSS hoặc sai nguồn email.
4. Email delivery ≤5 phút; failure/retry/alert đã kiểm chứng.

## 6. SRS blockers không được Pass oan

1. 2FA: BR-AUTH-01 canonical đã được CĐT xác nhận và ghi mã qua email, trong khi FR-VIII-20 vẫn ghi ứng dụng xác thực. Chờ BA sửa nguồn lệch. EM-TK-2FA-01 kiểm bắt buộc có yếu tố thứ hai nhưng không chấm kênh; EM-TK-2FA-02/03/04 chấm hành vi mã/session; build thiếu 2FA là Fail nếu chưa có quyết định BA bằng văn bản. EM-TK-2FA-05 là kiểm tra bảo mật `[NGOÀI SRS]`.
2. QTHT đổi email tài khoản qua FR-VIII-15/SCR-VIII-03 và xem JSON diff trên FR-VIII-28/SCR-VIII-10 đủ đường chạy cho CHG-01..06. Chỉ nhánh self-service của chủ tài khoản chưa có FR/SCR.
3. SCR có hành động gửi lại email kích hoạt và token một lần cho phép chạy lõi EM-TK-ACT-09; số lượng thư, rate-limit và UI message vẫn là observation ngoài SRS.
4. Lịch retry giữa các module chưa thống nhất.
5. Khi chỉ dùng Gmail thật, phải bảo đảm mọi `CB_PD_TW` có thể được resolver escalation chọn đều đã map sang alias nhận được tại `diupt01@gmail.com`.

## 7. Quy ước ID

Các ID `EM-TK-VAL-11`, `EM-TK-VAL-12`, `EM-INF-14`, `EM-INF-16`, `EM-INF-17` không được khai báo trong source generator và hiện không đại diện testcase nào; đây là khoảng ID chưa sử dụng, không phải lỗi sinh thiếu testcase.
