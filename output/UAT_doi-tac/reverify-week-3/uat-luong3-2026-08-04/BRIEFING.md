# BRIEFING — Re-verify vòng 2 trên môi trường UAT mới (04/08/2026)

**Bạn là QA verify lại bug đã được đánh Pass ở vòng 1, nay dev build lên môi trường UAT MỚI.**
Câu hỏi cần trả lời cho mỗi case: *"Trên bản dựng mới này, lỗi gốc mà đối tác phản ánh còn không?"*

---

## 0. Thông số môi trường (đã kiểm 04/08/2026 12:5x)

| Mục | Giá trị |
|---|---|
| Web | `https://htpldn-uat.ospgroup.vn/login` |
| Bản dựng đang phục vụ | `assets/index-DpIXRGaI.js` · last-modified `2026-08-04 04:27:22 GMT` (11:27 giờ VN) |
| MailHog | `https://htpldn-uat.ospgroup.vn/mailhog/` — API `.../mailhog/api/v2/messages?limit=N` |
| OTP | **`666666`** (mã cố định, đã verify qua API). Thư OTP KHÔNG về MailHog — đừng chờ, cứ gõ 666666 |
| Mật khẩu tài khoản nghiệp vụ | `Test@1234` · admin: `Secret@123` |

Tài khoản: `cbnv_tw` `cbnv_bn` `cbnv_dp` `cbpd_tw` `cbpd_bn` `cbpd_dp` (+ hậu tố `_01`.._04 cho tài khoản anh em cùng vai trò).
**Nếu login fail:** curl `POST /api/v1/auth/login` xem `error.code`. `ERR-AUTH-LOGIN-01` = sai creds → fallback sang tài khoản anh em **CÙNG vai trò + CÙNG cấp** (`cbnv_tw` → `cbnv_tw_01`), **CẤM đổi vai trò/cấp**. Ghi rõ tài khoản thực dùng vào báo cáo.

Dữ liệu có sẵn trên env (đo bằng `cbnv_tw` lúc 13:00): tổ chức tư vấn 10 · hồ sơ pháp lý DN 34 · tư liệu pháp lý VV 8 · vụ việc 62.

---

## 1. Công cụ

**Chrome DevTools MCP là công cụ bắt buộc** (`mcp__chrome-devtools__*`). Schema là deferred → gọi
`ToolSearch("select:mcp__chrome-devtools__new_page,mcp__chrome-devtools__navigate_page,mcp__chrome-devtools__take_snapshot,mcp__chrome-devtools__take_screenshot,mcp__chrome-devtools__click,mcp__chrome-devtools__fill,mcp__chrome-devtools__fill_form,mcp__chrome-devtools__type_text,mcp__chrome-devtools__wait_for,mcp__chrome-devtools__evaluate_script,mcp__chrome-devtools__list_network_requests,mcp__chrome-devtools__list_console_messages,mcp__chrome-devtools__list_pages,mcp__chrome-devtools__select_page")`
trước khi dùng. CẤM gstack `$B`, CẤM Playwright.

**Chỉ có MỘT trình duyệt dùng chung** — bạn là agent duy nhất đang chạy, nhưng đừng mở quá nhiều tab; xong việc thì để nguyên, đừng đóng tab của người khác.

### Mở đầu MỖI phiên verify (BẮT BUỘC — chống đo trên bản cũ)
1. `new_page("https://htpldn-uat.ospgroup.vn/login")` (hoặc `navigate_page` với `ignoreCache: true` nếu tab đã mở sẵn).
2. Đăng nhập → OTP `666666`.
3. `evaluate_script(() => [...document.querySelectorAll('script[src]')].map(s => s.src))` → xác nhận đang chạy `index-DpIXRGaI.js`. **Ghi tên bundle vào nhật ký đo.**
4. Đọc nhãn bản dựng ở góc sidebar (dạng `HTPLDN · V1.0.x`) và ghi lại.

### Quy tắc thao tác (rút từ CLAUDE.md)
- `wait_for([text])` trước mọi `fill`/`click`; timeout ≥10000ms.
- `take_snapshot` lấy `uid` FRESH sau mỗi navigate/mở cửa sổ. `uid` cũ vô hiệu.
- Sau khi đăng nhập thì **click sidebar**, KHÔNG `navigate_page` (mất phiên). Ngoại lệ duy nhất: bước 1 ở trên.
- Sidebar thu gọn → click "Thu gọn menu" để mở rộng trước khi bấm menu con lần đầu.
- Selector hay dùng: login `input[placeholder="Nhập tên đăng nhập"]` · `input[placeholder="Nhập mật khẩu"]` · OTP `input[inputmode="numeric"][maxlength="1"]` (điền đủ 6 số vào ô đầu → tự submit) · bảng `.ant-table-tbody tr.ant-table-row` · toast `.ant-message-notice-wrapper` · nút submit form thường là **[Đồng ý]** chứ không phải [Lưu] · hành động trên dòng là thẻ `<a>` không phải `<button>`.
- Form CRUD của app là **Drawer** (panel trượt bên phải), không phải modal giữa màn.

### Bắt thông báo nổi (toast) — CHỈ dùng bộ dùng chung
Đọc file `output/UAT_doi-tac/tools/toast-capture.js` rồi `evaluate_script` nguyên khối đó **TRƯỚC** khi bấm nút.
**CẤM tự viết observer có lọc trùng** (che double-toast → Pass oan) và **CẤM dùng `textContent`** (bắt cả node ẩn → bug ma).
Toast tự tắt: hẹn giờ bấm nút sau ~2500ms **rồi mới** gọi `take_screenshot` (đảo thứ tự), hoặc lấy response body của request làm bằng chứng mạnh hơn ảnh.
Mỗi lần SPA điều hướng (click menu, mở màn khác) là observer bị xoá → **cài lại**.

---

## 2. Nguyên tắc verdict (KHÔNG được vi phạm)

| Verdict | Khi nào |
|---|---|
| **Pass** | Chạy ĐỦ luồng tới đúng bước sinh ra lỗi cũ, lỗi không còn |
| **Reopen** | Vẫn tái hiện · fix **một phần** · fix đẻ ra bug mới cùng luồng |
| **BLOCKED** | Không dựng được tiền đề vì lý do **khách quan** (env/BE/DB hỏng) — báo về, KHÔNG tự quyết |

🔴 **CẤM Pass bằng quan sát tĩnh.** "Thấy field đã có rồi", "UI trông đúng" KHÔNG phải bằng chứng khi
case nói về hành vi. Phải bấm tới bước sinh lỗi. (Ngoại lệ: case thuần tĩnh — nhãn/thứ tự cột/icon —
thì quan sát màn hình CHÍNH LÀ phép đo, nhưng vẫn phải chụp ảnh và mở ảnh ra đọc.)

🔴 **Không dựng được tiền đề vì thiếu dữ liệu/trạng thái/tài khoản mà TỰ TẠO ĐƯỢC → phải tự seed rồi test.**
Bỏ qua rồi ghi Pass = Pass oan. Thiếu seed **không** phải blocker hợp lệ.

🔴 **Bug gộp nhiều ý → mọi ý phải hết lỗi mới Pass.** Còn ≥1 ý lỗi → Reopen.

🔴 **Bug về trường lưu trong DB** (tên tệp, ảnh chụp trạng thái): bản ghi CŨ tạo trước lúc fix vẫn hỏng là
bình thường → phép thử quyết định là **tạo bản ghi MỚI** qua luồng chuẩn.

🔴 **Câu chữ của dev ở cột `DEV phản hồi lần 1` không phải bằng chứng** — nó là ghi chép vòng 1, dùng để
biết *phải kiểm chỗ nào*, không dùng để kết luận.

🔴 **Thấy lỗi NGOÀI phạm vi case cũng phải ghi lại** (mục "Phát hiện thêm" trong báo cáo). Đừng bỏ qua.

---

## 3. Đầu ra bắt buộc cho MỖI case

Thư mục gốc đợt: `output/UAT_doi-tac/reverify-week-3/uat-luong3-2026-08-04/`

1. **Ảnh** → `image/<MãTC>-v2-NN-<mô-tả-ngắn>.png`. Chụp ở **mọi thao tác đổi trạng thái**, và **mở ảnh ra đọc bằng tool Read** rồi mô tả thấy gì. Ảnh không đọc = coi như không có.
2. **Bảng đối chiếu điều kiện** → `cond/<MãTC>.md`, theo mẫu:

```markdown
# Bảng đối chiếu điều kiện — <MãTC> (dòng <N>) — <tên ngắn>

**Kết luận:** <Pass|Reopen> — <1 câu>

| Điều kiện có thể đổi kết quả | Bug gốc (vòng 1) | Mình đo lại (tài khoản, 04/08/2026) | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | ... | ... | Không |
| Màn hình / entity + trạng thái | ... | ... | Không |
| Dữ liệu tiền đề | ... | ... | Không |
| Thao tác / input | ... | ... | Không |

**Bằng chứng:** `image/...png` (mô tả thấy gì) · network `<METHOD> <path>` [status]
```
Còn **1 ô GAP = chưa verify xong**, CẤM ra verdict.
Case thuần tĩnh có thể thay bảng bằng 1 đoạn nêu rõ vì sao không phụ thuộc vai trò/trạng thái.

3. **Nhật ký đo** → `reverify-audit/<MãTC>-vong2.md`: ghi ngay sau mỗi phép đo (giờ, thao tác, số liệu
   đo được, đường dẫn ảnh). Xem mẫu chuẩn: `../uat-luong2-2026-08-04/reverify-audit/CNDSMLTVV_01-vong2.md`.
4. **verdict** → nối 1 dòng JSON vào `verdicts.jsonl` ở thư mục gốc đợt:
   `{"ma_tc":"...","row":N,"verdict":"Pass|Reopen|BLOCKED","tom_tat":"<1 câu ≤25 từ>","evidence":"image/....png","cond":"cond/....md","tai_khoan":"...","phat_hien_them":"<hoặc chuỗi rỗng>"}`

---

## 4. Ghi Google Sheet

| Verdict | Ai ghi |
|---|---|
| **Pass** | **Bạn tự ghi** ngay sau khi xong case (chỉ 1 ô `Verify 2`, không đè gì của dev) |
| **Reopen / BLOCKED** | **KHÔNG ghi.** Dừng, báo về orchestrator — ghi Reopen sẽ ĐÈ cột của dev nên phải người duyệt |

Lệnh ghi Pass (chạy `--dry-run` trước, đọc kỹ old→new, rồi bỏ `--dry-run`):

```bash
cd "/Users/huongttt/Downloads/antigravity/PM HTPLDN/skilkk"
UAT_TAB="UAT_TGPL Doanh Nghiệp-tuần 3" python3 output/UAT_doi-tac/tools/sheet_write.py \
  --mode reverify2 --row <N> --ma-tc <MãTC> --status Pass \
  --evidence output/UAT_doi-tac/reverify-week-3/uat-luong3-2026-08-04/image/<ảnh>.png \
  --condition-table output/UAT_doi-tac/reverify-week-3/uat-luong3-2026-08-04/cond/<MãTC>.md \
  --vong2-do-dev-build "Dev build môi trường UAT mới htpldn-uat.ospgroup.vn 04/08/2026, đối tác chưa phản ánh vòng 2" \
  --dry-run
```
Case thuần tĩnh: thay `--condition-table ...` bằng `--static-bug "<lý do>"`.

🔴 **Script báo lỗi/chặn → DỪNG, báo về. CẤM ghi tay, CẤM viết script khác để lách.**

---

## 5. Kết thúc lô

Trả về (văn bản cuối cùng của bạn = dữ liệu, không phải lời chào):
- Bảng: `Mã TC | dòng | verdict | 1 câu lý do | đã ghi sheet? (có/không)`
- Danh sách case Reopen/BLOCKED kèm mô tả triệu chứng đủ để viết note cho đối tác.
- Mục "Phát hiện thêm" (lỗi ngoài phạm vi case).
