# QLHDTVVCG_03 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 309 · **Mô tả (G):** Tìm kiếm có kết quả
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công · 2. Tồn tại bản ghi phù hợp
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhập tiêu chí tìm kiếm · 3. Nhấn "Tìm kiếm"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` (FR-X.3-02 — Tìm kiếm hợp đồng tư vấn, UC159e)

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Có kết quả, hệ thống hiển thị danh sách hợp đồng phù hợp trên bảng kết quả." | `srs-fr-14-hop-dong-tv.md:226`, `:227`, `:228`, `:255` | **MATCH** | TEST | **UI:** nhập 1 từ khóa lấy từ **mã HĐ** của một bản ghi có thật → bấm "Tìm kiếm" → bảng phải hiện đúng bản ghi đó và loại các bản ghi không khớp. **Đối chứng:** gọi thẳng API tìm kiếm với cùng từ khóa, so `total` + danh sách mã HĐ trong response với số dòng + mã HĐ đang hiển thị trên bảng |

> Cột K chỉ có **một** mệnh đề ⇒ khóa **đúng một vế**. Phạm vi dữ liệu theo đơn vị (BR-AUTH-08), phân trang, và các tiêu chí lọc khác (TVV, khoảng ngày) là **tiền đề / hành vi kế bên** — đặc tả có quy định nhưng cột K **không nhắc** ⇒ **không tách thành vế, không mở thêm phép đo** (flow 04 §BUG SCOPE LOCK luật 1 + 4).

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:226`** (Processing FR-X.3-02, bước 2)
```
| 2 | Tìm kiếm toàn văn trên tên HĐ, mã HĐ, bên B | — |
```

**`srs-fr-14-hop-dong-tv.md:227`** (bước 3)
```
| 3 | Áp dụng bộ lọc AND logic | — |
```

**`srs-fr-14-hop-dong-tv.md:228`** (bước 4)
```
| 4 | Phân trang và trả về | BR-DATA-07 |
```

**`srs-fr-14-hop-dong-tv.md:255`** (Acceptance Criteria FR-X.3-02)
```
- **Given** CB NV nhập từ khóa **When** tìm kiếm **Then** trả DS HĐ matching, phân trang
```

**`srs-fr-14-hop-dong-tv.md:216`** (Inputs FR-X.3-02 — trường keyword)
```
| 1 | keyword | text | N | Từ khóa (tên HĐ, mã HĐ, bên B) | — | người dùng nhập |
```

**`srs-fr-14-hop-dong-tv.md:203`** (Tác nhân FR-X.3-02)
```
- Cán bộ Nghiệp vụ, Cán bộ Phê duyệt (TW/BN/ĐP) — phạm vi theo đơn vị (BR-AUTH-08)
```

**`srs-fr-14-hop-dong-tv.md:234`–`:240`** (Outputs FR-X.3-02 — các cột bảng kết quả)
```
| 1 | ma_hop_dong | text | luôn | HDTV-{date}-{seq} |
| 2 | ten_hop_dong | text | luôn | — |
| 3 | ben_a | text | luôn | — |
| 4 | ben_b | text | luôn | — |
| 5 | gia_tri_hop_dong | money | luôn | format tiền VND |
| 6 | thoi_han_ket_thuc | date | luôn | dd/mm/yyyy |
| 7 | trang_thai | text | luôn | — |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ** (hoặc Cán bộ Phê duyệt) TW/BN/ĐP. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `srs-fr-14-hop-dong-tv.md:203` — FR-X.3-02 khai đúng hai vai này; TVV/CG cũng tìm được nhưng **chỉ trong HĐ của mình** (`:204`) nên không dùng để đo vế này | `:203`, `:204` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234`. TW để phạm vi dữ liệu rộng nhất, tránh "không có kết quả" do phân quyền chứ không do tìm kiếm | brief §3 |
| **Dữ liệu** | **≥2 hợp đồng** trong phạm vi đơn vị, trong đó **≥1 khớp** tiêu chí sẽ nhập và **≥1 không khớp** — cần cả hai để chứng minh bảng *lọc* chứ không phải *trả hết*. Điều kiện (H) của phiếu đã ghi "Tồn tại bản ghi phù hợp" | `:226` (tìm kiếm toàn văn), `:227` (AND logic) |
| **Tiêu chí nhập** | Dùng **mã HĐ** hoặc **tên HĐ** hoặc **bên B** — đúng 3 trường `:226` khai là vùng tìm toàn văn. Nhập tiêu chí ngoài 3 trường này rồi không ra kết quả **không phải** lỗi | `:216`, `:226` |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng. Đây là **tiền đề**, không phải vế chấm — ghi đường thực tế đã đi, không log bug riêng (xem câu hỏi BA gộp ở `00-TONG-HOP-QLHDTVVCG.md`).

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Bảng có dòng là kết luận đạt.** Nếu ô tìm kiếm không thực sự lọc (bấm "Tìm kiếm" mà danh sách giữ nguyên toàn bộ), bảng vẫn "có kết quả" và vẫn "hiển thị danh sách hợp đồng". Phải có **≥1 bản ghi không khớp bị loại** mới chứng minh được — đây là lý do tiền đề đòi ≥2 bản ghi.
- **Từ khóa quá chung.** Gõ chuỗi khớp mọi bản ghi (vd "HDTV") → không phân biệt được lọc thật hay không lọc. Chọn chuỗi chỉ khớp đúng 1 bản ghi.
- **Kết quả cũ còn trên màn.** Bảng có thể là kết quả của lần lọc trước. Đối chứng bằng API cùng tham số, so `total` — không đếm bằng mắt.
- **Đếm nhầm số dòng.** Đếm gộp thẻ bọc ngoài với thẻ con của bảng AntD → số nhân đôi. Đếm bằng selector dòng cụ thể và đối chiếu `total` từ API.

**Dễ Fail oan:**
- **Fail vì tìm kiếm không khớp trường ngoài đặc tả.** `:226` chỉ khai toàn văn trên **tên HĐ, mã HĐ, bên B**. Gõ tên tư vấn viên, ghi chú, nội dung HĐ mà không ra kết quả là **đúng** đặc tả — TVV có bộ lọc riêng (`:217`), không nằm trong ô từ khóa.
- **Fail vì phải bấm nút "Tìm kiếm".** `:287` ghi hành vi thanh lọc là `change -> filter` (lọc ngay khi đổi giá trị). Nếu màn lọc tức thì và không có nút riêng, đó không phải lỗi — miễn là kết quả đúng.
- **Fail vì thiếu cột `trang_thai`.** Bảng kết quả tìm kiếm ở `:240` có cột Trạng thái, còn bảng danh sách ở `:288` thì không — **hai bảng của chính đặc tả lệch nhau**. Vế C1 chỉ chấm "có hiển thị danh sách hợp đồng phù hợp", không chấm bộ cột ⇒ không Fail vì lý do này; đưa vào câu hỏi BA gộp.
- **Fail vì kết quả ít hơn mong đợi do phân quyền.** BN/ĐP chỉ thấy dữ liệu đơn vị mình (`srs-v3.5.md:1376`–`:1377`). Nếu đo bằng tài khoản BN/ĐP mà thiếu bản ghi của đơn vị khác thì đó là **đúng** đặc tả.
