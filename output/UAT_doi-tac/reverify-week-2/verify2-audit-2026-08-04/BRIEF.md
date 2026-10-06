# BRIEF — Vòng soát lại 2 (Verify 2) cho 24 case tuần 2

**Ngày:** 2026-08-04 · **Tab sheet:** `UAT_TGPL Doanh Nghiệp-tuần 2` · **Mode ghi:** `reverify2` (cột X = `Verify 2`)

---

## 0. Bản chất công việc — đọc kỹ, đây là chỗ dễ làm sai nhất

24 case này **đã được QA chấm `Pass` ở vòng trước** (03/08 20:18 → 04/08 01:31, ~15 phút/case).
Việc của bạn **KHÔNG phải** xác nhận lại kết luận cũ cho nhanh. Việc của bạn là **soát lại một cách đối kháng**:

> Giả định mặc định: **kết luận `Pass` trước đó có thể SAI**. Nhiệm vụ của bạn là cố gắng **BÁC BỎ** nó.
> Chỉ khi cố bác mà không bác nổi (đã chạy trọn luồng, đúng vai trò/state/data của bug gốc) mới được ghi `Pass`.

- 🔴 **CẤM Pass bằng quan sát tĩnh.** "Nhìn thấy cột đã có rồi", "UI trông đúng" → KHÔNG đủ. Phải chạy hết
  luồng tới đúng bước sinh ra lỗi cũ.
- 🔴 **CẤM Pass khi chưa dựng lại được tiền đề.** Thiếu data/state/tài khoản mà tiền đề *tạo được* →
  phải seed / chuyển state / tạo account rồi test lại. Pass ở đây là **Pass oan**.
- 🔴 **Bug gốc gộp nhiều ý → mọi ý phải hết lỗi mới `Pass`.** Còn ≥1 ý lỗi → **`Reopen`**. Fix một phần = `Reopen`.
- 🔴 **Fix đẻ ra bug mới cùng luồng → `Reopen`.**
- Bug về **trường lưu trong DB** (tên file, snapshot, mã sinh): bản ghi cũ tạo trước lúc fix vẫn hỏng là bình thường
  → phép thử quyết định là **tạo bản ghi MỚI** qua luồng chuẩn.
- Nếu bạn kết luận `Pass` cho một case, trong báo cáo phải nêu rõ **"đã cố bác bằng cách nào mà không bác được"**.

---

## 1. Đọc BẮT BUỘC trước case đầu tiên

| File | Vì sao |
|---|---|
| `output/UAT_doi-tac/QA_VERIFY_PROTOCOL.md` | Luật gốc: 3 CỔNG · Quy tắc VÀNG + bảng đối chiếu điều kiện · GATE bằng chứng real-data · cách viết note |
| `output/UAT_doi-tac/QA_REVERIFY_PROTOCOL.md` | Luật riêng của bước re-verify: verdict chỉ `Pass` / `Reopen` / ô TRỐNG |
| `output/UAT_doi-tac/QA_POSTMORTEM_bo-sot-bug-2026-07-16.md` | Vì sao QA từng chạy 16 case mà không thấy lỗi hiện ngay trên màn |
| `CLAUDE.md` (gốc repo) | Chrome DevTools MCP Rule 1–8 · selector library · Rule 7 account lock · Rule 9 phân loại lỗi |
| `output/UAT_doi-tac/tools/toast-capture.js` | Bộ bắt thông báo **DUY NHẤT** được dùng |
| `output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/HO-SO-24-CASE.md` | Nội dung bug gốc từng case (phần của bạn) |

**SRS — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
(`srs-fr-01-dashboard.md` … `srs-fr-16-api.md`). **CẤM** quote số dòng từ `input/srs-update-2026-5-5/`.

---

## 2. Môi trường + tài khoản

- **Web:** `https://htpldn-uat.ospgroup.vn/login` (pre-flight 200 lúc 2026-08-04). Đây là env dev vừa build bản vá lên.
- **MailHog:** `https://htpldn-uat.ospgroup.vn/mailhog/` (200).
- **Mật khẩu tài khoản nghiệp vụ: `Test@1234`** (KHÔNG phải `Secret@123` — cái đó chỉ của `admin`).
- Tài khoản: `cbnv_tw` · `cbnv_bn` · `cbnv_dp` · `cbpd_tw` · `cbpd_bn` · `cbpd_dp`.
  Danh sách đầy đủ + tài khoản dự phòng `_01`.._05` + các account đã biết lỗi: `output/UAT_doi-tac/input/input.md`.
  ⚠️ Đã biết `cbpd_tw` và `cbnv_dp` login FAIL với `Test@1234` → fallback `cbpd_tw_01` / `cbnv_dp_01` (Rule 7: chỉ fallback
  CÙNG vai trò + CÙNG cấp).
- **Ghi rõ account thực dùng** trong mọi báo cáo + bảng điều kiện.
- Login: dùng Chrome DevTools MCP theo Template login trong `CLAUDE.md`. OTP lấy từ MailHog.

---

## 3. Vòng lặp MỖI CASE — làm TRỌN 1 case rồi mới sang case sau. CẤM gom lô.

1. **Đọc bug gốc** trong `HO-SO-24-CASE.md` (mục `## row N — <Mã TC>`), phần `DEV phản hồi lần 1` chính là
   mô tả bug gốc / lý do Pass vòng 1. Nếu có bảng điều kiện cũ ở
   `reverify-week-2/verify1-conlai-2026-08-03/cond/<Mã TC>.md` thì đọc để biết tiền đề.
2. **Chạy LẠI ĐỦ LUỒNG trên web** qua Chrome DevTools MCP, đúng vai trò / state / data của bug gốc.
   - Bắt thông báo **chỉ bằng** `tools/toast-capture.js`. CẤM tự viết observer có lọc trùng, CẤM `textContent`.
   - Luôn **đếm số request kèm số thông báo** (`list_network_requests`).
   - Chụp màn hình ở **mọi thao tác đổi trạng thái** — và **mở ảnh ra đọc**, lưu mà không đọc = vô nghĩa.
   - Ảnh lưu vào `output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/evidence/`
     đặt tên `<Mã TC>-v2-<mô-tả-ngắn>.png`. **CẤM** tên file chứa chữ `partner` (script sẽ chặn).
3. **Điền bảng đối chiếu điều kiện** `reverify-week-2/verify2-audit-2026-08-04/cond/<Mã TC>.md`.
   Cột giữa = điều kiện của **BUG GỐC**, cột phải = điều kiện **bạn thực tế test**. Format 4 cột:
   `| Điều kiện có thể đổi kết quả | Điều kiện bug gốc | Mình test | GAP? |`, cột GAP ghi `Không`.
   **Còn 1 ô GAP = chưa verify xong, CẤM mọi verdict.**
   Bug **TĨNH** (thiếu cột cố định / nhãn / icon / màu — không phụ thuộc vai trò, state, data) thì
   miễn bảng, dùng `--static-bug "<lý do ≥10 ký tự>"` thay cho `--condition-table`.
4. **Chốt verdict** → **ghi sheet NGAY** (lệnh ở §4) → **ghi 1 dòng vào `PROGRESS.md`** → sang case kế.
5. Tự hỏi: *"ngoài bug này, có thấy gì bất thường không?"* — dựa trên ảnh đã đọc, không suy đoán.
   Có → log dòng TC mới bằng `tools/sheet_add_bug_row.py`. Không → ghi rõ "không phát hiện thêm".

---

## 4. Ghi sheet — BẮT BUỘC dùng script, CẤM ghi tay

Chạy từ thư mục gốc repo `/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk`.

**Pass** (chỉ ghi 1 ô `Verify 2` = `Pass`, không đụng cột nào khác):

```bash
UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 2" python3 output/UAT_doi-tac/tools/sheet_write.py \
  --mode reverify2 --row <N> --ma-tc <Mã TC> --status Pass \
  --evidence "output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/evidence/<ảnh thao tác THÀNH CÔNG>.png" \
  --condition-table "output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/cond/<Mã TC>.md" \
  --vong2-do-dev-build "Vong 2 do DEV build ban va len UAT moi (htpldn-uat.ospgroup.vn) roi nho QA soat lai, khong phai doi tac phan anh lan 2" \
  --dry-run
```
→ xem output dry-run, đúng thì **bỏ `--dry-run`** chạy lại để ghi thật.

**Reopen** (ghi 3 ô: `Trạng thái dev fix 2` = Reopen · `Verify 2` = Reopen · `DEV phản hồi lần 2` = note mới):

```bash
UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 2" python3 output/UAT_doi-tac/tools/sheet_write.py \
  --mode reverify2 --row <N> --ma-tc <Mã TC> --status Reopen \
  --evidence "<ảnh/log bắt thao tác LỖI>" \
  --condition-table "<cond/<Mã TC>.md>" \
  --note-file "output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/notes/<Mã TC>.txt" \
  --vong2-do-dev-build "..." --dry-run
```

**Ô TRỐNG** (chỉ khi blocker **khách quan** env/BE/DB/tích hợp): `--status "" --blocker-category <B|C|D|E>`.
Nhóm **A (thiếu seed) bị CẤM** — thiếu data thì phải seed. Nhóm **F phải hỏi user trước**.

**Note partner-facing** (chỉ cần khi `Reopen`): tiếng Việt **có dấu**, gạch đầu dòng, mở đầu bằng
`✅ Vẫn còn lỗi — chưa đạt.` rồi nêu: đã kiểm bằng vai trò/tài khoản nào, bản dựng nào, phần nào đã hết lỗi,
phần nào còn lỗi + bằng chứng đo được. CẤM jargon (API 200, snake_case, mã FR/BR/số dòng SRS) trong note gửi đối tác.

**🔴 Script báo lỗi / chặn → DỪNG, báo lại. CẤM ghi tay, CẤM viết script ad-hoc để lách guard.**

---

## 5. Sau mỗi case — ghi PROGRESS.md

Append đúng 1 dòng vào `output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/PROGRESS.md`:

```
| <Mã TC> | row <N> | <Pass|Reopen|TRỐNG> | <account> | <≤20 từ: cố bác bằng cách nào / còn lỗi gì> | <path ảnh> |
```

---

## 6. Báo cáo cuối (trả về cho orchestrator)

Với **mỗi** case, 1 khối ngắn:
- Mã TC + row + verdict cuối + đã ghi sheet chưa (`ghi thật` / `chỉ dry-run vì ...`)
- 1–2 câu: đã cố bác bằng cách nào; nếu `Reopen` thì còn lỗi gì, đo được bằng gì
- Account + đường dẫn ảnh bằng chứng
- Bất thường phát hiện thêm (nếu có) + đã log dòng TC mới chưa
