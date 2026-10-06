# ĐỐI TÁC vòng 1 `Reopent` → DRIVE cột `Verify` đang là gì — Tuần 3

> ⛔ Báo cáo CHỈ ĐỌC — không ghi/sửa ô nào trên 2 spreadsheet.

**43 case bên đối tác đang `Reopent` ở vòng 1 · 43 map được sang DRIVE · 0 không tìm thấy bên DRIVE**

| Tuần | Số case `Reopent` |
|---|---|
| Tuần 3 | 43 |
| **Tổng** | **43** |

## Bên DRIVE, cột `Verify` của các case đó

| DRIVE `Verify` | Số case | Tỷ lệ /43 |
|---|---|---|
| `Pass` | 24 | 55% |
| `Reject` | 19 | 44% |

Bắt chéo với `Trạng thái dev fix 1` bên DRIVE:

| DRIVE `Trạng thái dev fix 1` | DRIVE `Verify` | Số case | Đọc là gì |
|---|---|---|---|
| `dev done` | `Pass` | 24 | DRIVE coi như xong, đối tác vẫn mở lại → **bất đồng** |
| `Reject` | `Reject` | 19 | DRIVE khẳng định không phải lỗi, đối tác mở lại → **đối đầu** |

> 🔴 **Không dòng nào bên DRIVE phản ánh việc đối tác đã mở lại.** Cả 43 case bên DRIVE đều đã ở trạng thái kết luận (`Pass` hoặc `Reject`) — không có ô `Verify` nào để trống, `Reopen`, hay `InProcess`. Hai bên đang lệch pha hoàn toàn ở nhóm này: đối tác coi là còn mở, DRIVE coi là đã đóng.

### 19 case `Reject`/`Reject` — đối tác phản bác bằng lý lẽ gì *(phân nhóm ghi tay từ ô `TKM phản hồi lần 1`)*

| Lập luận của đối tác | Số case | Mã TC |
|---|---|---|
| **Bản tài liệu**: "log đúng theo SRS bàn giao lần 2 ngày 10/7 v2.0"; VVTTG_02 nói thêm *"đến 27/7 vẫn chưa nhận được tài liệu"* mới | 8 | QLDNDHTPL_17, QLDNDHTPL_23, QLDNDHTPL_24, QLDNDHTPL_25, QLDNDHTPL_27, QLDNDHTPL_28, LKHDG_10, VVTTG_02 |
| **"Xóa bộ lọc" ≠ "Làm mới"** — cho rằng đây là 2 nút chức năng khác nhau, các màn khác đều tách rõ | 6 | SLHDVM_09, VVDTN_09, VVDHT_09, VVDHTHT_09, VVTTG_08, CLDTBDDDR_09 |
| **Biểu đồ** hiển thị sai/nén sát trục, không quan sát được | 2 | CPCTHTTLHDN_04, CPCTHTTTG_03 |
| **Tìm kiếm không kết quả** — tài liệu quy định "để trống vùng kết quả", web làm khác | 2 | QLDMCQDVQL_05, QLTKND_06 |
| **Cảnh báo vs chặn** — test case nói cảnh báo mà vẫn cho lưu, web chặn lưu | 1 | TLCTCDG_11 |

Nhóm 8 case đầu **không phải bất đồng kỹ thuật mà là bất đồng nguồn spec** — không re-verify nào giải được, phải chốt bản SRS dùng chung trước. 11 case còn lại là bất đồng cách hiểu yêu cầu, cần BA phân xử.

## Nguồn & cách map

- ĐỐI TÁC `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340) — lọc cột `Tuần` = `Tuần 3`, 961 dòng.
- DRIVE `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` — tab `tuần 3` (309 dòng).
- Bộ lọc: cột **vòng 1** `Trạng thái dev fix` bên đối tác chứa token `reopen` (chuẩn hoá `Reopent`→`reopen`). Cột vòng 2 là `Trạng thái dev fix 2`, KHÔNG tính.
- Map bằng **nội dung** `Mô tả + Kết quả mong đợi` (difflib, cùng tiền tố module, ưu tiên tab DRIVE cùng tuần), khoá phụ = **mã TC parse từ tên file** cột `Ảnh/vieo 1`. Không lấy chuỗi Mã TC làm khoá chính.

**Phân bố toàn bộ cột `Trạng thái dev fix` (vòng 1) bên đối tác:**

| Giá trị | Số dòng |
|---|---|
| `(trống)` | 644 |
| `dev done` | 180 |
| `Resoved` | 75 |
| `Reopent` | 43 |
| `Reject` | 1 |

## Chi tiết từng case

### DRIVE `dev fix 1 = dev done` · `Verify = Pass` — 24 case

| Tuần | Dòng đối tác | Mã TC đối tác | Mô tả | ĐỐI TÁC nói gì (`TKM phản hồi lần 1`) | Dòng DRIVE | Mã TC DRIVE | DRIVE `Verify` | Map |
|---|---|---|---|---|---|---|---|---|
| Tuần 3 | 564 | XNTGHTVV_04 | Xác nhận thành công | TKM retest 27/7: CBNV vẫn không nhận được thông báo | 3 (tuần 3) | XNTGHTVV_04 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 575 | PDHSVV_02 | Phê duyệt thành công | TKM retest 27/7: Lỗi chưa được fix | 7 (tuần 3) | PDHSVV_02 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 592 | CNKQHT_03 | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết quả hỗ trợ | TKM retest 27/7: Lỗi chưa được fix | 11 (tuần 3) | CNKQHT_03 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 598 | CNKQVV_02 | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết luận cuối | TKM retest 30/7: Lỗi vẫn chưa được fix | 13 (tuần 3) | CNKQVV_02 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 603 | DGKQHTVV_01 | Cung cấp chức năng để CB Nghiệp vụ hoặc DNNVV đánh giá chất lượng của… | TKM retest 27/7: Hệ thống vẫn chưa có nút chức năng | 15 (tuần 3) | DGKQHTVV_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 697 | QLDNDHTPL_13 | Thêm mới Nếu trường Tỉnh/Thành phố chưa nhập | TKM retest 30/7: Lỗi chưa được fix | 30 (tuần 3) | QLDNDHTPL_13 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 732 | LKHDG_12 | Xuất Excel | TKM retest 30/7: Hệ thống xuất danh sách không đúng với tiêu chí lọc | 49 (tuần 3) | LKHDG_12 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 766 | PCNTHDG_11 | Trình phê duyệt thành công | TKM retest 27/7: Lỗi chưa được fix | 62 (tuần 3) | PCNTHDG_11 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 767 | PDPCDG_01 | Lãnh đạo CQQLNN phê duyệt danh sách người thực hiện đánh giá. | TKM retest 27/7: Lỗi chưa được fix | 63 (tuần 3) | PDPCDG_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 771 | PDPCDG_05 | Từ chối thành công | TKM retest 27/7: Lỗi chưa được fix | 64 (tuần 3) | PDPCDG_05 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 792 | PDBCDG_01 | Lãnh đạo CQQLNN xem xét và phê duyệt báo cáo đánh giá. | TKM retest 27/7: Lỗi chưa được fix | 78 (tuần 3) | PDBCDG_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 795 | PDBCDG_04 | Từ chối báo cáo thành công | TKM retest 27/7: Lỗi chưa được fix | 79 (tuần 3) | PDBCDG_04 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 841 | QLBMHD_02 | Kiểm tra hiển thị các trường thông tin | TKM retest 27/7: Thiếu cột "Cơ quan ban hành" | 97 (tuần 3) | QLBMHD_02 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 842 | QLBMHD_03 | Kiểm tra nút chức năng "+ Thêm mới" | TKM retest 27/7: - Thiếu trường thông tin"Cơ quan ban hành" - Têp đính kèm đã pass | 98 (tuần 3) | QLBMHD_03 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1067 | QLDMTCDGHTCP_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | - Nhãn trường thông tin không chính xác dẫn đến việc hiểu sai và nhập sai dữ liệu đầu vào của bản ghi nên đây không chỉ là vấn đề tăng tính… | 160 (tuần 3) | QLDMTCDGHTCP_06 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1073 | QLDMTCDGHTCP_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | - Nhãn trường thông tin không chính xác dẫn đến việc hiểu sai và nhập sai dữ liệu đầu vào của bản ghi nên đây không chỉ là vấn đề tăng tính… | 161 (tuần 3) | QLDMTCDGHTCP_12 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1205 | QLDX_01 | Quản lý quy trình kết thúc phiên làm việc của người dùng. | TKM retest 28/7: Không hiển thị thông báo | 182 (tuần 3) | QLDX_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1206 | QLDX_02 | Kiểm tra Hộp thoại xác nhận đăng xuất | TKM retest 28/7: Không hiển thị hộp thoại xác nhận | 183 (tuần 3) | QLDX_02 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1212 | QLDKTK_02 | Kiểm tra Thông tin doanh nghiệp | TKM retest 28/7: Lỗi chưa được fix | 185 (tuần 3) | QLDKTK_02 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1213 | QLDKTK_03 | Kiểm tra Thông tin tài khoản | TKM retest 28/7: Lỗi chưa được fix | 186 (tuần 3) | QLDKTK_03 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1248 | VVDHT_01 | Thống kê số lượng vụ việc đang được xử lý theo đơn vị, chuyên gia. | TKM retest 28/7: Lỗi chưa được fix | 200 (tuần 3) | VVDHT_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1266 | VVTTG_01 | Thống kê diễn biến số lượng vụ việc theo các mốc thời gian (ngày, tuầ… | TKM retest 28/7: - Số liệu BC Vụ việc đã tiếp nhận > BC Vụ việc theo thời gian mặc dù chọn cùng 1 khoảng thời gian | 213 (tuần 3) | VVTTG_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1328 | VVTLV_01 | Thống kê số lượng vụ việc theo từng lĩnh vực pháp lý (Lao động, Thuế,… | TKM retest 28/7: Lỗi chưa được fix | 241 (tuần 3) | VVTLV_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1412 | CTTLV_01 | Thống kê số lượng chương trình hỗ trợ theo lĩnh vực pháp lý. | TKM retest 28/7: Lỗi chưa được xử lý | 270 (tuần 3) | CTTLV_01 | `Pass` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |

### DRIVE `dev fix 1 = Reject` · `Verify = Reject` — 19 case

| Tuần | Dòng đối tác | Mã TC đối tác | Mô tả | ĐỐI TÁC nói gì (`TKM phản hồi lần 1`) | Dòng DRIVE | Mã TC DRIVE | DRIVE `Verify` | Map |
|---|---|---|---|---|---|---|---|---|
| Tuần 3 | 701 | QLDNDHTPL_17 | Sắp xếp theo cột | TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.2.3. Chức năng trên màn hình" mô tả yêu cầu sắp xếp theo cột. | 32 (tuần 3) | QLDNDHTPL_17 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 707 | QLDNDHTPL_23 | Kiểm tra hiển thị Nhóm 1 — Thông tin doanh nghiệp (thẻ "Thông tin cơ… | - TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.3.2. Mô tả thông tin trên màn hình" - Trong video có chỉ ra… | 34 (tuần 3) | QLDNDHTPL_23 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 708 | QLDNDHTPL_24 | Kiểm tra hiển thị Nhóm 2 — Người đại diện | - TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.3.2. Mô tả thông tin trên màn hình" - Trong video có chỉ ra… | 35 (tuần 3) | QLDNDHTPL_24 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 709 | QLDNDHTPL_25 | Kiểm tra hiển thị Nhóm 3 — Tiêu chí ưu tiên theo Nghị định 55/2019/NĐ… | - TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.3.2. Mô tả thông tin trên màn hình" - Tài liệu sử dụng là t… | 36 (tuần 3) | QLDNDHTPL_25 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 711 | QLDNDHTPL_27 | Kiểm tra hiển thị Nhóm 5 — Chỉ số tổng hợp (chỉ hiển thị ở chế độ xem… | - TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.3.2. Mô tả thông tin trên màn hình" - Tài liệu sử dụng là t… | 38 (tuần 3) | QLDNDHTPL_27 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 712 | QLDNDHTPL_28 | Kiểm tra hiển thị Nhóm 6 — Danh sách vụ việc liên kết (thẻ "Lịch sử h… | - TKM phản hồi ngày 27/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.7.1.3.2. Mô tả thông tin trên màn hình" - Tài liệu sử dụng là t… | 39 (tuần 3) | QLDNDHTPL_28 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 730 | LKHDG_10 | Lưu nháp thành công | - TKM phản hồi ngày 30/7: Tài liệu SRS bàn giao lần 2 ngày 10/7 v2.0 mục "4.8.1.2.3. Chức năng trên màn hình" + Trường hợp 1 (thành công, n… | 48 (tuần 3) | LKHDG_10 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 753 | TLCTCDG_11 | Kiểm tra lưu thành công, tổng trọng số khác 100% | - Test case mô tả hiển thị thông điệp cảnh báo và vẫn cho phép lưu, không phải chặn thao tác lưu - Tài liệu cũng mô tả rõ ràng: Trường hợp… | 58 (tuần 3) | TLCTCDG_11 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 958 | QLDMCQDVQL_05 | Tìm kiếm không có kết quả | - Theo tài liệu nghiệp vụ được bàn giao, hành vi của hệ thống khi tìm kiếm không có kết quả đã được mô tả rõ: "Hệ thống để trống vùng kết q… | 139 (tuần 3) | QLDMCQDVQL_05 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1117 | QLTKND_06 | Tìm kiếm không có kết quả | - Theo tài liệu nghiệp vụ được bàn giao, hành vi của hệ thống khi tìm kiếm không có kết quả đã được mô tả rõ: "Hệ thống để trống vùng kết q… | 167 (tuần 3) | QLTKND_06 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1238 | SLHDVM_09 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 194 (tuần 3) | SLHDVM_09 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1247 | VVDTN_09 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 199 (tuần 3) | VVDTN_09 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1256 | VVDHT_09 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 206 (tuần 3) | VVDHT_09 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1265 | VVDHTHT_09 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 212 (tuần 3) | VVDHTHT_09 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1267 | VVTTG_02 | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | - Hiện tại đơn vị KTĐL Log bug đúng theo tài liệu được bàn giao vào ngày 10/7(v2.0)-trên nhóm zalo(đến ngày 27/7 vẫn chưa nhận được tài liệ… | 214 (tuần 3) | VVTTG_02 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1273 | VVTTG_08 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 219 (tuần 3) | VVTTG_08 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1282 | CLDTBDDDR_09 | Kiểm tra chức năng Xóa bộ lọc | - Xóa bộ lọc và Làm mới là 2 nút chức năng hoàn toàn khác nhau và các màn hình chức năng khác đều có phân rõ ràng 2 nút chức năng này + Làm… | 225 (tuần 3) | CLDTBDDDR_09 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1382 | CPCTHTTLHDN_04 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | - Về nội dung hiển thị của biểu đồ: + Theo Test case và tài liệu thiết kế, kết quả mong đợi quy định: Biểu đồ cột nhóm theo Loại hình và Mứ… | 256 (tuần 3) | CPCTHTTLHDN_04 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |
| Tuần 3 | 1390 | CPCTHTTTG_03 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | Hiện tại, các chỉ số như Số hồ sơ và Tỷ lệ bị nén sát trục khiến trục tung chỉ hiển thị giá trị 0, người dùng không thể quan sát và so sánh… | 259 (tuần 3) | CPCTHTTTG_03 | `Reject` | <sub>sim 1.00 · A(tuần+module) · ảnh khớp mã</sub> |

**Lệch Mã TC hai bên sau khi map: 0/43 dòng.**

