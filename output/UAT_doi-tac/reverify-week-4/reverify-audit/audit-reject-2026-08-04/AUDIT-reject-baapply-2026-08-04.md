# Audit verdict `Reject` — BƯỚC 2 áp quyết định BA, ngày 04/08/2026

**Ngày audit:** 2026-08-04 · **Người audit:** QA (Claude Code) · **Quy trình:** [QA_BA_APPLY_PROTOCOL.md](../../../QA_BA_APPLY_PROTOCOL.md) §"Sau khi BA chốt là BUG" — *"`Reject` không vào bug-report, nhưng lưu vết quyết định BA vào `reverify-audit/`"*.

**Phạm vi:** 3 dòng được chấm `Reject` trong đợt áp quyết định BA ngày 04/08/2026 (tab `UAT_TGPL Doanh Nghiệp-tuần 2` và `tuần 3`). Cả 3 trước đó đều mang `Trạng thái dev fix 1 = BA confirm` + `Verify = BA confirm`.

**Nguồn quyết định:** [`../../reverify-round-2026-08-04/phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md`](../../reverify-round-2026-08-04/phan-hoi-cac-diem-cho-BA-chot-2026-08-04.md) — phiếu BA phản hồi, duyệt 04/08/2026.

**SRS đối chiếu:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` — **mọi số dòng dưới đây đã mở file kiểm lại ngày 04/08/2026**, không quote từ trí nhớ và không lấy lại số dòng trong phiếu BA (xem §"Cảnh báo trôi số dòng" cuối file).

**Trạng thái ghi sổ:** ✅ **ĐÃ GHI** — 3 dòng đều ghi `Trạng thái dev fix 1` = `Reject` + `Verify` = `Reject` + note mới ở `DEV phản hồi lần 1`. Đọc lại xác nhận khớp. Nguyên trạng trước khi ghi: [`../../../reverify-audit/BACKUP-33-dong-truoc-baapply-2026-08-04.json`](../../../reverify-audit/BACKUP-33-dong-truoc-baapply-2026-08-04.json). Nhật ký ghi: [`../../reverify-round-2026-08-04/ket-qua-chay-write.log`](../../reverify-round-2026-08-04/ket-qua-chay-write.log).

---

## Kết luận tổng

| Tab | Row | Mã TC | P/Q trước | Verdict áp | Loại theo BA | Có việc cho Dev? |
|---|:-:|---|---|:-:|---|:-:|
| tuần 2 | 120 | `PDKHDTTH_04` | `BA confirm` | **Reject** | Phần mềm đúng đặc tả, đối tác cần cập nhật Kết quả mong đợi | Không |
| tuần 2 | 122 | `DKTGMLTVV_04` | `BA confirm` | **Reject** | Phần mềm đúng bản bàn giao hiện hành, đối tác bám bản cũ | Không |
| tuần 3 | 332 | `QLDMTCTV_OOS_06` | `BA confirm` | **Reject** | Đặc tả tự mâu thuẫn, phần mềm đúng; BA dọn tài liệu | Không |

**Vì sao 3 dòng này được phép `Reject` (không phải `BA confirm` tiếp):** `QA_VERIFY_PROTOCOL.md` §Verdict cấm dùng `Reject` cho bất đồng *kỳ vọng vs đặc tả* khi chưa có người có thẩm quyền chốt. Ở đây **BA đã chốt bằng văn bản ngày 04/08/2026** cho cả 3 mục ⇒ bất đồng không còn treo, `Reject` là nhãn đúng. Đây là điểm khác với đợt audit 27/07 ([`../audit-reject-2026-07-27/AUDIT-reject-tuan-4.md`](../audit-reject-2026-07-27/AUDIT-reject-tuan-4.md)), nơi 3 dòng bị `Reject` **trước khi** có ai chốt nên phải trả về `BA confirm`.

**Không dòng nào vào file bug-report** — đúng protocol.

---

## Row 120 — `PDKHDTTH_04` (tab tuần 2)

**Phiếu đối tác phản ánh:** cán bộ phê duyệt cấp Trung ương mở kế hoạch đào tạo "Chờ duyệt" do đơn vị cấp Địa phương lập thì không duyệt được, và **màn hình không hiện thông báo nào** giải thích vì sao. Kết quả mong đợi của phiếu là câu *"Không có quyền phê duyệt kế hoạch này"*.

**BA chốt (Vấn đề 14 — Loại 3, phần mềm đúng đặc tả):** theo tài liệu bàn giao mục **4.3.15.2.3 STT 1 "Phê duyệt kế hoạch năm"**, nút Phê duyệt / Từ chối **chỉ hiển thị** với cán bộ phê duyệt **cùng đơn vị** với kế hoạch. Cán bộ khác đơn vị không nhìn thấy nút ⇒ không phát sinh thao tác ⇒ **không có tình huống nào để sinh ra thông báo từ chối quyền**. Phần mềm đang chạy đúng như vậy.

**Phần QA đã đo và không tranh chấp:** việc **chặn** là đúng — `BR-AUTH-05` (`srs-v3.5.md:5480` — *"Phê duyệt cùng đơn vị (strict) … Áp dụng cho mọi action duyệt"*) và Preconditions của FR-III-15. Cùng tài khoản đó, với kế hoạch **cùng đơn vị** thì nút vẫn hiện và duyệt được bình thường ⇒ không phải lỗi ẩn nút toàn cục.

**Việc còn lại (của BA, không phải Dev):** phiếu BA ghi kèm một việc dọn tài liệu — bổ sung điều kiện cùng đơn vị vào đặc tả màn hình Kế hoạch đào tạo, vì chỗ đó đang ghi nút hiện theo trạng thái + vai trò mà **không nêu điều kiện đơn vị**, lệch với `BR-AUTH-05`.

**Việc của đối tác:** cập nhật lại Kết quả mong đợi của phiếu cho khớp tài liệu bàn giao.

---

## Row 122 — `DKTGMLTVV_04` (tab tuần 2)

**Phiếu đối tác phản ánh:** nhóm "Tổ chức & Mạng lưới" trên biểu mẫu Thêm mới Tư vấn viên hiển thị **3 trường** trong khi phiếu mong đợi **2 trường**.

**BA chốt (Vấn đề 17 — Loại 3, phần mềm đúng bản bàn giao hiện hành):** nhóm này gồm **ba trường** — *Tổ chức hành nghề chính*, *Tổ chức đối tác*, *Lĩnh vực pháp luật*. Trường **"Tổ chức đối tác"** có trong tài liệu bàn giao hiện hành, phục vụ trường hợp một tư vấn viên cộng tác với **nhiều tổ chức cùng lúc** (quan hệ nhiều-nhiều). Phần mềm đang hiển thị đúng ba trường này.

**Phần QA đã đo và không tranh chấp:** quan sát của tổ kiểm thử là **chính xác** — web hiển thị đúng 3 trường, không đổi theo giá trị ô "Loại" (Tư vấn viên / Chuyên gia). Bất đồng nằm ở **bản tài liệu nào là chuẩn**: kỳ vọng "chỉ 2 trường" bám bản SRS bàn giao lần 2 ngày 10/07, còn bản hiện hành có 3.

Xác nhận độc lập trên bản `Docs-…/srs-v3.5/` (kiểm ngày 04/08/2026): `srs-fr-04-chuyen-gia-tvv.md:1515` *Tổ chức chính (tùy chọn)* · `:1516` **Tổ chức đối tác** (chọn nhiều, N:N) · `:1517` *Lĩnh vực pháp luật* (bắt buộc) — đủ ba trường, khớp phần mềm.

**Việc của đối tác:** cập nhật lại Kết quả mong đợi cho khớp bản bàn giao hiện hành.

---

## Row 332 — `QLDMTCTV_OOS_06` (tab tuần 3)

> Đây là dòng **QA tự mở**, đối tác không có phiếu tương ứng ⇒ không có Kết quả mong đợi nào của đối tác cần cập nhật.

**Câu hỏi gốc QA gửi BA:** màn danh sách Tổ chức tư vấn có bao nhiêu thẻ lọc theo trạng thái? Đặc tả nói **6** ở phần màn hình nhưng nói **3** ở phần tiêu chí chấp nhận của chính chức năng đó.

**BA chốt (Vấn đề 20 — Loại 2, dọn đặc tả):** phần mềm đang **ĐÚNG với 6 thẻ**; dòng ghi "3 tab" là chỗ sót của bản cũ, BA sửa tài liệu chứ không đổi phần mềm. Thứ tự sắp xếp các thẻ không được quy định ràng buộc nên không chấm là sai.

**Kiểm chứng độc lập trên bản `Docs-…/srs-v3.5/` ngày 04/08/2026 — BA ĐÃ ÁP xong bản sửa:**

| Nội dung | Vị trí kiểm hôm nay | Trạng thái |
|---|---|---|
| *"Loại màn hình: **Danh sách 6 tab** + thao tác hàng loạt…"* | `srs-fr-04-chuyen-gia-tvv.md:1609` | đã có |
| Liệt kê rời 6 thẻ, mỗi thẻ một dòng | `:1624`–`:1629` (Đang hoạt động · Tạm dừng · Mới đăng ký · Chờ phê duyệt · Đã từ chối · Vô hiệu hóa) | đã có |
| Dòng tiêu chí chấp nhận từng ghi *"3 tab trạng thái"* | `:1129` | **ĐÃ SỬA** → *"**6 thẻ trạng thái** (…)"* kèm dấu `[BA chốt 2026-08-04 — QLDMTCTV_OOS_06]` |
| Chỗ *"3 tab trạng thái"* thứ hai ở màn Quản lý tư vấn viên | `:212` | **ĐÃ SỬA** → *"các thẻ trạng thái đúng như bảng thành phần màn hình SCR-IV-01"* |

Tra toàn văn cụm *"3 tab trạng thái"* trong file: **không còn kết quả nào** ⇒ mâu thuẫn đặc tả đã khép hoàn toàn, `Reject` đứng trên một đặc tả nhất quán.

### ⚠️ Một nghi vấn QA từng nêu — nay đã tự tan, KHÔNG cần hỏi BA

Khi đo lại màn này ngày 04/08/2026 (bản dựng **V1.0.5**, tài khoản `cbnv_tw` — vai trò **CB Nghiệp vụ**), QA chỉ đếm được **5 thẻ**: *Đang hoạt động · Mới đăng ký · Đã từ chối · Tạm dừng · Vô hiệu hóa* — **không thấy thẻ "Chờ phê duyệt"**. Vì BA phân tích trên giả định *"phần mềm đang làm 6"*, QA đã đánh dấu đây là điểm có thể phải hỏi lại BA.

**Kiểm tiếp đặc tả thì thấy không cần hỏi** — chính bảng thành phần màn hình đã quy định thẻ này hiển thị **có điều kiện theo vai trò**:

- `srs-fr-04-chuyen-gia-tvv.md:1627` — *"| 6 | tab | Tab "Chờ phê duyệt" | tab + số đếm + chấm đỏ nếu >0 | **Hiển thị khi vai trò là Cán bộ Phê duyệt** | Lọc trạng thái "Chờ phê duyệt" |"*
- `:1614` (§Quyền truy cập cùng màn) — *"Cán bộ Phê duyệt cùng đơn vị: xem + phê duyệt/từ chối tab "Chờ phê duyệt""*

⇒ Với vai trò **CB Nghiệp vụ**, việc chỉ hiện **5 thẻ** là **ĐÚNG đặc tả**. Con số "6 thẻ" là **tổng số thẻ của màn**, không phải số thẻ mà mọi vai trò đều nhìn thấy. Kết luận `Reject` của BA **không bị ảnh hưởng**.

> **⚠️ Bẫy cho lượt kiểm sau:** đừng mở lỗi *"thiếu thẻ Chờ phê duyệt"* khi đo bằng tài khoản cán bộ nghiệp vụ. Muốn kiểm đủ 6 thẻ phải đăng nhập vai trò **Cán bộ Phê duyệt cùng đơn vị**.

---

## Cảnh báo trôi số dòng SRS (áp dụng cho cả 3 dòng trên)

Phiếu BA ngày 04/08/2026 dẫn một số vị trí **lệch so với bản đặc tả hiện tại**, do chính BA chỉnh sửa file trong cùng ngày sau khi soạn phiếu:

| Phiếu BA dẫn | Vị trí thực tế khi kiểm 04/08/2026 | Độ trôi |
|---|---|:-:|
| `srs-fr-04-chuyen-gia-tvv.md:1610` (Loại màn hình 6 tab) | `:1609` | −1 |
| `srs-fr-04-chuyen-gia-tvv.md:1625-1630` (6 thẻ) | `:1624`–`:1629` | −1 |
| `srs-fr-04-chuyen-gia-tvv.md:1634` (bộ lọc Đơn vị quản lý) | `:1633` | −1 |
| `srs-fr-04-chuyen-gia-tvv.md:1637-1646` (10 cột bảng) | `:1636`–`:1645` | −1 |
| `srs-fr-03-dao-tao.md:1045` (FR-III-13 §Mô tả) | `:1068` | +23 |
| `srs-fr-03-dao-tao.md:1875` (SCR-III-01 Thành phần 8) | `:1898` | +23 |
| `srs-fr-03-dao-tao.md:600-603` (FR-III-05 §Outputs) | `:618`–`:621` | +18 |
| `srs-v3.5.md:1309` (`DE_XUAT_DAO_TAO` ma trận quyền) | `:1310` | +1 |

**Nội dung trích dẫn không đổi — chỉ số dòng đổi.** Nguyên nhân với nhóm `srs-fr-03-dao-tao.md` là khối *"Sửa đổi 2026-08-04 — chuẩn hoá nghiệp vụ nhập kết quả qua Excel (KTDGKQHT_05)"* được chèn vào đầu file, đẩy mọi mục bên dưới xuống.

**Hệ quả cần biết:** note đã ghi lên sổ ngày 04/08/2026 mang **số dòng theo phiếu BA**. Người đọc note mở đúng số đó sẽ lệch chỗ, rõ nhất ở hai dòng `116` và `135` (lệch 18–23 dòng, rơi sang mục khác). **Số dòng đúng đã được ghi trong bug entry** của từng lỗi:

- `BUG-KTDGKQHT_02` + `BUG-QLDXDTTH_11` → [`../../../reverify-week-2/verify1-conlai-2026-08-03/bug-reports/dao-tao/bug-report-dao-tao.md`](../../../reverify-week-2/verify1-conlai-2026-08-03/bug-reports/dao-tao/bug-report-dao-tao.md)
- `BUG-QLDMTCTV_OOS_05` + `BUG-QLDMTCTV_OOS_13` → [`../../../reverify-week-3/verify1-conlai-2026-08-03/bug-reports/to-chuc-tu-van/bug-report-to-chuc-tu-van.md`](../../../reverify-week-3/verify1-conlai-2026-08-03/bug-reports/to-chuc-tu-van/bug-report-to-chuc-tu-van.md)

**Bài học:** với đặc tả đang được BA sửa hằng ngày, trích dẫn nên đi kèm **tên mục + nguyên văn câu trích**, không chỉ số dòng — số dòng dùng để tra nhanh, câu trích mới là thứ định danh bền.

---

*Audit lập 2026-08-04 | QA Automation via Claude Code*
