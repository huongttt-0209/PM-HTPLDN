# Chuẩn chấm đã khóa — LKHDG_16 (dòng 127)

| Mục | Giá trị |
|---|---|
| **Bảng / tab / dòng** | `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `bug` (gid 1714340219) · **dòng 127** |
| **Mã TC** | `LKHDG_16` — Sửa kế hoạch đánh giá |
| **Tên rút gọn** | Không vào được chế độ sửa khi đợt ở trạng thái "Phân công" |
| **Bug entry** | `BUG-LKHDG-SUA-PHANCONG` — Major · P2 · **Open** |
| **Env đo** | https://18.143.165.120.nip.io (env dev nội bộ, **không** phải env nghiệm thu đối tác) |
| **Tài khoản** | **`cbnv_tw` / `Test@1234`** (CB Nghiệp vụ Trung ương, `BTP · TW`). OTP: MailHog http://18.143.165.120:8025 |
| **Màn** | Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách · `/danh-gia/ke-hoach/danh-sach` |
| **SRS nguồn chuẩn** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md` (1280 dòng) |
| **Ánh xạ ghi bảng** | tab `bug` chỉ có MỘT cột trạng thái ⇒ Pass ghi `Test done` vào `Trạng thái dev fix`; note ghi cột `Kết quả verify` |

**Nguồn đã đọc để dựng chuẩn này (đọc file trên đĩa, không mở web):**

- `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/bug-report-LKHDG.md` — entry `BUG-LKHDG-SUA-PHANCONG` (`:123-200`) + khối `CÁCH VERIFY` (`:234-263`)
- `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/audit/LKHDG_16-ketqua-verify-CU.md` — nội dung ô `Kết quả verify` CŨ
- `output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/tieuchi/LKHDG_16.md` — tiêu chí gốc + bằng chứng đối tác
- `output/UAT_doi-tac/reverify-week-5/ba-confirm/ba-confirmation-needed-LKHDG-2026-08-06.md` — phiếu hỏi BA vòng trước
- `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md` — **tự mở đếm lại từng dòng**

---

## 1. Lỗi gốc (Expected/Actual của phiếu) — ghi rõ vế nào đã hết lỗi vòng trước

**Kỳ vọng đối tác (cột "Kết quả mong đợi" của phiếu 127):**

> *"Chỉ hiển thị khi đợt đang ở trạng thái 'Lập kế hoạch' **hoặc 'Phân công'**, và Cán bộ nghiệp vụ thuộc đơn vị
> sở hữu đợt. Hệ thống mở màn hình chi tiết đợt đánh giá ở chế độ chỉnh sửa."*

**3 vế đối tác nêu (2 vòng) và hiện trạng chốt vòng trước (06/08, bản dựng V1.0.8 env dev):**

| Vế | Vòng | Đối tác ghi | Hiện trạng 06/08 | Còn phải đo lại? |
|---|---|---|---|---|
| **a** | 1 | "Các trường thông tin **không được chỉnh sửa**" | **ĐÃ HẾT LỖI** ở trạng thái *Lập kế hoạch* — [Sửa] mở khung nhập 9 mục, tất cả nhập/đổi được, nạp sẵn giá trị cũ; đổi rồi lưu thì mở lại thấy giá trị mới (bản ghi lên `version` 3, dấu `QA-LKHDG16-EDIT-20260806-0830`) | Đo lại **chống hồi quy** |
| **b** | 1 | "Breadcrumb hiển thị … / **Chi tiết**" | **ĐÃ HẾT LỖI** — [Sửa] không rời màn Danh sách, đường dẫn giữ *".../ Danh sách"*, khung nhập ghi rõ *"Sửa kế hoạch đánh giá"* | Đo lại **chống hồi quy** |
| **c** | 2 | "**Không hiển thị danh sách các tệp đính kèm** mặc dù tồn tại dữ liệu" | **ĐÃ HẾT LỖI** — khung Sửa liệt kê đủ tệp kèm kích thước + [Xem] [Xóa]; lưu form không đụng vùng đính kèm **không** làm mất tệp | Đo lại — và nay **đã có chỗ dựa đặc tả** (xem §3) |

**Vế CÒN LỖI, là lý do case đang Open:**

> Ở trạng thái **Phân công**, hệ thống **không mở được chế độ sửa**: hàng trong danh sách chỉ còn thao tác xem;
> màn chi tiết không có ô nhập nào cho khối "Thông tin kế hoạch" (nút duy nhất là **[Hủy đợt]**, **0** ô nhập);
> gửi yêu cầu cập nhật thẳng tới máy chủ trả **HTTP 409** · `ERR-BIZ-XI-01-02` ·
> *"Không thể cập nhật kế hoạch ở trạng thái 'PHAN_CONG'"*.
> Giao diện và máy chủ **thống nhất** với nhau ⇒ đây là **luật đang cài đặt**, không phải nút bị ẩn nhầm.

Hệ quả nghiệp vụ: luồng trạng thái **không có** đường lùi *Phân công → Lập kế hoạch*, nên một sai sót trong
thông tin kế hoạch sau khi đã phân công là **không sửa được nữa** — chỉ còn cách hủy cả đợt và lập lại.

---

## 2. Dẫn đặc tả (đã tự mở đếm lại)

> **Đã mở `srs-fr-08-danh-gia.md` đếm lại từng dòng ngày 07/08.** Toàn bộ dẫn cũ trong hồ sơ 06/08 **đều lệch**.
> Nguyên nhân: BA chèn thêm dòng ngày **2026-08-06** ở **hai** chỗ — `:113` + `:114` (bảng Inputs của FR-VI-01,
> nằm TRÊN mọi dẫn cũ ⇒ đẩy +2) và `:852` + `:854` (bảng thành phần form của SCR-VI-01) — cộng thêm phần chèn ở
> vùng entity `KE_HOACH_DANH_GIA`. Vì vậy **độ lệch KHÔNG đồng nhất +2**: vùng ≤ 851 lệch **+2**, vùng bảng form
> lệch **+2…+4**, vùng State Machine lệch **+5**. **Cấm bê số cũ.**

| Trích dẫn cũ | Trích dẫn ĐÚNG hiện tại | Nguyên văn dòng (≤200 ký tự) |
|---|---|---|
| `:837` (nút Sửa theo trạng thái) | **`:839`** | `\| 18 \| table \| Hành động \| icon-group \| Xem / Sửa (chỉ LAP_KE_HOACH/PHAN_CONG) / Xóa (chỉ LAP_KE_HOACH) \| click → tương ứng \| Luôn \|` |
| `:159` (AC chỉnh sửa KH) | **`:161`** | `- **Given** CB NV chỉnh sửa KH chưa duyệt **When** thay đổi **Then** validate + lưu` |
| `:1185-1194` (bảng chuyển trạng thái) | **`:1190-1199`** (10 dòng dữ liệu; tiêu đề bảng ở `:1188`, nhãn `**Bảng chuyển trạng thái:**` ở `:1186`) | `\| Từ \| Đến \| Trigger \| Guard \| Action \| FR Ref \| BR Ref \|` (`:1188`) |
| `:1188` (duyệt PC → Thực hiện) | **`:1193`** | `\| CHO_DUYET_PC \| THUC_HIEN \| CB PD duyệt phân công \| Cùng đơn vị; bộ tiêu chí vẫn thỏa tổng trọng số = 100% và chuẩn thang điểm = 100 \| Audit; mở bước chọn vụ việc…` |
| `:1194` (đường duy nhất rời PHAN_CONG là hủy) | **`:1199`** | `\| LAP_KE_HOACH/PHAN_CONG/THUC_HIEN/BAO_CAO \| HUY \| CB NV/PD hủy đợt \| Có lý do, chưa HOAN_THANH \| Audit, soft-delete \| — \| — \|` |
| `:843-851` ("danh sách đóng **7** dòng" của form tạo/sửa) | **`:845-855`** — tiêu đề `:845`, kẻ `:846`, **9 dòng dữ liệu `:847-855`** | Nay gồm `#21 #22 #23 #24 #25` **`#25a`** `#26` **`#26a`** `#27` — xem §3 |
| `:1043` (`file_dinh_kem` trên thực thể) | **`:1048`** | `\| 15 \| file_dinh_kem \| file[] \| N \| PDF/DOC/DOCX/XLS/XLSX. Tối đa 10 file/upload, tổng max 100MB, mỗi file max 20MB [BA chốt 2026-08-06] \| … \| Ô nhập: SCR-VI-01 thành phần #26a \|` |
| `:820` (breadcrumb — dòng breadcrumb DUY NHẤT của cả nhóm VI) | **`:822`** | `\| 1 \| toolbar \| Breadcrumb \| C01 \| "Trang chủ > Đánh giá > Theo dõi đánh giá hiệu quả HTPL" \| navigate \| Luôn \|` |
| — (mới) | **`:852`** | `\| 25a \| form \| Cơ quan được đánh giá \| C10 dropdown searchable \| **Bắt buộc.** Danh sách chọn từ danh mục Đơn vị, chọn 1 đơn vị (1:1)… [CR-10][BA chốt 2026-08-06] \| change → validate \| Khi mở form \|` |
| — (mới) | **`:854`** | `\| 26a \| form \| Tài liệu đính kèm \| C15 File Upload \| Không bắt buộc… **Hiện danh sách tệp đã có kèm thao tác [Xem] [Xóa]** [CR-07][BA chốt 2026-08-06] \| upload → validate \| Khi mở form \|` |
| — (tham chiếu độ phủ) | **`:1177-1184`** | Bảng 8 trạng thái của `SM-DANHGIA` (xem §8) |

**Kiểm chứng phản chứng — đã grep toàn file, KHÔNG có dòng nào giới hạn việc sửa vào riêng `LAP_KE_HOACH`:**

- `grep -n "chỉ sửa\|chỉ được sửa\|không được sửa\|khóa chỉnh sửa\|cho phép sửa"` → chỉ ra 4 dòng và **không dòng nào**
  nói về form kế hoạch (`:868` `:869` `:870` là điều kiện *"Khi TT cho phép sửa"* của **Tab 1 Tiêu chí**, không phải
  form kế hoạch; `:771 :773 :791 :793 :802 :863 :876 :898` là read-only của FR-VI-10 / info-card / bảng tổng hợp).
- Toàn file chỉ có **2** dòng nói về việc sửa kế hoạch đánh giá: **`:839`** và **`:161`** — **cả hai đều cho phép sửa ở
  `PHAN_CONG`**. `:839` còn phân biệt rõ: *Xóa* mới bị bó vào `LAP_KE_HOACH`, còn *Sửa* mở cho cả hai.
- `grep -rn "ERR-BIZ-XI"` toàn thư mục `srs-v3.5/` → **0 kết quả**. Mã lỗi máy chủ đang trả **không tồn tại** trong đặc tả.

---

## 3. 🔴 Kết luận về điểm chờ BA (2 mục BA chèn 06/08) — **ĐÃ GIẢI QUYẾT**

**Điểm QA tách sang phiếu hỏi BA ở vòng trước** (`ba-confirmation-needed-LKHDG-2026-08-06.md`, và gạch đầu dòng cuối
của ô `Kết quả verify` cũ):

> *"form Sửa đang hiển thị 'Tài liệu đính kèm' và 'Cơ quan được đánh giá', trong khi bảng thành phần form ở
> `:843-851` là danh sách đóng 7 dòng không có 2 mục đó."*
> Phiếu hỏi BA đặt 2 hướng: **Hướng 1** = danh sách MỞ, đề nghị BA bổ sung 2 dòng vào bảng · **Hướng 2** = danh sách
> ĐÓNG, hiện trạng là thừa so với đặc tả.

**Đã tự mở file đếm lại — bảng thành phần form tạo/sửa nay ở `:845-855`, có 9 dòng dữ liệu:**

| Dòng | # | Thành phần |
|---:|---|---|
| 847 | 21 | Tên đợt |
| 848 | 22 | Mục tiêu |
| 849 | 23 | Tần suất |
| 850 | 24 | Từ ngày / Đến ngày |
| 851 | 25 | Đối tượng |
| **852** | **25a** | **Cơ quan được đánh giá** — *"**Bắt buộc.** … `[CR-10][BA chốt 2026-08-06]`"* |
| 853 | 26 | Ghi chú |
| **854** | **26a** | **Tài liệu đính kèm** — *"… **Hiện danh sách tệp đã có kèm thao tác [Xem] [Xóa]** `[CR-07][BA chốt 2026-08-06]`"* |
| 855 | 27 | Thanh hành động |

### ⇒ KẾT LUẬN DỨT KHOÁT

1. **Đặc tả NAY ĐÃ CÓ đúng 2 mục đó**, ngay trong **bảng thành phần màn hình SCR-VI-01** (không phải ghi chú phạm vi,
   không phải CHANGELOG) — kèm dấu thay đổi `[BA chốt 2026-08-06]` ngay trên dòng. Đây chính là **Hướng 1** mà phiếu
   hỏi BA đề xuất. BA đã chèn đối xứng ở cả 3 chỗ: `:113` `:114` (Inputs FR-VI-01), `:852` `:854` (thành phần form),
   `:1048` `:1049` (entity `KE_HOACH_DANH_GIA`, có trỏ ngược *"Ô nhập: SCR-VI-01 thành phần `#25a` / `#26a`"*).
2. **Điểm chờ BA của LKHDG_16 ĐÃ ĐƯỢC GIẢI QUYẾT. Case này KHÔNG CÒN vế chờ BA.**
   ⇒ Verdict tới **chỉ có thể là `Pass` / `Reopen` / ô trống**. **KHÔNG được ghi `reopenba`.**
3. **Hệ quả bắt buộc lên chuẩn chấm** (đúng như QA đã cam kết ở phiếu hỏi BA mục "Nếu BA chọn Hướng 1"):
   **vế (c) chuyển từ "KHÔNG CHẤM — cần BA" sang "CHẤM ĐƯỢC"**. Từ nay `:854` là căn cứ nghiệp vụ: khi mở form
   Sửa, hệ thống **phải** hiện danh sách tệp đã có kèm thao tác [Xem] [Xóa]; và `:852` yêu cầu form **phải** có
   mục "Cơ quan được đánh giá" (**bắt buộc**).
   - Nếu bản dựng mới **vẫn hiện** đủ 2 mục → vế (c) PASS, nay đã có chỗ dựa đặc tả.
   - Nếu bản dựng mới **gỡ mất** 1 trong 2 mục → đó là **hồi quy mới, có căn cứ đặc tả rõ** ⇒ log bug mới, **không**
     đẩy sang BA nữa.
4. ⚠️ **Bảng "Lịch sử thay đổi" đầu file (`:12-19`) KHÔNG ghi mục 2026-08-06.** Đừng lấy việc bảng lịch sử im lặng
   làm lý do kết luận "BA chưa chốt" — dấu `[BA chốt 2026-08-06]` nằm trực tiếp trên dòng đặc tả màn hình mới là
   căn cứ, và nó mạnh hơn bảng lịch sử.

---

## 4. Precondition + dữ liệu + công thức dựng đợt "Phân công"

**Precondition (chép nguyên từ khối `CÁCH VERIFY`):**

```
Precondition: tài khoản `cbnv_tw` (CB Nghiệp vụ Trung ương, Test@1234) + màn
  https://18.143.165.120.nip.io/danh-gia/ke-hoach/danh-sach.
  Cần MỘT đợt ở trạng thái "Phân công" thuộc đơn vị của tài khoản và có >=1 tệp đính kèm.
  Chưa có thì tự dựng (đây là tiền đề TẠO ĐƯỢC, không phải blocker):
    a) mở đợt "Lập kế hoạch" -> tab Tiêu chí -> [Nhập từ danh mục] -> chọn nhóm "Hiệu quả HTPL"
       (4 tiêu chí, tổng trọng số 100%) -> sửa cột "Điểm tối đa" = 100 cho từng dòng -> [Lưu];
    b) tab Phân công -> [Thêm người đánh giá] -> chọn 1 người + vai trò -> [Thêm mới].
  Nếu bỏ bước (a) thì bước (b) bị chặn bởi guard "tổng điểm tối đa có trọng số phải = 100".
```

**🔴 Đọc lại cho rõ: đợt ở trạng thái "Phân công" là tiền đề TẠO ĐƯỢC, KHÔNG phải blocker.**
Không được mark "🚫 không đo được vì thiếu dữ liệu" — phải tự dựng theo công thức a) → b) ở trên.

**Giải thích guard (để không dựng sai):** bước (b) bị chặn bởi **BR-CALC-08** — *"tổng của (điểm tối đa × trọng số ÷
100) phải = 100"*. Đặc tả: `:867` (cảnh báo `WRN-DG-TC-02`), `:878` (nút [+ Thêm người đánh giá] **disabled** nếu
tổng trọng số ≠ 100% → `ERR-DG-PC-05`, **hoặc** chuẩn thang điểm ≠ 100 → `ERR-DG-PC-06`), `:879` (điều kiện trình
phê duyệt). Với nhóm "Hiệu quả HTPL" 4 tiêu chí tổng trọng số 100%, đặt Điểm tối đa = 100 cho **từng** dòng thì
tổng có trọng số = 100 ✔. `:864` ghi rõ ràng buộc này **không chặn lưu** ở Tab Tiêu chí — chỉ chặn ở Tab Phân công,
nên đừng tưởng lưu được tiêu chí là đã qua guard.

**Chuyển trạng thái sang PHAN_CONG:** theo `:1191` — `LAP_KE_HOACH → PHAN_CONG`, trigger *"CB NV phân công"*,
guard *"Có KH"*. Tức việc thêm 1 người đánh giá ở bước (b) chính là hành vi đẩy đợt sang **Phân công**.

**Dữ liệu tối thiểu cần có mặt (M = 3 dạng, theo tiêu chí gốc mục 5):**

| Dạng | Trạng thái | Tệp đính kèm | Ghi chú |
|---|---|---|---|
| 1 | Lập kế hoạch | đúng **1** tệp | vòng 06/08 dùng `DG-20260806-0001` |
| 2 | Lập kế hoạch | **≥2** tệp **khác định dạng** (vd `.docx` + `.pdf`) | vòng 06/08 dùng `DG-20260730-0002` |
| 3 | **Phân công** | **≥1** tệp | vòng 06/08 dùng `DG-20260806-0001` sau khi đẩy tiếp — **đây là dạng quyết định verdict** |

Tệp seed sẵn có trên đĩa nếu cần đính kèm lại:
`output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/seed-files/QA-LKHDG16-ke-hoach.pdf` (+ `QA-LKHDG16-baocao-mau.docx`).

---

## 5. Các bước đo (đánh số, thao tác UI thật)

> Bước **1-4** là 4 bước đã khóa trong khối `CÁCH VERIFY`. Bước **0**, **5**, **6** là bắt buộc bổ sung của lô F3.

**0) Ghi bản dựng TRƯỚC khi đo.** Đăng nhập `cbnv_tw` / `Test@1234` (OTP MailHog). Đọc số hiệu bản dựng ở **chân
sidebar** và tên gói mã JS đang tải. Ghi lại nguyên văn. So với bản đã đo 06/08 — xem cảnh báo §11.

**1) Ở màn Danh sách, tìm đợt đang "Lập kế hoạch": ghi lại cột Hành động có mấy thao tác.**
Vào **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**. Có thể lọc **Trạng thái = "Lập kế hoạch"** để tìm nhanh.
Đếm số biểu tượng ở cột **Hành động** của hàng đó (mong đợi theo `:839`: Xem · Sửa · Xóa).

**2) Tìm đợt đang "Phân công": ghi lại cột Hành động có mấy thao tác. So với bước 1.**
Lọc **Trạng thái = "Phân công"**. Đếm biểu tượng cột Hành động của hàng đợt Phân công.
Mong đợi theo `:839`: **có Xem và có Sửa**, **không** có Xóa. Chụp ảnh **cùng một bảng** có cả hàng *Lập kế hoạch*
và hàng *Phân công* để so trực tiếp (giống bố cục ảnh lỗi cũ).
⚠️ Thao tác Sửa/Xóa trên bảng của app này là thẻ `<a>`, **không** phải `<button>` — đếm bằng ảnh + DOM, đừng chỉ
đếm `button`.

**3) Mở [Sửa] của đợt "Phân công" (nếu có): đổi 1 trường bất kỳ rồi lưu, sau đó MỞ LẠI đối chiếu.**
Bấm [Sửa] trên hàng đợt Phân công → khung nhập mở ra. Đổi **Ghi chú** thành một dấu duy nhất, dễ tra, ví dụ
`QA-LKHDG16-PC-<YYYYMMDD-HHMM>`. Bấm nút xác nhận lưu. **Đóng khung, mở lại [Sửa] chính đợt đó** và đọc lại giá trị.
Không được chốt bằng toast.

**4) Đối chứng bằng đường thứ hai: gửi `PATCH /api/v1/ke-hoach-danh-gias/{id}` đổi trường Ghi chú, ghi lại mã HTTP + `error.code`.**
Xem §6.

**5) (bổ sung sau khi BA chốt 06/08 — nay là yêu cầu có căn cứ đặc tả) Kiểm thành phần form Sửa.**
Trên khung Sửa (đo trên **cả** đợt *Lập kế hoạch* và, nếu vào được, đợt *Phân công*), xác nhận có mặt:
**"Cơ quan được đánh giá"** (`:852`, **bắt buộc**) và **"Tài liệu đính kèm"** (`:854`) — mục đính kèm phải **liệt kê
tệp đã có** kèm thao tác **[Xem] [Xóa]**, không phải chỉ có vùng kéo-thả rỗng. Đây chính là triệu chứng vế (c) đối tác
nêu ở vòng 2. Thiếu → hồi quy mới, log bug riêng (không kéo sang BA nữa).

**6) (chống hồi quy vế a + b + c ở trạng thái Lập kế hoạch)** Lặp bước 3 trên đợt *Lập kế hoạch* dạng 1 và dạng 2:
xác nhận các trường nhập/đổi được và nạp sẵn giá trị cũ; xác nhận [Sửa] **không** rời màn Danh sách (đường dẫn giữ
ngữ cảnh danh sách/sửa, tiêu đề khung nhập ghi rõ đang **Sửa**); xác nhận lưu form mà **không đụng** vùng đính kèm
thì **không** làm mất tệp đã có (mở lại đếm lại số tệp).

---

## 6. Đường đo thứ hai (đối chứng độc lập)

**Đường 2 — gọi thẳng máy chủ, cùng phiên đăng nhập `cbnv_tw`** (JWT `access_token` là cookie ⇒ `fetch` trong trang
tự xác thực, `credentials:'include'`):

1. Lấy `id` (UUID) của đợt **Phân công** từ `GET /api/v1/ke-hoach-danh-gias?trangThai=PHAN_CONG&page=1&pageSize=20`.
2. Đọc bản ghi hiện tại `GET /api/v1/ke-hoach-danh-gias/{id}` → ghi lại `ghiChu` và `version`.
3. `PATCH /api/v1/ke-hoach-danh-gias/{id}` với **một thay đổi hợp lệ ở trường Ghi chú** (kèm `version` hiện tại nếu
   máy chủ đòi optimistic lock). **Ghi lại mã HTTP + `error.code` + `message` nguyên văn.**
4. `GET` lại bản ghi → đối chiếu `ghiChu` mới và `version` có tăng không.

**Số đo đối chứng của vòng 06/08 (để so):**

| Nơi kiểm tra | Đợt *Lập kế hoạch* | Đợt *Phân công* |
|---|---|---|
| Cột Hành động trên danh sách | Xem · **Sửa** · Xóa | **chỉ Xem** |
| Màn Xem chi tiết | (sửa vốn mở từ danh sách) | 0 ô nhập cho "Thông tin kế hoạch"; nút duy nhất **[Hủy đợt]** |
| `PATCH /api/v1/ke-hoach-danh-gias/{id}` | lưu được | **409** · `ERR-BIZ-XI-01-02` · *"Không thể cập nhật kế hoạch ở trạng thái 'PHAN_CONG'"* |

**Quy tắc đọc kết quả 2 đường:**

- UI **và** API cùng chặn ⇒ **luật đang cài đặt** (đúng như 06/08) — chốt Reopen được, không cần đoán.
- UI hiện [Sửa] **nhưng** API vẫn 409 ⇒ **FAIL** (fix nửa vời ở lớp FE). Phải nêu cả 2 số đo trong bug entry.
- API cho lưu **nhưng** UI vẫn giấu [Sửa] ⇒ **FAIL** (fix nửa vời ở lớp BE). Phải nêu cả 2 số đo.
- Chỉ khi **cả hai** đều thông mới xét PASS.

---

## 7. ✅ PASS khi / ❌ FAIL nếu — **chép NGUYÊN VĂN từ khối `CÁCH VERIFY`**

```
✅ PASS khi: đợt "Phân công" vào được chế độ sửa, đổi rồi lưu thì mở lại thấy giá trị mới,
   VÀ yêu cầu cập nhật ở bước 4 không bị từ chối vì lý do trạng thái.
❌ FAIL nếu: đợt "Phân công" không có lối vào sửa, hoặc lưu xong mở lại vẫn giá trị cũ,
   hoặc bước 4 trả 409 kèm thông điệp từ chối theo trạng thái.
```

**Ánh xạ verdict (tab `bug` chỉ có MỘT cột trạng thái):**

| Kết quả đo | Verdict | Ghi cột `Trạng thái dev fix` |
|---|---|---|
| PASS theo khối trên **và** không hồi quy vế a/b/c | **Pass** | `Test done` |
| FAIL theo khối trên, hoặc hồi quy bất kỳ vế a/b/c | **Reopen** | `Reopen` |
| Không đo được vì lý do ngoài case (env sập, tài khoản khóa hết siblings) | ô trống + báo điều phối | — |

**KHÔNG có nhánh `reopenba` cho case này** — xem §3.

---

## 8. Độ phủ biến thể bắt buộc

**Toàn bộ trạng thái đợt đánh giá theo `SM-DANHGIA`, đặc tả `:1177-1184` (8 trạng thái):**

| Dòng | Trạng thái | Mã | Có phải đo? |
|---:|---|---|---|
| 1177 | Lập kế hoạch | `LAP_KE_HOACH` | **BẮT BUỘC** — `:839` cho phép Sửa |
| 1178 | Phân công | `PHAN_CONG` | **BẮT BUỘC** — `:839` cho phép Sửa; **đây là trạng thái quyết định verdict** |
| 1179 | Chờ duyệt phân công | `CHO_DUYET_PC` | Không — `:839` không cho Sửa |
| 1180 | Thực hiện | `THUC_HIEN` | Không |
| 1181 | Báo cáo | `BAO_CAO` | Không |
| 1182 | Chờ phê duyệt | `CHO_PHE_DUYET` | Không |
| 1183 | Hoàn thành | `HOAN_THANH` | Không |
| 1184 | Hủy | `HUY` | Không |

**Tối thiểu phải đo trên: `LAP_KE_HOACH` VÀ `PHAN_CONG` — cả hai, không được bỏ một.**
Căn cứ: `:839` liệt kê đúng 2 trạng thái này cho thao tác Sửa; kỳ vọng đối tác cũng ghi *"'Lập kế hoạch' **hoặc**
'Phân công'"*. Đo mỗi *Lập kế hoạch* rồi kết luận "đã fix" là **sai phép đo** — đó chính là cách vòng trước suýt bỏ sót.

**M = 3 dạng dữ liệu (xem bảng ở §4):** (1) LKH · 1 tệp · (2) LKH · ≥2 tệp khác định dạng · (3) **PHAN_CONG · ≥1 tệp**.
Vòng 06/08 đạt M = 2/3 — dạng 3 không đo được **chính vì lỗi này**, và đó là **kết quả FAIL của dạng 3**, không phải
lỗ hổng của phép đo. Lô này phải cố đạt **M = 3/3**.

**Không cần phủ:** biến thể vai trò (chỉ CB NV, `:95` + `:100-101`), biến thể đơn vị (phạm vi theo đơn vị `:101`) —
trừ khi phát sinh nghi ngờ. **KHÔNG dùng `admin` để ra verdict.**

---

## 9. ⚠️ Bẫy / rule chống kết luận oan

**Chép nguyên văn 3 cảnh báo từ khối `CÁCH VERIFY`:**

```
⚠️ Đừng chấm Fail vì CHUỖI breadcrumb khác một mẫu cụ thể — đặc tả im lặng về breadcrumb màn Sửa;
   chỉ chấm "có rời khỏi ngữ cảnh Sửa hay không".
⚠️ Đừng kết luận "đã fix" khi chỉ thấy nút [Sửa] xuất hiện trở lại — phải bấm vào, đổi, lưu,
   rồi MỞ LẠI đối chiếu; và phải đo trên CẢ HAI trạng thái Lập kế hoạch và Phân công.
⚠️ Cảnh báo dụng cụ đo: bản dựng V1.0.8 dùng lớp CSS riêng (.ant-drawer-section, .ant-select-content,
   danh sách tệp KHÔNG dùng .ant-upload-list-item). Kịch bản đọc DOM theo tên lớp chuẩn sẽ báo
   "trống"/"0 tệp" ở chỗ THỰC TẾ CÓ dữ liệu -> luôn chốt bằng ảnh chụp đã mở xem + đọc lại bản ghi.
```

**Kiểm chứng bẫy breadcrumb vẫn đúng ở bản SRS hiện tại:** `grep -n "readcrumb"` toàn file → **đúng 1 dòng, `:822`**,
và dòng đó đặc tả breadcrumb của **màn danh sách**. Phần B (chi tiết 4 tab, từ `:857`) và "Quy tắc tương tác"
(từ `:906`) **không** có dòng breadcrumb nào. ⇒ Đặc tả **vẫn im lặng** về breadcrumb màn Sửa.

**Bẫy bổ sung của lô này:**

4. **Đừng bê số dòng SRS cũ.** Mọi dẫn `:837` / `:159` / `:1185-1194` / `:1188` / `:843-851` / `:1043` trong hồ sơ
   06/08 **đều sai** so với file hiện tại. Dùng bảng §2. Quote sai bản = bug invalid.
5. **Đừng đòi đúng mã lỗi.** `ERR-BIZ-XI-01-02` **không tồn tại** trong đặc tả v3.5 — đừng viết "phải trả mã X" và
   cũng đừng chấm Pass chỉ vì mã lỗi đổi. Chấm theo **hành vi**: yêu cầu cập nhật ở trạng thái *Phân công* có bị
   từ chối **vì lý do trạng thái** hay không.
6. **Đừng prescribe implementation.** Viết *"theo `:839`, đợt ở trạng thái Phân công phải có lối vào chỉnh sửa"* —
   **không** viết *"phải hiện icon bút chì"* / *"phải trả 200 ở endpoint Y"*.
7. **Đừng nhầm "không có lối vào Sửa" với "thiếu quyền".** Nếu đợt **không thuộc đơn vị** của `cbnv_tw` thì việc
   ẩn Sửa là **đúng** (`:101` phạm vi theo đơn vị). Phải dựng/chọn đợt **thuộc `BTP · TW`**.
8. **Đừng nhầm "không sửa được" với "chưa qua guard".** Guard `BR-CALC-08` chặn **thêm người đánh giá**, không chặn
   sửa kế hoạch. Nếu bước (b) bị chặn thì đó là lỗi dựng tiền đề của mình, không phải triệu chứng của case này.
9. **Bản chất bug là luật theo trạng thái (server-side gate), không phải trường đã lưu trong DB.** Vì vậy **được
   phép** đo lại trên bản ghi cũ `DG-20260806-0001` — không rơi vào bẫy "re-verify trường lưu phải test dữ liệu mới".
   Nhưng nếu bản ghi cũ đã bị đẩy sang trạng thái khác thì phải dựng đợt Phân công mới theo §4.
10. **Toast tự tắt <5s:** nếu cần bằng chứng toast, hẹn giờ bấm nút rồi mới chụp; hoặc lấy **response body** của
    request làm bằng chứng mạnh hơn ảnh.
11. **Tải lại trang trước khi verify.** Tab MCP mở lâu vẫn chạy gói JS cũ ⇒ dễ báo Reopen oan.

---

## 10. Đối chiếu khối note ↔ bug entry: **GIỐNG về nội dung đo — LỆCH ở 8 chỗ diễn đạt**

Đối chiếu `bug-report-LKHDG.md:236-263` ↔ `audit/LKHDG_16-ketqua-verify-CU.md:24-49`.

**Kết luận: KHÔNG lệch một điều kiện đo nào.** Ô sheet là bản rút gọn từ (bỏ hư từ) của khối trong bug entry.
PASS / FAIL / 3 cảnh báo / ảnh lỗi cũ **trùng khít về ngữ nghĩa**.

| # | Bug entry (bản gốc, dùng làm chuẩn) | Ô sheet (bản rút gọn) | Loại lệch |
|---:|---|---|---|
| 1 | "Chưa có thì tự dựng (**đây là** tiền đề TẠO ĐƯỢC…)" | "Chưa có thì tự dựng (tiền đề TẠO ĐƯỢC…)" | hư từ |
| 2 | "Điểm tối đa" = 100 **cho** từng dòng | "Điểm tối đa" = 100 từng dòng | hư từ |
| 3 | "**Nếu** bỏ bước (a) thì…" | "Bỏ bước (a) thì…" | hư từ |
| 4 | "1) Ở màn Danh sách, **tìm** đợt đang 'Lập kế hoạch': …" | "1) Ở màn Danh sách, đợt đang 'Lập kế hoạch': …" | hư từ |
| 5 | "2) **Tìm** đợt đang 'Phân công': …" | "2) Đợt đang 'Phân công': …" | hư từ |
| 6 | "3) … đổi 1 trường **bất kỳ** rồi lưu…" | "3) … đổi 1 trường rồi lưu…" | hư từ |
| 7 | "4) Đối chứng **bằng** đường thứ hai: **gửi** PATCH …" | "4) Đối chứng đường thứ hai: PATCH …" | hư từ |
| 8 | "✅ … VÀ yêu cầu **cập nhật** ở bước 4 không bị từ chối…" | "✅ … VÀ yêu cầu ở bước 4 không bị từ chối…" | hư từ |
| 9 | "⚠️ … nút [Sửa] xuất hiện **trở** lại …" | "⚠️ … nút [Sửa] xuất hiện lại …" | hư từ |

**Trùng khít 100% (chép y nguyên):** dòng `Precondition` + URL + điều kiện *"đợt Phân công … có >=1 tệp"* · bước
(a) và (b) + guard *"tổng điểm tối đa có trọng số phải = 100"* · toàn bộ dòng **❌ FAIL nếu** · cảnh báo breadcrumb ·
cảnh báo dụng cụ đo (3 lớp CSS) · dòng `Ảnh lỗi cũ`.

**Chỉ có ở ô sheet, KHÔNG có trong bug entry** (nằm ngoài khối `CÁCH VERIFY`, ở phần diễn giải):
gạch đầu dòng cuối *"Một điểm riêng đã tách sang phiếu hỏi BA … `:843-851` là danh sách đóng 7 dòng không có 2 mục
đó. Hiện trạng đang thoả kỳ vọng đối tác nên KHÔNG đề nghị dev gỡ."*
⇒ **Gạch đầu dòng này ĐÃ HẾT HIỆU LỰC** khi ghi lại ô `Kết quả verify` lần này — BA đã chốt (§3). Khi đè ô mới,
**phải bỏ / viết lại** gạch đầu dòng này, đừng chép nguyên bản cũ sang.

**Ảnh lỗi cũ — kiểm tra trên đĩa:** `LKHDG_16-D-hang-PhanCong-chi-con-nut-Xem-V108.png` **CÓ THẬT**, nằm tại
`output/UAT_doi-tac/reverify-bug-devfix-2026-08-06/bug-reports/image/` (thư mục `image/` **ngang cấp** với
`bug-report-LKHDG.md`, nên link tương đối `image/…` trong file bug là **đúng**). Cùng thư mục còn 3 ảnh khác của case:
`LKHDG_16-A-man-chitiet-co-2-tep-dinh-kem-V108.png` · `LKHDG_16-B-drawer-sua-6-truong-nhap-duoc-da-nap-san-V108.png` ·
`LKHDG_16-C-drawer-sua-dot-1-tep-ghichu-da-luu-V108.png`.

---

## 11. Cảnh báo cho agent đo

1. **🔴 Bản dựng: hai hồ sơ ghi hai gói mã KHÁC NHAU cho cùng lượt đo 06/08.**
   `bug-report-LKHDG.md:6` + `tieuchi/LKHDG_16.md:5` + phiếu BA ghi **`assets/index-DThrFe1_.js`**;
   `F3-devfix-2026-08-07/TIEN-DO.md:27-28` ghi **`assets/index-DIABnbIr.js`**.
   ⇒ Ở bước 0 **phải ghi lại tên gói mã thực tế** và so với **CẢ HAI**. Trùng một trong hai ⇒ **rất có thể chưa có
   bản dựng mới** ⇒ **báo điều phối TRƯỚC khi chốt verdict**, đừng lặng lẽ ghi Reopen.
2. **Không có bằng chứng dev đã sửa gì.** QA đã ghi `Reopen` lên đủ 6 dòng ngày 06/08 (dòng 127 lúc 08:38), nay cả 6
   lại về `Fixed` mà ô `DEV phản hồi lần 1` **trống**. Đo thật, đừng tin nhãn `Fixed`.
3. **Giới hạn hiệu lực.** Đo trên **env dev** `18.143.165.120.nip.io`; đối tác quay bằng chứng trên env nghiệm thu
   `htpldn-uat.ospgroup.vn` bản V1.0 / V1.0.2. Mọi kết luận "đã hết lỗi" chỉ có hiệu lực **trên bản dựng env dev**
   cho tới khi bản này lên env đối tác — **phải ghi câu giới hạn này vào ô `Kết quả verify`.**
4. **Mật khẩu:** `cbnv_tw` dùng **`Test@1234`** (KHÔNG phải `Secret@123` của `admin`). Sai nhiều lần trip rate-limit
   login (5 lần/60s) → khóa tạm. Account khóa → theo Rule 7 (fallback CÙNG vai trò + CÙNG cấp, ghi rõ account thực dùng).
5. **Chỉ MỘT agent gọi `chrome-devtools` tại một thời điểm** (lịch chạy tuần tự ở `TIEN-DO.md`).
6. **Ảnh mới lưu vào** `output/UAT_doi-tac/reverify-week-5/F3-devfix-2026-08-07/image/` — đặt tên có tiền tố
   `LKHDG_16-` + bản dựng, để không lẫn với ảnh V1.0.8 của lô 06/08.
7. **Case song sinh cùng lượt:** dòng 126 `LKHDG_12` (xuất Excel không theo bộ lọc) dùng chung màn và chung tài khoản —
   nhưng **verdict độc lập**, đừng để kết quả case này kéo case kia.
8. **Nếu bản dựng mới đã gỡ mất "Cơ quan được đánh giá" hoặc "Tài liệu đính kèm"** khỏi form Sửa → **log bug mới**
   (căn cứ `:852` / `:854`), **không** đẩy sang BA, và **không** gộp vào `BUG-LKHDG-SUA-PHANCONG`.
