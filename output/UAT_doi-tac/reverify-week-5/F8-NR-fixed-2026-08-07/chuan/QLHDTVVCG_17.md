# QLHDTVVCG_17 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 323 · **Mô tả (G):** Xóa — **Không có vụ việc liên kết**
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công · 2. **Không có vụ việc liên kết**
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "Xóa" và xác nhận
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — FR-X.3-01 Processing + BR-DATA-01 + BR-DATA-05

> 🔴 **Phiếu này có 2 vế `GAP` → CẤM Pass toàn phiếu, kết luận Cần BA** (dù C1/C2 đo đạt).

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống thực hiện **xóa mềm** (đánh dấu đã xóa, không xóa vật lý)" | `srs-fr-14-hop-dong-tv.md:124`, `:299`, `:182` + BR-DATA-01 `:505` | **MATCH** | TEST | **UI:** trên hợp đồng **không có vụ việc liên kết**, bấm Xóa → xác nhận → bản ghi biến khỏi danh sách. **Đối chứng:** gọi API đọc **đúng định danh** bản ghi đó — phải còn tồn tại với cờ đã xóa, **không** trả "không tìm thấy" kiểu đã xóa vật lý |
| **C2** | "…**lưu vết thao tác theo quy định**" | `srs-fr-14-hop-dong-tv.md:125`, `:162` + BR-DATA-05 `:522` | **MATCH** | TEST | **UI:** mở nhóm "Nhật ký" của hợp đồng (`:294`) hoặc màn nhật ký hệ thống, tìm bản ghi thao tác xóa vừa thực hiện. **Đối chứng:** đọc bản ghi nhật ký qua API — phải có mốc thời gian + người thực hiện + hành động xóa, gắn đúng hợp đồng vừa xóa |
| **C3** | "…hiển thị thông báo **"Đã xóa hợp đồng"**" | **IM LẶNG** — bảng Error Handling FR-X.3-01 `:166`–`:173` (đã đọc trọn, 6 dòng) **không có** thông báo cho thao tác xóa; bảng thông báo chung `srs-fr-05-vu-viec.md:1588`–`:1597` (đã đọc trọn) cũng **không có** câu xóa thành công | **GAP** | **BA** | Chỉ đo hiện trạng: cài `MutationObserver` **trước** thao tác, ghi lại nguyên văn chữ hệ thống hiện ra (hoặc ghi "không có chữ nào"). **CẤM Pass/Reopen vế này** |
| **C4** | "…và **làm mới danh sách**" | **IM LẶNG** — `:124` và `:299` chỉ khai điều kiện + xóa mềm, không khai hành vi màn hình sau khi xóa. Thêm nữa `:175` khẳng định nhóm X.3 **không có màn danh sách độc lập**, nên "danh sách" ở đây chưa xác định là màn nào | **GAP** | **BA** | Chỉ đo hiện trạng: sau khi xác nhận xóa, ghi lại màn dừng ở đâu và bản ghi còn hiển thị không. **CẤM Pass/Reopen vế này** |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:124`**–**`:125`** (Processing FR-X.3-01, bước 7 và 8)
```
| 7 | Xóa: chỉ khi KHÔNG có vụ việc liên kết, xóa mềm | BR-DATA-01 |
| 8 | Ghi nhật ký thao tác | BR-DATA-05 |
```

**`srs-fr-14-hop-dong-tv.md:166`**–**`:173`** (Error Handling FR-X.3-01 — **trọn bảng**, bằng chứng cho `GAP` của C3)
```
| # | Điều kiện lỗi | Mã lỗi | Phản hồi hệ thống | Severity |
|---|--------------|--------|-------------------|----------|
| E1 | Tên HĐ trống | ERR-HDTV-01 | "Tên hợp đồng là bắt buộc" | ERROR |
| E2 | Ngày bắt đầu > ngày kết thúc | ERR-HDTV-02 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
| E3 | Tổng thanh toán > giá trị HĐ | ERR-HDTV-03 | "Tổng thanh toán vượt giá trị hợp đồng" | ERROR |
| E4 | Xóa HĐ có VV liên kết | ERR-HDTV-04 | "Không thể xóa hợp đồng đang có vụ việc liên kết" | ERROR |
| E5 | Giá trị HĐ không hợp lệ | ERR-HDTV-05 | "Giá trị hợp đồng phải lớn hơn 0" | ERROR |
| I1 | Lưu HĐ thành công (thêm mới hoặc chỉnh sửa) | INF-HDTV-01 | "Đã lưu hợp đồng" | INFO |
```
> Có mã cho **xóa thất bại** (`E4`) và cho **lưu thành công** (`I1`), **không có** mã nào cho **xóa thành công** ⇒ C3 `GAP`.

**`srs-fr-05-vu-viec.md:1588`**–**`:1597`** (§E — bảng thông báo chung, **trọn bảng**, bằng chứng bổ sung cho `GAP` C3)
```
| Tình huống | Loại | Nội dung tiếng Việt |
|-----------|------|---------------------|
| Lưu thành công | Toast success | "Đã lưu thành công" |
| Lưu thất bại do lỗi mạng | Toast error | "Lưu thất bại. Vui lòng kiểm tra kết nối và thử lại." + nút [Thử lại] |
| Cập nhật thành công | Toast success | "Đã cập nhật thông tin vụ việc" |
| Hết phiên làm việc | Modal | "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." + nút [Đăng nhập] |
| Không có quyền truy cập | Toast error | "Bạn không có quyền thực hiện thao tác này" |
| Xóa hồ sơ | Confirm modal | Tiêu đề: "Xác nhận xóa vụ việc". Nội dung: "Bạn có chắc chắn xóa vụ việc {ma_vu_viec}? Hồ sơ sẽ được lưu trong thùng rác và quản trị viên có thể khôi phục." Nút: [Xóa] / [Hủy] |
| Xóa hàng loạt | Confirm modal | "Bạn sắp xóa {N} vụ việc. Tiếp tục?" |
| Xung đột optimistic lock | Modal | "Vụ việc đã được {ho_ten} cập nhật lúc {dd/mm HH:mm}. Vui lòng tải lại để xem thông tin mới nhất." + nút [Tải lại] |
```
> Bảng chung có **hộp xác nhận trước khi xóa** (và chỉ cho vụ việc), **không có** thông báo **sau khi xóa thành công** cho bất kỳ đối tượng nào.

**`srs-fr-14-hop-dong-tv.md:299`** (Quy tắc tương tác SCR-X3-01)
```
- Xóa HĐ: chỉ khi KHÔNG có vụ việc liên kết (soft delete)
```

**`srs-fr-14-hop-dong-tv.md:182`** (Acceptance Criteria)
```
- **Given** CB NV xóa HĐ không có VV liên kết **When** xác nhận **Then** soft delete
```

**`srs-fr-14-hop-dong-tv.md:159`** + **`:162`** (Postconditions)
```
- HĐ được tạo/cập nhật/xóa mềm
- AUDIT_LOG ghi nhận
```

**`srs-fr-14-hop-dong-tv.md:505`** (BR-DATA-01)
```
| **Phát biểu** | Mọi thao tác xóa đều là soft delete (set `is_deleted = 1`). Không xóa vật lý ngoại trừ purge theo policy retention |
```

**`srs-fr-14-hop-dong-tv.md:522`** (BR-DATA-05)
```
| **Phát biểu** | Mọi thao tác CUD + phê duyệt + đăng nhập/xuất đều ghi vào AUDIT_LOG. Log là immutable, không sửa/xóa |
```

**`srs-fr-14-hop-dong-tv.md:294`** (nơi đọc lưu vết trên giao diện)
```
| 10 | content (form) | Accordion: Nhật ký | timeline | Lịch sử CUD, mốc, thanh toán, liên kết VV | — | trang thêm/sửa (CB NV) hoặc xem chi tiết (TVV/CG xem được lịch sử của HĐ thuộc về mình) |
```

**`srs-fr-14-hop-dong-tv.md:288`** (nút Xóa nằm ở cột Hành động — chỉ CB NV thấy)
```
| 4 | content | Bảng hợp đồng | table | Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu <= 30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động (CB NV thấy Xem/Sửa/Xóa; TVV/CG CHỈ thấy nút Xem) | click -> action | luôn hiển thị |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68` (CB NV quyền CRUD **đầy đủ**), `:118` (TVV/CG bị **chặn mọi thao tác Create/Update/Delete**), `:288` (chỉ CB NV thấy nút Xóa). Ma trận quyền `srs-v3.5.md:1345` cũng cho CB_NV `CRUD*`, TVV/CG chỉ `R*` | `:68`, `:118`, `:288` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234`. **KHÔNG** dùng `admin` để ra kết luận — brief §3 cấm | brief §3 |
| **Dữ liệu — quyết định** | **1 hợp đồng KHÔNG có vụ việc liên kết nào** (cột "Số VV liên kết" = 0). Đây là điều kiện (H) của phiếu; dùng nhầm hợp đồng có liên kết sẽ rơi vào ca của phiếu `_18` và cho kết quả ngược | `:124`, `:299` |
| **Dữ liệu — dùng của QA** | **CẤM đụng dữ liệu đối tác.** Nếu không có hợp đồng "sạch liên kết" của QA thì tạo mới một hợp đồng tối thiểu rồi xóa nó. Khai vào báo cáo: mã hợp đồng đã tạo + đã xóa · env nội bộ | brief §4.5 |
| **Ghi lại định danh trước khi xóa** | Ghi **mã hợp đồng và định danh nội bộ** *trước* khi bấm Xóa — sau khi xóa mềm, bản ghi biến khỏi danh sách nên không tra ngược được nếu không có định danh. Thiếu bước này thì **C1 không đối chứng được** | `:505` |
| **Đọc lược đồ trước khi gọi API** | **Cấm đoán khóa JSON / đường dẫn.** Đọc `/api/docs-json` để biết cách tra bản ghi đã xóa mềm | brief §4.5 |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bản ghi biến khỏi danh sách = "đã xóa mềm".** Biến mất chỉ chứng minh **không còn hiển thị**. Xóa vật lý cũng cho đúng hiện tượng đó. **Bắt buộc** tra lại bản ghi theo định danh: còn tồn tại + có cờ đã xóa mới là xóa mềm; "không tìm thấy" là **Fail C1**.
- **Không ghi định danh trước khi xóa** → không tra được → buộc phải ghi Chưa chốt C1. Đây là lỗi quy trình hay gặp nhất ở phiếu xóa.
- **Nhật ký "có dòng nào đó" là đạt C2.** Phải là dòng **của chính thao tác vừa làm**: đúng hợp đồng, đúng người thực hiện, mốc thời gian khớp. Dòng nhật ký của thao tác tạo trước đó không tính.
- **Kết luận C3/C4 "đạt" vì web hiện đúng chữ "Đã xóa hợp đồng" và làm mới danh sách.** Hai vế đã khóa `GAP` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Trong tóm tắt phải nói rõ "web hiện tại **đúng kỳ vọng đối tác**" để người ngoài không đọc nhầm thành lỗi chưa xử lý; câu hỏi BA là **bổ sung điều này vào đặc tả**, không phải chặn bàn giao.
- **Thông báo tự tắt đã trượt** → kết luận sai "im lặng". Cài `MutationObserver` **trước** khi bấm xác nhận.

**Dễ Fail oan:**
- **Fail C3 vì không có chữ nào sau khi xóa.** Đặc tả **không** quy định thông báo xóa thành công — đây chính là `GAP`. Không Fail, chuyển BA.
- **Fail C4 vì màn không tự làm mới.** Đặc tả im lặng, lại còn nói nhóm X.3 không có màn danh sách độc lập (`:175`). Không Fail, chuyển BA.
- **Fail vì hộp xác nhận có câu chữ khác.** Đặc tả không khai câu xác nhận xóa cho hợp đồng; câu ở `srs-fr-05-vu-viec.md:1595` là **của vụ việc**, không áp cho hợp đồng.
- **Fail vì nút Xóa là biểu tượng thùng rác chứ không phải chữ "Xóa".** Phụ lục E §H6 (`srs-v3.5.md:6758`) bắt cột Hành động dùng **icon + tooltip** ⇒ icon là **đúng**.
- **Fail vì bản ghi vẫn còn trong dữ liệu.** Đó chính là **yêu cầu** của xóa mềm (`:505`) — còn dữ liệu mới đúng.
