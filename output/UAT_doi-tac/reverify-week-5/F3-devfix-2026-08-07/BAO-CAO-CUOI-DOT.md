# Báo cáo cuối đợt — FLOW 03 · lô F3-devfix-2026-08-07 (6 case)

**Nhánh:** RE-VERIFY DEV FIX · **Bảng:** tab `bug` (gid 1714340219) · **Nguồn đặc tả:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
**Môi trường:** `https://18.143.165.120.nip.io` (NỘI BỘ, không phải env nghiệm thu của đối tác)

## Kết quả 6 case

| Dòng | Mã TC | Verdict | Ô `Trạng thái dev fix` | Bản dựng đã đo (bó mã) |
|---:|---|---|---|---|
| 36 | CNHSNLTVV_03 | ✅ Pass | `Test done` | `index-D4Buvu4S.js` (R4+R5, vân tay đầu = cuối) |
| 37 | CNDSMLTVV_01 | 🔁 Reopen | ghi `Reopen` 01:12 — **bị đổi ngược về `fixed`** | `index-B2W2Krcs.js` |
| 51 | XNTGHTVV_03 | ✅ Pass | `Test done` | `index-B2W2Krcs.js` |
| 64 | DGKQHTVV_01 | 🔁 Reopen | `Reopen` | `index-B2W2Krcs.js` |
| 126 | LKHDG_12 | ✅ Pass | `Test done` | `index-DsMHK7Dp.js` |
| 127 | LKHDG_16 | ✅ Pass | `Test done` | `index-DsMHK7Dp.js` |

Ô ghi chú (`Kết quả verify`) của **cả 6 dòng** đã đối chiếu live: trùng khít từng ký tự với `note/*.md`.
Nội dung cũ của ô đã chép nguyên văn vào `audit/<MaTC>-ketqua-verify-CU.md` **trước khi** đè.

---

## Mục 1 — Lỗi phát hiện thêm ngoài phạm vi

Đây là **candidate**, không phải verdict. Theo luật của lô: phát hiện đã xếp loại candidate thì **CẤM**
đồng thời đem ra làm căn cứ chấm case. Mọi số dòng dưới đây đều **tự mở file đếm lại ngày 07/08**.

| # | Phát hiện | Gặp ở | Đặc tả nói gì | Đề xuất |
|---:|---|---|---|---|
| 1 | Mở hồ sơ năng lực của `CG-QLND38-UAT` → *"Hồ sơ năng lực không tồn tại"* (404) trong khi bản ghi vẫn có trong danh sách | 36 | im lặng | Dev tra: bản ghi có trong danh sách nhưng không có hồ sơ năng lực kèm theo |
| 2 | Trường **Trình độ** hiện mã thô `THAC_SI` thay vì nhãn tiếng Việt | 36 | im lặng về nhãn | Dev FE — nhất quán với các trường khác đã có nhãn |
| 3 | Thông báo công khai **thiếu mã/tên đối tượng**, trong khi mẫu chuẩn là *"Đã công khai {ten_doi_tuong} '{ma_hoac_ten}' lên Cổng Pháp luật Quốc gia."* | 37 | `srs-v3.5.md:6772` (E.I.1 — 5 mẫu thông báo chuẩn) ✅ **đã xác minh dòng** | Dev FE |
| 4 | Dòng thời gian ở **chế độ doanh nghiệp** hiện sự kiện **Phân công** — là sự kiện nội bộ phải ẩn | 64 | `srs-fr-05-vu-viec.md:1810` ✅ **đã xác minh dòng** | Dev FE |
| 5 | Danh sách vụ việc của DN `0109998887` **không trả 2 vụ việc** mang cùng `doanhNghiepId` | 64 | `:1846` chỉ nói lọc theo DN — có thể còn lọc thêm theo đơn vị | Dev BE tra; **chưa đủ căn cứ kết luận** |
| 6 | Dropdown **"Trạng thái"** ở thanh lọc dùng nhãn ngoài bộ trạng thái đặc tả (*Đang đánh giá / Đã đánh giá / Lập báo cáo*) và **thiếu mục "Hủy"** | 126, 127 | `srs-fr-08-danh-gia.md:827` — enum có đủ `… / HOAN_THANH / HUY` ✅ **đã xác minh dòng** | Dev FE — thiếu `HUY` là lệch thật |
| 7 | Nút **"Bộ lọc nâng cao (2)"** không có trong đặc tả vùng thanh lọc | 126, 127 | `srs-fr-08-danh-gia.md:824-829` (trọn vùng filter-bar) ✅ **đã xác minh vùng** | BA xác nhận: bổ sung ngoài đặc tả hay đặc tả thiếu |
| 8 | Nút lưu vẫn mang tên **"Lưu nháp"** trên đợt đã ở trạng thái *Phân công* (không còn là bản nháp) | 127 | im lặng | Dev FE — không chặn nghiệp vụ |
| 10 | Chứng chỉ chỉ có tệp (không nhập tên chứng chỉ): tab **"Hồ sơ"** để trống dòng *"Chứng chỉ chi tiết"*, trong khi tab **"Năng lực"** cùng lúc hiện đủ tên tệp — hai tab hiển thị không thống nhất | 36 (R5) | `srs-fr-04-chuyen-gia-tvv.md:1576` chỉ đặc tả tab *"Năng lực"* | Dev FE. **KHÔNG kéo vào verdict case 36**: khối khoá chỉ nói về tab "Năng lực", kéo tab "Hồ sơ" vào là **nới khối khoá**. R3 cũng bắt chuỗi kỹ thuật ở **tab Năng lực** (không phải tab Hồ sơ) ⇒ đây là bề mặt khác, không phải fix nửa vời |
| 9 | `GET /api/v1/files/{id}` trả **403 `ERR-PERM-FILE-03`** *"Loại đối tượng 'TVV_HO_SO' của tệp chưa được đăng ký"* — mọi màn nạp tệp đó bị đẩy sang trang báo không có quyền | 36 (R3) | — | **Đã tự hết ở R4** (200 cho 5/5 tệp, gồm đủ 3 tệp từng 403). Ghi lại để dev biết đã có một giai đoạn hỏng |

### Không phải lỗi — đã kiểm và loại, ghi lại để khỏi tố oan

| Quan sát | Vì sao KHÔNG log |
|---|---|
| Doanh nghiệp không thấy **Nhóm 4 / 5 / 7** ở màn chi tiết vụ việc | `srs-fr-05-vu-viec.md:1805`/`:1806`/`:1808` — **cố ý ẩn** với DN |
| Dòng thời gian chế độ DN có sự kiện **"Từ chối"** | `:1810` **liệt kê "từ chối" trong nhóm DN ĐƯỢC thấy**. Ban đầu candidate ghi gộp cả "Từ chối" — **đã thu hẹp lại, chỉ còn "Phân công"** |
| Hệ thống **từ chối công khai** một Tư vấn viên chưa có Số thẻ hành nghề | `srs-fr-04-chuyen-gia-tvv.md:1507` — *"Số thẻ hành nghề · Bắt buộc nếu Loại = Tư vấn viên"* ⇒ **từ chối là ĐÚNG**. Lỗi nằm ở chỗ khác: báo thành công sai + không nêu lý do từng bản ghi |
| `cbnv_tw_02` (cấp TW) nhìn thấy và tích chọn được hồ sơ **khác đơn vị** (`TVV-STP-AG-0001`) | `srs-fr-04-chuyen-gia-tvv.md:1420` im lặng về cấp TW (phạm vi *"Toàn quốc"*) |
| Hồ sơ ở *Yêu cầu bổ sung* tự chuyển sang *Đang thẩm định* sau khi lưu năng lực | `srs-fr-04-chuyen-gia-tvv.md:405` — đúng máy trạng thái |

---

## Mục 2 — Case chưa kết luận được × vì sao × cần gì để kết luận

| Case / vế | Vì sao chưa kết luận | Cần gì | Ai làm |
|---|---|---|---|
| **64 · vế D3** — *một bên đã chấm, bên còn lại vào chấm* | Muốn dựng thì **doanh nghiệp phải chấm được trước** — mà đó **chính là vế đang hỏng**. Đường thay thế đã thử và loại: 2 vụ việc `VV-BTP-TW-20260806-003/-004` **không thuộc** danh sách của `0109998887` | Sửa xong nhánh doanh nghiệp rồi mới dựng được tiền đề | Dev BE + Dev FE |
| **64 · dữ kiện gửi BA** | Mâu thuẫn *"vụ việc đã ở Đã đánh giá thì bên còn lại có được vào đánh giá không"* nằm ở **bảng nút chế độ CÁN BỘ** (`:1751`, chỉ có dòng `HOAN_THANH`). Ở **nhánh doanh nghiệp** thì `:1809` và `:1811` **thống nhất** ⇒ đặc tả **không** tự mâu thuẫn | BA chốt cho nhánh cán bộ. **Không kéo verdict case 64** — đó là lý do dòng 64 ghi `Reopen` thuần, **không** đánh dấu `Dopai = BA` | BA |
| **36** | ✅ **đã kết luận được** — nhưng phải đo **3 lượt** mới xong. R3 (Reopen) chạy trên bản dựng bị thay sau 9 phút ⇒ tự nó không đủ tin. R4 đo lại 2 quan sát quyết định → đạt, **nhưng còn 3 GAP** vì khối khoá đòi 6 lượt [Lưu] mà R4 chỉ chạy 2 ⇒ **agent đo từ chối nâng thành Pass**, đúng luật. R5 chạy nốt 4 lượt trên **cùng bó mã** với R4 (kiểm vân tay trước khi đo, đầu = cuối) ⇒ GAP trống, Pass | *(đã xong)* | — |

---

## Mục 3 — Rủi ro quy trình phát hiện trong lô (không thuộc 2 mục bắt buộc, nhưng phải nói)

**a) Verdict QA bị ghi đè khi lô còn đang chạy.** Cột `Trạng thái dev fix` **vừa là ô dev khai, vừa là ô
QA chấm**. Nhật ký công cụ chứng minh dòng 36 và 37 đều được ghi `Reopen` thành công (00:42 và 01:12),
sau đó **bị gõ tay đổi ngược** về `Fixed` / `fixed` (hai cách viết hoa-thường khác nhau). Ô ghi chú không
mất. ⇒ Cần **cửa sổ đóng băng** cột trong lúc QA chấm, hoặc **một cột riêng cho QA**. Bằng không mỗi vòng
re-verify đều có thể bị ghi đè trước khi đối tác kịp đọc.

**b) Môi trường deploy liên tục trong lúc đo.** 5 bó mã khác nhau trong 12 giờ; bó mã thứ 5 lên **giữa lúc
đang đo case 127**. Đã loại trừ nguyên nhân khác: 6/6 lượt `GET /` trả cùng etag + cùng bó mã ⇒ **không phải**
nhiều máy chủ phục vụ bản khác nhau. ⇒ Kết luận re-verify trên env này có **hạn dùng tính bằng chục phút**.

**c) 🔴 Nhãn phiên bản trên màn KHÔNG dùng làm định danh bản dựng được.** Bó mã `index-DsMHK7Dp.js`
(06/08 18:51 GMT) **mới hơn** bó mã của bản gắn nhãn V1.0.10 (`index-B2W2Krcs.js`, 17:39 GMT), nhưng sidebar
vẫn ghi **V1.0.9**. Bó mã tiếp theo (`index-D4Buvu4S.js`, 19:23 GMT) sidebar vẫn ghi V1.0.9.
⇒ Định danh thật = **bó mã `assets/index-*.js` + `last-modified`**. Mọi báo cáo phải ghi **cả mốc giờ đo**.
Đã sửa 3 dòng Re-test từng ghi *"bản dựng V1.0.9"* — dev đọc sẽ tưởng đo trên bản cũ hơn V1.0.10 rồi bác Pass.

**d) Độ lệch số dòng SRS KHÔNG đồng đều — cấm áp một offset chung.**

| File SRS | Lệch so với hồ sơ cũ |
|---|---|
| `srs-v3.5.md` | **+44 … +45** (BR-DATA-06 `5525→5570`; BR-PUBLIC-01 `5685→5729`) |
| `srs-fr-08-danh-gia.md` | **+2** ở vùng `:161`/`:823`/`:839`; **+5** ở vùng bảng chuyển trạng thái `:1190-1199` |
| `srs-fr-11-bao-cao.md` | **+5** |
| `srs-fr-04-chuyen-gia-tvv.md` · `srs-fr-05-vu-viec.md` | **0** |

**e) Công cụ ghi bảng bị thay giao diện giữa lô.** `tools/sheet_bug_verify_write.py` nay là công cụ tổng quát:
**giữ** khớp định danh dòng, kiểm dropdown thật, ghi batch, đọc lại, audit log — và **mạnh hơn** ở chỗ bắt buộc
khai giá trị cũ cho mọi ô sửa (chống đè mất thay đổi của dev). Nhưng **mất 2 chốt**: ép dẫn dòng SRS, và chặn
Pass khi quan hệ ≠ match. Lô này đã đóng verdict + quan hệ + dòng SRS vào `--reason` để audit log giữ vết,
nhưng từ nay **hai chốt đó do người chịu, không còn máy chặn**.
