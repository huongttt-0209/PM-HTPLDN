# DRIVE `dev done` + `Verify Pass` → ĐỐI TÁC đã map chưa — Tuần 3

> ⛔ Báo cáo CHỈ ĐỌC — không ghi/sửa ô nào trên 2 spreadsheet.

**213 case lọt bộ lọc · 180 đã map (`dev done`) · 24 chưa map · 9 không có bên đối tác**

> 🔴 **Đọc kỹ trước khi coi 24 dòng lệch là "đối tác quên cập nhật"** *(đoạn này ghi tay, không do script sinh)*
>
> 22/24 dòng có ô `TKM phản hồi lần 1` ghi rõ **"TKM retest …: Lỗi chưa được fix"** — tức đối tác đã retest và **vẫn thấy lỗi**. Đây là **bất đồng kết luận** giữa QA nội bộ (`Verify = Pass`) và đối tác, KHÔNG phải chậm cập nhật trạng thái. Giục đối tác đổi `Reopent` → `dev done` là sai bản chất; phải **re-verify vòng 2** trước.
>
> Ngày 2026-07-28 tool `sheet_w3_partner_reopen_dev.py` + `sheet_w3_reopen_append_fix.py` đã ghi `Reopen, dev done` vào cột `Trạng thái dev fix 1` cho **19 dòng** trong đúng nhóm này (xem `tools/sheet_w3_reopen_append_fix.log`). Hiện **cả 19 dòng đã về `dev done` thuần** — cột nguồn bên DRIVE có `0 dòng` chứa token `Reopen`. Dấu vết "đối tác đã mở lại" **đã bị gỡ khỏi DRIVE**, nên bộ lọc `dev done + Pass` giờ nuốt luôn cả nhóm đang tranh chấp. Cần chốt: gỡ token đó là chủ ý hay nhầm.
>
> 🔴 **`dev done` bên đối tác KHÔNG phải đối tác tự xác nhận — do chính phía QA ghi sang.** Log `tools/sheet2_verify_apply_w3.log` (2026-07-23, 113 ô) + `tools/sheet2_pass_devdone_w3.log` (2026-07-25, 74 ô) cho thấy cột `Trạng thái dev fix` bên đối tác được ghi bằng tool từ `Verify = Pass` bên DRIVE. Vì vậy **"180 đã map" chỉ chứng minh QA đã đồng bộ xong, KHÔNG chứng minh đối tác đã nghiệm thu.** Ý kiến thật của đối tác nằm ở `Trạng thái 2` + `TKM phản hồi` — xem mục "Vòng 2 bên ĐỐI TÁC" bên dưới.

| Bên đối tác đang để | Số case | Mã TC |
|---|---|---|
| `Reopent` | 24 | XNTGHTVV_04, PDHSVV_02, CNKQHT_03, CNKQVV_02, DGKQHTVV_01, QLDNDHTPL_13, LKHDG_12, PCNTHDG_11, PDPCDG_01, PDPCDG_05, PDBCDG_01, PDBCDG_04, QLBMHD_02, QLBMHD_03, QLDMTCDGHTCP_06, QLDMTCDGHTCP_12, QLDX_01, QLDX_02, QLDKTK_02, QLDKTK_03, VVDHT_01, VVTTG_01, VVTLV_01, CTTLV_01 |

**Chia nhóm theo NỘI DUNG ô `TKM phản hồi lần 1` (không theo ô dropdown):**

- **22 case — đối tác retest thấy VẪN LỖI** (`TKM retest …`): `XNTGHTVV_04`, `PDHSVV_02`, `CNKQHT_03`, `CNKQVV_02`, `DGKQHTVV_01`, `QLDNDHTPL_13`, `LKHDG_12`, `PCNTHDG_11`, `PDPCDG_01`, `PDPCDG_05`, `PDBCDG_01`, `PDBCDG_04`, `QLBMHD_02`, `QLBMHD_03`, `QLDX_01`, `QLDX_02`, `QLDKTK_02`, `QLDKTK_03`, `VVDHT_01`, `VVTTG_01`, `VVTLV_01`, `CTTLV_01`
- **2 case — đối tác lập luận đặc tả**, không phải kết quả retest: `QLDMTCDGHTCP_06`, `QLDMTCDGHTCP_12`

| Ngày đối tác retest | Số case | Mã TC |
|---|---|---|
| 27/7 | 11 | XNTGHTVV_04, PDHSVV_02, CNKQHT_03, DGKQHTVV_01, PCNTHDG_11, PDPCDG_01, PDPCDG_05, PDBCDG_01, PDBCDG_04, QLBMHD_02, QLBMHD_03 |
| 28/7 | 8 | QLDX_01, QLDX_02, QLDKTK_02, QLDKTK_03, VVDHT_01, VVTTG_01, VVTLV_01, CTTLV_01 |
| 30/7 | 3 | CNKQVV_02, QLDNDHTPL_13, LKHDG_12 |

## Nguồn & cách map

- DRIVE `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` tab `UAT_TGPL Doanh Nghiệp-tuần 3` (gid 387857822) — 309 dòng có nội dung.
- ĐỐI TÁC `1dJat1cc68-TNuX_ibzBK-0NcgOWvPLu6aioiEgeUa5c` tab `UAT_TGPL Doanh Nghiệp` (gid 799081340) — 1637 dòng có nội dung.
- Bộ lọc: `Trạng thái dev fix 1` chứa token `dev done` **và** `Verify` = `Pass` → 213 dòng (213 dòng đúng bằng `dev done`, 0 dòng đa-trạng thái `Reopen, dev done`).
- Map case bằng **nội dung** `Mô tả + Kết quả mong đợi` (chuẩn hoá khoảng trắng + lowercase, `difflib`, trong cùng tiền tố module), khoá phụ là **mã TC parse từ tên file** cột `Ảnh/vieo 1` bên đối tác. Không lấy chuỗi Mã TC làm khoá chính.
- Đối chiếu Mã TC hai bên sau khi map: **0/213 dòng lệch mã**.
- So trạng thái theo **tập token** (tách dấu phẩy), chuẩn hoá `Resoved`→`resolved`, `Reopent`→`reopen`. Dữ liệu gốc giữ nguyên văn trong bảng.

**Phân bố cột nguồn bên DRIVE:**

| Số dòng | `Trạng thái dev fix 1` | `Verify` |
|---|---|---|
| 213 | `dev done` | `Pass` |
| 51 | `Reject` | `Reject` |
| 45 | `Reject` | `Resolved` |

## Vòng 2 bên ĐỐI TÁC của 180 case đã map

Cột `Trạng thái 2` (đối tác tự chấm lại) và `Trạng thái dev fix 2` của đúng các dòng đối tác đã về `dev done`.

| `Trạng thái 2` bên đối tác | Số case | Tỷ lệ /180 |
|---|---|---|
| `(trống)` | 143 | 79% |
| `Pass` | 34 | 18% |
| `Fail` | 3 | 1% |

Bắt chéo với `Trạng thái dev fix 2`:

| `Trạng thái 2` | `Trạng thái dev fix 2` | Số case |
|---|---|---|
| `(trống)` | `(trống)` | 143 |
| `Pass` | `(trống)` | 34 |
| `Fail` | `(trống)` | 3 |

**⚠️ 3 case đối tác đã chấm vòng 2 nhưng KHÔNG phải `Pass` — mâu thuẫn ngay trong file đối tác (`dev fix = dev done` nhưng `Trạng thái 2` báo hỏng):**

| Dòng DRIVE | Mã TC | Dòng đối tác | `Trạng thái 2` | `Trạng thái dev fix 2` | `TKM phản hồi lần 1` |
|---|---|---|---|---|---|
| 2 | XNTGHTVV_03 | 563 | `Fail` | `(trống)` | (trống) |
| 16 | QLHSDNHTCP_03 | 617 | `Fail` | `(trống)` | (trống) |
| 50 | LKHDG_16 | 736 | `Fail` | `(trống)` | (trống) |

*(3 dòng dưới đây ghi tay — script không đọc cột `Kết quả thực tế lần 2`.)*

Đối tác không ghi `TKM phản hồi lần 2`, nhưng có ghi **`Kết quả thực tế lần 2` (cột R) + `Ảnh/video 2` (cột S)**. Cả 3 đều là **triệu chứng MỚI, khác lần 1** — nên đây không phải đối tác quên đóng, mà là lỗi còn sót sau khi dev fix:

| Mã TC | Lỗi lần 1 (đã fix) | `Kết quả thực tế lần 2` — lỗi còn lại | Bằng chứng |
|---|---|---|---|
| `XNTGHTVV_03` | Từ chối xong bị đá sang trang 403 | "Cán bộ nghiệp vụ phụ trách không nhận được thông báo kèm lý do từ chối" — vẫn nằm trong `Kết quả mong đợi` của case | `XNTGHTVV_03_v2.webm` |
| `QLHSDNHTCP_03` | Cột "Mức cảnh báo thời hạn" không giống thiết kế | "Dữ liệu cột *Mức cảnh báo thời hạn* bị tràn sang cột *Ngày nộp*" | `QLHSDNHTCP_03_v2.png` |
| `LKHDG_16` | Bấm "Sửa" không mở được màn chỉnh sửa | "Không hiển thị danh sách các tệp đính kèm mặc dù tồn tại dữ liệu" | `LKHDG_16.webm` |

**Thêm một dấu hiệu nội bộ DRIVE tự mâu thuẫn** — chính ô `DEV phản hồi lần 1` (cột R) bên DRIVE của 3 dòng này vẫn đang viết là chưa xong, trong khi `Verify` = `Pass`:

- `XNTGHTVV_03` (DRIVE dòng 2): *"✅ Bug ĐÚNG – chuyển dev…"*
- `QLHSDNHTCP_03` (DRIVE dòng 16): *"…- **Còn lỗi**: hồ sơ còn trong hạn vẫn bị báo quá hạn… - **Còn lỗi**: hồ sơ mới trễ ít bị đẩy lên mức nặng nhất…"*
- `LKHDG_16` (DRIVE dòng 50): *"✅ Bug ĐÚNG – chuyển dev…"*

Hoặc note cột R đã cũ (viết ở vòng trước khi dev fix) và chưa được ghi đè, hoặc ô `Verify = Pass` chấm sai. Phải mở từng case xác định, không suy đoán.

Riêng `QLHSDNHTCP_03`: log `tools/sheet2_pass_devdone_w3.log` phiên `2026-07-25 15:17:34` ghi `P651 QLHSDNHTCP_03 'InProcess'->'dev done' OK` — tức chính phía QA đã đẩy ô này sang `dev done`, còn đối tác thì chấm `Trạng thái 2 = Fail`.

## ⚠️ CHƯA map sang đối tác — 24 case

DRIVE coi như xong (dev fix + QA verify Pass) nhưng cột `Trạng thái dev fix` bên đối tác chưa về `dev done`.

| Dòng DRIVE | Mã TC DRIVE | Mô tả | DRIVE dev fix / Verify | Dòng đối tác | Mã TC đối tác | ĐỐI TÁC dev fix | ĐỐI TÁC Trạng thái 2 / dev fix 2 | Đối tác nói gì (`TKM phản hồi lần 1`) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|
| 3 | XNTGHTVV_04 | Xác nhận thành công | `dev done` / `Pass` | 564 | XNTGHTVV_04 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: CBNV vẫn không nhận được thông báo | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 7 | PDHSVV_02 | Phê duyệt thành công | `dev done` / `Pass` | 575 | PDHSVV_02 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 11 | CNKQHT_03 | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết quả hỗ trợ | `dev done` / `Pass` | 592 | CNKQHT_03 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 13 | CNKQVV_02 | Kiểm tra hiển thị các trường thông tin Nhóm 6 – Kết luận cuối | `dev done` / `Pass` | 598 | CNKQVV_02 | `Reopent` | `(trống)` / `(trống)` | TKM retest 30/7: Lỗi vẫn chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 15 | DGKQHTVV_01 | Cung cấp chức năng để CB Nghiệp vụ hoặc DNNVV đánh giá chất lượng của quá trình… | `dev done` / `Pass` | 603 | DGKQHTVV_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Hệ thống vẫn chưa có nút chức năng | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 30 | QLDNDHTPL_13 | Thêm mới Nếu trường Tỉnh/Thành phố chưa nhập | `dev done` / `Pass` | 697 | QLDNDHTPL_13 | `Reopent` | `(trống)` / `(trống)` | TKM retest 30/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 49 | LKHDG_12 | Xuất Excel | `dev done` / `Pass` | 732 | LKHDG_12 | `Reopent` | `(trống)` / `(trống)` | TKM retest 30/7: Hệ thống xuất danh sách không đúng với tiêu chí lọc | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 62 | PCNTHDG_11 | Trình phê duyệt thành công | `dev done` / `Pass` | 766 | PCNTHDG_11 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 63 | PDPCDG_01 | Lãnh đạo CQQLNN phê duyệt danh sách người thực hiện đánh giá. | `dev done` / `Pass` | 767 | PDPCDG_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 64 | PDPCDG_05 | Từ chối thành công | `dev done` / `Pass` | 771 | PDPCDG_05 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 78 | PDBCDG_01 | Lãnh đạo CQQLNN xem xét và phê duyệt báo cáo đánh giá. | `dev done` / `Pass` | 792 | PDBCDG_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 79 | PDBCDG_04 | Từ chối báo cáo thành công | `dev done` / `Pass` | 795 | PDBCDG_04 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 97 | QLBMHD_02 | Kiểm tra hiển thị các trường thông tin | `dev done` / `Pass` | 841 | QLBMHD_02 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: Thiếu cột "Cơ quan ban hành" | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 98 | QLBMHD_03 | Kiểm tra nút chức năng "+ Thêm mới" | `dev done` / `Pass` | 842 | QLBMHD_03 | `Reopent` | `(trống)` / `(trống)` | TKM retest 27/7: - Thiếu trường thông tin"Cơ quan ban hành" - Têp đính kèm đã pass | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 160 | QLDMTCDGHTCP_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1067 | QLDMTCDGHTCP_06 | `Reopent` | `(trống)` / `InProcess` | - Nhãn trường thông tin không chính xác dẫn đến việc hiểu sai và nhập sai dữ liệu đầu vào của bản ghi nên đây không chỉ là vấn đề tăng tính nhất quán… | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 161 | QLDMTCDGHTCP_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1073 | QLDMTCDGHTCP_12 | `Reopent` | `(trống)` / `InProcess` | - Nhãn trường thông tin không chính xác dẫn đến việc hiểu sai và nhập sai dữ liệu đầu vào của bản ghi nên đây không chỉ là vấn đề tăng tính nhất quán… | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 182 | QLDX_01 | Quản lý quy trình kết thúc phiên làm việc của người dùng. | `dev done` / `Pass` | 1205 | QLDX_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Không hiển thị thông báo | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 183 | QLDX_02 | Kiểm tra Hộp thoại xác nhận đăng xuất | `dev done` / `Pass` | 1206 | QLDX_02 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Không hiển thị hộp thoại xác nhận | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 185 | QLDKTK_02 | Kiểm tra Thông tin doanh nghiệp | `dev done` / `Pass` | 1212 | QLDKTK_02 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 186 | QLDKTK_03 | Kiểm tra Thông tin tài khoản | `dev done` / `Pass` | 1213 | QLDKTK_03 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 200 | VVDHT_01 | Thống kê số lượng vụ việc đang được xử lý theo đơn vị, chuyên gia. | `dev done` / `Pass` | 1248 | VVDHT_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 213 | VVTTG_01 | Thống kê diễn biến số lượng vụ việc theo các mốc thời gian (ngày, tuần, tháng,… | `dev done` / `Pass` | 1266 | VVTTG_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: - Số liệu BC Vụ việc đã tiếp nhận > BC Vụ việc theo thời gian mặc dù chọn cùng 1 khoảng thời gian | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 241 | VVTLV_01 | Thống kê số lượng vụ việc theo từng lĩnh vực pháp lý (Lao động, Thuế, Đất đai..… | `dev done` / `Pass` | 1328 | VVTLV_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Lỗi chưa được fix | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 270 | CTTLV_01 | Thống kê số lượng chương trình hỗ trợ theo lĩnh vực pháp lý. | `dev done` / `Pass` | 1412 | CTTLV_01 | `Reopent` | `(trống)` / `(trống)` | TKM retest 28/7: Lỗi chưa được xử lý | ⚠️ Chưa map<br>đối tác `Reopent` ≠ `dev done`<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |

## 🚫 Không tìm thấy case tương ứng bên đối tác — 9 case

Case QA tự mở hoặc nội dung đã bị sửa quá nhiều — đã quét toàn bộ tab đối tác.

| Dòng DRIVE | Mã TC DRIVE | Mô tả | DRIVE dev fix / Verify | Dòng đối tác | Mã TC đối tác | ĐỐI TÁC dev fix | ĐỐI TÁC Trạng thái 2 / dev fix 2 | Đối tác nói gì (`TKM phản hồi lần 1`) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|
| 302 | QLTMBMHD_OOS_01 | Thông báo lỗi trùng tên không chèn tên thư mục cụ thể theo mẫu ERR-TM-01 | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `QLTMBMHD_07` (dòng 804) sim 0.52 |
| 303 | XNTGHTVV_OOS_01 | Vụ việc bị tư vấn viên từ chối, quay về 'Đã tiếp nhận' để phân công lại, nhưng… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `XNTGHTVV_05` (dòng 565) sim 0.17 |
| 304 | XNTGHTVV_OOS_02 | Yêu cầu phân công bị máy chủ từ chối (HTTP 409, không lưu thay đổi) nhưng vẫn g… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `XNTGHTVV_05` (dòng 565) sim 0.17 |
| 305 | CGTVPL_LINHVUC | BC Số lượng CG/TVV (UC131) không hiển thị mục thống kê "theo lĩnh vực chuyên mô… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `CGTVPL_01` (dòng 1292) sim 0.35 |
| 306 | QLNDTVVCG_CONGKHAI | Màn Chi tiết TVCS (SCR-X1-02): nhóm accordion "Trạng thái công khai" (Công khai… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `QLNDTVVCG_15` (dòng 1443) sim 0.28 |
| 307 | QLDNDHTPL_OOS_01 | Chỉnh sửa Doanh nghiệp — QA phát hiện ngoài phạm vi (không thuộc các case đối t… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `QLDNDHTPL_20` (dòng 704) sim 0.14 |
| 308 | QLTLPLCVV_OOS_01 | Sửa tư liệu pháp lý trong Tư vấn chuyên sâu — QA phát hiện ngoài phạm vi (không… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `QLTLPLCVV_09` (dòng 1507) sim 0.16 |
| 309 | QLBMHD_OOS_01 | Chỉnh sửa biểu mẫu — QA phát hiện ngoài phạm vi (không thuộc case nào của đối t… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `QLBMHD_09` (dòng 848) sim 0.20 |
| 310 | IBMHD_OOS_01 | Nhập biểu mẫu hàng loạt — QA phát hiện ngoài phạm vi (không thuộc case nào của… | `dev done` / `Pass` | (trống) | (trống) | `(trống)` | (trống) | (trống) | 🚫 Không có bên đối tác<br>gần nhất `IBMHD_04` (dòng 870) sim 0.18 |

## ✅ Đã map đúng — 180 case

| Dòng DRIVE | Mã TC DRIVE | Mô tả | DRIVE dev fix / Verify | Dòng đối tác | Mã TC đối tác | ĐỐI TÁC dev fix | ĐỐI TÁC Trạng thái 2 / dev fix 2 | Đối tác nói gì (`TKM phản hồi lần 1`) | Kết luận |
|---|---|---|---|---|---|---|---|---|---|
| 2 | XNTGHTVV_03 | Từ chối thành công | `dev done` / `Pass` | 563 | XNTGHTVV_03 | `dev done` | `Fail` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 4 | TPDHSVV_02 | Kiểm tra hồ sơ chưa có kết quả hỗ trợ của người hỗ trợ | `dev done` / `Pass` | 567 | TPDHSVV_02 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 5 | TPDHSVV_04 | Trình phê duyệt thành công | `dev done` / `Pass` | 569 | TPDHSVV_04 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 8 | PDHSVV_03 | Cán bộ phê duyệt không cùng đơn vị với đơn vị hồ sơ | `dev done` / `Pass` | 576 | PDHSVV_03 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 9 | PDHSVV_04 | Từ chối | `dev done` / `Pass` | 577 | PDHSVV_04 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 10 | PDHSVV_05 | Từ chối thành công | `dev done` / `Pass` | 578 | PDHSVV_05 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 12 | CNKQHT_06 | Hồ sơ đã được người khác cập nhật trong lúc đang sửa | `dev done` / `Pass` | 595 | CNKQHT_06 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 14 | CNKQVV_05 | Hồ sơ đã được người khác cập nhật trong lúc đang thao tác | `dev done` / `Pass` | 601 | CNKQVV_05 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 16 | QLHSDNHTCP_03 | Kiểm tra Cột dữ liệu trong bảng kết quả | `dev done` / `Pass` | 617 | QLHSDNHTCP_03 | `dev done` | `Fail` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 18 | QLHSDNHTCP_09 | Kiểm tra hiển thị thanh tiến trình và tiêu đề trang | `dev done` / `Pass` | 623 | QLHSDNHTCP_09 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 19 | QLHSDNHTCP_10 | Nhóm 0 — Thanh thông tin tổng quan hồ sơ | `dev done` / `Pass` | 624 | QLHSDNHTCP_10 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 20 | QLHSDNHTCP_11 | Nhóm 1 — Thông tin doanh nghiệp (chỉ đọc, lấy từ Cổng Dịch vụ công) | `dev done` / `Pass` | 625 | QLHSDNHTCP_11 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 21 | QLHSDNHTCP_12 | Nhóm 2 — Thông tin tư vấn (chỉ đọc, lấy từ Cổng Dịch vụ công) | `dev done` / `Pass` | 626 | QLHSDNHTCP_12 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 22 | QLHSDNHTCP_13 | Nhóm 8 — Thông tin phê duyệt và Lịch sử xử lý | `dev done` / `Pass` | 627 | QLHSDNHTCP_13 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 24 | QLDNDHTPL_02 | Cột dữ liệu trong bảng kết quả | `dev done` / `Pass` | 686 | QLDNDHTPL_02 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 25 | QLDNDHTPL_04 | Kiểm tra Cấu trúc màn hình | `dev done` / `Pass` | 688 | QLDNDHTPL_04 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map · ❔map cần soi<br>sim nội dung 0.86<br><sub>sim 0.86 · khoá phụ (tên file ảnh) · tên file ảnh khớp mã</sub> |
| 26 | QLDNDHTPL_05 | Kiểm tra hiển thị Nhóm A — Định danh cơ bản (bắt buộc) | `dev done` / `Pass` | 689 | QLDNDHTPL_05 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 27 | QLDNDHTPL_06 | Kiểm tra hiển thị Nhóm B — Địa lý và phân loại (tùy chọn, có gợi ý mặc định) | `dev done` / `Pass` | 690 | QLDNDHTPL_06 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 28 | QLDNDHTPL_07 | Kiểm tra hiển thị Nhóm C — Thông tin bổ sung (tùy chọn) | `dev done` / `Pass` | 691 | QLDNDHTPL_07 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 29 | QLDNDHTPL_10 | Kiểm tra trùng mã số thuế | `dev done` / `Pass` | 694 | QLDNDHTPL_10 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 31 | QLDNDHTPL_14 | "Hủy" khi có thay đổi chưa lưu | `dev done` / `Pass` | 698 | QLDNDHTPL_14 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 33 | QLDNDHTPL_21 | Xem | `dev done` / `Pass` | 705 | QLDNDHTPL_21 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 37 | QLDNDHTPL_26 | Kiểm tra hiển thị Nhóm 4 — Thông tin khác | `dev done` / `Pass` | 710 | QLDNDHTPL_26 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 40 | QLDNDHTPL_31 | Kiểm tra nút chức năng Sửa tại màn hình xem chi tiết | `dev done` / `Pass` | 715 | QLDNDHTPL_31 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 41 | TKDNHTPL_02 | Kiểm tra Điều kiện tìm kiếm / bộ lọc | `dev done` / `Pass` | 717 | TKDNHTPL_02 | `dev done` | `(trống)` / `(trống)` | Cần chị anhduong16.work@gmail.com xác nhận có cần ô tìm kiếm theo Đơn vị hay không vì tài liệu có trường tìm kiếm này | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 42 | TKDNHTPL_03 | Tìm kiếm không có kết quả | `dev done` / `Pass` | 718 | TKDNHTPL_03 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 43 | LKHDG_02 | Kiểm tra hiển thị các trường thông tin trong danh sách | `dev done` / `Pass` | 722 | LKHDG_02 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 44 | LKHDG_03 | Kiểm tra Điều kiện tìm kiếm / bộ lọc | `dev done` / `Pass` | 723 | LKHDG_03 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 45 | LKHDG_04 | Tìm kiếm có kết quả | `dev done` / `Pass` | 724 | LKHDG_04 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 46 | LKHDG_07 | Kiểm tra nút chức năng Thêm mới | `dev done` / `Pass` | 727 | LKHDG_07 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 47 | LKHDG_08 | Thiếu trường bắt buộc | `dev done` / `Pass` | 728 | LKHDG_08 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 50 | LKHDG_16 | "Sửa" | `dev done` / `Pass` | 736 | LKHDG_16 | `dev done` | `Fail` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 51 | LKHDG_19 | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Kế hoạc… | `dev done` / `Pass` | 739 | LKHDG_19 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 52 | LKHDG_20 | Kiểm tra nút chức năng "Hủy" | `dev done` / `Pass` | 740 | LKHDG_20 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 53 | LKHDG_21 | Kiểm tra chức năng "Lưu nháp" | `dev done` / `Pass` | 741 | LKHDG_21 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 54 | LKHDG_22 | Kiểm tra chức năng "Lưu & Chuyển tiêu chí" | `dev done` / `Pass` | 742 | LKHDG_22 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 55 | TLCTCDG_07 | Kiểm tra nút chức năng "Sửa tiêu chí" | `dev done` / `Pass` | 749 | TLCTCDG_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 56 | TLCTCDG_08 | Kiểm tra nút chức năng "Xóa tiêu chí" | `dev done` / `Pass` | 750 | TLCTCDG_08 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 59 | TLCTCDG_12 | "Lưu & Quay lại Kế hoạch" | `dev done` / `Pass` | 754 | TLCTCDG_12 | `dev done` | `Pass` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 60 | PCNTHDG_06 | Kiểm tra nút chức năng "Hủy" | `dev done` / `Pass` | 761 | PCNTHDG_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 67 | CVVDG_03 | Tích chọn vụ việc đã thuộc đợt đánh giá khác | `dev done` / `Pass` | 774 | CVVDG_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 68 | CVVDG_04 | Không có vụ việc trong kỳ | `dev done` / `Pass` | 775 | CVVDG_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 69 | THDG_02 | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Thực hi… | `dev done` / `Pass` | 777 | THDG_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 70 | THDG_03 | Lưu kết quả khi điểm vượt | `dev done` / `Pass` | 778 | THDG_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 71 | THDG_04 | Tự động tính lại điểm tổng hợp và xếp loại | `dev done` / `Pass` | 779 | THDG_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 72 | THDG_05 | Lưu kết quả thành công | `dev done` / `Pass` | 780 | THDG_05 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 73 | LBCDG_02 | Kiểm tra hiển thị các trường thông tin trong Chi tiết đợt đánh giá (tab Báo cáo) | `dev done` / `Pass` | 785 | LBCDG_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 74 | LBCDG_04 | Kiểm tra nút chức năng "Xuất Excel" | `dev done` / `Pass` | 787 | LBCDG_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 75 | LBCDG_05 | "Xuất Word" thành công | `dev done` / `Pass` | 788 | LBCDG_05 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 77 | TPDBC_03 | Đợt không ở trạng thái "Báo cáo" | `dev done` / `Pass` | 791 | TPDBC_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 81 | QLTMBMHD_08 | Thêm mới tên quá dài | `dev done` / `Pass` | 805 | QLTMBMHD_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 83 | QLTMBMHD_13 | Kiểm tra hiển thị nút chức năng Xóa thư mục | `dev done` / `Pass` | 810 | QLTMBMHD_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 85 | QLTMBMHD_19 | Xóa hàng loạt thành công | `dev done` / `Pass` | 816 | QLTMBMHD_19 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 86 | QLTMBMHD_20 | Xóa hàng loạt một phần thành công | `dev done` / `Pass` | 817 | QLTMBMHD_20 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 87 | QLTMBMHD_23 | Xuất Excel | `dev done` / `Pass` | 820 | QLTMBMHD_23 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 88 | TKTMBMHD_02 | Kiểm tra hiển thị danh sách kết quả | `dev done` / `Pass` | 822 | TKTMBMHD_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 89 | TKTMBMHD_04 | Kiểm tra Điều kiện tìm kiếm / bộ lọc | `dev done` / `Pass` | 824 | TKTMBMHD_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 90 | TKTMBMHD_06 | Tìm kiếm không có kết quả | `dev done` / `Pass` | 826 | TKTMBMHD_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 91 | TKTMBMHD_07 | Xóa bộ lọc | `dev done` / `Pass` | 827 | TKTMBMHD_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 92 | CKTMBMHDLCTT_02 | Kiểm tra hiển thị nút chức năng công khai | `dev done` / `Pass` | 829 | CKTMBMHDLCTT_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 93 | CKTMBMHDLCTT_07 | Công khai hàng loạt thành công | `dev done` / `Pass` | 834 | CKTMBMHDLCTT_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 94 | CKTMBMHDLCTT_08 | Công khai hàng loạt một phần thành công | `dev done` / `Pass` | 835 | CKTMBMHDLCTT_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 95 | CKTMBMHDLCTT_10 | Ẩn hàng loạt thành công | `dev done` / `Pass` | 837 | CKTMBMHDLCTT_10 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 96 | CKTMBMHDLCTT_11 | Ẩn hàng loạt một phần thành công | `dev done` / `Pass` | 838 | CKTMBMHDLCTT_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 99 | QLBMHD_06 | Kiểm tra kích thước tệp không vượt 20 MB. | `dev done` / `Pass` | 845 | QLBMHD_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 100 | QLBMHD_07 | Tệp hỏng | `dev done` / `Pass` | 846 | QLBMHD_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 101 | QLBMHD_08 | Có mã độc | `dev done` / `Pass` | 847 | QLBMHD_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 102 | QLBMHD_09 | Tải tệp bị gián đoạn | `dev done` / `Pass` | 848 | QLBMHD_09 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 106 | QLBMHD_13 | Kiểm tra nút chức năng "Sửa | `dev done` / `Pass` | 852 | QLBMHD_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 109 | QLBMHD_16 | Kiểm tra nút chức năng Tải về trong màn hình chi tiết biểu mẫu | `dev done` / `Pass` | 855 | QLBMHD_16 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 110 | QLBMHD_17 | Kiểm tra nút chức năng "Xem trước" | `dev done` / `Pass` | 856 | QLBMHD_17 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 111 | QLBMHD_18 | Xem trước tệp DOC hoặc DOCX | `dev done` / `Pass` | 857 | QLBMHD_18 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 112 | QLBMHD_19 | Xem trước tệp XLS hoặc XLSX | `dev done` / `Pass` | 858 | QLBMHD_19 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 113 | TKBMHD_03 | Kiểm tra Điều kiện tìm kiếm / bộ lọc | `dev done` / `Pass` | 863 | TKBMHD_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 114 | TKBMHD_04 | Tìm kiếm không có kết quả | `dev done` / `Pass` | 864 | TKBMHD_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 118 | IBMHD_04 | Kiểm tra chức năng "Chọn tệp" | `dev done` / `Pass` | 870 | IBMHD_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 119 | IBMHD_07 | Một số lỗi | `dev done` / `Pass` | 873 | IBMHD_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 121 | IBMHD_11 | "Hủy" | `dev done` / `Pass` | 877 | IBMHD_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 122 | QLDMLVPL_02 | Kiểm tra hiển thị Danh sách loại danh mục (cột tab bên trái) | `dev done` / `Pass` | 880 | QLDMLVPL_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 123 | QLDMLVPL_09 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 887 | QLDMLVPL_09 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 124 | QLDMLVPL_14 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 892 | QLDMLVPL_14 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 125 | QLDMLVPL_16 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 894 | QLDMLVPL_16 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 128 | QLDMLHHT_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 906 | QLDMLHHT_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 129 | QLDMLHHT_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 911 | QLDMLHHT_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 130 | QLDMLHHT_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 913 | QLDMLHHT_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 133 | QLDMCTHT_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 924 | QLDMCTHT_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 134 | QLDMCTHT_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 929 | QLDMCTHT_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 135 | QLDMCTHT_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 931 | QLDMCTHT_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 136 | QLDMTTVV_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 941 | QLDMTTVV_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 137 | QLDMTTVV_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 946 | QLDMTTVV_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 138 | QLDMTTVV_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 948 | QLDMTTVV_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 140 | QLDMCQDVQL_12 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 965 | QLDMCQDVQL_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 142 | QLDMLDN_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 989 | QLDMLDN_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 143 | QLDMLDN_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 994 | QLDMLDN_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 144 | QLDMLDN_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 996 | QLDMLDN_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 146 | QLDMHSDNHT_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1007 | QLDMHSDNHT_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 147 | QLDMHSDNHT_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 1012 | QLDMHSDNHT_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 148 | QLDMHSDNHT_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1014 | QLDMHSDNHT_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 149 | QLDMHSDNTT_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1024 | QLDMHSDNTT_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 150 | QLDMHSDNTT_11 | Hủy thêm mới khi đang nhập | `dev done` / `Pass` | 1029 | QLDMHSDNTT_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 151 | QLDMHSDNTT_13 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1031 | QLDMHSDNTT_13 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 152 | QLCHTHXLHS_02 | Kiểm tra hiển thị Thanh thẻ (tab) ở đầu trang | `dev done` / `Pass` | 1037 | QLCHTHXLHS_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 153 | QLCHTHXLHS_03 | Kiểm tra hiển thị Bảng cấu hình SLA (thẻ "Thời hạn xử lý / SLA") | `dev done` / `Pass` | 1038 | QLCHTHXLHS_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 154 | QLCHTHXLHS_05 | Bật/tắt gửi thư điện tử | `dev done` / `Pass` | 1040 | QLCHTHXLHS_05 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 155 | QLCHTHXLHS_06 | Bật/tắt gửi thông báo trong hệ thống | `dev done` / `Pass` | 1041 | QLCHTHXLHS_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 156 | QLCHTHXLHS_07 | Kiểm tra màn hình/popup chỉnh sửa khi nhấn vàp biểu tượng chỉnh sửa tại dòng | `dev done` / `Pass` | 1042 | QLCHTHXLHS_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 157 | QLDMTCDGHQ_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1050 | QLDMTCDGHQ_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 158 | QLDMTCDGHQ_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1056 | QLDMTCDGHQ_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 162 | QLDMLTK_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1083 | QLDMLTK_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 163 | QLDMLTK_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1089 | QLDMLTK_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module)</sub> |
| 165 | QLTKND_02 | Kiểm tra Điều kiện tìm kiếm / bộ lọc | `dev done` / `Pass` | 1113 | QLTKND_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 166 | QLTKND_03 | Kiểm tra Thẻ trạng thái (tab nhanh) | `dev done` / `Pass` | 1114 | QLTKND_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 168 | QLTKND_15 | Kiểm tra trùng tên đăng nhập | `dev done` / `Pass` | 1126 | QLTKND_15 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 172 | QLPQTCDL_06 | Chọn/Bỏ chọn đơn vị | `dev done` / `Pass` | 1145 | QLPQTCDL_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 173 | QLPQCN_02 | Kiểm tra Bộ chọn vai trò | `dev done` / `Pass` | 1149 | QLPQCN_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 174 | QLPQCN_03 | Kiểm tra Ma trận Phân quyền | `dev done` / `Pass` | 1150 | QLPQCN_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 175 | QLLHTNHS_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1164 | QLLHTNHS_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 176 | QLLHTNHS_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1170 | QLLHTNHS_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 177 | QLDMKTNHS_06 | Kiểm tra các trường thông tin trên màn hình/popup thêm mới | `dev done` / `Pass` | 1180 | QLDMKTNHS_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 178 | QLDMKTNHS_12 | Kiểm tra các trường thông tin trên màn hình/popup sửa | `dev done` / `Pass` | 1186 | QLDMKTNHS_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 179 | QLDN_07 | Mã sai hoặc hết hiệu lực | `dev done` / `Pass` | 1197 | QLDN_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 180 | QLDN_10 | Tài khoản "Vô hiệu hóa" | `dev done` / `Pass` | 1200 | QLDN_10 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 181 | QLDN_12 | Tài khoản "Tạm khóa" do quản trị viên cật nhật trạng thái Tạm khóa | `dev done` / `Pass` | 1202 | QLDN_12 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 187 | QLDKTK_04 | Mã số thuế đã tồn tại trong hệ thống | `dev done` / `Pass` | 1214 | QLDKTK_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 188 | QLDKTK_08 | Kiểm tra các trường bắt buộc | `dev done` / `Pass` | 1218 | QLDKTK_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 192 | SLHDVM_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1236 | SLHDVM_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 195 | VVDTN_04 | Kiểm tra hiển thị Biểu đồ và bảng kết quả | `dev done` / `Pass` | 1242 | VVDTN_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 197 | VVDTN_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1245 | VVDTN_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 202 | VVDHT_04 | Kiểm tra hiển thị Biểu đồ và bảng kết quả | `dev done` / `Pass` | 1251 | VVDHT_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 204 | VVDHT_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1254 | VVDHT_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 207 | VVDHTHT_03 | Kiểm tra hiển thị Chỉ số tổng hợp nhanh | `dev done` / `Pass` | 1259 | VVDHTHT_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 208 | VVDHTHT_04 | Kiểm tra hiển thị Biểu đồ và bảng kết quả | `dev done` / `Pass` | 1260 | VVDHTHT_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 210 | VVDHTHT_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1263 | VVDHTHT_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 215 | VVTTG_03 | Kiểm tra hiển thị Biểu đồ và bảng kết quả | `dev done` / `Pass` | 1268 | VVTTG_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 217 | VVTTG_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1271 | VVTTG_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 220 | CLDTBDDDR_03 | Kiểm tra hiển thị Chỉ số tổng hợp | `dev done` / `Pass` | 1276 | CLDTBDDDR_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 223 | CLDTBDDDR_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1280 | CLDTBDDDR_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 228 | LDTBDDDR_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1289 | LDTBDDDR_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module)</sub> |
| 231 | CGTVPL_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1298 | CGTVPL_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 232 | DGHQHTPL_03 | Kiểm tra hiển thị Chỉ số tổng hợp | `dev done` / `Pass` | 1303 | DGHQHTPL_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 234 | DGHQHTPL_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1307 | DGHQHTPL_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 235 | CLDTBDPL_03 | Kiểm tra hiển thị Chỉ số tổng hợp | `dev done` / `Pass` | 1312 | CLDTBDPL_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 236 | CLDTBDPL_04 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1313 | CLDTBDPL_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 238 | CLDTBDPL_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1316 | CLDTBDPL_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 240 | VVTDVQL_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1325 | VVTDVQL_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 242 | VVTLV_03 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1330 | VVTLV_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 244 | VVTLV_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1333 | VVTLV_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 245 | VVTLHDN_03 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1338 | VVTLHDN_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 247 | VVTLHDN_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1341 | VVTLHDN_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 249 | VVTTGCT_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1349 | VVTTGCT_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 251 | CPHTCT_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1358 | CPHTCT_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 254 | CPCTHTTDVQL_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1367 | CPCTHTTDVQL_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 258 | CPCTHTTLHDN_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1385 | CPCTHTTLHDN_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 261 | CPCTHTTTG_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1393 | CPCTHTTTG_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 262 | SLCTHT_03 | Kiểm tra hiển thị Chỉ số tổng hợp | `dev done` / `Pass` | 1398 | SLCTHT_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 263 | SLCTHT_04 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1399 | SLCTHT_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 265 | SLCTHT_07 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1402 | SLCTHT_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 267 | CTTDVQL_03 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1407 | CTTDVQL_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 269 | CTTDVQL_05 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1409 | CTTDVQL_05 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 272 | CTTLV_04 | Kiểm tra hiển thị Biểu đồ và bảng tổng hợp | `dev done` / `Pass` | 1415 | CTTLV_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 274 | CTTLV_06 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1417 | CTTLV_06 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 276 | CTTTG_05 | Kiểm tra chức năng Xuất PDF | `dev done` / `Pass` | 1424 | CTTTG_05 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 278 | QLNDTVVCG_04 | Chọn thẻ phân loại trạng thái | `dev done` / `Pass` | 1432 | QLNDTVVCG_04 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 280 | QLNDTVVCG_07 | Kiểm tra thông tin hiển thị sau khi chọn Doanh nghiệp, Chuyên gia / Tư vấn viên | `dev done` / `Pass` | 1435 | QLNDTVVCG_07 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 281 | QLNDTVVCG_08 | Nhóm 2 — Nội dung tư vấn | `dev done` / `Pass` | 1436 | QLNDTVVCG_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 283 | QLNDTVVCG_15 | Cấu trúc màn hình | `dev done` / `Pass` | 1443 | QLNDTVVCG_15 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 284 | QLNDTVVCG_17 | Nhóm 1 — Thông tin cơ bản Nhóm 2 — Nội dung tư vấn | `dev done` / `Pass` | 1445 | QLNDTVVCG_17 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 286 | QLNDTVVCG_22 | Kiểm tra màn hình chức năng Phân công chuyên gia | `dev done` / `Pass` | 1450 | QLNDTVVCG_22 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 288 | QLNDTVVCG_27 | Kiểm tra nút chức năng Hoàn thành tư vấn | `dev done` / `Pass` | 1455 | QLNDTVVCG_27 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 289 | QLNDTVVCG_36 | Xác nhận hủy Với trạng thái "Đang tư vấn" | `dev done` / `Pass` | 1464 | QLNDTVVCG_36 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 290 | QLNDTVVCG_40 | Xuất Excel | `dev done` / `Pass` | 1468 | QLNDTVVCG_40 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module)</sub> |
| 291 | TKNDTVVCG_03 | Tìm kiếm theo tên DN | `dev done` / `Pass` | 1472 | TKNDTVVCG_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 292 | QLHSPLDN_02 | Bảng danh sách hồ sơ pháp lý | `dev done` / `Pass` | 1482 | QLHSPLDN_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 293 | QLHSPLDN_03 | Biểu mẫu thêm mới / chỉnh sửa hồ sơ pháp lý | `dev done` / `Pass` | 1483 | QLHSPLDN_03 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 294 | QLTLPLCVV_02 | Bảng danh sách tư liệu pháp lý | `dev done` / `Pass` | 1500 | QLTLPLCVV_02 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 296 | QLTLPLCVV_07 | Kiểm tra điều kiện hiển thị nút chức năng Sửa | `dev done` / `Pass` | 1505 | QLTLPLCVV_07 | `dev done` | `(trống)` / `(trống)` | uc này và uc QLTLPLCVV_09 về mặt ý nghĩa giống nhau, chỉ cần fix 1 tr 2 | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 297 | QLTLPLCVV_08 | Sửa thành công | `dev done` / `Pass` | 1506 | QLTLPLCVV_08 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 298 | QLTLPLCVV_09 | Sửa tư liệu đã chuyển sang "Công khai" | `dev done` / `Pass` | 1507 | QLTLPLCVV_09 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 299 | QLTLPLCVV_11 | Xóa tư liệu đang ở trạng thái "Công khai" | `dev done` / `Pass` | 1509 | QLTLPLCVV_11 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |
| 300 | QLTLPLCVV_15 | Tải lên tệp đính kèm chứa mã độc | `dev done` / `Pass` | 1513 | QLTLPLCVV_15 | `dev done` | `(trống)` / `(trống)` | (trống) | ✅ Đã map<br><sub>sim 1.00 · A(tuần+module) · tên file ảnh khớp mã</sub> |

