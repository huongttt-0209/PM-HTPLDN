# BRIEF — Reverify round 7 (2026-07-25)

Mục đích: verify lại 8 bug dev báo đã fix (P = `dev done`, Verify = `Reopen`).
**Tất cả file đường dẫn dưới đây tính từ repo root** `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk`.

---

## 0. Bối cảnh — ĐỌC KỸ, dễ chấm sai

- Cột `DEV phản hồi lần 1` (R) của 8 dòng này **hiện đang chứa note Reopen của CHÍNH QA** viết lúc 02:00–05:00 ngày 25/07, KHÔNG phải phản hồi mới của dev. Cột `Trạng thái dev fix 2` (W) / `DEV phản hồi lần 2` (X) **trống hoàn toàn** — dev chỉ lật P về `dev done`, không viết thêm gì.
- Vì vậy **bar chấm của round này** = file `tieu-chi/<MÃ TC>.md`, gồm:
  - **(A)** bộ "CÁCH VERIFY / PASS khi / FAIL nếu" gốc dev đã chốt (trích từ snapshot round-3);
  - **(B)** các gạch đầu dòng lỗi CÒN LẠI mà QA đã ghi cho đối tác ở lượt Reopen gần nhất.
- **PASS = (A) đủ điều kiện PASS **VÀ** (B) không còn gạch đầu dòng nào tái hiện.** Còn ≥1 → Reopen.
- **CẤM tự đặt tiêu chí mới** ngoài (A)+(B). Cũng CẤM bỏ qua ⚠️ "Bẫy" trong (A) — đó là các cách chấm sai đã xảy ra thật.

---

## 1. Môi trường + tài khoản

- Web: `https://18.143.165.120.nip.io/login` (KHÔNG dùng IP thô — cổng 443 trên IP từ chối kết nối).
- MailHog (lấy OTP): `http://18.143.165.120:8025` — IP thô, KHÔNG qua nip.io.
- **Bộ tài khoản 04** (user chỉ định), mật khẩu `Test@1234`:
  - `cbnv_tw_04` — CB Nghiệp vụ Trung ương
  - `cbnv_bn_04` — CB Nghiệp vụ Bộ ngành
  - `cbpd_tw_04` — CB Phê duyệt Trung ương (chỉ khi cần duyệt để seed)
- Đã kiểm 25/07: `POST /api/v1/auth/login` body `{"username": "...", "password": "Test@1234"}` → HTTP 200 + gửi OTP. **Field là `username`/`password`**, không phải `tenDangNhap`.
- Lấy OTP:
  ```bash
  curl -s "http://18.143.165.120:8025/api/v2/messages?limit=1" | python3 -c "
  import sys,json,re; d=json.load(sys.stdin); m=d['items'][0]
  print('To:', m['To'][0]['Mailbox']+'@'+m['To'][0]['Domain']); print('OTP:', re.search(r'\b(\d{6})\b', m['Content']['Body']).group(1))"
  ```
  ⚠️ MailHog trả **email mới nhất toàn hệ thống** — luôn đối chiếu dòng `To:` khớp tài khoản đang login.
- Token TTL: 30 phút **idle** (không phải 2 phút). 1 phiên login chạy trọn 1 batch ~20 phút được.

---

## 2. Công cụ — BẮT BUỘC

### Chrome DevTools MCP là tool mặc định
- Prefix `mcp__chrome-devtools__*`. **CẤM dùng curl để RA VERDICT.** curl chỉ dùng để: seed dữ liệu, tra cứu, tải bằng chứng, điều tra nguyên nhân.
- **MCP-Rule 1:** `wait_for(text[])` trước mọi `fill`/`click`, timeout ≥10000ms.
- **MCP-Rule 2:** `take_snapshot` lấy `uid` FRESH sau mỗi navigate/mở modal/render lại. `uid` cũ = vô hiệu.
- **MCP-Rule 3:** sau khi login thì **click sidebar**, KHÔNG `navigate_page` (full reload → văng về `/login`). Trong 1 số màn có thể `navigate_page` được nếu SPA giữ token, nhưng mặc định là click.
- **MCP-Rule 4:** lần đầu mỗi phiên, click "Thu gọn menu" để mở rộng sidebar trước khi bấm submenu.
- **MCP-Rule 8:** toast sống 3–5s → phải bắt bằng MutationObserver, KHÔNG poll DOM, KHÔNG kết luận từ ảnh.
- App-side quirk: form CRUD là **Drawer** bên phải (không phải Modal); nút submit là **[Đồng ý]** (không phải [Lưu]); row action Sửa/Xóa là thẻ `<a>`; toast wrapper class là `.ant-message-notice-wrapper`.
- ⚠️ Bug app đã biết: click sidebar tới lần thứ 4 hay làm trang bất ổn. Cap ~3 điều hướng/phiên, cần thì reload `/login` làm mốc mới.

### Bộ bắt thông báo
- **CHỈ dùng** `output/UAT_doi-tac/tools/toast-capture.js`. Đọc file rồi dán nguyên khối vào `evaluate_script` **TRƯỚC** khi bấm nút cần đo.
- **CẤM tự viết observer có lọc trùng. CẤM dùng `textContent`** (gom cả node ẩn của AntD → bug ma).
- Trước khi tin số liệu: `soObserverDangSong` PHẢI = 1. Khác 1 → số liệu VÔ HIỆU, cài lại.
- Luôn báo cả **SO_REQUEST** lẫn **SO_KHUNG_THONG_BAO** (phân biệt "gửi 2 lần" vs "1 lần hiện 2 khung").

### File mẫu (fixtures) — đã có sẵn, KHÔNG cần tạo lại
Thư mục: `output/UAT_doi-tac/reverify-week-3/reverify-audit/_scratch/testfiles/`
| File | Dùng cho |
|---|---|
| `eicar.docx` (68 B) | EICAR thô đổi đuôi — QLBMHD_08 bước 1 |
| `valid-eicar.docx` (1028 B) | .docx đúng cấu trúc Office, EICAR nằm trong `word/document.xml` — **phép thử quyết định** QLBMHD_08 |
| `qa-ok-1.docx`, `qa-ok-2.docx` (922 B) | 2 tệp hợp lệ — IBMHD_07 |
| `qa-loi.txt` (48 B) | sai định dạng — IBMHD_07 |
| `qa-hong.docx` (3010 B) | đúng đuôi, nội dung hỏng (header `NOT-A-ZIP-…`) — IBMHD_07 |
| `qa-edit-src.docx` (931 B) | tệp nguồn cho biểu mẫu cần sửa — QLBMHD_13 |
Upload qua `mcp__chrome-devtools__upload_file` với đường dẫn **tuyệt đối**.

---

## 3. Quy trình MỖI CASE (làm trọn 1 case rồi mới sang case sau — CẤM gom cuối lô)

1. Đọc `tieu-chi/<MÃ TC>.md` — nắm (A) và (B).
2. **Dựng tiền đề trước.** Thiếu data/state/thư mục → **tự seed** rồi mới test. Thiếu tiền đề *tạo được* mà không tạo = **CẤM ra verdict** (kể cả để trống). Seed cũng phải chụp màn hình và **đọc lại ảnh**.
3. Verify trên UI thật, đo bằng con số cụ thể (nguyên văn chuỗi thông báo, mã HTTP, số bản ghi, class/màu chữ của element).
4. **Chụp màn hình ở MỌI thao tác đổi trạng thái, kể cả bước seed — và PHẢI mở ảnh ra đọc** bằng tool Read. Lưu mà không đọc = vô nghĩa.
5. Chốt verdict theo mục 4 dưới → ghi sheet NGAY (mục 5) → ghi đo đạc vào `measurements.md`.
6. Tự hỏi: **"ngoài tiêu chí ra, có thấy gì bất thường không?"** Dựa trên ảnh đã đọc, không suy đoán. Có → ghi vào `phat-hien-them.md` và báo lại trong report cuối (đừng tự mở dòng TC mới).

---

## 4. Chốt verdict

| Kết quả đo | Ghi sheet |
|---|---|
| (A) PASS **và** (B) sạch | `Verify = Pass` — **chỉ đụng cột Verify**, không đổi P/R |
| Còn ≥1 điều kiện (A) trượt, hoặc ≥1 gạch (B) tái hiện | `Trạng thái dev fix 1 = Reopen` + `Verify = Reopen` + **ghi đè cột R** bằng mô tả lỗi ĐANG THẤY |

**Quyết định đã chốt với user cho `QLBMHD_08`:** phần "bộ quét chạy TRƯỚC khi ghi tệp vào kho" là chi tiết triển khai nội bộ, hộp đen không quan sát được → **KHÔNG dùng nó để giữ Reopen**. Chấm trên phần quan sát được: `valid-eicar.docx` bị TỪ CHỐI + thông báo đúng nội dung ERR-BM-07 ("Tệp chứa mã độc, không thể lưu trữ") + KHÔNG tạo được bản ghi. Đạt cả 3 → **Pass**.

**Nguyên tắc chống bác nhầm:**
- Verdict phải dựa trên **điều kiện của đối tác** (vai trò / state / dữ liệu tiền đề), không phải điều kiện mình tiện tái hiện.
- Bug candidate ≠ bug: đo lại bằng **phương pháp thứ hai** trước khi kết luận Reopen (UI fail → curl API cùng thao tác; API fail → reload UI test lại). 2 phương pháp mâu thuẫn → ghi cả 2, chưa được chốt.
- Không kết luận từ ảnh thu nhỏ; đọc full-res.

---

## 5. Ghi sheet — CHỈ bằng script, CẤM ghi tay

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk/output/UAT_doi-tac/tools"

# Hết lỗi:
python3 sheet_verify_write.py --row <N> --ma-tc <MÃ_TC> --pass

# Còn lỗi:
python3 sheet_verify_write.py --row <N> --ma-tc <MÃ_TC> --reopen --note "..."
```
- Chạy `--dry-run` trước để xem old → new, rồi chạy thật.
- Script tự guard spreadsheet/tab/header/mã TC + đọc lại xác nhận. Script báo lỗi → **DỪNG, báo lại**, tuyệt đối không sửa sheet bằng cách khác.

### Cách viết note Reopen (cột R) — đối tác đọc, không phải dev
- Tiếng Việt **có dấu**, mỗi ý 1 gạch đầu dòng (`\n- `). Ngắn gọn, cụ thể.
- **PHẢI nêu:** lỗi đang thấy là gì (nguyên văn chuỗi / số liệu thật), ở màn nào, trên bản ghi nào.
- **Ghi rõ phần ĐÃ ĐẠT trước, phần CÒN LỖI sau** — dev cần biết đã sửa đúng chỗ nào.
- Kết thúc bằng: `- Kiểm tra ngày 25/07/2026, tài khoản <vai trò tiếng Việt>.`
- **CẤM:** viết không dấu · nhét chi tiết nội bộ (video đối tác, so sánh 2 môi trường, mã màn MH-xx) · jargon (API 200, field snake_case, CRUD, BLOCKED/PENDING) · câu đệm rỗng kiểu "hệ thống hoạt động bình thường" mà không kèm bằng chứng.
- Note là **ghi đè**, không phải nối thêm lịch sử. Chỉ mô tả trạng thái HIỆN TẠI.

---

## 6. Nơi lưu bằng chứng

```
output/UAT_doi-tac/reverify-week-3/dev-fix-reverify-round-7-2026-07-25/
├── BRIEF.md              ← file này
├── tieu-chi/<MÃ TC>.md   ← bar chấm
├── <MÃ TC>/image/*.png   ← screenshot mỗi case (đặt tên có nghĩa, tiếng Việt không dấu)
├── measurements.md       ← số liệu đo, mỗi case 1 mục (append)
└── phat-hien-them.md     ← bất thường ngoài tiêu chí (nếu có)
```
- `take_screenshot({filePath})` phải trỏ **đường dẫn tuyệt đối** vào đúng `<MÃ TC>/image/`.
- Tên ảnh phải khớp nội dung pixel. Ảnh tên "toast-loi.png" mà pixel là form trống = INVALID.

---

## 7. Báo cáo cuối cho orchestrator

Với mỗi case, trả về đúng các trường:
`Mã TC | dòng | verdict (Pass/Reopen) | 2–4 số liệu quyết định | đường dẫn ảnh | đã ghi sheet lúc mấy giờ | phát hiện thêm (nếu có)`
