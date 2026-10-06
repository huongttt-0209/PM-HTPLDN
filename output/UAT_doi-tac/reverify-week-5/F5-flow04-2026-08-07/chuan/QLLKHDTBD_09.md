# QLLKHDTBD_09 — CHUẨN CHẤM (FLOW 04 · Giai đoạn A)

> **Giai đoạn A — chưa mở màn đang tranh chấp.** File này chỉ khóa chuẩn chấm. Verdict do Giai đoạn B ra.

---

## 1. Bảng đầu

| Mục | Giá trị |
|---|---|
| Bảng / tab / dòng | Bảng đối tác 2026-08-07 · tab `bug` · **dòng 20** |
| Mã TC | `QLLKHDTBD_09` — "Xuất Excel với điều kiện lọc" |
| Trạng thái nguồn | Trạng thái `Fail` · Dopai `dev done` · Trạng thái dev fix `Fixed` · DEV phản hồi lần 1 **(trống)** · Kết quả verify **(trống)** |
| TKM phản hồi lần 1 | `QLLKHDTBD_09_v2.jpg` + *"File excel được xuất thiếu trường thông tin Người tạo, Ngày tạo"* |
| Env đo | `https://18.143.165.120.nip.io` |
| Tài khoản dự kiến | `cbnv_tw_02` / `Test@1234` — vai trò **CB_NV_TW** (cùng vai trò + cấp với `cbnv_tw_01` đã dùng đo vòng 03-04/08, và cùng vai trò với đối tác trong video: badge `Cán bộ NV Trung ương · CB_NV_TW`). OTP qua MailHog `http://18.143.165.120:8025` |
| Màn | **Kế hoạch đào tạo năm** — SCR-III-00 · FR-III-14 (UC33) |
| URL | `/dao-tao/ke-hoach/danh-sach` (đối tác dùng `?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`) |
| SRS đã đọc | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-03-dao-tao.md` — **tổng 2296 dòng**<br>`Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-v3.5.md` — **tổng 7012 dòng** |

> 🔴 **Số dòng trong file này là số TỰ ĐẾM LẠI ngày 2026-08-07, không bê từ hồ sơ cũ.**
> Hồ sơ 03/08 (`.../verify1-conlai-2026-08-03/srs/QLLKHDTBD_09-srs.md`) dẫn `srs-v3.5.md:5524`, `srs-fr-03-dao-tao.md:1752 / 1147-1153 / 1201 / 1193 / 1755-1759 / 2220`. **Toàn bộ đã lệch** — nay lần lượt là `:5570`, `:1775`, `:1170-1176`, `:1224`, `:1216`, `:1778-1782`, `:2243`.
> Ngoài lệch dòng, **nội dung BR-DATA-06 cũng đã đổi**: hồ sơ cũ chép cột ngoại lệ là *"Báo cáo nhóm IX có xuất **Word**"*, bản chốt hiện tại ghi *"Báo cáo nhóm IX có xuất **PDF theo khung TT 17/2025**"*. ⇒ Cấm tái sử dụng bất kỳ trích dẫn nào từ hồ sơ cũ.

---

## 2. Nguồn đã đọc

**SRS (nguồn chuẩn duy nhất — tự mở trong lượt này):**
- `srs-fr-03-dao-tao.md:1090` — heading `FR-III-14: Lập kế hoạch đào tạo năm (UC33)`
- `srs-fr-03-dao-tao.md:1170-1176` — `Processing — Xuất Excel`
- `srs-fr-03-dao-tao.md:1189-1200` — `Outputs — Danh sách` (8 trường)
- `srs-fr-03-dao-tao.md:1216` — `ERR-KH-06` (giới hạn 10.000 dòng)
- `srs-fr-03-dao-tao.md:1224` — Acceptance Criteria xuất Excel
- `srs-fr-03-dao-tao.md:1765-1833` — **SCR-III-00 đọc TRỌN** (Thành phần 1→5 + Thông báo + UX-Spec ref)
- `srs-fr-03-dao-tao.md:2243` — bảng BR nhóm III: BR-DATA-06 áp cho FR-III-14
- `srs-v3.5.md:5570` — **BR-DATA-06** (bản chốt)
- `srs-v3.5.md:67` — dòng lịch sử phiên bản 3.5, mục (5) *"Câu hỏi BA chưa quyết"*
- Đối chứng phủ định (đã thử từ đồng nghĩa): `xuất excel · xuất file · kết xuất · tải xuống · export · người tạo · ngày tạo · người lập · ngày lập · thời điểm tạo · nguoi_tao · ngay_tao · created_at · createdBy · mẫu xuất · cấu trúc file xuất · các cột của tệp` — grep toàn thư mục `srs-v3.5/`.

**Bằng chứng đối tác (đã mở xem, không tin tên tệp):**
- `.../F5-flow04-2026-08-07/partner-evidence/QLLKHDTBD_09_v2.jpg`
- `.../F5-flow04-2026-08-07/partner-evidence/QLLKHDTBD_09.webm` → 5 frame tại `.../F5-flow04-2026-08-07/frames/QLLKHDTBD_09/`

**Tham chiếu (CHỈ để biết tra chỗ nào — KHÔNG dùng làm căn cứ verdict):** bug entry `BUG-QLLKHDTBD_09` + `reverify-audit/` + `cond/` + `srs/` của tuần 2, và 11 tệp `.xlsx` fixture cũ.

---

## 3. Đọc bằng chứng đối tác

### 3.1 Ảnh `QLLKHDTBD_09_v2.jpg` — bằng chứng vòng NÀY (quan trọng nhất)

Ảnh là **ảnh chụp nội dung tệp Excel mở trong MS Excel (Protected View)**, không phải ảnh màn hình web.

| Quan sát | Giá trị đọc được |
|---|---|
| Tên tệp trên thanh tiêu đề | `ke-hoach-dao-tao-1785838454544.xlsx` |
| Epoch trong tên tệp | `1785838454544` → **2026-08-04 17:14:14** |
| Đồng hồ máy trong ảnh | `05:17 PM · 2026-08-04` (khớp — ảnh chụp ~3 phút sau khi tải) |
| Tên sheet | `Kế hoạch đào tạo` |
| **Hàng tiêu đề (nguyên văn, A1→G1)** | `Mã KH` · `Tên kế hoạch` · `Năm` · `Từ ngày` · `Đến ngày` · `Ngân sách (VNĐ)` · `Trạng thái` |
| Số cột | **7** (A→G; H trở đi trống) |
| Số dòng dữ liệu | **4** (dòng 2→5; dòng 6 trở đi trống) |
| Các bản ghi | `KH-20260725-0003` Từ chối · `KH-20260725-0001` Đã duyệt · `KH-20260723-0001` Đã duyệt · `KH-20260515-0001` Chờ duyệt |

⇒ **Xác nhận vế mới của TKM: tệp xuất KHÔNG có cột `Người tạo` và KHÔNG có cột `Ngày tạo`.**

🔴 **Điều ảnh này KHÔNG chứng minh được:** ảnh chỉ có cửa sổ Excel, **không có cửa sổ trình duyệt** ⇒ **không biết đối tác đã đặt bộ lọc nào** và **màn hình lúc đó có bao nhiêu kết quả**. Vì vậy ảnh v2 **không tự nó** kết luận được vế C1 (lọc) là đạt hay không đạt.

### 3.2 Video `QLLKHDTBD_09.webm` — bằng chứng vòng 1 (~13 giây, 5 frame)

| Frame | Nội dung |
|---|---|
| `t003.03s.jpg` | Màn danh sách. URL `htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/danh-sach?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`. Vai trò `Cán bộ NV Trung ương · CB_NV_TW`, đơn vị `BTP · TW`. Bộ lọc: Từ ngày `01/07/2026`, Đến ngày `31/07/2026`. Tab `Tất cả 2`. **Chân bảng: "Hiển thị 1-2 / 2 kết quả"** — 2 bản ghi `KH-20260725-0001`, `KH-20260723-0001`. Đồng hồ `10:30 AM · 2026-07-25`. |
| `t009.05s.jpg` | Toast **"Xuất Excel thành công"**. Hộp thoại Save As, tên tệp `ke-hoach-dao-tao-1784950244818.xlsx` (→ **2026-07-25 10:30:44**). |
| `t012.07s.jpg` | Tệp vừa tải mở trong Excel. Hàng tiêu đề **giống hệt 7 cột ở §3.1**. **13 dòng có dữ liệu tính cả tiêu đề ⇒ 12 dòng dữ liệu** (dòng 2→13), gồm cả `KH-20260525-0001`, `KHDT-HDSD-AG-001`, `KH-20260509-0001/2/3`, `KH-20260508-0001/4/5/6` — **các bản ghi KHÔNG nằm trong 2 kết quả trên màn**. |

⇒ **Lỗi gốc vòng 1 tái hiện rõ: màn 2 · tệp 12.** Đây đúng là *"xuất toàn bộ danh sách hiện có"*.
⇒ **Cột `Người tạo` / `Ngày tạo` đã vắng mặt NGAY TỪ VÒNG 1 (25/07)** — vế C2 **không phải** do bản fix mới sinh ra, mà là tồn tại từ đầu, chỉ mới được TKM nêu ra ở vòng này.

### 3.3 Neo tái hiện rút ra

| Neo | Giá trị |
|---|---|
| Màn | `Đào tạo, tập huấn` → `Kế hoạch đào tạo` → `Danh sách` |
| URL pattern | `/dao-tao/ke-hoach/danh-sach?tuNgay=<yyyy-mm-dd>&denNgay=<yyyy-mm-dd>&page=1` |
| Vai trò | CB_NV_TW, đơn vị BTP · TW |
| Bộ lọc đối tác vòng 1 | Từ ngày `01/07/2026` · Đến ngày `31/07/2026` |
| Số đo quyết định vòng 1 | màn **2** kết quả · tệp **12** dòng dữ liệu |
| Nút | `Xuất Excel` (cạnh `+ Thêm mới` và `Làm mới`) |
| Tên tệp tải về | `ke-hoach-dao-tao-<epoch_ms>.xlsx`, sheet `Kế hoạch đào tạo` |

⚠️ **Env đối tác là `htpldn-uat.ospgroup.vn`, env đo của ta là `18.143.165.120.nip.io`** — hai môi trường khác dữ liệu. Không so số bản ghi tuyệt đối giữa hai bên; chỉ so **quan hệ số màn ↔ số dòng tệp** trong cùng một lần đo.

### 3.4 Manh mối (KHÔNG phải căn cứ verdict)

Tệp v2 của đối tác (04/08) có **4 dòng**, là **tập con** của 12 bản ghi thấy ở vòng 1. Điều này *gợi ý* vế lọc có thể đã được xử lý trên env đối tác — nhưng vì không biết bộ lọc họ đặt (§3.1), **không được dùng để chấm C1**. Ta vẫn phải tự đo lại C1 trong vòng này.

---

## 4. Hàng tiêu đề tệp `.xlsx` cũ (đọc bằng `openpyxl`)

> 🔴 **Đây là dữ liệu THAM CHIẾU của bản dựng cũ (03-04/08), KHÔNG phải phép đo của vòng này.** Dùng để trả lời đúng một câu hỏi: *vế "thiếu Người tạo / Ngày tạo" là tồn tại từ đầu hay mới phát sinh?*

**Hàng tiêu đề — GIỐNG HỆT NHAU ở cả 11/11 tệp:**

```
Mã KH | Tên kế hoạch | Năm | Từ ngày | Đến ngày | Ngân sách (VNĐ) | Trạng thái
```

Tên sheet ở cả 11 tệp: `Kế hoạch đào tạo`. **Không tệp nào có cột `Người tạo`, `Ngày tạo`, `Người lập`, `Ngày lập` hay `Thời điểm tạo`. Cũng không tệp nào có cột `Số chương trình`.**

| # | Đường dẫn tệp | Số cột | Số dòng dữ liệu |
|---|---|---|---|
| 1 | `output/UAT_doi-tac/reverify-week-2/verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/01-khong-loc-12-dong.xlsx` | 7 | 12 |
| 2 | `.../verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/02-loc-tungay-01.07-denngay-31.07.2026-man-1-file-13-dong.xlsx` | 7 | 13 |
| 3 | `.../verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/03-loc-tukhoa-RECON-man-2-file-13-dong.xlsx` | 7 | 13 |
| 4 | `.../verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/retest0804-01-khong-loc-man14-file14.xlsx` | 7 | 14 |
| 5 | `.../verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/retest0804-02-locA-tungay01.07-denngay31.07-man1-file1.xlsx` | 7 | 1 |
| 6 | `.../verify1-conlai-2026-08-03/fixtures/QLLKHDTBD_09/retest0804-03-locB-tukhoa-RECON-man2-file2.xlsx` | 7 | 2 |
| 7 | `output/UAT_doi-tac/reverify-week-2/verify2-audit-2026-08-04/fixtures/QLLKHDTBD_09/v2-00-khong-loc.xlsx` | 7 | 15 |
| 8 | `.../verify2-audit-2026-08-04/fixtures/QLLKHDTBD_09/v2-01-locA-tungay-denngay.xlsx` | 7 | 3 |
| 9 | `.../verify2-audit-2026-08-04/fixtures/QLLKHDTBD_09/v2-02-locB-tukhoa-TKM.xlsx` | 7 | 2 |
| 10 | `.../verify2-audit-2026-08-04/fixtures/QLLKHDTBD_09/v2-03-locC-tab-Nhap.xlsx` | 7 | 1 |
| 11 | `.../verify2-audit-2026-08-04/fixtures/QLLKHDTBD_09/v2-04-phantrang-pagesize10.xlsx` | 7 | 15 |

**Kết luận tham chiếu (3 điểm, dùng cho Giai đoạn B):**
1. Vế C2 **tồn tại liên tục** từ 25/07 (video đối tác) → 03/08 → 04/08 (fixture QA + ảnh v2 đối tác). **Không phải hồi quy do bản fix.**
2. Bộ 7 cột **ổn định tuyệt đối** qua 2 env và 3 mốc thời gian ⇒ nếu vòng này vẫn 7 cột thì là hành vi có chủ đích của dev, không phải trục trặc ngẫu nhiên.
3. Các tệp #5/#6/#8/#9/#10 (03-04/08) có số dòng **nhỏ hơn hẳn** tệp không lọc cùng ngày ⇒ đó là lý do QA chấm Closed hồi 04/08. **KHÔNG được dùng dữ kiện này để Pass vòng này** (luật FLOW 04: cấm Pass bằng hồ sơ cũ; và đây là bản dựng khác).

---

## 5. BUG SCOPE LOCK

| Vế | Expected đối tác (nguyên văn) | SRS `file:dòng` | Quan hệ | Route | Đường đo |
|---|---|---|---|---|---|
| **C1** | *"Hệ thống xuất danh sách theo điều kiện lọc hiện tại ra tệp Excel."* (KQ mong đợi) — đối lập KQ thực tế *"Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách"* | `srs-v3.5.md:5570` · `srs-fr-03-dao-tao.md:1775` · `srs-fr-03-dao-tao.md:1175` | **MATCH** | **TEST** | Bấm `Xuất Excel` trên UI sau khi lọc → mở tệp bằng `openpyxl`, đếm dòng dữ liệu, so với số kết quả trên màn |
| **C2** | *"File excel được xuất thiếu trường thông tin Người tạo, Ngày tạo"* (TKM phản hồi lần 1) | **IM LẶNG** về danh mục cột của **TỆP XUẤT**; đồng thời SRS **tự lệch** giữa `srs-fr-03-dao-tao.md:1795-1796` (bảng trên màn CÓ 2 cột này) và `srs-fr-03-dao-tao.md:1189-1200` (Outputs Danh sách KHÔNG có 2 cột này) | **GAP** | **BA** | Chỉ đo hiện trạng để làm rõ câu hỏi BA: in nguyên văn hàng tiêu đề tệp. **Cấm Pass/Reopen vế này.** |

---

### 5.1 C1 — trích nguyên văn SRS

**`srs-v3.5.md:5570`** (BR-DATA-06 — cột "Áp dụng" ghi `Toàn bộ CRUD list` ⇒ default áp dụng, không cần FR nhắc lại):

> `| BR-DATA-06 | **Export Excel:** Mọi danh sách có tính năng xuất Excel. File xuất theo bộ lọc hiện tại, không vượt quá 10,000 rows/file | Pattern IP-01 | Toàn bộ CRUD list | Báo cáo nhóm IX có xuất PDF theo khung TT 17/2025 | Test export limit |`

**`srs-fr-03-dao-tao.md:2243`** (bảng BR nhóm III — xác nhận BR-DATA-06 áp cho đúng FR-III-14):

> `| BR-DATA-06 | Export Excel | FR-III-01, FR-III-05, FR-III-06, FR-III-14 |`

**`srs-fr-03-dao-tao.md:1775`** (SCR-III-00 Thành phần 1 — đúng nút trên màn đang tranh chấp):

> `- Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng`

**`srs-fr-03-dao-tao.md:1170-1176`** (FR-III-14 Processing — Xuất Excel):

> `**Processing — Xuất Excel:**`
> `| Bước | Mô tả xử lý | BR áp dụng |`
> `| 1 | Kiểm tra quyền | BR-AUTH-01 |`
> `| 2 | Lấy danh sách theo filter, tối đa 10.000 dòng | BR-DATA-06 |`
> `| 3 | Tạo file Excel + trả về download | — |`

**Kết luận C1:** SRS nói rõ, **khớp** kỳ vọng đối tác trên cả 3 tầng (BR toàn hệ thống · SCR màn · FR Processing). ⇒ `MATCH` → route **TEST** → chốt Pass/Reopen bằng phép đo vòng này.

---

### 5.2 C2 — trích nguyên văn SRS + phân tích khoảng trống

**Dòng SRS mạnh nhất VỀ PHÍA đối tác — `srs-fr-03-dao-tao.md:1786-1796`** (SCR-III-00 **Thành phần 3 — Bảng kế hoạch**):

> `| Cột | Mô tả |`
> `|-----|-------|`
> `| Chọn dòng | hộp tích chọn nhiều bản ghi |`
> `| Tên kế hoạch | liên kết đến chi tiết / sửa |`
> `| Năm | YYYY |`
> `| Thời gian | dd/mm/yyyy – dd/mm/yyyy |`
> `| Ngân sách dự kiến | Định dạng dấu chấm (vd "500.000.000 đ"); rỗng → "—" |`
> `| Số chương trình | COUNT CTDT thuộc kế hoạch năm |`
> `| Trạng thái | Badge màu: ... |`
> `| Người tạo | Họ tên cán bộ tạo |`
> `| Ngày tạo | dd/mm/yyyy |`

🔴 **Đây là đặc tả của BẢNG TRÊN MÀN HÌNH, không phải của TỆP EXCEL.** SRS không có bất kỳ câu nào nói *"tệp xuất gồm đúng các cột của bảng"*.

**Dòng SRS ngược lại — `srs-fr-03-dao-tao.md:1189-1200`** (FR-III-14 **Outputs — Danh sách**, 8 trường):

> `| 1 | id | ... | 2 | ten_ke_hoach | ... | 3 | nam | ... | 4 | thoi_gian | ... | 5 | ngan_sach_du_kien | ... | 6 | so_ctdt | ... | 7 | trang_thai | ... | 8 | total_count | ... |`

⇒ **`Outputs — Danh sách` KHÔNG có `nguoi_tao` / `ngay_tao`.** Vậy chính SRS có **hai định nghĩa khác nhau** cho chữ *"danh sách"* mà `:1775` và `:1175` viện dẫn — dùng bản nào thì ra kết quả chấm ngược nhau.

**Bằng chứng SRS tự nhận còn nợ đặc tả mẫu xuất — `srs-v3.5.md:67`** (lịch sử phiên bản 3.5, mục (5)):

> `**Câu hỏi BA chưa quyết** (defer Sprint sau): cite TT 17/2025/TT-BTP, NĐ55/2019 Đ.8 K.1, mẫu xuất Excel UC159.`

(Đối chiếu `CHANGELOG-v3-to-v3.5.md:2518` — *"v4 chưa thêm bảng Inputs (filter áp dụng) và **Outputs (cấu trúc cột Excel)** tương ứng cho luồng Excel"* — và `:2557`, `:3556`. Ghi chú: những dòng này nói về UC159 / HĐ TV, **không phải** SCR-III-00; đưa vào đây chỉ để chứng minh SRS **chưa từng** chuẩn hóa cấu trúc cột tệp xuất ở bất kỳ màn nào, **không** dùng làm yêu cầu cho màn này.)

**Đối chứng phủ định:** grep toàn thư mục `srs-v3.5/` với `mẫu xuất · cấu trúc file xuất · định dạng file xuất · các cột của tệp` → **0 kết quả** định nghĩa cột tệp xuất cho SCR-III-00. Tiền lệ ngược: SRS **biết cách** liệt kê cột tệp xuất khi muốn — `srs-fr-03-dao-tao.md:609-625` (FR-III-05) có hẳn bảng Outputs 13 trường cho tệp Xuất Excel kết quả. **Có mẫu ở FR-III-05 mà không có ở FR-III-14 ⇒ im lặng là im lặng thật, không phải do đọc sót.**

**Kết luận C2:** SRS **im lặng** về danh mục cột của tệp Excel xuất ra ở SCR-III-00, và **tự mâu thuẫn** về nghĩa của chữ *"danh sách"*. Không xác định được chuẩn chấm ⇒ `GAP` → route **BA**. **Cấm Pass, cấm Reopen vế C2.**

---

### 5.3 Câu bắt buộc + câu hỏi BA cho C2

> **CẦN BA CONFIRM:** đối tác kỳ vọng *tệp Excel xuất từ màn Kế hoạch đào tạo năm phải có trường "Người tạo" và "Ngày tạo"*; SRS quy định *hai cột này thuộc **bảng hiển thị trên màn** (`srs-fr-03-dao-tao.md:1795-1796`) nhưng **không quy định danh mục cột của tệp Excel xuất ra** — phần xuất Excel chỉ ràng buộc phạm vi dữ liệu ("theo bộ lọc hiện tại", ≤10.000 dòng) tại `srs-v3.5.md:5570` và `srs-fr-03-dao-tao.md:1775 / :1175`; đồng thời `Outputs — Danh sách` của FR-III-14 (`srs-fr-03-dao-tao.md:1189-1200`) lại **không có** hai trường này*; web/dev hiện tại *`<điền sau khi đo Giai đoạn B — hàng tiêu đề nguyên văn + số cột>`*.

**Câu hỏi BA cụ thể (3 câu, trả lời được là đóng được GAP):**

1. **Tệp Excel xuất từ SCR-III-00 phải gồm đúng những cột nào?** Cụ thể: lấy theo **Thành phần 3 — Bảng kế hoạch** (`:1786-1796`, gồm `Người tạo` + `Ngày tạo`), hay theo **`Outputs — Danh sách`** của FR-III-14 (`:1189-1200`, không có 2 cột này)? Xin bổ sung một bảng "Outputs — Tệp Xuất Excel" vào FR-III-14 theo đúng cách đã làm ở FR-III-05 (`:609-625`).
2. Nếu chốt theo Thành phần 3: **cột `Số chương trình`** (có trong bảng màn, `:1793`) **có phải nằm trong tệp xuất không?** — hiện tệp xuất cũng không có cột này, nên câu trả lời sẽ quyết định phạm vi bug rộng hơn chỉ 2 cột TKM nêu.
3. **Cột `Mã KH`** có trong tệp xuất thực tế nhưng **không có** trong cả `:1786-1796` lẫn `:1189-1200`. Đây là cột được chấp nhận (bổ sung vào đặc tả) hay là cột thừa cần gỡ?

⚠️ **Ghi chú thể loại GAP (luật khóa 5 + mục "Với vế GAP" của FLOW 04):** nếu Giai đoạn B đo ra web **đang có** đủ `Người tạo`/`Ngày tạo` trong tệp, thì `WEB HIỆN TẠI` ghi *"đúng kỳ vọng đối tác"*, câu hỏi BA đổi mục đích thành **bổ sung điều này vào đặc tả** — **không** phải chặn bàn giao, và **vẫn không** được chuyển C2 thành MATCH/Pass.

---

## 6. Đường đo tối thiểu

> 🔴 **Hành động xuất tệp BẮT BUỘC bấm nút `Xuất Excel` trên UI thật.** Cấm gọi API thay thao tác. API chỉ được dùng ở bước đối chứng.
> 🔴 **Đối chứng = mở tệp bằng `openpyxl` đọc nội dung.** CẤM dừng ở *"tải được tệp"* / *"HTTP 200"* / *"có binary"*.

### C1 — tệp xuất theo đúng bộ lọc hiện tại

| | Nội dung |
|---|---|
| **Đường UI thật** | Login `cbnv_tw_02` → sidebar `Đào tạo, tập huấn` → `Kế hoạch đào tạo` → đọc & ghi **tổng số bản ghi khi KHÔNG lọc** (chân bảng `Hiển thị x-y / N kết quả`) → đặt bộ lọc §7 → `Tìm kiếm` → đọc & ghi **số kết quả sau lọc M** (M < N) → bấm **`Xuất Excel`** → ghi lại toast hiện ra |
| **Đối chứng độc lập** | Mở tệp `.xlsx` bằng `openpyxl`, đếm **số dòng dữ liệu** (`max_row − 1`, sau khi loại dòng trống đuôi) và liệt kê `Mã KH` từng dòng |
| **Đạt** | Số dòng dữ liệu **= M**, và tập `Mã KH` trong tệp **= đúng tập** bản ghi trên màn sau lọc |
| **Không đạt** | Số dòng **= N** (hoặc ≫ M), hoặc tệp chứa `Mã KH` không có trên màn sau lọc |

### C2 — tệp xuất có đủ trường Người tạo / Ngày tạo *(đo hiện trạng để trả lời BA — KHÔNG ra verdict)*

| | Nội dung |
|---|---|
| **Đường UI thật** | Dùng lại **chính tệp đã tải ở C1** (cùng một lần bấm `Xuất Excel` — không bấm lại, luật khóa 3) |
| **Đối chứng độc lập** | `openpyxl`: in **nguyên văn hàng 1** (toàn bộ ô, kể cả ô rỗng) + `max_column` + tên sheet |
| **Ghi vào kết quả** | Danh sách cột nguyên văn + số cột. Kèm quan sát phụ **cùng màn, không thao tác thêm**: bảng trên màn có/không hiển thị cột `Người tạo`, `Ngày tạo` (cuộn ngang bảng — bảng có scroll ngang, xem frame `t003.03s.jpg`) |

> 📌 **Quan sát phụ ở C2 đi qua gate "bug mới phát sinh trong lúc verify", KHÔNG đổi quan hệ GAP của C2.** Nếu **bảng trên màn** cũng thiếu `Người tạo`/`Ngày tạo` thì đó là vi phạm SRS **nói rõ** (`srs-fr-03-dao-tao.md:1795-1796`, đặc tả bảng màn hình) → log **bug mới riêng**, tra trùng trước. Không được nhập nó vào C2 và không được dùng nó để Reopen bug gốc.

### Ghi chú kỹ thuật — lấy tệp về khi Chrome chạy `--isolated`

Chrome do MCP mở ở chế độ `--isolated` **có thể KHÔNG đổ tệp về `~/Downloads`**. Theo thứ tự:

- **(a) Kiểm `~/Downloads` trước.** `ls -lt ~/Downloads/ke-hoach-dao-tao-*.xlsx | head` ngay sau khi bấm. Có tệp (mtime khớp thời điểm bấm) → copy vào `.../F5-flow04-2026-08-07/seed-files/` rồi đọc bằng `openpyxl`. Đối chiếu epoch trong tên tệp với thời điểm bấm để chắc **không nhặt nhầm tệp cũ**.
- **(b) Không có tệp → giải nén zip `.xlsx` ngay trong trang** qua `evaluate_script`: fetch blob/URL tải về → parse **EOCD** → lấy entry `xl/worksheets/sheet1.xml` + `xl/sharedStrings.xml` → giải nén bằng `DecompressionStream('deflate-raw')` → parse XML.
  🔴 **CHỈ `return` hàng tiêu đề (mảng chuỗi) + số dòng dữ liệu + số cột.** **CẤM trả base64 hoặc dump toàn bộ XML** (đốt token, và không phải thứ cần đo).
  ⚠️ Nếu đi đường (b) thì **giữ lại chuỗi base64 xuống đĩa qua bước riêng** hoặc ghi manifest, vì FLOW 04 yêu cầu *"verdict phụ thuộc file thì phải giữ lại chính file hoặc manifest có thể truy lại nội dung"*.

---

## 7. Tiền đề tối thiểu

**Ưu tiên dùng lại dữ liệu QA sẵn có** (FLOW 04 Giai đoạn B §3): env `18.143.165.120.nip.io` ngày 04/08 đã có **15 bản ghi** kế hoạch đào tạo (tệp `v2-00-khong-loc.xlsx`), thừa sức lọc phân biệt. **Không cần seed mới**, trừ khi đếm lại thấy tổng < 3 bản ghi.

### Bộ lọc đề xuất (theo thứ tự ưu tiên)

| Ưu tiên | Bộ lọc | Vì sao chọn |
|---|---|---|
| **A (chính)** | **Lọc `Trạng thái`** — chọn đúng **một** nhãn có ít bản ghi nhất mà vẫn ≥1 (vd `Đã duyệt` hoặc `Từ chối`; số trên badge tab đã hiện sẵn) | Là bộ lọc **SRS liệt kê tường minh** ở `srs-fr-03-dao-tao.md:1781` ⇒ chấm C1 neo được vào đúng bộ lọc mà đặc tả công nhận |
| **B (phụ, tái hiện đúng đối tác)** | **`Từ ngày` = 01/07/2026 · `Đến ngày` = 31/07/2026** | Đúng neo trong video đối tác (`t003.03s.jpg`) ⇒ loại trừ khả năng lỗi chỉ xảy ra với riêng bộ lọc ngày |
| **C (dự phòng)** | **Ô từ khóa** *"Tìm theo tên kế hoạch"* với một chuỗi khớp ít bản ghi | `srs-fr-03-dao-tao.md:1779` |

### Điều kiện bắt buộc của phép đo

🔴 **Phải ghi cả hai số: `N` = tổng bản ghi khi KHÔNG lọc, `M` = số kết quả sau lọc. Bắt buộc `M < N`.**

Nếu `M = N` thì tệp xuất "toàn bộ" và tệp xuất "theo lọc" **cho ra cùng một kết quả** ⇒ phép đo **không phân biệt được gì** ⇒ vô nghĩa, phải đổi bộ lọc. Lý tưởng `M ≤ N/3`.

⚠️ **Cẩn thận với `Lọc Đơn vị`:** `srs-fr-03-dao-tao.md:1782` cho TW quyền lọc đa đơn vị. Tài khoản `cbnv_tw_02` là TW nên mặc định thấy phạm vi rộng — đây là điều **tốt** cho phép đo (N lớn), nhưng đừng nhầm phạm vi quyền với kết quả lọc.

⚠️ **Phân trang:** `Outputs — Danh sách` có trường `total_count` (`:1200`) và mặc định 20/trang (`:1130`). Số cần lấy là **`N`/`M` ở chân bảng ("… / N kết quả")**, **không phải** số dòng đang nhìn thấy trên trang 1. Tệp xuất phải chứa **toàn bộ M**, không phải chỉ 20 dòng của trang hiện tại.

---

## 8. Bẫy chặn FAIL oan / PASS oan

| # | Bẫy | Cách chặn |
|---|---|---|
| **(a)** | **`M = N` → phép đo vô nghĩa.** Lọc ra đúng bằng tổng thì tệp "toàn bộ" và tệp "theo lọc" trùng nhau, PASS/FAIL đều không có căn cứ. | Bắt buộc chọn bộ lọc cho `M < N` (§7). Ghi cả `N` và `M` vào báo cáo. Nếu lỡ đo với `M = N` → **kết quả không dùng được**, đo lại. |
| **(b)** | **Tệp mở được ≠ nội dung đúng.** HTTP 200, toast *"Xuất Excel thành công"*, tệp `.xlsx` hợp lệ — **không** cái nào chứng minh dữ liệu bên trong đúng bộ lọc. (Đây đúng là điều video vòng 1 phơi ra: toast báo thành công, tệp mở ngon, nhưng 12 dòng thay vì 2.) | **Bắt buộc `openpyxl`**: đếm dòng dữ liệu **và** đối chiếu tập `Mã KH` với màn. Không được chốt bằng screenshot/toast/kích thước tệp. |
| **(c)** | **Tên cột có thể là từ đồng nghĩa.** `Người lập` · `Ngày lập` · `Thời điểm tạo` · `Cán bộ tạo` · `Ngày khởi tạo` đều có thể là hiện thân của yêu cầu TKM. | So theo **NỘI DUNG / ý nghĩa cột**, không so chuỗi cứng. In **nguyên văn toàn bộ hàng 1** rồi đọc thủ công, và đọc thêm 1-2 dòng dữ liệu để xác định cột đó chứa **họ tên người** / **ngày** thật. Đồng thời đối chiếu với đúng danh mục cột SRS quy định — ở đây là `srs-fr-03-dao-tao.md:1795-1796` dùng chính xác chữ **`Người tạo`** và **`Ngày tạo`**. |
| **(d)** | **Đổi C2 từ GAP sang MATCH vì web tình cờ làm đúng kỳ vọng đối tác.** | **CẤM.** Luật khóa 5 FLOW 04: kết quả web không đổi được quan hệ đã khóa. Chỉ được đổi khi **dẫn ra dòng SRS mới đọc được** quy định danh mục cột tệp xuất. Lý do kiểu *"web đã làm đúng expected"* / *"coi như đã đáp ứng"* **không** hợp lệ. Web đúng → ghi `WEB HIỆN TẠI: đúng kỳ vọng đối tác` + câu hỏi BA chuyển mục đích thành **bổ sung vào đặc tả** (§5.3). |
| **(e)** | **Dùng verdict `Closed` ngày 04/08 để Pass vòng này.** | **CẤM** (FLOW 04). Bản dựng nay là V1.0.10, khác bản đo 03-04/08. Hồ sơ cũ + 11 fixture ở §4 chỉ là **tham chiếu**. C1 **phải đo lại từ đầu** trong vòng này. |
| **(f)** | **Nhặt nhầm tệp cũ trong `~/Downloads`.** Thư mục đã có nhiều `ke-hoach-dao-tao-*.xlsx` từ các vòng trước. | Đối chiếu **epoch ms trong tên tệp** với thời điểm bấm nút (epoch → giờ thật, xem §3.1). Sắp xếp theo `mtime` và xác nhận lệch < 1 phút. |
| **(g)** | **Kết luận theo ảnh v2 của đối tác.** Ảnh v2 không có cửa sổ trình duyệt ⇒ không biết bộ lọc, không biết số kết quả trên màn. | Ảnh v2 **chỉ** dùng để xác định vế C2 (danh mục cột) và làm neo tái hiện. **Không** dùng để chấm C1. |
| **(h)** | **Trộn hai môi trường.** Đối tác đo trên `htpldn-uat.ospgroup.vn`, ta đo trên `18.143.165.120.nip.io`. | Chỉ so quan hệ `màn ↔ tệp` **trong cùng một lần đo trên cùng env**. Cấm so số bản ghi tuyệt đối giữa hai env. Verdict ghi rõ chỉ có hiệu lực cho env + thời điểm đã đo. |
| **(i)** | **Đếm dòng bằng `max_row` thô.** `openpyxl` có thể trả `max_row` lớn hơn thực tế do ô đã format/từng có dữ liệu. | Duyệt ngược từ cuối, bỏ các dòng toàn `None`/rỗng, rồi mới lấy số dòng dữ liệu. Đối chiếu chéo bằng **đếm số `Mã KH` khác rỗng**. |

---

## 9. Điều còn thiếu / câu hỏi cho điều phối

| # | Vấn đề | Ảnh hưởng | Đề xuất |
|---|---|---|---|
| 1 | **C2 là `GAP` ⇒ theo FLOW 04, case này chắc chắn có phần "Cần BA"**, kể cả khi C1 đo ra đạt. Verdict logic khả dĩ: **`Cần BA`** (nếu C1 đạt) hoặc **`Reopen + cần BA`** (nếu C1 vẫn lỗi). **Không có nhánh nào ra `Pass` thuần.** | Quyết định cách ghi lên bảng đối tác | Cần điều phối xác nhận quy ước ghi đa-trạng thái cho dòng 20 (tham chiếu quy ước *"Open, BA confirm"* đã dùng ở các đợt trước) |
| 2 | **DEV phản hồi lần 1 để trống** — không biết dev đã sửa cái gì. | Không suy được "fix có tác dụng hay không" | Theo FLOW 04 §Ca biên: chỉ kết luận **hiện trạng đúng/sai so với đặc tả**, **không** viết *"fix đã có tác dụng"*. Nếu lấy được ghi chú fix của dev thì tốt, không có vẫn chạy được. |
| 3 | **Bản dựng V1.0.10** — video đối tác cho thấy footer app ghi `HTPLDN · V1.0`. Cần định danh bản dựng thật tại thời điểm đo. | Ràng buộc hiệu lực verdict | Giai đoạn B ghi lại chuỗi phiên bản hiển thị ở sidebar/footer + thời điểm đo. |
| 4 | **Quan sát phụ có thể sinh bug mới:** nếu **bảng trên màn** thiếu `Người tạo`/`Ngày tạo` thì đó là vi phạm SRS nói rõ (`:1795-1796`) — khác hẳn C2 (GAP). | Có thể phát sinh 1 bug mới cần nơi lưu + mã | Prompt chưa chỉ định nơi lưu / cách cấp mã cho bug mới. Đề nghị điều phối chốt trước, nếu không Giai đoạn B sẽ đưa đầy đủ nội dung vào report cuối và báo rõ **chưa cập nhật ra ngoài**. |
| 5 | **Cột `Mã KH` và cột `Số chương trình`** đều lệch so với mọi bảng cột trong SRS (§5.3 câu hỏi 2-3). | Có thể mở rộng phạm vi câu hỏi BA | Đã gộp sẵn vào 3 câu hỏi BA ở §5.3 — **không** mở thêm phép đo cho việc này (luật khóa 1: expected đối tác không nhắc). |
| 6 | Tài khoản `cbnv_tw_02` chưa được xác minh còn hoạt động trên env này. | Có thể chặn Giai đoạn B | Nếu login fail → áp Rule 7 (fallback **cùng vai trò + cùng cấp**: `_03`…), **ghi rõ account thực dùng**. Tuyệt đối không đổi sang vai trò/cấp khác (đổi scope dữ liệu → phép đo C1 mất giá trị). |
