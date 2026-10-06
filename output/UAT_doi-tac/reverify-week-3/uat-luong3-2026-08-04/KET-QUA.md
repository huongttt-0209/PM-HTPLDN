# Kết quả re-verify vòng 2 — tab `UAT_TGPL Doanh Nghiệp-tuần 3` — 04/08/2026

**Môi trường:** `https://htpldn-uat.ospgroup.vn` · bản dựng `assets/index-DpIXRGaI.js` (last-modified 04/08/2026 11:27 giờ VN) · nhãn `HTPLDN · V1.0.5` · OTP cố định `666666`.

**Phạm vi (user chốt):** chỉ 20 dòng đúng bộ lọc `Trạng thái dev fix 1 = dev done` **và** `Verify = Pass`. Bỏ 5 dòng không khớp: 321 QLDKTK_01 (Reject/Resolved), 330 QLDMTCTV_OOS_04 (Reject), 331 OOS_05, 332 OOS_06, 339 OOS_13 (BA confirm).

**Kết quả: 20/20 Pass.** Đã ghi cột `Verify 2` = `Pass` cho cả 20 dòng, đọc lại khớp. Không đụng cột nào của dev.

> **Bổ sung 04/08/2026 15:35 — dòng 321 QLDKTK_01 (user yêu cầu riêng sau khi đối tác phản ánh lại):**
> **Reopen.** Doanh nghiệp có địa chỉ ở **Hà Nội** không đăng ký được — hệ thống báo nhầm "Mã số thuế đã tồn tại
> trong hệ thống" dù mã số thuế mới tinh; đổi Tỉnh/Thành phố sang TP.HCM hoặc An Giang thì đăng ký chạy trọn.
> Nguyên nhân: mã doanh nghiệp cấp theo "số bản ghi của tỉnh + 1", Hà Nội thủng dãy nên trùng `DN-HNI-0014`.
> Chi tiết: [cond/QLDKTK_01.md](cond/QLDKTK_01.md) · [reverify-audit/QLDKTK_01-vong2.md](reverify-audit/QLDKTK_01-vong2.md).
> Đã ghi `W321` = `X321` = `Reopen` + note vào `Y321` (3 ô trước đó đều trống, không đè gì của dev).

| Dòng | Mã TC | Verdict | Lý do (1 câu) |
|---:|---|:-:|---|
| 315 | CNKQHT_07 | Pass | Cập nhật kết quả lưu đủ nội dung + tệp; cán bộ nghiệp vụ phụ trách nhận thông báo đúng giây bấm |
| 316 | TPDBC_01 | Pass | Trình phê duyệt đổi trạng thái sang Chờ phê duyệt; cán bộ phê duyệt cùng đơn vị nhận thông báo đúng giây bấm |
| 317 | QLDMTCTV_02 | Pass | Bảng đã có ô tích chọn (kèm chọn tất cả) và cột STT; tích chọn hiện thanh thao tác hàng loạt |
| 318 | QLDMTCTV_05 | Pass | Thẻ có số đếm khớp số dòng; "Mới đăng ký" có huy hiệu đỏ; "Chờ phê duyệt" chỉ hiện với Cán bộ Phê duyệt |
| 319 | QLDMTCTV_06 | Pass | Biểu mẫu Thêm mới đã có Số QĐ công bố, Ngày QĐ công bố, Tệp đính kèm; tạo thử lưu đủ 3 trường |
| 320 | QLDMTCTV_09 | Pass | Biểu mẫu Sửa đủ 3 trường; 15/15 ô điền sẵn khớp dữ liệu trên 2 hồ sơ; đính kèm tệp lưu được |
| 322 | QLNDTVVCG_24 | Pass | Chuyên gia chấp nhận → cả doanh nghiệp lẫn cán bộ nghiệp vụ đều nhận thông báo đúng giây bấm |
| 323 | QLNDTVVCG_26 | Pass | Chuyên gia từ chối → cán bộ nghiệp vụ nhận thông báo có **nguyên văn lý do**; yêu cầu về lại Tiếp nhận |
| 324 | QLHSPLDN_06 | Pass | Mỗi dòng hồ sơ đã có nút Xem; mở cửa sổ chi tiết chỉ đọc kèm danh sách tệp; kiểm đủ 3 trạng thái |
| 325 | QLHSPLDN_07 | Pass | Sửa lưu thật cả 8 ô lẫn tệp mới; kiểm trên bản ghi **mới tạo** và bản ghi **cũ**, sau khi tải lại trang |
| 326 | QLTLPLCVV_17 | Pass | Nút Xem tệp hết bị vô hiệu hoá; PDF/ảnh mở xem trực tuyến, docx/xlsx tải về và là tệp thật |
| 327 | QLDMTCTV_OOS_01 | Pass | Thẻ "Chờ phê duyệt" có huy hiệu nền đỏ đúng bằng thẻ "Mới đăng ký" |
| 328 | QLDMTCTV_OOS_02 | Pass | Cột Công khai là công tắc bấm được, mở đúng hộp thoại công khai / hủy công khai |
| 329 | QLDMTCTV_OOS_03 | Pass | Nhóm lệnh "..." đủ theo vai trò và trạng thái; mỗi lệnh mở hộp xác nhận, Trình phê duyệt chạy trọn |
| 333 | QLDMTCTV_OOS_07 | Pass | Vùng rỗng có hình minh họa + câu hướng dẫn; thẻ "Mới đăng ký" có nút thêm |
| 334 | QLDMTCTV_OOS_08 | Pass | Biểu mẫu chia đủ 6 nhóm có tiêu đề, bấm tiêu đề co giãn được cả hai chiều |
| 335 | QLDMTCTV_OOS_09 | Pass | Đường dẫn khi Sửa ghi "Chỉnh sửa" kèm tên tổ chức, không còn cấp "Chi tiết" |
| 336 | QLDMTCTV_OOS_10 | Pass | Cả 5 nhãn đã đổi đúng đặc tả, giống nhau ở Thêm mới và Chỉnh sửa |
| 337 | QLDMTCTV_OOS_11 | Pass | Màn Chi tiết đủ 3 tab có dữ liệu, có vùng tệp đính kèm với nút Xem/Tải, có Lĩnh vực |
| 338 | QLDMTCTV_OOS_12 | Pass | Tìm theo người đại diện ra đúng tổ chức (4/4 phép thử); gợi ý đã ghi đủ mã, tên, người đại diện |

## Phát hiện thêm — đã đối chiếu đặc tả + đo lại (04/08/2026 16:20–17:30)

Đã tra từng mục vào bản đặc tả chốt (`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`) rồi đo lại
trên bản dựng `index-DpIXRGaI.js`. Kết quả: **3 mục là lỗi thật**, thêm **1 mục mới phát hiện lúc đo**,
**3 mục không phải lỗi**.

### Đã log thành dòng riêng trên sheet (mã đặt theo module của lỗi)

| Mã TC | Dòng | Nơi gặp | Nội dung | Đặc tả đối chiếu |
|---|---:|---|---|---|
| `QLDMTCTV_OOS_14` | 340 | Danh sách Tổ chức tư vấn | Chọn lệnh trong nhóm "..." ở danh sách → trang nền nhảy sang màn Chi tiết rồi hộp thoại mới hiện; bấm Hủy đứng lại ở Chi tiết, mất tab + bộ lọc | `srs-fr-04` dòng 1646 (mỗi mục chỉ mở hộp thoại) + dòng 1640 (chỉ bấm TÊN mới sang Chi tiết) |
| `QLDMTCTV_OOS_15` | 341 | Danh sách Tổ chức tư vấn | Nhóm "..." của dòng "Đang hoạt động" chỉ có "Xóa", thiếu "Cập nhật trạng thái" (8/8 dòng, trong đó 7 dòng cùng đơn vị) | `srs-fr-04` dòng 1646 |
| `QLDMTCTV_OOS_16` | 342 | Chi tiết Tổ chức tư vấn | Nút quay lại ghi "← Danh sách" thay vì "← Quay lại danh sách" | `srs-fr-04` dòng 1716 |
| `QLNDTVVCG_OOS_01` | 343 | Tư vấn chuyên sâu — chuyên gia từ chối nhiệm vụ | Bấm [Từ chối nhiệm vụ] nhưng khung thông báo ghi **"Đã xác nhận"** (1 request, 1 khung thông báo, đo bằng bộ bắt thông báo dùng chung) | `srs-fr-12` dòng 186 (luồng chấp nhận) vs dòng 196–197 (luồng từ chối) |

`QLDMTCTV_OOS_15` là mục **mới phát hiện trong lúc đo lại mục #1** — không nằm trong 6 mục ghi nhận ban đầu.

### Kết luận từng mục ban đầu

| # cũ | Kết luận | Căn cứ |
|---:|---|---|
| 1 | **Là lỗi** → `QLDMTCTV_OOS_14` | Tái hiện được với lệnh "Trình phê duyệt". Lệnh "Xóa" thì KHÔNG bị, nên phạm vi hẹp hơn ghi nhận ban đầu |
| 2a | **Là lỗi** → `QLDMTCTV_OOS_16` | Nhãn nút lệch đặc tả dòng 1716 |
| 2b | **Không phải lỗi** | Cột "Ngày tham gia" trống ở 13/13 bản ghi liên kết của 8 tổ chức, nhưng `srs-fr-04` dòng 2128 khai trường `ngay_tham_gia` là **không bắt buộc**, không có ô nhập ở bất kỳ màn nào và không bước xử lý nào đặt giá trị ⇒ ứng dụng đang đúng đặc tả. Nếu muốn có dữ liệu thì phải yêu cầu BA bổ sung đặc tả |
| 3 | **Là lỗi** → `QLNDTVVCG_OOS_01` | Đã đo lại bằng dữ liệu tự dựng, bắt được đúng 1 khung thông báo "Đã xác nhận" cho thao tác từ chối. Riêng vế "không quay về danh sách": đặc tả dòng 1162 không quy định điều hướng sau thao tác ⇒ **không log**, chỉ ghi nhận |
| 4 | **Không phải lỗi** | Đặc tả `srs-fr-08` FR-VI-08 (dòng 626) chỉ yêu cầu "Gửi thông báo CB PD", không quy định chữ trên khung thông báo ⇒ lệch chữ với phiếu là chuyện của phiếu, cùng lắm là **cần BA xác nhận** |
| 5 | **Không phải lỗi của ứng dụng** | Đặc tả `SCR-IV-NEW-03` (dòng 1729) quy định mỗi tệp có **nút "Xem"**, không quy định tên tệp bấm được ⇒ bước trong phiếu ghi sai, cần phản hồi lại bên viết phiếu |
| 6 | **Không phải phát hiện mới** | Trùng `QLDMTCTV_OOS_04` đã Reject vòng 1 |

### Ghi nhận thêm, chưa đủ căn cứ để log

- Màn danh sách Tư vấn chuyên sâu: thẻ đếm tab ("Chờ xử lý 37" / "Đang tư vấn 6" / "Hoàn thành 12") đếm **toàn hệ thống**,
  còn bảng bên dưới chỉ hiện bản ghi của chính chuyên gia đang đăng nhập (0 / 3 / 7). Chưa tra đặc tả phạm vi đếm nên
  chưa kết luận — cần đo thêm ở vòng sau.

## Dữ liệu QA tự tạo trên môi trường (để dev/BA biết mà bỏ qua)

- Hồ sơ pháp lý DN `HSPL-20260804-0001` (DN-XX-0005) — tạo mới rồi sửa để kiểm QLHSPLDN_07; tên chứa `QA-HSPL-V2-0408-742199`.
- Hồ sơ pháp lý DN `HSPL-20260731-0002` — đổi tên thành "Ho so x - SUA CU v2 742199" + thêm 1 tệp.
- Vụ việc `VV-BTP-TW-20260525-001` — thêm 1 lần cập nhật kết quả (nội dung chứa `QA-KQ-V2-0408-742199`) + 1 tệp.
- `TVCS-20260803-0003` chuyển sang "Đang tư vấn"; `TVCS-20260804-0005` bị từ chối, về "Tiếp nhận" (lý do chứa `QA-LYDO-V2-0408-742199`).
- Đợt đánh giá `DG-20260526-0003` chuyển sang "Chờ phê duyệt".
- **Khi đo QLDKTK_01 (04/08 15:20–15:30):** 5 doanh nghiệp + 5 tài khoản Chờ kích hoạt mới — mã số thuế
  `0311224455` `0311224477` `0311224488` `0311552277` `0311663388` (tên đều bắt đầu bằng "QA "), thuộc TP.HCM
  và An Giang, kèm 4 thư kích hoạt trong MailHog.
  **Đừng xóa bằng tay** — xóa sẽ tạo lỗ hổng trong dãy số của 2 tỉnh đó và làm chúng dính đúng lỗi của Hà Nội.
- **Khi đo phát hiện thêm (04/08 16:20–17:30):** `TVCS-20260804-0010` được phân công cho chuyên gia `huongcg`
  rồi cho từ chối để đo khung thông báo → bản ghi hiện về lại trạng thái **"Tiếp nhận"** và **không còn chuyên gia**.
  Ghi chú phân công chứa `QA dung lai dieu kien do thong bao khi chuyen gia tu choi phan cong`,
  lý do từ chối chứa `QA-TUCHOI-0408-checkthongbao`.
