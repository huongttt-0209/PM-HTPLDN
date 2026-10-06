# Lô F8 — brief chung cho cả đội (đọc TRƯỚC khi làm bất cứ việc gì)

**Ngày:** 2026-08-07 · **Quy trình bắt buộc:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
— đọc **trọn file** trước khi chạy phần việc của mình. File đó thắng mọi thói quen cũ.

---

## 1. Phạm vi & bộ lọc

Tab `bug` của `https://docs.google.com/spreadsheets/d/1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s`
(gid `1714340219`). Lọc: cột **`Dopai` (O) = `N/R`** **và** cột **`Trạng thái dev fix` (R) = `Fixed`**
→ **23 dòng**. Nội dung đầy đủ 23 dòng: [`PHAM-VI-23-dong.md`](PHAM-VI-23-dong.md) (chụp lúc 11:3x 07/08).

🔴 **Đặc điểm bất thường của lô này — đọc kỹ, nó đổi cách làm:**

- **22/23 dòng có `Trạng thái` (N) = `N/R`**, `Kết quả thực tế` (L) **RỖNG**, `Ảnh/vieo 1` (M) **RỖNG**.
  Đây là **phiếu đối tác chưa từng chạy**, KHÔNG phải bug đã báo rồi dev fix.
  ⇒ **`expected đối tác` = cột `Kết quả mong đợi` (K)**, không có "triệu chứng cũ" nào để đối chiếu.
  ⇒ Không có ảnh đối tác ⇒ Cổng bằng chứng của flow 04 rơi nhánh *"Thiếu bằng chứng nhưng tự tái hiện được
  → chạy tiếp và ghi điều kiện đã tái hiện"*. **Cấm** kết luận "không phải lỗi" chỉ vì không có bằng chứng.
- **Dòng 10 (`KTDGKQHT_05`) khác hẳn**: `Trạng thái` = `Fail`, đã có bằng chứng, và **đã có sẵn khối
  `CÁCH VERIFY`** do QA viết lúc 02:20 hôm nay ở ô `Kết quả verify`. Theo flow 04 BƯỚC 0 mục 2, dòng này
  **KHÔNG chạy flow 04 từ đầu** — chỉ chạy lại đúng khối `CÁCH VERIFY` đó
  ([`chuan/KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt`](chuan/KTDGKQHT_05-ket-qua-verify-cu-va-CACH-VERIFY.txt)).
- 🔴 **Vẫn phải chạy đủ luồng trên web.** CẤM Pass bằng quan sát tĩnh ("thấy nút đã có", "màn trông đúng").
  Fix thêm giao diện mà máy chủ vẫn hỏng là chuyện thường.

## 2. Nguồn chuẩn duy nhất — đặc tả

`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **đúng thư mục này, không bản nào khác.**
CẤM lấy số dòng từ `input/srs-update-2026-5-5/`, từ thư BA, từ báo cáo đợt cũ hay từ trí nhớ.
Mỗi trích dẫn **tự mở file đếm lại trong lượt của mình**, ghi `srs-fr-NN-x.md:DÒNG`.

- `QLHDTVVCG_*` → `srs-fr-14-hop-dong-tv.md` (536 dòng) là nơi bắt đầu; kiểm chéo `srs-fr-05-vu-viec.md`,
  `srs-fr-12-tv-chuyen-sau.md` khi vế nói tới vụ việc liên kết.
- `TPDBCKQTHCT_*`, `THBCTHCT_*` → `srs-fr-15-ct-htpldn.md` (1.610 dòng); `srs-fr-11-bao-cao.md` nếu vế nói
  tới biểu mẫu/xuất tệp.
- `KTDGKQHT_05` → `srs-fr-03-dao-tao.md`.

**Quan hệ khóa cứng:** `MATCH` (đặc tả nói rõ, khớp kỳ vọng phiếu) → được chấm Pass/Reopen ·
`DIFF` (đặc tả nói ngược phiếu) → **CẤM Pass**, kết luận Cần BA · `GAP` (đặc tả im lặng / tự mâu thuẫn)
→ **CẤM Pass**, Cần BA. Kết quả đo trên web **không** biến `DIFF/GAP` thành `MATCH`.
Một lệnh grep rỗng **không đủ** để kết luận đặc tả im lặng — phải đọc trọn bảng/mục liên quan,
tìm cả từ đồng nghĩa và dấu thay đổi `[STT…]` / `[CR-…]`.

## 3. Môi trường + tài khoản

- **Env đo:** `https://18.143.165.120.nip.io` (env **NỘI BỘ**, không phải env nghiệm thu
  `htpldn-uat.ospgroup.vn` của đối tác) · MailHog `http://18.143.165.120:8025`.
- **Bộ tài khoản: `_03`** (theo prompt) — `cbnv_tw_03`, `cbnv_bn_03`, `cbnv_dp_03`, `cbpd_tw_03`,
  `cbpd_bn_03`, `cbpd_dp_03`, mật khẩu `Test@1234`. Chọn vai trò theo cột `Tác nhân`/`Điều kiện` của phiếu,
  không phải theo cái nào tiện. **`admin` chỉ dùng dựng dữ liệu/điều tra, KHÔNG dùng để ra verdict.**
  Tài khoản khóa/không đăng nhập được → fallback **cùng vai trò + cùng cấp** (sang `_04`, `_05`), ghi rõ
  tài khoản thực dùng trong báo cáo. CẤM đổi vai trò/cấp.
- **Đăng nhập:** UI thật (mật khẩu → mã 6 số ở MailHog). Lấy token API để đối chứng:
  `/tmp/login.sh <username> [Test@1234]` (in ra accessToken; `idleTtl` 30 phút).
- **Bản dựng:** env này deploy liên tục. **Đo vân tay đầu VÀ cuối phiên**: bó mã `assets/index-*.js`
  + `last-modified` của `GET /`. Nhãn `V1.0.x` ở chân thanh bên **KHÔNG** phải định danh (đã có ca lùi nhãn).
  Ghi cả hai đầu vào báo cáo; hai đầu khác nhau → nói rõ quan sát nào rơi trước/sau mốc deploy.
- **Công cụ duyệt web:** Chrome DevTools MCP (`mcp__chrome-devtools__*`). Quy tắc + mẫu đăng nhập:
  `docs/htpldn-mcp-patterns.md`. 🔴 **Chỉ MỘT tác nhân dùng trình duyệt tại một thời điểm** — cả đội
  dùng chung một trình duyệt, chạy song song là giẫm chân nhau.

## 4. Kỷ luật đo (rút từ flow 04 — vi phạm là hỏng cả phiếu)

1. **Khóa chuẩn chấm TRƯỚC khi mở màn đang tranh chấp.** Mỗi vế đúng một dòng:
   `C1 · expected đối tác · SRS file:dòng (hoặc IM LẶNG/MÂU THUẪN) · MATCH/DIFF/GAP · route TEST/BA · đường đo`
   Lưu ở `chuan/<MÃ_TC>.md`. Sau khi mở màn **cấm đổi quan hệ** để khớp kết quả đo.
2. Mỗi thao tác/ảnh/phép đo phải trả lời được **"đang kiểm Cn nào?"**. Không ánh xạ được về vế → **CẤM chạy**.
3. Mỗi vế: **một đường UI ngắn nhất + một đối chứng độc lập** (đọc lại bản ghi qua API, mở tệp xuất ra đếm,
   đối chiếu DOM). Bấm lại cùng một nút **không** tính là đường thứ hai. Hai đường khớp thì DỪNG,
   không thêm đường thứ ba. **Hai phép mâu thuẫn = chưa được chốt.**
4. **Hành động đang tranh chấp phải bấm bằng UI thật.** API chỉ để dựng tiền đề + đối chứng.
5. **Dựng tiền đề tối thiểu**: ưu tiên dùng lại dữ liệu QA có sẵn; chỉ tạo phần còn thiếu. Seed = mutate môi
   trường chung ⇒ **khai vào báo cáo: đổi bản ghi nào · đổi gì · trên env nào**. Cấm đoán endpoint
   (đọc `/api/docs-json` trước), cấm ghi thẳng DB, cấm đụng dữ liệu đối tác.
6. **Tệp seed phải là fixture thật** (xlsx/docx/png đúng định dạng). Cấm đổi đuôi tệp văn bản.
7. **Chống dò mò:** script chỉ trả count/text/ID cần cho vế đang đo, không dump toàn DOM.
   Chữ người dùng nhìn thấy đọc bằng `innerText` (không `textContent` — gom node ẩn → bug ma).
   Bắt thông báo tự tắt: cài `MutationObserver` **trước** thao tác, **CẤM lọc trùng** (che double-toast).
8. **Kiểm nội dung tệp xuất, không chỉ "tệp tải về được"**: mở bằng `openpyxl`/`python-docx`/`PyMuPDF`,
   chỉ kiểm các thuộc tính mà vế Cn/đặc tả yêu cầu.
9. **Bug mới tự lộ:** chỉ ghi nhận sai lệch **trong chính màn/phản hồi/tệp đang quan sát**. Không bấm thử
   từng nút, không mở chức năng khác để săn bug. Cả phiếu chỉ được thêm **tối đa 1 phép xác nhận** cho bug
   mới. Không đủ căn cứ → ghi **candidate**, dừng điều tra.

## 5. Verdict → ghi gì lên bảng

| Verdict logic (flow 04) | Ô `Trạng thái dev fix` (R) |
|---|---|
| **Pass** | `Test done` |
| **Reopen** | `Reopen` |
| **Cần BA** | `BA confirm` |
| **Không phải lỗi** | `Test done` + ô diễn giải mở đầu bằng `❌ Không phải lỗi` |
| **Chưa chốt** | **KHÔNG ghi R.** Chỉ ghi diễn giải vào `Kết quả verify` nêu rõ blocker + cần bổ sung gì, rồi báo lại điều phối |

- Diễn giải đầy đủ → ô **`Kết quả verify` (T)**. Link ảnh Drive **đặt trong chính ô T** (như các lô trước).
- 🔴 **Ô CHỈ ĐỌC — cấm ghi đè:** `Trạng thái` (N) · `Kết quả thực tế` (L) · `TKM phản hồi lần 1` (Q) ·
  `DEV phản hồi lần 1` (S). Mỗi lượt ghi chỉ chạm **đúng 2 ô: R và T**.
- Ô R là dropdown; giá trị ghép kiểu `Reopen, BA confirm` **có thể bị ô từ chối**. Khi phiếu vừa Reopen vừa
  cần BA: ghi `Reopen` vào R và nêu rõ phần cần BA ngay trong ô T dưới đầu mục `CẦN NGHIỆP VỤ CHỐT`.
- **Verdict `Reopen`** bắt buộc kèm khối `── CÁCH VERIFY sau Dev fix ──` trong ô T (mẫu ở flow 04 §Hồ sơ tái hiện).
- **Vế `DIFF`** bắt buộc có câu: `CẦN BA CONFIRM: đối tác kỳ vọng <…>; SRS quy định <…> (file:dòng); web/dev hiện tại <…>.`
- Văn phong ô T: **tiếng Việt cho người đọc nghiệp vụ**, không thuật ngữ Anh (BLOCKED/PENDING), không đường
  dẫn tệp trên máy QA (dev không mở được → coi như không có bằng chứng). Nêu rõ **đo trên env nội bộ**,
  **bó mã bản dựng**, **tài khoản đã dùng**.

### Lệnh ghi bảng (bắt buộc dùng, có chặn ghi nhầm dòng)

```bash
cd "output/UAT_doi-tac"
python3 tools/sheet_bug_verify_write.py \
  --spreadsheet-id 1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s --sheet-title bug \
  --row <N> --id-column 'Mã TC' --id-value '<MÃ_TC>' \
  --expect 'Trạng thái dev fix=Fixed' --set 'Trạng thái dev fix=<Test done|Reopen|BA confirm>' \
  --expect-file 'Kết quả verify=<đường dẫn tệp giá trị CŨ>' \
  --set-file 'Kết quả verify=<đường dẫn tệp nội dung MỚI>' \
  --reason 'FLOW04 lo F8 - <MÃ_TC>' --dry-run
```
Chạy `--dry-run` trước, đọc kỹ old→new, rồi bỏ `--dry-run`. Script tự đọc lại sau khi ghi.
Nếu `--expect` báo lệch ⇒ **có người vừa sửa dòng đó** → đọc lại dòng, xem xét, rồi mới ghi.

### Tải ảnh bằng chứng lên Drive (link xem được)

```bash
cd "output/UAT_doi-tac"
python3 tools/drive_upload_f8.py --file <đường dẫn ảnh> --label "<mã TC + vế Cn + ảnh chứng minh điều gì>"
# hoặc nhiều ảnh: --manifest <tệp, mỗi dòng "đường-dẫn<TAB>chú thích">
```
Ảnh lưu ở `image/` của lô, đặt tên `<MÃ_TC>-<số>-<mô-tả-gạch-nối>.png`.
**Mỗi ảnh phải nêu nó chứng minh điều gì** và phải **mở lại xem** trước khi gắn link (ảnh chụp toàn trang
có thể bắt đúng lúc trang vẽ lại).

## 6. Thứ tự làm việc mỗi phiếu (tuần tự, không gộp)

1. Đọc lại dòng phiếu trên bảng (nguồn có thể đã đổi) → 2. khóa `chuan/<MÃ>.md` → 3. dựng tiền đề →
4. đo trên UI thật + đối chứng độc lập → 5. viết `do/<MÃ>.md` (nhật ký đo + số liệu + đường dẫn ảnh) →
6. tải ảnh lên Drive → 7. soạn nội dung ô T ra tệp `note/<MÃ>.txt` → 8. ghi bảng (dry-run → ghi thật) →
9. **đọc lại xác nhận** → 10. mới sang phiếu kế tiếp.

**Không dừng chờ nếu không có blocker.** Gặp blocker thật: ghi `Chưa chốt`, nêu đúng dữ kiện còn thiếu,
**bỏ qua phiếu đó và chạy tiếp phiếu sau**, báo lại ở bàn giao cuối.

## 7. Dòng bug mới ngoài phạm vi

Chỉ mở khi đủ **đặc tả + artifact + đối chứng độc lập** (xem §4.9). Quy tắc do prompt cấp:
- Mã = `<tiền tố module>_QA<số thứ tự>` (vd `QLHDTVVCG_QA01`), thêm vào **cuối** tab `bug`.
- Ô cần điền: `Mã TC` · `Tên chức năng` · `Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` ·
  `Kết quả thực tế` · `Trạng thái=Fail` · `Dopai=bug` · `Ảnh/vieo 1=<link Drive xem được>`.
- Tham khảo `tools/sheet_add_bug_row.py`. **Báo điều phối trước khi thêm dòng** (tránh 2 tác nhân cùng
  ghi vào một dòng cuối bảng).

## 8. Đầu ra của mỗi tác nhân

- `chuan/<MÃ_TC>.md` — bảng khóa chuẩn chấm (BUG SCOPE LOCK) từng vế.
- `do/<MÃ_TC>.md` — nhật ký đo: tài khoản, tiền đề (ID bản ghi), số đo, đối chứng, ảnh, kết luận từng vế.
- `note/<MÃ_TC>.txt` — đúng nội dung đã ghi vào ô `Kết quả verify`.
- `image/` — ảnh bằng chứng.
- Kết thúc phần việc: viết `BAN-GIAO-<mã lô con>.md` tóm tắt: verdict từng phiếu · đã ghi ô nào lúc mấy giờ ·
  dữ liệu đã seed/thay đổi · bug mới / candidate · phiếu Chưa chốt và cần bổ sung gì.
