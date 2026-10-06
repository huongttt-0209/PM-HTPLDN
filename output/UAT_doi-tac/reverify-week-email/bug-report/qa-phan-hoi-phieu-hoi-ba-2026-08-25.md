# QA phản hồi phiếu hỏi BA của Dev (lập 24/08)

**Ngày:** 25/08/2026 · **Người trả lời:** QA
**Trả lời phiếu:** [`cau-hoi-ba-2-diem-lo-bug-email-2026-08-24.md`](cau-hoi-ba-2-diem-lo-bug-email-2026-08-24.md)
**Nguồn đối chiếu:** SRS v3.5 tại `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — QA đã mở từng file, đọc trực tiếp từng dòng được trích.

> **Trước hết:** phần Dev mô tả hệ thống đang chạy thế nào là **chính xác hoàn toàn**, khớp đúng với những gì QA đo được trên DEV ngày 24/08. Các dòng SRS Dev trích cũng đúng nguyên văn. Chỗ QA có ý kiến khác chỉ nằm ở **kết luận rút ra**, không phải ở dữ kiện.

---

## Tóm tắt

| Case | Kết luận của QA | Việc tiếp theo |
|---|---|---|
| **BUG-EM-TK-013** | Cần fix — chọn **Phương án A** | Dev fix, **không phải chờ BA** |
| **BUG-EM-HDD-006** | Đúng là lỗi. **Phương án A của Dev là đúng** | Xin BA xác nhận 1 câu rồi fix |

---

## ĐIỂM 1 — BUG-EM-TK-013

**Kết luận: đề nghị làm theo Phương án A. Không cần chờ BA.**

Dev đề xuất giữ nguyên code (Phương án B) vì lo rằng fix theo SRS sẽ làm mất kênh tự phục hồi, khiến mọi ca tạm khóa đều phải nhờ QTHT mở tay.

**Nỗi lo này không xảy ra**, vì SRS đã có sẵn một kênh tự phục hồi khác:

> `srs-fr-10-quan-tri.md:2382` — **BR-AUTH-07**: *"Khóa tài khoản sau 5 lần đăng nhập sai liên tiếp. **Tự mở khóa sau 30 phút HOẶC QTHT mở khóa thủ công** qua UC113"*

Bảng vòng đời tài khoản (`srs-fr-10-quan-tri.md:2307-2310`, SM-TAIKHOAN) cũng chỉ liệt kê **đúng hai** cách thoát khỏi trạng thái Tạm khóa: QTHT mở khóa, hoặc hết 30 phút tự mở. **Đặt lại mật khẩu không nằm trong hai cách đó.**

Nên fix theo SRS sẽ không làm ai bị kẹt: người gõ sai mật khẩu 5 lần chỉ cần chờ 30 phút.

**Một điểm phiếu chưa đề cập.** Bảng trên có **hai nguyên nhân** dẫn tới Tạm khóa — gõ sai 5 lần (dòng 2307) và **QTHT chủ động khóa** (dòng 2308). Phiếu chỉ bàn nguyên nhân thứ nhất, nhưng cùng một đoạn xử lý đó áp cho cả hai. Hệ quả là **người bị QTHT khóa cũng tự mở khóa lại được cho chính mình.**

QA đã dựng lại đúng tình huống này trên DEV ngày 24/08:

```
08:32:05  QTHT khóa tài khoản 0409998821
08:32:56  Thư đặt lại mật khẩu vẫn được gửi đi
08:34:37  Người dùng đặt mật khẩu mới
08:35:37  Người dùng đăng nhập lại thành công
```

Nhật ký của tài khoản **không có thao tác mở khóa nào** giữa hai mốc đó, và trạng thái tài khoản sau cùng là Hoạt động.

**Về lo ngại lộ thông tin.** Màn đăng nhập hiện đã báo thẳng *"Tài khoản đã bị tạm khóa. Vui lòng liên hệ QTHT"* (`srs-fr-10-quan-tri.md:961`), và việc kiểm tra trạng thái diễn ra **trước** khi so mật khẩu (`:932` bước 4). Nghĩa là ai gõ đúng tên đăng nhập cũng biết được tài khoản có đang bị khóa hay không, không cần biết mật khẩu. Vì vậy báo rõ ở màn Quên mật khẩu **không làm lộ thêm thông tin gì mới**.

**Đề nghị:** giữ phiếu ở mức Critical và fix theo Phương án A.

Nếu Dev vẫn muốn theo hướng B, đề nghị viết lại nội dung hỏi BA cho đúng bản chất: không chỉ là *"giữ câu thông báo trung tính"*, mà là *"xin chấp nhận việc người bị QTHT khóa có thể tự gỡ lệnh khóa cho mình"*. Hai câu hỏi này rất khác nhau, và BA cần thấy rõ câu sau để quyết.

---

## ĐIỂM 2 — BUG-EM-HDD-006

**Kết luận: Dev xác định lỗi đúng, và Phương án A của Dev cũng đúng. Chỉ cần BA xác nhận một câu.**

Phiếu nêu SRS nhóm Hỏi đáp chỉ viết chữ *"escalate"* trần, không nói escalate tới ai, nên phải mượn cách làm của nhóm Vụ việc.

**Thực ra SRS nhóm Hỏi đáp đã trả lời câu này rồi**, ngay tại dòng phía trên dòng mà phiếu trích:

> `srs-fr-02-hoi-dap.md:1187`: *"Auto-escalate (CHO_PHE_DUYET > 3 ngày làm việc) | In-app + email + escalate | **CB PD cấp trên** | EC-01"*
>
> `srs-fr-02-hoi-dap.md:761` — EC-01: *"Tự động nhắc nhở CB PD + **escalate lên cấp trên**"*

Cộng với nhóm Vụ việc (`srs-fr-05-vu-viec.md:2460`: *"escalate **cấp trên**"*), cả ba chỗ đều thống nhất một nghĩa. Không chỗ nào trong SRS nói khác.

**Một chỗ cần đính chính nhỏ:** phiếu ghi `srs-fr-02-hoi-dap.md:1658` (BR-SLA-03) *"lặp lại cùng yêu cầu"*. Dòng đó thực ra **không nhắc tới escalate**, chỉ ghi CB NV + CB PD. Điều này càng cho thấy chữ "escalate" của nhóm Hỏi đáp chỉ xuất hiện đúng một lần, ở dòng 986.

**Đề nghị:** thay vì hỏi BA chọn A hay B, chỉ cần hỏi một câu xác nhận:

> *"Escalate của cảnh báo SLA nhóm Hỏi đáp là CB Phê duyệt của đơn vị cấp trên trực tiếp, giống EC-01 cùng nhóm và giống SLA nhóm Vụ việc — đúng không ạ?"*

BA gật xong là fix được theo Phương án A. Cách này gỡ chặn nhanh hơn nhiều.

---

## Việc cần làm

| Ai | Việc |
|---|---|
| **Dev** | Fix TK-013 theo Phương án A — không chờ BA |
| **QA / Dev** | Gửi BA 1 câu xác nhận đích escalate của HDD-006 |
| **BA** | Xác nhận đích escalate của nhóm Hỏi đáp |

*QA lập 25/08/2026 — mọi dòng SRS trích trong phiếu này đều đã mở file đọc trực tiếp tại `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.*
