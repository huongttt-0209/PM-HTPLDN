# Chuẩn chấm đã khóa — QLNDTVVCG_38 (dòng 288)

> **FLOW 04 — GIAI ĐOẠN A.** Bug dev báo đã fix, **KHÔNG có hồ sơ nội bộ**. Nguồn chuẩn chấm duy nhất = SRS
> tại đường dẫn prompt cấp. Chưa mở màn đang tranh chấp.
>
> **Đặc tả — nguồn duy nhất:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`
> — file chính `srs-fr-12-tv-chuyen-sau.md` (1.681 dòng, mtime **06/08/2026 22:52**), phụ trợ `srs-v3.5.md`.
> **Mọi số dòng dưới đây tự mở file đọc lại ngày 2026-08-07.**
>
> Chức năng: **FR-X.1-01 (UC147)** — màn danh sách **SCR-X1-01**, thanh hành động hàng loạt.
>
> 🔴 **KẾT LUẬN NGƯỢC VỚI GIẢ THIẾT TRONG PROMPT: SRS *KHÔNG* im lặng về phân công hàng loạt.**
> `srs-fr-12-tv-chuyen-sau.md:1127` **quy định rõ** nút **`[Phân công CG hàng loạt]`** trên thanh hành động
> hàng loạt của màn danh sách, chỉ áp cho bản ghi **`TIEP_NHAN`**. Yêu cầu này còn có **từ bản v3**
> (`srs-v3/srs-fr-12-tv-chuyen-sau.md:886`) ⇒ không phải mục mới thêm, không phải suy diễn.
> ⇒ Vế lõi của phiếu là **`MATCH`**, route **`TEST`**. Chỉ **một vế con** ("cùng MỘT chuyên gia cho tất cả")
> là `GAP` → BA.
>
> ⚠️ **Bằng chứng đối tác:** phiếu khai `QLNDTVVCG_38.jpg` (khớp `output/UAT_doi-tac/bug-con-fail-doi-tac-2026-07-31.csv:319`),
> **nhưng tệp này KHÔNG có trong repo** — `output/UAT_doi-tac/partner-evidence/` chỉ có
> `QLNDTVVCG_03/04/06/07/08/11/15/17/20/22/23/27/36/41`. **Không mở xem được.**
> Case vẫn **tự tái hiện được** (thao tác nằm trọn trên màn danh sách) ⇒ chạy tiếp, khai rõ điều kiện tự dựng.

---

## 1. Lỗi gốc — nguyên văn phiếu đối tác

| | Nội dung |
|---|---|
| **Mã TC / dòng** | `QLNDTVVCG_38` — dòng **288** |
| **Mô tả** | "Phân công chuyên gia hàng loạt" |
| **Điều kiện** | 1. Đăng nhập hệ thống thành công |
| **Các bước** | 1. Chọn menu "Tư vấn" => "Tư vấn chuyên sâu" · 2. Chọn ít nhất 1 dòng bằng ô chọn; các dòng được chọn đều ở trạng thái "Tiếp nhận" · 3. Bấm nút Phân công hàng loạt |
| **Kết quả mong đợi (nguyên văn)** | "Hệ thống mở cửa sổ phân công, áp dụng chuyên gia đã chọn cho tất cả yêu cầu được chọn đồng thời." |
| **Trạng thái** | Fail |
| **Dopai** | N/R |
| **TKM phản hồi lần 1** | "Hệ thống hiển thị popup 'Phân công hàng loạt chưa được hỗ trợ'" |
| **Trạng thái dev fix** | Fixed |
| **Ảnh bằng chứng** | `QLNDTVVCG_38.jpg` — **không có trong repo** |

> 🔴 **Ô TKM là mô tả một LỖI SẢN PHẨM**, không phải giải thích không tái hiện được: hệ thống **có** nút
> nhưng **từ chối bằng thông báo "chưa được hỗ trợ"**. Đây chính là vế phải đo tới cùng — **cấm Pass bằng
> quan sát tĩnh** ("thấy nút rồi").

---

## 2. Đặc tả đối chiếu — trích dẫn `file:dòng` (tự mở đọc lại 2026-08-07)

### 2.1 Dòng quyết định — SRS CÓ quy định phân công hàng loạt

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1102` | `### SCR-X1-01: Danh sách Tư vấn pháp luật chuyên sâu` |
| `srs-fr-12-tv-chuyen-sau.md:1110` | `Breadcrumb > Tiêu đề + nút hành động > Tab phân loại (3 tab) > Thanh lọc & tìm kiếm > Bảng dữ liệu > **Thanh hành động hàng loạt** > Phân trang` |
| `srs-fr-12-tv-chuyen-sau.md:1125` | `| 10 | content | Bảng nội dung TVCS | table | **Checkbox** / Mã (TVCS-{YYYYMMDD}-{SEQ}) / Tiêu đề / Tên DN / Tên CG / Lĩnh vực PL / Trạng thái SM-TVCS (badge) / Ngày tư vấn / Ngày tạo / Hành động (Xem / Sửa / Phân công CG / Hủy) | click hàng -> xem chi tiết | luôn hiển thị |` |
| 🔴 **`srs-fr-12-tv-chuyen-sau.md:1127`** | `| 12 | action-bar | Thanh hành động hàng loạt | button-group | **[Phân công CG hàng loạt] (chỉ bản ghi TIEP_NHAN)** / [Công khai chuyên trang hàng loạt] + [Hủy công khai hàng loạt] (chỉ bản ghi DA_DUYET — BR-PUBLIC-01) | **click -> action nhiều bản ghi** | **khi >= 1 checkbox chọn**; nút enable theo trạng thái dòng được chọn |` |
| `srs-fr-12-tv-chuyen-sau.md:1116` | `| 1 | toolbar | Breadcrumb | breadcrumb | "Trang chủ > Tư vấn > Tư vấn pháp luật chuyên sâu" | navigate | luôn hiển thị |` |
| `srs-fr-12-tv-chuyen-sau.md:1134` | `| TIEP_NHAN | **Tiếp nhận** | Xanh dương |` *(bảng nhãn trạng thái SM-TVCS — tên tiếng Việt phiếu dùng là ĐÚNG)* |
| `srs-fr-12-tv-chuyen-sau.md:1135` | `| PHAN_CONG | **Đã phân công** | Vàng nhạt |` *(nhãn sau khi phân công thành công)* |
| `srs-fr-12-tv-chuyen-sau.md:1118` | `| 3 | filter-bar | Tab phân loại | tab | 3 tab với số đếm: **Chờ xử lý (TIEP_NHAN + PHAN_CONG)** / Đang tư vấn (…) / Hoàn thành (…) | click -> filter theo nhóm trạng thái | luôn hiển thị |` |
| `srs-fr-12-tv-chuyen-sau.md:1123` | `| 8 | filter-bar | Dropdown Trạng thái | select | TIEP_NHAN / PHAN_CONG / … | change -> filter | luôn hiển thị |` |

**Nền lịch sử (chứng minh không phải mục mới của v3.5):**

| Dòng | Nguyên văn |
|---|---|
| `srs-v3/srs-fr-12-tv-chuyen-sau.md:886` | `| 12 | action-bar | Thanh hành động hàng loạt | button-group | [Phân công CG hàng loạt] | click -> phân công nhiều bản ghi | khi >= 1 checkbox chọn, chỉ bản ghi TIEP_NHAN |` |
| `srs-v3.5/CHANGELOG-v3-to-v3.5.md:1567` | `- §3 Màn hình SCR-X1-01 — thanh hành động hàng loạt **mở rộng** (Công khai / Hủy công khai hàng loạt cho bản ghi đã duyệt) (line 1082)` *(v3.5 chỉ **thêm** 2 nút công khai; nút phân công hàng loạt **giữ nguyên** từ v3)* |

### 2.2 Dòng quyết định — hệ quả bắt buộc sau khi phân công

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:166` | `**Processing — Phân công CG** (TIEP_NHAN → PHAN_CONG) `[GAP-X.1-01]`` |
| `srs-fr-12-tv-chuyen-sau.md:176` | `| 1 | Kiểm tra quyền CB NV và phạm vi đơn vị | BR-AUTH-01, BR-AUTH-08 |` |
| `srs-fr-12-tv-chuyen-sau.md:177` | `| 2 | Kiểm tra trạng thái hiện tại = TIEP_NHAN | SM-TVCS |` |
| 🔴 `srs-fr-12-tv-chuyen-sau.md:178` | `| 3 | Kiểm tra CG được chọn: phải **loại Chuyên gia (`loai_tvv = 'CG'`)**, đang hoạt động, **chuyên môn phù hợp lĩnh vực** `[BA chốt 2026-08-06]` | — |` |
| `srs-fr-12-tv-chuyen-sau.md:179` | `| 4 | Cập nhật chuyen_gia_id, trạng thái → PHAN_CONG | — |` |
| `srs-fr-12-tv-chuyen-sau.md:180` | `| 5 | Gửi thông báo CG (in-app + email): nội dung yêu cầu + SLA 2 ngày LV xác nhận | BR-NOTIF-01 |` |
| `srs-fr-12-tv-chuyen-sau.md:1546` | `| TIEP_NHAN | PHAN_CONG | CB NV phân công | Có CG phù hợp (`loai_tvv='CG'`) | TB CG (in-app + email) | FR-X.1-01 | BR-NOTIF-01 |` |
| `srs-fr-12-tv-chuyen-sau.md:1517` | `    TIEP_NHAN --> PHAN_CONG : CB NV phân công` *(SM-TVCS)* |
| `srs-fr-12-tv-chuyen-sau.md:111` | `| 3 | chuyen_gia_id | identifier | N | FK -> TU_VAN_VIEN, phải đang hoạt động **và `loai_tvv = 'CG'`** … Để trống khi bản ghi mới tạo ở TIEP_NHAN, **gán khi phân công** | — | người dùng chọn |` |
| 🔴 `srs-v3.5.md:1440` | `| TVCS_ASSIGN | Phân công người tư vấn | **CB_NV_{cap}** | `user.don_vi_id = record.don_vi_id` AND `record.trang_thai = TIEP_NHAN` AND người được chọn có `loai_tvv = 'CG'` | FR-X.1-01 |` |

### 2.3 Dòng nền — khuôn "cửa sổ phân công" (chỉ đặc tả cho MÀN CHI TIẾT)

| Dòng | Nguyên văn |
|---|---|
| `srs-fr-12-tv-chuyen-sau.md:1180` | `- Phân công CG (gộp từ MH-12.4): **modal overlay** với gợi ý TOP 5 CG (lĩnh vực khớp, điểm TB DESC, workload ASC) + tìm kiếm CG thủ công + ghi chú + info SLA (2 ngày LV xác nhận)` |
| `srs-fr-12-tv-chuyen-sau.md:1169` | `… Chuyên gia (dropdown searchable WHERE `trang_thai` hoạt động AND `loai_tvv = 'CG'`; **khoá ở chế độ thêm mới** … việc gán người tư vấn **chỉ thực hiện qua nút [Phân công CG]** để chạy đúng bước kiểm loại, gửi thông báo và đếm SLA 2 ngày `[BA chốt 2026-08-06]` …` |

> ⚠️ `:1180` nằm trong **"Quy tắc tương tác" của SCR-X1-02 (màn CHI TIẾT)**, mô tả cửa sổ phân công **một bản
> ghi**. SRS **không** nói cửa sổ này dùng lại cho luồng hàng loạt ở SCR-X1-01. Dùng nó làm **khuôn tham chiếu**
> để hiểu "cửa sổ phân công" là gì, **không** biến thành tiêu chí chấm cho luồng hàng loạt.

### 2.4 Đã tra gì để dám nói "SRS im lặng" ở vế C5

- `grep -n "hàng loạt|bulk|đồng thời|nhiều bản ghi|nhiều yêu cầu|chọn nhiều|theo lô|checkbox|Checkbox"` trên
  **toàn bộ** `srs-fr-12-tv-chuyen-sau.md` → **đúng 3 kết quả**: `:1110`, `:1125`, `:1127`. Không còn dòng nào
  khác nói về thao tác theo lô của nhóm X.1.
- Đọc **trọn** §2 FR-X.1-01 `:86–349` — toàn bộ 9 khối Processing (`:128`, `:136`, `:146`, `:155`, `:166`,
  `:183`, `:195`, `:206`, `:217`, `:229`, `:240`, `:252`, `:263`, `:273`) đều mô tả **một bản ghi**; **không có**
  khối Processing riêng cho phân công hàng loạt. Bộ **Error Handling** `:323–333` (E1–E9) **không có** mã lỗi
  nào cho thao tác theo lô. Bộ **Acceptance Criteria** `:337–348` **không có** dòng nào cho hàng loạt.
- Đọc **trọn** §3 Màn hình `:1098–1231` và §5 SM-TVCS `:1504–1558`.
- `grep -rn "hàng loạt" --include="srs-fr-*.md"` toàn thư mục để tìm **khuôn anh em**:
  - `srs-fr-04-chuyen-gia-tvv.md:1462` — `**Phê duyệt hàng loạt** … → mở MD-PHE-DUYET-HANG-LOAT (**bảng nhập Số quyết định cho từng hồ sơ**) → áp dụng cho tất cả.` ⇒ khuôn **nhập TỪNG bản ghi** rồi áp một lượt.
  - `srs-fr-02-hoi-dap.md:1053` — nút Phê duyệt hàng loạt có **tối đa 100 bản ghi/lần**, **optimistic locking per-record**, **modal báo cáo cuối** `"Duyệt thành công {S}, lỗi {E}"`.
  - `srs-fr-05-vu-viec.md:970` / `:1658` — có nơi SRS **nói thẳng "KHÔNG hỗ trợ hàng loạt"**.
  ⇒ Dự án **biết cách viết rõ cả 3 kiểu**: có-hàng-loạt-một-giá-trị, có-hàng-loạt-nhập-từng-dòng, và
  không-có-hàng-loạt. Với TVCS, SRS **chỉ khẳng định có nút**, **không** chọn kiểu nào ⇒ đây là **im lặng thật**,
  không phải mình chưa tìm ra.
- `grep -n "Phân công CG hàng loạt|Phân công hàng loạt"` trên `srs-v3.5.md` và `CHANGELOG-v3-to-v3.5.md`
  → **rỗng** ⇒ hai file này **không** bổ sung và cũng **không mâu thuẫn** với `srs-fr-12:1127`.

---

## 3. BUG SCOPE LOCK — các dòng `Cn`

```
C1 · Danh sách TVCS có ô chọn (checkbox) trên từng dòng
   · srs-fr-12:1125 · MATCH · route TEST
   · Mở màn danh sách → đếm ô chọn trên dòng

C2 · Chọn ≥1 dòng ở trạng thái "Tiếp nhận" → thanh hành động hàng loạt hiện, có nút phân công
     chuyên gia hàng loạt ở trạng thái dùng được
   · srs-fr-12:1127 (+ :1110, :1134; nền v3: srs-v3/srs-fr-12:886) · MATCH · route TEST
   · Tích 2 dòng "Tiếp nhận" cùng lĩnh vực → quan sát thanh hành động

C3 · Bấm nút → hệ thống MỞ BƯỚC CHỌN CHUYÊN GIA để phân công (KHÔNG từ chối bằng thông báo
     "chưa được hỗ trợ")  ← đây là vế bug gốc
   · srs-fr-12:1127 ("click -> action nhiều bản ghi") · MATCH · route TEST
   · Bấm nút thật, cài bộ bắt thông báo TRƯỚC khi bấm
   ⚠ SRS IM LẶNG về HÌNH THỨC (cửa sổ nổi / ngăn kéo / tại chỗ) → chấm BẢN CHẤT, cấm Fail vì hình thức

C4 · Xác nhận xong → TẤT CẢ bản ghi được chọn đều được phân công: chuyển "Đã phân công"
     + có tên chuyên gia
   · srs-fr-12:1127 + :179 + :1546 + :1135 + :111 · MATCH · route TEST
   · Tải lại danh sách, đọc lại trạng thái + cột Tên CG của TỪNG mã đã chọn

C5 · Áp dụng CÙNG MỘT chuyên gia đã chọn cho TẤT CẢ yêu cầu được chọn (một lần chọn, không phải
     chọn riêng từng dòng)
   · IM LẶNG — srs-fr-12:1127 chỉ ghi "action nhiều bản ghi"; khối Processing phân công :166-181
     chỉ mô tả MỘT bản ghi; module anh em dùng khuôn NHẬP TỪNG DÒNG (srs-fr-04:1462)
   · GAP · route BA · CẤM Pass vế này; chỉ ghi nhận hiện trạng
```

**Tổng hợp quan hệ:** `C1·C2·C3·C4 = MATCH` → `TEST` (4 vế này quyết định triệu chứng đối tác báo).
`C5 = GAP` → `BA`.

**Hệ quả verdict logic (Flow 04 §Ca biên — case gộp nhiều vế):**

| Kết quả đo | Verdict logic |
|---|---|
| C1–C4 đạt hết | **Cần BA** (còn `GAP` C5) — tóm tắt **phải ghi rõ** `WEB HIỆN TẠI: đúng kỳ vọng đối tác`, và câu hỏi BA có mục đích **bổ sung điều này vào đặc tả**, KHÔNG phải chặn bàn giao |
| ≥1 vế trong C1–C4 hỏng | **Reopen + cần BA** — nêu riêng vế hỏng và câu hỏi BA cho C5 |
| Không dựng nổi tiền đề (§4) | **Chưa chốt** — nêu đúng dữ kiện còn thiếu |

**Câu bắt buộc cho vế `GAP` C5 (ghi nguyên văn vào kết quả):**
> `CẦN BA CONFIRM: đối tác kỳ vọng thao tác phân công hàng loạt áp dụng CÙNG MỘT chuyên gia đã chọn cho toàn bộ`
> `yêu cầu được chọn; SRS quy định có nút [Phân công CG hàng loạt] cho bản ghi Tiếp nhận nhưng KHÔNG quy định`
> `chọn chuyên gia chung hay chọn riêng từng bản ghi (srs-fr-12-tv-chuyen-sau.md:1127; khối Processing phân công`
> `:166-181 chỉ mô tả một bản ghi; module anh em srs-fr-04-chuyen-gia-tvv.md:1462 dùng khuôn nhập từng hồ sơ);`
> `web/dev hiện tại <điền sau khi đo>.`
> **Câu hỏi:** *Với phân công chuyên gia hàng loạt của Tư vấn chuyên sâu, cán bộ chọn **một** chuyên gia áp cho
> mọi hồ sơ đã chọn, hay chọn chuyên gia **riêng cho từng hồ sơ** trong cùng một cửa sổ? Nếu là một chuyên gia
> chung thì xử lý thế nào khi các hồ sơ đã chọn thuộc **lĩnh vực khác nhau**, trong khi bước 3 của khối Phân
> công (`:178`) buộc kiểm "chuyên môn phù hợp lĩnh vực"?*

**Nằm NGOÀI scope — CẤM biến thành tiêu chí chấm** (SRS `srs-fr-12` im lặng, expected không nhắc):
giới hạn số bản ghi/lần · báo cáo lỗi từng bản ghi kiểu `"thành công {S}, lỗi {E}"` · khóa lạc quan / xử lý
tranh chấp phiên bản · hành vi khi chọn lẫn dòng khác trạng thái · hành vi khi chọn dòng khác đơn vị · tự bỏ
chọn sau khi xong · 2 nút công khai/hủy công khai hàng loạt (`:1127`, khác vế) · nút "Phân công CG" **từng
dòng** ở cột Hành động (`:1125`, khác vế).
*(Các quy tắc này chỉ tồn tại ở module khác — `srs-fr-02:1053`, `srs-fr-09:274` — **không** áp cho nhóm X.1.)*

---

## 4. Tiền đề tối thiểu

### 4.1 Vai trò / tài khoản

**Vai trò của vế này = CÁN BỘ NGHIỆP VỤ**, cùng đơn vị với bản ghi — `srs-v3.5.md:1440` (`TVCS_ASSIGN`,
`CB_NV_{cap}`, `user.don_vi_id = record.don_vi_id`) + `srs-fr-12:176`.
CG · TVV · NHT · CB PD **không** phải vai trò của vế này (`srs-v3.5.md:1436-1446`).

| Vai trò | Tài khoản (env nội bộ `https://18.143.165.120.nip.io`) | Mật khẩu | Ghi chú |
|---|---|---|---|
| **CB NV cấp TW — ra verdict** | `cbnv_tw` (dự phòng cùng vai trò + cấp: `cbnv_tw_01`, `cbnv_tw_02`) | `Test@1234` | `output/UAT_doi-tac/input/input.md:19, 38, 46`. Cấp TW nhìn dữ liệu **mọi đơn vị** (`srs-v3.5.md:1375`) — nhưng **quyền GHI vẫn buộc cùng đơn vị** (`:1440`) ⇒ phải chọn bản ghi **thuộc đúng đơn vị của tài khoản**, nếu không sẽ bị từ chối **đúng đặc tả** |
| CB NV cấp ĐP (thay thế) | `cbnv_dp_01` | `Test@1234` | `input.md:31-33`, đơn vị `…8002-000000000006`, cấp ĐP |
| **CẤM ra verdict** | `admin` | — | Vế này là thao tác có ràng buộc phân quyền (`:1440`) — quyền rộng che đúng loại lỗi đang đo |

Env đối tác `https://htpldn-uat.ospgroup.vn` dùng **bộ tài khoản khác** (`input.md:120–131`): `cbnv_tw` /
`Test@1234` đã kiểm chứng dùng được; mã xác thực ở MailHog của **chính env đó** (`input.md:123`).
**Phải khai rõ đo trên env nào** — TKM báo lỗi trên env đối tác.

### 4.2 Dữ liệu

| Cần | Số lượng | Vì sao |
|---|---|---|
| Bản ghi TVCS ở **`TIEP_NHAN`**, **thuộc đơn vị của tài khoản đăng nhập**, **cùng một lĩnh vực PL** | **≥2** (nên 3) | `:1127` nút chỉ áp cho `TIEP_NHAN`; `:1440` buộc cùng đơn vị. **≥2** mới chứng minh được "hàng loạt" — 1 dòng không phân biệt được với phân công đơn lẻ. **Cùng lĩnh vực** để tránh FAIL oan ở §6.1 bẫy 3 |
| **Chuyên gia** `loai_tvv = 'CG'`, **đang hoạt động**, **chuyên môn khớp lĩnh vực** của các bản ghi trên | **≥1** | `:178`, `:111`, `:1546`, `:1440`. **Thiếu → cửa sổ chọn chuyên gia RỖNG** — đây là thiếu tiền đề, KHÔNG phải lỗi |

**Cách dựng bản ghi `TIEP_NHAN`** (seed hợp lệ — không phải hành vi đang tranh chấp):
CB NV bấm **`[+ Thêm yêu cầu TV]`** trên màn danh sách (`:1117`) → nhập DN, Lĩnh vực PL, Tiêu đề, Nội dung TV,
Ngày tư vấn. Ô **Chuyên gia bị khóa ở chế độ thêm mới** và hồ sơ **luôn vào `TIEP_NHAN` với ô này trống**
(`:1169`, `:111`, `:1516`) ⇒ **đúng tiền đề, không cần thao tác thêm**. Dùng **cùng một Lĩnh vực PL** cho cả
2–3 bản ghi. Seed là mutate môi trường ⇒ **khai vào báo cáo: tạo mã nào · trên env nào · lĩnh vực gì**.

**Chuyên gia trên env nội bộ:** `qa_tvvseed28` / `Test@1234` — QA đã đổi `loaiTvv` **TVV→CG** ngày 21/07/2026
(`input.md:114–117`, `tuVanVienId = 98cfd963-3cd3-4c8a-bfa9-625460824d6d`), chính vì *"env nip.io ban đầu 0 TVV
loaiTvv=CG trong đơn vị → modal Phân công chuyên gia của TVCS rỗng"*. Thuộc **Cục Bổ trợ tư pháp - Bộ Tư pháp,
cấp TW** ⇒ ghép với tài khoản `cbnv_tw*`.
🔴 **Trên env đối tác `ospgroup.vn` chưa biết có CG hợp lệ hay không — phải kiểm TRƯỚC khi bấm**, nếu không sẽ
FAIL oan y hệt sự cố 21/07.

---

## 5. Đường đo ngắn nhất + đối chứng độc lập

**Đường UI (1 đường duy nhất — luật khóa 3):**
1. Đăng nhập `cbnv_tw` / `Test@1234`. **Tải lại trang bằng địa chỉ**; ghi bó mã FE + `last-modified` + `etag`
   + chuỗi phiên bản ở chân sidebar.
2. **Kiểm tiền đề chuyên gia TRƯỚC** (chống FAIL oan): mở **một** hồ sơ `TIEP_NHAN`, bấm nút Phân công **từng
   dòng** (`:1125`) và xác nhận danh sách chuyên gia **không rỗng** → **đóng lại, KHÔNG xác nhận** (không được
   tiêu mất bản ghi tiền đề). Rỗng ⇒ dừng, seed CG, khai rõ.
3. Menu **Tư vấn → Tư vấn pháp luật chuyên sâu** (`:1116`). Lọc **Trạng thái = Tiếp nhận** (`:1123`) hoặc tab
   **"Chờ xử lý"** (`:1118`). Tích **2 dòng cùng lĩnh vực, cùng đơn vị**. **Ghi lại 2 mã `TVCS-…`.**
4. Chụp 1 ảnh thanh hành động hàng loạt (bằng chứng C1 + C2).
5. **Cài bộ bắt thông báo TRƯỚC khi bấm** (`output/UAT_doi-tac/tools/toast-capture.js` — **cấm lọc trùng**,
   đọc `innerText`, đếm theo **mốc giờ khác nhau**, đếm kèm **số lời gọi**). Bấm nút phân công hàng loạt.
6. Ghi **nguyên văn** những gì hiện ra (C3): mở được bước chọn chuyên gia, hay ra thông báo từ chối kiểu
   *"chưa được hỗ trợ"*. Nếu mở được → chọn CG hợp lệ → xác nhận. Ghi lại **giao diện cho chọn 1 CG chung hay
   chọn riêng từng dòng** (dữ kiện cho C5 — **ghi nhận, không chấm**).

**Đối chứng độc lập (đúng 1 đường, khác đường UI):**
- **Tải lại danh sách bằng địa chỉ** rồi đọc lại **trạng thái + cột Tên CG** của **từng mã** đã chọn ở bước 3.
  Kỳ vọng theo `:1135` + `:179`: nhãn **"Đã phân công"** + có tên chuyên gia — **trên TẤT CẢ** các mã (C4).
- Hoặc đọc lại chính các bản ghi đó **từ máy chủ bằng chính phiên đăng nhập đó**, so `trang_thai` +
  `chuyen_gia_id`. **KHÔNG tự đoán đường dẫn** — lấy đường dẫn từ lời gọi thật của màn danh sách, hoặc tra
  `/api/docs-json` trước khi dùng.
- **Bấm lại cùng một nút KHÔNG tính là phương pháp thứ hai.** Hai đường khớp thì dừng, không thêm đường thứ ba.
- **Hai phép mâu thuẫn ⇒ CHƯA được chốt** — ghi cả hai, hỏi user.

---

## 6. Bẫy chấm sai

### 6.1 ⚠️ Bẫy **FAIL oan**

1. 🔴 **Cửa sổ chọn chuyên gia RỖNG.** Nếu đơn vị không có ai `loai_tvv='CG'` + đang hoạt động thì danh sách
   rỗng là **thiếu tiền đề**, không phải lỗi (`:178`, `:111`, `:1546`; sự cố có thật `input.md:114–117`).
   **Phải kiểm trước ở bước 2 của §5.**
2. 🔴 **Nút mờ / không bấm được vì dòng đã chọn KHÔNG ở "Tiếp nhận".** `:1127` ghi rõ *"chỉ bản ghi TIEP_NHAN"*
   và *"nút enable theo trạng thái dòng được chọn"* ⇒ **đúng đặc tả**.
3. 🔴 **Bị từ chối vì lĩnh vực không khớp chuyên môn CG.** `:178` buộc kiểm *"chuyên môn phù hợp lĩnh vực"*.
   Chọn các bản ghi **khác lĩnh vực** rồi Fail = FAIL oan. **Seed cùng lĩnh vực.**
4. **Bị từ chối vì bản ghi khác đơn vị.** `:1440` buộc `user.don_vi_id = record.don_vi_id` — kể cả tài khoản
   cấp TW **nhìn thấy** bản ghi đơn vị khác (`srs-v3.5.md:1375`) thì **ghi vẫn bị chặn đúng đặc tả**.
   *(Đã có tiền lệ: `F3-devfix-2026-08-07/TIEN-DO.md:148` — `cbnv_tw_02` nhìn thấy + tích chọn được bản ghi
   khác đơn vị.)*
5. **Hình thức "cửa sổ".** SRS **im lặng** về việc luồng hàng loạt dùng cửa sổ nổi / ngăn kéo / khối tại chỗ
   (`:1180` chỉ đặc tả cho **màn chi tiết**). Chấm bản chất *"có bước chọn chuyên gia rồi phân công"*.
6. **Không có báo cáo lỗi từng bản ghi, không giới hạn 100 bản ghi/lần, không tự bỏ chọn sau khi xong.**
   `srs-fr-12` **im lặng** — các quy tắc đó chỉ có ở `srs-fr-02:1053` và `srs-fr-09:274`, **không áp** cho X.1.
7. **Tưởng "mất dòng" sau khi phân công.** Tab **"Chờ xử lý" gộp `TIEP_NHAN` + `PHAN_CONG`** (`:1118`) ⇒ dòng
   **vẫn nằm nguyên tab đó**, chỉ đổi nhãn sang "Đã phân công". Nếu đang lọc **Trạng thái = Tiếp nhận**
   (`:1123`) thì dòng biến mất là **đúng** — đừng Fail.
8. **Không thấy thông báo trong ứng dụng gửi tới CG.** `:180` yêu cầu thông báo cho CG, nhưng đó là **hệ quả
   phía máy chủ**, expected của phiếu **không nhắc** ⇒ ngoài scope; thiếu thì ghi **candidate một dòng**,
   không kéo verdict.

### 6.2 ⚠️ Bẫy **PASS oan**

1. 🔴 **Thấy nút [Phân công hàng loạt] hiện ra là Pass.** Vế bug gốc là **bấm vào thì bị từ chối bằng thông
   báo "chưa được hỗ trợ"**. **CẤM Pass bằng quan sát tĩnh** — phải bấm thật và chạy tới cùng (C3 + C4).
2. 🔴 **Thông báo "Phân công thành công" là Pass.** Không đủ. Phải **tải lại danh sách** và đọc lại trạng thái
   + tên chuyên gia của **TỪNG mã** đã chọn (`:1135`, `:179`).
3. 🔴 **Chỉ 1 trong N bản ghi đổi trạng thái mà vẫn Pass.** *"Đúng một phần vẫn là FAIL"* cho vế C4 — vế
   expected là *"cho **tất cả** yêu cầu được chọn"*.
4. 🔴 **Chọn đúng 1 dòng rồi Pass.** Phiếu ghi *"ít nhất 1 dòng"*, nhưng vế bug là **HÀNG LOẠT**; 1 dòng
   **không phân biệt được** với nút phân công từng dòng ở cột Hành động (`:1125`). **Bắt buộc ≥2 dòng.**
5. 🔴 **Chấm C5 thành `MATCH` vì "web làm đúng expected".** Luật khóa 5 cấm — kết quả web **không** biến
   `GAP` thành `MATCH`. Web đúng y kỳ vọng thì vẫn **Cần BA**, và tóm tắt phải ghi rõ
   `WEB HIỆN TẠI: đúng kỳ vọng đối tác` để người ngoài không đọc nhầm thành lỗi chưa xử lý.
6. **Dùng `admin`.** Che ràng buộc `TVCS_ASSIGN` (`srs-v3.5.md:1440`) → verdict vô hiệu.
7. **Bộ bắt thông báo lọc trùng hoặc dùng `textContent`.** Lọc trùng che thông báo đúp (Pass oan);
   `textContent` đọc cả nút ẩn (bug ma). Dùng `innerText`, đếm theo **mốc giờ**, đếm kèm **số lời gọi**.
   Cài **TRƯỚC** khi bấm; cài lại sau mỗi lần chuyển màn.
8. **Bản dựng cũ trong tab / nhầm env.** Tải lại bằng địa chỉ, ghi vân tay bản dựng. TKM báo trên env đối tác
   `htpldn-uat.ospgroup.vn`; đo trên env nội bộ thì verdict chỉ có hiệu lực cho **env + bản dựng đã đo** —
   ghi câu giới hạn này.

---

## 7. Kết luận sơ bộ — route

| | |
|---|---|
| **Quan hệ SRS ↔ expected** | **C1·C2·C3·C4 = `MATCH`** · **C5 = `GAP`** (SRS im lặng về "cùng MỘT chuyên gia cho tất cả") |
| **Route** | 🟢 **`TEST`** cho C1–C4 (quyết định triệu chứng đối tác báo) + 🟡 **`BA`** cho C5 |
| **Vì sao KHÔNG chốt BA ngay ở Giai đoạn A** | Flow 04 chỉ cho chốt-BA-ngay khi **mọi** vế đều `DIFF/GAP`. Ở đây còn **4 vế `MATCH` bắt buộc phải đo** — trong đó C3 chính là triệu chứng TKM mô tả (*popup "chưa được hỗ trợ"*) |
| **Cảnh báo lớn nhất** | Giả thiết trong prompt (*"nếu SRS chỉ quy định phân công từng bản ghi và không hề có hàng loạt"*) **KHÔNG đúng** — `srs-fr-12:1127` quy định rõ nút, từ v3. **Nếu web vẫn báo "chưa được hỗ trợ" thì đó là Reopen, KHÔNG phải chuyện BA phải chốt.** |
| **Rủi ro FAIL oan cao nhất** | Cửa sổ chọn chuyên gia rỗng do env không có `loai_tvv='CG'` — **kiểm trước, seed trước** |
| **Chưa có verdict** | Đúng — file này chỉ khóa chuẩn chấm |

**Nhắc lại luật khóa 5:** sau khi mở màn, **cấm** đổi `MATCH/DIFF/GAP` để khớp kết quả đo. Đổi chỉ hợp lệ khi
dẫn được **dòng SRS mới đọc được**.

**Nhắc ca biên Flow 04:** không có ảnh "lỗi cũ" của chính mình (tệp `QLNDTVVCG_38.jpg` **không có trong repo**)
⇒ **không suy ra được "fix có tác dụng"**, chỉ kết luận được **hiện trạng đúng/sai so với đặc tả**.

**Ảnh chụp lưu đúng:** `output/UAT_doi-tac/reverify-week-5/F6-flow04-devfix-2026-08-07/image/`.
