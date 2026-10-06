# Bảng đối chiếu điều kiện — PDHSTVV_06

**Evidence đã xem:** `partner-evidence/PDHSTVV_06.webm` → frames `reverify-audit/PDHSTVV_06/frames/`
- f011-f016: CB_PD_TW mở TVV "Nguyễn Văn Tư Vấn 15" (Chờ phê duyệt) → hộp thoại "Xác nhận phê duyệt" → nhập số QĐ **`QĐ-123/QĐ-BTP`** (hợp lệ) + ý kiến → bấm Phê duyệt.
- f017-f018 — **frame chứa LỖI (theo đối tác)**: toast **"Phê duyệt TVV thành công"**, hồ sơ chuyển badge **"Chờ kích hoạt tài khoản"** (đối tác kỳ vọng "Đang hoạt động").
- f028-f029: đối tác đăng xuất, đăng nhập lại bằng tài khoản **CB_NV_TW** (`cbn***@htpldn.gov.vn`) → mở chuông Thông báo → danh sách chỉ có "Tài khoản vừa đăng nhập ở nơi khác" + "Hồ sơ TVV đã được bổ sung", **không có thông báo nào về việc công nhận TVV**.

**Đối tác phản ánh cụ thể (3 ý):** (a) trạng thái sau duyệt là "Chờ kích hoạt tài khoản" chứ không phải "Đang hoạt động"; (b) không gửi thông báo đến chủ hồ sơ; (c) thông báo hiển thị không giống thiết kế ("Đã công nhận tư vấn viên").

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Cán bộ PD Trung ương (CB_PD_TW) thực hiện duyệt; kiểm thông báo bằng CB_NV_TW | cbpd_tw (CB_PD_TW) thực hiện duyệt; kiểm thông báo bằng cbnv_tw (CB_NV_TW — chính là người đã thẩm định hồ sơ) | Không |
| Entity + trạng thái (state machine) | TVV "Nguyễn Văn Tư Vấn 15" cấp TW, trạng thái **Chờ phê duyệt** trước thao tác | TVV-BTP-TW-0006 "QA TVV PheDuyet W2 A" cấp TW (BTP), trạng thái **Chờ phê duyệt** trước thao tác (đã seed qua thẩm định → trình duyệt) | Không |
| Input / giá trị nhập | Số quyết định **hợp lệ** `QĐ-123/QĐ-BTP` + ý kiến phê duyệt | Số quyết định **`QĐ-123/QĐ-BTP`** (y hệt) + ý kiến "QA verify PDHSTVV_06 - phe duyet hop le" | Không |

**Kết quả verify trên web (cbpd_tw):**
- Toast (bắt bằng MutationObserver): **"Phê duyệt TVV thành công"**.
- Trạng thái hồ sơ → **"Chờ kích hoạt tài khoản"**; Ngày công nhận 12/07/2026 được ghi nhận.
- **Thông báo tới chủ hồ sơ: CÓ GỬI** — MailHog nhận mail tới đúng email chủ hồ sơ `qa.tvv.pheduyet.a@htpldn.test` lúc 10:33:18, tiêu đề "**Hồ sơ TVV đã được phê duyệt — kích hoạt tài khoản**", nội dung kèm link đặt mật khẩu lần đầu. → ý (b) của đối tác **KHÔNG tái hiện** theo đúng câu chữ SRS (chủ hồ sơ = TVV/CG).
- Thông báo tới **CB NV đã thẩm định**: KHÔNG có (unread giữ nguyên 58, không có mục mới) — trùng quan sát đối tác. Nhưng SRS FR-IV-07 **không yêu cầu** thông báo cho CB NV ở bước phê duyệt.

**Đối chiếu SRS (3 ý):**

- **(a) Đối tác kỳ vọng chuyển "Đang hoạt động".** → **Mâu thuẫn nội bộ SRS:** FR-IV-07 §Processing bước 2 (dòng 591) + §Postconditions (dòng 619) + SM-TVV quy định PHE_DUYET → **CHO_KICH_HOAT**; NHƯNG SCR-IV-03 nút Phê duyệt (dòng 1545) + §Quy tắc tương tác (dòng 1582) vẫn ghi "**đặt trạng thái Đang hoạt động**". CHANGELOG v3→v3.5 "Thay đổi 11" (dòng 148) khai đã sửa §3 nhưng 2 dòng này còn sót. Web chạy theo §2. → **BA confirm** (mâu thuẫn giữa các nguồn).
- **(b) Đối tác báo không gửi thông báo chủ hồ sơ.** → FR-IV-07 §Processing bước 4 (dòng 593): "Gửi thông báo **TVV/CG (chủ hồ sơ)** qua email đã khai"; bước 2 (dòng 591): gửi mail link kích hoạt. SRS KHÔNG yêu cầu thông báo cho CB NV / NHT. Web CÓ gửi email tới chủ hồ sơ (TVV) kèm link kích hoạt → ý này không tái hiện theo câu chữ SRS; kỳ vọng đối tác (gửi tới "Người hỗ trợ", nội dung "mã số tư vấn viên: {mã}") khác SRS. → **BA confirm**.
- **(c) Đối tác báo thông báo khác thiết kế.** → SRS §3.0b (dòng 1394-1405) chỉ quy định text **hộp thoại xác nhận**, KHÔNG quy định text toast thành công sau phê duyệt. Web hiện "Phê duyệt TVV thành công". → **BA confirm** (SRS im lặng).

**Verdict:** `BA confirm` (không có ý nào Open; theo QA_VERIFY_PROTOCOL §"1 case gộp nhiều lỗi con": không Open mà còn BA confirm → verdict tổng BA confirm, KHÔNG Reject cả case).
