# FLOW 02 — Áp quyết định của BA

**Dùng khi:** BA đã trả lời các case chốt *"cần BA quyết"* — từ [FLOW 01](01-verify-bug-doi-tac.md),
hoặc từ [FLOW 03](03-reverify-sau-dev-fix.md)/[FLOW 04](04-verify-bug-dev-fix-khong-ho-so.md) khi re-verify
lộ ra phần lỗi mà đặc tả chưa quy định.

**Bước này KHÔNG test lại web.** Việc của QA: dịch quyết định của BA thành verdict, và viết **CÁCH VERIFY**
đủ cụ thể để FLOW 03 re-verify không sai.

> Flow chỉ nói **quy trình + cách check**. Thông tin dự án do **prompt truyền vào**.
> Thiếu tham số bắt buộc → **DỪNG hỏi user, cấm đoán**.

---

## PROMPT MẪU

```
Áp dụng @flows/02-ap-quyet-dinh-ba.md
- Sheet: <link>   | Tab: <tên tab>
- Ô mã case: "<...>" | Ô trạng thái dev: "<...>" | Ô kết quả QA: "<...>" | Ô note: "<...>"
- Từ vựng: là bug="<...>" · không phải bug="<...>" · nhãn chờ BA="<...>"
- File BA TRẢ LỜI: <đường dẫn>        ← quyết định của BA, KHÔNG phải file QA đi hỏi
- Bug report: <file gộp>  | Ảnh: <thư mục image/>
- Đặc tả (SRS): <đường dẫn>
- Công cụ ghi kết quả: <lệnh/script>
- Phạm vi: <danh sách mã case | "mọi case đang chờ BA">
```

## 🔴 Phân biệt 2 loại file — nhầm là cập nhật sai toàn bộ

| File | Là gì | Dùng ở flow này? |
|---|---|---|
| File QA **đi hỏi** BA (`ba-confirmation-needed-*`) | chỉ có câu hỏi | ❌ **KHÔNG** |
| File BA **trả lời** (`phan-hoi-ba-*`, `ba-response-*`) | có quyết định | ✅ đúng file cần |

Prompt đưa file chỉ toàn câu hỏi → **DỪNG, hỏi lại user**.

**Tham số khác:** tab phải khớp đợt của bug (có cả `gid=` lẫn tên tab bằng chữ → resolve rồi so sánh,
lệch → DỪNG) · định vị ô bằng **TÊN HEADER** · map bug ↔ dòng qua **ô mã case** (Bug ID = `BUG-<mã case>`).

## Vai trò 4 ô

| Vai trò | Flow này ghi gì |
|---|---|
| **ô mã case** | không ghi — chỉ để map |
| **ô trạng thái dev** | 🔴 **CHỈ** đổi khi ô đang mang nhãn *"chờ BA"*. Giá trị khác (dev đã xử lý) → **GIỮ NGUYÊN** |
| **ô kết quả QA** | verdict theo quyết định BA |
| **ô note** | §Layout — **người đọc đổi theo verdict** |

---

## Vòng lặp MỖI BUG — **hồ sơ trước, bảng sau**

**CẤM gom lô.** Xong 1 bug → ghi → rồi mới sang bug kế.

1. Đọc đủ **bug gốc + quyết định BA + expected + đúng SRS hiện tại** do prompt cấp.
2. Đối chiếu từng nội dung BA chốt với expected và SRS hiện tại:
   - **MATCH** — ba nguồn không mâu thuẫn → tiếp tục.
   - **DIFF/GAP** — SRS chưa cập nhật, im lặng hoặc khác BA/expected → ghi nguyên các phía kèm `file:dòng`,
     kết luận `Chưa chốt — BA/SRS chưa đồng bộ` và gửi BA xác nhận. Không dùng riêng một nguồn để tạo verdict
     hoặc `CÁCH VERIFY`.
   - Không hỏi lại nội dung nghiệp vụ BA đã trả lời; chỉ hỏi BA xác nhận nguồn có hiệu lực hoặc yêu cầu cập
     nhật SRS. Chỉ tiếp tục khi các nguồn đã đồng bộ.
3. 🔴 **BA trả lời chưa đủ rõ → DỪNG, hỏi lại user. CẤM đoán.**
   **Đủ rõ = trả lời được cả 3 câu** từ chính văn bản BA, không suy diễn:
   - Hành vi **đúng** là gì (không phải chỉ "hiện tại sai")?
   - Áp cho **vai trò / trạng thái / trường hợp nào** — mọi trường hợp hay chỉ một nhánh?
   - Nhìn vào đâu để biết đã đúng — **cái gì quan sát được** đổi?

   Thiếu 1 trong 3 → chưa viết được `✅ PASS khi:` đo được ⇒ hỏi lại. Đây là chỗ hỏng đắt nhất: cách
   verify mơ hồ → FLOW 03 chấm sai → bug đóng oan hoặc mở oan.

4. Phân loại theo quyết định đã qua hai cổng trên:

   | Phân loại | ô kết quả QA | ô trạng thái dev |
   |---|---|---|
   | **Là bug, cần dev fix** | `Open` | `Open` — chỉ khi đang *"chờ BA"* |
   | **Không phải bug** | `Reject` | `Reject` — chỉ khi đang *"chờ BA"* |

   *(Từ vựng mặc định; dự án khác → prompt khai. Giá trị không có trong dropdown → **DỪNG**, cấm bịa.)*
5. **Là bug → thêm entry bug-report + copy khối CÁCH VERIFY vào entry TRƯỚC** (§Đầu ra).
6. **Rồi mới** soạn note → ghi dòng đó → **đọc lại xác nhận** → bug kế.

---

Quy ước icon trong note: `📌` chỉ dùng cho kết quả chung · `❌` còn lỗi/xác nhận là bug · `❓` cần BA ·
`✅` đạt/không phải lỗi · `⏸` chưa đủ căn cứ · `🔎` phạm vi đã kiểm tra. `⚠️` chỉ dùng cho caveat/cảnh báo
trong `CÁCH VERIFY`, không dùng làm verdict.

## Layout note — LÀ BUG

Người đọc chính là **dev/BA** → **giữ** reference đặc tả (mã chức năng, mục, số dòng).
Ô note vẫn là ô đối tác xem được → không nhét chi tiết nội bộ (video đối tác quay, so sánh 2 môi trường).

```
📌 KẾT QUẢ CHUNG: XÁC NHẬN LÀ LỖI — CHUYỂN DEV

❌ CÒN LỖI — <hành vi BA xác nhận là lỗi>
- Kết quả mong đợi: <hành vi BA chốt, đã khớp expected và SRS file:dòng>.
- Dev cần xử lý: <hành vi cần đạt, không ép cách triển khai>. <mức độ nếu có căn cứ>.

── CÁCH VERIFY sau Dev fix ──
Phạm vi: <chỉ vế còn lỗi + BA/expected/SRS file:dòng đã đồng bộ>.
Precondition:
- <URL môi trường · vai trò · màn · trạng thái/input bắt buộc>.
- <dữ liệu phân biệt được hành vi lỗi cũ với hành vi cần đạt>.
1) <đường UI ngắn nhất tới hành vi cần kiểm>
2) <thao tác và output cần quan sát>
Đối chứng độc lập: <đọc lại đúng bản ghi/giao dịch/request/tệp của lượt trên và nối được với UI>.
✅ PASS khi: <mọi điều kiện/biến thể bắt buộc đều đạt và bằng chứng phân biệt được hành vi mới với lỗi cũ>.
❌ FAIL nếu: <ít nhất một yêu cầu bắt buộc sai trên đúng tiền đề, có đối chứng độc lập>.
⏸ CHƯA CHỐT khi: <thiếu tiền đề/dữ liệu phân biệt; không nối được UI với đối chứng; hoặc hai phép đo mâu thuẫn>.
⚠️ Caveat: <bẫy có bằng chứng dễ gây Pass oan/Fail oan; không có thì bỏ>.
Ảnh lỗi cũ: <đường dẫn ảnh — lấy từ file gửi BA của FLOW 01>
```

🔴 **Khối này là nguồn tiêu chí PASS/FAIL mà FLOW 03 đọc.** Ghi vào **ô note** (nơi FLOW 03 tìm) **và**
copy vào bug entry (để đọc được cả khi không mở sheet). Hai chỗ phải **giống nhau từng chữ**.

**Chất lượng `CÁCH VERIFY`:** chỉ đưa một biến thể vào khi nó thuộc đúng vế BA chốt, có căn cứ trong BA/expected
và không mâu thuẫn với SRS. Điều kiện SRS làm vế có hiệu lực là tiền đề, không phải phạm vi test mới. Mỗi bước
phải trả lời trực tiếp vế lỗi. Không Pass bằng dữ liệu mà hành vi cũ và mới đều có thể cho cùng kết quả, khi
mới đo một phần hoặc thiếu biến thể bắt buộc. Không Fail khi sai tiền đề, thiếu dữ liệu hoặc chưa nối được bằng
chứng. Lặp lại cùng tín hiệu không phải đối chứng; trường hợp biên chưa được nguồn quy định → Cần BA.

Tự kiểm: người chưa biết case có dựng đúng tiền đề, chạy đúng phạm vi và tự phân biệt PASS/FAIL/CHƯA CHỐT chỉ
bằng khối này không? Nếu không, viết lại trước khi ghi.

**Ca dễ sai:** BA chốt *"là bug"* nhưng dev đã lặng lẽ sửa trong lúc chờ BA → dòng đó có thể **đã mang
verdict bug**. Không đè (guard 3) — DỪNG, báo user, để FLOW 03 xử lý sau khi dev báo fix.

## Layout note — KHÔNG PHẢI BUG

Người đọc là **đối tác** → **bỏ** mã đặc tả/số dòng/mã màn/jargon. **Không có** CÁCH VERIFY.

```
📌 KẾT QUẢ CHUNG: KHÔNG PHẢI LỖI

✅ KHÔNG PHẢI LỖI — BA xác nhận <ngày>
- Kết quả mong đợi đúng: <yêu cầu nghiệp vụ BA đã chốt, đã khớp SRS>.
- Kết quả phía đối tác đang kỳ vọng: <điều kiện/kỳ vọng chưa đúng>.
- <cải tiến / đối tác chỉnh lại kết quả mong đợi — chỉ nếu BA có nêu>.
```

---

## Ghi kết quả

Có công cụ ghi → **bắt buộc dùng**. Chạy thử → ghi thật → **đọc lại xác nhận cả 3 ô** của đúng dòng đó.

**Bước này KHÔNG đo lại web** → công cụ **không** nên đòi ảnh bằng chứng: bắt chụp ảnh cho một bước không
quan sát gì sẽ đẻ ra **bằng chứng giả** chỉ để qua cổng. Thứ phải truy vết được là **"quyết định này lấy từ
đâu"** → công cụ đòi **đường dẫn file BA trả lời**, và **từ chối** nếu đó là file QA đi hỏi.

4 guard riêng (ngoài guard chung: khớp mã case, kiểm dropdown, in old→new, đọc lại, log giá trị cũ):

| # | Guard | Vì sao |
|:-:|---|---|
| 1 | **Ô kết quả QA phải đang mang nhãn *"chờ BA"*** — khác → DỪNG | Dấu hiệu dòng thật sự thuộc phạm vi bước này. Ghi vào dòng khác = đè nhầm kết luận khác |
| 2 | **Ô trạng thái dev chỉ ghi khi đang *"chờ BA"***; khác → giữ nguyên + cảnh báo | Đó là cột xử lý của dev |
| 3 | **Dòng đã mang verdict bug** (`Open`/`Reopen`) → **CẤM đè** | Bước này chỉ *gỡ nhãn chờ BA*. Verdict bug đã chốt là kết luận có hiệu lực — đổi thì dùng FLOW 03 |
| 4 | Verdict **là bug** mà note thiếu khối `── CÁCH VERIFY sau Dev fix ──` hoặc thiếu `Precondition:` / `✅ PASS khi:` / `❌ FAIL nếu:` → **CHẶN**. Verdict **không phải bug** mà note **có** khối đó → cũng **CHẶN** | Biến layout CÁCH VERIFY từ *lời dặn* thành *cổng máy*. Thiếu nó, FLOW 03 sẽ **tự chế tiêu chí** và chấm sai |

**Guard 4 chỉ đếm được sự có mặt của nhãn, không đo được chất lượng.** Nó chặn *bỏ trống*, không chặn
*viết cho có* (`✅ PASS khi: hiển thị đúng`). Chất lượng vẫn do 4 câu tự kiểm ở trên — công cụ nên thêm
cảnh báo khi `✅ PASS khi:` ngắn bất thường hoặc chứa từ mơ hồ (*đúng · phù hợp · hợp lý · bình thường*).

**Công cụ chặn → DỪNG, báo user.** Cấm ghi tay để lách. **Cấm viết script dùng-một-lần** cho từng
module/đợt — đó là cách thư mục công cụ phình lên hàng chục bản gần giống nhau, mỗi bản hardcode danh sách
bug, không tái dùng và không có guard đồng nhất.

> ⚠️ **Chưa có công cụ ghi cho bước này:** guard 1–4 chỉ còn là lời dặn → **báo user rõ độ tin cậy thấp
> hơn**, tự đọc lại từng ô sau khi ghi, và tự soát guard 4 bằng mắt trước khi ghi.

## Đầu ra

**BA chốt là bug** → 1 entry vào **file bug-report gộp** + **khối CÁCH VERIFY** (copy y hệt note).
Ảnh: **dùng lại ảnh lỗi FLOW 01 đã lưu** khi gửi BA — bước này không test nên **không chụp ảnh mới**.
Không có ảnh cũ → ghi rõ *"chưa có ảnh, cần bổ sung ở lần re-verify"*, đừng chụp ảnh màn hình hiện tại rồi
gọi là ảnh lỗi (ảnh sai trạng thái, còn tệ hơn không có).

**Vì sao entry bắt buộc:** BƯỚC 0 của FLOW 03 đối chiếu *dòng dev báo đã fix trên sheet* với *bug trong
file bug-report*. Bug chốt ở flow này mà không có entry → FLOW 03 báo thiếu và dừng.

**BA chốt không phải bug** → không vào bug-report, nhưng **lưu vết quyết định BA** vào hồ sơ audit (ai chốt,
ngày nào, căn cứ gì) — để lần sau đối tác hỏi lại còn dẫn được.
