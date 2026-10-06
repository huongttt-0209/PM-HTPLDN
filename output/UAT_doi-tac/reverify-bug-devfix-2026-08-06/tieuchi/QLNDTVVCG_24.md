# Tiêu chí verify — QLNDTVVCG_24

Mã case: **QLNDTVVCG_24** (dòng 286, tab `bug`)  ·  Thời điểm viết: **2026-08-06 09:05**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: ghi ở mục 6 (đo tại giai đoạn B)

> Viết **TRƯỚC** khi mở màn Tư vấn chuyên sâu trên env verify. Nguồn lúc viết: dòng 286 bảng `bug`,
> bằng chứng `partner-evidence/QLNDTVVCG_24.webm` (10.013.914 byte, ~31s — **đã mở xem**, trích frame đọc
> full-res), và đặc tả SRS v3.5.
>
> **Khai báo minh bạch:** case này **chưa có** bug entry nội bộ và **chưa có** khối `CÁCH VERIFY sau Dev fix`.
> Lịch sử nội bộ ghi Pass 2 lần (2026-08-03 env dev bản V1.0.5; 2026-08-04 env `ospgroup` bản V1.0.5) nhưng
> **không kèm số đo** nên không dùng làm ngưỡng. Mục 4 dưới đây suy ra từ đặc tả, không lấy kết quả cũ.

---

## 1. Đối tác phản ánh

| Vế | Nội dung đối tác ghi | Nguồn |
|---|---|---|
| **a** | "**Doanh nghiệp và CBNV không nhận được thông báo**" (sau khi Chuyên gia bấm *Chấp nhận*) | cột "Kết quả thực tế", dòng 286 |

**Kỳ vọng đối tác ghi ở cột "Kết quả mong đợi":**
- *"Chuyển trạng thái yêu cầu: Đã phân công → Đang tư vấn, ghi nhận thời điểm bắt đầu tư vấn."*
- *"Tạo bản ghi phiên tư vấn mới liên kết với yêu cầu."*
- *"**Gửi thông báo cho doanh nghiệp và cán bộ nghiệp vụ phụ trách.**"*

**Bằng chứng đã mở xem — đọc full-res tới khoảnh khắc lỗi** (`frames/QLNDTVVCG_24/`):

- `t006.03s.jpg` — tài khoản **`huongcg`** (nhãn vai trò `TVV · CG`, đơn vị `BTP · TW`) vừa bấm chấp nhận:
  toast **"Đã xác nhận"**, bản ghi **`TVCS-20260803-0001`**, Doanh nghiệp **TKM Company**, Lĩnh vực *Thuế*,
  Chuyên gia `huongcg`, Trạng thái **"Đang tư vấn"**, Ngày bắt đầu **03/08/2026**. Stepper đã sang bước 3.
  ⇒ 2 kỳ vọng đầu (đổi trạng thái + ghi thời điểm bắt đầu) **đã đạt ngay trong video của đối tác**.
- `t015.06s.jpg` — đổi sang tài khoản **"Tester TKM"** nhãn **`DN`** (doanh nghiệp), mở chuông thông báo:
  danh sách **chỉ có 1 mục** *"Tài khoản vừa đăng nhập ở nơi khác"* (vài giây trước). **Không** có mục nào
  nói về việc CG đã xác nhận.
- `t030.43s.jpg` — đổi sang tài khoản **"Cán bộ NV Trung ương"** nhãn `CB_NV_TW`, mở chuông: 5 mục hiện ra là
  4 lần *"Tài khoản vừa đăng nhập ở nơi khác"* + 1 mục *"Hồ sơ TVV đã được phê duyệt"* (3 ngày trước).
  **Không** có mục nào về `TVCS-20260803-0001`.
- Bối cảnh chung: env **`htpldn-uat.ospgroup.vn`**, bản dựng **HTPLDN · V1.0.3**, ngày **2026-08-03 08:57**.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

- **Bước xử lý khi CG xác nhận** — `srs-fr-12-tv-chuyen-sau.md:181-187`, bảng *"Processing — CG xác nhận
  (PHAN_CONG → DANG_TU_VAN)"*. Bảy bước, trong đó:
  - `:184` — *"Cập nhật trạng thái → DANG_TU_VAN, ghi `ngay_bat_dau` = NOW()"*
  - `:185` — *"Tạo PHIEN_TU_VAN mới liên kết với bản ghi TVCS"*
  - `:186` — *"**Gửi thông báo DN + CB NV: CG đã xác nhận** | BR-NOTIF-01"*
  - `:187` — *"Ghi nhật ký thao tác | BR-DATA-05"*
  ⇒ Yêu cầu gửi thông báo cho **cả hai** đối tượng là **một bước xử lý bắt buộc của chính FR này**, ghi thẳng
  trong bảng, không phải suy diễn. Kỳ vọng của đối tác **trùng khít** đặc tả.
- **Định nghĩa BR-NOTIF-01** — `srs-v3.5.md:5612`: *"Khi entity workflow chuyển trạng thái có ý nghĩa với bên
  liên quan, hệ thống PHẢI gửi thông báo **in-app + email** cho các đối tượng tương ứng."*

**IM LẶNG / KHÔNG RÕ về:**
- **Kênh gửi cho riêng sự kiện này.** Cột "Áp dụng" của BR-NOTIF-01 (`srs-v3.5.md:5612`) liệt kê các nhóm FR
  được áp: `FR-II-08, FR-III-*, FR-IV-06/07, FR-V.I, FR-V.II, FR-VI, FR-XI` — **không có FR-X.1** (tư vấn
  chuyên sâu). Bảng BR của chính module cũng chỉ map `BR-NOTIF-01` cho **FR-X.1-03 và FR-X.1-05**
  (`srs-fr-12-tv-chuyen-sau.md:1555`), **không** cho FR-X.1-01 là FR chứa bước `:186`.
  ⇒ *Việc phải gửi thông báo* thì rõ (nằm ở `:186`); *phải gửi qua kênh nào* thì **không chốt được** cho sự
  kiện này. Vì vậy mục 4 **chỉ chấm việc có thông báo hay không**, không chấm đủ/thiếu kênh.
- **Nội dung / tiêu đề chính xác của thông báo.** Đặc tả chỉ nói ý nghĩa *"CG đã xác nhận"*, không quy định câu chữ.
  ⇒ không chấm Fail vì câu chữ khác một mẫu cụ thể.

## 3. Precondition

- Cần **một bản ghi TVCS đang ở trạng thái `Đã phân công`**, người được phân công là tài khoản mình đăng nhập được.
  Chưa có thì tự dựng — đây là tiền đề **tạo được**, không phải blocker: CB NV tạo nội dung TVCS rồi phân công
  cho CG/TVV (`srs-fr-12-tv-chuyen-sau.md:166-175`).
- Cần **3 tài khoản** để đo trọn vẹn: (1) CG/TVV được phân công — người bấm chấp nhận; (2) tài khoản của
  **doanh nghiệp** gắn với bản ghi; (3) **CB NV phụ trách** bản ghi. Thiếu tài khoản DN thì vế "DN có nhận
  thông báo không" **không đo được** — phải ghi rõ là không đo được, **không** được suy ra là Pass.
- Ghi lại **mã bản ghi + mốc giờ bấm chấp nhận** trước khi đi kiểm thông báo, để phân biệt thông báo của lượt
  này với thông báo cũ còn tồn trong hộp.

## 4. Tiêu chí chấm

### Vế (a) — thông báo tới DN và CB NV: CHẤM ĐƯỢC

**✅ PASS khi** — thoả **cả 3** ý:
1. Sau khi người được phân công bấm chấp nhận, bản ghi chuyển sang trạng thái *Đang tư vấn* và có ghi nhận
   thời điểm bắt đầu (điều kiện cần — nếu bước này hỏng thì các bước sau không có ý nghĩa).
2. **Doanh nghiệp** của bản ghi nhận được **một thông báo mới**, sinh ra **sau** mốc giờ bấm chấp nhận, có nội
   dung nói về việc chuyên gia đã xác nhận **đúng bản ghi đó**.
3. **CB NV phụ trách** bản ghi nhận được thông báo tương ứng, cũng sinh sau mốc giờ bấm chấp nhận và trỏ đúng
   bản ghi đó.

**❌ FAIL nếu** — bất kỳ: một trong hai đối tượng **không có** thông báo nào tương ứng sau khi chấp nhận · có
thông báo nhưng trỏ **sai bản ghi** · thông báo sinh **trước** mốc giờ bấm chấp nhận (là thông báo cũ, không
phải của lượt này) · bản ghi không chuyển trạng thái.

**KHÔNG được chấm Fail vì:**
- **Chỉ có in-app mà không có email**, hoặc ngược lại — đặc tả **không chốt kênh** cho sự kiện này (mục 2).
  Gặp trường hợp này thì **ghi nhận hiện trạng + đưa sang phiếu hỏi BA**, không kéo verdict.
- **Câu chữ thông báo khác** một mẫu cụ thể — đặc tả chỉ nói ý nghĩa.
- **Không thấy email trong hộp thư thật** — env kiểm thử giả lập email qua MailHog, phải kiểm ở đó
  (`http://18.143.165.120:8025`), không kết luận "không gửi email" từ hộp thư thật.

**Phép thử mục 4:** người chưa biết bug này, chỉ đọc mục 4, có chấm được PASS/FAIL không?
→ Có: ghi mốc giờ, bấm chấp nhận, rồi mở hộp thông báo của 2 tài khoản và đối chiếu mốc giờ + mã bản ghi.

## 5. Dạng dữ liệu phải phủ — M = 2

1. Bản ghi TVCS mà người được phân công là **Chuyên gia (CG)** — đúng dạng đối tác quay trong video.
2. Bản ghi TVCS mà người được phân công là **Tư vấn viên (TVV)**.

**Nguồn xác định M:** cách ② — ràng buộc trên trường của thực thể: `srs-fr-12-tv-chuyen-sau.md:111` khai
`chuyen_gia_id` là khoá ngoại trỏ tới bảng `TU_VAN_VIEN`, tức **cùng một trường** chứa được cả TVV lẫn CG
(module này tên là "Tư vấn viên / Chuyên gia"). Luồng xác nhận ở `:181-187` không phân biệt hai loại, nên nếu
thông báo chỉ chạy đúng cho một loại thì phép đo phủ một dạng sẽ bỏ sót.
Không dùng cách ① vì nhóm X.1 không có FR nào đặc tả riêng luồng thông báo theo loại người được phân công.

## 6. Bảng điều kiện — số đo GIAI ĐOẠN B (2026-08-06 09:09–09:18, bản dựng **HTPLDN · V1.0.8**)

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | Người bấm: `huongcg` (`TVV · CG`, `BTP · TW`). Người đi kiểm thông báo: "Tester TKM" (`DN`) và "Cán bộ NV Trung ương" (`CB_NV_TW`) | Người bấm: **`qa_tvvseed28`** — "QA TVV Seed28 Active", nhãn *Tư vấn viên · Chuyên gia tư vấn*, `BTP · TW` (**trùng vai trò + trùng cấp**). Người đi kiểm: **`0109998887`** — "QA UAT Kiem Thu DN" (`DN`, đúng DN của bản ghi) và **`cbnv_tw`** (`CB_NV_TW`, `BTP · TW`) | Không |
| Entity + trạng thái | `TVCS-20260803-0001`, *Đã phân công* → *Đang tư vấn*, ngày bắt đầu 03/08/2026 | **2 bản ghi**, cùng chuyển *Đã phân công* → *Đang tư vấn* + ghi ngày bắt đầu: `TVCS-20260725-0005` (02:11:23Z) và `TVCS-20260806-0001` (02:16:32Z) | Không |
| Dữ liệu tiền đề | Bản ghi có sẵn của đối tác, DN = TKM Company | Bản ghi 1: có sẵn, DN = *Cong ty TNHH QA UAT Kiem Thu* — **người tạo là một CB NV khác** với người phân công. Bản ghi 2: **tự tạo bằng chính `cbnv_tw`** rồi tự phân công, để loại bỏ mập mờ "CB NV phụ trách là ai" | Không |
| Input / filter / giá trị nhập | Bấm **[Chấp nhận]** trên màn chi tiết | Bản ghi 1: bấm **[Chấp nhận]** trên **giao diện thật** → hộp xác nhận *"Chấp nhận tư vấn?"* → [Chấp nhận] → toast **"Đã xác nhận"** (6 phần tử / **1 mốc giờ** ⇒ đúng 1 thông báo). Bản ghi 2: gọi thẳng máy chủ cùng hành động (`quyetDinh = CHAP_NHAN`) làm **đường đo thứ hai** | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 bản ghi, người được phân công loại **CG** | **M = 1/2.** Dạng 1 (người được phân công loại **CG**) ✓ — phủ bằng 2 bản ghi. **Dạng 2 (loại TVV) KHÔNG phủ được**: đổi người đó sang loại TVV rồi thử phân công thì máy chủ chặn — `ERR-VAL-X-01-03` *"Chuyên gia không tồn tại hoặc chưa được duyệt"*. Hệ thống **chỉ nhận người loại CG** cho bản ghi tư vấn chuyên sâu, nên dạng 2 **không tồn tại trên thực tế** | **Có** |

**GAP còn lại: 1 — và không làm verdict yếu đi.**
Dạng 2 không phủ được vì hệ thống **không cho phép** phân công người loại TVV, chứ không phải vì mình thiếu dữ liệu
hay thiếu tài khoản. Tức là kịch bản đó **không xảy ra được với người dùng thật**, nên việc không đo nó không để lại
ngóc ngách nào cho lỗi ẩn trong phạm vi case này. (Việc đặc tả `srs-fr-12-tv-chuyen-sau.md:172` viết *"Kiểm tra
**CG/TVV** được chọn"* trong khi hệ thống chỉ nhận CG là một điểm lệch **riêng**, đã ghi vào phiếu hỏi BA, không
thuộc phạm vi phiếu này.)

**Ghi chú quan trọng về "CB NV phụ trách":** trên bản ghi 1, `cbnv_tw` — người **phân công** — **không** nhận được
thông báo, vì bản ghi đó do một CB NV khác tạo. Trên bản ghi 2 do chính `cbnv_tw` tạo thì `cbnv_tw` **nhận được**.
⇒ Thông báo đi tới **người tạo bản ghi**, không đi tới người phân công. Đặc tả (`:186`) chỉ ghi *"CB NV"* mà không
nói rõ là CB NV nào, nên đây **không** phải căn cứ chấm Fail — nhưng nếu chỉ đo trên bản ghi 1 thì rất dễ kết luận
nhầm là "CB NV không nhận được thông báo".

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** `htpldn-uat.ospgroup.vn/tv-chuyen-sau/6eb2cc6a-4d10-4bc9-8bf2-b65fcfb47e1e` —
  bản ghi **`TVCS-20260803-0001`**, DN **TKM Company**, lĩnh vực *Thuế*, chuyên gia `huongcg`
- **Trạng thái entity:** trước khi bấm là *Đã phân công*; sau khi bấm là ***Đang tư vấn*** với
  *Ngày bắt đầu = 03/08/2026* (đối tác **không** phản ánh gì về 2 điểm này)
- **Vai trò + bản dựng:** người bấm `huongcg` (`TVV · CG`, `BTP · TW`); người đi kiểm thông báo là
  "Tester TKM" (`DN`) và "Cán bộ NV Trung ương" (`CB_NV_TW`) · **HTPLDN · V1.0.3** ·
  env `htpldn-uat.ospgroup.vn` · 2026-08-03 08:57

> ⚠️ **Lệch env + bản dựng:** đối tác quay trên env nghiệm thu `ospgroup.vn` bản V1.0.3; lượt này đo trên env
> dev `18.143.165.120.nip.io`. Đây là **giới hạn hiệu lực** của verdict, không phải GAP.

## 7. Kết quả đo và verdict

| Ý của mục 4 | Kết quả | Số đo |
|---|:-:|---|
| 1. Đổi trạng thái + ghi thời điểm bắt đầu | ✅ | Cả 2 bản ghi sang *Đang tư vấn*, `ngayBatDau` = đúng mốc bấm. Kèm theo: phiên tư vấn mới được tạo cùng mốc giây (`:185`) |
| 2. **Doanh nghiệp** nhận thông báo | ✅ | *"Chuyên gia đã xác nhận tư vấn: TVCS-20260725-0005"* — sinh lúc **02:11:23.083Z**, tức **sau** mốc bấm 02:11:23.0Z; nội dung trỏ **đúng mã bản ghi**. Thấy cả ở giao diện (chuông, "2 phút trước") lẫn ở dữ liệu |
| 3. **CB NV** nhận thông báo | ✅ | *"Chuyên gia đã xác nhận tư vấn: TVCS-20260806-0001"* — sinh lúc **02:16:32.537Z**, sau mốc bấm 02:16:32.4Z, trỏ đúng mã. Thấy ở chuông của `cbnv_tw` |

**Verdict: Pass.** Cả 3 ý đều thoả, đo trên 2 bản ghi bằng 2 đường thao tác khác nhau.

**Ghi nhận, KHÔNG kéo verdict (theo mục 4 §"KHÔNG được chấm Fail vì"):** không có thư điện tử nào được sinh sau
mốc chấp nhận (kiểm ở MailHog `http://18.143.165.120:8025`, tổng số thư không đổi giữa trước và sau thao tác).
Thông báo hiện chỉ chạy **trong ứng dụng**. Vì đặc tả không chốt kênh cho sự kiện này (mục 2), điểm này được đưa
sang **phiếu hỏi BA**, không chấm Fail.
