# BA confirmation needed — QLNDTVVCG (Tư vấn chuyên sâu) — 2026-08-06

> **File này để làm gì:** gom các testcase mà QA **không tự chốt verdict được** hoặc cần BA phản hồi lại đối tác, kèm đầy đủ đối chiếu SRS + evidence UI để BA quyết nhanh. KHÔNG dùng file này thay bug-report (bug có SRS reference rõ → log vào `bug-report-*.md`).

> **Phạm vi file này:** đợt re-verify FLOW 04 các bug đối tác đã đánh `Dopai=dev done` + `Trạng thái dev fix=Fixed`,
> bảng `1OKBN2otlmdZ44…` tab `bug`. Đo trên **env dev `https://18.143.165.120.nip.io`**, bản dựng **HTPLDN · V1.0.8**.
>
> **Lưu ý:** cả 3 câu hỏi dưới đây **không** treo verdict của case nào. `QLNDTVVCG_24` và `QLNDTVVCG_26` đều đã
> chấm **Pass** trên căn cứ độc lập (xem `../../reverify-bug-devfix-2026-08-06/tieuchi/QLNDTVVCG_24.md` và `../../reverify-bug-devfix-2026-08-06/tieuchi/QLNDTVVCG_26.md` mục 7).
> Đây là các điểm đặc tả cần chốt để lượt kiểm thử sau không chấm sai và để dev không "dọn dẹp" nhầm.

---

## QLNDTVVCG_24 — Thông báo khi chuyên gia xác nhận hiện chỉ chạy trong ứng dụng, chưa có thư điện tử

**Bối cảnh testcase**

- Dòng Excel: **286**, mã TC `QLNDTVVCG_24`, tab `bug`.
- Nội dung kiểm tra: chuyên gia được phân công bấm **[Chấp nhận]** trên màn *Tư vấn chuyên sâu*.
- Expected trong file UAT: *"Gửi thông báo cho doanh nghiệp và cán bộ nghiệp vụ phụ trách."*
- Actual đối tác ghi: *"Doanh nghiệp và CBNV không nhận được thông báo"* → đối tác chấm `Fail`.

**Kết quả verify UI hiện tại**

- Verify lại ngày **06/08/2026** qua **Chrome DevTools MCP**, tài khoản `qa_tvvseed28` (*Tư vấn viên · Chuyên gia
  tư vấn*, `BTP · TW`) bấm chấp nhận trên giao diện thật.
- **Thông báo trong ứng dụng ĐÃ CÓ, cho cả hai đối tượng** — sinh đúng mốc giây bấm chấp nhận, nội dung trỏ đúng
  mã bản ghi:
  - Doanh nghiệp `0109998887`: *"Chuyên gia đã xác nhận tư vấn: TVCS-20260725-0005"*.
  - Cán bộ nghiệp vụ `cbnv_tw`: *"Chuyên gia đã xác nhận tư vấn: TVCS-20260806-0001"*.
- **Thư điện tử: KHÔNG có.** Kiểm ở MailHog của env (`http://18.143.165.120:8025`) — tổng số thư **không đổi**
  giữa trước và sau thao tác; không có thư nào tạo sau mốc chấp nhận.
- Evidence: `../../reverify-bug-devfix-2026-08-06/bug-reports/image/QLNDTVVCG_24-B-DN-nhan-thong-bao-CG-da-xac-nhan-V108.png` ·
  `../../reverify-bug-devfix-2026-08-06/bug-reports/image/QLNDTVVCG_24-C-CBNV-nhan-thong-bao-CG-da-xac-nhan-V108.png`

**Điểm cần BA chốt**

1. **Bước xử lý của FR yêu cầu gửi thông báo, nhưng không nói kênh nào.**
   *"Gửi thông báo DN + CB NV: CG đã xác nhận | BR-NOTIF-01"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:186`

2. **Quy tắc được viện dẫn (BR-NOTIF-01) đòi hai kênh, nhưng phạm vi áp dụng của nó lại KHÔNG bao gồm nhóm FR này.**
   Định nghĩa quy tắc ghi *"hệ thống PHẢI gửi thông báo **in-app + email**"*, nhưng cột "Áp dụng" liệt kê
   `FR-II-08, FR-III-*, FR-IV-06/07, FR-V.I, FR-V.II, FR-VI, FR-XI` — **không có FR-X.1**. Bảng quy tắc của chính
   module cũng chỉ map `BR-NOTIF-01` cho **FR-X.1-03** và **FR-X.1-05**, không cho FR-X.1-01 là FR chứa bước `:186`.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md:5612`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1555`

**Câu hỏi cần BA xác nhận**

Sự kiện *"chuyên gia xác nhận nhận việc"* phải gửi thông báo qua **những kênh nào**?

1. **Hướng 1 — chỉ trong ứng dụng là đủ.** Hiện trạng **đạt yêu cầu**; đề nghị BA ghi rõ kênh vào `:186` (hoặc bổ
   sung FR-X.1-01 vào phạm vi áp dụng của BR-NOTIF-01 kèm ngoại lệ về kênh) để lượt kiểm thử sau không tranh cãi.
2. **Hướng 2 — phải có cả thư điện tử** (theo đúng chữ "in-app + email" của BR-NOTIF-01).
   Thì đây là **thiếu sót cần dev bổ sung**, và verdict `QLNDTVVCG_24` phải đổi từ Pass sang Còn lỗi.

**Đề xuất QA tạm thời**

- Verdict `QLNDTVVCG_24`: **Pass** — vì yêu cầu *"gửi thông báo"* ở `:186` đã được đáp ứng, còn *kênh* thì đặc tả
  không chốt cho sự kiện này. QA **không** tự đặt thêm luật về kênh.
- **Chưa** gửi điểm này cho Dev cho tới khi BA chốt hướng.
- Nếu BA chọn Hướng 2 → mở lại case, owner `Dev BE`.

---

## QLNDTVVCG_26 — Sau khi chuyên gia từ chối, màn hình ở nguyên trang Chi tiết; đối tác mong đợi tự quay về danh sách

**Bối cảnh testcase**

- Dòng Excel: **287**, mã TC `QLNDTVVCG_26`, tab `bug`.
- Nội dung kiểm tra: chuyên gia được phân công nhập lý do rồi bấm **[Từ chối]** trên màn *Tư vấn chuyên sâu*.
- Expected trong file UAT (vế đầu tiên): *"NSD nhập lý do và bấm 'Xác nhận từ chối', hệ thống hiển thị thông báo
  **'Đã từ chối yêu cầu'** và **quay về danh sách**."*
- Actual đối tác ghi: *"Hệ thống không gửi thông báo tới cán bộ nghiệp vụ phụ trách kèm lý do từ chối"* — tức
  đối tác **không** phản ánh gì về vế điều hướng này; nó chỉ nằm trong cột "Kết quả mong đợi".

**Kết quả verify UI hiện tại**

- Verify lại ngày **06/08/2026**, tài khoản `qa_tvvseed28` (*Tư vấn viên · Chuyên gia tư vấn*, `BTP · TW`),
  bấm từ chối trên giao diện thật, 2 bản ghi.
- **Thông báo trên màn:** *"Đã từ chối nhiệm vụ"* — **khác câu chữ** đối tác ghi (*"Đã từ chối yêu cầu"*) nhưng
  đúng bản chất hành động. (Trên bản V1.0.3 của đối tác, toast lại là ***"Đã xác nhận"*** — sai bản chất; điểm
  đó đã hết trên V1.0.8.)
- **Điều hướng:** trang **ở nguyên màn Chi tiết**, chỉ đổi trạng thái tại chỗ về *Tiếp nhận*. Không tự quay về
  danh sách. Đây cũng đúng với hành vi trong video của đối tác.
- Evidence: `../../reverify-bug-devfix-2026-08-06/bug-reports/image/QLNDTVVCG_26-C-sau-tu-choi-banghi-B-toast-dang-mo-dan-V108.png` ·
  `../../reverify-bug-devfix-2026-08-06/bug-reports/image/QLNDTVVCG_26-B-sau-tu-choi-ve-Tiepnhan-go-chuyengia-V108.png`

**Điểm cần BA chốt**

1. **Đặc tả không quy định câu chữ thông báo cũng không quy định điều hướng sau khi từ chối.**
   Chỗ duy nhất nói về hai nút này chỉ mô tả *sự tồn tại* của chúng trên thanh hành động:
   *"PHAN_CONG: [Hủy yêu cầu] + (CG được phân công: [Chấp nhận] [Từ chối])"* và *"khi user là CG được phân công,
   hiện [Chấp nhận] / [Từ chối] trên thanh hành động"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1162`
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:1169`

2. **Bảng bước xử lý cũng dừng ở nghiệp vụ, không nói gì về màn hình sau đó** — 6 bước của
   *"Processing — CG từ chối"* chỉ gồm kiểm quyền / kiểm trạng thái / đòi lý do / đổi trạng thái / gửi thông
   báo / ghi nhật ký.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:189-198`

**Câu hỏi cần BA xác nhận**

Sau khi chuyên gia từ chối nhiệm vụ, màn hình **nên** đi đâu?

1. **Hướng 1 — ở nguyên màn Chi tiết** (hiện trạng). Người dùng thấy ngay bản ghi đã về *Tiếp nhận* và chuyên gia
   đã bị gỡ, không phải mở lại để kiểm chứng. Nếu chọn hướng này, đề nghị BA **phản hồi lại đối tác** rằng vế
   *"quay về danh sách"* trong phiếu UAT là kỳ vọng riêng của đối tác, không có gốc đặc tả.
2. **Hướng 2 — tự quay về danh sách** như đối tác mong đợi. Thì cần bổ sung câu này vào đặc tả màn hình rồi mới
   giao Dev FE, **không** giao Dev khi chưa có văn bản.

**Đề xuất QA tạm thời**

- Verdict `QLNDTVVCG_26`: **Pass** — vế đối tác phản ánh (thông báo tới CB NV) đã đạt, kèm cả lý do từ chối.
  Vế điều hướng không có gốc đặc tả nên QA **không** tự đặt luật.
- **Chưa** gửi điểm này cho Dev cho tới khi BA chốt hướng.
- Câu chữ toast (*"Đã từ chối nhiệm vụ"* vs *"Đã từ chối yêu cầu"*) QA **không** đề nghị sửa: đặc tả im lặng và
  câu hiện tại đã đúng bản chất hành động.

**Ghi chú gộp về kênh gửi:** bước từ chối `:197` cũng chỉ ghi *"Gửi thông báo CB NV"* mà **không** ghi kênh, y
như `:186`. Đo được: chỉ có thông báo trong ứng dụng, không có thư điện tử. Điểm này **thuộc chung câu hỏi 1**
ở đầu file — BA chốt một lần cho cả nhóm sự kiện của FR-X.1, không cần trả lời riêng.
Đối chiếu để BA thấy rõ đặc tả đang không nhất quán: bước **phân công** `:174` ghi thẳng *"(in-app + email)"*,
còn hai bước **xác nhận** `:186` và **từ chối** `:197` thì không ghi kênh.

---

## QLNDTVVCG_24 (điểm phụ) — Hệ thống chỉ nhận người loại "Chuyên gia" khi phân công, trong khi đặc tả viết "CG/TVV"

**Bối cảnh**

- Phát hiện khi đang phủ dạng dữ liệu thứ 2 của `QLNDTVVCG_24` (người được phân công là **TVV** thay vì **CG**).
- Không nằm trong nội dung đối tác phản ánh; ghi lại vì nó **giới hạn phạm vi kiểm thử** của mọi case thuộc luồng
  phân công tư vấn chuyên sâu.

**Kết quả verify UI hiện tại**

- Đổi một người đang hoạt động từ loại *Chuyên gia* sang loại *Tư vấn viên*, rồi thử phân công người đó cho một
  bản ghi tư vấn chuyên sâu → máy chủ từ chối:
  `ERR-VAL-X-01-03` — *"Chuyên gia không tồn tại hoặc chưa được duyệt"*.
- Đổi lại thành loại *Chuyên gia* thì phân công được ngay. ⇒ Điều kiện chặn là **loại người**, không phải trạng thái.
- Đã **khôi phục nguyên trạng** loại của người đó về *Chuyên gia* ngay sau phép thử.

**Điểm cần BA chốt**

1. Bước kiểm tra khi phân công ghi là *"Kiểm tra **CG/TVV** được chọn: phải đang hoạt động, chuyên môn phù hợp
   lĩnh vực"* — câu chữ hàm ý **cả hai loại** đều chọn được.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:172`

2. Trường lưu người được phân công cũng **không** giới hạn theo loại: *"`chuyen_gia_id` | identifier | Y | FK ->
   TU_VAN_VIEN, phải đang hoạt động"*.

   Citation:
   - `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-12-tv-chuyen-sau.md:111`

**Câu hỏi cần BA xác nhận**

Nội dung tư vấn chuyên sâu được phép giao cho **những ai**?

1. **Hướng 1 — chỉ Chuyên gia.** Hiện trạng đúng; đề nghị sửa câu chữ `:172` từ *"CG/TVV"* thành *"CG"* và ghi rõ
   ràng buộc loại vào `:111`, để QA không dựng kịch bản không tồn tại.
2. **Hướng 2 — cả Chuyên gia lẫn Tư vấn viên.** Thì việc chặn hiện nay là **lỗi**, owner `Dev BE`.

**Đề xuất QA tạm thời**

- **Chưa** log thành bug và **chưa** gửi Dev — câu chữ *"CG/TVV"* có thể chỉ là cách viết tắt của BA, chưa đủ chắc
  để khẳng định là lỗi. Chờ BA chốt.
- Ảnh hưởng tới kiểm thử: mọi case thuộc luồng này chỉ phủ được dạng "người được phân công là CG"; đã ghi rõ trong
  `../../reverify-bug-devfix-2026-08-06/tieuchi/QLNDTVVCG_24.md` mục 6 thay vì lặng lẽ bỏ qua.
