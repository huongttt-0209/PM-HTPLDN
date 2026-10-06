# Bàn giao lô F5 — verify dev fix, nhóm Báo cáo kết quả CT HTPLDN · 2026-08-07

**Phạm vi:** 7 phiếu, dòng **335–340** + **342**, tab `bug` của
`https://docs.google.com/spreadsheets/d/1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` (gid `1714340219`).
**Quy trình áp dụng:** [`flows/04-verify-bug-dev-fix-khong-ho-so.md`](../../../../flows/04-verify-bug-dev-fix-khong-ho-so.md)
— Giai đoạn A (khóa chuẩn chấm trước khi mở màn) → Giai đoạn B (đo).
**Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
(1.610 dòng). Mọi số dòng trích trong báo cáo đều **tự mở file đếm lại ngày 2026-08-07**.

**Môi trường verify:** `https://18.143.165.120.nip.io` · bó mã giao diện **`index-D4Buvu4S.js`**
(07/08/2026 02:23 VN) · nhãn phiên bản trên thanh bên **HTPLDN · V1.0.9**.

> ⚠️ **Bó mã đổi giữa lô.** Phiếu 1 (LBCKQTHCT_01) đo trên **`index-DsMHK7Dp.js`** (07/08 01:51);
> từ phiếu 2 trở đi là **`index-D4Buvu4S.js`** (07/08 02:23). Đã ghi rõ trong từng báo cáo; kết luận của
> phiếu 1 chỉ có hiệu lực cho bó mã cũ.
>
> ⚠️ **Khác môi trường với đối tác.** Bằng chứng đối tác quay trên `htpldn-uat.ospgroup.vn`, nhãn
> **V1.0.3** (03/08/2026). Mọi kết luận trong lô là **kết luận cho bản dựng nội bộ đo được**.

---

## 1. Kết quả 7 phiếu

| Dòng | Mã TC | Verdict | Ô `Trạng thái dev fix` | Tóm tắt một dòng |
|---|---|---|---|---|
| 335 | `LBCKQTHCT_01` | Cần BA | **BA confirm** | Lỗi đối tác báo (403 `ERR-AUTH-VPD`) đã hết; còn vế rơi vùng đặc tả im lặng |
| 336 | `LBCKQTHCT_03` | Pass | **Test done** | Biểu 21a nay có đủ 4 cột (đối tác quay bản cũ chỉ có 2 cột) |
| 337 | `LBCKQTHCT_04` | Pass | **Test done** | Biểu 21b có đủ "Số liệu kỳ trước" + "Ghi chú"; phải seed đợt `CA_HAI` mới đo được |
| 338 | `LBCKQTHCT_05` | Cần BA | **BA confirm** | Khối *Nhận xét, kiến nghị* có và lưu/đọc lại được, nhưng chỉ hiện sau [Lập báo cáo] |
| 339 | `LBCKQTHCT_06` | Cần BA | **BA confirm** | Khối *Chương trình HTPL liên quan* có và dùng được, cùng vấn đề thời điểm hiển thị như 338 |
| 340 | `TPDBCKQTHCT_01` | **Reopen** | **Reopen** | Triệu chứng cũ hết, nhưng **không trình duyệt được** — 11/13 chỉ tiêu không có ô nhập mà vẫn bị báo "còn thiếu" |
| 342 | `GKQTHCTHTPL_01` | Cần BA | **BA confirm** | "Forbidden" đã hết, gửi TW chạy trót lọt 4/5 vế; vế trạng thái ĐỢT vướng mâu thuẫn đặc tả |

**Đã ghi + đọc lại xác nhận cả 7 dòng.** 4 ô chỉ đọc (`Trạng thái`, `Kết quả thực tế`,
`TKM phản hồi lần 1`, `DEV phản hồi lần 1`) **nguyên vẹn** ở cả 7 dòng — cột `Trạng thái` vẫn `Fail`.
Không mở dòng bug mới `_QA<n>` nào (xem §4).

---

## 2. Một lỗi phải mở lại — dòng 340

Đây là mục **duy nhất** chặn bàn giao.

Trên màn Chi tiết đợt, bảng biểu mẫu 21a hiện đủ giá trị ở **13/13** chỉ tiêu: chỉ tiêu **1–11** hiện sẵn
số `0` kèm dấu `(HT)` và **không có ô để cán bộ nhập/sửa**; chỉ tiêu 12–13 có ô nhập. Bấm
[Trình duyệt KQ] → hệ thống chặn, liệt kê đúng **11 chỉ tiêu không có ô nhập** là "còn thiếu".

Đặc tả `:802` (BA chốt 06/08/2026) nói thẳng: *"Ô để trống là chưa điền; giá trị **0 là đã điền** (đơn vị
không phát sinh hoạt động trong kỳ **vẫn phải nộp**)"*. Cán bộ **không có đường nào** hoàn tất thao tác:
không sửa được 11 chỉ tiêu, mà giá trị hệ thống tự đưa ra thì chính hệ thống từ chối.
Tái hiện trên **2 đợt độc lập** (`MAU_21A` và `CA_HAI`).

**Kết quả kéo theo:** điều kiện nghiệm thu `:829` không thể đạt bằng thao tác trên màn ⇒ luồng
lập BC → trình duyệt → phê duyệt → gửi TW **đứt ở bước trình duyệt** với mọi đơn vị.
*(Phiếu 342 đo được là nhờ QA ép qua tiền đề bằng đường dữ liệu — đã khai rõ trong báo cáo phiếu đó.)*

---

## 3. Câu hỏi gửi BA — gom 3 nhóm, trả lời 1 lần

### Nhóm 1 — thời điểm hiển thị phần lập báo cáo *(dòng 338 + 339, cùng 1 câu hỏi)*

Khi đơn vị **chưa vào pha lập báo cáo**, màn Chi tiết đợt có phải hiển thị khối *Nhận xét, kiến nghị* và
khối *Chương trình HTPL liên quan* ở **dạng chỉ đọc** không, hay đúng là chỉ hiện sau khi bấm [Lập báo cáo]?
Đặc tả `:1169` chỉ đặt điều kiện *"khi đợt ở DANG_LAP_BC"* và **im lặng** về các trạng thái còn lại; bảng
thành phần màn hình (`:1163`–`:1175`) **không có dòng nào** khai khối truy vết chương trình liên quan.

### Nhóm 2 — mô hình trạng thái ĐỢT vs ĐƠN VỊ *(dòng 342, ảnh hưởng cả 335/338/339/340)*

Trạng thái người dùng nhìn thấy ở Chi tiết đợt là trạng thái **của đơn vị mình** hay **của đợt**?
Phép đo đã lộ hành vi nhập nhằng: cùng đợt `DOT-SO_BO_NAM-2026-1` sau khi gửi TW thành công,
cán bộ **Địa phương** đọc **"Đã gửi TW"** còn cán bộ **Trung ương** đọc **"Tạo đợt"**; tab lọc "Đã gửi TW"
của Trung ương **rỗng**.
Đặc tả tự mâu thuẫn: `:937` bắt chuyển trạng thái **ĐỢT**, `:938` lại quy định chính ba việc đó ở cấp
**ĐƠN VỊ**, `:1512` bắt đợt sang `DANG_LAP_BC` khi bắt đầu lập nhưng phần xử lý FR-XI-06 (`:739`–`:747`)
không có bước nào đụng trạng thái đợt — trong khi `:1368` chỉ cho mỗi đợt **một** giá trị mà phạm vi đợt
là **83 đơn vị** (`:621`/`:646`/`:1398`).

### Nhóm 3 — câu chữ thông báo *(dòng 335 + 342)*

FR-XI-07 và FR-XI-08 **không có mã `INF-XI-07-*` / `INF-XI-08-*`**, trong khi SRS **có** khai câu chữ ở chỗ
khác (`:1032` `INF-XI-09-01`). Câu chữ thông báo thành công có bị ràng buộc đúng chuỗi trong phiếu UAT không,
hay chỉ cần một thông báo thành công bất kỳ? *(Thực tế đo được ở dòng 342 trùng khít chuỗi đối tác kỳ vọng.)*

---

## 4. Ghi nhận gửi DEV — không phải vế phiếu, không mở dòng bug mới

| # | Nội dung | Nguồn |
|---|---|---|
| 1 | Chặn sai cấp trả chuỗi tiếng Anh thô **"Forbidden"** + mã quyền chung `ERR-PERM-SYS-00-01`, không phải thông điệp tiếng Việt đã đặc tả (`:962` `ERR-XI-08-01` · `:963` `ERR-XI-08-02`). **Việc chặn là đúng spec**, chỉ thông điệp chưa đúng | dòng 342 |
| 2 | Mã lỗi khi chặn trình duyệt là `ERR-VAL-XI-07-02`, đặc tả `:825` khai `ERR-XI-07-01` (câu chữ thì khớp) | dòng 340 |
| 3 | 3 chỉ tiêu đã lưu (số vụ việc, số DN được hỗ trợ, tổng chi phí) không hiển thị ở bảng 13 chỉ tiêu | dòng 340 |
| 4 | Thông báo gửi cán bộ TW chỉ nêu mã đợt, không nêu tên đơn vị đã nộp (đợt có 83 đơn vị) | dòng 342 |
| 5 | Một lần gửi TW sinh **2** mục nhật ký cùng mốc giờ | dòng 342 |
| 6 | Danh sách chương trình trong khối truy vết không lọc theo trạng thái CT (bản Dự thảo vẫn hiện) và không lọc theo kỳ báo cáo | dòng 339 |
| 7 | Bảng 21b trên màn đang dựng giống hệt 21a (13 dòng chỉ tiêu), trong khi Phụ lục D mô tả 21b là bảng tổng hợp cấp tỉnh mỗi dòng một Sở/ban ngành | dòng 337 |

**Vì sao không mở dòng `_QA<n>`:** cả 7 mục đều là *thông điệp / nội dung / cấu trúc* mà đặc tả hoặc im
lặng hoặc tự mâu thuẫn, hoặc là hệ quả của cùng một câu hỏi BA ở §3. Mở thành phiếu bug lúc này sẽ chốt sẵn
một phía khi chưa biết phía nào đúng. Đề nghị BA trả lời §3 trước, mục nào còn lệch thì mở phiếu sau.

---

## 5. Kiểm chứng thêm — đối chiếu với bằng chứng gốc của đối tác

Ảnh đối tác `TPDBCKQTHCT_01-partner-sau-reload-van-Tao-dot.jpg` (env `ospgroup.vn`, **V1.0.3**, 03/08/2026)
xác nhận **hai điều**, độc lập với phép đo của QA:

1. Bảng 21a trên bản đối tác chỉ có **2 cột** (`Chỉ tiêu | Kỳ này`) — cột "Số liệu kỳ trước" và "Ghi chú"
   thực sự **từng thiếu** ⇒ chấm **Pass** cho dòng 336/337 là có căn cứ, không phải đối tác đo sai.
2. Sau khi trình duyệt, thanh tiến trình của đối tác vẫn ở **bước 1 "Tạo đợt"**; trên bản nội bộ hiện tại
   nó nhảy sang **bước 3 "Chờ duyệt KQ"** ⇒ triệu chứng cũ của dòng 340 **đã hết** thật, và phần Reopen của
   dòng 340 là **điểm hỏng mới ở chỗ khác**, không phải lỗi cũ chưa fix.

**Bằng chứng đối tác có vấn đề — đã khai trong báo cáo:** `LBCKQTHCT_05.jpg` và `LBCKQTHCT_06.jpg` là
**cùng một file ảnh** (trùng mã băm `c0fb9837447ee90ac8c8f975a298aaef`) dùng cho hai khiếu nại về hai khối
khác nhau, và ảnh chỉ bắt phần dưới trang. `LBCKQTHCT_04.jpg` bị cắt mất tiêu đề thẻ nên không xác định được
ảnh chụp 21a hay 21b. Vì vậy QA **không** dựa vào ảnh, mà tự tái hiện đúng các bước phiếu mô tả.

---

## 6. Dữ liệu QA đã dựng / đã đổi — cần biết để dọn

| Bản ghi | QA đã làm gì | Trạng thái để lại |
|---|---|---|
| Đợt `DOT-TRON_NAM-2026-1` (`a63a3214…`) | `cbnv_tw` tạo mới, biểu mẫu **`CA_HAI`**, phạm vi 2 đơn vị — để đo được 21b (dòng 337) | đơn vị `DANG_LAP` |
| Đợt `DOT-SO_BO_NAM-2026-1` (`e9909d96…`) | lập BC → ép tiền đề trình duyệt (đường dữ liệu) → `cbpd_hn` duyệt KQ → `cbnv_hn` **gửi TW qua giao diện** | đơn vị **Đã nộp**, có mặt trong danh sách tổng hợp TW |
| Chương trình `CT-20260807-0001` | `cbnv_hn` tạo — để khối truy vết có dữ liệu mà chọn (dòng 339) | còn |
| Chuỗi mốc-giờ | `QA-BCCT-20260807-0209-*`, `QA-F5-NHANXET-20260807-*`, `QA-F5-20260807-tien-de-case7-duyet-KQ` | dữ liệu thử |

Toàn bộ là dữ liệu QA dựng để kiểm thử, **xóa hoặc đưa về trạng thái cũ được** sau khi đối tác đọc xong.

---

## 7. Cấu trúc hồ sơ lô

```
F5-devfix-BCCT-2026-08-07/
├── BAN-GIAO.md              ← file này
├── chuan/                   ← chuẩn chấm khóa TRƯỚC khi mở màn (Giai đoạn A), 7 phiếu + 2 file chung
├── do/                      ← báo cáo phép đo đầy đủ, 7 phiếu
├── note/                    ← đúng nội dung đã ghi vào ô "Kết quả verify" của từng dòng
├── image/                   ← ảnh QA chụp + ảnh trích từ bằng chứng đối tác (tiền tố `-partner-`)
├── partner-evidence/        ← bằng chứng gốc đối tác + DOC-BANG-CHUNG.md
└── audit/                   ← giá trị các ô TRƯỚC khi ghi (đối chứng khi cần truy)
```
