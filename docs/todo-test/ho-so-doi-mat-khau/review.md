# Review — Hồ sơ + Đổi MK test plan
**Reviewer:** agent-skills:code-reviewer
**Date:** 2026-05-12 12:35:00

## Gaps

- **G1. TC-14 "smoke 11 role" gộp scope với TC-01/TC-02 dẫn tới mơ hồ** (test-plan.md:200) — TC-01 đã verify QTHT xem 5 field, TC-02 verify 11 role read-only của `username/email/vaiTro`. TC-14 lại nói "11 role login + verify 5 field" → trùng với TC-02 + TC-03. Cần ghi rõ TC-14 chỉ cover "entry visible trên header dropdown + landing `/profile` không 403" (sub-smoke entry-point) thay vì lặp field verify.

- **G2. TC-10 multi-device invalidate KHÔNG có bước verify access token bị revoke server-side** (test-plan.md:196) — `ho-so-doi-mat-khau.md:25` nói "auto đăng xuất các phiên đăng nhập trên thiết bị khác". Plan chỉ verify session 2 incognito bị invalidate qua UI (redirect /login). Thiếu: (a) timing — invalidate ngay tức thì hay lag, (b) verify qua `list_network_requests` thấy 401 ở session 2 khi gọi `/api/v1/auth/me` sau đổi MK, (c) verify session đổi MK (session 1) KHÔNG bị invalidate. Memory `qa_htpldn_jwt_revoke_aggressive` lưu pattern BE revoke JWT ~2 phút bất chấp `exp` — TC-10 cần bypass quirk này.

- **G3. Rule MK conflict (Mâu thuẫn 1) defer BA nhưng chưa có TC parameterize** (test-plan.md:233) — Plan note "tạm theo rule profile 4 thành phần". Nếu BA chốt 5 thành phần (thêm ký tự đặc biệt), TC-07 phải re-design. Đề xuất: thêm 1 dòng "**Nếu BA chốt 5 thành phần → TC-07 thêm sub-case `Abc12345` (thiếu ký tự đặc biệt) → expect FAIL**" để khi nhận quyết định BA, không phải viết lại plan.

- **G4. Thiếu TC verify tab Bảo mật cho 11 role × 2 loại TK (LOCAL vs VNeID)** — TC-11 chỉ cover VNeID disable nhưng không nói TEST trên role/account nào cụ thể. CB nội bộ (QTHT/CB_NV/CB_PD) **luôn LOCAL** theo `users.csv`, KHÔNG có VNeID. Chỉ DN/NHT/TVV/CG có thể LOAI_DK = VNEID. Cần ghi rõ TC-11 áp dụng cho 4 role này, role còn lại không có TC tương ứng vì N/A theo nature account.

- **G5. TC-12 cross-user 403 chưa nói rõ endpoint** (test-plan.md:198) — Plan ghi `/api/v1/profile/{user_B_id}` nhưng SRS không có endpoint dedicated cho profile. SRS `srs-fr-10-quan-tri.md:1952-1964` chỉ có entity TAI_KHOAN, không có URL pattern. Cần check thực tế qua `list_network_requests` khi load `/profile` để biết endpoint thật (có thể là `/api/v1/auth/me` / `/api/v1/users/me` / `/api/v1/tai-khoans/{id}`). Plan đoán endpoint = false positive risk.

- **G6. Avatar field test (TC-02 hint, §2.4) chưa có TC dedicated** (test-plan.md:127) — Plan list avatar trong UI Layout proposed nhưng KHÔNG có TC nào test upload/delete/format/size avatar. Nếu BA confirm có avatar → cần TC mới (positive upload PNG/JPG, negative format SVG/exe, size max). Nếu BA bỏ → xóa khỏi §2.4 luôn. Hiện trạng "đề xuất nhưng không test" là không complete.

- **G7. Permission matrix §2.3 chưa cover "Đổi MK Self khi đang TAM_KHOA"** — `TAI_KHOAN.trang_thai` có state TAM_KHOA (line 148). User TAM_KHOA login được không? Nếu được, có đổi MK được không? Spec không nói. Cần thêm 1 TC negative hoặc note "block phải có BA quyết".

- **G8. TC-13 AUDIT_LOG verify cách query không cụ thể** (test-plan.md:199) — "Query AUDIT_LOG row" — qua endpoint API hay direct DB? QA không có DB access theo convention. Nếu API → endpoint nào? `srs-v3/srs-v3.md:3976` chỉ nói BR có audit log, không nói cách verify. Cần đẩy thành "verify qua endpoint admin (nếu QTHT có UI Audit log viewer)" hoặc defer Nhóm F (DB-level only).

## Suggestions

- **S1. Thêm Bảng 1 + Bảng 2 (snapshot TC + nguyên nhân block)** theo rule project enforced 2026-05-10 — ngay sau Verdict §5. Bảng hiện trống vì plan chưa run, nhưng cấu trúc bảng phải có sẵn (skeleton 14 dòng TC). Tester sau handoff sẽ fill round phát hiện + status.

- **S2. Tách TC-04 thành 3 sub-case rõ ràng** (hoTen empty, hoTen >200, hoTen XSS) — hiện gộp 3 negative vào 1 TC, fail 1 sub không phân biệt được. Mỗi sub = 1 ERR code riêng → 3 TC con TC-04a/b/c hoặc 1 TC có 3 step độc lập.

- **S3. Thêm TC verify "đổi MK xong cũ KHÔNG login được"** (positive negative pair với TC-06) — TC-06 verify "MK mới login được". Cần TC-06b verify "MK cũ login → fail ERR-AUTH-INVALID-CRED". Đây là acceptance critical cho BR-AUTH-PWD-04 thực sự đổi MK trong DB, không phải chỉ "echo success".

- **S4. Đánh dấu rõ Nhóm A-F nguyên nhân block cho mỗi TC defer/block** trong Bảng 2 — vd TC-13 = Nhóm F (DB-level), TC-11 VNeID = Nhóm A (thiếu seed VNeID account), TC-07 5-thành-phần = Nhóm C (chờ BA confirm). Theo template `output/template/tc-block-classification-template.md`.

- **S5. Bổ sung cross-ref `output/permission-matrix.md` chính thức** §1.3 — plan tự inferred permission từ BR-AUTH-11. Cần grep file matrix xem có entry "Hồ sơ cá nhân" cho 11 role chưa. Nếu chưa → action update matrix là task song song trước run TC.

- **S6. TC-11 VNeID — thêm bước precondition seed account VNeID** — Plan note line 165 "gap nếu chưa có (cần seed FR-VIII-25)". Cần ghi explicit: TC-11 phụ thuộc R7.2.X (seed VNeID account NHT/DN/TVV) — nếu chưa có thì TC-11 block Nhóm A. Format `[need: ≥1 VNeID account state HOAT_DONG]` theo CLAUDE.md state marker workflow.

- **S7. Đổi label "Mật khẩu mới không trùng MK hiện tại" (ERR-PWD-PROFILE-04)** từ "proposed extra" sang "TC defer BA confirm" — đây không phải spec rule, là ý tưởng QA. Nếu BA không confirm → bỏ TC này, không cần log bug. Hiện ngôn ngữ "proposed extra" mơ hồ.

- **S8. Bổ sung TC verify timeout/rate-limit khi đổi MK liên tục** — Edge case: user đổi MK 5 lần trong 1 phút → BE có rate limit không? Spec không nói. Defer Nhóm C BA, nhưng plan nên list để không miss.

## Verdict

**REVISE** — Plan có structure tốt + cite SRS line đúng + cover BR/Permission/Error code đầy đủ cho scope đã định. Tuy nhiên 8 gap (G1-G8) cần fix trước khi viết TC detail: trùng scope TC-14 vs TC-02, thiếu test rule MK 5-thành-phần parameterize cho rủi ro BA flip, endpoint cross-user đoán không verify, avatar half-implemented, AUDIT_LOG verify method mơ hồ. 6 open issue BA confirm (§5) là blocker cứng — không thể RUN plan đến khi BA quyết. Re-review sau khi: (a) fix 8 gap + 8 suggestion áp dụng, (b) nhận BA decision 6 mâu thuẫn, (c) thêm 2 bảng skeleton theo template project.
