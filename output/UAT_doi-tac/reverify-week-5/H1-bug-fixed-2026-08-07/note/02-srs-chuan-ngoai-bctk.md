# SRS chuẩn đối chiếu — 6 case ngoài nhóm BCTK

> **Nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> Mọi số dòng dưới đây đều **mở file đọc trực tiếp ngày 07/08/2026**, không lấy từ đề bài, không lấy từ `input/srs-update-2026-5-5/` hay `input/srs-v3/`.
> Tài liệu này CHỈ trích spec làm chuẩn đo — không kết luận Pass/Reopen.

---

## QLDXDTTH_OOS_01

**Yêu cầu case đòi:** Cán bộ nghiệp vụ phải có đường đi trên giao diện để tiếp nhận và đánh dấu thực hiện đề xuất đào tạo do doanh nghiệp / người hỗ trợ gửi tới đơn vị mình.

**Trích SRS:**
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md:1068` — "**Mô tả:** DN/NHT gửi đề xuất đào tạo. CB NV tiếp nhận. Sửa/xóa khi chưa tiếp nhận."
- `…/srs-fr-03-dao-tao.md:1078` — "**Outputs:** id, linh_vuc, noi_dung (truncate), trang_thai (MOI/DA_TIEP_NHAN/DA_THUC_HIEN), ngay_tao."
- `…/srs-fr-03-dao-tao.md:1898` — "**Thành phần 8 — Tab \"Đề xuất đào tạo\":** Tab phụ tiếp nhận đề xuất từ DN/NHT. Bảng cột Lĩnh vực · Nội dung (cắt 150 ký tự) · Người đề xuất · Trạng thái (3 nhãn v3 — giữ nguyên do BA OUT Thay đổi 15) · Ngày tạo · Hành động (Xem · Tiếp nhận · Đánh dấu thực hiện)."
- `…/srs-fr-03-dao-tao.md:1086` (Tiêu chí nghiệm thu FR-III-13) — "- **Given** CB NV xóa đề xuất **When** đề xuất chưa tiếp nhận **Then** xóa mềm"

**Mã màn hình liên quan:** SCR-III-01 — Chương trình đào tạo (sub-menu 2), heading tại `srs-fr-03-dao-tao.md:1837`; Thành phần 8 là tab "Đề xuất đào tạo" của chính màn này. FR-III-13 khai màn hình tại `:1066` — "**Màn hình:** SCR-III-01 (tab \"De xuat\")".

**Đối chiếu số dòng đề bài:** khớp cả hai (đề bài ghi 1068 và 1898 — đọc thực tế đúng 1068 và 1898).

**⚠️ Hai điểm SRS không nói / nói ngược, phải nêu khi đo:**
1. `…/srs-fr-03-dao-tao.md:1070` ghi "**Tác nhân:** DN / NHT" — FR-III-13 **không liệt kê CB NV vào dòng Tác nhân**; vai trò CB NV chỉ xuất hiện ở câu Mô tả (`:1068`) và ở tiêu chí nghiệm thu (`:1086`).
2. Ma trận quyền mức dữ liệu `…/srs-v3.5.md:1314` cho `DE_XUAT_DAO_TAO`: cột `CB_NV_TW` = `R`, `CB_NV_BN`/`CB_NV_DP` = `R*` — **chỉ Đọc, không có U**. Nhưng `…/srs-v3.5.md:1296` làm rõ: "Bảng này là quyền ở MỨC DỮ LIỆU, không phải quyền chạy chức năng … Tác nhân của từng chức năng do dòng **Tác nhân** và **Điều kiện tiên quyết** của chính FR quyết định". Vậy ma trận `R` **không** phủ định được cột "Hành động (Xem · Tiếp nhận · Đánh dấu thực hiện)" ở `:1898`.

**Chốt để đo:** Vào tab "Đề xuất đào tạo" của màn Chương trình đào tạo (SCR-III-01) bằng tài khoản Cán bộ nghiệp vụ, đọc cột "Hành động" của dòng ở trạng thái Mới gửi và dòng Đã tiếp nhận. Có đủ lối vào "Tiếp nhận" (dòng Mới gửi) và "Đánh dấu thực hiện" (dòng Đã tiếp nhận), bấm chạy được và trạng thái chuyển đúng theo `:1078` → đủ căn cứ đóng. Cột "Hành động" vẫn là dấu gạch ngang với mọi vai trò cán bộ → còn nguyên vi phạm `:1898`.

---

## QLDMTCTV_OOS_14

**Yêu cầu case đòi:** Khi người dùng chọn một lệnh trong nhóm "..." ở màn danh sách Tổ chức tư vấn, hệ thống chỉ được mở hộp thoại xác nhận tương ứng; người dùng phải còn đứng ở màn danh sách (đúng tab + bộ lọc đang mở) cả trong lúc hộp thoại hiện lẫn sau khi hủy hộp thoại.

**Trích SRS:**
- `…/srs-fr-04-chuyen-gia-tvv.md:1645` (SCR-IV-NEW-01, Thành phần **24** "Hành động", cột *Hành vi*) — "2 icon thường: Xem (mắt) → SCR-IV-NEW-03; Sửa (bút chì) → SCR-IV-NEW-02 (ẩn nếu trạng thái Vô hiệu hóa). Dropdown \"...\" chứa: **\"Trình phê duyệt\"** (chỉ khi Mới đăng ký hoặc Đã từ chối, có Giấy ĐKHĐ); … | **Click → tương ứng (mỗi mục mở modal MD-\* tương ứng)**"
- `…/srs-fr-04-chuyen-gia-tvv.md:1639` (SCR-IV-NEW-01, Thành phần **18**) — "| 18 | bảng | Tên tổ chức | cột (đường liên kết, đậm) | — | **Click → SCR-IV-NEW-03 chi tiết** |"

**Mã màn hình liên quan:** SCR-IV-NEW-01 — Danh sách Tổ chức tư vấn (heading `srs-fr-04-chuyen-gia-tvv.md:1607`, đường dẫn `/chuyen-gia-tvv/to-chuc` tại `:1611`); màn đích bị nhảy sang là SCR-IV-NEW-03 — Chi tiết Tổ chức tư vấn (heading `:1699`).

**Đối chiếu số dòng đề bài:** lệch cả hai — đề bài 1646 → thực tế **1645** (Thành phần 24); đề bài 1640 → thực tế **1639** (Thành phần 18). Lệch đều −1.

**⚠️ Lưu ý mức chứng cứ:** SRS **không có câu chữ trực tiếp** kiểu "chọn lệnh trong '...' thì KHÔNG được điều hướng nền". Căn cứ là gián tiếp nhưng khép kín: `:1645` khai hành vi của mọi mục trong "..." là *mở modal*, và `:1639` là **mục duy nhất** của SCR-IV-NEW-01 khai hành vi *điều hướng sang SCR-IV-NEW-03*. Không có thành phần nào khác của màn danh sách (`:1620-1649`) khai điều hướng sang màn chi tiết ngoài Thành phần 18 và icon Xem ở `:1645`.

**Chốt để đo:** Ở tab "Mới đăng ký", bấm "..." → "Trình phê duyệt", đọc thanh địa chỉ **ngay lúc hộp thoại đang hiện**. Địa chỉ còn giữ `/chuyen-gia-tvv/to-chuc?...` và bấm [Hủy] thì về đúng danh sách với nguyên tab + bộ lọc → khớp `:1645`. Địa chỉ đã đổi sang `/chuyen-gia-tvv/to-chuc/{id}` → còn vi phạm, vì đó là hành vi mà SRS chỉ gán cho Thành phần 18 (`:1639`).

---

## QLDMTCTV_OOS_15

**Yêu cầu case đòi:** Nhóm lệnh "..." của dòng ở tab "Đang hoạt động" phải có lệnh "Cập nhật trạng thái" cho Cán bộ Nghiệp vụ cùng đơn vị — tức chuyển trạng thái được ngay từ màn danh sách, không bắt buộc phải vào màn chi tiết.

**Trích SRS:**
- `…/srs-fr-04-chuyen-gia-tvv.md:1645` (SCR-IV-NEW-01, Thành phần **24** "Hành động") — "Dropdown \"...\" chứa: **\"Trình phê duyệt\"** (chỉ khi Mới đăng ký hoặc Đã từ chối, có Giấy ĐKHĐ); **\"Phê duyệt\"** (vai trò Cán bộ Phê duyệt cùng đơn vị, trạng thái Chờ phê duyệt); **\"Từ chối\"** (vai trò Cán bộ Phê duyệt cùng đơn vị, trạng thái Chờ phê duyệt); **\"Cập nhật trạng thái\"** (Cán bộ Nghiệp vụ cùng đơn vị, trạng thái Đang hoạt động/Tạm dừng/Vô hiệu hóa); **\"Xóa\"** (chỉ khi không có tư vấn viên liên kết)"
- `…/srs-fr-04-chuyen-gia-tvv.md:1613` (SCR-IV-NEW-01, Quyền truy cập) — "- Cán bộ Nghiệp vụ: thêm/sửa/xóa, xuất Excel, công khai, **cập nhật trạng thái** (Tổ chức tư vấn thuộc đơn vị)"
- Đối chiếu màn chi tiết (nơi chức năng hiện đang chạy được) — `…/srs-fr-04-chuyen-gia-tvv.md:1721` (SCR-IV-NEW-03, Thành phần 8) — "Nút **Cập nhật trạng thái** … | Vai trò = Cán bộ Nghiệp vụ cùng đơn vị; trạng thái ∈ {Đang hoạt động, Tạm dừng, Vô hiệu hóa} |"

**Mã màn hình liên quan:** SCR-IV-NEW-01 (danh sách — nơi thiếu lối vào); SCR-IV-NEW-03 (chi tiết — nơi lệnh vẫn có). Chức năng nghiệp vụ gốc: FR-IV-NEW-02 "Cập nhật trạng thái Tổ chức tư vấn" (`:966`).

**Đối chiếu số dòng đề bài:** lệch — đề bài 1646 → thực tế **1645**.

**Chốt để đo:** Đăng nhập Cán bộ Nghiệp vụ, mở tab "Đang hoạt động", bấm "..." ở dòng **cùng đơn vị với tài khoản**, đếm số lệnh. Có "Cập nhật trạng thái" (bên cạnh "Xóa") và bấm mở được hộp thoại chọn trạng thái + lý do → khớp `:1645`. Chỉ còn mỗi "Xóa" → còn thiếu đúng mục mà `:1645` liệt kê. Lưu ý điều kiện của SRS là *cùng đơn vị*: dòng khác đơn vị không có lệnh này là đúng spec, không tính là lỗi.

---

## QLDMTCTV_OOS_16

**Yêu cầu case đòi:** Nhãn nút quay lại ở đầu màn Chi tiết Tổ chức tư vấn phải đúng câu chữ mà đặc tả màn hình quy định.

**Trích SRS:**
- `…/srs-fr-04-chuyen-gia-tvv.md:1715` (SCR-IV-NEW-03, Thành phần **2**) — "| 2 | thanh điều hướng | Nút Quay lại | nút phụ | **\"← Quay lại danh sách\"** | Click → SCR-IV-NEW-01 | Luôn |"

**Mã màn hình liên quan:** **SCR-IV-NEW-03 — Chi tiết Tổ chức tư vấn** (heading `srs-fr-04-chuyen-gia-tvv.md:1699`). Đây là màn đúng của case. Cùng file còn 2 dòng nhãn giống hệt nhưng **thuộc màn khác, không được dùng thay**: `:1550` là SCR-IV-03 (chi tiết Tư vấn viên, click → SCR-IV-01) và `:1845` là SCR-IV-NHT-03 (chi tiết Người hỗ trợ, click → SCR-IV-NHT-01).

**Đối chiếu số dòng đề bài:** lệch — đề bài 1716 → thực tế **1715**.

**Chốt để đo:** Bấm tên một tổ chức để vào màn Chi tiết Tổ chức tư vấn (đường dẫn `/chuyen-gia-tvv/to-chuc/{id}`), đọc nguyên văn nhãn nút quay lại ở đầu trang. Đọc ra đúng chuỗi "← Quay lại danh sách" → khớp `:1715`. Đọc ra "← Danh sách" hay bất kỳ biến thể rút gọn nào → còn lệch câu chữ đặc tả. Đo bằng mắt trên đúng màn chi tiết Tổ chức tư vấn, đừng lấy nhãn của màn chi tiết Tư vấn viên / Người hỗ trợ.

---

## QLNDTVVCG_QA01

**Yêu cầu case đòi:** Nhãn trạng thái hiển thị trên màn danh sách Tư vấn chuyên sâu phải đúng câu chữ trong bảng nhãn trạng thái SM-TVCS của đặc tả màn hình.

**Trích SRS:** bảng "Bảng nhãn trạng thái SM-TVCS", heading tại `…/srs-fr-12-tv-chuyen-sau.md:1130`, các dòng nhãn:
- `…/srs-fr-12-tv-chuyen-sau.md:1134` — "| TIEP_NHAN | Tiếp nhận | Xanh dương |"
- `…/srs-fr-12-tv-chuyen-sau.md:1135` — "| PHAN_CONG | **Đã phân công** | Vàng nhạt |"
- `…/srs-fr-12-tv-chuyen-sau.md:1136` — "| DANG_TU_VAN | Đang tư vấn | Vàng |"
- `…/srs-fr-12-tv-chuyen-sau.md:1137` — "| HOAN_THANH | Hoàn thành TV | Xanh lá nhạt |"
- `…/srs-fr-12-tv-chuyen-sau.md:1138` — "| CHO_PHE_DUYET | Chờ phê duyệt | Vàng |"
- `…/srs-fr-12-tv-chuyen-sau.md:1139` — "| DA_DUYET | Đã duyệt | Xanh lá |"
- `…/srs-fr-12-tv-chuyen-sau.md:1140` — "| HUY | **Đã hủy** | Xám |"

Neo bảng vào đúng cột trên màn: `…/srs-fr-12-tv-chuyen-sau.md:1125` (SCR-X1-01, Thành phần 10) — "Bảng nội dung TVCS | table | Checkbox / Mã (TVCS-{YYYYMMDD}-{SEQ}) / Tiêu đề / Tên DN / Tên CG / Lĩnh vực PL / **Trạng thái SM-TVCS (badge)** / Ngày tư vấn / Ngày tạo / Hành động…"

**Mã màn hình liên quan:** **SCR-X1-01 — Danh sách Tư vấn pháp luật chuyên sâu** (heading `srs-fr-12-tv-chuyen-sau.md:1102`). Bảng nhãn `:1130-1140` nằm **trong** mục đặc tả của chính màn danh sách này, nên đúng màn mà case đo.

**Đối chiếu số dòng đề bài:** khớp (đề bài ghi "các dòng 1130-1140", "Đã phân công" dòng 1135, "Đã hủy" dòng 1140 — đọc thực tế đúng như vậy).

**⚠️ Đừng lấy nhầm 2 bảng khác trong cùng file:** `…:1533-1539` (Phụ lục C.8 SM-TVCS, "Bảng trạng thái") là bảng **mô tả trạng thái + mã kỹ thuật** (`received` / `assigned` / `cancelled`), không phải nhãn hiển thị; `…:1168` (SCR-X1-02, thanh tiến trình) in **mã enum** `[TIEP_NHAN]--[PHAN_CONG]--…`, cũng không phải nhãn badge. Nhãn hiển thị duy nhất là bảng ở `:1130-1140`.

**Chốt để đo:** Ở SCR-X1-01, đọc nguyên văn badge cột "Trạng thái" của một hồ sơ đã phân công chuyên gia và một hồ sơ đã hủy. Badge đọc ra đúng "Đã phân công" và "Đã hủy" → khớp `:1135` và `:1140`. Đọc ra "Phân công" / "Hủy" → còn lệch câu chữ. Nên đọc luôn 5 nhãn còn lại (`:1134`, `:1136`-`:1139`) trong cùng lượt vì đợt trước mới đo được 2/7 nhãn.

---

## QLNDTVVCG_OOS_02

**Yêu cầu case đòi:** Người dùng không mang vai trò Cán bộ Nghiệp vụ (ở đây là tài khoản chỉ có Tư vấn viên + Chuyên gia) phải bị hệ thống từ chối thao tác phân công chuyên gia cho hồ sơ tư vấn chuyên sâu, và giao diện không được mời họ thao tác đó.

**Trích SRS — vai trò nào được phân công:**
- `…/srs-v3.5.md:1440` (bảng **TU_VAN_CHUYEN_SAU — Action-level permissions**, `[BA chốt 2026-08-06 — UAT tuần 5]`, heading ở `:1428`) — "| TVCS_ASSIGN | Phân công người tư vấn | **CB_NV_{cap}** | `user.don_vi_id = record.don_vi_id` AND `record.trang_thai = TIEP_NHAN` AND người được chọn có `loai_tvv = 'CG'` | FR-X.1-01 |"
- `…/srs-fr-12-tv-chuyen-sau.md:176` (FR-X.1-01, Processing — Phân công CG, bước 1) — "| 1 | **Kiểm tra quyền CB NV và phạm vi đơn vị** | BR-AUTH-01, BR-AUTH-08 |"
- `…/srs-fr-12-tv-chuyen-sau.md:1517` (Phụ lục C.8, sơ đồ SM-TVCS) — "TIEP_NHAN --> PHAN_CONG : **CB NV phân công CG**"

**Trích SRS — phạm vi quyền của Chuyên gia (đã được BA mở rộng ngày 06/08/2026, KHÔNG gồm phân công):**
- `…/srs-fr-12-tv-chuyen-sau.md:97` (FR-X.1-01, Tác nhân) — "**Tác nhân:** Cán bộ Nghiệp vụ (TW/BN/ĐP) — toàn bộ vòng đời. **Chuyên gia (CG)** — chỉ trên bản ghi mình được phân công: nhận việc / từ chối / hoàn thành, và **sửa nội dung khi hồ sơ ở trạng thái DANG_TU_VAN**; chặn Tạo mới và Xóa `[BA chốt 2026-08-06]`. **Cán bộ Phê duyệt (TW/BN/ĐP)** — phê duyệt / từ chối phê duyệt, và hủy hồ sơ đang tư vấn"
- `…/srs-fr-12-tv-chuyen-sau.md:34` (Tác nhân chính của nhóm X.1) — "**Tác nhân chính:** Cán bộ Nghiệp vụ (TW/BN/ĐP) — UC147/148/150/152; **Chuyên gia (CG)** — trên bản ghi được phân công: nhận việc/từ chối/hoàn thành, sửa nội dung ở trạng thái DANG_TU_VAN (UC147), đọc tư liệu R-only (UC152, BR-AUTH-14) `[BA chốt 2026-08-06]`; Người hỗ trợ — chỉ UC148 … Cổng Pháp luật quốc gia (API inbound) — UC149/151/153"
- Các quyền CG được liệt kê đích danh trong bảng action-level, đều **không có phân công**: `…/srs-v3.5.md:1441` TVCS_ACCEPT (CG nhận việc), `:1442` TVCS_REJECT (từ chối nhận việc), `:1443` TVCS_COMPLETE (hoàn thành). `:1436` TVCS_CREATE ghi rõ "**Chuyên gia và Tư vấn viên đều bị chặn**"; `:1439` TVCS_DELETE ghi "**CG bị chặn**".
- `…/srs-fr-12-tv-chuyen-sau.md:1175` (SCR-X1-02, Thành phần 9 — Thanh hành động cố định) — "TIEP_NHAN: [Hủy] [Lưu] [Phân công CG ->] / PHAN_CONG: [Hủy yêu cầu] + (CG được phân công: [Chấp nhận] [Từ chối]) …", cột *Điều kiện hiển thị* = "**theo trạng thái + vai trò**".

**Mã màn hình liên quan:** SCR-X1-02 — Thêm mới / Chi tiết Tư vấn chuyên sâu (thanh hành động chứa nút [Phân công CG] tại `:1175`); nút phân công cũng có ở SCR-X1-01 (cột Hành động `:1125` và nút hàng loạt `:1127`).

**Đối chiếu số dòng đề bài:**
- Đề bài dòng **34** → số dòng khớp, nhưng **nội dung đã đổi**: bản chốt hiện tại đã bổ sung Chuyên gia (CG) làm tác nhân với phạm vi hẹp `[BA chốt 2026-08-06]`. Trích cụt như đề bài ("chỉ định một tác nhân duy nhất") **không còn đúng nguyên văn**.
- Đề bài dòng **97** → số dòng khớp, nội dung cũng đã mở rộng thêm CG và CB Phê duyệt. Kết luận nghiệp vụ vẫn giữ (CG không có quyền phân công) nhưng phải trích đủ câu, không được trích cụt.
- Đề bài dòng **170** ("Kiểm tra quyền CB NV và phạm vi đơn vị") → **lệch, thực tế dòng 176**. Dòng 170 hiện là đoạn "Lý do nghiệp vụ" giải thích vì sao chỉ giao cho loại CG.
- Đề bài **không nhắc** `srs-v3.5.md:1440` (TVCS_ASSIGN) — đây mới là dòng đặc tả mạnh nhất, ghi thẳng role được phép, và là bản BA chốt cùng ngày 06/08/2026 với ô phản hồi dev.

**Chốt để đo:** Đăng nhập tài khoản **chỉ có** vai trò Tư vấn viên + Chuyên gia, mở chi tiết một hồ sơ ở trạng thái TIEP_NHAN thuộc đơn vị đó và (a) xem thanh hành động có nút [Phân công CG] không, (b) gửi thẳng thao tác phân công bằng chính phiên đó. Cả hai tầng đều chặn — nút không mời thao tác và thao tác bị từ chối, hồ sơ giữ nguyên TIEP_NHAN → khớp `srs-v3.5.md:1440` + `srs-fr-12:176`. Còn thao tác thành công (hồ sơ chuyển sang PHAN_CONG, nhật ký ghi dòng phân công do tài khoản này thực hiện) → còn vượt quyền, kể cả khi nút đã bị ẩn ở giao diện. Đo cả 2 tầng vì `:1175` chỉ ràng buộc phần hiển thị, còn `:1440` + `:176` ràng buộc phần xử lý.

---

## Tóm tắt đối chiếu số dòng

| Case | Đề bài ghi | Thực đọc được | Kết luận |
|---|---|---|---|
| QLDXDTTH_OOS_01 | fr-03:1068 · fr-03:1898 | 1068 · 1898 | khớp |
| QLDMTCTV_OOS_14 | fr-04:1646 · fr-04:1640 | **1645** · **1639** | lệch −1 cả hai |
| QLDMTCTV_OOS_15 | fr-04:1646 | **1645** | lệch −1 |
| QLDMTCTV_OOS_16 | fr-04:1716 | **1715** | lệch −1 |
| QLNDTVVCG_QA01 | fr-12:1130-1140 · 1135 · 1140 | 1130-1140 · 1135 · 1140 | khớp |
| QLNDTVVCG_OOS_02 | fr-12:34 · fr-12:97 · fr-12:170 | 34 · 97 (nội dung đã mở rộng 06/08) · **176** | 2 khớp số dòng nhưng trích cụt · 1 lệch +6 |

**SRS im lặng:** 0/6 case bị im lặng hoàn toàn. Riêng **QLDMTCTV_OOS_14** chỉ có căn cứ **gián tiếp** — SRS khai hành vi của mục trong "..." là *mở modal* (`fr-04:1645`) và khai điều hướng sang màn chi tiết **chỉ** ở Thành phần 18 (`fr-04:1639`), nhưng **không có câu nào cấm điều hướng nền bằng chữ**.
