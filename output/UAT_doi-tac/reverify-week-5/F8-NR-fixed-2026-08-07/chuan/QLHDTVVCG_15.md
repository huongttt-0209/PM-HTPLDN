# QLHDTVVCG_15 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 321 · **Mô tả (G):** Thêm hợp đồng thành công
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "+ Thêm hợp đồng" · 3. Nhập thông tin hợp lệ và nhấn Lưu
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — FR-X.3-01 (Processing / Postconditions / Error Handling / AC)

> 🔴 **Phiếu này có 1 vế `DIFF` → CẤM Pass toàn phiếu, kết luận Cần BA** (flow 04 §Verdict + §Ca biên).

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Sinh mã hợp đồng **HDTV-{YYYYMMDD}-{số thứ tự}**" | `srs-fr-14-hop-dong-tv.md:81`, `:119`, `:514` | **MATCH** | TEST | **UI:** lưu hợp đồng mới → đọc `innerText` mã hợp đồng vừa sinh, đối chiếu khuôn `HDTV-` + ngày hôm nay dạng `YYYYMMDD` + số thứ tự. **Đối chứng:** đọc lại bản ghi qua API, so `ma_hop_dong` lưu trong dữ liệu với chuỗi hiển thị |
| **C2** | "…tạo bản ghi hợp đồng **cùng toàn bộ mốc tiến độ, thanh toán giai đoạn, liên kết vụ việc, tệp đính kèm đã nhập**" | `srs-fr-14-hop-dong-tv.md:122`, `:123`, `:92`, `:159`–`:161` | **MATCH** | TEST | **UI:** trước khi lưu, nhập **≥1 mốc + ≥1 giai đoạn thanh toán + ≥1 vụ việc liên kết + ≥1 tệp đính kèm**; sau khi lưu, mở lại chi tiết hợp đồng và đếm từng nhóm. **Đối chứng:** đọc lại bản ghi qua API, đếm phần tử trong `moc_tien_do`, `thanh_toan_giai_doan`, danh sách vụ việc, danh sách tệp — so với số đã nhập |
| **C3** | "…gán trạng thái **"Đang thực hiện"**" | `srs-fr-14-hop-dong-tv.md:396` (mặc định `'DANG_THUC_HIEN'`) + `:464` | **MATCH** | TEST | **UI:** đọc `innerText` ô Trạng thái của hợp đồng vừa tạo. **Đối chứng:** API trả `trang_thai = DANG_THUC_HIEN` cho chính bản ghi đó |
| **C4** | "Hệ thống hiển thị thông báo **"Đã lưu hợp đồng"**" — chấm theo **hành vi**: có báo lưu thành công | `srs-fr-14-hop-dong-tv.md:173` (`INF-HDTV-01`, nguyên văn đúng chuỗi đối tác kỳ vọng) + `:187` | **MATCH** | TEST | **UI:** cài `MutationObserver` trên `document.body` **trước** khi bấm Lưu (CẤM lọc trùng) → bắt chữ hiện ra. **Đối chứng:** mã phản hồi của chính request lưu (thành công) gắn với cùng mốc thời gian |
| **C5** | "…và **quay về danh sách**" | `srs-fr-14-hop-dong-tv.md:175` — **BA chốt 2026-08-06 nói NGƯỢC LẠI**: nhóm X.3 **không có màn danh sách độc lập**, sau khi lưu **trả người dùng về ngữ cảnh đã mở biểu mẫu** | **DIFF** | **BA** | Chỉ đo hiện trạng để ghi dev đang theo phía nào (sau khi lưu, màn dừng ở đâu — đọc đường dẫn + tiêu đề màn). **CẤM Pass vế này kể cả khi web quay về danh sách đúng như đối tác mong đợi** |

### Câu bắt buộc cho vế `DIFF` (soạn sẵn)

> **CẦN BA CONFIRM:** đối tác kỳ vọng sau khi lưu hợp đồng mới thì hệ thống **quay về màn danh sách hợp đồng**; SRS quy định nhóm X.3 **không có màn danh sách độc lập**, sau khi lưu hệ thống **đóng biểu mẫu và trả người dùng về ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên) — `srs-fr-14-hop-dong-tv.md:175`, ghi chú `[BA chốt 2026-08-06]`; web/dev hiện tại **&lt;điền sau khi đo&gt;**.

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:119`** (Processing bước 2)
```
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
```

**`srs-fr-14-hop-dong-tv.md:122`**–**`:123`** (Processing bước 5, 6)
```
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
| 6 | Liên kết vụ việc: tạo liên kết many-to-many | — |
```

**`srs-fr-14-hop-dong-tv.md:92`** (Inputs — tệp đính kèm)
```
| 12 | file_dinh_kem | file[] | N | Upload nhiều file | — | người dùng upload |
```

**`srs-fr-14-hop-dong-tv.md:159`**–**`:162`** (Postconditions FR-X.3-01, trọn mục)
```
- HĐ được tạo/cập nhật/xóa mềm
- Mốc tiến độ và thanh toán giai đoạn được quản lý
- Liên kết vụ việc many-to-many
- AUDIT_LOG ghi nhận
```

**`srs-fr-14-hop-dong-tv.md:173`** (Error Handling — dòng thông tin I1)
```
| I1 | Lưu HĐ thành công (thêm mới hoặc chỉnh sửa) | INF-HDTV-01 | "Đã lưu hợp đồng" | INFO |
```
> Chuỗi trùng **từng chữ** với kỳ vọng đối tác ⇒ C4 `MATCH`.

**`srs-fr-14-hop-dong-tv.md:175`** (ghi chú BA — **nguồn của vế `DIFF`**)
```
> **Câu thông báo sau khi lưu + điều hướng** `[BA chốt 2026-08-06]`: dùng chung một câu `INF-HDTV-01` cho cả chế độ Thêm mới lẫn Chỉnh sửa. Nhóm X.3 **không có màn danh sách độc lập** (xem §3 — quyết định BA 11/05/2026), nên sau khi lưu hệ thống đóng biểu mẫu và trả người dùng về **ngữ cảnh đã mở nó** (Chi tiết Vụ việc hoặc Chi tiết Tư vấn viên) — đây là biến thể hợp lệ của Phụ lục E §H7 "Sau khi thêm mới quay về danh sách".
```

**`srs-fr-14-hop-dong-tv.md:187`** (Acceptance Criteria)
```
- **Given** CB NV lưu hợp đồng hợp lệ **When** ở chế độ Thêm mới hoặc Chỉnh sửa **Then** hiện thông báo `INF-HDTV-01` "Đã lưu hợp đồng" + đóng biểu mẫu, quay về ngữ cảnh đã mở nó
```

**`srs-fr-14-hop-dong-tv.md:396`** (thực thể `HOP_DONG_TU_VAN` — trạng thái)
```
| trang_thai | text | Y | CHECK IN ('DANG_THUC_HIEN','HOAN_THANH','HUY','TAM_DUNG') | 'DANG_THUC_HIEN' | Trạng thái |
```

**`srs-fr-14-hop-dong-tv.md:464`**
```
Trạng thái HĐ (`DANG_THUC_HIEN`, `HOAN_THANH`, `HUY`, `TAM_DUNG`) chỉ là status field đơn giản, không theo vòng đời phê duyệt.
```

**`srs-fr-14-hop-dong-tv.md:514`** (BR-DATA-04)
```
| **Phát biểu** | Các entity nghiệp vụ có mã tự sinh theo format `PREFIX-YYYYMMDD-SEQ` (VD: HDTV-20260325-001) |
```

**`srs-fr-14-hop-dong-tv.md:120`**–**`:121`** (hai kiểm tra hợp lệ phải vượt qua để "nhập thông tin hợp lệ")
```
| 3 | Kiểm tra: ngày bắt đầu <= ngày kết thúc | — |
| 4 | Kiểm tra: tổng thanh toán giai đoạn <= giá trị HĐ | — |
```

**`srs-v3.5.md:6759`** (Phụ lục E §H7 — quy ước chung mà `:175` tự nhận là "biến thể hợp lệ")
```
| **H7** | Sau khi thêm mới quay về danh sách | Sau khi thực hiện thành công thao tác Thêm mới một bản ghi, hệ thống chuyển hướng về trang Danh sách (SCR-XX-01) kèm toast thông báo. Trừ trường hợp đối tác/CĐT yêu cầu giữ lại trang Chi tiết bản ghi vừa tạo (vd. cần thao tác liên hoàn — phải có ghi chú riêng tại FR cụ thể). | BẮT BUỘC |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68` (CB NV — CRUD đầy đủ), `:286` (nút thêm chỉ hiện với CB NV), `:290` (chỉ CB NV vào trang biểu mẫu) | `:68`, `:286`, `:290` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu đầu vào (bắt buộc để C2 đo được)** | Trước khi bấm Lưu phải nhập đủ **4 nhóm phụ**: ≥1 **mốc tiến độ** (Tên mốc + Ngày dự kiến — hai trường bắt buộc theo `:99`, `:100`), ≥1 **giai đoạn thanh toán** (Giai đoạn + Số tiền — `:109`, `:110`), ≥1 **vụ việc liên kết**, ≥1 **tệp đính kèm**. Thiếu nhóm nào thì phần đó của C2 **không đo được** → ghi Chưa chốt phần đó | `:122`, `:123`, `:92` |
| **Tiền đề của vụ việc liên kết** | Cần **≥1 vụ việc** trong phạm vi đơn vị để chọn. Không có ⇒ phải seed vụ việc trước, hoặc chạy `_22` trước rồi dùng lại (xem thứ tự chạy ở `00-TONG-HOP-QLHDTVVCG.md`) | `:123` |
| **Tệp đính kèm** | Phải là **tệp thật đúng định dạng** (pdf/docx/xlsx/png hợp lệ). **CẤM** tạo tệp văn bản rồi đổi đuôi | brief §4.6 |
| **Giá trị nhập phải hợp lệ** | Thời hạn bắt đầu ≤ kết thúc (`:120`) và **tổng số tiền các giai đoạn ≤ giá trị hợp đồng** (`:121`). Vi phạm sẽ bị chặn lưu và phiếu không đo được | `:120`, `:121` |
| **Khai báo seed** | Việc lưu hợp đồng mới **là thay đổi môi trường chung** ⇒ báo cáo phải khai: mã hợp đồng đã tạo · các bản ghi con · env nội bộ | brief §4.5 |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Lưu xong thấy thông báo là kết luận đạt.** C2 là vế nặng nhất: 4 nhóm con phải **thực sự được lưu**. Rất hay gặp ca giao diện nhận dữ liệu con nhưng máy chủ chỉ lưu phần Thông tin chung. **Bắt buộc mở lại bản ghi sau khi lưu và đếm**, không tin màn hình ngay sau khi bấm.
- **Đếm nhóm con ngay trên biểu mẫu chưa tải lại.** Các dòng vừa nhập vẫn nằm trong bộ nhớ trình duyệt. Phải tải lại / mở lại chi tiết rồi mới đếm, và đối chứng bằng bản ghi đọc qua API.
- **Mã hợp đồng "trông đúng khuôn" nhưng ngày sai.** `:81` đòi `HDTV-{YYYYMMDD}-{SEQ}`. Kiểm cả phần ngày phải là **ngày tạo**, không phải ngày bắt đầu hợp đồng hay ngày cố định.
- **Trạng thái hiển thị "Đang thực hiện" nhưng dữ liệu lưu khác.** Giao diện có thể hiển thị mặc định cứng. Bắt buộc đối chứng `trang_thai` qua API.
- **Thông báo tự tắt đã trượt.** `INF-HDTV-01` severity `INFO` ⇒ thường tự tắt sau vài giây. Poll DOM muộn → kết luận sai "im lặng". Cài `MutationObserver` **trước** khi bấm Lưu.
- **Kết luận C5 "đạt" vì web quay về danh sách đúng ý đối tác.** C5 đã khóa `DIFF` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Dù web làm đúng y kỳ vọng đối tác, vẫn **CẤM Pass**; ghi hiện trạng + câu hỏi BA.

**Dễ Fail oan:**
- **Fail C5 vì sau khi lưu không quay về danh sách.** Đó chính là điểm `DIFF`: `:175` nói phải trả về **ngữ cảnh đã mở biểu mẫu**, không phải danh sách. **Không Fail**, chuyển BA.
- **Fail vì câu chữ thông báo lệch.** Chấm theo **hành vi** (có báo lưu thành công). Chữ khác nhỏ ("Lưu hợp đồng thành công"…) ⇒ không Fail; ghi chênh lệch câu chữ cho BA. Lưu ý `:173` dùng **chung một câu** cho cả Thêm mới lẫn Chỉnh sửa — thấy cùng một chữ ở hai chế độ là **đúng**.
- **Fail vì nhãn hiển thị trạng thái không đúng chữ "Đang thực hiện".** Đặc tả khai **giá trị** `DANG_THUC_HIEN` (`:396`) nhưng **không có bảng ánh xạ mã → nhãn tiếng Việt cho hợp đồng** (bảng §B ở `srs-fr-05-vu-viec.md:1490`–`:1566` chỉ có vụ việc, cảnh báo, ưu tiên, kênh tiếp nhận, quy mô DN, loại đối tượng, loại tài liệu). Nhãn khác chữ ⇒ ghi cho BA. **Nhưng** nếu màn hiện thẳng mã `DANG_THUC_HIEN` thì **là lỗi** — vi phạm `srs-fr-05-vu-viec.md:1492`.
- **Fail vì phải qua bước phê duyệt.** `:302` và `:462` ghi rõ nhóm X.3 **KHÔNG cần phê duyệt, chỉ CRUD thuần** ⇒ lưu xong là xong.
- **Fail vì số thứ tự trong mã không bắt đầu từ 001.** `:514` chỉ nêu khuôn `PREFIX-YYYYMMDD-SEQ` với ví dụ; không quy định giá trị khởi đầu hay số chữ số.
