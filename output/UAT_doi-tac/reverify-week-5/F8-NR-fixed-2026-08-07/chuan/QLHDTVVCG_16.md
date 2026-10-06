# QLHDTVVCG_16 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 322 · **Mô tả (G):** Xuất Excel
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Tìm kiếm hợp lệ · 3. Nhấn "Xuất Excel"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §Processing — Xuất Excel · **Kiểm chéo:** `srs-v3.5.md` Phụ lục E §H8 (quy ước tên tệp xuất, BẮT BUỘC toàn hệ thống); `srs-fr-11-bao-cao.md` (tiền lệ áp H8)

> 🔴 **Phiếu này có 1 vế `DIFF` + 1 vế `GAP` → CẤM Pass toàn phiếu, kết luận Cần BA.**

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Áp dụng **toàn bộ bộ lọc đang hiển thị** (từ khóa, tư vấn viên, khoảng ngày) và **phân quyền dữ liệu theo đơn vị** của NSD" | `srs-fr-14-hop-dong-tv.md:132`, `:133`, `:184` + BR-AUTH-08 `:496` | **MATCH** | TEST | **UI:** đặt bộ lọc từ khóa cho ra **tập con thật sự nhỏ hơn** tổng số (vd 2/8 bản ghi) → bấm Xuất Excel. **Đối chứng:** mở tệp bằng `openpyxl`, đếm số dòng dữ liệu và đọc mã hợp đồng từng dòng — phải **đúng bằng** tập đang hiển thị, không phải toàn bộ dữ liệu |
| **C2** | "Tạo tệp định dạng .xlsx **gồm các cột đang hiển thị trên màn hình danh sách**" | `srs-fr-14-hop-dong-tv.md:134` — chính đặc tả ghi *"cấu trúc cột Excel **cần CĐT xác nhận template**"*, và cả khối mang cờ `[GAP-X.3-02]` (`:127`) ⇒ **chưa chốt trong đặc tả** | **GAP** | **BA** | Chỉ mở tệp đọc **danh sách tiêu đề cột thực tế** để mô tả cho BA (đối chiếu tham khảo với `:288` và `:147`–`:155`). **CẤM Pass/Reopen vế này** |
| **C3** | "…giới hạn tối đa **10.000 dòng** trong một tệp" | `srs-fr-14-hop-dong-tv.md:134` (nguyên văn "max 10.000 dòng") | **MATCH** | TEST | Môi trường không có 10.000 hợp đồng (`:398` ước tính ~1.000 bản ghi/năm) ⇒ **không dựng được ca chạm ngưỡng**. Đo được: mở tệp đếm số dòng ≤ 10.000 và **không bị cắt** so với tập đang lọc. Nếu tổng dữ liệu < 10.000 thì vế này chỉ chứng minh được "không cắt sai", ghi rõ giới hạn hiệu lực; **cấm** seed 10.000 bản ghi để thử |
| **C4** | "Trả tệp về máy NSD với tên dạng **HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx**" | `srs-v3.5.md:6760` — Phụ lục E §H8 **BẮT BUỘC**, áp cho **mọi nhóm chức năng**, khuôn `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`, `{TenTep}` **viết liền PascalCase, bỏ mọi ký tự không phải chữ hoặc số kể cả dấu gạch nối**. Khuôn đối tác kỳ vọng dùng **chữ thường + dấu gạch nối** ⇒ **ngược quy ước** | **DIFF** | **BA** | Chỉ đo hiện trạng: đọc **tên tệp thật** hệ thống trả về (không phải tên mình đặt lại khi lưu). **CẤM Pass kể cả khi tên tệp trùng đúng kỳ vọng đối tác** |

### Câu bắt buộc cho vế `DIFF` (soạn sẵn)

> **CẦN BA CONFIRM:** đối tác kỳ vọng tên tệp xuất dạng **`HDTV-danh-sach-{YYYYMMDD-HHmm}.xlsx`** (chữ thường, ngăn bằng dấu gạch nối); SRS quy định quy ước tên tệp xuất **thống nhất toàn hệ thống** theo khuôn **`{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`**, trong đó `{TenTep}` **viết liền kiểu PascalCase và bỏ mọi ký tự không phải chữ hoặc số, kể cả dấu gạch nối** — `srs-v3.5.md:6760` (Phụ lục E §H8, `[BA chốt 2026-08-06]`); web/dev hiện tại **&lt;điền sau khi đo&gt;**.

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:127`** (tiêu đề khối — mang cờ gap của chính đặc tả)
```
**Processing — Xuất Excel** `[GAP-X.3-02]`:
```

**`srs-fr-14-hop-dong-tv.md:131`**–**`:135`** (trọn bảng Processing — Xuất Excel, 5 bước)
```
| 1 | Kiểm tra quyền CB NV | BR-AUTH-01 |
| 2 | Áp dụng filter hiện tại (TVV, trạng thái, thời gian) | — |
| 3 | Truy vấn HOP_DONG_TU_VAN theo filter | — |
| 4 | Tạo file .xlsx (max 10.000 dòng — cấu trúc cột Excel **cần CĐT xác nhận template**; mặc định Excel generic theo các cột hiển thị ở Outputs) | — |
| 5 | Trả file download cho user | — |
```
> Bước 4 vừa là neo `MATCH` của C3 ("max 10.000 dòng"), vừa là neo `GAP` của C2 ("cần CĐT xác nhận template").
> ⚠️ Bước 2 liệt kê bộ lọc **"TVV, trạng thái, thời gian"** — **thiếu "từ khóa"** (trường `keyword` có thật ở `:216`) và **thừa "trạng thái"** (FR-X.3-02 `:216`–`:219` **không** khai bộ lọc trạng thái). Lệch nội bộ này đưa vào câu hỏi BA, không dùng để Fail C1.

**`srs-fr-14-hop-dong-tv.md:184`** (Acceptance Criteria)
```
- **Given** CB NV xem DS hợp đồng **When** nhấn Xuất Excel **Then** tải file .xlsx theo filter hiện tại `[GAP-X.3-02]`
```

**`srs-fr-14-hop-dong-tv.md:147`**–**`:155`** (Outputs FR-X.3-01 — "các cột hiển thị ở Outputs" mà bước 4 nhắc tới)
```
| 1 | ma_hop_dong | text | luôn | HDTV-{date}-{seq} |
| 2 | ten_hop_dong | text | luôn | — |
| 3 | ben_a | text | luôn | — |
| 4 | ben_b | text | luôn | — |
| 5 | gia_tri_hop_dong | money | luôn | format tiền VND |
| 6 | thoi_han_bat_dau | date | luôn | dd/mm/yyyy |
| 7 | thoi_han_ket_thuc | date | luôn | dd/mm/yyyy |
| 8 | so_vv_lien_ket | number | luôn | badge |
| 9 | tien_do_tt | number | luôn | progress bar % |
```

**`srs-fr-14-hop-dong-tv.md:288`** (các cột "đang hiển thị trên màn hình danh sách" theo cách hiểu của đối tác)
```
| 4 | content | Bảng hợp đồng | table | Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu <= 30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động (CB NV thấy Xem/Sửa/Xóa; TVV/CG CHỈ thấy nút Xem) | click -> action | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:496`** (BR-AUTH-08 — phân quyền dữ liệu)
```
| **Phát biểu** | Chính sách phân quyền dữ liệu áp dụng cho MỌI bảng có cột `don_vi_id`. Không có exception ngoại trừ QTHT |
```

**`srs-fr-14-hop-dong-tv.md:398`** (khối lượng dữ liệu — lý do không dựng được ca 10.000 dòng)
```
**Volume & Growth:** ~1,000 records/năm.
```

**`srs-v3.5.md:6760`** (Phụ lục E §H8 — **nguồn của vế `DIFF`**, trích trọn)
```
| **H8** | Tên tệp xuất thống nhất | Áp cho **tệp kết xuất dữ liệu** phần mềm sinh ra theo yêu cầu người dùng (xuất danh sách, xuất báo cáo), ở **mọi nhóm chức năng**. **Không áp** cho tệp mẫu nhập liệu tải sẵn (vd "Tải mẫu điểm danh"), tệp người dùng tải lên và tệp đính kèm — các loại này giữ tên gốc theo quy ước riêng của từng FR. **Khuôn:** `{TenTep}[_{DinhDanh}]_{YYYYMMDD_HHmm}.{đuôi}`. `{TenTep}` viết liền kiểu PascalCase, bỏ dấu tiếng Việt và bỏ mọi ký tự không phải chữ hoặc số (kể cả dấu gạch nối, dấu cách, dấu câu); dấu gạch dưới chỉ dùng để ngăn các đoạn. `{DinhDanh}` là đoạn tuỳ chọn khi tệp gắn với một bản ghi cụ thể — phải lấy từ một trường **đã khai trong entity** của bản ghi đó và áp cùng quy tắc ký tự. Phần giờ-phút bắt buộc để xuất hai lần trong cùng ngày không đè tệp. Tổng độ dài tối đa **255 ký tự**; vượt thì cắt bớt `{TenTep}`, không cắt phần thời gian. Trùng tên (hai lần xuất trong cùng phút) thì tự thêm hậu tố `_1`, `_2` — theo cách đã dùng cho tệp tải lên tại `srs-fr-02-hoi-dap.md:108`. `[BA chốt 2026-08-06 — nâng phạm vi quyết định 2026-08-04 của Nhóm IX thành quy ước chung]` | BẮT BUỘC |
```
> "**xuất danh sách**" + "**ở mọi nhóm chức năng**" ⇒ tệp của phiếu này **thuộc phạm vi H8**. Khuôn đối tác kỳ vọng vi phạm ba điểm: chữ thường (không PascalCase) · dấu gạch nối trong `{TenTep}` · dấu gạch nối giữa ngày và giờ (H8 dùng `_`).

**`srs-v3.5.md:6762`** (điều khoản xử lý khi FR lệch quy ước §H)
```
**Tham chiếu chéo:** Các FR/SCR có quy ước UI riêng phải cross-ref về Phụ lục E §H thay vì viết lại; nếu lệch quy ước H1–H8 phải ghi rõ lý do nghiệp vụ tại FR đó.
```
> `srs-fr-14-hop-dong-tv.md` **không** ghi bất kỳ lý do nghiệp vụ nào để lệch H8 ⇒ H8 áp nguyên vẹn cho nhóm X.3.

**`srs-fr-11-bao-cao.md:85`** (tiền lệ: nhóm khác đã áp H8 cho tệp .xlsx)
```
| 7 | Nếu xuất Excel: tạo file .xlsx (khổ A4, Times New Roman cỡ 13). Tên tệp `{TenBaoCao}_{YYYYMMDD_HHmm}.xlsx` theo **Phụ lục E §H8**; `{TenBaoCao}` là tên loại báo cáo `[BA chốt 2026-08-04, nâng thành quy ước chung 2026-08-06]` | — |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:131` ("Kiểm tra quyền **CB NV**") và `:184` (AC nêu đích danh CB NV). Nút Xuất Excel ở `:286` không ghi điều kiện vai trò riêng, nhưng bước xử lý đầu tiên đã chốt vai trò | `:131`, `:184` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234`. Ghi rõ **đơn vị** của tài khoản — cần cho phần phân quyền dữ liệu của C1 | brief §3 |
| **Dữ liệu — quyết định C1** | **≥4 hợp đồng** trong phạm vi, trong đó bộ lọc sắp dùng chỉ khớp **≈2**. Có cả bản ghi **bị loại** mới chứng minh được "áp bộ lọc"; xuất khi không lọc gì thì C1 **không đo được** | `:132`, `:133` |
| **Thứ tự thao tác** | Bước J bắt **"Tìm kiếm hợp lệ" trước rồi mới "Xuất Excel"** — xuất khi chưa lọc là sai kịch bản | bước J của phiếu |
| **Công cụ đọc tệp** | Mở tệp bằng `openpyxl` để đếm dòng + đọc tiêu đề cột + đọc mã hợp đồng. **Ảnh chụp màn hình tải tệp KHÔNG thay được việc mở tệp** | brief §4.8 |
| **Lấy tên tệp thật** | Đọc tên tệp do máy chủ trả (tiêu đề `Content-Disposition` của chính request tải, hoặc tên tệp lúc trình duyệt lưu). **Không** dùng tên do mình đặt lại khi lưu | `:135` |
| **Lưu giữ tệp** | Verdict phụ thuộc nội dung tệp ⇒ phải **giữ lại tệp** hoặc bản kê nội dung truy lại được | flow 04 §Chạy bước 8 |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **"Tệp tải về được" = đạt.** Mã phản hồi thành công + tệp nhị phân chỉ chứng minh **tạo được tệp**, không chứng minh **nội dung đúng**. Bắt buộc mở bằng `openpyxl`.
- **Xuất khi chưa lọc gì.** Tệp sẽ chứa toàn bộ dữ liệu và "trông đúng" — nhưng C1 chấm **áp bộ lọc**, ca này không đo được gì.
- **Đếm dòng gộp cả dòng tiêu đề.** Lệch 1 dòng dễ làm số "khớp" giả. Đếm riêng dòng tiêu đề và dòng dữ liệu, so với số bản ghi đang hiển thị.
- **So số lượng mà không so danh tính.** Trùng số dòng nhưng khác bản ghi vẫn là sai bộ lọc. Phải so **mã hợp đồng từng dòng**.
- **Kết luận C4 "đạt" vì tên tệp trùng đúng kỳ vọng đối tác.** C4 đã khóa `DIFF` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Trùng kỳ vọng đối tác nghĩa là **lệch §H8**; vẫn CẤM Pass, ghi hiện trạng + câu hỏi BA.
- **Kết luận C2 "đạt" vì cột trong tệp giống hệt màn danh sách.** C2 đã khóa `GAP` vì chính đặc tả ghi "cần CĐT xác nhận template". Không Pass.

**Dễ Fail oan:**
- **Fail C4 vì tên tệp không giống khuôn đối tác.** Đó chính là điểm `DIFF` — tên tệp theo §H8 (vd `HopDongTuVan_20260807_1432.xlsx`) là **đúng đặc tả**. Không Fail, chuyển BA.
- **Fail C2 vì tệp thiếu/thừa cột.** Đặc tả tự khai chưa chốt cấu trúc cột. Không Fail, chuyển BA.
- **Fail vì tệp không có cột "Hành động".** Cột này là nút thao tác trên màn (`:288`), không phải dữ liệu; `:147`–`:155` không có nó.
- **Fail C3 vì không thử được 10.000 dòng.** Môi trường chỉ có cỡ ~1.000 bản ghi/năm (`:398`). **Cấm** seed 10.000 bản ghi chỉ để thử ngưỡng — ghi rõ giới hạn hiệu lực của phép đo.
- **Fail vì tệp không theo khổ A4 / phông Times New Roman 13.** Yêu cầu đó thuộc **nhóm báo cáo** (`srs-fr-11-bao-cao.md:85`), **không** được khai cho nhóm X.3. Đây là xuất danh sách, không phải văn bản hành chính.
- **Fail vì thiếu cột "trạng thái" mà bước 2 (`:132`) có nhắc.** Bộ lọc trạng thái **không tồn tại** trong Inputs FR-X.3-02 (`:216`–`:219`) — lệch nội bộ của đặc tả, đưa vào câu hỏi BA.
