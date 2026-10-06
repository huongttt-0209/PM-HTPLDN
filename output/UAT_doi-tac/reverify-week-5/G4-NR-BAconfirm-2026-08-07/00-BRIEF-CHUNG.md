# Lô G4 — Verify lại bug `Dopai = N/R` ∩ `Trạng thái dev fix = BA confirm` (2026-08-07)

> **File này là nguồn chung của cả team.** Mọi agent đọc trước khi làm. Không lặp nội dung
> file này vào note riêng — trỏ về đây.

## Tham số đợt

| Tham số | Giá trị |
|---|---|
| Sheet | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab **`bug`** (gid=1714340219) |
| Môi trường đo | `https://18.143.165.120.nip.io` — env **NỘI BỘ**, KHÔNG phải env đối tác `htpldn-uat.ospgroup.vn` |
| MailHog | `http://18.143.165.120:8025` |
| Tài khoản | `output/UAT_doi-tac/input/input.md`. Bộ nghiệp vụ mật khẩu `Test@1234`; `admin`/`Secret@123` chỉ dùng prep/điều tra, **không ra verdict** |
| SRS nguồn chuẩn | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **mở file đọc thật mới được quote số dòng** |
| Bản dựng tại thời điểm mở lô | `index-BbPPdate.js`, `last-modified 2026-08-07 06:47:57 UTC` = **13:47:57 giờ VN** |
| Output lô | `output/UAT_doi-tac/reverify-week-5/G4-NR-BAconfirm-2026-08-07/` |
| Dữ liệu 7 dòng gốc | `do/00-sheet-7-dong-goc.txt` (đã dump trọn 26 cột — **đọc từ đây, đừng gọi lại API**) |

## Phạm vi — 7 dòng, chạy theo đúng thứ tự này

**Nhóm A trước (3 dòng)** — lượt đo cũ chạy trên bản dựng CŨ `index-eWHwDgt2.js` (09:11 VN) ⇒ đo lại trên bản hiện tại là công việc thật:

| # | Dòng | Mã TC | Nội dung | Căn cứ BA/Dev (ô S, CHỈ ĐỌC) |
|---|---:|---|---|---|
| A1 | 10 | `KTDGKQHT_05` | Tải tệp Excel điểm danh | BA chốt 04/08: KHÔNG thêm trường mã HV; cơ chế "Tải mẫu → điền → tải lên"; `lich_hoc_id` ở metadata tệp; thêm `ERR-KQ-09`, đổi câu `ERR-KQ-03` |
| A2 | 343 | `THBCTHCT_01` | Tổng hợp báo cáo thực hiện chương trình từ nhiều đơn vị | Dev tự fix theo SRS (`INF-XI-09-01`); đã sửa: danh sách tổng hợp trả đúng bản ghi từng đơn vị (trước gộp sai theo đợt) |
| A3 | 344 | `THBCTHCT_02` | Bấm "Tổng hợp" → gợi ý số liệu Biểu 21a/21b | Dev tự fix theo SRS; đã bổ sung gợi ý số liệu 21a/21b + xuất Excel/Word theo mẫu TT 17/2025/TT-BTP |

**Nhóm B sau (4 dòng)** — lượt đo cũ đã chạy trên **đúng bản dựng hiện tại**:

| # | Dòng | Mã TC | Nội dung | Căn cứ BA (ô S, CHỈ ĐỌC) |
|---|---:|---|---|---|
| B1 | 308 | `QLHDTVVCG_02` | Bộ lọc màn danh sách Hợp đồng tư vấn | BA 06/08 hướng A: giữ quyết định 11/05 **bỏ menu riêng**; phần mềm đúng bản gốc; lối vào = Chi tiết Vụ việc / Lịch sử TVV. Dev đã bổ sung bộ lọc ngữ cảnh |
| B2 | 319 | `QLHDTVVCG_13` | Nút "Thêm hợp đồng" mở biểu mẫu Thêm mới | BA 06/08 hướng A (như trên) |
| B3 | 321 | `QLHDTVVCG_15` | Thêm hợp đồng thành công, sinh mã `HDTV-…` | BA 06/08 hướng B: câu thông báo đúng là **"Đã lưu hợp đồng"** (`INF-HDTV-01`); Kết quả mong đợi của phiếu viết ĐÚNG. Dev đã dùng chung câu này cho mọi đường lưu |
| B4 | 345 | `THBCTHCT_05` | Xuất tệp báo cáo tổng hợp (Excel/Word) | BA 06/08: (1) tên tệp `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}.xlsx/.docx` theo Phụ lục E; (2) khối ký = ngày ký + họ tên cán bộ xuất + chỗ trống chữ ký/chức vụ/con dấu, **KHÔNG in sẵn dòng chức danh**. Dev đã áp cả hai |

## 🔴 Điểm xuất phát khác mọi lô trước — ĐỌC KỸ

Cả 7 dòng **đã có bài verify của chính QA trong ngày hôm nay**, nằm ở ô `Kết quả verify` (cột T),
dài 5.700–10.000 ký tự, và verdict lượt đó là **"cần BA xác nhận"** — đó chính là lý do ô R đang
mang giá trị `BA confirm`.

Hệ quả bắt buộc:

1. **ĐỌC ô T của dòng mình trong `do/00-sheet-7-dong-goc.txt` TRƯỚC KHI đo.** Trong đó đã ghi rõ
   tiền đề đã dựng (mã vụ việc, mã khóa học, mã đợt báo cáo, tài khoản), đường vào thực tế, và
   **chính xác điểm nào còn treo**. Dựng lại từ đầu = phí thời gian và dễ lệch tiền đề.
2. **Việc của lượt này KHÔNG phải "đo lại từ số 0"** mà là: *căn cứ BA đã chốt ở ô S có làm cho
   điểm treo đó hết treo không?* Nếu hết → chốt được Pass/Reopen. Nếu điểm treo là thứ BA **chưa**
   nói tới → giữ `BA confirm`, KHÔNG được ép sang Pass cho tròn lô.
3. **Nhóm A còn một câu hỏi thật cần trả lời:** lượt cũ đo trên bản 09:11, bản hiện tại là 13:47.
   Phải kiểm bản dựng **trước và sau** lượt đo của mình và ghi vào note.

## 🔴 PHẠM VI ĐO — user chốt 2026-08-07, CẤM mở rộng

Mỗi case chỉ đo **đúng hai thứ**, không hơn:

1. **Các bước trong bug gốc** — chạy đúng cột `[J] Các bước thực hiện` của chính dòng đó, chấm theo
   cột `[K] Kết quả mong đợi` và việc đối tác phản ánh ở cột `[Q] TKM phản hồi lần 1`.
2. **Nội dung BA chốt** — ô `[S] DEV phản hồi lần 1`. BA chốt gì thì đo nấy, từng ý một.

**CẤM:** tự nghĩ thêm kịch bản ngoài 2 nguồn trên · đo lan sang màn/chức năng khác · dựng lại toàn bộ
tiền đề khi ô T đã ghi sẵn tiền đề dùng được · điều tra sâu một điểm mà cả phiếu lẫn BA đều không nhắc.

**Ngoại lệ duy nhất:** lỗi **tự lộ ra** trong lúc chạy đúng các bước trên thì vẫn phải báo lead (luật 7)
— báo, chứ **không** được mở rộng case để đi tìm.

## Quy tắc chốt verdict — chỗ dễ sai nhất của lô này

| Đo được gì | Ô `Trạng thái dev fix` (cột R) |
|---|---|
| Lỗi **đối tác báo ban đầu** đã hết, các ý chấm được đều ĐẠT; phần còn lại chỉ là điểm đặc tả chưa quy định và **không chặn bàn giao** | **`Test done`** (Pass) — ô T phải nói rõ còn điểm gì treo |
| Lỗi đối tác báo **vẫn còn**, hoặc việc Dev khai đã làm ở ô S mà đo ra **chưa làm / làm sai** | **`Reopen`** |
| Điểm treo là thứ **BA chưa chốt** và nó quyết định đạt/không đạt của phiếu | **giữ `BA confirm`** — ghi rõ câu hỏi cần BA |

- 🔴 **Không được Pass bằng quan sát tĩnh.** Phải tự tay chạy thao tác. Xuất tệp thì phải **mở đọc nội
  dung tệp** (openpyxl / PyMuPDF / python-docx) — `200 + binary` chỉ chứng minh CREATE, không chứng
  minh CORRECT.
- 🔴 **Không được Reopen oan vì bản ghi cũ.** Bug về trường lưu trong DB (tên tệp, snapshot, nhãn nhật
  ký) phải đo trên **bản ghi tạo mới sau lúc dev fix**; bản ghi cũ vẫn hỏng là bình thường.
- 🔴 **1 phiếu gộp nhiều ý → chấm từng ý rồi mới ra verdict tổng.** Có ≥1 ý Reopen → tổng Reopen.
  Không có Reopen mà còn ý cần BA → tổng `BA confirm`. Mọi ý đạt → `Test done`.
- **Bước 1 của phiếu ghi "Chọn menu Hợp đồng Tư vấn" là lối vào ĐÃ HẾT HIỆU LỰC** (BA 11/05 bỏ menu
  riêng). Đây là đường đi, **không phải điểm chấm** → không được tính là lỗi. Đường thực tế:
  Vụ việc HTPL → Chi tiết vụ việc → mục "HĐ tư vấn liên kết".

## Luật chung — áp cho mọi agent trong lô

1. **Tuần tự tuyệt đối.** Xong TRỌN 1 case (đo → ảnh → note → lead ghi sheet → đọc lại xác nhận) rồi
   mới sang case kế. CẤM gom lô ghi sheet.
2. **Chỉ MỘT agent điều khiển Chrome DevTools MCP tại một thời điểm.** Trình duyệt dùng chung —
   chạy song song = nhiễm phiên đăng nhập giữa các vai trò = verdict vô giá trị.
3. **Ghi nhãn bản dựng ở mỗi case** (đọc bằng `curl -sk https://18.143.165.120.nip.io/login | grep -oE 'index-[A-Za-z0-9_-]+\.js'`),
   đo **cả trước và sau** lượt đo. Tab MCP mở lâu vẫn chạy JS cũ → **tải lại trang** trước khi verify.
4. **Bắt thông báo chỉ bằng** `output/UAT_doi-tac/tools/toast-capture.js`. CẤM tự viết observer có lọc
   trùng, CẤM dùng `textContent` gộp. Cài lại observer sau **mỗi** lần điều hướng SPA.
5. **Tiền đề thiếu thì TỰ TẠO** (dữ liệu / trạng thái / tài khoản) — không phải blocker. Chỉ blocker khi
   BE/DB/env hỏng thật.
6. **Ảnh:** lưu vào `image/` của lô, đặt tên `<mãTC>-<mô-tả-ngắn>.png`. Chụp ở MỌI thao tác đổi trạng
   thái và **mở ảnh ra đọc** — lưu mà không đọc = vô nghĩa. Toast sống ~3s → hẹn giờ bấm nút rồi mới
   chụp; trượt thì lấy phản hồi request làm bằng chứng.
7. **Bug tình cờ ngoài phạm vi case vẫn phải log** — báo lead, lead mở dòng mới bằng
   `tools/sheet_add_bug_row.py`. Không lặng lẽ bỏ qua.

## Ghi sheet — lead làm, agent KHÔNG tự ghi

| Verdict | Ô `Trạng thái dev fix` (cột R) |
|---|---|
| Pass | `Test done` |
| Reopen | `Reopen` |
| Cần BA | `BA confirm` (giữ nguyên) |

- Diễn giải → ô **`Kết quả verify`** (cột T). Lượt này **OVERWRITE** nội dung cũ (kỷ luật "1 dòng
  latest"); giá trị cũ được lưu trong `tools/sheet_update_audit.jsonl` để khôi phục.
- 🔴 **Ô CHỈ ĐỌC, CẤM ghi đè:** `Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) ·
  `DEV phản hồi lần 1` (S).
- Prompt đợt này **không cấp** ô `Ảnh/video verify` (U) ⇒ **không ghi cột U**; link ảnh xem được nhúng
  thẳng trong ô `Kết quả verify`.
- Lệnh ghi: `tools/sheet_bug_verify_write.py` — `--dry-run` trước, ghi thật, rồi **đọc lại** bằng
  `UAT_TAB=bug python3 tools/sheet_read.py --row <N>`. Script chặn → **DỪNG, báo lead**. CẤM ghi tay.

## 🔴 Nội dung ô `Kết quả verify` cũng PHẢI nằm trong phạm vi — user chốt 2026-08-07 22:0x

Ô gửi đối tác **chỉ được nói về**: (1) các bước / Kết quả mong đợi của chính phiếu đó, và (2) nội dung
BA/Dev chốt ở ô `[S]`. Hết.

**CẤM đưa vào ô sheet:** mục "ghi nhận thêm" / "điểm đề nghị ghi nhận" / "các điểm đã nêu ở lượt trước"
liệt kê quan sát ngoài phiếu (thiếu lối vào menu, hai nút trùng tên, nhãn không dấu, chưa có màn xem
lại, đề nghị đổi cách trình bày…). Những quan sát đó **vẫn ghi trong note chi tiết** ở `note/` để nội bộ
biết, và báo lead — nhưng **không** đi vào ô đối tác đọc.

*(Đã áp hồi tố: ô của A2 dòng 343 và A3 dòng 344 đã cắt các mục này trước khi ghi.)*

## Văn phong ô `Kết quả verify` — người đọc là ĐỐI TÁC

- Tiếng Việt có dấu, gạch đầu dòng, tả **triệu chứng lần này**.
- Mở đầu bằng: ngày giờ đo + nhãn bản dựng + tài khoản/vai trò đã dùng.
- **CẤM lộ nội bộ:** so sánh 2 môi trường, video đối tác quay, mã màn `SCR-xx`/`MH-xx`, jargon
  (API 200, snake_case, CRUD, endpoint), lịch sử BA chốt nội bộ, số dòng đặc tả.
- Icon quy ước: ✅ là bug · ⚠️ cần BA xác nhận · ❌ không phải lỗi.
- Case "không phải lỗi" vẫn ghi `Test done`, ô diễn giải mở đầu bằng **"❌ Không phải lỗi"**.

## Bàn giao của agent về lead (bắt buộc đủ 5 mục)

1. `verdict`: `Test done` | `Reopen` | `BA confirm`
2. Đường dẫn file note chi tiết trong `note/`
3. Đường dẫn file **nội dung ô `Kết quả verify`** trong `note/` (văn phong đối tác, đã sẵn sàng ghi thẳng)
4. Danh sách ảnh trong `image/` + 1 câu mô tả ảnh nào chứng minh điều gì
5. Trả lời: *"ngoài tiêu chí đang chấm, có thấy gì bất thường không?"* — có thì mô tả, không thì ghi
   rõ "không phát hiện thêm"
