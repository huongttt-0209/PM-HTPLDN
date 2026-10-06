# QLHDTVVCG_18 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 324 · **Mô tả (G):** Xóa — **Có vụ việc liên kết**
**Điều kiện (H):** 1. Đăng nhập hệ thống thành công · 2. **Có vụ việc liên kết**
**Bước (J):** 1. Chọn menu "Hợp đồng Tư vấn" · 2. Nhấn "Xóa" và xác nhận
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` — FR-X.3-01 Processing + Error Handling + AC

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **chặn thao tác**…" | `srs-fr-14-hop-dong-tv.md:124`, `:183`, `:299` + `:171` (severity `ERROR`) | **MATCH** | TEST | **UI:** trên hợp đồng **có ≥1 vụ việc liên kết**, bấm Xóa → xác nhận → bản ghi phải **vẫn còn** trong danh sách. **Đối chứng:** gọi API đọc lại bản ghi đó — phải **chưa** có cờ đã xóa (chứng minh máy chủ cũng chặn, không chỉ giao diện) |
| **C2** | "…và hiển thị thông báo **"Không thể xóa hợp đồng đang có vụ việc liên kết"**" — chấm theo **hành vi**: có báo lý do từ chối | `srs-fr-14-hop-dong-tv.md:171` (`ERR-HDTV-04`, nguyên văn đúng chuỗi đối tác kỳ vọng) + `:183` | **MATCH** | TEST | **UI:** cài `MutationObserver` trên `document.body` **trước** khi bấm xác nhận (CẤM lọc trùng) → bắt chữ hiện ra. **Đối chứng:** mã phản hồi của chính request xóa (bị từ chối) gắn cùng mốc thời gian |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:171`** (Error Handling FR-X.3-01, dòng E4)
```
| E4 | Xóa HĐ có VV liên kết | ERR-HDTV-04 | "Không thể xóa hợp đồng đang có vụ việc liên kết" | ERROR |
```
> Chuỗi trùng **từng chữ** với kỳ vọng đối tác ⇒ C2 `MATCH`. Severity `ERROR` ⇒ chặn.

**`srs-fr-14-hop-dong-tv.md:124`** (Processing FR-X.3-01, bước 7)
```
| 7 | Xóa: chỉ khi KHÔNG có vụ việc liên kết, xóa mềm | BR-DATA-01 |
```

**`srs-fr-14-hop-dong-tv.md:183`** (Acceptance Criteria)
```
- **Given** CB NV xóa HĐ có VV liên kết **When** xác nhận **Then** từ chối + thông báo
```

**`srs-fr-14-hop-dong-tv.md:299`** (Quy tắc tương tác SCR-X3-01)
```
- Xóa HĐ: chỉ khi KHÔNG có vụ việc liên kết (soft delete)
```

**`srs-fr-14-hop-dong-tv.md:118`** (Processing bước 1 — ai được xóa)
```
| 1 | Kiểm tra quyền. CB NV: áp phân quyền đơn vị (BR-AUTH-08). TVV/CG: chỉ trả HĐ có `tu_van_vien_id` thuộc về user đang đăng nhập; chặn mọi thao tác Create/Update/Delete | BR-AUTH-01, BR-AUTH-08 |
```

**`srs-fr-14-hop-dong-tv.md:288`** (nút Xóa — chỉ CB NV thấy)
```
| 4 | content | Bảng hợp đồng | table | Mã HĐ (HDTV-{YYYYMMDD}-{SEQ}) / Tên HĐ / Bên A / Bên B / Giá trị (format tiền) / Thời hạn bắt đầu / Thời hạn kết thúc (đỏ nếu <= 30 ngày) / Số VV liên kết (badge) / Tiến độ TT (progress bar %) / Hành động (CB NV thấy Xem/Sửa/Xóa; TVV/CG CHỈ thấy nút Xem) | click -> action | luôn hiển thị |
```

**`srs-fr-14-hop-dong-tv.md:291`** (nơi nhìn thấy vụ việc liên kết để xác nhận tiền đề)
```
| 7 | content (form) | Accordion: Vụ việc liên kết | table + modal | Bảng VV liên kết: Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. Nút [+ Liên kết VV] -> modal multi-select. N:N | click -> action | trang thêm/sửa — chỉ CB NV |
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:68`, `:118` (TVV/CG bị chặn mọi thao tác xóa nên không dùng để đo), `:288`. Nếu đo bằng TVV/CG thì thao tác bị chặn **vì sai vai trò**, không phải vì có vụ việc liên kết ⇒ Pass oan | `:68`, `:118`, `:288` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234`. **KHÔNG** dùng `admin` để ra kết luận | brief §3 |
| **Dữ liệu — quyết định** | **1 hợp đồng CÓ ≥1 vụ việc liên kết** (cột "Số VV liên kết" ≥ 1, xác nhận bằng bảng ở `:291` **trước khi** bấm Xóa). Đây là điều kiện (H) của phiếu; dùng nhầm hợp đồng sạch liên kết sẽ rơi vào ca `_17` và cho kết quả ngược | `:124`, `:291` |
| **Xác nhận tiền đề trước khi đo** | **Bắt buộc mở nhóm "Vụ việc liên kết" đếm số dòng ≥1** và đối chứng qua API trước khi bấm Xóa. Tin vào con số badge ngoài danh sách là chưa đủ nếu badge tính sai | `:291`, `:154` |
| **Cách dựng nếu thiếu** | Chạy `_22` (liên kết vụ việc) trước để tạo tiền đề, hoặc dùng lại hợp đồng đã dựng cho `_09`. Khai vào báo cáo: hợp đồng nào · gắn vụ việc nào · env nội bộ | brief §4.5 |
| **Rủi ro dữ liệu** | Nếu hệ thống **không** chặn, hợp đồng sẽ bị xóa mềm thật ⇒ **không dùng hợp đồng quan trọng**; dùng hợp đồng QA tự dựng và ghi lại định danh để khôi phục/đối chứng | `:505` |

> 🔴 Đường vào màn: bước J ghi "Chọn menu Hợp đồng Tư vấn" nhưng `:266`–`:268` nói nhóm X.3 không có menu riêng ⇒ **tiền đề**, không phải vế chấm.

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Nút Xóa bị làm mờ/ẩn nên không bấm được → coi như "đã chặn".** Đó **không** đo được vế C1: cột K nói hệ thống **chặn thao tác và hiển thị thông báo**. Nếu không bấm được thì cũng không có thông báo ⇒ C2 không đo được. Ghi rõ hiện trạng và ghi **Chưa chốt** phần không đo được, thay vì Pass.
- **Chặn ở giao diện nhưng máy chủ vẫn cho xóa.** Phải đối chứng bằng cách đọc lại bản ghi qua API — còn nguyên, chưa có cờ xóa.
- **Tiền đề sai: hợp đồng thực ra không có vụ việc liên kết.** Khi đó hệ thống xóa thành công là **đúng** đặc tả, nhưng ta lại chấm Fail — hoặc tệ hơn, nếu hệ thống chặn nhầm thì ta Pass oan. Bắt buộc xác nhận ≥1 liên kết trước.
- **Thông báo tự tắt đã trượt** → kết luận sai "im lặng". Cài `MutationObserver` **trước** khi bấm xác nhận.
- **Đọc bằng `textContent`** → gom node ẩn của AntD, thấy chuỗi lỗi không thật sự hiển thị (bug ma ngược). Dùng `innerText`.

**Dễ Fail oan:**
- **Fail vì câu chữ không trùng từng ký tự.** Chấm theo **hành vi** (có chặn + có nêu lý do là do vụ việc liên kết). Chữ khác nhỏ ⇒ **không Fail**; ghi chênh lệch câu chữ cho BA.
- **Fail vì không hiện mã lỗi `ERR-HDTV-04`.** Mã là định danh nội bộ, đặc tả không đòi hiển thị cho người dùng.
- **Fail vì hệ thống chặn ngay khi bấm Xóa, chưa kịp hiện hộp xác nhận.** Cột K chỉ đòi "chặn thao tác + hiển thị thông báo"; chặn sớm hơn vẫn thoả. Bước J có ghi "và xác nhận" nhưng đó là mô tả thao tác, không phải yêu cầu phải có hộp xác nhận.
- **Fail vì thông báo hiển thị dạng hộp thoại thay vì chữ nổi.** Đặc tả chỉ ghi severity + nội dung, không quy định hình thức.
- **Fail vì sau khi bị chặn, màn không làm mới.** Cột K của phiếu này **không** nhắc tới làm mới danh sách (khác `_17`) ⇒ không thành tiêu chí chấm.
