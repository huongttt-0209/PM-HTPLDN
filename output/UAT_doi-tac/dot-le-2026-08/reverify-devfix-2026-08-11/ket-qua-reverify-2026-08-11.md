# Re-verify bug Dev đã fix — 11/08/2026

**Môi trường:** https://18.143.165.120.nip.io (nội bộ) · bó mã đang chạy `assets/index-x06iyQ52.js` · nhãn chân sidebar `V1.0.12`
**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`, tab `bug` (gid 1714340219)
**Phạm vi:** dòng có `Trạng thái dev fix` = *Fixed* **và** cột `Kết quả verify` đã có sẵn tiêu chí → **5 dòng**
(17 dòng *Fixed*, 12 dòng còn lại chưa có tiêu chí nên ngoài phạm vi).

| Dòng | Mã TC | Kết quả | Đã ghi vào sheet |
|---|---|---|---|
| 20 | QLLKHDTBD_09 | ✅ Hết lỗi | `Trạng thái dev fix` = **Test done** |
| 64 | DGKQHTVV_01 | ✅ Hết lỗi *(lượt 3 — dev fix xong)* | `Trạng thái dev fix` = **Test done** |
| 65 | DGKQHTVV_02 | ✅ Hết lỗi | `Trạng thái dev fix` = **Test done** |
| 338 | LBCKQTHCT_05 | ✅ Hết lỗi | `Trạng thái dev fix` = **Test done** |
| 339 | LBCKQTHCT_06 | ✅ Hết lỗi | `Trạng thái dev fix` = **Test done** |
| 342 | GKQTHCTHTPL_01 | ✅ Hết lỗi *(lượt 4 — 12/08, dev fix nốt vế (b))* | `Trạng thái dev fix` = **Test done** |

> **Bổ sung lượt 2 (11/08 chiều).** Dòng 338/339 ban đầu để trống vì tiêu chí ghi "đừng đo khi đặc tả chưa sửa". User quyết định đo tiếp, BA cập nhật SRS sau — đã đo trọn 6 bước, kết quả PASS. Xem mục riêng phía dưới.
>
> **Bổ sung lượt 3 (11/08 tối, bó mã mới `assets/index-BTT8H1bn.js`).** Dev báo đã fix `DGKQHTVV_01` + `GKQTHCTHTPL_01` → đo lại cả hai. Dòng 64 nay PASS trọn 3 điều kiện. Dòng 342 phần A hết lỗi, phần B sửa được phần cốt lõi (đơn vị nộp sau không còn bị chặn) nhưng màn Chi tiết đợt của tài khoản Trung ương vẫn còn ô trạng thái vòng đời của đợt → Reopen. Xem 2 mục riêng cuối file.

---

## Dòng 20 — QLLKHDTBD_09 (Xuất Excel theo bộ lọc) → PASS

Đo trên màn *Đào tạo, tập huấn → Kế hoạch đào tạo → Danh sách*, tài khoản `cbnv_tw`.

| Điều kiện PASS của tiêu chí | Kết quả đo |
|---|---|
| (a) Hàng tiêu đề tệp phủ đủ danh mục cột trên màn | ✅ 10/10 cột dữ liệu: Mã KH · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Số chương trình · Trạng thái · Người tạo · Ngày tạo |
| (b) Có 1 cột họ tên cán bộ lập + 1 cột ngày lập | ✅ **Người tạo** + **Ngày tạo** (trước đây tệp chỉ 7 cột, thiếu đúng 2 cột này) |
| (c) Tệp lọc có đúng N dòng | ✅ lọc "Đã duyệt" → N = 4, tệp có đúng 4 dòng (danh sách chưa lọc T = 14, tệp không lọc có 14 dòng) |
| (d) Mẫu A/B trùng khít giá trị trên màn | ✅ `KH-20260803-0003` → *CB Nghiệp vụ - Trung ương* / **03/08/2026**; `KHDT-QAW7-01` → *Quản trị hệ thống* / **25/07/2026** |

Bẫy đã tránh: `KH-20260803-0003` có Từ ngày 05/07, Đến ngày 25/07, Ngày tạo 03/08 — tệp lấy **đúng ngày lập**, không nhầm sang 2 cột hiệu lực.
Tệp đã đọc bằng openpyxl (không chấm bằng việc "tải được tệp").
Ảnh: `image/QLLKHDTBD_09-danhsach-14ban-ghi-2026-08-11.png`

---

## Dòng 64 — DGKQHTVV_01 (DN đánh giá vụ việc) → REOPEN

Tài khoản DN `0109998887`; đối chứng `cbnv_tw`, `cbpd_tw_01`.

| Điều kiện PASS | Kết quả |
|---|---|
| (a) DN thấy đủ tập chuẩn S, có cả vụ việc do TW thụ lý | ✅ **18/18** (13 do TW thụ lý + 5 do Sở Tư pháp HN thụ lý) |
| (b) Mở được từ danh sách **và** khi dán thẳng địa chỉ | ✅ cả hai đường |
| (c) Tải được tài liệu, đọc được kết quả hỗ trợ | ✅ tệp đính kèm tải về HTTP 200; khối *Kết quả hỗ trợ* đọc được |
| (d) **Gửi được đánh giá, tải lại trang đọc đúng nội dung** | ❌ **HỎNG** |
| (e) Chặn vụ việc của DN khác | ✅ "Không tìm thấy vụ việc" |

**Chi tiết lỗi (d):** trên `VV-BTP-TW-20260804-001` (Hoàn thành, **chưa ai đánh giá**), DN nhập 9 · 8 · 10 + nhận xét `QA-DGKQ-20260811-1826` → bấm Xác nhận → toast *"Lỗi hệ thống, vui lòng thử lại sau"*, `POST …/danh-gia` trả **500 `ERR-SYS-00-00-01`**. Tải lại trang: khối Đánh giá vẫn "Chưa có thông tin".
Bộ bắt thông báo: `soObserverDangSong=1`, `SO_REQUEST=1`, `SO_KHUNG_THONG_BAO=1` (không phải lỗi bộ đo).

**Phép thử phân biệt (đã loại trừ 2 cách hiểu sai):**
1. *Không phải do bản ghi đã có đánh giá:* lần đầu đo trên `VV-BTP-TW-20260806-004` (đã có đánh giá của CB) — DN nhận 500, còn cán bộ nhận **409 "Vụ việc đã được đánh giá"**. Vì vậy đã dựng bản ghi sạch rồi đo lại.
2. *Không phải endpoint hỏng chung:* trên **chính** `VV-BTP-TW-20260804-001` sạch đó, tài khoản `cbnv_tw` gửi đánh giá → **201 thành công**.
⇒ Hỏng nằm ở đường đi của vai trò doanh nghiệp.

Ảnh: `image/DGKQHTVV_01-dn-danh-gia-500-2026-08-11.png`

> **Ghi chú ô `Kết quả verify` (T64).** Bản ghi lần đầu chỉ mô tả lỗi, **thiếu mục "Cách verify sau khi fix"** — trong khi CLAUDE.md bắt buộc mục này với mọi bug Reopen, và dòng 338/339 trên cùng sheet cũng đang dùng khuôn đó. Đã viết lại theo khuôn: LỖI Ở ĐÂU / LỖI THẾ NÀO / CHỈ HỎNG VỚI VAI TRÒ DOANH NGHIỆP / PHẦN ĐÃ ĐẠT / CẦN ĐẠT / ── VERIFY LẠI SAU KHI FIX ── (tiền đề · 5 bước · ✅ PASS · ❌ FAIL · 3 bẫy).
> Đường đi trong mục "LỖI Ở ĐÂU" đã **xác minh trực tiếp** ngày 11/08 chứ không viết theo trí nhớ: trang chi tiết vụ việc có nút `[Đánh giá]` và thẻ "Đánh giá" trong bộ thẻ *Thông tin Doanh nghiệp / Nội dung Yêu cầu / Tài liệu đính kèm / Kết quả hỗ trợ / **Đánh giá** / HĐ tư vấn liên kết*.
> Cùng lúc phát hiện: **cả 4 vụ việc Hoàn thành của DN `0109998887` nay đều ở "Đã đánh giá"** (`VV-BTP-TW-20260803-001`, `-20260804-001`, `-20260806-003`, `-20260806-004`) ⇒ lượt verify sau **bắt buộc dựng vụ việc mới**, đo lại trên 4 vụ này sẽ ra thông báo nghiệp vụ khác và không kết luận được. Đã ghi cảnh báo này vào tiền đề trong ô.
> Nội dung nguyên văn đã ghi: [`noi-dung-da-ghi-T64-ketquaverify.txt`](noi-dung-da-ghi-T64-ketquaverify.txt) · bản cũ: [`backup-o-sheet-truoc-khi-ghi/row64-T-truoc-khi-doi-format-2026-08-11.txt`](backup-o-sheet-truoc-khi-ghi/row64-T-truoc-khi-doi-format-2026-08-11.txt)

---

## Dòng 65 — DGKQHTVV_02 (hiển thị Nhóm 8 – Đánh giá) → PASS

Tài khoản `cbnv_tw`. Đo ở 3 bề rộng cửa sổ × 3 vụ việc; số dòng hình học đọc bằng `Range.getClientRects()`.

| Vụ việc | 1440 | 1280 | 1024 | Chuỗi hiển thị |
|---|---|---|---|---|
| `VV-BTP-TW-20260806-003` (9·8·10) | 1 dòng | 1 dòng | 1 dòng | 9.0 · 8.0 · 10.0 · tổng **9.0**/10 |
| `VV-QAW7-DG01` (ca từng vỡ) | 1 dòng | 1 dòng | 1 dòng | 4.0 · 8.0 · 9.0 · tổng **7.0**/10 |
| `VV-BTP-TW-20260803-001` (9·8·8, dựng mới) | 1 dòng | 1 dòng | 1 dòng | 9.0 · 8.0 · 8.0 · tổng **8.3**/10 |

- (a) Không ô điểm nào bị tách giá trị làm hai dòng (chiều cao 17.5px, line-height 22px → đúng 1 dòng) ✅
- (b) Mọi ô hiện 1 chữ số thập phân, kể cả điểm nguyên (9 → 9.0) ✅
- (c) Tổng của 9 · 8 · 8 hiện đúng **8.3** (không phải 8,33 / 8,4 / 8 / 8,0) ✅

Đã tránh 2 bẫy FAIL oan mà tiêu chí nêu: không chấm theo bộ nhãn 5 ô, không chấm theo việc nhóm hiện 7 ô. Dấu phân cách là dấu chấm — tiêu chí ghi rõ không quyết định PASS/FAIL.
Ảnh: `image/DGKQHTVV_02-diem-tong-8.3-tong-le-2026-08-11.png`, `image/DGKQHTVV_02-VVQAW7DG01-1024px-2026-08-11.png`

---

## Dòng 338 + 339 — LBCKQTHCT_05 / _06 → PASS (đo trọn 6 bước, lượt 2 ngày 11/08)

**Trạng thái đặc tả khi đo — ghi rõ để khỏi hiểu nhầm:** SRS **chưa** được sửa. `Docs-PM-HTPLDN/…/srs-v3.5/srs-fr-15-ct-htpldn.md` không đổi từ 06/08 12:46; dòng 1169 vẫn nguyên văn `| 39 | form | Nhan xet kien nghi | textarea | Max 5000 ky tu | input | khi dot o DANG_LAP_BC |`, bảng thành phần :1163–1175 vẫn thiếu dòng "Chương trình liên quan". Tiêu chí trong ô `Kết quả verify` khuyên đừng đo lúc này; user quyết định đo tiếp vì BA sẽ cập nhật SRS sau. Do đó **căn cứ chấm là quyết định BA ghi trong chính ô `Kết quả verify`**, không phải câu chữ SRS hiện hành.

**Tiền đề đã dựng cho lượt đo:**

| Đợt | Mã | Trạng thái đợt | Sở Tư pháp HN | Đơn vị khác |
|---|---|---|---|---|
| X | `DOT-SO_BO_6_THANG-2027-1` (QA tạo mới) | Tạo đợt | Chưa nộp | — |
| Y | `DOT-SO_BO_6_THANG-2026-1` (có sẵn) | **Đã tổng hợp** | **Đang lập** | Bộ KH&ĐT **đã nộp** 07/08 |
| Z | `DOT-SO_BO_NAM-2027-1` (QA tạo mới) | Tạo đợt | Chưa nộp | — |

Chương trình HTPL: đã seed thêm `CT-20260811-0001` → ô chọn có đủ **2** mục.

**Kết quả từng bước** (tài khoản `cbnv_hn`, bó mã `assets/index-x06iyQ52.js`):

| Bước | Đo gì | Kết quả |
|---|---|---|
| 1 | Mở chi tiết đợt X khi HN chưa bấm lập | ✅ Cả 2 khối **không** hiện — đúng thiết kế, đây chính là chỗ đối tác đo hụt |
| 2 | Bấm [Lập báo cáo] → xác nhận "Bắt đầu lập báo cáo?" | ✅ 1 request `POST /start`, 1 thông báo *"Đã bắt đầu lập báo cáo"*; khối **Nhận xét, kiến nghị** (ô nhập, 0/5000) và khối **Chương trình HTPL liên quan trong kỳ** (ô chọn nhiều) đều hiện và nhập được |
| 3 | Nhập `QA-NXKN-20260811-1152` + chọn đúng 2 chương trình → [Lưu nháp] → tải lại bằng địa chỉ | ✅ 1 request `PATCH /bao-cao`, 1 thông báo; đọc lại **đúng chuỗi** (bộ đếm 21/5000) và **đúng 2** chương trình, không mất không thừa |
| 4 | **Phép thử quyết định** — mở đợt Y (Bộ KH&ĐT đã nộp, đợt đã tổng hợp) | ✅ Khối **vẫn hiện, vẫn nhập được**; sửa nhận xét thành `QA-NXKN-DOTY-20260811-1156` + thêm chương trình thứ 2, lưu, tải lại đọc lại đúng. Màn còn hiển thị "Trạng thái: **Đang lập báo cáo**" — tức bám theo trạng thái nộp của chính đơn vị, không bám trạng thái đợt |
| 5 | Chứng âm `cbnv_tw` mở đợt X | ✅ **0 ô nhập / 0 ô chọn** (chỉ hiển thị chỉ đọc + nút [Tổng hợp]) |
| 6 | *(riêng 339)* Đợt Z, bỏ trống hoàn toàn ô Chương trình | ✅ Lưu nháp OK **và** [Trình duyệt KQ] thành công → "Chờ duyệt kết quả" |

⇒ Dòng 338 đạt cả 4 điều kiện (a)(b)(c)(d); dòng 339 đạt cả 5 điều kiện (a)(b)(c)(d)(e).

**Một bẫy đã suýt chấm sai ở bước 6:** lần trình đầu bị chặn *"Vui lòng hoàn chỉnh báo cáo trước khi trình"*. Không kết luận ngay là do ô Chương trình trống — mở phần trả lời của máy chủ thì lý do là `chiTieuConThieu: ["12. KP chi HĐ khác", "13. KP xã hội hóa"]` (mã `ERR-XI-07-01`). Điền 2 chỉ tiêu đó xong, ô Chương trình **vẫn để trống** thì trình được ngay ⇒ ô này đúng là không bắt buộc.

**Ảnh:** `image/LBCKQTHCT_05-06-b1-dotX-chua-lap-khong-co-khoi-2026-08-11.png` · `…-b2-dotX-sau-lap-hien-2-khoi-…` · `…-b3-dotX-doc-lai-sau-tai-lai-…` · `…-b4-dotY-donvi-khac-da-nop-van-nhap-duoc-…` · `…-b5-chungam-TW-khong-co-o-nhap-…` · `LBCKQTHCT_06-b6-de-trong-o-chuongtrinh-van-trinh-duoc-2026-08-11.png`

**Việc còn lại của BA (không chặn dev, không chặn 2 dòng này):** sửa `srs-fr-15-ct-htpldn.md` cho khớp thực tế đã chạy — đổi điều kiện hiển thị dòng 39 (và 21a/21b ở :1167 · :1168) từ *neo trạng thái đợt* sang *neo trạng thái nộp của đơn vị*, và bổ sung dòng khai khối "Chương trình liên quan" vào bảng thành phần (Loại 4 hướng B, khuôn UI-12).

---

## Lượt 3 (11/08 tối) — Dòng 64 · DGKQHTVV_01 → PASS, đã ghi **Test done**

**Bó mã:** `assets/index-BTT8H1bn.js` (mới, khác `index-x06iyQ52.js` của lượt sáng) — ghi ở cả đầu và cuối phiên đo.

**Vụ việc dùng để đo:** `VV-BTP-TW-20260806-004` — trạng thái `HOAN_THANH`, `danhGia = null`, tức **sạch, chưa ai đánh giá**. Đây chính là bẫy FAIL/PASS oan lớn nhất của dòng này nên đã kiểm bằng bản ghi trước khi bấm.

| Bước | Việc làm | Kết quả |
|---|---|---|
| 1 | DN `0109998887` → Vụ việc HTPL → mở `VV-BTP-TW-20260806-004` từ **danh sách** | Nút **[Đánh giá]** hiện ra |
| 2 | Nhập 9 · 8 · 10 + nhận xét `QA-DGKQ-20260811-2255` → [Xác nhận] | Toast **"Đã đánh giá vụ việc"**; `POST /api/v1/vu-viecs/{id}/danh-gia` trả **201**, `loaiNguoiDanhGia: "DN"`; **không** còn "Lỗi hệ thống", không còn 500 |
| 3 | Tải lại trang **bằng địa chỉ**, đọc lại khối Đánh giá | Hiện đúng **9.0 / 8.0 / 10.0**, điểm tổng 9.0, người đánh giá "QA UAT Kiem Thu DN", nhận xét đúng chuỗi `QA-DGKQ-20260811-2255` — không mất, không cắt |
| 4 | Phép thử phân biệt bằng `cbnv_tw` | **Không chạy** — theo đúng tiêu chí, chỉ chạy khi bước 2 vẫn lỗi |
| 5 | DN khác `0209888006` dán thẳng địa chỉ vụ việc trên | **"Không tìm thấy vụ việc."** — vế chặn không vỡ |

**Kiểm thêm để khỏi PASS oan:** mở lại `VV-BTP-TW-20260804-001` (đã có đánh giá) bằng chính tài khoản DN — nút [Đánh giá] không còn hiện, tức đường gửi trùng đã bị chặn ở mức giao diện, không có cách nào ép ra lỗi hệ thống nữa.

**Bộ bắt thông báo:** cài trước khi bấm, tự kiểm `soObserverDangSong = 1`, không lọc trùng, đếm cả lời gọi khác GET → đúng **1 thông báo** và **1 lời gọi** cho thao tác gửi.

**Ảnh:** `image/r2-DGKQHTVV_01-b2-dn-gui-danhgia-thanh-cong-2026-08-11.png` · `…-b3-doc-lai-sau-tai-lai-…` · `…-b5-dn-khac-van-bi-chan-…`

> ⚠️ **Một chỗ sai trong ghi chú lượt trước cần biết:** ô `Kết quả verify` cũ của dòng 64 (viết lúc chiều) ghi *"CẢ 4 vụ việc Hoàn thành của doanh nghiệp này đều đã có đánh giá"* và liệt kê `VV-BTP-TW-20260806-004` trong đó. Thực tế lượt này bản ghi `-20260806-004` vẫn `HOAN_THANH` / `danhGia = null`. Câu đó **sai**. Vì dòng đã chuyển Test done và quy ước là "hết lỗi thì không đụng cột khác", ô vẫn giữ nguyên chữ cũ — nếu cần sửa cho sạch hồ sơ thì phải làm riêng.

---

## Lượt 3 (11/08 tối) — Dòng 342 · GKQTHCTHTPL_01 → phần A PASS, phần B còn sót → ghi **Reopen**

**Bó mã:** `assets/index-BTT8H1bn.js`. Đặc tả `srs-fr-15-ct-htpldn.md` **vẫn chưa sửa** (không đổi từ 06/08 12:46), nên căn cứ chấm phần B là **quyết định BA ghi trong chính ô `Kết quả verify`**, theo đúng chỉ đạo "BA sẽ cập nhật SRS sau".

**Phần A — đạt cả 3 điều kiện:**

| Bước | Kết quả |
|---|---|
| A1 · `cbnv_tw` mở Chi tiết đợt Z | Không còn nút gửi lên TW (danh sách nút chỉ có `["Tổng hợp"]`). Ép gọi thẳng chức năng gửi bằng chính phiên đó → bị từ chối, câu trả lời là **tiếng Việt** nêu đúng lý do nghiệp vụ ("Chỉ đơn vị BN/ĐP mới gửi BC lên TW"), **không** còn chuỗi "Forbidden" hay chuỗi tiếng Anh thô |
| A2 · `cbnv_hn` bấm [Gửi lên TW] → [Đồng ý] | Đúng **1** lời gọi + **1** thông báo: *"Đã gửi báo cáo lên Trung ương"*; trạng thái đơn vị chuyển "Đã gửi TW"; bảng Tiến độ nộp của TW hiện `Sở Tư pháp Hà Nội · DP · Đã nộp · 11/08/2026` |

**Sáu ý phụ — đã đo LẠI trên bó mã hiện hành, không chép kết quả 07/08:** ghi nhận thời điểm gửi (15:30:48 cho HN, 15:36:46 cho Bộ KH&ĐT) · đánh dấu vào danh sách tổng hợp của TW (`DA_GUI_TW` cho cả hai) · thông báo cho cán bộ TW (2 thông báo, đúng mốc giờ từng lượt gửi) · lưu vết ngày nộp kèm mã báo cáo từng đơn vị · nguyên văn thông báo nhanh đúng tiếng Việt. Đã **hủy** hộp thoại [Tổng hợp] để không làm đổi trạng thái đợt khi chỉ đang đọc.

**Phần B — dựng đợt `DOT-TRON_NAM-2027-1`, 3 đơn vị (HN · Bộ KH&ĐT · An Giang):**

| Bước | Việc làm | Kết quả |
|---|---|---|
| B1 | HN đi trọn luồng lập → lưu nháp → trình duyệt → `cbpd_hn` phê duyệt → gửi TW; Bộ KH&ĐT để đang lập dở; An Giang chưa mở | Dựng xong |
| B2 | Đọc Chi tiết đợt bằng 3 phiên | HN đọc **"Đã gửi TW"** (bước 5) · Bộ KH&ĐT đọc **"Đang lập báo cáo"** · **TW đọc "Tạo đợt"** (bước 1) trong khi bảng ngay dưới ghi 2 đơn vị **Đã nộp 11/08/2026** |
| B3 | `cbpd_bn` phê duyệt rồi `cbnv_bn` bấm [Gửi lên TW] | **Gửi được** — `POST …/gui-tw` trả 200, toast "Đã gửi báo cáo lên Trung ương", trạng thái "Đã gửi TW". **Không** bị chặn vì HN đã gửi trước ✅ |
| B4 | `cbnv_tw` mở danh sách đợt, dùng bộ lọc tiến độ | Cột vòng đời đã bỏ, thay bằng **"Tiến độ nộp"** (`2/3`, `1/2`, `0/2`…). Ba mức lọc trả đúng và **không rỗng**: Chưa có đơn vị nào nộp → 1 đợt · Đang nộp dở → 4 đợt (có đợt vừa nộp) · Đã đủ đơn vị → 2 đợt ✅ |
| + | Vế quá hạn: dựng `DOT-SO_BO_6_THANG-2025-1` hạn nộp 31/07/2025 | Đơn vị vẫn bấm được **[Lập báo cáo]**, chuyển "Đang lập báo cáo", giữ trạng thái thật ✅ |

**Chỗ còn lỗi — phép thử phân biệt đã chạy:** mở đợt `DOT-TRON_NAM-2026-1` (đã tổng hợp) bằng **chính** phiên `cbnv_tw` thì ô đó đọc **"Đã tổng hợp"** và thanh bước nhảy tới bước 6. Vậy ô trạng thái trên màn Chi tiết đợt đang bám **vòng đời của ĐỢT**, không phải tiến trình của đơn vị đang đăng nhập — đúng trục mà BA đã chốt bỏ. Hệ quả: vòng đời đợt nay đứng ở "Tạo đợt" suốt giai đoạn nộp rồi nhảy thẳng sang "Đã tổng hợp", các bước 2·3·4·5 không bao giờ hiện; và tài khoản Trung ương đọc ra đúng cái ảnh mà đối tác đã chụp.

**Ảnh:** `image/r2-GKQTHCTHTPL_01-B2-TW-doc-taodot-du-2-donvi-danop-2026-08-11.png` (ảnh lỗi) · `…-A1-TW-khong-co-nut-gui-…` · `…-A2-hn-gui-tw-thanh-cong-…` · `…-B3-donvi-B-gui-duoc-sau-donvi-A-…` · `…-B4-TW-loc-tiendo-dangnopdo-…` · `…-B-quahan-van-lap-duoc-…`

**Đối chiếu với nội dung gốc đối tác log (đã kiểm riêng, 11/08 tối):** phiếu gốc ghi tác nhân là **CB NV BN/ĐP**, các bước là mở Chi tiết đợt rồi bấm "Gửi Trung ương", kết quả thực tế là *"Forbidden"*. Chấm riêng 5 gạch "Kết quả mong đợi" của phiếu bằng số liệu lượt này thì **đạt cả 5** (chuyển sang "Đã gửi TW" trên màn của CB NV ĐP · ghi nhận thời điểm gửi + đánh dấu vào danh sách tổng hợp TW · thông báo cho CB NV TW · lưu vết ngày nộp kèm mã báo cáo · thông báo nhanh đúng nguyên văn), và chữ "Forbidden" đã hết. Lưu ý câu chữ: gạch thứ nhất viết "chuyển trạng thái **đợt báo cáo**" — trục của đợt hôm nay không đổi, chỉ trạng thái nộp của **đơn vị** đổi; đây đúng là thứ BA chốt bỏ nên không tính lỗi. **Vậy nếu chỉ bám nội dung đối tác log thì dòng này đã đạt.** Chỗ Reopen (tài khoản Trung ương đọc "Tạo đợt") nằm **ngoài** case của đối tác, thuộc vế (b) do BA bồi thêm. **Quyết định của user 11/08: giữ Reopen**, bám tiêu chí phần B trong ô `Kết quả verify`.

**Ghi nhận thêm, KHÔNG chấm FAIL:** BA có nhắc "Quá hạn" nên thành nhãn cảnh báo suy ra từ hạn nộp, nhưng màn hiện chưa có nhãn nào cho đợt quá hạn. Điều kiện PASS/FAIL của phiếu chỉ đo "đơn vị quá hạn có bị khoá không" — không bị khoá, nên đạt. Nhãn cảnh báo là việc BA/dev chốt sau.

**Tài khoản:** `cb_nv_dp_10` · `cb_nv_dp_09` · `cb_nv_bn_09` đều **đăng nhập không được** (`ERR-AUTH-LOGIN-01`) dù `input/input.md` ghi đã đặt lại mật khẩu ngày 11/08 → theo Rule 7 đã dùng `cbnv_bn` / `cbpd_bn` (CB NV + CB PD **Bộ Kế hoạch và Đầu tư**) làm đơn vị B, và đã đưa đơn vị này vào phạm vi đợt để giữ đúng vai trò/cấp.

---

## Lượt 4 (12/08) — Dòng 342 · GKQTHCTHTPL_01 → PASS, đã ghi **Test done**

**Bó mã:** `assets/index-CutX4DNo.js` — ghi ở **đầu và cuối** phiên, cả hai lần đều bó mã này, và khác `index-BTT8H1bn.js` của lượt 11/08 ⇒ đúng là bản dựng mới. Dev đổi ô `Trạng thái dev fix` về *Fixed* nhưng **để trống ô phản hồi**, không nói sửa gì → đo lại toàn bộ, không dùng lại số liệu 11/08.

**Bước 1 — TW mở Chi tiết đợt `DOT-TRON_NAM-2027-1` (2/3 đơn vị đã nộp):** màn **đã bỏ hẳn** ô "Trạng thái" vòng đời **và** thanh 6 bước (đếm được 0 phần tử bước). Thay vào đó là **"Tiến độ nộp 2/3"** + bảng theo đơn vị + dòng "Đã nộp: 2/3 đơn vị". Không còn chỗ nào mâu thuẫn với bảng tiến độ. ✅

**Bước 3 — phép thử phân biệt (vẫn chạy dù bước 1 đã đạt, để loại khả năng chỉ ẩn theo điều kiện):** mở đợt `DOT-TRON_NAM-2026-1` (**đã tổng hợp**) bằng CHÍNH phiên TW → cũng 0 thanh bước, cũng không có nhãn "Đã tổng hợp", chỉ có Tiến độ nộp 2/2. ⇒ ô vòng đời của đợt bị **gỡ hẳn**, không phải ẩn theo trạng thái. ✅

**Bước 2 — cùng đợt đó đọc bằng phiên đơn vị (`cbnv_hn`):** thanh bước nay mang nhãn của **trục đơn vị** — `Chưa nộp · Đang lập · Chờ duyệt · Đã duyệt · Đã nộp · Đã tổng hợp` — đang dừng ở bước 5 **Đã nộp**, kèm ô riêng "Trạng thái nộp của đơn vị: Đã nộp". Hai vai trò không còn đọc ra hai vòng đời mâu thuẫn: TW không còn trục vòng đời nào, đơn vị đọc đúng trục của mình. ✅

**Bước 4 — 3 vế "không được vỡ", đo TƯƠI hết, không chép lượt trước:**

| Vế | Cách đo lượt này | Kết quả |
|---|---|---|
| Bộ lọc tiến độ của TW | Mở danh sách đợt, bấm lần lượt cả 4 thẻ | Cột vòng đời vẫn không có; cột **"Tiến độ nộp"** còn nguyên. Tất cả: 8 · Chưa có đơn vị nào nộp: 2 · **Đang nộp dở: 4** · Đã đủ đơn vị: 2 — không thẻ nào rỗng, đợt vừa có đơn vị nộp nằm đúng thẻ ✅ |
| Đơn vị nộp **sau** vẫn gửi được | Tài khoản An Giang (`cb_nv_dp_10`, `cbnv_ag`) vẫn 401 → **dựng đợt mới `DOT-TRON_NAM-2028-1`** phủ Hà Nội + Bộ KH&ĐT. HN chạy trọn luồng gửi TW lúc 23:38:57 (1/2). Sau đó Bộ KH&ĐT mở chính đợt đó: đọc "Chưa nộp", vẫn có [Lập báo cáo] → lập → lưu nháp → trình duyệt → `cbpd_bn` phê duyệt → **[Gửi lên TW]** | `POST …/gui-tw` **200**, thông báo *"Đã gửi báo cáo lên Trung ương"*, trạng thái đơn vị "Đã nộp", tiến độ **2/2**. Không bị chặn vì HN đã gửi trước ✅ |
| Đơn vị quá hạn vẫn lập tiếp được | **Dựng đợt quá hạn mới `DOT-TRON_NAM-2025-1`** (hạn nộp 31/12/2025), mở bằng `cbnv_hn` | Vẫn bấm được **[Lập báo cáo]** → "Đã bắt đầu lập báo cáo", trạng thái "Đang lập" ✅. **Mới so với 11/08:** cạnh trạng thái nay có thêm **nhãn "Quá hạn"** — đúng thứ BA chốt (Quá hạn thành nhãn cảnh báo suy ra từ hạn nộp, không phải một giá trị trạng thái) |

**Vế (a) — liếc lại xem có hồi quy không:** TW mở Chi tiết đợt chỉ có nút `["Tổng hợp"]`, không có nút gửi; ép gọi thẳng chức năng gửi bằng chính phiên TW → **403** với câu tiếng Việt *"Chỉ đơn vị BN/ĐP mới gửi BC lên TW"*; quét toàn màn không còn chuỗi "Forbidden". ✅

**Ý phụ đo kèm trên chính lượt gửi hôm nay:** ngày nộp ghi 12/08/2026 cho cả hai đơn vị · TW nhận đủ **2 thông báo** đúng mốc 23:38:57 và 23:42:15 · danh sách tổng hợp của TW ghi cả hai lượt là `DA_GUI_TW` kèm giờ. ✅

**Bộ bắt thông báo:** cài trước mỗi lần bấm, tự kiểm `soObserverDangSong = 1`, không lọc trùng, có đếm lời gọi khác GET.

**Ảnh:** `image/r3-GKQTHCTHTPL_01-b1-TW-khong-con-o-vongdoi-2026-08-12.png` · `…-b2-donvi-doc-truc-cua-minh-…` · `…-b4a-TW-loc-tiendo-…` · `…-b4b-donvi-nop-sau-van-gui-duoc-…` · `…-b4c-quahan-nhan-canhbao-van-lap-duoc-…`

> **Ghi chú quy trình:** dòng này Test done nên **không đụng** ô `Kết quả verify` — ô đó vẫn giữ nguyên văn Reopen của lượt 11/08. Bản sao lưu trước lượt đo: `backup-o-sheet-truoc-khi-ghi/row342-KetQuaVerify-truoc-luot3-2026-08-12.txt`.

---

## Thay đổi dữ liệu do lượt đo này gây ra (bàn giao cho lượt sau)

| Bản ghi | Trước | Sau |
|---|---|---|
| `VV-BTP-TW-20260804-001` | Đang xử lý | Hoàn thành → đã đánh giá 9·8·10 (bởi `cbnv_tw`, nhận xét `QA-DISCRIM-CB-20260811-1827`) |
| `VV-BTP-TW-20260803-001` | Đang xử lý | Hoàn thành → đã đánh giá 9·8·8 (dựng để đo ca tổng lẻ, nhận xét `QA-DGKQ-TONGLE-20260811`) |
| `DOT-SO_BO_6_THANG-2026-1` (đợt Y) | HN đang lập, nhận xét `QA-NXKN-20260811-1836`, 1 chương trình | nhận xét đổi thành `QA-NXKN-DOTY-20260811-1156`, **2** chương trình |
| `VV-BTP-TW-20260806-004` | Hoàn thành, **chưa** ai đánh giá (ghi chú lượt chiều nói "đã đánh giá" là **sai**) | Đã đánh giá 9·8·10 bởi **DN** `0109998887`, nhận xét `QA-DGKQ-20260811-2255` — bản ghi dùng để chấm PASS dòng 64 |
| `DOT-TRON_NAM-2027-1` (đợt B) | *chưa tồn tại* | QA tạo mới, 3 đơn vị. HN **đã gửi TW** · Bộ KH&ĐT **đã gửi TW** · An Giang chưa nộp |
| `DOT-SO_BO_6_THANG-2025-1` (đợt quá hạn) | *chưa tồn tại* | QA tạo mới, hạn nộp 31/07/2025 (quá hạn). HN **đang lập báo cáo** |
| `DOT-SO_BO_NAM-2027-1` (đợt Z) | HN Chờ duyệt kết quả | HN **đã gửi TW** (dùng cho phần A) |
| `DOT-TRON_NAM-2028-1` (đợt C) | *chưa tồn tại* | QA tạo 12/08, 2 đơn vị. HN **đã nộp** 12/08 · Bộ KH&ĐT **đã nộp** 12/08 → tiến độ 2/2 |
| `DOT-TRON_NAM-2025-1` (đợt quá hạn mới) | *chưa tồn tại* | QA tạo 12/08, hạn nộp 31/12/2025, 1 đơn vị. HN **đang lập báo cáo**, có nhãn "Quá hạn" |
| `DOT-SO_BO_6_THANG-2027-1` (đợt X) | *chưa tồn tại* | QA tạo mới; HN đang lập, nhận xét `QA-NXKN-20260811-1152`, 2 chương trình |
| `DOT-SO_BO_NAM-2027-1` (đợt Z) | *chưa tồn tại* | QA tạo mới; HN đã **trình duyệt** → Chờ duyệt kết quả, ô chương trình để trống |
| `CT-20260811-0001` | *chưa tồn tại* | QA tạo mới (Dự thảo) để ô chọn có đủ 2 chương trình |

Tài khoản: `cbpd_tw` **không đăng nhập được** ("Tên đăng nhập hoặc mật khẩu không đúng") → đã fallback sibling cùng vai trò/cấp `cbpd_tw_01` theo Rule 7.

## Sao lưu

Nội dung gốc 5 ô `Kết quả verify` + `Trạng thái dev fix` đã sao lưu trước khi ghi, tại thư mục nháp phiên làm việc (`backup/row{20,64,65,338,339}-*.txt`).

Lượt 3 (11/08 tối): ô `Kết quả verify` dòng 342 đã sao lưu nguyên văn 5.692 ký tự vào `backup-o-sheet-truoc-khi-ghi/row342-KetQuaVerify-truoc-luot2-2026-08-11.txt` **trước** khi ghi đè. Dòng 64 chỉ đổi `Trạng thái dev fix` → Test done, **không** đụng ô `Kết quả verify` (đúng quy ước "hết lỗi thì không đụng cột khác").
