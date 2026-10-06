# Tiêu chí verify — LKHDG_16

Mã case: **LKHDG_16** (dòng 127, tab `bug`)  ·  Thời điểm viết: **2026-08-06 08:20**
Môi trường verify: **https://18.143.165.120.nip.io**  ·  Bản dựng: **HTPLDN · V1.0.8**, gói mã
`assets/index-DThrFe1_.js` · (đo ở GIAI ĐOẠN B, ghi lại ở mục 6)

> Viết **TRƯỚC** khi mở màn Sửa đợt đánh giá trên env verify. Nguồn lúc viết: 2 dòng bảng đối tác (vòng 1 +
> vòng 2), bằng chứng `LKHDG_16.jpg` + `LKHDG_16.webm` (đã mở xem), và đặc tả SRS v3.5.
>
> **Khai báo minh bạch:** trước khi viết mục 4 tôi CÓ đọc hồ sơ QA đợt trước
> (`reverify-week-3/reverify-audit/LKHDG_16/audit.md`, `bug-reports/dghq/Pass-bug-report-DGHQ.md:192-241`) —
> đó là số đo trên **bản dựng CŨ**. Hồ sơ đó chỉ dùng để biết case từng được đo thế nào; mục 4 dưới đây suy ra
> từ **SCR-VI-01** trong đặc tả, không lấy kết quả đo cũ làm ngưỡng.

---

## 1. Đối tác phản ánh — tách 3 vế (2 vòng)

| Vế | Vòng | Nội dung đối tác ghi | Nguồn |
|---|---|---|---|
| **a** | 1 | "Các trường thông tin **không được chỉnh sửa**" | cột "Kết quả thực tế" |
| **b** | 1 | "**Breadcrum** hiển thị đường dẫn là *Trang chủ/Đánh giá hiệu quả/Kế hoạch đánh giá/Chi tiết*" | cột "Kết quả thực tế" |
| **c** | 2 | "**Không hiển thị danh sách các tệp đính kèm** mặc dù tồn tại dữ liệu" | cột "Kết quả verify" (giá trị cũ, sẽ bị đè) + `Trạng thái 2 = Fail` |

**Kỳ vọng đối tác ghi ở cột "Kết quả mong đợi":** *"Chỉ hiển thị khi đợt đang ở trạng thái 'Lập kế hoạch' hoặc
'Phân công', và Cán bộ nghiệp vụ thuộc đơn vị sở hữu đợt. Hệ thống mở màn hình chi tiết đợt đánh giá ở chế độ
chỉnh sửa."*

**Bằng chứng đã mở xem — đọc full-res tới khoảnh khắc lỗi:**

- `partner-evidence/LKHDG_16.jpg` (237.800 byte) — **vòng 1**. URL
  `htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/b927c33b-9c8f-4d56-952f-f084d3379c0b`, breadcrumb
  *"Trang chủ / Đánh giá hiệu quả / Kế hoạch đánh giá / **Chi tiết**"*, vai trò **CB_NV_TW** (`BTP · TW`), bản
  dựng **HTPLDN · V1.0**, 2026-07-11 10:25. Đợt `DG-20260711-0002` "TKM kiểm thử chức năng lưu & chuyển tiêu
  chí". Khối "Thông tin kế hoạch" là **bảng chỉ-đọc** (Mã kế hoạch / Tên đợt / Tần suất / Đối tượng / Mục tiêu /
  Ghi chú), không có ô nhập. Mục "Tài liệu đính kèm" **có** liệt kê `Báo cáo mẫu.docx`.
- `partner-evidence/LKHDG_16.webm` (6.002.087 byte, ~16s) — **vòng 2**, env `ospgroup.vn` bản **V1.0.2**,
  2026-07-30 14:14. Frame đã đọc:
  - `frames/LKHDG_16/t009.06s.jpg` — màn **Chi tiết** đợt `DG-20260730-0002` "Đánh giá tháng 8/2026", stepper
    đang ở bước **1 Lập kế hoạch**. Mục "Tài liệu đính kèm" liệt kê **3 tệp**: `Báo cáo mẫu.docx`,
    `Plan kiem thu.xlsx`, `2K15 T5 (30.7) & T7 (1.8).pdf` — mỗi tệp kèm [Xem] [Xóa].
  - `frames/LKHDG_16/t015.09s.jpg` — **drawer "Sửa kế hoạch đánh giá"** mở từ màn Danh sách (breadcrumb sau
    lưng vẫn là *".../ Danh sách"*). Drawer CÓ ô nhập sửa được (Thời gian bắt đầu `30/07/2026`, kết thúc
    `31/07/2026`, Ghi chú `a`) và thanh `[Hủy] [Lưu nháp] [Lưu & Chuyển tiêu chí]`. Mục **"Tài liệu đính kèm"
    trong drawer chỉ có vùng kéo-thả RỖNG**, không liệt kê 3 tệp đã tồn tại của chính đợt đó.

  ⇒ Bằng chứng vòng 2 cho thấy vế (a) và (b) **đã được sửa** (Sửa nay là drawer form, không rời màn Danh sách),
  và vế (c) là triệu chứng **mới** sinh ra từ chính cách fix đó.

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-08-danh-gia.md`.

- **Nút Sửa — điều kiện hiện** (`:837`): *"| 18 | table | Hành động | icon-group | Xem / **Sửa (chỉ
  LAP_KE_HOACH/PHAN_CONG)** / Xóa (chỉ LAP_KE_HOACH) | click → tương ứng | Luôn |"*.
- **Form tạo/sửa đợt đánh giá** (`:841-851`) — bảng thành phần, mỗi dòng điều kiện hiển thị *"Khi mở form"*:
  `#21` Tên đợt (bắt buộc, max 500) · `#22` Mục tiêu (Rich Text, bắt buộc) · `#23` Tần suất (dropdown bắt buộc) ·
  `#24` Từ ngày / Đến ngày (validate `tu_ngay < den_ngay`) · `#25` Đối tượng (dropdown bắt buộc) ·
  `#26` Ghi chú (textarea max 2000) · `#27` Thanh hành động `[Hủy] [Lưu nháp] [Lưu & Chuyển tiêu chí]`.
- **Vai trò / phạm vi** (`:95`, `:100-101`): tác nhân *Cán bộ Nghiệp vụ (TW/BN/ĐP)*, cần quyền *"Quản lý đánh
  giá"*, *"Phạm vi dữ liệu áp dụng theo đơn vị"*. AC `:159`: *"**Given** CB NV chỉnh sửa KH chưa duyệt **When**
  thay đổi **Then** validate + lưu"*.
- **Trường đính kèm trên thực thể** (`:1043`): `KE_HOACH_DANH_GIA` #15 `file_dinh_kem | file[] | N |
  PDF/DOC/DOCX/XLS/XLSX, max 20MB/file | — | File đính kèm kế hoạch đánh giá [CR-07]`.

**IM LẶNG về:**
- **Breadcrumb của màn Sửa / màn chi tiết đợt.** Cả nhóm VI chỉ có **1** dòng breadcrumb — `:820`, và dòng đó
  đặc tả breadcrumb của **màn danh sách** (*"Trang chủ > Đánh giá > Theo dõi đánh giá hiệu quả HTPL"*). Phần B
  (màn chi tiết 4 tab, `:853-900`) và "Quy tắc tương tác" (`:902-912`) không có dòng breadcrumb nào.
- **Việc form Sửa có phải hiển thị danh sách tệp đã đính kèm hay không.** Thực thể **có** trường `file_dinh_kem`
  (`:1043`), nhưng bảng thành phần form tạo/sửa (`:843-851`) là **danh sách đóng 7 dòng #21-#27** và **không**
  có dòng nào tên "Tài liệu đính kèm". Không có dòng đặc tả màn hình nào bắt form Sửa phải render danh sách đó.
  ⇒ Hai cách đọc đều dẫn tới **cần BA**: (i) nếu coi bảng là danh sách **đóng** thì đặc tả đang nói form chỉ có
  7 thành phần ⇒ kỳ vọng đối tác **ngược** đặc tả — mà *"kỳ vọng đối tác khác đặc tả ⇒ luôn là câu hỏi cho BA,
  không phải verdict của QA"*; (ii) nếu coi là **im lặng** thì cũng là cần BA. QA **không** tự bác đối tác.

## 3. Precondition

- Tài khoản **`cbnv_tw`** (CB Nghiệp vụ Trung ương, `Test@1234`) — trùng vai trò + trùng cấp với đối tác
  (`CB_NV_TW`, `BTP · TW` đọc từ ảnh vòng 1 và frame vòng 2). Không dùng `admin` để ra verdict.
- Màn **Đánh giá hiệu quả → Kế hoạch đánh giá → Danh sách**, `/danh-gia/ke-hoach/danh-sach`.
- Dữ liệu tiền đề: đợt ở trạng thái **Lập kế hoạch** hoặc **Phân công** (mới có nút Sửa theo `:837`), thuộc
  đơn vị của tài khoản, và **đã có ≥1 tệp đính kèm**. Chưa có tệp thì **phải tự đính kèm** trước khi đo —
  đây là tiền đề *tạo được*, không phải blocker.

## 4. Tiêu chí chấm

### Vế (a) — các trường có sửa được không: CHẤM ĐƯỢC

**✅ PASS khi** — trên đợt đang ở `Lập kế hoạch`, bấm **[Sửa]** thì hệ thống mở giao diện **nhập liệu** cho
đúng đợt đó, trong đó **cả 6 thành phần dữ liệu** `:845-850` đều **nhập/đổi được** (Tên đợt · Mục tiêu ·
Tần suất · Từ ngày/Đến ngày · Đối tượng · Ghi chú), **và** sau khi đổi ≥1 trường rồi lưu thì giá trị mới
**thực sự được lưu** — mở lại thấy giá trị mới (không chỉ hiện toast).

**❌ FAIL nếu** — bất kỳ: giao diện mở ra là bảng **chỉ-đọc** không có ô nhập · thiếu thành phần nhập cho ≥1
trong 6 mục trên · đổi rồi lưu nhưng mở lại vẫn là giá trị cũ.

### Vế (b) — breadcrumb: CHẤM ĐƯỢC MỘT PHẦN, chỉ chấm "có rời khỏi ngữ cảnh Sửa hay không"

**✅ PASS khi** — thao tác [Sửa] **không** đưa người dùng sang một màn mà hệ thống tự gọi là *"Chi tiết"*: hoặc
breadcrumb giữ nguyên ngữ cảnh danh sách/sửa, hoặc tiêu đề khu vực nhập liệu nói rõ đang **Sửa**.

**❌ FAIL nếu** — bấm [Sửa] mà hệ thống mở đúng màn **Xem chi tiết** (cùng đường dẫn với nút Xem) và không có
dấu hiệu nào cho biết đang ở chế độ sửa.

**KHÔNG được chấm Fail vì** *chuỗi ký tự* breadcrumb khác một mẫu cụ thể nào đó — đặc tả **im lặng** về
breadcrumb màn Sửa (mục 2), nên đòi đúng một chuỗi là QA tự đặt luật.

### Vế (c) — danh sách tệp đính kèm trong form Sửa: **KHÔNG CHẤM**

→ **cần BA** vì *đặc tả có trường `file_dinh_kem` trên thực thể (`:1043`) nhưng bảng thành phần form tạo/sửa
(`:843-851`) là danh sách đóng 7 dòng và không có "Tài liệu đính kèm" — kỳ vọng của đối tác không có chỗ dựa
trong đặc tả màn hình, cũng không bị đặc tả bác bỏ.*

Với vế này: **đo và chụp ảnh hiện trạng, ghi vào file gửi BA, không kết luận đúng/sai.** Đo thêm 1 điều mà
đối tác không nêu nhưng ảnh hưởng trực tiếp tới an toàn dữ liệu: **lưu form Sửa (không đụng vùng đính kèm) có
làm mất các tệp đã có không** — nếu mất thì đó là lỗi mới do cách fix gây ra, xử riêng, không kéo verdict.

**Phép thử mục 4:** người chưa biết bug này, chỉ đọc mục 4, có chấm được PASS/FAIL cho (a) và (b) không?
→ Có: mở [Sửa], đếm số ô nhập được, đổi 1 trường rồi lưu và mở lại đối chiếu.

## 5. Dạng dữ liệu phải phủ — M = 3

1. Đợt trạng thái **Lập kế hoạch** có **đúng 1** tệp đính kèm.
2. Đợt trạng thái **Lập kế hoạch** có **≥2** tệp, **khác định dạng** nhau (vd `.docx` + `.pdf`).
3. Đợt trạng thái **Phân công** có **≥1** tệp.

**Nguồn xác định M:** cách ② — giá trị enum ngay trên màn + ràng buộc trên thực thể: `:837` cho biết nút Sửa
hiện ở **2** trạng thái (`LAP_KE_HOACH`, `PHAN_CONG`) nên phải phủ cả hai; `:1043` khai `file_dinh_kem` là
`file[]` **nhiều định dạng** nên phải phủ cả trường hợp 1 tệp và nhiều tệp khác định dạng.
Không dùng cách ① vì nhóm VI không có FR nào đặc tả luồng đính kèm tệp của kế hoạch đánh giá.

## 6. Bảng điều kiện — số đo GIAI ĐOẠN B (2026-08-06 08:35–08:50)

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — "Cán bộ Nghiệp vụ Trung ương", đơn vị `BTP · TW` (cả 2 vòng) | **`cbnv_tw`** — CB_NV_TW, `BTP · TW`. Trùng vai trò + trùng cấp | Không |
| Entity + trạng thái | Vòng 1 `DG-20260711-0002` **Lập kế hoạch**; vòng 2 `DG-20260730-0002` **Lập kế hoạch**, 3 tệp | `DG-20260730-0002` **Lập kế hoạch** (2 tệp) · `DG-20260806-0001` **Lập kế hoạch** (1 tệp) rồi đẩy tiếp sang **Phân công** (giữ 1 tệp) — phủ rộng hơn đối tác | Không |
| Dữ liệu tiền đề | Đợt đã sẵn 3 tệp (`.docx` + `.xlsx` + `.pdf`) | Tự đính kèm qua vùng kéo-thả thật: `QA-LKHDG16-baocao-mau.docx` (1.298 B) + `QA-LKHDG16-ke-hoach.pdf` (398 B) cho đợt 2 tệp; riêng `.pdf` cho đợt 1 tệp. API xác nhận `trangThaiQuet=SACH` | Không |
| Input / filter / giá trị nhập | Mở **[Sửa]** từ màn Danh sách, đổi Thời gian bắt đầu/kết thúc + Ghi chú `a` | Mở **[Sửa]** từ màn Danh sách. Đợt 2 tệp: đổi Tên đợt + Ghi chú, dấu `QA-LKHDG16-EDIT-20260806-0830`. Đợt 1 tệp: đổi Ghi chú, dấu `QA-LKHDG16-V1-1TEP-20260806`. Cả 2 lượt mở lại đối chiếu bằng **2 đường**: đọc bản ghi qua API + mở lại drawer trên giao diện | Không |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 1 đợt/vòng, đều **Lập kế hoạch** | **M = 2/3.** Dạng 1 (Lập kế hoạch · 1 tệp) ✓ · Dạng 2 (Lập kế hoạch · 2 tệp khác định dạng) ✓ · **Dạng 3 (Phân công · ≥1 tệp) ĐO KHÔNG ĐƯỢC** — ở trạng thái Phân công hệ thống không mở được chế độ sửa: hàng chỉ còn nút Xem, màn chi tiết chỉ có [Hủy đợt] và 0 ô nhập, gọi thẳng API sửa trả 409 `ERR-BIZ-XI-01-02` *"Không thể cập nhật kế hoạch ở trạng thái 'PHAN_CONG'"* | **Có** |

**GAP còn lại: 1 — và chính GAP đó là kết quả đo, không phải chỗ hổng của phép đo.**
Dạng 3 không đo được **không phải** vì thiếu dữ liệu tiền đề (đợt Phân công có tệp đã dựng xong, đúng tiền đề mục 3)
mà vì hệ thống chặn hẳn lối vào sửa ở trạng thái đó. Vì `srs-fr-08-danh-gia.md:837` **và** kỳ vọng đối tác ghi ở cột
"Kết quả mong đợi" của chính phiếu này (*"Chỉ hiển thị khi đợt đang ở trạng thái 'Lập kế hoạch' hoặc 'Phân công'…"*)
đều đòi có [Sửa] ở **cả hai** trạng thái, việc không vào được là **kết quả FAIL của vế (a) trên dạng 3**, chứ không
làm verdict yếu đi. Verdict vì vậy tựa trên 3 phép đo hoàn chỉnh (2 dạng PASS + 1 dạng FAIL), không có ô nào bỏ trống.

**3 dữ kiện neo (đối tác):**
- **URL / bản ghi:** vòng 1 `htpldn-uat.ospgroup.vn/danh-gia/ke-hoach/b927c33b-9c8f-4d56-952f-f084d3379c0b`
  (đợt `DG-20260711-0002`); vòng 2 `…/danh-gia/ke-hoach/b863bd1a-4b4a-4819-838d-154e4cbbeccf` (đợt
  `DG-20260730-0002` "Đánh giá tháng 8/2026") rồi drawer Sửa mở từ `…/danh-gia/ke-hoach/danh-sach`
- **Trạng thái entity:** cả 2 vòng đều là đợt ở **Lập kế hoạch** (vòng 2 thấy rõ stepper ở bước 1); vòng 2 đợt
  có **3 tệp** đính kèm (`.docx` + `.xlsx` + `.pdf`)
- **Vai trò + bản dựng:** `CB_NV_TW` · `BTP · TW` · vòng 1 **HTPLDN · V1.0** (2026-07-11 10:25) · vòng 2
  **HTPLDN · V1.0.2** (2026-07-30 14:14) · env `htpldn-uat.ospgroup.vn`

> ⚠️ **Lệch env + bản dựng:** đối tác quay trên env nghiệm thu `ospgroup.vn` bản V1.0 / V1.0.2; lượt này đo
> trên env dev `18.143.165.120.nip.io` bản V1.0.8. Đây là **giới hạn hiệu lực** của verdict, không phải GAP.

## 7. Sửa đổi so với lần viết trước + chỗ phép đo suýt nói dối

**2026-08-06 08:50 — không nới lỏng tiêu chí nào.** Mục 1-5 giữ nguyên như lúc viết (trước khi mở màn Sửa).
Chỉ điền mục 6 bằng số đo thật.

**Cảnh báo phép đo (ghi lại để lượt sau không sập bẫy):** bản dựng V1.0.8 đổi tên lớp CSS so với thư viện chuẩn —
drawer là `.ant-drawer-section` (không phải `.ant-drawer-content`), giá trị dropdown nằm ở `.ant-select-content`
(không phải `.ant-select-selection-item`), và danh sách tệp đính kèm **không** dùng `.ant-upload-list-item`. Kịch bản
đọc DOM theo tên lớp cũ trả về "(trống)" / "0 tệp" cho những chỗ **thực tế có dữ liệu**. Mọi kết luận ở mục 6 vì vậy
đều được chốt bằng **ảnh chụp đã mở xem** + **đọc lại bản ghi qua API**, không chốt bằng một mình kịch bản DOM.
