# QLHDTVVCG_04 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 310 · **Mô tả (G):** Tìm kiếm không có kết quả
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công · 2. **Không tồn tại bản ghi phù hợp**
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhập tiêu chí tìm kiếm · 3. Nhấn "Tìm kiếm"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` (FR-X.3-02, bảng Error Handling)

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "…bảng dữ liệu để trống…" | `srs-fr-14-hop-dong-tv.md:251` (hệ quả trực tiếp của điều kiện "Không có kết quả") + `:228` | **MATCH** | TEST | **UI:** nhập chuỗi chắc chắn không khớp (vd `ZZZKHONGTONTAI`) → bảng phải **không còn dòng dữ liệu nào**. **Đối chứng:** gọi API tìm kiếm cùng từ khóa, xác nhận `total = 0` / mảng dữ liệu rỗng |
| **C2** | "…hệ thống hiển thị thông báo **"Không tìm thấy hợp đồng phù hợp"**." — chấm theo **hành vi**: có báo cho người dùng biết không có kết quả | `srs-fr-14-hop-dong-tv.md:251` (`INF-HDTV-TK-01` — nguyên văn đúng chuỗi đối tác kỳ vọng) | **MATCH** | TEST | **UI:** đọc `innerText` vùng trống của bảng + vùng thông báo ngay sau khi bấm tìm. **Đối chứng:** cài `MutationObserver` trên `document.body` **trước** thao tác (CẤM lọc trùng) để bắt cả thông báo dạng nổi tự tắt, đối chiếu với chữ đọc được ở trạng thái tĩnh |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:250`–`:251`** (Error Handling FR-X.3-02 — trọn bảng, 2 dòng)
```
| E1 | tu_ngay > den_ngay | ERR-HDTV-TK-01 | "Ngày bắt đầu phải trước ngày kết thúc" | ERROR |
| E2 | Không có kết quả | INF-HDTV-TK-01 | "Không tìm thấy hợp đồng phù hợp" | INFO |
```
> Chuỗi ở `:251` **trùng từng chữ** với kỳ vọng đối tác ⇒ quan hệ `MATCH`.

**`srs-fr-14-hop-dong-tv.md:258`** (Acceptance Criteria FR-X.3-02)
```
- **Given** không có kết quả **When** tìm kiếm **Then** hiển thị "Không tìm thấy hợp đồng" `[GAP-X.3-03]`
```
> ⚠️ Chính đặc tả ghi **hai chuỗi khác nhau**: `:251` có chữ "phù hợp", `:258` không có. Đây là lệch **câu chữ**, không lệch **hành vi** ⇒ xử theo mục (d) — chấm hành vi, không bắt trùng từng chữ.

**`srs-fr-14-hop-dong-tv.md:228`** (Processing FR-X.3-02, bước 4)
```
| 4 | Phân trang và trả về | BR-DATA-07 |
```

**`srs-fr-14-hop-dong-tv.md:244`** (Postconditions FR-X.3-02)
```
- Read-only, không thay đổi dữ liệu
```

**`srs-fr-05-vu-viec.md:1580`** (§D — trạng thái dữ liệu chung, dòng "Rỗng (cán bộ CMS)")
```
| Rỗng (cán bộ CMS) | Icon thư mục trống + chữ "Không có vụ việc nào trong phạm vi quản lý" |
```
> Quy ước chung §D chỉ khai **hình thức** trạng thái rỗng và câu chữ **của vụ việc**, không khai cho hợp đồng. Với hợp đồng, câu chữ chuẩn nằm ở `srs-fr-14-hop-dong-tv.md:251`. **Không** lấy dòng này áp cho HĐ.

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ** (hoặc Cán bộ Phê duyệt) TW/BN/ĐP. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `srs-fr-14-hop-dong-tv.md:203` | `:203` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Dữ liệu** | **Không cần seed.** Điều kiện (H) đòi "không tồn tại bản ghi phù hợp" — tạo bằng cách **nhập từ khóa vô nghĩa**, không cần xóa dữ liệu. ⚠️ Nên có **≥1 hợp đồng tồn tại** trong phạm vi để phân biệt "rỗng do lọc" với "rỗng do chưa có dữ liệu nào" (hai ca này có thể ra hai câu chữ khác nhau) | `:251` (điều kiện lỗi là "Không có kết quả" của phép tìm) |
| **Tiêu chí nhập** | Chuỗi vô nghĩa vào ô **từ khóa** (trường `keyword`, `:216`). Không dùng bộ lọc TVV/khoảng ngày cho vế này — giữ đúng một đường UI ngắn nhất | `:216`, `:226` |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bảng rỗng nhưng KHÔNG có thông báo → vẫn chấm đạt.** Cột K có **hai** mệnh đề. Bảng trống chỉ thoả C1. Thiếu chữ báo cho người dùng thì C2 **Fail**, cả phiếu **Reopen**.
- **Thông báo là loại tự tắt và đã trượt mất.** Chuỗi `INF-HDTV-TK-01` có severity `INFO` → nhiều khả năng là thông báo nổi tự tắt. Poll DOM sau vài giây sẽ **không thấy** và kết luận sai "im lặng". Bắt buộc cài `MutationObserver` **trước** khi bấm tìm.
- **Nhầm trạng thái rỗng mặc định với thông báo tìm kiếm.** Bảng chưa tìm gì đã sẵn chữ "Không có dữ liệu" thì chữ đó **không** chứng minh hệ thống phản hồi phép tìm. Phải so trước/sau thao tác.
- **Đọc bằng `textContent`.** Gom node ẩn của AntD → thấy chuỗi không thật sự hiển thị. Dùng `innerText`.

**Dễ Fail oan:**
- **Fail vì câu chữ không trùng từng ký tự.** Chính đặc tả đã lệch với chính nó: `:251` ghi "Không tìm thấy hợp đồng **phù hợp**", `:258` ghi "Không tìm thấy hợp đồng". Theo nguyên tắc *mô tả yêu cầu, không áp đặt cách làm*: chấm **có báo cho người dùng biết không tìm thấy hợp đồng** hay không. Chữ sai khác nhỏ (thiếu/thừa "phù hợp", thêm dấu chấm, đổi "hợp đồng nào") ⇒ **không Fail**; ghi nhận chênh lệch câu chữ vào phần cần BA chốt.
- **Fail vì thông báo hiển thị dạng khác.** Đặc tả chỉ ghi severity `INFO` + nội dung, **không** quy định là thông báo nổi, chữ trong lòng bảng, hay dòng dưới ô tìm kiếm. Mọi hình thức mà người dùng đọc được đều thoả.
- **Fail vì bảng vẫn còn phần khung/tiêu đề cột.** C1 đòi "bảng dữ liệu để trống" = không còn **dòng dữ liệu**, không đòi ẩn cả bảng.
- **Fail vì bộ đếm phân trang vẫn hiển thị "0".** `:228` yêu cầu phân trang; hiển thị "0 kết quả" là hợp lệ.
