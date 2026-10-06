# QA Verify Protocol — Verify bug đối tác

> 🔴 **Đọc trước khi verify:** [QA_POSTMORTEM_bo-sot-bug-2026-07-16.md](QA_POSTMORTEM_bo-sot-bug-2026-07-16.md)
> Quy trình này rất chặt về **chấm đúng case được giao**, nhưng 16/07/2026 đã lộ ra nó **không hề bắt QA quan sát**:
> QA chạy 16 case mà không thấy lỗi hiện ngay trên màn hình, vì (a) phép đo tự lọc trùng đã giấu lỗi, và
> (b) bước seed bị coi là "không phải test" nên không ai soi. Postmortem chốt 4 việc dưới — áp cho MỌI tester:
>
> 1. **Bộ bắt thông báo:** chỉ dùng [tools/toast-capture.js](tools/toast-capture.js). **CẤM** tự viết observer có lọc trùng; **CẤM** dùng `textContent` để đọc chữ hiển thị (gom cả node ẩn → bug ma). Luôn **đếm số request kèm số thông báo**.
> 2. **Chụp màn hình ở MỌI thao tác đổi trạng thái — kể cả bước seed — và PHẢI mở ảnh ra đọc.** Lưu mà không đọc = vô nghĩa.
> 3. **Bug ngoài phạm vi case cũng PHẢI log** — mở dòng TC mới bằng [tools/sheet_add_bug_row.py](tools/sheet_add_bug_row.py) để nó tới được dev, đừng để nằm im trong file .md.
> 4. **Bug candidate ≠ bug** — đo lại bằng phương pháp thứ hai trước khi log (2 phương pháp mâu thuẫn → chưa được log).

## Vòng lặp MỖI CASE (làm TRỌN 1 case rồi mới sang case sau — CẤM gom cuối lô)

Mỗi case đi đúng thứ tự 5 bước, xong bước này mới sang bước sau:
1. Xem evidence (qua 3 CỔNG).
2. Verify trên web.
3. Ghi verdict + note vào Google Sheet NGAY.
4. Nếu `Open`: thêm entry bug-report + ≥1 screenshot (đừng bỏ bước này sau khi ghi sheet).
5. Báo cáo ngắn 1 case cho user → rồi mới sang case tiếp.
6. **Trả lời "ngoài tiêu chí BA ra, có thấy gì bất thường không?"** — dựa trên ảnh đã đọc ở bước 2, không phải suy đoán. Có → log theo (3) ở khối trên. Không → ghi rõ "không phát hiện thêm" trong report.

## 3 CỔNG bắt buộc (qua đủ 3 cổng mới được chốt verdict)

1. **Cổng bằng chứng** — phải **mở XEM được** file đối tác rồi mới verify:
   - **Lấy evidence:** BẮT BUỘC chạy `python3 tools/fetch_evidence.py --row N` (đọc text thường sẽ **GIẤU** link Drive). Video → trích frame, xem tới **khoảnh khắc lỗi**.
   - **"Không thấy file local" ≠ "đối tác không gắn":** chỉ kết luận không có evidence khi script báo **RỖNG (exit 3)** → verdict TRỐNG + hỏi user. Chưa xem được file = **Cổng 1 CHƯA đóng, CẤM verify bằng text**.
   - **Đọc FULL-RES** — không kết luận từ montage thu nhỏ.
   - **Trích 3 dữ kiện neo** (viết ra TRƯỚC khi hình thành giả thuyết): (a) URL/ID bản ghi · (b) trạng thái entity đối tác đang đứng (stepper / badge / cột trạng thái) · (c) dữ liệu tiền đề của case.
2. **Cổng hiểu bug.** Ghi 3 dòng trước khi verify: *evidence đã xem: file + frame/timestamp chứa LỖI + 1 câu tả lỗi thấy trong frame đó* (chưa thấy frame lỗi → verdict TRỐNG + hỏi user, không tự nhận "đã xem") · *đối tác phản ánh CỤ THỂ gì* (thiếu cột/message/state nào — không chung chung) · *data+bước tái hiện*.
3. **Cổng đối chiếu.** Lập bảng *SRS yêu cầu (dẫn line)* vs *thực tế web* → đủ/thiếu. Cấm kết luận cảm tính "nhìn render ổn".

## 🔴 Quy tắc VÀNG + Bảng đối chiếu điều kiện (áp MỌI case, MỌI loại bug, MỌI tester)

> **Kết luận phải dựa trên ĐIỀU KIỆN của ĐỐI TÁC, không phải điều kiện mình tiện tái hiện.**
> Tái hiện ở một điều kiện KHÁC điều kiện đối tác rồi thấy "chạy được" = **CHƯA verify**, KHÔNG phải `Reject`.

**Với bug phụ thuộc role/state/data/input** (workflow, permission, filter, validation, empty-screen): trước khi chốt **bất kỳ verdict nào** BẮT BUỘC điền Bảng đối chiếu điều kiện — chỉ kết luận khi 0 GAP. **Bug tĩnh** (typo/label/icon/màu/cột hiển thị cố định) KHÔNG cần bảng, chỉ cần Cổng 3 (SRS vs web). Ô TRỐNG do blocker cũng không cần bảng.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | ... | ... | |
| Entity + **trạng thái** (state machine) | ... | ... | |
| Dữ liệu tiền đề (record/entity/cấu hình/file import/lịch/trạng thái liên quan...) | ... | ... | |
| Input / filter / giá trị nhập | ... | ... | |

- Chỉ ghi dòng điều kiện **có khả năng đổi kết quả** (chọn theo "Checklist theo loại bug") — đừng máy móc điền đủ 4 dòng.
- Còn **1 ô GAP = CHƯA verify xong** → **CẤM mọi verdict** (kể cả ô TRỐNG). Phải đóng GAP: tạo tài khoản / seed / chuyển đúng trạng thái rồi test lại (§Nguyên tắc 4). Chỉ khi GAP **không thể đóng** (blocker khách quan) mới để ô **TRỐNG**.
- GAP mà chứng minh được **không** ảnh hưởng kết quả (dẫn SRS/thử nghiệm) → ghi rõ lý do mới được bỏ qua. **KHÔNG áp cho GAP tạo được** (tài khoản/vai trò, dữ liệu, state): các GAP này chỉ đóng bằng **test thật sau khi đã tạo tiền đề**.

## Nguyên tắc

1. **SRS/BA là chuẩn**, không phải Expected đối tác. Thứ bậc khi mâu thuẫn: `SRS/BA duyệt > thiết kế nội bộ duyệt > thiết kế/expected đối tác`. **Nhắc:** Expected đối tác khác SRS → `BA confirm`, KHÔNG auto-Reject (dù SRS > expected). Định nghĩa đầy đủ Reject vs BA confirm ở **bảng Verdict** (nguồn chuẩn duy nhất).
2. **Verify qua UI thật** (Chrome DevTools MCP). API/DB chỉ để ghi sheet / tải bằng chứng / điều tra. **UI mâu thuẫn API/DB/log** → verdict theo **UI + SRS**. UI không quan sát được vì blocker **khách quan** (env/BE/DB/tích hợp — sau khi đã tạo đủ tiền đề, §Nguyên tắc 4) → **ô TRỐNG**; vướng **căn cứ nghiệp vụ cần BA quyết** → `BA confirm`.
3. **Login đúng vai trò của bug.** Admin chỉ dùng prep data/điều tra, **không dùng ra verdict** (quyền rộng → che lỗi phân quyền). Ghi rõ account đã dùng.
4. 🔴 **Thiếu tiền đề thì TỰ TẠO — không phải blocker.** Áp cho cả 3 loại tiền đề: **tài khoản/vai trò · dữ liệu · trạng thái (state/cấu hình)**. Tiền đề *tạo được* mà không tạo → **CẤM** ghi verdict (kể cả ô TRỐNG). Chỉ "không verify được" khi blocker **khách quan** (BE/DB/tích hợp/env hỏng), hoặc tiền đề **không thể tạo** (vd vai trò chỉ đăng nhập qua VNeID Tier 2 mà QA không có).
   - **Thiếu dữ liệu / trạng thái** → seed, hoặc chuyển record về đúng state tiền đề của evidence đối tác, rồi test lại.
   - **Thiếu tài khoản** → tạo mới: login `admin` → **Quản trị hệ thống → Tài khoản & phân quyền → Thêm mới** → hệ thống gửi **link kích hoạt** tới email → lấy link trong **MailHog** → "Đặt mật khẩu lần đầu". (Vai trò khả dụng: **Quản trị hệ thống → Vai trò**.) Tạo xong → **ghi vào `input/input.md`** để lần sau dùng lại.
   - **CẤM đóng GAP bằng lập luận** (kiểu *"màn dùng chung nên vai trò khác không đổi kết quả"*) — phải đóng bằng **test thật trên tiền đề đã tạo**.
   - Ghi rõ trong note + bug-report là đã verify bằng **đúng vai trò / state của đối tác**.
5. **Ghi sheet an toàn:** BẮT BUỘC dùng `sheet_write.py` (tự guard spreadsheet/tab/header/mã TC/dropdown → in old→new → đọc lại xác nhận → append `tools/sheet_write.log` kèm **giá trị cũ** của ô bị đè). Chỉ ghi đúng 2 ô, lệch bất kỳ → dừng. **Không chạy được script → DỪNG, hỏi user, KHÔNG ghi tay** (ghi tay = mất hết guard dưới đây):

   | status | Cờ BẮT BUỘC | Script DỪNG khi |
   |---|---|---|
   | verdict (`Open`/`Reject`/`BA confirm`) | `--evidence <path>` + `--condition-table <file.md>` | evidence không tồn tại / rỗng / tên chứa 'partner'; bảng còn ô `...` chưa điền hoặc cột GAP chưa ghi "Không"; verdict sai từ vựng của mode; giá trị không thuộc dropdown của cột |
   | verdict, **bug tĩnh** | `--evidence` + `--static-bug "<lý do ≥10 ký tự>"` | miễn bảng phải CỐ Ý khai, không được im lặng bỏ qua |
   | ô TRỐNG | `--blocker-category A-F` | nhóm A (thiếu seed); nhóm F thiếu `--user-approved` |

## Verdict — 2 cột: `Trạng thái dev fix 1` (P) + `Verify` (Q), note cột `DEV phản hồi lần 1` (R)

> **2 cột, KHÔNG phải 1:** `Trạng thái dev fix 1` (P) = trạng thái xử lý (`Open`/`Reject`/`BA confirm`/`""`). `Verify` (Q) = kết quả QA re-verify (`Pass`/`Reopen`/`Resolved`). Bug **không tái hiện + đối tác CÓ bằng chứng** = cặp mã hoá chuẩn **P=`Reject` (giữ nguyên) + Verify=`Resolved`** (chỉ set Verify, KHÔNG đổi P sang Resolved). Đây là quy ước tuần-3 đã có tiền lệ.

| Verdict | Khi nào |
|---|---|
| `Open` | Actual sai rule SRS (dẫn line rõ), HOẶC hệ thống chặn luồng hợp lệ dù đủ điều kiện |
| `Reject` | **CHỈ khi** chứng minh được đối tác **thao tác/hiểu sai** hoặc báo cáo vô hiệu — web chạy đúng SRS, lỗi đối tác báo **không có thật** (bất đồng về **THỰC TẾ**). ⚠️ **Không tái hiện mà đối tác CÓ bằng chứng (video/ảnh lỗi thật) → KHÔNG Reject → dùng `Resolved`** (không phủ nhận được báo cáo của họ). **KHÔNG** dùng `Reject` cho bất đồng kỳ vọng vs SRS (dù web đúng SRS) |
| `Resolved` *(cột **Verify** — giữ P=`Reject`)* | Bug **không tái hiện** trên bản hiện tại **nhưng đối tác ĐÃ có bằng chứng** (video/ảnh lỗi). Sau khi **re-verify LIVE** thấy chức năng chạy OK → ghi **Verify=`Resolved`**, giữ **P=`Reject`** nguyên. Note: *"Đã kiểm tra lại, không tái hiện được lỗi — chức năng &lt;tên case&gt; hoạt động bình thường."* **CẤM Resolved tĩnh — phải re-verify live qua Chrome DevTools MCP** |
| `BA confirm` | **Expected/kỳ vọng đối tác KHÁC SRS** (kể cả khi SRS đã ghi rõ — đối tác quan sát đúng thực tế nhưng kỳ vọng thứ SRS không quy định/quy định khác) → bất đồng về **ĐẶC TẢ**, để BA chốt có bổ sung/đổi spec không, QA **KHÔNG tự Reject**; HOẶC SRS/BA silent; HOẶC mâu thuẫn giữa các nguồn (SRS vs BA vs thiết kế đã duyệt vs expected đối tác) — nêu rõ đã đọc file/line nào |
| **ô TRỐNG** | Chưa đủ điều kiện verify: không mở được/thiếu evidence, chưa thấy frame lỗi, hoặc blocker **khách quan** env/BE/DB/tích hợp. **KHÔNG** dùng cho tiền đề tạo được (thiếu tài khoản/data/state → phải tạo, §Nguyên tắc 4) — ghi lý do + cần gì |

**Ca biên khi chốt verdict:**
- `Open` vs `BA confirm`: SRS nêu rõ cột/vị trí/message mà app sai → `Open`; SRS chỉ nêu nghiệp vụ chung, app đáp ứng cách khác → `BA confirm`.
- Env/build khác (env được giao luôn khác env đối tác log): sau khi đã đóng GAP điều kiện — lỗi đối tác báo **KHÔNG tái hiện**: (a) đối tác **có bằng chứng** (video/ảnh lỗi thật) → **Verify=`Resolved`** (giữ P=`Reject`), note *"đã kiểm tra lại, không tái hiện, chức năng OK"* — **KHÔNG** phủ nhận đối tác, **KHÔNG** dùng "→ Đối tác kiểm tra lại"; (b) chỉ dùng `Reject` + *"→ Đối tác kiểm tra lại."* khi **chứng minh được đối tác thao tác/hiểu sai**. Web **mâu thuẫn** evidence, HOẶC evidence đúng actual mà chỉ tranh chấp expected/spec → `BA confirm`.

**Tự vấn bắt buộc trước khi ghi sheet** (bác nhầm nguy hơn Open): `Open` → sai clause SRS nào (dẫn line)? · `Reject` → đã **chứng minh** đối tác **thao tác/hiểu sai** chưa (không phải chỉ "tôi ko tái hiện được")? đã mở SRS xác nhận web đúng? **Đối tác CÓ bằng chứng mà chỉ là không tái hiện → `Resolved` (cột Verify, giữ P=`Reject`), KHÔNG Reject.** **evidence đúng actual mà chỉ tranh chấp expected/spec → `BA confirm`, không Reject.** · `Resolved` → đã re-verify **LIVE** (không phải Resolved tĩnh)? · Còn GAP / SRS silent → KHÔNG chốt, quay lại bảng Verdict. · **Bước cuối:** pass đối kháng ở §GATE — chưa làm = chưa được ghi sheet.

**1 case gộp nhiều lỗi con:** tách rõ từng ý trong note + audit, ra verdict cho từng ý. Verdict tổng: `Open` nếu ≥1 ý Open; không có Open mà còn `BA confirm`/ô TRỐNG → lấy theo ý đó (ưu tiên `BA confirm` > ô TRỐNG), **KHÔNG Reject cả case**; chỉ `Reject` khi MỌI ý đều Reject.

**Checklist theo loại bug** (Cổng 3): Hiển thị→cột SRS vs web · Validation→input sai→rule→message · Permission→role×action allowed/denied (role thật) · Workflow→state trước→event→sau · Filter→điều kiện→số bản ghi kỳ vọng vs thực · Màn rỗng→điều kiện no-data→message/hành động · Import/Upload→file mẫu→rule validate→kết quả từng dòng · Tìm kiếm/Sắp xếp/Phân trang→query+tiêu chí→kết quả kỳ vọng vs thực.

## 🔴 GATE BẰNG CHỨNG REAL-DATA — bắt buộc trước khi ghi BẤT KỲ verdict (enforced 2026-07-11)

**Cơ chế lách mà gate này chặn:** gặp friction (không vào được surface đối tác) → thay bằng chứng RẺ ("đọc SRS", "xem video đối tác") cho bước test ĐẮT (seed data + tự tay chạy thao tác). Friction = tín hiệu đi tìm **surface tương đương + seed data**, KHÔNG phải cớ để punt.

**Gate cứng — mỗi verdict (Open/Reject/BA confirm/Resolved/ô TRỐNG) PHẢI kèm 1 trong 2 artifact.** `Resolved` bắt buộc artifact QUAN SÁT từ **re-verify LIVE** (chứng minh thao tác chạy OK / observer+network sạch trên bản hiện tại) — CẤM Resolved dựa trên đọc SRS hay xem lại video đối tác. Ngoại lệ **duy nhất**: ô TRỐNG do **evidence rỗng** — artifact = log `fetch_evidence.py` exit 3 (nhóm F) + hỏi user.

1. **Artifact QUAN SÁT** — hình dạng theo **loại claim** (bám Checklist ở Cổng 3, KHÔNG chỉ toast):

   | Loại claim | Artifact hợp lệ (chạy trên **data đã seed**, surface truy cập được) |
   |---|---|
   | Hiển thị/render | Ảnh full-res đúng phần tử tranh chấp (cột/field/label), KHÔNG cắt cụt |
   | Thao tác/state | Kết quả thao tác thật — toast (MutationObserver) / network status của chính thao tác đó |
   | Absence ("phải báo lỗi X nhưng không") | Tự chạy đúng thao tác + chứng minh observer/network/explainErrors đều RỖNG |
   | Filter/search/count | Baseline + query phân biệt + số bản ghi thực (vd 3 · "QA"→3 · "Video"→1) |

   **Mở đọc lại pixel/log của file, đối chiếu TÊN file ↔ nội dung ↔ claim** — tên "toast-loi.png" mà pixel là form trống = INVALID, phải re-verify.
2. **Artifact BLOCKER:** chứng minh đã thử **cạn kiệt** mọi surface accessible mà thao tác vẫn không tồn tại / không vào được. **Bảng BẮT BUỘC** (không phải ví dụ): vai trò × surface × URL/menu × account × kết quả × ảnh path — còn ô chưa thử = chưa được kết luận cạn kiệt. Trước blocker phải đóng mọi tiền đề tạo được (§Nguyên tắc 4). **Nhóm A–F** (CLAUDE.md): A "thiếu seed" **CẤM** ghi sheet; chỉ B/C/D/E/F ghi được, riêng **F (lý do khác) là hộp mở dễ bị lạm dụng để né test → BẮT BUỘC hỏi user trước**. **CẤM lách bằng cách gán D/E/F cho tiền đề tạo được.** Script chỉ chặn nhãn nhóm, **không kiểm bảng** → bảng phải điền TRƯỚC khi gọi script. Riêng **evidence rỗng**: không điền bảng, artifact = log exit 3.

**Cấm:** ghi verdict khi chưa có 1 trong 2 artifact. "Đọc SRS thấy đúng/sai" hay "video đối tác cho thấy" KHÔNG thay được artifact real-data — chỉ là input bổ trợ.

**External vs Internal — quyết TRƯỚC khi gán `BA confirm`** (bug liên quan kết nối ngoài): chỉ gán External sau khi đã **loại trừ mọi tín hiệu Internal**; còn ≥1 tín hiệu chưa loại trừ → KHÔNG được punt.
- **External → BA confirm** (sau khi đã chứng minh cạn kiệt CMS): thao tác CHỈ quan sát được trên chuyên trang DN/NHT đăng nhập **VNeID**, HOẶC phụ thuộc cơ chế **PULL Cổng PLQG**.
- **Internal → PHẢI verify trên CMS** (KHÔNG được punt): thao tác của Cán bộ, **sinh thông báo nội bộ**, cập nhật trạng thái, CRUD màn CMS, audit-log. Thông báo do 1 hành động nội bộ sinh ra là internal — verify được trên CMS dù đối tác quay ở portal.

## Viết note sheet cho đối tác (partner-facing) — bug-report riêng cho dev

**Định dạng:** tiếng Việt **có dấu** + **gạch đầu dòng** (`\n`). Nội dung theo bảng mẫu dưới.

**🔴 Tham chiếu theo VERDICT (bắt buộc) — KHÔNG áp đồng loạt UC cho mọi note:**
- **`Reject` / `Resolved` → note CHỈ dùng UC + mô tả bằng lời** (người đọc chính là đối tác). CẤM ghi mã FR (`FR-<module>-NN`), `BR-xx`, số dòng SRS, mã màn `SCR/MH-xx`, jargon (API 200, field snake_case, CRUD) — vô nghĩa với đối tác.
- **`Open` / `BA confirm` → note PHẢI giữ `FR-<module>-NN (UCxx) §mục (dòng N)` + BR (nếu có)** (người đọc chính là dev/BA, cần reference chính xác). Vẫn mô tả bằng lời dễ hiểu.
- **Lấy UC:** mở đúng mục SRS của chức năng đang test, đọc dòng `**UC Reference:** UC NN` — KHÔNG hardcode bảng map của module khác. Mục SRS không có `UC Reference` → dùng tên chức năng + section + số dòng SRS, ghi rõ "không có mã UC/FR trong SRS".
- **Dẫn chứng cụ thể > câu đệm:** `Reject` phải trích **đúng thông báo/trạng thái web đang hiển thị** (vd "Email không hợp lệ"). CẤM câu đệm rỗng kiểu "đúng như phản ánh", "hệ thống hoạt động bình thường" mà không kèm bằng chứng.

**Mẫu note ngắn theo verdict (không copy máy móc):**

| Verdict | Dòng đầu | Bắt buộc có | Reference |
|---|---|---|---|
| `Open` | `✅ Bug ĐÚNG – chuyển dev.` | web sai gì · expected theo SRS · verify account/data · Bug ID | Giữ `FR/UC/BR/dòng` |
| `Reject` | `❌ Không phải bug.` | **chứng minh** đối tác thao tác/hiểu sai · web đúng SRS · `→ Đối tác kiểm tra lại.` (chỉ khi CHỨNG MINH được đối tác sai) | Chỉ UC/tên chức năng, KHÔNG FR/dòng/jargon |
| `Resolved` | `☑️ Đã kiểm tra lại — không tái hiện.` | đối tác có bằng chứng nhưng lỗi không tái hiện · đã re-verify live · chức năng &lt;tên case&gt; chạy bình thường | Chỉ UC/tên chức năng, KHÔNG FR/dòng/jargon |
| `BA confirm` | `⚠️ Cần BA xác nhận.` | actual đối tác/web đang đúng · expected đối tác khác SRS/silent · câu hỏi BA cụ thể | Giữ `FR/UC/BR/dòng` |

**Cấm:** viết không dấu, câu dài dính liền, mô tả mơ hồ ("không giống thiết kế" mà không nói thiếu gì); **nhét chi tiết nội bộ** (video đối tác quay, lịch sử BA chốt, mã màn MH-xx, so sánh 2 môi trường → đẩy hết vào `reverify-audit/`). Note chỉ nói web hiện tại đúng/không đúng vs SRS.

## Open → bug-report

- **Open** → **Bug ID = `BUG-<mã TC>`** (vd `BUG-KTDGKQHT_01`; đặt tên file ảnh theo Bug ID) + 1 entry vào file bug-report gộp (template `output/template/bug-report-template.md`, đúng 6 sections) + ≥1 screenshot trong `image/`. `Reject`/`BA confirm`/`Resolved` không vào bug-report nhưng **lưu evidence audit** (file đã xem + frame + screenshot web + SRS line; `Resolved` kèm artifact re-verify LIVE).
