# Phân tích 2 vấn đề KTDGKQHT_03 và KTDGKQHT_08 — Module Đào tạo

**Ngày:** 16/07/2026
**Nguồn issue:** Sheet UAT `7. Trợ giúp pháp lý Doanh nghiệp — UAT_TGPL Doanh Nghiệp`, Tuần 2, ngày test 06/07/2026 (dòng 291 và 296).
**Nguồn đối chiếu:** Bộ SRS `_bmad-output/planning-artifacts/srs-v3.5/` — `srs-fr-03-dao-tao.md` (FR-III-05, FR-III-17, SCR-III-02) và `srs-v3.5.md` (entity KET_QUA_DAO_TAO §3.4.3.23, bảng chuyển trạng thái Khóa học, BR-KQ-01/02).

**Trạng thái hiện tại của cả 2 issue:** Tester đánh **Fail** → Dev trả lời **"Không phải bug"** → Tester **Reopen**. Đang bế tắc.

---

## ✅ ĐÃ CHỐT — BA quyết định 16/07/2026

| QĐ | Nội dung | **BA chốt** | Ghi chú |
|---|---|---|---|
| **A** | Điểm kiểm tra nhập ở trạng thái nào | **Phương án A2** — cả "Đang diễn ra" và "Đã kết thúc" | **Khác đề xuất A1 của tôi.** Đối chiếu CSV baseline sau đó cho thấy **A2 mới đúng** — xem ô cảnh báo dưới |
| **B** | Có tách FR-III-05 thành 2 khối | **KHÔNG tách** | Giữ 1 FR, chỉ viết rõ 2 nhánh bên trong |
| **C** | Dòng hướng dẫn bảng điểm danh trống | **Đồng ý** | "Vui lòng chọn buổi học để bắt đầu điểm danh" |
| — | 3 lỗi SRS thứ cấp phát hiện thêm | **KHÔNG sửa** | Để ngoài phạm vi đợt này. Đã gỡ khỏi tài liệu + hoàn nguyên SRS về nguyên trạng |

> ### ⚠️ Đối chiếu CSV baseline sau khi chốt — phát hiện quan trọng
>
> Sau khi chị chốt A2, tôi tra CSV `Danh sách transaction_v1.1_2026-03-27.csv` (chuẩn cao hơn SRS) và phát hiện **hai điều**:
>
> **1. A2 đúng, đề xuất A1 của tôi sai.** CSV UC24 (dòng 111-117) liệt kê transaction *"nhập kết quả điểm học tập"* **không kèm bất kỳ ràng buộc trạng thái nào**. Vậy baseline vốn không hề bắt phải kết thúc khóa mới nhập được điểm. Đề xuất A1 của tôi thực chất là **hợp thức hóa hành vi chặn của Dev** — đúng thứ mà nguyên tắc của chị cấm.
>
> **2. Nhưng lời khuyên "A2 → bỏ ràng buộc DA_KET_THUC của FR-III-17" của tôi cũng sai.** CSV UC36 (dòng 178-181) ghi rõ *"cập nhật kết quả kiểm tra/đánh giá **sau khi khóa học kết thúc**"* và chứa transaction *"trình phê duyệt kết quả"*. Bỏ ràng buộc đó là **trái baseline**.
>
> **Cách giải quyết đã áp dụng:** CSV vốn đã tách vai 2 UC rõ ràng, chỉ là SRS chép lẫn lộn. Nên không cần chọn bỏ FR nào:
>
> | | **FR-III-05 (UC24)** | **FR-III-17 (UC36)** |
> |---|---|---|
> | Vai trò | Nhập liệu trong quá trình | Chốt sổ + trình duyệt |
> | Trạng thái | Đang diễn ra + Đã kết thúc ✅ **A2** | Chỉ Đã kết thúc |
> | Tác nhân (CSV) | CB NV + CB PD | Chỉ CB NV |
>
> Cách này thực hiện đúng A2, gỡ hết mâu thuẫn, **không phải tách FR-III-05** (đúng Quyết định B).

> ### ⚠️ Hệ quả của A2: issue 08 ĐẢO CHIỀU
>
> Với A1, "không hiện danh sách ở khóa Đang diễn ra" là **đúng đặc tả**. Với **A2 thì đó là LỖI DEV** — Dev đang chặn một việc mà baseline cho phép. Trả lời *"❌ Không phải bug"* của Dev **không còn đứng vững**.
>
> Vậy KTDGKQHT_08 giờ có **hai lỗi Dev** phải sửa, không phải một:
> 1. Không hiện danh sách học viên khi khóa "Đang diễn ra" ← mới, do A2
> 2. Nhập >10 tự kéo về 10 ← đã có từ trước, độc lập với A1/A2
>
> **Tổ kiểm thử đúng ở cả phần Fail lẫn phần Reopen của issue này.** Riêng câu trích *"SRS: Điều kiện hiển thị..."* vẫn là trích sai (câu đó không có trong SRS) — nhưng kết luận cuối của họ thì đúng.

**SRS đã sửa xong theo 3 quyết định trên** — chi tiết ở `_bmad-output/planning-artifacts/srs-v3.5/CHANGELOG-v3-to-v3.5.md`, mục `[2026-07-16] UAT tuần 2 — KTDGKQHT_03 + KTDGKQHT_08`.

---

## Phần 1 — Đọc trước phần này: vì sao hai bên cãi nhau mà không ai sai

Cả tester lẫn Dev đều đang trích SRS. Vấn đề là **họ trích hai chỗ khác nhau trong SRS, và hai chỗ đó nói ngược nhau.**

SRS hiện có **hai điều khoản cùng mô tả một màn hình**:

| | FR-III-05 (UC24) | FR-III-17 (UC36) |
|---|---|---|
| **Tên** | Quản lý kiểm tra, đánh giá kết quả | Ghi nhận kết quả |
| **Điều kiện để dùng** | *"Khóa học tồn tại"* — **không ràng buộc trạng thái** | *"Khóa học ở **Đã kết thúc**"* |
| **Màn hình** | SCR-III-02, Tab Kết quả | SCR-III-02, Tab Kết quả |
| **Ghi vào đâu** | KET_QUA_HOC_TAP | KET_QUA_HOC_TAP |
| **Vị trí** | `srs-fr-03-dao-tao.md:516` | `srs-fr-03-dao-tao.md:1225` |

Hai điều khoản, cùng một màn hình, cùng một bảng dữ liệu, nhưng **một cái cho nhập bất kỳ lúc nào, một cái bắt phải kết thúc khóa mới nhập được**.

- **Dev đọc FR-III-17** → code chặn, chỉ cho nhập khi khóa "Đã kết thúc" → Dev có căn cứ.
- **Tester đọc FR-III-05** → test ở khóa "Đang diễn ra" → tester cũng có căn cứ.

**Đây là lỗi của tài liệu, không phải lỗi của bên nào.** Chừng nào chưa chốt điều khoản nào là chuẩn thì hai bên còn cãi nhau mãi, vì cả hai đều cầm giấy tờ hợp lệ trong tay.

## Nguyên tắc xử lý (BA chốt 16/07/2026)

**Thứ tự bắt buộc:**

1. **Chốt các điểm SRS mâu thuẫn trước.** Quyết định dựa trên **nghiệp vụ đúng**, không dựa trên phần mềm hiện đang làm gì. Hiện trạng code **không phải là căn cứ** để chọn phương án SRS — nếu chấp nhận lối đó thì mọi chỗ Dev làm sai đều có thể hợp thức hóa bằng cách sửa SRS cho khớp.
2. **Sau khi SRS đã rõ, chỗ nào Dev làm khác SRS thì Dev phải sửa.** Không thương lượng, không sửa SRS cho khớp code.

**Hệ quả — 3 loại vấn đề, chỉ 1 loại cần chị quyết:**

| Loại | Xử lý | Trong tài liệu này |
|---|---|---|
| **SRS mâu thuẫn / SRS chưa quy định** | **Cần chị quyết** | 2 điểm: **Quyết định A, C** (Quyết định B đã chốt "không tách") |
| **SRS rõ, Dev làm khác** | **Dev phải sửa** — không cần quyết | 2 điểm: bộ chọn buổi học, kéo điểm về 10 |

> **Cách đọc:** Phần 2 và 3 phân tích từng issue, mỗi phần kết thúc bằng phần xử lý ngay tại chỗ. Phần 4 là bản nháp phản hồi tổ kiểm thử. Bảng tổng hợp ở cuối.
>
> **Quyết định A là gốc** — chốt A xong thì issue 08 tự có kết luận và danh sách việc Dev phải sửa mới chốt được.

---

## Phần 2 — KTDGKQHT_03: Điểm danh không hiện danh sách học viên

### Vấn đề

Tester vào khóa học → tab "Điểm danh" → mong thấy danh sách học viên để tick Có mặt / Vắng, nhưng **bảng trống** dù khóa học có học viên thật. Đánh Fail.

Dev trả lời: không phải bug — phải **chọn ngày buổi học trước** thì danh sách mới hiện. Đã tái hiện thành công: chọn ngày → hiện đủ 4 học viên → bấm Lưu → báo "Đã lưu điểm danh".

Tester reopen với lý do: *"SRS yêu cầu CHỌN BUỔI HỌC TỪ DANH SÁCH — không phải chọn ngày có buổi học."*

### SRS thực sự nói gì

**Về nghiệp vụ — Dev đúng.** SRS quy định điểm danh **bắt buộc gắn với một buổi học cụ thể**:

- FR-III-05, bảng Đầu vào, trường số 3: `lich_hoc_id` — **bắt buộc** — *"Buổi học cụ thể (FK → LICH_HOC) — điểm danh phải gắn với 1 buổi cụ thể"* (`srs-fr-03:538`)
- SCR-III-02 Tab 4 "Điểm danh" có cột **"Buổi học (FK lich_hoc_id)"** (`srs-fr-03:1822`)
- Entity LICH_HOC được mô tả là *"prerequisite cho điểm danh (FR-III-05)"* (`srs-v3.5.md:3452`)

Nên **bảng trống khi chưa chọn buổi là đúng thiết kế**, không phải mất dữ liệu.

**Nhưng tester chỉ ra một điểm lệch có thật.** SRS nói chọn **buổi học**, phần mềm lại cho chọn **ngày**. Hai thứ này khác nhau:

> Một ngày có thể có **2 buổi** — sáng và chiều. Nếu bộ lọc chỉ là ô chọn ngày, cán bộ **không phân biệt được** mình đang điểm danh buổi sáng hay buổi chiều. Điểm danh sẽ ghi sai buổi, kéo theo tỷ lệ chuyên cần sai, kéo theo kết quả Đạt/Không đạt sai (BR-KQ-02).

Tab 2 "Lịch học" của cùng màn hình đã có sẵn đủ thông tin để hiển thị một buổi cho tử tế: **Ngày · Khung giờ · Hình thức · Địa điểm · Nội dung** (`srs-fr-03:1820`). Bộ chọn buổi cần hiển thị chừng đó, không phải một ô chọn ngày trơ trọi.

### Lỗ hổng của SRS ở đây

**SRS không hề mô tả bảng trống trông như thế nào.** Không có một dòng nào quy định khi chưa chọn buổi thì hiển thị gì. Nên phần mềm để bảng trống trơn, không một chữ hướng dẫn.

Tester nhìn bảng trống → hiểu là dữ liệu bị mất → đánh Fail. **Phản ứng này hoàn toàn hợp lý.** Nếu SRS có quy định một dòng chữ *"Vui lòng chọn buổi học để bắt đầu điểm danh"* thì issue này đã không bao giờ phát sinh.

### Một lỗi nữa: điều kiện của chính test case sai

Ô Điều kiện của test ghi: khóa học ở *"Đang diễn ra" **hoặc "Đã kết thúc"***.

Nhưng bảng chuyển trạng thái trong SRS master ghi rõ: bước chuyển `Đang diễn ra → Đã kết thúc` có **Tác động = "Đóng điểm danh"** (`srs-v3.5.md:5759`).

Nghĩa là: **khóa đã kết thúc thì điểm danh phải đóng, không nhập được nữa.** Test case cho phép điểm danh ở "Đã kết thúc" là sai so với SRS.

### Kết luận issue 03

| Nội dung | Ai đúng | Xử lý |
|---|---|---|
| Bảng trống khi chưa chọn buổi | **Dev đúng** — đúng thiết kế | Không phải bug |
| Bộ chọn là "ngày" thay vì "buổi học" | **Tester đúng** | **Dev phải sửa** — SRS đã rõ, không cần quyết |
| Bảng trống không có dòng hướng dẫn | **SRS thiếu** | → **Quyết định C** |
| Điều kiện test có "Đã kết thúc" | **Test sai** | Sửa test case — SRS đã rõ, không cần quyết |

### 🔧 Dev phải sửa — Bộ chọn buổi học ở tab Điểm danh

*(Không cần chị quyết: SRS đã quy định rõ, Dev làm khác → Dev sửa.)*

Hiện là ô chọn **ngày**. SRS yêu cầu chọn **buổi học** (`lich_hoc_id` — FR-III-05 Đầu vào trường 3, bắt buộc). Đây là **Dev làm khác SRS**, không phải điểm SRS mâu thuẫn — nên không có gì để quyết, chỉ có việc phải sửa.

**Cách sửa:** đổi thành danh sách buổi học, mỗi dòng hiển thị **Ngày · Khung giờ · Nội dung** (lấy từ LICH_HOC, giống Tab 2 Lịch học). Sửa cho khớp SRS hiện hành, không phải chức năng mới — **không đưa vào yêu cầu cải tiến**.

### ✅ Quyết định C — Bổ sung dòng hướng dẫn cho bảng trống

Khi chưa chọn buổi, tab Điểm danh hiển thị: *"Vui lòng chọn buổi học để bắt đầu điểm danh"*.

Đây là **chức năng mới** (SRS chưa quy định) nhưng rất nhỏ và chính nó là nguyên nhân sinh ra issue này.

☐ Bổ sung vào SRS + giao Dev  ☐ Đưa vào danh sách yêu cầu cải tiến  ☐ Bỏ qua

---

## Phần 3 — KTDGKQHT_08: Nhập điểm kiểm tra không hiện danh sách

### Vấn đề

Tester vào khóa học **"Đang diễn ra"** → tab "Kết quả kiểm tra" → định nhập một điểm sai (ví dụ 15) để kiểm tra hệ thống có báo lỗi *"Điểm kiểm tra phải từ 0 đến 10"* không. Nhưng **danh sách học viên không hiện** nên không nhập được gì. Đánh Fail.

Dev trả lời: không phải bug — điểm kiểm tra là **điểm cuối khóa**, chỉ nhập được khi khóa **"Đã kết thúc"**. Khóa đang diễn ra thì tab Kết quả trống và nút Lưu bị khóa, đúng thiết kế.

### Điểm 1 — Câu tester trích không có trong SRS

Tester reopen với lý do: *"Tài liệu SRS: Điều kiện hiển thị: Khóa học ở trạng thái 'Đang diễn ra' hoặc 'Đã kết thúc'."*

**Tôi đã tìm toàn bộ file `srs-fr-03-dao-tao.md` — cụm từ "Điều kiện hiển thị" không tồn tại.** Câu này lấy từ chính ô "Điều kiện" của test case, không phải trích từ SRS. Tester đang trích lại đề bài của mình rồi gọi đó là SRS.

Cần lưu ý điểm này khi phản hồi, nhưng **không có nghĩa là tester sai hoàn toàn** — xem điểm 2.

### Điểm 2 — Dev cũng chỉ đúng một nửa, vì SRS tự mâu thuẫn

Dev nói "chỉ nhập được khi Đã kết thúc" — đúng theo **FR-III-17**.
Nhưng **FR-III-05** thì chỉ ghi điều kiện là *"Khóa học tồn tại"*, không chặn trạng thái nào cả.

Đây chính là mâu thuẫn đã nêu ở Phần 1. **Chưa chốt được điều khoản nào chuẩn thì chưa kết luận được phần này.**

### Điểm 3 — Và đây mới là điều quan trọng nhất: trong lời giải trình của Dev có một bug thật

Dev viết, với ý định chứng minh mình đúng:

> *"ô Điểm kiểm tra giới hạn 0–10, **nhập >10 hệ thống tự đưa về 10**, không cho lưu điểm sai"*

**Hành vi này sai đặc tả.** SRS quy định rõ ràng ở hai chỗ độc lập:

1. **FR-III-05, bảng Xử lý lỗi, dòng E1** (`srs-fr-03:600`):
   > *Điểm ngoài 0-10 → mã `ERR-KQ-01` → **"Điểm kiểm tra phải từ 0 đến 10"** → Severity: ERROR*

   SRS yêu cầu **TỪ CHỐI và BÁO LỖI**. Không phải **âm thầm kéo về 10**.

2. **Entity KET_QUA_DAO_TAO, trường `diem_kiem_tra`** (`srs-v3.5.md:2504`):
   > ràng buộc `CHECK BETWEEN 0 AND 10`

   Ràng buộc kiểu CHECK trong cơ sở dữ liệu nghĩa là **chặn không cho ghi**, chứ không phải tự sửa giá trị.

**Hậu quả nghiệp vụ — đây là chỗ nguy hiểm:**

> Cán bộ định nhập `1.5` nhưng gõ nhầm thành `15`.
> → Hệ thống lặng lẽ đổi thành `10`. Không báo gì.
> → Theo BR-KQ-01, `10 điểm` xếp loại **Giỏi**.
> → Theo BR-KQ-02, học viên **Đạt** khóa học.
> → Kết quả này được **công bố vào tài khoản học viên** qua FR-III-19.
> → Không ai biết đó là lỗi gõ nhầm. Từ `1.5` (trượt) thành `10` (Giỏi) mà không một cảnh báo nào.

Nếu SRS được tuân thủ, hệ thống sẽ báo *"Điểm kiểm tra phải từ 0 đến 10"* và cán bộ sửa lại ngay tại chỗ.

**Ngoài ra:** cách làm hiện tại khiến mã lỗi `ERR-KQ-01` trở thành **mã chết** — đã đặc tả trong SRS nhưng vĩnh viễn không bao giờ kích hoạt được, vì giao diện đã chặn từ trước không cho giá trị sai đi tới bước kiểm tra. Test case KTDGKQHT_08 vốn được viết ra để kiểm tra đúng mã lỗi này, nên **về bản chất test case này không sai — nó đang chỉ đúng vào một lỗi thật, chỉ là bị chặn ở bước trước nên chưa chạm tới được.**

### Kết luận issue 08

| Nội dung | Ai đúng | Xử lý |
|---|---|---|
| Tester trích "Điều kiện hiển thị" từ SRS | **Tester trích sai** — câu này không có trong SRS | Ghi nhận khi phản hồi |
| Không hiện danh sách khi khóa "Đang diễn ra" | **Chưa kết luận được** — SRS tự mâu thuẫn | → **Quyết định A** (phải chốt trước) |
| Nhập >10 tự kéo về 10 | **Dev sai** — trái E1/ERR-KQ-01 và trái ràng buộc CHECK | **Dev phải sửa** — SRS đã rõ, không cần quyết |

### ✅ Quyết định A — Điểm kiểm tra nhập được ở trạng thái nào? → **BA CHỐT: PHƯƠNG ÁN A2** (16/07/2026)

> **🔴 Đề xuất A1 bên dưới của tôi là SAI — giữ lại để truy vết.** Sau khi BA chốt A2, tôi tra CSV baseline và xác nhận **A2 mới đúng**: CSV UC24 liệt kê thao tác *"nhập kết quả điểm học tập"* **không kèm ràng buộc trạng thái nào**. Hai lý do tôi đưa ra cho A1 đều rút từ **SRS** — mà SRS chính là thứ đang lỗi ở đây; đáng lẽ phải tra CSV (chuẩn cao hơn) **trước khi** đề xuất. Bài học: khi hai điều khoản SRS mâu thuẫn thì không được lấy chính SRS làm trọng tài — phải lên baseline.
>
> **Xem mục "ĐÃ CHỐT" ở đầu tài liệu** để biết cách gỡ mâu thuẫn cuối cùng (tách vai UC24 nhập liệu / UC36 chốt sổ theo CSV).

Phải chọn một, vì FR-III-05 và FR-III-17 đang nói ngược nhau. **Đây là điểm SRS mâu thuẫn duy nhất khiến issue 08 bế tắc** — chốt xong thì mọi thứ còn lại tự suy ra.

**So sánh thuần nghiệp vụ** — cố ý **không** đưa "phần mềm hiện đang làm gì" vào bảng, vì hiện trạng code không phải căn cứ chọn phương án SRS:

| | **Phương án A1 — Chỉ khi "Đã kết thúc"** | **Phương án A2 — Cả "Đang diễn ra" và "Đã kết thúc"** |
|---|---|---|
| **Nghiệp vụ** | Điểm kiểm tra là **điểm cuối khóa** → phải học xong mới kiểm tra. Khớp tên trường `diem_kiem_tra` = *"Điểm kiểm tra cuối khóa"* trong entity | Cho cán bộ nhập dần, không phải chờ đóng khóa |
| **Khớp SRS nào** | Khớp **FR-III-17**, khớp luồng `Đã kết thúc → Chờ duyệt KQ` | Khớp **FR-III-05** |
| **Rủi ro** | Không nhập được điểm cho khóa dài ngày trước khi đóng khóa | Điểm nhập giữa chừng có thể bị hiểu là điểm chính thức; xung đột với `Đóng điểm danh` khi kết thúc |
| **Việc phải làm ở SRS** | Sửa FR-III-05 PRE-02 thêm ràng buộc "Khóa ở Đã kết thúc" | ~~Sửa FR-III-17 bỏ ràng buộc DA_KET_THUC~~ ← **ô này SAI**, CSV UC36 ghi rõ "sau khi khóa học kết thúc" nên **không được bỏ**. Cách đúng: giữ `DA_KET_THUC` cho FR-III-17, chỉ mở trạng thái ở FR-III-05 |

**~~Tôi đề xuất Phương án A1~~ (đã bị bác — xem ô đỏ trên).** Hai lý do, cả hai đều thuần nghiệp vụ:
1. SRS gọi chính trường này là *"Điểm kiểm tra **cuối khóa**"* (`srs-v3.5.md:2504`), và học viên chỉ thấy đề kiểm tra khi khóa đã kết thúc (`srs-fr-03:1483`). Nhập điểm cuối khóa khi khóa chưa xong là mâu thuẫn với chính định nghĩa của trường.
2. Khớp luồng duyệt kết quả: `Đã kết thúc → Chờ duyệt KQ → Hoàn thành`. Điểm phải chốt xong mới trình duyệt được.

> **Ghi chú về hiện trạng code:** phần mềm đang làm theo hướng A1. Tôi **cố ý không tính điều này thành lý do** — nếu A2 mới là nghiệp vụ đúng thì Dev phải sửa code, chứ không vì code đã làm A1 mà chốt SRS theo A1. Việc A1 trùng với code là *may mắn*, không phải *căn cứ*.

~~**Nếu chốt A1**~~ → issue 08 phần "không hiện danh sách" = không phải lỗi.
**✅ BA chốt A2** → issue 08 phần "không hiện danh sách" = **lỗi Dev**, chuyển Dev bỏ chặn trạng thái.

☐ ~~Phương án A1~~  ☑ **Phương án A2 — BA chốt 16/07/2026**

### 🔧 Dev phải sửa — Bug "kéo điểm về 10"

*(Không cần chị quyết: SRS đã quy định rõ ở hai tầng, Dev làm khác → Dev sửa. **Độc lập với Quyết định A** — chốt A1 hay A2 thì bug này vẫn phải sửa.)*

Trái E1/`ERR-KQ-01` (FR-III-05) và trái ràng buộc `CHECK BETWEEN 0 AND 10` (entity KET_QUA_DAO_TAO).

**Cách sửa:** bỏ cơ chế tự kéo về 10; cho phép gõ giá trị bất kỳ; khi bấm Lưu thì kiểm tra, sai thì **từ chối + hiện đúng thông báo "Điểm kiểm tra phải từ 0 đến 10"** (mã `ERR-KQ-01`). Áp dụng cho cả nhập tay lẫn nhập từ file Excel.

---

## Phần 4 — Bản nháp phản hồi gửi tổ kiểm thử

*(Bản này đã soạn lại theo **Phương án A2** BA chốt 16/07/2026 — thay bản nháp cũ viết theo A1.)*

### KTDGKQHT_03 — Giữ Fail một phần, không phải bug ở phần chính

> **Về việc bảng danh sách học viên trống:** đây là **đúng thiết kế**, không phải lỗi dữ liệu. Theo SRS (FR-III-05), điểm danh bắt buộc gắn với một buổi học cụ thể (`lich_hoc_id`), nên phải chọn buổi trước thì danh sách học viên của buổi đó mới hiện.
>
> **Tuy nhiên tổ kiểm thử phản ánh đúng ở phần Reopen:** bộ chọn hiện là **ô chọn ngày**, trong khi SRS quy định chọn **buổi học**. Một ngày có thể có hai buổi (sáng/chiều), chọn theo ngày không phân biệt được buổi nên sẽ ghi sai buổi → sai tỷ lệ chuyên cần → sai kết quả Đạt/Không đạt. Đây là **Dev làm khác SRS**, đã chuyển Dev sửa thành danh sách buổi học (Ngày · Khung giờ · Nội dung).
>
> **Bổ sung theo phản ánh của tổ kiểm thử:** SRS trước đây không quy định bảng trống hiển thị gì, nên phần mềm để trống trơn — đây là lý do chính khiến tổ kiểm thử hiểu nhầm là mất dữ liệu. BA đã bổ sung vào SRS: khi chưa chọn buổi, hiển thị **"Vui lòng chọn buổi học để bắt đầu điểm danh"**. Đã chuyển Dev.
>
> **Đề nghị tổ kiểm thử sửa ô Điều kiện của test case:** bỏ trạng thái "Đã kết thúc". Theo SRS (bảng chuyển trạng thái Khóa học), khi khóa chuyển "Đã kết thúc" thì điểm danh được **đóng** — chỉ điểm danh được khi khóa "Đang diễn ra".

### KTDGKQHT_08 — Xác nhận Fail, chuyển Dev sửa (2 lỗi)

> **Kết luận: tổ kiểm thử đúng, đây là lỗi. Trả lời "Không phải bug" của Dev không chính xác.**
>
> **Lỗi 1 — Không hiện danh sách học viên khi khóa "Đang diễn ra".** BA đã rà soát và chốt: **điểm kiểm tra được phép nhập khi khóa "Đang diễn ra" hoặc "Đã kết thúc"**. Căn cứ: Danh sách UC/Transaction (baseline) — UC24 "Quản lý kiểm tra, đánh giá kết quả học tập" liệt kê thao tác *"nhập kết quả điểm học tập"* **không kèm ràng buộc trạng thái** nào. Việc phần mềm khóa tab "Kết quả" khi khóa đang diễn ra là **chặn một chức năng mà baseline cho phép** → Dev bỏ chặn.
>
> *Lưu ý phân biệt:* ràng buộc "sau khi khóa học kết thúc" thuộc **UC36 — Ghi nhận kết quả đào tạo bồi dưỡng** (thao tác *trình phê duyệt kết quả*), không phải UC24. Nhập điểm và trình duyệt kết quả là hai việc khác nhau: nhập điểm được từ khi khóa đang diễn ra; trình duyệt kết quả thì vẫn phải chờ khóa kết thúc. SRS đã được sửa để tách rõ hai việc này.
>
> Khi khóa chưa kết thúc, tab "Kết quả kiểm tra" sẽ hiển thị nhãn **"Kết quả tạm tính"** — vì học viên chưa học hết buổi nên tỷ lệ chuyên cần và kết quả Đạt/Không đạt chưa phải số liệu chính thức.
>
> **Lỗi 2 — Nhập điểm >10 tự kéo về 10.** Hiện tại hệ thống tự động đổi giá trị nhập thành 10 mà không cảnh báo. Theo SRS (FR-III-05 mục Xử lý lỗi, mã `ERR-KQ-01`) hệ thống phải **từ chối và hiển thị "Điểm kiểm tra phải từ 0 đến 10"**, đồng thời ràng buộc dữ liệu của hệ thống là chặn ghi chứ không sửa giá trị. Tự kéo về 10 khiến lỗi gõ nhầm (gõ `15` thay vì `1.5`) thành điểm 10 — xếp loại Giỏi, kết quả Đạt — rồi công bố vào tài khoản học viên mà không ai phát hiện. Đã chuyển Dev sửa: giữ nguyên giá trị vừa gõ, báo lỗi để cán bộ sửa lại.
>
> **Một điểm nhỏ xin trao đổi lại:** câu *"Tài liệu SRS: Điều kiện hiển thị: Khóa học ở trạng thái Đang diễn ra hoặc Đã kết thúc"* nêu ở phản hồi lần 1 **không có trong tài liệu SRS** — chúng tôi đã rà toàn bộ tài liệu Đào tạo và không tìm thấy. Nội dung đó nằm ở ô "Điều kiện" của chính test case. Kết luận của tổ kiểm thử là đúng, nhưng đề nghị các lần sau trích đúng mục trong SRS để hai bên đối chiếu nhanh hơn.
>
> **Đề nghị tổ kiểm thử tách test case này làm hai:** một ca kiểm tra hiển thị + nhập điểm ở khóa "Đang diễn ra"; một ca kiểm tra ràng buộc điểm 0–10 (nhập 15 → phải báo lỗi, không tự thành 10). Ô Điều kiện hiện tại **giữ nguyên** — đã đúng.

---

## Tóm tắt — thứ tự xử lý

### ✅ Bước 1 — Chốt SRS — **XONG** (BA chốt 16/07/2026)

A = Phương án **A2** · B = **không tách** · C = **đồng ý**. Xem mục "ĐÃ CHỐT" đầu tài liệu.

### ✅ Bước 2 — BA dọn SRS — **XONG**

| # | Việc | Trạng thái |
|---|---|---|
| 1 | FR-III-05 PRE: bổ sung PRE-03/04/05 theo A2 | ✅ Đã sửa |
| 2 | FR-III-05 Inputs: Y → Cond + bổ sung `de_kiem_tra_id` | ✅ Đã sửa |
| 3 | FR-III-05: bổ sung ERR-KQ-06/07 + ghi chú cấm clamp + 5 AC | ✅ Đã sửa |
| 4 | FR-III-17: thu hẹp về vai "chốt sổ + trình duyệt", giữ `DA_KET_THUC` | ✅ Đã sửa |
| 5 | SCR-III-02 Tab 4: bộ chọn buổi + trạng thái rỗng (QĐ C) | ✅ Đã sửa |
| 6 | SCR-III-02 Tab 5: điều kiện hiển thị A2 + nhãn "Kết quả tạm tính" | ✅ Đã sửa |
| 7 | Baseline: SM-KHOAHOC + BR-KQ-01/02 (tạm tính vs chính thức) | ✅ Đã sửa |
| 8 | Tách FR-III-05 thành 2 FR | ⛔ **Không làm** — QĐ B |
| 9 | 3 lỗi SRS thứ cấp (thực thể ma, sai số tab, gộp bảng Inputs) | ⛔ **Không làm** — BA chốt ngoài phạm vi; SRS đã hoàn nguyên về nguyên trạng |

### ⏳ Bước 3 — Dev sửa chỗ làm khác SRS (không thương lượng) — **CHUYỂN DEV**

| # | Việc | Căn cứ SRS | Issue |
|---|---|---|---|
| 1 | **Bỏ chặn tab "Kết quả" khi khóa "Đang diễn ra"** — cho hiện danh sách HV + nhập điểm | FR-III-05 PRE-04 (A2); CSV UC24 | KTDGKQHT_08 |
| 2 | **Bỏ kéo điểm về 10** → từ chối + báo `ERR-KQ-01`, giữ nguyên giá trị vừa gõ | FR-III-05 E1 + `CHECK BETWEEN 0 AND 10` | KTDGKQHT_08 |
| 3 | **Đổi ô chọn ngày → bộ chọn buổi học** (Ngày · Khung giờ · Nội dung) | FR-III-05 Inputs trường 3 | KTDGKQHT_03 |
| 4 | Thêm dòng "Vui lòng chọn buổi học để bắt đầu điểm danh" | SCR-III-02 Tab 4 (QĐ C) | KTDGKQHT_03 |
| 5 | Thêm nhãn "Kết quả tạm tính" khi khóa chưa kết thúc | SCR-III-02 Tab 5; BR-KQ-02 | (mới, từ A2) |
| 6 | Tab 4 chỉ đọc khi khóa "Đã kết thúc"; Tab 5 chỉ đọc từ "Chờ duyệt KQ" | FR-III-05 PRE-03; FR-III-17 | (mới) |

### ⏳ Bước 4 — Tổ kiểm thử sửa test case

| # | Việc |
|---|---|
| 1 | KTDGKQHT_03: bỏ "Đã kết thúc" khỏi ô Điều kiện |
| 2 | KTDGKQHT_08: **giữ nguyên ô Điều kiện** (đã đúng theo A2); tách làm 2 ca — hiển thị/nhập ở "Đang diễn ra" · ràng buộc điểm 0–10 |
