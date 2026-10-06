# Bảng đối chiếu điều kiện — PDHSTVV_08

**Evidence đã xem:** `partner-evidence/PDHSTVV_08.webm` → frames `reverify-audit/PDHSTVV_08/frames/`
- f001-f006: CB_PD_TW mở TVV-BTP-TW-0046 "TVV BUG dup test" (Chờ phê duyệt) → bấm "Từ chối" → hộp thoại "Từ chối hồ sơ TVV" → nhập lý do (có báo lỗi khi lý do quá ngắn) → bấm "Xác nhận từ chối".
- f007 (00:19): toast **"Đã từ chối hồ sơ TVV"**, hồ sơ chuyển badge **"Từ chối"**.
- f013 (00:37) — **frame chứa LỖI**: đối tác đăng nhập lại bằng **CB_NV_TW**, mở chuông Thông báo → danh sách chỉ có "Tài khoản vừa đăng nhập ở nơi khác" + "Hồ sơ TVV đã được bổ sung", **không có thông báo nào về việc hồ sơ bị từ chối**.

**Đối tác phản ánh cụ thể:** "Hệ thống không gửi thông báo đến **Cán bộ nghiệp vụ đã thẩm định**" (Kết quả mong đợi của case: gửi thông báo đến CB nghiệp vụ đã thẩm định **và Người hỗ trợ là chủ hồ sơ** kèm lý do).

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_PD_TW từ chối; kiểm thông báo bằng CB_NV_TW | cbpd_tw (CB_PD_TW) từ chối; kiểm thông báo bằng cbnv_tw (CB_NV_TW — chính là tài khoản đã thẩm định hồ sơ này) + kiểm hộp thư chủ hồ sơ | Không |
| Entity + trạng thái (state machine) | TVV-BTP-TW-0046 cấp TW, trạng thái **Chờ phê duyệt** trước thao tác | TVV-BTP-TW-0007 "QA TVV PheDuyet W2 B" cấp TW (BTP), trạng thái **Chờ phê duyệt** trước thao tác | Không |
| Input / giá trị nhập | Lý do từ chối hợp lệ (≥10 ký tự) | Lý do từ chối hợp lệ 83 ký tự: "Ho so thieu bang cap goc va the hanh nghe khong con hieu luc - QA verify PDHSTVV_08" | Không |

**Kết quả verify trên web (cbpd_tw):**
- Toast **"Đã từ chối hồ sơ TVV"**, hồ sơ chuyển **"Từ chối"** → khớp đối tác.
- Hồ sơ **CÓ ghi nhận** người từ chối + thời điểm + lý do (`nguoiDuyetId`, `ngayDuyet=2026-07-12T10:38:37`, `ghiChuPheDuyet` = đúng lý do đã nhập) → phần "ghi nhận vào hồ sơ" của case ĐẠT.
- **Chủ hồ sơ KHÔNG nhận được thông báo nào:** MailHog (115 mail) **không có mail nào** gửi tới `qa.tvv.pheduyet.b@htpldn.test` sau thao tác từ chối. Đối chứng cùng phiên: khi **phê duyệt** TVV-BTP-TW-0006 thì chủ hồ sơ **CÓ** nhận mail ngay (10:33:18) ⇒ kênh mail hoạt động bình thường, **chỉ luồng TỪ CHỐI là không gửi**. → **vi phạm SRS** (xem dưới) → **Open**.
- **CB NV đã thẩm định KHÔNG nhận thông báo:** unread giữ nguyên **58**, không có mục mới → khớp quan sát đối tác. Nhưng **SRS FR-IV-07 không yêu cầu** thông báo cho CB NV ở bước phê duyệt/từ chối → ý này không phải lỗi theo SRS, cần BA chốt nếu muốn bổ sung.

**SRS:**
- FR-IV-07 (UC45) §Processing bước 4 (`srs-fr-04-chuyen-gia-tvv.md` dòng 593): "**Gửi thông báo TVV/CG (chủ hồ sơ) qua email đã khai**" — áp dụng cho cả nhánh PHE_DUYET và TU_CHOI.
- FR-IV-07 §Acceptance Criteria (dòng 627): "**Given** CB PD từ chối **When** nhập lý do **Then** TVV → TU_CHOI, **gửi thông báo TVV/CG (chủ hồ sơ)**".
- SCR-IV-03 §3.0b MD-TU-CHOI (dòng 1398): "Vui lòng nhập lý do (tối thiểu 10 ký tự) — **lý do sẽ được gửi đến chủ hồ sơ**".

**Verdict:** `Open` (≥1 ý Open — chủ hồ sơ không nhận thông báo từ chối, trái SRS dòng 593/627/1398. Ý "CB NV không nhận thông báo" đúng như đối tác quan sát nhưng SRS không quy định → tách sang BA confirm).

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data của bug gốc (0 GAP):

| Điều kiện có thể đổi kết quả | Bug gốc (bug-report) | Mình test (re-verify) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_PD_TW từ chối; kiểm hộp thư chủ hồ sơ | cbpd_tw (CB_PD_TW) từ chối; kiểm hộp thư chủ hồ sơ + đối chứng nhánh phê duyệt | Không |
| Entity + trạng thái | Hồ sơ TVV cấp TW (BTP), trạng thái **Chờ phê duyệt** trước thao tác | TVV-BTP-TW-0012 "QA TVV RVPD08 Reject" cấp TW (BTP), trạng thái **Chờ phê duyệt** (tự seed: tạo mới → thẩm định ĐẠT → trình duyệt) | Không |
| Input / giá trị nhập | Lý do từ chối hợp lệ (≥10 ký tự) | Lý do từ chối hợp lệ 98 ký tự | Không |

**Kết quả re-verify (cbpd_tw):**
- Bấm "Từ chối" + lý do 98 ký tự → "Xác nhận từ chối": toast **"Đã từ chối hồ sơ TVV"**, hồ sơ chuyển **"Từ chối"** ✅.
- **Chủ hồ sơ VẪN KHÔNG nhận mail:** hộp thư `qa.tvv.rvpd08@htpldn.test` **0 mail** sau thao tác từ chối (chờ >9s).
- **Đối chứng cùng phiên (chứng minh kênh mail hoạt động):** phê duyệt hồ sơ khác `TVV-BTP-TW-0013` (email `qa.tvv.rvpd08.approve@htpldn.test`) → chủ hồ sơ **NHẬN** mail "Hồ sơ TVV đã được phê duyệt — kích hoạt tài khoản" trong vài giây. ⇒ kênh gửi mail hoạt động bình thường, **riêng nhánh TỪ CHỐI vẫn không gửi mail cho chủ hồ sơ** — y hệt bug gốc.
- Ảnh: `bug-reports/image/PDHSTVV_08-reverify-mailhog-chi-co-mail-pheduyet-khong-co-mail-tuchoi.png` (tìm "qa.tvv.rvpd08" chỉ ra đúng 1 mail — mail phê duyệt; không có mail từ chối) + `bug-reports/image/PDHSTVV_08-reverify-web-hoso-da-tu-choi.png`.

**Verdict re-verify:** `Reopen` — nhánh từ chối vẫn không gửi thông báo kèm lý do cho chủ hồ sơ, trái SRS dòng 593/627/1398.
