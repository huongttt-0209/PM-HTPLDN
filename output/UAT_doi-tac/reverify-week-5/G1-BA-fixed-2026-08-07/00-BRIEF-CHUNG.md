# Lô G1 — Verify lại bug Dopai=BA ∩ Trạng thái dev fix=Fixed (2026-08-07)

> **File này là nguồn chung của cả team.** Mọi agent đọc trước khi làm. Không lặp lại nội dung
> file này vào note riêng — trỏ về đây.

## Tham số đợt

| Tham số | Giá trị |
|---|---|
| Sheet | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** (gid=1714340219) |
| Môi trường đo | `https://18.143.165.120.nip.io` — **KHÔNG** phải env đối tác `htpldn-uat.ospgroup.vn` |
| MailHog | `http://18.143.165.120:8025` |
| Bộ tài khoản | **04** (`cbnv_tw_04` / `cbpd_tw_04` / … · mật khẩu `Test@1234`). Vai trò QTHT chỉ có `admin` / `Secret@123` (không có biến thể `_04`) |
| SRS nguồn chuẩn | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **quote số dòng phải mở file đọc thật** |
| Phiếu BA đã chốt | `../ba-confirm/phan-hoi-ba-7-diem-can-chot-2026-08-06.md` |
| Phiếu BA **chưa** trả lời | `../ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md` (mục 1 = `VVDTN_04`) |
| Output lô | `output/UAT_doi-tac/reverify-week-5/G1-BA-fixed-2026-08-07/` |
| Dữ liệu 11 dòng gốc | `do/00-sheet-11-dong-goc.txt` (đã dump từ sheet, đọc từ đây, đừng gọi lại API) |

## Phạm vi — 11 dòng

| # | Dòng | Mã TC | Cụm | Nội dung bug gốc |
|---|---|---|---|---|
| 1 | 178 | `VVDTN_04` | **C — biểu đồ** | BC Vụ việc đã tiếp nhận: thiếu biểu đồ tròn theo lĩnh vực + bảng thiếu cột Theo kênh / Theo lĩnh vực |
| 2 | 179 | `VVDTN_06` | A — xuất Excel | BC Vụ việc đã tiếp nhận: bấm Xuất Excel → "Forbidden" |
| 3 | 185 | `VVDHT_06` | A | BC Vụ việc đang hỗ trợ: Xuất Excel → "Forbidden" |
| 4 | 189 | `VVDHTHT_06` | A | BC Vụ việc đã hỗ trợ hoàn thành: Xuất Excel → "Forbidden" |
| 5 | 195 | `VVTTG_05` | A | BC Vụ việc theo thời gian: Xuất Excel → "Forbidden" |
| 6 | 222 | `VVTDVQL_06` | A | BC Vụ việc theo đơn vị quản lý: Xuất Excel → "Forbidden" |
| 7 | 226 | `VVTLV_05` | A | BC Vụ việc theo lĩnh vực: Xuất Excel → "Forbidden" |
| 8 | 230 | `VVTLHDN_05` | A | BC Vụ việc theo loại hình DN: Xuất Excel → "Forbidden" |
| 9 | 234 | `VVTTGCT_05` | A | BC Vụ việc theo tổ chức/thời gian chi tiết: Xuất Excel → "Forbidden" |
| 10 | 263 | `CPCTHTTTG_05` | A | BC Chi phí chi trả hỗ trợ theo thời gian: Xuất Excel → "Forbidden" |
| 11 | 362 | `QLNDTVVCG_OOS_04` | B — nhật ký | Nhật ký thao tác CG từ chối không hiện lý do |

## 🔴 ĐÍNH CHÍNH 2026-08-07 15:1x — số dòng SRS trong brief này ĐÃ LỆCH, dùng bảng dưới

A1 mở file đọc lại hôm nay và phát hiện: **SRS đã được sửa ngày 06/08 để áp kết luận BA**, nội dung
trôi xuống. Mọi số dòng tôi ghi ở các mục dưới là số của bản **trước khi sửa**.

| Chỗ brief ghi | Số dòng THẬT (đọc 2026-08-07) |
|---|---|
| `srs-fr-11-bao-cao.md:1051` / `:1052` / `:1053` (3 nút) | **`:1056` / `:1057` / `:1058`** |
| `srs-fr-11-bao-cao.md:1064` / `:1065` / `:1067` (bảng loại biểu đồ) | **`:1069` / `:1070` / `:1072`** |
| `srs-fr-11-bao-cao.md:215` (dữ liệu theo lĩnh vực) | **`:218`** |
| `srs-fr-11-bao-cao.md:1268` (QTHT bypass) | **`:1273`** — và **nội dung đã ĐẢO**, xem dưới |
| `srs-v3.5.md:1335` (dòng BAO_CAO ma trận quyền) | **`:1339`** |
| `srs-fr-12-tv-chuyen-sau.md:198` (nhật ký kèm lý do) | **`:204`** |

Vẫn đúng nguyên, không đổi: `srs-fr-11-bao-cao.md:51` · `:62` · `:79` · `:85` · `:117` · `srs-v3.5.md:684`.

🔴 **Quote sai số dòng = bug invalid.** Mọi agent phải **mở file đọc lại** trước khi quote, kể cả khi
lấy từ bảng này. Chi tiết đầy đủ ở `chuan/chuan-cum-A-xuat-excel.md`.

### Hệ quả 1 — CẤM dùng lập luận "SRS có ngoại lệ QTHT bypass"

`srs-fr-11-bao-cao.md:1273` nay ghi **ngược lại**: *"QTHT không phải tác nhân của nhóm IX nên không có
ca bypass ở đây"* `[BA chốt 2026-08-06]`. Mâu thuẫn nội tại của đặc tả **đã hết**.

### Hệ quả 2 — 7 việc sửa đặc tả của BA mục 5 ĐÃ ÁP XONG vào SRS

`:79` (kiểm vai trò chặn ngay cửa vào chức năng) · `:120` (mã lỗi mới `ERR-RPT-08` cho thao tác xuất) ·
`:127`/`:128` (2 tiêu chí chấp nhận mới) · `:1046` (điều kiện vào màn) · `:1056–1058` (điều kiện vai trò
cho 3 nút) · `srs-v3.5.md:1296`/`:1298` (ô `R` là quyền dữ liệu, không kèm quyền chạy chức năng).

⇒ **Vế (b) của cụm A nay có căn cứ đặc tả trực tiếp, không còn là suy luận từ phiếu BA.** QTHT vào được
màn báo cáo là **trái `:1046`**, thấy nút Xuất là **trái `:1056–1058`**.

### Hệ quả 3 — Cụm B: đọc nhật ký bằng vai trò CHUYÊN GIA là FAIL OAN

`srs-fr-12-tv-chuyen-sau.md:1173` + tiêu chí chấp nhận `:348` quy định **cố ý**: dòng phụ "Lý do" trên
khối nhật ký **chỉ hiện với vai trò nội bộ** (CB NV / CB PD / NHT), **KHÔNG hiện với người trong mạng
lưới tư vấn**. Thêm nữa `:1189`: chuyên gia bấm [Từ chối] xong **bị đưa về màn danh sách**.

⇒ Bước "mở lại chi tiết, đọc khối Nhật ký thao tác" **bắt buộc** làm bằng **`cbnv_tw_04`**, KHÔNG phải
`qa_tvvseed28`. Mục "Cụm B" phía dưới viết thiếu vai trò — lấy đoạn này làm chuẩn.

### 🔴 Hai bẫy tiền đề — áp cho MỌI agent đo

1. **Bấm [Xem báo cáo] từ lần thứ 2 trở đi sẽ KHOÁ nút Xuất cả phiên** (lỗi riêng đã log `BCTK_QA07`).
   ⇒ Muốn xuất được thì mỗi lần xuất phải là **lần Xem đầu tiên của phiên**. Đổi bộ lọc rồi xem lại →
   nút Xuất khoá → **đó là `BCTK_QA07`, KHÔNG phải "vai trò đúng cũng không xuất được"**. Chấm nhầm chỗ
   này sẽ Reopen oan cả 9 dòng. Cách né: tải lại trang (hoặc đăng nhập lại) trước mỗi lượt xuất.
2. **Bug về trường lưu trong DB phải đo trên bản ghi MỚI.** Bản ghi tạo trước lúc dev fix vẫn hỏng là
   bình thường (dữ liệu đóng băng trước fix) → đọc lại bản ghi 06/08 sẽ **Reopen oan**. Cụm B bắt buộc
   chạy **một lượt từ chối MỚI** rồi mới đọc nhật ký.

---

## Kết luận BA đã chốt — áp làm chuẩn, KHÔNG tự suy diễn lại

### Cụm A (9 case xuất Excel) — phiếu BA mục 5

BA chốt 06/08/2026:
- Vai trò **Quản trị hệ thống KHÔNG phải tác nhân** của bất kỳ chức năng báo cáo thống kê nào
  (`srs-fr-11-bao-cao.md:51`, `:62`; 23/23 mục FR + 23/23 giao dịch UC đều chỉ ghi CB NV / CB PD).
- ⇒ **Máy chủ chặn xuất là ĐÚNG. Không nới quyền.** Đối tác đo bằng tài khoản QTHT là **sai vai trò**.
- ⇒ Nhưng **giao diện SAI**: vẫn cho QTHT vào màn báo cáo và vẫn mời bấm nút Xuất.
  **Dev action: ẩn màn báo cáo thống kê với vai trò quản trị viên — ẩn, KHÔNG làm mờ** (quy ước M-05,
  `srs-v3.5.md:684`).
- Câu từ chối hiện đang là chuỗi tiếng Anh `"Forbidden"` (`ERR-PERM-SYS-00-01`) — BA chốt phải là câu
  cho **thao tác** (*"Bạn không có quyền thực hiện thao tác này"*, mã mới `ERR-RPT-08`), **không phải**
  câu cho *xem* (`:117`). Phiếu `BUG-BCTK-QA01` của QA phải chỉnh theo — **đây là việc của QA, không
  kéo verdict 9 dòng này**.

**🔴 Quy tắc chốt verdict cụm A — đọc kỹ, đây là chỗ dễ Pass oan nhất:**

| Đo được gì | Verdict |
|---|---|
| (a) Vai trò đúng (`cbnv_tw_04`/`cbpd_tw_04`) xuất Excel **ra tệp, mở đọc được, nội dung khớp màn** **VÀ** (b) vai trò `admin`/QTHT **không còn thấy** menu Báo cáo thống kê (bị ẩn theo M-05) | **Pass** → `Trạng thái dev fix` = `Test done` |
| (a) đạt nhưng (b) **chưa** — QTHT vẫn vào được màn / vẫn thấy nút Xuất | **Reopen** — đúng việc Dev còn nợ theo BA mục 5 |
| (a) **không** đạt — vai trò đúng vẫn không xuất được tệp | **Reopen** (lỗi nặng hơn hẳn) |

- **CẤM Pass bằng quan sát tĩnh.** Phải bấm nút Xuất thật, tệp phải về máy và phải **mở đọc nội dung**
  (đúng tiêu đề báo cáo · kỳ · đơn vị · số liệu khớp từng con số trên màn · tên tệp đúng khuôn).
  `200 + binary` chỉ chứng minh CREATE, không chứng minh CORRECT.
- **CẤM** kết luận (b) bằng cách chỉ nhìn menu. Nếu menu đã ẩn thì phải kiểm thêm: gõ thẳng URL màn
  báo cáo bằng phiên QTHT → phải bị chặn/điều hướng, không được vào xem số liệu.
- Mỗi dòng là **một loại báo cáo khác nhau** → phải xuất riêng từng loại, không suy từ loại khác sang.

### Cụm B (`QLNDTVVCG_OOS_04`, dòng 362) — phiếu BA mục 6

BA chốt 06/08/2026: yêu cầu *"ghi nhật ký kèm lý do từ chối"* là **ĐẠT — không phải lỗi**.
Nhưng BA duyệt **cải tiến**: hiện lý do **có kiểm soát** trên khối nhật ký của hồ sơ; đồng thời
**tách nhãn thao tác "Từ chối"** khỏi nhãn "Cập nhật" chung.
Dev ghi ở ô `DEV phản hồi lần 1`: *"Dev đã tách nhãn thao tác 'Từ chối' … và hiển thị lý do có kiểm soát trên nhật ký."*

⇒ Phải chạy lại **đủ luồng**: CG được phân công → bấm [Từ chối nhiệm vụ] + nhập lý do → mở lại chi tiết
→ khối "Nhật ký thao tác". Pass khi dòng nhật ký mới **hiện nhãn Từ chối** (không còn gộp "Cập nhật")
**và** hiện được lý do vừa nhập. Thiếu 1 trong 2 vế → Reopen.

### Cụm C (`VVDTN_04`, dòng 178) — **BA CHƯA trả lời**

Câu hỏi treo ở `cau-hoi-BA-tong-hop-2026-08-06.md` mục 1: *BC Vụ việc đã tiếp nhận có bắt buộc có
biểu đồ tròn theo lĩnh vực không?* — SRS `srs-fr-11-bao-cao.md:1065` chốt UC125 = `Bar + Trend`
(cố ý **không** gán Donut, trong khi cùng bảng gán Donut cho UC124 `:1064` và UC127 `:1067`).
Kỳ vọng đối tác **ngược** đặc tả. Phiếu 7 điểm **không** có mục này.

Bug gốc có **2 vế**, phải đo cả hai:
- Vế (b) *bảng thiếu cột Theo kênh / Theo lĩnh vực* — vòng 06/08 đo đã hết lỗi. **Đo lại xác nhận.**
- Vế (a) *thiếu biểu đồ tròn theo lĩnh vực* — đo xem bản dựng hôm nay **đã có donut chưa**.

| Đo được gì | Verdict |
|---|---|
| Đã có biểu đồ tròn theo lĩnh vực (dev bổ sung thật) **và** vế (b) đạt | **Pass** = `Test done` — đúng kỳ vọng đối tác, hết tranh chấp |
| Vẫn không có biểu đồ tròn (đúng đặc tả hiện hành) | **`BA confirm`** — KHÔNG Reopen, KHÔNG Pass |
| Vế (b) tái hiện trở lại | **Reopen** |

## Luật chung — áp cho mọi agent trong lô

1. **Tuần tự tuyệt đối.** Xong TRỌN 1 case (đo → ảnh → note → ghi sheet → **đọc lại xác nhận**) rồi
   mới sang case kế. CẤM gom lô ghi sheet.
2. **Chỉ MỘT agent được điều khiển Chrome DevTools MCP tại một thời điểm.** Đây là một trình duyệt
   dùng chung — chạy song song = nhiễm phiên đăng nhập giữa các vai trò = verdict vô giá trị.
3. **Ghi lại nhãn bản dựng** (số hiệu build hiện trên giao diện) ở mỗi case. Tab MCP mở lâu vẫn chạy
   JS cũ → **tải lại trang** trước khi verify một bản fix mới.
4. **Bắt thông báo chỉ bằng** `output/UAT_doi-tac/tools/toast-capture.js`. CẤM tự viết observer có lọc
   trùng, CẤM dùng `textContent` gộp. Cài lại observer sau **mỗi** lần điều hướng SPA.
5. **Log bug tình cờ.** Thấy lỗi ngoài case đang verify → vẫn phải log thành dòng mới bằng
   `tools/sheet_add_bug_row.py`, mã `<tiền tố module>_QA<số>`. Không lặng lẽ bỏ qua.
6. **Ảnh bằng chứng phải là link xem được.** Lưu ảnh vào `image/`, upload Drive bằng
   `tools/drive_upload_f8.py --file … --label …` (hoặc script lô G1 nếu A2 đã dựng), rồi gắn vào cột
   `Ảnh/video verify`. Đường dẫn file trên máy QA = coi như **không có** bằng chứng.
7. **Ảnh phải bắt đúng thao tác lỗi** (toast / phản hồi 4xx của chính thao tác đó), không phải ảnh form
   chụp sau. Toast sống ~3s → hẹn giờ bấm nút rồi mới chụp; trượt thì lấy phản hồi request làm bằng
   chứng mạnh hơn ảnh.

## Ghi sheet — ô nào ghi, ô nào cấm

| Verdict | `Trạng thái dev fix` (cột R) |
|---|---|
| Pass | `Test done` |
| Reopen | `Reopen` |
| Cần BA | `BA confirm` |

- Diễn giải → cột **`Kết quả verify`** (cột T). Link ảnh → cột **`Ảnh/video verify`** (cột U).
- 🔴 **Ô CHỈ ĐỌC, CẤM ghi đè:** `Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) ·
  `DEV phản hồi lần 1` (S).
- Lệnh ghi: `tools/sheet_bug_verify_write.py` — bắt buộc `--dry-run` trước, rồi ghi thật, rồi
  **đọc lại** bằng `UAT_TAB=bug python3 tools/sheet_read.py --row <N>`.
- Giá trị phải nằm trong dropdown thật của chính ô đó. Script chặn → **DỪNG, báo lead**. CẤM ghi tay,
  CẤM viết script ad-hoc để lách.

## 🔴 Bắt buộc với 9 case cụm A — câu hướng dẫn đối tác đo lại đúng vai trò

Ô `Kết quả verify` không được dừng ở chỗ giải thích **vì sao** QTHT không xuất được. Đối tác đo vòng
trước bằng tài khoản quản trị viên; đọc xong ô này họ mở lại đúng tài khoản cũ, thấy mục "Báo cáo thống
kê" **biến mất khỏi menu**, và rất dễ mở lại phiếu với nội dung mới *"chức năng bị mất"*. Một lượt qua
lại thừa mà một câu chặn được.

Cuối ô (trước câu về bản dựng) phải có đủ **3 ý**:

1. Chức năng báo cáo thống kê **thuộc về cán bộ nghiệp vụ / cán bộ phê duyệt**.
2. Menu ẩn với tài khoản quản trị viên là **thay đổi có chủ đích**, không phải chức năng bị mất.
3. **Đề nghị Quý đơn vị kiểm thử lại bằng tài khoản cán bộ nghiệp vụ hoặc cán bộ phê duyệt.**

🔴 **ĐÍNH CHÍNH 15:40 — bản trước của mục này ghi kèm lý do *"vì tệp kết xuất là văn bản hành chính có
quốc hiệu, tiêu ngữ, tên cơ quan và họ tên cán bộ lập báo cáo"*. CẤM dùng câu đó.** Khung văn bản hành
chính theo Thông tư 17/2025 chỉ áp cho bản **PDF** (`srs-fr-11-bao-cao.md:86`, `:125`), **không** áp cho
tệp XLSX. B1 đã mở đọc 6 tệp XLSX xuất ra: đều chỉ có 4 mục đầu tệp (tên báo cáo · kỳ · đơn vị · ngày
tạo), **không có "Người tạo"**. Ghi câu đó vào ô gửi đối tác thì họ mở tệp ra là bắt được ngay.
Giữ đủ 3 ý, **bỏ vế lý do**.

Vẫn giữ nguyên các lệnh cấm ở mục dưới: không nhắc phiếu BA, không nhắc quyết định nội bộ ngày nào,
không mã màn / mã lỗi / số dòng đặc tả, không so sánh hai môi trường.

## Văn phong ô `Kết quả verify` — người đọc là ĐỐI TÁC

- Tiếng Việt có dấu, gạch đầu dòng, tả **triệu chứng lần này**.
- Mở đầu bằng ngày đo + nhãn bản dựng + tài khoản/vai trò đã dùng.
- **CẤM lộ nội bộ:** so sánh 2 môi trường, video đối tác quay, mã màn `SCR-xx`/`MH-xx`, jargon
  (API 200, snake_case, CRUD, endpoint), lịch sử BA chốt nội bộ.
- Icon quy ước: ✅ là bug · ⚠️ cần BA xác nhận · ❌ không phải lỗi.
- Case "không phải lỗi" vẫn ghi `Test done`, ô diễn giải mở đầu bằng **"❌ Không phải lỗi"**.
