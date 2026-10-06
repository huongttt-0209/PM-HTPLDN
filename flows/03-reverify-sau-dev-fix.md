# FLOW 03 — Re-verify sau khi dev báo đã fix

**Dùng khi bug đã có hồ sơ nội bộ**, ở một trong hai nhánh:

- **Re-verify dev fix:** có bug entry + khối `CÁCH VERIFY`, dev vừa báo fix.
- **Tái xác nhận trên môi trường khác:** đã Pass ở môi trường nguồn, nay cần xác nhận trên môi trường đích.
  Nhánh này có thể không còn khối `CÁCH VERIFY`; dùng bug entry + dấu vết Pass trước + SRS hiện tại để khôi
  phục đúng phép thử cũ.

Bug chưa có hồ sơ nội bộ hoặc chưa từng khóa cách đo → dùng
[FLOW 04](04-verify-bug-dev-fix-khong-ho-so.md).

Nguyên tắc thời gian của flow này:

> **Pass phải chạy hết các vế và biến thể đã khóa. Reopen được dừng ngay khi một vế bắt buộc FAIL trên đúng
> tiền đề và đã được kiểm chéo độc lập.** Không chạy tiếp chỉ để hoàn thành ma trận hoặc làm hồ sơ dày hơn.

---

## ĐẦU VÀO TỪ PROMPT

**Bắt buộc để verify:** nguồn case + expected gốc · phạm vi · nhánh chạy · đúng đường dẫn SRS hiện hành · bug
entry/dấu vết Pass trước · tài khoản · môi trường. Thiếu dữ kiện làm thay đổi chuẩn chấm hoặc không thể dựng
đúng tiền đề → Chưa chốt đúng case đó và hỏi user; cấm tự đoán.

**Tùy chọn:** bằng chứng cũ · mẫu đầu ra · công cụ seed/bắt thông báo. Thiếu tùy chọn → tiếp tục nếu vẫn đo và
kết luận được.

**Mọi cập nhật ra ngoài phép đo** — Sheet/Drive/file nào, trường nào, giá trị nào, dùng phương tiện nào — do
prompt quyết định. Prompt không yêu cầu thì không cập nhật. Flow chỉ tạo verdict logic và nội dung căn cứ;
không định nghĩa mapping, cột, dropdown, đường dẫn, thứ tự ghi hay công cụ ghi.

**Ảnh/video trên Sheet bug:** chỉ tạo, tải lên và gắn ảnh/video mới khi kết luận **Reopen** hoặc xác nhận **bug
mới**. Với Pass/Hiện tại đạt/Không phải lỗi/Cần BA/Chưa chốt/candidate, không tạo ảnh chỉ để làm bằng chứng
verify và không điền cột ảnh; giữ nguyên nội dung cũ nếu có. Yêu cầu “cập nhật Sheet” chung không đồng nghĩa
phải gắn ảnh. Luật này không bỏ phép đo, đối chứng độc lập hoặc việc mở đọc output/tệp bắt buộc.

---

# GIAI ĐOẠN A — khóa phép thử, chưa mở màn đang tranh chấp

## Thứ bậc nguồn

1. **SRS tại đúng đường dẫn prompt cung cấp** quyết định hệ thống phải làm gì.
2. **Expected/bug gốc** quyết định phạm vi vấn đề đang re-verify.
3. **Khối `CÁCH VERIFY` hoặc dấu vết Pass trước** quyết định cách tái hiện và phép đo đã khóa; nó không được
   thêm yêu cầu trái SRS hiện tại.
4. Note Sheet, phản hồi dev, ảnh cũ, thư BA và báo cáo cũ chỉ là manh mối để tìm đúng nội dung trên ba nguồn
   trên; không tự quyết verdict.

Mỗi vế bug phải đối chiếu lại với SRS hiện tại trước khi đo:

| Quan hệ expected gốc ↔ SRS hiện tại | Xử lý |
|---|---|
| `MATCH` | Được re-verify theo đường đo đã khóa |
| `DIFF` | Cấm Pass vế đó; kết luận Cần BA và ghi nguyên hai phía |
| `GAP` — SRS im lặng/tự mâu thuẫn | Cấm Pass/Reopen vế đó; kết luận Cần BA và tạo câu hỏi cụ thể |

Một vế có phần chung và phần mâu thuẫn thì tách nhỏ: phần cả expected lẫn SRS cùng yêu cầu là `MATCH`; phần
khác nhau là `DIFF`. Chỉ phần `MATCH` mới được Pass/Reopen bằng phép đo.

Nếu dev đang đúng SRS nhưng expected gốc khác SRS, ghi rõ:
`DEV ĐANG ĐÚNG SRS HIỆN HÀNH · EXPECTED GỐC KHÁC SRS: …`; đây không phải Pass.

Chỉ mở lại **các đoạn SRS được vế bug hoặc `CÁCH VERIFY` dẫn tới**. Nếu số dòng đã lệch, tìm lại theo mã
requirement/nội dung rồi đọc trọn bảng hoặc đoạn liên quan. Không diff cả module, quét mọi dấu thay đổi hoặc
tái lập toàn bộ tiêu chí nếu không có dấu hiệu nguồn đã đổi.

## BƯỚC 0 — chốt lô và nguồn canonical

1. Lấy đúng danh sách/tiêu chí lọc từ prompt; in vị trí nguồn + mã case.
2. Mỗi case, xác định **một nguồn canonical cho cách đo**:
   - Nhánh dev fix: khối `CÁCH VERIFY` trong bug entry do prompt chỉ định; note ở nơi khác chỉ dùng đối chiếu
     khi prompt tuyên bố đó là nguồn canonical.
   - Nhánh môi trường đích: bug entry + dấu vết Pass ở môi trường nguồn + SRS hiện tại.
   - Không có nguồn đủ để xác định PASS/FAIL đo được → Chưa chốt; không tự viết một bộ test mới.
3. Từ kết quả Reopen gần nhất, tách rõ:
   - **phần còn lỗi** → phải đo lại;
   - **phần đã đạt / ghi rõ không cần test lại** → không đo lại để ra verdict, trừ khi nó là tiền đề bắt buộc
     để đi tới phần còn lỗi.
4. Nhóm case cùng module/env/role để đọc SRS một lượt và dùng chung phiên đăng nhập.
5. Ghi env + định danh bản dựng/deploy một lần đầu lô. Chỉ kiểm lại khi có deploy, đổi phiên, hoặc hành vi cho
   thấy có thể đang chạy bản khác.

Trong ngữ cảnh làm việc, khóa mỗi vế còn phải đo bằng một dòng; **không tạo file tiêu chí riêng**:

`C1 · lỗi còn lại · SRS file:dòng · MATCH/DIFF/GAP · thao tác · PASS khi · FAIL khi · biến thể bắt buộc`

Biến thể bắt buộc chỉ được lấy từ expected gốc, SRS hoặc nguồn canonical. Không tự bổ sung role, nguồn dữ
liệu, trạng thái, cỡ lô hoặc loại tệp chỉ vì “có thể khác”.

Nếu mọi vế đều `DIFF/GAP` và câu hỏi BA đã rõ, chốt Cần BA ngay ở Giai đoạn A. Không mở app chỉ để tạo thêm
bằng chứng. Case còn vế `MATCH` thì sang Giai đoạn B cho đúng vế đó.

---

# GIAI ĐOẠN B — đo đúng phần còn lỗi

## Chuẩn bị tối thiểu

1. Đăng nhập đúng vai trò của vế đang đo. Tài khoản quản trị chỉ được ra verdict khi quản trị chính là vai trò
   cần kiểm; nếu không chỉ dùng để chuẩn bị dữ liệu.
2. Tải lại trang trước lô đo hoặc sau khi có deploy/đổi phiên.
3. Ưu tiên dữ liệu QA có sẵn nếu đúng role · trạng thái · env và chưa bị thay đổi. Chỉ tạo phần còn thiếu.
4. Chỉ seed qua cách prompt cho phép và khi seed không phải hành vi đang tranh chấp. Seed xong mở UI xác nhận
   tiền đề cuối; khai bản ghi nào đã đổi, đổi gì và env nào. Không đụng dữ liệu đối tác.
5. Nếu bug liên quan dữ liệu sinh sau thao tác ghi hoặc fix không hồi tố, dùng bản ghi/thao tác **mới sau bản
   fix**. Không lấy dữ liệu cũ đóng băng để Reopen oan.

Hoàn nguyên dữ liệu QA khi prompt/chính sách môi trường yêu cầu và có đường an toàn, nhưng coi đó là cleanup,
không biến thao tác hoàn nguyên thành một phép regression mới trừ khi chính bug đang kiểm hành vi đó.

## Chạy

1. Chạy đúng đường UI trong nguồn canonical tới hành động từng sinh lỗi. Không chạy lại các vế đã được kết quả
   gần nhất ghi rõ là đã đạt, trừ phần tối thiểu cần làm tiền đề.
2. Hành động đang tranh chấp phải thực hiện bằng UI thật. API/DB/log chỉ làm đối chứng, không thay thao tác UI.
3. Đối chứng bằng **một phương pháp độc lập phù hợp với claim**:
   - trạng thái/lưu dữ liệu → đọc lại bản ghi hoặc response;
   - hiển thị → đối chiếu dữ liệu nguồn;
   - tệp xuất/tải lên → mở chính tệp hoặc đọc lại metadata/nội dung liên quan.
   Bấm lại cùng nút không phải phương pháp độc lập.
4. Chỉ giữ quan sát/số liệu quyết định verdict; setup trung gian ghi ID + trạng thái là đủ. Pass không chụp ảnh;
   nếu verdict phụ thuộc tệp thì vẫn phải mở đọc nhưng không tải lên/gắn Sheet. Khi Reopen hoặc có bug mới, một
   artifact lỗi có thể chứng minh nhiều vế. Không lặp thao tác chỉ để săn lại ảnh/toast.
5. So đúng các điều kiện có thể đổi kết quả: role, trạng thái, dữ liệu và input/filter. Chênh lệch liên quan
   chưa giải quyết được → Chưa chốt; không mở rộng sang mọi nhánh có thể tưởng tượng.

## Luật dừng sớm

### Khi có FAIL

Một vế `MATCH` được coi là FAIL khi:

- chạy đúng tiền đề và thao tác đã khóa;
- vi phạm điều kiện FAIL/PASS bắt buộc;
- có quan sát quyết định + một đối chứng độc lập;
- sai lệch không phải do env, tài khoản, dữ liệu test hoặc bản dựng chưa xác định.

Đủ bốn điều kiện → **Reopen và dừng các lượt/biến thể còn lại**. Chỉ tiếp tục khi:

1. cần một bước ngắn để phân biệt lỗi sản phẩm với blocker môi trường/dữ liệu;
2. claim vốn là lỗi không ổn định và nguồn canonical quy định số mẫu tối thiểu;
3. case có vế `DIFF/GAP` độc lập cần đo hiện trạng để đặt câu hỏi BA;
4. prompt yêu cầu hoàn tất toàn bộ độ phủ dù đã có FAIL.

Trước khi dừng, ghi nhận mọi vế bắt buộc có thể kết luận từ **chính thao tác/artifact đã có**; không mở thêm
vòng UI hoặc dựng thêm dữ liệu để tìm lỗi thứ hai.

Không cần đóng mọi GAP hay chạy đủ mọi biến thể để chứng minh Reopen. Nếu lỗi sản phẩm ở chính luồng bắt buộc
làm chặn các bước sau, vẫn Reopen và ghi rõ phần downstream chưa đo; nếu blocker nằm ngoài sản phẩm thì Chưa chốt.

### Khi chưa có FAIL

Muốn Pass phải chạy hết:

- mọi vế `MATCH` còn phải đo;
- mọi biến thể được nguồn canonical/SRS/expected gốc nêu đích danh;
- mọi điều kiện PASS bắt buộc;
- đối chứng độc lập cho các quan sát quyết định.

Nguồn canonical ghi “ít nhất 2 mẫu” thì đo 2 mẫu hợp lệ là đủ; flow không tự nâng thành 3 dạng. Không đủ biến
thể bắt buộc để đo → Chưa chốt, trừ khi một biến thể khác đã FAIL đủ căn cứ để Reopen theo luật trên.

---

## Bug mới tự lộ — không exploratory

Trong lúc chạy tiền đề, thao tác hoặc đọc output bắt buộc của case, không được bỏ qua sai lệch rõ ràng trong
chính màn/phản hồi/tệp đang quan sát. Được đọc một lượt phần đang hiển thị, nhưng không bấm thử từng field/nút,
không chạy checklist regression và không mở chức năng khác chỉ để tìm bug.

1. Mở SRS thật, dẫn `file:dòng`. SRS im lặng → candidate; SRS mâu thuẫn → candidate + câu hỏi BA. Cả hai:
   không log như bug đã xác nhận.
2. Tra phiếu trùng trước khi đo thêm. Đã có phiếu → liên kết và dừng xử lý hiện tượng này; tiếp tục hoàn tất
   case gốc.
3. Artifact sẵn có chưa đủ → ngoài các phép đo bắt buộc của case, cả case chỉ được thêm tối đa **1 phép xác nhận**
   cho bug mới. Phép xác nhận giữ nguyên role/dữ liệu/bộ lọc; chỉ được replay đúng thao tác, hoặc đọc một kết quả/
   side effect trực tiếp đã phát sinh từ cùng bản ghi/giao dịch. Thao tác có thể làm thay đổi dữ liệu/trạng thái
   nghiệp vụ hoặc tạo thêm đầu ra nghiệp vụ mới — như gửi mail/thông báo, tạo hoặc sửa bản ghi, giao dịch hay tệp —
   thì **KHÔNG replay**; chỉ đọc lại kết quả/side effect đã có. Không seed, không thực hiện chức năng hoặc luồng
   nghiệp vụ khác.
4. Đủ SRS + artifact + đối chứng độc lập → log bug mới và tạo `CÁCH VERIFY`. Chưa đủ sau phép xác nhận → candidate,
   không điều tra tiếp.
5. Nhiều hiện tượng cùng lộ: hiện tượng đủ bằng chứng sẵn có thì log; hiện tượng cần thêm thao tác ghi candidate,
   không cộng thêm lượt xác nhận.
6. Bug mới chỉ đổi verdict case gốc khi làm điều kiện PASS không đạt hoặc chặn chính phép đo bắt buộc; trường hợp
   khác log riêng.

Candidate: `<hiện tượng> · xuất hiện tại <bước> · artifact <...> · còn thiếu <...> để xác nhận`.
Nơi lưu, mã bug và cách cập nhật theo prompt; không có chỉ dẫn thì đưa vào bàn giao cuối, cấm tự suy đích/mã.

---

# Chốt

## Verdict logic

| Verdict | Khi nào |
|---|---|
| **Pass** | Mọi vế đều `MATCH`; đã chạy hết phạm vi/biến thể bắt buộc; tất cả đạt và có đối chứng quyết định |
| **Reopen** | Ít nhất một vế `MATCH` FAIL đủ bốn điều kiện của luật dừng sớm; gồm cả fix một phần |
| **Reopen + Cần BA** | Có vế `MATCH` FAIL và đồng thời có vế độc lập `DIFF/GAP` |
| **Cần BA** | Không có vế đủ Reopen nhưng expected gốc khác SRS hiện tại, hoặc SRS im lặng/tự mâu thuẫn |
| **Chưa chốt** | Blocker khách quan, nguồn canonical mơ hồ, hai phép đo mâu thuẫn hoặc thiếu biến thể quyết định để Pass |

Pass/Reopen chỉ có hiệu lực trên env + bản dựng/thời điểm đã đo. Khác môi trường không tự động đổi verdict;
ghi rõ giới hạn hiệu lực. Không viết “fix đã có tác dụng” nếu không có bằng chứng trạng thái trước fix; chỉ kết
luận hiện trạng đạt/sai so với SRS.

## Nội dung kết quả cho người đọc

Mục này chỉ chuẩn hóa cách diễn giải; prompt vẫn quyết định nơi lưu. Dòng đầu luôn dùng icon trung tính `📌`,
không dùng lại icon của các mục chi tiết:

- `📌 KẾT QUẢ CHUNG: ĐÃ HẾT LỖI` — hoặc `HIỆN TẠI ĐẠT` nếu không có bằng chứng trạng thái lỗi trước đó
- `📌 KẾT QUẢ CHUNG: CÒN LỖI (REOPEN)`
- `📌 KẾT QUẢ CHUNG: CẦN BA XÁC NHẬN`
- `📌 KẾT QUẢ CHUNG: CÒN LỖI (REOPEN) + CẦN BA XÁC NHẬN`
- `📌 KẾT QUẢ CHUNG: CHƯA THỂ KẾT LUẬN`

Sau đó chỉ ghi các mục có nội dung, theo thứ tự:

| Mục | Phải trả lời rõ |
|---|---|
| `❌ CÒN LỖI — <hành vi sai cụ thể>` | Kết quả mong đợi · kết quả thực tế + số liệu quyết định · dev cần sửa |
| `❓ CẦN BA XÁC NHẬN — <điểm chưa chốt>` | Expected ↔ SRS · kết quả thực tế · một câu hỏi BA trả lời trực tiếp · ghi rõ chưa chấm đạt/lỗi |
| `✅ ĐÃ HẾT LỖI — <lỗi gốc>` | Kết quả mong đợi · kết quả thực tế + số liệu quyết định; chỉ dùng khi có bằng chứng lỗi cũ |
| `✅ HIỆN TẠI ĐẠT — <hành vi>` | Kết quả mong đợi · kết quả thực tế; dùng khi phép đo đạt nhưng không có bằng chứng tin cậy về lỗi trước đó |
| `⏸ CHƯA CHỐT — <phần chưa kết luận>` | Kết quả cần kiểm tra · kết quả thực tế/điều kiện còn thiếu · dữ kiện cần bổ sung |
| `🔎 PHẠM VI ĐÃ ĐO` | URL môi trường · bản dựng/thời điểm · role · dữ liệu/biến thể quyết định |

Dùng lời người đọc hiểu; mã `C4a`, `MATCH/DIFF/GAP`, enum, tên biến script hoặc định danh bundle chỉ để trong
hồ sơ audit, trừ khi thật sự cần truy vết cho dev/BA. Đặt SRS và số liệu/artifact lỗi cạnh kết luận nó chứng
minh. Không tạo mục rỗng, lặp bằng chứng hoặc trộn ghi chú ngoài phạm vi vào các mục chính.

Mỗi mục có phép đo web chỉ ghi ngắn gọn `Kết quả mong đợi` và `Kết quả thực tế`; số liệu quyết định đặt ngay
trong kết quả thực tế. `CÒN LỖI` thêm `Dev cần sửa`; `CẦN BA` thêm câu hỏi; `CHƯA CHỐT` thêm dữ kiện cần bổ
sung. Lịch sử điều tra để trong hồ sơ audit; cột ảnh chỉ nhận artifact lỗi theo luật ở đầu flow, không dùng
cho Pass.

```text
📌 KẾT QUẢ CHUNG: <verdict>
<icon> <MỤC KẾT QUẢ> — <hành vi>
- Kết quả mong đợi: <hành vi cần đạt>.
- Kết quả thực tế: <hành vi đo được + số liệu quyết định>.
🔎 PHẠM VI ĐÃ ĐO: <URL môi trường> · <thời gian/bản dựng> · <vai trò>.
```

```text
❌ CÒN LỖI — <nêu chính xác hành vi đang sai>
- Kết quả mong đợi: <expected và SRS file:dòng quy định gì>.
- Kết quả thực tế: <đúng tiền đề · output sai · số đo/ví dụ quyết định · phạm vi tái hiện>.
- Dev cần sửa: <kết quả quan sát được phải đạt; không đoán nguyên nhân, không ép cách triển khai>.
```

Nghĩa icon cố định: `📌` tổng kết · `❌` còn lỗi/xác nhận là bug · `❓` cần BA · `✅` đạt/không phải lỗi ·
`⏸` chưa đủ căn cứ · `🔎` phạm vi đã kiểm tra. `⚠️` chỉ dùng cho caveat/cảnh báo, không dùng làm verdict.
Cấm đảo nghĩa icon theo cách diễn đạt của verdict.

**Reopen và bug mới đã xác nhận bắt buộc có `CÁCH VERIFY`** để vòng sau không tự chế phép đo; các verdict khác
không cần, trừ khi prompt yêu cầu. Nơi lưu do prompt quyết định. Nếu lưu cùng nội dung kết quả, đặt khối này
sau đường phân cách vì đây là bàn giao kỹ thuật, không phải phần giải thích verdict.

```text
── CÁCH VERIFY sau Dev fix ──
Phạm vi: <chỉ vế còn lỗi + expected/SRS file:dòng>.
Precondition:
- <URL môi trường · vai trò · màn · trạng thái/input bắt buộc>.
- <dữ liệu phân biệt được hành vi lỗi cũ với hành vi cần đạt>.
1) <đường UI ngắn nhất tới hành vi lỗi>
2) <thao tác và output cần quan sát>
Đối chứng độc lập: <đọc lại đúng bản ghi/giao dịch/request/tệp của lượt trên và nối được với UI>.
✅ PASS khi: <mọi điều kiện/biến thể bắt buộc đều đạt và bằng chứng phân biệt được hành vi mới với lỗi cũ>.
❌ FAIL nếu: <ít nhất một yêu cầu bắt buộc sai trên đúng tiền đề, có đối chứng độc lập>.
⏸ CHƯA CHỐT khi: <thiếu tiền đề/dữ liệu phân biệt; không nối được UI với đối chứng; hoặc hai phép đo mâu thuẫn>.
⚠️ Caveat: <bẫy có bằng chứng; không có thì bỏ>.
```

Mỗi bước phải trả lời trực tiếp một phần của vế còn lỗi. Không Pass bằng dữ liệu mà hành vi cũ và mới đều có
thể cho cùng kết quả, khi mới đo một phần hoặc thiếu biến thể bắt buộc. Không Fail khi sai tiền đề, thiếu dữ
liệu hoặc chưa nối được bằng chứng. Lặp lại cùng tín hiệu không phải đối chứng; trường hợp biên chưa được
expected/SRS quy định → Cần BA. Đủ một FAIL hợp lệ thì Reopen, không chạy thêm để tìm lỗi khác.

Khi Reopen, khối mới chỉ giữ vế còn lỗi và vế chưa đo; bỏ vế đã đạt, không thêm biến thể ngoài nguồn. Khi Pass,
không cần tạo lại khối này trừ khi prompt yêu cầu lưu lịch sử đầy đủ.

**Cổng hỏi BA:** Chỉ hỏi khi đã mở đúng SRS trong chính case, đọc trọn đoạn/bảng liên quan và vẫn còn `DIFF/GAP`;
không hỏi chỉ từ mô tả, web, note cũ hoặc suy đoán. Câu hỏi phải kèm expected ↔ SRS `file:dòng`, hoặc `IM LẶNG`
kèm vị trí đã rà, và chỉ cần BA chốt một quyết định. Dùng lại trích dẫn đã có trong case, không quét toàn module;
thiếu dữ liệu, tài khoản, môi trường hoặc quyền truy cập là blocker vận hành, không hỏi BA.

## Cổng tự kiểm trước khi chốt

1. Chuẩn chấm có bám đúng SRS hiện tại và expected gốc không?
2. Đã đo đúng phần còn lỗi, hay vô tình chạy lại phần đã đạt/kiểm chức năng kế bên?
3. Reopen đã có một FAIL hợp lệ + đối chứng độc lập chưa; nếu có, vì sao còn chạy tiếp?
4. Pass đã phủ hết đúng các vế/biến thể được nguồn canonical yêu cầu chưa?
5. Căn cứ quyết định verdict (số liệu/response/tệp hoặc artifact lỗi) đã được đọc lại chưa? Pass không cần ảnh.
6. Người không tham gia phiên đo có phân biệt ngay phần còn lỗi, phần cần BA, phần đã đạt và phần chưa đo không?

Flow kết thúc ở verdict + nội dung căn cứ. Nơi lưu, trường, giá trị, cách cập nhật và format báo cáo theo prompt;
chúng không được làm thay đổi verdict hoặc buộc mở thêm phép đo. Nếu prompt không quy định format, bàn giao gọn:
kết quả từng case · bug mới/candidate · dữ liệu đã seed/thay đổi · case Chưa chốt và dữ kiện cần bổ sung.

Nếu trong đợt chạy có bằng chứng chính flow làm giảm chất lượng kết quả hoặc gây thao tác thừa lặp lại, thêm
`CẢI TIẾN FLOW: <vấn đề> · <ảnh hưởng> · <rule/chỗ cần xem lại>`. Không có thì bỏ mục; không đo thêm chỉ để
đánh giá flow và không tự sửa flow trong phiên verify.
