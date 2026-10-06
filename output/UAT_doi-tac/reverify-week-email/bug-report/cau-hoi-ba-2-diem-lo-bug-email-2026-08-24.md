# Phiếu hỏi BA — 2 điểm chặn của lô 33 bug Email (UAT reverify email)

**Ngày:** 24/08/2026 · **Liên quan:** lô 33 bug tại `my_local/bug-email-report/` (10 file QA, env DEV 120 V1.0.15 + MailHog) · Checklist thẩm định: [`../CHECKLIST-BUG-EMAIL-2026-08-24.md`](../CHECKLIST-BUG-EMAIL-2026-08-24.md)
**Người hỏi:** Dev · **Cổng kích hoạt:** `QUY-TRINH-FIX-BUG.md` §*Cổng confirm* — điểm 1 thuộc trường hợp *SRS mâu thuẫn với chuẩn bảo mật/hành vi chủ đích của code*; điểm 2 thuộc trường hợp *SRS thiếu đặc tả chi tiết cần thiết để fix*.
**Trạng thái:** ⏳ **CHỜ BA** — 2 phiếu bug tương ứng (`BUG-EM-TK-013`, `BUG-EM-HDD-006`) đang treo `[!]` trong checklist, KHÔNG code cho tới khi chốt.

> Bối cảnh chung: lô 33 bug đã thẩm định xong (2 lượt đối chiếu SRS + 2 lượt truy code + Codex second-opinion). 31/33 bug có hướng fix tự suy đủ từ SRS v3.5 và sẽ triển khai không chờ phiếu này. Chỉ 2 điểm dưới đây là SRS hoặc bỏ trống, hoặc xung đột với hành vi chủ đích của hệ thống.

---

## ĐIỂM 1 — BUG-EM-TK-013: Quên mật khẩu với tài khoản Tạm khóa / Vô hiệu hóa — theo SRS E2 hay giữ phương án trung tính?

### 1.1 Vấn đề

SRS FR-VIII-26 §Error Handling **E2** (`srs-fr-10-quan-tri.md:1341`) quy định:

> Tài khoản đang TAM_KHOA hoặc VO_HIEU_HOA | `ERR-PWD-02` | *"Tài khoản đã bị khóa hoặc vô hiệu hóa. Liên hệ quản trị viên để được hỗ trợ"* | ERROR

kèm Preconditions `:1298` (*"tài khoản tương ứng không ở TAM_KHOA/VO_HIEU_HOA"*) và gate bước 4a `:1319`.

Code hiện hành **chủ đích làm khác** (không phải quên):

| Trạng thái TK | Hành vi hiện tại | Nguồn code |
|---|---|---|
| `TAM_KHOA` | **Vẫn cho reset**: sinh token + gửi thư; reset xong **tự mở khóa** TAM_KHOA → HOAT_DONG (comment code gọi là *"lock-out self-recovery"*) | `auth/workflow/auth.workflow.ts:47-50` (eligible-set có TAM_KHOA) + `:60-66` (`deriveTrangThaiAfterReset`) + `auth.service.ts:927` |
| `VO_HIEU_HOA` | Trả **200 trung tính** (*"Nếu tài khoản tồn tại, link đặt lại mật khẩu đã được gửi"*), không token, không thư | `auth.service.ts:744-747` (`ANTI_ENUM_RESPONSE`) |

QA đo đúng hiện tượng này (phiếu `BUG-EM-TK-013`, bug-report-em-tk.md): cả hai nhánh không ra `ERR-PWD-02`; nhánh TAM_KHOA còn gửi thư reset thật.

### 1.2 Phân tích xung đột (đã thẩm định)

- **SRS nội tại KHÔNG mâu thuẫn**: nguyên tắc trả lời trung tính (chống dò tài khoản) trong SRS chỉ áp cho tình huống **tài khoản không tồn tại** (E1/ERR-PWD-01, bước 4b/4c, AC `:1362`, E.J `srs-v3.5.md:6911`). Với TAM_KHOA/VO_HIEU_HOA, SRS chủ động chọn báo tường minh E2. → Theo SRS hiện hành, QA log đúng.
- **Nhưng E2 tường minh tự nó tiết lộ**: tài khoản tồn tại + đang bị khóa (leak nhẹ so với khuyến nghị OWASP về forgot-password). Hiện trạng "trung tính mọi nhánh" về bảo mật **tốt hơn** SRS.
- **Fix đúng SRS sẽ phá kênh self-recovery**: người dùng bị tạm khóa (ví dụ nhập sai mật khẩu quá số lần) hiện tự thoát bằng quên-mật-khẩu; nếu chặn bằng ERR-PWD-02 thì mọi ca tạm khóa phải qua QTHT mở khóa tay.
- Codex (second-opinion độc lập) cũng kết luận: *NEEDS_BA_DECISION — BA/security phải chọn giữa SRS compliance và chính sách an toàn hơn hiện tại, rồi sửa code hoặc sửa SRS cho nhất quán.*

### 1.3 Hai phương án

**Phương án A — Sửa code theo đúng SRS E2** *(tuân thủ đặc tả)*
- Thêm nhánh chặn TAM_KHOA/VO_HIEU_HOA trả `ERR-PWD-02` tường minh; bỏ TAM_KHOA khỏi eligible-set; bỏ auto-unlock sau reset.
- Được: khớp SRS 100%, QA đóng phiếu ngay.
- Mất: lộ trạng thái tài khoản cho người ngoài; mất self-recovery (tăng việc cho QTHT); đổi hành vi một luồng auth đang chạy ổn trên mọi env.

**Phương án B — Giữ hành vi hiện tại, sửa SRS E2** *(Dev đề xuất)*
- SRS sửa E2 thành: TAM_KHOA/VO_HIEU_HOA cũng trả câu trung tính như tài khoản không tồn tại; bổ sung đặc tả kênh self-recovery TAM_KHOA (reset xong tự mở khóa) — hiện code có mà SRS chưa ghi.
- Được: giữ chuẩn chống dò tài khoản + giữ self-recovery; không đụng code auth.
- Mất: cần BA sửa SRS + QA cập nhật testcase; riêng vế "VO_HIEU_HOA im lặng nhưng UI báo *đã gửi*" nên cân nhắc giữ nguyên câu trung tính (đúng bản chất anti-enum) — QA đóng phiếu theo SRS bản mới.

**Câu hỏi cho BA:** chọn **A** hay **B**? Nếu B: xác nhận luôn 2 ý — (i) câu trung tính áp cho cả TAM_KHOA/VO_HIEU_HOA, (ii) self-recovery TAM_KHOA→HOAT_DONG sau reset là hành vi chính thức được ghi vào SRS.

---

## ĐIỂM 2 — BUG-EM-HDD-006: Đích "escalate" của cảnh báo SLA Hỏi đáp mức Quá hạn nghiêm trọng là ai?

### 2.1 Vấn đề

Bug đã xác nhận (không tranh cãi phần này): cron SLA hỏi đáp hiện chỉ gửi cảnh báo cho **người xử lý**; SRS đòi thêm CB Phê duyệt ở 2 mức quá hạn:

> `srs-fr-02-hoi-dap.md:985`: QUA_HAN → *"Thông báo CB NV + CB PD"*
> `:986`: QUA_HAN_NGHIEM_TRONG → *"Thông báo CB NV + CB PD **+ escalate**"*
> `:976` (bước 6), `:1188` (bảng thông báo), `:1658` (BR-SLA-03) — lặp lại cùng yêu cầu.

Root cause code: `hoi-dap-sla-check.processor.ts:298-317` — `buildRecipients` chỉ trả `nguoiPhanCongId` + `nguoiDuyetId` (một cá nhân từng duyệt, có thể null), không fan-out nhóm CB PD, không có nhánh escalate.

**Chỗ SRS bỏ trống:** toàn bộ nhóm Hỏi đáp chỉ viết chữ **"escalate"** trần — không nói escalate **tới ai, đơn vị nào, vai trò nào**. Đối chiếu: nhóm Vụ việc có đặc tả đầy đủ (`srs-fr-05-vu-viec.md:2460` BR-SLA-03: *"QUA_HAN_NGHIEM_TRONG → CB NV + CB PD + escalate **cấp trên**"*). Đây là chỗ duy nhất trong lô 33 bug mà SRS thật sự thiếu đặc tả.

### 2.2 Bằng chứng QA (phiếu BUG-EM-HDD-006, đã re-test 24/08 tái hiện)

6 lần chuyển mức / 3 hồ sơ / 2 đơn vị trong ngày 21/08: 6/6 thư chỉ đến người xử lý; `cbpd_tw_01`, `cbpd_bn_01` không nhận thư lẫn thông báo trong ứng dụng; không có gì đi lên đơn vị cấp trên (Bộ KH&ĐT → Cục Bổ trợ tư pháp có 6 CB PD TW hoạt động, 0 người nhận).

### 2.3 Phương án đề xuất

**Phương án A — Mirror nhóm Vụ việc** *(Dev đề xuất)*: escalate = **CB Phê duyệt của đơn vị cấp trên trực tiếp** (theo cây đơn vị), kênh in-app + email, có dedup 24h như cơ chế hiện hành. Đơn vị không có cấp trên (Trung ương) → không escalate thêm, chỉ CB NV + CB PD cùng đơn vị.

**Phương án B — Đích khác do BA chỉ định** (ví dụ: lãnh đạo đơn vị hiện tại, hoặc QTHT, hoặc một vai trò khác).

**Câu hỏi cho BA:** chốt đích escalate của Hỏi đáp (A hay B-cụ-thể-là-ai), và xác nhận đơn vị Trung ương không có cấp trên thì xử lý như đề xuất. Sau khi chốt, Dev fix trọn phiếu HDD-006 trong 1 commit (cả vế CB PD cùng đơn vị + vế escalate) và đề nghị BA bổ sung câu đặc tả tương ứng vào `srs-fr-02-hoi-dap.md` để đồng bộ với nhóm V.I.

---

## PHẦN ĐỂ-BIẾT (không cần trả lời — Dev code ngay theo SRS, báo trước để tránh bất ngờ)

3 quyết định fix dưới đây tự suy đủ từ SRS hiện hành, nêu để BA phản hồi **chỉ khi thấy khác ý**:

1. **BUG-EM-TVCS-001** — Sẽ **gỡ quyền `approve_noi_dung_tu_van_cs` khỏi 3 vai CB_NV_TW/BN/DP** (seed `role-permissions.map.ts:255/545/832`) + migration backfill `vai_tro_quyen_han` cho env đã seed. Căn cứ: `srs-fr-12:1183` — nút [Phê duyệt]/[Từ chối] ở CHO_PHE_DUYET chỉ dành cho *"CB Phê duyệt cùng đơn vị"*; `:244` chặn cả CB NV/CG ở thao tác hủy `[QLNDTVVCG_36 chốt 24/07]`. Lưu ý: đây là **đổi phân quyền thật** (CB NV hiện đang duyệt được TVCS qua API), không riêng thông báo.
2. **BUG-EM-DT-004** — Email "KQ đào tạo đã có" gửi về **email tài khoản người đã đăng ký học viên** (`nguoiDangKyId` — TK doanh nghiệp/NHT), đúng nguyên văn `srs-fr-03-dao-tao.md:1433`; học viên không có người đăng ký → ghi cảnh báo nhật ký, không chặn luồng (điều khoản BR-NOTIF-01); không gửi bản riêng cho học viên.
3. **BUG-EM-DT-003** — Khai giảng khóa học: giảng viên/học viên **không có tài khoản** nhận qua **email liên hệ** (`giang_vien.email` / `hoc_vien.email`) theo điều khoản BR-NOTIF-01 "bên nhận chưa có tài khoản → chỉ gửi thư điện tử" (điều khoản viết ví dụ *"điển hình"* cho DN nhóm TVCS — áp suy rộng theo đúng chữ "điển hình").

---

## Tác động khi chưa chốt

- 31/33 bug của lô vẫn triển khai bình thường, không phụ thuộc phiếu này.
- 2 phiếu `BUG-EM-TK-013` + `BUG-EM-HDD-006` giữ trạng thái Open phía QA cho tới khi BA chốt và Dev fix xong; nếu QA cần cập nhật sổ, ghi chú "đang chờ BA confirm — phiếu 24/08".

*Phiếu lập: 24/08/2026 — Dev (Claude Code) · Nguồn thẩm định: checklist lô bug email + Codex second-opinion session `01a032d5-4ac9`*
