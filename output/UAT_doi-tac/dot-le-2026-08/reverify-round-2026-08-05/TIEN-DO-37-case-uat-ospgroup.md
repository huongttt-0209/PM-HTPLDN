# Tiến độ đo lại 37 phiếu trên môi trường nghiệm thu đối tác

- Môi trường: `https://htpldn-uat.ospgroup.vn` · bundle `assets/index-Dn5IWt_M.js` · nhãn `HTPLDN · V1.0.7`
- Hộp thư lấy mã xác thực: `https://htpldn-uat.ospgroup.vn/mailhog/`
- Bắt đầu: 05/08/2026 14:31
- Ghi kết quả: tab tuần cột `Verify 2` = `Pass` · tab `bug` cột `Trạng thái dev fix` = `UAT done`
- Case Reopen ghi 3 ô cùng giá trị `Reopen`: tab tuần cột `Trạng thái dev fix 2` + `Verify 2`, tab `bug`
  cột `Trạng thái dev fix` (chốt 05/08/2026). Riêng `QLDXDTTH_10` giữ nguyên theo yêu cầu — phiếu này chờ
  BA chốt đặc tả chứ không phải dev fix, và cũng không có dòng trong tab `bug`.
- Công cụ ghi: `tools/dong_bo_uat_ospgroup.py --only <Mã TC> --evidence <ảnh> --write`

## Lưu ý phạm vi

- 4 mã **không có dòng trong tab `bug`** → chỉ ghi được tab tuần: `QLDXDTTH_10` · `QLDXDTTH_11` ·
  `QLLKHDTBD_50` · `TKHSYCHTPL_OOS_01`.
- 27/37 dòng đã sẵn `Verify 2 = Pass` từ vòng đo trên môi trường nội bộ trước đó; đợt này đo lại thật
  trên môi trường đối tác rồi mới xác nhận.

## Bảng theo dõi

| # | Mã TC | Tuần · dòng | Kết quả | Ghi sheet | Bảng đối chiếu |
|---:|---|---|---|---|---|
| 1 | CBKQDTBD_01 | 2 · 121 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CBKQDTBD_01-uat.md` |
| 2 | DKTGMLTVV_05 | 2 · 123 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/DKTGMLTVV_05-uat.md` |
| 3 | NHSYC_01 | 2 · 127 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/NHSYC_01-uat.md` |
| 4 | QLHSVV_07 | 2 · 128 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/QLHSVV_07-uat.md` |
| 5 | QLDXDTTH_10 | 2 · 134 | ❌ Reopen | ✅ Verify 2 = Reopen (bug: giữ nguyên) | `cond/QLDXDTTH_10-uat.md` |
| 6 | QLDXDTTH_11 | 2 · 135 | ✅ Pass | ✅ Verify 2 (không có dòng bug) | `cond/QLDXDTTH_11-uat.md` |
| 7 | QLLKHDTBD_50 | 2 · 144 | ✅ Pass | ✅ Verify 2 (không có dòng bug) | `cond/QLLKHDTBD_50-uat.md` |
| 8 | TKHSYCHTPL_OOS_01 | 2 · 145 | ✅ Pass | ✅ Verify 2 (không có dòng bug) | `cond/TKHSYCHTPL_OOS_01-uat.md` |
| 9 | KTDGKQHT_23 | 2 · 149 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/KTDGKQHT_23-uat.md` |
| 10 | NHSYC_OOS_02 | 2 · 154 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/NHSYC_OOS_02-uat.md` |
| 11 | TKHSYCHTPL_OOS_02 | 2 · 155 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/TKHSYCHTPL_OOS_02-uat.md` |
| 12 | NHSYC_OOS_03 | 2 · 156 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/NHSYC_OOS_03-uat.md` |
| 13 | QLLSHTCTVV_03 | 2 · 125 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/QLLSHTCTVV_03-uat.md` |
| 14 | TKTMBMHD_07 | 3 · 91 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/TKTMBMHD_07-uat.md` |
| 15 | SLHDVM_07 | 3 · 192 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/SLHDVM_07-uat.md` |
| 16 | VVDTN_07 | 3 · 197 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVDTN_07-uat.md` |
| 17 | VVDHT_07 | 3 · 204 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVDHT_07-uat.md` |
| 18 | VVDHTHT_07 | 3 · 210 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVDHTHT_07-uat.md` |
| 19 | VVTTG_06 | 3 · 217 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVTTG_06-uat.md` |
| 20 | CLDTBDDDR_07 | 3 · 223 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CLDTBDDDR_07-uat.md` |
| 21 | LDTBDDDR_07 | 3 · 228 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/LDTBDDDR_07-uat.md` |
| 22 | CGTVPL_07 | 3 · 231 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CGTVPL_07-uat.md` |
| 23 | DGHQHTPL_07 | 3 · 234 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/DGHQHTPL_07-uat.md` |
| 24 | CLDTBDPL_07 | 3 · 238 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CLDTBDPL_07-uat.md` |
| 25 | VVTDVQL_07 | 3 · 240 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVTDVQL_07-uat.md` |
| 26 | VVTLHDN_06 | 3 · 247 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVTLHDN_06-uat.md` |
| 27 | VVTTGCT_06 | 3 · 249 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/VVTTGCT_06-uat.md` |
| 28 | CPHTCT_07 | 3 · 251 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CPHTCT_07-uat.md` |
| 29 | CPCTHTTDVQL_07 | 3 · 254 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CPCTHTTDVQL_07-uat.md` |
| 30 | CPCTHTTLHDN_07 | 3 · 258 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CPCTHTTLHDN_07-uat.md` |
| 31 | CPCTHTTTG_03 | 3 · 259 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CPCTHTTTG_03-uat.md` |
| 32 | CPCTHTTTG_06 | 3 · 261 | ❌ Reopen | ✅ dev fix 2 + Verify 2 + bug đều `Reopen` | `cond/CPCTHTTTG_06-uat.md` |
| 33 | SLCTHT_07 | 3 · 265 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/SLCTHT_07-uat.md` |
| 34 | CTTDVQL_05 | 3 · 269 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CTTDVQL_05-uat.md` |
| 35 | CTTLV_06 | 3 · 274 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CTTLV_06-uat.md` |
| 36 | CTTTG_05 | 3 · 276 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/CTTTG_05-uat.md` |
| 37 | QLDMTCTV_OOS_13 | 3 · 339 | ✅ Pass | ✅ Verify 2 + UAT done | `cond/QLDMTCTV_OOS_13-uat.md` |

**Xong 37/37 lúc 17:34 ngày 05/08/2026 — 36 Pass · 1 Reopen (`CPCTHTTTG_06`).**

## Ghi nhận ngoài phạm vi phiếu (chờ báo lại, KHÔNG tự log dòng mới)

- **KTDGKQHT_23** — bản vá đúng, nhưng bản ghi kết quả tạo TRƯỚC bản vá vẫn giữ mẫu số cũ cho tới lần đổi
  lịch học kế tiếp. Đề nghị dev chạy một lượt tính lại cho các khóa đã điểm danh trước bản vá.
- **Sheet `bug` dịch dòng** (05/08 lúc ~16:00): 1 dòng bị xóa phía trên dòng 346 → đuôi bảng dịch lên 1
  (`KTDGKQHT_23` 347→346, `NHSYC_OOS_02` 352→351, `TKHSYCHTPL_OOS_02` 353→352, `NHSYC_OOS_03` 354→353,
  `QLDMTCTV_OOS_13` 355→354). Chốt chặn của công cụ ghi đã bắt được, đã cập nhật bảng dòng.
- **QLDXDTTH_10** — cần BA chốt: nhóm đề xuất gửi từ chuyên trang chỉ lưu mã định danh người gửi, không lưu
  họ tên → cột "Người đề xuất" hiện dấu gạch ngang. Chốt là chuyên trang phải gửi kèm họ tên, hay đặc tả
  chấp nhận nhãn thay thế. Chi tiết ở `cond/QLDXDTTH_10-uat.md`.
- **NHSYC_OOS_02** — bản vá đúng, nhưng đo được một điểm khác nằm ngoài phiếu: mốc hạn xử lý đang cộng
  **+15 ngày lịch** thay vì **+15 ngày làm việc** như đặc tả (`srs-fr-05-vu-viec.md:343`, `BR-SLA-01`).
  Hồ sơ tiếp nhận 05/08/2026 (thứ Tư) ra hạn 20/08/2026, đúng ra phải 26/08/2026 — chênh 6 ngày. Cần BA xác
  nhận môi trường có đặt cấu hình SLA khác (UC108) không, rồi mới quyết có mở phiếu riêng. Chi tiết ở
  `cond/NHSYC_OOS_02-uat.md`.
- **QLLSHTCTVV_03** — hai điểm ngoài phạm vi phiếu, cần BA/dev xem: (a) bảng "Lịch sử hỗ trợ" nay có **14
  cột** thay vì 9 cột BA chốt (thêm Mã HĐ · Tên hợp đồng · Trạng thái · Ngày bắt đầu · Ngày kết thúc);
  (b) điểm đánh giá vụ việc vẫn **nhập và lưu ở thang 0–10**, chỉ quy đổi khi hiển thị, trong khi
  `srs-fr-04-chuyen-gia-tvv.md:795` mô tả trường ở thang 1.0–5.0. Chi tiết ở `cond/QLLSHTCTVV_03-uat.md`.
- **Ô `CBKQDTBD_01` ở tab `bug` bị ai đó xóa trắng sau khi mình ghi.** Ghi lúc 14:42 và đọc lại đúng
  `UAT done`; đến 17:36 rà lại thì ô trống (dòng 28 `CBKQDTBD_02` cũng trống). Đã ghi lại lúc 17:37. Sheet
  đang có người khác sửa song song — nên rà lại toàn bộ 37 ô trước khi chốt bàn giao.
- **CPCTHTTTG_06 — đã ghi nhầm Pass lúc 16:59, đã sửa lại Reopen lúc 17:12.** Nguyên nhân phát hiện: tên tệp
  trả về mang tên báo cáo khác. Đã rà chéo tiêu đề bên trong **toàn bộ tệp PDF** của đợt đo (23 bản bắt) —
  chỉ đúng phiếu này lệch, 19 phiếu báo cáo còn lại tệp khớp đúng loại. Bổ sung `--tra-lai-bug` cho
  `tools/dong_bo_uat_ospgroup.py` để trả ô tab `bug` về giá trị cũ khi phải đảo verdict.
- **CBKQDTBD_01** — khóa `KH-HDSD-AG-003` của đơn vị An Giang: tài khoản cấp Trung ương xem được đầy đủ
  nhưng thao tác hủy công bố bị máy chủ trả "Khóa học không tồn tại" (`ERR-VAL-III-04-01`, 404) dù bản ghi
  vẫn tồn tại. Cùng thao tác trên khóa thuộc đơn vị của tài khoản thì chạy bình thường.
