# BRIEF CHUNG — lô F9 · tái xác nhận 6 case QLHSPLDN trên env NGHIỆM THU của đối tác

**Ngày:** 2026-08-07 · **Flow áp dụng:** [`flows/03-reverify-sau-dev-fix.md`](../../../../flows/03-reverify-sau-dev-fix.md)
— **nhánh 2: "Tái xác nhận trên môi trường khác"** (đã Pass ở env nguồn = env nội bộ, nay xác nhận trên env đích
= env nghiệm thu của đối tác).

---

## 1. Phạm vi — đúng 6 dòng tab `bug` (gid 1714340219)

| Dòng | Mã TC | Mô tả ô phiếu | Trạng thái dev fix hiện tại | Nguồn canonical cho cách đo |
|---|---|---|---|---|
| 291 | `QLHSPLDN_06` | Xem | `Test done` | [`tieuchi/QLHSPLDN_06.md`](../tieuchi/QLHSPLDN_06.md) §4 §5 §7 + entry `BUG-HSPLDN-QLHSPLDN-06` trong [`bug-report.md`](../bug-report.md) |
| 292 | `QLHSPLDN_07` | Sửa | `Test done` | [`tieuchi/QLHSPLDN_07.md`](../tieuchi/QLHSPLDN_07.md) §4 §5 §7 + entry `BUG-HSPLDN-QLHSPLDN-07` trong [`bug-report.md`](../bug-report.md) |
| 293 | `QLHSPLDN_11` | Tìm kiếm có kết quả | `Test done` | entry `BUG-HSPLDN-QLHSPLDN-11` + bảng vế C1 trong [`F4-pilot/bao-cao-lo-2026-08-07.md`](../F4-pilot-QLHSPLDN-2026-08-07/bao-cao-lo-2026-08-07.md) |
| 294 | `QLHSPLDN_12` | Tìm kiếm không kết quả | `Test done` | entry `BUG-HSPLDN-QLHSPLDN-12` + vế C2 (cùng file trên) |
| 295 | `QLHSPLDN_13` | Khoảng ngày không hợp lệ | `Test done` | entry `BUG-HSPLDN-QLHSPLDN-13` + vế C3 (cùng file trên) |
| 296 | `QLHSPLDN_14` | Xuất Excel thành công | `Test done` | entry `BUG-HSPLDN-QLHSPLDN-14` + vế C4 (cùng file trên) |

**KHÔNG thuộc phạm vi:** dòng 297 `QLHSPLDN_15` (đang `BA confirm`). Không đụng.

> 🔴 **Cả 6 dòng ĐÃ có `Kết quả verify` của vòng env NỘI BỘ**, đều kết bằng câu *"Pass tạm cho tới khi bản dựng
> lên môi trường nghiệm thu"*. Lô này chính là lượt đóng câu đó. Nội dung ô sẽ được **GHI ĐÈ** bằng kết quả đo
> trên env đối tác — không phải nối thêm.

---

## 2. Môi trường + bản dựng

| Hạng mục | Giá trị |
|---|---|
| Env verify (BẮT BUỘC) | `https://htpldn-uat.ospgroup.vn` — env **NGHIỆM THU CỦA ĐỐI TÁC** |
| MailHog của chính env này | `https://htpldn-uat.ospgroup.vn/mailhog/` · API `/mailhog/api/v2/messages?limit=5` |
| Bó mã FE đo lúc 12:43 VN 07/08 | `assets/index-D4NhKEjr.js` · `assets/index-DVlgOkLg.css` |
| `GET /` last-modified | `Fri, 07 Aug 2026 04:17:55 GMT` (= **11:17 giờ VN 07/08**) |
| `GET /` etag | `"6a755c73-428"` |
| Máy chủ web | `nginx` |

🔴 **Bản dựng này MỚI TINH — deploy ~11:17 VN hôm nay**, khác cả bản `V1.0.3` trong bằng chứng đối tác lẫn bản
`V1.0.8`/`V1.0.9` của env nội bộ nơi 6 case được chấm Pass. ⇒ **Số đo cũ ở env nội bộ KHÔNG chứng minh gì cho
lô này.** Phải đo lại thật.

🔴 **Nhịp deploy của dự án rất dày** (env nội bộ 5 bản trong ~12h ngày 06-07/08) và **chuỗi `V1.0.x` trên sidebar
KHÔNG phải định danh bản dựng** (đã có ca bó mã mới hơn mà nhãn lùi số — xem [`BAN-DUNG.md`](../BAN-DUNG.md)).
⇒ Định danh thật = **bó mã `assets/index-*.js` + `last-modified`**. **Đo vân tay ở CẢ ĐẦU VÀ CUỐI mỗi case**;
hai đầu khác nhau ⇒ khai rõ quan sát nào rơi trước/sau mốc deploy và đo lại case đó.

---

## 3. Tài khoản

**Tài khoản ra verdict cho cả 6 case: `cbnv_tw` / `Test@1234`** — vai trò `CB_NV_TW`, cấp TW.

- Trùng đúng vai trò đọc được trên bằng chứng đối tác (badge *"Cán bộ NV Trung ương  CB_NV_TW"*, phạm vi `BTP · TW`).
- Đã kiểm sống 07/08 05:43 GMT: `POST /api/v1/auth/login {username, password}` → trả `otpToken` ⇒ **env này CÓ
  bước mã xác thực**, lấy ở MailHog của chính env.
- 🔴 **Env đối tác KHÔNG có bộ `_01`.._05`** như env nội bộ. `cbnv_tw` bị khóa ⇒ **KHÔNG có sibling để fallback
  theo Rule 7** ⇒ dừng, mark BLOCKED, báo điều phối. **Cấm** đổi sang cấp BN/ĐP.
- `admin` / `Secret@123` (QTHT) **chỉ** dùng để đọc màn Nhật ký hệ thống (`SCR-VIII-10`) ở vế (c) của `_07`.
  **Tuyệt đối không dùng `admin` để ra verdict** — quyền rộng che lỗi phân quyền.
- Giới hạn đăng nhập **5 lượt / 60 giây**. Sai mật khẩu nhiều lần sẽ bị chặn — đừng đoán mò.

---

## 4. Kỷ luật dữ liệu trên env đối tác — ĐỌC KỸ

Đây là env **nghiệm thu của đối tác**, không phải sân chơi QA.

1. **CẤM sửa/xoá bất kỳ bản ghi nào QA không tự tạo.** Cụ thể cấm đụng `DN-XX-0005`
   (`1a715c55-bc31-46de-ae07-56dd4f403ce5`), `HSPL-20260803-0001`, `HSPL-20260731-0002` — đó là dữ liệu trong
   ảnh/video bằng chứng của đối tác.
2. **Thiếu tiền đề ⇒ TẠO MỚI, không mượn bản ghi có sẵn.** Bản ghi QA tạo phải mang dấu nhận dạng rõ ràng
   dạng `QA-W5-…` để đối tác nhìn là biết của QA.
3. **Seed bằng UI thật.** Buộc phải gọi máy chủ thì đường gọi **lấy từ chính request UI phát ra**
   (`list_network_requests`) — **cấm đoán đường dẫn API, cấm ghi thẳng CSDL**.
4. **Khai đầy đủ vào báo cáo:** tạo/đổi bản ghi nào · đổi gì · trên env nào. Bản ghi không khai = coi như chưa đo.
5. Không đụng dữ liệu của module khác chỉ vì tiện tay.

---

## 5. Luật chấm (Flow 03) — bản rút gọn, đọc bản đầy đủ trước khi chạy

### Thứ bậc nguồn
1. **SRS tại `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`** — quyết định hệ thống PHẢI làm gì.
   (Prompt session chỉ định đúng thư mục này. Không mở `input/srs-update-2026-5-5/` để lấy số dòng.)
2. **Expected gốc / ô phiếu đối tác** — quyết định phạm vi vấn đề đang re-verify.
3. **Nguồn canonical ở §1** — quyết định cách tái hiện + phép đo đã khóa. Không được thêm yêu cầu trái SRS.
4. Note sheet, phản hồi dev, ảnh cũ, báo cáo cũ = **manh mối tìm chỗ đọc**, KHÔNG tự quyết verdict.

### Quan hệ expected ↔ SRS (khóa TRƯỚC khi mở app)
| Quan hệ | Xử lý |
|---|---|
| `MATCH` | Được re-verify theo đường đo đã khóa |
| `DIFF` | **Cấm Pass** vế đó → Cần BA, ghi nguyên hai phía |
| `GAP` (SRS im lặng / tự mâu thuẫn) | **Cấm Pass/Reopen** vế đó → Cần BA + câu hỏi cụ thể |

### Luật dừng sớm
- **Có FAIL:** vế `MATCH` chạy đúng tiền đề + vi phạm điều kiện FAIL/PASS + có quan sát quyết định **+ một đối
  chứng độc lập** + sai lệch không do env/tài khoản/dữ liệu/bản dựng ⇒ **Reopen và DỪNG** các biến thể còn lại.
  Trước khi dừng, ghi nhận mọi vế có thể kết luận từ **chính artifact đã có**; không mở thêm vòng UI để tìm lỗi thứ hai.
- **Chưa có FAIL:** muốn Pass phải chạy **hết** mọi vế `MATCH` còn phải đo + mọi biến thể nguồn canonical nêu
  đích danh + mọi điều kiện PASS + đối chứng độc lập cho từng quan sát quyết định.

### 🔴 CẤM Pass bằng quan sát tĩnh
Yêu cầu của chủ việc, nhắc lại nguyên văn: *"CẤM Pass bằng quan sát tĩnh (thấy field đã có, UI trông đúng rồi).
Phải chạy hết luồng — fix thêm UI mà BE vẫn hỏng là chuyện thường."*
⇒ Có ô tìm kiếm **không** đủ cho `_11`; phải gõ từ khóa, bấm, đọc kết quả **và** đối chứng phản hồi máy chủ.
Có nút Xuất Excel **không** đủ cho `_14`; phải bấm, **mở nội dung tệp** đọc header + số dòng.
Có nút Xem **không** đủ cho `_06`; phải bấm thật, đọc nội dung cửa sổ, đối chiếu từng trường với bản ghi.

### Đối chứng độc lập — bấm lại cùng nút KHÔNG tính
- trạng thái / lưu dữ liệu → đọc lại bản ghi hoặc response máy chủ
- hiển thị → đối chiếu dữ liệu nguồn
- tệp xuất / tải lên → **mở chính tệp** hoặc đọc lại metadata/nội dung

### Verdict logic
| Verdict | Khi nào | Ghi ô `Trạng thái dev fix` |
|---|---|---|
| **Pass** | Mọi vế `MATCH`, chạy hết phạm vi/biến thể bắt buộc, tất cả đạt, có đối chứng quyết định | `UAT done` |
| **Reopen** | ≥1 vế `MATCH` FAIL đủ 4 điều kiện (gồm fix một phần) | `Reopen` |
| **Reopen + Cần BA** | Có vế `MATCH` FAIL **và** vế độc lập `DIFF/GAP` | `Reopen` |
| **Cần BA** | Không vế nào đủ Reopen nhưng expected khác SRS, hoặc SRS im lặng/mâu thuẫn | `BA confirm` |
| **Chưa chốt** | Blocker khách quan / nguồn mơ hồ / 2 phép đo mâu thuẫn / thiếu biến thể quyết định | **KHÔNG ghi ô** — báo điều phối |

**Pass/Reopen chỉ có hiệu lực trên env + bản dựng đã đo.** Không viết *"fix đã có tác dụng"* nếu không có bằng
chứng trạng thái trước fix — chỉ kết luận **hiện trạng đạt/sai so với SRS**.

---

## 6. Định dạng nội dung ô `Kết quả verify`

Dòng đầu **luôn** dùng icon trung tính `📌`. Sau đó chỉ ghi các mục **có nội dung**, đúng thứ tự:

```
📌 KẾT QUẢ CHUNG: ĐÃ HẾT LỖI            ← hoặc HIỆN TẠI ĐẠT / CÒN LỖI (REOPEN) / CẦN BA XÁC NHẬN
                                          / CÒN LỖI (REOPEN) + CẦN BA XÁC NHẬN / CHƯA THỂ KẾT LUẬN
❌ CÒN LỖI — <hành vi>          : vì sao thuộc case · SRS file:dòng đòi gì · web sai thế nào + bằng chứng · dev cần sửa gì
❓ CẦN BA XÁC NHẬN — <điểm>     : expected ↔ SRS · một câu hỏi BA trả lời trực tiếp được · ghi rõ chưa chấm đạt/lỗi
✅ ĐÃ HẾT LỖI — <lỗi gốc>       : triệu chứng cũ · yêu cầu SRS/expected · hiện trạng + số đo chứng minh
⏸ CHƯA KIỂM TRA — <phần>       : phần chưa đo · lý do · dữ kiện cần bổ sung
🔎 PHẠM VI ĐÃ ĐO                : env · bản dựng/thời điểm · role · dữ liệu/biến thể quyết định
```

**Nghĩa icon cố định, CẤM đảo:** `📌` tổng kết · `❌` còn lỗi · `❓` cần BA · `✅` đạt/không phải lỗi ·
`⏸` chưa đủ căn cứ · `🔎` phạm vi. `⚠️` chỉ dùng cho caveat, **không** dùng làm verdict.

**Viết bằng lời người đọc hiểu.** Mã `C4a`, `MATCH/DIFF/GAP`, enum thô, tên biến script, định danh bó mã
chỉ để trong hồ sơ audit — trừ khi thật sự cần truy vết cho dev/BA. Đặt SRS/artifact **cạnh** kết luận nó
chứng minh. Không tạo mục rỗng, không lặp bằng chứng.

Người đọc ô này là **đối tác + dev**, không phải QA nội bộ. Không lộ chuyện test 2 môi trường như một quy trình
nội bộ — nhưng **bắt buộc** ghi rõ ở mục `🔎 PHẠM VI ĐÃ ĐO` rằng đã đo trên chính env nghiệm thu, kèm mốc giờ.

---

## 7. Ghi Drive — mapping cứng do chủ việc quy định

| Verdict | Ô `Trạng thái dev fix` |
|---|---|
| Pass | `UAT done` |
| Reopen | `Reopen` |
| Cần BA | `BA confirm` |

- Diễn giải → ô **`Kết quả verify`**.
- 🔴 **Ô CHỈ ĐỌC, CẤM ghi đè:** `Trạng thái` · `Kết quả thực tế` · `TKM phản hồi lần 1` · `DEV phản hồi lần 1`.
- Dropdown thật của `Trạng thái dev fix` (đã đọc 07/08):
  `['In Progress', 'Fixed', 'UAT done', 'Bug', 'Test done', 'reject', 'Reopen', 'BA confirm']` — cả 3 giá trị
  cần dùng đều hợp lệ.
- Công cụ ghi: `tools/sheet_bug_verify_write.py` (generic, có guard `--expect` chống ghi đè thay đổi mới).
  **Chạy `--dry-run` trước, rồi ghi thật, rồi ĐỌC LẠI xác nhận** bằng `UAT_TAB=bug python3 tools/sheet_read.py --row N`.
- Spreadsheet: `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug`.
  ⚠️ **KHÔNG nhầm với `1dJat1cc68…`** — đó là file của ĐỐI TÁC, cấm ghi.
- Công cụ ghi bị guard chặn ⇒ **DỪNG, báo điều phối**. Cấm ghi tay để lách, cấm viết script dùng-một-lần.

**Bug mới ngoài phạm vi** (nếu tự lộ trong luồng bắt buộc): mã `QLHSPLDN_QA<số thứ tự>`, thêm dòng mới với các ô
`Mã TC` · `Tên chức năng` · `Mô tả` · `Các bước thực hiện` · `Kết quả mong đợi` · `Kết quả thực tế` ·
`Trạng thái=Fail` · `Dopai=bug` · `Ảnh/vieo 1=<link xem được>`. **Báo điều phối trước khi thêm dòng.**

---

## 8. Bug mới tự lộ — KHÔNG exploratory

Trong lúc chạy tiền đề / thao tác / đọc output **bắt buộc** của case, không được bỏ qua sai lệch rõ ràng trong
chính màn/phản hồi/tệp đang quan sát. Được đọc một lượt phần đang hiển thị, **nhưng**:

- **không** bấm thử từng field/nút, **không** chạy checklist regression, **không** mở chức năng khác để tìm bug;
- mở SRS thật dẫn `file:dòng`. SRS im lặng → **candidate**; SRS mâu thuẫn → **candidate + câu hỏi BA**;
- artifact sẵn có chưa đủ ⇒ cả case chỉ được thêm **tối đa 1 phép xác nhận**, giữ nguyên role/dữ liệu/bộ lọc,
  chỉ replay đúng thao tác hoặc đọc side-effect đã phát sinh. Thao tác **làm đổi dữ liệu / tạo đầu ra nghiệp vụ
  mới** (gửi mail, tạo/sửa bản ghi, tạo tệp) ⇒ **KHÔNG replay**, chỉ đọc lại kết quả đã có;
- bug mới **chỉ** đổi verdict case gốc khi làm điều kiện PASS không đạt hoặc chặn chính phép đo bắt buộc.

Candidate ghi dạng: `<hiện tượng> · xuất hiện tại <bước> · artifact <...> · còn thiếu <...> để xác nhận`.

---

## 9. Công cụ đo — Chrome DevTools MCP

**Chỉ MỘT agent duy nhất được chạm `mcp__chrome-devtools__*` trong cả lô** (agent ĐO). Trình duyệt là tài nguyên
dùng chung — hai agent thao tác song song sẽ giẫm chân nhau và làm hỏng số đo.

- `wait_for(text[])` trước mọi `fill`/`click`; timeout ≥10000ms.
- `take_snapshot` lấy `uid` **fresh** sau mỗi navigate/modal/render.
- **`click` sidebar, KHÔNG `navigate_page` sau khi đăng nhập** — auth ở `localStorage` + HttpOnly cookie,
  full reload sẽ đá về `/login`. (Trừ khi CỐ Ý tải lại trang để đo đường thứ hai — khi đó chấp nhận đăng nhập lại.)
- Sidebar thu gọn ⇒ click *"Thu gọn menu"* mở rộng trước khi vào submenu lần đầu.
- Verify thông báo tự tắt (<5s): cài `MutationObserver` trên `document.body` **TRƯỚC** khi bấm, capture
  `addedNodes` 2-5s. **CẤM dedupe** (che double-toast → Pass oan) và **CẤM `textContent`** (bắt node ẩn AntD →
  bug ma) — đọc `innerText`. Luôn đếm request kèm thông báo, bọc **cả `fetch` lẫn `XMLHttpRequest`**.
- Cảnh báo dụng cụ đã gãy ở vòng trước: đếm tệp dùng `.ant-upload-list-item-container`; đọc ô chọn dùng
  `.ant-select-content`; điền ô phải đặt giá trị qua **setter gốc + phát `input`/`change`** (`fill_form` **nối
  chuỗi** thay vì thay thế → phải clear field trước).
- Nút submit form là **`Đồng ý`**, không phải `Lưu`. Row action `Sửa`/`Xoá` là thẻ `<a>`.
- Đọc `.xlsx` tải về: MCP isolated Chrome **không** đổ file về `~/Downloads` → parse EOCD + `DecompressionStream`
  ngay trong trang, chỉ return đúng thứ cần đo (xem memory `reference-read-xlsx-content-in-browser-zip-parse`).
- Ảnh lưu vào `F9-uatdoitac-QLHSPLDN-2026-08-07/image/`.

---

## 10. Bố cục thư mục lô

```
F9-uatdoitac-QLHSPLDN-2026-08-07/
├── 00-BRIEF-CHUNG.md          ← file này
├── chuan/<MA_TC>.md           ← Giai đoạn A: vế đã khóa + quan hệ SRS + PASS/FAIL/biến thể bắt buộc
├── do/<MA_TC>.md              ← Giai đoạn B: số đo thô + vân tay bản dựng 2 đầu + verdict
├── note/note-sheet-<MA_TC>.txt← nội dung ô `Kết quả verify` (đúng nguyên văn đã ghi lên sheet)
├── image/                     ← ảnh + response quyết định verdict
├── seed-files/                ← tệp dùng để seed
└── BAO-CAO-LO.md              ← báo cáo cuối lô
```
