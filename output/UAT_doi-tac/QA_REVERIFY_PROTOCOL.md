# QA Reverify Protocol — Verify lại bug dev đã fix (BƯỚC 3)

> **Luật chung ở [QA_VERIFY_PROTOCOL.md](QA_VERIFY_PROTOCOL.md)** — 3 CỔNG, GATE bằng chứng real-data,
> Nguyên tắc 1–5, cách viết note partner-facing. File này CHỈ ghi phần **khác biệt của bước 3**.
> Mâu thuẫn giữa 2 file → **QA_VERIFY_PROTOCOL.md thắng**.
>
> **Khác biệt cốt lõi:** vòng 1 hỏi *"có phải bug không?"* · bước 3 hỏi *"dev fix rồi, lỗi còn không?"*
> → verdict chỉ có **Pass / Reopen / ô TRỐNG**.
> **KHÔNG dùng `Resolved` ở bước này.** `Resolved` là của vòng 1 (chưa ai fix mà không tái hiện).
> Ở đây dev đã fix — không tái hiện nữa nghĩa là fix có tác dụng → **Pass**.

---

## THAM SỐ ĐỢT — prompt phải cấp đủ, thiếu → DỪNG hỏi user

| Tham số | Ví dụ |
|---|---|
| Link sheet + **tên tab** | link + `UAT_TGPL Doanh Nghiệp-tuần 3` |
| Module / luồng | `Chi trả` |
| File bug-report gộp | `reverify-week-3/bug-reports/chi-tra/bug-report-UAT-tuan-3-chi-tra.md` |
| Bộ tài khoản | `01` — tra `input/input.md` |
| Phạm vi *(tuỳ chọn)* | danh sách Mã TC. Không có → lấy toàn bộ theo BƯỚC 0 |

**Guard tab (bắt buộc):** prompt có cả link `gid=...` lẫn tên tab bằng chữ → **resolve gid ra tên tab
rồi so sánh**; lệch → DỪNG hỏi user. Mọi lệnh truyền tab qua env `UAT_TAB="<tên tab>"`.

**Định vị cột bằng TÊN HEADER** — `Mã TC` · `Trạng thái dev fix 1` · `Verify` · `DEV phản hồi lần 1`.
CẤM dùng chữ cái cột: thứ tự cột đổi được, script đã dò theo tên.

---

## BƯỚC 0 — Kiểm tra giả định (chạy 1 lần, TRƯỚC case đầu tiên)

```bash
UAT_TAB="<tên tab>" python3 output/UAT_doi-tac/tools/sheet_read.py
```

1. Từ output, lấy các dòng có `Trạng thái dev fix 1` = **dev done** **VÀ** `Verify` **còn trống**
   → in **số dòng + danh sách Mã TC**.
2. Đối chiếu với số bug **Open/Reopen** trong Bug Summary Table của file bug-report.
3. **Lệch → DỪNG, báo user.** Khớp → mới chạy verify.

Đây là gate quan trọng nhất của bước 3: sai phạm vi ở đây thì mọi verdict phía sau đều sai chỗ.

---

## Vòng lặp MỖI CASE — làm TRỌN 1 case rồi mới sang case sau

**CẤM gom lô.** Xong 1 bug → ghi sheet + cập nhật file md → rồi mới sang bug kế.

1. **Đọc bug gốc** trong file bug-report: Bước tái hiện · KQ mong đợi · vai trò · state · data tiền đề.
2. **Chạy LẠI ĐỦ LUỒNG trên web** qua Chrome DevTools MCP, **đúng vai trò/state/data như bug gốc**.
   - 🔴 **CẤM Pass bằng quan sát tĩnh** ("thấy field đã có rồi", "UI trông đúng"). Fix thêm UI mà BE
     vẫn hỏng là chuyện thường — phải chạy hết luồng, đến bước sinh ra lỗi cũ.
   - Bắt thông báo **chỉ bằng** `tools/toast-capture.js` (cấm tự viết observer có lọc trùng).
   - Chụp màn hình ở **mọi thao tác đổi trạng thái** và **mở ảnh ra đọc**.
3. **Điền bảng đối chiếu điều kiện** `cond/<Mã TC>.md` — cột giữa là **điều kiện của BUG GỐC**
   (không phải của đối tác như vòng 1). Còn 1 ô GAP = chưa verify xong, CẤM mọi verdict.
4. **Chốt verdict** (bảng dưới) → **ghi sheet** → **cập nhật file md** → báo user 1 dòng → case kế.
5. Trả lời: *"ngoài bug này, có thấy gì bất thường không?"* — dựa trên ảnh đã đọc. Có → log thêm
   dòng TC mới bằng `tools/sheet_add_bug_row.py`. Không → ghi rõ "không phát hiện thêm".

---

## Verdict

| Verdict | Khi nào | Ghi cột nào |
|---|---|---|
| **Pass** | Khớp "KQ mong đợi" trong bug entry, chạy đủ luồng | chỉ `Verify` = `Pass`. **KHÔNG đụng** `Trạng thái dev fix 1`, **KHÔNG đụng** note |
| **Reopen** | Vẫn tái hiện · fix **một phần** · fix đẻ ra **bug mới cùng luồng** | `Trạng thái dev fix 1` = `Reopen` · `Verify` = `Reopen` · `DEV phản hồi lần 1` = **đè** note mới |
| **ô TRỐNG** | Blocker **khách quan** (env/BE/DB/tích hợp hỏng) | chỉ note. Bắt buộc `--blocker-category B–F` |

**Ca biên bắt buộc nhớ:**

- **Không tái hiện được vì chưa dựng lại được tiền đề (thiếu data/state/tài khoản) → KHÔNG được Pass.**
  Tiền đề *tạo được* thì phải seed / chuyển state / tạo account rồi test lại (QA_VERIFY_PROTOCOL §Nguyên tắc 4).
  Pass ở đây là Pass oan.
- **Fix một phần = Reopen**, không phải Pass kèm ghi chú.
- Bug gốc gộp nhiều ý → mọi ý phải hết lỗi mới Pass; còn ≥1 ý lỗi → **Reopen**.
- Bug về **trường lưu trong DB** (tên file, snapshot): record cũ tạo trước lúc fix vẫn hỏng là bình thường
  → phép thử quyết định là **tạo record MỚI** qua luồng chuẩn, đừng Reopen theo record cũ.

---

## Ghi sheet — bắt buộc dùng script, CẤM ghi tay

```bash
# xem trước
UAT_TAB="<tên tab>" python3 output/UAT_doi-tac/tools/sheet_write.py --mode reverify \
    --row <N> --ma-tc <Mã TC> --status Pass \
    --evidence <ảnh bắt thao tác THÀNH CÔNG> --condition-table cond/<Mã TC>.md --dry-run

# ghi thật: bỏ --dry-run
```

| Tình huống | Cờ thêm |
|---|---|
| **Reopen** | `--status Reopen --note-file <file note>` (evidence phải bắt thao tác **LỖI**) |
| **Pass** mà vòng trước QA đã ghi Reopen | `--pass-ghi-de-note --note-file <file>` — nếu không, note cũ còn nội dung Reopen, mâu thuẫn với `Verify=Pass` |
| **ô TRỐNG** | `--status "" --blocker-category <B–F>` · nhóm **A (thiếu seed) bị cấm** · nhóm **F phải hỏi user trước** rồi thêm `--user-approved` |
| Bug **tĩnh** (label/icon/màu) | `--static-bug "<lý do>"` thay cho `--condition-table` |

Script tự guard: khớp `Mã TC`, kiểm giá trị có trong dropdown, in old→new, đọc lại sau ghi,
log giá trị cũ vào `tools/sheet_write.log` (khôi phục được nếu ghi nhầm).

**🔴 Script báo lỗi/chặn → DỪNG, báo user. CẤM ghi tay, CẤM viết script ad-hoc để lách.**
Hai lỗi đã biết trước, gặp thì báo chứ đừng tự xử:
- Giá trị không nằm trong dropdown của dòng đó (vd sheet dùng `Reopent` chứ không phải `Reopen`).
- Dropdown cột `Trạng thái dev fix 1` ở dòng dev vừa đụng là từ vựng của dev, có thể không chứa `Reopen`.

---

## Cập nhật file bug-report (ngay sau khi ghi sheet, cùng case)

```bash
python3 output/UAT_doi-tac/tools/bugmd_set_status.py \
    --file <bug-report.md> --bug BUG-<Mã TC> --verdict pass|reopen \
    --round R<N> --note "<1–2 câu>" --dry-run
```

Script sửa nguyên tử 4 chỗ (heading `~~BUG-X~~ [CLOSED]` · dòng Re-test · Bug Summary Table ·
Severity breakdown) + bump `**Ngày**` ở header. **Mỗi bug giữ đúng 1 dòng Re-test — OVERWRITE, không append.**

Khi **mọi** bug trong file đã Closed → đổi tên `bug-report-<slug>.md` → `Pass-bug-report-<slug>.md`
**và cập nhật mọi link trỏ tới nó** (quy tắc đầy đủ: `CLAUDE.md` §Bug-report folder discipline).

---

## Note cột `DEV phản hồi lần 1` — CHỈ khi Reopen, người đọc là ĐỐI TÁC

- Tiếng Việt **có dấu**, **gạch đầu dòng**, tả **triệu chứng đang thấy lần này** (không phải lỗi cũ).
- **CẤM lộ chi tiết nội bộ:** video đối tác quay, so sánh 2 môi trường, mã màn `MH-xx`/`SCR-xx`,
  jargon (API 200, snake_case, CRUD), lịch sử BA chốt.
- Pass thì **không viết note** (giữ nguyên phản hồi của dev) — trừ ca `--pass-ghi-de-note` ở trên.
