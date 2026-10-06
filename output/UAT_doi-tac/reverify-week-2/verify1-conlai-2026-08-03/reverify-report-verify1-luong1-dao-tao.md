# Báo cáo verify vòng 1 — LUỒNG 1: Đào tạo, tập huấn (6 case)

- **Ngày:** 2026-08-03
- **Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · rows 116–121
- **Môi trường:** `https://18.143.165.120.nip.io` · bản dựng **HTPLDN V1.0.5** (bundle build 2026-08-03 07:59 GMT)
- **SRS đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md`
- **Cách ghi:** bước 1 `--mode qaverdict` (ghi Q + R). Bước 2 — **theo yêu cầu user 2026-08-03**, đồng bộ cột `Trạng thái dev fix 1` (P) = cột `Verify` (Q) cho các dòng **chưa Pass** bằng `--mode verify1`; 2 dòng `Pass` giữ `dev done` vì đã nhất quán.
- **Ký hiệu ⚠️ trong note:** mọi dòng thuộc phần **cần BA quyết** (vướng mắc đặc tả + câu hỏi cho BA + dòng trạng thái "ĐANG CHỜ BA XÁC NHẬN") đều gắn ⚠️ đầu dòng để phân biệt với phần mô tả bug. Phần mô tả bug giữ nguyên, không cắt.

## 1. Kết quả 6 case

| row | Mã TC | **P = Q** | **Q (QA)** | Kết luận ngắn | SRS neo |
|---|---|---|---|---|---|
| 116 | KTDGKQHT_02 | `BA confirm` *(cũ: `Reject`)* | **BA confirm** | Đối tác quan sát đúng (tab "Kết quả" chỉ 10 cột, bất biến ở 3 trạng thái). SRS **tự mâu thuẫn**: đặc tả cột 2 tab đều thiếu 4 trường, nhưng Outputs UC24 có đủ. Lập luận của dev ("4 cột thuộc tab Điểm danh") **sai dữ kiện** — tab đó chỉ 7 cột. | `:1901` · `:1896` · `:600-603` · `:520` |
| 117 | QLKTLBG_09 | `Open` *(cũ: `dev done`)* | **Open** | Xem trước bài giảng `.pptx` → khung xem trước **trắng hoàn toàn**, không trình chiếu, không thông báo thay thế, không nút Tải về. | `:1955` · `:792` · `:1951` · `:726` |
| 118 | QLDXDTTH_01 | `dev done` | **Pass** | Chứng minh dương tính end-to-end: gửi → `201 MOI_GUI` → danh sách tự cập nhật → còn sau hard reload → cán bộ đúng đơn vị thấy + nhận thông báo trùng giây. | `:1043` · `:1053` · `:1057` · `:1875` |
| 119 | QLLKHDTBD_09 | `Open` *(cũ: `Reject`)* | **Open** | Tái hiện **2/2 bộ lọc**: màn 1 dòng / 2 dòng nhưng file Excel đều **13 dòng** = trọn kho. Request xuất **có** mang tham số lọc ⇒ lỗi ở bước dựng dữ liệu file. | `:1752` · `:1147` · `:1152` · BR-DATA-06 `srs-v3.5.md:5524` |
| 120 | PDKHDTTH_04 | `BA confirm` *(cũ: `Reject`)* | **BA confirm** | Chặn duyệt khác cấp là **đúng SRS**; quan sát đối tác cũng đúng (0 request → 0 thông báo, 2/2 lần). Tranh chấp rơi vào vùng **3 nguồn nội bộ mâu thuẫn**. Dev sai 1 ý: FE **gỡ hẳn nút**, message của BE không tới người dùng. | `:1217` · `:1221` · `:683` · `:1774` · `:277` · `:283` · BR-AUTH-05 `srs-v3.5.md:5480` |
| 121 | CBKQDTBD_01 | `dev done` | **Pass** | Tab "Công bố kết quả" nay **có**, hiện vô điều kiện (8 tab ở cả khoá *Đang diễn ra* lẫn *Hoàn thành*). Ảnh đối tác cho thấy khoá của họ **đã Hoàn thành** mà chỉ có 7 tab ⇒ fix thật. Đã chứng minh tab hoạt động (Công bố / Hủy công bố), dữ liệu khôi phục nguyên trạng. | `:1350` · `:1891` · `:1909` · `:1363-1364` |

**Tổng:** 2 `Open` · 2 `BA confirm` · 2 `Pass` · 0 `Reject` · 0 ô TRỐNG.

**Đối chiếu với dev:** dev khai `Reject` 3 dòng → QA bác **2/3** (119 thành `Open`, 116 thành `BA confirm`); chỉ 120 là dev đúng phần "chặn", nhưng sai phần "FE hiển thị toast end-to-end". Dev khai `dev done` 3 dòng → QA xác nhận **2/3** (`Pass`), còn 117 vẫn lỗi (`Open`).

## 2. Bug mới phát hiện ngoài phạm vi case (đã mở dòng TC mới trên sheet)

| row | Mã TC | Q | Nội dung | Nguồn |
|---|---|---|---|---|
| 130 | KTDGKQHT_20 | `Open` | Tỷ lệ chuyên cần lấy mẫu số = số buổi **đã điểm danh** thay vì **tổng buổi của khoá** (3 buổi, điểm danh 1 → hiện `1/1 = 100%`). Ngưỡng 80% ⇒ sai kết luận Đạt/Không đạt. Đo 3 cách độc lập. | case 116 |
| 132 | QLKTLBG_10 | `Open` | Bài giảng **PDF** cũng không xem trực tuyến được ("refused to connect"), không có nút Tải về. Tái hiện 3/3. | case 117 |
| 134 | QLDXDTTH_10 | `Open` | Tab Đề xuất thiếu cột "Người đề xuất" (`:1875`); máy chủ có trả dữ liệu. | case 118 |
| 135 | QLDXDTTH_11 | `BA confirm` | **Cán bộ đúng đơn vị không có thao tác "Tiếp nhận"** ⇒ đề xuất kẹt vĩnh viễn ở "Mới gửi"; ngược lại cán bộ lại thấy nút "Gửi đề xuất mới". SRS mâu thuẫn: `:1045`/`:1875` vs ma trận quyền `srs-v3.5.md:1309`. **Có thể block cả nhóm TC đề xuất.** | case 118 |
| 136 | QLDXDTTH_12 | `Open` | Lộ mã kỹ thuật `DAN_SU - Dân sự` ra người dùng. | case 118 |
| 137 | QLDXDTTH_13 | `Open` | Thông báo "Đề xuất đào tạo mới" dùng biểu tượng **X đỏ báo lỗi**. | case 118 |
| 144 | QLLKHDTBD_50 | `Open` | Danh sách Kế hoạch đào tạo chỉ 8 cột, thiếu ô tích chọn / Số chương trình / Người tạo / Ngày tạo (`:1767-1775`); ngân sách hiện số thô `100000000.00`. | case 120 |
| 146 | CBKQDTBD_02 | `Pass` | Lỗi **có thật lúc 17:55** (7 cột) nhưng **đã sửa** ở gói giao diện triển khai 19:51 cùng ngày; đo lại 20:00 trên đúng khoá đó thấy **đủ 12 cột**. Đã đính chính note + chuyển `Verify = Pass`; dev tự đặt `P = dev done`. Cột "Đề kiểm tra" hiện **vô điều kiện** (chưa gán đề → `—`). | case 121 |
| 147 | KTDGKQHT_21 | `Open` | Tab "Kết quả" thiếu cột **"Đề kiểm tra"** (`:1901`) ở **cả 4 tình huống** đo — kể cả khi khoá đã gán đề và điểm đã trỏ đúng đề. Đối chứng dương tính: Tab 8 cùng bản dựng **có** cột đó ⇒ dữ liệu đã tới giao diện. | case 116 |
| 148 | KTDGKQHT_22 | `Open` | Tab "Đề kiểm tra" chỉ có 5 cột, thiếu **STT · Mã đề · Lĩnh vực · Người thêm** (`:1908`) và cột Hành động không có **"Xem chi tiết"**. Lỗi tĩnh. | phát sinh khi seed đề |

## 3. Việc còn treo

1. ✅ **ĐÃ XONG — row 130 + 146 nay đã có verdict.** Soát lại cả 8 dòng OOS phát hiện **3 dòng hở**, không chỉ 2: row 146 hở **cả P lẫn Q**, row 130 hở Q, row 135 hở P. Đã vá đủ. **Nguyên nhân gốc:** `sheet_add_bug_row.py` lấy giá trị từ file JSON do agent soạn và **không cảnh báo khi thiếu ô trạng thái** → agent nào quên khai là dòng đó hở. Đây là lỗ hổng công cụ, sẽ lặp ở các luồng khác nếu không sửa.
2. ⏳ **Ảnh bằng chứng của các dòng OOS là tên file trần**, chưa phải link Drive xem được — dev mở sheet không xem được ảnh. `tools/drive_upload_evidence.py` chỉ có batch cứng `r1..r5`, chưa có batch cho đợt này. **Chưa làm — chờ quyết định.**
3. ✅ **3 nghi vấn đã chốt xong** (vòng seed 19:45–20:20, gói `index-RAuQ-eDH.js`) — audit: [`reverify-audit/seed-de-kiem-tra-2026-08-03.md`](reverify-audit/seed-de-kiem-tra-2026-08-03.md):
   - (a) Tab "Kết quả" thiếu cột `Đề kiểm tra` → **LÀ BUG**, đã mở row 147 `KTDGKQHT_21`. Đo 4 tình huống (có/không gán đề × 2 khoá), `colgroup = 10`, 0 cột ẩn, đã cuộn ngang hết cỡ.
   - (b) `Xếp loại` có giá trị khi `Điểm` trống → **KHÔNG PHẢI BUG, lỗi phép đo của QA**: ô Điểm là `<input>` nên `td.innerText` luôn rỗng. Đọc `input.value` + API đều khớp BR-KQ-01 (`:2230`). Không mở dòng.
   - (c) Danh sách cột thiếu của row 146 → **đã sai và đã đính chính**: lỗi có thật lúc log nhưng bản dựng 19:51 đã sửa; row 146 chuyển `Pass`.
   - Kèm theo phát hiện Tab 7 thiếu 4 cột → đã mở row 148 `KTDGKQHT_22`.
   - **Đã dựng đề kiểm tra ĐẦU TIÊN của hệ thống** (`QA-DEKT-0803`) — trước đó kho đề trống, nên mọi TC liên quan đề kiểm tra trước đây đều chưa test được thực chất.
4. ⚠️ **Row 130 (`KTDGKQHT_20`) — giữ nguyên `Open`, KHÔNG dùng lại quan sát vòng seed.** Vòng seed có đo lại và thấy `tongBuoi = 1` trên khoá `KH-QAW7-HOINGHI`, nhưng **đó đúng là khoá mà dev đã cảnh báo sẽ còn sai** (*"giá trị stored — khóa cũ tự đúng khi điểm danh lần kế"*), nên quan sát đó **không chứng minh được bản fix hỏng**. Verdict `Open` vẫn đúng vì **chính dev cũng công nhận "BUG thật"**. Khi nào muốn chuyển `Pass`/`Reopen` thì **bắt buộc dựng khoá mới**, thêm nhiều buổi, điểm danh một phần rồi mới đo — xem [`reverify-audit/KTDGKQHT_20.md`](reverify-audit/KTDGKQHT_20.md).
5. ⏳ **Row 135 (`QLDXDTTH_11`) cần BA quyết sớm** — nếu CB NV thật sự không có quyền tiếp nhận thì toàn bộ luồng đề xuất đào tạo không đi tiếp được. Đã đưa vào file gửi BA (mục 3, đánh dấu ưu tiên cao nhất).
6. 🚫 **4 dòng lệch `P='dev done'` vs `Q='Open'`** (rows 132, 134, 136, 137) — **quyết định: giữ nguyên**, không đồng bộ. Lý do: `dev done` ở các dòng này được dev viết **sau** khi QA mở bug, kèm số hiệu commit — là thông tin mới hơn kết luận QA. Cặp giá trị hiện tại đọc ra đúng thực tế: *dev bảo đã sửa, QA đã xác nhận là bug thật và chưa kiểm lại bản sửa.*

## 3b. Đồng bộ cột P = cột Q (thực hiện theo yêu cầu 2026-08-03)

Ban đầu 6 dòng luồng 1 ghi theo `--mode qaverdict` (chỉ Q + R, không đụng P của dev). Sau đó đồng bộ P = Q cho **4 dòng chưa Pass**; 2 dòng `Pass` giữ `dev done` vì đã nhất quán.

| row | Mã TC | P cũ (của dev) | P mới |
|---|---|---|---|
| 116 | KTDGKQHT_02 | `Reject` | `BA confirm` |
| 117 | QLKTLBG_09 | `dev done` | `Open` |
| 119 | QLLKHDTBD_09 | `Reject` | `Open` |
| 120 | PDKHDTTH_04 | `Reject` | `BA confirm` |

**Note dev bị đè đã archive nguyên văn** trước khi ghi: row 117 → `reverify-audit/QLKTLBG_09.md` (dev thừa nhận bug thật, khai đã fix ở commit `abca9b459` / PR #71 — nhưng bản trên UAT lúc đo vẫn lỗi, cần re-verify sau deploy); row 130 → `reverify-audit/KTDGKQHT_20.md` (dev khai fix ở commit `94bf3820`, cảnh báo là **giá trị stored** nên khoá cũ chỉ tự đúng khi điểm danh lần kế → re-verify phải dùng **dữ liệu MỚI**).

## 3c. File gửi BA

`ba-confirm/ba-confirmation-needed-luong1-dao-tao-2026-08-03.md` — theo `output/template/ba-confirmation-needed-template.md`, gồm 3 mục, **cả 3 đều Dạng B** (SRS tự mâu thuẫn / không quy định).

**2 lỗi citation đã phát hiện và sửa khi soạn file này** (tự mở SRS kiểm lại thay vì tin số dòng agent báo):

1. **M-05 bị trích sai file** — nằm ở `srs-v3.5.md:683`, không phải `srs-fr-03-dao-tao.md:683` (dòng 683 của file đào tạo là dòng kẻ bảng trong mục "Xuất Excel").
2. **M-05 bị dùng sai phạm vi** — nguyên văn chỉ nói về **menu item** (*"menu item chỉ hiện nếu vai trò có quyền truy cập ≥ 1 chức năng trong đó"*), không nói về nút thao tác trong màn chi tiết. Điều này làm **yếu** hướng "ẩn nút là đủ" và **mạnh** hướng "phải có thông báo" ở mục `PDKHDTTH_04`. Đã tách thành câu hỏi phụ riêng cho BA và **ghi đè lại note row 120** trên sheet cho khớp.

**Ký hiệu ⚠️:** mọi dòng thuộc phần cần BA quyết trong note gửi lên sheet đều gắn ⚠️ đầu dòng (11 dòng ở row 116, 6 dòng ở row 120), phần mô tả bug giữ nguyên không gắn — để phân biệt *sự thật đã đo* với *thứ đang chờ BA*.

## 4. Rủi ro quy trình ghi nhận trong đợt

- **Nhiều phiên QA chạy song song dùng chung một profile trình duyệt MCP.** Agent case 121 bị đăng xuất **5 lần** do phiên khác đăng nhập `cbnv_tw_02` trên cùng profile; nhiều khả năng đây cũng là nguyên nhân thật của "2 lần rớt phiên 401" mà case 119 quy cho BE restart. Kết quả 6 case vẫn đứng vững nhờ mỗi phép đo có đối chứng danh tính tài khoản, nhưng đây là rủi ro false-positive phân quyền — cần tách profile hoặc chạy tuần tự giữa các phiên.
- **Phiên chạy LUỒNG 2 dùng `--mode verify1` → ghi đè mất cột P của dev** ở rows 122, 123, 125, 126 (`Reject`/`dev done` → verdict QA). Giá trị cũ khôi phục được từ `tools/sheet_write.log` (`writes[].old`). Trái `PROMPT §5.1` (yêu cầu `--mode qaverdict` cho cả 27 dòng).
- **Dev phản hồi realtime**: rows 130 và 132 đã có `P='dev done'` + giải trình chỉ ~1 giờ sau khi QA mở → các dòng OOS này cần một vòng re-verify.

## 5. Tài khoản đã bổ sung vào `input/input.md`

- `cbnv_dp` login FAIL 401 → dùng `cbnv_dp_01` (đã ghi nhận, Rule 7).
- `cbpd_tw` FAIL 401 (đã biết trước) → dùng `cbpd_tw_01`.

## 6. Dữ liệu seed để lại cho dev re-test

| Mã | Mô tả |
|---|---|
| `KH-20260803-0003` | Kế hoạch đào tạo 05/07–25/07/2026 — lọc 01/07–31/07/2026 phải ra **đúng 1 dòng** trong file Excel (case 119). |
| `KH-20260803-0004` | Kế hoạch cấp ĐP, trạng thái **Chờ duyệt** — dùng test phê duyệt khác cấp (case 120). |
| `b69a9545-59e4-4121-9760-91be29b65c19` | Đề xuất đào tạo mở đầu `QA-VERIFY-0803`, trạng thái "Mới gửi" (case 118). |
| `KH-QAW7-HOINGHI` | Khoá *Đang diễn ra*, 3 buổi lịch học + 1 buổi đã điểm danh — dùng tái hiện lỗi tỷ lệ chuyên cần (row 130). |
