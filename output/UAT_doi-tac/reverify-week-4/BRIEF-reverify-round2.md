# BRIEF — Re-verify vòng 2 sau khi dev fix (tuần 4)

> Mọi agent module ĐỌC FILE NÀY TRƯỚC khi làm. Đọc xong mới mở bug entry của mình.

## Bối cảnh

Dev báo đã fix các bug tuần 4 (cột `Trạng thái dev fix 1` = `dev done` trên sheet).
Nhiệm vụ: **re-verify LIVE từng bug**, rồi cập nhật CẢ file `.md` VÀ Google Sheet.

- **Env:** https://18.143.165.120.nip.io/login — tài khoản ở `output/UAT_doi-tac/input/input.md`
  (nghiệp vụ: `Test@1234`; admin `admin` / `Secret@123`). MailHog: http://18.143.165.120:8025/
- **File bug:** `output/UAT_doi-tac/reverify-week-4/bug-reports/bug-report-UAT-tuan-4.md`
- **Ảnh:** `output/UAT_doi-tac/reverify-week-4/bug-reports/image/`
- **Sheet tab:** `UAT_TGPL Doanh Nghiệp-tuần 4`
- **SRS chuẩn:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`

## 🔴 Luật cứng

1. **CẤM Pass bằng quan sát tĩnh.** Không được kết luận "thấy field đã có / UI trông đúng rồi".
   Phải **chạy lại ĐỦ luồng** của bug gốc, đúng vai trò + state + data như phần "Các bước tái hiện".
   Fix thêm UI mà BE vẫn hỏng là chuyện thường.
2. **Verify qua Chrome DevTools MCP** (`mcp__chrome-devtools__*`). **KHÔNG verify bằng API.**
   API/curl chỉ được dùng để *seed dữ liệu tiền đề* hoặc *điều tra thêm*, không dùng ra verdict.
3. **Thiếu tiền đề thì TỰ TẠO** (seed record, chuyển state, tạo tài khoản) — không phải blocker.
4. **Làm TRỌN 1 bug rồi mới sang bug sau.** Xong 1 bug: ghi `.md` → ghi sheet → mới verify bug kế.
   CẤM gom cuối lô.
5. **Chụp màn hình mọi thao tác đổi trạng thái và PHẢI mở ảnh ra đọc.** Lưu mà không đọc = vô nghĩa.
6. **Bắt toast** bằng `output/UAT_doi-tac/tools/toast-capture.js` (MutationObserver, CẤM lọc trùng,
   CẤM `textContent`). Luôn đếm **số request kèm số thông báo**.
7. **Bug tình cờ phát hiện ngoài phạm vi cũng phải báo** — ghi vào báo cáo cuối của agent, nêu rõ
   "bug mới, chưa log", KHÔNG tự mở dòng sheet mới (chủ đợt quyết).

## Verdict

| Verdict | Khi nào |
|---|---|
| **Pass** | Chạy hết luồng, kết quả khớp mục **"Kết quả mong đợi"** trong bug entry |
| **Reopen** | (a) vẫn tái hiện lỗi · (b) fix **một phần** · (c) fix đẻ ra bug mới **cùng luồng** |

Bug entry có nhiều ý con → chỉ `Pass` khi **mọi ý** đều đạt; còn ≥1 ý hỏng = `Reopen`.

## Cập nhật file .md — dùng script, KHÔNG sửa tay

```bash
cd "<repo>/output/UAT_doi-tac"
python3 tools/bugmd_set_status.py \
  --file reverify-week-4/bug-reports/bug-report-UAT-tuan-4.md \
  --bug BUG-XXX --verdict pass|reopen --round R2 \
  --note "1-2 câu: pass = vì sao đã đạt; reopen = triệu chứng đang thấy" [--dry-run]
```

Script tự làm nguyên tử 5 việc: đổi heading `~~BUG-X~~ [CLOSED]` · **OVERWRITE đúng 1 dòng Re-test**
(không append) · đổi Status trong Bug Summary Table · tính lại cột Closed/Open của Severity breakdown ·
bump `**Ngày**` ở header. Chạy `--dry-run` xem trước rồi mới chạy thật.

**Nếu Reopen và cần mô tả lại triệu chứng cho chính xác:** sau khi chạy script, được phép Edit thêm
phần **"Kết quả thực tế"** của bug entry đó để tả đúng lỗi ĐANG thấy (ghi rõ `(đo lại DD/MM/YYYY)`).
Đừng xoá mô tả cũ nếu nó vẫn đúng — chỉ bổ sung/hiệu chỉnh.

**Ảnh mới:** lưu vào `reverify-week-4/bug-reports/image/`, đặt tên `R2-<BUG-ID>-<mô-tả>.png`,
rồi chèn link tương đối `![...](image/R2-....png)` vào mục **Bằng chứng** của bug entry.
CẤM base64, CẤM để ảnh ngoài thư mục `image/`.

## Ghi Google Sheet

```bash
cd "<repo>/output/UAT_doi-tac/tools"

# Pass — CHỈ ghi cột Verify, không đụng cột nào khác
UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 4" python3 sheet_verify_write.py \
  --row <N> --ma-tc <MÃ_TC> --pass

# Reopen — ghi 3 ô: Trạng thái dev fix 1 = Reopen, Verify = Reopen, DEV phản hồi lần 1 = note
UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 4" python3 sheet_verify_write.py \
  --row <N> --ma-tc <MÃ_TC> --reopen --note-file /tmp/note.txt
```

Script tự guard: khớp `Mã TC` với `--row`, in old→new, đọc lại xác nhận. Lệch → nó tự DỪNG.
**Chạy `--dry-run` trước.** Script fail → DỪNG, báo lại, **KHÔNG ghi tay**.

### Note cột "DEV phản hồi lần 1" — chỉ khi Reopen. ĐỐI TÁC ĐỌC.

- Tiếng Việt **có dấu**, **gạch đầu dòng** (`- `), mỗi ý 1 dòng.
- Tả **triệu chứng ĐANG THẤY lần re-verify này**, cụ thể: thấy gì trên màn nào, thao tác nào,
  thông báo gì. Nêu rõ nếu chỉ fix được một phần (phần nào đạt / phần nào chưa).
- **CẤM lộ chi tiết nội bộ:** video/ảnh đối tác quay, so sánh 2 môi trường, mã màn `SCR/MH-xx`,
  jargon kỹ thuật (API 200, tên field snake_case, tên endpoint, CRUD), lịch sử BA chốt.
- Được giữ tham chiếu SRS dạng `FR-xx (UCxx) dòng N` vì dev/BA đọc — nhưng đừng dán nguyên khối.

Mẫu:

```
- Đã kiểm tra lại trên bản mới: màn Kho câu hỏi vẫn chưa có cột "Câu trả lời".
- Cột điểm vẫn mang nhãn "Đánh giá", chưa đổi thành "Điểm TB" theo đặc tả.
- Đã thử với cả vai trò CB Nghiệp vụ và CB Phê duyệt, kết quả như nhau.
```

## Báo cáo cuối của agent (trả về cho chủ đợt)

Mỗi bug 1 khối ngắn:

```
BUG-XXX (Mã TC ..., row ...) — Pass | Reopen
  Đã chạy   : <luồng thật đã chạy, vai trò, record/ID cụ thể>
  Quan sát  : <kết quả đo — số bản ghi / toast / cột / state>
  Bằng chứng: <đường dẫn ảnh đã lưu VÀ ĐÃ MỞ ĐỌC>
  .md       : đã cập nhật ✔   Sheet: row N đã ghi ✔
```

Cuối cùng thêm mục **"Bất thường ngoài phạm vi"** — có thì liệt kê, không có thì ghi rõ
"không phát hiện thêm".

## Mẹo MCP cho app này

- `wait_for(text[])` trước mọi `fill`/`click`; app render chậm → timeout ≥10000ms.
- `take_snapshot` lấy `uid` **fresh** sau mỗi navigate/modal/render.
- Sau khi đăng nhập: **click sidebar**, KHÔNG `navigate_page` (full reload → văng `/login`).
- Sidebar thu gọn → click "Thu gọn menu" để mở rộng trước khi bấm submenu lần đầu.
- Đăng xuất để đổi vai trò: `fetch('/api/v1/auth/logout',{method:'POST',credentials:'include'})`
  + xoá localStorage/sessionStorage → rồi `navigate_page` tới `/login`.
- Selector hay dùng: `input[placeholder="Nhập tên đăng nhập"]` · `input[placeholder="Nhập mật khẩu"]` ·
  OTP `input[inputmode="numeric"][maxlength="1"]` · bảng `.ant-table-tbody tr.ant-table-row` ·
  nút submit drawer là **[Đồng ý]** hoặc **[Lưu]** · toast wrapper `.ant-message-notice-wrapper`.
- Trình duyệt là **tài nguyên dùng chung** — chỉ 1 agent chạy tại một thời điểm. Xong việc thì để
  nguyên trạng, đừng đóng hết tab.
