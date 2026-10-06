# QLLKHDTBD_09 — Audit verify vòng 1 (2026-08-03)

**Sheet:** `1OKBN2otlmdZ44THkmhtsn-_63M2Boh7zQwearwjYR3s` · tab `UAT_TGPL Doanh Nghiệp-tuần 2` · **row 119**
**Verdict QA (cột `Verify`, Q):** `Open`
**Cột `Trạng thái dev fix 1` (P):** `Reject` — QA **KHÔNG đụng**, giữ nguyên của dev.
**Tài khoản QA dùng:** `cbnv_tw` (CB_NV_TW, `BTP · TW`) — **đúng vai trò + cấp của đối tác**. Không dùng `admin` ra verdict.
**Bản dựng test:** `HTPLDN · V1.0.5` (đọc ở sidebar) · env `https://18.143.165.120.nip.io`

---

## Note dev trước khi QA đè (2026-08-03)

Nguyên văn ô `DEV phản hồi lần 1` (cột R) đọc lại từ sheet lúc 2026-08-03 17:00 ngay trước khi ghi:

> KHÔNG phải bug: Xuất Excel dùng chung query builder với danh sách + cap 10.000 dòng (BR-DATA-06) → đã áp đủ điều kiện lọc. "Xuất toàn bộ" không tái hiện (do build cũ / chưa đặt bộ lọc).

Các ô khác của row 119 tại thời điểm đọc:

| Cột | Giá trị |
|---|---|
| C `Tuần` | `Tuần 2` |
| D `Mã TC` | `QLLKHDTBD_09` |
| G `Mô tả` | `Xuất Excel với điều kiện lọc` |
| H `Điều kiện` | `1. Đăng nhập tài khoản` |
| J `Các bước thực hiện` | `1. Chọn menu "Đào tạo, tập huấn" -> "Kế hoạch đào tạo"` / `2. Bấm nút "Gửi phê duyệt"` / `3. Nhập tiêu chí lọc và nhấn Xuất excel` |
| K `Kết quả mong đợi` | `Hệ thống xuất danh sách bài giảng theo điều kiện lọc hiện tại ra tệp Excel.` |
| L `Kết quả thực tế` | `Hệ thống xuất toàn bộ danh sách hiện có trên bảng danh sách` |
| M `Ảnh/vieo 1` | ` QLLKHDTBD_09.webm` |
| N `Trạng thái 1` | `Fail` |
| P `Trạng thái dev fix 1` | `Reject` |
| Q `Verify` | *(TRỐNG — QA điền ở lượt này)* |

### Phản biện từng ý của dev

| Ý dev khai | Kết quả đo được | Kết luận |
|---|---|---|
| *"Xuất Excel dùng chung query builder với danh sách"* | **SAI ở tầng kết quả.** Cùng một bộ lọc, danh sách trả 1 bản ghi (`GET /api/v1/ke-hoach-dao-taos?tuNgay=…&denNgay=…` → màn "Hiển thị 1-1 / 1 kết quả") nhưng tệp xuất trả 13 dòng. Hai đường đi cho ra hai tập dữ liệu khác nhau ⇒ không dùng chung bộ lọc | Bác bỏ |
| *"đã áp đủ điều kiện lọc"* | Yêu cầu xuất **CÓ mang** đủ tham số lọc: `POST /api/v1/ke-hoach-dao-taos/export?tuNgay=2026-07-01&denNgay=2026-07-31&page=1&pageSize=20`. Tức tham số được gửi lên nhưng **không được dùng** khi dựng tệp | Bác bỏ — lỗi nằm ở phía xử lý, không phải ở phía gửi |
| *"'Xuất toàn bộ' không tái hiện (do build cũ / chưa đặt bộ lọc)"* | Tái hiện **2/2 bộ lọc** trên bản dựng mới `V1.0.5`, với bộ lọc **đặt đúng** (địa chỉ trang mang tham số, chân bảng đổi số). Khung hình `t000.00s.jpg` cũng cho thấy đối tác **có** đặt bộ lọc | Bác bỏ cả hai giả định |
| *"cap 10.000 dòng (BR-DATA-06)"* | Đúng phần hạn mức, nhưng BR-DATA-06 (`srs-v3.5.md:5524`) còn có vế **"File xuất theo bộ lọc hiện tại"** — vế đang bị vi phạm | Trích dẫn không đầy đủ |

---

## Cổng 1 — bằng chứng đối tác (đã tự mở xem, không đọc lại kết luận của phiên trước)

Video gốc: `partner-evidence/QLLKHDTBD_09.webm` (4.450.495 bytes, ~14,5 giây). Frame đã mở đọc full-res:

| Frame | Nội dung đọc được từ pixel |
|---|---|
| `frames/QLLKHDTBD_09/dense/t000.00s.jpg` | Địa chỉ trang `htpldn-uat.ospgroup.vn/dao-tao/ke-hoach/danh-sach?tuNgay=2026-07-01&denNgay=2026-07-31&page=1`; ô "Từ ngày" = `01/07/2026`, "Đến ngày" = `31/07/2026`, ô tìm kiếm và "Năm kế hoạch" trống; tab `Tất cả 2`; bảng 2 dòng (`KH-20260725-0001`, `KH-20260723-0001`); chân bảng **"Hiển thị 1-2 / 2 kết quả"**; góc phải "Cán bộ NV Trung ương · CB_NV_TW", "BTP · TW"; đồng hồ máy `10:30 AM 2026-07-25` |
| `frames/QLLKHDTBD_09/dense/t008.20s.jpg` | Toast xanh **"Xuất Excel thành công"** + hộp thoại Save As, tên tệp `ke-hoach-dao-tao-1784950244818.xlsx`; **bộ lọc trên màn vẫn nguyên** `01/07/2026`–`31/07/2026` và vẫn "Hiển thị 1-2 / 2 kết quả" |
| `frames/QLLKHDTBD_09/dense/t014.51s.jpg` — **FRAME LỖI** | Tệp mở bằng Excel (Protected View), sheet `Kế hoạch đào tạo`, header `Mã KH · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Trạng thái`, dữ liệu **dòng 2 → dòng 13 = 12 bản ghi**, gồm nhiều bản ghi nằm hoàn toàn ngoài khoảng lọc (`15/5/2026–30/6/2026`, `31/12/2025–30/12/2026`, `1/1/2026–31/12/2026`) |

**3 dữ kiện neo:**
- (a) Màn/bản ghi: danh sách Kế hoạch đào tạo, địa chỉ trang mang `tuNgay=2026-07-01&denNgay=2026-07-31&page=1`; tệp xuất `ke-hoach-dao-tao-1784950244818.xlsx`.
- (b) Trạng thái entity: tab `Tất cả` (2) — trong đó `Chờ duyệt` 1, `Đã duyệt` 1; **không** lọc theo trạng thái.
- (c) Dữ liệu tiền đề: kho có 12 kế hoạch trải 4 đơn vị và đủ 5 trạng thái; chỉ 2 rơi vào khoảng lọc.

**3 con số bắt buộc rút từ video:** bộ lọc = `Từ ngày 01/07/2026` + `Đến ngày 31/07/2026` (không có ô nào khác) · số bản ghi trên màn sau lọc = **2** · số dòng dữ liệu trong tệp Excel = **12**.

## Cổng 2 — hiểu bug (3 dòng)

1. **Evidence + frame chứa LỖI:** `partner-evidence/QLLKHDTBD_09.webm`, frame `dense/t011.28s.jpg` và `dense/t014.51s.jpg` (giây 11–14,5) — tệp Excel mở ra có 12 dòng dữ liệu trong khi màn danh sách phía sau chỉ có 2 kết quả.
2. **Đối tác phản ánh CỤ THỂ:** không phải sai cột, không phải tệp hỏng — mà **tệp xuất không áp bộ lọc đang đặt trên màn**, xuất trọn danh sách thay vì phần khớp bộ lọc.
3. **Data + bước tái hiện:** đăng nhập CB_NV_TW → `Đào tạo, tập huấn → Kế hoạch đào tạo` → đặt `Từ ngày 01/07/2026`, `Đến ngày 31/07/2026`, các ô khác trống → `Tìm kiếm` → ghi số ở chân bảng → `Xuất Excel` → mở tệp đếm dòng dữ liệu và so.

## Cổng 3 — đối chiếu SRS vs thực tế web

Nguồn SRS **duy nhất**: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`. Đã tự mở file xác nhận số dòng (không lấy từ trí nhớ).

| SRS yêu cầu (file:line, nguyên văn) | Thực tế web (2026-08-03, `V1.0.5`) | Đủ/Thiếu |
|---|---|---|
| `srs-fr-03-dao-tao.md:1067` — *"### FR-III-14: Lập kế hoạch đào tạo năm (UC33)"*; `:1069` — *"**UC Reference:** UC 33 \| **Priority:** Essential \| **Stability:** High"* | Màn `/dao-tao/ke-hoach/danh-sach` đúng là màn của FR này | — (định danh) |
| `srs-fr-03-dao-tao.md:1752` — *"- Nút "Xuất Excel" (phụ): xuất danh sách KH theo bộ lọc, tối đa 10.000 dòng"* | Nút có, bấm được, tệp tạo được — **nhưng nội dung tệp không theo bộ lọc**: màn 1 kết quả → tệp 13 dòng | **Thiếu** |
| `srs-fr-03-dao-tao.md:1147` — heading *"**Processing — Xuất Excel:**"*; `:1152` — *"\| 2 \| Lấy danh sách theo filter, tối đa 10.000 dòng \| BR-DATA-06 \|"* | Bước "lấy danh sách theo filter" không xảy ra: tham số lọc được gửi lên nhưng tệp vẫn chứa trọn kho dữ liệu | **Thiếu** |
| `srs-v3.5.md:5524` — BR-DATA-06 *"**Export Excel:** Mọi danh sách có tính năng xuất Excel. **File xuất theo bộ lọc hiện tại**, không vượt quá 10,000 rows/file"*, phạm vi *"Toàn bộ CRUD list"* | Vế "không vượt 10.000 dòng" đạt; vế **"theo bộ lọc hiện tại"** không đạt | **Thiếu** |
| `srs-fr-03-dao-tao.md:2220` — *"\| BR-DATA-06 \| Export Excel \| FR-III-01, FR-III-05, FR-III-06, FR-III-14 \|"* | Xác nhận BR-DATA-06 áp đúng cho FR-III-14 → không phải suy luận của QA | — (phạm vi) |

> **Giới hạn phạm vi có chủ ý:** danh sách cột bên trong tệp Excel là vùng **SRS không quy định** → case này **không** xét đúng/sai phần cột, định dạng ngày hay thứ tự cột. Chỉ đo đúng một thứ: **số bản ghi trong tệp có khớp bộ lọc đang đặt hay không.**

---

## Phép đo (artifact loại "Filter/search/count")

Bản dựng `HTPLDN · V1.0.5`. Bộ bắt thông báo: `tools/toast-capture.js` (không lọc trùng, đọc `innerText`, tự kiểm `soObserverDangSong = 1` trước mỗi lần đo).

| # | Bộ lọc đặt trên màn | Địa chỉ trang / chuỗi tham số của yêu cầu xuất | Số bản ghi **trên màn** | Số dòng **dữ liệu trong tệp** | Khớp? |
|:-:|---|---|:-:|:-:|:-:|
| 0 | **Không lọc** (mốc đối chứng, trước khi seed) | `POST /api/v1/ke-hoach-dao-taos/export?page=1&pageSize=20` | **12** ("Hiển thị 1-12 / 12 kết quả") | **12** | ✅ khớp |
| A | **Đúng bộ lọc của đối tác:** Từ ngày `01/07/2026`, Đến ngày `31/07/2026`, các ô khác trống, tab Tất cả | `POST /api/v1/ke-hoach-dao-taos/export?tuNgay=2026-07-01&denNgay=2026-07-31&page=1&pageSize=20` | **1** ("Hiển thị 1-1 / 1 kết quả", tab "Tất cả 1") | **13** | ❌ **lệch — bằng đúng tổng kho** |
| B | **Chiều lọc khác:** từ khoá tên kế hoạch `RECON`, ô ngày trống | `POST /api/v1/ke-hoach-dao-taos/export?keyword=RECON&page=1&pageSize=20` | **2** ("Hiển thị 1-2 / 2 kết quả") | **13** | ❌ **lệch — bằng đúng tổng kho** |

**Quan sát then chốt:** chuỗi tham số của yêu cầu xuất **CÓ mang đủ điều kiện lọc** (`tuNgay`, `denNgay`, `keyword`) — tức phía giao diện gửi đúng. Nhưng tệp trả về vẫn là trọn kho 13 bản ghi. Lỗi nằm ở **bước dựng dữ liệu cho tệp**, không phải ở bước gửi tham số. Đây chính là điểm bác bỏ trực tiếp khai báo "dùng chung query builder với danh sách" của dev.

**Nội dung tệp của phép đo A** (đọc bằng `openpyxl`, sheet `Kế hoạch đào tạo`, 13 dòng dữ liệu) — 12/13 dòng nằm **ngoài** khoảng `01/07/2026 – 31/07/2026`:

```
0  Mã KH            | Tên kế hoạch                                | Năm  | Từ ngày    | Đến ngày   | Trạng thái
1  KH-20260803-0003 | QA VERIFY QLLKHDTBD_09 - KHDT trong thang 7 | 2026 | 05/07/2026 | 25/07/2026 | Nháp        ← DUY NHẤT khớp bộ lọc
2  KH-20260803-0002 | RECON 03/08 - KHDT cap BO NGANH …           | 2026 | 01/09/2026 | 31/12/2026 | Chờ duyệt   ← ngoài khoảng
3  KH-20260803-0001 | RECON 03/08 - KHDT cho PDKHDTTH_04 …        | 2026 | 01/09/2026 | 31/12/2026 | Chờ duyệt   ← ngoài khoảng
4  KH-20260731-0003 | CAI_TIEN-002 R2 - KHDT KHONG anh dai dien   | 2026 | 01/11/2026 | 30/11/2026 | Nháp        ← ngoài khoảng
5  KH-20260731-0002 | CAI_TIEN-002 re-verify 31/07 R2 …           | 2026 | 01/10/2026 | 31/10/2026 | Đã công khai← ngoài khoảng
6  KH-20260731-0001 | CAI_TIEN-002 verify 31/07 …                 | 2026 | 01/09/2026 | 30/09/2026 | Nháp        ← ngoài khoảng
7  KHDT-QAW7-01     | QAW7 — Kế hoạch đào tạo 2026                | 2026 | 01/01/2026 | 31/12/2026 | Đã duyệt    ← ngoài khoảng
8  KHDT-2026-001    | Kế hoạch đào tạo PL doanh nghiệp 2026       | 2026 | 01/01/2026 | 31/12/2026 | Đã duyệt    ← ngoài khoảng
9  KH-20260715-0002 | QA Reverify KH no budget 20260715 …         | 2026 | 01/05/2026 | 30/11/2026 | Nháp        ← ngoài khoảng
10 KH-20260714-0001 | QA Reverify KH R2 devfix 20260714           | 2026 | 01/03/2026 | 31/12/2026 | Nháp        ← ngoài khoảng
11 KH-20260712-0002 | QA Reverify KH file 20260712                | 2026 | 01/09/2026 | 30/09/2026 | Nháp        ← ngoài khoảng
12 KH-20260712-0001 | QA Re-verify KH 500 20260712                | 2026 | 01/08/2026 | 31/08/2026 | Nháp        ← ngoài khoảng
13 KHDT-SEED-0001   | Kế hoạch đào tạo seed 2026                  | 2026 | 01/01/2026 | 31/12/2026 | Đã duyệt    ← ngoài khoảng
```

**Nội dung tệp của phép đo B** — 11/13 dòng **không** chứa từ khoá `RECON` (chỉ dòng 2 và 3 chứa).

### Bug candidate ≠ bug — đã đo lại bằng phương pháp thứ hai

| Phương pháp | Cách làm | Kết quả phép đo A |
|---|---|---|
| 1 — đọc tệp ngay trong trình duyệt | `fetch` đúng đường dẫn xuất kèm phiên đăng nhập → lấy `ArrayBuffer` → tự đọc EOCD + central directory → giải nén `xl/worksheets/sheet1.xml` bằng `DecompressionStream('deflate-raw')` → đếm thẻ `<row>` | 14 thẻ `<row>` = **13 dòng dữ liệu** (7.596 bytes) |
| 2 — mở tệp đã tải về bằng công cụ ngoài | Bấm nút `[Xuất Excel]` thật → tệp về `~/Downloads/ke-hoach-dao-tao-1785750930343.xlsx` → đọc bằng `openpyxl` | **13 dòng dữ liệu** (7.596 bytes) |

Hai phương pháp **cùng con số, không mâu thuẫn** → đủ điều kiện log bug.

### Bộ đếm thông báo (bắt buộc theo postmortem 16/07)

| Thao tác | Số yêu cầu gửi máy chủ | Số khung thông báo | Chữ trên khung |
|---|:-:|:-:|---|
| Seed "Thêm mới" kế hoạch | 1 (`POST /api/v1/ke-hoach-dao-taos` → 201) | 1 | "Tạo kế hoạch thành công" |
| Xuất Excel không lọc | 1 | 1 | "Xuất Excel thành công" |
| Xuất Excel bộ lọc A | 1 | 1 | "Xuất Excel thành công" |
| Xuất Excel bộ lọc B | 1 | 1 | "Xuất Excel thành công" |

Không phát hiện thông báo lặp (1 yêu cầu → 1 khung ở mọi thao tác).

---

## Nhiễu môi trường trong phiên đo (ghi nhận, KHÔNG log thành bug)

- Một lần `POST /api/v1/ke-hoach-dao-taos/export?tuNgay=…&denNgay=…` trả **HTTP 502** (thân phản hồi rỗng, `server: Caddy`), giao diện hiện toast **"Xuất Excel thất bại"**. Gọi lại đúng chuỗi tham số đó **2/2 lần đều trả 200** kèm tệp `.xlsx` hợp lệ.
- Ngay sau đó phiên đăng nhập bị **401 hai lần** trong ~10 phút dù mã phiên có `idleTtl = 1800` (30 phút) và thao tác liên tục → phải đăng nhập lại 2 lần.
- **Đánh giá:** cụm 502 + 401 liên tiếp khớp dấu hiệu **máy chủ khởi động lại / triển khai lại giữa phiên**, không tái hiện có quy luật. Theo §C2 "bug candidate ≠ bug", **không** log thành dòng TC mới; ghi lại ở đây để nếu đợt sau gặp lại thì có tiền lệ đối chiếu.
- Một ảnh chụp bị bỏ (`…-05-toast-…`) vì bấm trúng lúc phiên rớt: tên tệp nói "toast" nhưng pixel là màn đăng nhập → **huỷ, không dùng làm bằng chứng** (đúng luật "tên tệp phải khớp nội dung").

---

## Ngoài tiêu chí của case, có thấy gì bất thường không?

Dựa trên các ảnh **đã mở đọc** (`BUG-QLLKHDTBD_09-01/02/04`, `QLLKHDTBD_09-seed-form-truoc-luu`, `QLLKHDTBD_09-seed-sau-luu-13-ket-qua`) và nội dung tệp đã mở:

- **Không phát hiện thêm lỗi nào đủ điều kiện log.** Cụ thể đã soi và loại trừ:
  - Cột trong tệp Excel (`Mã KH · Tên kế hoạch · Năm · Từ ngày · Đến ngày · Ngân sách (VNĐ) · Trạng thái`), định dạng ngày, ô ngân sách trống ở vài dòng — **vùng SRS không quy định** → theo phạm vi case, không log.
  - Không có thông báo lặp ở bất kỳ thao tác nào (bảng đếm ở trên).
  - Nhiễu 502/401 đã phân tích ở mục trên → nhiễu môi trường, không log.

---

## Artifact

| Loại | Đường dẫn |
|---|---|
| Video gốc đối tác | `partner-evidence/QLLKHDTBD_09.webm` |
| Frame baseline (bộ lọc + "1-2 / 2 kết quả") | `frames/QLLKHDTBD_09/dense/t000.00s.jpg` |
| Frame toast + hộp thoại lưu tệp | `frames/QLLKHDTBD_09/dense/t008.20s.jpg` |
| **Frame LỖI — Excel 12 dòng** | `frames/QLLKHDTBD_09/dense/t011.28s.jpg`, `dense/t014.51s.jpg` |
| Ảnh web — baseline không lọc, 12 kết quả | `bug-reports/dao-tao/image/BUG-QLLKHDTBD_09-01-baseline-12-ket-qua.png` |
| Ảnh web — bộ lọc A, 1 kết quả | `bug-reports/dao-tao/image/BUG-QLLKHDTBD_09-02-loc-01-31.07.2026-man-hinh-1-ket-qua.png` |
| Ảnh web — bộ lọc B, 2 kết quả | `bug-reports/dao-tao/image/BUG-QLLKHDTBD_09-04-loc-tu-khoa-RECON-man-hinh-2-ket-qua.png` |
| Ảnh seed — form trước khi lưu | `image/QLLKHDTBD_09-seed-form-truoc-luu.png` |
| Ảnh seed — danh sách sau khi lưu (13 kết quả) | `image/QLLKHDTBD_09-seed-sau-luu-13-ket-qua.png` |
| Tệp Excel — không lọc (12 dòng) | `fixtures/QLLKHDTBD_09/01-khong-loc-12-dong.xlsx` |
| Tệp Excel — bộ lọc A (13 dòng) | `fixtures/QLLKHDTBD_09/02-loc-tungay-01.07-denngay-31.07.2026-man-1-file-13-dong.xlsx` |
| Tệp Excel — bộ lọc B (13 dòng) | `fixtures/QLLKHDTBD_09/03-loc-tukhoa-RECON-man-2-file-13-dong.xlsx` |
| Cổng 1 + Cổng 2 chi tiết (phiên trước, đã tự kiểm lại) | `reverify-audit/QLLKHDTBD_09-evidence.md` |
| Cổng 3 chi tiết (phiên trước, đã tự kiểm lại) | `srs/QLLKHDTBD_09-srs.md` |
| Bảng đối chiếu điều kiện (0 GAP) | `cond/QLLKHDTBD_09.md` |
| Note ghi cột R | `notes/QLLKHDTBD_09.txt` |
| Bug entry | `bug-reports/dao-tao/bug-report-dao-tao.md` → `BUG-QLLKHDTBD_09` |

## Dữ liệu QA để lại trên môi trường

`KH-20260803-0003` — *"QA VERIFY QLLKHDTBD_09 - KHDT trong thang 7-2026"*, `05/07/2026 – 25/07/2026`, trạng thái `Nháp`, đơn vị BTP · TW. Giữ lại để dev re-test bản vá bằng đúng bộ lọc `01/07/2026 – 31/07/2026`.
