# QLHDTVVCG_05 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 311 · **Mô tả (G):** Nhập khoảng ngày với ngày bắt đầu muộn hơn ngày kết thúc
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. nhập khoảng ngày với ngày bắt đầu muộn hơn ngày kết thúc · 3. Nhấn "Tìm kiếm"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — **FR-X.3-02 (tìm kiếm)**, KHÔNG phải FR-X.3-01 (biểu mẫu).

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **chặn thao tác**…" | `srs-fr-14-hop-dong-tv.md:250` (severity `ERROR`) + `:219` (ràng buộc `den_ngay >= tu_ngay`) | **MATCH** | TEST | **UI:** trên thanh lọc, đặt Từ ngày = `20/08/2026`, Đến ngày = `10/08/2026` → bấm "Tìm kiếm". Hệ thống phải **không thực hiện** phép tìm với khoảng ngày nghịch. **Đối chứng:** `list_network_requests` — không có request tìm kiếm nào rời đi với cặp tham số nghịch (hoặc nếu có, máy chủ trả lỗi chứ không trả danh sách) |
| **C2** | "…và hiển thị thông báo **"Ngày bắt đầu phải trước ngày kết thúc"**." — chấm theo **hành vi**: có báo lỗi cho người dùng | `srs-fr-14-hop-dong-tv.md:250` (`ERR-HDTV-TK-01` — nguyên văn đúng chuỗi đối tác kỳ vọng) | **MATCH** | TEST | **UI:** đọc `innerText` vùng lỗi cạnh ô ngày + vùng thông báo nổi. **Đối chứng:** cài `MutationObserver` trên `document.body` **trước** thao tác (CẤM lọc trùng) để bắt thông báo tự tắt |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:250`** (Error Handling **FR-X.3-02 — Tìm kiếm**, dòng E1)
```
| E1 | tu_ngay > den_ngay | ERR-HDTV-TK-01 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
```
> Chuỗi trùng **từng chữ** với kỳ vọng đối tác ⇒ `MATCH`. Severity `ERROR` ⇒ chặn, không phải cảnh báo mềm.

**`srs-fr-14-hop-dong-tv.md:218`–`:219`** (Inputs FR-X.3-02 — hai trường ngày)
```
| 3 | tu_ngay | date | N | — | — | người dùng chọn |
| 4 | den_ngay | date | N | >= tu_ngay | — | người dùng chọn |
```
> Ràng buộc là `den_ngay >= tu_ngay` ⇒ **hai ngày bằng nhau là HỢP LỆ**.

**`srs-fr-14-hop-dong-tv.md:287`** (thành phần thanh lọc SCR-X3-01 — nơi đặt cặp ngày này)
```
| 3 | filter-bar | Thanh lọc (UC159e) | form | Full-text: tên HĐ, mã HĐ, bên B. TVV (searchable). Khoảng ngày | change -> filter | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:169`** (Error Handling **FR-X.3-01 — biểu mẫu**, dòng E2 — *đây KHÔNG phải neo của phiếu này*)
```
| E2 | Ngày bắt đầu > ngày kết thúc | ERR-HDTV-02 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
```
> ⚠️ Trích ra đây **chỉ để cảnh báo nhầm lẫn**: hai mã lỗi khác nhau (`ERR-HDTV-02` cho biểu mẫu thêm/sửa, `ERR-HDTV-TK-01` cho thanh lọc) nhưng **câu chữ giống hệt**. Bước J của phiếu này là **thanh lọc** ⇒ neo đúng là `:250`.

**`srs-fr-14-hop-dong-tv.md:88`** (Inputs FR-X.3-01 — ràng buộc ngày trên biểu mẫu, để phân biệt)
```
| 8 | thoi_han_ket_thuc | date | Y | >= thoi_han_bat_dau | — | người dùng chọn |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ** (hoặc Cán bộ Phê duyệt) TW/BN/ĐP. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `srs-fr-14-hop-dong-tv.md:203` (tác nhân FR-X.3-02) | `:203` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu** | **Không cần seed.** Đây là kiểm tra hợp lệ đầu vào ở thanh lọc, chạy trước khi truy vấn (`:250` là điều kiện lỗi, không phụ thuộc dữ liệu) | `:250` |
| **Vị trí đo** | **Thanh lọc của màn danh sách** (`:287`), **KHÔNG** phải cặp ngày Thời hạn bắt đầu/kết thúc trong biểu mẫu thêm/sửa (`:290`). Đo nhầm chỗ ⇒ đang chấm `ERR-HDTV-02` chứ không phải `ERR-HDTV-TK-01` ⇒ phiếu hỏng | `:287` vs `:290` |
| **Giá trị nhập** | Từ ngày **muộn hơn hẳn** Đến ngày (cách nhau ≥10 ngày). Không dùng hai ngày bằng nhau — `:219` cho phép bằng nhau, dùng nó sẽ đo sai vế | `:219` |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Ô chọn ngày tự chặn nên không nhập nổi ca lỗi.** Nhiều bộ chọn khoảng ngày khoá sẵn ngày trước mốc bắt đầu → không tạo được ca nghịch bằng cách bấm lịch. Đó **không phải** bằng chứng "hệ thống đã chặn": phải nhập tay vào ô (gõ chuỗi ngày) hoặc dựng cặp tham số nghịch rồi kiểm phản hồi. Nếu tuyệt đối không tạo được ca nghịch qua UI, ghi **Chưa chốt** kèm lý do — **không** Pass bằng "không nhập được nên coi như đã chặn".
- **Thông báo tự tắt đã trượt.** Severity `ERROR` thường hiện dạng nổi ngắn. Poll DOM muộn → kết luận sai "im lặng". Cài `MutationObserver` **trước** thao tác.
- **Chặn ở giao diện nhưng máy chủ vẫn nhận.** C1 chỉ cần chặn ở một tầng, nhưng phải **chứng minh có chặn**: kiểm `list_network_requests` xem phép tìm với khoảng ngày nghịch có rời đi và có trả về danh sách hay không.
- **Đo nhầm trên biểu mẫu thêm/sửa** rồi thấy báo lỗi đúng chữ → Pass oan cho phiếu này (xem mục (c) "Vị trí đo").

**Dễ Fail oan:**
- **Fail vì câu chữ không trùng từng ký tự.** Chấm theo **hành vi** (có chặn + có báo lỗi). Chữ khác biệt nhỏ ("Từ ngày phải nhỏ hơn Đến ngày"…) ⇒ **không Fail**; ghi chênh lệch câu chữ vào phần cần BA chốt.
- **Fail vì không hiện đúng mã lỗi.** Đặc tả không đòi hiển thị mã `ERR-HDTV-TK-01` cho người dùng — mã là định danh nội bộ.
- **Fail vì hệ thống báo lỗi ngay khi đổi ngày, chưa cần bấm "Tìm kiếm".** `:287` khai hành vi thanh lọc là `change -> filter`; chặn sớm là chặt hơn, vẫn thoả "chặn thao tác".
- **Fail khi Từ ngày = Đến ngày.** `:219` ghi `>= tu_ngay` ⇒ **bằng nhau là hợp lệ**, hệ thống phải cho tìm. Nếu web chặn ca bằng nhau thì đó là lệch đặc tả theo hướng ngược lại — ghi nhận riêng theo gate "bug mới tự lộ", **không** dùng để Pass/Fail vế C1.
