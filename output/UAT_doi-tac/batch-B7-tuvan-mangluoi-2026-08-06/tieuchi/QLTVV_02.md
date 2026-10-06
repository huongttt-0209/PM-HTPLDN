# Tiêu chí verify — QLTVV_02

```
Mã case: QLTVV_02 (tab `bug`, dòng 32)          Thời điểm viết: 2026-08-06 15:50
Môi trường verify: https://18.143.165.120.nip.io  (env NỘI BỘ — đối tác đo trên env nghiệm thu khác)
Bản dựng: chuỗi trên màn `HTPLDN · V1.0.8` · gói mã `/assets/index-DIABnbIr.js` + `/assets/index-DVlgOkLg.css`
          · `GET /` → `last-modified: Thu, 06 Aug 2026 07:13:15 GMT`, `etag W/"6a74340b-428"`
          (env dựng lại 14:13 giờ VN 06/08 nhưng GIỮ NGUYÊN chuỗi V1.0.8 ⇒ chuỗi phiên bản không đủ để
           phân biệt bản dựng, phải neo bằng tên gói mã + last-modified)
Đo lúc: 2026-08-06 16:05 → 16:20
```

> **Khai báo hồ sơ QA nội bộ đã đọc trước khi viết mục 4** (bắt buộc theo flow 04 §Giai đoạn A):
> - `output/UAT_doi-tac/reverify-week-2/bug-reports/Pass-bug-report-UAT-tuan-2.md` (dòng 536-573) —
>   entry `BUG-QLTVV_02` **vòng 1**: cột "Loại" hiện mã viết tắt + cột "Điểm ĐG" sai thang /10.
>   Đóng ngày 2026-07-14 (R2).
> - `output/UAT_doi-tac/reverify-week-2/bug-reports/mang-luoi-tvv/Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md`
>   (dòng 46-101) — entry `BUG-QLTVV_02` **vòng 2**: cột Hành động là liên kết chữ thay vì nhóm icon.
>   Đóng ngày 2026-07-29 (R4), có kèm **số đo cũ** ở 1920 / 1440 / 1280 px.
>
> **Mục 4 và mục 5 dưới đây suy TỪ ĐẶC TẢ + kỳ vọng đối tác, KHÔNG lấy số đo cũ làm ngưỡng.**
> Số đo cũ (R4, 29/07, bản dựng khác) chỉ có giá trị **bối cảnh**, không chứng minh gì cho lượt này —
> phải đo lại từ đầu bằng toạ độ thật.

---

## 1. Đối tác phản ánh

Mô tả case: **"Kiểm tra hiển thị bảng danh sách"** — màn *Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia*.

Case này **gộp nhiều vế và đã qua 2 vòng**. Bộ vế phải đo lần này lấy từ ô **"Kết quả verify"** (chữ đối tác
viết ở vòng 2) + 2 vế còn treo trong ô **"Kết quả mong đợi"** mà vòng 1 đối tác ghi là chưa đạt:

| Vế | Nội dung đối tác nêu | Nguồn ô | Trạng thái đặc tả |
|---|---|---|---|
| **(a)** | "Dữ liệu cột Điểm ĐG **bị tràn/đè lên cột Trạng thái**" | Kết quả verify (vòng 2) + TKM phản hồi lần 2 (retest 3/8) | đặc tả **nói rõ** (`:1452`, `:1453`, §C, §F) — khớp kỳ vọng |
| **(b)** | "Dữ liệu cột Điểm ĐG **hiển thị không đồng nhất**: chưa có điểm hiển thị `-/5` nhưng có điểm hiển thị số sao" | Kết quả verify (vòng 2) | đặc tả **tự mâu thuẫn** (Loại UI = "số + sao" vs ví dụ ca chưa có điểm chỉ ghi `—/5`) ⇒ **cần BA** |
| **(c)** | "Các nút thao tác **Xem, Sửa bị xuống dòng**" | Kết quả verify (vòng 2) | đặc tả **nói rõ** (`:1455`, Phụ lục E §H6) — khớp kỳ vọng |
| **(d)** | "Mặc định: hệ thống **sắp xếp theo ngày công nhận mới nhất trước**" (vòng 1 ghi thực tế: không sắp xếp) | Kết quả mong đợi + Kết quả thực tế (vòng 1) | đặc tả **IM LẶNG** ⇒ **cần BA** |
| **(e)** | "**20 bản ghi mỗi trang**" | Kết quả mong đợi | đặc tả **nói rõ** (`:1457`, `:247`, BR-DATA-07) — khớp kỳ vọng |

### Bằng chứng đã xem

**① `partner-evidence/QLTVV_02_v2.png`** — ảnh tĩnh 1906×1034, 305.550 byte, tải về từ ô **"Ảnh/video verify"**
(cột U dòng 32) bằng `tools/fetch_evidence.py`. **Đây là bằng chứng của đúng bộ vế (a)(b)(c) lần này.**
Đã mở full-res. Đọc được trên ảnh:

- Thanh địa chỉ: `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach` — **env nghiệm thu của đối tác**.
- Góc phải: `BTP · TW` · avatar `CU` · **"Cán bộ NV Trung ương  CB_NV_TW"** · chuông `99+`.
- Chân thanh bên trái: **"HTPLDN · V1.0"**. Đồng hồ máy: **11:28 AM 2026-07-25**.
- Tab đang mở: **"Đang hoạt động"**; các tab khác: Tạm dừng · Mới đăng ký `26` · Chờ thẩm định ·
  Yêu cầu bổ sung `2` · Đang thẩm định · Chờ phê duyệt · Chờ kích hoạt tài khoản · Từ chối · `…`
- Chân bảng: **"1-10 / 10 mục"**, ô trang `1`, ô chọn **"20 / trang"**.
- Cột hiện có: Họ tên · Loại · Lĩnh vực · Tổ chức · **Điểm ĐG** · **Trạng thái** · Ngày công nh… ·
  Công khai · **Hành động**. Bảng đang **cuộn ngang** (cột Mã TVV đã bị đẩy khuất, có thanh cuộn ngang
  dưới bảng) ⇒ bảng rộng hơn khung chứa ở bề rộng đối tác dùng.
- **Vế (a):** khung đỏ số 1 bao 2 hàng — `TVV R12 A18 UI Walk` hiện `★★★☆ 3.7/5` và `TVV R11 Verify Mail Fix`
  hiện `★★★★★ 8.3/5`. Chuỗi `3.7/5` và `8.3/5` **nằm chồng lên chữ "Đang hoạt động"** của cột Trạng thái
  (đọc thấy chữ số và chữ "Đang hoạt" chèn vào nhau) ⇒ đúng triệu chứng tràn/đè.
- **Vế (b):** 3 hàng chưa có điểm (`Nguyễn TVV An Giang 01`, `TVV R13 A19 Gate Verify`, `huongcg`) hiện
  **`—/5` không kèm sao nào**; 2 hàng có điểm hiện **sao + số**. Hai ca hiển thị khác kiểu nhau.
- **Vế (c):** khung đỏ số 2 bao cột Hành động — chữ **"Xe m"** và **"Sử a"** bị **ngắt làm 2 dòng**,
  chữ "Xóa" đỏ nằm tràn ra ngoài khung. ⇒ cột Hành động **vẫn là nhãn chữ**, và chữ bị xuống dòng.
- Ghi nhận thêm (**đối tác KHÔNG nêu**): giá trị **`8.3/5`** — điểm 8.3 trên thang tối đa 5.

**② `partner-evidence/QLTVV_02.webm`** — video 21,4 giây, 4.656.907 byte, ô **"Ảnh/vieo 1"** (vòng 1).
Đã trích 8 frame (mỗi 3 giây) và xem full-res 1920×1080. Nội dung: đồng hồ máy **01:59 PM 2026-07-07**,
cùng màn `htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach?page=1&pageSize=20`, cùng vai trò
`Cán bộ NV Trung ương CB_NV_TW`; frame 0-6 s soi cột **Điểm ĐG** (hàng `TVV R11 Verify Mail Fix` hiện
`★ 8.3`, các hàng khác hiện `—`), frame 9-21 s chuyển sang cửa sổ **Word** mở tài liệu thiết kế
`7.BTP_CPLQG_S7_2025_PM_L4_PMHTPLDN.docx` trang 254, bôi đen đúng ô *"Điểm đánh giá trung bình thang 1–5;
định dạng "x.x/5" kèm 5 sao trực quan. Hiển thị "/5" khi tư vấn viên chưa có đánh giá."*

**Kiểm bằng chứng có đúng case này không:** ✅ cả 2 tệp đều đúng màn + đúng vai trò + đúng mã case.
⚠️ Nhưng **video là bằng chứng VÒNG 1** (07/07, nói về thang điểm /10 và mã viết tắt — đã đóng ở
`Pass-bug-report-UAT-tuan-2.md`), **không** chứa vế (a)(b)(c) của vòng này. Bằng chứng quyết định cho
lượt đo này là ảnh `QLTVV_02_v2.png` (25/07).

## 2. Đặc tả nói gì

Nguồn: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` (bản chốt duy nhất).

**a) Bảng "Thành phần màn hình" của SCR-IV-01 — `srs-fr-04-chuyen-gia-tvv.md`, mở file đọc từng dòng:**

- `:1452` → `| 24 | bảng | Điểm đánh giá | số + sao | Ví dụ: "4.5/5" + 5 sao. Nếu chưa có đánh giá: hiển thị "—/5" | — |`
- `:1453` → `| 25 | bảng | Trạng thái | badge | Theo bảng ánh xạ § 3.0 | — |`
- `:1454` → `| 26 | bảng | Ngày công nhận | cột (định dạng ngày) | dd/mm/yyyy; nếu chưa có: "—" | — |`
- `:1455` → `| 27 | bảng | Hành động | nhóm icon | Icon Xem (mắt) → SCR-IV-03; Icon Sửa (bút chì) → SCR-IV-02 (ẩn nếu trạng thái Vô hiệu hóa); Icon Xóa (thùng rác) — chỉ khi không có vụ việc đang xử lý, mở MD-XOA xác nhận | — |`
- `:1457` → `| 29 | phân trang | Phân trang | pagination | 20 mục/trang; hiển thị tổng mỗi tab | — |`

Bảng này liệt kê **đóng** 27 thành phần, mỗi thành phần một ô riêng trong cùng một hàng bảng dữ liệu.

**b) Điểm đánh giá — quy định thang và ca rỗng:**

- `:2538` (BR-CALC-06) → *"…Thang **1–5**, làm tròn **1 chữ số thập phân** (round-half-up). Nếu chưa có
  đánh giá → `NULL`, hiển thị "—/5" (không hiển thị "0")."*
- `:958` (FR-IV-CROSS-01, bảng lỗi E1) → *"Chưa có đánh giá | INF-TVV-DG-01 | "Chưa có đánh giá" —
  hiển thị "—/5" thay vì 0 | INFO"*
- `:962` (AC) → *"**Given** TVV chưa có đánh giá **When** hiển thị **Then** "—/5" (không hiển thị 0)"*
- `:2035` (Entity TU_VAN_VIEN) → `diem_danh_gia_tb … DECIMAL(3,1), CHECK BETWEEN 1.0 AND 5.0`

**c) Phân trang:**

- `:247` (FR-IV-02 §Processing bước 3) → *"Phân trang (mặc định 20/trang) | BR-DATA-07"*
- `srs-fr-05-vu-viec.md:2394` (BR-DATA-07) → *"Mọi danh sách sử dụng phân trang. Default: 20 rows/page,
  max: 100 rows/page."*

**d) Quy ước UI dùng chung — `srs-v3.5.md` Phụ lục E §H:**

- `:6714` (**H6**) → *"Cột Hành động dạng icon + tooltip BẮT BUỘC | Cột Hành động trong mọi bảng dùng icon
  (Mắt = Xem, Bút = Sửa, Thùng rác = Xóa, …) **thay cho nhãn text**. **Mỗi icon BẮT BUỘC có `aria-label`
  và tooltip hover**… | BẮT BUỘC"*
- `:6718` → *"Các FR/SCR có quy ước UI riêng phải cross-ref về Phụ lục E §H…"*

**e) Quy ước chung về trình bày bảng — `srs-fr-05-vu-viec.md` §3.C và §3.F** (Phụ lục E §A–G ghi rõ khối
này **áp cho toàn hệ thống**, hiện còn để tại srs-fr-05 chờ di chuyển — `srs-v3.5.md:6696`):

- `:1568-1573` (§C Quy ước cắt nội dung dài) → *"Áp dụng cho mọi cột text trong bảng: Cột tên / tiêu đề
  > 30 ký tự: **cắt + dấu `...` cuối + tooltip** hover hiển thị nội dung đầy đủ…"* ⇒ cách xử lý nội dung
  vượt chỗ mà đặc tả chọn là **cắt trong ô**, không có chỗ nào cho phép nội dung tràn sang ô khác.
- `:1601-1603` (§F Thiết kế responsive) → *"**Phía cán bộ (CMS)…: tối thiểu hỗ trợ máy tính bảng
  1024×768**. Không bắt buộc mobile."*

### IM LẶNG về

- **Thứ tự sắp xếp mặc định của SCR-IV-01.** Đã grep toàn bộ `srs-fr-04-chuyen-gia-tvv.md` với
  `sắp xếp` / `sort` / `ORDER BY` / `DESC` / `mới nhất trước` → **0 kết quả**. FR-IV-02 §Processing
  (`:243-:247`) chỉ có "kiểm quyền → kết hợp điều kiện AND → phân trang", không có bước sắp xếp.
  BR-DATA-07 (`srs-fr-05:2392-2394`) chỉ nói phân trang, không nói thứ tự. (Đối chiếu: các nhóm khác
  **có** quy định — `srs-fr-08-danh-gia.md:904`, `srs-fr-12-tv-chuyen-sau.md:1132`,
  `srs-fr-05-vu-viec.md:1665` — càng cho thấy nhóm IV bỏ trống chứ không phải nằm ở chỗ khác.)
- **Có hay không 5 sao ở ca "chưa có đánh giá".** `:1452` khai Loại UI của cột là **"số + sao"** (ngụ ý
  cột luôn có phần sao) nhưng chính dòng đó, ở ca chưa có đánh giá, chỉ ghi `"—/5"` và **không nhắc sao**;
  `:958`, `:962`, `:2538` cũng chỉ ghi `"—/5"`. Hai vế trong **cùng một ô đặc tả** không chốt được ca rỗng
  có sao hay không ⇒ đây là **tự mâu thuẫn**, không phải im lặng hoàn toàn.
- **Ngưỡng bề rộng cửa sổ tối thiểu ngoài 1024×768** — không có.

## 3. Precondition

- Tài khoản: **`cbnv_tw_02`** / `Test@1234` — vai trò **CB_NV_TW** (Cán bộ Nghiệp vụ Trung ương), cấp **TW**.
  Đúng vai trò + cấp đọc được trên ảnh đối tác (`Cán bộ NV Trung ương  CB_NV_TW`, `BTP · TW`).
  Theo `:1420` vai trò Cán bộ Nghiệp vụ có "thêm/sửa/xóa, xuất Excel, công khai (TVV thuộc đơn vị)".
  Không dùng tài khoản quản trị để ra verdict.
- Màn: **`/chuyen-gia-tvv/danh-sach`**, tab **"Đang hoạt động"** (tab mặc định, đúng tab trong ảnh đối tác).
- Dữ liệu tiền đề: danh sách phải có **đồng thời** ≥1 tư vấn viên **đã có điểm đánh giá** và ≥1 tư vấn viên
  **chưa có điểm** trong cùng một trang — nếu env thiếu ca "đã có điểm" thì **phải seed** (đặc tả `:951`:
  điểm TB sinh từ DANH_GIA_SAU_VU_VIEC).
- Bề rộng cửa sổ: đo tối thiểu **1440×900** (chuẩn dự án) và **1280** (bề rộng hay lộ tràn); thêm bề rộng
  suy từ bằng chứng đối tác (ảnh 1906 px ⇒ cửa sổ ~1920) và **1024** (ngưỡng tối thiểu đặc tả §F).

## 4. Tiêu chí chấm

> Rẽ nhánh **từng vế**. Vế (b) và (d) đi nhánh **cần BA** — vẫn đo, nhưng **không chấm**.

**✅ PASS vế (a) — không tràn/đè — khi ĐỦ cả 3:**

1. Trên **mọi** hàng của trang 1, ở **mọi** bề rộng đã đo: hình chữ nhật thật (`getBoundingClientRect`) của
   ô cột **Điểm đánh giá** và ô cột **Trạng thái** **không chồng lấn** — `right(Điểm ĐG) ≤ left(Trạng thái)`,
   sai số cho phép 0 px. Chồng lấn > 0 px = có tràn.
2. Nội dung bên trong ô Điểm đánh giá **không vượt khỏi ô**: phần tử con trong ô có
   `right ≤ right(ô) + 0px` và ô không ở tình trạng `scrollWidth > clientWidth` mà vẫn để nội dung hiện ra
   ngoài (nếu vượt thì phải **cắt / ẩn** theo §C, không được hiện đè).
3. Chữ của cột Trạng thái đọc được nguyên vẹn trên ảnh chụp (không bị ký tự cột khác chèn lên).

**❌ FAIL vế (a) nếu:** ≥1 hàng ở ≥1 bề rộng có chồng lấn > 0 px, **hoặc** nội dung ô Điểm đánh giá vượt
ra ngoài mép phải của ô mà không bị cắt.

**✅ PASS vế (c) — nút thao tác không xuống dòng — khi ĐỦ cả 3:**

1. Ô cột **Hành động** của **mọi** hàng trang 1, ở **mọi** bề rộng đã đo: các điều khiển trong ô **cùng
   nằm trên một dòng** — chênh lệch `top` giữa các điều khiển trong cùng ô ≤ 2 px.
2. Chiều cao thật của cụm điều khiển (`offsetHeight` của phần tử bọc) **không lớn hơn 1,5 lần** chiều cao
   của một điều khiển đơn trong chính ô đó (ngưỡng suy từ định nghĩa "xuống dòng": 2 dòng ⇒ ≥ 2×).
3. Nhãn của từng điều khiển **không bị ngắt giữa chữ** (không có hàng nào cho ra chữ kiểu `"Xe\nm"`);
   đo bằng số hàng dòng thật của phần tử nhãn (`getClientRects().length` = 1).

**❌ FAIL vế (c) nếu:** ≥1 ô Hành động ở ≥1 bề rộng có điều khiển lệch `top` > 2 px, **hoặc** nhãn của
điều khiển trải trên > 1 hàng dòng.

**✅ PASS vế (e) — 20 bản ghi mỗi trang — khi ĐỦ cả 2:**

1. Bộ chọn số dòng mỗi trang ở chân bảng **mặc định là 20** khi vào màn lần đầu (không tự đổi tay).
2. Nếu tổng số bản ghi của tab ≥ 21: trang 1 hiển thị **đúng 20 hàng** (`.ant-table-tbody tr.ant-table-row`,
   **đếm thô**, không lọc) và có ≥ 2 trang. Nếu tổng < 21: chỉ chứng minh được **vế mặc định 20**; phải ghi
   rõ **không đủ dữ liệu** để chứng minh việc cắt trang và nêu cần seed thêm bao nhiêu bản ghi.

**❌ FAIL vế (e) nếu:** bộ chọn mặc định khác 20, hoặc tổng ≥ 21 mà trang 1 có số hàng ≠ 20.

**→ cần BA vế (b)** vì đặc tả **tự mâu thuẫn** giữa "Loại UI = số + sao" (`:1452` cột Loại UI) và ví dụ ca
chưa có đánh giá chỉ ghi `"—/5"` (`:1452`, `:958`, `:962`, `:2538`). Vẫn **đo và ghi nhận hiện trạng**:
ca chưa có điểm hiển thị gì (có sao không, mấy sao, chữ gì) · ca có điểm hiển thị gì · có đúng thang 1–5
và 1 chữ số thập phân không. **Không chấm Pass/Fail vế này.**
*Ngoại lệ theo flow §Nhánh cần BA:* nếu đo xong thấy bản dựng đang hiển thị **đồng nhất đúng như đối tác
mong đợi** thì hết bất đồng ⇒ bỏ khỏi danh sách hỏi BA, chỉ ghi nhận.

**→ cần BA vế (d)** vì đặc tả **IM LẶNG** về thứ tự sắp xếp mặc định của SCR-IV-01. Vẫn **đo và ghi nhận**:
đọc cột "Ngày công nhận" của **toàn bộ** hàng trang 1 (không nhìn 2-3 hàng đầu), kiểm dãy có giảm dần thật
không; nếu cột này không đủ để kết luận thì đối chiếu thêm thứ tự trả về của lời gọi danh sách.
**Không chấm Pass/Fail vế này.** *Ngoại lệ như trên:* nếu dãy ngày công nhận giảm dần đúng như đối tác mong
đợi ⇒ hết bất đồng, bỏ khỏi danh sách hỏi BA.

### KHÔNG được chấm Fail vì

- **Cột Hành động là chữ hay là icon** — đó là nội dung của bug vòng 2 **đã đóng** ngày 29/07
  (`Pass-bug-report-tuan-2-r2-mang-luoi-tvv.md`), không thuộc bộ vế lần này. Nếu phát hiện tái phát thì
  báo riêng, **không** kéo verdict case.
- **Giá trị điểm nằm ngoài thang 1–5** (vd `8.3/5` trên ảnh đối tác) — đối tác **không nêu** ở vòng này;
  gặp thì xử theo flow §Ca biên (log riêng / đưa vào file hỏi BA), **không** kéo verdict case.
- **Bề rộng < 1024 px** — đặc tả §F chỉ cam kết tối thiểu 1024×768 cho màn phía cán bộ.
- **Thứ tự các cột, màu badge, số cột hiển thị** — không thuộc vế đối tác nêu lần này.

## 5. Dạng dữ liệu phải phủ — **M = 4**

Bug này là bug về **cột hiển thị dữ liệu**, nên M bắt buộc ≥ 2. Liệt kê:

| # | Dạng | Vì sao là một dạng riêng | Vế nào cần |
|---|---|---|---|
| **D1** | Tư vấn viên **chưa có đánh giá** (`diem_danh_gia_tb = NULL`) | `:2538` + `:958` quy định riêng cách hiển thị ca này (`"—/5"`) | (a) (b) |
| **D2** | Tư vấn viên **đã có đánh giá** (giá trị trong 1.0–5.0) | `:1452` quy định riêng ca này (`"x.x/5"` + 5 sao); độ dài chuỗi khác D1 nên rủi ro tràn khác | (a) (b) |
| **D3** | Hàng có ô Hành động **đủ 3 điều khiển** (Xem / Sửa / Xóa) | `:1455` — ca ô Hành động rộng nhất, dễ xuống dòng nhất | (c) |
| **D4** | Hàng có ô Hành động **bị ẩn bớt điều khiển** (trạng thái *Vô hiệu hóa* → ẩn Sửa theo `:1455`) | ô hẹp hơn D3 ⇒ hành vi bọc dòng khác; cũng là ca đặc tả nói rõ | (c) |

**Nguồn xác định M:** ① đặc tả mục nói về nguồn dữ liệu — `:951` (điểm TB tính từ DANH_GIA_SAU_VU_VIEC,
chưa có đánh giá → NULL) và `:1455` (điều kiện ẩn icon Sửa theo trạng thái); ② bộ lọc + giá trị enum ngay
trên màn — 9 tab trạng thái + dropdown "Trạng thái" 10 giá trị theo § 3.0.

**Nếu env thiếu dạng nào → SEED** (flow cấm ra verdict khi tiền đề tạo được mà không tạo). Ghi rõ đã đổi
bản ghi nào, đổi gì, trên env nào.

**Độ phủ bề rộng — 4 mốc** (mỗi mốc đo lại toàn bộ hàng trang 1): **1920** (suy từ ảnh đối tác 1906 px) ·
**1440** (chuẩn dự án) · **1280** · **1024** (ngưỡng tối thiểu §F `srs-fr-05:1601`).

## 6. Bảng điều kiện

| Điều kiện có thể đổi kết quả | Đối tác | Mình test lần này | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | `CB_NV_TW` — badge "Cán bộ NV Trung ương  CB_NV_TW", `BTP · TW` | **`cbnv_tw_02`** — badge trên màn "CB Nghiệp vụ - Trung ương #02 / **Cán bộ Nghiệp vụ Trung ương**", `BTP · TW`, đơn vị *Cục Bổ trợ tư pháp - Bộ Tư pháp*. **Không nới chiều nào** (đúng vai trò + đúng cấp + đơn vị chứa toàn bộ TVV) | **Không** |
| Entity + trạng thái | Tab "Đang hoạt động"; 5 hàng đọc được đều `Đang hoạt động`; cột Công khai có cả `Công khai` và `Chưa công kh…` | Tab "Đang hoạt động" (6/6 hàng `Đang hoạt động`) — đo chính. Đo thêm 3 tab để phủ dạng ô Hành động: "Mới đăng ký" (7), "Yêu cầu bổ sung" (6), "Vô hiệu hóa" (1). Cột Công khai có cả `Công khai` (3) và `Chưa công khai` (3) | **Không** |
| Dữ liệu tiền đề | 10 bản ghi trong tab; **3 hàng chưa có điểm** (`—/5`) + **2 hàng có điểm** (`3.7/5`, `8.3/5`) | 6 bản ghi trong tab; **4 hàng chưa có điểm** (`—/5`) + **2 hàng có điểm** (`4.1/5`, `3.3/5`) ⇒ đủ cả D1 và D2. Dạng D4 (ô Hành động bị ẩn bớt điều khiển) **không có sẵn → đã seed**: đổi `CG-QLND38-UAT` sang *Vô hiệu hóa* để đo, rồi **khôi phục** về *Đang hoạt động* | **Không** |
| Input / filter / giá trị nhập | Không lọc gì (đã bấm được nút "Xóa bộ lọc"/"Tìm kiếm" nhưng bảng ghi `1-10 / 10 mục` = toàn bộ tab); ô "… / trang" = **20**; bảng đang **cuộn ngang** | Không lọc (`1-6 / 6 mục` = toàn bộ tab); ô "… / trang" = **20** (không đụng tay, mở bộ chọn thấy 10/20/50/100, đang chọn 20); bảng **cuộn ngang** ở 1024/1280/1440 (`scrollWidth 1530 > clientWidth 889` ở 1024), hết cuộn ở 1920 | **Không** |
| Độ phủ biến thể (N bản ghi, M dạng) | N = 5 hàng nhìn thấy / 10 hàng của tab · M = 2 dạng điểm (có / không) · 1 bề rộng (~1920) | N = **6/6 hàng trang 1, đo hết, không lấy mẫu** × **4 bề rộng** (1920 · 1440 · 1280 · 1024) · M = **4 dạng** (D1 · D2 · D3 ô Hành động 3 điều khiển · D4 ô Hành động 2 điều khiển) | **Không** |

**Ghi chú giới hạn (KHÔNG phải GAP):** cảnh "tổng ≥ 21 bản ghi để thấy trang bị cắt" **không dựng được** — tab
đông nhất chỉ có 7 bản ghi, bộ chọn nhỏ nhất là 10/trang, muốn dựng phải seed thêm **≥14 bản ghi vào cùng một
tab**. Đây **không** là GAP so với đối tác: chính ảnh đối tác cũng chỉ có **10 bản ghi** (`1-10 / 10 mục`) nên
phía đối tác cũng chưa từng chạm cảnh cắt trang. Phần đặc tả nêu ở `:1457` (*"20 mục/trang; hiển thị tổng mỗi
tab"*) đã đo được trực tiếp và đầy đủ.

**3 dữ kiện neo của đối tác:**
`htpldn-uat.ospgroup.vn/chuyen-gia-tvv/danh-sach` tab "Đang hoạt động", 1-10/10 mục, 20/trang ·
5 hàng đọc được đều ở trạng thái `Đang hoạt động` (2 công khai / 3 chưa công khai) ·
vai trò `CB_NV_TW` cấp TW, bản dựng ghi trên màn là **`HTPLDN · V1.0`**, ảnh chụp 11:28 ngày 25/07/2026.

> **Lệch env + lệch bản dựng so với đối tác** (họ đo trên env nghiệm thu `htpldn-uat.ospgroup.vn` bản
> `V1.0`; mình đo trên env nội bộ `18.143.165.120.nip.io` bản ghi ở đầu file) — đây là **giới hạn hiệu lực**
> của verdict, không phải GAP. Mọi kết luận chỉ có hiệu lực cho env + bản dựng đã ghi.
