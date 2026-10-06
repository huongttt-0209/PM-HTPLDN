# Phép đo — LBCKQTHCT_05 (dòng 338) · 2026-08-07 — Khối **Nhận xét, kiến nghị**

**Verdict logic: CẦN BA** — vế chấm được **ĐẠT đầy đủ** (khối có thật, đúng giới hạn 5.000 ký tự,
nhập–lưu–đọc lại được). Nhưng **quan sát của đối tác tái hiện được** ở đúng các bước phiếu mô tả,
và tình huống đó rơi vào **vùng SRS IM LẶNG** ⇒ Flow 04 cấm Pass lẫn Reopen vế đó.

Chuẩn chấm: [`../chuan/LBCKQTHCT_05.md`](../chuan/LBCKQTHCT_05.md)

---

## 1. Vì sao case này KHÁC case 03/04 dù cùng một luật

Ba case đều vướng cùng một điều kiện `:1167/:1168/:1169` (*"khi dot o DANG_LAP_BC"*), và ở cả ba tôi đều
áp **luật khóa 1** — điều kiện SRS đặt ra là **tiền đề**, không phải vế. Khác nhau ở **hệ quả thực tế**:

| Case | Ở trạng thái SRS quy định | Ở trạng thái đối tác thao tác | Câu hỏi im lặng có ảnh hưởng kết quả? |
|---|---|---|---|
| 03 (21a) · 04 (21b) | có đủ 2 cột | **cũng có đủ 2 cột** | ❌ Không — claim bị bác ở **mọi** trạng thái ⇒ **Pass** |
| **05 (khối nhận xét)** | **có khối** | 🔴 **KHÔNG có khối** | ✅ **Có** — claim đúng hay sai **phụ thuộc hẳn** vào câu SRS chưa trả lời ⇒ **Cần BA** |

Đây là phân biệt có nguyên tắc, không phải chấm theo cảm tính: ở 03/04 câu hỏi im lặng **không đổi được**
kết quả nên không cản Pass; ở 05 nó **quyết định** kết quả nên rơi đúng bảng "Đối chiếu đặc tả" của Flow 04:
*"Im lặng hoặc tự mâu thuẫn → **không Pass/Reopen vế này**; kết luận Cần BA và tạo câu hỏi xác nhận."*

---

## 2. Điều kiện đo

| Mục | Giá trị |
|---|---|
| Env / bản dựng | `18.143.165.120.nip.io` · **`assets/index-D4Buvu4S.js`** (07/08/2026 02:23 VN), đã đọc lại tên bó mã trong tab |
| Tài khoản | **`cbnv_hn`** — `CB_NV_DP`, cấp ĐP, Sở Tư pháp Hà Nội (đúng tác nhân `:712`) |
| Bản ghi A | `DOT-TRON_NAM-2026-1` (`a63a3214…`) — đợt QA seed ở case 04, đơn vị `DANG_LAP` |
| Bản ghi B | `DOT-SO_BO_6_THANG-2026-1` (`a61e07f1…`) — đơn vị **`CHUA_NOP`**, nguyên trạng |
| Bản ghi C | `DOT-SO_BO_NAM-2026-1` (`e9909d96…`) — đã có `nhanXet` lưu từ case 01, dùng làm **đợt thứ hai** chứng minh lưu/đọc lại |

---

## 3. Kết quả — vế chấm được ĐẠT

### 3.1 Khối tồn tại, đúng thuộc tính SRS

Thẻ **`Nhận xét, kiến nghị`** (đọc từ tiêu đề thẻ, xác nhận lại bằng cây trợ năng), chứa:

| Thuộc tính | Đo được | SRS `:1169` |
|---|---|---|
| Kiểu điều khiển | vùng soạn nhiều dòng, 6 dòng hiển thị | `textarea` ✅ |
| Giới hạn | **`maxlength = 5000`**, bộ đếm trên màn `0 / 5000` | `Max 5000 ky tu` ✅ |
| Gợi ý trong ô | `Nhận xét về kết quả thực hiện và kiến nghị (tối đa 5.000 ký tự)` | — |
| Vị trí | ngay **sau** 2 thẻ biểu mẫu 21a/21b (#37/#38), **trước** nhóm nút hành động (#40) | đúng thứ tự `:1167`→`:1170` ✅ |

### 3.2 Nhập → lưu → đọc lại được (yêu cầu §7 chuẩn chấm)

Chuỗi mốc-giờ ghi trước khi bấm: `QA-F5-NHANXET-20260807-case05-doc-lai-duoc` (42 ký tự).

| Bước | Kết quả |
|---|---|
| Gõ vào ô | bộ đếm nhảy **`42 / 5000`** — khớp đúng độ dài chuỗi |
| Bấm [Lưu nháp] của **chính thẻ Nhận xét** | đúng **1** `PATCH /api/v1/dot-bao-caos/{id}/bao-cao` → **200** (không gửi trùng) |
| **Tải lại trang bằng địa chỉ** | giao diện: ô nhận xét = `QA-F5-NHANXET-20260807-case05-doc-lai-duoc` |
| Đối chứng máy chủ | `nhanXet` = **cùng chuỗi, khớp từng chữ** |

⇒ **Hai đường khớp** — không phải "khối chỉ có vỏ".
**Đợt thứ hai:** đợt `DOT-SO_BO_NAM-2026-1` giữ `nhanXet = QA-BCCT-20260807-0209-nhan-xet` từ case 01
⇒ lưu/đọc lại được trên **2 bản ghi độc lập**.

Ảnh: [`../image/LBCKQTHCT_05-khoi-nhanxet-doc-lai-sau-tai-lai.png`](../image/LBCKQTHCT_05-khoi-nhanxet-doc-lai-sau-tai-lai.png)

---

## 4. 🔴 Quan sát tái hiện được đúng bước phiếu mô tả

Các bước trong phiếu chỉ có 2 bước: **1. Chọn menu "Đợt báo cáo" · 2. Mở Trang Chi tiết đợt báo cáo.**
Làm **đúng 2 bước đó** trên đợt mà đơn vị chưa bắt đầu lập (`trangThaiNop = CHUA_NOP`):

| Đo trên màn | Kết quả |
|---|---|
| Danh sách thẻ trên màn | **chỉ có `Biểu mẫu 21a/TP/HTPLDN`** |
| Có thẻ `Nhận xét, kiến nghị`? | ❌ **KHÔNG** |
| Số ô soạn văn bản toàn màn | **0** |
| Có chữ "Nhận xét" bất kỳ đâu trong vùng nội dung? | ❌ **KHÔNG** |
| Nút khả dụng | chỉ `[Lập báo cáo]` |

Khối **chỉ xuất hiện sau khi cán bộ bấm [Lập báo cáo]** (đơn vị chuyển `CHUA_NOP → DANG_LAP`).

Ảnh: [`../image/LBCKQTHCT_05-truoc-khi-lap-bc-khong-co-khoi-nhanxet.png`](../image/LBCKQTHCT_05-truoc-khi-lap-bc-khong-co-khoi-nhanxet.png)

⇒ **Khiếu nại của đối tác KHÔNG phải quan sát sai.** Họ mở Chi tiết mà chưa bắt đầu lập báo cáo — đúng
2 bước phiếu ghi — và ở đó khối thật sự không có. Chấm "Pass" trơn ở đây sẽ khiến đối tác mở lại phiếu
ngay vòng sau.

**Nhưng cũng KHÔNG được Reopen:** `:1169` ràng buộc hiển thị *"khi dot o DANG_LAP_BC"*, tức đặc tả
**chỉ yêu cầu khối trong pha đang lập**, và **im lặng** về việc màn phải hiện gì ở các trạng thái còn lại.
Không có dòng nào bắt phải hiện khối ở dạng chỉ đọc trước khi lập.

---

## 5. CẦN BA CONFIRM

> **CẦN BA CONFIRM:** đối tác kỳ vọng màn Chi tiết đợt báo cáo **có sẵn** khối *Nhận xét, kiến nghị* ngay khi
> mở màn (phiếu chỉ ghi 2 bước: mở menu Đợt báo cáo → mở Chi tiết).
> **SRS quy định** `srs-fr-15-ct-htpldn.md:1169`: `| 39 | form | Nhan xet kien nghi | textarea | Max 5000 ky tu |
> input | khi dot o DANG_LAP_BC |` — có khai đích danh khối, **nhưng điều kiện hiển thị chỉ nêu pha đang lập**;
> SRS **IM LẶNG** về nội dung màn ở `TAO_DOT` / `CHO_DUYET_KQ` / `DA_DUYET_KQ` / `DA_GUI_TW` / `DA_TONG_HOP`.
> **Web/dev hiện tại:** khối **có đủ và hoạt động đúng** trong pha đang lập (đúng 5.000 ký tự, lưu và đọc lại
> được); **chưa** hiển thị trước khi cán bộ bấm [Lập báo cáo].
>
> **Câu hỏi BA:**
> (1) Khi đợt/đơn vị **chưa vào pha lập báo cáo**, màn Chi tiết có phải hiển thị khối *Nhận xét, kiến nghị*
> ở **dạng chỉ đọc** không, hay đúng là chỉ hiện khi bắt đầu lập? Đề nghị ghi thẳng điều kiện hiển thị cho
> **các trạng thái còn lại** vào dòng #39 bảng thành phần màn hình.
> (2) Mô hình STT-52 tách hai bậc trạng thái — cấp **ĐỢT** (`:1368`, có `DANG_LAP_BC`) và cấp **ĐƠN VỊ NỘP**
> (`:1389`, có `DANG_LAP`). Dòng #39 chỉ nhắc *"dot o DANG_LAP_BC"*, trong khi đợt là bản ghi dùng chung cho
> nhiều chục đơn vị. Đề nghị BA chốt: điều kiện hiển thị neo vào **trạng thái nộp của ĐƠN VỊ** hay
> **trạng thái của ĐỢT**? (Hiện phần mềm đang neo vào ĐƠN VỊ.)
>
> ⚠️ Mục đích: **bổ sung/làm rõ đặc tả màn hình — KHÔNG chặn bàn giao.** Chức năng nhập nhận xét đã dùng được.

---

## 6. Bẫy đã kiểm và loại trừ

| Bẫy | Đã làm gì |
|---|---|
| 3 — *"không bắt buộc nhập ⇒ không cần hiện"* | Không dùng lập luận này. `:802` chỉ nói `nhan_xet` không tính vào "BC hoàn chỉnh" khi trình duyệt, **không** miễn nghĩa vụ hiển thị |
| 4 — nhầm ô nhận xét của module khác | Chỉ tính ô **trên đúng màn Chi tiết đợt báo cáo**, xác định bằng tiêu đề thẻ |
| 5 — nhầm với "Ghi chú" của đợt | Ô Ghi chú của đợt (`:1158`/`:1369`) là thứ khác, không dùng để chấm |
| 6 — nhầm với ghi chú bước phê duyệt | Không tính `ghiChu` của `TrinhDuyetBcDto` |
| 7 — bẫy câu chữ | Không chấm theo nhãn; đo bằng **có ô nhập dùng được** |
| 8 — cấm suy chéo | Khối *Chương trình HTPL liên quan* nằm cùng thẻ nhưng **không** chấm ở đây — thuộc phiếu LBCKQTHCT_06 |
| 9 — bản dựng cũ | Tải lại bằng địa chỉ + đọc lại tên bó mã |

---

## 7. Giới hạn hiệu lực

Chỉ có hiệu lực cho `18.143.165.120.nip.io` + bó mã `index-D4Buvu4S.js` (07/08/2026 02:23 VN).
Bằng chứng đối tác `LBCKQTHCT_05.jpg` **trùng md5 với `LBCKQTHCT_06.jpg`** (`c0fb9837447ee90ac8c8f975a298aaef`)
— 1 ảnh dùng cho 2 claim về 2 khối khác nhau, và ảnh **chỉ bắt phần dưới trang** nên không loại trừ được
khả năng khối nằm phía trên. Vì vậy QA **không** dựa vào ảnh, mà tự tái hiện đúng 2 bước phiếu mô tả.
