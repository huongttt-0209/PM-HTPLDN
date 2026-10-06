# Bảng đối chiếu điều kiện — TDHSTVV_18 (Trình phê duyệt, CB Nghiệp vụ cấp Địa phương)

Evidence đối tác: `partner-evidence/TDHSTVV_18.webm` — frame 00:04-00:12: tài khoản **CB Nghiệp vụ Địa phương (CB_NV_DP, badge BTP · DP)**, hồ sơ **`TVV-STP-HN-0001` ("Lê Hà Giang")** (`/chuyen-gia-tvv/a25d37d7-1f66-47cd-849d-76e1fe00f087`), tab Thẩm định điền đủ, Kết luận thẩm định = **ĐẠT**, bấm **"Trình duyệt"**. Frame 00:15: biểu mẫu chuyển sang chỉ đọc, **không có thông báo nào**. Frame 01:16-01:25: đăng nhập `cbpd_tw` → hồ sơ đã ở trạng thái **"Chờ phê duyệt"** (nghiệp vụ chạy được). Frame 01:49: đăng nhập `cbnv_bn` (Bộ ngành) → tab "Chờ phê duyệt" **rỗng** ⇒ hồ sơ **không** tự chuyển lên cấp Bộ/Ngành.

| Điều kiện | Đối tác (từ evidence full-res) | Mình test | GAP? |
|---|---|---|---|
| Vai trò / tài khoản | CB Nghiệp vụ **Địa phương** — CB_NV_DP, badge BTP · DP (đúng cấp mà case yêu cầu) | CB Nghiệp vụ Địa phương — `cbnv_dp`, CB_NV_DP, badge BTP · DP, đơn vị `00000000-...-0006` (cấp ĐP) — trùng khớp | Không |
| Entity + trạng thái | Hồ sơ TVV `TVV-STP-HN-0001` (đơn vị Sở Tư pháp — cấp ĐP), trạng thái **"Đang thẩm định"**; sau thao tác = "Chờ phê duyệt" | Hồ sơ TVV `TVV-STP-AG-0001` ("QA TVV Dia Phuong R18") — **tự seed mới** ở đơn vị ĐP, trạng thái **"Đang thẩm định"** trước thao tác; sau thao tác = "Chờ phê duyệt" | Không |
| Dữ liệu tiền đề | Nhóm 1 đủ 4 mục + Kết luận Pháp lý = Đạt; Nhóm 2 điểm 3; Nhóm 3 N/A; Nhóm 4 có tham gia; **Kết luận thẩm định = ĐẠT** | Nhóm 1 đủ 4 mục + Kết luận Pháp lý = Đạt; Nhóm 2 điểm 3; Nhóm 3 N/A; Nhóm 4 có tham gia; cả 3 ô Nhận xét có nội dung; **Kết luận thẩm định = ĐẠT** | Không |
| Input / thao tác | Bấm nút **"Trình duyệt"** trong tab Thẩm định | Bấm nút **"Trình duyệt"** trong tab Thẩm định (cùng nút, cùng màn) | Không |
| Người nhận thông báo | Cán bộ Phê duyệt có thẩm quyền với hồ sơ cấp ĐP | `cbpd_dp` — CB_PD_DP, **cùng đơn vị** `00000000-...-0006` với `cbnv_dp`; đăng nhập bằng phiên cách ly ngay sau thao tác để kiểm hộp thông báo | Không |

Kết luận: **0 GAP** — đúng vai trò CB_NV_DP cấp Địa phương, đúng trạng thái "Đang thẩm định", đúng thao tác "Trình duyệt", và kiểm thông báo bằng **đúng tài khoản Cán bộ Phê duyệt cùng đơn vị** (theo SRS dòng 518 + 570).

## Tiền đề tự tạo (không coi là blocker)

Tài khoản `cbnv_dp` ban đầu **không thấy hồ sơ TVV nào** (toàn bộ TVV hiện có thuộc BTP · TW). Đã tự dựng chuỗi tiền đề:
1. Tạo **Tổ chức tư vấn `TC-STP-AG-0001`** (cbnv_dp) → Trình phê duyệt → `cbpd_dp` phê duyệt (Số QĐ `QD-QA-DP-2026-001`) → tổ chức ở trạng thái **Đang hoạt động** (bắt buộc, vì ô "Tổ chức hành nghề chính" của biểu mẫu TVV chỉ liệt kê tổ chức đang hoạt động).
2. Tạo TVV **`TVV-STP-AG-0001`** (cbnv_dp) → trạng thái Mới đăng ký → mở tab Thẩm định, điền + "Lưu nháp" → trạng thái chuyển **Đang thẩm định** ⇒ khớp đúng trạng thái đối tác.

## Quan sát (artifact real-data) — cả 2 ý "Kết quả thực tế" của đối tác đều TÁI HIỆN

**Ý 1 — Hệ thống không hiển thị thông báo:** MutationObserver cài **trước** cú bấm "Trình duyệt", theo dõi 4 giây → `addedNodes = 3`, cả 3 chỉ là phần tử biểu mẫu chuyển sang chế độ chỉ đọc (`ant-pro-field-readonly`), **0 phần tử** `.ant-message` / `.ant-notification`. ⇒ **Không có thông báo thành công.** Ảnh: `bug-reports/image/BUG-TDHSTVV_18-cbnvdp-trinh-duyet-khong-thong-bao.png` (badge đã là "Chờ phê duyệt", màn hình không có thông báo nào).

**Ý 2 — Cán bộ phê duyệt không nhận được thông báo:** đăng nhập `cbpd_dp` (CB_PD_DP, **cùng đơn vị** với người thẩm định) bằng phiên cách ly ngay sau thao tác:
- Hồ sơ `TVV-STP-AG-0001` **CÓ** nằm trong hàng chờ "Chờ phê duyệt" của tài khoản này (1/1 mục) ⇒ đúng người có thẩm quyền phê duyệt, lẽ ra phải được báo.
- Hộp thông báo: **"Không có thông báo mới"**, số chưa đọc = **0**, tổng số thông báo = **0**.
- Ảnh: `bug-reports/image/BUG-TDHSTVV_18-cbpd-dp-khong-nhan-thong-bao.png` — một ảnh chứa cả hai: hộp thông báo rỗng **và** hồ sơ nằm trong tab "Chờ phê duyệt".
- Cơ chế thông báo của hệ thống vẫn chạy cho luồng khác (xác minh ở TDHSTVV_17: `cbpd_tw` có thông báo đào tạo / hỏi đáp) ⇒ thiếu sót nằm riêng ở luồng trình duyệt hồ sơ TVV, không phải hệ thống thông báo chết.

**Nghiệp vụ chính chạy đúng:** trạng thái hồ sơ chuyển `DANG_THAM_DINH` → **`CHO_PHE_DUYET`**, đơn vị quản lý giữ nguyên `...0006` (cấp ĐP).

## Về "Kết quả mong đợi" của đối tác (tự động chuyển lên cấp Bộ/Ngành)

Đối tác kỳ vọng "Hệ thống tự động chuyển hồ sơ lên cấp Bộ/Ngành tương ứng với lĩnh vực chuyên môn". Web: hồ sơ **giữ nguyên ở đơn vị ĐP** (`donViId` không đổi), CB_PD_DP là người duyệt. Đối chiếu SRS:
- dòng 80 — "CB NV cùng đơn vị thẩm định → CB PD cùng đơn vị phê duyệt (BR-FLOW-03 — **KHÔNG xuyên cấp**)".
- dòng 518 — "gửi thông báo CB_PD **cùng đơn vị với CB NV thẩm định** ... **KHÔNG có ESCALATE bắt buộc** — mỗi cấp tự công bố theo phạm vi phân cấp".
- dòng 570 — "**CB_PD_ĐP duyệt hồ sơ do CB_NV_ĐP thẩm định** (mạng lưới địa phương — NĐ 121/2025 Đ.39-40)".

⇒ Hành vi web (không escalate) **ĐÚNG SRS**; kỳ vọng của đối tác **trái SRS** → tách ra hỏi BA, xem `ba-confirmation-needed-week-2.md` §TDHSTVV_18. Phần này **không** tính là lỗi.

## Đối chiếu SRS (Cổng 3) — phần kết luận Open

- `srs-fr-04-chuyen-gia-tvv.md` dòng 518 (Processing bước 4) — Trình duyệt → chuyển CHO_PHE_DUYET + **gửi thông báo CB_PD cùng đơn vị**. → Web: chuyển trạng thái **đúng**, **KHÔNG gửi thông báo**. **KHÔNG khớp.**
- dòng 551 (Acceptance Criteria) — "**Given** CB NV kết luận ĐẠT **When** nhấn 'Trình duyệt' **Then** TVV → CHO_PHE_DUYET, **CB PD nhận thông báo**". **KHÔNG khớp.**
- dòng 1565 (ô 20d) — Click → **MD-TRINH-DUYET** (hộp thoại xác nhận, dòng 1396) → đặt trạng thái + thông báo CB PD cùng đơn vị. → Web: **không có hộp thoại xác nhận**. **KHÔNG khớp.**
- `srs-v3.5.md` dòng 571 — **UI-04**: "Toast notification cho thao tác thành công". → Web: thao tác thành công nhưng **không có thông báo**. **KHÔNG khớp.**

## Phát hiện thêm (ngoài 2 ý đối tác)

- **Không ghi nhận người trình / ngày trình:** đọc bản ghi sau thao tác → `nguoiGuiDuyetId = null`, `ngayGuiDuyet = null`, dù trạng thái đã là `CHO_PHE_DUYET` (giống TDHSTVV_17 ở cấp TW ⇒ lỗi chung, không phụ thuộc cấp).
- **"Lưu nháp" đổi trạng thái hồ sơ:** SRS dòng 1563 (ô 20b) ghi "Lưu kết quả thẩm định tạm, **không chuyển trạng thái**". Web: bấm "Lưu nháp" ở hồ sơ Mới đăng ký → trạng thái nhảy sang **Đang thẩm định**. Ngoài ra tải lại trang thì nội dung nháp **không được khôi phục** (cùng gốc BUG-TDHSTVV_08).

## Re-verify 2026-07-15 (sau dev fix — vòng 2)

Re-test đúng vai trò/state/data bug gốc (0 GAP):

| Điều kiện | Bug gốc (bug-report) | Mình test (re-verify) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Địa phương (CB_NV_DP) trình duyệt | `cbnv_dp` (CB_NV_DP, badge BTP · DP) trình duyệt | Không |
| Entity + trạng thái | Hồ sơ TVV cấp ĐP, trạng thái hợp lệ trước Trình duyệt | `TVV-STP-AG-0002` "QA TVV RV18 DiaPhuong" (tổ chức TC-STP-AG-0001, cấp ĐP), Mới đăng ký → thẩm định ĐẠT | Không |
| Dữ liệu tiền đề | Kết luận Pháp lý Đạt + Kết luận thẩm định ĐẠT | Kết luận Pháp lý Đạt + Nhóm 2/3 mặc định + Kết luận thẩm định ĐẠT | Không |
| Input / thao tác | Bấm "Trình duyệt" | Bấm "Trình duyệt" → xác nhận hộp thoại | Không |
| Người nhận thông báo | Cán bộ Phê duyệt cùng đơn vị | `cbpd_dp` (CB_PD_DP, cùng đơn vị ĐP), phiên cách ly ngay sau thao tác | Không |

**Kết quả re-verify — cả 3 thiếu sót ĐÃ FIX:**
1. **Hộp thoại xác nhận (MD-TRINH-DUYET):** ĐÃ CÓ — hiện hộp "Trình phê duyệt hồ sơ thẩm định — Sau khi trình, hồ sơ chuyển 'Chờ phê duyệt' và không thể chỉnh sửa thẩm định. Bạn xác nhận trình phê duyệt?" + nút Hủy / Trình phê duyệt. Khớp SCR-IV-03 ô 20d.
2. **Thông báo thành công cho CB Nghiệp vụ:** ĐÃ CÓ — toast **"Đã trình hồ sơ lên cấp phê duyệt"** (MutationObserver bắt được). Khớp UI-04.
3. **Thông báo cho Cán bộ Phê duyệt cùng đơn vị:** ĐÃ CÓ — `cbpd_dp` chuông Thông báo có **1 chưa đọc**, nội dung: *"PHE_DUYET · Hồ sơ TVV chờ phê duyệt · Hồ sơ TVV QA TVV RV18 DiaPhuong đã được thẩm định và chờ phê duyệt"* (một phút trước). Khớp SRS dòng 518 + 551 + 570 (CB_PD_ĐP nhận thông báo hồ sơ do CB_NV_ĐP thẩm định).

- Trạng thái hồ sơ chuyển **"Chờ phê duyệt"** đúng.
- Ảnh: `bug-reports/image/TDHSTVV_18-reverify-cbpd-dp-nhan-thong-bao-trinh-duyet.png` (thông báo cbpd_dp) + `bug-reports/image/TDHSTVV_18-reverify-cbnvdp-trinh-duyet-chophe-duyet.png` (cbnv_dp sau trình duyệt).

**Verdict re-verify:** `Pass` — cả 3 thiếu sót (hộp thoại xác nhận, toast thành công, thông báo CB_PD cùng đơn vị) đã fix.
