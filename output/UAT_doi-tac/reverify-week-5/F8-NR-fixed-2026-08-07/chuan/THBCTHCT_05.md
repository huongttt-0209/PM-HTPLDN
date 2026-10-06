# Chuẩn chấm đã khóa — THBCTHCT_05 (dòng 345) — "Xuất tệp báo cáo tổng hợp (Excel/Word)"

> **Đặc tả — nguồn DUY NHẤT:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-15-ct-htpldn.md`
> (1.610 dòng). Dòng `:1017` **tự nó trỏ tiếp** sang hai chỗ trong cùng thư mục nguồn chuẩn:
> `srs-v3.5.md` **§D.2.4** (khung trình bày TT 17/2025) và **Phụ lục E §H8** (khuôn tên tệp) — đây là **cross-ref
> do chính đặc tả của nhóm XI khai**, không phải nguồn khác. Kiểm chéo `srs-fr-11-bao-cao.md` (nhóm IX) chỉ để
> đối chiếu cách diễn đạt, **không dùng ra verdict cho nhóm XI**.
> **Mọi số dòng dưới đây do agent này tự mở file đếm lại ngày 2026-08-07.**
>
> **Trạng thái phiếu:** đối tác **CHƯA TỪNG CHẠY** (`N/R`, `Kết quả thực tế` RỖNG, không ảnh)
> ⇒ **`expected đối tác` = nguyên văn cột `Kết quả mong đợi` (K)**.
>
> **Điều kiện (H345):** *"1. NSD là cán bộ nghiệp vụ cấp Trung ương và có ít nhất một báo cáo từ Bộ/Ngành hoặc
> Địa phương đã gửi lên. 2. **Đã hoàn thành tổng hợp báo cáo toàn quốc** và NSD là cán bộ nghiệp vụ cấp TW."*

**Expected đối tác (nguyên văn K345):**
```
- Hệ thống tạo tệp tổng hợp theo biểu mẫu Thông tư số 17/2025/TT-BTP — khổ A4, phông chữ Times New Roman
  cỡ 13, đầu trang có quốc hiệu và tên cơ quan, cuối trang có ngày ký và chức danh người ký.
- Đặt tên tệp theo định dạng BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}.xlsx hoặc .docx.
```

---

## 1. BẢNG SCOPE LOCK — 8 vế (mỗi thuộc tính tệp một dòng)

| Vế | Expected đối tác (nguyên văn) | Nguồn đặc tả | Nguyên văn dòng | Quan hệ | Route | Đường đo (mở nội dung tệp) |
|---|---|---|---|---|---|---|
| **C0** | "Hệ thống **tạo tệp tổng hợp** … `.xlsx` **hoặc** `.docx`" | `srs-fr-15-ct-htpldn.md:1017` · `:1006` · `:1175` | `:1006` = `\| 8 \| Xuất file Excel/Word theo mẫu TT17 \| — \|` · `:1175` (trích) = `… [Xuat Excel] [Xuat Word] theo TT17/2025` | **MATCH** | **TEST** | Bấm [Xuất Excel] rồi [Xuất Word] **trên giao diện thật** → thu được tệp mở được đúng định dạng (`openpyxl` đọc `.xlsx`, `python-docx` đọc `.docx`) |
| **C1** | "**khổ A4**" | `srs-v3.5.md:6719` (qua cross-ref `:1017` → §D.2.4) | `:6719` = `- Khổ giấy: A4 (210 × 297mm)` | **MATCH** | **TEST** | `.xlsx`: `ws.page_setup.paperSize` = mã A4 · `.docx`: `section.page_width/page_height` ≈ 21,0 × 29,7 cm |
| **C2** | "**phông chữ Times New Roman cỡ 13**" | `srs-v3.5.md:6720` | `:6720` = `- Phông chữ: Times New Roman, cỡ 13pt` | **MATCH** | **TEST** | `.xlsx`: `cell.font.name` / `cell.font.size` của **các ô thân bảng chỉ tiêu** · `.docx`: font của style `Normal` + của các đoạn thân tệp |
| **C3** | "**đầu trang có quốc hiệu**" | `srs-v3.5.md:6721` | `:6721` = `- Header: Quốc hiệu + Tên cơ quan ban hành` | **MATCH** | **TEST** | Đọc chuỗi ở phần đầu tệp (hàng đầu của sheet / đoạn đầu của văn bản / header trang in) — tìm quốc hiệu |
| **C4** | "**tên cơ quan**" (đầu trang) | `srs-v3.5.md:6721` | *(cùng dòng trên)* | **MATCH** | **TEST** | Cùng đường đo C3 — tìm tên cơ quan ban hành |
| **C5** | "cuối trang có **ngày ký**" | `srs-fr-15-ct-htpldn.md:1017` · `srs-v3.5.md:6722` | `:6722` = `- Footer: Ngày ký + Họ tên cán bộ xuất + chỗ trống cho chữ ký, chức vụ và con dấu (nếu in chính thức)` | **MATCH** | **TEST** | Đọc chuỗi ở phần cuối tệp — tìm mốc ngày ký |
| **C6** | "cuối trang có … **chức danh người ký**" | `srs-fr-15-ct-htpldn.md:1017` · `srs-v3.5.md:6723` | `:1017` (trích) = `**Khối ký cuối trang** theo ngoại lệ §D.2.4: ngày ký + họ tên cán bộ xuất báo cáo + chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức — **không in sẵn dòng chức danh**` | 🔴 **DIFF** | **BA** | **CẤM Pass/Reopen vế này.** Chỉ ghi nhận: cuối tệp **có / không có** dòng chức danh in sẵn |
| **C7** | "Đặt tên tệp theo định dạng **`BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}.xlsx`** hoặc `.docx`" | `srs-fr-15-ct-htpldn.md:1017` · `srs-v3.5.md:6760` (§H8) | `:1017` (trích) = `**Tên tệp** `BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}.{ext}` theo Phụ lục E §H8 `[BA chốt 2026-08-06]`` | 🔴 **DIFF** | **BA** | **CẤM Pass/Reopen vế này.** Chỉ ghi nhận tên tệp thực tế (nguyên văn, kể cả dấu gạch dưới) |
| **C8** | "tạo tệp tổng hợp **theo biểu mẫu Thông tư số 17/2025/TT-BTP**" (phần nội dung) | `srs-fr-15-ct-htpldn.md:1006` · `:1017` · `srs-v3.5.md:6705`,`:6706`,`:6713`,`:6714` | `:6705` = `\| Excel (.xlsx) \| Apache POI \| Template 21a/21b có sẵn, fill data \|` · `:6713` = `\| 1 \| Báo cáo sơ bộ 6 tháng CT HTPLDN \| Mẫu 21a \| FR-XI-06 \| …` | **MATCH** (chỉ ở mức "tệp mang bảng chỉ tiêu tổng hợp khớp số liệu đã lưu") | **TEST** | Đọc bảng chỉ tiêu trong tệp → so **từng chỉ tiêu** với số liệu bản tổng hợp đã lưu ở phiếu 343 |

### 1.1 🔴 Hai vế `DIFF` — bắt buộc có câu CẦN BA CONFIRM trong kết quả

**(1) C6 — chức danh người ký:**
> **CẦN BA CONFIRM:** đối tác kỳ vọng *"cuối trang có ngày ký và **chức danh người ký**"*; SRS quy định
> **ngược lại** — `srs-fr-15-ct-htpldn.md:1017` khai khối ký cuối trang gồm *"ngày ký + họ tên cán bộ xuất
> báo cáo + chỗ trống cho chữ ký, chức vụ và con dấu khi in chính thức — **không in sẵn dòng chức danh**"*,
> và `srs-v3.5.md:6723` nêu **ngoại lệ chung cho mọi tệp xuất** `[BA chốt 2026-08-04, mở rộng phạm vi
> 2026-08-06]` với hai căn cứ: hồ sơ tài khoản (`TAI_KHOAN`) không lưu chức vụ nên không có nguồn dữ liệu,
> và biểu mẫu gốc 21a/21b để trống chỗ này cho người ký tự ghi khi ký tay; web/dev hiện tại
> **<điền sau khi mở tệp>**.
>
> **Câu hỏi BA:** phiếu UAT 345 viết trước hay sau chốt 2026-08-06? Tệp xuất của nhóm XI có phải **in sẵn**
> dòng chức danh người ký không, hay giữ đúng ngoại lệ §D.2.4 (chỉ chừa chỗ trống)? Nếu giữ ngoại lệ, xin
> xác nhận để cập nhật lại kỳ vọng của phiếu.

**(2) C7 — khuôn tên tệp lệch đúng một dấu gạch dưới:**
> **CẦN BA CONFIRM:** đối tác kỳ vọng tên tệp **`BaoCaoTongHop_CTHTPL_{YYYYMMDD_HHmm}`**; SRS quy định
> **`BaoCaoTongHopCTHTPL_{YYYYMMDD_HHmm}.{ext}`** (`srs-fr-15-ct-htpldn.md:1017`, `[BA chốt 2026-08-06]`),
> theo khuôn §H8 (`srs-v3.5.md:6760`): *"`{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền
> kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (kể cả dấu gạch nối, dấu cách,
> dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn. `{DinhDanh}` là đoạn tuỳ chọn khi tệp gắn với một bản ghi
> cụ thể — phải lấy từ một trường **đã khai trong entity** của bản ghi đó"* — mà `CTHTPL` **không phải** một
> trường đã khai trong entity nào, nên không thể là `{DinhDanh}`; web/dev hiện tại **<điền tên tệp thực tế>**.
>
> **Câu hỏi BA:** tên tệp đúng là `BaoCaoTongHopCTHTPL_…` (viết liền, theo §H8) hay `BaoCaoTongHop_CTHTPL_…`
> (như phiếu UAT)? Chốt xong xin sửa cho khớp giữa `:1017` và phiếu.

> ⚠️ **Hệ quả bắt buộc:** dù tệp xuất ra tên gì, **KHÔNG được Pass và KHÔNG được Reopen** vế C7 — kể cả khi
> tên trùng khít kỳ vọng đối tác (luật khóa 5). Tương tự với C6.

### 1.2 Vế **KHÔNG** thuộc phạm vi chấm (SRS có yêu cầu nhưng phiếu không nhắc) — chỉ ghi nhận

- **Họ tên cán bộ xuất báo cáo** ở khối ký (`:1017`, `:6722`).
- **Chỗ trống cho chữ ký / con dấu** (`:1017`, `:6722`).
- **Lề trang** (`srs-v3.5.md:6724` = `- Lề: Trên 2cm, Dưới 2cm, Trái 3cm, Phải 2cm`).
- **Tiêu ngữ** — `:6721` chỉ khai *"Quốc hiệu + Tên cơ quan ban hành"*; chuỗi "tiêu ngữ" chỉ xuất hiện ở
  `srs-fr-11-bao-cao.md:86` (**nhóm IX**, và chỉ cho PDF) ⇒ **không** dùng để chấm nhóm XI.
- **Giới hạn 10.000 dòng** (`srs-fr-11-bao-cao.md:87`, BR-DATA-06) — nhóm IX, không áp cho vế phiếu này.

Theo BUG SCOPE LOCK luật 1: *"tách đúng các vế trong expected đối tác, không thêm chức năng kế bên"*
⇒ thiếu/thừa các mục trên **không** kéo verdict; ghi vào mục "gửi dev/BA".

### 1.3 Căn cứ đã đọc trọn mục (không phải grep rỗng)

Đọc trọn FR-XI-09 `:971`–`:1038` (đặc biệt Outputs `:1012`–`:1017`, Processing bước 8 `:1006`,
Postconditions `:1019`–`:1023`), khối màn hình `:1161`–`:1175` (dòng #44, #45), Quy tắc tương tác `:1217`–`:1232`
(`:1232` = `- Xuat Excel/Word theo mau TT17/2025`). Ở `srs-v3.5.md`: D.2.3 `:6701`–`:6707`, D.2.4 `:6709`–`:6724`,
Phụ lục E §H `:6747`–`:6762` (H8 = `:6760`), LEG-06 `:4714`.
FR-XI-09 **không có** mã `INF-XI-09-*` nào cho thao tác xuất tệp (chỉ `:1032` cho tổng hợp thành công)
⇒ **thông báo sau khi xuất tệp là vùng SRS im lặng, KHÔNG chấm.**

---

## 2. Tiền đề tối thiểu — **phụ thuộc phiếu 343**

### 2.1 Tài khoản

| Vai trò | Tài khoản | Dùng để |
|---|---|---|
| 🔴 **Người ra verdict** — CB Nghiệp vụ cấp **TW** | **`cbnv_tw_03`** · `Test@1234` | **Bấm [Xuất Excel] / [Xuất Word] bằng giao diện thật**. `:982`, `:986`, `:1175` (*"user TW"*) |
| Dựng tiền đề đơn vị #1 / #2 | `cbnv_dp_03` + `cbpd_dp_03` · `cbnv_bn_03` + `cbpd_bn_03` (**mỗi cặp cùng `donViId`**) | Chuỗi lập → trình → duyệt → gửi TW |
| **CẤM ra verdict** | `admin` | Quyền rộng che lỗi phạm vi |

### 2.2 Chuỗi tiền đề (dài nhất trong 4 phiếu)

```
[A] ≥2 báo cáo đơn vị ở "Đã gửi Trung ương"      → ĐÃ CÓ SẴN, xem khung bên dưới
                                                    (công thức dựng lại: 00-TONG-HOP-BCCT.md §3;
                                                     dự phòng bước Trình duyệt: THBCTHCT_01.md §3.4)
[B] cbnv_tw_03 tick chọn các báo cáo → [Tổng hợp] → form tổng hợp hiện ra   (phiếu 344)
[C] cbnv_tw_03 bấm [Lưu] → ĐÃ HOÀN THÀNH TỔNG HỢP TOÀN QUỐC                 (phiếu 343)
        ← đây chính là điều kiện H345 mục 2; KHÔNG có bước này thì phiếu 345 KHÔNG đo được
        ⚠️ có thể còn MỘT bước chốt nữa sau [Lưu] — xem khung "bước chốt" bên dưới
[D] ĐO PHIẾU NÀY: bấm [Xuất Excel] → thu tệp; bấm [Xuất Word] → thu tệp
```

> 🟢 **[A] đã có sẵn — không phải dựng.** Trinh sát chỉ-đọc 11:33–11:50 ngày 2026-08-07
> ([`01-KIEM-KE-TIEN-DE.md`](01-KIEM-KE-TIEN-DE.md) §4.2): cặp **`c4801d2d…`** (Bộ KH&ĐT) +
> **`df6498aa…`** (Sở TP An Giang), cùng đợt `DOT-THBC01-UAT`, kỳ `SO_BO_6_THANG`, biểu `MAU_21A`, cả hai
> `DA_GUI_TW`. ⚠️ **Manh mối, không phải chuẩn chấm — xác minh lại trước khi đo.**
>
> 🔴 **[C] chỉ chạy sạch được MỘT lượt** ⇒ **thứ tự bắt buộc 344 → 343 → 345**, và phiếu 345 phải bám ngay
> sau 343 **trong cùng một phiên**. Đảo thứ tự hoặc để cách quãng = mất tiền đề.

> ⚠️ **KHUNG "BƯỚC CHỐT" — kiểm trước khi kết luận "chưa hoàn thành tổng hợp nên không xuất được".**
> Bản dựng có **hai** thao tác tách rời (trinh sát §3.2): lưu bản tổng hợp, và
> `POST /api/v1/bao-cao-ct-htpl/{id}/hoan-thanh-tong-hop` — mô tả của thao tác sau mới nói đưa báo cáo sang
> `DA_DUYET` và đợt sang `DA_TONG_HOP`. ⇒ Nếu sau [Lưu] mà nút xuất tệp chưa hiện / bị chặn, **rà màn tìm
> nút "Hoàn thành/Chốt tổng hợp" và bấm nốt** rồi mới kết luận. Không tìm thấy nút nào như vậy ⇒ ghi nhận
> và xử theo §6.

🔴 **Ghi lại TRƯỚC khi bấm xuất:** mốc giờ bấm (để đối chiếu đoạn `{YYYYMMDD_HHmm}` trong tên tệp) ·
danh sách báo cáo đã tổng hợp · số liệu từng chỉ tiêu của bản tổng hợp đã lưu (để đối chiếu C8).

### 2.3 Cái gì bằng API — cái gì BẮT BUỘC bằng giao diện

| Việc | Đường được phép |
|---|---|
| Toàn bộ [A] (tạo đợt, lập BC, trình, duyệt, gửi TW) | **API hoặc UI đều được** — tiền đề |
| [B] và [C] | **Giao diện** (đó là hành vi tranh chấp của phiếu 344/343; ở phiếu 345 chúng là tiền đề nhưng vẫn nên bấm UI để không phải dựng hai lần) |
| 🔴 **[D] Bấm [Xuất Excel] / [Xuất Word]** | **BẮT BUỘC GIAO DIỆN THẬT** — hành vi đang tranh chấp |
| Đọc nội dung tệp | **Bắt buộc mở tệp bằng thư viện** (`openpyxl` / `python-docx`) — **CẤM chấm bằng ảnh chụp** |

---

## 3. 🔴 Cách thu tệp và đọc nội dung — bắt buộc

**Nguyên tắc:** tệp đem đo **phải là tệp do chính lượt bấm trên giao diện sinh ra**. Ảnh chụp màn hình,
mã trạng thái 200, hay "thấy tệp tải về" đều **KHÔNG** thay được việc mở tệp.
*(Bài học đã ghi: "200 + nhị phân" chỉ chứng minh TẠO ĐƯỢC, không chứng minh ĐÚNG.)*

**Thứ tự thử khi thu tệp (dừng ở cách đầu tiên chạy được, khai rõ đã dùng cách nào):**

1. **Tệp về thư mục tải xuống của máy** (`~/Downloads`) → đo trực tiếp. *(Đã có tiền lệ chạy được với luồng
   xuất PDF của dự án này.)*
2. **Trình duyệt cách ly không đổ tệp ra đĩa** → đọc ngay trong trang: lấy nội dung nhị phân của phản hồi
   xuất tệp rồi **giải nén trong trang** (`.xlsx`/`.docx` đều là gói zip) và **chỉ trả về đúng thứ cần đo**
   (danh sách phần tử, chuỗi văn bản, khai báo phông/khổ giấy) — **KHÔNG** trả base64 toàn tệp.
3. **Tải lại đúng địa chỉ tệp mà lượt bấm đã gọi**, bằng **chính phiên `cbnv_tw_03`**, ghi ra tệp rồi đo.
   Khai rõ đây là **đối chứng**, không thay cho thao tác bấm ở [D].
   *(Manh mối đường dẫn — trinh sát §3.2 đọc `/api/docs-json` thấy `POST /api/v1/dot-bao-caos/tong-hop/export`
   nhận `baoCaoIds` + `format` (`xlsx`/`docx`) + `bieuMau`. **Vẫn phải tự xác minh lượt bấm thật gọi đường
   nào — cấm đoán endpoint**, và cấm dùng đường này thay cho việc bấm nút.)*

**Bảng đo bắt buộc lập cho MỖI định dạng:**

| Vế | `.xlsx` — đọc bằng `openpyxl` | `.docx` — đọc bằng `python-docx` |
|---|---|---|
| C0 | tệp mở được, có ≥1 sheet | tệp mở được, có ≥1 đoạn |
| C1 | `ws.page_setup.paperSize` = mã khổ A4 (ghi nguyên giá trị đọc được) | `section.page_width` ≈ 21,0 cm và `section.page_height` ≈ 29,7 cm (ghi số thực đọc được) |
| C2 | `cell.font.name` / `cell.font.size` của **các ô thân bảng chỉ tiêu** | phông của style `Normal` + của các đoạn thân tệp |
| C3–C4 | chuỗi ở các hàng đầu sheet **hoặc** phần header trang in (`ws.oddHeader`) | các đoạn đầu văn bản **hoặc** `section.header` |
| C5–C6 | chuỗi ở các hàng cuối **hoặc** `ws.oddFooter` | các đoạn cuối **hoặc** `section.footer` |
| C7 | tên tệp nguyên văn (kèm nguồn: tên tệp tải về / `Content-Disposition`) | như trên |
| C8 | bảng chỉ tiêu: `chỉ tiêu | giá trị trong tệp | giá trị bản tổng hợp đã lưu` | như trên |

---

## 4. ✅ PASS khi / ❌ FAIL nếu

```
✅ PASS khi (đủ C0 + C1 + C2 + C3 + C4 + C5 + C8, cho ĐỊNH DẠNG đang xét, trên tệp sinh từ lượt bấm MỚI):
   (C0) Bấm nút xuất trên giao diện → thu được tệp mở đúng định dạng bằng thư viện đọc tệp.
   (C1) Khổ giấy khai trong tệp là A4.
   (C2) Phông chữ thân tệp là Times New Roman cỡ 13.
   (C3) Phần đầu tệp có quốc hiệu.
   (C4) Phần đầu tệp có tên cơ quan.
   (C5) Phần cuối tệp có ngày ký.
   (C8) Bảng chỉ tiêu trong tệp khớp số liệu của bản tổng hợp đã lưu.
   ⚠️ Còn C6 + C7 = DIFF ⇒ theo flow 04 §Verdict: có DIFF giữa SRS và expected ⇒ verdict logic của phiếu là
      **Cần BA**, KHÔNG phải Pass — kể cả khi 6 vế MATCH đều đạt.

❌ REOPEN nếu (vế MATCH sai — chỉ Reopen phần mà CẢ SRS lẫn expected cùng yêu cầu mà web không đạt):
   - Bấm nút xuất mà không sinh ra tệp, hoặc tệp hỏng/không mở được bằng thư viện đọc tệp;
   - HOẶC một trong hai định dạng (.xlsx / .docx) không tạo được trong khi :1017 + :1175 khai cả hai;
   - HOẶC khổ giấy không phải A4, hoặc phông thân tệp không phải Times New Roman 13;
   - HOẶC thiếu quốc hiệu, thiếu tên cơ quan ở đầu tệp, hoặc thiếu ngày ký ở cuối tệp;
   - HOẶC số liệu trong tệp không khớp bản tổng hợp đã lưu.

⏸ CHƯA CHỐT nếu: chưa hoàn thành được bước [C] (lưu tổng hợp) ⇒ điều kiện H345 mục 2 không đạt;
   hoặc không thu được tệp để mở nội dung sau khi đã thử đủ 3 cách §3.
```

### 4.1 ⚠️ Bẫy chống **FAIL oan**

1. 🔴 **Chấm C6/C7 thành lỗi.** Hai vế này đã khóa **DIFF** — **cấm Pass và cấm Reopen**, kể cả khi tệp làm
   đúng y kỳ vọng đối tác hoặc đúng y SRS. Chỉ ghi nhận + câu hỏi BA §1.1.
2. **FAIL vì tệp thiếu "tiêu ngữ".** `:6721` chỉ khai *"Quốc hiệu + Tên cơ quan ban hành"*; chuỗi "tiêu ngữ"
   thuộc nhóm IX (`srs-fr-11-bao-cao.md:86`) ⇒ không phải yêu cầu của nhóm XI, và phiếu cũng không nhắc.
3. **FAIL vì tiêu đề/quốc hiệu không phải cỡ 13.** `:6720` khai phông chung, **không** khai riêng cho dòng
   tiêu đề. Chấm C2 theo **phông thân tệp** (các ô/đoạn của bảng chỉ tiêu); tiêu đề in đậm/cỡ khác **không**
   dùng để FAIL. Ghi nhận nếu lệch.
4. **FAIL vì quốc hiệu nằm ở hàng dữ liệu thay vì "header trang in" của bảng tính.** `:6721` nói *"Header"*
   nhưng **không** quy định chỗ đặt trong tệp bảng tính ⇒ đặt ở các hàng đầu sheet **cũng đạt**.
5. **FAIL vì thiếu họ tên cán bộ xuất / chỗ trống con dấu / lề trang.** Không thuộc vế phiếu (§1.2).
6. **FAIL vì không có thông báo sau khi xuất.** SRS im lặng (§1.3) ⇒ không chấm.
7. **Nhãn nút khác phiếu.** `:1175` khai `[Xuat Excel] [Xuat Word]`; phiếu ghi "Xuất Excel"/"Xuất Word" —
   khớp. Nếu giao diện đặt nhãn khác, phiếu không nhắc nhãn ⇒ cấm FAIL vì nhãn.
8. **Tài khoản không phải cấp TW bị chặn xuất** = ĐÚNG SPEC (`:986`, `:1030`, `:1175` *"user TW"*).

### 4.2 ⚠️ Bẫy chống **PASS oan**

1. 🔴 **Chấm bằng ảnh chụp / bằng "tệp tải về được".** Bắt buộc **mở nội dung tệp** bằng thư viện.
2. 🔴 **Đo tệp cũ.** Tệp của lượt xuất **trước** bản dựng đang đo mang dữ liệu cũ. Đối chiếu đoạn
   `{YYYYMMDD_HHmm}` trong tên tệp với **mốc giờ bấm** đã ghi ở §2.2; lệch quá vài phút ⇒ **không phải tệp
   của lượt này**.
3. **Chỉ đo `.xlsx` rồi suy cho `.docx`.** Hai đường sinh tệp khác nhau ⇒ **đo riêng từng định dạng**,
   lập **hai** bảng ở §3.
4. **Kiểm một ô rồi kết luận phông toàn tệp.** Đọc phông của **nhiều ô/đoạn thân bảng**, ghi rõ đã đọc bao
   nhiêu ô và có ô nào lệch không.
5. **So số liệu tệp với số trên màn thay vì với bản ghi đã lưu.** Màn có thể còn giá trị chưa lưu; C8 phải
   so với **bản tổng hợp đã lưu** (đọc lại sau khi tải lại trang bằng địa chỉ).
6. **Tin tên tệp hiển thị trên giao diện.** Lấy tên tệp từ **tệp thực tế** hoặc `Content-Disposition`,
   ghi **nguyên văn** kể cả dấu gạch dưới và đuôi.
7. **Tab mở lâu chạy bó mã cũ** ⇒ tải lại bằng địa chỉ, đọc tên bó mã `assets/index-*.js` đầu và cuối phiên.
8. **Kết luận trên env khác** ⇒ ghi câu giới hạn hiệu lực (đo trên env nội bộ).

---

## 5. Đường đo thứ hai (đối chứng độc lập — đúng 1 đường)

**Mở nội dung tệp là đường thứ nhất.** Đường thứ hai = đọc lại **bản ghi tổng hợp đã lưu** bằng chính phiên
`cbnv_tw_03` và so từng chỉ tiêu với bảng số trong tệp (vế C8), đồng thời đối chiếu mốc giờ bấm với đoạn
thời gian trong tên tệp (vế C7 — chỉ ghi nhận).
🔴 Tra `/api/docs-json` lấy đúng đường dẫn — **CẤM đoán endpoint**.
Bấm lại cùng nút xuất **không** tính là đường thứ hai.
**Hai đường mâu thuẫn ⇒ CHƯA được chốt.**

---

## 6. 🔴 Rủi ro verdict **Chưa chốt** — CAO NHẤT trong 4 phiếu

| # | Rủi ro | Vì sao | Cần bổ sung gì mới chốt được |
|---|---|---|---|
| **R1** | **Không hoàn thành được bước [C] (Lưu tổng hợp)** | Điều kiện H345 mục 2 đòi *"Đã hoàn thành tổng hợp báo cáo toàn quốc"*. Nếu phiếu 343 rơi vào rủi ro R1 của nó (máy chủ chặn vì trạng thái ĐỢT chưa `DA_GUI_TW`) thì **cả phiếu 345 không có tiền đề** | Ghi **Chưa chốt**, nêu rõ: cần dev mở được luồng tổng hợp, hoặc BA chốt mô hình trạng thái đợt (câu hỏi ở `THBCTHCT_01.md` §2.1) |
| **R2** | **Không thu được tệp để mở nội dung** | Trình duyệt cách ly có thể không đổ tệp ra đĩa | Thử đủ 3 cách §3; vẫn không được ⇒ **Chưa chốt**, nêu rõ cần bật đường tải tệp hoặc cấp tệp mẫu do dev xuất |
| **R3** | **Chỉ có một trong hai nút xuất** | `:1017` + `:1175` khai cả `.xlsx` lẫn `.docx` | Đo định dạng có sẵn; nửa còn lại ghi ⏸ **chưa đo được** + ghi nhận cho dev. Nếu nút **có** mà bấm không ra tệp ⇒ **Reopen** vế C0 cho định dạng đó |
| **R4** | Không dựng nổi ≥2 báo cáo "Đã gửi TW" | ~~Rủi ro~~ → **đã hạ mức**: kiểm kê 11:50 thấy cặp sẵn sàng (§2.2) | Nếu dữ liệu bị tiêu thụ mất: dựng lại theo `THBCTHCT_01.md` §6 R5 (duyệt + gửi TW 2 báo cáo `CHO_PHE_DUYET` của Bộ KH&ĐT) |
| **R5** | **Chỉ có MỘT lượt tiền đề sạch** — 343 chạy xong là cặp nguồn hết dùng lại được | Trinh sát §5.3(b)(c) | Đo 345 **ngay sau** 343 trong **cùng phiên**. Lỡ mất ⇒ dựng lại theo R4 rồi chạy lại cả 343 |

> 🟢 **Mức rủi ro tổng thể giảm so với đánh giá ban đầu** (tiền đề [A] đã có sẵn), **nhưng phiếu này vẫn
> rủi ro cao nhất lô** vì phụ thuộc dây chuyền 344 → 343 → 345 và vì còn khâu thu tệp (R2).

---

## 7. Ghi nhận (KHÔNG chấm) — gửi BA/dev

1. **Câu chữ `:1017` và phiếu UAT lệch nhau ở đúng một dấu gạch dưới của tên tệp** (§1.1 mục 2) — đề nghị
   chốt một khuôn duy nhất rồi sửa cho khớp.
2. **Ngoại lệ "không in sẵn dòng chức danh"** (`:1017`, `:6723`, `[BA chốt 2026-08-06]`) mâu thuẫn với kỳ vọng
   phiếu UAT (§1.1 mục 1).
3. Nếu tệp thiếu **họ tên cán bộ xuất báo cáo** / **chỗ trống con dấu** / sai **lề trang** — SRS **có** yêu
   cầu (`:1017`, `:6722`, `:6724`) nhưng phiếu không nhắc ⇒ ghi nhận cho dev, không kéo verdict.
4. FR-XI-09 **không khai thông báo** cho thao tác xuất tệp (không có `INF-XI-09-*` nào ngoài `:1032`) —
   nếu muốn ràng buộc, đề nghị BA bổ sung.

---

## 8. Độ phủ biến thể — **sàn: 1 lượt xuất mỗi định dạng**

| # | Dạng | Bắt buộc? |
|---|---|---|
| **①** | [Xuất Excel] → `.xlsx` | **BẮT BUỘC** |
| **②** | [Xuất Word] → `.docx` | **BẮT BUỘC** (`:1017` + `:1175` khai cả hai; phiếu cũng nhắc cả hai) |

**KHÔNG mở rộng:** không xuất lại nhiều lần để dò hậu tố `_1`/`_2` của §H8 (phiếu không nhắc) · không đo
xuất tệp ở màn khác (danh sách CT `:1110` [Xuat Excel] là **chức năng khác**, FR-XI-02 `:387`) · không đo
giới hạn 10.000 dòng · không đo bằng vai trò khác.
