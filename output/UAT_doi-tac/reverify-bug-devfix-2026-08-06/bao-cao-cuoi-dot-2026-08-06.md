# Báo cáo cuối đợt — Re-verify bug dev claim đã fix (FLOW 04) · 2026-08-06

| Thông tin | Giá trị |
|---|---|
| **Phạm vi** | Bảng `1OKBN2otlmdZ44…` tab `bug`, các dòng có `Dopai = dev done` **và** `Trạng thái dev fix = Fixed`; giới hạn **2 module** |
| **Module đã chọn** | **LKHDG** (Đánh giá hiệu quả · Kế hoạch đánh giá) và **QLNDTVVCG** (Tư vấn chuyên sâu) |
| **Case đã verify** | **4/4** — `LKHDG_12` (dòng 126) · `LKHDG_16` (dòng 127) · `QLNDTVVCG_24` (dòng 286) · `QLNDTVVCG_26` (dòng 287) |
| **Môi trường đo** | `https://18.143.165.120.nip.io` — bản dựng **HTPLDN · V1.0.8** |
| **Đặc tả tham chiếu** | `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/` |

## Verdict đã ghi vào bảng

| Dòng | Mã TC | Verdict | Ô đã ghi | Thời điểm ghi |
|---:|---|---|---|---|
| 126 | `LKHDG_12` | 🔁 **Reopen** | `Trạng thái dev fix = Reopen` + `Kết quả verify` | 08:09:36 |
| 127 | `LKHDG_16` | 🔁 **Reopen** | `Trạng thái dev fix = Reopen` + `Kết quả verify` | 08:38:40 |
| 286 | `QLNDTVVCG_24` | ✅ **Pass** | `Trạng thái dev fix = Test done` + `Kết quả verify` | 09:21:37 |
| 287 | `QLNDTVVCG_26` | ✅ **Pass** | `Trạng thái dev fix = Test done` + `Kết quả verify` | 09:40:25 |

Mọi lượt ghi đều chạy qua công cụ có guard (`tools/sheet_bug_verify_write.py`): khớp gid + tiêu đề tab, dò cột
theo **tên**, khớp lại **Mã TC** của đúng dòng, kiểm giá trị mới có nằm trong dropdown của chính ô đó, và
**đọc lại** sau khi ghi. Nhật ký giá trị *cũ → mới*: `tools/sheet_bug_verify_write.log`.

---

## 1. Lỗi phát hiện thêm ngoài phạm vi

**Có — 3 lỗi**, tất cả đều thuộc module Tư vấn chuyên sâu, phát hiện trong lúc **dựng tiền đề** và **đo** cho
`QLNDTVVCG_26`. Không lỗi nào nằm trong nội dung đối tác phản ánh, nên **không** kéo verdict của 4 case trên.
Hồ sơ đầy đủ: [`bug-reports/bug-report-QLNDTVVCG.md`](bug-reports/bug-report-QLNDTVVCG.md).

| Bug ID | Dòng trên bảng | Mức | Tóm tắt | Căn cứ đặc tả | Chủ việc |
|---|---|---|---|---|---|
| `BUG-TVCS-PHANCONG-QUYEN` | `QLNDTVVCG_OOS_02` — dòng **360** | **Major** | Tài khoản chỉ có vai trò *Tư vấn viên / Chuyên gia* vẫn phân công được nội dung tư vấn chuyên sâu — giao diện hiện nút **và** máy chủ chấp nhận (HTTP 200, bản ghi đổi trạng thái thật) | `srs-fr-12-tv-chuyen-sau.md:34` · `:97` · `:170` | Dev BE (chặn ở máy chủ) → Dev FE (ẩn thao tác) |
| `BUG-TVCS-PHANCONG-EMAIL` | `QLNDTVVCG_OOS_03` — dòng **361** | Medium | Bước phân công chuyên gia không sinh thư điện tử, dù đây là bước **duy nhất** trong nhóm ghi rõ kênh *"(in-app + email)"* | `srs-fr-12-tv-chuyen-sau.md:174` | Dev BE |
| `BUG-TVCS-NHATKY-LYDO` | `QLNDTVVCG_OOS_04` — dòng **362** | Minor | Nhật ký thao tác của lượt chuyên gia từ chối chỉ ghi hành động chung *"Cập nhật"*, không lưu lý do từ chối | `srs-fr-12-tv-chuyen-sau.md:198` | Dev BE |

**Về `BUG-TVCS-PHANCONG-QUYEN`:** đây là lỗi **vượt quyền ở tầng máy chủ**, không phải chỉ lỗi ẩn/hiện nút. Đã đo
2 đường độc lập và đã hoàn nguyên dữ liệu ngay sau phép thử. Đề nghị xử lý trước 2 lỗi còn lại.

**Câu "phát hiện thêm 3 lỗi" dựa trên quan sát nào:** ảnh
`bug-reports/image/QLNDTVVCG_26-B-…png` (thanh hành động có [Phân công] khi đang đăng nhập bằng tài khoản
Tư vấn viên / Chuyên gia) · số liệu hộp thư giả lập của env trước/sau thao tác phân công · danh sách trường của
bản ghi nhật ký đọc trực tiếp từ hệ thống. Không có mục nào chỉ dựa vào suy đoán.

### Lỗi gặp lại nhưng **đã có phiếu** — không mở dòng mới

| Phiếu đã có | Trạng thái đang ghi trên bảng | Đo lại 06/08 trên V1.0.8 | Đề nghị |
|---|---|---|---|
| `QLNDTVVCG_OOS_01` — dòng **358** — *chuyên gia bấm "Từ chối nhiệm vụ" nhưng khung thông báo ghi "Đã xác nhận"* | `Trạng thái = Fail` · `Trạng thái dev fix = Fixed` · `Dopai = bug` | **Đã hết lỗi** — thông báo nay ghi *"Đã từ chối nhiệm vụ"*, đúng bản chất thao tác. Đo trong lúc chạy `QLNDTVVCG_26` | Dòng này **nằm ngoài** bộ lọc của đợt (`Dopai = bug`, không phải `dev done`) nên QA **không tự ghi verdict**. **User quyết** có cho ghi `Test done` + *Kết quả verify* hay để dev/đối tác tự xác nhận |

Không mở dòng mới cho lỗi này — phiếu đã tồn tại từ đợt tuần 3.

---

**Đã đưa lên bảng theo dõi** (06/08/2026): 3 dòng mới `QLNDTVVCG_OOS_02` / `_03` / `_04` ở cuối tab `bug`
(dòng **360–362**), `Trạng thái = Fail`, `Dopai = bug`, ảnh bằng chứng gắn dạng đường liên kết xem được ở cột
*Ảnh/vieo 1*. Ô `Trạng thái dev fix` để **trống** (user chốt bỏ qua cột này — giá trị `open` không có trong danh
sách chọn của ô; 12 dòng `*_OOS_*` cũ cũng được log với ô này trống, dev điền sau).

---

## 2. Dữ liệu đã seed / thay đổi

Toàn bộ trên env `https://18.143.165.120.nip.io` (bản dựng V1.0.8). **Không** thao tác gì trên env nghiệm thu
của đối tác.

### 2.1 Module Đánh giá hiệu quả (LKHDG)

| Bản ghi | Thay đổi | Hoàn nguyên được? |
|---|---|---|
| `DG-20260730-0002` | Tải lên **2 tệp** đính kèm; sửa *Tên đợt* + *Ghi chú* (dấu nhận dạng `QA-LKHDG16-EDIT-20260806-0830`), bản ghi lên **version 3** | Được — xoá tệp + sửa lại text |
| `DG-20260806-0001` | **Tạo mới**. Tải lên 1 tệp `QA-LKHDG16-ke-hoach.pdf`; *Ghi chú* = `QA-LKHDG16-V1-1TEP-20260806`; nhập **4 tiêu chí** từ danh mục với *Điểm tối đa* = 100; thêm **1 người đánh giá**; trạng thái **Lập kế hoạch → Phân công** | ⚠️ **Không** — luồng trạng thái không có đường lùi *Phân công → Lập kế hoạch*; chỉ có thể huỷ cả đợt |

### 2.2 Module Tư vấn chuyên sâu (QLNDTVVCG)

| Bản ghi | Thay đổi | Trạng thái cuối đợt |
|---|---|---|
| `TVCS-20260725-0005` | Phân công chuyên gia → chuyên gia chấp nhận | **Đang tư vấn** (có ngày bắt đầu + 1 phiên tư vấn mới) |
| `TVCS-20260806-0001` (`c20bfe33-…`) | **Tạo mới** bằng `cbnv_tw` → phân công → chấp nhận | **Đang tư vấn** (có ngày bắt đầu + 1 phiên tư vấn mới) |
| `TVCS-20260806-0002` (`83eb5e0c-…`) | **Tạo mới** bằng `cbnv_tw`. Phân công → chuyên gia từ chối → phân công lại (phép thử quyền) → từ chối lần 2 | **Tiếp nhận**, không có chuyên gia, version 5, *Ghi chú* mang dấu nhận dạng QA |
| `TVCS-20260803-0003` (`099a739d-…`) | Phân công → chuyên gia từ chối | **Tiếp nhận**, không có chuyên gia, version 5, *Ghi chú* mang dấu nhận dạng QA |

### 2.3 Danh mục / tài khoản

| Đối tượng | Thay đổi | Trạng thái cuối đợt |
|---|---|---|
| Tư vấn viên `qa_tvvseed28` (`98cfd963-…`) | Đổi *loại* Chuyên gia → Tư vấn viên (để thử dạng dữ liệu thứ 2 của `QLNDTVVCG_24`) rồi **đổi lại Chuyên gia** | ✅ **Đã hoàn nguyên** (version 22) |

### 2.4 Tác dụng phụ không tránh được

- **Thông báo trong ứng dụng** đã sinh thêm cho: `cbnv_tw`, `cbnv_tw_04`, `qa_tvvseed28`, và tài khoản doanh
  nghiệp `0109998887` — đúng nội dung nghiệp vụ của các thao tác ở mục 2.2.
- **Hộp thư giả lập của env**: tổng số thư **1510 → 1514**; cả 4 thư tăng thêm đều là **mã đăng nhập** của các
  tài khoản đã dùng, không phải thư nghiệp vụ.
- Mỗi lần đổi tài khoản đều sinh thông báo *"Tài khoản vừa đăng nhập ở nơi khác"* cho tài khoản bị đá phiên.

---

## 3. Việc chưa chốt được × vì sao × cần ai làm gì

### A. Case đã có verdict nhưng chưa đóng được

| Hạng mục | Vì sao chưa chốt | Cần ai làm gì |
|---|---|---|
| `LKHDG_12` — Reopen | Vế *xuất Excel không áp bộ lọc đang bật* vẫn tái hiện nguyên vẹn trên 2 bộ lọc khác cột nhau | **Dev BE** sửa theo `BUG-LKHDG-EXPORT-FILTER`, rồi chạy lại đúng khối *CÁCH VERIFY* ở ô note dòng 126 |
| `LKHDG_16` — Reopen | Đợt ở trạng thái *Phân công* không vào được chế độ sửa; giao diện và máy chủ thống nhất nhau (409 `ERR-BIZ-XI-01-02`) nên là luật đang cài đặt, trái `:837` + `:159` | **Dev BE** gỡ chặn cập nhật ở trạng thái `PHAN_CONG` → **Dev FE** hiện lại thao tác Sửa. Nếu luật thật sự là "chỉ sửa ở Lập kế hoạch" thì **BA** phải chốt và sửa `:837` |
| 3 lỗi mới ở mục 1 | Mới log, chưa có bản sửa | **Dev BE** (cả 3) → **Dev FE** (riêng phần ẩn nút của `BUG-TVCS-PHANCONG-QUYEN`) |

### B. Việc bị chặn về công cụ — **cần user quyết**

> Theo quy tắc của flow: công cụ **ghi** bị chặn thì **DỪNG và báo user**, cấm ghi tay để lách và cấm viết
> script dùng-một-lần. Hai hạng mục dưới đây đang ở tình trạng đó.

| Mã | Việc còn thiếu | Vì sao chặn | Cần ai làm gì |
|---|---|---|---|
| ~~**B1**~~ | ~~3 lỗi ngoài phạm vi ở mục 1 chưa có dòng case riêng trên bảng theo dõi~~ | ~~`sheet_bug_verify_write.py` không có chức năng thêm dòng mới~~ | ✅ **Đã xong 06/08/2026.** User cho phép thêm vào cuối tab `bug`. Không viết script dùng-một-lần: mở rộng công cụ có sẵn `sheet_add_bug_row.py` (vốn đã có 8 guard cho việc append) để nhận thêm tab `bug` + bộ header của tab đó. Kết quả: dòng **360–362** |
| ~~**B3**~~ | ~~3 dòng mới 360–362 để trống ô *Trạng thái dev fix* trong khi yêu cầu là ghi `open`~~ | ~~Ô đó là ô chọn (kiểm tra chặt), danh sách `In Progress · Fixed · UAT done · Bug · Test done · reject · Reopen` không có `open`~~ | ✅ **Đã chốt 06/08/2026** — user quyết **bỏ qua cột này**, giữ trống, dev điền sau. Đúng tiền lệ 12 dòng `*_OOS_*` cũ |
| **B2** | Ô *Kết quả verify* của **dòng 286 và 287** còn thiếu khối **CÁCH VERIFY sau Dev fix** (dòng 126 và 127 đã có). Riêng dòng 287 còn một câu nhắc tới bằng chứng của đối tác — thuộc nhóm chi tiết nội bộ cần gỡ khỏi ô note | Guard của công cụ chỉ cho ghi khi *Trạng thái dev fix* đang là `Fixed`; hai dòng này **đã** thành `Test done` sau lượt ghi ban đầu, nên lượt ghi bù bị từ chối: *"'Trạng thái dev fix' dòng 286 đang là 'Test done', chỉ ghi khi thuộc ['Fixed']"* | **User quyết**: cho phép bổ sung chế độ *chỉ ghi đè ô Kết quả verify* (không đụng cột trạng thái, vẫn bắt buộc `--cho-phep-de-ketqua` + đọc lại). Nội dung thay thế đã soạn sẵn, chỉ chờ ghi |

**Ảnh hưởng của B2:** verdict trên bảng **đúng** và ô *Kết quả verify* **đã có** đủ căn cứ + cách tái hiện dạng
văn xuôi. Thiếu là **khối CÁCH VERIFY dạng chuẩn** — thứ giúp vòng sau chỉ cần chạy lại đúng khối đó thay vì
verify lại từ đầu. Khối này **đã có đầy đủ** trong 2 bug entry `BUG-TVCS-XACNHAN-THONGBAO` và
`BUG-TVCS-TUCHOI-THONGBAO` tại `bug-reports/bug-report-QLNDTVVCG.md`, nên hồ sơ **không mất**, chỉ chưa đồng bộ
sang ô note.

### C. Điểm chờ BA — không case nào bị treo verdict vì các điểm này

| Phiếu | Câu hỏi | Nếu BA chọn hướng ngược lại thì sao |
|---|---|---|
| [`../reverify-week-5/ba-confirm/ba-confirmation-needed-LKHDG-2026-08-06.md`](../reverify-week-5/ba-confirm/ba-confirmation-needed-LKHDG-2026-08-06.md) | Bảng thành phần form tạo/sửa đợt đánh giá (`:843-851`) là danh sách **đóng** hay **mở**? Giao diện đang hiện thêm *Tài liệu đính kèm* + *Cơ quan được đánh giá* | Nếu **đóng** → kỳ vọng của đối tác ở `LKHDG_16` vòng 2 là sai so với đặc tả, **BA phản hồi đối tác**; vẫn **không** đề nghị Dev gỡ tính năng |
| [`../reverify-week-5/ba-confirm/ba-confirmation-needed-QLNDTVVCG-2026-08-06.md`](../reverify-week-5/ba-confirm/ba-confirmation-needed-QLNDTVVCG-2026-08-06.md) | Sự kiện *chuyên gia xác nhận / từ chối* phải gửi thông báo qua **kênh nào**? `:186` và `:197` không ghi kênh, còn `BR-NOTIF-01` đòi *in-app + email* nhưng phạm vi áp dụng **không** gồm FR-X.1 | Nếu **phải có email** → mở lại `QLNDTVVCG_24` và `QLNDTVVCG_26`, chủ việc **Dev BE** |
| ↳ cùng phiếu | Nội dung tư vấn chuyên sâu được giao cho **những ai**? `:172` viết *"CG/TVV"* nhưng hệ thống chỉ nhận loại Chuyên gia | Nếu **cả hai loại** → việc chặn hiện nay là lỗi, chủ việc **Dev BE**; đồng thời mở lại được dạng dữ liệu thứ 2 của `QLNDTVVCG_24` |
| ↳ cùng phiếu | Sau khi từ chối, màn hình **nên đi đâu**? Đối tác mong đợi *quay về danh sách*; đặc tả im lặng | Nếu **phải quay về danh sách** → bổ sung vào đặc tả màn hình trước, rồi mới giao **Dev FE** |

---

## Hồ sơ đợt này

```
reverify-bug-devfix-2026-08-06/
├── bao-cao-cuoi-dot-2026-08-06.md          ← file này
├── tieuchi/                                 ← viết TRƯỚC khi mở màn tranh chấp
│   ├── LKHDG_12.md · LKHDG_16.md
│   └── QLNDTVVCG_24.md · QLNDTVVCG_26.md
├── bug-reports/
│   ├── bug-report-LKHDG.md                  ← 2 bug Open (Reopen)
│   ├── bug-report-QLNDTVVCG.md              ← 3 bug Open (ngoài phạm vi) + 2 entry Closed (Pass)
│   └── image/                               ← 15 ảnh, đều đã mở đọc lại trước khi trích dẫn
├── ba-confirm/
│   ├── ba-confirmation-needed-LKHDG-2026-08-06.md
│   └── ba-confirmation-needed-QLNDTVVCG-2026-08-06.md
├── partner-evidence/                        ← bằng chứng đối tác (chỉ đọc)
└── frames/                                  ← khung hình trích ra để đọc full-res
```

> **Giới hạn hiệu lực của cả đợt:** mọi kết luận "đã hết lỗi" chỉ đúng trên **bản dựng V1.0.8 của env dev**.
> Đối tác quay bằng chứng trên env nghiệm thu với bản dựng cũ hơn (V1.0 / V1.0.2 / V1.0.3). Verdict chưa có hiệu
> lực nghiệm thu cho tới khi bản dựng này lên env đối tác.
