# Tuần 3 — các nội dung CHƯA ĐÓNG, còn phải làm tiếp — 2026-08-03

> **File này để làm gì:** liệt kê mọi dòng của tab `UAT_TGPL Doanh Nghiệp-tuần 3` **chưa được đóng**, kèm lý do chưa đóng và việc tiếp theo thuộc về ai. Dùng làm danh sách bàn giao cho vòng verify sau. KHÔNG thay bug-report, KHÔNG thay file BA confirm.

> **Cách lập:** đọc trực tiếp sheet `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `UAT_TGPL Doanh Nghiệp-tuần 3` (gid `387857822`) ngày 03/08/2026 — rà **toàn bộ 338 dòng có Mã TC** rồi lọc theo cột `Verify`, không gom tay theo trí nhớ.

> **⚠️ Nguồn gốc số liệu:** 12/13 dòng dưới đây thuộc phần việc của **tổ verify Luồng 4 (Tổ chức tư vấn)**; dòng còn lại (`QLDKTK_01`) thuộc luồng Quản trị tài khoản. Người lập file **không tự chạy lại UI** cho dòng nào — nội dung mô tả lấy nguyên từ sheet và từ artifact `oos/QLDMTCTV_OOS_*.json` của tổ đó. Đây là **danh sách việc**, không phải báo cáo verify.

---

## Tổng quan

| Trạng thái cột `Verify` | Số dòng | Đã đóng? |
|---|:-:|---|
| `Pass` | 229 | ✅ Đóng |
| `Reject` | 51 | ✅ Đóng |
| `Resolved` | 45 | ✅ Đóng |
| **`Open`** | **9** | ❌ Chờ dev fix rồi re-verify |
| **`BA confirm`** | **3** | ❌ Chờ BA chốt |
| **(TRỐNG)** | **1** | ❌ QA chưa kết luận |
| **Tổng chưa đóng** | **13** | |

---

## Nhóm 1 — QA CHƯA KẾT LUẬN (cột `Verify` còn trống): 1 dòng

> Đây là nhóm duy nhất đúng nghĩa đen "còn cần Verify" — chưa có bất kỳ kết luận nào của QA.

### row 321 — `QLDKTK_01` · Quản lý đăng ký tài khoản

- **Đối tác báo:** Một số trường thông tin không giống với tài liệu · Trạng thái 1 = `Fail`
- **Kỳ vọng trong phiếu:** Dữ liệu hợp lệ, hệ thống hiển thị trang xác nhận "Đăng ký thành công. Vui lòng kiểm tra thư điện tử và nhấn liên kết kích hoạt để đặt mật khẩu".
- **Dev đã trả lời (cột P = `Reject`):** KHÔNG phải bug: Chặn "MST đã tồn tại" khi MST đã có trong DOANH_NGHIEP là ĐÚNG SRS (srs-fr-10:1078). Triệu chứng do dữ liệu test (lượt trước đã tạo DN cùng MST) — dùng MST mới hoặc chức năng Quên mật khẩu để verify.
- **Vì sao chưa đóng:** dev kết luận "không phải bug" và có dẫn đặc tả, nhưng **QA chưa kiểm chứng lại**. Theo nguyên tắc không lấy lời dev làm bằng chứng, phải tự dựng lại tình huống rồi mới ghi verdict.
- **Việc tiếp theo:** đăng ký bằng **mã số thuế MỚI chưa có trong hệ thống** (loại trừ nguyên nhân dữ liệu cũ mà dev nêu) → nếu đăng ký được thì verdict `Reject`; nếu vẫn chặn thì `Open`. Song song kiểm luôn ý gốc của đối tác là *"một số trường thông tin không giống tài liệu"* — ý này dev **chưa trả lời**.
- **Ai làm:** QA.

---

## Nhóm 2 — ĐÃ KẾT LUẬN LÀ LỖI, chờ dev fix rồi re-verify (`Open`): 9 dòng

> Cả 9 dòng đều là lỗi QA tự phát hiện thêm (`_OOS_`) khi kiểm 4 phiếu `QLDMTCTV_02 / _05 / _06 / _09`, đã ghi `Open` ở cột `Verify`. Cột `Trạng thái dev fix 1` đang là `dev done` — tức **dev báo đã sửa nhưng QA chưa re-verify**, không phải đã đóng.

| Row | Mã TC | Lỗi | Đặc tả bị vi phạm |
|:-:|---|---|---|
| 327 | `QLDMTCTV_OOS_01` | Danh sách Tổ chức tư vấn — thẻ "Chờ phê duyệt" không chuyển dấu đỏ khi đang có hồ sơ chờ xử lý | dòng 1628 (thẻ "Chờ phê duyệt" phải có chấm đỏ nếu >0) |
| 328 | `QLDMTCTV_OOS_02` | Danh sách Tổ chức tư vấn — cột "Công khai" là nhãn tĩnh, bấm không mở được hộp thoại công khai | dòng 1645 (cột "Công khai" là toggle, bấm mở hộp thoại) |
| 329 | `QLDMTCTV_OOS_03` | Danh sách Tổ chức tư vấn — cột "Hành động" thiếu nhóm lệnh "..." (Trình phê duyệt / Phê duyệt / Từ chối / Cập nhật trạng thái) | dòng 1646 (cột "Hành động" có nhóm lệnh "…") |
| 333 | `QLDMTCTV_OOS_07` | Danh sách Tổ chức tư vấn — màn hình rỗng chỉ hiện chữ "Trống", thiếu câu hướng dẫn theo đặc tả | đặc tả yêu cầu câu hướng dẫn tiếng Việt cho màn rỗng |
| 334 | `QLDMTCTV_OOS_08` | Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — không chia 6 nhóm thu gọn như đặc tả | dòng 1676–1695 (biểu mẫu chia 6 nhóm thu gọn) |
| 335 | `QLDMTCTV_OOS_09` | Biểu mẫu Chỉnh sửa Tổ chức tư vấn — đường dẫn điều hướng không kèm tên tổ chức đang sửa | dòng 1675 (đường dẫn điều hướng kèm tên tổ chức) |
| 336 | `QLDMTCTV_OOS_10` | Biểu mẫu Thêm mới / Chỉnh sửa Tổ chức tư vấn — 5 nhãn trường hiển thị khác nhãn trong đặc tả | dòng 1676–1695 (nhãn trường) |
| 337 | `QLDMTCTV_OOS_11` | Màn Chi tiết Tổ chức tư vấn — thiếu toàn bộ 3 tab và không có vùng tệp đính kèm | đặc tả màn Chi tiết `SCR-IV-NEW-03` (3 tab + vùng tệp đính kèm) |
| 338 | `QLDMTCTV_OOS_12` | Danh sách Tổ chức tư vấn — ô tìm kiếm không tìm được theo Người đại diện | đặc tả ô tìm kiếm của `SCR-IV-NEW-01` |

**Chi tiết quan sát (nguyên văn từ sheet):**

- **row 327 `QLDMTCTV_OOS_01`** — Thẻ "Chờ phê duyệt" đang có 1 hồ sơ nhưng huy hiệu vẫn nền XANH. Cùng lúc đó thẻ "Mới đăng ký" cũng có hồ sơ thì huy hiệu nền ĐỎ. Hai thẻ được đặc tả bằng cùng một mệnh đề nhưng hiển thị khác nhau. Hệ quả: Cán bộ Phê duyệt mất tín hiệu cảnh báo trên đúng thẻ chứa việc của mình.
- **row 328 `QLDMTCTV_OOS_02`** — Cột "Công khai" chỉ là nhãn tĩnh, không bấm được (con trỏ chuột không đổi thành hình bàn tay), bấm vào không mở hộp thoại nào. Nhãn hiển thị cũng khác đặc tả: web dùng "Công khai" / "Riêng tư", đặc tả yêu cầu "Đã công khai" / "Chưa công khai". Hiện chỉ công khai được bằng cách tích chọn dòng rồi bấm nút trên thanh thao tác hàng loạt.
- **row 329 `QLDMTCTV_OOS_03`** — Cột "Hành động" chỉ có 3 biểu tượng rời: Xem, Sửa, Xóa. Không có nhóm lệnh "..." nào. Hệ quả: các lệnh "Trình phê duyệt" và "Cập nhật trạng thái" không thao tác được từ danh sách, phải mở màn Chi tiết của từng tổ chức mới làm được.
- **row 333 `QLDMTCTV_OOS_07`** — Vùng bảng chỉ hiện hình minh họa kèm đúng một chữ "Trống" — là chữ mặc định của thư viện giao diện, không phải câu tiếng Việt mà đặc tả yêu cầu. Không có câu hướng dẫn nào cho người dùng. Đã kiểm ở thẻ "Đã từ chối"; thẻ "Tạm dừng" và "Vô hiệu hóa" hiển thị y hệt.
- **row 334 `QLDMTCTV_OOS_08`** — Biểu mẫu để phẳng, không có nhóm nào thu gọn hay mở ra được. Chỉ 2 trong 6 nhóm có tiêu đề mục hiển thị là "Công bố" và "Tệp đính kèm"; 4 nhóm còn lại không có tiêu đề phân tách. Giống nhau ở cả chế độ Thêm mới và chế độ Chỉnh sửa. Không cản trở việc nhập liệu, nhưng biểu mẫu dài và khó tìm mục.
- **row 335 `QLDMTCTV_OOS_09`** — Đường dẫn hiển thị là "Trang chủ / Mạng lưới Tư vấn viên / Tổ chức tư vấn / Chi tiết / Chỉnh sửa" — không kèm tên tổ chức. Ngoài ra còn chèn thêm một cấp "Chi tiết" không có trong đặc tả. Hệ quả: khi mở nhiều tổ chức liên tiếp, người dùng không biết mình đang sửa hồ sơ nào nếu chỉ nhìn đường dẫn.
- **row 336 `QLDMTCTV_OOS_10`** — Năm nhãn hiển thị khác đặc tả: - "Chức vụ đại diện" (đặc tả: "Chức vụ người đại diện") - "Ngày cấp" (đặc tả: "Ngày cấp Giấy đăng ký hành nghề") - "Lĩnh vực pháp lý" (đặc tả: "Lĩnh vực pháp luật") - "Địa chỉ" (đặc tả: "Địa chỉ trụ sở") - "Điện thoại" (đặc tả: "Số điện thoại") Giống nhau ở cả chế độ Thêm mới và Chỉnh sửa. Nghĩa của trường không đổi, vẫn nhập liệu bình thường — mức ảnh hưởng nhẹ.
- **row 337 `QLDMTCTV_OOS_11`** — Màn Chi tiết KHÔNG có tab nào (đếm được 0 tab). Cả ba tab "Thông tin", "Tư vấn viên liên kết" và "Lịch sử" đều không tồn tại — người dùng không xem được danh sách tư vấn viên liên kết lẫn nhật ký thao tác của tổ chức. Không có mục tệp đính kèm nào, cũng không có nút "Xem" hay "Tải xuống", dù tổ chức này đang có 1 tệp PDF (mở chế độ Chỉnh sửa thì thấy tệp). Muốn xem tệp phải vào chế độ Chỉnh sửa. Bảng thông tin cũng t…
- **row 338 `QLDMTCTV_OOS_12`** — Tìm theo TÊN trả về 2 tổ chức, tìm theo MÃ trả về 1 tổ chức — ô tìm kiếm hoạt động bình thường. Nhưng tìm theo NGƯỜI ĐẠI DIỆN "Nguyen Van QA" trả về 0 kết quả, bảng hiện màn hình rỗng, dù người này đang hiện đúng ở cột "Người đại diện" của tổ chức TC-STP-AG-0001. Nội dung gợi ý trong ô tìm kiếm cũng chỉ ghi "Tìm theo tên hoặc mã tổ chức", thiếu hẳn phần "người đại diện" so với đặc tả. Hệ quả: cán bộ không tra được tổ…

- **Vì sao chưa đóng:** dev đã đặt `dev done` nhưng **chưa ai đo lại trên bản dựng mới**. Nhãn `dev done` là lời khai của dev, không phải bằng chứng.
- **Việc tiếp theo:** re-verify từng dòng trên bản dựng hiện hành → `Pass` nếu hết lỗi, `Reopen` nếu còn.
- **Ai làm:** QA (tổ Luồng 4). Dòng nào `Reopen` thì chuyển lại **Dev FE** — cả 9 lỗi đều thuộc phần giao diện.

---

## Nhóm 3 — CHỜ BA CHỐT (`BA confirm`): 3 dòng

> Ba dòng này **không chờ dev**, chờ BA quyết đâu là nguồn chuẩn. Nội dung đầy đủ (đối chiếu SRS + câu hỏi gửi BA + các hướng xử lý) đã nằm ở **`ba-confirmation-needed-luong4-to-chuc-tu-van-2026-08-03.md`** cùng thư mục — file dưới đây chỉ tóm tắt để tra nhanh.

| Row | Mã TC | Mục trong file BA | Cần BA chốt | Ảnh hưởng |
|:-:|---|:-:|---|---|
| 339 | `QLDMTCTV_OOS_13` | 1 | Giấy ĐKHĐ: một tên gọi chuẩn + một mức bắt buộc duy nhất | 🔴 **Chạm chức năng** — nếu chốt bắt buộc, hồ sơ cũ thiếu dữ liệu không lưu lại được |
| 332 | `QLDMTCTV_OOS_06` | 2 | Số thẻ trạng thái: 6 hay 3 | Tài liệu — chưa chốt thì mọi lượt kiểm sau vẫn báo lệch |
| 331 | `QLDMTCTV_OOS_05` | 3 | Cột "Đơn vị quản lý": giữ và bổ sung vào đặc tả, hay bỏ | Hiển thị — mức Minor |

- **Vì sao chưa đóng:** đặc tả tự mâu thuẫn (339, 332) hoặc lệch bản đã duyệt mà không có điều khoản cấm (331) → QA không tự chốt được.
- **Việc tiếp theo:** gửi file BA, nhận quyết định, rồi cập nhật verdict + sửa đặc tả tương ứng.
- **Ai làm:** BA. Sau khi BA chốt: `Dev FE` nếu phải sửa giao diện, hoặc `BA` cập nhật đặc tả rồi QA đóng dòng.

---

## Bảng tra nhanh — 13 dòng chưa đóng

| Row | Mã TC | `Verify` | Chờ ai | Việc tiếp theo |
|:-:|---|:-:|---|---|
| 321 | `QLDKTK_01` | (trống) | **QA** | Dựng lại bằng mã số thuế mới rồi ghi verdict |
| 327 | `QLDMTCTV_OOS_01` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 328 | `QLDMTCTV_OOS_02` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 329 | `QLDMTCTV_OOS_03` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 333 | `QLDMTCTV_OOS_07` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 334 | `QLDMTCTV_OOS_08` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 335 | `QLDMTCTV_OOS_09` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 336 | `QLDMTCTV_OOS_10` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 337 | `QLDMTCTV_OOS_11` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 338 | `QLDMTCTV_OOS_12` | `Open` | **QA** | Re-verify trên bản dựng mới (dev đã báo `dev done`) |
| 339 | `QLDMTCTV_OOS_13` | `BA confirm` | **BA** | Chờ quyết định, xem file BA cùng thư mục |
| 332 | `QLDMTCTV_OOS_06` | `BA confirm` | **BA** | Chờ quyết định, xem file BA cùng thư mục |
| 331 | `QLDMTCTV_OOS_05` | `BA confirm` | **BA** | Chờ quyết định, xem file BA cùng thư mục |

---

## Ghi chú — 2 điểm lệch cần dọn

1. **Cột "Mô tả" của row 332 và 339 đã lỗi thời.** Ngày 03/08/2026 QA rà lại và **rút 2 ý** khỏi hai dòng này (ý "thứ tự thẻ trạng thái" ở row 332, ý "thứ tự trường trên biểu mẫu" ở row 339) vì bảng thành phần màn hình là bảng liệt kê thành phần, không phải bản vẽ bố cục. Verdict và note (cột `Verify` + `DEV phản hồi lần 1`) đã cập nhật, nhưng **cột "Mô tả" vẫn ghi tiêu đề cũ** — người đọc sheet sẽ thấy tiêu đề nói về thứ tự trong khi câu hỏi còn lại là về số lượng thẻ / tên giấy tờ. Đề nghị tổ Luồng 4 sửa lại tiêu đề 2 dòng cho khớp.
2. **Row 330 `QLDMTCTV_OOS_04` đã được đóng cùng đợt rà đó** (`BA confirm` → `Reject`, không phải lỗi: ẩn huy hiệu khi số đếm bằng 0 là hành vi mặc định của thư viện giao diện, đặc tả không quy định trường hợp bằng 0). Nên không còn trong danh sách chưa đóng. Bản sao P/Q/R trước khi sửa: `reverify-audit/BACKUP-sheet-tuan3-rows-330-331-332-339-truoc-khi-sua-2026-08-03.json`.
