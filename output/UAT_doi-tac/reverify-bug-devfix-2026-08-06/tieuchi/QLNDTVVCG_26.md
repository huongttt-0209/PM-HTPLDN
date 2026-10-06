# Tiêu chí verify — QLNDTVVCG_26

Mã case: **QLNDTVVCG_26** (dòng 287, tab `bug`)  ·  Thời điểm viết: **2026-08-06 10:05**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: ghi ở mục 6 (đo tại giai đoạn B)

> Viết **TRƯỚC** khi mở màn Tư vấn chuyên sâu trên env verify. Nguồn lúc viết: dòng 287 bảng `bug`,
> bằng chứng `partner-evidence/QLNDTVVCG_26.webm` (~24s — **đã mở xem**, trích frame đọc full-res),
> và đặc tả SRS v3.5.
>
> **Khai báo minh bạch:** case này **chưa có** bug entry nội bộ và **chưa có** khối `CÁCH VERIFY sau Dev fix`.
> Mục 4 dưới đây suy ra từ đặc tả, không lấy kết quả cũ.

---

## 1. Đối tác phản ánh

| Vế | Nội dung đối tác ghi | Nguồn |
|---|---|---|
| **a** | "**Hệ thống không gửi thông báo tới cán bộ nghiệp vụ phụ trách kèm lý do từ chối**" | cột "Kết quả thực tế", dòng 287 |

**Kỳ vọng đối tác ghi ở cột "Kết quả mong đợi":**
- *"NSD nhập lý do và bấm 'Xác nhận từ chối', hệ thống hiển thị thông báo 'Đã từ chối yêu cầu' và quay về danh sách."*
- *"Chuyển trạng thái yêu cầu: Đã phân công → Tiếp nhận."*
- *"Gỡ liên kết chuyên gia khỏi yêu cầu."*
- *"**Gửi thông báo cho cán bộ nghiệp vụ phụ trách kèm lý do từ chối để phân công lại.**"*

**Bằng chứng đã mở xem — đọc full-res tới khoảnh khắc lỗi** (`frames/QLNDTVVCG_26/`):

- `t006.03s.jpg` — tài khoản **`huongcg`** (nhãn `TVV · CG`, đơn vị `BTP · TW`) đang mở hộp thoại
  **"Từ chối nhiệm vụ?"** trên bản ghi `TVCS-2026080…`, DN **TKM Company**, lĩnh vực *Thuế*, chuyên gia
  `huongcg`, trạng thái **"Phân công"**. Ô *"Lý do từ chối"* có dấu `*` bắt buộc, đang gõ dở
  *"tkm kiểm thử chức năng"* (22/1000). Hai nút **[Quay lại] [Từ chối]**.
- `t009.04s.jpg` — lý do đã gõ đủ *"tkm kiểm thử chức năng từ chối"* (30/1000), con trỏ đang bấm **[Từ chối]**.
- `t012.06s.jpg` — **ngay sau khi từ chối**: toast **"Đã xác nhận"** (dấu tick xanh), bản ghi
  **`TVCS-20260803-0001`** giờ ở trạng thái **"Tiếp nhận"**, ô *Chuyên gia* = **"Chưa phân công"**,
  stepper lùi về bước 1. Trang **vẫn ở màn Chi tiết**, không quay về danh sách.
  ⇒ 2 kỳ vọng giữa (đổi trạng thái + gỡ liên kết chuyên gia) **đã đạt ngay trong video của đối tác**.
- `t015.07s.jpg` / `t018.08s.jpg` — đăng xuất (*"Đăng xuất thành công"*) rồi đăng nhập **`cbnv_tw`**.
- `t024.10s.jpg` — tài khoản **"Cán bộ NV Trung ương"** (`CB_NV_TW`), mở chuông thông báo: 5 mục hiện ra là
  4 lần *"Tài khoản vừa đăng nhập ở nơi khác"* (mục đầu **9 phút trước**) + 1 mục *"Hồ sơ TVV đã được phê
  duyệt"* (3 ngày trước). **Không** có mục nào về việc chuyên gia từ chối `TVCS-20260803-0001`.
- Bối cảnh chung: env **`htpldn-uat.ospgroup.vn`**, bản dựng **HTPLDN · V1.0.3**, ngày **2026-08-03 08:54**.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

- **Bước xử lý khi CG từ chối** — `srs-fr-12-tv-chuyen-sau.md:189-198`, bảng *"Processing — CG từ chối
  (PHAN_CONG → TIEP_NHAN)"*. Sáu bước, trong đó:
  - `:195` — *"Yêu cầu lý do từ chối (bắt buộc)"*
  - `:196` — *"**Xóa liên kết `chuyen_gia_id`, trạng thái → TIEP_NHAN**"*
  - `:197` — *"**Gửi thông báo CB NV: CG từ chối, cần phân công lại** | BR-NOTIF-01"*
  - `:198` — *"Ghi nhật ký thao tác (**kèm lý do từ chối**) | BR-DATA-05"*
  ⇒ Yêu cầu gửi thông báo cho CB NV là **một bước xử lý bắt buộc của chính FR này**, ghi thẳng trong bảng.
- **Bảng chuyển trạng thái** — `srs-fr-12-tv-chuyen-sau.md:1521`: *"PHAN_CONG | TIEP_NHAN | CG từ chối |
  Có lý do | Quay lại chọn CG khác | FR-X.1-01"*.
- **Thanh hành động màn chi tiết** — `:1162`: ở trạng thái `PHAN_CONG`, CG được phân công thấy
  **[Chấp nhận] [Từ chối]**; `:1169` nhắc lại *"khi user là CG được phân công, hiện [Chấp nhận] / [Từ chối]
  trên thanh hành động"*.

**IM LẶNG / KHÔNG RÕ về:**

- **Lý do từ chối có nằm TRONG nội dung thông báo hay không.** `:197` chỉ ghi ý nghĩa *"CG từ chối, cần phân
  công lại"*; chỗ duy nhất đặc tả gắn *lý do* vào là **nhật ký thao tác** (`:198`), **không phải** thông báo.
  ⇒ Kỳ vọng của đối tác (*"…kèm lý do từ chối"*) **rộng hơn** đặc tả. Mục 4 vì vậy chấm **việc có thông báo
  đúng sự kiện + đúng bản ghi**; phần *"kèm lý do"* chỉ **ghi nhận**, không kéo verdict → nếu lệch thì đưa
  sang phiếu hỏi BA.
- **"CB NV" là CB NV nào.** `:197` viết trống là *"CB NV"*, không nói người **tạo** bản ghi hay người **phân
  công**. Đây không phải chuyện chữ nghĩa: lượt đo `QLNDTVVCG_24` cùng module đã chứng minh hai người này
  **có thể khác nhau** và thông báo chỉ tới **người tạo**. ⇒ đẻ ra M = 2 ở mục 5.
- **Kênh gửi.** Bước `:174` (phân công CG) ghi rõ *"(in-app + email)"*, nhưng `:197` (từ chối) **không** ghi
  kênh. Cột "Áp dụng" của `BR-NOTIF-01` (`srs-v3.5.md:5612`) cũng **không liệt kê FR-X.1**.
  ⇒ chỉ chấm *có thông báo hay không*, **không** chấm đủ/thiếu kênh.
- **Câu chữ toast + có quay về danh sách hay không.** Đặc tả **không** quy định câu chữ thông báo trên màn,
  cũng **không** quy định điều hướng sau khi từ chối (`:1162`, `:1169` chỉ nói có nút). Kỳ vọng *"hiển thị
  thông báo 'Đã từ chối yêu cầu' và quay về danh sách"* là **câu chữ của đối tác**, không có gốc đặc tả.
  ⇒ **không** chấm Fail vì hai điểm này; ghi nhận + đưa BA nếu lệch.
  ⚠️ Ngoại lệ: nếu toast báo **sai bản chất hành động** (ví dụ bấm *Từ chối* mà báo *"Đã xác nhận"*) thì đó
  **không** còn là "khác câu chữ" mà là thông tin sai gửi tới người dùng → **log riêng** thành phát hiện độc
  lập, vẫn không kéo verdict của vế (a).

## 3. Precondition

- Cần **bản ghi TVCS ở trạng thái `Đã phân công`**, người được phân công là tài khoản mình đăng nhập được.
  Chưa có thì tự dựng — tiền đề **tạo được**, không phải blocker: CB NV tạo nội dung TVCS rồi phân công cho CG
  (`srs-fr-12-tv-chuyen-sau.md:166-175`).
- Cần **2 tài khoản tối thiểu**: (1) CG được phân công — người bấm *Từ chối*; (2) **CB NV phụ trách** bản ghi.
  Để phủ M = 2 (mục 5) cần thêm bản ghi **do một CB NV khác tạo**.
- **Ghi lại mã bản ghi + mốc giờ bấm từ chối + lý do đã nhập** trước khi đi kiểm thông báo, để phân biệt
  thông báo của lượt này với thông báo cũ còn tồn trong hộp.
- Ghi lại **tổng số thư MailHog** (`http://18.143.165.120:8025`) trước và sau thao tác — để kết luận về email
  bằng số đo chứ không bằng cảm giác.

## 4. Tiêu chí chấm

### Vế (a) — thông báo tới CB NV phụ trách khi CG từ chối: CHẤM ĐƯỢC

**✅ PASS khi** — thoả **cả 3** ý:

1. Sau khi CG được phân công nhập lý do và xác nhận từ chối, bản ghi chuyển về trạng thái *Tiếp nhận*
   **và** liên kết chuyên gia bị gỡ (ô Chuyên gia trống / *"Chưa phân công"*) — điều kiện cần, hỏng bước này
   thì các bước sau vô nghĩa.
2. **CB NV phụ trách bản ghi** nhận được **một thông báo mới**, sinh ra **sau** mốc giờ bấm từ chối, nội dung
   nói về việc chuyên gia **từ chối** và trỏ **đúng bản ghi đó**.
3. Thao tác từ chối **bị chặn khi bỏ trống lý do** (`:195` — lý do là bắt buộc).

**❌ FAIL nếu** — bất kỳ: CB NV phụ trách **không có** thông báo nào tương ứng sau khi từ chối · có thông báo
nhưng trỏ **sai bản ghi** · thông báo sinh **trước** mốc bấm từ chối (là thông báo cũ) · bản ghi **không** về
*Tiếp nhận* · liên kết chuyên gia **vẫn còn** · từ chối **không nhập lý do vẫn đi qua**.

**KHÔNG được chấm Fail vì:**

- **Thông báo không chứa lý do từ chối** — `:197` không đòi; lý do chỉ được đặc tả gắn vào nhật ký (`:198`).
  Gặp trường hợp này thì **ghi nhận + đưa sang phiếu hỏi BA**, không kéo verdict.
- **Chỉ có in-app mà không có email**, hoặc ngược lại — đặc tả không chốt kênh cho sự kiện này (mục 2).
- **Toast không đúng câu "Đã từ chối yêu cầu"**, hoặc **không tự quay về danh sách** — đặc tả im lặng.
  (Nhưng toast **sai bản chất hành động** thì log riêng, xem mục 2.)
- **Không thấy email trong hộp thư thật** — env giả lập email qua MailHog, phải kiểm ở đó.
- **`cbnv_tw` không nhận được thông báo trên bản ghi do CB NV khác tạo** — chừng nào **người tạo** bản ghi đó
  vẫn nhận được. Đây là chuyện *"CB NV nào"* mà đặc tả bỏ ngỏ (mục 2), **không** phải thiếu thông báo.
  Chỉ chấm Fail khi **không một CB NV nào** trong hai người (người tạo / người phân công) nhận được gì.

**Phép thử mục 4:** người chưa biết bug này, chỉ đọc mục 4, có chấm được PASS/FAIL không?
→ Có: ghi mốc giờ + mã bản ghi, bấm từ chối kèm lý do, đọc lại bản ghi, rồi mở hộp thông báo của CB NV và
đối chiếu mốc giờ + mã bản ghi. Thêm một lượt bấm từ chối bỏ trống lý do để chấm ý 3.

## 5. Dạng dữ liệu phải phủ — M = 2

1. Bản ghi TVCS mà **người tạo cũng chính là người phân công** (một CB NV làm cả hai việc) — dạng không mập mờ
   *"CB NV phụ trách là ai"*.
2. Bản ghi TVCS mà **người tạo khác người phân công** — đúng dạng dễ gây hiểu nhầm, và là dạng có khả năng
   khớp với bản ghi đối tác quay (`TVCS-20260803-0001` không rõ ai tạo).

**Nguồn xác định M:** cách ③ — điểm **không rõ của đặc tả**: `:197` chỉ ghi *"CB NV"* mà không nói là người
tạo hay người phân công, trong khi phép đo `QLNDTVVCG_24` cùng module đã chứng minh hai vai này **tách rời
được** và thông báo chỉ tới người tạo. Đo một dạng thôi thì hoặc bỏ sót lỗi thật (nếu chỉ đo dạng 1 mà dạng 2
hỏng), hoặc kết luận nhầm là lỗi (nếu chỉ đo dạng 2 — đúng cái bẫy làm đối tác chấm Fail).
Không dùng cách ① vì nhóm X.1 không có FR nào đặc tả riêng luồng thông báo theo người tạo/người phân công.

## 6. Bảng điều kiện — số đo GIAI ĐOẠN B (2026-08-06 09:28–09:36, bản dựng **HTPLDN · V1.0.8**)

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người bấm: `huongcg` (`TVV · CG`, `BTP · TW`). Người đi kiểm thông báo: "Cán bộ NV Trung ương" (`CB_NV_TW`) | Người bấm: **`qa_tvvseed28`** — "QA TVV Seed28 Active", nhãn *Tư vấn viên · Chuyên gia tư vấn*, `BTP · TW` (**trùng vai trò + trùng cấp**). Người đi kiểm: **`cbnv_tw`** và **`cbnv_tw_04`** (đều `CB_NV_TW`, `BTP · TW`) | Không |
| Entity + trạng thái | `TVCS-20260803-0001`, *Phân công* → *Tiếp nhận*, Chuyên gia → *Chưa phân công* | **2 bản ghi**, cùng *Phân công* → *Tiếp nhận* + `chuyenGiaId` về `null`: `TVCS-20260806-0002` (02:30:46.119Z) và `TVCS-20260803-0003` (02:31:47.108Z) | Không |
| Dữ liệu tiền đề | Bản ghi có sẵn của đối tác, DN = TKM Company | Cả 2 bản ghi DN = *Cong ty TNHH QA UAT Kiem Thu*, đều được `cbnv_tw` phân công cho `qa_tvvseed28` lúc 02:28:56 (2 thông báo phân công vào đúng hộp của CG). Bản ghi A **do chính `cbnv_tw` tạo**; bản ghi B **do `cbnv_tw_04` tạo** (đọc từ Nhật ký thao tác: *"03/08/2026 20:19 · Tạo mới · CB Nghiệp vụ - Trung ương #04 (cbnv_tw_04)"*) | Không |
| Input / filter / giá trị nhập | Nhập lý do *"tkm kiểm thử chức năng từ chối"* (30 ký tự) → bấm **[Từ chối]** | 3 lượt bấm trên **giao diện thật**: (1) bỏ trống lý do → bị chặn; (2) lý do 61 ký tự trên bản ghi A; (3) lý do 61 ký tự trên bản ghi B. Toast mỗi lượt: **"Đã từ chối nhiệm vụ"** (3 phần tử / **1 mốc giờ** ⇒ đúng 1 thông báo, không nhân đôi) | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 bản ghi | **M = 2/2.** Dạng 1 (người tạo = người phân công): bản ghi A, `cbnv_tw` tạo + phân công ✓. Dạng 2 (người tạo ≠ người phân công): bản ghi B, `cbnv_tw_04` tạo — `cbnv_tw` phân công ✓ | Không |

**GAP còn lại: 0.** Cả hai dạng đều dựng được và đo được bằng tài khoản thật; không có ô nào phải bỏ trống.

**Ghi chú quan trọng về "CB NV phụ trách":** thông báo từ chối đi tới **người TẠO bản ghi**, không đi tới người
phân công. Trên bản ghi B, `cbnv_tw` (người phân công) **không** thấy gì, còn `cbnv_tw_04` (người tạo) **nhận
được** đúng lúc 02:31:47.138Z — tức **30 mili-giây** sau thao tác từ chối. Nếu chỉ đo trên một bản ghi do người
khác tạo thì rất dễ kết luận nhầm thành *"CB NV không nhận được thông báo"* — đúng cái bẫy đã làm hỏng lượt đo
đầu của `QLNDTVVCG_24`, và cũng là cách giải thích khả dĩ cho quan sát của đối tác.

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** `htpldn-uat.ospgroup.vn/tv-chuyen-sau/6eb2cc6a-4d10-4bc9-8bf2-b65fcfb47e1e` —
  bản ghi **`TVCS-20260803-0001`**, DN **TKM Company**, lĩnh vực *Thuế*, chuyên gia `huongcg`,
  lý do từ chối đã nhập: *"tkm kiểm thử chức năng từ chối"*
- **Trạng thái entity:** trước khi bấm là *Phân công*; sau khi bấm là ***Tiếp nhận*** với
  *Chuyên gia = "Chưa phân công"* (đối tác **không** phản ánh gì về 2 điểm này)
- **Vai trò + bản dựng:** người bấm `huongcg` (`TVV · CG`, `BTP · TW`); người đi kiểm thông báo là
  "Cán bộ NV Trung ương" (`CB_NV_TW`) · **HTPLDN · V1.0.3** · env `htpldn-uat.ospgroup.vn` · 2026-08-03 08:54

> ⚠️ **Lệch env + bản dựng:** đối tác quay trên env nghiệm thu `ospgroup.vn` bản V1.0.3; lượt này đo trên env
> dev `18.143.165.120.nip.io`. Đây là **giới hạn hiệu lực** của verdict, không phải GAP.

## 7. Kết quả đo và verdict

| Ý của mục 4 | Kết quả | Số đo |
|---|:-:|---|
| 1. Về *Tiếp nhận* + gỡ liên kết chuyên gia | ✅ | Cả 2 bản ghi: `trangThai = TIEP_NHAN`, `chuyenGiaId = null`. Giao diện hiện *Tiếp nhận* / *Chưa phân công*, stepper lùi về bước 1. Ảnh: `QLNDTVVCG_26-B-…png` |
| 2. **CB NV phụ trách** nhận thông báo đúng bản ghi, sinh sau mốc từ chối | ✅ | Bản ghi A: *"Chuyên gia từ chối phân công: TVCS-20260806-0002"* sinh **02:30:46.157Z**, sau mốc bấm **02:30:46.119Z** (38 ms), vào hộp của `cbnv_tw` — người tạo. Bản ghi B: *"…: TVCS-20260803-0003"* sinh **02:31:47.138Z**, sau mốc **02:31:47.108Z** (30 ms), vào hộp của `cbnv_tw_04` — người tạo. Thấy cả ở chuông lẫn màn *Thông báo*. Ảnh: `…-D-…png` · `…-E-…png` · `…-F-…png` |
| 3. Bỏ trống lý do thì bị chặn | ✅ | Hộp thoại giữ nguyên, báo *"Vui lòng nhập lý do từ chối"* + *"Lý do phải có ít nhất 10 ký tự"*; đọc lại bản ghi vẫn `PHAN_CONG` + còn nguyên `chuyenGiaId`. Ảnh: `…-A-…png` |

**Verdict: Pass.** Cả 3 ý đều thoả, đo trên 2 bản ghi phủ đủ M = 2 dạng, GAP = 0.

**Vượt cả kỳ vọng đối tác:** nội dung thông báo **có kèm lý do từ chối** — *"Mã: TVCS-20260806-0002. Chuyên gia
đã từ chối, cần phân công lại. **Lý do:** QA FLOW04 QLNDTVVCG_26 - ly do tu choi ban ghi A luc 20260806"*.
Đặc tả `:197` không đòi phần *"kèm lý do"*, nhưng đối tác thì đòi — và hiện trạng đáp ứng. ⇒ **không** còn điểm
nào của phiếu này phải hỏi BA về mặt nghiệp vụ.

**Ghi nhận, KHÔNG kéo verdict (theo mục 4 §"KHÔNG được chấm Fail vì"):**

1. **Toast đã đúng bản chất hành động.** Video đối tác (bản V1.0.3) cho thấy bấm *Từ chối* nhưng toast báo
   **"Đã xác nhận"** — thông tin sai bản chất. Trên V1.0.8 toast là **"Đã từ chối nhiệm vụ"**. Triệu chứng này
   đã hết, không cần log riêng.
2. **Không tự quay về danh sách** — sau khi từ chối, trang vẫn ở màn *Chi tiết* (đúng như video đối tác). Đặc tả
   im lặng về điều hướng ⇒ đưa sang phiếu hỏi BA, không chấm Fail.
3. **Không có thư điện tử.** MailHog (`http://18.143.165.120:8025`) tổng số thư **1511 → 1513** trong cả đợt đo,
   và 2 thư tăng thêm đều là **mã đăng nhập** của `cbnv_tw` / `cbnv_tw_04`; không thư nào sinh sau 2 mốc từ
   chối. Thông báo hiện chỉ chạy **trong ứng dụng**. `:197` không chốt kênh cho sự kiện này ⇒ cùng nhóm với câu
   hỏi BA đã mở ở `QLNDTVVCG_24`.
4. **Nhật ký thao tác không lưu lý do từ chối.** `:198` đòi *"Ghi nhật ký thao tác (kèm lý do từ chối)"*; bản ghi
   nhật ký thực tế chỉ có `hanhDong = "UPDATE"` + endpoint + người thực hiện, **không có trường nào chứa lý do**
   (đọc `GET /api/v1/noi-dung-tu-van-cs/{id}/audit-logs`, 18 trường, không có `lyDo`/`chiTiet`/`noiDungThayDoi`).
   Đây là điểm lệch **riêng**, nằm ngoài phạm vi đối tác phản ánh ⇒ ghi vào mục "lỗi phát hiện ngoài phạm vi",
   không kéo verdict phiếu này.
