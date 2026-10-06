# Quyết định của điều phối — lô F8

Ghi lại các quyết định cắt ngang nhiều phiếu, để mọi tác nhân xử giống nhau và người sau truy được lý do.

---

## QĐ-01 (2026-08-07) — Phiếu còn vế `GAP`/`DIFF` thì ghi ô `Trạng thái dev fix` là gì?

**Bối cảnh:** tác nhân chuẩn bị `KTDGKQHT_05` hỏi: nếu vế đang hỏng (`C2`) lần này **đạt**, mà vế `G1`
(đặc tả im lặng về câu chữ thông báo kết quả nạp) vẫn là `GAP`, thì ghi `Test done` hay `BA confirm`?
Ô `R` chỉ nhận **một** giá trị.

**Quyết định — theo đúng flow 04, không phải theo tiện lợi.** Bảng Verdict + §Ca biên của
`flows/04-verify-bug-dev-fix-khong-ho-so.md` đã trả lời sẵn:

| Tình trạng các vế sau khi đo | Verdict logic | Ghi vào ô `R` | Bắt buộc có trong ô `T` |
|---|---|---|---|
| Mọi vế `MATCH` + đều đạt, **không còn** `DIFF/GAP` | **Pass** | `Test done` | — |
| Có ≥1 vế `MATCH` **còn lỗi** (kể cả đúng một phần) | **Reopen** | `Reopen` | khối `── CÁCH VERIFY sau Dev fix ──`; nếu đồng thời còn `DIFF/GAP` thì thêm mục `CẦN NGHIỆP VỤ CHỐT` + câu hỏi BA |
| **Không** vế `MATCH` nào còn lỗi, **nhưng còn** `DIFF/GAP` | **Cần BA** | `BA confirm` | câu hỏi BA cụ thể; với `DIFF` bắt buộc câu `CẦN BA CONFIRM: đối tác kỳ vọng …; SRS quy định … (file:dòng); web/dev hiện tại ….` |

⇒ Trả lời trực tiếp cho `KTDGKQHT_05`: **`C2` đạt mà `G1` vẫn `GAP` ⇒ `BA confirm`**, KHÔNG phải `Test done`.
`C2` vẫn hỏng ⇒ `Reopen` (Reopen thắng), phần BA nêu trong ô `T`.

**Cấm tuyệt đối:** hạ `GAP`/`DIFF` xuống `MATCH` để được ghi `Test done`. Đổi quan hệ chỉ hợp lệ khi
**dẫn được dòng SRS mới đọc được** (flow 04, luật khóa 5). Lý do kiểu *"web đã làm đúng y kỳ vọng rồi"*
không đổi được quan hệ.

**Chống hiểu nhầm — bắt buộc với vế `GAP` mà web đang làm ĐÚNG y kỳ vọng đối tác:** ô `T` phải nói rõ
`WEB HIỆN TẠI: đúng kỳ vọng đối tác`, và câu hỏi BA phải nêu đúng mục đích là **bổ sung điều này vào đặc tả**,
**không phải chặn bàn giao**. Người ngoài đọc không được hiểu nhầm thành "lỗi chưa xử lý".

---

## QĐ-02 (2026-08-07) — Sao lưu ô `Kết quả verify` trước khi ghi đè

Ô `T` của dòng 10 đang chứa **khối `CÁCH VERIFY` giao việc cho dev** (6.790 ký tự). Ghi đè mất là mất bản
giao việc. **Đã chụp toàn bộ 23 dòng trước khi ghi:** [`audit/gia-tri-o-truoc-khi-ghi.md`](audit/gia-tri-o-truoc-khi-ghi.md)
+ nội dung dài tách ra `audit/o-truoc-khi-ghi/<MÃ>-T-cu.txt`.

**Quy tắc khi ghi:** luôn truyền `--expect-file 'Kết quả verify=<tệp giá trị cũ>'`. Nếu công cụ báo lệch
⇒ **có người vừa sửa dòng đó** → đọc lại dòng trên bảng, xem thay đổi là gì, rồi mới quyết ghi.
Nội dung mới của dòng 10 **phải mang theo khối `CÁCH VERIFY`** (đã cập nhật theo kết quả đo mới) nếu verdict
vẫn là `Reopen`.

---

## QĐ-03 (2026-08-07) — 22/23 phiếu không phải "bug dev đã fix"

`Trạng thái` = `N/R`, `Kết quả thực tế` RỖNG, không ảnh ⇒ đối tác **chưa từng chạy** phiếu.
`Fixed` ở đây nghĩa là *"dev đã dựng xong, mời chạy"*, không phải *"đã sửa lỗi bạn báo"*.

**Hệ quả bắt buộc cho ô `T` của 22 phiếu này:** mở đầu diễn giải bằng một câu nói rõ bối cảnh, ví dụ
*"Phiếu này bên nghiệm thu chưa chạy lượt nào (ô Kết quả thực tế để trống, không có ảnh), nên đây là lượt
chạy đầu tiên; chuẩn chấm lấy từ ô Kết quả mong đợi của phiếu đối chiếu với đặc tả."*
Không được viết như thể đang xác nhận một bản sửa lỗi — dev đọc sẽ hiểu sai việc mình đã làm.

**Hệ quả thứ hai:** tỉ lệ rơi `Cần BA` ở lô này sẽ **cao bất thường**, vì nhiều kỳ vọng dạng *"hiển thị giống
thiết kế"* / *"hiện đúng câu chữ X"* mà đặc tả thường im lặng. Đó là **kết quả đúng theo flow**, không phải
né việc. Nhưng cũng **không được lười**: trước khi kết luận `GAP`, phải đọc trọn bảng/mục liên quan
(thành phần màn hình, quy tắc tương tác, bảng mã lỗi-thông báo, Business Rules) — grep rỗng không đủ.

---

## QĐ-04 (2026-08-07 14:2x) — Ứng viên bug "màn Tổng hợp toàn quốc không có lối vào": **đổi cách diễn đạt trước khi mở dòng**

**Bối cảnh:** [`BAN-GIAO-BCCT.md`](BAN-GIAO-BCCT.md) §7 mục 1 ghi *"`/ct-htpldn/tong-hop` **không có lối vào
trên menu**, cũng không có nút dẫn từ màn Đợt báo cáo"*, đề nghị điều phối cân nhắc mở phiếu riêng.

**Đã tra đặc tả (điều phối tự mở file đếm lại):**

| Dòng | Nội dung |
|---|---|
| `srs-fr-15-ct-htpldn.md:977` | FR-XI-09 → **Màn hình: SCR-XI-01** — *"(v2.1: action gửi TW / **tổng hợp** trong tab **'Đợt báo cáo'**)"* |
| `srs-fr-15-ct-htpldn.md:1175` | hàng 45 bảng thành phần SCR-XI-01: *"`[TW] Tổng hợp (gộp từ MH-15.8)` · **content** · form (editable) · Chọn BC (checkbox) → [Tổng hợp] → … · user TW"* |

⇒ Đặc tả **KHÔNG đòi mục menu riêng** cho chức năng này. Nó đòi chức năng tổng hợp là **một mục nội dung
nằm trong tab "Đợt báo cáo" của SCR-XI-01**, hiện với **user TW**.

**Quyết định:**

1. **CẤM mở dòng bug với câu chữ "thiếu mục menu".** Đó là **kê đơn cách làm** (prescribe), và còn kê **sai** —
   đặc tả không hề đòi menu. Dev đọc sẽ hiểu nhầm việc mình phải làm.
2. Nếu mở dòng, câu đúng phải là **mô tả yêu cầu**: *"Theo `:977` + `:1175`, chức năng tổng hợp phải là một
   mục trong tab 'Đợt báo cáo' của SCR-XI-01, hiện với cán bộ cấp TW. Thực tế cán bộ TW mở tab 'Đợt báo cáo'
   không thấy chỗ nào dẫn tới chức năng tổng hợp; chỉ vào được khi tự gõ địa chỉ."*
3. **Chưa đủ căn cứ để mở ngay** — phần *"cũng không có nút dẫn từ màn Đợt báo cáo"* mới là vế quyết định,
   nhưng nó là **quan sát phụ** trong lúc chạy phiếu 344, **chưa được đo riêng** với đủ điều kiện của
   hàng 45 (đúng vai trò TW · đúng đợt có `da_gui_tw = 1` · đã chọn ô báo cáo). ⇒ **Giữ làm ứng viên**,
   xếp lịch **một lượt đo riêng ngắn** sau khi xong cụm `QLHDTVVCG`, rồi mới quyết mở dòng.
4. **KHÔNG nhét lượt đo này vào phiên của cụm hợp đồng** — khác nhóm chức năng, vi phạm luật "không mở rộng case".

**Ghi chú cho người đo lượt riêng:** trạng thái đợt `DOT-THBC01-UAT` **đã bị tiêu thụ** (`DA_TONG_HOP`) ở lượt
đo phiếu 343. Muốn tái lập điều kiện phải duyệt + gửi TW hai báo cáo `CHO_PHE_DUYET` của Bộ KH&ĐT, hoặc dùng
đợt khác. Xem [`BAN-GIAO-BCCT.md`](BAN-GIAO-BCCT.md) §dữ liệu đã đổi.

---

## QĐ-05 (2026-08-07) — Không đăng nhập trùng tài khoản với nhóm đang chạy

Lúc 13:1x điều phối dùng `cbnv_tw_03` gọi API seed dữ liệu hợp đồng, trong khi nhóm đo BCCT **cũng đang dùng
chính tài khoản đó** trên giao diện ⇒ nhóm dính `ERR-AUTH-SYS-00-03` hai lần, phải đổi sang `cbnv_tw_05`
theo Rule 7. Kết quả không sai (cùng vai trò/cấp/đơn vị, đã khai đủ), nhưng **tốn một vòng chẩn đoán oan**.

**Quy tắc từ nay:** khi có nhóm đang chạy trên giao diện, việc dựng dữ liệu/đối chứng bằng API phải dùng
**tài khoản khác bộ** (vd `_05` khi nhóm dùng `_03`), hoặc **chờ nhóm xong**. Luôn khai tài khoản thực dùng.
